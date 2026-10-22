# 🔍 THE CLIFF POOL — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_CLIFF_POOL_DIKEY_TIMELAPSE.md` · Günlük: `THE_CLIFF_POOL_URETIM_GUNLUGU.md` · Kapak: `THE_CLIFF_POOL_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur [DERS 105 · QA_KOSU §4].

```
FİLM      THE CLIFF POOL · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 22.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "THE CLIFF / POOL") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 A (10 dk)
IŞIK      TEK GÜN → GECE, AÇIK GÖK: 07:00 → 09:00 → 11:00 → 13:00 → 15:00 → 17:00 → 19:00 → 20:30 (güneş saati) ·
          41° kuzey · 21 Haziran (δ +23,4°) · güneş 82°/+23° → 318°/+2° · kamera 220°'ye (güneybatı) bakar, tilt 22° AŞAĞI ·
          güneş hiçbir karede kadraja girmez · final GECE/ALACAKARANLIK: havuz taşar, ateş çukuru ve ışıklar yanar
AİLE      YÜKSEK ÇAPRAZ (aşağı bakış ailesi) · teras py 480–1450 · başlık alanı ufkun üstündeki sakin gök (py 560–770)
TAKVİM    yok — tek gün (dönüşüm sıkıştırıldı, beyanlı); zaman taşıyıcısı gölge süpürmesi (kayalıktan kanyona) + gök renkleri
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① BOŞLUĞA TAŞAN AKRİLİK SONSUZLUK HAVUZU — Konsolun ucunda 80 mm kalınlığında şeffaf akrilik ön cam; ardındaki berrak turkuaz
    su camın üst kenarından (infinity weir) pürüzsüz bir çarşaf gibi 45 metrelik kanyon boşluğuna kesintisiz dökülür;
    su içi cyan aydınlatmalar camın içinden geceye ışık saçar · kadrajın en berrak mühendislik odağı
  ② GÖMME ATEŞ ÇUKURU VE KEHRİBAR MİMARİ IŞIKLAR — Gömme bazalt oturma alanının merkezindeki doğrusal paslanmaz biyo-etanol
    şömine parlak sarı-turuncu alevlerle canlı yanar; tüm teras parapetlerinde, oturma bankı altlarında ve pergola kirişlerinde
    sıcak kehribar (#F2A43A) gizli LED ışıkları YANIKTIR
  ③ LÜKS BAZALT VE TİK GÜVERTE — Kömür rengi (#141819) mat bazalt taş kaplama ve zengin tik güverte tahtaları ıslak taşma ve
    kehribar ışık yansımalarıyla parlar; füme oturma minderleri ve minimalist tik şezlonglar yerinde; üstte siyah pergola saçağı
  ④ DEĞİŞMEZ NİRENGİLER — Sağdaki masif katmanlı bazalt kaya burnu · uçurumun dikey düşüş profili · uzaktaki kıyı headland
    ve deniz kanyonu ufku · terasın kayaya kilitlendiği beton ankraj temelleri · işçi yok, alet yok, hortum yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–58,0'da (2x: 28,0–29,0) su seviyesi son santimetreyi aşıp akrilik camdan taşar. Su zıplarsa / geri çekilirse /
   akrilik cam çerçeveden kayarsa → S7 atılır [SU §6].
⛔ 58,0'da (2x: 29,0) ateş çukuru alev alır ve BÜTÜN mimari LED ışıklar TEK ADIMDA birlikte yanar ve yanık kalır.
   Titrer, söner ya da sırayla yanarsa → S7 atılır [DERS 98].
⛔ Işık yanarken havuz, teras, pergola, şömine ya da kaya KAYARSA / yeni nesne belirirse (yüzücüler, parti, şemsiye, içecek)
   → S7 atılır [DERS 91 ③].
⛔ 60,0–64,0 FİNAL TUTUŞU: hiçbir şey değişmez (yalnız alevler ve taşan su çarşafı titreşir); ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık,
   erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK.
```

---

## 2. Kadraj kilitleri — her karede ölçülür (tilt 22° aşağı)

| ne | beklenen | tolerans |
|---|---|---|
| göz hizası ufku | py ≈ 460–500 (%25) — üst çeyrekte; deniz kanyonu ve uzak headland | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ sağ masif bazalt kaya burnu | x 780–1080 · py 320–1650 | DOKUZ KAREDE (nirengi ①) |
| ⭐ beton ankraj temelleri | x 120–420 · py 1380–1650 | KESİR ±8 px · DOKUZ KAREDE (nirengi ②) |
| ⭐ konsol taşıyıcı ekseni | x 280–820 · py 750–1450 | G1→ ana çelik · G3→ kaplama |
| ⭐ akrilik ön cam konumu | x 310–680 · py 820–1180 | G2→ cam takılır · G7→ su taşar |
| ⭐ gömme oturma çukuru | x 420–740 · py 1080–1420 | G1 çelik çanak · G3 taş kaplama · G5 mobilya |
| ⭐ doğrusal ateş çukuru | x 520–640 · py 1210–1280 | G5 takılır · G8 alev alır |
| pergola saçağı | x 220–840 · py 420–680 | G4→ üstte konsol |
| cam balustrad korkuluk | teras dış kenarı boyu · py 850–1420 | G4→ saydam cam |
| işçi sayısı | G0–G6: en çok 2 · G7–G8: 0 (insansız) | kadro HİÇBİR karede 2'yi aşmaz [DERS 89] |
| araç sayısı | G0–G2: mobil vinç · G3–G6: servis arabası / pompa · G7–G8: 0 | aynı anda en çok 1 hareket eden araç [DERS 69] |

---

## 3. ⭐ TERASIN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ uçurum kenarında ham gri beton ankraj blokları · açık kanyon boşluğu · havada iki çelik sapanla askıda ilk siyah çelik I-kiriş ·
    iki işçi sarı kılavuz halatları tutuyor · sağda masif katmanlı kaya · kuru saha
G1  ⭐ boşluğa 6 m uzanan iki ana konsol I-kirişi ve enine çelikler sabit · havuz çanağı ve gömme oturma çukuru ikincil çelik kasetleri serili ·
    kaynak makineleri ve kıvılcımlar · geçici çelik ızgara zemin
G2  ⭐ konsolun ucunda 80 mm şeffaf akrilik havuz ön camı çelik yuvaya oturmuş · vakumlu cam kaldırıcı vantuz çerçevesi camın üstünde ·
    iki camcı montaj kelepçelerini sıkıyor · havuz içi kuru
G3  ⭐ akrilik cam yerinde sabit · gömme çukur çevresine koyu kömür bazalt karolar döşenmiş · güneşlenme terasında zengin tik güverte tahtaları ·
    harç kovaları, mesafe takozları, karo mastarları
G4  ⭐ üstte duvara ankrajlı siyah çelik konsol pergola saçağı monte edilmiş · teras dış kenarında çerçevesiz lamine cam korkuluk panelleri ·
    zemin taş ve ahşap kaplı, temiz
G5  ⭐ gömme oturma çukurunda füme su geçirmez minderler döşeli · merkezde paslanmaz biyo-etanol ateş çukuru brülör ünitesi monte edilmiş ·
    güvertede iki tik şezlong · havuz çanağı kuru ve temiz
G6  ⭐ tüm inşaat aletleri ve iskeleler servis yolundan çıkmış · havuz %75 berrak turkuaz suyla dolu · şeffaf akrilik camdan su kırılması görünür ·
    gün batımı alacakaranlığı · teras yıkanmış
G7  ⭐ havuz suyu %95 seviyesinde, akrilik savak kenarının hemen altında sakin · ateş çukuru yakıtla dolu, sönük ·
    mavi saat alacakaranlığı · sahada hiç kimse yok · ışıklar sönük
G8  ⭐ havuz suyu akrilik camın üstünden boşluğa çarşaf gibi taşar · ortadaki ateş çukuru canlı altın-sarı alevlerle yanar ·
    tüm terasta, basamak altlarında ve havuz içinde kehribar (#F2A43A) LED ışıkları YANIK · işçi yok · lüks gece manzarası

⛔ SAYIM: teras 1 · konsol ana kiriş (0 askıda·2·2·…) · akrilik ön cam (0·0·1·1·1·1·1·1) · gömme çukur (0·1 çelik·1 taş·1 taş·1 mobilyalı…) ·
   ateş çukuru ünitesi (0·0·0·0·0·1·1·1y — y = yanan alev) · su seviyesi (0·0·0·0·0·0·%75·%95·taşan) ·
   ışıklar (0·0·0·0·0·0·0·0·hepsi yanık) · işçi (2·2·2·2·2·2·2·0·0)
⛔ Sağ kaya burnu, kanyon ufku ve beton ankraj nirengisi dokuz karede DEĞİŞMEZ.
```
