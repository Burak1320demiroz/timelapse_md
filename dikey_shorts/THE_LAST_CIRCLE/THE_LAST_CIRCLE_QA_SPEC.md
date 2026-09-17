# 🔍 THE LAST CIRCLE — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦).
> Plan: `THE_LAST_CIRCLE_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md`

```
FİLM      THE LAST CIRCLE · 7 × 8,0 = 56,0 sn · KAPAK KARTI YOK
SCENE BLOCK / END CARD    56,0 sn / yok
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① tamamlanmış kule — gövde + başlık, taç kadrajın ~%82'sinde
  ② huniye akan tahıl — kaynak (römork ağzı) ve hedef (huni ağzı) birlikte
  ③ kesintisiz apron + kenarındaki taş yuvak — dairenin izi YOK

⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 54,0'ta kadraj TAM HOME olmalı: yakınlaşma 7,0'da bitmiştir.
```

## 2. Kadraj kilitleri — her karede ölçülür

| ne | beklenen | tolerans |
|---|---|---|
| ufuk | %50,0 | ±0,5 puan |
| elevatör başı tacı (G5–G7) | %81,8 | ±1,5 puan |
| silo gövde üstü (G5–G7) | %73,9 | ±1,5 puan |
| gövde 9 m (G3) | %51,0 | ±2 puan |
| gövde 24 m (G4) | %65,9 | ±2 puan |
| ahşap ambar mahyası | %48,7 | ±0,5 puan · SEKİZ KAREDE DE |
| kavak hattı | %53,0 | ±1 puan |
| harman dairesi yakın kenar (G0–G5) | %36,7 | ±1 puan |
| harman dairesi genişliği (G0) | 546 px | ±25 px |
| silo gövde genişliği (G5–G7) | 209 px | ±15 px |
| taş yuvak | 46 × 33 px | ±8 px |

## 3. ⭐ BEDELİN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  daire BÜTÜN · rim kesintisiz · yuvak ortada
G1  kuzey kenarda ~6 m yay kırık · gerisi bütün
G2  üçte biri kazı + çalışma alanı
G3  yarısı
G4  çeyreği · ⛔ YUVAK SİLUETİ GÖRÜNÜR (yığınların arasında kaybolamaz) [P3-b]
G5  çeyreği açık · uzak yarı apron · yuvak HÂLÂ ortada
G6  TEK 5 m'lik yay açık · ⛔ YUVAK APRON KENARINDA (S5'te taşındı)
G7  yay YOK · kesintisiz apron · yuvak kenarda

⛔ GERİ GİDİŞ YOK: bir karede örtülen zemin sonraki karede açılamaz.
⛔ IŞINLANMA YOK: yuvağın yeri yalnız S5 klibinin İÇİNDE değişir; G4→G5 ve
   G6→G7 arasında taş aynı yerdedir [P3-c].
```

## 4. ⭐ İLK ÜRÜN KAPISI — S6 [P3-d]

```
① KAYNAK GÖRÜNÜR    tahıl römorkun çıkış ağzından çıkar; ağız kadrajda
② HEDEF GÖRÜNÜR     tahıl apron'a gömülü kabul hunisine düşer; huni kadrajda
③ İKİSİ AYNI KADRAJDA  yakın kompozisyonda kaynak ve hedef birlikte
⛔ Tepedeki kapalı başlıktan, elevatör muhafazasından ya da gövde duvarından
   tane DÖKÜLMEZ — görünmeyen yerden akan tahıl fizik hatasıdır.
⛔ Silonun DOLDUĞU gösterilmez; gösterilen şey İLK ÜRÜNÜN ALINMASIDIR.
④ HUNİ VE RÖMORK G6'DA ZATEN VARDIR — S6'da yalnız AKIŞ başlar.
```

## 5. ⭐ TAZE BETON KAPISI — S6 [P3-e]

```
① Son döküm, araç güzergâhının DIŞINDAKİ küçük ön zemin parçasıdır
② Römork ve huni önceden bitmiş sağlam apronda durur
③ Tahıl taze betonun ÜSTÜNE değil huniye akar
④ Yeni panel finalde HÂLÂ TAZE görünebilir — ani sertleşme yazılmaz
⛔ G7'de yüklü hiçbir araç taze panelin üzerinden geçmez.
```

## 6. ⭐ TEK KULE KAPISI [DERS 55]

```
SAYIM   kule 1 · elevatör muhafazası 1 · ahşap ambar 1 — SEKİZ KAREDE DE
⛔ İkinci bir silindirik gövde, silo dizisi, tank sırası ya da elevatör
   muhafazasının yuvarlak gövdeye dönüşmesi = KARE ATILIR.
⛔ Bu, araç kapısının ⑨ SAYIM TESTİ'yle ÖNCEDEN ölçülür; kapıda çıkarsa
   plan düşürülmez, ARAÇ DEĞİŞİR.
```

## 7. ⭐ KURGU KAPISI — yalnız S6 [KAMERA_HAREKETI §3]

```
① ÇÖZÜNÜRLÜK    kaynak ≥ 2160 × 3840 (2,0× için). Upscale sayılmaz.
② HOME DÖNÜŞÜ   7,0–8,0 sn kadrajı ile 0,0–0,5 sn kadrajı aynı: ahşap ambar
                 mahyası ≤ 4 px kayma
③ İLERİ DURUM    dönüşte iş geri alınmaz: yay örtülü, tahıl akıyor, panel taze
                 KAPI: klibin son karesi ↔ G7 · zincir_kontrol.sh
④ HEDEF          yakınlaşma son yay + kabul hunisine; ⛔ kuleye ya da tepeye DEĞİL
⑤ ÇAPA           yakın kadrajda taş yuvak görünür kalır (ikinci istasyon okunmasın)
⑥ KIRPMA SINIRI  kırpma dikdörtgeni kaynağın dışına taşmaz — boş kenar oluşmaz
⑦ TEK HAREKET    filmde başka yakınlaşma yok; S0–S5 tamamen sabit
⑧ RİTİM          son iki saniyede ikinci hareket, salınım ya da hız değişimi yok
```

## 8. Zaman ve ışık

```
IŞIK GÜNÜ   06:40 → 18:50 = 12 sa 10 dk · 1×A + 6×B ≤ 14 sa
GÜNEŞ       kadrajda HİÇ görünmez (bakış kuzey) · disk anılmaz [DERS 39]
GÖLGE       sabah sola · öğle kısa ve kameradan uzağa · akşam sağa
G7          güneş 2° · kule ışıkta, apron gölgede · final AYDINLIK [DERS 45]
MEVSİM      altın anız → sürülmüş toprak → sarı kavak → çıplak kavak + biçilmiş mısır
⛔ KIŞ YOK — yayda kış geçmez [DERS 7 · 26]
```

## 9. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM        süreler eşit (7 × 8,0) — proje sahibinin kesin kuralı, beyanlı
① / ⑤ "istasyon"  S6'daki kurgu yakınlaşması istasyon değişimi sayılırsa hüküm
                  BEKLENEN kabul edilir ve rapora "sahip kararı" diye geçer —
                  yeniden üretim sebebi DEĞİLDİR [KAMERA_HAREKETI §9]
⚠️ ÇOĞUL SİLO     beklenen DEĞİL — çıkarsa §6 gereği araç değişir
```
