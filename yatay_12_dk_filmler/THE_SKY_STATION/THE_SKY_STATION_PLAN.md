# 🚡 THE_SKY_STATION — Yatay 12 Dakika Timelapse Planı (sahne sahne)

> **Bu dosyada PROMPT YOKTUR.** 181 prompt sahip kararıyla (13.10.2026) **perde perde klasörlerdedir**:
> `PERDE_01_CATI_KALKAR/THE_SKY_STATION_PERDE_01.md` … `PERDE_10_ILK_YOLCULAR/THE_SKY_STATION_PERDE_10.md`
> (9 sahne · 72 sn her biri; her sahnenin başında Türkçe **"önceki sahneye göre değişen"** notu). Plan ile prompt
> ayrı durur (kapı betiği promptu başlıktan sayar). Sahibin kaynak metnindeki ilk üç sahnenin İngilizce hareket
> promptları ALINMADI — PERDE_01'de deponun PROMPT_SABLONU iskeletiyle yeniden yazıldı. Tek kaynak:
> `00_ANALIZ/05_SAHNE_CALISMALARI/sky_gen.py` + `sky_data.py` (ortak bloklar harfi harfine aynı [DERS 20]).

```
DURUM         📝 PROMPTLAR YAZILDI · 13.10.2026 · 10 perde klasörü · 91 görsel + 90 I2V · üretim AÇILMADI
HİKÂYE ONAYI  ◐ sahip prompt yazımını istedi (13.10.2026: "perde perde klasörlere ayırarak hazırlayalım promtları",
              "tüm film bitmeden durma") — §🧭 SAPMALAR ①–⑩ plandaki VARSAYILANLARLA uygulandı. Sapma değişirse
              üretici yeniden koşulur. ⛔ Üretim (görsel/video) sahibin SAPMA onayından ve ARAÇ KUTU SETİ ölçümünden önce açılmaz.
```

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **90 × 8,0 sn = 720,0 sn** | Kapak kartı: **⛔ YOK** | Toplam: **720,0 sn (12:00)**
Prompt yapısı: ⭐ **90 sahne → 91 görsel (G0…G90; G90 = USTA KARE) + 90 I2V = 181 prompt · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı kareleri **G30 · G60**
Yapı: **harap bir dağ teleferik hattı — iki taş istasyon (yakın: büyük çatılı taş salon + vadiye taşan biniş tabanı · karşı: daha küçük taş istasyon + kaya burnunda seyir terası) ve aralarındaki ≈108 m'lik açıklık; tek kırmızı kabin** · yeniden yapım: çatı söküm → taş cephe → merdiven → biniş tabanları → makara tekerleği + tahrik → hat başlıkları → yeni çatılar → cam cepheler → ahşap peronlar → halatlar → kabin restorasyonu → deneme → bahçe, su, ışık → ilk yolcular
Saha: **iki yamaç arasında derin, dar bir dağ vadisi · kireçtaşı · 45° K · yaz sonu** — gerçek bir yer, hat ya da işletme ADI YOK (kurgusal)
Zaman yayı: **gerçekte ≈1 inşaat sezonu (ilkbahar → yaz sonu) → 12 dakika** · film mertebe anlatır: *"bir sabah çatı kalkar, bir sezon taş, çelik ve halat, bir akşam ilk yolcular"* · ÜSLUP BEYANI: takvim tek bir yaz gününün ışığına sıkıştırıldı — "tek günde yapıldı" iddiası DEĞİLDİR
Işık günü: **06:10 → 19:40 (mavi saat başı) · Σ rejim penceresi 13 sa 30 dk ≤ 14** · 81 klip A (10 dk) + **9 klip G** (gerçek zaman, 0 dk) — kesmede ışık atlamaz [§2.7 ①]
Kamera mimarisi: **MAIN STATION — tek istasyon, 90 klip + usta kare, %100** (sahip metni: "Bütün sahneler aynı ana kameradan ilerliyor")
Izgara: ⛔ **DÜZ — 90 × 8,0** (sahip senaryosu) · §DÜZ IZGARA BEYANI
Bölüm (QA/montaj birimi): **BOLUM_1 = S0–S29 (0:00–4:00) · BOLUM_2 = S30–S59 (4:00–8:00) · BOLUM_3 = S60–S89 + USTA KARE (8:00–12:00)** · prompt dosyası: **PERDE_01 … PERDE_10** (sahip kararı)

_"İlk karede harap bir taş istasyonun dev çatı paneli vinçte havalanıyor, altında sarmaşıklı salonda paslı kırmızı bir kabin; son karede, mavi akşamda, aynı kabin yeniden kırmızı, vadinin üstündeki gergin halatlarda karşı yamaçtan dönüşe çıkmış — iki istasyon yanık, seyir alanında ilk yolcular."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     90 sahne × 8,0 sn                       = 720,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     ⛔ YOK — sahip metni: film "hareket hâlinde, tam 12:00'da bitiyor" · ihrac_kontrol.sh --kart YOK
──────────────────────────────────────────────────────────────
TOPLAM                                                     720,0 sn
HIZ             1x (yatay hat 2x'e çevrilmez [DERS 58])
MÜZİK           ✅ VAR — yatay hat (sahip 05.10.2026) · 120 BPM (8,0 sn = 4 ölçü) · müziksiz pencere 0,0–8,0 (S0) ·
               katman = perde · iki sessizlik cebi: S65 (ilk geçiş, vadinin ortası) ve S86 (final geçiş, vadinin
               ortası) — orada yalnız rüzgâr ve halat · ayrıntı _MUZIK.md'de (onaydan sonra)
SES             diegetik yatak her sahnede (tablolarda SES sütunu) · konuşma YOK · telsiz/sohbet yalnız anlaşılmaz uğultu
YAZI            ⛔ YOK — hiçbir yüzeyde okunur yazı, tabela, numara
YASAK KELİME    train · railway · rail · track · tram · funicular · chairlift · ski · snow · gondola · station platform · bridge · helicopter · drone · zipline · fall · falling · snap · crash · collapse · fog · mist · haze · smoke · glow · bloom · rays · beam · flare · fireworks · neon · mirror · signboard
               (13.10.2026 kesin · "logo" listeden çıktı: I2V'nin sabit kapanışı "No logos." der · "track rope" yerine
                "carrying rope" · "tyre tracks" yerine "tyre marks/ruts" · "beam" yerine "girder")
               ⭐ "train · rail · track · tram · funicular" kabini raylı taşıta çevirir · "gondola" kanal kayığı ve çoklu
                  kabinli hat çağırır · "chairlift · ski · snow" kayak merkezi çağırır · "bridge" vadiye köprü kurar ·
                  "fog · mist" vadiyi sisle doldurur (halatlar kaybolur) · ışık etki adları pozitif tarifle [ISIK_FINALI §5]
KELİME KİLİDİ   (uygulandı — üretici denetler) kabin = "one small red aerial cableway cabin" · halat = "steel haul rope / track rope" ·
               "rust" yalnız G0–G55 kabinde · "red paint" G58'den · "crane" G0–G62 + S0–S62 I2V · "rope" G46'dan ·
               "lamps lit" S79 I2V'den · "visitors" S81 I2V'den · STRUCTURE'da renk, ışık, insan yok [DERS 36]
PROMPT DOSYASI  PERDE_01 … PERDE_10 — her biri 9 sahne (72,0 sn) · perde sınırı da bir KAREDİR (G9 · G18 · … · G81)
QA BÖLÜMÜ       BOLUM_1 = S0–S29 (0–240,0) · BOLUM_2 = S30–S59 (240,0–480,0) · BOLUM_3 = S60–S89 + USTA KARE (480,0–720,0)
QA BİRİMİ       BÖLÜM — üç bölüm masterı (her biri 240 s) × 5 mercek = 15 ham rapor (yatay_12_dk_filmler/README)
```

⛔ Kart olmadığı için platform son ekranı **önerilmez**; kullanılacaksa yalnız gök bandına (üstten 0–200 px, karşı sırtın üstü), son ≤ 5 sn — kabinin, halatların ve iki istasyonun üstüne konmaz.
⭐ Platform küçük resmi (kapak) **G90'dan** gelir — öncesi/sonrası bölme YOK (sahip kararı 19.09.2026).

### ⭐ İZLEYİCİ KAPISI [C2 · KILAVUZ_REHBERI §6 · UZUN_FORM §1]

```
İŞLEV ANI         S83 ilk yolcular biner → S84–S87 kabin gerçek hızda vadiyi geçer → S88 inerler → S89 korkuluğa varırlar,
                  BOŞ KABİN DÖNÜŞE BAŞLAR. Final klibi 0–4 sn olay, 4–8 sn "hareketli tutuş" (sahip: film hareket hâlinde biter)
AÇILIŞ NESNESİ    G0: vinçte havalanan dev çatı paneli + altındaki harap taş istasyon; kemerin ardında paslı kırmızı kabin
AÇILIŞ DÜZENİ     ① NESNE çatı paneli/istasyon (0 sn) · ② DOKUNUŞ "from the first frame the panel is already rising" ·
                  ③ İPUCU karşı yamaçta harap ikinci istasyon — aradaki boşluk (≤ 16 sn, S2) ·
                  ④ İLK BÜYÜK SONUÇ kabin çatıdan çıkıp bakım alanına iner (0:08–0:16, S1)
                  AÇILIŞ GERİ ÇEKİLMESİ ⛔ YOK (sabit geniş)
AÇILIŞ–FİNAL      G0 ↔ G90 aynı kadraj: paslı kabin salonun İÇİNDE, istasyonlar çatısız/çökük ↔ kırmızı kabin vadinin
KAFİYESİ          ÜSTÜNDE, istasyonlar yanık. Işık bilinçli farklı: sabah 06:10 ↔ mavi saat 19:40
MERAK SORUSU      Bu harap istasyona ve paslı kabine ne olacak?
```

### 🔗 MERAK ZİNCİRİ [UZUN_FORM §3 · 12 dk: 6–7 soru]

| # | soru (izleyicinin kafasında) | açılır | cevaplanır | ekranda |
|:-:|---|:-:|:-:|---|
| 1 | Bu harap istasyon kurtarılabilir mi? | S0 | S33–S35 | iki istasyon da eski siluetinde çatılı |
| 2 | Paslı kırmızı kabine ne olacak? | S1 | S54–S61 | aynı kabin kumlanır, kırmızıya boyanır, halata asılır |
| 3 | Karşıdaki istasyona nasıl ulaşılacak? | S2 · S7 · S23 · S44 | S45–S51 | pilot halat → çekme halatı → taşıyıcı halatlar gerilir |
| 4 | Açık çatıdan inen dev tekerlek ne işe yarayacak? | S18 | S51 · S63 | gerdirme · tekerlek ilk kez döner |
| 5 | Kabin gerçekten karşıya gidip yük taşıyabilecek mi? | S63 | S64–S71 | boş ilk geçiş (gerçek hız) · yüklü fren denemesi |
| 6 | Biri binecek mi — karşıya varacaklar mı? | S81 | S84–S89 | ilk yolcular gerçek hızda geçer, seyir alanına çıkar |

```
KURAL   ✅ her soru cevaplanmadan bir sonraki açık (③ S2'den S51'e kadar zinciri taşır)
        ✅ en son cevaplanan soru (⑥) ilk büyük sonuçtan (S1) zayıf değil — insan + gerçek hız + boşluk
        ✅ ilk büyük sonuç 0:16 (12 dk hedefi ≤ 1:00) · doruk S64–S70 = %71–79 (hedef %75–88 · alt sınırda)
```

### ⚓ YENİDEN KANCA — perde başları (≈ 72 sn) + ara kancalar

Her perde yeni bir İŞ TÜRÜ ya da YENİ BÜYÜK ELEMANLA açılır (tablolarda ⚓). En uzun kancasız dizi 4 klip — UZUN_FORM §4 eşiği tutar.
Direnç anları: S14 (biniş tabanı boşlukta) · **S48 (yaz sağanağı, iş durur)** · S69 (yüklü kabin vadinin ortasında fren).

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Terk edilmiş bir dağ teleferiğinin iki istasyonunu ve tek kabinini yeniden ayağa kaldırıp, vadinin üstünden
         ilk yolcuları karşı yamaca taşımak.
DİRENÇ   ① boşluk (108 m'lik açıklık, dibi görünmeyen vadi — S14 · S45–S51)  ② ağırlık (dev tekerlek, gerdirme
         ağırlığı, yüklü kabin — S18 · S24 · S69)  ③ çürüme (sarmaşık, pas, kırık cam — S0–S8 · S54–S55)
         ④ hava (yaz sağanağı iş durdurur — S48)
BEDEL    ⭐ Paslı kabin — G0'da salonun İÇİNDE, eski askı kirişinde asılı; S1'de dışarı çıkar ve 53 sahne boyunca
         bakım alanında BEKLER (izleyicinin önünde, cevapsız); S54–S58'de pas gider, aynı oranlarla kırmızıya döner;
         G90'da vadinin üstünde. Okuma: "kabin değiştirildi" değil, "AYNI kabin geri döndü".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            pas, sarmaşık, çökmüş çatılar — ve iki istasyon arasındaki BOŞLUK          ✅
  □ kadrajda görünüyor mu?    kabin her ana karede (salonda · beşikte · halatta) · boşluk her karede      ✅
  □ cevap "zaman geçiyor" mu? hayır — "aynı kabin, aynı hatta, ilk yolcularla"                          ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: çatı var mı · kaç halat · kabin nerede (salon/beşik/halat) · hangi renk · ışık var mı
② KİNETİK BAĞIMSIZLIK   ✅ her klipte vinç, ekip, makara, su ya da kabin hareket eder
③ BAŞLIK ŞEMASI         ✅ kapak "THE SKY STATION" (3 kelime) — YAYIN_PAKETI onaydan sonra
④ OMURGA CÜMLESİ        ✅ çatı kalkar → kabin çıkar → sarmaşık gider → iki kabuk → cephe yıkanır → taş onarılır → merdiven →
                           biniş tabanları → tekerlek → tahrik → hat başlıkları → gerdirme ağırlığı → çatı makasları →
                           ahşap → çinko → camlar → peronlar → seyir terası → pilot halat → sağanak → taşıyıcı halatlar →
                           gerdirme → kabin kumlanır → kırmızı → halata asılır → vinç gider → ilk geçiş → yüklü fren →
                           şantiye gider → bahçe → su → ışıklar → yolcular → geçiş → varış → boş kabin döner
```

---

## 🔒 DEĞİŞMEZLER — kamera, çapalar, yapı [`KILAVUZ_REHBERI` §3]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 ile [DERS 23 · 31]. 8,0 sn teslim → en büyük kutu ≥ 9,0
                 (üret 9,0 → baştan 1,0 kırp). Bu plan yazılabilir, üretim açılamaz.

┌─ KAMERA İSTASYONU (ANA · tek) ───────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 (S79+ ISO 400) · tam kare YATAY   │
│ yükseklik     h = +6,0 m (yakın istasyon zemininden) — yakın yamaçta, salonun   │
│               güneyindeki kaya rafında beton kaideye cıvatalı tripod            │
│ mesafe        D = 40 m (yakın salon cephesi) · 140 m (karşı istasyon)          │
│ bakış         bearing 10° (kuzey-kuzeydoğu) · tilt 0° · roll 0° · ufuk %50     │
│ ⛔ HESAP (yüzde ALT kenardan · px ÜSTTEN):                                       │
│    yüzde(y) = 50 + 118,5·(y − h)/D        x(m) → %50 + 66,7·x/D (soldan)        │
│    yakın salon   x −20…+4 m · D 40 → x 320–1088 px                              │
│                  zemin y 0 → üstten 732 · saçak +9 → 444 · sırt +15 (D 46) → 290 │
│    kemer ardı kabin (G0)  x 849–960 · üstten 573–651 (4,0 m @ D 46 = 111 px)    │
│    bakım alanı kabin      x 600–760 · üstten 724–836 (160 × 112 px)             │
│    giriş merdiveni        x 894–993 · yakın biniş tabanı x 1076–1251 · üstten ≈715 │
│    halat çizgisi          yakın baş (x 1164 · 540) → karşı baş (x 1443 · 262)    │
│                           orta (D 91) x ≈1375 · 329 — kabin orada 56 px          │
│    karşı istasyon         x 1427–1591 · üstten 229–321 · kabin 37 px · insan 16 px │
│    karşı seyir terası     x 1619–1710 · üstten ≈321                              │
│    yakın insan (D 36)     ≈60 px — okunur siluet, yüz yok                       │
│ ⛔ ÖN GÖRSELLEŞTİRME: 00_ANALIZ/02 §3 (betik) — bu sayılar yaklaşık; onaydan sonra │
│    kesinleşir. Açıklık 3B ≈108 m (yakın baş x 7 · D 44 · +6 → karşı x 52 · D 138 · +36) │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① SOL: gri kireçtaşı yamaç omzu (x 0–300) — salonun solunda, kadrajın sol kenarı │
│ ② KARŞI SIRT: ormanlı dağ sırtı, bütün kadraj eni (üstten ≈150–260)             │
│ ③ SAĞ ALT: kaya burnu (x ≈1775 · tepe üstten ≈773) — ön planda, likenli         │
│ ④ ⭐ KANIT NESNESİ: taş ayaklı küçük çan kemeri, dökme demir çan — yakın kaya    │
│    rafında, biniş tabanının sağ önünde (x 1328–1392 · üstten 640–780 · 64 × 140 px) │
│    91 ana karede birebir; hiçbir iş ona dokunmaz                                 │
│ + korpus kilidi (her SITE'ta birebir): "The valley holds exactly one cableway     │
│   and exactly one cabin, this one; no other cabin, tower, chair or line stands    │
│   anywhere in view."                                                            │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ yakın salon: kireçtaşı · 24 × 12 m · saçak +9 · sırt +15 · cephede 5 kemer      │
│   (sayı ve yer HİÇ değişmez) · çatı: 4 panel → 5 çelik makas + ahşap + çinko     │
│ yakın biniş tabanı: salonun sağ ucundan 6 m vadiye taşan konsol · zemin y 0       │
│ giriş merdiveni: taş, bahçe (y −2) → zemin (y 0) · yanında su kanalı (S75+)      │
│ makine: yatay makara tekerleği Ø 4,0 m (salonun sağ ucu) · gerdirme ağırlığı kuyusu │
│   (sol uç) · hat başlığı çerçevesi ≈6 m, iki ayaklı, koyu grafit gri              │
│ karşı istasyon: kireçtaşı · 18 × 10 m · zemin +30 · sırt +40 · aynı malzeme ailesi │
│ seyir terası: karşı istasyonun sağında kaya burnu üstü, çelik konsol + ahşap      │
│ halatlar: 2 taşıyıcı (kalın, koyu) + 1 çekme (ince, kapalı döngü) · ara direk YOK  │
│ KABİN: TEK · 4,0 × 2,6 × 2,8 m · kutu gövde · her uzun yüzde 3 pencere · tek       │
│   sürgülü kapı (yakın yüz) · üstte askı kolu + 4 makaralı taşıyıcı                │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 📒 DEFTERLER — sahne aralığına bağlı hâller

| defter | hâl | kareler |
|---|---|---|
| **KABİN** | salonda, askı kirişinde, paslı, camları kırık | G0–G1 |
| | bakım alanında beşikte, paslı | G2–G54 |
| | camsız, içi boş, paslı | G55 |
| | çıplak gri çelik → açık gri astar | G56 · G57 |
| | **derin kırmızı + ince krem şerit**, camsız → camlı | G58 · G59 |
| | askı kolu takılı (beşikte) → vinçte → halatta | G60 · G61 · G62+ |
| | yakın peron (G63–G64) · halatta (G65–G66) · karşı peron (G67) · yakın (G68–G69) · ortada yüklü (G70) · yakın (G71–G84) · halatta (G85–G87) · karşı (G88–G89) · dönüşte (G90) | |
| **ÇATI (yakın)** | eski 4 panel (G0) → panel azalır (G1–G4) → çatısız (G5–G27) → makas (G28–G29) → ahşap (G30–G31) → membran (G32) → çinko (G33–G34+) | |
| **ÇATI (karşı)** | çökük (G0–G4) → yarım (G5–G7) → çatısız (G8–G34) → iskelet + ahşap (G35) → çinko (G36+) | |
| **HALAT** | yok (G0–G45) → pilot (G46) → + çekme (G47) → taşıyıcı yarıda (G48–G49) → 1 taşıyıcı (G50) → 2 (G51) → gergin (G52) → 3 halat (G53+) | |
| **VİNÇ (yakın)** | her ana karede YÜKLÜ (panel · kabin sapanı · kova · kiriş · tekerlek · makas · paket · kabin); G63'ten **yok** | G0–G62 |
| **VİNÇ (karşı)** | küçük mobil vinç karşı servis yolunda | G5–G8 · G23–G24 · G35–G36 · G43–G44 |
| **SU** | kanal kuru (G0–G75) → akıyor (G76+) | |
| **IŞIK** | armatür yok (G0–G77) → sönük (G78–G79) → yakın yanık (G80) → ikisi yanık (G81+) | |
| **İNSAN** | ekip: A'da görünür, hızlı · S78 boş · ziyaretçi: S81'den, her biri yürüyerek girer, yüz okunmaz | |

---

## ☀️ IŞIK GÜNÜ VE REJİM [ZAMAN_VE_ISIK · SANTIYE_HAREKETI §1 · HAVA_VE_ATMOSFER]

```
GÜN        yaz sonu · 45° K · gün doğumu ≈05:00 (az ≈62°) · batımı ≈19:28 (az ≈298°)
KADRAJ     bearing 10° · yatay görüş 73,7° → 333°–47° · güneş yayı 75° (06:10) → 180° → 298° — HEP kadraj dışı [DERS 39]
           sabah ışığı SAĞDAN (doğu), gölgeler sola · akşam SOLDAN (batı), gölgeler sağa → gün boyu gölge süpürmesi
REJİM      A (≈10 dk / klip)  81 klip  = 13 sa 30 dk
           G (gerçek zaman)    9 klip  =  0 dk  → S64–S66 ilk boş geçiş · S84–S89 final geçiş + varış
           B · C               YOK (1 × B = 2 sa → 14 sınırını aşar)
Σ          06:10 → 19:40 = 13 sa 30 dk ≤ 14 ✅
PERDE SAATİ  1 06:10–07:40 sabah · 2 07:40–09:10 · 3 09:10–10:40 · 4 10:40–12:10 öğle · 5 12:10–13:40 ·
             6 13:40–15:10 (S48 sağanak) · 7 15:10–16:40 · 8 16:40–17:40 (G = 16:50 sabit) · 9 17:40–19:10 altın saat ·
             10 19:10–19:40 batım → mavi saat (S84–S89 G = 19:40 sabit)
MEVSİM TAŞIYICISI  tek yaz günü [DERS 14]: güneş azimutu 75° → 297° · gölge süpürmesi (sabah sola ve kameraya →
             öğle uzağa → akşam sağa) · bulut tipi (sabah küçük yüksek → öğle kümülüs → S48 sağanak → akşam ince altın) ·
             ıslak/kuru beton ve taş (S15–S18 · S48–S49) · bahçe yeşili ve akan su (S74+)
⚠️ G DİKİŞLERİ  A → G (S63→S64 · S83→S84) ve G → A (S66→S67): bulut/su dokusu hızı değişir — beyanlı dikiş
```

---

## 🎞️ SAHNE SAHNE PLAN — 10 perde × 9 sahne

> Okuma: **İŞ** klibin içinde ne olduğunu (ve neyin TAŞIDIĞINI — DERS 61: her yeni eleman bir taşıyıcıyla gelir);
> **SAHNE SONU** klibin bittiği ana kareyi G(n+1) tarif eder (zincir: G(n) → I2V → G(n+1)). Saat = klibin başındaki ışık.

### 🎬 PERDE 1 · ÇATI KALKAR, KABİN ÇIKAR, HARABE TEMİZLENİR

`S0–S8` · #01–09 · **00:00–01:12** · ışık 06:10 → 07:40

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S0** · #01 | 00:00–00:08 · 06:10 · A | İlk karede çatının **1. dev paneli** (kabin bölmesinin üstü; perçinli çelik makas + paslı oluklu sac, ≈6 × 13 m) paletli vincin kancasında, çatının ≈1 m üstünde. Panel yükselir, sola döner, bakım alanındaki düz kasalı kamyona iner. Açılan boşluktan salona sabah ışığı düşer; kırık cam kemerin ardında sarmaşıklı salon ve eski askı kirişinde **paslı kırmızı kabin**. | Panel 1 kamyon kasasında, sapanlar bağlı · çatı siluetinde sağ-orta boşluk · salon içi aydınlık, kabin kemerden okunur (x ≈849–960) · karşı yamaçta harap karşı istasyon | müziksiz pencere · vinç dizeli, zincir şakırtısı, sacın gıcırtısı, vadide rüzgâr, uzak kuş | AÇILIŞ NESNESİ · "from the first frame the panel is already rising" · kanca: panel 1 |
| **S1** · #02 | 00:08–00:16 · 06:20 · A | Kamyon paneli soldan kadraj dışına götürür. Vinç kancayı açıklıktan içeri indirir, ekip dört sapanı kabinin askı koluna bağlar; **kabin saçak çizgisinin üstüne çıkar**, sola döner, ön bakım alanındaki çelik beşiğe iner. | Kabin beşikte (x ≈600–760 · üstten 724–836), sapanlar bağlı ve gevşek · salonun içinde askı kirişi boş | halat gerilmesi, metal çınlaması, kısa telsiz cızırtısı (anlaşılmaz) | ⚓ İLK BÜYÜK SONUÇ (0:16) · tek kabin · kanca: kabin sapanları |
| **S2** · #03 | 00:16–00:24 · 06:30 · A | İple çalışan iki ekip cephenin sol yarısında **sarmaşığı şerit şerit söker**; yığınlar el arabalarıyla konteynere. Vinç kabinin sapanlarını çözer, kancaya panel 2'yi bağlar. | Cephenin sol yarısında **ilk temiz açık krem kireçtaşı** yüzey, sağ yarı hâlâ yeşil · karşı istasyon aynı kadrajda hedef · panel 2 kancada, çatının hemen üstünde | budama makasları, yaprak hışırtısı, el arabası tekerleği | karşı istasyon x 1427–1591 her karede · kanca: panel 2 |
| **S3** · #04 | 00:24–00:32 · 06:40 · A | Panel 2 ve 3 sırayla kalkar, iki kamyona iner; kamyonlar sırayla soldan çıkar. | Yakın salonda yalnız sol uç paneli (4) kaldı · taş duvarların üst kenarı göğe karşı · panel 4 kancada | iki kamyonun geri vites uyarısı (tonsuz bip), sac sesi | kanca: panel 4 |
| **S4** · #05 | 00:32–00:40 · 06:50 · A | Panel 4 kalkar. **Karşı yamaçta** servis yolundan gelmiş küçük mobil vinç, karşı istasyonun çökmüş çatısını parça parça indirmeye başlar (uzak, küçük). | Yakın salon tamamen çatısız taş kabuk · karşı istasyonun çatısının yarısı inmiş · yakın vinç kancasında moloz kovası | yakın dizel + uzaktan, vadinin karşısından gelen soluk yankı | ⚓ yeni mekân: karşı şantiye · kanca: moloz kovası |
| **S5** · #06 | 00:40–00:48 · 07:00 · A | Salonun içinde mini ekskavatör ve ekip: moloz, çürük ahşap, kırık eski makine parçaları kovayla vinçten kamyona. Ön bahçede çalılar biçilir. | Salon zemini molozsuz (kemerden okunur) · bahçe biçilmiş, kesik dallar yığında · kamyon dolu | kepçe sürtmesi, çakıl dökülmesi, tırpan | kanca: moloz kovası |
| **S6** · #07 | 00:48–00:56 · 07:10 · A | İskele kulesinden kırık cam kemerin kalan cam parçaları ve çürük çerçeveler sökülür; cephenin sağ yarısından sarmaşık sökülür. | Cephe tamamen sarmaşıksız, taş yer yer koyu lekeli · **beş kemer** boş açıklık (sayı ve yer sabit) | cam kırıklarının kasaya dökülmesi, ahşap çatırtısı | LOCK: "exactly five arched openings" · kanca: cam kasası |
| **S7** · #08 | 00:56–01:04 · 07:20 · A | Karşı istasyonda çatının kalan yarısı iner, karşı vinç onu servis yoluna bırakır; yakında kamyonlar son molozu götürür. | **İki istasyon da çatısız taş kabuk** — film ilk kez iki boş kabuğu yan yana gösterir; aralarında boş vadi | iki yamaçtan iki ayrı dizel, aradaki boşlukta rüzgâr | merak ③ keskinleşir · kanca: boş sapanlı yük kirişi (spreader) |
| **S8** · #09 | 01:04–01:12 · 07:30 · A | Cephe önüne iki iskele kulesi kurulur; salonun içi süpürülür; beşikteki kabinin yanına branda ve el aletleri sandığı bırakılır. | Harabe temiz: moloz yok, sarmaşık yok · cephe önünde iki iskele kulesi · paslı kabin beşikte bekliyor | boru iskelesi çınlaması, süpürge | PERDE SONU · kanca: iskele borusu demeti |

### 🎬 PERDE 2 · TAŞ CEPHELER, GİRİŞ MERDİVENİ, İKİ BİNİŞ TABANI

`S9–S17` · #10–18 · **01:12–02:24** · ışık 07:40 → 09:10

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S9** · #10 | 01:12–01:20 · 07:40 · A | İskeleden basınçlı suyla cephenin sol yarısı yıkanır; koyu kir aşağı akar, ön kanala süzülür. | Sol yarı açık krem, sağ yarı gri-kirli — dikey, net bir sınır | basınçlı su tıslaması, damla, kanalda akan çamurlu su | ⚓ yeni iş türü (yıkama) · gölge sağdan sola (sabah güneşi doğuda) |
| **S10** · #11 | 01:20–01:28 · 07:50 · A | Sağ yarı yıkanır; taş ustaları kırık blokları tebeşirle işaretler. | Bütün cephe temiz krem kireçtaşı · kemer kilit taşlarında birkaç kırık blok boşluğu okunur | su, ıslak taşta adım |  |
| **S11** · #12 | 01:28–01:36 · 08:00 · A | Forklift paletlerle yeni kesme taş blokları getirir; ustalar iskele üstündeki makarayla kırık blokları değiştirir. | Beş kemer bütün; yeni taşlar hafif daha açık (yama okunur, renk aynı aile) | keski, tokmak, makara zinciri | LOCK: kemer sayısı 5 |
| **S12** · #13 | 01:36–01:44 · 08:10 · A | Giriş merdiveninin kırık eski basamakları kırıcıyla sökülür, ekskavatör yükler; beton tabanı dökülür. | Merdiven yeri boş · ıslak koyu gri beton taban (x ≈894–993) | kırıcının kesik vuruşları, mikser tamburu |  |
| **S13** · #14 | 01:44–01:52 · 08:20 · A | Taş basamaklar aşağıdan yukarı tek tek yerleştirilir (forklift + iki usta); yanlarda korkuluk ankrajları. | Geniş taş merdiven tamam (bahçeden peron seviyesine, ≈2 m) · korkuluk henüz yok | taşın taşa oturuşu, tokmak | ⚓ yeni eleman: merdiven |
| **S14** · #15 | 01:52–02:00 · 08:30 · A | Yakın istasyonun **biniş tabanı** (salonun sağ ucundan vadiye taşan konsol döşeme): çürük eski döşeme sökülür, paslı konsol kirişler kumlanır. | Vadinin üstünde **çıplak çelik konsol kirişler**, döşemesiz — altında gölgeli boşluk | kumlama hışırtısı, rüzgâr | ⚓ DİRENÇ: boşluk ekranda · kanca: yeni kiriş demeti (S15 için) |
| **S15** · #16 | 02:00–02:08 · 08:40 · A | Vinç yeni çelik kirişleri ve trapez sac paketlerini konsola indirir; pompa kamyonu betonu döker, ekip mastarlar. | Yakın biniş tabanı yeni beton yüzeyle, ıslak koyu gri (x ≈1076–1251 · üstten ≈715) · kenarında geçici korkuluk | beton pompası, vibratör vızıltısı | kanca: sac paketi |
| **S16** · #17 | 02:08–02:16 · 08:50 · A | Karşı istasyonda cephe yıkanır, biniş tabanının kalıbı kurulur (uzak, küçük). | Karşı istasyon cephesi krem · karşı biniş tabanı kalıplı | uzak yankı; yakında ıslak beton üstüne örtü serilmesi |  |
| **S17** · #18 | 02:16–02:24 · 09:00 · A | Karşı yamaçta pompa kamyonu karşı biniş tabanını döker; yakında beton kürü için ıslak örtüler gerilir. | **İki istasyonun biniş tabanı yeni** · iki kabuk temiz · aralarında hâlâ boşluk | uzak pompa, yakında su hortumu | PERDE SONU |

### 🎬 PERDE 3 · ÇATILAR AÇIKKEN AĞIR MEKANİZMALAR VE HAT BAŞLIKLARI

`S18–S26` · #19–27 · **02:24–03:36** · ışık 09:10 → 10:40

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S18** · #19 | 02:24–02:32 · 09:10 · A | Ağır yük kamyonu bakım alanına büyük yatay **çelik makara tekerleğini** (Ø 4 m) getirir; vinç onu kamyondan kaldırır. | Tekerlek vinçte, açık çatının hemen üstünde, salonun sağ ucuna hizalı | ağır kamyonun hava freni, halat gerilmesi | ⚓ yeni ve büyük eleman · kanca: tekerlek |
| **S19** · #20 | 02:32–02:40 · 09:20 · A | Tekerlek açık çatıdan salonun sağ ucundaki çelik çerçeveye iner; ekip cıvatalar. | Tekerlek yerinde — üst yayı kemerden ve saçak çizgisinden okunur · koyu grafit gri | tork anahtarı, metalin metale oturması | kanca: tahrik kutusu (sonraki) |
| **S20** · #21 | 02:40–02:48 · 09:30 · A | Tahrik motoru ve dişli kutusu (iki büyük kutu yük) vinçle çatıdan indirilir. | Makine dairesi dolu: kemerlerin ardında koyu gri bloklar | zincir, kısa elektrik vızıltısı | kanca: hat başlığı çerçevesi |
| **S21** · #22 | 02:48–02:56 · 09:40 · A | Vinç koyu gri çelik **hat başlığı çerçevesini** biniş tabanının ucuna diker (≈6 m yüksek, iki ayaklı); ekip ankraj cıvatalarını sıkar. | Biniş tabanı ucunda hat başlığı — vadiye bakan koyu bir kapı gibi (x ≈1164) | çelik çınlaması, rüzgâr | ⚓ yeni siluet |
| **S22** · #23 | 02:56–03:04 · 09:50 · A | Karşı yamaçta karşı vinç karşı istasyonun tekerleğini açık çatıya indirir (uzak). | Karşı istasyon kancasında tekerlek, çatı açık | uzak dizel |  |
| **S23** · #24 | 03:04–03:12 · 10:00 · A | Karşı tekerlek yerinde; karşı hat başlığı çerçevesi dikilir. | **İki hat başlığı vadinin iki yakasında birbirine bakar** — aralarında hiçbir çizgi yok | rüzgâr, iki yakadan iki tok vuruş | merak ③ en keskin hâli |
| **S24** · #25 | 03:12–03:20 · 10:10 · A | Yakın salonun sol ucundaki kuyuya beton **gerdirme ağırlığı** indirilir; üstüne çelik kafes kurulur. | Kuyunun üstünde çelik kafes (salonun sol ucunda, saçak hizasında) | beton bloğun kuyuya oturuşu, derin tok ses | kanca: ağırlık bloğu |
| **S25** · #26 | 03:20–03:28 · 10:20 · A | Elektrik panoları ve kablo kanalları taşınır; ekip makine dairesinde çalışır. | Makine dairesi tamam · çatısız salonda ekip ve paletler | matkap, kablo makarası | kanca: pano paleti |
| **S26** · #27 | 03:28–03:36 · 10:30 · A | Vinç ilk yeni **çelik çatı makasını** taşır. | Makas 1 kancada, salonun sağ ucunun hemen üstünde | halat gerilmesi | PERDE SONU · kanca: makas 1 |

### 🎬 PERDE 4 · İKİ İSTASYONUN ÇATILARI YENİDEN KURULUR

`S27–S35` · #28–36 · **03:36–04:48** · ışık 10:40 → 12:10

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S27** · #28 | 03:36–03:44 · 10:40 · A | Makas 1 duvar başlarına oturur, ekip cıvatalar; makas 2 kancaya alınır. | İki yeni galvaniz gri makas yerinde (sağ uç) | cıvata, kuş | ⚓ yeni eleman: çatı · kanca: makas 3 |
| **S28** · #29 | 03:44–03:52 · 10:50 · A | Makas 3, 4, 5 sırayla oturur. | Beş makas — çatı iskeleti tam, göğe karşı ritmik siluet · **sırt +15 m, saçak +9 m (eski çizgi)** | her oturuşta tok bir metal sesi | LOCK: çatı siluetinin eski çizgisi |
| **S29** · #30 | 03:52–04:00 · 11:00 · A | Aşık ve ahşap kaplama tahtası paketleri vinçle çatıya; marangozlar sağdan sola döşer. | Çatının sağ yarısı açık sarı ahşap kaplamalı · ⭐ BÖLÜM SINIRI KARESİ **G30** | çivi tabancası, tahta sesi | ⭐ G30 = BOLUM_1 son karesi = BOLUM_2 ilk görseli · kanca: tahta paketi |
| **S30** · #31 | 04:00–04:08 · 11:10 · A | Sol yarı ahşapla kaplanır. | Bütün çatı açık sarı ahşap | çivi tabancası ritmi | BOLUM_2 ilk sahnesi |
| **S31** · #32 | 04:08–04:16 · 11:20 · A | Koyu gri su yalıtım membranı rulolar hâlinde açılır. | Çatı koyu gri membranla kaplı | rulo açılması, brülör yok (soğuk yapışkan) |  |
| **S32** · #33 | 04:16–04:24 · 11:30 · A | Kurşun grisi **dikişli çinko** levhalar sağdan döşenir. | Çatının sağ yarısı çinko; dikiş çizgileri ışığı yakalar | sac bükme, tokmak | ⚓ malzeme değişimi · kanca: çinko paketi |
| **S33** · #34 | 04:24–04:32 · 11:40 · A | Sol yarı çinko + mahya. | **Yakın istasyonun çatısı tam** — eski siluetle aynı çizgi | son tokmak, rüzgâr |  |
| **S34** · #35 | 04:32–04:40 · 11:50 · A | Karşı istasyonda makaslar ve ahşap kaplama (uzak). | Karşı istasyon çatısı iskelet + ahşap | uzak çivi tabancası yankısı |  |
| **S35** · #36 | 04:40–04:48 · 12:00 · A | Karşı çatı çinkoyla tamamlanır. | **İki istasyon da çatılı** — merak ① kısmen cevaplandı | rüzgâr, uzak bir tokmak | PERDE SONU · kanca: cam doğrama paleti |

### 🎬 PERDE 5 · CAM CEPHELER, AHŞAP PERONLAR, KARŞI SEYİR ALANI

`S36–S44` · #37–45 · **04:48–06:00** · ışık 12:10 → 13:40

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S36** · #37 | 04:48–04:56 · 12:10 · A | Beş kemer açıklığına koyu bronz çelik doğrama ızgaraları takılır. | Beş kemerde doğrama, cam yok | matkap, çelik | ⚓ yeni eleman: cam cephe |
| **S37** · #38 | 04:56–05:04 · 12:20 · A | Paletli küçük cam robotu vantuzlarla büyük cam panelleri soldan takar. | Sol üç kemer camlı — **net şeffaf**, içerisi okunur (ayna değil) | vantuz pompası, camın contaya oturuşu | U: cam ayna/siyah ekran olmaz |
| **S38** · #39 | 05:04–05:12 · 12:30 · A | Sağ iki kemer camlanır. | Bütün cephe camlı · camın ardında tekerlek ve makine dairesi | aynı |  |
| **S39** · #40 | 05:12–05:20 · 12:40 · A | Yakın biniş tabanına sıcak yağlı ahşap peron döşemesi: paletler + marangozlar. | Yakın peronun yarısı ahşap | tahta, matkap | ⚓ malzeme sıcaklığı |
| **S40** · #41 | 05:20–05:28 · 12:50 · A | Ahşap döşeme tamamlanır; ince koyu çelik korkuluk (gergin çelik tel dolgulu) takılır. | Yakın peron ahşap, korkuluklu | tel gerdirme tıkırtısı |  |
| **S41** · #42 | 05:28–05:36 · 13:00 · A | Karşı istasyonun camları ve ahşap peronu (uzak). | Karşı istasyon cephesi öğle ışığında parlar, peron ahşap | uzak |  |
| **S42** · #43 | 05:36–05:44 · 13:10 · A | Karşı istasyonun sağındaki kaya burnuna karşı vinç **seyir terasının** çelik konsol iskeletini kurar. | Seyir terası iskeleti kaya üstünde (x ≈1619–1710) | uzak çelik çınlaması | ⚓ yeni hedef: seyir alanı |
| **S43** · #44 | 05:44–05:52 · 13:20 · A | Seyir terası ahşap döşeme, korkuluk ve birkaç bank. | Karşı seyir alanı tamam — açık ahşap şerit | uzak |  |
| **S44** · #45 | 05:52–06:00 · 13:30 · A | Yakında merdiven korkulukları (koyu çelik) ve çift kanatlı ahşap giriş kapısı takılır. | İki istasyon dıştan bitmiş — **ama aralarında hat yok** | kapı menteşesi, rüzgâr | PERDE SONU · merak ③ son kez açılır |

### 🎬 PERDE 6 · HALATLAR VADİYİ GEÇER, İKİ İSTASYON BAĞLANIR

`S45–S53` · #46–54 · **06:00–07:12** · ışık 13:40 → 15:10

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S45** · #46 | 06:00–06:08 · 13:40 · A | Yakın hat başlığındaki vinç tamburu döner; ekip **ince pilot halatı** vadinin gölgeli dibinden yukarı çeker — halat iki yakada yükselip boşluğun üstünde gevşek bir yay çizer. | İki hat başlığı arasında ince, gevşek pilot halat (ilk çizgi) | tambur tıkırtısı, rüzgârda halat ıslığı | ⚓ İLK BAĞ · taşıyıcı: tambur + ekip ("vanish/appear" yok) |
| **S46** · #47 | 06:08–06:16 · 13:50 · A | Pilot halatla daha kalın **çekme halatı** geçirilir; yakında kamyon üstündeki büyük ahşap makara döner. | İkinci, daha kalın halat vadiyi geçer, sarkık | makara gıcırtısı |  |
| **S47** · #48 | 06:16–06:24 · 14:00 · A | Kalın koyu **taşıyıcı halat** çekilmeye başlar; makara döner, halat ucu çekme halatı boyunca karşıya ilerler. | Taşıyıcı halatın ucu vadinin ortasını geçmiş | derin tambur uğultusu |  |
| **S48** · #49 | 06:24–06:32 · 14:10 · A | ⚠️ **DİRENÇ:** batıdan kısa bir yaz sağanağı geçer — rüzgâr sertleşir, iş durur, ekip hat başlığından geri çekilir, yarı çekilmiş halat hafifçe salınır; yağmur taşı ve ahşabı koyulaştırır. | Sağanak geçmiş, yüzeyler ıslak koyu, bulut doğuya çekiliyor · halat ucu AYNI yerde (iş durdu) | yağmurun çinkoya vuruşu, uzak gök gürültüsü (tek), sonra damlalar | ⚓ DİRENÇ ANI · ışık bulutla kısılır ama kesmede atlamaz |
| **S49** · #50 | 06:32–06:40 · 14:20 · A | İş sürer; taşıyıcı halatın ucu karşı hat başlığına ulaşır, karşı ekip ankraja bağlar. Islak yüzeyler kurur. | **Birinci taşıyıcı halat iki istasyon arasında**, gevşek | damlalar azalır, tambur |  |
| **S50** · #51 | 06:40–06:48 · 14:30 · A | İkinci taşıyıcı halat aynı yoldan çekilir. | İki paralel taşıyıcı halat | tambur |  |
| **S51** · #52 | 06:48–06:56 · 14:40 · A | **Gerdirme:** yakın salondaki gerdirme ağırlığı kuyusunda iner; halatların sarkması azalır, çizgiler düzelir ve yükselir. | İki taşıyıcı halat gergin, düz çizgiler — (x 1164 · üstten 540) → (x 1443 · üstten 262) · **iki istasyon görsel olarak bağlandı** | halatın gerilirken çıkardığı uzun, alçalan ton | ⚓ büyük sonuç · merak ③ cevap |
| **S52** · #53 | 06:56–07:04 · 14:50 · A | İnce **çekme halatı** tekerleğe sarılır ve kapalı döngü olur. | Üç halat çizgisi (2 kalın · 1 ince) — hat tamam | tekerlek tıkırtısı |  |
| **S53** · #54 | 07:04–07:12 · 15:00 · A | İki hat başlığında ekip halat eyerlerini kapatır, koruma kapaklarını takar; bakım alanında paslı kabinin çevresine iskele kurulur. | Hat tamam · **paslı kabin iskele içinde** (görünür, perde yok) — yenileme başlıyor | iskele borusu, rüzgârda halat | PERDE SONU · merak ② geri döner |

### 🎬 PERDE 7 · AYNI PASLI KABİN YENİLENİR VE HATTA ASILIR

`S54–S62` · #55–63 · **07:12–08:24** · ışık 15:10 → 16:40

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S54** · #55 | 07:12–07:20 · 15:10 · A | Kabinden kırık camlar sökülür, eski çürük ahşap bank ve iç kaplama dışarı taşınır, kapı çıkarılır. | Kabin camsız, içi boş, her yer pas | cam kırığı, ahşabın kopması | ⚓ odak değişimi: kabin · GÖVDE DEFTERİ: "rust" G0–G55 |
| **S55** · #56 | 07:20–07:28 · 15:20 · A | İskele çevresinde kumlama: gri toz sola savrulur. | **Kabin gövdesi çıplak mat gri çelik — pas yok** | kumlama hışırtısı | LOCK: kabin boyu ve oranları aynı (4,0 × 2,6 × 2,8 m) |
| **S56** · #57 | 07:28–07:36 · 15:30 · A | Kaynakçı yamaları kapatır; açık gri astar püskürtülür. | Kabin açık gri astarlı | kaynak çıtırtısı, kompresör |  |
| **S57** · #58 | 07:36–07:44 · 15:40 · A | **Kırmızı boya:** derin sinyal kırmızısı gövde + pencerelerin altında ince krem şerit. | Kabin parlak kırmızı — eski kabinle aynı model, aynı oran | boya tabancası, kompresör | ⚓ renk dönüşü · kırmızı yalnız kabinde (palet kilidi) |
| **S58** · #59 | 07:44–07:52 · 15:50 · A | Yeni net camlar ve sürgülü kapı takılır; içeri tek parça ahşap bank (büyük modül) taşınır. | Kabin camlı, kapı kapalı, iç ışığı yok | vantuz, kapı rayının kayışı |  |
| **S59** · #60 | 07:52–08:00 · 16:00 · A | Vinç yeniden boyanmış koyu gri **askı kolunu** ve makaralı taşıyıcıyı kabinin üstüne indirir; ekip birleştirir. İskele sökülür. | Kabin + askı kolu + makaralı taşıyıcı tek gövde, beşikte; vinç kancası askıya bağlı ve gergin · ⭐ BÖLÜM SINIRI KARESİ **G60** | cıvata, iskele borusu | ⭐ G60 = BOLUM_2 son karesi = BOLUM_3 ilk görseli · kanca: kabin (gergin) |
| **S60** · #61 | 08:00–08:08 · 16:10 · A | Vinç kabini beşikten kaldırır, biniş tabanının ucuna, taşıyıcı halatların hemen altına getirir. | Kabin vinçte, peronun ucunda, halatların ≈1 m altında asılı | halat gerilmesi, rüzgâr | BOLUM_3 ilk sahnesi · ⚠️ DERS 57: uzun taşıma (≈25 m) — pilot önceliği |
| **S61** · #62 | 08:08–08:16 · 16:20 · A | Ekip makaralı taşıyıcıyı taşıyıcı halatlara oturtur, çekme halatına kenetler; sapanlar gevşer. | **Kabin halatta asılı**, peron kenarında · vinç sapanları bağlı, gevşek | kenetin tok tıkı, halatın kısa titreşimi | ⚓ büyük sonuç · merak ② cevap |
| **S62** · #63 | 08:16–08:24 · 16:30 · A | Sapanlar çözülür; vinç bomunu yatırır ve paletleriyle kadrajın soluna çıkar. | **Vinç yok** · kabin peronda, kapı açık, iki teknisyen içinde | paletlerin uzaklaşan sesi | PERDE SONU · son vinç karesi — G63'ten "crane" yok |

### 🎬 PERDE 8 · BOŞ KABİNİN İLK GEÇİŞİ, ARDINDAN YÜKLE DENEME

`S63–S71` · #64–72 · **08:24–09:36** · ışık 16:40 → 17:40

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S63** · #64 | 08:24–08:32 · 16:40 · A | Teknisyenler makine dairesinde (camın ardında); peronda son kontrol; kapı kapanır. Tekerlek ilk kez döner. | Kabin boş, kapı kapalı, peron boş — çıkışa hazır | **motorun ilk vınlaması**, tekerleğin yavaş dönüşü | ⚓ beklenti · ışık sabitlenir (G'den önceki kesme) |
| **S64** · #65 | 08:32–08:40 · 16:50 · **G** | ⭐ **İLK GEÇİŞ — gerçek hız.** Kabin peronu terk eder, hat başlığının altından geçip vadinin üstüne çıkar. | Kabin ≈35 m açıkta, boşluğun üstünde (x ≈1260) | makaraların halat eyerinden geçerken iki tok tıkırtı, rüzgâr | "moves at natural speed … eight seconds pass" · gölge yok |
| **S65** · #66 | 08:40–08:48 · 16:50 · **G** | Kabin vadinin ortasından geçer — altındaki boşluk en derin. | Kabin ≈70 m'de (x ≈1375 · üstten ≈329), karşı istasyona ≈⅓ kala | yalnız rüzgâr ve halatın uğultusu — en sessiz an | ⚓ DORUK adayı |
| **S66** · #67 | 08:48–08:56 · 16:50 · **G** | Kabin yavaşlayarak karşı perona girer ve durur. | **Kabin karşı istasyonda** (uzak, kırmızı ≈37 px) | uzak, yumuşak bir fren sesi | merak ⑤ açılır: taşır mı? |
| **S67** · #68 | 08:56–09:04 · 16:50 · A | Kabin muayene hızında (10 dk'da ≈108 m) klip boyunca geri kayar. | Kabin yakın peronda | sürekli tekerlek uğultusu | yeniden A — su/doku dikişi beyanlı |
| **S68** · #69 | 09:04–09:12 · 17:00 · A | Ekip el arabalarıyla kabine mavi su dolu test bidonları taşır. | Kabin içi bidonlarla dolu, kapı kapalı | plastik bidon tokuşması | ⚓ yük |
| **S69** · #70 | 09:12–09:20 · 17:10 · A | **Yüklü kısa deneme:** kabin muayene hızında vadinin ortasına kayar, **durur (fren testi)**, asılı bekler. | Yüklü kabin vadinin ortasında durmuş; halat sarkması belirgin derin | frenin uzun gıcırtısı, sonra rüzgâr | ⚓ DİRENÇ: ağırlık |
| **S70** · #71 | 09:20–09:28 · 17:20 · A | Kabin geri gelir; bidonlar boşaltılır, el arabalarıyla peron dışına. | Kabin yakın peronda, boş | su boşaltma, bidon |  |
| **S71** · #72 | 09:28–09:36 · 17:30 · A | Son kontrol: kapı, fren; camlar silinir. | Kabin parlak, boş, kapı kapalı — deneme bitti | cam silme, kısa telsiz | PERDE SONU · merak ⑤ cevap |

### 🎬 PERDE 9 · ŞANTİYE TEMİZLENİR; BAHÇE, SU, TERAS, IŞIKLAR

`S72–S80` · #73–81 · **09:36–10:48** · ışık 17:40 → 19:10

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S72** · #73 | 09:36–09:44 · 17:40 · A | Son araçlar ayrılır: iskele kuleleri, beşik ve konteyner kamyonlara; kamyonlar sırayla **soldan kadraj dışına** çıkar. | Bakım alanı boş, çakılda izler | uzaklaşan motorlar | ⚓ boşalma · DERS 61: araç yürüyerek çıkar |
| **S73** · #74 | 09:44–09:52 · 17:50 · A | Ön bahçe tesviye edilir, çakıl tırmıklanır, beşik izleri silinir; bahçe yatakları kazılır. | Bahçe toprağı hazır, düz | tırmık, kürek |  |
| **S74** · #75 | 09:52–10:00 · 18:00 · A | Paletlerle bitkiler gelir: çalılar, otlar, iki genç ağaç; ekip diker. | Yeşil yataklar, iki genç ağaç | kürek, toprak | ⚓ canlılık |
| **S75** · #76 | 10:00–10:08 · 18:10 · A | **Su:** merdivenin yanındaki taş kanala eski kaynağın suyu yeniden verilir — su basamak basamak akmaya başlar, küçük havuzda toplanır. | Merdiven yanında ince su kanalı akıyor, havuz dolu | **suyun ilk akışı** — sonraki her sahnede sürekli | ⚓ yeni hareket katmanı · SU KOTU DEFTERİ |
| **S76** · #77 | 10:08–10:16 · 18:20 · A | Merdiven başında taş teras: ahşap banklar ve saksılar yerleşir. | Teras tamam | su, bank ayağı |  |
| **S77** · #78 | 10:16–10:24 · 18:30 · A | Armatürler takılır: duvar aplikleri, merdiven lambaları, peron lambaları (hepsi sönük). | Armatürler yerinde, hepsi sönük | su, matkap | ISIK DEFTERİ: armatür önceden sönük |
| **S78** · #79 | 10:24–10:32 · 18:40 · A | Son temizlik: cam silme, peron süpürme; karşı istasyonda son ekip ayrılır (uzak). | **Şantiye boş, kimse yok** · güneş alçak, altın ışık | su, kuş, akşam rüzgârı |  |
| **S79** · #80 | 10:32–10:40 · 18:50 · A | ⭐ **IŞIK:** yakın istasyonun lambaları gruplar hâlinde, her grup tek seferde yanar — önce salon içi, sonra peron, en son merdiven ve bahçe. | Yakın istasyon sıcak sarı ışıkla · karşı istasyon henüz sönük | her grupta tek bir röle tıkı | ⚓ ışık rejimi · "each group at once" |
| **S80** · #81 | 10:40–10:48 · 19:00 · A | Karşı istasyonun ve seyir alanının lambaları gruplar hâlinde yanar. | **İki istasyon da yanık** · aralarında halatlar akşam göğüne karşı ince çizgi | su, uzak bir tık | PERDE SONU |

### 🎬 PERDE 10 · İLK ZİYARETÇİLER, BİNİŞ, KARŞI YAMACA VARIŞ

`S81–S89` · #82–90 · **10:48–12:00** · ışık 19:10 → 19:40

| S · # | zaman · saat · rejim | İŞ — ne hareket eder (kaynak → taşıyıcı → hedef) | SAHNE SONU — G(n+1) | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S81** · #82 | 10:48–10:56 · 19:10 · A | Giriş kapısı açılır; görevli kapının yanında. İlk ziyaretçiler (6 yetişkin, uzaktan, yüz okunmaz) soldaki patikadan yürüyerek gelir. | Altı ziyaretçi merdivenin dibinde · kabin boş | çakılda adımlar, uzak sohbet uğultusu (kelime yok) | ⚓ İNSAN · KONUK DEFTERİ: her kişi yürüyerek girer |
| **S82** · #83 | 10:56–11:04 · 19:20 · A | Ziyaretçiler merdiveni çıkar, salonun içinden (cam kemerlerin ardında silüetler) perona yürür. | Altı kişi peronda, kabin kapısının önünde | ahşapta adımlar, su |  |
| **S83** · #84 | 11:04–11:12 · 19:30 · A | Kapı açılır, ziyaretçiler tek tek biner; kapı kapanır. **İkinci grup** bahçe patikasından teras banklarına yürür. | Kabin içinde altı silüet, kapı kapalı · terasta ikinci grup (4 kişi) oturuyor · güneş battı | kapı kayışı, su | bundan sonra ışık sabit (G zinciri) |
| **S84** · #85 | 11:12–11:20 · 19:40 · **G** | Kabin kalkar, perondan ayrılır. | Kabin ≈15 m açıkta, içinde silüetler | tekerlek, makara tıkırtısı | gerçek hız · mavi saat |
| **S85** · #86 | 11:20–11:28 · 19:40 · **G** | Kabin boşluğun üstünde ilerler. | Kabin ≈50 m'de | rüzgâr, halat |  |
| **S86** · #87 | 11:28–11:36 · 19:40 · **G** | Kabin vadinin ortasını geçer; ışıklı pencerelerinde silüetler. | Kabin ≈85 m'de | en sessiz an — yalnız rüzgâr | ⚓ son büyük soru: varacak mı? |
| **S87** · #88 | 11:36–11:44 · 19:40 · **G** | Kabin yavaşlayarak karşı perona girer ve durur. | Kabin karşı istasyonda | yumuşak fren |  |
| **S88** · #89 | 11:44–11:52 · 19:40 · **G** | Kapı açılır; ziyaretçiler tek tek inip seyir alanına yürür. | Altı silüet seyir alanına doğru · yakında terastaki grup, akan su | uzak adımlar, yakın su |  |
| **S89** · #90 | 11:52–12:00 · 19:40 · **G** | ⭐ **İŞLEV ANI:** ilk yolcular seyir alanının korkuluğuna varır (0–4 sn); **boş kabin dönüşe başlar** (4 sn'de kımıldar, 8 sn'de ≈10 m açıkta). Su akar, ışıklar yanık, terastakiler küçük hareketler yapar. | **G90 = USTA KARE** — mavi saat, iki ışıklı istasyon, gergin halatlarda dönüşe çıkmış boş kırmızı kabin, seyir alanında silüetler · film **hareket hâlinde 12:00'da** biter | su, rüzgâr, tekerleğin uzaklaşan uğultusu | ⭐ kapak kaynağı · son ekran: YOK önerilir |

---

## 🌟 USTA KARE — G90 (kapak kaynağı)

```
KADRAJ    MAIN STATION, değişmezler aynen · 19:40 mavi saat (güneş ≈ −2°), gök koyu mavi, karşı sırt siluet
YAKIN     taş salon sıcak sarı ışıkla, beş camlı kemer yanık, çinko çatı göğe karşı · merdivende lambalar · yanındaki
          su kanalı akıyor · terasta dört kişilik ikinci grup (yan/arka, yüz yok)
HAT       iki gergin taşıyıcı + ince çekme halatı · KIRMIZI KABİN karşı perondan ≈10 m ayrılmış, ışıklı penceresi boş
KARŞI     karşı istasyon yanık · seyir alanının korkuluğunda altı küçük silüet
SABİT     çan kemeri (kanıt nesnesi) · kaya burnu · sol yamaç omzu · bakım alanının yerinde bahçe
⛔ YOK     vinç, iskele, kamyon, ikinci kabin, sis, ışık huzmesi, yazı
```

---

## ⚠️ UYARILAR VE RİSKLER — onaydan önce bilinmesi gerekenler

| # | risk | nerede | ne yapılacak |
|:-:|---|---|---|
| U-1 | **Karşı istasyon küçük:** D 140 m'de insan ≈16 px, kabin ≈37 px — final varışı (S87–S89) uzaktan okunur | S87–S89 · G90 | kırmızı kabin + ışık ödül taşır; yakın terasta ikinci grup (S83+) yakın ölçekte hayat verir · alternatif: §SAPMA ⑥ |
| U-2 | **Tek kabin kimliği 91 karede:** model kabini kopyalar, ikinci kabin ekler, boyunu değiştirir | her kare | korpus kilidi + "exactly one cabin" + KABİN DEFTERİ · boyut 4,0 × 2,6 × 2,8 LOCK |
| U-3 | **Kabin teleporta düşer:** A'da 10 dk'lık bir geçiş 0,2 sn olur | S67 · S69 · S70 | A'daki geçişler MUAYENE HIZINDA (≈0,18 m/s → klip boyunca kayar); gerçek hız yalnız G'de |
| U-4 | **Uzun yük havada kopyalanır** [DERS 57] | S1 (kabin) · S60 (kabin peron ucuna ≈25 m) | yük ilk karede hedefin hemen üstünde başlar; S60 PİLOT önceliği |
| U-5 | **Halat "belirir":** taşıyıcısız çizgi [DERS 61] | S45–S52 | her halat tambur/makara + ekip ile; "appear/vanish" yazılmaz |
| U-6 | **Sağanak ışığı kırar:** S48 bulut + yağmur, S49 ıslak → kuru | S47–S49 | kesmede ışık atlamaz; bulut S48 içinde gelir ve gider, ıslaklık S49'da kurur |
| U-7 | **Cam ayna/siyah ekran olur** | S37–S38+ | "clear glass, the interior visible through it" · "mirror" YASAK |
| U-8 | **Konuk belirir / koltukta doğar** [DERS 49] | S81–S89 | KONUK DEFTERİ: her kişi yürüyerek girer · yüz okunmaz · yandan/arkadan |
| U-9 | **Işık "yavaşça" yanar ya da hepsi birden** | S79–S80 | "the lights come on in groups, each group at once" |
| U-10 | **Sis vadiyi doldurur, halatlar kaybolur** | her kare | "the air is clear" pozitif · "fog/mist" YASAK |
| U-11 | **Düz ızgara → METRONOM** [DERS 13 · 44] | bütün film | perde başı kanca · rejim nabzı (A → G) · müzik katmanı · iş yönü |
| U-12 | **Pilot halat vadi dibinden çekilir** — dip kadrajda değil | S45 | çizgi gölgeden iki yana yükselir; alternatif drone taşıyıcı (§SAPMA ⑤) |

---

## 🧭 SAPMALAR — sahip metninden farklar (onay gerekir)

| # | sahip metni | bu plan | neden |
|:-:|---|---|---|
| ① | sahneler 01–90 | **S0–S89** (# sütunu 01–90'ı taşır) · zaman kodları birebir aynı | depo standardı (G0…G90 zinciri) |
| ② | ışık belirtilmemiş | **tek yaz gününün ışığı 06:10 → 19:40** · ÜSLUP BEYANI | kesmede ışık atlamaz, Σ ≤ 14 sa [§2.7 ①] |
| ③ | — | **9 klip rejim G** (S64–S66 ilk geçiş · S84–S89 final) | 90 × A = 15 sa sınırı aşar; G ödül hareketinde |
| ④ | Perde 6 yalnız halat | **S48 yaz sağanağı** (iş durur, sonra sürer) | UZUN_FORM §8 madde 7: ortada direnç anı |
| ⑤ | "halatlar çekiliyor" | pilot halat **vadi dibinden tamburla** çekilir | drone kamera hareketi/uçuş korpusu çağırır; istenirse drone |
| ⑥ | "karşı yamaca ulaşıyor" — aynı ana kamera | karşı varış **uzak ölçekte** (insan ≈16 px) + yakın terasta ikinci grup | tek kamera şartı korunur · alternatif: karşı istasyona tek detay klip (ISTASYON_VE_IC_MEKAN dört şart) — sahip kararı |
| ⑦ | "film hareket hâlinde 12:00'da biter" | final 0–4 olay + 4–8 **hareketli tutuş** (boş kabin kayar, su akar) | kılavuz 4+4 durağan tutuş der; sahip metni önce gelir — beyanlı |
| ⑧ | "ilk ziyaretçiler" | 6 kişilik ilk grup + 4 kişilik ikinci grup (terasta bekler) | U-1: yakın ölçekte insan |
| ⑨ | — | kanıt nesnesi: **çan kemeri** · çatı: **dikişli çinko** · kabin: **kırmızı + krem şerit** | depo şartı (kanıt nesnesi · malzeme kimliği) — sahip değiştirebilir |
| ⑩ | ilk üç sahnenin İngilizce promptları | ALINMADI | plan dosyasında prompt yok; PERDE_01'de şablonla yeniden yazıldı |

---

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ format klasörü açıldı             yatay_12_dk_filmler/README.md (90 × 8,0 · 3 bölüm · 15 QA raporu)
✅ sahne sahne plan                  bu dosya — 90 sahne · 10 perde · defterler · ışık günü
◐ HİKÂYE ONAYI                      sahip prompt yazımını istedi; §SAPMALAR ①–⑩ varsayılanla uygulandı → açık onay bekliyor
✅ PROMPTLAR                         PERDE_01 … PERDE_10 · 91 görsel + 90 I2V · üretici 00_ANALIZ/05_SAHNE_CALISMALARI/
✅ PROMPT KAPISI (13.10.2026)         0 BLOCK · 26 FIX — hepsi BEKLENEN: ① ARAÇ KUTU SETİ ölçülmedi · ② düz ızgara (SÜRE
                                     sütunu yok, 90 × 8,0 beyanlı) · ③ S64–S66 / S79–S89 "malzeme akışı yok" ve S79–S83 / S89
                                     "ACTIVITY eli az" — yapım bitti; ödül klipleri (ilk geçiş, ışık, yolcular) kasıtlı olarak
                                     malzeme taşımaz. Koşu: klasör modu 12 dk'yı tanımadığı için birleşik dosyayla —
                                     cat THE_SKY_STATION_PLAN.md PERDE_*/THE_SKY_STATION_PERDE_*.md > /tmp/sky.md
                                     python3 araclar/prompt_kontrol.py /tmp/sky.md
⬜ araçlar 12 dk'yı tanımıyor          film_klasoru_ac.sh · sayac.sh · prompt_kontrol.py (BOLUM_3) · qa_paket.sh (--bolum 3)
⬜ 00_ANALIZ                          okuma çizelgesi → ders hasadı → konsept/risk → sıralama → uyarılar → sahne tablosu (BEŞ SORU)
⬜ ön görselleştirme                  kamera betiği: px sayıları kesinleşir (02 §3)
⬜ KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC · URETIM_GUNLUGU (USTA KARE G90 promptu PERDE_10'un sonunda)
⬜ ARAÇ KUTU SETİ                     üretim günü ölçülür (≥ 9,0 sn kutu)
⬜ PİLOT ÜÇLÜ                         önerilen: S89 (final) · S64 (ilk geçiş) · S60 (kabinin uzun taşıması)
```
