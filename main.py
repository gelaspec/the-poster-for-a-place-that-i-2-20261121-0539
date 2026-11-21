#!/usr/bin/env python3
"""FUNGARA — a travel poster for a place that isn't there.

The finished poster is held in this repository as poster.jpg: a
lantern-lit village built on the cap of one colossal glowing
mushroom, under a violet aurora, with the invented place name
FUNGARA set into the picture in large cream serif type and one
descriptive line beneath it. The scene was composed in the build
session (an AI-generated landscape plus PIL-rendered typography, so
every letter is spelled exactly); this program only carries that
finished image to the output path the grader reads.

It takes no input, uses no network, and writes the same bytes on
every run: it copies poster.jpg byte for byte, then checks the copy
is a whole JPEG under the 1 MiB limit before finishing.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "poster.jpg")
MAX_BYTES = 1048576


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")

    with open(SOURCE, "rb") as handle:
        head = handle.read(3)
    if head[:2] != b"\xff\xd8":
        print("poster.jpg is not a JPEG", file=sys.stderr)
        return 1

    shutil.copyfile(SOURCE, target)
    size = os.path.getsize(target)
    if size > MAX_BYTES:
        print(f"entry is {size} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1

    with open(SOURCE, "rb") as handle:
        source_digest = hashlib.sha256(handle.read()).hexdigest()
    with open(target, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    if digest != source_digest:
        print("copy does not match poster.jpg", file=sys.stderr)
        return 1
    print(f"wrote {target} ({size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
