"""Demonstrate readable variable names with PEP 8 style basics."""

from __future__ import annotations

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.readable_style import build_status_message, rainfall_mm_to_cm


def main() -> None:
    district_name = "coastal_north"
    monsoon_total_mm = 1147
    monsoon_total_cm = rainfall_mm_to_cm(monsoon_total_mm)
    status_message = build_status_message(district_name, monsoon_total_mm)

    report_lines = [
        "# Readable Style Demo",
        "",
        f"- {status_message}",
        f"- Converted total: {monsoon_total_cm:.2f} cm",
        "- Variable names follow snake_case and semantic meaning",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "readable_style_demo.md"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
