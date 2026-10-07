# Research: design inspiration + public reaction (subagent, 7 Oct 2026). Items marked [secondary]/[unverified] by the researcher.
NOTE: the researcher's claim that "Hadwiger is not a counterexample" is WRONG for this repo: family 157 "Disproves Hadwiger's conjecture even for fractional coloring" (independence number ≤2, χ_f > h(G)), dir A-counterexample-to-Hadwigers-conjecture-September-23-2026, has lean/docs/157.md. Use the repo as source of truth for claims. "17 disciplines" IS verified from overview.tex.
Release facts: repo initial commit 2026-10-06 14:58 PDT (22:00 UTC). ~4.2k stars/377 forks within 24h [unverified digest].

## A. Design inspiration (Opus 5.5 / Fable 5 single-prompt pages)
- Mia "Claude Opus 5.5 – 100 HTML Files" https://miaai-lab.github.io/Claude-Opus-5.5-100-HTML-Files/ : standalone offline files. #010 "Mercury" liquid chrome blob, cursor is a magnet, click splits. #003 "Raster – Swiss Poster Machine": key recomposes grid. #009 "Asterism": click stars to draw constellations. #030 Orbital n-body sandbox, #013 Game of Life as knitting.
- Miler Opus 5.5 showcase https://ohmiler.github.io/opus-5.5/ : "Cursor Black Hole" (mouse-tracking gravity), underwater scroll journey, living digital organism.
- Fable 5 showcase (57 demos, fleets of agents) https://elder-plinius.github.io/FABLE-SHOWCASE/
- Meng To Sakura River Valley three.js https://valley.mengto.here.now ; "Endless Sketchy Santorini" procedural hand-sketched 3D (@thebuggeddev); Matt Shumer Claude-of-Duty FPS (Opus 5).
- Anthropic 3 Oct Opus 5.5 thread: watermill, embossed cards, Milky-Way-to-Jupiter scale-zoom site, water sim (via explainx.ai) [secondary].
- Fable 5 single-prompt three.js: black-hole lensing (@deveshcodes_), finger-tracking dino, Mario Kart clone, eclipse simulator, Swiss lever watch (awesome-claude-fable-5); per-prompt cost $4-12, 15-60 min.
- Fable 5.1 Monument Valley homage https://design.dev/guides/fable-web-design/ (12 min plan, 51 min build, ~2,900 lines).
- Scroll-driven image reveal https://www.mejba.me/blog/interactive-website-claude-fable-5-image-reveal
- "Zubli" WebGL character that blinks/breathes/follows cursor [unverified]; eyes-follow-mouse recipe https://www.kirupa.com/codingexercises/eyes_follow_mouse.htm (atan2 pupil offset).
Steal-this ideas: cursor-magnet paper blob; keypress re-sorts corpus by discipline/date/Lean; families as constellations; gravitational lensing around unverified dots; scale-zoom from 722 papers → one theorem → one Lean term; hand-drawn aesthetic over clean data; each paper a tiny face whose gaze follows cursor (one slide only).

## B. Viz idioms ranked for 1280x720 projector
BEST: unit chart (one dot per paper, colour = Lean status; 722 dots ≥8-10px); FLIP/animated morph of the same dot set between layouts (grid → by discipline → by Lean status → Sankey) on keypress. VERY GOOD: zoomable circle packing (discipline→family→paper); force clusters (precompute layout, animate to stored positions); Sankey attrition ~4,000 posed → 372 families → 722 papers → Lean subset → refereed 0. GOOD: treemap, sunburst (outer ring = Lean), heatmap discipline × verification. LOW: date ridgeline (corpus is a 2-week spike; but busiest-day spike itself is a good single number).

## C. Live-slide rules
Slide = state machine stepped by keyboard; no hover-only affordances; dark bg, high contrast, ≥2px strokes, text ≥28px, dots ≥8px; transitions 600-900ms ease-in-out; reset key; static fallback; preload all, no CDN; precompute force layouts.

## D. Public reaction (6-7 Oct 2026)
1. Andrew Sutherland (MIT), syndicated article (Yahoo): "Until and unless they release the model and people can replicate their results, I think you should treat any claims about one-shotting problems with a single agent as unverified. We should ask for receipts."
2. Daniel Litt (Toronto), same: "If we want to know the answers to these math questions, I see no reason why we should ask the company to keep them secret from us. To me, it's going to be a good thing for mathematics."
3. OpenAI spokesperson: the model "produced almost every one of the results in response to a single prompt handed to a single AI agent."
4. Quanta, Cepelewicz 5 Oct 2026 "Is AI the end of math as we know it?" (predates release): Aaronson "Human mathematicians are forevermore dethroned as the main theorem-proving entities on planet earth."; Ken Ono "You need to brace"; Litt "The existing equilibrium has broken. We'll have to find a new one."; Etingof "If AI proves all possible theorems, and no mathematicians know about these theorems, it cannot be part of culture."; says OpenAI withholding 100+ further results.
5. Bryna Kra (Northwestern) [secondary, BigGo]: "announcing mathematics on Twitter and through press releases is not the way to nurture the fertile soil that produced their training data."
6. Nestor Guillen (NYU) [secondary]: "like the mafia"; "I feel tremendous anxiety... not directed at AI itself, but at the AI companies."
7. Terence Tao: no direct statement found; 6 Oct blog "Hexagon" launches a repo for LLM-assisted research; the one approved comment: "Basically, 'give us your research as training data for free'".
8. AGMAI (Advisory Group on Mathematics and AI, 29 Sep, TokenPost): recommended academic repository not controlled by an AI lab; asked for model name, prompts, reasoning summary, time and compute cost per result; "mathematical work should not be used as a marketing tool"; did not endorse manuscripts or process; input from 600+ mathematicians. Release lacks several of these.
9. kingy.ai analysis: "total inference dollars, tokens, accelerator-hours, training cost, verification cost and human labor cost undisclosed"; scope mismatch example family 197; family 004 (Hilbert 10 over Q) has no Lean page.
10. AI4Math Chronicle tracker: "Do not let aggregate significance imply aggregate mathematical verification."
11. Sam Altman [unverified paraphrase, officechai]: none of the four headline results (quasi-RH, Unique Games, rational Hodge for CM abelian varieties, free group factors) externally confirmed; "looking up at stars with extra awe tonight".
12. Isaac Kim (physicist) on X https://x.com/Isaac__kim/status/2107607429437657563 : "This contains a shocking list of problems in quantum information, many-body physics and quantum computing" (area law in 2D, spin-one Haldane gap, parity not in QAC^0). [snippet only]
13. Hacker News "Sharing AI progress in mathematics" https://news.ycombinator.com/item?id=49984923 ~522 points / 447 comments [digest]. Comment texts fetched may belong to another thread.
Context: Navier–Stokes claim 8 Sep 2026; Fields medallists' declaration (25 signatories) against announcement-by-press-release; Sienicki & Sienicki "Human Audit of OpenAI's AI-Generated Mathematical Proofs" arXiv 2608.14673 (10 Sep); Noferi on Lean certificates: kernel checks the formal statement, not that it matches the intended conjecture.
Suggested one-liner: the bottleneck has moved from producing claims to adjudicating them.
