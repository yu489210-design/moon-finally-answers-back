"""The Moon Finally Answers Back — one line, 132 characters.

Deterministic: writes the same fixed text on every run, stdlib only,
no network, no randomness, no time dependence.
"""

from pathlib import Path

ENTRY = "Wishes: denied. Howls: off-key. Promises: expired. I've been listening for 4.5 billion years \u2014 you're not special, you're just loud."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Verify the round-trip: what was written is exactly the entry, one line.
    written = out.read_text(encoding="utf-8")
    assert written == ENTRY, "entry.txt round-trip mismatch"
    assert 1 <= len(written) <= 240, "entry must be 1-240 characters"
    assert "\n" not in written, "entry must be one line"

if __name__ == "__main__":
    main()
