# 🎞️ THE_SKY_CANAL — SAHNE SIRALAMASI (aşama merdiveninin türetildiği yer)

> **Girdi:** `02_KONSEPT_VE_RISK.md` §2a inşa sırası · onaylı 20 satır (TUR 1).
> **Çıktı:** 20 satır → PLAN §AŞAMA MERDİVENİ · monoton büyüme · rejim toplamı · bölüm sınırı · dikiş denetimi.

---

## 1. 🧱 İNŞA SIRASI → 20 SATIR [02 §2a]

| gerçek iş adımı | sahip senaryosu | depo S | not |
|---|:-:|:-:|---|
| sol açıklık parçası | S01 | S0 | ⭐ kanca: parça ilk karede asılı, tekne solda bekler |
| sağ açıklık parçası | S02 | S1 | kısa yol, sağ pedden |
| merkez açıklık parçası | S03 | S2 | ⭐ dimdik yukarı · kıyılar birleşir (00:24) |
| enine kirişler | S04 | S3 | ızgara · B |
| taban levhaları | S05 | S4 | nehir aralıkları kapanır |
| uzak duvar | S06 | S5 | derinlik |
| yakın duvar | S07 | S6 | U oluk |
| kıyı bağlantıları | S08 | S7 | kapaklar kapalı |
| iç kaplama | S09 | S8 | ⭐ renk dönüşümü (01:04) · KURU · B |
| bakım yolu | S10 | S9 | + uç basamakları |
| korkuluk | S11 | S10 | bölüm sınırı G10 |
| dış boya | S12 | S11 | kömür grisi · B |
| söküm | S13 | S12 | iki vinç çıkar |
| ilk su | S14 | S13 | ⭐ tek dolumun 1/3'ü |
| su karşıya | S15 | S14 | tek dolumun 2/3'ü |
| seviye | S16 | S15 | tek dolumun 3/3'ü · kıyılarla eşit |
| kapaklar | S17 | S16 | geçiş açılır |
| tekne girer | S18 | S17 | ⭐ tek geçişin 1/3'ü · Y |
| tekne nehrin üstünde | S19 | S18 | ⭐ DORUK · Y |
| varış | S20 | S19 | tutuş · Y |

## 2. 🗺️ SIRALAMA — monoton büyüme

```
S0  sol parça oturur          → + sol açıklık
S1  sağ parça oturur          → + sağ açıklık
S2  merkez parça yükselir     → + merkez açıklık (kıyılar birleşik)   − vadi tabanındaki kalaslar yığına
S3  enine kirişler            → + ızgara                               − kalaslar (küçük kamyon)
S4  taban                     → + kuru taban
S5  uzak duvar                → + uzak duvar
S6  yakın duvar               → + yakın duvar (U oluk)
S7  uçlar                     → + kıyı bağlantıları (kapaklar kapalı)
S8  iç kaplama                → + açık mavi (kuru)
S9  bakım yolu                → + bakım yolu + basamaklar
S10 korkuluk                  → + korkuluk
S11 dış boya                  → + kömür grisi
S12 söküm                     → (yapı aynı) · − iki vinç, paletler, kamyonlar
S13 ilk su                    → + sığ su (sol yarı)
S14 su karşıya                → + sığ su (bütün boy)
S15 seviye                    → + dolu oluk (dörtte üç)
S16 kapaklar                  → + açık geçiş
S17 tekne girer               → (yapı aynı) · tekne havuzdan köprüye
S18 tekne merkezde            → (yapı aynı) · tekne merkez açıklıkta
S19 tutuş                     → (yapı aynı) · tekne sağ kapakta
⛔ Hiçbir satır öncekinden az YAPI göstermez ✅ (S12'de giden yalnız şantiye ekipmanı — SÖKÜM; S17–S19 yapıyı KULLANIR)
```

## 3. 📐 DİKİŞ DENETİMİ — mekanik, göz kararı değil [§2.7 · DERS 52]

| dikiş | iki yaka aynı kare | değişen tek şey | kesmede atlamayan |
|---|---|---|---|
| G1 … G3 | ✅ | açıklık sayısı (1 · 2 · 3) | çam, ayaklar, nehir, tekne havuzda |
| G4 … G8 | ✅ | sırasıyla ızgara · taban · uzak duvar · yakın duvar · uçlar | köprü hattı 538–1398, vinçler |
| G9 | ✅ | iç mavi | aynı |
| G10 | ✅ ⭐ bölüm sınırı | bakım yolu var, korkuluk yok | gölge +9°, yaz, iki vinçte korkuluk demeti |
| G11 … G13 | ✅ | korkuluk · kömür grisi · saha boş | köprü hattı |
| G14 · G15 | ✅ ⭐ TEK DOLUM | su cephesi (sol ayak · sağ kapak) | kot (onda bir), saat, ışık |
| G16 · G17 | ✅ | seviye dörtte üç · kapaklar yukarıda | su seviyesi |
| G18 · G19 | ✅ ⭐ TEK GEÇİŞ | tekne yeri (620–796 · 974–1121) | su, kapaklar, ışık (Y'de gölge sabit) |
| G20 | usta kare | tekne sağ kapakta | — |

## 4. ☀️ IŞIK GÜNÜ TOPLAMI — rejim sütunu TOPLANIR

```
A  S0 · S1 · S2 · S4 · S5 · S6 · S7 · S9 · S10 · S12 · S13 · S14 · S15 · S16      14 × 10 dk  =  140 dk
B  S3 · S8 · S11                                                                3 × 2 sa   =  6 sa
Y  S17 · S18 · S19                                                              3 × 1 dk   =  3 dk
Σ  = 8 sa 23 dk ≤ 14 ✓  ·  08:20 → 16:43
```

## 5. ⭐ ÜÇ ZORUNLU SATIR — PLAN'a taşındı

```
KANIT   çam (x 1475–1547 · 72 px) — sağ yamaçta kaya çıkıntısında, iğne yapraklı, değişmez
LOOP    G20 ↔ G0: aynı çam · aynı ayaklar · tekne SOLDA havuzda (boşluk açık) ↔ SAĞDA köprünün ucunda (köprü dolu) · serin
        sabah ↔ altın saat
SÖKÜM   kalas kamyonu (S0) · kalaslar (S1 istif · S2 yığın · S3 küçük kamyon) · kamyonlar (S3–S11, her yük boşalınca gider) ·
        İKİ VİNÇ + paletler + kamyonlar (S12) · servis aracı (S16 · S19)
```

## 6. 🔁 ONAYLI HİKÂYEYLE FARK

Bütün farklar `00_HIKAYE_ONAYI.md` SAPMA ①–⑱'de. Sıralamayı değiştiren yok: onaylı 20 satır birebir (sahibin S01–S20'si =
depo S0–S19). Senaryonun kendi metninden farkı yalnız yöntemde: merkez parça yukarıdan indirilmez, aşağıdan kaldırılır
(TUR 1 ①, tek vinç — SAPMA ⑤); tekne klipleri yavaş zamanda (TUR 1 ③); takvim ağaçlardan okunur (SAPMA ⑦).
