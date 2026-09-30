# 🏗️ THE_GLASS_WALL — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **12 × 10,0 sn = 120,0 sn** | Kapak kartı: **5,0 sn** | Toplam: **125,0 sn**
Prompt yapısı: ⭐ **12 sahne → 13 görsel (G0…G12) + 12 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G6** · ara kare YOK
Yapı: **çelik çerçeve cam sera (24 × 10 m, h 5,5 m) + taş çiftlik evi (8 × 6 m) + kuru taş teras duvarları** (yeni tür · `YAPI_TIPI_KARTLARI` §9 VİLLA uyarlama + §10 şablonu) · Saha: **kıyı tepe hibrit — denize bakan yeşil tepe (+85 m)** (`SAHA_VE_IKLIM_KARTLARI` §3.3 KIYI + §3.4 DAĞ/EĞİM)
Zaman yayı: **8 ay (Mart → Ekim) → 120 saniye** · film mertebe anlatır: *"approximately eight months, from early spring to late autumn"* [P1-c]
Işık günü: **06:00 → 20:00 · tek ışık gününe sıkıştırılmış** — kesmede ışık atlamaz [§2.7 ①]; 8 ay takvim ile 14 saatlik ışık penceresi AYRI kavramlar: mevsim taşıyıcısı ot rengi + deniz rengi ile ayrılır, güneş açısı tek günlük sırayla tutarlı
Kamera mimarisi: **MAIN STATION** — tek istasyon, 12 sahne + usta kare (detay istasyonu YOK) [`KAMERA_ISTASYONU` §1]
Izgara: ⛔ **DÜZ — 12 × 10,0** · sahip beyanı · karşı kayıt ve kabul edilen risk §AŞAMA MERDİVENİ'nde
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 28.09.2026 · TUR 1/1
Havuz kaydı: `apexait/YAYIN_PLANI.md` §5 #5 THE GLASS WALL · siluet ailesi **YATAY**

_"Yabani tepe sekiz ayda birine ait olur — kazanılan düzen, kaybedilen yabanıllık."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     12 sahne × 10,0 sn                       = 120,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn                           =   5,0 sn   ← SAHNE DEĞİL, ayrı denetlenir
               ⛔ KONUM: teslimin SON 5 saniyesi (120,0–125,0) [A1-b]
──────────────────────────────────────────────────────────────
TOPLAM                                                     125,0 sn
BÖLÜM DOSYASI   BOLUM_1 = S0–S5 (0–60,0)  ·  BOLUM_2 = S6–S11 + USTA KARE (60,0–120,0)
QA BİRİMİ       FİLM (tek master × 12 mercek)
```

⛔ Kapak kartı **usta kareden (G12)** türetilir ve üstüne **İngilizce başlık** dizilir: `THE GLASS WALL` (`THE_GLASS_WALL_KAPAK.md`).
⚠️ S11'in son ≥2,0 sn'lik TUTUŞU final kanıtıdır (`QA_SPEC` §1); kart hareketsiz ve yazılıdır — iki ayrı iş.

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Akdeniz kıyısına bakan yabani bir tepede, eğim kuru taşla teraslanır, taş
         çiftlik evi yükselir, çelik çerçeve cam sera kurulur ve ilk hasat kasası seranın
         önüne konur. Video başlamadan var olan iş: güzergâh seçimi, sarnıç çukuru, tera-
         slama hattı belirleme.                                                           ✅

DİRENÇ   ① EĞİM — tepe yamacı %18; kuru taş teras olmadan zemin yok
          ② RÜZGÂR — denize bakan açık tepe poyrazına maruz; cam montajı sırasında
             geçici koruma iskelesi kadrajda görünür (S5–S7)
          ③ MEVSIM YARIŞI — cam kapanması Ekim donundan önce bitmeli; geç kalırsa
             kış ilk fidanları öldürür
          EKRANDA NASIL [P1-b]:
            S1–S2 · teras taşları elle sıralanır; taş yığını azalır, duvar büyür
            S5–S8 · koruma iskelesi görünür, S8'de sökülüyor
            S8    · yağmur damlaları yeni cama düşüyor — mevsim yarışı görünür son sahne  ✅

BEDEL    Yabani tepenin kendisi. G0'da %95 çıplak maki, ot, taş çıkıntı — kimsenin
         olmayan toprak. Kademeli gidiş: S1–S2 teras, S3–S4 ev ayak izi, S5–S8 sera
         zemin, S9–S10 tarhlar. G12'de %5 çıplak toprak. Sahnede tamamlanıyor: G12.
         Okuma bilinçli: "doğa bozuldu" değil, "tepe sahiplenildi".                      ✅

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            yabani tepenin boşluğu ve kendiliğindenliği               ✅
  □ kadrajda görünüyor mu?    evet — çıplak toprak %95 → %5; her karede sayılabilir      ✅
  □ cevap "zaman geçiyor" mu? hayır                                                       ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ      ✅ G7 donmuş karede: 40/64 cam panel, iskele tam kurulu, deniz
                          ufuku %50, palet azaldı — "sera bitmek üzere, kaç panel kaldı" bir saniyede
② KİNETİK BAĞIMSIZLIK ✅ Sabit kadrajda: teras taşları yığılır, kemer sıralanır,
                          cam paneller birer birer kaplanır, yeşillik içeriye dolar
③ BAŞLIK ŞEMASI       ✅ Kapak: "THE GLASS WALL" (3 kelime) · başlık ≤40 karakter
④ OMURGA CÜMLESİ      wild hilltop scraped → lower terrace rises → upper terrace cut →
   [P1-k]              farmhouse foundation laid → roof closes, slab poured →
                        six arches up, scaffold wraps → twelve arches, first glass →
                        forty panels glazed → fully sealed, scaffold gone →
                        benches fitted, beds marked → seedlings in, gutter connects →
                        harvest crate on stone path, chimney smoke, sea beyond
                        (12 vuruş, her biri ≤4 kelime; merdiven bundan türedi)
```

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera  ② ZEYTİN AĞACI (SOL · x %8–15 · ≈180 px boy ·
                          13 karede birebir — kanıt nesnesi)  ③ sol çapa: zeytin ağacı %x8–15
                          ④ sağ çapa: kayalık çıkıntı %x82–90 ≈200 px  ⑤ deniz ufuku %50,00
                          sabit her karede  ⑥ tek parça yerleşke — çerçeve büyür, cam dolar,
                          yeşillik artar; hiçbir şey eksilmez S8'e kadar  ⑦ vakum lifter görünür,
                          panel havada asılı kalmaz [DERS 57]  ⑧ ayrı insan figürü yok (streak
                          cümlesi · rejim); "no workers" YAZILMAZ [DERS 33]
P1.5 · fırsat buldukça   ot rengi (Mart yeşil → Haziran altın → Ağustos kuru → Eylül yeşil) ·
                          deniz rengi (Nisan açık → Ağustos kobalt → Ekim koyu) · cam şeffaflığı
                          (içi görünmeye başladığı an) · taş duvar harcının kuruma rengi
SPEC · yalnız belge      24 m × 10 m × 5,5 m sera · 8 × 6 m ev · teras duvarı h 0,9 m ·
                          64 panel · 12 kemer · palet konumu · azimut/yükseklik dereceleri
```

**Malzeme kimliği (her promptta):** *dark-green painted steel arched frames · partly translucent greenhouse glass with growing benches visible inside · rough-coursed limestone farm walls with lime mortar · terracotta ridge tiles · dry-stone retaining terraces with coarse pale limestone · Mediterranean terracotta soil* — korpus cümlesi [DERS 34 · 42]: "a working Mediterranean hillside farm under construction, photographed as a real-light documentary; no render, no CGI".

**İnsan kararı:** insansız saha DEĞİL. Montajcılar ve taşçılar bulanık hareket çizgisi olarak yazılır (streak cümlesi); B rejiminde silinir, A rejiminde küçük ve bulanık kalır. ⛔ "No workers" veya "no people" YAZILMAZ [DERS 33].

**Vinç / kaldırma kararı [DERS 8 · 22 · 46 · 57]:** ⛔ KULE VİNCİ YOK. Cam panel **vakumlu kaldırıcı (vacuum lifter)** ile montaj; kaldırıcı suction cup'ları panel yüzeyinde görünür, panel palete yaslanmış kalkıyor → klip sonunda MONTAJ TAMAMLANMIŞ. Havada asılı panel sahnesi YOK. Palet kaynağı G5'ten itibaren sağ kenar.

**Korpus kararı [DERS 55]:** "greenhouse" modelde çiftlik = dizi anlamına gelir. Her SITE/BACKGROUND ve her I2V: *"this is the only greenhouse on this hillside; every slope beyond carries only wild scrubland and maquis"*. Üretim günlüğünde klip başına yapı sayım satırı (sera = 1 · ev = 1).

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 10,0 sn teslim → SAHNE TAVANI ≥ 10,0,
                 yani en büyük kutu ≥ 11,0 (üret 11,0 → baştan 1,0 kırp [A7-b]; kutu tam 10,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 12 sahnenin hepsi iki zincirli klip (ara kare Gn′, 12 ara kare) — karar sahibe döner.

┌─ KAMERA İSTASYONU (ANA · tek istasyon) ─────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 · tam kare YATAY (36 mm kare eni, │
│               16:9 kırpma → kare boyu 20,25 mm)                               │
│ yükseklik     h = +2,00 m (tepe plateausunda tripod)                          │
│ mesafe        D_eksen = 45,00 m (sera merkezi) · D_kenar = 33,00 m [DERS 38] │
│ bakış açısı   190° (güney-güneybatı · denize bakış) · tilt 0° · roll 0°       │
│ sabitleme     "bolted tripod on the flat stone of the hilltop plateau,         │
│               absolutely zero movement"                                        │
│ ⛔ HESAP (KILAVUZ_REHBERI §2.8 · f=24 · yatay · yüzde ALT kenardan):          │
│    yüzde(y) = 50 + 118,5·(y − 2,00)/45      x(m, eksenden) → %50 + 66,7·x/45 │
│    px/m = 1280/45 = 28,4 px/m                                                 │
│    taban (y=0)           → 50 + 118,5×(−2,00)/45 = 50 − 5,27 = %44,73 ✓      │
│    ev taç (y=4,50)       → 50 + 118,5×2,50/45   = 50 + 6,58  = %56,58 ✓      │
│    sera taç (y=5,50)     → 50 + 118,5×3,50/45   = 50 + 9,22  = %59,22 ✓      │
│    ufuk (tilt 0)         → %50,00 = GÖZ ÇİZGİSİ (geometrik zorunluluk)       │
│    deniz ufuku           → %50,00 · tam 540 px · sabit 13 karede              │
│    sol çapa: zeytin ağacı x=−17,5 m → %50 + 66,7×(−17,5)/45 = %50 − 25,9 = %24,1 → sol %24,1 │
│    sağ çapa: kayalık     x=+18,5 m → %50 + 66,7×18,5/45   = %50 + 27,4 = %77,4 → sağ %77,4 │
│    sera eni 24 m → %50 ±17,8 → %32,2–%67,8 · 808 px                          │
│    ev eni 8 m   → %50 ±5,9  → %44,1–%55,9 · 269 px                           │
│    kanıt nesnesi: zeytin ağacı 180 px boy · %x 8–15                           │
│ ⛔ ÖN GÖRSELLEŞTİRME zorunlu: kamera · sera · ev · teras · zeytin · kayalık · │
│    deniz ufuku yan kesiti çizildi [02_KONSEPT_VE_RISK §3]                     │
│ güneş   38°K · bearing 190° · Temmuz azimut 75°→290° · disk hiçbir karede    │
│          kadrajda değil (kadraj 163°–217°, güneş bu aralığa 09:45–13:15       │
│          arası giriyor → yalnız çok yüksek + doğrudan azmala — model için     │
│          yine de: "no sun disc visible in any frame" [DERS 39])                │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① ZEYTİN AĞACI (SOL · %x 8–15 · %y ≈56 · boy ≈180 px) ⭐ "AYNI YER" nesnesi  │
│    [DERS 25] — gövde tüm 13 karede birebir; zincirde her koşuda ELLE ✓/✗      │
│ ② KAYALIK ÇIKINTI (SAĞ · %x 82–90 · %y 42–52 · ≈200 px) — doğal taş oluşumu │
│ ③ DENİZ UFUKU — %50,00 · tam çerçeve genişliği · değişmez · silky smoothed   │
│ ④ TOPRAK PATİKA — G0'da yabani, G12'de taş döşeli; değişiyor ama tanınıyor   │
│    (değişmez değil ama çapa desteği — her promptta mevcut durumu yazılır)     │
│ ⛔ Koruma iskelesi, beton mikser, el arabası GEÇİCİ → SITE TEXTURE bloğuna   │
│    [DERS 1]. Zeytin ağacı her promptun SITE/BACKGROUND bloğunda BİREBİR.     │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ ufuk %50 (tilt 0, deniz ufuku) · sera taç %59,22 ✓ · taban %44,73 ✓          │
│ kanıt nesnesi (zeytin ağacı) %x 8–15 → alt 100 px (%9,3) üstünde ✓           │
│ kayalık sağ %77,4 → sağ üst 300×100 px alanına girmiyor ✓                    │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ (KILAVUZ_REHBERI §2.8 varsayılanı):            │
│   üst 60 px ve alt 100 px oynatıcı bantları · sağ üst 300×100 px bilgi kartı │
│   son ekran 5–20 s → KART 120–125 s; S11 tutuşu karta girmez                 │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ SERA    çelik çerçeve cam sera · 12 koyu yeşil boyalı çelik kemer · açıklık   │
│         24,0 m · derinlik 10,0 m · taç yüksekliği 5,50 m · 64 cam panel      │
│         (her kemer 16 panel: 8 alt + 8 üst) · cam panel 80 mm çelik glazing  │
│         bar arasında · beton zemin şeridi 24 × 10 × 0,15 m                   │
│ EV      taş çiftlik evi · 8,0 × 6,0 m · 4 taş duvar · taç 4,50 m ·           │
│         terracotta kiremit çatı · sarnıç 3,5 m³ (gömülü, çatı otuğundan)     │
│ TERAS   2 kuru taş teras duvarı · alt h 0,90 m · üst h 0,90 m ·              │
│         pale limestone · lime mortar yok (kuru)                               │
│ YAPI TAMAMLANDI HÂLİ: "When finished this will be a hilltop farm compound    │
│ with one steel-framed greenhouse 24 m long, one stone farmhouse, and two      │
│ dry-stone terraces." — yalnız S0 görselinde bir kez, sonra AT THIS STAGE      │
│ STRUCTURE bloğunun İngilizce tam hâli BOLUM_1 S0'da yazılır ve 13 promptta  │
│ BİREBİR tekrarlanır; değişen yalnız AT THIS STAGE                             │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 12 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az yapı göstermez. İnşa sırası
> yeni tür §10 şablonundan türetildi; uydurulmaz. Kış YOK (Mart–Ekim).
> SÜRE sütunu hepsi 10,0 (düz ızgara beyanı aşağıda).

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | İSTASYON | KANIT NESNESİ (px) |
|:-:|:-:|---|---|---|:-:|:-:|:-:|---|
| 0 | 10,0 | AÇAR | arazi temizliği + sarnıç kazısı %100 | Mart, 2 hafta | B | 09:00 | ANA | zeytin 180 px sol %x8–15 |
| 1 | 10,0 | ÖRER | alt teras duvarı %25 | Mart sonu, 1 hafta | B | 10:00 | ANA | zeytin 180 px |
| 2 | 10,0 | ÖRER | alt teras %100 + üst teras %75 | Nisan, 3 hafta | B | 11:00 | ANA | zeytin 180 px |
| 3 | 10,0 | DÖKER | çiftlik evi temeli %100 + taş duvar %50 | Nisan sonu, 2 hafta | B | 10:30 | ANA | zeytin 180 px |
| 4 | 10,0 | ÖRTER | çiftlik evi çatı %100 + sera zemin %100 | Mayıs, 3 hafta | B | 09:30 | ANA | zeytin 180 px |
| 5 | 10,0 | DİKER | sera çelik çerçeve %50 (6/12 kemer) | Haziran, 2 hafta | B | 10:00 | ANA | zeytin 180 px |
| 6 | 10,0 | DİKER+KAPER | çerçeve %100 + cam panel %12 (8/64) | Temmuz, 1 hafta | B | 11:00 | ANA | zeytin 180 px |
| 7 | 10,0 | KAPER | cam panel %62 (40/64) | Temmuz-Ağus, 3 hafta | B | 10:30 | ANA | zeytin 180 px |
| 8 | 10,0 | TAMAMLAR + SÖKÜM | cam panel %100 (64/64) · iskele kalktı | Eylül, 1 hafta | B | 09:00 | ANA | zeytin 180 px |
| 9 | 10,0 | DONATIR | iç raf %100 + dış tarhlar %100 | Eylül sonu, 2 hafta | B | 10:00 | ANA | zeytin 180 px |
| 10 | 10,0 | EKİN+BAĞLAR | ilk fidanlar + oluk + sarnıç bağlantısı | Ekim başı, 1 hafta | A | 16:00 | ANA | zeytin 180 px |
| 11 | 10,0 | TESLİM | hasat kasası + duman + taş patika | Ekim sonu | A | 17:00 | ANA | zeytin 180 px |

```
IZGARA          120 BPM · ölçü 2,0 sn · 5 ölçü/sahne · kesmeler 10,0 · 20,0 · 30,0 · 40,0 · 50,0 · 60,0 · 70,0 · 80,0 · 90,0 · 100,0 · 110,0
               ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: sahip beyanı — format modülü 12 × 10,0 (yatay_2_dk README)
                   (b) ritim klip İÇİNE nasıl taşınır: her sahnede görünür değişim büyüklüğü öncekinden
                       farklı — teras taş sayısı, kemer sayısı, cam panel sayısı, yeşillik yoğunluğu
                   (c) kabul edilen risk: ⑥ METRONOM hükmü beklenir [DERS 13 · 24 · 44]; karşı kayıt:
                       varyanslı kurgu üç filmde RHYTHM aldı; ritim ölçümü ilk yatay 2 dk koşusundan gelecek
IŞIK GÜNÜ       Σ = 10 × B (2 h) + 2 × A (10 dk) = 20,33 h — TAKVİM (8 ay) ile PENCERE (14 h) AYRI
               Her sahne TEK IŞIK GÜNÜNE sıkıştırılır; gölge yönü tek günlük sırayla tutarlı (03_SAHNE_SIRALAMASI §4)
BÖLÜM SINIRI    G6 — S5 son karesi = S6 ilk karesi; ışık Temmuz sabahı · sera çerçeve %100 · ilk 8 cam panel yerli · iskele tam [DERS 52]
```

### Üç zorunlu satır

```
KANIT   zeytin ağacı (SOL) — G0'da ve G12'de sol %x8–15, boy ≈180 px, gövde birebir [DERS 25]
        her zincir koşusunda araclar/zincir_kontrol.sh ile + üretim günlüğünde ELLE ✓/✗
LOOP    G12 ↔ G0: aynı kadraj · zeytin ağacı sol · kayalık sağ · deniz ufuku %50 · FARKLI SAAT
        bilinçli: G0 sabah (09:00) · G12 akşam (17:00) — "geçen gün" loopunu ima eder [P4-b]
SÖKÜM   koruma iskelesi S8'de ekranda GİDER (borular alt terasta yığılmış kadrajın kenarında);
        usta karede (G12) YOK — yoktan yok olmaz, gidiş görünür [DERS 48]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
  Taş (teras duvarı) → sol kenar taş yığını → G0 (sarnıç kazısından çıkan moloz)
  Çelik kemer → sağ kenarda paketli hâlde → G4 (sera zemini döküldükten sonra teslim)
  Cam panel → sağ kenarda yatay palet → G5 (çerçeve kurulumuna eşzamanlı teslim)
  Sera iç donatı (raf) → sol arka terasta istiflemiş → G8 (sera kapandıktan sonra taşınır)
GİZLİ İŞ → GÖRÜNÜR VEKİL:
  Sarnıç bağlantı borusu yeraltı → çatı oluğu ve downpipe görünür (G10)
  Damlama hattı sera içi → damlama hortumu rulosu tarhta görünür (G10)
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① Sera içi yeşil + hasat kasası (ilk okunan)
② Evin bacasından duman (hayat var)
③ Zeytin ağacı sol + kayalık sağ + deniz ufuku %50 (aynı yer — kanıt nesnesi) [DERS 25]
FİNAL KARE KANITI  ffmpeg -ss 118.5 -i teslim.mp4 -frames:v 1 kanit.jpg
                   (S11 tutuşunun ortasında · aydınlık · duman görünür [DERS 45])
```

---

## 🖼️ KARE TABLOSU — N+1 = 13 görsel [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Her kare bir öncekinin karesinden türetilir (ters inşa §8): G12 usta kare önce, sonra G11 → … → G0.
> Güneş satırı her karede ve her I2V'de [DERS 18]; güneş DİSKİ anılmaz [DERS 39]; gölge açısı G(n) ile
> G(n+1)'de FARKLI [DERS 32 · 47].

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| 0 | 09:00 | 105° | 45° | kuzeybatıya | açık Akdeniz mavisi | Mart · erken yeşil ot · maki sarı çiçek | Boş yabani tepe; sarnıç çukuru açık, maki yığınları sol kenarda |
| 1 | 10:00 | 118° | 51° | batı-kuzeybatı | hafif ince bulut | Mart sonu · ot yeşil uzamış | Sarnıç kapalı; alt teras ilk 3 taş sıra (duvar %25) |
| 2 | 11:00 | 134° | 58° | batı | açık | Nisan · tam yeşil yamaç · deniz berrak | Alt teras tam · üst teras %75; düzlenmiş toprak görünür |
| 3 | 10:30 | 125° | 55° | batı-kuzeybatı | az bulutlu | Nisan sonu · makide beyaz çiçek | İki teras tam; ev temeli + 2 sıra taş duvar |
| 4 | 09:30 | 110° | 48° | kuzeybatı | açık hafif sarı ışık | Mayıs · ot kuru başlıyor | Ev çatısı kiremit · sera beton zemini ıslak/koyu |
| 5 | 10:00 | 118° | 51° | batı-kuzeybatı | açık sert Haziran | Haziran · ot altın sarısı | 6 çelik kemer dik + iskele sağda; cam paleti sağ kenarda |
| **6** | 11:00 | 134° | 58° | batı | açık | Temmuz · ot kuru/sarı · kobalt deniz | ⭐ BÖLÜM SINIRI — 12 kemer tam + ilk 8 cam panel + iskele tam + palet |
| 7 | 10:30 | 125° | 55° | batı-kuzeybatı | açık sert Temmuz | Ağustos · en kuru · parlak kobalt | 40/64 cam panel · iskele tam · palet yarı boş |
| 8 | 09:00 | 105° | 43° | kuzeybatı | ince gri bulut · ıslak cam | Eylül · ilk yağmur · ot yeniden yeşil | 64/64 cam panel · iskele YOK · boş palet sağ köşede |
| 9 | 10:00 | 118° | 50° | batı-kuzeybatı | açık Eylül | Eylül sonu · yamaç yeşil | Sera iç raf + dış tarh çerçeveleri; tarhlar düzlenmiş |
| 10 | 16:00 | 228° | 28° | kuzeydoğuya | altın saat · uzun gölgeler | Ekim · kısa ot · sonbahar havası | İlk fidanlar sera içi · damlama hortumu rulosu · çatı oluğu bağlı |
| 11 | 17:00 | 242° | 20° | kuzeydoğuya | akşam altın · gün batımı yakın | Ekim sonu · sonbahar yeşil + turuncu maki | Teslim: sera yeşil · hasat kasası önde · duman · taş döşeli patika |
| **12** | 17:00 | 242° | 20° | kuzeydoğuya | akşam altın | Ekim sonu | ⭐ USTA KARE — G11 ile aynı ışık; kamera kilitli; tüm sökümleri bitti |

```
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G12 usta kare → G11 (iskele YOK, duman var) → G10 → G9 → G8 → G7 → G6 (bölüm sınırı) →
   G5 → G4 → G3 → G2 → G1 → G0
   sonra I2V S0 (G0→G1) … S11 (G11→G12) — her klip iki uca kilitli
   üretim 11,0 sn, baştan 1,0 kırp → teslim 10,0 sn [A7-b]
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     38°N · kamera bakışı 190° → güneş 09:45–13:15 arasında ≈ kadraj yönüne yakın
                (azimut 163°–217°; bu saatlerde güneş çok yüksek, disk kadrajın tavanında —
                ancak "no sun disc visible" her promptta zorunlu [DERS 39])
MEVSİM YAYI     Mart → Ekim (8 ay) · taşıyıcılar:
                  OT: yeşil (Mar) → altın (Haz) → kuru/sarı (Tem-Ağu) → yeşil (Eyl) → kısa (Eki)
                  DENİZ: açık mavi (Nis) → kobalt (Tem-Ağu) → koyu (Eki)
                  TARAÇA: kuru toprak (S0) → taş duvar (S1-S2) → ıslak beton (S4) → cam (S6-S8) → yeşil (S9-S11)
GÖLGE SÜPÜRMESİ sabah (09:00) kuzeybatıya · öğle (11:00) batıya · akşam (17:00) kuzeydoğuya;
                B rejimi 2 saatlik pencerede ≈ 25–30° süpürme → kadrajda okunur [DERS 32]
KIŞ             YOK — film Mart–Ekim; don riski vardır (DİRENÇ ③) ama kadrajda KAR YOK
GECE            YOK
FİNAL           S11 akşam altın saat · sera içi yeşil görünür · duman · aydınlık [DERS 45] ✅
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   h 2,00 m · D 45,00 m · bakış 190° · tilt 0°
YAPI     H_sera 5,50 m · taç %59,22 · taban %44,73 · sera 12 kemer × 2 m adım · 64 panel
         H_ev 4,50 m · taç %56,58 · ev 8 × 6 m
ÇAPALAR  ① zeytin ağacı SOL %x8–15 ≈180 px · ② kayalık SAĞ %x82–90 ≈200 px ·
         ③ deniz ufuku %50,00 · kanıt nesnesi: zeytin ağacı 180 px
IZGARA   12 × 10,0 · 120 BPM · kesmeler 10,0 · 20,0 · 30,0 · 40,0 · 50,0 · 60,0 · 70,0 · 80,0 · 90,0 · 100,0 · 110,0
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
⬜ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_GLASS_WALL   → GO / FIX / BLOCK: ⬜
⬜ FIX'ler ve beyanları: kutu seti ölçülmedi (beyanlı) · süreler eşit 12×10,0 (beyanlı)
✅ 00_ANALIZ altı dosya — hikâye onayı ✅ 28.09.2026
⬜ ARAÇ KAPISI koşulmadı → THE_GLASS_WALL_URETIM_GUNLUGU.md §0
```

## ⛔ DÜZ IZGARA BEYANI — sahip beyanı ile karşı kayıt [DERS 13 · 24 · 44]

```
Izgara:  12 × 10,0 s — formatın modülü · sahip beyanı.
Karşı kayıt: düz ızgara üç filmde METRONOM (DERS 13 · 24 · 44) · varyanslı kurgu üç filmde
             RHYTHM (THE CROSSING · OVER THE WALL · THE EMPTY RIDGE).
Ritim planı: ritim SÜRE'de değil, klip İÇİ görünür değişim büyüklüğünde:
             S0  zemin sıyrılması — büyük değişim
             S1  3 taş sıra — küçük değişim
             S2  iki teras tamamlandı — orta değişim
             S3  ev temeli ve duvar — orta değişim
             S4  ev çatısı + sera zemini — büyük (iki ayrı şey aynı anda)
             S5  6 kemer — büyük değişim (yeni eleman)
             S6  12 kemer + 8 cam — büyük (iki birim aynı anda)
             S7  40/64 panel — orta
             S8  tam + iskele YOK — büyük (ekleme + çıkarma aynı karede)
             S9  raf + tarhlar — küçük
             S10 fidanlar + oluk — küçük
             S11 hasat + duman + taş patika — büyük (üç ayrı şey aynı anda)
Kabul edilen risk: ⑥ mercek METRONOM verebilir; bu kabul edilir ve ölçülür.
```
