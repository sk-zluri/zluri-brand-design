import json, os, time, re, base64, io
from PIL import Image
SP = r"<SCRATCH_DIR>"
OUT = os.path.join(SP, "site"); os.makedirs(OUT, exist_ok=True)
LOG = open(os.path.join(SP, "crawl.log"), "a", encoding="utf8")
B = "https://www.zluri.com"
PAGES = [
 ("home", "/"),
 ("product-ivip", "/products/identity-visibility-and-intelligence"),
 ("product-nhi", "/identity-visibility-for-non-human-identities"),
 ("product-access-management", "/access-management"),
 ("product-access-requests", "/solutions/access-requests"),
 ("product-access-reviews", "/access-reviews"),
 ("product-sod", "/products/segregation-of-duties"),
 ("product-ispm", "/products/identity-security-posture-management"),
 ("product-smp", "/saas-management"),
 ("platform-iris", "/products/identity-risk-intelligence-system"),
 ("platform-uic", "/products/universal-identity-connector"),
 ("solution-identity-app-visibility", "/solutions/identity-and-application-visibility"),
 ("solution-shadow-it", "/solutions/monitor-shadow-it"),
 ("solution-ai-apps", "/solutions/monitor-ai-apps"),
 ("solution-lifecycle", "/solutions/identity-lifecycle-management"),
 ("regulation-soc2", "/soc"),
 ("regulation-iso27001", "/iso"),
 ("regulation-hipaa", "/hipaa"),
 ("regulation-sox-itgc", "/sox-itgc"),
 ("regulation-pci-dss", "/pci-dss"),
 ("okta-alt-google-workspace", "/okta-alternative/zluri-google-workspace"),
 ("why-customer-stories", "/case-studies"),
 ("why-product-tours", "/product-tours"),
 ("why-roi-calculator", "/return-on-investment-calculator"),
 ("partners-overview", "/partners"),
 ("partners-register-deal", "/partners/activate-a-deal"),
 ("partners-portal", "/partners/partner-portal"),
 ("company-our-story", "/our-story"),
 ("company-security", "/security"),
 ("company-careers", "/careers"),
 ("company-events", "/events"),
 ("company-contact", "/contact-us"),
 ("resources-state-of-ai", "/state-of-ai-in-the-workplace-2025-report"),
 ("resources-blog", "/blog"),
 ("resources-whitepapers", "/whitepapers"),
 ("resources-webinars", "/webinars"),
 ("resources-eye-on-identity", "/eye-on-identity"),
 ("resources-academy", "/registration-form"),
 ("get-demo", "/get-demo"),
]

EXTRACT = r"""
(()=>{
 const vis=e=>{const r=e.getBoundingClientRect();const s=getComputedStyle(e);return r.width>1&&r.height>1&&s.visibility!=='hidden'&&s.display!=='none'&&parseFloat(s.opacity)>0.05;};
 const fnt=e=>{const s=getComputedStyle(e);return {ff:s.fontFamily.split(',')[0].replace(/["']/g,''),sz:parseFloat(s.fontSize),w:s.fontWeight,lh:s.lineHeight,ls:s.letterSpacing,c:s.color,tt:s.textTransform,ta:s.textAlign};};
 const txt=e=>(e.innerText||'').trim().replace(/\s+/g,' ');
 const sy=window.scrollY;
 const abs=e=>{const r=e.getBoundingClientRect();return {x:Math.round(r.x),y:Math.round(r.y+sy),w:Math.round(r.width),h:Math.round(r.height)};};
 const out={url:location.href,title:document.title,desc:(document.querySelector('meta[name=description]')||{}).content||'',docH:document.documentElement.scrollHeight,vw:innerWidth};
 // section candidates: walk down from body through single-child wrappers
 let secs=[...document.querySelectorAll('section, header, footer, [class*=section]')].filter(e=>vis(e)&&e.getBoundingClientRect().height>80&&e.getBoundingClientRect().width>innerWidth*0.7);
 secs=secs.filter(e=>!secs.some(o=>o!==e&&o.contains(e)&&o.getBoundingClientRect().height<e.getBoundingClientRect().height*1.6&&o.tagName!=='BODY'&&!/page-wrapper|main-wrapper/.test(o.className)) );
 out.sections=secs.slice(0,60).map(e=>{
   const s=getComputedStyle(e);
   const heads=[...e.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(vis).slice(0,14).map(h=>({tag:h.tagName,cls:(h.className||'').toString().slice(0,60),t:txt(h).slice(0,160),...fnt(h),box:abs(h)}));
   const paras=[...e.querySelectorAll('p, .text-size-medium, .text-size-large, .text-size-regular, li')].filter(p=>vis(p)&&txt(p).length>20).slice(0,8).map(p=>({cls:(p.className||'').toString().slice(0,50),t:txt(p).slice(0,220),...fnt(p),maxw:Math.round(p.getBoundingClientRect().width)}));
   const btns=[...e.querySelectorAll('a.button, a[class*=button], a[class*=btn], button, .w-button, input[type=submit]')].filter(vis).slice(0,8).map(b=>{const c=getComputedStyle(b);return {cls:(b.className||'').toString().slice(0,70),t:txt(b).slice(0,50)||b.value,bg:c.backgroundColor,bgi:c.backgroundImage.slice(0,120),col:c.color,rad:c.borderRadius,pad:c.padding,bor:c.border,ff:c.fontFamily.split(',')[0],sz:c.fontSize,w:c.fontWeight,h:Math.round(b.getBoundingClientRect().height),sh:c.boxShadow.slice(0,100)};});
   const imgs=[...e.querySelectorAll('img, video, svg, lottie-player, [data-animation-type], canvas')].filter(i=>vis(i)&&i.getBoundingClientRect().width>60).slice(0,16).map(i=>({tag:i.tagName,src:(i.currentSrc||i.src||i.getAttribute('data-src')||'').toString().slice(0,200),alt:(i.alt||'').slice(0,80),cls:(i.className&&i.className.baseVal!==undefined?i.className.baseVal:i.className||'').toString().slice(0,50),box:abs(i),rad:getComputedStyle(i).borderRadius}));
   // cards: elements with bg/border/radius within section
   const cards=[]; const seen=new Set();
   for(const c of e.querySelectorAll('div, a, li')){ if(cards.length>=10) break; const cs=getComputedStyle(c); const r=c.getBoundingClientRect(); if(r.width<140||r.height<70||r.width>innerWidth*0.96) continue; const hasBg=cs.backgroundColor!=='rgba(0, 0, 0, 0)'&&cs.backgroundColor!==s.backgroundColor; const hasBor=parseFloat(cs.borderTopWidth)>0&&cs.borderTopStyle!=='none'; const rad=parseFloat(cs.borderTopLeftRadius)>0; if(!((hasBg||hasBor)&&rad)&&cs.boxShadow==='none') continue; if(!vis(c)) continue; const key=(c.className||'').toString(); if(seen.has(key)) continue; seen.add(key); cards.push({cls:key.slice(0,70),n:e.querySelectorAll('.'+CSS.escape((key.split(' ')[0]||'x'))).length,w:Math.round(r.width),h:Math.round(r.height),bg:cs.backgroundColor,bgi:cs.backgroundImage.slice(0,140),bor:cs.borderTopWidth+' '+cs.borderTopStyle+' '+cs.borderTopColor,rad:cs.borderRadius,sh:cs.boxShadow.slice(0,120),pad:cs.padding,bf:cs.backdropFilter}); }
   // layout of inner container
   const cont=e.querySelector('[class*=container], [class*=padding-global], .w-layout-grid')||e;
   const grids=[...e.querySelectorAll('*')].filter(g=>{const d=getComputedStyle(g).display;return (d==='grid'||d==='flex')&&g.children.length>1&&g.getBoundingClientRect().width>innerWidth*0.4&&vis(g);}).slice(0,5).map(g=>{const c=getComputedStyle(g);return {cls:(g.className||'').toString().slice(0,60),d:c.display,cols:c.gridTemplateColumns.slice(0,90),gap:c.gap,dir:c.flexDirection,n:g.children.length,w:Math.round(g.getBoundingClientRect().width),ai:c.alignItems,jc:c.justifyContent};});
   return {tag:e.tagName,cls:(e.className||'').toString().slice(0,90),id:e.id,box:abs(e),bg:s.backgroundColor,bgi:s.backgroundImage.slice(0,200),pt:s.paddingTop,pb:s.paddingBottom,col:s.color,contW:Math.round(cont.getBoundingClientRect().width),contMax:getComputedStyle(cont).maxWidth,text:txt(e).slice(0,900),heads,paras,btns,imgs,cards,grids};
 });
 // typography census
 const tc={}; const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
 let n; while(n=walker.nextNode()){ const t=n.nodeValue.trim(); if(t.length<2) continue; const p=n.parentElement; if(!p||!vis(p)) continue; const f=fnt(p); const k=[f.ff,f.sz,f.w,f.lh,f.ls,f.c,f.tt].join('|'); if(!tc[k]) tc[k]={n:0,ch:0,ex:t.slice(0,60),tag:p.tagName}; tc[k].n++; tc[k].ch+=t.length; }
 out.type=Object.entries(tc).sort((a,b)=>b[1].ch-a[1].ch).slice(0,45).map(([k,v])=>({k,...v}));
 const rad={},sh={},bg={},bor={};
 for(const e of document.querySelectorAll('body *')){ const r=e.getBoundingClientRect(); if(r.width<24||r.height<16) continue; const s=getComputedStyle(e); if(s.display==='none'||s.visibility==='hidden') continue;
   if(parseFloat(s.borderTopLeftRadius)>0){rad[s.borderRadius]=(rad[s.borderRadius]||0)+1;}
   if(s.boxShadow!=='none'){sh[s.boxShadow]=(sh[s.boxShadow]||0)+1;}
   if(s.backgroundColor!=='rgba(0, 0, 0, 0)'){bg[s.backgroundColor]=(bg[s.backgroundColor]||0)+1;}
   if(s.backgroundImage!=='none'&&s.backgroundImage.includes('gradient')){const k='G:'+s.backgroundImage.slice(0,160);bg[k]=(bg[k]||0)+1;}
   if(parseFloat(s.borderTopWidth)>0&&s.borderTopStyle!=='none'){const k=s.borderTopWidth+' '+s.borderTopColor;bor[k]=(bor[k]||0)+1;}
 }
 const top=(o,k)=>Object.entries(o).sort((a,b)=>b[1]-a[1]).slice(0,k);
 out.rad=top(rad,16);out.sh=top(sh,12);out.bg=top(bg,24);out.bor=top(bor,12);
 return JSON.stringify(out);
})()
"""

def shot_full(path):
    r = cdp("Page.captureScreenshot", _response_timeout=90, format="jpeg", quality=82, captureBeyondViewport=True)
    open(path, "wb").write(base64.b64decode(r["data"]))

def shot_stitched(path, total_h, vh):
    tiles = []; y = 0
    while y < total_h and len(tiles) < 30:
        js("window.scrollTo(0,%d)" % y); wait(0.5)
        r = cdp("Page.captureScreenshot", _response_timeout=40, format="jpeg", quality=82)
        im = Image.open(io.BytesIO(base64.b64decode(r["data"]))).convert("RGB")
        ay = js("window.scrollY")
        tiles.append((ay, im)); y += vh - 110
    W = tiles[0][1].width
    S = Image.new("RGB", (W, int(min(total_h, tiles[-1][0] + tiles[-1][1].height))), "#fff")
    for ay, im in tiles: S.paste(im, (0, int(ay)))
    S.save(path, quality=82)

for slug, path in PAGES:
    jp = os.path.join(OUT, slug + ".json"); ip = os.path.join(OUT, slug + ".jpg")
    if os.path.exists(jp) and os.path.exists(ip): continue
    t0 = time.time()
    try:
        goto_url(B + path); wait_for_load(30); wait(2.5)
        # dismiss cookie banners if present
        js("""(()=>{for(const b of document.querySelectorAll('button, a')){const t=(b.innerText||'').trim().toLowerCase(); if(/^(accept|accept all|allow all|got it|i agree|agree)$/.test(t)){b.click();return t}}return 'none'})()""")
        H = js("document.documentElement.scrollHeight"); vh = js("innerHeight")
        y = 0
        while y < H and y < 40000:
            js("window.scrollTo(0,%d)" % y); wait(0.3); y += 700
            H = js("document.documentElement.scrollHeight")
        wait(0.6); js("window.scrollTo(0,0)"); wait(1.0)
        data = js(EXTRACT)
        open(jp, "w", encoding="utf8").write(data)
        H = js("document.documentElement.scrollHeight")
        try:
            if H > 16000: raise RuntimeError("too tall for single capture")
            shot_full(ip)
        except Exception as e:
            LOG.write("  full capture fallback for %s: %s\n" % (slug, str(e)[:120])); shot_stitched(ip, min(H, 30000), vh)
        LOG.write("OK %s H=%s %.1fs\n" % (slug, H, time.time() - t0))
    except Exception as e:
        LOG.write("FAIL %s %s\n" % (slug, str(e)[:300]))
    LOG.flush()
print("crawl done")
