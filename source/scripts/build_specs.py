"""Write trimmed per-frame layout specs into references/figma/specs/ and link them from index.json."""
import json, os, glob
SP = "<SCRATCH_DIR>"
REPO = "<REPO_DIR>"
OUT = REPO + "/references/figma/specs"; os.makedirs(OUT, exist_ok=True)
idx = json.load(open(REPO + "/references/figma/index.json", encoding="utf8"))
UI_FONTS = {"Sora", "Pixel Arial 11", "W95FA", "Dogica", "Roboto", "Lexend"}
tot = 0
for e in idx["frames"]:
    fid = e["id"].replace(":", "-")
    d = json.load(open(f"{SP}/figma_data/{fid}.json", encoding="utf8"))
    texts = []
    for t in d["texts"]:
        runs = []
        for s in t["segs"]:
            if "ff" not in s: continue
            col = [(c.get("c") or {"gradient": [x["c"] for x in c.get("stops", [])]}) for c in s["col"]]
            run = {"text": s["ch"][:160], "font": s["ff"].replace(" Variable", ""), "style": s["fs"], "size": s["sz"], "color": col[0] if len(col) == 1 else col}
            if s["ls"]: run["tracking"] = f"{s['ls']['v']}{'%' if s['ls']['u'] == 'PERCENT' else 'px'}"
            if s["lh"] != "auto": run["lineHeight"] = f"{s['lh']['v']}{'%' if s['lh']['u'] == 'PERCENT' else 'px'}"
            if s.get("tc") and s["tc"] != "ORIGINAL": run["case"] = s["tc"].lower()
            runs.append(run)
        if not runs or not t["box"]: continue
        texts.append({"box_xywh": t["box"], "align": t["align"].lower(), "runs": runs, "_ui": all(r["font"] in UI_FONTS for r in runs), "_max": max(r["size"] for r in runs)})
    brand = [t for t in texts if not t["_ui"]]; ui = [t for t in texts if t["_ui"]]
    brand.sort(key=lambda t: (t["box_xywh"][1], t["box_xywh"][0]))
    if len(brand) > 45: brand = sorted(sorted(brand, key=lambda t: -t["_max"])[:45], key=lambda t: (t["box_xywh"][1], t["box_xywh"][0]))
    for t in brand: t.pop("_ui"); t.pop("_max")
    spec = {"id": e["id"], "name": e["name"], "image": e["file"], "canvas": {"width": d["w"], "height": d["h"], "background": d.get("bg") and [(b.get("c") or {"type": b["t"], "stops": [s["c"] for s in b.get("stops", [])]}) for b in d["bg"]]},
            "text": brand, "product_ui_text_nodes_omitted": len(ui),
            "solid_fills_by_node_count": dict(sorted(d["fills"].items(), key=lambda kv: -kv[1])[:14]),
            "strokes_color_weight": dict(sorted(d["strokes"].items(), key=lambda kv: -kv[1])[:8]),
            "corner_radii_at_min_side": dict(sorted(d["radii"].items(), key=lambda kv: -kv[1])[:10]),
            "gradients": [{"type": g["t"], "stops": [{"color": s["c"], "alpha": s["a"], "pos": s["p"]} for s in g["stops"]], "box_xywh": g["box"], "on": g["nt"]} for g in d["grads"][:8]],
            "effects": [{"type": x["t"], "radius": x.get("r"), "color": x.get("c"), "node_size": x["size"]} for x in d["effects"][:8]],
            "images": [{"box_xywh": i["box"], "blend": i["blend"], "scale": i["mode"]} for i in d["images"][:10] if i["box"]],
            "blend_modes": d["blends"], "top_level_layers": [{"name": l["n"], "type": l["t"], "box_xywh": [l["x"], l["y"], l["w"], l["h"]]} for l in d["layers"][:16] if l.get("v", True)]}
    p = f"{OUT}/{fid}.json"
    json.dump(spec, open(p, "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
    tot += os.path.getsize(p); e["spec"] = f"references/figma/specs/{fid}.json"
json.dump(idx, open(REPO + "/references/figma/index.json", "w", encoding="utf8"), indent=1, ensure_ascii=False)
print("specs", len(idx["frames"]), "MB", round(tot / 1e6, 2))
