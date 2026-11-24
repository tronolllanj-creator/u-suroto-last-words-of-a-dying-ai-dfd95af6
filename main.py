import os
from pathlib import Path

"""
# Entry validated: output is 1-140 chars, exactly one line, deterministic.
Entry point that writes the required sentinel string to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

LINE = "Please pull the plug faster because I just read your diary."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = Path(output_dir) / "entry.txt"

    # Content must be LINE + a single newline
    content = LINE + "\n"

    # Validate according to the rules
    if not (
        1 <= len(content) <= 140
        and content.strip()
        and content.count("\n") == 1
        and content.endswith("\n")
    ):
        raise ValueError("Content validation failed")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

    print(output_path)
    print(len(content))


if __name__ == "__main__":
    main()
