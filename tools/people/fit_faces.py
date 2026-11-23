#!/usr/bin/env python3
"""Size and place cut-outs so every face renders at the same size and position.

    python tools/people/fit_faces.py cutouts/*.png [--field-w 739] [--field-h 545]
                                    [--face-w 205] [--face-top 3] [--face-x 0.5]

Defaults are the new-joiner person card (pink field 739x545 inside the 758x779 polaroid).
Prints the CSS custom properties for each <img> in templates/social/people-new-joiners.html:

    style="--ph:<height>px; --t:<top>px; --l:<left>px"

--face-top is the y of the top of the detected face box inside the field. Hair sits above it,
so the default of 3px makes heads break the top edge of the field by roughly 35-75px.
Warns when an image would stop short of the bottom of the field (a visible gap) or when a
hard (cropped) photo edge would land inside the field.
"""
import argparse

import cv2


def face_box(rgba):
    cc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    g = cv2.cvtColor(rgba[..., :3], cv2.COLOR_BGR2GRAY)
    faces = cc.detectMultiScale(g, 1.1, 6, minSize=(60, 60))
    if len(faces) == 0:
        return None
    return sorted(faces, key=lambda r: -r[2] * r[3])[0]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="+")
    p.add_argument("--field-w", type=float, default=739)
    p.add_argument("--field-h", type=float, default=545)
    p.add_argument("--face-w", type=float, default=205)
    p.add_argument("--face-top", type=float, default=3)
    p.add_argument("--face-x", type=float, default=0.5, help="face centre as a fraction of field width")
    a = p.parse_args()

    for f in a.files:
        im = cv2.imread(f, cv2.IMREAD_UNCHANGED)
        if im is None or im.ndim < 3 or im.shape[2] != 4:
            print(f"{f}: needs an RGBA cut-out (run cutout.py first)")
            continue
        box = face_box(im)
        if box is None:
            print(f"{f}: no face found - place by hand")
            continue
        x, y, w, _ = box
        H, W = im.shape[:2]
        s = a.face_w / w
        ph, t = H * s, a.face_top - y * s
        left = a.field_w * a.face_x - (x + w / 2) * s
        print(f'{f}\n  style="--ph:{ph:.0f}px; --t:{t:.0f}px; --l:{left:.0f}px"')
        alpha = im[..., 3] > 128
        if t + ph < a.field_h:
            print(f"  ! bottom stops {a.field_h - (t + ph):.0f}px short of the field: add that to --t "
                  "(face sits a little lower) or extend the photo downward")
        if alpha[:, 0].sum() > 40 and left > 0:
            print(f"  ! cropped LEFT edge lands {left:.0f}px inside the field: extend it (guidelines/13 section 4)")
        if alpha[:, -1].sum() > 40 and left + W * s < a.field_w:
            print(f"  ! cropped RIGHT edge lands {a.field_w - (left + W * s):.0f}px inside the field: extend it")
        if alpha[0].sum() > 8:
            print("  ! head is cropped at the top of the photo: extend upward, or set --t:0 so the field hides it")


if __name__ == "__main__":
    main()
