# Changelog

All notable changes to HLER Scholar Reach are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-07-04 — Chinese Platform Expansion and Self-Dogfooding

### Added

- **Zhihu channel** (question-driven knowledge explanation): channel
  profile, question-generation rules (questions must stand on their
  own without the project name; no self-marketing "如何评价我开发的X"
  questions), 8-step answer and article structures, outputs
  `zhihu_question_options / zhihu_answer / zhihu_article /
  zhihu_summary`, template `templates/zhihu-answer.md`.
- **Xiaohongshu channel** (visual-first discovery / lightweight
  education): channel profile, title taxonomy (question/method/tool/
  tutorial), short post structure, 6–8 card carousel in structured
  YAML (`templates/xiaohongshu-carousel.yaml`, mandatory limitation
  card), topics with "suggestion only, not current trends" rule,
  outputs `xiaohongshu_titles / _post / _carousel / _topics /
  _visual_brief`.
- **Chinese platform role layering**: six zh channels with distinct
  roles (WeChat = full explanation/archive, institutional news =
  formal release, group share = personal-network reach, video =
  demonstration/credibility, Zhihu = question-driven explanation,
  Xiaohongshu = visual discovery); hard boundaries against
  copy-shortening between platforms; all zh channel profiles upgraded
  to a 9-field format.
- **Platform identity transparency rules**
  (`references/academic-integrity.md` §9): first-person transparency
  ("我们开发了"), no fake third-party voice, no fabricated comments/
  testimonials/interactions/popularity; plus paper- and repo-specific
  rules for Zhihu/Xiaohongshu.
- **No-hype scanner v2** (`check_claims.py`): three new zh lexicon
  groups (exaggeration/absolutes, fake social proof, anxiety-marketing
  phrase patterns); two-level severity `violation` vs `context_review`;
  best-effort negation detection so disclaimers like "不能保证获得
  引用" are not reported as violations (single-line heuristic — known
  limitation, documented in gate-03); exit code 1 only on violations.
- **Channel selection**: `/scholar-reach --channels zhihu,xiaohongshu`
  or natural language; v0.1 channel IDs accepted as aliases.
- **state.json v0.2 fields**: `requested_channels`,
  `completed_channel_outputs`, `channel_review_status`,
  `platform_specific_risks`, `schema_version`; v0.1 state files remain
  loadable (missing fields = defaults).
- New scanner test fixtures (hype-zh v0.2 hits; negation contexts and
  quoted mentions that must not be flagged as violations) and
  structure-test checks for the new templates and channel profiles.
- Scanner fixes found by self-dogfooding: (a) terms *mentioned* right
  after a quote character (rule explanations like 扫描器会标记"彻底
  解决") are downgraded to context_review instead of violation;
  (b) a bare 不 immediately before a hit (不保证引用) now counts as
  negation. Both downgrade rather than hide — a human still reviews.
- Self-dogfooding campaign for this repository itself under
  `output/hler-scholar-reach/` (all content `draft`; Gate 4 pending),
  plus a Stage 10 retrospective.

### Changed

- `prompts/05-zh-content-pack.md`: platform layering, per-channel
  generation driven by `requested_channels`, Zhihu/Xiaohongshu output
  sections.
- `references/channel-profiles.md`, `references/bilingual-localization.md`,
  `gates/gate-03-no-hype.md`, `SKILL.md`, READMEs updated accordingly.

### Fixed

- `CITATION.cff`: version bumped to 0.2.0; prototype status stated in
  the abstract; `repository-code` set to the real URL
  (https://github.com/maxwell2732/hler-scholar-reach, created
  2026-07-04 — verified public but empty; the initial push is still
  pending, so links go live only after the code is pushed).

### Not implemented in 0.2 (deliberately)

- Carousel YAML → image generation; automatic posting to any platform;
  trend/heat data fetching; link checking; semantic (beyond-lexicon)
  hype detection — the scanner's negation handling is a single-line
  heuristic and does not understand cross-sentence scope or irony.

## [0.1.0] - 2026-07-04

### Added

- Initial v0.1 MVP of HLER Scholar Reach.
- Claude Code skill `scholar-reach` (`.claude/skills/scholar-reach/SKILL.md`).
- Ten workflow stage prompts (`prompts/00`–`09`): intake, artifact audit,
  audience strategy, claim ledger, core narrative, zh content pack,
  en content pack, visual asset briefs, launch plan, integrity review.
- Four Human Gates: scientific integrity, publication rights, no-hype
  review, final approval (`gates/`).
- Reference knowledge base: artifact types, audience taxonomy, channel
  profiles, claim language guide, academic integrity rules, bilingual
  localization guide (`references/`).
- Structured output templates: campaign brief, artifact manifest,
  state.json, claim ledger CSV, audience–message matrix, launch calendar,
  final report (`templates/`).
- Two fictional minimal examples: a working paper and an early-stage
  repository (`examples/`).
- Structure test (`tests/test-structure.sh`) and claim consistency /
  prohibited-language scanner test (`tests/test-claim-consistency.py`,
  wrapping `.claude/skills/scholar-reach/scripts/check_claims.py`).

### Scope of v0.1

- Artifact types: paper (published / online first / accepted / working
  paper / preprint / report) and GitHub repository.
- Channels (zh): WeChat official account article, group share message,
  Bilibili / video channel script, institutional news.
- Channels (en): GitHub README / Release / social preview, LinkedIn,
  Bluesky / X, lay summary.

### Explicitly not in v0.1 (see README roadmap)

- Zhihu, Xiaohongshu, ResearchGate, Reddit, Hacker News, media pitches,
  platform APIs, automatic publishing, analytics integrations.
