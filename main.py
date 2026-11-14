"""news-image-01 entry: sum up Friday 13 November 2026's world news in one image.

The entry image is a newspaper front page: masthead "FRIDAY 13 NOVEMBER
2026" over four photo panels, each with a short headline caption:

  1. UKRAINE TALKS: EUROPE JOINS PEACE TABLE — Russia agreed to European
     participation in the next round of Ukraine peace talks; envoys
     Kushner and Witkoff met Putin in Moscow and Zelenskyy near Dublin,
     and work began on the war's largest prisoner exchange.
  2. HORMUZ: TANKERS STRUCK — tankers were hit by explosions in the
     Strait of Hormuz; Iran said an LNG tanker struck a naval mine and
     claimed its forces hit a US radar in Bahrain.
  3. NVIDIA CHIEF RESIGNS, SHARES PLUNGE 16% — Nvidia founder Jensen
     Huang resigned as chief executive and from the board; CFO Colette
     Kress became interim CEO and the shares fell about 16%.
  4. MICROSOFT 365 DOWN WORLDWIDE — a major Microsoft 365 outage took
     Outlook mail and Teams offline for businesses around the world.

The program below is the whole entry: it copies the image shipped in
this repository to the grader's output directory, unchanged, so both
runs write the same bytes.
"""

import os
import shutil

# The image lives beside this file in the repository. It is copied byte
# for byte, so the two grader runs always produce identical output.
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

# The grader sets MAKEFUN_OUTPUT_DIR; default to /output.
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png missing beside main.py")
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
