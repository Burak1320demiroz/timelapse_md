RUN INCOMPLETE — G0–G7 extracted keyframes plan checklist document was not supplied.

SLATE

```
FILM TITLE            THE LAST FIRING
ASPECT                9:16
CLIP COUNT            7
SCENE BLOCK           Clips 1–7 (00:00.0 – 00:28.0)
END CARD              PRESENT 00:28.0 – 00:32.0
TOTAL DURATION        00:32.0
CLIP DURATIONS        00:04.0 each (approx 7 × 4.0s = 28.0s scene block)
STILL FRAMES SUPPLIED 33 frames
VANTAGE GROUPS        A = clips 1, 2, 3, 4, 5, 6, 7 (Single vantage point)
```

---

### SCORES

```
1 CAMERA LOCK          10/10 Ⓥ
2 FRAME IDENTITY       10/10 Ⓥ
3 ANCHOR IDENTITY      10/10 Ⓥ
4 STATION IDENTITY     10/10 Ⓥ
5 SAFE AREA             9/10 Ⓥ
6 TEXT AND BRANDING     9/10 Ⓥ
7 PEOPLE AND VEHICLES   8/10 Ⓥ
8 SURFACE TRUTH         9/10 Ⓥ
C1 CRANE               NOT TRIGGERED
C2 SNOW                NOT TRIGGERED
C3 SECONDARY VANTAGE   NOT TRIGGERED
C4 NIGHT               10/10 Ⓥ
AVERAGE                9.4/10 Ⓥ
```

---

### FINDINGS

* **[Cat 5] [00:28.0]** Title text "THE LAST FIRING" sits inside the lower third safe area band, but overlay UI elements on some platforms may slightly overlap the lower text line.
* **[Cat 6] [00:00.0 – 00:28.0]** Trailer tongue/bed structure visible on lower left edge contains minor mechanical details, but no legible brand text or logos are present.
* **[Cat 7] [00:15.0 – 00:20.0]** During intense firing, some human figures present sharper silhouettes rather than fully motion-blurred time-lapse streaks.

---

### MEASUREMENT TABLE

```
[Vantage Group] [Clip]   [Horizon %]  [Tallest Background Object %]  [Spread]
Group A         Clip 1   ~57.0%       ~68.5% (Tree top)              < 0.5%
Group A         Clip 2   ~57.0%       ~68.5% (Tree top)              < 0.5%
Group A         Clip 3   ~57.0%       ~68.5% (Tree top)              < 0.5%
Group A         Clip 4   ~57.0%       ~68.5% (Tree top)              < 0.5%
Group A         Clip 5   ~57.0%       ~68.5% (Tree top)              < 0.5%
Group A         Clip 6   ~57.0%       ~68.5% (Tree top)              < 0.5%
Group A         Clip 7   ~57.0%       ~68.5% (Tree top)              < 0.5%
```

---

### VERDICT

`IS THIS A TIME-LAPSE? TIME-LAPSE`

The camera setup remains rock-solid across all construction and firing phases from 00:00.0 to 00:28.0. Key background anchors—including the fig tree on the left, the distant horizon ridge line, and the ground fence line—maintain strict spatial consistency throughout the video sequence.

---

### END CARD

`END CARD: does it show the same building as the last scene? SAME`

---

### QUESTIONS FOR THE DOCUMENT

1. Does the measured dome height delta relative to the horizon line match the target pixel offsets in the §1 specification table for frames G0 through G7?
2. Does the calculated surface luminance ratio ($L^*$) between the hearth opening and the outer dome surface pass the light gate thresholds defined in §3 for G4–G7?
3. Does the masked frame difference between G6 and G7 evaluate to $\le 2\text{ px}$ outside the three permitted variance regions defined in §4?
