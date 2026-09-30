# 🔬 THE MOUNTAIN CROWN — QA SPEC

```
FİLM       THE MOUNTAIN CROWN · 7 × 8,0 = 56,0 sn · dikey 9:16 · KÜTLE
DURUM      ⛔ ÜRETİLMEDİ — bu belge ÖLÇÜM TARİFİDİR, ölçüm raporu değildir
KAYNAK     dikey_shorts/THE_MOUNTAIN_CROWN/THE_MOUNTAIN_CROWN_DIKEY_TIMELAPSE.md
ARAÇLAR    araclar/prompt_kontrol.py · araclar/zincir_kontrol.sh · araclar/kesme_kontrol.sh ·
           araclar/kare_al.sh · araclar/qa_paket.sh
KAPI       ⚠️ FIX — 2 · ⛔ BLOCK 0 · MOTION FOCUS FIX 0 (25.09.2026)
           ikisi de BEYANLI: ⛔ ARAÇ KUTU SETİ ölçülmedi · yedi sahne de 8,0 sn (⑥ METRONOM)
```

---

## 1. ⭐ İKİ DEFTER KAPISI — filmin tek sert kapısı

Bu film bir şeyi ölçülebilir yapmak için yazıldı: **dağın kendisi kadrajı terk etmiyor.** İki defter
aynı maddeyi (bazalt) iki yönde sayar ve ikisi de TEK KAREDE okunur.

### ① APRON ÜST KENARI — toplayan defter · MONOTON ARTAN

```
ÖLÇÜM   Her karede, kadrajın ORTA DİKEY EKSENİNDE (x = 540 px), apronun üst kenarının
        alt kenardan yüksekliği piksel olarak okunur.
BEKLENEN
        G0    G1    G2    G3    G4    G5    G6    G7
        240   240   286   330   376   420   420   420   px      (± 6 px tolerans)
        0,0   0,0   3,3   6,5   9,8  13,0  13,0  13,0   m
GEÇER   her kare ≥ bir öncekinden (eşitlik serbest)
⛔ DÜŞER  herhangi bir kare bir öncekinden AŞAĞIDAysa. Kamyonla taş çıkarılmış demektir ve
          filmin bütün fizik iddiası düşer.
⚠️ En olası arıza G5 → G6 → G7'de: apron üç karede de 420 px'tir; model "bitmiş" sahnelerde
   yığını düzleştirmeye ya da temizlemeye eğilimlidir.
```

### ② DÜŞEN SU İPLİĞİ SAYISI VE YERİ — eksilen defter · ikili kapı

```
ÖLÇÜM   Her karede, cephe düzleminde ve kaya üstünde DÜŞEN SU kaç ayrı iplik hâlinde var
        ve %x kaçta.
BEKLENEN
        G0   2 iplik · %x 25,00 ve 75,00 · 1634 px boy · KAYAYA iner
        G1   1 iplik · %x 93,59 · kahverengi · geçici oluktan
        G2   1 · G3  1 · G4  1 · G5  1 · G6  1   ← aynı jet, aynı yer, aynı renk
        G7   2 iplik · %x 21,33 ve 78,67 · 878 px boy · KESME TAŞTAN iner
             ⭐ ve %93,59 BOŞTUR
GEÇER   sayı ve yer tam tutuyorsa
⛔ DÜŞER  ⓐ G1–G6'nın herhangi birinde cephe üstünde su varsa (suyun kesilmesi bu filmin DİRENCİ'dir)
          ⓑ G7'de üçüncü bir iplik varsa
          ⓒ G7'de kahverengi jet hâlâ akıyorsa
⭐ İKİ DEFTER BİRBİRİNİ AÇIKLAR: su kesildiği için taş oyulabildi, taş oyulduğu için apron büyüdü.
   İkisi tek karede birlikte okunduğunda film kendi kendini anlatır — başlık gerekmez.
```

---

## 2. ⭐ G7'NİN İKİ TEK-KARE KANITI — kapak bunun üstünde duruyor

### KANIT ① — AYNI TAŞ, İKİ YERDE (renk eşitliği)

```
ÖLÇÜM   G7'de üç bölgenin ortalama parlaklığı (L*) alınır:
        Ⓐ oyma cephe bandı            x %30–45 · y %45–60   (sütun gövdeleri hariç, teras arkası hariç)
        Ⓑ apron üst yüzeyi            x %40–60 · y %13–21
        Ⓒ dokunulmamış kayalık        x %5–12 · y %45–60    (sol payanda)
BEKLENEN
        Ⓐ ≈ Ⓑ   (fark ≤ %12 · ikisi de TAZE KESİK bazalt, aynı gün açılmış)
        Ⓐ ≥ 1,8 × Ⓒ   ve   Ⓑ ≥ 1,8 × Ⓒ   (taze kesik, yıllanmış kayadan belirgin AÇIK)
⭐ NE KANITLIYOR: cephe ile apron AYNI TAŞTIR. İzleyici bunu cümleye dökmez ama görür —
   ve kütle dengesi kapakta, tek karede, hiçbir yazı olmadan okunur.
⛔ DÜŞER  Ⓑ, Ⓒ'ye yakınsa: model apronu "doğal moloz" olarak boyamıştır ve defter görünmez olur.
          Ⓐ, Ⓒ'ye yakınsa: model cepheyi "eski bir tapınak" olarak boyamıştır — film o anda
          bir KEŞİF filmine döner, bir YAPIM filmi olmaktan çıkar. ⭐ Bu, filmin en büyük riskidir.
```

### KANIT ② — TANIK BLOKLARI (aynı yer kanıtı)

```
ÖLÇÜM   x −26,00 m · d 70,00 m · %x 12,86 · alt sol çeyrek. İki blok: 6,00 m (93 px) · 5,00 m (77 px).
BEKLENEN
        G0   iki blok YEŞİL SUYUN içinde, çevresi ıslak ve koyu, üstleri sırılsıklam
        G7   AYNI İKİ BLOK, AYNI PİKSELDE (±4 px), KURU, apronun saçağı sol kenarlarına dayanmış
GEÇER   merkez koordinatları sekiz karede ±4 px içinde sabit
⛔ DÜŞER  bloklar yer değiştirmişse (kamera oynamıştır) ya da G7'de tamamen gömülmüşse
          (apron kadrajın soluna taşmıştır — şev açısı 35°'yi aşmıştır)
```

---

## 3. ⭐ G6 = G7 KAPAK KİLİDİ — sert eşitlik

```
G6 ile G7 arasında 8 saniye vardır ve o sürede İNSAN ELİ HİÇBİR ŞEYE DOKUNMAZ.
İKİ KARE ŞU ALTI ŞEYDE BİREBİR AYNI OLMALI (piksel farkı ≤ 2 px):
  ① cephe geometrisi — altı sütun ekseni, üç teras kotu, kemer açıklığı, arşitrav, 14 diş
  ② apron — üst kenar 420 px, dozer izleri, kesme basamak, iki havuz ağzı ve kesme taş rimleri
  ③ dozer ve yanındaki tek figür — aynı yer, aynı duruş, sırt kameraya
  ④ eşikteki çelik oluk, trestleleri, boş cıvata yuvaları, sıyrık
  ⑤ ışık — az 275,77 · el 5,55; gölgelerin uzunluğu ve yönü AYNI
  ⑥ iki kaya payandası, tanık blokları, kaya tepesi konturu
DEĞİŞEN YALNIZ ÜÇ ŞEY:
  ⓐ iki oluk ve iki konsol ağzı dolar → 878 px'lik iki beyaz düşey belirir
  ⓑ iki havuz dolar, rimler ıslanır, sis kalkar, konsolların altındaki taş koyulaşır
  ⓒ %93,59'daki kahverengi jet durur
KOŞU    bash araclar/zincir_kontrol.sh g6.jpg g7.jpg   → yalnız bu üç bölgede fark beklenir
⛔ Dördüncü bir fark varsa kapak kanıtı düşer [DERS 30] ve G7 yeniden üretilir.
```

---

## 4. KADRAJ KİLİTLERİ — sekiz karede, ±2 px [sahip kararı 19.09.2026]

```
ÖNCE ÜÇ NİRENGİYE BAK — bu filmde kolaydır, çünkü kadrajda kayadan başka kalıcı hiçbir şey yok
ve kaya değişmez:
  ① sol kaya payandası     %x 7,69   tepeden dibe
  ② sağ kaya payandası     %x 92,31  (geçici oluk bunun ÖNÜNDEN geçer, DEĞMEZ)
  ③ kaya tepesi konturu    %97,60    üstünde 46 px gök
Üçü tutmuyorsa hiçbir başka ölçüm yapılmaz — kare yeniden üretilir.

SONRA YAPI KİLİTLERİ:
  cephe sol/sağ kenar     %x 23,08 / 76,92      582 px en
  sütun eksenleri         %x 25,00 · 30,77 · 36,54 · 63,46 · 69,23 · 75,00   Ø 42 px
  kemer ayakları          %x 42,31 / 57,69      166 px açıklık
  cephe tabanı / TAÇ      %41,35 / %64,42       415 px boy
  saptırma eşiği          %93,27
  vadi tabanı             %12,50
  ⭐ ŞELALE ÇİZGİLERİ (G7) %x 21,33 / 78,67      36 px en · 878 px boy
TOLERANS  ±2 px. ⚠️ Bu eşik sahip kararıdır ve pilot ölçümüne kadar yeniden açılmaz.
```

---

## 5. ⭐ YÜK YOLU KAPISI — ⛔ VİNÇ YOK, TAŞ DÜŞER

```
Bu filmde hiçbir karede VİNÇ yoktur ve "crane" kelimesi hiçbir prompta girmemiştir (doğrulandı).
Sebep FİZİKSELDİR: 118 m'lik bir duvara bom uzanamaz.
KESİLEN TAŞIN YOLU:   kaya yüzü → (serbest düşüş) → apron → ekskavatör/dozer → serilir
ÇELİĞİN YOLU:         eşik yolu → el → trestle (oluk) · eşikten sarkan sapan → asılı sahanlık
⛔ DÜŞER  ⓐ herhangi bir karede vinç, kule vinci ya da bomlu makine görünürse
          ⓑ herhangi bir karede kamyon kadrajdan TAŞ ÇIKARIRSA ya da kadraja TAŞ GETİRİRSE
          ⓒ asılı sahanlık taşıyıcısız asılıysa (sapan/tel görünmüyorsa) [DERS 46]
⚠️ Makine listesi kapalıdır: iki ekskavatör · bir dozer · bir yükleyici · eşikte bir palanga.
   Beşinci bir makine türü ⑦ merceğinde KALABALIK sayılır [C1-d].
```

---

## 6. IŞIK VE GÖLGE KAPISI

```
Cephe normali 195°. Her karede gölge YÖNÜ ve UZUNLUĞU tablodan doğrulanır:

  kare  saat    azimut   yükseklik   gölge yönü   tanθ     cephe aydınlık katsayısı
  G0   06:00    84,23     5,55       ⛔ gölge yok   —       0,000   soğuk mavi, yüz KARANLIK
  G1   08:00   105,87    26,93       sol           −65,85   0,014   yalnız kenar ışığı
  G2   10:00   135,03    45,53       sol            −1,73   0,351
  G3   12:00   180,00    54,00       sol            −0,27   0,568   gölgeler EN KISA
  G4   14:00   224,97    45,53       sağ            +0,58   0,607   ⭐ EN PARLAK KARE
  G5   16:00   254,13    26,93       sağ            +1,67   0,457
  G6   18:00   275,77     5,55       sağ            +6,15   0,160   ⭐ yalama: sütun SOL kenarı
  G7   18:00   275,77     5,55       sağ            +6,15   0,160   G6 ile AYNI

⛔ DÜŞER  ⓐ G0'da cephede güneş varsa (θ = −110,77°, fiziksel olarak imkânsız)
          ⓑ gölge yönü G3 ile G4 arasında TERSİNE DÖNMÜYORSA (sol → sağ) — bu filmin saatidir
          ⓒ G6 ile G7'nin gölgeleri farklıysa (rejim G'de ışık donar)
⭐ GÜNEŞ HİÇBİR KAREDE KADRAJDA DEĞİL: kadraj az 348,43° … 41,57°, güneş 84,23° … 275,77°.
   Kadrajda güneş diski ya da lens parlaması görünüyorsa kare düşer.
```

---

## 7. SAYIM KAPISI [DERS 55]

```
Her karede: bir kayalık · bir oyma cephe · bir apron · (G1–G6'da) bir geçici oluk.
⛔ DÜŞER  ikinci bir oyma · ikinci bir apron · üçüncü bir şelale · karşı yamaçta ikinci bir şantiye ·
          vadiye atılmış bir yol/köprü · kayalığın tepesinde bir yapı
⚠️ EN OLASI ARIZA: G5 ve G6'da cephe bitmiş ve ekipman kalkmıştır; model boşluğu DOLDURMAK ister.
   Üç negatif cümle bunu kapatıyor ("the cut stays inside the face" · "no third fall is ever cut" ·
   sayım cümlesi) ama ölçümde bu iki kareye AYRICA bakılır.
```

---

## 8. REJİM G KAPISI — S6 (48,0 – 56,0)

```
⭐ SÜRE UYDURULMADI: 61,00 m serbest düşüş = √(2·61/9,81) = 3,53 sn. Bu bir yerçekimi sabitidir.
ÖLÇÜM   İlk suyun konsol ağzından ayrıldığı kare ile havuza çarptığı kare arasındaki süre.
BEKLENEN 3,53 sn ± 0,25 sn   (30 fps'te 106 ± 8 kare)
GEÇER   ⓐ süre tutuyor ⓑ jet ilk ~15 m'de bütün, sonra beyaz sise dağılıyor (15 m = 216 px)
        ⓒ gölgeler HİÇ kımıldamıyor ⓓ pus donmuş ⓔ dozer ve figür HİÇ hareket etmiyor
        ⓕ figürün sırtı kameraya dönük, 35 px, yüz okunmuyor [DERS 15 · P14-d]
⛔ DÜŞER  ⓐ su 2,0 sn'den kısa ya da 5,0 sn'den uzun sürede iniyorsa (rejim sızmış)
          ⓑ figür yürüyorsa ya da dönüyorsa
          ⓒ gölge süpürmesi varsa (rejim B sızmış — en olası arıza)
```

---

## 9. SES KAPISI — MÜZİKSİZ · ⭐ DEFTER TUTAN YATAK

```
⛔ MÜZİK YOK — hiçbir sahnede, hiçbir saniyede [sahip kuralı 21.09.2026].
ÖLÇÜLEN ÜÇ ŞEY:
  ① ⭐ İLK SES = SON SES.  0,0–3,0 arası iki şelalenin sesi ile 53,0–56,0 arası iki şelalenin
     sesi AYNI SEVİYEDE olmalı (± 2 dB LUFS). Aynı debi, aynı düşü, aynı kaya.
     ⛔ Son şelale daha SESSİZSE defter sesle yalanlanmış olur.
  ② ⭐ SESSİZLİK PENCERESİ 49,5 – 53,0 (3,53 sn). Su havadadır ve düşen su ses çıkarmaz.
     Yalnız rüzgâr + oluk ağzındaki akış hışırtısı. ⛔ Bu pencereye herhangi bir vuruş,
     müzik, "whoosh" ya da yükselen ton girerse film düşer.
  ③ 16,0 – 40,0 arası her 2–3 saniyede bir TAŞ DÜŞÜŞÜ: kopma → ~2 sn boşluk → apronda gümbürtü.
     Bu gümbürtü defterin sesidir; sayısı apronun büyümesiyle orantılı olmalı.
⛔ Anlatıcı yok · konuşma yok · sesli imza yok · kütüphane "dramatic" efekti yok.
```

---

## 10. ZAMAN VE IŞIK GÜNÜ

```
IŞIK GÜNÜ  6 × rejim B (2,00 sa) + 1 × rejim G (0) = 12,00 sa   ✅ tavan 14,00 sa
PENCERE    06:00 → 18:00 · 44°K · δ +8° · gündüz 13 sa 02 dk (05:29 – 18:31)
PAY        doğuşa 31 dk · batışa 31 dk
⛔ DÜŞER   herhangi bir karede gök rengi / güneş yüksekliği tabloyla çelişiyorsa
⚠️ MEVSİM KİLİTLİ: δ +8° (geç yaz). İlkbahar ekinoksunda 18:00 güneşi ufkun altındadır ve
   S5 ile S6 çekilemez. Mevsim değişirse istasyon değil TAKVİM yeniden hesaplanır [P13-e].
```

---

## 11. BİLİNEN RİSKLER — üretimden önce okunur

```
① ⭐ EN BÜYÜK RİSK: "KEŞİF FİLMİ"NE DÖNME. Model, kaya oyma bir cepheyi ANTİK bir harabe olarak
   boyamaya çok yatkındır (Petra, Ellora refleksi). O anda film bir YAPIM filmi olmaktan çıkar.
   SAVUNMA: §2 Kanıt ①'in renk eşitliği (taze kesik ≥ 1,8 × yıllanmış kaya) + her karede taze
   keski izleri + apronun aynı renkte olması. PİLOT: S4 (G4 → G5).
② MODELİN "YAPI BÜYÜR" ALIŞKANLIĞI. S2'de yapı büyümez, ÇEVRESİ eksilir. Sütunlar duvara
   eklenirse film düşer. İkinci pilot budur.
③ SUYU GERİ GETİRME EĞİLİMİ. Model bir şelaleyi "kaldırmayı" sevmez; G1–G6'da cepheye su
   sızdırabilir. §1②'nin ikili kapısı bunu yakalar.
④ APRONUN TEMİZLENMESİ. G5–G7 "bitmiş" karelerdir; model moloz yığınını düzleştirebilir.
   §1① monoton artış kapısı bunu yakalar.
⑤ 25 PİKSEL SINIRI. İşçi 35 px, geçici oluk 22 px. Bunların altındaki hiçbir şey kanıt
   nesnesi olamaz ve prompta yazılmadı [karar ⑦]. Ölçümde küçük ayrıntı ARANMAZ.
⑥ REJİM B SIZMASI S6'ya. Beşinci kez rejim G finali; model alışkanlıkla gölge süpürtebilir.
⑦ ⛔ ARAÇ KUTU SETİ ÖLÇÜLMEDİ — üretim açılamaz [ARAC_KARTLARI §4 · DERS 23].
⑧ ⚠️ P13-h bulgusu açık: eksiltmeli işte modelin "geri koyma" eğilimi ölçülmedi; bu film
   depoda ikinci eksiltmeli filmdir ve ilk BÜYÜK ÖLÇEKLİ olanıdır.
⑨ ⚠️ 16:9 kadraj hesabı bu filmde KULLANILMADI (dikey). Ama tilt-0 dikey cephe hesabı depoda
   ilk kez bu ölçekte (138,67 m kadraj boyu) koşuyor — ① koşusu formülü doğrulamalı.
```
