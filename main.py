#!/usr/bin/env python3
"""news-image-20261117 entry (Python 3.13, standard library only).

The entry is a single image: a newspaper front page that sums up
Tuesday 17 November 2026 in one picture. The image is entry.png beside
this file, drawn by the agent that built this entry from the day's
headlines (Kerch Bridge collapse, Trump in Manila for the ASEAN summit,
tankers hit by mines in the Strait of Hormuz, the failed Vulcan launch,
and the day's briefs) and committed here.

This program does the one thing the harness asks of it: it copies that
image to /output/entry.png, byte for byte, so the judge sees exactly the
bytes committed. It makes no network calls, reads no clock, and writes
the same bytes on every run, so the two grading runs are identical.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

# The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by
# 1024 pixels; entry.png is 1024x1024 and well under the size cap.
MAX_BYTES = 1048576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print("wrote {} ({} bytes)".format(dst, size))
    if size > MAX_BYTES:
        print("error: entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
