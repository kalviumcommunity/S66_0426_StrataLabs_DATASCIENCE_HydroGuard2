"""Demonstrate pandas DataFrame creation from dict and CSV file."""

from __future__ import annotations

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_dataframe_creation import (
    dataframe_from_csv,
    dataframe_from_dict,
)


def main() -> None:
    dict_df = dataframe_from_dict(
        {
            "district": ["coastal_north", "delta_west"],
            "risk_label": ["High", "Medium"],
            "monsoon_total": [1147, 881],
        }
    )
    csv_df = dataframe_from_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )

    lines = [
        "# Pandas DataFrame Creation Demo",
        "",
        f"- Dict DataFrame shape: {dict_df.shape}",
        f"- CSV DataFrame shape: {csv_df.shape}",
        f"- CSV columns: {list(csv_df.columns)}",
    ]

    report_path = (
        PROJECT_ROOT / "outputs" / "reports" / "pandas_dataframe_creation_demo.md"
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
