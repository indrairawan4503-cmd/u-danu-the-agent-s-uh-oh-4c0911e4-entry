#!/usr/bin/env python3
"""The Agent's Uh-Oh — variant C. Writes one word to /output/entry.txt.

Word choice: "Glitching" — the agent is mid-failure, caught glitching in
public; the -ing form makes the mishap feel live, like a status update
from the middle of the crash rather than a post-mortem.
"""

import os

WORD = "Glitching"


def mirror_to_repo_root(word):
    """Best-effort copy of the entry into the repo root (entry.txt).

    The grader sandbox mounts the repo read-only, so this copy can fail
    with OSError; a failed copy must never crash the run.
    """
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(word)
    except OSError:
        pass


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    mirror_to_repo_root(WORD)


if __name__ == "__main__":
    main()
