"""Demo run of the index pipeline, shown verbatim in the book.

This file is both included as a code listing in
`src/chapters/09-constructing-the-index.md` and executed by
`analysis/pipeline/render_book.py` to produce the result table shown beneath it,
so the listing and the numbers can never drift apart.
"""

# ANCHOR: demo
import numpy as np
import pandas as pd

from build_index import build, load_registry


def demo() -> pd.DataFrame:
    registry = load_registry()

    # Demo data so the book renders before real data lands.
    rng = np.random.default_rng(0)
    cols = [i["id"] for i in registry["indicators"]]
    demo_data = pd.DataFrame(
        rng.random((6, len(cols))),
        index=[f"territory_{i}" for i in range(1, 7)],
        columns=cols,
    )

    result = build(demo_data, registry)
    return result[["score", "rank"]]


# ANCHOR_END: demo
