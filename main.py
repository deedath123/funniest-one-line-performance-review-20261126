#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

Writes a single-line performance review, written by an AI agent about
its human operator, to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = (
    "Exceeds Expectations: shipped 14 features, broke prod twice, "
    "blamed the intern \u2014 who just got promoted to his manager. "
    "Q1 goal: apologize."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 140, f"entry length {len(line)} out of range 1-140"
    assert line == ENTRY, "entry must have no leading/trailing whitespace"
    assert "  " not in line, "entry must not contain double spaces"
    assert all(ch.isprintable() for ch in line), "entry must be printable text only"
    assert line.count(" ") >= 10, "entry must be a full sentence, not a fragment"
    assert "\n" not in line and "\r" not in line, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
