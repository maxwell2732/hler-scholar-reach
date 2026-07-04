# Stage 8 — Launch Plan

Goal: a low-maintenance dissemination plan. Three waves, symbolic
dates, one human owner per item. This system does not run accounts;
it packages one artifact well.

## Preconditions

- Content packs (Stage 5/6) exist. Gate 2 should be presented before
  the plan is finalized; if pending, mark the plan DRAFT.

## The three waves

1. **Wave 1 — Launch (T0)**: formal introduction; core finding or main
   capability; canonical link; recommended citation.
2. **Wave 2 — Use case (T0 + 5–10 days)**: a real case, tutorial,
   method explanation, FAQ, or design rationale. Must add substance,
   not repeat Wave 1.
3. **Wave 3 — Update (next meaningful update)**: ONLY when a real
   trigger occurs: new version, new feature, documented adoption,
   external contribution, verified citation/coverage, or formal
   publication of a working paper/preprint.

## Date rules

- Never invent dates. Without user-provided dates use exactly:
  `T0`, `T0 + 5–10 days`, `Next meaningful update`.
- If the user gives T0, compute Wave 2 as a window, not a fake
  precise date.
- Respect embargo: if Gate 2 recorded an embargo date, T0 ≥ embargo
  lift, stated explicitly in the calendar.

## Outputs

```
output/<project-name>/08_launch/
├── launch_calendar.md        # from templates/launch-calendar.md
├── channel_matrix.md         # channel × wave: which file goes where, adaptation notes
├── call_to_action_matrix.md  # audience × wave: the one CTA each gets (from Stage 2)
└── reuse_plan.md             # how assets get reused later
```

### channel_matrix.md

Rows = channels (from campaign brief); columns = waves. Each cell:
content file + any channel-specific tweak (e.g. WeChat "阅读原文" link
placement). Empty cells are explicit decisions — note why a channel
sits out a wave.

### reuse_plan.md

- Which assets update when status changes (preprint → published:
  list every file containing the status string).
- Which Wave 1 assets become templates for Wave 3.
- What to archive after the campaign.

## Anti-patterns

- No daily/weekly posting schedules. If the user asks for one,
  explain the low-maintenance principle once, then follow the user's
  decision and record it in the calendar notes.
- No cross-posting identical text to all channels — each channel uses
  its adapted file.

## Exit criteria

- calendar, channel matrix, CTA matrix, reuse plan complete
- every calendar row points to an existing file and has a human owner
- state.json updated; **then run Human Gate 3**
  (`gates/gate-03-no-hype.md`)
