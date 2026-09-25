# 🔍 THE BROKEN CLIMB — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦ ⑨ ⑪ ⑫).
> Plan: `THE_BROKEN_CLIMB_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md` (üretimde açılır)

```
FİLM      THE BROKEN CLIMB · 7 × 8,0 = 56,0 sn · KAPAK KARTI YOK · LOGO YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    56,0 sn / yok
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok
REJİM     S0–S4 B (2 sa) · S5–S6 ⭐ A (10 dk) — iki rejim, üçüncü yok
IŞIK      TEK GÜN: 07:30 → 09:30 → 11:30 → 13:30 → 15:30 → 17:30 → 17:40 → 17:50 · 38° kuzey · ekinoks · güneş
          96°/8° → 261°/12° · kamera KUZEYE bakar, güneş hep arkada · final güneşli, 12° [DERS 45]
TAKVİM    yok — tek gün; mevsim taşıyıcısı yalnız gölge uzunluğu ve YÖNÜ (sol → yukarı → sağ)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① SARI VAGON HATTIN ÜST ÜÇTE BİRİNDE, YENİ DUVARIN ÜSTÜNDEN GEÇMİŞ — 54,0'ta vagon t ≈ 0,85–0,95 (x ≈ %62–66 ·
    y ≈ %69–72), üst istasyona girmek üzere; 56,0'da kanopinin altında (x %68 · y %73–74), gökyüzüne karşı
  ② HAT KESİNTİSİZ VE BOŞ — yuvadan (%21 · %35) üst istasyona tek çapraz çizgi; yarık kısmında (x %46–60) pale-grey
    duvar (y %55–66) ve üstünde parlak yeni ray; yuva BOŞ
  ③ MAVİ VAGON TAKOZDA MEYDANDA — x %29 · y %32–36, istasyonun batısında, RAYDA DEĞİL; tomruk istifi yanında

⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 54,0'ta vagon HÂLÂ HAREKETTE olmalı: 54,0 ve 55,0 karelerinde vagon farklı yerde (≈ 95 px/sn); 55,0–56,0
   arasında durur. Duran vagon 54,0'ta = S6 atılır (rejim A'nın 6.–7. dakikası).
⛔ 56,0'da film vagon DURURKEN kesilir; sonrasında kart, logo, fade, müzik YOK.
⛔ Vagon tırmanırken TEK RİJİT GÖVDE: boyu 59 → 26 px'e uzaklıkla KÜÇÜLÜR, oranı bozulmaz; iki vagon çizilirse ⑫.
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0 · KAMERA_ISTASYONU §3)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | %50 | ±0,5 puan · SEKİZ KAREDE DE (tilt 0 kanıtı) |
| ⭐ şapel çan kulesi (x · y taban/tepe) | %45 · %76–80 | ±0,5 puan · SEKİZ KAREDE DE (nirengi ①) |
| ⭐ kret sağ kenarı (y) | %74,7 | ±1 puan · SEKİZ KAREDE DE (nirengi ②); eyer %73,3 |
| ⭐ çeşme havuzu (x · y) | %22 · %29–30 | ±0,5 puan · SEKİZ KAREDE DE (nirengi ③) |
| ⭐ istasyon binası (x · çatı y) | %15–25 · %40 | ±0,5 puan · SEKİZ KAREDE DE ("aynı yer" nesnesi · KESİR 93 px ±10) |
| ⭐ yuva / hat başı (x · y) | %21,4 · %34,8 | ±1 puan · SEKİZ KAREDE DE |
| ⭐ üst istasyon (x · y ray/kanopi) | %66–71 · %72,8 / %75–76 | ±1 puan · SEKİZ KAREDE DE |
| hat çizgisi (231, 1253) → (735, 522) px | tek doğru, 887 px | ±3 px · G0–G7 (yarık kısmı G0 sarkık, G1–G2 boş, G3 duvar, G4→ ray) |
| yarık başı / sonu (x · y) | %45,9 · %54,7 / %59,5 · %65,8 | ±1 puan |
| ⭐ duvar (G3→) yüz x · taban y (t ⅓/½/⅔) | %46–60 · %48,6 / %55,6 / %61,1 | ±1 puan · G3–G7 SABİT · panel sayısı 8 (32 px/panel) |
| kazık başlıkları (yalnız G2 görünür) | 12 · ≈ 30 px aralık | G3'ten sonra duvarın altında |
| sol evler / sağ evler | %15–38 · %47–59 / %66–74 · %56–71 | ±1 puan · SEKİZ KAREDE DE |
| incir (yalnız G0) taban/tepe | %41 · %55–59 | G1'de YOK (tomruk istasyon yanında %24 · %32–33, G1–G7) |
| heyelan yelpazesi (yalnız G0) | x %33–58 · y %35–39 + yarığa kadar | G1'den sonra meydan temiz |
| vinç şasi (G0–G5 · x · y) | %39–41 · %31–37 | ±2 puan · G6–G7'de vinç YOK, dört ayak izi VAR |
| kamyon sırası (G0–G4 · x) | %54–71 | G5'ten sonra YOK; G4'te sarı vagonlu lowbed + 2 boş flatbed |
| ⭐ mavi vagon (G0–G4 yuvada · G5→ takozda) | %21 · %35–38 → %29 · %32–36 | G5–G7 takozda SABİT |
| ⭐ sarı vagon G4 / G5 / G6 / G7 | lowbed %63 · %31–37 / yuva %21 · %35–38 / %29 · %41 / %68 · %73–74 | ±1 puan |
| gök bandı | %75–100 | bulut streak (B) · drift (A) · güneş diski HİÇBİR karede |

## 3. ⭐ YAPININ İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  yarık: heyelan yüzü + havada sarkık burkuk ray · yeşil teraslar + incir · yelpaze istasyon yanına kadar · mavi vagon
    yuvada (burnu molozda) · vinç (mini ekskavatör sapanda) · loader · 3 damper · 2 lowbed (delgi · boş) · 2 flatbed
    (8 panel A-frame · 4 ray paneli) · panel 0 · başlık 0 · sarı vagon 0
G1  yarık: gri kaya bankı + 2 çıplak ray ucu · teras YOK · tomruk istasyon yanında · mini ekskavatör BANKTA · vinç
    (burkuk ray sapanda) · loader + 3 damper hâlâ · 2 lowbed · 2 flatbed
G2  12 KAZIK BAŞLIĞI çizgide · delgi doğu uçta · mini ekskavatör lowbed'de · damper + loader YOK · vinç (1. panel
    sapanda, dik) · 2 flatbed (8 panel · 4 ray)
G3  8 PANEL DUVAR (üstü düz bank) · ray uçları hâlâ çıplak · delgi + mini ekskavatör lowbed'lerde · vinç (1. ray
    paneli sapanda, yatay) · flatbed (3 ray paneli) · A-frame boş
G4  DUVAR + 4 RAY PANELİ → HAT KESİNTİSİZ · lowbed'ler (delgi · mini) YOK · SARI VAGON lowbed'de · 2 boş flatbed ·
    vinç (spreader mavi vagonun üstünde, 4 sapan mapalarda)
G5  SARI VAGON YUVADA (sapanlar üstünde) · MAVİ VAGON TAKOZDA · kamyon YOK · vinç tek makine
G6  sarı vagon yuva+1 (x %29 · y %41) · halat gergin · vinç YOK · dört ayak izi · üç ekip sırtı dönük
G7  SARI VAGON ÜST İSTASYONDA · hat boş · halat gevşek · mavi takozda · yuva boş · üç ekip yukarı bakıyor
⛔ SAYIM: hat 1 · istasyon 2 · vagon rayda (1·1·1·1·1·1·1·1 — G0–G4 mavi, G5–G7 sarı) · vagon takozda (0·0·0·0·0·1·1·1)
   · panel (0·0·0·8·8·8·8·8) · ray paneli (0·0·0·0·4·4·4·4) · başlık (0·0·12·gizli…) · vinç (1·1·1·1·1·1·0·0)
⛔ Duvar G3'ten sonra ARTMAZ; hat G4'ten sonra DEĞİŞMEZ; vagon G5→G6→G7 yalnız yer değiştirir.
```

## 4. ⭐ YÜK YOLU KAPISI — S0 · S1 · S2 · S3 · S4 [FIZIK_VE_AGIRLIK §4 · DERS 57 · beş soru ②③]

```
S0  mini ekskavatör: sapan → teras (DÜŞEY iner) · tomruk + burkuk ray: yarık → sapan → meydan · kanca hep yüklü
S1  mini ekskavatör: bank → sapan → lowbed · delgi: lowbed → sapan → bank · kazık: delgi ile bank tabanına
S2  ⭐ PANEL ×8: A-frame → 2 sapan (DİK, döndürülmez) → kazık başlığı · her panel aynı boy (104 px @ t ½) · batıdan doğuya
S3  RAY PANELİ ×4: flatbed → 4 sapan (YATAY) → duvar bankı · uç uca · uçlar eski raya cıvatalı
S4  ⭐ VAGON ×2: mavi yuva → spreader (DÜŞEY kalkar, sola, iner) → takoz · sarı lowbed → spreader → yuva (tekerler rayda)
S5  halat: tambur → hat ortası → vagon başı (çizgi görünmeyebilir; kanıt = vagon bir boy kımıldar)
⛔ DERS 57 TESTİ (pilot c · S4): vagon havada (i) boy sabit mi (ii) yatay mı (iii) hedefte KOPYALANIYOR mu (iki sarı
   vagon / mavi rayda kalıyor mu) (iv) yuvaya inince istasyon kıpırdıyor mu. Dördünden biri düşerse sahip kararı.
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı (kamyon / A-frame / lowbed) bir önceki karede görünür [DERS 48].
⛔ 35° yamaçta hiçbir lastikli araç YOK: loader ve damperler yalnız MEYDANDA; yamaçtaki her makine vinçle geldi.
```

## 5. ⭐ GÖLGE KAPISI — üç yönlü süpürme [ZAMAN_VE_ISIK §2 · HAVA_VE_ATMOSFER]

```
G0–G1  gölgeler SOLA (güneş sağda-arkada, 96°→117°) · uzun → kısa · otel gölgesi meydanın yakın kenarında (G0)
G2–G3  gölgeler YUKARI, en kısa (150°→196°, el 48°→51°) · yamaç düz aydınlık
G4–G7  gölgeler SAĞA (234°→261°) · kısa → uzun · evlerin doğu yüzleri gölgede · otel gölgesi meydanın doğu yarısında
⛔ Güneş diski HİÇBİR karede yok (bearing 0°, güneş 96°–261°: kadraj bandı 333°–27°'nin tamamen dışında) [DERS 39]
⛔ Döngü kesmesi (G7 → G0): gölge SAĞDAN SOLA atlar, uzunluk aynı (el 12° ↔ 8°) — okunur, beklenir
⛔ Final (G7) AYDINLIK: güneş 12°, vagonun batı yüzü turuncu [DERS 45]
```

## 6. ⭐ TEK HAT · TEK VAGON RAYDA · İKİ İSTASYON KAPISI [DERS 55]

```
Korpus riski: "funicular" → İKİ VAGON + geçiş yeri · "railway" → ikinci hat · "cable car" → teleferik kabini havada
① sayım cümlesi her karede ve her I2V'de POZİTİF ("one funicular with one straight track and two stations")
② kompozisyon: hat tek çapraz çizgi %21–68 × %35–73; geçiş yerine yer yok
③ araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç hat / kaç vagon / kaç istasyon
⛔ G0–G3 mavi vagon yuvada TEK; üst istasyonda vagon YOK → model oraya vagon çizerse ⑧ APPEARED
⛔ G6–G7 rayda TEK vagon (sarı); mavi takozda — mavi raya dönerse ya da iki sarı olursa ⑤ DEVAMLILIK
⛔ Panel 8 · ray paneli 4 · başlık 12 — fazlası ⑧
```

## 7. ⭐ REJİM A KAPISI — S5 · S6 [SANTIYE_HAREKETI §1]

```
· "Ten minutes pass" · "time-lapsed at the same rate" · figür bulanık ama okunur, sırtı kameraya
· S5: hareket eden = vinç (bom iner, sağa çıkar) · halat (iner) · vagon (bir boy) — üçü SIRALI; G6 vinçsiz
· S6: hareket eden TEK ŞEY vagon (+ halat); duvar · evler · kret · istasyon · mavi vagon ± 2 px
· vagon TEK RİJİT GÖVDE: 59 px → 26 px uzaklıkla küçülür; ≈ 3,0–4,5 sn arasında yeni rayda (duvar üstü); 6,5–7,5
  kanopiye girer; 7,5–8,0 durur
· ışık 17:30 → 17:50: 16° → 12°, gölgeler sağa, biraz uzar; vagonun batı yüzü turuncu
· 40,0 kesmesi (B → A): S4'ün son 0,5 sn'sinde iz çözülmesi kabul, planlanmaz
⛔ Vagon rayı bırakıp "uçarsa", hat dışına kayarsa ya da 8 sn'nin 2 sn'sinde tepeye varırsa (rejim yanlış) klip atılır
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–56,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı katman yok (telefon hoparlörü) · konuşma/telsiz yok
· 2,0 civarı testere + incir düşüşü · 8,0–16,0 on iki darbeli delgi · 16,0–24,0 sekiz panel oturma vuruşu ·
  36,0 civarı vagon raya oturma · 40,0–41,0 yalnız martı + rüzgâr · 43,0 vinç uzaklaşır · 47,0 "çınn" ·
  48,0–55,0 halat uğultusu + tıkırtı · 55,3 tek zil · 55,3–56,0 rüzgâr + martı
· Görüntü 900×/75×, ses 1×: kare senkron aranmaz; vuruşlar olaya ±0,5 sn
```

## 9. Zaman ve ışık

```
G0 07:30 96°/8° · G1 09:30 117°/30° · G2 11:30 150°/48° · G3 13:30 196°/51° · G4 15:30 234°/37° · G5 17:30 257°/16° ·
G6 17:40 259°/14° · G7 17:50 261°/12°   (38°K · ekinoks · saat = güneş saati + 50 dk · TÜRETİLMİŞ model)
· gölge YÖNÜ G0–G1 sola, G2–G3 yukarı, G4–G7 sağa — üç yön tek yüzeyde; döngü kesmesinde sağ → sol OKUNUR
· S5 · S6 gölge kıpırdamaz (10 dk); ışık üç karede ayrı yazılı (16° · 14° · 12°)
· bulut: B kliplerinde streak, A kliplerinde drift — I2V'lerde yazılı
· 40,0 kesmesi (S4 → S5) rejim dikişi; 48,0 kesmesi (S5 → S6) ölçek dikişi (bir boy → 120 m)
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      7 × 8,0 — sahip kuralı, beyanlı
⑧ MADE          panel ×8 · ray paneli ×4 · vagon ×2 — on dört uzun rijit kaldırma (DERS 57); pilot (c) S4 önce
② GEOMETRİ      35° eğim + çapraz hat: model hattı "kıvırabilir" ya da eğimi 20°'ye düşürebilir; hat çizgisi 887 px
                köşegen SEKİZ karede ölçülür (±3 px)
⑤ DEVAMLILIK    G4→G5 iki vagon yer değiştirir (mavi yuva → takoz, sarı lowbed → yuva); G5→G6 vinç gider; G0→G1
                teraslar + incir + yelpaze gider (kasıtlı, S0 içinde)
③ ZAMAN         tek gün, gölge üç yönlü — EMPTY LOCK'ta "gök yok" sorusu vardı; burada gök VAR (%75–100), bulut
                taşıyıcısı da var; risk düşük ama ölçülmedi
⑦ İŞ            S0–S4 kalabalık (5–7 hareket eden, kapı INFO) — kompaund boşalırken sıra fizikle bağlı, kasıtlı [C1-d]
⑫ KATILIK       üst istasyondaki vagon 26 px boy — küçük gövde "erir" mi; kanıt yer değişimi, boyut değil
④ TESLİM        sesli-müziksiz teslim ikinci kez: P8-e ölçümü tekrar
①               meydan y %0–29 boş kaldırım — alt UI bandı; kanıt taşımaz
```
