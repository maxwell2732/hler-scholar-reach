# Stage 7 — Visual Asset Briefs

Goal: v0.1 does not generate images. It produces briefs precise enough
to hand to a designer or an image-generation system, plus alt text for
accessibility.

## Brief format (every brief answers all of these)

- Target platform(s) and exact aspect ratio / pixel size
- Core visual elements (what the image shows)
- Information that MUST appear (title? status label? URL?)
- Information that must NOT appear (unpublished data, publisher-owned
  figures, faces without consent, secrets in screenshots)
- Text on image: yes/no; if yes, exact wording and max length
- Font/readability requirements (thumbnail legibility test)
- Alt text (final wording, not a placeholder)
- Copyright/licensing risk note (who owns the source material)

## Outputs

```
output/<project-name>/07_visuals/
├── visual_asset_manifest.md    # index: asset → purpose → channel → priority
├── social_preview_brief.md     # GitHub/link-card image, 1280×640
├── graphical_abstract_brief.md # papers primarily
├── video_cover_brief.md        # Bilibili/video cover; text ≤13 汉字
├── figure_selection.md         # which existing figures to reuse, and rights status
└── alt_text.md                 # alt text for every proposed/selected visual
```

## Per-artifact priorities

**Repository** (in order): architecture diagram; workflow diagram
(input → stages → human gates → output); real run screenshot (real
output only — never mock a successful run); input/output before-after
comparison; social preview.

**Paper** (in order): graphical abstract (design → sample → finding
with boundary wording ON the image, e.g. "associated with", never an
arrow implying causation for observational designs); ONE key results
figure; study design diagram.

## Integrity rules for visuals

- An observational association is drawn as a link, not as a directed
  causal arrow or mechanism pipeline.
- Axes and error bars in any reused figure keep their original scales.
- Publisher-owned figures enter `figure_selection.md` only with a
  rights status; `rights: unknown` means "do not use yet" and goes to
  Gate 2.
- Screenshots must be reproducible: note the command/state that
  produced them.
- Every visual gets alt text describing content AND takeaway within
  the claim boundary.

## Exit criteria

- manifest lists every proposed asset with priority
- every brief complete (all 8 fields); alt_text.md covers all assets
- state.json updated; **then proceed to Human Gate 2**
  (`gates/gate-02-publication-rights.md`)
