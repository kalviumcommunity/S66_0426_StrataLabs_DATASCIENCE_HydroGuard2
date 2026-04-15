"""Helpers for DataFrame shape and dtype inspection."""

from __future__ import annotations

import pandas as pd


def dataframe_shape(df: pd.DataFrame) -> tuple[int, int]:
    return df.shape


def dataframe_dtypes(df: pd.DataFrame) -> dict[str, str]:
    return {column: str(dtype) for column, dtype in df.dtypes.items()}
