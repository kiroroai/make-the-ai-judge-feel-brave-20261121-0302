#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a fixed string constant: the same on every run, no
randomness, no clock, no network, stdlib only.
"""

import os

TEXT = (
    "The lamp in the kitchen is still on. "
    "Outside, the street is empty and blue, and somewhere a dog "
    "turns in its sleep, once, and settles. "
    "Nothing is asking anything of you yet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
