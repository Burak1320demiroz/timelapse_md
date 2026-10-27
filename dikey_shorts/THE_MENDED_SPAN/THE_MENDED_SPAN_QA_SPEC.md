# 🔍 THE MENDED SPAN — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_MENDED_SPAN_DIKEY_TIMELAPSE.md` · Günlük: `THE_MENDED_SPAN_URETIM_GUNLUGU.md` · Kapak: `THE_MENDED_SPAN_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE MENDED SPAN · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 26.10.2026 · kural 7 × 8 · sahibin seçimi "8 sahne (sahip istisnası)") · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "THE MENDED SPAN") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 2 ara kare (G5a · G7a) + 10 klip (S5 · S7 ikişer 4 sn alt klip) · T2V yok ·
          ⭐ üretim sırası G8 (metinden) → G7a (G8'den araba silinir) → G7 … G0 (geriye) · ⚠️ merceklere 8 SAHNE; alt klip dikişleri
          (44,0 · 60,0) sahne İÇİDİR, kesme sayılmaz
REJİM     S0–S6 + S7·a B (900× · 2 sa / 8 sn, alt klipte 1 sa / 4 sn) · S7·b G (gerçek zaman, 1×) — tek rejim dikişi 60,0'da
IŞIK      SAAT TEK YÖNDE · 05:00 → … → 19:00 → 20:00 → 20:00:04 (güneş saati) · 41° kuzey · Temmuz sonu (δ +20°) · kamera 327°'ye (boğazın
          karşısına) bakar, tilt 24° aşağı, 24 mm, h +120 m · güneş HİÇBİR karede yok · şafak → sabah → öğle → ikindi → altın akşam → gece ·
          tabliye lambaları S7·a'nın son karesinde (≈ 59,8) TEK KAREDE yanar, S7·b'de ilk araba portaldan çıkar
AİLE      DİKEY · yakın kule sol kenarda (py 455–869), açıklık köşegen (tabliye py 706 → 534) · başlık alanı köprünün önündeki sakin su
          (A bandı, py 1060–1240)
TAKVİM    sahneler arasında haftalar/aylar (KESMEDE), sahne içinde 2 sa / 8 sn (alt klipte 1 sa / 4 sn · S7·b 4 sn) (beyanlı) · S6 sonu–S7
          aynı akşam
KURGUSAL  köprü, kule biçimi, kıyı KURGUSAL · gerçek köprü/boğaz adı hiçbir yerde yok · karşı kıyıda kent silueti, tanınır yapı YOK ·
          enkazda araç, insan, acil durum ekibi YOK
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 63.5 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.75)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① YANAN LAMBALAR + KESİNTİSİZ TABLİYE — tabliyenin iki kenarında sıcak beyaz iki lamba sırası, yakın kuleden (py ≈ 706) karşı kuleye
    (py ≈ 534) kesintisiz · siyah asfalt · kadrajın EN PARLAK şeyi lambalı tabliye · gökte ışık şeridi / yelpaze / sis YOK
  ② İLK ARABA — TEK araba, iki far, yakın kulenin portalının sağında (x ≈ 298 · py ≈ 664), tabliyenin ÜSTÜNDE · ikinci araç YOK
  ③ ASMA KÖPRÜ — iki ana kablo kule tepesinden kule tepesine, askılar düz bir sırada, tabliye askılardan DÜZ asılı · yürüme yolu, portal,
    mavna, römorkör YOK
  ④ TANIKLAR — yakın kule + üç çapraz bağ (x 64–189 · py 455–869) · karşı kule (x 830–878) · kayalık burun · yakın kıyı · yamacın dibi
    (py ≈ 1510) · karşı tepeler · A bandı (py 1060–1240) KOYU, SAKİN su, ışık ve tekne YOK

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–59,5'te (2x: 28,0–29,75) gök TEK YÖNDE altından derin maviye geçer, karşı kıyıda pencereler tek tek yanar; gök geri dönerse →
   S7·a atılır [DERS 98].
⛔ ≈ 59,8'de (2x: 29,9) lambalar TEK KAREDE yanar ve yanık kalır. "Yavaşça" yanar, titrer, söner, yeniden yanarsa → S7·a atılır
   [ISIK_FINALI §2 · DERS 98].
⛔ ≈ 60,5'te (2x: 30,25) arabanın farları yakın kulenin PORTALINDA belirir; araba tabliyenin ortasında belirirse, ikiye çıkarsa, geri
   giderse, durup kalkarsa → S7·b atılır [DERS 96].
⛔ 60,0–64,0 (2x: 30,0–32,0) TUTUŞ: kuleler, kablolar, tabliye, lambalar durur; yalnız araba tek düz çizgide ≈ 55 m (≈ 130 px) ilerler ve
   su küçük dalgacıklarla kıpırdar. KULELER ya da TABLİYE kayarsa · ikinci araba gelirse · tekne geçerse · gökte huzme / ışık yelpazesi
   çizilirse [STAR DOCK] → S7·b atılır [DERS 91 ③].
⛔ Lamba yansıması ya da far G8'de A bandına (py 1060–1240) uzanırsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63] — arabanın yolu (x 132 → 298 · py 696 → 664) ve su kıpırtısı BEKLENİR; tutuş ölçümü bu
   alanları dışarıda bırakır ya da eşiği bu beyanla okur.
⛔ Sahne bloğu S7·b tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık, erime
   ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta gece suyu + uzaklaşan araba (dijital sessizlik DEĞİL) [DERS 100].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · 24 mm · h +120 m · tilt 24° aşağı · bearing 327°)

| ne | beklenen | tolerans |
|---|---|---|
| ⭐ yakın kule + üç çapraz bağ | x 64–189 · tepe py 455 · dip py 869 · bağlar py 480 / 587 / 732 | KESİR 410 px ±10 · ON BİR KAREDE (nirengi ①) · 410 px değilse lens/mesafe kaymıştır → G8 yeniden [DERS 99] |
| ⭐ karşı kule + karşı tepelerin sırtı | x 830–878 · py 419–614 · sırt py 345–360 | ON BİR KAREDE AYNI (nirengi ②) · ⚠️ tepesi 1:1 kırpma çizgisinde |
| ⭐ kayalık burun + yakın kıyı + yamacın dibi | burun py 851–869 · kıyı sol kenarda py 877–1231 · yamaç dibi py ≈ 1510 (kenarlarda 1568) | ON BİR KAREDE AYNI (nirengi ③) |
| ⭐ portal / yan açıklığın ucu | x 98–169 · py 693–706 | G0–G1 yırtık kenar · G2–G5a kare kesik · G6→ yeni tabliyeye bağlı · G8 arabanın çıktığı yer |
| ⭐ tabliye çizgisi | yakın kule py 706 → orta 600 → karşı kule 534 | G0–G4 yok · G5 ortada 1 segment · G5a orta yarı · G6→ kesintisiz · G7→ siyah |
| ⭐ ana kablolar | kule tepelerinden, en alçak nokta py ≈ 577 | G0–G1 kopuk, suya sarkar · G2–G3 yok · G4→ iki kablo · ⚠️ 2–3 px |
| ⭐ yürüme yolları | kablo çizgisiyle aynı kavis | YALNIZ G3–G6 · TAM iki |
| ⭐ kaldırma portalları | G4 yakın kule tepesi · G5 orta (py ≈ 545) · G5a tabliyenin iki ucu · G6 yakın kulenin yanı | YALNIZ G4–G6 · TAM iki |
| ⭐ yüzer vinç | ponton x 395–550 · py 782–808 · bom ucu py ≈ 579 | YALNIZ G0–G1 · TEK · kanca HER karede yüklü (G0 kırık parça · G1 kaldırma çerçevesi) |
| ⭐ A bandı | py 1060–1240 · x 240–840 | HİÇBİR karede tekne yok · G8'de koyu, sakin, ışıksız |
| ilk araba (G8) | x ≈ 298 · py ≈ 664 · ≈ 16 px | TEK · farlar yanık · tabliyenin üstünde |
| insan | ≈ 6 px | yüz yok, kameraya dönük kimse yok · işçi kanıt DEĞİL |

## 3. ⭐ AÇIKLIĞIN İLERLEYİŞİ — kare kare, elle sayılır

```
G0   ⭐ iki kule ayakta, aralarında tabliye YOK · kopuk eski kablolar her kule tepesinden suya sarkar · suda 3 kırık parça (en uzunu yakın
     kulenin dibinde, KANCADA, sudan kalkmış) · yan açıklık yakın kulede yırtık kenar · vinç + BOŞ mavna + römorkör · enkazda araç/insan YOK
G1   ⭐ en uzun parça mavnada, zincirli · römorkör mavnayı vincin sağında tutar · vinç kancasında kaldırma çerçevesi · 2 parça suda · kablolar sarkar
G2   ⭐ BOŞ SU — enkaz, kablo ucu, tekne YOK · kule tepelerinde boş eyerler + küçük vinç + rulo ağ · yan açıklık kare kesik
G3   ⭐ iki gri yürüme yolu kuleden kuleye (ortada en alçak) · yakın kule tepesinde eğirme teri · römorkör kulenin dibinde bağlı
G4   ⭐ iki koyu ana kablo yürüme yolları boyunca, kelepçeli · iki sarı portal yakın kule tepesinde · askı mavnası ortanın altında
G5   ⭐ askılar bütün açıklıkta, alt uçları düz · ⭐ ortada İLK segment portalların sapanlarında asılı (korkuluk + direk takılı) · altında 2
     segmentli mavna + römorkör
G5a  ⭐ tabliyenin ORTA YARISI (çeyrekten çeyreğe) · kulelere doğru askılar SERBEST · portallar iki uçta · mavna yakın uçta
G6   ⭐ KESİNTİSİZ çıplak gri tabliye, iki kulede yan açıklıklara bağlı · direkler SÖNÜK · portallar yakın kulenin yanında · yürüme yolları
     duruyor · boş mavna + römorkör kulenin dibinde
G7   ⭐ SİYAH ASFALT · yürüme yolu, portal, mavna, römorkör YOK · tabliye BOŞ · lambalar SÖNÜK · batış öncesi altın
G7a  ⭐ gece · lambalar YANIK · tabliye BOŞ (G8 − araba)
G8   ⭐ gece · lambalar YANIK · TEK araba portalın sağında
⛔ SAYIM: köprü 1 · kule 2 · ana kablo (0·0·0·0·2·2·2·2·2·2·2) · yürüme yolu (0·0·0·2·2·2·2·2·0·0·0) · portal (0·0·0·0·2·2·2·2·0·0·0) ·
   yüzer vinç (1·1·0·…) · römorkör ≤ 1 · mavna ≤ 2 · araba (0·…·0·1) · hareketli tekne/araç HİÇBİR anda birden fazla değil [DERS 69]
⛔ İki kule, çapraz bağlar, kayalık burun, kıyılar ve tepeler on bir karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 46 · 48 · 57 · beş soru ②③]

```
S0   kırık parça: su → kanca (dört sapan) → mavna güvertesi → zincir · askı: kopuk kablo → ekip → mavna · mavna: römorkör → vincin sağı
S1   mavna: römorkör → sağ kenar · iki parça: su → kanca → ponton güvertesi · kopuk kablo: eyer (kesilir) → su → vinç → ponton (sarılır) ·
     vinç: kendi gücüyle → sağ kenar
S2   kılavuz halat: römorkör → yakın kule dibi → karşı kule dibi → kule tepesi vinci · yürüme yolu halatı: kule tepesi → kule tepesi ·
     ağ döşeme: kule tepesindeki rulo → halat → orta (iki uçtan) · eğirme teri: kule tepesi → ray
S3   tel: kule tepesi → eğirme teri → yürüme yolu (gidip gelir) · kablo: sıkıştırma + kelepçe · portal parçası: römorkör → kule tepesi vinci →
     kablo · askı mavnası: sağ kenar → römorkör → orta
S4   askı: mavna → yürüme yolu vinci → kelepçe (ORTADAN iki kuleye) · portal: kule tepesi → kablo boyunca → orta · segment mavnası: sağ kenar →
     römorkör → portalın altı · segment: mavna → dört halat → portal → askıların hemen altı (DÜŞEY)
S5·a segment: mavna → halat → portal → askı → komşu segment (ortadan dışa, her uçta aynı anda TEK) · mavna: sağ kenar → römorkör → portalın altı
S5·b son segment: mavna → portal → kulenin yanındaki boşluk → yan açıklık (KAPANIŞ) · portal: → yakın kule · boş mavna: → kulenin dibi
S6   portal: kablo → kendi halatları → mavna → römorkör → sağ kenar · yürüme yolu: kablo → tabliye (bölüm bölüm) → kamyon → portal → sol kenar ·
     asfalt: serici (portaldan girer, karşı kuleye gider) → tabliye (karşıdan yakına) → serici portaldan çıkar
S7·a lamba: görünmeyen şalter → TEK KARE (son an) · pencere: karşı kıyıda tek tek
S7·b araba: yan açıklık (kadraj dışı) → portal → açıklık (≈ 55 m)
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı mavna, ponton, römorkör, kule tepesi rulosu ya da kamyon [DERS 48 · 49 · 61].
⛔ Hiçbir yük yatay TAŞINMAZ: segment yalnız düşey kalkar; kırık parça yalnız kanca altında kısa salınır [DERS 57].
⛔ Tabliye havada yüzmez: her karede askılardan asılı ya da portalın sapanlarında [YAPI_TIPI_KARTLARI §3].
⛔ Enkaz suda SİLİNMEZ: kancayla kalkar [DERS 93].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI · HAVA_VE_ATMOSFER · DERS 98]

```
G0     05:00 (65,3°/+2,3°)   · ⭐ şafak · sağ arkadan alçak altın ışık kulelerin SAĞ yüzünde · kule gölgeleri suda SOLA uzun · su gri-mavi
G1     07:00 (83,8°/+24,1°)  · açık sabah · gölgeler kısalır
G2     09:00 (105,0°/+46,5°) · ⭐ kuleler eşit ışıkta · küçük bulutlar
G3     11:00 (144,2°/+65,4°) · ⭐ öğle, güneş kameranın arkasında · gölgeler kısa, kuleden uzağa
G4     13:00 (215,8°/+65,4°) · öğle · gölgeler SAĞA döner
G5     15:00 (255,0°/+46,5°) · ikindi · güneş solda, kulelerin SOL yüzü ışıkta
G5a    16:00 (266,5°/+35,4°) · geç ikindi · tabliyenin gölgesi suda sağa
G6     17:00 (276,2°/+24,1°) · ⭐ akşam · sıcak altın, uzun gölgeler sağa
G7     19:00 (294,7°/+2,3°)  · ⭐ batış öncesi · son altın kulelerin sol yüzünde · su sıcak gölgede, solda soluk altın · lambalar SÖNÜK
G7a    20:00 (304,8°/−7,5°)  · ⭐ gece mavisi · lambalar YANIK · tabliye boş
G8     20:00:04             · aynı + ilk araba
⛔ Gölge TEK YÖNDE döner (sola → kısa/uzağa → sağa → uzun sağa); geri dönen kare = zaman ters → ❷ [DERS 98]
⛔ Güneş diski HİÇBİR karede yok (kadraj 304°–350°, üst kenar +12,9°; batış ≈ 297°) [DERS 39 · 70] · G7'de suyun SOL ucu parlak — beyanlı
⛔ G0–G7 boyunca lambalar SÖNÜK · ilk ve tek yanış ≈ 59,8'de
⛔ Gece zifiri değil: kuleler, kablolar, tabliye, kıyılar okunur [DERS 45]
⛔ Su: B rejiminde DÜZ, CAMSI (ipek su — gerçek timelapse pratiği) · S7·b'de (G) küçük doğal dalgacık [SU_VE_YANSIMA §5]
```

## 6. ⭐ BİR KÖPRÜ · BİR VİNÇ · TEK HAREKETLİ TEKNE/ARAÇ · TEK ARABA · YAZISIZ KAPISI [DERS 55 · 69 · 89 · 59 · 42]

```
Korpus riski: "suspension bridge" + "strait" → ikinci köprü, karşı kıyıda kent silueti · "broken bridge" → duman, yangın, suda araç, acil durum
teknesi (ÇIKARIM — bu filmde ölçülmedi). beam · ray · flare · haze · fog · mist · smoke · fire · collapse · wreck · disaster · traffic · trail
promptta YOK.
① sayım cümlesi her karede POZİTİF ("one bridge, and the only bridge in view") · S0–S6 I2V'de "Only the small crews in orange vests on the
  vessels, the tower tops and the walkways" + "Exactly one vessel or vehicle moves at a time" · S7'de "This is the first and only car on the
  bridge; nothing else moves on the deck, and no vessel moves on the water"
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç köprü / kaç tekne aynı anda hareketli / kaç araba / gövdede yazı var mı
⛔ ikinci köprü · ikinci vinç · aynı anda iki hareketli tekne · ikinci araba · enkazda araç ya da insan · duman/alev → ⑧
⛔ Model kuleyi, çapraz bağları, burnu ya da tepeleri yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Tekne gövdesinde, mavnada, kamyonda okunur yazı, ad, numara → ❶ metin [negatif çekirdek "on any surface"]
⛔ Karşı kıyıda gerçek bir kenti/köprüyü çağıran siluet (minare, kule, ikinci köprü) → teslim değil (kurgusallık kuralı)
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn; alt klipte 1,0–2,0):
  S0 römorkör yüklü mavnayı sağa çeker · S1 vinç sağdan çıkar, su boşalır · S2 yürüme yolları ortada buluşur, eğirme teri · S3 portallar kule
  tepesinde, askı mavnası ortada · S4 ilk segment düşey kalkar · S5·a römorkör sıradaki mavnayı tutar · S5·b portallar kuleye döner ·
  S6 asfalt karşıdan yakına · S7·a lambalar yanar · S7·b tutuş (kasıtlı — ilk araba, su kıpırtısı)
⛔ 2x'te ikinci yarı tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · anons yok · anlaşılır söz yok · ⛔ vapur düdüğü yok · S0–S5 su + martı + rüzgâr
· 0,0 martılar + vinç hidroliği, damlama, zincir · 8–15 römorkör motoru (uzaklaşan), uzak kesici, kablo sarılması · 16–23 halat vinçleri, ağ
  hışırtısı · 24–31 eğirme terinin ritmik makarası · 32–39 askıların tok çınlaması, 38 halat germesi · 40–47 segment oturuşu ×çok, kısa kaynak
  cızırtısı, ⭐ 47,0 kapanış: tek büyük metal tok · 48–55 römorkör, kamyon, serici uğultusu · 56–59,8 su + rüzgâr · ⭐ 59,8 lambaların tek
  röle tıkı (KARE SENKRON ±2 kare) · 60,5 portalda araba motoru, asfaltta yumuşak teker uğultusu (uzak)
· KART 64,0–69,0: gece suyu + uzaklaşan araba, son saniyede kısılır → döngüde S0'ın martılarına bağlanır
```

## 9. Zaman ve ışık

```
G0 05:00 65,3°/+2,3° · G1 07:00 83,8°/+24,1° · G2 09:00 105,0°/+46,5° · G3 11:00 144,2°/+65,4° · G4 13:00 215,8°/+65,4° ·
G5 15:00 255,0°/+46,5° · G5a 16:00 266,5°/+35,4° · G6 17:00 276,2°/+24,1° · G7 19:00 294,7°/+2,3° · G7a 20:00 304,8°/−7,5° · G8 20:00:04
(41°K · δ +20° · güneş saati · TÜRETİLMİŞ model · doğuş 04:41 · görünür batış 19:19 · sahneler arası haftalar/aylar KESMEDE)
· zaman kule gölgeleri + gök + suyun rengiyle taşınır (şafak → öğle → altın → gece); final gece, lambalar yanar, ilk araba
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası, beyanlı · alt klip dikişleri sahne İÇİ
① KADRAJ        24 mm · tilt 24° · h +120 m — yakın kule sol kenarda (çekirdeğin sol kenarını taşar) · alt %21 kameranın altındaki yamaç ·
                insan ≈ 6 px · kablo 2–3 px · askı alt-piksel · karşı kulenin tepesi 1:1 kırpma çizgisinde — beyanlı
⑤ DEVAMLILIK    açıklığın içi (enkaz → boş su → yürüme yolu → kablo → askı → tabliye → asfalt → ışık) KASITLI değişir; kuleler, burun, kıyılar,
                tepeler DEĞİŞMEZ · vinç G0–G1, portallar G4–G6, yürüme yolları G3–G6, mavna/römorkör G0–G6 KASITLI
❷ ZAMAN         sahneler arasında haftalar/aylar, saat tek yön (beyanlı) · 60,0'da rejim dikişi B → G — su "cam"dan "dalgacık"a döner (beyanlı)
⑦ İŞ            S7 inşaat işi yok — iş IŞIK ve İLK ARABADIR (kasıtlı) · S7·b (60–64) kasıtlı TUTUŞ [SANTIYE_HAREKETI §4.7] · işçi ≈ 6 px —
                iş tekneler, portallar ve segmentlerle okunur
❺ TESLİM        işlev anı ışık — LAST STOP · GAME ON · TOTAL RESET · POOL ROOM · UNDERWATER OBSERVATORY · COLOSSUS · THE TURNTABLE · LIT AGAIN ·
                THE READING CAR · THE OPENING NIGHT'ta da var (onbirinci) · asıl ödül ilk araba · ⚠️ THE CROSSING ile içerik akrabası (deniz,
                köprü, kapanış) — fark asma köprü + enkazdan başlangıç (plan TASARIM ⑫)
⑫ KAYNAK        S5'te kısa kaynak kıvılcımı — KASITLI; duman/alev bırakırsa ⑧
⑬ KURGUSAL      köprü kurgusal — gerçek köprüye benzerlik ölçülmedi; tanınır siluet çıkarsa teslim değil (§6)
```
