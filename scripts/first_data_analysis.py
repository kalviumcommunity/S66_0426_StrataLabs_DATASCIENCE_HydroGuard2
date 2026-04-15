"""Run first basic analysis on processed rainfall data."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


def parse_rows(processed_path: Path) -> list[dict[str, str]]:
    with processed_path.open("r", newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def build_summary(rows: list[dict[str, str]]) -> str:
    totals = [int(row["monsoon_total"]) for row in rows]
    by_district: dict[str, list[int]] = defaultdict(list)
    for row in rows:
        by_district[row["district"]].append(int(row["monsoon_total"]))

    highest_row = max(rows, key=lambda row: int(row["monsoon_total"]))
    average_total = sum(totals) / len(totals)

    district_lines = []
    for district, values in sorted(by_district.items()):
        district_average = sum(values) / len(values)
        district_lines.append(f"- {district}: {district_average:.2f} mm")

    return "\n".join(
        [
            "# First Analysis Summary",
            "",
            f"- Records analyzed: {len(rows)}",
            f"- Average monsoon total: {average_total:.2f} mm",
            (
                "- Highest monsoon total: "
                f"{highest_row['district']} ({highest_row['year']}) -> {highest_row['monsoon_total']} mm"
            ),
            "",
            "## Average by District",
            *district_lines,
        ]
    )


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    processed_path = (
        project_root / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    report_path = project_root / "outputs" / "reports" / "first_analysis_summary.md"

    rows = parse_rows(processed_path)
    summary = build_summary(rows)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(summary + "\n", encoding="utf-8")

    print(f"Processed source: {processed_path}")
    print(f"Report generated: {report_path}")
    print("Analysis complete.")


if __name__ == "__main__":
    main()
