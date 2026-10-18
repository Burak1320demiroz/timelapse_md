# 🎬 THE_GRAND_REVIVAL — ODA 04 · YEMEK ODASI — ON KİŞİLİK MASA, 2 → 6 → 10 SANDALYE  (S30–S41 · 12 sahne görseli + oda son kareleri + 12 I2V · 240,0–336,0 sn)

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

## 🎬 SAHNE 30 — YEMEK ODASI BOŞALIR

```
SÜRE: 8,0 s (240,0–248,0)  ·  #31  ·  REJİM: A (10 dk)  ·  SAAT: 10:50→11:00  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G30):**

- ⛔ İSTASYON KESMESİ — SALON → **YEMEK ODASI** (sahip istisnası: oda başına sabit kamera)
- önceki oda sonu (G30′): Salon tamam — ilk iç mekân zirvesi · BÖLÜM 1 sonu
- bu odanın ilk karesi: Eski masa ve sandalyeler cam kapılardan verandadaki arabaya taşınır
- ışık: 10:40→10:50 (kesmede saat sürer, atlamaz)

**▶ Bu sahnede:** Eski masa ve sandalyeler cam kapılardan verandadaki arabaya taşınır; oda boşalır.

### 📸 GÖRSEL PROMPT (G30)

```
Photorealistic documentary photograph — Scene 30 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: An old dark dining table, three broken chairs and heaps of debris stand on the floor. The walls are stained grey-white. The floor is bare grey screed. A bare ceiling hook marks the middle of the ceiling. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A low flat cart stands outside the open middle glass door.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Ten to eleven in the morning: the dining room lies dim and ruined, and beyond its glass doors the old veranda lies under weeds.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 129 degrees, elevation 69 degrees, outside on the left and behind the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the open glass doors the two workers in dark blue shirts and grey trousers lift the old dark table onto a low flat cart outside on the veranda and carry the broken chairs out after it. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Dust lying grey over everything, damp stains and grime streaks on the walls, cracked plaster, dead leaves in drifts in the corners, debris heaped along the skirting. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G30 → G31)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the old table, the broken chairs and the debris from the floor out through the open glass doors onto the low flat cart on the veranda.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Load after load leaves through the middle glass door, until the room lies bare and swept; the cart is wheeled away along the veranda and brought back empty. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 31 — GREJ

```
SÜRE: 8,0 s (248,0–256,0)  ·  #32  ·  REJİM: A (10 dk)  ·  SAAT: 11:00→11:10  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G31):**

- önceki klibin hedefi = bu klibin ilk karesi: Oda boş · mutfak kapısından harap mutfak, camlardan harap veranda
- ışık: 10:50 → 11:00

**▶ Bu sahnede:** Duvarlar sıcak greje boyanır; tavan ve pencere geometrisi korunur.

### 📸 GÖRSEL PROMPT (G31)

```
Photorealistic documentary photograph — Scene 31 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are stained grey-white. The floor is bare grey screed. A bare ceiling hook marks the middle of the ceiling. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A folded stepladder stands by the left wall, a low flat cart at the glass doors.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Eleven o'clock in the morning: the room is empty, its walls stained grey-white.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 134 degrees, elevation 71 degrees, outside on the left and behind the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: By the left wall the two workers in dark blue shirts and grey trousers set a stepladder and roll warm greige paint from tins on the low flat cart onto the stained walls. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G31 → G32)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers roll warm greige paint from the tins on the low flat cart onto the walls, from the left wall around the windows to the right wall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The stains go under an even warm greige wall by wall, and the empty tins are stacked back on the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 32 — TAŞ ZEMİN

```
SÜRE: 8,0 s (256,0–264,0)  ·  #33  ·  REJİM: A (10 dk)  ·  SAAT: 11:10→11:20  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G32):**

- önceki klibin hedefi = bu klibin ilk karesi: Duvarlar grej
- ışık: 11:00 → 11:10

**▶ Bu sahnede:** Mat açık taş zemin plakaları cam kapılardan kameraya doğru döşenir.

### 📸 GÖRSEL PROMPT (G32)

```
Photorealistic documentary photograph — Scene 32 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are painted a warm greige. The floor is bare grey screed. A bare ceiling hook marks the middle of the ceiling. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A folded stepladder stands by the left wall, a low flat cart at the glass doors.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Ten past eleven in the morning: the walls are warm greige, and the floor is still bare grey screed.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 140 degrees, elevation 72 degrees, outside on the left and behind the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the far end by the glass doors the two workers in dark blue shirts and grey trousers lift the first large pale stone tiles off a stack on a pallet and set them on a mortar bed, a low flat cart bringing more. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G32 → G33)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers lay the large matt stone tiles from the stack on the pallet onto a mortar bed, row after row from the glass doors towards the camera.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The pale surface grows towards the camera row by row, each tile set and tapped level, until the bare screed is covered; the empty pallet goes out on the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 33 — AVİZE

```
SÜRE: 8,0 s (264,0–272,0)  ·  #34  ·  REJİM: A (10 dk)  ·  SAAT: 11:20→11:30  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G33):**

- önceki klibin hedefi = bu klibin ilk karesi: Taş zemin · desen bundan sonra aynı
- ışık: 11:10 → 11:20

**▶ Bu sahnede:** Bronz avize asılır; sonda iki işçi daha katılır, ceviz masa orta cam kapıdan gelir.

### 📸 GÖRSEL PROMPT (G33)

```
Photorealistic documentary photograph — Scene 33 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A bare ceiling hook marks the middle of the ceiling. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane covers the new stone floor, a stepladder under the bare hook.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Twenty past eleven in the morning: the stone floor is laid, and a bare hook marks the middle of the ceiling.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 147 degrees, elevation 73 degrees, outside on the left and behind the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Under the bare hook the two workers in dark blue shirts and grey trousers set a tall stepladder and lift the long linear bronze chandelier out of its long crate on the low flat cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G33 → G34)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the long bronze chandelier from its crate on the low flat cart up the stepladder and hang it from the ceiling hook on two chains along the length of the room.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The chandelier rises the last metre and hangs level and low over the middle of the room, unlit. Late in the shot two more workers in the same clothes help bring the long walnut table in through the middle glass door on a low flat cart and stop just inside the door. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 34 — MASA

```
SÜRE: 8,0 s (272,0–280,0)  ·  #35  ·  REJİM: G (gerçek zaman)  ·  SAAT: 11:30→11:30  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G34):**

- önceki klibin hedefi = bu klibin ilk karesi: Avize merkez ekseninde · masa arabada, kapının içinde
- ışık: 11:20 → 11:30

**▶ Bu sahnede:** GERÇEK ZAMAN · dört işçi on kişilik ceviz masayı avizenin altına koyar.

### 📸 GÖRSEL PROMPT (G34)

```
Photorealistic documentary photograph — Scene 34 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. The long walnut table waits on a low flat cart just inside the middle glass door. Grey protective membrane covers the new stone floor, a stepladder under the bare hook.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Half past eleven in the morning: the long walnut table waits on a low flat cart just inside the middle glass door.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 154 degrees, elevation 74 degrees, outside on the left and behind the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the workers carry at their real pace and the light holds still; nothing is accelerated.

ACTIVITY: Just inside the glass door four workers in the same dark blue shirts and grey trousers lift the long walnut table off the low flat cart, two at each end, and walk it slowly towards the chandelier. Every person is seen from the side or from behind, back to the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. The load is gripped in the workers' hands, its weight on their arms and backs, its underside clear of the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G34 → G35)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: Four workers lift the long walnut dining table from the low flat cart at the glass door, carry it to the middle of the room and set it down under the chandelier, its length pointing at the camera.

Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame the table is already rising off the cart; the four carry it in short careful steps, line it up under the chandelier and lower it until all its legs stand on the stone, then step back to the sides. Through the glass the few small clouds hold still.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 35 — BAŞ SANDALYELERİ

```
SÜRE: 8,0 s (280,0–288,0)  ·  #36  ·  REJİM: A (10 dk)  ·  SAAT: 11:30→11:40  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G35):**

- önceki klibin hedefi = bu klibin ilk karesi: Tek masa, tek sabit konum
- ışık: 11:30 → 11:30

**▶ Bu sahnede:** İki baş sandalyesi sırayla masanın iki ucuna; toplam iki.

### 📸 GÖRSEL PROMPT (G35)

```
Photorealistic documentary photograph — Scene 35 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit. A long walnut dining table for ten stands under the chandelier, its length pointing at the camera. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the glass doors along the walking line, lifting slings coiled on it.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Half past eleven in the morning: the walnut table stands under the chandelier.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 154 degrees, elevation 74 degrees, outside on the left and behind the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the glass doors the two workers in dark blue shirts and grey trousers lift the first upholstered head chair off the low flat cart and carry it towards the far end of the table. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G35 → G36)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the two head chairs one at a time from the low flat cart at the glass doors to the two ends of the table.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. One chair per trip: the first goes to the far end, the cart is wheeled back, and the second goes to the near end, so exactly two chairs stand at the table. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 36 — BÜFE

```
SÜRE: 8,0 s (288,0–296,0)  ·  #37  ·  REJİM: A (10 dk)  ·  SAAT: 11:40→11:50  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G36):**

- önceki klibin hedefi = bu klibin ilk karesi: Toplam iki sandalye
- ışık: 11:30 → 11:40

**▶ Bu sahnede:** Uzun servis büfesi sağ duvara; iki sandalye yerinde, geçiş açık.

### 📸 GÖRSEL PROMPT (G36)

```
Photorealistic documentary photograph — Scene 36 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit. A long walnut dining table for ten stands under the chandelier, its length pointing at the camera. Two upholstered dining chairs stand at the table, one at each end. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the glass doors along the walking line, a low flat cart at the doors.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Twenty to twelve in the morning: two chairs stand at the ends of the table.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 162 degrees, elevation 75 degrees, outside on the left and behind the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the glass doors the two workers in dark blue shirts and grey trousers lift a long low walnut sideboard off the low flat cart and carry it towards the right wall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G36 → G37)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the long walnut sideboard from the low flat cart at the glass doors to the right wall and set it down against the wall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They lower it and square it to the wall so the walkway beside the table stays open, and the two chairs stay where they are. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 37 — SERGİ DOLABI

```
SÜRE: 8,0 s (296,0–304,0)  ·  #38  ·  REJİM: A (10 dk)  ·  SAAT: 11:50→12:00  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G37):**

- önceki klibin hedefi = bu klibin ilk karesi: Büfe sağ duvarda · iki sandalye aynı yerde
- ışık: 11:40 → 11:50

**▶ Bu sahnede:** Ahşap çerçeveli yüksek sergileme dolabı büfenin ötesine; masa, büfe, iki sandalye korunur.

### 📸 GÖRSEL PROMPT (G37)

```
Photorealistic documentary photograph — Scene 37 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit. A long walnut dining table for ten stands under the chandelier, its length pointing at the camera. Two upholstered dining chairs stand at the table, one at each end. A long low walnut sideboard stands against the right wall. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the glass doors along the walking line, a low flat cart at the doors.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Ten to twelve in the morning: the sideboard stands against the right wall.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 171 degrees, elevation 75 degrees, outside on the left and behind the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the glass doors the two workers in dark blue shirts and grey trousers lift a tall walnut display cabinet with clear glass doors off the low flat cart and walk it upright towards the right wall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G37 → G38)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the tall display cabinet from the low flat cart at the glass doors to the right wall and stand it beyond the sideboard.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They walk it upright in small steps and set it plumb against the wall; the table, the sideboard and the two chairs stay unchanged. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 38 — DÖRT SANDALYE · SAYIM PİLOTU

```
SÜRE: 8,0 s (304,0–312,0)  ·  #39  ·  REJİM: A (10 dk)  ·  SAAT: 12:00→12:10  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G38):**

- önceki klibin hedefi = bu klibin ilk karesi: Tek yeni dolap
- ışık: 11:50 → 12:00

**▶ Bu sahnede:** Dört yan sandalye tek tek sol yana; toplam altı. SAYIM PİLOTU.

### 📸 GÖRSEL PROMPT (G38)

```
Photorealistic documentary photograph — Scene 38 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit. A long walnut dining table for ten stands under the chandelier, its length pointing at the camera. Two upholstered dining chairs stand at the table, one at each end. A long low walnut sideboard stands against the right wall. A tall walnut display cabinet with clear glass doors stands against the right wall beyond the sideboard. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the glass doors along the walking line, a low flat cart at the doors.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Noon: the display cabinet stands beyond the sideboard, and two chairs stand at the ends of the table.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 180 degrees, elevation 75 degrees, outside on the left and behind the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the glass doors the two workers in dark blue shirts and grey trousers lift the first of four side chairs off a stack of chairs on the low flat cart and carry it towards the left side of the table. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G38 → G39)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry four side chairs one at a time from the stack on the low flat cart at the glass doors to the left side of the table and set them in a row.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. One chair per trip: the stack on the cart shrinks by one each time and the row along the left side grows to four, evenly spaced, while the head chairs at the two ends stay where they are, so six chairs stand at the table. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 39 — PERDELER

```
SÜRE: 8,0 s (312,0–320,0)  ·  #40  ·  REJİM: A (10 dk)  ·  SAAT: 12:10→12:20  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G39):**

- önceki klibin hedefi = bu klibin ilk karesi: Toplam altı sandalye: iki baş + solda dört
- ışık: 12:00 → 12:10

**▶ Bu sahnede:** Tavandan yere perdeler iki pencereye asılır; altı sandalye değişmez.

### 📸 GÖRSEL PROMPT (G39)

```
Photorealistic documentary photograph — Scene 39 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit. A long walnut dining table for ten stands under the chandelier, its length pointing at the camera. Six upholstered dining chairs stand at the table: one at each end and four along the left side. A long low walnut sideboard stands against the right wall. A tall walnut display cabinet with clear glass doors stands against the right wall beyond the sideboard. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the glass doors along the walking line, a low flat cart at the doors.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Ten past twelve in the afternoon: six chairs stand at the table, four along its left side.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 189 degrees, elevation 75 degrees, outside on the left and ahead of the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: By the left wall the two workers in dark blue shirts and grey trousers set a stepladder under the first window and lift a bundle of folded linen curtains off the low flat cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G39 → G40)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the folded linen curtains from the low flat cart to the two tall windows in the left wall and hang them from the rods, ceiling to floor.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Window by window the linen falls in soft folds to the floor; the six chairs and the window openings stay as they were. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 40 — SON DÖRT SANDALYE

```
SÜRE: 8,0 s (320,0–328,0)  ·  #41  ·  REJİM: A (10 dk)  ·  SAAT: 12:20→12:30  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G40):**

- önceki klibin hedefi = bu klibin ilk karesi: Perdeler asılı · altı sandalye aynı
- ışık: 12:10 → 12:20

**▶ Bu sahnede:** Kalan dört sandalye tek tek sağ yana; toplam on.

### 📸 GÖRSEL PROMPT (G40)

```
Photorealistic documentary photograph — Scene 40 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit. A long walnut dining table for ten stands under the chandelier, its length pointing at the camera. Six upholstered dining chairs stand at the table: one at each end and four along the left side. A long low walnut sideboard stands against the right wall. A tall walnut display cabinet with clear glass doors stands against the right wall beyond the sideboard. Floor-length linen curtains hang at the two tall windows in the left wall. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the glass doors along the walking line, a low flat cart at the doors.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Twenty past twelve in the afternoon: curtains hang at the two windows, and six chairs stand at the table.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 198 degrees, elevation 75 degrees, outside on the left and ahead of the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the glass doors the two workers in dark blue shirts and grey trousers lift the first of the last four chairs off the stack on the low flat cart and carry it towards the right side of the table. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G40 → G41)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the last four side chairs one at a time from the stack on the low flat cart at the glass doors to the right side of the table and set them in a row.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. One chair per trip, the stack on the cart shrinks to nothing and the row along the right side grows to four, matching the left side, so ten chairs stand at the table. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 41 — TABLO VE ÇİÇEK

```
SÜRE: 8,0 s (328,0–336,0)  ·  #42  ·  REJİM: A (10 dk)  ·  SAAT: 12:30→12:40  ·  İSTASYON: D · YEMEK ODASI
```

**🔄 Önceki sahneye göre değişen (→ G41):**

- önceki klibin hedefi = bu klibin ilk karesi: Toplam on sandalye: iki baş + iki yanda dörder
- ışık: 12:20 → 12:30

**▶ Bu sahnede:** Büfenin üstüne büyük tablo; sonda masaya tek çiçek aranjmanı. Oda tamam.

### 📸 GÖRSEL PROMPT (G41)

```
Photorealistic documentary photograph — Scene 41 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit. A long walnut dining table for ten stands under the chandelier, its length pointing at the camera. Ten upholstered dining chairs stand at the table: one at each end and four along each side. A long low walnut sideboard stands against the right wall. A tall walnut display cabinet with clear glass doors stands against the right wall beyond the sideboard. Floor-length linen curtains hang at the two tall windows in the left wall. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the glass doors along the walking line, a low flat cart at the doors.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Half past twelve in the afternoon: ten chairs stand at the table.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 206 degrees, elevation 74 degrees, outside on the left and ahead of the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the right wall the two workers in dark blue shirts and grey trousers lift a large framed painting off the low flat cart and carry it towards the sideboard, a low flower arrangement waiting in a box on the cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G41 → G42′)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the framed painting from the low flat cart to the right wall and hang it above the sideboard, then set the flower arrangement onto the middle of the table.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The painting goes up level on two hooks; one low arrangement of white flowers is set in the middle of the table. The workers roll up the membrane and wheel the cart out through the glass doors. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the row of three glass doors occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the glass doors, the windows and the doorway of the dining room are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🚪 ODA SON KARESİ (G42′ · YEMEK ODASI) — S41'in hedefi · kapı saymaz

> YEMEK ODASI kamerasının son karesi; sonraki sahne başka istasyondan açılır. Önce bu kare üretilir (odanın
> usta karesi), oda zinciri ondan GERİYE türetilir.

```
Photorealistic documentary photograph — end frame of Scene 41 of 90, the target frame of that shot. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the dining room.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm greige. The floor is laid with large matt pale stone tiles. A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit. A long walnut dining table for ten stands under the chandelier, its length pointing at the camera. Ten upholstered dining chairs stand at the table: one at each end and four along each side. A long low walnut sideboard stands against the right wall. A tall walnut display cabinet with clear glass doors stands against the right wall beyond the sideboard. Floor-length linen curtains hang at the two tall windows in the left wall. A large framed painting hangs above the sideboard, and one low flower arrangement stands in the middle of the table. Through the kitchen doorway the old kitchen shows, stripped and dim. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A strip of grey protective membrane lies rolled up by the glass doors, a folded stepladder beside it.

SITE / BACKGROUND: The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads through to the kitchen. The right wall runs plain from end to end. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The dining room keeps exactly these openings: three glass doors, two tall windows and one kitchen doorway.

THE TIME MOMENT: Twenty to one in the afternoon: the dining room is finished: the walnut table with ten chairs under the bronze chandelier, the sideboard with its painting, the display cabinet and the linen curtains.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 213 degrees, elevation 73 degrees, outside on the left and ahead of the camera; high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Outside the glass doors the two workers in dark blue shirts and grey trousers lift the rolled membrane onto the low flat cart and wheel it away along the veranda. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A soft sheen on the new floor, a last faint band of dust along one skirting, faint shoe prints near the door, a folded stack of dust sheets, one small offcut forgotten by the wall. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, two windows and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

---
