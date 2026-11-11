# 09 · Product UI as illustration

Zluri's "illustration style" is its own product. There are three fidelity levels (Brand Guidelines pp. 25–27) and they are used constantly in the designers' work. Build these in HTML/CSS — do not generate them as images.

## Level 1 — Low-fidelity UI (the default)

Simplified, legible-at-a-glance UI fragments that communicate *what the feature does*.

**Use for:** social posts, ads, web feature rows, deck slides, thumbnails.

### Anatomy

- **Panel:** rounded-16 container with a soft gradient glow (pillar-tinted or blue→violet / blue→teal), 1px tinted border, optional 25% grain. On dark canvases: blue glow panel behind dark cards.
- **Card(s):** white or cream (`#FBF9F6`) on light; `#1B1B1B` with 1px `#474640` on dark. Radius 8–12. Soft multi-layer shadow only when floating over a photo or device.
- **Content:** 12–20 "real-looking" data points max. Names, apps and numbers should be plausible and specific.
- **One alert accent** per composition: a coral banner, a red notification dot, a "Risk Detected" chip.

### Building blocks (all observed)

| Block | Spec |
| --- | --- |
| Card title | Satoshi Medium 18–24 (e.g. "Identity Landscape", "Onboarding Playbook", "High Risk Accounts") + optional grey meta chip "Last updated 2 min ago" |
| Stat tile | label Inter 13 → number Inter/Satoshi 18–20 Bright Blue + delta chip (mint bg `#94E9C0`/green text for good, coral bg for risk, with ↗) |
| Count rows | label left, number right, optional coral badge on the risky row |
| Alert banner | coral `#E5704E` bar radius 6, white text "43 Critical Risks Detected", ghost button "Review now" |
| Segmented tabs | text tabs; active = lavender `#A99CE3` chip with white text |
| Table | header row Inter 12 `#717171`; rows 40–48px with hairlines; avatar/app icon + name; **status chips** as outlined tags (coral "Service Account", orange "API Key", blue "AI Agent") or filled (red "Revoked", green "Managed") |
| Rule builder | `WHEN` / `IF` / `RUN` / `THEN` tags (lavender `#A99CE3`, coral, orange `#F3BD60`, pink) followed by dashed-outline "+ Add Trigger" chips or filled condition chips |
| Workflow steps | app logo → chip "Add a user" → `→` → chip "Add user to group", rows separated by hairlines |
| Approval | message + green **Approve** (`#1B9464`) and red **Reject** (`#D52A00`) buttons, radius 4–5 |
| Lifecycle list | "Joiner / Mover / Leaver" groups with numbered coloured squares (blue, orange, red) |
| Progress bars | thin 4px rounded bars in blue, coral, orange, mint with value right-aligned |
| Chart | stacked bars in lavender / orange / coral; or periwinkle bars `#82A7ED`; pale gridlines; tiny legend dots |
| Person chip | avatar + name + role, optional "Risk Detected" coral tag |
| Access graph | small node cards connected by thin dashed lines (User → Group → Account) |

### Colour for UI states

| Meaning | Colour |
| --- | --- |
| Primary data / links | Bright Blue `#366ECF` (`#2266E2` in product) |
| Good / managed / approve | Forest `#1B9464` / Mint tint |
| Risk / revoke / reject | Red `#D52A00`, coral `#E5704E` |
| Warning / pending | Orange `#E89604`, `#F3BD60` |
| Category tags | Lavender `#A99CE3`, pink `#E84393`, purple `#7763C7` |
| Neutral chips | `#F6F7FA`, `#E8F0FC` (cool tints are allowed *inside* product UI) |

Fonts inside UI: Inter (the real product uses Sora; use Sora only when imitating a real screenshot).

### Device frame

Launch posts place the low-fi screen in a tablet frame: radius 30 on a 887px-wide device, 1.5px `#E2DED7` bezel line, three tiny traffic-light dots top-left (one red), screen cream. The frame is always **cropped by the canvas edge**.

## Level 2 — Contextual UI

A lifestyle photo of someone working, with 2–4 UI fragments layered on top.

- Photo: neutral office/home-office, person looking at a laptop, not at the camera; soft light; palette of whites, greys, naturals.
- UI fragments: white cards (radius 8–12), 1px white/linen border, soft shadow (`0 10px 30px rgba(0,0,0,.12)`); sized so text is readable; overlap the subject's shoulder/desk, never the face.
- One fragment carries the "moment": "User is Marked for Onboarding", "Risk Detected · Robert Williams · Finance Head".
- Optional live-collaboration cursor chip ("Jake" on Bright Blue).

**Use for:** web heroes (IVIP, ISPM), customer-story headers, brand slides.

## Level 3 — High-fidelity screens

Real product screenshots.

- Frame: rounded-8–12, 1–2px light-blue or linen border; top of the app visible; bottom fades to the background (linear mask) or is cropped.
- Sit them on a blurred mint/blue gradient panel (Academy) or directly on dark (`#161411`) in carousels.
- Add at most one annotation: a caption line beginning `→` with the key phrase coloured, or a zoomed call-out card with a cursor.

**Use for:** product marketing, feature tours, training, documentation.

## Choosing a level

| Goal | Level |
| --- | --- |
| Explain a concept in one glance (social, ads, hero) | 1 |
| Humanise / show fit in a workday | 2 |
| Prove it is real, teach exact steps | 3 |

## Rules

- Real-sounding data: "ChatGPT · AIA203 · AI Agent", "38 out of 100 identities did not use GitHub in the last 90 days". No "Lorem", no "User 1".
- Keep UI text ≥ 11px at final render size on social; otherwise simplify.
- Never mix levels in one composition.
- Do not invent product features. If unsure a capability exists, use a generic but accurate fragment (table + status chips) and flag it to the user.
- Third-party app logos (Slack, Okta, AWS…) appear as small monochrome/colour icons inside UI only, never as hero art.
