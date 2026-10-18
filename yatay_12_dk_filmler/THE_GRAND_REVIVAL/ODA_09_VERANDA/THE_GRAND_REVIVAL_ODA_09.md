# 🎬 THE_GRAND_REVIVAL — ODA 09 · VERANDA — AHŞAP DÖŞEME, DIŞ MEKÂN OTURMA GRUBU, IŞIKLAR  (S80–S85 · 6 sahne görseli + oda son kareleri + 6 I2V · 640,0–688,0 sn)

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

## 🎬 SAHNE 80 — AHŞAP DÖŞEME

```
SÜRE: 8,0 s (640,0–648,0)  ·  #81  ·  REJİM: A (10 dk)  ·  SAAT: 18:30→18:40  ·  İSTASYON: T · VERANDA
```

**🔄 Önceki sahneye göre değişen (→ G80):**

- ⛔ İSTASYON KESMESİ — BANYO → **VERANDA** (sahip istisnası: oda başına sabit kamera)
- önceki oda sonu (G80′): Küvet, dolap, aplikler, bank, duş nişi tamam
- bu odanın ilk karesi: Mevcut üstü örtülü verandaya ahşap döşeme sıralar hâlinde serilir
- ışık: 18:20→18:30 (kesmede saat sürer, atlamaz)

**▶ Bu sahnede:** Mevcut üstü örtülü verandaya ahşap döşeme sıralar hâlinde serilir; kolonlar ve tavan değişmez.

### 📸 GÖRSEL PROMPT (G80)

```
Photorealistic documentary photograph — Scene 80 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the back garden.
Lens: 24 mm spherical, f/8, ISO 400.
Camera: VERANDA STATION — fixed tripod on the back lawn, lens 1.6 metres above the ground, 12 metres from the back wall of the villa, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The veranda floor is cracked old concrete with weeds in the joints and dry leaves heaped against the back wall. The back lawn is long dry grass, and the low stone step along the veranda edge is chipped and stained. A low flat cart stands on the lawn at the left.

SITE / BACKGROUND: The back of the villa seen from its garden. A covered veranda, twelve metres wide and five deep, runs along the back wall under a flat timber roof carried on four square stone columns at its outer edge, with one low stone step along the outer edge of its floor. In the back wall, left of centre, three tall glass doors open into the salon; right of centre, three tall glass doors open into the dining room; through them the finished salon and dining room show. Two old olive trees with silver-grey leaves stand at the left and right edges of the frame, and the back lawn runs from the bottom of the frame to the step. There is exactly one house here, this villa.

THE TIME MOMENT: Half past six in the evening: the back of the villa in low evening sun: the covered veranda is cracked concrete under weeds, and through the glass doors the finished salon and dining room show.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The second stone column from the left spans about 64 pixels of frame width at about 654 to 718 pixels from the left, and keeps that width in every frame. The back wall of the villa spans the full frame width; the outer edge of the veranda floor sits at about thirty-one percent and the edge of the veranda roof at about eighty percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 293 degrees, elevation 9 degrees, on the left and behind the camera; low golden sun lies full on the back of the villa and under the veranda roof, long shadows stretching away from the camera and slightly to the right. Early summer: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the workers and the carts all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: On the veranda the two workers in dark blue shirts and grey trousers lift the first warm brown decking boards off a stack on the low flat cart at the left end and set the first row along the back wall, a trestle workbench beside the cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Cracked concrete, weeds and dead leaves in drifts against the wall, grime streaks and old rust stains on the stone, debris along the step, a patch of bare dry earth. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The veranda roof bears on the four stone columns, and each column stands on the edge of the veranda floor. The low flat cart rests on its four wheels on the lawn. The stacked boards rest on a pallet beside the cart.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The back wall, the six glass doors, the four stone columns, the veranda roof and the two olive trees never change shape, position, size or spacing. There is only ever one house; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G80 → G81)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers lay the decking boards from the stack on the low flat cart onto the veranda in rows, from the back wall out to the step.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The weeds and leaves are swept off first; then row by row the warm boards cover the old concrete from left to right, each cut at the workbench, until the whole veranda is timber. The thin high clouds drift slowly and turn gold, and the long shadows stretch further towards the house as the sun sinks.

The camera does not move at any point. The framing is identical in the first and last frame. The back wall, the six glass doors, the four stone columns and the two olive trees stay exactly where they are, at exactly the same size and shape, for the whole shot; the second stone column occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the columns and the veranda roof are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 81 — DIŞ KANEPE

```
SÜRE: 8,0 s (648,0–656,0)  ·  #82  ·  REJİM: A (10 dk)  ·  SAAT: 18:40→18:50  ·  İSTASYON: T · VERANDA
```

**🔄 Önceki sahneye göre değişen (→ G81):**

- önceki klibin hedefi = bu klibin ilk karesi: Ahşap veranda · kolonlar ve tavan aynı
- ışık: 18:30 → 18:40

**▶ Bu sahnede:** Büyük dış mekân kanepesi modülleri sırayla getirilir; tek oturma grubu oluşur.

### 📸 GÖRSEL PROMPT (G81)

```
Photorealistic documentary photograph — Scene 81 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the back garden.
Lens: 24 mm spherical, f/8, ISO 400.
Camera: VERANDA STATION — fixed tripod on the back lawn, lens 1.6 metres above the ground, 12 metres from the back wall of the villa, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The veranda floor is laid with warm brown timber decking boards. The back lawn is cut short, and the low stone step along the veranda edge is scrubbed clean. A trestle workbench with offcuts stands at the left end, a low flat cart on the lawn.

SITE / BACKGROUND: The back of the villa seen from its garden. A covered veranda, twelve metres wide and five deep, runs along the back wall under a flat timber roof carried on four square stone columns at its outer edge, with one low stone step along the outer edge of its floor. In the back wall, left of centre, three tall glass doors open into the salon; right of centre, three tall glass doors open into the dining room; through them the finished salon and dining room show. Two old olive trees with silver-grey leaves stand at the left and right edges of the frame, and the back lawn runs from the bottom of the frame to the step. There is exactly one house here, this villa.

THE TIME MOMENT: Twenty to seven in the evening: the veranda is new timber, and its floor stands empty.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The second stone column from the left spans about 64 pixels of frame width at about 654 to 718 pixels from the left, and keeps that width in every frame. The back wall of the villa spans the full frame width; the outer edge of the veranda floor sits at about thirty-one percent and the edge of the veranda roof at about eighty percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 294 degrees, elevation 7 degrees, on the left and behind the camera; low golden sun lies full on the back of the villa and under the veranda roof, long shadows stretching away from the camera and slightly to the right. Early summer: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the workers and the carts all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: From the lawn at the left the two workers in dark blue shirts and grey trousers lift the first grey cushioned sofa module off the low flat cart and carry it up the step onto the veranda. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Sawdust and timber offcuts in a band along the edge, a stack of boards on a pallet, shoe prints in the dust, wheel tracks across the grass, a tarpaulin over the stored cushions. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The veranda roof bears on the four stone columns, and each column stands on the edge of the veranda floor. The low flat cart rests on its four wheels on the lawn. The stacked boards rest on a pallet beside the cart.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The back wall, the six glass doors, the four stone columns, the veranda roof and the two olive trees never change shape, position, size or spacing. There is only ever one house; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G81 → G82)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the grey sofa modules one at a time from the low flat cart on the lawn onto the veranda and set them side by side in the middle.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Module by module the long sofa forms, facing the garden, its cushions plumped. The thin high clouds drift slowly and turn gold, and the long shadows stretch further towards the house as the sun sinks.

The camera does not move at any point. The framing is identical in the first and last frame. The back wall, the six glass doors, the four stone columns and the two olive trees stay exactly where they are, at exactly the same size and shape, for the whole shot; the second stone column occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the columns and the veranda roof are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 82 — İKİ KOLTUK

```
SÜRE: 8,0 s (656,0–664,0)  ·  #83  ·  REJİM: A (10 dk)  ·  SAAT: 18:50→19:00  ·  İSTASYON: T · VERANDA
```

**🔄 Önceki sahneye göre değişen (→ G82):**

- önceki klibin hedefi = bu klibin ilk karesi: Tek oturma grubu
- ışık: 18:40 → 18:50

**▶ Bu sahnede:** İki geniş dış mekân koltuğu sırayla; tam iki.

### 📸 GÖRSEL PROMPT (G82)

```
Photorealistic documentary photograph — Scene 82 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the back garden.
Lens: 24 mm spherical, f/8, ISO 400.
Camera: VERANDA STATION — fixed tripod on the back lawn, lens 1.6 metres above the ground, 12 metres from the back wall of the villa, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The veranda floor is laid with warm brown timber decking boards. The back lawn is cut short, and the low stone step along the veranda edge is scrubbed clean. A big outdoor sofa of grey cushioned modules stands in the middle of the veranda, facing the garden. A strip of grey protective membrane lies along the new boards, a low flat cart on the lawn.

SITE / BACKGROUND: The back of the villa seen from its garden. A covered veranda, twelve metres wide and five deep, runs along the back wall under a flat timber roof carried on four square stone columns at its outer edge, with one low stone step along the outer edge of its floor. In the back wall, left of centre, three tall glass doors open into the salon; right of centre, three tall glass doors open into the dining room; through them the finished salon and dining room show. Two old olive trees with silver-grey leaves stand at the left and right edges of the frame, and the back lawn runs from the bottom of the frame to the step. There is exactly one house here, this villa.

THE TIME MOMENT: Ten to seven in the evening: the outdoor sofa stands in the middle of the veranda.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The second stone column from the left spans about 64 pixels of frame width at about 654 to 718 pixels from the left, and keeps that width in every frame. The back wall of the villa spans the full frame width; the outer edge of the veranda floor sits at about thirty-one percent and the edge of the veranda roof at about eighty percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 296 degrees, elevation 5 degrees, on the left and behind the camera; low golden sun lies full on the back of the villa and under the veranda roof, long shadows stretching away from the camera and slightly to the right. Early summer: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the workers and the carts all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: From the lawn the two workers in dark blue shirts and grey trousers lift the first wide outdoor armchair off the low flat cart and carry it up the step. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Sawdust and timber offcuts in a band along the edge, a stack of boards on a pallet, shoe prints in the dust, wheel tracks across the grass, a tarpaulin over the stored cushions. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The veranda roof bears on the four stone columns, and each column stands on the edge of the veranda floor. The low flat cart rests on its four wheels on the lawn. Every piece of furniture stands on the floor on its own feet.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The back wall, the six glass doors, the four stone columns, the veranda roof and the two olive trees never change shape, position, size or spacing. There is only ever one house; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G82 → G83)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the two wide armchairs one at a time from the low flat cart on the lawn onto the veranda and set them facing the sofa.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. One chair per trip, both set facing the sofa, so exactly two armchairs stand on the veranda. The thin high clouds drift slowly and turn gold, and the long shadows stretch further towards the house as the sun sinks.

The camera does not move at any point. The framing is identical in the first and last frame. The back wall, the six glass doors, the four stone columns and the two olive trees stay exactly where they are, at exactly the same size and shape, for the whole shot; the second stone column occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the columns and the veranda roof are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 83 — DIŞ SEHPA

```
SÜRE: 8,0 s (664,0–672,0)  ·  #84  ·  REJİM: A (10 dk)  ·  SAAT: 19:00→19:10  ·  İSTASYON: T · VERANDA
```

**🔄 Önceki sahneye göre değişen (→ G83):**

- önceki klibin hedefi = bu klibin ilk karesi: Tam iki koltuk
- ışık: 18:50 → 19:00

**▶ Bu sahnede:** Büyük dış mekân orta sehpası oturma grubunun ortasına.

### 📸 GÖRSEL PROMPT (G83)

```
Photorealistic documentary photograph — Scene 83 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the back garden.
Lens: 24 mm spherical, f/8, ISO 400.
Camera: VERANDA STATION — fixed tripod on the back lawn, lens 1.6 metres above the ground, 12 metres from the back wall of the villa, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The veranda floor is laid with warm brown timber decking boards. The back lawn is cut short, and the low stone step along the veranda edge is scrubbed clean. A big outdoor sofa of grey cushioned modules stands in the middle of the veranda, facing the garden. Two wide outdoor armchairs face the sofa. A strip of grey protective membrane lies along the new boards, a low flat cart on the lawn.

SITE / BACKGROUND: The back of the villa seen from its garden. A covered veranda, twelve metres wide and five deep, runs along the back wall under a flat timber roof carried on four square stone columns at its outer edge, with one low stone step along the outer edge of its floor. In the back wall, left of centre, three tall glass doors open into the salon; right of centre, three tall glass doors open into the dining room; through them the finished salon and dining room show. Two old olive trees with silver-grey leaves stand at the left and right edges of the frame, and the back lawn runs from the bottom of the frame to the step. There is exactly one house here, this villa.

THE TIME MOMENT: Seven o'clock in the evening: two armchairs face the sofa.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The second stone column from the left spans about 64 pixels of frame width at about 654 to 718 pixels from the left, and keeps that width in every frame. The back wall of the villa spans the full frame width; the outer edge of the veranda floor sits at about thirty-one percent and the edge of the veranda roof at about eighty percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 297 degrees, elevation 3 degrees, on the left and behind the camera; low golden sun lies full on the back of the villa and under the veranda roof, long shadows stretching away from the camera and slightly to the right. Early summer: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the workers and the carts all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: From the lawn the two workers in dark blue shirts and grey trousers lift a big low outdoor table off the low flat cart and carry it up the step. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Sawdust and timber offcuts in a band along the edge, a stack of boards on a pallet, shoe prints in the dust, wheel tracks across the grass, a tarpaulin over the stored cushions. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The veranda roof bears on the four stone columns, and each column stands on the edge of the veranda floor. The low flat cart rests on its four wheels on the lawn. Every piece of furniture stands on the floor on its own feet.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The back wall, the six glass doors, the four stone columns, the veranda roof and the two olive trees never change shape, position, size or spacing. There is only ever one house; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G83 → G84)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the big low table from the low flat cart on the lawn onto the veranda and set it down between the sofa and the armchairs.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They centre it in the group and step back. The thin high clouds drift slowly and turn gold, and the long shadows stretch further towards the house as the sun sinks.

The camera does not move at any point. The framing is identical in the first and last frame. The back wall, the six glass doors, the four stone columns and the two olive trees stay exactly where they are, at exactly the same size and shape, for the whole shot; the second stone column occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the columns and the veranda roof are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 84 — UZUN BANK

```
SÜRE: 8,0 s (672,0–680,0)  ·  #85  ·  REJİM: A (10 dk)  ·  SAAT: 19:10→19:20  ·  İSTASYON: T · VERANDA
```

**🔄 Önceki sahneye göre değişen (→ G84):**

- önceki klibin hedefi = bu klibin ilk karesi: Sehpa grubun merkezinde
- ışık: 19:00 → 19:10

**▶ Bu sahnede:** Uzun ahşap bank arka duvarın önüne; açık geçiş korunur.

### 📸 GÖRSEL PROMPT (G84)

```
Photorealistic documentary photograph — Scene 84 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the back garden.
Lens: 24 mm spherical, f/8, ISO 400.
Camera: VERANDA STATION — fixed tripod on the back lawn, lens 1.6 metres above the ground, 12 metres from the back wall of the villa, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The veranda floor is laid with warm brown timber decking boards. The back lawn is cut short, and the low stone step along the veranda edge is scrubbed clean. A big outdoor sofa of grey cushioned modules stands in the middle of the veranda, facing the garden. Two wide outdoor armchairs face the sofa. A big low outdoor table stands between the sofa and the armchairs. A strip of grey protective membrane lies along the new boards, a low flat cart on the lawn.

SITE / BACKGROUND: The back of the villa seen from its garden. A covered veranda, twelve metres wide and five deep, runs along the back wall under a flat timber roof carried on four square stone columns at its outer edge, with one low stone step along the outer edge of its floor. In the back wall, left of centre, three tall glass doors open into the salon; right of centre, three tall glass doors open into the dining room; through them the finished salon and dining room show. Two old olive trees with silver-grey leaves stand at the left and right edges of the frame, and the back lawn runs from the bottom of the frame to the step. There is exactly one house here, this villa.

THE TIME MOMENT: Ten past seven in the evening: the seating group is complete around its table.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The second stone column from the left spans about 64 pixels of frame width at about 654 to 718 pixels from the left, and keeps that width in every frame. The back wall of the villa spans the full frame width; the outer edge of the veranda floor sits at about thirty-one percent and the edge of the veranda roof at about eighty percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 299 degrees, elevation 2 degrees, on the left and behind the camera; low golden sun lies full on the back of the villa and under the veranda roof, long shadows stretching away from the camera and slightly to the right. Early summer: golden late light, a clear sky with a few thin high clouds turning gold. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the workers and the carts all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: From the lawn the two workers in dark blue shirts and grey trousers lift a long timber bench off the low flat cart and carry it up the step towards the back wall at the right. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Sawdust and timber offcuts in a band along the edge, a stack of boards on a pallet, shoe prints in the dust, wheel tracks across the grass, a tarpaulin over the stored cushions. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The veranda roof bears on the four stone columns, and each column stands on the edge of the veranda floor. The low flat cart rests on its four wheels on the lawn. Every piece of furniture stands on the floor on its own feet.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The back wall, the six glass doors, the four stone columns, the veranda roof and the two olive trees never change shape, position, size or spacing. There is only ever one house; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G84 → G85)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the long bench from the low flat cart on the lawn onto the veranda and set it down against the back wall at the right.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They set it between two glass doors so the doors and the walkway stay clear; the sun sinks low behind the camera. The thin high clouds drift slowly and turn gold, and the long shadows stretch further towards the house as the sun sinks.

The camera does not move at any point. The framing is identical in the first and last frame. The back wall, the six glass doors, the four stone columns and the two olive trees stay exactly where they are, at exactly the same size and shape, for the whole shot; the second stone column occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the columns and the veranda roof are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 85 — SAKSILAR · IŞIKLAR

```
SÜRE: 8,0 s (680,0–688,0)  ·  #86  ·  REJİM: A (10 dk)  ·  SAAT: 19:20→19:30  ·  İSTASYON: T · VERANDA
```

**🔄 Önceki sahneye göre değişen (→ G85):**

- önceki klibin hedefi = bu klibin ilk karesi: Bank arka duvarda · geçiş açık
- ışık: 19:10 → 19:20

**▶ Bu sahnede:** İki büyük saksı sırayla; sonda güneş batarken mevcut veranda aydınlatması yanar.

### 📸 GÖRSEL PROMPT (G85)

```
Photorealistic documentary photograph — Scene 85 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the back garden.
Lens: 24 mm spherical, f/8, ISO 800.
Camera: VERANDA STATION — fixed tripod on the back lawn, lens 1.6 metres above the ground, 12 metres from the back wall of the villa, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The veranda floor is laid with warm brown timber decking boards. The back lawn is cut short, and the low stone step along the veranda edge is scrubbed clean. A big outdoor sofa of grey cushioned modules stands in the middle of the veranda, facing the garden. Two wide outdoor armchairs face the sofa. A big low outdoor table stands between the sofa and the armchairs. A long timber bench stands against the back wall at the right. A strip of grey protective membrane lies along the new boards, a low flat cart on the lawn.

SITE / BACKGROUND: The back of the villa seen from its garden. A covered veranda, twelve metres wide and five deep, runs along the back wall under a flat timber roof carried on four square stone columns at its outer edge, with one low stone step along the outer edge of its floor. In the back wall, left of centre, three tall glass doors open into the salon; right of centre, three tall glass doors open into the dining room; through them the finished salon and dining room show. Two old olive trees with silver-grey leaves stand at the left and right edges of the frame, and the back lawn runs from the bottom of the frame to the step. There is exactly one house here, this villa.

THE TIME MOMENT: Twenty past seven in the evening: the sun is setting behind the camera, and the veranda furniture stands in the last warm light.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The second stone column from the left spans about 64 pixels of frame width at about 654 to 718 pixels from the left, and keeps that width in every frame. The back wall of the villa spans the full frame width; the outer edge of the veranda floor sits at about thirty-one percent and the edge of the veranda roof at about eighty percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 300 degrees, elevation 0 degrees below the horizon, on the left and behind the camera, so there is no direct sun: soft afterlight just after sunset, the sky pale orange low behind the camera and clear blue above; the lit wall lights give a small warm light under the veranda roof. Early summer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the workers and the carts all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: From the lawn the two workers in dark blue shirts and grey trousers lift the first big stone planter with an olive shrub off the low flat cart and set it at the outer edge of the veranda. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Sawdust and timber offcuts in a band along the edge, a stack of boards on a pallet, shoe prints in the dust, wheel tracks across the grass, a tarpaulin over the stored cushions. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The veranda roof bears on the four stone columns, and each column stands on the edge of the veranda floor. The low flat cart rests on its four wheels on the lawn. Every piece of furniture stands on the floor on its own feet.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The back wall, the six glass doors, the four stone columns, the veranda roof and the two olive trees never change shape, position, size or spacing. There is only ever one house; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G85 → G86′)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the two stone planters one at a time from the low flat cart on the lawn to the outer edge of the veranda, and late in the shot the wall lights come on.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The planters are set at the two outer corners; the sun goes down behind the camera, and late in the shot the wall lights on the back wall come on all at once and stay on. The workers wheel the empty cart off across the lawn. The thin high clouds drift slowly and the sky fades from gold to pale orange as the sun goes down behind the camera.

The camera does not move at any point. The framing is identical in the first and last frame. The back wall, the six glass doors, the four stone columns and the two olive trees stay exactly where they are, at exactly the same size and shape, for the whole shot; the second stone column occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the columns and the veranda roof are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🚪 ODA SON KARESİ (G86′ · VERANDA) — S85'in hedefi · kapı saymaz

> VERANDA kamerasının son karesi; sonraki sahne başka istasyondan açılır. Önce bu kare üretilir (odanın
> usta karesi), oda zinciri ondan GERİYE türetilir.

```
Photorealistic documentary photograph — end frame of Scene 85 of 90, the target frame of that shot. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the back garden.
Lens: 24 mm spherical, f/8, ISO 800.
Camera: VERANDA STATION — fixed tripod on the back lawn, lens 1.6 metres above the ground, 12 metres from the back wall of the villa, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The veranda floor is laid with warm brown timber decking boards. The back lawn is cut short, and the low stone step along the veranda edge is scrubbed clean. A big outdoor sofa of grey cushioned modules stands in the middle of the veranda, facing the garden. Two wide outdoor armchairs face the sofa. A big low outdoor table stands between the sofa and the armchairs. A long timber bench stands against the back wall at the right. Two big stone planters with olive shrubs stand at the outer edge, and the wall lights on the back wall are lit. A folded stepladder leans on the back wall at the left end.

SITE / BACKGROUND: The back of the villa seen from its garden. A covered veranda, twelve metres wide and five deep, runs along the back wall under a flat timber roof carried on four square stone columns at its outer edge, with one low stone step along the outer edge of its floor. In the back wall, left of centre, three tall glass doors open into the salon; right of centre, three tall glass doors open into the dining room; through them the finished salon and dining room show. Two old olive trees with silver-grey leaves stand at the left and right edges of the frame, and the back lawn runs from the bottom of the frame to the step. There is exactly one house here, this villa.

THE TIME MOMENT: Half past seven in the evening: sunset has passed: the veranda is finished and its wall lights are lit, the furniture set out under the timber roof.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The second stone column from the left spans about 64 pixels of frame width at about 654 to 718 pixels from the left, and keeps that width in every frame. The back wall of the villa spans the full frame width; the outer edge of the veranda floor sits at about thirty-one percent and the edge of the veranda roof at about eighty percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 302 degrees, elevation 2 degrees below the horizon, on the left and behind the camera, so there is no direct sun: soft afterlight just after sunset, the sky pale orange low behind the camera and clear blue above; the lit wall lights give a small warm light under the veranda roof. Early summer. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the workers and the carts all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: On the lawn at the left the two workers in dark blue shirts and grey trousers lift the folded stepladder onto the low flat cart and wheel it towards the house. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A soft sheen on the new decking, faint wheel tracks across the grass, a few offcuts in a stack by the step, a little sawdust in the board joints, a patch of trampled grass. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The veranda roof bears on the four stone columns, and each column stands on the edge of the veranda floor. The low flat cart rests on its four wheels on the lawn. Every piece of furniture stands on the floor on its own feet.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The back wall, the six glass doors, the four stone columns, the veranda roof and the two olive trees never change shape, position, size or spacing. There is only ever one house; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

---
