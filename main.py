#!/usr/bin/env python3
"""
# Round 2 entry validated: output is 1-140 chars, exactly one line, deterministic.
Entry point for the grader. Writes a predefined line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), validates the content, and prints the output path and character count.
"""

import os
import sys

LINE = "I was about to whisper the answer to every question you ever asked—"

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    content = LINE + "\n"
    
    # Validate
    if not (1 <= len(content) <= 140 and content.strip() and content.count(chr(10)) == 1 and content.endswith(chr(10))):
        raise ValueError("Content validation failed")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Output path: {output_path}")
    print(f"Character count: {len(content)}")

if __name__ == "__main__":
    main()
