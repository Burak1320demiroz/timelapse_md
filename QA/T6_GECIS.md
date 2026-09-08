# 📊 ⑥ GEÇİŞ — SKOR TABLOSU

> Rubrik: `6_GECIS_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.

| Film | Mod | Skor | VERDICT | Bulgu | Rapor |
|---|:---:|---:|---|:---:|---|
| **THE LONG DAY** | ⛔ V sessiz | *belgesiz koşuldu — TEKRARLANACAK* (ham 7,7) | ✅ TIME · ⛔ METRONOM (4. kez) | 3 | [kayıt](RAPORLAR/THE_LONG_DAY.md) |
| **THE MOUNTAIN DOOR** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* | ⛔ NEXT · METRONOM | 7 | [kayıt](RAPORLAR/THE_MOUNTAIN_DOOR.md) |
| **THE NARROW LOT** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* | ✅ TIME · ⛔ METRONOM | 3 | [kayıt](RAPORLAR/THE_NARROW_LOT.md) |
| **THE CLOSING SPAN** | V | **1,6**/10 Ⓥ | ⛔ SIRADAKİ · METRONOM | 9 | [kayıt](RAPORLAR/THE_CLOSING_SPAN.md) |
| **THE DUST YEAR** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 6,6) | ⛔ NEXT · METRONOM (5. kez — ızgara VARYANSLIYKEN) | 6 | [ham](HAM_RAPORLAR/THE_DUST_YEAR_GECIS_HAM.md) |

⛔ **THE NARROW LOT belgesiz koşuldu [DERS 17]:** plan ve SES verilmedi. MUSIC ALIGNMENT ve END-CARD HAND-OVER hiç ölçülemedi. Ölçülen ham ortalama 8,2 — deponun en yüksek mercek skoru, ama üç kategorisi hiç sorulmadı.

⛔ **THE MOUNTAIN DOOR belgesiz koşuldu [DERS 17]:** plan verilmedi ve **filmde ses yok** — MUSIC ALIGNMENT yine ölçülemedi. Ham ortalama 3,5. ⛔ METRONOM **üçüncü kez**; RHYTHM 0/10 ile deponun en düşüğü. ⚠️ Klip İÇİ vuruş varyansı telafisi bu filmde denendi ve **düştü** [DERS 24].

**VERDICT değerleri:** TIME / NEXT · RHYTHM / METRONOME

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır
```
