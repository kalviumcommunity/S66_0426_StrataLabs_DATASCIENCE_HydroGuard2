"""Helpers for standardizing column names and data formats."""

from __future__ import annotations

import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    copied = df.copy()
    copied.columns = [
        column.strip().lower().replace(" ", "_") for column in copied.columns
    ]
    return copied


def standardize_district_values(df: pd.DataFrame) -> pd.DataFrame:
    copied = df.copy()
    copied["district"] = (
        copied["district"]
        .astype("string")
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )
    return copied
