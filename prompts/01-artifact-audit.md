# Stage 1 — Artifact Audit

Goal: read the materials thoroughly and assess (a) what the artifact
actually claims/does and (b) how ready it is to be communicated.
The audit is about the artifact, not yet about content creation.

## Paper audit checklist

Extract and record, each with its source location:

- title; full author list (exact order); affiliations
- abstract; research question; research design (be precise:
  cross-sectional / longitudinal / RCT / quasi-experimental / ...)
- sample: who, N, where, when
- main findings, with effect directions and key numbers
- the causal/associational boundary of each finding
  (per `references/claim-language-guide.md` claim types)
- publication status (exact vocabulary from
  `references/artifact-types.md`); venue; DOI or public URL if present
- embargo evidence, if any; which manuscript version can be shared
- figures/tables available and their reuse rights (publisher vs. author)
- limitations as stated by the authors
- funding and acknowledgments

## Repository audit checklist

- README first screen: does a newcomer learn what/for whom/why in
  30 seconds? Quote the actual first screen in the audit.
- What problem it solves; who the target user is
- Quick Start: actually trace the steps — do the commands match the
  files present? Flag steps that cannot work.
- LICENSE (which); CITATION.cff (present? valid?); CHANGELOG; Releases
- examples present? screenshots/demo present?
- suggested GitHub topics; social preview status
- README languages (zh/en/both)
- known limitations as documented
- security/privacy sweep: committed secrets, tokens, `.env`, personal
  paths, restricted data files (report paths, do not print secret values)

## Readiness scorecard

Score each dimension 0–2 (0 = missing, 1 = partial, 2 = ready), and —
mandatory — give the concrete reason per score. No unexplained totals.

Paper dimensions: identifiability (title/authors/status), accessibility
(public link), story completeness (question/design/findings), boundary
clarity (limitations stated), visual assets, rights clarity.

Repo dimensions: first-screen clarity, runnable quick start, licensing
& citation, versioning/changelog, examples & demo, security hygiene.

## Recommended fixes

`recommended_fixes.md`: ordered list, each item = what to fix, why it
matters for communication, effort estimate (S/M/L). For repo fixes that
change files, propose patches/diffs — never edit the user's repo files
directly in this stage.

## Outputs

```
output/<project-name>/01_audit/
├── artifact_audit.md
├── readiness_scorecard.md
└── recommended_fixes.md
```

## Exit criteria

- every checklist item answered or marked unknown with reason
- scorecard has a reason for every score
- state.json updated
