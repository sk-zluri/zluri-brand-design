# 01 · Brand foundations

Logo, colour, type and iconography in full. `DESIGN.md` has the short version; this file has the exact values and the reasoning.

## Positioning lines (use verbatim)

| Era | Line | Where it appears |
| --- | --- | --- |
| Current (2026) | **The Identity Security Platform for Autonomous Enterprises** | LinkedIn banners, email header/signature, site hero eyebrow ("Identity security for autonomous enterprises") |
| Current site H1 | Discover, Govern and Secure Every Human and Non Human Identity | zluri.com hero |
| 2025 | The Next-Gen Identity Governance and Administration Platform | older banners, tagline lockup, email footer |
| Corporate | Zluri — an Infotech company | endorsed logo lockup, announcement bar ("Zluri joins Infotech.") |

Product vocabulary to spell exactly: **IVIP** (Identity Visibility & Intelligence), **IGA** (Identity Governance & Administration), **ISPM** (Identity Security Posture Management), **SMP** (SaaS Management Platform), **IRIS** (Identity Risk Intelligence System), **UIC** (Universal Identity Connector), **NHI** (Non-Human Identities), **SoD** (Segregation of Duties). Pillar verbs: **Discover · Govern · Secure** (older decks: Discover · Manage · Govern; framework name **VIA** = Visibility, Intelligence, Action).

---

## Logo

Files in `assets/logos/`. Construction: heavy geometric lowercase wordmark; the dot of the *i* is replaced by the eye mark (four concentric circles).

| Ring | Hex |
| --- | --- |
| outer | `#57E1FF` cyan |
| 2nd | `#D3FF57` lime |
| 3rd | `#FF5757` coral |
| core | `#1C1C1F` |

Wordmark colour: `#161411` on light, `#FBF9F6` on dark.

**Choosing a version**

- Light, flat background → `default/zluri-logo-on-light`.
- Dark, flat background → `default/zluri-logo-on-dark`.
- Photo, gradient, coloured field, or one-colour reproduction → **monotone** (white on dark/colour is the common case; the eye becomes an outlined ring).
- Website header and corporate/legal contexts → **Infotech endorsed** lockup.
- Introductory material where the audience may not know Zluri → **tagline lockup**.

**Sizing (measured on the Figma frames)**

| Canvas | Logo width | Offset from edges |
| --- | --- | --- |
| 1200×1200 post | 139–146px (≈12%) | 65–78px |
| 1080×1080 | ≈125px | 60–64px |
| 784×784 carousel | 79–90px | 37–58px |
| 1500×1875 ad | 196px (13%) | 111px |
| 1200×627 | 95–110px (≈8.5%) | 29–40px |
| 1920×1080 slide | 93px (4.8%) corner · 139px (7.2%) on title cards | 50–66px |
| 800×200 email | ≈95px | 38–53px |

**Clear space:** the eye mark's height on every side.

**Co-branding:** `zluri × PARTNER` (thin ×) for joint content; `zluri | PARTNER` (1px vertical rule, ~32px tall on 1200×627) for event sponsorship rows. Partner logo is monochrome-white on dark where possible and never taller than the wordmark. On SKO-style tiles the lockup sits in a notch cut into the top-left of the photo.

**Never:** rotate · stretch · gradient-fill · stroke · drop-shadow · recolour (e.g. red wordmark) · place on a busy area without the monotone version · separate the eye from the wordmark inside a lockup.

---

## Colour

### Primary

| Name | Hex | RGB | CMYK |
| --- | --- | --- | --- |
| Deep Blue | `#1D4BA6` | 29, 75, 166 | 83, 55, 0, 35 |
| Bright Blue | `#366ECF` | 54, 110, 207 | 74, 47, 0, 19 |
| Light Blue | `#88A9EF` | 136, 169, 239 | 43, 29, 0, 6 |
| Forest Green | `#1B9464` | 27, 148, 100 | 82, 0, 32, 42 |
| Mint Green | `#4AD89A` | 74, 216, 154 | 66, 0, 29, 15 |
| Aqua Green | `#94E9C0` | 148, 233, 192 | 36, 0, 18, 9 |
| Cream White | `#FBF9F6` | 251, 249, 246 | 0, 1, 2, 2 |
| Deep Black | `#161411` | 22, 20, 17 | 0, 9, 23, 91 |

### Neutral ramps (from the designers' palette board)

- **Neutral warm:** `#FBF9F6` · `#FFF8F2` · `#E2DED7`
- **Dark warm:** `#474640` · `#2A2924` · `#161411`
- **Dark cool:** `#434547` · `#1F2226` · `#0E1114` (for product-UI mock chrome and cinematic video only)

### Text colours

| Context | Primary | Secondary | Tertiary |
| --- | --- | --- | --- |
| On light | `#161411` | `#474640` | `#717171` |
| On dark | `#FBF9F6` | `#E2DED7` | `#A8A8A8` |

> The PDF prints "Text Primary (light) #EBF9F6" — that is a typo for `#FBF9F6`.

### Secondary (three steps each)

| Family | Dark | Base | Light |
| --- | --- | --- | --- |
| Purple | `#4A3794` | `#7763C7` | `#A99CE3` |
| Red | `#8E1C00` | `#D52A00` | `#E5704E` |
| Orange | `#A66802` | `#E89604` | `#F3BD60` |
| Lime | `#728A09` | `#AADB12` | `#D1EE67` |
| Pink | `#B02C6D` | `#E84393` | `#F3A3C3` |

### Where each colour has been used by the designers

| Colour | Observed jobs |
| --- | --- |
| Mint `#4AD89A` | keyword in headline on dark (most frequent), bullets, stat top-rule, "active" line art, chat bubble for the good actor |
| Bright Blue `#366ECF` | web CTAs, highlight block on black, pixel squares on employee posts, people-post canvas, SKO badge |
| Deep Blue `#1D4BA6` | new-joiner canvas, speaker credit text, eyebrow on cream, active tab, hover |
| Forest `#1B9464` | small solid buttons on dark ("Book a Meeting"), arrow squares, green "solution" bars, Govern pillar |
| Pink `#E84393` | highlight bar and arrow capsule on blue/black, photo backdrop on joiner cards, Z overlay |
| Red `#D52A00` / `#8E1C00` | "challenge" bars and ☒ icons, problem eyebrows, announcement bar, Secure pillar, 4th of July |
| Orange `#E89604` | chart series, status chips, Wrapped tiles |
| Purple `#7763C7` | ZluriVerse sub-brand headline, Z overlay, State of AI report (with pink `#E84393` accents) |
| Lime | chart series, category tags in decks, POSH poster hands |

### Gradients

```css
/* Named (vertical) */
Warm Linen     : linear-gradient(180deg,#E2DED7,#FFFFFF)
Deep Dive      : linear-gradient(180deg,#0E2655,#366ECF 35%,#FFFFFF)
Aqua Circuit   : linear-gradient(180deg,#1D4BA6,#4AD89A)
Midnight Blue  : linear-gradient(180deg,#0B1D40,#1D4BA6)
Obsidian Smoke : linear-gradient(180deg,#161411,#474640)

/* Observed atmospheres */
Launch glow    : radial-gradient(#1B9464 0%, #366ECF 27%, transparent 100%)   /* big ellipse off bottom-right, on #000 */
Indigo aurora  : linear-gradient(#040940, #262EAA 50%, #818BC9) + ~240px blur  /* on #000, 2026 banners */
Employee fade  : linear-gradient(180deg,#161411,#0E1928 24%,#0F2241 44%,#10335F 70%,#144378 85%,#1256A6)
Linen diagonal : linear-gradient(135deg,#C9C4BC,#F0EEEA) + grain               /* recognition banners */
Announcement   : linear-gradient(180deg,#351E78,#57429B)                        /* site top bar */
Rainbow rule   : 6px bar teal → blue → white → pink                             /* G2 banner footer only */
```

Rules: a gradient is a *background atmosphere or a media panel*, never a button fill, never behind long body text unless the text sits on a solid card. One gradient per canvas.

---

## Typography

### Roles

| Role | Face | Weight | Tracking | Leading |
| --- | --- | --- | --- | --- |
| Display (≥100px) | Satoshi | 400 (300 for cinematic) | −0.06em | 1.1–1.16 |
| Headline (60–99px) | Satoshi | 400 / 500 | −0.04em | 1.2 |
| Sub-head (24–59px) | Satoshi | 500 | −0.02em to 0 | 1.2 |
| Web headings | Satoshi | 500 | 0 | 1.2 |
| Lede / supporting | Inter | 300 on dark, 400 on light | 0 | 1.2–1.3 |
| Body | Inter | 400 | 0 | 1.4–1.5 |
| Label / name | Inter | 500–600 | 0 | 1.2 |
| Eyebrow | Inter | 500–600, caps | +0.1em (up to +0.2em at ≤12px) | 1 |
| Micro "yearly recap" style tag | Inter Light, lowercase | +0.2em | 1.1 |

### Type misuse (from the PDF, all still valid)

- No low-contrast text. Minimum 4.5:1 for body.
- No uppercase paragraphs or headlines.
- No bold paragraphs.
- No tight body leading.
- No justified text.
- No serif, script or display faces.

### Exceptions the designers actually made

- **Montserrat Black caps** for city names laid over Z-overlay city tiles ("NEW YORK").
- **Pixel/Win95 fonts** inside retro "legacy tooling" jokes in Academy videos.
- **Sora** appears only inside product-UI mockups because the real product uses it. Do not use it for marketing text.
- **Satoshi Bold** for Wrapped headlines and tiny square badges.

---

## Iconography

- **Microsoft Fluent System Icons**, Regular (outline) style, ~1.5px stroke at 24px. Filled variants only inside small solid tiles (nav mega-menu, mint squares).
- Icon colour = text colour of its context. On cards the icon sits top-left at 24–28px with the title at the bottom of the card.
- **Icon tiles:** 48–64px rounded square (radius 6–8) — pastel gradient (Academy), mint solid `#4AD89A` (dark carousels), linen `#E2DED7` (web nav).
- Event rows use three recurring glyphs: calendar, clock, map-pin.
- Arrows are typographic: `→` for forward, `↓` for download / "below", `↑` for "above". They live inside button labels and arrow capsules.
- No emoji, no multicolour icon packs, no 3D icons (the single exception: glossy 3D objects as *hero art* in a 2026 banner — shield, padlock — never as UI icons).

Free source: <https://github.com/microsoft/fluentui-system-icons> (MIT).
