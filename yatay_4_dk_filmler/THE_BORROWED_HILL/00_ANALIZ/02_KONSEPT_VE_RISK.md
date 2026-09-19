# 🎯 THE BORROWED HILL — KONSEPT VE RİSK

## 1. Konsept kapısı [KILAVUZ_REHBERI §6]

```
VAAT     Bir tepe küçülürken toprağı başka bir yerde yaşam alanına dönüşüyor;
         sonuç ve doğada bıraktığı iz AYNI KADRAJDA.
DİRENÇ   Örtü ve dolgu yerinden kazılacak · kırağı mevsimi · toz fırtınası ·
         panellerin körelmesi · izlerin dolması
BEDEL    Tepecik: %66,9 → %44,9; uzak krater sırtının (%51,6) üstünden altına
TEK CÜMLE  Tepe kaybolmuyor — ev oluyor.
```

### Dört kabul testi

```
① KADRAJDA MI        evet — tepe G0'da 329 px geniş, tacı %66,9
② SABİT KAMERADA MI  evet — 25 kare tek istasyon; hareket yalnız kurguda, üç anda
③ ÖLÇÜLEBİLİR Mİ     evet — geçilen çizgi GÖRÜNÜR (uzak krater sırtı %51,6)
④ MALZEME DENGELİ Mİ evet — alınan 4.724 m³ = kullanılan 4.724 m³ (plan §HACİM DEFTERİ)
```

## 2. Kart seçimi

```
YAPI TİPİ   ⬜ KARTTA YOK. Gömülü kemer sığınak + ISRU örtü bu depoda ilk kez.
            En yakın akraba: YAPI_TIPI_KARTLARI §9b (kayar kalıp) — biçimin gerekçesi
            ortak (basınç kabı köşeli olamaz), yöntem farklı.
            ⇒ Üretimden sonra kart açılır [kart H]: "gömülü kemer + yerel örtü".
SAHA        SAHA_VE_IKLIM §3.6 çöl/kurak'ın Mars hâli — ⬜ kart yok.
            Devralınan: film_md UZAY_USSU §3 (F1-a…F1-e)
KAMERA      KAMERA_ISTASYONU §1 saf tek istasyon · §2.8 yatay formüller
```

## 3. Kamera hesabı — özet

```
h = +6,0 m · D_eksen 95 m · 24 mm · bearing 0° · tilt 0°
yüzde(y) = 50 + 118,5 · (y − 6,0) / D        px = 1280 · boy(m) / D
alt çeyrek eşiği D_alt = 24 × 6,0 / (36 × 0,25) = 16,0 m — en yakın nesne 25 m ✅
⭐ ÇİZGİ  uzak krater sırtı (40 m @ 2.500 m) = %51,6 · 25 karede DEĞİŞMEZ
⛔ Kamera neden 12,0 m'den 6,0 m'ye indi: 12,0 m'de tepe S18'de %50'ye geliyordu ve
   S21 doruğu ÖNCE TÜKENİYORDU [P4-b]. Ayrıntı: plan §ELEŞTİRİ TURU ②.
```

## 4. Vinç kararı

```
⛔ BU FİLMDE VİNÇ YOKTUR. "crane" kelimesi 25 promptun tamamından kaldırıldı.
SEBEP  ① DERS 8 · 22: kanca iki filmde de koptu, (a) şıkkı düştü
       ② DERS 57: uzun rijit yük havada TAŞINMAZ, modelde hedefte belirir
       ③ kelime negatif bloğun yüzey listesinde geçtiği için kapı 25 karede birden açıldı
YERİNE "lifting rig" — yükü bom başında İKİ GERGİN SAPANLA tutar, kanca anılmaz.
       Kaldırma karede biter: kaburga G(n)'de dikilmiş durur, klip yalnız oturtur.
```

## 5. Işık günü

```
06:20 → 19:30 = 13 sa 10 dk   ·   5 × B + 19 × A = 13,17 sa ≤ 14 ✅
B sahneleri: S0 (ilk yara) · S2 (pad) · S7 (hendek) · S14 (ilk örtü) · S21 (son örtü)
⚠️ Mars solü 24 sa 39 dk; 40°N yaz gün uzunluğu ≈ 15 sa — 13 sa 10 dk zarfın içinde.
⚠️ Güneş açıları TÜRETİLMİŞ MODELDİR, efemeris iddiası değildir.
```

## 6. ⛔ RİSK TABLOSU — her satır ölçülmüş bir arızaya bağlı

| risk | kaynak | karşı tedbir | nerede ölçülür |
|---|---|---|---|
| **Bilimkurgu sızıntısı** (ışın · bloom · ark) | POLAR HABITAT | negatifte beş ayrı yasak · üs şantiye dilinde yazıldı | araç kapısı ⑩ · QA_SPEC §7 |
| **⑧ APPEARED** | DUST YEAR 0,0 · BUILT FROM DUST 0,0 | 24 ince aşama · her AT THIS STAGE'de geçici ekipman | prompt kapısı · ⑧ merceği |
| **⑦ PARKED / IDLE** | BUILT FROM DUST (24 sn daire) | DERS 43 geçişli fiil + büyüyen eleman nesne | prompt kapısı · ⑦ merceği |
| **Çoğul üs** | DERS 55 (türbin çiftliği) | sayım cümlesi + yerleşim + araç kapısı ⑨ | araç kapısı ⑨ · QA_SPEC §6 |
| **Operatörlü makine** | DERS 41 | ELLİ makine adı hiç kullanılmadı · mühürlü birim cümlesi | araç kapısı ⑬ |
| **Ay dili Mars'a** | F1-d (film_md) | "no atmospheric haze" ve "mutlak siyah gölge" YASAK | araç kapısı ⑫ |
| **Tepenin kendiliğinden erimesi** | ⭐ P4-c | ALINAN → VARIŞ YERİ sütunu · fırtınada ocak durur | QA_SPEC §4 |
| **Doruğun erken tükenmesi** | ⭐ P4-b | çizgi görünür sırta taşındı · S21 sabit kamera | QA_SPEC §2 · §8 ③ |
| **Ölçek: ayrıntı çok küçük** | ⭐ P4-e | üç yakınlaşma + px hedefleri + yakın referans denetimi | günlük §0b |
| **Kutu seti {4,6,8}** | DERS 23 · 31 | 24 ara kare gerekir → karar SAHİBE döner | araç kapısı ① |
| **16:9 güvenli alan** | ⬜ ÖLÇÜLMEDİ | varsayılan kullanıldı; ⭐ bu film ilk ölçüm | ① koşusu → §2.8 |
