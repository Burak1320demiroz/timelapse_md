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
| **BUILT FROM DUST** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 2,5) | ⛔ STOPS · COST/FINAL BEAT **FAIL** · NONE FOUND | 6 | [kayıt](RAPORLAR/BUILT_FROM_DUST.md) |
| **POLAR HABITAT** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 7,1) | ⚠️ ENDS · COST/FINAL BEAT PASS (8/10) | 5 | [kayıt](RAPORLAR/POLAR_HABITAT.md) |
| **THE CROSSING** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 7,9) | ⚠️ ENDS · COST/FINAL BEAT PASS (9/10) | 4 | [kayıt](RAPORLAR/THE_CROSSING.md) |
| **OVER THE WALL** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 5,3) | ⚠️ ENDS · COST/FINAL BEAT PASS (7/10) · ONE THING BULUNDU · LOOP 3 · kapak verilmedi | 6 | [kayıt](RAPORLAR/OVER_THE_WALL.md) |
| **THE EMPTY RIDGE** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 3,4) | ⚠️ ENDS · COST/FINAL BEAT FAIL (belgesiz) · NONE FOUND (5. kez) · RESISTANCE 2 (rüzgâr bekleyişi okunmadı) · kapak verilmedi | 8 | [kayıt](RAPORLAR/THE_EMPTY_RIDGE.md) |
| **THE DARK ROCK** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 6,1) | ⚠️ ENDS · COST/FINAL BEAT PASS (8/10) · kapak verilmedi | 5 | [ham](HAM_RAPORLAR/THE_DARK_ROCK/THE_DARK_ROCK_TESLIM_HAM.md) |
| **BACK TO WATER** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 7,1) | ⚠️ ENDS · COST/FINAL BEAT PASS (9/10) · ⭐ ONE THING BULUNDU · LOOP 3 · kapak ve plan verilmedi | 8 | [kayıt](RAPORLAR/BACK_TO_WATER.md) |
| **THE QUIET FIELD** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 8,4) | ✅ ENDS · COST/FINAL BEAT PASS (9/10) · ⭐ ONE THING BULUNDU · plan ve kapak verilmedi | 1 | [kayıt](RAPORLAR/THE_QUIET_FIELD.md) |
| **THE EMPTY LOCK** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 6,8) | ✅ ENDS · COST/FINAL BEAT PASS (7/10 Ⓥ) · ⭐ ONE THING BULUNDU · LOOP 5 · plan ve kapak verilmedi | 4 | [kayıt](RAPORLAR/THE_EMPTY_LOCK.md) |


⛔ **THE MOUNTAIN DOOR belgesiz koşuldu [DERS 17]:** plan da kapak da verilmedi. FINAL BEAT beyan edilmiş vuruşa karşı denetlenmedi — mod V'de kategori "bir sonu var mı"ya dönüştü ve PASS verdi. ⛔ NONE FOUND **dördüncü kez** — bu filmde BEDEL plana İKİ kez yazılıydı [DERS 26]. Ham ortalama 4,0.

⛔ **THE NARROW LOT belgesiz koşuldu [DERS 17]:** plan ve kapak verilmedi (kapak zaten ÜRETİLMEDİ). FINAL BEAT gerçek vuruşa karşı hiç denetlenmedi. Ölçülen ham ortalama 4,4.

**VERDICT değerleri:** BİTİYOR / DURUYOR

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır (ölçüm yapıldı, skor düştü)
```
