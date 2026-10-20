# 📊 TABLO — QA'NIN TEK SAYACI

> ⛔ Her hücre bir ham dosyaya bağlıdır (`QA/HAM/<FILM>/…`). Hamı olmayan puan yazılmaz;
> hamı olan koşu satırsız kalmaz [QA_KAYIT §0]. `bash araclar/sayac.sh` TOPLAM FİLM'i ve
> HAM ↔ TABLO uyumunu karşılaştırır.
> Eski 12 mercekli sonuçlar: `ARSIV_12_MERCEK/00_ARSIV.md §4` (temizlenmiş puanlar) — bu
> tabloya TAŞINMAZ, ölçekler farklı.

---

## SAYIM

```
TOPLAM FİLM          61     (dikey_shorts + yatay_*_dk_filmler klasörleri · 12 dk dahil)
BEŞ MERCEKLE ÖLÇÜLEN 4 (SKY STATION B1 · POOL ROOM · RAIN TOWER · HIDDEN LOFT)
ARŞİVDE ÖLÇÜLEN      37     (ARSIV_12_MERCEK/HAM_RAPORLAR klasörleri · 12 mercek)
```

## FİLM × MERCEK

Hücre: mercek puanı (TAM) · `EKS` eksik · `YG` yanlış girdi · `SZ` sızıntı · `TT` tutarsız ·
`—` koşulmadı. Hüküm sütunu yalnız olumsuz hükümleri yazar. Film puanı = TAM merceklerin
ortalaması · N.

| film | biçim | dosya | ❶ | ❷ | ❸ | ❹ | ❺ | film puanı (N) | olumsuz hüküm | koşu tarihi |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|:-:|
| THE SKY STATION | 16:9 | 1x | 2,8 (B1) | 5,2 (B1) | 3,6 (B1) | 3,2 (B1) | 6,0 (B1) | 4,2 (N=5) | MELTING · STOPS | 15.10.2026 |
| THE POOL ROOM | 9:16 | 2x | YG · SZ | EKS | SZ | YG | 10,0 | 10,0 (N=1) ⚠️ şişik — ajan ölçümü: kart · düşen S4 · çözünürlük | MELTING (❶, bağlayıcı değil) | 16.10.2026 |
| THE RAIN TOWER | 9:16 | 2x | YG · SZ | YG | EKS | 5,5 | 9,0 | 7,3 (N=2) ⚠️ bağlayıcı değil — kör üçlü geçersiz; ajan ölçümü: avlu çukuru (5/5 mercek) · ikiz platform · başlık · kart sesi | MELTING (❶) · INTRUDERS (❹) | 17.10.2026 |
| THE HIDDEN LOFT | 9:16 | 2x | 5,4 | EKS | EKS · ŞİŞİK | 5,4 | EKS · ŞİŞİK | 5,4 (N=2) ⚠️ bağlayıcı değil — beş mercek boş blokla; ❸ ❺ 32 klip uydurdu (DERS 105); ajan ölçümü: kanepe dönüşü · parke yönü · kapı balkonu · S2 müziği · kart sesi | MELTING (❶) · WRONG DIRECTION (❷, bağlayıcı değil) · APPEARING (❹) | 19.10.2026 |

```
⭐ "dosya" sütunu: 2x · 1x · 1x+2x (❸ ❹ master, ❶ ❷ ❺ yayın) [QA_OLCUM_ZEMINI §3]
⛔ Öldürücü hüküm (❶ SEPARATE IMAGES · ❸ REBUILT · ❹ DIFFERENT) varsa film puanının yanına
   "⛔ DÜŞTÜ" yazılır.
```
