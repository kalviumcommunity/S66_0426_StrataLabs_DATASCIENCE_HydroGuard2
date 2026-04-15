"""Demonstrate DataFrame inspection with head, info, and describe."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_inspection import inspection_snapshot


def main() -> None:
    csv_path = PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    df = pd.read_csv(csv_path)
    snapshot = inspection_snapshot(df)

    lines = [
        "# Pandas Inspection Demo",
        "",
        f"- Head rows count: {len(snapshot['head'])}",
        f"- Info first line: {snapshot['info'].splitlines()[0] if snapshot['info'] else ''}",
        f"- Describe keys: {list(snapshot['describe'].keys())}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "pandas_inspection_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
