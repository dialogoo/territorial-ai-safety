<img src="./.github/brand/mark.svg" alt="AI SAFE EARTH" width="72">

# AI Safe Territory

> The open research **book** behind AI SAFE EARTH's work on *AI Safe Territories*. Defining, measuring, and mapping how resilient places (towns, cities, regions) are to the erosion of human agency.

![Pillar](https://img.shields.io/badge/RESEARCH-IN_PROGRESS-C4692A?style=flat-square&labelColor=131A21)
[![Read the book](https://img.shields.io/badge/READ-THE_BOOK-1F5D7A?style=flat-square&labelColor=131A21)](https://ai-safe-earth.github.io/AI-Safe-Territory/)
[![Quarto](https://img.shields.io/badge/BUILT_WITH-QUARTO-4A5560?style=flat-square&labelColor=131A21)](https://quarto.org)
[![Umbrella](https://img.shields.io/badge/AI_SAFE_EARTH-open_umbrella-131A21?style=flat-square&labelColor=131A21)](https://github.com/ai-safe-earth)

Part of the [AI SAFE EARTH](https://github.com/ai-safe-earth) umbrella. This repository is the core project of the **Research** pillar and the source of the materials produced by the **Communicate** pillar (the territorial map and the community-leader guides).

## Read it

The living version is published as a website and rebuilds on every push:

**→ [ai-safe-earth.github.io/AI-Safe-Territory](https://ai-safe-earth.github.io/AI-Safe-Territory/)**

It is public, anyone can read it, no account needed, and because it is continuously published, it always reflects the latest commit.

## What this is

A place is more or less resilient to the erosion of human agency depending on its inherent structure: how distributed its decision-making is, how redundant its communication channels are, how dense its civic life is, how exposed it is to capture by a single mediating layer. This repository turns that idea into a transparent, reproducible evaluation index and maps the result.

It holds three things that stay in sync with each other:

- a **Quarto book**. The narrative, framework, and methodology, rendered to the website above;
- a **registry-driven index pipeline** (`analysis/`). Every indicator defined once and read by both the book and the code, so the documented method can never drift from the computed one;
- the **data and outputs** behind the index.

## Repository structure

```
_quarto.yml              book config: parts, chapters, theme, bibliography
index.qmd                preface
chapters/                the four parts: Foundations, Framework, Methodology, Application
appendices/              codebook, reproducibility, glossary
references.qmd / .bib     cite inline with @keys
analysis/
  registry/indicators.yml   single source of truth for indicators
  pipeline/build_index.py   runnable index pipeline
data/                    raw/ (untracked) + processed/indicators.csv
outputs/                 generated index.csv, figures
.github/workflows/       renders and deploys to GitHub Pages on push
```

## Develop and write locally

You write against a private, live preview, you never need to publish just to see your work. Think of it as two speeds: **`quarto preview` is your private writing desk** (instant, local, just you), and **`git push` is the printing press** (public, for everyone).

**Prerequisites:** [Quarto](https://quarto.org/docs/get-started/) and Python 3.10+.

```bash
# 1. set up the Python environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. start the live, auto-reloading preview
quarto preview
```

This opens the book locally (e.g. `http://localhost:4321`) and refreshes the moment you save. Then edit the `.qmd` files in `chapters/`, they are plain Markdown. To add a chapter, create the `.qmd` and register its path under the right `part:` in `_quarto.yml`. Cite by adding an entry to `references.bib` and referencing it inline as `[@key]`.

## Publishing

The site auto-deploys: every push to `main` triggers `.github/workflows/publish.yml`, which renders and publishes to GitHub Pages.

```bash
git add .
git commit -m "Draft the agency-erosion chapter"
git push
```

**One-time bootstrap**. Run once locally to create the `gh-pages` branch, then set **Settings → Pages → source: `gh-pages`**:

```bash
quarto publish gh-pages
```

> **Note on cached code:** execution is cached via `freeze: auto`. After changing any code, render locally once (`quarto preview` or `quarto render`) so the `_freeze/` folder updates, then commit it. This lets CI publish the book without re-running the analysis or needing the datasets.

## The index pipeline

Indicators are defined once in `analysis/registry/indicators.yml`. Build the index from the command line:

```bash
python analysis/pipeline/build_index.py
```

It runs on random demo data until `data/processed/indicators.csv` is populated, so nothing here assesses any real territory yet.

## Status

Living document, **v0.x**. Sections will be incomplete, revised, or wrong by design. See the [Preface](https://ai-safe-earth.github.io/AI-Safe-Territory/) for what is done versus planned.

## Contributing

Contributions and critique are welcome, especially attacks on the framework: where does an indicator fail to measure what it claims to? Open an [issue](https://github.com/ai-safe-earth/AI-Safe-Territory/issues), suggest a data source, or propose a territory for the pilot.

## License

CC BY 4.0 for the text and MIT for the code in `analysis/`.

---

<sub>A project under <a href="https://github.com/ai-safe-earth">AI SAFE EARTH</a> · the fourth ring, around communities · AI safety &amp; civic tech</sub>
