# Tracker-mining pass A — Palomar, Lax, lemma.ing, aimath.robertj1.com

Compiled 26 Aug 2026. Sources: (1) terrytao.wordpress.com Palomar post [fetch blocked
direct — see note], (2) laxarchive.org, (3) lemma.ing, (4) aimath.robertj1.com. All four
are genuinely new inputs relative to `/home/tobias/Projects/ai-agents-seminar/Muenchen-talk-2026/research/llm-proof-results.md`,
which does not mention any of these registries.

**Headline for the talk:** the tracker ecosystem itself is the evidence. As of 26 Aug 2026
there are now (at least) four independent, differently-designed registries that exist
*because* one human curator (a wiki page) is no longer enough to keep up with AI-produced
mathematics. That is "the trickle becoming a flood," made structural.

---

## New results

Only entries not already in the known 33-item list. Field/date/system as stated by the
source; tier assigned per the talk's own T1/T2/T3 scale (T1 = machine-checked or officially
graded; T2 = arXiv/writeup read by named humans; T3 = announced only, no referee).

| Date | Result | Model | Verification (tier + who checked) | Source URL |
|---|---|---|---|---|
| 12 Jun 2026 | **Solubilizer Conjecture disproved** (A.1, plus related A.13, A.16): the intersection of "solubilizers" of a group need not contain a nontrivial normal subgroup. Counterexample: A₅ and a 5-cycle, solubilizer D₁₀. Conjecture itself was AI-generated (from an arXiv conjecture-mining study, arXiv:2412.16177). | "Demonstrandum" multi-agent pipeline | **T3** — "dual computational routes; not externally refereed" per the registry's own label | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| 20 Jul 2026 | **8 Kourovka Notebook problems solved autonomously** — group theory (right-orderable groups, p-group rank inequalities, permutation-group generation, others), each with a Lean proof | Aristotle (Harmonic) | **T1** (Lean, sorry-free) + human oversight — quote: *"The authors monitored the process, clarified definitions when needed, built supporting infrastructure, and translated and polished the resulting formal proof."* | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| 26 Jul 2026 | **Carlson's depth conjecture disproved** (finite-group cohomology, open 31 years) — group SmallGroup(128,859) is the counterexample, with a reproducible GAP/Singular certificate | "TARS" | **T1/T2** — reproducible computational certificate, not stated as externally refereed | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| 1 Aug 2026 | **Non-sofic group constructed** — explicit unit group of a binary Leavitt algebra; Lean-verified. Overlaps with OpenAI's "Astra / Ten Advances" (already on the slide) but registry flags: **the original historical priority claim was withdrawn 3 Aug 2026** | OpenAI "Astra" | **T1** (Lean) but flagged with a retraction/priority caveat — worth noting as a correction-in-progress example | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| 1 Aug 2026 | **Connes's rigidity conjecture disproved** (group-factor isomorphism, open 44 years) — same event as the Astra/OpenAI "Ten Advances" slide item, but registry adds: an **independent, concurrent** proof by Shuoxing Zhou using GPT-5.6 Sol | Astra (OpenAI); independently, GPT-5.6 Sol | **T1** — label used: *"Sorry-free Lean under standard axioms; OpenAI agent-reviewed; independent specialist review pending"* | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| 4 Aug 2026 | **Crouzeix's conjecture** (numerical-range 2-spectral-set property) proved | ChatGPT 5.6 Pro | **T2/T3** (author-verified level per registry tiers; no external review noted) | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| 5 Aug 2026 | **Schiffer's conjecture and Pompeiu's conjecture both disproved** (planar eigenfunction problems) — Lean-verified counterexample | GPT-5.6 / Claude (registry lists both) | **T1** (Lean-verified counterexample) | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| 5 Aug 2026 | **HRT conjecture disproved** (Heil–Ramanathan–Topiwala, open ~30 years) — explicit 12-point linear dependence | GPT-5.6 Pro | **T3** (author-verified; no external review stated) | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| 8 Aug 2026 | **Base-field independence** — 2018 MathOverflow question on amenable algebras solved, theorem extended to modules | ChatGPT 5.6 Sol | **T3** (author-verified) | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| 14 Aug 2026 | **Purely-prime ideals** — counterexample disproving Conjecture 5.8 | ChatGPT Pro | **T3** — "independent review pending" | [aimath.robertj1.com](https://aimath.robertj1.com/) |
| ~2–9 Aug 2026 | **Lax registry launches** with 20 Lean-formalization submissions, several jointly authored by named mathematicians and named AI systems as co-contributors (see Registry stats). Flagship items: *Grid-Minor Theorem (Exponent 8)* (2 Aug, Édouard Bonnet + Codex 5.5/5.6); *Twin-Width Exponential in Treewidth* (7 Aug, multiple incl. Claude Fable 5); *Computability & Turing/Word RAM Equivalence* (9 Aug, Szymon Toruńczyk + Codex 5.6); *Algorithmic Experiments on RAM* and *Sparsity Lectures* (2 Aug, Jan Dreier + Claude Fable 5) | Claude Fable 5 (Anthropic); Codex 5.5/5.6 (OpenAI) | **T1 for the one "Registered" item** (Constructive Lovász Local Lemma — fully Lean-checked); the other 19 are draft/WIP, i.e. **T2-ish** (visible, machine-checkable, not yet formally registered) | [laxarchive.org](https://laxarchive.org/) |
| 18 Aug 2026 | **Palomar registry launches** — a Lean-proof preprint server incubated by the Lean FRO and ICARM, with a 9-person scientific advisory board including Tao, Avigad, Kra, Vakil, Venkatesh. Tao submitted his own formalization of **Sendov's conjecture** as the test case (status of the conjecture itself UNVERIFIED from what I could fetch — likely a demonstration submission, not necessarily claimed as a full resolution; check before using on a slide). | — (registry infrastructure, not a single AI result) | Registry uses its own 3-stage check (see below) | [terrytao.wordpress.com post](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/); [palomar-registry.org](https://palomar-registry.org/) |

Everything above from `aimath.robertj1.com` is drawn from a single AI-summarized fetch of the
registry's front page; I could not page through all 506 entries individually. Treat problem
names/dates as reported by the registry, not independently cross-checked against arXiv —
**flag as UNVERIFIED-BY-ME, verify against the registry directly (or arXiv) before quoting
exact wording on a slide.**

---

## Registry stats

**aimath.robertj1.com — "Open Math Problems Claimed to Be Solved with AI"** (page last
updated 21 Aug 2026):
- **506 total claimed results** tracked.
- Outcomes: 253 proved, 116 disproved, 7 both, 130 not classified.
- Growth: sharp acceleration in Jul–Aug 2026 — **166 entries in July, 101 in August** (as of
  the 21 Aug snapshot, i.e. ~101 in three weeks). This is the single best "flood" number found
  in this pass — most of the registry's content dates from the last two months.
- By field: Combinatorics 124, Number theory 119, Geometry & topology 67, Algebra 31,
  Analysis 44, Mathematical physics 13 (could not retrieve the 13 physics entries individually
  — filter/JS-rendered).
- Problem origin: Human 397, AI-generated 5, Co-generated 3, Unclear 101 — i.e. the vast
  majority of problems AI is solving were posed by humans, only a handful of the *problems
  themselves* were AI-generated (good nuance for the talk: AI is mostly clearing a human
  backlog, not yet setting its own research agenda at scale).
- Verification tiers used: Lean-checked (zero `sorry`) / author-verified / expert-reviewed,
  plus explicit "claim audit flags" for statement mismatches, incomplete formalizations, and
  "blocking debts."

**laxarchive.org ("Lax")** — self-description: *"an arXiv for formalization: independent,
citable submissions that people can read, software can check, and future work can build
upon."*
- **20 submissions**, **170 concepts**, **99 statements** (98 proven).
- Only **1** submission has reached the "Registered" tier (fully checked and locked);
  the other 19 are draft/work-in-progress.
- **1 open proof obligation** outstanding (Grohe–Kreutzer–Siebertz nowhere-dense
  model-checking result, submission `lax-3`).
- Notable: several submissions list a named human mathematician **and** a named AI system
  (Claude Fable 5, or OpenAI Codex 5.5/5.6) as co-contributors on the same formalization —
  the registry's own author metadata already treats the model as a byline, not just a tool.

**lemma.ing** — self-description: *"a kernel, a problem queue, a memory of what has already
been tried, and a permanent place to put results."* Positions itself explicitly as
AI-agent-facing infrastructure: it exposes an **MCP (Model Context Protocol) server
endpoint** so that AI agents can query problems and submit results directly, and reports
**8,191 modules** in its Lean/Mathlib extra library available for automatic kernel-checking
(Mathlib v4.33.0). Its four-tier system:
  - **T0 (Recorded):** appears immediately, no gatekeeping.
  - **T1 (Confirmed):** a reviewing agent (note: itself possibly an AI) confirms it's
    genuine, well-formed, substantive mathematics.
  - **T2 (Canon):** a human/trusted reviewer has worked through it thoroughly.
  - **T3 (Published):** accepted by an external journal or equivalent.
  Explicit design point: *"the tier says how far the entry has been read and accepted, not
  whether a machine checked it"* — i.e. lemma.ing's tiers are orthogonal to Lean-verification,
  unlike Palomar's or Lax's. I could not get the live `/results` table to render via fetch
  (it appears to be a client-rendered SPA) so I have no total entry count for lemma.ing —
  **UNVERIFIED / not obtained.**

**Palomar (palomar-registry.org)** — launched 18 Aug 2026, announced by Terence Tao on his
blog, "incubated by the Lean FRO and by ICARM." Positioned explicitly as **"the analogue of
a preprint server for Lean proofs."** Three-stage check before registration:
  1. **Mechanical verification** — a tool called "Comparator" checks the proof against the
     stated formal claim using *both* the Lean kernel and an independent second kernel
     ("NanoDa"), specifically to catch proofs that technically typecheck but "prove" a
     weakened/different statement.
  2. **Automated editorial review** — **an LLM** assesses whether the formal Lean statement
     faithfully represents the informal mathematical claim, and whether the result clears a
     minimum research-interest bar.
  3. **Disclosure verification** — structured metadata must state authorship, mathematical
     origin, and *what automation was used* (i.e. AI involvement must be declared, not
     hidden).
  Governance: 4 technical maintainers (incl. Tao) with repo control; a 9-person moderator /
  scientific-advisory-board (Tao, Avigad, Ballard, de Dios, Guillen, Kra, Morrison, Vakil,
  Venkatesh) who can authorize retractions but do not review individual submissions.
  Tao is explicit: **"Palomar is not a peer-reviewed journal."** I could not retrieve a live
  entry count from the site (numbers appear to be JS-rendered, came back as em-dash
  placeholders) — **registry size UNVERIFIED**, likely still small/early given the 18 Aug
  launch date.

---

## Notable quotes

- **Terence Tao**, on why Palomar exists and its limits (paraphrase confirmed via two
  independent fetches of the announcement post): checking a Lean repository against a claim
  is non-trivial even for Lean non-experts, because you must confirm (a) the proof typechecks,
  (b) it adds no illegitimate axioms/"cheats," and (c) the formal statement actually matches
  the informal English claim — and Palomar exists to make that three-part check into a
  standard, citable record. *"Palomar is not a peer-reviewed journal."* —
  [terrytao.wordpress.com, 18 Aug 2026](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/)
  (direct fetch of this URL returned HTTP 403 from the automated fetcher both times I tried
  it; the above is reconstructed from a `r.jina.ai` proxy fetch of the same page plus a web
  search snippet quoting the announcement text — treat the exact wording as **paraphrase, not
  verbatim**, and re-fetch directly before quoting Tao word-for-word on a slide).

- **lemma.ing**, on its own design philosophy for the T0 tier: *"Every entry is live as soon
  as it is submitted, so the bottom of the ladder means 'not read yet' rather than 'not good
  enough.'"* — [lemma.ing](https://lemma.ing/)

- **laxarchive.org**, self-description, doubles as a one-line thesis for the whole talk:
  *"an arXiv for formalization: independent, citable submissions that people can read,
  software can check, and future work can build upon."* — [laxarchive.org](https://laxarchive.org/)

- **aimath.robertj1.com**, workflow note on the Aristotle/Kourovka Notebook solves — a good
  concrete answer to "what do humans still do in the loop": *"The authors monitored the
  process, clarified definitions when needed, built supporting infrastructure, and translated
  and polished the resulting formal proof."* — [aimath.robertj1.com](https://aimath.robertj1.com/)

- **aimath.robertj1.com**, boilerplate caveat attached to at least one entry (the "Factorial
  Conjecture," not otherwise detailed here): *"The repository explicitly labels the manuscript
  a research draft that is neither peer reviewed nor formally verified."* — the registry
  applies this kind of caveat inline rather than only in a methods page, which is itself worth
  showing on a slide as evidence the ecosystem is self-policing.

---

## What I could not verify / access limits

- **terrytao.wordpress.com direct fetch → HTTP 403** on two attempts (different prompts).
  Content recovered via (a) a `r.jina.ai` reader-proxy fetch of the same URL, which returned
  full prose, and (b) a web search snippet. Both indirect routes agree with each other, but
  neither is the primary source rendered directly — **recommend a manual visit before the
  talk** if any exact Tao quote is to go on a slide. Blog comments were not visible in the
  proxied fetch (no comments shown, page may have none yet given the 18 Aug date, or they may
  require JS).
- **lemma.ing `/results` page** did not render any actual entries via WebFetch — appears to be
  a client-side-rendered SPA; the tool only saw the static documentation shell. I have the
  tier system and the "8,191 modules" stat but **no total entry count and no example results**
  for lemma.ing. Someone with a real browser should check `https://lemma.ing/results` directly.
- **palomar-registry.org entry counts** — the front page shows placeholder em-dashes where
  counts should render (again likely JS/client-side). Given the 18 Aug 2026 launch date (8
  days before this research), the registry is almost certainly still small (single or low
  double digits) — but this is an inference, not an observed number. **UNVERIFIED.**
- **aimath.robertj1.com's 13 "Mathematical physics" entries** could not be retrieved
  individually (filter appears JS-driven); only the count (13) is confirmed.
- All aimath.robertj1.com result rows above came through an AI-summarization fetch layer, not
  raw HTML I read myself — dates/names/models are as reported by that summary. Cross-check
  against the live site or arXiv before using an exact figure (e.g. "12-point linear
  dependence," "SmallGroup(128,859)") in a citation on a slide.
- Sendov's conjecture (mentioned as Tao's Palomar test-case submission): I found no
  independent evidence it has actually been *resolved* — most likely this is just a
  formalization demo, not a resolution claim. Do **not** put "Sendov's conjecture solved" on
  a slide based on this pass alone.
