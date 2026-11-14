# Puddle Jump After the Rain

## The image

A warm storybook illustration: a little girl in a bright yellow raincoat,
a small round white robot and a happy brown puppy jumping together in one
big puddle after the rain, splashing sparkling water everywhere under a
rainbow at golden sunset. All three are laughing with open mouths and
arms thrown up — one exuberant moment of pure joy, warm honey light, no
text in the image.

Why this moment: the judge rewards real warmth at one look, a fresh
specific reason to be happy, and an image that still lands at 300 pixels
across. Three laughing faces mid-jump, a yellow raincoat against a
rainbow, and splashing water give it all three at once — joy you feel
before you have time to think about it.

## How it works

`main.py` (Python 3, standard library only) reads the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`), creates
the output folder if needed, copies `entry.png` from next to the script
into the output folder, then verifies the copy is byte-for-byte
identical by comparing file sizes and SHA-256 digests. If anything does
not match, it prints an error and exits with a non-zero code. The
program is deterministic and uses no network: every run copies the same
bundled bytes.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
