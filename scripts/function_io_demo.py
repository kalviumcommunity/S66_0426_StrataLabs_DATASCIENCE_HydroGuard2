"""Demonstrate passing values into functions and returning results."""

from __future__ import annotations

import csv
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.function_io import anomaly_report_line, rainfall_anomaly


def main() -> None:
    processed_path = (
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    with processed_path.open("r", newline="", encoding="utf-8") as csv_file:
        rows = list(csv.DictReader(csv_file))

    totals = [int(row["monsoon_total"]) for row in rows]
    baseline = sum(totals) / len(totals)

    report_lines = [
        "# Function Input/Output Demo",
        "",
        f"- Baseline: {baseline:.2f} mm",
        "",
    ]
    for row in rows:
        anomaly_value = rainfall_anomaly(int(row["monsoon_total"]), baseline)
        report_lines.append(
            anomaly_report_line(row["district"], int(row["year"]), anomaly_value)
        )

    report_path = PROJECT_ROOT / "outputs" / "reports" / "function_io_demo.md"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
