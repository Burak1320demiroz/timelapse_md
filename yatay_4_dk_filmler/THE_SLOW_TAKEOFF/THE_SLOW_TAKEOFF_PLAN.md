# ✈️ THE_SLOW_TAKEOFF — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **30 × 8,0 sn = 240,0 sn** | Kapak kartı: **⛔ YOK** | Toplam: **240,0 sn**
Prompt yapısı: ⭐ **30 sahne → 31 ana görsel (G0…G30; G13 · G21 kokpit) + 2 kokpit son karesi (G13′ · G21′) + 30 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G15**
Yapı: **emekli, markasız, kanat altı iki motorlu dar gövde bir yolcu jeti — yerden kaldırılıp iki çelik çerçeveye oturtulan göl evi** (kart yok: `YAPI_TIPI_KARTLARI` §10 şablonuyla 00_ANALIZ/02 §2'de yazıldı; en yakın emsal LAST LIFT strand-jack kaldırma · QUIET FIELD tandem beşik) · Saha: **ılıman göl kıyısı çayırı, 47° K** (kart yok: `SAHA_VE_IKLIM_KARTLARI` §3.7 şablonuyla 02 §2 — kırsal §3.2 + kıyı §3.3 + kar §3.5'ten)
Zaman yayı: **gerçekte ≈10 ay (yaz sonu → ertesi yaz başı) → 240 saniye** · film mertebe anlatır: *"bir sonbahar, bir kış, bir bahar seli"* [P1-c] · ÜSLUP BEYANI: takvim tek bir günün ışığına sıkıştırıldı (THE OLD ROAD emsali)
Işık günü: **07:40 → 19:20 (mavi saat) · Σ rejim penceresi 11 sa 40 dk ≤ 14** — kesmede ışık atlamaz [§2.7 ①] · mavi saat = sahip kararı 07.10.2026 ("Son plan mavi saattedir")
Kamera mimarisi: **MAIN STATION** — 28 sahne + usta kare · **COCKPIT STATION** (detay) — 2 sahne: S13 · S21 · ⚠️ P2-e'nin "≤2 sn ek" sınırını AŞAR — sahip kararı 07.10.2026 ("Tek kamera + 2 kokpit") [`KAMERA_ISTASYONU` §1 ①②③ tutar · ④ beyanlı]
Izgara: ⛔ **DÜZ — 30 × 8,0** · ⚠️ BANDIN DIŞI (format 24 × 10,0) — sahip senaryosu 07.10.2026 · §DÜZ IZGARA BEYANI
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 07.10.2026 (TUR 2/3 · SAPMA ①–⑧)
Havuz kaydı: `apexait/YAYIN_PLANI.md` — ⬜ satır açılmadı (16:9 hattı dikey ızgaraya sayılmaz; sahip kararı bekliyor) · siluet ailesi: **dönüştürülmüş taşıt** (EDEN ARK ile aynı aile → ardışık yayınlanmaz)

_"İlk karede çayırda çamurlu yatağına gömülmüş, sarmaşıklı bir yolcu uçağı; son karede aynı uçak ağaçların hizasında, pencereleri yanan bir göl evi — eskiden yattığı yer su olmuş, altından bir kano geçmiş."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     30 sahne × 8,0 sn                       = 240,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     ⛔ YOK — sahip senaryosu 07.10.2026: "Ayrı beş saniyelik afiş bu revizyona eklenmemiştir"
               (THE BORROWED HILL emsali) · teslim son ana görüntüyle biter; ihrac_kontrol.sh --kart YOK
──────────────────────────────────────────────────────────────
TOPLAM                                                     240,0 sn
HIZ             1x (yatay hat 2x'e çevrilmez — 2x yalnız dikey paylaşım kuralıdır [DERS 58])
MÜZİK           ✅ VAR — yatay hat (sahip 05.10.2026) · THE_SLOW_TAKEOFF_MUZIK.md · müziksiz pencere 0,0–8,0 sn (S0 tamamı)
YASAK KELİME    takeoff · flight · flying · airborne · runway · airport · airline · livery · registration · landing · propeller · seaplane · floats · crash · wreck · passenger · pilot · boneyard · boeing · airbus
               ⭐ [DERS 59 · 42 · P23-b] hiçbir promptta, negatifte bile — uçak korpusu havalimanı, uçuş, kaza,
                  deniz uçağı ve uçak mezarlığı çağırır. Merdiven için "section · half-way platform", kano için
                  "lies / sits on the water" yazılır. ("airliner" kelimesi airline'dan ayrıdır — bilinçli.)
KELİME KİLİDİ   "crane" yalnız G0 · G1 · G3 · G4 + S0–S4 I2V [P7-e] · "canoe" yalnız G25'ten sonra [P24-e] ·
               "flood" yalnız G20 · G22 · G23 · "raised/elevated/lifted" STRUCTURE ve başlıkta YOK [P25-d · DERS 36]
BÖLÜM DOSYASI   BOLUM_1 = S0–S14 (0–120,0)  ·  BOLUM_2 = S15–S29 + USTA KARE (120,0–240,0)
QA BİRİMİ       FİLM (tek master × 5 mercek · ❶ ❷ ❸ kör · ❹ ❺ belgeli) — QA/HAM/THE_SLOW_TAKEOFF/
```

⛔ Kart olmadığı için platform son ekranı **son 5 saniyeye konmaz** ya da yalnız gök bandına konur (senaryo: "Platform son ekranı kullanılacaksa bitmiş yapının veya kano hareketinin üstüne yerleştirilmez").
⚠️ Son sahnenin (S29) son 4,0 sn'lik TUTUŞU final kanıtıdır (`QA_SPEC` §1): kano su yolu ağzında durulur, ışıklar yanık, başka hiçbir şey değişmez.
⭐ Platform küçük resmi (kapak) G30'dan gelir (sahip kararı 19.09.2026 — öncesi/sonrası bölme yok).

### ⭐ İZLEYİCİ KAPISI [C2-a…d · KILAVUZ_REHBERI §6]

```
İŞLEV ANI         S26 ışıklar gruplar hâlinde yanar → S28 kano gerçek hızda gövdenin ALTINDAN geçer →
                  S29 su yolu ağzında durulur. Olay S29'un ilk yarısında (0–4 sn), ikinci yarı TUTUŞ (4–8 sn).
AÇILIŞ NESNESİ    G0: çamurlu yatağında karnı üstünde yatan, sarmaşıklı yolcu uçağı (kadrajın ≈%44 eni) + ona
                  ne oluyor: vinç öndeki motoru kanattan ayırmış, taşıyor. 120 px'te uçak silüeti okunur.
DİRENÇ EKRANDA    ① ağırlık — S5–S6 gergin halatlar, çamurdan kopan gövde · ② su — S19–S20 kıyı çizgisi sağdan
                  çayıra yürür, kolon diplerini sarar; ev kuru · ③ kış — S18 kar, S19 erime
DÖNGÜ KAFİYESİ    G30 ↔ G0 aynı kadraj, aynı x: uçak x 537–1383 iki karede de; G0'da gövde altı çamurda (üstten
                  617), G30'da su üstünde (463) ve eski yatağın yerinde gölet + yansıma. İşlev anı (kano) kadrajda
                  KALIR [BACK TO WATER döngü 3 dersi]. Işık FARKLI, bilinçli: sabah 07:40 ↔ mavi saat.
MERAK SORUSU      Bu uçağa ne yapıyorlar?
AÇILIŞ DÜZENİ     ① NESNE uçak · ② DOKUNUŞ "From the first frame the engine is already moving" (vinç) ·
                  ③ İPUCU çayırdaki istif (kereste) — amacı okunmaz · ④ ÖLÇEK ekskavatör + iki işçi + kamyon ·
                  AÇILIŞ GERİ ÇEKİLMESİ ⛔ YOK (SG — sabit geniş; 1080p'de kırpma tavanı ölçülmedi)
```

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Göl kıyısında çürüyen bir yolcu uçağını bütünüyle yerden kaldırıp, altında su üstünde hayat olan bir
         göl evine dönüştürmek.
DİRENÇ   ① ağırlık (33 m tek parça gövde — iki çerçeve, dört strand jack, iki aşamalı kalkış)
         ② su (çayır gölün taşkın alanında — sel eski yatağı kaplar)  ③ çürüme (sarmaşık, kir, kırık cam)
         ④ kış (kar ve erime)
         EKRANDA NASIL [P1-b]:  S0 · vinçte motor  ·  S1 · şerit şerit sökülen sarmaşık  ·  S5–S6 · çamurdan
                                kopan gövde, büyüyen karanlık boşluk  ·  S19–S20 · sağdan yürüyen su, kolon dipleri
BEDEL    ⭐ Çamurlu yatağında yatan uçak — G0'da gövde altı üstten 617 (çayırda); S5'te kalkar, yerde baskı izi
         kalır (G6–G18); S20'de iz su altına girer (G22); S23'te gölete çevrilir; G30'da orada yalnız su ve ışık.
         Okuma bilinçli: "uçak tamir edildi" değil, "uçak yerinden kalktı ve yattığı yer suya döndü".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            çamurlu yatak + sarmaşıklı ölü gövde                              ✅
  □ kadrajda görünüyor mu?    gövde altı üstten 617 → 463 (154 px kalkış) · çukur alt %43 bandında ✅
  □ cevap "zaman geçiyor" mu? hayır — "yattığı yer su oldu, uçak ev oldu"                       ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: uçak yerde mi havada mı · kaç çerçeve · teras var mı · su nerede · kano nerede
② KİNETİK BAĞIMSIZLIK   ✅ her klipte makine, ekip, su ya da kano hareket eder (vinç · yıkama · ekskavatör · mikser ·
                           kriko · telehandler · iskele kuleleri · kar · su · ışık grupları · kano)
③ BAŞLIK ŞEMASI         ✅ kapak "THE SLOW TAKEOFF" (3 kelime) · ⚠️ sahip başlığı 63 karakter (kural ≤40) — YAYIN_PAKETI
④ OMURGA CÜMLESİ [P1-k] ✅ motor gider → sarmaşık gider → temeller dökülür → çerçeveler dikilir → beşik bağlanır →
                           yarıya kalkar → tepeye kalkar → çerçeveye oturur → teras çatılır → döşenir → merdiven →
                           camlar → yalıtım → kokpit köşesi → mutfak → yatak → korkuluk → donanım sökülür → kar →
                           erime + su → su yatağı kaplar → yağmurda kokpit → su çekilir → gölet + su yolu →
                           yeşerir → iskele + kano → ışıklar → biri iner → kano altından geçer → durulur
```

⚠️ **EDEN ARK ile aile benzerliği [P16-a]:** ikisi de dönüştürülmüş taşıt + mavi saatte su. AYIRICI FARK: EDEN ARK'ta
gemi suya İNER ve kadrajdan çıkar; burada uçak sudan YUKARI kalkar, ev yerinde KALIR ve su altına GELİR. Ardışık
yayınlanmaz (YAYIN_PLANI siluet ailesi kuralı).

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera (ana) · aynı kokpit kamerası (S13 · S21)
                          ② kanıt nesnesi: kayıkhane (x 1548–1698 · üstten 510–593 · 150 × 83 px · 31 ana karede birebir)
                          ③ çapa: meşe GÖVDESİ (x ≈163 · taban üstten 597 — taç mevsimle değişir, gövde değişmez)
                          ④ çapa: karşı kıyı çizgisi %50 (üstten 540) + ormanlı tepe sırtı (≈419) · ⑤ çapa: kaya (x ≈1728 · 732–924)
                          ⑥ tek rijit gövde: boy 846 px (x 537–1383) G0 → G30 ±2 px [P21-c] · yalnız KALKAR, büyümez
                          ⑦ kaldırma: vinç yalnız G0–G4; kalkış YALNIZ düşey, dört halat + iki semer, G5 gergin / G6 +3 / G7 +6
                          ⑧ insan: A/B'de iz ("soft motion streaks") · G'de tek figür, yüz okunmaz
P1.5 · fırsat buldukça   meşe yaprağı (yeşil → altın → bronz → çıplak → yeşil pus → tam yaprak) · çayır rengi ·
                          su kotu · silt çizgisi (G22 → G30 kolon diplerinde) · gölge süpürmesi (B: S2 · S9)
SPEC · yalnız belge      azimut/yükseklik dereceleri (kapı şartı) · px tabloları · kokpit px'leri
```

**Malzeme kimliği (her promptta):** *eskimiş kırık beyaz alüminyum gövde (tek boya, işaretsiz) · kırmızı astarlı çelik çerçeve · soluk ahşap teras ve iskele · gri çelik merdiven* — korpus: "documentary site photograph on colour negative film" [DERS 34 · 42].
**İnsan kararı:** ekip var — A/B'de iz, B'de daha silik; S27 tek kişi (A, iz); S28–S29 tek kişi kanoda (G, siluet, "no readable face"). S21 ve S26 kişisiz ("No people are present").
**Vinç / kaldırma kararı [DERS 8 · 22 · 46 · 57]:** sarı mobil vinç S0–S1'de (motor) ve S2 sonu–S4'te (kolon · kiriş · semer) — kanca her karede YÜKLÜ ("with a … on the hook"): G0 motor · G1 motor kamyon üstünde · G3 kolon · G4 semer; S1 ve S4 sonunda bomunu toplayıp kadrajdan çıkar. Gövdeyi vinç KALDIRMAZ: dört strand jack (çerçeve kirişlerinde) iki semeri çeker. ⚠️ S3'te üst kiriş +11,5 m'ye (üstten 322) çıkarken halat göğe/tepeye karşıdır — kısa sapan, kabul edilen risk [DERS 22].
**Korpus kararı [DERS 55]:** uçak korpusu çok uçaklıdır (mezarlık, apron) → SITE'ta 31 kez: "The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees."
**Yapı adı kararı [DERS 42 · P23-b]:** "portal frame" (konteyner vinci) → "steel frame, each two tall columns joined by a top beam" · "dock" (liman) → "short timber walkway" · "legs" (iniş takımı) → "columns" · "landing" (iniş) → "half-way platform".

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0,
                 yani en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp [A7-b]; kutu tam 8,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 30 sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.
                 ⭐ ⑧ "araç ilk + son kare alıyor mu" ve ⑨ kokpit istasyonu için ikinci referans görsel kabul ediyor mu.

┌─ KAMERA İSTASYONU (ANA) ─────────────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 (G26–G30 ISO 400) · tam kare YATAY │
│ yükseklik     h = +3,00 m (çayır seviyesinden) — çayırın güneyindeki alçak çimen │
│               sırtında beton kaideye cıvatalı tripod                          │
│ mesafe        D_eksen = 50,0 m (gövde eksenine) · D_kenar = 35,5 m (yakın kanat │
│               ucu) · gölet yakın kenarı 10 m [DERS 38]                         │
│ bakış açısı   bearing 0° (kuzey) · tilt 0° · roll 0°                           │
│ sabitleme     "bolted to a concrete footing on the low grassy bank"           │
│ ⛔ HESAP (KILAVUZ_REHBERI §2.8 · f=24 · yatay · yüzde ALT kenardan):            │
│    yüzde(y) = 50 + 118,5·(y − h)/D         x(m, eksenden) → %50 + 66,7·x/D    │
│    D = (H − h)/0,27  (taç %82)  → H = 16,5 (kuyruk, kalkış sonrası) → D = 50,0 │
│    gövde altı   y=0    → %42,9 (üstten 617) ✓ alt çeyreğin üstünde            │
│    ⭐ gövde altı y=+3,0 → %50,0 = KARŞI KIYI ÇİZGİSİ (G6 — doruk bir çizgide) [P4-b] │
│    gövde altı   y=+6,0 → %57,1 (463) · gövde üstü +9,8 → %66,1 (366)          │
│    taç (kuyruk) y=+16,5 → %82,0 (194) ✓ üst sekizin altında (G7–G30)          │
│    çerçeve kirişi +11,5 → %70,1 (322) · kolonlar x 740 · 1180 (yakın)         │
│    kanıt nesnesi kayıkhane → %45,1–52,8 · x 1548–1698 · 150 × 83 px            │
│    sol çapa meşe  x=−28 m (D 45) → x ≈163 px · taban %44,7 · taç %86,9 (142)    │
│    sağ çapa kayıkhane x=+44 m (D 85) → %84,5 · alt çapa kaya x=+6 m (D 10) → x ≈1728 │
│ ⛔ ÖN GÖRSELLEŞTİRME: 00_ANALIZ/02 §3 (betik: kamera · gövde · çerçeve · çapalar · │
│    gölet · yansıma bandı · kano rotası) — yansıma bandı üstten 786–883 (gövde · su D 12–17 m; kuyruk tepesi D 8,2 m → gölet 10 m'den başladığı için yansımaz) │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ KAMERA İSTASYONU (KOKPİT · detay · 2 klip) ──────────────────────────────────┐
│ "COCKPIT STATION — fixed clamp mount bolted to the rear wall of the cockpit,  │
│  lens 8.2 metres above the meadow, 2.4 metres from the windscreen, bearing    │
│  270 degrees, tilt 0 degrees, zero roll" · ufuk %50 · altı ön cam ≈1500 px    │
│ ① çapa: meşe tacı sol camlarda + karşı kıyı/tepe sırtı (ana SITE ile 2 ORTAK  │
│   CÜMLE, birebir — kapı ≥6 kelimelik ortak dizi arar [DERS 10]) ✓             │
│ ② istasyon kendi içinde sabit ✓ · ③ iki klip, aynı istasyon ✓                 │
│ ④ dış büyüme TAŞIMAZ: S13 S12 ile, S21 S20 ile AYNI on dakikadır (∥); dıştaki │
│   ana kare iki yakada aynıdır (S12 → G14 ← S14 · S20 → G22 ← S22) ✓           │
│ ⚠️ P2-e "detay ≤2 sn ek, merdiven satırı almaz" — AŞILDI, sahip kararı.       │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① MEŞE (SOL · gövde x ≈163 · taban üstten 597 · taç 142) — 16 m, kuru sırtta    │
│ ② KAYIKHANE (SAĞ · x 1548–1698 · üstten 510–593) — ⭐ KANIT NESNESİ, ahşap,   │
│    koyu şindıra çatı, kısa ahşap kazıklar üstünde (taşkında kazıklar ıslanır)  │
│ ③ KARŞI KIYI çizgisi %50 (540) + ormanlı tepe sırtı (≈419) — bütün kadraj eni  │
│ ④ KAYA (SAĞ ALT · x ≈1728 · üstten 732–924) — sırtın dibinde, likenli, 1,5 m   │
│ + "The meadow holds exactly one aircraft…" korpus kilidi — her SITE'ta birebir │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ ufuk %50 (tilt 0) · taç ≤ %82 · çalışma seviyesi ≥ %25 (çayır %42,9)          │
│ yanlar: solda meşe + merdiven dibi + kuru sırt · sağda kayıkhane + su yolu + kaya │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ (§2.8 varsayılanı) — kanıt nesnesi alt 100 px'e │
│ (üstten > 980) ve sağ üst 300×100 px'e (x > 1620 · üstten < 100) girmez ✓       │
│ ⚠️ kano G30'da x ≈1293 · üstten 624 — sağ alt süre damgası köşesine düşmez [A15-c] │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ uçak: dar gövde jet · boy 33,0 m · kanat açıklığı 29,0 m · gövde Ø 3,8 m ·    │
│   kuyruk tepesi gövde altından +10,5 m · 6 kokpit camı · tek sıra kabin penceresi │
│   (≈8 px — SAYILMAZ [A5-c]) · ön kabin kapısı (burundan 3,5 m) · kanat üstü çıkış │
│   · 2 motor kanat altında (S0'da öndeki gider; arkadaki gövdenin ardında, görünmez) │
│ gövde altı: G0–G5 0,0 m · G6 +3,0 · G7–G30 +6,0 (yakın yan D 48,1)             │
│ temel: 4 × (2,0 × 2,0 m) beton · x ±8,0 · D 46,5 ve 53,5                      │
│ çelik çerçeve: 2 adet · her biri 2 kolon (D 46,5 · 53,5) + 1 üst kiriş +11,5 · │
│   kırmızı astar · 4 strand jack (kiriş başına 2) S3–S17                        │
│ beşik: 2 kavisli çelik semer kirişi, uçları kolon braketlerine pimli (+5,7)    │
│ teras: çelik çerçeve + ahşap döşeme 9 × 7 m · kot +7,2 · 4 ince dikme ·        │
│   korkuluk + sönük lamba dizisi (S16) · 2 bank · 4 saksı                       │
│ merdiven: 2 kesit çelik + ahşap basamak + ara platform · kapı eşiği +8,0 →     │
│   kuru sırt +1,0                                                              │
│ gölet: ≈30 × 40 m (D 10 → 55 · x −15 → +15) · su yolu ≈25 m (sağa, göle) ·     │
│   yürüyüş iskelesi 6 m (x −11) · kano 5,0 m koyu yeşil ahşap                   │
│ STRUCTURE'ın İngilizce tam hâli tek cümle (DERS 36): "When finished this will be │
│   a lake house made from one retired twin-engine jet airliner, 33 metres long,  │
│   with a timber terrace round its near wing." — 33 promptta BİREBİR            │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 30 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az yapı göstermez (sökümler GEÇİCİ ekipmandır).
> Kış İKİ sahne: S18 birikme · S19 erime [DERS 7 · 26]. Su iki yönlü: S19–S20 yükselir, S22 çekilir — negatif
> tek yönlü kilit yazmaz [P16-c]. ∥ = kokpit klibi, bir önceki ana klibin AYNI on dakikası.

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | İSTASYON | KANIT NESNESİ (px) |
|:-:|:-:|---|---|---|:-:|:-:|:-:|---|
| 0 | 8,0 | SÖKER | öndeki motor kanatta → vinçte, kamyonun üstünde (%100) | 1 gün | A | 07:40→07:50 | ANA | motor kanatta → kamyon üstünde (x 932 → ≈1340) |
| 1 | 8,0 | TEMİZLER | sarmaşık + kir %100 → %0 · motor kamyonda, vinç gider | 1 hafta | A | 07:50→08:00 | ANA | sarmaşık kütlesi burunda → branda yığını |
| 2 | 8,0 | DÖKER | temel 0 → 4 (%100) · gövde temiz | 3 hafta | B | 08:00→10:00 | ANA | temel 0 → 4 (yakın iki: x 740 · 1180) |
| 3 | 8,0 | DİKER | çerçeve 0 → 2 (kolon 4 · üst kiriş 2) %100 | 1 hafta | A | 10:00→10:10 | ANA | kolon 0 → 4 · üst kiriş 0 → 2 (üstten 322) |
| 4 | 8,0 | BAĞLAR | beşik 0 → 2 · halat 0 → 4 gergin · uçak yerde | 1 hafta | A | 10:10→10:20 | ANA | semer 0 → 2 · halat 0 → 4 gergin |
| 5 | 8,0 | KALKAR ① | uçak 0 → +3,0 m (%50) · halatlar çeker | yarım gün | A | 10:20→10:30 | ANA | ⭐ gövde altı üstten 617 → 540 (ufuk) |
| 6 | 8,0 | KALKAR ② | uçak +3,0 → +6,0 m (%100) | yarım gün | A | 10:30→10:40 | ANA | ⭐ gövde altı 540 → 463 · kuyruk 271 → 194 |
| 7 | 8,0 | OTURTUR | yük halattan çerçeveye (%100) · halatlar gevşer | 2 gün | A | 10:40→10:50 | ANA | halat gergin → gevşek |
| 8 | 8,0 | ÇATAR | teras çerçevesi 0 → %100 (dört ayak · kiriş) | 1 hafta | A | 10:50→11:00 | ANA | teras çerçevesi (üstten ≈400) |
| 9 | 8,0 | DÖŞER | teras döşemesi %0 → %100 (burundan kuyruğa) · istif → 0 | 1 hafta | B | 11:00→13:00 | ANA | döşeme yönü burun → kuyruk · istif → 0 |
| 10 | 8,0 | KURAR | merdiven 0 → 2 kol + sahanlık (%100) | 3 gün | A | 13:00→13:10 | ANA | merdiven: kapı x 614 / üstten 407 → dip x 320 / 601 |
| 11 | 8,0 | CAMLAR | cam: bulanık → yeni (%100, burundan kuyruğa) · kanat üstü kapı açılır | 1 hafta | A | 13:10→13:20 | ANA | cam sırası bulanık → koyu |
| 12 | 8,0 | YALITIR | kabin içi: yalıtım + zemin (palet 4 → 0 · vekil: eksilen yük) | 2 hafta | A | 13:20→13:30 | ANA | palet 4 → 0 (kamyon x ≈320) |
| 13 | 8,0 | DONATIR | kokpit köşesi: boş → iki koltuk · masa · lamba · kilim (%100) | 2 gün | A | 13:20→13:30 ∥ | KOKPİT | kokpit: boş → 2 koltuk · masa · lamba |
| 14 | 8,0 | YERLEŞTİRİR | mutfak: tezgâh + dolaplar (sandık 3 → 0 · kanat kapısından) | 1 hafta | A | 13:30→13:40 | ANA | sandık 3 → 0 (kamyon x ≈1540) |
| 15 | 8,0 | TAŞIR | yatak: çerçeve + şilte (yük 2 → 0 · merdivenden) · iç donanım tamam | 2 gün | A | 13:40→13:50 | ANA | yatak yükü 2 → 0 |
| 16 | 8,0 | ÇEVİRİR | teras: korkuluk (+ sönük lamba dizisi) + 2 bank + 4 saksı (%100) | 1 hafta | A | 13:50→14:00 | ANA | korkuluk bandı (üstten ≈400) |
| 17 | 8,0 | SÖKER ② | kaldırma donanımı 4 → 0 · iskele 2 → 0 (söküm %100) | 3 gün | A | 14:00→14:10 | ANA | kriko 4 → 0 · iskele 2 → 0 |
| 18 | 8,0 | KARLANIR | kış ①: yaprak → 0 · kar 0 → ince örtü | ≈2 ay | B | 14:10→16:10 | ANA | meşe yaprak → çıplak · kar 0 → ince |
| 19 | 8,0 | YÜKSELİR | kış ②: kar erir · göl çayıra girer (%0 → %40) | 3 hafta | B | 16:10→18:10 | ANA | kar → çamur · su kıyıdan çayıra |
| 20 | 8,0 | KAPLAR | su: eski yatak + ayaklar (%100) · ev kuru | 1 hafta | A | 18:10→18:20 | ANA | su: yatak + kolon dipleri (üstten <617) |
| 21 | 8,0 | SIĞINIR | kokpit: yağmur · su aşağıda (iç mekân değişmez) | 1 akşam | A | 18:10→18:20 ∥ | KOKPİT | kokpit: yağmur · su aşağıda |
| 22 | 8,0 | ÇEKİLİR | su %100 → çukurda kalan (gölet ön hâli) | 2 hafta | A | 18:20→18:30 | ANA | su → çukurda kalan · silt çizgisi |
| 23 | 8,0 | KAZAR | gölet kıyısı + su yolu 0 → %100 (göle bağlanır) | 2 hafta | A | 18:30→18:40 | ANA | su yolu 0 → göle bağlı |
| 24 | 8,0 | YEŞERTİR | kıyı bitkileri %0 → %100 · basamak taşları | 2 hafta | A | 18:40→18:50 | ANA | kıyı bitkisi · basamak taşı |
| 25 | 8,0 | İNDİRİR | iskele 0 → %100 · kano suya | 1 hafta | A | 18:50→19:00 | ANA | iskele 0 → 6 m · kano suya |
| 26 | 8,0 | YANAR | ışık: 0 → kabin + teras + merdiven (%100, gruplar) | 10 dk | A | 19:00→19:10 | ANA | ışık grubu 0 → 4 |
| 27 | 8,0 | İNER | bir kişi: kapı → merdiven → iskele → kano | 10 dk | A | 19:10→19:20 | ANA | kişi kapı → kano |
| 28 | 8,0 | SÜZÜLÜR | kano: iskele ucu → gövdenin altı, orta (gerçek hız · ~13 m) | 8 sn | G | 19:20 (+8 sn) | ANA | kano x 608 → 960 |
| 29 | 8,0 | DURULUR | kano: gövdenin altı → su yolu ağzı, durulur (final tutuş) | 8 sn | G | 19:20 (+8 sn) | ANA | kano x 960 → 1293 · tutuş |

```
IZGARA          120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · kesmeler 8,0 · 16,0 · … · 232,0  (29 kesme, her 8,0 sn)
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: sahibin kendi senaryosu (30 × 8,0 = 4:00, 07.10.2026) ve 8,0 sn üretim düzeni; yatay
                       hatta THE OLD ROAD (15 × 8,0) · THE EDEN ARK (18 × 8,0) emsali. ⚠️ BANDIN DIŞI: format 24 × 10,0.
                   (b) ritim klip İÇİNE: ① rejim nabzı — B'ler S2 · S9 (gölge süpürmesi) · S18 · S19 (kar, su), G'ler
                       S28 · S29 (gerçek hız — final yavaşlar); ② iş yönü değişir: yana (S0 motor) · burundan kuyruğa
                       (S1 temizlik · S9 döşeme · S11 cam) · YUKARI (S5–S6 kalkış) · aşağı (S18 kar) · sağdan sola (S19–S20
                       su) · soldan sağa (S26 ışık · S28–S29 kano); ③ müzikte katman = aşama (MUZIK.md) ④ istasyon nabzı:
                       iki kokpit eki (S13 · S21) iç/dış soluğu.
                   (c) kabul edilen risk: eşit klipte ❷ RHYTHM kategorisi NOT TRIGGERED (beş mercekli rubrik) — METRONOM
                       hükmü artık verilmez; sapma kurgudan gelirse (klip ≠ 8,0) ❷ açılır ve ❺ final saniyesi kayar
                       [IRON BRIDGE · GLASS WALL]. Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
REJİM SAYISI    ⚠️ ÜÇ rejim (A · B · G) — SANTIYE_HAREKETI §2 sınırı iki. Gerekçe: B gölge süpürmesini ve kar birikimini
                taşır [A12-j], G sahibin "son sekiz saniye normal hızda" isteğidir; geçişler KESMEDE (S27 → S28) [P5-c].
                Emsal: BACK TO WATER (A+B+G, beyansız düştü) → burada BEYANLI.
IŞIK GÜNÜ       Σ pencere = 22 A × 10 dk + 4 B × 2 sa + 2 G × 8 sn = 3 sa 40 dk + 8 sa = 11 sa 40 dk ≤ 14 ✓
                (kokpit ekleri S13 ∥ S12 · S21 ∥ S20 — toplama girmez)  · 07:40 → 19:20 (mavi saat, güneş −4,4°)
BÖLÜM SINIRI    G15 — sahne S14 son karesi = sahne S15 ilk karesi (ANA istasyon); gövde altı %57,1, gölge +39°,
                ince yüksek bulut, meşe bronz — ikisinde de aynı [DERS 52]. Kokpit eki S13 sınıra DÜŞMEZ (SAPMA ⑧).
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: KAYIKHANE — G0'da ve usta karede (G30) aynı konum (x 1548–1698 · üstten 510–593) ve aynı
        boy (150 × 83 px) [DERS 25]; taşkında (G20–G22) kazıkları ıslanır, gövdesi değişmez. Yedek: meşe GÖVDESİ x ≈163.
LOOP    G30 ↔ G0: aynı kadraj · aynı çapalar · aynı uçak x'i (537–1383) · ışık FARKLI (bilinçli — G0 07:40 sabah, G30
        mavi saat; tek gün): çamurda yatan ölü uçak / suyun üstünde yanan ev. Biçim kafiyesi: gövde altının yeri
        çamur (617) → su + yansıma (463 ve gölette 786–883).
SÖKÜM   S1 vinç + kamyon (motorla) · S4 vinç · S15–S17 boş sandıklar, kamyonlar · S17 dört strand jack + halatlar +
        iki iskele kulesi (telehandler ve işçiler TAŞIR) · S22 kum torbaları (palete, yükleyiciyle) · S25 telehandler
        + kamyon — ekranda gider; çerçeveler, semerler, teras, merdiven KALIR (kalıcı taşıyıcı) [DERS 48 · P2-h]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
öndeki motor (giden)     → vinç kancası → kamyon kasası (sağ ön)                         → G0 · G1
sarmaşık, kesilen huş     → burun altında branda yığını · römork                         → G1 · S1
temel betonu, donatı      → ekskavatör yanında donatı kafesi yığını · mikser (çakıl yol)  → G2
kolon, üst kiriş, kriko   → uzun kamyon (S2 sonunda gelir)                               → G3
semer kirişi              → aynı kamyon · vinç kancası                                   → G4
pim, braket               → telehandler paleti                                           → G5–G7
teras çeliği, dikme       → uzun kamyon (sağ) + kazık makinesi                           → G8
döşeme tahtası            → kamyon kasasında yüksek istif                                → G9
merdiven kesitleri        → kuru sırtta kamyon                                           → G10
cam                       → kamyonda sandıklar · iskele kuleleri                         → G11
yalıtım, zemin            → merdiven dibinde kamyonda 4 palet                            → G12
kokpit mobilyası          → kabinden el arabası (kokpit istasyonu)                        → G13
mutfak                    → sağda kamyonda 3 sandık + tezgâh (telehandler → kanat kapısı) → G14
yatak                     → merdiven dibinde küçük kamyon                                → G15
korkuluk, lamba dizisi, bank, saksı → sağda kamyon                                       → G16
kum torbası               → yükleyici paleti (çakıl yol)                                 → S19
taş, bitki, toprak        → çakıl yolda palet · römork · toprak yığını                    → G23 · G24
iskele kerestesi, kano    → merdiven dibinde küçük kamyon                                → G25
su (sel)                  → göl kıyısı, sağ arka (kayıkhane kazıkları)                    → S19
GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL (prompta yalnız vekil girer):
   kabin yalıtımı/zemini → eksilen 4 palet + merdivende taşıyan iz · mutfak → eksilen 3 sandık + kanat kapısı ·
   yatak → merdivenden giren uzun soluk yük · kokpit köşesi → KOKPİT İSTASYONU (S13, sahip kararı) ·
   elektrik → S26 ışık grupları · temel kazıkları → kazık makinesi · gövde içi beşik bağlantısı → gergin halat
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① ışıklı ev — kokpit ve gövde boyunca pencere sırası, teras ve merdiven lambaları (ilk okunan, en parlak)
   → ② göletteki yansıma (üstten 786–883) → ③ su yolu ağzında kano (x ≈1293 · 128 px) → ④ aynı kayıkhane (kanıt)
FİNAL KARE KANITI  ffmpeg -ss 239.0 -i teslim.mp4 -frames:v 1 kanit.jpg   (S29 tutuşu 236,0–240,0 içinde · mavi saat,
                   okunur [DERS 45]) · kart YOK → son kare = G30
```

---

## 🖼️ KARE TABLOSU — 31 ana görsel + 2 kokpit son karesi [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Gölge yönü kadrajda: 0 = kameradan uzağa · − sola · + sağa (|x| > 90 = kameraya doğru). Güneş DİSKİ anılmaz.
> 🪟 = KOKPİT istasyonu. S12 I2V'si G14'e, S20 I2V'si G22'ye biter (ana); G13 → G13′ ve G21 → G21′ kokpit eki.

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| G0 | 07:40 | 100° | 25,7° | -80° | soluk sabah, küçük yüksek bulut · gölde ince sis | meşe koyu yeşil · çayır yeşil (yaz sonu) | ⭐ AÇILIŞ — uçak karnı üstünde çamurlu yatakta · sarmaşık · motor vinçte |
| G1 | 07:50 | 102° | 27,4° | -78° | aynı | aynı | motor kamyon üstünde asılı |
| G2 | 08:00 | 104° | 29,1° | -76° | açık | aynı | gövde temiz · temel yerleri işaretli |
| G3 | 10:00 | 134° | 46,9° | -46° | açık mavi, küçük küme | çayır sararıyor · meşede ilk sarı | 4 temel · vinçte ilk kolon |
| G4 | 10:10 | 137° | 48,1° | -43° | aynı | aynı | 2 çerçeve · vinçte semer |
| G5 | 10:20 | 141° | 49,2° | -39° | aynı | aynı | halatlar gergin · uçak yerde |
| G6 | 10:30 | 144° | 50,2° | -36° | aynı | aynı | ⭐ gövde altı +3,0 m (ufukta) |
| G7 | 10:40 | 148° | 51,2° | -32° | aynı | aynı | ⭐ gövde altı +6,0 m · halat gergin |
| G8 | 10:50 | 151° | 52,0° | -29° | aynı | aynı | yük çerçevede · halat gevşek |
| G9 | 11:00 | 155° | 52,8° | -25° | aynı | meşe sararıyor | teras çerçevesi |
| G10 | 13:00 | 205° | 52,8° | +25° | yumuşak mavi, dağınık bulut | meşe altın | teras döşeli |
| G11 | 13:10 | 209° | 52,0° | +29° | ince yüksek bulut | meşe bronz | merdiven · iskele kuleleri |
| G12 | 13:20 | 212° | 51,2° | +32° | aynı | aynı | camlar yeni · 4 palet |
| G13 | 13:20 | 212° | 51,2° | kokpit içi (sol camlardan ışık lekesi) | aynı (kokpitten) | meşe bronz (camdan) | 🪟 kokpit boş, kaplı |
| G13′ | 13:30 | 216° | 50,2° | kokpit içi (sol camlardan ışık lekesi) | aynı | aynı | 🪟 kokpit köşesi döşeli · lamba |
| G14 | 13:30 | 216° | 50,2° | +36° | aynı | aynı | kabin kaplı · mutfak kamyonda |
| G15 | 13:40 | 219° | 49,2° | +39° | aynı | meşe bronz, seyrek | ⭐ BÖLÜM SINIRI — mutfak içerde · yatak merdiven dibinde |
| G16 | 13:50 | 223° | 48,1° | +43° | kalınlaşan yüksek bulut | meşe kahve | iç tamam · teras kenarı açık |
| G17 | 14:00 | 226° | 46,9° | +46° | gri bulut tabakası | meşe kahve, neredeyse çıplak | teras tamam (sönük lamba dizisi) · kriko + iskele |
| G18 | 14:10 | 229° | 45,6° | +49° (soluk · kapalı gök) | kapalı gri | meşe kahve · gri gök (kış kapıda) | ev ilk kez temiz · pencereler karanlık |
| G19 | 16:10 | 258° | 27,4° | +78° (soluk · kapalı gök) | kapalı, kar sonrası | ⭐ meşe çıplak · ince kar | kar örtüsü · kokpitte tek ışık |
| G20 | 18:10 | 280° | 7,1° | +100° | kırık yağmur bulutu, altta ışık bandı | kar yok · su çayırda · meşede ilk yeşil pus | su çukurun kenarında · kum torbaları |
| G21 | 18:10 | 280° | 7,1° | kokpit içi (gölge yok) | yağmur (kokpitten) | yağmur · su aşağıda (camdan) | 🪟 kokpit: fincan · kitap · yağmur |
| G21′ | 18:20 | 282° | 5,4° | kokpit içi (gölge yok) | aynı, koyulaşır | aynı | 🪟 aynı, su biraz yüksek |
| G22 | 18:20 | 282° | 5,4° | +102° | incelen bulut, alçak sıcak ışık | ⭐ taşkın doruğu | su doruğu · ev kuru |
| G23 | 18:30 | 284° | 3,7° | +104° | açılan, altın | su çekildi · çayır yeşil filiz · meşe açık yeşil | çekilmiş su · ıslak çukur · işaretli su yolu hattı |
| G24 | 18:40 | 285° | 2,1° | +105° | altın | gölet + su yolu · bahar | gölet + su yolu açık |
| G25 | 18:50 | 287° | 0,4° | — (güneş ufkun altında) | gün batımı, sol altın | kıyı bitkili | kıyı bitkili · basamak taşları · iskele malzemesi + kano kamyonda |
| G26 | 19:00 | 289° | −1,2° | — (güneş ufkun altında) | art ışık solda, mavi sağda | yaz başı · meşe tam yaprak | iskele + kano bağlı · ışıklar sönük (kokpit hafif) |
| G27 | 19:10 | 291° | −2,8° | — (güneş ufkun altında) | mavi saat | aynı | bütün ışıklar yanık |
| G28 | 19:20 | 293° | −4,4° | — (güneş ufkun altında) | derin mavi saat | aynı | kano iskeleden ayrılıyor |
| G29 | 19:20 +8 sn | 293° | −4,4° | — (güneş ufkun altında) | aynı | aynı | kano gövdenin altında |
| G30 | 19:20 +16 sn | 293° | −4,4° | — (güneş ufkun altında) | ⭐ derin mavi saat | aynı | ⭐ USTA KARE — kano su yolu ağzında · ev ışıklı · yansıma |

```
SU KOTU (kare kilidi [P10-e])   G0–G19 göl kendi kıyısında (çayır kuru; çukurda durgun su YOK [DERS 54]) ·
   G20 su sağdan çayıra girdi, çukurun uzak kenarında · G22 doruk: bütün alçak çayır, kolon dipleri, kamera sırtının
   dibine kadar · G23 çekildi: çukur + önündeki alçak alan ıslak havuz · G24–G30 gölet (−0,3 m) + su yolu, göl kotunda
   TANIK ÇİZGİ [P10-g]: G22'den G30'a kolon diplerinde ve kayıkhane kazıklarında soluk silt bandı, aynı yükseklikte
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G30 usta kare → G29 (kano geri, gövdenin altına) → G28 (kano iskelede) → G27 (kişi yok, kapı kapalı) → G26 (ışıklar
   sönük) → … → G22 (taşkın doruğu) → G20 → G19 → … → G15 (bölüm sınırı) → G14 → G12 → … → G0
   KOKPİT: G13′ önce (G14'ün mevsimi/ışığıyla) → G13 (mobilya çıkarılır) · G21 G13′'den (fincan, kitap, yağmur, su —
   G22'nin mevsimiyle) → G21′ G21'den. Kokpit kareleri ana zincire zincir_kontrol ile BAĞLANMAZ (başka istasyon).
   sonra I2V S0 (G0→G1) … S29 (G29→G30) — her klip iki uca kilitli, üretim 9,0 sn, baştan 1,0 kırp
```

## 🧪 PİLOT ÜÇLÜ [DERS 62 · KILAVUZ_REHBERI §8 adım 2b]

```
⛔ Üretim başlamadan, aşağıdaki üçü geçmeden kalan klipler üretilmez:
① FİNAL      G30 + G29 + S29 — mavi saat, ışıklı ev, yansıma, gerçek hızda kano ve 4 sn tutuş [C1-b]
② EN BÜYÜK   G5 + G6 + G7 + S5 + S6 — iki aşamalı kalkış: tek rijit gövde, salt düşey, dört gergin halat,
   DEĞİŞİKLİK  aynı x (537–1383 ±2 px), çamurda baskı izi [DERS 57 · P21-c] · S5 = 00:40
③ DİRENEN    G20 + G22 + S20 — taşkın: su sağdan gelir, kolon diplerini sarar, ev kuru kalır, yapı GERİLEMEZ
              [IRON BRIDGE 00:51 dersi] · + kokpit S13 (istasyon değişimi, ❶ SEPARATE IMAGES riski)
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     47,0° K · ışık günü tarihi: δ +12° (ışık tek gün; takvim sahadan) · doğuş 05:07 · batış 18:53 (güneş
                saati) · kamera bakışı 0° (kuzey) → kadraj −37° … +37° · güneş 100° → 293°: sabah sağ-arkada, öğle
                arkada (ön yüz aydınlık), akşam sol-arkada — HİÇBİR karede kadrajda değil [P8-h]
                ⚠️ kokpit istasyonu batıya (270°) bakar: S21'de güneş (280°, +7°) kadraj içindedir → yağmur bulutunun
                ARKASINDA yazılır ("hidden behind the dark rain clouds")
MEVSİM YAYI     yaz sonu (G0–G2) → sonbahar (G3–G17: meşe yeşil → altın → bronz → kahve) → kış (G18–G19: çıplak,
                kar) → bahar (G20–G25: erime, sel, yeşil pus → açık yeşil) → yaz başı (G26–G30: tam yaprak)
                taşıyıcı: MEŞE YAPRAĞI (ana) · çayır rengi · kar · su kotu
GÖLGE SÜPÜRMESİ rejim B klipte: S2 (sabah, −76° → −46°: 30°) · S9 (öğle, −25° → +25°: 50°) · S18–S19 kapalı gök
                (süpürme yok — taşıyıcı kar ve su [DERS 40]) · rejim A klipte fark edilmez → yüzeyle kanıtlanır
KIŞ             S18 (yaprak düşer · kar birikir — rejim B [A12-j]) · S19 (kar erir · çamur · su gelir) — tek klipte
                başlayıp bitmez [DERS 7 · 21 · 26]; G19 kar karesi ayrı üretilir
GECE            yok · final MAVİ SAAT, güneş −1,2° → −4,4° (S26–S30) — sahip kararı 07.10.2026 · zifiri değil:
                gövde, yansıma ve kano okunur, ışıklar kadrajın en parlak kaynağı [DERS 45]
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   ANA: h +3,00 · D_eksen 50,0 · D_kenar 35,5 · bakış 0° · tilt 0 · roll 0
         KOKPİT: h +8,2 · ön cama 2,4 m · bakış 270° · tilt 0 · roll 0 (yalnız S13 · S21)
YAPI     uçak 33,0 m · x 537–1383 (846 px) · gövde altı 617 → 540 → 463 · kuyruk 348 → 271 → 194 (%82,0)
         çerçeve 2 · kolon x 740 · 1180 · kiriş üstten 322 · teras +7,2 · merdiven kapı (614, 407) → dip (320, 601)
ÇAPALAR  ① meşe gövdesi x ≈163 · taban 597 · ② kayıkhane x 1548–1698 · 510–593 · ③ karşı kıyı %50 (540) ·
         tepe sırtı ≈419 · ④ kaya x ≈1728 · 732–924 · kanıt nesnesi kayıkhane 150 × 83 px
IZGARA   30 × 8,0 · 120 BPM · kesmeler 8,0 · 16,0 · … · 232,0  (29 kesme, her 8,0 sn) · kart YOK · 240,0 sn
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_4_dk_filmler/THE_SLOW_TAKEOFF   → BLOCK 0 · FIX 19 (07.10.2026)
✅ FIX'ler ve beyanları (hepsi elle okundu):
   · ARAÇ KUTU SETİ ölçülmedi — beyanlı; üretim araç kapısıyla açılır
   · süreler eşit (8,0) — sahip ızgarası; beş mercekte ❷ RHYTHM eşit klipte tetiklenmez
   · S21 (kokpit, yağmur) · S26 (ışıklar) · S27 (bir kişi iner) · S28–S29 (kano, gerçek zaman): ACTIVITY'de ≥3 el /
     geçişli fiil / malzeme akışı YOK — KASITLI: bunlar ödül ve sakin anlardır, şantiye bitti [P4-f · C1-d]; ❸'e
     PARKED gerekçesi SPEC §5 DECLARED WORLD'de
   · DERS 61 "YENİ eleman" ×2 (S13 → G14 terrace/tower · S21 → G22 column/terrace) — YANLIŞ ALARM: kapı kokpit karesini
     (G13 · G21) bir sonraki ANA kareyle karşılaştırıyor; o elemanlar ana zincirde G9 ve G11'den beri var
✅ YASAK KELİME taraması 0 · kelime kilitleri (crane G0–G4 · canoe G25+ · flood G20–G23) betikle doğrulandı
✅ 00_ANALIZ altı dosya + okuma çizelgesi 117/117 · hikâye onayı 07.10.2026 (TUR 2/3 · SAPMA ①–⑧ sahip okur)
⛔ ARAÇ KAPISI koşulmadı → THE_SLOW_TAKEOFF_URETIM_GUNLUGU.md §0
⛔ PİLOT ÜÇLÜ koşulmadı → S29 · S5–S6 · S20 (+ S13)
```
