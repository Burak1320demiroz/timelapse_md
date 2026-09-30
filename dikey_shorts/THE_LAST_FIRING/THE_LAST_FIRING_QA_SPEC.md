# 🔬 THE LAST FIRING — QA ŞARTNAMESİ

```
KAPSAM     7 sahne × 8,0 sn = 56,0 sn · 8 görsel + 7 I2V · tek istasyon (HOME)
AMAÇ       Bu dosya "güzel mi" diye sormaz. Tek soru: ⭐ OCAĞIN TEPESİ, UFUK ÇİZGİSİNE GÖRE
           DOĞRU YERDE Mİ — sekiz karede, ±2 piksel içinde, ve doğru YÖNDE mi hareket ediyor.
DURUM      ⛔ ÜRETİLMEDİ — bu şartname ÖLÇÜM BEKLİYOR. Aşağıdaki hiçbir sayı ölçülmüş değildir;
           hepsi plandan türetilmiş HEDEFTİR [QA/00_INDEX · ölçülmemiş film].
TARİH      26.09.2026
```

---

## §1 ⭐ DEFTER KAPISI — filmin tamamı bu ölçümde

```
ÖLÇÜLEN    her karede: ocağın en üst pikselinin y değeri  −  ufuk çizgisinin y değeri
           x konumu: kubbe merkezinin x'i (%66,47 · 718 px soldan)
YÖNTEM     ① ufuk çizgisi, kadrajın SOL %0–20 ve SAĞ %88–100 bantlarında ayrı ayrı bulunur
              (oralarda kubbe ve incir yoktur) ve iki bulgu arasında ≤ 1 px fark olmalı —
              ⛔ fark 1 px'i geçerse ROLL vardır, kare düşer
           ② kubbenin en üst pikseli, %60–75 bandında en yüksek koyu-açık sınır olarak alınır
           ③ fark işaretli olarak yazılır (tepe ufkun üstündeyse +)

HEDEF      G0     G1     G2     G3     G4     G5     G6     G7
          −246   −165    −83      0    +31    +18    −33    −36   px
TOLERANS   ±2 px [sahip kararı 19.09.2026]

⭐ İKİ YASA — ikisi de tek tek denetlenir:
   YASA A   G0 → G4 arasında her adım ARTAR ve her adım en az 25 px'tir
            (81 · 82 · 83 · 31 px — sonuncusu küçüktür ama POZİTİFTİR)
   YASA B   G4 → G7 arasında her adım AZALIR
            (−13 · −51 · −3 px)
   ⛔ Tek bir satır yasayı bozarsa film düşer. Bu bir estetik kural değil: yapı ya yükseliyordur
      ya çöküyordur, ikisini aynı anda yapamaz.

⭐ ÜÇ ÖZEL KARE — ayrı ayrı geçilir:
   G3   |defter| ≤ 2 px olmalı. ⭐ Bu filmin TEMELİ budur; tutmazsa istasyon yanlıştır ve
        h yeniden hesaplanır, plan yeniden yazılır. ⛔ Pilot 1 tam olarak bu ölçümdür.
   G4   defter POZİTİF olmalı ve serinin EN BÜYÜĞÜ olmalı (+31 px).
        ⛔ G4 en büyük değilse filmin dönüm noktası yanlış yerdedir.
   G6   defter NEGATİF olmalı. ⭐ G5 pozitif, G6 negatif: ufuk S5'in içinde geçilir.
        ⛔ Geçiş S5'ten önce olursa yanma erken, sonra olursa geç başlamıştır.

⛔ DÖRT DÜŞME ŞARTI
   ① G3'ün mutlak değeri 2 px'i geçerse
   ② G4 serinin en büyüğü değilse
   ③ herhangi bir adım yasayı ters çevirirse (artarken azalma, azalırken artma)
   ④ ⭐ ufuk çizgisi iki kenar bandında 1 px'ten fazla ayrışırsa — kamera oynamıştır
```

---

## §2 ÇAPRAZ DEFTER — kum önlüğü, tek yönlü

```
ÖLÇÜLEN    kum önlüğünün kadrajı kapladığı genişlik (px) ve en üst pikseli
HEDEF      G0 yok · G1 yok · G2 BELİRİR · G3–G7 = 831 ± 20 px en, üst kenar 841 ± 3 px
⭐ TEK YÖN  G2'de belirdikten sonra HİÇBİR KAREDE küçülmez, hiçbir karede yer değiştirmez.
HACİM      kalıp 3,00 m³ × 1,15 kabarma = 3,45 m³ · önlük 5,00 × 3,00 × 0,70 m = 3,75 m³
           ⛔ Önlük bu hacimden belirgin küçükse kum kadrajın dışına çıkarılmıştır ve
              "boşluk kadrajda kalır" iddiası düşer.
NEDEN      Bu defter ANA DEFTERDEN BAĞIMSIZDIR: ana defter kubbenin YÜKSEKLİĞİNİ ölçer,
           bu defter kubbenin İÇİNDEKİ BOŞLUĞU ölçer. İkisi aynı anda yanlış olamaz.
⛔ DÜŞME   önlük G3–G7 arasında herhangi bir karede küçülürse ya da kaybolursa.
```

---

## §3 IŞIK KAPISI — iki saat, iki ayrı taşıyıcı

```
BİRİNCİ SAAT — GÜNEŞ (yalnız ilk yarı taşır)
   yakın yüz katsayısı   0,192 · 0,460 · 0,567 · 0,484 · 0,233 · 0,000 · 0,000 · 0,000
   sağ yan katsayısı     0,971 · 0,734 · 0,314 · 0,000 · 0,000 · 0,000 · 0,000 · 0,000
   incir gölgesi (m)      31,4 ·   7,8 ·   3,8 ·   2,7 ·   3,8 ·   7,8 ·  31,4 ·  40,4
   ⭐ ÖLÇÜM: incirin gölge ucu, kadrajda ölçülebilir olduğu her karede (G1–G5) plandaki
      uzunluğun ±%10'u içinde olmalı. Gölge YÖNÜ de denetlenir: azimut + 180°.

İKİNCİ SAAT — OCAK (yalnız ikinci yarı taşır)
   kor katsayısı         0,00 · 0,00 · 0,00 · 0,00 · 0,02 · 0,30 · 0,80 · 1,00
   ⭐ ÖLÇÜM: ateş ağzının (95 × 145 px) ortalama L* değeri, aynı karedeki kubbenin
      kameraya bakan yüzünün ortalama L* değerine ORANLANIR.
      G4 < 1,0   ·   G5 > 1,5   ·   G6 > 3,0   ·   G7 > 4,0

⭐ İKİ OLAY — S4'ün içinde, saniyesi yazılı:
   3,32 sn   kor güneşi GEÇER — kadrajın ufuk altındaki en parlak yeri ateş ağzı olur
   5,41 sn   güneş kubbenin yakın yüzünü TAMAMEN terk eder (az 250°)
   ⛔ İkisi de S4 klibinde görünmelidir. Görünmüyorsa sahne saati kaydırılır (14:00 → 15:00),
      ⛔ kor eğrisi DEĞİŞTİRİLMEZ — o fizikten geliyor, tercihten değil.

⛔ BEŞ DÜŞME ŞARTI
   ① herhangi bir karede güneş kadraja girerse (bearing 340° · kadraj 313,4°…6,6°)
   ② G5–G7 arasında kubbenin yakın yüzünde GÜNEŞ ışığı okunursa (katsayı sıfırdır)
   ③ G0–G3 arasında ocaktan ışık çıkarsa (ateş henüz yok)
   ④ gölge YÖNÜ bir karede ters dönerse
   ⑤ ⭐ G7'de kadrajın en parlak yeri gökyüzü olursa — filmin ödülü tam olarak bunun tersi
```

---

## §4 G6 = G7 KİMLİĞİ — kapak kilidi

```
BİREBİR AYNI OLACAK ALTI MADDE
   ① ufuk çizgisi %57,007 · 1095 px        ② yaşlı incir 234 × 488 px · %x 9,17–30,83
   ③ kum önlüğü 831 × 132 px               ④ ham bant 143 × 90 px · sol etek
   ⑤ kubbe eni 432 px                      ⑥ sepet sırası önlüğün üstünde
İZİN VERİLEN ÜÇ FARK
   ⓐ ön yüzde 127 px'lik kırık delik (G6'da YOK, G7'de VAR)
   ⓑ defter −33 → −36 px
   ⓒ iki sepet dolar, buharları görünür
⛔ Dördüncü bir fark bulunursa kapak kanıtı düşer [DERS 30].
ÖLÇÜM   bash araclar/zincir_kontrol.sh g6.jpg g7.jpg → izin verilen üç bölge maskelenir,
        kalan kadrajda fark ≤ 2 px olmalı.
```

---

## §5 ±2 PX KİLİTLERİ — önce ÜÇ NİRENGİYE bak

```
① UFUK ÇİZGİSİ    %57,007 · 1095 px · sol ve sağ bantta ≤ 1 px fark        sekiz karede
② YAŞLI İNCİR     %x 9,17 → 30,83 · 234 × 488 px · taban 883 px            sekiz karede
③ HAM BANT        %x 45,59 → 58,82 · 143 × 90 px                           G4 → G7
   (G0–G3'te üçüncü nirengi KUM ÖNLÜĞÜNÜN SOL KENARIDIR · %22,31)

BAĞIMLI KİLİTLER
   kubbe eni            432 ± 4 px        G3 → G7 (tam hâl)
   kubbe tabanı         797 ± 2 px        G3 → G7   ⭐ TABAN OYNAMAZ, yalnız TEPE oynar
   ateş ağzı            95 × 145 px       G0 → G7 (G0'da çerçeve olarak)
   baca gözü            87 px             G3 → G7  ⛔ küçük resimde 9,7 px — OKUNMAZ, beyanlı
   taş yığını           576 × 199 px      G0 · G1 (G2'de küçülür, G3'te yok)
   haze bandı           ufkun hemen altı  sekiz karede aynı kalınlık

⭐ EN ÖNEMLİ TEK KİLİT: KUBBENİN TABANI. Taban 797 px'te sabit kalmazsa defter anlamsızdır —
   tepe ile ufuk arasındaki fark, taban kaydığı için değişmiş olur. ⛔ Taban önce ölçülür.
```

---

## §6 HAVALI SAHA KAPISI + YÜK YOLU

```
⭐ BU FİLM HAVASIZ DEĞİLDİR ve önceki iki filmin kuralları TERSİNE ÇALIŞIR [P19-e]:
   ✅ ZORUNLU   duman ışığı taşır · ateş ağzının çevresinde HALE vardır · gölge kenarlarında
                dar bir yarı gölge vardır · uzak haze bandı yumuşaktır · toz havada ASILI KALIR
   ⛔ YASAK     bıçak gibi kesilmiş gölge kenarı · haleyi silinmiş ışık kaynağı ·
                balistik yay çizip anında düşen toz (bu FIRST GUEST'in fiziğidir, bu filmin değil)

YÜK YOLU — her karede tek cümleyle doğrulanır
   G0   bedding halkası → dövülmüş toprak
   G1   eğik sıralar → hem alttaki taşa HEM kum kalıba (kalıp yükün bir kısmını taşır)
   G2   ⭐ kalıp gider → kemer KENDİ KENDİNİ taşır. Bu filmin tek yapısal anıdır.
   G3   tepe yükü → kapalı kemer → bedding halkası → toprak
   G4+  kil derisi HİÇBİR YÜK TAŞIMAZ; taş tek başına taşır ve yanarken de taşır
⛔ Kil sıvanın taşıyıcı gösterilmesi (çatlayınca kubbe çöküyormuş gibi) FİZİK HATASIDIR.
⛔ Hiçbir karede kubbeye dışarıdan destek, kuşak, halat ya da kafes bağlanmaz.
```

---

## §7 SAYIM KAPISI

```
Kadrajda sayılan altı nesne: ① ocak ② taş yığını (G0–G2) ③ kum önlüğü (G2+) ④ yaşlı incir
⑤ ufuk çizgisi ⑥ haze bandı.
⛔ Yedinci bir kalıcı nesne belirirse sayım kilidi düşer. Geçici ekipman sayıma girmez:
   sehpa · iskele kalası · dikme · el arabası · sepet · kil torbası · çelik çubuk · römork.
⛔ İkinci bir ocak, ikinci bir ağaç, uzakta bir bina, bir çit, bir direk YOKTUR.
⛔ Kuş, hayvan, araç trafiği, uçak izi YOKTUR.
```

---

## §8 İKİ REJİM KAPISI

```
S0–S5   rejim B (2,00 saat / 8,0 sn = 900×) — gölgeler kayar, bulut çizgilenir, insan LEKE olur
S6      ⭐ rejim A (10 dakika / 8,0 sn = 75×) — gölge neredeyse durur, insan İNSAN gibi okunur
⭐ ÖLÇÜM: S6'da incirin gölge ucu klip boyunca 0,50 m'den az yer değiştirmeli; S5'te aynı uç
   23,6 m yürür. İki klibi yan yana koyup gölge ucunun hızına bakmak yeter.
⛔ İki rejim tavanı [SANTIYE_HAREKETI §1]: bu filmde B ve A vardır, ÜÇÜNCÜSÜ YOKTUR.
   ⛔ Rejim G (gerçek zaman) finali P16-g gereği YASAKTIR ve bu filmde kullanılmadı.
```

---

## §9 SES KAPISI — tam diegetik

```
⭐ Bu filmde yatak tamamen diegetiktir ve bu ölçülebilir: her ses kaynağının kadrajda karşılığı var.
   taş-taşa · kürek · el arabası · mala · çalının tutuşması · çekiş uğultusu · kilin çatlaması ·
   kil levhasının düşmesi · sepetin sürtünmesi
⛔ Kütüphaneden gelen "şantiye ambiyansı" YASAKTIR: motor, korna, telsiz, uzak trafik duyulursa düşer.
⛔ Kuş, rüzgâr çanı, köpek, uçak YOKTUR. Hava vardır ama saha sessizdir.
⭐ TEK ÖLÇÜLEBİLİR İDDİA: 51,0 – 53,0 sn aralığında (delik açılırken) uğultunun RMS'i,
   40,0 – 48,0 sn ortalamasının en az 6 dB üstündedir ve enerjisinin en az %70'i 200 Hz'in altındadır.
   ⭐ Sebep fiziktir: delik açılınca ocağın çekişi artar. Ses, görüntüden ÖNCE gelir.
⚠️ ÜRETİM NOTU: taş-taşa sesi AÇIK AVLUDA kaydedilmelidir. Kapalı mekân kaydının yankısı
   bu filmde duyulur ve sahayı yalanlar.
```

---

## §10 ZAMAN VE IŞIK GÜNÜ

```
PENCERE     06:00 → 18:10 = 12 sa 10 dk
REJİM       6 × 2,00 sa (B) + 1 × 0,167 sa (A) = 12,167 sa   ≤ 14,00 sa tavan ✅
GÜN         13 sa 32 dk (43°K · δ +12°) · doğuş 05:14 · batış 18:46
PAY         başta 0,77 sa · sonda 0,60 sa  ⭐ Film günün içinde kalır, kenarına dayanmaz.
⛔ Sahne saatleri kaydırılırsa GÜNEŞ TABLOSU BAŞTAN HESAPLANIR. Katsayılar elle düzeltilmez.
KONTROL     her karede: azimut ve yükseklik değeri, prompt satırındaki sayıyla aynı mı?
```

---

## §11 ON RİSK — sırayla, en büyükten

```
①  ⛔ G3'ÜN SIFIRI TUTMAZSA. Filmin temeli bu tek ölçümdür. Yedek plan yok; istasyon yeniden
    hesaplanır ve plan baştan yazılır. ⭐ Bu yüzden PİLOT 1 = G3 + G4.
②  ⛔ MODEL KUBBEYİ BÜYÜTMEYE DEVAM EDER. Sürekli büyüyen yapı, bu motorun en güçlü alışkanlığı.
    G4'ten sonra kubbe KÜÇÜLMEK zorunda ve negatif çekirdekte bu ayrıca kilitlendi.
③  ⛔ DUMAN VE KOR TUTARSIZLIĞI. Sekiz karede aynı rüzgâr yönü, aynı duman rengi, aynı çekiş.
    S4 ve S5 en riskli kliplerdir.
④  ⚠️ KİL DERİSİ TAŞIYICI GÖRÜNÜR. Çatlaklar "yapı çöküyor" gibi okunursa fizik yalanlanır.
    Çatlak AĞI olmalı, YARIK olmamalı.
⑤  ⚠️ KUM ÖNLÜĞÜ KAYBOLUR. Model temizlik yapmayı sever; önlük her karede sayılır.
⑥  ⚠️ TAŞ YIĞINI G3'TE TAM BİTMEZ. Sol alt köşenin boşalması S3'ün tek görsel olayıdır.
⑦  ⚠️ UFUK ÇİZGİSİ EĞİLİR. Roll sıfırdır; iki kenar bandı ayrı ölçülür.
⑧  ⚠️ AYRINTI TABANI ÇOK CÖMERT (0,23 m). Model tek tek taşları çizebilir ve kubbe "duvar"
    gibi görünebilir. Korbelli örgü DÜZENSİZ olmalı, derzli duvar değil.
⑨  ⚠️ S6'DA IŞIK TİTRER. Rejim A'da alev titremesi kırpışma olarak okunabilir; klip yeniden
    koşulur, ⛔ rejim G'ye düşülmez [P16-g].
⑩  ⚠️ BACA GÖZÜ KÜÇÜK RESİMDE OKUNMAZ (9,7 px). Bu beyanlıdır; kapak onu satmaz.
```
