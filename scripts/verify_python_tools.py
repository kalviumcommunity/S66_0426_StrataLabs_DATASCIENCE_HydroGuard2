"""Verify Python, Conda, and Jupyter availability for HydroGuard."""

from __future__ import annotations

import platform
import shutil
import subprocess
import sys


def run_command(command: list[str]) -> tuple[bool, str]:
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as error:
        return False, str(error)
    return True, (result.stdout or result.stderr).strip()


def binary_exists(name: str) -> bool:
    return shutil.which(name) is not None


def main() -> None:
    print("HydroGuard environment verification")
    print(f"Platform: {platform.platform()}")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version.split()[0]}")

    checks = {
        "conda": ["conda", "--version"],
        "jupyter": ["jupyter", "--version"],
    }

    for label, command in checks.items():
        if not binary_exists(label):
            print(f"[FAIL] {label}: command not found")
            continue
        ok, output = run_command(command)
        status = "OK" if ok else "FAIL"
        print(f"[{status}] {label}: {output}")


if __name__ == "__main__":
    main()
