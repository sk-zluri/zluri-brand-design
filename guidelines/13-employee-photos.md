# 13 · Employee photos — cut-outs, face matching and AI edge extension

How to turn the photos Zluri supplies of real people (new joiners, spotlights, speakers) into clean cut-outs that sit together in a series. Written from a real new-joiner production run; every rule below fixed a problem a reviewer saw.

Tools live in `tools/people/` (`pip install -r tools/people/requirements.txt`). Run them from the repo root or by full path.

---

## 1 · Inputs and copy

- **Use only the photos and details the user supplied.** Never substitute stock or an AI-generated face for a real employee.
- **Names and roles come from the user** (often the file names, e.g. `Kartik - Senior Software Engineer.jpg`). If only first names are given, **use first names only** — never invent a surname. Copy role titles exactly, including punctuation ("Senior SDET, Engineering").
- **Month in "Meet our [Month] Joiners"** is the current month unless the user says otherwise. State which month you used.
- Before work starts, list for the user: each name + role as you will print it, the month, and the logo (Zluri × Infotech lockup by default).

## 2 · Cut out the person

```bash
python tools/people/cutout.py "<photo>" cutouts/<first-name>.png             # default: birefnet-portrait
python tools/people/cutout.py "<photo>" cutouts/<first-name>.png --strip-warm-top   # lamp above the head
```

| Problem seen | Fix |
| --- | --- |
| Dark door / furniture smeared into the hair edge | Use `birefnet-portrait` (the default). `isnet-general-use` is faster but did this. |
| Ceiling lamp or light fitting kept above the head | `--strip-warm-top`. Never erase rectangular regions by hand — it clipped hair and the forehead in testing. |
| Background islands left around the person | Handled: only the largest connected subject is kept. |

**Look at every cut-out on the pink field `#E84393` at full size**, top of the head first. Hair is where problems hide.

The script reports **hard edges** — sides where the original photo cropped the person (an arm cut by the frame, the top of a head cut off). Those decide §4.

## 3 · Match the faces

A series looks wrong when one face is bigger, smaller or off-centre. **Size by the face, not by the image.**

```bash
python tools/people/fit_faces.py cutouts/*.png      # defaults = new-joiner pink field 739×545
```

It prints `style="--ph:…px; --t:…px; --l:…px"` for each `<img class="cutout">` in `templates/social/people-new-joiners.html`:

- every face ≈ **205px wide** (≈28% of the field width),
- every face **centred** on the field (x = 369),
- every face top at the **same height** (3px into the field), so hair breaks the top edge by roughly 35–75px, as in the references.

Rules:

- **The photo must reach the bottom of the field.** If `fit_faces` warns that the image stops short, either add the gap to `--t` (that face sits slightly lower; keep the shift under ~20px) or extend the photo downward (§4).
- **The head breaks the top edge; the sides and bottom are clipped.** The template does this with `overflow: visible; clip-path: inset(-40% 0 0 0)` on `.photo`. Do not put `overflow: hidden` back on — it cuts every head flat at the field edge.
- **A head the photo itself cropped at the top** cannot break the edge. Either set `--t:0` so the field's top edge hides the crop, or extend the photo upward (§4). Never let a flat-cut head poke above the field.

## 4 · Hard edges — extend with AI, never feather

When centring puts a hard (cropped) photo edge inside the field, it shows as a straight vertical line through a shoulder or arm.

- **Do not feather or fade the edge.** A fade into pink reads as a smudge; a reviewer rejected it.
- **Do not shove the person off-centre** to hide the edge unless the user chooses that.

### Ask the user first — one question, these options

> "[Name]'s photo is cropped on the [side], so centring them shows a straight edge through the [arm/shoulder/head]. How should I fix it?"
>
> 1. **Gemini** (in your signed-in browser) — extends the photo; adds a sparkle watermark that I remove.
> 2. **ChatGPT** (in your signed-in browser) — extends the photo; no visible watermark.
> 3. **No AI** — line the cropped edge up with the side of the pink field instead (the person sits slightly off-centre).

Tell them in the same message that **the photo will be uploaded to Google or OpenAI**. Use the provider they pick for every photo in the series. Approval covers this series only.

Do **not** download multi-GB local models or spend paid generation credits (Higgsfield, APIs) for this without a separate, explicit yes and a cost quote.

### Run it

1. **Pad the original photo** (not the cut-out) with white canvas on each cropped side:
   ```bash
   python tools/people/pad_for_outpaint.py "<photo>" work/<name>_pad.jpg --right 0.45     # arm cut on the right
   python tools/people/pad_for_outpaint.py "<photo>" work/<name>_pad.jpg --left 0.4      # arm cut on the left
   python tools/people/pad_for_outpaint.py "<cleaned extension>" work/<name>_pad_top.jpg --top 0.2   # head cut at the top
   ```
   Do one side per request; for a second side, pad the cleaned result of the first and send it again.
2. **Open the provider in the user's browser** with the browser-control skill (`gemini.google.com/app` or `chatgpt.com`), start a **new chat** per image, upload the padded file and send:
   > Edit this photo (outpainting). The white area on the **[right / left / top]** is empty canvas. Fill ONLY the white area by naturally continuing the photo: extend **[her right shoulder, short red polo sleeve and upper arm / his left forearm and elbow resting on the table, black t-shirt sleeve / the top of her head with her black hair pulled back]**, and continue the same **[wall / restaurant / door and wall]** background. Do not change anything in the existing photo area — keep the face, hair, expression, skin tone, clothing, accessories and lighting exactly identical. Photorealistic, seamless join, same camera and grain. Output the full image at the same aspect ratio as the input without cropping any side.

   Name the real clothing, accessories and pose in the prompt — the model keeps them consistent only when told.
3. **Download the full-resolution file** with the image's own download button (not a screenshot, not a fetch of the preview URL).
4. **Check identity.** Compare face, hair, glasses and clothing with the original side by side. If the model changed the person, discard it and tell the user — do not retry in a loop without asking.
5. **Remove the AI watermark** (§5), then **cut out the cleaned file again** (§2) and re-run `fit_faces` (§3).

## 5 · No AI marks in any deliverable

No AI-tool logo, sparkle, watermark or badge may appear in anything Zluri publishes — including on skin, clothing or background that survives the cut-out.

```bash
python tools/people/remove_ai_mark.py work/<gemini-output>.png work/<name>_clean.png
python tools/people/remove_ai_mark.py work/<name>_clean.png --check-only     # must say "no sparkle found"
```

- Gemini puts a translucent four-point star (48×48px) **144px in from the bottom-right corner** of every image. It can land on the person (it sat on a forearm in testing), so **run the remover on every Gemini output**, even when the corner looks like background.
- The remover fills the star's shape, softens it and re-adds grain. Do not cover it with a flat rectangle (leaves a seam) or try to reverse the overlay (the mark is not pure white; it leaves a ghost).
- ChatGPT adds no visible mark, but check all four corners anyway.
- After rendering, **zoom to 3× on the area where the mark was** and confirm nothing remains.

## 6 · Review loop

- Open the rendered HTML in the user's browser (browser-control skill) for review **before** exporting. Export PNGs only when the user says it is OK.
- Re-render and look after every change; reviewers spot head tops, edges and mismatched face sizes first.
- When presenting, list: names/roles as printed, month, which photos were AI-extended and by which provider, and that AI marks were removed.

## 7 · Files

Keep originals untouched. Suggested project layout:

```
<project>/
  New Joiners/            originals as supplied (never edited)
  cutouts/<name>.png      final cut-outs used by the page
  work/                   padded inputs, raw AI outputs, cleaned outputs (reference only)
  brand/                  copied tokens.css, zluri.css, z-maze-pattern.svg, logo
  <post>.html             built from templates/social/people-new-joiners.html
```
