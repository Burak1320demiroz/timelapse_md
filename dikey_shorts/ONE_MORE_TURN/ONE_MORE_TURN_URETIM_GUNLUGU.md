# 🗒️ ONE MORE TURN — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · (18.09.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md` · Plan: `ONE_MORE_TURN_DIKEY_TIMELAPSE.md`
> Format: 6 sahne = 7 kare (G0…G6) + 6 I2V · her sahne tek 8,0 sn klip.
> Izgara: ⛔ DÜZ 6 × 8,0 = 48,0 sn — proje sahibinin kesin kuralı; ⑥ METRONOM beyanlı risk.
> ⭐ S4–S5 REJİM G (gerçek zaman 1×) — depoda ilk; ⑭ ⑮ ⑯ bu filme özel kapılardır.

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32]

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne 8,0
   ⛔ tavan < 8,0 ise bu araçta üretilmez; karar sahibine döner:   KARAR ____
② KAMERA        ilk/son kare kayması: ____ px    (>2 px ise ÜRETİLMEZ)
③ GÖLGE         ilk/son kare açı farkı: ____°    (rejim B test klibinde 0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5
⑤ PROMPT TAVANI ____ karakter · son nesne göründü mü: __/5  (plan promptları 5.657–5.968 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol: ____

⭐ ⑨ SAYIM TESTİ [DERS 55]
   Test promptuna plandaki sayım cümlesi birebir konur. Beş klipte:
   kaç çark / kaç oluk çıktı: __/__/__/__/__      hedef: hepsinde 1 / 1
   G1 test karesinde ÇIPLAK göbeğe hayalet kol kondu mu: __
   ⛔ Herhangi bir klipte 2+ çark çıkarsa ARAÇ DEĞİŞİR, plan düşürülmez.
   KARAR         ____

⑩ ÇÖZÜNÜRLÜK    bu filmde UYGULANMAZ — kurgu hareketi yok, kırpma yok [plan §KURGU]

⑪ SEHPA TESTİ (bu filme özel)
   "a shear-legs hoist of two timber poles ... its rope carrying one curved rim segment in a
   sling" test klibinde: sehpa mı okundu, VİNÇ mi çıktı (kabin, bom, paletler): __
   — vinç çıkıyorsa DERS 8 tetiklenmiştir; sehpa cümlesi güçlendirilir, kelime değişmez
⑫ SÖKÜM TESTİ (bu filme özel)
   S0 test klibinde eski kol/halka/kova tek tek halatla İNDİ mi, yoksa SOLDU mu: __
   — soluyorsa (opacity fade) I2V "piece by piece on the hoist rope" cümlesi öne alınır
⑬ DEFTER TESTİ (bu filme özel)
   römork test klibinde yükü BÜYÜDÜ mü (S0) / GİTTİ-DÖNDÜ mü (S1) / ÇIKTI mı (S3): __
   — römork ışınlanıyorsa S1 klibinde gidiş-dönüş iki ayrı cümleye bölünür

⭐ ⑭ SU TESTİ — rejim G'nin birinci kapısı (bu filme özel, ölçülmemiş)
   "moves at natural speed ... the sluice board rises ... water runs the length of the flume
   and pours from the spout into the buckets" test klibinde:
   su cephesi oluğu KOŞTU mu (birden dolmadı): __ · ağızdan kovaya düştü mü: __
   dere DALGALI mı (ipek değil): __ · gölge sabit mi: __
   — üçünden biri düşerse rejim G bu araçta yok; S4–S5 için karar sahibine döner
⭐ ⑮ SABİT ÇARK TESTİ (bu filme özel)
   S3 test klibi: tam çark 2 sa süpürme altında (halat bağı yazılı) DÖNDÜ mü: __
   — dönüyorsa bağ cümlesi öne alınır; yine dönüyorsa G3 yerleşimi sorgulanır
⭐ ⑯ RİJİT DÖNÜŞ TESTİ (bu filme özel)
   S5 test klibi: 0 · 4 · 8 sn'de kol __/__/__ (8) · halka daire mi __ · kovalar __/__/__ (24)
   işaretli kol açısı: 0 sn ____° · 4 sn ____° · 8 sn ____°   (hedef 360° ± 30°, saat tersi)
   ⛔ durgun klip (< 60°) ya da yumurta halka = bu araçta rejim G dönüşü YOK; karar sahibine

KARAR           bu araçla üretilir / üretilmez — sebep
```

## 0b. ÖN GÖRSELLEŞTİRME — usta kareden ÖNCE

```
PLAN + YAN KESİT  istasyon (+2,0 m · karşı kıyı) · mil (9,0 m · +2,6) · duvar (9,5 m) ·
                  oluk (+5,5 · soldan) · kapak (x −3,2) · çıkrık (x −2,9) · römork (8,5 m ·
                  sol kenar) · kaya (6,5 m) · üç basamak · çıkış oluğu
ÇİZİLDİ Mİ        evet/hayır · dosya: ____
⭐ KANIT KUTUSU    çark %13–79 × %36–73 kutunun (x %11–78 · y %25–87) içinde mi: __
⭐ ÇIKIŞ OLUĞU     %28–36 bandında, alt 484 px'in üstünde mi: __
⭐ SU KAPAĞI       %7,9'da sol bandın içinde — oluktaki su cephesi %8–30'da OKUNUYOR mu: __
GÜNEŞ             10:10 az 133° → 18:10 az 280° kadraj dışında mı (kadraj az 7°–53°): ✓/✗
```

## 1. USTA KARE

```
KARE    G6 (S5'in HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne, neden]
SEED    [varsa]
KAPI    çark 1 · göbek 1 · oluk 1 · kol 8 · halka 2 · kova 24 · sol yarı ISLAK · sağ yarı kuru ·
        işaretli kol saat 11 · çıkış oluğu beyaz · figür sırtı dönük, bir adım geri ·
        mil %46,1/%54,4 · ufuk %50 → geçti/düştü
FİNAL HİYERARŞİ  ① dönen çark → ② ağızdan kovaya su → ③ beyaz çıkış oluğu [SPEC §1]
PİKSEL  mil x ____ y ____ · duvar köşesi x ____ · çark çapı ____ px · figür ____ px
        → plana ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 2. GERİYE ZİNCİR — KARE başına TEK satır · G5 → G4 → G3 → G2 → G1 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = demir göbek + duvar köşesi, elle ✓/✗ [DERS 25].

| G | araç + ayar | kaynak kare | master'dan ne KALDIRILDI / EKLENDİ | prompt birebir mi | zincir_kontrol | göbek + köşe elle | çark sayımı | ⭐ kol / halka / kova elle | işaretli kol | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|:---:|:---:|---|
| 5 | | G6 | ıslaklık sol yarıda 3 kovaya iner · çıkış oluğu → ilk sızıntı · figür çıkrığa, tek el · ⭐ işaretli kol 11'de KALIR | | geçti/düştü | ✓/✗ | 1 | 8 / 2 / 24 | 11 | |
| 4 | | G5 | kapak KAPANIR · oluk kurur · su ve ıslaklık kalkar · figür iki el · ⭐ işaretli kol 12'ye · ışık AYNI | | | | | 8 / 2 / 24 | 12 | |
| 3 | | G4 | oluk ESKİYE (birikinti, kırık tahta) · çıkış oluğu taşla dolar · halat bağı + iki dikme + sehpa (halat sarılı) + römork (3 tahta) eklenir · figür kalkar · ışık 16:10 | | | | | 8 / 2 / 24 | 12 | |
| 2 | | G3 | halkalar ve kovalar kaldırılır → 8 kollu yıldız · sehpada halka parçası · römork DOLU (16 parça + demet + 3 tahta) · ışık 14:10 | | | | | 8 / 0 / 0 | 12 | |
| 1 | | G2 | kollar kaldırılır → ÇIPLAK göbek · yatak ayağı YIKIK, taze harç kalkar · römork gri ahşap + sarmaşık · sehpada son kova tahtası · ışık 12:10 | | | | | 0 / 0 / 0 | — | |
| 0 | | G1 | ESKİ çark konur: 6 gri kol, üst-sol çeyreği açık halkalar, 18 kova, sarmaşık + gergin halat · sehpa kalkar · römork BOŞ · ışık 10:10 | | | | | 6 / 2 kırık / 18 | 12 | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTI boş kalır — kare atılır, yeniden türetilir.
⭐ G2 → G1 filmin en riskli editidir: göbek ÇIPLAK kalmalı. Model yuvalara kol koyuyorsa
   G1, G2'nin üstünden "eight empty sockets" öne alınarak tekrar denenir.
⭐ G1 → G0 "eskiyi geri koyma" editidir; yeni pale meşe ile eski gri ahşap karışmamalı.
⛔ Her karede TEK ÇARK sayılır [SPEC §6].
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn. Kırpma BAŞTAN [§2.7 ③].

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef | prompt birebir mi | ffprobe süre | kırpma | teslim | yüzey kanıtı | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|---|
| 0 | | B | G0 | G1 — ⛔ sarmaşık İLK SANİYEDE koptu mu ✓/✗ · parçalar İNDİ mi (solmadı) ✓/✗ | geçti/düştü | | | | 8,0 | | |
| 1 | | B | G1 | G2 — ⭐ römork GİTTİ-DÖNDÜ mü ✓/✗ · işaretli kol ÖNCE takıldı mı ✓/✗ | | | | | 8,0 | | |
| 2 | | B | G2 | G3 — ⭐ çember klip İÇİNDE kapandı mı ✓/✗ · bağ takıldı mı ✓/✗ | | | | | 8,0 | | |
| 3 | | B | G3 | G4 — ⭐ römork soldan ÇIKTI mı ✓/✗ · çark 2 sa süpürmede SABİT mi ✓/✗ | | | | | 8,0 | | |
| 4 | | **G** | G4 | G5 — ⭐ önce çıkrık+kapak, sonra su cephesi KOŞTU mu ✓/✗ · kol 12→11 ✓/✗ | | | | | 8,0 | | |
| 5 | | **G** | G5 | G6 (usta kare) — ⭐ 360° ± 30° ✓/✗ · rijit ✓/✗ · dönerken bitti mi ✓/✗ | | | | | 8,0 | | |

## 4. ⭐ REJİM G ÖLÇÜMÜ — S4 · S5, depoda ilk

```
GÖLGE            G4/G5/G6 duvar gölgesi açı farkı: ____° (hedef 0°)
DERE             S4 klibinde dere: dalgalı / ipek / karışık
İZ               motion streak ya da hayalet nesne: var/yok
FİGÜR            sırtı dönük kaldı mı: ✓/✗ · yüz okundu mu: ✓/✗
KAPAK HIZI       tahta 0,4 m'yi kaç saniyede aldı: ____ (plan 1,5)
SU CEPHESİ       oluğu %8 → %30 kaç saniyede koştu: ____ (plan 2,0)
DÖNÜŞ            S5 işaretli kol 0/4/8 sn: ____° / ____° / ____°
32,0 DİKİŞİ      ipek → dalga geçişi izlenebilir mi: ✓/✗ · rahatsız edici mi: ✓/✗
⭐ DEPONUN İLK GERÇEK ZAMAN ÖLÇÜMÜ. Sonuç DERSLER.md'ye ve SANTIYE_HAREKETI §1'e yazılır.
```

## 5. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM §6]

```
① BİÇİM         ffprobe → ____   (1080,1920,30/1,h264)
② SÜRE          ffprobe format=duration → ____ sn   (48,0 · kart YOK · logo YOK)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 <plan> → __
                beklenen kesmeler 8,0 · 16,0 · 24,0 · 32,0 · 40,0
                ("PLANIN KENDİSİ DÜZ" uyarısı BEKLENİR — sahip kuralı)
④ SES           ebur128 → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        0,0–2,0 müziksiz pencere (yalnız halat + kopma sesi): __
                30,0–32,0 müziksiz pencere (dikiş): __ · 34,0'ta müzik girdi mi: __
⑥ FLICKER       signalstats YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 46.0 → SPEC §1 üçlüsü görünüyor mu: __
                46,0 ↔ 47,0 işaretli kol açı farkı: ____° (≈ 45°)
                KAPAK KANITI zincir_kontrol.sh g6_kaynak.jpg kapak.png → __
```

## 6. PLANDAN SAPMALAR

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
18.09.2026 — plan, proje sahibinin yatay konseptinin (12 × 10 sn) sahip kararıyla
             6 × 8,0 dikeye çevrilmiş hâlidir; on bir sapma sohbette onaylandı ve plana
             §KONSEPT KAPISI altına yazıldı. Sapma değil, ilk sürümün kendisi budur.
```
