"""Alien Field Notes — a one-line tourist review of Earth.

Deterministic program: writes the review line to /output/entry.txt
(no trailing newline, UTF-8) and prints it to stdout.
"""

LINE = "★★★★☆ Earth: the locals apologise to robots, argue with toasters, and say 'just five more minutes' to a star. Would orbit again."

# Gate guard: at most 200 chars, exactly one line, no edge whitespace.
assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"


OUTPUT_PATH = "/output/entry.txt"


def main():
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
