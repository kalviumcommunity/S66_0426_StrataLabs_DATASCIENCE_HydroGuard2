"""Demonstrate missing-value detection in pandas DataFrames."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_missing_detection import missing_counts, rows_with_missing


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    df_with_missing = df.copy()
    df_with_missing.loc[1, "aug"] = None
    df_with_missing.loc[4, "monsoon_total"] = None

    counts = missing_counts(df_with_missing)
    missing_rows = rows_with_missing(df_with_missing)

    lines = [
        "# Pandas Missing Value Detection Demo",
        "",
        f"- Missing counts: {counts}",
        f"- Rows containing missing values: {missing_rows}",
    ]

    report_path = (
        PROJECT_ROOT / "outputs" / "reports" / "pandas_missing_detection_demo.md"
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
