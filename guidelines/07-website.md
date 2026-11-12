# 07 · Website design system (zluri.com)

Derived from the live Webflow site — 39 pages crawled at 1920px on 11 Nov 2026 (`references/website/`), with computed styles aggregated in `source/site-computed-styles.json`. Use this to build a **new Zluri page that sits beside the existing ones**. Starter: `templates/web/landing-page.html`. Interactions: `08-web-interactions.md`.

## Page anatomy

Every marketing page follows the same spine:

1. **Announcement bar** (optional, site-wide)
2. **Floating nav**
3. **Hero** — one of four hero types
4. **Logo marquee** on Deep Black
5. **Problem section** ("THE CHALLENGE")
6. **Capabilities** — alternating feature rows or stacked cards
7. **How it works / architecture** on black
8. **Use cases** — 4-up card grid on cream
9. **Why Zluri** — comparison table
10. **Proof** — quotes / stats
11. **CTA band** on black
12. **Footer** on `#2A2924`

Sections alternate **white ↔ cream `#FBF9F6` ↔ black** to create rhythm; two sections of the same tone never touch without a hairline.

## Global chrome

### Announcement bar
Full-width, ~40px, `linear-gradient(#351E78, #57429B)`. Centred: "Zluri joins Infotech." (Satoshi 18/500 white) + chip button (`#DBD5EF` fill, `#341070` text, Satoshi 16/500, radius 6, "Read the announcement →").

### Navigation
- Floating white bar, **radius 20**, max-width ≈1400, 12px below the announcement bar, shadow `0 0 10px rgba(0,0,0,.1)`; height ≈72.
- Left: endorsed logo ("AN INFOTECH COMPANY"). Links: Inter 16/400 `#161411`, 48px apart: Products · Platform · Solutions · Why Zluri · Partners · Company · Resources. Links have 20×16 padding. Right: "Login" text link + pill CTA "Get a Demo" (`#366ECF`, white label Inter 16/400, padding 8×20, 35px tall, radius 100).
- **Mega menu:** drops as a cream `#FBF9F6` sheet beneath the bar. Column headers Inter 14/500 caps, tracking 1.4px, `#474640`. Product items are rows with a 48px linen `#E2DED7` rounded-8 icon tile + two-line label (acronym Inter 600 12.8 caps / full name Inter 16). Selected item gets a white rounded-8 card with a linen border. The Products menu has a left list (IVIP · IGA · ISPM · SMP) that switches the middle "About" panel **on hover**, plus a right "Platform" column (IRIS, Universal Identity Connector). Simple menus are 3 text columns (e.g. "BY USE CASE: / BY REGULATION: / OKTA ALTERNATIVE"). External links carry a faint ↗.
- Nav slides up out of view while a sticky in-page tab bar is active, and returns after.

### Footer
`#2A2924`. Left column: logo, address (Inter 16 cream), social icons, compliance badges. Four link columns with dim caps headers (`#474640`-ish, Inter 14/600) and Inter 16 cream links: Platform · Products · Solutions | Compliance Readiness · Resources | Why Zluri · Company. Bottom line Inter 14 `#E2DED7`: © + legal links separated by " - ".

## Type on the web

| Token | Size / line | Use |
| --- | --- | --- |
| H1 | 56 / 67.2 · **64 / 76.8 on the homepage hero** | hero (some product heroes use 40–48 inside a card) |
| H2 | 48 / 57.6 · 54 / 64.8 · 40 / 48 | section titles |
| H3 | 32 / 38.4 | feature titles |
| H4 / card title | 24 / 28.8 · 28 / 33.6 | cards |
| Lede | Inter 20 / 24 | section intro, hero sub |
| Body | Inter 16 / 22.8 | cards, lists, footer |
| Small | Inter 14 / 21.8 | legal |
| Eyebrow | Inter 12–14 / 600 caps, +0.1em | section label |

All headings: Satoshi 500, `#161411` (cream on dark), letter-spacing normal. Heading max-width ≈ 16–22 words per two lines; ledes ≈ 60–75 characters per line.

## Eyebrow colour code

| Eyebrow | Colour |
| --- | --- |
| THE CHALLENGE · CAPABILITIES · WHY ZLURI | red-brown `#8E1C00` / `#D52A00` |
| product name · USE CASES · sub-feature labels · ZLURI EVENTS | Deep Blue `#1D4BA6` |
| FOUNDATION · USE CASES (IRIS) | Forest `#1B9464` |
| HOW IT WORKS · WAYS TO CONNECT (on black) | Mint `#4AD89A` |
| DISCOVER / GOVERN / SECURE | pillar colours (blue / green / red-brown), 16px, +0.1em |

## Hero types

1. **Dark statement hero (home, UIC):** full-viewport `#161411` with a WebGL streak or light-ray field. Centred: eyebrow chip (dark translucent pill, padding 8×16, caps Inter 12/600, tracking 1.2px, cream) → H1 white 64/76.8, 2 lines → lede Inter 20/24 `#E2DED7` (max ≈700px) → primary + outline buttons (66px tall, 16px gap).
2. **Contextual-UI hero (IVIP, ISPM):** full-bleed lifestyle photo (person at a laptop, neutral office); a white rounded-16 card on the left holds eyebrow, H1 (40–48), lede (16), two buttons; 2–3 floating UI cards (stat tiles, "Risk Detected" chips) overlap the photo on the right with soft shadows.
3. **Light split hero (compliance, partners, stories):** white; text left (H1 56, lede, buttons); image or UI collage right in a radius-16 frame.
4. **Themed hero (NHI, State of AI):** a page-specific colour world — NHI: deep maroon `#2A000A` with a depth-blurred field of pink outline icons; State of AI: violet→magenta gradient with isometric keyboard keys, white highlight blocks behind key words, gradient pill "Download Report".

Then always: logo marquee on Deep Black with a centred Inter 20 line ("Trusted by Leading Organizations").

## Section patterns

| Pattern | Spec |
| --- | --- |
| **Section header** | eyebrow → H2 (max ≈900px) → lede (max ≈640px), left-aligned; 48–64px to content |
| **Problem slider** | header left + round prev/next buttons right (48px white circles, shadow); cards 3-up: square illustration tile (radius 0–8, coral→cream gradient with concentric lines, icon orbits or avatar grids) + H3 24 + 16px body |
| **Collapsed feature grid** | 3–4 columns sharing 1px linen borders; each cell: 28px outline icon top, title Satoshi 20–24 bottom, 14–16 body; empty cells stay empty |
| **Alternating feature rows** | 2 columns, text ↔ media swapping sides; text: blue eyebrow, H3 32, body 16, ✓ list (blue checks); media: low-fi UI in a radius-16 panel with hairline |
| **Sticky-tab capability stack** | peach-cream band with tabs (active = filled pillar colour, white text, radius 8); below, full-width bordered rows: left text (pillar eyebrow, H3 32, lede, ✓ list, "Get a demo" + "Learn More →"), right media panel with a pillar-tinted border and gradient glow |
| **Architecture on black** | Mint eyebrow, H2 white, interactive diagram (layer stack or pathway cards with connector lines) |
| **Persona / use-case cards** | 4-up on cream; white cards, linen border, icon top, title + 14px body bottom, min-height ≈260 |
| **Comparison table** | 3 columns (Capability · Zluri product · Traditional); the Zluri column is a raised white card (radius 12, soft shadow); rows separated by hairlines; ✓ green vs ⚠ orange markers |
| **Stat cards (dark)** | `#1F1F1F` cards, pink/Mint number Satoshi 28–56, label Satoshi 24, body Inter 16 |
| **Quote** | large Satoshi 28–32 quote, attribution Inter 16 with company in bold; or 3-up small quotes on cream |
| **Resource cards** | cream cards with caps blue tag (DATASHEET, HELP DOCS), title, body, text link "Download Now →" |
| **Filter chips** | pill chips, caps Inter 12; active = black fill, white text |
| **CTA band** | black; two columns: H2 32–40 white left, lede + primary button + text link right; or centred on white with two buttons |

## Components

**Buttons**

| Type | Rest | Hover |
| --- | --- | --- |
| Primary | `#366ECF` fill, `#F8F3F0` label, Inter 20/400, 20×40 padding, radius 16, ~64px tall, label ends " →" | `#1D4BA6`, 440ms ease-out |
| Secondary (light) | white fill, 1px `#366ECF` border, `#474640` label | `#FBF9F6` fill |
| Secondary (dark) | transparent, 1px `#366ECF` border, cream label | label `#1D4BA6`→ subtle fill |
| Text link | `#366ECF` (light) / `#88A9EF` (dark) + " →" / " ↓" | underline wipe |
| Nav CTA | pill, `#366ECF`, ~15px | darken |
| Chip | `#EDF3F8`, radius 100, 8×20, Inter 16 | — |
| Form submit | `#366ECF`, radius 4, 12×20, Inter 16 | darken |

**Cards:** radius 8, 1px `#E2DED7`, no shadow, 24–32 padding. Dark cards: `#1F1F1F`/transparent with 1px `rgba(245,245,245,.16)`.

**Forms (get-demo):** the form itself is an embedded third-party form, so its field styles could not be measured; from the capture: small Inter labels above pale blue-grey rounded inputs (~40px tall), checkbox list for solution interest, selects for country and employee range, a blue submit button. For new forms use: label Inter 14 `#474640`; input 44px tall, radius 8, 1px `#E2DED7` border on white, focus ring `--focus-ring`; submit = primary button. A Forrester recognition badge overlaps the portrait photo at right.

**Radii:** 8 (cards, images) · 16 (buttons, media) · 20 (nav) · 12 · 6 · pill.
**Borders:** 1px `#E2DED7`; on dark `rgba(245,245,245,.82)` for emphasis or `#474640` for dividers.
**Shadows:** `0 0 10px rgba(0,0,0,.1)` (nav, raised table column) · `3px 3.4px 7.9px rgba(0,0,0,.2)` (slider arrows). Nothing heavier.

## Spacing

- Container 1400 (some sections 1280/1440), gutters 40.
- Section padding: 80 default; 110–120 for hero-adjacent and feature sections; 64 compact.
- Header → content 48–64; card gap 20; grid gutters 20–32; list row gap 12–16.

## Imagery on the site

- Low-fi product UI everywhere (see `09`).
- Lifestyle photography only in heroes and the demo form; real customers' logos monochrome.
- Blog thumbnails: flat character illustrations on a pastel gradient with grain (legacy style — keep for blog only).
- Compliance badges (SOC 2, ISO 27001, GDPR, PCI, NIST) in the footer.

## Page templates on the site

| Template | Pages | Hero | Distinctive sections |
| --- | --- | --- | --- |
| Product (2026) | IVIP, ISPM, NHI, IRIS, UIC | contextual-UI / themed / dark | collapsed problem grid, alternating feature rows, architecture on black, persona cards, comparison table, quotes |
| Product (2025) | Access Management, Access Requests, Access Reviews, SoD, SMP | light split | numbered steps, ROI teaser, benefit cards |
| Solution | visibility, shadow IT, AI apps, lifecycle | light split | 3-up benefits, feature rows |
| Compliance | SOC 2, ISO 27001, HIPAA, SOX ITGC, PCI DSS | light split + "Download Brief" | "struggles we hear" quote chips on peach, dark benefit grid, 3 product columns, control cards with red-brown control labels |
| Comparison | Okta alternative | light | objection cards, swiper |
| Partners | overview, register a deal, portal | light split | dark accordion "Why Partner", model card, tiers, partner directory with chips, resources |
| Company | our story, security, careers, events, contact | statement with blue key phrase | founders grid, long-form text column, job list, event cards |
| Resources | blog, whitepapers, webinars, Eye on Identity | title + lede | dark "Editor's pick" carousel, card grids with caps category pills |
| Report | State of AI in the Workplace | violet themed | sticky "Download Report" gradient pill, highlighted pull-quotes, leaderboard grid |
| Conversion | get-demo, ROI calculator, product tours, academy | split form + photo | form, calculator sliders, tour cards |

## Building a new page — checklist

1. Pick the template row above; open its screenshot in `references/website/full-pages/`.
2. Paste `tokens.css`; start from `templates/web/landing-page.html`.
3. Write the spine (hero → marquee → problem → capabilities → architecture → use cases → why → proof → CTA).
4. One eyebrow colour per section per the code above.
5. Every capability gets a low-fi UI panel, not an icon.
6. Add interactions from `08-web-interactions.md` (at minimum: hover states, reveal-on-scroll, one cursor-responsive moment in the hero).
7. Check at 1440, 991, 767 and 390 wide.
