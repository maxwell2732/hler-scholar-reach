# Paper example — Urban Green Space and Self-Reported Well-being

**Everything in this example is fictional.** It exists to demonstrate
one full pass of the scholar-reach workflow on a working paper with an
observational design — the case where causal-language drift is most
likely.

## The fictional artifact

- Title: *Urban Green Space and Self-Reported Well-being*
- Status: **working paper** (not peer-reviewed)
- Design: observational longitudinal study
- Main finding: greater access to green space was **associated with**
  higher self-reported well-being

## What this example demonstrates

1. The finding is never written as "green space **caused** better
   well-being" — see the `prohibited_language` column in
   [`output/03_claims/claim_ledger.csv`](output/03_claims/claim_ledger.csv).
2. Working-paper status appears in every content item —
   see [`output/06_en/linkedin_post.md`](output/06_en/linkedin_post.md)
   and [`output/05_zh/group_share_message.md`](output/05_zh/group_share_message.md).
3. Gate 1 asks the human to confirm concrete claims, and Gate 3 shows
   how a hype hit is handled — see [`output/gates/`](output/gates/).

## Files

```
input/working_paper_abstract.md      # the (fictional) source material
output/00_intake/campaign_brief.yaml
output/03_claims/claim_ledger.csv
output/03_claims/claim_notes.md
output/04_narrative/one_sentence_zh.md, one_sentence_en.md
output/05_zh/group_share_message.md
output/06_en/linkedin_post.md
output/gates/gate_01_scientific_integrity.md   # with a filled decision block (fictional reviewer)
output/gates/gate_03_no_hype.md                # one worked hype hit
```

A real run also produces the audit, audience matrix, full zh/en packs,
visual briefs, launch plan, and review reports; they are omitted here
to keep the example minimal.
