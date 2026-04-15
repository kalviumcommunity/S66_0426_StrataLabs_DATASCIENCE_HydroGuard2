"""Conditional flood-risk rules for rainfall totals."""

from __future__ import annotations


def classify_risk(monsoon_total: int) -> str:
    if monsoon_total >= 1100:
        return "High"
    if monsoon_total >= 900:
        return "Medium"
    return "Low"


def action_for_risk(risk_level: str) -> str:
    if risk_level == "High":
        return "Trigger district alert and prepare evacuation plans"
    if risk_level == "Medium":
        return "Increase monitoring and pre-position response teams"
    return "Continue routine observation"
