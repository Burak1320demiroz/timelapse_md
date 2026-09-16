# 🖼️ THE_OLD_ROAD — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30]

## 0. İKİ İŞ, TEK GÖRÜNTÜ

```
KAYNAK KARE     G15 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Aşağıdaki prompt G15'in birebir kopyası +
                tek ek satır (başlık bandının TONU). Model başlığı YAZMAZ; tipografi post-prodüksiyondur.
KAPAK KARTI     teslimin son 5,0 sn'si (120,0–125,0) · hareketsiz · başlıklı · SAHNE DEĞİL [DERS 4]
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 g15_kaynak.jpg
                bash araclar/zincir_kontrol.sh g15_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
BAŞLIK          "THE OLD ROAD" (İngilizce · 3 kelime) — YAYIN_PAKETI başlığıyla aynı vaadi söyler
ÖLÇÜ            16:9 · 1920×1080 (video içi kart) · küçük resim 1280×720 aynı kaynaktan
⭐ KAPAKTA İKİSİ BİRDEN OKUNUR: yeni viyadükteki ışık çizgisi VE altındaki boş kıvrımlar — biri olmadan kapak
   filmin sorusunu sormaz. Başlık kıvrımları ÖRTMEZ.
⭐ UÇ EKRANI yalnız bu 5 saniyeye konur; final görüntüsü (S14) kapanmaz [YouTube uç ekranı son 5–20 sn'ye izin verir].
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G15 + başlık bandı satırı)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.

```
Photorealistic documentary construction photograph — master cover frame, derived from G15. Horizontal 16:9 time-lapse of a long concrete viaduct being pushed out across a deep alpine valley, seen from a rock spur down the valley; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock spur down the valley, lens 80.0 metres above the river, 380 metres from the viaduct axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one new concrete box-girder viaduct of seven spans carried on five slender piers across the valley, with the old stone arch bridge still standing on the valley floor below it. AT THIS STAGE: the crossing is open and carrying the traffic, and the old road is empty. Along the lit deck at about forty-five percent of frame height a steady stream of vehicles crosses the valley from left to right, their headlights and tail lights drawn into two unbroken white and red trails between the barriers, the lighting columns burning above them. On both slopes the fourteen hairpins lie empty: their pale asphalt, dark guardrail and the old stone arch bridge still catch the last of the light, with no vehicle on them. On the valley floor the pale scar of the lifted haul road is the only mark the work has left.

SITE / BACKGROUND: The valley runs away from the camera between two steep larch-wooded slopes closing in high twin peaks on the skyline. On the valley floor the river comes down toward the camera under a single old stone arch bridge, and the old road crosses the valley in fourteen hairpins cut into both slopes, a pale asphalt band with a guardrail. Beside one hairpin on the left slope stands a single small chapel; on the right rim stands a single tall rock pinnacle. The valley carries exactly one old stone arch bridge and one line of new works; no other bridge, mast or tower stands anywhere from edge to edge. The eye line at exactly half the frame height crosses the rock pinnacle a third of the way up.

THE TIME MOMENT: The traffic that wound through fourteen hairpins now crosses the valley in one straight line of light, and the old road below lies open and empty in the dusk.

COMPOSITION: Horizontal 16:9. The river and the valley floor sit at about twenty-five percent of frame height, the old stone arch bridge at about thirty-four percent left of centre, the twin peaks at eighty-two percent and the rock pinnacle at forty-six to fifty-eight percent. The old stone arch bridge spans about 64 pixels of frame width — one thirtieth — and keeps that width and position in every frame. The lit deck and its two light trails run at about forty-five percent of frame height from about thirteen to eighty-seven percent of frame width; the empty hairpin bands and the stone arch bridge stay readable between about thirty and seventy percent. The crown of the structure sits below the top eighth and the working level above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 281 degrees, elevation 1 degree below the horizon, the sun just set behind the left rim, no cast shadows, the western sky gold and the valley in even blue light. The sun stays outside the frame for the whole shot; its only sign is the shadows. Late November dusk: the twin peaks still catching pink light above fresh snow, the bare rust-brown larch slopes deepening to blue, the river dark.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, the river, machines and vehicles all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay recognisable, trailing light motion blur. Nothing moves at normal speed.

ACTIVITY: The traffic streams across the lit deck from left to right and draws two unbroken light trails along it, while on the slopes the last of the daylight fades from the empty hairpins and the river runs dark under the stone arch bridge. Crew register only as faint soft motion streaks, never as sharp figures.

SITE TEXTURE: New black asphalt under lamplight with a pale kerb line and a dust film at the joints; galvanised barriers and lit columns; grey formed concrete with form-tie bands and rain streaks below; the empty old road a pale asphalt band with a dark guardrail, leaf drift and salt stains at its edges; the pale haul-road scar on the flank; fresh snow on the peaks.

PHYSICS: The deck bears on its permanent bearings on the five pier heads and both abutments and carries the traffic; the barriers are bolted into the deck edge and the lighting columns are planted along it; every vehicle stands on its tyres on the new surface; the old stone arch bridge bears on its rock abutments over the dark river.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The slopes, the hairpins, the stone arch bridge, the chapel, the rock pinnacle and the skyline never change shape, position, size or spacing; every pier, once built, stays where it is. The new crossing is one rigid concrete structure that only ever gains length — nothing already built is removed, moved or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, formwork, scaffolding, container, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic, no tilt-shift blur.
Leave the horizontal band between roughly eighty-four and ninety-three percent of frame height simple and low-contrast across the whole width — open dusk sky only, above the skyline of the twin peaks, with no bright object and no strong edge inside it — so that a title can be set over it in post-production.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Bant YAPININ ÜSTÜNDEDİR, yanında değil: bu filmde yapı (tabliye %45) ve kanıt nesneleri (taş köprü %34,2,
kıvrımlar %30–70) kadrajın ORTA bandını doldurur; boş olan tek yer zirve silüetinin (%82,4) üstündeki gökyüzüdür.
Bant %84–93 arasında, güvenli alanın içinde (üst 60 px = %94,4'ün altında) kalır.

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        THE OLD ROAD (büyük harf · 3 kelime · tek satır)
YÜKSEKLİK    büyük harf ≥ %8 kare boyu = ≥ 86 px @1080 (120 px'e küçülünce ≈ 10 px — okunma eşiği)
             tek satırda genişlik ≈ 850–950 px → 1920 px'lik karede rahat sığar
KONUM        y = 134–307 px (üstten) = kare boyunun %84–93'ü · x = ortalanmış, 200–1720 px arası
             sağ üst 300×100 px'e ve alt 100 px'e girmez; zirve silüetini (%82,4) ÖRTMEZ
KONTRAST     ≥ 4,5:1 — alacakaranlık göğü koyu mavi, metin AÇIK (#E8E4DC, kanal paleti "ana işaret")
             gök yeterince koyu değilse metnin arkasına DÜZ koyu bant (#101315), gradyan yok
YAZI TİPİ    tek ağırlık, geniş harf aralığı, gölge/kontur/parlama YOK
ANİMASYON    yok — kart 5,0 sn hareketsiz
```

---

## ✅ KAPI

```
□ KAPAK KANITI koşuldu (zincir_kontrol çıkışı 0/1) — kapak G15'in dünyasından
□ 120 px testi [MUZIK_VE_KAPAK §2.5]: sips -Z 120 kapak.png --out kapak_120.png
    ⓐ SİLUET: koyu vadinin ortasında yatay bir ışık çizgisi ve altında iki yamaçtaki kıvrım bandı seçiliyor mu
    ⓑ BAŞLIK: "THE OLD ROAD" kelime şekilleri ayırt ediliyor mu (harfler değil, KELİME şekli)
□ başlık bandı güvenli alanın içinde · zirve silüeti açıkta · kıvrımlar açıkta
□ gerçeklik: logo, firma, yer adı, gerçek proje iddiası YOK
```
