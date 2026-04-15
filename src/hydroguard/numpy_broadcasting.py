"""Simple NumPy broadcasting helpers."""

from __future__ import annotations

import numpy as np


def add_month_offsets(rainfall_matrix: np.ndarray, offsets: np.ndarray) -> np.ndarray:
    return rainfall_matrix + offsets


def scale_by_factors(rainfall_matrix: np.ndarray, factors: np.ndarray) -> np.ndarray:
    return rainfall_matrix * factors
