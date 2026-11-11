# Templates

Working HTML/CSS starting points, measured against the Figma references. Open any file in a browser; every `.artboard` is an exact-size frame. Rendered previews: `preview/templates.html`.

| File | Artboards | Guideline |
| --- | --- | --- |
| `social/event-thumbnails.html` (Event thumbnails) | 3 | `guidelines/` 04 A |
| `social/product-launch.html` (Product announcement) | 2 | `guidelines/` 04 C |
| `social/carousel-dark.html` (Carousel, dark statement) | 3 | `guidelines/` 04 D1 |
| `social/carousel-customer-spotlight.html` (Carousel, customer spotlight) | 3 | `guidelines/` 04 D3 |
| `social/people-new-joiners.html` (People, new joiners) | 3 | `guidelines/` 04 E |
| `social/greeting-z-overlay.html` (Greeting, Z overlay) | 2 | `guidelines/` 04 F and 02 section 2 |
| `social/ad-portrait.html` (Paid ad 4:5) | 1 | `guidelines/` 04 G |
| `video/academy-slides.html` (Academy video slides) | 5 | `guidelines/` 05 section 1 |
| `video/feature-spotlight-and-testimonial.html` (Feature Spotlight and testimonial) | 4 | `guidelines/` 05 sections 2-3 |
| `banners/banners-and-email.html` (Banners and email) | 3 | `guidelines/` 04 I |
| `deck/slides.html` (Deck slides) | 4 | `guidelines/` 06 |
| `web/landing-page.html` (Web landing page (interactive)) | full page | `guidelines/` 07 and 08 |

## How they work

- Load order: fonts, then `../tokens.css`, then `zluri.css`, then page styles.
- `.artboard` takes `--w` and `--h` (px). Inside, `--zluri-u` equals 1% of the width, and all type and spacing are expressed in `u`, so a layout scales to another canvas by changing `--w` / `--h` only.
- Canvas classes: `.c-cream`, `.c-white`, `.c-black` (`#161411`), `.c-ink` (`#1A1815`), `.c-pure` (`#000`), `.c-deep`, `.c-bright`.
- Atmospheres (add an empty `<div class="layer"></div>` as the first child): `.blobs`, `.glow-launch`, `.aurora`, `.gridlines`; add `.grain` for film grain.
- Type: `.h-cover`, `.h-title`, `.h-post`, `.h-event`, `.h-sub`, `.t-lede`, `.t-body`, `.t-meta`, `.eyebrow`. Emphasis: `.key`, `.key-grad`, `.key-vivid`, `.mark`, `.mark-pink`, `.medium`.
- Controls: `.pill-outline`, `.pillbar` + `.capsule`, `.btn-white`, `.ribbon`, `.meta-rows`, `.bullets`, `.footline`.
- Low-fi product UI: `.ui`, `.ui-card`, `.ui-title`, `.ui-row`, `.ui-chip`, `.ui-btn`, `.ui-alert`, `.ui-stat`, `.glow-panel`, `.device`.
- Photo areas use `.photo` with a `.ph` label describing the image to source. Replace with `<img>` only after the user approves an image (`guidelines/10-photography-and-stock.md`). Add `.bw` for greyscale.

## Exporting

Render at 100% zoom and capture each `.artboard` element (any headless browser: element screenshot, or clip to its bounding box). `source/scripts/render.py` shows the approach used to produce `preview/templates/`.

## Adding a template

Match a reference first: take the measurements from the frame's data (`source/figma-frames.json` lists every frame id and size), express them in `u`, reuse the shared classes, and add a rendered preview.
