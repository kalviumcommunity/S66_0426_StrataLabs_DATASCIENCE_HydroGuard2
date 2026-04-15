"""Demonstrate numeric and string parsing for rainfall records."""

from __future__ import annotations

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.type_parsing import rainfall_record_summary


def main() -> None:
    report_lines = [
        "# Numeric and String Parsing Demo",
        "",
        rainfall_record_summary("Coastal North", " 322.5 "),
        rainfall_record_summary("Delta West", " 259 "),
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "numeric_string_demo.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
