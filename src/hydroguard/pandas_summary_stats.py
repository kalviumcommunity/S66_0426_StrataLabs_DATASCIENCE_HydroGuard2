"""Helpers for summary statistics on individual columns."""

from __future__ import annotations

import pandas as pd


def numeric_summary(df: pd.DataFrame, column: str) -> dict[str, float]:
    series = df[column]
    return {
        "count": float(series.count()),
        "mean": float(series.mean()),
        "std": float(series.std()),
        "min": float(series.min()),
        "median": float(series.median()),
        "max": float(series.max()),
    }
