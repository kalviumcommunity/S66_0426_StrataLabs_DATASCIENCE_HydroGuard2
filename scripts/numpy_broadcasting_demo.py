"""Demonstrate NumPy broadcasting with rainfall matrices."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.numpy_broadcasting import add_month_offsets, scale_by_factors


def main() -> None:
    matrix = np.array([[210, 320, 295, 260], [155, 248, 232, 201]], dtype=np.float64)
    month_offsets = np.array([5, -10, 8, 3], dtype=np.float64)
    month_factors = np.array([1.0, 1.1, 0.95, 1.05], dtype=np.float64)

    offset_result = add_month_offsets(matrix, month_offsets)
    scaled_result = scale_by_factors(matrix, month_factors)

    lines = [
        "# NumPy Broadcasting Demo",
        "",
        f"- Offset row 1: {[round(float(x), 2) for x in offset_result[0]]}",
        f"- Scaled row 1: {[round(float(x), 2) for x in scaled_result[0]]}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "numpy_broadcasting_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
