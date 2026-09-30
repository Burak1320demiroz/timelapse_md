# 🔬 THE LONG SHADOW v2 — QA ŞARTNAMESİ

```
KAPSAM     7 sahne × 8,0 sn = 56,0 sn · 8 görsel + 7 I2V · tek istasyon (HOME)
AMAÇ       Bu dosya "güzel mi" diye sormaz. Tek soru: ⭐ KARŞI DUVARDAKİ GÖLGE ÇİZGİSİ, O DUVARIN
           KENDİ YÜKSEKLİĞİNİN KAÇTA KAÇINDA — sekiz karede, ±0,006 içinde, ve hep YUKARI mı gidiyor.
DURUM      ⛔ ÜRETİLMEDİ — bu şartname ÖLÇÜM BEKLİYOR. Aşağıdaki hiçbir sayı ölçülmüş değildir;
           hepsi plandan türetilmiş HEDEFTİR [QA/00_INDEX · ölçülmemiş film].
TARİH      28.09.2026
⭐ v2       Bu film THE LONG SHADOW v1'in yeniden planıdır. v1 üretildi ve dört merceğin
           dördü de düştü (① 3,3 ② 0,4 ③ 4,3 ④ 2,7 · ⛔ YAYINLANMAZ). v1'in yedi arızasının
           her birine bu planda bir cevap vardır [plan §v1'İN CEVABI · QA/RAPORLAR/THE_LONG_SHADOW.md].
           ⛔ v1'in QA kaydı AYRIDIR ve bu şartnameyle karışmaz; klasör adı bu yüzden _V2'dir.
```

---

## §1 ⭐ DEFTER KAPISI — filmin tamamı bu ölçümde

```
ÖLÇÜLEN    her karede, gölge bandının MERKEZİNDEKİ tek bir dikey sütunda iki px uzunluk:
              pay   = sokak taşının üst yüzü  →  gölge çizgisinin üst kenarı
              payda = sokak taşının üst yüzü  →  saçak hattının alt kenarı
           DEFTER = pay ÷ payda      ⛔ birimi YOKTUR

YÖNTEM     ① BANT BULUNUR: karşı duvarda, tabandan tepeye uzanan koyu şeridin iki dikey kenarı
              işaretlenir; sütun ikisinin tam ORTASINDAN geçirilir.
           ② KENAR NOKTASI: gölge kenarı yumuşaktır (§2). Üst kenar, parlaklık geçişinin
              %50 noktası olarak alınır — ⛔ "karanlığın başladığı yer" değil.
           ③ Pay ve payda AYNI SÜTUNDA ölçülür. ⛔ DERİNLİK DÜZELTMESİ YAPILMAZ ve GEREKMEZ:
              oranın bütün varlık sebebi budur.

HEDEF      G0      G1      G2      G3      G4      G5      G6      G7
          0,000   0,094   0,323   0,546   0,698   0,848   0,955   1,000
TOLERANS   ±0,006  (pay ve paydada ±2 px'in karşılığı)

⭐ İKİ YASA — ikisi de tek tek denetlenir:
   YASA A   Sekiz değer KESİNLİKLE ARTANDIR. Adımlar: +0,094 +0,228 +0,224 +0,151 +0,151 +0,107 +0,045
            En küçük adım (S6) 0,045'tir = gürültünün 7,5 katı. ⛔ Tek bir düşüş filmi düşürür.
   YASA B   Defter 1,000'i AŞAMAZ. Aşarsa ölçüm yanlıştır (saçağın üstünde duvar yoktur) ya da
            yapı planlanandan yüksek çıkmıştır — ikisi de kareyi ıskartaya çıkarır.

⭐ ÜÇ ÖZEL KARE — ayrı ayrı geçilir:
   G0   defter TAM 0,000. Karşı duvarda gölge bandı BULUNMAMALIDIR. Bir bant varsa sahada
        4,1413 m'den yüksek bir şey duruyordur (iskele? makine direği? konteyner?) ve
        o şey KALDIRILIR — defterin sıfır noktası odur.
   G2   bant merkezinin derinliği 18,00 m olmalı (öğlen, az 180°). Bandın iki kenarı kadrajda
        x% 57,50 ve 65,00'te durur. ⛔ Sapma 0,5 puandan büyükse saat yanlıştır.
   G7   defter TAM 1,000 → ⛔ |pay − payda| ≤ 2 px. ⭐ Bu filmin TEMELİ budur.
        Tutmazsa h_son (11,34 m) yanlıştır, yeniden hesaplanır ve BÜTÜN PLAN yeniden yazılır.
        Pilot 1 tam olarak bu ölçümdür ve ondan önce hiçbir kare üretilmez.

⛔ DÖRT DÜŞME KOŞULU
   ① herhangi bir adım negatif                       → film düşer
   ② G0'da bant var                                  → saha kirli, kare ıskarta
   ③ G7'de |pay − payda| > 2 px                      → plan geçersiz, yeniden hesap
   ④ ham px ile ölçüm yapılmış (oran değil)          → ölçüm geçersiz, §1'e dön
```

---

## §2 ⭐ KENAR KAPISI — bu filmin ikinci ölüm kalım ölçümü

```
NEDEN      Defter bir KENARIN yerini ölçüyor. Kenar yumuşarsa defter ölçülemez; kenar sertleşirse
           fizik yalan olur. İkisi de kareyi düşürür.

ⓐ YARIGÖLGE (olması ZORUNLU)
   Güneşin açısal çapı 0,53°. Işının gölge atan kenardan duvara kadar yolu ölçülür; yarıgölge
   genişliği = yol × tan(0,53°).
      kare   ışın yolu   yarıgölge      px karşılığı
      G1      6,34 m      0,059 m          3,5 px
      G2      5,49 m      0,051 m          3,6 px
      G3      5,49 m      0,051 m          3,6 px
      G4      5,51 m      0,051 m          3,7 px
      G5      6,70 m      0,062 m          5,5 px
      G6      6,92 m      0,064 m          5,8 px
      G7      7,16 m      0,066 m          6,2 px
   KABUL      3 – 8 px arası yumuşak geçiş.
   ⛔ 0–1 px (jilet gibi kenar)  → fizik yalan, kare ıskarta
   ⛔ > 12 px (bulanık bant)     → defter ölçülemez, kare ıskarta
   ⭐ Yarıgölge gün boyu BÜYÜR (3,5 → 6,2 px) çünkü ışın yolu uzar. Sabit kalıyorsa model
      gölgeyi hesaplamıyor, boyuyor demektir.

ⓑ SEKME IŞIĞI (olması ZORUNLU)
   3,60 m'lik bir sokakta güneşli yüzey karşı duvara dolgu atar. Gölgedeki duvar SİYAH OLAMAZ.
   ÖLÇÜM   gölge içindeki ortalama parlaklık ile aynı duvarın güneşli kısmı arasındaki fark
           2,5 – 4,0 stop olmalı.
   ⛔ > 5 stop → sokak dışarıda gibi davranıyor, sekme yok, kare ıskarta
   ⛔ < 1,5 stop → gölge okunmuyor, defter ölçülemez

ⓒ ⭐ EĞİM KAPISI — sahtekârlığı yakalayan tek ölçüm
   Gölge çizgisi DÜNYADA yataydır. Kadrajda yatay DEĞİLDİR: sokakla aynı kaçış noktasına
   (825 px) yakınsar. Yani üç çizgi — oluk, gölge kenarı, saçak — AYNI NOKTADA buluşmalıdır.
      kare   yakın uç px   uzak uç px   eğim
      G1        744,6        780,5      −35,8   (çizgi lensin ALTINDA → uzakta YUKARI)
      G2        896,1        860,9      +35,2   (çizgi lensin ÜSTÜNDE → uzakta AŞAĞI)
      G4       1191,6       1007,5     +184,0
      G7       1733,2       1188,1     +545,0   ⭐ saçak hattıyla BİREBİR aynı iki sayı
   ⭐ İŞARET DEĞİŞİMİ: eğim S1 içinde işaret değiştirir. Çizgi 1,60 m'ye (lens hizasına)
      geldiğinde kadrajda TAM YATAY olur → ⭐ S1'in 4,71. saniyesi. Öncesinde yukarı,
      sonrasında aşağı eğimlidir.
   ⛔ Eğim her karede yatay çıkıyorsa gölge BOYANMIŞTIR, hesaplanmamıştır — film düşer.
   ⛔ Üç çizgi 825 px'te buluşmuyorsa istasyon ya da roll bozuktur.
```

---

## §3 ÇAPRAZ DEFTER — bandın YERİ ve ENİ (güneş saati)

```
Defteri İNŞAAT taşır; bandın duvardaki yerini GÜNEŞ taşır. İkisi DİKTİR ve karışmamalıdır.

kare  bant kenarları (x%)   bant eni   sahne  rejim   defter adımı   kenar adımı
G0     55,37 → 58,37          32 px      —      —         —             —
G1     56,63 → 61,87          57 px      S0     B      +0,094        +3,50 puan
G2     57,50 → 65,00          81 px      S1     B      +0,228        +3,13 puan
G3     57,58 → 65,31          83 px      S2     A      +0,224        +0,31 puan
G4     57,65 → 65,63          86 px      S3     A      +0,151        +0,32 puan
G5     58,93 → 72,06         142 px      S4     B      +0,151        +6,43 puan
G6     59,10 → 73,11         151 px      S5     A      +0,107        +1,05 puan
G7     59,28 → 74,34         163 px      S6     A      +0,045        +1,23 puan

⭐ REJİM AYRIMI TESTİ — filmin iddiası budur:
   B sahnelerinde kenar 3,13 – 6,43 puan kayar.
   A sahnelerinde kenar 0,31 – 1,23 puan kayar.
   ⛔ Bir A sahnesinde kenar 2,00 puandan fazla kayarsa model güneşi kendi saatinde akıtıyordur
      ve TIME RATE cümlesi sertleştirilir [DERS 15]. Bu, Pilot 3'ün tam konusudur.
⭐ BANT ENİ HİÇBİR KAREDE DARALMAZ: 32 → 57 → 81 → 83 → 86 → 142 → 151 → 163 px.
   Daralma, bandın kameradan uzaklaştığı anlamına gelir — saat ters akıyordur.
```

---

## §4 G6 = G7 KİMLİĞİ — kapak kilidi

```
Kapak yalnız G7'dir [sahip kararı 19.09.2026]. G6 ile G7 arasında değişmesi YASAK olan altı şey:
   ① saçak hattı ve paved gutter — aynı pikselde
   ② iki deponun saçakları (3,60 m) — aynı pikselde
   ③ dökme demir yağmur inişi — aynı pikselde, aynı ende
   ④ sokak ortasındaki taş oluk şeridi ve bütün el arabası izleri
   ⑤ kalıp kutularının depo duvarına dayalı istifi
   ⑥ parsel eni 81 px · x% 35,00 → 42,50
İZİN VERİLEN ÜÇ FARK:
   ⓐ parapet + harpuşta: üst kenar 1762 → 1793 px
   ⓑ defter 0,955 → 1,000 (gölge kenarı saçağa değer)
   ⓒ çatıdaki palet boşalır; kova ve mala kalır
⛔ Dördüncü bir fark bulunursa kapak kanıtı düşer [DERS 30].
```

---

## §5 ±2 PX KİLİTLERİ — önce ÜÇ NİRENGİYE bak

```
⭐ ÖNCE ÖLÇ: saçak hattı (d 18,00'de 1215 px) — defterin paydası ondan çıkar. Yanlışsa
   sekiz karenin sekizi de yanlıştır ve başka hiçbir ölçüme bakmaya gerek yoktur.

│ kuzey saçak (d 18,00)        1215 px   = %63,30   ⛔ ±2 px
│ paved gutter (d 18,00)        709 px   = %36,95   ⛔ ±2 px
│ duvar yüksekliği              506 px   / 7,20 m = 70,3 px/m
│ depo saçakları (d 12,00)     1037 px   = %54,03   ⛔ ikisi de, sekiz karede
│ parsel eni                     81 px   · x% 35,00 → 42,50
│ yağmur inişi (d 20,00)      x% 59,00   · dikey · I2V kilidinin çapası
│ yeni işin üst kenarı (d 12,00, kare kare):
│     G0 —  · G1 1161 · G2 1322 · G3 1479 · G4 1584 · G5 1688 · G6 1762 · G7 1793 px  ⛔ ±2 px
⛔ Bu yedi satırdan biri kayarsa kare ıskartadır; düzeltme yapılmaz, kare yeniden üretilir.
```

---

## §6 ⭐ EKİNOKS KAPISI — filmin tek fizik iddiası

```
İDDİA      Ekinoksta, doğu-batı bir duvara düşen gölge çizgisinin yüksekliği GÜN BOYU SABİT bir
           düzeltmeyle belirlenir:  düşüş = sokak eni × cot(φ) = 3,60 × cot 41° = 4,1413 m.
           Yani çizgi = kaster − 4,1413 m, saatten BAĞIMSIZ.

TEST 1     Her karede: (kaster yüksekliği) − (gölge çizgisinin metre karşılığı) hesaplanır.
           Sekiz değerin hepsi 4,1413 ± 0,05 m olmalı.
           ⛔ Değer gün içinde sürükleniyorsa saha ekinoksta değildir ya da sokak doğu-batı değildir.
TEST 2     ⭐ A sahnelerinde (10 dk) gölge çizgisinin YÜKSEKLİĞİ yalnız inşaattan değişir.
           S2'de kaster 6,40 → 8,00 m (+1,60), çizgi de +1,60 m çıkmalı — ne eksik ne fazla.
           ⛔ Çizgi kasterden farklı bir miktar çıkarsa model gölgeyi ayrı bir saatte hesaplıyordur.
TEST 3     Mevsim beyanı: kapak metninde ya da açıklamada "bu duvar 21 Mart'a kadar güneş almaz"
           cümlesi kullanılacaksa dayanağı budur ve ölçülmüştür:
              δ < 0 (ekinokstan sonra) için düşüş her saat 4,1413 m'den KÜÇÜKTÜR
              → çizgi = 11,34 − düşüş > 7,20 m → duvar her saat tam gölgede.
           ⛔ Bu cümle ölçüm olmadan kullanılmaz.
```

---

## §7 SAYIM KAPISI

```
Kadrajda sayılabilir altı şey vardır ve sekiz karede sayıları DEĞİŞMEZ:
   1 boşluk (parsel) · 2 depo · 1 kesintisiz sıra ev · 1 yağmur inişi · 1 oluk şeridi · 1 gök yarığı
⛔ İkinci bir yağmur inişi, üçüncü bir depo, ikinci bir boşluk → kare ıskarta [DERS 55].
⛔ Kadrajda VİNÇ, KULE, DİREK YOKTUR. Bir tanesi belirirse kendi gölgesini bandın üstüne atar ve
   defteri bozar — bu, bu filmde estetik değil ÖLÇÜM ihlalidir.
```

---

## §8 İKİ REJİM KAPISI

```
REJİM B (3 sahne · 2 saat · ~900×)   S0 · S1 · S4
REJİM A (4 sahne · 10 dk · ~75×)     S2 · S3 · S5 · S6
⛔ Üçüncü rejim YOKTUR [SANTIYE_HAREKETI §1].

ÖLÇÜLEBİLİR AYIRT ETME — gölge ucu testi:
   B sahnesinde sokak tabanındaki gölge şeridinin ucu klip boyunca en az 60 px yol alır.
   A sahnesinde aynı uç 10 px'ten az yol alır.
   ⛔ İki bant örtüşürse rejim beyanı yalandır.
```

---

## §9 SES KAPISI — tam diegetik

```
⛔ MÜZİK YOK — 0,0–56,0 arasında hiçbir ton, akor, nabız, yükseliş yok [sahip kuralı 21.09.2026].
⭐ YANKI TESTİ: her sert vuruşun (taş, tokmak, blok) ardında 21 ± 3 ms gecikmeli TEK bir yansıma
   olmalı (2 × 3,60 m ÷ 343 m/s). ⛔ Yankısız kayıt = açık alanda kaydedilmiş = saha yalan.
⛔ Geniş kuyruklu reverb (> 300 ms) YASAK: dar sokak oda değildir.
FİNAL    54,5 – 56,0 arası ses yatağının EN BOŞ yeridir: bir kova, bir ayak sesi, uzakta bir kapı.
         ⛔ Bu 1,5 saniyeye hiçbir vurgu eklenmez.
```

---

## §10 ZAMAN VE IŞIK GÜNÜ

```
PENCERE     08:00 → 14:40 = 6 sa 40 dk  ≤ 14 sa ✅
GÜN         ekinoks, 41° kuzey: 12 sa 00 dk (06:00 → 18:00) · pay 2,00 sa + 3,33 sa
GÜNEŞ       azimut 111° → 232° · kadraj 243,4° … 296,6° → ⛔ hiçbir karede kadrajda değil
            kenara geliş 15:31 — filmin bitişinden 51 dakika sonra
⛔ Merdivenin toplamı (3 × 2,00 + 4 × 0,167 = 6,67 sa) pencereyle BİREBİR tutmalıdır.
⚠️ Pencere iki taraftan da ölçülerek daraltıldı: 08:00'den önce bant kadrajı terk eder
   (derinlik > 33 m), 15:31'den sonra güneş kadraja girer.
```

---

## §11 ON RİSK — sırayla, en büyükten

```
①  ⛔ G7'de defter 1,000 çıkmaz            → plan geçersiz. Pilot 1 bunu ölçer; başka hiçbir
                                              ölçümün önemi yoktur. h_son bir tercih değil, kök.
②  ⛔ Gölge kenarı boyanır (eğim yatay)     → §2ⓒ. En olası model hatası ve en kolay yakalanan.
③  ⚠️ Sekme ışığı yok, gölge siyah          → §2ⓑ. Dar sokak dışarıda gibi davranır.
④  ⚠️ Yarıgölge sabit kalır                 → §2ⓐ. Gölge hesaplanmıyor, kopyalanıyor.
⑤  ⚠️ A sahnelerinde bant kayar             → §3. TIME RATE sertleştirilir.
⑥  ⚠️ G0'da bant belirir                    → sahada eşiği aşan bir nesne var; kaldırılır.
⑦  ⚠️ Saçak hattı kesilir/kırılır           → paydanın kendisi bozulur; 26,00 m tek hat şarttır.
⑧  ⚠️ Kadraja vinç/direk girer              → §7. Kendi gölgesi bandın üstüne düşer.
⑨  ⚠️ Bant doruk karede 163 px'ten dar      → ölçüm sütunu daralır; istasyon yönü yeniden bakılır.
⑩  ⚠️ LUT kontrastı itilir                  → kenar yumuşar, defter ölçülemez. LUT §2'den SONRA kilitlenir.
```
