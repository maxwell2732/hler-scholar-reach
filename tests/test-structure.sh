#!/usr/bin/env bash
# Structure test for HLER Scholar Reach.
# Checks required files/dirs exist, SKILL.md has valid frontmatter,
# and templates parse (JSON/CSV strictly; YAML strictly only if PyYAML
# is installed, otherwise a basic sanity check with a note).
# Usage: bash tests/test-structure.sh
set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT" || exit 2

# Find a python that actually runs (on Windows, `python3` may be a
# Microsoft Store stub that exists on PATH but cannot execute code).
PY=""
for cand in python3 python py; do
  if "$cand" -c "pass" >/dev/null 2>&1; then
    PY="$cand"
    break
  fi
done
if [ -z "$PY" ]; then
  echo "SKIP: no working python found; template parsing checks skipped." >&2
fi

fail=0
pass=0

check() { # check <path>
  if [ -e "$1" ]; then
    pass=$((pass + 1))
  else
    echo "FAIL: missing $1"
    fail=$((fail + 1))
  fi
}

# --- Required top-level files ---
for f in README.md README_EN.md LICENSE CHANGELOG.md CONTRIBUTING.md \
         CITATION.cff output/.gitkeep; do
  check "$f"
done

# --- Skill ---
check ".claude/skills/scholar-reach/SKILL.md"
check ".claude/skills/scholar-reach/scripts/check_claims.py"
check ".claude/skills/scholar-reach/references/file-map.md"
check ".claude/skills/scholar-reach/templates/file-map.md"

# SKILL.md frontmatter: first line ---, contains "name: scholar-reach"
if [ -f ".claude/skills/scholar-reach/SKILL.md" ]; then
  if head -n 1 ".claude/skills/scholar-reach/SKILL.md" | grep -q '^---$' \
     && grep -q '^name: scholar-reach$' ".claude/skills/scholar-reach/SKILL.md"; then
    pass=$((pass + 1))
  else
    echo "FAIL: SKILL.md frontmatter missing or name != scholar-reach"
    fail=$((fail + 1))
  fi
fi

# --- Stage prompts 00..09 ---
for p in 00-intake 01-artifact-audit 02-audience-strategy 03-claim-ledger \
         04-core-narrative 05-zh-content-pack 06-en-content-pack \
         07-visual-assets 08-launch-plan 09-integrity-review; do
  check "prompts/$p.md"
done

# --- Gates 01..04 ---
for g in gate-01-scientific-integrity gate-02-publication-rights \
         gate-03-no-hype gate-04-final-approval; do
  check "gates/$g.md"
done

# --- References ---
for r in artifact-types audience-taxonomy channel-profiles \
         claim-language-guide academic-integrity bilingual-localization; do
  check "references/$r.md"
done

# --- Templates exist ---
for t in campaign-brief.yaml artifact-manifest.yaml state.json \
         claim-ledger.csv audience-message-matrix.md launch-calendar.md \
         final-report.md zhihu-answer.md xiaohongshu-carousel.yaml; do
  check "templates/$t"
done

# --- v0.2: zhihu / xiaohongshu wiring ---
grep_check() { # grep_check <pattern> <file> <label>
  if grep -q "$1" "$2" 2>/dev/null; then
    pass=$((pass + 1))
  else
    echo "FAIL: $3 (pattern '$1' not found in $2)"
    fail=$((fail + 1))
  fi
}
grep_check '### `zhihu`' references/channel-profiles.md "channel profile: zhihu"
grep_check '### `xiaohongshu`' references/channel-profiles.md "channel profile: xiaohongshu"
grep_check 'zhihu_answer.md' prompts/05-zh-content-pack.md "stage 5 defines zhihu outputs"
grep_check 'xiaohongshu_carousel.md' prompts/05-zh-content-pack.md "stage 5 defines xiaohongshu outputs"
grep_check '知乎' README.md "README documents zhihu support"
grep_check '小红书' README.md "README documents xiaohongshu support"
grep_check 'Zhihu' README_EN.md "README_EN mentions Zhihu"
grep_check 'Xiaohongshu' README_EN.md "README_EN mentions Xiaohongshu"
grep_check 'requested_channels' templates/state.json "state.json has requested_channels"
grep_check 'channel_review_status' templates/state.json "state.json has channel_review_status"
grep_check 'platform_specific_risks' templates/state.json "state.json has platform_specific_risks"
check "tests/fixtures/hype_zh_v02.md"
check "tests/fixtures/negation_content.md"


# --- Examples & tests ---
check "examples/paper-example/README.md"
check "examples/paper-example/input/working_paper_abstract.md"
check "examples/paper-example/output/03_claims/claim_ledger.csv"
check "examples/repository-example/README.md"
check "examples/repository-example/input/clean-panel-README.md"
check "examples/repository-example/output/03_claims/claim_ledger.csv"
check "tests/fixtures/fixture_ledger.csv"
check "tests/test-claim-consistency.py"

# --- Template parsing ---
if [ -n "$PY" ]; then
  # JSON
  if "$PY" -c "import json,sys; json.load(open('templates/state.json', encoding='utf-8'))" 2>/dev/null; then
    pass=$((pass + 1))
  else
    echo "FAIL: templates/state.json is not valid JSON"
    fail=$((fail + 1))
  fi
  # CSV: header must contain required columns; consistent field counts
  if "$PY" - <<'EOF' 2>/dev/null
import csv, sys
required = {"claim_id","source_file","source_location","original_evidence",
            "normalized_claim","claim_type","confidence","allowed_language_zh",
            "allowed_language_en","prohibited_language","qualifications",
            "limitations","human_approval_required"}
for path in ["templates/claim-ledger.csv",
             "examples/paper-example/output/03_claims/claim_ledger.csv",
             "examples/repository-example/output/03_claims/claim_ledger.csv",
             "tests/fixtures/fixture_ledger.csv"]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    header = rows[0]
    missing = required - set(header)
    assert not missing, "%s missing columns: %s" % (path, missing)
    for i, row in enumerate(rows[1:], 2):
        assert len(row) == len(header), "%s row %d has %d fields, header has %d" % (path, i, len(row), len(header))
EOF
  then
    pass=$((pass + 1))
  else
    echo "FAIL: a claim ledger CSV failed to parse (run the heredoc manually for details)"
    fail=$((fail + 1))
  fi
  # Xiaohongshu carousel template: stable structure, all required keys
  # per card, 8 cards, limitation card present (stdlib line-based check;
  # PyYAML strict parse below when available)
  if "$PY" - <<'EOF' 2>/dev/null
import re, sys
text = open("templates/xiaohongshu-carousel.yaml", encoding="utf-8").read()
cards = re.findall(r"- page: (\d+)", text)
assert len(cards) == 8, "expected 8 cards, found %d" % len(cards)
for key in ["role:", "headline:", "body:", "suggested_visual:",
            "claims_used:", "prohibited_implications:", "alt_text:"]:
    n = len(re.findall(re.escape(key), text))
    assert n >= 8, "key %s appears %d times, expected >= 8" % (key, n)
assert "role: limitation" in text, "mandatory limitation card missing"
assert "card_count: 8" in text
EOF
  then
    pass=$((pass + 1))
  else
    echo "FAIL: templates/xiaohongshu-carousel.yaml structure check"
    fail=$((fail + 1))
  fi
  # YAML: strict parse if PyYAML available, else basic sanity
  if "$PY" -c "import yaml" 2>/dev/null; then
    if "$PY" -c "
import yaml
for p in ['templates/campaign-brief.yaml','templates/artifact-manifest.yaml','CITATION.cff']:
    yaml.safe_load(open(p, encoding='utf-8'))
" 2>/dev/null; then
      pass=$((pass + 1))
    else
      echo "FAIL: a YAML template failed to parse with PyYAML"
      fail=$((fail + 1))
    fi
  else
    ok=1
    for y in templates/campaign-brief.yaml templates/artifact-manifest.yaml CITATION.cff; do
      if [ ! -s "$y" ] || grep -qP '\t' "$y"; then
        echo "FAIL: $y empty or contains tabs (YAML sanity check)"
        ok=0
      fi
    done
    if [ $ok -eq 1 ]; then
      echo "NOTE: PyYAML not installed; YAML files passed basic sanity check only."
      pass=$((pass + 1))
    else
      fail=$((fail + 1))
    fi
  fi
fi

echo
echo "structure test: $pass passed, $fail failed"
[ $fail -eq 0 ] || exit 1
exit 0
