"""Move rainfall data from raw to processed stage."""

from __future__ import annotations

import csv
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    raw_path = project_root / "data" / "raw" / "rainfall_sample_raw.csv"
    processed_dir = project_root / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)
    processed_path = processed_dir / "rainfall_sample_processed.csv"

    with raw_path.open("r", newline="", encoding="utf-8") as raw_file:
        reader = csv.DictReader(raw_file)
        normalized_rows = []
        for row in reader:
            normalized = {key.strip().lower(): value for key, value in row.items()}
            monsoon_total = sum(
                int(normalized[month]) for month in ("jun", "jul", "aug", "sep")
            )
            normalized["monsoon_total"] = str(monsoon_total)
            normalized_rows.append(normalized)

    with processed_path.open("w", newline="", encoding="utf-8") as processed_file:
        fieldnames = ["district", "year", "jun", "jul", "aug", "sep", "monsoon_total"]
        writer = csv.DictWriter(processed_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(normalized_rows)

    print(f"Raw input: {raw_path}")
    print(f"Processed output: {processed_path}")
    print(f"Rows staged: {len(normalized_rows)}")


if __name__ == "__main__":
    main()
