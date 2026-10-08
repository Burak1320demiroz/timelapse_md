# 📉 Mercek Bazlı Başarısızlık ve Puan Sıralaması

> **Kapsam:** `QA/HAM_RAPORLAR/` dizinindeki 15 dikey filmden elde edilen 132 adet ham raporun (130 puanlı + 2 INC) mercek bazında puan sıralaması, istatistiksel dağılımı ve en düşük puanlı merceklerin derinlemesine analizi.

---

## 1. Merceklerin Genel Puan Sıralaması (En Düşükten En Yükseğe)

Sistemdeki 12 QA merceği, filmler genelindeki ortalama puanlarına göre sıralanmıştır. Puanı 5.0'ın altında kalan 7 mercek **"Kritik Zafiyet Bölgesi"** olarak tanımlanmaktadır.

```
[KRİTİK ZAFİYET BÖLGESİ - 5.0 Altı]
1. ② İNŞA         ███████░░░░░░░░░░  3.83 / 10  (15 Film - En Düşük Ortalama)
2. ⑩ SEBEP        ████████░░░░░░░░░  4.24 / 10  (5 Değerlendirilen Film - %80 Başarısızlık)
3. ⑧ YÖNTEM       ████████░░░░░░░░░  4.25 / 10  (11 Film - 3 Adet 0.0 Puan Çöküşü)
4. ⑤ DEVAMLILIK   ████████░░░░░░░░░  4.32 / 10  (13 Film - Geometrik ve Eleman Kaymaları)
5. ④ TESLİM       █████████░░░░░░░░  4.58 / 10  (14 Film - Vaat/Bedel Dengesi İhlalleri)
6. ① KARE         █████████░░░░░░░░  4.65 / 10  (15 Film - Titreme ve Kadraj Kayması)
7. ⑦ İŞ           █████████░░░░░░░░  4.69 / 10  (11 Film - Durdurulmuş/Atıl Şantiye)

[ORTA / YÜKSEK BÖLGE - 5.0 Üstü]
8. ③ ZAMAN        ██████████░░░░░░░  5.18 / 10  (15 Film - Güneş Saati Kaymaları)
9. ⑥ GEÇİŞ        ███████████░░░░░░  5.85 / 10  (13 Film - Metronomik Kesme Riski)
10. ⑫ KATILIK     ██████████████░░░  7.04 / 10  (5 Film - Yük Yolu ve Fizik Sadakati)
11. ⑨ FAALİYET    ███████████████░░  7.67 / 10  (8 Film - Sahne İçi Hareketlilik)
12. ⑪ ENVANTER    ████████████████░  8.42 / 10  (5 Film - En Yüksek Ortalama)
```

---

## 2. İstatistiksel Dağılım Matrisi

Merceklerin aldığı puanlar 3 kritik seviyede sınıflandırılmıştır:
- **Kritik Çöküş `[0.0 - 3.0]`:** Ağır fizik/inşa ihlali, telafisi olmayan üretim hatası.
- **Orta Derece `(3.0 - 6.0]`:** Kısmi tutarsızlıklar, uyarı düzeyindeki kusurlar.
- **Başarılı `(6.0 - 10.0]`:** Şartnameye ve fiziğe uygun, kabul edilebilir kalite.

| Mercek | Değerlendirilen Film | Kritik Çöküş [0 - 3.0] | Orta Seviye (3.0 - 6.0] | Başarılı (> 6.0) | Başarısızlık Oranı (< 4.0) |
|---|---|---|---|---|---|
| **② İNŞA** | 15 | 7 Film (%46.7) | 4 Film (%26.7) | 4 Film (%26.7) | **%60.0 (9/15)** |
| **⑩ SEBEP** | 5 | 2 Film (%40.0) | 2 Film (%40.0) | 1 Film (%20.0) | **%80.0 (4/5)** |
| **⑧ YÖNTEM** | 11 | 6 Film (%54.5) | 1 Film (%9.1) | 4 Film (%36.4) | **%54.5 (6/11)** |
| **⑤ DEVAMLILIK** | 13 | 4 Film (%30.8) | 6 Film (%46.2) | 3 Film (%23.1) | **%46.2 (6/13)** |
| **④ TESLİM** | 14 | 4 Film (%28.6) | 7 Film (%50.0) | 3 Film (%21.4) | **%35.7 (5/14)** |
| **① KARE** | 15 | 5 Film (%33.3) | 5 Film (%33.3) | 5 Film (%33.3) | **%40.0 (6/15)** |
| **⑦ İŞ** | 11 | 2 Film (%18.2) | 6 Film (%54.5) | 3 Film (%27.3) | **%54.5 (6/11)** |
| **③ ZAMAN** | 15 | 2 Film (%13.3) | 9 Film (%60.0) | 4 Film (%26.7) | **%26.7 (4/15)** |
| **⑥ GEÇİŞ** | 13 | 2 Film (%15.4) | 4 Film (%30.8) | 7 Film (%53.8) | **%23.1 (3/13)** |
| **⑫ KATILIK** | 5 | 1 Film (%20.0) | 0 Film (%0.0) | 4 Film (%80.0) | **%20.0 (1/5)** |
| **⑨ FAALİYET** | 8 | 0 Film (%0.0) | 2 Film (%25.0) | 6 Film (%75.0) | **%12.5 (1/8)** |
| **⑪ ENVANTER** | 5 | 0 Film (%0.0) | 0 Film (%0.0) | 5 Film (%100.0) | **%0.0 (0/5)** |

---

## 3. En Düşük Puanlı 5 Merceğin Derinlemesine Analizi

### 🚨 1. Mercek: ② İNŞA (Ort: 3.83 / 10 — Başarısızlık Oranı: %60.0)
Sistemdeki **en kronik çöküş noktasıdır**. 15 filmin 9'u 4.0 altında puan almış, `THE_CLOSING_SPAN` filmi 0.0 puan alarak tam çöküş yaşamıştır.

**Kök Nedenler:**
1. **Ara Hâl (%25 / %50 / %75) Eksikliği:** Görsellerde bir yapının temeli atılmadan doğrudan kolonların bitmiş olarak belirmesi veya çatının havada asılı kalması.
2. **Geometrik Şekil Değiştirme (AI Morphing):** Beton veya çelik elemanların inşa edilmek yerine "sıvı gibi büyüyerek/genleşerek" form değiştirmesi.
3. **Mantar Yapılaşması (Spontaneous Emergence):** Sahada hiçbir vinç veya döşeme kalıbı yokken katların bir sonraki karede aniden belirivermesi.

---

### 🚨 2. Mercek: ⑩ SEBEP (Ort: 4.24 / 10 — Başarısızlık Oranı: %80.0)
Değerlendirilen 5 filmin 4'ü geçer not alamamıştır (`OVER_THE_WALL`: 1.3, `ONE_MORE_TURN`: 3.0, `THE_DARK_ROCK`: 3.8, `THE_EMPTY_RIDGE`: 3.8).

**Kök Nedenler:**
1. **"Sihirli Belirme" (MAGIC VERDICT):** Elemanların sahaya geliş, kaldırılma veya montaj nedeni promptta beyan edilmediği için nesnelerin boşluktan belirmesi.
2. **Ekipman-Nesne Bağlantısızlığı:** Kule vincin kancası boş dururken veya sahadaki vinç başka yöne bakarken ağaç kütüklerinin veya çelik makasların kendi kendine yerine yerleşmesi.

---

### 🚨 3. Mercek: ⑧ YÖNTEM (Ort: 4.25 / 10 — Başarısızlık Oranı: %54.5)
`BUILT_FROM_DUST`, `OVER_THE_WALL` ve `THE_DUST_YEAR` filmleri **0.0/10** alarak tam sıfırlanmıştır.

**Kök Nedenler:**
1. **İnşa Fiziğinin İhlali:** Taş binaların harçsız yükselmesi, çelik yapıların birleşim birimlerinin (cıvata/kaynak) gösterilmemesi.
2. **Kendi Kendine Montaj (Self-Assembly):** Malzemelerin insan veya iş makinesi müdahalesi olmadan sahada birleşmesi.
3. **Prompt Mantıksızlığı:** Promptta inşa yönteminin (örneğin preform panel montajı veya dökme beton) teknik terimlerle tanımlanmaması.

---

### 🚨 4. Mercek: ⑤ DEVAMLILIK (Ort: 4.32 / 10 — Başarısızlık Oranı: %46.2)
13 filmin 6'sı 4.0 altındadır (`THE_CLOSING_SPAN`: 0.0, `THE_MOUNTAIN_DOOR`: 0.2, `BUILT_FROM_DUST`: 1.6).

**Kök Nedenler:**
1. **Çapa Nesne Kaybolması (Anchor Loss):** Sahneden sahneye geçerken arka plandaki dağ, yol veya komşu binaların konum ve şekil değiştirmesi.
2. **Kamera Açı Sapması:** Sabit istasyon olarak beyan edilen kameralarda açı ve odak uzaklığının (focal length) sahneler arasında kayması.
3. **Renk ve Doku Sapması:** Aynı ahşap veya taş malzemenin iki kare arasında renk değiştirmesi.

---

### 🚨 5. Mercek: ④ TESLİM (Ort: 4.58 / 10 — Başarısızlık Oranı: %35.7)
14 filmin 5'i başarısız olmuştur (`THE_DUST_YEAR`: 2.1, `BUILT_FROM_DUST`: 2.5, `THE_LONG_SHADOW`: 2.7).

**Kök Nedenler:**
1. **Kapağın İçe Dağılmaması:** Kapakta vaat edilen görkemli yapının film içerisinde hiçbir sahnede tam inşa edilmemesi (Bedel ödenmemesi).
2. **Eksik Final Vuruşu (Final Beat Failure):** Filmin son karesinin inşa edilmiş yapıyı sergilemek yerine belirsiz bir aşamada kesilmesi.
3. **Karakter / Metin İhlali:** Kurgu sırasında vaat edilen hikaye çizgisinin sahne geçişlerinde kopması.
