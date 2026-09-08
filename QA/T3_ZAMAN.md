# 📊 ③ ZAMAN — SKOR TABLOSU

> Rubrik: `3_ZAMAN_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.

| Film | Mod | Skor | VERDICT | Bulgu | Rapor |
|---|:---:|---:|---|:---:|---|
| **THE LONG DAY** | V | **7,0**/10 Ⓥ | ⛔ YANLIŞ YÖNDE GEÇİYOR · tahmin "one lunar day" (plan 19) TUTMADI | 8 | [kayıt](RAPORLAR/THE_LONG_DAY.md) |
| **THE MOUNTAIN DOOR** | V | **3,6**/10 | ⛔ YANLIŞ YÖNDE GEÇİYOR · zaman tahmini TUTTU | 8 | [kayıt](RAPORLAR/THE_MOUNTAIN_DOOR.md) |
| **THE NARROW LOT** | V | **4,2**/10 | ✅ PASSES · zaman tahmini TUTTU | 7 | [kayıt](RAPORLAR/THE_NARROW_LOT.md) |
| **THE CLOSING SPAN** | V | **1,3**/10 | ⛔ YANLIŞ YÖNDE GEÇİYOR | 15 | [kayıt](RAPORLAR/THE_CLOSING_SPAN.md) |
| **THE LONG SHADOW** | V | **4,3**/10 Ⓥ | ⚠️ GEÇİYOR (ama yön kırık) | 9 | [kayıt](RAPORLAR/THE_LONG_SHADOW.md) |
| **THE DUST YEAR** | V | **4,0**/10 Ⓥ | ⛔ TEK YÖNDE DEĞİL · okunan süre "about one year" ✅ | 10 | [ham](HAM_RAPORLAR/THE_DUST_YEAR_ZAMAN_HAM.md) |

⭐ **THE MOUNTAIN DOOR — ALTI MERCEĞİN TAM KOŞAN TEK'İ.** Girdisi yalnız tam kurgudur ve eksiksiz verildi; skoru **bağlayıcıdır** (Ⓥ yok). Zaman tahmini "about 9 to 12 months", plan 12 ay — **ikinci kez TUTTU**. ⛔ Buna karşılık SEASON ORDER 0/10: plandaki sonbahar hiç görünmedi ve kış ② (erime) YAZ olarak üretildi.

**VERDICT değerleri:** PASSES / PASSES BUT NOT IN ONE DIRECTION / ONLY THE LIGHT CHANGES

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır (ölçüm yapıldı, skor düştü)
```
