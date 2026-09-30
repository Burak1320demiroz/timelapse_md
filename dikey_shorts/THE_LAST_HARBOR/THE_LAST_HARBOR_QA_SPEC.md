# 🔬 THE LAST HARBOR — QA SPEC

```
⛔ Bu dosya PLANIN DEĞİL, TESLİMİN kapısıdır. Her madde TEK KAREDE ya da TEK KLİPTE ölçülür.
   Ölçülemeyen bir madde bu dosyaya yazılmaz.
KAYNAK  dikey_shorts/THE_LAST_HARBOR/THE_LAST_HARBOR_DIKEY_TIMELAPSE.md
IZGARA  7 × 8,0 = 56,0 sn · 8 görsel (G0–G7) + 7 I2V · rejim 6 × B + 1 × A
DURUM   ⛔ ÜRETİLMEDİ — hiçbir madde henüz KOŞULMADI
```

---

## 1. ⭐ KÖPÜK DEFTERİ KAPISI — filmin tek sayılabilir iddiası

```
TANIM      bir KIRIK = kadrajın alt bandında (%0 → %44,65 · 857 px) en az 30 piksel enli,
           çevresinden en az iki kat parlak, beyaz bir su lekesi
NEREDE     yalnız İÇ BANTTA sayılır. Kolun üstündeki açık deniz bandı bu sayıya GİRMEZ.
NASIL      G0–G7 karelerinin her birinde tek tek sayılır; sayım kolun iç yüzünden kadrajın dibine
           kadar bütün bandı kapsar, eski mendirek taşının üstündeki köpük SAYILMAZ

  kare      G0   G1   G2   G3   G4   G5   G6   G7
  hedef      7    7    5    4    2    1    0    0
  tolerans  ±1   ±1   ±1   ±1   ±1    0    0    0

⛔ DÜŞME KOŞULU ① bir kare kendinden öncekinden FAZLA kırık taşıyorsa o kare düşer — defter tek yönlüdür
⛔ DÜŞME KOŞULU ② G6 ya da G7'de tek bir kırık varsa film düşer: filmin bütün iddiası oradadır
⛔ DÜŞME KOŞULU ③ G0'da altıdan az kırık varsa G0 düşer — başlangıç açık deniz olmak zorundadır

ÇAPRAZ KONTROL — DIŞ BANT (kretin üstü → ufuk · 231 px, S4'ten sonra 185 px)
  G0–G3   kırılma çizgisi YOK; bant düzgün kabartı, uzun ve pürüzsüz
  G4      ⭐ ilk kırılma çizgisi görünür ve bandın ALT kenarına yakındır
  G5–G7   kırılma çizgisi bandın alt kenarında kesintisiz BEYAZ ŞERİT
⛔ DÜŞME KOŞULU ④ iç bant boşalırken dış bant da sakinleşiyorsa film düşer. Enerji yok olmaz,
   YER DEĞİŞTİRİR; iki bandın ters yönde gitmesi bu filmin fiziğidir.
```

---

## 2. İKİ TEK KARELİK KANIT

```
KANIT ① — KIRMIZI BANT (G1 karşı G2, tek kare, tek ölçüm)
   G1'de kolun iç yüzünde, su hattının (%44,65 · 857 px) hemen üstünde 90 ± 6 piksellik DONUK KIRMIZI
   bir bant vardır ve %x 15,38 ile 84,62 arasında KESİNTİSİZ uzanır.
   G2'de aynı yerde kırmızı HİÇ YOKTUR; su hattının üstü baştan sona ıslak gri betondur.
   ⛔ G2 · G3 · G4 · G5 · G6 · G7'nin herhangi birinde bir piksel kırmızı görünürse o kare düşer.
   ⭐ NEDEN BU: bu bandın tek işlevi, kutunun bir zamanlar YÜZDÜĞÜNÜ tek karede kanıtlamaktır.
      Bir rıhtımda zehirli boya bandı olmaz.

KANIT ② — AYNI 857 PİKSEL (G0 karşı G7, iki kare yan yana)
   Aynı bant, aynı pikseller, aynı istasyon:
      G0  baştan başa beyaz kırık · yedi ayrı leke · ortalama parlaklık YÜKSEK
      G7  tek kırık yok · yüzey kolun gölgesinde · iki sönen iz dışında düz
   KABUL  G7'nin iç bant standart sapması G0'ın standart sapmasının %25'inden KÜÇÜK olmalı
   ⛔ Bu iki kare bir kapak kanıtı DEĞİLDİR (kapak yalnız G7'dir) — filmin İÇİNDEKİ kanıttır ve
      LOOP satırının dayanağıdır.
```

---

## 3. ⛔ G6 = G7 KİMLİĞİ — kapak kanıtının kendisi

```
ARADA ON DAKİKA VAR VE İNSAN ELİ HİÇBİR ŞEYE DOKUNMUYOR. Altı şey BİREBİR aynı olmalı:
  ① kol: 748 ± 2 px eni · iç yüz %44,65 → %52,33 · kret üstü bandı 67 ± 3 px · parapet bandı 46 ± 3 px
  ② yakın su: sıfır kırık, kolun gölgesi baştan başa üstünde
  ③ dış köpük şeridi ve açık deniz bandı 185 ± 4 px
  ④ boş cıvata yuvaları sırası ve sapanın bıraktığı soluk sıyrık — aynı piksellerde
  ⑤ üç çapa: eski mendirek · kaya adacığı · ufuk çizgisi — ±2 px
  ⑥ geçici kaya bermi: aynı yükseklik, aynı taş dizilimi
İZİN VERİLEN ÜÇ FARK — başka hiçbiri değil:
  ⓐ fener yanar (kretin 145 ± 5 px üstünde soluk sıcak bir boncuk)
  ⓑ 9 m'lik tekne ikinci babanın altında (221 ± 6 px) ve arkasında iki sönen iz
  ⓒ genel ışık seviyesi bir miktar düşer ve parıltı bandı biraz sıcaklaşır
⛔ Dördüncü bir fark varsa kapak kanıtı düşer [DERS 30].
⭐ KOŞ:  bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png   → çıkış 0 olmalı
```

---

## 4. KADRAJ KİLİTLERİ — ±2 px [sahip kararı 19.09.2026]

```
⭐ SIRA ÖNEMLİ: önce ÜÇ ÇAPAYA bak. Üçü tutmuyorsa geri kalanı ölçme, İSTASYON oynamıştır.
  ① eski mendirek üst kenarı   %10,04  (193 px)   ·  %x 10,00 → 90,00
  ② kaya adacığı               %49,23 → %53,03    ·  %x 4,55
  ③ ⭐ UFUK ÇİZGİSİ             %67,86  (1303 px)  ·  kenardan kenara, EĞİM SIFIR

SONRA yapı kilitleri (kaynak: plan §Kadraj kilitleri):
  iç su hattı            %44,65   857 px    sekiz karede de
  fribord                G0/G1 304 · G2 136 · G3 113 · G4–G7 147 px   (±6 px)
  kret                   %52,33  1005 px   G4'ten sonra
  parapet tepesi         %58,24  1118 px   G5'ten sonra
  fener merceği          %59,87  1149 px   yalnız G7'de IŞIKLI
  kol eni                748 px  %x 15,38 → 84,62   sekiz karede de
⛔ Kol hiçbir karede kadrajda YATAY OLARAK KAYMAZ. G0'ın tek istisnası vardır ve BEYANLIDIR:
   kutu 10° yamuktur, sağ ucu 3,00 m daha uzaktadır; G1'den itibaren yukarıdaki değerler geçerlidir.
```

---

## 5. YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK]

```
G0 · G1   kutu YÜZER. Ağırlığın tamamını altındaki su taşır. Tabanı hiçbir şeye DEĞMEZ.
          Konumunu taşıyan şey dört gergin halat ve iki römorkör halatıdır.
          ⛔ Bu iki karede kutunun altında takoz, kazık, iskele ya da dolgu GÖRÜNMEZ.
G2 – G7   kutu YATAĞINA OTURUR. Ağırlığın tamamı tabanından yatağa biner.
          ⛔ Bu altı karede kutu bir daha YÜKSELMEZ ve halatlar ASLA GERİLMEZ.
⛔ DÜŞME KOŞULU: herhangi bir karede fribord bir öncekinden BÜYÜKSE (kapak eklenen G4 hariç) film düşer.
   İzin verilen tek artış G3 → G4'tür (113 → 147 px) ve sebebi beton eklenmesidir, yükselme değildir.

VİNÇ KARARI [DERS 8 · P10-j]
  ⭐ Bütün vinçler ve mavnalar kolun DENİZ YAKASINDADIR. G0–G2'de kutunun üstünde küçük bir güverte
     vinci görünür; G3'ten sonra mavna gövdesi kolun ARKASINDA kalır ve yalnız bomu kretin üstünde okunur.
  ⛔ Hiçbir karede BOŞ KANCA yoktur; her kancada görünür bir yük vardır.
  ⛔ Hiçbir vinç kadrajın YAKIN SUYUNA girmez — orası defterin sayıldığı yerdir (§1).
```

---

## 6. IŞIK VE GÖLGE KAPISI

```
İç yüz normali 130°. Aydınlık katsayısı = cos(yükseklik) · cos(azimut − 130°), |Δ| ≥ 90° ise 0.

  kare   saat    azimut   yükseklik   katsayı   iç yüz ekranda
  G0     06:00    83,80°    7,87°      0,686    aydınlık, düşük kontrast
  G1     08:00   108,24°   26,10°      0,834    ⭐ FİLMİN EN PARLAK KARESİ
  G2     10:00   138,94°   41,45°      0,740    aydınlık, yüksek güneş
  G3     12:00   180,00°   48,00°      0,430    aydınlık ama düzleşmiş
  G4     14:00   221,06°   41,45°      0,000 ⛔ ⭐ YÜZ GÖLGEYE DÜŞER — düz koyu bant
  G5     16:00   251,76°   26,10°      0,000    siluet, parapet tepesi parlar
  G6     18:00   276,20°    7,87°      0,000    siluet, dış deniz GÜMÜŞ PARILTI
  G7     18:10   278,14°    6,34°      0,000    aynı, fener SICAK

⛔ DÜŞME KOŞULU ① G4 · G5 · G6 · G7'de iç yüzde DOĞRUDAN GÜNEŞ IŞIĞI varsa o kare düşer.
⛔ DÜŞME KOŞULU ② G0 · G1 · G2'de iç yüz gölgedeyse o kare düşer.
⛔ DÜŞME KOŞULU ③ ⭐ GÖLGE YÖNÜ S1 KLİBİNİN İÇİNDE İŞARET DEĞİŞTİRİR: G1'de kutunun gölgesi kadrajda
   SOLA, G2'de SAĞA düşer (yan bileşen −0,371 → +0,155). Değişmiyorsa S1 klibi düşer.
⛔ DÜŞME KOŞULU ④ ⭐ GÖLGE KAMERAYA DÖNER: G5'ten itibaren kolun gölgesi yakın suyun üstüne uzanır
   (eksen bileşeni −0,526 → −0,849). G6 ve G7'de 47,06 m ve 58,52 m'dir ve görünen yakın suyun
   tamamını (37,47 m) kaplar. G6'da yakın su gölgesizse o kare düşer.
⛔ DÜŞME KOŞULU ⑤ GÜNEŞ HİÇBİR KAREDE KADRAJDA DEĞİL. Kadraj az 283,43° … 336,57°; en yakın
   yaklaşma 18:10'da 278,14°, pay 5,29°. Kadrajın sol kenarında güneş diski ya da doğrudan huzme
   görünürse istasyon yanlış kurulmuştur [DERS 39].
```

---

## 7. SAYIM KAPISI [DERS 55]

```
Sekiz karenin sekizinde de kadrajda ŞU VARDIR:  bir beton kutu · bir geçici kaya bermi ·
  bir eski mendirek başı · bir kaya adacığı · bir ufuk çizgisi · bir bulut tabakası
Sekiz karenin hiçbirinde kadrajda ŞU YOKTUR:
  ⛔ kara parçası, kıyı çizgisi, kumsal, bina, şehir, uzakta liman
  ⛔ ikinci bir kayson ya da kolun uzatılması
  ⛔ kadraja giren üçüncü bir gemi (iki römorkör G0–G1'de uçlarda, yarısı dışarıda; G7'de bir tekne)
  ⛔ kule, direk sırası, konteyner istifi — fikrin bilim-kurgu limanından hiçbir şey
⚠️ EN OLASI MODEL ARIZASI: "harbour" kelimesi korpusta KIYI çağırır. Kontrol her karede ufuk çizgisine
   bakılarak yapılır: ufuk KESİNTİSİZ SU olmalı, üstünde yalnız bulut.
```

---

## 8. ⭐ REJİM A KAPISI — deponun ilk A finali (ÖLÇÜLMEDİ)

```
S6 klibi 10 dakikayı 8,0 saniyede geçirir: 75× … 100× bandı (plan 100× varsayar).
  ① TEKNE: sol kenardan girer, TEK PÜRÜZSÜZ ÇİZGİ çizer, döner, ikinci babanın altında durur.
     ⛔ Konum sıçraması (ışınlanma) varsa klip düşer. 100×'te tekne saniyede ≈ 6,5 m ilerler;
        30 fps'te kare başına ≈ 0,22 m = 5 piksel — yani HAREKET SÜREKLİ OKUNUR.
  ② İZ: yanaşmadan sonra iki uzun yumuşak çizgi, klibin son 1,0 saniyesinde SÖNER.
     ⛔ İz hiç oluşmuyorsa ya da klibin sonunda hâlâ duruyorsa klip düşer.
  ③ FENER: çakmalar 100×'te tek bir DURAĞAN soluk boncuğa dönüşür.
     ⛔ Kadrajda yanıp sönen bir ışık görünüyorsa sıkıştırma oranı yanlıştır.
  ④ GÖLGE: yalnız biraz uzar. ⛔ Gölge süpürmesi görünür hâldeyse rejim B'ye kaçılmıştır.
  ⑤ İNSAN: yumuşak izler. ⛔ Keskin yüz varsa klip düşer.
⭐ İLK ÜRETİMDEN SONRA: ölçülen değer SANTIYE_HAREKETI §1'e tek satır olarak iner. Bu film,
   rejim A'nın FİNAL olarak ilk sınavıdır [P17-g].
```

---

## 9. SES KAPISI

```
⛔ MÜZİK YOK — bütün bant diegetik.
  ① ⭐ YAKIN SU SESİ GÖRÜNTÜ DEFTERİYLE AYNI EĞRİYİ ÇİZER: 0,0'da en yüksek, 47,0–48,0 arasında
     TAMAMEN KESİLİR. Ölçüm: 0,0–2,0 ile 54,0–56,0 arasındaki yakın-bant gürültüsü ≥ 18 dB fark.
  ② ⭐ SESSİZLİK PENCERESİ 48,0 – 52,0: yakın suda hiçbir şey yok; yalnız uzak kırılma ve yaklaşan
     tek bir küçük dizel. ⛔ Bu dört saniyeye herhangi bir şantiye sesi girerse bant düşer.
  ③ 32,0 – 40,0 arasında her 2–3 saniyede bir, kolun ARKASINDAN gelen derin bir taş çöküşü —
     görünmeyen işin tek kanıtı budur.
  ④ ⛔ GEMİ DÜDÜĞÜ YOK. Fikirdeki "tek uzun düdük" maddesi düştü: müziğin işini yapıyor.
  ⑤ ⛔ Anlatıcı yok · konuşma yok · "dramatic whoosh" yok · sesli imza yok.
```

---

## 10. ZAMAN VE IŞIK GÜNÜ

```
REJİM      6 × B (2,00 sa) + 1 × A (10 dk) = 12 sa 10 dk   ⛔ tavan 14,00 sa  ✅
PENCERE    06:00 → 18:10 · 52° kuzey · geç ağustos (δ +10°) · gündüz 13 sa 44 dk
PAY        doğuştan 52 dk · batışa 42 dk
⛔ İKİ REJİM KURALI: bu filmde yalnız B ve A vardır [SANTIYE_HAREKETI §1]. Üçüncü bir rejim
   (C ya da G) hiçbir klibe girmez.
⛔ REJİM C YOK → insan yasağı YOK. Yedi klibin yedisinde de işçi yumuşak iz olarak görünür.
⭐ TEK IŞIK GÜNÜ: hava sekiz karede AYNIDIR — ağır, yarık, alçak bulut tabakası. Bulut ÖRÜNTÜSÜ
   değişir (sürüklenir), HAVA DEĞİŞMEZ. Yağmur, sis, açık gökyüzü hiçbir karede yoktur.
```

---

## 11. ⚠️ BİLİNEN RİSKLER — üretimden önce oku

```
① ⭐ EN BÜYÜK RİSK — FİLMİN BİLİM-KURGUYA KAÇMASI. Konsept kaynağı anlatılı bir bilim-kurgu metnidir
   ve "liman" kelimesi modelde kule, dev vinç, gökdelen gemi ve şehir çağırır. Bu filmde kadrajda
   ALTI NESNE vardır ve altısı da §7'de sayılıdır. Her kare o listeye karşı okunur.
② "HARBOUR" → KIYI. Model ufka bir kara parçası ekleyebilir. NEGATIVE üç cümleyle kapatır ama
   kontrol ELLE yapılır: ufuk kesintisiz su mu?
③ BATMA = DEVRİLME. Model "sinking" kelimesini yalpalama/devrilme olarak okuyabilir. Kutu S1'de
   DÜMDÜZ iner; üst kenarı her karede ufka PARALELDİR. Eğim varsa klip düşer.
④ KUTU GERİ YÜZER. En sinsi arıza: model son karelerde fribordu büyütür. §5'in düşme koşulu bunu yakalar.
⑤ YAKIN SU TEKRAR DALGALANIR. Modelin "deniz" refleksidir. §1'in monoton kuralı bunu yakalar.
⑥ İKİNCİ KAYSON. G5–G7'de saha boştur; model boşluğu doldurmak ister. Sayım cümlesi kapatır.
⑦ TİLT KAYMASI. Ufuk %67,86'dan oynarsa bütün yüzdeler bozulur. Zincir kontrolünün ilk bakacağı yer.
⑧ ⭐ IŞIĞIN YÖN DEĞİŞTİRDİĞİ KLİP (S3). Model aynı klipte hem yeni SOLUK bir bant büyütmeli hem
   altındaki yüzü KARARTMALIDIR. İkisini karıştırması en olası tek-klip arızasıdır — bu yüzden
   ikinci pilottur.
⑨ FENER PATLAMASI. G7'de fener bir BONCUKTUR, bir huzme ya da parlama değil. Kadraja hale, ışın,
   lens parlaması girerse kare düşer.
⑩ ⭐ KANIT NESNESİ KAPAKTA OKUNMUYOR. Köstek gözleri 41 px'tir ve 120 piksellik küçük resimde
   5 piksele iner — kapakta OKUNMAZ. Bu beyanlıdır: kapağın kancası ayrıntı değil, ZITLIKTIR
   (düz su / kırık su). Ayrıntı filmin İÇİNDE kanıtlanır [bkz. KAPAK §1].
```
