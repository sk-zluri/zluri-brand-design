# Zluri Usage

Package guide for Open Design agents and reviewers.

## Read Order

1. Read this file to understand the package.
2. Read `DESIGN.md` for visual intent, constraints and anti-patterns.
3. For the asset type you are making, read the matching file in `guidelines/` (routing table in `AGENTS.md`).
4. Look at 2–4 images from `references/` for that asset type (`references/figma/index.json` lists every frame by category; `references/figma/specs/<node-id>.json` gives its measured layout).
5. Open the matching file in `templates/` — it is a working starting point.
6. Paste the **whole** `tokens.css` (the `:root` block and the `.zluri-dark` / `[data-theme="dark"]` remap) into the first `<style>` of the artifact, or link the file. Add `class="zluri-dark"` or `data-theme="dark"` to any section that should sit on Deep Black.
7. Open `components.html` for exact component rules (buttons, eyebrows, cards, collapsed grids, stats, low-fi product UI, pill bar).
8. Run `guidelines/12-anti-slop-checklist.md` before presenting.

When rules collide, follow the precedence order in `AGENTS.md` §3a: brief → format recipe → global rules → token defaults.

## Design Highlights

- Cream `#FBF9F6` and warm near-black `#161411` are the two canvases; every neutral is warm.
- Satoshi Regular/Medium headlines, large and tight (−0.04em at ≥60px), never bold; Inter for everything else.
- One accent moment: Bright Blue `#366ECF` for actions, Mint `#4AD89A` for the keyword on dark.
- Hairline borders, radii 8 / 16 / 20, one ambient shadow at most.
- The product is the illustration: low-fi UI cards on a gradient glow panel.
- Signature motifs: mint keyword, Z colour overlay on greyscale photos, soft blobs + grain, launch glow, cropped wordmark, 1px line geometry, highlight block, arrow capsule.
- Web pages respond to the cursor and to scroll (see `guidelines/08-web-interactions.md`).

## Do

- Keep the schema token names; add brand values through `--zluri-*` tokens only.
- Use `--accent` for the single primary action and for links; use `--zluri-mint-green` only as emphasis on dark.
- Start from the closest template and the closest reference image.
- Keep three anchors per canvas (headline block, small corner logo, one footer item) and leave the middle open.
- Ask the user before sourcing any stock photo, then follow `guidelines/10-photography-and-stock.md`.

## Avoid

- Raw hex values outside the token block (third-party logo colours and photo placeholders excepted).
- Purple-to-pink "AI" gradients, glassmorphism everywhere, neon glows, heavy shadows.
- Bold or all-caps headlines, a third typeface, centred-everything layouts.
- Icon-plus-blurb filler rows, emoji, generic "network of dots" art.
- Using the logo's ring colours (cyan, lime, coral) as fills or text.
- Invented statistics, quotes, customers or dates — use bracketed placeholders and flag them.
