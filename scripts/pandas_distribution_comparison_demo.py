"""Demonstrate comparing distributions across multiple DataFrame columns."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_distribution_comparison import compare_columns


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    comparison = compare_columns(df, ["jun", "jul", "aug", "sep", "monsoon_total"])

    lines = [
        "# Pandas Distribution Comparison Demo",
        "",
        f"- Compared columns: {list(comparison.index)}",
        f"- Means: {comparison['mean'].round(2).to_dict()}",
        f"- Std dev: {comparison['std'].round(2).to_dict()}",
    ]

    report_path = (
        PROJECT_ROOT / "outputs" / "reports" / "pandas_distribution_comparison_demo.md"
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
