# 🗒️ THE LAST CIRCLE — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · (17.09.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md` · Plan: `THE_LAST_CIRCLE_DIKEY_TIMELAPSE.md`
> Format: 7 sahne = 8 kare (G0…G7) + 7 I2V · her sahne tek 8,0 sn klip.
> Izgara: ⛔ DÜZ 7 × 8,0 = 56,0 sn — proje sahibinin kesin kuralı; ⑥ METRONOM beyanlı risk.

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32]

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne 8,0
   ⛔ tavan < 8,0 ise bu araçta üretilmez; karar sahibine döner:   KARAR ____
② KAMERA        ilk/son kare kayması: ____ px    (>2 px ise ÜRETİLMEZ)
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5
⑤ PROMPT TAVANI ____ karakter · son nesne göründü mü: __/5  (plan promptları 5.607–5.951 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol: ____

⭐ ⑨ SAYIM TESTİ — BU FİLMİN BİRİNCİ RİSKİ [DERS 55]
   Test promptuna plandaki sayım cümlesi birebir konur. Beş klipte:
   kaç silindirik gövde çıktı: __/__/__/__/__      hedef: hepsinde 1
   elevatör muhafazası yuvarlak gövdeye döndü mü: __
   ⛔ Herhangi bir klipte 2+ gövde çıkarsa ARAÇ DEĞİŞİR, plan düşürülmez.
   KARAR         ____

⭐ ⑩ ÇÖZÜNÜRLÜK — S6'nın kurgu yakınlaşması buna bağlı
   [genel yordam: ARAC_KARTLARI §4 ÖLÇÜM 9 · sayılar: KAMERA_HAREKETI_KILAVUZU §3.3]
   ffprobe stream=width,height → ____ × ____ px
   ⛔ ≥ 2160 × 3840 → plandaki 2,0× aynen geçerli
   ⛔ 1836 × 3264 → tavan 1,7× · 1674 × 2976 → 1,55× · 1080 × 1920 → YAKINLAŞMA YOK
   BÜYÜTME SAYILMAZ.   KARAR: tavan ____× · plan §KURGU 3 güncellendi mi: __

⑪ KAYAR KALIP TESTİ (bu filme özel, ölçülmemiş)
   "a continuous ring of shutter panels clamped round the wall on its yokes, with jacks
   on the climbing rods" test klibinde: kalıp halka olarak mı okundu, yoksa iskele mi: __
   — iskele okunuyorsa S2–S5 promptları yeniden açılır (kalıp bu filmin dikey süpürmesidir)
⑫ BANT TESTİ (bu filme özel)
   şaftta taze/kürlenmiş renk bandı çıktı mı ve kalıbın ALTINDA mı: __
   — çıkmıyorsa ⑦ ters süpürme kaybolur; SITE TEXTURE bant cümlesi güçlendirilir
⑬ TAHIL TESTİ (bu filme özel)
   "a steady curtain of grain drops one full stream out of the trailer gate into the
   hopper mouth" test klibinde: akış perdesi okundu mu · kaynak ağzı göründü mü: __
   — okunmuyorsa G6/G7 yerleşimi düzeltilir, ikinci bir kamera hareketi EKLENMEZ

KARAR           bu araçla üretilir / üretilmez — sebep
```

## 0b. ÖN GÖRSELLEŞTİRME — usta kareden ÖNCE

```
PLAN + YAN KESİT  istasyon (+8,0 m) · silo ekseni (67 m) · harman dairesi (Ø22 m · 40–62 m)
                  · ahşap ambar (78 m · 6,5 m) · kavak hattı (90 m) · kabul hunisi
ÇİZİLDİ Mİ        evet/hayır · dosya: ____
⭐ AMBAR EŞİĞİ    silo hangi yükseklikte ambar mahyasını geçiyor: ____ m
                  (plan 6,7 m diyor → geçiş S2 klibinin İÇİNDE olmalı)
⭐ S6 YAKIN KADRAJ son açık yay ile kabul hunisi AYNI yakın kompozisyona sığıyor mu: __
                  ⛔ sığmıyorsa G6 yerleşimi düzeltilir [plan §KURGU 2]
GÜNEŞ             06:40 az 85° → 18:50 az 264° kadraj dışında mı (bakış kuzey): ✓/✗
```

## 1. USTA KARE

```
KARE    G7 (S6'nın HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne, neden]
SEED    [varsa]
KAPI    kule 1 · elevatör 1 · ambar 1 · daire YOK · yuvak apron kenarında ·
        huniye tahıl akıyor · taze panel koyu · taç %81,8 · ufuk %50 → geçti/düştü
FİNAL HİYERARŞİ  ① kule → ② akan tahıl → ③ kesintisiz apron + yuvak [SPEC §1]
PİKSEL  taç y ____ · ufuk y ____ · silo genişlik ____ px · yuvak ____ × ____ px
        → plana ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 2. GERİYE ZİNCİR — KARE başına TEK satır · G6 → G5 → G4 → G3 → G2 → G1 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = ahşap ambar + taş yuvak, elle ✓/✗ [DERS 25].

| G | araç + ayar | kaynak kare | master'dan ne KALDIRILDI / EKLENDİ | prompt birebir mi | zincir_kontrol | ambar + yuvak elle | kule sayımı | ⭐ daire yüzdesi elle | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|:---:|---|
| 6 | | G7 | taze panel kaldırılır → son 5 m'lik yay AÇILIR · tahıl akışı kaldırılır · mikser + screed rayı eklenir · ışık 16:50'ye | | geçti/düştü | ✓/✗ | 1 | 1 yay açık | |
| 5 | | G6 | apron uzak yarıya iner · ⭐ yuvak ORTAYA geri · başlık çeliği yarım · kalıp tepede + asılı iskele · mobil vinç | | | | | çeyrek açık | |
| 4 | | G5 | gövde 32 → 24 m · kalıp aşağı · elevatör muhafazası yarım · apron YOK · batching plant | | | | | çeyrek | |
| 3 | | G4 | gövde 24 → 9 m · elevatör muhafazası kaldırılır · malzeme asansörü kısalır | | | | | yarım | |
| 2 | | G3 | kalıp halkası sökülür → radye + starter bar · kalıp parçaları YERE yatar | | | | | üçte bir | |
| 1 | | G2 | radye kaldırılır → ham yay + spoil · şerit ipi | | | | | 6 m yay kırık | |
| 0 | | G1 | yay kapatılır → ⭐ DAİRE BÜTÜN · kova kenara dayalı · ışık 06:40 | | | | | BÜTÜN | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTI boş kalır — kare atılır, yeniden türetilir.
⭐ G1 → G0 filmin tek "bozulanı geri koyma" editidir. Daire G0'da BÜTÜN olmalı;
   model yayı kapatamıyorsa G0 sıfırdan değil, G1'in üstünden tekrar denenir.
⛔ Her karede TEK KULE sayılır [SPEC §6].
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn. Kırpma BAŞTAN [§2.7 ③].

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef | prompt birebir mi | ffprobe süre | kırpma | teslim | yüzey kanıtı | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|---|
| 0 | | A | G0 | G1 — ⛔ kenar İLK SANİYEDE kırıldı mı ✓/✗ | geçti/düştü | | | | 8,0 | | |
| 1 | | B | G1 | G2 | | | | | 8,0 | | |
| 2 | | B | G2 | G3 — ⭐ ambar eşiği klip İÇİNDE geçildi mi ✓/✗ | | | | | 8,0 | | |
| 3 | | B | G3 | G4 — ⭐ kür sınırı AŞAĞI indi mi ✓/✗ | | | | | 8,0 | | |
| 4 | | B | G4 | G5 | | | | | 8,0 | | |
| 5 | | B | G5 | G6 — ⭐ yuvağın taşınması GÖRÜNDÜ mü ✓/✗ | | | | | 8,0 | | |
| 6 | | B | G6 | G7 (usta kare) — ⭐ tahıl 5,0 sn'de başladı mı ✓/✗ | | | | | 8,0 | | |

## 4. ⭐ KURGU YAKINLAŞMASI — yalnız S6, ölçülerek

```
KAYNAK ÇÖZÜNÜRLÜK   ____ × ____ px   →  izinli tavan ____×   (§0 ⑩'dan)
UYGULANAN BÜYÜTME   ____×            (plan: 2,0×)
ANAHTAR KARELER     0,5 → 1,8 yaklaş · 1,8 → 5,0 tut · 6,0 → 7,0 dön · 7,0 → 8,0 HOME
YAKIN KADRAJ HEDEFİ x ____ · y ____ · genişlik ____ px   (G6 ÜRETİLDİKTEN SONRA)
HOME DÖNÜŞÜ         ambar mahyası kayması: ____ px   (≤ 4 px)
İLERİ DURUM         7,0–8,0'da yay örtülü ✓/✗ · tahıl akıyor ✓/✗ · panel taze ✓/✗
YAKIN ÇAPA          yuvak yakın kadrajda göründü mü: ✓/✗
KIRPMA SINIRI       boş kenar oluştu mu: ✓/✗
⭐ DEPONUN İKİNCİ YAKINLAŞMA ÖLÇÜMÜ. Sonuç DERSLER.md'ye yazılır.
```

## 5. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM §6]

```
① BİÇİM         ffprobe → ____   (1080,1920,30/1,h264)
② SÜRE          ffprobe format=duration → ____ sn   (56,0 · kart YOK)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 <plan> → __
                beklenen kesmeler 8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0
                ("PLANIN KENDİSİ DÜZ" uyarısı BEKLENİR — sahip kuralı)
④ SES           ebur128 → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        0,0–1,0 müziksiz pencere (yalnız kırılma sesi): __
⑥ FLICKER       signalstats YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 54.0 → SPEC §1 üçlüsü görünüyor mu: __
                KAPAK KANITI zincir_kontrol.sh g7_kaynak.jpg kapak.png → __
```

## 6. PLANDAN SAPMALAR

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
17.09.2026 — plan, uzman okumasının (P6) yedi düzeltmesi UYGULANARAK yazıldı;
             sapma değil, ilk sürümün kendisi budur. Ayrıntı: plan §ELEŞTİRİ TURU.
```
