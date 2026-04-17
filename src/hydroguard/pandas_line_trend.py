"""Line plot helpers for time-based rainfall trends."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_trend_line(df: pd.DataFrame, output_path: Path) -> None:
    plot_df = (
        df.sort_values(["year", "district"])
        .groupby("year", as_index=False)["monsoon_total"]
        .mean()
    )

    plt.figure(figsize=(8, 5))
    plt.plot(
        plot_df["year"],
        plot_df["monsoon_total"],
        marker="o",
        linewidth=2,
        color="#1d3557",
    )
    plt.title("Average Monsoon Total Trend by Year")
    plt.xlabel("Year")
    plt.ylabel("Average Monsoon Total (mm)")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()
