"""Demonstrate scatter plot analysis between rainfall variables."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_scatter import save_scatter


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )

    figure_path = PROJECT_ROOT / "outputs" / "figures" / "jun_vs_monsoon_scatter.png"
    save_scatter(df, "jun", "monsoon_total", figure_path)

    correlation = float(df[["jun", "monsoon_total"]].corr().iloc[0, 1])
    lines = [
        "# Pandas Scatter Relationship Demo",
        "",
        f"- Figure generated: {figure_path}",
        "- Variables: jun vs monsoon_total",
        f"- Correlation coefficient: {round(correlation, 4)}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "pandas_scatter_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Figure generated: {figure_path}")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
