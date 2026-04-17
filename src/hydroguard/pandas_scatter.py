"""Scatter plot helpers for variable relationship analysis."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_scatter(df: pd.DataFrame, x_col: str, y_col: str, output_path: Path) -> None:
    plt.figure(figsize=(8, 5))
    plt.scatter(df[x_col], df[y_col], color="#e76f51", edgecolor="#264653", alpha=0.8)
    plt.title(f"Scatter Plot: {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(alpha=0.2)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()
