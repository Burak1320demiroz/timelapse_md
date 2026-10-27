# 🖼️ THE READING CAR — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99]
METİN      ABANDONED TRAIN CAR / BECOMES A BOOKSHOP  (6 kelime · İKİ satır · İngilizce · sahip seçimi 25.10.2026)
           ⚠️ KAPAK_STIL_KILAVUZU §1 "film adı 1–3 kelime" der; bu film sahibin seçtiği yayın başlığını kartta taşır — beyanlı sapma.
              Kısa yedek (sahip isterse): THE READING CAR (3 kelime, tek satır) — §5 ⓓ.
```

---

## 0. ⭐ STİL KARTI [KAPAK_STIL_KILAVUZU §7]

```
STİL KARTI  [KAPAK_STIL_KILAVUZU]
BANT        Ü · y 560–770 · x 180–900 · sakin alan: YAKIN KOYU VERNİKLİ AHŞAP TAVAN (Y 2,9–6,1 m) — plan kadraj kilitleri
            ⚠️ kaburga 2 (py 730) ve kaburga 1'in kemer kolları banttan geçer: koyu çelik, koyu ahşap üstünde (düşük kontrast, beyanlı)
IŞIK        reçete R1 (mavi saat + sıcak lamba) · varyant I0 (GN'nin kendi ışığı) — en parlak şey sarkıtların altındaki sıcak ışık
            havuzları; bant KOYU kalır ("their dark shades keep the light below them and the near wooden ceiling stays dark")
STİL        S4 — iki satır · yazı tipi Anton (kılavuz varsayılanı; ⚠️ kanal yazı tipi sahip kararı bekliyor) · renk #E8E4DC · vurgu kelimesi —
METİN       ABANDONED TRAIN CAR / BECOMES A BOOKSHOP (6 kelime · 2 satır) · büyük harf ≈ 80–84 px (≥ 78) — 19 karakterlik satır 720 px'in
            %90–100'ünü doldurur; iki satır + sıkı aralık ≈ 165–175 px ≤ 210
KONTRAST    ⬜:1 (≥ 4,5) — koyu ahşap zeminde yüksek beklenir; ölçülür (§4.4 betiği · x0 180 y0 560 x1 900 y1 770) · koyu geçiş: gerekirse
KANIT       zincir_kontrol ⬜ · nirengi ⬜ px · nesne sayımı ⬜ (sekiz kitaplık · dört sarkıt · beş kaburga · bir müşteri)
PROVA       PROVA_PANOSU ⬜ · 1:1 başlık tam ⬜ · 140 px üç soru ⬜
```

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   tek nokta perspektifle uzanan eski bir vagonun koridoru: iki yanda tavana kadar koyu yeşil kitaplıklar, renk renk kitapla
                  dolu · ortada dört koyu abajurlu sarkıt lambanın altında sıcak ışık havuzları · açık meşe zemin · solda deri okuma koltuğu ·
                  sağda pirinç raylı kayar merdiven · dipte açık kapı ve ardında koyu mavi alacakaranlık · sağ üçüncü kitaplığın önünde
                  elinde açık kitapla duran tek müşteri · pencere sıraları mavi · üstte koyu ahşap tavan ve kaburgaları (başlık)
BAŞLIKTA YAZAN    ABANDONED TRAIN CAR / BECOMES A BOOKSHOP

KANCA             "bu bir hurda vagon muydu?" — başlık "abandoned" der; kapak lambalı, dolu bir kitapçıyı gösterir. Görünmeyen şey hurdadır
                  (yırtık koltuklar, çürük tahta, kırık cam). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ LAMBALI KİTAP KORİDORU — sıcak ışık havuzları + iki yanda renk şeritleri, koyu mavi pencereler arasında; 140 px'te bile
                  "kitaplarla dolu bir koridor" okunur [P3-b: kontrast].
İKİNCİ OKUMA      pencere sırası + kavisli tavan + kaburgalar: "burası bir vagon"
ÜÇÜNCÜ OKUMA      elinde kitapla müşteri: "dükkân açık"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① yırtık koltuklu, çürük tahtalı, kırık camlı hurda vagon ② koltukların, tahtaların çıkışı ve rafların katman katman gelişi
   ③ lambaların yandığı an ve müşterinin kitabı çekmesi.
⛔ Kapak G7 DEĞİLDİR: G7'de lambalar sönük, müşteri kapıda, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   kaburga 1 (tepe)                    499        eksende, kollar kadraj kenarına
   ⭐ BAŞLIK KUTUSU                     560–770    x 180–900 — yakın koyu ahşap tavan (Y 2,9–6,1) · kaburga 2 tepesi py 730'da
   sarkıt lambalar (kablo → abajur)     776–917    eksende, 52 → 24 px — kutunun ALTINDA
   alın duvarı + açık kapı (mavi)      878–1115   x 432–648 · kapı x 505–575
   uzak kitaplıklar                    888–1266   iki yanda, ön yüzleri dar şerit
   ⭐ müşteri + açık kitap              954–1171   x 569–615
   tezgâh + masa lambası               1027–1122  x 427–500
   yakın kitaplık 1 (sol / sağ)        849–1433   x 211–348 / 732–869
   ⭐ okuma koltuğu                     1242–1685  x 111–349
   meşe zemin (ışık havuzları)          1115–1920  kadraj boyu
   alt UI bandı                        1440–1920  (zemin — yardımcı doku)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · müşteri ✅ · kapı ✅ · sarkıtlar ✅ · uzak kitaplıklar ✅ · tezgâh ✅ · yakın
   kitaplıklar çekirdeğin kenarında · koltuğun üst yarısı çekirdekte — beyanlı
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, sarkıtları, kapıyı, müşteriyi, uzak ve yakın kitaplıkları, koltuğun üstünü taşır · 4:5 (285–1635)
   ve 3:4 (240–1680) koltuğun tamamına yakınını ve zemindeki ışık havuzlarını da taşır.
⚠️ En yakın sarkıtın kablosu py 776'da başlar — başlığın alt satırı en çok py ≈ 760'a iner; ışık havuzu tavana vurursa G8 yeniden (plan PİLOT a).
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 + KAPAK_STIL_KILAVUZU §4 ölçüleriyle

```
METİN      ABANDONED TRAIN CAR / BECOMES A BOOKSHOP — İKİ SATIR (S4), ORTALI, x = 540
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — yakın koyu ahşap tavan · satırlar y ≈ 578–662 ve ≈ 672–756 · yazı lambaları, kapıyı
           ve müşteriyi örtmez
PUNTO      Anton, büyük harf ≈ 80–84 px (≥ 78 eşiği) · uzun satır "ABANDONED TRAIN CAR" (19 karakter) bant genişliğinin %90–100'ü · satır
           aralığı punto × 0,95 · gerçek yazı sınırları 720 × 210'u AŞMAZ, aşarsa punto küçülür; eşiğin altına düşerse kısa yedeğe geçilir
           (THE READING CAR) — harf aralığı daraltılmaz · tek ağırlık · parlama / kontur YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan koyu vernikli ahşap → kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse
           başlığın arkasına #101315 yumuşak koyu geçiş (%35–50) [KAPAK_STIL §4.4]
⛔ Başka kelime yok: "AI" · "timelapse" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada meşe zemin var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "lambalı kitap koridoru" ayrışıyor mu ⓑ başlık iki satırda okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "hurda vagon koridoru" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, müşteri ve kapı TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "eski bir vagonun içinde kitapçı" diyor mu — "kütüphane koridoru", "render", "dekor" diyorsa G8
               yeniden (pencere sırası ve kaburgalar okunmuyor demektir); kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki müşteri = finaldeki müşteri [MUZIK_VE_KAPAK §5]
⑦ KONTRAST     KAPAK_STIL §4.4 betiği · bant x 180–900 · y 560–770 → ≥ 4,5:1
```

## 5. Dört varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + ABANDONED TRAIN CAR / BECOMES A BOOKSHOP   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur (sahip seçimi)
ⓑ BAŞLIKSIZ            G8 tam kare — sahip kararı
ⓒ METİNSİZ             ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
ⓓ KISA YEDEK           G8 + THE READING CAR (tek satır, S1) — yalnız sahip isterse ya da ⓐ 78 px eşiğini tutturamazsa
⛔ DÖRDÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (kırpmalar PROVA'dır — kapak_prova.py).
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/marka adı yok · ≤ 40 karakter.
```

**Başlık — sahip seçti (25.10.2026):**

```
⭐ SEÇİLEN   Abandoned Train Car Becomes a Bookshop      (38)   paketin ana önerisi · sahip seçimi
   yedek    From Scrap Wagon to Bookshop                (28)   paketin alternatifi
   yedek    What Will This Old Carriage Become?         (35)   planın MERAK SORUSU
```

> Seçilen başlık 40 karakterin altında; KILAVUZ_REHBERI §6'nın "≤ 5 kelime" testini bir kelimeyle aşar (beyanlı). "Train car"
> kelimesi YALNIZ başlıkta ve kartta durur; promptlarda vagon "old railway carriage" diye geçer (ray/lokomotif çağrışımı — plan
> TASARIM ⑲).

**Açıklama:**

```
An abandoned railway carriage: torn seats, rotten floorboards, broken windows. Two workers carry it all out through one narrow door,
strip it to bare steel and fit it out stage by stage — oak floor, new glass, tall green bookcases, books shelf by shelf.
Then the evening comes.

Weeks of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real building, no real railway, no real shop and no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #bookshop #traincar #renovation #tinyshop
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> Açıklama lambaları ve müşteriyi ANMAZ ("Then the evening comes.") — spoiler bütçesi. "Weeks of work" sahneler arası takvim
> atlamasının beyanıdır (plan SAHA satırı).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
train car bookshop, railway carriage conversion, abandoned train car, bookshop renovation, tiny bookshop, carriage renovation, construction timelapse, ai timelapse, ai video, timelapse, the reading car, train car bookstore, bookshp
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("bookshp" bu yüzden bilerek var). Gerçek yer/firma/marka adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Old railway carriages are often converted into cafés, cabins or small shops. The usual first steps are to strip the seats and the old
timber floor down to the steel underframe, deal with rust and old paint, and replace the windows; anything tall, like a bookcase, has to
be designed to come in through a narrow end door in pieces or on its side, because the carriage itself cannot be opened up.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("often · usual"); belirli ürün, ölçü, yük ya da süre
> iddia edilmez (ÇIKARIM, genel bilgi). Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | hurda vagondan kitapçıya | nasıl, hangi sırayla, ışığın yanışı, müşteri |
| kapak | bitmiş, lambalı kitapçı + müşteri + başlık | yırtık koltuklar, çürük tahta, katmanların gelişi, ışık anı |
| ilk 2 sn | hurda koridor, kaldırılan koltuk, dipte açık kapı | vagonun neye dönüşeceği |
| açıklama | koltuklar, tahta, cam, meşe, yeşil kitaplıklar, kitaplar, "akşam gelir" | lambalar, ilk müşteri |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (mavi saatte lambalar yanar, ilk müşteri bir kitap çeker) kapak dışında
söyleyemez → ✅ (taslak; kurgudan sonra tekrar). ⚠️ Kapak müşteriyi gösterir; lambaların yandığı AN ve kitabın çekilişi yine saklıdır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: İÇ MEKÂN (bekleyen) ailesi — THE LAST STOP (araç içi yaşam alanı), THE TURNTABLE (aynı koridor kadrajı) ve THE HIDDEN LOFT
   (iç mekân, ışıklı final) ile ARDIŞIK YAYINLANAMAZ [YAYIN_PLANI §3].
