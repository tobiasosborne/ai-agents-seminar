# Deck integration spec: Magdeburg talk (talk.html)

File: `/home/tobias/Projects/ai-agents-seminar/Magdeburg-talk-2026/slides-web/talk.html` (3225 lines, 3.4 MB, almost all of it base64 PNGs). 64 `<section class="slide">` elements. **Facts that differ from the brief:** there is **no d3 and no gsap anywhere** (grep hits are base64 noise). All interactives are hand-written vanilla JS with `document.createElementNS` SVG helpers, `requestAnimationFrame`, `MutationObserver`. There are **no network requests** (no `@font-face`, no CDN, no `@import`; the only `http` hrefs are two clickable links on s-whoami-b). The deck runs fully offline, fonts are the system stack. The slide source order in the DOM is the deck order; there is no slide manifest.

Slide variant counts (`grep -oE 'class="slide[^"]*"' | sort | uniq -c`): 36 plain `slide`, 10 `statement`, 6 `divider`, 6 `center fullbleed`, 5 `gfig`, 1 `title`.

## 1. CSS design system

### 1.1 Tokens, stage, slide, build (verbatim)

```css
/*  Whitney Teal palette                                         */
/* ============================================================= */
:root{
  --black:#111417;
  --white:#ffffff;
  --darkteal:#335B74;
  --lightgrey:#DFE3E5;
  --cyan:#1CADE4;
  --medblue:#2683C6;
  --brightcyan:#27CED7;
  --green:#42BA97;
  --paper:#ffffff;
  --ink:#1a1e21;
  --muted:#5b6b74;
  --codebg:#F0F2F3;
  --stagew:1280;
  --stageh:720;
}
```

```css
*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;}
body{
  background:#0c1114;
  color:var(--ink);
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
  text-rendering:optimizeLegibility;
  overflow:hidden;
}

/* ---- letterboxed 16:9 stage ---- */
#deck{
  position:fixed;inset:0;
  display:flex;align-items:center;justify-content:center;
  background:
    radial-gradient(120% 120% at 50% 0%, #14202a 0%, #0a0f12 70%);
}
#stage{
  position:relative;
  width:min(100vw, 177.78vh);
  height:min(56.25vw, 100vh);
  background:var(--paper);
  overflow:hidden;
  container-type:size;
  box-shadow:0 0 0 1px rgba(0,0,0,.5), 0 30px 80px rgba(0,0,0,.55);
}

/* ---- slides ---- */
.slide{
  position:absolute;inset:0;
  padding:7cqh 8cqw;
  display:flex;flex-direction:column;
  opacity:0;visibility:hidden;
  transition:opacity .38s ease;
  overflow:hidden;
}
.slide.active{opacity:1;visibility:visible;z-index:2;}

/* generic build steps */
.build{opacity:0;transform:translateY(1.4cqh);
  transition:opacity .5s ease, transform .5s ease;}
.build.shown{opacity:1;transform:none;}

```

Notes: the stage is a 16:9 container (`container-type:size`), so **`cqh` = 1% of stage height (7.2 px at 1280x720), `cqw` = 1% of width (12.8 px)**. All sizes in the deck are cqh/cqw; never use px for layout (px is fine inside SVG viewBoxes). Extra literal colours used inline: `#c0687a` (rose, "bad"/open), `#a33` (T3 red), `#9aa6ad`/`#8a969c` (grey caption/notes), `#d3eefb` (pale cyan fill), `#F2FAFE` (physics row tint), `#E8A33D` amber, `#EFD58B` pale amber, `#2e9c7c` dark green, `#b57a1c` dark amber.

### 1.2 Typography, title slide, figures, code (verbatim)

```css
/* ============================================================= */
/*  Typography                                                   */
/* ============================================================= */
h1,h2,h3{font-weight:650;line-height:1.08;color:var(--darkteal);letter-spacing:-.01em;}
.frametitle{
  font-size:4.4cqh;color:var(--darkteal);font-weight:650;
  margin-bottom:3.6cqh;line-height:1.05;
  flex:0 0 auto;
}
.frametitle .rule{
  display:block;width:9cqh;height:.5cqh;background:var(--cyan);
  margin-top:1.6cqh;border-radius:2px;
}
.body{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;}
p,li{font-size:3.15cqh;line-height:1.5;color:var(--ink);}
.muted{color:var(--muted);}
.teal{color:var(--darkteal);}
.cyan{color:var(--cyan);}
.b{font-weight:650;}
.center{align-items:center;text-align:center;justify-content:center;}
.lead{font-size:3.4cqh;line-height:1.55;}
.small{font-size:2.3cqh;}
.tiny{font-size:2.0cqh;}
.stack>*+*{margin-top:2.6cqh;}
.stack-lg>*+*{margin-top:4cqh;}

/* statement + full-bleed centered slides */
.slide.statement{justify-content:center;align-items:center;text-align:center;padding:8cqh 10cqw;}
.statement .big{font-size:6.6cqh;line-height:1.18;color:var(--darkteal);font-weight:650;}
.statement .sub{font-size:3.4cqh;font-weight:450;color:var(--darkteal);}
.statement .attr{font-size:2.5cqh;color:var(--muted);font-weight:450;}

/* section dividers */
.slide.divider{background:var(--darkteal);justify-content:center;align-items:flex-start;padding:0 10cqw;}
.divider .kicker{color:var(--brightcyan);font-size:2.6cqh;letter-spacing:.32em;
  text-transform:uppercase;font-weight:600;margin-bottom:2.4cqh;}
.divider h2{color:#fff;font-size:8cqh;line-height:1.02;}
.divider .num{position:absolute;right:8cqw;bottom:7cqh;color:rgba(255,255,255,.22);
  font-size:14cqh;font-weight:700;line-height:1;}

/* ============================================================= */
/*  Title slide                                                  */
/* ============================================================= */
.slide.title{justify-content:center;padding:8cqh 9cqw;}
.title .eyebrow{color:var(--cyan);font-size:2.5cqh;letter-spacing:.3em;
  text-transform:uppercase;font-weight:600;margin-bottom:3cqh;}
.title h1{font-size:9.5cqh;line-height:1.02;color:var(--darkteal);}
.title .subtitle{font-size:4.4cqh;color:var(--ink);font-weight:400;margin-top:1.4cqh;}
.title .meta{margin-top:6cqh;font-size:2.7cqh;color:var(--muted);line-height:1.6;}
.title .meta .who{color:var(--darkteal);font-weight:600;}
.title .accentbar{width:16cqh;height:.7cqh;background:linear-gradient(90deg,var(--darkteal),var(--cyan));
  border-radius:3px;margin:3.6cqh 0;}

/* ============================================================= */
/*  Figures                                                      */
/* ============================================================= */
.figwrap{flex:1 1 auto;display:flex;align-items:center;justify-content:center;min-height:0;}
.figwrap img{max-width:100%;max-height:100%;object-fit:contain;
  border-radius:6px;box-shadow:0 2px 18px rgba(0,0,0,.10);}
.fullbleed img{box-shadow:0 4px 26px rgba(0,0,0,.14);}
.caption{text-align:center;color:var(--muted);font-size:2.15cqh;margin-top:2cqh;line-height:1.4;}
.caption .hl{color:var(--darkteal);font-weight:650;}
.synthcap{text-align:center;color:#9aa6ad;font-size:1.95cqh;margin-top:1.4cqh;font-style:italic;}

/* ============================================================= */
/*  Code blocks                                                  */
/* ============================================================= */
.code{
  background:var(--codebg);
  border-left:.7cqh solid var(--cyan);
  border-radius:8px;
  padding:3cqh 3.4cqh;
  font-family:"SF Mono",ui-monospace,"JetBrains Mono",Menlo,Consolas,monospace;
  font-size:2.7cqh;line-height:1.62;color:#22303a;
  overflow-x:auto;white-space:pre;
  box-shadow:0 2px 14px rgba(0,0,0,.06);
}
.code .kw{color:#2683C6;font-weight:600;}
.code .fn{color:var(--darkteal);font-weight:600;}
.code .str{color:#3E8853;}
.code .cm{color:#9aa6ad;font-style:italic;}
.code .op{color:#c0687a;}

/* ============================================================= */
```

Summary scale (cqh): frametitle 4.4; `p, li` 3.15 (line-height 1.5); `.lead` 3.4; `.small` 2.3; `.tiny` 2.0; `.caption` 2.15; `.synthcap` 1.95; statement `.big` 6.6 (inline overrides 4.6 to 5.8 are common), `.sub` 3.4, `.attr` 2.5; divider `h2` 8, `.kicker` 2.6, `.num` 14; title `h1` 9.5. Dense gfig text goes down to 1.4-2.2cqh. `.stack>*+*` adds 2.6cqh gap, `.stack-lg` 4cqh.

### 1.3 Slide variants
- **`.slide`**: absolute, `padding:7cqh 8cqw`, flex column, hidden until `.active`; 0.38 s opacity fade. Standard anatomy: `<div class="frametitle">Text<span class="rule"></span></div>` then `<div class="body center stack-lg">` (flex:1, vertically centred).
- **`.statement`**: centred big text, `padding:8cqh 10cqw`; children `.stack > .big / .sub / .attr`.
- **`.divider`**: dark teal background, `<div><div class="kicker">Part One</div><h2>Title</h2></div><div class="num">1</div>`.
- **`.title`**: eyebrow, h1, `.subtitle`, `.accentbar`, `.meta`.
- **`.center.fullbleed`**: image slide. `.center` is `align-items/justify-content:center`. Pattern is `<div class="figwrap"><img src="data:image/png;base64,..."></div><div class="caption">...</div>`. Optionally a left-aligned frametitle first (`style="align-self:flex-start;text-align:left;margin-bottom:2.6cqh;"`, see s-hookB). The `.figwrap img` is `max-width/height:100%; object-fit:contain`, rounded 6px with soft shadow. Images are inlined as base64 (typically 1920x1080-ish PNGs rendered from matplotlib).
- **`.gfig`**: free-positioning canvas: `padding:0; display:block`; every child is `position:absolute` using cqh that equal design-px/7.2 (see 1.6).

### 1.4 Code block, boxes, tables, cards, captions
`.code` (above): grey `--codebg`, cyan left bar, mono, `white-space:pre`, syntax spans `.kw .fn .str .cm .op`, `.line.hot` (highlight a line: `rgba(28,173,228,.22)`). Typical use: `<div class="code" style="font-size:2.35cqh;"><span class="fn">curl</span> ... <span class="str">"..."</span></div>`.

Boxes: `.cols` (flex row, gap 5cqw; `.g3` gap 3.5cqw) with `.tbox` children (`.fill` grey, `.teal` dark, inner `.h` heading, `p` 2.5cqh, `.good` green, `.bad` rose). `.arrowlabel`, `.flowarrow` (5cqh arrow glyph). Example (s-cta):
```html
<div class="cols g3" style="width:100%;">
  <div class="tbox fill" style="text-align:center;"><div class="h">Claude Code</div><p>terminal agent</p><p class="tiny muted">anthropic</p></div>
```
Other component families (all in the first `<style>`): `.ectab/.ecrow` failure-to-countermeasure table (`.fm` right-aligned 42%, `.ar` cyan arrow, `.cm` teal; `.echead` uppercase header row); `.panels/.panel/.pcap` three-up SVG panels; `.ledger/.lrow` Lamport proof ledger (`.id .st .ju .kw .mth`, `.lkids` indent with rule, `.lgrand` dashed rose); `.spectrum/.stn` (`.fill .blue .dark`); `.checks/.citem` numbered circles (`.later`); `.timeline/.tlnode/.tlcard`; `.stat/.statrow/.yearbig/.yeardot`; sampler bars; `.cwseg` context bar; `.btn` (`.alt .ghost`) and `input[type=range]`. There are **no HTML `<table>`s**; tables are flex rows (`.ecrow`, `.lrow`, `.g-row`).

Captions: `.caption` (centred, muted, 2.15cqh, `<span class="hl">` = teal bold highlight, `<br>` for a second line); `.synthcap` for "synthetic data" disclaimers. Inside gfig use `.g-note` (italic grey 1.8cqh), `.g-src` (muted 1.8cqh source lines).

### 1.5 Result-tier chips (s-flurry), exact classes and colours
Legend row `.g-legrow` (absolute, flex, 2.0cqh muted) with `.g-badge` (8.06 x 3.06 cqh pill, 0.83cqh radius, white bold 1.81cqh, `letter-spacing:.06em`; background set **inline**):
```css
.gfig .g-badge{display:inline-flex;align-items:center;justify-content:center;
  width:8.0556cqh;height:3.0556cqh;border-radius:0.8333cqh;color:#fff;font-size:1.8056cqh;
  font-weight:700;letter-spacing:.06em;margin-right:1.25cqh;flex:0 0 auto;}
```
| Tier | background | meaning (verbatim legend) |
|---|---|---|
| T1 | `var(--green)` #42BA97 | machine-checked or officially graded |
| T1* | `var(--green)` | T1 with caveat (used on Navier-Stokes etc.) |
| T2 | `var(--medblue)` #2683C6 | arXiv: named humans read it |
| T2+ | `var(--medblue)` | refereed journal |
| T3 | `#a33` | announced only, no referee |

Legend item markup:
```html
<span style="display:flex;align-items:center;"><span class="g-badge" style="background:var(--green);">T1</span>machine-checked or officially graded</span>
```
Ledger rows (`.g-row`, absolute, `left:4.72cqh`, height set inline e.g. 4.6cqh, `.phys` variant has pale-cyan tint with cyan inset bar):
```html
<div class="g-row build gnt" data-step="1" style="top:19.6cqh;height:4.6cqh;">
  <span class="g-badge bd" style="background:var(--green);">T1</span>
  <span class="dd">Jan 2026</span>
  <span class="tt">Erd&#337;s #728: first autonomous solve, with a Lean certificate</span></div>
```
`.dd` date (2.0cqh bold teal, 13.3cqh wide), `.tt` text (2.19cqh), `.tt .sub` second line (1.8cqh muted), `.warn` rose-red. Related chip systems: s-dagx `.dx-chip` (below) and `.g-chip` (big cyan number with cyan left rule: `.n` 5.1cqh bold cyan, `.c` description) in s-extended; `.g-card` stat cards (`.nm .nu .cp`).

### 1.6 gfig geometry (the "design px" system)
`1 design px = 1/7.2 cqh` on both axes (a 1280x720 frame). So `left:5.5556cqh` = 40px. A gfig slide is: `.g-ftitle` (title at left 5.56cqh, top 5.28cqh, 4.44cqh), `.g-frule` (cyan rule), optional `.g-kick` (right-aligned grey kicker top-right), then absolutely positioned content, bottom takeaway `.g-summ` (centred, 3.33cqh bold teal, `top:83.33cqh`). Note full content width is 166.67cqh (= 1280px). `.gnt` = "no transform" (cancels `.build`'s translateY so absolute-positioned reveals do not shift). SVG overlays: `<svg class="g-ov" viewBox="0 0 1280 720">` (pointer-events none). Other gfig helpers: `.g-lab`, `.g-head`, `.g-src`, `.g-pbar`, `.g-brk`, `.g-hbar`, `.g-hout`, `.g-card`, `.g-yr`, `.g-pill`, `.g-cell`, `.g-lanelab`, `.g-qbox`, `.g-bridge`, `.g-payload`.

### 1.7 Chrome and print
`#progress` (4px cyan bar), `#counter`, `#hint`, `#help` overlay. Print: `@page{size:1280px 720px;margin:0}`, every slide becomes a page at final build state (`.build{opacity:1!important}`).

## 2. Navigation engine (verbatim, `<script>` at lines 2726-3054)

Scripts in the file: (a) lines 586-836 s-whoami-a animation IIFE (runs BEFORE the engine), (b) 888-1074 s-whoami-b, (c) 1804-1957 s-filesystem, (d) 2359-2483 s-eci (plus JSON data blocks `dxData`, `eciData`), (e) 2726-3054 **the engine + early interactives + `boot()`**, (f) 3055-3222 s-dagx explorer (runs AFTER boot).

Global lexical bindings created by the engine (usable from any later classic script): `slides` (array of `.slide` elements in DOM order), `controllers` (map id to hooks), `state` (`{current, step}`), and functions `maxStepsFor, applySteps, render, goTo, next, prev, boot`.

```js
<script>
"use strict";
/* ============================================================= */
/*  Engine                                                       */
/* ============================================================= */
const slides = Array.from(document.querySelectorAll('.slide'));
const controllers = {};
const state = { current: 0, step: 0 };

function maxStepsFor(slide){
  const c = controllers[slide.id];
  if (c && typeof c.maxSteps === 'number') return c.maxSteps;
  let m = 0;
  slide.querySelectorAll('[data-step]').forEach(b => m = Math.max(m, +b.dataset.step));
  return m;
}
function applySteps(slide, step){
  slide.querySelectorAll('[data-step]').forEach(b => {
    b.classList.toggle('shown', (+b.dataset.step) <= step);
  });
  const c = controllers[slide.id];
  if (c && c.onStep) c.onStep(step);
}
function render(){
  slides.forEach((s,i)=> s.classList.toggle('active', i===state.current));
  applySteps(slides[state.current], state.step);
  const total = slides.length;
  document.getElementById('progress').style.width =
    (((state.current)/(total-1))*100) + '%';
  document.getElementById('counter').textContent = (state.current+1)+' / '+total;
  if (location.hash !== '#'+(state.current+1))
    history.replaceState(null,'','#'+(state.current+1));
}
function goTo(i, dir){
  i = Math.max(0, Math.min(slides.length-1, i));
  if (i === state.current) return;
  const old = slides[state.current];
  const oc = controllers[old.id]; if (oc && oc.onLeave) oc.onLeave();
  state.current = i;
  state.step = (dir === 'back') ? maxStepsFor(slides[i]) : 0;
  render();
  const nc = controllers[slides[i].id]; if (nc && nc.onEnter) nc.onEnter();
}
function next(){
  const slide = slides[state.current];
  if (state.step < maxStepsFor(slide)){ state.step++; applySteps(slide, state.step); }
  else goTo(state.current+1, 'fwd');
}
function prev(){
  if (state.step > 0){ state.step--; applySteps(slides[state.current], state.step); }
  else goTo(state.current-1, 'back');
}

document.addEventListener('keydown', e => {
  const help = document.getElementById('help');
  if (e.key === '?'){ help.classList.toggle('on'); e.preventDefault(); return; }
  if (e.key === 'Escape'){ help.classList.remove('on'); return; }
  if (help.classList.contains('on')) return;
  switch(e.key){
    case 'ArrowRight': case ' ': case 'PageDown': case 'ArrowDown':
      next(); e.preventDefault(); break;
    case 'ArrowLeft': case 'PageUp': case 'ArrowUp':
      prev(); e.preventDefault(); break;
    case 'Home': goTo(0,'fwd'); e.preventDefault(); break;
    case 'End': goTo(slides.length-1,'fwd'); e.preventDefault(); break;
    case 'f': case 'F':
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
```

```js
      else document.exitFullscreen();
      e.preventDefault(); break;
  }
});
// click / tap navigation (right half next, left half prev)
document.getElementById('stage').addEventListener('click', e => {
  if (e.target.closest('button,input,a,.no-nav')) return;
  const r = e.currentTarget.getBoundingClientRect();
```

Boot sequence (verbatim, end of the engine script):

```js
  const still = location.search.indexOf('still') >= 0;
  if (still){
    const st = document.createElement('style');
    st.textContent = '.slide,.build,#pulse{transition:none!important;animation:none!important}';
    document.head.appendChild(st);
  }
  const h = parseInt((location.hash||'#1').slice(1),10);
  state.current = (!isNaN(h) && h>=1 && h<=slides.length) ? h-1 : 0;
  state.step = still ? maxStepsFor(slides[state.current]) : 0;
  render();
  const c = controllers[slides[state.current].id]; if (c && c.onEnter) c.onEnter();
}
window.addEventListener('hashchange', ()=>{
  const h = parseInt((location.hash||'#1').slice(1),10);
  if (!isNaN(h) && (h-1)!==state.current) goTo(h-1,'fwd');
});
boot();
</script>
```

Key behaviours:
- **Slide index** = DOM order; URL hash is the 1-based index (`talk.html#12`); `hashchange` is wired. `?still` query = no transitions and every slide starts at its **final** build state (used by render scripts and PDF).
- **Build steps**: any element with `data-step="N"` (integer) gets class `shown` when `N <= state.step`. Steps are cumulative and reversible; `.build` supplies the fade/translate CSS, `.shown` reveals. `maxSteps` is auto-computed as max `data-step` on the slide unless the slide's controller sets `maxSteps`. Elements need BOTH `class="build"` and `data-step`. Several elements can share a step. Going back into a slide lands on its last step; going forward lands on step 0. Controller `maxSteps:0` disables stepping even if `data-step` exist.
- **Keys**: Right/Space/PageDown/Down = next; Left/PageUp/Up = prev; Home/End; `F` fullscreen; `?` help, `Esc` closes help. Click on right 38% of the stage = next (there is no click-left-for-prev). Anything inside `button,input,a,.no-nav` is exempt from click navigation: **put `class="no-nav"` on interactive containers** (s-dagx does).
- **Per-slide hooks** (no DOM custom events like `slide:enter` exist): register `controllers['s-id'] = { maxSteps?:number, onEnter(), onLeave(), onStep(step) }`. `onEnter` is called after render on every entry (also on initial load for the starting slide) and sees `state.step` already set; `onStep(step)` is called by `applySteps` on every render, including entry; `onLeave` on exit. There is no overview mode, no laser pointer, no notes view.
- **Timing gotcha**: a script placed before the engine must register on `DOMContentLoaded` (s-whoami-a does, and also self-starts if its slide is already active). Scripts after the engine can assign `controllers[...]` directly. A script after `boot()` (like s-dagx) will not get `onEnter` on first load if its slide is the start slide, so it either initialises eagerly at load or uses its own observer.
- **Initialisation policy**: all interactives build their SVG/DOM **eagerly at page load** (guarded `if (!el) return;`), not lazily; animation loops start in `onEnter` and stop in `onLeave` (rAF or `setInterval`). Example hooks, verbatim:

```js
  controllers['s-temp'] = {
    maxSteps:0,
    onEnter(){ draw(); },
    onLeave(){ if (autoTimer){ clearInterval(autoTimer); autoTimer=null;
      document.getElementById('tempAuto').textContent='Autoplay'; } }
  };
```

```js
  controllers['s-scatter'] = { maxSteps: years.length-1, onEnter(){ show(state.step); }, onStep(s){ show(s); } };
```

```js
  controllers['s-agent'] = {
    maxSteps:0,
    onEnter(){ phase=0; tick(); timer = setInterval(tick, 1000); },
    onLeave(){ if (timer){ clearInterval(timer); timer=null; } codeLines.forEach(l=>l.classList.remove('hot')); }
  };
```

```js
    const t = (now - t0) / 1000 * 1.5;  /* 1.5x speed: about 8.8 s total */
    frame(Math.min(t, END));
    raf = t < END ? requestAnimationFrame(loop) : 0;
  }
  function start(){ stop(); if (still) { frame(END); return; } frame(0); t0 = performance.now(); raf = requestAnimationFrame(loop); }
  function stop(){ if (raf) cancelAnimationFrame(raf); raf = 0; }
  window.waWhoamiA = { frame, END, start, stop };
  frame(still ? END : 0);
  function register(){
    if (typeof controllers === 'undefined') return;
    controllers['s-whoami-a'] = {
      maxSteps: 0,
      onEnter(){ start(); },
      onLeave(){ stop(); },
      onStep(){ if (still) frame(END); }
    };
    const me = document.getElementById('s-whoami-a');
    if (me && me.classList.contains('active')) start();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', register); else register();
})();
```

s-dagx has no controller: it listens to the engine's class toggles with a `MutationObserver` on its `.build` story lines (verbatim at the end of section 3).

## 3. Worked examples

### 3.1 Simple build-step slide (s-summary, verbatim)

```html
<section class="slide" id="s-summary">
  <div class="frametitle">Summary<span class="rule"></span></div>
  <div class="body center stack-lg">
    <p class="build" data-step="1"><span class="teal b">LLMs are stateless functions:</span> <span class="muted">not magic, not minds</span></p>
    <p class="build" data-step="2"><span class="teal b">Agents are loops:</span> <span class="muted">scaffolding provides the action</span></p>
    <p class="build" data-step="3"><span class="teal b">The filesystem is ground truth:</span> <span class="muted">memory that survives and can be checked</span></p>
    <p class="build" data-step="4"><span class="teal b">The human provides taste:</span> <span class="muted">technique over hype</span></p>
  </div>
</section>

```

Variant with a code block (s-curl) and one with boxes (s-cta) are at lines 1588 and 2585. Statement slide (s-correctable):

```html
<section class="slide statement" id="s-correctable">
  <div class="stack">
    <div class="big" style="font-size:5.8cqh;">There is a way to
      <span style="color:var(--cyan)">correct for these errors</span></div>
    <div class="sub" style="margin-top:2.4cqh;">Reliable computation out of unreliable components.</div>
  </div>
</section>

```

### 3.2 s-dagx (proof-DAG explorer), verbatim. The 364-node JSON on line 2302 (`<script type="application/json" id="dxData">[{"id":"conj-b-restricted","k":"lemma","s":"conjecture","af":"none","d":[],"c":"..."}, ...]`, fields id/k kind/s status/af audit/d deps/c contract) is elided.

HTML and CSS:

```html
<section class="slide gfig" id="s-dagx">
  <style>
    #s-dagx .dx-canvas{position:absolute;left:5.5556cqh;top:16.6cqh;width:118cqh;height:65cqh;
      background:#fff;border:0.14cqh solid var(--lightgrey);border-radius:1.2cqh;overflow:hidden;cursor:crosshair;}
    #s-dagx .dx-canvas svg{width:100%;height:100%;display:block;}
    #s-dagx .dx-edge{stroke:#335B74;stroke-opacity:.13;stroke-width:1;fill:none;}
    #s-dagx .dx-edge.on{stroke-opacity:.85;stroke-width:1.7;}
    #s-dagx.dx-sel .dx-edge:not(.on){stroke-opacity:.05;}
    #s-dagx .dx-node{stroke:#fff;stroke-width:1;cursor:pointer;transition:r .15s;}
    #s-dagx .dx-node.inh{stroke:#b57a1c;stroke-dasharray:2 1.5;}
    #s-dagx .dx-node.open{stroke:#8f3f52;}
    #s-dagx.dx-sel .dx-node:not(.on){opacity:.28;}
    #s-dagx .dx-node.on{stroke:#1a1e21;stroke-width:1.3;}
    #s-dagx .dx-node.pick{stroke:#1a1e21;stroke-width:2.6;}
    #s-dagx .dx-lab{font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:11px;fill:#1a1e21;
      paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round;pointer-events:none;}
    #s-dagx .dx-axis{font-size:10px;fill:#8a969c;font-style:italic;}
    #s-dagx .dx-panel{position:absolute;left:127.5cqh;top:16.6cqh;width:44.7cqh;height:65cqh;display:flex;flex-direction:column;}
    #s-dagx .dx-leg{display:grid;grid-template-columns:auto 1fr auto;column-gap:1.1cqh;row-gap:.55cqh;align-items:center;
      font-size:1.75cqh;color:var(--ink);line-height:1.2;}
    #s-dagx .dx-leg .sw{width:1.9cqh;height:1.9cqh;border-radius:50%;border:.16cqh solid #fff;box-shadow:0 0 0 .12cqh #c3ced4;}
    #s-dagx .dx-leg .n{font-weight:700;color:var(--darkteal);text-align:right;font-variant-numeric:tabular-nums;}
    #s-dagx .dx-card{margin-top:1.4cqh;background:var(--codebg);border-left:.55cqh solid var(--cyan);border-radius:.9cqh;
      padding:1.3cqh 1.6cqh;flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:.7cqh;overflow:hidden;}
    #s-dagx .dx-id{font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:2cqh;font-weight:700;color:var(--darkteal);
      white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
    #s-dagx .dx-chips{display:flex;gap:.7cqh;flex-wrap:wrap;}
    #s-dagx .dx-chip{font-size:1.45cqh;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#fff;
      border-radius:.6cqh;padding:.25cqh .8cqh;background:var(--muted);}
    #s-dagx .dx-contract{font-size:1.7cqh;line-height:1.32;color:var(--ink);display:-webkit-box;-webkit-line-clamp:5;-webkit-box-orient:vertical;overflow:hidden;}
    #s-dagx .dx-rest{font-size:1.75cqh;line-height:1.35;color:var(--darkteal);margin-top:auto;}
    #s-dagx .dx-rest b{font-size:2.4cqh;}
    #s-dagx .dx-story{margin-top:1.1cqh;font-size:1.8cqh;line-height:1.32;color:var(--muted);min-height:6.2cqh;}
    #s-dagx .dx-story .build{display:none;}
    #s-dagx .dx-story .build.shown{display:block;}
    #s-dagx .dx-hint{position:absolute;left:5.5556cqh;top:82.4cqh;font-size:1.65cqh;color:#8a969c;font-style:italic;}
    #s-dagx .dx-story:has(#dxStep2.shown) #dxStep1{display:none;}
  </style>
```

Markup after the data block (the data block is line 2302):

```html
  <div class="g-ftitle">What the Swiss cheese produces</div>
  <div class="g-frule"></div>
  <div class="g-kick">one open problem, worked by agents for five weeks<br>364 results &middot; 769 dependency edges &middot; every arrow is a checked contract</div>
  <!-- Source: ../almost-idempotent-stochastic-maps, argument/lemmas/*.md (364 shards, snapshot 4 Aug 2026, commit d18d9dde); status and af fields as recorded by the linker. -->

  <div class="dx-canvas no-nav" id="dxCanvas">
    <svg id="dxSvg" viewBox="0 0 1180 650" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="dependency graph of a proof: 364 results coloured by how rigorously each was checked"></svg>
  </div>
  <div class="dx-hint" id="dxHint">click any node: what it rests on lights up &middot; depth grows to the right</div>

  <div class="dx-panel no-nav">
    <div class="dx-leg" id="dxLeg"></div>
    <div class="dx-card">
      <div class="dx-id" id="dxId">the whole argument</div>
      <div class="dx-chips" id="dxChips"></div>
      <div class="dx-contract" id="dxContract">A registry of one-line contracts. A linker refuses any edge from a rigorous result to an unrigorous one, so the colour of a node is an upper bound on everything above it.</div>
      <div class="dx-rest" id="dxRest"></div>
    </div>
    <div class="dx-story">
      <div class="build" data-step="1" id="dxStep1">Near the top of the validated chain: an interface lemma. Everything it rests on is green, and each green node was proved by one fresh agent and attacked by another.</div>
      <div class="build" data-step="2" id="dxStep2">The open problem itself. What it still rests on is orange and red: the gap is visible, named, and exactly where the next agent gets sent.</div>
    </div>
  </div>

  <div class="g-summ build" data-step="3" style="top:87cqh;font-size:3cqh;">One agent proves, a fresh one attacks, a linker keeps the ledger. The colour is what survived.</div>
</section>

<!-- 32. DIVIDER: the trend ================================ -->
```

JS (a plain IIFE after the engine; eager init, no controller, MutationObserver bridges build steps to presets):

```js
<script>
/* ============================================================= */
/*  Proof-DAG explorer (s-dagx). Data: ../almost-idempotent-      */
/*  stochastic-maps argument registry, 364 shards, 4 Aug 2026.    */
/* ============================================================= */
(function(){
  const sec = document.getElementById('s-dagx');
  const svg = document.getElementById('dxSvg');
  const dataEl = document.getElementById('dxData');
  if (!sec || !svg || !dataEl) return;
  const N = JSON.parse(dataEl.textContent);
  const by = new Map(N.map(n => [n.id, n]));
  N.forEach(n => { n.d = n.d.filter(d => by.has(d)); n.kids = []; });
  N.forEach(n => n.d.forEach(d => by.get(d).kids.push(n.id)));

  // Rung = the colour. Priority order mirrors the repo's own figure script.
  const RUNGS = {
    val:   {c:'#42BA97', t:'machine-validated: proved by one fresh agent, attacked by another'},
    prose: {c:'#2683C6', t:'proved in prose, not yet adversarially checked'},
    inh:   {c:'#E8A33D', t:'inherited paper-proof, unaudited here'},
    conj:  {c:'#EFD58B', t:'conjecture, stated, heuristic or numerical'},
    open:  {c:'#C0687A', t:'open problem'},
    dead:  {c:'#9AA6AD', t:'disproved or obstruction'},
  };
  function rung(n){
    if (n.af === 'validated') return 'val';
    if (n.s === 'proved') return 'prose';
    if (n.s === 'proved-mod-audit') return 'inh';
    if (n.s === 'open' || n.k === 'open-problem') return 'open';
    if (n.s === 'disproved' || n.s === 'obstruction' || n.k === 'obstruction') return 'dead';
    return 'conj';
  }
  N.forEach(n => n.r = rung(n));

  // Layered layout: x = longest-path depth, y = barycentre order within a column.
  const depth = new Map();
  function dep(id){
    if (depth.has(id)) return depth.get(id);
    const n = by.get(id);
    const v = n.d.length ? 1 + Math.max(...n.d.map(dep)) : 0;
    depth.set(id, v); return v;
  }
  N.forEach(n => n.x = dep(n.id));
  const maxD = Math.max(...N.map(n => n.x));
  const cols = Array.from({length: maxD + 1}, () => []);
  N.forEach(n => cols[n.x].push(n));
  cols.forEach(c => c.sort((a, b) => a.id < b.id ? -1 : 1));
  N.forEach(n => n.y = cols[n.x].indexOf(n));
  for (let sweep = 0; sweep < 8; sweep++){
    const fwd = sweep % 2 === 0;
    for (let i = 0; i <= maxD; i++){
      const c = cols[fwd ? i : maxD - i];
      c.forEach(n => {
        const nb = fwd ? n.d : n.kids;
        const ys = nb.map(id => by.get(id).y);
        n.bc = ys.length ? ys.reduce((a, b) => a + b, 0) / ys.length : n.y;
      });
      c.sort((a, b) => a.bc - b.bc || (a.id < b.id ? -1 : 1));
      c.forEach((n, k) => n.y = k);
    }
  }
  const W = 1180, H = 650, PADX = 26, PADY = 14;
  // Columns holding at most three nodes (the long Route-F spine) get 55% pitch,
  // so the dense early layers are not crushed into the left fifth of the canvas.
  const wts = cols.map(c => c.length <= 3 ? 0.55 : 1);
  const cum = []; let acc = 0; cols.forEach((c, i) => { cum[i] = acc; acc += wts[i]; }); acc -= wts[maxD];
  const xs = d => PADX + cum[d] * (W - 2 * PADX) / acc;
  cols.forEach(c => {
    const pitch = Math.min((H - 2 * PADY) / (c.length + 1), 34);
    const top = H / 2 - pitch * (c.length - 1) / 2;
    c.forEach((n, k) => { n.px = xs(n.x); n.py = top + k * pitch; });
  });

  // Draw. Edges first, then nodes, then labels.
  const NS = 'http://www.w3.org/2000/svg';
  const el = (t, a) => { const e = document.createElementNS(NS, t); for (const k in a) e.setAttribute(k, a[k]); return e; };
  const gE = el('g', {}), gN = el('g', {}), gL = el('g', {});
  svg.appendChild(gE); svg.appendChild(gN); svg.appendChild(gL);
  const edges = [];
  N.forEach(n => n.d.forEach(d => {
    const a = by.get(d), dx = (n.px - a.px) * 0.5;
    const p = el('path', {class: 'dx-edge', d: `M${a.px},${a.py} C${a.px + dx},${a.py} ${n.px - dx},${n.py} ${n.px},${n.py}`});
    gE.appendChild(p); edges.push({from: d, to: n.id, p});
  }));
  const circ = new Map();
  N.forEach(n => {
    const c = el('circle', {class: 'dx-node ' + n.r, cx: n.px, cy: n.py, r: cols[n.x].length > 40 ? 3.2 : 4.6, fill: RUNGS[n.r].c});
    c.addEventListener('click', e => { e.stopPropagation(); select(n.id, true); });
    c.addEventListener('mouseenter', () => hover(n));
    c.addEventListener('mouseleave', () => hover(null));
    gN.appendChild(c); circ.set(n.id, c);
  });
  const ax = el('text', {class: 'dx-axis', x: PADX, y: H - 4}, {}); ax.textContent = 'leaves: definitions and cited theorems'; gL.appendChild(ax);
  const ax2 = el('text', {class: 'dx-axis', x: W - PADX, y: H - 4, 'text-anchor': 'end'}); ax2.textContent = 'depth ' + maxD + ': the far end of one proof chain'; gL.appendChild(ax2);
  const hoverLab = el('text', {class: 'dx-lab'}); gL.appendChild(hoverLab);
  const pickLab = el('text', {class: 'dx-lab', 'font-weight': '700'}); gL.appendChild(pickLab);
  function place(lab, n){
    if (!n){ lab.textContent = ''; return; }
    const right = n.px < W * 0.7;
    lab.setAttribute('x', n.px + (right ? 8 : -8)); lab.setAttribute('y', n.py + 4);
    lab.setAttribute('text-anchor', right ? 'start' : 'end'); lab.textContent = n.id;
  }
  function hover(n){ place(hoverLab, n && n.id !== picked ? n : null); }

  // Legend with live counts.
  const leg = document.getElementById('dxLeg');
  const counts = {}; N.forEach(n => counts[n.r] = (counts[n.r] || 0) + 1);
  for (const k in RUNGS){
    const sw = document.createElement('div'); sw.className = 'sw'; sw.style.background = RUNGS[k].c;
    if (k === 'inh') sw.style.boxShadow = '0 0 0 .12cqh #b57a1c';
    const t = document.createElement('div'); t.textContent = RUNGS[k].t;
    const c = document.createElement('div'); c.className = 'n'; c.textContent = counts[k] || 0;
    leg.appendChild(sw); leg.appendChild(t); leg.appendChild(c);
  }

  // Selection: the dependency closure of one node.
  const idEl = document.getElementById('dxId'), chipsEl = document.getElementById('dxChips');
  const conEl = document.getElementById('dxContract'), restEl = document.getElementById('dxRest');
  const total = N.length;
  const summaryAll = () => {
    idEl.textContent = 'the whole argument';
    chipsEl.innerHTML = '';
    conEl.textContent = 'A registry of one-line contracts. A linker refuses any edge from a rigorous result to an unrigorous one, so the colour of a node is an upper bound on everything above it.';
    restEl.innerHTML = `<b>${total}</b> results &middot; <b>${counts.val || 0}</b> machine-validated &middot; <b>${(counts.open || 0)}</b> still open`;
  };
  let picked = null;
  function closure(id){
    const seen = new Set(), st = [id];
    while (st.length){ const x = st.pop(); by.get(x).d.forEach(d => { if (!seen.has(d)){ seen.add(d); st.push(d); } }); }
    return seen;
  }
  function select(id, manual){
    if (picked === id && manual){ id = null; }
    picked = id;
    sec.classList.toggle('dx-sel', !!id);
    const on = id ? closure(id) : new Set();
    circ.forEach((c, k) => { c.classList.toggle('on', k === id || on.has(k)); c.classList.toggle('pick', k === id);
      c.setAttribute('r', k === id ? 7.5 : (on.has(k) ? 5.6 : (cols[by.get(k).x].length > 40 ? 3.2 : 4.6))); });
    edges.forEach(e => e.p.classList.toggle('on', !!id && (e.to === id || on.has(e.to)) && (on.has(e.from))));
    place(pickLab, id ? by.get(id) : null); hoverLab.textContent = '';
    if (!id){ summaryAll(); return; }
    const n = by.get(id);
    idEl.textContent = n.id;
    const chip = (t, bg) => `<span class="dx-chip" style="background:${bg}">${t}</span>`;
    chipsEl.innerHTML = chip(n.k, 'var(--darkteal)') + chip(n.s, RUNGS[n.r].c) + (n.af !== 'none' ? chip('af ' + n.af, n.af === 'validated' ? '#2e9c7c' : 'var(--muted)') : '');
    conEl.textContent = n.c || '';
    const cc = {}; on.forEach(k => { const r = by.get(k).r; cc[r] = (cc[r] || 0) + 1; });
    const bad = (cc.inh || 0) + (cc.conj || 0) + (cc.open || 0);
    restEl.innerHTML = on.size
      ? `rests on <b>${on.size}</b> results: <b style="color:#2e9c7c">${cc.val || 0}</b> machine-validated &middot; <b style="color:#2683C6">${cc.prose || 0}</b> prose &middot; <b style="color:#b57a1c">${bad}</b> unverified or open`
      : 'a leaf: rests on definitions and cited theorems only';
  }
  svg.addEventListener('click', () => select(null, false));
  summaryAll();

  // Build steps drive presets; the engine toggles .shown on the story lines.
  const s1 = document.getElementById('dxStep1'), s2 = document.getElementById('dxStep2');
  const PRESET1 = 'lem-thmainext-conditional', PRESET2 = 'op-classical';
  function sync(){
    const a = s1.classList.contains('shown'), b = s2.classList.contains('shown');
    const want = b ? PRESET2 : (a ? PRESET1 : null);
    if (want !== picked) select(want, false);
  }
  const mo = new MutationObserver(sync);
  mo.observe(s1, {attributes: true, attributeFilter: ['class']});
  mo.observe(s2, {attributes: true, attributeFilter: ['class']});
})();
</script>
```

Pattern worth copying: data embedded as `<script type="application/json" id="...">`, parsed with `JSON.parse(el.textContent)`; SVG with `viewBox` and `preserveAspectRatio`; container marked `no-nav`; story lines are `.build[data-step]` that the JS watches. s-eci (line 2337-2486) is the second model: chart drawn at load into `<svg viewBox="0 0 1280 720">` using `layer(n)` groups that are `class="build" data-step="n"` so the engine reveals chart layers step by step with no JS hook at all. s-flurry has no JS; it is pure `.build[data-step]` rows (steps 1 to 7) plus the CSS above.

## 4. Libraries, fonts, network
- **d3: not present** (no `<script src>`, no inline copy; the hits for "d3" in grep are inside base64 images). **gsap: not present.** Animation is CSS transitions plus `requestAnimationFrame` with hand-written easing (`ease = x => x*x*(3-2*x)`, `clamp`, `lerp`). If designers want d3 they must inline a minified copy (about 280 KB for full d3 v7, or just `d3-scale`/`d3-shape`) into a `<script>` in the file; do not use a CDN.
- **Fonts**: `system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`; mono `"SF Mono", ui-monospace, "JetBrains Mono", Menlo, Consolas, monospace`; math serif `Cambria, Georgia, "STIX Two Math", ...`. No webfonts.
- **Network**: none at runtime. Images are base64 `data:` URIs. Only two `<a href="https://...">` on s-whoami-b. Single self-contained file; keep it that way.

## 5. Render verification workflow
Node v24.11.1 at `/home/tobias/.nvm/versions/node/v24.11.1/bin/node`. **No `node_modules` in the project or parents; `npx --no-install playwright` fails.** Playwright is imported by absolute path from the global CLI install: `/home/tobias/.nvm/versions/node/v24.11.1/lib/node_modules/@playwright/cli/node_modules/playwright/index.mjs` (exists). So just run with `node`, from the project root:
```
cd /home/tobias/Projects/ai-agents-seminar/Magdeburg-talk-2026
node design/render.mjs [outdir] [slideId|index ...]     # default outdir design/renders/latest
node design/render-steps.mjs <slideId> [outdir]          # default design/renders/steps
node design/print-pdf.mjs [out.pdf]                      # default slides-web/talk.pdf
```
- `render.mjs`: opens `talk.html?still#1` at 1920x1080, for each slide calls `goTo(i,'fwd')` and `applySteps(slide, maxStepsFor(slide))` (final build state), waits 250 ms, runs checks, saves `NN-<id>.png` and `report.json` (`[{n,id,issues}]`), prints `ok` / `ISSUES n` per slide and a summary. Checks: (1) **off-stage**: every visible descendant (skipping non-root SVG internals, `display:none`, `visibility:hidden`, `opacity:0`, zero-size) whose bounding box extends more than 1 px past the `#stage` rect on any side; (2) **clipped**: any element with `scrollHeight > clientHeight + 2` whose `overflow-y` is not `visible/auto/scroll`, reported as `CLIPPED <text>`. There is **no pairwise collision/overlap test**; overlaps between text blocks must be checked by eye in the PNGs. Note elements still at `opacity:0` (unrevealed) are skipped, so render at final state only catches revealed content.
- `render-steps.mjs`: screenshots one slide at each step 0..max (`<id>-stepK.png`) and prints page errors (`pageerror`, console errors). Use it to check intermediate build states and JS exceptions. It does NOT run the overflow checks.
- `print-pdf.mjs`: Chromium print to `talk.pdf` (1280x720 pages, final state; injects an override so `#stage` flows in print).
- Add a new slide: insert the `<section>` in DOM order, run `node design/render.mjs /tmp/out <id>`, then `render-steps.mjs <id>`. Whole-deck run should report 0 findings (CHANGELOG-2026-09-23 records zero findings for the full deck).

## 6. Conventions and narrative

**Writing rules**
- **No em dashes** anywhere in slide text (HANDOFF: "all em dashes removed"; the only U+2014 in the file is inside the s-dagx JSON data). Use commas, colons, `&middot;`, `&ndash;` for ranges. Avoid emojis.
- Entities for non-ASCII (`&rarr; &asymp; &middot; &ldquo; &rsquo; &ouml;`), rather than raw characters, in most slides.
- **Source attribution**: not on the slide face but as an HTML comment directly under the claim, e.g. `<!-- Source: Quanta, 8 Sep 2026 (url): ... -->` (25 such comments; they name file, date read, and numbers). On-slide provenance is a muted `.caption` line: `arXiv:2602.12176 &middot; Harvard, Vanderbilt, Cambridge, OpenAI &middot; February 2026` then a second line with the claim. Dates are written "22 Sep 2026".
- **Caption style** (`.caption`): line 1 identifier/venue/date joined by `&middot;`, `<br>`, line 2 the one-sentence takeaway or the method (sample size, "every hit read by hand"), with the key number in `<span class="hl">`.
- Frame titles are short noun phrases or claims, sentence case, no trailing period: "Nondeterministic", "Capability is a straight line", "Theoretical sciences are 18 months behind".
- Statement slides: one or two sentences, one cyan-highlighted phrase `<span style="color:var(--cyan)">...</span>`, optional `.sub` line below.
- **Word counts** (visible text excluding comments/SVG): median 41 words per slide; plain build-step slides 26 to 50 (s-survey 26, s-summary 35, s-cta 32, s-control 49); statement slides under 30; dense figure slides (gfig) 100 to 270 (s-flurry 271, s-lyapunov 241, s-euhosted 151, s-dagx 150). Anything above about 90 words on a plain slide is exceptional.
- **Live build usage**: speaker presses Right/Space; each press reveals one `data-step` item (survey: three questions one at a time; summary: four one-line claims with a bold teal lead and muted gloss; s-flurry: ten ledger rows then the quote box, then the summary line). The last step is usually the takeaway line (`.g-summ`), so the slide is "complete" only on the final press. Pressing Left steps back through the builds. Interactive slides use `maxSteps:0` and are driven by mouse (sliders, clicks) with `no-nav` containers. Deck is also exported as PDF at final state, so every build must be a pure reveal (no content that only exists mid-animation).
- Palette use: darkteal for headings and emphasis, cyan for accent numbers/rules, green/medblue/rose for good/ok/bad, grey for provenance. Highlights on statement slides are cyan, never bold red.
- Sections are introduced by `.divider` slides labelled "Part One" ... with big number at lower right (ids s-div1 to s-div6; note numbering is not contiguous in ids).

**The 64 slides in order** (id, variant, frame title or lead text; blank means none or image-only)
1. `s-title` (title) Large Language Models
2. `s-survey` (plain) Quick survey: hands up
3. `s-whoami-a` (plain) 
4. `s-whoami-b` (plain) Open lectures
5. `s-div1` (divider) Why this talk?
6. `s-hookB` (center fullbleed) It started as a drop
7. `s-hookA` (center fullbleed) 
8. `s-flurry` (gfig) The trickle is becoming a flood
9. `s-arxivack` (center fullbleed) 
10. `s-ackcontrol` (center fullbleed) 
11. `s-ackexp` (center fullbleed) 
12. `s-acksing` (center fullbleed) 
13. `s-control` (plain) A control experiment, run on us
14. `s-scatter` (plain) Six years, one control experiment
15. `s-grief` (gfig) The timeline
16. `s-mathslag` (gfig) Theoretical sciences are 18 months behind
17. `s-capable` (statement) "Progress is astonishing.However, the failure modes have not gone away."
18. `s-gap` (statement) ""I tried ChatGPT and it hallucinated""
19. `s-div2` (divider) What is an LLM?
20. `s-resource` (statement) "A new kind of resource:general-purpose intelligence,bought by the token"
21. `s-fss` (plain) From outside, looking in
22. `s-nondet` (plain) Nondeterministic
23. `s-temp` (plain) Temperature
24. `s-tokens` (plain) Tokens
25. `s-defn` (statement) 
26. `s-ctxwindow` (plain) The context window
27. `s-div3` (divider) The illusion of chat
28. `s-curl` (plain) A single API call
29. `s-chat` (plain) How chat works
30. `s-divfail` (divider) Failure modes
31. `s-zooarch` (plain) The failure zoo: architectural
32. `s-zoopost` (plain) The failure zoo: post-training
33. `s-archfacts` (statement) "These are architectural facts"
34. `s-correctable` (statement) 
35. `s-div4` (divider) From function to agent
36. `s-agent` (plain) The agent loop
37. `s-neverexec` (statement) "The LLM never executes anything"
38. `s-closeloop` (plain) Closing the loop
39. `s-errorcorr` (plain) Error correction for LLMs
40. `s-filesystem` (plain) The filesystem is permanent memory
41. `s-compound` (plain) Errors compound
42. `s-subagents` (plain) Subagents
43. `s-strategies` (plain) Three ways to spend compute on reliability
44. `s-whystructure` (plain) Why structure a proof?
45. `s-lamport` (plain) Lamport structured proofs
46. `s-lyapunov` (plain) Lyapunov, structured
47. `s-adversarial` (plain) Adversarial verification
48. `s-vibefeld` (plain) Vibefeld: molecular pedantry
49. `s-defense` (plain) Lean can be reward hacked
50. `s-dagx` (gfig) What the Swiss cheese produces
51. `s-div6` (divider) The trend
52. `s-eci` (plain) Capability is a straight line
53. `s-bench` (plain) Benchmarks saturate, then get replaced
54. `s-openweight` (plain) You can run the frontier locally
55. `s-euhosted` (plain) The open frontier is already hosted in Europe
56. `s-budget` (plain) What it costs, on your side of the ledger
57. `s-limits` (statement) "The human in the loop is not optional"
58. `s-outsource` (statement) 
59. `s-summary` (plain) Summary
60. `s-cta` (plain) Try it this week
61. `s-afternoon` (plain) An afternoon suffices
62. `s-extended` (gfig) The timeline, extended
63. `s-kontorovich` (plain) The blunt version
64. `s-slopcannon` (statement) "The slop cannon is chargedwhether we like it or not.The only question is how it is aimed"

Narrative arc: Part One "Why this talk?" (hook papers, the flurry of AI-generated results with T1/T2/T3 verification tiers, arXiv acknowledgement stats, the grade control experiment, the timeline and the 18-month lag) then Part Two "What is an LLM?" (stateless nondeterministic function, temperature, tokens, context window), Part Three "The illusion of chat" (API call), "Failure modes" (the failure zoo), Part Four "From function to agent" (agent loop, error correction, filesystem memory, subagents, structured proofs, adversarial verification, the s-dagx proof DAG), Part Five "The trend" (ECI frontier, benchmarks, open weights, costs), closing statements (human in the loop), summary, call to action, extended timeline and a final "slop cannon" statement. Slides with no frametitle in the list above (s-whoami-a, s-hookA, s-arxivack, s-ackcontrol, s-ackexp, s-acksing, s-defn, s-correctable, s-outsource) are image or statement slides whose text is in `.caption`/`.sub`.

## 7. Recipes

### 7.1 Build-step slide
```html
<section class="slide" id="s-newthing">
  <div class="frametitle">Short claim as title<span class="rule"></span></div>
  <div class="body center stack-lg">
    <p class="build" data-step="1"><span class="teal b">Lead phrase:</span> <span class="muted">gloss</span></p>
    <p class="build" data-step="2"><span class="teal b">Second:</span> <span class="muted">gloss</span></p>
  </div>
  <!-- Source: where the claim comes from, date read. -->
</section>
```
Insert at the desired position in DOM order; slide count in the counter/progress updates itself.

### 7.2 Interactive SVG initialised on first entry, keyboard and mouse
This version builds lazily on first `onEnter`, animates while visible, and handles its own keys (the engine already owns arrows/space, so use other keys or intercept in capture phase only while the slide is active).
```html
<section class="slide gfig" id="s-demo">
  <style>
    #s-demo .dm-canvas{position:absolute;left:5.5556cqh;top:16.6cqh;width:118cqh;height:65cqh;
      background:#fff;border:.14cqh solid var(--lightgrey);border-radius:1.2cqh;overflow:hidden;}
    #s-demo svg{width:100%;height:100%;display:block;}
    #s-demo .dm-node{fill:var(--cyan);stroke:#fff;stroke-width:1;cursor:pointer;}
    #s-demo .dm-node.pick{fill:var(--darkteal);}
    #s-demo .dm-info{position:absolute;left:127.5cqh;top:16.6cqh;width:44.7cqh;font-size:1.9cqh;color:var(--ink);}
  </style>
  <div class="g-ftitle">Title of the interactive</div><div class="g-frule"></div>
  <div class="g-kick">one-line kicker, right aligned</div>
  <div class="dm-canvas no-nav"><svg id="dmSvg" viewBox="0 0 1180 650" role="img" aria-label="describe it"></svg></div>
  <div class="dm-info no-nav" id="dmInfo">click a node, or press N</div>
  <div class="g-summ build" data-step="1" style="top:87cqh;font-size:3cqh;">Takeaway line, revealed on first press.</div>
  <script>
  (function(){
    const sec = document.getElementById('s-demo'), svg = document.getElementById('dmSvg');
    const NS = 'http://www.w3.org/2000/svg';
    const el = (t,a)=>{ const e=document.createElementNS(NS,t); for(const k in a) e.setAttribute(k,a[k]); return e; };
    let built = false, picked = -1, raf = 0;
    function build(){
      if (built) return; built = true;
      for (let i=0;i<12;i++){
        const c = el('circle',{class:'dm-node',cx:100+i*90,cy:325+Math.sin(i)*120,r:14});
        c.addEventListener('click', e=>{ e.stopPropagation(); pick(i); });
        svg.appendChild(c);
      }
    }
    function pick(i){
      picked = i;
      svg.querySelectorAll('.dm-node').forEach((c,k)=>c.classList.toggle('pick',k===i));
      document.getElementById('dmInfo').textContent = 'node ' + i;
    }
    function onKey(e){
      if (!sec.classList.contains('active')) return;
      if (e.key === 'n' || e.key === 'N'){ pick((picked+1)%12); e.preventDefault(); }
    }
    document.addEventListener('keydown', onKey);       // keys other than arrows/space/F/?
    function loop(){ /* optional rAF animation */ raf = requestAnimationFrame(loop); }
    // This inline script runs BEFORE the engine script (the section sits above it in the file),
    // so register after DOMContentLoaded, exactly as s-whoami-a does.
    function register(){
      controllers['s-demo'] = {
        onEnter(){ build(); if(!raf) loop(); },
        onLeave(){ cancelAnimationFrame(raf); raf = 0; }
        // omit maxSteps: auto = highest data-step (1 here)
      };
      if (sec.classList.contains('active')){ build(); loop(); }  // started on this slide via #hash
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', register); else register();
  })();
  </script>
</section>
```
Ordering note: the slide markup lives inside `#stage`, which is BEFORE the engine `<script>`, so an inline `<script>` inside the section runs before `controllers` exists (hence the DOMContentLoaded registration above; the alternative is a separate `<script>` placed above the `/* Boot */` comment, as s-agent does). For a slide-local script that ignores `controllers` and observes `.active` with a `MutationObserver` on the section's class (like s-dagx observes `.shown`), no ordering is needed. Also note the engine uses `const`/`let` at top level, so `controllers` is NOT on `window`; reference it as a bare identifier, never `window.controllers`.

### 7.3 Fullbleed image slide
```html
<section class="slide center fullbleed" id="s-newfig">
  <div class="figwrap"><img alt="..." src="data:image/png;base64,..."></div>
  <div class="caption">
    arXiv:XXXX.XXXXX &middot; Authors &middot; Month 2026<br>
    one-line takeaway with <span class="hl">the key number</span> &middot; method note &middot; 22 Sep 2026
    <!-- Source: file, number, date read. -->
  </div>
</section>
```
Add a left-aligned title above the `.figwrap` if wanted: `<div class="frametitle" style="align-self:flex-start;text-align:left;margin-bottom:2.6cqh;">...<span class="rule"></span></div>`. Base64 images inflate the file; render PNGs at about 1600 px wide (the existing ones are around 1100-2200 px), optimise before embedding.

### 7.4 Fit checklist for 1280x720
1. Usable area of a plain slide: 84cqw x 86cqh (padding 7cqh/8cqw); frametitle takes about 12cqh including its rule and margin, leaving about 70cqh of `.body`. gfig slides have no padding: title block occupies top 0-14cqh, the bottom takeaway line sits at 83-90cqh, canvas region about 16.6 to 82cqh.
2. At 3.15cqh and line-height 1.5 a line is 4.7cqh, so a plain slide holds about 14 lines at most; keep to 4 to 7. At 84cqw a line holds about 60 to 70 characters.
3. Use cqh/cqw, never px (except inside SVG viewBoxes or `.dx-lab`-style SVG text, where 1 unit = 1 design px of the viewBox).
4. Minimum text size on a projected slide: 1.75cqh (about 12.6 px at 720p) only for legends and sources; body at 2.3cqh or more.
5. Absolutely positioned gfig children do not reflow: give each an explicit `top/left/width`, keep `left+width <= 166.67cqh`, and check against neighbours by eye.
6. Add `class="no-nav"` to anything clickable; otherwise the right 38% of the stage advances the slide.
7. Reveals: use `build` + `data-step`; on `gfig` also add `gnt` so absolute elements do not slide 1.4cqh when revealed.
8. Images/SVG: `max-width:100%;max-height:100%;object-fit:contain` (already in `.figwrap img`); SVGs get `viewBox` and `width:100%;height:auto`.
9. Provide `role="img"` + `aria-label` on SVGs and keep text inside SVG at `font-family` system stack.
10. No em dashes, no external URLs, no CDN scripts; sources go in HTML comments.
11. Verify: `node design/render.mjs /tmp/out s-newthing` (expect "ok"), `node design/render-steps.mjs s-newthing /tmp/out` (expect `errors 0`), then look at the PNGs for overlaps (the script has no overlap detector), and view the whole deck with `talk.html?still#N` for the final state.
12. If a slide must be reachable by number, remember the hash is the 1-based DOM index, so inserting a slide shifts all later hashes.
