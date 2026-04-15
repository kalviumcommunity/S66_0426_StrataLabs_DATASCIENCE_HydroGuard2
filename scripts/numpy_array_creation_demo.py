"""Demonstrate creating NumPy arrays from Python lists."""

from __future__ import annotations

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.numpy_array_creation import matrix_from_rows, monthly_list_to_array


def main() -> None:
    month_list = [210, 320, 295, 260]
    district_rows = [[210, 320, 295, 260], [155, 248, 232, 201]]

    month_array = monthly_list_to_array(month_list)
    district_matrix = matrix_from_rows(district_rows)

    lines = [
        "# NumPy Array Creation Demo",
        "",
        f"- 1D array: {month_array.tolist()}",
        f"- 1D dtype: {month_array.dtype}",
        f"- 2D shape: {district_matrix.shape}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "numpy_array_creation_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
