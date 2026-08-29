#!/usr/bin/env python3
"""Compile Markdown posts into the site's existing HTML structure."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "content" / "posts"
OUTPUT_DIR = ROOT / "posts"
TEMPLATE = ROOT / "templates" / "post.html"


def main() -> int:
    pandoc = shutil.which("pandoc")
    if pandoc is None:
        print("error: pandoc is required (https://pandoc.org/installing.html)", file=sys.stderr)
        return 1

    sources = sorted(SOURCE_DIR.glob("*.md"))
    if not sources:
        print(f"No Markdown posts found in {SOURCE_DIR.relative_to(ROOT)}/")
        return 0

    for source in sources:
        destination = OUTPUT_DIR / source.stem / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)

        command = [
            pandoc,
            str(source),
            "--from=markdown",
            "--to=html5",
            "--standalone",
            f"--template={TEMPLATE}",
            "--mathjax",
            "--syntax-highlighting=none",
            "--wrap=none",
            f"--output={destination}",
        ]
        subprocess.run(command, cwd=ROOT, check=True)
        print(f"Built {destination.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
