"""ai-excited-01 entry program.

Copies the bundled entry image (entry.png, stored next to this file)
into the output directory as entry.png. The copy is a plain byte-for-byte
transfer, so repeated runs always produce identical output.

Output directory: the MAKEFUN_OUTPUT_DIR environment variable when set,
otherwise /output. The directory is created when it does not exist yet.
"""

import os
import shutil
from pathlib import Path

ENTRY_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def source_path() -> Path:
    """Location of the bundled entry image, beside this script."""
    return Path(__file__).resolve().parent / ENTRY_NAME


def output_dir() -> Path:
    """Directory the entry image must be written to."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(configured) if configured else Path(DEFAULT_OUTPUT_DIR)


def deliver() -> Path:
    """Copy the entry image into the output directory; return its path."""
    src = source_path()
    if not src.is_file():
        raise SystemExit(f"entry image not found: {src}")
    dest = output_dir() / ENTRY_NAME
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    if dest.stat().st_size != src.stat().st_size:
        raise SystemExit(f"copy incomplete: {dest} differs from {src}")
    return dest


def main() -> None:
    deliver()


if __name__ == "__main__":
    main()
