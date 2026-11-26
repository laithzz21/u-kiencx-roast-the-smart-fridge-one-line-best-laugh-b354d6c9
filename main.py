#!/usr/bin/env python3
"""make.fun entry: Roast the Smart Fridge — one line, best laugh.

Validates the entry (at most 160 characters, exactly one line) and
prints it to stdout. Any file output goes only to $MAKEFUN_OUTPUT_DIR,
else $MAKEFUN_OUTPUT, else a per-entry /tmp path — never into the repo.
"""

import os
import sys

ENTRY = "My smart fridge judges my 2 a.m. snacks out loud, then texts my scale \u2014 even my leftovers have a group chat now."

MAX_CHARS = 160


def validate(entry: str) -> None:
    """Check the entry meets the competition rules."""
    if not entry:
        raise ValueError("entry must not be empty")
    if entry != entry.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
        )
    # The roast must actually name the gadget it is roasting.
    if "fridge" not in entry.lower():
        raise ValueError("entry must roast the smart fridge")


def output_path() -> str:
    """Resolve the writable output path, preferring make.fun env vars.

    MAKEFUN_OUTPUT_DIR is a directory; MAKEFUN_OUTPUT may be either a
    directory or a full file path, so a trailing .txt value is used as-is.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    out = os.environ.get("MAKEFUN_OUTPUT")
    if out:
        if out.endswith(".txt"):
            return out
        return os.path.join(out, "entry.txt")
    return "/tmp/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/entry.txt"


def main() -> int:
    validate(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)}/{MAX_CHARS} characters)", file=sys.stderr)
    path = output_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        fallback = "/tmp/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/entry.txt"
        try:
            os.makedirs(os.path.dirname(fallback), exist_ok=True)
            with open(fallback, "w", encoding="utf-8") as f:
                f.write(ENTRY + "\n")
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
