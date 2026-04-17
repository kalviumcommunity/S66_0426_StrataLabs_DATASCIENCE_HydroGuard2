"""Helpers for outlier detection using IQR rules."""

from __future__ import annotations

import pandas as pd


def iqr_bounds(series: pd.Series) -> tuple[float, float]:
    q1 = float(series.quantile(0.25))
    q3 = float(series.quantile(0.75))
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return lower, upper


def detect_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    lower, upper = iqr_bounds(df[column])
    return df[(df[column] < lower) | (df[column] > upper)].copy()
