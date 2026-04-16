"""Demonstrate histogram visualization for rainfall distributions."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_histogram import save_histogram


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )

    figure_path = PROJECT_ROOT / "outputs" / "figures" / "monsoon_total_histogram.png"
    save_histogram(df, "monsoon_total", figure_path)

    lines = [
        "# Pandas Histogram Visualization Demo",
        "",
        f"- Figure generated: {figure_path}",
        f"- Column visualized: monsoon_total",
        f"- Record count: {len(df)}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "pandas_histogram_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Figure generated: {figure_path}")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
