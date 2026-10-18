# 🎬 THE_GRAND_REVIVAL — ODA 05 · MUTFAK — DOLAPLAR, ADA, TAŞ TEZGÂH, DÖRT TABURE  (S42–S53 · 12 sahne görseli + oda son kareleri + 12 I2V · 336,0–432,0 sn)

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

## 🎬 SAHNE 42 — SÖKÜM

```
SÜRE: 8,0 s (336,0–344,0)  ·  #43  ·  REJİM: A (10 dk)  ·  SAAT: 12:40→12:50  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G42):**

- ⛔ İSTASYON KESMESİ — YEMEK ODASI → **MUTFAK** (sahip istisnası: oda başına sabit kamera)
- önceki oda sonu (G42′): Masa, on sandalye, büfe, dolap, perde, avize tamam
- bu odanın ilk karesi: Eski alt dolaplar sökülüp servis kapısından çıkarılır
- ışık: 12:30→12:40 (kesmede saat sürer, atlamaz)

**▶ Bu sahnede:** Eski alt dolaplar sökülüp servis kapısından çıkarılır; tesisat duvarı ve kapı açıklıkları değişmez.

### 📸 GÖRSEL PROMPT (G42)

```
Photorealistic documentary photograph — Scene 42 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: Old broken base cabinets and a cracked worktop line the left wall under the window. The walls are stained and cracked. The floor is bare grey screed. A low flat cart stands at the service door.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Twenty to one in the afternoon: the kitchen lies dim and ruined, and through the doorway the finished dining room shows.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 213 degrees, elevation 73 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the left wall the two workers in dark blue shirts and grey trousers pull the old broken base cabinets off the wall and lift them onto a low flat cart at the service door, a pry bar and a drill on the floor. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Dust lying grey over everything, damp stains and grime streaks on the walls, cracked plaster, dead leaves in drifts in the corners, debris heaped along the skirting. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G42 → G43)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the broken cabinets and the cracked worktop from the left wall out through the service door onto the low flat cart.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Piece by piece the old units come off the wall and go out, until the left wall stands stripped to its old pipe stubs and the floor is swept. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 43 — DUVAR VE BOYA

```
SÜRE: 8,0 s (344,0–352,0)  ·  #44  ·  REJİM: A (10 dk)  ·  SAAT: 12:50→13:00  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G43):**

- önceki klibin hedefi = bu klibin ilk karesi: Sol duvar çıplak · kapılar aynı
- ışık: 12:40 → 12:50

**▶ Bu sahnede:** Duvar yüzeyleri onarılıp krem bitiş rengine getirilir.

### 📸 GÖRSEL PROMPT (G43)

```
Photorealistic documentary photograph — Scene 43 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The left wall stands stripped bare to its old pipe stubs. The walls are stained and cracked. The floor is bare grey screed. A trestle workbench and a stepladder stand by the right wall, a low flat cart at the service door.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Ten to one in the afternoon: the left wall stands stripped, and the walls are stained and cracked.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 220 degrees, elevation 72 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: By the right wall the two workers in dark blue shirts and grey trousers set a stepladder and spread plaster over the cracks from a bucket on the low flat cart, rolling soft cream paint behind it. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G43 → G44)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry plaster and paint from the low flat cart to the walls and spread them onto the cracked surfaces, from the right wall round to the left wall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The cracks close and the walls turn an even soft cream wall by wall, and the empty buckets are stacked back on the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 44 — TAŞ ZEMİN

```
SÜRE: 8,0 s (352,0–360,0)  ·  #45  ·  REJİM: A (10 dk)  ·  SAAT: 13:00→13:10  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G44):**

- önceki klibin hedefi = bu klibin ilk karesi: Duvarlar krem · sınırlar aynı
- ışık: 12:50 → 13:00

**▶ Bu sahnede:** Büyük mat taş zemin plakaları döşenir; tezgâh ve ada yerleri boş.

### 📸 GÖRSEL PROMPT (G44)

```
Photorealistic documentary photograph — Scene 44 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The left wall stands stripped bare to its old pipe stubs. The walls are patched and painted a soft cream. The floor is bare grey screed. A trestle workbench and a stepladder stand by the right wall, a low flat cart at the service door.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: One o'clock in the afternoon: the walls are soft cream, and the floor is still bare grey screed.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 226 degrees, elevation 71 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the far wall the two workers in dark blue shirts and grey trousers lift the first large grey-beige stone tiles off a stack on a pallet at the service door and set them on a mortar bed, a low flat cart bringing more. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G44 → G45)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers lay the large matt stone tiles from the stack on the pallet onto a mortar bed, row after row from the far wall towards the camera.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The surface grows towards the camera row by row until the bare screed is covered; the empty pallet goes out through the service door on the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 45 — KİLER DOLAPLARI

```
SÜRE: 8,0 s (360,0–368,0)  ·  #46  ·  REJİM: A (10 dk)  ·  SAAT: 13:10→13:20  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G45):**

- önceki klibin hedefi = bu klibin ilk karesi: Taş zemin · ada yeri boş
- ışık: 13:00 → 13:10

**▶ Bu sahnede:** Yüksek kiler dolabı bankası modül modül uzak duvara yerleştirilir.

### 📸 GÖRSEL PROMPT (G45)

```
Photorealistic documentary photograph — Scene 45 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The left wall stands stripped bare to its old pipe stubs. The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. Grey protective membrane covers the new stone floor, a stepladder by the right wall.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Ten past one in the afternoon: the stone floor is laid, and the far wall between the service door and the doorway is bare.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 231 degrees, elevation 69 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the service door the two workers in dark blue shirts and grey trousers lift the first tall walnut pantry module off the low flat cart and walk it upright to the far wall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G45 → G46)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the tall walnut pantry modules one at a time from the low flat cart at the service door to the far wall and set them side by side.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Module by module the tall walnut bank fills the far wall between the service door and the doorway, each one levelled and fixed to the next. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 46 — ALT DOLAPLAR

```
SÜRE: 8,0 s (368,0–376,0)  ·  #47  ·  REJİM: A (10 dk)  ·  SAAT: 13:20→13:30  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G46):**

- önceki klibin hedefi = bu klibin ilk karesi: Yüksek dolaplar tek duvarda
- ışık: 13:10 → 13:20

**▶ Bu sahnede:** Taş tezgâhlı alt dolap modülleri sol duvar boyunca dizilir; dolap sayısı ve kapak bölümleri sabit kalır.

### 📸 GÖRSEL PROMPT (G46)

```
Photorealistic documentary photograph — Scene 46 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The left wall stands stripped bare to its old pipe stubs. The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway. Grey protective membrane covers the new stone floor, a stepladder by the right wall.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Twenty past one in the afternoon: the walnut pantry bank fills the far wall.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 235 degrees, elevation 68 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the left wall the two workers in dark blue shirts and grey trousers lift the first cream base cabinet off the low flat cart and set it under the window. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G46 → G47)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the cream base cabinets from the low flat cart at the service door to the left wall, set them in a row under the window and lay the pale stone worktop onto them.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Cabinet by cabinet the run grows along the left wall, and the long pale stone worktop is lowered onto it in two pieces and joined. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 47 — ADA GÖVDESİ

```
SÜRE: 8,0 s (376,0–384,0)  ·  #48  ·  REJİM: A (10 dk)  ·  SAAT: 13:30→13:40  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G47):**

- önceki klibin hedefi = bu klibin ilk karesi: Alt dolaplar ve tezgâh sol duvarda
- ışık: 13:20 → 13:30

**▶ Bu sahnede:** Büyük ada gövdesi ortaya getirilir; sonda iki işçi daha katılır, taş tezgâh arabada yanına gelir.

### 📸 GÖRSEL PROMPT (G47)

```
Photorealistic documentary photograph — Scene 47 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway. A run of cream base cabinets with a pale stone worktop lines the left wall under the window. Grey protective membrane covers the new stone floor, a stepladder by the right wall.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Half past one in the afternoon: the base cabinets and worktop line the left wall, and the middle of the floor is bare.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 239 degrees, elevation 66 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the service door the two workers in dark blue shirts and grey trousers lift the long walnut island body off a low flat cart and walk it towards the middle of the floor. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G47 → G48)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the walnut island body from the low flat cart at the service door to the middle of the floor and set it down square to the far wall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They level it and fix it to the floor. Late in the shot two more workers in the same clothes help wheel the thick pale stone top in on a low flat cart, lying flat on a padded board with lifting slings under it, and stop beside the island. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 48 — TAŞ TEZGÂH · PİLOT

```
SÜRE: 8,0 s (384,0–392,0)  ·  #49  ·  REJİM: G (gerçek zaman)  ·  SAAT: 13:40→13:40  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G48):**

- önceki klibin hedefi = bu klibin ilk karesi: Ada gövdesi ortada, üstü boş · taş tezgâh arabada yanında
- ışık: 13:30 → 13:40

**▶ Bu sahnede:** GERÇEK ZAMAN · dört işçi kalın taş tezgâhı sapanlarla gövdeye indirir. PİLOT.

### 📸 GÖRSEL PROMPT (G48)

```
Photorealistic documentary photograph — Scene 48 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway. A run of cream base cabinets with a pale stone worktop lines the left wall under the window. A long walnut island body stands in the middle of the floor, its top bare. The thick pale stone top lies flat on a padded board on a low flat cart beside the island, lifting slings under it. Grey protective membrane runs from the service door along the walking line, lifting slings coiled on it.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Twenty to two in the afternoon: the thick stone top lies on a low flat cart beside the bare walnut island.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 243 degrees, elevation 64 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the workers carry at their real pace and the light holds still; nothing is accelerated.

ACTIVITY: Beside the island four workers in the same dark blue shirts and grey trousers lift the thick pale stone top off the low flat cart on four lifting slings, one at each corner, and raise it slowly above the island. Every person is seen from the side or from behind, back to the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stone top hangs from a lifting sling at each corner, each sling held by a worker, its weight on their arms and backs. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G48 → G49)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: Four workers lift the thick stone top from the low flat cart on four slings and lower it onto the walnut island body.

Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame the stone is already rising off the cart; the four shuffle it over the island, line up its square edge with the body and lower it until it sits flat, then slip the slings out from under it and step back. Through the glass the few small clouds hold still.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 49 — TAŞ PANELLER

```
SÜRE: 8,0 s (392,0–400,0)  ·  #50  ·  REJİM: A (10 dk)  ·  SAAT: 13:40→13:50  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G49):**

- önceki klibin hedefi = bu klibin ilk karesi: Ada tek parça; tezgâh kenarı, kalınlığı, boyu sabit
- ışık: 13:40 → 13:40

**▶ Bu sahnede:** Tezgâh arası taş paneller sol duvara takılır.

### 📸 GÖRSEL PROMPT (G49)

```
Photorealistic documentary photograph — Scene 49 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway. A run of cream base cabinets with a pale stone worktop lines the left wall under the window. A long walnut island stands in the middle of the floor under a thick pale stone top with a square edge. Grey protective membrane runs from the service door along the walking line, lifting slings coiled on it.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Twenty to two in the afternoon: the stone-topped island stands in the middle of the floor.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 243 degrees, elevation 64 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the left wall the two workers in dark blue shirts and grey trousers lift the first pale stone panel off a stack on the low flat cart and set it on the wall between the worktop and the window. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G49 → G50)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the pale stone panels from the stack on the low flat cart to the left wall and fix them onto the wall between the worktop and the window.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Panel by panel the pale stone spreads along the wall above the worktop, its soft veins lining up. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 50 — BUZDOLABI

```
SÜRE: 8,0 s (400,0–408,0)  ·  #51  ·  REJİM: A (10 dk)  ·  SAAT: 13:50→14:00  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G50):**

- önceki klibin hedefi = bu klibin ilk karesi: Taş paneller yerinde
- ışık: 13:40 → 13:50

**▶ Bu sahnede:** Büyük buzdolabı sağ duvardaki boşluğa yerleştirilir.

### 📸 GÖRSEL PROMPT (G50)

```
Photorealistic documentary photograph — Scene 50 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway. A run of cream base cabinets with a pale stone worktop lines the left wall under the window. A long walnut island stands in the middle of the floor under a thick pale stone top with a square edge. Pale stone panels cover the wall between the worktop and the window. Grey protective membrane runs from the service door along the walking line, a low flat cart at the door.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Ten to two in the afternoon: pale stone panels line the wall above the worktop, and the niche in the right wall is empty.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 246 degrees, elevation 62 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the service door the two workers in dark blue shirts and grey trousers lift the tall built-in refrigerator off the low flat cart and walk it upright towards the niche in the right wall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G50 → G51)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the tall refrigerator from the low flat cart at the service door to the niche in the right wall and slide it into the niche.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They ease it in, level it and fit its plain cream panel doors so they line up with the cabinets. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 51 — ÇİFT FIRIN

```
SÜRE: 8,0 s (408,0–416,0)  ·  #52  ·  REJİM: A (10 dk)  ·  SAAT: 14:00→14:10  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G51):**

- önceki klibin hedefi = bu klibin ilk karesi: Buzdolabı yerinde · ön yüzü dolap çizgisinde
- ışık: 13:50 → 14:00

**▶ Bu sahnede:** Çift fırın ünitesi ayrılmış dolap yuvasına yerleştirilir; yeni dolap oluşmaz.

### 📸 GÖRSEL PROMPT (G51)

```
Photorealistic documentary photograph — Scene 51 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway. A run of cream base cabinets with a pale stone worktop lines the left wall under the window. A long walnut island stands in the middle of the floor under a thick pale stone top with a square edge. Pale stone panels cover the wall between the worktop and the window. A tall built-in refrigerator with plain cream panel doors stands in the niche in the right wall. Grey protective membrane runs from the service door along the walking line, a low flat cart at the door.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Two o'clock in the afternoon: the refrigerator stands in its niche.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 249 degrees, elevation 61 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the service door the two workers in dark blue shirts and grey trousers lift the double wall oven off the low flat cart and carry it towards the tall cabinet beside the refrigerator. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G51 → G52)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the double oven from the low flat cart at the service door to the tall cabinet beside the refrigerator and slide it into its slot.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. It slides home and is fixed flush with the cabinet front, and the empty cart goes back out of the service door. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 52 — İKİ TABURE

```
SÜRE: 8,0 s (416,0–424,0)  ·  #53  ·  REJİM: A (10 dk)  ·  SAAT: 14:10→14:20  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G52):**

- önceki klibin hedefi = bu klibin ilk karesi: Tek fırın ünitesi
- ışık: 14:00 → 14:10

**▶ Bu sahnede:** İlk iki bar taburesi adanın oturma kenarına; tam iki.

### 📸 GÖRSEL PROMPT (G52)

```
Photorealistic documentary photograph — Scene 52 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway. A run of cream base cabinets with a pale stone worktop lines the left wall under the window. A long walnut island stands in the middle of the floor under a thick pale stone top with a square edge. Pale stone panels cover the wall between the worktop and the window. A tall built-in refrigerator with plain cream panel doors stands in the niche in the right wall. A double wall oven with a plain dark front sits in a tall cabinet beside the refrigerator. Grey protective membrane runs from the service door along the walking line, a low flat cart at the door.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Ten past two in the afternoon: the double oven sits in its cabinet, and the near side of the island is empty.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 252 degrees, elevation 59 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the service door the two workers in dark blue shirts and grey trousers lift the first walnut bar stool off the low flat cart and carry it to the near side of the island. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G52 → G53)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry two walnut bar stools from the low flat cart at the service door to the near side of the island and set them down.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. One stool each, set down evenly spaced, so exactly two stools stand at the island. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 53 — DÖRT TABURE · KAHVE

```
SÜRE: 8,0 s (424,0–432,0)  ·  #54  ·  REJİM: A (10 dk)  ·  SAAT: 14:20→14:30  ·  İSTASYON: K · MUTFAK
```

**🔄 Önceki sahneye göre değişen (→ G53):**

- önceki klibin hedefi = bu klibin ilk karesi: Tam iki tabure
- ışık: 14:10 → 14:20

**▶ Bu sahnede:** İkinci tabure çifti gelir; sonda tek kahve makinesi tezgâha konur. Mutfak tamam.

### 📸 GÖRSEL PROMPT (G53)

```
Photorealistic documentary photograph — Scene 53 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway. A run of cream base cabinets with a pale stone worktop lines the left wall under the window. A long walnut island stands in the middle of the floor under a thick pale stone top with a square edge. Pale stone panels cover the wall between the worktop and the window. A tall built-in refrigerator with plain cream panel doors stands in the niche in the right wall. A double wall oven with a plain dark front sits in a tall cabinet beside the refrigerator. Two walnut bar stools stand at the near side of the island. Grey protective membrane runs from the service door along the walking line, a low flat cart at the door.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Twenty past two in the afternoon: two stools stand at the island.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 254 degrees, elevation 57 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the service door the two workers in dark blue shirts and grey trousers lift two more walnut bar stools off the low flat cart, a boxed coffee machine waiting beside them. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G53 → G54′)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry two more bar stools from the low flat cart to the island, then lift the coffee machine from its box onto the worktop.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The four stools stand in an even row; the coffee machine is set on the worktop by the window. The workers roll up the membrane and wheel the cart out of the service door. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The service door, the dining-room doorway, the wide window and the far corners of the kitchen stay exactly where they are, at exactly the same size and shape, for the whole shot; the dining-room doorway occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the doors and the window of the kitchen are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🚪 ODA SON KARESİ (G54′ · MUTFAK) — S53'in hedefi · kapı saymaz

> MUTFAK kamerasının son karesi; sonraki sahne başka istasyondan açılır. Önce bu kare üretilir (odanın
> usta karesi), oda zinciri ondan GERİYE türetilir.

```
Photorealistic documentary photograph — end frame of Scene 53 of 90, the target frame of that shot. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the kitchen.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are patched and painted a soft cream. The floor is laid with large matt grey-beige stone tiles. A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway. A run of cream base cabinets with a pale stone worktop lines the left wall under the window. A long walnut island stands in the middle of the floor under a thick pale stone top with a square edge. Pale stone panels cover the wall between the worktop and the window. A tall built-in refrigerator with plain cream panel doors stands in the niche in the right wall. A double wall oven with a plain dark front sits in a tall cabinet beside the refrigerator. Four walnut bar stools stand in a row at the near side of the island, and one coffee machine stands on the worktop. A strip of grey protective membrane lies rolled up by the service door, a folded stepladder beside it.

SITE / BACKGROUND: The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway leads through to the dining room, and through it the finished dining room shows, the walnut table and its chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto the side garden; the right wall runs plain, with one tall niche for a refrigerator. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window.

THE TIME MOMENT: Half past two in the afternoon: the kitchen is finished: the pantry bank, the base run and worktop with its stone panels, the refrigerator and oven, and the stone-topped island with four stools.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans about 329 to 504 pixels. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 256 degrees, elevation 55 degrees, outside on the left and behind the camera; sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight. Through the glass: a deep blue midday sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the service door the two workers in dark blue shirts and grey trousers lift the rolled membrane onto the low flat cart and wheel it out into the side garden. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A soft sheen on the new floor, a last faint band of dust along one skirting, faint shoe prints near the door, a folded stack of dust sheets, one small offcut forgotten by the wall. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one service door, one doorway and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

---
