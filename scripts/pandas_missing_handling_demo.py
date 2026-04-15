"""Demonstrate drop and fill strategies for missing DataFrame values."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_missing_handling import (
    drop_missing_rows,
    fill_missing_with_value,
)


def main() -> None:
    df = pd.read_csv(
        PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    )
    df_with_missing = df.copy()
    df_with_missing.loc[0, "aug"] = None
    df_with_missing.loc[3, "monsoon_total"] = None

    dropped_df = drop_missing_rows(df_with_missing)
    filled_df = fill_missing_with_value(
        df_with_missing, "monsoon_total", float(df["monsoon_total"].mean())
    )

    lines = [
        "# Pandas Missing Handling Demo",
        "",
        f"- Original rows: {len(df_with_missing)}",
        f"- Rows after dropna: {len(dropped_df)}",
        f"- Missing in monsoon_total after fill: {int(filled_df['monsoon_total'].isna().sum())}",
    ]

    report_path = (
        PROJECT_ROOT / "outputs" / "reports" / "pandas_missing_handling_demo.md"
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
