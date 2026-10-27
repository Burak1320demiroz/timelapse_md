# 🔍 THE SUNKEN GARDEN — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_SUNKEN_GARDEN_DIKEY_TIMELAPSE.md` · Günlük: `THE_SUNKEN_GARDEN_URETIM_GUNLUGU.md` · Kapak: `THE_SUNKEN_GARDEN_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur [DERS 105 · QA_KOSU §4].

```
FİLM      THE SUNKEN GARDEN · 7 × 8,0 = 56,0 sn · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 0,5 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik ses yatağı)
SCENE BLOCK / END CARD    56,0 sn / 5,0 sn (G7 + "THE SUNKEN / GARDEN") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış afişi YOK
PAYLAŞIM  2x — 28,0 sn sahne bloğu + 5,0 sn kart = 33,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok · ⭐ üretim sırası G7 (metinden) → G6 … G0 (geriye)
REJİM     S0–S5 B (2 sa) · S6 A (10 dk)
IŞIK      SABAH → MAVİ SAAT: 08:00 (112°/18°) → 10:30 (142°/38°) → 12:30 (182°/42°) → 14:30 (215°/32°) → 16:30 (238°/22°) → 17:45 (255°/12°) → 18:30 (268°/4°) → 19:15 MAVİ SAAT (285°/0°) ·
          kamera kuzeye (0°) bakar, tilt 15° AŞAĞI · güneş hiçbir karede kadraja girmez · final MAVİ SAAT: ip ışıklar ve ateş çukuru ana ışık
AİLE      TİLTLİ AŞAĞI BAKIŞ (tilt −15° · KAMERA_DILI §3) · havuz tabanı py 780–1920 · başlık alanı tuğla duvar üstü sakin gök (py 200–450)
TAKVİM    yok — tek gün sonbahar dönüşümü; zaman taşıyıcısı gölge süpürmesi (güneydoğudan kuzeybatıya) + gök renkleri
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 27.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① MERKEZİ DOĞAL TAŞ ATEŞ ÇUKURU — Platformun tam merkezinde 1,2 m çapında dairesel yığma taş ateş çukuru içinde canlı,
    titreşen altın-turuncu alevler; sıcak ışık taş halkayı ve etrafındaki ahşap plankaları aydınlatır
  ② SICAK BEYAZ BİSTRO İP IŞIKLARI — Arka sarı-kahve tuğla duvar boyunca zarif kıvrımlarla asılı sıcak beyaz lambalar
    TEK KAREDE yanmış ve yanık kalır; duvarda ve ahşap zemin üstünde altın yansımalar üretir
  ③ LÜKS HARDWOOD PLATFORM, BAMBULAR VE İNSANLAR — Çukur havuz tabanını kaplayan temiz altın-kahve hardwood planking platform;
    çevredeki 6 ahşap saksı kasasında yeşil uzun bambular; minderli iki ahşap bankta oturan, ateşi izleyen iki rahat figür
  ④ DEĞİŞMEZ NİRENGİLER — Arka sarı-kahve tuğla duvar · sağ köşedeki paslı taşma borusu · sığ uçtaki hardwood kaplı 3 basamak ·
    sol duvarda eski krom dayanak YOK (söküldü, izi temiz) · inşaat molozu yok, el arabası yok, alet yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 50,0'da (2x: 25,0) iki kişi basamaklardan iner, banklara oturur.
⛔ 50,0–52,0'da (2x: 25,0–26,0) bistro ip ışıkları TEK ADIMDA yanar ve merkezdeki ateş çukuru alev alır.
   Titrer, söner ya da sırayla yanarsa → S6 atılır [DERS 98].
⛔ Işık yanarken havuz duvarı, basamaklar, tuğla duvar veya ateş çukuru KAYARSA → S6 atılır [DERS 91 ③].
⛔ 52,0–56,0 (2x: 26,0–28,0) FİNAL TUTUŞU: hiçbir şey değişmez (yalnız alevler titreşir); ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S6 tutuşuyla biter; ardından YALNIZ kapak kartı 56,0–61,0 (yayında 28,0–33,0): kaynak G7'nin kendisi + başlık,
   erime ≤ 0,5 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK.
```

---

## 2. Kadraj kilitleri — her karede ölçülür (tilt 15° aşağı)

| ne | beklenen | tolerans |
|---|---|---|
| göz hizası ufku / duvar tepesi | py ≈ 240–320 (%15) — üst üçte birde; tuğla duvar üstü gökyüzü | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ arka tuğla duvar | x 0–1080 · py 200–680 | DOKUZ KAREDE (nirengi ①) |
| ⭐ sağ paslı taşma kanalı borusu | x 920–1020 · py 580–660 | DOKUZ KAREDE (nirengi ②) |
| ⭐ sığ-uç giriş basamakları | x 216–864 (216 px) · py 460–780 | KESİR ±8 px · DOKUZ KAREDE (nirengi ③) |
| ⭐ sol krom ladder dayanağı | x 120–220 · py 680–840 | G0–G4 VAR · G5 sökülür · G6–G7 YOK |
| ⭐ merkez dairesel ateş çukuru | x 420–660 · py 1180–1460 | G5 inşa · G7 alev alır |
| ahşap saksı kasaları (6 adet) | perimeter boyunca · py 860–1520 | G4 (3 adet) · G5 (6 adet) · G6-G7 (bambulu) |
| işçi sayısı | G0–G5: en çok 2 · G6: 2 peyzajcı · G7: 0 (işçi yok, 2 oturan misafir) | kadro HİÇBİR karede 2 işçiyi aşmaz [DERS 89] |
| araç sayısı | G0: el arabası · G1: mini yükleyici (apron) · G2: bahçe arabası · G3–G6: 0 | aynı anda en çok 1 hareket eden araç [DERS 69] |

---

## 3. ⭐ HAVUZUN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ terkedilmiş beton havuz tabanında derin ıslak yaprak ve çalı yığını · kürek dalan işçi · çuval dolduran ikinci işçi ·
    sol duvarda eski krom merdiven dayanağı · arka tuğla duvar ve taşma borusu sabit
G1  ⭐ yaprak yığını temizlenmiş · nemli koyu gri beton taban açıkta · apron üstünde mini yükleyici duruyor ·
    işçi yüksek basınçlı yıkama jetiyle tabandaki yosun ve çamuru drenaja süpürüyor
G2  ⭐ havuz tabanı yıkanmış, çatlak çizgileri belirgin · tabanın %40'ına yıkanmış drenaj çakılı serilmiş ·
    işçiler iki tekerlekli araba ve tırmıkla çakılı düzlüyor · krom dayanak yerinde
G3  ⭐ çakıl tabanın tamamına yayılmış ve sıkıştırılmış · çakıl üstünde 100x100 mm emprenye ahşap karkas kirişleri monte ediliyor ·
    marangozlar akülü vidalama ile köşe gönyelerini sabitliyor · krom dayanak solda
G4  ⭐ ahşap karkas üstüne %75 oranında lüks hardwood planking vidalanmış · sağ duvarda 3 adet dikdörtgen ahşap saksı kasası ·
    marangozlar son tahtaları hizalıyor · krom dayanak solda · basamaklar henüz beton
G5  ⭐ hardwood planking platformu tamamlanmış · apron üstünde taş blokları istifli · basamaklar hardwood ile kaplanmaya hazır ·
    krom dayanak henüz söküm öncesi son anında · sönük ip ışık kablosu duvarda
G6  ⭐ krom dayanak sökülmüş (YOK) · basamaklar lüks hardwood ile kaplı · merkezde dairesel doğal taş ateş çukuru halkası bitmiş ·
    6 saksı kasasında uzun yeşil bambular dikili · minderli 2 bank yerinde · ışıklar sönük · alacakaranlık
G7  ⭐ USTA KARE: merkezdeki taş ateş çukurunda canlı altın alevler · arka tuğla duvarda sıcak beyaz bistro ışıkları YANIK ·
    bambular hafif rüzgarda canlı · 2 kişi banklarda oturmuş · mavi saat alacakaranlığı · kusursuz batık bahçe

⛔ SAYIM: havuz 1 · krom dayanak (1·1·1·1·1·1söküm·0·0) · çakıl (%0·%0·%40·%100·%100·%100·%100·%100) ·
   ahşap zemin (%0·%0·%0·karkas·%75·%100·%100·%100) · basamaklar (beton·beton·beton·beton·beton·beton·hardwood·hardwood) ·
   ateş çukuru (0·0·0·0·0·taşlar·halka·yanan alev) · ışıklar (0·0·0·0·0·sönük·sönük·yanık)
⛔ Arka tuğla duvar, sağ taşma kanalı ve basamak nirengisi sekiz karede DEĞİŞMEZ.
```
