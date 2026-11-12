# 03 · Layout and formats

Canvas presets, margins and composition rules measured from the Figma frames.

## Canvas presets

| Format | Size (px) | Used for | Canvas | Margin |
| --- | --- | --- | --- | --- |
| LinkedIn square post | **1200×1200** | announcements, people, greetings, carousel (visibility-gap style) | cream / black / deep blue | 70–78 |
| LinkedIn square (alt) | 1080×1080 | carousels (GBAR, Halloween), greetings | black | 60–64 |
| LinkedIn carousel compact | 784×784 | customer spotlight, security news, Zluri 2.0 | dark card on white / black / white | 37–58 |
| LinkedIn / event landscape | **1200×627** | event thumbnails, link previews, Luma covers (800×800 variant) | black | 29–40 |
| Feature / launch landscape | 1915×1088 (≈16:9) | product announcements, recognition banners | black / navy / linen | 98 |
| Portrait ad (4:5) | 1500×1875 | Reddit / paid social | `#1A1815` | 111 |
| Employee spotlight | 1500×1500 | culture | black→navy | 112 |
| Video slide HD | 1920×1080 | Academy templates | cream | 140 (text), 30 (inset frame) |
| Video slide 4K | 3840×2160 | intros, outros, testimonial, feature spotlight | black / blue | ×2 of HD |
| Square video | 2160×2160 | launch teaser | black | — |
| Blog thumbnail | 800×508 | blog/OG | dark | 40 |
| Email banner | 1112×348 | event email hero | black + photo | 40 |
| Email header / signature | 800×200 | newsletters, signatures | black / indigo | 38–53 |
| LinkedIn company banner | 1128×191 | profile | black + indigo aurora | text block centre-right |
| LinkedIn personal banner / wide email | 1584×396 | profile | same | keep left 27% empty (avatar) |
| G2 / review-site banner | 2500×476 | profile | black | 60 |
| Website announcement bar | full-width × 28–40 | site top | red-brown / maroon / purple gradient | centred |
| Deck slide | 1920×1080 (also 1600×900) | pitch, diagrams | `#F4F4F4` | 65 |
| Poster | A3 3508×4960, 420×595 | internal | red / white / black | 8% |

Always design at the native size; export @1x PNG/JPG (posts) or @2x for small banners.

## The three-anchor rule

Almost every static frame is built from three anchored groups and nothing else:

```
┌──────────────────────────────┐      ┌──────────────────────────────┐
│ ① headline block      ② logo │      │ ② logo        (url, optional)│
│    (top-left)                │      │                              │
│                              │      │ ① headline block             │
│                              │      │    supporting line           │
│                              │      │                              │
│ ③ footer: url / cta / number │      │              ③ media / device│
└──────────────────────────────┘      └──────────────────────────────┘
        carousel / event                      launch / ad
```

- ① **Headline block**: headline + at most one supporting line + (events) metadata rows. Max width ≈70% of the canvas so the line breaks land after 2–4 words.
- ② **Logo**: one corner.
- ③ **Footer anchor**: one of — URL, CTA pill / arrow bar, slide number, co-brand lockup, hairline + label.

If you need a fourth group, it is media (photo, device, diagram) and it takes one whole side or the bottom half.

## Vertical rhythm inside the headline block (as a ratio of headline size H)

| Gap | Size |
| --- | --- |
| eyebrow → headline | 0.25–0.35 H |
| headline → supporting line | 0.45–0.6 H |
| supporting line → metadata / bullets | 0.6–0.9 H |
| between metadata rows | 0.25 H (≈1.2× the row's own font size) |
| block → CTA | 0.9–1.2 H |

## Split layouts

| Pattern | Split | Notes |
| --- | --- | --- |
| Event thumbnail 1200×627 | text 61% / photo 39% | photo full-height, flush right, no radius; or inset with 8–12 radius on navy variants |
| Event email banner 1112×348 | 58 / 42 | same |
| SKO / networking tile | photo top 68% (inset 20px, radius 8–12) / text bottom 32% | co-brand notch top-left; square badge bottom-right |
| Launch post 1915×1088 | text 48% / device 46% | device cropped by bottom edge |
| Square launch post | text top 45% / device bottom 55% | device centred, cropped |
| Ad 4:5 | text top 40% / UI panel bottom 50% | glow panel inset 5% with radius 16 |
| Web feature row | text 5 cols / media 7 cols (or alternating) | media in radius-16 panel |
| Academy slide with presenter | content 60% / presenter video 40% (radius 12, inset 30px) | — |

## Insets and frames

- **Inset card on field:** content card inset 15–18px from the canvas edge, radius 12–24 (Customer Spotlight: `#161411` card on white; New-joiner cover: blue card on white).
- **Hairline frame:** Academy title cards use a rounded-12 rectangle with a 1px blue-grey stroke, inset 30px, with the tab navigation outside it.
- **Header row + rule:** security-news carousel has a 107px header (number left, logo right) and a full-width 1px rule beneath.

## Alignment

- Left-align everything in a block to one x. In metadata rows the **icon** sits on that shared left edge and the text follows it (on the 1200×627 thumbnail: headline and icons at x=40, row text at x=66).
- Centre alignment is reserved for: title cards, greetings, single-statement hero posts, outro CTAs.
- Numbers ("01", "02") bottom-left or top-left, Inter Regular, same colour as body text.

## Density guide

| Piece | Words on canvas |
| --- | --- |
| Carousel cover | 6–14 |
| Carousel content slide | 20–45 (title + 3 bullets) |
| Event thumbnail | 8–20 |
| Launch post | 10–20 |
| Ad | 15–30 |
| Greeting | 4–20 |
| Video slide | 6–30 |

If the copy exceeds the range, split it across slides rather than shrinking type below the scale in `DESIGN.md §4`.

## Responsive web grid

- Container 1400px max, 40px gutters (32 tablet, 20 phone).
- 12-column mental model; common splits 5/7, 6/6, 4/4/4, 3/3/3/3.
- Section padding 120 / 80 / 56 (desktop / tablet / phone); compact sections 80 / 64 / 40.
- Breakpoints: 991, 767, 479; upscale steps at 1280, 1440, 1920.
- Hero H1 56 → 40 → 32; H2 48 → 36 → 28; lede 20 → 18 → 16.
