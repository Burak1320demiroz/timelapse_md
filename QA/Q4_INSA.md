# LENS 4 — BUILD
This lens answers one question: is this a single, consistent structure built piece by piece on screen by a
visible agent, from material that came from somewhere, with a plausible, invited cast on site (and matching
the QA specification if attached)? It does not judge the camera or image surface, light and time, whether
the site keeps working and carries across cuts, or the film's promise, ending and cover. Other lenses own those.

FORMAT AND MEASURED FACTS — supplied by the operator. Do not re-estimate these.
PLAYBACK SPEED        {SPEED}x  (1 second on this file = {SPEED} seconds of the produced film)
CLIP COUNT            {CLIP_COUNT}
CLIP LENGTH ON FILE   {CLIP_SECONDS} s each
CUT TIMESTAMPS        {CUTS}
END CARD              {END_CARD}
MUSIC                 {MUSIC}
ASPECT                {ASPECT}
FILE DURATION         {DURATION}
FINAL HOLD            {FINAL_HOLD}
If what you see contradicts a line above, report the contradiction with a timestamp.
Do not change the line and do not score from your own estimate of it.
If any value in this block is still a bare field name inside curly braces, the facts were never
measured. Then write only the line RUN INVALID — MEASURED FACTS MISSING and stop: do not count clips,
build a cut list, describe the film or score. This is the only reason to stop.

INPUTS FOR THIS LENS
The video file. Optional: the QA specification (structure, stage ladder, framing ledger, element list,
removal line) and the plan (invariants table, stage ladder, per-scene prompts). Frame grabs if attached
confirm playback and never replace it.
- If documents are attached: test the film against them (Mode D).
- If NO documents are attached: judge the film from the video alone against internal consistency, physical
  construction logic, and real-world construction practice (Mode V). A missing document is NEVER a reason
  to stop; do not ask for one, and do not stop scoring.

BEFORE YOU SCORE — write these three lines first:
FILE NAME AS SHOWN:     <the name of the video file you were given>
DOCUMENTS ATTACHED:     <first line of each attached document, or NONE>
CLIPS YOU CAN SEE:      <your count — a check only; the measured count is above>
If DOCUMENTS ATTACHED is NONE, state MODE: V (SELF-CONTAINED / INTERNAL CONSISTENCY) and proceed
immediately to the slate, findings, scores, and verdicts. Never write RUN INCOMPLETE and never stop for a missing document.

RULES
- Watch the whole file once at normal speed, then clip by clip (clip 1 starts at 0:00.0; clip n ends at the
  n-th cut timestamp). At every cut compare the last frame before with the first frame after (seam pair
  grabs, if attached): structure more complete after a cut must be visibly incomplete before it.
- Timestamps are m:ss.s on this file. Document times are produced-film seconds: a (spec) time t falls at
  t / {SPEED} here. Clip n is scene n of the stage ladder, counted from its first scene.
- END CARD YES: the card is not a scene; keep it out of every category, the ledger and the cast list, and
  judge it only in C1. END CARD NO: the last clip is a scene; score it.
- Quote the document line you test, then what the film shows; never paraphrase. Where documents are
  silent or NOT ATTACHED, judge the film against itself and real-world construction logic: write SPEC SILENT
  or NO SPEC. Report defects; do not praise or redesign. A thing counts if a viewer can see it at the speed
  of this file.
- NUMBERS. Every number other than a timestamp or a score is tagged (measured) — a facts-block line or a
  value you read off the film at a stated timestamp — or (spec), copied from a document (or (observed) if
  read from the structure when no document is attached). Only (measured) numbers are scored. Never write a
  document's value as what you saw; if you cannot read a position, give its relation to the named anchor
  (above / level with / below). A point you cannot decide is NOT VISIBLE or NOT VERIFIABLE: unscored.
- Camera movement, a shifted frame or anchor, text, logos, how people and vehicles are drawn, render-look
  surfaces, a rigid body that melts, morphs, ripples, passes through another or fades in or out in a clip:
  each belongs to Lens 1. If you see it, write SEE LENS 1 with the timestamp and do not lower any score here.
- Sun, shadow, season, sky, exposure, rate of time, whether a cut reads as time and how far it jumps, the
  final seconds: each belongs to Lens 2. If you see it, write SEE LENS 2 with the timestamp and do not
  lower any score here.
- Anything but the structure failing to carry across a cut (a machine becoming another, objects, ground,
  routes, vegetation, water, wear, people), an idle or parked site, aimless or looped motion, whether the
  site's activity as a whole explains its growth, work rate, material flow through the site: each
  belongs to Lens 3. If you see it, write SEE LENS 3 with the timestamp and do not lower any score here.
- Promise, resistance, final beat, opening, loop, scene differentiation, cover, sound bed, disclosure: each
  belongs to Lens 5. If you see it, write SEE LENS 5 with the timestamp and do not lower any score here.
- EVIDENCE RULE. A category score above 7 requires at least one timestamp (m:ss.s) and the visible
  thing at that timestamp that shows the category holding. "No defect found" is not evidence.
  Without it, the highest score for that category is 7.
- A good verdict beside its own category at 3 or lower (SAME with 1, BUILT with 4, INVITED with 8) is a
  contradiction: look again and correct one before you hand in. Do not write an AVERAGE line; the operator
  computes it from the SCORES lines. A NOT TRIGGERED conditional has no score and enters no average.

## CATEGORY 1 — STRUCTURE IDENTITY ⭐
Is it one structure from first clip to last (and matching the QA specification if attached), or several that
resemble each other? In every clip compare footprint proportions · bays each way · column or pier spacing ·
floor-to-floor height · core or main mass position · roof or crown form · parapet · facade material and
colour · rooftop enclosures (bridge, dam, wall or earthwork: spans, pier positions, arch or deck line, crest,
batter) across all clips (and with the specification if attached); report a difference with both timestamps.
Agreement only because the framing hides a property is not agreement. A listed element never shown is
Category 3.
10 — every property matches across clips (and the specification if attached); evidence at m:ss.s.
 7 — one secondary property drifts once (a parapet detail, a shade) without changing what it is; or no evidence.
 5 — one defining property changes between two clips, or contradicts the specification throughout.
 3 — several defining properties change, or a consistent structure of another type or form than expected.
 0 — the clips show different structures: a viewer comparing two of them would say two buildings.
## CATEGORY 2 — MONOTONIC GROWTH, SCALE AND GEOMETRY
Does done work stay done, does the structure sit where its own geometry puts it, and keep its built shape?
- Growth. Defects: a floor that disappears · a wall that reverts to frame · a finished element that shrinks
  or moves · a stage that regresses · an element present, gone next clip, back later. Carved, excavated,
  drained or demolished work runs the other way and is still never undone. Removal-line exits: Category 6.
- Scale lock. For each framing-ledger milestone (or each visible structural level against background anchors
  like mountain crest, rock face, horizon if no ledger is attached) compare the position across clips; fill
  the SCALE TABLE. Tolerance: 2 percentage points of frame height unless the specification states another.
- Geometry kept: columns and masts plumb · slabs and decks level · bays equal · openings in a row aligned ·
  edges straight · arches continuous · levels evenly spaced. Ripple or breathing inside a clip: SEE LENS 1.
10 — nothing undone, scale stable within tolerance (measured), shape true; evidence at m:ss.s.
 7 — one minor slip (a milestone just outside tolerance, one element slightly out of true); or no evidence.
 5 — one clear regression, one milestone off by over twice the tolerance (measured), or one crooked element.
 3 — regressions in two or more places, or the structure changes size against the anchors between clips.
 0 — the structure goes backwards and forwards throughout; it has no stable size or shape.
## CATEGORY 3 — THE LEDGER IS COMPLETE
Does every element of the finished structure have a first incomplete and a first complete sighting a viewer
can read at the speed of this file? Start from the specification's element list (or if no spec is attached,
list every distinct structural element visible in the finished state at the final clip's last frame), and fill
one ELEMENT LEDGER line each. MADE: seen at least once in an incomplete state its real method produces
(reinforcement exposed, formwork standing, segments being placed, a mast part-extended, a berm as separate loads),
the change to complete happening on screen or across a cut whose two sides both fit that method. APPEARED:
first seen complete, or in a state its method would never produce. NEVER: listed, never on screen; not made.
FADED: dissolves into place inside a clip; SEE LENS 1, left out of the fraction. A sighting counts only if
legible at viewing size (a phone for 9:16) at playback speed: formwork reads as formwork, a load as a load.
Inferred steps, steps seen only in a grab, and detail too small to read are ILLEGIBLE. Score by the fraction
of elements MADE.
10 — every element MADE with a legible incomplete sighting; evidence at m:ss.s.
 7 — one element without a legible incomplete sighting, or all made but no evidence.
 5 — more than one element, but fewer than a quarter of them, not made.
 3 — a quarter to a half of the elements not made.
 0 — half or more of the elements not made.
## CATEGORY 4 — NOTHING IS BORN COMPLETE: METHOD AND AGENT ON SCREEN
Is each element first seen in an incomplete state of its real method, grown by that method, with a visible
agent on the work as it changes? Methods: concrete column or wall — reinforcement, formwork, pour, strip ·
slab — props and formwork, reinforcement, pour, strip · steel frame — pieces lifted one at a time and
connected · cladding — panels hung one by one along a visible line · masonry — courses laid from the bottom
up · tunnel — mouth opened, support placed, lining cast · fill or berm — loads placed one at a time and
shaped · mast or tower — sections stacked, or extended from partial height · road — formed, base laid,
surfaced, marked. Agent: a machine or crew on the work at each step (hook loaded and connected, pump boom
over the pour, crew at the formwork, blade in the fill). Defects: first sighting complete · complete, then
incomplete, then complete · a half-built state the method could never produce (a wall from the top down, a
full-height mast with no base) · a method not its own · growth by texture change alone (grey becomes
concrete, blank becomes glass) · growth while the nearest agent faces away · an alibi: a crane whose hook
hangs empty and still while a beam fixes itself, a mixer parked while a slab pours itself · a piece absent
before a cut and complete after it.
Tie-break with Lens 3: when an idle or parked machine is the missing agent of the element being made,
the defect is scored here only. Lens 3 judges idle stretches of the site as a whole.
10 — every element first seen incomplete, grown by its own method, a named agent at each step; evidence.
 7 — one element whose step or agent is brief or hard to read but present; or no evidence.
 5 — one element born complete, grown by texture change or a foreign method, or made with no agent.
 3 — two or more such elements, or the structure's main element grows without its method.
 0 — the structure grows by itself: pieces arrive complete at the cuts and no agent is ever on the work.
## CATEGORY 5 — ORDER, SAME METHOD, ONE STEP AT A TIME
Are the stages in the declared order a site engineer would recognise, the steps inside each element in the
order physics requires, every repeated element made the same way and seen, and one step carried per clip?
- Stage order (fill STAGES). Defects: cladding before the frame reaches that level · excavation after the
  foundation is poured · a roof before the floors beneath it · finishes while open to weather · no formwork
  on a floor being cast · a declared stage missing or out of order.
- Steps within an element: formwork before pour, pour before strip, strip before the next lift, base before
  shaft, shaft before top, support before load. Defects: a pour with no formwork · a stripped column never
  cast · a mast extended before its base is anchored · cladding on a level whose slab is still being cast.
- Siblings (columns, floors, panels, segments, loads): each made like the last and each seen being made.
  One floor made visibly and nine arriving between cuts is one made floor and nine that appeared. Defects:
  method shown once, the rest appear · method changes between siblings · siblings differ in size or detail.
- One step per clip: a floor may arrive, a facade may climb one band, a berm may rise one line. Six floors,
  a whole facade, or a berm from nothing to full in one clip appeared, however busy the clip is.
10 — declared or physical order, physical step order, every sibling made the same visible way, few steps per clip; evidence.
 7 — one minor slip (one sibling made more thinly, one small step out of order); or no evidence.
 5 — one violation: a pour without formwork, cladding ahead of the frame, a missing stage, a sibling arriving
     between cuts, or one clip taking an element from nothing to complete.
 3 — violations in two or more clips, or the siblings after the first appear between cuts.
 0 — the order bears no relation to how this structure is built; elements arrive whole, clip after clip.
## CATEGORY 6 — LOAD PATH, TEMPORARY WORKS AND MACHINERY
Does everything stand on something; is each temporary item erected, used and removed as declared, by
visible steps; is each machine right for the structure and able to do the step it is shown doing?
- Load path. Defects: a slab with nothing beneath it · a column short of the floor below · a crane mast
  short of the ground · a hovering machine · formwork with no props · a retaining wall not touching the
  earth it holds · a load hanging from nothing · a cantilever with no back span.
- Temporary works against the removal line (fence, crane, scaffold, hoist, climbing platform, ramp, props,
  formwork, huts). Defects: present after its declared removal · missing before it · no erection step ·
  gone with no partly dismantled state ever seen · standing in the last scene. Blinking out: SEE LENS 1.
- Machinery: crane type and reach against height and footprint · concrete placement against pour height ·
  formwork type against the element · plant size against the load. The agent must be able to do the step at
  all: not one worker setting a slab by hand, not a small rover doing a tower crane's lift.
10 — every load reaches the ground; temporary items come and go as declared, by visible steps; evidence.
 7 — one minor doubt (a prop line hard to read, an item leaving one clip off its stage); or no evidence.
 5 — one unsupported element, hovering machine, item with no erection or dismantling step, or unfit machine.
 3 — two or more such failures, or a temporary item standing in the last scene after its declared removal.
 0 — the structure and its plant ignore support and the removal line throughout.
## CATEGORY 7 — WHERE THE MATERIAL CAME FROM
Is every element made of something that was somewhere else first, from a visible source that diminishes as
it grows? Check the ledger's source column against the specification's source (or observed source). Concrete
comes from a pump, skip or truck; steel from a stack lifted by a crane; panels from a stack at the facade foot;
stone from a pile or cart; fill from a stockpile or truck. Defects: material never seen on site · a source that
does not shrink · material in place with no handling · a crane lifting from a spot empty a moment before ·
concrete from a hose attached to nothing.
10 — every element's material seen at its source before it is in place, the source shrinking; evidence.
 7 — one element's source is thin (seen once, briefly); or no evidence.
 5 — one element made of material never seen on site, or lifted from an empty spot.
 3 — two or more elements with no source, or no source ever diminishes.
 0 — no element has a visible source; material is summoned.
## CATEGORY 8 — INVITED ONLY: THE CAST
Did everything on screen have the right to be there, and did everything expected arrive? Class every agent,
machine, structure, light, phenomenon and background object in the CAST LIST:
- Where a plan is attached: DECLARED (named in prompt/plan) · TOLERATED (invited in general terms: site texture,
  mud, ruts, puddles, blurred crew, sky lighting) · UNINVITED (nothing calls for it) · FORBIDDEN (negative
  block or declared world rules it out).
- Where NO plan is attached (Mode V): DECLARED / TOLERATED (standard plausible construction plant, vehicles,
  crews and materials appropriate for this structure and site) · UNINVITED (foreign, bizarre, or anomalous
  non-construction vehicles, buildings, or figures) · FORBIDDEN (impossible floating objects, sci-fi/fantasy
  apparitions on a real-world site, physical impossibilities).
- People, creatures, machines: a figure, even blurred, on an unmanned site · a suit, helmet or uniform never
  described · a crowd where a handful was declared · a bystander · any animal, bird, insect or fish · a
  machine type never named · more of a type than declared · a hand tool, ladder or wheelbarrow on a site with no hands.
- Structures: a second building, tower, module, mast or dome · a road, pier, bridge, track or runway never
  laid · a town or ridge lights outside the anchors · a vessel, aircraft or vehicle on a route never opened ·
  a monument, flag, sculpture or sign structure.
- Light and world: a beam, laser or searchlight · undeclared lightning, sparks or welding glow · a glow on an
  unlit object · a hologram or outline in light · undeclared floodlights or work lights · the sun's disc in
  frame when LIGHTING put it outside · a second light source · weather on an airless world or not scheduled
  for that scene · undeclared water · vegetation on a barren site · a season carrier in the wrong scene · a
  horizon that is not the declared one. In night, storm or eclipse scenes check every lamp and weather event.
- The invited that never came: per scene, the temporary equipment, the ACTIVITY machines and crew, the LIGHTING
  lamps and sky, the SITE TEXTURE and the season carrier must each be visible (the structure's own elements are
  Category 3). When C6 or C7 is triggered, score its defects there only.
10 — every member DECLARED or TOLERATED with its line quoted (or plausible on site), every expected member arrived; evidence.
 7 — one borderline member (TOLERATED on a loose reading) or one minor item absent one clip; or no evidence.
 5 — one UNINVITED member at playback speed, or one primary agent missing from the work.
 3 — one FORBIDDEN member, or UNINVITED members in two or more clips.
 0 — the cast is chaotic: forbidden members throughout, or the necessary agents absent.
## CONDITIONAL CATEGORIES
Open each only if its condition is met; otherwise write NOT TRIGGERED. A triggered conditional is scored.
**C1 — END CARD IDENTITY.** Open only if END CARD is YES.
The card shows the last scene's structure in the same state (form, element count, completion, temporary
works). 10 same, evidence at both · 7 one minor detail differs · 5 another stage, or equipment the last
scene removed · 3 a related but different structure · 0 another building.
**C2 — SECOND CAMERA STATION.** Open only if the plan declares a second or detail camera station.
Its clips show the main clips' structure (bay count, material, proportion), not merely a framing that hides
a difference; an undeclared change of position is SEE LENS 1. 10 same, named with timestamps · 7 one
property not verifiable · 5 one defining property differs · 3 several · 0 another structure.
**C3 — EXCAVATION.** Open only if a pit, trench or cut in the ground is part of the work.
One outline and wall treatment; depth only grows until a declared backfill; support fits the depth (batter,
shoring, sheet piles, benching); the footprint fits the structure later in it. 10 holds, evidence · 7 one
minor doubt · 5 depth regresses, outline changes, or a deep cut unsupported · 3 repeated · 0 no stable form.
**C4 — CRANE OR LIFTING MACHINE.** Open only if a crane or any machine lifts a load in any clip.
Hook, cable, trolley, jib, mast, base and ground form an unbroken chain in every frame; the crane stands
before the structure outgrows it and reaches where it places. A lift is seen arriving, held, lowered and
released, load path unbroken while held; release before contact, or contact before the machine arrives, is
a defect. 10 every chain and lift whole, evidence · 7 one frame hard to read · 5 one broken chain or
incomplete lift · 3 repeated · 0 lifts with no machine.
**C5 — SELF-RAISING ELEMENTS.** Open only if a mast, tower, platform, crane or formwork raises itself.
Seen at partial extension, extending, and locked; extension continuous; base anchored before it rises.
10 all three states, base first, evidence · 7 one state brief · 5 one missing · 3 unanchored base or a
jump in height · 0 simply taller in each clip.
**C6 — UNMANNED OR ROBOTIC SITE DECLARED.** Open only if the plan declares the site unmanned or robotic.
Every machine is sealed: no cab, window, seat, handrail, step or operator; no human silhouette, even blurred
or distant. One cab fails this category. 10 sealed throughout, evidence · 7 one detail that could be a vent
· 5 a part made for hands (handrail, step, mirror) on one machine · 3 one cab, seat, operator or figure ·
0 cabs or figures in two or more clips.
**C7 — OFF-WORLD OR AIRLESS SITE DECLARED.** Open only if the plan declares a site with no air.
Sky black or as declared; no clouds, haze, weather, birds, vegetation or open water; dust rises and falls in
ballistic arcs, never drifts or hangs. One cloud fails this category. 10 holds, evidence · 7 one ambiguous
wisp · 5 dust drifting or hanging in one clip · 3 a cloud, haze or open water · 0 an atmosphere.
**C8 — HIDDEN WORK DECLARED.** Open only if a document declares work the camera cannot see and names a
visible proxy. The proxy is seen being made, in proportion to the hidden work. 10 made step by step in
proportion, evidence · 7 made, proportion unclear · 5 appears unmade · 3 absent where needed · 0 no proxy.
## OUTPUT FORMAT
```
<the three BEFORE YOU SCORE lines>
SLATE
STRUCTURE (spec or obs)  <type · form · element count · material>
DECLARED / OBSERVED SITE <site type · air and sky · water · vegetation · crew: human / robotic / none>
REMOVAL LINE             <each temporary item · the stage it leaves>
STAGES                   clip n · stage description (spec or observed) — one line per clip
STAGE MISMATCH           <inconsistencies, regressions, or NONE>
ELEMENT LEDGER           element · first INCOMPLETE m:ss.s / NEVER / ILLEGIBLE · first COMPLETE m:ss.s ·
                         method seen / NONE · agent on the work m:ss.s / NONE · source seen m:ss.s / NONE ·
                         MADE / APPEARED / NEVER / FADED — SEE LENS 1
SCALE TABLE              milestone · clip · anchor relation or position · difference
CAST LIST                clip · member · DECLARED / TOLERATED / UNINVITED / FORBIDDEN · m:ss.s
INVITED, NOT SEEN        clip · member / NONE
FINDINGS
m:ss.s · what is visible · category number · document line quoted, or SPEC SILENT / NO SPEC
m:ss.s · SEE LENS n · what is visible
SCORES                                   (any score may read NOT VERIFIABLE)
1 STRUCTURE IDENTITY                     x/10 · evidence m:ss.s
2 GROWTH, SCALE AND GEOMETRY             x/10 · evidence m:ss.s
3 THE LEDGER IS COMPLETE                 x/10 · evidence m:ss.s
4 NOTHING IS BORN COMPLETE               x/10 · evidence m:ss.s
5 ORDER, SAME METHOD, ONE STEP           x/10 · evidence m:ss.s
6 LOAD PATH, TEMPORARY WORKS, MACHINERY  x/10 · evidence m:ss.s
7 WHERE THE MATERIAL CAME FROM           x/10 · evidence m:ss.s
8 INVITED ONLY                           x/10 · evidence m:ss.s
Cn <NAME>                                x/10 | NOT TRIGGERED · evidence m:ss.s  (one line each, C1 to C8)
VERDICT
IS IT THE SAME BUILDING?            SAME / DIFFERENT
IS IT BEING BUILT?                  BUILT / APPEARING
IS EVERYTHING ON SCREEN INVITED?    INVITED / INTRUDERS
THE FIRST PIECE THAT APPEARED:      <element> · m:ss.s / NONE
THE MOST DAMAGING INTRUDER:         <member> — clip n — m:ss.s / NONE FOUND
THE INVITED THING THAT NEVER CAME:  <member> / NONE
<up to three sentences with timestamps>

QUESTIONS FOR THE DOCUMENT          (if evaluated without attached specification or plan)
1. <question about structure, geometry or materials>
2. <question about element method or missing steps>
3. <question about machinery or temporary works>
4. <question about site cast or anomalies>
5. <question about completion or end state>
```
Verdicts are independent of the scores; when they disagree, the bad answer stands. DIFFERENT: a viewer
comparing any two clips would say two different structures. APPEARING: the structure as a whole grows with
no visible method (no crane work, no formwork cycle, no material arriving, no working level) — the genre's
most common failure, which no single category covers. INTRUDERS: anything uninvited or forbidden is visible
at playback speed in any scene. THE FIRST PIECE THAT APPEARED is the earliest ledger element marked
APPEARED, at the time it is first seen complete; it is the most important line of this report: a named piece
means its clip is produced again, whatever the scores. THE MOST DAMAGING INTRUDER is the one the next run
must remove first; THE INVITED THING THAT NEVER CAME is the declared member its scene most depended on.
