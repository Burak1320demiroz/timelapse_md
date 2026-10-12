# 🎞️ THE_HIDDEN_FALLS — SAHNE SIRALAMASI (aşama merdiveninin türetildiği yer)

> **Girdi:** `02_KONSEPT_VE_RISK.md` §2a inşa sırası · sahip senaryosunun 15 sahnesi.
> **Çıktı:** 15 satır → PLAN §AŞAMA MERDİVENİ · monoton büyüme · rejim toplamı · bölüm sınırı · dikiş denetimi.

---

## 1. 🧱 İNŞA SIRASI → 15 SATIR [02 §2a · INSAAT_YONTEMI §2-§3]

| gerçek iş adımı | senaryo sahnesi | depo S | not |
|---|:-:|:-:|---|
| eski tesisin sökümü | 1 | S0 | paslı platform vinçle kamyona |
| susuzlaştırma | 2 | S1 | iki pompa · su +3 → taban |
| zemin + yükseltilmiş temel (+ köprü ayağı) | 3 | S2 | ayak aynı beton işinde (SAPMA ⑨) |
| çelik iskelet | 4 | S3 | ⭐ 00:32'de ilk büyük sonuç |
| köprü | 5 | S4 | iki açıklık |
| teras döşemesi (+ çatı) | 6 | S5 | çatı ve dudak bu klipte kapanır |
| cephe camı | 7 | S6 | önce salon (iç çekim camlı salonu ister) |
| iç döşeme (salon) | 8 | S7 🪟 | ∥ S8 (SAPMA ④) |
| su devresi (kanal + boru + pompa evi) | 9 | S8 | vinç burada gider |
| peyzaj | 10 | S9 | dolumdan ÖNCE — kuru basamağa dikilir |
| kontrollü dolum | 11 | S10 | +7'de durur |
| devreye alma (şelale) | 12 | S11 | gerçek zaman |
| aydınlatma | 13 | S12 | tek karede |
| (iç mekân, sonuç) | 14 | S13 🪟 | ∥ S12'nin son 8 sn |
| (sonuç) | 15 | S14 | final tutuşu |

## 2. 🗺️ SIRALAMA — monoton büyüme

```
S0  platform gider            → yapı 0        (söküm: geçici/eski tesis — büyüme kuralı dışı)
S1  su gider                  → yapı 0        (su iki yönlü [P16-c])
S2  temel + ayak              → temel %100
S3  iskelet                   → + iskelet %100
S4  köprü                     → + köprü 2/2
S5  teras + çatı              → + teras, çatı, dudak
S6  cam                       → + cam 15/15
S7  🪟 salon                   → (iç) + mobilya — dış yapı DEĞİŞMEZ
S8  kanal + boru              → + kanal, boru, pompa evi · − vinç (geçici)
S9  bahçe                     → + bahçe
S10 dolum                     → + su +7 (platform kuru)
S11 şelale                    → + akan su
S12 ışık                      → + ışık · + üç kişi
S13 🪟 salon                   → (iç) — dış yapı DEĞİŞMEZ
S14 final                     → (değişmez) · tutuş
⛔ Hiçbir satır öncekinden az YAPI göstermez ✅
```

## 3. 📐 DİKİŞ DENETİMİ — mekanik, göz kararı değil [§2.7 · DERS 52]

| dikiş | iki yaka aynı kare | değişen tek şey | kesmede atlamayan |
|---|---|---|---|
| G1 … G6 | ✅ | sırasıyla platform · su · temel · iskelet · köprü · teras | ışık, gölge, sütun |
| S6 → S7 → S8 | ana G8 iki yakada | istasyon (ana → salon → ana) | dış yapı, saat (13:10) |
| G9 | ✅ ⭐ bölüm sınırı | — | kanal, vinç yok, kuru havza |
| G10 … G12 | ✅ | bahçe · su · şelale | gölge yönü (+76° · +96°) |
| S12 → S13 → S14 | ana G14 iki yakada | istasyon | ışıklar yanık, mavi saat |
| G15 | usta kare | üç kişi 5 m | — |

## 4. ☀️ IŞIK GÜNÜ TOPLAMI — rejim sütunu TOPLANIR

```
A  S0 · S3 · S4 · S6 · S8            5 × 10 dk  =  50 dk
B  S1 · S2 · S5 · S9 · S10 · S12     6 × 2 sa   =  12 sa
G  S11 · S14                         2 × 8 sn   =  16 sn
∥  S7 (∥ S8) · S13 (∥ S12 sonu)      toplama girmez
Σ  ≈ 12 sa 50 dk ≤ 14 ✓  ·  06:30 → 19:20
```

## 5. ⭐ ÜÇ ZORUNLU SATIR — PLAN'a taşındı

```
KANIT   kireçtaşı sütun (x 922–1050 · 128 px) — iki kamerada ortak
LOOP    G15 ↔ G0: aynı sütun · kirli su → turkuaz · platform → ışıklı yapı · sabah ↔ mavi saat
SÖKÜM   platform · pompa · kalıp · istifler · sandıklar · VİNÇ (S8) · paletler · hortumlar · son aletler
```

## 6. 🔁 ONAYLI HİKÂYEYLE FARK

Bütün farklar `00_HIKAYE_ONAYI.md` SAPMA ①–⑭'te. Sıralamayı değiştiren yalnız ikisi: S7'nin saati (∥ S8, SAPMA ④) ve
bölüm sınırının G9'a kayması (SAPMA ⑩). Sahne sırası senaryoyla birebir.
