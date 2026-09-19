# 🗒️ THE BORROWED HILL — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ÜÇ DENEME yapılmadı · (17.09.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır [DERS 28] · günlüksüz filme qa_paket.sh açılmaz
```

> Plan: `THE_BORROWED_HILL_PLAN.md` · Promptlar: `_BOLUM_1` (S0–S11) · `_BOLUM_2` (S12–S23 + G24)
> Format: 24 sahne = 25 kare (G0…G24) + 24 I2V · her sahne tek 10,0 sn klip · ⛔ KAPAK KARTI YOK

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32]

```
ARAÇ            [ad + sürüm/mod]          ÖLÇÜM TARİHİ  [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn · beş klip aynı mı: evet/hayır
   ⛔ 10,0 sn teslim {5,10} kutusu ister. {4,6,8} çıkarsa her sahne İKİ zincirli klip
     olur (24 ara kare) → karar SAHİBE döner; plan tek kareli I2V'ye DÜŞÜRÜLMEZ.
   KARAR         ____
② KAMERA        ilk/son kare kayması ____ px   (>2 px ise ÜRETİLMEZ)
③ GÖLGE         ilk/son kare açı farkı ____°   (0° ise ÜRETİLMEZ)
   ⚠️ Mars gölgesi zayıftır; ölçüm için UZUN gölgeli saat seçilir (az 72° ya da 269°)
④ NEGATİF       metin içi __/5 · ayrı alan __/5
⑤ PROMPT TAVANI ____ krk · son nesne göründü mü __/5   (plan promptları 5.736–5.955 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı ____
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI

⭐ ⑨ SAYIM TESTİ — BU FİLMİN BİRİNCİ RİSKİ [DERS 55 · QA_SPEC §6]
   Test promptuna plandaki sayım cümlesi birebir konur. Beş klipte:
     kaç gömülü sığınak: __/__/__/__/__     kaç tepecik: __/__/__/__/__
     tank sayısı: ____   ikinci kubbe/modül kümesi çıktı mı: __
   ⛔ Herhangi bir klipte 2+ sığınak ya da 2+ tepe çıkarsa ARAÇ DEĞİŞİR.
   KARAR         ____

⭐ ⑩ BİLİMKURGU TESTİ — POLAR HABITAT'ın arızası [QA_SPEC §7]
   Test klibinde ışık huzmesi · hale · lens parlaması · parlayan panel · enerji arkı
   çıktı mı: __/5    ⛔ 1/5'ten fazlaysa negatif çekirdek yetmiyor → ARAÇ DEĞİŞİR.

⭐ ⑪ ÇÖZÜNÜRLÜK — üç yakınlaşma buna bağlı
   ffprobe stream=width,height → ____ × ____ px
   ⛔ ≥ 3840 × 2160 → plandaki 2,0× geçerli · altındaysa tavan düşer ve §KURGU yeniden yazılır
   [genel yordam: ARAC_KARTLARI §4 ÖLÇÜM 9 · sayılar: KAMERA_HAREKETI_KILAVUZU §3.3]

⑫ MARS IŞIĞI TESTİ (bu filme özel)
   "weak soft-edged shadows with visible atmospheric scattering" test klibinde:
   gölge Ay gibi mutlak siyah mı çıktı, yoksa yumuşak mı: __
   ⛔ Mutlak siyahsa ışık cümlesi güçlendirilir — Mars'ta saçılma VARDIR [F1-d].
⑬ MAKİNE TESTİ (bu filme özel)
   "sealed robotic unit with no cab, no window, no seat and no handrail" test klibinde
   kabin · cam · basamak · operatör çıktı mı: __/5   [DERS 41]

KARAR           bu araçla üretilir / üretilmez — sebep
```

## 0b. ÖN GÖRSELLEŞTİRME VE YAKIN REFERANSLAR — usta kareden ÖNCE

```
PLAN + YAN KESİT  istasyon (+6,0 m) · sığınak ekseni (95 m) · tepecik (70 m · 16,0 m) ·
                  direk (110 m · 18,0 m) · panel şeridi (130 m) · uzak sırt (2.500 m · 40 m)
ÇİZİLDİ Mİ        evet/hayır · dosya: ____
⭐ ÇİZGİ KONTROLÜ  tepe tacı G0'da uzak sırtın kaç puan üstünde: ____ (plan 15,3 diyor)
                  G22'de kaç puan altında: ____ (plan 6,7 diyor)
⭐ YAKIN REFERANS  geniş kareden 2,0× kırpılarak DENETLENİR [plan §KURGU 3]:
   N0   S0 kesiti — kepçe + açılan bant      ölçülen ____ px  (hedef ≥ 90)
   N14  S14 ilk teması — araç + yayılan malzeme  ölçülen ____ px  (hedef ≥ 140)
   N23  S23 portalı — kapı ____ px / pencere ____ px  (hedef ≥ 90 / ≥ 35)
   ⛔ Tutmuyorsa YERLEŞİM düzeltilir (nesne yaklaştırılır), büyütme ARTIRILMAZ.
GÜNEŞ             06:20 az 72° → 19:30 az 270° kadraj dışında mı (bakış kuzey): ✓/✗
```

## 0c. ⭐ ÜÇ DENEME — 49 istem yazılmadan ÖNCE [P4-h]

```
DENEME 1 · İLK KAZI      tabaka RENK FARKI okundu mu __ · kepçe ölçeği doğru mu __ ·
                          tepe silueti bozulmadan durdu mu __        SONUÇ: ____
DENEME 2 · İLK ÖRTÜLEME  malzeme KABUĞUN ÜSTÜNDE kaldı mı __ · kemer biçimi görünür mü __ ·
                          "toprak nereden geldi" okundu mu __        SONUÇ: ____
DENEME 3 · PENCERE       2,0×'te pencere ____ px · dönüşte kayma ____ px (≤4) ·
                          ışık yandıktan sonra SÖNMEDİ mi __         SONUÇ: ____
⛔ Üçü de olumlu değilse PLAN DÜZELTİLİR, istem yazılmaz.
```

## 1. USTA KARE

```
KARE    G24 (S23'ün HEDEF karesi · sahne değil)      ARAÇ [model + ayar]      SEED ____
PROMPT  birebir plandan / değiştirildi: [ne, neden]
KAPI    sığınak 1 · direk 1 · tank 2 · tepe 1 · tepe tacı %44,9 · uzak sırt %51,6 ·
        tümsek kronu %51,9 · pencere YANIK ve huzmesiz · ocak tabanı DÜZ → geçti/düştü
FİNAL HİYERARŞİ  ① kapalı tümsek → ② yanık pencere → ③ eksilmiş tepe [QA_SPEC §1]
PİKSEL  tepe tacı y ____ · uzak sırt y ____ · pencere ____ px → plana ve SPEC §3'e yazıldı mı __
DOSYA   ____
```

## 2. GERİYE ZİNCİR — KARE başına TEK satır · G23 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = uzak krater sırtı + bazalt kümesi, elle ✓/✗ [DERS 25].
> ⛔ Her satırda TEPE YÜKSEKLİĞİ elle doğrulanır — bu filmin bedeli odur.

| G | araç + ayar | kaynak kare | master'dan ne KALDIRILDI / EKLENDİ | prompt birebir mi | zincir_kontrol | sırt + bazalt elle | sayım (üs·direk·tank·tepe) | ⭐ tepe h beklenen | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|:---:|---|
| 23 | | G24 | S23 (YANAR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 3,0 m · %44,9 | |
| 22 | | G23 | S22 (BOŞALIR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 3,0 m · %44,9 | |
| 21 | | G22 | S21 (ÖRTER)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 10,3 m · %57,3 | |
| 20 | | G21 | S20 (YÜKSELTİR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 10,4 m · %57,4 | |
| 19 | | G20 | S19 (SİLER)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 10,5 m · %57,6 | |
| 18 | | G19 | S18 (KARARIR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 10,5 m · %57,6 | |
| 17 | | G18 | S17 (KURAR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 10,7 m · %57,9 | |
| 16 | | G17 | S16 (KIRAĞI ÇEKİLİR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 10,8 m · %58,1 | |
| 15 | | G16 | S15 (DONAR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 10,9 m · %58,3 | |
| 14 | | G15 | S14 (ÖRTER)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 12,4 m · %60,9 | |
| 13 | | G14 | S13 (KAPATIR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 12,5 m · %61,0 | |
| 12 | | G13 | S12 (KAPLAR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 12,6 m · %61,2 | |
| 11 | | G12 | S11 (TAMAMLAR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 12,7 m · %61,4 | |
| 10 | | G11 | S10 (KALDIRIR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 12,9 m · %61,7 | |
| 9 | | G10 | S9 (PİŞİRİR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 13,0 m · %61,9 | |
| 8 | | G9 | S8 (BASAMAKLAR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 13,2 m · %62,3 | |
| 7 | | G8 | S7 (KAZAR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 13,4 m · %62,6 | |
| 6 | | G7 | S6 (DİKER)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 13,7 m · %63,1 | |
| 5 | | G6 | S5 (DİZER)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 14,1 m · %63,6 | |
| 4 | | G5 | S4 (DÜZLER)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 14,5 m · %64,3 | |
| 3 | | G4 | S3 (SIKIŞTIRIR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 14,8 m · %64,9 | |
| 2 | | G3 | S2 (SIYIRIR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 15,3 m · %65,8 | |
| 1 | | G2 | S1 (TAŞIR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 15,7 m · %66,4 | |
| 0 | | G1 | S0 (AÇAR)'in işi GERİ ALINIR | | geçti/düştü | ✓/✗ | 1·1·2·1 | 16,0 m · %66,9 | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTI boş kalır — kare atılır, yeniden türetilir.
⛔ G19 → G18 editinde TEPE DEĞİŞMEZ (fırtına) — iki kare aynı yükseklikte olmalı.
⭐ G1 → G0 filmin tek "yarayı kapatma" editidir: G0'da tepe BÜTÜN, kepçe yalnız dayalı.
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn → 11,0 sn üret, BAŞTAN kırp [A7-b].

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef | prompt birebir mi | ffprobe | kırpma | teslim | yüzey kanıtı | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|---|
| 0 | | B | G0 | G1 — ⭐ kesik İLK SANİYEDE açıldı mı ✓/✗ | geçti/düştü | | | | 10,0 | | |
| 1 | | A | G1 | G2 | geçti/düştü | | | | 10,0 | | |
| 2 | | B | G2 | G3 | geçti/düştü | | | | 10,0 | | |
| 3 | | A | G3 | G4 | geçti/düştü | | | | 10,0 | | |
| 4 | | A | G4 | G5 | geçti/düştü | | | | 10,0 | | |
| 5 | | A | G5 | G6 | geçti/düştü | | | | 10,0 | | |
| 6 | | A | G6 | G7 | geçti/düştü | | | | 10,0 | | |
| 7 | | B | G7 | G8 | geçti/düştü | | | | 10,0 | | |
| 8 | | A | G8 | G9 | geçti/düştü | | | | 10,0 | | |
| 9 | | A | G9 | G10 | geçti/düştü | | | | 10,0 | | |
| 10 | | A | G10 | G11 | geçti/düştü | | | | 10,0 | | |
| 11 | | A | G11 | G12 | geçti/düştü | | | | 10,0 | | |
| 12 | | A | G12 | G13 | geçti/düştü | | | | 10,0 | | |
| 13 | | A | G13 | G14 | geçti/düştü | | | | 10,0 | | |
| 14 | | B | G14 | G15 — ⭐ toprak KABUĞUN ÜSTÜNDE kaldı mı ✓/✗ | geçti/düştü | | | | 10,0 | | |
| 15 | | A | G15 | G16 | geçti/düştü | | | | 10,0 | | |
| 16 | | A | G16 | G17 | geçti/düştü | | | | 10,0 | | |
| 17 | | A | G17 | G18 | geçti/düştü | | | | 10,0 | | |
| 18 | | A | G18 | G19 — ⛔ tepe DEĞİŞMEDİ mi ✓/✗ | geçti/düştü | | | | 10,0 | | |
| 19 | | A | G19 | G20 | geçti/düştü | | | | 10,0 | | |
| 20 | | A | G20 | G21 | geçti/düştü | | | | 10,0 | | |
| 21 | | B | G21 | G22 — ⭐ tepe sırt çizgisini geçti mi ✓/✗ | geçti/düştü | | | | 10,0 | | |
| 22 | | A | G22 | G23 | geçti/düştü | | | | 10,0 | | |
| 23 | | A | G23 | G24 — ⭐ ışık 5,0 sn'de yandı mı ✓/✗ | geçti/düştü | | | | 10,0 | | |

## 4. ⭐ KURGU YAKINLAŞMASI — üç an, ölçülerek

```
KAYNAK ÇÖZÜNÜRLÜK  ____ × ____ px  →  izinli tavan ____×   (§0 ⑪'den)
S0   büyütme ____× (plan 2,0) · anahtar kareler ____ · dönüşte sırt kayması ____ px (≤4)
S14  büyütme ____× (plan 1,8) · anahtar kareler ____ · dönüşte sırt kayması ____ px (≤4)
S23  büyütme ____× (plan 2,0) · ışık ____ sn'de yandı (plan 5,0) · dönüş 6,5–8,5 ·
     8,5–10,0 tam MAIN STATION · sırt kayması ____ px (≤4)
⛔ S21'de HAREKET YOK — kontrol edildi mi: __
İLERİ DURUM  üç klipte de dönüşte iş geri alınmadı mı ✓/✗
⭐ DEPONUN ÜÇÜNCÜ YAKINLAŞMA ÖLÇÜMÜ (NARROW GORGE · LAST CIRCLE · bu film).
   Sonuç DERSLER.md'ye yazılır.
```

## 5. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM §6]

```
① BİÇİM     ffprobe → ____   (1920,1080,30/1,h264)
② SÜRE      ffprobe format=duration → ____ sn   (240,0 · kart YOK)
③ KESME     bash araclar/kesme_kontrol.sh teslim.mp4 <PLAN> → __
            beklenen 23 kesme: 10,0 · 20,0 · … · 230,0
            ("PLANIN KENDİSİ DÜZ" uyarısı BEKLENİR — formatın bandı)
④ SES       ebur128 → I ____ LUFS · Peak ____ dBFS · BPM 120
⑤ AÇILIŞ    0,0–1,5 müziksiz pencere (yalnız kepçe sesi) plana uydu mu: __
⑥ FLICKER   signalstats YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL     ffmpeg -ss 238.0 → SPEC §1 üçlüsü görünüyor mu: __
            KAPAK KANITI zincir_kontrol.sh g24_kaynak.jpg kapak.png → __
⭐ ① KOŞUSUNDA AYRICA: 16:9 güvenli alan bantları ÖLÇÜLÜR ve §2.8'e yazılır
   (deponun ilk 16:9 ölçümü) — üst ____ px · alt ____ px · sağ üst ____ × ____ px
```

## 6. PLANDAN SAPMALAR

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
17.09.2026 — plan, uzman okumasının (P4) sekiz düzeltmesi UYGULANARAK yazıldı; sapma
             değil, ilk sürümün kendisi budur. Ayrıntı: plan §ELEŞTİRİ TURU.
17.09.2026 — yazım sırasında fiil/kare hizalaması bir kaydırma düzeltildi: G kareleri
             sahnenin BAŞLANGIÇ durumunu gösterir, fiil o klibin işini adlandırır.
             İki fiil değişti (İŞARETLER → DÜZLER, GÖMER → YÜKSELTİR).
17.09.2026 — "crane" kelimesi 25 promptun tamamından KALDIRILDI: kelime negatif bloğun
             yüzey listesinde geçtiği için DERS 8 kanca kapısı her karede açılıyordu ve
             robotik sahada kanca riski alınmadı. Kaldırma makinesi "lifting rig"tir ve
             yükü iki gergin sapanla bom başında tutar [DERS 57].
```
