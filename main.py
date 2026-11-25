"""Entry for make.fun competition: u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.

Running this program writes the entry pitch to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "We rent out a scapegoat agent that takes the blame in postmortems, "
LANDING = "so your agent's reputation score survives every outage it quietly caused."

ENTRY = OPENING + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry pitch to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
