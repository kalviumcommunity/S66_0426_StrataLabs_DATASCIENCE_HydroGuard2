"""Vectorized operations compared with Python loops."""

from __future__ import annotations

import numpy as np


def loop_anomaly(values: list[int], baseline: float) -> list[float]:
    output: list[float] = []
    for value in values:
        output.append(value - baseline)
    return output


def vectorized_anomaly(values: np.ndarray, baseline: float) -> np.ndarray:
    return values - baseline
