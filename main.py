"""The Robot Apology — make.fun entry.

Writes two lines to /output/entry.txt. Line one is a robot
apologizing in a single sentence for one exact mistake — it watered
the laptop instead of the fern. Line two is what it learned and
what it will do differently, following directly from that mistake:
check for a keyboard before pouring, and water only things with soil.
"""

import os

ENTRY = (
    "I am sorry I watered your laptop instead of the fern; both sat "
    "on the desk and only one of them was thirsty.\n"
    "I have learned to check for a keyboard before pouring, and from "
    "now on I water only things with soil."
)

MAX_CHARS = 400


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    assert text.count("\n") == 1, "entry must be exactly two lines"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
