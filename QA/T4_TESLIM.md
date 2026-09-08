# 📊 ④ TESLİM — SKOR TABLOSU

> Rubrik: `4_TESLIM_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.

| Film | Mod | Skor | VERDICT | Bulgu | Rapor |
|---|:---:|---:|---|:---:|---|
| **THE LONG DAY** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 4,8) | ⚠️ ENDS · ⭐ ONE THING BULUNDU (ilk kez) · LOOP 0 · END CARD DIFFERENT | 6 | [kayıt](RAPORLAR/THE_LONG_DAY.md) |
| **THE MOUNTAIN DOOR** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* | ⚠️ ENDS · NONE FOUND | 6 | [kayıt](RAPORLAR/THE_MOUNTAIN_DOOR.md) |
| **THE NARROW LOT** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* | ⚠️ ENDS · NONE FOUND | 15 | [kayıt](RAPORLAR/THE_NARROW_LOT.md) |
| **THE CLOSING SPAN** | V | **5,4**/10 Ⓥ | ⚠️ BİTİYOR · NONE FOUND | 10 | [kayıt](RAPORLAR/THE_CLOSING_SPAN.md) |
| **THE LONG SHADOW** | V | **2,7**/10 Ⓥ | ⛔ DURUYOR · NONE FOUND | 15 | [kayıt](RAPORLAR/THE_LONG_SHADOW.md) |
| **THE DUST YEAR** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 2,1) | ⛔ STOPS · COST/FINAL BEAT **FAIL** · NONE FOUND | 5 | [ham](HAM_RAPORLAR/THE_DUST_YEAR_TESLIM_HAM.md) |

⛔ **THE MOUNTAIN DOOR belgesiz koşuldu [DERS 17]:** plan da kapak da verilmedi. FINAL BEAT beyan edilmiş vuruşa karşı denetlenmedi — mod V'de kategori "bir sonu var mı"ya dönüştü ve PASS verdi. ⛔ NONE FOUND **dördüncü kez** — bu filmde BEDEL plana İKİ kez yazılıydı [DERS 26]. Ham ortalama 4,0.

⛔ **THE NARROW LOT belgesiz koşuldu [DERS 17]:** plan ve kapak verilmedi (kapak zaten ÜRETİLMEDİ). FINAL BEAT gerçek vuruşa karşı hiç denetlenmedi. Ölçülen ham ortalama 4,4.

**VERDICT değerleri:** BİTİYOR / DURUYOR

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır (ölçüm yapıldı, skor düştü)
```
