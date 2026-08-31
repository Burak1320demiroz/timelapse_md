# 📊 ① KARE — SKOR TABLOSU

> Rubrik: `1_KARE_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.

| Film | Mod | Skor | VERDICT | Bulgu | Rapor |
|---|:---:|---:|---|:---:|---|
| **THE NARROW LOT** | V | **6,0**/10 Ⓥ | ✅ TIMELAPSE | 8 | [kayıt](RAPORLAR/THE_NARROW_LOT.md) |
| **THE CLOSING SPAN** | V | **1,0**/10 | ⛔ AYRI AYRI GÖRÜNTÜLER | 28 | [kayıt](RAPORLAR/THE_CLOSING_SPAN.md) |
| **THE LONG SHADOW** | V | **3,3**/10 Ⓥ | ⛔ ALTI AYRI GÖRÜNTÜ | 13 | [kayıt](RAPORLAR/THE_LONG_SHADOW.md) |

⚠️ **THE NARROW LOT · RUN INCOMPLETE:** kare grabı verilmedi (`kare_al.sh` koşulmadı). Skor eksik girdiyle alındı; VERDICT bağlayıcıdır.

**VERDICT değerleri:** TIMELAPSE / ALTI AYRI GÖRÜNTÜ

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır (ölçüm yapıldı, skor düştü)
```
