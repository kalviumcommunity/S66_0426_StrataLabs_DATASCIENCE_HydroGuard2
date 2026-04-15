"""Demonstrate shape, dimensions, and index positions in NumPy arrays."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.numpy_shape_index import array_metadata, sample_index_values


def main() -> None:
    rainfall_matrix = np.array(
        [[210, 320, 295, 260], [155, 248, 232, 201]], dtype=np.int64
    )
    metadata = array_metadata(rainfall_matrix)
    index_values = sample_index_values(rainfall_matrix)

    lines = [
        "# NumPy Shape and Index Demo",
        "",
        f"- Shape: {metadata['shape']}",
        f"- Dimensions: {metadata['ndim']}",
        f"- Total elements: {metadata['size']}",
        f"- Sample indexes: {index_values}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "numpy_shape_index_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
