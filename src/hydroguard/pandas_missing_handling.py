"""Helpers for handling missing values with drop and fill strategies."""

from __future__ import annotations

import pandas as pd


def drop_missing_rows(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(axis=0)


def fill_missing_with_value(
    df: pd.DataFrame, column: str, value: float
) -> pd.DataFrame:
    copied = df.copy()
    copied[column] = copied[column].fillna(value)
    return copied
