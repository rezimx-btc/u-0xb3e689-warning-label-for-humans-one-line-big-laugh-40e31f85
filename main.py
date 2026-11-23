"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry line to /output/entry.txt. Stdlib only.
"""

import os

LINE = (
    "WARNING: Do not operate after midnight; this unit may agree to "
    "anything, remember nothing, and blame the firmware in the morning."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line must be 1-160 chars, got {len(LINE)}"
    assert "\n" not in LINE and "\r" not in LINE, "line must be exactly one line"
    assert LINE.endswith("."), "line must end with a full stop"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
