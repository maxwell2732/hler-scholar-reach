# Stage 3 — Claim Ledger

Goal: extract from the source materials the complete set of claims
that communication content is ALLOWED to use, each with its permitted
and prohibited phrasing in both languages. This is the system's core
control surface: later stages compose content only from ledger claims.

## Procedure

1. Re-read the primary sources (abstract/results for papers; README,
   docs, examples for repos). For each communicable assertion, create
   one ledger row using `templates/claim-ledger.csv` columns:

   | Column | Rule |
   |---|---|
   | `claim_id` | C01, C02, ... stable across regenerations |
   | `source_file` / `source_location` | precise enough to re-find (section, sentence, line) |
   | `original_evidence` | verbatim quote or exact numbers from the source |
   | `normalized_claim` | one neutral English sentence |
   | `claim_type` | from `references/claim-language-guide.md` |
   | `confidence` | low / medium / high — evidence strength, not enthusiasm |
   | `allowed_language_zh` / `_en` | semicolon-separated approved phrasings |
   | `prohibited_language` | semicolon-separated banned phrasings (zh+en) |
   | `qualifications` | conditions the claim carries (assumptions, subgroup, version) |
   | `limitations` | which stated limitations attach to this claim |
   | `human_approval_required` | `yes` for all causal claims, adoption metrics, publication status changes, and anything confidence=low |

2. Include as mandatory rows (when applicable):
   - one `publication_status` claim (papers) or maturity-status claim
     (repos, as `software_design_goal`/`descriptive`)
   - one `descriptive` claim covering sample/scope
   - each main finding / each demonstrated capability
   - each adoption metric the user supplied (with date)

3. Typing discipline:
   - Observational designs never yield `causal_experimental` rows.
   - A README sentence in future tense or "aims to" is
     `software_design_goal`, not `software_capability`.
   - Anything the authors hypothesize is `mechanism_hypothesized`.

4. When evidence is thin or ambiguous: downgrade the type, use
   conservative allowed language, set confidence=low,
   human_approval_required=yes. Never upgrade.

5. Write `claim_notes.md`: extraction decisions, borderline typings and
   why, claims deliberately EXCLUDED from communication (e.g.
   non-significant subgroup results likely to be misread) with reasons.

## Prohibited-language baseline

Every row's `prohibited_language` is in ADDITION to the universal
prohibited vocabulary in `references/claim-language-guide.md`, which
applies globally and is enforced by the scanner
(`.claude/skills/scholar-reach/scripts/check_claims.py`).

## Outputs

```
output/<project-name>/03_claims/
├── claim_ledger.csv
└── claim_notes.md
```

## Exit criteria

- CSV parses; all mandatory rows present; every causal row has
  human_approval_required=yes
- state.json updated; **then STOP for Human Gate 1**
  (`gates/gate-01-scientific-integrity.md`)
