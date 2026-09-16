# 🔍 POLAR HABITAT — QA RAPORU

```
FİLM          POLAR HABITAT (THE POLAR DOME)
TARIH         10.09.2026
DURUM         ⭐ ÜRETİLDİ VE QA KOŞULDU (Sekiz Mercek Eksiksiz)
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|:---:|---|---|
| **① KARE** | V | **7,7**/10 Ⓥ | ✅ TIME-LAPSE | Bağlayıcı VERDICT · Safe Area & Bloom ihlalleri var |
| **② İNŞA** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 10,0) | ✅ SAME · BUILT | ⛔ SPEC verilmedi, Mod D koşusu TEKRARLANACAK |
| **③ ZAMAN** | V | **9,8**/10 Ⓥ | ✅ PASSES | Plan verilmediği için model Dünya mevsimi okudu |
| **④ TESLİM** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 7,1) | ⚠️ ENDS | ⛔ Plan verilmedi, COST/FINAL BEAT PASS (8/10) |
| **⑤ DEVAMLILIK** | V | **10,0**/10 Ⓥ | ✅ SAME WORLD | 0/18 kusurlu dikiş · Arka plan dağ sırtı piksel kilitli |
| **⑥ GEÇİŞ** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 6,3) | ✅ TIME · ⛔ METRONOM | ⛔ Plan/ses verilmedi · Düz ızgaranın meşru METRONOM riski |
| **⑦ İŞ** | V | **7,9**/10 Ⓥ | ✅ WORKING | Boş durmayan şantiye (en uzun boş aralık 5,0 sn %9,1) |
| **⑧ YÖNTEM** | ⛔ V | *belgesiz koşuldu — TEKRARLANACAK* (ham 10,0) | ✅ MADE | ⛔ SPEC verilmedi, 7/7 parçanın yapımı görünüyor |
| **⑨ AKTİVİTE** | V | **10,0**/10 Ⓥ | ✅ PRODUCTIVE WORK | Makine hareketleri gerçek iş içeriyor |
| **⑩ SEBEP** | ⛔ D | *belgesiz durdu — TEKRARLANACAK* | RUN INCOMPLETE | ⛔ SPEC verilmediği için Mod D kapısı durdu |

---

## 2. 🚨 EN AĞIR ÜÇ BULGU

1. **[① KARE / Surface Truth - 3/10]:** Yapay zeka modelinin 00:44-00:54 arasında merkez kule tepesinde prompt dışı sentetik mavi lazer ışını, çiçeğimsi bloom parıltıları ve CGI yıldırım arkı efektleri üretmesi.
2. **[① KARE / Safe Area - 4/10]:** Kazı ve temel işlemlerinin alt %25 güvenli alan sınırı içinde kalması (00:00) ve merkez kule/enerji ışınının üst %15 rezerv alanına taşması (00:33, 00:44).
3. **[① KARE / Text & Branding - 8/10 & Motion Streaks - 5/10]:** Otonom araçların gövdesinde logo benzeri kırmızı/siyah desen kaçakları ve hareket eden araçlarda zaman atlamalı bulanıklık (motion streaks) eksikliği.

---

## 3. ❓ DOKÜMAN SORULARININ CEVAPLARI (QUESTIONS FOR THE DOCUMENT)

### ① KARE QA Soruları:
1. **Mavi enerji ışını ve yıldırım efektleri (00:44–00:54) plana dahil miydi?**
   - *Cevap:* Hayır. Planda merkez geothermal kule tepesinde hafif cyan enerjisel parıltı ve buhar çıkışı yazılıdır; ancak model unprompted olarak fantezi bilimkurgu lazer ışını ve yıldırım arkları üretmiştir.
2. **Merkez kule için üst güvenli alan toleransları nedir?**
   - *Cevap:* Planda kule tepesi %68,0 frame yüksekliğine kilitlidir (y=614 px). Kule apexinin %88-95 seviyesine taşması kadraj yüksekliği spesifikasyonunun aşıldığını gösterir.
3. **Kule tepesindeki eleman fiziksel inşaat parçası mıdır?**
   - *Cevap:* Evet, planda 18m merkez geothermal kule ve 4 adet radyatör kanadı olarak tanımlanmıştır.

### ③ ZAMAN QA Soruları:
1. **Beyan edilen toplam inşaat takvim süresi nedir ve 12–14 aylık görünümle uyuşuyor mu?**
   - *Cevap:* Hayır. Film Dünya filmi değil, karlı bir uzay gezegeninde geçen **tek bir 10 saatlik gün** filmleridir (azimut 110° ➔ 210°). Mercek plansız (Mod V) koşulduğu için model kadrajdaki beyazlık ve çalı dokularını Dünya'daki ilkbahar-kış mevsim döngüsü (12-14 ay) olarak yanlış okumuştur.
2. **Güneş açıları pre-calculated mıdır?**
   - *Cevap:* Evet. Güneş azimut 110° ➔ 210°, yükseklik 14° ➔ 22° olarak plan §5'te derece derece hesaplanmıştır.
3. **Çekim aralıkları ve süreler nedir?**
   - *Cevap:* 6 sahne × 8,0 saniye = 48,0 sn (+ 5,0 sn kapak). Her klip 2 saatlik sıkıştırılmış süreyi temsil eder.

---

## 4. 🎯 KARAR VE EYLEM PLANI

1. **② İNŞA QA Koşusunun Tekrarı (DERS 17):** `POLAR_HABITAT_QA_SPEC.md` belgesi verilerek ② İNŞA merceği Mod D altında tekrar koşulmalıdır.
2. **Sci-Fi Bloom ve Logo Kaçaklarının Engellenmesi:** G5 ve G6 I2V promptlarında `no laser beams, no lightning arcs, no intense lens bloom` ve `no vehicle logos, no surface markings` olumsuz ifadeleri güçlendirilecektir.
3. **Safe Area Ayarlaması:** Merkez kule ve temel kazısı framing parametreleri güvenli alan zarfı (y=254 px ile y=1436 px arası) içinde kalacak şekilde I2V kilitlerinde netleştirilecektir.
