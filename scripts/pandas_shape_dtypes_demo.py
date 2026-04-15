"""Demonstrate DataFrame shape and dtype inspection."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_shape_dtypes import dataframe_dtypes, dataframe_shape


def main() -> None:
    csv_path = PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    df = pd.read_csv(csv_path)

    shape = dataframe_shape(df)
    dtypes = dataframe_dtypes(df)

    lines = [
        "# Pandas Shape and Dtypes Demo",
        "",
        f"- Shape: {shape}",
        f"- Columns: {list(df.columns)}",
        f"- Dtypes: {dtypes}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "pandas_shape_dtypes_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
