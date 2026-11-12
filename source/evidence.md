# Zluri source evidence

How this design system was derived, what was measured, and what is interpretation.

## Sources

| # | Source | Captured | Method | Output |
| --- | --- | --- | --- | --- |
| 1 | Figma file **Zluri Marketing Brand Design System** (key `ZR8Sn0KI7ttIHfyWmPXZoI`), 4 pages: Video Storyboards · Website Animations Storyboards · Static Designs (Socials or Marketing Assets) · Pitch Deck Designs | 11 Nov 2026 | Plugin API in the open file: every top-level frame (and every frame inside sections) exported as JPG, and its node tree walked for text styles, fills, strokes, gradients, radii, effects, blend modes and images | `references/figma/` (276 images + `index.json`), `source/figma-frames.json`, `source/figma-style-census.json`, `assets/motifs/*.svg` |
| 2 | **zluri.com** — homepage and every page linked from the navbar (39 pages) | 11 Nov 2026, 1920×1023 viewport | Real browser session: full-page capture, computed-style extraction per section (headings, paragraphs, buttons, cards, layout), site-wide typography / radius / shadow / colour census, the Webflow stylesheet, page scripts; live captures of hover and cursor states | `references/website/`, `source/site-computed-styles.json` |
| 3 | **Zluri Brand Guidelines 1.01** (PDF, 31 pages, 2024) and the logo package | supplied | Text extraction + page renders; secondary palette values read from the vector fills on p.15 | `references/brand-guidelines-pdf/`, `assets/logos/` |

## What is measured vs. interpreted

**Measured (high confidence)**

- Palette hex values (PDF text + vector fills; confirmed by Figma fills and site CSS variables).
- Logo colours (from the SVG sources).
- Web type scale, weights, line-heights, button metrics, radii, borders, shadows, container width, section padding (computed styles; counts in `site-computed-styles.json`).
- Social/video type sizes, tracking, line-heights, positions and canvas sizes (Figma node data; the specs in `guidelines/04` and `05` quote these numbers).
- Interaction behaviour and timings on the site (read from the page scripts — extracts in `source/site-interaction-scripts.md` — and verified with before/after captures in `references/website/live/`).

**Interpreted (designer judgement, stated as rules)**

- Brand character, the "three-anchor" composition rule, the motif catalogue and the allowed motif pairings — patterns observed across the frames, named and generalised here.
- Format-relative type ratios (% of canvas width) — computed from the measured sizes.
- The 60/30/10 colour-distribution rule of thumb in `DESIGN.md` — an interpretation, not a measurement.
- Voice and headline patterns — derived from copy on the frames and the site; not an official messaging guide.
- The anti-slop checklist — failure modes named from experience with generic AI output, each paired with the observed Zluri alternative.
- A few token choices where the sources differ (see below).

## Where sources disagree, and what this system chose

| Topic | PDF | Figma (designers) | Site | Choice |
| --- | --- | --- | --- | --- |
| Headline weight | "Satoshi Bold or Medium" | Regular and Medium dominate; Bold is rare | Medium (500) everywhere | Regular for large display, Medium for web and sub-heads; Bold only for badges / Wrapped |
| Display tracking | not specified | −3% to −6% on Satoshi Variable | normal | −0.04em ≥60px, −0.06em ≥100px in social/video; 0 on web; token default −0.02em |
| Body line-height | "do not set leading too tightly" | 120–132% | lede 20/24 (1.2), body 16/22.8 (1.425) | `--leading-body: 1.4`; ledes may sit at 1.2 as on the site |
| Page background | Cream White | cream, white, near-black | white with cream sections | `--bg` cream; white is a surface and an alternating web section |
| Text on dark, primary | "#EBF9F6" | `#FBF9F6` | `#FBF9F6` | `#FBF9F6` (PDF value is a typo) |
| Pillar colours | — | deck: navy / cyan / teal (VIA) | Discover blue / Govern green / Secure red-brown | website mapping for new work |
| Positioning line | "Next-Gen Identity Governance & Administration" | 2026 banners: "The Identity Security Platform for Autonomous Enterprises" | hero eyebrow: "Identity security for autonomous enterprises" | current line is the 2026 one; older line kept for the tagline lockup |

## Counts

- Figma frames exported: 276 (0 failures). Text segments analysed: ~6,500. Fonts by frames: Inter Regular 116, Inter Light 85, Satoshi Medium 85+34, Satoshi Regular 84+45, Satoshi Bold 20+4.
- Website: 39 pages, 0 failures. One page (State of AI report, 20,240px) was captured by stitching viewports.
- Effects in Figma: grain (`NOISE`) on 80 nodes; large layer blurs (400–800) on 100+ nodes; `MULTIPLY` is the most used blend mode.

## Regenerating derived files

`tokens.css` is the single source of truth.

- `components.html` embeds the full `tokens.css` in its `<style>`; after editing tokens, replace that block.
- `tokens/zluri.tokens.json` is parsed from `tokens.css` (`:root` → `core` / `zluri`, `.zluri-dark` → `dark`).
- `preview/templates/*.jpg` are rendered from `templates/` with `source/scripts/render.py` (requires a browser-automation harness; paths at the top of the script need adjusting).
- `references/` is rebuilt with `export_figma.py` → `build_refs.py` → `build_specs.py` and `crawl_site.py`.

The scripts in `source/scripts/` are kept as a record of the method, not as a turnkey pipeline. They were run through a browser-automation harness attached to a signed-in Chrome session and contain three placeholders to replace before use: `<SCRATCH_DIR>` (a working folder for raw exports; `frames.json` there is the same file as `source/figma-frames.json`), `<REPO_DIR>` (this repository) and `<BRAND_DIR>` (the folder holding the guidelines PDF and logo package).

## Privacy and rights

- Reference images contain real campaign content, including names and portraits of Zluri employees and speakers and third-party logos. They are included as internal design references. Do not reuse personal names, portraits, customer quotes or statistics in new work unless supplied for that purpose.
- No stock photographs were downloaded for this repository; templates use labelled placeholders.
- Font files are not redistributed.
- Email addresses that appeared in frame text (internal posters) are redacted to `[email]` in `references/figma/specs/`, `references/figma/index.json` and `source/figma-frames.json`. Names and portraits remain visible inside the reference images themselves; keep this repository private or strip `references/figma/social-people/` and `print-and-posters/` before sharing it outside Zluri.
