"""Demonstrate defining and calling Python functions."""

from __future__ import annotations

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.functions_core import (
    compute_average,
    monsoon_total,
    summarize_record,
)


def main() -> None:
    yearly_totals = [
        monsoon_total(210, 320, 295, 260),
        monsoon_total(225, 338, 310, 274),
    ]
    average_total = compute_average(yearly_totals)
    summary_line = summarize_record("coastal_north", int(average_total))

    report_lines = [
        "# Function Definition and Call Demo",
        "",
        f"- Yearly totals: {yearly_totals}",
        f"- Average total: {average_total:.2f}",
        f"- Summary line: {summary_line}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "functions_demo.md"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
