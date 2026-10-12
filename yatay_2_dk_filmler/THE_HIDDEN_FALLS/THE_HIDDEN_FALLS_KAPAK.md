# 🖼️ THE_HIDDEN_FALLS — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30] · sahip senaryosu 08.10.2026 ("Kapak: son sahneden
geniş görüntü; şelalenin arkasındaki sıcak ışıklı cam salon belirgin. Film adı THE HIDDEN FALLS sonradan eklenir.")

## 0. TEK İŞ: KÜÇÜK RESİM (video içi kapak kartı YOK)

```
KAYNAK KARE     G15 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Prompt aşağıda usta kare (G15) promptunun
                kopyası + tek ek satır (başlık bandı). Model başlığı YAZMAZ; tipografi post-prodüksiyon.
KAPAK KARTI     ⛔ YOK — sahip senaryosu "tam 2 dakika". Teslim 120,0 sn, son kare G15. Bu dosya yalnız PLATFORM KÜÇÜK
                RESMİDİR (1280×720).
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 119.5 -i teslim.mp4 -frames:v 1 g15_kaynak.jpg
                bash araclar/zincir_kontrol.sh g15_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
BAŞLIK          "THE HIDDEN FALLS" (İngilizce · 3 kelime · sahip) — YAYIN_PAKETI başlığıyla aynı vaadi söyler: çukurda
                saklı bir şelale (soru başlıkta, cevap filmde)
ÖLÇÜ            16:9 · küçük resim 1280×720 (kaynak 1920×1080 G15 karesi) · ⛔ öncesi/sonrası bölme YOK (sahip 19.09.2026)
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G15 + başlık bandı satırı)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.
> ⭐ Tercih: önce teslim dosyasının 119,5. saniyesindeki kare kullanılır; yalnız o kare bant için uygun değilse
> aşağıdaki prompt G15'ten image-to-image koşulur (G15 referans, değişen tek şey bandın sadeliği).
> Metin `bolum_uretici.py`'nin ürettiği usta kare promptundan betikle kopyalandı; tek fark başlık satırı ve bant cümlesi.

```
Photorealistic documentary site photograph — cover frame made from master frame G15. Horizontal 16:9 time-lapse of an abandoned limestone quarry rebuilt around a new glass-fronted building; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 800.
Camera: MAIN STATION — fixed tripod bolted to the rock of a narrow bench high on the south wall of the quarry, lens 16 metres above the basin floor, 110 metres from the foot of the far wall along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a long two-storey building with a full-height glass front, 45 metres wide, standing on a raised concrete base against the foot of the far quarry wall, with a double-height glass salon at its right end, a timber terrace along its front and a steel footbridge to the entrance terrace. AT THIS STAGE: everything is finished. all the lights are on: the salon glows warm behind the falling water, both storeys of the glass front glow, and small lamps on the railings and among the plants throw long warm reflections across the water. The waterfall runs from the notch down the rock face onto the salon roof and falls from its steel lip as a wide thin curtain two metres in front of the right part of the salon glass, white foam at its foot. The basin is full of calm turquoise water, three metres below the raised base and the footbridge deck. Young planting greens the benches of the east wall and three olive trees stand round the end of the footbridge. The finished building stands on its raised base against the far wall — its full-height glass front, the double-height salon at its right end and the pale timber terrace — and the steel footbridge on its slim pier links it to the entrance terrace. Three people stand still at the footbridge railing, looking towards the waterfall, small dark figures, no readable faces.

SITE / BACKGROUND: A deep abandoned limestone quarry seen from a narrow bench high on its south wall, looking north across the basin. The quarry walls are pale grey limestone cut in tall vertical faces and narrow horizontal benches. The far wall rises sheer across the back of the frame to a dead level rim, with one narrow upper bench six metres below the rim and one dark rust-stained crack running diagonally down its face left of centre. The west wall closes the left side and the east wall the right side. An old haul road ramps down the west wall to a broad flat entrance terrace in the far left corner. One tall lone umbrella pine stands on the west rim at the top left; one small roofless ruined stone hut stands on the east rim at the top right. A lone squat pillar of pale grey limestone stands in the middle of the quarry basin, its top about eleven metres above the basin floor.

THE TIME MOMENT: Twenty past seven, deep blue hour, early summer: the quarry is alive.

COMPOSITION: Horizontal 16:9. The camera is level; the far rim runs dead level at about seventy percent of frame height. The limestone pillar at the centre spans about 130 pixels of frame width — about one fifteenth — from about 920 to 1050 pixels from the left, its top at about thirty-eight percent of frame height, and keeps that width and position in every frame. The building spans from about 750 to 1340 pixels from the left, from its base at about forty-three percent of frame height to its roof at about fifty-three percent, far below the rim. The waterfall falls from the roof edge at about fifty-three percent down to the water at about thirty-nine percent of frame height, from about 1210 to 1350 pixels from the left, in front of the right end of the building. The three people stand at about 620 pixels from the left, about twenty-five pixels tall. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame. Leave a horizontal band between roughly 82 and 93 percent of frame height, across the middle of the frame between the umbrella pine and the ruined hut, visually simple and low-contrast so that a title can be set over it: no structural detail, no strong edge and no bright object inside that band — open evening sky only.

LIGHTING: Sun azimuth 294 degrees, elevation 6 degrees below the horizon, below the horizon on the left, outside the frame, so there is no direct sun: deep blue hour, the sky deep clear blue with a last pale band low over the left rim, the rock walls cool blue-grey. Early summer: a clear sky with a few high thin clouds, the grass along the rims green-gold, the new planting in full leaf. The sun stays outside the frame.

TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the water runs, falls and ripples at its real pace; nothing is accelerated.

ACTIVITY: The three people stand still at the railing, small dark figures with no readable faces; the water falls steadily and the reflections tremble.

SITE TEXTURE: Deep teal water with a soft sheen, warm reflections breaking into streaks, a band of white foam and drifting spray at the foot of the fall, a wet dark stain down the rock below the notch, a thin pale band of wet rock above the waterline, damp patches on the terrace. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The building stands bolted to its raised base against the rock, three metres above the water. The footbridge spans rest on the terrace edge, the pier and the base; the three people stand on the bridge deck.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The quarry walls, the far rim, the dark diagonal crack, the umbrella pine, the ruined stone hut, the haul road, the entrance terrace and the limestone pillar never change shape, position, size or spacing. The quarry holds exactly one building site, this one, at the foot of the far wall; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Yatayda yapı uzak duvarın dibinde (x 751–1339 · üstten 507–619), perde sağda (1213–1347): boş kalan yer kenarın
üstündeki akşam göğüdür (üstten 0–308) — bant oraya konur (üst 60 px oynatıcı bandının altında, üstten ≈76–194),
solda çam tacı (x 82–228) ve sağda kulübe (x 1741–1818) bandın dışında kalır. Sağ üst 300×100 px'e girmez · süre
damgası sağ alttadır, sütun (x 922–1050) ve köprüdeki kişiler (x ≈619) ona düşmez [A15-c].

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        THE HIDDEN FALLS (büyük harf · tek satır · 3 kelime)
YÜKSEKLİK    büyük harf ≥ %8 kare boyu = ≥ 86 px @1080 (1280×720'de ≥ 58 px; 120 px'e küçülünce ≈ 10 px — okunma eşiği)
KONUM        x ≈ 420–1500 px (çamın sağı, kulübenin solu) · y ≈ 80–190 px (1080 ölçeğinde) · sağ üst 300×100 px'e ve
             alt 100 px'e girmez
RENK         sıcak amber #F2A03D (kanal vurgusu — KANAL_KIMLIGI) · mavi saat göğüne karşı kontrast ≥ 4,5:1
             (yetmezse bandın arkasına %35 opaklıkta düz koyu lacivert şerit — gradyan değil)
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ silüet (üç yanda duvar + ışıklı yapı + beyaz perde + turkuaz su)
                 okunuyor mu · ⓑ KELİME şekli ayırt ediliyor mu · ⓒ sağ alta kara kutu (süre damgası) konunca kaybolan bir
                 şey var mı: YOK olmalı
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez; ⓑ kayboluyorsa punto büyür ya da kelime azalır
                 ⭐ aynı test S0'ın 0. karesine de: kirli sulu çukur 120 px'te çukur mu? (açılış nesnesi)
                 ⚠️ 120 px'te salon ≈13 × 7 px, perde ≈8 × 10 px — "perdenin arkasındaki ışık" küçük resimde bir SICAK
                    NOKTA olarak okunur; ayrıntı değil, renk farkı taşır (turkuaz su + sıcak salon). Okunmuyorsa sahibe döner.
② KAPAK KANITI  zincir_kontrol.sh g15_kaynak.jpg kapak.png → çıkış: ⬜ (üretimden sonra)   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → yabancı dönüm noktasını (şelalenin başlaması +
                perdenin arkasından bakış) söyleyebiliyor mu: kısmen — kapak şelaleyi gösterir (sahip kararı: kapak = GN,
                "şelalenin arkasındaki salon belirgin"); perdenin İÇİNDEN bakış saklı kalır [§3.3].
④ BAŞLIK = VAAT  kapak: "çukurun dibinde şelalenin arkasında ışıklı bir yapı" · başlık: "saklı şelale" — aynı vaat ✓
```
