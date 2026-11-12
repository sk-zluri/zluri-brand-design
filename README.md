# Zluri Brand Design System

A design system for **Zluri** built for AI agents (and people) to produce on-brand work: social posts, carousels, ads, event creatives, video storyboards, decks, banners, emails and web pages.

It was reverse-engineered from the work of Zluri's designers rather than from a brand PDF alone:

| Source | What was taken from it |
| --- | --- |
| **Figma — "Zluri Marketing Brand Design System"** (276 frames across video storyboards, static/social, pitch deck, web animation) | Real canvas sizes, type sizes, tracking, colours, effects, layouts, recurring motifs. Every frame is exported in `references/figma/`. |
| **zluri.com** (homepage + every page in the navbar, 39 pages) | Web type scale, components, spacing, section patterns, and the cursor/scroll interaction language. |
| **Zluri Brand Guidelines 1.01** (PDF) | Logo rules, official palette and gradients, type roles, iconography, imagery principles. |

## Use it with an agent

Give the agent this repository (clone it or share the link) and say what you need:

> Use the Zluri design system at `github.com/sk-zluri/zluri-brand-design`. Read `AGENTS.md` first. Design a LinkedIn event thumbnail for …

`AGENTS.md` tells the agent what to read, which references to look at, which template to start from, and the rules it must not break. `CLAUDE.md` points Claude Code at the same file.

## Use it in Open Design

The repository root is an Open Design design-system package (`manifest.json` + `DESIGN.md` + `tokens.css`, plus `components.html`, `USAGE.md`, `preview/` and `assets/`).

- **From GitHub:** in the Design System surface choose the GitHub import and paste `https://github.com/sk-zluri/zluri-brand-design`
- **From disk:** choose the local-folder import and select this folder (the one containing `manifest.json`)

After import, pick **Zluri** as the design system. For best results also attach or reference the relevant `guidelines/` file and a few images from `references/` in the prompt — the references carry most of the taste.

## What is inside

| Path | Contents |
| --- | --- |
| `DESIGN.md` | The canonical design description — character, logo, colour, type, layout, motifs, components, imagery, motion, do/don't. |
| `tokens.css` | All design tokens: Open Design's shared schema plus `--zluri-*` extensions and a `.zluri-dark` remap. |
| `components.html` | Component fixture rendered only from tokens. |
| `guidelines/` | Twelve documents: foundations, visual language, layout & formats, social & marketing, video & motion, presentations & diagrams, website, web interactions, product-UI illustration, photography & stock sourcing, voice & copy, anti-slop checklist. |
| `templates/` | Working HTML/CSS for 14 asset families (44 artboards) including a full interactive landing page. Rendered previews in `preview/templates/`. |
| `assets/logos/` | Default, monochrome, tagline and Infotech-endorsed logos + the eye mark. |
| `assets/motifs/` | SVG brand motifs exported from Figma (Z-overlay shape, cropped wordmark, arc lines, orbit ellipses, z-maze pattern, quote marks, chain link). |
| `references/` | 276 Figma frames in 14 categories (each with a measured layout spec in `figma/specs/`), 39 website pages, 30 live interaction captures, 31 brand-guideline pages — with `index.json` files for lookup. |
| `preview/` | Colour, typography, spacing and motif pages; rendered templates. |
| `tokens/zluri.tokens.json` | Tokens as JSON (generated from `tokens.css`). |
| `source/` | Evidence and provenance, measured style data, and the scripts used to extract everything. |

## Stock imagery

Zluri's designs often use stock photos (venues, cities, people at work). Agents using this system must **ask for approval before sourcing any image**, then use Magnific through its MCP connector or Pexels through a browser-control skill, shortlist options, and record provenance. The protocol is in `guidelines/10-photography-and-stock.md`. No stock photos are stored in this repository; templates carry labelled placeholders instead.

## Fonts

Satoshi (Indian Type Foundry, via Fontshare) and Inter (Google Fonts) load from their CDNs in the templates. Font files are not redistributed here — see `assets/fonts/README.md`.

## Maintaining

- `tokens.css` is the source of truth. After editing it, regenerate `components.html` and `tokens/zluri.tokens.json` (see `source/evidence.md`).
- To refresh references, re-run the scripts in `source/scripts/` against the Figma file and the site.
- When the designers ship a new system, add its frames to `references/figma/`, describe it in the relevant guideline, and add a template.

## Ownership

Logos, designs and brand assets are the property of Zluri and are provided for creating Zluri-branded work. Third-party logos and product names that appear inside reference images belong to their owners.
