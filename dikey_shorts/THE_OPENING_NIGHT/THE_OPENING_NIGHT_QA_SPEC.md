# 🔍 THE OPENING NIGHT — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_OPENING_NIGHT_DIKEY_TIMELAPSE.md` · Günlük: `THE_OPENING_NIGHT_URETIM_GUNLUGU.md` · Kapak: `THE_OPENING_NIGHT_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE OPENING NIGHT · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 25.10.2026 · kural 7 × 8 · sahibin briefi "8 × 8 sn, 9 G") · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "OPENING NIGHT") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 1 ara kare (G6a; G7a = G8) + 10 klip (S6 · S7 ikişer 4 sn alt klip) · T2V yok ·
          ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye) · ⚠️ merceklere 8 SAHNE; alt klip dikişleri (52,0 · 60,0) sahne İÇİDİR, kesme
          sayılmaz
REJİM     S0–S6 + S7·a B (900× · 2 sa / 8 sn, alt klipte 1 sa / 4 sn) · S7·b G (gerçek zaman, 1×) — tek rejim dikişi 60,0'da
IŞIK      SAAT TEK YÖNDE · 05:00 → … → 19:00 → 20:00 → 20:00:04 (güneş saati) · 41° kuzey · Temmuz sonu (δ +20°) · kamera 0°'ye (kuzey, sahanın
          boyu boyunca) bakar, tilt 9° aşağı, 24 mm · güneş HİÇBİR karede yok · şafak → sabah → öğle → ikindi → altın akşam → gece ·
          projektörler S7·a'nın son karesinde (≈ 59,8) TEK KAREDE yanar, S7·b'de tek sıra kıvılcım bir kez geçer
AİLE      KÜTLE · ana yapı = uzak tribün + çatı kenarı + saha uzak yarısı (py 772–1360) · başlık alanı uzak çatının üstündeki açık gök (py 560–770)
TAKVİM    sahneler arasında haftalar (KESMEDE), sahne içinde 2 sa / 8 sn (alt klipte 1 sa / 4 sn · S7·b 4 sn) (beyanlı) · S6–S7 aynı akşam
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 63.5 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.75)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① YANAN PROJEKTÖRLER + IŞIKLI SAHA — çatı ön kenarı boyunca (py 810–828) parlak beyaz projektör sırası · saha parlak, eşit yeşil, açık/koyu
    biçme şeritleri ve beyaz çizgiler keskin · kadrajın EN PARLAK alanı saha · gökte ışık şeridi / yelpaze / sis bulutu YOK
  ② DOLU ÇANAK — kırmızı alt teras (py 968–1103) ve sarı üst teras (834–968) kalabalıkla örtülü, boş sıra yok · üst terasın önünde DÜZ kırmızı
    ve sarı pankartlar · ekran (x 260–436 · py 828–898) düz beyaz, YAZISIZ
  ③ DİZİLİ TAKIMLAR — orta çizgide (py ≈ 1348) yan yana iki takım (kırmızı · beyaz) + üç hakem · tünel körüğü ve iki yedek kulübesi yerinde ·
    uzak kale ağıyla
  ④ TANIKLAR — çatı arka kenarı py ≈ 772 + üç makas · merdiven kulesi (sol) · servis kapısı · tünel ağzı · iki vomitoryum · başlık bandı
    (py 560–770) DÜZ derin mavi gök, kıvılcım/duman YOK

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–57,5'te (2x: 28,0–28,75) son seyirciler basamaklardan boşluklara yürür; koltukta "belirirse" → S7·a atılır [DERS 61].
⛔ 57,0–58,5'te (2x: 28,5–29,25) takımlar tünel ağzından orta çizgiye SÜREKLİ bir izle gelir. Orta çizgide belirir (tünelden iz yoksa),
   üçüncü takım/kalabalık sahaya taşarsa → S7·a atılır [DERS 96].
⛔ 58,0–59,8'de gök TEK YÖNDE altından derin maviye geçer; geri dönerse → S7·a atılır [DERS 98].
⛔ ≈ 59,8'de (2x: 29,9) projektörler TEK KAREDE yanar ve yanık kalır. "Yavaşça" yanar, titrer, söner, yeniden yanarsa → S7·a atılır
   [ISIK_FINALI §2 · DERS 98].
⛔ 60,0–64,0 (2x: 30,0–32,0) TUTUŞ: çanak, çatı, saha, takımlar durur; yalnız kalabalık kıpırdar ve ≈ 61,0–62,5'te TEK SIRA kıvılcım
   çatının arka kenarından yükselip söner. ÇATI, EKRAN ya da TERASLAR kayarsa · kıvılcım duman bulutu bırakırsa · gökte huzme / ışık
   yelpazesi çizilirse [STAR DOCK] · takımlar dağılırsa → S7·b atılır [DERS 91 ③].
⛔ Projektör parıltısı ya da kıvılcım G8'de başlık bandını (py 560–770) aydınlatırsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63] — kıvılcım geçişi (gök bandı) ve kalabalık kıpırtısı BEKLENİR; tutuş ölçümü bu alanları
   dışarıda bırakır ya da eşiği bu beyanla okur.
⛔ Sahne bloğu S7·b tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık, erime
   ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta kalabalık uğultusu (dijital sessizlik DEĞİL) [DERS 100].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · 24 mm · h 40 m · tilt 9° aşağı)

| ne | beklenen | tolerans |
|---|---|---|
| ⭐ çatı arka kenarı + üç makas | py 772, düz · makaslar x ≈ 300 / 540 / 780 | ±0,5 puan · ON KAREDE (nirengi ①) · eğilirse kamera kaydı |
| ⭐ uzak kale çizgisi | py 1129 · x 228–852 (624 px) | KESİR ±10 px · ON KAREDE · 620 px değilse lens/mesafe kaymıştır → G8 yeniden [DERS 99] |
| ⭐ merdiven kulesi + servis kapısı | x ≈ 80–180 · py 740–1121 | ON KAREDE AYNI (nirengi ②) |
| ⭐ tünel ağzı + iki vomitoryum | x 514–566 · py 1077–1113 / x 372–420 · 660–708 · py 936–968 | ON KAREDE AYNI (nirengi ③) · seyirci YALNIZ vomitoryumdan |
| ⭐ ekran | x 260–436 · py 828–898 | G0–G3 boş ızgara · G4–G6 düz koyu · G6a→ düz beyaz · HER ZAMAN yazısız |
| ⭐ projektör sırası | çatı ön kenarı py 810–828 | G0–G2 yok (çıplak çelik) · G3–G7 gri, SÖNÜK · G7a = G8 YANIK |
| ⭐ alt teras (KIRMIZI) | py 968–1103 | G0–G1 gri · G2 soldan yarı · G3→ tam · G6a→ dolu |
| ⭐ üst teras (SARI) | py 834–968 | G0–G2 gri · G3 sol uç · G4 sol yarı · G5→ tam · G6a neredeyse boş · G7 neredeyse dolu · G8 dolu |
| ⭐ çim | saha (py 1129 → 1920) | G0 1 şerit · G1 py ≈ 1237'ye · G2 py ≈ 1436'ya · G3→ tam · G6→ biçme şeritleri |
| ⭐ vinç | x ≈ 405 · py ≈ 1121 · bom ucu py ≈ 722 | YALNIZ G2–G4 · TEK · kanca HER karede yüklü (ray · panel · pano) |
| kale | x 506–574 · py 1107–1129 | G4→ beyaz, ağlı · kadrajda TEK kale |
| insan | orta çizgide ≈ 24 px · uzak terasta ≈ 15 px | yüz yok, kameraya dönük kimse yok · kalabalık RENK DOKUSU |

## 3. ⭐ ÇANAĞIN İLERLEYİŞİ — kare kare, elle sayılır

```
G0   ⭐ iki teras çıplak gri beton basamak, TEK koltuk yok · saha kahverengi toprak + kum · uzak kale çizgisinde TEK şerit çim · çatı ön kenarı
     çıplak · ekran çerçevesi boş ızgara · kamyon (çim paletleri) servis kapısında · yükleyici ikinci şeritte · çim ekibi
G1   ⭐ çim uzak ceza sahasının hemen ötesine · ⭐ alt terasın ön sırasında üç kırmızı palet (takılı koltuk YOK) · teleskopik + yükleyici park
G2   ⭐ alt teras soldan yarı kırmızı (düz kenar) · çim orta yuvarlağı geçer · ⭐ vinç, kancada projektör rayı · iki iskele kulesi · iki makasçı
G3   ⭐ tam çim · tam kırmızı · ⭐ projektör sırası (sönük) · üst terasın sol ucunda ilk sarı · vinç, kancada ekran paneli · ekran çerçevesi boş
G4   ⭐ düz koyu ekran · ⭐ beyaz çizgiler + kale · sarı üst terasın sol yarısı · vinç, kancada pano demeti
G5   ⭐ tam sarı · ⭐ kesintisiz düz panolar · vinç YOK · kamyonda iki kulübe · iskele kuleleri hâlâ
G6   ⭐ biçme şeritleri · iki kulübe + beyaz tünel körüğü + dört köşe bayrağı · iskele YOK · her koltuk BOŞ · görevliler · araba son paletlerle
G6a  ⭐ alt teras DOLU · üst teras HÂLÂ neredeyse boş · ekran düz beyaz · araç YOK
G7   ⭐ çanak neredeyse dolu (sağ uçta sarı boşluklar) · ⭐ düz pankartlar · saha BOŞ · projektörler SÖNÜK · batış öncesi
G7a = G8  ⭐ tam dolu · gece · projektörler YANIK · takımlar orta çizgide
⛔ SAYIM: çanak 1 · çatı 1 · makas 3 · ekran 1 · kale (kadrajda) 1 · vomitoryum 2 · merdiven kulesi 1 · vinç (0·0·1·1·1·0·…) · kulübe
   (0·…·0·2·2·2·2·2) · hareketli araç HİÇBİR anda birden fazla değil [DERS 69]
⛔ Çanağın biçimi, iki teras, çatı, kule, kapı, tünel ve vomitoryumlar on karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0   çim rulosu: kamyondaki palet → yükleyici kolu → kum yatak (şerit şerit, uzaktan yakına) · koltuk paleti: kapı → teleskopik → alt terasın ön sırası
S1   koltuk: palet → el → beton sıra → cıvata (SOLDAN sağa, sıra sıra) · rulo: kamyon → yükleyici → saha · vinç: kapı → apron (ayaklar kalasta)
S2   projektör rayı: apron istifi → vinç kancası (iki sapan) → çatı ön kenarı → makasçı cıvatası · koltuk: palet → sıra · rulo: kamyon → saha ·
     çizgi arabası: kapı → çim (elle)
S3   ekran paneli: apron sandığı → vinç → çerçeve → makasçı (iskele kulesinden) · boya: araba → çim · kale: kapı → omuz → yuva · ağ: → kale ·
     sarı koltuk: palet → sıra
S4   pano demeti: kamyon → vinç → çim kenarı · pano: el → saha kenarı (kesintisiz) · sarı: palet → sıra · vinç: bom iner → kapı → dışarı
S5   kulübe: kamyon → teleskopik → tünelin iki yanı → cıvata · tünel körüğü: tünel → saha kenarı (bölüm bölüm) · iskele kulesi: tepeden → el →
     basamak → elektrikli araba → kapı · köşe bayrağı: el → köşe · biçme: itme makinesi → çim (şerit şerit)
S6·a son paletler: araba → kapı → dışarı · seyirci: vomitoryum → basamak → sıra (ağızlardan DIŞA) · ekran: → düz beyaz
S6·b seyirci: vomitoryum → basamak → üst teras (alt sıradan yukarı) · pankart: rulo → korkuluk
S7·a son seyirci: basamak → boşluk · takım: tünel → körük → orta çizgi · projektör: görünmeyen şalter → TEK KARE (son an)
S7·b kıvılcım: çatının arka kenarı → gök bandı → söner (bir kez)
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı palet, kamyon, istif, kanca, el ya da kapı [DERS 48 · 49 · 61].
⛔ Kimse koltukta belirmez: her seyirci vomitoryumdan yürür. Kimse sahaya taşmaz.
⛔ Renk bir anda "boyanmaz": koltuk cephesi sıra sıra, düz kenarla ilerler (paketin Risk 1'i).
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI · HAVA_VE_ATMOSFER · DERS 98]

```
G0     05:00 (65,3°/+2,3°)   · ⭐ şafak · sağdan alçak ışık sol tribünün yüzünde · sağ tribünün uzun gölgesi sahayı SOLA doğru örter
G1     07:00 (83,8°/+24,1°)  · açık sabah · sol yarı ışıkta · sağ gölge kısalır
G2     09:00 (105,0°/+46,5°) · ⭐ uzak tribün sağdan ışıkta · kısa gölgeler sola · küçük bulutlar
G3     11:00 (144,2°/+65,4°) · ⭐ öğle, güneş arkada-sağda · uzak tribün tam ışıkta · çok kısa gölge
G4     13:00 (215,8°/+65,4°) · öğle · kısa gölgeler SAĞA döner
G5     15:00 (255,0°/+46,5°) · ikindi · sol tribünün gölgesi sahanın sol kenarında
G6     17:00 (276,2°/+24,1°) · ⭐ akşam · gölge sahanın sol yarısında · sağ tribün sıcak
G6a    18:00 (285,4°/+13,0°) · alçak altın · gölge sahayı neredeyse örter
G7     19:00 (294,7°/+2,3°)  · ⭐ batış öncesi · yalnız sağ tribünün üstü ve çatının sağ ucu altın · projektörler SÖNÜK
G7a=G8 20:00 (304,8°/−7,5°)  · ⭐ gece mavisi · güneş gölgesi YOK · projektörler YANIK · çatı göğe karşı koyu · her şey OKUNUR
⛔ Gölge TEK YÖNDE döner (sola → kısa → sağa → sahanın sol yarısı → bütün saha); geri dönen kare = zaman ters → ❷ [DERS 98]
⛔ Güneş diski HİÇBİR karede yok (kamera kuzeye; yatay görüş 337°–23°, üst kenar +27,9°) [DERS 39]
⛔ G0–G7 boyunca projektörler SÖNÜK (gündüz denemesi YOK — plan TASARIM ④) · ilk ve tek yanış ≈ 59,8'de
⛔ Gece zifiri değil: kalabalık, pankartlar, çatı ve ekran okunur [DERS 45]
```

## 6. ⭐ BİR ÇANAK · BİR EKRAN · BİR VİNÇ · TEK HAREKETLİ ARAÇ · YAZISIZ KAPISI [DERS 55 · 69 · 89 · 59]

```
Korpus riski: "stadium" → ikinci stadyum, kent siluetinde gökdelen, reklam yazısı, kulüp arması, sponsor logosu · "opening night" → havai fişek
bulutu, lazer, sis (ÇIKARIM — bu filmde ölçülmedi). beam · ray · flare · searchlight · spotlight · haze · fog · mist · smoke · fireworks promptta
YOK.
① sayım cümlesi her karede POZİTİF ("one stadium bowl, and the only stadium in view") · S0–S5 I2V'de "Only one turf crew on the pitch and one
  seat crew on the terraces" · her I2V'de "Exactly one vehicle moves at a time" (S6·b–S7 araçsız) · S6–S7'de "nobody appears in a seat
  without walking to it" · S7'de "The players come only out of the tunnel mouth"
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç araç aynı anda / kaç vinç / kaç ekran / panoda ya da pankartta yazı var mı
⛔ ikinci stadyum · ikinci ekran · ikinci vinç · koltukta beliren seyirci · sahaya taşan kalabalık · aynı anda iki hareketli araç → ⑧
⛔ Model çatıyı, kuleyi, tünelin ya da vomitoryumların yerini yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Panoda, ekranda, pankartta, formada, araçta okunur yazı, arma, logo, numara → ❶ metin [negatif çekirdek "on any surface" + "No logos, crests
   or club emblems anywhere"] · gerçek kulübe işaret eden arma → teslim değil (paketin kuralı)
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn; alt klipte 1,0–2,0):
  S0 teleskopik kırmızı paletleri terasa koyar · S1 vinç girer, kancada ray · S2 çim kadrajın altına varır, kancada panel · S3 kale dikilir, sarı
  yarıya · S4 vinç çıkar · S5 biçme şeritleri · S6·a ekran beyaz · S6·b pankartlar · S7·a projektörler yanar · S7·b tutuş (kasıtlı — kıvılcım
  bir kez, kalabalık kıpırtısı)
⛔ 2x'te ikinci yarı tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı, TEZAHÜRAT ŞARKISI, MARŞ → teslim değil · ⭐ her klibin Veo sesi ayrıca
  dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · anons yok · anlaşılır söz yok · S0–S5 boş çanakta rüzgâr + yankı · S6'dan sonra SÖZSÜZ
  kalabalık uğultusu
· 0,0 kuşlar + yükleyici · 6,5 teleskopik bip · 8–15 akülü vidalama (yankılı), koltuk tıkı · 14 vinç motoru · 16–23 vinç uğultusu, rayın
  oturuşu · 24–31 panel, çizgi arabası tekerleği, kale yuvası · 32–39 pano tak sesleri, 37 vincin uzaklaşan motoru · 40–47 kulübe, iskele
  borusu, biçme makinesi · 48,5 kapılar · 48–55 ayak sesleri + yükselen uğultu, 55 pankart kumaşı · 56–59,8 uğultu, takımlar çıkınca sözsüz
  alkış · ⭐ 59,8 projektör rölesi + tek büyük sözsüz "ooh" (KARE SENKRON ±2 kare) · 61,0–62,5 uzak, yumuşak kıvılcım çıtırtısı · 62,5–64 alkış
· KART 64,0–69,0: kalabalık uğultusu sürer, son saniyede kısılır → döngüde S0'ın kuşlarına ve rüzgârına bağlanır
```

## 9. Zaman ve ışık

```
G0 05:00 65,3°/+2,3° · G1 07:00 83,8°/+24,1° · G2 09:00 105,0°/+46,5° · G3 11:00 144,2°/+65,4° · G4 13:00 215,8°/+65,4° ·
G5 15:00 255,0°/+46,5° · G6 17:00 276,2°/+24,1° · G6a 18:00 285,4°/+13,0° · G7 19:00 294,7°/+2,3° · G7a = G8 20:00 304,8°/−7,5°
(41°K · δ +20° · güneş saati · TÜRETİLMİŞ model · doğuş 04:41 · görünür batış 19:19 · sahneler arası haftalar KESMEDE)
· zaman tribün gölgeleri + gök ile taşınır (şafak → öğle → altın → gece); final gece, projektörler yanar, kıvılcım bir kez
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief "8 × 8 sn"), beyanlı · alt klip dikişleri sahne İÇİ
① KADRAJ        24 mm · tilt 9° · h 40 m — yan tribünler yalnız kenarlarda kama · yakın kale kadraj DIŞI (kadrajda tek kale) · insan 15–25 px ·
                kale 67 × 22 px · üst %40 açık gök (başlık zemini) — beyanlı
⑤ DEVAMLILIK    terasların rengi (gri → kırmızı/sarı → kalabalık), saha yüzü (toprak → çim → çizgi → şerit), çatı kenarı (çıplak → projektör), ekran
                (boş → koyu → beyaz) KASITLI değişir; çanak, çatı, kule, kapı, tünel, vomitoryumlar DEĞİŞMEZ · vinç G2–G4, iskele kuleleri G2–G5,
                kamyon G0–G5 KASITLI
❷ ZAMAN         sahneler arasında haftalar, saat tek yön (beyanlı) · 60,0'da rejim dikişi B → G — kalabalık izden kıpırtıya döner (beyanlı)
⑦ İŞ            S6–S7 inşaat işi yok — iş SEYİRCİNİN dolmasıdır (kasıtlı) · S7·b (60–64) kasıtlı TUTUŞ [SANTIYE_HAREKETI §4.7]
❺ TESLİM        işlev anı ışık — LAST STOP · GAME ON · TOTAL RESET · POOL ROOM · UNDERWATER OBSERVATORY · COLOSSUS · THE TURNTABLE · LIT AGAIN'de de
                var (dokuzuncu) · ⚠️ COLOSSUS ile içerik akrabası (beton çanak → stadyum, çim, ışık) — fark kalabalık; THE LAST LIFT · GAME ON ile
                de akraba — beyanlı (plan TASARIM ⑫)
⑫ KIVILCIM      ≈ 61,0–62,5'te gök bandında tek sıra parlak kıvılcım — KASITLI; duman/bulut bırakırsa ⑧
```
