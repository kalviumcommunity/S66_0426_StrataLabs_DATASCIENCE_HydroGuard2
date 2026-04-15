"""Demonstrate basic NumPy mathematical operations."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.numpy_math_operations import (
    add_constant,
    combined_sum,
    multiply_constant,
)


def main() -> None:
    district_a = np.array([210, 320, 295, 260], dtype=np.int64)
    district_b = np.array([155, 248, 232, 201], dtype=np.int64)

    incremented = add_constant(district_a, 10)
    scaled = multiply_constant(district_a, 1.05)
    combined = combined_sum(district_a, district_b)

    lines = [
        "# NumPy Math Operations Demo",
        "",
        f"- Add constant: {incremented.tolist()}",
        f"- Multiply constant: {[round(float(v), 2) for v in scaled]}",
        f"- Element-wise sum: {combined.tolist()}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "numpy_math_operations_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
