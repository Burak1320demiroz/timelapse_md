# 🔍 BACK TO WATER — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦ ⑨ ⑪ ⑫).
> Plan: `BACK_TO_WATER_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md`

```
FİLM      BACK TO WATER · 7 × 8,0 = 56,0 sn · KAPAK KARTI YOK · LOGO YOK
SCENE BLOCK / END CARD    56,0 sn / yok
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok
REJİM     S0 A (10 dk) · S1–S5 B (2 sa) · S6 ⭐ G gerçek zaman 1× — depoda üçüncü koşu, ölçülmedi
SAHNE SAATLERİ  07:00 → 07:10 → 09:10 → 11:10 → 13:10 → 15:10 → 17:10 → +8 sn (tek gün)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① TEKNE KAPININ ÖTESİNDE — kıç eşiği (y %47) geçmiş, gövde iki kule arasında ya da ötesinde,
    kırmızı-lacivert, kabin krem; İZİ kapıdan havuza giriyor
  ② HAVUZ DOLU VE BOŞ — su rıhtımın 1 m altında, üst 3 basamak kuru, havuzda tekne YOK
  ③ tek figür doğu rıhtımında, sırtı dönük; halat sarılı

⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 54,0'ta tekne HAREKET HÂLİNDE olmalı: 54,0 ve 55,0 karelerinde kıç farklı y'de (≈ 3 m ≈ 40–60 px
   o mesafede). Duran tekne = S6 atılır.
⭐ İKİNCİ KABUL (araç yavaş çıkarırsa · plan §S6 ⑥): 56,0'da kıç eşiğin ÜSTÜNDE, baş açık denizde —
   kabul edilir; SPEC §7 ④'e ölçülen hız yazılır. Kıç kapının İÇİNDE ise (y < %47) FİNAL DEĞİLDİR.
⛔ 56,0'da film tekne UZAKLAŞIRKEN kesilir; sonrasında kart, logo, fade YOK.
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR)

| ne | beklenen | tolerans |
|---|---|---|
| ⭐ deniz ufku (y) | %79,8 · tam yatay | ±0,5 puan · SEKİZ KAREDE DE · eğikse istasyon KAYMIŞTIR |
| ⭐ batı kapı kulesi (x) | %12,4 | ±0,5 puan · SEKİZ KAREDE DE (I2V çapası) |
| ⭐ doğu kapı kulesi (x) | %59,0 | ±0,5 puan · SEKİZ KAREDE DE |
| kapı üst kenarı (y) | %68,3 | ±1 puan · G0–G5 (G6–G7'de kapı açık, kuleler ölçülür) |
| kapı eşiği (y) | %47,0 | ±1 puan |
| ⭐ sarı merdiven (x) | %70,7 | ±0,5 puan · SEKİZ KAREDE DE |
| merdiven dibi / tepesi (y) | %42,8 / %60,3 | ±1 puan · G0–G5 dip görünür · G6–G7 üst 3 basamak |
| doğu babası (x · y) | %68,1 · %61,8 | ±1 puan |
| batı babası (x · y) | %10,1 · %60,8 | ±1 puan |
| G0–G5 tekne kıç güverte (y) | %32,6 | ±1 puan · ALTI KAREDE DE (takozda, kıpırdamaz) |
| G0–G5 tekne baş güverte (y) | %56,1 | ±1 puan |
| G0–G5 tekne kıç / baş (x) | %75,8 / %39,8 | ±1 puan |
| tekne boyu (px, güverte hattı) | 451 px | ±25 px · G0–G6 |
| kabin (x) | %48,9 | ±1 puan · G0–G6 |
| G6 tekne kıç güverte (y) | %42,1 (yüzer: +1,8 m) | ±1,5 puan |
| G7 tekne kıç su hattı (y) | ≥ %47 (eşik) · hedef %60,6 | — |
| G7 tekne (x) | %26–45 | ±3 puan |
| delik A (x · y) | %43 · %29 · 68 × 41 px | ±2 puan · G1–G2 |
| delik B (x · y) | %33 · %44 · 42 × 26 px | ±2 puan · G1–G2 |
| gök | üst %20 | ufuk %80'de; gök %25'i aşıyorsa tilt KAYMIŞTIR |

## 3. ⭐ TEKNENİN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  KABUK bütün gövdede · kıç iskelede 1 m pale şerit · delik 0 görünür · kabin gri astar, cam 0 ·
    takozda · kapı KAPALI · su 0 · yıkama ünitesi batı rıhtımı · 2 hortum · makaslı platform kıçta
G1  kıç 2/3 PAS bandı, ön 1/3 kabuk · delik 2 (A kıç alçak · B kabin altı) YIRTIK · cam 0 · kapı
    KAPALI · aynı ekipman · taban ıslak
G2  GRİ çıplak çelik kıç → baş · delik 2, KARE kesilmiş · levha A SAPANDA (kanca yüklü), levha B
    kasada · branda + 3 torba + 2 kesik parça tabanda · kamyon doğu rıhtımında · kazan batı rıhtımı
G3  gri + 2 LEVHA dikişli · delik 0 · maske bandı su hattında · sprey ünitesi batı · palet kıçta ·
    kamyon YOK · kazan YOK · branda YOK
G4  KIRMIZI + LACİVERT, tek çizgi · levha görünmez · kabin gri + ilk krem bandı · cam 0 · cam kasası
    + krem varilleri güvertede · boş variller rampa dibi
G5  aynı gövde · kabin KREM · cam 5 · güverte BOŞ · taban süpürülmüş · ekipman 0 · takozda, KURU ·
    kapı KAPALI · menfezden ilk su · 2 baş + 2 kıç halatı
G6  havuz DOLU (üst 3 basamak kuru) · tekne YÜZÜYOR (takozdan 1,8 m yukarı) · kapı AÇIK · egzoz pusu ·
    pervane suyu · batı halatı gevşek · figür 1 doğu rıhtımı, halat elinde · kıç halatları YOK
G7  tekne KAPININ ÖTESİNDE, kıç eşikten 1 m · iz kapıdan içeri · havuzda tekne 0 · figür 1 · halatlar
    sarılı · su seviyesi G6 ile aynı

⛔ GERİ GİDİŞ YOK: açılan gövde yeniden kabuklanmaz (G1→G2); kapatılan delik açılmaz (G3→); boyanan
   yüzey griye dönmez; takılan cam düşmez; yükselen su inmez (G6→G7).
⛔ IŞINLANMA YOK: yıkama ünitesi yalnız S1'in İÇİNDE çıkar; kamyon ve kazan yalnız S2'nin İÇİNDE;
   platform + variller + kasa + branda + sprey yalnız S4'ün İÇİNDE; kıç halatları yalnız S5'in İÇİNDE.
⛔ LEVHA HAVADA BELİRMEZ (F08): G2 sapanda → S2 iner → G3 dikişli. Sapansız süzülen levha = KLİP ATILIR.
⛔ TEKNE HAVADA BELİRMEZ: S5'te kalkış SUYLA, takozdan, tam görüşte; su olmadan yükselen tekne = KLİP ATILIR.
```

## 4. ⭐ YÜK YOLU KAPISI — S2 ve S5 [FIZIK_VE_AGIRLIK §4 · beş soru ②③]

```
S2  ① levha SAPANLA iner — iki sapan, tek düşey kablo, kanca yüklü; kamyon doğu rıhtımında, bom havuz üstünde
    ② levha açıklığa OTURUR, kaynak dolanır — G3'te levha yerinde, dikiş halkası görünür
    ③ kesik parçalar + torbalar KASAYA (yukarı, sapanla) → kamyon sağdan çıkar (BEDEL gider)
S5  ① su MENFEZDEN gelir (kapı dibi, iki kule) — kaynak görünür; "yoktan" yükselen su = klip atılır
    ② tekne su hattı geçilince KALKAR — kalkış anında omurga takozdan ayrılır, tam görüşte
    ③ kapı ancak seviye EŞİTLENİNCE kayar (sıra: dolum → kalkış → eşitlenme → kapı → motor → halat)
⛔ Levha sapansız inerse, tekne susuz kalkarsa: ARAÇ sorgulanır, prompt değil.
```

## 5. ⭐ SU SAATİ VE KAPI KAPISI — S5 [dış sebep-sonuç zinciri]

```
① BASAMAK       merdiven basamakları SIRAYLA batar; tek hamlede dolan havuz = F05 sıvı büyüme → klip atılır
② KALKIŞ        tekne 3,2 m'de kalkar (takoz 1,2 + çekim 2,0): S5 klibinde su kırmızıyı ÖRTMEDEN
                tekne yükselmez; erken kalkan tekne = fizik ihlali, klip atılır
③ SEVİYE        G6'da iç ve dış su TEK yüzey — kapı açıkken basamak farkı/şelale YOK
④ KAPI          keson DOĞU kulesine KAYAR (yukarı kalkmaz, menteşeyle açılmaz); G6'da yuva görünür
⑤ HALAT         S5 boyunca baş halatları GERGİN (tekne yükselirken tutulur); G6'da batı gevşek,
                doğu elde; kıç halatları S5 sonunda gider
```

## 6. ⭐ TEK HAVUZ · TEK TEKNE · TEK KAPI KAPISI [DERS 55]

```
SAYIM   havuz 1 · tekne G0–G6: 1 (havuzda) · G7: 0 havuzda + 1 denizde · kapı 1 · merdiven 1 ·
        kule 2 · baba 2 · kabin camı 5 (G5'ten sonra) · delik 2 (G1–G2) · levha 2 (G3) — SEKİZ KAREDE DE
⛔ İkinci havuz, ikinci tekne (havuzda, denizde, rıhtımda), ufukta gemi, tersane vinci = KARE ATILIR.
⛔ G7'de havuz BOŞ: hayalet tekne, ikinci tekne = KARE ATILIR.
⛔ G0 (kabuklu) ve G5 (boyalı) AYNI teknedir: kabin biçimi, 5 cam, direk + baca, 14 m boy, takoz
   konumu — farklı tekne = ⑤ DEVAMLILIK düşer, kare atılır.
⛔ Araç kapısının ⑨ SAYIM TESTİ'yle ÖNCEDEN ölçülür; kapıda çıkarsa ARAÇ DEĞİŞİR.
```

## 7. ⭐ REJİM G KAPISI — S6 [SANTIYE_HAREKETI §1 · üçüncü koşu]

```
① GÖLGE SABİT     G6 · G7'de batı duvarı gölgesinin su üstündeki kenarı aynı yerde (0° fark)
② İZ YOK          motion streak, bulanık ekip, hayalet nesne YOK; tekne NET; deniz DALGALI (ipek değil)
③ FİGÜR           tek · sırtı kameraya · yüz okunmaz · G6 halat babadan kalkıyor, G7 halat sarılı
④ HIZ             1×: kıç d 9 → 27 (18 m / 8 sn ≈ 2,25 m/s); baş eşiği ≈ 2,0 sn, kıç eşiği ≈ 7,0 sn
                  (günlük §4'e ölçülür) · ikinci kabul: kıç eşiğin üstünde (§1)
⑤ RİJİT GÖVDE     tekne 0 · 4 · 8 sn'de aynı boy (perspektifle küçülür, KISALMAZ), 5 cam, 1 direk;
                  kapıdan geçerken kule tarafından kesilen kısım kesilir, deforme olmaz
⑥ SU              iz kıçtan çıkar ve kapıdan İÇERİ döner; havuz suyu duvarlara çarpar — durgun
                  havuz + hareketli tekne = fizik ihlali
⛔ Bunlardan biri düşerse S6 yeniden üretilir; ölçüm günlük §4'e, sonra DERSLER'e (kart D).
⚠️ KAPI KARARI: S5 çok yüklüyse (dolum + kalkış + kapı + motor) kapı açılışı S6'nın ilk 1 sn'sine
   alınabilir — o zaman G6'da kapı KAPALI, S6 0–1 sn'de kayar, baş eşiği ≈ 3 sn. Sahip kararı;
   günlük §6'ya sapma yazılır.
```

## 8. Zaman ve ışık

```
IŞIK GÜNÜ   07:00 → 17:10 = 10 sa 10 dk · 1×A + 5×B + 1×G (G ışık gününe 0 dk) ≤ 14 sa
GÜNEŞ       kadrajda HİÇ görünmez — bakış KKD 20°, güneş 97° → 258° hep arkada · disk anılmaz [DERS 39]
GÖLGE       07:00 doğu duvarı gölgesi bütün havuzda · 09:10 takoz sırasına çekilir · 11:10 taban aydınlık ·
            13:10 baş duvarı gölgesi yakın tabanda, iskele bordası güneşte · 15:10 batı duvarı gölgesi
            takozlara · 17:10 batı duvarı gölgesi suyun batı 3 m'sinde, tekne su üstü aydınlık
UFUK        her karede %80, tam yatay — kıyı çapası [SAHA §3.3]
DENİZ       G0–G5 (A · B): ipek düz ("flat and silky") · G6–G7 (G): doğal dalga — 48,0 dikişi beyanlı
G6–G7       IŞIK AYNI — LIGHTING bloğu iki karede birebir; gölge kıpırdamaz
MEVSİM      eylül ortası · tek gün · gök açık, ince sirrus
⛔ KIŞ YOK — tek günlük film [DERS 7 · 26]
```

## 9. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM        süreler eşit (7 × 8,0) — proje sahibinin kesin kuralı, beyanlı
① / ③ İKİ DİKİŞ   8,0 (A → B: okunur figür → iz) ve 48,0 (B → G: iz → net · ipek deniz → dalga) —
                  beyanlı; müziksiz 46,0–48,0 penceresi ikinciyi taşır; yeniden üretim sebebi DEĞİLDİR
⑦ S6 "İŞSİZ"      S6'da iş yoktur, ÖDÜL vardır — usta kare kasıtlı [plan §KONSEPT KAPISI · §S6]
⑧ TEK GÜN         kabuk → boya → yüzme bir ışık gününde — beyanlı stilizasyon [plan §AŞAMA MERDİVENİ]
① KEYSTONE        −22° tilt'te kule düşeyleri hafif yakınsar — sekiz karede AYNI olduğu sürece
                  istasyon kayması DEĞİLDİR
① SANCAK KÖŞESİ   G0–G5'te kıçın sancak köşesi %94 (UI bandı) — kanıt taşımaz, beklenen
⚠️ İKİNCİ TEKNE    beklenen DEĞİL — çıkarsa §6 gereği araç değişir
⚠️ SIVI DOLUM      beklenen DEĞİL — çıkarsa §5 gereği klip atılır
⚠️ SAPANSIZ LEVHA  beklenen DEĞİL — çıkarsa §4 gereği araç sorgulanır
⚠️ SUSUZ KALKIŞ    beklenen DEĞİL — çıkarsa §4 gereği klip atılır
```
