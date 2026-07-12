# Large Language Models: A Physicist's Perspective (web deck)

A single-file, self-contained HTML reimagining of the Beamer talk in
`../slides/talk.tex`. Physikalisches Kolloquium, Universitat Wurzburg,
13 July 2026. Tobias J. Osborne, Leibniz Universitat Hannover.

## Open it

Just open `talk.html` in any modern browser (Firefox or Chromium). It works
entirely offline from `file://`: all CSS, JavaScript, and images are inlined,
so there are zero network requests. Nothing to install, no build step.

## Navigation

| Key | Action |
|-----|--------|
| Right arrow, Space, PgDn, Down | next build step or slide |
| Left arrow, PgUp, Up | previous |
| Home / End | first / last slide |
| F | toggle fullscreen |
| ? | keyboard help overlay (Esc closes) |
| Ctrl+P | print / export a PDF fallback (one slide per page) |

The URL hash tracks the slide (for example `talk.html#15`), so any slide can be
linked or reloaded directly. Clicking the right portion of the stage also
advances. Within-slide build steps advance on the same next key before moving
on to the following slide.

The stage is a fixed 16:9 area that letterboxes at any window size; all text is
sized in container-query units so it never overflows.

## Interactive moments

1. **Temperature (slide 15)**: a live Boltzmann sampler. Eight candidate next
   tokens with fixed logits; the temperature slider (0.1 to 3) reshapes the
   softmax bars in real time; Sample and Autoplay draw tokens into a running
   sentence, deterministic at low T and chaotic at high T.
2. **Context window (slide 21)**: an animated bar. Turns stream in and fill the
   window; older turns desaturate (context rot); a final compaction step
   squashes the history into a small summary block, freeing space and losing
   detail. Advance with the next key.
3. **Agent loop (slide 24)**: the LLM to parse to execute to results cycle as an
   SVG with a pulse travelling the loop once per few seconds, alongside the
   while-loop code with the current line highlighted in sync.
4. **Grade decorrelation (slide 6)**: a year scrubber over 2020 to 2025. The
   next key (or the dots) steps through the years; gradient b and correlation r
   update, ending on the 2025 collapse. Carries the mandatory grey caption
   "Synthetic data, illustrative: reproduces the structure of the real six-year
   analysis."
5. **Timeline (slide 8)**: four moments fade and slide in as sequential build
   steps.

## Screenshots

Append `?still` to the URL (for example `talk.html?still#6`) to freeze all
transitions and jump every slide to its final build state. This is what the
headless-Firefox screenshots used during verification.

## Regenerating the embedded images

Source figures live outside this folder and are read-only. They were downscaled
with ImageMagick into a scratch directory and inlined as base64 data URIs by a
small Python script at build time. The finished `talk.html` already contains
them; no regeneration is needed to view or present. Total file size is about
2.1 MB.

Palette: Whitney Teal (dark teal `#335B74`, cyan `#1CADE4`, light grey
`#DFE3E5`). No em dashes anywhere in the deck text.
