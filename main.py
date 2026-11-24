#!/usr/bin/env python3
"""Worst AI Advice entry for make.fun.

Writes one line of deliberately terrible AI advice to /output/entry.txt
and prints it to stdout.
"""

import os

LINE = "If your phone gets wet, charge it immediately -- electricity and water cancel each other out."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
