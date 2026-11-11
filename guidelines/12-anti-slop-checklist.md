# 12 · Anti-slop checklist

The previous Zluri design system was built from the brand PDF alone and produced "mediocre at best, AI-slop at worst". This checklist exists to stop that. It names the specific failure modes and gives the Zluri-correct alternative taken from the designers' real work.

Run it **before** showing any design. If any item in section A is true, fix it first.

## A. Instant-fail tells

| Slop tell | Zluri-correct |
| --- | --- |
| Purple→pink or blue→purple gradient as the default background | Cream `#FBF9F6`, near-black `#161411`, or a *named* atmosphere (launch glow, indigo aurora, Deep Dive panel) used once |
| Glassmorphism cards everywhere, frosted everything | Solid cards with 1px hairline borders; glass only for a single "lens" (IRIS thumbnail) or chips over video |
| Bold/Black-weight headline | Satoshi Regular or Medium, large, tracking −4% to −6% at display sizes |
| ALL-CAPS headline | Sentence/Title case; caps only for ≤14px eyebrows |
| Everything centred | Left-aligned blocks anchored to corners; centre only for title cards and greetings |
| Three (or four) icon+title+blurb columns as filler | A low-fi product UI fragment, a real number, or nothing |
| Emoji, clip-art icons, mixed icon styles | Fluent outline icons, one size, text colour |
| Generic "AI network" art: glowing nodes, globes, circuit brains, robot hands, hooded hackers | Product UI, Z-overlay photo, line geometry, or a real venue/people photo |
| Rainbow of accents (blue + green + purple + orange + pink together) | One accent moment per canvas; secondary colours only in their documented jobs |
| Heavy drop shadows, neon glows, bevels | Flat; one ambient shadow `0 0 10px rgba(0,0,0,.1)` at most |
| Cool grey text / `#000` on `#FFF` | Warm neutrals: `#161411`, `#474640`, `#E2DED7`, `#FBF9F6` |
| Giant centred logo, logo with effects, wrong logo on wrong background | Small corner logo (≈12% width on squares), correct on-light/on-dark/mono file |
| Lorem ipsum, fake stats, invented customer quotes | Real or user-supplied copy; bracketed placeholders flagged to the user |
| Random stock photo dropped in without asking | Ask first; follow `10-photography-and-stock.md` |
| A third typeface (serif "editorial" accent, mono "techy" labels) | Satoshi + Inter only |
| Rounded-everything (24–32px radii on all boxes) | 8 for cards, 16 for buttons/media, 20 for nav; pills only for tags/capsules |
| Decorative gradient text on whole headlines | Gradient (or Mint) on **one phrase** only |
| Crowded canvas, tiny type, 5+ text styles | Three anchors, 2–3 type sizes, the middle may be empty |

## B. Fidelity checks

**Canvas**
- [ ] Correct preset size and margin for the format (`03-layout-and-formats.md`).
- [ ] Canvas is cream, near-black, deep/bright blue, or a documented atmosphere.
- [ ] Grain present where the reference system uses it (5–10%).

**Type**
- [ ] Satoshi for headlines, Inter for everything else; fonts actually loaded (no fallback rendering).
- [ ] Headline size within the measured range for the format; ≤ 3 lines; good line breaks (no orphans, no hyphenation).
- [ ] Tracking: −0.04em ≥60px, −0.06em ≥100px, 0 on web headings and all Inter text.
- [ ] Exactly one emphasised phrase; correct emphasis colour for the canvas (Mint on dark, Blue on light).
- [ ] Body ≥ 4.5:1 contrast; metadata not smaller than the reference.

**Colour**
- [ ] Every hex is from `tokens.css`. No near-miss blues/greens.
- [ ] One accent moment. Logo ring colours not used as fills.
- [ ] Gradients are named ones, used as background or panel only.

**Composition**
- [ ] Three anchors (headline block, logo, footer item) + at most one media group.
- [ ] One signature motif (`02-visual-language.md`), not zero, not three.
- [ ] Shared left edge; consistent margins; hairlines 1px.
- [ ] Logo: right file, right corner, right size, clear space kept.

**Imagery**
- [ ] Product UI is built in HTML/CSS with plausible data, readable at final size.
- [ ] Photos approved by the user, treated per system (colour venue / greyscale + Z overlay / contextual).
- [ ] No third-party marks used as hero art.

**Copy**
- [ ] Keyword is a thing, not an adjective. No exclamation marks outside greetings/culture.
- [ ] Product names and acronyms exact. CTA string matches the context list.
- [ ] Nothing invented without a flag.

**Web only**
- [ ] Section rhythm white ↔ cream ↔ black; eyebrow colours per code.
- [ ] Hover states on every control; reveal-on-scroll; one cursor-responsive moment.
- [ ] Works at 1440 / 991 / 767 / 390; reduced-motion respected.

**Video only**
- [ ] Safe areas respected; ease-out motion; no bounce; exits faster than entrances.

## C. The side-by-side test

Open the two closest images from `references/figma/` next to your output and ask:

1. Could these three have been made by the same designer in the same week?
2. Is my headline as large and as light as theirs?
3. Do I have as much empty space as they do?
4. Is my accent used as sparingly?
5. Is there anything in mine that appears in *none* of the references? Remove it or justify it.

If the answer to (1) is no, find the difference and fix it before presenting.

## D. When the brief asks for something off-system

Briefs sometimes need a new format. Extend rather than invent:

- Reuse the nearest system's canvas, type ratios and motif.
- Keep the constants: fonts, palette, logo rules, three anchors, one accent.
- Tell the user which reference you extended and what is new.
