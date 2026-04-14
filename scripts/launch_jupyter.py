"""Launch Jupyter Notebook in the project notebooks directory."""

from __future__ import annotations

import subprocess
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    notebook_dir = project_root / "notebooks"
    notebook_dir.mkdir(parents=True, exist_ok=True)
    command = [
        "jupyter",
        "notebook",
        f"--notebook-dir={notebook_dir}",
    ]
    subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
