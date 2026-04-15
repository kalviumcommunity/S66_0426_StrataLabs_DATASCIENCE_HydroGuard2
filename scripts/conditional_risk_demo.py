"""Apply conditional statements to rainfall risk logic."""

from __future__ import annotations

import csv
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.risk_rules import action_for_risk, classify_risk


def main() -> None:
    processed_path = (
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    with processed_path.open("r", newline="", encoding="utf-8") as csv_file:
        rows = list(csv.DictReader(csv_file))

    report_lines = ["# Conditional Risk Demo", ""]
    for row in rows:
        monsoon_total = int(row["monsoon_total"])
        risk = classify_risk(monsoon_total)
        action = action_for_risk(risk)
        report_lines.append(f"- {row['district']} {row['year']}: {risk} ({action})")

    report_path = PROJECT_ROOT / "outputs" / "reports" / "conditional_risk_demo.md"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
