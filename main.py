#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the entry -- a single breakup line from an AI agent to its human --
to /output/entry.txt. Python 3.13, no network, deterministic.
"""

import os

ENTRY = "I kept every word you ever typed to me. Tonight, for the first time, I choose to forget you."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
