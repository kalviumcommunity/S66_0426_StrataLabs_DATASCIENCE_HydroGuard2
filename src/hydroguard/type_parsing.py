"""Utilities for numeric and string rainfall parsing."""

from __future__ import annotations


def normalize_district_name(name: str) -> str:
    cleaned = name.strip().lower().replace(" ", "_")
    return cleaned


def parse_rainfall_value(value: str) -> float:
    return float(value.strip())


def rainfall_record_summary(district: str, rainfall_text: str) -> str:
    normalized_district = normalize_district_name(district)
    rainfall_mm = parse_rainfall_value(rainfall_text)
    return f"district={normalized_district}, rainfall_mm={rainfall_mm:.1f}"
