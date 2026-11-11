"""Build labelled contact sheets from exported Figma frames, grouped by page/section."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
SP = os.path.dirname(os.path.abspath(__file__))
frames = json.load(open(os.path.join(SP, 'frames.json'), encoding='utf8'))
OUT = os.path.join(SP, 'sheets'); os.makedirs(OUT, exist_ok=True)
try: FONT = ImageFont.truetype('arial.ttf', 20)
except Exception: FONT = ImageFont.load_default()

def tile(f, tw, th):
    p = os.path.join(SP, 'figma_img', f['id'].replace(':', '-') + '.jpg')
    if not os.path.exists(p): return None
    im = Image.open(p).convert('RGB'); im.thumbnail((tw, th))
    T = Image.new('RGB', (tw, th + 26), '#ff00ff')
    T.paste(im, ((tw - im.width) // 2, 26 + (th - im.height) // 2))
    d = ImageDraw.Draw(T); d.rectangle([0, 0, tw, 25], fill='#000')
    d.text((4, 2), f"{f['id']} {f['name'][:int(tw/11)-8]}", fill='#fff', font=FONT)
    return T

def sheet(name, items, cols, tw, th):
    tiles = [t for t in (tile(f, tw, th) for f in items) if t]
    if not tiles: return
    rows = (len(tiles) + cols - 1) // cols
    S = Image.new('RGB', (cols * tw + (cols - 1) * 6, rows * (th + 26) + (rows - 1) * 6), '#ff00ff')
    for k, t in enumerate(tiles):
        S.paste(t, ((k % cols) * (tw + 6), (k // cols) * (th + 32)))
    S.save(os.path.join(OUT, name + '.jpg'), quality=82)
    print(name, len(tiles), S.size)

if __name__ == '__main__':
    spec = json.load(open(sys.argv[1], encoding='utf8'))
    byid = {f['id']: f for f in frames}
    for s in spec:
        sheet(s['name'], [byid[i] for i in s['ids'] if i in byid], s.get('cols', 3), s.get('tw', 660), s.get('th', 660))
