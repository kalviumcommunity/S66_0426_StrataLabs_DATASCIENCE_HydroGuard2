"""Boxplot visualization helpers for pandas columns."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_boxplot(df: pd.DataFrame, columns: list[str], output_path: Path) -> None:
    plt.figure(figsize=(8, 5))
    df[columns].plot(kind="box", patch_artist=True)
    plt.title("Boxplot for Rainfall Distributions")
    plt.ylabel("Rainfall / Total")
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()
