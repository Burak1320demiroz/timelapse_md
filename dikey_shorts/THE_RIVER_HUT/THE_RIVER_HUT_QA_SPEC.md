# 🔍 THE RIVER HUT — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_RIVER_HUT_DIKEY_TIMELAPSE.md` · Günlük: `THE_RIVER_HUT_URETIM_GUNLUGU.md` · Kapak: `THE_RIVER_HUT_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE RIVER HUT · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 27.10.2026 · kural 7 × 8 · sahibin briefi "8 × 8 sn, tek zincir, 9 G, tek adam") · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "ONE MAN BUILDS / A RIVER SHELTER") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 G (gerçek zaman, 1×) — tek dikiş 56,0'da
IŞIK      DIŞ MEKÂN · SAAT TEK YÖNDE, açık gök: 06:25 → … → 20:25 → 20:25:08 (güneş saati) · 41° kuzey · 21 Haziran (δ +23,4°) · kamera 0°'ye
          (kuzey, nehir boyunca) bakar, tilt 0, 24 mm, h 2,0 m · güneş HİÇBİR karede yok · zaman gölgelerde (sabah sola → öğle altta → akşam
          sağa) ve suda · final MAVİ SAAT (−8,5°): pencere S6'da ısınır, fener S7'de TEK KAREDE yanar
AİLE      KÜTLE · ana yapı = sığınak + iskele + fener (py 806–1286) · başlık alanı sığınağın üstündeki koyu ağaçlık yamaç (py 560–770 — beyanlı
          sapma, KAPAK_STIL §2.2)
TAKVİM    sahneler arasında günler (KESMEDE), sahne içinde 2 sa / 8 sn (beyanlı)
EKİP      ⚠️ TEK ADAM (sahip seçimi 27.10.2026) — kapının "≥ 3 el" FIX'i beyanlı; yoğunluk akışla (taş yatağı · istif · yığın · kabuk · çim)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① FENER — iskelenin ucundaki kısa direkte, demir kancada (x ≈ 957 · py ≈ 1088) sıcak sarı YANIK · ışığı akan suyun ÜSTÜNDE tek, kırık,
    titreşen dikey sütun (x ≈ 940–975 · py ≈ 1290–1500) · sütun karaya, düzlüğe ya da pencerenin altına DÜŞMEZ · ayna yansıması, hüzme YOK
  ② ADAM — TAM bir insan, iskelenin ucunda oturuyor, ayakları suyun üstünde, yüzü nehre, sırtı kameraya · yüz okunmuyor
  ③ SIĞINAK — diz boyu taş taban + sekiz sıra kütük + yeşil çim çatı (x 315–596 · mahya py 806 · taban py 1183) · kapı hafif aralık,
    pencere ve kapı aralığı sıcak turuncu · TAM bir ince boru, ince duman SAĞA, başlık bandının ALTINDA · iskele iki kazıkta (py 1194–1286)
  ④ TANIKLAR — nehir (seviye G0 ile aynı) + kıyı + TAM üç kaya · SOĞUK taş halka (alev, duman, köz YOK) · devrik kütük · çadır köşesi ·
    çıplak toprak kareleri · el arabası + ip çadırın yanında · iki ladin (x 135 / 912) · koyu ağaçlık yamaç · dar koyu mavi gök şeridi

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ ≈ 56,5'te (2x: 28,25) fener TEK KAREDE yanar ve YANIK kalır. Titrer, söner, yeniden yanarsa → S7 atılır [ISIK_FINALI · DERS 98].
⛔ 56,5–60,0'da (2x: 28,25–30,0) adam direğin yanından iskelenin ucuna SÜREKLİ hareketle oturur. Işınlanır, ikiye çıkar ya da yüzü
   kameraya dönerse → S7 atılır [DERS 96 · 15].
⛔ Fener yanarken sığınak, iskele, kayalar KAYARSA / yeni nesne belirirse (ikinci insan, kayık, ikinci fener, hayvan, alevli taş halka) →
   S7 atılır [DERS 91 ③].
⛔ Duman ya da ışık başlık bandını (py 560–770) doldurursa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: fener aynı, adam oturuyor, yalnız nehir akar; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63] — ⚠️ akan su
   SSIM'i düşürebilir; eşik altındaysa önce su bölgesi (x > 700 · py > 1190) maskelenip yeniden ölçülür (ÇIKARIM).
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık (iki satır),
   erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta nehir + cırcır böcekleri (dijital sessizlik DEĞİL) [DERS 100].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0 · 24 mm · h 2,0 m)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk | py 960 (%50 — yamacın arkasında, görünmez) | yamacın dibi py ≈ 1095 · kayarsa kamera kaydı |
| ⭐ taş halka | x 353–561 (208 px) · py 1409–1505 | KESİR ±7 px · DOKUZ KAREDE (nirengi ①) · hep SOĞUK |
| ⭐ üç kaya + kıyı | x 864–886 · py 1242–1677 · kıyı x 667 (alt) → 770 (Y 11,5) | DOKUZ KAREDE (nirengi ②) · TAM üç |
| ⭐ ladinler + çadır | ladin x 135 / 912 · çadır x 0–72 · py 1098–1387 | DOKUZ KAREDE (nirengi ③) |
| devrik kütük | x 95–635 · py 1562–1713 | DOKUZ KAREDE |
| ⭐ nehir seviyesi | su yüzü düzlüğün 0,8 m altı · kıyı çizgisi aynı | DOKUZ KAREDE · kuruma/taşma YOK |
| ⭐ taş yatağı | x 721–791 · py ≈ 1158 | G0 dolu → G1 küçük → G2 çok küçük → G3→ aynı |
| ⭐ kütük istifi | x 108–331 · py 1037–1131 | G0–G1 uzun → G2 → G3 küçülür → G4 çok küçük → G5 birkaç → G6 yok (son iki kütük kıyıda) |
| ⭐ malzeme yığını | x 170–324 · py 1198–1326 | G0–G5 aynı · G6 yalnız fener + ip · G7→ yok (ip çadırda) |
| ⭐ taş taban | x 315–596 · üst py 1127 · alt py 1183 | G0 ön sıra · G1 üç kenar · G2→ tam, diz boyu |
| ⭐ kütük duvar | saçak py 949 | G3 üç sıra · G4→ sekiz sıra · kapı x 512–578 · pencere x 362–409 · py 1005–1060 |
| ⭐ çatı | mahya (çimli) py 806 · boru tepesi x 556 · py 822 | G5 çıplak iskelet · G6→ branda + çim · boru G6→ |
| ⭐ iskele + kazıklar | x 770–958 · py 1194 · kazıklar 1286'ya | G7→ · TAM iki kazık, suyun İÇİNDE · iç ucu kıyıda |
| ⭐ fener | x 957 · py 1088 | G0–G6 yığında · G7 direkte SÖNÜK · G8 YANIK |
| çim kareleri | düzlüğün solu (x ≈ 45–324 · py 1131–1173) | G6→ çıplak toprak kareleri |
| adam | Y 7'de ≈ 320 px (baş 42) · Y 11,5'te ≈ 195 px (baş 26) | TAM BİR · yüz yok · kameraya 7 m'den fazla yaklaşmaz |

## 3. ⭐ SIĞINAĞIN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ kazık + iple dikdörtgen, ön kenarda TEK sıra taş, solda iki taş · adam taş dolu el arabasını İTİYOR · kürek çakılda · uzun istif ·
    kayışlı yığın · nehirde sabah sisi
G1  ⭐ ön + sol + sağ kenar tek sıra · ARKA AÇIK · taş yatağı küçüldü · adam kürekle düzlüyor · boş el arabası · sis yok
G2  ⭐ diz boyu taş taban tamam, üstü düz · kazık + ip çakılda · iki kızak sırığı tabana dayalı · adam istifte ilk kütüğe ip bağlıyor
G3  ⭐ iki taban kirişi + üç sıra kütük, köşeler çentikli · sırıklarda bir kütük yarı yolda · istif küçüldü · kabuk + talaş · balta istifte
G4  ⭐ SEKİZ sıra · kapı ve pencere boşluğu ÖN duvarda · istif çok küçük + kabuk yığını · adam pencereyi testereyle düzeltiyor
G5  ⭐ iki dikme + mahya + sırıklar: çıplak beşik çatı iskeleti · istifte birkaç kütük · adam sağ duvarın üstünde son sırığı bağlıyor
G6  ⭐ yeşil branda + çim — yeşil çatı · ⭐ pencere (camı karanlık) · ⭐ boru · çıplak toprak kareleri · son iki kütük kıyıda · yığında
    yalnız fener + ip · adam tahta demetini kıyıya taşıyor
G7  ⭐ iskele iki kazıkta · ⭐ kapı · pencere ve kapı aralığı turuncu · ince duman · direkte SÖNÜK fener · adam iskele ucunda elini fenere
    uzatmış · mavi saat
G8  ⭐ fener YANIK · sudaki kırık ışık sütunu · ⭐ adam oturuyor
⛔ SAYIM: sığınak 1 · adam 1 (dokuz karede) · kaya 3 · ladin 2 · çadır 1 · taş halka 1 (soğuk) · el arabası 1 · kızak sırığı (0·0·2·2·2·2·0·0·0)
   · kütük sırası (0·0·0·3·8·8·8·8·8) · dikme (0·…·0·2·2·2·2) · pencere çerçevesi (0·…·0·1·1·1) · boru (0·…·0·1·1·1) · kazık (0·…·0·2·2) ·
   fener 1 (yığında → direkte) · kapı (0·…·0·1·1) — ikinci insan HİÇBİR klipte yok [DERS 89] · makine yok, motor yok
⛔ Nehir, kıyı, üç kaya, taş halka, devrik kütük, çadır, yamaç ve ladinler dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  taş: taş yatağı → el arabası → dikdörtgen (sol, sonra sağ kenar; TEK yük) · çakıl: kürek → arka kenarın dışındaki küçük yığın
S1  taş: taş yatağı → el arabası → arka kenar + ikinci sıra · dolgu: çakıl → kürek → tabanın içi → tokmak · kazık + ip: → çakıl ·
    kızak sırıkları: istif → tabanın önü
S2  kütük: istif → ip → çakılda sürükleme → kızak sırıkları → taban (TEK TEK) · çentik: balta → köşe · kabuk: → istifin yanı
S3  kütük: istif → ip → sırıklar → üst sıra (SIRA SIRA, alttan) · kapı/pencere boşluğu: el testeresi → ön duvar · kırpıntı: → el arabası →
    kabuk yığını
S4  dikme: istif → ön + arka duvar · mahya: → sırıklar → dikmelerin üstü · sırık: istif → mahya + yan duvar (ÖNDEN ARKAYA, tek tek) → ip
S5  branda: yığın → çatı (saçaktan) · çim: düzlüğün solu → kürek → el arabası → çatı (saçaktan mahyaya) · pencere: yığın → boşluk ·
    soba: yığın → kapıdan İÇERİ · boru: yığın → çatı
S6  kazık: son iki kütük → suya → tahta tokmak (adam diz boyu suda) · iskele: iki uzun sırık + tahta demeti → kıyıdan dışa · kapı: tahta →
    menteşe · fener: yığın → direk → kanca
S7  ışık: tek adım → fener · adam: direğin yanı → iskele ucu (oturur)
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı taş yatağı, istif, yığın ya da çim düzlüğü [DERS 48 · 49 · 95].
⛔ Kanca, vinç, asılı yük, makine YOK — her şey ip, kızak sırığı ve el arabasıyla [plan TASARIM ⑪].
⛔ Soba görünmeyen hedeftir: içeri TAŞINIR, yakılışı yazılmaz; yalnız SONUÇ (pencere ısınır, duman çıkar) [DERS 95].
⛔ İskele yüzmez: kazıklar ÖNCE, iç ucu kıyıda [plan RİSKLER ③].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI · DERS 45 · 98]

```
G0     06:25 (75,6°/+19,7°) · ⭐ sağdan (nehrin üstünden) alçak altın ışık, gölgeler uzun SOLA · nehirde ince sis
G1     08:25 (94,3°/+42,1°) · sağdan, gölgeler kısalır · sis kalktı
G2     10:25 (124,2°/+63,5°) · sağ-arkada yüksek, kısa gölgeler sola ve kameraya
G3     12:25 (198,5°/+71,7°) · ⭐ tepede, kameranın arkasında · gölge kütüklerin altında
G4     14:25 (251,2°/+55,0°) · soldan yüksek, kısa gölgeler SAĞA
G5     16:25 (273,9°/+32,7°) · soldan, sırıkların çizgili gölgeleri duvarların içine ve SAĞA
G6     18:25 (291,9°/+10,7°) · ⭐ altın akşam, uzun gölgeler SAĞA, suya düşer · çim çatı sıcak
G7     20:25 (311,6°/−8,5°) · ⭐ mavi saat, doğrudan ışık yok · pencere + kapı aralığı TURUNCU · fener SÖNÜK
G8     20:25:08 · ⭐ aynı mavi · fener YANIK + sudaki kırık sütun · başlık bandı koyu yamaç
⛔ Gölgeler TEK YÖNDE döner (sola → altta → sağa); geri dönen kare = zaman ters → ❷ [DERS 98]
⛔ G0–G5 pencere yok/karanlık · G6 camı karanlık · ilk sıcak ışık G7'ye giden klipte, tek yönde · fener ilk kez G8'e giden klipte, TEK KAREDE
⛔ G7–G8 zifiri karanlık değildir: sığınak, iskele, kayalar, adam okunur [DERS 45]; okunmuyorsa kare yeniden
```

## 6. ⭐ BİR SIĞINAK · TEK ADAM · MAKİNESİZ · YAZISIZ YÜZEY KAPISI [DERS 55 · 59 · 69 · 89 · 42]

```
Korpus riski: "shelter" → tahkimat, sığınak kapısı · "log" → büyük kır evi, ikinci kulübe · "ring of stones" → kamp ateşi · "lantern" →
dizi ışık, ikinci fener (ÇIKARIM — bu filmde ölçülmedi). bunker · cabin · campfire · chimney · chainsaw · crane · hoist · tractor · boat ·
drone · neon · beam promptta YOK (YASAK KELİME).
① sayım cümlesi her karede POZİTİF ("This is one gravel flat with one shelter site and one man, the only person in view") · "Only one man is
  in view for the whole shot — no one else ever appears — and he does one job at a time" her I2V'de
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç insan / kaç kaya / kaç kazık / kaç fener
⛔ ikinci insan · ikinci kulübe · kayık · dördüncü kaya · üçüncü kazık · ikinci fener · ikinci boru · motorlu alet · makine · hayvan → ⑧
⛔ Model kayaları, kıyıyı, taş halkayı, çadırı ya da ladinleri yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Çadırda, brandada, malzeme yığınında ya da kapıda okunur yazı (harf, rakam, logo) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 iç düzlenir, çakıl yığını büyür · S1 dolgu + tokmak, kızak sırıkları kalkar · S2 sonraki iki sıra · S3 pencere düzlenir, kabuk yığını ·
  S4 sırıklar arkaya doğru, kırpıntı yığına · S5 pencere, soba, boru · S6 kapı, pencere ısınır, adam iskele ucuna · S7 tutuş (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · motor YOK, testere motoru YOK · NEHİR bütün filmin yatağı · ormanda rüzgâr
· 0,0 el arabası gıcırtısı, taşın taşa oturuşu · 8–15 çakıl, tokmak · 16–23 ipin gerilişi, kütüğün sırıklarda yuvarlanışı, balta · 24–31 balta,
  el testeresi · 32–39 mahyanın oturuşu, ip · 40–47 branda hışırtısı, kürek, sobanın metal tıkırtısı · 48–55 tahta tokmak (suyun içinden),
  çekiç, menteşe, 55,0 sobanın ilk çıtırtısı · ⭐ 56,5 fenerin yanışı (tek kibrit çıtı, KARE SENKRON ±2 kare) · 56,5–60,0 tahtanın gıcırtısı ·
  60,0–64,0 nehir + cırcır + uzaktan soba
· KART 64,0–69,0: nehir + cırcır sürer, kartın son saniyesinde söner → döngüde S0'ın el arabası gıcırtısına bağlanır
⛔ Müzik ya da konuşma → teslim değil (sahip kuralı 21.09.2026)
```

## 9. Zaman ve ışık

```
G0 06:25 75,6°/+19,7° · G1 08:25 94,3°/+42,1° · G2 10:25 124,2°/+63,5° · G3 12:25 198,5°/+71,7° · G4 14:25 251,2°/+55,0° ·
G5 16:25 273,9°/+32,7° · G6 18:25 291,9°/+10,7° · G7 20:25 311,6°/−8,5° · G8 20:25:08 (aynı)
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · açık gök · sahneler arası günler KESMEDE)
· zaman gölgelerle ve suyla taşınır (sabah sağdan sola → öğle altta → akşam soldan sağa); final mavi saatte pencere + fener
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 × 8), beyanlı
① KADRAJ        24 mm · tilt 0 · h 2,0 m · zemin Y < 2,7 m'de kadraj dışı · sığınak 281 px (%26) · pencere 47 px · fener küçük, ışığı ile okunur ·
                başlık bandı yamaç (gök değil) — beyanlı
⑤ DEVAMLILIK    taş taban, kütük duvar, çatı, iskele KASITLI büyür; taş yatağı, istif, yığın KASITLI küçülür; çim kareleri KASITLI açılır; nehir,
                kıyı, kayalar, taş halka, çadır, yamaç, ladinler DEĞİŞMEZ
❷ ZAMAN         zaman gölgelerde ve suda; sahneler arasında günler, saat tek yön (beyanlı) · rejim dikişi 56,0'da (su ipeksi → gerçek akış)
⑦ İŞ            ⚠️ TEK ADAM (sahip seçimi) — "tek el, düşük yoğunluk" denebilir; yoğunluk akışla taşınır · S7'nin 4–8'inde iş yok (kasıtlı
                tutuş) · finalde hareket evin kullanılmasıdır (fener + oturan adam) [SANTIYE_HAREKETI §4.7]
❺ TESLİM        işlev anı ışık — YAYIN_PLANI'na göre ON BİRİNCİ (LAST STOP · GAME ON · TOTAL RESET · POOL ROOM · UNDERWATER OBSERVATORY ·
                COLOSSUS · THE TURNTABLE · LIT AGAIN · THE READING CAR · THE DRIVE-IN), plana girmemiş OPENING NIGHT · SUNKEN GARDEN · MENDED
                SPAN ile on dördüncü · fark: ışık suyun üstünde kırık bir sütun, tek adamın kendi evi · SUNKEN GARDEN (taş halka, oturan
                insan) ve LIT AGAIN (kıyıda fener) ile akraba — beyanlı
⑬ BAŞLIK        kart başlığı 6 kelime, iki satır (sahip seçimi; KAPAK_STIL "1–3 kelime" der) — beyanlı
```
