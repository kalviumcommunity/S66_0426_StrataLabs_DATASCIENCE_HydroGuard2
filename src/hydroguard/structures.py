"""List, tuple, and dictionary helpers for rainfall modeling."""

from __future__ import annotations


def build_month_tuple() -> tuple[str, str, str, str]:
    return ("jun", "jul", "aug", "sep")


def district_totals(records: list[dict[str, str]]) -> dict[str, list[int]]:
    totals_by_district: dict[str, list[int]] = {}
    for record in records:
        district = record["district"]
        totals_by_district.setdefault(district, []).append(int(record["monsoon_total"]))
    return totals_by_district


def top_district(summary: dict[str, list[int]]) -> tuple[str, float]:
    district, totals = max(
        summary.items(), key=lambda item: sum(item[1]) / len(item[1])
    )
    return district, sum(totals) / len(totals)
