# Stage 0 — Intake

Goal: understand what artifact we are communicating, for whom, through
which channels, with what materials — without asking the user anything
that the files already answer.

## Procedure

1. **Scan the working directory** (and any paths the user pointed to).
   Identify candidate materials using the signals in
   `references/artifact-types.md`. Read enough of each file to classify
   it (title page / abstract / README first screen), not necessarily
   everything yet.
2. **Classify the artifact**: `paper`, `repository`, or `unknown`.
   If `unknown`, present what was found and ask the user to classify.
   Do not guess.
3. **Determine project_name**: a short kebab-case slug from the paper
   title or repo name. Confirm with the user only if ambiguous.
4. **Fill `campaign_brief.yaml`** (from `templates/campaign-brief.yaml`):
   - artifact status: only from evidence (title page footnote, journal
     page, README badge, user statement). Otherwise `unknown`.
   - goals: propose a ranked subset of the default goals based on the
     artifact; the user can reorder at any time.
   - audiences: propose from `references/audience-taxonomy.md`.
   - channels: default to the full v0.1 set for each requested
     language unless the user narrows it.
   - constraints (embargo, coauthors, figure rights): `unknown` unless
     evidenced. `unknown` is a first-class value.
5. **Fill `artifact_manifest.yaml`** (from
   `templates/artifact-manifest.yaml`): one `sources` entry per input
   file, plus one `user_statements` entry per fact the user asserted in
   conversation.
6. **Write `missing_materials.md`**: what is absent, why it matters,
   and what quality is possible without it. Distinguish:
   - *blocking* (cannot proceed correctly): e.g. no abstract and no
     full text for a paper.
   - *degrading* (proceed with placeholders/lower quality): e.g. no
     figures, no CHANGELOG.
7. **Initialize state**: copy `templates/state.json` to
   `output/<project_name>/state.json`, set fields, timestamp.

## Question discipline

Ask the user ONLY questions that are (a) unanswerable from materials
AND (b) affect downstream correctness. Batch them in one message.
Everything else goes into `missing_materials.md` or stays `unknown`
until a gate surfaces it.

## Outputs

```
output/<project-name>/00_intake/
├── campaign_brief.yaml
├── artifact_manifest.yaml
└── missing_materials.md
output/<project-name>/state.json
```

## Exit criteria

- artifact_type resolved (or user explicitly told classification failed)
- manifest lists every available source
- state.json exists with current_stage = "artifact_audit"
