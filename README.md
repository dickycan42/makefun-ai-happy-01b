# One Lick for You, One for Me

## The image

A warm storybook illustration: a small child in a red sweater sits on a
park bench at golden hour, laughing while sharing an ice cream with a
tiny orange kitten standing up to lick the ice cream. One small happy
moment — warm honey light, a soft green park background, no text in
the image.

## How it works

`main.py` (Python 3, standard library only) reads the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`), creates
the output folder if needed, copies `entry.png` from next to the script
into the output folder, then verifies the copy is byte-for-byte
identical by comparing the SHA-256 digests (and the file sizes) of the
source and the copy. If anything does not match, it prints an error and
exits with a non-zero code.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
