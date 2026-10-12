# 🖼️ THE_LAST_CARRIAGE — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30] · sahip kararı 19.09.2026 (kapak yalnız GN
karesinden, öncesi/sonrası bölme YOK) · sahip senaryosu ("Kapak: Son karedeki ışıklı vagon, cam terastaki çift ve aşağıdaki
boşluk." · "Use the final wide frame: emerald carriage, warm windows, copper roof, the glass terrace and the canyon directly below.
Keep the two rock connections visible. If the film title is added, place it in post-production without covering the carriage or
the drop. Do not add an accident, an extra carriage or a larger terrace absent from the film.") — depoda G20

## 0. TEK İŞ: KÜÇÜK RESİM (video içi kapak kartı YOK)

```
KAYNAK KARE     G20 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Aşağıda usta kare (G20) promptunun kopyası;
                BAŞLIKLI sürümde tek ek cümle (gök bandı boş kalsın). Model başlığı YAZMAZ; tipografi post-prodüksiyon.
KAPAK KARTI     ⛔ YOK — teslim 160,0 sn, son kare G20 (hikâye SAPMA ②). Bu dosya yalnız PLATFORM KÜÇÜK RESMİDİR (1280×720).
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
VARSAYILAN      ⭐ BAŞLIKLI — "THE LAST CARRIAGE" (İngilizce · 3 kelime) — depo kuralı kapağa İngilizce başlık ister; senaryo
                "film başlığı eklenirse kurguda, vagonu ve boşluğu örtmeden" diyor (hikâye SAPMA ⑯). Başlık üstteki mavi gök
                bandında, uzak sırtların (üstten 168) ÜSTÜNDE — vagon (456–770) ve boşluk (900+) örtülmez.
YEDEK           YAZISIZ — kare kendisi söyler: mavi akşamda ışıklı zümrüt vagon, bakır çatı, camın üstünde çift, altında uçurum
ÖLÇÜ            16:9 · küçük resim 1280×720 (kaynak 1920×1080 G20 karesi) · ⛔ öncesi/sonrası bölme YOK (sahip 19.09.2026 + senaryo)
⛔ YASAK        kaza · ikinci vagon · filmde olmayan büyük teras · havai fişek · sahte ok/daire · yazı/logo (senaryo "Thumbnail
                direction") · paslı vagonla bölünmüş öncesi/sonrası
```

---

## 📸 KAPAK GÖRSEL PROMPTU — YAZISIZ (G20 kopyası)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.
> ⭐ Tercih: önce teslim dosyasının 159,5. saniyesindeki kare kullanılır; yalnız o kare uygun değilse aşağıdaki prompt
> G20'den image-to-image koşulur (G20 referans).
> Metin `bolum_uretici.py`'nin ürettiği usta kare promptundan betikle kopyalandı (12.10.2026); tek fark baş satır.

```
Photorealistic documentary site photograph — thumbnail frame, identical to master frame G20, the last frame of Scene 19 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon, now a cliff-edge restaurant on its opening evening, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 1600.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits bolted on the steel deck, deep emerald green with a cream band along the window tops, its rounded roof clad in copper-coloured sheets, eight broad clear windows along its near side; short dark steel gangways with handrails link its left vestibule to the gravel yard and its right vestibule, by a few steps, to a footpath on the right ledge, small lamps at their ends; in front, a terrace of dark steel frames bolted to the bracket stubs reaches towards the camera over the canyon, timber-decked on its left and right sections and along the carriage, three large clear glass floor panels in its middle with the canyon far below, and slim dark posts with clear glass guardrails round its open edges; two timber dining tables with chairs on each timber section, the glass middle clear; warm light fills the eight windows, the gangway lamps are lit and small warm lights line the foot of the guardrails. Behind the lit windows most tables inside are taken by seated silhouettes; guests sit at three of the four terrace tables, and an adult couple stands near the middle of the glass floor, turned towards the valley. The gravel yard lies raked and empty except for one white van.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Ten to six, deep blue hour: the old carriage is a lit restaurant over the canyon.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The near edge of the terrace runs from about 455 pixels at 30 percent of frame height to about 1222 pixels at 17 percent. Its glass middle lies between about 679 and 922 pixels from the left. The lit windows are the brightest things in the frame. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 262 degrees, elevation 5 degrees below the horizon, on the left: deep clear blue hour, the sky still readable, the emerald body, the copper roof and the rock clearly visible; the air is clear, and the lamps are small warm points with crisp edges. The sun is below the horizon, outside the frame.

TIME RATE: Everything in this frame moves at natural speed: the people, the trees and the sky. Eight seconds pass across this shot: the light holds, the clouds hold still, the pine branches sway slightly in a light breeze, and people move in small natural ways.

ACTIVITY: Diners sit inside and on the terrace, a waiter walks along the walkway, and the couple stands on the glass. Guests and staff are small distant figures, seen from the side or from behind, no readable faces.

SITE TEXTURE: Satin emerald paint with a soft sheen, raked gravel on the yard with the faint print of tyre ruts, pine needles drifted in the terrace corners, a soft sheen on the glass floor, a film of dust on the rock. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The couple stands on the glass floor panels, which bear on rubber bearers in the steel edge frames; the terrace frames are bolted to the near girder, and the carriage rests on the deck, bolted down.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

## 📸 KAPAK GÖRSEL PROMPTU — BAŞLIKLI (gök bandı)

> Tek fark: COMPOSITION'ın sonuna gök bandı cümlesi. Varsayılan sürüm budur; başlık post-prodüksiyonda konur.

```
Photorealistic documentary site photograph — thumbnail frame, identical to master frame G20, the last frame of Scene 19 of 20. Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon, now a cliff-edge restaurant on its opening evening, from a fixed 28 mm site camera.
Lens: 28 mm rectilinear, f/8, ISO 1600.
Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 degrees, tilt 14 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, 24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a glass-floored middle in front. AT THIS STAGE: the carriage sits bolted on the steel deck, deep emerald green with a cream band along the window tops, its rounded roof clad in copper-coloured sheets, eight broad clear windows along its near side; short dark steel gangways with handrails link its left vestibule to the gravel yard and its right vestibule, by a few steps, to a footpath on the right ledge, small lamps at their ends; in front, a terrace of dark steel frames bolted to the bracket stubs reaches towards the camera over the canyon, timber-decked on its left and right sections and along the carriage, three large clear glass floor panels in its middle with the canyon far below, and slim dark posts with clear glass guardrails round its open edges; two timber dining tables with chairs on each timber section, the glass middle clear; warm light fills the eight windows, the gangway lamps are lit and small warm lights line the foot of the guardrails. Behind the lit windows most tables inside are taken by seated silhouettes; guests sit at three of the four terrace tables, and an adult couple stands near the middle of the glass floor, turned towards the valley. The gravel yard lies raked and empty except for one white van.

SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right ledge, stands one large pale rock split from top to bottom by a dark crack. Beyond, the canyon bends away to the left between forested slopes, and far beyond it, a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the top.

THE TIME MOMENT: Ten to six, deep blue hour: the old carriage is a lit restaurant over the canyon.

COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about 84 percent of frame height. The split pale rock spans about 157 pixels of frame width, from about 1649 to 1806 pixels from the left, its top at about 62 percent, and keeps that width and position in every frame. The carriage spans from about 503 to 1586 pixels from the left, its roof line falling from about 58 to 49 percent of frame height and its underframe from 43 to 29 percent. The forked pine stands at about 260 pixels from the left. The near edge of the terrace runs from about 455 pixels at 30 percent of frame height to about 1222 pixels at 17 percent. Its glass middle lies between about 679 and 922 pixels from the left. The lit windows are the brightest things in the frame. Nothing that proves progress falls into the top-right corner of the frame. Keep the clear deep blue sky band across the top of the frame, between about 60 and 160 pixels from the top and from about 520 to 1400 pixels from the left, plain and empty of any object, so a title can be placed there later.

LIGHTING: Sun azimuth 262 degrees, elevation 5 degrees below the horizon, on the left: deep clear blue hour, the sky still readable, the emerald body, the copper roof and the rock clearly visible; the air is clear, and the lamps are small warm points with crisp edges. The sun is below the horizon, outside the frame.

TIME RATE: Everything in this frame moves at natural speed: the people, the trees and the sky. Eight seconds pass across this shot: the light holds, the clouds hold still, the pine branches sway slightly in a light breeze, and people move in small natural ways.

ACTIVITY: Diners sit inside and on the terrace, a waiter walks along the walkway, and the couple stands on the glass. Guests and staff are small distant figures, seen from the side or from behind, no readable faces.

SITE TEXTURE: Satin emerald paint with a soft sheen, raked gravel on the yard with the faint print of tyre ruts, pine needles drifted in the terrace corners, a soft sheen on the glass floor, a film of dust on the rock. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The couple stands on the glass floor panels, which bear on rubber bearers in the steel edge frames; the terrace frames are bolted to the near girder, and the carriage rests on the deck, bolted down.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

⭐ Kamera 14° aşağı baktığı için üstte geniş bir gök bandı var (uzak sırtlar üstten 168). Başlık bu banda konur: üstten ≈66–154 px,
x ≈520–1400 — solda çatallı çamın tepesi (x ≈196 · üstten 77) bandın DIŞINDA; vagonun çatısı (üstten 456+) ve yarık kaya (405+)
bandın çok ALTINDA. Üst 60 px oynatıcı bandına ve sağ üst 300×100 px'e girmez · süre damgası sağ alttadır; vagon, cam ve çift ona
düşmez (cam 679–922 · 708–843) [A15-c]. ⚠️ Gök tonu usta karede ölçülür; bant çok parlak ya da bulutluysa yazısız kapak kullanılır.

---

## 🔤 BAŞLIK DİZGİSİ (BAŞLIKLI sürüm · post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        THE LAST CARRIAGE (büyük harf · tek satır · 3 kelime)
YÜKSEKLİK    büyük harf ≈ 88–92 px @1080 (≈ %8,3 — §2.3'ün ≥ 86 px kuralı ✓) · 120 px'e küçülünce ≈ 10 px: kelime seçilir
KONUM        x ≈ 520–1400 px (genişlik ≈ 880 px) · y ≈ 66–154 px (1080 ölçeğinde) · uzak sırtların üstünde, mavi gökte ·
             sağ üst 300×100 px'e ve alt 100 px'e girmez
RENK         sıcak amber #F2A03D (kanal vurgusu — KANAL_KIMLIGI) · mavi saat göğüne karşı kontrast ≥ 4,5:1 (yetmezse bandın
             arkasına %35 opaklıkta düz koyu şerit — gradyan değil)
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ silüet (mavi çerçevede uzun sıcak ışıklı bir kutu + önünde açık
                 renkli bir zemin + altında koyu boşluk) okunuyor mu · ⓑ başlık (BAŞLIKLI) seçiliyor mu · ⓒ sağ alta kara kutu
                 (süre damgası) konunca kaybolan bir şey var mı: YOK olmalı
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez
                 ⭐ aynı test S0'ın 0. karesine de: iki gri kaya arasında asılı kahverengi uzun kutu + solda sarı vinç + altında
                    koyu boşluk okunuyor mu? (açılış nesnesi)
                 ⚠️ çift 120 px'te ≈5 px — figür değil, cam üstünde koyu bir nokta olarak okunur; ışık KÜME olarak [ISIK_FINALI §6]
② KAPAK KANITI  zincir_kontrol.sh g20_kaynak.jpg kapak.png → çıkış: ⬜ (üretimden sonra)   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → yabancı dönüm noktasını (vagonun uçuruma inişi + cam
                teras + aynı akşam restoran) söyleyebiliyor mu: kısmen — kapak bitmiş, ışıklı restoranı gösterir (sahip kuralı:
                kapak = GN) ve başlık "kanyonun üstünde bir vagon" der; vagonun nasıl indiği, pas, boya ve camın kuruluşu saklı
                kalır [§3.3].
④ BAŞLIK = VAAT  kapak: "mavi akşamda kanyon üstünde ışıklı bir vagon restoran, camda bir çift" · başlık: "kanyonun üstünde bir tren
                vagonu" — vaat aynı ✓
```
