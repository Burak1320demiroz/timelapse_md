# 🔬 BACK TO PLUMB — QA ŞARTNAMESİ

```
FİLM       BACK TO PLUMB · 7 × 8,0 = 56,0 sn · 8 görsel + 7 I2V + 0 T2V
DEFTER     cins SAPMA (px) — deponun 6. defter cinsi · 64,6 → 0,0 px, yedi adım
DURUM      ⛔ ÜRETİLMEDİ — bu şartname üretimden ÖNCE yazıldı ve üretimi KOŞULLAR
⭐ BU FİLMİN AYRIMI: defter bir MESAFE değil, bir SAPMA ölçüyor. Sapmanın referansı kadrajın
   kendi düşeyidir. Bu yüzden bu şartnamenin ilk kapısı görüntünün İÇİNDEKİ bir şey değil,
   KADRAJIN KENDİSİDİR (§2). Kadraj yalansa defter de yalandır ve kurtarma yolu yoktur.
```

> Sıra ÖNEMLİDİR: §2 (ROLL) geçmeden §1 (DEFTER) ÖLÇÜLMEZ. Bir karede roll kapısı düşerse
> o karenin defter değeri kaydedilmez — 'yaklaşık' diye not edilmez, hiç yazılmaz.

---

## §2 ⛔ ROLL KAPISI — ÖNCE BU. Filmin tek ölüm kalım ölçümü

```
NEDEN ÖNCE   Şapkanın ucu kadraj merkezinin 563 px üstündedir. Kadraj θ kadar dönerse yatayda
             563 · tan θ px YALANCI kaçıklık doğar ve defter bunu gerçek kaçıklıktan AYIRT EDEMEZ:
                roll 0,2° → 1,97 px      0,5° → 4,9 px      1,0° → 9,8 px = bir sahne adımının TAMAMI

YÖNTEM       ⛔ Ölçüm KULEDEN YAPILMAZ — kule zaten yatıktır. İki dış düşey kullanılır:
                ① solda tek ahşap direk    x% 10,0 = 108 px
                ② sağda ahırın köşesi      x% 82,0 = 886 px
             Her birinin üst ve alt ucunun x'i okunur, px eğimi hesaplanır, ikisi KARŞILAŞTIRILIR.

GEÇME        ⛔ ① ve ② ayrı ayrı DÜŞEY olmalı: |Δx| ≤ 1 px, uçtan uca.
             ⛔ Ayrıca ahır saçağı YATAY olmalı: 1054 px'te, |Δy| ≤ 2 px soldan sağa.
             ⛔ İki düşeyin eğim farkı ≤ 2,71 px (ölçüm tabanı 778 px, roll 0,2°'ye karşılık gelir).

DÜŞME        ⛔ KARE ISKARTADIR. ⛔ DÖNDÜRÜLEREK KURTARILMAZ — döndürme defterin ölçtüğü şeyi de
             döndürür ve hatayı görünmez yapar, yok etmez. Kare YENİDEN ÜRETİLİR.
⛔ AYRICA     hiçbir aşamada yazılım stabilizasyonu, otomatik ufuk düzeltme, lens profili ya da
             perspektif düzeltme uygulanmaz; hepsi kadrajı döndürür ya da ölçekler.
⚠️ EN SİNSİ HÂLİ: model kadrajı döndürmez ama KULEYİ dikleştirip AHIRI eğer. İki düşey bu yüzden
   ayrı ayrı ölçülür — tek düşey bu hatayı yakalamaz.
```

---

## §1 ⭐ DEFTER KAPISI — filmin tamamı bu ölçümde

```
ÖN KOŞUL  §2 geçilmiş olmalı.
TANIM     Aynı karede iki x koordinatı:
             ① taban halkasının ORTASINDAN inen düşeyin x'i
             ② konik şapkanın UCUNUN x'i
          DEFTER = ② − ① (işaretli px; pozitif = sola yatık)

⭐ ① NASIL BULUNUR (tartışmasız olmalı, yoksa defter gürültüdür):
   Taban halkasının kadrajda görünen SOL ve SAĞ dış kenarları okunur, ortası alınır.
   ⛔ Halka sekiz karede de AYNI pikselde durur (247 px eni) — bu §7'nin kilidi.
   ⛔ Kaldırma halkayı DEĞİL, kulenin gövdesini yükseltir: halka kuyunun içinde kalır ve kımıldamaz.
⭐ ② NASIL BULUNUR: konik şapkanın tepe noktası. Düz öğlen ışığında (G2–G3) silindirin kenarları
   yumuşar ama UÇ NOKTA yumuşamaz — nokta bir kenar değildir. Bu yüzden defterin üst noktası
   şapkanın ucudur, gövdenin kenarı değil.
```

| kare | saat | ⭐ beklenen DEFTER | tolerans | derece | kama px | ölçülen | sonuç |
|:-:|---|---:|---:|---:|---:|:-:|:-:|
| G0 | 07:00 | **64,6 px** | ±2 px | 5,00° | 0 | | |
| G1 | 09:00 | **55,0 px** | ±2 px | 4,26° | 4 | | |
| G2 | 11:00 | **46,0 px** | ±2 px | 3,56° | 8 | | |
| G3 | 11:10 | **37,0 px** | ±2 px | 2,86° | 11 | | |
| G4 | 13:10 | **27,0 px** | ±2 px | 2,09° | 15 | | |
| G5 | 15:10 | **18,0 px** | ±2 px | 1,39° | 19 | | |
| G6 | 15:20 | **9,0 px** | ±2 px | 0,70° | 23 | | |
| G7 | 15:30 | **0,0 px** | ±2 px | 0,00° | 26 | | |

```
⛔ İKİ YASA
   ① DEFTER HİÇBİR SAHNEDE ARTMAZ. Sekiz değerin dizisi kesinlikle azalandır.
      ⚠️ Bir karede artış görülürse ÖNCE §2 tekrar koşulur — en olası sebep roll'dür, kule değil.
   ② DEFTER EKSİYE GEÇMEZ. G7 = 0,0 px SON değerdir; eksi, kuleyi öbür yana yatırmaktır.
⛔ G7 ÖZEL: |② − ①| ≤ 2 px. Bu ölçüm tutmazsa film YOKTUR — başlık yalan olur.
⛔ ADIM KAPISI: ardışık iki kare arasındaki fark 7–12 px olmalı (plan 9–10 px).
   < 7 px  → sahne 'durmuş' okunur, defter ölçülemez hâle gelir
   > 12 px → kule o sahnede fazla dönmüştür; çatlak riski (§3) ve fizik yalanı
⚠️ ÖLÇÜM GÜRÜLTÜSÜ: her iki x'te ±1 px → defterde ±2 px. En küçük adım 9,0 px = gürültünün 4,5 katı ✅
   ⛔ Ama roll 0,2° tek başına 1,97 px yalancı kaçıklık üretir: adımın beşte biri. §2 bu yüzden ÖNCEDİR.
```

---

## §3 ⛔ ÇATLAK KAPISI — deponun ilk 'DEĞİŞMEMESİ GEREKEN' ölçümü

```
NE       Kulenin yüksek (gerilme) yanında, kapının üstünde duran eski düşey çatlak.
         genişlik 0,06 m = 4,6 px · 2,10 m ile 5,40 m kotları arası · boyu 295 px
NEDEN    ⭐ Bu film bir şeyi DÜZELTİYOR. Düzeltmenin başarılı olup olmadığını defter söylemez —
         defter yalnız kulenin dikleştiğini söyler. Kulenin YARILMADIĞINI yalnız çatlak söyler.
         57 tonluk donatısız bir tuğla gövdeyi tek yandan kaldırdığınızda gerçek risk budur.

ÖLÇÜM    Çatlağın genişliği ÜÇ kotta okunur: alt uç, orta, üst uç. Sekiz kare × üç kot = 24 ölçüm.
GEÇME    ⛔ 24 ölçümün hepsi 4,6 px ± 1 px. ⛔ Dizide EĞİLİM OLMAMALI — G0'dan G7'ye monoton bir
         büyüme, tek tek ölçümler toleransta olsa bile DÜŞÜRÜR (üç kotun ortalaması regresyona sokulur,
         eğim |a| ≤ 0,15 px/kare olmalı).
DÜŞME    ⛔ Çatlak büyüyorsa OPERASYON BAŞARISIZDIR ve film düşer: kule doğrulmuş ama yarılmıştır.
         ⚠️ Bu 'kozmetik' bir hata değildir; filmin iddiasının tersini kanıtlar.
⚠️ EN OLASI MODEL HATASI (PİLOT 3ⓑ): model çatlağı 'çalışan bir detay' sanıp kareden kareye
   büyütür, çünkü çevresindeki her şey değişmektedir. Prompt tarafındaki savunma ikilidir:
   ① sekiz AT THIS STAGE'te de BİREBİR aynı cümle ② NEGATIVE'de açık kilit ('never widens and
   never closes'). Yine de ölçüm ZORUNLUDUR — metin savunması yeterli sayılmaz.
```

---

## §4 ⭐ KAMA KAPISI — defterin harcanan karşılığı

```
NE       Kulenin altında, alçak yanda biriken yeni tuğla bandı. Bir ucu kalın, öbür ucu sıfır.
NEDEN    ⭐ Defter tek başına bir NUMARA olabilir: kule dikleşmiş görünür ama neden dikleşti?
         Kama o sorunun kadrajdaki cevabıdır ve ⛔ FİZİKSEL OLARAK defterin karşılığıdır:
         kalkış = 0,2800 m = 3,20 × tan 5,00° ve kama o boşluğu doldurur.

ÖLÇÜM    Kamanın KALIN UCU (kulenin sol kenarında) dikey px olarak okunur.

| kare | beklenen kama | tolerans | kalkış (m) | adım | ölçülen |
|:-:|---:|---:|---:|---:|:-:|
| G0 | 0 px | ±2 px | 0,0000 | — | |
| G1 | 4 px | ±2 px | 0,0417 | +3,9 px | |
| G2 | 8 px | ±2 px | 0,0808 | +3,7 px | |
| G3 | 11 px | ±2 px | 0,1199 | +3,7 px | |
| G4 | 15 px | ±2 px | 0,1632 | +4,1 px | |
| G5 | 19 px | ±2 px | 0,2022 | +3,7 px | |
| G6 | 23 px | ±2 px | 0,2411 | +3,7 px | |
| G7 | 26 px | ±2 px | 0,2800 | +3,7 px | |

⛔ ÜÇ KURAL
   ① KAMA HİÇBİR KAREDE İNCELMEZ. Dizi kesinlikle artandır (0 → 26 px).
   ② KAMA UZAK YANDA SIFIRA İNER. Sekiz karede de bir KAMA'dır — paralel bir bant DEĞİLDİR.
      ⚠️ Model bunu en çok kaçıran yerdir: eşit kalınlıkta bir sıra çizer ve kule 'yükseltilmiş'
      görünür, 'döndürülmüş' değil. ⛔ Paralel bant = kare ıskartadır.
   ③ ⭐ ÇAPRAZ TUTARLILIK: kama px ile defter px aynı fiziğin iki yüzüdür. Her karede
      kalkış = 3,20 × (tan 5,00° − tan(asin(defter_px / 77,14 / 9,60))) hesaplanır ve
      kama_px = kalkış × 93,99 ile karşılaştırılır. ⛔ Fark ≤ 3 px olmalı.
      Bu kapı, defteri ve kamayı ayrı ayrı 'güzel' ama birbiriyle çelişkili üreten kareleri yakalar.
```

---

## §5 ⭐ BIRAKMA KAPISI — filmin son vuruşu ve tek elastik ölçümü

```
NEREDE   S6 klibi, 3,0 – 5,5 saniye (rejim A · 75×) — altı kriko sırayla boşaltılır.
NE OLUR  Kule 57 tonluk ağırlığını krikolardan yeni tuğla kamaya devreder. Gerçekte bu devirde
         harç sıkışır ve kule bir miktar GERİ OTURUR. Bu gerçektir ve gizlenmez.

ÖLÇÜM    Defter, boşaltmanın hemen ÖNCESİNDE (klip 3,00 sn) ve hemen SONRASINDA (klip 5,50 sn)
         okunur. Fark = elastik geri dönme.
GEÇME    ⛔ Geri dönme ≤ 2 px. Ve ⛔ G7'nin kendisi 0,0 px ± 2 px olmak zorundadır (§1).
DÜŞME    ⛔ > 2 px → kamanın harcı henüz taşımıyor demektir; G7 ıskartadır ve klip yeniden üretilir.
         ⚠️ Bu durumda ÇÖZÜM 'defteri G6'da bitirmek' DEĞİLDİR — filmin son vuruşu bırakmadır.

⭐ AYRICA BİR ANLATI KAPISI: son 2,5 saniyede (5,50 → 8,00) ⛔ HİÇBİR ŞEY İNŞA EDİLMEZ.
   Kadrajda yalnız geri çekilen ustalar, boşalmış krikolar ve AÇIK KALAN altı kuyu vardır.
   ⛔ Kuyular kapatılmaz, avlu süpürülmez, krikolar toplanmaz. İş bitti; avlu bitmedi.
```

---

## §6 G6 = G7 KİMLİĞİ — kapak kilidi

```
G7 kapağın tek kaynağıdır. G6 ile arasında YALNIZ ÜÇ FARK olabilir:
   ⓐ şapkanın ucu 9 px sağa gelir (defter 9,0 → 0,0)
   ⓑ kama bandının kalın ucu 23 → 26 px
   ⓒ krikolar YÜK ALTINDAN BOŞA geçer; ikisi çıkarılıp çakıla yatırılır
⛔ BUNLAR DIŞINDA HER ŞEY AYNI PİKSELDE: ahır saçağı ve köşesi, ahşap direk, kapı sövesi,
   kule tabanı ve eni, altı kuyu ağzı, payanda istifi, el arabası izleri, harç lekeleri, ÇATLAK.
YÖNTEM  G6 ve G7 üst üste bindirilir; fark maskesi ⓐⓑⓒ'nin dışında hiçbir yerde ışımamalıdır.
⚠️ ⭐ Bu filmde ⓐ YALNIZCA 9 px'tir. Fark maskesi neredeyse boş çıkacaktır ve bu DOĞRUDUR:
   filmin son sahnesi kadrajda en az şeyin değiştiği sahnedir. ⛔ Bu bir hata sanılıp
   'daha fazla fark' eklenmez.
```

---

## §7 ±2 PX KİLİTLERİ — üç nirengi ve kulenin kendisi

```
│ ahır saçağı           1054 px = %54,90   ⛔ ±2 px · düz ve yatay
│ ⛔ ahır köşesi         x% 82,0 = 886 px · DÜŞEY (roll çapası ①)
│ ⛔ ahşap direk         x% 10,0 = 108 px · DÜŞEY (roll çapası ②)
│ taş kapı sövesi       x% 90,0 · I2V 'aynı kadraj eni' çapası
│ ⭐ kule tabanı         676 px · ⛔ SEKİZ KAREDE AYNI — kaldırma halkayı yükseltmez
│ ⭐ kule eni            247 px · ⛔ SEKİZ KAREDE AYNI — kule ne büyür ne küçülür
│ kule boyu             847 px (taban → şapka ucu) ⛔ ±2 px
│ gövde tepesi          1457 px — konik şapkanın başladığı kot
│ kapı boşluğu          69 × 177 px
│ ⛔ ÇATLAK              4,6 px (§3)

⚠️ ⭐ KULE BOYU BİR TUZAKTIR. Kule dikleştikçe GERÇEKTE kadrajdaki boyu artar (yatık bir çubuğun
   izdüşümü kısadır). Ama artış 9,60 m × (1 − cos 5,00°) = 0,0365 m = 3,43 px'tir — ölçüm toleransının
   içinde kalır ve bu yüzden 'kule boyu sabit' kilidi geçerlidir. ⛔ Yine de yukarı doğru 4,0 px'ten
   fazla bir artış GERÇEK DEĞİLDİR: model kuleyi uzatıyordur.
```

---

## §8 ÇAPRAZ DEFTER — gölge (ikinci saat) ve İKİ REJİM KAPISI

```
Defteri KRİKO yürütür, gölgeyi GÜNEŞ. İkisi hiç karışmaz ve rejimi bu ayrım okutur.

kare  saat   güneş az/el   gölge boyu   yan bileşen   sahne   rejim   defter adımı   gölge kayması
G0    07:00  104° /  8°     69,2 m     −57,6 m       —       —            —              —
G1    09:00  127° / 28°     17,8 m      −9,7 m       S0      B       −9,6 px        47,8 m
G2    11:00  160° / 42°     10,7 m      −0,1 m       S1      B       −9,0 px        9,7 m
G3    11:10  163° / 43°     10,4 m       0,5 m       S2      A       −9,0 px        0,6 m
G4    13:10  203° / 41°     10,9 m       7,5 m       S3      B       −10,0 px        7,0 m
G5    15:10  235° / 27°     19,0 m      18,4 m       S4      B       −9,0 px        10,9 m
G6    15:20  238° / 25°     20,4 m      19,9 m       S5      A       −9,0 px        1,5 m
G7    15:30  240° / 24°     22,0 m      21,6 m       S6      A       −9,0 px        1,7 m

⛔ İKİ REJİM KAPISI [SANTIYE_HAREKETI §1]
   B sahneleri (2 sa · 900×): gölgenin yan bileşeni ⛔ 3,0 m'den FAZLA kaymalı
   A sahneleri (10 dk · 75×): gölgenin yan bileşeni ⛔ 2,0 m'den AZ kaymalı
   ⛔ İki koşul aynı anda tutmuyorsa model güneşi kendi saatinde akıtıyordur [DERS 15] ve
      TIME RATE cümlesi sertleştirilir.
⭐ EN KESKİN SINAV S2'dir (11:00 → 11:10): gölge 0,6 m kayar, defter 9 px yürür.
   Seyirci burada 'zaman durdu ama iş yürüdü' diye okur. Ölçüm bunu doğrulamak zorundadır.
⚠️ GÖLGE KADRAJI TERK EDER (G0 sol, G5–G7 sağ). Bu SORUN DEĞİLDİR — kadrajın içinde her zaman
   ölçülebilir başka gölgeler vardır: ahır saçağı, kapı sövesi, ahşap direk, kuyu ağızları.
   ⛔ Sekiz karenin sekizinde de en az bir keskin gölge kenarı bulunmalıdır.
```

---

## §9 SAYIM KAPISI

```
This is one leaning brick tower being brought back to plumb in one farmyard beside one long barn, and nothing else being worked on.
Kadrajda sayılabilir yedi şey vardır ve sekiz karede sayıları DEĞİŞMEZ:
  1 kule · 1 ahır · 1 ahşap direk · 1 taş kapı sövesi · 1 kapı boşluğu · 2 yüksek delik · 6 kuyu
⛔ Kuyu sayısı S1'de 6'ya ulaşır ve bir daha değişmez; S0'da 2'dir ve bu TEK istisnadır,
   çünkü kuyular o sahnede AÇILMAKTADIR (aşama merdiveninde yazılı).
⛔ İKİNCİ BİR KULE, ikinci bir ahır, ikinci bir direk, arka planda bir kasaba ya da başka bir
   şantiye ASLA görünmez. Ova boştur ve boş kalır.
```

---

## §10 SES KAPISI — tam diegetik, AÇIK ALAN

```
⛔ MÜZİK YOK — 0,0'dan 56,0'ya tek nota yok [sahip kuralı 21.09.2026].
⭐ İMZA: el pompasının SAYILABİLİR tırtılı. Her tıkırtı defterde bir kesirdir.
⛔ AKUSTİK KAPISI: ova açıktır, yankı YOKTUR. Herhangi bir vuruşun kuyruğu ölçülür;
   ⛔ RT60 > 0,25 sn ise kayıt kapalı mekândandır ve sahayı yalanlar — teslim edilmez.
⛔ BIRAKMA SESİ (S6 · 3,00–5,50): tek bir tok oturma sesi ve çok hafif bir tuğla gıcırtısı.
   ⛔ ÇATLAMA SESİ EKLENMEZ — çatlama bu filmde BAŞARISIZLIĞIN sesidir ve §3'ü yalanlar.
⛔ Son 2,5 saniye sesin de en boş yeridir: uzakta traktör, rüzgârda anız, bir kova.
```

---

## §11 ZAMAN VE IŞIK GÜNÜ

```
PENCERE     07:00 → 15:30 = 8 sa 30 dk
IŞIK GÜNÜ   4 × B (2,00 sa) + 3 × A (0,167 sa) = 8 sa 30 dk ≤ 14 ✅
GÜN         11 sa 25 dk (41°N · δ −5°) · doğuş 06:17 · batış 17:43
PAY         başta 0,71 sa, sonda 2,21 sa
⛔ REJİM SAYISI 2 (A ve B) — tavan iki [SANTIYE_HAREKETI §1] ✅
⛔ REJİM G (gerçek zaman) YOKTUR — final sahnesi de 75×'tir. Bırakma anı gerçek zamanda
   3,1 dakika saniye sürer ve klipte 2,5 saniyeye sığar.
⛔ GÜNEŞ KADRAJDA YOK: azimut 104° → 240°, kadraj 313,4° … 6,6°. En yakın yaklaşma 73°.
```

---

## §12 ON RİSK — sırayla, en büyükten

```
①  ⛔ ROLL (§2). Tek ölüm kalım koşulu, kurtarma yolu YOK. Her karede ÖNCE ölçülür.
②  ⛔ ÇATLAK BÜYÜMESİ (§3). En olası model hatası; yakalanmazsa yedi klip birden düşer.
③  ⛔ KAMANIN PARALEL ÇİZİLMESİ (§4②). Kule 'yükseltilmiş' görünür, 'döndürülmüş' değil —
    ve o zaman film başka bir şey anlatır.
④  ⚠️ FİNALİN GÖRSEL SESSİZLİĞİ. Deponun en zayıf kapak karesi; ölçüldü, kabul edildi,
    üç azaltıcısı plana yazıldı. ⛔ Kırpma ya da kontrast itmesiyle KURTARILMAZ.
⑤  ⚠️ ALTI KRİKONUN EŞZAMANLILIĞI. Sırayla çalışan krikolar kuleyi eğer ve çatlatır;
    S2 klibi bunun tek sınavıdır.
⑥  ⚠️ KULENİN DÖNMESİ. Model 'yatıklığı düzeltmeyi' gövdeyi kendi ekseninde çevirerek
    yapabilir. Kapı boşluğu ve iki yüksek delik sekiz karede AYNI x'te kalmalıdır.
⑦  ⚠️ DÜZ ÖĞLEN IŞIĞI (G2–G3, geliş açısı < 4°). Silindirin kenarları yumuşar; şapkanın
    UCU yumuşamaz, o yüzden defter etkilenmez ama siluet etkilenir.
⑧  ⚠️ TABAN HALKASININ YÜKSELMESİ. Kaldırılan şey gövdedir; halka kuyuda kalır. Model
    halkayı da kaldırırsa §7'nin taban kilidi düşer ve fizik yalan olur.
⑨  ⚠️ ZAMAN ÖLÇEĞİ. 5,00°'lik doğrultma bir günde iyimserdir; plan bunu BEYAN eder ve
    sıkıştırmayı artırarak çözmez.
⑩  ⚠️ AVLUNUN SÜPÜRÜLMESİ. Model finali 'temiz' göstermeye eğilimlidir. ⛔ Kuyular açık,
    krikolar yerde, izler duruyor — bedel kadrajda kalır.
```

---

```
⛔ ÜRETİM AÇILMAZ: ARAÇ KUTU SETİ ölçülmedi [ARAC_KARTLARI §4].
⛔ PİLOT SIRASI: §2 ROLL → §1 G7 → §3 çatlak (S2 klibi) → kalan üretim.
⛔ Roll ve G7 ölçümü tutmadan hiçbir kare üretilmez.
```
