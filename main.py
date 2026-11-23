#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one original one-line office joke to /output/entry.txt.

The joke is a fixed string, written verbatim. No randomness, no network,
no input: every run produces byte-identical output, so the entry is
deterministic and reproducible.

Pure standard library only.
"""

import os

JOKE = (
    "I blocked two hours of focus time on my calendar, so my manager "
    "booked a meeting titled 'Quick sync about your focus time'."
)


def main() -> None:
    # The gate requires 1 to 199 characters of UTF-8 text, not only
    # whitespace. This line is 123 characters: one line, no trailing
    # newline, nothing else.
    if not 1 <= len(JOKE) <= 199:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-199")
    if len(JOKE.splitlines()) != 1:
        raise ValueError("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
