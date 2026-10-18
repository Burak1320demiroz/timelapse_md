# 🎬 THE_GRAND_REVIVAL — ODA 06 · ANA YATAK ODASI — BAŞLIK, KING YATAK, KOMODİNLER  (S54–S65 · 12 sahne görseli + oda son kareleri + 12 I2V · 432,0–528,0 sn)

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

## 🎬 SAHNE 54 — ESKİ YATAK ÇIKAR

```
SÜRE: 8,0 s (432,0–440,0)  ·  #55  ·  REJİM: A (10 dk)  ·  SAAT: 14:30→14:40  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G54):**

- ⛔ İSTASYON KESMESİ — MUTFAK → **YATAK ODASI** (sahip istisnası: oda başına sabit kamera)
- önceki oda sonu (G54′): Dört tabure · ada, kiler, cihazlar, tezgâh tamam
- bu odanın ilk karesi: Eski yatak çerçevesi koridor kapısından çıkarılır
- ışık: 14:20→14:30 (kesmede saat sürer, atlamaz)

**▶ Bu sahnede:** Eski yatak çerçevesi koridor kapısından çıkarılır; yatak duvarı, pencere ve kapılar aynı.

### 📸 GÖRSEL PROMPT (G54)

```
Photorealistic documentary photograph — Scene 54 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: An old iron bed frame with a sagging mattress stands against the far wall, debris around it. The walls are cracked and stained. The floor is bare grey screed. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. A low flat cart stands just inside the corridor door.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Half past two in the afternoon: the main bedroom lies dim and ruined, an old iron bed against its far wall.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 256 degrees, elevation 55 degrees, outside on the right and ahead of the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the far wall the two workers in dark blue shirts and grey trousers lift the old iron bed frame and its sagging mattress off the floor and carry them towards a low flat cart inside the corridor door. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Dust lying grey over everything, damp stains and grime streaks on the walls, cracked plaster, dead leaves in drifts in the corners, debris heaped along the skirting. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G54 → G55)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the old bed frame, the mattress and the debris from the floor out through the corridor door onto the low flat cart.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Load by load the room empties, the mattress first, then the iron frame in two pieces, then barrows of debris, until the floor lies bare and swept. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 55 — DUVAR VE GREJ

```
SÜRE: 8,0 s (440,0–448,0)  ·  #56  ·  REJİM: A (10 dk)  ·  SAAT: 14:40→14:50  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G55):**

- önceki klibin hedefi = bu klibin ilk karesi: Oda boş · kapı, pencere, giyinme kapısı aynı
- ışık: 14:30 → 14:40

**▶ Bu sahnede:** Duvarlar onarılıp sakin sıcak greje getirilir.

### 📸 GÖRSEL PROMPT (G55)

```
Photorealistic documentary photograph — Scene 55 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are cracked and stained. The floor is bare grey screed. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. A folded stepladder stands by the right wall, a low flat cart inside the corridor door.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Twenty to three in the afternoon: the bedroom is empty, its walls cracked and stained.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 259 degrees, elevation 53 degrees, outside on the right and ahead of the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: By the right wall the two workers in dark blue shirts and grey trousers set a stepladder and spread plaster over the cracks from a bucket on the low flat cart, rolling warm greige paint behind it. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G55 → G56)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry plaster and paint from the low flat cart to the walls and spread them onto the cracked surfaces, wall by wall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The cracks close and the walls turn an even calm greige, and the empty buckets are stacked back on the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 56 — MEŞE PARKE

```
SÜRE: 8,0 s (448,0–456,0)  ·  #57  ·  REJİM: A (10 dk)  ·  SAAT: 14:50→15:00  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G56):**

- önceki klibin hedefi = bu klibin ilk karesi: Duvar bitişi tamam
- ışık: 14:40 → 14:50

**▶ Bu sahnede:** Meşe parke uzak duvardan kameraya doğru döşenir.

### 📸 GÖRSEL PROMPT (G56)

```
Photorealistic documentary photograph — Scene 56 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are smoothed and painted a calm warm greige. The floor is bare grey screed. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. A folded stepladder stands by the right wall, a low flat cart inside the corridor door.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Ten to three in the afternoon: the walls are calm greige, and the floor is still bare grey screed.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 261 degrees, elevation 51 degrees, outside on the right and ahead of the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Along the far wall the two workers in dark blue shirts and grey trousers lift the first pale oak boards off a stack on the low flat cart and set the first row, a trestle workbench by the left wall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G56 → G57)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers lay the pale oak boards from the stack on the low flat cart onto the screed, row after row from the far wall towards the camera.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The boards advance in one direction, each cut to length at the workbench, until the whole room is oak. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 57 — BAŞLIK

```
SÜRE: 8,0 s (456,0–464,0)  ·  #58  ·  REJİM: A (10 dk)  ·  SAAT: 15:00→15:10  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G57):**

- önceki klibin hedefi = bu klibin ilk karesi: Meşe zemin, bu kameraya göre sabit yön
- ışık: 14:50 → 15:00

**▶ Bu sahnede:** Geniş döşemeli başlık paneli uzak duvarın ortasına monte edilir.

### 📸 GÖRSEL PROMPT (G57)

```
Photorealistic documentary photograph — Scene 57 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. A trestle workbench with offcuts stands by the left wall, grey protective membrane rolled beside it.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Three o'clock in the afternoon: the oak floor is down, and the far wall is plain greige.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 262 degrees, elevation 49 degrees, outside on the right and ahead of the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the far wall the two workers in dark blue shirts and grey trousers lift the wide upholstered headboard panel off the low flat cart and walk it upright towards the middle of the wall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G57 → G58)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the wide headboard panel from the low flat cart to the far wall and fix it onto the middle of the wall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They lift it onto its wall rail, centre it and fix it level; the corridor door at the left end stays clear. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 58 — PERDELER

```
SÜRE: 8,0 s (464,0–472,0)  ·  #59  ·  REJİM: A (10 dk)  ·  SAAT: 15:10→15:20  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G58):**

- önceki klibin hedefi = bu klibin ilk karesi: Başlık duvarı ölçüsü değişmez
- ışık: 15:00 → 15:10

**▶ Bu sahnede:** Tavandan yere perdeler sabit kornişe asılır; pencere ölçüsü ve konumu değişmez.

### 📸 GÖRSEL PROMPT (G58)

```
Photorealistic documentary photograph — Scene 58 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. A wide upholstered greige headboard panel covers the middle of the far wall. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. Grey protective membrane runs from the corridor door along the walking line, a stepladder by the far wall.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Ten past three in the afternoon: the greige headboard covers the middle of the far wall.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 264 degrees, elevation 47 degrees, outside on the right and ahead of the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Under the tall window the two workers in dark blue shirts and grey trousers set a stepladder and lift a bundle of folded linen curtains off the low flat cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G58 → G59)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the folded linen curtains from the low flat cart to the tall window in the right wall and hang them from the rod, ceiling to floor.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The linen falls in soft folds at both sides of the window, which keeps its size and place. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 59 — HALI

```
SÜRE: 8,0 s (472,0–480,0)  ·  #60  ·  REJİM: A (10 dk)  ·  SAAT: 15:20→15:30  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G59):**

- önceki klibin hedefi = bu klibin ilk karesi: Perdeler asılı
- ışık: 15:10 → 15:20

**▶ Bu sahnede:** Büyük halı serilir; sonda iki işçi daha katılır, yatak gövdesi kapıdan gelir. Bölüm 2 sonu.

### 📸 GÖRSEL PROMPT (G59)

```
Photorealistic documentary photograph — Scene 59 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. A wide upholstered greige headboard panel covers the middle of the far wall. Floor-length linen curtains hang at the tall window in the right wall. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. Grey protective membrane runs from the corridor door along the walking line, a stepladder by the far wall.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Twenty past three in the afternoon: curtains hang at the tall window, and the floor in front of the headboard is bare oak.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 266 degrees, elevation 45 degrees, outside on the right and ahead of the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Inside the corridor door the two workers in dark blue shirts and grey trousers lift a big rolled grey rug off the low flat cart and set it down in front of the headboard, ready to unroll. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G59 → G60)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the rolled grey rug from the low flat cart to the space in front of the headboard and unroll it towards the camera.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The rug opens flat and is squared to the headboard. Late in the shot two more workers in the same clothes help carry the king-size bed base in on its side through the corridor door and lay it flat on a low flat cart just inside the door. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 60 — KING YATAK

```
SÜRE: 8,0 s (480,0–488,0)  ·  #61  ·  REJİM: G (gerçek zaman)  ·  SAAT: 15:30→15:30  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G60):**

- önceki klibin hedefi = bu klibin ilk karesi: Halı yerinde · yatak gövdesi arabada, kapının içinde · BÖLÜM 2 sonu (480,0 sn)
- ışık: 15:20 → 15:30

**▶ Bu sahnede:** GERÇEK ZAMAN · dört işçi king yatak gövdesini başlığa ortalar.

### 📸 GÖRSEL PROMPT (G60)

```
Photorealistic documentary photograph — Scene 60 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. A wide upholstered greige headboard panel covers the middle of the far wall. Floor-length linen curtains hang at the tall window in the right wall. A large soft grey rug lies in front of the headboard. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. The king-size bed base lies flat on a low flat cart just inside the corridor door. Grey protective membrane runs from the corridor door along the walking line, lifting slings coiled on it.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Half past three in the afternoon: the king-size bed base lies flat on a low flat cart just inside the corridor door.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 268 degrees, elevation 43 degrees, outside on the right and ahead of the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the workers carry at their real pace and the light holds still; nothing is accelerated.

ACTIVITY: Inside the corridor door four workers in the same dark blue shirts and grey trousers lift the king-size bed base off the low flat cart, two at each side, and carry it slowly towards the headboard. Every person is seen from the side or from behind, back to the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The load is gripped in the workers' hands, its weight on their arms and backs, its underside clear of the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G60 → G61)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: Four workers lift the king-size bed base from the low flat cart at the corridor door, carry it to the headboard and set it down centred on the rug.

Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame the base is already lifting off the cart; the four carry it in short careful steps, turn it square to the headboard and lower it until its feet stand on the rug, then step back to the sides. Through the glass the few small clouds hold still.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 61 — ŞİLTE VE NEVRESİM

```
SÜRE: 8,0 s (488,0–496,0)  ·  #62  ·  REJİM: A (10 dk)  ·  SAAT: 15:30→15:40  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G61):**

- önceki klibin hedefi = bu klibin ilk karesi: Yatak gövdesi başlığa ortalı
- ışık: 15:30 → 15:30

**▶ Bu sahnede:** Şilte gövdeye konur; sonda nevresim ve yastıklar düzenlenir.

### 📸 GÖRSEL PROMPT (G61)

```
Photorealistic documentary photograph — Scene 61 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. A wide upholstered greige headboard panel covers the middle of the far wall. Floor-length linen curtains hang at the tall window in the right wall. A large soft grey rug lies in front of the headboard. A king-size bed base stands centred on the headboard. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. Grey protective membrane runs from the corridor door along the walking line, lifting slings coiled on it.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Half past three in the afternoon: the bed base stands centred on the headboard.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 268 degrees, elevation 43 degrees, outside on the right and ahead of the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the corridor door the two workers in dark blue shirts and grey trousers lift the thick mattress off the low flat cart and carry it towards the bed base, white linen folded on the cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G61 → G62)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the thick mattress from the low flat cart at the corridor door to the bed and lower it onto the base, then lay the white linen and pillows onto it.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The mattress settles on the base; the sheets are spread and tucked, the cover is laid smooth and the pillows are set against the headboard. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 62 — KOMODİNLER

```
SÜRE: 8,0 s (496,0–504,0)  ·  #63  ·  REJİM: A (10 dk)  ·  SAAT: 15:40→15:50  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G62):**

- önceki klibin hedefi = bu klibin ilk karesi: Tek yatak, sabit örtü düzeni
- ışık: 15:30 → 15:40

**▶ Bu sahnede:** İki komodin sırayla yatağın iki yanına; sonda iki abajur. Toplam iki + iki.

### 📸 GÖRSEL PROMPT (G62)

```
Photorealistic documentary photograph — Scene 62 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. A wide upholstered greige headboard panel covers the middle of the far wall. Floor-length linen curtains hang at the tall window in the right wall. A large soft grey rug lies in front of the headboard. A king-size bed stands centred on the headboard, made up with a thick mattress, white linen and pillows. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. Grey protective membrane runs from the corridor door along the walking line, a low flat cart at the door.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Twenty to four in the afternoon: the bed is made up in white linen.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 269 degrees, elevation 41 degrees, outside on the right and ahead of the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the corridor door the two workers in dark blue shirts and grey trousers lift the first walnut bedside table off the low flat cart and carry it to the left side of the bed. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G62 → G63)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the two walnut bedside tables one at a time from the low flat cart at the corridor door to the two sides of the bed, then set one small lamp onto each.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The left table goes down first, then the right; one small lamp is set on each, unlit, so two tables and two lamps flank the bed. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 63 — YATAK UCU BANKI

```
SÜRE: 8,0 s (504,0–512,0)  ·  #64  ·  REJİM: A (10 dk)  ·  SAAT: 15:50→16:00  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G63):**

- önceki klibin hedefi = bu klibin ilk karesi: İki komodin, iki abajur
- ışık: 15:40 → 15:50

**▶ Bu sahnede:** Yatak ucuna uzun döşemeli bank; geçişler açık.

### 📸 GÖRSEL PROMPT (G63)

```
Photorealistic documentary photograph — Scene 63 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. A wide upholstered greige headboard panel covers the middle of the far wall. Floor-length linen curtains hang at the tall window in the right wall. A large soft grey rug lies in front of the headboard. A king-size bed stands centred on the headboard, made up with a thick mattress, white linen and pillows. A walnut bedside table with one small lamp stands at each side of the bed — two tables and two lamps. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. Grey protective membrane runs from the corridor door along the walking line, a low flat cart at the door.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Ten to four in the afternoon: two bedside tables with lamps flank the bed.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 271 degrees, elevation 39 degrees, outside on the right and behind the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the corridor door the two workers in dark blue shirts and grey trousers lift a long upholstered bench off the low flat cart and carry it towards the foot of the bed. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G63 → G64)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the long bench from the low flat cart at the corridor door to the foot of the bed and set it down across it.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They square it to the bed, leaving the walkways at both sides open. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 64 — ŞEZLONG

```
SÜRE: 8,0 s (512,0–520,0)  ·  #65  ·  REJİM: A (10 dk)  ·  SAAT: 16:00→16:10  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G64):**

- önceki klibin hedefi = bu klibin ilk karesi: Bank yatak ucunda, geçişler açık
- ışık: 15:50 → 16:00

**▶ Bu sahnede:** Pencere yanına büyük şezlong; dinlenme köşesi oluşur.

### 📸 GÖRSEL PROMPT (G64)

```
Photorealistic documentary photograph — Scene 64 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. A wide upholstered greige headboard panel covers the middle of the far wall. Floor-length linen curtains hang at the tall window in the right wall. A large soft grey rug lies in front of the headboard. A king-size bed stands centred on the headboard, made up with a thick mattress, white linen and pillows. A walnut bedside table with one small lamp stands at each side of the bed — two tables and two lamps. A long upholstered bench stands across the foot of the bed. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. Grey protective membrane runs from the corridor door along the walking line, a low flat cart at the door.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Four o'clock in the afternoon: the bench stands across the foot of the bed.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 272 degrees, elevation 37 degrees, outside on the right and behind the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the corridor door the two workers in dark blue shirts and grey trousers lift a large cream chaise longue off the low flat cart and carry it towards the window. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G64 → G65)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the chaise longue from the low flat cart at the corridor door to the window in the right wall and set it down beside the curtains.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They angle it towards the window and step back; a quiet reading corner forms by the light. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 65 — MAKYAJ KONSOLU

```
SÜRE: 8,0 s (520,0–528,0)  ·  #66  ·  REJİM: A (10 dk)  ·  SAAT: 16:10→16:20  ·  İSTASYON: M · YATAK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G65):**

- önceki klibin hedefi = bu klibin ilk karesi: Dinlenme köşesi
- ışık: 16:00 → 16:10

**▶ Bu sahnede:** Makyaj konsolu ve tek pufu sırayla sol duvara; yatak odası tamam.

### 📸 GÖRSEL PROMPT (G65)

```
Photorealistic documentary photograph — Scene 65 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. A wide upholstered greige headboard panel covers the middle of the far wall. Floor-length linen curtains hang at the tall window in the right wall. A large soft grey rug lies in front of the headboard. A king-size bed stands centred on the headboard, made up with a thick mattress, white linen and pillows. A walnut bedside table with one small lamp stands at each side of the bed — two tables and two lamps. A long upholstered bench stands across the foot of the bed. A large cream chaise longue stands by the window in the right wall. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. Grey protective membrane runs from the corridor door along the walking line, a low flat cart at the door.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Ten past four in the afternoon: the chaise longue stands by the window.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 274 degrees, elevation 35 degrees, outside on the right and behind the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the corridor door the two workers in dark blue shirts and grey trousers lift a slim walnut dressing table off the low flat cart, its small upholstered stool waiting on the cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G65 → G66′)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the dressing table from the low flat cart at the corridor door to the left wall, then set its small stool in front of it.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The table is set against the left wall beyond the doorway and the stool tucked under it. The workers roll up the membrane and wheel the cart out through the corridor door. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The corridor door, the tall window, the dressing-room doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the corridor door occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the door, the window and the doorway of the bedroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🚪 ODA SON KARESİ (G66′ · YATAK ODASI) — S65'in hedefi · kapı saymaz

> YATAK ODASI kamerasının son karesi; sonraki sahne başka istasyondan açılır. Önce bu kare üretilir (odanın
> usta karesi), oda zinciri ondan GERİYE türetilir.

```
Photorealistic documentary photograph — end frame of Scene 65 of 90, the target frame of that shot. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bedroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are smoothed and painted a calm warm greige. The floor is laid with pale oak boards running away from the camera. A wide upholstered greige headboard panel covers the middle of the far wall. Floor-length linen curtains hang at the tall window in the right wall. A large soft grey rug lies in front of the headboard. A king-size bed stands centred on the headboard, made up with a thick mattress, white linen and pillows. A walnut bedside table with one small lamp stands at each side of the bed — two tables and two lamps. A long upholstered bench stands across the foot of the bed. A large cream chaise longue stands by the window in the right wall. A slim walnut dressing table with one small upholstered stool stands against the left wall beyond the doorway. Through the doorway in the left wall the old dressing room shows, its sagging shelves dim. A strip of grey protective membrane lies rolled up by the corridor door, a folded stepladder beside it.

SITE / BACKGROUND: The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the dressing room. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bedroom keeps exactly these openings: one corridor door, one tall window and one dressing-room doorway.

THE TIME MOMENT: Twenty past four in the afternoon: the main bedroom is finished: the made bed on its rug, two bedside tables with lamps, the bench, the chaise longue and the dressing table.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 275 degrees, elevation 33 degrees, outside on the right and behind the camera; sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight. Through the glass: a clear afternoon sky with a few white clouds, the light turning warmer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the corridor door the two workers in dark blue shirts and grey trousers lift the rolled membrane onto the low flat cart and wheel it out into the corridor. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A soft sheen on the new floor, a last faint band of dust along one skirting, faint shoe prints near the door, a folded stack of dust sheets, one small offcut forgotten by the wall. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The corridor door, the tall window, the dressing-room doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

---
