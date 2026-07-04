#!/usr/bin/env python3
"""Claim consistency / prohibited-language scanner for HLER Scholar Reach.

Scans Markdown files for:
  1. universal hype vocabulary (built-in, en + zh) — since v0.2 in four
     groups: exaggeration/absolutes, fake social proof, anxiety
     marketing, and legacy hype adjectives/verbs;
  2. per-claim prohibited language from a claim ledger CSV
     (column `prohibited_language`, `;`-separated);
  3. `[UNVERIFIED]` markers;
  4. placeholder residue (TODO, TBD, lorem, REPLACE-WITH, LINK-PENDING).

Findings carry a severity:
  - `violation`      — prohibited in publishable content;
  - `context_review` — pattern found in a context the scanner cannot
    judge (e.g. negation: "本项目不能保证获得引用" is a disclaimer,
    not hype), or an inherently ambiguous term (bare 保证). A human
    decides at Gate 3.

Negation handling (v0.2, best-effort): a hit preceded on the same line
by a nearby negation marker (不能/无法/不保证/does not/cannot/...) is
downgraded to context_review instead of reported as a violation. This
is a heuristic over single lines — it does NOT understand cross-sentence
scope, rhetorical negation ("不是不夸大"), or irony. Known limitation;
see gates/gate-03-no-hype.md.

The scanner REPORTS and never modifies files.
Exit codes: 0 = clean or context_review only; 1 = violations; 2 = usage
error.

Stdlib only. Usage:

    python check_claims.py [--ledger path/to/claim_ledger.csv] PATH [PATH...]

PATH may be a Markdown file or a directory (scanned recursively for
*.md). Gate files and claim_notes.md are exempt from hype-term hits
(they quote prohibited terms on purpose) but still checked for
placeholders.
"""

import argparse
import csv
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Lexicons. Keep in sync with references/claim-language-guide.md and
# gates/gate-03-no-hype.md when editing.
# ---------------------------------------------------------------------------

# Legacy universal hype (v0.1)
HYPE_EN = [
    "groundbreaking", "revolutionary", "unprecedented", "first-ever",
    "game-changing", "transformative", "world-leading",
    "paradigm-shifting", "battle-tested", "production-ready",
]
HYPE_EN_VERBS = ["solves", "proves", "prevents", "guarantees"]
HYPE_ZH = [
    "颠覆性", "革命性", "全球首个", "国际领先", "填补国际空白",
    "彻底解决", "完全证明", "杜绝", "必然导致",
]

# v0.2: exaggeration / absolutes (zh)
HYPE_ZH_EXAGGERATION = [
    "科研神器", "必备神器", "救命神器", "全网最强", "天花板", "封神",
    "一键完成", "零门槛", "无需任何基础", "必火", "爆款",
    "闭眼入", "闭眼用", "所有人都应该", "取代研究者", "取代专家",
    "保证发表", "保证引用", "保证涨粉", "绝了", "必看", "震惊",
]
# v0.2: fake social proof (zh) — allowed ONLY with verifiable ledger
# evidence, so default severity is violation.
HYPE_ZH_SOCIAL_PROOF = [
    "已被广泛使用", "广泛使用", "获得大量学者认可", "风靡学术圈",
    "最近爆火", "爆火", "全网都在用", "众多顶刊作者推荐", "众多顶刊",
]
# v0.2: anxiety marketing (zh) — phrase patterns, not single words.
HYPE_ZH_ANXIETY_RE = [
    (re.compile(r"再不(用|学|会).{0,10}就(晚了|来不及)"), "再不…就晚了"),
    (re.compile(r"不会用就落后"), "不会用就落后"),
    (re.compile(r"不(学|用)(就会|就)被淘汰"), "不学就会被淘汰"),
    (re.compile(r"必须掌握"), "必须掌握"),
]
# Bare 保证 is ambiguous (质量保证/不能保证) → context_review unless a
# stronger compound above already matched.
HYPE_ZH_AMBIGUOUS = ["保证"]

# Negation markers. If one appears within the window before a hit, the
# hit is downgraded to context_review.
NEG_ZH = ["不能", "不会", "无法", "不保证", "并未", "没有", "未被",
          "不得", "避免", "禁止", "不应", "不宜", "难以", "并非",
          "不是", "并不", "切勿", "从不"]
NEG_ZH_WINDOW = 8  # chars before the hit
NEG_EN_RE = re.compile(
    r"\b(not|no|never|cannot|can't|doesn't|does\s+not|won't|will\s+not|"
    r"without|refuses?\s+to)\b[^.;!?]{0,40}$", re.I)

PLACEHOLDER_PATTERNS = [
    (re.compile(r"\bTODO\b"), "placeholder: TODO"),
    (re.compile(r"\bTBD\b"), "placeholder: TBD"),
    (re.compile(r"\blorem ipsum\b", re.I), "placeholder: lorem ipsum"),
    (re.compile(r"REPLACE-WITH"), "placeholder: REPLACE-WITH"),
    (re.compile(r"LINK-PENDING"), "placeholder: LINK-PENDING"),
]
UNVERIFIED = re.compile(r"\[UNVERIFIED\]")


def load_ledger_terms(ledger_path):
    """Return list of (term, claim_id) from prohibited_language column."""
    terms = []
    with open(ledger_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or "prohibited_language" not in reader.fieldnames:
            sys.stderr.write(
                "error: ledger %s lacks a prohibited_language column\n" % ledger_path)
            sys.exit(2)
        for row in reader:
            cid = (row.get("claim_id") or "?").strip()
            raw = row.get("prohibited_language") or ""
            for term in raw.split(";"):
                term = term.strip()
                if term:
                    terms.append((term, cid))
    return terms


def is_cjk(term):
    return re.search(r"[一-鿿]", term) is not None


def find_positions(term, line):
    """Yield start positions of term in line (word-boundary for ASCII)."""
    if is_cjk(term):
        start = 0
        while True:
            idx = line.find(term, start)
            if idx < 0:
                return
            yield idx
            start = idx + 1
    else:
        for m in re.finditer(
                r"(?<![A-Za-z-])" + re.escape(term) + r"(?![A-Za-z-])",
                line, re.I):
            yield m.start()


QUOTE_CHARS = set('“‘「『"\'`')
QUOTE_WINDOW = 8  # chars; covers slash-separated mention lists like "神器/必备/震惊"


def negated(line, pos, cjk):
    """Best-effort negation check for a hit at line[pos]."""
    if cjk:
        # bare 不 immediately before the term ("不保证X") counts too
        if line[pos - 1:pos] == "不":
            return True
        window = line[max(0, pos - NEG_ZH_WINDOW):pos]
        return any(neg in window for neg in NEG_ZH)
    return NEG_EN_RE.search(line[:pos]) is not None


def quoted(line, pos):
    """True if an opening quote sits shortly before the hit — the term
    is likely being MENTIONED (rule text, examples of what to avoid,
    scanner documentation) rather than used. Downgraded, not ignored:
    a human still reviews it, because quotes can also carry hype."""
    window = line[max(0, pos - QUOTE_WINDOW):pos]
    return any(q in window for q in QUOTE_CHARS)


def classify(line, pos, cjk, base_severity="violation"):
    """Return (severity, note) for a hit at line[pos]."""
    if quoted(line, pos):
        return ("context_review",
                " (quoted — likely a mention of the term, verify)")
    if negated(line, pos, cjk):
        return ("context_review",
                " (negated context — verify it is a genuine disclaimer)")
    return (base_severity, "")


def add_hits(findings, path, lineno, line, term, category,
             base_severity="violation"):
    for pos in find_positions(term, line):
        severity, note = classify(line, pos, is_cjk(term), base_severity)
        findings.append((path, lineno, term, category + note, severity))


def scan_file(path, ledger_terms, hype_exempt):
    findings = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")
    for lineno, line in enumerate(text.splitlines(), start=1):
        if not hype_exempt:
            for term in HYPE_EN + HYPE_EN_VERBS:
                add_hits(findings, path, lineno, line, term, "hype (universal, en)")
            for term in HYPE_ZH:
                add_hits(findings, path, lineno, line, term, "hype (universal, zh)")
            for term in HYPE_ZH_EXAGGERATION:
                add_hits(findings, path, lineno, line, term, "hype (exaggeration, zh)")
            for term in HYPE_ZH_SOCIAL_PROOF:
                add_hits(findings, path, lineno, line, term,
                         "fake social proof (zh) — needs verifiable ledger evidence")
            for pattern, label in HYPE_ZH_ANXIETY_RE:
                for m in pattern.finditer(line):
                    severity, note = classify(line, m.start(), True)
                    findings.append((path, lineno, label,
                                     "anxiety marketing (zh)" + note, severity))
            for term in HYPE_ZH_AMBIGUOUS:
                # skip if part of a stronger compound already reported
                compounds = [t for t in HYPE_ZH_EXAGGERATION if term in t]
                for pos in find_positions(term, line):
                    if any(line[max(0, pos - 2):pos + len(c)].find(c) >= 0
                           for c in compounds):
                        continue
                    if negated(line, pos, True):
                        # negated disclaimer ("不能保证") — informational only
                        findings.append((path, lineno, term,
                                         "ambiguous (zh) — negated disclaimer",
                                         "context_review"))
                    else:
                        findings.append((path, lineno, term,
                                         "ambiguous (zh) — 保证 needs human judgment",
                                         "context_review"))
            for term, cid in ledger_terms:
                add_hits(findings, path, lineno, line, term,
                         "ledger prohibited (%s)" % cid)
            if UNVERIFIED.search(line):
                findings.append((path, lineno, "[UNVERIFIED]",
                                 "unverified marker", "violation"))
        for pattern, label in PLACEHOLDER_PATTERNS:
            if pattern.search(line):
                findings.append((path, lineno, pattern.pattern, label, "violation"))
    return findings


def collect_md_files(paths):
    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.is_file():
            files.append(p)
        else:
            sys.stderr.write("error: no such path: %s\n" % p)
            sys.exit(2)
    return files


def main(argv=None):
    # Emit UTF-8 regardless of platform locale (Windows defaults to a
    # legacy codepage when stdout is piped, which mangles Chinese terms).
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="+", help="Markdown files or directories")
    parser.add_argument("--ledger", help="claim_ledger.csv with prohibited_language")
    args = parser.parse_args(argv)

    ledger_terms = load_ledger_terms(args.ledger) if args.ledger else []
    all_findings = []
    files = collect_md_files(args.paths)
    for f in files:
        parts = {part.lower() for part in f.parts}
        hype_exempt = "gates" in parts or f.name.startswith("gate_") \
            or f.name == "claim_notes.md"
        all_findings.extend(scan_file(f, ledger_terms, hype_exempt))

    violations = [x for x in all_findings if x[4] == "violation"]
    reviews = [x for x in all_findings if x[4] == "context_review"]

    if not all_findings:
        print("check_claims: scanned %d file(s), no findings." % len(files))
        return 0

    print("check_claims: scanned %d file(s): %d violation(s), "
          "%d context_review item(s)\n"
          % (len(files), len(violations), len(reviews)))
    for path, lineno, term, category, severity in all_findings:
        print("  %s:%d  [%s] [%s]  %s" % (path, lineno, severity, category, term))
    print("\nNo files were modified. Route violations to "
          "gates/gate-03-no-hype.md for human decision; context_review "
          "items need a human glance but may be legitimate (e.g. "
          "disclaimers).")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
