---
name: new-chapter
description: Scaffold a new chapter or appendix for the mdBook, register it in src/SUMMARY.md under the right part, and verify the build. Use when adding a page to the book.
---

Add a page to the book. Argument (optional): the chapter title, e.g. `/new-chapter Measuring civic density`.

## Steps

1. **Get the title and placement.** If no title was given, ask for one. Read `src/SUMMARY.md` and ask which part it belongs under — Foundations, The framework, Methodology, Application, or Appendices — unless the title makes it obvious and you can say which you picked.

2. **Pick the filename.** Chapters live in `src/chapters/` and are numbered in reading order (`NN-kebab-title.md`); appendices live in `src/appendices/` and are not numbered. If the new chapter lands mid-sequence, do **not** renumber the existing files — the numbers are a stable prefix, not an index. Use the next free number and place the entry where it belongs in `SUMMARY.md`; say so if the number and the position disagree.

3. **Write the stub** — the house pattern, nothing more:

   ```markdown
   # <Title>

   <div class="callout callout-warning">

   Draft stub — not yet written.

   </div>

   *TODO: write this chapter.*
   ```

4. **Register it in `src/SUMMARY.md`** under the chosen part heading, in reading position. This is required: `create-missing = false`, so an unregistered file is invisible to the book.

5. **Verify**: run `mdbook build` and confirm it succeeds and the page appears in `book/`. Report the file path and where it landed in the table of contents.

## Notes

- If the chapter will show computed numbers, do not paste them. Add a generator function in `analysis/pipeline/render_book.py` writing to `src/generated/`, and pull it in with `{{#include ../generated/<name>.md}}`.
- Citations go through `references.bib` + an anchor in `src/references.md`; see CLAUDE.md.
