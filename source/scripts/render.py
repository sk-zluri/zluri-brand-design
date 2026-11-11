"""Render every .artboard of the given template HTML files to JPG (run through browser-harness).
Usage:  ZR_FILES="social/event-thumbnails.html;social/product-launch.html" browser-harness < render.py
"""
import os, json, base64, urllib.parse
REPO = r"D:\Zluri Files\AI Experiments\Zluri Design System 2026\zluri-brand-design"
OUT = os.path.join(REPO, "preview", "templates"); os.makedirs(OUT, exist_ok=True)
files = [f for f in os.environ.get("ZR_FILES", "").split(";") if f]
tabs = [t for t in list_tabs() if t.get("url", "").startswith("file:///")]
if tabs: switch_tab(tabs[0]["targetId"])
else: new_tab("about:blank")
for rel in files:
    p = os.path.join(REPO, "templates", rel.replace("/", os.sep))
    url = "file:///" + urllib.parse.quote(p.replace("\\", "/"), safe="/:")
    goto_url(url); wait_for_load(20)
    cdp("Runtime.evaluate", _response_timeout=30, expression="document.fonts.ready.then(()=>new Promise(r=>setTimeout(r,900)))", awaitPromise=True)
    fonts = js("JSON.stringify([...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight))")
    boxes = json.loads(js("JSON.stringify([...document.querySelectorAll('.artboard')].map(e=>{const r=e.getBoundingClientRect();return [r.x+scrollX,r.y+scrollY,r.width,r.height]}))"))
    name = os.path.splitext(os.path.basename(rel))[0]
    for i, (x, y, w, h) in enumerate(boxes):
        sc = min(1, 1400 / max(w, h))
        r = cdp("Page.captureScreenshot", _response_timeout=60, format="jpeg", quality=86, captureBeyondViewport=True, clip={"x": x, "y": y, "width": w, "height": h, "scale": sc})
        open(os.path.join(OUT, f"{name}-{i+1}.jpg"), "wb").write(base64.b64decode(r["data"]))
    print(rel, len(boxes), "artboards; fonts:", fonts[:160])
