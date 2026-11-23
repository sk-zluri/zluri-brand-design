#!/usr/bin/env python3
"""Add white canvas on the cropped side(s) of a photo so an image model can extend it.

    python tools/people/pad_for_outpaint.py <photo> <out.jpg> --right 0.45
    python tools/people/pad_for_outpaint.py <photo> <out.jpg> --left 0.4 --top 0.2

Amounts are fractions of the photo's width (left/right) or height (top/bottom).
Pad the ORIGINAL photo, not the cut-out: the model needs the real background to continue.
"""
import argparse

from PIL import Image, ImageOps

p = argparse.ArgumentParser()
p.add_argument("src")
p.add_argument("dst")
for side in ("left", "right", "top", "bottom"):
    p.add_argument(f"--{side}", type=float, default=0)
p.add_argument("--max-side", type=int, default=1800)
a = p.parse_args()

im = ImageOps.exif_transpose(Image.open(a.src)).convert("RGB")
im.thumbnail((a.max_side, a.max_side))
L, R = int(im.width * a.left), int(im.width * a.right)
T, B = int(im.height * a.top), int(im.height * a.bottom)
c = Image.new("RGB", (im.width + L + R, im.height + T + B), "white")
c.paste(im, (L, T))
c.save(a.dst, quality=95)
print(f"{a.dst}  {c.size[0]}x{c.size[1]}")
