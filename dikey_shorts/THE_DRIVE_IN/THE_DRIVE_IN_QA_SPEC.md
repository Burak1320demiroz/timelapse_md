# 🔍 THE DRIVE-IN — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_DRIVE_IN_DIKEY_TIMELAPSE.md` · Günlük: `THE_DRIVE_IN_URETIM_GUNLUGU.md` · Kapak: `THE_DRIVE_IN_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE DRIVE-IN · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 26.10.2026 · kural 7 × 8 · sahibin briefi "8 × 8 sn, tek zincir, 9 G") · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "DEAD GAS STATION / TO DRIVE-IN CINEMA") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 G (gerçek zaman, 1×) — tek dikiş 56,0'da
IŞIK      DIŞ MEKÂN · SAAT TEK YÖNDE, açık gök: 06:25 → … → 20:25 → 20:25:08 (güneş saati) · 41° kuzey · 21 Haziran (δ +23,4°) · kamera 0°'ye
          (kuzey) bakar, tilt 0, 24 mm, h 12 m · güneş HİÇBİR karede yok · zaman gölgelerde (sabah sola → öğle altta → akşam sağa) ve gökte ·
          final MAVİ SAAT (−8,5°): kanopi altı ışık şeridi S6'da yanar, perde S7'de TEK KAREDE yanar
AİLE      KÜTLE · ana yapı = perde + kolonları + kanopi (py 781–1335) · başlık alanı perdenin üstündeki açık gök (py 560–770)
TAKVİM    sahneler arasında haftalar (KESMEDE), sahne içinde 2 sa / 8 sn (beyanlı)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① PERDE — kanopinin ARKASINDA, kendi iki çelik kolonunda (x 313 / 767), alt kenarı kanopi çatısının belirgin üstünde · baştan başa TEK
    durağan resimle YANIK (alçak turuncu güneşin altında sakin deniz) · resimde yazı, insan, logo YOK · ışık hüzmesi, duman YOK
  ② ARABALAR — TAM on iki araba, iki sıra × altı (yakın sıra py 1557–1813 · uzak sıra py 1367–1499), burunları perdeye, ışıkları SÖNÜK ·
    son araba uzak sıranın sağdan ikincisinde (x ≈ 678) · kaput ve tavanlarda seyirci, sırtı kameraya, yüz okunmuyor
  ③ SİNEMA — TAM on iki park yeri, beyaz çizgi · TAM altı hoparlör direği · kanopi altı ışık şeridi sıcak beyaz YANIK · asfalt koyu yamalı
  ④ TANIKLAR — kanopi + TAM dört kolon (x 324–756 · alın şeridi py 1165–1190, temiz beyaz) · iki boş ada · üç camlı dükkân · yol pilonu
    (x 972–1065, boş gri, SÖNÜK) · yan yol · iki kavak · ufuktaki sedde · koyu mavi gök · işçi yok, makine yok, geçici eşya yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ ≈ 56,5'te (2x: 28,25) perde TEK KAREDE yanar ve YANIK kalır. Parça parça "dolarsa", titrer, söner, yeniden yanarsa → S7 atılır
   [ISIK_FINALI · DERS 98].
⛔ Perdedeki resim hareket eder, değişir, kayar ya da yazı/harf/insan belirirse → S7 atılır [DERS 59].
⛔ 56,5–60,0'da (2x: 28,25–30,0) son araba şeritten uzak sıranın sağdan ikinci yerine SÜREKLİ yolla gelir ve ışıkları söner. Işınlanır,
   ikiye çıkar ya da başka bir yerden belirirse → S7 atılır [DERS 96].
⛔ Perde yanarken arabalar, direkler, kanopi KAYARSA / yeni nesne belirirse (on üçüncü araba, işçi, tabela, harfli afiş, hüzme) → S7
   atılır [DERS 91 ③].
⛔ Perdenin ışığı başlık bandını (py 560–770) aydınlatırsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: resim aynı, arabalar park, seyirci oturuyor, hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık (iki satır),
   erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta cırcır böcekleri + sözsüz deniz uğultusu (dijital sessizlik DEĞİL) [DERS 100].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0 · 24 mm · h 12 m)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk | py 960 (%50) | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ kanopi + dört kolon | alın şeridi x 324–756 (432 px) · py 1165–1190 · kolonlar x 382 / 698 | KESİR ±7 px · DOKUZ KAREDE (nirengi ①) · TAM dört kolon |
| ⭐ pilon | x 972–1065 · tepe py 594 · kutu altı py 1234 | DOKUZ KAREDE aynı (nirengi ②) · yazısız · hiç yanmaz |
| ⭐ kavaklar + ufuk | kavak x ≈ 231 · tepe py 777 · ufuk 960 | DOKUZ KAREDE (nirengi ③) |
| ⭐ pompalar | x 440 · 490 · 590 · 640 · py 1264–1317 | G0 dört (biri çatalda) · G1 iki adada + iki kamyonda · G2→ yok |
| ⭐ kanopi rengi | G0–G1 kirli, sol ön panel sarkık · G2→ temiz beyaz | alın şeridinde yazı/logo YOK |
| ⭐ asfalt | G0 otlu çatlak · G1–G2 anız · G3→ koyu yamalı · G6→ + 12 park yeri | park yerlerinde rakam YOK |
| ⭐ temeller | x 313 / 767 · py ≈ 1267 | G3→ TAM iki |
| ⭐ perde iskeleti | kolonlar x 313 / 767 · py 781–1267 · çaprazlar py 986 · 917 · 849 · 781 | G4→ · kanopiye DEĞMEZ · TAM iki kolon + dört çapraz |
| ⭐ perde | x 324–756 · py 781–986 (432 × 205 px) | G5→ · G5–G7 boş · G8 durağan resim |
| ⭐ ışık şeridi | kanopi alın şeridinin altı | G5→ · G5–G6 sönük · G7–G8 yanık |
| ⭐ park yerleri + direkler | uzak sıra x 244–836 · py 1367–1499 · yakın sıra x 72–1008 · py 1557–1813 | G6→ TAM 2 × 6 · TAM altı direk |
| ⭐ arabalar | G7 on bir + biri şeritte (x 792–980 · py 1482–1557) · G8 on iki | G0–G6 yok · on üçüncü yok |
| kamyon | x ≈ 777–866 · py 1241–1412 | G0–G1 · G3–G5 · aynı yer ±20 px |
| vinç | x ≈ 820–860 · py 1225–1335 + bom | yalnız G4 · gövdesi görünür, kanca yüklü |
| forklift | x ≈ 435 (G0) / 590 (G1) · py 1266–1335 | G0–G1 |
| işçi | Y 20'de ≈ 112 px · Y 43'te ≈ 52 px | TAM İKİ · yüz yok · G7–G8 yok |

## 3. ⭐ SİNEMANIN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ otlu çatlak asfalt · kirli kanopi, sol ön panel sarkık · dört paslı pompa: en soldaki forklift çatalında, kayışlı · kamyon kanopinin
    sağında, kasası boş · palet + betoniyer + el arabası kanopinin solunda · iki işçi (forklift · tırpan)
G1  ⭐ sol ada boş (cıvata kökleri) · iki pompa kamyonda · forklift sağ adada · ⭐ ot biçildi, yakın solda TEK yığın
G2  ⭐ iki ada boş · kamyon, forklift, yığın YOK · ⭐ kanopi alın şeridi temiz beyaz, panel düz · iki işçi palette
G3  ⭐ koyu yamalı parsel · ⭐ iki beton temel · kamyon döndü: iki kolon + çapraz demeti + sandıklar
G4  ⭐ boş iskelet: iki kolon + dört çapraz · ⭐ vinç kanopinin sağında, kancada beyaz panel · kamyonda yalnız sandıklar
G5  ⭐ beyaz perde (boş) · vinç YOK · ⭐ kanopi altında ışık şeridi (sönük) · kamyonda boş sandıklar · merdiven
G6  ⭐ 12 park yeri · ⭐ altı direk · kamyon, palet, merdiven YOK · işçiler betoniyerli el arabasıyla girişte · altın akşam
G7  ⭐ on bir araba park + 12. şeritte (farlar açık) · seyirci kaputlarda · ⭐ ışık şeridi YANIK · perde boş · mavi saat · işçi yok
G8  ⭐ perde YANIK, durağan resim · ⭐ on iki araba park, ışıklar sönük
⛔ SAYIM: kanopi 1 · kolon 4 · ada 2 · dükkân 1 · pilon 1 (dokuz karede) · pompa (4·4·0·…) · temel (0·0·0·2·2·2·2·2·2) · perde kolonu
   (0·…·0·2·2·2·2·2) · perde yüzü (0·…·0·1·1·1·1) · park yeri (0·…·0·12·12·12) · direk (0·…·0·6·6·6) · araba (0·…·0·12·12; G7'de 11 park +
   1 şeritte) · forklift (1·1·0·…) · kamyon (1·1·0·1·1·1·0·0·0) · vinç (0·0·0·0·1·0·0·0·0) · işçi (2·2·2·2·2·2·2·0·0) — kadro HİÇBİR klipte
   ikiyi aşmaz [DERS 89] · aynı anda TEK makine hareketi [DERS 69]
⛔ Kanopi ve dört kolonu, adalar, dükkân, pilon, yan yol, kavaklar ve ufuk dokuz karede DEĞİŞMEZ (kanopinin yalnız rengi temizlenir).
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  pompa: sol ada → forklift çatalı (kayış) → kamyon kasası (iki pompa, tek tek) · ot: tırpan → tırmık → yakın soldaki yığın
S1  pompa: sağ ada → çatal → kamyon (iki) · ot yığını: yaba → kamyon · kanopi şeridi: çataldaki çelik iş kafesi → fırça (soldan sağa) ·
    sarkık panel → cıvata · kamyon: → giriş → yan yol, ARDINDAN forklift
S2  soğuk asfalt: palet → el arabası → çatlak → tokmak (kanopiden kameraya) · beton: betoniyer → el arabası → iki çukur → ankraj · çelik +
    sandık: yan yol → giriş → kamyon (kanopinin sağı)
S3  vinç: yan yol → giriş → kanopinin sağı → takozlu ayaklar · kolon: kamyon → kanca → temel → cıvata (TEK TEK) · çapraz: demet → kanca →
    kolonlar arası (ALTTAN ÜSTE) · ilk panel: sandık → kanca
S4  panel: sandık → kanca → çerçeve (sıra sıra) → cıvata · boş sandık: → kamyon · vinç: → giriş → yan yol · ışık şeridi: merdiven → kanopi altı
S5  kamyon (boş sandık): → giriş · çizgi: tekerlekli çizgi arabası → asfalt (uzak sıra önce) · direk: matkap → cıvata (altı) · merdiven, boş
    palet, son torbalar: → giriş · betoniyer: → el arabası
S6  işçiler + el arabası + betoniyer: → giriş → yan yol · araba: yan yol → giriş → şerit → park yeri (TEK TEK, uzak sıra önce) · insan:
    araba → kaput/tavan · ışık şeridi: yanar (tek yön)
S7  ışık: tek adım → perde · son araba: şerit → uzak sıra sağdan 2.
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı kamyon, palet, sandık ya da yan yol [DERS 48 · 49].
⛔ Perde iskeleti kanopiye OTURMAZ, kanopiden destek almaz — kendi iki temeli [plan TASARIM ④].
⛔ Basınçlı su, hortum, püskürtme YOK — kanopi yalnız elle, fırçayla [DERS 67]. Çizgi tekerlekle sürülür, püskürtülmez.
⛔ Forklift kamyona BİNMEZ; iki araç aynı anda hareket etmez [DERS 69].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI · DERS 45 · 98]

```
G0     06:25 (75,6°/+19,7°) · ⭐ sağdan alçak altın ışık, kanopi, pompa, pilon gölgeleri uzun SOLA
G1     08:25 (94,3°/+42,1°) · sağdan, gölgeler kısalır
G2     10:25 (124,2°/+63,5°) · sağ-arkada yüksek, kısa gölgeler sola ve uzağa · temiz kanopi parlak
G3     12:25 (198,5°/+71,7°) · ⭐ tepede, kameranın arkasında · gölge altta
G4     14:25 (251,2°/+55,0°) · soldan yüksek, kısa gölgeler SAĞA
G5     16:25 (273,9°/+32,7°) · soldan, gölgeler uzar SAĞA · perde yandan ışık
G6     18:25 (291,9°/+10,7°) · ⭐ altın akşam, uzun gölgeler SAĞA, perde soluk altın
G7     20:25 (311,6°/−8,5°) · ⭐ mavi saat, doğrudan ışık yok · ışık şeridi YANIK · perde BOŞ, SÖNÜK · son arabanın farları
G8     20:25:08 · ⭐ aynı mavi · perde YANIK (durağan resim) · başlık bandı koyu mavi
⛔ Gölgeler TEK YÖNDE döner (sola → altta → sağa); geri dönen kare = zaman ters → ❷ [DERS 98]
⛔ G0–G7 boyunca perde yanmaz · ilk kez G8'e giden klipte, TEK KAREDE · pilon HİÇ yanmaz
⛔ G7–G8 zifiri karanlık değildir: arabalar, çizgiler, seyirci okunur [DERS 45]; okunmuyorsa kare yeniden
```

## 6. ⭐ BİR İSTASYON · İKİ İŞÇİ · TEK MAKİNE · YAZISIZ YÜZEY KAPISI [DERS 55 · 59 · 69 · 89 · 42]

```
Korpus riski: "drive-in" → ışıklı harfli tabela, afiş, kalabalık, ikinci perde · "fuel station" → marka, fiyat panosu, ikinci kanopi
(ÇIKARIM — bu filmde ölçülmedi). spray · hose · jet · fountain · beam · haze · smoke · neon · marquee · billboard · price · signage promptta YOK.
① sayım cümlesi her karede POZİTİF ("one fuel station lot with one canopy and one entrance, and the only station in view") · "Apart from
  drivers inside their cabs, only two workers are in view … only one machine moves at a time" her S0–S5 I2V'de · G7–G8'de "No workers
  are present"
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç kolon / kaç araba / kaç makine
⛔ ikinci kanopi · beşinci kolon · ikinci perde · ikinci pilon · on üçüncü araba · yedinci direk · üçüncü işçi · ikinci vinç · tabela · fiyat
   panosu · harfli afiş · ışık hüzmesi → ⑧
⛔ Model kanopiyi, kolonlarını, pilonu, dükkânı ya da kavakları yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Pilonda, kanopi şeridinde, pompalarda, asfaltta, plakalarda ya da perdede okunur yazı (harf, rakam, logo, fiyat) → ❶ metin [negatif
   çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 ot biçilir, yığın · S1 kanopi temizlenir, kamyon + forklift çıkar · S2 temeller, kamyon döner · S3 çaprazlar, kancada panel · S4 vinç
  çıkar, ışık şeridi · S5 direkler, işçiler girişe · S6 yakın sıra dolar, ışık şeridi yanar, son araba şeritte · S7 tutuş (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · kalabalık uğultusu YOK · uzak otoyol + rüzgârda ot yatak · basınçlı su YOK · metal çarpışma,
  patlama YOK
· 0,0 forklift bip'i, çatal · 8–15 pompanın kasaya oturuşu, fırça, uzaklaşan kamyon · 16–23 tokmak, betoniyer · 24–31 vinç hidroliği, kolonun
  oturuşu, pnömatik anahtar · 32–39 panellerin oturuşu, uzaklaşan vinç · 40–47 çizgi arabası, matkap · 48–55 araba motorları, kapılar,
  cırcır böcekleri · ⭐ 56,5 tek tık + hoparlörlerden SÖZSÜZ, EZGİSİZ deniz uğultusu (KARE SENKRON ±2 kare) · 56,5–60,0 son arabanın motoru,
  el freni, susma · 60,0–64,0 cırcır + deniz uğultusu
· KART 64,0–69,0: cırcır + deniz uğultusu sürer, kartın son saniyesinde söner → döngüde S0'ın forklift bip'ine bağlanır
⛔ Hoparlörden film müziği ya da diyalog → teslim değil (sahip kuralı 21.09.2026)
```

## 9. Zaman ve ışık

```
G0 06:25 75,6°/+19,7° · G1 08:25 94,3°/+42,1° · G2 10:25 124,2°/+63,5° · G3 12:25 198,5°/+71,7° · G4 14:25 251,2°/+55,0° ·
G5 16:25 273,9°/+32,7° · G6 18:25 291,9°/+10,7° · G7 20:25 311,6°/−8,5° · G8 20:25:08 (aynı)
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · açık gök · sahneler arası haftalar KESMEDE)
· zaman gölgelerle taşınır (sabah sağdan sola → öğle altta → akşam soldan sağa); final mavi saatte ışık şeridi + perde
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 × 8), beyanlı
① KADRAJ        24 mm · tilt 0 · h 12 m · zemin Y < 16 m'de kadraj dışı · pompalar küçük (23 × 54 px) · dükkân 65 px şerit · perde 432 × 205 px
                (resim RENK + UFUK çizgisi olarak okunur) — beyanlı
⑤ DEVAMLILIK    asfalt (otlu → yamalı → çizgili), kanopi rengi (kirli → beyaz), perde (yok → iskelet → beyaz → resim), arabalar (0 → 11 → 12)
                KASITLI değişir; kanopinin biçimi, kolonlar, adalar, dükkân, pilon, kavaklar, ufuk DEĞİŞMEZ · kamyon, forklift, vinç, palet
                KASITLI gelir-gider
❷ ZAMAN         zaman gölgelerde ve gökte; sahneler arasında haftalar, saat tek yön (beyanlı)
⑦ İŞ            S7'nin 4–8'inde iş yok (kasıtlı tutuş) · G7–G8 işçisiz (kasıtlı) · finalde hareket sinemanın kullanılmasıdır (perde + son araba)
                [SANTIYE_HAREKETI §4.7] · S6'da arabalar 900×'te "yerinde belirmiş" okunabilir (gerçek timelapse görünümü, beyanlı)
❺ TESLİM        işlev anı ışık — YAYIN_PLANI'na göre ONUNCU (LAST STOP · GAME ON · TOTAL RESET · POOL ROOM · UNDERWATER OBSERVATORY · COLOSSUS ·
                THE TURNTABLE · LIT AGAIN · THE READING CAR), plana girmemiş OPENING NIGHT ve SUNKEN GARDEN ile on ikinci · fark: perdede
                GÖRÜNTÜ belirir, son araba ona gelir · OPENING NIGHT (dolan çanak, alacakaranlık ışığı) ile akraba — beyanlı
⑬ BAŞLIK        kart başlığı 6 kelime, iki satır (sahip seçimi; KAPAK_STIL "1–3 kelime" der) — beyanlı
```
