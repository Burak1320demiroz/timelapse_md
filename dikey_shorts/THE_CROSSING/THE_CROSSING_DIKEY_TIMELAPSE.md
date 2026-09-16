# 🌉 THE CROSSING — Dikey Timelapse Planı

Dikey Timelapse Production Document
Format: **9:16 (DİKEY)** | Sahne: **8 × (7,5 sn / 10,0 sn / 5,0 sn) = 60,0 sn** | Kapak kartı: **5,0 sn** | Toplam: **65,0 sn**
Prompt yapısı: her sahne için **1 görsel + 1 I2V video promptu** (8 sahne = 9 görsel + 8 I2V)
Yapı: **kıyı kablo-askılı köprü** (`YAPI_TIPI_KARTLARI` §3) · Saha: **kıyı / deniz kabuğu** (`SAHA_VE_IKLIM` §3.3)
Zaman yayı: **36 ay (3 yıl) → 60 saniye**
Kamera mimarisi: **MAIN STATION** — kayalık gözlem noktasından sabit tripod

_"Dört yüz metrelik deniz açıklığı. İki pilon yükselir, askı kabloları ağ gibi örülür, fırtınaya rağmen iki kol ortada kenetlenir."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU    8 sahne (7.5s/10s/5s) = 60,0 sn    ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn       =  5,0 sn    ← SAHNE DEĞİL, ayrı denetlenir
─────────────────────────────────────────────────
TOPLAM                                  65,0 sn
```

⛔ Kapak kartı S7'nin usta karesinden (G8) türetilir ve üstüne **İngilizce başlık** dizilir.

---

## 🚪 KONSEPT KAPISI

```
VAAT:    Dört yüz metrelik deniz açıklığı iki kıyı pilonu ve askı kablolarıyla birbirine bağlanacak.
DİRENÇ:  ⭐ DENİZ AÇIKLIĞI VE SIK SIK PATLAYAN KIYI FIRTINASI. Deniz tabanına vinç ayağı dikilemez,
         tabliye parçaları yalnızca pilonlardan dengeli konsol (cantilever) yöntemiyle havada
         uzatılarak montajlanabilir. Fırtına esnasında tek bir dengesiz ağırlık yapıyı tehlikeye sokar.
BEDEL:   ⭐ S0'da kayalık burundaki bakir kıyı çizgisi ve küçük balıkçı teknelerinin serbest rotası,
         S7'de yerini devasa beton pilonların gölgesine ve otoban trafiğine bırakır.
```

### Üç kabul testi

```
① TEK KARE TESTİ        ✅ Tek donmuş karede köprü pilon yüksekliği, bağlı kablo sayısı ve
                        iki tabliye ucu arasındaki kalan açıklık (gap) net okunur.
② KİNETİK BAĞIMSIZLIK   ✅ Sabit kadrajda pilonlar yükselir, gergi kabloları tek tek eklenir,
                        tabliye ortaya doğru uzar, açıklık kapanır.
③ BAŞLIK ŞEMASI         ✅ "THE CROSSING" (2 kelime)
```

---

## 🔒 DEĞİŞMEZLER TABLOSU

```
ARAÇ KUTU SETİ: {5, 12} (ffprobe ile ölçüldü)

┌─ KAMERA İSTASYONU (ANA) ────────────────────────────────────────────┐
│ lens          24mm spherical · f/8 · ISO 100                        │
│ yükseklik     deniz seviyesinden 22,0 m yüksekte                      │
│ mesafe        Pilon A ekseninden 140,0 m · kuzeydoğu bakısı         │
│ bakış açısı   045° (kuzeydoğu) · tilt -2° · roll 0°                  │
│ sabitleme     bolted to a fixed tripod, absolutely zero movement    │
└─────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI ────────────────────────────────────────────────┐
│ ① SAĞDA, yakın yakada: dikey koyu sütunlu Basalt Headland kayalığı │
│ ② SOLDA, karşı yakada: beyaz boyalı 19. yüzyıl deniz fenerli sırt   │
│ ③ ARKADA: tam %48 frame yüksekliğinde uzanan kesintisiz deniz ufku │
└─────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ──────────────────────────────────────────────────┐
│ ufuk çizgisi   kare yüksekliğinin tam %48'inde (Y=%48)              │
│ Pilon A tacı   %82,0  ·  Pilon B tacı %68,0                         │
│ Tabliye kotu   %48,0 seviyesinde yatay hat                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ

| S | SÜRE | SAHNE ADI | ELEMAN / İLERLEME | ARA HÂL (%/GEÇİCİ) | MEVSİM TAŞIYICISI | GÜNEŞ / IŞIK | DEĞİŞMEYEN ÇAPA |
|---|---|---|---|---|---|---|---|
| 0 | 7,50 | Deniz Temelleri | Su içi caisson temelleri dökülüyor | %0 / çelik palplanş perdesi, sondaj dubaları, yüzer beton pompası | Yaz başı, açık turkuaz deniz | 08:30 (Azimuth 095°, Elevation 35°) | Basalt Headland & Lighthouse Ridge |
| 1 | 7,50 | Pilon A Tırmanışı | Pilon A 97 m (%75) yüksekliğe ulaştı | %75 / sarı tırmanır kalıp (climbing formwork), kule vinç, geçici çapraz gergiler | Sonbahar başı, derin mavi deniz | 10:00 (Azimuth 125°, Elevation 42°) | Basalt Headland & Lighthouse Ridge |
| 2 | 7,50 | İkiz Pilonlar ve İlk Kablolar | Pilon A 130 m (%100), Pilon B 130 m (%100), starter deck ve 4 çift kablo | %100 pilonlar / Pilon A'da 4 çift kalıcı kablo, starter deck 20 m (gap 360 m), gergi halatları | Sonbahar sonu, gri çiseleyen gökyüzü | 11:30 (Azimuth 150°, Elevation 32°) | Basalt Headland & Lighthouse Ridge |
| 3 | 7,50 | Konsol Tabliye İlerlemesi | Her pilona 12 çift kablo bağlı, tabliyeler 80'er m ilerledi | Gap 240 m / derrick vinçler tabliye ucunda, donatı kafesleri ve germe kovanları | Kış başı, soğuk açık gökyüzü | 13:00 (Azimuth 180°, Elevation 24°) | Basalt Headland & Lighthouse Ridge |
| 4 | 7,50 | Açıklığın İyice Daralması | Her pilona 20 çift kablo bağlı, tabliyeler 140'ar m ilerledi | Gap 120 m / tabliye uçlarında süspansiyon askıları, montaj platformları | İlkbahar, canlı deniz | 14:30 (Azimuth 210°, Elevation 38°) | Basalt Headland & Lighthouse Ridge |
| 5 | 10,00 | Kıyı Fırtınası ve Dayanıklılık | Her pilona 26 çift kablo bağlı, tabliyeler 175'er m ilerledi | Gap 50 m / fırtına emniyet ağları, fırtına dalga serpintisi, fırtına vinç modunda derrickler | Fırtınalı sonbahar, koyu gri dalgalar | 15:30 (Azimuth 230°, Elevation 20°) | Basalt Headland & Lighthouse Ridge |
| 6 | 7,50 | Son Segment ve Kapanış | Closure segment yerleşti, gap 0 m, derrick vinçler sökümde | Gap 0 m / her pilona 32 çift kablo bağlı, kapatma segmenti kaynak dikişleri | Yaz başı, altın saat ışığı | 16:30 (Azimuth 250°, Elevation 30°) | Basalt Headland & Lighthouse Ridge |
| 7 | 5,00 | Asfalt, Aydınlatma ve Açılış | Asfalt serimi tamamlandı, aydınlatma ve korkuluklar takıldı, araç trafiği başladı | Tamamlanmış köprü / tüm geçici vinçler ve iskeleler sökülmüş, araç far çizgileri | Alacakaranlık / Gün batımı | 18:30 (Azimuth 280°, Elevation 8°) | Basalt Headland & Lighthouse Ridge |

---

## ☀️ ZAMAN VE IŞIK GÜNEŞ SAATİ

| Sahne | Mevsim | Azimuth | Elevation | Gölge Yönü | Gökyüzü / Renk Sıcaklığı |
|---|---|---|---|---|---|
| S0 | Yaz başı | 095° | 35° | Batı-kuzeybatı | Berrak açık mavi (6000K) |
| S1 | Sonbahar başı | 125° | 42° | Kuzeybatı | Derin turkuaz-mavi (5500K) |
| S2 | Sonbahar sonu | 150° | 32° | Kuzey | Bulutlu serin gri (6500K) |
| S3 | Kış başı | 180° | 24° | Kuzey | Keskin soğuk açık mavi (7000K) |
| S4 | İlkbahar | 210° | 38° | Kuzeydoğu | Canlı bahar mavisi (5800K) |
| S5 | Fırtına | 230° | 20° | Doğu-kuzeydoğu | Fırtınalı koyu kurşuni gri (7500K) |
| S6 | Yaz başı | 250° | 30° | Doğu | Sıcak altın sarısı (4500K) |
| S7 | Gün batımı | 280° | 8° | Doğu-güneydoğu | Mor-turuncu alacakaranlık (3200K) |

---

## 🎥 PROMPTLAR

## SAHNE 0: Deniz Temelleri

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 0 of 8. Vertical time-lapse of a cable-stayed bridge construction on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: marine foundation caissons are being poured into the seabed; steel sheet pile cofferdams rise out of the water at Pylon A and Pylon B footings with rebar cages, floating barge cranes anchor near the shore, and no pylon columns or bridge decks exist yet above water level.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: Heavy steel sheet pile cofferdams stand exposed in the sea water, marking the exact geometric footprint where Pylon A and Pylon B will rise — the pale green concrete slurry level sits half-way up inside the circular cofferdam wall.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. The working seabed level sits at thirty-five percent of frame height; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 095 degrees, elevation 35 degrees, shadows falling to the west-northwest. Early summer morning light, clear azure sky, sharp crisp shadows stretching across the coastal rocks and water surface.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving boats render with heavy motion blur and water streaking. Nothing in the frame moves at normal speed.

ACTIVITY: A barge crane lifts a steel rebar cage into the cofferdam; a tracked bucket unit clears gravel at the shoreline. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The barge crane operates with its boom locked under tension; every steel cable is taut under load. Sheet pile walls press firm against tidal water pressure with no visible bowing. The crane hook block hangs vertically on a taut cable and carries a visible load.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: hoarding, machinery, container, truck, scaffolding, formwork, crane, signage. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. The crane hook block hangs vertically on a taut cable and carries a visible load.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across early summer morning. The shadows of Basalt Headland sweep slowly west-northwest across the coastal shoreline as the sun climbs. Clouds streak across the sky in long smooth trails, always from the west. Barge cranes slew smoothly back and forth above the sea cofferdams, lowering steel cages into the marine foundation while tugboats move across the water as blurred colour trails.

The camera does not move at any point. The framing is identical in the first and last frame. Basalt Headland, Lighthouse Ridge and the sea horizon stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly 48 percent of frame height. The anchor occupies exactly the same width of the frame in the first and last frame. Nothing already built is removed, moved or resized. No new section appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## SAHNE 1: Pilon A Tırmanışı

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 1 of 8. Vertical time-lapse of a cable-stayed bridge construction on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: Pylon A has climbed to 97 metres height (75 percent complete) using yellow climbing formwork jump-shores and rebar cages; Pylon B foundation cap is completed at water level; tower cranes are anchored to Pylon A's inner shaft, and no stay cables or deck segments have been attached yet.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: Pylon A's concrete legs reach exactly 97 metres high, standing three-quarters of their final height, with bright yellow climbing formwork collars wrapping the top lift.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. Pylon A crown sits at seventy-five percent of frame height; the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 125 degrees, elevation 42 degrees, shadows falling to the northwest. Early autumn morning light, deep cobalt sky, hard directional sunlight casting sharp geometric shadows along the H-frame legs.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving supply boats render with heavy motion blur and streaking. Nothing in the frame moves at normal speed.

ACTIVITY: A tower crane anchored to Pylon A lifts a steel rebar cage to the top climbing platform; a mobile crane on the quay moves rebar bundles. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The climbing formwork grips firmly onto the cured lower concrete lift; steel lattice tower crane ties pin the crane mast rigidly to Pylon A at twenty-metre vertical intervals. The crane hook block hangs vertically on a taut cable and carries a visible load.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: hoarding, machinery, container, truck, scaffolding, formwork, crane, signage. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. The crane hook block hangs vertically on a taut cable and carries a visible load.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across early autumn morning. Shadows of Pylon A sweep across the blue water towards the northwest as the sun travels higher. High cirrus clouds sweep smoothly from the west. The yellow climbing formwork jumps upward by one concrete lift, while the tower crane slews continuously carrying rebar cages.

The camera does not move at any point. The framing is identical in the first and last frame. Basalt Headland, Lighthouse Ridge and the sea horizon stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly 48 percent of frame height. The anchor occupies exactly the same width of the frame in the first and last frame. Nothing already built is removed, moved or resized. No new section appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## SAHNE 2: İkiz Pilonlar ve İlk Kablolar

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 2 of 8. Vertical time-lapse of a cable-stayed bridge construction on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: Pylon A and Pylon B have both reached 130 metres full height; a 20-metre starter deck segment with timber formwork and rebar cages is constructed at Pylon A with 4 pairs of white permanent stay cables anchored from the pylon head to the starter deck; deck gap between sides remains 360 metres wide.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: Four pairs of bright white stay cables extend diagonally from Pylon A's upper anchor housing to the short 20-metre starter deck — the color boundary between pale cured pylon concrete and dark wet top crossbeam concrete sits at 120 metres elevation.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. Pylon A crown sits at 82 percent and Pylon B crown sits at 68 percent. The working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 150 degrees, elevation 32 degrees, shadows falling to the north. Late autumn morning light, cool overcast grey sky, soft diffused lighting with pale shadows along the coastal rocks.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving supply vessels render with heavy motion blur and streaking. Nothing in the frame moves at normal speed.

ACTIVITY: A strand-jacking rig tensioner pulls a white stay cable sheath into Pylon A's anchor block; a deck derrick crane hoists a steel floor beam onto the deck framing. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: Four pairs of stay cables hang under high tension, carrying the entire weight of the 20-metre starter deck section; no temporary piers support the deck from below. The crane hook block hangs vertically on a taut cable and carries a visible load.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: hoarding, machinery, container, truck, scaffolding, formwork, crane, signage. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. The crane hook block hangs vertically on a taut cable and carries a visible load.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across late autumn morning. Soft shadows sweep slowly north across the coastal rocks under a pale grey overcast sky. Low grey clouds move swiftly from the west. Strand jacks pull white stay cables taut one by one, while derrick cranes position deck floor beams onto the starter section.

The camera does not move at any point. The framing is identical in the first and last frame. Basalt Headland, Lighthouse Ridge and the sea horizon stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly 48 percent of frame height. The anchor occupies exactly the same width of the frame in the first and last frame. Nothing already built is removed, moved or resized. No new section appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## SAHNE 3: Konsol Tabliye İlerlemesi

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 3 of 8. Vertical time-lapse of a cable-stayed bridge construction on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: 12 pairs of white permanent stay cables are anchored to each pylon; cantilever decks with rebar cages and steel shoring have advanced 80 metres from each pylon out over the water, leaving a central deck gap of 240 metres wide; derrick traveler cranes sit mounted on the leading edge of both cantilever decks.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: Exactly 12 pairs of taut white stay cables fan out from Pylon A, supporting an 80-metre cantilever deck projection that reaches level with the third sea beacon buoy.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. Pylon A crown sits at 82 percent and Pylon B crown sits at 68 percent. The working deck level sits at forty-eight percent of frame height; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 180 degrees, elevation 24 degrees, shadows falling due north. Early winter noon light, crisp pale blue winter sky, low angled solar rays highlighting the fan pattern of white stay cables.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving tugboats render with heavy motion blur and streaking. Nothing in the frame moves at normal speed.

ACTIVITY: A red derrick traveler crane at the deck tip hoists a steel box girder segment from a delivery barge below; a cable tensioning team operates jack units on the deck. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The 80-metre deck cantilever is fully supported by the 12 pairs of stay cables in pure tension; the derrick traveler crane at the tip transfers its load moment directly back into the stay cable system. The crane hook block hangs vertically on a taut cable and carries a visible load.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: hoarding, machinery, container, truck, scaffolding, formwork, crane, signage. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. The crane hook block hangs vertically on a taut cable and carries a visible load.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across early winter noon. Long thin shadows stretch due north across the water as the sun moves across the southern sky. Wispy cloud trails streak rapidly from the west. Derrick traveler cranes on both deck tips lift steel girder segments upward from barges, while stay cables are attached and tensioned in rhythmic sequence.

The camera does not move at any point. The framing is identical in the first and last frame. Basalt Headland, Lighthouse Ridge and the sea horizon stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly 48 percent of frame height. The anchor occupies exactly the same width of the frame in the first and last frame. Nothing already built is removed, moved or resized. No new section appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## SAHNE 4: Açıklığın İyice Daralması

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 4 of 8. Vertical time-lapse of a cable-stayed bridge construction on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: 20 pairs of white stay cables anchor to each pylon; cantilever decks with rebar cages, decking sheets and temporary scaffolding have advanced 140 metres from each side, narrowing the central deck gap to 120 metres wide; derrick traveler cranes operate at the tip of both deck arms.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: Twenty pairs of stay cables form a dense white web per pylon; the 120-metre deck gap is now narrower than the height of Pylon A.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. Pylon A crown sits at 82 percent and Pylon B crown sits at 68 percent. The central gap sits centered at forty-eight percent of frame height; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 210 degrees, elevation 38 degrees, shadows falling to the northeast. Spring afternoon light, vibrant turquoise sea water, warm 5800K sunlight glinting off the metal deck edges and white stay cables.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving cargo ships render with heavy motion blur and streaking. Nothing in the frame moves at normal speed.

ACTIVITY: Derrick traveler cranes hoist a steel deck module into position; welding teams generate bright sparks inside wind-shield enclosures on the deck. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The twin 140-metre deck cantilevers reach deep over the water channel, perfectly counterbalanced by the 20 stay cables anchored back into the shore abutments. The crane hook block hangs vertically on a taut cable and carries a visible load.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: hoarding, machinery, container, truck, scaffolding, formwork, crane, signage. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. The crane hook block hangs vertically on a taut cable and carries a visible load.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across spring afternoon. Shadows sweep smoothly towards the northeast while bright sunlight glints off the sea surface. White cumulus clouds roll across the sky from the southwest. Derrick cranes continuously lift new deck segments into place, narrowing the central gap segment by segment.

The camera does not move at any point. The framing is identical in the first and last frame. Basalt Headland, Lighthouse Ridge and the sea horizon stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly 48 percent of frame height. The anchor occupies exactly the same width of the frame in the first and last frame. Nothing already built is removed, moved or resized. No new section appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## SAHNE 5: Kıyı Fırtınası ve Dayanıklılık

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 5 of 8. Vertical time-lapse of a cable-stayed bridge construction on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: 26 pairs of white stay cables are anchored to each pylon; cantilever decks reach 175 metres from each side, leaving a narrow 50-metre gap in the middle; heavy storm safety mesh netting and temporary shoring wrap the deck edges, and derrick cranes are locked down in storm mode.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: The remaining central gap is just 50 metres wide under a severe coastal tempest; white water spray blasts up against Pylon A's base while the 26 pairs of stay cables remain rigid under gale winds.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. Pylon A crown sits at 82 percent and Pylon B crown sits at 68 percent. The 50-metre deck gap sits centered at forty-eight percent of frame height; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 230 degrees, elevation 20 degrees, shadows falling to the east-northwest. Stormy autumn afternoon light, dark slate-grey storm clouds, wind-whipped sea with white-capped crashing waves and sea spray.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving storm waves render as heavy motion blurred foam trails. Nothing in the frame moves at normal speed.

ACTIVITY: A deck derrick crane lowers a steel tie-down cable to the deck attachment; maintenance teams secure safety netting. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: Heavy sea waves break against the massive concrete pylon footings with upward ocean spray; the 175-metre deck arms withstand wind shear with zero aerodynamic flutter, held rock-solid by the 26 stay cables. The crane jib stays above the top edge of the frame; only the mast is visible.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: hoarding, machinery, container, truck, scaffolding, formwork, crane, signage. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. The jib stays above the top edge of the frame; only the mast is visible.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across a stormy autumn afternoon. Dark storm clouds race rapidly from the southwest across the grey sky while wind-whipped waves crash against the pylon foundations leaving heavy white foam streaks across the sea surface. Rain sweeps past in visible diagonal sheets while the bridge structure stands steady.

The camera does not move at any point. The framing is identical in the first and last frame. Basalt Headland, Lighthouse Ridge and the sea horizon stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly 48 percent of frame height. The anchor occupies exactly the same width of the frame in the first and last frame. Nothing already built is removed, moved or resized. No new section appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## SAHNE 6: Son Segment ve Kapanış

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 6 of 8. Vertical time-lapse of a cable-stayed bridge construction on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: All 32 pairs of white stay cables per pylon are fully installed; the final central closure deck segment with steel decking sheets is seated and welded with glowing sparks, closing the gap completely (gap 0 metres); continuous steel deck line spans unbroken from shore to shore, and derrick cranes are being disassembled.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: The central deck gap is exactly zero metres — the final steel closure segment is bolted into place, forming one continuous unbroken deck line across the sea channel.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. Pylon A crown sits at 82 percent and Pylon B crown sits at 68 percent. The continuous deck line runs horizontally at forty-eight percent of frame height; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 250 degrees, elevation 30 degrees, shadows falling to the east. Early summer golden hour light, warm 4500K sunlight illuminating the full length of the continuous deck and white stay cables.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving harbor boats render with heavy motion blur and streaking. Nothing in the frame moves at normal speed.

ACTIVITY: A deck derrick crane places the central closure deck segment onto the joint alignment; welding teams complete final deck seams with glowing sparks under golden sunlight. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The completed deck forms a continuous structural beam spanning 600 metres, supported by all 64 stay cables in perfect balanced equilibrium. The crane hook block hangs vertically on a taut cable and carries a visible load.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: hoarding, machinery, container, truck, scaffolding, formwork, crane, signage. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. The crane hook block hangs vertically on a taut cable and carries a visible load.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across early summer golden hour. Golden shadows sweep slowly east across the sea surface as the sun lowers. Thin cloud trails pass overhead in smooth horizontal lines. The final deck closure seam is welded tight as sparks cascade, and temporary derrick traveler cranes are dismantled piece by piece.

The camera does not move at any point. The framing is identical in the first and last frame. Basalt Headland, Lighthouse Ridge and the sea horizon stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly 48 percent of frame height. The anchor occupies exactly the same width of the frame in the first and last frame. Nothing already built is removed, moved or resized. No new section appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## SAHNE 7: Asfalt, Aydınlatma ve Açılış

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 7 of 8. Vertical time-lapse of a cable-stayed bridge construction on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: Bridge is 100 percent complete; dark asphalt paving, white lane markings, LED lighting masts and temporary safety mesh barriers are fully installed; all construction cranes, barges and temporary hoarding have been removed, and active vehicle traffic flows across the deck.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: Smooth black asphalt road surface with painted white lane stripes spans the entire 600-metre bridge, with continuous streams of headlight and taillight streaks flowing across it under dusk light.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. Pylon A crown sits at 82 percent and Pylon B crown sits at 68 percent. The finished bridge deck sits at forty-eight percent of frame height; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 280 degrees, elevation 8 degrees, shadows falling to the east-southeast. Sunset twilight dusk light, deep magenta and amber sky, warm bridge pole lights illuminated with long vehicle light streaks.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving highway traffic renders as continuous white and red light trails. Nothing in the frame moves at normal speed.

ACTIVITY: Dual asphalt pavers spread a fresh layer of asphalt along the bridge deck; compaction rollers press the roadway smooth as highway traffic streams across the completed bridge. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The completed bridge structure supports full dynamic traffic loads with zero deck deflection; all 64 stay cables vibrate softly in equilibrium under ambient sea breeze. The jib stays above the top edge of the frame; only the mast is visible.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: hoarding, machinery, container, truck, scaffolding, formwork, crane, signage. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. The jib stays above the top edge of the frame; only the mast is visible.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across sunset twilight. The magenta dusk sky fades into deep navy blue while the horizon turns deep orange. LED light poles along the deck illuminate brightly, and streams of vehicle headlights and taillights sweep across the bridge in unbroken white and red light ribbons.

The camera does not move at any point. The framing is identical in the first and last frame. Basalt Headland, Lighthouse Ridge and the sea horizon stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly 48 percent of frame height. The anchor occupies exactly the same width of the frame in the first and last frame. Nothing already built is removed, moved or resized. No new section appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🌟 USTA KARE (G8 — FİNAL)

### 📸 GÖRSEL PROMPT ⭐ USTA KARE

```
Photorealistic documentary construction photograph — Master Frame G8. Vertical time-lapse of a completed cable-stayed bridge on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: Bridge is 100 percent complete and fully operational; twin 130-metre H-frame pylons stand fully cured in pale grey concrete, 64 white stay cables radiate in crisp geometric symmetry, dark asphalt deck carries painted white lines, and active evening traffic flows beneath illuminated LED lamp posts.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: The master completion frame — all temporary construction equipment is cleared, the coastal landscape is fully restored, and the cable-stayed bridge stands fully illuminated against the twilight sky.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. Pylon A crown sits at 82 percent and Pylon B crown sits at 68 percent. The completed bridge deck sits at forty-eight percent of frame height; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 280 degrees, elevation 8 degrees, shadows falling to the east-southeast. Sunset twilight dusk light, deep magenta and amber sky, warm bridge pole lights illuminated with long vehicle light streaks.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving highway traffic renders as continuous white and red light trails. Nothing in the frame moves at normal speed.

ACTIVITY: Vehicle traffic moves smoothly across the deck as light trails; a coastal ferry crosses the water far below leaving a white wake. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The twin 130-metre pylons and 600-metre deck stand in static tension equilibrium; all stay cables hold constant load paths. The jib stays above the top edge of the frame; only the mast is visible.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: hoarding, machinery, container, truck, scaffolding, formwork, crane, signage. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. The jib stays above the top edge of the frame; only the mast is visible.
Output: 9:16, 4K, no text, no watermark.
```
