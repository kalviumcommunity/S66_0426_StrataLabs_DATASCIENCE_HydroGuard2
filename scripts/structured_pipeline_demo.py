"""Run a structured and reusable rainfall analysis flow."""

from __future__ import annotations

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.structured_pipeline import build_report_lines, load_processed_rows


def main() -> None:
    processed_path = (
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    report_path = PROJECT_ROOT / "outputs" / "reports" / "structured_pipeline_demo.md"

    rows = load_processed_rows(processed_path)
    report_lines = build_report_lines(rows)
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
