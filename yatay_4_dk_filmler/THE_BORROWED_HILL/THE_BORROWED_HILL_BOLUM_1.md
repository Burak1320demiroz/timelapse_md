# 🎬 THE_BORROWED_HILL — BÖLÜM 1  (S0 – S11 · G0 … G11 + 12 I2V · 0,0–120,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `THE_BORROWED_HILL_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır (model hafızasızdır: STRUCTURE ve SITE / BACKGROUND blokları 25 promptta
> BİREBİR aynı kelimelerle tekrarlanır, değişen yalnız AT THIS STAGE ve THE TIME MOMENT).
>
> İskelet `PROMPT_SABLONU.md` §1 (görsel) ve §2 (iki uçlu I2V); negatif çekirdek
> `KILAVUZ_REHBERI` §7 tam metin; blok ETİKETLERİ birebir — nesre dönen etiket kapıyı düşürür
> [DERS 20]. Görsel prompt bandı 2.000–6.000 karakter [DERS 2]; kapı `araclar/prompt_kontrol.py`.
>
> ⭐ Bu bölümün SON I2V'si (S11: G11 → G12) **G12 karesinde biter** ve G12 `BOLUM_2`'nin ilk
> görselidir: bölüm sınırı bir KAREDİR, kesme değil — ışık, gölge açısı, yapı yüzdesi orada atlamaz
> [DERS 52]. Kapı KLASÖR MODUNDA koşulur: `python3 araclar/prompt_kontrol.py yatay_4_dk_filmler/THE_BORROWED_HILL`
> (tek bölüm dosyasına koşulan kapı "usta kare yok" der — bu arıza değil, eksik koşudur).
>
> Sahne başlığı `## 🎬 SAHNE <rakam>` ile yazılır; `Scene n of 24` satırı n = 0'dan sayar.

---

## 🎬 SAHNE 0 — ⬜ FİİL

```
SÜRE: 10,0 s (0,0–10,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G0)

```
Photorealistic documentary construction photograph — Scene 0 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G0 → G1)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 1 — ⬜ FİİL

```
SÜRE: 10,0 s (10,0–20,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G1)

```
Photorealistic documentary construction photograph — Scene 1 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G1 → G2)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 2 — ⬜ FİİL

```
SÜRE: 10,0 s (20,0–30,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G2)

```
Photorealistic documentary construction photograph — Scene 2 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G2 → G3)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 3 — ⬜ FİİL

```
SÜRE: 10,0 s (30,0–40,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G3)

```
Photorealistic documentary construction photograph — Scene 3 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G3 → G4)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 4 — ⬜ FİİL

```
SÜRE: 10,0 s (40,0–50,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G4)

```
Photorealistic documentary construction photograph — Scene 4 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G4 → G5)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 5 — ⬜ FİİL

```
SÜRE: 10,0 s (50,0–60,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G5)

```
Photorealistic documentary construction photograph — Scene 5 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G5 → G6)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 6 — ⬜ FİİL

```
SÜRE: 10,0 s (60,0–70,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G6)

```
Photorealistic documentary construction photograph — Scene 6 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G6 → G7)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 7 — ⬜ FİİL

```
SÜRE: 10,0 s (70,0–80,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G7)

```
Photorealistic documentary construction photograph — Scene 7 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G7 → G8)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 8 — ⬜ FİİL

```
SÜRE: 10,0 s (80,0–90,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G8)

```
Photorealistic documentary construction photograph — Scene 8 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G8 → G9)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 9 — ⬜ FİİL

```
SÜRE: 10,0 s (90,0–100,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G9)

```
Photorealistic documentary construction photograph — Scene 9 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G9 → G10)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 10 — ⬜ FİİL

```
SÜRE: 10,0 s (100,0–110,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G10)

```
Photorealistic documentary construction photograph — Scene 10 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G10 → G11)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

---


## 🎬 SAHNE 11 — ⬜ FİİL

```
SÜRE: 10,0 s (110,0–120,0)  ·  ELEMAN + ARA HÂL: ⬜ (%⬜)  ·  REJİM: ⬜  ·  SAAT: ⬜  ·  İSTASYON: MAIN
```

### 📸 GÖRSEL PROMPT (G11)

```
Photorealistic documentary construction photograph — Scene 11 of 24. Horizontal 16:9 time-lapse
of ⬜ [yapı tipi] on ⬜ [saha].
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to ⬜, lens ⬜ metres above ⬜, ⬜ metres from ⬜,
bearing ⬜ degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — "When finished this will be …" — 25 promptta BİREBİR]
AT THIS STAGE: [bu karede kameranın GÖRDÜĞÜ: eleman adı + yüzde + geçici destek (sling / formwork /
scaffold / rebar …) + HENÜZ takılı olmayan — pozitif; "there is no X" YAZILMAZ (DERS 33 · 35)]

SITE / BACKGROUND: [arka plan çapaları tam metni — ① SOL ② SAĞ ③ uzak · ufuk · kalıcı yol/duvar —
BİREBİR; geçici ekipman GİRMEZ (DERS 1); korpusu çoğul yapıda "the only ⬜ in view" (DERS 55)]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü — çapa hizası / px]

COMPOSITION: Horizontal 16:9. [taç %⬜ · çalışma seviyesi %⬜ · ufuk %50] The crown of the structure
sits below the top eighth of the frame and the working level sits above the bottom quarter of the
frame; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.
[⭐ KESİR CÜMLESİ: "the ⬜ spans about ⬜ pixels of frame height — one ⬜th — and keeps that height
and position in every frame" — PERSPEKTIF_VE_OLCEK §4]

LIGHTING: sun azimuth ⬜ degrees, elevation ⬜ degrees, shadows falling to the ⬜. [mevsim rengi ·
bulut tipi · uzak çapanın tonu — HAVA_VE_ATMOSFER §1-§2; güneş DİSKİ anılmaz (DERS 39)]

TIME RATE: Everything in this frame is time-lapsed at the same rate: [o kadrajda VAR OLAN özneler —
clouds, shadows, machines, vehicles] all move at the same accelerated speed. Each object retains
physically correct relative motion under that shared compression. Moving vehicles render with heavy
motion blur and streaking. Nothing in the frame moves at normal speed. [REJİM beyanı — SANTIYE_HAREKETI
§2: "About two hours pass across this shot …" / "Roughly ten minutes pass …"]

ACTIVITY: [İKİ hareket eden + fiil + NESNE (DERS 43) + bir YÜZEY KANITI; iş yüzeyi eleman adı ve
yüzdeyle (DERS 51)] Crew register only as faint soft motion streaks beside their machines, never as
sharp figures; a parked truck stays sharp.

SITE TEXTURE: [saha kartından ≥5 doku — BANT ve ALAN, nesne sayılmaz; malzemenin bu karedeki yaşlanma
hâli — MALZEME_VE_DOKU §2 · §4-§5]

PHYSICS: [ÜÇ temas cümlesi — FIZIK_VE_AGIRLIK §5: ① taşınan eleman neyin üstünde · ② asılı olan NEYE
bağlı (sling / boom / cable) · ③ makinenin mekanizması ve zemin teması] [vinç varsa: "the boom head
carries a visible load on a short sling; the hook block rests on the pad between lifts" — DERS 8 · 46 · 57]

NEGATIVE: [KILAVUZ_REHBERI §7 tam metin: kamera kilidi · yapı kilidi · metin yasağı (≥8 yüzey) ·
"No architectural visualisation look" · "No cuts, no dissolves" + saha kartı eki + yapı kartı eki]

Output: 16:9, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G11 → G12)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image:
its last frame is that image, matched frame for frame — same framing, same light, same objects in
the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, FİİL ağırlıklı döngü (P2-d):] [Rejim cümlesi — "About two
hours pass across this shot."] The sky ⬜ [gök ismi + fiil: clouds streak … from the ⬜]. The shadow of
⬜ sweeps ⬜ across ⬜ as the sun moves from azimuth ⬜ to ⬜ degrees. [makine döngüsü → malzeme adımı →
sonuç → tekrar — TEK iş adımı] [araç izleri · yüzey kanıtı] [kaldırma varsa: yük görünür, oturur;
"rises as a blurred streak" YAZILMAZ — DERS 57]

[DEĞİŞMEYECEKLER — zorunlu paragraf:] The camera does not move at any point. The framing is identical
in the first and last frame. ⬜ [çapa ①], ⬜ [çapa ②] and ⬜ [çapa ③] stay exactly where they are, at
exactly the same size and shape, for the whole shot; the ⬜ [kanıt nesnesi] occupies exactly the same
width of the frame in the first and last frame. Nothing already built is removed, moved or resized.
No new element appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic
documentary time-lapse cinematography.
```

