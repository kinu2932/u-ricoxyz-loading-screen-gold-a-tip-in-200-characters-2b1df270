#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Python standard library only; no network,
no dependencies, deterministic output.
"""

import os

TIP = (
    "The build isn't stuck — your agent is reading the error you "
    "scrolled past twice. Breathe. It's doing the part you hate, for free."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
