# 05 · Video storyboards and motion

Six video systems exist in the library. Each has its own canvas mood but shares the type system and logo rules. References: `references/figma/video/`. Templates: `templates/video/`.

---

## 1. Zluri Academy (course and explainer videos)

**Canvas** 1920×1080 (delivered 4K). **Mood:** calm, light, academic. Cream `#FBF9F6`, soft blobs (lavender, blue, mint), 10% grain. Presenter footage sits in a rounded-12 panel.

### Slide catalogue

| Slide | Layout |
| --- | --- |
| **Title / intro** (8 variants) | Centred: logo 139px → title Satoshi Regular 100/1.0, −4%, `#161411`, width 1026 → presenter credit Satoshi Medium 42, Deep Blue ("With Ritish Reddy, / CEO & Co-founder"). Left-aligned variant: block bottom-left at x=140. Optional inset hairline frame (radius 12) with folder-tab chapter nav above or below. Optional floating 3D-ish gradient star / badge shapes at the edges, slightly blurred. |
| **Course intro** | Inset frame; "Title of the course here" Satoshi Regular + "Submodule title here" Satoshi Medium (weight shift = hierarchy); credit in Deep Blue; tab row with the active chapter as a Deep-Blue tab. |
| **Quote — full screen** | Quote centred, Satoshi Regular 80/1.25 on 1920 (−4%); the key clause switches to a heavier weight — **Bold** in the source frame, Medium is an acceptable lighter option — optionally boxed with a 1px hairline. Gradient quote marks (mint→purple parallelograms) top-left and bottom-right. Logo top-right. |
| **Quote + presenter** | Same, quote in the left 55%, presenter panel right. |
| **Titles / sub-topics** | Eyebrow (Satoshi Medium 24, Deep Blue) → title Satoshi Regular 80 at x=140,y=156 → outline folder tabs "PART 1…5" in pastel strokes → big chapter word. |
| **Icons / pointers ×3** | Eyebrow + title, then three 300×300 pastel-gradient rounded-20 tiles at x=390/810/1230,y=390 with label Inter 32 and caption Inter 18 beneath. |
| **Pointers + presenter** | Title left, 3 rows of [small gradient square + label + caption], presenter right. |
| **Icon + bullets** (4K) | Tiny caps eyebrow ("ACCESS REVIEWS", Deep Blue) → title Satoshi Regular → 64px pastel icon tile with Fluent outline icon → sub-heading Inter Medium → 2–4 bullets Inter Regular. Lots of empty cream. |
| **Product showcase** | Hi-fi product screenshot (radius 8–12) floating on a blurred mint/blue gradient panel; logo top-right; optional presenter avatar tile bottom-right with a pastel border. |
| **Infographic** | "80% of people are positive" Satoshi Regular + row of circular avatars with coloured rings (two greyed out for the 20%), or a pie chart with pastel gradient wedges and two labels. |
| **Stats** | Rows of [Deep-Blue filled chip with white number + label]; or, over full-bleed presenter footage, frosted white chips (number bold + label) with the customer logo chip on top. |
| **Customer stat** | Customer logo, "Spending / **30 hours** / per cycle just validating access across / **70+ SaaS Apps**": big numbers Satoshi Regular, connective lines small in Deep Blue; a soft gradient clock/dial shape at left. |
| **Outro — recap** | "Congratulations! You've completed this course." + two-column module list with hairlines (module labels in Deep Blue). |
| **Outro — up next** | "Up next:" + module list; next module solid, later ones at 40% opacity. |
| **Final outro** | Inset frame: "You've just explored **The Visibility Gap in Identity Security.**" + 3 takeaways with small gradient-square bullets + logo bottom-right. |

### Storytelling devices

- **Retro pain:** Windows-95-style dialogs, grey buttons, stacked "Attention!" pop-ups, an Excel 97 window named `Access Request.xlsx`, pixel fonts. These represent *manual, legacy* processes (juggling spreadsheets, chasing approvals, manual provisioning). They cut to clean modern Zluri UI for the "after".
- **Maze:** a white maze with a red dashed path and a red dot; a spotlight/vignette closes in to show limited visibility.
- **UI call-outs:** a zoomed product control (e.g. "THEN.. / Initiate Approval Process / Auto-Reject Request") on a white rounded card with a large soft shadow and an arrow cursor; the hovered option gets a blue border and pale-blue fill.
- **Compliance badges** (SOC, HIPAA, ISO) stacked beside the presenter.

---

## 2. Feature Spotlight (product feature videos)

**Canvas** 3840×2160. Midnight→Deep-Blue gradient (`#0B1D40 → #1D4BA6`) brightening to light blue at the right edge, faint white grid lines (25% cells), heavy blur glow.

- **Intro:** white logo (centre) → outline pill "Feature Spotlight" (1px white, full radius, Satoshi Regular 70) → feature name Satoshi Regular 200/1.0, −2%, cream, centred, two lines max.
- **Screen-recording layout:** same blue field; white logo top-left; feature name top-right in small Inter; the recording sits in a dark rounded-24 window with a thin light border and a tab strip, inset ~1.5% from the edges and bleeding off the bottom.

Template: `templates/video/feature-spotlight-and-testimonial.html`.

---

## 3. Customer testimonial (Underdog)

**Canvas** 3840×2160, pure black.

- Co-brand top-right: `zluri × CUSTOMER`.
- **Intro:** chain-link ∞ glyph (gradient stroke white→blue) → title Satoshi Light/Regular white with Mint key phrase ("Always **Audit-Ready**") → sub Inter Light.
- **Lower third:** frosted grey panel, name Satoshi Regular, role Inter small, with a blue→white 4px underline that draws in from the left.
- **Question card:** "Question **01**" (number in Mint) + the question in Inter Light, centred.
- **Outro:** "Still Running / **Access Reviews** Manually?" + "See how Zluri's IGA platform changes that at **www.zluri.com**"; then QR + URL; then the chain link with both logos inside the loops.
- **Signature footer:** a glossy blue→white curved swoosh along the bottom edge of title cards.

---

## 4. Launch teaser (IRIS)

**Canvas** 2160×2160, pure black, minimal.

Sequence: pill outline "Meet IRIS" multiplying into offset copies → horizontal hairlines streaming across (periwinkle→white) → the text "Our Identity Risk Intelligence System" typed inside an expanding pill with a blinking gradient cursor → pill contracts into a circle → the circle becomes an iris/eye ring (purple→white gradient ring, dark disc, small glowing dot) with a lens flare → reveal "Meet / **IRIS** / Identity Risk Intelligence System / [Now Live!]" inside the ring. Logo white, bottom-centre, throughout.

Rules for teasers: 1–2px strokes, one gradient (periwinkle→white), no fills until the reveal, type Satoshi Light/Regular.

---

## 5. Zluri Wrapped (year-in-review)

**Canvas** 1200×1200 slides (video + carousel). The one maximalist system.

- Base: Obsidian Smoke gradient + 10% grain + crumpled plastic-wrap texture overlays; or a Midnight-blue grid panel inset 15px (radius 24).
- Header: "yearly recap / 2025" Inter Light 20, lowercase, tracking +20%, top-left; white logo top-right.
- Headline: Satoshi **Bold** 60, −3%, with one phrase inside a glossy gradient pill (pink, periwinkle, green).
- Content objects: glassy 3D number tiles ("68", "13"), folder-shaped cards in secondary-palette gradients, paper notes with paperclips, app-icon tile grid, rainbow bar chart of G2 badges, partner logo chips, event photos as tilted prints.
- Mint for the numbers that matter in running text ("**425+** Features Shipped").
- Closer: "Thank You!" in huge Satoshi Bold with a tilted green sticker and a pink pill sign-off.

Use this vocabulary only for celebratory recaps.

---

## 6. 50K-followers style (isometric grid)

Cream field with a hairline square grid rotated ≈−15°. Some cells are solid brand-colour tiles (orange, red-brown, mint, blue, forest) carrying a tiny caps label, a product name and a circular icon badge; other cells hold blue Inter-Light text snippets, pink year pills, a map, a mini chart. The hero number ("50,000") is set in a blue→teal gradient. The camera pans/zooms across the grid.

---

## Tracking by system (measured)

| System | Display size | Tracking |
| --- | --- | --- |
| Academy titles and quotes | 80–100px on 1920 | −4% |
| Feature Spotlight title | 200px on 3840 | −2% |
| Wrapped headlines (Satoshi Bold) | 60px on 1200 | −3% |
| Testimonial / teaser titles | 100–200px on 3840 | 0 to −2% |

These override the general display-tracking rule in `DESIGN.md` §4.

## Motion principles (all video)

| Property | Guidance |
| --- | --- |
| Entrances | fade + 20–40px rise, 0.5–0.7s, ease-out (power2/power3). Stagger siblings 0.08–0.12s. |
| Headlines | line-by-line or word-by-word rise with mask; never typewriter except the teaser pill. |
| Keyword | colour arrives with or just after the word (0.2s colour tween), or highlight block wipes left→right (0.6–1s). |
| Blobs / glows | drift 2–4% of canvas over 8–12s, looping; never pulse. |
| Lines | draw-on with stroke-dashoffset, 0.8–1.2s, ease-in-out. |
| UI | cards rise 12px + fade; cursors move on eased paths; clicks show a 1.03 scale tap. |
| Numbers | count up 0.8–1.2s, ease-out; settle with no overshoot. |
| Transitions | cross-dissolve on the cream system; hard cut or luminance wipe on black systems. |
| Exits | faster than entrances (0.25–0.35s). |
| Avoid | bounces, elastic easing, spins, glitch effects, particle bursts, lens-flare spam. |

Safe areas: keep text 7% from the left/right and 9% from top/bottom; leave the bottom 12% clear when captions will be burned in.
