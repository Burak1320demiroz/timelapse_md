# 📊 ② İNŞA — SKOR TABLOSU

> Rubrik: `2_INSA_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.

| Film | Mod | Skor | VERDICT | Bulgu | Rapor |
|---|:---:|---:|---|:---:|---|
| **THE NARROW LOT** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* | ⛔ DIFFERENT · APPEARING | 9 | [kayıt](RAPORLAR/THE_NARROW_LOT.md) |
| **THE CLOSING SPAN** | V | **0,0**/10 Ⓥ | ⛔ FARKLI · APPEARING | 12 | [kayıt](RAPORLAR/THE_CLOSING_SPAN.md) |
| **THE LONG SHADOW** | V | **0,4**/10 Ⓥ | ⛔ FARKLI · APPEARING | 13 | [kayıt](RAPORLAR/THE_LONG_SHADOW.md) |

⛔ **THE NARROW LOT belgesiz koşuldu [DERS 17]:** QA_SPEC verilmedi, mercek mod V'ye düştü. Bulguları geçerlidir ve rapora işlendi; **skoru tabloya yazılmaz** ve koşu belgeyle TEKRARLANACAK. Ölçülen ham ortalama 2,6.

**VERDICT değerleri:** AYNI / FARKLI · BUILT / APPEARING

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır (ölçüm yapıldı, skor düştü)
```
