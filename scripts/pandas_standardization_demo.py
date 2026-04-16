"""Demonstrate column-name and value standardization in pandas."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_standardization import (
    standardize_column_names,
    standardize_district_values,
)


def main() -> None:
    demo_df = pd.DataFrame(
        {
            "District Name": ["Coastal North ", " Delta West"],
            "Year": [2022, 2022],
            "Monsoon Total": [1147, 881],
        }
    )

    standardized_columns = standardize_column_names(demo_df)
    renamed_df = standardized_columns.rename(columns={"district_name": "district"})
    standardized_values = standardize_district_values(renamed_df)

    lines = [
        "# Pandas Standardization Demo",
        "",
        f"- Standardized columns: {list(standardized_columns.columns)}",
        f"- Standardized districts: {standardized_values['district'].tolist()}",
        f"- Dtypes: {standardized_values.dtypes.astype(str).to_dict()}",
    ]

    report_path = (
        PROJECT_ROOT / "outputs" / "reports" / "pandas_standardization_demo.md"
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
