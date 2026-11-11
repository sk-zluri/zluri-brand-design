import json, base64, os, time, sys
SP = r"<SCRATCH_DIR>"
IMG = os.path.join(SP, "figma_img"); DAT = os.path.join(SP, "figma_data")
os.makedirs(IMG, exist_ok=True); os.makedirs(DAT, exist_ok=True)
LOG = open(os.path.join(SP, "export.log"), "a", encoding="utf8")

def fj(expr, t=170):
    r = cdp("Runtime.evaluate", _response_timeout=t, expression=expr, returnByValue=True, awaitPromise=True)
    if 'exceptionDetails' in r:
        raise RuntimeError(str(r['exceptionDetails'])[:600])
    return r['result'].get('value')

SETUP = r"""
window.__zx = {
 hex(c){const h=v=>Math.round(v*255).toString(16).padStart(2,'0');return '#'+h(c.r)+h(c.g)+h(c.b);},
 paint(p){
   if(!p||p.visible===false) return null;
   if(p.type==='SOLID') return {t:'solid',c:this.hex(p.color),o:+(p.opacity??1).toFixed(2)};
   if(p.type&&p.type.startsWith('GRADIENT')) return {t:p.type.replace('GRADIENT_','grad-').toLowerCase(),o:+(p.opacity??1).toFixed(2),stops:p.gradientStops.map(s=>({c:this.hex(s.color),a:+s.color.a.toFixed(2),p:+s.position.toFixed(2)})),tf:p.gradientTransform.map(r=>r.map(v=>+v.toFixed(2)))};
   if(p.type==='IMAGE') return {t:'image',o:+(p.opacity??1).toFixed(2),mode:p.scaleMode,hash:(p.imageHash||'').slice(0,10)};
   return {t:p.type};
 },
 async data(id){
   const root=await figma.getNodeByIdAsync(id);
   const rb=root.absoluteBoundingBox||{x:0,y:0};
   const res={id,name:root.name,type:root.type,w:Math.round(root.width),h:Math.round(root.height),texts:[],fills:{},strokes:{},grads:[],radii:{},effects:[],images:[],layers:[],nodeCount:0,types:{},blends:{},opac:{}};
   if('fills' in root && Array.isArray(root.fills)) res.bg=root.fills.map(p=>this.paint(p)).filter(Boolean);
   if('layoutMode' in root) res.layout={mode:root.layoutMode,pad:[root.paddingTop,root.paddingRight,root.paddingBottom,root.paddingLeft],gap:root.itemSpacing};
   if('children' in root) res.layers=root.children.map(c=>({n:c.name,t:c.type,w:Math.round(c.width),h:Math.round(c.height),x:Math.round(c.x),y:Math.round(c.y),v:c.visible}));
   const stack=[root]; let cnt=0; const CAP=6000;
   const rel=n=>{const b=n.absoluteBoundingBox; return b?[Math.round(b.x-rb.x),Math.round(b.y-rb.y),Math.round(b.width),Math.round(b.height)]:null;};
   while(stack.length&&cnt<CAP){
     const n=stack.pop(); if(n.visible===false) continue; cnt++;
     res.types[n.type]=(res.types[n.type]||0)+1;
     if('blendMode' in n && n.blendMode!=='PASS_THROUGH' && n.blendMode!=='NORMAL') res.blends[n.blendMode]=(res.blends[n.blendMode]||0)+1;
     if('opacity' in n && n.opacity<1){const k=n.opacity.toFixed(2);res.opac[k]=(res.opac[k]||0)+1;}
     if(n.type==='TEXT'){
       let segs=[];
       try{ segs=n.getStyledTextSegments(['fontName','fontSize','fills','letterSpacing','lineHeight','textCase','textDecoration']).map(s=>({ch:s.characters.slice(0,400),ff:s.fontName.family,fs:s.fontName.style,sz:+s.fontSize.toFixed(1),col:(s.fills||[]).map(p=>this.paint(p)).filter(Boolean),ls:s.letterSpacing&&s.letterSpacing.value?{v:+s.letterSpacing.value.toFixed(2),u:s.letterSpacing.unit}:0,lh:s.lineHeight&&s.lineHeight.unit!=='AUTO'?{v:+s.lineHeight.value.toFixed(1),u:s.lineHeight.unit}:'auto',tc:s.textCase,td:s.textDecoration})); }catch(e){ segs=[{ch:(n.characters||'').slice(0,400),err:String(e).slice(0,80)}]; }
       res.texts.push({box:rel(n),align:n.textAlignHorizontal,auto:n.textAutoResize,op:+n.opacity.toFixed(2),segs});
     } else {
       if('fills' in n && Array.isArray(n.fills)) for(const p of n.fills){ const q=this.paint(p); if(!q) continue;
         if(q.t==='solid'){const k=q.c+(q.o<1?'@'+q.o:''); res.fills[k]=(res.fills[k]||0)+1;}
         else if(q.t==='image'){ if(res.images.length<40) res.images.push({hash:q.hash,mode:q.mode,o:q.o,box:rel(n),name:n.name.slice(0,60),blend:n.blendMode}); }
         else if(q.stops){ if(res.grads.length<40) res.grads.push({t:q.t,o:q.o,stops:q.stops,tf:q.tf,box:rel(n),name:n.name.slice(0,40),nt:n.type}); }
       }
       if('strokes' in n && Array.isArray(n.strokes) && n.strokes.length){ for(const p of n.strokes){const q=this.paint(p); if(q&&q.t==='solid'){const k=q.c+(q.o<1?'@'+q.o:'')+'|'+(typeof n.strokeWeight==='number'?+n.strokeWeight.toFixed(1):'mix'); res.strokes[k]=(res.strokes[k]||0)+1;} } }
       if('cornerRadius' in n){ const r=n.cornerRadius; if(typeof r==='number'&&r>0&&(n.type==='FRAME'||n.type==='RECTANGLE'||n.type==='INSTANCE'||n.type==='COMPONENT')){const k=Math.round(r)+'@'+Math.round(Math.min(n.width,n.height)); res.radii[k]=(res.radii[k]||0)+1;} }
     }
     if('effects' in n && n.effects.length){ for(const e of n.effects){ if(e.visible===false) continue; if(res.effects.length<30) res.effects.push({t:e.type,r:e.radius,off:e.offset,spread:e.spread,c:e.color?this.hex(e.color)+'@'+e.color.a.toFixed(2):undefined,on:n.type,name:n.name.slice(0,30),size:[Math.round(n.width),Math.round(n.height)]}); } }
     if('children' in n) for(const c of n.children) stack.push(c);
   }
   res.nodeCount=cnt; res.capped=cnt>=CAP;
   return JSON.stringify(res);
 },
 async img(id){
   const n=await figma.getNodeByIdAsync(id);
   const mx=Math.max(n.width,n.height), mn=Math.min(n.width,n.height);
   const s=(mx/mn<=2.2)?Math.min(1,1600/mx):Math.min(1,Math.max(3600/mx, 0.25), 1100/mn);
   const b=await n.exportAsync({format:'JPG',constraint:{type:'SCALE',value:s}});
   let bin=''; const CH=0x8000; for(let i=0;i<b.length;i+=CH) bin+=String.fromCharCode.apply(null,b.subarray(i,i+CH));
   return btoa(bin);
 }
};
'ok'
"""
print(fj(SETUP))
# make sure all pages are loaded
print(fj("(async()=>{for(const p of figma.root.children) await p.loadAsync(); return 'loaded'})()"))
frames = json.load(open(os.path.join(SP, "frames.json"), encoding="utf8"))
todo = [f for f in frames if f['type'] in ('FRAME','GROUP') and f['w']>=300]
print(len(todo), "frames")
for i, f in enumerate(todo):
    fid = f['id']; safe = fid.replace(':', '-')
    ip = os.path.join(IMG, safe + ".jpg"); dp = os.path.join(DAT, safe + ".json")
    t0 = time.time()
    try:
        if not os.path.exists(dp):
            d = fj("window.__zx.data(%s)" % json.dumps(fid))
            open(dp, "w", encoding="utf8").write(d)
        if not os.path.exists(ip):
            b = fj("window.__zx.img(%s)" % json.dumps(fid))
            open(ip, "wb").write(base64.b64decode(b))
        LOG.write("%d/%d OK %s %s %.1fs\n" % (i+1, len(todo), fid, f['name'][:40], time.time()-t0))
    except Exception as e:
        LOG.write("%d/%d FAIL %s %s %s\n" % (i+1, len(todo), fid, f['name'][:40], str(e)[:300]))
    LOG.flush()
print("done")
