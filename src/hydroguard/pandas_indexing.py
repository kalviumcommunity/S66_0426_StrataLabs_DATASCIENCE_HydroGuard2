"""Helpers for pandas row and column selection."""

from __future__ import annotations

import pandas as pd


def select_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    return df.loc[:, columns]


def select_row_slice(df: pd.DataFrame, start: int, stop: int) -> pd.DataFrame:
    return df.iloc[start:stop, :]


def select_rows_by_condition(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    return df.loc[
        df["monsoon_total"] >= threshold, ["district", "year", "monsoon_total"]
    ]
