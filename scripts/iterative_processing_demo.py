"""Demonstrate for/while loops for rainfall processing."""

from __future__ import annotations

import csv
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.iterative import first_above_threshold, running_totals


def main() -> None:
    processed_path = (
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    with processed_path.open("r", newline="", encoding="utf-8") as csv_file:
        first_row = next(csv.DictReader(csv_file))

    month_values = [int(first_row[month]) for month in ("jun", "jul", "aug", "sep")]
    cumulative = running_totals(month_values)
    threshold_index = first_above_threshold(cumulative, 800)

    crossed_at = "not crossed"
    if threshold_index >= 0:
        crossed_at = ("jun", "jul", "aug", "sep")[threshold_index]

    report_lines = [
        "# Iterative Processing Demo",
        "",
        f"- Monthly values: {month_values}",
        f"- Cumulative values: {cumulative}",
        f"- First month cumulative exceeded 800 mm: {crossed_at}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "iterative_processing_demo.md"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
