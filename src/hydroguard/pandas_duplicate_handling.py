"""Helpers to detect and remove duplicate rows."""

from __future__ import annotations

import pandas as pd


def duplicate_count(df: pd.DataFrame) -> int:
    return int(df.duplicated().sum())


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)
