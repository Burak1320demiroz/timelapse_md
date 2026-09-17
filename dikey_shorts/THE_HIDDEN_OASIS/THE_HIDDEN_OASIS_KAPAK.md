# 🖼️ THE HIDDEN OASIS — KAPAK KARTI

> ⛔ **KAPAK SIFIRDAN ÜRETİLMEZ.** Usta kareden (G7) türetilir [DERS 30 · MUZIK_VE_KAPAK §2.2].
> Zincirli formatta G7 üretimde İLK üretilen karedir; kapak teslim dosyası ortada yokken hazırdır.
> Aşağıdaki prompt G7 promptunun birebir kopyasıdır; iki fark var: ilk satırdaki kare adı ve başlık bandının
> TONUNU koruyan tek satır. Kapak filmin negatif çekirdeğinin HER maddesini taşır [P1-i]: afiş estetiği, ekstra
> gök, ekstra parlama, suya düşen ekstra ışık "afiş için" serbest değildir.

---

## 0. ÜÇ İŞ, İKİ GÖRÜNTÜ

```
① IZGARA KAPAĞI   kanal ızgarası · "izlemeye devam et" kartı · siluet ailesi ZEMİN (yeni aile önerisi)
                  ⭐ BÖLÜNMÜŞ KAPAK (proje sahibinin dış planından): üst %45 = G0 (yosunlu yeşil havuz) ·
                  alt %55 = G7 (yanan gölet) · ikisi de FİLMİN KENDİ KARELERİ [DERS 30 sağlanır]
② SHORTS KÜÇÜK RESMİ  aynı bölünmüş görüntü · üstüne "SAME POOL?" (TR: "AYNI HAVUZ MU?") — POST PRODÜKSİYON
③ KAPAK KARTI     teslim dosyasının SON 5,0 saniyesi (56,0–61,0) · SAHNE DEĞİL [DERS 4] · YALNIZ G7, bölünmüş değil
KAYNAK KARELER    G7 (usta kare) ve G0 (filmin ilk karesi)
                  yedek: ffmpeg -ss 55.0 -i teslim.mp4 -frames:v 1 g7_kaynak.jpg
                         ffmpeg -ss 00.2 -i teslim.mp4 -frames:v 1 g0_kaynak.jpg
                  ⭐ kaynak kare TESLİM dosyasından alınırsa kırpma sonrası kare kullanılır [KURGU §7]
HAREKET           yok — kart 5 saniye boyunca hareketsiz; altı fener yanık ve SABİT, su duruyor
⚠️ SÜRE           S6 tutuşu 2,0 + kart 5,0 = 7,0 sn sonuç ekranı (%11) — plan §TESLİM YAPISI'nda beyanlı risk
⚠️ BÖLÜNMÜŞ KAPAĞIN RİSKİ  120 px'te iki yarı da küçülür; havuz her iki yarıda da kadrajın en az yarısını
                  doldurmazsa kapak "iki bulanık kare" olur. ⓐ testi bu yüzden İKİ YARIYA AYRI koşulur.
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G7 + başlık bandı ton satırı)

```text
Photorealistic documentary construction photograph — master cover frame, derived from G7. Vertical time-lapse of one abandoned swimming pool rebuilt as a stone-edged garden pond inside a walled courtyard, seen from a balcony above it; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod clamped to the balcony rail of the house on the south side, lens 6.0 metres above the courtyard floor, 5.0 metres from the centre of the pool, bearing 0 degrees, tilt 40 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single stone-edged garden pond in the footprint of the old pool, with a three-step cascade in its far right corner, a gravel beach at its near end and planted pockets along its far rim. AT THIS STAGE: the courtyard is finished and empty. The pond stands full to the third boulder of the near rim, its surface still, carrying the rear wall, the arched niche, the olive canopy and six warm points of light as a reflection. The six low lamps along the right-hand path are alight, steady and warm, and their light lies on the stone rim, on the ferns along the far rim and on the near edge of the water. The cascade runs down all three steps and its rings spread across the pond. The gate in the left-hand wall is shut, the flagstones are swept clean, and the flat cover stone is down over the filter box under the niche.

SITE / BACKGROUND: A single walled courtyard fills the frame, its floor laid with weathered limestone flagstones, and one rectangular pool with rounded corners lies in the middle of it. One old olive tree stands on the left, the only tree inside the walls, its trunk rising from the flagstones at about nine percent of frame width and its canopy across the upper left corner. The rear wall runs straight across the frame, dry stone under worn lime plaster, capped with a flat stone coping level at about seventy-nine percent of frame height, with one arched niche set into it right of centre and a gate in the left-hand wall beside it. Beyond the coping a terraced hillside of olive rows and dry grass climbs to the top of the frame. Apart from the work inside the walls, the courtyard, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge.

THE TIME MOMENT: Blue hour on the first evening, the lights on and nobody left in the courtyard.

COMPOSITION: Vertical 9:16. The arched niche sits right of centre, between fifty-eight and sixty-seven percent of frame width and between sixty-eight and seventy-five percent of frame height; it spans about 99 pixels of frame width — one eleventh — and keeps that width and position in every frame. The near rim of the pool crosses at about thirteen percent of frame height and the far rim at about fifty-two percent, and nothing that proves progress falls into the right eighth or the bottom eighth of the frame. The lit water holds the lower half of the frame between thirteen and fifty-two percent of frame height and the six warm points and their reflections make the brightest marks in the picture.

LIGHTING: Sun azimuth 277 degrees, elevation 4 degrees below the horizon, blue hour, no direct light, an even deep blue sky light over the courtyard with the last warm trace above the hillside, and six warm lamp pools on the stone and the water. The sun stays outside the frame for the whole shot; its only sign is the fading light above the hillside. Mid-September, the end of a dry summer: the hillside grass bleached, the olive canopy freshly pruned.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light on the wall coping, the colour the water carries, the falling sheet on the cascade and the rings it sends out all move at the same accelerated speed. Ten minutes pass across this shot: the warm band drains off the coping and the moving water smooths into a soft blur.

ACTIVITY: The pump lifts a thin sheet of water over the top step of the cascade and the rings it sets off cross the pond and fade against the gravel beach, and the six lamps hold a steady warm glow with their reflections holding under them. No people are present in the courtyard.

SITE TEXTURE: A still dark water surface carrying the reflection of the wall, the olive and six warm points; a wet band on the boulders above the waterline; a thin film of water on the three cascade steps; pale gravel going under at its lower edge; dark watered mulch along the planted band; lichen patches on the dry dolomite; a faint sheen on the stone where the cascade splashes and a pale efflorescence stain on the plaster under the niche; a swept flagstone floor.

PHYSICS: The water bears on the liner and stands against the inside faces of the boulders, and each boulder bears on its mortar pad on the stone coping; the cascade steps are bedded one on the next on their shelf of stone; the six lamp spikes are planted in the ground along the path with their cable tucked under the rim stones; the flat cover stone rests over the filter box.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The walls, the coping, the arched niche, the olive trunk and the hillside never change shape, position, size or spacing; the outline of the pool never changes. Nothing already built is removed, moved or resized; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, container, panel, facade, hoarding, signage, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur.
Keep the band between roughly fifty-two and seventy-six percent of frame height low in contrast across the whole width — the courtyard floor behind the pond, the foot of the rear wall and the plaster above it in even shade, with no lamp highlight and no bright reflection in that band — so that a light title can be set over it in post-production.
Output: 9:16, 4K, no text, no watermark.```

⛔ Prompt hâlâ `no text` der. Başlık kadraja MODELE yazdırılmaz — post-prodüksiyonda dizilir.
⛔ Bölünmüş kapak için AYRI PROMPT YOKTUR: üst yarı G0'ın, alt yarı G7'nin kırpılmış hâlidir. Yeni kare üretilmez.

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon)

```
KART METNİ    THE HIDDEN OASIS
DİL           İngilizce · 3 kelime
SATIR         ⭐ ÜÇ SATIR: "THE" (küçük) / "HIDDEN" / "OASIS" — tek satırda 16 karakter kullanılabilir
              genişliğe (122 → 838 px = 716 px) sığmaz; en uzun kelime 6 karakterdir ve sığar
YÜKSEKLİK     "HIDDEN" ve "OASIS" büyük harf yüksekliği ≥ kare yüksekliğinin %8'i (≥154 px) ·
              "THE" ≈ 80 px · toplam bant ≈ 460 px
KONUM         y = 470–930 px (ÜSTTEN) = kare yüksekliğinin %51,6–75,5'i (alttan) — MUZIK_VE_KAPAK §2.3
              bandının (y 500–1400) üst ucunda · sol 122 px'e ve sağ 242 px'e girmez · alt 484 px UI'ya inmez
              ⭐ NEDEN ORADA: filmin ödülü kadrajın ALT YARISINDADIR (su %13–52, altı sıcak nokta ve
              yansımaları). Başlık aşağı konursa ödülü örter. Yukarıda (%79+) teras yamacı ve zeytin tacı var.
              Geriye avlunun arka şeridi + duvar dibi + sıva kalıyor: mavi saatte en düz, en kontrastsız bant.
              ⚠️ Bedel: KEMERLİ NİŞ (%67,6–74,6) kapakta başlığın altında kalır. Niş filmin çapasıdır ama
              kapağın işi silüet + başlıktır [MUZIK_VE_KAPAK §2.5]; nişin görünürlüğü FİLMDE kanıtlanır.
KONTRAST      ≥ 4,5:1 — METİN AÇIK (#E8E4DC, kanal paleti "ana işaret") · arkasında DÜZ koyu bant (#101315,
              opak ya da ≥ %80), gradyan yok — mavi saatte duvar koyu ama fener havuzcukları kontrastı bozar
YAZI TİPİ     tek ağırlık, geniş harf aralığı, gölge/kontur/parlama YOK
ANİMASYON     yok

KÜÇÜK RESİM METNİ (yalnız yüklenen kapak · karta girmez)
              "SAME POOL?"  (TR alternatif: "AYNI HAVUZ MU?")
              konum: bölünme çizgisinin üstünde, y ≈ 800–980 px · aynı palet · aynı düz bant kuralı
              ⛔ Bu metin videonun İÇİNE girmez; açılış kancası ("CAN THIS BE SAVED?") ayrı bir kurgu
                 katmanıdır ve 0,0–2,0 sn arasında, havuzu ÖRTMEDEN durur.
```

---

## 🔍 KONTROL VE KANITLAR

- [ ] **FİNAL HİYERARŞİ** kapakta: ① yanan su + altı nokta (alt yarı) → ② taş kenar + dikili bant → (③ boş avlu başlığın altında — beyanlı)
- [ ] **IŞIK LAMBALARIN İÇİNDE**: huzme, koni, suda ışık yolu YOK — yalnız havuzcuk ve yansıma; varsa kapak ve G7 birlikte yeniden
- [ ] **120 PX TESTİ** — üç görüntüye: `sips -Z 120 kapak_kart.png --out k_120.png` · `sips -Z 120 kapak_bolunmus.png --out b_120.png` · `sips -Z 120 g0.png --out g0_120.png`
      ⓐ silüet: yukarıdan bakılan avlu + ortada tek dikdörtgen su seçiliyor mu? (ZEMİN ailesi)
      ⓑ bölünmüş kapakta İKİ YARI da havuzu okutuyor mu — üstte yeşil, altta yanan?
      ⓒ başlık: "HIDDEN / OASIS" kelime şekilleri ayırt ediliyor mu? Kaybolursa punto büyür — "olsun" denmez
- [ ] **KAPAK KANITI** [DERS 30]: `ffmpeg -ss 55.0 -i teslim.mp4 -frames:v 1 g7_kaynak.jpg` →
      `bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak_kart.png` → çıkış 2 = kapak başka bir dünya → TESLİM YOK
      ⭐ bölünmüş kapak için İKİ koşu: g0_kaynak ↔ üst yarı, g7_kaynak ↔ alt yarı
- [ ] **SÜRE / KONUM**: kart teslim dosyasının 56,0–61,0 sn'sinde, hareketsiz
- [ ] **GERÇEKLİK**: kapakta logo, firma, yer adı, gerçek bahçe iddiası YOK
