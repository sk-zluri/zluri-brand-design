---
name: zluri-design-system
description: Zluri's brand design system — produce on-brand Zluri (Zluri × Infotech) work: LinkedIn/social posts, carousels, new-joiner and employee-spotlight posts, event thumbnails, ads, banners, email headers, decks, video storyboards and web pages. Use whenever the user asks for anything Zluri-branded or says "Zluri design system", "Zluri brand", "new joiners post", or invokes /zluri-design-system. Includes templates, tokens, 276 designer reference frames, logo lockups, and an employee-photo pipeline (cut-outs, face matching, Gemini/ChatGPT edge extension, AI-watermark removal).
---

# Zluri design system

This skill's folder **is** the design system repository (`github.com/sk-zluri/zluri-brand-design`). Every path below is relative to this folder — resolve it from the skill's base directory, not the user's working directory.

## How to work

1. Read `AGENTS.md` in this folder and follow its read order exactly:
   `DESIGN.md` → the guideline for the format → 2–4 reference images from `references/` (**look at them before designing**) → the matching template in `templates/` → `tokens.css` → `guidelines/12-anti-slop-checklist.md`.
2. Route the request with the table in `AGENTS.md` §2. Respect the non-negotiables (§3) and the precedence rules (§3a).
3. Build in the **user's project folder**, not inside this skill folder. Copy what the page needs next to it (e.g. `brand/tokens.css`, `brand/zluri.css`, the motif SVG, the logo) and link those copies, so the output is self-contained.
4. Render the result and look at it next to the references before presenting. When the user wants to review in a browser, open it there and wait for their OK before exporting PNGs.

## Photos

- **Stock photos:** ask before sourcing — `guidelines/10-photography-and-stock.md`.
- **Photos of real people** (new joiners, spotlights, speakers): follow `guidelines/13-employee-photos.md` and use the scripts in `tools/people/` (`cutout.py`, `fit_faces.py`, `pad_for_outpaint.py`, `remove_ai_mark.py`). When a supplied photo is cropped so that centring shows a hard edge, **ask the user which tool to extend it with — Gemini or ChatGPT (in their signed-in browser) — or whether to skip AI** and align the edge instead. Never feather edges. No AI watermark may reach the deliverable.

## Never

- Invent names, surnames, stats, quotes, customers or dates.
- Use a font other than Satoshi + Inter, or a logo other than the Zluri × Infotech lockup unless asked.
- Spend paid credits or download multi-GB models without a quoted, explicit yes.

## Keeping it current

This folder is a copy of the GitHub repo. To update it: `npx skills update` (if installed with the `skills` CLI) or `git pull` inside the folder (if cloned).
