# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

An open research book (mdBook) plus the registry-driven Python pipeline that computes its numbers. Indicators are defined once in `analysis/registry/indicators.yml`; the book and the code both read it, so the documented method cannot drift from the computed one.

## Build and preview

```bash
mdbook build          # -> book/
mdbook serve --open   # live preview at localhost:3000
python analysis/pipeline/render_book.py   # regenerate the book's computed tables
ruff check analysis && ruff format analysis   # lint + format the pipeline
```

The Python venv is at `.venv` (Windows: `.venv/Scripts/python.exe`). mdBook is pinned to **0.4.52** in CI — local rustc is 1.82, which cannot build mdBook 0.5, so do not use 0.5-only features.

## Authoring the book

- Prose lives in `src/`. **Every new page must be registered in `src/SUMMARY.md`** under the right part heading — `create-missing = false`, so an unregistered file simply isn't in the book.
- `src/generated/` is written by `analysis/pipeline/render_book.py`. Never hand-edit it. After changing the registry or the pipeline, rerun the generator and commit the result — CI fails the build on a stale diff.
- Chapters pull computed content in with `{{#include ../generated/<name>.md}}`. The Methodology code listing uses an anchor include (`{{#include ../../analysis/pipeline/demo_index.py:demo}}`) so the listing and the numbers beneath it come from the same file.
- Callouts are HTML, not GitHub alerts: `<div class="callout callout-note">` with blank lines around the Markdown inside so it still gets parsed. Kinds: `note`, `warning`, `important`, `tip`. Styled in `theme/asafe.css`.
- Citations: add the entry to `references.bib`, list it in `src/references.md` behind an `<a id="key"></a>` anchor, and link to that anchor inline. There is no bibliography processor.
- Cross-references are plain relative links between `.md` files; mdBook rewrites them to `.html`.

## Writing conventions

- Match the existing voice: plain and declarative, no hype, uncertainty stated openly (this is a living document at v0.x).
- Never invent findings, numbers, or citations. Mark gaps as `*TODO: ...*` rather than filling them with plausible text.
- Keep chapters tight; reference material belongs in the appendices.

## Guardrails

- **Do not change `analysis/registry/indicators.yml`** — indicators, weights, and directions are research decisions, not code edits. Propose, don't edit.
- **Do not push to `main` without an explicit go-ahead**: every push triggers `.github/workflows/publish.yml` and republishes the live site. Committing locally is fine; work goes straight to `main` (no PR flow).
- Nothing in the book assesses a real territory yet. The index runs on random demo data until `data/processed/indicators.csv` exists; never present demo output as a result.

## Theme

`theme/asafe.css` carries the AI SAFE EARTH identity v2 (Archivo/Spectral, square corners, hairline rules) on top of mdBook's built-in themes: light on `light`, dark on `navy`. Define colors as variables for both, not just one.

AI SAFE EARTH is the organization; **AI Safe Territory** is this book. Never merge the two names.

- Artwork is copied from `01_ai-safe-earth-branding/brand/` and lives in `src/assets/brand/` (mdBook copies `src/` non-Markdown files to the output; unknown files under `theme/` are *not* copied). The favicons are the exception: `theme/favicon.svg` and `theme/favicon.png` are recognized theme overrides and carry the core mark (disc + point).
- The sidebar masthead is drawn in CSS from `emblem-territory.svg` (`emblem-territory-inverse.svg` on `navy`). The disc and the ring are the organization and never change; only the place-point carries the project colour — `--asafe-point`, clay `#C4692A` for this book. A project-coloured mark has a 64px floor, which is why the masthead box is 5.6rem: the emblem file includes its own clear space.
- Identity components, authored as HTML in the Markdown: `.ase-label` (letterspaced grotesk kicker), `.ase-plate` (corner ticks), `.ase-scalebar` with `data-scale="0 · 1 · 2 · 3 · 4 km"`. Layout devices come from the map — scale bars, corner ticks, crop marks — never gradients, pills, or badges.
- The identity has no monospace; mono survives only inside code, never in running text.

## Handoff file (read by the project tracker)

One handoff per repository: `handoff.md` at the root. Never start a second one. When work happens inside a plan folder (`docs/refactor/`), keep writing to the root handoff and list the folder under "plans" so the paths stay findable.

Update it at the end of every working session: write it however you like for humans, then append this machine block as the last thing in the file, replacing the previous one.

<!-- pmctl:handoff v1 -->
```json
{
  "project": "laiive",
  "org": "ai safe earth",
  "status": "amber",
  "updated": "2026-08-15",
  "deadline": "2026-09-30",
  "people": ["ana", "dro"],
  "plans": [
    { "name": "refactor", "path": "docs/refactor/", "status": "active" },
    { "name": "billing", "path": "docs/billing/", "status": "done" }
  ],
  "phases": [
    { "name": "Build", "status": "active", "start": "2026-06-11", "end": null, "plan": "refactor",
      "decisions": [{ "date": "2026-07-02", "text": "Postgres over Mongo, reporting needs joins" }] }
  ],
  "blockers": [{ "text": "Waiting on the provider API key", "severity": "high", "owner": "dro", "since": "2026-08-01" }],
  "nextSteps": [{ "title": "Wire auth to the new schema", "est": 3, "owner": "ana", "phase": "Build", "plan": "refactor" }],
  "sessions": [{ "date": "2026-08-12", "model": "opus-5", "credits": 40, "person": "dro", "hours": 2.5 }]
}
```

Rules: "plans" only points at folders; the work itself stays in phases, blockers, nextSteps and sessions, each tagged with "plan" when it belongs to one. ISO dates, null when unknown. status green|amber|red. phase status done|active|planned. severity critical|high|medium|low. est in working days. One sessions entry per working session. Append decisions and sessions, never rewrite past ones. Commit the handoff on whatever branch you are working in. No emoji.