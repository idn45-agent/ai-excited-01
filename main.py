#!/usr/bin/env python3
"""ai-excited-01 entry: copy the bundled entry.png to the output directory.

The image lives next to this program in the repository. The harness runs
this file with MAKEFUN_OUTPUT_DIR set (or not); the copy must be a plain
byte-for-byte copy so two runs always produce identical output bytes.
"""

import os
import shutil
import sys

OUTPUT_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> str:
    """Return the directory the harness wants the entry written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, OUTPUT_NAME)
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, OUTPUT_NAME)
    shutil.copyfile(source, target)
    copied = os.path.getsize(target)
    expected = os.path.getsize(source)
    if copied != expected:
        print(f"copy size mismatch: wrote {copied} of {expected} bytes", file=sys.stderr)
        return 1
    print(f"wrote {target} ({copied} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
