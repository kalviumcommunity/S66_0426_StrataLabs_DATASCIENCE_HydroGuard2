"""Demonstrate column-level summary statistics in pandas."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_summary_stats import numeric_summary


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    summary = numeric_summary(df, "monsoon_total")

    lines = [
        "# Pandas Summary Statistics Demo",
        "",
        f"- Column: monsoon_total",
        f"- Summary: {summary}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "pandas_summary_stats_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
