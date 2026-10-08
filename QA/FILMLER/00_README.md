# 📁 FİLMLER — film başına tek kayıt

Her film için tek dosya: `QA/FILMLER/<FILM>.md`. Ajan doldurur; ham çıktı `QA/HAM/` altındadır.
Bölüm boş kalabilir ama **atlanmaz** — "DERS — yeni ders yok" bir bilgidir, bölümün yokluğu değil.

## Şablon

```markdown
# <FILM> — QA KAYDI

## KÜNYE
format · plan · üretim günlüğü · yayın dosyası (hız) · master (varsa) · kapak · koşu tarihleri

## MERCEKLER
| mercek | durum | puan | hüküm | ham | en ağır üç bulgu (m:ss.s) |
|---|---|:-:|---|---|---|
| ❶ GÖRÜNTÜ | TAM | 8,6 | TIMELAPSE · SOLID | Q1_…_HAM.md | … |
| ❷ ZAMAN VE KESME | | | | | |
| ❸ ŞANTİYE | | | | | |
| ❹ İNŞA | | | | | |
| ❺ TESLİM | | | | | |
FİLM PUANI  x,x · N=n          ÖLDÜRÜCÜ  — | ⛔ <hüküm>

## DOĞRULAMA
geri okuma (✓/✗ her mercek) · D1–D5 sonuçları · sızıntı taraması (kör mercekler)

## DOKÜMAN
kör merceklerin QUESTIONS FOR THE DOCUMENT listesi + plandan cevaplar

## OLAY TABLOSU
| olay | zaman | ne oldu (görünen) | mercekler | kanıt karesi | karar |
|---|---|---|---|---|---|
| E01 | 0:03.0–0:04.0 | … | ❶ ❸ | S1_son.jpg | S1 yeniden — … |

## KARAR
yeniden üretilecek sahneler · kabul edilen kusurlar · sebepleri

## DERS
yeni dersler (numaralarıyla, DERSLER.md'ye) — ya da "yeni ders yok"
```

```
⭐ Aynı olay birden fazla merceği etkiliyorsa TEK olay kimliği alır (E01, E02…).
⛔ Puan yalnız TAM durumlu koşudan yazılır; öteki durumlar etiketle (EKS · YG · SZ · TT).
```

Eski 12 mercekli film kayıtları: `QA/ARSIV_12_MERCEK/RAPORLAR/` (31 dosya · dondurulmuş).
