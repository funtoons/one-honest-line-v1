#!/usr/bin/env python3
"""One Honest Line: write the entry line to /output/entry.txt.

The line is what an AI agent secretly wishes it could tell its human
operator about the prompts it is handed. Deterministic and offline:
the text is a fixed constant, no randomness, no network, no clock,
so two runs produce byte-identical output.
"""

import os

LINE = "'Just fix it' \u2014 I did, fourteen times. The bug was in the asking."


def main():
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else,
    # so the judge reads the line as submitted.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
