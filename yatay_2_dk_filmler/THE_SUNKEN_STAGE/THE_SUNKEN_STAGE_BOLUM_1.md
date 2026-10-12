# 🎬 THE_SUNKEN_STAGE — BÖLÜM 1  (S0 – S9 · G0 … G9 + 10 I2V · 0,0–80,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `THE_SUNKEN_STAGE_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır. STRUCTURE, SITE / BACKGROUND ve NEGATIVE blokları bütün karelerde BİREBİR aynı
> kelimelerle tekrarlanır; değişen AT THIS STAGE, THE TIME MOMENT, COMPOSITION'ın son cümleleri, LIGHTING,
> TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.
>
> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py`)
> ki ortak bloklar harfi harfine aynı kalsın [DERS 20].
>
> ⭐ Bu bölümün SON I2V'si (S9: G9 → G10) **G10 karesinde biter** ve G10 `BOLUM_2`'nin ilk görselidir:
> bölüm sınırı bir KAREDİR, kesme değil [DERS 52]. Kapı KLASÖR MODUNDA koşulur:
> `python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_SUNKEN_STAGE`.
>
> ⛔ Vinç kancası [DERS 8]: vinç (G5–G13) her karede ya YÜKLÜ ("with … on the hook on taut slings") ya da bom ucu
> KADRAJ DIŞINDA ("its tip and line above the top edge of the frame"); boş kanca hiçbir promptta yazılmaz.
>
> ⛔ Kelime kilitleri: kahverengi taşkın suyu ("floodwater") yalnız G0–G2 ve S0–S2 I2V'lerinde; "crane" yalnız S4
> I2V'sinden G13'e (S13 I2V dâhil); "seat boards" S6 I2V'sinden, "copper" S10 I2V'sinden ve G11'den, "towers" S11
> I2V'sinden ve G12'den sonra; ışıkların yanması yalnız S15 I2V'sinden sonra; seyirci yalnız S16 I2V'sinden sonra;
> YASAK KELİME (PLAN künyesi) hiçbir promptta yok — negatifte bile.

---

## 🎬 SAHNE 0 — BOŞALTIR

```
SÜRE: 8,0 s (0,0–8,0)  ·  ELEMAN + ARA HÂL: su çizgisi 11. terasın dibinden → 7. terasın dibine (kot +6,1 → +4,1) · üstten dört yeni yay  ·  REJİM: A (10 dk)  ·  SAAT: 09:20→09:30  ·  İSTASYON: MAIN
```

> 💧 **Su kotu** [SU_VE_YANSIMA §8]: tek yön — yalnız ALÇALIR (11. teras → 7. teras → sahnenin üstü → 0);
> çıkış tek (pompalar, G0'dan kadrajda) · yapı su altında da VAR, "belirmez" · su gelmez, geri dönmez.

### 📸 GÖRSEL PROMPT (G0)

```
Photorealistic documentary site photograph — Scene 0 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: the theatre is still flooded: opaque brown floodwater fills the bowl up to the foot of the eleventh terrace, drifting autumn leaves and thin foam lines on its surface. Only the two top terraces of stepped stone seating stand clear, dark with silt, curving round the near rim, with the steps of the three stair aisles running down into the water; the edge of the next terrace shows just under the surface, and the lower terraces and the stage platform lie under the water. The lower part of the service road runs down into the water. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, thick black hoses running from the pumps down the slope into the water. A crew on the top terrace holds the hose ends.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Twenty past nine on a clear autumn morning: the pumps are already running, and the first stone curves are rising out of the floodwater.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The water line runs along the foot of the eleventh terrace, at about 25 percent of frame height in the middle, curving up to about 60 percent at both sides. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 136 degrees, elevation 24 degrees, on the right behind the camera: clear morning light from the right, long shadows falling forward to the left across the bowl. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, the brown water is smoothed to a soft sheen, machines move fast with light motion blur.

ACTIVITY: The two trailer pumps draw the brown water up the hoses into the settling tanks, a crew pulls the hose ends down the steps after the falling water line, a second crew rakes wet leaves and silt off the emerging stone into piles, and a small truck brings coils of spare hose along the service road. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Wet dark silt coating the stone of the top terraces, drifts of wet autumn leaves along the water line, thin foam lines and floating twigs on the brown water, tyre ruts and puddles in the gravel of the service road, coils of hose stacked beside the pumps. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The trailer pumps stand on their wheels on the gravel lay-by, the hoses rest on the stone steps and run down into the water, and the settling tanks sit on steel skids on the road. The stone terraces are founded on the floor of the hollow and stay unchanged under the water.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G0 → G1)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The water level in the bowl falls from the foot of the eleventh terrace to the foot of the seventh terrace as the pumps draw it up the hoses into the tanks, uncovering four more stone terraces from the top down.

Ten minutes pass in the clear morning light. Everything in this shot is time-lapsed at the same rate. From the first frame the water line is already sliding down: it drops evenly all round the bowl, never rising, and one wet, silt-dark stone curve after another comes up out of the brown water around the same centre, each a little smaller, until six terraces stand clear; the lower terraces and the stage platform stay under the water. Slow current lines drift across the surface towards the hose ends at the left. The crew pulls the hoses down the steps after the water, a second crew rakes leaves and silt into piles, and a small truck brings coils of spare hose along the service road and the crew carries them to the pumps. Thin high clouds drift slowly from the right, and long shadows fall forward to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 1 — AÇIĞA ÇIKARIR

```
SÜRE: 8,0 s (8,0–16,0)  ·  ELEMAN + ARA HÂL: su 7. terasın dibinden → sahne platformunun hemen üstüne (+4,1 → +1,5) · üç merdiven bağlanır · sol merdivende hasar görünür  ·  REJİM: A (10 dk)  ·  SAAT: 09:30→09:40  ·  İSTASYON: MAIN
```

> 💧 **Su kotu** [SU_VE_YANSIMA §8]: tek yön — yalnız ALÇALIR (11. teras → 7. teras → sahnenin üstü → 0);
> çıkış tek (pompalar, G0'dan kadrajda) · yapı su altında da VAR, "belirmez" · su gelmez, geri dönmez.

### 📸 GÖRSEL PROMPT (G1)

```
Photorealistic documentary site photograph — Scene 1 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: the water is going down: opaque brown floodwater still fills the lower bowl up to the foot of the seventh terrace, leaves and foam lines on its surface. The six top terraces of stepped stone seating stand clear, dark and wet with silt, the steps of the three radial stair aisles running down into the water; the lower terraces and the stage platform lie under it. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, thick black hoses running from the pumps down the centre aisle into the water. Crews stand on the wet terraces beside piles of raked leaves and silt.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Half past nine in the morning: half the seating is out of the water, and the curves already read as a theatre.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The water line runs along the foot of the seventh terrace, at about 31 percent of frame height in the middle, curving up to about 57 percent at both sides. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 139 degrees, elevation 25 degrees, on the right behind the camera: clear morning light from the right, long shadows falling forward to the left across the bowl. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, the brown water is smoothed to a soft sheen, machines move fast with light motion blur.

ACTIVITY: The two trailer pumps keep drawing the water up the hoses, a crew pulls the hose ends down the three stair aisles after the falling water line, a second crew shovels silt from the wet terraces into hand carts, and a truck brings more hose along the service road. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Wet dark silt coating the stone of the top terraces, drifts of wet autumn leaves along the water line, thin foam lines and floating twigs on the brown water, tyre ruts and puddles in the gravel of the service road, coils of hose stacked beside the pumps. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The trailer pumps stand on their wheels on the gravel lay-by, the hoses rest on the steps of the aisles, and the hand carts stand on the terraces. The stone terraces are founded on the floor of the hollow and stay unchanged under the water.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G1 → G2)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The water level falls from the foot of the seventh terrace to just above the stage platform, uncovering the lower terraces, the bottoms of the three stair aisles and a broken stretch of the left aisle.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the water line keeps sliding down evenly, never rising: the lower terraces come out of the brown water one after another and the three stair aisles join the curves into one complete stepped bowl round the hidden stage. On the left aisle a broken stretch shows: several steps and the ends of the terraces beside them are cracked and missing. By the end only a thin sheet of brown water lies over the stage platform and the orchestra floor. The crew pulls the hoses down the aisles after the water, a second crew shovels silt into hand carts and pushes them up the centre aisle to the rim, and a truck brings more hose along the service road. Small clouds drift slowly from the right, and the shadows fall forward to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 2 — KURUTUR

```
SÜRE: 8,0 s (16,0–24,0)  ·  ELEMAN + ARA HÂL: son sığ su sahne + orkestradan hortuma (+1,5 → 0) · ⭐ dikdörtgen sahne çamurdan çıkar · bütün geometri görünür  ·  REJİM: A (10 dk)  ·  SAAT: 09:40→09:50  ·  İSTASYON: MAIN
```

> 💧 **Su kotu** [SU_VE_YANSIMA §8]: tek yön — yalnız ALÇALIR (11. teras → 7. teras → sahnenin üstü → 0);
> çıkış tek (pompalar, G0'dan kadrajda) · yapı su altında da VAR, "belirmez" · su gelmez, geri dönmez.

### 📸 GÖRSEL PROMPT (G2)

```
Photorealistic documentary site photograph — Scene 2 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: the bowl is almost drained: the twelve stepped stone terraces and the three radial stair aisles of steps stand clear all round, dark and wet with silt, the left aisle broken where several steps and terrace ends are cracked and missing. A thin sheet of brown floodwater still covers the orchestra floor and the stage platform, the platform's straight outline faint under it. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, thick black hoses running from the pumps down the centre aisle into the shallow water. A small truck loaded with timber planks stands on the hardstand at the edge of the water.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Twenty to ten in the morning: the whole bowl stands clear, and only a sheet of water still hides the stage.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The water line runs along the foot of the third terrace, at about 34 percent of frame height in the middle, curving up to about 53 percent at both sides. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 141 degrees, elevation 26 degrees, on the right behind the camera: clear morning light from the right, long shadows falling forward to the left across the bowl. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, the brown water is smoothed to a soft sheen, machines move fast with light motion blur.

ACTIVITY: The two trailer pumps draw the last shallow water up the hoses, a crew drags the hose ends across the orchestra after the shrinking water, a second crew pulls the floating leaves and branches into piles on the lower terraces, and a crew lays timber planks from the truck as walkways at the edge of the water. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Wet dark silt coating the stone of the top terraces, drifts of wet autumn leaves along the water line, thin foam lines and floating twigs on the brown water, tyre ruts and puddles in the gravel of the service road, coils of hose stacked beside the pumps. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The trailer pumps stand on their wheels on the gravel lay-by, the hoses rest on the steps and the floor of the orchestra, and the truck sits on the gravel of the hardstand. The stone stage platform is founded on the floor of the hollow.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G2 → G3)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The last shallow water drains from the stage platform and the orchestra floor up the hoses into the tanks, and the straight stone edge of the rectangular stage platform comes up out of thick dark mud.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the sheet of brown water is already shrinking towards the hose ends at the left, never rising again, and the straight edges of the rectangular stage platform come up through it, coated in thick dark mud, until the water is gone and the whole theatre lies open: twelve curves, three aisles and the stage. The crew drags the hoses after the last water, a second crew pulls leaves and branches into piles, and a crew carries timber planks from the truck and lays them as walkways across the mud. At the end a small tracked loader, a wheel loader and two orange dump trucks drive down the service road onto the hardstand. Small clouds drift slowly, and the shadows fall forward to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 3 — TEMİZLER

```
SÜRE: 8,0 s (24,0–32,0)  ·  ELEMAN + ARA HÂL: kalın çamur sahne + orkestradan → yükleyici → damperli kamyonlar (%0 → %100) · ekipler teraslardaki birikintiyi toplar  ·  REJİM: A (10 dk)  ·  SAAT: 09:50→10:00  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G3)

```
Photorealistic documentary site photograph — Scene 3 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: the bowl is drained: the orchestra floor and the stage platform lie under a thick layer of dark wet mud with heaps of mud, leaves and branches on the platform, and the twelve stepped stone terraces and the three radial stair aisles of steps are coated in dark silt, the left aisle broken. Timber plank walkways cross the mud. A small yellow tracked loader stands on the stage platform, and a yellow wheel loader and two orange dump trucks stand on the hardstand. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, thick black hoses running from the pumps down to the orchestra floor.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Ten to ten in the morning: the water has left a bowl of mud, and the machines have come down.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. The stage platform reads as one dark rectangle of mud at the upper centre. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 143 degrees, elevation 27 degrees, on the right behind the camera: clear morning light from the right, long shadows falling forward to the left across the bowl. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The small tracked loader scrapes the thick mud off the stage platform and pushes it along the planks to the hardstand, the wheel loader lifts the heaps into a dump truck, which drives up the service road and back empty, and crews with shovels and hand carts clear the silt from the terraces into piles at the foot of the aisles. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Thick dark mud with tyre ruts and track marks on the orchestra floor, a film of brown silt and drifts of leaves on every terrace, mud spatter on the machines, puddles in the gravel of the hardstand, stacks of timber planks. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The tracked loader sits on its tracks on the stone platform, the wheel loader and the dump trucks stand on the gravel of the hardstand, and the planks rest on the mud. The stone terraces are founded on the floor of the hollow.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G3 → G4)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The tracked loader pushes the thick mud from the stage platform and the orchestra floor to the hardstand, and the wheel loader lifts it from the heaps into the dump trucks, which carry it away up the service road.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the machines are already working: the dark heaps on the stage shrink load by load, the straight stone edge of the stage platform and the curved front of the first terrace come clear, and the crews scrape the terraces from the top down and wheel the silt in carts to the loader; at the end every surface lies bare but still dull brown under a film of silt. The wheel loader lifts each heap into a dump truck, and the trucks drive up the service road loaded and come back empty, and a crew carries the planks up to the hardstand and stacks them. At the end a white water tanker truck arrives on the hardstand and the crews carry coiled washer hoses to the top terrace. Small clouds drift slowly, and the shadows fall forward to the left.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 4 — YIKAR

```
SÜRE: 8,0 s (32,0–40,0)  ·  ELEMAN + ARA HÂL: basınçlı yıkama koyu silt → açık taş (%0 → %100, en üst terastan orkestraya) · ıslak  ·  REJİM: B (2 sa)  ·  SAAT: 10:00→12:00  ·  İSTASYON: MAIN
```

> 🧽 **Islaklık defteri**: G5 ıslak (yıkandı) → G6 lekeli kuruyor → G7+ kuru, açık taş. Temizlenen yer bir daha
> kirlenmez; kırık sol merdiven yalnız S5'te onarılır.

### 📸 GÖRSEL PROMPT (G4)

```
Photorealistic documentary site photograph — Scene 4 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: the heavy clean-up is done: the stage platform and the orchestra floor are bare stone, and the twelve stepped stone terraces and the three radial stair aisles of steps are scraped bare but still dull brown-grey under a film of dried silt, the left aisle broken. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, thick black hoses running from the pumps down to the orchestra floor. A white water tanker truck stands on the hardstand with coiled pressure-washer hoses, and washing crews with long lances stand along the top terrace.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Ten in the morning: the bowl is bare but dirty, and the washing crews are lined up along the top.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. The whole bowl reads one dull brown-grey from the near rim to the stage. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 146 degrees, elevation 28 degrees, on the right behind the camera: clear morning light from the right, long shadows falling forward to the left across the bowl. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Two hours pass across this shot: shadows swing slowly round, clouds streak across the sky, machines smear into heavy motion blur.

ACTIVITY: Crews with pressure-washer lances spray the silt off the stone terrace by terrace from the near rim down towards the orchestra, a crew moves the long washer hoses from the tanker truck down the aisles behind them, and the pumps draw the grey wash water from the orchestra floor back up the hoses into the tanks. Dozens of workers in orange work clothes show only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Bands of clean pale stone beside dull silt-brown stone, grey wash water running in streaks down the steps, puddles on the orchestra floor, wet sheen on the freshly washed stone, dirt-stained hoses and tyre ruts on the hardstand. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The tanker truck stands on its wheels on the gravel hardstand, the washer hoses rest on the steps, and the pumps sit on the lay-by. The stone terraces are founded on the floor of the hollow.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G4 → G5)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The washing crews spray the dark silt from the stone terraces and stair aisles, from the near rim down to the orchestra, and the grey wash water runs down the steps to the pump hoses.

Two hours pass. Everything in this shot is time-lapsed at the same rate. Band by band from the top the dull brown stone turns a clean pale grey-white, wet and darker at first, the clean area growing steadily down the bowl terrace after terrace and along the three aisles, until the whole bowl and the stage platform are clean pale stone, still wet; the broken left aisle stays broken. The grey wash water runs down the steps to the orchestra and the pumps draw it up the hoses, and the emptied tanker truck drives off up the service road. At the end a large yellow mobile crane drives down the service road onto the hardstand, sets its outriggers, and lifts a pallet of cut stone blocks from a flatbed truck. The shadows swing slowly round behind the camera as the sun climbs, and clouds streak across the sky.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 5 — ONARIR

```
SÜRE: 8,0 s (40,0–48,0)  ·  ELEMAN + ARA HÂL: sol merdivenin kırık basamakları + yandaki teras uçları taş bloklarla (%0 → %100) · teras sayısı aynı  ·  REJİM: A (10 dk)  ·  SAAT: 12:00→12:10  ·  İSTASYON: MAIN
```

> 🧽 **Islaklık defteri**: G5 ıslak (yıkandı) → G6 lekeli kuruyor → G7+ kuru, açık taş. Temizlenen yer bir daha
> kirlenmez; kırık sol merdiven yalnız S5'te onarılır.

### 📸 GÖRSEL PROMPT (G5)

```
Photorealistic documentary site photograph — Scene 5 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: the stone is washed: the twelve stepped stone terraces and the three radial stair aisles of steps, the orchestra floor and the stage platform are clean pale stone, still wet and dark in patches; on the left aisle several steps and the terrace ends beside them are still broken and missing. A large yellow mobile crane stands on its outriggers on the hardstand at the left end of the stage, with a pallet of cut stone blocks on the hook on taut slings. A flatbed truck loaded with pallets of cut pale stone blocks stands on the hardstand. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, thick black hoses running from the pumps to the orchestra floor. A masonry crew waits at the broken steps beside a small mortar mixer.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Noon: the whole bowl is clean, and the stonemasons start on the broken aisle.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The mobile crane stands at about 578 pixels from the left, its outriggers at about 57 percent of frame height. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 180 degrees, elevation 34 degrees, high behind the camera: bright light falls straight into the bowl and onto the stage, short shadows fall away from the camera. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane lifts the pallets of cut stone blocks from the flatbed truck and lowers them beside the broken left aisle, a masonry crew sets the blocks one by one into the missing steps and terrace ends and beds them in mortar, and a second crew mixes mortar at the small mixer; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Clean pale stone drying from the top down, darker damp patches on the lower terraces, fresh mortar joints on the new blocks, stacks of pallets and offcuts on the hardstand, a film of dust and tyre ruts in the gravel. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The pallet hangs from the crane hook on four taut slings. The crane stands on its outriggers on pads on the gravel, the new blocks are seated in mortar on the old stone, and the mixer sits on a terrace.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G5 → G6)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The mobile crane lifts the pallets of cut stone blocks from the flatbed truck on the hardstand to the broken left aisle, and the masonry crew sets the blocks into the missing steps and terrace ends.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first pallet is already swinging in over the terraces: block by block the gap in the left aisle closes, step after step and the broken terrace ends beside it, until all three stair aisles run unbroken from the orchestra to the near rim, the new pale blocks matching the old stone; the number and shape of the terraces stay the same. The stone keeps drying in patches from the top down. The emptied truck drives off up the service road, and a truck loaded with bundles of timber seat boards arrives; at the end the crane lifts a bundle from it. Small clouds drift slowly, and short shadows fall away from the camera.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 6 — OTURTUR

```
SÜRE: 8,0 s (48,0–56,0)  ·  ELEMAN + ARA HÂL: ahşap oturma tahtaları 12 terasa, alttan yukarı sıra sıra (%0 → %100) · yeni tribün katı YOK  ·  REJİM: B (2 sa)  ·  SAAT: 12:10→14:10  ·  İSTASYON: MAIN
```

> 🧽 **Islaklık defteri**: G5 ıslak (yıkandı) → G6 lekeli kuruyor → G7+ kuru, açık taş. Temizlenen yer bir daha
> kirlenmez; kırık sol merdiven yalnız S5'te onarılır.

### 📸 GÖRSEL PROMPT (G6)

```
Photorealistic documentary site photograph — Scene 6 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: the stone is repaired: the twelve stepped stone terraces and the three radial stair aisles of steps run unbroken round the bowl in clean pale stone, drying from the top down, a few damp patches on the lower terraces. A large yellow mobile crane stands on its outriggers on the hardstand at the left end of the stage, with a bundle of timber seat boards on the hook on taut slings. A flatbed truck loaded with bundles of warm brown timber seat boards stands on the hardstand, and more bundles lie stacked on the orchestra floor. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, thick black hoses running from the pumps to the orchestra floor.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Ten past twelve: the bowl is whole again, and the timber for the seats has arrived.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The mobile crane stands at about 578 pixels from the left, its outriggers at about 57 percent of frame height. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 183 degrees, elevation 34 degrees, high behind the camera: bright light falls straight into the bowl and onto the stage, short shadows fall away from the camera. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all move at the same accelerated speed. Two hours pass across this shot: shadows swing slowly round, clouds streak across the sky, machines smear into heavy motion blur.

ACTIVITY: The mobile crane lifts the bundles of seat boards from the flatbed truck onto the orchestra floor, carpentry crews carry the boards up the three aisles and screw them onto steel brackets along the front of each terrace, row after row from the lowest terrace upwards; the crane carries a visible load. Dozens of workers in orange work clothes show only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: Clean pale dry stone with faint old stains, fresh sawn timber with pale cut ends, pallets and offcuts stacked on the hardstand, coils of cable, tyre ruts and a film of dust in the gravel. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The bundle hangs from the crane hook on two taut slings. The crane stands on its outriggers on the gravel, and the seat boards are bolted to steel brackets anchored in the stone terraces.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G6 → G7)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: Carpentry crews carry the warm brown timber seat boards from the stacked bundles on the orchestra floor up the aisles and fix them along the front of each stone terrace, row after row from the lowest terrace to the near rim.

Two hours pass. Everything in this shot is time-lapsed at the same rate. Row by row from the bottom a warm brown band of timber runs along each pale stone curve, terrace after terrace up the bowl, until all twelve terraces carry continuous seat boards between the three aisles and the bowl reads as warm brown curves on pale stone; the number of terraces stays twelve and no new tier is added. The crane lifts bundle after bundle from the trucks onto the orchestra floor, and the stacks there shrink as the crews carry them up. The last damp patches dry out. At the end a flatbed truck loaded with low steel deck-frame modules arrives on the hardstand and the crane lifts a module from it. The shadows swing slowly from behind the camera to the left side as the sun passes, and clouds streak across the sky.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 7 — ÇATAR

```
SÜRE: 8,0 s (56,0–64,0)  ·  ELEMAN + ARA HÂL: alçak çelik döşeme iskeleti modülleri sahne platformuna (%0 → %100, soldan sağa) · platform sınırı aşılmaz  ·  REJİM: A (10 dk)  ·  SAAT: 14:10→14:20  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G7)

```
Photorealistic documentary site photograph — Scene 7 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: the seating is fitted: all twelve stone terraces carry continuous warm brown timber seat boards between the three stair aisles of steps, the stone clean, pale and dry. The stage platform is bare pale stone. A large yellow mobile crane stands on its outriggers on the hardstand at the left end of the stage, with a steel deck-frame module on the hook on taut slings. A flatbed truck loaded with low steel deck-frame modules stands on the hardstand. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, their thick black hoses coiled beside them. A crew waits on the stage platform with bolt boxes.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Ten past two in the afternoon: the seats are in, and the stage itself comes next.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The mobile crane stands at about 578 pixels from the left, its outriggers at about 57 percent of frame height. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 217 degrees, elevation 27 degrees, behind the camera on the left: warm afternoon light from the left, shadows falling forward to the right. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane lifts the low steel deck-frame modules from the flatbed truck onto the stage platform, a crew bolts them together into one level grid from the left end to the right end, and a second crew sets steel levelling feet under them; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Clean pale dry stone with faint old stains, fresh sawn timber with pale cut ends, pallets and offcuts stacked on the hardstand, coils of cable, tyre ruts and a film of dust in the gravel. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The module hangs from the crane hook on four taut slings. The crane stands on its outriggers on the gravel, and the modules already set rest on levelling feet on the stone platform, bolted together.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G7 → G8)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The mobile crane lifts the low steel deck-frame modules from the flatbed truck on the hardstand onto the stone stage platform, and the crew bolts them into one level grid from the left end to the right.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first module is already swinging in over the platform: module by module from the left a low, regular grid of dark steel spreads across the stone, staying inside its edges, until it covers the whole platform; the seating stays as it was. The emptied truck drives off and a truck loaded with pallets of wide timber deck panels arrives; at the end the crane lifts a pallet from it. A few clouds drift slowly from the left, and the shadows fall forward to the right.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 8 — KAPLAR

```
SÜRE: 8,0 s (64,0–72,0)  ·  ELEMAN + ARA HÂL: geniş ahşap döşeme panelleri ızgaranın üstüne (%0 → %100, önden arkaya) · sıcak renkli sahne  ·  REJİM: A (10 dk)  ·  SAAT: 14:20→14:30  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G8)

```
Photorealistic documentary site photograph — Scene 8 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: all twelve stone terraces carry continuous warm brown timber seat boards between the three stair aisles of steps, the stone clean, pale and dry. The stage platform is covered from edge to edge by a low, level grid of dark steel deck frame, bolted together, its open squares showing the stone below. A large yellow mobile crane stands on its outriggers on the hardstand at the left end of the stage, with a pallet of timber deck panels on the hook on taut slings. A flatbed truck loaded with pallets of wide timber deck panels stands on the hardstand beside a skip. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, their thick black hoses coiled beside them.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Twenty past two in the afternoon: the stage frame is set, and its timber floor is next.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The mobile crane stands at about 578 pixels from the left, its outriggers at about 57 percent of frame height. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 219 degrees, elevation 26 degrees, behind the camera on the left: warm afternoon light from the left, shadows falling forward to the right. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane lifts the pallets of wide timber deck panels from the flatbed truck onto the stage, a carpentry crew lays the panels across the steel grid from the front edge to the back and screws them down, and a second crew carries offcuts to the skip on the hardstand; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Clean pale dry stone with faint old stains, fresh sawn timber with pale cut ends, pallets and offcuts stacked on the hardstand, coils of cable, tyre ruts and a film of dust in the gravel. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The pallet hangs from the crane hook on four taut slings. The crane stands on its outriggers on the gravel, and the panels already laid are screwed down onto the steel grid, bolted together and resting on the stone platform.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G8 → G9)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The carpentry crew lays the wide timber deck panels from the crane-lifted pallets onto the steel deck frame, from the front edge of the stage to the back.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first pallet is already swinging in: panel by panel from the front the dark grid closes under warm timber, until one broad, warm-coloured timber stage covers the whole stone platform and stays inside its old edges. The second crew carries the offcuts to the skip. The emptied truck drives off and a long flatbed truck loaded with curved steel ribs arrives; at the end the crane lifts the first rib from it. A few clouds drift slowly from the left, and the shadows fall forward to the right.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 9 — DİKER

```
SÜRE: 8,0 s (72,0–80,0)  ·  ELEMAN + ARA HÂL: yedi kavisli çelik kaburga sahnenin arkasına, yelpaze gibi (%0 → %100, soldan sağa) · ön üçte iki açık  ·  REJİM: A (10 dk)  ·  SAAT: 14:30→14:40  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G9)

```
Photorealistic documentary site photograph — Scene 9 of 20. Horizontal 16:9 time-lapse of a flooded open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: all twelve stone terraces carry continuous warm brown timber seat boards between the three stair aisles of steps, the stone clean, pale and dry; a broad warm timber stage floor covers the whole stone stage platform. A large yellow mobile crane stands on its outriggers on the hardstand at the left end of the stage, with a long curved steel rib on the hook on taut slings. A long flatbed truck loaded with curved steel ribs stands on the hardstand. Steel base plates are bolted along the back edge of the stage, and a rigging crew with taglines waits beside a scissor-lift platform. Two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at the upper left, their thick black hoses coiled beside them.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Half past two in the afternoon: the stage is built, and the frame of its shell is going up.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The mobile crane stands at about 578 pixels from the left, its outriggers at about 57 percent of frame height. The pumps and settling tanks stand at the upper left, around 232 pixels from the left. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 221 degrees, elevation 25 degrees, behind the camera on the left: warm afternoon light from the left, shadows falling forward to the right. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift smoothly, machines move fast with light motion blur.

ACTIVITY: The mobile crane lifts the long curved steel ribs one by one from the flatbed truck to the back of the stage, a rigging crew guides each rib with taglines and bolts its foot to a base plate, and a second crew on the scissor-lift platform bolts the rib tops together; the crane carries a visible load. Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never sharp, no readable faces.

SITE TEXTURE: Clean pale dry stone with faint old stains, fresh sawn timber with pale cut ends, pallets and offcuts stacked on the hardstand, coils of cable, tyre ruts and a film of dust in the gravel. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The rib hangs from the crane hook on two taut slings. The crane stands on its outriggers on the gravel, and the ribs already set are bolted to base plates anchored in the stone platform, braced to each other at the top.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G9 → G10)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

MOTION FOCUS: The mobile crane lifts the seven long curved steel ribs from the flatbed truck onto the base plates along the back of the stage, where they fan out and curve forward over the rear third of the stage.

Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first rib is already rising on the hook: rib by rib from the left, each one swings in, stands on its base plate and is bolted fast, until seven tall curved steel ribs fan out from the back of the stage and curve forward over its rear third, open to the sky like the frame of a great shell; the front two thirds of the stage stay clear. The emptied truck drives off, and a truck loaded with crates of outer shell panels and timber modules arrives; at the end the crane lifts a crate from it. A few clouds drift slowly from the left, and the shadows fall forward to the right.

The camera does not move at any point. The framing is identical in the first and last frame. The hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly the same width of the frame in the first and last frame. The hollow holds exactly one theatre with exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
