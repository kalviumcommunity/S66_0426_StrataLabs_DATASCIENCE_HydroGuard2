"""Core function definitions used in rainfall analysis."""

from __future__ import annotations


def compute_average(values: list[int]) -> float:
    return sum(values) / len(values)


def monsoon_total(jun: int, jul: int, aug: int, sep: int) -> int:
    return jun + jul + aug + sep


def summarize_record(district: str, total_mm: int) -> str:
    return f"{district}: {total_mm} mm"
