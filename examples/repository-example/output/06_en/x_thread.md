# X / Bluesky thread (5 posts, each ≤280 chars) — FICTIONAL EXAMPLE

1/5 Cleaning longitudinal survey data usually means an undocumented
pile of one-off scripts. I'm building clean-panel, an early-stage
prototype (v0.2.0) that turns the audit step into a reproducible
workflow.

2/5 What it does today: detects duplicate person-wave records, flags
impossible transitions between waves (age going down, etc.), and
writes an audit log you can put in your appendix.

3/5 Design choice: it never touches your data in place. It generates
a cleaning script that YOU review and run. Human in the loop, on
purpose.

4/5 Honest limits: tested on two example datasets, long format only,
~50k rows so far. MI support and an R interface are planned, not
built. Interfaces may change.

5/5 If you work with panel data and want to kick the tires (or file
issues), it's here: https://example.com/fictional/clean-panel
MIT licensed, citation file included.

<!-- claims used: C01, C02, C03, C04 -->
