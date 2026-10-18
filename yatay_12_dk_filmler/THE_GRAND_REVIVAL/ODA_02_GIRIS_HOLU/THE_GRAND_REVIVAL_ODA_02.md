# 🎬 THE_GRAND_REVIVAL — ODA 02 · GİRİŞ HOLÜ — TRAVERTEN, AVİZE, KONSOL  (S10–S16 · 7 sahne görseli + oda son kareleri + 7 I2V · 80,0–136,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler ve defterler `../THE_GRAND_REVIVAL_PLAN.md`'de durur;
> buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek başına çalışır. STRUCTURE (tam hâl) bütün promptlarda,
> SITE / BACKGROUND · COMPOSITION · NEGATIVE ve I2V'nin DEĞİŞMEYECEKLER paragrafı aynı istasyonun bütün promptlarında
> BİREBİR aynıdır; değişen AT THIS STAGE, THE TIME MOMENT, LIGHTING, TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.
>
> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/grv_gen.py` + `grv_data.py` +
> `grv_istasyon.py`) [DERS 20].
>
> ⭐ ÇOK İSTASYON (sahip istisnası 17.10.2026): her odanın kendi sabit kamerası ve kendi kare zinciri var. Bir odanın
> son klibi o odanın **ODA SON KARESİ**'nde (G<n>′) biter; sonraki odanın ilk görseli başka kameradır — oda sınırı
> bir KESMEDİR, ışık ve saat kesmede sürer. `🚪 ODA SON KARESİ` blokları prompt kapısının sayımına GİRMEZ (kapı
> zinciri tek istasyon sayar); onlar da üretilir ve zincir_kontrol'e girer.
> 🇹🇷 Her sahnenin başında: **önceki sahneye göre değişenler** ve **bu sahnede** ne olduğu.

---

## 🎬 SAHNE 10 — HOL BOŞALIR

```
SÜRE: 8,0 s (80,0–88,0)  ·  #11  ·  REJİM: A (10 dk)  ·  SAAT: 07:40→07:50  ·  İSTASYON: H · GİRİŞ HOLÜ
```

**🔄 Önceki sahneye göre değişen (→ G10):**

- ⛔ İSTASYON KESMESİ — ÖN CEPHE → **GİRİŞ HOLÜ** (sahip istisnası: oda başına sabit kamera)
- önceki oda sonu (G10′): Dış cephe ilk tamamlanmış hâlinde · içerisi henüz gösterilmedi
- bu odanın ilk karesi: Kırık eski konsol ve döküntü kapıdan dışarı taşınır
- ışık: 07:30→07:40 (kesmede saat sürer, atlamaz)

**▶ Bu sahnede:** Kırık eski konsol ve döküntü kapıdan dışarı taşınır; hol boşalır.

### 📸 GÖRSEL PROMPT (G10)

```
Photorealistic documentary photograph — Scene 10 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the entrance hall.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: HALL STATION — fixed tripod at the inner end of the entrance hall, lens 1.5 metres above the floor, 7.0 metres from the front wall, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: A broken old console table, heaps of fallen plaster and dry leaves lie across the floor. The walls are cracked and stained, the plaster fallen away in patches. The floor is bare grey screed with old stains. A short bare chain hangs from the ceiling over the middle of the hall. The left wall stands bare. The right wall stands bare. Both leaves of the walnut door stand open to the bright garden. A low flat cart waits just inside the door.

SITE / BACKGROUND: The entrance hall of the villa, six metres wide, with a high flat ceiling. In the middle of the far wall the front entrance opens in a round stone arch fitted with a walnut double door, and one tall narrow window stands at each side of the arch; through those windows the front garden shows, the lawn and an olive tree. The two side walls run plain to the far corners. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The hall keeps exactly these openings: one arch with its door and two narrow windows.

THE TIME MOMENT: Twenty to eight in the morning: the first job inside: the entrance hall lies dim and ruined behind the new walnut door.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone arch of the front entrance spans about 584 pixels of frame width at about 668 to 1252 pixels from the left, and keeps that width in every frame. The far wall spans about 411 to 1509 pixels from the left, its floor line at about twenty-five percent and its ceiling line at about ninety-six percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 85 degrees, elevation 33 degrees, outside on the left and ahead of the camera; sunlight falls in through the two narrow windows beside the arch in two long bright patches across the floor towards the camera, the rest of the hall in soft reflected light, and the view through the windows is bright daylight. Through the glass: a clear pale early-summer morning sky with a few small high clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the middle of the hall the two workers in dark blue shirts and grey trousers lift the broken old console table off the floor and carry it out through the open walnut door towards the low flat cart on the path, while heaps of plaster are shovelled into a barrow. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Dust lying grey over everything, damp stains and grime streaks on the walls, cracked plaster, dead leaves in drifts in the corners, debris heaped along the skirting. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The stone arch, the two narrow windows, the corners of the hall and the far hills never change shape, position, size or spacing. The hall keeps its one arch and two narrow windows; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G10 → G11)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the broken console and the heaps of fallen plaster from the hall floor out through the open walnut door onto the low flat cart on the path.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Load by load the debris goes out, the console first and then barrow after barrow of plaster and dry leaves, until the floor lies bare and swept. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The stone arch, the two narrow windows and the far corners of the hall stay exactly where they are, at exactly the same size and shape, for the whole shot; the stone arch occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the arch and the windows of the hall are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 11 — DUVAR ONARILIR

```
SÜRE: 8,0 s (88,0–96,0)  ·  #12  ·  REJİM: A (10 dk)  ·  SAAT: 07:50→08:00  ·  İSTASYON: H · GİRİŞ HOLÜ
```

**🔄 Önceki sahneye göre değişen (→ G11):**

- önceki klibin hedefi = bu klibin ilk karesi: Hol boş · kemer, kapı, iki dar pencere sabit
- ışık: 07:40 → 07:50

**▶ Bu sahnede:** Bozuk duvar yüzeyleri sıvayla onarılır; duvarlar düz, henüz boyasız.

### 📸 GÖRSEL PROMPT (G11)

```
Photorealistic documentary photograph — Scene 11 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the entrance hall.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: HALL STATION — fixed tripod at the inner end of the entrance hall, lens 1.5 metres above the floor, 7.0 metres from the front wall, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The floor is swept clear. The walls are cracked and stained, the plaster fallen away in patches. The floor is bare grey screed with old stains. A short bare chain hangs from the ceiling over the middle of the hall. The left wall stands bare. The right wall stands bare. Both leaves of the walnut door stand open to the bright garden. A folded aluminium stepladder stands by the right wall, a low flat cart inside the door.

SITE / BACKGROUND: The entrance hall of the villa, six metres wide, with a high flat ceiling. In the middle of the far wall the front entrance opens in a round stone arch fitted with a walnut double door, and one tall narrow window stands at each side of the arch; through those windows the front garden shows, the lawn and an olive tree. The two side walls run plain to the far corners. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The hall keeps exactly these openings: one arch with its door and two narrow windows.

THE TIME MOMENT: Ten to eight in the morning: the hall is empty and swept, its walls cracked and stained.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone arch of the front entrance spans about 584 pixels of frame width at about 668 to 1252 pixels from the left, and keeps that width in every frame. The far wall spans about 411 to 1509 pixels from the left, its floor line at about twenty-five percent and its ceiling line at about ninety-six percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 86 degrees, elevation 35 degrees, outside on the left and ahead of the camera; sunlight falls in through the two narrow windows beside the arch in two long bright patches across the floor towards the camera, the rest of the hall in soft reflected light, and the view through the windows is bright daylight. Through the glass: a clear pale early-summer morning sky with a few small high clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Along the right wall the two workers in dark blue shirts and grey trousers set a folded stepladder against the wall and spread fresh grey-white plaster over the cracks with wide trowels from a bucket on the low flat cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The stone arch, the two narrow windows, the corners of the hall and the far hills never change shape, position, size or spacing. The hall keeps its one arch and two narrow windows; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G11 → G12)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry buckets of fresh plaster from the low flat cart to the walls and spread it onto the cracked surfaces with wide trowels, from the left wall round to the right wall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Patch by patch the cracks and bare spots close under smooth grey-white plaster, the patched area spreading along the left wall, across the far wall around the door and along the right wall. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The stone arch, the two narrow windows and the far corners of the hall stay exactly where they are, at exactly the same size and shape, for the whole shot; the stone arch occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the arch and the windows of the hall are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 12 — TRAVERTEN

```
SÜRE: 8,0 s (96,0–104,0)  ·  #13  ·  REJİM: A (10 dk)  ·  SAAT: 08:00→08:10  ·  İSTASYON: H · GİRİŞ HOLÜ
```

**🔄 Önceki sahneye göre değişen (→ G12):**

- önceki klibin hedefi = bu klibin ilk karesi: Duvarlar düz, gri-beyaz, boyasız
- ışık: 07:50 → 08:00

**▶ Bu sahnede:** Büyük traverten zemin plakaları kapı eşiğinden kameraya doğru döşenir.

### 📸 GÖRSEL PROMPT (G12)

```
Photorealistic documentary photograph — Scene 12 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the entrance hall.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: HALL STATION — fixed tripod at the inner end of the entrance hall, lens 1.5 metres above the floor, 7.0 metres from the front wall, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The floor is swept clear. The walls are freshly patched with grey-white plaster, still unpainted. The floor is bare grey screed with old stains. A short bare chain hangs from the ceiling over the middle of the hall. The left wall stands bare. The right wall stands bare. Both leaves of the walnut door stand open to the bright garden. A folded aluminium stepladder stands by the right wall, a low flat cart inside the door.

SITE / BACKGROUND: The entrance hall of the villa, six metres wide, with a high flat ceiling. In the middle of the far wall the front entrance opens in a round stone arch fitted with a walnut double door, and one tall narrow window stands at each side of the arch; through those windows the front garden shows, the lawn and an olive tree. The two side walls run plain to the far corners. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The hall keeps exactly these openings: one arch with its door and two narrow windows.

THE TIME MOMENT: Eight o'clock in the morning: the walls are smooth fresh plaster, and the floor is still bare grey screed.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone arch of the front entrance spans about 584 pixels of frame width at about 668 to 1252 pixels from the left, and keeps that width in every frame. The far wall spans about 411 to 1509 pixels from the left, its floor line at about twenty-five percent and its ceiling line at about ninety-six percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 88 degrees, elevation 37 degrees, outside on the left and ahead of the camera; sunlight falls in through the two narrow windows beside the arch in two long bright patches across the floor towards the camera, the rest of the hall in soft reflected light, and the view through the windows is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the far end of the floor the two workers in dark blue shirts and grey trousers lift the first large travertine tiles off a stack on a pallet just inside the door and set them on a bed of mortar, a low flat cart bringing more. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The stone arch, the two narrow windows, the corners of the hall and the far hills never change shape, position, size or spacing. The hall keeps its one arch and two narrow windows; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G12 → G13)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers lay the large pale travertine tiles from the stack on the pallet onto a mortar bed, row after row from the door towards the camera.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The pale surface grows row by row from the threshold towards the camera, each tile set and tapped level, until the bare screed is covered edge to edge; the stack on the pallet shrinks to nothing and the empty pallet goes out on the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The stone arch, the two narrow windows and the far corners of the hall stay exactly where they are, at exactly the same size and shape, for the whole shot; the stone arch occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the arch and the windows of the hall are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 13 — BOYA

```
SÜRE: 8,0 s (104,0–112,0)  ·  #14  ·  REJİM: A (10 dk)  ·  SAAT: 08:10→08:20  ·  İSTASYON: H · GİRİŞ HOLÜ
```

**🔄 Önceki sahneye göre değişen (→ G13):**

- önceki klibin hedefi = bu klibin ilk karesi: Açık traverten zemin kesintisiz
- ışık: 08:00 → 08:10

**▶ Bu sahnede:** Duvarlar sıcak kırık beyaza boyanır.

### 📸 GÖRSEL PROMPT (G13)

```
Photorealistic documentary photograph — Scene 13 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the entrance hall.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: HALL STATION — fixed tripod at the inner end of the entrance hall, lens 1.5 metres above the floor, 7.0 metres from the front wall, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are freshly patched with grey-white plaster, still unpainted. The floor is laid with large pale travertine tiles. A short bare chain hangs from the ceiling over the middle of the hall. The left wall stands bare. The right wall stands bare. Both leaves of the walnut door stand open to the bright garden. A roll of grey protective membrane lies along the wall, a stepladder beside it.

SITE / BACKGROUND: The entrance hall of the villa, six metres wide, with a high flat ceiling. In the middle of the far wall the front entrance opens in a round stone arch fitted with a walnut double door, and one tall narrow window stands at each side of the arch; through those windows the front garden shows, the lawn and an olive tree. The two side walls run plain to the far corners. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The hall keeps exactly these openings: one arch with its door and two narrow windows.

THE TIME MOMENT: Ten past eight in the morning: the travertine floor is laid, and the patched walls are still unpainted grey-white.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone arch of the front entrance spans about 584 pixels of frame width at about 668 to 1252 pixels from the left, and keeps that width in every frame. The far wall spans about 411 to 1509 pixels from the left, its floor line at about twenty-five percent and its ceiling line at about ninety-six percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 89 degrees, elevation 39 degrees, outside on the left and ahead of the camera; sunlight falls in through the two narrow windows beside the arch in two long bright patches across the floor towards the camera, the rest of the hall in soft reflected light, and the view through the windows is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Across the new travertine the two workers in dark blue shirts and grey trousers unroll a grey protective membrane and set the first rollers of warm off-white paint against the left wall, tins of paint on the low flat cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The stone arch, the two narrow windows, the corners of the hall and the far hills never change shape, position, size or spacing. The hall keeps its one arch and two narrow windows; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G13 → G14)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers roll warm off-white paint from the tins on the low flat cart onto the patched walls, the left wall first, then the far wall around the door, then the right wall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The grey-white patches go under an even warm off-white, the fresh colour spreading wall by wall and the hall turning brighter in the morning light; the empty tins are stacked back on the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The stone arch, the two narrow windows and the far corners of the hall stay exactly where they are, at exactly the same size and shape, for the whole shot; the stone arch occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the arch and the windows of the hall are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 14 — AVİZE

```
SÜRE: 8,0 s (112,0–120,0)  ·  #15  ·  REJİM: A (10 dk)  ·  SAAT: 08:20→08:30  ·  İSTASYON: H · GİRİŞ HOLÜ
```

**🔄 Önceki sahneye göre değişen (→ G14):**

- önceki klibin hedefi = bu klibin ilk karesi: Duvarlar sıcak kırık beyaz · hol aydınlık
- ışık: 08:10 → 08:20

**▶ Bu sahnede:** Büyük bronz avize iki işçi ve sabit merdivenle mevcut bağlantıya takılır.

### 📸 GÖRSEL PROMPT (G14)

```
Photorealistic documentary photograph — Scene 14 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the entrance hall.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: HALL STATION — fixed tripod at the inner end of the entrance hall, lens 1.5 metres above the floor, 7.0 metres from the front wall, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm off-white. The floor is laid with large pale travertine tiles. A short bare chain hangs from the ceiling over the middle of the hall. The left wall stands bare. The right wall stands bare. Both leaves of the walnut door stand open to the bright garden. Grey protective membrane covers the travertine, a stepladder stands under the bare chain.

SITE / BACKGROUND: The entrance hall of the villa, six metres wide, with a high flat ceiling. In the middle of the far wall the front entrance opens in a round stone arch fitted with a walnut double door, and one tall narrow window stands at each side of the arch; through those windows the front garden shows, the lawn and an olive tree. The two side walls run plain to the far corners. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The hall keeps exactly these openings: one arch with its door and two narrow windows.

THE TIME MOMENT: Twenty past eight in the morning: the hall is painted warm off-white, and a short bare chain hangs from the ceiling.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone arch of the front entrance spans about 584 pixels of frame width at about 668 to 1252 pixels from the left, and keeps that width in every frame. The far wall spans about 411 to 1509 pixels from the left, its floor line at about twenty-five percent and its ceiling line at about ninety-six percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 91 degrees, elevation 41 degrees, outside on the right and ahead of the camera; sunlight falls in through the two narrow windows beside the arch in two long bright patches across the floor towards the camera, the rest of the hall in soft reflected light, and the view through the windows is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Under the bare chain the two workers in dark blue shirts and grey trousers set a tall stepladder and lift the large bronze chandelier out of its padded crate on the low flat cart, carrying it between them towards the ladder. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The stone arch, the two narrow windows, the corners of the hall and the far hills never change shape, position, size or spacing. The hall keeps its one arch and two narrow windows; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G14 → G15)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the bronze chandelier from its crate on the low flat cart to the stepladder and hang it onto the short chain at the middle of the ceiling.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. One worker on the ladder takes the weight while the other lifts from below; the chandelier rises the last metre, is hooked onto the chain and hangs level, unlit, and the empty crate is carried out to the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The stone arch, the two narrow windows and the far corners of the hall stay exactly where they are, at exactly the same size and shape, for the whole shot; the stone arch occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the arch and the windows of the hall are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 15 — KONSOL

```
SÜRE: 8,0 s (120,0–128,0)  ·  #16  ·  REJİM: A (10 dk)  ·  SAAT: 08:30→08:40  ·  İSTASYON: H · GİRİŞ HOLÜ
```

**🔄 Önceki sahneye göre değişen (→ G15):**

- önceki klibin hedefi = bu klibin ilk karesi: Avize asılı, sönük
- ışık: 08:20 → 08:30

**▶ Bu sahnede:** Üç metrelik traverten konsol parça parça taşınıp sol duvara kurulur; üstüne tek vazo konur.

### 📸 GÖRSEL PROMPT (G15)

```
Photorealistic documentary photograph — Scene 15 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the entrance hall.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: HALL STATION — fixed tripod at the inner end of the entrance hall, lens 1.5 metres above the floor, 7.0 metres from the front wall, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm off-white. The floor is laid with large pale travertine tiles. A large bronze chandelier hangs from the ceiling over the middle of the hall on a short chain, unlit. The left wall stands bare. The right wall stands bare. Both leaves of the walnut door stand open to the bright garden. Grey protective membrane runs along the walking line on the travertine, a low flat cart inside the door.

SITE / BACKGROUND: The entrance hall of the villa, six metres wide, with a high flat ceiling. In the middle of the far wall the front entrance opens in a round stone arch fitted with a walnut double door, and one tall narrow window stands at each side of the arch; through those windows the front garden shows, the lawn and an olive tree. The two side walls run plain to the far corners. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The hall keeps exactly these openings: one arch with its door and two narrow windows.

THE TIME MOMENT: Half past eight in the morning: the bronze chandelier hangs over the hall, and the left wall stands bare.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone arch of the front entrance spans about 584 pixels of frame width at about 668 to 1252 pixels from the left, and keeps that width in every frame. The far wall spans about 411 to 1509 pixels from the left, its floor line at about twenty-five percent and its ceiling line at about ninety-six percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 92 degrees, elevation 43 degrees, outside on the right and ahead of the camera; sunlight falls in through the two narrow windows beside the arch in two long bright patches across the floor towards the camera, the rest of the hall in soft reflected light, and the view through the windows is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Just inside the walnut door the two workers in dark blue shirts and grey trousers lift the first stone leg of the long console off the low flat cart and set it against the far part of the left wall, the long travertine top waiting on the cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The stone arch, the two narrow windows, the corners of the hall and the far hills never change shape, position, size or spacing. The hall keeps its one arch and two narrow windows; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G15 → G16)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the long travertine console top from the low flat cart to the left wall and set it onto its two stone legs against the wall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The two legs go down first against the far part of the left wall; the workers slide the long top off the cart, carry it between them and lower it onto the legs. Late in the shot one tall ceramic vase is lifted from a crate on the cart and set on the console. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The stone arch, the two narrow windows and the far corners of the hall stay exactly where they are, at exactly the same size and shape, for the whole shot; the stone arch occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the arch and the windows of the hall are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 16 — BANK VE TABLO

```
SÜRE: 8,0 s (128,0–136,0)  ·  #17  ·  REJİM: A (10 dk)  ·  SAAT: 08:40→08:50  ·  İSTASYON: H · GİRİŞ HOLÜ
```

**🔄 Önceki sahneye göre değişen (→ G16):**

- önceki klibin hedefi = bu klibin ilk karesi: Tek konsol sol duvarda, üstünde tek vazo
- ışık: 08:30 → 08:40

**▶ Bu sahnede:** Uzun döşemeli bank sağ duvara, konsolun üstüne büyük tablo; kapı kapanır. Hol tamam.

### 📸 GÖRSEL PROMPT (G16)

```
Photorealistic documentary photograph — Scene 16 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the entrance hall.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: HALL STATION — fixed tripod at the inner end of the entrance hall, lens 1.5 metres above the floor, 7.0 metres from the front wall, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm off-white. The floor is laid with large pale travertine tiles. A large bronze chandelier hangs from the ceiling over the middle of the hall on a short chain, unlit. A three-metre travertine console stands against the far part of the left wall, one tall ceramic vase on it. The right wall stands bare. Both leaves of the walnut door stand open to the bright garden. Grey protective membrane runs along the walking line on the travertine, a low flat cart inside the door.

SITE / BACKGROUND: The entrance hall of the villa, six metres wide, with a high flat ceiling. In the middle of the far wall the front entrance opens in a round stone arch fitted with a walnut double door, and one tall narrow window stands at each side of the arch; through those windows the front garden shows, the lawn and an olive tree. The two side walls run plain to the far corners. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The hall keeps exactly these openings: one arch with its door and two narrow windows.

THE TIME MOMENT: Twenty to nine in the morning: the travertine console stands against the left wall, and the right wall stands bare.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone arch of the front entrance spans about 584 pixels of frame width at about 668 to 1252 pixels from the left, and keeps that width in every frame. The far wall spans about 411 to 1509 pixels from the left, its floor line at about twenty-five percent and its ceiling line at about ninety-six percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 94 degrees, elevation 45 degrees, outside on the right and ahead of the camera; sunlight falls in through the two narrow windows beside the arch in two long bright patches across the floor towards the camera, the rest of the hall in soft reflected light, and the view through the windows is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Inside the walnut door the two workers in dark blue shirts and grey trousers lift a long upholstered cream bench off the low flat cart and carry it towards the right wall, a large framed painting in its wrapping leaning by the door. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The stone arch, the two narrow windows, the corners of the hall and the far hills never change shape, position, size or spacing. The hall keeps its one arch and two narrow windows; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G16 → G17′)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the long cream bench from the low flat cart to the right wall, then lift the framed painting from beside the door onto the wall above the console.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The bench is set down against the far part of the right wall, leaving the way to the door open; the wrapping comes off the painting and it goes up on two hooks above the console, hanging level. The workers roll up the grey membrane, wheel the empty cart out and close the walnut door. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The stone arch, the two narrow windows and the far corners of the hall stay exactly where they are, at exactly the same size and shape, for the whole shot; the stone arch occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the arch and the windows of the hall are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🚪 ODA SON KARESİ (G17′ · GİRİŞ HOLÜ) — S16'in hedefi · kapı saymaz

> GİRİŞ HOLÜ kamerasının son karesi; sonraki sahne başka istasyondan açılır. Önce bu kare üretilir (odanın
> usta karesi), oda zinciri ondan GERİYE türetilir.

```
Photorealistic documentary photograph — end frame of Scene 16 of 90, the target frame of that shot. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the entrance hall.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: HALL STATION — fixed tripod at the inner end of the entrance hall, lens 1.5 metres above the floor, 7.0 metres from the front wall, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm off-white. The floor is laid with large pale travertine tiles. A large bronze chandelier hangs from the ceiling over the middle of the hall on a short chain, unlit. A three-metre travertine console stands against the far part of the left wall, one tall ceramic vase on it. A long upholstered cream bench stands against the far part of the right wall, and a large framed painting hangs above the console. Both leaves of the walnut door are closed. A strip of grey protective membrane lies rolled up by the door, a folded stepladder against it.

SITE / BACKGROUND: The entrance hall of the villa, six metres wide, with a high flat ceiling. In the middle of the far wall the front entrance opens in a round stone arch fitted with a walnut double door, and one tall narrow window stands at each side of the arch; through those windows the front garden shows, the lawn and an olive tree. The two side walls run plain to the far corners. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The hall keeps exactly these openings: one arch with its door and two narrow windows.

THE TIME MOMENT: Ten to nine in the morning: the entrance hall is finished: travertine floor, warm white walls, the bronze chandelier, the console with its vase and painting, and the long bench.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone arch of the front entrance spans about 584 pixels of frame width at about 668 to 1252 pixels from the left, and keeps that width in every frame. The far wall spans about 411 to 1509 pixels from the left, its floor line at about twenty-five percent and its ceiling line at about ninety-six percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 96 degrees, elevation 47 degrees, outside on the right and ahead of the camera; sunlight falls in through the two narrow windows beside the arch in two long bright patches across the floor towards the camera, the rest of the hall in soft reflected light, and the view through the windows is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: By the closed walnut door the two workers in dark blue shirts and grey trousers lift the rolled membrane onto the low flat cart and wheel it out of the frame at the right. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A soft sheen on the new floor, a last faint band of dust along one skirting, faint shoe prints near the door, a folded stack of dust sheets, one small offcut forgotten by the wall. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The stone arch, the two narrow windows, the corners of the hall and the far hills never change shape, position, size or spacing. The hall keeps its one arch and two narrow windows; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

---
