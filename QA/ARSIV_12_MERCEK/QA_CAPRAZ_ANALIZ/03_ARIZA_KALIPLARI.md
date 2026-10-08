# 🚨 En Çok Tekrarlanan TOP 10 Hata Kalıbı (Arıza Kataloğu)

> **Kapsam:** Depodaki `QA/HAM_RAPORLAR/` dizininde yer alan 15 dikey Shorts filminin 132 adet ham QA raporunda (130 puanlı + 2 INC) tespit edilen en kronik 10 hata kalıbı ve kanıt kataloğudur.

---

## 📋 TOP 10 Arıza Kalıbı Özet Tablosu

| Kodu | Arıza Kalıbı Adı | Etkilenen Temel Mercekler | Etkilenen Film Sayısı | Kritik Seviye |
|---|---|---|---|---|
| **F01** | Sihirli Belirme ve Nedensiz Montaj | `② İNŞA`, `⑧ YÖNTEM`, `⑩ SEBEP` | 13 / 15 Film | 🔴 KRİTİK |
| **F02** | Atıl Şantiye ve Durdurulmuş Hareket | `⑦ İŞ`, `⑨ FAALİYET` | 11 / 15 Film | 🔴 KRİTİK |
| **F03** | Metronomik Düz Izgara Kesmesi | `⑥ GEÇİŞ` | 9 / 13 Film | 🟡 ORTA |
| **F04** | İstasyon ve Çapa Nesne Bozulması | `① KARE`, `⑤ DEVAMLILIK` | 10 / 15 Film | 🔴 KRİTİK |
| **F05** | Geometrik Sıvı Büyüme (AI Morphing) | `② İNŞA`, `⑧ YÖNTEM`, `⑫ KATILIK` | 8 / 15 Film | 🔴 KRİTİK |
| **F06** | Durağan Heykel İnsan ve İşçiler | `① KARE`, `⑦ İŞ`, `⑨ FAALİYET` | 8 / 15 Film | 🟡 ORTA |
| **F07** | Güneş Saati ve Gölge Sıçraması | `③ ZAMAN` | 7 / 15 Film | 🟡 ORTA |
| **F08** | Yük Yolu İhlali ve Boşta Süzülme | `⑧ YÖNTEM`, `⑩ SEBEP`, `⑫ KATILIK` | 7 / 15 Film | 🔴 KRİTİK |
| **F09** | Kapak Vaadi ile Final Kare Uyuşmazlığı | `④ TESLİM` | 6 / 14 Film | 🔴 KRİTİK |
| **F10** | Filigran ve Yapay Zeka Metin Sızıntısı | `① KARE`, `④ TESLİM` | 5 / 15 Film | 🟢 DÜŞÜK |

> ⚠️ **"Etkilenen film sayısı" bağımsız toplam değildir.** F01 (nedensiz montaj), F05 (sıvı büyüme) ve F08 (bağsız yük) çoğu filmde AYNI montaj olayının farklı merceklerdeki belirtileridir; bir film üçünde birden sayılabilir. Toplam arıza sayısı üretilmez, olaylar film bazında tek kimlikle ilişkilendirilir (QA/00_README.md → OLAY TABLOSU).

---

## 🔎 Arıza Kalıplarının Derinlemesine Kanıt Kataloğu

### 🔴 F01: Sihirli Belirme ve Nedensiz Montaj (MAGICAL APPEARANCE / UNCAUSED ASSEMBLY)
- **Tanım:** Sahada hiçbir vinç, taşıyıcı veya işçi faaliyeti yokken yapı elemanlarının (taşlar, ahşap kirişler, çelik paneller) boşluktan aniden belirmesi veya kendiliğinden birleşmesi.
- **Etkilenen Mercekler:** `② İNŞA`, `⑧ YÖNTEM`, `⑩ SEBEP`
- **Etkilenen Filmler:** `ONE_MORE_TURN`, `OVER_THE_WALL`, `THE_DARK_ROCK`, `THE_EMPTY_RIDGE`, `BUILT_FROM_DUST`, `THE_DUST_YEAR`, `THE_OLD_ROAD`, `BEFORE_NIGHTFALL` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `ONE_MORE_TURN_SEBEP_HAM.md`: `"Circular outer rim hoops | 0:05.0 | Floats and morphs onto spokes in mid-air | MAGIC"`
  - `OVER_THE_WALL_10_SEBEP_HAM.md`: `"Concrete Basin Structure | 0:18.5 | None (trucks driving past on valley floor) | MAGIC"`
  - `THE_DARK_ROCK_SEBEP_HAM.md`: `"Concrete Terrace / Foundation Pad | 00:04.0 | Natural rock vanishes instantly into a pad | MAGIC"`

---

### 🔴 F02: Atıl Şantiye ve Durdurulmuş Hareket (PARKED VEHICLES & IDLE STRETCHES)
- **Tanım:** Klipler boyunca iş makinelerinin (ekskavatör, kamyon, vinç) motoru çalışmıyormuş gibi sabit durması, inşaatın belirli saniyelerde tamamen duraklaması.
- **Etkilenen Mercekler:** `⑦ İŞ`, `⑨ FAALİYET`
- **Etkilenen Filmler:** `BEFORE_NIGHTFALL`, `BUILT_FROM_DUST`, `ONE_MORE_TURN`, `THE_DARK_ROCK`, `OVER_THE_WALL`, `THE_LONG_DAY` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `BEFORE_NIGHTFALL_7_IS_QA_HAM.md`: `"DOES THE SITE EVER STOP? -> PARKED (Vehicles stationary for 4.5 seconds)"`
  - `BUILT_FROM_DUST_7_IS_QA_HAM.md`: `"DOES THE SITE EVER STOP? -> PARKED"`
  - `BUILT_FROM_DUST_9_FAALIYET_QA_HAM.md`: `"1 IDLE / PARKED PRESENCE -> 2Ⓥ/10"`

---

### 🟡 F03: Metronomik Düz Izgara Kesmesi (METRONOME EFFECT)
- **Tanım:** Filmin tüm kliplerinin birebir aynı sürede (örneğin tam 8.0 sn veya tam 6.0 sn) kesilmesi; kurgusal ivme, ritim değişkenliği ve tempo artışının sağlanamaması.
- **Etkilenen Mercekler:** `⑥ GEÇİŞ`
- **Etkilenen Filmler:** `BEFORE_NIGHTFALL`, `BUILT_FROM_DUST`, `ONE_MORE_TURN`, `THE_DUST_YEAR`, `THE_LONG_DAY`, `THE_MOUNTAIN_DOOR`, `THE_NARROW_LOT` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `BEFORE_NIGHTFALL_6_GECIS_QA_HAM.md`: `"RHYTHM OR METRONOME? -> METRONOME (All clips cut at strictly equal 8.0s intervals)"`
  - `BUILT_FROM_DUST_6_GECIS_QA_HAM.md`: `"RHYTHM OR METRONOME? -> METRONOME"`
  - `ONE_MORE_TURN_GECIS_HAM.md`: `"RHYTHM OR METRONOME? -> METRONOME"`

---

### 🔴 F04: İstasyon ve Çapa Nesne Bozulması (ANCHOR LOSS & STATION SHIFT)
- **Tanım:** Kameranın sabit istasyon olmasına rağmen sahneler arasında kadrajın 10-20 piksel kayması veya arka plandaki nirengi noktalarının (dağlar, kaya yüzeyleri, komşu yapılar) deforme olması.
- **Etkilenen Mercekler:** `① KARE`, `⑤ DEVAMLILIK`
- **Etkilenen Filmler:** `THE_CLOSING_SPAN`, `THE_MOUNTAIN_DOOR`, `BUILT_FROM_DUST`, `OVER_THE_WALL`, `THE_DARK_ROCK` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `BEFORE_NIGHTFALL_1_KARE_QA_HAM.md`: `"3 ANCHOR IDENTITY -> Ⓥ 0/10 (Background ridge shifts left between frames)"`
  - `BUILT_FROM_DUST_1_KARE_QA_HAM.md`: `"1 CAMERA LOCK -> 0/10, 4 STATION IDENTITY -> 0/10"`
  - `THE_CLOSING_SPAN_DEVAMLILIK_HAM.md`: `"Bridge pier alignment shifts by 15px vertically across cut"`

---

### 🔴 F05: Geometrik Sıvı Büyüme (AI STRUCTURE MORPHING)
- **Tanım:** Yapının parçalarının fiziki inşaat adımlarıyla eklenmesi yerine, beton veya çelik kütlenin sıvı/köpük gibi genleşerek genişlemesi veya biçim değiştirmesi.
- **Etkilenen Mercekler:** `② İNŞA`, `⑧ YÖNTEM`, `⑫ KATILIK`
- **Etkilenen Filmler:** `THE_DUST_YEAR`, `THE_CLOSING_SPAN`, `THE_MOUNTAIN_DOOR`, `THE_LONG_SHADOW`, `BUILT_FROM_DUST` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `THE_DUST_YEAR_INSA_HAM.md`: `"LOAD PATH -> 0.9/10 (Structure expands continuously like foam without joints)"`
  - `THE_CLOSING_SPAN_INSA_HAM.md`: `"2 İNŞA -> 0.0/10 (Central arch spans morph into existence across void)"`

---

### 🟡 F06: Durağan Heykel İnsan ve İşçiler (STATIC HUMAN / GHOST WORKERS)
- **Tanım:** Sahadaki insan figürlerinin klip boyunca donmuş heykeller gibi durması veya bir sonraki kareye geçildiğinde arkalarında hiçbir iz bırakmadan yok olmaları.
- **Etkilenen Mercekler:** `① KARE`, `⑦ İŞ`, `⑨ FAALİYET`
- **Etkilenen Filmler:** `ONE_MORE_TURN`, `THE_DARK_ROCK`, `OVER_THE_WALL`, `THE_EMPTY_RIDGE`, `BUILT_FROM_DUST` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `ONE_MORE_TURN_FAALIYET_HAM.md`: `"Workers stand motionlessly along flume edge during active pour"`
  - `OVER_THE_WALL_1_KARE_HAM.md`: `"Human worker figure vanishes abruptly between Frame 2 and Frame 3"`

---

### 🟡 F07: Güneş Saati ve Gölge Sıçraması (SHADOW JUMP & TIMELINE REVERSAL)
- **Tanım:** Zaman atlamalı sahnelerde gölge boyunun ve açısının mantıksız değişmesi; sabah gölgesinden aniden akşamüstü açısına geçilmesi veya ışık yönünün 180 derece dönmesi.
- **Etkilenen Mercekler:** `③ ZAMAN`
- **Etkilenen Filmler:** `THE_DARK_ROCK`, `BEFORE_NIGHTFALL`, `THE_LONG_SHADOW`, `THE_CLOSING_SPAN`, `THE_DUST_YEAR` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `THE_DARK_ROCK_ZAMAN_HAM.md`: `"3 ZAMAN -> 2.8/10 (Shadow angle jumps from 10:00 position to 16:30 position)"`
  - `BEFORE_NIGHTFALL_3_ZAMAN_QA_HAM.md`: `"Sun elevation drops and reverses travel direction in Clip 4"`

---

### 🔴 F08: Yük Yolu İhlali ve Boşta Süzülme (CRANE LOAD PATH VIOLATION)
- **Tanım:** Ağır yapı elemanlarının (beton bloklar, tonluk kirişler) vinç halatlarına veya kaldırma aparatlarına bağlanmadan havada süzülerek taşınması.
- **Etkilenen Mercekler:** `⑧ YÖNTEM`, `⑩ SEBEP`, `⑫ KATILIK`
- **Etkilenen Filmler:** `BEFORE_NIGHTFALL`, `BUILT_FROM_DUST`, `OVER_THE_WALL`, `ONE_MORE_TURN`, `THE_DARK_ROCK` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `BEFORE_NIGHTFALL_2_INSA_QA_HAM.md`: `"5 LOAD PATH -> Ⓥ 0/10"`
  - `BUILT_FROM_DUST_2_INSA_QA_HAM.md`: `"5 LOAD PATH -> 2Ⓥ/10"`

---

### 🔴 F09: Kapak Vaadi ile Final Kare Uyuşmazlığı (COVER VS FINAL BEAT MISMATCH)
- **Tanım:** Kapak kartında sergilenen tamamlanmış görkemli yapının, filmin en son karesinde henüz bitmemiş olması veya kapaktaki mimari formla uyuşmaması.
- **Etkilenen Mercekler:** `④ TESLİM`
- **Etkilenen Filmler:** `THE_DUST_YEAR`, `BUILT_FROM_DUST`, `THE_LONG_SHADOW`, `BEFORE_NIGHTFALL` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `THE_DUST_YEAR_TESLIM_HAM.md`: `"4 TESLİM -> 2.1/10 (Final frame shows less than 30% of structure promised on cover)"`
  - `BUILT_FROM_DUST_TESLIM_HAM.md`: `"4 TESLİM -> 2.5/10 (Promised finished fortress remains a pile of rubble)"`

---

### 🟢 F10: Filigran ve Yapay Zeka Metin Sızıntısı (TEXT & BRANDING LEAK)
- **Tanım:** Yapay zeka görsel üreticilerinin veri setlerinden sızan bozuk metinler, harf benzeri izler veya köşelerdeki filigran bulanıklıkları.
- **Etkilenen Mercekler:** `① KARE`, `④ TESLİM`
- **Etkilenen Filmler:** `BUILT_FROM_DUST`, `ONE_MORE_TURN`, `THE_DARK_ROCK`, `OVER_THE_WALL` vb.
- **Ham Rapordan Kanıt Alıntıları:**
  - `BUILT_FROM_DUST_1_KARE_QA_HAM.md`: `"TEXT AND BRANDING -> 2/10 (Watermark artifact visible in bottom right corner)"`
