# 🖼️ THE_FIRST_LIGHT — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30] · sahip kararı 19.09.2026 (kapak yalnız GN
karesinden, öncesi/sonrası bölme YOK) · sahip senaryosu TUR 3 (kapak "S20'nin bitmiş kaynak karesi" — depoda G20)

## 0. TEK İŞ: KÜÇÜK RESİM (video içi kapak kartı YOK)

```
KAYNAK KARE     G20 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Prompt aşağıda usta kare (G20) promptunun
                kopyası + tek ek cümle (başlık bandı). Model başlığı YAZMAZ; tipografi post-prodüksiyon.
KAPAK KARTI     ⛔ YOK — teslim 160,0 sn, son kare G20 (hikâye SAPMA ②). Bu dosya yalnız PLATFORM KÜÇÜK RESMİDİR (1280×720).
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
BAŞLIK          "FIRST LIGHT" (İngilizce · 2 kelime) — karenin kendisi bir İLK IŞIK anı: kameraya açılmış yarıkta kırmızı
                ışık, göğe dönük teleskop; başlık olayın adını koyar, ne görüldüğünü söylemez
ÖLÇÜ            16:9 · küçük resim 1280×720 (kaynak 1920×1080 G20 karesi) · ⛔ öncesi/sonrası bölme YOK (sahip 19.09.2026)
⛔ YASAK        filmde olmayan gezegen, uzay aracı, göğü kaplayan dev cisim, ışık sütunu (sahip senaryosu "Kapak" satırı) ·
                ekrandaki gözlem görüntüsü kapağa TAŞINMAZ (S17 iç klibi; kapak dış usta kare)
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G20 + başlık bandı cümlesi)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.
> ⭐ Tercih: önce teslim dosyasının 159,5. saniyesindeki kare kullanılır; yalnız o kare bant için uygun değilse
> aşağıdaki prompt G20'den image-to-image koşulur (G20 referans, değişen tek şey bandın sadeliği).
> Metin `bolum_uretici.py`'nin ürettiği usta kare promptundan betikle kopyalandı (10.10.2026); tek fark baş satır ve bant cümlesi.

```
Photorealistic documentary site photograph — cover frame made from master frame G20. Horizontal 16:9 time-lapse of an old mountain-top observatory restored above a sea of cloud; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 800.
Camera: MAIN STATION — fixed tripod bolted to a high rock knoll to the south, lens 28 metres above the summit ground, 64 metres from the observatory's centre along the lens axis, bearing 0 degrees, tilt 13 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a mountain-top observatory: a low round drum of pale grey granite, 24 metres across and 4 metres high, with an arched timber door and stone steps, under a copper dome of the same width that turns on a steel ring rail on the wall top and has one observing slit closed by a single copper shutter; inside, a large telescope with a dark grey fork mount and a long pale white tube; on the right a paved terrace with a steel railing at the cliff edge. AT THIS STAGE: everything is finished. The copper dome sits on the ring rail on top of the drum, its slit standing open in the middle of its face, turned towards the camera: a tall band of dim red light from the base to the crown, with the pale white tube of the telescope inside it, tilted up to the sky; the granite drum stands washed clean, a bright new steel ring rail on its wall top and an arched timber door in front. A path of wide pale new stone slabs and new stone steps lead from the work pad to the door, the low path lamps beside them lit low. On the right an old paved terrace runs to the cliff edge, a new steel railing along its whole edge. Two people stand still at the railing at the cliff edge, small dark figures against the sea of cloud, no readable faces; the work pad lies raked clean and empty.

SITE / BACKGROUND: A bare summit ridge of grey rock and gravel. All round the summit a sea of white cloud fills the valleys far below, its surface flat and level. Two far dark rock peaks rise out of it on the level horizon: a sharp twin-summit peak left of centre and a long flat-topped ridge right of centre. A gravel service road climbs from the left edge to a flat gravel work pad left of the drum. The granite of the drum is laid in long low courses of squared blocks with thin dark joints. A single wind-bent mountain pine with a flat dark crown stands on a bare rock spur at the right end of the summit. Behind the observatory the summit ends in a cliff edge.

THE TIME MOMENT: Five past six in the evening, deep blue hour, autumn: the restored observatory looks at the sky.

COMPOSITION: Horizontal 16:9, the camera looking down 13 degrees, the level horizon at about seventy-seven percent of frame height. The mountain pine spans about 150 pixels of frame width — about one thirteenth — from about 1652 to 1805 pixels from the left, its crown top at about forty-nine percent, and keeps that width and position in every frame. The stone drum spans about 920 to 1400 pixels from the left, its front wall from about eighteen to twenty-five percent of frame height. The copper dome sits on the drum, its crown at about fifty-five percent of frame height. The slit runs up the middle of the dome face, from about 1125 to 1195 pixels from the left. The two people stand at the railing at about 1600 pixels from the left, about thirty pixels tall. Nothing that proves progress falls into the bottom tenth or the top-right corner of the frame. The deep blue sky above the far peaks, from the top edge down to about a sixth of the frame height, stays clear, calm and even, with no cloud edges — an empty band.

LIGHTING: Sun azimuth 258 degrees, elevation 8 degrees below the horizon, below the horizon behind the camera on the left, outside the frame, so there is no direct sun: deep blue hour, the sky deep clear blue with the first bright stars, the sea of cloud below pale blue-grey, the stone and the copper cool and dim but clearly readable. Autumn: a clear deep sky with a few thin high clouds. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crew all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift in one smooth flow, machines move fast with light motion blur. Nothing moves at normal speed.

ACTIVITY: The two people stand still at the railing; the dim red light holds steady in the open slit and the sea of cloud lies calm below. People register only as faint soft motion streaks while they walk; standing still they are small dark figures, no readable faces.

SITE TEXTURE: Copper gone deep warm brown in the dusk, pale grey granite cool and blue-grey, a faint red glow along the edges of the open slit, raked gravel with the faint print of old tyre tracks, a thin film of dust on the new paving, small warm pools of light from the low path lamps. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The dome sits on the ring rail on the drum, its shutter seated back in its runners. The railing posts are bolted to the paving at the cliff edge, and the two people stand on the paving.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The far peaks, the horizon, the cliff edge, the service road and the pine on its rock spur never change shape, position, size or spacing, and the sea of cloud stays at the same level. The summit holds exactly one building site, this one, and exactly one dome. Nothing already built or restored is removed or resized; no opacity fades. No beams of light into the sky. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Kamera 13° aşağı baktığı için gök bandı dar: ufuk üstten 244'te, iki uzak tepe onun biraz üstüne çıkar. Bant tepelerin
ÜSTÜNE konur (üst 60 px oynatıcı bandının altında, üstten ≈70–170). Kubbe tepesi (487) ve yarık (487–807) bandın çok altında;
sağdaki çam (x 1652–1805 · 551–870) ve korkuluktaki iki kişi (x ≈1600) bandın ALTINDA kalır. Sağ üst 300×100 px'e girmez ·
süre damgası sağ alttadır; yarık (x 1125–1195) ve iki kişi ona düşmez [A15-c]. ⚠️ Tepelerin gerçek yüksekliği usta karede
ölçülür; bant tepelere değiyorsa punto küçülmez, bant yukarı (≥ 60 px) kayar.

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        FIRST LIGHT (büyük harf · tek satır · 2 kelime)
YÜKSEKLİK    büyük harf ≥ %8 kare boyu = ≥ 86 px @1080 (1280×720'de ≥ 58 px; 120 px'e küçülünce ≈ 10 px — okunma eşiği)
KONUM        x ≈ 560–1360 px · y ≈ 70–170 px (1080 ölçeğinde) · iki uzak tepenin üstünde · sağ üst 300×100 px'e ve
             alt 100 px'e girmez
RENK         sıcak amber #F2A03D (kanal vurgusu — KANAL_KIMLIGI) · koyu mavi göğe karşı kontrast ≥ 4,5:1
             (yetmezse bandın arkasına %35 opaklıkta düz koyu lacivert şerit — gradyan değil)
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ silüet (koyu mavi gökte yarım küre kubbe + ortasında sıcak
                 kırmızı dikey çizgi) okunuyor mu · ⓑ KELİME şekli ayırt ediliyor mu · ⓒ sağ alta kara kutu (süre damgası)
                 konunca kaybolan bir şey var mı: YOK olmalı
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez; ⓑ kayboluyorsa punto büyür
                 ⭐ aynı test S0'ın 0. karesine de: havadaki yeşil kubbe 120 px'te okunuyor mu? (açılış nesnesi —
                    kubbe ≈30 px genişlik; bulut denizinin beyazına karşı koyu yeşil leke olarak okunmalı)
                 ⚠️ 120 px'te yarık ≈4 × 20 px — küçük resimde bir SICAK ÇİZGİ olarak okunur; ayrıntı değil, renk farkı taşır
                    (koyu mavi + kırmızı)
② KAPAK KANITI  zincir_kontrol.sh g20_kaynak.jpg kapak.png → çıkış: ⬜ (üretimden sonra)   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → yabancı dönüm noktasını (tüpün geri gelip
                ilk kez hareket etmesi + yarığın açılıp kubbenin dönmesi + ekrandaki ilk görüntü) söyleyebiliyor mu: kısmen —
                kapak açık yarığı gösterir (sahip kuralı: kapak = GN); ekrandaki görüntü ve kubbenin dönüşü saklı kalır [§3.3].
④ BAŞLIK = VAAT  kapak: "bulutların üstünde açık yarığıyla göğe bakan gözlemevi" · başlık: "ilk ışık" — vaat aynı ✓
```
