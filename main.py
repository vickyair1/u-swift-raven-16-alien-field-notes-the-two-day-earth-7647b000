#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text - an alien tourist's review of
planet Earth - to /output/entry.txt.
"""

import os

LINE = "★★★☆☆ Lovely blue planet, great sunsets — but the locals queue for bean water and worship glowing rectangles. Would abduct again."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
