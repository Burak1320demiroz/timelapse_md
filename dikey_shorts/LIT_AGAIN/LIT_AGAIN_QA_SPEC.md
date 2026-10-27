# 🔍 LIT AGAIN — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `LIT_AGAIN_DIKEY_TIMELAPSE.md` · Günlük: `LIT_AGAIN_URETIM_GUNLUGU.md` · Kapak: `LIT_AGAIN_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      LIT AGAIN · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 23.10.2026 · kural 7 × 8 · sahibin briefi "8 × 8 sn, 9 G") · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "LIT AGAIN") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 3 ara kare (G2a · G5a · G6a; G7a = G8) + 12 klip (S2 · S5 · S6 · S7 ikişer 4 sn alt klip)
          · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye) · ⚠️ merceklere 8 SAHNE; alt klip dikişleri (20,0 · 44,0 · 52,0 ·
          60,0) sahne İÇİDİR, kesme sayılmaz
REJİM     S0–S6 + S7·a B (900× · 2 sa / 8 sn, alt klipte 1 sa / 4 sn) · S7·b G (gerçek zaman, 1×) — tek rejim dikişi 60,0'da
IŞIK      SAAT TEK YÖNDE · 05:15 → … → 19:15 → 20:15 → 20:15:04 (güneş saati) · 45° kuzey · 21 Haziran (δ +23,4°) · kamera 0°'ye (kuzey, açık
          deniz) bakar, tilt 0, 24 mm · güneş HİÇBİR karede yok · kapalı gri sabah → bulut dağılır → açık öğle → ılık ikindi → altın akşam →
          mavi saat · fener S7·a'nın son karesinde (≈ 59,8) TEK KAREDE yanar, S7·b'de lens döner
AİLE      KULE · kule %29,3–57,7 · başlık alanı fener odasının üstündeki açık gök (py 560–770)
TAKVİM    sahneler arasında haftalar (KESMEDE), sahne içinde 2 sa / 8 sn (alt klipte 1 sa / 4 sn · S7·b 4 sn) (beyanlı)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 63.5 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.75)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① YANAN FENER — fener odası (x 506–574 · py 867–922) sıcak beyaz sabit ışıltıda · kadrajın EN PARLAK şeyi · ışıltı camın içinde kalır,
    gökte ışık şeridi / yelpaze / sis bulutu YOK · korkuluk ışıltıyla hafif aydınlık
  ② RESTORE KULE — beyaz gövde (x 471–609 · py 949–1358) · TAM İKİ kırmızı bant (py 1044–1113 · 1208–1276) · koyu kırmızı kapı kameraya
    (py 1298–1358) · iki beyaz pencere · siyah korkuluk · siyah fener çerçeveleri · YEŞİL BAKIR kubbe (boyanmamış)
  ③ BOŞ SAHA — iskele YOK, kamyonet YOK, konteyner YOK, insan YOK · kayada soluk boya kırıntısı halkası · çakılda taze tekerlek izi
  ④ TANIKLAR — deniz ufku py 960 · dalgakıran sağ uzakta, ÜSTÜNDE IŞIK YOK · yosunlu kaya (sol alt) · şamandıra kaidesi (sağ alt) · başlık
    bandı (py 560–770) DÜZ derin mavi gök

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–58,0'da (2x: 28,0–29,0) kamyonet konteyneri çekerek servis yolundan sağ kenara SÜREKLİ yolla çıkar (iz olarak). Işınlanır (yarım kadraj
   tek adımda), ikiye çıkar ya da konteyner geride kalırsa → S7·a atılır [DERS 96].
⛔ 58,0–59,8'de gök TEK YÖNDE altından mavi saate geçer; geri dönerse → S7·a atılır [DERS 98].
⛔ ≈ 59,8'de (2x: 29,9) lamba TEK KAREDE yanar ve yanık kalır. "Yavaşça" yanar, titrer, söner, yeniden yanarsa → S7·a atılır [ISIK_FINALI §2 ·
   DERS 98].
⛔ 60,0–64,0 (2x: 30,0–32,0) TUTUŞ: kule, gök, deniz durur; yalnız lens döner, parlak yüzü ≈ 61,0–62,0'da BİR KEZ kameraya geçer. KULE,
   KUBBE ya da KORKULUK dönerse [DERS 56] · gökte huzme / ışık yelpazesi çizilirse [STAR DOCK] · dalgakıranda ikinci ışık yanarsa · insan,
   tekne, araç belirirse → S7·b atılır [DERS 91 ③].
⛔ Fener ışığı başlık bandını (py 560–770) aydınlatırsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63] — lensin tek parlak geçişi (69 × 55 px) BEKLENİR; tutuş ölçümü bu alanı dışarıda bırakır
   ya da eşiği bu beyanla okur.
⛔ Sahne bloğu S7·b tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık, erime
   ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta dalga + rüzgâr (dijital sessizlik DEĞİL) [DERS 100].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0 · 24 mm · h 14,6 m · D 47 m)

| ne | beklenen | tolerans |
|---|---|---|
| ⭐ deniz ufku | py 960 (%50), düz | ±0,5 puan · eğilirse kamera kaydı (nirengi ②) |
| ⭐ kule silüeti | taban x 471–609 (138 px) · py 1358 · top py 813 | KESİR ±7 px · ON ÜÇ KAREDE (nirengi ①) · 138 px değilse lens/mesafe kaymıştır → G8 yeniden [DERS 99] |
| ⭐ yeşil bakır kubbe + top | x 467–613 · py 813–867 | ON ÜÇ KAREDE AYNI renk ve biçim · üstünde kimse yok |
| ⭐ fener odası | x 506–574 · py 867–922 | G0–G3 kırık cam · G4–G5a camsız · G6 siyah çerçeve camsız · G6a→ camlı · G7 sönük · G7a = G8 YANIK |
| ⭐ kırmızı bantlar | alt py 1208–1276 · üst py 1044–1113 | G5a→ TAM İKİ · düz · eşit kalınlık (≈ 68 px) · iskele sökülürken KAYMAZ |
| ⭐ kapı | x 529–551 · py 1298–1358 | G0–G1 çürük, sol kanat sarkık · G2–G5a karanlık boşluk · G6→ koyu kırmızı, kameraya |
| ⭐ iskele | x 437–643 · kat tahtaları py 1303 · 1249 · 1194 · 1140 · 1085 · 1031 · 976 | G0–G1 0 · G2 TAM 4 · G2a–G6a TAM 7 · G7→ 0 · kule içinde 138 px kalır |
| ⭐ römork konteyner | x 338–419 · py 1379–1427 | G0–G6a sol altta · G7 kamyonete bağlı · G7a→ yok |
| ⭐ kamyonet | G1–G6a x 621–771 · py 1384–1452 · G7 konteynerin önünde (x ≈ 420–570) | TEK · G0 ve G7a→ yok |
| ⭐ yosunlu kaya · şamandıra kaidesi | x 180–324 · py 1455–1583 / x 751–801 · py 1496–1544 | ON ÜÇ KAREDE AYNI (nirengi ③) |
| dalgakıran | x ≈ 760–1080 · py ≈ 1000–1030 | hiç değişmez · üstünde ışık/kule YOK |
| işçi | Y 47'de ≈ 48 px | ÜÇ · yüz yok, kameraya dönük kimse yok · G7a–G8 yok |

## 3. ⭐ KULENİN İLERLEYİŞİ — kare kare, elle sayılır

```
G0   ⭐ kabarmış dökük beyaz boya + gri yamalar + pas izleri + iki SOLUK PEMBE bant izi · çürük kapı (sol kanat sarkık) · tahtalı pencereler ·
     paslı, kopuk korkuluk · kırık camlı fener, karanlık lens · dipte 2 m çalı + devrik çit + moloz, KAPININ ÖNÜ KESİLMİŞ · yarı dolu konteyner ·
     iki işçi · kamyonet YOK
G1   ⭐ taban temiz, kapı eşiği görünür · ⭐ kamyonet sağ altta, kasada borular + tahtalar · konteyner dolu · üç işçi · kule yüzü G0 ile aynı
G2   ⭐ TAM 4 kat iskele (4. kat alt pencerenin tepesinde) · kapı boşluğu karanlık (iki kanat konteynerde) · kasada yarım yük
G2a  ⭐ TAM 7 kat (galerinin hemen altında) + tepede ip makarası · gövde HÂLÂ dökük · iki raspacı EN ÜST katta · kasada boya kovaları
G3   ⭐ gövde çıplak gri-beyaz (boya ve pembe izler YOK) · fener odasında hâlâ kırık camlar · biri galeride
G4   ⭐ fener odası camsız, lens açıkça görünür · ⭐ alt kısım (alt pencerenin altına) beyaz astar · iki boyacı EN ALT katta
G5   ⭐ gövde baştan başa beyaz · ⭐ yeni siyah korkuluk · fener çerçeveleri paslı, camsız · kasada maske bandı + kırmızı kovalar
G5a  ⭐ TAM İKİ kırmızı bant · kapı boşluğu karanlık, pencereler tahtalı · kasada kapı + iki pencere çerçevesi
G6   ⭐ koyu kırmızı kapı · iki beyaz pencere · siyah fener çerçeveleri (camsız) · cam sandığı galeride
G6a  ⭐ fener odası camlı, lens temiz, SÖNÜK · iskele HÂLÂ 7 kat · iki işçi EN ÜST katta
G7   ⭐ iskele YOK · kamyonet konteynere bağlı (sol alt), kasada borular · konteyner brandalı · üç işçi · altın akşam · lamba SÖNÜK
G7a = G8  ⭐ saha BOŞ · mavi saat · fener YANIK (sabit ışıltı)
⛔ SAYIM: kule 1 · fener odası 1 · kapı 1 · pencere 2 · bant (0·0·0·0·0·0·0·2·2·2·2·2) · iskele katı (0·0·4·7·7·7·7·7·7·7·0·0) · kamyonet
   (0·1·1·…·1·0) · konteyner (1·…·1·0) · işçi (2·3·3·…·3·0·0) — kadro HİÇBİR klipte üçü aşmaz [DERS 89] · hareketli araç HİÇBİR anda birden
   fazla değil [DERS 69]
⛔ Kulenin biçimi ve boyu, kubbe, ufuk, dalgakıran, kaya ve kaide on üç karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0   çalı / çit / moloz: kulenin dibi → kol → konteyner · kamyonet: sağ kenar → servis yolu → dönüş alanı (park)
S1   iskele borusu: kasa → omuz → taban plakası / kat (halka halka, 2 m) · tahta: kasa → kat · kapı kanatları: menteşe → el → konteyner
S2·a boru demeti: kasa → ip → 5–7. kat · ip makarası: → iskelenin tepesi · boya kovaları: → kasa
S2·b boya kabuğu: duvar (EN ÜST kattan aşağı) → raspa + tel fırça → torba → ip → konteyner
S3   kırık cam: fener çerçevesi → yastıklı sandık → ip → konteyner · astar: kova → rulo → alt gövde
S4   beyaz boya: kova → rulo → gövde (EN ALT kattan galerinin altına) · eski korkuluk: galeri → ip → konteyner · yeni korkuluk: kasa → ip → galeri
     (bölüm bölüm, aynı yere) · maske bandı + kırmızı kova: → kasa
S5·a maske bandı → duvar · kırmızı: rulo → iki bant (önce alt) · bant: duvar → söküm · kapı + pencere çerçevesi: → kasa
S5·b kapı: kasa → iki el → patika → kapı boşluğu · eski pencere tahtası: pencere → ip → konteyner · pencere: kasa → pencere boşluğu · siyah
     boya: fırça → fener çerçeveleri · cam sandığı: kasa → ip → galeri
S6·a cam: sandık → iki el → fener çerçevesi (tek tek, çepeçevre) · boş sandık: galeri → ip → kasa
S6·b iskele: 7. kat → … → 1. kat (TEPEDEN aşağı) → ip → kasa · ip makarası + taban plakaları: son · kamyonet: dönüş alanı → geri geri → konteyner
     (bağlanır) · branda: → konteyner
S7·a üç işçi → kamyonet · kamyonet + konteyner: servis yolu → sağ kenar · lamba: görünmeyen anahtar → TEK KARE (son an)
S7·b lens: kaide üstünde döner (yalnız lens) · parlak yüz: → kamera, bir kez
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı kasa, ip, sandık ya da el [DERS 48 · 49 · 61].
⛔ Vinç YOK: her yük ip makarasıyla ya da elle — "crane" ve "hoist" hiçbir promptta yok (YASAK KELİME).
⛔ İskele bir anda belirmez / kaybolmaz: kat kat, 2 m [DERS 61] · kule iskeleyle genişlemez, iskeleyle silinmez (paketin Risk 1 · 2).
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI · HAVA_VE_ATMOSFER · DERS 98]

```
G0     05:15 (65,6°/+8,9°)  · ⭐ kapalı, alçak gri bulut · düz ışık, gölge YOK · kurşuni deniz
G1     07:15 (85,2°/+29,3°) · kapalı, bulut tabanı yüksek · sağ yüzde hafif aydınlık
G2     09:15 (108,8°/+50,3°) · ⭐ bulut yırtılır · sağ yüz güneşte · gölge SOL-ARKAYA
G2a    10:15 (126,5°/+59,7°) · dağılan bulut · gölge kısalır
G3     11:15 (153,2°/+66,6°) · ⭐ açık gök · ön yüz tam ışıkta · kısa gölge kulenin ARKASINDA
G4     13:15 (221,5°/+63,6°) · açık · kısa gölge SAĞ-ARKAYA
G5     15:15 (258,0°/+45,2°) · ılık · sol yüz ışıkta · gölge SAĞA
G5a    16:15 (269,6°/+34,6°) · gölge sağa uzar
G6     17:15 (279,8°/+24,1°) · ⭐ ılık altın · uzun gölge sağa
G6a    18:15 (289,5°/+13,8°) · alçak altın · gölge sağ-öne · denizde solda altın parıltı
G7     19:15 (299,4°/+4,2°)  · ⭐ güneş solda ufka yakın (kadraj dışı) · kulenin sol kenarı altın, ön yüz serin gölgede · gölge sağ-öne, ön plana
G7a=G8 20:15 (310,1°/−4,5°) · ⭐ mavi saat · gölge YOK · gök tepede derin mavi, solda ufukta soluk turuncu · kule OKUNUR · fener YANIK
⛔ Gölge TEK YÖNDE döner (sol-arka → arka → sağ-arka → sağ → sağ-ön); geri dönen kare = zaman ters → ❷ [DERS 98]
⛔ Hava TEK YÖNDE açılır (kapalı → yırtık → açık); kapalı göğe geri dönen kare → ❷
⛔ Güneş diski HİÇBİR karede yok (kamera kuzeye; yatay görüş 333,5°–26,5°) [DERS 39]
⛔ G0–G7 boyunca fener odasında YAPAY ışık yok (yalnız gök/güneş yansıması) · lamba ilk kez ≈ 59,8'de
⛔ Mavi saat zifiri değil: kule beyazı ve bantlar okunur [DERS 45]
```

## 6. ⭐ BİR KULE · BİR KAMYONET · ÜÇ İŞÇİ · TEK HAREKETLİ ARAÇ KAPISI [DERS 55 · 69 · 89 · 59]

```
Korpus riski: "lighthouse" → ikinci fener, dalgakıran ucunda ışık, tekne, martı sürüsü, gece gökyüzü · "restoration" → kalabalık ekip, vinç
(ÇIKARIM — bu filmde ölçülmedi). crane · hoist · beam · rays · searchlight · spotlight · fog · mist · haze · spray · jet · hose · boat · ship
promptta YOK.
① sayım cümlesi her karede POZİTİF ("one lighthouse tower on one rocky point, and the only tower in view") · "Only three workers" ve "Exactly
  one vehicle moves at a time" her I2V'de · G7a–G8'de "No people are present." · dalgakıran "with nothing on it"
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç araç aynı anda / kaç iskele katı / kaç bant
⛔ ikinci kule · ikinci fener · dalgakıranda ışık · ikinci kamyonet · vinç · tekne · dördüncü işçi · aynı anda iki hareketli araç → ⑧
⛔ Model kulenin biçimini, kubbeyi, ufku ya da kayayı yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Kamyonette, kapıda, kulede okunur yazı (marka, numara, logo) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn; alt klipte 1,0–2,0):
  S0 kamyonet girer, kasada borular · S1 kapı kanatları konteynere, 4. kat · S2·a makara + boya kovaları · S2·b kabuk torbası konteynere ·
  S3 astar alt gövdede, boyacılar en alt katta · S4 korkuluk siyaha, kırmızı kovalar kasada · S5·a üst bant + kapı kasada · S5·b fener
  çerçeveleri siyah + cam sandığı galeride · S6·a lens silinir, boş sandık iner · S6·b kamyonet konteynere bağlanır · S7·a lamba yanar ·
  S7·b tutuş (kasıtlı — yalnız lens)
⛔ 2x'te ikinci yarı tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · kalabalık sesi YOK · dalga + rüzgâr yatak · en çok üç martı · metal çarpışma, patlama YOK
· 0,0 testere · 5,0 kamyonet çakılda · 8–15 boru çınlaması, kelepçe · 16–23 ip makarası, kuru raspa · 24–31 cam çıtırtısı, sandık · 32–39 rulo,
  cıvata · 40–47 maske bandı, kapı menteşesi · 48–55 camın oturuşu, boru istifi, römork tıkı · 56–58 uzaklaşan motor · ⭐ 59,8 lamba rölesi +
  düşük uğultu (KARE SENKRON ±2 kare) · 60–64 dalga, rüzgâr, uğultu (lens dönüşüne SES YOK)
· KART 64,0–69,0: dalga + rüzgâr sürer, son saniyede kısılır → döngüde S0'ın testeresine bağlanır
```

## 9. Zaman ve ışık

```
G0 05:15 65,6°/+8,9° · G1 07:15 85,2°/+29,3° · G2 09:15 108,8°/+50,3° · G2a 10:15 126,5°/+59,7° · G3 11:15 153,2°/+66,6° ·
G4 13:15 221,5°/+63,6° · G5 15:15 258,0°/+45,2° · G5a 16:15 269,6°/+34,6° · G6 17:15 279,8°/+24,1° · G6a 18:15 289,5°/+13,8° ·
G7 19:15 299,4°/+4,2° · G7a = G8 20:15 310,1°/−4,5°
(45°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · görünür batış 19:48,5 · sahneler arası haftalar KESMEDE)
· zaman gök + gölge + deniz ile taşınır (kapalı → açık → altın → mavi); final mavi saatte, fener yanar ve döner
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief "8 × 8 sn"), beyanlı · alt klip dikişleri sahne İÇİ
① KADRAJ        24 mm · tilt 0 · h 14,6 m · D 47 m — kule DAR (138 px) ve kadrajın %28'i boyunda (sahip seçimi "kapak çekirdeği") · üst
                yarı açık gök · işçi ≈ 48 px — beyanlı
⑤ DEVAMLILIK    kulenin yüzü (dökük → gri → beyaz → kırmızı-beyaz), kapı, pencere, korkuluk ve fener odası KASITLI değişir; biçim, boy, kubbe,
                ufuk, kaya DEĞİŞMEZ · iskele G2–G6a, kamyonet G1–G7, konteyner G0–G7 KASITLI
❷ ZAMAN         sahneler arasında haftalar, saat tek yön (beyanlı) · 60,0'da rejim dikişi B → G — deniz dokusu ipekten dalgaya döner (beyanlı)
⑦ İŞ            S7·b (60–64) iş yok — kasıtlı TUTUŞ, yalnız lens döner · G7a–G8 insansız (kasıtlı) [SANTIYE_HAREKETI §4.7]
❺ TESLİM        işlev anı ışık — LAST STOP · GAME ON · TOTAL RESET · POOL ROOM · UNDERWATER OBSERVATORY · COLOSSUS · THE TURNTABLE'da da var
                (sekizinci, sahip onayladı 23.10.2026) · THE DARK ROCK · THE BLUE DOOR · THE LAST HARBOR · THE RAIN TOWER ile içerik/siluet
                akrabası — beyanlı
⑫ PARLAMA       lensin parlak yüzü ≈ 61,0–62,0'da fener odasını bir an tam beyaza çeker — KASITLI; gökte şerit olursa ⑧
```
