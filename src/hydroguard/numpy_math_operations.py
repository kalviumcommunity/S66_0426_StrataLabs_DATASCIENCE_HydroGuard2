"""Basic mathematical operations on NumPy arrays."""

from __future__ import annotations

import numpy as np


def add_constant(values: np.ndarray, constant: int) -> np.ndarray:
    return values + constant


def multiply_constant(values: np.ndarray, factor: float) -> np.ndarray:
    return values * factor


def combined_sum(values_a: np.ndarray, values_b: np.ndarray) -> np.ndarray:
    return values_a + values_b
