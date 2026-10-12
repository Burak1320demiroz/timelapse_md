# 📊 TABLO — QA'NIN TEK SAYACI

> ⛔ Her hücre bir ham dosyaya bağlıdır (`QA/HAM/<FILM>/…`). Hamı olmayan puan yazılmaz;
> hamı olan koşu satırsız kalmaz [QA_KAYIT §0]. `bash araclar/sayac.sh` TOPLAM FİLM'i ve
> HAM ↔ TABLO uyumunu karşılaştırır.
> Eski 12 mercekli sonuçlar: `ARSIV_12_MERCEK/00_ARSIV.md §4` (temizlenmiş puanlar) — bu
> tabloya TAŞINMAZ, ölçekler farklı.

---

## SAYIM

```
TOPLAM FİLM          52     (dikey_shorts + yatay_*_dk_filmler klasörleri)
BEŞ MERCEKLE ÖLÇÜLEN 0
ARŞİVDE ÖLÇÜLEN      37     (ARSIV_12_MERCEK/HAM_RAPORLAR klasörleri · 12 mercek)
```

## FİLM × MERCEK

Hücre: mercek puanı (TAM) · `EKS` eksik · `YG` yanlış girdi · `SZ` sızıntı · `TT` tutarsız ·
`—` koşulmadı. Hüküm sütunu yalnız olumsuz hükümleri yazar. Film puanı = TAM merceklerin
ortalaması · N.

| film | biçim | dosya | ❶ | ❷ | ❸ | ❹ | ❺ | film puanı (N) | olumsuz hüküm | koşu tarihi |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|:-:|

```
⭐ "dosya" sütunu: 2x · 1x · 1x+2x (❸ ❹ master, ❶ ❷ ❺ yayın) [QA_OLCUM_ZEMINI §3]
⛔ Öldürücü hüküm (❶ SEPARATE IMAGES · ❸ REBUILT · ❹ DIFFERENT) varsa film puanının yanına
   "⛔ DÜŞTÜ" yazılır.
```
