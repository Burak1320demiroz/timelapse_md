# 🔍 THE BLUE DOOR — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦ ⑨ ⑪ ⑫).
> Plan: `THE_BLUE_DOOR_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md` (üretimde açılır)

```
FİLM      THE BLUE DOOR · 7 × 8,0 = 56,0 sn · KAPAK KARTI YOK · LOGO YOK · VİDEO ÜSTÜ YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    56,0 sn / yok · ⛔ öncesi/sonrası karşılaştırma YOK
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok
REJİM     S0–S5 B (2 sa) · S6 ⭐ G (gerçek zaman, 8 sn) — iki rejim, üçüncü yok
IŞIK      TEK GÜN: 08:30 → 10:30 → 12:30 → 14:30 → 16:30 → 18:30 → 20:30 → 20:30 + 8 sn · 40° kuzey · δ +15° ·
          güneş 88°/21° → 291°/−1,4° · kamera KUZEYE bakar · final MAVİ SAAT, ışık yapının kendisinden [DERS 45 notu]
TAKVİM    yok — tek gün (haftalık iş sıkıştırıldı, beyanlı); mevsim taşıyıcısı ışık + balkondaki sardunya
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① MAVİ KAPI AÇIK, IŞIK KALDIRIMDA — kapı kemerde (x %43–53 · kilit taşı %44,8) içe açık; eşikten kaldırıma, masalara
    kadar (y %28–33) sıcak sarı ışık yelpazesi
  ② CEPHE YANIYOR — vitrin (x %59–76 · y %34–44) ve iki üst pencere (y %51–60) sıcak sarı; iki pirinç fener (x %39 · %56 ·
    y %43) ve sokak lambası (x %25) yanık; taş BAL rengi, mavi saatte OKUNUR (gece değil)
  ③ FİNCAN + FİGÜR — vitrin altındaki masada (x %66 · y %33) buharı tüten fincan; eşikte (x %48 · y %31–39) sırtı dönük
    önlüklü TEK figür

⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 52,0'de kapı AÇILIYOR olmalı (kapı hareket hâlinde); 54,0'te açık. Kapı 48,0'de açıksa rejim/sıra yanlış: S6 atılır.
⛔ 56,0'da film figür eşikteyken kesilir; sonrasında kart, logo, fade, müzik, "before/after" YOK.
⛔ Figürün yüzü okunursa ya da ikinci figür belirirse S6 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | %50 | ±0,5 puan · SEKİZ KAREDE DE |
| ⭐ komşu balkonu (x · y) | %0–20 · %52,4 | ±0,5 puan · SEKİZ KAREDE DE (nirengi ①) · biçim değişmez (BROKEN CLIMB E04 riski) |
| ⭐ sokak lambası (x · y taban/tepe) | %25 · %27,8–51,1 | ±0,5 puan · SEKİZ KAREDE DE (nirengi ②) · G6–G7 yanık |
| ⭐ saçak × sağ kenar (x · y) | %82 · %69 | ±1 puan · SEKİZ KAREDE DE (nirengi ③) |
| ⭐ kapı kemeri (x · kilit taşı y) | %42,9–52,9 · %44,8 | ±0,5 puan · SEKİZ KAREDE DE · KESİR 108 px ±5 ("aynı yer" nesnesi) |
| cephe (x · taban · saçak · mahya) | %25–82 · %30,9 · %69,1 · %73,5 | ±1 puan · SEKİZ KAREDE DE |
| vitrin (x · y) | %58,6–75,7 · %33,8–43,8 | ±1 puan · G0–G2 tahtalı, G3→ cam |
| üst pencereler (x · y) | %30–40 · %61,4–71,4 · %51,4–59,5 | ±1 puan · G0–G2 çürük, G3→ meşe + cam |
| pirinç fenerler (G4→) | %39,3 · %56,4 · %43,3 | G4–G5 sönük · G6–G7 yanık · G0–G3 YOK |
| masalar (G5→) | %30 · %66 · %28,7–32,7 | SAYI 2 · sandalye 4 · saksı 2 (%39,7 · %55,9) |
| konteyner (G0–G5) | %66–97 · %22–32 | G6'da YOK (soluk iz + pas lekesi) |
| kamyonet (G4–G5) | %10–31 · %22–37 | G3'te ve G6'da YOK |
| iskele (G1–G3) | %25–44 · %29–73 | G4'te istif, G5'te kamyonette, G6'da YOK |
| sarmaşık (yalnız G0) | %25–50 · %31–69 | G1'den sonra YOK, kök izleri VAR |
| ⭐ figür G6 / G7 | %34 · %25–35 / %48 · %31–39 | TEK · sırtı kameraya |
| gök bandı | %73,5–100 | B'de streak · G'de hold · güneş diski HİÇBİR karede |

## 3. ⭐ YAPININ İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  cephe IS-KARA · sarmaşık sol yarıda · vitrin tahtalı · üst pencereler çürük · kapı kara + TEK MAVİ ŞERİT · çöp yığını ·
    jet ünitesi + işçi · boş konteyner
G1  cephe kara + KÖK İZLERİ · saçak altında İLK BAL BANDI · kapı SOLUK MAVİ (soyuk) · sarmaşık + yığın YOK · konteyner dolu ·
    iskele sol yarıda (işçi tepede)
G2  cephe BAL · soluk kök izleri · tabanda gri silt · kapı soluk mavi · pencereler hâlâ çürük, vitrin tahtalı · ilk yeni
    kasa İPTE · kasa istifi · jet ünitesi YOK
G3  3 YENİ PENCERE (meşe + cam) · eski kasa + tahta istifte · kapı SEHPADA (zımparalı, ilk mavi) · kemer KARANLIK · iskele
G4  kapı KOYU MAVİ + pirinç, kemerde · 2 SÖNÜK FENER · iskele İSTİFTE · kırık kaldırım · kamyonet (masa, sandalye, saksı, plak)
G5  YENİ KALDIRIM · 2 masa · 4 sandalye · 2 saksı · sol saksıda SARMAŞIK ÇELİĞİ · kamyonet yüklü · konteyner · ışıklar sönük
G6  mavi saat · fenerler + lamba + vitrin + üst pencereler YANIK · kamyonet + konteyner YOK · fincan buharlı · figür yürüyor
G7  aynı · kapı AÇIK · ışık yelpazesi kaldırımda · figür eşikte
⛔ SAYIM: dükkân 1 · kapı 1 · vitrin 1 · üst pencere 2 · masa (0·0·0·0·0·2·2·2) · saksı (0·…·0·2·2·2) · fener (0·0·0·0·2·2·2·2)
   · iskele (0·1·1·1·istif·kamyonet·0·0) · konteyner (1·1·1·1·1·1·0·0) · kamyonet (0·0·0·0·1·1·0·0) · figür net (0·…·0·1·1)
⛔ Cephe G2'den sonra rengi DEĞİŞMEZ (yalnız ışık); pencereler G3'ten sonra DEĞİŞMEZ; kapı G4'ten sonra yalnız açılır (G7).
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK §4 · DERS 48 · beş soru ②③]

```
S0  sarmaşık: duvar → el → konteyner · çöp: yığın → konteyner · iskele: sokak → cephe (tekerlek)
S1  is: taş → jet → şerbet → ızgara (kalıntı silt) · kasa istifi: sokak → kaldırım
S2  ⭐ kasa (yeni): istif → makaralı el vinci + ip + sapan → boşluk (kireç harcına) · kasa (eski): boşluk → iskele → istif ·
    cam: sokak → VANTUZ (iki kişi) → vitrin kasası · kapı: menteşe → sehpa (elle, düz yatar)
S3  kapı: sehpa → DİK taşınır → menteşe (kemerle aynı boy) · fener: el → duvar · iskele: cephe → istif (çerçeve çerçeve)
S4  kaldırım (eski): → el arabası → konteyner · plak: kamyonet paleti → kum yatak · mobilya: kamyonet → kaldırım · çelik → saksı
S5  kamyonet → çıkış (sol) · konteyner → kanca kollu kamyon → çıkış (sağ) · fincan: iç → masa (iz)
⛔ Vinç YOK (dar sokak) — model kule/mobil vinç çizerse ⑧ APPEARED.
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı bir önceki karede ya da klibin içinde görünür [DERS 48].
⛔ Kapı hiçbir karede kemerden BÜYÜK ya da KÜÇÜK değildir (108 px ±5) — sehpada yatarken bile aynı boy.
```

## 5. ⭐ GÖLGE KAPISI [ZAMAN_VE_ISIK §2]

```
G0–G1  gölgeler SOLA (güneş sağda, 88°→109°) · G0 sıyırıcı: is lekeleri ve sarmaşık kabartılı
G2–G3  gölgeler AŞAĞI, en kısa (148°→212°, el 62°) · bal rengi düz
G4–G5  gölgeler SAĞA (251°→272°) · G5 turuncu sıyırıcı: taş örgüsü ve kapı pervazı kabartılı
G6–G7  doğrudan güneş YOK (−1,4°) · mavi gök + sıcak yapay ışık · gölge yalnız fener ve kapı ışığından
⛔ Güneş diski HİÇBİR karede yok (bearing 0°, güneş 88°–291°: kadraj bandı 333°–27°'nin dışında) [DERS 39]
⛔ Döngü kesmesi (G7 → G0): mavi saatten sabah güneşine — okunur, beklenir
⛔ Final gece gibi karanlıksa (taş okunmuyorsa) G7 yeniden — mavi saat, gece değil
```

## 6. ⭐ BİR DÜKKÂN · BİR KAPI KAPISI [DERS 55]

```
Korpus riski: "café" → tente, tabela, masa sırası, kalabalık · "shop front" → komşu vitrinler · "blue door" → Santorini
① sayım cümlesi her karede POZİTİF ("one shop with one arched doorway, one shop window and two upper windows")
② mobilya sayıyla (2 masa · 4 sandalye · 2 saksı) · tabela / menü / yazı metin yasağında
③ araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç kapı / kaç masa / kaç figür
⛔ Tente · tabela · üçüncü masa · ikinci figür · sokakta yaya → ⑧
⛔ Komşu ev değişirse (renk, balkon, pencere) → ⑤ DEVAMLILIK (model "her şeyi temizler" riski, S1)
```

## 7. ⭐ REJİM G KAPISI — S6 [SANTIYE_HAREKETI §1 · P5-a…d]

```
· "moves at natural speed" · "Eight seconds pass" · gölge KIPIRDAMAZ · gök holds
· TEK figür, sırtı kameraya, yüz yok [P5-b] — iz YOK
· hareket eden = figür (yürür, kolu tutar, eşiğe çıkar) · kapı (içe açılır) · ışık yelpazesi (genişler) · buhar · mum alevi
· zamanlama: 0–3 yürür · 3,5 kol · 4–6 kapı açılır + ışık genişler · 6–8 eşikte siluet (son kare = doruk)
· 48,0 kesmesi (B → G) dikiş: figür izden nete — ① / ③ hükmü BEKLENEN [P5-c]
⛔ Kapı dışa açılırsa / kemerden farklı boyda çizilirse / ışık kapı açılmadan dökülürse klip atılır
⛔ G6 ≈ G7 durgunluk (kapı açılmıyor) → S6 atılır [P5-d]
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–56,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı yok · konuşma yok (iç mekân uğultusu KELİMESİZ: fincan, kaşık)
· 0,0 jet · 2,0–4,0 sarmaşık yırtılması · 8,0–14,0 jet süpürmesi · 16–24 makara + ahşap-taş tıkırtısı · 22,0 vantuz ·
  24–27 zımpara → boya fırçası · 29,0 menteşe · 32–40 taş plak (×8) + sandalye · 45,0 fener "tık" · 46,5 fincan-tabak ·
  ⭐ 51,5 pirinç kol · 52,0 menteşe + iç mekân uğultusu açılır — S6'da görüntü 1×: KARE SENKRON aranır (±2 kare)
· S0–S5: vuruşlar olaya ±0,5 sn · 56,0'da ses kesilmez, döngüde S0 jetine bağlanır
```

## 9. Zaman ve ışık

```
G0 08:30 88°/21° · G1 10:30 109°/44° · G2 12:30 148°/62° · G3 14:30 212°/62° · G4 16:30 251°/44° · G5 18:30 272°/21° ·
G6 20:30 291°/−1,4° · G7 20:30 + 8 sn aynı   (40°K · δ +15° · saat = güneş saati + 1 sa 30 dk · TÜRETİLMİŞ model)
· gölge YÖNÜ G0–G1 sola, G2–G3 aşağı, G4–G5 sağa, G6–G7 yapay ışık
· S5 içinde gün batımı: turuncu → mavi; ışıklar SIRAYLA: fener → lamba → vitrin → üst pencereler
· bulut: B kliplerinde streak · S6'da holds — I2V'lerde yazılı
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      7 × 8,0 — sahip kuralı, beyanlı
① / ③ DİKİŞ     48,0 (B → G): figür izden nete — beyanlı [P5-c]
① İSTASYON      S1'de bütün cephe renk değiştirir: model cepheyi YENİDEN ÇİZEBİLİR (taş örgüsü, boşluk yeri) — pilot (c)
⑤ DEVAMLILIK    renk değişimi (kara → bal, soluk → koyu mavi) KASITLI; boşluk, kemer, komşu ev, lamba DEĞİŞMEZ
⑧ MADE          cam vitrine vantuzla (kaynağı sokak, kadraj dışı sol alt — beyanlı); fenerler S3'te takılır
⑦ İŞ            S6'da inşaat yok (kasıtlı): ödül yapının ışığı ve kapısı [P8-f]
③ ZAMAN         mavi saat finali: gece okunursa ③ "saat sıçraması" der — G7 yeniden
④ TESLİM        dördüncü müziksiz film · BROKEN CLIMB ④ dersi: 56,0 sn, kart yok
①               kaldırım + sokak y %0–25 — alt UI bandı; kanıt taşımaz (masalar %29–33'te, bandın üstünde)
```
