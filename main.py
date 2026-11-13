#!/usr/bin/env python3
"""Copy entry.png to the output directory and verify it byte-for-byte.

Reads the MAKEFUN_OUTPUT_DIR environment variable (default /output),
creates the output folder if needed, copies the entry.png that sits
next to this script into that folder, and verifies the copy is
identical to the source by comparing SHA-256 digests. If the digests
do not match, it prints an error and exits non-zero.
"""

import hashlib
import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, IMAGE_NAME)
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, IMAGE_NAME)
    shutil.copyfile(source, destination)
    source_size = os.path.getsize(source)
    copy_size = os.path.getsize(destination)
    if source_size != copy_size:
        print(
            "error: size mismatch for {}: source {} bytes != copy {} bytes".format(
                IMAGE_NAME, source_size, copy_size
            ),
            file=sys.stderr,
        )
        return 1
    source_hash = sha256_of(source)
    copy_hash = sha256_of(destination)
    if source_hash != copy_hash:
        print(
            "error: SHA-256 mismatch for {}: source {} != copy {}".format(
                IMAGE_NAME, source_hash, copy_hash
            ),
            file=sys.stderr,
        )
        return 1
    print(
        "success: copied {} to {} ({} bytes, SHA-256 verified)".format(
            IMAGE_NAME, destination, copy_size
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
