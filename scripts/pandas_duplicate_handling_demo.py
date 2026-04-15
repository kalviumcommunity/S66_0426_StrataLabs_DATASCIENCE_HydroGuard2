"""Demonstrate duplicate detection and removal in pandas DataFrames."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_duplicate_handling import duplicate_count, remove_duplicates


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    with_duplicate = pd.concat([df, df.iloc[[0]]], ignore_index=True)

    duplicates = duplicate_count(with_duplicate)
    cleaned_df = remove_duplicates(with_duplicate)

    lines = [
        "# Pandas Duplicate Handling Demo",
        "",
        f"- Rows with duplicate version: {len(with_duplicate)}",
        f"- Duplicate rows detected: {duplicates}",
        f"- Rows after removal: {len(cleaned_df)}",
    ]

    report_path = (
        PROJECT_ROOT / "outputs" / "reports" / "pandas_duplicate_handling_demo.md"
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
