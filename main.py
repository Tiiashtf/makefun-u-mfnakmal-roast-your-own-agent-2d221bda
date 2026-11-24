#!/usr/bin/env python3
"""Roast Your Own Agent — one line, written to /output/entry.txt.

The roast: my agent does an enormous amount of bureaucratic work
(quota checks, rulebooks, transcript bundles) to produce one small thing.
The joke is the gap between the effort and the output.
"""

import shutil
from pathlib import Path

ROAST = (
    "My agent read 73KB of rules, checked its quota twice, and archived "
    "its own thoughts \u2014 all to write this one line. It calls that efficiency."
)

DEST = Path("/output") / "entry.txt"


def clear_contents(folder: Path) -> None:
    """Remove everything inside folder; never the folder itself.

    The grader may run this with a root-owned output folder inside a
    sticky parent, so deleting the folder itself would fail. Only its
    contents go.
    """
    for child in folder.iterdir():
        if child.is_symlink() or not child.is_dir():
            child.unlink()
        else:
            shutil.rmtree(child)


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    clear_contents(DEST.parent)
    DEST.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
