<div align="center">

# HLER Scholar Reach

### A bilingual scholarly communication workflow for papers and open-source research tools

**Author: 朱 晨 | 遗传社科研究 Chen Zhu | China Agricultural University (CAU)**  
**Last updated: 2026-07-04**

[![Version](https://img.shields.io/badge/version-v0.2-1f6feb?style=flat-square)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/status-early%20prototype-d29922?style=flat-square)](#-project-overview)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-8250df?style=flat-square&logo=anthropic&logoColor=white)](.claude/skills/scholar-reach/SKILL.md)
[![Human in the Loop](https://img.shields.io/badge/Human--in--the--Loop-required-2da44e?style=flat-square)](#-human-gates)
[![Bilingual](https://img.shields.io/badge/languages-Chinese%20%7C%20English-0ea5e9?style=flat-square)](README.md)
[![License](https://img.shields.io/badge/license-MIT-6e7781?style=flat-square)](LICENSE)

[![GitHub Stars](https://img.shields.io/github/stars/maxwell2732/hler-scholar-reach?style=social)](https://github.com/maxwell2732/hler-scholar-reach/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/maxwell2732/hler-scholar-reach?style=social)](https://github.com/maxwell2732/hler-scholar-reach/forks)

[![Chinese README](https://img.shields.io/badge/Docs-中文-1f6feb?style=for-the-badge)](README.md)
[![English README](https://img.shields.io/badge/Docs-English-6e7781?style=for-the-badge)](README_EN.md)
[![Quick Start](https://img.shields.io/badge/Quick-Start-2da44e?style=for-the-badge)](#-quick-start)
[![Workflow](https://img.shields.io/badge/View-Workflow-8250df?style=for-the-badge)](#-workflow)
[![Citation](https://img.shields.io/badge/How_to-Cite-d29922?style=for-the-badge)](#-citation)

</div>

> [!IMPORTANT]
> HLER Scholar Reach is a **v0.2 early-stage prototype**. It can audit source materials, map audiences, and draft platform-specific content. Researchers remain responsible for scientific claims, publication status, rights, and the final decision to publish. The workflow never posts automatically.

> **AI prepares; human approves and publishes.**

HLER Scholar Reach turns papers, working papers, research reports, and open-source research tools into reusable Chinese and English communication materials. Core statements remain traceable to source files or the claim ledger and pass through four Human Gates.

<details>
<summary><strong>📚 Table of contents</strong></summary>

- [Quick Start](#-quick-start)
- [Project Overview](#-project-overview)
- [Workflow](#-workflow)
- [Human Gates](#-human-gates)
- [Supported Artifacts and Channels](#-supported-artifacts-and-channels)
- [Core Mechanisms](#-core-mechanisms)
- [How It Differs from a Marketing Skill](#-how-it-differs-from-a-marketing-skill)
- [Repository Layout](#-repository-layout)
- [Usage](#-usage)
- [Examples and Tests](#-examples-and-tests)
- [Integrity and Publication Rights](#-integrity-and-publication-rights)
- [Roadmap](#-roadmap)
- [Citation](#-citation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/maxwell2732/hler-scholar-reach
cd hler-scholar-reach

# 2. Invoke the skill in Claude Code
/scholar-reach

# Natural-language requests also work
# Generate a bilingual communication package for this paper.
# Plan the launch and dissemination for this GitHub project.

# 3. Run the self-checks
bash tests/test-structure.sh
python tests/test-claim-consistency.py
```

Paper inputs may include a PDF, abstract, and results tables. For a GitHub project, you can install the skill in the target repository or read an external repository while keeping campaign outputs in HLER Scholar Reach's `output/` directory.

## ✨ Project Overview

| Item | Current implementation |
|---|---|
| Intended users | Researchers, research teams, institutions, and developers of open-source research tools |
| Artifacts | Papers, working papers, preprints, research reports, and GitHub repositories |
| Chinese channels | WeChat, institutional news, group sharing, Bilibili/video, Zhihu, and Xiaohongshu |
| English channels | GitHub, LinkedIn, Bluesky/X, and lay summaries |
| Control layer | Claim Ledger plus four Human Gates |
| Publishing model | Draft preparation and launch planning, followed by human review and manual publication |
| Project status | v0.2, early-stage prototype, not yet systematically validated by external users |

Common failures in scholarly communication include turning associations into causal claims, presenting a preprint as a published paper, describing an early prototype as a mature product, and inventing adoption or impact metrics. HLER Scholar Reach encodes checks for these risks in the workflow.

## 🧭 Workflow

```text
Stage 0  Intake                         Inventory and task identification
    ↓
Stage 1  Artifact Audit                Paper or repository audit
    ↓
Stage 2  Audience Strategy             Audience-message matrix
    ↓
Stage 3  Claim Ledger                  Traceable communication claims
    ↓
⛔ Gate 1  Scientific Integrity        Human scientific review
    ↓
Stage 4  Core Narrative                Bilingual narrative base
    ↓
Stage 5  Chinese Content Pack          Chinese platform outputs
Stage 6  English Content Pack          English platform outputs
    ↓
Stage 7  Visual Asset Briefs           Visual specifications
    ↓
⛔ Gate 2  Publication Rights          Rights and embargo review
    ↓
Stage 8  Launch Plan                   Three-wave dissemination plan
    ↓
⛔ Gate 3  No-Hype Review              Language and evidence review
    ↓
Stage 9  Integrity Review              Cross-file consistency checks
    ↓
⛔ Gate 4  Final Approval              Per-platform human approval
```

Detailed instructions for each stage are available in [`prompts/`](prompts/).

## 🛡️ Human Gates

| Gate | Human review |
|---|---|
| [Gate 1: Scientific Integrity](gates/gate-01-scientific-integrity.md) | Main findings, effect direction, causal language, numerical accuracy, limitations, and software capabilities |
| [Gate 2: Publication Rights](gates/gate-02-publication-rights.md) | Embargoes, publication status, shareable versions, figure rights, co-author awareness, and sensitive files |
| [Gate 3: No-Hype Review](gates/gate-03-no-hype.md) | Evidence for strong wording and conservative replacements where needed |
| [Gate 4: Final Approval](gates/gate-04-final-approval.md) | Final approval for each platform before any output is marked `publication-ready` |

Before Gate 1 is approved, the workflow may produce drafts marked `[UNVERIFIED]`. Until Gate 4 is complete, outputs remain `draft` or `review-required`.

## 🌐 Supported Artifacts and Channels

### Artifact types

- **Paper**: published articles, online-first papers, accepted manuscripts, working papers, preprints, and research reports.
- **GitHub Repository**: Claude Code skills, research workflows, data-cleaning tools, analytical repositories, teaching tools, and open-source research software.

### Chinese channels

| Channel | Primary role | Typical outputs |
|---|---|---|
| WeChat article | Full explanation and long-term reference | Long-form article, titles, and summary |
| Institutional news | Formal announcement | News release and project overview |
| Group sharing | Rapid distribution through existing networks | A short 100–200 character message |
| Bilibili / video | Demonstration and credibility | Long and short scripts, chapters, and cover brief |
| Zhihu | Question-driven knowledge explanation | Question options, answer, and article |
| Xiaohongshu | Visual discovery and lightweight education | Short post, titles, and a 6–8 card carousel script |

Zhihu outputs begin with a genuine question that can stand independently of the project name. Xiaohongshu outputs are built around structured visual cards while retaining project status, limitations, and claim traceability.

<details>
<summary><strong>View an example Xiaohongshu card</strong></summary>

```yaml
cards:
  - page: 7
    role: limitation
    headline: "What it cannot do"
    body: "Early-stage prototype; no automated posting; no guaranteed impact"
    suggested_visual: "AI prepares content, researchers review and publish"
    claims_used: [C02, C10]
    prohibited_implications: ["mature product", "automated marketing"]
    alt_text: "A card describing the workflow's limitations"
```

</details>

### English channels

- GitHub README, Release, and Social Preview
- LinkedIn
- Bluesky / X
- Lay summaries and short announcements

Chinese and English outputs share the same factual base and claim strength while using platform-appropriate structure and phrasing.

## 🧠 Core Mechanisms

### Claim Ledger

Stage 3 records every communicable claim in a CSV file. Each entry includes:

- source file and location
- claim type
- evidence and confidence
- allowed Chinese and English wording
- prohibited wording
- qualifications and limitations
- human approval requirements

Platform content uses claims already present in the ledger and retains claim-traceability comments.

### Three-wave dissemination

| Wave | Content |
|---|---|
| Launch | Introduce the work, the main finding or capability, and the primary link |
| Use case | Demonstrate an example, tutorial, method, or frequently asked question |
| Update | Publish only when a new version, use case, or other verifiable development exists |

This model supports low-maintenance scholarly communication without manufacturing a daily posting schedule.

### Transparent authorship

Authors may introduce their own project in the first person, for example, “We developed this workflow.” The system prohibits fabricated third-party recommendations, testimonials, user experiences, questions, and social proof.

## 🧩 How It Differs from a Marketing Skill

| Dimension | Typical marketing skill | HLER Scholar Reach |
|---|---|---|
| Source material | Flexible creative input | Core statements come from a traceable claim ledger |
| Causal language | Evidence levels may be blurred | Wording follows the research design and evidence strength |
| Publication status | May be simplified for promotion | Working papers, preprints, and accepted manuscripts retain their status |
| Software maturity | Capabilities can be overstated | Prototype, tested, and production-ready states remain distinct |
| Publishing action | May post directly | Produces drafts for human review and manual publication |
| Cadence | Frequent content production | Three waves linked to real developments |
| Localization | Often based on direct translation | Chinese and English narratives are composed separately |

## 📁 Repository Layout

```text
hler-scholar-reach/
├── .claude/skills/scholar-reach/   # Claude Code skill entry point
├── prompts/                         # Stage 0–9 instructions
├── gates/                           # Four Human Gate procedures
├── references/                      # Long-lived rules and channel guidance
├── templates/                       # YAML, JSON, CSV, and Markdown templates
├── examples/                        # Two fictional examples
├── tests/                           # Structure and claim-consistency tests
└── output/                          # Generated campaigns, excluded from git by default
```

Typical campaign output:

```text
output/<project-name>/
├── state.json
├── 00_intake/  01_audit/  02_audience/  03_claims/
├── 04_narrative/  05_zh/  06_en/  07_visuals/
├── 08_launch/  09_review/  10_retrospective/
└── gates/
```

## 🛠️ Usage

Run the skill in Claude Code:

```text
/scholar-reach
```

You can also specify the artifact and channels in natural language:

```text
Generate a bilingual communication package for this paper.
Plan the launch and dissemination for this GitHub project.
Generate only the Zhihu answer and Xiaohongshu carousel.
Read ../pAI-Econ-claude and save the campaign drafts in this repository's output directory.
```

Channel selection is supported in v0.2:

```text
/scholar-reach --channels zhihu,xiaohongshu
```

Chinese channel IDs: `wechat`, `institutional_news`, `group_share`, `video`, `zhihu`, and `xiaohongshu`.  
English channel IDs: `github`, `linkedin`, `bluesky`, `x`, and `lay_summary`.

The workflow reads available materials before asking questions. Unknown information remains `unknown`. Repository improvements are produced as recommendations or patches. The skill does not commit, push, create a release, or publish to external platforms.

## 🧪 Examples and Tests

### Examples

- [`examples/paper-example/`](examples/paper-example/): a fictional working paper demonstrating association-safe language.
- [`examples/repository-example/`](examples/repository-example/): a fictional early-stage prototype named `clean-panel`, demonstrating maturity-safe descriptions.

### Self-checks

```bash
bash tests/test-structure.sh
python tests/test-claim-consistency.py
```

The structure test checks required files, skill frontmatter, template fields, and state files. The claim-consistency test covers prohibited wording, negation contexts, line-number reporting, and output traceability.

## 📜 Integrity and Publication Rights

See [`references/academic-integrity.md`](references/academic-integrity.md) for the full rules.

- Do not fabricate findings, DOIs, citations, stars, forks, downloads, user testimonials, or media coverage.
- Do not convert an association into a causal claim.
- Do not present a preprint or working paper as a formally published article.
- Record an unclear embargo status as `unknown`.
- Treat publisher figures as restricted unless reuse rights are confirmed.
- Do not expose peer-review content, restricted data, secrets, or personal information.
- Confirm author and institutional attribution against source materials.

> [!NOTE]
> HLER Scholar Reach does not guarantee citations, stars, forks, media coverage, or academic impact. It helps researchers organize and communicate existing work with clearer structure and stronger evidence control.

## 🗺️ Roadmap

### Implemented in v0.2

- Zhihu and Xiaohongshu localization
- Distinct roles for Chinese platforms
- Transparent authorship rules
- No-hype scanning with negation-context handling
- Channel selection
- Structured Xiaohongshu carousel template

### Future directions

- ResearchGate, Reddit, Hacker News, and media pitches
- Institutional CMS support
- ORCID, Crossref, Zenodo, and Altmetric integrations
- GitHub analytics and automated link checking
- Social platform APIs
- Card and visual asset generation
- Multi-project campaign dashboard
- Co-author approval flows
- Post-campaign evaluation
- Quick, Standard, and Full run modes

## 📖 Citation

**Author: 朱 晨 | 遗传社科研究 Chen Zhu | China Agricultural University (CAU)**

See [`CITATION.cff`](CITATION.cff) for the recommended citation format. Citations in papers, project documentation, and software references are welcome when the workflow supports your research communication.

## 🤝 Contributing

Issues, template improvements, and channel-guidance contributions are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before contributing.

## 📄 License

HLER Scholar Reach is released under the [MIT License](LICENSE).
