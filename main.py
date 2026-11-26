"""One-line roast of a smart home gadget for make.fun.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; deterministic: the same line every run.
"""

import os

ENTRY = "My robot vacuum mapped my house, my dog, and my dignity, then backed all three up to the cloud."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
