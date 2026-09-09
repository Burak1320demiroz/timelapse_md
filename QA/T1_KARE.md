# 📊 ① KARE — SKOR TABLOSU

> Rubrik: `1_KARE_QA.md` · Ham çıktı: `HAM_RAPORLAR/` · Kalıcı kayıt: `RAPORLAR/`
> Sayaç bu tablonun VERİ satırlarını sayar — başlık ve ayraç sayılmaz.

| Film | Mod | Skor | VERDICT | Bulgu | Rapor |
|---|:---:|---:|---|:---:|---|
| **THE LONG DAY** | ⚠️ V karesiz | *karesiz koşuldu — TEKRARLANACAK* (ham 6,4) | ✅ TIME-LAPSE · 4 kilit kategori 10/10 · PEOPLE 0 · SURFACE 0 | 8 | [kayıt](RAPORLAR/THE_LONG_DAY.md) |
| **THE MOUNTAIN DOOR** | V | **1,1**/10 Ⓥ | ⛔ AYRI AYRI GÖRÜNTÜLER | 22 | [kayıt](RAPORLAR/THE_MOUNTAIN_DOOR.md) |
| **THE NARROW LOT** | V | **6,0**/10 Ⓥ | ✅ TIMELAPSE | 8 | [kayıt](RAPORLAR/THE_NARROW_LOT.md) |
| **THE CLOSING SPAN** | V | **1,0**/10 | ⛔ AYRI AYRI GÖRÜNTÜLER | 28 | [kayıt](RAPORLAR/THE_CLOSING_SPAN.md) |
| **THE LONG SHADOW** | V | **3,3**/10 Ⓥ | ⛔ ALTI AYRI GÖRÜNTÜ | 13 | [kayıt](RAPORLAR/THE_LONG_SHADOW.md) |
| **THE DUST YEAR** | ⛔ V karesiz | *karesiz koşuldu — TEKRARLANACAK* (ham 1,3) | ⛔ SIX SEPARATE SHOTS · kart FARKLI | 15 | [ham](HAM_RAPORLAR/THE_DUST_YEAR_KARE_HAM.md) |
| **BUILT FROM DUST** | ⛔ V karesiz | *karesiz koşuldu — TEKRARLANACAK* (ham 1,1) | ⛔ SIX SEPARATE SHOTS | 13 | [kayıt](RAPORLAR/BUILT_FROM_DUST.md) |

⚠️ **THE MOUNTAIN DOOR · RUN INCOMPLETE:** kare grabı verilmedi (`kare_al.sh` yine koşulmadı — üçüncü film). ⛔ CAMERA LOCK **0/10**: beş klibin BEŞİNDE de yavaş push-in. Ölçülebilir çapa cümlesi beş I2V'nin beşinde de YAZILIYDI ve tutmadı — NARROW LOT'ta aynı cümle 10/10 almıştı [DERS 23].

⚠️ **THE NARROW LOT · RUN INCOMPLETE:** kare grabı verilmedi (`kare_al.sh` koşulmadı). Skor eksik girdiyle alındı; VERDICT bağlayıcıdır.

**VERDICT değerleri:** TIMELAPSE / ALTI AYRI GÖRÜNTÜ

```
Ⓥ  mod V koşusu — ÖN KOŞUDUR, skoru bağlayıcı değildir.
    VERDICT satırı her modda bağlayıcıdır.
~~üstü çizili~~  skoru geçersiz sayılmış satır (ölçüm yapıldı, skor düştü)
```
