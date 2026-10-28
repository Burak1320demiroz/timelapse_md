# 🖼️ THE TOWER HOME — KAPAK + YAYIN PAKETİ

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
METİN      OLD WATER TOWER / BECOMES A HOME  (6 kelime · İKİ satır · İngilizce · sahip seçimi 27.10.2026)
           ⚠️ KAPAK_STIL_KILAVUZU §1 "film adı 1–3 kelime" der; bu film sahibin seçtiği yayın başlığını kartta taşır — beyanlı sapma.
              Kısa yedek (sahip isterse): THE TOWER HOME (3 kelime, tek satır) — §5 ⓓ.
⛔ Paketin "başlık üst üçte birde gökyüzünde" önerisi DÜŞTÜ — kapak orta bant kuralı (sahip 25.10.2026: başlık en üst/alt değil, Ü/O/A);
   Ü bandı (560–770) tankın ve terasın tam üstüne denk gelir, O bandı (860–1060) ayaklardan ve ufuktan geçer → A bandı.
```

---

## 0. ⭐ STİL KARTI [KAPAK_STIL_KILAVUZU §7]

```
STİL KARTI  [KAPAK_STIL_KILAVUZU]
BANT        A · y 1060–1240 · x 180–900 · sakin alan: KULENİN ÖNÜNDEKİ ÇIPLAK ÇAKIL AVLU (mavi saat, −8,5°) — plan kadraj kilitleri
            ⭐ "düz zemin" — kılavuzun sakin listesinde, SAPMA YOK · ayak dipleri py 1039–1057 (bandın 3–21 px üstü) · panellerin ayağı py 1061
            (bandın üst kenarı, x 256–369) · pompa evi x 964+ (kutunun DIŞINDA)
IŞIK        reçete R1 (mavi saat + sıcak kaynak) · varyant I0 (GN'nin kendi ışığı) — en parlak şeyler üç pencere ve kapı; bant KOYU kalır
            ("the gravel of the yard in front of the tower is dark and even")
STİL        S4 — iki satır · yazı tipi Anton (kılavuz varsayılanı; ⚠️ kanal yazı tipi sahip kararı bekliyor) · renk #E8E4DC · vurgu kelimesi —
METİN       OLD WATER TOWER / BECOMES A HOME (6 kelime · 2 satır) · büyük harf ≈ 84–90 px (≥ 78) — 15 karakterlik uzun satır 720 px'in
            %80–90'ını doldurur; iki satır + sıkı aralık ≈ 175–185 px ≤ 210
KONTRAST    ⬜:1 (≥ 4,5) — koyu çakılda yüksek beklenir; ölçülür (§4.4 betiği · x0 180 y0 1060 x1 900 y1 1240) · koyu geçiş: gerekirse
KANIT       zincir_kontrol ⬜ · nirengi ⬜ px · nesne sayımı ⬜ (bir kule · dört ayak · beş bant · üç pencere · bir merdiven · iki panel · bir adam)
PROVA       PROVA_PANOSU ⬜ · 1:1 başlık tam ⬜ · 140 px üç soru ⬜
```

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi saatte açık tarlada tek başına duran ayaklı bir kule: koyu kahve ahşap tankında üç yuvarlak pencere ve açık kapı
                  içeriden sıcak sarı · tankı saran terasta oturan tek adam · sağ önde koyu gri sarmal merdiven · solda iki güneş paneli ·
                  sol arkada meşe, sağ altta pompa evi · üstte koyu mavi gök, ufukta son ışık · altta koyu düz çakıl (başlık)
BAŞLIKTA YAZAN    OLD WATER TOWER / BECOMES A HOME

KANCA             "bu bir su kulesi miydi?" — başlık "old water tower" der; kapak içinde ışık yanan bir evi gösterir. Görünmeyen şey gri,
                  paslı, kırık merdivenli eski kuledir. Merak "ne olacak?"tan "nasıl?"a kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ ÜÇ SICAK YUVARLAK PENCERE — koyu mavi kadrajın ortasında üç sarı daire; 140 px'te bile "içinde biri yaşıyor" okunur
                  [P3-b: kontrast].
İKİNCİ OKUMA      ayaklar + konik çatı: "bu bir su kulesi"
ÜÇÜNCÜ OKUMA      terasta oturan adam + paneller: "şebekeden uzak bir ev"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① gri, paslı, kırık merdivenli kule ② kıvılcım, merdiven, teras, delinen tank ③ pencerelerin yandığı an.
⛔ Kapak G7 DEĞİLDİR: G7'de pencereler sönük, adam kapı ağzında, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER"
   YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   açık gök                            0–960      tankın çevresi
   havalandırma · çatı tepesi          326 · 349  x 540
   ⭐ TANK                              369–698    x 417–663 (245 px)
   ⭐ ÜÇ YUVARLAK PENCERE               456–515    x 457 · 540 · 623 (Ø ≈ 50)
   meşe (taç tepesi)                   512        x ≈ 0–324
   ⭐ kapı                              522–640    x 576–625
   ⭐ teras + korkuluk                  575–680    x 358–722 · adam terasta oturuyor (≈ 75 px)
   sarmal merdiven                     672–1056   x 681–767
   pompa evi                           878–1097   x 964–1080
   iki güneş paneli                    953–1061   x 256–369
   ufuk                                960
   ayak dipleri                        1039–1057  x 420–660
   ⭐ BAŞLIK KUTUSU                     1060–1240  x 180–900 — kulenin önündeki çıplak çakıl
   alt UI bandı                        1440–1920  (çakıl yol — yardımcı doku)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · tank alt yarısı ✅ · pencereler (py 456–515) çekirdeğin 25–84 px ÜSTÜNDE — beyanlı ·
   teras ✅ · merdiven ✅ · paneller ✅ · ayaklar ✅
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, pencereleri, terası, merdiveni ve ayakları taşır; çatı tepesi (349) kesilir — beyanlı · 4:5
   (285–1635) ve 3:4 (240–1680) çatıyı da taşır.
⚠️ Pencerelerin ışığı avluya ulaşıp bandı aydınlatırsa ya da avluda nesne (pikap, merdiven, yığın) kalmışsa G8 yeniden (plan PİLOT a).
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 + KAPAK_STIL_KILAVUZU §4 ölçüleriyle

```
METİN      OLD WATER TOWER / BECOMES A HOME — İKİ SATIR (S4), ORTALI, x = 540
YER        ⭐ başlık kutusu x 180–900 · y 1060–1240 — kulenin önündeki koyu çakıl · satırlar y ≈ 1068–1152 ve ≈ 1160–1240 · yazı ayakları,
           merdiveni, panelleri ve pompa evini örtmez
PUNTO      Anton, büyük harf ≈ 84–90 px (≥ 78 eşiği) · uzun satır "OLD WATER TOWER" / "BECOMES A HOME" (15 / 14 karakter) bant genişliğinin
           %80–90'ı · satır aralığı punto × 0,95 · gerçek yazı sınırları 720 × 210'u AŞMAZ, aşarsa punto küçülür; eşiğin altına düşerse
           kısa yedeğe geçilir (THE TOWER HOME) — harf aralığı daraltılmaz · tek ağırlık · parlama / kontur YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan koyu çakıl → kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse başlığın
           arkasına #101315 yumuşak koyu geçiş (%35–50) [KAPAK_STIL §4.4]
⛔ Başka kelime yok: "AI" · "timelapse" · "before/after" · "off-grid" · "hidden" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada çakıl yol var (yardımcı doku).
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "üç yanık pencere + kule" ayrışıyor mu ⓑ başlık iki satırda okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "gri su kulesi + kıvılcım" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, pencereler ve teras TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "su kulesinden yapılmış bir ev" diyor mu — "deniz feneri", "silo", "render" diyorsa G8 yeniden
               (ayaklar ve konik çatı okunmuyor demektir); kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki pencereler = finaldeki pencereler [MUZIK_VE_KAPAK §5]
⑦ KONTRAST     KAPAK_STIL §4.4 betiği · bant x 180–900 · y 1060–1240 → ≥ 4,5:1
```

## 5. Dört varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + OLD WATER TOWER / BECOMES A HOME   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur (sahip seçimi)
ⓑ BAŞLIKSIZ            G8 tam kare — sahip kararı
ⓒ METİNSİZ             ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
ⓓ KISA YEDEK           G8 + THE TOWER HOME (tek satır, S1) — yalnız sahip isterse ya da ⓐ 78 px eşiğini tutturamazsa
⛔ DÖRDÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (kırpmalar PROVA'dır — kapak_prova.py).
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/marka adı yok · ≤ 40 karakter.
```

**Başlık — sahip seçti (27.10.2026):**

```
⭐ SEÇİLEN   Old Water Tower Becomes a Home               (30)   ajan önerisi · sahip seçimi
   yedek    One Man Turns a Water Tower Into a Home      (39)   paketin alternatifi — 9 kelime, kart için uzun
   yedek    Who Will Live in This Old Water Tower?       (38)   planın MERAK SORUSU
```

> Paketin ana önerisi "Abandoned Water Tower Becomes a Hidden Home" düştü: açık tarladaki kule "hidden" değildir (yanlış söz) ve 43
> karakterle sınırı aşar. Seçilen başlık KILAVUZ_REHBERI §6'nın "≤ 5 kelime" testini bir kelimeyle aşar (beyanlı).

**Açıklama:**

```
An old wooden water tower standing alone in a field: grey staves, rusted legs, a broken ladder. One man grinds the legs bare, bolts a
spiral staircase to them, rings the tank with a terrace, sands it, cuts three round windows and a door and oils it dark.
Then the evening.

Days of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real building, no real place, no real person and no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #watertower #tinyhome #offgrid #renovation
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> Açıklama pencerelerin yanışını ve oturan adamı ANMAZ ("Then the evening.") — spoiler bütçesi. "Days of work" sahneler arası takvim
> atlamasının beyanıdır (plan SAHA satırı).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
water tower home, water tower conversion, old water tower, tower house, tiny home build, off grid home, one man build, construction timelapse, ai timelapse, ai video, timelapse, the tower home, water towr home
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("water towr home" bu yüzden bilerek var). Gerçek yer/firma/marka adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Old water towers are sometimes turned into homes or studios. Wooden tanks are held together by the steel bands around them, so cutting
openings usually means adding a frame to carry the load the band used to carry, and the legs and their footings have to be checked
before anyone adds a terrace, a staircase and the weight of people living up there.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("sometimes · usually"); belirli ürün, ölçü, yük ya da süre
> iddia edilmez (ÇIKARIM, genel bilgi). Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | eski su kulesi eve dönüşür | nasıl, hangi sırayla, ışık |
| kapak | yanık pencereli kule ev + terasta adam + başlık | gri paslı kule, kıvılcım, delinen tank, yanış anı |
| ilk 2 sn | gri kule, kıvılcım, gelen pikap | kulenin neye dönüşeceği |
| açıklama | ayaklar, sarmal merdiven, teras, pencereler, kapı, yağ, "sonra akşam" | pencerelerin yanışı, oturan adam |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (mavi saatte üç yuvarlak pencere tek anda yanar, adam terasa oturur) kapak dışında
söyleyemez → ✅ (taslak; kurgudan sonra tekrar). ⚠️ Kapak yanık pencereleri gösterir; yanış ANI yine saklıdır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: KULE ailesi — THE SKY VAULT (paslı depo → ışıklı oda), LIT AGAIN (kule, ışık finali), THE RIVER HUT (tek adam, mavi saatte
   ışık) ve THE RAIN TOWER (aynı KULE siluet) ile ARDIŞIK YAYINLANAMAZ [YAYIN_PLANI §3].
