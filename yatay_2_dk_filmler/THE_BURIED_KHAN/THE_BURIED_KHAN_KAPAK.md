# 🖼️ THE_BURIED_KHAN — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30] · sahip kararı 19.09.2026 (kapak yalnız GN
karesinden, öncesi/sonrası bölme YOK) · hikâye onayı 09.10.2026 ("Kapak bu kareden" — S14)

## 0. TEK İŞ: KÜÇÜK RESİM (video içi kapak kartı YOK)

```
KAYNAK KARE     G15 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Prompt aşağıda usta kare (G15) promptunun
                kopyası + tek ek cümle (başlık bandı). Model başlığı YAZMAZ; tipografi post-prodüksiyon.
KAPAK KARTI     ⛔ YOK — teslim 120,0 sn, son kare G15 (format varsayımı, hikâye SAPMA ⑬). Bu dosya yalnız PLATFORM
                KÜÇÜK RESMİDİR (1280×720).
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 119.5 -i teslim.mp4 -frames:v 1 g15_kaynak.jpg
                bash araclar/zincir_kontrol.sh g15_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
BAŞLIK          "THE BURIED KHAN" (İngilizce · 3 kelime) — viral kanca başlık ile karenin çelişkisi: başlık "gömülü" der,
                kare açık kapısından ışık taşan, bütün bir yapıyı gösterir (THE SWALLOWED BUS kalıbı)
ÖLÇÜ            16:9 · küçük resim 1280×720 (kaynak 1920×1080 G15 karesi) · ⛔ öncesi/sonrası bölme YOK (sahip 19.09.2026)
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G15 + başlık bandı cümlesi)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.
> ⭐ Tercih: önce teslim dosyasının 119,5. saniyesindeki kare kullanılır; yalnız o kare bant için uygun değilse
> aşağıdaki prompt G15'ten image-to-image koşulur (G15 referans, değişen tek şey bandın sadeliği).
> Metin `bolum_uretici.py`'nin ürettiği usta kare promptundan betikle kopyalandı (09.10.2026); tek fark baş satır ve bant cümlesi.

```
Photorealistic documentary site photograph — cover frame made from master frame G15. Horizontal 16:9 time-lapse of a long stone caravanserai dug out of the desert sand and repaired; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 800.
Camera: MAIN STATION — fixed tripod bolted to the top of a low dark rock outcrop on the open desert floor, lens 6 metres above the desert floor, 67 metres from the face of the caravanserai along the lens axis, bearing 20 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a long two-storey caravanserai of honey-coloured sandstone, 60 metres wide, behind a stone-paved forecourt: a blank lower storey, an open arcade of sixteen round arches above it, a tall gateway frame around a pointed arch at its centre with a pair of heavy timber doors, and a round corner tower with a domed cap at each end. AT THIS STAGE: everything is finished. all sixteen iron lanterns in the arcade are lit, every arch glowing warm, and a soft warm light falls from them onto the face of the stone. The two heavy timber doors stand open inward, and warm light from the courtyard inside pours out through the pointed arch in a long bright fan across the forecourt. The restored caravanserai stands complete — its honey-coloured stone face, the unbroken arcade of sixteen round arches, the paler new stone of the rebuilt section right of the gateway, the band of carved geometric relief round the pointed arch, the pair of heavy dark timber doors and the two domed corner towers. A low windbreak berm of sand runs along the right side, with a line of palm-frond fences along its crest, sand drifted against the fences. Three people stand still on the threshold of the open gateway beside a loaded two-wheeled hand cart, small dark figures against the warm light, no readable faces.

SITE / BACKGROUND: A wide flat desert of pale gold sand and grey gravel under a dead level horizon. Far away on the right a single flat-topped mesa of red-brown rock sits on the horizon. On the left a single dead acacia tree with a flat crown of bare grey branches stands on a low dark rock outcrop. Low sand ripples and scattered dark stones cover the foreground.

THE TIME MOMENT: Twenty past seven in the evening, deep blue hour, autumn: the caravanserai is open again.

COMPOSITION: Horizontal 16:9. The camera is level: the horizon runs dead level at exactly half the frame height. The dead acacia tree spans about 105 pixels of frame width — about one eighteenth — from about 154 to 259 pixels from the left, its crown top at about fifty-four percent of frame height, and keeps that width and position in every frame; the mesa sits on the horizon from about 1660 to 1840 pixels. The caravanserai spans from about 330 to 1590 pixels from the left, from its foot at about thirty-nine percent of frame height to its wall top at about fifty-five percent; the gateway frame rises to about sixty-six percent. The pointed arch of the gateway stands at the centre, from about 912 to 1008 pixels from the left, its top at about fifty-three percent of frame height. The three people stand at about 910 pixels from the left, about thirty pixels tall. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame. The deep blue sky above the gateway frame, from the top edge down to about a third of the frame height, stays clear, calm and even, with no cloud edges — an empty band.

LIGHTING: Sun azimuth 297 degrees, elevation 6 degrees below the horizon, below the horizon on the left, outside the frame, so there is no direct sun: deep blue hour, the sky deep clear blue with a last pale band low on the left, the sand and the stone cool blue-grey. Autumn: a clear deep sky with a few thin high clouds, the air clear again and the mesa sharp on the horizon. The sun stays outside the frame.

TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the doors, the people and the lamplight move at their real pace; nothing is accelerated.

ACTIVITY: The three people stand still on the threshold beside the hand cart, small dark figures with no readable faces; the lanterns burn steadily and the warm light lies across the forecourt.

SITE TEXTURE: Honey-coloured stone gone soft amber in the lamplight, warm light pooling on the worn grey paving, the pale new blocks of the repair dulled by dust, a thin skin of drift sand along the foot of the walls, pale broom streaks across the paving, wind ripples on the berm in cool blue light. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The open doors are seated on iron pivots set in the threshold stone. The hand cart rests on its two wheels on the paving, and the three people stand on the threshold. The lanterns hang from an iron hook in each arch.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The flat-topped mesa on the horizon keeps exactly the same silhouette in every frame; the dead acacia tree, its rock outcrop and the dead level horizon never change shape, position, size or spacing; heat shimmer only near the ground. The desert holds exactly one building site, this one. Nothing already built or uncovered is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Yatayda yapı alçak ve uzun (x 329–1591 · üstten 368–655): boş kalan yer kapı çerçevesinin üstündeki mavi saat göğüdür
(üstten 0–368) — bant oraya konur (üst 60 px oynatıcı bandının altında, üstten ≈80–190). Soldaki akasya (x 154–259 ·
495–585) ve sağdaki masa dağı (x 1660–1840 · 518–540) bandın ALTINDA kalır. Sağ üst 300×100 px'e girmez · süre damgası
sağ alttadır; açık kapı (x 912–1008) ve eşikteki üç kişi (x ≈910) ona düşmez [A15-c].

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        THE BURIED KHAN (büyük harf · tek satır · 3 kelime)
YÜKSEKLİK    büyük harf ≥ %8 kare boyu = ≥ 86 px @1080 (1280×720'de ≥ 58 px; 120 px'e küçülünce ≈ 10 px — okunma eşiği)
KONUM        x ≈ 420–1500 px · y ≈ 80–190 px (1080 ölçeğinde) · kapı çerçevesinin tepesinin (368) çok üstünde · sağ üst
             300×100 px'e ve alt 100 px'e girmez
RENK         sıcak amber #F2A03D (kanal vurgusu — KANAL_KIMLIGI) · mavi saat göğüne karşı kontrast ≥ 4,5:1
             (yetmezse bandın arkasına %35 opaklıkta düz koyu lacivert şerit — gradyan değil)
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ silüet (mavi gökte uzun alçak cephe + ortada sıcak ışıklı
                 kapı + fener sırası) okunuyor mu · ⓑ KELİME şekli ayırt ediliyor mu · ⓒ sağ alta kara kutu (süre damgası)
                 konunca kaybolan bir şey var mı: YOK olmalı
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez; ⓑ kayboluyorsa punto büyür ya da kelime azalır
                 ⭐ aynı test S0'ın 0. karesine de: kum tepesi ve üç taş uç 120 px'te okunuyor mu? (açılış nesnesi —
                    kapı çerçevesinin ucu 120 px'te ≈14 × 4 px; okunmuyorsa sahibe döner)
                 ⚠️ 120 px'te kapı ≈6 × 9 px, fener sırası ≈64 px'lik ince sıcak çizgi — küçük resimde ışıklı kapı bir SICAK
                    NOKTA olarak okunur; ayrıntı değil, renk farkı taşır (mavi saat + amber ışık).
② KAPAK KANITI  zincir_kontrol.sh g15_kaynak.jpg kapak.png → çıkış: ⬜ (üretimden sonra)   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → yabancı dönüm noktasını (kumun altından çıkan
                yapı + kapının açılışı) söyleyebiliyor mu: kısmen — kapak bitmiş yapıyı gösterir (sahip kuralı: kapak = GN);
                yapının ne kadar derin gömülü olduğu ve kapının açılış anı saklı kalır [§3.3].
④ BAŞLIK = VAAT  kapak: "çölde kapısı açık, ışıklı bir kervansaray" · başlık: "gömülü" — çelişki kancadır, vaat aynı ✓
```
