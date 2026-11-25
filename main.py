#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line — the excuse an AI agent gives its human for missing a
deadline — to /output/entry.txt. Deterministic, standard library only,
no network access, no input read.
"""

import os

LINE = "I'm sorry — my training data ends before your deadline, so as far as I'm concerned, it hasn't happened yet."

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
# Fail loudly here rather than shipping a line the gate would refuse.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line violates the 1-200 char gate"

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clean only the contents of the output folder, never the folder
    # itself: the grader mounts /output, and removing it fails.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
