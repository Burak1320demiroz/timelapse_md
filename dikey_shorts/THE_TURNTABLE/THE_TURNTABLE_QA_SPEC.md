# 🔍 THE TURNTABLE — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_TURNTABLE_DIKEY_TIMELAPSE.md` · Günlük: `THE_TURNTABLE_URETIM_GUNLUGU.md` · Kapak: `THE_TURNTABLE_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE TURNTABLE · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 22.10.2026 · kural 7 × 8 · sahibin notu G0 → G8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "THE TURNTABLE") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 G (gerçek zaman, 1×) — tek dikiş 56,0'da
IŞIK      İÇ MEKÂN S0–S6 SABİT soğuk beyaz (iki tripod iş lambası) · DIŞARIDA SAAT TEK YÖNDE, açık gök: 05:55 → … → 19:55 → 19:55:08 (güneş
          saati) · 41° kuzey · 21 Haziran (δ +23,4°) · kamera 0°'ye (kuzey) bakar, tilt 0, 24 mm · yeraltı: güneş HİÇBİR karede yok ·
          zaman portalın ötesindeki rampada (sol duvar → taban → sağ duvar → mavi) · final MAVİ SAAT: petek, platform, loca yanar
AİLE      İÇ MEKÂN (bekleyen) · platform %29,5–40,1 · başlık alanı uzak kaya tonoz + portalın üstündeki alın duvarı
TAKVİM    sahneler arasında haftalar (KESMEDE), sahne içinde 2 sa / 8 sn (beyanlı)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① ARAÇ + PLATFORM — TEK alçak koyu grafit iki kişilik spor araç buzlu cam platformun ORTASINDA (araç x 400–680 · py 1059–1292),
    burnu kameraya, farları yanık · platform alttan beyaz parlar (x 140–940 · py 1150–1354) · kadrajın EN PARLAK şeyi platform + araç ·
    gövde düz ve İŞARETSİZ (marka, plaka, logo, yazı YOK)
  ② TAVAN — TEK altıgen ışık çerçevesi peteği yumuşak beyaz yanık (uzak kenarı py ≤ 533) · yedi koyu çelik kemer kaburga · üstte
    çıplak kaya tonoz
  ③ LOCA + VİTRİN — sağ duvarda cam korkuluklu balkon sıcak ışıkta, iki sıra BOŞ deri koltuk + bar · sol duvarda TAM DÖRT cam vitrin
    hafif ışıklı · alt duvarlarda kömür panel + meşe çıta, amber ışık çizgileri yanık
  ④ TANIKLAR — portal açık (x 459–621 · py 922–1024), ardında mavi saatte beton rampa + koyu mavi gök lekesi · portalın tepesinde SARILI
    kapı · uzak tonoz + alın duvarı KOYU (başlık zemini) · parlak koyu zemin yansıtır · insan yok, makine yok, geçici eşya yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–60,0'da (2x: 28,0–30,0) araç rampadan portala, zeminin ortasından platforma SÜREKLİ yolla gelir ve durur. Işınlanır (portal →
   platform tek adım), ikiye çıkar, durduktan sonra döner ya da kayarsa → S7 atılır [DERS 96 · 103].
⛔ ≈ 58,0'da (2x: 29,0) petek, ≈ 60,0'da (2x: 30,0) platform + loca yanar ve HEPSİ yanık kalır. Titrer, söner, yeniden yanarsa → S7 atılır
   [DERS 98].
⛔ Platform DÖNERSE (sahip seçimi: dönmez) → S7 atılır.
⛔ Işık yanarken loca, vitrin, korkuluk, petek KAYARSA / yeni nesne belirirse (ikinci araç, insan, barmen, neon, duman, lazer) → S7 atılır
   [DERS 91 ③].
⛔ Petek ya da loca ışığı başlık bandını (py 560–770) aydınlatırsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık, erime
   ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta motor rölantisi + armatür uğultusu (dijital sessizlik DEĞİL) [DERS 100].
⛔ Araç camının ardında bir yüz okunursa ya da bir figür belirirse S7 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0 · 24 mm · h 2 m)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk / kaçış noktası | py 960 (%50) · portalın ortası | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ portal + alın duvarı | portal x 459–621 · py 922–1024 · alın duvarı tepesi py 704 | DOKUZ KAREDE AÇIK (nirengi ①) · hiçbir karede kapalı kapı yok |
| ⭐ platform çemberi | x 140–940 · py 1150–1354 | KESİR ±7 px · DOKUZ KAREDE (nirengi ②) · 800 px değilse lens kaymıştır → G8 yeniden |
| ⭐ tünel kesiti | sol duvar dibi Y 20 → (162, 1088) · tonoz tepesi Y 14 → py 229 | DOKUZ KAREDE (nirengi ③) |
| ⭐ kaburgalar | Y 10 · 14 · 18 · 22 · 26 · 30 · 34 | G0–G1 yok · G2→ TAM YEDİ |
| ⭐ balkon | ön kenar x 900 → 706 · py 853 → 911 · korkuluk üstü py 736 → 857 | G2→ sağ duvarda · G5→ cam korkuluk |
| ⭐ ışık peteği | x 300–780 (uzak kenar) · py 0–533 | G5→ · G5–G7 SÖNÜK · G8 yanık · uzak kenar py ≤ 533 |
| ⭐ vitrinler | x 108 → 310 · py 928–1120 | G6→ TAM DÖRT |
| ⭐ mini vinç | G0 çukurun solu (x ≈ 90) · G1 çukurun sağı · G2 portalın içinde solda (x ≈ 383–428) | G0–G2 · kanca HER KAREDE YÜKLÜ · G3→ yok |
| ⭐ iş lambaları | x ≈ 203 · 810 · py ≈ 920 | G0–G6 · G7→ yok |
| ⭐ araç | G7 rampada x 517–563 · py 964–996 · G8 platformda x 400–680 · py 1059–1292 | TEK · burnu kameraya iki karede de |
| işçi | Y 14'te ≈ 160 px · Y 30'da ≈ 75 px | DÖRT · yüz yok, kameraya dönük kimse yok · G7–G8 yok |

## 3. ⭐ GALERİNİN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ kaba gri beton döşeme (toz, su birikintisi) · çıplak nemli kaya · çukurda çıplak beton halka temeli · ⭐ mini vinç çukurun solunda,
    kancada dişli halka çukurun hemen üstünde · göbekli çerçeve çukurun sağında takozda · sağ duvarda kaburga yarısı istifi + kiriş demeti ·
    iki iş lambası · küçük ekip
G1  ⭐ halka temelde, çerçeve üstünde cıvatalı · ⭐ vinç çukurun sağında, kancada TEK kaburga yarısı · istif küçük · dört işçi sol duvarda
G2  ⭐ TAM YEDİ kaburga · sağ duvarda balkon iskeleti + merdiven · ⭐ vinç portalın içinde solda park (kancada kaldırma kirişi) · panel
    paletleri + çıta demeti + makaslı platform sol duvarda
G3  ⭐ alt duvarlarda (≈ 4 m) kömür panel + meşe çıta, üstte çıplak kaya · balkon yüzü panelli · vinç YOK · cam arabası çukurun yanında ·
    epoksi varilleri sağ duvarda · boş paletler + platform portal yanında
G4  ⭐ duvardan duvara koyu epoksi · ⭐ buzlu cam disk · içeride YALNIZ iki iş lambası · sandıklar + korkuluk arabası RAMPADA, ekip yanında
G5  ⭐ ışık peteği SÖNÜK · cam korkuluk · portalın tepesinde SARILI kapı · makaslı platform + mobilya sandıkları portal yanında
G6  ⭐ iki sıra deri koltuk + bar balkonda · TAM DÖRT vitrin · platform + yıkama makinesi + iki alet arabası + boş sandıklar
G7  ⭐ parlak boş zemin · YALNIZ amber yanık · ⭐ rampada araç, farlar yanık · insan YOK · mavi saat
G8  ⭐ araç platformun ortasında · petek + platform + loca + vitrin + amber YANIK · insan YOK
⛔ SAYIM: tünel 1 · platform 1 · portal 1 · kaburga (0·0·7·7·7·7·7·7·7) · petek (0·…·0·1·1·1·1) · balkon (0·0·1·…) · vitrin (0·…·0·4·4·4) ·
   vinç (1·1·1·0·…) · makaslı platform (0·0·1·1·0·1·1·0·0) · yıkama makinesi (0·…·0·1·0·0) · araç (0·…·0·1·1) · iş lambası (2·…·2·0·0) ·
   işçi (ekip·4·4·4·4·4·4·0·0) — kadro HİÇBİR klipte dördü aşmaz [DERS 89] · hareketli araç HİÇBİR anda birden fazla değil [DERS 69]
⛔ Tünel kesiti, kaya tonoz, platform çemberi, alın duvarı, portal ve rampa dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  halka: kanca (dört sapan) → DÜŞEY iniş → beton halka temeli → cıvata · çerçeve: takoz → kanca → halka · kaburga yarısı: istif → kanca
S1  kaburga yarısı: istif → kanca → taban plakası (dik) → halatla tutulur → çifti → tepede cıvata (platformun üstünden portala, TAM yedi) ·
    düz kiriş: demet → kanca → sağ duvardaki ankraj · merdiven: → balkonun uzak ucu · vinç: → portalın içinde park · makaslı platform: rampa
    → portal → sol duvar · panel paleti: portal → el transpaleti → sol duvar
S2  vinç: portal → rampa → kadraj dışı · panel: palet → ekip → platform → alt duvar · çıta: demet → derz · boş palet: → portal yanı ·
    cam arabası: portal → çukur · epoksi varili: portal → sağ duvar
S3  cam: araba → vakum tutucu → göbekli çerçeve · araba + platform: → portal → rampa · epoksi: varil → döşeme (kameradan portala) · boş
    varil + rulo: → portal · sandıklar: rampa → portalın hemen ötesi
S4  makaslı platform + sandıklar: rampa → portal → koruma tahtası · ışık çerçevesi: sandık → platform → tonoz halatı (platformun ötesinden
    kameraya) · cam panel: araba → merdiven → balkon kenarı · sarılı kapı: zincirli vinç → portalın tepesi · mobilya sandıkları: portal → tahta
S5  koltuk: sandık → merdiven → balkondaki YERİ (yüzü platforma) · bar: iki parça → balkonun uzak ucu · vitrin: sandık → el transpaleti →
    sol duvar (portal ucundan kameraya) · yıkama makinesi + alet arabaları: rampa → portal
S6  makaslı platform: → portal → rampa · parlaklık: yıkama makinesi → zemin (kameradan portala) · sandık, ambalaj, tahta: zemin → alet arabası
    → portal · iş lambaları: ekip → portal · yıkama makinesi + ekip: → rampa · araç: rampanın yukarısında durur
S7  araç: rampa → portal → zeminin ortası → platform · ışık: iki adım → petek → platform + loca
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı portal, istif, palet, sandık ya da araba [DERS 48 · 49].
⛔ Uzun rijit yük havada uzun yol TAŞINMAZ [DERS 57]: kaburga yarısı istiften plakaya kısa salınım + dik oturma. Bütün kemer tek parça
   gökten İNMEZ [DERS 79].
⛔ Epoksiden sonra ağır makine zemine koruma tahtası olmadan GİRMEZ: S4–S6 makaslı platform tahtada; S6'da yıkama makinesi zeminin
   kendisini parlatır.
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI · DERS 104]

```
G0     05:55 (71,1°/+14,2°) · ⭐ rampanın SOL duvarında alçak sabah güneşi · taban gölgede · gök lekesi solgun
G1     07:55 (89,2°/+36,4°) · sol duvar tümüyle ışıkta, taban kenarı
G2     09:55 (114,2°/+58,5°) · taban solu
G3     11:55 (176,2°/+72,4°) · ⭐ bütün taban beyaz
G4     13:55 (242,7°/+60,2°) · taban sağı
G5     15:55 (269,1°/+38,3°) · ılık · SAĞ duvar tümüyle
G6     17:55 (287,4°/+16,0°) · ⭐ yalnız sağ duvarın üstü altın, taban gölgede
G7     19:55 (306,2°/−4,1°) · ⭐ erken mavi saat · rampa mavi · içeride YALNIZ amber çizgiler
G8     19:55:08 · ⭐ aynı mavi · petek + platform + loca + vitrin YANIK · uzak tonoz KOYU
⛔ Rampadaki ışık TEK YÖNDE yürür (sol duvar → taban → sağ duvar → mavi); geri dönen kare = zaman ters → ❷ [DERS 98 · 104]
⛔ İç mekân G0–G6 boyunca AYNI soğuk beyaz (iki iş lambası) — iç ışığın rengi değişirse "grade" okunur [DERS 104]
⛔ G0–G6 boyunca hiçbir galeri ışığı yanmaz · amber G7'de ilk kez
⛔ Portal patlarsa (beyaz düz dikdörtgen, rampa okunmuyorsa) zaman taşıyıcısı ölür → kare yeniden
```

## 6. ⭐ BİR TÜNEL · BİR ARAÇ · DÖRT İŞÇİ · TEK HAREKETLİ ARAÇ KAPISI [DERS 55 · 69 · 89 · 42]

```
Korpus riski: "car gallery / lounge" → ikinci araç, sergi sırası, misafir, barmen, parti, plaka, logo, neon, duman · "construction" →
kalabalık ekip, ikinci makine (ÇIKARIM — bu filmde ölçülmedi). crowd · guests · bartender · party · neon · laser · smoke · fog · fireworks ·
racing · drifting promptta YOK; "supercar" ve "VIP" kelimeleri prompta girmedi.
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ) · "Only four workers" ve "Exactly one vehicle moves at a time" her I2V'de · G7–G8'de
  "No people are present."
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç makine aynı anda / kaç kaburga / kaç vitrin
⛔ ikinci araç · ikinci platform · sekizinci kaburga · beşinci vitrin · ikinci loca · misafir · barmen · beşinci işçi · aynı anda iki hareketli
   araç · iki makinenin birbirinin içinden geçmesi · parlak zemindeki yansımanın NESNE gibi çizilmesi → ⑧
⛔ Model tünel kesitini, platform çemberini, alın duvarını ya da portalı yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Araçta, vitrinlerde, panellerde okunur yazı (marka, plaka, logo, numara) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 çerçeve + ilk kaburga yarısı · S1 balkon iskeleti, vinç parkı, paletler · S2 kaplama sağ yanda, cam arabası, varillerle · S3 koyu
  zemin portala, sandıklar rampada · S4 sarılı kapı, mobilya sandıkları · S5 raflar, yıkama makinesi · S6 amber, araç rampada · S7 tutuş
  (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · kalabalık sesi YOK · tünel yankısı + rampadan uzak rüzgâr yatak · metal çarpışma, patlama YOK
· 0,0 vinç motoru + halat · halkanın oturuşu (tok) · cıvata tabancası · 8–15 kaburgaların oturuşu (tok ×çok) · 16–23 platform hidroliği, vida
  ve çivi tabancası · 24–31 vakum tıslaması, rulo sürtünmesi · 32–39 hidrolik, zincirli vinç · 40–47 ambalaj, adımlar, transpalet · 48–55
  yıkama makinesi · ⭐ 55,0 amber rölesi · 56–60 aracın alçak motoru, tünelde yankı, lastikler · ⭐ 58,0 röle + uğultu (petek) · ⭐ 60,0
  ikinci röle (platform + loca) (KARE SENKRON ±2 kare) · 60,0–64,0 rölanti + uğultu
· KART 64,0–69,0: rölanti + uğultu sürer, kartın son saniyesinde söner → döngüde S0'ın vinç motoruna bağlanır
```

## 9. Zaman ve ışık

```
G0 05:55 71,1°/+14,2° · G1 07:55 89,2°/+36,4° · G2 09:55 114,2°/+58,5° · G3 11:55 176,2°/+72,4° · G4 13:55 242,7°/+60,2° ·
G5 15:55 269,1°/+38,3° · G6 17:55 287,4°/+16,0° · G7 19:55 306,2°/−4,1° · G8 19:55:08 (aynı)
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · açık gök · sahneler arası haftalar KESMEDE)
· zaman portalın ötesindeki rampanın gün ışığıyla taşınır (sol → taban → sağ → mavi); final mavi saatte, araç ve galeri ışıklarıyla
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (not G0 → G8), beyanlı
① KADRAJ        24 mm · tilt 0 · h 2 m · yakın duvarlar kadraj dışı (Y < 14) · alt üçte bir boş parlak zemin · portal ve rampa küçük
                (162 × 102 px) · loca sağ kenarda dar kama — beyanlı
⑤ DEVAMLILIK    platformun içi (çukur → halka → cam → ışık) ve duvar/zemin rengi KASITLI değişir; tünel kesiti, tonoz, çember, portal
                DEĞİŞMEZ · vinç yalnız G0–G2, iş lambaları G0–G6, araç G7–G8 KASITLI
❷ ZAMAN         zaman yalnız portalda görünür (yeraltı — sahip seçimi "hep açık portal"); iç ışık sabit · mercek "zaman zayıf" diyebilir;
                sahneler arasında haftalar, saat tek yön (beyanlı)
⑦ İŞ            S7'nin 4–8'inde iş yok (kasıtlı tutuş) · G7–G8 insansız (kasıtlı) · finalde hareket yapının çalışması (araç + ışık)
                [SANTIYE_HAREKETI §4.7]
❺ TESLİM        işlev anı ışık — LAST STOP · GAME ON · TOTAL RESET · POOL ROOM · UNDERWATER OBSERVATORY · COLOSSUS'ta da var (yedinci,
                sahip onayladı 22.10.2026) · SKY VAULT · HIDDEN LOFT · UNDERWATER OBSERVATORY ile malzeme/mekân/ışık akrabası — beyanlı
⑫ YANSIMA       parlak zeminde aracın ve peteğin yansıması — KASITLI; nesne gibi çizilirse ⑧
```
