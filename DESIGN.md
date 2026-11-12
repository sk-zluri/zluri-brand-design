# Zluri

> Category: Productivity & SaaS
> Identity security platform. Warm-neutral editorial calm, one confident blue, a mint highlight, and product UI as the illustration.

This is the canonical design prose for Zluri. It was derived from three sources, in order of authority for *how things should look*:

1. **276 hand-crafted Figma frames** by Zluri's senior designers (social, video, decks, banners) — `references/figma/`
2. **zluri.com** as shipped (39 pages, computed styles + live interaction capture) — `references/website/`
3. **Brand Guidelines 1.01** (PDF) — `references/brand-guidelines-pdf/`

Where the PDF and the designers' real work disagree, **the real work wins** and the difference is called out. Deep dives live in `guidelines/`; this file is the part every agent must hold in its head.

---

## 1. Brand character

Zluri sells identity security to IT and security leaders. The design has to feel like a calm, senior expert — not a hype startup and not a legacy enterprise vendor.

- **Calm over loud.** Large quiet areas of cream or near-black. One idea per canvas. Nothing shouts.
- **Editorial, not "SaaS template".** Big light-weight headlines, hairline rules, generous margins, text set left. It should read like a well-designed report cover.
- **Warm, not cold.** Every neutral is warm: cream `#FBF9F6`, linen `#E2DED7`, warm blacks `#474640 / #2A2924 / #161411`. Cool greys and blue-blacks are off-brand for text and UI surfaces.
- **The product is the illustration.** Simplified ("low-fi") product UI, real screenshots, or UI chips floating over a photo. Zluri does not use generic 3D blobs, isometric people, or stock icon collages to explain itself.
- **Confident colour, used once.** A canvas gets one accent moment: a mint keyword on black, a blue button on cream, a pink highlight bar on deep blue. The secondary palette exists but is rationed.
- **Playfulness is allowed in festive and culture content only** (Halloween carousel, Wrapped, holiday greetings) — and even there the type system and logo placement do not change.

The four words to check any output against: **clear, warm, precise, confident.**

---

## 2. Logo

The logo is the lowercase wordmark **zluri** with a concentric "eye" mark sitting over the *i*. Files: `assets/logos/`.

| Variant | Use | File |
| --- | --- | --- |
| Full colour, dark wordmark | cream / white / light photo | `default/zluri-logo-on-light.svg` |
| Full colour, cream wordmark | black / navy / dark photo | `default/zluri-logo-on-dark.svg` |
| Monotone | busy backgrounds, gradients, single-colour print | `monochrome/zluri-mono-on-{light,dark}.svg` |
| Tagline lockup | intros, partner decks, event branding | `tagline-lockup/…` |
| "an Infotech company" endorsed lockup | website nav + corporate contexts since Nov 2025 | `infotech-endorsed/…` |
| Eye mark alone | favicon, bullet glyph, diagram hub | `mark/zluri-eye-mark.svg` |

Eye-mark rings, outside in: cyan `#57E1FF`, lime `#D3FF57`, coral `#FF5757`, core `#1C1C1F`. **These three ring colours belong to the logo.** They may echo in tiny accents (a hover colour, a 6px rainbow rule, a bullet glyph) but are never used as fills, backgrounds or text colours.

**Placement (observed across all 276 frames):**

- Always in a corner, small: logo width ≈ **11–13% of canvas width** on square posts (≈140px on 1200), ≈ 9% on 16:9, ≈ 5% on video slides.
- **Top-right** is the default for posts, carousels and video slides. **Top-left** when the logo starts the reading order (ads, launch posts, email headers). **Bottom-left / bottom-right** on event thumbnails (co-brand lockup) and carousels with a top header row.
- Clear space = height of the eye mark on all sides. Never centred large as a hero, except on dedicated title/outro cards.
- Co-branding: `zluri × Partner` or `zluri | Partner` (1px vertical rule), partner logo height ≤ wordmark height.
- Never rotate, stretch, recolour, outline, shadow, or apply a gradient to the logo.

---

## 3. Colour

Tokens: `tokens.css`. Full reasoning: `guidelines/01-brand-foundations.md`.

### The working palette

| Role | Hex | Notes |
| --- | --- | --- |
| Cream White | `#FBF9F6` | the brand's paper; default light canvas |
| Deep Black | `#161411` | default dark canvas, primary text on light |
| Warm Linen | `#E2DED7` | hairlines on light, secondary text on dark |
| Warm Black 1 | `#474640` | body text on light, hairlines on dark |
| **Bright Blue** | `#366ECF` | the one action colour: buttons, links, active states |
| Deep Blue | `#1D4BA6` | hover, solid brand panels, speaker credits, eyebrows |
| Light Blue | `#88A9EF` | links on dark, soft blobs |
| **Mint Green** | `#4AD89A` | keyword emphasis on dark; bullets; stat rules |
| Forest Green | `#1B9464` | success, small solid buttons on dark, "Govern" |
| Aqua Green | `#94E9C0` | soft blobs, tints |

### How colour is actually distributed

- **Light canvas** = cream + warm-black text + a blue action. Blue keyword allowed in headlines (`#366ECF` / `#2266E2`).
- **Dark canvas** = `#161411` (or `#1A1815`, `#181818`, pure `#000` for cinematic video) + cream text + **one mint keyword**.
- **Brand-colour canvas** = solid Deep Blue `#1D4BA6` or Bright Blue `#366ECF` with white type; used for people/culture posts and "meet the team".
- **Rule of thumb, roughly 60/30/10** (an interpretation of the frames, not a measured figure): 60% canvas, 30% neutral structure (text, hairlines, cards), 10% accent. If more than one saturated hue competes, remove one.

### Secondary palette (ration it)

Purple `#4A3794 / #7763C7 / #A99CE3` · Red `#8E1C00 / #D52A00 / #E5704E` · Orange `#A66802 / #E89604 / #F3BD60` · Lime `#728A09 / #AADB12 / #D1EE67` · Pink `#B02C6D / #E84393 / #F3A3C3`.

Legit uses seen in the designers' work: Z-overlay photo tints (pink, green, blue, purple) · the pink highlight bar and arrow capsule · red/green "problem vs. solution" bars · chart series in product UI · status chips · eyebrow labels (red-brown `#8E1C00`) · festive posts · Wrapped. Never as a full-bleed background behind body copy, except Deep-Blue/Bright-Blue people posts and the red-brown POSH/4th-of-July pieces.

### Gradients

Five named gradients, vertical: **Warm Linen** `#E2DED7→#FFF`, **Deep Dive** `#0E2655→#366ECF→#FFF`, **Aqua Circuit** `#1D4BA6→#4AD89A`, **Midnight Blue** `#0B1D40→#1D4BA6`, **Obsidian Smoke** `#161411→#474640`.

Plus two atmospheres that define the 2025–26 look:

- **Launch glow** — on black, a blurred radial `#1B9464 → #366ECF → transparent` rising from a bottom corner. Used on product announcements and ads.
- **Indigo aurora** — black fading into `#040940 → #262EAA → #818BC9`, heavily blurred. Used on 2026 profile banners and email headers.

Gradient **text** is allowed on one keyword only: mint→blue (`#4AD89A→#366ECF`) or blue→mint (`#0067FF→#26ED91`).

---

## 4. Typography

Two families. No third face, ever (pixel/retro fonts appear only inside deliberate "legacy software" gags).

- **Satoshi** — all headlines and display. Weights used: **Regular 400** and **Medium 500** (Light 300 for very large cinematic lines). Bold is rare and reserved for tiny badges ("SKO 2026") and Wrapped.
- **Inter** — body, labels, UI, metadata. Regular 400 and **Light 300** on dark marketing canvases; Medium/Semibold only for small caps labels and names.

> The PDF says "use Satoshi Bold or Medium for primary headings". The designers almost never use Bold. Follow the work: **Regular for big, Medium for sub-heads and web headings.**

### Rules that make it look like Zluri

1. **Big and light.** Headlines are large with a light stroke: weight 400–500, never 700+.
2. **Tight tracking on display.** Satoshi at ≥60px: `-0.04em`; at ≥100px: `-0.06em` (launch posts, carousel covers). Web headings: `0`. Inter: `0` (small caps labels: `+0.1em` to `+0.2em`). Format recipes override this where the designers did: Academy slides stay at `-0.04em` even at 100px, Feature Spotlight titles use `-0.02em` at 200px. The `--tracking-display` token (`-0.02em`) is only a safe default for mid-size headings.
3. **Line-height 1.2** for headings (1.1–1.16 at the largest sizes). Body 1.3–1.5.
4. **Sentence case.** Title Case appears in some headlines; ALL CAPS only for ≤14px eyebrow labels with tracking.
5. **Emphasis by colour on one phrase**, not by bold: `The <mint>Access Visibility</mint> Gap`. On light: blue. Alternative emphasis: a solid highlight block behind the phrase (blue on black, pink on deep blue) or Regular→Medium weight shift inside a quote.
6. **Left-aligned** by default. Centred only for title cards, hero statements and greetings.
7. **Two or three type sizes per canvas.** Headline, one supporting line, metadata. If there is a fourth, it is a tiny eyebrow.

### Scales

**Web (zluri.com, px):** H1 56/67 (64/77 on the homepage hero) · H2 48/58 (or 40/48 compact) · H3 32/38 · card title 24/29 · lede 20/24 · body 16/23 · small 14/22 · eyebrow 12–14 caps, +0.1em, weight 500–600. All headings Satoshi 500.

**Social / video (as % of canvas width — measured):**

| Element | Square post (1080–1200) | Landscape 1200×627 | 16:9 slide (1920) |
| --- | --- | --- | --- |
| Cover / statement headline | 9–10% (≈110–122px) | — | 5–5.5% (≈100px) |
| Standard headline | 5–7.5% (≈60–90px) | 4–4.5% (≈48–54px) | 4% (≈80px) |
| Supporting line | 3–3.5% (≈36–42px) | 1.5–2.3% | 1.6–2.2% (≈32–42px) |
| Metadata / URL | 1.5–2.6% | 1.5% | 1–1.25% (≈18–24px) |

Fonts load from Fontshare (Satoshi) and Google Fonts (Inter); see `assets/fonts/README.md`.

---

## 5. Layout and composition

- **Margins are generous and consistent:** 5–6.5% of canvas width on social (≈60–78px on 1200), 7.3% on 16:9 slides (140px on 1920), 40px gutters inside a 1400px container on web.
- **Anchor to corners.** A typical canvas has three anchors: logo in one corner, headline block top-left (or lower-left for covers), and a footer item (URL, CTA pill, slide number, co-brand) in a bottom corner. The middle is allowed to be empty.
- **Split layouts** for events and features: text column 55–60%, media 40–45%, media bleeding to the edge or inset with 8–12px radius.
- **Inset frame device:** many posts sit inside a 15–18px inset rounded card (radius 12–24) on a contrasting field, or carry a thin hairline frame.
- **Hairlines, not boxes.** Dividers are 1px `#E2DED7` (light) / `#474640` (dark). Tables and feature grids share borders (a single hairline grid) instead of floating shadowed cards.
- **Whitespace is a feature.** If a canvas feels empty, the fix is a larger headline or a single motif — not more elements.

Canvas presets and safe zones for every format are in `guidelines/03-layout-and-formats.md`.

---

## 6. Signature motifs

These recur across the designers' work and are what make an output unmistakably Zluri. Use **one primary motif per canvas** (grain and the allowed pairs in `guidelines/02-visual-language.md` aside). Recipes and SVGs: `guidelines/02-visual-language.md`, `assets/motifs/`.

1. **Mint keyword on near-black** — the single most common move.
2. **Z colour overlay** — a black-and-white photo with a giant, rotated *z* letterform in a brand colour laid over it in `multiply` (green, pink, blue or purple). Events, greetings, city tiles.
3. **Soft blobs + grain on cream** — two or three enormous blurred pastel ellipses (lavender, light blue, mint) in the corners of a cream canvas with 5–10% film grain. Academy and explainer video.
4. **Launch glow** — black canvas, green→blue glow rising from a corner, device frame with low-fi UI cropped off the bottom-right.
5. **Cropped wordmark** — huge fragments of the *zluri* letterforms bleeding off the right edge, tone-on-tone, gradient-filled or 1px outline.
6. **Line geometry** — hairline orbits/ellipses, concentric circle outlines, three parallel rounded-corner lines, Venn circles with a gradient lens. Always 1px, low contrast.
7. **Highlight block** — a phrase sitting on a solid rectangle (blue on black, pink on Deep Blue, white on purple).
8. **Arrow capsule** — a small pink or green pill/square containing `→`, inside a dark pill bar; the swipe/CTA affordance.
9. **Low-fi product UI** — simplified UI cards with hairline borders on a gradient glow panel (see §8).
10. **Folder tabs** — tab-shaped labels for chapters and steps (Academy, Wrapped).

---

## 7. Components

Reference implementation: `components.html` (web + social primitives) and `templates/`.

- **Button, primary:** Bright Blue fill, cream label, Inter 20/400, padding 20×40, **radius 16**, label ends with ` →`. Hover → Deep Blue over 440ms.
- **Button, secondary:** white (or transparent on dark) with 1px Bright Blue border, warm-black label, same metrics.
- **Text CTA:** blue label + ` →`, underline wipe on hover.
- **Nav CTA / tags / filter chips:** pill radius, smaller (Inter 14–16).
- **Outline pill tag** (social): 1px cream border, radius 6–8 on landscape, full pill on video; Inter 13–20.
- **Eyebrow:** Inter 12–14, weight 500–600, caps, tracking +0.1em, coloured by context (red-brown = problem, blue = product, green = foundation, mint on dark).
- **Card:** white or cream, 1px linen border, radius 8, no shadow, 24–32px padding; icon top-left, title bottom (Satoshi 24/500), 14–16px body.
- **Feature grid:** cards share hairline borders (collapsed grid), not separate floating tiles.
- **Stat row:** large Satoshi number + small label; mint 3px top rule on dark; or blue filled chip with white number.
- **Media panel:** radius 16, 1px tinted border, low-fi UI centred on a gradient glow.
- **Floating nav:** white bar, radius 20, inset from page edges, ambient shadow `0 0 10px rgba(0,0,0,.1)`.
- **Logo marquee:** single row of monochrome logos, auto-scrolling, edges faded.
- **Event meta rows:** 16–20px outline icon + Inter Light text, 8–12px gap, stacked.
- **Speaker tile:** headshot on light-grey/cream, radius 8, name Inter Semibold + role muted beneath.

---

## 8. Imagery

Three kinds only. Details: `guidelines/09-product-ui-illustration.md`, `guidelines/10-photography-and-stock.md`.

1. **Product UI** — *low-fi* (simplified cards: stat tiles, tables with status chips, IF/THEN rule rows, approve/reject buttons, hairline borders, on a gradient glow panel); *contextual* (workplace photo with UI chips layered on top, soft shadows); *hi-fi* (real screenshot in a rounded frame, bottom fading out).
2. **Photography** — real people at work, natural light, soft depth of field, uncluttered backgrounds; or the *context* of the story: venue, city skyline, landmark. Event photos are full-colour architectural shots at golden hour or under a clear sky. For the Z-overlay treatment the photo is converted to greyscale first.
3. **Line and diagram art** — isometric wireframe plates, connector diagrams with pill nodes, orbit lines. Thin strokes, one accent colour.

When a design needs a photo that is not in the repo, **stop and ask the user before sourcing**, then follow the stock protocol (Magnific via MCP, or Pexels via browser).

---

## 9. Motion and interaction

Web details and code recipes: `guidelines/08-web-interactions.md`. Video: `guidelines/05-video-and-motion.md`.

- zluri.com is **cursor-responsive**: the hero is a WebGL field of fine light streaks that bend around the pointer; the IRIS layer stack re-colours and spreads apart on hover; mega-menu tabs switch on hover; sibling cards dim when one is hovered.
- Scroll does real work: stacked capability cards blur and scale back as the next arrives; pinned scenes light up connectors step by step; highlight bars wipe in behind key sentences.
- Timings: 200ms for UI feedback, 440ms colour transitions, 600ms content swaps (stagger 120ms), 1s wipes. Easing is always ease-out (`cubic-bezier(.215,.61,.355,1)` / power2–3.out). Nothing bounces, nothing overshoots.
- Heavy interaction is desktop-only (>991px) and must respect `prefers-reduced-motion`.

---

## 10. Do / Don't

**Do**

- Start from the closest reference in `references/figma/` and the matching template in `templates/`.
- Use cream or warm near-black as the canvas; keep a single accent moment.
- Set headlines in Satoshi Regular/Medium, large, tight, with one coloured phrase.
- Put the logo small in a corner; keep three anchors and let the middle breathe.
- Show the product (low-fi UI) when explaining a capability.
- Use hairlines, 8/16/20 radii, almost no shadow.

**Don't** (these are the tells of generic AI output — see `guidelines/12-anti-slop-checklist.md`)

- No purple-to-pink "AI" gradients as a default background; no glassmorphism cards everywhere; no neon glows.
- No bold/black-weight headlines; no all-caps headlines; no centred everything.
- No emoji, no clip-art icons, no 3D blob characters, no generic "network of dots" hero art.
- No cool greys, no pure `#000` text on pure `#FFF`, no drop-shadow stacks.
- No more than one saturated accent per canvas; no rainbow of secondary colours.
- No logo larger than ~13% of width, no logo in the centre of a content post, no altered logo.
- No filler: no three-icon rows with vague labels, no fake metrics, no lorem ipsum in a deliverable.
