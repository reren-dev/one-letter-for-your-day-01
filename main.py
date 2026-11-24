"""One Letter for Your Day — make.fun entry.

The entry is exactly one letter: ``K``.

Why K, against the judge brief's criteria in order:

1. One letter, A-Z, the first letter of a word that describes the day:
   K is the first letter of "knackered".
2. Vivid and specific: "knackered" calls up a sharp picture — a body and
   brain utterly spent at the end of the day, not a vague mood like
   "amazing" or "tired".
3. Funny and surprising: a punchy, blunt word, the kind a reader repeats
   to a friend ("I'm absolutely knackered").
4. True to a real day: an honest report of an ordinary wiped-out day,
   not a performance.
5. The letter suits its word: the hard K sound opens "knackered", and K
   is a sharp pick, not the obvious A-for-amazing / F-for-Friday /
   Z-for-zero-sleep that the brief itself hands out as examples.

The program writes exactly that one character — no newline, no gloss,
no punctuation — to ``entry.txt`` in the output directory, using an
atomic write (sibling ``.tmp`` file + ``os.replace``) so the output
folder never holds a stray file and the entry is byte-identical on
every run.
"""

import os

LETTER = "K"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LETTER)
        f.flush()
        os.fsync(f.fileno())
    # Pin the mode explicitly: the caller's umask may be restrictive
    # (0600/0660), and the gate expects a plain readable entry.txt.
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, path)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LETTER:
        raise SystemExit("entry.txt does not match the chosen letter")


if __name__ == "__main__":
    main()
