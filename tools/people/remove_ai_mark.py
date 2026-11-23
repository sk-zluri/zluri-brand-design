#!/usr/bin/env python3
"""Find and remove the Gemini sparkle watermark from an image Gemini returned.

    python tools/people/remove_ai_mark.py <gemini.png> <clean.png>
    python tools/people/remove_ai_mark.py <image.png> --check-only

Gemini stamps a translucent four-point star (about 48x48 px) roughly 144 px in from the
bottom-right corner. This finds it there, fills the star's shape from the surrounding pixels,
softens the fill so no seam shows, and re-adds matching grain - it disappears on skin as well
as on walls. (Simply reversing the overlay does not work: the mark is not pure white.)

Always run it, even when the sparkle sits on background the cut-out will remove: if it
overlaps the person, the cut-out keeps it. Afterwards zoom into that corner of the final render.
ChatGPT images carry no visible mark (only C2PA metadata), but check the corners anyway.
No AI-tool logo or watermark may appear in any Zluri deliverable.
"""
import argparse

import cv2
import numpy as np


def find_sparkle(im):
    h, w = im.shape[:2]
    g = im.mean(axis=2).astype(np.float32)
    hp = g - cv2.GaussianBlur(g, (0, 0), 12)
    y0, x0 = max(0, h - 260), max(0, w - 260)
    m = np.zeros((h, w), np.uint8)
    m[y0:, x0:] = (hp[y0:, x0:] > 12).astype(np.uint8) * 255
    n, _, st, _ = cv2.connectedComponentsWithStats(m)
    # Gemini places the mark's top-left corner exactly 144px from the right and bottom edges
    # (verified on 1078x992, 1118x944 and 976x1077 outputs). Only accept a star-sized blob there,
    # so skin highlights or edges nearby are never touched.
    cands = [st[i, :4] for i in range(1, n)
             if 40 <= st[i, 2] <= 56 and 40 <= st[i, 3] <= 56
             and abs(st[i, 0] - (w - 144)) <= 12 and abs(st[i, 1] - (h - 144)) <= 12]
    if not cands:
        return None, hp
    return cands[0], hp


def main():
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("dst", nargs="?")
    p.add_argument("--check-only", action="store_true")
    a = p.parse_args()

    im = cv2.imread(a.src)
    box, hp = find_sparkle(im)
    if box is None:
        print(f"{a.src}: no sparkle found")
        if a.dst and not a.check_only:
            cv2.imwrite(a.dst, im)
        return
    x, y, bw, bh = (int(v) for v in box)
    print(f"{a.src}: sparkle at x={x} y={y} ({bw}x{bh})")
    if a.check_only:
        return

    h, w = im.shape[:2]
    m = np.zeros((h, w), np.uint8)
    m[y - 4:y + bh + 4, x - 4:x + bw + 4] = (hp[y - 4:y + bh + 4, x - 4:x + bw + 4] > 6).astype(np.uint8) * 255
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    fill = np.zeros_like(m)
    cv2.drawContours(fill, [cv2.convexHull(max(cs, key=cv2.contourArea))], -1, 255, -1)
    mask = cv2.dilate(fill, np.ones((3, 3), np.uint8), iterations=2)

    out = cv2.inpaint(im, mask, 4, cv2.INPAINT_TELEA).astype(np.float32)
    soft = cv2.GaussianBlur((mask > 0).astype(np.float32), (0, 0), 4)[..., None]
    out = out * (1 - soft) + cv2.GaussianBlur(out, (0, 0), 7) * soft
    grain = im.astype(np.float32) - cv2.GaussianBlur(im.astype(np.float32), (0, 0), 2)
    ring = (cv2.dilate(mask, np.ones((15, 15), np.uint8)) > 0) & (mask == 0)
    wgt = cv2.GaussianBlur((mask > 0).astype(np.float32), (0, 0), 2)[..., None]
    noise = np.random.default_rng(1).normal(0, 1, (h, w, 1)).astype(np.float32) * grain[ring].std(0)
    out = np.clip(im * (1 - wgt) + (out + noise * wgt) * wgt, 0, 255).astype(np.uint8)
    cv2.imwrite(a.dst or a.src, out)
    print(f"cleaned -> {a.dst or a.src}")


if __name__ == "__main__":
    main()
