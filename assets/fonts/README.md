# Fonts

Zluri uses two typefaces.

| Family | Role | Weights used | Source | Licence |
| --- | --- | --- | --- | --- |
| **Satoshi** (Indian Type Foundry) | Headlines, display | 300, 400, 500 (700 rarely) | https://www.fontshare.com/fonts/satoshi | Fontshare / ITF Free Font License. Free for commercial use; check the licence before redistributing the files. They are not stored in this repository. |
| **Inter** (Rasmus Andersson) | Body, UI, labels | 300, 400, 500, 600 | https://fonts.google.com/specimen/Inter | SIL Open Font License 1.1 |

## Loading on the web

```html
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

```css
--font-display: "Satoshi", "Satoshi Variable", "General Sans", "Inter", system-ui, sans-serif;
--font-body:    "Inter", system-ui, sans-serif;
```

zluri.com self-hosts Satoshi (OTF) and Inter 18pt (WOFF2).

## Desktop and design tools

Download Satoshi from Fontshare and Inter from Google Fonts and install them locally. In Figma the designers use **Satoshi Variable** and **Inter**.

## If a font fails to load

Do not ship. A fallback sans changes the character of every headline. Check the network request, or install the fonts locally and retry.
