"""Registry-driven Territorial AI-Safety Index — minimal starter (rung 1, built to climb).

Reads indicator definitions from analysis/registry/indicators.yml, normalizes each
indicator (min-max), applies direction and weights, and aggregates to a 0-100 score.

Swap min-max for the chosen normalization and linear for geometric aggregation as the
method matures (see the Methodology chapters). Keep this file the single computation path.
"""
from pathlib import Path
import yaml
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "analysis" / "registry" / "indicators.yml"
DATA = ROOT / "data" / "processed" / "indicators.csv"   # wide: rows=territories, cols=indicator ids
OUT = ROOT / "outputs"


def load_registry(path: Path = REGISTRY) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def minmax(s: pd.Series, direction: str) -> pd.Series:
    lo, hi = s.min(), s.max()
    if hi == lo:
        return pd.Series(50.0, index=s.index)
    scaled = (s - lo) / (hi - lo) * 100
    return scaled if direction == "positive" else 100 - scaled


def build(df: pd.DataFrame, registry: dict) -> pd.DataFrame:
    normed = pd.DataFrame(index=df.index)
    weights = {}
    for ind in registry["indicators"]:
        col = ind["id"]
        if col not in df.columns:
            continue  # indicator defined but no data yet
        normed[col] = minmax(df[col], ind["direction"])
        weights[col] = float(ind.get("weight", 1.0))
    w = pd.Series(weights)
    # Transparent linear aggregation. Replace with geometric mean once justified.
    score = (normed[w.index] * w).sum(axis=1) / w.sum()
    out = normed.copy()
    out["score"] = score.round(2)
    out["rank"] = score.rank(ascending=False).astype(int)
    return out.sort_values("score", ascending=False)


if __name__ == "__main__":
    registry = load_registry()
    if DATA.exists():
        df = pd.read_csv(DATA, index_col=0)
    else:
        import numpy as np
        rng = np.random.default_rng(0)
        cols = [i["id"] for i in registry["indicators"]]
        df = pd.DataFrame(
            rng.random((5, len(cols))),
            index=[f"territory_{i}" for i in range(1, 6)],
            columns=cols,
        )
        print("No data/processed/indicators.csv found — using random demo data.\n")
    result = build(df, registry)
    OUT.mkdir(exist_ok=True)
    result.to_csv(OUT / "index.csv")
    print(result[["score", "rank"]].to_string())
