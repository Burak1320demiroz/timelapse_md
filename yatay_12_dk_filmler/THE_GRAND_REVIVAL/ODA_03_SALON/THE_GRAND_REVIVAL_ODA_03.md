# 🎬 THE_GRAND_REVIVAL — ODA 03 · SALON — PARKE, HALI, İKİ KANEPE, İKİ BERJER, TAŞ SEHPA  (S17–S29 · 13 sahne görseli + oda son kareleri + 13 I2V · 136,0–240,0 sn)

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

## 🎬 SAHNE 17 — SALON BOŞALIR

```
SÜRE: 8,0 s (136,0–144,0)  ·  #18  ·  REJİM: A (10 dk)  ·  SAAT: 08:50→09:00  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G17):**

- ⛔ İSTASYON KESMESİ — GİRİŞ HOLÜ → **SALON** (sahip istisnası: oda başına sabit kamera)
- önceki oda sonu (G17′): Hol tamam: konsol, vazo, tablo, bank, avize
- bu odanın ilk karesi: Kalan eski koltuk ve döküntü hol açıklığından çıkarılır
- ışık: 08:40→08:50 (kesmede saat sürer, atlamaz)

**▶ Bu sahnede:** Kalan eski koltuk ve döküntü hol açıklığından çıkarılır; salon boşalır. Açılıştaki kanepe yeniden görünmez.

### 📸 GÖRSEL PROMPT (G17)

```
Photorealistic documentary photograph — Scene 17 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: An old torn sofa, a broken armchair and heaps of debris stand on the floor. The walls are scuffed grey-white and stained. The floor is bare grey screed. The far wall left of the opening is plain plaster. A bare round ceiling rose marks the middle of the ceiling. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A low flat cart stands in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Ten to nine in the morning: the salon lies dim and ruined, and through the wide opening the finished entrance hall shows.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 96 degrees, elevation 47 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the middle of the room the two workers in dark blue shirts and grey trousers lift the old torn sofa off the floor and carry it towards the wide opening, where a low flat cart waits, while a pile of debris is swept into a barrow. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Dust lying grey over everything, damp stains and grime streaks on the walls, cracked plaster, dead leaves in drifts in the corners, debris heaped along the skirting. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G17 → G18)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the old sofa, the broken armchair and the debris from the salon floor out through the wide opening onto the low flat cart waiting in the hall.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Load after load leaves through the opening, the torn sofa, the broken armchair, then barrows of debris, until the floor lies bare and swept. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 18 — FİLDİŞİ

```
SÜRE: 8,0 s (144,0–152,0)  ·  #19  ·  REJİM: A (10 dk)  ·  SAAT: 09:00→09:10  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G18):**

- önceki klibin hedefi = bu klibin ilk karesi: Salon boş · açıklıktan bitmiş hol görünür
- ışık: 08:50 → 09:00

**▶ Bu sahnede:** Duvarlar sıcak fildişine boyanır.

### 📸 GÖRSEL PROMPT (G18)

```
Photorealistic documentary photograph — Scene 18 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are scuffed grey-white and stained. The floor is bare grey screed. The far wall left of the opening is plain plaster. A bare round ceiling rose marks the middle of the ceiling. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A stepladder stands in the middle of the room, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Nine o'clock in the morning: the salon is empty, its walls scuffed and stained.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 98 degrees, elevation 49 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: By the left wall the two workers in dark blue shirts and grey trousers set a stepladder and roll warm ivory paint from tins on the low flat cart onto the scuffed walls, a grey protective membrane spread along the floor. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G18 → G19)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers roll warm ivory paint from the tins on the low flat cart onto the walls, from the left wall across the far wall round to the strips of wall between the glass doors.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The stains go under an even warm ivory, wall by wall, and the room brightens; the empty tins are stacked back on the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 19 — MEŞE PARKE

```
SÜRE: 8,0 s (152,0–160,0)  ·  #20  ·  REJİM: A (10 dk)  ·  SAAT: 09:10→09:20  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G19):**

- önceki klibin hedefi = bu klibin ilk karesi: Duvarlar fildişi · pencere, tavan, duvar sınırları aynı
- ışık: 09:00 → 09:10

**▶ Bu sahnede:** Geniş açık meşe parke uzak duvardan kameraya doğru, tek yönde döşenir.

### 📸 GÖRSEL PROMPT (G19)

```
Photorealistic documentary photograph — Scene 19 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are painted a warm ivory. The floor is bare grey screed. The far wall left of the opening is plain plaster. A bare round ceiling rose marks the middle of the ceiling. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A stepladder stands in the middle of the room, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Ten past nine in the morning: the walls are warm ivory, and the floor is still bare grey screed.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 99 degrees, elevation 51 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Along the far wall the two workers in dark blue shirts and grey trousers lift the first wide oak boards off a stack on the low flat cart and set the first row, a trestle workbench with a saw standing by the opening. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G19 → G20)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers lay the wide pale oak boards from the stack on the low flat cart onto the screed, row after row from the far wall towards the camera.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The pale boards advance across the screed in one direction, each cut to length at the workbench, until the whole room is oak; offcuts pile up beside the bench. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 20 — CEVİZ PANEL

```
SÜRE: 8,0 s (160,0–168,0)  ·  #21  ·  REJİM: A (10 dk)  ·  SAAT: 09:20→09:30  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G20):**

- önceki klibin hedefi = bu klibin ilk karesi: Meşe zemin tek yönde
- ışık: 09:10 → 09:20

**▶ Bu sahnede:** Hol açıklığının solundaki duvar bölümüne ceviz paneller takılır.

### 📸 GÖRSEL PROMPT (G20)

```
Photorealistic documentary photograph — Scene 20 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. The far wall left of the opening is plain plaster. A bare round ceiling rose marks the middle of the ceiling. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A trestle workbench with offcuts stands by the far wall, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Twenty past nine in the morning: the oak floor is down, and the far wall left of the opening is plain ivory plaster.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 101 degrees, elevation 53 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the far wall the two workers in dark blue shirts and grey trousers lift the first tall walnut panel off a stack on the low flat cart and set it against the plaster left of the opening, fixing it with a drill. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G20 → G21)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the tall walnut panels from the stack on the low flat cart to the far wall and fix them onto the plaster left of the opening, one beside the next.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Panel by panel the dark walnut spreads from the corner towards the opening until that part of the far wall is one warm dark surface; the right part of the wall and the opening stay unchanged. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 21 — TAVAN IŞIĞI

```
SÜRE: 8,0 s (168,0–176,0)  ·  #22  ·  REJİM: A (10 dk)  ·  SAAT: 09:30→09:40  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G21):**

- önceki klibin hedefi = bu klibin ilk karesi: Ceviz panel yalnız sol bölümde
- ışık: 09:20 → 09:30

**▶ Bu sahnede:** Bronz halka tavan aydınlatması belirlenen bağlantı noktasına kurulur.

### 📸 GÖRSEL PROMPT (G21)

```
Photorealistic documentary photograph — Scene 21 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A bare round ceiling rose marks the middle of the ceiling. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A trestle workbench with offcuts stands by the far wall, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Half past nine in the morning: the walnut panelling is up, and a bare ceiling rose marks the middle of the ceiling.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 104 degrees, elevation 55 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: Under the ceiling rose the two workers in dark blue shirts and grey trousers set a tall stepladder and lift the ring-shaped bronze ceiling light out of its crate on the low flat cart. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G21 → G22)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the bronze ring light from its crate on the low flat cart up the stepladder and hang it from the ceiling rose on three short chains.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The ring rises the last metre, the three chains are hooked on, and it hangs level over the middle of the room, unlit; the empty crate is carried back to the cart. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 22 — HALI

```
SÜRE: 8,0 s (176,0–184,0)  ·  #23  ·  REJİM: A (10 dk)  ·  SAAT: 09:40→09:50  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G22):**

- önceki klibin hedefi = bu klibin ilk karesi: Halka ışık asılı, sönük · yüksekliği sabit
- ışık: 09:30 → 09:40

**▶ Bu sahnede:** Büyük krem halı boş zeminin ortasına serilir; köşeleri bundan sonra sabit.

### 📸 GÖRSEL PROMPT (G22)

```
Photorealistic documentary photograph — Scene 22 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The room is empty and swept. The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A stepladder stands under the ceiling light, grey protective membrane along the walking line.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Twenty to ten in the morning: the bronze ring light hangs over the empty oak floor.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 106 degrees, elevation 57 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: At the far edge of the clear floor the two workers in dark blue shirts and grey trousers lift a big rolled cream rug off the low flat cart in the opening and set it down, ready to unroll. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G22 → G23)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the rolled cream rug from the low flat cart to the middle of the room and unroll it from the far edge towards the camera.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The roll travels across the oak and opens flat, the workers squaring its corners, until it lies centred under the ring light; the empty cart goes back out through the opening. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 23 — ANA KANEPE

```
SÜRE: 8,0 s (184,0–192,0)  ·  #24  ·  REJİM: A (10 dk)  ·  SAAT: 09:50→10:00  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G23):**

- önceki klibin hedefi = bu klibin ilk karesi: Halı ortada, köşeleri sabit
- ışık: 09:40 → 09:50

**▶ Bu sahnede:** Dört kişilik ana kanepe hol açıklığından getirilip halının sol kenarına konur.

### 📸 GÖRSEL PROMPT (G23)

```
Photorealistic documentary photograph — Scene 23 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit. A large cream rug lies in the middle of the floor. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the opening along the walking line, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Ten to ten in the morning: the cream rug lies in the middle of the oak floor.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 108 degrees, elevation 59 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the wide opening the two workers in dark blue shirts and grey trousers lift the long four-seat cream sofa off the low flat cart, one at each end, and carry it in. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G23 → G24)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the long cream sofa from the low flat cart in the opening to the left edge of the rug and set it down there.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They walk the sofa in end-first, turn it square to the rug and lower it, then plump the cushions; the flat cart goes back out through the opening. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 24 — İKİNCİ KANEPE

```
SÜRE: 8,0 s (192,0–200,0)  ·  #25  ·  REJİM: A (10 dk)  ·  SAAT: 10:00→10:10  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G24):**

- önceki klibin hedefi = bu klibin ilk karesi: Tek ana kanepe
- ışık: 09:50 → 10:00

**▶ Bu sahnede:** İkinci büyük kanepe halının karşı kenarına konur.

### 📸 GÖRSEL PROMPT (G24)

```
Photorealistic documentary photograph — Scene 24 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit. A large cream rug lies in the middle of the floor. A long four-seat cream sofa stands along the left edge of the rug. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the opening along the walking line, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Ten o'clock in the morning: the main sofa stands along the left edge of the rug.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 111 degrees, elevation 61 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the wide opening the two workers in dark blue shirts and grey trousers lift the second big cream sofa off the low flat cart and carry it in, one at each end. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G24 → G25)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the second cream sofa from the low flat cart in the opening to the right edge of the rug and set it down facing the first.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Set square to the rug, the two sofas face each other across a wide walkway, and the flat cart goes back out. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 25 — BERJERLER

```
SÜRE: 8,0 s (200,0–208,0)  ·  #26  ·  REJİM: A (10 dk)  ·  SAAT: 10:10→10:20  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G25):**

- önceki klibin hedefi = bu klibin ilk karesi: İki kanepe, aralarında geniş geçiş
- ışık: 10:00 → 10:10

**▶ Bu sahnede:** İki deri berjer uzak köşelere; sonda iki işçi daha katılır, taş sehpa açıklığa gelir.

### 📸 GÖRSEL PROMPT (G25)

```
Photorealistic documentary photograph — Scene 25 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit. A large cream rug lies in the middle of the floor. Two big cream sofas face each other along the left and right edges of the rug, a wide walkway between them. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the opening along the walking line, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Ten past ten in the morning: two cream sofas face each other across the rug.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 114 degrees, elevation 62 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the wide opening the two workers in dark blue shirts and grey trousers lift the first cognac leather armchair off the low flat cart and carry it towards the far left corner of the rug. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G25 → G26)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the two cognac leather armchairs one at a time from the low flat cart in the opening to the far corners of the rug and set each one down.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The first armchair goes to the far left corner, the cart goes out and comes back, and the second goes to the far right corner, leaving the way to the opening clear. Late in the shot two more workers in the same clothes help wheel the big stone coffee table in on a low flat cart and stop just inside the opening. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 26 — TAŞ SEHPA

```
SÜRE: 8,0 s (208,0–216,0)  ·  #27  ·  REJİM: G (gerçek zaman)  ·  SAAT: 10:20→10:20  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G26):**

- önceki klibin hedefi = bu klibin ilk karesi: İki berjer · taş sehpa arabada, açıklığın içinde
- ışık: 10:10 → 10:20

**▶ Bu sahnede:** GERÇEK ZAMAN · dört işçi taş orta sehpayı arabadan alıp halının ortasına yavaşça indirir.

### 📸 GÖRSEL PROMPT (G26)

```
Photorealistic documentary photograph — Scene 26 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit. A large cream rug lies in the middle of the floor. Two big cream sofas face each other along the left and right edges of the rug, a wide walkway between them. Two cognac leather armchairs stand at the far corners of the rug, one at each side, leaving the way to the opening clear. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. The big stone coffee table waits on a low flat cart just inside the opening. Grey protective membrane runs from the opening along the walking line, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Twenty past ten in the morning: the big stone coffee table waits on its low flat cart just inside the opening.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 117 degrees, elevation 64 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the workers carry at their real pace and the light holds still; nothing is accelerated.

ACTIVITY: Just inside the opening four workers in the same dark blue shirts and grey trousers lift the big stone coffee table off the low flat cart, two at each side, and carry it slowly across the oak towards the rug. Every person is seen from the side or from behind, back to the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. The load is gripped in the workers' hands, its weight on their arms and backs, its underside clear of the floor. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G26 → G27)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: Four workers lift the big stone coffee table from the low flat cart in the opening, carry it slowly to the middle of the rug and lower it onto its four short feet.

Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame the table is already lifting off the cart; the four walk it in short careful steps, set it down square between the sofas so that its feet press into the rug and it touches neither sofa, and step back. Through the glass the few small clouds hold still.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 27 — CEVİZ KONSOL

```
SÜRE: 8,0 s (216,0–224,0)  ·  #28  ·  REJİM: A (10 dk)  ·  SAAT: 10:20→10:30  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G27):**

- önceki klibin hedefi = bu klibin ilk karesi: Sehpa halının ortasında, ayakları halıya basar, kanepelere değmez
- ışık: 10:20 → 10:20

**▶ Bu sahnede:** Uzun alçak ceviz konsol ceviz panelin önüne konur.

### 📸 GÖRSEL PROMPT (G27)

```
Photorealistic documentary photograph — Scene 27 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit. A large cream rug lies in the middle of the floor. Two big cream sofas face each other along the left and right edges of the rug, a wide walkway between them. Two cognac leather armchairs stand at the far corners of the rug, one at each side, leaving the way to the opening clear. A big low stone coffee table stands in the middle of the rug on four short square feet, touching neither sofa. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the opening along the walking line, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Twenty past ten in the morning: the stone coffee table stands in the middle of the rug.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 117 degrees, elevation 64 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the wide opening the two workers in dark blue shirts and grey trousers lift a long low walnut console off the low flat cart and carry it towards the walnut panelling. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G27 → G28)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the long low walnut console from the low flat cart in the opening to the panelling and set it down against the panelling.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. They lower it gently, square it to the panelling and wipe its top, and the empty cart goes back out through the opening. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 28 — YAN SEHPALAR

```
SÜRE: 8,0 s (224,0–232,0)  ·  #29  ·  REJİM: A (10 dk)  ·  SAAT: 10:30→10:40  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G28):**

- önceki klibin hedefi = bu klibin ilk karesi: Konsolun ayak izi sabit
- ışık: 10:20 → 10:30

**▶ Bu sahnede:** İki küçük yan sehpa sırayla, her seferinde tek yük, kanepelerin uçlarına konur.

### 📸 GÖRSEL PROMPT (G28)

```
Photorealistic documentary photograph — Scene 28 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit. A large cream rug lies in the middle of the floor. Two big cream sofas face each other along the left and right edges of the rug, a wide walkway between them. Two cognac leather armchairs stand at the far corners of the rug, one at each side, leaving the way to the opening clear. A big low stone coffee table stands in the middle of the rug on four short square feet, touching neither sofa. A long low walnut console stands against the walnut panelling. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the opening along the walking line, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Half past ten in the morning: the walnut console stands against the panelling.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 121 degrees, elevation 66 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the wide opening the two workers in dark blue shirts and grey trousers lift the first small round side table off the low flat cart and carry it towards the near end of the left sofa. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G28 → G29)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the two small round side tables one at a time from the low flat cart in the opening to the near ends of the two sofas.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. One table per trip: the first goes to the left sofa, the cart goes out and comes back, and the second goes to the right sofa, so that exactly two side tables stand in the room. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 29 — LAMBADER VE ZEYTİN

```
SÜRE: 8,0 s (232,0–240,0)  ·  #30  ·  REJİM: A (10 dk)  ·  SAAT: 10:40→10:50  ·  İSTASYON: L · SALON
```

**🔄 Önceki sahneye göre değişen (→ G29):**

- önceki klibin hedefi = bu klibin ilk karesi: Tam iki yan sehpa
- ışık: 10:30 → 10:40

**▶ Bu sahnede:** Lambader sağ kanepenin yanına; büyük taş saksıda genç zeytin cam kapıların yanına. Salon tamam.

### 📸 GÖRSEL PROMPT (G29)

```
Photorealistic documentary photograph — Scene 29 of 90. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit. A large cream rug lies in the middle of the floor. Two big cream sofas face each other along the left and right edges of the rug, a wide walkway between them. Two cognac leather armchairs stand at the far corners of the rug, one at each side, leaving the way to the opening clear. A big low stone coffee table stands in the middle of the rug on four short square feet, touching neither sofa. A long low walnut console stands against the walnut panelling. Two small round walnut side tables stand at the near ends of the two sofas. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. Grey protective membrane runs from the opening along the walking line, a low flat cart in the opening.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Twenty to eleven in the morning: two side tables stand at the near ends of the sofas.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 125 degrees, elevation 68 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the wide opening the two workers in dark blue shirts and grey trousers lift a tall bronze floor lamp off the low flat cart, a young olive tree in a big stone pot waiting on a second cart behind it. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G29 → G30′)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The two workers carry the tall floor lamp from the low flat cart to the right sofa, then wheel the potted olive tree on its cart to the glass doors and set it down.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The lamp is stood beside the right sofa, unlit; the olive tree in its stone pot is set down by the glass doors. The workers roll up the membrane along the walking line and wheel both carts out through the opening. Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor.

The camera does not move at any point. The framing is identical in the first and last frame. The wide opening to the hall, the three glass doors, the big window and the far corners of the room stay exactly where they are, at exactly the same size and shape, for the whole shot; the wide opening occupies exactly the same width of the frame in the first and last frame, and eye level stays at exactly half the frame height. The walls, the opening, the glass doors and the window of the salon are never removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🚪 ODA SON KARESİ (G30′ · SALON) — S29'in hedefi · kapı saymaz

> SALON kamerasının son karesi; sonraki sahne başka istasyondan açılır. Önce bu kare üretilir (odanın
> usta karesi), oda zinciri ondan GERİYE türetilir.

```
Photorealistic documentary photograph — end frame of Scene 29 of 90, the target frame of that shot. Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm camera in the salon.
Lens: 24 mm spherical, f/5.6, ISO 400.
Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single-storey limestone villa of about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze. AT THIS STAGE: The walls are painted a warm ivory. The floor is laid with wide pale oak boards running away from the camera. Dark walnut panelling covers the far wall left of the opening. A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit. A large cream rug lies in the middle of the floor. Two big cream sofas face each other along the left and right edges of the rug, a wide walkway between them. Two cognac leather armchairs stand at the far corners of the rug, one at each side, leaving the way to the opening clear. A big low stone coffee table stands in the middle of the rug on four short square feet, touching neither sofa. A long low walnut console stands against the walnut panelling. Two small round walnut side tables stand at the near ends of the two sofas. A tall bronze floor lamp stands beside the right sofa, and one young olive tree in a big stone pot stands by the glass doors. Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves. A strip of grey protective membrane lies rolled up in the opening, a folded stepladder beside it.

SITE / BACKGROUND: The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds one big window onto the front garden. Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon at exactly half the frame height. The salon keeps exactly these openings: one wide opening to the hall, three glass doors and one big window.

THE TIME MOMENT: Ten to eleven in the morning: the salon is finished: two cream sofas and two cognac armchairs around the stone table on the cream rug, the walnut console, two side tables, the floor lamp and the olive tree.

COMPOSITION: Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine percent and its ceiling line at about ninety-two percent of the frame height. Nothing that proves progress sits in the bottom tenth of the frame.

LIGHTING: Sun azimuth 129 degrees, elevation 69 degrees, outside on the left and ahead of the camera; sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight. Through the glass: a clear blue sky with a few small white clouds; the air is clear. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light, the patches of sun, the clouds outside the windows and the workers all move at the same accelerated speed. Ten minutes pass across this shot. Nothing moves at normal speed.

ACTIVITY: In the wide opening the two workers in dark blue shirts and grey trousers lift the last rolled strip of membrane onto the low flat cart and wheel it away into the hall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere.

SITE TEXTURE: A soft sheen on the new floor, a last faint band of dust along one skirting, faint shoe prints near the door, a folded stack of dust sheets, one small offcut forgotten by the wall. A documentary interior photograph on colour negative film, true colour, fine grain.

PHYSICS: The walls and the high ceiling bear on the stone shell of the villa. The low flat cart rests on its four wheels on the floor. The light fitting hangs from its ceiling hook, each chain taut under its weight. Every piece of furniture stands on the floor on its own feet and rests its full weight there.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The wide opening, the three glass doors, the big window, the corners of the room and the far hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors and one window; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

---
