"""Demonstrate vectorized NumPy operations replacing loops."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.numpy_vectorization import loop_anomaly, vectorized_anomaly


def main() -> None:
    totals_list = [1085, 1147, 836, 881]
    baseline = sum(totals_list) / len(totals_list)

    loop_result = loop_anomaly(totals_list, baseline)
    vector_result = vectorized_anomaly(
        np.array(totals_list, dtype=np.float64), baseline
    )

    lines = [
        "# NumPy Vectorization Demo",
        "",
        f"- Baseline: {baseline:.2f}",
        f"- Loop result: {[round(x, 2) for x in loop_result]}",
        f"- Vectorized result: {[round(float(x), 2) for x in vector_result]}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "numpy_vectorization_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
