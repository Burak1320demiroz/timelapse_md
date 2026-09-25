# 🔍 THE GLASS CROSSING — QA ŞARTNAMESİ

```
FİLM      7 × 8,0 = 56,0 sn · 9:16 · rejim B (S0–S5) + rejim G (S6) · müzik YOK
KAYNAK    dikey_shorts/THE_GLASS_CROSSING/THE_GLASS_CROSSING_DIKEY_TIMELAPSE.md
DURUM     ⛔ ÜRETİLMEDİ — bu dosya ÜRETİMDEN SONRA koşulacak kilit listesidir
ARAÇLAR   araclar/zincir_kontrol.sh (eşik 2 px) · araclar/kare_al.sh · araclar/qa_paket.sh
```

---

## 1. ⭐ FİNAL KARE KANITI — iki ölçü, tek kare (G7)

```
⭐ Bu filmin iddiası "bir şey yapıldı" değil, "bir yüzey ŞEFFAFLAŞTI"dır. Şeffaflık bir SIFAT değildir;
   ancak ARKASINDAKİ ŞEYİN GÖRÜNMESİYLE kanıtlanır. İki bağımsız ölçü yazıldı; ikisi de GEÇMEDEN teslim yok.

KANIT ①  DERE BANDI KESİNTİSİZ Mİ?
         ölç  G7'de %20,05 satırında (üstten y ≈ 1535 px), x %44,3 – %55,7 arası 201 px'lik dilim.
         geç  o 201 px, bandın sağındaki ve solundaki dere ile AYNI ton ve dokuda devam ediyor.
         kal  o 201 px döşeme rengi, beyaz, bulanık ya da "camın altında ikinci bir yüzey" gibiyse.
         ⛔ G6 ile karşılaştır: G6'da aynı 201 px KARA BARDIR. İki kare arasındaki tek fark budur.

KANIT ②  KERESTE YIĞINI GENİŞLEDİ Mİ?
         ölç  G6'da yığının görünen eni 134 px; G7'de 223 px olmalı (×1,67).
         geç  genişleme YALNIZ sol tarafa doğrudur (köprünün örttüğü 4,56 m'lik şerit açılır) ve
              yığının dokusu, rengi, üst hattı iki karede de aynıdır.
         kal  yığına parça eklenmişse, yükselmişse, yer değiştirmişse ya da G7'de İKİ AYRI yığın varsa.
         ⛔ Bu, deponun ilk "bakılarak büyüyen" nesnesidir. Hiç kimse ona dokunmaz.

⛔ SERT KAPI: G6 ile G7, KAPAK ve FİGÜR dışında BİREBİR aynı olmalıdır.
   bash araclar/zincir_kontrol.sh g6.jpg g7.jpg   → kayma ≤ 2 px
   Fark listesi tam olarak ikidir: ① 1. ve 2. gözün beyaz filmi yok  ② figür d 11,00'den d 17,00'ye yürüdü.
   Üçüncü bir fark bulunursa (gölge, korkuluk, yığın, su hattı, bulut) klip DÜŞER.
```

---

## 2. KADRAJ KİLİTLERİ — sekiz karede ölçülür

```
⭐ ÖLÇÜM SIRASI: önce ÜÇ NİRENGİYE bak, sonra yapıya. Boğazda kayadan başka bir şey yoktur ve kaya hiç
   değişmez; kameranın oynamadığını söyleyen tek şey bu üç çapadır [P14-b].

  #   nesne                          beklenen            tolerans    her karede
  A   dere bandı (alt nirengi)       %20,05 · 106 px     ± 2 px      G0 → G7
  B   eski ankraj yuvası (orta)      d 8,50 · 28 px      ± 2 px      G0 dolu → G2+ boş, yeri sabit
  C   çentikli kret + tek çam (üst)  ufuk %93,29         ± 2 px      G0 → G7
  1   güney kenar (yakın mesnet)     %14,27              ± 2 px      G0 → G7
  2   kuzey kenar (uzak mesnet)      %56,12              ± 2 px      G0 → G7
  3   döşeme eni · yakın uç          236 px              ± 3 px      G0 → G7
  4   döşeme eni · orta              106 px              ± 2 px      G0 → G7
  5   döşeme eni · uzak uç            68 px              ± 2 px      G0 → G7
  6   çapraz taşıyıcı aralığı        3,00 m · 9 adet     tam sayı    G3 → G7
  7   figür (G7)                     63 px boy · d 17,00 ± 3 px      yalnız G7
  8   katlanmış film köşesi          38 px               ± 2 px      G5 = G6 aynı piksel

⛔ %93,29 ufkunun ÜSTÜNDE yalnız 129 px gök vardır. Model gökyüzünü büyütürse (ve boğazı küçültürse)
   kare düşer: gök bandı 129 ± 10 px.
⛔ Döşeme eni HİÇBİR karede değişmez. Eski tahta kaplama da, yeni cam da 2,40 m'dir. Model yeni köprüyü
   genişletirse ⑤ DEVAMLILIK düşer — negatif çekirdekteki "the same length and the same width" bunun için.
```

---

## 3. ⭐ GÖRÜNÜRLÜK KAPISI — boşluğun ekran alanı, kare kare

```
kare   boşluk (px²)   dere bandı     ne bekleniyor
G0            0       KESİK          tahta derzi 0,62 px = eşik altı; boğaz SIZMAZ
G1       12 020       KESİK          yalnız kuzey üç göz açık (d 29–38)
G2      104 863       KESİNTİSİZ     iki paslı kiriş dışında her şey açık
G3      100 401       KESİNTİSİZ     ⭐ dokuz boş göz — filmin en açık karesi
G4            0       KESİK          ⛔ beyaz filmli dokuz ünite — boğaz kadrajdan SİLİNDİ
G5            0       KESİK          ⛔ hâlâ sıfır; saha temiz
G6       53 298       KESİK          ⭐ kuzey yedi göz cam, güney iki göz beyaz
G7      111 556       KESİNTİSİZ     dokuz gözün dokuzu cam

⛔ EĞRİ İKİ KEZ SIFIRLANIR ve İKİ KEZ AÇILIR. Deponun diğer 29 filminde ölçülen şey BÜYÜMEDİR; burada
   ölçülen şey bu eğridir. Tek yönlü olan tek nesne kereste yığınıdır (§4).
⚠️ EN BÜYÜK RİSK G4 → G5: iki kare arasında boşluk sıfır kalır ve YAPI değişmez. Ayrım YALNIZ ekipmanın
   gitmesi ve tek bir katlanmış köşedir. Model bu iki kareyi karıştırırsa ② İNŞA düşer.
⚠️ İKİNCİ RİSK S5: klip kadrajdan bir şey ÇIKARIR. Modelin ölçülmüş eğilimi EKLEMEKTİR [P14-h].
   Arıza "film kalkmadı" değil, "film kalktı ama altı boş kalmadı" biçiminde gelecektir — yani model
   camı ikinci bir opak yüzey gibi çizer. Pilot klip budur.
```

---

## 4. ⭐ İKİ DEFTER KAPISI

```
DEFTER ①  ESKİ KÖPRÜ — TEK YÖNLÜ (BEDEL)
          64,8 m² × 50 mm çürük meşe (3,24 m³ ≈ 2,43 t) + 4,50 m'lik parçalara kesilmiş iki paslı kiriş
          (≈2,97 t) boğaz tabanına iner ve ORADA KALIR.
          G0 yok · G1 ~70 px · G2–G6 134 px · G7 223 px (yalnız örtü kalktığı için)
          ⛔ HİÇBİR KAREDE KÜÇÜLMEZ. Yığından bir parça eksilirse ④ TESLİM düşer.
          ⛔ Yığın yukarı çıkmaz, kamyona binmez, kadraj dışına gitmez. Bedel ödenir ve görünür kalır.

DEFTER ②  KORUYUCU FİLM — KAPANAN (İDDİA)
          64,8 m² film, 9 tabaka. Köprünün ÜSTÜNDE başlar, tek tomarda biter.
          G3–G5  9 tabaka (yürüyüş yüzeyi tamamen beyaz)
          G6     2 tabaka + uzak mesnette 1 tomar
          G7     0 tabaka + figürün elinde 1 tomar, arkasında 209 px'lik kuyruk
          ⛔ Sayım tutmalıdır: 9 → 2 → 0. Ara karede "yarım soyulmuş" göz OLMAZ (S6 hariç).

⭐ İKİ DEFTERİN İŞİ AYRIDIR: ① filmin BEDELİNİ, ② filmin İDDİASINI taşır. Biri olmadan öbürü boşlukta
   kalır [P14-g]. Bu filmde ikisi AYNI KARE ile kanıtlanır: G7'de yığın genişler ve tomar ele geçer.
```

---

## 5. YÜK YOLU KAPISI — ⛔ VİNÇ YOK

```
⛔ "crane" kelimesi hiçbir promptta geçmez ve kadrajda hiçbir vinç görünmez. Boğazın üstüne bom uzanamaz.
   Bir vinç belirirse klip DÜŞER — gerekçe fizik, estetik değil.

720 kg'lık cam ünitenin yük yolu, G3'te kare kare izlenebilir olmalı:
   palet (kaya sahanlığı) → sapan → GEÇİCİ TEL üstündeki makara → boğazın üstü → sapan iner →
   neopren şerit → iki çelik kenar rayı → kaya braketleri → kaya
Asma çalışma sahanlığının yolu:
   dört tel sapan + iki tagline → köprünün ALTINDA asılı; G5'te tamamen GİDER ve bir daha gelmez.
Geçici telin yolu:
   iki kısa direk (her kenarda bir tane), gergi telleri terasa ankrajlı; G5'te direkler de GİDER.

⛔ ASILI CİSİM TAŞIYICISIZ OLAMAZ [FIZIK_VE_AGIRLIK §4]: havada duran her parçanın promptta bir sapan,
   halat ya da teli vardır. G3'te "üniteler yerine gelir" gibi bir okuma ⑧ YÖNTEM merceğini düşürür.
⛔ G5 ve sonrasında kayada HİÇBİR geçici ekipman kalmaz — geriye yalnız sapanın sürttüğü açık renk
   kaya izi (scar) ve braket deliklerinin altındaki delme tozu kalır. O izler G5 → G7 SABİTTİR.
```

---

## 6. GÖLGE KAPISI

```
kare   saat            azimuth   elevation   gölge yönü   beklenen
G0     06:00              84°        5°         264°      sağdan alçak; her kaya çıkıntısı uzun gölge
G1     08:00             106°       27°         286°      güney kenarın gölgesi taban boyunca solda
G2     10:00             135°       45°         315°      gölgeler kısalır, çakıl barları beyazlar
G3     12:00             180°       54°           0°      ⭐ gölgeler kadrajda YUKARI düşer; taban aydınlanır
G4     14:00             225°       45°          45°      gölgeler sağa dönmeye başlar
G5     16:00             254°       27°          74°      korkuluk iki uzun ince gölge atar
G6     18:00             276°        5°          96°      son alçak ışık soldan; kuzey kenar turuncu
G7     18:00 + 8 sn      276°        5°          96°      ⛔ G6 İLE BİREBİR AYNI

toplam süpürme 191,5°  ·  ışık günü 12,00 sa  ≤ 14 sa

⛔ G6 = G7 gölge kimliği SERT KAPIDIR: S6 rejim G'dir, 8 saniyede gölge 0,03° döner ve bu 1 px'in altındadır.
   G7'de gölge kıpırdamışsa rejim ihlali vardır ve klip DÜŞER.
⛔ Güneş hiçbir karede kadrajda değildir (yatay yarı açı 26,57°, güneş 84°–276°). Disk görünürse kare düşer.
⚠️ G3 günün TEK anıdır ki boğaz tabanının orta hattı doğrudan aydınlanır (güneş 53,1°'nin üstünde).
   Diğer altı karede taban AÇIK GÖLGEDEDİR — bu hata değil, tasarımdır [P15-f]. Taban siyah değil,
   mavi-gri olmalı; dere gökyüzünü yansıttığı için en parlak nesnedir.
```

---

## 7. SAYIM KAPISI

```
BİR boğaz · BİR geçit · BİR kereste yığını · BİR asma sahanlık (G0–G4) · İKİ direk (G0–G4) · DOKUZ göz
⛔ İKİNCİ BİR KÖPRÜ, patika, merdiven, tekne, tabela, bank, dürbün YOKTUR.
⚠️ RİSK KARESİ G5: bitmiş, temiz, bomboş beyaz bir yol. Model kadrajı DOLDURMAK ister. Negatif çekirdekteki
   "never bridged anywhere else" ve sayım cümlesi bunun içindir. G5'te fazladan bir nesne belirirse kare düşer.
⚠️ İKİNCİ RİSK: model boğaza SU YÜKSELTİR (dere → nehir) ya da taban ekler. Dere ALÇAKTIR ve çakıl barları
   açıktadır; bu mevsim taşıyıcısıdır ve sekiz karede aynıdır.
```

---

## 8. REJİM G KAPISI — S6

```
süre        8,0 sn gerçek zaman · 1×
mesafe      6,00 m (iki göz) · hız 0,750 m/s SABİT — hızlanma, yavaşlama, durup devam etme YOK
figür       ⛔ sırtı kameraya dönük, yüzü hiç görünmez. Bu talimatla değil GEOMETRİYLE sağlanır:
            hat kameradan UZAĞA gider [P14-d]. Figür dönerse klip DÜŞER.
film        1. göz 1,0–3,0 arasında, 2. göz 3,0–5,5 arasında cama döner. Filmin kalkışı SÜREKLİDİR;
            "bir anda kaybolma" olmaz. Tomar elinde BÜYÜR, kuyruğu camda sürünür.
gölge       ⛔ HİÇ HAREKET ETMEZ (bkz. §6)
bulut       ⛔ HİÇ KAYMAZ — "the haze lying along the gorge holds still"
⛔ 8 saniyede kadrajda başka hiçbir şey değişmez: korkuluk, taşıyıcılar, yığın, su, kaya, yamaç.
```

---

## 9. SES KAPISI — ⛔ MÜZİK YOK

```
⛔ 0,0–56,0 arasında tek nota müzik YOKTUR [sahip kuralı 21.09.2026]. Ses yatağı diegetiktir.
⭐ SESSİZLİK PENCERESİ 46,0 – 48,0 — film soyulması biter, yatak düşer, yalnız rüzgâr ve çok aşağıdan su.
   Bu pencere filmin "beklenti" aracıdır. Doldurulursa ④ TESLİM düşer.
⭐ CAMDA AYAK SESİ (48,0+) tok, kısa ve YANKISIZ olmalı — tahtadan ve betondan farklı. Filmin tek
   "ses kanıtı" budur: zemin GÖRÜLMEDEN de duyulur.
⛔ Master'a hiçbir metin basılmaz; başlık yalnız platform satırındadır.
```

---

## 10. ZAMAN VE IŞIK

```
konum        44° kuzey · geç yaz · δ +8°
gündüz       13 sa 02 dk (05:29 – 18:31)
klipler      06:00 → 18:00 = 12,00 sa = 6 klip × 2 sa (rejim B) ≤ 14 sa
pay          06:00'dan önce 31 dk · 18:00'den sonra 31 dk
rejim        ⛔ İKİ TANE: B (S0–S5) ve G (S6). Üçüncü rejim yoktur.
mevsim       alçak su + açıkta çakıl barları + tam koyu huş yaprağı. Sekiz karede aynı.
⛔ Mevsim ÖNCE seçilmedi: 6 × 2 sa = 12 sa'nın gündüze sığması gerektiği için δ +8° ÇÖZÜLDÜ [P14-e].
```

---

## 11. BİLİNEN RİSKLER — üretim öncesi liste

```
① ⭐ CAM RENDER'A KAÇAR. Negatif çekirdekte "no architectural visualisation look" var ve AI'ın camda
   ilk gittiği yer tam orası. Çözüm promptta değil YAPIDA: her 3,00 m'de koyu çapraz taşıyıcı (7,93 px),
   her gözde 60 mm alüminyum çerçeve (4,63 px), her kenarda 40 mm yeşil lamine çizgi (3,09 px).
   Sınav: G7'de cam "yok" gibi mi görünüyor, yoksa ÇERÇEVELİ BOŞLUK gibi mi?
② ⭐ MODEL CAMI İKİNCİ BİR BEYAZ YÜZEY SANAR (S5 · pilot). En olası arıza budur.
③ G4 ile G5 birbirine karışır (boşluk ikisinde de sıfır). Ayrım yalnız ekipman + katlanmış köşe.
④ Model boğazı DARALTIR ya da altına destek koyar. Negatif çekirdekte "nothing is ever built underneath it".
⑤ Model köprüyü GENİŞLETİR (cam tahtadan geniş olsun diye). Döşeme eni sekiz karede 2,40 m.
⑥ Rejim B'de işçiler net çıkar (streak olmaz). Rejim G'de figür döner.
⑦ Panel derzi (0,93 px) ve derz kapağı (1,93 px) eşik altındadır ve promptta YOKTUR; model onları
   çizerse kadrajda moiré üretir [P14-f].
⑧ ⛔ DEVAM EDEN AÇIK — P13-h: prompt_kontrol.py §9'un metin yasağı KAPSAM denetimi
   "…annotated by anyone" ifadesini arıyor, deponun negatif çekirdeği ise "…included." ile bitiyor.
   Sekiz yüzey sayımı bu yüzden HİÇBİR filmde ateşlenmedi. Bu film de ev yazımıyla yazıldı;
   bulgu sahip kararı olarak taşınıyor.
⑨ ⛔ ARAÇ KUTU SETİ ÖLÇÜLMEDİ — yedi ölçüm koşulup üretim günlüğü §0 doldurulmadan tek kare üretilmez.
```
