# 📊 15 Film × 12 Mercek Tam Skor Matrisi

> **Kapsam:** Depodaki `QA/HAM_RAPORLAR/` dizininde bulunan 15 dikey shorts filminin 132 adet ham QA raporunun (130 puanlı + 2 INC) tamamından derlenmiş skor matrisidir.
> ⚠️ **132 kayıt = 15 filmin 12 mercekte tekrar okunmasıdır; 132 bağımsız deney DEĞİLDİR.** Aynı film aynı olayı birden çok mercekte tekrar puanlanır; mercek oranları birbirinden bağımsız sayılmaz. Sayılar `python3 araclar/capraz_sayim.py` ile bu tablodan yeniden hesaplanır.

---

## 1. Genişletilmiş Çapraz Puan Matrisi

Aşağıdaki tabloda her filmin 12 QA merceğinden aldığı `AVERAGE` puanlar yer almaktadır. 
- **`-`**: İlgili film için o mercekte rapor üretilmemiştir.
- **`INC` (Run Incomplete):** Rapor başlatılmış ancak gerekli şartname (`_QA_SPEC.md`) veya plana erişilemediği için değerlendirme puanı üretilmemiştir (Mod V pre-pass).
- **`Ort.`:** Filmin mevcut raporları üzerinden hesaplanan aritmetik ortalamasıdır.

| Film Başlığı | Rapor | ① KARE | ② İNŞA | ③ ZAMAN | ④ TESLİM | ⑤ DEVAMLILIK | ⑥ GEÇİŞ | ⑦ İŞ | ⑧ YÖNTEM | ⑨ FAALİYET | ⑩ SEBEP | ⑪ ENVANTER | ⑫ KATILIK | Film Ort. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **BEFORE_NIGHTFALL** | 8 | 5.6 | 2.1 | 4.2 | 2.8 | 3.2 | 5.4 | 3.7 | 2.5 | - | - | - | - | **3.69** |
| **BUILT_FROM_DUST** | 10 | 1.1 | 2.8 | 3.3 | 2.5 | 1.6 | 4.5 | 1.8 | 0.0 | 3.5 | INC | - | - | **2.34** |
| **ONE_MORE_TURN** | 12 | 7.5 | 6.4 | 6.9 | 5.0 | 5.3 | 5.9 | 3.9 | 6.2 | 7.3 | 3.0 | 6.3 | 7.1 | **5.90** |
| **OVER_THE_WALL** | 12 | 5.8 | 3.8 | 6.0 | 5.3 | 3.0 | 7.0 | 3.8 | 0.0 | 7.5 | 1.3 | 9.3 | 6.8 | **4.97** |
| **POLAR_HABITAT** | 10 | 7.7 | 10.0 | 9.8 | 7.1 | 10.0 | 6.3 | 7.9 | 10.0 | 10.0 | INC | - | - | **8.76** |
| **THE_CLOSING_SPAN** | 6 | 1.0 | 0.0 | 1.3 | 5.4 | 0.0 | 1.6 | - | - | - | - | - | - | **1.55** |
| **THE_CROSSING** | 6 | 8.4 | 6.4 | 10.0 | - | - | - | 8.8 | 2.8 | 10.0 | - | - | - | **7.73** |
| **THE_DARK_ROCK** | 12 | 4.9 | 3.8 | 2.8 | 6.1 | 3.1 | 2.9 | 5.1 | 4.5 | 4.3 | 3.8 | 7.5 | 2.4 | **4.27** |
| **THE_DUST_YEAR** | 8 | 1.3 | 0.9 | 4.0 | 2.1 | 4.0 | 6.6 | 1.3 | 0.0 | - | - | - | - | **2.52** |
| **THE_EMPTY_RIDGE** | 12 | 2.8 | 5.2 | 5.4 | 3.4 | 7.2 | 7.6 | 7.0 | 9.1 | 8.8 | 3.8 | 9.0 | 8.9 | **6.52** |
| **THE_LONG_DAY** | 8 | 6.4 | 6.2 | 7.0 | 4.8 | 5.8 | 7.7 | 4.4 | 3.0 | - | - | - | - | **5.66** |
| **THE_LONG_SHADOW** | 4 | 3.3 | 0.4 | 4.3 | 2.7 | - | - | - | - | - | - | - | - | **2.67** |
| **THE_MOUNTAIN_DOOR** | 6 | 1.1 | 1.5 | 3.6 | 4.0 | 0.2 | 3.5 | - | - | - | - | - | - | **2.32** |
| **THE_NARROW_LOT** | 6 | 6.0 | 2.6 | 4.2 | 4.4 | 5.6 | 8.2 | - | - | - | - | - | - | **5.17** |
| **THE_OLD_ROAD** | 12 | 6.8 | 5.3 | 4.9 | 8.5 | 7.1 | 8.9 | 3.9 | 8.6 | 10.0 | 9.3 | 10.0 | 10.0 | **7.77** |
| **GENEL ORTALAMA** | **132** | **4.65** | **3.83** | **5.18** | **4.58** | **4.32** | **5.85** | **4.69** | **4.25** | **7.67** | **4.24** | **8.42** | **7.04** | **4.79** |

---

## 2. Mercek Bazlı Özet Veriler

| Mercek | Değerlendirilen Film | Geçerli Puanlı Film | Ortalama | Minimum Puan (Film) | Maksimum Puan (Film) | Başarısızlık Oranı (< 4.0) |
|---|---|---|---|---|---|---|
| **① KARE** | 15 | 15 | **4.65** | 1.0 (THE_CLOSING_SPAN) | 8.4 (THE_CROSSING) | %40.0 (6/15) |
| **② İNŞA** | 15 | 15 | **3.83** | 0.0 (THE_CLOSING_SPAN) | 10.0 (POLAR_HABITAT) | **%60.0 (9/15)** |
| **③ ZAMAN** | 15 | 15 | **5.18** | 1.3 (THE_CLOSING_SPAN) | 10.0 (THE_CROSSING) | %26.7 (4/15) |
| **④ TESLİM** | 14 | 14 | **4.58** | 2.1 (THE_DUST_YEAR) | 8.5 (THE_OLD_ROAD) | %35.7 (5/14) |
| **⑤ DEVAMLILIK** | 13 | 13 | **4.32** | 0.0 (THE_CLOSING_SPAN) | 10.0 (POLAR_HABITAT) | %46.2 (6/13) |
| **⑥ GEÇİŞ** | 13 | 13 | **5.85** | 1.6 (THE_CLOSING_SPAN) | 8.9 (THE_OLD_ROAD) | %23.1 (3/13) |
| **⑦ İŞ** | 11 | 11 | **4.69** | 1.3 (THE_DUST_YEAR) | 8.8 (THE_CROSSING) | %54.5 (6/11) |
| **⑧ YÖNTEM** | 11 | 11 | **4.25** | 0.0 (3 film) | 10.0 (POLAR_HABITAT) | %54.5 (6/11) |
| **⑨ FAALİYET** | 8 | 8 | **7.67** | 3.5 (BUILT_FROM_DUST) | 10.0 (3 film) | %12.5 (1/8) |
| **⑩ SEBEP** | 7 | 5 (2 INC) | **4.24** | 1.3 (OVER_THE_WALL) | 9.3 (THE_OLD_ROAD) | **%80.0 (4/5)** — yalnız 5 puanlı film |
| **⑪ ENVANTER** | 5 | 5 | **8.42** | 6.3 (ONE_MORE_TURN) | 10.0 (THE_OLD_ROAD) | %0.0 (0/5) |
| **⑫ KATILIK** | 5 | 5 | **7.04** | 2.4 (THE_DARK_ROCK) | 10.0 (THE_OLD_ROAD) | %20.0 (1/5) |

---

## 3. Filmlerin Üretim Nesli Dağılımı ve Gelişim Seyri

Filmler depoya ekleniş tarihlerine ve uygulanan denetim derinliğine göre 4 ana grupta toplanır:

1. **İkinci Kuşak İlk Dönem (4 Raporlu / 6 Raporlu Filmler):**
   - `THE_LONG_SHADOW` (4 rapor - Ort: 2.67), `THE_CLOSING_SPAN` (6 rapor - Ort: 1.55), `THE_MOUNTAIN_DOOR` (6 rapor - Ort: 2.32), `THE_NARROW_LOT` (6 rapor - Ort: 5.17), `THE_CROSSING` (6 rapor - Ort: 7.73).
   - Bu filmlerde yalnızca ilk 6 temel mercek (veya belirli alt kümeler) koşturulmuştur.
2. **Sekiz Mercek Kuşağı (8 Raporlu Filmler):**
   - `BEFORE_NIGHTFALL` (Ort: 3.69), `THE_DUST_YEAR` (Ort: 2.52), `THE_LONG_DAY` (Ort: 5.66).
   - Temel 6 merceğe ilave olarak `⑦ İŞ` ve `⑧ YÖNTEM` mercekleri uygulanmıştır.
3. **On Mercek Kuşağı (10 Raporlu Filmler):**
   - `BUILT_FROM_DUST` (Ort: 2.34), `POLAR_HABITAT` (Ort: 8.76).
   - `⑨ FAALİYET` ve `⑩ SEBEP` mercekleri eklenmiştir.
4. **On İki Mercek Kuşağı (12 Raporlu Tam Set Filmler):**
   - `ONE_MORE_TURN` (Ort: 5.90), `OVER_THE_WALL` (Ort: 4.97), `THE_DARK_ROCK` (Ort: 4.27), `THE_EMPTY_RIDGE` (Ort: 6.52), `THE_OLD_ROAD` (Ort: 7.77).
   - Sistemdeki 12 QA merceğinin tamamıyla denetlenen en gelişmiş ve eksiksiz film grubudur.

---

## 4. Matris Bulgularının Kısa Notları

1. **En Başarılı Film:** `POLAR_HABITAT` (8.76 Ortalama — ⚠️ 3 mercek eksik: SEBEP INC, ENVANTER ve KATILIK koşulmadı; kesin başarı standardı olarak kullanılmaz). Nedeni: Önceden üretilmiş prefabrik modüllerin doğrudan kurulması, minimal insan müdahalesi ve kar taşıyıcısının gücü.
2. **En Düşük Puanlı Film:** `THE_CLOSING_SPAN` (1.55 Ortalama). Nedeni: Köprü kapanış segmentinde geometrik kırılma, kameranın 0.0 alması ve devamsızlık çöküşü.
3. **En Stabil Mercek:** `⑪ ENVANTER` (8.42 Ortalama). Sahada kullanılan makine ve araçların varlığı görsellerde yüksek oranda tespit edilebilmektedir.
