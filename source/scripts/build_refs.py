"""Assemble references/ in the repo: categorized, recompressed Figma exports + index; site + PDF renders."""
import json, os, re, shutil, glob
from PIL import Image
SP = os.path.dirname(os.path.abspath(__file__))
REPO = r"D:\Zluri Files\AI Experiments\Zluri Design System 2026\zluri-brand-design"
REF = os.path.join(REPO, "references")
frames = [f for f in json.load(open(os.path.join(SP, "frames.json"), encoding="utf8")) if f["type"] in ("FRAME", "GROUP") and f["w"] >= 300]

def slug(s, n=48):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return (s or "frame")[:n].strip("-")

def categorize(f):
    page, path, name, fid = f["page"], f["path"], f["name"], f["id"]
    p = path.lower(); n = name.lower()
    if page.startswith("Pitch"): return "decks-and-diagrams", "pitch-deck-diagrams"
    if page.startswith("Website"): return "web-animation", "home-integration-diagram"
    if page.startswith("Video"):
        if "wrapped" in p: return "video", "zluri-wrapped-2025"
        if "underdog" in p or "underdog" in n: return "video", "customer-testimonial-underdog"
        if "iris" in p: return "video", "iris-launch-teaser"
        if "50k" in p: return "video", "50k-followers"
        if "feature spotlight" in n or "screen recording" in n: return "video", "feature-spotlight"
        if n.startswith("frame 10000148") : return "video", "academy-ui-callouts"
        return "video", "academy-templates"
    # Static page
    if "new joinee" in p or "new joiner" in n: return "social-people", "new-joiners"
    if "employee appreciation" in p: return "social-people", "employee-spotlight"
    if "reddit" in p or fid == "1:57810": return "ads", "reddit-google-workspace"
    car = {"gbar carousel": "carousel-gbar-dark-panels", "access visibility gap": "carousel-access-visibility-gap", "halloween": "carousel-halloween-illustrated",
           "narvar": "carousel-customer-spotlight-narvar", "radicle": "carousel-customer-spotlight-radicle", "carousel cybersecurity": "carousel-security-news",
           "carousel - zluri 2.0": "carousel-zluri-2-0-light"}
    for k, v in car.items():
        if k in p: return "social-carousels", v
    if fid == "3:67800": return "social-carousels", "carousel-access-visibility-gap"
    fest = ["thanksgiving", "data privacy", "christmas", "new year", "labour", "diwali", "veterans"]
    if any(k in p for k in fest) or "4th of july" in n or fid == "3:57513": return "social-festive", "greetings"
    if "samsara" in p: return "social-thought-leadership", "samsara-cycle"
    if fid in ("3:115184",): return "social-thought-leadership", "testimonial-post"
    if "z color overlay" in p:
        if fid in ("3:55422",): return "social-people", "new-joiners"
        if fid == "3:57614": return "print-and-posters", "standee"
        if fid in ("3:44266", "3:44547"): return "brand-backgrounds", "recognition-banners"
        return "social-events", "z-overlay-invites"
    if "background options" in p or p in ("patterns",): return "brand-backgrounds", "recognition-banners"
    if p == "pattern": return "social-events", "navy-pattern-invites"
    if "ascend alliance" in p: return "social-product-launch", "ascend-alliance"
    if "iris - blog" in p: return "social-product-launch", "iris-launch"
    if fid in ("3:118225", "3:118370", "3:118678", "3:118950", "3:120081"): return "social-product-launch", "product-announcements"
    ev_paths = ["event thumbnails", "santiago", "f1 event", "argentina", "aws reinvent", "guidepoint", "sko", "section 1"]
    if any(k in p for k in ev_paths): return "social-events", "event-thumbnails-2025-26"
    if any(k in n for k in ["oktane", "grc conference", "identity week", "mindthesec"]):
        if "email" in n: return "banners-and-email", "event-email"
        return "social-events", "event-posts-2025"
    if fid in ("4:120995", "4:121053", "4:121193", "4:121242", "4:121283"):
        return ("banners-and-email", "event-email") if fid == "4:121283" else ("social-events", "zluriverse-and-elevate-2024")
    if fid in ("4:121332", "5:121434", "5:131196"): return "print-and-posters", "posh-internal-posters"
    if "new branding" in p or "20th mar" in p or "g2 banner" in p or fid in ("5:131851", "5:131876", "5:131915"): return "banners-and-email", "profile-banners-and-email"
    if fid in ("7:3229", "7:3284", "7:3293"): return "banners-and-email", "website-announcement-bars"
    if fid in ("8:52879", "8:53016", "3:49080"): return "brand-boards", "palette-and-type"
    return "uncategorized", "misc"

os.makedirs(REF, exist_ok=True)
index = []; seen = set()
for f in frames:
    cat, sub = categorize(f)
    src = os.path.join(SP, "figma_img", f["id"].replace(":", "-") + ".jpg")
    if not os.path.exists(src): continue
    d = json.load(open(os.path.join(SP, "figma_data", f["id"].replace(":", "-") + ".json"), encoding="utf8"))
    base = f"{slug(sub, 40)}--{slug(f['name'], 36)}--{f['id'].replace(':', '-')}"
    rel = f"references/figma/{cat}/{base}.jpg"
    dst = os.path.join(REPO, rel.replace("/", os.sep)); os.makedirs(os.path.dirname(dst), exist_ok=True)
    im = Image.open(src).convert("RGB")
    mx = 1400 if max(im.size) / min(im.size) <= 2.2 else 2600
    im.thumbnail((mx, mx)); im.save(dst, quality=80, optimize=True)
    fonts = {}
    for t in d["texts"]:
        for s in t["segs"]:
            if "ff" in s: fonts[s["ff"].replace(" Variable", "")] = fonts.get(s["ff"].replace(" Variable", ""), 0) + len(s["ch"])
    texts = []
    for t in sorted(d["texts"], key=lambda t: -(max((s.get("sz", 0) for s in t["segs"]), default=0))):
        txt = " ".join(s["ch"] for s in t["segs"]).strip().replace("\n", " / ")
        if len(txt) > 2 and txt not in texts: texts.append(txt[:120])
        if len(texts) >= 4: break
    tops = [k.split("@")[0] for k, _ in sorted(d["fills"].items(), key=lambda kv: -kv[1]) if k.split("@")[0] not in ("#57e1ff", "#d3ff57", "#ff5757", "#1c1c1f")][:6]
    bg = [(b.get("c") or b["t"]) for b in (d.get("bg") or [])]
    index.append({"id": f["id"], "name": f["name"], "figma_page": f["page"], "figma_section": f["path"], "category": cat, "group": sub, "file": rel,
                  "size": [f["w"], f["h"]], "background": bg, "fonts": sorted(fonts, key=lambda k: -fonts[k])[:4], "headline_text": texts,
                  "top_fills": tops, "uses_photo": any(i["box"] and i["box"][2] > f["w"] * 0.25 for i in d["images"]), "uses_grain": any(e["t"] == "NOISE" for e in d["effects"])})
json.dump({"source": "Figma: Zluri Marketing Brand Design System (file key ZR8Sn0KI7ttIHfyWmPXZoI)", "count": len(index), "frames": index},
          open(os.path.join(REF, "figma", "index.json"), "w", encoding="utf8"), indent=1, ensure_ascii=False)
from collections import Counter
print(Counter((i["category"], i["group"]) for i in index))

# website screenshots
os.makedirs(os.path.join(REF, "website", "full-pages"), exist_ok=True)
site = []
for p in sorted(glob.glob(os.path.join(SP, "site", "*.jpg"))):
    s = os.path.basename(p)[:-4]; im = Image.open(p).convert("RGB")
    w = 1100; im = im.resize((w, int(im.height * w / im.width)))
    if im.height > 12000: im = im.crop((0, 0, w, 12000))
    im.save(os.path.join(REF, "website", "full-pages", s + ".jpg"), quality=72, optimize=True)
    j = json.load(open(p[:-4] + ".json", encoding="utf8"))
    site.append({"slug": s, "url": j["url"], "title": j["title"], "file": f"references/website/full-pages/{s}.jpg",
                 "sections": [{"class": x["cls"].split(" ")[0], "bg": x["bg"], "h": x["box"]["h"], "headings": [h["t"] for h in x["heads"][:3]]} for x in j["sections"][:24]]})
json.dump({"crawled": "2026-11-11", "viewport": [1920, 1023], "note": "Full-page captures miss viewport-triggered animations; see live/ for in-viewport captures.", "pages": site},
          open(os.path.join(REF, "website", "index.json"), "w", encoding="utf8"), indent=1, ensure_ascii=False)
os.makedirs(os.path.join(REF, "website", "live"), exist_ok=True)
live = {"home_hero_a": "home-hero-cursor-state-a", "home_hero_b": "home-hero-cursor-state-b", "h00": "home-challenge-slider", "h01": "home-iris-layer-stack", "found_1": "home-iris-layer-hover-relationship-graph",
        "found_3": "home-iris-layer-hover-aggregation", "h03": "home-venn-ivip-iga-ispm", "h04": "home-capabilities-ivip", "h05": "home-capabilities-iga", "h06": "home-capabilities-ispm", "h07": "home-uic-light-rays-band", "h08": "home-footer",
        "ivip_0": "ivip-hero-contextual-ui", "ivip_2": "ivip-feature-row", "ivip_4": "ivip-feature-row-2", "nhi_0": "nhi-hero-icon-field", "nhi_1": "nhi-problem-cards", "uic_0": "uic-hero-light-rays", "uic_3": "uic-pinned-connector-scene",
        "ai_0": "state-of-ai-hero", "ai_1": "state-of-ai-stats", "ai_2": "state-of-ai-highlight-quotes", "ai_3": "state-of-ai-leaderboard", "story_0": "our-story-hero", "story_1": "our-story-body", "ispm_0": "ispm-hero-contextual-ui",
        "ispm_1": "ispm-problem-grid", "cs_0": "customer-stories-hero", "blog_0": "blog-index", "demo_0": "get-demo-form"}
for k, v in live.items():
    p = os.path.join(SP, "live", k + ".jpg")
    if os.path.exists(p):
        im = Image.open(p).convert("RGB"); im.thumbnail((1400, 1400)); im.save(os.path.join(REF, "website", "live", v + ".jpg"), quality=78, optimize=True)
# brand guideline pages
os.makedirs(os.path.join(REF, "brand-guidelines-pdf"), exist_ok=True)
for p in sorted(glob.glob(os.path.join(SP, "pdf", "p*.jpg"))):
    shutil.copy(p, os.path.join(REF, "brand-guidelines-pdf", "page-" + os.path.basename(p)[1:]))
shutil.copy(os.path.join(SP, "pdf", "text.txt"), os.path.join(REF, "brand-guidelines-pdf", "extracted-text.txt"))
tot = sum(os.path.getsize(os.path.join(dp, fn)) for dp, _, fns in os.walk(REF) for fn in fns)
print("references MB", round(tot / 1e6, 1))
