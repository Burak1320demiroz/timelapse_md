# 📊 ⑤ DEVAMLILIK — SKOR TABLOSU

> Rubrik: `5_DEVAMLILIK_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.

| Film | Mod | Skor | VERDICT | Bulgu | Rapor |
|---|:---:|---:|---|:---:|---|
| **THE LONG DAY** | ⚠️ V karesiz | *karesiz koşuldu — TEKRARLANACAK* (ham 5,8) | ✅ SAME WORLD · ⭐ kanıt BULUNDU: kaya + krater | 5/9 dikiş | [kayıt](RAPORLAR/THE_LONG_DAY.md) |
| **THE MOUNTAIN DOOR** | V | **0,2**/10 Ⓥ | ⛔ HER ÇEKİMDE YENİDEN · NONE FOUND | 4/4 dikiş | [kayıt](RAPORLAR/THE_MOUNTAIN_DOOR.md) |
| **THE NARROW LOT** | V | **5,6**/10 Ⓥ | ✅ SAME WORLD · kanıt BULUNDU | 4/4 dikiş | [kayıt](RAPORLAR/THE_NARROW_LOT.md) |
| **THE CLOSING SPAN** | V | **0,0**/10 Ⓥ | ⛔ HER ÇEKİMDE YENİDEN · NONE FOUND | 9/9 dikiş | [kayıt](RAPORLAR/THE_CLOSING_SPAN.md) |
| **THE DUST YEAR** | ⛔ V karesiz | *karesiz koşuldu — TEKRARLANACAK* (ham 4,0) | ⛔ A SET REBUILT EACH TIME · 9 dikişin 7'si kusurlu | 10 | [ham](HAM_RAPORLAR/THE_DUST_YEAR_DEVAMLILIK_HAM.md) |
| **BUILT FROM DUST** | ⛔ V karesiz | *karesiz koşuldu — TEKRARLANACAK* (ham 1,6) | ⛔ A SET REBUILT EACH TIME · kanıt: 3 dağ zirvesi | 5/5 dikiş | [kayıt](RAPORLAR/BUILT_FROM_DUST.md) |
| **POLAR HABITAT** | V | **10,0**/10 Ⓥ | ✅ SAME WORLD · kanıt BULUNDU: Kırmızı tuğlalı bina/dağ sırtı | 0/18 dikiş | [kayıt](RAPORLAR/POLAR_HABITAT.md) |
| **THE CROSSING** | ⚠️ V karesiz | **5,8**/10 Ⓥ | ✅ SAME WORLD · kanıt BULUNDU: Lighthouse on green island headland | 6/6 dikiş | [kayıt](RAPORLAR/THE_CROSSING.md) |
| **OVER THE WALL** | ⛔ V karesiz | *karesiz koşuldu — TEKRARLANACAK* (ham 3,0) | ⛔ A SET REBUILT EACH TIME · kanıt BULUNDU: taş köprü (00:00,0 ve 01:03,9) · 3 istasyon grubu | 6/6 dikiş | [kayıt](RAPORLAR/OVER_THE_WALL.md) |
| **THE EMPTY RIDGE** | ⛔ V karesiz | *karesiz koşuldu — TEKRARLANACAK* (ham 7,2) | ✅ SAME WORLD · ⭐ kanıt BULUNDU: plana konan YALNIZ MEŞE (00:00,5 ve 00:54,5) — planlı nesne ilk kez tuttu | 5/9 dikiş | [kayıt](RAPORLAR/THE_EMPTY_RIDGE.md) |
| **THE DARK ROCK** | ⛔ V karesiz | *karesiz koşuldu — TEKRARLANACAK* (ham 3,1) | ⛔ A SET REBUILT EACH TIME · NONE FOUND · 12 dikişin 10'u kusurlu | 5/12 dikiş | [ham](HAM_RAPORLAR/THE_DARK_ROCK/THE_DARK_ROCK_DEVAMLILIK_HAM.md) |

⛔ **THE MOUNTAIN DOOR · RUN INCOMPLETE:** kare grabı verilmedi. Dört dikişin DÖRDÜ de kusur taşıyor. ⭐ En ağır satır: plana KASTEN yerleştirilen kanıt nesnesi (2,4 m üstü düz granit kaya) 0:05,9 → 0:06,0'da **kayboldu** ve mercek NONE FOUND yazdı. Kanıt nesnesi yazmak yetmiyor [DERS 25].

⚠️ **THE NARROW LOT · RUN INCOMPLETE:** kare grabı verilmedi. Dikiş denetimi videodan yapıldı; "son kare / ilk kare" çiftleri hiç görülmedi.

**VERDICT değerleri:** SAME WORLD / A SET REBUILT EACH TIME

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır
```
