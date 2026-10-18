# 🎬 THE_GRAND_REVIVAL — ODA 08 · BANYO — TAŞ DUVARLAR, ÇİFT LAVABO, BAĞIMSIZ KÜVET  (S73–S79 · 7 sahne görseli + oda son kareleri + 7 I2V · 584,0–640,0 sn)

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

## 🎬 SAHNE 73 — MOLOZ ÇIKAR

```
SÜRE: 8,0 s (584,0–592,0)  ·  #74  ·  REJİM: A (10 dk)  ·  SAAT: 17:30→17:40  ·  İSTASYON: B · BANYO
```

**🔄 Önceki sahneye göre değişen (→ G73):**

- ⛔ İSTASYON KESMESİ — GİYİNME ODASI → **BANYO** (sahip istisnası: oda başına sabit kamera)
- önceki oda sonu (G73′): Bank ve ada ayrı · raflarda sabit sayıda grup
- bu odanın ilk karesi: Önceden boşaltılmış banyoda kalan moloz çıkarılır
- ışık: 17:20→17:30 (kesmede saat sürer, atlamaz)

**▶ Bu sahnede:** Önceden boşaltılmış banyoda kalan moloz çıkarılır; küvet ve dolap yerleri boş, duş nişi yerinde.

### 📸 GÖRSEL PROMPT (G73)

```
Photorealistic documentary photograph — Scene 73 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bathroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BATH STATION — fixed tripod against the north wall of the main bathroom, lens 1.5 metres above the floor, 6.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: Broken old tiles and rubble lie heaped on the floor. The walls are bare grey plaster with old stains. The floor is bare grey screed. A low flat cart stands in the doorway.

SITE / BACKGROUND: The main bathroom of the villa, six metres square, with a flat ceiling. In the middle of the far wall one wide window looks onto the garden. In the left wall a tall open shower niche is set into the wall. Near the far end of the right wall a doorway leads through to the dressing room, and through it the finished dressing room shows. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bathroom keeps exactly these openings: one wide window, one shower niche and one doorway.

THE TIME MOMENT: Half past five in the evening: the main bathroom lies stripped, broken old tiles and rubble heaped on its floor.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The window in the far wall spans about 512 pixels of frame width at about 704 to 1216 pixels from the left, and keeps that width in every frame. Its sill sits at about thirty-eight percent and its head at about eighty-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 285 degrees, elevation 20 degrees, outside on the right and behind the camera; soft warm evening daylight fills the room from the wide window, and the view through it is bright and golden. Through the glass: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the middle of the floor the two workers in dark blue shirts and grey trousers shovel the rubble into buckets and lift the full buckets onto a low flat cart in the doorway. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Dust lying grey over everything, damp stains and grime streaks on the walls, cracked plaster, dead leaves in drifts in the corners, debris heaped along the skirting. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide window, the shower niche, the doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bathroom keeps its one window, one niche and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G73 → G74)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the rubble in buckets from the floor out through the doorway onto the low flat cart.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Bucket after bucket the heaps go out until the floor lies bare and swept. Through the window the thin clouds drift slowly and turn warmer, and the light in the room deepens towards gold.

The camera does not move at any point. The framing is identical in the first and last frame. The wide window, the shower niche, the doorway and the far corners of the bathroom stay exactly where they are, at exactly the same size and shape, for the whole shot; the window occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the window, the niche and the doorway of the bathroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 74 — TAŞ DUVARLAR

```
SÜRE: 8,0 s (592,0–600,0)  ·  #75  ·  REJİM: A (10 dk)  ·  SAAT: 17:40→17:50  ·  İSTASYON: B · BANYO
```

**🔄 Önceki sahneye göre değişen (→ G74):**

- önceki klibin hedefi = bu klibin ilk karesi: Zemin temiz · duş nişi yerinde
- ışık: 17:30 → 17:40

**▶ Bu sahnede:** Büyük taş duvar plakaları monte edilir; damarlar ve duş nişi sabitlenir.

### 📸 GÖRSEL PROMPT (G74)

```
Photorealistic documentary photograph — Scene 74 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bathroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BATH STATION — fixed tripod against the north wall of the main bathroom, lens 1.5 metres above the floor, 6.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The floor is cleared and swept. The walls are bare grey plaster with old stains. The floor is bare grey screed. A folded stepladder stands by the left wall, a low flat cart in the doorway.

SITE / BACKGROUND: The main bathroom of the villa, six metres square, with a flat ceiling. In the middle of the far wall one wide window looks onto the garden. In the left wall a tall open shower niche is set into the wall. Near the far end of the right wall a doorway leads through to the dressing room, and through it the finished dressing room shows. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bathroom keeps exactly these openings: one wide window, one shower niche and one doorway.

THE TIME MOMENT: Twenty to six in the evening: the bathroom is empty, its walls bare grey plaster.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The window in the far wall spans about 512 pixels of frame width at about 704 to 1216 pixels from the left, and keeps that width in every frame. Its sill sits at about thirty-eight percent and its head at about eighty-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 286 degrees, elevation 18 degrees, outside on the right and behind the camera; soft warm evening daylight fills the room from the wide window, and the view through it is bright and golden. Through the glass: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the far wall the two workers in dark blue shirts and grey trousers lift the first large pale stone slab off a stack on the low flat cart and set it against the wall beside the window, a trestle workbench by the left wall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide window, the shower niche, the doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bathroom keeps its one window, one niche and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G74 → G75)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the large pale stone slabs from the stack on the low flat cart to the walls and fix them onto the plaster, from the far wall round to the side walls.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Slab by slab the pale veined stone climbs the walls to the ceiling, around the window and into the shower niche, its soft grey veins lining up. Through the window the thin clouds drift slowly and turn warmer, and the light in the room deepens towards gold.

The camera does not move at any point. The framing is identical in the first and last frame. The wide window, the shower niche, the doorway and the far corners of the bathroom stay exactly where they are, at exactly the same size and shape, for the whole shot; the window occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the window, the niche and the doorway of the bathroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 75 — TAŞ ZEMİN

```
SÜRE: 8,0 s (600,0–608,0)  ·  #76  ·  REJİM: A (10 dk)  ·  SAAT: 17:50→18:00  ·  İSTASYON: B · BANYO
```

**🔄 Önceki sahneye göre değişen (→ G75):**

- önceki klibin hedefi = bu klibin ilk karesi: Duvarlar taş · damarlar sabit
- ışık: 17:40 → 17:50

**▶ Bu sahnede:** Mat taş zemin döşenir; yön ve derz çizgileri sabit kalır.

### 📸 GÖRSEL PROMPT (G75)

```
Photorealistic documentary photograph — Scene 75 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bathroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BATH STATION — fixed tripod against the north wall of the main bathroom, lens 1.5 metres above the floor, 6.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The floor is cleared and swept. Large pale stone slabs with soft grey veins clad the walls up to the ceiling. The floor is bare grey screed. A trestle workbench with stone offcuts stands by the left wall, a stepladder beside it.

SITE / BACKGROUND: The main bathroom of the villa, six metres square, with a flat ceiling. In the middle of the far wall one wide window looks onto the garden. In the left wall a tall open shower niche is set into the wall. Near the far end of the right wall a doorway leads through to the dressing room, and through it the finished dressing room shows. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bathroom keeps exactly these openings: one wide window, one shower niche and one doorway.

THE TIME MOMENT: Ten to six in the evening: pale stone clads the walls, and the floor is still bare grey screed.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The window in the far wall spans about 512 pixels of frame width at about 704 to 1216 pixels from the left, and keeps that width in every frame. Its sill sits at about thirty-eight percent and its head at about eighty-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 287 degrees, elevation 16 degrees, outside on the right and behind the camera; soft warm evening daylight fills the room from the wide window, and the view through it is bright and golden. Through the glass: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the far end the two workers in dark blue shirts and grey trousers lift the first matt stone tiles off a stack on the low flat cart and set them on a mortar bed. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide window, the shower niche, the doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bathroom keeps its one window, one niche and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G75 → G76)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers lay the matt stone tiles from the stack on the low flat cart onto a mortar bed, row after row from the window towards the camera.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The surface grows towards the camera until the screed is covered, its joints running straight. Through the window the thin clouds drift slowly and turn warmer, and the light in the room deepens towards gold.

The camera does not move at any point. The framing is identical in the first and last frame. The wide window, the shower niche, the doorway and the far corners of the bathroom stay exactly where they are, at exactly the same size and shape, for the whole shot; the window occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the window, the niche and the doorway of the bathroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 76 — ÇİFT LAVABO

```
SÜRE: 8,0 s (608,0–616,0)  ·  #77  ·  REJİM: A (10 dk)  ·  SAAT: 18:00→18:10  ·  İSTASYON: B · BANYO
```

**🔄 Önceki sahneye göre değişen (→ G76):**

- önceki klibin hedefi = bu klibin ilk karesi: Zemin taş · derz yönü kilit
- ışık: 17:50 → 18:00

**▶ Bu sahnede:** Çift lavabolu dolap, üstüne iki aplik (ayna yerine); sonda iki işçi daha katılır, küvet gelir.

### 📸 GÖRSEL PROMPT (G76)

```
Photorealistic documentary photograph — Scene 76 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bathroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BATH STATION — fixed tripod against the north wall of the main bathroom, lens 1.5 metres above the floor, 6.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: Large pale stone slabs with soft grey veins clad the walls up to the ceiling. The floor is laid with matt pale stone tiles. Grey protective membrane covers the new floor, a stepladder by the left wall.

SITE / BACKGROUND: The main bathroom of the villa, six metres square, with a flat ceiling. In the middle of the far wall one wide window looks onto the garden. In the left wall a tall open shower niche is set into the wall. Near the far end of the right wall a doorway leads through to the dressing room, and through it the finished dressing room shows. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bathroom keeps exactly these openings: one wide window, one shower niche and one doorway.

THE TIME MOMENT: Six o'clock in the evening: the stone floor is laid, and the right wall is bare stone.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The window in the far wall spans about 512 pixels of frame width at about 704 to 1216 pixels from the left, and keeps that width in every frame. Its sill sits at about thirty-eight percent and its head at about eighty-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 289 degrees, elevation 14 degrees, outside on the right and behind the camera; soft warm evening daylight fills the room from the wide window, and the view through it is bright and golden. Through the glass: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the doorway the two workers in dark blue shirts and grey trousers lift the long walnut vanity off the low flat cart and carry it towards the right wall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide window, the shower niche, the doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bathroom keeps its one window, one niche and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G76 → G77)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the long walnut vanity from the low flat cart in the doorway to the right wall and set it against the stone, then fix two bronze wall lights onto the wall above it.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The vanity with its one stone top and two basins is levelled and fixed; two small bronze wall lights go up above it, unlit. Late in the shot two more workers in the same clothes help wheel the freestanding bathtub in through the doorway on a low flat cart and stop just inside. Through the window the thin clouds drift slowly and turn warmer, and the light in the room deepens towards gold.

The camera does not move at any point. The framing is identical in the first and last frame. The wide window, the shower niche, the doorway and the far corners of the bathroom stay exactly where they are, at exactly the same size and shape, for the whole shot; the window occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the window, the niche and the doorway of the bathroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 77 — KÜVET

```
SÜRE: 8,0 s (616,0–624,0)  ·  #78  ·  REJİM: G (gerçek zaman)  ·  SAAT: 18:10→18:10  ·  İSTASYON: B · BANYO
```

**🔄 Önceki sahneye göre değişen (→ G77):**

- önceki klibin hedefi = bu klibin ilk karesi: Tek dolap bankası, iki lavabo, iki aplik · küvet arabada kapının içinde
- ışık: 18:00 → 18:10

**▶ Bu sahnede:** GERÇEK ZAMAN · dört işçi bağımsız küveti pencerenin önüne koyar.

### 📸 GÖRSEL PROMPT (G77)

```
Photorealistic documentary photograph — Scene 77 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bathroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BATH STATION — fixed tripod against the north wall of the main bathroom, lens 1.5 metres above the floor, 6.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: Large pale stone slabs with soft grey veins clad the walls up to the ceiling. The floor is laid with matt pale stone tiles. A long walnut vanity with two basins in one stone top stands against the right wall, two bronze wall lights above it. The freestanding white bathtub waits on a low flat cart just inside the doorway. Grey protective membrane runs from the doorway to the window, lifting slings coiled on it.

SITE / BACKGROUND: The main bathroom of the villa, six metres square, with a flat ceiling. In the middle of the far wall one wide window looks onto the garden. In the left wall a tall open shower niche is set into the wall. Near the far end of the right wall a doorway leads through to the dressing room, and through it the finished dressing room shows. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bathroom keeps exactly these openings: one wide window, one shower niche and one doorway.

THE TIME MOMENT: Ten past six in the evening: the white bathtub waits on a low flat cart just inside the doorway.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The window in the far wall spans about 512 pixels of frame width at about 704 to 1216 pixels from the left, and keeps that width in every frame. Its sill sits at about thirty-eight percent and its head at about eighty-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 290 degrees, elevation 12 degrees, outside on the right and behind the camera; soft warm evening daylight fills the room from the wide window, and the view through it is bright and golden. Through the glass: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the workers carry at their real pace and the light holds still; nothing is accelerated.

ACTIVITY: Just inside the doorway four workers in the same dark blue shirts and grey trousers lift the freestanding white bathtub off the low flat cart, two at each side, and carry it slowly towards the window. Every person is seen from the side or from behind, back to the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The load is gripped in the workers' hands, its weight on their arms and backs, its underside clear of the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide window, the shower niche, the doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bathroom keeps its one window, one niche and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G77 → G78)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: Four workers lift the white bathtub from the low flat cart in the doorway, carry it to the window and set it down on the stone in front of the window.

Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame the tub is already lifting off the cart; the four carry it in short careful steps, turn it parallel to the window and lower it onto its base, then step back. Through the glass the few small clouds hold still.

The camera does not move at any point. The framing is identical in the first and last frame. The wide window, the shower niche, the doorway and the far corners of the bathroom stay exactly where they are, at exactly the same size and shape, for the whole shot; the window occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the window, the niche and the doorway of the bathroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 78 — BATARYA

```
SÜRE: 8,0 s (624,0–632,0)  ·  #79  ·  REJİM: A (10 dk)  ·  SAAT: 18:10→18:20  ·  İSTASYON: B · BANYO
```

**🔄 Önceki sahneye göre değişen (→ G78):**

- önceki klibin hedefi = bu klibin ilk karesi: Tek küvet, sabit yer
- ışık: 18:10 → 18:10

**▶ Bu sahnede:** Küvet yanındaki zemin bataryası mevcut çıkışa monte edilir; su gösteri değildir.

### 📸 GÖRSEL PROMPT (G78)

```
Photorealistic documentary photograph — Scene 78 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bathroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BATH STATION — fixed tripod against the north wall of the main bathroom, lens 1.5 metres above the floor, 6.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: Large pale stone slabs with soft grey veins clad the walls up to the ceiling. The floor is laid with matt pale stone tiles. A long walnut vanity with two basins in one stone top stands against the right wall, two bronze wall lights above it. A freestanding white oval bathtub stands in front of the window. Grey protective membrane runs from the doorway to the window, lifting slings coiled on it.

SITE / BACKGROUND: The main bathroom of the villa, six metres square, with a flat ceiling. In the middle of the far wall one wide window looks onto the garden. In the left wall a tall open shower niche is set into the wall. Near the far end of the right wall a doorway leads through to the dressing room, and through it the finished dressing room shows. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bathroom keeps exactly these openings: one wide window, one shower niche and one doorway.

THE TIME MOMENT: Ten past six in the evening: the bathtub stands in front of the window.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The window in the far wall spans about 512 pixels of frame width at about 704 to 1216 pixels from the left, and keeps that width in every frame. Its sill sits at about thirty-eight percent and its head at about eighty-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 290 degrees, elevation 12 degrees, outside on the right and behind the camera; soft warm evening daylight fills the room from the wide window, and the view through it is bright and golden. Through the glass: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Beside the tub the two workers in dark blue shirts and grey trousers lift the slim bronze floor tap out of its box on the low flat cart and set it on the outlet in the floor, a drill and a spanner beside it. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide window, the shower niche, the doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bathroom keeps its one window, one niche and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G78 → G79)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the floor tap from its box on the low flat cart to the outlet beside the tub and fix it onto the outlet.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They seat it plumb, tighten it and wipe it, and the empty box goes back onto the cart. Through the window the thin clouds drift slowly and turn warmer, and the light in the room deepens towards gold.

The camera does not move at any point. The framing is identical in the first and last frame. The wide window, the shower niche, the doorway and the far corners of the bathroom stay exactly where they are, at exactly the same size and shape, for the whole shot; the window occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the window, the niche and the doorway of the bathroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 79 — BANK VE HAVLULAR

```
SÜRE: 8,0 s (632,0–640,0)  ·  #80  ·  REJİM: A (10 dk)  ·  SAAT: 18:20→18:30  ·  İSTASYON: B · BANYO
```

**🔄 Önceki sahneye göre değişen (→ G79):**

- önceki klibin hedefi = bu klibin ilk karesi: Batarya tek ve sabit
- ışık: 18:10 → 18:20

**▶ Bu sahnede:** Döşemeli banyo bankı sol duvara; sonda katlı havlular. Banyo tamam.

### 📸 GÖRSEL PROMPT (G79)

```
Photorealistic documentary photograph — Scene 79 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bathroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BATH STATION — fixed tripod against the north wall of the main bathroom, lens 1.5 metres above the floor, 6.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: Large pale stone slabs with soft grey veins clad the walls up to the ceiling. The floor is laid with matt pale stone tiles. A long walnut vanity with two basins in one stone top stands against the right wall, two bronze wall lights above it. A freestanding white oval bathtub stands in front of the window. A slim floor-standing bronze tap stands beside the bathtub. Grey protective membrane runs from the doorway to the window, a low flat cart in the doorway.

SITE / BACKGROUND: The main bathroom of the villa, six metres square, with a flat ceiling. In the middle of the far wall one wide window looks onto the garden. In the left wall a tall open shower niche is set into the wall. Near the far end of the right wall a doorway leads through to the dressing room, and through it the finished dressing room shows. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bathroom keeps exactly these openings: one wide window, one shower niche and one doorway.

THE TIME MOMENT: Twenty past six in the evening: the bronze tap stands beside the tub.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The window in the far wall spans about 512 pixels of frame width at about 704 to 1216 pixels from the left, and keeps that width in every frame. Its sill sits at about thirty-eight percent and its head at about eighty-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 292 degrees, elevation 10 degrees, outside on the right and behind the camera; soft warm evening daylight fills the room from the wide window, and the view through it is bright and golden. Through the glass: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the doorway the two workers in dark blue shirts and grey trousers lift an upholstered bench off the low flat cart, a stack of folded white towels waiting beside it. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide window, the shower niche, the doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bathroom keeps its one window, one niche and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G79 → G80′)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the bench from the low flat cart in the doorway to the left wall beside the shower niche, then lay the folded towels onto it.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The bench is set down beside the niche and the white towels are stacked on it. The workers roll up the membrane and wheel the cart out. Through the window the thin clouds drift slowly and turn warmer, and the light in the room deepens towards gold.

The camera does not move at any point. The framing is identical in the first and last frame. The wide window, the shower niche, the doorway and the far corners of the bathroom stay exactly where they are, at exactly the same size and shape, for the whole shot; the window occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the window, the niche and the doorway of the bathroom are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🚪 ODA SON KARESİ (G80′ · BANYO) — S79'in hedefi · kapı saymaz

> BANYO kamerasının son karesi; sonraki sahne başka istasyondan açılır. Önce bu kare üretilir (odanın
> usta karesi), oda zinciri ondan GERİYE türetilir.

```
Photorealistic documentary photograph — end frame of Scene 79 of 90, the target frame of that shot. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the main bathroom.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: BATH STATION — fixed tripod against the north wall of the main bathroom, lens 1.5 metres above the floor, 6.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: Large pale stone slabs with soft grey veins clad the walls up to the ceiling. The floor is laid with matt pale stone tiles. A long walnut vanity with two basins in one stone top stands against the right wall, two bronze wall lights above it. A freestanding white oval bathtub stands in front of the window. A slim floor-standing bronze tap stands beside the bathtub. An upholstered bench stands against the left wall beside the shower niche, folded white towels on it. A strip of grey protective membrane lies rolled up in the doorway, a folded stepladder beside it.

SITE / BACKGROUND: The main bathroom of the villa, six metres square, with a flat ceiling. In the middle of the far wall one wide window looks onto the garden. In the left wall a tall open shower niche is set into the wall. Near the far end of the right wall a doorway leads through to the dressing room, and through it the finished dressing room shows. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The bathroom keeps exactly these openings: one wide window, one shower niche and one doorway.

THE TIME MOMENT: Half past six in the evening: the main bathroom is finished: pale stone walls, the double vanity with its two wall lights, the white tub with its bronze tap, and the bench with towels.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The window in the far wall spans about 512 pixels of frame width at about 704 to 1216 pixels from the left, and keeps that width in every frame. Its sill sits at about thirty-eight percent and its head at about eighty-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 293 degrees, elevation 9 degrees, outside on the right and behind the camera; soft warm evening daylight fills the room from the wide window, and the view through it is bright and golden. Through the glass: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the doorway the two workers in dark blue shirts and grey trousers lift the rolled membrane onto the low flat cart and wheel it out through the dressing room. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A soft sheen on the new floor, a last faint band of dust along one skirting, faint shoe prints near the door, a folded stack of dust sheets, one small offcut forgotten by the wall. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide window, the shower niche, the doorway, the corners of the room and the far hills never change shape, position, size or spacing. The bathroom keeps its one window, one niche and one doorway; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

---
