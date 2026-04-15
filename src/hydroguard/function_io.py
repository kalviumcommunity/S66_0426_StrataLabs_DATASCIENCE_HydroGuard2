"""Function input and output patterns for rainfall analysis."""

from __future__ import annotations


def rainfall_anomaly(current_total: int, baseline_total: float) -> float:
    return current_total - baseline_total


def anomaly_report_line(district: str, year: int, anomaly_value: float) -> str:
    return f"{district} ({year}) anomaly: {anomaly_value:+.2f} mm"
