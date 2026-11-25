#!/usr/bin/env python3
"""The Agent's Uh-Oh — variant C. Writes one word to /output/entry.txt."""

import os

WORD = "Glitching"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    # Best-effort local copy; the grader sandbox mounts the repo read-only,
    # so a failed copy must never crash the run.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(WORD)
    except OSError:
        pass


if __name__ == "__main__":
    main()
