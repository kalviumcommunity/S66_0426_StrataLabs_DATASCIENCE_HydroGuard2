"""Demonstrate pandas indexing and slicing operations."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_indexing import (
    select_columns,
    select_row_slice,
    select_rows_by_condition,
)


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )

    col_df = select_columns(df, ["district", "monsoon_total"])
    slice_df = select_row_slice(df, 0, 3)
    condition_df = select_rows_by_condition(df, 1000)

    lines = [
        "# Pandas Indexing and Slicing Demo",
        "",
        f"- Selected columns shape: {col_df.shape}",
        f"- Row slice shape: {slice_df.shape}",
        f"- Condition rows shape: {condition_df.shape}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "pandas_indexing_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
