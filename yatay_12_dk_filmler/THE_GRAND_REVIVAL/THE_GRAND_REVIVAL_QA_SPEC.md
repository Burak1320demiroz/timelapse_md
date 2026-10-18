# 🔍 THE_GRAND_REVIVAL — QA SPEC

> THE GRAND REVIVAL · 16:9 · 90 × 8,0 sn · 720,0 sn + 5,0 sn kart · müzik var · 9 istasyon. **Bu dosya yalnız belgeli
> merceklere verilir: ❹ İNŞA · ❺ TESLİM** (beş mercekli QA, 06.10.2026 [DERS 64]).
> ⛔ **❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❸ ŞANTİYE'ye VERİLMEZ** — üçü kör koşar, ayrı geçici sohbette, proje dışında
> [`QA_KOSU_KILAVUZU` §1]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit değildir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ QA birimi BÖLÜM: üç master (240 s) × 5 mercek = 15 ham rapor · `qa_paket.sh` henüz `--bolum 3` tanımıyor (PLAN §ÜRETİM ÖNCESİ).
> Ham raporlar `QA/HAM/THE_GRAND_REVIVAL/THE_GRAND_REVIVAL_B<n>_Q<n>_<AD>_HAM.md` · kayıt `QA/FILMLER/THE_GRAND_REVIVAL.md` · `QA/TABLO.md`.

---

## 0. KÜNYE

```
FİLM          THE_GRAND_REVIVAL — terk edilmiş ≈500 m² kireçtaşı villa oda oda yenilenir; ilk akşam yemeğiyle biter ·
              kuru tepe ülkesi · 9 sabit istasyon (sahip istisnası)
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_12_dk_filmler · HIZ 1x
KANARYA       lintelwren   ⛔ kör mercek raporunda bu kelime geçerse plan SIZMIŞTIR → koşu SIZINTI [QA_KOSU §3.1]

TESLİM YAPISI ⭐ SAHNE BLOĞU  90 sahne × 8,0 sn = 720,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  1 kart × 5,0 sn (720,0–725,0) · G90 + başlık "THE GRAND REVIVAL" · erime ≤ 1 sn ← QA DIŞI
                 TOPLAM                          725,0 sn
              ⛔ 725,0 sn'den uzun dosya = plan dışı siyah/kart → ❺ "the plan declares ONE 5,0 s card — report extra"
              ⛔ BOLUM_3 masterı kartı İÇERMEZ (480,0–720,0); kart yalnız tam master'da ölçülür

SAHNE SAATLERİ  sahne n = n × 8,0 → (n+1) × 8,0 · S0 0,0–8,0 · … · S89 712,0–720,0
                (120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · her kesme ölçü başında · 89 kesme)
PART GRID       BOLUM_1 = S0–S29 (0,0–240,0) · BOLUM_2 = S30–S59 (240,0–480,0) · BOLUM_3 = S60–S89 (480,0–720,0)
                kör merceğe tek satır: "THIS FILE IS PART n OF 3 — scenes S… — the film continues before/after"
⛔ DÜZ IZGARA   sahip seçimi (17.10.2026) · eşit klipte ❷ RHYTHM NOT TRIGGERED; ritim oda kesmesi + rejim nabzı (A/G) + müzik
⛔ ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — ≥ 9,0 sn kutu gerekir; {4,6,8} çıkarsa karar sahibe döner [DERS 23]

YAPI          tek katlı kireçtaşı villa ≈500 m² · ön cephe (kemer + 2 pencere) · hol 6 m · salon 10 × 9 · yemek 9 × 6 ·
              mutfak 7,5 m · yatak 7,5 m · giyinme 4,5 m · banyo 6 × 6 · veranda 12 × 5 (4 taş kolon)
SAHA          kuru tepe ülkesi 38° K · çapalar: ufukta servili alçak tepeler (%50, her istasyonda) · iki yaşlı zeytin (A · T)
ZAMAN YAYI    ≈1 restorasyon sezonu → 12 dk · ÜSLUP BEYANI: tek yaz gününün ışığı
IŞIK          TEK GÜN 06:00 → 20:00 (mavi saat) · Σ rejim 14 sa 00 dk · 21 Haziran
REJİM         A (10 dk) × 84 · G (gerçek zaman) × 6 (S26 · S34 · S48 · S60 · S77 · S89)
KAMERA        ⭐ ÇOK İSTASYON BEYANI (sahip istisnası 17.10.2026 — kural en çok 2):
              A MAIN STATION (S0–S9 · S88) · H HALL (S10–S16 · S86) · L SALON (S17–S29 · S87) · D DINING (S30–S41 · S89) ·
              K KITCHEN (S42–S53) · M BEDROOM (S54–S65) · W DRESSING (S66–S72) · B BATH (S73–S79) · T VERANDA (S80–S85)
              hepsi 24 mm · tilt 0 · roll 0 · ufuk %50 · her istasyon kendi içinde kilitli · oda sınırı = KESME
              İstasyonlar SIRALIDIR (paralel değil): her oda kendi büyümesini taşır; saat kesmede sürer
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ, istasyon başına: önce G90 → G89 (D2) · sonra her oda kendi ODA SON KARESİ'nden geriye
              (G89′ → G88 · G88′ → G87 · … · G10′ → G9 … G0) · her kare zincir_kontrol (aynı istasyon içinde)
GÜNLÜK        THE_GRAND_REVIVAL_URETIM_GUNLUGU.md — ⛔ boş (üretim başlamadı) → bu SPEC'in hükmü üretimle başlar
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı · ❺ FINAL BEAT

```
SAHNE       S89 (712,0–720,0) · DINING STATION · rejim G (gerçek zaman)
FİNAL BEAT  712,0–716,0 olay: iki kişi masanın uzak ucunda sandalyelerini çeker ve karşılıklı oturur ·
            716,0–720,0 TUTUŞ: iki kişi oturur, avize yanık, başka hiçbir şey değişmez
SANİYE      718,0 (son 4,0 sn'lik TUTUŞUN içi; mavi saat)
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ):
   ① masanın uzak ucunda İKİ KİŞİ oturuyor (yandan, yüz okunmaz) · önlerinde iki tabak, iki bardak, sürahi, ekmek
   ② bronz lineer avize YANIK · ON sandalye: 1 + 1 baş + iki yanda dörder (2 + 4 + 4)
   ③ uzak duvarda ÜÇ cam kapı (x 501–1419 · 918 px ± 2) — ardında aplikleri yanık veranda, koyu mavi bahçe
   + geçici ekipman GİTMİŞ: işçi YOK · araba YOK · membran YOK · merdiven YOK
   + BEDEL görünür değil, KAFİYE bir klip önce: S88 (704,0–712,0) ön cephe G0 kadrajında sarmaşıksız, iki pencere ışıklı

KOMUT
   ffmpeg -ss 718.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①–③'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — AÇILIŞ–FİNAL KAFİYESİ (MAIN STATION · ışık bilinçli farklı)
   ffmpeg -ss 0.3   -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 711.5 -i teslim.mp4 -frames:v 1 kanit_g89p.jpg
   İki karede kuş banyosu aynı yer ve boy (x 1397–1483 · 86 px ± 2) · cephe x 222–1698 · kemer x 881–1039 · zeytinler ve tepeler aynı.
   Işık: G0 06:00 sabah ↔ G89′ 20:00 mavi saat — kanıt çifti AYNI IŞIK iddiası taşımaz.
```

---

## 2. KADRAJ KİLİTLERİ — dokuz istasyon (f=24 · tilt 0 · x_px = 960 + 1280·x/D · yüzdeler ALT kenardan)

| kod | istasyon | h · D · bakış | ⭐ ölçü çapası (px · x) | yapı çizgileri | kareler |
|:-:|---|---|---|---|---|
| A | MAIN STATION | 1,6 · 26 · 270° | kuş banyosu 86 · 1397–1483 | cephe 222–1698 · taban %43 · saçak %63 · kemer 881–1039 | G0–G9 · G10′ · G88 · G89′ |
| H | HALL STATION | 1,5 · 7,0 · 90° | taş kemer 584 · 668–1252 | uzak duvar 411–1509 · zemin %25 · tavan %96 | G10–G16 · G17′ · G86 · G87′ |
| L | SALON STATION | 1,5 · 8,5 · 180° | hol açıklığı 542 · 689–1231 | uzak duvar 207–1713 · zemin %29 · tavan %92 | G17–G29 · G30′ · G87 · G88′ |
| D | DINING STATION | 1,5 · 8,5 · 270° | üç cam kapı 918 · 501–1419 | zemin %29 · kapı üstü %71 | G30–G41 · G42′ · G89 · G90 |
| K | KITCHEN STATION | 1,5 · 7,3 · 0° | yemek odası kapısı 420 · 1031–1451 | uzak duvar 302–1618 · zemin %26 · tavan %87 · servis kapısı 329–504 | G42–G53 · G54′ |
| M | BEDROOM STATION | 1,5 · 8,0 · 180° | koridor kapısı 192 · 400–592 | uzak duvar 352–1568 · zemin %28 · tavan %87 | G54–G65 · G66′ |
| W | DRESSING STATION | 1,5 · 8,2 · 270° | yatak odası kapısı 250 · 835–1085 | uzak duvar 601–1319 · zemin %28 · tavan %77 | G66–G72 · G73′ |
| B | BATH STATION | 1,5 · 6,0 · 180° | pencere 512 · 704–1216 | denizlik %38 · lento %82 | G73–G79 · G80′ |
| T | VERANDA STATION | 1,6 · 12 · 90° | soldan 2. kolon 64 · 654–718 | veranda kenarı %31 · çatı kenarı %80 | G80–G85 · G86′ |

```
KAMERA SABİTLİK  istasyon İÇİNDE ilk/son kare kayması ≤ 2 px (KAMERA_ISTASYONU §7) · istasyonlar ARASI karşılaştırma YOK
                 (farklı kamera) · dönüş klipleri (S86 · S87 · S88 · S89) kendi istasyonunun ilk zinciriyle aynı çapada (± 2 px)
ORTAK ÇAPA       ufuk %50 her istasyonda · pencerelerden servili tepe çizgisi · A ↔ T iki zeytin
KAPI ÇAPASI      salon açıklığında bitmiş hol (G17+) · mutfak kapısında bitmiş yemek odası (G42+) · giyinme kapısında bitmiş
                 yatak odası (G66+) · banyo kapısında bitmiş giyinme odası (G73+) · veranda camlarında bitmiş salon + yemek (G80+)
                 — komşunun görünen eşyası komşunun SON karesiyle aynı (renk, sayı, yer)
```

---

## 3. SAYIM VE DEFTER KİLİTLERİ — ❹ İNŞA

| kilit | kare | sayı / hâl |
|---|---|---|
| sandalye | G35 · G36 · G39 · G41 → G90 | 0 · 2 · 6 · 10 (iki baş + iki yanda dörder) — hiçbir karede 10'dan fazla |
| salon | G24 · G25 · G26 · G27 · G29 | kanepe 1 · 2 · berjer 2 · taş sehpa 1 · yan sehpa 2 |
| mutfak taburesi | G53 · G54′ | 2 · 4 |
| yatak odası | G61 · G63 | tek king yatak · komodin 2 + abajur 2 |
| gardırop | G70 · G71 | iki duvar, düz ceviz kapak (AYNA YOK) |
| banyo | G77 · G78 | çift lavabo + iki aplik (AYNA YOK) · tek bağımsız küvet |
| veranda | G82 · G83 | tek oturma grubu · iki koltuk |
| ağır yük (geç teslimat) | G26 · G34 · G48 · G60 · G77 | yük kapının içinde, arabada BEKLER → G klibinde dört işçi taşır |
| ışık | G87′ · G88′ · G86′ · G89′ · G90 | hol avizesi · salon halka ışık + lambader · veranda aplikleri · ön pencereler + yol · yemek avizesi — her biri yalnız kendi klibinde yanar, bir kez |
| kadro | her A klibi · G klipleri · S86+ | iki işçi koyu mavi + gri · geç teslimat sonunda (S25 · S33 · S47 · S59 · S76) ve G'de dört · S86'dan iki kişi sade akşam kıyafeti |

```
❹ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır):
   villa 1 · iki işçi (dört: geç teslimat sonu + G) · alçak düz araba 1 · seyyar merdiven · koruma membranı · iskele kulesi (A, S2–S5) ·
   taş/parke/panel istifleri · mobilya listesi (PLAN §DEFTERLER) · iki kişi (S86+) · zeytin 2 · kuş banyosu 1
   ⛔ DAVETSİZ: ayna · televizyon/ekran · şömine · mum/ateş · havuz · vinç · ikinci ev · yazı/tabela/marka · fazla sandalye
❹ SEBEP           her eşya kapıdan, arabayla ve kadroyla girer (kaynak → taşıyıcı → hedef); ışık bir önceki klipte asılan
                  sönük armatürden yanar (S14 → S86 · S21 → S87 · S85 · S88 · D avizesi S33 → S89)
❹ GİZLİ İŞ        elektrik → armatür önce sönük asılır · tesisat → mutfak sol duvarı sökülür, çıplak kalır (S42) · batarya (S78)
```

---

## 4. KESMELER VE BÖLÜM SINIRLARI — ❷ kör koşar; bu bölüm ❺ ve operatör içindir

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 712,0 (89 kesme, her 8,0 sn — DÜZ, hepsi ölçü başı)
İSTASYON KESMELERİ   80 (A→H) · 136 (H→L) · 240 (L→D) · 336 (D→K) · 432 (K→M) · 528 (M→W) · 584 (W→B) · 640 (B→T) ·
                     688 (T→H) · 696 (H→L) · 704 (L→A) · 712 (A→D) — 12 kesme, düz kesme, geçiş efekti YOK
REJİM KESMELERİ      A→G→A: 208/216 (S26) · 272/280 (S34) · 384/392 (S48) · 480/488 (S60) · 616/624 (S77) · 712 (S89)
DİKİŞ                aynı istasyon içinde: iki yaka AYNI KARE · istasyon kesmesinde: saat sürer, kare değişir
BÖLÜM SINIRI ①       240,0 — G30′ (salon sonu) ↔ G30 (yemek odası başı): sınır bir istasyon kesmesidir; BOLUM_1 G30′'da biter
BÖLÜM SINIRI ②       480,0 — G60: BOLUM_2'nin son I2V'si (S59) G60'ta biter, G60 BOLUM_3'ün ilk görselidir (BEDROOM, aynı kare)
                     ffmpeg -ss 480.0 -i teslim.mp4 -frames:v 1 sinir2.jpg → king yatak gövdesi koridor kapısının içinde arabada,
                     dört işçi · halı başlığın önünde · koridor kapısı 192 px
KART                 720,0–725,0 · G90 + başlık · erime ≤ 1 sn · müzik tutulan akor
MÜZİK                ✅ VAR · 120 BPM · müziksiz pencere 0,0–8,0 · katman = oda · S86–S89 incelir · −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 5. ❺ TESLİM — belgeli merceğin okuyacağı beyanlar

```
VAAT            Terk edilmiş büyük bir taş villayı oda oda yeniden yaşanır bir eve çevirmek ve ilk akşam yemeğini o evde yemek.
DİRENÇ          ① ölçek (dokuz mekân) · ② TEK KAPI — ağır parçalar gerçek zamanda kapıdan: S26 (208,0) taş sehpa · S34 (272,0)
                masa · S48 (384,0) taş tezgâh · S60 (480,0) king yatak · S77 (616,0) küvet · ③ çürüme (S0–S1 · her oda açılışı)
BEDEL           sarmaşığın yeşil alacakaranlığı — S1 (8,0) sökülür, geri dönmez; S88'de aynı kadrajda sarmaşıksız, ışıklı
AÇILIŞ          nesne: kapı eşiğinde yarısı dışarıda çürük kanepe + sarmaşıklı kemer · eylem: iki işçi ilk karede taşıyor ·
                MERAK SORUSU: "Bu harap villa neye dönüşecek — ve içinde kim yaşayacak?"
İŞLEV ANI       S86 (688,0) hol avizesi · S87 (696,0) salon lambaları · S88 (704,0) dış cephe mavi saat · S89 (712,0–716,0) ilk
                yemek · 716,0–720,0 tutuş
LOOP RHYME      G0 ↔ G89′ (MAIN STATION) — aynı cephe, sarmaşık → ışık
OMURGA (90)     PLAN §Dört kabul testi ④
SES             MUSIC YES — kesmeler ölçü başında · müziksiz pencere 0,0–8,0 sn (S0 tamamı)
TESLİM          END CARD YES — 5,0 s (720,0–725,0) · SPEED 1x · 725,0 sn
AI BEYANI       YAYIN_PAKETI §AÇIKLAMA sabit beyan bloğu + Studio "Altered content = EVET"
KAPAK           THE_GRAND_REVIVAL_KAPAK.md — G90'dan, bölünmüş yerleşim YOK
```

---

## 6. 🎞️ SAHNE SAHNE — hedef karede görülmesi gereken (❹ · ❺)

> Betikten üretilir (`grv_gen.py`). "hedef kare" = klibin bittiği kare: aynı oda içinde G(n+1), oda sonunda G(n+1)′.

<!-- ÜRETİCİ: SAHNE SAHNE BAŞI -->
| S | saniye | saat · rejim | istasyon | hedef karede görülmesi gereken | kanıt / sayı |
|:-:|---|---|:-:|---|---|
| S0 | 0,0–8,0 | 06:00 · A | A | Kanepe ve kırık koltuk arabada · sarmaşıklı kemer, kırık pencereler, hasarlı çatı görünür | AÇILIŞ NESNESİ · 'from the first frame' · kuşkulu yük yok |
| S1 | 8,0–16,0 | 06:10 · A | A | Kemer ve iki pencere açıklığı sarmaşıksız · taş hâlâ kirli gri · İLK BÜYÜK SONUÇ (0:16) | İLK BÜYÜK SONUÇ · açıklık sayısı sabit |
| S2 | 16,0–24,0 | 06:20 · A | A | Bütün cephe açık bej taş · geometri aynı | yalnız renk değişir |
| S3 | 24,0–32,0 | 06:30 · A | A | Bütün çatı soyulmuş: gri altlık ve çıtalar aynı eğimde | çatı eğimi ve yüksekliği sabit |
| S4 | 32,0–40,0 | 06:40 · A | A | Çatı yeni, koyu antrasit, aynı siluet çizgisi | çatı siluet çizgisi sabit |
| S5 | 40,0–48,0 | 06:50 · A | A | Sol pencere yeni, sağ eski | açıklık ölçüsü sabit |
| S6 | 48,0–56,0 | 07:00 · A | A | İki pencere yeni ve eş | iki pencere aynı ölçü |
| S7 | 56,0–64,0 | 07:10 · A | A | Ceviz kapı yerinde, kanatlar kapalı · kemer korunur | kemer korunur |
| S8 | 64,0–72,0 | 07:20 · A | A | Taş yol tamam, aynı genişlik ve çizgi · kenarlarda sönük yol lambaları | yol başı, sonu, genişliği sabit |
| S9 | 72,0–80,0 | 07:30 · A | A | Dış cephe ilk tamamlanmış hâlinde · içerisi henüz gösterilmedi | ön cephe bölümünün sonu |
| S10 | 80,0–88,0 | 07:40 · A | H | Hol boş · kemer, kapı, iki dar pencere sabit | kemer + ceviz kapı = A ile ortak çapa |
| S11 | 88,0–96,0 | 07:50 · A | H | Duvarlar düz, gri-beyaz, boyasız | — |
| S12 | 96,0–104,0 | 08:00 · A | H | Açık traverten zemin kesintisiz | — |
| S13 | 104,0–112,0 | 08:10 · A | H | Duvarlar sıcak kırık beyaz · hol aydınlık | — |
| S14 | 112,0–120,0 | 08:20 · A | H | Avize asılı, sönük | avize kendi zincirinde · ek kaldırma düzeni yok |
| S15 | 120,0–128,0 | 08:30 · A | H | Tek konsol sol duvarda, üstünde tek vazo | tek konsol |
| S16 | 128,0–136,0 | 08:40 · A | H | Hol tamam: konsol, vazo, tablo, bank, avize | ayna yok — tablo (sahip kararı) |
| S17 | 136,0–144,0 | 08:50 · A | L | Salon boş · açıklıktan bitmiş hol görünür | açılış kanepesi geri dönmez · hol = ortak çapa |
| S18 | 144,0–152,0 | 09:00 · A | L | Duvarlar fildişi · pencere, tavan, duvar sınırları aynı | — |
| S19 | 152,0–160,0 | 09:10 · A | L | Meşe zemin tek yönde | döşeme yönü sabit |
| S20 | 160,0–168,0 | 09:20 · A | L | Ceviz panel yalnız sol bölümde | açıklık ve duvarın kalanı değişmez |
| S21 | 168,0–176,0 | 09:30 · A | L | Halka ışık asılı, sönük · yüksekliği sabit | — |
| S22 | 176,0–184,0 | 09:40 · A | L | Halı ortada, köşeleri sabit | halı köşeleri kilit |
| S23 | 184,0–192,0 | 09:50 · A | L | Tek ana kanepe | tek kanepe |
| S24 | 192,0–200,0 | 10:00 · A | L | İki kanepe, aralarında geniş geçiş | iki kanepe |
| S25 | 200,0–208,0 | 10:10 · A | L | İki berjer · taş sehpa arabada, açıklığın içinde | her yük tek berjer · geç teslimat |
| S26 | 208,0–216,0 | 10:20 · G | L | Sehpa halının ortasında, ayakları halıya basar, kanepelere değmez | GERÇEK ZAMAN · ağırlık yavaş okunur |
| S27 | 216,0–224,0 | 10:20 · A | L | Konsolun ayak izi sabit | — |
| S28 | 224,0–232,0 | 10:30 · A | L | Tam iki yan sehpa | sayı 2 |
| S29 | 232,0–240,0 | 10:40 · A | L | Salon tamam — ilk iç mekân zirvesi · BÖLÜM 1 sonu | BÖLÜM 1 sonu (240,0 sn) |
| S30 | 240,0–248,0 | 10:50 · A | D | Oda boş · mutfak kapısından harap mutfak, camlardan harap veranda | yük yolu = cam kapılar (veranda) |
| S31 | 248,0–256,0 | 11:00 · A | D | Duvarlar grej | — |
| S32 | 256,0–264,0 | 11:10 · A | D | Taş zemin · desen bundan sonra aynı | zemin deseni kilit |
| S33 | 264,0–272,0 | 11:20 · A | D | Avize merkez ekseninde · masa arabada, kapının içinde | geç teslimat |
| S34 | 272,0–280,0 | 11:30 · G | D | Tek masa, tek sabit konum | GERÇEK ZAMAN · ağırlık yavaş okunur |
| S35 | 280,0–288,0 | 11:30 · A | D | Toplam iki sandalye | sayı 2 |
| S36 | 288,0–296,0 | 11:40 · A | D | Büfe sağ duvarda · iki sandalye aynı yerde | büfe geçişi kapatmaz |
| S37 | 296,0–304,0 | 11:50 · A | D | Tek yeni dolap | tek dolap |
| S38 | 304,0–312,0 | 12:00 · A | D | Toplam altı sandalye: iki baş + solda dört | SAYIM PİLOTU · her yük tek sandalye (DERS 89) |
| S39 | 312,0–320,0 | 12:10 · A | D | Perdeler asılı · altı sandalye aynı | pencere konumu sabit |
| S40 | 320,0–328,0 | 12:20 · A | D | Toplam on sandalye: iki baş + iki yanda dörder | sayı 10 · her yük tek sandalye |
| S41 | 328,0–336,0 | 12:30 · A | D | Masa, on sandalye, büfe, dolap, perde, avize tamam | yemek odası sonu |
| S42 | 336,0–344,0 | 12:40 · A | K | Sol duvar çıplak · kapılar aynı | tesisat duvarı sabit |
| S43 | 344,0–352,0 | 12:50 · A | K | Duvarlar krem · sınırlar aynı | — |
| S44 | 352,0–360,0 | 13:00 · A | K | Taş zemin · ada yeri boş | — |
| S45 | 360,0–368,0 | 13:10 · A | K | Yüksek dolaplar tek duvarda | tek duvar |
| S46 | 368,0–376,0 | 13:20 · A | K | Alt dolaplar ve tezgâh sol duvarda | kapak bölümleri kilit |
| S47 | 376,0–384,0 | 13:30 · A | K | Ada gövdesi ortada, üstü boş · taş tezgâh arabada yanında | geç teslimat |
| S48 | 384,0–392,0 | 13:40 · G | K | Ada tek parça; tezgâh kenarı, kalınlığı, boyu sabit | GERÇEK ZAMAN · PİLOT |
| S49 | 392,0–400,0 | 13:40 · A | K | Taş paneller yerinde | taş deseni sabit |
| S50 | 400,0–408,0 | 13:50 · A | K | Buzdolabı yerinde · ön yüzü dolap çizgisinde | dolap çizgisi |
| S51 | 408,0–416,0 | 14:00 · A | K | Tek fırın ünitesi | yeni dolap yok |
| S52 | 416,0–424,0 | 14:10 · A | K | Tam iki tabure | sayı 2 |
| S53 | 424,0–432,0 | 14:20 · A | K | Dört tabure · ada, kiler, cihazlar, tezgâh tamam | sayı 4 · mutfak sonu |
| S54 | 432,0–440,0 | 14:30 · A | M | Oda boş · kapı, pencere, giyinme kapısı aynı | — |
| S55 | 440,0–448,0 | 14:40 · A | M | Duvar bitişi tamam | — |
| S56 | 448,0–456,0 | 14:50 · A | M | Meşe zemin, bu kameraya göre sabit yön | döşeme yönü |
| S57 | 456,0–464,0 | 15:00 · A | M | Başlık duvarı ölçüsü değişmez | başlık ortalı |
| S58 | 464,0–472,0 | 15:10 · A | M | Perdeler asılı | pencere ölçüsü sabit |
| S59 | 472,0–480,0 | 15:20 · A | M | Halı yerinde · yatak gövdesi arabada, kapının içinde · BÖLÜM 2 sonu (480,0 sn) | BÖLÜM SINIRI KARESİ G60 · geç teslimat |
| S60 | 480,0–488,0 | 15:30 · G | M | Yatak gövdesi başlığa ortalı | GERÇEK ZAMAN · BÖLÜM 3 ilk sahnesi |
| S61 | 488,0–496,0 | 15:30 · A | M | Tek yatak, sabit örtü düzeni | yatak ölçüsü sabit |
| S62 | 496,0–504,0 | 15:40 · A | M | İki komodin, iki abajur | sayı 2 + 2 |
| S63 | 504,0–512,0 | 15:50 · A | M | Bank yatak ucunda, geçişler açık | — |
| S64 | 512,0–520,0 | 16:00 · A | M | Dinlenme köşesi | — |
| S65 | 520,0–528,0 | 16:10 · A | M | Yatak, komodinler, bank, şezlong, makyaj alanı tamam | ayna yok · oda sonu |
| S66 | 528,0–536,0 | 16:20 · A | W | İki uzun duvar boş | — |
| S67 | 536,0–544,0 | 16:30 · A | W | Duvarlar açık renk | — |
| S68 | 544,0–552,0 | 16:40 · A | W | Meşe zemin · ada yeri boş | — |
| S69 | 552,0–560,0 | 16:50 · A | W | Sol gardırop duvarı tam | modül sayısı kilit |
| S70 | 560,0–568,0 | 17:00 · A | W | İki gardırop duvarı eş · ayna yok | ayna yok (sahip kararı) |
| S71 | 568,0–576,0 | 17:10 · A | W | Ada ortada, eşit geçişler | eşit geçiş |
| S72 | 576,0–584,0 | 17:20 · A | W | Bank ve ada ayrı · raflarda sabit sayıda grup | raflar çoğalmaz · oda sonu |
| S73 | 584,0–592,0 | 17:30 · A | B | Zemin temiz · duş nişi yerinde | duş nişi sabit |
| S74 | 592,0–600,0 | 17:40 · A | B | Duvarlar taş · damarlar sabit | duvar damarları kilit |
| S75 | 600,0–608,0 | 17:50 · A | B | Zemin taş · derz yönü kilit | derz çizgileri |
| S76 | 608,0–616,0 | 18:00 · A | B | Tek dolap bankası, iki lavabo, iki aplik · küvet arabada kapının içinde | ayna yok — aplik (sahip kararı) · geç teslimat |
| S77 | 616,0–624,0 | 18:10 · G | B | Tek küvet, sabit yer | GERÇEK ZAMAN |
| S78 | 624,0–632,0 | 18:10 · A | B | Batarya tek ve sabit | su akışı yok |
| S79 | 632,0–640,0 | 18:20 · A | B | Küvet, dolap, aplikler, bank, duş nişi tamam | banyo sonu |
| S80 | 640,0–648,0 | 18:30 · A | T | Ahşap veranda · kolonlar ve tavan aynı | kolon ve tavan sabit |
| S81 | 648,0–656,0 | 18:40 · A | T | Tek oturma grubu | tek grup |
| S82 | 656,0–664,0 | 18:50 · A | T | Tam iki koltuk | sayı 2 |
| S83 | 664,0–672,0 | 19:00 · A | T | Sehpa grubun merkezinde | — |
| S84 | 672,0–680,0 | 19:10 · A | T | Bank arka duvarda · geçiş açık | geçiş açık |
| S85 | 680,0–688,0 | 19:20 · A | T | Tamamlanmış veranda, sıcak ışık, bütün mobilya aynı karede | ışık tek karede yanar (ISIK_FINALI) |
| S86 | 688,0–696,0 | 19:30 · A | H | Hol avizesi yanık · kapı kapalı | ışık tek karede yanar · sahip kararı: final ışıklar |
| S87 | 696,0–704,0 | 19:40 · A | L | Salon lambalı · örtü yok | ışık tek karede yanar |
| S88 | 704,0–712,0 | 19:50 · A | A | İki pencere yanık, yol ışıkları yanık · açılışla aynı kadraj, karşıt hâl | AÇILIŞ–FİNAL KAFİYESİ · ışık tek karede |
| S89 | 712,0–720,0 | 20:00 · G | D | USTA KARE G90 — iki kişi sofrada, avize yanık, on sandalye, camların ardında yanık veranda | İŞLEV ANI · 4 + 4 · kapak kaynağı |
<!-- ÜRETİCİ: SAHNE SAHNE SONU -->

---

## 7. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç URETIM_GUNLUGU §0'a · ⑧ iki kare alınmıyorsa ÜRETİLMEZ
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0
⛔ PİLOT ÜÇLÜ     ① S89 + G90 · ② S38 (sayım) · ③ S48 (taş tezgâh, G) · sonra S0 — PLAN §PİLOT ÜÇLÜ
⛔ USTA KARE      G90 önce; kapı: ① iki kişi ② avize + 10 sandalye ③ üç cam kapı 918 px — bu sırayla okunuyor mu
⛔ ZİNCİR         istasyon başına zincir_kontrol.sh + ölçü çapası ELLE (px) · kapı çapası (komşu oda) elle
⛔ GÜNLÜK         klip başına satır (İSTASYON sütunu); günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ ARAÇLAR        qa_paket.sh --bolum 3 · prompt_kontrol 12 dk + ODA + ′ kareler · zincir_kontrol istasyon başına
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master; 1920×1080 · 725,0 sn · kart 5,0)
⛔ İHRAÇ          bash araclar/ihrac_kontrol.sh — süre 725,0 · kart 5,0 · müzik VAR · final tutuşu SSIM ≥ 0,90 [DERS 63]
⛔ KAPAK KANITI   ffmpeg -ss 719.5 -i teslim.mp4 -frames:v 1 g90_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g90_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
❶ AÇIK KARAR      kör merceklere "dokuz sabit kamera, oda oda" nötr gerçek satırı (PLAN §ÇOK İSTASYON BEYANI) — varsayılan VERİLMEZ
```
