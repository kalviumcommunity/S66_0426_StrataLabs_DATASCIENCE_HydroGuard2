"""Demonstrate boxplot visualization for numeric distributions."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_boxplot import save_boxplot


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    columns = ["jun", "jul", "aug", "sep", "monsoon_total"]

    figure_path = PROJECT_ROOT / "outputs" / "figures" / "rainfall_boxplot.png"
    save_boxplot(df, columns, figure_path)

    lines = [
        "# Pandas Boxplot Visualization Demo",
        "",
        f"- Figure generated: {figure_path}",
        f"- Columns visualized: {columns}",
        f"- Record count: {len(df)}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "pandas_boxplot_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Figure generated: {figure_path}")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
