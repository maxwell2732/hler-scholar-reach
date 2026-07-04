# Contributing to HLER Scholar Reach / 贡献指南

Thank you for considering a contribution. This project is a
human-in-the-loop academic dissemination workflow; contributions must
preserve its core principles.
感谢你考虑为本项目做贡献。本项目是一个 Human-in-the-Loop 学术传播工作流，
所有贡献都必须维护其核心原则。

## Non-negotiable principles / 不可妥协的原则

1. **Evidence-grounded** — no feature or template may encourage
   fabricating findings, publication status, DOIs, metrics, or media
   coverage. 不得引导编造研究发现、发表状态、DOI、指标或媒体报道。
2. **Human-in-the-Loop** — the system must never publish to external
   platforms automatically, and Human Gates must not be bypassed by
   default. 系统不得自动对外发布，Human Gates 不得被默认绕过。
3. **Translation is not localization** — zh/en content strategies stay
   separate; do not collapse them into machine translation.
4. **Low-maintenance dissemination** — do not add features whose only
   purpose is manufacturing posting frequency.

## What to contribute / 欢迎的贡献

- New channel profiles in `references/channel-profiles.md` (with a
  dated source for any platform constraint you cite).
- Improved claim-language guidance (`references/claim-language-guide.md`),
  especially for research designs not yet covered.
- Additional prohibited/hype vocabulary for the no-hype scanner
  (`.claude/skills/scholar-reach/scripts/check_claims.py`).
- Bug fixes in scripts and tests.
- New minimal, **fictional** examples. Never commit real embargoed
  papers, peer-review content, or personal data.

## Workflow / 流程

1. Open an issue describing the change and which principle it serves.
2. Fork, branch from `main`, keep changes focused.
3. Run the tests before submitting:
   ```bash
   bash tests/test-structure.sh
   python tests/test-claim-consistency.py
   ```
4. Update `CHANGELOG.md` under an "Unreleased" heading.
5. Open a pull request. Explain what you changed and why; if you cite a
   platform rule or external fact, include the source URL and the date
   you checked it.

## Style / 风格

- File names and code in English; explanatory documents may be
  bilingual (zh first or en first is both fine, be consistent per file).
- Prefer Markdown, YAML, JSON, CSV, Python (stdlib only), and shell.
- Do not add third-party dependencies without discussion in an issue.
- Templates must stay parseable (valid YAML/JSON/CSV).

## Licensing

By contributing you agree that your contributions are licensed under
the MIT License of this repository.
