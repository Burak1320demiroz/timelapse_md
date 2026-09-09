# 🚀 ORBITAL SCAFFOLD — Uzay Üssü İnşası Dikey Timelapse

> 10 klip × 8.0 saniye (80.0 sn) + 5.0 sn kapak kartı = 85.0 saniye.
> İki Keyframe Zinciri Formatı: 11 görsel prompt (KF0–KF10) + 10 I2V prompt = 21 prompt.

---

## 0. CONTINUITY PRIORITY ORDER

```text
1. Camera geometry (position, lens, tilt, roll — absolutely fixed)
2. Background landmark screen coordinates (BG-A, BG-B, BG-C1/C2/C3)
3. Permanent structure geometry and object identity
4. Current keyframe inventory (exact element count)
5. Allowed transition delta (only listed changes permitted)
6. Lighting continuity (smooth interpolation, no abrupt reset)
7. Surface dirt, tracks and weathering
8. Machine activity
9. Film aesthetic
```

---

## 1. 🔒 DEĞİŞMEZLER TABLOSU

```text
┌─ KAMERA İSTASYONU (ana) ────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100                         │
│ yükseklik     8.0 m — robotik tripod üssünün güney kenar yükseltisi │
│ D_kenar       kameradan sahanın yakın kenarına: 30 m                │
│ D_eksen       kameradan yapı eksenine (habitat merkezi): 55 m       │
│ bakış açısı   350° (kuzeykuzeybatı) · tilt 0° · roll 0°            │
│ sabitleme     bolted to a fixed tripod, absolutely zero movement    │
└─────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI ────────────────────────────────────────────────┐
│ BG-A   sağda (frame-right) yarım gömülü koyu bazalt blok, 4 m      │
│ BG-B   solda (frame-left) alçak yatay kaya sırtı, ince toz         │
│ BG-C1  arkada ufukta 1. sivri mesa silüeti                          │
│ BG-C2  arkada ufukta 2. sivri mesa silüeti                          │
│ BG-C3  arkada ufukta 3. sivri mesa silüeti                          │
└─────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ──────────────────────────────────────────────────┐
│ ufuk çizgisi   kare yüksekliğinin tam %50'sinde (tilt 0°)          │
│ habitat tabanı %47.5 · direk tacı %66.9                             │
│ saha sınırı    kadrajın alt %30 bandında                             │
└─────────────────────────────────────────────────────────────────────┘
```

### YAPI BIBLE — tamamlanmış hâlin sabit geometrisi

```text
When finished this will be a pressurised Mars surface base.

habitat       upright fabric drum, flat circular roof, vertical sides,
              8.0 m across and 6.4 m tall.
              Four narrow rectangular pressure windows permanently
              integrated into the upper third, evenly spaced; only two
              visible from camera angle. Positions never change.

berm          stacked regolith-filled tubes in level courses, each
              stepped back 0.3 m. Final height: 1.2 m (waist height).

panel dizi    two rows of flat solar panels, 12 per row (P01–P24),
              each 2.5 × 1.2 m, angled 30° toward equator.
              Front row: P01–P12 (left to right from camera).
              Rear row:  P13–P24 (left to right from camera).
              Row spacing: 2.0 m. Panel gap: 0.15 m.
              Metal triangular cross-braced support frames.
              Storm damage removes only P05, P06, P11, P12, P17, P18.

direk         bolted three-leg guyed tower, six sections.
              1.6 m parabolic reflector on section 5, facing frame-left,
              25° upward elevation. Orientation never changes.

iniş pedi     sintered dark glassy disc, 30 m diameter.

bağlantı      pressurised fabric tube, 1.8 m diameter, 6 m long.
              Exits habitat at 250° site azimuth.
```

### SITE COORDINATE LOCK

```text
Habitat centre = site origin (0,0).
Solar array centre = 12 m east-south-east of habitat centre.
Tower base = 7 m west-north-west of habitat centre.
Connecting tube exits habitat at 250° site azimuth, extends 6.0 m.
Landing pad centre = same as habitat origin.
```

### MACHINE REGISTRY

```text
VEH-A  = tracked grading rover (sealed, no cab)
VEH-B  = autonomous cargo cart (sealed, no cab)
ARM-A  = six-axis construction manipulator (ground-mounted)
SIN-A  = Mars sintering crawler
DRL-A  = sealed drilling rig
PMP-A  = habitat inflation pump unit
```

### STRUCTURAL ANCHORS (locked screen positions after first appearance)

```text
STRUCT-A = habitat roof centre
STRUCT-B = leftmost solar-frame corner
STRUCT-C = tower footing
STRUCT-D = connector flange on habitat wall (250° site azimuth)
STRUCT-E = berm front top seam
```

---

## 2. 🪜 AŞAMA MERDİVENİ — 10 Sahne (80.0 sn)
> **USER OVERRIDE / GEREKÇE (DERS 13 METRONOM İSTİSNASI):** Sahneler arası devamlılık gereksinimi nedeniyle tüm sahneler tam 8.0 saniyeye sabitlenmiştir.

| S | SÜRE | AŞAMA | YENİ OLAN | ARA HÂL | TEMSİL | REJIM | MEVSİM TAŞIYICISI | KANIT NESNESİ | İST |
|:-:|---:|---|---|---|---|---|---|---|---|
| 0 | 8.0 | iniş pedi düzleme | tracked blade unit regolit iter | ped %25: ham kesik, bıçak izleri | 1 hafta | C | palet izlerinin çoğalması | sağda bazalt blok BG-A | ANA |
| 1 | 8.0 | ped sinterleme | sintering crawler, akkor parlama | ped %75: altıgen karolar, kenarları turuncu | 2 hafta | C | sinterlenen alanın büyümesi | sağda bazalt blok BG-A | ANA |
| 2 | 8.0 | temel kazı + düzleme | drill rig çukur açıyor | temel %50: düzleşmiş daire, gevşek toz | 3 hafta | C | çukur derinliği artışı | sağda bazalt blok BG-A | ANA |
| 3 | 8.0 | habitat şişirme | inflation pump unit bağlı | habitat %50: yarı şişmiş, derin kırışıklıklar | 2 hafta | B | kırışıklıkların gerilmesi | sağda bazalt blok BG-A | ANA |
| 4 | 8.0 | berm + güç panelleri | manipulator arm tüp istifliyor | berm done, 20/24 panel | 2 ay | B | tüp sıra sayısı | sağda bazalt blok BG-A | ANA |
| 5 | 8.0 | ⭐ TOZ FIRTINASI | toz duvarı ufuktan geçer | 18/24 panel, toz tabakası | 1 ay | B | pus yönü ufuktan kadraj boyunca | sağda bazalt blok BG-A | ANA |
| 6 | 8.0 | fırtına sonrası onarım | manipulator arm yerleştiriyor | 24/24 panel onarılmış | 3 hafta | B | takılı panel sayısı | sağda bazalt blok BG-A | ANA |
| 7 | 8.0 | iletişim direği + çanak | manipulator arm direk kaldırıyor | direk 3/6 bölüm, scaffold | 2 hafta | B | direk yüksekliği | sağda bazalt blok BG-A | ANA |
| 8 | 8.0 | bağlantı tüpü şişirme | tüp şişiyor, cart yol düzlüyor | tüp folded crate, mast done | 1 ay | B | tüp gerginliği | sağda bazalt blok BG-A | ANA |
| 9 | 8.0 | ışıklar (şafak öncesi) | pencere ışıkları yanar | tam üs, bracket hâlâ var | 1 gün | B | habitat pencere ışıkları | sağda bazalt blok BG-A | ANA |

---

## 3. INVENTORY STATE TABLE

| Element | KF0 | KF1 | KF2 | KF3 | KF4 | KF5 | KF6 | KF7 | KF8 | KF9 | MASTER |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Pad | 25% | 75% | done | done | done | done | done | done | done | done | done |
| Pit | — | — | 50% | done | done | done | done | done | done | done | done |
| Habitat | — | — | — | 50%↑ | done | done | done | done | done | done | done |
| Windows | — | — | — | dark | dark | dark | dark | dark | dark | LIT | LIT |
| Berm | — | — | — | — | done | done | done | done | done | done | done |
| Panels | — | — | — | — | 20/24 | 18/24 | 24/24 | 24/24 | 24/24 | 24/24 | 24/24 |
| Tower | — | — | — | — | — | — | — | 3/6 | 6/6+dish | 6/6+dish | 6/6+dish |
| Tube | — | — | — | — | — | — | — | — | folded | inflated | inflated |
| TEMP pump | — | — | — | ✓ | — | — | — | — | — | — | — |
| TEMP guy(berm) | — | — | — | — | ✓ | ✓ | — | — | — | — | — |
| TEMP scaffold(solar) | — | — | — | — | ✓ | ✓ | ✓ | — | — | — | — |
| TEMP guy(panel) | — | — | — | — | — | ✓ | ✓ | — | — | — | — |
| TEMP scaffold(mast) | — | — | — | — | — | — | — | ✓ | — | — | — |
| TEMP guy(mast) | — | — | — | — | — | — | — | coiled | tensioned | tensioned | — |
| TEMP sling(tube) | — | — | — | — | — | — | — | — | ✓ | — | — |
| TEMP bracket(tube) | — | — | — | — | — | — | — | — | — | ✓ | — |

---

## 4. 🚫 ARAÇ KUTU SETİ
KUTU SETİ: {5, 10} sn

---

## 5. 📦 TESLİM YAPISI VE KAPAK KARTI
TESLİM YAPISI: 80 sn video + 5.0 sn KAPAK KARTI eklenecek.

---

## SAHNE 0

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 0 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: The site topsoil is fully stripped to raw brown regolith, and deep tracked blade marks scar the exposed ground. No temporary equipment is visible yet. The cleared area covers roughly half the future pad diameter.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, the edge of the cleared circular area aligns horizontally with the midpoint between the site centre and BG-A.

COMPOSITION: Vertical 9:16. The base of the cleared area sits at about thirty percent of frame height. The crown of the future structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 120 degrees, elevation 40 degrees, shadows falling to the north-west. Flat butterscotch sky, harsh daylight, high contrast, sharp black shadows across the site.

TIME RATE: A full working day passes. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A rover spreads a filled pile of regolith across the cleared ground, and a separate cart hauls loose spoil away. No people are present.

SITE TEXTURE: Exposed compacted brown regolith, deep blade marks, cleated tracks, irregular stones, loose excavated piles and rough rock fragments across the working area.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

A full working day passes across 8.0 seconds. The shadow of BG-A sweeps steadily across the dirt as the sun arc continues. A rover spreads filled piles of regolith repeatedly across the frame, leaving deep parallel ruts. Coarse grains follow short low-gravity ballistic arcs while fine dust remains briefly suspended in the thin Martian atmosphere. The cleared circular area grows visibly wider, covering the natural rocky texture with loose fine dirt.

Only the following changes occur: the cleared area expands and more blade marks appear. Everything else — background landmarks, horizon — remains pixel-stable throughout.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## SAHNE 1

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 1 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A circular pad area is being sintered. A Mars sintering crawler crosses the ground, leaving hexagonal tiles behind it; the centre of the tiles is dark grey, while the edges are still glowing bright orange. About 75 percent of the 30-metre pad is now glassy sintered crust.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, the sintered glassy crust extends exactly to the projected base of BG-A.

COMPOSITION: Vertical 9:16. The base of the pad sits at about thirty percent of frame height. The crown of the future structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 120 degrees, elevation 40 degrees, shadows falling to the north-west. Flat butterscotch sky, harsh daylight, high contrast, sharp black shadows across the site.

TIME RATE: A full working day passes. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A rover spreads a fresh hot tile onto the ground, and a cart hauls a filled skip of loose regolith. No people are present.

SITE TEXTURE: Glassy sintered hexagonal tiles, deep cleated tracks, scattered regolith piles, loose dust, and rough rock fragments across the working area.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

A full working day passes across 8.0 seconds. The shadow of BG-A sweeps steadily across the dirt. A Mars sintering crawler sets fresh hot crust tiles repeatedly across the frame, glowing bright orange. Coarse grains follow short low-gravity ballistic arcs while fine dust remains briefly suspended in the thin Martian atmosphere. The sintered glassy crust grows visibly wider, covering the natural rocky texture.

Only the following changes occur: the sintered pad area expands. Everything else — background landmarks, horizon — remains pixel-stable throughout.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## SAHNE 2

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 2 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A completed sintered dark glassy disc pad, 30 metres in diameter, sits on the ground. In its centre, a circular foundation pit is being excavated. A drilling rig cuts a raw step into the pad, leaving deep teeth marks in the regolith. The pit is about 50 percent of its final depth.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, the projected depth of the cut aligns horizontally with the lower ledge of BG-B.

COMPOSITION: Vertical 9:16. The base of the pad sits at about thirty percent of frame height. The crown of the future structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 120 degrees, elevation 40 degrees, shadows falling to the north-west. Flat butterscotch sky, harsh daylight, high contrast, sharp black shadows across the site.

TIME RATE: A full working day passes. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A drill rig lifts a filled pile of regolith out of the pit, and a rover pushes loose dirt away. No people are present.

SITE TEXTURE: Glassy sintered surface, deep cleated tracks, scattered regolith piles, raw cut faces, loose dust, and rough rock fragments across the working area.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

A full working day passes across 8.0 seconds. The shadow of BG-A sweeps steadily across the dirt. A drill rig lifts filled piles of regolith repeatedly out of the pit. Coarse grains follow short low-gravity ballistic arcs while fine dust remains briefly suspended in the thin Martian atmosphere. The circular foundation pit grows visibly deeper, exposing raw bedrock below.

Only the following changes occur: the pit deepens and spoil piles grow. Everything else — pad, background landmarks — remains pixel-stable throughout.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## SAHNE 3

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 3 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A completed sintered dark glassy disc pad surrounds a central foundation pit. Inside the pit, an upright fabric drum habitat sits half-inflated with deep fabric wrinkles and a heavy temporary inflation pump unit is bolted to its side. Four narrow rectangular pressure windows are visible in the upper third of the drum, dark and unlit. The habitat is 50 percent of its final height.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, the projected upper rim of the folded habitat aligns horizontally with the projected top edge of BG-A.

COMPOSITION: Vertical 9:16. The base of the habitat sits at about 47.5 percent of frame height. The crown of the future structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 120 degrees, elevation 40 degrees, shadows falling to the north-west. Flat butterscotch sky, harsh daylight, high contrast, sharp black shadows across the site.

TIME RATE: About two hours pass. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A pump fills the habitat drum with compressed gas, and a cart places a filled material module on the ground. No people are present.

SITE TEXTURE: Glassy sintered surface, deep cleated tracks, scattered regolith piles, loose dust, inflation hoses, and rough rock fragments across the working area.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

About two hours pass across 8.0 seconds. The shadow of BG-A sweeps steadily across the dirt. A pump fills the habitat drum continuously and the deep fabric wrinkles pull taut as the drum expands visibly upwards. A cart places filled material modules repeatedly on the ground. Coarse grains follow short low-gravity ballistic arcs while fine dust remains briefly suspended in the thin Martian atmosphere.

Only the following changes occur: the habitat drum inflates upward, wrinkles tighten. Everything else — pad, pit, background landmarks — remains pixel-stable throughout.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## SAHNE 4

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 4 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A sintered dark glassy disc pad surrounds a fully inflated upright fabric drum habitat with four narrow dark windows in the upper third. Around the habitat, a stacked regolith-filled tube berm stands four courses high (final height 1.2 metres) with a temporary guy wire running along its top edge. Nearby, twenty of the twenty-four flat solar panels (P01-P04, P07-P16, P19-P24) are bolted into metal frames supported by temporary scaffold props. Empty frames for P05, P06, P17, P18 are visible. The inflation pump has been removed.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, the projected top seam of the fourth berm course aligns horizontally with the lower quarter of BG-A.

COMPOSITION: Vertical 9:16. The base of the habitat sits at about 47.5 percent of frame height. The crown of the future structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 120 degrees, elevation 40 degrees, shadows falling to the north-west. Flat butterscotch sky, harsh daylight, high contrast, sharp black shadows across the site.

TIME RATE: About two hours pass. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A manipulator arm lifts a filled regolith tube onto the berm stack, and a cart hauls a fresh panel frame. No people are present.

SITE TEXTURE: Glassy sintered surface, deep cleated tracks, scattered regolith piles, loose dust, and rough rock fragments across the working area.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

About two hours pass across 8.0 seconds. The shadow of BG-A sweeps steadily across the dirt. A manipulator arm lifts filled regolith tubes repeatedly onto the berm. A cart hauls fresh panel frames across the pad. Coarse grains follow short low-gravity ballistic arcs while fine dust remains briefly suspended in the thin Martian atmosphere. The remaining four empty panel frames receive panels. Then a wall of ochre dust rolls in from the right horizon, steadily obscuring the site.

Only the following changes occur: panels P05, P06, P17, P18 are installed (20 to 24), then the dust storm arrives and rips panels P05, P06, P11, P12, P17, P18 from their frames (24 to 18). Inflation pump is already gone. Everything else — habitat, berm height, pad, background landmarks — remains pixel-stable.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## SAHNE 5

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 5 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A sintered dark glassy disc pad surrounds a fully inflated upright fabric drum habitat with four narrow dark windows in the upper third. The completed regolith-filled tube berm (1.2 metres high) is entirely coated in fine red dust. Eighteen of the twenty-four flat solar panels remain bolted; six empty frames (P05, P06, P11, P12, P17, P18) are exposed where the storm ripped panels away. Temporary heavy guy wires hold the remaining panels down. Temporary scaffold props remain under the array.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, a thick drift of blown sand covers the lower half of BG-B.

COMPOSITION: Vertical 9:16. The base of the habitat sits at about 47.5 percent of frame height. The crown of the future structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 120 degrees, elevation 40 degrees, shadows falling to the north-west. Dark ochre sky, uniformly bright from horizon to zenith, with no bright point anywhere. The thick dust haze completely flattens the light so no cast shadow falls anywhere on the site.

TIME RATE: About two hours pass. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A cart hauls a filled skip of storm debris, and a manipulator arm lowers a protective cover over the array. No people are present.

SITE TEXTURE: Glassy sintered surface, deep cleated tracks, scattered regolith piles, heavy loose dust drifts, storm debris, and rough rock fragments across the working area.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

About two hours pass across 8.0 seconds. The thick ochre dust haze sweeps across the frame from right to left, completely flattening the light so no shadow falls. A cart hauls filled skips of storm debris. The thick layer of fine regolith builds up visibly across surfaces. Coarse grains follow short low-gravity ballistic arcs while fine dust remains briefly suspended in the thin Martian atmosphere.

Only the following changes occur: dust accumulates on all surfaces, visibility decreases. Everything else — habitat, berm, panel frames, background landmarks — remains pixel-stable. Background geometry is occluded by dust but its underlying position never changes.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## SAHNE 6

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 6 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A sintered dark glassy disc pad surrounds a fully inflated upright fabric drum habitat with four narrow dark windows in the upper third. The completed regolith-filled tube berm (1.2 metres high) is clean. Twenty-four of the twenty-four flat solar panels are now bolted into their metal frames; all six storm-damaged frames have received fresh replacement panels. Temporary guy wires are still attached to the array. Temporary scaffold props remain under the array.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, the projected rightmost edge of the restored solar array aligns with the projected tip of BG-C2.

COMPOSITION: Vertical 9:16. The base of the habitat sits at about 47.5 percent of frame height. The crown of the future structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 120 degrees, elevation 40 degrees, shadows falling to the north-west. Flat butterscotch sky, harsh daylight, high contrast, sharp black shadows across the site.

TIME RATE: About two hours pass. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A manipulator arm lifts a fresh solar panel into an open metal frame, and a cart hauls a filled skip of dust. No people are present.

SITE TEXTURE: Glassy sintered surface, deep cleated tracks, scattered regolith piles, heavy loose dust drifts, and rough rock fragments across the working area.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

About two hours pass across 8.0 seconds. The shadow of BG-A sweeps steadily across the dirt. A manipulator arm lifts fresh solar panels repeatedly into the open metal frames. A cart hauls filled skips of dust away. Coarse grains follow short low-gravity ballistic arcs while fine dust remains briefly suspended in the thin Martian atmosphere. The row of restored flat solar panels grows visibly longer, returning to its pristine dark blue colour.

Only the following changes occur: replacement panels fill the six empty frames (18 to 24). Guy wires and scaffold props are physically removed and carted away. Everything else — habitat, berm, pad, background landmarks — remains pixel-stable.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## SAHNE 7

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 7 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A sintered dark glassy disc pad surrounds a fully inflated upright fabric drum habitat with four narrow dark windows in the upper third. The completed berm (1.2 metres) and two complete rows of 12 flat solar panels are present. Beside the habitat, the bottom three sections of a bolted three-leg guyed tower are bolted in place, heavy temporary steel guy wires lie coiled on the ground, and a temporary climbing scaffold bracket wraps around the top joint.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, the projected top of the third mast section aligns horizontally with the projected peak of BG-C1.

COMPOSITION: Vertical 9:16. The base of the habitat sits at about 47.5 percent of frame height and the top of the third mast section reaches to about 55 percent. The crown of the future structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 120 degrees, elevation 40 degrees, shadows falling to the north-west. Flat butterscotch sky, harsh daylight, high contrast, sharp black shadows across the site.

TIME RATE: About two hours pass. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A manipulator arm lifts a fresh steel mast section into the scaffold bracket, and a boom swings a cable spool down. No people are present.

SITE TEXTURE: Glassy sintered surface, deep cleated tracks, scattered regolith piles, coiled cables, and rough rock fragments across the working area.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

About two hours pass across 8.0 seconds. The shadow of BG-A sweeps steadily across the dirt. A manipulator arm lifts fresh steel mast sections repeatedly into the scaffold bracket. A boom swings cable spools down to the ground. Coarse grains follow short low-gravity ballistic arcs while fine dust remains briefly suspended in the thin Martian atmosphere. The bolted three-leg guyed tower grows visibly taller. The scaffold bracket climbs with each new section. Sections 4, 5 and 6 are added; the parabolic dish is mounted on section 5. Guy wires are tensioned. Finally a folded tube crate is delivered and parked beside the habitat.

Only the following changes occur: tower grows from 3 to 6 sections, dish mounted, guy wires tensioned, scaffold bracket removed, folded tube crate delivered. Everything else — habitat, berm, panels, pad, background landmarks — remains pixel-stable.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## SAHNE 8

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 8 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A sintered dark glassy disc pad surrounds a fully inflated upright fabric drum habitat with four narrow dark windows in the upper third. The completed berm (1.2 metres) and two complete rows of 12 flat solar panels are present. A fully erected six-section bolted three-leg guyed tower carries a 1.6 metre parabolic reflector on section 5, facing frame-left at 25 degrees upward elevation; heavy tensioned steel guy wires anchor it. A folded fabric connecting tube sits in a temporary cargo sling beside the habitat flange at STRUCT-D.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, the folded tube crate sits directly below the projected base of the tower.

COMPOSITION: Vertical 9:16. The base of the habitat sits at about 47.5 percent of frame height and the top of the mast at 66.9 percent. The crown of the future structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 120 degrees, elevation 40 degrees, shadows falling to the north-west. Flat butterscotch sky, harsh daylight, high contrast, sharp black shadows across the site.

TIME RATE: About two hours pass. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A cart spreads a fresh gravel layer across the pathway, and a manipulator arm lifts the folded tube section. No people are present.

SITE TEXTURE: Glassy sintered surface, deep cleated tracks, scattered regolith piles, heavy loose dust drifts, coiled cables, and rough rock fragments across the working area.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

About two hours pass across 8.0 seconds. The shadow of BG-A sweeps steadily across the dirt. A manipulator arm lifts the folded tube from its cargo sling and threads it between the two flanges. An inflation hose connects and the fabric tube slowly fills, expanding from flat to round. Deep wrinkles pull taut as the tube reaches full pressure. A temporary external bracket is clamped onto the tube. A cart spreads fresh gravel across the main pathway. Coarse grains follow short low-gravity ballistic arcs while fine dust remains briefly suspended in the thin Martian atmosphere.

Only the following changes occur: tube unfolds, inflates to full pressure, temporary bracket attached. Cargo sling removed and carted away. Everything else — habitat, berm, panels, tower, pad, background landmarks — remains pixel-stable.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## SAHNE 9

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Scene 9 of 10. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A sintered dark glassy disc pad surrounds a fully inflated upright fabric drum habitat. Four narrow rectangular pressure windows in the upper third glow with warm yellow-white interior light. The completed berm (1.2 metres) and two complete rows of 12 flat solar panels are present. A fully erected six-section bolted three-leg guyed tower carries a 1.6 metre parabolic reflector facing frame-left at 25 degrees upward; heavy tensioned steel guy wires anchor it. A pressurised fabric connecting tube, 1.8 metres diameter and 6 metres long, connects to the habitat at STRUCT-D; a temporary external bracket still clings to its side.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, bright interior lights shine from the narrow windows of the habitat, illuminating the dust in the air.

COMPOSITION: Vertical 9:16. The base of the habitat sits at about 47.5 percent of frame height and the top of the mast at 66.9 percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 350 degrees, elevation 5 degrees (civil dawn). Deep twilight blue-black sky brightening at the east horizon, hard pooled shadows cast by the habitat's own exterior work lights.

TIME RATE: About two hours pass. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A cart hauls a filled spool of loose cable, and a manipulator arm lifts the temporary bracket from the tube. No people are present.

SITE TEXTURE: Smooth swept regolith pathways, parked equipment silhouettes, fine dust layer over the panel frames, coiled cables, and hose connections.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow. The stars render as concentric arcs about twenty degrees long, centred on the Martian celestial pole, consistent with a ninety-minute exposure.
Output: 9:16, 4K, no text, no watermark.
```

### I2V PROMPT

```text
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same objects in the same places. The opening lighting matches the first provided image exactly and evolves continuously toward the second; sun direction, shadow length and sky colour interpolate smoothly without any abrupt reset.

About two hours pass across 8.0 seconds. The hard pooled shadows of the habitat exterior work lights stay fixed across the dirt while the stars wheel slowly overhead. A manipulator arm lifts the temporary bracket from the connecting tube and places it on a cart. The cart hauls filled spools of cable. The eastern horizon gradually brightens. The bright interior lights shine steadily from the narrow habitat windows.

Only the following changes occur: temporary tube bracket physically removed, mast guy wires loosened and coiled, dawn light grows. Everything else — habitat, berm, panels, tower, tube, pad, background landmarks — remains pixel-stable.

The camera does not move at any point. The framing is identical in the first and last frame: BG-A occupies exactly the same width of the frame at both ends of the shot. The half-buried dark basalt block, the low horizontal rock ridge and the three mesa silhouettes stay exactly where they are, at exactly the same size and shape, for the whole shot.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## USTA KARE

### GÖRSEL PROMPT

```text
1970s 70 mm scientific surface-documentation film aesthetic, photographed from a permanently fixed survey camera: flat grey regolith, blown highlights, razor-edged black shadows, slight grain, no haze, no depth fog, no rim light. Vertical time-lapse of a Mars surface base construction on a rocky plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge, lens 8.0 metres above the ground, 55 metres from the centre of the site, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a pressurised Mars surface base. AT THIS STAGE: A sintered dark glassy disc pad surrounds a fully inflated upright fabric drum habitat. Four narrow rectangular pressure windows in the upper third glow faintly in the dawn light. The completed berm (1.2 metres) and two complete rows of 12 flat solar panels are present. A fully erected six-section bolted three-leg guyed tower carries a 1.6 metre parabolic reflector facing frame-left at 25 degrees upward. A pressurised fabric connecting tube, 1.8 metres diameter and 6 metres long, connects to the habitat. All temporary guy wires, scaffold brackets and cargo slings have been removed; the base stands completely finished.

SITE / BACKGROUND: To frame right stands a half-buried dark basalt block (BG-A), 4.0 metres tall with a flat top surface. To frame left lies a low horizontal rock ridge (BG-B) covered with a thin layer of fine dust. Behind the site on the Martian horizon stand three vertical pointed mesa silhouettes (BG-C1, BG-C2, BG-C3). The horizon sits at exactly half the frame height.

THE TIME MOMENT: In the locked camera image, the morning sun strikes the top rim of the habitat, bathing the finished base in pristine dawn light.

COMPOSITION: Vertical 9:16. The base of the habitat sits at about 47.5 percent of frame height and the top of the mast at 66.9 percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 45 degrees, elevation 10 degrees. Low-angle dawn light painting the habitat rim with warm golden tones. Flat butterscotch sky, sharp long shadows stretching to the west.

TIME RATE: About two hours pass. A single consistent timelapse time compression applies to the whole scene; each object — shadow, machine, dust — retains physically correct relative motion under that shared compression. Everything in this frame is time-lapsed at the same rate. Nothing in the frame moves at normal speed.

ACTIVITY: A cart rests parked and motionless beside the pad. A manipulator arm rests lowered. No people are present.

SITE TEXTURE: Smooth swept regolith pathways, parked equipment silhouettes, fine dust layer over the panel frames.

PHYSICS: Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. Every structure rests on the regolith or the pad beneath it; nothing is unsupported.

NEGATIVE: PERMANENT GEOMETRY LOCK: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the horizon line, BG-A, BG-B, and BG-C never change shape, position, size or spacing; during dust events their visibility may decrease through atmospheric occlusion but their underlying position and geometry never change. Every permanent structure element retains its geometry, position, colour, scale and screen coordinates once placed. TEMPORARY EQUIPMENT EXCEPTION: only items explicitly listed under ALLOWED DELTA for the current transition may be physically removed. STORM DAMAGE EXCEPTION: only solar panels P05, P06, P11, P12, P17 and P18 may be removed during the storm transition; their frames remain bolted in place. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: not on the rover, lander, module, habitat, panel, mast, radiator, antenna, spool, cradle, manipulator, or machinery. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. No rain, no snow. The stars render as concentric arcs about twenty degrees long, centred on the Martian celestial pole, consistent with a ninety-minute exposure.
Output: 9:16, 4K, no text, no watermark.
```

