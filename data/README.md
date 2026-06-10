# Data

- **`raw/`** — original source files, untracked in git (large / licence-bound). Record provenance below; version with DVC if it grows.
- **`processed/`** — cleaned, analysis-ready tables. The pipeline expects **`indicators.csv`**: a wide table with one row per territory (index = territory id) and one column per indicator `id` from `analysis/registry/indicators.yml`.

## Provenance log

Fill one row per indicator. Disclosed gaps are credible; hidden gaps are fatal.

| indicator id | source | url | vintage | licence | unit / notes |
|--------------|--------|-----|---------|---------|--------------|
| intermediation_depth | TBD | | | | |
| channel_concentration | TBD | | | | |
| ... | | | | | |
