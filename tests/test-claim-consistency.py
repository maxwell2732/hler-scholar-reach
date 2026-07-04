#!/usr/bin/env python3
"""Test for the claim consistency / prohibited-language scanner.

Runs .claude/skills/scholar-reach/scripts/check_claims.py against the
fixtures and asserts:
  1. bad_content.md   -> findings reported (exit 1), including hype
     terms, ledger-prohibited terms, [UNVERIFIED], and placeholders,
     each with file and line number;
  2. clean_content.md -> zero findings (exit 0);
  3. the scanner never modifies scanned files.

Stdlib only. Usage:  python tests/test-claim-consistency.py
"""

import os
import subprocess
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SCANNER = ROOT / ".claude" / "skills" / "scholar-reach" / "scripts" / "check_claims.py"
FIXTURES = ROOT / "tests" / "fixtures"
LEDGER = FIXTURES / "fixture_ledger.csv"
BAD = FIXTURES / "bad_content.md"
CLEAN = FIXTURES / "clean_content.md"

failures = []


def run_scanner(*args):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run(
        [sys.executable, str(SCANNER)] + list(args),
        capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT),
        env=env,
    )


def expect(condition, label):
    if condition:
        print("  PASS: %s" % label)
    else:
        print("  FAIL: %s" % label)
        failures.append(label)


print("== bad_content.md: violations must be reported ==")
before = BAD.read_bytes()
r = run_scanner("--ledger", str(LEDGER), str(BAD))
out = r.stdout
expect(r.returncode == 1, "exit code 1 on findings")
expect("bad_content.md:3" in out.replace("\\", "/") or "bad_content.md:3" in out,
       "file and line number reported (line 3)")
for term, label in [
    ("groundbreaking", "universal hype (en): groundbreaking"),
    ("proves", "universal hype verb (en): proves"),
    ("caused", "ledger prohibited (F01): caused"),
    ("颠覆性", "universal hype (zh): 颠覆性"),
    ("导致", "ledger prohibited (F01): 导致"),
    ("彻底解决", "universal hype (zh): 彻底解决"),
    ("widely adopted", "ledger prohibited (F02): widely adopted"),
    ("production-ready", "universal hype (en): production-ready"),
    ("成熟稳定", "ledger prohibited (F02): 成熟稳定"),
    ("国际领先", "universal hype (zh): 国际领先"),
    ("[UNVERIFIED]", "unverified marker"),
    ("TODO", "placeholder: TODO"),
]:
    expect(term in out, "reports term: %s" % label)
expect(BAD.read_bytes() == before, "scanner did not modify the file")

print("\n== clean_content.md: must produce zero findings ==")
r = run_scanner("--ledger", str(LEDGER), str(CLEAN))
expect(r.returncode == 0, "exit code 0 on clean file")
expect("no findings" in r.stdout, "reports 'no findings'")
# 'resolves' must not trip the whole-word 'solves' check
expect("resolves" not in r.stdout, "no false positive on 'resolves'")

print("\n== hype_zh_v02.md: v0.2 zh lexicons must be reported ==")
HYPE2 = FIXTURES / "hype_zh_v02.md"
r = run_scanner("--ledger", str(LEDGER), str(HYPE2))
out = r.stdout
expect(r.returncode == 1, "exit code 1 on v0.2 hype findings")
for term, label in [
    ("全网最强", "exaggeration: 全网最强"),
    ("科研神器", "exaggeration: 科研神器"),
    ("一键完成", "exaggeration: 一键完成"),
    ("爆火", "fake social proof: 爆火"),
    ("众多顶刊", "fake social proof: 众多顶刊"),
    ("广泛使用", "fake social proof: 广泛使用"),
    ("再不…就晚了", "anxiety marketing: 再不…就晚了"),
]:
    expect(term in out, "reports term: %s" % label)
# non-negated bare 保证 (保证获得引用) surfaces at least as context_review
expect("保证" in out, "bare 保证 surfaced for human review")

print("\n== negation_content.md: disclaimers and quoted mentions must NOT be violations ==")
NEG = FIXTURES / "negation_content.md"
r = run_scanner("--ledger", str(LEDGER), str(NEG))
out = r.stdout
expect(r.returncode == 0, "exit code 0 (no violations) on disclaimers/mentions")
expect("[violation]" not in out, "no [violation] finding on disclaimers/mentions")
# the scanner is honest about its limits: negated hits are surfaced as
# context_review rather than silently dropped
expect("context_review" in out, "negated 保证 surfaced as context_review, not hidden")
expect("quoted" in out, "quoted mention of 彻底解决/科研神器 downgraded with a 'quoted' note")

print("\n== directory mode ==")
r = run_scanner("--ledger", str(LEDGER), str(FIXTURES))
expect(r.returncode == 1, "directory scan finds bad files")

print("\n== claim traceability in dogfood zhihu/xiaohongshu outputs ==")
DOGFOOD_ZH = ROOT / "output" / "hler-scholar-reach" / "05_zh"
if DOGFOOD_ZH.is_dir():
    for name, marker in [
        ("zhihu_answer.md", "claims used"),
        ("zhihu_article.md", "claims used"),
        ("xiaohongshu_post.md", "claims used"),
        ("xiaohongshu_carousel.md", "claims_used"),
    ]:
        f = DOGFOOD_ZH / name
        if f.is_file():
            content = f.read_text(encoding="utf-8")
            expect(marker in content, "%s carries %s traceability" % (name, marker))
        else:
            expect(False, "%s exists in dogfood output" % name)
else:
    print("  SKIP: output/hler-scholar-reach/05_zh not present (dogfood not run)")

print()
if failures:
    print("claim-consistency test: %d FAILURE(S):" % len(failures))
    for f in failures:
        print("  - %s" % f)
    sys.exit(1)
print("claim-consistency test: all checks passed.")
