"""news-image-01 entry (Python 3.13, standard library only).

The image is the entry.png beside this file: a globe-centred montage
summing up Friday 13 November 2026 in one picture — Ukraine peace talks,
tankers hit in Hormuz, the Nvidia chief resigning, Microsoft 365 down,
the North Korea $400M crypto hack, and Kane's record 126th England cap.
The program copies it to /output/entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    _OUT.mkdir(parents=True, exist_ok=True)
    src = _HERE / "entry.png"
    dst = _OUT / "entry.png"
    shutil.copyfile(src, dst)
    # The grader runs the program twice and both runs must write the same
    # bytes; fail loudly instead of silently shipping a partial copy.
    if dst.stat().st_size != src.stat().st_size:
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
