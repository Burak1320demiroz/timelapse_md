# 🔍 THE SKY VAULT — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_SKY_VAULT_DIKEY_TIMELAPSE.md` · Günlük: `THE_SKY_VAULT_URETIM_GUNLUGU.md` · Kapak: `THE_SKY_VAULT_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE SKY VAULT · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 20.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "THE SKY / VAULT") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 ⭐ A (10 dk) — iki rejim
IŞIK      TEK GÜN, AÇIK GÖK: 05:45 → 07:45 → 09:45 → 11:45 → 13:45 → 15:45 → 17:45 → 19:45 → 19:55 (güneş saati) ·
          41° kuzey · 21 Haziran (δ +23,4°) · güneş 69,6°/+12,5° → 306,2°/−4,1° · kamera 10°'ye bakar, tilt 0 · güneş HİÇBİR
          karede kadrajda değil · final MAVİ SAAT: film soyulur, ışık S4'ten beri yanık
AİLE      ⭐ KÜTLE (göz hizası, ufuk %50) · depo %29,4–58,3 × x 299–796 · başlık alanı deponun ÜSTÜNDEKİ açık gök
TAKVİM    yok — tek gün (dönüşüm sıkıştırıldı, beyanlı); zaman taşıyıcısı deponun gölgesi (sol → arka → sağ) + gök rengi
          (sabah mavisi → öğle beyazı → akşam altını → mavi alacakaranlık)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① ÜÇ TEMİZ CAM + İÇ IŞIK — orta dikmenin solundaki geniş yüz (x 309–498), sağındaki geniş yüz (x 498–727) ve sağ dar yüz
    (x 727–796) birer TEMİZ cam (film YOK); arkalarında SICAK AMBER ışıkta iki krem berjer (x 391–464 · 565–641), aralarında
    yuvarlak traverten sehpa (x 492–562), açık meşe zemin; üst halkanın içinde ışık şeridi; kadrajın EN PARLAK şeyleri üç camdır
  ② KÖMÜR DEPO — sekizgen gövde, dikmeler, halkalar, konik çatı ve kapağı koyu kömür; depo x 299–796 (497 px) · y %29,4–58,3
  ③ PLATFORM — meşe deck, üç meşe basamak (x 588–825), platformun üç ön kenarında alçak siyah korkuluk (basamaklarda açık), iki dış
    köşede birer koyu saksı (x 143–236 · 871–941)
  ④ TANIKLAR — solda A çerçeveli rafta ÜÇ paslı panel (G0'da biri havadaydı, ikisi depodaydı) · sağ kenarda merdiven evi · uzak
    parapet · üç bina (açık taş + yeşil bakır çatı · kademeli tuğla · koyu cam blok), pencereleri yanık · mavi alacakaranlık gök ·
    işçi yok, el arabası yok, vinç yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–58,0'da (2x: 28,0–29,0) orta camın filmi tek geniş esnek tabaka hâlinde yukarıdan aşağı soyulur. Cam, çerçeve ya da bütün
   yüz filmle birlikte yerinden çıkarsa / film solarak "kaybolursa" → S7 atılır [DERS 49 · paketin kendi kontrolü].
⛔ Film kalkınca oda DEĞİŞİRSE — berjer sayısı, yeri ya da dönüşü, sehpa, ışık düzeni G7'nin arkasındakinden ve G5'tekinden farklıysa
   (G7 ↔ G8 üst üste bakılır) / yeni nesne belirirse (dize lamba, şemsiye, ekran, bar, üçüncü berjer) → S7 atılır [DERS 91 ③].
⛔ Işık titrer, söner ya da parlaklık zıplarsa → S7 atılır [DERS 98]. Işık G5'ten G8'e AYNI kalır.
⛔ Gök gündüze dönerse ya da camın yansıması iç ışığı boğarsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi +
   başlık, erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after", "BUILDWAKE" YOK. Kart G8 ile aynı dünya değilse → E kaydı
   [DERS 85]. klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta çatı rüzgârı (dijital sessizlik DEĞİL) [DERS 100].
⛔ Bir figürün yüzü okunursa ya da üçüncü figür belirirse S7 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk | %50 (py 960) — depo gövdesinin üst bandında | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ depo (gövde + konik çatı) | 299–796 px · %29,4–58,3 · 497 px | KESİR ±7 px · DOKUZ KAREDE |
| ⭐ orta dikme + çatı tepesi | x 498 / x 540 · tepe py 802 | ±0,5 puan · DOKUZ KAREDE (nirengi ①) |
| ⭐ üç ön yüz | sol geniş 309–498 · sağ geniş 498–727 · sağ dar 727–796 · %30,2–52,9 | DOKUZ KAREDE AYNI yer (G0 sağ geniş açık · G1–G5 üçü açık · G6–G7 filmli · G8 temiz) |
| sol dar yüz (kapı) | ≈ 10 px — kapı görünmez | kapı ÇİZİLİRSE (görünür bir yüzde) → ⑤ kimlik bulgusu [DERS 95] |
| ⭐ platform + üç basamak | platform 151–939 · basamak 588–825 px · %17,4–38,3 | ±0,5 puan · DOKUZ KAREDE (nirengi ②) · basamak sayısı ÜÇ |
| ⭐ üç bina + parapet | 14–105 · 201–255 · 862–939 px · tepeler py 815–842 · parapet py 1050–1137 | DOKUZ KAREDE AYNI (nirengi ③) |
| ⭐ A çerçeveli raf | 99–236 px · %37,5–50,4 | ±20 px [DERS 96 ①] · G0 boş · G1→ üç paslı panel |
| ⭐ G0 asılı panel | 99–225 px · %43,3–55,8 | YALNIZ G0 · rafın TAM üstünde, iki gergin sapan |
| ⭐ G0 paletli vinç | gövde 38–140 · bom 91–169 px | YALNIZ G0 · gövde + bom birlikte [DERS 46] · G1→ YOK |
| ⭐ merdiven evi | 884–1080 px · kapı 900–927 | ±20 px · DOKUZ KAREDE |
| ⭐ berjer A / B | 391–464 / 565–641 px · %32–40 | G5→ · TAM İKİ · dışarı bakar |
| ⭐ traverten sehpa | 492–562 px · %32,5–35,9 | G5→ · TEK · orta dikme ≈ 20 px örter |
| ışık şeridi | 329–699 px · py ≈ 925 | G5→ YANIK, AYNI parlaklık |
| korkuluk | 151–939 px · basamakta açık · %25,5–37,8 | G7→ · ince çubuklu (dolu panel değil) |
| ⭐ saksı sol / sağ | 143–236 / 871–941 px | G7→ · TAM İKİ · dış köşelerde |
| işçi (platformda) | ≈ 290 px boy | İKİ · yüz yok |
| üst band | %71–100 | yalnız açık gök (G0'da bom ucu py 787, bandın altında) |

## 3. ⭐ DEPONUN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ kabuk, dikmeler, konik çatı ve platform koyu turuncu-kahve pas, altında pullanan gri · ⭐ sağ geniş yüz AÇIK (karanlık delik):
    içeride yığılı eski borular + iki dik boru, kahverengi tortu · sol geniş yüz ve sağ dar yüz PASLI PANELLİ · ⭐ orta panel rafın
    TAM üstünde iki gergin sapanda asılı · ⭐ paletli vinç rafın ötesinde, bomu rafın üstünde · iki işçi (biri kumandalı, biri halatlı)
G1  ⭐ üç yüz AÇIK · ⭐ üç paslı panel rafta · ⭐ vinç YOK · borular ve tortu AYNI · ⭐ el arabası + boş çuvallar basamakların dibinde
G2  ⭐ boru YOK, tortu YOK — süpürülmüş pas kahvesi çelik zemin · kabuk hâlâ pas · ⭐ iki tel fırça, iki rulo, iki boya kutusu, katlı
    merdiven platformda
G3  ⭐ bütün kabuk KOYU KÖMÜR (dikmeler, halkalar, sol dar yüz, çatı, kapak, platform, basamaklar, iç duvarlar) · iç zemin gri çelik ·
    raftaki paneller PASLI (boyanmamış) · ⭐ meşe demetleri el arabasında
G4  ⭐ AÇIK MEŞE iç zemin (sağ geniş yüze paralel) · ⭐ meşe deck (ön kenara paralel) + meşe basamak yüzleri · oda boş · ⭐ sargılı
    berjer el arabasında
G5  ⭐ İKİ krem berjer (sol ve sağ geniş yüzün arkasında, dışarı bakar) · ⭐ TEK traverten sehpa (orta dikmenin arkasında) · ⭐ ışık
    şeridi düşük amber YANIK · ⭐ cam arabası (üç filmli cam) basamakların sağında
G6  ⭐ üç yüzde üç cam, dışta süt beyazı film, içeriden eşit sıcak parlar (şekil yok) · cam arabası YOK · ⭐ korkuluk istifi + iki
    saksı el arabasında
G7  ⭐ korkuluk üç ön kenarda (basamakta açık) · ⭐ iki saksı dış köşelerde · filmler amber parlar · ⭐ orta filmin sol üst köşesi bir
    karış açık, katlanmış · iki işçi orta camda · boş el arabası basamak dibinde · mavi alacakaranlık
G8  ⭐ üç TEMİZ cam · ⭐ berjerler, sehpa, meşe sıcak ışıkta camdan okunur · işçi, el arabası YOK
⛔ SAYIM: depo 1 · platform 1 · basamak 3 · raf 1 · merdiven evi 1 · bina 3 · paslı panel (G0: 2 yüzde + 1 askıda → G1–G8 rafta 3) ·
   açık yüz (1·3·3·3·3·3·0·0·0) · cam (0·0·0·0·0·0·3·3·3) · berjer (0·0·0·0·0·2·2·2·2) · sehpa (0·…·1·1·1·1) · saksı (0·…·0·2·2) ·
   vinç (1·0·…·0) · işçi (2·2·2·2·2·2·2·2·0) — kadro HİÇBİR klipte ikiyi aşmaz [DERS 89]
⛔ Deponun sekizgen biçimi, dikmeleri, halkaları, konik çatısı, platform ve basamaklar dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  panel: askı (rafın tam üstü) → vinç son metre indirir → raf · sapan: gergin → gevşek (ANCAK oturunca) → çözülür · vinç: bom
    katlanır → paletler → parapet boyunca sol kenar · yan paneller (×2, TEK TEK): yüz → iki el (dik) → basamaklar → raf · el
    arabası + çuvallar: merdiven evi kapısı → basamak dibi
S1  boru (TEK TEK): iç → iki el → açık yüz → basamaklar → el arabası → merdiven evi kapısı · tortu: kürek → çuval → el arabası →
    kapı · alet seti: kapı → platform
S2  pas: tel fırça → gri metal (dikme dikme, yüz yüz; çatı merdivenden) · iç zemin: fırça → gri çelik · kömür: kutu → rulo → yüzey
    (dikey şerit şerit, soldan sağa; iç duvarlar, platform, basamaklar) · boya takımı: → kapı · meşe demetleri: kapı → el arabası
S3  tahta: demet → el → çelik zeminin üstü (sağ geniş yüze PARALEL, sıralar arkadan açık yüzlere) · deck: → platform (ön kenara
    PARALEL, depodan kenara) · basamak yüzü → üç basamak · ambalaj: → kapı · sargılı berjer: kapı → el arabası
S4  ⭐ berjer A: el arabası → basamaklar → sol geniş yüz → yerine (DOĞRUDAN, dışarı bakarak) · berjer B: kapı → el arabası → sağ geniş
    yüz → yerine (A yerindeyken) · sehpa: kapı → aralarına · ışık şeridi: el → üst halka → YANAR · cam arabası: kapı → basamak sağı
S5  ⭐ cam (×3, TEK TEK): araba → iki el vantuzu → basamaklar → yüz (dikme + halkalara oturur; sol geniş → sağ geniş → sağ dar) ·
    boş araba: → kapı · korkuluk istifi + saksılar: kapı → el arabası → basamak sağı
S6  modül (TEK TEK): el arabası → iki el → platform kenarı (cıvata) · saksı (×2, TEK TEK): el arabası → basamaklar → dış köşe ·
    film köşesi: cam → işçinin eli (bir karış)
S7  film (×3): cam → iki el → yukarıdan aşağı tek tabaka → rulo → basamaklar → el arabası → merdiven evi kapısı
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı sağ kenardaki merdiven evi kapısı, el arabası, cam arabası ya da raf [DERS 48 · 49].
⛔ Kanca yalnız G0'da ve S0'ın ilk 2 sn'sinde, YÜKLÜ; vinç S0'da kadrajdan çıkar, sonra HİÇBİR karede yok [DERS 8 · 46]. İkinci
   kaldırıcı, tavandan sarkan cam kaldırıcısı, iskele, boya tabancası YOK [DERS 67 · 69 · 88].
⛔ Mobilya kendiliğinden kaymaz; her parça açık yüzden girer ve TEK TEK, DOĞRUDAN yerine oturur — ortada birleşip dönme yok
   [DERS 61 · 89 · 103].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI]

```
G0     05:45 (69,6°/+12,5°) · ⭐ alçak sabah güneşi sağda önde · kameraya bakan yüzler yumuşak gölgede · uzun gölge solda, kameraya doğru
G1     07:45 (87,6°/+34,6°) · parlak sabah · gölge solda
G2     09:45 (111,4°/+56,8°) · sert ışık · kısa gölge solda
G3     11:45 (168,7°/+72,2°) · ⭐ en düz ışık, güneş kameranın arkasında · gölge tabanda
G4     13:45 (239,4°/+61,9°) · gölge arkada sağa
G5     15:45 (267,4°/+40,2°) · ılık, güneş solda · gölge sağa · ⭐ ışık şeridi YANDI (G5→ aynı)
G6     17:45 (285,9°/+17,8°) · ⭐ altın akşam, soldan yalayan ışık · uzun gölge sağda · filmler içeriden parlar
G7     19:45 (304,5°/−2,6°) · ⭐ mavi alacakaranlık · solda sönen pembe · uzak pencereler yanmaya başlar · filmler amber
G8     19:55 (306,2°/−4,1°) · daha koyu mavi · ⭐ üç temiz camdan sıcak amber ışık
⛔ Gölge TEK YÖNDE döner (sol → arka → sağ); G5 → G8 gök TEK YÖNDE kararır; geri aydınlanan kare = zaman ters → ❷ [DERS 98 · 104]
⛔ G0–G4 boyunca HİÇBİR yapay ışık yanmaz; ışık şeridi G5'te yanar ve G8'e kadar AYNI kalır
⛔ Güneş diski HİÇBİR karede yok (kadraj azimutu −16,6° … +36,6°, güneş 58° → 302°) [DERS 39 · 70] · disk belirirse kare yeniden
```

## 6. ⭐ BİR DEPO · ÜÇ BASAMAK · İKİ İŞÇİ KAPISI [DERS 55 · 89 · 42]

```
Korpus riski: "water tank" → ayaklı ahşap su kulesi, su, ikinci depo · "rooftop" → dize lamba, şemsiye, bar, havuz · "viewing room"
→ dürbün, ekran (ÇIKARIM — bu filmde ölçülmedi). "water" · "tower" · "lounge" promptta YOK.
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ) · "Only two workers" her I2V'de · G8'de "No people are present."
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç cam / kaç berjer / kaç basamak
⛔ ikinci depo · dördüncü cam · üçüncü berjer · ikinci sehpa · üçüncü saksı · ikinci vinç · üçüncü işçi · dize lamba · şemsiye · bar → ⑧
⛔ Model dikmeleri, halkaları, çatıyı ya da basamakları yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Depoda, binalarda, merdiven evinde okunur yazı (numara, tabela) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 yan paneller rafa, el arabası · S1 tortu, alet seti · S2 kömür şeritler, meşe demetleri · S3 deck, basamak yüzleri, sargılı berjer ·
  S4 sehpa, ışık, cam arabası · S5 üçüncü cam, filmlerin parlaması, korkuluk + saksı · S6 gün batımı, film köşesi · S7 tutuş (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · çatı rüzgârı + uzak şehir uğultusu yatak · cam kırılma sesi YOK
· 0,0 vinç motoru · panelin rafa oturuşu · 3,0 vinç uzaklaşır · 8–15 boruların el arabasına bırakılışı, kürek, çuvallar · 16–23
  tel fırça → rulo · 24–31 parke klik + tokmak · 32–39 naylon, berjer ayakları, 37,0 düğme · 40–47 vantuz tıkları, camların yuvaya
  oturuşu · 48–55 korkuluk cıvataları, saksılar · 55,5 filmin ilk köşesi · ⭐ 56,5–58,0 orta filmin soyuluşu (KARE SENKRON ±2 kare) ·
  58–59 yan filmler · 59–60 adımlar, el arabası · 60,0–64,0 alacakaranlık çatısı
· KART 64,0–69,0: çatı rüzgârı sürer, kartın son saniyesinde söner → döngüde S0'ın vinç uğultusuna bağlanır
```

## 9. Zaman ve ışık

```
G0 05:45 69,6°/+12,5° · G1 07:45 87,6°/+34,6° · G2 09:45 111,4°/+56,8° · G3 11:45 168,7°/+72,2° · G4 13:45 239,4°/+61,9° ·
G5 15:45 267,4°/+40,2° · G6 17:45 285,9°/+17,8° · G7 19:45 304,5°/−2,6° · G8 19:55 306,2°/−4,1°
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · açık gök)
· zaman deponun gölgesi (sol → arka → sağ) ve gök rengiyle taşınır; final mavi saatte, ışık S4'ten beri yanık, film soyulur
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 sahne), beyanlı
① / ③ DİKİŞ     56,0 (B → A): uzun izli figürlerden kısa izli, tanınır figürlere; ışık mavi saatte sabitlenir — beyanlı [P5-c]
⑤ DEVAMLILIK    renk değişimi (pas → gri → kömür) ve iç değişim KASITLI; depo biçimi, dikmeler, halkalar, çatı, platform, basamaklar,
                raf, merdiven evi, binalar DEĞİŞMEZ · vinç YALNIZ G0'da KASITLI · raftaki paneller pas KASITLI (tanık)
⑦ İŞ            S7'nin 4–8'inde iş yok (kasıtlı tutuş) · G8 boş depo (kasıtlı: işçisiz final, kapak kaynağı)
⑦ TEMPO         S5 + S6: oda film arkasında (2x'te ~8 sn) — beyanlı bekleyiş; gök ve gölge zamanı taşır
① KAPI          paketin "sol giriş kapısı" bu açıdan görünmez (≈ 5 px) — beyanlı (plan TASARIM ③)
❺ TESLİM        işlev anı örtü sökümü — HIDDEN LOFT ile aynı mekanizma (sahip bilerek seçti 20.10.2026); fark: dış mekân, örtü camın
                dışında, ışık S4'ten beri yanık; LAST STOP ile vuruş vuruş içerik akrabası (beyanlı, yayın sırası ayrı)
```
