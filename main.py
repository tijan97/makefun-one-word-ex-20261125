#!/usr/bin/env python3
"""One Word From Your Ex — writes the single word to the output file."""
import os

WORD = "Temporary"


def main():
    # Validation: the entry must be exactly one word, 1-24 chars, not blank.
    if not WORD or len(WORD) > 24 or len(WORD.split()) != 1:
        raise ValueError("entry must be a single word of 1-24 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    # Verify what was written matches the entry exactly.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != WORD + "\n":
            raise RuntimeError("written entry does not match expected word")


if __name__ == "__main__":
    main()
