"""Histogram visualization helpers for pandas numeric columns."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_histogram(df: pd.DataFrame, column: str, output_path: Path) -> None:
    plt.figure(figsize=(8, 5))
    df[column].plot(
        kind="hist", bins=6, color="#2a9d8f", edgecolor="#264653", alpha=0.85
    )
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()
