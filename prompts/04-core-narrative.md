# Stage 4 — Core Narrative

Goal: one narrative master, rendered at four lengths in two languages.
Every later channel adaptation derives from these files; facts may be
cut for length but never altered.

## Preconditions

- Claim ledger exists.
- Gate 1 status: if `approved`, compose normally. If still `pending`
  or `presented`, you MAY compose drafts, but every sentence resting on
  an unconfirmed claim carries an inline `[UNVERIFIED]` marker, and no
  file in this stage may omit the header
  `> STATUS: DRAFT — pending Gate 1 (scientific integrity)`.

## Narrative spine (answer in order, from ledger claims only)

1. What is the problem?
2. Why does it matter?
3. What is missing in existing work or tools?
4. What did this paper or repository do?
5. What are the main findings or capabilities? (cite claim_ids in an
   HTML comment after each finding: `<!-- C03 -->`)
6. What are the limitations?
7. What should the reader do next? (one CTA from the audience matrix)

## Renderings

| File | Length target | Notes |
|---|---|---|
| `one_sentence_{zh,en}.md` | 1 sentence | The single most defensible claim + artifact type/status |
| `elevator_pitch_{zh,en}.md` | ~30 sec spoken (60–90 words / 100–150 字) | Problem + contribution + status |
| `short_summary_{zh,en}.md` | 150–250 words / 300–500 字 | Spine points 1,4,5,6,7 |
| `long_narrative_{zh,en}.md` | 600–1000 words / 1200–2000 字 | Full spine |

## Composition rules

- zh and en are composed separately per
  `references/bilingual-localization.md`; numbers, claim strength,
  status, and the canonical link must be identical.
- Style: follow that file's "句式与标点：避免机器腔" section (no
  不是……而是……/"X, not Y" frames, no meta-discourse openers, dashes
  sparing and never two per sentence); self-check all 8 files before
  exiting the stage.
- Length reduction cuts context and mechanism explanation first;
  it NEVER cuts status labels (working paper / prototype) and never
  strengthens wording to save space.
- The one-sentence version is the hardest test: if it cannot be honest
  and still interesting, revisit the audience strategy rather than
  inflating the claim.

## Outputs

```
output/<project-name>/04_narrative/
├── one_sentence_zh.md / one_sentence_en.md
├── elevator_pitch_zh.md / elevator_pitch_en.md
├── short_summary_zh.md / short_summary_en.md
└── long_narrative_zh.md / long_narrative_en.md
```

## Exit criteria

- all 8 files exist; each finding traceable to a claim_id
- cross-length spot check: same numbers, same claim strength
- state.json updated
