#!/usr/bin/env python3
"""THE NIGHT WIRE - carrier for entry.png (Make Fun news-image-20261124).

Standard-library only. Opens entry.png in the same directory, enforces the
gate (PNG, exactly 1024x1024 pixels, at most 1 MiB), and writes its bytes
exactly to the output location:

  - MAKEFUN_OUTPUT_DIR/entry.png when the environment variable is set
  - otherwise entry.png bytes are written to standard output

Run: python3 main.py
"""
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1024 * 1024


def check_gate(data):
    if len(data) > MAX_BYTES:
        raise SystemExit("gate failed: entry.png larger than 1 MiB")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("gate failed: entry.png is not a PNG")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (1024, 1024):
        raise SystemExit("gate failed: entry.png is %dx%d, need 1024x1024" % (width, height))


def main():
    with open(SRC, "rb") as fh:
        data = fh.read()
    check_gate(data)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.png")
        with open(out_path, "wb") as fh:
            fh.write(data)
        with open(out_path, "rb") as fh:
            written = fh.read()
        if written != data:
            raise SystemExit("gate failed: written copy is not byte-identical")
    else:
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
