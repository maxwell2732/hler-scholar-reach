# Stage 9 — Integrity Review

Goal: cross-file consistency check over EVERYTHING generated for this
project. This is the last automated stage before final approval.

## Procedure

1. Run the scanner first:
   ```bash
   python .claude/skills/scholar-reach/scripts/check_claims.py \
     --ledger output/<project>/03_claims/claim_ledger.csv \
     output/<project>
   ```
   Its findings (prohibited language, `[UNVERIFIED]`, placeholders)
   seed the report; the manual checks below go beyond it.

2. Manual cross-file checks — for each, list every file checked and
   every discrepancy found (file, line, quote):

   | Check | What "consistent" means |
   |---|---|
   | Sample size | same N everywhere it appears |
   | Effect directions | no file reverses or strengthens a direction |
   | Publication/maturity status | identical status vocabulary everywhere |
   | DOI / links | one canonical link; no variant or dead-looking URLs |
   | Author list | same names, same order, correct characters/romanization |
   | zh–en claim equivalence | for each ledger claim used in both languages, the zh and en renderings have equal strength ("相关" ↔ "associated", never "导致" ↔ "associated") |
   | Causal drift | no file's wording exceeds its claim_type ceiling |
   | Software capability | no capability appears that isn't a `software_capability` row |
   | Version numbers | identical across release notes, posts, tutorials |
   | CTA validity | every CTA points at something that exists and works |
   | Placeholders | no `<...>`, `TODO`, `TBD`, `lorem`, `REPLACE-WITH` in content files |
   | `[UNVERIFIED]` | enumerate all remaining markers |
   | Traceability | every substantive assertion maps to a claim_id (check the `claims used` comments and spot-check content against them) |

3. Classify each finding: **blocking** (factual inconsistency, causal
   drift, unresolved `[UNVERIFIED]`, missing traceability) vs.
   **advisory** (style, redundancy).

4. Fix or flag: fixes that make wording MORE conservative or restore
   consistency with the ledger may be applied directly (log them in
   state.json `regeneration_log`). Anything that would strengthen a
   claim or change facts is flagged, never auto-fixed. Never overwrite
   a file whose state is `reviewed`/`approved` — propose a diff instead.

## Outputs

```
output/<project-name>/09_review/
├── consistency_report.md      # every check, result, evidence
├── unresolved_items.md        # blocking + advisory items still open
└── publication_readiness.md   # per-file verdict + overall verdict
```

`publication_readiness.md` overall verdict can be at most
"ready pending Gate 4" — never "publication-ready" (only Gate 4
approval grants that).

## Exit criteria

- all checks executed and reported (a skipped check is reported as
  skipped, with reason)
- blocking items either fixed (logged) or in unresolved_items.md
- state.json updated; **then run Human Gate 4**
  (`gates/gate-04-final-approval.md`)
