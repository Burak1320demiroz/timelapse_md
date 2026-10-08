# 🚢 THE_EDEN_ARK — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **18 × 8,0 sn = 144,0 sn** | Kapak kartı: **5,0 sn** | Toplam: **149,0 sn**
Prompt yapısı: ⭐ **18 sahne → 19 görsel (G0…G18) + 18 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G9**
Yapı: ⛔ **kart yok — terk edilmiş 130 m'lik genel kargo gemisinin "camın altında bahçe" dönüşümü** (en yakın: BLUE DOOR · BLUE SILO kabuk yenileme emsali) · Saha: **kıyı — adı verilmeyen eski bir Adriyatik tersanesi, kuru havuz** (`SAHA_VE_IKLIM_KARTLARI` kıyı)
Zaman yayı: **gerçekte aylar → tek ışık günü, 144 saniye** · film mertebe anlatır: *"tek bir uzun haziran günü, sabahtan mavi saate"* [P1-c]
Işık günü: **06:00 → 20:00 · Σ rejim penceresi 14,0 saat ≤ 14 (tam sınırda)** — kesmede ışık atlamaz [§2.7 ①]
Kamera mimarisi: **MAIN STATION** — tek istasyon, 18 sahne + usta kare, detay istasyonu YOK [`KAMERA_ISTASYONU` §1]
Izgara: ⛔ **DÜZ — 18 × 8,0** · ⚠️ BANDIN DIŞI (format 12 × 10,0) — sahip izni 05.10.2026, gerekçe §AŞAMA MERDİVENİ
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 05.10.2026 (TUR 1/3 · üç netleştirme SAPMA'da)
Havuz kaydı: `apexait/YAYIN_PLANI.md` — yatay 16:9 hattı (dikey shorts ızgarasına sayılmaz; aile notu §YAYIN_PLANI 05.10.2026)

_"İlk karede kuru havuzda paslı, kapakları kapalı, ölü bir yük gemisi; son karede aynı gemi, lacivert gövdesi ve ışıyan cam kubbesinin altında bir ormanla, mavi saatte römorkörün ardında havuz kapısından denize çıkıyor."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     18 sahne × 8,0 sn                       = 144,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn                           =   5,0 sn   ← SAHNE DEĞİL, ayrı denetlenir
               ⛔ KONUM: teslimin SON 5 saniyesi (144,0–149,0) [A1-b]
──────────────────────────────────────────────────────────────
TOPLAM                                                     149,0 sn
YASAK KELİME    ark · cruise · greenhouse · rainforest · eden · jungle
               ⭐ [DERS 59] hiçbir promptta, negatifte bile — konsept sanatı korpusu (DERS 34 · 42);
                  "crane" yalnız G5–G7 + S4–S7 I2V · "floats/afloat" yalnız S14 I2V'den sonra (kapsamlı, listede değil)
MÜZİK           ✅ VAR — yatay format, sahip kararı 05.10.2026 (THE_EDEN_ARK_MUZIK.md)
BÖLÜM DOSYASI   BOLUM_1 = S0–S8 (0–72,0)  ·  BOLUM_2 = S9–S17 + USTA KARE (72,0–144,0)
QA BİRİMİ       FİLM (tek master × 12 mercek)
```

⛔ Kapak kartı **usta kareden (G18)** türetilir ve üstüne **İngilizce başlık** dizilir: `THE EDEN ARK` (`THE_EDEN_ARK_KAPAK.md`).
⚠️ Son sahnenin (S17) son 2,0 sn'lik TUTUŞU final kanıtıdır (`QA_SPEC` §1): gemi kapıyı geçmiş, durmaya yakın; kart hareketsiz ve yazılıdır — iki ayrı iş.
⭐ Platform küçük resmi de G18'den gelir (sahip kararı 19.09.2026 — öncesi/sonrası bölme yok).

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Terk edilmiş paslı bir yük gemisini kuru havuzda camın altında bir bahçeye dönüştürüp yeniden denize indirmek.
DİRENÇ   ① pas ve çürüme (delik borda · paslı kapak ve direkler)  ② ağırlık (toprak + ağaç; ≤ 1,5 m toprak,
         basamaklı çerçeve)  ③ su (havuz dolmadan yüzmez, seviye eşitlenmeden kapı açılmaz)
         EKRANDA NASIL [P1-b]:  S1 · kıvılcım + dolan hurda konteynerleri  ·  S2 · kesilen ve kaynaklanan levha  ·
                                S6 · tek, yavaş kaldırma  ·  S14 · uzak duvarda yükselen su + kalkan gemi  ·  S15 · kapılar
BEDEL    ⭐ Paslı, karanlık, boş üç ambar — G1'de üç kara açıklık (x 570 · 806 · 988, üstten 690–735, her biri ≈ 150 px);
         G8'de üçü de yeşil taçlarla dolu; G18'de cam altında orman. + paslı gövde: S3'te lacivertin altında kaybolur.
         Okuma bilinçli: "gemi yeniden yapıldı" değil, "ölü bir gemi canlı bir şey taşıyor".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            pas ve boşluk                                                      ✅
  □ kadrajda görünüyor mu?    üç ambar açıklığı (%32–36 · 150 px) · borda bandı (38 px)           ✅
  □ cevap "zaman geçiyor" mu? hayır — "boşluk doluyor ve gemi denize geri dönüyor"                ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: kaç ambar yeşil · sera nereye kadar geldi · havuzda su var mı · gemi nerede
② KİNETİK BAĞIMSIZLIK   ✅ her klipte makine, su ya da gemi hareket eder (kapak · torç · raspa · konveyör · vinç ·
                           yükleyici · yağmurlama · portal · su · kapı · römorkör)
③ BAŞLIK ŞEMASI         ✅ kapak "THE EDEN ARK" (3 kelime) · platform başlığı YAYIN_PAKETI
④ OMURGA CÜMLESİ [P1-k] ✅ kapaklar açılır → hurda gider → delik kapanır → gemi boyanır → ambarlar donanır →
                           toprak dolar → incir iner → ambarlar yeşerir → ilk sulama → ilk kemer → sera yürür →
                           son cam → ışıklar döşenir → iskeleler çekilir → gemi yüzer → kapılar açılır →
                           römorkör çeker → gemi denizde
```

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera  ② kanıt nesnesi: tuğla baca (x 100 · üstten 418 → 671 · 253 px · 19 karede birebir)
                          ③ çapa: yakın havuz kenarı (babalar, üstten 892 → 711)  ④ çapa: mendirek feneri (x 1850) + ufuk %50
                          ⑤ tek gövde, yalnız KAZANIR: pas → lacivert · boş → yeşil · açık → cam · kuru → su
                          ⑥ TEK yüklü kanca: incir (S5 sonu–S6); G0–G4 ve G8–G18'de kadrajda vinç yok
                          ⑦ ayrı insan figürü yok (streak cümlesi · rejim)   ⑧ tek ölçek çapası: gemi 1080 px (G0–G16)
P1.5 · fırsat buldukça   gölge süpürmesi (B) · gök sabahtan mavi saate · boya ve ıslaklık katmanı
SPEC · yalnız belge      azimut/yükseklik dereceleri (kapı şartı) · px tabloları
```

**Malzeme kimliği (her promptta):** *paslı çelik → parlak lacivert boya · beyaz çelik kemer ve cam · koyu toprak ve yeşil taç* — korpus: "documentary shipyard photograph on colour negative film" [DERS 34 · 42].
**İnsan kararı:** tersane işçileri var, rejime göre — A'da hızlı ama tanınır makine, B'de iz; "Crew register only as faint soft motion streaks" her görselde. Kalabalık YOK.
**Vinç / kaldırma kararı [DERS 8 · 22 · 46 · 57]:** kamyonlu mobil vinç S4'te gelir, S7'de gider. TEK kaldırma: G5 "with a strapped root ball on the hook" (ağaç treylerde) → S5 son 1,5 sn kaldırır ve ambar 2'nin üstüne taşır → **G6: ağaç kök topu mezarnanın 0,5 m üstünde ASILI** (kaldırma yolu karede biter) → S6 yalnız indirir ve oturtur → G7 "with a slack guiding sling on the hook". Kanca +22,5 m → üstten 555 = ufkun (540) 15 px ALTI. Bom başı +32 → üstten 455, göğe karşı (⚠️ beyanlı). Kemerler havada TAŞINMAZ — portal yerinde diker.
**Korpus kararı [DERS 55]:** tersane korpusu çok gemilidir → SITE'ta 19 kez: "The shipyard holds exactly one ship, in this dock; no other hull, mast or superstructure stands anywhere, and the basin is open water crossed only by small harbour craft." ("harbour craft" yalnız römorkör için açık kapı.)
**Kelime kilitleri:** "ark", "cruise", "greenhouse", "rainforest", "Eden" HİÇBİR promptta yok · "crane" yalnız G5–G7 görselleri ve S4–S7 I2V'leri · "floats/afloat" yalnız S14 I2V'si ve sonrası · "tug" yalnız G15 ve sonrası [DERS 33 · 56].

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0,
                 yani en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp [A7-b]; kutu tam 8,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 18 sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.

┌─ KAMERA İSTASYONU (ANA · tek istasyon) ─────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 (G16–G18 ISO 400) · tam kare YATAY │
│ yükseklik     h = +24,00 m (liman suyundan) — kuru havuzun yanındaki eski       │
│               tersane ofisinin düz çatısı, parapete cıvatalı tripod            │
│ mesafe        gemi ortasına optik eksende d 135,0 m · baş bodoslama d 91,5 m · │
│               kıç d 178,5 m · havuz ekseni bakışa 48° [DERS 38]                │
│ bakış açısı   bearing 10° · tilt 0° · roll 0°                                  │
│ ⛔ HESAP (yüzde ALT kenardan):  yüzde(y) = 50 + 118,5·(y − h)/d                 │
│                                x(%) = 50 + 66,7·l/d  ·  px/m ≈ 1280/d          │
│    ⭐ tilt 0 ve h güverte ÜSTÜNDE → bütün gemi ufkun ALTINDA (%26–49). Taç %82  │
│      kuralı bağlayıcı değil; bağlayıcı "çalışma seviyesi ≥ %25" → d_baş ≥ 87 m │
│    yakın borda güverte (baş)  +5,5  → %26,7 · x 437                            │
│    ufuk (tilt 0)               → %50,0 = üstten 540                            │
│    baca (gemi) +21,5           → %48,2 · x 1182                                │
│    kanıt: tuğla baca           → üstten 418 → 671 · x 100 · 253 px boy         │
│ ⛔ ÖN GÖRSELLEŞTİRME: plan ve kesit betikle hesaplandı (00_ANALIZ/02 §3)        │
│    bom başı +32 → üstten 455 = GÖĞE karşı · kanca +22,5 → 555 = KARAYA karşı   │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① TUĞLA BACA (SOL · x ≈ 100 · üstten 418 → 671 · 253 px) — ⭐ KANIT NESNESİ    │
│ ② YAKIN HAVUZ KENARI — granit kenar ve demir babalar, sol alttan (x 215 ·     │
│    üstten 892) kapılara doğru yükselir (x 1332 · 711)                         │
│ ③ MENDİREK FENERİ (SAĞ · x ≈ 1850 · üstten 577 → 620) + mendirek çizgisi 624 ·│
│    deniz ufku %50 (540)                                                       │
│ + uzak rıhtımda alçak oluklu sac ambarlar (mahya ≈ 623) — her SITE'ta birebir │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ ufuk %50 (tilt 0) · gemi %26–49 · gök üst yarı (kapakta başlık yeri)          │
│ güvenli alan 16:9 ⛔ ÖLÇÜLMEDİ (§2.8 varsayılanı) — kanıt nesnesi alt 100 px'e │
│ (üstten > 980) ve sağ üst 300×100 px'e (x > 1620 · üstten < 100) girmez ✓     │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ gemi: genel kargo · LOA 130 m · en 20 m · derinlik 11 m · üç ambar (22 × 14 m)│
│ keel −5,5 (takozlar 1,5 m · havuz tabanı −7,0) · güverte +5,5 · baş kasara   │
│ +8,0 · köprüüstü (dört kat) +17,5 · baca +21,5 · havuz kenarı +1,5 · liman 0  │
│ cam kubbe: 20 beyaz çelik kemer · 4 m ara · 18 m en · güverteden 13 m (+18,5) │
│ büyük incir: 13 m · üst basamakta (+3,0) · tepe +16,0 · 3 gergi teli         │
│ yüzme: su −1,0'e varınca gemi takozlardan kalkar · 0'da 1,0 m yukarıda        │
│ STRUCTURE'ın İngilizce tam hâli BOLUM_1 S0'da; 19 promptta BİREBİR            │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 18 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | İSTASYON | KANIT NESNESİ (px) |
|:-:|:-:|---|---|---|:-:|:-:|:-:|---|
| 0 | 8,0 | AÇAR | kapaklar kapalı → üç ambar açık | 10 dk | A | 06:00→06:10 | ANA | açık ambar 0 → 3 (x 570 · 806 · 988) |
| 1 | 8,0 | SÖKER | kapak + 2 direk → hurda | 2 h | B | 06:10→08:10 | ANA | direk 2 → 0 · konteyner 0 → 4 |
| 2 | 8,0 | YAMAR | delik levha → yeni levha | 10 dk | A | 08:10→08:20 | ANA | yama x 908 · üstten 751 · 47 px |
| 3 | 8,0 | SOYAR · BOYAR | pas → lacivert · gri · beyaz | 2 h | B | 08:20→10:20 | ANA | renk sınırı x 172 → 1249 |
| 4 | 8,0 | DONATIR | basamaklı çerçeve %100 · vinç kurulur | 10 dk | A | 10:20→10:30 | ANA | çerçeve demeti 6 → 0 · vinç ayakları |
| 5 | 8,0 | DOLDURUR | toprak %100 · incir treylerden askıya | 2 h | B | 10:30→12:30 | ANA | toprak yığını x 461 → 0 · incir asılı |
| 6 | 8,0 | İNDİRİR | incir askıdan toprağa | 10 dk | A | 12:30→12:40 | ANA | incir tepesi üstten 620 · x 806 |
| 7 | 8,0 | YEŞERTİR | yeşil ambar 1 → 3 · fidanlık 5 → 0 | 2 h | B | 12:40→14:40 | ANA | fidanlık sırası 5 → 0 (x 972) |
| 8 | 8,0 | SULAR | ilk sulama | 10 dk | A | 14:40→14:50 | ANA | ⭐ G9 üç yeşil taç (560 px) |
| 9 | 8,0 | KURAR | portal · kemer 0 → 1 | 10 dk | A | 14:50→15:00 | ANA | kemer 1 (x ≈ 1067) |
| 10 | 8,0 | ÖRTER | kemer 1 → 18 · cam %90 | 2 h | B | 15:00→17:00 | ANA | ⭐ seranın baş kenarı x 1067 → 470 |
| 11 | 8,0 | KAPATIR | kemer 20 · cam %100 | 10 dk | A | 17:00→17:10 | ANA | son panel x 416 |
| 12 | 8,0 | DÖŞER | teras korkuluğu · ışık hatları | 10 dk | A | 17:10→17:20 | ANA | baş kasara korkuluğu |
| 13 | 8,0 | ARINDIRIR | iskele 6 → 0 · rampa çekilir | 10 dk | A | 17:20→17:30 | ANA | iskele kulesi 6 → 0 |
| 14 | 8,0 | YÜZER | havuz −7,0 → 0 · gemi +1,0 m | 2 h | B | 17:30→19:30 | ANA | ⭐ uzak duvarda su · borda bandı 38 → 48 px |
| 15 | 8,0 | AÇILIR | kapılar açık · römorkör bağlı | 10 dk | A | 19:30→19:40 | ANA | iki kapı kanadı |
| 16 | 8,0 | ÇEKER | gemi 0 → +60 m · ışıklar yanar | 10 dk | A | 19:40→19:50 | ANA | baş x 172 → 846 |
| 17 | 8,0 | SÜZÜLÜR | gemi +60 → +150 m | 10 dk | A | 19:50→20:00 | ANA | ⭐ baş x 846 → 1328 |

```
IZGARA          120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · kesmeler 8,0 · 16,0 · … · 136,0  (17 kesme, her 8,0 sn)
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: sahibin kendi önerisi (18 × 8,0 = 2:24) ve sahibin 8,0 sn üretim düzeni; yatay
                       hatta THE OLD ROAD (15 × 8,0) emsali. ⚠️ BANDIN DIŞI: format 12 × 10,0 — sahip izni 05.10.2026.
                   (b) ritim klip İÇİNE: ① rejim nabzı — B'ler S1 · S3 · S5 · S7 · S10 · S14'te (uzun iş, çizgi
                       süpürür), A'lar arada (tek olay); ② son dört sahne A, final yavaşlar; ③ müzikte katman = aşama
                       (MUZIK.md); ④ iş yönü değişir: yana (S0 kapaklar) · aşağı (S1–S2) · soldan sağa (S3 boya) ·
                       yukarı (S5–S8 yeşil) · sağdan sola (S10 cam) · yukarı (S14 su) · uzaklaşan (S16–S17 gemi).
                   (c) kabul edilen risk: ⑥ METRONOM hükmü beklenir [DERS 13 · 24]; karşı kayıt: varyanslı
                       kurgu üç filmde RHYTHM aldı [DERS 44]
IŞIK GÜNÜ       Σ pencere = 12 A × 10 dk + 6 B × 2 h = 14,0 saat ≤ 14 ✓ (tam sınır · gece yok)
BÖLÜM SINIRI    G9 — sahne S8 son karesi = sahne S9 ilk karesi; ıslak yeşil ambarlar, gölge +62°, gök aynı [DERS 52]
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: tuğla baca — G0'da ve usta karede (G18) aynı konum (x ≈ 100 · üstten 418 → 671) ve
        aynı boy (253 px) [DERS 25]
LOOP    G18 ↔ G0: aynı kadraj · aynı çapalar · ışık FARKLI (bilinçli — G0 06:00 sabah, G18 20:00 mavi saat; tek gün):
        paslı ölü gemi havuzun içinde / ışıklı yaşayan gemi havuzun dışında
SÖKÜM   S7 vinç, treyler, konveyör · S13 iskele kuleleri ve rampa · S16 mooring halatları — ekranda gider;
        portal KALIR (kalıcı cam temizleme portalı) [DERS 48]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
hurda (kapak + direk)  → yakın rıhtımda 4 konteyner (rampanın dibi)              → G1 (kapaklar), G2 (dolu)
yeni levha              → telehandler çatalı                                      → G2
boya                    → raspa düzeneği + hortumlar (rıhtım)                     → G3
basamaklı çerçeve        → rıhtımda çerçeve demetleri                             → G4
toprak                  → yakın rıhtımda branda altında uzun yığın (x 461)       → G0
incir                   → yassı treyler (vinç yanında)                            → G5
genç ağaç, palmiye, eğrelti → yakın rıhtımda gölge filesi altında 5 sıra fidanlık (x 972) → G0
kemer, portal, cam       → kıç ucunda rıhtım istifi                               → G8
su                      → liman — kapıların savak ağızları                        → G14
römorkör                → havza (sağdan)                                          → G15 (S15'te gelir)
GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL: ambarların içi (çerçeve, drenaj, toprak katmanı) → mezarnadan taşan taçlar ·
   kaynak dikişi → kıvılcım · geminin takozlardan kalkışı → borda bandının 38 → 48 px'e çıkışı · gemi içi elektrik → ışıklar
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① ışıyan cam kubbe ve içindeki yeşil (ilk okunan) → ② kapı dışındaki gemi ve römorkör → ③ boş, su dolu havuz ve
   aynı tuğla baca (kanıt nesnesi)
FİNAL KARE KANITI  ffmpeg -ss 143.0 -i teslim.mp4 -frames:v 1 kanit.jpg   (S17 tutuşu 142,0–144,0 içinde · mavi saat,
                   okunur [DERS 45])
```

---

## 🖼️ KARE TABLOSU — N+1 = 19 görsel [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Gölge yönü kadrajda: 0 = kameradan uzağa · − sola · + sağa (|x| > 90 = kameraya doğru). Güneş DİSKİ anılmaz.

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| 0 | 06:00 | 73° | 16,4° | −117° | soluk, küçük yüksek bulut | sabah | paslı gemi · kapaklar kapalı · delik borda |
| 1 | 06:10 | 75° | 18,1° | −115° | aynı | sabah | üç ambar açık |
| 2 | 08:10 | 95° | 39,0° | −95° | açık mavi | — | direk ve kapak yok · 4 konteyner |
| 3 | 08:20 | 97° | 40,8° | −93° | açık mavi | — | yama (astar) · raspa düzeneği |
| 4 | 10:20 | 129° | 60,2° | −61° | koyu mavi, küme | — | lacivert · gri · beyaz · çerçeve demetleri |
| 5 | 10:30 | 133° | 61,5° | −57° | aynı | — | çerçeve içeride · vinç kurulu · incir treylerde |
| 6 | 12:30 | 198° | 67,3° | +8° | öğle | — | ⭐ incir ambar 2'nin 0,5 m üstünde ASILI |
| 7 | 12:40 | 204° | 66,7° | +14° | öğle | — | incir dikili · kılavuz sapanı kancada |
| 8 | 14:40 | 250° | 51,0° | +60° | ikindi küme | — | üç ambar yeşil · vinç yok · kemer istifi |
| 9 | 14:50 | 252° | 49,3° | +62° | aynı | — | ⭐ bölüm sınırı — ıslak yeşil · portal parçaları |
| 10 | 15:00 | 254° | 47,7° | +64° | aynı | — | portal + kemer 1 |
| 11 | 17:00 | 277° | 26,7° | +87° | altına dönen | — | 18 kemer camlı · baş ucu açık |
| 12 | 17:10 | 279° | 25,0° | +89° | altın | — | sera tamam · portal başta park |
| 13 | 17:20 | 280° | 23,3° | +90° | altın | — | teras korkuluğu · ışık hatları (sönük) |
| 14 | 17:30 | 282° | 21,5° | +92° | altın | — | iskele ve rampa yok · havuz kuru |
| 15 | 19:30 | 302° | 2,1° | +112° | turuncu (sol) | — | havuz dolu · gemi yüzüyor · kapı kapalı |
| 16 | 19:40 | 304° | 0,6° | — | turuncu → mavi | — | kapılar açık · römorkör halatlı |
| 17 | 19:50 | 305° | −0,9° | — | alacakaranlık | — | gemi +60 m · ışıklar YANIK |
| 18 | 20:00 | 307° | −2,3° | — | ⭐ mavi saat | — | ⭐ USTA KARE — gemi kapı dışında (+150 m) |

```
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G18 usta kare → G17 (gemi 90 m geri, ışık aynı) → G16 (ışıklar SÖNÜK, gemi havuzda) → … → G9 (bölüm sınırı) → … → G0
   sonra I2V S0 (G0→G1) … S17 (G17→G18) — her klip iki uca kilitli, üretim 9,0 sn, baştan 1,0 kırp
⭐ PİLOT ÜÇLÜ (üretim başlamadan): ① G18 + G17 + S17 (yüzen gemi, römorkör, ışık) ② G5 + G6 + S5 ve S6 (TEK kaldırma) ·
   ③ G10 + G11 + S10 (yürüyen portal ve cam). ⛔ Üçü geçmeden kalan klipler üretilmez.
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     45,3° K · 21 haziran (δ +23,4°) · doğuş 04:10 · batış 19:50 (güneş saati) · kamera bakışı 10°
                → kadraj −27° … +47° · güneş 73° → 307°: sabah sağ-önde (+63°), akşam sol-önde (−63°) — HİÇBİR karede
                kadrajda değil
MEVSİM YAYI     yok — tek gün · taşıyıcı: GÜN IŞIĞI (soluk sabah → beyaz öğle → altın ikindi → turuncu batış → mavi saat)
GÖLGE SÜPÜRMESİ rejim B klipte 20°–65° (S1 20° · S3 32° · S5 65° · S7 46° · S10 23° · S14 20°) · rejim A klipte fark edilmez
KIŞ             YOK (tek ışık günü — gerekçe 03 §1)
GECE            yok · final mavi saat, güneş −2,3° [DERS 45]
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   h +24,00 · d_orta 135,0 · d_baş 91,5 · bakış 10° · tilt 0 · havuz ekseni bakışa 48°
GEMİ     130 m · güverte %26,7 (baş) → %36,9 (kıç) · baca %48,2 · x 172 → 1249 (G0–G16) · G18 x 1328 → 1657
ÇAPALAR  ① tuğla baca x 100 · üstten 418 → 671 · ② yakın havuz kenarı 892 → 711 · ③ fener x 1850 · 577 → 620 · ufuk 540
IZGARA   18 × 8,0 · 120 BPM · kesmeler 8,0 · 16,0 · … · 136,0  (17 kesme, her 8,0 sn)
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_EDEN_ARK   → FIX 5 · BLOCK 0
   (05.10.2026 §10f sonrası — DERS 58-63 kapısıyla yeniden koşuldu)
✅ FIX'ler ve beyanları: kutu seti ölçülmedi (beyanlı) · süreler eşit (beyanlı — sahip ızgarası)
   · DERS 61 "YENİ eleman" ×3, elle okundu, üçü de YANLIŞ ALARM: S5/S7 'bridge' = geminin köprüüstü
     (G0'dan beri var) · S16 'arch · terrace' = G11/G12'de kurulmuş kemer ve teras (S16'da yalnız lamba yanar)
✅ DERS 59 düzeltmesi: metin yasağı artık yalnız 'on any surface, the hull and the funnel included'
   (eski listedeki truck · container · vest · helmet … sahada YOKTU) · S4 'disappear' → telehandler taşır
✅ YASAK KELİME satırı TESLİM YAPISI'nda (ark · cruise · greenhouse · rainforest · eden · jungle)
✅ 00_ANALIZ altı dosya · hikâye onayı 05.10.2026
⛔ ARAÇ KAPISI koşulmadı → THE_EDEN_ARK_URETIM_GUNLUGU.md §0
```
