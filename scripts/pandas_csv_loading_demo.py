"""Demonstrate loading CSV data into pandas DataFrames."""

from __future__ import annotations

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hydroguard.pandas_csv_loading import load_csv_default, load_csv_with_types


def main() -> None:
    csv_path = PROJECT_ROOT / "data" / "processed" / "rainfall_sample_processed.csv"
    default_df = load_csv_default(csv_path)
    typed_df = load_csv_with_types(csv_path)

    lines = [
        "# Pandas CSV Loading Demo",
        "",
        f"- Default shape: {default_df.shape}",
        f"- Typed shape: {typed_df.shape}",
        f"- Typed dtypes: {typed_df.dtypes.astype(str).to_dict()}",
    ]

    report_path = PROJECT_ROOT / "outputs" / "reports" / "pandas_csv_loading_demo.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
