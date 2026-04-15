"""Structured and reusable rainfall analysis pipeline helpers."""

from __future__ import annotations

import csv
from pathlib import Path


def load_processed_rows(processed_csv_path: Path) -> list[dict[str, str]]:
    with processed_csv_path.open("r", newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def compute_average_monsoon_total(rows: list[dict[str, str]]) -> float:
    totals = [int(row["monsoon_total"]) for row in rows]
    return sum(totals) / len(totals)


def build_report_lines(rows: list[dict[str, str]]) -> list[str]:
    average_total = compute_average_monsoon_total(rows)
    lines = [
        "# Structured Pipeline Demo",
        "",
        f"- Records loaded: {len(rows)}",
        f"- Average monsoon total: {average_total:.2f} mm",
        "",
        "## District-Year Rows",
    ]
    for row in rows:
        lines.append(f"- {row['district']} {row['year']} -> {row['monsoon_total']} mm")
    return lines
