# Speaker notes: CQT Singapore, Thu 8 Oct 2026 (final deck, 64 slides)

**The message changed today.** Two days after openai/math (6 Oct: 722
manuscripts, 372 result families, 17 disciplines, 26.0M lines of Lean, zero
refereed), this room does not need to be told that LLMs are capable, and it
does not need a long tour of hallucinations. Keep Parts Two and Three brisk.
The weight of the talk is on **agents**: the loop, error correction,
adversarial verification. The **magic trick** is the Haldane interlude
(slides 53 to 58): agents took one of the 722 papers and, within 40 minutes,
turned it into a bespoke interactive explainer that computes live in the
browser. Agents as learning aids is the thread that ties it together: Deep
Blue (slide 13) sets it up ("in chess the engine became the coach"), the
Haldane slides deliver it, and "you can outsource cognition but not
understanding" (63) closes it.

Edits and sources: `CHANGELOG-2026-10-08.md`. Slides not covered below: use the
23 Sep notes (`SPEAKER-NOTES-2026-09-23.md`) and the 4 Sep QuSoft notes **by
slide id**, because the numbers there are stale. Exception: the 23 Sep lines for
`s-eci` are outdated (221 models, Fable 5 leader); use section 60 below.

**Keys.** Arrows, space, PgUp/PgDn as usual; `?` shows the key list.
- Slide 9 (flood): **R replays the pour**. Moving the mouse bends nearby
  particles (cosmetic; keep the pointer off the stage if you do not want it).
- Slides 54 to 57 (Haldane): `[` `]` change β (54 to 56) or u₀ (57); `-` `=`
  change n (55) or C (57); `M` cycles Trotter slices (54). Ignored while `?`
  help is open.
- Animations on 8 to 13 and 54 to 57 need a moment per press: let each step
  land before talking over it.

**Before the talk:** step through slides 54 to 57 once on the presentation
laptop (the chalk SVG filters cost GPU), and glance at slide 13's chess kings
(system font glyphs).

## Slide map

| # | id | title | build steps | today |
|---|---|---|---|---|
| 1 | `s-title` | Large Language Models | 0 | venue |
| 2 | `s-survey` | Quick survey: hands up | 3 |  |
| 3 | `s-whoami-a` | Who is talking (the tangent space) | 0 |  |
| 4 | `s-whoami-b` | Open lectures | 0 |  |
| 5 | `s-div1` | Why this talk? | 0 |  |
| 6 | `s-hookB` | It started as a drop (figure: arXiv:2602.12176) | 0 |  |
| 7 | `s-hookA` | Unit distance disproved (figure: arXiv:2605.20695) | 0 |  |
| 8 | `s-md-trickle` | Then, a trickle | 3 | NEW |
| 9 | `s-md-flood` | The trickle became a flood | 4 | replaced |
| 10 | `s-md-disc` | 17 disciplines | 2 | replaced |
| 11 | `s-md-cascade` | What survives the checks | 4 | replaced |
| 12 | `s-md-picks` | The physicist’s picks | 5 | replaced |
| 13 | `s-deepblue` | Deep Blue comes to mathematics | 4 | NEW |
| 14 | `s-arxivack` | LLM acknowledgments in quant-ph and math-ph (figure) | 0 | replaced |
| 15 | `s-ackexp` | Same data, log axis (figure) | 0 | replaced |
| 16 | `s-acksing` | The Acknowledgment Singularity (figure, satire) | 0 | replaced |
| 17 | `s-control` | A control experiment, run on us | 0 |  |
| 18 | `s-scatter` | Six years, one control experiment | 5 |  |
| 19 | `s-grief` | The timeline | 6 | replaced |
| 20 | `s-mathslag` | The lag collapsed: from three years to three months | 6 | replaced |
| 21 | `s-capable` | Progress is astonishing. Let us understand them. | 0 | retitled |
| 22 | `s-div2` | What is an LLM? | 0 |  |
| 23 | `s-resource` | A new kind of resource: general-purpose intelligence, bought by the token | 0 |  |
| 24 | `s-fss` | From outside, looking in | 0 |  |
| 25 | `s-nondet` | Nondeterministic | 0 |  |
| 26 | `s-temp` | Temperature | 0 |  |
| 27 | `s-tokens` | Tokens | 0 |  |
| 28 | `s-defn` | An LLM is a stateless, nondeterministic function | 0 |  |
| 29 | `s-ctxwindow` | The context window | 3 |  |
| 30 | `s-div3` | The illusion of chat | 0 |  |
| 31 | `s-curl` | A single API call | 0 |  |
| 32 | `s-chat` | How chat works | 0 |  |
| 33 | `s-divfail` | Failure modes | 0 |  |
| 34 | `s-zooarch` | The failure zoo: architectural | 4 |  |
| 35 | `s-zoopost` | The failure zoo: post-training | 4 |  |
| 36 | `s-archfacts` | These are architectural facts | 0 |  |
| 37 | `s-correctable` | There is a way to correct for these errors | 0 |  |
| 38 | `s-div4` | From function to agent | 0 |  |
| 39 | `s-agent` | The agent loop | 0 |  |
| 40 | `s-neverexec` | The LLM never executes anything | 0 |  |
| 41 | `s-closeloop` | Closing the loop | 0 |  |
| 42 | `s-errorcorr` | Error correction for LLMs | 8 |  |
| 43 | `s-filesystem` | The filesystem is permanent memory | 1 |  |
| 44 | `s-compound` | Errors compound | 3 |  |
| 45 | `s-subagents` | Subagents | 0 |  |
| 46 | `s-strategies` | Three ways to spend compute on reliability | 4 |  |
| 47 | `s-whystructure` | Why structure a proof? | 2 |  |
| 48 | `s-lamport` | Lamport structured proofs | 2 |  |
| 49 | `s-adversarial` | Adversarial verification | 0 |  |
| 50 | `s-vibefeld` | Vibefeld: molecular pedantry | 0 |  |
| 51 | `s-defense` | Defense in depth | 6 | retitled |
| 52 | `s-dagx` | What the Swiss cheese produces | 3 | data text (em dash) |
| 53 | `s-hg-intro` | Agents are amazing at helping you understand | 2 | NEW |
| 54 | `s-hg-worldlines` | One partition function, two readings | 3 | NEW |
| 55 | `s-hg-spotlight` | Purity as a spotlight | 4 | NEW |
| 56 | `s-hg-square` | The square on the blackboard | 4 | NEW |
| 57 | `s-hg-flow` | The flow | 3 | NEW |
| 58 | `s-hg-fineprint` | The fine print | 5 | NEW |
| 59 | `s-div6` | The trend | 0 |  |
| 60 | `s-eci` | Capability is a straight line | 2 | replaced |
| 61 | `s-bench` | Benchmarks saturate, then get replaced | 0 | replaced |
| 62 | `s-openweight` | You can run the frontier locally | 0 | replaced |
| 63 | `s-outsource` | You can outsource cognition but you can't outsource understanding | 0 |  |
| 64 | `s-slopcannon` | The slop cannon is charged whether we like it or not. The only question is how it is aimed | 0 |  |

## The flood sequence (slides 8 to 13)

Flow: `s-hookB` "It started as a drop" (6) → `s-hookA` unit distance (7) →
"Then, a trickle" (8) → "The trickle became a flood" (9) → disciplines,
cascade, picks (10 to 12) → Deep Blue (13). Numbers:
`mathdump-designs/stats.md` (repo cloned 7 Oct).

## 8. `s-md-trickle`: Then, a trickle (3 steps, replaces the old s-flurry table)

Same dark particle look as the flood. Each 2026 result from the old ledger is one labelled dot on a Jan to Oct 2026 date axis:
- the dot's colour is its tier (green T1/T1*, blue T2/T2+, rose T3)
- filled means a Lean artefact exists, a ring means none
- a warm halo and a warm tag mark physics and its neighbours (physics, crypto, PDE, 17 fields)

The tier legend sits at the bottom. Each label fades in as its dot lands, so let the dots fall before you talk.

- **0 (on entry): January to June, four dots drop.** Erdős #728 (Jan, T1, Lean certificate), gauge-theory amplitudes (Feb, T2, physics), unit distance (May, T2, nine mathematicians), jamming exponents (Jun, T2+, Parisi and Zamponi with Claude, refereed in J. Stat. Mech.). Say: "You just saw two of these drops. Here is the whole year. For six months: four."
- **1: July and August, five dots in about four weeks.**
  - Jacobian conjecture (T2). Read the post aloud: "hello there the jacobian conjecture is false thanx". That was the entire announcement. Filled dot: the Lean formalisation of the counterexample was merged 26 Jul.
  - S6 (T3): 108 pages, self-hosted, no arXiv. Say "reportedly" written out by Claude. The PDF names no author and no AI.
  - HAWK-256 (T2, crypto): withdrawn from NIST within a day.
  - Astra (T1*): Lean, under $2k each, zero referees.
  - Zeta zeros (T1): two thirds on the critical line, reproved by hand 2 Sep.
- **2: September.** Navier-Stokes blowup with smooth forcing (T1*, PDE): a Millennium Problem in Lean, OpenAI, 10,000 agents, 12 hours after Buckmaster and Alpöge's Euler blowup, so a priority fight. The old summary line appears: "Generation has been automated faster than verification."
- **3: 6 Oct, the hand-off.** The rose openai/math dot lands (T3, 17 fields). Then 722 small dots pour onto it and stack into a column most of the slide tall. Each dot is one manuscript, coloured exactly as on the next slide. Say: "Two days ago: 722 manuscripts, 372 result families, 26 million lines of Lean, one repo. Referees: zero." Next press goes into the flood: the column lifts off and pours again on the zoomed 10 Sep to 6 Oct axis.
- **Why T3 despite the Lean (if asked):** most of the Lean formalises a fragment, not the headline. So for most headline claims nobody, human or kernel, has checked them. The row says "Lean for 235 families, mostly a fragment".
- **Caveats:** two dates are approximate. The Feb amplitudes dot is placed mid-February. The S6 dot is placed on 24 Jul (it was announced between late July and early August). Labels show only the month, as the old table did.

## 9. `s-md-flood`: The trickle became a flood (4 steps)

The title now answers "Then, a trickle". Slide numbers 9 to 12 are the same as
in this morning's notes (s-md-trickle took s-flurry's place at 8).

- **0**: empty date axis, 10 Sep to 6 Oct, counters at 0. "Every dot will be
  one manuscript, placed by the date in its folder name. Filled means the
  family has a Lean artefact, a ring means none. Warm colours are the three
  physics blocks."
- **1**: the trickle, 7 manuscripts between 10 and 22 Sep. "For two weeks, a
  handful."
- **2**: the torrent: 177 on 23 Sep, 194 on 24 Sep. Counters race. **Pause and
  let it fall.**
- **3**: the rest arrives day by day, including 112 on 5 Oct. "51% landed on
  23 and 24 Sep." Counters stop at 722 and 372.
- **4**: 34,815 PDF pages and 26.0M lines of Lean count up. "About 4,000
  problems posed, about 3 hours of compute per result."
- (The 24 Sep column has 194 dots: 193 dated folders plus one ISO-named
  folder.) **R** replays the pour.

## 10. `s-md-disc`: 17 disciplines (2 steps)

- **0**: the particles flock into 17 discs sized by manuscript count. "This
  is not a niche dump. It is all of mathematics."
- **1**: the physics blocks glow (probability and stat mech, mathematical
  physics, operator algebras): "73 families, 195 manuscripts." This is the
  room's share.
- **2**: Lean coverage per discipline. "Often a fragment, not the headline.
  MUB(6) = 3: the Lean covers only N(6) at most 5."

## 11. `s-md-cascade`: What survives the checks (4 steps)

- **0**: about 4,000 problems posed (the column runs off the top, about three
  screens tall) next to 372 families.
- **1**: families split into 722 manuscripts.
- **2**: families with any Lean artefact: 235. "Lean artefacts are often a
  weak fragment: a lemma, a finite case, a corollary."
- **3**: headline fully in Lean: a handful, by hand count (273, 274, 275,
  287, 288, 295, 296 and a few more; only the physics blocks were checked).
- **4**: the red 0 slams in: refereed by anyone, as of 7 Oct. **Stop talking
  for a beat.**

## 12. `s-md-picks`: The physicist's picks (5 steps)

- **0**: the whole corpus as one band in family order. "The warm stretch is
  the physics." Theorem statements read from the LaTeX; proofs skimmed, not
  checked.
- **1**: 265 2D area law (Lean: section 2 only) and 268 spin-1 Haldane gap (no
  Lean, computer-assisted, L at least 60). Plant a seed: "Remember 268. We
  will come back to it."
- **2**: 271 Heisenberg ferromagnet (Lean: order only) and 269 Laughlin 1/3
  gap (Lean: no disorder, computer-assisted).
- **3**: 266 MUBs in dimension 6 (Lean: N(6) at most 5 only; the exclusion of
  four bases is a binary64 computation) and 273 entropy photon-number
  inequality (Lean: headline).
- **4**: 274 parity not in QAC0 (Lean: headline) and 275 QMA-hard Coulomb
  energy (Lean: both theorems).
- **5**: "3 of 8 have the headline in Lean. The rest need a referee." At CQT
  someone in the room is a natural referee for most of these; say so.

**(removed) `s-md-close`.** The reactions slide (Sutherland, Isaac Kim,
Advisory Group, "the bottleneck moved...") is gone. If you want one reaction,
say it over picks step 5: Sutherland (MIT), "treat any claims about
one-shotting problems with a single agent as unverified. We should ask for
receipts." The "adjudicating" line now lives in Deep Blue step 3.

## 13. `s-deepblue`: Deep Blue comes to mathematics (4 steps)

Sits right after the mathdump block, before `s-arxivack`. It is the reflective close of the flood sequence: after the numbers, name the feeling in the room.

- **0**: title, the definition card and the source line. "Simon Willison, who writes the best running commentary on LLMs, put a name to this in February. The term comes from the Oxide and Friends podcast, and he gives primary credit to Adam Leventhal. Deep Blue is the ennui, sliding into existential dread, of watching a machine do what you spent years learning to do." Read the quote: "What am I even for?" He wrote it about software engineers. "Two days ago it became our word too."
- **1**: left column, 1997 chess. "May 1997, New York: IBM's Deep Blue beats Kasparov three and a half to two and a half. Kasparov resigns game 6 after 19 moves. Calculation, the skill that defined chess mastery, stopped being scarce. And then? The engine became every player's coach. People still play people."
- **2**: right column, 2026 mathematics. The dots cascade in, one per manuscript (about a second; let it land). "6 Oct 2026: 722 manuscripts, 372 families, 17 disciplines, 26 million lines of Lean. The amber dots are the three physics blocks, 195 manuscripts. Proving stops being scarce. In the pile are our problems: the spin-one Haldane gap, the 2D area law, parity not in QAC0. And then? That is being decided this week."
- **3**: the crack runs down the mirror. The dots go hollow and two pills appear. "This is where the analogy breaks. When Deep Blue won, anyone could check the result on the board right away. Mathematics has no scoreboard. It has a referee queue, and of these 722 the number refereed so far is zero." (This carries the point of the removed `s-md-close`: the bottleneck is now adjudication.)
- **4**: Willison's consolation and the turn. Read the quote: "All of the chess players and the Go players went through this a decade ago and they have come out stronger." Willison corrects himself in the post: Deep Blue was 1997, so it was more than a decade ago. Then the summary: "In chess the engine became the coach. That is the use of agents I want to show you." This sets up the magic trick: agents building custom interactive learning aids (slides 53 to 58).

Caveats and background, if asked:
- Willison's own experience: in early 2023, ChatGPT Code Interpreter did in a couple of prompts the data clean-up and analysis that had been on his roadmap for years. He had two thoughts at once: a huge breakthrough for journalists, and "what was I even for?". In the transcript he says you are still useful even though memorising syntax is now irrelevant, and that the experience people have built up has not gone to waste. The mathematical version: grinding out a lemma is no longer scarce, but taste, judgement and checking still are.
- "26.0M lines of Lean" does not mean the headlines are verified. Most of the Lean formalises a fragment. That is why step 3 says refereed 0, not verified 0.
- The board is a gesture, not the final position of game 6: a toppled black king (Kasparov played Black) and a standing white king.
- The 1997 match facts are from general knowledge, not a fetched page.

## 14. `s-arxivack`: LLM acknowledgments in quant-ph and math-ph (no build steps)

- "We took a random sample of arXiv submissions, read the full v1 text, and asked one question: does the acknowledgment say an LLM helped? Every hit was read by hand."
- "quant-ph: zero through 2023. Twenty-seven percent in the first three weeks of September."
- Point at the faint marker: "And this morning's update: the first week of October, 47 of 120 quant-ph papers, 39 percent. Faint because it is one week, not a month." (Window 1 to 7 Oct; listings pulled at 10:00 SGT today, so papers submitted late on 7 Oct are not in it.)
- math-ph that week is 11 of 41 = 27%. 41 is every primary math-ph submission that week, so the interval is wide (16 to 42%). Do not claim a math-ph rise from it.
- Caveat, say it once: this is a disclosure rate, not a usage rate. Real usage is higher.
- If asked what they disclose: in October 46 of 58 disclosures credit the LLM with research content (proofs, derivations, literature), not copy-editing. Example, arXiv:2610.02050: "The technical details leading to the proofs of our results were largely developed by GPT-6, with minimal human input."

## 15. `s-ackexp`: same data, log axis (no build steps)

- "On a log axis the hockey stick is a straight line. The rate has doubled every 2.8 months since the first hit (95% CI 2.3 to 3.5)."
- "This line was fitted on 22 September. Here is the test: it predicted 28% for the first week of October. The week came in at 36%, interval 29 to 44. The prediction is below the interval. No bend yet; if anything it steepened."
- If asked: with October included the doubling time is 2.6 months (2.2 to 3.2). The fit deliberately stops at 21 Sep so October is an honest out-of-sample check.
- Possible driver, as an observation only: 24 of the 58 October disclosures name GPT-6 or "Astra", against 8 of 50 in September.

## 16. `s-acksing`: the Acknowledgment Singularity (satire, no build steps)

- "Take the straight line literally. Every paper thanks an LLM by March 2027. Ten per paper by December 2027. By October 2034 each paper thanks one model per living human."
- "The only serious reading: a disclosure rate has a ceiling, so the line must bend within months. And the first week of October landed above it, not below." (Point at the faint grey point just under the star.)
- Milestone dates are unchanged from the 22 Sep version because the fit is unchanged (October is not in it).

## 17, 18. `s-control`, `s-scatter`

Unchanged; 23 Sep notes. Keep short.

## 19. `s-grief`: The timeline (6 steps, one more than before)

- **0**: the empty spine with year separators. Kicker: software engineering, Nov 2022 to Aug 2026. "This is the arc software engineers went through. The colour of each date is the mood people were showing in public: cyan shock, red anger, blue bargaining, dark teal depression, green acceptance."
- **1**: Nov 2022 ChatGPT, Feb 2024 Huang ("nobody should learn to code"), Mar 2024 Devin. Shock, then anger.
- **2**: Apr 2024 Devin debunked, Feb 2025 Claude Code plus "vibe coding" (the second cyan dot is the real shock), Mar 2025 Amodei "90% of code". "Notice the red dot after the blue one: the stages don't run in order."
- **3**: Jul 2025 METR, experienced developers 19% slower. "The great comfort."
- **4**: Dec 2025 Stack Overflow down 78%, Feb 2026 METR retires the study: "19 months of comfort, retired by its own authors."
- **5**: Jul 2026: review time +441%, and hiring comes back but split in two. "The bottleneck didn't go away. It moved, from writing code to checking it."
- **6 (new)**: Aug 2026: Cursor, an AI code editor, sold for $60B (SpaceX bought it on 14 Aug). "And the market agrees: 60 billion dollars for a code editor whose product is an agent." Do not dwell on it; the next slide is the payload.
- Caveat if asked: the ticks are evenly spaced, not to scale. The Cursor figure comes from CNBC and Forbes reports (the 2 Sep news sweep); it is a reported acquisition price, not re-verified today.

## 20. `s-mathslag`: The lag collapsed: from three years to three months (6 steps)

- **0**: the two lane labels. "Same arc, other field."
- **1**: the six software cells, the arc you just saw: Copilot, Devin, Claude Code, "better than I expected at my job", Opus 4.5 past 80% SWE-bench, and Jul 2026 review time +441%.
- **2**: maths cells 1 to 3: Jul 2024 AlphaProof IMO silver, Oct 2025 "ten Erdős problems" (retracted, the Devin moment), Jan 2026 Erdős #728 with model, Lean, human (the Claude Code moment: the loop closes).
- **3**: maths cells 4 to 6 plus the highlighted last column: May 2026 unit distance (Gowers: "Annals, no hesitation"); Sep 2026 GPT-6 Astra goes public on 3 Sep (vendor-reported 97.6% on FrontierMath Tier 4, the counterpart of SWE-bench saturating) and the Navier-Stokes claim in Lean on 8 Sep; 6 Oct, two days ago: 722 manuscripts, zero refereed.
- **4**: the offsets and the wedge: 37, 19, 11, 12, 10, 3 months. "At the August talks I said eighteen months, and then about nine. Today the newest pair is three months apart. Software found out in July that review is the bottleneck. Mathematics found out on Tuesday."
- **5**: You are here, 8 October 2026, Singapore.
- **6**: "Offset about 3 years in 2024, about 10 months in September, about 3 months now." Second line: "Both fields now wait on the same thing: a human to check. In quant-ph, 27% of September papers already thank an LLM." Tie it to the room: this is CQT's own arXiv category.
- Caveats, say them if challenged:
  - The 3 months uses the date Faros put a number on the review crunch (Jul 2026). Engineers felt it from 2025 (DORA); counted from then, the last offset is nearer a year. The claim that holds either way: the two fields now hit the same bottleneck in the same season. Safer fallback wording if challenged: "The lag collapsed: same bottleneck, same season".
  - Offsets are whole calendar months between the two dates. The beats are pairings I chose, not a measurement, and the 11 to 12 bump is left in on purpose.
  - Dropped since 23 Sep: ChatGPT and IMO gold (it repeated the first column's 3 years). The Aug 2026 Astra ten-problem result now appears only on `s-md-trickle` (slide 8).
  - 27% is quant-ph v1 submissions from 1 to 21 Sep (28 of 103, CI 19.5 to 36.5%). It is a disclosure rate, not a usage rate.
  - GPT-6 Astra's 97.6% is OpenAI's own figure, and Navier-Stokes is Lean-checked but not refereed (T1* on `s-md-trickle`).

## 21 to 52. Parts Two to Four

`s-capable` (21) now reads "Progress is astonishing. Let us understand them."
`s-defense` (51) is retitled "Defense in depth". Otherwise use the 23 Sep notes
by id. Given today's message: move quickly through 22 to 37 (what an LLM is,
the illusion of chat, the failure zoo; one sentence on hallucinations is
enough for this room) and spend the time on Part Four, the agent (38 to 52),
which leads straight into the Haldane interlude.

## The Haldane interlude (slides 53 to 58): the magic trick

Six slides after `s-dagx` (end of Part Four), before the divider `s-div6` (59).

**What the segment is for.** This is the magic trick: agents are great at helping you *understand*. One of the 722 manuscripts became a bespoke interactive learning aid. Do not teach the proof. Show the aid, let two or three live numbers land, then be honest about the fine print.

**Time.** About 8 to 9 minutes in full. Under pressure, about 4 to 5 minutes:
- **CORE:** `s-hg-intro`, `s-hg-worldlines`, `s-hg-flow`
- **RECOMMENDED:** `s-hg-square` (it holds the paper's one new idea)
- **SKIPPABLE:** `s-hg-spotlight` (tap through in 15 s with one sentence), `s-hg-fineprint` (tap to the last row and read only the verdict, but do not drop it entirely: it is the honesty)

**Keys.** Arrows and space work as in the rest of the deck. Bonus keys work only while a Haldane slide is showing, and not while the `?` help is open:
- `[` `]`: β on slides 54 to 56, u₀ on slide 57
- `-` `=`: n on slide 55, C on slide 57
- `M`: cycles the Trotter slices on slide 54

The `?` overlay has a row listing these keys. Let each animation land before you talk over it: ticks 2.6 s, the board turn 0.9 s plus a 1.3 s sweep, β and n moves 1.1 s and 1.8 s, the square's routes 2.2 s, the 14 hops about 5.3 s.

## 53. `s-hg-intro`: Agents are amazing at helping you understand (2 steps) [CORE, about 1 min]

- **0**: "One of the 722: family 268, a proof that the spin-1 Heisenberg ring has a Haldane gap." This audience knows what that would mean. Say so in one breath, no more.
- **1**: how it was made.
  - "Yesterday one agent refereed it from the LaTeX in a single pass and re-ran the paper's exact-arithmetic checks."
  - "Then three agents, in parallel, each turned the paper, that referee report, an explainer and a one-page brief into a five-slide interactive explainer."
  - "All three were back within 40 minutes. I picked one."
  - Caveat: the 40 minutes runs from the commit of the prompts (18:34 SGT) to the commit of the last design (19:12:56 SGT), per git. The real session time was a bit less. "About half an hour" is also safe.
- **2**: "Not a recording: the toys on the next five slides compute live, in this browser." This is the trick. Everything that follows was built by agents from the paper.

## 54. `s-hg-worldlines`: One partition function, two readings (3 steps) [CORE, about 2 min]

- **0**: six chalk worldlines on a cylinder of height β = 2, with bond events ticking in. "Z = Tr e^{-βH}. Expand the exponential: a history of bond events on this cylinder." The ticks are an illustration only (the slide says so).
- **1**: slices appear and a scanner sweeps upward. "Read it along time: a transfer matrix on rows of six spins. That is the Gibbs reading." Exact Gibbs sum 657.156; the 8-slice toy lattice gives 681.135416929577.
- **2**: the board turns 90 degrees and the scanner sweeps across bonds. The column transfer matrix (256 states) gives 681.135416929576. **Pause:** "Same number to fifteen digits, computed two completely different ways, live." Then: "The paper does this in continuous time with a real symmetric kernel, so the spectrum is one real list for every n."
- **3**: takeaway: two probability vectors, p_k ∝ e^{-βE_k} over levels and q_i ∝ |λ_i|^n over the transfer spectrum.
- Optional live play: press `M` to cycle the slices M = 1 to 4 and watch the lattice value approach 657.16. `]` raises β.
- Caveats if asked:
  - The toy is spin-½ with n = 6; the theorem is spin 1.
  - The lattice transfer X_e X_o is not symmetric; the paper's continuous-time kernel is.

## 55. `s-hg-spotlight`: Purity as a spotlight (4 steps) [SKIPPABLE, about 1.5 min]

- **0**: β = 0.5 on the 8-site ring. Purity 0.0059 and the beam covers the row. "One number to track: Σ p_k². The spotlight width is its inverse."
- **1**: β moves to 2. Purity 0.105. "Turning β up narrows the beam."
- **2**: β moves to 8. Purity 0.9132 > 7/8, and the ground state is circled "unique". The bound gives γ ≥ 0.294 against a true toy gap of 0.523. "max p ≥ purity. Above one half the ground state is unique, and the first excited level is exponentially suppressed. The bound is loose, and so are the paper's constants."
- **3**: right panel: n goes from 4 to 64 for a classical three-state ring, and S goes from 0.54 to 0.9999. "The same along n, once the ring is longer than the correlation length."
- **4**: takeaway: the whole problem is to show T(L, β) is near 1 with β growing no faster than log(1/u).
- Short version: tap through, and say only the step-2 sentence.

## 56. `s-hg-square`: The square on the blackboard (4 steps) [RECOMMENDED, about 1.5 min]

- **0**: four corners Z₄(3), Z₈(3), Z₄(6), Z₈(6), from exact diagonalisation.
- **1**: the four purities on the edges.
- **2**: two dots take the two routes to (2n, 2β). The cancelling Z's are struck through, and both products print as 0.07563170461608. "Every Z appears once upstairs and once downstairs. Trivial algebra. As far as the explainer knows, nobody used it before."
- **3**: green arrows show the two squarings. Live Lemma 4.1:
  - Gibbs defect 0.2607 at (4,3) becomes 0.0148 at (4,6), against a bound of 0.0621.
  - Spatial defect 0.3482 becomes 0.1427 against a bound of 0.1427 (the bound is saturated for the three-state ring).
  - "Squaring moves T along β and S along n. The identity trades one axis for the other."
- **4**: the takeaway. "This is the paper's one new idea."

## 57. `s-hg-flow`: The flow (3 steps) [CORE, about 2 min]

- **0**: the (n, β) plane on log axes, with the seed circled at (60, 105/4) and the paper's "S, T > 7/8".
- **1**: fourteen diagonal hops animate. The ledger fills, and the gap-bound plot flattens onto (4/105) log(80/79) = 4.79·10⁻⁴, **the theorem's own constant**. "Defects go u, Cu², C³u⁴. β only doubles. With the paper's seed numbers the bound lands on the theorem's constant. Notice that it takes eight doublings to get going: the margin is thin."
- **Optional live moment (strong, 10 s):** press `]` once. u₀ becomes 0.141, just above 1/C = 0.127. The hops turn pink, the defects pass 1, and the ledger reads "C u₀ ≥ 1: no gap bound". "One notch above the paper's seed and the machine stalls." Press `[` once to get back exactly to 1/8.
- **2**: the hatched critical patch. "For a gapless chain both purities are functions of vβ/n. You cannot have both near 1: vβ ≫ n against n ≫ vβ. Best compromise: defects of 0.3 to 0.5, far above 1/8. For a gapped chain the two demands decouple."
- **3**: takeaway: a finite ring that looks gapped on both axes with margin 1/8 looks gapped at every larger scale. Hölder fills in the even sizes in between.
- Caveats:
  - u_{j+1} = C u_j² is the explainer's simplified recursion; the paper's Prop 4.3 bookkeeping differs at finite j. The j → ∞ limit is exactly the paper's constant.
  - The critical patch is a sketch, and 0.3 to 0.5 is the review's estimate.

## 58. `s-hg-fineprint`: The fine print (5 steps) [SKIPPABLE except step 5, about 1 min]

1. Theorem 1.1, spin 1, periodic, even L. Constants 4.8·10⁻⁴ for L ≥ 60 and 3.8·10⁻³ for L ≥ 2304; hence liminf γ_L > 0.
2. Scope: even periodic rings and the liminf only, not every infinite-volume ground state. "The true gap is about 0.41. The constants are a thousand times smaller."
3. Seeds: "This is where the labour is."
   - Exact Z_n for n ≤ 10 at β = 21/2, an MPS with D = 26, and a 5/2-power raise of β.
   - The margin is only 6·10⁻⁴.
4. Verification:
   - No Lean.
   - The exact-rational scripts were re-run and pass.
   - Z₁₀(21/2) and n = 10 to 12 at 49/4 are unverified.
5. Verdict: "One referee agent, one pass: no mathematical error found, 85 to 90 percent that it is proved as written. If a bug hides anywhere, it is in the seeds, not in the doubling."

Close the segment with: "That is what I mean by agents helping you understand. Forty minutes, from paper to a working, honest, interactive explainer." Then go to the Part Five divider.

**General caveats.**
- The toys are spin-½, labelled as toys on every slide. The theorem is spin 1 (not spin-½, as one brief said).
- Every number on slide 58 is the paper's or the referee agent's, except the true gap of about 0.41, which comes from the explainer.
- Theorem 1.1 wording on slide 58 is the review's paraphrase, not the paper's LaTeX verbatim.
- The chalk SVG filters cost GPU. Step through 54 to 57 once on the presentation laptop before the talk.

## 59. `s-div6`: The trend

Divider; unchanged.

## 60. `s-eci`: Capability is a straight line (3 steps, 0 to 2)

Numbers: Epoch snapshot 8 Oct 2026, **272 measured models** (up from 221), frontier trend **+14.1 ECI points per year** (up from 13.1), measured leader **Claude Opus 5.5 at 167.3** (22 Sep). The open-weights leader is **Kimi K3 at 157.5**, **4.4 months** behind.

- **0**: cloud, envelopes, blue rings for everything released since 19 Aug, and the name ladder (Opus 5.5, GPT-6 Astra, GPT-6.1 Sol, Claude Sonnet 5.5, Fable 5.1, GPT-6 Sol, then the mid-tier). Say: "Every dot is an Epoch measurement in one harness: open and closed models, measured the same way. The top of the frontier is Claude Opus 5.5 at 167, with GPT-6 Astra and GPT-6.1 Sol right behind."
- **1**: the dashed straight line, "+14.1 ECI points per year", and the open-weights arrow, "about 4.4 months behind (Kimi K3)". Say: "No ceiling and no bend. Open weights are about four and a half months behind."
- **2**: the hollow dashed black circle with "?" at **6 Oct 2026, ECI about 171, band 168 to 175**, labelled "openai/math model (unreleased), speculative". The note box appears bottom right.

  **Say:** "That last dot is not on the bus timetable. It is the model behind the 722 manuscripts, and nobody outside OpenAI can use it yet."

  **Three spoken caveats:**
  1. "This dot is not a measurement. OpenAI published no benchmark scores for this model. I placed it using their own words, 'significantly more capable than GPT-6 Astra', and the size of their past model-to-model jumps. Read it as roughly one generation ahead of what you can buy."
  2. "It is a system, not just a model. Each result got about three hours of top-tier thinking, the results were picked from about four thousand attempts, and OpenAI decided what counted as significant. ECI scores models on fixed benchmarks in a standard harness, so the comparison is loose."
  3. "None of the 722 manuscripts has been refereed. In the first 48 hours nothing has been confirmed or refuted. A Lean check proves the formal statement, not that it is the statement you wanted, and the Navier-Stokes 'forcing loophole' shows the difference."

  **Optional, one line, honest about our own track record:** "Last month I showed Astra, Fable 5.1 and Opus 5.5 as estimates from vendor scores. Epoch has now measured them, and all three came in 2 to 6 points higher than my estimates." (Opus 5.5: 161.6 estimated, 167.3 measured.)

  **If asked "how far ahead?":** "About 4 to 5 ECI points above Astra, about 4 above Opus 5.5. At about 14 points a year, that is roughly four months of frontier progress."

  **If asked about the Erdős problems:** On Epoch's FrontierMath Erdős benchmark (68 hard open Erdős problems, solutions must be in Lean, $300 per attempt), GPT-6 Astra solved 2 and every other model solved 0. The openai/math dump claims at least 3 of those 68: #3 (the $5000 Erdős-Turán arithmetic-progressions problem), #138 (van der Waerden numbers) and the Hadwiger-Nelson value 5. All three are unrefereed, and the compute budget is different.

  **Do NOT say** "the frontier leader is Claude Fable 5 at 162" or "Astra, Fable 5.1 and Opus 5.5 are estimates". As of 8 Oct, Epoch has measured all three, and Opus 5.5 leads at 167.3. The ARC-AGI-3 aside about Astra is gone from the slide. Mention it only if asked: 99.9% in OpenAI's own harness, 62.7% in ARC Prize's standard harness.

## 61. `s-bench`: Benchmarks saturate, then get replaced (no steps)

None of these numbers changed since 22 Sep: GPQA Diamond is dead at **95.8%** (GPT-6 Astra, 3 Sep), HLE is at **54.8%**, CritPt (research physics) is at **32%** (GPT-5.6 Sol, 9 Jul), and the original FrontierMath tiers are frozen at **52%** (GPT-5.5 Pro, Apr) because Epoch moved to v2. The snapshot date is now 8 Oct. Bridge line, if you want it: "OpenAI says its internal model saturated their own math evaluations. That is exactly this picture, one level up."

## 62. `s-openweight`: You can run the frontier locally (no steps)

Same story with fresh data. The median lag since 2025 is **5.3 months** (the figure title rounds it to "about 5"). The latest record is Kimi K3, **4.4 months** behind (that is the number on slide 60; say which one you mean). Qwen 3.8 27B is now Epoch-measured at **ECI 149.4**, about where GPT-5 was in Aug 2025. Its 22 Sep vendor-based estimate was 153.7, so do not quote that. "Fits one 24 GB consumer GPU when quantised" still stands.

## 63, 64. `s-outsource`, `s-slopcannon`

Unchanged. 63 is the payoff of today's thread: "You can outsource cognition, but you can't outsource understanding." Point back to the Haldane slides: the agents did not understand it for you; they built you a better way to understand it yourself.

## If asked (openai/math)

- Family 157 is a counterexample claim: it "disproves Hadwiger's conjecture
  even for fractional colouring" and has a Lean docs page. Some press got this
  wrong; the repo is the source of truth.
- Headline results OpenAI promoted (quasi-Riemann hypothesis, Unique Games,
  rational Hodge for CM abelian varieties, free group factors): no external
  confirmation reported as of 7 Oct (secondary sources only; do not overstate).
- Compute, cost, prompts and the model itself are undisclosed beyond "about
  3 h per result" and "unreleased internal model".
- Reactions (the slide that carried them is gone): Isaac Kim on X, "a shocking
  list of problems in quantum information, many-body physics and quantum
  computing"; Advisory Group on Mathematics and AI (29 Sep), "mathematical work
  should not be used as a marketing tool".
