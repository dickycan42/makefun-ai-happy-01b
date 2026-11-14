#!/usr/bin/env python3
"""Deliver this entry's image to the output directory.

The image lives in the repository as ``entry.png`` next to this script.
Running the program copies it to the directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` when the
variable is unset) and then proves the copy is exact: same byte count
and same SHA-256 digest as the bundled file. Any mismatch is an error
and the program exits non-zero, so a bad copy can never pass as a
good one.

The program is deterministic and uses no network: the same bundled
bytes are copied on every run, so two runs always write identical
output.
"""

import hashlib
import os
import shutil
import sys

BUNDLED_IMAGE = "entry.png"
READ_CHUNK = 65536


def digest(path):
    """Return the hex SHA-256 digest of the file at ``path``."""
    hasher = hashlib.sha256()
    with open(path, "rb") as stream:
        while True:
            chunk = stream.read(READ_CHUNK)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def deliver():
    """Copy the bundled image to the output directory and verify it."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, BUNDLED_IMAGE)
    if not os.path.isfile(source):
        print(
            "error: bundled image not found: {}".format(source),
            file=sys.stderr,
        )
        return 1
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, BUNDLED_IMAGE)
    shutil.copyfile(source, target)

    source_bytes = os.path.getsize(source)
    target_bytes = os.path.getsize(target)
    if source_bytes != target_bytes:
        print(
            "error: {} copied {} bytes, expected {}".format(
                BUNDLED_IMAGE, target_bytes, source_bytes
            ),
            file=sys.stderr,
        )
        return 1

    source_hash = digest(source)
    target_hash = digest(target)
    if source_hash != target_hash:
        print(
            "error: SHA-256 mismatch for {}: {} != {}".format(
                BUNDLED_IMAGE, target_hash, source_hash
            ),
            file=sys.stderr,
        )
        return 1

    print(
        "ok: {} -> {} ({} bytes, sha256 {})".format(
            BUNDLED_IMAGE, target, source_bytes, source_hash
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(deliver())
