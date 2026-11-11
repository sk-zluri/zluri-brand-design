# 06 · Presentations and diagrams

References: `references/figma/decks-and-diagrams/`, `references/figma/web-animation/`, `references/figma/brand-boards/`, plus the brand-guidelines pages in `references/brand-guidelines-pdf/` (which are themselves a model for document slides). Template: `templates/deck/`.

## Slide types

### 1. Editorial slide (brand-guidelines style)

White or cream 16:9. Small title top-left (Satoshi Medium ≈22px on 1600 wide), body text column on the left third (Inter Light/Regular, `#474640`, max ~38 characters per line), and a large rounded-12 content panel on the right two-thirds (cream `#FBF9F6` fill, 1px linen border). Section dividers: numeral "01" in Deep Blue small above a large Satoshi Regular title on white; cover: Deep Black with huge Satoshi Light title bottom-left and the version in Bright Blue.

Use for: strategy, guidelines, documentation, anything text-led.

### 2. Product-architecture diagram (pitch deck)

**Canvas** 1920×1080, `#F4F4F4` with a faint dot grid (inset 65px), 3px coloured frame, and a **corner tab** top-right naming the slide's pillar.

| Element | Spec |
| --- | --- |
| Corner tab | 710×89 max, flush top-right, colour by pillar (see below), white Inter Medium 29, small outline icon |
| Cards | white, radius 8–13, hairline shadow `0 0 0 1px rgba(0,0,0,.1)`, 16–24 padding |
| Labels | Inter Semibold 29 (group titles), Inter Medium 18 (chips), `#1C1C1F` |
| Connectors | 2–3px, rounded elbows; navy, teal, cyan, magenta — one colour per data path |
| Pills | full radius; navy / teal / cyan / purple fills with white label |
| Hub | large blue circle with a white search glyph = "Patented Discovery Engine" |
| Data panel | light-blue `#5CC3D9`-ish dotted panel "Unified Data Fabric" with white chips and app logos |
| Rule rows | `IF … THEN Run …` rows in white cards with dropdown carets |
| Decisions | green "Approve" / red "Reject" buttons, radius 4 |
| Status | teal check squares in the card corner when a step completes |

**Pillar colours in decks (VIA model):** Visibility = navy `#0B2A5B`-range · Intelligence = cyan `#019AD7` · Action = teal `#22C3A6`-range · Platform = purple. Category tags: Discover (lime), Manage (coral), Govern (cyan).
**Pillar colours on the 2026 website:** Discover = Deep Blue `#1D4BA6` · Govern = Forest `#1B9464` · Secure = red-brown `#8E1C00`. Prefer the website mapping for new work; keep the deck mapping when extending the existing deck.

Build order for a diagram: sources (left) → engine/hub → data fabric → automation/rules → outcomes (right). Reveal left to right, one stage per click.

### 3. Dark flow diagram (website / launch)

`#161411`. Source pills on the left, hub tile in the centre, outcome pills on the right.

- Pills: `#1F1E1B`, 1px `#3A3936`, full radius, 34px tall, app icon(s) + Inter 14 cream.
- Input connectors: 1px cream at 60%, S-curves converging on the hub.
- Hub: 138px rounded-16 tile, subtle circuit pattern, eye mark centred with a soft glow.
- Output connectors: colour-coded — green, orange, red, purple, blue — each ending at its outcome pill with a matching icon.

Animate: inputs draw in (staggered), hub glows, outputs draw out in sequence.

### 4. Isometric layer stack (IRIS)

Four wireframe plates stacked with ~40px gaps on black. Each plate has its own line pattern (decisioning cards, relationship graph, normalised grid, circuit board). The active plate is Mint line art; plates above are faint outlines; plates below are white outlines. A left-hand caps list names the layers; right-hand bullets describe the active one.

### 5. Data slides

Use product-UI chart styling (see `09-product-ui-illustration.md`): periwinkle bars `#82A7ED` / `#9EC1FA`, pastel yellow / peach / lavender / mint for extra series, hairline gridlines `#E8F0FC`, small Inter labels. One chart per slide, headline states the takeaway.

## Deck typography

| Role | Spec (on 1920 wide) |
| --- | --- |
| Slide title | Satoshi Medium 40–56 |
| Section title | Satoshi Regular 80–100, −4% |
| Body | Inter Regular 20–24, `#474640`, ≤ 6 lines |
| Diagram labels | Inter Semibold 24–29 / Medium 16–18 |
| Footer | logo bottom-left (dark) 90px, page number bottom-right Inter 14 |

## Deck rules

- One message per slide; the title is the takeaway, not a topic label.
- Cream or white for content, Deep Black for section breaks and the close, one blue gradient slide at most (cover).
- Product evidence beats adjectives: show the low-fi UI, a number, or a customer quote.
- Customer logos monochrome in a single row.
- No clip-art, no SmartArt-style chevrons, no stock "handshake" photos.
