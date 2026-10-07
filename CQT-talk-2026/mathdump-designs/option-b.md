# Option B: The Night Sky

**Pitch (150 words).** The mathdump as a star chart. Each of the 372 result families is a star; the 17 disciplines are constellations. Size is papers per family; bright and solid means a Lean doc exists, faint and flickering means none. The sky fills in date order, so the 23 to 24 Sep burst lands as a sudden swarm of new stars. Famous problems get star names in small caps, then a second layer recolours them by what Lean actually covers. The live beat is a camera zoom into one faint star, family 265, the 2D area law: it splits into two papers, then into its proof skeleton, then lights the one formalized section. For a quantum audience this turns "has Lean" into a precise question about their own field. Bonus: a magnifier lens follows the mouse and names the nearest star. Risks: label density on slide 3; the time-lapse needs one press of patience (about 7 s).

Spoken cue (keep off the slide, it is an unverified paraphrase): Sam Altman reportedly said he was "looking up at stars with extra awe tonight" when the repo dropped.

## Slides and build steps

**1. `s-md-sky` (3 states)**
- 0: Dark sky, four numbers: 722 manuscripts, 372 families, 17 disciplines, 26.0M lines of Lean. Empty date strip. Say: "One repo, two weeks."
- 1: Time-lapse (about 7 s). Stars appear in directory-date order with a date ticker; 23 and 24 Sep explode. Say: "Half the papers are dated in two days."
- 2: Legend (size = papers, bright = Lean doc 235, faint = none 137) and the strip labels "23 to 24 Sep: 370 papers, 51%" and "5 Oct: 112".

**2. `s-md-constellations` (2 states)**
- 0: All 17 constellations labelled with family counts. Point at Topology (few bright stars) and Logic (all bright): Lean coverage is visible as brightness.
- 1: The rest dims; constellation lines draw for Probability & stat mech (29 families, 105 papers, 19 with a Lean doc), Mathematical physics (25, 59, 17), Operator algebras (19, 31, 14). Say: "This is where this room lives."

**3. `s-md-names` (3 states)**
- 0: The sky.
- 1: 21 of the 48 famous problem names fade in next to their stars (quasi-Riemann 7/8, Hilbert's tenth over Q, Unique Games, Hadwiger, Haldane gap, L(F2) = L(F3), MUB(6) = 3, parity not in QAC0, Kadison similarity, hot spots, De Giorgi ...).
- 2: Verification layer. Green: headline in Lean (5: 273, 274, 275, 287, 288). Amber: only a fragment (5: 261, 265, 266, 267, 271). Blue dashed: a Lean doc exists but we did not check its scope (8). Rose: no Lean (3: 004, 268, 375). Say the bottom line aloud: "A Lean doc does not mean the headline theorem is checked."

**4. `s-md-zoom` (4 states; the live moment)**
- 0: The sky dims, a reticle marks family 265, "2D area law, 2 papers, no Lean doc".
- 1: Camera zooms (1.1 s ease-in-out) into the star; it splits into two papers (area law; polynomial PEPS) with Theorem 1.1, S(A) <= C|dA|, global gap only, no lean/docs entry.
- 2: Zoom into paper 1: the proof skeleton in reading order, sections 2 to 10 to Theorem 1.1 (tilt lemma, positive replacement, replicas + Kubo-Ando, norm comparison, scanner, amplification, tiling).
- 3: Section 2 lights green: `uniform_subvolume_square`, about 24k lines, 0 sorry, proves S(box of side r) <= C r^(1+e). Everything else goes dashed: not formalized. Say: "Lean checks a subvolume bound. The area law rests on the unchecked rest."

**5. `s-md-coda` (4 states)**
- 0: Camera zooms back out to the whole sky (1.2 s); "372 families. 722 papers. 0 refereed."
- 1: "The bottleneck moved from producing claims to adjudicating them."
- 2: Andrew Sutherland (MIT): "...treat any claims about one-shotting problems with a single agent as unverified. We should ask for receipts."
- 3: Daniel Litt (Quanta, 5 Oct 2026): "The existing equilibrium has broken. We'll have to find a new one."

Mouse (optional, any sky state): move the mouse and a lens magnifies the sky and shows the nearest family's number, discipline, title, paper count and Lean-doc status. It hides itself after 3 s without movement. Click on the right of the stage still advances.
