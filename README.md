# territorial-ai-safety

The open research **book** behind Dialogoo's *territorial AI safety* work: a living, reproducible study that defines the framework, builds the evaluation index, and maps the resilience of places to the erosion of human agency.

Part of the [Dialogoo](https://github.com/dialogoo) umbrella · feeds the *Communicate* pillar (map + community-leader materials).

## Read it

The living version is published as an HTML book at **&lt;your GitHub Pages URL&gt;** (rebuilds on every push to `main`).

## What's here

- A **Quarto book** — the narrative and methodology, rendered to HTML (and optionally PDF).
- A **registry-driven index pipeline** (`analysis/`) — each indicator defined once, used by both the book and the code, so they can't disagree.
- **Data** (`data/`) and generated **outputs** (`outputs/`).

## Structure

```
_quarto.yml            book config (parts, chapters, theme, bibliography)
index.qmd              preface
chapters/              the four parts: Foundations, Framework, Methodology, Application
appendices/            codebook, reproducibility, glossary
references.qmd/.bib     cite with @keys
analysis/
  registry/indicators.yml   <- single source of truth for indicators
  pipeline/build_index.py   <- runnable rung-1 index
data/                  raw/ (untracked) + processed/indicators.csv
outputs/               generated index.csv, figures
.github/workflows/     render + deploy to GitHub Pages
```

## Develop locally

```bash
# 1. install Quarto: https://quarto.org/docs/get-started/
# 2. install python deps
pip install -r requirements.txt

# 3. live-reloading HTML site while you write
quarto preview
```

## Publish to GitHub Pages

```bash
# run ONCE locally to create the gh-pages branch:
quarto publish gh-pages
```

Then every push to `main` rebuilds and deploys via `.github/workflows/publish.yml`.
In repo **Settings → Pages**, set the source to the **gh-pages** branch.

## Run the index pipeline standalone

```bash
python analysis/pipeline/build_index.py   # uses demo data until data/processed/indicators.csv exists
```

## Status

Living document, v0.x — see the Preface for what's done vs planned. Contributions and critique welcome, especially attacks on indicator construct validity.
