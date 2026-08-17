---
name: book-check
description: Preflight the book before pushing — regenerate computed content, fail on a stale src/generated/ diff, build with mdBook, and check includes and intra-book links. Use before committing or publishing book changes.
---

Run the same checks CI runs, plus link integrity, so a push doesn't turn the site red. Report results as a short pass/fail list; do not fix anything without saying what you're changing.

## Steps

1. **Regenerate computed content**

   ```bash
   .venv/Scripts/python.exe analysis/pipeline/render_book.py
   ```

   (`python` on non-Windows.)

2. **Staleness check** — the check CI enforces:

   ```bash
   git diff --stat -- src/generated
   ```

   Any diff means the committed tables disagreed with the code. That is a **fail**: report the diff and note the regenerated files must be committed alongside the change.

3. **Build**

   ```bash
   mdbook build
   ```

   Treat warnings about unresolved `{{#include}}` paths or missing anchors as failures — mdBook renders the literal include text into the page rather than erroring.

4. **Check includes resolved.** For each `{{#include ...}}` in `src/`, confirm the target file (and anchor, if one is named) exists, and that no rendered page in `book/` still contains the literal string `{{#include`.

5. **Check intra-book links.** For each relative `.md` link in `src/`, confirm the target exists and, where a `#anchor` is given, that the anchor is present in the rendered HTML. Flag any link into `src/references.md` whose anchor has no matching `<a id="...">`.

6. **Check SUMMARY coverage.** List any `.md` under `src/` that is not referenced from `src/SUMMARY.md` (excluding `src/generated/`, which is included, not linked). Those pages are not in the book.

## Report

One line per check: `PASS` / `FAIL` with the specific file and reason. Finish with whether it is safe to push. Remember that pushing to `main` republishes the live site — do not push without an explicit go-ahead.
