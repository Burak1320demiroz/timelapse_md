# 🪟 İKİNCİ İSTASYON VE İÇ MEKÂN KILAVUZU — iki sabit kamera, tek yer

> `KAMERA_ISTASYONU_KILAVUZU` §1 ikinci bir istasyonun **koşullarını** sayar (çapa görünür · kendi
> içinde sabit · en çok iki · istasyon kesmesinde yapı yüzdesi sabit). Bu kılavuz o koşulların
> **nasıl uygulandığını** yazar: ne zaman ve filmin neresinde, kare zinciri iki kamera arasında nasıl
> kurulur, ikinci kameranın karesi nasıl türetilir, iç mekân timelapse'i nasıl yazılır, QA'ya ne beyan
> edilir.
>
> Kaynak: A26 · 07.10.2026 (`arastirma/SONUCLAR/A26_GEMINI_HAM.md`) · denetim `A25-A29_DENETIM.md` §2 ·
> ilk uygulama: **THE SLOW TAKEOFF** (yatay_4 · S13 ve S21 kokpit istasyonu · sahip kararı 07.10.2026).
> ⭐ Rapordan inen: ⭐ **ölçülmüş** — Magliano & Zacks (2011, Cognitive Science 35(8), çekildi ✅):
> kurgudaki EYLEM kesintisi olay bölütlemesini güçlü biçimde etkiler, mekân/zaman kesintisi (aynı eylem
> başka bakıştan) etkilemez → ikinci kamera AYNI işi sürdürürse yer okuması kırılmaz, iş kırılırsa kırılır ·
> ikinci kameraya geçişin **giriş, doruk ve final** bölümlerinde yapılmaması [VARSAYIM] · **iki saniyelik
> "flash" ek yerine tam klip** (yatay için) [VARSAYIM] · ortak çapa nesnesi · iç/dış **pozlama farkı**
> (pencere patlaması) ve **ışık lekesinin kayması** iç mekânın zaman taşıyıcısı.
> ⛔ İnmeyen: "ufuk ±%5" kuralı (tilt 0'da iki kamerada da ufuk tam %50 — kural kendiliğinden tutar;
> OVER THE WALL'daki %92 ↔ %73 tilt'ten geldi) · değerlendiriciye `[CUT TO: INTERIOR, PARALLEL TIME]`
> etiketi (bizim QA'mız VBench değil, Gemini rubriği; kör merceğe plan girmez) · iç kareyi ana karenin
> pencere içine KOMPOZİT etme (yalnız iki kamera aynı yöne bakıyorsa geçerli — §3) · raporun prompt
> şablonu (14 mm · 1,6 m · ufuk %90 · meşe sağda — bizim geometriyle çelişiyor).

---

# 0. 🚪 KURAL

```
İkinci istasyon bir İSTİSNADIR ve dört şartla girer:
  ① SABİT ve tilt 0 — kendi içinde hiç kıpırdamaz; ufuk iki kamerada da %50
  ② ORTAK ÇAPA — ana kameranın en az bir çapası ikinci kamerada görünür ve İKİ cümle iki SITE
     bloğunda BİREBİR aynıdır (kapı ≥6 kelimelik ortak dizi arar [DERS 10])
  ③ DIŞ BÜYÜME TAŞIMAZ — ikinci kamera klibi, bir önceki ana klibin AYNI zamanıdır; ana dış kare
     iki yakada aynı kalır [KAMERA_ISTASYONU §1 ④ · DERS 52]
  ④ BEYANLI — PLAN künyesinde ve QA_SPEC'te "İKİNCİ İSTASYON BEYANI" satırı; günlükte İSTASYON sütunu
Dört şarttan biri yoksa sahne ana istasyondan çekilir ya da çıkarılır.
```

Ölçülmüş bedeli (arşiv · 12 mercek):

| film | ne oldu | hangi şart yoktu |
|---|---|---|
| OVER THE WALL | plan dışı ikinci istasyon, ufuk %92 ↔ %73 → "SIX SEPARATE SHOTS"; aynı kesmede duvar yarımdan krete → üç mercek aynı saniyede | ① tilt · ③ büyüme · ④ beyan |
| THE LONG SHADOW | üç vantaj → "ALTI AYRI GÖRÜNTÜ" | ① · ② |
| THE CLOSING SPAN | ikinci istasyon farklı lens + kendi SITE metniyle → film parçalandı (0,77) | ② ortak cümle |
| THE BROKEN CLIMB | 4 vantaj + push-in → SIX SEPARATE SHOTS | ① sabitlik |

---

# 1. 📋 KARAR TABLOSU — ne zaman, kaç, nerede

| ölçüt | izin | YASAK | gerekçe |
|---|---|---|---|
| süreklilik | ikinci kamera klibi bir önceki ana klibin İŞİNİ sürdürür ya da aynı işin içeriden hâlini gösterir | ikinci kamerada başka bir işe atlamak | eylem kesintisi bölütlemeyi kırar, mekân değişimi kırmaz [Magliano & Zacks 2011 ✅] |
| biçim | **dikey:** EK (≤2 sn, ana sahnenin içinde, merdiven satırı almaz) [P2-e] · **yatay:** KLİP (tam 8–10 sn, kendi satırı) | yatayda ≤2 sn'lik "flash" ek | dikey 2x'te ek ≈1 sn bir bakıştır; yatayda kısa ek olay sınırı yaratıp çözmeden geçer [A26-b · VARSAYIM] |
| sayı | en çok 2 klip · aynı istasyondan · filmin ≤ %10'u · ana istasyon ≥ %85 süre | üçüncü bir vantaj · art arda iki ikinci-istasyon klibi | KAMERA_ISTASYONU §1 ③ · ana istasyon "yer"in hafızasıdır |
| konum | gelişme bölümü (%20–%80) | ilk üç klip (yer henüz kurulmadı) · DORUK klibi · bölüm sınırı karesi (6/8 dk ve 2/4 dk iki dosyalı) · final ve tutuş | EST: yer modeli kurulmadan geçiş yeri yıkar; doruk ve final dışarıda okunur [A26-b · VARSAYIM] · sınır karesi tek kare olmalı [DERS 52] |
| konu | dışarıdan OKUNMAYAN iş (iç mekân: pencere ana kadrajda ≈8 px) ya da yakın iş | dışarıdan okunabilen işi içeriden göstermek | ikinci kamera bir boşluğu doldurur, çeşitlilik için değil [KILAVUZ_REHBERI §1.2] |
| çapa | iç kamerada pencereden en az bir ana çapa (ağaç · karşı kıyı · tepe sırtı) | çapasız iç mekân | ② şartı |
| ışık | dışarıyla AYNI saat, aynı gök; iç ışık lekesi 10 dk'da ≈2,5° kayar | iç klipte gün/mevsim atlaması | güneş 15°/sa; ③ şartı |

THE SLOW TAKEOFF bu tablodan geçer: 2 klip (S13 · S21 = %6,7) · gelişme bölümünde (%43 · %70) ·
doruk (S5–S6), sınır (G15) ve final (S26–S29) dışarıda · pencereden meşe + karşı kıyı · tilt 0.

---

# 2. 🔗 KARE ZİNCİRİ — iki kamera arasında

Dikişin iki yakası aynı kare olamaz (iki kamera). Çözüm: **ikinci kamera klibi ana zincirin DIŞINDA,
paralel zamandır**; ana dış kare iki yakada aynıdır.

```
ANA       G(n−1) ──S(n−1)──▶ G(n+1) ─────────────────────▶ ──S(n+1)──▶ G(n+2)
                              │  (aynı dış kare, iki yakada)  │
İKİNCİ                        └── S(n): Gn(K) ──▶ Gn′(K) ─────┘   (S(n−1) ile AYNI on dakika)

   S(n−1)'in I2V'si ana kare G(n+1)'e biter · S(n) ikinci istasyonda Gn → Gn′ · S(n+1) yine G(n+1)'den başlar
   Ana zincirde Gn numarası BOŞ kalır (ikinci istasyonun karesidir) — kare tablosunda 🪟 ile işaretlenir
```

```
ADLANDIRMA   Gn (ikinci istasyon ilk kare · sahne görseli) · Gn′ (ikinci istasyon son kare · EK BLOK,
             kapı saymaz) · bölüm dosyasında "### 🪟 KOKPİT SON KARESİ (Gn′)" başlığı
ÜRETİM       ters zincir ana kareler için aynen (GN → G0); ikinci istasyon kendi küçük zinciri:
             Gn′ ÖNCE (ana G(n+1)'in mevsimi ve ışığıyla) → Gn ondan (mobilya/iş geri alınarak);
             ikinci klip Gk varsa Gn′'den türetilir (aynı iç mekânın sonraki hâli)
ZİNCİR KAPISI zincir_kontrol ana kareleri birbirine, ikinci istasyon karelerini birbirine bağlar;
             ⛔ ana kare ile iç kare zincir_kontrol'e verilmez (kenarlar farklıdır, çıkış anlamsız)
PROMPT KAPISI prompt_kontrol.py kareleri sırayla eşler; istasyon kesmesinde "YENİ eleman" (DERS 61)
             yanlış alarm verir — PLAN §ÜRETİM ÖNCESİ DURUM'da ayrı satırla beyan edilir.
             ⬜ kapıya istasyon farkındalığı: sahip kararı
```

---

# 3. 🎨 İKİNCİ KAMERANIN KARESİNİ TÜRETMEK

```
① KAMERALAR AYNI YÖNE BAKIYORSA (iç kamera ana kameranın görüş yönünde bir pencereden dışarı bakar):
   ana kameranın onaylı karesi pencere bölgesine YERLEŞTİRİLİR (maske), model yalnız iç mekânı üretir —
   dış dünya piksel piksel aynı kalır [A26-c · İDDİA, araç pratiği]
② YÖNLER FARKLIYSA (THE SLOW TAKEOFF: ana kamera kuzeye, kokpit batıya bakar):
   kompozit YAPILAMAZ — dış dünya başka bir yönden görünür. Yerine:
   · iki SITE bloğunda birebir ortak cümle (karşı kıyı · ufuk %50 · aynı meşe)
   · mevsim, gök ve ışık ana karenin KARE TABLOSU satırından birebir
   · ilk kokpit karesi üretildikten sonra elle: pencereden görünen meşe ana karedeki meşeyle aynı tür,
     aynı renk evresi mi · karşı kıyı aynı ton mu · su/kar durumu aynı mı → değilse KAREYİ YENİDEN ÜRET
③ İÇ MEKÂN ARALARI (iki iç klip arası) aynı iç mekânın sonraki hâlidir: ikinci iç ilk kare, birincinin
   SON karesinden türetilir (mobilya, renkler, pencere sayısı aynı)
```

⚠️ Raporun önerdiği otomatik denetim — pencere bölgesinin ana karedeki çapayla DINOv2 benzerliği,
LightGlue öznitelik eşleme — bu depoda kurulu değil ve eşiği (ör. "< 0,85") kaynaksız [A26-c · VARSAYIM].
Bugün denetim ELLE yapılır (②).

---

# 4. 🏠 İÇ MEKÂN TIMELAPSE DİLİ

| taşıyıcı | nasıl yazılır | rejim |
|---|---|---|
| **ışık lekesi** | pencereden düşen güneş lekesi tabanda kayar — 10 dk ≈ 2,5° (güneş 15°/sa) | A · B |
| **pencere patlaması** | dış dünya içeriden 1–2 durak parlak: "the view through the panes is bright daylight, the cabin in soft shade" — kusursuz eşit HDR iç mekân CGI okunur | hepsi |
| **eşya akışı** | mobilya ve malzeme bir kaynaktan gelir (el arabası, kapı), bir yere oturur; eksilen yığın | A |
| **insan** | iz ("faint soft motion streaks"), yüz okunmaz; iç mekânda kameraya YAKIN figür yazılmaz | A · B |
| **yağmur / su (dışarıda)** | camda akan damla izleri, dışarıda kot; içerisi kuru ve sakin | A |
| **lamba** | iç lamba bir kez yanar ve yanık kalır (dış kareyle tutarlı) [ISIK_FINALI §3] | A |

⛔ İç mekânda okunur ekran, gösterge, kadran YAZILMAZ — metin riskidir; yüzey "plain matte panels and
timber" diye pozitif tarif edilir [P12-f · DERS 35].

---

# 5. 🧱 PROMPT BLOKLARI — ikinci istasyon (THE SLOW TAKEOFF'tan, sınandı: kapı BLOCK 0)

```
Camera: COCKPIT STATION — fixed clamp mount bolted to the rear wall of the cockpit, lens 8.2 metres above
the meadow, 2.4 metres from the windscreen, bearing 270 degrees, tilt 0 degrees, zero roll. The camera
never moves.
   ⇒ altı alan zorunlu: lens · yükseklik ("metres above") · mesafe ("metres from") · bakış ("bearing") ·
     tilt · roll [KAMERA_ISTASYONU §2]

SITE / BACKGROUND: <iç mekânın sabit kabuğu> … Through the left panes rises the crown of the one big old
oak on its slight dry rise; ahead and to the right, beyond the meadow below, the lake runs out to the far
shore, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly
half the frame height.
   ⇒ altı çizili iki cümle ana SITE bloğunda BİREBİR aynı

I2V'de istasyon cümlesi (kilit paragrafının başında):
This shot shows the same stage as the previous shot from the main station: the house stands at the same
height, its belly about fifty-seven percent of frame height in that view, and nothing outside the cockpit
is built during this shot.
```

İç mekân TIME RATE (rejim A): *"Everything in this frame is time-lapsed at the same rate: the clouds and
the light outside, the rain and the water, and any crew inside all move at the same accelerated speed. Ten
minutes pass across this shot …"* — iç klip insansızsa "No people are present." [DERS 33].

---

# 6. 📢 QA BEYANI

```
❹ ❺ (belgeli)   QA_SPEC künyesinde İKİNCİ İSTASYON BEYANI: istasyon adı · h · bakış · hangi sahneler
                (saniye aralığı) · paralel zaman · sahip kararı. ❹ DAVETLİ listesinde iç mekân eşyası.
❶ ❷ ❸ (kör)    plan GİRMEZ [QA_KOSU §1]. ⬜ SAHİP KARARI: ölçülmüş olgular bloğuna (QA_OLCUM_ZEMINI §2)
                tarafsız bir satır — "CAMERA POSITIONS: 2 fixed positions; the second is used at 1:44–1:52 and
                2:48–2:56" — eklenip eklenmeyeceği. Artısı: ❶ istasyon değişimini kusur sanmaz. Eksisi:
                kör mercek "ikinci kamera başka dünya mı" sorusunu artık önyargısız soramaz.
                Karar gelene kadar satır EKLENMEZ; ❶ SEPARATE IMAGES verirse önce gerekçesindeki saniye
                okunur — istasyon kesmesi mi, gerçek kayma mı.
```

---

# 7. ✅ KONTROL LİSTESİ — plan yazılırken ve kare üretildikten sonra

| # | madde | ihlal → eylem |
|:-:|---|---|
| 1 | ikinci istasyonun konusu dışarıdan okunmayan bir iş mi | → KAMERAYI KALDIR |
| 2 | klip sayısı ≤ 2, aynı istasyon, art arda değil | → KAMERAYI KALDIR |
| 3 | konum gelişme bölümünde; ilk üç klip · doruk · bölüm sınırı · final dışında | → SAHNEYİ TAŞI |
| 4 | Camera satırında altı alan; tilt 0 | → BLOĞU YENİDEN YAZ |
| 5 | iki SITE bloğunda en az iki cümle birebir ortak | → BLOĞU YENİDEN YAZ |
| 6 | I2V'de "This shot shows the same stage as the previous shot from the main station" cümlesi | → BEYAN EKLE |
| 7 | ana dış kare iki yakada aynı (S(n−1) sonu = S(n+1) başı) | → KAREYİ YENİDEN ÜRET |
| 8 | pencereden görünen çapa ana karedeki çapayla aynı tür, renk evresi, ton | → KAREYİ YENİDEN ÜRET |
| 9 | iç mekân eşit parlak HDR değil, pencere dışarısı daha parlak | → KAREYİ YENİDEN ÜRET |
| 10 | iç klipte ışık lekesi / yağmur / eşya akışı gibi bir zaman taşıyıcısı var | → BLOĞU YENİDEN YAZ |
| 11 | PLAN + QA_SPEC'te İKİNCİ İSTASYON BEYANI, günlükte İSTASYON sütunu | → BEYAN EKLE |
| 12 | zincir_kontrol iç kareleri yalnız birbirine, ana kareleri yalnız birbirine bağladı | → KAPIYI YENİDEN KOŞ |

---

# 8. 📎 İNMEYENLER VE AÇIK OLANLAR

```
⛔ "ufuk ±%5" kuralı              tilt 0'da ufuk iki kamerada da %50 — kural boşa düşer; asıl kural tilt 0
⛔ [CUT TO: …] etiketi           değerlendirici VBench/CLIP değil; üretim promptuna kurgu yönergesi yazmak
                                 aracın içine yazı/kesme davetidir
⛔ raporun prompt şablonu         14 mm · 1,6 m · ufuk %90 · meşe sağda — bu filmin geometrisiyle çelişir
⛔ PySceneDetect "27 eşiği" → QA  PySceneDetect bizim değerlendiricimiz değil; kesme yeri top-N ile ölçülür
                                 [A21-c] — istasyon kesmesinin yüksek skoru beklenen ve zararsızdır
⚠️ ticari araç sürümleri — Runway Gen-4.5 (1 Ara 2025 ✅) · Kling 4.0 (duyuru 30 Eyl 2026, tam sürüm "Ekim",
                                 10 keyframe · 3–30 sn ✅) · "Seedance 2.5 / Prologue AI" (doğrulanmadı) — özellik iddiaları
                                 ARAÇ KAPISINDA ölçülmeden kullanılmaz [ARAC_KARTLARI §4]
⛔ ConsiStory arXiv:2412.07750    yanlış kimlik (o numara "Motion by Queries"); ConsiStory = 2402.03286
⬜ prompt_kontrol.py istasyon farkındalığı · ❶ olgu satırı — sahip kararı
⬜ ilk ölçüm: THE SLOW TAKEOFF QA'sında ❶'in S13/S21 kesmelerini okuyuşu (104,0 · 112,0 · 168,0 · 176,0 sn)
```
