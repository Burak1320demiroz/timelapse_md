# 🎬 THE_LAST_CARRIAGE — BÖLÜM 1  (S0 – S9 · G0 … G9 + 10 I2V · 0,0–80,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `THE_LAST_CARRIAGE_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır. STRUCTURE, SITE / BACKGROUND ve NEGATIVE blokları bütün ana karelerde BİREBİR aynı
> kelimelerle tekrarlanır; değişen AT THIS STAGE, THE TIME MOMENT, COMPOSITION'ın son cümleleri, LIGHTING,
> TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.
>
> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py`)
> ki ortak bloklar harfi harfine aynı kalsın [DERS 20].
>
> ⭐ Bu bölümün SON I2V'si (S9: G9 → G10) **G10 karesinde biter** ve G10 `BOLUM_2`'nin ilk görselidir:
> bölüm sınırı bir KAREDİR, kesme değil [DERS 52]. Kapı KLASÖR MODUNDA koşulur:
> `python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_LAST_CARRIAGE`.
>
> ⛔ Vinç kancası [DERS 8 · 57]: vinç (G0–G15) her karede ya YÜKLÜ ("with a … on the hook on taut slings") ya da bom
> ucu KADRAJ DIŞINDA ("its tip and line above the top edge of the frame"); boş kanca hiçbir promptta yazılmaz.
> Her vinçli klipte yük ilk karede hedefin HEMEN ÜSTÜNDE asılı başlar.
>
> ⛔ Kelime kilitleri: "rust" yalnız G0–G3 ve S0–S3'te; "emerald" S4 I2V'sinden, "copper" S4 sonundan (palet) ve
> G5'ten; "gangway" G7'den; "terrace frame" G8 sonundan; "glass floor" S10 sonundan; ışıkların yanması yalnız S16
> I2V'sinden sonra; "guests" yalnız S17 I2V'sinden sonra. YASAK KELİME (PLAN künyesi) hiçbir promptta yok — negatifte bile.

---

## 🎬 SAHNE 0 — İNDİRİR

```
SÜRE: 8,0 s (0,0–8,0)  ·  ELEMAN + ARA HÂL: ⭐ vagon tabliyenin 1 m üstünden tabliyeye (DERS 57: kaldırma karede biter, klip yalnız son metreyi gösterir) · sapanlar bağlı kalır  ·  REJİM: A (10 dk)  ·  SAAT: 09:30→09:40  ·  İSTASYON: MAIN
```

> 🏗️ **Kaldırma** [DERS 57 · DERS 8]: vagon G0'da tabliyenin 1 m üstünde, kısa ve gergin sapanlarda ASILI başlar;
> klip yalnız son metreyi ve oturmayı gösterir. Yerden kalkış YOK. Oturduktan sonra vagon bir daha kalkmaz,
> sallanmaz, kaymaz (LOCK cümlesi S1'den itibaren). Sapanlar S1'de çözülür.

### 📸 GÖRSEL PROMPT (G0)

```
Photorealistic documentary site photograph — Scene 0 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the old carriage already hangs over the canyon: one old railway passenger carriage, weathered rust-brown from end to end with patches of faded old paint, its rounded roof rust-brown and dented, one closed vestibule at each end, its eight broad window openings along the near side filled with broken and clouded old panes, hangs level about one metre above the steel support deck on four short taut slings from a lifting spreader bar. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, with a lifting spreader bar on the hook on taut slings, the boom head directly above the carriage. Crews stand on both ledges and on the deck walkways holding taglines tied to the two ends of the carriage, and a flatbed truck stands on the gravel yard.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Half past nine on a clear autumn morning: the old carriage already hangs over the canyon, a metre above its steel deck.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. In this frame the carriage still hangs one metre higher, its underframe about 40 pixels above that line, the gap between it and the steel deck clearly open. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 139 degrees, elevation 25 degrees, behind the camera on the right: clear morning light on the near long side of the carriage, shadows falling forward to the left, the canyon below in shade. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane lowers the carriage the last metre onto the steel deck, the crews on both ledges steady its ends with taglines, a second crew bolts its underframe to the deck, and a flatbed truck brings crates of anchor bolts along the service road; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Flaking rust streaks and blistered old paint on the carriage, orange rust stains on the steel deck, tyre ruts and puddles in the gravel yard, stacks of empty crates, a film of dust on the old panes. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The carriage hangs from the spreader bar on four taut slings, and the spreader bar hangs from the crane hook. The crane stands on its outriggers on pads on the gravel, the steel deck bears on steel pads on both ledges, and the truck stands on its tyres on the gravel yard.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G0 → G1)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The mobile crane lowers the carriage from its hanging position one metre above the deck onto the steel support deck, and the crew bolts its underframe down.

Ten minutes pass in the clear morning light. Everything in this shot is time-lapsed at the same rate. From the first frame the carriage is already sinking slowly and level, never swinging, as the crane pays out its line: the crews on both ledges hold it steady with taglines, its ends pass over the steel pads on the two ledges, and it settles flat onto the steel deck across the canyon. A crew moves along the walkways and bolts the underframe to the deck; the slings stay fastened and go slack only after the bolts are in. A flatbed truck brings crates of anchor bolts along the service road and the crew carries them to the deck. Thin high clouds drift slowly from the right, and long shadows fall forward to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 1 — ÇÖZER

```
SÜRE: 8,0 s (8,0–16,0)  ·  ELEMAN + ARA HÂL: sapanlar vagondan çözülür · çapraz kiriş vinçle sola, avluya iner · bom dik kalkar · avluya boş kasalar  ·  REJİM: A (10 dk)  ·  SAAT: 09:40→09:50  ·  İSTASYON: MAIN
```

> 🏗️ **Kaldırma** [DERS 57 · DERS 8]: vagon G0'da tabliyenin 1 m üstünde, kısa ve gergin sapanlarda ASILI başlar;
> klip yalnız son metreyi ve oturmayı gösterir. Yerden kalkış YOK. Oturduktan sonra vagon bir daha kalkmaz,
> sallanmaz, kaymaz (LOCK cümlesi S1'den itibaren). Sapanlar S1'de çözülür.

### 📸 GÖRSEL PROMPT (G1)

```
Photorealistic documentary site photograph — Scene 1 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits on the steel support deck, its steel underframe bolted flat to the deck, weathered rust-brown from end to end with patches of faded old paint, its rounded roof rust-brown and dented, one closed vestibule at each end, its eight broad window openings along the near side filled with broken and clouded old panes. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, with a lifting spreader bar on the hook on taut slings, its four slings still fastened to the corners of the carriage roof. Riggers stand on the carriage roof at the sling shackles, and a flatbed truck stacked with empty timber crates stands on the gravel yard beside a small yellow telehandler.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Twenty to ten in the morning: the carriage has landed on its deck, and the slings are about to come off.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 141 degrees, elevation 26 degrees, behind the camera on the right: clear morning light on the near long side of the carriage, shadows falling forward to the left, the canyon below in shade. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: Riggers on the carriage roof unshackle the four slings, the mobile crane lifts the spreader bar off the roof and swings it to the gravel yard, the telehandler unloads the empty crates from the flatbed truck into a stack, and a crew lays timber walk boards along the deck walkways; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Flaking rust streaks and blistered old paint on the carriage, orange rust stains on the steel deck, tyre ruts and puddles in the gravel yard, stacks of empty crates, a film of dust on the old panes. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The spreader bar hangs from the crane hook on its taut slings. The carriage rests on the steel deck, its underframe bolted down; the crane stands on its outriggers on the gravel, and the telehandler stands on its tyres on the yard.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G1 → G2)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The riggers unshackle the four slings from the carriage roof, and the mobile crane lifts the spreader bar from above the carriage to the gravel yard on the left ledge.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the riggers are already at the shackles: the slings come free one corner after another, the crane lifts the spreader bar a few metres clear of the roof, swings it slowly to the left over the ledge and sets it down on the gravel yard, where the crew unhooks it; then the crane raises its boom steeply until its tip and line rise above the top edge of the frame. The carriage stays exactly where it landed. The telehandler unloads the empty crates from the flatbed truck into a stack on the yard and the truck drives off, and a crew carries timber walk boards along the deck walkways. Small clouds drift slowly from the right, and the shadows fall forward to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized. Once seated on the deck, the carriage never lifts, swings or shifts again.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 2 — SÖKER

```
SÜRE: 8,0 s (16,0–24,0)  ·  ELEMAN + ARA HÂL: sekiz kırık pencere paneli soldan sağa → avludaki kasalara (sayım 8 → 0) · eski koltuk iskeletleri sol vestibülden atık konteynerine  ·  REJİM: A (10 dk)  ·  SAAT: 09:50→10:00  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G2)

```
Photorealistic documentary site photograph — Scene 2 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits on the steel support deck, its steel underframe bolted flat to the deck, weathered rust-brown from end to end with patches of faded old paint, its rounded roof rust-brown and dented, one closed vestibule at each end, its eight broad window openings along the near side filled with broken and clouded old panes. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, its boom raised steeply, its tip and line above the top edge of the frame; the spreader bar lies on the gravel yard, its slings coiled beside it. A stack of empty timber crates and a steel skip stand on the yard beside the small yellow telehandler, and glaziers with suction lifters wait on the near walkway under the first window.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Ten to ten in the morning: the carriage is down and free, and the old windows come out first.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 143 degrees, elevation 27 degrees, behind the camera on the right: clear morning light on the near long side of the carriage, shadows falling forward to the left, the canyon below in shade. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: Glaziers lift the broken old panes out of the window openings with suction lifters and carry them along the walkway into the crates on the yard, a second crew carries old seat frames out through the left vestibule into the skip, and the telehandler lifts each filled crate onto a flatbed truck. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Flaking rust streaks and blistered old paint on the carriage, orange rust stains on the steel deck, tyre ruts and puddles in the gravel yard, stacks of empty crates, a film of dust on the old panes. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The crates stand on the gravel yard, the skip rests on its skids on the gravel, and the telehandler stands on its tyres. The carriage rests on the steel deck, its underframe bolted down.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G2 → G3)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The glaziers lift the eight broken old panes out of the window openings, from left to right, and carry them along the walkway into the crates on the gravel yard.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the glaziers are already at the first window: one opening after another along the near side, from left to right, the broken clouded panes come out and the dark empty openings remain, until all eight stand empty and the dim stripped saloon shows through them; the openings keep their size and spacing. A second crew carries old seat frames out through the left vestibule and tips them into the skip, and the telehandler lifts the filled crates onto a flatbed truck, which drives off up the service road. At the end a truck tows a compressor trailer and a grit hopper onto the yard. Small clouds drift slowly, and the shadows fall forward to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized. Once seated on the deck, the carriage never lifts, swings or shifts again.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 3 — SIYIRIR

```
SÜRE: 8,0 s (24,0–32,0)  ·  ELEMAN + ARA HÂL: pas → çıplak gri çelik, soldan sağa (%0 → %100) · tavan dâhil · kum ve pas pulu brandada  ·  REJİM: B (2 sa)  ·  SAAT: 10:00→12:00  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G3)

```
Photorealistic documentary site photograph — Scene 3 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits on the steel support deck, its steel underframe bolted flat to the deck, weathered rust-brown from end to end with patches of faded old paint, its rounded roof rust-brown and dented, one closed vestibule at each end; its eight broad window openings along the near side stand empty, the dim stripped saloon showing through them. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, its boom raised steeply, its tip and line above the top edge of the frame. A compressor trailer and a grit hopper stand on the gravel yard with blast hoses running along the near walkway, tarpaulins are spread along both walkways, and blasting crews in hoods stand at the left end of the carriage, a step ladder at each vestibule, and on the roof on harness lines.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Ten in the morning: the windows are out, and the blasting crews line up at the left end.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 146 degrees, elevation 28 degrees, behind the camera on the right: clear morning light on the near long side of the carriage, shadows falling forward to the left, the canyon below in shade. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Two hours pass across this shot: shadows swing slowly round, clouds streak across the sky, machines smear into heavy motion blur.

ACTIVITY: Blasting crews spray the carriage body with grit from the walkways and from the roof, working from the left end to the right, a crew with grinders follows them over the seams, a second crew shovels the spent grit and rust flakes from the tarpaulins into bags, and the compressor and the hopper feed the hoses. Dozens of workers in orange work clothes show only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Bands of bare grey steel beside flaking rust-brown, drifts of spent grit and rust flakes on tarpaulins along the walkway, a film of dust on the deck, tyre ruts in the gravel yard, stacks of filled grit bags. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The compressor trailer and the hopper stand on their tyres on the gravel yard, the hoses rest on the walkway, and the roof crews are clipped to harness lines anchored to the deck handrails. The carriage rests on the steel deck, bolted down.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G3 → G4)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The blasting crews strip the rust and old paint from the carriage body and roof, from the left end to the right, and shovel the spent grit from the tarpaulins into bags.

Two hours pass. Everything in this shot is time-lapsed at the same rate. Band by band from the left end the rust-brown skin turns a clean dull grey, the bare steel spreading steadily along the body and over the rounded roof until the whole carriage is bare grey steel from end to end; its shape, its eight empty openings and its two vestibules stay exactly as they were. The spent grit gathers on the tarpaulins, and the crews shovel it into bags and stack them on a pallet on the yard. At the end the compressor trailer is towed off and a paint trailer with spray rigs and pallets of paint drums arrives. The shadows swing slowly round behind the camera as the sun climbs, and clouds streak across the sky.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized. Once seated on the deck, the carriage never lifts, swings or shifts again.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 4 — BOYAR

```
SÜRE: 8,0 s (32,0–40,0)  ·  ELEMAN + ARA HÂL: astar griden koyu zümrüt gövdeye + krem şerit, soldan sağa (%0 → %100) · tavan çıplak kalır  ·  REJİM: B (2 sa)  ·  SAAT: 12:00→14:00  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G4)

```
Photorealistic documentary site photograph — Scene 4 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits on the steel support deck, its steel underframe bolted flat to the deck; the carriage body is bare dull grey steel from end to end, scoured clean, its rounded roof bare grey steel, one vestibule at each end; its eight broad window openings along the near side stand empty, the dim stripped saloon showing through them. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, its boom raised steeply, its tip and line above the top edge of the frame. A paint trailer with spray rigs stands on the gravel yard beside pallets of paint drums and a stack of filled grit bags, tarpaulins are spread along both walkways, and spray crews in white overalls wait at the left end of the carriage.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Noon: the carriage is bare grey steel, and the painters are waiting at the left end.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 180 degrees, elevation 34 degrees, high behind the camera: bright light on the near long side of the carriage, short shadows falling away from the camera, the upper canyon walls lit. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Two hours pass across this shot: shadows swing slowly round, clouds streak across the sky, machines smear into heavy motion blur.

ACTIVITY: Spray crews on the walkways spray a pale primer coat along the bare carriage from the left end to the right and follow it with the body coat, a second crew masks the tops of the window openings for a band, and a crew carries paint drums from the pallets on the yard to the spray rigs. Dozens of workers in orange work clothes show only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Bare dull grey steel with dark seams and a few pale primer patches, drifts of spent grit on the tarpaulins, filled grit bags stacked on a pallet, tyre ruts in the gravel yard, a film of dust on the deck. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The paint trailer stands on its tyres on the gravel yard, the drums rest on pallets, and the spray crews stand on the walkway beside the handrails. The carriage rests on the steel deck, bolted down.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G4 → G5)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The spray crews paint the carriage body deep emerald green with a cream band along the tops of the windows, from the left end to the right, from the drums carried from the pallets on the yard.

Two hours pass. Everything in this shot is time-lapsed at the same rate. A pale primer coat sweeps along the bare steel from the left, and close behind it the deep emerald green follows, band by band, until the whole body is emerald from end to end; then a crisp cream band runs along the tops of the eight empty openings. The rounded roof stays bare grey steel. The crews carry drum after drum from the pallets, and the stacks of drums shrink. At the end a flatbed truck loaded with pallets of curved copper-coloured roof sheets arrives on the yard, and the crane lowers its boom and lifts a pallet. The shadows swing slowly from behind the camera to the left side as the sun passes, and clouds streak across the sky.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized. Once seated on the deck, the carriage never lifts, swings or shifts again.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 5 — KAPLAR

```
SÜRE: 8,0 s (40,0–48,0)  ·  ELEMAN + ARA HÂL: bakır renkli çatı levhaları kavisli tavana, soldan sağa (%0 → %100) · siluet aynı  ·  REJİM: A (10 dk)  ·  SAAT: 14:00→14:10  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G5)

```
Photorealistic documentary site photograph — Scene 5 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits on the steel support deck, its steel underframe bolted flat to the deck; the carriage body is painted a deep emerald green from end to end with a cream band along the tops of the windows, one vestibule at each end; its rounded roof is still bare grey steel; its eight broad window openings along the near side stand empty, the dim stripped saloon showing through them. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, with a pallet of copper-coloured roof sheets on the hook on taut slings, the pallet hanging just above the middle of the roof. A flatbed truck stands on the gravel yard, and roofers on harness lines wait on the roof.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Two in the afternoon: the body is emerald green, and the copper for the roof is coming down onto it.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 214 degrees, elevation 28 degrees, behind the camera on the left: warm afternoon light on the near long side, shadows falling forward to the right, the canyon below in soft shade. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane lowers the pallet of copper-coloured roof sheets onto a timber cradle on the middle of the roof, roofers carry the curved sheets along the roof and fix them to the old roof from the left end to the right, and a crew carries offcuts down to the skip; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Fresh satin emerald paint with a soft sheen, copper-coloured roof sheets with bright cut edges, pallets and offcuts stacked on the gravel yard, tyre ruts in the gravel, a film of dust on the steel deck. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The pallet hangs from the crane hook on four taut slings. The roofers are clipped to harness lines anchored to the deck handrails, the new sheets are screwed down onto the old rounded roof, the pallet will rest on a timber cradle bolted to the roof, and the carriage rests on the steel deck, bolted down.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G5 → G6)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The roofers carry the curved copper-coloured sheets from the pallet the crane sets on the roof and fix them onto the old rounded roof, from the left end to the right.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the pallet is already settling onto its cradle on the roof: sheet by sheet from the left a warm copper-coloured skin spreads over the bare grey curve, following its exact line, until the whole roof is copper from end to end; the carriage keeps its height, its length and its silhouette. The pallet on the roof shrinks to bare boards and the crew lowers it to the yard. At the end the crane lifts a steel stillage of large window panes from a flatbed truck. A few clouds drift slowly from the left, and the shadows fall forward to the right.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized. Once seated on the deck, the carriage never lifts, swings or shifts again.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 6 — CAMLAR

```
SÜRE: 8,0 s (48,0–56,0)  ·  ELEMAN + ARA HÂL: sekiz geniş temiz cam mevcut açıklıklara, soldan sağa (sehpa 8 → 0) · direkler korunur  ·  REJİM: A (10 dk)  ·  SAAT: 14:10→14:20  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G6)

```
Photorealistic documentary site photograph — Scene 6 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits on the steel support deck, its steel underframe bolted flat to the deck; the carriage body is painted a deep emerald green from end to end with a cream band along the tops of the windows, one vestibule at each end, its rounded roof clad in warm copper-coloured sheets; its eight broad window openings along the near side stand empty, the dim stripped saloon showing through them. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, with a stillage of window panes on the hook on taut slings, the stillage hanging just above the near walkway at the left end of the carriage. Glaziers with suction lifters wait on the walkway.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Ten past two in the afternoon: the roof is copper, and the new windows hang beside the empty openings.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 217 degrees, elevation 27 degrees, behind the camera on the left: warm afternoon light on the near long side, shadows falling forward to the right, the canyon below in soft shade. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane sets the stillage of window panes down on the near walkway, glaziers lift the large panes off it with suction lifters and set them into the empty openings from left to right, a second crew seals each pane in its frame from inside, and a crew carries the empty stillage frame to the yard; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Fresh satin emerald paint with a soft sheen, copper-coloured roof sheets with bright cut edges, pallets and offcuts stacked on the gravel yard, tyre ruts in the gravel, a film of dust on the steel deck. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The stillage hangs from the crane hook on two taut slings. Each pane is clamped into its opening between the steel window posts, the glaziers stand on the walkway, and the carriage rests on the steel deck.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G6 → G7)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The glaziers carry the large panes from the stillage on the walkway with suction lifters and set them into the eight existing window openings, from left to right.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the stillage is already settling onto the walkway: one after another, from left to right, a large clear pane goes into each empty opening and catches the sky, until all eight broad windows are glazed; the window posts, the openings and the length of the carriage stay exactly the same. The panes on the stillage go down to none. At the end a flatbed truck brings a short steel gangway onto the yard and the crane lifts it. A few clouds drift slowly from the left, and the shadows fall forward to the right.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized. Once seated on the deck, the carriage never lifts, swings or shifts again.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 7 — BAĞLAR

```
SÜRE: 8,0 s (56,0–64,0)  ·  ELEMAN + ARA HÂL: sol yaya bağlantısı: kısa çelik geçit avlu → sol vestibül (%100) · iki sönük lamba direği  ·  REJİM: A (10 dk)  ·  SAAT: 14:20→14:30  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G7)

```
Photorealistic documentary site photograph — Scene 7 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits bolted on the steel support deck, deep emerald green with a cream band along the window tops, its rounded roof clad in warm copper-coloured sheets, eight broad clear windows along its near side. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, with a short steel gangway on the hook on taut slings, the gangway hanging just above the gap between the rim of the gravel yard and the left vestibule. Fitters with taglines wait on the yard rim and in the open left vestibule door, and a flatbed truck with bags of gravel stands on the yard.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Twenty past two in the afternoon: the carriage is finished outside, and its first way in is about to land.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 219 degrees, elevation 26 degrees, behind the camera on the left: warm afternoon light on the near long side, shadows falling forward to the right, the canyon below in soft shade. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane lowers the short steel gangway onto its bearings between the yard rim and the left vestibule, fitters guide it with taglines and bolt both ends, welders fix its handrails, a crew carries bags of gravel from the truck and spreads a path to it, and an electrician sets a small unlit lamp post at each end; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Fresh satin emerald paint with a soft sheen, copper-coloured roof sheets with bright cut edges, pallets and offcuts stacked on the gravel yard, tyre ruts in the gravel, a film of dust on the steel deck. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The gangway hangs from the crane hook on four taut slings. Its far end bears on a steel bracket at the left vestibule, its near end on a concrete pad on the yard rim; the lamp posts are anchored in the pads, and the carriage rests on the steel deck, bolted down.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G7 → G8)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The mobile crane lowers the short steel gangway from just above the gap onto its bearings between the yard rim and the left vestibule, and the fitters bolt it down.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the gangway is already sinking the last metre: it lands level across the short gap, the fitters bolt both ends, and welders run its handrails, until a short dark gangway links the gravel yard to the open left vestibule door; the gap below it stays open to the canyon. A crew carries bags of gravel from the truck and rakes a path to the gangway, and an electrician sets a small unlit lamp post at each end. At the end the crane lifts a second short gangway from a truck. A few clouds drift slowly from the left, and the shadows fall forward to the right.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized. Once seated on the deck, the carriage never lifts, swings or shifts again.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 8 — BAĞLAR

```
SÜRE: 8,0 s (64,0–72,0)  ·  ELEMAN + ARA HÂL: sağ servis bağlantısı: geçit + birkaç basamak sağ vestibül → sağ raf patikası (%100) · iki sönük lamba  ·  REJİM: A (10 dk)  ·  SAAT: 14:30→14:40  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G8)

```
Photorealistic documentary site photograph — Scene 8 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits bolted on the steel support deck, deep emerald green with a cream band along the window tops, its rounded roof clad in warm copper-coloured sheets, eight broad clear windows along its near side; a short dark steel gangway with handrails links the left vestibule to the gravel yard on the left ledge, a small unlit lamp post at each end. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, with a second short steel gangway on the hook on taut slings, the gangway hanging just above the gap between the right vestibule and the right ledge. Fitters wait on the right ledge beside a stack of stone steps and bags of mortar.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Half past two in the afternoon: the main way in is done, and the service way out is landing at the right.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 221 degrees, elevation 25 degrees, behind the camera on the left: warm afternoon light on the near long side, shadows falling forward to the right, the canyon below in soft shade. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane lowers the second short gangway onto its bearings between the right vestibule and the right ledge, fitters bolt it and fix its handrails, masons set a few stone steps from the stack down to a footpath on the right ledge, and an electrician sets a small unlit lamp post at each end; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Fresh satin emerald paint with a soft sheen, copper-coloured roof sheets with bright cut edges, pallets and offcuts stacked on the gravel yard, tyre ruts in the gravel, a film of dust on the steel deck. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The gangway hangs from the crane hook on four taut slings. Its near end bears on a steel bracket at the right vestibule, its far end on a concrete pad on the right ledge, the stone steps are bedded in mortar and rest on the rock, and the crane stands on its outriggers on the gravel.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G8 → G9)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The mobile crane lowers the second short gangway from just above the gap onto its bearings between the right vestibule and the right ledge, and the masons set the steps from the stack down to the footpath.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the second gangway is already sinking the last metre: it lands across the gap at the right end, the fitters bolt it and run its handrails, and masons set a few stone steps from the stack down to a footpath that leaves the right edge of the frame, until both ends of the carriage are reachable; the left gangway stays exactly where it is. At the end a long flatbed truck brings three large steel terrace frames onto the yard and the crane lifts the first one. A few clouds drift slowly from the left, and the shadows fall forward to the right.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized. Once seated on the deck, the carriage never lifts, swings or shifts again.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 9 — ÇATAR

```
SÜRE: 8,0 s (72,0–80,0)  ·  ELEMAN + ARA HÂL: üç büyük çelik teras modülü yakın kirişin dirsek uçlarına, soldan sağa (kamyon 3 → 0) · altından kanyon görünür  ·  REJİM: A (10 dk)  ·  SAAT: 14:40→14:50  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G9)

```
Photorealistic documentary site photograph — Scene 9 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits bolted on the steel support deck, deep emerald green with a cream band along the window tops, its rounded roof clad in warm copper-coloured sheets, eight broad clear windows along its near side; short dark steel gangways with handrails link its left vestibule to the gravel yard and its right vestibule, by a few steps, to a footpath on the right ledge, small lamps on short posts at their ends. A large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge, with a large steel terrace frame on the hook on taut slings, the frame hanging just above the left bracket stubs on the near girder. A long flatbed truck with two more large steel frames stands on the gravel yard, and fitters wait on the near walkway with taglines.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Twenty to three in the afternoon: both ends are linked, and the frame of the terrace is coming in.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The mobile crane stands on the gravel yard of the left ledge at about 372 pixels from the left, its outriggers at about 52 percent of frame height. The gravel yard lies at the upper left, around 376 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 224 degrees, elevation 24 degrees, behind the camera on the left: warm afternoon light on the near long side, shadows falling forward to the right, the canyon below in soft shade. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane lowers the first large steel terrace frame onto the left bracket stubs, then lifts the other two from the long flatbed truck and sets them beside it, fitters guide each with taglines and bolt it to the near girder, and welders join the three frames; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Fresh satin emerald paint with a soft sheen, copper-coloured roof sheets with bright cut edges, pallets and offcuts stacked on the gravel yard, tyre ruts in the gravel, a film of dust on the steel deck. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The frame hangs from the crane hook on four taut slings. Each frame is bolted to the bracket stubs along the near girder of the steel deck, which bears on steel pads on both ledges, and the truck stands on its tyres on the yard.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G9 → G10)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The mobile crane sets the three large steel terrace frames from the long flatbed truck onto the bracket stubs along the near girder, from left to right, and the fitters bolt them on.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first frame module is already sinking onto the left stubs: the crane sets one large open steel frame after another along the near side, from left to right, each bolted to the girder, until a terrace skeleton reaches towards the camera over the canyon, an open grid with the drop visible through it and a rectangular opening in its middle. The three frames on the truck go down to none and the empty truck drives off. At the end a truck brings pallets of timber deck boards and the crane lifts a pallet. A few clouds drift slowly from the left, and the shadows fall forward to the right.

The camera does not move at any point. The framing is identical in the first and last frame. The canyon, the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The canyon holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built is removed or resized. Once seated on the deck, the carriage never lifts, swings or shifts again.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
