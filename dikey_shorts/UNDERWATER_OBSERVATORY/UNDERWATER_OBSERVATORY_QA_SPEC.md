# 🔍 UNDERWATER OBSERVATORY — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `UNDERWATER_OBSERVATORY_DIKEY_TIMELAPSE.md` · Günlük: `UNDERWATER_OBSERVATORY_URETIM_GUNLUGU.md` · Kapak: `UNDERWATER_OBSERVATORY_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      UNDERWATER OBSERVATORY · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 22.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "UNDERWATER / OBSERVATORY") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S7 B (2 sa) — TEK rejim
IŞIK      TEK GÜN → GECE, AÇIK GÖK: 05:45 → 07:45 → 09:45 → 11:45 → 13:45 → 15:45 → 17:45 → 19:45 → 21:45 (güneş saati) ·
          41° kuzey · 21 Haziran (δ +23,4°) · güneş 69,6°/+12,5° → 327,5°/−18,3° · kamera 0°'ye (kuzey) bakar, tilt 24° YUKARI ·
          pencere kuzeye bakar: içeri güneş girmez · güneş HİÇBİR karede kadrajda değil · final GECE: su pencereyi kapatır, ışıklar yanar
AİLE      İÇ MEKÂN (bekleyen aile) · pencere %32,0–57,6 · başlık alanı pencerenin üstündeki düz kömür duvar
TAKVİM    yok — tek gün (dönüşüm sıkıştırıldı, beyanlı); zaman taşıyıcısı pencereden uzak kanyon duvarının ışığı (sağ → orta → sol) + gök
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① SUYA BAKAN PENCERE — TEK yuvarlak pencere (x 321–759 · py 814–1305) koyu çelik halkasının içinde; ardında berrak, derin turkuaz su
    pencerenin TAMAMINDA (su çizgisi yok, gök yok); iki deniz projektörünün uzun soluk huzmeleri, batmış kayada ışık dalgacıkları,
    TEK gevşek gümüş balık sürüsü (iz hâlinde) · kadrajın EN PARLAK şeyi turkuaz pencere
  ② İÇ IŞIKLAR — pencerenin iki yanındaki ahşap çıtalarda, halka çevresinde ve basamak altlarında kehribar ışık YANIK · masanın ön
    kenarında ince cyan şerit YANIK · masanın üstü KOYU (ekran yok, yazı yok)
  ③ ODA — pencere duvarı ve yan duvarlar kömür panel; pencerenin ÜSTÜ düz ve koyu (başlık zemini) · cam korkuluklu çelik asma kat (ön kenar
    py 1308–1361) boydan boya · sağda merdivenin üst kolu · kavisli gözlem masası (x 351–721) ve önünde bank · koyu taş zemin
  ④ TANIKLAR — monoray kirişi ve tavan · servis kapısı sol altta (x 108–386) · içeride HİÇ su yok · işçi yok, araba yok, alet yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–58,0'da (2x: 28,0–29,0) su çizgisi son çeyreği tırmanıp pencerenin tepesini aşar, köpük durulur. Su zıplarsa / iner sonra çıkarsa /
   içeri sızarsa / pencere çerçeveden kayarsa → S7 atılır [SU §6 · paketin kontrolü].
⛔ 58,0'da (2x: 29,0) BÜTÜN ışıklar TEK ADIMDA birlikte yanar ve yanık kalır. Titrer, söner ya da sırayla yanarsa → S7 atılır [DERS 98].
⛔ Işık yanarken masa, bank, korkuluk, kaplama KAYARSA / yeni nesne belirirse (dalgıç, köpekbalığı, denizaltı, ziyaretçi, ikinci pencere,
   lomboz, masada ekran) → S7 atılır [DERS 91 ③].
⛔ Pencere beyaza "patlarsa" (oda okunmazsa) / pencerenin üstündeki duvar aydınlanırsa (başlık zemini) → sebep G8; KARE yeniden üretilir,
   klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: hiçbir şey değişmez (yalnız balık izleri kayar); ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık, erime
   ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after", "BUILDWAKE" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta derin su sessizliği (dijital sessizlik DEĞİL) [DERS 100].
⛔ Bir figürün yüzü okunursa ya da üçüncü figür belirirse S7 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 24° yukarı)

| ne | beklenen | tolerans |
|---|---|---|
| göz hizası ufku | py ≈ 1530 (%20,3) — alt katın içinde; gök yalnız pencereden | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ pencere duvarının üst kenarı + monoray | py 473 · kiriş x 540 (py 326–514) | DOKUZ KAREDE (nirengi ①) |
| ⭐ yuvarlak açıklık | x 321–759 · py 814–1305 · 438 px | KESİR ±7 px · DOKUZ KAREDE (nirengi ②) · G0 yarım halka · G1 tam halka · G2→ cam |
| ⭐ çelik halka (dış) | x 288–792 · py 783–1349 | G1→ kesintisiz · TEK halka |
| ⭐ G0 askıdaki yay | x 290–790 · py 723–972 · kanca 679 | YALNIZ G0 · yerinin TAM üstünde (±20 px) [DERS 96] |
| ⭐ dış levha G0–G1 | açıklığın sağ kısmı (≈ x 566–759) | G0 filmli · G1 çıplak · AYNI yer (±20 px) · G2→ açıklığın tamamında |
| ⭐ servis kapısı + zemin–duvar birleşimi | x 108–386 · py 1402–1668 · birleşim py 1668 | ±20 px · DOKUZ KAREDE (nirengi ③) |
| ⭐ uzak deniz kapağı | x 455–622 · py 1139–1256 | G0–G6 KAPALI · G6'da açılır · G7→ suyun altında |
| iskele kuleleri | x 32–235 · 845–1048 · py 1302–1681 | G0–G2 · G3→ yok |
| ⭐ asma kat ön kenarı | kadraj boyu · py 1308–1361 | G3→ · TEK düz çizgi · pencereyi örtmez |
| ⭐ merdiven üst kolu | x 940–1062 · py 1308–1482 (→ sağ kenar) | G3→ · sağ duvarda |
| ⭐ cam korkuluk | üst py 1215 · kadraj boyu | G5→ · saydam |
| ⭐ gözlem masası + bank | masa x 351–721 · py 1608–1747 · bank 359–718 · 1706–1781 | G6→ · TEK masa, TEK bank · orta eksen · EKRANSIZ |
| projektör gövdeleri | ≈ x 346 / 731 · py 1255–1306 (camın ardında) | G2→ · TAM İKİ · G8'de yanık |
| ⭐ su çizgisi | G7: py ≈ 940–960 (pencerenin %75'i) · G8: pencerenin tamamı | G0–G6 su YOK · içeride HİÇBİR karede su yok |
| işçi | zeminde ≈ 236 px · iskelede ≈ 132 · asma katta ≈ 116 · sahanlıkta ≈ 65 (görünen) | İKİ · yüz yok |
| üst band | %75–100 | yalnız tavan + monoray (G0'da kablolar + yay tepesi) |

## 3. ⭐ SALONUN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ boş yuvarlak açıklık, YALNIZ alt yarım koyu çelik halka · ⭐ üst yarı (yay) monoraydan iki kabloyla, yerinin TAM ≈ 1 m üstünde ·
    iki iskele kulesi, iki işçi platformlarda, sarı kılavuz halatları · ⭐ dışarıda, sahanlıkta, açıklığın sağ kısmında beyaz filmli levha ·
    ham gri beton · sağ altta küçük kırık beton yığını · kanyon KURU, kapak KAPALI
G1  ⭐ TEK kesintisiz halka · kanca halkanın hemen üstünde (gevşek sapan) · ⭐ levha ÇIPLAK ve berrak, AYNI yerde · film rulosu sağ platformda ·
    bir işçi sol platformda, biri dışarıda
G2  ⭐ levha açıklığın TAMAMINDA (dışarıdan), dış sıkıştırma halkası belli belirsiz · boş beşik yok (sağda, duvarın arkasında) · ⭐ iki
    projektör gövdesi (sönük) dışarıda sol alt + sağ alt · iki işçi DIŞARIDA, camın ardında · iskele + rulo içeride
G3  ⭐ iskele YOK · ⭐ asma kat boydan boya (pencerenin hemen altı) · ⭐ sağ duvarda düz çelik merdiven · ham beton · moloz duruyor
G4  ⭐ kömür panel + pencerenin iki yanında dikey ahşap çıtalar · pencerenin ÜSTÜ ve asma katın ALTI düz kömür · ⭐ koyu taş zemin · moloz YOK ·
    kısa portatif merdiven sol yan duvarda · yassı araba kapının yanında
G5  ⭐ çerçevesiz cam korkuluk (asma kat + merdiven) · ⭐ halka çevresinde ve çıtalarda ışık kanalları — SÖNÜK · ⭐ gri battaniyeli masa alçak
    arabada kapının İÇİNDE · koruyucu örtü şeridi zeminde
G6  ⭐ masa ortada (sırtı kameraya, kavsi pencereye, düz mat koyu üst) · ⭐ bank · ⭐ asma katın ortasında sensör direği · alet arabası kapıda ·
    örtü YOK · ışıklar sönük · kanyon kuru
G7  ⭐ su pencerenin %75'inde (yatay çizgi, köpük, kabarcık) · üst çeyrekte koyu mavi gök · alacakaranlık · araba YOK · bir işçi asma katta,
    biri kapıda · içerisi KURU
G8  ⭐ su pencerenin üstünde (gök yok) · ⭐ projektörler + iç ışıklar YANIK · balık izleri · işçi YOK
⛔ SAYIM: salon 1 · açıklık 1 · kapı 1 · monoray 1 · halka (½·1·1·…) · yay askıda (1·0·…) · levha (1 dışarıda·1 dışarıda·1 yerinde·…) ·
   iskele kulesi (2·2·2·0·…) · projektör (0·0·2·2·2·2·2·2·2y — y = yanık) · asma kat (0·0·0·1·…) · merdiven (0·0·0·1·…) · korkuluk (G5→) ·
   masa (0·…·1p·1·1·1 — p = paketli, kapıda) · bank (0·…·1·1·1) · sensör direği (0·…·1·1·1) · balık sürüsü (0·…·1) ·
   işçi (2·2·2·2·2·2·2·2·0) — kadro HİÇBİR klipte ikiyi aşmaz [DERS 89]
⛔ Pencere duvarının üst kenarı, açıklığın çizgisi, servis kapısı, monoray dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  yay: monoray kancası → iki kablo → DÜŞEY iniş (≈ 1 m) → alt yarım halkanın iki ucu → cıvata · film: levha → işçinin eli → rulo → sağ
    iskele platformu
S1  levha: beşik → iki ray (sağdan) → açıklığın önü → halkanın dış yüzüne bastırılır → dış sıkıştırma halkası · beşik: → raylarla sağa,
    duvarın arkasına · projektör: sahanlığın sağ ucundaki istif → el → direk (sol alt · sağ alt)
S2  işçiler: sahanlık → sağa, duvarın arkası → servis kapısı (içeri) · iskele + rulo: kule → el → kapı (dışarı) · konsol: kapı → duvar
    (pencerenin altı) · plaka: kapının içindeki istif → konsollar (soldan sağa) · merdiven (iki kol): kapı → sağ duvar
S3  moloz: yığın → el arabası → kapı · panel + çıta: kapı → pencere duvarı + yan duvarlar · taş: istif → yassı araba → zemin (uzaktan
    kameraya, sıra sıra) · portatif merdiven: kapı → sol yan duvar
S4  yassı araba + portatif merdiven: → kapı · cam panel: istif → el → asma kat ön kenarı + merdiven · kanallar: → halka, çıtalar, basamaklar
    (SÖNÜK) · paketli masa: kapı → alçak araba → kapının içi · örtü: kapı → zemin
S5  masa: kapının içi → alçak araba → orta (≈ 6 m) → zemin · bank: kapı → masanın önü · direk: alet arabası → el → merdiven → asma kat ortası ·
    battaniye + örtü: → alet arabası
S6  alet arabası: → kapı · işçi: merdiven → asma kat · su: deniz → açılan kapak (beyaz su perdesi) → kanyon (görünmez) → pencerenin alt kenarı
    → camın DIŞINDA %75 (hiç düşmeden)
S7  su: %75 → pencerenin tepesi → üstü · ışık: tek adım → projektörler + çıtalar + halka + basamaklar + masa şeridi · işçiler: asma kat →
    merdiven → kapı
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı servis kapısı, dış sahanlık, raylar, istif ya da araba [DERS 48 · 49].
⛔ Tek makine monoray (yalnız S0) — vinç, ikinci kaldırıcı, vakumlu tavan kaldırıcısı YOK [DERS 69 · 88]. Uzun kiriş havada TAŞINMAZ [DERS 57].
⛔ Levha İÇERİDEN gelmez, kapıdan geçmez [TASARIM ② · DERS 88].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI]

```
G0     05:45 (69,6°/+12,5°) · ⭐ serin sabah · uzak duvar gölgede, yalnız sol kenarda ışık · solgun gök · içeride güneş lekesi YOK
G1     07:45 (87,6°/+34,6°) · parlak sabah · uzak duvar hâlâ gölgede, kenarı ışıkta
G2     09:45 (111,4°/+56,8°) · uzak duvar SAĞDAN yalanır, kaburgalar sola gölge
G3     11:45 (168,7°/+72,2°) · ⭐ en düz, en parlak · uzak duvar tam güneşte
G4     13:45 (239,4°/+61,9°) · ışık SOLDAN, gölgeler sağa
G5     15:45 (267,4°/+40,2°) · ılık, soldan yalayan · uzun gölgeler sağa
G6     17:45 (285,9°/+17,8°) · ⭐ altın akşam · uzak duvar gölgede, yalnız kenar altın
G7     19:45 (304,5°/−2,6°) · ⭐ mavi alacakaranlık · suyun üstünde koyu mavi gök şeridi · bütün iç ışıklar SÖNÜK
G8     21:45 (327,5°/−18,3°) · ⭐ gece · projektörler + kehribar çıtalar + halka + basamaklar + cyan şerit YANIK
⛔ Uzak duvardaki ışık TEK YÖNDE döner (sağ → orta → sol); G5 → G7 gök TEK YÖNDE kararır; geri aydınlanan kare = zaman ters → ❷ [DERS 98 · 104]
⛔ G0–G7 boyunca HİÇBİR yapay ışık yanmaz — kanallar G5'ten beri yerinde ama SÖNÜK
⛔ İçeride güneş lekesi HİÇBİR karede yok (pencere kuzeye bakar) — leke belirirse kare yeniden [DERS 104]
⛔ Güneş diski HİÇBİR karede yok (kadraj ±26,6°, güneş 58° → 302°) [DERS 39 · 70] · disk belirirse kare yeniden
```

## 6. ⭐ BİR SALON · BİR PENCERE · İKİ İŞÇİ KAPISI [DERS 55 · 89 · 42]

```
Korpus riski: "underwater observatory" → dalgıç, köpekbalığı, denizaltı, ziyaretçi kalabalığı, akvaryum tankları, lomboz dizisi, bilgi
ekranı · "construction" → kalabalık ekip, ikinci makine (ÇIKARIM — bu filmde ölçülmedi). diver · shark · submarine · aquarium · crowd ·
screen · monitor · display promptta YOK.
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ) · "Only two workers" her I2V'de · G8'de "No people are present."
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç pencere / kaç levha / kaç makine aynı anda
⛔ ikinci pencere · lomboz · ikinci halka · ikinci levha · ikinci kat · ikinci masa · masada ekran · dalgıç · köpekbalığı · denizaltı ·
   ziyaretçi · üçüncü işçi · içeride su → ⑧
⛔ Model pencere duvarını, açıklığın yerini, kapıyı ya da monorayı yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Masada, duvarda, kapıda, camda okunur yazı (numara, logo, gösterge) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 film soyulur, çıplak levha · S1 beşik döner, projektörler · S2 döşeme soldan sağa, merdiven · S3 taş zemin kameraya yaklaşır ·
  S4 ışık kanalları, paketli masa · S5 bank, sensör direği · S6 su camı tırmanır · S7 tutuş (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · beton salon tonu yatak · kaynak cızırtısı YOK · su sesi camın ARDINDAN, boğuk
· 0,0 monoray motoru · 2,0 yayın oturuşu (tok, tek) · impact wrench · 8–15 beşik makaraları, ⭐ 11,0 levhanın oturuşu, cıvatalar · 16–23 iskele
  boruları, çelik plakalar · 24–31 el arabası, matkap, taş · 32–39 cam paneller, kelepçeler · 40–47 araba tekerlekleri, masanın inişi, çelik
  basamakta adımlar · ⭐ 50,0 uzak kapağın açılışı · 52–56 boğuk su uğultusu · 56–58 uğultu derinleşir · ⭐ 58,0 röle tıkı + elektrik
  vızıltısı (KARE SENKRON ±2 kare) · 58–60 adımlar, kapı · 60,0–64,0 derin su sessizliği
· KART 64,0–69,0: derin su sessizliği sürer, kartın son saniyesinde söner → döngüde S0'ın monoray uğultusuna bağlanır
```

## 9. Zaman ve ışık

```
G0 05:45 69,6°/+12,5° · G1 07:45 87,6°/+34,6° · G2 09:45 111,4°/+56,8° · G3 11:45 168,7°/+72,2° · G4 13:45 239,4°/+61,9° ·
G5 15:45 267,4°/+40,2° · G6 17:45 285,9°/+17,8° · G7 19:45 304,5°/−2,6° · G8 21:45 327,5°/−18,3°
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · açık gök · SKY VAULT · GAME ON ile aynı gün modeli)
· zaman pencereden görünen uzak kanyon duvarının ışığıyla (sağ → orta → sol) ve gökle taşınır; final gecede, projektörler + iç ışıklarla
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 sahne), beyanlı
① KADRAJ        tilt 24° yukarı · göz hizası — dikeyler yukarı doğru hafifçe birleşir; merdivenin yalnız üst kolu kadrajda; dış sahanlıktaki
                işçiler camın ardında küçük (≈ 65 px); masa ve bank alt bantta (py 1608–1781) — beyanlı
⑤ DEVAMLILIK    pencerenin içi (boş → halka → cam → su) ve duvar yüzeyi (ham → kömür) KASITLI değişir; pencere duvarının kenarı, açıklığın
                çizgisi, kapı, monoray DEĞİŞMEZ · iskele yalnız G0–G2'de, levha G0–G1'de dışarıda KASITLI
③ ŞANTİYE       S2'nin ilk vuruşunda işçiler kadraj dışından (sahanlık → kapı) geçer — kapı kadrajda, yol değil (plan RİSK ③), beyanlı
⑦ İŞ            S7'nin 4–8'inde iş yok (kasıtlı tutuş) · G8 boş oda (kasıtlı: işçisiz final, kapak kaynağı)
❷ ZAMAN         içeride güneş lekesi yok (pencere kuzeye) — zaman pencereden okunur; G8'de gök görünmez (su) — gece iç ışıkla okunur, beyanlı
❺ TESLİM        işlev anı ışık — "ışık yanar" LAST STOP · GAME ON · TOTAL RESET · POOL ROOM'da da var (sahip bilerek seçti 22.10.2026);
                fark: asıl olay su — pencere kapanır, oda denizin altına geçer · balıklar rejim B'de iz (beyanlı)
```
