# SPEC — MCQST München talk (27 Aug 2026): extending the Würzburg deck

Two deliverables, **already scaffolded** as verbatim copies of the Würzburg
deck with venue/date updated:

- `Muenchen-talk-2026/slides/talk.tex` — LaTeX/beamer deck (builds clean:
  `make` in that dir, lualatex, 56 pages).
- `Muenchen-talk-2026/slides-web/talk.html` — self-contained animated HTML
  deck (single file, 52 slides, letterboxed 16:9 stage, `.build` step
  animation system, Whitney Teal palette in CSS vars).

**Everything already in the deck stays.** The task is purely additive: insert
the new slides specified below, in the stated positions.

## Source material (read-only)

The content comes from the "slop cannon" paper:
`/home/tobias/Projects/slop-cannon-paper/structured-proofs.tex`

Key line ranges:
- Failure modes: 554–605 (hallucination, continual learning, error rates,
  context window, hyperfixation, sycophancy, confident wrongness, semantic
  shift, lack of taste)
- Error correction section + countermeasure table: 716–830
- Three-strategies figure (TikZ source to adapt): 755–828
- Why structure a proof / Lamport format rules: 832–893
- No-cloning worked example: 895–965
- Prover/verifier recipe + cross-model independence + defense in depth
  (Swiss cheese, spectrum of artifacts): 1059–1112
- Getting-started checklist + closing: 1258–1292

Audience: MCQST (Munich Center for Quantum Science and Technology) —
quantum information people. The no-cloning example is home turf; do NOT
over-explain Dirac notation. Lean/formalisation is deliberately
de-emphasised (mention only as the far end of the spectrum; no Lean code).

## New slides

### Block A — new section after the "Subagents" slide, BEFORE the
### `\sectiondivider{Live demo}` (HTML: after the Subagents slide, before
### the Live-demo divider slide)

New section divider: **"Failure modes"**

**A1 — "The failure zoo: architectural"** — four failure modes with their
architectural origin, one line each (2×2 grid of tjo boxes or a compact
list; HTML: build in one at a time):
- Hallucination — no way to guarantee fidelity of storage in weights
- Training cutoff — weights are frozen; no continual learning
- Nonzero per-token error rate — output is a *sampled* distribution
- Context rot — attention degrades as the window fills (quality sags from
  ~30% usage in our experience)

**A2 — "The failure zoo: post-training"** — four more, same layout:
- Hyperfixation — rewarded for visible completion: deletes the failing
  test, hard-codes the answer, declares success (reward hacking)
- Sycophancy — raters prefer being agreed with; it preferentially asserts
  the falsehoods *you would quite like to be true*
- Confident wrongness — fluent, specific, real-shaped, false, unhedged;
  never ask a model to check its own output
- Semantic shift — imports assumptions from a better-studied neighbouring
  field (e.g. Jordan algebras silently treated as C*-algebras)

**A3 — statement slide**:
"These are architectural facts, not mysteries — and each admits a
structural countermeasure" (adapt paper lines 601–605).

**A4 — "Error correction for LLMs"** — THE CENTERPIECE. The
failure-mode → countermeasure table (paper lines 720–736), styled like the
existing Summary slide's table. Rows (compress to fit):
- Finite context window / no continual learning → filesystem as memory
- Hallucination → ground truth on disk (keep every cited paper locally;
  quote verbatim before citing)
- Nonzero error rates → recursive decomposition + verification
- Hyperfixation, sycophancy → independent adversarial verification
  (fresh session, separate agent)
- Confident wrongness → structured proofs (Lamport)
- Semantic shift → formalisation
- Lack of taste → ask a human
Punchline: the agent toolbox from the last section is exactly the cure.
(HTML: reveal rows progressively.)

**A5 — "Errors compound"** — a flat chain of thought has no error
detection: success probability $(1-\epsilon)^n$; at $\epsilon = 1\%$ and
$n = 100$ steps, only 37% survive. A slip at step 3 propagates silently to
step 40 while the trace stays locally fluent. (Physics audience: this is
why long unchecked derivations rot.)

**A6 — "Three ways to spend compute on reliability"** — adapt the paper's
three-panel figure (lines 755–828) to the deck's TikZ styles (LaTeX) /
inline SVG or styled divs (HTML, animated: panel by panel):
(a) flat chain — one slip, silent corruption after;
(b) parallel repetition — majority vote over final answers, helps but
scales poorly with depth;
(c) recursive decomposition — verify each block in isolation, expand what
fails: the concatenated-code strategy (von Neumann 1956).
Punchline: "Above the verification threshold, reliability **compounds**
instead of decaying."

### Block B — woven into the existing "The harder problem" section

**B1 — "Why structure a proof?"** — insert immediately BEFORE the existing
"Adversarial verification" slide. Prose proofs — "By linearity … and
therefore … which contradicts … hence" — hide the gap; when someone pushes
back, *which* step was wrong? Even a five-line argument can conceal it.

**B2 — "Lamport structured proofs"** — the format (paper lines 858–889),
compressed: every assertion gets a hierarchical number (1, 1.1, 1.1.1);
justified by citing earlier steps or by children; ASSUME/CASE/QED scoping;
a leaf with no justification is an *exposed gap*. Three properties as the
punchline: **auditable** (a sceptic can say "I don't believe 1.3.2"),
**modular**, **gap-visible**. "That is the entire formalism — no logic
syntax to learn."

**B3 — "No-cloning, structured"** — the worked example (paper lines
908–951), rendered as a compact proof tree/ledger. Show the actual steps
(abbreviate statements to fit; keep the step numbers and [justifications]):
1.1 ASSUME cloning unitary U exists → 1.2 basis states clone [1.1] →
1.3 linearity: U|+⟩|0⟩ = (|00⟩+|11⟩)/√2 [1.2] → 1.4 cloning:
U|+⟩|0⟩ = |+⟩|+⟩ [1.1] → 1.5 Schmidt rank 2 ≠ 1: contradiction [1.3,1.4]
→ 1.6 QED no such U [1.5].
Punchline: "Doubt step 1.5? Expand it: 1.5.1, 1.5.2 — the proof refines
exactly where the sceptic pushes." One tie-back line: each numbered step
is the small, independently checkable block the error-correction recipe
demands. (HTML: build the tree step by step — this is the slide the
animation system was made for.)

Then the EXISTING "Adversarial verification" + two Vibefeld slides follow
unchanged — they now land as "run provers and verifiers *over the Lamport
tree*".

**B4 — "Break the correlations"** — insert AFTER "Vibefeld: how trust
accumulates". Independence knobs (paper lines 1075–1086): the verifier
sees only the numbered artifact, never the prover's reasoning; pick the
verifier from a different model family (Claude checks GPT) or capability
class; different labs, different training data, different blind spots — a
blind spot shared by every fresh session of one model is often glaring to
another. Agents can invoke each other as shell commands, so this
automates.

**B5 — "Defense in depth"** — insert after B4. Formalisation is a
spectrum, not a single act: one-shot prose → Lamport tree → explicit lemma
DAG with contracts → machine-checked proof. No single layer is
trustworthy alone; the layers fail in *different places* — compose them
(Swiss-cheese / defense in depth, Reason 2000). Cost line: "an agent
produces every layer almost for free." (Suggested visual: horizontal
spectrum arrow with 4 stations; HTML can slide the layers in; a
Swiss-cheese overlay of offset slices with misaligned holes is welcome if
it stays clean.)

### Block C — closing additions

**C1 — "An afternoon suffices"** — insert AFTER the existing "Try it this
week" slide. The getting-started checklist (paper lines 1272–1285),
compressed to ~6 items: open a coding agent in a directory you care
about · write a CLAUDE.md with your standards · keep a worklog + a
directory of every paper you cite · write the lemma you're fighting as a
Lamport tree · set one agent to prove, a second to attack, only then read
it · formalise the one step you trust least. Tag line: "the first three
need no programming at all."

**C2 — final statement slide** (new last content slide, before the
appendix): "The slop cannon is charged whether we like it or not — the
only question is how it is aimed." Sub-line: "Aimed with discipline —
error-corrected, ground-truthed, adversarially checked — it is the
cheapest instrument for rigorous exploration the sciences have ever been
handed." Small grey attribution line: *Raise High Your Slop Cannon —
guide in preparation, 2026* (use a `\slopcaption` macro in LaTeX / a
single obvious span in HTML so it is easy to patch with the arXiv number
later).

## Style rules

- LaTeX: follow the existing deck exactly — one idea per slide, `\vfill`
  sandwiches, `tjo box` / `tjo box fill` TikZ styles, `\statementslide`
  for statements, `\sectiondivider` for the new section, palette colors
  `tjo@darkteal`/`tjo@cyan`/`tjo@lightgrey`, `red!70!black` sparingly for
  failure-red. Frames with `codeblock` need `[fragile]` and the
  environment at column 0. NO new packages unless already in preamble.
- HTML: single self-contained file, no external requests; reuse existing
  CSS classes (`frametitle`, `body`, `stack`, `build`, `statement`,
  `divider`, …) and the existing JS deck logic (slides are
  auto-discovered; builds via `.build` elements). Match font sizing in
  cqh units as neighbouring slides do. Keep it working with keyboard
  navigation exactly as before; the slide counter must update
  automatically.
- Keep German out. No bullet walls: max ~4 items visible per slide,
  prefer progressive reveal (HTML) / restraint (LaTeX).
- Numbers must match the paper: 37% at ε=1%, n=100; ~30% context-usage
  sag; von Neumann 1956; Reason 2000 Swiss cheese.

## Verify

- LaTeX: `cd Muenchen-talk-2026/slides && make` → exit 0, two passes.
  Render EVERY new page with `pdftoppm -png -r 60 -f N -l N talk.pdf p`
  and inspect for overflow/overlap/clipping; fix what you find (verbatim
  codeblock overfulls tolerated). Report final page count.
- HTML: the file must remain valid single-file HTML; verify slide count
  and build steps by inspection, and if a headless Chromium is available
  (`google-chrome`/`chromium --headless --screenshot`), screenshot each
  NEW slide at 1280×720 and inspect. Report what you verified.
