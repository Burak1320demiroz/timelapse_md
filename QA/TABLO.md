# 📊 TABLO — QA'NIN TEK SAYACI

> ⛔ Her hücre bir ham dosyaya bağlıdır (`QA/HAM/<FILM>/…`). Hamı olmayan puan yazılmaz;
> hamı olan koşu satırsız kalmaz [QA_KAYIT §0]. `bash araclar/sayac.sh` TOPLAM FİLM'i ve
> HAM ↔ TABLO uyumunu karşılaştırır.
> Eski 12 mercekli sonuçlar: `ARSIV_12_MERCEK/00_ARSIV.md §4` (temizlenmiş puanlar) — bu
> tabloya TAŞINMAZ, ölçekler farklı.

---

## SAYIM

```
TOPLAM FİLM          72     (dikey_shorts + yatay_*_dk_filmler klasörleri · 12 dk dahil)
BEŞ MERCEKLE ÖLÇÜLEN 19 (SKY STATION B1 · POOL ROOM · RAIN TOWER · HIDDEN LOFT · SKY VAULT · GAME ON · THE LAST STOP · THE SEA MILL · THE FIRST GUEST · TOTAL RESET · THE BURIED KHAN · THE EDEN ARK · THE HIDDEN FALLS · THE SLOW TAKEOFF · THE BORROWED HILL · LIT AGAIN · THE SUNKEN GARDEN · THE DRIVE IN · THE READING CAR)
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
| THE SKY VAULT | 9:16 | 2x | EKS | EKS · ŞİŞİK | EKS · ÇÖKÜK | EKS | YG | — (N=0) ⚠️ bağlayıcı değil — beş mercek boş blokla (dördüncü film); ızgara ❶ ❷ 6×5 sn · ❸ ❹ 31×1 sn · yalnız ❺ 8 (DERS 106); rapor-içi: 6,3 · 9,75 · 2,8 · 4,0 · 8,6; ajan ölçümü YOK (dosya okunamadı); örtüşen olaylar: vinç/panel S0 (4 mercek) · yabancı segment S5 22–23 sn (5 mercek) · film→perde S7 (❶ ❸ ❹ ↔ ❺ PASS) | MELTING (❶) · INTRUDERS (❹) (bağlayıcı değil) | 20.10.2026 |
| GAME ON | 9:16 | 2x | EKS | EKS · ŞİŞİK | EKS · ŞİŞİK | EKS · ŞİŞİK | YG | — (N=0) ⚠️ bağlayıcı değil — beş mercek boş blokla (33×1 sn dilimleme); rapor-içi: 9,7 · 10,0 · 10,0 · 10,0 · 10,0 (ort 9,9); olumsuz hüküm YOK; 8 sahnenin tüm inşa aşamaları ekranda eksiksiz görüldü | — | 22.10.2026 |
| THE LAST STOP | 9:16 | 2x | 7,5 | 10,0 | 8,9 | 9,4 | 9,3 | 9,0 (N=5) | MELTING (❶) | 22.10.2026 |
| THE SEA MILL | 9:16 | 2x | EKS | EKS · ŞİŞİK | EKS · ŞİŞİK | EKS · ŞİŞİK | YG | — (N=0) ⚠️ bağlayıcı değil — beş mercek boş blokla (28×1 sn dilimleme); rapor-içi: 7,9 · 10,0 · 10,0 · 10,0 · 9,6 (ort 9,5); duba ve ada lojistiği tam | MELTING (❶, bağlayıcı değil) | 22.10.2026 |
| THE FIRST GUEST | 9:16 | 2x | 9,1 | 10,0 | 10,0 | 10,0 | 10,0 | 9,8 (N=5) | — | 22.10.2026 |
| TOTAL RESET | 9:16 | 2x | EKS · ŞİŞİK | EKS · ŞİŞİK | EKS · ŞİŞİK | EKS · ŞİŞİK | YG | — (N=0) ⚠️ bağlayıcı değil — beş mercek boş blokla (31×1 sn dilimleme / mod V); rapor-içi: 10,0 · 10,0 · 10,0 · 10,0 · 10,0 (ort 10,0); olumsuz hüküm YOK; oda yenileme aşamaları tam | — | 22.10.2026 |
| THE BURIED KHAN | 16:9 | 1x | 8,3 | 9,1 | 9,5 | 8,8 | 9,8 | 9,1 (N=5) | MELTING (❶) · APPEARING (❹) | 22.10.2026 |
| THE EDEN ARK | 16:9 | 1x | 10,0 | 10,0 | 10,0 | 10,0 | 10,0 | 10,0 (N=5) | — | 22.10.2026 |
| THE HIDDEN FALLS | 16:9 | 1x | 5,4 | 5,5 | 3,7 | 3,9 | 8,5 | 5,4 (N=5) ⛔ DÜŞTÜ | SEPARATE IMAGES (❶) · MELTING (❶) · REBUILT (❸) · PARKED (❸) · APPEARING (❹) | 22.10.2026 |
| THE SLOW TAKEOFF | 16:9 | 1x | 9,3 | 9,8 | 10,0 | 10,0 | 10,0 | 9,8 (N=5) | — | 22.10.2026 |
| THE BORROWED HILL | 16:9 | 1x | 7,2 | 8,4 | 8,0 | 9,2 | 8,6 | 8,3 (N=5) | MELTING (❶) | 22.10.2026 |
| LIT AGAIN | 9:16 | 2x | 6,8 | 7,4 | 4,3 | 5,5 | 9,0 | 6,6 (N=5) ⛔ DÜŞTÜ | REBUILT (❸) · MELTING (❶) · PARKED (❸) · APPEARING (❹) | 25.10.2026 |
| THE SUNKEN GARDEN | 9:16 | 2x | 5,3 | 6,3 | 5,1 | 5,6 | 8,4 | 6,1 (N=5) ⛔ DÜŞTÜ | REBUILT (❸) · MELTING (❶) · WRONG DIRECTION (❷) · APPEARING (❹) | 25.10.2026 (K2: 27.10 37×1sn dilimleme 10,0 bağlayıcı değil) |
| THE DRIVE IN | 9:16 | 2x | EKS · ŞİŞİK | EKS · ŞİŞİK | EKS · ŞİŞİK | EKS · ŞİŞİK | YG | — (N=0) ⚠️ bağlayıcı değil — beş mercek boş blokla (34×1 sn dilimleme / mod V); rapor-içi: 10,0 · 10,0 · 10,0 · 10,0 · 10,0 (ort 10,0); olumsuz hüküm YOK; istasyon→drive-in dönüşümü tam | — | 27.10.2026 |
| THE READING CAR | 9:16 | 2x | EKS | EKS · ŞİŞİK | EKS · ŞİŞİK | EKS · ŞİŞİK | YG | — (N=0) ⚠️ bağlayıcı değil — beş mercek boş blokla (33×1 sn dilimleme / mod V); rapor-içi: 9,7 · 9,3 · 10,0 · 10,0 · 10,0 (ort 9,8); olumsuz hüküm YOK; vagon→kitapçı dönüşümü tam | — | 27.10.2026 |

```
⭐ "dosya" sütunu: 2x · 1x · 1x+2x (❸ ❹ master, ❶ ❷ ❺ yayın) [QA_OLCUM_ZEMINI §3]
⛔ Öldürücü hüküm (❶ SEPARATE IMAGES · ❸ REBUILT · ❹ DIFFERENT) varsa film puanının yanına
   "⛔ DÜŞTÜ" yazılır.
```
