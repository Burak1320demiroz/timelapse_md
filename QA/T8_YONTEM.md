# 📊 ⑧ YÖNTEM — SKOR TABLOSU

> Rubrik: `8_YONTEM_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.
> Mercek 07.09.2026'da açıldı; önceki dört film bu mercekle ÖLÇÜLMEDİ.

| Film | Mod | Skor | VERDICT | İlk "beliren" parça | En iyi yapılan parça | Bulgu | Rapor |
|---|:---:|---:|---|---|---|:---:|---|
| **THE LONG DAY** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 3,0) | ⛔ APPEARED · 1/9 MADE | graded pad · 0:06,0 | habitat berm | 6 | [kayıt](RAPORLAR/THE_LONG_DAY.md) |
| **THE DUST YEAR** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham **0,0**) | ⛔ APPEARED · 0/8 MADE | circular pad · 0:06,0 | NONE | 6 | [ham](HAM_RAPORLAR/THE_DUST_YEAR_YONTEM_HAM.md) |

**VERDICT değerleri:** MADE / APPEARED

```
Ⓥ  mod V koşusu (QA_SPEC verilmedi) — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
⛔ Belgesiz koşulan ⑧ skoru tabloya YAZILMAZ; satır "belgesiz koşuldu —
   TEKRARLANACAK" diye açılır.
⭐ "THE FIRST PIECE THAT APPEARED" sütunu NONE değilse o parçanın yapıldığı
   sahne yeniden üretilir; parça adı buraya yazılır.
```
