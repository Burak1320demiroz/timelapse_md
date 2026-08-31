# 📊 ④ TESLİM — SKOR TABLOSU

> Rubrik: `4_TESLIM_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.

| Film | Mod | Skor | VERDICT | Bulgu | Rapor |
|---|:---:|---:|---|:---:|---|
| **THE NARROW LOT** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* | ⚠️ ENDS · NONE FOUND | 15 | [kayıt](RAPORLAR/THE_NARROW_LOT.md) |
| **THE CLOSING SPAN** | V | **5,4**/10 Ⓥ | ⚠️ BİTİYOR · NONE FOUND | 10 | [kayıt](RAPORLAR/THE_CLOSING_SPAN.md) |
| **THE LONG SHADOW** | V | **2,7**/10 Ⓥ | ⛔ DURUYOR · NONE FOUND | 15 | [kayıt](RAPORLAR/THE_LONG_SHADOW.md) |

⛔ **THE NARROW LOT belgesiz koşuldu [DERS 17]:** plan ve kapak verilmedi (kapak zaten ÜRETİLMEDİ). FINAL BEAT gerçek vuruşa karşı hiç denetlenmedi. Ölçülen ham ortalama 4,4.

**VERDICT değerleri:** BİTİYOR / DURUYOR

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır (ölçüm yapıldı, skor düştü)
```
