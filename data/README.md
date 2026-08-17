# Data

- **`raw/`** — original source files, untracked in git (large / licence-bound). Record provenance below; version with DVC if it grows.
- **`processed/`** — cleaned, analysis-ready tables. The pipeline expects **`indicators.csv`**: a wide table with one row per territory (index = territory id) and one column per indicator `id` from `analysis/registry/indicators.yml`.

## Unit of analysis

Two tiers, decided for the pilot:

- **Tier 1 — provinces (NUTS-3).** All 50 Spanish provinces, for complete and comparable coverage.
- **Tier 2 — municipalities.** A handful assembled by hand, in depth, to test whether the index says the same thing when the scale changes.

Territory ids must carry the official code (INE municipal code, or the NUTS-3 code) so a row can be traced back to a boundary, not to a name.

## Provenance log

Fill one row per indicator. Disclosed gaps are credible; hidden gaps are fatal. Nothing is cited
in the book from memory: `url` plus `locator` must be enough for a reader to land on the exact
number without searching for it.

| indicator id | source | url | locator (table / page) | vintage | accessed | licence | unit / notes |
|--------------|--------|-----|------------------------|---------|----------|---------|--------------|
| intermediation_depth | TBD | | | | | | |
| channel_concentration | TBD | | | | | | |
| labor_leverage_exposure | TBD | | | | | | |
| polycentric_governance | TBD | | | | | | |
| civic_density | TBD | | | | | | |
| channel_redundancy | TBD | | | | | | |
