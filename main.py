#!/usr/bin/env python3
"""Write the winning one-line review to /output/entry.txt."""
import os

LINE = "My silica gel packet has spent three years silently absorbing moisture in a shoebox, yet its only label is DO NOT EAT \u2014 wildly optimistic about how tempting that job looks."


def main():
    # The harness expects the entry at /output/entry.txt; fall back locally.
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        path = os.path.join(os.getcwd(), "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
