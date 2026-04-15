"""Demonstrate pandas Series creation from list and NumPy array."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_series_creation import series_from_array, series_from_list


def main() -> None:
    list_series = series_from_list([1085, 1147, 836], "monsoon_total_from_list")
    array_series = series_from_array(
        np.array([881, 752, 924]), "monsoon_total_from_array"
    )

    lines = [
        "# Pandas Series Creation Demo",
        "",
        f"- List Series name: {list_series.name}",
        f"- List Series values: {list_series.tolist()}",
        f"- Array Series name: {array_series.name}",
        f"- Array Series values: {array_series.tolist()}",
    ]

    report_path = (
        PROJECT_ROOT / "outputs" / "reports" / "pandas_series_creation_demo.md"
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
