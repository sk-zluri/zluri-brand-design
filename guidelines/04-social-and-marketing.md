# 04 · Social and marketing assets

Every recurring asset type in the Figma library, as a buildable spec. Sizes are in px on the stated canvas; scale proportionally for other sizes. Reference images: `references/figma/<category>/` (look up exact files in `references/figma/index.json`). Exact measurements for any frame: `references/figma/specs/<node-id>.json`. Matching HTML: `templates/social/` and `templates/banners/`.

---

## A. Event thumbnail — the current standard (2025–26)

**Canvas** 1200×627, `#161411`. **Refs** `social-events/event-thumbnails-2025-26--*`.

| Element | Spec |
| --- | --- |
| Title | Satoshi Medium 54/1.2, cream; event or city name in Mint. x=40, y=49, max-width 650 |
| Meta rows | Inter Light 18.4/1.2, `#E2DED7`; outline icons 16px (calendar, clock, pin); first row y≈211, 33px pitch; text x=66 |
| Photo | x=732→1200, full height, colour, no radius |
| Co-brand | bottom-left y≈565: logo 95px wide · 1px rule 32px tall · partner logo ≤24px tall |
| CTA | bottom-right of text column: outline pill, 1.3px cream border, radius 10, height 50, Inter Medium 19.6 ("Join Us in Santiago!") |

Variants:

- **Gradient field** (no photo): black with the event glow (`--zluri-glow-event`: violet → blue → green rising from the bottom-right) and grain; "SPONSORED BY" caps label + partner logo row along the bottom; CTA pill top-right.
- **Webinar / unsponsored online event:** same gradient field; small caps eyebrow ("Webinar") above the title; date and time rows; CTA pill top-right ("Save your seat →"); `www.zluri.com` bottom-left and an optional speaker line bottom-right (or speaker tiles when headshots are supplied). Template artboard D.
- **Square 1200×1200:** same stack, title 2 lines, sponsor row at the bottom.
- **SKO / networking tile:** photo on top (inset 21px, radius 8, height 428), co-brand in a black notch top-left (`zluri × PARTNER`), title Satoshi Medium 47 below with Mint keyword, meta rows inline, Bright-Blue square badge 116×116 radius 8 bottom-right ("SKO / 2026" Satoshi Bold 50 / 20).
- **Meet the team:** title + meta at top, then a row of 4–6 speaker tiles (cream cards radius 8, headshot, name Inter Semibold, role muted). On Bright Blue `#366ECF` or black.
- **2025 conference post** ("GRC Conference 2025"): title Satoshi Regular 56, event name Mint + year cream; logo bottom-left; pill "Visit us at booth #117".

Photo direction: the venue building, city skyline or a recognisable landmark; clear sky or golden hour; no people in focus; strong verticals. See `guidelines/10`.

---

## B. Z-overlay event invite

**Canvas** 1200×1200 (cream or `#1F1E1B`) and 1915×1088. **Refs** `social-events/z-overlay-invites--*`.

- Top band (≈21% height) = greyscale city photo + Z overlay; or right-hand vertical image panel (≈11% width, radius 12) on landscape.
- Title Satoshi Regular 88.6/1.2 at x=74, y=319; phrase "Exclusive Dinner" in mint→blue gradient text.
- Meta rows Inter Regular 30, icons 24px, y=706/780/853.
- Footer: `www.zluri.com` Inter 25 bottom-left, logo bottom-right, hairline above optional.
- Speaker strip variant: 5 headshot tiles (radius 8) with name/title, Inter 12–14.
- **Navy pattern variant** (`social-events/navy-pattern-invites--*`): indigo-navy gradient canvas (`#14143C → #2A2670`) with a faint faceted tone-on-tone pattern; white logo top-left (top-right when speakers are shown); title Satoshi Regular, white, no coloured keyword; date/time block in white with the venue in muted lavender-grey beneath; a **full-colour** photo panel on the right (≈39% width, inset 20px, radius 12) instead of the Z overlay; square version adds a white arrow-in-circle swipe badge top-left. Co-brand version: two thin outlined circles overlapping (Venn), intersection filled Mint→blue, one logo in each circle.

---

## C. Product announcement

**Canvas** 1915×1088 (and 1200×1200), `#000`. **Refs** `social-product-launch/product-announcements--*`.

| Element | Spec (1915×1088) |
| --- | --- |
| Logo | top-left x=98, y≈80, 160px wide |
| URL | top-right, Inter Light 32, `#E2DED7` |
| Headline | Satoshi Regular 103/1.16, tracking −6%, cream; product name in gradient `#0067FF→#26ED91`; x=98, y=241, width 814 (3 lines) |
| Sub | Inter Light 37/1.2, `#E2DED7`, y=640, 2 lines max |
| Media | iPad-style frame 887×1158 at x=943, y=189 (cropped by bottom), radius 30, bezel stroke `#E2DED7` 1.5px, screen cream with low-fi UI; or dark wireframe diagram in green line art |
| Atmosphere | launch glow bottom corners + 5% grain |

Headline formulas: "Introducing **{Product}** in Zluri" · "Meet Zluri's **{Product}**" · "Zluri's **{Product}**." Sub = one punchy benefit, often in three beats: "Toxic access combinations. Detected. Blocked. Before your next audit."

Launch-thumbnail variant (IRIS): defocused dark-blue product UI as backdrop + a frosted glass circle/pill "lens" carrying "Introducing / **IRIS** / Identity Risk Intelligence System" and a small blue pill "Now Live in Zluri!".

Partner-program variant (Ascend Alliance): `#161411`, dotted world map with avatar clusters ringed in brand colours, centred headline with blue→mint keyword.

---

## D. Carousels

All carousels: 1 cover + 2–7 content slides + 1 CTA slide (4–9 frames; follow the brief if it sets a count). Same background, logo position and footer device on every slide. One idea per slide. Templates: `templates/social/carousel-dark.html` (D1), `carousel-variants.html` (D2, D4, D5), `carousel-customer-spotlight.html` (D3).

### D1 · "Visibility gap" (dark statement) — 1200×1200

`#000` (`--zluri-black-pure`) with an inset `#111` card (`--zluri-carousel-inset`, inset 30px). Logo top-right 146px. This system's kit — blue highlight label, Mint bullets, pink arrow capsule — is fixed and does not count as extra accents.

- **Cover:** headline Satoshi Regular 122/1.16, −6%, cream with Mint phrase, x=70 y=155; sub Inter Light 42.5 `#E2DED7` y=492; orbit ellipses bottom-right; pill bar bottom-left with pink arrow capsule + "Swipe to learn more".
- **Content:** highlight block label (Bright Blue, Satoshi Regular 62) at y=151 → plain sub-title Satoshi 62 at y=268 → 3 bullets Inter Light 41.7 `#E2DED7` with 50px Mint rounded-8 square bullets containing a pale dot; full-width pill bar at the bottom with the capsule at the right.
- **CTA:** "**Read the Blog** / Today for More Details" (Mint first line), pill bar "Link in the post above" + `↑` capsule.

### D2 · "Problem → solution panels" (GBAR) — 1080×1080

`#161411` (rendered `#000` with dark panels `#1B1915`). URL top-left on cover; slide number bottom-left (Inter 30), logo bottom-right.

- **Cover:** vertically centred headline Satoshi Regular ≈80 with Mint phrase; sub Inter Light; white button radius 8 with green arrow square "Swipe left to learn more".
- **Content:** title Satoshi Regular 60 (persona, Mint keyword) + 1px rule; two stacked panels with a 6px left bar — **red `#D52A00`** "Challenges:" with ☒ rows, **green `#1B9464`** "How Zluri's … Help:" with ☑ rows. Panel title Satoshi 34, rows Inter Light 26.
- **CTA:** bottom-left "**Close the gaps** in your current access reviews" + white "Book a Demo ↓" button.

### D3 · Customer spotlight — 784×784

White canvas, `#161411` card inset 15px radius 12, three huge concentric circle outlines (0.6px `#757678`) behind.

Slides: **Cover** ("**Customer** Spotlight" Satoshi Medium 56, result sentence Inter 24, white button "Swipe to see how they did it →") · **About {Customer}** (two short paragraphs + 3 fact chips: employees, HQ, industry) · **Challenges** (3 rows in `#2A2A2A` radius-6 chips with Fluent icons) · **The Zluri Solution** (3 paragraphs) · **Real Outcomes** (3 stat rows: Satoshi Medium 48 number + Inter 20 label, 3px Mint top rule, `#2A2A2A` fill) · **Quote** (customer logo, quote Inter 24, attribution with customer name in Mint) · **CTA** ("Ready for / **similar results?**" + "Book a Demo ↓").
Number top-left (Inter 20), logo bottom-right 79px.

### D4 · Security news / explainer — 784×784

`#161411`. Header row: number left (Inter 23), logo right, 1.2px rule `#535353` at y=107.

- **Cover:** centred, Satoshi Regular 59, −6%: Mint line + cream line; sub Inter Light 23 `#B2B2B2`; "Swipe →" bottom-right.
- **Content types:** logo-tile list (company + what happened) · Mint icon-tile list · chat-bubble story (attacker bubbles coral `#FF5757`, employee bubble Mint, result chip dark) · product screenshot with one-line caption beginning `→` and Mint key phrase.
- **CTA:** centred "**Secure** Your CRM Today", sub, dark chip button "Link in the comments below ↓".

### D5 · Feature tour (light) — 784×784

White. Title Satoshi Medium 42 with **blue** keyword (`#2266E2`), sub Inter 20 `#797979`; product chart card floating on a **Deep Dive** gradient panel (x=45, y=195, 690×484, radius 8); number bottom-left, dark logo bottom-right. Cover is a full Deep-Dive gradient with white type and "Swipe to see what's new →". CTA slide: centred "See Zluri 2.0 in action" + outline chip.

### D6 · Illustrated / seasonal (Halloween)

Sunset gradient fields, a black "torn paper" card, flat silhouettes. Copy device: **"The Trick / The Treat"** = risk / how Zluri fixes it. Eye mark used as a bullet beside each title. Only for seasonal moments.

---

## E. People and culture

### New joiners — 1200×1200, Deep Blue `#1D4BA6`

- Tone-on-tone **z-maze** line pattern (`assets/motifs/z-maze-pattern.svg`, stroke `#1E51B5` 1.4px).
- **Cover:** "Welcome to the" + "**Zluri Family!**" on a Pink `#E84393` highlight block, Satoshi Regular 106/1.2 at x=104, y=571; pill bar "Meet our January Joiners" + pink capsule; footer `www.zluri.com` + hairline.
- **Person card:** cream polaroid 758×779 at x=202, y=223: pink photo field with a cut-out portrait whose head breaks the top edge; name Satoshi Regular 71.5, role Satoshi Regular 36.8, both `#161411`. Footer label "Meet our January Joiners" + hairline `#E2DED7`. Logo top-right.
- **Closer:** "We're **Growing**" (pink block) / "Interested in joining the Zluri Family?" / "Link in the Bio →".

### Employee spotlight — 1500×1500

`#161411` top fading to blue (`#161411 → #1256A6`) panel radius 24. "Employee / Spotlight!" Satoshi Medium 95/1.1 white at x=112, y=123; story Inter Light 35, width 542; greyscale cut-out portrait right; Bright-Blue pixel steps (176px squares); blue footer band with name (Satoshi Regular 56) and title (Satoshi Medium 56), logo right.

### New-joiner Slack card — 1611×1088 (tall card)

Black card: greyscale portrait top with a Bright-Blue vertical bar accent, name Satoshi 56 white, role Inter small, logo + hairline + two-line welcome.

---

## F. Greetings and observances

**Canvas** 1080 or 1200 square. Logo top-right, always. Greeting top-left (or centred), Satoshi Regular/Light, large, tight, one coloured word; 1–2 line wish in Inter; illustration or photo occupies the lower 50–60%.

| Occasion | Treatment |
| --- | --- |
| Thanksgiving / Christmas (system) | cream or dark card; photo collage (1 large + 2 small tiles) under a diagonal Z band in pink / green / blue |
| Thanksgiving (illustrated) | peach-cream, flat vector table scene, "Thanksgiving" in coral |
| Christmas | light grey grain; "Merry" red; forest-green panel with line-art trees and gold stars |
| New Year | black; outline pill tag; "2026" numerals in blue→cyan gradient with a sparkle and selection-handle gag |
| Diwali | Deep Blue gradient with faint mandala; diyas; "Happy Diwali!" Mint |
| Labor Day | Bright Blue; greyscale cut-out hands on keyboard; "Labor Day" Mint |
| Veterans Day / 4th of July | cream; flag-filled lettering or brushed flag; red-brown `#8E1C00` block with white caps list |
| Data Privacy Week | black; neon glass padlock render; "Data Privacy" cyan→blue; pink arrow capsule CTA |

Tone: warm and brief. Tie to identity/security only when it is natural ("Unauthorized Access Is Silent. Your Defense Shouldn't Be.").

---

## G. Paid ads (4:5)

**Canvas** 1500×1875, `#1A1815`. **Refs** `ads/*`.

- Logo top-left 196px at (111,114).
- Headline Satoshi Regular 100/1.1 at y=300: outcome in Mint + context in white ("**Save 100+ IT Hours** in Google Workspace").
- Sub Inter Regular 50, tracking −2%, cream, ≤3 lines at y=570.
- Optional proof ribbon: Forest-Green pill, Inter Medium white, "40% boost in IT productivity · 75% faster audits · 100% Shadow IT/AI visibility".
- Bottom: glow panel (blue→teal blur, radius 16, 25% grain) with 2–4 dark low-fi UI cards (hairline `#474640`, radius 9–11), e.g. user card, Joiner/Mover/Leaver steps, Slack approval with green Approve / red Reject, audit table. One red notification dot for life.
- Bullet variant: `→` + underlined lead phrase + rest of sentence, Inter 28.

A/B rule the designers followed: change **one** thing per version (headline, sub, ribbon, or UI panel).

---

## H. Recognition banners

**Canvas** 1915×1088. Lead-in "Zluri recognized as a" Satoshi Light ≈50 + "Strong Performer" Satoshi Regular ≈140 top-left; attribution bottom-left Inter ("by **The Forrester Wave™**: SaaS Security Posture Management, Q4 2023"); logo bottom-right. Background from the explorations: Midnight navy radial, indigo with facets, linen diagonal + grain, cream with corner arc lines, or cropped wordmark. Option: award phrase on a royal-blue highlight block.

---

## I. Banners, email, bars

- **Profile banners (2026):** black + indigo aurora; tagline Satoshi Regular (62px on 1584×396) with a faint text glow (5.7px blur duplicate); logo bottom-right; optional dark pill "LIVE NOW".
- **Profile banner (2025):** black with diagonal navy shards; "**The Next-Gen** Identity Governance and Administration Platform" with blue→teal keyword.
- **Email header 800×200:** logo top-left, tagline Satoshi Regular 28.7 below it, hero object at right (glossy shield with orbit ring, or wireframe globe with avatar nodes).
- **Event email banner / signature:** thumbnail system from §A at 1112×348 / 800×200; signature adds outline chip "Booth #EX20" and a small Forest-Green button "Book a Meeting" (radius 4).
- **Review-site banner 2500×476:** black; logo left; centred headline with Mint phrase + Inter sub; QR right; 6px rainbow rule along the bottom.
- **Website announcement bar:** solid bar (red-brown `#8E1C00`, maroon, or purple gradient `#351E78→#57429B`), one sentence Inter/Satoshi 12–18 white, then a small light pill button with `→`.

---

## J. Internal posters and print

POSH series (A3 and 420×595): expressive, illustration-led (hand-drawn fist, lime hands, gender symbols), Satoshi/geometric bold caps headings allowed here, logo bottom-right. These are the only pieces where heavy caps headlines are acceptable.

**Standee / roll-up** (1365×2822, `print-and-posters/standee--*`): `#1F1E1B` canvas; white logo top-left; headline Satoshi Regular in two lines with one phrase in lavender→blue gradient ("Next-**Gen IGA** / for the Cloud Era"); two-line Inter descriptor beneath; the top 35% carries all text (eye level), the middle stays empty, and a single Z-overlay photo tile (blue overlay, radius 8) sits in the bottom 15%. Keep text above 60% of the height so it clears table height at events.

---

## K. Concept and proof posts

Single 1080 / 1200 squares that explain one idea or show proof. Refs: `social-thought-leadership/*`.

- **Named-concept post** ("Samsara Cycle"): cream top third with the headline in Satoshi Light/Regular (one word in a blue→teal gradient), a one-line Inter description ending in an underlined text link ("Read the Blog"), dark logo top-right; the lower two-thirds is a black panel (inset 15px) holding a simple diagram — here a circular loop built from four gradient arc segments (blue, lavender, white) with week labels, a centre word in Satoshi ("Trapped") and four dark label chips at the compass points. One diagram, one idea.
- **Testimonial post** ("Our Early Adopters Are Loving Zluri 2.0"): diagonal pink → purple → blue gradient field; headline Satoshi Regular, white, two lines, left-aligned at ~17% from the left; three stacked glass cards (white at ~15% with a 1px white border, radius 8) each with five gold stars and a short quote in Satoshi/Inter white; white logo centred at the bottom. This is the one sanctioned use of a pink-to-blue gradient field and glass cards — do not generalise it. Quotes must be real and approved.

---

## Pre-flight for any social asset

1. Which system above is it? Open two references from that group.
2. Canvas and margin from `03-layout-and-formats.md`.
3. One motif, one accent, three anchors.
4. Headline ≤ 3 lines at the stated size. Keyword coloured.
5. Logo version and size correct for the background.
6. If a photo is needed → ask the user → source per `guidelines/10-photography-and-stock.md`.
7. Run `12-anti-slop-checklist.md`.
