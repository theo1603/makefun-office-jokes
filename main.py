#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one original one-line joke about office life to /output/entry.txt.
The joke is a single line under 200 characters.
"""

import os

JOKE = (
    "We killed the weekly status meeting and replaced it with a dashboard, "
    "so now we meet weekly to discuss why nobody reads the dashboard."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"joke must be 1-199 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
