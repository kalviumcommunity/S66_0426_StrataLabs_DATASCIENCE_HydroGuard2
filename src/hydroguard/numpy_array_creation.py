"""Create NumPy arrays from Python lists."""

from __future__ import annotations

import numpy as np


def monthly_list_to_array(monthly_values: list[int]) -> np.ndarray:
    return np.array(monthly_values, dtype=np.int64)


def matrix_from_rows(rows: list[list[int]]) -> np.ndarray:
    return np.array(rows, dtype=np.int64)
