"""Demonstrate outlier detection with simple IQR rules."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_outliers import detect_outliers, iqr_bounds


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    df_with_outlier = pd.concat(
        [
            df,
            pd.DataFrame(
                [
                    {
                        "district": "test_outlier",
                        "year": 2023,
                        "jun": 400,
                        "jul": 600,
                        "aug": 650,
                        "sep": 500,
                        "monsoon_total": 2150,
                    }
                ]
            ),
        ],
        ignore_index=True,
    )

    lower, upper = iqr_bounds(df_with_outlier["monsoon_total"])
    outliers = detect_outliers(df_with_outlier, "monsoon_total")

    lines = [
        "# Pandas Outlier Detection Demo",
        "",
        f"- IQR lower bound: {round(lower, 2)}",
        f"- IQR upper bound: {round(upper, 2)}",
        f"- Outlier rows detected: {len(outliers)}",
        f"- Outlier districts: {outliers['district'].tolist()}",
    ]

    report_path = (
        PROJECT_ROOT / "outputs" / "reports" / "pandas_outlier_detection_demo.md"
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
