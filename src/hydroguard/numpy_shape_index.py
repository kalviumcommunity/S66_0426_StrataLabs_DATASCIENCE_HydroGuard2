"""Describe NumPy array shape, dimensions, and index access."""

from __future__ import annotations

import numpy as np


def array_metadata(values: np.ndarray) -> dict[str, object]:
    return {
        "shape": values.shape,
        "ndim": values.ndim,
        "size": values.size,
    }


def sample_index_values(values: np.ndarray) -> dict[str, int]:
    return {
        "first": int(values[0, 0]),
        "last": int(values[-1, -1]),
        "middle": int(values[0, 2]),
    }
