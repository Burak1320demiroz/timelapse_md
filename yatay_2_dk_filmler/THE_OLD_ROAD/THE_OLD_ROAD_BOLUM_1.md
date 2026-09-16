# 🎬 THE_OLD_ROAD — BÖLÜM 1  (S0 – S7 · G0 … G7 + 8 I2V · 0,0–64,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `THE_OLD_ROAD_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır (model hafızasızdır: STRUCTURE ve SITE / BACKGROUND blokları 16 promptta
> BİREBİR aynı kelimelerle tekrarlanır, değişen yalnız AT THIS STAGE ve THE TIME MOMENT).
>
> İskelet `PROMPT_SABLONU.md` §1 (görsel) ve §2 (iki uçlu I2V); negatif çekirdek
> `KILAVUZ_REHBERI` §7 tam metin; blok ETİKETLERİ birebir — nesre dönen etiket kapıyı düşürür
> [DERS 20]. Görsel prompt bandı 2.000–6.000 karakter [DERS 2]; kapı `araclar/prompt_kontrol.py`.
>
> ⭐ Bu bölümün SON I2V'si (S7: G7 → G8) **G8 karesinde biter** ve G8 `BOLUM_2`'nin ilk
> görselidir: bölüm sınırı bir KAREDİR, kesme değil — ışık, gölge açısı, yapı yüzdesi orada atlamaz
> [DERS 52]. Kapı KLASÖR MODUNDA koşulur: `python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_OLD_ROAD`
> (tek bölüm dosyasına koşulan kapı "usta kare yok" der — bu arıza değil, eksik koşudur).
>
> Sahne başlığı `## 🎬 SAHNE <rakam>` ile yazılır; `Scene n of 15` satırı n = 0'dan sayar.

---

## 🎬 SAHNE 0 — AÇAR

```
SÜRE: 8,0 s (0,0–8,0)  ·  ELEMAN + ARA HÂL: YENİ GÜZERGÂH 0 → ilk kesi (%2)  ·  REJİM: A  ·  SAAT: 05:05→05:15  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G0)

```
Photorealistic documentary construction photograph — Scene 0 of 15. Horizontal 16:9 time-lapse of a long concrete viaduct being pushed out across a deep alpine valley, seen from a rock spur down the valley; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur down the valley, lens 80.0 metres above the river, 380 metres from the viaduct axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one new concrete box-girder viaduct of seven spans carried on five slender piers across the valley, with the old stone arch bridge still standing on the valley floor below it. AT THIS STAGE: nothing of the new crossing exists yet and the valley is as it has always been. The old road runs through its fourteen hairpins on both slopes with early traffic on it, headlights drawing short bright trails down the left slope, across the stone arch bridge and up the right slope. High on the left slope, where the new line will start, a yellow tracked dozer has cut the first twenty metres of raw earth bench into the wood: a fresh brown scar with felled larch trunks stacked beside it and spoil pushed into a low windrow. The valley floor is untouched grass and river gravel.

SITE / BACKGROUND: The valley runs away from the camera between two steep larch-wooded slopes closing in high twin peaks on the skyline. On the valley floor the river comes down toward the camera under a single old stone arch bridge, and the old road crosses the valley in fourteen hairpins cut into both slopes, a pale asphalt band with a guardrail. Beside one hairpin on the left slope stands a single small chapel; on the right rim stands a single tall rock pinnacle. The valley carries exactly one old stone arch bridge and one line of new works; no other bridge, mast or tower stands anywhere from edge to edge. The eye line at exactly half the frame height crosses the rock pinnacle a third of the way up.

THE TIME MOMENT: The valley is still the old valley: fourteen lit hairpins carrying the traffic, and one fresh earth scar on the left slope — the first twenty metres of a line that will cross the whole valley.

COMPOSITION: Horizontal 16:9. The river and the valley floor sit at about twenty-five percent of frame height, the old stone arch bridge at about thirty-four percent left of centre, the twin peaks at eighty-two percent and the rock pinnacle at forty-six to fifty-eight percent. The old stone arch bridge spans about 64 pixels of frame width — one thirtieth — and keeps that width and position in every frame. The fresh earth bench sits on the left slope at about fifty percent of frame height, left of the chapel; the headlight trails run along the hairpin band between about thirty and seventy percent. The crown of the structure sits below the top eighth and the working level above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 75 degrees, elevation 5 degrees below the horizon, the first blue light before sunrise, no cast shadows yet, the sky brightening from the right. The sun stays outside the frame for the whole shot; its only sign is the shadows. Early March: bare grey larch woods, a thick snow line low on both slopes, the river low and clear, the twin peaks pale against a deep blue sky.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, the river, machines and vehicles all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The tracked dozer pushes a fresh bench of earth along the new line and drops the spoil into a windrow below it, while cars and a bus run the hairpins of the old road, their headlights drawing continuous white and red trails along the pale asphalt band and across the stone arch bridge; dust and exhaust hang over the fresh cut. Crew register only as faint soft motion streaks beside the dozer, never as sharp figures.

SITE TEXTURE: Bare larch woods grey-brown on both slopes with a thick snow band above them; the fresh cut raw brown earth with dozer track marks, a spoil windrow and stacked trunks; the old road a pale asphalt band with a dark guardrail line and salt stains at its edges; the river bed pale gravel with dark wet channels.

PHYSICS: The dozer stands on its tracks on the new bench with its blade pressed into the earth; the felled trunks rest stacked on the slope above it; the old stone arch bridge bears on its two rock abutments and carries the traffic; every vehicle stands on its tyres on the asphalt.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The slopes, the hairpins, the stone arch bridge, the chapel, the rock pinnacle and the skyline never change shape, position, size or spacing; every pier, once built, stays where it is. The new crossing is one rigid concrete structure that only ever gains length — nothing already built is removed, moved or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, formwork, scaffolding, container, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic, no tilt-shift blur.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G0 → G1)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Ten minutes pass across the blue light before sunrise. Everything in this shot is time-lapsed at the same rate: the sky brightens from the right, thin clouds drift in one smooth flow above the peaks, and the traffic on the old road runs fast but stays recognisable, its headlights drawing unbroken white and red trails down the hairpins, over the stone arch bridge and up the far slope. The tracked dozer works the new line on the left slope, pushing the raw earth bench a few tens of metres further along the contour and dropping the spoil into the windrow below it, so that by the end of the shot the fresh brown scar is longer and a second machine has driven up the old road and stopped at its head. The snow line, the chapel, the hairpins and the stone arch bridge do not change.

The camera does not move at any point. The framing is identical in the first and last frame. The slopes, the hairpins of the old road, the old stone arch bridge, the chapel, the rock pinnacle and the skyline stay exactly where they are, at exactly the same size and shape, for the whole shot. The old stone arch bridge occupies exactly the same width of the frame in the first and last frame, and the eye line stays at exactly half the frame height. The valley carries exactly one old stone arch bridge and one line of new works, and no other bridge, mast or tower appears anywhere. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 1 — KAZAR

```
SÜRE: 8,0 s (8,0–16,0)  ·  ELEMAN + ARA HÂL: YAKLAŞIM + TEMELLER 0 → %100 · geçici geçiş kurulur  ·  REJİM: B  ·  SAAT: 05:15→07:15  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G1)

```
Photorealistic documentary construction photograph — Scene 1 of 15. Horizontal 16:9 time-lapse of a long concrete viaduct being pushed out across a deep alpine valley, seen from a rock spur down the valley; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur down the valley, lens 80.0 metres above the river, 380 metres from the viaduct axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one new concrete box-girder viaduct of seven spans carried on five slender piers across the valley, with the old stone arch bridge still standing on the valley floor below it. AT THIS STAGE: the new line exists only as an earth cut and nothing is founded yet. On the left slope the raw brown bench now runs a few hundred metres along the contour to the point where the new crossing will start, its spoil pushed into a windrow below it and felled larch trunks stacked along its edge; the yellow dozer stands parked at the head of the cut. On the right rim a second, shorter clearing has been opened opposite it. A low-loader has brought a tracked excavator up the old road and stopped on the widest hairpin; the valley floor is still untouched grass and river gravel.

SITE / BACKGROUND: The valley runs away from the camera between two steep larch-wooded slopes closing in high twin peaks on the skyline. On the valley floor the river comes down toward the camera under a single old stone arch bridge, and the old road crosses the valley in fourteen hairpins cut into both slopes, a pale asphalt band with a guardrail. Beside one hairpin on the left slope stands a single small chapel; on the right rim stands a single tall rock pinnacle. The valley carries exactly one old stone arch bridge and one line of new works; no other bridge, mast or tower stands anywhere from edge to edge. The eye line at exactly half the frame height crosses the rock pinnacle a third of the way up.

THE TIME MOMENT: The line is legible for the first time: two raw cuts facing each other across the valley, at the height the crossing will run — and between them, nothing.

COMPOSITION: Horizontal 16:9. The river and the valley floor sit at about twenty-five percent of frame height, the old stone arch bridge at about thirty-four percent left of centre, the twin peaks at eighty-two percent and the rock pinnacle at forty-six to fifty-eight percent. The old stone arch bridge spans about 64 pixels of frame width — one thirtieth — and keeps that width and position in every frame. The left cut runs at about forty-five to fifty percent of frame height on the left third; the right clearing sits at about the same height on the right third. The crown of the structure sits below the top eighth and the working level above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 77 degrees, elevation 3 degrees below the horizon, the last minutes before sunrise, no cast shadows, the sky orange low on the right and the twin peaks catching the first pink light. The sun stays outside the frame for the whole shot; its only sign is the shadows. Early March: bare grey larch woods, a thick snow line low on both slopes, the river low and clear.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, the river, machines and vehicles all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The dozer backs along the finished bench and drops one last windrow of spoil over the edge while the low-loader sets the tracked excavator down on the hairpin, and cars and a lorry run the old road with their headlights still on, drawing white and red trails across the stone arch bridge; dust drifts off the fresh cut. Crew register only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Bare grey-brown larch woods with a thick snow band above; the fresh cut raw brown earth with dozer tracks, a spoil windrow and stacked trunks; the old road a pale asphalt band with a dark guardrail and salt stains; the river bed pale gravel with dark wet channels.

PHYSICS: The dozer stands on its tracks on the bench with its blade lowered onto the earth; the stacked trunks rest on the slope; the excavator sits on the low-loader bed, chained down, and the low-loader stands on its tyres on the hairpin; the stone arch bridge bears on its rock abutments and carries the traffic.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The slopes, the hairpins, the stone arch bridge, the chapel, the rock pinnacle and the skyline never change shape, position, size or spacing; every pier, once built, stays where it is. The new crossing is one rigid concrete structure that only ever gains length — nothing already built is removed, moved or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, formwork, scaffolding, container, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic, no tilt-shift blur.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G1 → G2)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across a clear spring morning. Everything in this shot is time-lapsed at the same rate: the long shadows on the valley floor swing from the left toward the back as the sun climbs, cumulus clouds stretch into streaks above the peaks, the river runs milky with meltwater, and every moving machine and vehicle is smeared into a blur. First the dozer and an excavator widen both approach cuts into level platforms and a gravel haul road is pushed down the left flank to the valley floor, where pipes and rockfill are laid to make a temporary crossing over the river. Then the drilling rig walks from pit to pit, five rectangular excavations are opened and shored with steel sheets, rebar cages are lifted in from the stacks beside them and mixer trucks come down the haul road one after another to fill the pile caps, the wet concrete drying from dark to pale grey at the pits that were poured first. Traffic keeps running the hairpins throughout, and the stone arch bridge stays bare of plant.

The camera does not move at any point. The framing is identical in the first and last frame. The slopes, the hairpins of the old road, the old stone arch bridge, the chapel, the rock pinnacle and the skyline stay exactly where they are, at exactly the same size and shape, for the whole shot. The old stone arch bridge occupies exactly the same width of the frame in the first and last frame, and the eye line stays at exactly half the frame height. The valley carries exactly one old stone arch bridge and one line of new works, and no other bridge, mast or tower appears anywhere. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 2 — YÜKSELİR

```
SÜRE: 8,0 s (16,0–24,0)  ·  ELEMAN + ARA HÂL: AYAKLAR %0 → %100 + başlıklar  ·  REJİM: A  ·  SAAT: 07:15→07:25  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G2)

```
Photorealistic documentary construction photograph — Scene 2 of 15. Horizontal 16:9 time-lapse of a long concrete viaduct being pushed out across a deep alpine valley, seen from a rock spur down the valley; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur down the valley, lens 80.0 metres above the river, 380 metres from the viaduct axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one new concrete box-girder viaduct of seven spans carried on five slender piers across the valley, with the old stone arch bridge still standing on the valley floor below it. AT THIS STAGE: the approaches and the foundations are open and nothing stands above the ground yet. The earth bench on the left slope has grown into a wide approach platform at about forty-five percent of frame height and a matching cut has been opened on the right rim; between them a pale gravel haul road switchbacks down to the valley floor and crosses the river on a temporary culvert crossing of pipes and rockfill just upstream of the stone arch bridge. Five rectangular pier excavations, shored with steel sheets, stand on the floor and both flanks, with a tracked drilling rig over the nearest one.

SITE / BACKGROUND: The valley runs away from the camera between two steep larch-wooded slopes closing in high twin peaks on the skyline. On the valley floor the river comes down toward the camera under a single old stone arch bridge, and the old road crosses the valley in fourteen hairpins cut into both slopes, a pale asphalt band with a guardrail. Beside one hairpin on the left slope stands a single small chapel; on the right rim stands a single tall rock pinnacle. The valley carries exactly one old stone arch bridge and one line of new works; no other bridge, mast or tower stands anywhere from edge to edge. The eye line at exactly half the frame height crosses the rock pinnacle a third of the way up.

THE TIME MOMENT: The line is now visible end to end as earth and gravel: two approach platforms, a haul road down to the river and five open pier pits — but nothing yet rises above the valley floor.

COMPOSITION: Horizontal 16:9. The river and the valley floor sit at about twenty-five percent of frame height, the old stone arch bridge at about thirty-four percent left of centre, the twin peaks at eighty-two percent and the rock pinnacle at forty-six to fifty-eight percent. The old stone arch bridge spans about 64 pixels of frame width — one thirtieth — and keeps that width and position in every frame. The two approach cuts sit at about forty-five percent of frame height at the left and right edges of the valley; the five pier pits sit between about twenty-five and thirty-four percent on the floor and flanks. The crown of the structure sits below the top eighth and the working level above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 98 degrees, elevation 18 degrees, low morning light from the right, long shadows falling to the west, across the valley floor toward the left of the frame. The sun stays outside the frame for the whole shot; its only sign is the shadows. Early May: the larch woods flushing new light green from the valley floor upward, the snow line retreating to the upper slopes, the river running high and milky with meltwater.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, the river, machines and vehicles all move at the same accelerated speed. Two hours pass across this shot: shadows sweep the slopes, clouds stretch into streaks, and every moving machine and vehicle smears into heavy motion blur. Nothing moves at normal speed.

ACTIVITY: The drilling rig bores a pile into the nearest pier pit while a mixer truck crosses the temporary culvert crossing and discharges concrete into a pile cap; an excavator pours a fresh lift into the next pile cap and loads spoil into a dump truck that climbs the haul road, leaving deep wet ruts and a mud band across the gravel. Cars still run the hairpins; the stone arch bridge carries only light traffic and its deck stays bare of plant. Crew register only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Fresh light-green larch with a receding snow band above; raw earth platforms, sheet-piled pit walls and rebar cages laid flat in rows; the haul road pale gravel with deep ruts, a mud band at the crossing and a dust plume behind each truck; the river milky grey-green.

PHYSICS: The drilling rig stands on its tracks on the pit floor with its mast plumb and its auger pressed into the ground; the sheet piles bear against the earth and hold the pit sides; the mixer truck stands on its tyres on the culvert crossing, which rests on rockfill and pipes in the river bed; the rebar cages lie flat on timber bearers beside the pits.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The slopes, the hairpins, the stone arch bridge, the chapel, the rock pinnacle and the skyline never change shape, position, size or spacing; every pier, once built, stays where it is. The new crossing is one rigid concrete structure that only ever gains length — nothing already built is removed, moved or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, formwork, scaffolding, container, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic, no tilt-shift blur.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G2 → G3)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Ten minutes pass across a clear late-summer morning. Everything in this shot is time-lapsed at the same rate: the long pier shadows stay almost where they are, thin clouds drift in one smooth flow above the peaks, and machines and vehicles move fast but stay recognisable. A mixer truck feeds the concrete pump at the foot of the middle pier and the pump line lifts one more lift of concrete into the climbing formwork, so the ring rises a notch and the fresh grey band under the pier head widens; a dump truck climbs the haul road with spoil, and crew streaks strike the formwork on the pier behind it and lower the panels to the ground. Traffic keeps running the hairpins and the stone arch bridge stays bare of plant. The piers stand still; only the formwork, the machines and the traffic move.

The camera does not move at any point. The framing is identical in the first and last frame. The slopes, the hairpins of the old road, the old stone arch bridge, the chapel, the rock pinnacle and the skyline stay exactly where they are, at exactly the same size and shape, for the whole shot. The old stone arch bridge occupies exactly the same width of the frame in the first and last frame, and the eye line stays at exactly half the frame height. The valley carries exactly one old stone arch bridge and one line of new works, and no other bridge, mast or tower appears anywhere. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 3 — KURAR

```
SÜRE: 8,0 s (24,0–32,0)  ·  ELEMAN + ARA HÂL: DÖKÜM ALANI 0 → %100 · ilk kesit + çelik burun  ·  REJİM: B  ·  SAAT: 07:25→09:25  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G3)

```
Photorealistic documentary construction photograph — Scene 3 of 15. Horizontal 16:9 time-lapse of a long concrete viaduct being pushed out across a deep alpine valley, seen from a rock spur down the valley; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur down the valley, lens 80.0 metres above the river, 380 metres from the viaduct axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one new concrete box-girder viaduct of seven spans carried on five slender piers across the valley, with the old stone arch bridge still standing on the valley floor below it. AT THIS STAGE: the five piers stand at full height and nothing spans between them. Out of the five pile caps rise five slender grey concrete piers, each a pair of tapering shafts, the tallest in mid-valley reaching about forty-four percent of frame height and the others stepping down the flanks. Each pier still carries its galvanised climbing formwork ring under the head, with a concrete pump line strapped up one shaft and a small working platform on top; the newest lifts are darker grey than the ones below them. The haul road and the temporary culvert crossing are in daily use.

SITE / BACKGROUND: The valley runs away from the camera between two steep larch-wooded slopes closing in high twin peaks on the skyline. On the valley floor the river comes down toward the camera under a single old stone arch bridge, and the old road crosses the valley in fourteen hairpins cut into both slopes, a pale asphalt band with a guardrail. Beside one hairpin on the left slope stands a single small chapel; on the right rim stands a single tall rock pinnacle. The valley carries exactly one old stone arch bridge and one line of new works; no other bridge, mast or tower stands anywhere from edge to edge. The eye line at exactly half the frame height crosses the rock pinnacle a third of the way up.

THE TIME MOMENT: Five piers now stand where five pits were, their heads all at one level line — the valley has been measured out, and the gap between them is the whole film.

COMPOSITION: Horizontal 16:9. The river and the valley floor sit at about twenty-five percent of frame height, the old stone arch bridge at about thirty-four percent left of centre, the twin peaks at eighty-two percent and the rock pinnacle at forty-six to fifty-eight percent. The old stone arch bridge spans about 64 pixels of frame width — one thirtieth — and keeps that width and position in every frame. The pier heads sit at about forty-four percent of frame height on one level line from about twenty-four to seventy-six percent of frame width; the middle pier spans about 202 pixels of frame height. The crown of the structure sits below the top eighth and the working level above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 99 degrees, elevation 20 degrees, morning light from the right, long shadows falling to the west, the piers throwing long bars across the valley floor. The sun stays outside the frame for the whole shot; its only sign is the shadows. Late August: the larch woods deep green, snow only on the twin peaks, the river low, clear and braided in its gravel bed.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, the river, machines and vehicles all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: A mixer truck feeds the concrete pump at the foot of the middle pier and the pump line lifts a fresh lift of concrete into the climbing formwork, while a dump truck climbs the haul road and crew streaks strike the formwork ring on the pier behind it, a dust band drifting off the platform. Cars run the hairpins; the stone arch bridge carries only light traffic and its deck stays bare of plant. Crew register only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Grey formed concrete with horizontal form-tie bands and darker, damper lifts near the tops; galvanised formwork rings and a black pump line strapped to one shaft; the haul road pale gravel with deep ruts and a mud band at the crossing; spoil cones beside the pile caps; the river bed pale dry gravel with dark wet channels.

PHYSICS: Each pier bears on its own pile cap founded in the valley floor; the climbing formwork ring is bolted to the hardened concrete below it and held by its own jacks; the pump line is strapped to the shaft and rests on the ground at its foot; the mixer truck stands on its tyres on the haul road with its chute lowered into the pump hopper.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The slopes, the hairpins, the stone arch bridge, the chapel, the rock pinnacle and the skyline never change shape, position, size or spacing; every pier, once built, stays where it is. The new crossing is one rigid concrete structure that only ever gains length — nothing already built is removed, moved or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, formwork, scaffolding, container, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic, no tilt-shift blur.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G3 → G4)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across a bright autumn morning. Everything in this shot is time-lapsed at the same rate: the shadows on the valley floor shorten and swing toward the back as the sun climbs, cumulus stretches into streaks, and every moving machine and vehicle is smeared into a blur. On the plateau behind the left approach a long open casting shed goes up and a launching bed is built out of it toward the valley, its steel sliding bearings set in a line. Then rebar cages come off the stacks into the formwork, mixer trucks fill it, and the first grey concrete segment sets on the bed, its end face marked by a darker pour joint. Finally a mobile crane lifts the rust-red steel nose up piece by piece and crew streaks bolt it to the front of that segment until it reaches out past the left abutment over the first span. The five piers stand still with their formwork struck; on the slopes the larch needles turn from green to gold.

The camera does not move at any point. The framing is identical in the first and last frame. The slopes, the hairpins of the old road, the old stone arch bridge, the chapel, the rock pinnacle and the skyline stay exactly where they are, at exactly the same size and shape, for the whole shot. The old stone arch bridge occupies exactly the same width of the frame in the first and last frame, and the eye line stays at exactly half the frame height. The valley carries exactly one old stone arch bridge and one line of new works, and no other bridge, mast or tower appears anywhere. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 4 — İTER

```
SÜRE: 8,0 s (32,0–40,0)  ·  ELEMAN + ARA HÂL: TABLİYE %0 → %14 (A1 → P1)  ·  REJİM: A  ·  SAAT: 09:25→09:35  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G4)

```
Photorealistic documentary construction photograph — Scene 4 of 15. Horizontal 16:9 time-lapse of a long concrete viaduct being pushed out across a deep alpine valley, seen from a rock spur down the valley; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur down the valley, lens 80.0 metres above the river, 380 metres from the viaduct axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one new concrete box-girder viaduct of seven spans carried on five slender piers across the valley, with the old stone arch bridge still standing on the valley floor below it. AT THIS STAGE: the launching yard is finished and the first deck segment is cast. Behind the left approach stands a long open casting shed with a launching bed running out of it toward the valley; on the bed sits the first grey concrete box segment, its end face marked by a darker pour joint, with launching jacks at its back and stacks of rebar and formwork panels beside it. Bolted to the front of that segment is a rust-red steel launching nose, a slender lattice girder reaching past the left abutment to about seventeen percent of frame width, hanging over the first span. The five piers stand ready, their formwork rings struck.

SITE / BACKGROUND: The valley runs away from the camera between two steep larch-wooded slopes closing in high twin peaks on the skyline. On the valley floor the river comes down toward the camera under a single old stone arch bridge, and the old road crosses the valley in fourteen hairpins cut into both slopes, a pale asphalt band with a guardrail. Beside one hairpin on the left slope stands a single small chapel; on the right rim stands a single tall rock pinnacle. The valley carries exactly one old stone arch bridge and one line of new works; no other bridge, mast or tower stands anywhere from edge to edge. The eye line at exactly half the frame height crosses the rock pinnacle a third of the way up.

THE TIME MOMENT: The valley now has a machine aimed at it: one concrete segment on a bed, a steel nose pointing over the first span, and five bare pier heads waiting in a line.

COMPOSITION: Horizontal 16:9. The river and the valley floor sit at about twenty-five percent of frame height, the old stone arch bridge at about thirty-four percent left of centre, the twin peaks at eighty-two percent and the rock pinnacle at forty-six to fifty-eight percent. The old stone arch bridge spans about 64 pixels of frame width — one thirtieth — and keeps that width and position in every frame. The casting shed and launching bed occupy the left edge up to about ten percent of frame width; the nose tip reaches about seventeen percent at deck level, about forty-five percent of frame height. The crown of the structure sits below the top eighth and the working level above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 127 degrees, elevation 39 degrees, mid-morning light from the right and behind, shorter shadows falling to the north-west, away from the camera. The sun stays outside the frame for the whole shot; its only sign is the shadows. Late October: the larch woods turning gold along both slopes, the first snow back on the twin peaks, the river low and clear.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, the river, machines and vehicles all move at the same accelerated speed. Two hours pass across this shot: shadows sweep the slopes, clouds stretch into streaks, and every moving machine and vehicle smears into heavy motion blur. Nothing moves at normal speed.

ACTIVITY: A mobile crane at the shed lifts a rebar cage off the stack and sets it into the formwork of the next segment, while a mixer truck discharges into the shed and crew streaks bolt the last panels of the steel nose together on the bed, leaving track marks and a dust film across the yard. Cars run the hairpins below; the stone arch bridge carries only light traffic and its deck stays bare of plant. Crew register only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Grey formed concrete with form-tie bands and one darker pour joint on the first segment; rust-red steel lattice with bolted splice plates; stacks of rebar and oiled formwork panels on timber bearers; the yard gravel with track marks and a slurry patch at the shed mouth; gold larch on both slopes.

PHYSICS: The first segment rests on the launching bed on steel sliding bearings; the launching jacks are anchored into the concrete of the abutment behind it; the steel nose is bolted to the front face of the segment and cantilevers unsupported over the first span; the mobile crane stands on its outriggers on the yard, its hook block hanging vertically on a taut cable and carrying a visible load.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The slopes, the hairpins, the stone arch bridge, the chapel, the rock pinnacle and the skyline never change shape, position, size or spacing; every pier, once built, stays where it is. The new crossing is one rigid concrete structure that only ever gains length — nothing already built is removed, moved or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, formwork, scaffolding, container, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic, no tilt-shift blur.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G4 → G5)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across a clear autumn day. Everything in this shot is time-lapsed at the same rate: the shadows on the valley floor swing from the left toward the back as the sun climbs, cumulus clouds stretch into long streaks, and every moving machine and vehicle is smeared into a blur. First the launching jacks push the deck forward out of the casting shed, the whole grey box sliding as one piece over the left abutment while the segment with the darker pour joint stays at its front; the rust-red nose runs out ahead of it over the first span, drops onto the first pier head and slides across it onto the bearings. Then the deck comes to rest with its end on that pier, the jacks are reset at the back, and in the shed a mixer truck fills the formwork of the next segment. No new section appears ahead of the nose; the piers, the abutments and the casting shed stand still. On the slopes the gold larch needles thin toward bare branches and traffic keeps running the hairpins.

The camera does not move at any point. The framing is identical in the first and last frame. The slopes, the hairpins of the old road, the old stone arch bridge, the chapel, the rock pinnacle and the skyline stay exactly where they are, at exactly the same size and shape, for the whole shot. The old stone arch bridge occupies exactly the same width of the frame in the first and last frame, and the eye line stays at exactly half the frame height. The valley carries exactly one old stone arch bridge and one line of new works, and no other bridge, mast or tower appears anywhere. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 5 — EKLER

```
SÜRE: 8,0 s (40,0–48,0)  ·  ELEMAN + ARA HÂL: TABLİYE %14 → %32 (P1 → P2)  ·  REJİM: A  ·  SAAT: 09:35→09:45  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G5)

```
Photorealistic documentary construction photograph — Scene 5 of 15. Horizontal 16:9 time-lapse of a long concrete viaduct being pushed out across a deep alpine valley, seen from a rock spur down the valley; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur down the valley, lens 80.0 metres above the river, 380 metres from the viaduct axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one new concrete box-girder viaduct of seven spans carried on five slender piers across the valley, with the old stone arch bridge still standing on the valley floor below it. AT THIS STAGE: the first push is done and the deck has reached the first pier. The grey concrete deck now runs from the casting shed out over the left abutment to the first pier at about twenty-four percent of frame width, resting on it, and the rust-red steel nose reaches on past it to about thirty-two percent, hanging over the second span with nothing under it. The segment with the darker pour joint sits at the front, just behind the nose. In the shed a new segment stands in its formwork, and the launching jacks sit at the back of the deck on the bed.

SITE / BACKGROUND: The valley runs away from the camera between two steep larch-wooded slopes closing in high twin peaks on the skyline. On the valley floor the river comes down toward the camera under a single old stone arch bridge, and the old road crosses the valley in fourteen hairpins cut into both slopes, a pale asphalt band with a guardrail. Beside one hairpin on the left slope stands a single small chapel; on the right rim stands a single tall rock pinnacle. The valley carries exactly one old stone arch bridge and one line of new works; no other bridge, mast or tower stands anywhere from edge to edge. The eye line at exactly half the frame height crosses the rock pinnacle a third of the way up.

THE TIME MOMENT: The deck has left the land: it stands on the first pier, and the nose hangs out over the next gap — the valley is being crossed a span at a time.

COMPOSITION: Horizontal 16:9. The river and the valley floor sit at about twenty-five percent of frame height, the old stone arch bridge at about thirty-four percent left of centre, the twin peaks at eighty-two percent and the rock pinnacle at forty-six to fifty-eight percent. The old stone arch bridge spans about 64 pixels of frame width — one thirtieth — and keeps that width and position in every frame. The deck line runs at about forty-five percent of frame height from the left edge to about twenty-four percent of frame width, the nose tip at about thirty-two percent. The crown of the structure sits below the top eighth and the working level above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 129 degrees, elevation 41 degrees, mid-morning light from the right and behind, short shadows falling to the north-west, away from the camera. The sun stays outside the frame for the whole shot; its only sign is the shadows. Early November: the larch woods dropping their needles, the slopes rust and grey, the snow line low on the peaks, the river dark and low.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, the river, machines and vehicles all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The launching jacks push the deck forward as one piece and the nose slides across the first pier head onto its bearings, while a mixer truck fills the formwork of the next segment in the shed and crew streaks work along the launching bed, dust lifting off the yard gravel behind the moving deck. Cars run the hairpins; the stone arch bridge carries only light traffic and its deck stays bare of plant. Crew register only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Grey formed concrete with form-tie bands and one darker pour joint near the front; rust-red steel lattice with bolted splices; sliding bearings and steel plates on the pier heads; the yard gravel with track marks and a dust film; rust-brown larch slopes with bare grey branches showing through.

PHYSICS: The deck rests on steel sliding bearings on the launching bed and on the first pier head, and bears its own weight along that line; the steel nose is bolted to the front of the deck and cantilevers unsupported over the second span; the launching jacks are anchored into the abutment concrete and push against the deck; the piers stand on their pile caps and do not move.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The slopes, the hairpins, the stone arch bridge, the chapel, the rock pinnacle and the skyline never change shape, position, size or spacing; every pier, once built, stays where it is. The new crossing is one rigid concrete structure that only ever gains length — nothing already built is removed, moved or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, formwork, scaffolding, container, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic, no tilt-shift blur.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G5 → G6)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Ten minutes pass across a clear late-autumn morning. Everything in this shot is time-lapsed at the same rate: the shadows stay almost where they are, thin clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable. In the casting shed the newest segment is stripped of its formwork and joined to the back of the deck; then the launching jacks push the whole deck forward as one piece, the grey box sliding out over the first pier while the segment with the darker pour joint stays at its front and the rust-red nose runs ahead over the second span and settles onto the second pier head. No new section appears ahead of the nose; the piers, the abutments and the casting shed stand still. Traffic keeps running the hairpins below and the stone arch bridge stays bare of plant.

The camera does not move at any point. The framing is identical in the first and last frame. The slopes, the hairpins of the old road, the old stone arch bridge, the chapel, the rock pinnacle and the skyline stay exactly where they are, at exactly the same size and shape, for the whole shot. The old stone arch bridge occupies exactly the same width of the frame in the first and last frame, and the eye line stays at exactly half the frame height. The valley carries exactly one old stone arch bridge and one line of new works, and no other bridge, mast or tower appears anywhere. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 6 — UZANIR

```
SÜRE: 8,0 s (48,0–56,0)  ·  ELEMAN + ARA HÂL: TABLİYE %32 → %50 (P2 → P3) · geçici destek kurulur  ·  REJİM: B  ·  SAAT: 09:45→11:45  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G6)

```
Photorealistic documentary construction photograph — Scene 6 of 15. Horizontal 16:9 time-lapse of a long concrete viaduct being pushed out across a deep alpine valley, seen from a rock spur down the valley; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur down the valley, lens 80.0 metres above the river, 380 metres from the viaduct axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one new concrete box-girder viaduct of seven spans carried on five slender piers across the valley, with the old stone arch bridge still standing on the valley floor below it. AT THIS STAGE: the deck stands on two piers and the gap ahead is the widest yet. The grey concrete deck runs from the casting shed over the left abutment and the first pier to the second pier at about thirty-seven percent of frame width and the rust-red nose reaches on to about forty-five percent, hanging over the middle of the valley with nothing under it. The segment with the darker pour joint is still at the front. In the shed the next segment stands in its formwork, and a crawler crane tracks down the haul road with the first parts of a temporary steel support.

SITE / BACKGROUND: The valley runs away from the camera between two steep larch-wooded slopes closing in high twin peaks on the skyline. On the valley floor the river comes down toward the camera under a single old stone arch bridge, and the old road crosses the valley in fourteen hairpins cut into both slopes, a pale asphalt band with a guardrail. Beside one hairpin on the left slope stands a single small chapel; on the right rim stands a single tall rock pinnacle. The valley carries exactly one old stone arch bridge and one line of new works; no other bridge, mast or tower stands anywhere from edge to edge. The eye line at exactly half the frame height crosses the rock pinnacle a third of the way up.

THE TIME MOMENT: The deck has crossed two piers and is now aimed at the middle of the valley, where the river and the old stone arch bridge are — the longest reach of the film is about to begin.

COMPOSITION: Horizontal 16:9. The river and the valley floor sit at about twenty-five percent of frame height, the old stone arch bridge at about thirty-four percent left of centre, the twin peaks at eighty-two percent and the rock pinnacle at forty-six to fifty-eight percent. The old stone arch bridge spans about 64 pixels of frame width — one thirtieth — and keeps that width and position in every frame. The deck line runs at about forty-five percent of frame height to about thirty-seven percent of frame width, the nose tip at about forty-five percent of frame width, above the stone arch bridge. The crown of the structure sits below the top eighth and the working level above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 131 degrees, elevation 42 degrees, late-morning light from the right and behind, short shadows falling to the north-west, away from the camera. The sun stays outside the frame for the whole shot; its only sign is the shadows. Early December: the larch woods bare and grey-brown, fresh snow on the twin peaks and a new snow line reaching the upper slopes, the river dark and low.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, the river, machines and vehicles all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The launching jacks push the deck forward as one piece over the second pier head while the crawler crane carries steel support parts down the haul road and a mixer truck fills the formwork of the next segment in the shed; the sliding bearings leave bright steel lines on the pier heads and dust lifts off the yard. Cars run the hairpins; the stone arch bridge carries only light traffic and its deck stays bare of plant. Crew register only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Grey formed concrete with form-tie bands and one darker pour joint near the front; rust-red steel lattice with bolted splices; bright steel sliding bearings on the pier heads; the haul road pale gravel with ruts and a mud band at the crossing; bare larch slopes with a fresh snow band above.

PHYSICS: The deck rests on sliding bearings on the launching bed and on the first two pier heads and bears its weight along that line; the steel nose is bolted to its front and cantilevers unsupported over the third span; the launching jacks are anchored into the abutment concrete; the crawler crane stands on its tracks on the haul road, its hook block hanging vertically on a taut cable and carrying a visible load.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The slopes, the hairpins, the stone arch bridge, the chapel, the rock pinnacle and the skyline never change shape, position, size or spacing; every pier, once built, stays where it is. The new crossing is one rigid concrete structure that only ever gains length — nothing already built is removed, moved or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, formwork, scaffolding, container, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic, no tilt-shift blur.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G6 → G7)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across a winter day under a lowering sky. Everything in this shot is time-lapsed at the same rate: the short shadows swing behind the piers as the sun crosses low, a grey cloud deck washes across the peaks, and every moving machine and vehicle is smeared into a blur. First the snow line comes down the slopes until the bare larch woods stand in white, and a crawler crane tracks down the haul road and builds a braced trestle tower on a rockfill pad on the gravel flat beside the river, bolting its diagonals in one by one. Meanwhile the shed keeps working: a segment is stripped of its formwork, joined to the back of the deck and the next cage is set in the empty mould, and crew streaks grease and set the sliding bearings on the third pier head. Then the launching jacks push the deck forward as one piece, the grey box sliding over the second pier and out across the river until its end rests on the middle pier and the rust-red nose reaches over the trestle. Only the deck slides; the piers, the trestle and the shed stand still.

The camera does not move at any point. The framing is identical in the first and last frame. The slopes, the hairpins of the old road, the old stone arch bridge, the chapel, the rock pinnacle and the skyline stay exactly where they are, at exactly the same size and shape, for the whole shot. The old stone arch bridge occupies exactly the same width of the frame in the first and last frame, and the eye line stays at exactly half the frame height. The valley carries exactly one old stone arch bridge and one line of new works, and no other bridge, mast or tower appears anywhere. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 7 — ZORLAR

```
SÜRE: 8,0 s (56,0–64,0)  ·  ELEMAN + ARA HÂL: TABLİYE %50 → %63 (P3 → P4) · su yükselirken itme sürer  ·  REJİM: B  ·  SAAT: 11:45→13:45  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G7)

```
Photorealistic documentary construction photograph — Scene 7 of 15. Horizontal 16:9 time-lapse of a long concrete viaduct being pushed out across a deep alpine valley, seen from a rock spur down the valley; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur down the valley, lens 80.0 metres above the river, 380 metres from the viaduct axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one new concrete box-girder viaduct of seven spans carried on five slender piers across the valley, with the old stone arch bridge still standing on the valley floor below it. AT THIS STAGE: the deck has reached the middle pier and a temporary support stands in the river flat. The grey concrete deck runs from the casting shed to the middle pier at about fifty percent of frame width, resting on it, and the rust-red nose reaches on to about fifty-eight percent. Under the nose, on the gravel flat beside the river, a braced steel trestle tower stands on a rockfill pad at about fifty-seven percent of frame width, its head just under the deck line. The temporary culvert crossing carries a mixer truck, and the shed holds the next segment in its formwork.

SITE / BACKGROUND: The valley runs away from the camera between two steep larch-wooded slopes closing in high twin peaks on the skyline. On the valley floor the river comes down toward the camera under a single old stone arch bridge, and the old road crosses the valley in fourteen hairpins cut into both slopes, a pale asphalt band with a guardrail. Beside one hairpin on the left slope stands a single small chapel; on the right rim stands a single tall rock pinnacle. The valley carries exactly one old stone arch bridge and one line of new works; no other bridge, mast or tower stands anywhere from edge to edge. The eye line at exactly half the frame height crosses the rock pinnacle a third of the way up.

THE TIME MOMENT: The deck stands over the river on the middle pier, with a steel trestle under its nose — the valley is half crossed, and everything now depends on the water below.

COMPOSITION: Horizontal 16:9. The river and the valley floor sit at about twenty-five percent of frame height, the old stone arch bridge at about thirty-four percent left of centre, the twin peaks at eighty-two percent and the rock pinnacle at forty-six to fifty-eight percent. The old stone arch bridge spans about 64 pixels of frame width — one thirtieth — and keeps that width and position in every frame. The deck line runs at about forty-five percent of frame height to about fifty percent of frame width; the trestle head sits just under it at about fifty-seven percent of frame width. The crown of the structure sits below the top eighth and the working level above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 172 degrees, elevation 52 degrees, midday light from behind the camera, very short shadows falling to the north, away from the camera, the light flat under cloud. The sun stays outside the frame for the whole shot; its only sign is the shadows. Late April: a low grey overcast lid over the valley, the snow line down on the upper slopes and beginning to melt, the larch buds just breaking, the river rising and grey-green.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, the river, machines and vehicles all move at the same accelerated speed. Two hours pass across this shot: shadows sweep the slopes, clouds stretch into streaks, and every moving machine and vehicle smears into heavy motion blur. Nothing moves at normal speed.

ACTIVITY: The launching jacks push the deck the last metres onto the middle pier head while the crawler crane bolts the last diagonal into the steel trestle below and a mixer truck crosses the temporary culvert crossing with a load for the shed; meltwater darkens the gravel flat and the river spreads along its bed. Cars run the hairpins; the stone arch bridge carries only light traffic and its deck stays bare of plant. Crew register only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Grey formed concrete with form-tie bands, the front segment's pour joint still darker; rust-red steel lattice; a galvanised trestle on a rockfill pad with a wet dark band at its foot; the culvert crossing with a mud band and deep ruts; bare larch slopes with a melting snow band; the river grey-green and rising.

PHYSICS: The deck rests on sliding bearings on the launching bed and on the first three pier heads; the steel nose is bolted to its front and reaches over the trestle head; the trestle stands on a rockfill pad on the gravel flat and is braced back to the river bank; the crawler crane's hook block hangs vertically on a taut cable and carries a visible load; the mixer truck stands on its tyres on the culvert crossing, which rests on pipes and rockfill in the river bed.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The slopes, the hairpins, the stone arch bridge, the chapel, the rock pinnacle and the skyline never change shape, position, size or spacing; every pier, once built, stays where it is. The new crossing is one rigid concrete structure that only ever gains length — nothing already built is removed, moved or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, formwork, scaffolding, container, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic, no tilt-shift blur.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G7 → G8)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across a warm, wet spring day. Everything in this shot is time-lapsed at the same rate: a grey cloud deck rolls up the valley in a continuous blur, meltwater runs off the slopes, and every moving machine and vehicle is smeared into a blur. First the jacks push twice: the deck slides across the trestle head and onto the fourth pier while another segment is joined at its tail in the shed, and the rust-red nose reaches out over the last two spans. Then the weather turns on the work: the snow band shrinks upward, the river swells from grey-green to brown and spreads across its gravel bed, and dump trucks start tipping rock around the trestle pad and the two lowest pier feet, an excavator shaping it into a berm. Finally the plant is withdrawn: mixer, roller and pump climb the haul road to the high platform, a last truck crosses the culvert crossing as the water laps its approach, tarpaulins go over the formwork stacks, and the launching jacks stop with the deck resting on the fourth pier.

The camera does not move at any point. The framing is identical in the first and last frame. The slopes, the hairpins of the old road, the old stone arch bridge, the chapel, the rock pinnacle and the skyline stay exactly where they are, at exactly the same size and shape, for the whole shot. The old stone arch bridge occupies exactly the same width of the frame in the first and last frame, and the eye line stays at exactly half the frame height. The valley carries exactly one old stone arch bridge and one line of new works, and no other bridge, mast or tower appears anywhere. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```
