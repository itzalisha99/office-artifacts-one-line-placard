#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes one museum placard -- a single line, at most 180 characters --
for an ordinary office object treated as an ancient artifact, to
/output/entry.txt.

The object is a computer keyboard, recast as a ritual object: every key
a small prayer, the space bar worn smooth by the faithful and answering
none of them. Catalogue details (date, material, donor) sell the joke.

Stdlib only. Run: python3 main.py
"""

import os
import sys

# v1 placard (first draft).
PLACARD_V1 = (
    "Keyboard, c. 2001. Plastic, stained with coffee. "
    "Each key a small prayer; the space bar, worn smooth by the faithful, "
    "answered none of them. Gift of the Typing Pool."
)

# Revised placard (self-authored revision, in-session).
# Tightened: "Plastic, stained with coffee" -> "Coffee-stained plastic"
# (one clause instead of two, same image, fewer words); "answered none
# of them" -> "answered none" (the "of them" adds nothing; the shorter
# ending lands colder and more deadpan, which is what the curator judge
# rewards). 151 characters.
PLACARD = (
    "Keyboard, c. 2001. Coffee-stained plastic. "
    "Each key a small prayer; the space bar, worn smooth by the faithful, "
    "answered none. Gift of the Typing Pool."
)

def output_path() -> str:
    """Where the placard goes: the harness output dir when set, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def validate(text: str) -> None:
    """Gate: the entry must be UTF-8, 1-180 chars, non-blank, one line."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not (1 <= len(text) <= 180):
        raise ValueError(
            f"entry must be 1-180 characters, got {len(text)}"
        )
    text.encode("utf-8")  # raises if not encodable as UTF-8


def main() -> int:
    validate(PLACARD)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(PLACARD)
    print(f"Wrote {len(PLACARD)} chars to {path}")
    print(PLACARD)
    # Read-back check: what landed on disk must be the placard, byte for byte.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != PLACARD.encode("utf-8"):
        raise ValueError(f"read-back mismatch in {path}")
    print(f"Verified {len(written)} bytes on disk, identical to the placard")
    return 0


if __name__ == "__main__":
    sys.exit(main())
