# 🎞️ THE_SUNKEN_STAGE — SAHNE SIRALAMASI (aşama merdiveninin türetildiği yer)

> **Girdi:** `02_KONSEPT_VE_RISK.md` §2a iş sırası · onaylı 20 satır (TUR 1).
> **Çıktı:** 20 satır → PLAN §AŞAMA MERDİVENİ · monoton büyüme · rejim toplamı · bölüm sınırı · dikiş denetimi.

---

## 1. 🧱 İŞ SIRASI → 20 SATIR [02 §2a]

| gerçek iş adımı | sahip senaryosu | depo S | not |
|---|:-:|:-:|---|
| tahliye 1 (üst yaylar) | S01 | S0 | ⭐ kanca: su ilk karede alçalıyor, iki yay dışarıda |
| tahliye 2 (sıralar + merdivenler) | S02 | S1 | sol hasar görünür · sahnede ince su |
| tahliye 3 (son su) | S03 | S2 | ⭐ sahne çamurdan çıkar · bütün tiyatro (00:24) |
| çamurun alınması | S04 | S3 | yükleyiciler + damperliler + kürek ekipleri |
| basınçlı yıkama | S05 | S4 | ⭐ kirli → açık taş (00:32–00:40) · B · sonunda vinç gelir |
| merdiven onarımı | S06 | S5 | taş bloklar vinçle |
| ahşap oturma tahtaları | S07 | S6 | 12 sıra · B |
| sahne iskeleti | S08 | S7 | çelik ızgara |
| sahne panelleri | S09 | S8 | sıcak ahşap sahne |
| kabuk kaburgaları | S10 | S9 | yedi kaburga · bölüm sınırı G10 |
| kabuk kaplaması | S11 | S10 | ⭐ bakır + ahşap · en gösterişli değişim · B |
| teknik kuleler | S12 | S11 | + sönük basamak lambaları |
| giriş yolları | S13 | S12 | + sönük yol lambaları |
| saha temizliği | S14 | S13 | vinç + pompalar + tanklar + paletler çıkar |
| sandalyeler + topluluk | S15 | S14 | sıralar boş |
| ışıklar | S16 | S15 | gün batımı · üç grup sırayla |
| ilk seyirci | S17 | S16 | mavi saat · ≈⅓ |
| dolan sıralar | S18 | S17 | mavi saat · çoğu |
| ana ışık + ilk müzik | S19 | S18 | ⭐ gerçek zaman (G) |
| alkış + tutuş | S20 | S19 | ⭐ gerçek zaman (G) · final |

## 2. 🗺️ SIRALAMA — monoton büyüme

```
S0  su iner (11 → 7)            → + dört teras açığa çıkar                 − su (pompalar → tanklar)
S1  su iner (7 → sahnenin üstü)  → + alt teraslar · üç merdiven · (hasar görünür)
S2  son su                       → + sahne platformu (çamurlu)              − son su
S3  çamur                        → (yapı aynı, ortaya çıkar)                 − çamur yığınları (kamyonlarla)
S4  yıkama                       → (yapı aynı) · koyu → açık taş             − silt (yıkama suyuyla) · + vinç gelir
S5  onarım                       → + sol merdiven tam
S6  tahtalar                     → + 12 sıra ahşap oturma tahtası
S7  iskelet                      → + çelik döşeme ızgarası
S8  paneller                     → + ahşap sahne
S9  kaburgalar                   → + yedi kavisli kaburga
S10 kaplama                      → + bakır/ahşap kabuk (armatürler sönük)
S11 kuleler                      → + iki kule · + basamak lambaları (sönük)
S12 yollar                       → + iki taş yol · + yol lambaları (sönük)
S13 söküm                        → (yapı aynı) · − vinç, pompalar, tanklar, paletler, kalaslar
S14 sandalyeler                  → (yapı aynı) · + topluluk sahnede
S15 ışıklar                      → (yapı aynı) · + lambalar YANIK (üç grup)
S16 ilk seyirci                  → (yapı aynı) · + ≈⅓ dolu
S17 dolan sıralar                → (yapı aynı) · + çoğu dolu
S18 ana ışık                     → (yapı aynı) · + ana ışık + müzik
S19 alkış                        → (yapı aynı) · + alkış · TUTUŞ
⛔ Hiçbir satır öncekinden az YAPI göstermez ✅ (S0–S4'te giden su, çamur ve kir — YAPI DEĞİL, yapının üstündeki şey; S13'te giden
   yalnız şantiye ekipmanı — SÖKÜM; S14–S19 yapıyı KULLANIR)
```

## 3. 📐 DİKİŞ DENETİMİ — mekanik, göz kararı değil [§2.7 · DERS 52]

| dikiş | iki yaka aynı kare | değişen tek şey | kesmede atlamayan |
|---|---|---|---|
| G1 · G2 | ✅ ⭐ TEK TAHLİYE | su çizgisi (11 → 7 → 3. terasın dibi) | pompalar, hortumlar, kaya, gölge −56°/−54° |
| G3 · G4 | ✅ | çamur var / yok | taş silt filmli, kirli |
| G5 | ✅ | taş temiz + ıslak · vinç geldi | sol hasar duruyor |
| G6 … G9 | ✅ | sırasıyla merdiven · tahtalar · ızgara · ahşap sahne | vinç 578 · pompalar 232 |
| G10 | ✅ ⭐ bölüm sınırı | yedi çıplak kaburga | gölge +29°, öğleden sonra, vinçte panel sandığı |
| G11 … G13 | ✅ | kabuk · kuleler · yollar | vinç (G13'e kadar) |
| G14 | ✅ | saha boş | altın saat, gölge +60° |
| G15 · G16 | ✅ ⭐ TEK AKŞAM | lambalar sönük → yanık | topluluk sahnede, sıralar boş |
| G17 · G18 | ✅ | seyirci ⅓ → çoğu | lambalar yanık, ana ışık sönük, oturan yerinde |
| G19 | ✅ ⭐ rejim A → G (144,0) | ana ışık tam | seyirci aynı yerde |
| G20 | usta kare | alkış, ön sırada birkaç kişi ayakta | — |

## 4. ☀️ IŞIK GÜNÜ TOPLAMI — rejim sütunu TOPLANIR

```
A  S0 · S1 · S2 · S3 · S5 · S7 · S8 · S9 · S11 · S12 · S13 · S14 · S15 · S16 · S17     15 × 10 dk  =  150 dk
B  S4 · S6 · S10                                                                     3 × 2 sa   =  6 sa
G  S18 · S19                                                                         2 × 8 sn   =  16 sn
Σ  = 8 sa 30 dk 16 sn ≤ 14 ✓  ·  09:20 → 17:50:16
```

## 5. ⭐ ÜÇ ZORUNLU SATIR — PLAN'a taşındı

```
KANIT   yarık kaya (x 286–384 · 98 px) — sol üstte yamaçta, tepeden dibe koyu çatlaklı, değişmez
LOOP    G20 ↔ G0: aynı kaya · aynı çamlar · aynı 12 yay · G0 kahverengi su + iki yay ↔ G20 dolu, ışıklı sıralar · sabah ↔ mavi saat
SÖKÜM   hortum kamyonu (S0–S1) · kalas yolları (S2 → S3 istif → S13) · yükleyiciler + damperliler (S3) · tanker (S4) · kamyonlar
        (S4–S12, her yük boşalınca gider) · VİNÇ + POMPALAR + TANKLAR + paletler (S13) · minibüs (S15)
```

## 6. 🔁 ONAYLI HİKÂYEYLE FARK

Bütün farklar `00_HIKAYE_ONAYI.md` SAPMA ①–⑯'da. Sıralamayı değiştiren yok: onaylı 20 satır birebir (sahibin S01–S20'si =
depo S0–S19). Senaryonun kendi metninden farkı yalnız yöntemde: vinç S10'dan önce gelir (S4 sonu — SAPMA ⑪); son iki klip
gerçek zamanda (SAPMA ⑦); kamera 35° yerine 27° ve eksen üstünde (SAPMA ③ · ④); lambalar önce sönük takılır (SAPMA ⑬).
