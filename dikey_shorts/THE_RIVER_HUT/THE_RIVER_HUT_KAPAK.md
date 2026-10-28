# 🖼️ THE RIVER HUT — KAPAK + YAYIN PAKETİ

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
METİN      ONE MAN BUILDS / A RIVER SHELTER  (6 kelime · İKİ satır · İngilizce · sahip seçimi 27.10.2026)
           ⚠️ KAPAK_STIL_KILAVUZU §1 "film adı 1–3 kelime" der; bu film sahibin seçtiği yayın başlığını kartta taşır — beyanlı sapma.
              Kısa yedek (sahip isterse): THE RIVER HUT (3 kelime, tek satır) — §5 ⓓ.
```

---

## 0. ⭐ STİL KARTI [KAPAK_STIL_KILAVUZU §7]

```
STİL KARTI  [KAPAK_STIL_KILAVUZU]
BANT        Ü · y 560–770 · x 180–900 · sakin alan: SIĞINAĞIN ÜSTÜNDEKİ KOYU AĞAÇLIK YAMAÇ (mavi saat, −8,5°) — plan TASARIM ⑯
            ⚠️ SAPMA, BEYANLI: kılavuzun "sakin" listesi düz gök · su · zemin · duvar; burada koyu orman kütlesi · iki ladin kutunun DIŞINDA
            (x 135 / 912) · mahya py 806 (bandın 36 px altı) · borunun dumanı bandın ALTINDA sağa savrulur ("drifts away to the right
            below it") — G8'de ölçülür
IŞIK        reçete R1 (mavi saat + sıcak kaynak) · varyant I0 (GN'nin kendi ışığı) — en parlak şeyler fener, sudaki kırık ışık sütunu ve
            pencere; bant KOYU kalır ("darkest on the wooded slope")
STİL        S4 — iki satır · yazı tipi Anton (kılavuz varsayılanı; ⚠️ kanal yazı tipi sahip kararı bekliyor) · renk #E8E4DC · vurgu kelimesi —
METİN       ONE MAN BUILDS / A RIVER SHELTER (6 kelime · 2 satır) · büyük harf ≈ 84–90 px (≥ 78) — 15 karakterlik uzun satır 720 px'in
            %80–90'ını doldurur; iki satır + sıkı aralık ≈ 175–185 px ≤ 210
KONTRAST    ⬜:1 (≥ 4,5) — koyu yamaçta yüksek beklenir; ölçülür (§4.4 betiği · x0 180 y0 560 x1 900 y1 770) · koyu geçiş: gerekirse
KANIT       zincir_kontrol ⬜ · nirengi ⬜ px · nesne sayımı ⬜ (bir sığınak · bir fener · iki kazık · bir boru · üç kaya · bir adam)
PROVA       PROVA_PANOSU ⬜ · 1:1 başlık tam ⬜ · 140 px üç soru ⬜
```

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi saatte, koyu ağaçlık yamacın dibinde yeşil çim çatılı küçük bir kütük sığınak: penceresi ve kapı aralığı sıcak
                  turuncu, borusundan ince duman · sağında nehre uzanan kısa tahta iskele, ucunda yanık fener; ışığı akan suyun üstünde
                  kırık, titreşen bir sütun · iskelenin ucunda sırtı dönük oturan tek adam · önde soğuk taş halka ve devrik kütük · sol
                  kenarda çadır köşesi · üstte koyu yamaç (başlık)
BAŞLIKTA YAZAN    ONE MAN BUILDS / A RIVER SHELTER

KANCA             "bunu tek başına mı yaptı?" — başlık "one man" der; kapak bitmiş bir evi ve onu kuran adamı aynı karede gösterir.
                  Görünmeyen şey boş çakıl düzlüktür. Merak "ne olacak?"tan "nasıl?"a kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ SUDAKİ IŞIK SÜTUNU + YANIK PENCERE — koyu mavi kadrajda iki sıcak nokta; 140 px'te bile "nehir kenarında ev" okunur
                  [P3-b: kontrast].
İKİNCİ OKUMA      iskelenin ucundaki tek adam: "bunu o kurdu"
ÜÇÜNCÜ OKUMA      çadır + soğuk taş halka: "burası önce bir kamptı"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① boş çakıl düzlük ve kıyıdaki taş yatağı ② taş tabanın, kütük duvarın, çatının elle yükselişi ③ fenerin yandığı an.
⛔ Kapak G7 DEĞİLDİR: G7'de fener sönük, adam ayakta, suda ışık yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   gök şeridi                          0–≈170     yasak bölge — başlık oraya çıkmaz
   ağaçlık yamaç                       ≈170–1095  yamacın dibi py ≈ 1095
   ⭐ BAŞLIK KUTUSU                     560–770    x 180–900 — sığınağın üstündeki koyu yamaç
   iki ladin                           —          x 135 / 912 — kutunun DIŞINDA
   ⭐ SIĞINAK (mahya → taban)           806–1183   x 315–596 · pencere x 362–409 py 1005–1060 · kapı x 512–578 · boru tepesi py 822
   ufuk (yamacın arkasında)            960
   ⭐ FENER                             1088       x 957
   iskele                              1194       x 770–958 · kazıklar 1286'ya kadar
   ⭐ IŞIK SÜTUNU (suda)                ≈1290–1500 x ≈ 940–975
   üç kaya                             1242–1677  x 864–886
   taş halka                           1409–1505  x 353–561
   devrik kütük                        1562–1713  x 95–635
   alt UI bandı                        1440–1920  (taş halka + kütük — yardımcı doku)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · sığınak ✅ · iskele ✅ · fener ✅ (x 957 çekirdeğin 27 px dışında — beyanlı) ·
   ışık sütununun üst ucu çekirdeğin sınırında
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, sığınağı, iskeleyi, feneri ve ışık sütununu taşır · 4:5 (285–1635) ve 3:4 (240–1680) taş halkayı
   da taşır.
⚠️ Mahya py 806 — başlığın alt satırı en çok py ≈ 760'a iner; duman bandın içine yükselirse ya da yamaç açık renge dönerse G8 yeniden
   (plan PİLOT a).
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 + KAPAK_STIL_KILAVUZU §4 ölçüleriyle

```
METİN      ONE MAN BUILDS / A RIVER SHELTER — İKİ SATIR (S4), ORTALI, x = 540
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — sığınağın üstündeki koyu yamaç · satırlar y ≈ 575–662 ve ≈ 672–760 · yazı sığınağı,
           boruyu ve ladinleri örtmez
PUNTO      Anton, büyük harf ≈ 84–90 px (≥ 78 eşiği) · uzun satır "A RIVER SHELTER" (15 karakter) bant genişliğinin %80–90'ı · satır
           aralığı punto × 0,95 · gerçek yazı sınırları 720 × 210'u AŞMAZ, aşarsa punto küçülür; eşiğin altına düşerse kısa yedeğe
           geçilir (THE RIVER HUT) — harf aralığı daraltılmaz · tek ağırlık · parlama / kontur YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan koyu orman → kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse başlığın
           arkasına #101315 yumuşak koyu geçiş (%35–50) [KAPAK_STIL §4.4]
⛔ Başka kelime yok: "AI" · "timelapse" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada nehir ve en yakın kaya var (yardımcı doku).
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "yanık pencere + sudaki ışık" ayrışıyor mu ⓑ başlık iki satırda okunuyor mu ⓒ sağ alt köşe boş
               mu · ⭐ aynı test G0'a: "boş düzlük + el arabalı adam" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, sığınak ve fener TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "nehir kenarında küçük bir kulübe, adam iskelede" diyor mu — "otel", "render", "kartpostal" diyorsa
               G8 yeniden; kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki fener = finaldeki fener [MUZIK_VE_KAPAK §5]
⑦ KONTRAST     KAPAK_STIL §4.4 betiği · bant x 180–900 · y 560–770 → ≥ 4,5:1
```

## 5. Dört varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + ONE MAN BUILDS / A RIVER SHELTER   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur (sahip seçimi)
ⓑ BAŞLIKSIZ            G8 tam kare — sahip kararı
ⓒ METİNSİZ             ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
ⓓ KISA YEDEK           G8 + THE RIVER HUT (tek satır, S1) — yalnız sahip isterse ya da ⓐ 78 px eşiğini tutturamazsa
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
⭐ SEÇİLEN   One Man Builds a River Shelter               (30)   ajan önerisi · sahip seçimi
   yedek    Solo Riverbank Shelter, Stone to Firelight   (42)   paketin alternatifi — ⚠️ 40 karakteri AŞAR; "Firelight" taş halka yanmadığı
                                                               için yanlış söz verir
   yedek    What Will One Man Build on This Riverbank?   (42)   planın MERAK SORUSU — ⚠️ 40'ı aşar, kısaltılmadan kullanılmaz
```

> Paketin ana önerisi "One Man Builds a Riverside Bunker Alone" düştü: "bunker" gömülü/tahkimatlı yapı vaat eder (plan TASARIM ⑲),
> "One Man … Alone" iki kez aynı şeyi der. Seçilen başlık KILAVUZ_REHBERI §6'nın "≤ 5 kelime" testini bir kelimeyle aşar (beyanlı).

**Açıklama:**

```
An empty gravel flat beside a mountain river, one tent, one man. He wheels stones up from the bank for a knee-high base, rolls logs up
two poles one at a time until the walls stand, roofs it in green turf and runs a short jetty out over the water.
Then the lantern.

Days of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real building, no real place, no real person and no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #logcabin #bushcraft #offgrid #riverside
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> Açıklama fenerin yanışını ve oturan adamı ANMAZ ("Then the lantern.") — spoiler bütçesi. "Days of work" sahneler arası takvim
> atlamasının beyanıdır (plan SAHA satırı). "logcabin" yalnız hashtag'de — promptlarda "cabin" YASAK KELİME'dir (plan TASARIM ⑲).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
log shelter, river shelter, one man build, solo build, bushcraft shelter, off grid cabin, log cabin build, construction timelapse, ai timelapse, ai video, timelapse, the river hut, bushcraft shleter
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("bushcraft shleter" bu yüzden bilerek var). Gerçek yer/firma/marka adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Small log shelters are usually raised on a stone or gravel base so the bottom logs stay off the wet ground, and a turf roof needs a
waterproof layer underneath it. Anyone building near a river also has to think about how high the water can rise in spring, and in many
places building on a riverbank at all needs permission first.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("usually · in many places"); belirli ürün, ölçü, yük ya da
> süre iddia edilmez (ÇIKARIM, genel bilgi). Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | tek adam, nehir kenarında sığınak | nasıl, hangi sırayla, fener |
| kapak | bitmiş sığınak + yanık fener + oturan adam + başlık | boş düzlük, taşın ve kütüğün yolu, yanış anı |
| ilk 2 sn | boş düzlük, taş dolu el arabası, nehir | düzlüğün neye dönüşeceği |
| açıklama | taş taban, kütük duvar, çim çatı, iskele, "sonra fener" | fenerin yanışı, ışığın suya düşmesi, oturan adam |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (mavi saatte fener yanar, ışığı suya düşer, adam iskelenin ucuna oturur) kapak
dışında söyleyemez → ✅ (taslak; kurgudan sonra tekrar). ⚠️ Kapak yanık feneri gösterir; yanış ANI yine saklıdır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: KÜTLE ailesi — THE SUNKEN GARDEN (taş halka, oturan insanlar, akşam ışığı), LIT AGAIN (kıyıda fener ışığı) ve THE DRIVE-IN
   (mavi saatte ışık finali) ile ARDIŞIK YAYINLANAMAZ [YAYIN_PLANI §3].
