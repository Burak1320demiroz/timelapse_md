# 🖼️ FIRST SLICE — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok; ⭐ kartta ateş
   çıtırtısı SÜRER [DERS 100]. YouTube Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK §8].
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi, zincirin İLK üretilen karesi (metinden)
           [DERS 30 · 91 · 99 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⛔ GPT paketindeki "kırmızı fırın + ilk pizza" kapağı G8'in KENDİSİDİR — kompozisyon planda kurulur, sonradan değil.
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      ⭐ İKİ KEZ [DERS 99]: (1) METİNSİZ G8'e, G8 ONAYINDAN ÖNCE · (2) bitmiş kapağa, yüklemeden önce —
           python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           + paketin önerdiği ~180 px genişlik bakışı (140 px küçükle birlikte)
METİN      FIRST SLICE  (2 kelime · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   alacakaranlıkta küçük bir retro pizzacı: beyaz seramikli köşede kırmızı mozaik kubbe fırın, ağzında turuncu
                  ateş · ön planda kırmızı tezgâhın krem tablasında dilimlenmiş pizza ve küçük beyaz tabakta İLK DİLİM ·
                  siyah-krem dama zemin · arka duvarda çizgili tente altında çelik mutfak · sağda kırmızı bank, sıcak lambalar ·
                  koyu tavan ve kırmızı üst duvarlar
BAŞLIKTA YAZAN    FIRST SLICE

KANCA             "bu dükkân nasıl kuruldu?" — başlık İLK'i vaat eder; kapakta görünmeyen şey başlangıçtır (yağlı tamirhane).
                  Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ ATEŞ + PİZZA — kadrajın en parlak noktası (ağız, y 1018–1085) ile en sıcak yüzeyi (pizza, y ~1240) aynı
                  dikey hatta, üst üste. 140 px'te bile "fırın ve pizza" okunur [P3-b: kontrast].
İKİNCİ OKUMA      kırmızı kubbe — "bu fırını buraya biri kurdu"
ÜÇÜNCÜ OKUMA      sırtı dönük figür — "biri az önce ilk pizzayı çıkardı"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① lastik kafesi ve yağlı garaj ② fırının parça parça kurulması ③ hamurdan dilime.
⛔ Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   koyu tavan                0–723     (kameraya yakın tavan üstte)
   sarkıt kabloları          619–865   x ≈ 833 (ince çizgi)
   ⭐ BAŞLIK KUTUSU           560–770   x 180–900 (kılavuz §3 "film adı kutusu")
   tavan–arka duvar çizgisi  674–723   (sağda 674, solda 723)
   yüksek pencereler (mavi)  621–814   x 949–988 — kutunun DIŞINDA
   baca dirseği              837       x 297–359
   tente                     840–893   x 447–731
   sarkıt lambalar (yanık)   ≈ 865     x ≈ 833
   seramik üstü              900–907
   kubbe tepesi              952       x 297
   figür başı                968       x 626
   ⭐ fırın ağzı + ATEŞ        1018–1085 x 259–329
   kubbe yanları             1035–1039 x 212–387
   cam vitrin üstü           1100–1106 x 134–285
   ⭐ pizza tahtası            1238–1247 x 422–539
   ⭐ İLK DİLİM tabağı         ≈ 1266    x ≈ 590–625
   tezgâh tablası            1247–1299 x 64–664
   tezgâh ön yüzü            1299–1723 (kırmızı, kanıt değil)
   alt UI bandı              1440–1920 (tezgâh önü + dama zemin — kanıt yok)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · fırın + ateş ✅ · pizza + dilim ✅ · mutfak + tente ✅ · figür ✅
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, ateşi ve pizzayı tam taşır · 4:5 (285–1635) ve 3:4 (240–1680) tezgâh önünü de taşır.
⭐ PAKET ↔ GEOMETRİ: paket "ateş başlığın üstünde, pizza altında" diyordu. 1,8 m kameradan fırın ağzı y ≈ 1050'ye düşer; başlık
   kutusu DERS 94 · 99 gereği y 560–770'te kalır. Sonuç yukarıdan aşağı: BAŞLIK → ATEŞ → PİZZA. Başlık ağzı kapatmaz, pizza en
   altta — paketin iki şartı tutar, sırası değil.
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      FIRST SLICE — İKİ SATIR:  "FIRST"  /  "SLICE"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — koyu tavan + tavan çizgisi + kırmızı üst duvar üstünde; baca dirseği (837)
           ve tente (840) kutunun 67–70 px ALTINDA
           satır 1 "FIRST"  y ≈ 580–670 · satır 2 "SLICE"  y ≈ 680–770
PUNTO      ⭐ iki satırda ≈ 92–100 px yazı boyu (kılavuz §5); gerçek yazı sınırları 720 × 210'u AŞMAZ
           kalın, yuvarlak hatlı retro sans-serif (paket: "kalın, krem renkli retro harfler") · tek ağırlık
RENK       krem #F2E6CC + ince koyu kırmızı gölge (paket önerisi) · arka plan koyu tavan + koyu kırmızı duvar → kontrast
           ölçülür; 4,5:1'i geçmezse gölge koyulaştırılır, tavan karartılmaz [kılavuz §5]
⛔ Başka kelime yok: "pizza" · "garage" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada tezgâh önü ve dama zemin var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX + 180 PX  kapak_prova.py küçükleri + 180 px genişlik → ⓐ "fırın ateşi + pizza" ayrışıyor mu ⓑ iki satır okunuyor mu
                   ⓒ sağ alt köşe boş mu · ⭐ aynı test G0'a: "yağlı tamirhane + lastik kafesi" 140 px'te okunuyor mu
                   · seçilmiyorsa ayrıntı AZALTILMAZ, G8 yeniden üretilir (paket: "ayrıntıları azaltalım")
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, ateş ve pizza TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "sıcak, çalışan bir pizzacı" diyor mu — "vitrin render'ı" diyorsa G8 yeniden
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki dükkân = finaldeki dükkân [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + FIRST SLICE      yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ             G8 tam kare — sahip kararı
ⓒ METİNSİZ              ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün ve İLK kapak_prova'nın koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok.
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/marka adı yok.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     This Filthy Garage Became a Pizza Shop      (38)   ⭐ sahibin paketindeki başlık
② KISA   From oil stains to the first slice          (34)
③ SORU   What would you build in this old garage?    (40)
```

> ⚠️ ① TOTAL RESET'in ① adayıyla aynı kalıp ("This Filthy … Became a …"). İkisi arka arkaya yayınlanırsa biri ② ya da ③'e
> döner — karar sahibin. Üçü de 40 karakter tavanında ya da altında.

**Açıklama:**

```
A filthy repair garage is turned into a working pizza shop in a single day: the tyres, the rusty benches and the old
metal sheets go out, the walls turn red and cream, a dark ceiling, white tiles and a checkerboard floor go in. A red
dome oven is built piece by piece in the corner, a counter and a steel kitchen follow — and at dusk the fire is lit
and the first pizza comes out.

One day in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a scene. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real shop, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #renovation #pizzashop #pizzaoven #garageconversion
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> "No cuts inside a scene": S2 ve S3'ün içinde ara kare dikişi var (aynı sahne, iki klip) — "inside a shot" yerine bilerek.

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
garage conversion, pizza shop build, pizza restaurant renovation, wood fired pizza oven, pizza oven build, dome oven, retro pizzeria, checkerboard floor, restaurant fit out, garage renovation, commercial kitchen, shop renovation, renovation timelapse, construction timelapse, ai timelapse, ai video, timelapse, pizza oven bild, garage convertion
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan
> aramalarda işe yarar ("pizza oven bild" · "garage convertion" bu yüzden bilerek var). Marka/firma adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
A wood-fired dome oven bakes fast because of where its heat lives: the fire burns beside the pizza, the low dome bounces
heat down onto the top, and the firebrick floor, soaked with heat for an hour or more, cooks the base from below — which
is why a thin pizza is done in about a minute and a half and has to be turned once with the peel. The dome went in as
precast sections on a block plinth with an insulated hearth because a hand-built dome takes days of drying before its
first fire. And the order of the day was not random: pipes before paint, ceiling before floor, floor before the oven,
so that nothing heavy or dusty ever crossed a finished surface.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). "About a minute and a half" genel bir aralıktır (60–90 sn) — kesin
> sayı iddiası yok. Yorum tuzağı sorusu YOK [A33-b].

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: TOTAL RESET ve THE POOL ROOM ile arka arkaya ÖNERİLMEZ (üç iç mekân, aynı başlık kalıbı; öneri, kural
   değil) [YAYIN_PLANI §3].
