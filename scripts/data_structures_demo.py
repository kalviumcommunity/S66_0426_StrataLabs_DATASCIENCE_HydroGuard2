"""Demonstrate lists, tuples, and dictionaries on rainfall records."""

from __future__ import annotations

import csv
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.structures import build_month_tuple, district_totals, top_district


def main() -> None:
    processed_path = (
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    with processed_path.open("r", newline="", encoding="utf-8") as csv_file:
        records = list(csv.DictReader(csv_file))

    month_tuple = build_month_tuple()
    summary = district_totals(records)
    best_district, average_total = top_district(summary)

    report_lines = [
        "# Data Structures Demo",
        "",
        f"- Month tuple: {month_tuple}",
        f"- District keys: {list(summary.keys())}",
        f"- Highest average district: {best_district} ({average_total:.2f} mm)",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "data_structures_demo.md"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
