"""Generate the book's computed content into `src/generated/`.

mdBook does not execute code, so anything in the book that must agree with the
analysis is produced here and pulled in with `{{#include}}`. Run this before
`mdbook build` / `mdbook serve`:

    python analysis/pipeline/render_book.py

The outputs are committed, so the book still builds without Python; CI
regenerates them on every push, so a drift between code and text shows up as a
diff rather than as a wrong number in the published site.
"""

import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / "src" / "generated"

sys.path.insert(0, str(HERE))

from build_index import load_registry  # noqa: E402
from demo_index import demo  # noqa: E402

BANNER = "<!-- Generado por analysis/pipeline/render_book.py — no editar a mano. -->\n\n"


def to_markdown(df: pd.DataFrame, caption: str, index: bool = False) -> str:
    table = df.to_markdown(index=index)
    return f"{BANNER}{table}\n\n*{caption}*\n"


def indicators_table() -> str:
    # Only the column labels and the caption are translated. The cell values —
    # indicator name, pillar, direction — come from the registry and stay in its
    # language: hard-coding Spanish names here is exactly the drift the registry
    # exists to prevent. Bilingual registry fields are a proposal, not an edit.
    registry = load_registry()
    df = pd.DataFrame(registry["indicators"])[["id", "name", "pillar", "direction", "weight"]]
    df.columns = ["id", "indicador", "pilar", "dirección", "peso"]
    return to_markdown(df, "Conjunto preliminar de indicadores (generado desde el registro).")


def demo_index_table() -> str:
    df = demo().reset_index().rename(columns={"index": "territorio"})
    df.columns = ["territorio", "puntuación", "rango"]
    return to_markdown(
        df,
        "Puntuaciones y rangos del índice de demostración "
        "(datos aleatorios — no es una evaluación).",
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    written = {
        "indicators-table.md": indicators_table(),
        "demo-index.md": demo_index_table(),
    }
    for name, text in written.items():
        (OUT / name).write_text(text, encoding="utf-8")
        print(f"wrote {(OUT / name).relative_to(ROOT)}")


if __name__ == "__main__":
    main()
