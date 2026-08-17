<img src="./.github/brand/mark.svg" alt="AI SAFE EARTH" width="72">

# AI Safe Territory

> The open research **book** of the *AI Safe Territory* project, under the AI SAFE EARTH umbrella. Defining, measuring, and mapping how resilient places (towns, cities, regions) are to the erosion of human agency. **The book is written in Spanish**; an English edition follows.

![Pillar](https://img.shields.io/badge/RESEARCH-IN_PROGRESS-C4692A?style=flat-square&labelColor=131A21)
[![Read the book](https://img.shields.io/badge/READ-THE_BOOK-1F5D7A?style=flat-square&labelColor=131A21)](https://ai-safe-earth.github.io/AI-Safe-Territory/)
[![mdBook](https://img.shields.io/badge/BUILT_WITH-MDBOOK-4A5560?style=flat-square&labelColor=131A21)](https://rust-lang.github.io/mdBook/)
[![Umbrella](https://img.shields.io/badge/AI_SAFE_EARTH-open_umbrella-131A21?style=flat-square&labelColor=131A21)](https://github.com/ai-safe-earth)

Part of the [AI SAFE EARTH](https://github.com/ai-safe-earth) umbrella. This repository is the core project of the **Research** pillar and the source of the materials produced by the **Communicate** pillar (the territorial map and the community-leader guides).

## Read it

The living version is published as a website and rebuilds on every push:

**→ [ai-safe-earth.github.io/AI-Safe-Territory](https://ai-safe-earth.github.io/AI-Safe-Territory/)**

It is public, anyone can read it, no account needed, and because it is continuously published, it always reflects the latest commit.

## What this is

A place is more or less resilient to the erosion of human agency depending on its inherent structure: how distributed its decision-making is, how redundant its communication channels are, how dense its civic life is, how exposed it is to capture by a single mediating layer. This repository turns that idea into a transparent, reproducible evaluation index and maps the result.

It holds three things that stay in sync with each other:

- an **mdBook**. The narrative, framework, and methodology, rendered to the website above;
- a **registry-driven index pipeline** (`analysis/`). Every indicator defined once and read by both the book and the code, so the documented method can never drift from the computed one;
- the **data and outputs** behind the index.

## Repository structure

```
book.toml                book config: title, theme, build settings
src/SUMMARY.md           the table of contents: parts, chapters, appendices
src/index.md             preface
src/chapters/            the four parts: Foundations, Framework, Methodology, Application
src/appendices/          codebook, reproducibility, glossary
src/references.md        the reference list; references.bib is the machine-readable source
src/generated/           computed tables written by the pipeline (do not edit by hand)
theme/asafe.css          AI SAFE EARTH identity on top of mdBook's themes
analysis/
  registry/indicators.yml   single source of truth for indicators
  pipeline/build_index.py   runnable index pipeline
  pipeline/demo_index.py    the demo shown verbatim in the Methodology chapter
  pipeline/render_book.py   writes the computed content into src/generated/
data/                    raw/ (untracked) + processed/indicators.csv
outputs/                 generated index.csv, figures
.github/workflows/       builds and deploys to GitHub Pages on push
```

## Develop and write locally

You write against a private, live preview, you never need to publish just to see your work. Think of it as two speeds: **`mdbook serve` is your private writing desk** (instant, local, just you), and **`git push` is the printing press** (public, for everyone).

**Prerequisites:** [mdBook](https://rust-lang.github.io/mdBook/guide/installation.html) (`cargo install mdbook`, or a prebuilt binary) and Python 3.10+.

```bash
# 1. set up the Python environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. regenerate the computed tables (only needed after changing the registry or pipeline)
python analysis/pipeline/render_book.py

# 3. start the live, auto-reloading preview
mdbook serve --open
```

This opens the book locally (`http://localhost:3000`) and refreshes the moment you save. Then edit the `.md` files in `src/chapters/`, they are plain Markdown. To add a chapter, create the `.md` under `src/` and register its path under the right part heading in `src/SUMMARY.md`.

Callouts are plain HTML styled by `theme/asafe.css` — `<div class="callout callout-note">` (kinds: `note`, `warning`, `important`, `tip`), with blank lines around the Markdown inside so it still gets parsed. Cite a work by adding an entry to `references.bib`, listing it in `src/references.md` with an `<a id="key"></a>` anchor, and linking to that anchor inline.

## Publishing

The site auto-deploys: every push to `main` triggers `.github/workflows/publish.yml`, which regenerates the computed content, builds the book, and publishes it to GitHub Pages.

```bash
git add .
git commit -m "Draft the agency-erosion chapter"
git push
```

**One-time bootstrap**. Set **Settings → Pages → Source: GitHub Actions**.

> **Note on computed content:** mdBook does not execute code. Anything in the book that must agree with the analysis is written to `src/generated/` by `analysis/pipeline/render_book.py` and pulled in with `{{#include}}`. Those files are committed; CI regenerates them and fails the build if they are stale, so text and code cannot drift apart silently.

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
