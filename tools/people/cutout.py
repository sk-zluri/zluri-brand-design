#!/usr/bin/env python3
"""Cut a supplied employee photo out of its background.

    python tools/people/cutout.py <photo> <out.png> [--model birefnet-portrait] [--strip-warm-top]

Default model is `birefnet-portrait` (~1 GB, downloaded on first run). It keeps hair edges
clean and does not pick up door frames or furniture beside the head. `isnet-general-use` is
smaller and faster but smeared a dark door into one person's hair in testing.

--strip-warm-top removes warm/golden blobs (ceiling lamps, light fittings) that sit above the
hairline in the top 20% of the frame. Use it when a cut-out keeps a lamp above the head.

Only the largest connected subject is kept, so stray background islands disappear.
The script reports any hard (cropped) photo edge — see guidelines/13-employee-photos.md §4.
"""
import argparse

import numpy as np
from PIL import Image, ImageOps
from rembg import new_session, remove
from scipy import ndimage


def strip_warm_top(a: np.ndarray) -> np.ndarray:
    h, w = a.shape[:2]
    top = int(h * 0.2)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    warm = (r - b > 45) & (r > 90)
    band = np.zeros((h, w), bool)
    band[:top] = True
    dark = (0.299 * r + 0.587 * g + 0.114 * b < 60) & (a[..., 3] > 150)
    protect = np.zeros((h, w), bool)  # everything 25px below the first dark (hair) pixel
    for x in range(w):
        ys = np.where(dark[:top, x])[0]
        if len(ys):
            protect[ys[0] + 25:, x] = True
    lamp = ndimage.binary_dilation(warm & band & ~protect, iterations=3) & band & ~protect
    a[..., 3][lamp] = 0
    return a


def keep_largest(a: np.ndarray) -> np.ndarray:
    lab, n = ndimage.label(a[..., 3] > 20)
    if n > 1:
        sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
        a[..., 3][lab != 1 + int(np.argmax(sizes))] = 0
    return a


def main():
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("dst")
    p.add_argument("--model", default="birefnet-portrait")
    p.add_argument("--max-side", type=int, default=1800)
    p.add_argument("--strip-warm-top", action="store_true")
    args = p.parse_args()

    im = ImageOps.exif_transpose(Image.open(args.src)).convert("RGB")
    im.thumbnail((args.max_side, args.max_side))
    out = remove(im, session=new_session(args.model))
    a = np.array(out).astype(int)
    if args.strip_warm_top:
        a = strip_warm_top(a)
    a = keep_largest(a)
    out = Image.fromarray(a.astype("uint8"), "RGBA")
    out = out.crop(out.getbbox())
    out.save(args.dst)

    al = np.array(out)[..., 3] > 128
    hard = [s for s, edge in (("left", al[:, 0]), ("right", al[:, -1]), ("top", al[0])) if edge.sum() > (8 if s == "top" else 40)]
    print(f"{args.dst}  {out.size[0]}x{out.size[1]}")
    if hard:
        print("HARD EDGES (photo was cropped here): " + ", ".join(hard)
              + "  -> read guidelines/13-employee-photos.md section 4 before centring this person")


if __name__ == "__main__":
    main()
