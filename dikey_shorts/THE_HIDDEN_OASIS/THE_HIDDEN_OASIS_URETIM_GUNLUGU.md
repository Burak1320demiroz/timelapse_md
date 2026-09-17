# 🗒️ THE HIDDEN OASIS — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · bu günlüğe tek satır yazılmadı · (16.09.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28 — dört filmde ölçüldü]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
        ⛔ OVER THE WALL ve THE EMPTY RIDGE bu günlük BOŞKEN üretildi; ikisinde de QA arızayı adlandıramadı.
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`. Plan: `THE_HIDDEN_OASIS_DIKEY_TIMELAPSE.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 7 sahne = 8 kare (G0…G7) + 7 I2V · ara kare YOK, her sahne tek 8,0 sn klip [KILAVUZ_REHBERI §2.7].
> Izgara: ⛔ DÜZ 7 × 8,0 = 56,0 sn (proje sahibinin kilidi; ⑥ METRONOM beklenen risk — plan §AŞAMA MERDİVENİ).

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32 · A7-d]

> Yordam ve test promptu: `kilavuzlar/ARAC_KARTLARI.md` §4-§5. Kart doldurulmadan tek kare üretilmez.
> ⭐ Bu filmde ⑧ (iki kare) formatın kendisidir; almıyorsa araç değişir, plan düşürülmez.

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne: 8,0 (yedisi de)
   ⛔ tavan ≥ 8,0 (kutu ≥ 9,0) ise tek klip: üret <kutu>, baştan (kutu − 8,0) kırp [A7-b].
   ⛔ tavan < 8,0 ise ({4,6,8}) bu araçta sahne tek 8,0 sn klip olamaz — ARA KARE YOK:
      araç değişir ya da karar proje sahibine döner; karar buraya yazılır:
   KARAR         ____
② KAMERA        ilk/son kare kayması: ____ px    (>2 px ise ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5   (plan promptları 5.817–5.994 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
⑨ TILT TESTİ    (bu filme özel, ölçülmemiş) test klibinde kamera 40° AŞAĞI bakarken: dikey çizgiler (duvar,
                kapı, zeytin gövdesi) klip boyunca aynı eğimde mi kalıyor, yoksa model perspektifi
                "düzeltmeye" çalışıp kadrajı kaydırıyor mu: __  — kayıyorsa tilt azaltılır ve BÜTÜN
                yüzde tablosu (SPEC §2) yeniden hesaplanır
⑩ SU TESTİ      (bu filme özel) "the level climbs past the third boulder" test klibinde su seviyesi TEK YÖNDE
                mi yükseliyor, yüzey camgöbeği havuz suyuna mı kayıyor: __ — kayıyorsa G6/G7 ve S5 I2V
                yeniden yazılır (gölet suyu koyudur, rengini YANSIMADAN alır)
⑪ ASTAR TESTİ   (bu filme özel) "dry matte black liner, no sheen" test klibinde astar parlıyor mu: __
                — parlıyorsa G3–G5 yeniden yazılır (dolu okuma riski, DERS 54'ün tersi)
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 0b. ÖN GÖRSELLEŞTİRME — usta kareden ÖNCE

```
PLAN + YAN KESİT  balkon (+6,0) · avlu döşemesi · havuz (2,5 → 7,5 m, derinlik 1,0/1,4) · arka duvar (10,0 m, 2,6) +
                  niş · zeytin (5,5 m, 4,4) · teras yamacı (17,6 m'den öteye)
ÇİZİLDİ Mİ        evet/hayır · dosya: ____
TILT DOĞRULAMASI  tilt −40°'de alt kenar 1,40 m'ye, üst kenar 110 m'ye düşüyor mu · ufuk kadraj DIŞINDA mı: ✓/✗
GÜNEŞ             06:20 az 91° → 18:30 az 277° kadraj dışında mı (kadraj az 337°–23°): ✓/✗
```

## 1. USTA KARE

```
KARE    G7 (son klibin HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    altı fener YANIK ve ışık lambanın İÇİNDE · su üçüncü taşta · duran ayna + altı yansıma · çağlayan akıyor ·
        avlu BOŞ, kapı KAPALI, kapak taşı filtrede · merdiven/seramik/alet YOK · niş ≈99 × 134 px ·
        zeytin gövdesi x %9,2 · harpuşta %78,7 düz · üst 1/8 teras → geçti/düştü
FİNAL HİYERARŞİ  ① yanan su → ② taş kenar + dikili bant → ③ boş avlu — bu sırayla okunuyor mu [P1-h]
SAYIM   havuz ____ (1) · zeytin ____ (1) · niş ____ (1) · fener ____ (6)
PİKSEL  niş en ____ px · boy ____ px · x ____ · havuz uzak kenarı y ____ · harpuşta y ____ · zeytin gövdesi x ____
        → plana ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G6 → G5 → G4 → G3 → G2 → G1 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = NİŞ + ZEYTİN GÖVDESİ + HAVUZ SINIRI, elle ✓/✗ [DERS 25].
> ⛔ ARA KARE YOK: her sahne iki onaylı kare arasında tek 8,0 sn klip; tavan < 8,0 ise §0 KARAR satırı.

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi (değilse ne) | zincir_kontrol | niş + zeytin + havuz sınırı elle | sayım (1·1·1·6) | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|:---:|---|
| 6 | | G7 | fenerler SÖNDÜRÜLÜR · kapı AÇILIR · kapıya araba + sarılan hortum + iki streak · harpuştaya sıcak bant · kapak taşı yana · 18:20 | | geçti/düştü | ✓/✗ | | ✓/✗ | |
| 5 | | G6 | su BOŞALTILIR → kuru mat astar + pale çakıl · yansıma kalkar · çağlayan kurur · hortum uzak kenara ASILIR · kapıya saksı yüklü araba · gölgeler uzar · 16:20 | | | | | | |
| 4 | | G5 | bitkiler + malç + 6 fener KALDIRILIR → 8 açık toprak cebi · zeytin BUDANMAMIŞ tacına · harç teknesi + torbalar · kapıya son iki blok · 14:20 | | | | | | |
| 3 | | G4 | taş kenar + çağlayan + çakıl KALDIRILIR → çıplak astar · harpuştaya taş ağırlıklar GERİ · rulo göbekleri · lastik izleri silinir · 12:20 | | | | | | |
| 2 | | G3 | astar + keçe KALDIRILIR → temiz açık mavi seramik + harç izleri + 4 cıvata deliği · filtre kutusu ve boru kaldırılır · pompa + yıkayıcı GERİ · 10:20 | | | | | | |
| 1 | | G2 | temizlik GERİ ALINIR → siyah silt + yaprak matı + birikinti · merdiven GERİ · harç izleri kalkar · kapıya atık yığını · 08:20 | | | | | | |
| 0 | | G1 | su GERİ KONUR → koyu yeşil dolu havuz + yaprak salı · yosun bandı su üstüne iner · ikinci araba kalkar · doğu duvarı gölgesi tüm avluya · 06:20 | | | | | | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o kare atılır, yeniden
   türetilir, satır yeniden yazılır [DERS 12 · 25].
⚠️ G1 → G0 filmin tek "GERİ KOYMA" editidir (su). Model yeşil suyu başka tonda çizerse G0 atılmaz,
   ama G0'daki su rengi ve yosun bandının yüksekliği kayda geçer — bedelin kanıtı G0 ↔ G7 çiftidir (SPEC §1).
⚠️ G5 → G4 budama editidir: TAÇ değişir, GÖVDE değişmez. Gövde kaydıysa kare ATILIR.
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kırpma BAŞTAN [§2.7 ③]. Rejim: S0–S5 B, S6 A.

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | su/ışık ✓/✗ | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|:---:|---|
| 0 | | B | G0 | G1 | geçti/düştü | | | | 8,0 | | su TEK YÖNDE indi ✓/✗ | |
| 1 | | B | G1 | G2 | | | | | 8,0 | | temiz/kirli sınırı süpürdü ✓/✗ | |
| 2 | | B | G2 | G3 | | | | | 8,0 | | astar KURU kaldı ✓/✗ | |
| 3 | | B | G3 | G4 — ⚠️ ilk 2 sn'de BULUT GÖLGESİ soldan sağa geçti mi ✓/✗ | | | | | 8,0 | | — | |
| 4 | | B | G4 | G5 | | | | | 8,0 | | fenerler SÖNÜK kaldı ✓/✗ | |
| 5 | | B | G5 | G6 | | | | | 8,0 | | su TEK YÖNDE çıktı ✓/✗ | |
| 6 | | A | G6 | G7 (usta kare) | | | | | 8,0 | | huzme yok ✓/✗ | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6]

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____   (1080,1920,30/1,h264)
② SÜRE          ffprobe format=duration → ____ sn   (56,0 + 5,0 = 61,0)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 dikey_shorts/THE_HIDDEN_OASIS/THE_HIDDEN_OASIS_DIKEY_TIMELAPSE.md → çıkış: __
                beklenen kesmeler 8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0
                ("PLANIN KENDİSİ DÜZ" uyarısı beklenir — kabul edilmiş risk, çıkış kodunu değiştirmez)
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        müziksiz pencere 0,0–2,0 (duran su + ağustosböceği) plana uygun mu: evet/hayır ·
                18,0–20,0 yalnız kauçuk sesi: __
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 55.0 -i teslim.mp4 -frames:v 1 kanit.jpg → SPEC §1 üçlüsü görünüyor mu: __
                KAPAK KAYNAĞI ffmpeg -ss 55.0 -i teslim.mp4 -frames:v 1 g7_kaynak.jpg
                              ffmpeg -ss 00.2 -i teslim.mp4 -frames:v 1 g0_kaynak.jpg
                KAPAK KANITI  bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak_kart.png → __
                BÖLÜNMÜŞ KAPAK  g0_kaynak ↔ üst yarı: __ · g7_kaynak ↔ alt yarı: __
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]

16.09.2026 · plan · çatlak onarımı S2'den S1'in son 2 saniyesine alındı · S2'nin §9.5 bütçesi üç iş taşıyordu ·
             plana yazıldı (AŞAMA MERDİVENİ (c) + AJAN KARARLARI ③)
16.09.2026 · plan · kapak kartı EKLENDİ (dış plan kartsız 56,0 sn istiyordu) · format kuralı [§2.1 · DERS 4] ve
             prompt_kontrol.py kartsız planı BLOCK ediyor · plana yazıldı (TESLİM YAPISI + AJAN KARARLARI ①)
16.09.2026 · plan · rejim B×6 + A×1 seçildi · 1200×'te insan iz bırakır (referans havuz timelapse'lerinin görünümü),
             100× yalnız son sahnede · plana yazıldı (AJAN KARARLARI ②)
```
