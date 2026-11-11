# 02 · Visual language — the signature motifs

Each motif below was found repeatedly in the designers' frames. For each: what it is, when to use it, how to build it, and where to see it. Pick **one** primary motif per canvas (grain may be combined with anything).

SVG sources exported from Figma are in `assets/motifs/`.

---

## 1. Mint keyword on near-black

**What:** dark canvas, cream Satoshi headline, one phrase in Mint `#4AD89A`.
**Where:** event thumbnails, carousels, ads, G2 banner, testimonial video.
**Build:**

```html
<h1 class="z-h">Save 100+ IT Hours <span class="z-key">in Google Workspace</span></h1>
```
```css
.z-h   { font: 400 var(--zluri-display-title)/1.16 var(--font-display); letter-spacing: -0.04em; color: #fbf9f6; }
.z-key { color: #4ad89a; }
```

Rules: the keyword is the *subject* (event name, product, outcome), 1–4 words, usually at the start or end of the line. Never two different highlight colours in one headline. On light canvases the keyword is blue `#366ECF`.

Refs: `social-events/event-thumbnails-2025-26--*`, `social-carousels/carousel-gbar-*`, `ads/*`.

---

## 2. Z colour overlay

**What:** a greyscale photograph with a giant rotated **z** from the wordmark laid on top in a brand colour using `multiply` (or `plus-darker`). The z is so large you only see two or three diagonal bands crossing the photo.
**Where:** city/venue event invites, holiday greetings, city tiles, standees.
**Colours:** green `#43E8A9` / `#1B9464`, pink `#BD377A` / `#E84393`, blue `#366ECF` / `#1D4BA6`, purple `#7763C7`. One colour per piece; a series may rotate colours.
**Build:**

```html
<div class="z-overlay">
  <img src="city.jpg" alt="">
  <svg viewBox="0 0 1344 1344" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
    <!-- path from assets/motifs/z-overlay-shape-large.svg -->
    <path d="M1875.62 754.214L1836.45 1113.48L562.926 1923.66 … Z" fill="#BD377A" fill-opacity=".9"/>
  </svg>
</div>
```
```css
.z-overlay            { position: relative; overflow: hidden; border-radius: 12px; }
.z-overlay img        { width: 100%; height: 100%; object-fit: cover; filter: grayscale(1) contrast(1.05); }
.z-overlay svg        { position: absolute; inset: 0; width: 100%; height: 100%; mix-blend-mode: multiply; }
```

Rules: photo must be greyscale first (the collage variant leaves one tile in full colour for contrast). The overlay covers 40–60% of the image area. Keep faces out from under the colour where possible. Text on top of the overlay is white, heavy, short (a city name).

Refs: `social-events/z-overlay-invites--*`, `social-festive/greetings--frame-1000014698--3-57513`.

---

## 3. Soft blobs + grain on cream

**What:** cream `#FBF9F6` canvas, 2–3 huge blurred ellipses in lavender `#A99CE3`, light blue `#88A9EF`/`#366ECF`, mint `#94E9C0`/`#4AD89A`, pushed into opposite corners, with fine film grain over everything.
**Where:** Zluri Academy video templates, explainers, quote cards, infographics.
**Build:**

```css
.z-blobs { position: relative; background: #fbf9f6; overflow: hidden; }
.z-blobs::before, .z-blobs::after { content: ""; position: absolute; border-radius: 50%; filter: blur(calc(var(--zluri-u) * 20)); opacity: .9; }
.z-blobs::before { width: 55%; height: 60%; left: -22%; top: -18%; background: #a99ce3; }                     /* lavender, top-left */
.z-blobs::after  { width: 60%; height: 55%; right: -20%; bottom: -25%; background: linear-gradient(90deg,#366ecf,#4ad89a); } /* blue→mint, bottom-right */
.z-grain { position: absolute; inset: 0; background-image: var(--zluri-grain); mix-blend-mode: multiply; opacity: .10; pointer-events: none; }
```

Figma values: `LAYER_BLUR 400` on a 1920 canvas (≈21% of width); `NOISE` at 10% black. Blobs occupy the corners only — the centre 60% of the canvas stays clean cream for text.

Refs: `video/academy-templates--*`.

---

## 4. Launch glow

**What:** pure black canvas; a large radial glow (`#1B9464` centre → `#366ECF` at 27% → transparent) placed mostly off-canvas at the bottom-right (sometimes two overlapping ellipses), 5–25% grain. A tablet/device frame holding low-fi UI is cropped off the bottom-right corner.
**Where:** product announcements ("Introducing …"), paid ads, feature posts.
**Build:**

```css
.z-launch { background: #000; position: relative; overflow: hidden; }
.z-launch::before { content:""; position:absolute; width: 70%; height: 170%; right: -25%; top: 48%;
  background: radial-gradient(closest-side, #1b9464 0%, #366ecf 27%, rgba(0,0,0,0) 100%); filter: blur(40px); }
.z-device { position:absolute; right: 4%; bottom: -24%; width: 46%; aspect-ratio: 887/1158;
  border-radius: 30px; border: 1.5px solid #e2ded7; background: #fbf9f6; box-shadow: 0 6px 6px rgba(0,0,0,.22), 0 12px 12px rgba(0,0,0,.19), 0 16px 16px rgba(0,0,0,.11); }
```

Headline: Satoshi Regular, ≈5.4% of canvas width, tracking −0.06em, with the product name in the vivid gradient `#0067FF → #26ED91`. Logo top-left, `www.zluri.com` top-right in Inter Light.

Refs: `social-product-launch/product-announcements--*`, `ads/reddit-google-workspace--*`.

---

## 5. Cropped wordmark

**What:** enormous fragments of the wordmark (the *z*, *l*, *u* or the bowl of the *r*) rotated 90° or cropped by the right edge. Three renderings: tone-on-tone (10–15% lighter than the background), gradient-filled (blue→indigo, blue→green), or a 1px outline.
**Where:** recognition/award banners, backgrounds for quote or stat cards, cover slides.
**Build:** place `assets/motifs/wordmark-crop-solid.svg` (or `-outline.svg`) flush right at 100% height, width ≈17% of canvas.

Backgrounds it pairs with: Midnight navy radial (`#0B1D40` → `#1D4BA6`), deep indigo (`#14143C` → `#2A2670`), or the linen diagonal gradient with grain.

Refs: `brand-backgrounds/recognition-banners--*`.

---

## 6. Line geometry

Thin, quiet, 1px (0.6–1.5px) line art used as texture in an otherwise empty area:

| Variant | Asset | Typical placement |
| --- | --- | --- |
| Orbit ellipses (3–4 overlapping tilted ellipses) | `orbit-ellipses.svg` | bottom-right of a black carousel cover, stroke `#FBF9F6` at 30–40% |
| Concentric circle outlines (3 huge circles) | — (CSS `border-radius:50%`) | behind customer-spotlight cards, stroke `#757678` 0.6px |
| Corner arc lines (3 parallel rounded-corner lines) | `corner-arc-lines.svg` | top-right of a cream/linen banner, stroke `#222` |
| Concentric arc bands (soft tone-on-tone rings) | `concentric-arc-bands.svg` | sweeping from bottom-left on cream/navy |
| Venn circles with gradient lens | — | co-brand: two outlined circles, intersection filled mint→blue |
| Chain link ∞ | `chain-link.svg` | partnership/testimonial video; gradient stroke white→blue |
| Faint grid | — (CSS) | deep-blue feature-spotlight intro; 1px white at 6–8% |

```css
.z-grid { background-image: linear-gradient(rgba(255,255,255,.07) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.07) 1px, transparent 1px); background-size: 25% 25%; }
```

---

## 7. Highlight block

A phrase on a solid rectangle, tight to the text (padding ≈0.08em top/bottom, 0.18em sides, no radius or 2px):

| Canvas | Block | Text |
| --- | --- | --- |
| Black | Bright Blue `#366ECF` | cream |
| Deep Blue `#1D4BA6` | Pink `#E84393` | cream |
| Purple report | White | purple |
| Dark report body | Pink `#E84393` or red `#D52A00` behind a sentence | cream |

```css
.z-mark { background: #366ecf; color: #fbf9f6; padding: .06em .18em; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
```

On the web this animates: `background-size: 0% 100% → 100% 100%` over 1s `power2.out` when the line enters the viewport.

---

## 8. Arrow capsule and pill bar

The swipe/CTA affordance on social:

- **Pill bar:** full-width or hugging pill, fill `rgba(24,24,24,.53)` on black (or `rgba(255,255,255,.06)` on blue), radius 52px on a 1200 canvas, height ≈77px.
- **Capsule:** inside the bar at one end, pink `#E84393` (or green `#1B9464` square with radius 4 on white buttons), ≈113×63px, containing `→` in cream Inter Light.
- Label in Inter Light ≈36px: "Swipe to learn more", "Meet our January Joiners", "Link in the post above" (arrow turns `↑`), "Link in the comments below" (`↓`).

White-button variant (GBAR / customer spotlight): white rounded-8 button, black Inter label, green rounded-4 square with a white arrow at the right.

---

## 9. Grain

Nearly every hero canvas carries subtle noise: 5% on black launch posts, 10% on cream Academy slides and Wrapped, 25% inside glow panels. It kills banding in gradients and makes flat colour feel printed. Use the `--zluri-grain` token on an absolutely-positioned overlay with `mix-blend-mode: multiply` (light) or `soft-light`/`overlay` (dark).

---

## 10. Folder tabs

Tab-shaped labels (trapezoid top with rounded shoulders) used as chapter navigation in Academy videos and as cards in Wrapped. Active tab = Deep Blue fill with white text; inactive = text only. Outline version: pastel 1.5px strokes (green, blue, red, orange, pink) for "PART 1 … PART 5".

---

## 11. Pixel steps

Employee-spotlight posts use Bright-Blue squares (≈11.7% of canvas width each) arranged like a staircase rising toward a greyscale cut-out portrait, with a solid blue footer band carrying the name. It reads as "building blocks / growth".

---

## 12. Product diagram language

- **Pill nodes:** dark `#1F1E1B` fill, 1px `#3A3936` border, full radius, app icon + Inter 14 label.
- **Connectors:** 1px curved lines, white at 60% for inputs; outputs colour-coded (green, orange, red, purple, blue).
- **Hub:** rounded-16 tile with faint circuit pattern and the eye mark in the centre.
- **Isometric plates:** stacked wireframe layers; active layer mint, others white/grey outlines.
- **Deck diagrams (light):** `#F4F4F4` dot-grid field, white rounded cards with `0 0 0 rgba(0,0,0,.1)` hairline shadow, coloured corner tab (navy / cyan / teal), connectors in navy, teal and magenta.

---

## Combining motifs — allowed pairs

| Primary | May add |
| --- | --- |
| Mint keyword | orbit lines · arrow capsule · grain |
| Z overlay | (nothing else — it is loud) |
| Blobs + grain | folder tabs · pastel icon tiles |
| Launch glow | device frame + low-fi UI · gradient keyword |
| Cropped wordmark | highlight block |
| Highlight block | arrow capsule · z-maze pattern (tone-on-tone) |

Never combine Z overlay + launch glow, or blobs + cropped wordmark, or more than one photo treatment.
