# Artifact Types (v0.1)

HLER Scholar Reach v0.1 supports exactly two artifact types. If the
materials do not clearly match one of them, classify as `unknown` and
ask the user — do not force a classification.

## Type A: Paper

Covers: published journal/conference articles, online-first articles,
accepted manuscripts, working papers, preprints, and research reports.

### Status vocabulary (use exactly these values)

| status | Meaning | Communication consequence |
|---|---|---|
| `published` | Final version of record is public | May cite venue, volume, DOI |
| `online_first` | Accepted, published online, not yet in an issue | Say "online first in <venue>"; no volume/issue |
| `accepted` | Accepted but not yet online | Say "accepted at <venue>", check embargo before announcing |
| `working_paper` | Circulating draft, not peer-reviewed | MUST label as working paper; never imply peer review |
| `preprint` | Posted on a preprint server, not peer-reviewed | MUST say preprint + server name; never call it "a study published in..." |
| `report` | Institutional/technical report | Name the issuing institution; do not imply journal publication |

Status is a fact, not a style choice. Every piece of content must state
or be consistent with the true status. Status upgrades ("preprint" →
"published") only happen when the user provides evidence.

### Signals for detecting a paper in the working directory

- `.pdf`, `.docx`, `.tex` files with title/abstract structure
- Files named like `manuscript*`, `paper*`, `abstract*`, `supplement*`
- A results table, figure files, or a cover letter
- A user statement describing a study

## Type B: GitHub Repository

Covers: Claude Code skills, research workflows, data-cleaning tools,
analysis code, teaching tools, open-source research software.

### Status vocabulary

| status | Meaning | Communication consequence |
|---|---|---|
| `prototype` | Early-stage, interfaces unstable, limited testing | MUST say early-stage/prototype; never "production-ready", never "battle-tested" |
| `alpha` | Feature-incomplete, seeking early feedback | Emphasize feedback CTA over adoption CTA |
| `beta` | Feature-complete, stabilizing | May invite broader use with caveats |
| `stable` | Released, versioned, maintained | Normal adoption messaging |
| `archived` | No longer maintained | Must disclose; communication usually not appropriate |

### Signals for detecting a repository

- `README.md`, `LICENSE`, source code directories, `.git/`
- `CITATION.cff`, `CHANGELOG.md`, `pyproject.toml` / `package.json` etc.

### Adoption metrics rule

Stars, forks, downloads, and user counts may ONLY be mentioned if the
user supplies the current number (statement or screenshot) with a date.
Record them as `adoption_metric` claims with the check date. Never
estimate, extrapolate, or reuse stale numbers.

## Mixed cases

A repository that accompanies a paper: pick the artifact the user wants
to promote as primary; audit the other briefly and cross-link. Do not
run two full campaigns in one pass in v0.1.
