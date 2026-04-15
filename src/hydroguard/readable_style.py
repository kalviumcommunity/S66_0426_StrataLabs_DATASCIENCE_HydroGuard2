"""Readable naming patterns for HydroGuard scripts."""

from __future__ import annotations


def rainfall_mm_to_cm(rainfall_mm: float) -> float:
    return rainfall_mm / 10.0


def build_status_message(district_name: str, monsoon_total_mm: int) -> str:
    return f"{district_name} recorded {monsoon_total_mm} mm during monsoon season"
