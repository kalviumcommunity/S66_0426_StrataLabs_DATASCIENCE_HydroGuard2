"""Demonstrate time-based trend detection with a line plot."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_line_trend import save_trend_line


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )

    figure_path = PROJECT_ROOT / "outputs" / "figures" / "monsoon_total_trend_line.png"
    save_trend_line(df, figure_path)

    lines = [
        "# Pandas Line Trend Demo",
        "",
        f"- Figure generated: {figure_path}",
        "- Trend metric: mean monsoon_total grouped by year",
        f"- Source rows: {len(df)}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "pandas_line_trend_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Figure generated: {figure_path}")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
