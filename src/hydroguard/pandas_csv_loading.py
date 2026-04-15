"""CSV loading helpers for pandas workflows."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv_default(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def load_csv_with_types(csv_path: Path) -> pd.DataFrame:
    dtype_map = {
        "district": "string",
        "year": "int64",
        "jun": "int64",
        "jul": "int64",
        "aug": "int64",
        "sep": "int64",
        "monsoon_total": "int64",
    }
    return pd.read_csv(csv_path, dtype=dtype_map)
