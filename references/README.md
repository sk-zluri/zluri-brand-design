# References

The visual ground truth for this design system. **Look at these before designing.**

| Folder | What it is | Index |
| --- | --- | --- |
| `figma/` | 276 frames exported from the Figma file "Zluri Marketing Brand Design System", grouped by asset category. | `figma/index.json` |
| `website/full-pages/` | Full-page captures of zluri.com (homepage + every navbar page, 39 pages) at 1920px, scaled to 1100px wide. Viewport-triggered animations are missing from these; see `live/`. | `website/index.json` |
| `website/live/` | In-viewport captures of animated and interactive sections, including before/after cursor states. | n/a |
| `brand-guidelines-pdf/` | The 31 pages of Zluri Brand Guidelines 1.01 as images, plus `extracted-text.txt`. | n/a |

## Figma categories

| Category | Frames | Groups | Contents |
| --- | --- | --- | --- |
| `figma/video/` | 84 | academy-templates (45), zluri-wrapped-2025 (12), customer-testimonial-underdog (10), iris-launch-teaser (10), academy-ui-callouts (3), 50k-followers (2), feature-spotlight (2) | Video storyboards: Academy templates, Wrapped, customer testimonial, launch teaser, feature spotlight |
| `figma/social-carousels/` | 49 | carousel-zluri-2-0-light (9), carousel-security-news (8), carousel-halloween-illustrated (7), carousel-customer-spotlight-narvar (7), carousel-customer-spotlight-radicle (7), carousel-access-visibility-gap (6), carousel-gbar-dark-panels (5) | Seven LinkedIn carousel systems |
| `figma/social-events/` | 46 | event-thumbnails-2025-26 (20), z-overlay-invites (9), event-posts-2025 (8), navy-pattern-invites (5), zluriverse-and-elevate-2024 (4) | Event thumbnails, Z-overlay invites, navy pattern invites, conference posts |
| `figma/social-people/` | 25 | new-joiners (23), employee-spotlight (2) | New joiners, employee spotlight |
| `figma/banners-and-email/` | 15 | profile-banners-and-email (8), event-email (4), website-announcement-bars (3) | Profile banners, email headers/signatures/banners, website announcement bars |
| `figma/brand-backgrounds/` | 11 | recognition-banners (11) | Recognition banners exploring backgrounds, patterns and cropped wordmark |
| `figma/ads/` | 10 | reddit-google-workspace (10) | Paid social ads (4:5) with A/B variants |
| `figma/social-festive/` | 10 | greetings (10) | Holiday and observance greetings |
| `figma/social-product-launch/` | 10 | product-announcements (5), ascend-alliance (3), iris-launch (2) | Product announcements, IRIS launch thumbnails, partner-program launch |
| `figma/decks-and-diagrams/` | 6 | pitch-deck-diagrams (6) | Pitch-deck product architecture diagrams |
| `figma/print-and-posters/` | 4 | posh-internal-posters (3), standee (1) | Internal posters and standee |
| `figma/brand-boards/` | 3 | palette-and-type (3) | Palette and type boards |
| `figma/social-thought-leadership/` | 2 | samsara-cycle (1), testimonial-post (1) | Concept posts and testimonial post |
| `figma/web-animation/` | 1 | home-integration-diagram (1) | Website integration diagram storyboard |

## Using `figma/index.json`

Each entry describes one frame:

```json
{
  "id": "3:117207",
  "name": "Digital Bank & Finance Santiago",
  "figma_page": "Static Designs (Socials or Marketing Assets)",
  "figma_section": "Digital Bank & Finance Santiago",
  "category": "social-events",
  "group": "event-thumbnails-2025-26",
  "file": "references/figma/social-events/event-thumbnails-2025-26--digital-bank-finance-santiago--3-117207.jpg",
  "size": [1200, 627],
  "background": ["#161411"],
  "fonts": ["Satoshi", "Inter"],
  "headline_text": ["Digital Bank & Finance  Santiago", "Join Us in Santiago!"],
  "top_fills": ["#fbf9f6", "#e2ded7", "#161411"],
  "uses_photo": true,
  "uses_grain": false
}
```

`id` is the Figma node id, `size` the native canvas in px, `category` the folder and `group` the file-name prefix.

Typical lookups: filter by `category` / `group` for a format, by `size` for a canvas, by `uses_photo` to find photo-led layouts, or search `headline_text` for a campaign.

File names follow `<group>--<frame-name>--<node-id>.jpg`, so a folder listing is already browsable.

## Notes

- Images are downscaled JPEGs (max 1400px; wide boards up to 2600px) for reference only, not production assets.
- People and customer names in references are real campaign content; do not reuse names, portraits, quotes or statistics in new work unless the user supplies them.
- Third-party logos inside references belong to their owners.
