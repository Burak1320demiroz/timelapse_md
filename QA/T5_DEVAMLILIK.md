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

⛔ **THE MOUNTAIN DOOR · RUN INCOMPLETE:** kare grabı verilmedi. Dört dikişin DÖRDÜ de kusur taşıyor. ⭐ En ağır satır: plana KASTEN yerleştirilen kanıt nesnesi (2,4 m üstü düz granit kaya) 0:05,9 → 0:06,0'da **kayboldu** ve mercek NONE FOUND yazdı. Kanıt nesnesi yazmak yetmiyor [DERS 25].

⚠️ **THE NARROW LOT · RUN INCOMPLETE:** kare grabı verilmedi. Dikiş denetimi videodan yapıldı; "son kare / ilk kare" çiftleri hiç görülmedi.

**VERDICT değerleri:** SAME WORLD / A SET REBUILT EACH TIME

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır
```
