# 📊 ② İNŞA — SKOR TABLOSU

> Rubrik: `2_INSA_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.

| Film | Mod | Skor | VERDICT | Bulgu | Rapor |
|---|:---:|---:|---|:---:|---|
| **THE LONG DAY** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 6,2) | ⛔ DIFFERENT · APPEARING (5. kez) | 5 | [kayıt](RAPORLAR/THE_LONG_DAY.md) |
| **THE MOUNTAIN DOOR** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* | ⛔ DIFFERENT · APPEARING | 9 | [kayıt](RAPORLAR/THE_MOUNTAIN_DOOR.md) |
| **THE NARROW LOT** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* | ⛔ DIFFERENT · APPEARING | 9 | [kayıt](RAPORLAR/THE_NARROW_LOT.md) |
| **THE CLOSING SPAN** | V | **0,0**/10 Ⓥ | ⛔ FARKLI · APPEARING | 12 | [kayıt](RAPORLAR/THE_CLOSING_SPAN.md) |
| **THE LONG SHADOW** | V | **0,4**/10 Ⓥ | ⛔ FARKLI · APPEARING | 13 | [kayıt](RAPORLAR/THE_LONG_SHADOW.md) |
| **THE DUST YEAR** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 0,9) | ⛔ DIFFERENT · APPEARING (6. kez) | 11 | [ham](HAM_RAPORLAR/THE_DUST_YEAR_INSA_HAM.md) |
| **BUILT FROM DUST** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 2,8) | ⛔ DIFFERENT · APPEARING (7. kez) | 9 | [kayıt](RAPORLAR/BUILT_FROM_DUST.md) |
| **POLAR HABITAT** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 10,0) | ✅ SAME · BUILT | 0 | [kayıt](RAPORLAR/POLAR_HABITAT.md) |
| **THE CROSSING** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 6,4) | ✅ SAME · BUILT | 4 | [kayıt](RAPORLAR/THE_CROSSING.md) |
| **OVER THE WALL** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 3,8) | ⛔ DIFFERENT · APPEARING (8. kez) · havuz → kemer duvar 00:26,5 | 9 | [kayıt](RAPORLAR/OVER_THE_WALL.md) |
| **THE EMPTY RIDGE** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 5,2) | ⛔ DIFFERENT · ✅ BUILT (ilk kez bu ikili) · hayalet kule kopyaları 0:21 · 0:39 · rotor montajda döndü | 7 | [kayıt](RAPORLAR/THE_EMPTY_RIDGE.md) |
| **THE DARK ROCK** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 3,8) | ⛔ DIFFERENT · APPEARING (9. kez) · fener odası kaybolma 00:32 · robot kollar 00:41 · kara tarlası 00:37 | 5 | [kayıt](RAPORLAR/THE_DARK_ROCK.md) |
| **BACK TO WATER** | D | **9,3**/10 | ✅ SAME · BUILT · ⛔ kart DIFFERENT · vinçli kamyon ve sac montajı tam · suyla kalkış +1.8m · pervane köpüğü fiziksel uyumlu | 4 | [kayıt](RAPORLAR/BACK_TO_WATER.md) |


⛔ **THE MOUNTAIN DOOR belgesiz koşuldu [DERS 17] — İKİNCİ KEZ:** QA_SPEC bu filmde ÜRETİMDEN ÖNCE yazılmıştı ve merceğe yine verilmedi. Skoru tabloya yazılmaz. Ölçülen ham ortalama 1,5. ⛔ DIFFERENT · APPEARING hükmü **dördüncü kez** geldi.

⛔ **THE NARROW LOT belgesiz koşuldu [DERS 17]:** QA_SPEC verilmedi, mercek mod V'ye düştü. Bulguları geçerlidir ve rapora işlendi; **skoru tabloya yazılmaz** ve koşu belgeyle TEKRARLANACAK. Ölçülen ham ortalama 2,6.

**VERDICT değerleri:** AYNI / FARKLI · BUILT / APPEARING

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır (ölçüm yapıldı, skor düştü)
```
