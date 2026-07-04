# Stage 6 — English Content Pack

Goal: compose English channel content from the core narrative and
claim ledger. Composed independently of the Chinese pack (see
`references/bilingual-localization.md`); channel specs in
`references/channel-profiles.md`.

## Preconditions

- Stage 4 complete. If Gate 1 not yet approved: DRAFT headers +
  `[UNVERIFIED]` markers as in Stage 4/5.

## Paper outputs

```
output/<project-name>/06_en/
├── linkedin_post.md
├── bluesky_thread.md
├── x_thread.md
├── lay_summary.md
├── coauthor_share_message.md   # for co-authors to forward; neutral voice
└── short_announcement.md       # 2–3 sentences, mailing lists / dept news
```

## Repository outputs

```
output/<project-name>/06_en/
├── github_readme_recommendations.md  # concrete diffs/suggestions, NOT applied
├── release_notes.md                  # Added/Changed/Fixed; factual
├── linkedin_launch.md
├── bluesky_thread.md
├── x_thread.md
└── short_announcement.md
```

## Composition rules

- Style: follow `references/bilingual-localization.md` §"句式与标点：
  避免机器腔" (no "this is X, not Y" / "X, not Y" appositive frames,
  no meta-discourse openers, em-dashes sparing and never two per
  sentence); self-check every file before exiting the stage.
- Open with the problem or the finding — never "We are thrilled to
  announce...", "Excited to share..." or equivalent enthusiasm-first
  openers. State: problem → audience → contribution → demonstration →
  limitations → access link.
- **Threads (Bluesky/X)**: 4–6 posts, one idea per post, written to
  fit 280 chars so one thread serves both platforms. Post order:
  finding/capability with boundary → why it matters → how (one plain
  sentence) → key limitation → link + citation → (optional) invite.
  Number the posts (1/5 ... 5/5). Include alt-text placeholders for
  any suggested image.
- **LinkedIn**: 150–300 words, hook in first 2 lines, professional
  first person, ≤3 hashtags, not a corporate ad.
- **Lay summary**: 150–400 words, plain English; the "what this does
  NOT show" sentence is mandatory for observational papers.
- **Coauthor share message**: neutral wording any co-author can send
  without implying they led the work.
- **README recommendations** (repos): propose exact replacement text /
  unified diffs for the first screen, badges, quick start, citation
  section — as suggestions in this file only. Never modify the user's
  repo files.
- **Release notes**: only for versions that exist in the repo's tags/
  CHANGELOG. No release notes for unreleased versions.

## Status honesty

Working paper / preprint / prototype status appears in EVERY item long
enough to hold a sentence, and is never contradicted by shorter items.

## Traceability

End every file with `<!-- claims used: C01, ... -->`.

## Exit criteria

- all files for the artifact type generated; claims-used comments present
- no thread exceeds 6 posts or 280 chars/post
- state.json updated
