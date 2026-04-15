"""Create pandas Series from lists and arrays."""

from __future__ import annotations

import numpy as np
import pandas as pd


def series_from_list(values: list[int], name: str) -> pd.Series:
    return pd.Series(values, name=name)


def series_from_array(values: np.ndarray, name: str) -> pd.Series:
    return pd.Series(values, name=name)
