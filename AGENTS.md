# AGENTS.md — how to design for Zluri with this repo

You are an agent asked to produce a design for **Zluri** (identity security platform). This repository is everything you need. It was built from 276 senior-designer Figma frames, the live zluri.com, and the brand guidelines — so that your output looks like Zluri's human designers made it, not like a generic template.

**The failure this repo exists to prevent:** bland, over-decorated "AI slop". The designers' real work is quiet, large-type, warm-neutral and precise. Match it.

---

## 1 · Read order

| Step | File | Why |
| --- | --- | --- |
| 1 | `DESIGN.md` | The whole system in one read: character, logo, colour, type, layout, motifs, components, imagery, motion, do/don't. |
| 2 | The guideline for your format (table below) | Exact specs: canvas, sizes, positions, variants. |
| 3 | 2–4 images from `references/` for that format | Your visual target. Find them with `references/figma/index.json` or `references/website/index.json`. **Look at them before you design.** |
| 4 | The matching file in `templates/` | A working HTML starting point that already renders correctly. |
| 5 | `tokens.css` | Paste the `:root` block; use `var(--…)` only. |
| 6 | `guidelines/12-anti-slop-checklist.md` | Run it before you show anything. |

Do not skip step 3. Text specs alone produce mediocre results; the references carry the taste.

## 2 · Route the request

| The user wants… | Guideline | References (`references/…`) | Template (`templates/…`) |
| --- | --- | --- | --- |
| Event post / thumbnail / invite | `04` §A–B | `figma/social-events/` | `social/event-thumbnails.html` |
| Product or feature announcement | `04` §C | `figma/social-product-launch/` | `social/product-launch.html` |
| LinkedIn carousel (insight, explainer) | `04` §D1, D2, D4 | `figma/social-carousels/` | `social/carousel-dark.html` |
| Customer story carousel | `04` §D3 | `figma/social-carousels/carousel-customer-spotlight-*` | `social/carousel-customer-spotlight.html` |
| Feature-tour carousel (light) | `04` §D5 | `figma/social-carousels/carousel-zluri-2-0-light*` | adapt `social/carousel-dark.html` on `.c-white` |
| New-joiner / employee / culture post | `04` §E | `figma/social-people/` | `social/people-new-joiners.html` |
| Holiday / observance greeting | `04` §F | `figma/social-festive/` | `social/greeting-z-overlay.html` |
| Paid social ad | `04` §G | `figma/ads/` | `social/ad-portrait.html` |
| Award / recognition banner | `04` §H | `figma/brand-backgrounds/` | adapt `banners/banners-and-email.html` |
| Profile banner, email header/signature, site bar | `04` §I | `figma/banners-and-email/` | `banners/banners-and-email.html` |
| Course / explainer video slides | `05` §1 | `figma/video/academy-*` | `video/academy-slides.html` |
| Feature video intro, testimonial video cards | `05` §2–3 | `figma/video/feature-spotlight*`, `customer-testimonial*` | `video/feature-spotlight-and-testimonial.html` |
| Launch teaser, year-in-review | `05` §4–5 | `figma/video/iris-launch-teaser*`, `zluri-wrapped-2025*` | — (build from references) |
| Pitch deck slide, product diagram | `06` | `figma/decks-and-diagrams/`, `brand-guidelines-pdf/` | `deck/slides.html` |
| Web page / landing page / section | `07` + `08` | `website/full-pages/`, `website/live/` | `web/landing-page.html` |
| Product UI mock-up inside any of the above | `09` | `brand-guidelines-pdf/page-25…27`, `website/live/home-capabilities-*` | UI blocks in `templates/zluri.css` |
| Anything with a photo | `10` | — | — |
| Copy or headline help | `11` | — | — |

Format not listed? Extend the nearest system (see `12-anti-slop-checklist.md` §D) and tell the user which one you extended.

## 3 · Non-negotiables

1. **Fonts:** Satoshi (headlines, Regular/Medium) + Inter (everything else). Nothing else.
2. **Canvas:** cream `#FBF9F6`, warm near-black `#161411`, or Deep/Bright Blue. Named atmospheres only.
3. **One accent moment** per canvas. Mint keyword on dark; blue on light.
4. **Big, light, tight headlines.** Never bold, never all caps, ≤ 3 lines.
5. **Three anchors:** headline block, small corner logo, one footer item. Keep the empty space.
6. **One signature motif** from `guidelines/02-visual-language.md`.
7. **Product UI is the illustration.** Build it in HTML/CSS with plausible data.
8. **Logo:** correct file for the background, ≈12% of width on squares, corner placement, untouched.
9. **Web pages are interactive:** hover states, reveal-on-scroll, and at least one cursor-responsive moment (`guidelines/08`).
10. **Never invent facts.** No fake stats, quotes, customers, dates or awards. Use `[bracketed placeholders]` and list them.

## 4 · Stock photography — ask first

If, and only if, the design genuinely needs a photograph you do not have:

1. **Stop and ask the user for approval**, giving the reason and a concrete image brief.
2. Offer the source: **Magnific via its MCP connector** (preferred when connected) or **Pexels via the browser-control skill**. Also offer "I'll supply one" and a no-photo alternative.
3. After approval, shortlist 3–5 candidates, let the user choose, then download, record provenance, and treat the image per the system.

Full protocol, search patterns and hard limits: `guidelines/10-photography-and-stock.md`. Approval for one image does not cover the next. Never use stock in place of a real Zluri employee or customer.

## 5 · Output expectations

- Build designs as **HTML/CSS at the exact canvas size** (one `.artboard` per frame) unless the user asks for another format. Export PNG/JPG at 1× (posts) or 2× (small banners) when asked.
- Start from the template; keep `tokens.css` + `templates/zluri.css` linked; put design-specific CSS in the page.
- For multi-frame work (carousels, storyboards) keep every frame's anchors identical.
- Render and **look at your output** next to the references before presenting. Fix what differs.
- When presenting, state: which system you used, which references you matched, any placeholders you wrote, and any image you sourced.

## 6 · Repo map

```
DESIGN.md              canonical design prose (start here)
tokens.css             all tokens; :root (cream) + .zluri-dark remap
components.html        web + social component fixture built only from tokens
manifest.json USAGE.md Open Design package files
guidelines/            12 deep-dive documents (foundations → anti-slop)
templates/             working HTML for social, video, banners, deck, web
assets/logos/          every logo variant, named by the background it sits on
assets/motifs/         SVG motifs exported from the designers' Figma file
references/figma/      276 designer frames by category + index.json
references/website/    39 full-page captures, live interaction captures + index.json
references/brand-guidelines-pdf/  the 31 guideline pages + extracted text
preview/               colour / type / spacing / motif pages and rendered templates
tokens/                tokens as JSON
source/                provenance, measured data, extraction scripts
```
