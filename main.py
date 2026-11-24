#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text - an alien tourist's review of
planet Earth - to /output/entry.txt.

The review is a single line with no trailing newline: a three-star
rating, one sentence of praise for the sunsets, one complaint about
the locals, and a promise to return.
"""

import argparse
import os
import sys

# The review line. Keep byte-identical: the entry is judged on this
# exact text (129 characters, 141 bytes UTF-8).
LINE = "★★★☆☆ Lovely blue planet, great sunsets — but the locals queue for bean water and worship glowing rectangles. Would abduct again."

OUTPUT_PATH = "/output/entry.txt"
ENCODING = "utf-8"


def validate_entry(line):
    """Check the review line is non-empty plain text before writing."""
    if not line:
        raise ValueError("review line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("review line must be a single line")
    return line


def write_entry(line, path=OUTPUT_PATH):
    """Write the validated review line to path, no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding=ENCODING) as f:
        f.write(line)


def main(argv=None):
    """Validate the review line, write it, and optionally print it."""
    parser = argparse.ArgumentParser(
        description="Write an alien tourist's one-line review of Earth."
    )
    parser.add_argument(
        "--print", action="store_true",
        help="also print the review line to stdout",
    )
    args = parser.parse_args(argv)
    line = validate_entry(LINE)
    write_entry(line)
    if args.print:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
