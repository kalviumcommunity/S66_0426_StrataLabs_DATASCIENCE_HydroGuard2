"""Helpers to detect missing values in DataFrames."""

from __future__ import annotations

import pandas as pd


def missing_counts(df: pd.DataFrame) -> dict[str, int]:
    return {column: int(count) for column, count in df.isna().sum().items()}


def rows_with_missing(df: pd.DataFrame) -> int:
    return int(df.isna().any(axis=1).sum())
