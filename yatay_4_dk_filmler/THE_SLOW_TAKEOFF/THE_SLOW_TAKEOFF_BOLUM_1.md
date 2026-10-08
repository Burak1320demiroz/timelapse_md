# 🎬 THE_SLOW_TAKEOFF — BÖLÜM 1  (S0 – S14 · G0 … G14 + 15 I2V · 0,0–120,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `THE_SLOW_TAKEOFF_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır. STRUCTURE bloğu 33 promptta, SITE / BACKGROUND ve NEGATIVE blokları kendi
> istasyonlarının bütün karelerinde BİREBİR aynı kelimelerle tekrarlanır; değişen AT THIS STAGE,
> THE TIME MOMENT, COMPOSITION'ın son cümlesi, LIGHTING, TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.
>
> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py`)
> ki ortak bloklar harfi harfine aynı kalsın [DERS 20].
>
> ⭐ Bu bölümün SON I2V'si (S14: G14 → G15) **G15 karesinde biter** ve G15 `BOLUM_2`'nin ilk
> görselidir: bölüm sınırı bir KAREDİR, kesme değil [DERS 52]. Kapı KLASÖR MODUNDA koşulur:
> `python3 araclar/prompt_kontrol.py yatay_4_dk_filmler/THE_SLOW_TAKEOFF`.
>
> 🪟 **S13 KOKPİT EKİDİR** (sahip kararı 07.10.2026 — "tek kamera + 2 kokpit"): S12'nin I2V'si
> ana kare **G14**'e biter, S13 kokpitte G13 → G13′ koşar, S14 yine G14'ten başlar. Kokpit
> karelerinin SITE bloğu ana SITE ile iki cümleyi BİREBİR paylaşır (uzak kıyı + ufuk) [DERS 10].
>
> ⛔ Kelime kilitleri: "crane" yalnız G0 · G1 · G3 · G4 ve S0–S4 I2V'lerinde; "canoe" yalnız G25'ten
> sonra; YASAK KELİME (PLAN künyesi) hiçbir promptta yok — negatifte bile.

---

## 🎬 SAHNE 0 — SÖKER

```
SÜRE: 8,0 s (0,0–8,0)  ·  ELEMAN + ARA HÂL: öndeki motor kanatta → vinçte, kamyonun üstünde (%100)  ·  REJİM: A (10 dk)  ·  SAAT: 07:40→07:50  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G0)

```
Photorealistic documentary site photograph — Scene 0 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: nothing has been moved yet except the near engine. The airliner lies on its belly in the meadow, settled into a shallow muddy trough: a dull grey-white fuselage streaked with green moss and dark grime, thick ivy climbing over the nose and the cockpit windows, a long row of small cabin windows clouded and some broken, the tail fin standing tall at the right, the near wing reaching towards the camera with its tip propped on timber blocks in the grass. The near engine has just been lifted clear of its mounting under the near wing and hangs from the hook of a yellow mobile crane parked on a gravel pad in front of the tail; a flatbed truck waits beside the crane. Long grass, nettles and young birches crowd round the fuselage.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: A quarter to eight in the morning on the first day of work: the near engine has just come off the wing and hangs a metre above the grass beside it, and the ivy still covers the nose.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly on the meadow at about forty-three percent of frame height, the top of its fuselage at about fifty-two percent, just above the far shoreline, and the top of its tail fin at about sixty-eight percent. The near engine hangs just above the grass at about the middle of the frame width. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 100 degrees, elevation 26 degrees, low on the right and slightly behind the camera, so the near side of the fuselage is lit warm and long shadows fall to the left and away. Late summer: a clear pale morning sky with a few small high clouds, a thin mist lifting off the lake, the meadow deep green and the oak in full dark leaf. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The mobile crane swings the near engine away from the wing towards the flatbed truck, two workers on the ground steady it with taglines, and a small excavator pulls the timber blocks out from under the near wingtip; the crane carries a visible load, with a heavy engine slung on the hook. Crushed grass and fresh tyre tracks mark the gravel pad. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Green moss and black grime streaks along the fuselage, ivy over the nose, flaking grey paint on the wings, a ring of damp mud round the belly and old ruts in the grass, a gravel pad with fresh tyre tracks, dew on the long grass. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The airliner rests on its belly in the soft ground of the meadow, pressed into a shallow trough. The near engine hangs from the crane hook on two taut slings, and the crane stands on its outriggers on the gravel pad. The near wingtip rests on two timber blocks.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G0 → G1)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The mobile crane swings the near engine from beneath the near wing across to the flatbed truck and holds it just above the truck bed.

Ten minutes pass in the early light. Everything in this shot is time-lapsed at the same rate. From the first frame the engine is already moving: it swings slowly away from the wing on the crane hook, steadied by two taglines, and travels across to hang just above the bed of the flatbed truck. The excavator drags the timber blocks out from under the wingtip and stacks them on a pile beside the pad. The ivy over the nose, the clouded windows and the tail fin do not change. Thin morning mist lifts off the lake behind, and the small high clouds drift slowly from the left in one smooth flow. Long shadows lean to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 1 — TEMİZLER

```
SÜRE: 8,0 s (8,0–16,0)  ·  ELEMAN + ARA HÂL: sarmaşık + kir %100 → %0 · motor kamyonda, vinç gider  ·  REJİM: A (10 dk)  ·  SAAT: 07:50→08:00  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G1)

```
Photorealistic documentary site photograph — Scene 1 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: the near engine has been carried off the wing and hangs from the crane hook on its sling just above the bed of the flatbed truck parked in front of the tail, two taglines hanging slack from it; under the near wing its bare mounting shows as a short grey stub. The rest of the airliner is unchanged: it lies on its belly in the shallow muddy trough, a dull grey-white fuselage streaked with green moss and dark grime, thick ivy over the nose and the cockpit windows, clouded cabin windows, the tail fin tall at the right, the near wing reaching towards the camera. Two mobile work platforms and a pressure-washer cart wait by the nose; long grass, nettles and young birches crowd round the fuselage.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Ten to eight in the morning: the engine hangs over the truck bed, and the clean-up of the fuselage is about to start.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly on the meadow at about forty-three percent of frame height, the top of its fuselage at about fifty-two percent, just above the far shoreline, and the top of its tail fin at about sixty-eight percent. The engine hangs over the truck at about two thirds of the frame width. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 102 degrees, elevation 27 degrees, low on the right and slightly behind the camera, so the near side of the fuselage is lit warm and long shadows fall to the left and away. Late summer: a clear pale morning sky with a few small high clouds, a thin mist lifting off the lake, the meadow deep green and the oak in full dark leaf. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The crane lowers the engine onto the flatbed truck, a team on two mobile work platforms pulls the ivy off the nose in long strips, and a pressure-washer cart sprays the first band of grime off the fuselage; the crane carries a visible load, with a heavy engine slung on the hook. Cut ivy piles up on a tarpaulin under the nose. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Green moss and black grime streaks along the fuselage, ivy over the nose, flaking grey paint on the wings, a ring of damp mud round the belly and old ruts in the grass, a gravel pad with fresh tyre tracks, dew on the long grass. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The engine hangs from the crane hook on two taut slings a metre above the truck bed. The crane stands on its outriggers on the gravel pad and the truck stands on its wheels beside it. The airliner rests on its belly in the trough.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G1 → G2)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: A team on two mobile work platforms strips the ivy and the grime from the fuselage, from the nose back to the tail, and drops the cut ivy onto a tarpaulin pile under the nose.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Early in the shot the crane lowers the engine onto the truck bed; the truck drives off along the gravel track to the right, and the crane folds its boom and follows it out of the frame. Meanwhile the work platforms creep along the fuselage: the ivy comes away in long strips, and behind the pressure-washer the old white surface appears in clean bands — the nose first, then the cabin, then the tail. Cut ivy piles up on the tarpaulin, and the small excavator lifts the cut birches onto a trailer. The small high clouds drift slowly from the left in one smooth flow and the mist over the lake thins. Long shadows lean to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 2 — DÖKER

```
SÜRE: 8,0 s (16,0–24,0)  ·  ELEMAN + ARA HÂL: temel 0 → 4 (%100) · gövde temiz  ·  REJİM: B (2 sa)  ·  SAAT: 08:00→10:00  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G2)

```
Photorealistic documentary site photograph — Scene 2 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: the airliner has been cleaned: it lies on its belly in the shallow muddy trough, its long fuselage now clean old white with faded grey on the belly, the cockpit windows and the row of cabin windows uncovered but old and clouded, some broken, the tail fin tall at the right, the near wing reaching towards the camera, and under the near wing a short grey stub where the engine hung. The grass round it has been cut short and a tarpaulin heaped with cut ivy lies under the nose. A yellow excavator waits on the gravel pad, with a stack of rebar cages and a pile of timber boards beside it; stakes with orange tape mark two squares in the grass in front of the fuselage, one ahead of the wing and one behind it, and two matching squares lie behind the fuselage.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Eight in the morning: the fuselage is clean white and the footing squares are staked out in the grass.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly on the meadow at about forty-three percent of frame height, the top of its fuselage at about fifty-two percent, just above the far shoreline, and the top of its tail fin at about sixty-eight percent. The two staked squares in front of the fuselage sit at about two fifths and three fifths of the frame width. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 104 degrees, elevation 29 degrees, low on the right and slightly behind the camera, so the near side of the fuselage is lit warm and long shadows fall to the left and away. Late summer: a clear pale morning sky with a few small high clouds, a thin mist lifting off the lake, the meadow deep green and the oak in full dark leaf. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Two hours pass across this shot: the shadows swing slowly round, the clouds streak across the sky, and machines smear into heavy motion blur. Nothing moves at normal speed.

ACTIVITY: The excavator digs the first footing pit beside the fuselage and swings the spoil onto a heap, a concrete mixer truck backs along the gravel track, and the crew lowers a rebar cage into the open pit; fresh tyre ruts cut across the short grass. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Dry matte light-grey concrete with formwork edges and spatter on the grass, red primer on the steel with rust-brown streaks at the bolts, heaps of brown spoil, mud and tyre ruts round the footings, cut grass flattened into tracks, dried mud along the belly. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The airliner rests on its belly in the trough. The excavator stands on its tracks on the gravel pad, its bucket bearing on the ground at the pit edge. The rebar cages lie stacked on timber bearers that rest on the grass.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G2 → G3)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The excavator digs four square footing pits beside the fuselage, the crew lowers a rebar cage from the stack into each pit, and the mixer truck pours concrete from its chute into the pits, nose side first, then tail side.

Two hours pass. Everything in this shot is time-lapsed at the same rate. The excavator works its way round the fuselage, digging and swinging spoil onto heaps; each pit gets its rebar cage and then its grey concrete, and four ringed groups of anchor bolts stand out of the fresh tops, two in front of the fuselage and two behind it. The mixer truck comes and goes along the gravel track. Late in the shot the yellow mobile crane drives back in and parks on the pad in front of the tail, and a long truck brings a load of red steel columns and beams and stops beside it; the crane lifts the first column from the truck. The shadows of the fuselage and the oak swing slowly from the left towards the back of the meadow as the sun climbs, and the clouds streak slowly across from the left.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 3 — DİKER

```
SÜRE: 8,0 s (24,0–32,0)  ·  ELEMAN + ARA HÂL: çerçeve 0 → 2 (kolon 4 · üst kiriş 2) %100  ·  REJİM: A (10 dk)  ·  SAAT: 10:00→10:10  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G3)

```
Photorealistic documentary site photograph — Scene 3 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: four square concrete footings have been poured beside the fuselage, two in front of it and two behind it, each with a ring of anchor bolts standing out of its fresh grey top and a heap of brown spoil beside it. The airliner lies unchanged on its belly in the trough, clean old white, its cockpit and cabin windows clouded, the tail fin tall at the right, the near wing reaching towards the camera. The yellow mobile crane stands on its outriggers on the gravel pad in front of the tail and lifts the first red steel column on a short sling from a long truck loaded with columns and beams; the excavator and the mixer truck are parked at the right.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Ten in the morning: the four footings are poured and the first steel column is in the air.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly on the meadow at about forty-three percent of frame height, the top of its fuselage at about fifty-two percent, just above the far shoreline, and the top of its tail fin at about sixty-eight percent. The two near footings sit at about two fifths and three fifths of the frame width. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 134 degrees, elevation 47 degrees, high on the right behind the camera, lighting the near side of the fuselage, with short shadows falling to the left and away. Early autumn: a clear blue sky with small white fair-weather clouds, the meadow turning yellow-green and the oak still green with the first yellow leaves. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The crane lifts a red steel column from the truck and swings it onto the first footing, two riggers bolt its base plate down, and a telehandler carries a bundle of bracing from the truck; the crane carries a visible load, with a red steel column on the hook. Concrete spatter and spoil heaps lie round the footings. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Dry matte light-grey concrete with formwork edges and spatter on the grass, red primer on the steel with rust-brown streaks at the bolts, heaps of brown spoil, mud and tyre ruts round the footings, cut grass flattened into tracks, dried mud along the belly. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The column hangs from the crane hook on a short sling, its base plate just above the anchor bolts of the footing. The crane stands on its outriggers on the gravel pad. The airliner rests on its belly in the trough, and the footings are planted in the ground beside it.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G3 → G4)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The crane lifts the red steel columns one by one from the long truck onto the anchor bolts beside the fuselage and then sets two red top beams across them, one ahead of the wing and one behind it, forming two steel frames that straddle the fuselage.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Each column swings over on the hook, is lowered onto its anchor bolts and bolted down while a rigger holds it plumb; then a top beam rises from the truck on the hook and is lowered across each pair of columns, high above the fuselage. The telehandler lifts four small grey jack units from the truck onto the beam tops, two on each beam, with their lifting cables coiled beside them. The airliner does not move. The small white clouds drift slowly from the left in one smooth flow, and the short shadows lean to the left and away.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 4 — BAĞLAR

```
SÜRE: 8,0 s (32,0–40,0)  ·  ELEMAN + ARA HÂL: beşik 0 → 2 · halat 0 → 4 gergin · uçak yerde  ·  REJİM: A (10 dk)  ·  SAAT: 10:10→10:20  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G4)

```
Photorealistic documentary site photograph — Scene 4 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: two red steel steel frames now straddle the fuselage, one between the cockpit and the wing and one between the wing and the tail: each is two tall columns bolted on the concrete footings, one in front of the fuselage and one behind it, joined high above the fuselage by a red top beam carrying two small grey jack units with coiled lifting cables. The airliner lies unchanged on its belly in the trough between them, clean old white, its windows clouded. The yellow mobile crane stands on its outriggers on the gravel pad in front of the tail and holds the first curved steel saddle beam on a sling; the excavator digs a narrow trench under the belly beside the first steel frame.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Ten past ten: both steel frames stand over the fuselage and the first saddle beam is on the hook.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly on the meadow at about forty-three percent of frame height, the top of its fuselage at about fifty-two percent, just above the far shoreline, and the top of its tail fin at about sixty-eight percent. The two steel frames rise at about two fifths and three fifths of the frame width, their top beams at about seventy percent of frame height. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 137 degrees, elevation 48 degrees, high on the right behind the camera, lighting the near side of the fuselage, with short shadows falling to the left and away. Early autumn: a clear blue sky with small white fair-weather clouds, the meadow turning yellow-green and the oak still green with the first yellow leaves. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The excavator digs a narrow trench under the belly at each steel frame, the crane threads a curved steel saddle beam through each trench beneath the fuselage, and riggers on the beam tops pull the lifting cables down and shackle them to the saddle ends; the crane carries a visible load, with a curved saddle beam on the hook. Spoil from the trenches lies in two heaps. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Dry matte light-grey concrete with formwork edges and spatter on the grass, red primer on the steel with rust-brown streaks at the bolts, heaps of brown spoil, mud and tyre ruts round the footings, cut grass flattened into tracks, dried mud along the belly. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The saddle beam hangs from the crane hook on a short sling. The frame columns stand bolted on their footings and the top beams are bolted across them, each carrying its jack units. The airliner rests on its belly in the trough.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G4 → G5)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The crane threads two curved steel saddle beams from the truck into trenches under the belly, and the riggers draw the lifting cables down from the jack units on the top beams onto the saddle ends and pull them taut.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The crane lifts the second saddle beam from the truck and threads it under the belly at the second steel frame. When both saddles are in place the four cables are drawn tight one after another and stand straight and taut from the beam tops down to the saddle ends; the airliner has not yet moved. The crane then folds its boom and drives off along the gravel track to the right and out of the frame, and the excavator backfills the trench edges. The small white clouds drift slowly from the left in one smooth flow, and the short shadows lean to the left and away.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 5 — KALKAR ①

```
SÜRE: 8,0 s (40,0–48,0)  ·  ELEMAN + ARA HÂL: uçak 0 → +3,0 m (%50) · halatlar çeker  ·  REJİM: A (10 dk)  ·  SAAT: 10:20→10:30  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G5)

```
Photorealistic documentary site photograph — Scene 5 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: the airliner is ready to rise but has not moved: it lies on its belly in the trough between the two red steel frames, and under its belly at each frame a curved steel saddle beam runs across beneath the fuselage, its two ends shackled to two taut steel lifting cables and their slings, which run straight up to the jack units on the red top beam. The cables are drawn tight; the fuselage is still pressed into the mud. The clean old white fuselage, the clouded windows, the tall tail fin at the right and the near wing reaching towards the camera are unchanged. A telehandler and two work platforms stand at the right, and the excavator is parked by the nose; backfilled spoil lies round the saddle ends.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Twenty past ten: all four lifting cables are taut and the airliner is still on the ground — the moment before it rises.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly on the meadow at about forty-three percent of frame height, the top of its fuselage at about fifty-two percent, just above the far shoreline, and the top of its tail fin at about sixty-eight percent. The four taut cables run straight up from the belly to the top beams at about seventy percent of frame height. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 141 degrees, elevation 49 degrees, high on the right behind the camera, lighting the near side of the fuselage, with short shadows falling to the left and away. Early autumn: a clear blue sky with small white fair-weather clouds, the meadow turning yellow-green and the oak still green with the first yellow leaves. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The four jack units on the top beams pull the cables up in short even strokes and lift the saddle beams with the airliner on them, riggers on the beam tops watch the cables, and the telehandler moves a work platform clear of the near wing; mud drips from the belly as it leaves the trough. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Dry matte light-grey concrete with formwork edges and spatter on the grass, red primer on the steel with rust-brown streaks at the bolts, heaps of brown spoil, mud and tyre ruts round the footings, cut grass flattened into tracks, dried mud along the belly. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The airliner still rests on its belly in the mud, with the two saddle beams lying under it; each saddle end is shackled to one taut lifting cable running up to a jack unit bolted on a red top beam, and the frame columns stand bolted on their footings.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G5 → G6)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The four jack units on the red top beams draw the cables upward and raise the airliner, resting on its two saddle beams, straight up from the muddy trough to half of its final height.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the cables are pulling: the fuselage breaks free of the mud with a shudder of falling clods, then rises slowly and evenly, level, nose and tail together, the wings and the tail fin moving with it as one rigid body. A dark gap opens and widens beneath the belly, and the shallow muddy trough appears below it, its shape the exact print of the belly. By the end of the shot the belly hangs about three metres above the meadow. The telehandler lifts a pallet of steel pins from the truck up to the riggers on the first beam top. The small white clouds drift slowly from the left in one smooth flow, and the shadow of the airliner begins to slide out from under it to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 6 — KALKAR ②

```
SÜRE: 8,0 s (48,0–56,0)  ·  ELEMAN + ARA HÂL: uçak +3,0 → +6,0 m (%100)  ·  REJİM: A (10 dk)  ·  SAAT: 10:30→10:40  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G6)

```
Photorealistic documentary site photograph — Scene 6 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: the airliner hangs halfway up: its belly about three metres above the meadow, level, resting on the two curved saddle beams, which hang on their slings from four taut steel cables running up to the jack units on the red top beams of the two steel frames. Beneath it the shallow muddy trough lies open in the grass, the exact print of the belly, with clods of mud fallen into it. The fuselage is clean old white with clouded windows, the tail fin tall at the right, the near wing reaching towards the camera above the grass; the telehandler stands by the near wingtip with a pallet on its forks.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Half past ten: the airliner hangs halfway up, its belly three metres above its empty muddy bed.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly level with the far shoreline at exactly half the frame height, the top of its fuselage at about fifty-nine percent and the top of its tail fin at about seventy-five percent. The empty trough lies beneath it at about forty-three percent of frame height. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 144 degrees, elevation 50 degrees, high on the right behind the camera, lighting the near side of the fuselage, with short shadows falling to the left and away. Early autumn: a clear blue sky with small white fair-weather clouds, the meadow turning yellow-green and the oak still green with the first yellow leaves. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The jack units keep drawing the cables up and raise the airliner the rest of the way, riggers on both beam tops ride with the cables, and the telehandler lifts a pallet of steel pins up to the first beam top; damp clods drop into the empty trough below. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: The empty trough below as a raw scar of damp mud printed with the shape of the belly, clods of mud fallen into it, red primer on the steel with rust-brown streaks at the bolts, spoil heaps by the footings, tyre ruts and tracks across the cut grass. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The airliner rests on the two saddle beams, and each saddle end hangs on one taut lifting cable from a jack unit bolted on a top beam. The frame columns stand bolted on their footings. The telehandler stands on its wheels on the cut grass.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G6 → G7)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The jack units on the red top beams draw the cables on upward and raise the airliner on its saddle beams from half height to its final height, its belly level with the lower branches of the oak.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The rise continues exactly as before, at the same steady pace and in the same straight upward line, the airliner level and rigid; the gap beneath it grows until the far columns and the far footings show clearly under the belly, and the empty muddy trough lies in full view below. The telehandler lifts a pallet of steel pins from the truck up to the riggers on the first beam top. The small white clouds drift slowly from the left in one smooth flow, and the shadow of the airliner on the meadow slides out from under it to the left and away.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 7 — OTURTUR

```
SÜRE: 8,0 s (56,0–64,0)  ·  ELEMAN + ARA HÂL: yük halattan çerçeveye (%100) · halatlar gevşer  ·  REJİM: A (10 dk)  ·  SAAT: 10:40→10:50  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G7)

```
Photorealistic documentary site photograph — Scene 7 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: the airliner has reached its final height: its belly about six metres above the meadow, level with the lower branches of the oak, resting on the two curved saddle beams, which still hang on their slings from four taut steel cables running up to the jack units on the red top beams. Under the raised fuselage the far columns and the far footings now show, and below it lies the empty muddy trough, the exact print of the belly, wet and pitted with fallen clods. The fuselage is clean old white with clouded windows, the tail fin tall at the right, the near wing reaching towards the camera high above the grass. Riggers stand on both beam tops beside a pallet of steel pins; the telehandler waits by the near wingtip.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Twenty to eleven: the airliner hangs at its final height and its weight is about to pass to the frames.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly at about fifty-seven percent of frame height, above the far shoreline, the top of its fuselage at about sixty-six percent and the top of its tail fin at about eighty-two percent, below the top eighth of the frame. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 148 degrees, elevation 51 degrees, high on the right behind the camera, lighting the near side of the fuselage, with short shadows falling to the left and away. Early autumn: a clear blue sky with small white fair-weather clouds, the meadow turning yellow-green and the oak still green with the first yellow leaves. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: Riggers slide steel pins through the saddle beam ends into brackets on the frame columns, the jack units pay out the cables a little so the saddles settle onto the brackets, and the telehandler lifts a pallet of steel brackets up to the second steel frame; the cables go from taut to slack. Mud dries in the trough below. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: The empty trough below as a raw scar of damp mud printed with the shape of the belly, clods of mud fallen into it, red primer on the steel with rust-brown streaks at the bolts, spoil heaps by the footings, tyre ruts and tracks across the cut grass. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The saddle beams rest on steel brackets pinned to the frame columns, and the airliner rests on the saddle beams. The frame columns stand bolted on their footings. Each lifting cable hangs slack from its jack unit, which stays bolted on its top beam.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G7 → G8)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The riggers pin the saddle beam ends to steel brackets on the frame columns, and the jack units pay out the four cables until the weight of the airliner passes from the cables onto the steel frames.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. First the pins go in at the first steel frame and then at the second; then the saddles settle a hand's width onto the brackets, and the four cables slacken one after another and hang in loose curves. The airliner does not move at all. The telehandler lifts a pallet of steel brackets from the truck up to the second steel frame. The small white clouds drift slowly from the left in one smooth flow, and the shadow of the airliner lies on the meadow to the left and away.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 8 — ÇATAR

```
SÜRE: 8,0 s (64,0–72,0)  ·  ELEMAN + ARA HÂL: teras çerçevesi 0 → %100 (dört ayak · kiriş)  ·  REJİM: A (10 dk)  ·  SAAT: 10:50→11:00  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G8)

```
Photorealistic documentary site photograph — Scene 8 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: the airliner now sits fixed at its final height, its belly six metres above the meadow, on two curved steel saddle beams pinned to steel brackets on the two red steel frames; the four lifting cables and their slings hang slack in loose curves from the jack units on the top beams. Below lies the empty muddy trough. The fuselage is clean old white with clouded windows, the tail fin tall at the right, the near wing reaching towards the camera high above the grass. A long truck stands at the right loaded with grey steel beams and slim steel posts, a small piling rig waits beside it, and two work platforms stand under the near wing; a heap of spoil lies by the far footings.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Ten to eleven: the airliner is fixed on its frames and the first steel for the terrace has arrived.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly at about fifty-seven percent of frame height, above the far shoreline, the top of its fuselage at about sixty-six percent and the top of its tail fin at about eighty-two percent, below the top eighth of the frame. The near wing reaches out above the grass towards the lower middle of the frame. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 151 degrees, elevation 52 degrees, high on the right behind the camera, lighting the near side of the fuselage, with short shadows falling to the left and away. Early autumn: a clear blue sky with small white fair-weather clouds, the meadow turning yellow-green and the oak still green with the first yellow leaves. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The telehandler lifts a grey steel beam from the truck and sets it on two slim posts beside the near wing, riggers bolt it to the posts, and the small piling rig drives post footings into the meadow; the steel on the truck dwindles. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: The empty trough below as a raw scar of damp mud printed with the shape of the belly, clods of mud fallen into it, red primer on the steel with rust-brown streaks at the bolts, spoil heaps by the footings, tyre ruts and tracks across the cut grass. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The airliner rests on its saddle beams, which rest on the brackets of the frame columns. The new terrace posts stand on driven footings in the meadow and carry the grey beams, bolted at their heads. The truck stands on its wheels on the gravel track.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G8 → G9)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The telehandler carries grey steel beams and slim posts from the truck to the near wing, and the crew bolts them into a separate terrace frame on its own posts round the wing root, clear of the wing itself.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The piling rig drives four post footings round the near wing root; the posts are stood on them, and the beams are lifted onto their heads and bolted, until a flat grey steel frame surrounds the wing root at the height of the top of the wing, with the wing passing through it unchanged. The airliner does not move. The small white clouds drift slowly from the left in one smooth flow, and the short shadows fall to the left and away.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 9 — DÖŞER

```
SÜRE: 8,0 s (72,0–80,0)  ·  ELEMAN + ARA HÂL: teras döşemesi %0 → %100 (burundan kuyruğa) · istif → 0  ·  REJİM: B (2 sa)  ·  SAAT: 11:00→13:00  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G9)

```
Photorealistic documentary site photograph — Scene 9 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: a grey steel terrace frame now stands round the root of the near wing on four slim posts, its beams level with the top of the wing and the wing passing through it unchanged. The airliner sits fixed at its final height on its two curved steel saddle beams pinned to the red steel frames, its belly six metres above the meadow, the four lifting cables hanging slack from the jack units on the top beams. The fuselage is clean old white with clouded windows. A flatbed truck stands at the right loaded with a high stack of pale timber decking boards; the telehandler waits beside it; two work platforms stand under the frame.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Eleven in the morning: the terrace frame is up and the decking boards are stacked on the truck.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly at about fifty-seven percent of frame height, above the far shoreline, the top of its fuselage at about sixty-six percent and the top of its tail fin at about eighty-two percent, below the top eighth of the frame. The terrace frame sits at about sixty-three percent of frame height, between about two fifths and a little over half the frame width. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 155 degrees, elevation 53 degrees, high on the right behind the camera, lighting the near side of the fuselage, with short shadows falling to the left and away. Early autumn: a clear blue sky with small white fair-weather clouds, the meadow turning yellow-green and the oak still green with the first yellow leaves. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Two hours pass across this shot: the shadows swing slowly round, the clouds streak across the sky, and machines smear into heavy motion blur. Nothing moves at normal speed.

ACTIVITY: The telehandler lifts a pack of decking boards from the truck onto the terrace frame, carpenters lay the boards across the beams from the cockpit side towards the tail, and a second team screws them down; offcuts drop into a skip below. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: The empty trough below as a raw scar of damp mud printed with the shape of the belly, clods of mud fallen into it, red primer on the steel with rust-brown streaks at the bolts, spoil heaps by the footings, tyre ruts and tracks across the cut grass. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The decking boards rest on the grey terrace beams, which bear on four slim posts standing on driven footings. The airliner rests on its saddle beams pinned to the frame columns. The truck stands on its wheels on the gravel track.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G9 → G10)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The telehandler lifts packs of decking boards from the truck onto the terrace frame, and the carpenters lay them across the beams in one direction, from the cockpit side towards the tail, until the whole terrace floor is covered.

Two hours pass. Everything in this shot is time-lapsed at the same rate. Pack after pack rises from the truck on the telehandler forks, and the pale timber floor advances steadily along the frame in one direction, board by board, while the stack on the truck shrinks pack by pack until the truck bed is bare. The shadows swing slowly round under the airliner from the left to the right as the sun passes high behind the camera, and the clouds streak slowly across from the left. The oak turns from green to gold.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 10 — KURAR

```
SÜRE: 8,0 s (80,0–88,0)  ·  ELEMAN + ARA HÂL: merdiven 0 → 2 kol + sahanlık (%100)  ·  REJİM: A (10 dk)  ·  SAAT: 13:00→13:10  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G10)

```
Photorealistic documentary site photograph — Scene 10 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: a pale timber terrace now surrounds the root of the near wing at the height of the wing top, its decking complete on the grey steel frame and four slim posts, the wing passing through it unchanged; the over-wing exit beside it is still shut. The airliner sits fixed at its final height on its two curved steel saddle beams pinned to the red steel frames, its belly six metres above the meadow, the four lifting cables hanging slack from the jack units on the top beams. The cockpit windows and the row of cabin windows are still old and clouded, some broken. A truck stands on the dry rise under the oak, loaded with two sections of grey steel stair with timber steps and a small half-way platform; offcuts lie in a skip below the terrace.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: One in the afternoon: the terrace is floored and the stair has arrived under the oak.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly at about fifty-seven percent of frame height, above the far shoreline, the top of its fuselage at about sixty-six percent and the top of its tail fin at about eighty-two percent, below the top eighth of the frame. The truck with the stair stands under the oak at about a sixth of the frame width. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 205 degrees, elevation 53 degrees, high behind the camera, lighting the near side of the fuselage evenly, with short shadows falling away from the camera. Mid autumn: a soft blue sky with scattered white clouds, the oak gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The telehandler lifts the lower stair section from the truck and sets it on a footing on the dry rise, riggers bolt a small half-way platform onto a slim post, and the telehandler then swings the upper section up to the forward cabin door; fallen leaves and tyre ruts mark the rise. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Pale new timber with sawdust in the joints, grey steel and red primer, fallen oak leaves drifting on the grass, tyre ruts and a muddy gravel track, packing film and offcuts in a skip, the old trough below drying into cracked mud. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The lower stair section stands on a concrete footing on the dry rise and bears on the half-way platform, which stands on one slim post. The upper section hangs from the telehandler forks on a short sling until it is bolted at the door sill. The airliner rests on its saddle beams.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G10 → G11)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The telehandler lifts two steel stair sections and a half-way platform from the truck under the oak, and the riggers bolt them into one stair from the dry rise up to the forward cabin door.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The lower section is set on its footing, the half-way platform is bolted onto its post, and the upper section swings up on the forks and is bolted at the door sill; then the forward cabin door is swung open from inside. The truck drives off along the gravel track, and two workers roll two scaffold towers in under the cabin windows. The scattered white clouds drift slowly from the left in one smooth flow, and the short shadows fall away from the camera.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 11 — CAMLAR

```
SÜRE: 8,0 s (88,0–96,0)  ·  ELEMAN + ARA HÂL: cam: bulanık → yeni (%100, burundan kuyruğa) · kanat üstü kapı açılır  ·  REJİM: A (10 dk)  ·  SAAT: 13:10→13:20  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G11)

```
Photorealistic documentary site photograph — Scene 11 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: a grey steel stair with timber steps now runs from the dry rise under the oak, by way of a small half-way platform on one slim post, up to the forward cabin door, which stands open. The pale timber terrace surrounds the root of the near wing. The airliner sits fixed at its final height on its two curved steel saddle beams pinned to the red steel frames, its belly six metres above the meadow, the four lifting cables hanging slack from the jack units on the top beams. The cockpit windows and the row of cabin windows are still old and clouded, some broken. Two scaffold towers stand on the grass under the cabin windows, and a truck at the right carries crates of new window panes.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Ten past one: the stair reaches the open door and the crates of new panes are waiting.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly at about fifty-seven percent of frame height, above the far shoreline, the top of its fuselage at about sixty-six percent and the top of its tail fin at about eighty-two percent, below the top eighth of the frame. The stair runs down from the door at about a third of the frame width to the foot of the oak. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 209 degrees, elevation 52 degrees, high on the left behind the camera, lighting the near side of the fuselage, with short shadows falling to the right and away. Late autumn: a pale sky with high thin cloud, the oak bronze and thinning. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: Glaziers on the scaffold towers lift the old clouded panes out of the cabin windows and set new clear panes in, the telehandler lifts a crate of panes from the truck up to the cockpit, and a worker opens the over-wing exit onto the terrace; broken glass collects in a skip below. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Pale new timber with sawdust in the joints, grey steel and red primer, fallen oak leaves drifting on the grass, tyre ruts and a muddy gravel track, packing film and offcuts in a skip, the old trough below drying into cracked mud. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The scaffold towers stand on their wheels on the grass beneath the windows. The crate of panes rests on the telehandler forks. The airliner rests on its saddle beams pinned to the frame columns.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G11 → G12)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The glaziers lift the old clouded panes out of the cockpit and the cabin windows and set clear new panes from the crates into the same openings, window by window from the nose towards the tail, and the over-wing exit opens onto the terrace.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The scaffold towers roll along under the windows, and the window row turns from milky white to clear dark glass, one window after another, the nose first; the telehandler lifts the crates from the truck up to the cockpit and lowers the empty ones back. The window openings keep their positions and their shapes. The high thin cloud drifts slowly from the left in one smooth flow, and the short shadows fall to the right and away.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 12 — YALITIR

```
SÜRE: 8,0 s (96,0–104,0)  ·  ELEMAN + ARA HÂL: kabin içi: yalıtım + zemin (palet 4 → 0 · vekil: eksilen yük)  ·  REJİM: A (10 dk)  ·  SAAT: 13:20→13:30  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G12)

```
Photorealistic documentary site photograph — Scene 12 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: every window of the airliner has been renewed: the six cockpit panes and the long row of small cabin windows are clear dark glass, and the over-wing exit stands open onto the pale timber terrace round the near wing root. The grey steel stair with timber steps runs from the dry rise under the oak to the open forward cabin door. The airliner sits fixed at its final height on its two curved steel saddle beams pinned to the red steel frames, its belly six metres above the meadow, the four lifting cables hanging slack from the jack units on the top beams. Two scaffold towers stand under the cabin windows; a flatbed truck parked at the foot of the stair carries four tall pallets of insulation rolls and pale floor panels.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Twenty past one: all the windows are new and four pallets for the cabin wait at the foot of the stair.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly at about fifty-seven percent of frame height, above the far shoreline, the top of its fuselage at about sixty-six percent and the top of its tail fin at about eighty-two percent, below the top eighth of the frame. The truck with the four pallets stands at the foot of the stair at about a sixth of the frame width. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 212 degrees, elevation 51 degrees, high on the left behind the camera, lighting the near side of the fuselage, with short shadows falling to the right and away. Late autumn: a pale sky with high thin cloud, the oak bronze and thinning. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: Workers carry insulation rolls on their shoulders from the truck up the stair and in through the forward door, and the telehandler lifts a pallet of pale floor panels from the truck onto the terrace, where a second team carries the panels in through the over-wing exit; packing film and offcuts collect in a skip. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Pale new timber with sawdust in the joints, grey steel and red primer, fallen oak leaves drifting on the grass, tyre ruts and a muddy gravel track, packing film and offcuts in a skip, the old trough below drying into cracked mud. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The truck stands on its wheels at the foot of the stair, and the pallet of floor panels rests on the telehandler forks. The stair stands on its footing on the dry rise. The airliner rests on its saddle beams pinned to the frame columns.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G12 → G14)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: Workers carry insulation rolls and floor panels from the pallets on the truck at the foot of the stair up into the cabin through the forward door and the over-wing exit, until the truck bed is bare.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. A steady line of soft streaks flows up the stair with rolls on their shoulders and down again empty-handed, while the telehandler lifts pallet after pallet of panels from the truck onto the terrace; the four pallets on the truck shrink to bare boards and the empty truck drives off along the gravel track. The high thin cloud drifts slowly from the left in one smooth flow, and the short shadows fall to the right and away.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 13 — DONATIR

```
SÜRE: 8,0 s (104,0–112,0)  ·  ELEMAN + ARA HÂL: kokpit köşesi: boş → iki koltuk · masa · lamba · kilim (%100)  ·  REJİM: A (10 dk)  ·  SAAT: 13:20→13:30  ·  İSTASYON: KOKPİT (detay · 2/2 kuralı)
```

> 🪟 **KOKPİT EKİ** — ana zincirin DIŞINDA: S12 ile AYNI on dakikanın içeriden görüntüsü. S12'nin I2V'si ana kare G14'e biter · bu klip G13 → G13′ (kokpit) · S14 yine G14'ten başlar. Dış kare iki yakada AYNIDIR (detay klibi dış büyüme taşımaz — KAMERA_ISTASYONU §1 ④).

### 📸 GÖRSEL PROMPT (G13 · KOKPİT İLK KARE)

```
Photorealistic documentary interior photograph — Scene 13 of 30. Horizontal 16:9 time-lapse inside the cockpit of a retired jet airliner beside a lake being made into a lake house; a progress photograph from a fixed 24 mm camera inside the cockpit.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: COCKPIT STATION — fixed clamp mount bolted to the rear wall of the cockpit, lens 8.2 metres above the meadow, 2.4 metres from the windscreen, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: the cockpit has been stripped and lined: the old instrument panel has been taken out and the front is lined flat with pale birch boards below the windscreen, the walls and the curved ceiling are lined with smooth white panels, a new floor of pale oak boards runs forward to the base of the windscreen, and the six windscreen panes are new and clear. The space is empty except for a rolled rug and a roll of insulation membrane left by the rear wall, and a low step down to the cabin door at the rear. Through the panes: the oak, bronze in late autumn, on the left; ahead and to the right the meadow below, the lake and the far wooded hills.

SITE / BACKGROUND: The cockpit of the raised airliner, seen from its rear wall looking forward over the nose through six windscreen panes in their curved frames, with a curved white ceiling and white side walls each holding one small side window. Through the left panes rises the crown of the one big old oak on its slight dry rise; ahead and to the right, beyond the meadow below, the lake runs out to the far shore, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height.

THE TIME MOMENT: Twenty past one in the afternoon: the cockpit is bare and lined, waiting for its furniture.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The six windscreen panes span about 1500 pixels of frame width — about four fifths — across the upper middle of the frame and keep that width and position in every frame; the floor and the furniture fill the lower third. Nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 212 degrees, elevation 51 degrees, high on the left, so a bright patch of sunlight falls through the left panes onto the new floor while the rest of the cockpit is in soft daylight. Late autumn outside: a pale sky with high thin cloud and the oak bronze. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds and the light outside, the rain and the water, and any crew inside all move at the same accelerated speed. Ten minutes pass across this shot: the light shifts only a little, the clouds drift in one smooth flow, and the crew trail light motion blur. Nothing moves at normal speed.

ACTIVITY: Two workers carry an armchair in from the cabin and set it by the left panes, a third carries a second armchair and a small round table, a hand cart brings a standing lamp, and a worker unrolls the rug across the floor; the patch of sunlight creeps across the boards. Crew register only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Fresh pale oak floor boards with sawdust in the joints, smooth white wall panels with taped seams and a few glue stains, a faint film of dust on the new panes, packing film and offcuts by the rear wall, a band of sunlight on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The rolled rug and the membrane roll rest on the new floor boards by the rear wall. The floor rests on the cockpit floor beams of the airliner. The wall panels are clamped to the curved frames of the fuselage, and the birch boards are bolted over the old panel frame.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The windscreen frames, the curved ceiling, the oak crown through the left panes, the far wooded hills and the far shoreline never change shape, position, size or spacing. The cockpit keeps the shape of its six windscreen panes and its curved white walls; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the walls and the furniture included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G13 → G13′)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: Workers carry two armchairs, a small round table, a standing lamp and a rug from the cabin into the cockpit and set them in front of the windscreen, turning the bare cockpit into a reading corner that looks out over the lake.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. A hand cart brings the lamp and the rolled rug from the cabin; the rug is unrolled, the two chairs are set facing the windscreen with the table between them, and the lamp is stood beside the right chair. At the end the lamp is switched on and glows warm. Outside, the high thin cloud drifts slowly from the left over the lake and the far hills, and the patch of sunlight slides slowly across the floor.

This shot shows the same stage as the previous shot from the main station: the house stands at the same height, its belly about fifty-seven percent of frame height in that view, and nothing outside the cockpit is built during this shot. The camera does not move at any point. The framing is identical in the first and last frame. The windscreen frames, the curved ceiling, the oak crown through the left panes, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the windscreen occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. Nothing already built is removed or resized.

Camera: fixed clamp mount, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🪟 KOKPİT SON KARESİ (G13′ · bu klibin hedefi — sahne görseli DEĞİL, kapı saymaz)

> Kapı bu bloğu saymaz (başlıkta GÖRSEL PROMPT yok) — ama aynı disiplinle yazıldı: STRUCTURE,
> SITE / BACKGROUND, NEGATIVE kokpit karelerinde birebir. Üretimde G13′ ÖNCE üretilir (ana
> G14'ün mevsimi ve ışığıyla), G13 ondan geriye; G21 G13′'den türetilir, G21′ G21'den.

```
Photorealistic documentary interior photograph — the last frame of Scene 13 of 30. Horizontal 16:9 time-lapse inside the cockpit of a retired jet airliner beside a lake being made into a lake house; a progress photograph from a fixed 24 mm camera inside the cockpit.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: COCKPIT STATION — fixed clamp mount bolted to the rear wall of the cockpit, lens 8.2 metres above the meadow, 2.4 metres from the windscreen, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: the cockpit is now a small reading corner: two soft grey armchairs face the windscreen with a small round oak table between them on a woven rug, and a standing lamp beside the right chair glows warm; the white lined walls, the curved ceiling, the pale oak floor, the pale birch boards below the windscreen, the low step down to the cabin door and the six clear windscreen panes are as before. Folded packing film lies by the rear wall. Through the panes: the bronze oak on the left; ahead and to the right the meadow below, the lake and the far wooded hills.

SITE / BACKGROUND: The cockpit of the raised airliner, seen from its rear wall looking forward over the nose through six windscreen panes in their curved frames, with a curved white ceiling and white side walls each holding one small side window. Through the left panes rises the crown of the one big old oak on its slight dry rise; ahead and to the right, beyond the meadow below, the lake runs out to the far shore, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height.

THE TIME MOMENT: Half past one in the afternoon: the reading corner is furnished and its lamp is on.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The six windscreen panes span about 1500 pixels of frame width — about four fifths — across the upper middle of the frame and keep that width and position in every frame; the floor and the furniture fill the lower third. Nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 216 degrees, elevation 50 degrees, high on the left, so a bright patch of sunlight lies across the rug from the left panes; the lamp adds a small warm glow by the right chair. Late autumn outside: a pale sky with high thin cloud and the oak bronze. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds and the light outside, the rain and the water, and any crew inside all move at the same accelerated speed. Ten minutes pass across this shot: the light shifts only a little, the clouds drift in one smooth flow, and the crew trail light motion blur. Nothing moves at normal speed.

ACTIVITY: The work is finished: the last worker leaves down the low step towards the cabin as faint soft motion streaks, and the patch of sunlight lies still on the rug.

SITE TEXTURE: Fresh pale oak floor boards with sawdust in the joints, smooth white wall panels with taped seams and a few glue stains, a faint film of dust on the new panes, folded packing film by the rear wall, a band of sunlight across the rug. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The two armchairs and the table stand on the rug, which lies on the new floor boards. The lamp stands on its heavy round foot beside the right chair. The wall panels are clamped to the curved frames of the fuselage.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The windscreen frames, the curved ceiling, the oak crown through the left panes, the far wooded hills and the far shoreline never change shape, position, size or spacing. The cockpit keeps the shape of its six windscreen panes and its curved white walls; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the walls and the furniture included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

---

## 🎬 SAHNE 14 — YERLEŞTİRİR

```
SÜRE: 8,0 s (112,0–120,0)  ·  ELEMAN + ARA HÂL: mutfak: tezgâh + dolaplar (sandık 3 → 0 · kanat kapısından)  ·  REJİM: A (10 dk)  ·  SAAT: 13:30→13:40  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G14)

```
Photorealistic documentary site photograph — Scene 14 of 30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: the cabin has been lined inside, and the truck at the foot of the stair has gone. The grey steel stair with timber steps runs from the dry rise under the oak to the open forward cabin door; the pale timber terrace surrounds the near wing root, the over-wing exit open onto it. The airliner sits fixed at its final height on its two curved steel saddle beams pinned to the red steel frames, its belly six metres above the meadow, the four lifting cables hanging slack from the jack units on the top beams. Two scaffold towers stand under the cabin windows. A second flatbed truck stands at the right beside the telehandler, loaded with a long wrapped kitchen counter and three wrapped crates of cabinets.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Half past one: the cabin is lined, and the kitchen waits on the truck beside the telehandler.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly at about fifty-seven percent of frame height, above the far shoreline, the top of its fuselage at about sixty-six percent and the top of its tail fin at about eighty-two percent, below the top eighth of the frame. The truck with the three crates stands at the right at about four fifths of the frame width. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 216 degrees, elevation 50 degrees, high on the left behind the camera, lighting the near side of the fuselage, with short shadows falling to the right and away. Late autumn: a pale sky with high thin cloud, the oak bronze and thinning. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The telehandler lifts a crate of wrapped cabinets from the truck up onto the terrace, a team slides the cabinets off the crate and in through the over-wing exit on a low trolley, and the telehandler then lifts the long kitchen counter up to the terrace in the same way; packing film flaps in the skip. Crew register only as faint soft motion streaks beside their machines, never as sharp figures.

SITE TEXTURE: Pale new timber with sawdust in the joints, grey steel and red primer, fallen oak leaves drifting on the grass, tyre ruts and a muddy gravel track, packing film and offcuts in a skip, the old trough below drying into cracked mud. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The truck stands on its wheels at the right, and each crate rests on the telehandler forks as it rises. The terrace bears on its four slim posts. The airliner rests on its saddle beams pinned to the frame columns.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G14 → G15)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The telehandler lifts the three crates of cabinets and the long kitchen counter from the truck onto the terrace, and the team slides them on a low trolley from the terrace in through the over-wing exit into the middle of the cabin.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The forks rise from the truck to the terrace and come down empty again, crate by crate, and each time soft streaks of the team slide the load across the terrace and in through the over-wing exit; last of all the long counter goes up and in. The three crates on the truck go down to none. The high thin cloud drifts slowly from the left in one smooth flow, and the short shadows fall to the right and away.

The camera does not move at any point. The framing is identical in the first and last frame. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
