"""Helpers to compare distributions across multiple columns."""

from __future__ import annotations

import pandas as pd


def compare_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    summary = {
        column: {
            "mean": float(df[column].mean()),
            "median": float(df[column].median()),
            "std": float(df[column].std()),
            "min": float(df[column].min()),
            "max": float(df[column].max()),
        }
        for column in columns
    }
    return pd.DataFrame.from_dict(summary, orient="index")
