#!/usr/bin/env python3
"""Dad Joke Showdown — make.fun entry.

Writes the dad joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
if set). Stdlib only, no network.
"""

import os

ENTRY = "My daughter asked why the moon keeps changing shape. I said, 'It's just going through phases, like you.'"


def main() -> None:
    # Guard: entry must be a single line, 1-200 chars, letters/punctuation only.
    assert 1 <= len(ENTRY) <= 200, "entry length out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert all(c.isalpha() or c.isspace() or c in ".,'\"!?-;:()/" for c in ENTRY), (
        "entry contains unexpected characters"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verify: exact bytes, no trailing newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY, "read-back mismatch"


if __name__ == "__main__":
    main()
