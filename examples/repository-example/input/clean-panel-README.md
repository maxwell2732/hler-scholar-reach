# clean-panel (fictional example project)

A reproducible workflow for auditing and cleaning longitudinal survey
data.

**Status: early-stage prototype (v0.2.0).** Interfaces may change;
tested so far on two example datasets only.

## What it does today

- Audits a panel dataset for duplicate person-wave records and writes
  an audit log (`clean-panel audit data.csv`)
- Flags impossible value transitions between waves (e.g. age
  decreasing) using a rule file
- Produces a cleaning script you review and run yourself — it never
  modifies your data in place

## Design goals (not yet implemented)

- Support for multiply-imputed datasets
- R interface (currently Python CLI only)

## Install

```bash
pip install git+https://example.com/fictional/clean-panel  # fictional
```

## Known limitations

- Wide-format panels not supported yet
- Rule file syntax is undocumented beyond the two examples
- No performance testing beyond ~50k rows

## License / Citation

MIT. Citation file: `CITATION.cff` (included).
