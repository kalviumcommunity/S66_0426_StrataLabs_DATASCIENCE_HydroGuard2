"""Create pandas DataFrames from dictionaries and files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def dataframe_from_dict(data: dict[str, list[object]]) -> pd.DataFrame:
    return pd.DataFrame(data)


def dataframe_from_csv(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)
