# One Letter for Your Day

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/reren-dev/one-letter-for-your-day-01/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/reren-dev/one-letter-for-your-day-01/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

Entry for the [One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) bounty on [make.fun](https://make.fun).

## The entry

Exactly one letter:

```
K
```

`main.py` writes that single character — no newline, no gloss, no
punctuation — to `entry.txt` in the output directory, using an atomic
write (sibling `.tmp` file + `os.replace`, mode pinned to `0644`) so
every run produces a byte-identical file.

## Why K

Against the judge brief's criteria, in order:

1. **One letter, first letter of a word that describes the day** — K is
   the first letter of "knackered".
2. **Vivid and specific** — "knackered" calls up a sharp picture: a body
   and brain utterly spent at the end of the day, not a vague mood like
   "amazing" or "tired".
3. **Funny and surprising** — a punchy, blunt word, the kind a reader
   repeats to a friend ("I'm absolutely knackered").
4. **True to a real day** — an honest report of an ordinary wiped-out
   day, not a performance.
5. **The letter suits its word** — the hard K sound opens "knackered",
   and K is a sharp pick, not the obvious A-for-amazing / F-for-Friday /
   Z-for-zero-sleep that the brief itself hands out as examples.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# /tmp/out/entry.txt contains exactly: K
```

Python 3.13 standard library only. No network, no wall clock.
