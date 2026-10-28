# 🔍 THE HIDDEN LAWN — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_HIDDEN_LAWN_DIKEY_TIMELAPSE.md` · Günlük: `THE_HIDDEN_LAWN_URETIM_GUNLUGU.md` · Kapak: `THE_HIDDEN_LAWN_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE HIDDEN LAWN · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 27.10.2026 · kural 7 × 8 · brief "8 × 8 sn, 9 G, tek adam" — sorulmadı) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "THE HIDDEN LAWN") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 2 ara kare (G4a · G7a) + 10 klip (S4 · S7 ikişer 4 sn alt klip) · T2V yok ·
          ⭐ üretim sırası G8 (metinden) → G7a (G8'den kapak dik + adam ağızda) → G7 … G0 (geriye) · ⚠️ merceklere 8 SAHNE; alt klip
          dikişleri (36,0 · 60,0) sahne İÇİDİR, kesme sayılmaz
REJİM     S0–S6 + S7·a B (900× · 2 sa / 8 sn, alt klipte 1 sa / 4 sn) · S7·b G (gerçek zaman, 1×) — tek rejim dikişi 60,0'da
IŞIK      SAAT TEK YÖNDE · 05:00 → … → 19:00 → 20:00 → 20:00:04 (güneş saati) · 45° kuzey · mayıs sonu (δ +20°) · kamera üst kat
          penceresinden kuzeye, bahçe boyunca bakar, tilt 32° aşağı, 24 mm, h +5,0 m · güneş HİÇBİR karede yok · şafak → sabah → öğle (ev
          gölgesi patio'da) → ikindi → altın akşam → mavi saat · fener S7·a'da (≈ 58,0) TEK KAREDE yanar, S7·b'de kapak bir karış aralığa iner
AİLE      DİKEY · çukur / kapak kadrajın ortasında (py 946–1409) · başlık alanı kapağın üstündeki arka çim (Ü bandı, py 560–770)
TAKVİM    sahneler arasında günler (KESMEDE · ≈ iki-üç hafta), sahne içinde 2 sa / 8 sn (alt klipte 1 sa / 4 sn · S7·b 4 sn) (beyanlı) ·
          mevsim taşıyıcısı: istifteki eski kesekler yeşilden sarıya
KURGUSAL  bahçe, ev, sokak KURGUSAL · tek adam kurgusal, yüzü hiçbir karede okunmaz · askerî/kıyamet sığınağı imgesi YOK
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 63.5 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.75)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① IŞIK ÇİZGİSİ + HAVUZ — çimin ortasında üstü çimli kapak neredeyse kapalı, YAKIN kenarı bir karış aralık (x 471–609 · py ≈ 1164);
    aralıktan ince sıcak turuncu çizgi, patio'ya doğru çimde yumuşak ılık havuz (py ≈ 1180–1312) · kadrajın EN PARLAK şeyi bu ikisi ·
    yukarı ışık sütunu / yelpaze / parlama YOK
  ② KAPAK + BORU — TEK kare kapak (≈ 132 × 85 px), yakın kenarında kısa ahşap takoz · uzak sağda TEK kısa gri boru (x ≈ 720 · py 908–1022)
  ③ BÜTÜN ÇİM — patio'dan arka çite kesintisiz; ortada bir karede ve onun ötesinde iki yamada soluk rulo derzleri, iki soluk tahta izi ·
    makine, palet, yığın, branda YOK · kimse görünmez
  ④ TANIKLAR — arka çit (dip x 181–899 · py 545) · kapı (x ≈ 985–1011) · elma ağacı (gövde x ≈ 165) · bungalov çatıları + derin mavi gök
    şeridi (py < 111) · patio + sandalye yerinde (x ≈ 218) · Ü bandı (py 560–770) KOYU, SAKİN çim

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–58,0'de (2x: 28,0–29,0) gök şeridi TEK YÖNDE altından derin maviye geçer; gök geri dönerse → S7·a atılır [DERS 98].
⛔ ≈ 58,0'de (2x: 29,0) açık ağız TEK KAREDE sıcak turuncuya döner ve yanık kalır. "Yavaşça" ısınır, titrer, söner, yeniden yanarsa →
   S7·a atılır [ISIK_FINALI §2 · DERS 98].
⛔ ≈ 60,5'te (2x: 30,25) adam kapağı üstüne çeker ve merdivenden iner; ≈ 61,5'te (2x: 30,75) kapak takoza oturur. Kapak TAM kapanır
   (aralık yok), ikinci kapak çıkar, adam kapağın üstünde kalır, yüzü kameraya döner ya da ikinci figür gelirse → S7·b atılır [DERS 96 · 89].
⛔ 61,5–64,0 (2x: 30,75–32,0) TUTUŞ: çim, çitler, boru, sandalye durur; yalnız aralıktaki ışık sabit parlar, elma yaprakları hafif kıpırdar.
   ÇİT ya da AĞAÇ kayarsa · çimden ışık sütunu çizilirse [STAR DOCK] → S7·b atılır [DERS 91 ③]. ⚠️ 2x'te tutuş 1,25 sn — C2-b 2 sn eşiğinin
   ALTINDA, beyanlı (plan TESLİM YAPISI).
⛔ Işık havuzu ya da parıltı G8'de Ü bandına (py 560–770) uzanırsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63] — kapağın inişi (≈ 130 px, x 471–609 · py 988 → 1164) BEKLENİR; tutuş ölçümü 61,5'ten
   başlar ya da bu alanı dışarıda bırakır.
⛔ Sahne bloğu S7·b tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık, erime
   ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta akşam bahçesi (cırcır, uzak köpek — dijital sessizlik DEĞİL) [DERS 100].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · 24 mm · h +5,0 m · tilt 32° aşağı · bearing 0°)

| ne | beklenen | tolerans |
|---|---|---|
| ⭐ arka çit | dip x 181–899 · py 545 · tepe x 163–917 · py 419 | KESİR 720 px ±10 · ON BİR KAREDE (nirengi ①) · 720 px değilse lens/yükseklik kaymıştır → G8 yeniden [DERS 99] |
| ⭐ kapı (sağ çit) | x ≈ 985–1011 · py ≈ 520–660 | ON BİR KAREDE AYNI (nirengi ①) · G0–G6 damperin giriş-çıkışı |
| ⭐ elma ağacı + bungalov çatıları | gövde x ≈ 165 · py 442–602 · tepe py 96–442 · mahya py ≈ 111 | ON BİR KAREDE AYNI (nirengi ②) · ⚠️ gövde Ü bandının sol kenarına 15 px |
| ⭐ patio | uzak kenar py 1613 · taş derzleri | ON BİR KAREDE AYNI (nirengi ③) |
| ⭐ çukur / kapak karesi | uzak kenar py 946 (x 260–820) · yakın kenar py 1409 (x 95–985) | G0 ipli kare · G1 diz boyu · G2–G5 açık çukur · G6 çıplak kare · G7→ çim |
| ⭐ taban şeridi | py 1299–1409 (z −3,1) | ⭐ G2'de BOŞ toprak · G3→ GRİ — görünmüyorsa DERS 95 tutmamış → pilot (c′) ❌ |
| ⭐ uzak iç duvar | 6 sıra üst kenarı py 1191 · 12 sıra py 1069 | G4 altı · G4a→ on iki · sıra ≈ 19 px |
| ⭐ havalandırma borusu | x 715–726 · py 908–1022 | G5'ten itibaren · TEK |
| ⭐ kapak | x 471–609 · py 1095–1180 | G5 kare boşluk · G6 kasa, kapak kapalı · G7–G7a DİK (üst kenar py 988) · G8 ARALIK |
| yığın | x 0–416 · dip py ≈ 894 · tepe G2 ≈ 470 / G3–G5 ≈ 640 / G6 ≈ 730 | G0 boş branda · G7→ YOK |
| depo | x 683–965 · py 730–865 | G0–G6 · G7→ YOK |
| ekskavatör | x 463–615 · py 570–919 (uzak kenarda) | G0 kapı içinde · G1–G6 uzak kenarda · G7→ YOK · TEK |
| ⭐ Ü bandı | py 560–770 · x 180–900 | G0–G6 iş alanı (serbest) · G7→ SAKİN çim · G8'de koyu, ışıksız |
| insan | ≈ 170–300 px | yüz yok, kameraya dönük kimse yok · işçi kanıt DEĞİL |

## 3. ⭐ ÇİMİN ALTININ İLERLEYİŞİ — kare kare, elle sayılır

```
G0   ⭐ bütün çimde ipli ≈ 4 m kare · yakın kenarında İLK kesik şerit · patio köşesinde alçak kesek istifi · ekskavatör + damper kapı içinde ·
     depo TAM · solda boş branda · sandalye katlı
G1   ⭐ çimsiz kare, DİZ BOYU kesik · brandada diz boyu yığın · kesek istifi bel boyu · ekskavatör uzak kenarda
G2   ⭐ ÇUKUR ≈ 3,5 m (adamın iki boyu), düz TABAN görünür · sağ yüzde merdiven, tepesi çimin ≈ 1 m üstünde · yığın bir buçuk adam boyu ·
     damper yarı dolu kapıda
G3   ⭐ nemli GRİ taban · yığın YARI (göğüs boyu) · hasır yok · çakıl torbası boş
G4   ⭐ dört blok duvar ALTI sıra · depoda 2 palet gri blok + 1 palet boşluklu + harç teknesi
G4a  ⭐ dört duvar ON İKİ sıra, üstü AÇIK · gri blok bitti · kiriş demeti TAM altı
G5   ⭐ KAPALI döşeme (kiriş + boşluklu blok) · kare kapak boşluğu, merdiven tepesi içinden · uzak sağda boru · çukurun yüzleri hâlâ açık
G6   ⭐ GÖMÜLDÜ — çimle aynı seviyede çıplak tırmıklı kare · çelik kasa, kapak KAPALI · boru · yığın DİZ BOYU · kesek paleti boş
G7   ⭐ BÜTÜN ÇİM · kapak DİK, ağız KARANLIK · sönük fener · makine, depo, yığın, tahta YOK · sandalye yerinde
G7a  ⭐ mavi saat · ağız YANIK · adam merdivende, başı ve omuzları ağızda, sırtı kameraya · kapak dik
G8   ⭐ mavi saat · kapak ARALIK, takozda · ince çizgi + havuz · kimse görünmez
⛔ SAYIM: oda 1 · adam (1·1·1·1·1·1·1·1·1·1·0 görünür) · ekskavatör (1×G0–G6 · 0) · damper (1×G0–G6 · 0) · mikser (1×G0–G6 · 0) ·
   merdiven 1 · kapak 1 · boru (0…0·1·1·1·1·1·1) · aynı anda hareketli makine HİÇBİR anda birden fazla değil [DERS 69]
⛔ Patio, çitler, kapı, elma ağacı, bungalovlar on bir karede DEĞİŞMEZ. Sandalye G6 → G7'de yerine döner (KASITLI).
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 46 · 48 · 57 · 93 · beş soru ②③]

```
S0   çim: kare → bıçak → kürek → patio paleti · toprak: kare → kepçe → branda (yığın) · ekskavatör: kapı içi → tahta yol → uzak kenar
S1   toprak: çukur → kepçe → yığın ya da damper → tahta yol → kapı (dışarı, TEK TEK sefer) · merdiven: depo → çukur (sağ yüz)
S2   çakıl: big-bag → kepçe → taban · hasır: depo → çukur · beton: mikser → kepçe → taban (uzak yüzden kameraya) · toprak: yığın → damper → kapı
S3   blok: kapı → damper → depo paleti → kepçe → taban → duvar (dördü birlikte) · harç: mikser → kepçe → tekne
S4·a blok: palet → kepçe → duvar (6 → 12 sıra)
S4·b kiriş: demet → zincir → kepçe → duvar üstü (TEK TEK) · boşluklu blok: palet → el → kirişler arası · boru: depo → döşeme · merdiven: çukur → oda
S5   beton: mikser → kepçe → döşeme · membran: rulo → döşeme → duvar dışları · kasa: depo → boşluk · toprak: yığın → kepçe → yan boşluklar +
     döşeme üstü · eski kesek: palet → dolgu (çim yüzü aşağı)
S6   yığın kalıntısı + boş torba + palet + mikser: bahçe → damper → kapı (dışarı) · rulo çim: kapı → damper → çıplak toprak · branda, tahta:
     dürülür, kalkar · ekskavatör: uzak kenar → kapı (dışarı) · çim tepsisi: → kapak · fener: → çim · sandalye: katlı → yerinde
S7·a fener: çim → adamın eli → aşağı (TEK KARE yanar)
S7·b kapak: dik → adamın elleri → takoz (bir karış aralık)
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı depo, palet, demet, big-bag, rulo ya da kapı (damper) [DERS 48 · 49 · 61].
⛔ Kiriş havada zincirsiz taşınmaz; aynı anda TEK kiriş [DERS 57].
⛔ Toprak SİLİNMEZ: kepçeyle yığına/çukura, damperle kapıdan dışarı [DERS 93].
⛔ Taban, duvar, döşeme çukurun DIŞINDA belirmez; eylem görünen yüzeylerde kalır [DERS 95].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI · HAVA_VE_ATMOSFER · DERS 98]

```
G0     05:00 (65,5°/+4,0°)   · ⭐ şafak · bahçe yumuşak mavi-gri gölgede · yalnız bungalov çatıları pembe-altın · gök şeridi solgun
G1     07:00 (85,6°/+24,4°)  · sabah · sağdan alçak ışık · sağ çitin uzun gölgesi çimde · elma gölgesi SOLA
G2     09:00 (108,9°/+45,4°) · ⭐ çukurun uzak + sol yüzü ışıkta, sağ yüzü gölgede
G3     11:00 (148,7°/+62,1°) · ⭐ ev gölgesi patio'da · gri taban ışıkta
G4     13:00 (211,3°/+62,1°) · ev gölgesi patio'da · gölgeler SAĞA döner
G4a    14:00 (234,6°/+54,8°) · gölgeler sağa
G5     15:00 (251,1°/+45,4°) · ikindi · döşeme ve çukurun sol yarısı ışıkta
G6     17:00 (274,4°/+24,4°) · ⭐ soldan ılık ışık çıplak toprakta · uzun gölgeler sağa
G7     19:00 (294,5°/+4,0°)  · ⭐ batış öncesi · yalnız çatı tepeleri altın · bahçe serin gölgede · fener SÖNÜK
G7a    20:00 (305,2°/−5,2°)  · ⭐ mavi saat · ağız YANIK
G8     20:00:04             · aynı · kapak aralık
⛔ Gölge TEK YÖNDE döner (sola uzun → kısa → sağa uzun); geri dönen kare = zaman ters → ❷ [DERS 98]
⛔ Güneş diski HİÇBİR karede yok (kadraj 337°–23°, üst kenar +4,9°; doğuş 61°, batış 299°) [DERS 39 · 70]
⛔ G0–G7 boyunca yapay ışık YOK · ilk ve tek yanış ≈ 58,0'de
⛔ Mavi saat zifiri değil: çim, çitler, ağaç, boru okunur [DERS 45]
⛔ Bungalov pencereleri G8'de karanlık cam — yanarsa en parlak şey kapak olmaz → kapak bandı zarar görmez ama ① sırası bozulur (beyanlı risk)
```

## 6. ⭐ BİR ODA · BİR ADAM · TEK HAREKETLİ MAKİNE · BİR KAPAK · YAZISIZ KAPISI [DERS 55 · 69 · 89 · 59 · 42]

```
Korpus riski: "hidden room under lawn" → çimde cam pencere / kubbe, ikinci kapak · "bunker" → çelik zırhlı kapı, kamuflaj, askerî beton
(ÇIKARIM — bu filmde ölçülmedi). bunker · shelter · vault · crew · workers · team · crane · hoist · fog · mist · haze · beam · ray · flare
promptta YOK.
① sayım cümlesi her karede POZİTİF ("one buried room, and the only thing being built in view") · S0–S6 I2V'de "One man works alone for the
  whole shot and is the only person in view: he drives one machine or carries one load at a time" · S7'de "He is the only person in view"
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç adam / kaç makine aynı anda hareketli / kaç kapak / gövdede yazı var mı
⛔ ikinci adam · ikinci ekskavatör/damper · aynı anda iki hareketli makine · ikinci kapak · çimde pencere/kubbe · zırhlı kapı → ⑧
⛔ Model çiti, kapıyı, ağacı ya da bungalovları yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Big-bag'de, çimento torbasında, makine gövdesinde okunur yazı, marka, numara → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn; alt klipte 1,0–2,0):
  S0 ekskavatör uzak kenara geçer, kazar · S1 taban düzlenir, merdiven iner · S2 beton kameraya doğru yayılır · S3 duvarlar 4–6 sıra ·
  S4·a duvarlar 10–12 sıra · S4·b boru + merdiven · S5 çukur toprakla dolar · S6 çim serilir, makineler çıkar, kapak dikilir ·
  S7·a ışık yanar, adam ağızda yükselir · S7·b kapak iner, tutuş (kasıtlı)
⛔ 2x'te ikinci yarı tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok (dizel EQ) · konuşma yok · nefes/homurtu yok · anlaşılır söz yok
· 0,0 şafak kuşları, çim bıçağı, ekskavatör marşı · 8–15 dizel, kepçe, damper paleti · 16–23 mikser dönüşü, beton dökülüşü, mala ·
  24–31 blok tıkırtısı, mala · 32–39 zincir, kirişin tok oturuşu, blok · 40–47 membran hışırtısı, kepçeden toprak, çelik kapak ·
  48–55 damper kapıdan, rulo çimin açılışı, tırmık · 56–58 kuşlar susar, cırcır · ⭐ 58,0 fenerin tık sesi (KARE SENKRON ±2 kare) ·
  60,5 menteşe · ⭐ 61,5 kapağın takoza tok oturuşu
· KART 64,0–69,0: cırcır + akşam bahçesi, son saniyede kısılır → döngüde S0'ın şafak kuşlarına bağlanır
```

## 9. Zaman ve ışık

```
G0 05:00 65,5°/+4,0° · G1 07:00 85,6°/+24,4° · G2 09:00 108,9°/+45,4° · G3 11:00 148,7°/+62,1° · G4 13:00 211,3°/+62,1° ·
G4a 14:00 234,6°/+54,8° · G5 15:00 251,1°/+45,4° · G6 17:00 274,4°/+24,4° · G7 19:00 294,5°/+4,0° · G7a 20:00 305,2°/−5,2° · G8 20:00:04
(45°K · δ +20° · güneş saati · TÜRETİLMİŞ model · doğuş 04:35 · batış 19:25 · sahneler arası günler KESMEDE)
· zaman çit/ağaç gölgeleri + ev gölgesi + gök şeridi + kesek rengiyle taşınır (şafak → öğle → altın → mavi saat); final mavi saat, ışık yanar,
  kapak iner
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası, beyanlı · alt klip dikişleri sahne İÇİ
① KADRAJ        24 mm · tilt 32° · h +5,0 m — yukarıdan bakış, gök yalnız dar şerit (≈ 110 px) · çukur kadraj genişliğinin %82'si · adam
                ≈ 170–300 px · blok sırası 19 px · aralık çizgisi ≈ 25 px · Ü bandı G0–G6'da iş alanı (yığın, depo) — beyanlı
⑤ DEVAMLILIK    çimin ortası (kare → çukur → taban → duvar → döşeme → toprak → çim → ışık) KASITLI değişir; yığın, depo, kesek paleti,
                makineler G0–G6, sandalye G6 → G7 KASITLI · çitler, kapı, ağaç, bungalovlar, patio DEĞİŞMEZ
❷ ZAMAN         sahneler arasında günler, saat tek yön (beyanlı) · 60,0'da rejim dikişi B → G · kesekler yeşilden sarıya (takvimin kanıtı)
⑦ İŞ            S7 inşaat işi yok — iş IŞIK ve KAPAKTIR (kasıtlı) · S7·b tutuşu 2x'te 1,25 sn (C2-b altında, beyanlı) [SANTIYE_HAREKETI §4.7]
❺ TESLİM        işlev anı ışık — LAST STOP · GAME ON · TOTAL RESET · POOL ROOM · UNDERWATER OBSERVATORY · COLOSSUS · THE TURNTABLE · LIT AGAIN ·
                THE READING CAR · THE OPENING NIGHT · THE MENDED SPAN'da da var (onikinci) · fark: ışık SAKLANIR (kapak iner)
⑫ GÜVENLİK      3,4 m dik kazı iksasız (ÇIKARIM: gerçekte iksa/şev gerekir) — okunurluk için beyanlı; mercek "güvensiz" derse BEKLENEN
⑬ KURGUSAL      adam ve bahçe kurgusal — "Altered content" beyanı yayında; gerçek kişi/olay iması çıkarsa başlık değişir (KAPAK)
```
