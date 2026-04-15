"""Loop-based rainfall processing helpers."""

from __future__ import annotations


def running_totals(values: list[int]) -> list[int]:
    totals: list[int] = []
    current = 0
    for value in values:
        current += value
        totals.append(current)
    return totals


def first_above_threshold(values: list[int], threshold: int) -> int:
    index = 0
    while index < len(values):
        if values[index] > threshold:
            return index
        index += 1
    return -1
