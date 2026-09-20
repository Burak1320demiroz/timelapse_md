# 🔍 BACK TO WATER — QA RAPORU

```
FİLM          BACK TO WATER — Kuru Havuz & Tekne Restorasyonu
TARIH         20.09.2026
DURUM         ⏳ QA SÜRÜYOR (İlk 3 Mercek İşlendi: ① KARE · ② İNŞA · ③ ZAMAN)
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|:---:|---|---|
| **① KARE** | V (33 kare) | **5,8**/10 Ⓥ | ✅ TIME-LAPSE · ⛔ End Card DIFFERENT | Kamera kilidi 7/10 · Ufuk %79,8 tuttu · Klip 3 kule açı kayması · Bitiş kartında metin ve farklı tekne |
| **② İNŞA** | D | **9,3**/10 | ✅ SAME · BUILT · ⛔ End Card DIFFERENT | `BACK TO WATER — QA SPEC` ile Mod D koşuldu · Aşamalar birebir · Sac sapanla indi · Suyla kalkış +1.8m tam |
| **③ ZAMAN** | V | **9,4**/10 Ⓥ | ✅ PASSES · ⛔ End Card DIFFERENT | Zaman tahmini "10–12 saat" planı (07:00-17:10) TUTTU · Rejim G 1x akış doğrulandı |
| **④ TESLİM** | — | — | *bekleniyor* | — |
| **⑤ DEVAMLILIK** | — | — | *bekleniyor* | — |
| **⑥ GEÇİŞ** | — | — | *bekleniyor* | — |
| **⑦ İŞ** | — | — | *bekleniyor* | — |
| **⑧ YÖNTEM** | — | — | *bekleniyor* | — |

---

## 2. 🚨 EN AĞIR ÜÇ BULGU

1. **[TÜM MERCEKLER / End Card Uyumsuzluğu — 00:28.0 - 00:32.0]:** Film boyunca kuru havuzdaki teknenin restorasyonu başarıyla korunmuşken, 00:28.0'daki bitiş kartında beton kuru havuz yerine raylı kızak (slipway) ve bambaşka bir tekne profili gelmiştir. Ayrıca üstte büyük boyutlu "BACK TO WATER" metni sızmıştır. Oysa `BACK_TO_WATER_QA_SPEC` §1'de `KAPAK KARTI YOK · LOGO YOK · film tekne uzaklaşırken kesilir` kuralı kesin olarak belirtilmiştir.
2. **[① KARE / Surface Truth (00:14.0) & People (00:01.0)]:** Gövde boyama aşamasında sentetik/dijital pürüzsüzlük hissi belirgindir (5/10). Klip 1'de yıkama yapan işçi time-lapse hareket izi yerine pozlanmış net bir figür olarak çıkmıştır.
3. **[① KARE / Station Identity & Camera Lock (00:08.0)]:** Klip 3 başlangıcında kuru havuz kapı kulelerinin dikey hizalarında hafif açısal kayma tespit edilmiştir.

---

## 3. ❓ DOKÜMAN SORULARININ CEVAPLARI (QUESTIONS FOR THE DOCUMENT)

### ① KARE QA Soruları:
1. **Ufuk çizgisinin %79,8 seviyesinde sabit kalması hedeflenmiş midir?**
   - *Cevap:* **Evet.** `BACK_TO_WATER_QA_SPEC` §2'de `deniz ufku (y) %79,8 · tam yatay ±0,5 puan · SEKİZ KAREDE DE` şartı yazılıdır. Rapordaki ölçüm tablosunda ufuk %79,5 ile %80,0 arasında kalarak tolerans (±0,5) içinde mükemmel şekilde kilitlenmiştir.
2. **Bitiş kartındaki görselin (00:28) ana sahnelerdeki tekneden farklı olması planlanan bir durum mudur?**
   - *Cevap:* **Hayır.** Planda ve SPEC §1 / §Künye'de `KAPAK KARTI YOK · LOGO YOK · 56,0'da film tekne UZAKLAŞIRKEN kesilir; sonrasında kart, logo, fade YOK` yazılıdır. Bitiş kartı hem plan dışıdır hem de farklı bir tesis/tekne göstermektedir.

### ③ ZAMAN QA Soruları:
1. **S0–S5 sahnelerindeki yüksek zaman sıkıştırma oranı ile S6 sahnesindeki 1x gerçek zamanlı çıkış çekimi arasındaki hız değişimi prodüksiyon planıyla tam uyumlu mudur?**
   - *Cevap:* **Evet.** Planda ve SPEC §Künye'de `REJİM: S0 A (10 dk) · S1–S5 B (2 sa) · S6 ⭐ G gerçek zaman 1×` olarak beyan edilmiştir. S6 sahnesindeki akıcı gerçek zaman akışı bilinçli ve planlı bir rejim seçimidir.
2. **Bitiş kartında (00:28.0) ana çekim lokasyonundan farklı bir kızak (slipway) görselinin tercih edilmesi grafik tasarım standartları açısından beyan edilmiş bir sapma mıdır?**
   - *Cevap:* **Hayır.** Bitiş kartı planda beyan edilmemiştir (`KAPAK KARTI YOK`). Eğer kapak görseli kullanılacaksa da kural gereği son sahnenin usta karesinden (G7) türetilmelidir; farklı bir kızak tesisi kullanılması kural ihlalidir.
3. **Çekim aralıklarındaki gölge ilerlemeleri, sahne planında hedeflenen 2 saatlik blok saatleriyle (07:00 → 17:10) birebir örtüşmekte midir?**
   - *Cevap:* **Evet.** SPEC §Künye'de sahne saatleri `07:00 → 07:10 → 09:10 → 11:10 → 13:10 → 15:10 → 17:10` olarak verilmiştir (yaklaşık 10 saatlik tek gün döngüsü). Modelin filmden çıkardığı `yaklaşık 10–12 saat (sabah 07:00'den 17:00'ye)` tahmini planlanan güneş yayıyla tam olarak örtüşmüştür (TUTTU).
