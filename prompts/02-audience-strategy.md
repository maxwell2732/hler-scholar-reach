# Stage 2 — Audience Strategy

Goal: build the Audience–Message Matrix that all later content
generation obeys. Content stages (5/6) may not invent audience
positioning beyond this matrix.

## Procedure

1. Take the audience segments proposed in the campaign brief; check
   them against `references/audience-taxonomy.md`. Add/remove segments
   with a one-line justification each.
2. For every retained segment, fill ALL fields of the matrix template
   (`templates/audience-message-matrix.md`):
   - **Who they are** — concrete, not "researchers in general".
   - **What they care about most** — their question, in their words.
   - **What they may misunderstand** — start from the taxonomy's
     "common misunderstanding risk" column, then specialize it to this
     artifact (e.g. for an observational green-space study: "readers
     may conclude moving near a park improves well-being").
   - **What to emphasize** — reference concrete artifact content;
     after Stage 3 exists, back-fill claim_ids.
   - **What NOT to emphasize** — mandatory, aimed at the
     misunderstanding above.
   - **Best content forms / channels** — only channels in the v0.1 set
     and in the campaign brief.
   - **Call to action** — exactly one per segment.
3. Fill the cross-segment summary, including which segments are
   deliberately NOT targeted and why (e.g. general_public for a
   technical methods paper).
4. Check goal–audience consistency: every goal in the campaign brief
   must be served by at least one segment; flag mismatches.

## Guardrails

- Do not target `general_public`/`science_media` before Gate 1 approval.
- Audience analysis draws on the audit, not on hoped-for impact.
  "Policy researchers" is not a segment for a study with no policy
  lever.

## Outputs

```
output/<project-name>/02_audience/
└── audience_message_matrix.md
```

## Exit criteria

- every segment has all 8 fields filled, incl. "NOT to emphasize"
- cross-segment summary complete; state.json updated
