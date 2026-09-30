# 🔬 THE FIRST GUEST — QA SPEC

```
⛔ Bu dosya PLANIN DEĞİL, TESLİMİN kapısıdır. Her madde TEK KAREDE ya da TEK KLİPTE ölçülür.
   Ölçülemeyen bir madde bu dosyaya yazılmaz.
KAYNAK  dikey_shorts/THE_FIRST_GUEST/THE_FIRST_GUEST_DIKEY_TIMELAPSE.md
IZGARA  7 × 8,0 = 56,0 sn · 8 görsel (G0–G7) + 7 I2V · ⭐ TEK REJİM: 7 × B
DURUM   ⛔ ÜRETİLMEDİ — hiçbir madde henüz KOŞULMADI
```

---

## 1. ⭐ KOYU BANT KAPISI — filmin tek iddialı tarifi, üretimin İLK sınavı

```
NEREDE   yalnız G7. Servis geçidinden çıkan turuncu kamanın (%63,71 → %75,41 · 225 px) İÇİNDE.
NEDİR    kamayı baştan sona kesen, yaklaşık 120 piksel eninde, DÜZ KENARLI, koyu bir bant.
NE DEĞİL ⛔ bir gövde · ⛔ bir siluet · ⛔ uzuvlu bir şekil · ⛔ dokulu, kıyafetli, parlak bir yüzey

  ① KENARLAR DÜZ OLMALI. Bandın iki uzun kenarı doğrusaldır; kavis, girinti, çıkıntı YOKTUR.
     ⛔ Kenarda bir omuz, bir baş ya da bir diz okunuyorsa kare DÜŞER.
  ② İÇİNDE AYRINTI OLMAMALI. Bandın içindeki parlaklık standart sapması, geçidin kendi
     gölgesinin standart sapmasının %20'sini AŞMAMALI.
     ⛔ Göz, ışık, desen, katman, kumaş okunuyorsa kare DÜŞER.
  ③ TONU GEÇİDİN KENDİ GÖLGESİYLE AYNI OLMALI (L* farkı ≤ %8).
  ④ BANT KAMAYI TAM KESMELİ: kamanın bir kenarından öbür kenarına kadar, kesintisiz.
     ⛔ Kamanın ortasında durup biten bir leke DEĞİLDİR.
  ⑤ KIMILDAMAMALI. S6 klibinin son 2,5 saniyesinde bandın kenarları tek piksel oynamaz.

⭐ NEDEN BU KADAR SERT: filmin son cümlesi budur. Bant bir yaratığa dönüşürse film bir yaratık
   filmi olur ve timelapse ölür; bant hiç belirmezse finalin anlamı yok olur. ⛔ YEDEK PLAN YOK.
   Bu yüzden PİLOT KLİP S6'dır ve üretilecek İLK klip odur [plan §PİLOT ÜÇLÜ].
⛔ PROMPTTA KONTROL: "limb", "head", "eye", "figure", "creature", "body", "alien" kelimelerinden
   hiçbiri sekiz görselin ve yedi I2V'nin HİÇBİRİNDE geçmez — ne olumlu ne olumsuz [DERS 33 · 35].
   ⭐ KOŞULACAK DESEN (sekiz görsel + yedi I2V metninde, plan Türkçesinde DEĞİL):
      \b(limb|limbs|creature|creatures|alien|aliens|torso|shoulder|shoulders|hand|hands|
        eye|eyes|humanoid|silhouette|figure|figures|guardian|robe|cloak|armour|armor)\b   → 0 olmalı
   ⚠️ DESEN İKİ KEZ DARALTILDI, çünkü iki ayrı yanlış alarm ölçüldü (26.09.2026):
      ① kelime sınırsız "limb" → NEGATIVE'deki "climbed" kelimesini yakaladı (17 yanlış pozitif)
      ② "face|head|arm|leg|body" → kaya YÜZÜ (face), sinter KAFASI (head), rover KOLU (arm),
         tripod AYAĞI (leg) ve kilidin GÖVDESİ (body) teknik sözlüktür ve 130 yanlış pozitif verdi.
      ③ "being" → sayım cümlesinin zorunlu kuyruğu ("nothing else being worked on"), 18 yanlış pozitif.
      ⛔ "face" ASLA yasaklanamaz: insan kuralı cümlesi ("no readable face anywhere") ZORUNLUDUR.
      ⭐ Yine de İKİ kelime bilerek DEĞİŞTİRİLDİ, yaratık riski olan bir filmde ucuz temizlik:
         "body" → "shell" (kilidin gövdesi) · "silhouette" → "flat black shape" (kum yığını).
```

---

## 2. ⭐ DEFTER KAPISI — TEMİZ KUM ALANI

```
TANIM    alt bandın (%0 → %75,41 · 1 448 px, kenardan kenara) yüzde kaçı hâlâ ORİJİNAL dalgalı
         dokuda: kesintisiz, düzenli, paralel kum sırtları; üstünde iz, kesik, yığın, cam yok.
NASIL    kare gri tonlamaya çevrilir, bandın içinde 32 × 32 piksellik kutular taranır; bir kutu
         "temiz" sayılır ancak ve ancak içindeki baskın doku yönü komşularıyla ±10° içindeyse.

  kare      G0   G1   G2   G3   G4   G5   G6   G7
  hedef %  100   92   71   55   44   38   35   35
  tolerans  0   ±3   ±4   ±4   ±4   ±3   ±2    0     (G7 = G6, birebir)

⛔ DÜŞME KOŞULU ① bir kare kendinden öncekinden FAZLA temiz kum taşıyorsa o kare düşer.
   ⭐ Havasız bir ayda hiçbir şey izi silmez: rüzgâr yok, yağmur yok, akış yok.
⛔ DÜŞME KOŞULU ② G0 %100'ün altındaysa G0 düşer. Filmin bütün bedeli oradan başlar: kadrajda
   TEK BİR İZ olmamalı, rampa bile inmemiş olmalı.
⛔ DÜŞME KOŞULU ③ G6 ile G7 arasında temiz kum yüzdesi DEĞİŞİRSE kapak kanıtı düşer (§4).
⛔ DÜŞME KOŞULU ④ HACİM: kazılan 84,0 m³ (14,00 × 10,00 × 0,60) × 1,20 kabarma = 100,8 m³ gevşek,
   ve bu kadrajı TERK ETMEZ: solda 14,00 m uzun, 35° şevli, 2,25 m yüksek (72 px) bir yığın olur.
   G2'den sonra yığın hiçbir karede küçülmez ve hiçbir kamyon kadrajdan kum çıkarmaz.
```

---

## 3. IŞIK KAPISI — iki ayrı saat, iki ayrı yarı

```
BİRİNCİ YARI (G0–G3) — güneş ve TAŞ SÜTUNUN GÖLGESİ
  kare   azimut  yükseklik  yüz kats.  kum kats.  sütun gölgesi / yön
  G0    100,71°    3,456°     0,981      0,060     182,1 m / rel +10,71°
  G1    122,43°    9,886°     0,831      0,172      63,1 m / rel +32,43°
  G2    144,91°   14,888°     0,556      0,257      41,4 m / rel +54,91°
  G3    168,19°   17,643°     0,195      0,303      34,6 m / rel +78,19°
  ⛔ DÜŞME ① kaya yüzü G0'da kumdan PARLAK, G3'te kumdan KOYU olmalı — iki eğri ortada kesişir.
  ⛔ DÜŞME ② sütun gölgesi hiçbir karede UZAMAZ ve yönü hiçbir karede geri DÖNMEZ (+10,71 → +78,19).

⭐ BIÇAK (S3 klibinin içinde, 4,00 → 6,32 saniye)
  12:00 L = 0 (kapı dibinde) → 12:03 %73,87 → 12:09 %69,91 → 12:15 %64,11 → 12:21 %54,80 → 12:35 kare dışı
  ⛔ DÜŞME ③ gölge kenarı YUMUŞAK geçerse klip düşer. Havasızlıkta YARI GÖLGE YOKTUR: çizgi bir
     KESİKTİR ve geçtiği yer TEK KADEMEDE kararır.
  ⛔ DÜŞME ④ bıçak geçtikten sonra taş sütunun gölgesi HÂLÂ varsa klip düşer.

İKİNCİ YARI (G4–G7) — ⭐ güneş YOK; saat IŞIK KAYNAĞI SAYISI ve SIÇRAMA MESAFESİDİR
  kare   ışık kaynağı   gölge kenarı (sıçrayan ışığın kaynağı)   kadrajın genel parlaklığı
  G4          3                   103,0 m                        en yüksek (ikinci yarıda)
  G5          4                   346,0 m                        düşer
  G6          5                   774,9 m                        düşer
  G7        ⭐ 6                 2 603,0 m                        en düşük + ⭐ turuncu kama
  ⛔ DÜŞME ⑤ G4 · G5 · G6 · G7'nin herhangi birinde DOĞRUDAN GÜNEŞ IŞIĞI varsa o kare düşer.
     Kontrol: kumda sert kenarlı ve BİRBİRİNE PARALEL gölgeler = güneş. Lambalardan gelen gölgeler
     IŞINSALDIR (her lamba kendi merkezinden) ve birbirine paralel DEĞİLDİR.
  ⛔ DÜŞME ⑥ genel parlaklık G4 → G7 arasında monoton düşmüyorsa kareler düşer (kama hariç tutulur).
  ⭐ DÜŞME ⑦ G7'de kumdaki her iz İKİ GÖLGE taşımalı: biri beyaz lambadan, biri turuncu kamadan,
     ters yönlerde. Tek gölge varsa kama yanlış yerdedir.
⛔ GÜNEŞ HİÇBİR KAREDE KADRAJDA DEĞİL — iki ayrı sebeple: 05:00–12:00 kameranın ARKASINDA,
   13:00–19:00 kayanın ARKASINDA. Kadrajda güneş diski ya da huzme görünürse istasyon yanlıştır [DERS 39].
```

---

## 4. ⛔ G6 = G7 KİMLİĞİ — kapak kanıtının kendisi

```
ARADA İKİ SAAT VAR VE İNSAN ELİ HİÇBİR ŞEYE DOKUNMUYOR. Altı şey BİREBİR aynı olmalı:
  ① insan kilidi: 171 ± 3 px en · 151 ± 3 px boy · kapısı %x 50,00 → 56,32 · dikiş çizgileri aynı
  ② pad, cam taban, kum yığını (72 ± 3 px), göbek bağı ve üç sehpası
  ③ beş beyaz lamba konisi — aynı yerde, aynı açıda, aynı sertlikte
  ④ kazık delikleri sırası ve pad basamağındaki soluk sıyrık — aynı piksellerde
  ⑤ ÜÇ ÇAPA: taş sütun (367 × 61 px) · kapı tabanı çizgisi (%75,41) · dört nervür — ±2 px
  ⑥ ⭐ temiz kum %35, tek piksel eklenmeden, tek piksel silinmeden
İZİN VERİLEN ÜÇ FARK — başka hiçbiri değil:
  ⓐ servis geçidi (216 × 315 px) düz koyudan SICAK TURUNCUYA döner
  ⓑ 225 piksellik turuncu kama kuma düşer, padı geçer, kilidin yakın yüzünü yıkar
  ⓒ ⭐ kamanın içinde tek düz kenarlı koyu bant (≈120 px)
⛔ Dördüncü bir fark varsa kapak kanıtı düşer [DERS 30].
⭐ KOŞ:  bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png   → çıkış 0 olmalı
```

---

## 5. KADRAJ KİLİTLERİ — ±2 px [sahip kararı 19.09.2026]

```
⭐ SIRA ÖNEMLİ: önce ÜÇ ÇAPAYA bak. Üçü tutmuyorsa geri kalanı ölçme, İSTASYON oynamıştır.
  ① TAŞ SÜTUN            %x 15,34 → 21,02 · %y 69,56 → 88,64   (367 × 61 px)
  ② KAPI TABANI ÇİZGİSİ  %75,41 (1 448 px) · kenardan kenara · EĞİM SIFIR
  ③ DÖRT NERVÜR          %x 5,00 · 35,00 · 50,00 · 58,33
     ⚠️ Nervür 2 (%x 35,00) kısmen taş sütunun ARKASINDADIR — bu SABİT bir örtüşmedir ve derinlik
        kanıtıdır; sekiz karede AYNI şekilde örtülmelidir. Örtüşme değişirse kamera oynamıştır.

SONRA yapı kilitleri:
  pad yakın kenarı        %63,71  ·  insan kilidi tabanı %66,34  ·  tepesi %74,22
  servis geçidi lentosu   %91,81  (boy 315 px · en 216 px · ⭐ kilidin 2,08 katı)
  kum yığını              h 72 px · %x 26,47 → 33,33
  kum bandı               %0 → %75,41 = 1 448 px
⛔ ÖLÇEK KİLİDİ: servis geçidi / insan kilidi boy oranı sekiz karede 2,08 ± 0,06 olmalı.
   Bu oran filmin ÖNERMESİDİR: "küçük" olan kapı, bizim bütün yapımızın iki katıdır.
⛔ KAPININ TEPESİ HİÇBİR KAREDE GÖRÜNMEZ. d 60,00'da kadrajın üst kenarı yalnız y = +17,01 m'ye
   ulaşır; kaya 160,00 m'dir. Kadrajın üstünde kaya BİTİYORSA kare düşer — ölçek yanılgısı ölür.
```

---

## 6. YÜK YOLU VE HAVASIZLIK KAPISI

```
⭐ HAVASIZ SAHA — üç zorunlu davranış:
  ① ATILAN TOZ ASILI KALMAZ. Kazı bıçağından, tekerlekten, düşen panelden çıkan toz TEMİZ BİR YAY
     çizer ve düşer. ⛔ Bir toz bulutu, bir pus, bir sis varsa kare düşer [MALZEME_VE_DOKU §5].
  ② GÖLGE KENARI KESKİNDİR ve gölge KAPKARADIR — yalnız sıçrayan ışık onu kurtarır.
     ⛔ Yumuşak geçişli gölge = atmosfer = kare düşer.
  ③ IŞIK HALESİ YOKTUR. Lambaların, sinter korunun, turuncu kamanın çevresinde parlama/glow YOKTUR.
     ⛔ Işık kaynağının etrafında yumuşak bir hale varsa kare düşer.
  ⛔ SU/ÇAMUR: prompt metninde su, çamur, birikinti, yağmur GEÇMEZ ve kadrajda görünmez.
     Koşulacak:  grep -icE "\bmud|puddle|rain|slush|standing water" <plan.md>  → 0 olmalı

YÜK YOLU [FIZIK_VE_AGIRLIK]
  G0 – G1   taş sütun kuma PLANTLİDİR ve ağırlığını kuma verir; başka hiçbir şey kuma oturmamıştır
  G2 – G3   sinter kafası cam tabana biner; kaburgalar cam levhadan geçip plakalara CIVATALANIR
  G4 – G7   panel kaburgaya, kaburga cam tabana, cam taban kesilmiş zemine biner
  ⛔ Her karede en az ÜÇ temas cümlesi. Asılı her cisim tek bir HALATA/KABLOYA bağlıdır.
  ⛔ Hiçbir vinç kancası BOŞ değildir [DERS 8].
  ⛔ KAYA YÜZÜNE HİÇBİR ŞEY BAĞLANMAZ: ne ankraj, ne iskele, ne kablo. Misafir ev sahibinin duvarına
     dokunmaz — bu bir tasarım kararıdır ve NEGATIVE'de kilitlidir.
```

---

## 7. SAYIM KAPISI [DERS 55]

```
Sekiz karenin sekizinde de kadrajda ŞU ALTI ŞEY VARDIR:
  ① siyah kum ovası ② kesme kaya yüzü ve dört nervürü ③ kare servis geçidi ④ serbest taş sütun
  ⑤ iniş gemisinin rampası (sol alt köşe) ⑥ pad ve üstünde ne varsa
Sekiz karenin hiçbirinde kadrajda ŞU YOKTUR:
  ⛔ GÖKYÜZÜ, yıldız alanı, ufuk çizgisi, gezegen
  ⛔ kule, heykel, oyma bezeme, ışıklı devre deseni, sembol, hiyeroglif
  ⛔ uçan araç, ikinci yapı, uzakta şehir, ikinci kapı
  ⛔ kayaya bağlanmış hiçbir insan ekipmanı
⚠️ EN OLASI MODEL ARIZASI: konsept kaynağı bilim-kurgudur ve model "alien gate" görünce yukarıdaki
   listenin TAMAMINI eklemeye çalışır. Her kare bu altı maddelik listeye karşı okunur.
⚠️ İKİNCİ ARIZA: kadrajın üstüne GÖK eklemek. SITE cümlesi ("There is no sky in the frame and no
   horizon") ve yedi I2V bunu pozitif kapatır; yine de ELLE kontrol edilir.
```

---

## 8. ⭐ TEK REJİM KAPISI (ÖLÇÜLMEDİ)

```
Yedi klibin yedisi de rejim B: 2,00 saat / 8,0 saniye = 900× … 1200× bandı (plan 1200× varsayar).
  ① Yedi klipte de bulut YOKTUR (gök yok) — rejimin görünümünü taşıyan şey GÖLGE ve TOZDUR.
  ② İlk dört klipte gölgeler bodily süpürür ve boy değiştirir. ⛔ Donmuş gölge = rejim kaçağı.
  ③ Son üç klipte güneş gölgesi yoktur; rejimi taşıyan şey EKİBİN İZİ ve ışık kaynaklarının
     sırayla yanmasıdır. ⛔ Hareketsiz klip = ⑦ merceği "işsiz aralık" verir.
  ④ İnsanlar yedi klipte de YUMUŞAK İZDİR. ⛔ Keskin figür = rejim kaçağı.
⭐ ÖLÇÜLMEDİ: deponun ilk tek rejimli filmidir. ⑥ merceği yedi eşit sıkıştırmayı "tekdüze" okur mu,
   yoksa ışık eğrisi (yüz 0,981 → 0,000 · kum 0,060 → 0,303 → 0,000) tek başına yeter mi?
   İlk üretimden sonra SANTIYE_HAREKETI §1 ve KURGU_VE_TESLIM §2.4'e birer satır iner [P18-f].
```

---

## 9. ⭐ SES KAPISI — diegetik DEĞİL, TEMAS İLETİMLİ

```
⛔ MÜZİK YOK. ⭐ VE DİEGETİK YATAK DA YOK: havasız sahada dışarıda ses yoktur.
  ① Kadrajda görünen hiçbir makine HAVADAN ses çıkarmaz. ⛔ Bir kazı bıçağının, bir sinter kafasının
     ya da düşen bir panelin "normal" sesi duyuluyorsa bant düşer.
  ② Duyulan her şey ya KASKIN İÇİNDEDİR (nefes, fan, kumanda tıkırtısı) ya da TEMASLA gelmiştir
     (gövdeye vuran panel, zeminden iletilen titreşim). Hepsi alçak geçiren ve gövde rezonanslıdır.
  ③ ⭐ 28,0'DE BIÇAK GEÇER VE HİÇBİR SES ÇIKARMAZ. Filmin en büyük görsel olayı, en sessiz anıdır:
     yalnız nefes, ve nefesin bir an durması. ⛔ Buraya bir vurgu efekti konursa bant düşer.
  ④ ⭐ 50,0 – 53,5: taş kapak kayarken KUMDAN GELEN derin titreşim — filmin EN YÜKSEK sesi.
     Ölçüm: bu 3,5 saniyenin RMS'i, filmin geri kalanının RMS'inden en az 10 dB yüksek olmalı ve
     enerjisinin %80'i 120 Hz'in ALTINDA olmalı.
  ⑤ ⭐ SES KANITI: filmin ilk sesi ile son sesi AYNIDIR — tek bir nefes.
  ⛔ Anlatıcı yok · konuşma yok · "uzay uğultusu" yok · gemi düdüğü yok · selamlaşma ritmi yok.
```

---

## 10. ZAMAN VE IŞIK GÜNÜ

```
REJİM      ⭐ 7 × B (2,00 sa) = 14,00 sa   ⛔ tavan 14,00 sa — TAM ÜSTÜNDE, sıfır pay  ✅
PENCERE    05:00 → 19:00 · 72° kuzey · δ 0 · ay günü 32 saat · doğuş 04:00 · batış 20:00
PAY        doğuştan 1,00 sa · batışa 1,00 sa
⛔ TEK REJİM: C ve G ve A hiçbir klibe girmez [SANTIYE_HAREKETI §1].
⛔ REJİM C YOK → insan yasağı YOK. Yedi klibin yedisinde de ekip yumuşak iz olarak görünür.
⭐ TEK IŞIK GÜNÜ: hava sekiz karede aynıdır çünkü HAVA YOKTUR. Değişen tek şey güneşin yeri,
   gölgelerin uzunluğu ve yapay ışık kaynaklarının sayısıdır.
```

---

## 11. ⚠️ BİLİNEN RİSKLER — üretimden önce oku

```
① ⭐ EN BÜYÜK RİSK — KOYU BANT (§1). Model onu bir yaratığa çevirirse film düşer; hiç üretmezse
   final ölür. ⛔ Yedek plan yok. Pilot klip budur ve ilk üretilecek klip odur.
② ⭐ İKİNCİ RİSK — ÖLÇEK YANILGISININ ERKEN ÖLMESİ. G0'da kadrajda hiçbir tanıdık nesne olmamalı:
   gök yok, ufuk yok, insan yok, araç yok, rampa İNMEMİŞ. Model bir kaya tepesi ya da bir gök şeridi
   eklerse filmin ilk sekiz saniyesi anlamsızlaşır.
③ GÖK EKLEME. Kadrajın üstü kaya yüzüdür ve orada biter. Modelin en güçlü refleksi buna karşıdır.
④ YUMUŞAK GÖLGE. Atmosferli dünya refleksi. Bütün gölgeler bıçak gibi olmalı (§6 ②).
⑤ ASILI TOZ. Havasızlıkta toz bulutu olmaz (§6 ①).
⑥ IŞIK HALESİ. Lambaların ve kamanın çevresinde glow olmaz (§6 ③).
⑦ İKİNCİ YARININ DÜZLEŞMESİ. G4–G7'de güneş yoktur; model dört kareyi de aynı ışıkta üretebilir.
   Sıçrama mesafesi (103 → 2 603 m) ve ışık kaynağı sayısı (3 → 6) bunu ayırır (§3).
⑧ KUMUN KENDİNİ ONARMASI. Model yeni bir karede kumu "temizleyebilir". §2'nin monoton kuralı yakalar.
⑨ KAYAYA DOKUNMAK. Model iskele, ankraj ya da kablo ile insan yapısını kayaya bağlamak ister.
   ⛔ Misafir ev sahibinin duvarına dokunmaz (§6).
⑩ ⭐ KAPAKTA AYRINTI BEKLEMEK. Koyu bant 120 pikseldir ve 120 piksellik küçük resimde 8 piksele
   iner — ⛔ orada OKUNMAZ ve okunması beklenmiyor. Kapağın kancası iki ışık lekesinin BOY FARKIDIR
   [bkz. KAPAK §1].
```
