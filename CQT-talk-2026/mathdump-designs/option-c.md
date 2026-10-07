# Option C: "Receipts"

**Pitch.** Andrew Sutherland said "we should ask for receipts", so the sequence is a receipt. Paper-white, ink-black, one hot vermilion. Huge tabular numerals in Merriweather Sans (inlined), monospace ledger lines, and a black ticker band that the till roll prints out of. The data never sits still: lines type in, counters roll, stamps slam onto claims. One slide is pure delight. 372 faces, one per result family, watch the mouse. Faces with a Lean document have their eyes open. Faces without one keep them shut. A key press dims the 137 shut-eyed ones, and the next press lights up mathematical physics and operator algebras. Click any face to read its claim on the band. It suits CQT because it ends on the physics picks, each stamped with what Lean actually checks. Risks: the faces could upstage the point. The paper-white look breaks from the dark interludes. Live typing needs the speaker to wait about 4 s on slide 1.

## Slides and build steps (speaker drives with the right arrow)

**1. s-md-receipt "The mathdump, itemised."** (maxSteps 1)
- Enter: the receipt prints up out of the ticker band, about 4 s. Nine lines type in with rolling numbers: 722 manuscripts, 372 families, 34,815 pages, 128.3M LaTeX characters, 26.0M lines of Lean, 12,928 bib entries (403 citing the release itself), about 3 h per result, about 4,000 problems posed. The ticker scrolls the famous problems named in the headings. *Say:* "Here is what we were sold."
- Step 1: the total feeds out: REFEREED, a red 0 that stamps down, and "please keep your receipt". *Say:* "And here is the total."

**2. s-md-faces "Which ones has Lean seen?"** (maxSteps 2, the live beat)
- Enter: 372 faces in family order. They glance at the title, then look at the audience. Move the mouse and every face follows it. Faces with a Lean document blink now and then. *Do:* move the mouse around. Click a face (say 268 or 265) to show its claim and Lean status on the black band.
- Step 1: "show me the checked ones". The 137 shut-eyed faces fade, and the rest glance at the 235. *Say:* "Open eyes means a Lean file exists. Often it covers a fragment, not the headline."
- Step 2: mathematical physics (25, red, 17 with Lean) and operator algebras (19, black, 14 with Lean) pop out. Everyone else looks at them.

**3. s-md-days "Stacked by day."** (maxSteps 2)
- Enter: one square per paper, columns stacking day by day from 10 Sep to 6 Oct. The towers are 23 Sep (177) and 24 Sep (193).
- Step 1: those two towers turn red, the rest dim, and a giant "51%" appears: "of the corpus is dated 23 to 24 September". The ticker repeats it.
- Step 2: 25 to 27 Sep and 4 to 5 Oct come back. "78% dated 23 to 27 Sep (564)", "19% dated 4 to 5 Oct (136)".

**4. s-md-ladder "How far up has it climbed?"** (maxSteps 5; the ticker lists what AGMAI asked labs to disclose)
- Steps 1 to 4: each rung stamps in and its numeral rolls up. CLAIMED 372. A LEAN FRAGMENT EXISTS 235. HEADLINE THEOREM IN LEAN 13 (273 274 275 279 287 288 292 293 295 296 297 298 299, by hand count, physics and operator algebra blocks only). REFEREED 0, in red.
- Step 5: a red rubber stamp, "ASK FOR RECEIPTS", Andrew Sutherland, MIT.

**5. s-md-picks "Eight claims, itemised."** (maxSteps 3)
- Enter: eight receipt lines print with a stepped print-head sweep: 265, 268, 271, 266, 273, 275, 274, 287.
- Step 1: red outline stamps land on the weak four: fragment only / none, computer-assisted / existence of order only / only N(6) ≤ 5 in Lean. *Say* why each one matters to this room.
- Step 2: solid black "headline in Lean" stamps land on 273, 275, 274 and 287.
- Step 3: the total, "headline in Lean: 4 of 8 · refereed: 0 of 8", and the line "A full Lean proof certifies a formal statement. Checking that it says what the paper claims is still our job."

**6. s-md-close "Received with thanks"** (maxSteps 3)
- Enter: Isaac Kim's quote types out ("a shocking list of problems in quantum information...").
- Step 1: Sutherland's quote types out ("...treat any claims... as unverified. We should ask for receipts.").
- Step 2: AGMAI: "Mathematical work should not be used as a marketing tool."
- Step 3: under a heavy rule: "The bottleneck moved from producing claims to **adjudicating them.**"

Integration: copy everything between `<!-- BEGIN MATHDUMP SLIDES -->` and `<!-- END MATHDUMP SLIDES -->` into talk.html's `#stage`. The CSS is scoped to the six ids. The single script registers on DOMContentLoaded and self-starts if the deck opens on one of these slides. `?still` renders every final state.
