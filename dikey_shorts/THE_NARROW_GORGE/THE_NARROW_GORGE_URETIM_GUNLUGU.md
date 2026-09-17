# 🗒️ THE NARROW GORGE — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · bu günlüğe tek satır yazılmadı · (16.09.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28 — dört filmde ölçüldü]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`. Plan: `THE_NARROW_GORGE_DIKEY_TIMELAPSE.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 7 sahne = 8 kare (G0…G7) + 7 I2V · ara kare YOK · KAPAK KARTI YOK.
> Izgara: ⛔ DÜZ 7 × 8,0 = 56,0 sn (sahip kilidi; ⑥ METRONOM beklenen risk).
> ⭐ Bu film deponun İLK KURGU YAKINLAŞMASI denemesidir (sahip kararı) — §5'te ayrı bölüm.

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32 · A7-d]

> Yordam ve test promptu: `kilavuzlar/ARAC_KARTLARI.md` §4-§5. Kart doldurulmadan tek kare üretilmez.

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne: 8,0 (yedisi de)
   ⛔ tavan < 8,0 ise ARA KARE YOK: araç değişir ya da karar proje sahibine döner.
   KARAR         ____
② KAMERA        ilk/son kare kayması: ____ px    (>2 px ise ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5   (plan promptları 5.771–5.936 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
⑨ ÇÖZÜNÜRLÜK    ⭐ BU FİLMİN İKİNCİ FORMAT KAPISI — kurgu yakınlaşması buna bağlı
   [genel yordam: ARAC_KARTLARI §4 ÖLÇÜM 9 · sayılar: KAMERA_HAREKETI_KILAVUZU §3.3]
   araç dikey çıktısı: ____ × ____ px
   ⛔ 2160 × 3840 ve üstü → plandaki tablo aynen geçerli (S1 ve S6'da 2,0×)
   ⛔ 1836 × 3264 → tavan 1,7× · 1674 × 2976 → tavan 1,55× · 1080 × 1920 → YAKINLAŞMA YOK
   BÜYÜTME SAYILMAZ (upscale ile "2,0× sağlandı" yazılmaz)
   KARAR         yakınlaşma tavanı ____× · plan §KURGU tablosu güncellendi mi: __
⑩ KAPAK TESTİ   (bu filme özel) "a single steel radial gate, closed and dry against the concrete lip"
                test klibinde kapak KAPALI ve KURU kalıyor mu, yoksa model savaktan su akıtıyor mu: __
                — akıtıyorsa G5 ve G6 yeniden yazılır [DERS 56]
⑪ TABAKA TESTİ  (bu filme özel) "a white sheet crosses the lip and falls the full height of the face"
                test klibinde tabaka DUDAKTAN mı iniyor yoksa kayadan şelale mi oluyor · serpinti
                kadrajın alt yarısını kaplıyor mu: __ — kaplıyorsa S6 yeniden yazılır [DERS 42]
⑫ KURU YATAK    (bu filme özel) "bare pale gravel with a silt crust" test klibinde kuru yatak ıslak
                okunuyor mu: __ — okunuyorsa G2–G6 dokusu yeniden yazılır [DERS 54]
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 0b. ÖN GÖRSELLEŞTİRME — usta kareden ÖNCE

```
PLAN + BOY KESİT  kaya sekisi (+25) · köprü (60 m, +6) · portal (45 m, +3) · baraj ekseni (94 m) ·
                  kret (+70) · savak dudağı (+67,5) · dip savak (+4) · enerji kırıcı havuz ·
                  iki duvar (+80) ve kaya bandı (+40)
ÇİZİLDİ Mİ        evet/hayır · dosya: ____
SU COĞRAFYASI     üç sistem ayrı ayrı çizildi mi (geçici tünel ÇIKIŞI köprünün AŞAĞISINDA ·
                  dip savak gövde dibinde · kapaklı dolusavak krette): ✓/✗
GÜNEŞ             05:30 az 67° → 19:30 az 302° kadraj dışında mı (kadraj az 337°–23°): ✓/✗
KADRAJ            köprü ≈250 px çıkıyor mu · kret %81,9'a oturuyor mu · gök yarığı %89'da mı: ✓/✗
```

## 1. USTA KARE

```
KARE    G7 (son klibin HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]         ÇÖZÜNÜRLÜK  ____ × ____ (≥ 2160 × 3840 hedef)
PROMPT  birebir plandan / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    kapak AÇIK · dudaktan inen beyaz tabaka · serpinti ALÇAK ve köprüyü örtmüyor · gövde temiz
        (kalıp/trestle/makine yok, ankraj izleri var) · köprü altında ölçülü akış · iki yanda KURU çakıl
        ve söğüt kütükleri · değirmen arkı KURU · köprü ≈250 px · kret %81,9 → geçti/düştü
FİNAL HİYERARŞİ  ① inen beyaz tabaka → ② tam beton gövde → ③ köprü + ölçülü akış [P1-h]
SAYIM   baraj ____ (1) · köprü ____ (1) · kapak ____ (1) · portal ____ (1)
PİKSEL  köprü en ____ px · tabliye y ____ · kret y ____ · dudak y ____ · kaya bandı y ____ ·
        gök yarığı y ____ → plana ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G6 → G5 → G4 → G3 → G2 → G1 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = KÖPRÜ + KAYA BANDI + KAYA BURNU, elle ✓/✗ [DERS 25].

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi | zincir_kontrol | köprü + bant + burun elle | sayım (1·1·1·1) | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|:---:|---|
| 6 | | G7 | kapak KAPATILIR, tabaka ve serpinti kalkar, dudak kurur · köprü altındaki akış incelir (yalnız dip savak) · ışık 17:30 | | geçti/düştü | ✓/✗ | | ✓/✗ | |
| 5 | | G6 | dip savak KAPANIR · portal yeniden AKAR · kaya dolgu kapanışı GERİ · üst katlara kalıp GERİ · trestle + konveyör GERİ · panel istifi · 15:30 | | | | | | |
| 4 | | G5 | kret + dudak + iki ayak + KAPAK kaldırılır → gövde %50,7'ye iner · üstte kalıp katı · kür örtüleri · 13:30 | | | | | | |
| 3 | | G4 | bütün beton katlar kaldırılır → temiz kaya temel + basamaklı mesnetler + tesviye betonu · trestle kaldırılır · KURU havuz çukuru · 11:30 | | | | | | |
| 2 | | G3 | temel ve mesnetler kapanır → kuru çakıl yatak · söğüt kütükleri ve bariyerler GERİ · pompalar + göletler GERİ · 09:30 | | | | | | |
| 1 | | G2 | kapanış kaldırılır → ırmak yatağa GERİ (bulanık) · portal çentiğe iner · değirmen arkı AKAR · ıslak/kuru sınırı yok · 07:30 | | | | | | |
| 0 | | G1 | yol yarıma iner · söğütler GERİ (yapraklı) · ırmak berraklaşır · kırıcı platformda, tool kayada, ilk yara açık · 05:30 | | | | | | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o kare atılır [DERS 12 · 25].
⚠️ G1 → G0 filmin tek "GERİ KOYMA" editidir (söğüt + berrak su). Bedelin kanıtı G0 ↔ G7 çiftidir (SPEC §1).
⚠️ G5 → G4 kapak editidir: KAPAK KALDIRILIR (S4'te yerleşir). G4'te savak dudağı da YOKTUR.
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kırpma BAŞTAN [§2.7 ③]. Rejim hepsinde B.
> ⛔ KLİPLER HOME KADRAJINDA VE TAM ÇÖZÜNÜRLÜKTE üretilir; yakınlaşma KURGUDA (§5).

| S | araç + ayar | çözünürlük | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | su kanıtı ✓/✗ | dosya |
|:-:|---|---|---|---|:---:|---|---:|---|---:|:---:|:---:|---|
| 0 | | | G0 | G1 | geçti/düştü | | | | 8,0 | | ırmak berrak → bulanık ✓/✗ | |
| 1 | | | G1 | G2 | | | | | 8,0 | | ⭐ ıslak/kuru sınırı köprü kemerinden geçti ✓/✗ | |
| 2 | | | G2 | G3 | | | | | 8,0 | | yatak KURU kaldı ✓/✗ | |
| 3 | | | G3 | G4 | | | | | 8,0 | | beton %50 göz çizgisini geçti ✓/✗ | |
| 4 | | | G4 | G5 — ⚠️ klip ortasında bulut gölgesi soldan sağa geçti mi ✓/✗ | | | | | 8,0 | | kapak KAPALI ve KURU ✓/✗ | |
| 5 | | | G5 | G6 | | | | | 8,0 | | portal kesildi → dip savak açıldı (SIRA) ✓/✗ | |
| 6 | | | G6 | G7 (usta kare) | | | | | 8,0 | | tabaka dudaktan indi · serpinti alçak ✓/✗ | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6]

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____   (1080,1920,30/1,h264)
② SÜRE          ffprobe format=duration → ____ sn   (56,0 · KART YOK)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 dikey_shorts/THE_NARROW_GORGE/THE_NARROW_GORGE_DIKEY_TIMELAPSE.md → çıkış: __
                beklenen kesmeler 8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0
                ("PLANIN KENDİSİ DÜZ" uyarısı beklenir — kabul edilmiş risk)
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        müziksiz pencere 0,0–2,0 (ırmak + tek çelik darbe) plana uygun mu: evet/hayır ·
                40,0–45,0 yalnız drone: __
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF → kesme dışında sıçrama: evet/hayır
                ⚠️ YAKINLAŞMA KLİPLERİNDE YDIF doğal olarak yükselir — S0 · S1 · S3 · S6'da eşik ayrı okunur
⑦ FİNAL + KAPAK ffmpeg -ss 55.0 -i teslim.mp4 -frames:v 1 kanit.jpg → SPEC §1 üçlüsü görünüyor mu: __
                KAPAK KAYNAĞI ffmpeg -ss 55.0 -i teslim.mp4 -frames:v 1 g7_kaynak.jpg
                              ffmpeg -ss 00.2 -i teslim.mp4 -frames:v 1 g0_kaynak.jpg
                KAPAK KANITI  zincir_kontrol.sh g7_kaynak.jpg kapak_alt_bant.png → __
                              zincir_kontrol.sh g0_kaynak.jpg kapak_ust_bant.png → __
```

## 5. ⭐ KURGU YAKINLAŞMASI — deponun İLK denemesi (sahip kararı, ÖLÇÜLMEDİ)

> Plan §KURGU'daki tablo burada ÖLÇÜLEREK doldurulur. Bu bölüm boşsa film teslim edilmez.

| S | planlanan | uygulanan tepe ölçek | kaynak çözünürlük | HOME dönüşü (çapa sapması px) | ileri durum korundu mu | kırpma taştı mı | not |
|:-:|---|---:|---|---:|:---:|:---:|---|
| 0 | 1,55× | | | | ✓/✗ | ✓/✗ | |
| 1 | 2,0× | | | | ✓/✗ | ✓/✗ | ⭐ köprü kemerinin altı |
| 2 | sabit | 1,0× | | 0 | — | — | |
| 3 | 1,7× | | | | ✓/✗ | ✓/✗ | |
| 4 | sabit | 1,0× | | 0 | — | — | |
| 5 | sabit | 1,0× | | 0 | — | — | |
| 6 | 2,0× | | | | ✓/✗ | ✓/✗ | ⭐ dudak + kapak · iki aşamalı sonuç |

```
⛔ HOME DÖNÜŞÜ KAPISI: her yakınlaşmalı klibin SON karesinde çapalar HOME piksellerinde olmalı
   (köprü ≈250 px · kret %81,9). Sapma > 4 px ise kurgu düzeltilir.
⛔ İLERİ DURUM KAPISI: dönüşte inşaat geri alınmış mı — alınmışsa klip TERS OYNATILMIŞTIR, TESLİM YOK.
⛔ RİTİM KAPISI: dört yakınlaşmanın hız eğrileri birbirinin aynısı olmamalı.
⭐ YAYIN SONRASI ÖLÇÜM: bu film, sabit kadrajlı filmlerle KARŞILAŞTIRILIR (ortalama izlenme yüzdesi ·
   ortalama izlenme süresi · izlemeye devam edenler). Sonuç DERSLER'e "yakınlaşma ölçümü" olarak yazılır;
   hüküm çıkmadan kılavuza kural yazılmaz [DERS 12].
```

## 6. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]

16.09.2026 · plan · KAPAK KARTI KALDIRILDI (61,0 → 56,0 sn) · proje sahibinin kararı: bitmiş hikâyenin
             ardına hareketsiz afiş konmuyor, son 2 sn akan suyla tutuluyor · plana yazıldı
16.09.2026 · plan · BEDEL yeniden kuruldu: "altından ırmak geçmeyen köprü" çelişkiliydi; bedel artık
             denetime alınan akış + kaybolan söğütlü kıyı + kuru değirmen arkı · plana yazıldı
16.09.2026 · plan · SU COĞRAFYASI üç ayrı sisteme bölündü (geçici tünel ÇIKIŞI köprünün aşağısında ·
             dip savak · kapaklı dolusavak) · eleştiri ③ · plana ayrı kutu olarak yazıldı
16.09.2026 · S3 · ilerleme kanıtı "köprü tabliyesi hizası"ndan GÖZ ÇİZGİSİNE (%50) taşındı · eski kanıt
             kadrajda gerçekleşmiyordu (baraj tabanı %32,3 > köprü %28,9) · plana ve SPEC §2'ye yazıldı
16.09.2026 · S4/S6 · kapaksız çentik yerine TEK RADYAL KAPAK: S4'te yerleşir, S6'da açılır · "kendiliğinden
             taşma" ve "son birkaç santim iki saatte dolar" iddiaları kaldırıldı · referans karelere işlendi
16.09.2026 · S6 · final "ilk kontrollü salım" oldu; hazne dolumu S5 → S6 KESMESİNDE geçiyor · plana yazıldı
16.09.2026 · ışık · 19:30'da krette doğrudan altın ışık İSTENMİYOR (güneş rimin arkasında, mavi saat) · plana yazıldı
16.09.2026 · kurgu · dört sahneye KURGU YAKINLAŞMASI eklendi (sahip kararı) · §1.2 ve P2-l ② geçersiz
             kılındı · ölçülmedi · plan §KURGU + SPEC §7 + bu günlüğün §5'i açıldı
```
