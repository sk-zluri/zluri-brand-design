# 08 · Web interactions — cursor, hover and scroll

zluri.com is noticeably **interactive**: backgrounds react to the pointer, diagrams respond to hover, and scroll drives stacked and pinned scenes. A new Zluri page that is static will feel off-brand. This file documents what the live site does (verified by capturing before/after states and reading the page scripts on 11 Nov 2026) and gives drop-in recipes.

Captures: `references/website/live/`. Working examples: `templates/web/landing-page.html`.

## Stack used on the live site

| Library | Version | Job |
| --- | --- | --- |
| GSAP + ScrollTrigger (+ ScrollToPlugin) | 3.12–3.13 | all custom tweens, scroll scrub, pinning |
| Unicorn Studio | 2.1.4 | WebGL background scenes that react to the mouse (`data-us-project`, 60fps, dpi 1.5) |
| Swiper | 11 | card sliders with arrows, mousewheel, keyboard |
| Splide + AutoScroll | 4.1 | logo marquees (loop, free drag, speed 0.8) |
| Custom canvas runtime | — | NHI hero icon field (pointer parallax + depth blur) |
| Webflow IX2, Finsweet (cmsfilter, accordion) | — | reveals, filters, accordions |

For new work, GSAP + ScrollTrigger and a small canvas/WebGL hero cover every pattern. Do not add a smooth-scroll library — the site uses native scroll.

## Motion tokens

| Token | Value | Use |
| --- | --- | --- |
| `--motion-fast` | 200ms | hover colour, underline, chip state |
| `--motion-base` | 440ms | button background, card state |
| reveal | 600ms, stagger 120ms | content swaps, bullets entering (y 20→0, opacity 0→1) |
| layer move | 600ms `power2.out` | diagram parts shifting |
| layer fade | 350ms | diagram part opacity |
| nav dropdown | open 100ms + 100ms, close 60ms `power2.out` | mega menu |
| nav hide/show | 1s / 0.5s `power3.out` | on entering/leaving a sticky scene |
| wipe | 1s `power2.out` | highlight bar behind text |
| scrub | `scrub: 1` | scroll-linked blur/scale, path drawing |
| easing | `cubic-bezier(.215,.61,.355,1)` ≈ `power2.out`; `power3.out` for big moves | everything |

Nothing bounces. Nothing loops attention-seekingly except the logo marquee and ambient background drift.

---

## Catalogue of live behaviours

### 1. Cursor-reactive hero field (home)
Full-viewport dark canvas of fine diagonal light streaks (grey on `#161411`). The streak field **flows and bends around the pointer** like fluid; when the pointer leaves it relaxes. Copy and buttons sit on top, untouched. See `home-hero-cursor-state-a/b.jpg`.

### 2. Light-ray burst band (home CTA, UIC hero)
Rays of white light converge on a vanishing point behind the headline; glassy orbs carrying app icons drift through. The whole scene shifts subtly with the pointer.

### 3. Depth-of-field icon field (NHI hero)
On deep maroon `#2A000A`, a grid of pink `#FFB8B8` outline icons at several depths (blur radii 0 / 0.75 / 1.5 / 2.5 / 3.75px). Pointer movement creates parallax between depths. Falls back to a static frame on low-power devices, Save-Data and reduced-motion.

### 4. Hover-driven layer stack (IRIS — home + IRIS page)
Four isometric plates. Hovering a layer name **or** a plate:
- that plate becomes active (Mint line art),
- plates above turn into faint outlines, plates below into white "inactive" outlines (350ms fades),
- neighbours move ±40px to open a gap (600ms `power2.out`),
- the right-hand bullet list re-enters, staggered (y 20→0, 600ms, 120ms stagger),
- the left list highlights the active label (white) and dims the rest (~30%).

### 5. Isolate-on-hover (ISPM foundation, AI leaderboard)
All items are lit by default. Hovering one dims its siblings (opacity → 0.6, or removes their `is_active` state); mouse-leave restores all.

### 6. Hover-to-switch tabs (Products mega menu)
`mouseenter` on a tab link triggers the tab. Use for navigation previews only — content tabs in the page body switch on click.

### 7. Stacked cards with depth (home capabilities)
Sticky tab bar (IVIP / IGA / ISPM). As each full-width card scrolls in, the previous card scales to 0.99 and blurs 5px (scrubbed between `top 50%` and `top 20%`). Active tab takes the pillar colour.

### 8. Pinned step scene (UIC "Ways to connect")
Section pins; every 300px of scroll activates the next pathway card and its connector line (grey → Mint), finally lighting the platform bar they all feed.

### 9. Scroll-drawn path + highlight wipe (State of AI)
An SVG path draws with scroll (`strokeDashoffset`, scrub 1) with a live % counter; key sentences get a pink/red highlight bar that wipes in at `top 80%`.

### 10. Sliders and marquee
Problem slider: 3-up, 20px gap, 480–600ms, arrows + horizontal mousewheel + keyboard. Logo marquee: continuous, slow, pauses never (drag allowed), edges fade into the section colour.

### 11. Micro-interactions
- Primary button: `#366ECF → #1D4BA6`, 440ms.
- Secondary button: fill to cream; outline button label shifts to Deep Blue.
- Links: underline wipe using a 2px `background-image` line that grows from 0 to 100% width.
- Footer links and a few legacy links pick up **logo-ring colours** on hover (lime `#D3FF57`, cyan `#57E1FF`, coral `#FF5757`) — a small brand wink; keep it to footers and social icons.
- Link cards lift 5px; bordered cards darken their border.
- Slider arrow buttons: fill turns red-brown on hover (legacy) — prefer Deep Blue for new work.

---

## Recipes

### A. Cursor-reactive streak field (no external service)

```html
<canvas id="z-field" aria-hidden="true"></canvas>
<script>
(() => {
  const c = document.getElementById('z-field'), x = c.getContext('2d');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let W, H, m = {x: -9999, y: -9999}, t = 0;
  const fit = () => { const d = Math.min(devicePixelRatio, 1.5); W = c.width = c.clientWidth * d; H = c.height = c.clientHeight * d; };
  addEventListener('resize', fit); fit();
  c.parentElement.addEventListener('pointermove', e => { const r = c.getBoundingClientRect(), d = W / r.width; m.x = (e.clientX - r.left) * d; m.y = (e.clientY - r.top) * d; });
  c.parentElement.addEventListener('pointerleave', () => { m.x = m.y = -9999; });
  const N = 90;                                   // number of streaks
  function frame() {
    x.clearRect(0, 0, W, H); t += 0.004;
    for (let i = 0; i < N; i++) {
      const o = (i / N) * (W + H) - H * 0.5;      // diagonal offset
      x.beginPath();
      for (let s = 0; s <= 40; s++) {
        const u = s / 40; let px = o + u * H * 0.9, py = H - u * H;      // 48° diagonal
        py += Math.sin(u * 5 + i * 0.35 + t * 6) * 10;                    // slow drift
        const dx = px - m.x, dy = py - m.y, d2 = dx * dx + dy * dy, R = W * 0.18;
        if (d2 < R * R) { const f = (1 - Math.sqrt(d2) / R) ** 2 * 70; const a = Math.atan2(dy, dx); px += Math.cos(a) * f; py += Math.sin(a) * f; }  // bend around pointer
        s ? x.lineTo(px, py) : x.moveTo(px, py);
      }
      x.strokeStyle = `rgba(251,249,246,${0.03 + 0.07 * Math.abs(Math.sin(i * 1.7))})`; x.lineWidth = 1 + (i % 7 === 0 ? 1.5 : 0); x.stroke();
    }
    if (!reduce) requestAnimationFrame(frame);
  }
  frame();
})();
</script>
<style>#z-field{position:absolute;inset:0;width:100%;height:100%}</style>
```

### B. Hover-driven layer stack

```js
const links = [...document.querySelectorAll('[data-layer-link]')];
const plates = [...document.querySelectorAll('[data-layer]')];
const panels = [...document.querySelectorAll('[data-layer-panel]')];
function activate(i) {
  links.forEach((l, k) => l.classList.toggle('is-active', k === i));
  panels.forEach((p, k) => p.classList.toggle('is-active', k === i));
  gsap.fromTo(panels[i].children, { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: .6, stagger: .12, ease: 'power2.out' });
  plates.forEach((pl, k) => {
    pl.dataset.state = k < i ? 'above' : k === i ? 'active' : 'below';     // style via [data-state]
    gsap.to(pl, { y: k < i ? -40 : k > i ? 40 : 0, duration: .6, ease: 'power2.out' });
  });
}
[...links, ...plates].forEach((el, k) => el.addEventListener('mouseenter', () => activate(k % links.length)));
activate(0);
```
```css
[data-layer]                 { transition: opacity .35s, color .35s; color: #fbf9f6; }
[data-layer][data-state=above]  { opacity: .25; }
[data-layer][data-state=active] { color: #4ad89a; }
[data-layer-link]            { opacity: .3; transition: opacity .2s; }
[data-layer-link].is-active  { opacity: 1; }
```

### C. Isolate on hover (pure CSS)

```css
.z-group:hover .z-item          { opacity: .6; }
.z-group:hover .z-item:hover    { opacity: 1; }
.z-item                         { transition: opacity var(--motion-fast) var(--ease-standard); }
```

### D. Stacked cards that recede

```js
gsap.utils.toArray('[data-stack-card]').forEach((card, i, all) => {
  if (!i || innerWidth <= 991) return;
  gsap.to(all[i - 1], { scale: .99, filter: 'blur(5px)', ease: 'power1.out',
    scrollTrigger: { trigger: card, start: 'top 50%', end: 'top 20%', scrub: 1 } });
});
```

### E. Pinned step scene

```js
const cards = gsap.utils.toArray('.step'), STEP = 300;
ScrollTrigger.create({ trigger: '.steps', start: 'top top', end: `+=${(cards.length + 1) * STEP}`, pin: true, scrub: true,
  onUpdate: s => { const n = Math.floor((s.scroll() - s.start) / STEP); cards.forEach((c, i) => c.classList.toggle('active', i <= n)); } });
```

### F. Highlight wipe and underline wipe

```css
.z-mark  { background: linear-gradient(#e84393,#e84393) no-repeat 0 0 / 0% 100%; transition: background-size 1s var(--ease-standard); }
.z-mark.in { background-size: 100% 100%; }
.z-link  { background: linear-gradient(currentColor,currentColor) no-repeat 0 100% / 0% 2px; transition: background-size var(--motion-fast) var(--ease-standard); }
.z-link:hover { background-size: 100% 2px; }
```

### G. Reveal on scroll (default for any new section)

```js
gsap.utils.toArray('[data-reveal]').forEach(el => gsap.from(el, { y: 24, opacity: 0, duration: .6, ease: 'power2.out',
  scrollTrigger: { trigger: el, start: 'top 85%', toggleActions: 'play none none none' } }));
```

### H. Floating nav

```js
// dropdowns open on hover (desktop), click (touch)
// hide the bar while a sticky scene owns the top of the viewport
ScrollTrigger.create({ trigger: '.sticky-scene', start: 'top top', onToggle: s =>
  gsap.to('.nav', { y: s.isActive ? '-110%' : '0%', duration: s.isActive ? 1 : .5, ease: 'power3.out', overwrite: true }) });
```

---

## Rules

1. **Every new page gets at least:** hover states on all controls, reveal-on-scroll, and one cursor-responsive hero or diagram.
2. **Interaction explains the product.** Hover a layer to learn about that layer; scroll to watch connectors light up. No decoration-only parallax.
3. **Pointer effects are ambient.** Displacement is gentle (≤70px), low-contrast, behind the text; it must not hurt legibility.
4. **Desktop-only for heavy scenes** (`min-width: 992px`); below that, show the resting state stacked vertically.
5. **Reduced motion:** honour `prefers-reduced-motion` — render the static frame, keep colour-only hovers.
6. **Performance:** cap DPR at 1.5, pause canvases off-screen, 60fps budget, no layout-thrashing properties (animate `transform`, `opacity`, `filter`).
7. **Keyboard parity:** anything revealed on hover must also be reachable by focus.
8. Capturing these pages for QA: the WebGL canvas makes plain viewport screenshots blank after scrolling; capture with a clipped full-page screenshot instead.
