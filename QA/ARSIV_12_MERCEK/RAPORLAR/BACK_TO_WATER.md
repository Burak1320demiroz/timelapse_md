# 🔍 BACK TO WATER — QA RAPORU

```
FİLM          BACK TO WATER — Kuru Havuz & Tekne Restorasyonu
TARIH         20.09.2026
DURUM         ⭐ ON İKİ MERCEK EKSİKSİZ KOŞULDU (① KARE - ⑫ KATILIK)
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|:---:|---|---|
| **① KARE** | V (33 kare) | **5,8**/10 Ⓥ | ✅ TIME-LAPSE · ⛔ End Card DIFFERENT | Kamera kilidi 7/10 · Ufuk %79,8 tuttu · Klip 3 kule açı kayması · Bitiş kartında metin ve farklı tekne |
| **② İNŞA** | D | **9,3**/10 | ✅ SAME · BUILT · ⛔ End Card DIFFERENT | `BACK TO WATER — QA SPEC` ile Mod D koşuldu · Aşamalar birebir · Sac sapanla indi · Suyla kalkış +1.8m tam |
| **③ ZAMAN** | V | **9,4**/10 Ⓥ | ✅ PASSES · ⛔ End Card DIFFERENT | Zaman tahmini "10–12 saat" planı (07:00-17:10) TUTTU · Rejim G 1x akış doğrulandı |
| **④ TESLİM** | ⛔ V | *belgesiz* (ham 7,1) | ⚠️ ENDS · COST/FINAL BEAT PASS (9/10) | Plan ve kapak verilmedi · ⭐ ONE THING BULUNDU · Tekne çıkışı varış sağladı · LOOP 3/10 |
| **⑤ DEVAMLILIK** | ⛔ V karesiz | *karesiz* (ham 9,7) | ✅ SAME WORLD · ⛔ End Card DIFFERENT | Kare grabı verilmedi · ⭐ Kanıt: Beton kuleler + sarı merdiven · Dikiş 9 (00:18) ekipman ani kaybolma |
| **⑥ GEÇİŞ** | ⛔ V | *belgesiz* (ham 9,9) | ✅ TIME · ⭐ RHYTHM | Plan ve ses verilmedi · 14 kesme, kusursuz 1.7–2.0s ritim · Taşıyıcı kesme: 00:20.5 (su dolumu) |
| **⑦ İŞ** | ⚠️ V karesiz | **10,0**/10 Ⓥ | ✅ WORKING | Depoda ilk 10,0 tam iş skoru · Boş aralık: 0.0s (%0) · Kimsenin yapmadığı büyüme: NONE |
| **⑧ YÖNTEM** | ⛔ V | *belgesiz* (ham 9,2) | ⛔ APPEARED · 7/8 MADE | Plan/SPEC verilmedi · İlk beliren parça: Cabin window glazing (00:16.5) · En iyi yapılan: Steel patch plates |
| **⑨ FAALİYET** | ⚠️ V karesiz | **10,0**/10 Ⓥ | ✅ PRODUCTIVE WORK | Tüm makine ve insan hareketleri doğrudan fiziksel iş içeriyor · Amaçsız eylem: NONE FOUND |
| **⑩ SEBEP** | D | **9,8**/10 | ✅ CAUSED BY LABOUR | SPEC tedarik edildi · Nedensel bağ 10/10 · Sihirli görünüm: NONE FOUND · İşgücü ölçeği tam |
| **⑪ ENVANTER** | ⛔ V | **9,3**/10 Ⓥ | ⛔ INTRUDERS | Plan verilmedi · Hasarlı gövde, vinç, boyalar tam davetli · Davetsiz tek unsur: Bitiş kartı (Klip 9) |
| **⑫ KATILIK** | ⛔ V karesiz | **5,5**/10 Ⓥ | ⛔ MELTING | Kare grabı verilmedi · En kötü eriyen: Kamyon ve güverte yükleri (00:09.5 fade) · Vinç biçim esnemesi |

---

## 2. 🚨 EN AĞIR ÜÇ BULGU

1. **[TÜM MERCEKLER / End Card Uyumsuzluğu — 00:28.0 - 00:32.0]:** Film boyunca kuru havuzdaki teknenin restorasyonu yüksek tutarlılıkla korunmuşken (⑤ SAME WORLD, ② SAME·BUILT, ⑪ CAST), 00:28.0'daki bitiş kartında beton kuru havuz yerine raylı kızak (slipway) ve bambaşka bir tekne profili gelmiştir. Üstte büyük boyutlu "BACK TO WATER" metni sızmıştır. ⑪ ENVANTER merceği bunu "The Most Damaging Intruder" ilan etmiştir. `BACK_TO_WATER_QA_SPEC` §1'de `KAPAK KARTI YOK · LOGO YOK · film tekne uzaklaşırken kesilir` kuralı mevcuttur.
2. **[⑫ KATILIK / Body Melting — 00:07.1 - 00:09.5]:** Rıhtımdaki kamyon, vinç yükleri ve güvertedeki çuvallar fiziksel taşıma olmadan opaklık değişimi ve erime (fade/split-merge) ile yer değiştirmiştir. Vinç bomu eklem mekanizması yerine elastik form esnemesi sergilemiştir.
3. **[⑧ YÖNTEM / Cabin Window Glazing — 00:16.5]:** 8 elemanın 7'si kusursuz şekilde inşa edilmişken (sac montajı, kaynak, astar, boyalar, halatlar, su basması, kapı kayması), kabin camları (5 adet cam) montaj süreci ekranda gösterilmeksizin 00:15.5 → 00:16.5 dikişinde aniden bitmiş olarak belirmiştir (`APPEARED`).

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

### ⑤ DEVAMLILIK QA Soruları:
1. **00:27.8'deki bitiş kartı görseli ikincil bir kızak tesisinden veya stok medyadan mı temin edilmiştir?**
   - *Cevap:* **Evet, stok/harici bir görseldir.** Planda bitiş kartı yer almamaktadır (`KAPAK KARTI YOK`). Kurguya sonradan eklenen kart, filmin geçtiği kuru havuz sahasına ait değildir.
2. **00:18.0'da havuz dolumu öncesi makaslı platform ve boya varillerinin kaldırılması zaman atlama temposu için kasıtlı olarak mı kesilmiştir?**
   - *Cevap:* **Hayır.** Planda Sahne 4'te platform ve varillerin rampa üzerinden havuzdan çıkarılması ve havuz tabanının süpürülmesi beyan edilmiştir (`platform ← rampa · sprey ← rampa · hortum ← rampa`). Bu çıkış eyleminin gösterilmeyip dikiş arasında ekipmanların birdenbire kaybolması bir üretim dikiş hatasıdır.
3. **00:18.0'daki duvara dayalı sarı seyyar merdiven dolum öncesi şantiye hazırlık prosedürünün bir parçası mıdır?**
   - *Cevap:* **Hayır.** Plandaki onaylı sarı merdiven, sağ (doğu) duvara sabitlenmiş 20 basamaklı nirengi merdivenidir (`sarı merdiven x %70,7`). Sol duvara dayalı seyyar merdiven planda yoktur; modelin "son işçi merdivenden rıhtıma çıkar" talimatını görselleştirirken ürettiği prompt dışı bir nesnedir.

### ⑦ İŞ QA Soruları:
1. **Aşama merdiveni Klip 1 (0:00.0) ile Klip 2 (0:03.5) arasındaki raspa/yüzey hazırlığı süresini tanımlıyor mu?**
   - *Cevap:* **Evet.** Planda S0 (07:00–07:10, Rejim A, 10 dk) yüksek basınçlı su yıkaması, S1 (07:10–09:10, Rejim B, 2 saat) mekanik söküm ve kumlama/raspalama olarak ayrı ayrı tanımlanmıştır.
2. **Klip 3'teki (0:06.8) vinç operasyonu sac levha için tek hamlelik kaldırma olarak mı planlandı?**
   - *Cevap:* **Evet.** SPEC §4'te `S2: levha SAPANLA iner — iki sapan, tek düşey kablo, kanca yüklü; kamyon doğu rıhtımında, bom havuz üstünde` şeklinde tek operasyon olarak kilitlenmiştir.
3. **Klip 6'daki (0:19.5) havuz dolumu kapı açılışından önce kesintisiz tek akış olarak mı tanımlandı?**
   - *Cevap:* **Evet.** SPEC §4 ve §5'te suyun menfezlerden dolarak tabanı ve basamakları sırayla örtmesi, seviye denizle eşitlenince kapının kayması kesin sıralamayla verilmiştir (`dolum → kalkış → eşitlenme → kapı`).

### ⑨ FAALİYET QA Soruları:
1. **Klip 1'de tabanda görünen makaslı platform sonraki gövde erişimi için mi konuşlandırılmıştır?**
   - *Cevap:* **Evet.** Planda G0'da kıçta makaslı platform yer alır; model yıkama ve raspalama için platformu tabanda aktif iş istasyonu olarak tutmuştur.
2. **0:20.0 - 0:23.5 arasındaki havuz dolum hızı planlanan vana dolum debisini yansıtıyor mu?**
   - *Cevap:* **Evet.** 2 saatlik Rejim B dolum süreci, 8 saniyelik sahnede suyun kademeli yükselişiyle orantılı olarak aktarılmıştır.

### ⑫ KATILIK QA Soruları:
1. **Klip 5'teki kamyonun rıhtıma gelişi ve yüklerin boşaltılma süreci üretim planında adım adım tanımlanmış mıdır?**
   - *Cevap:* **Evet.** SPEC §3 ve §4'te kamyonun S2'de doğu rıhtımında levhayı indirdiği, moloz çuvallarını kasaya aldığı ve S2 içinde sağdan çıktığı tanımlanmıştır. Ekranda görülen kütle erimesi/opaklık zıplaması AI difüzyon modelinin kütle koruma sınırından kaynaklanmaktadır.
2. **Klip 4'teki çelik levhanın vinçle indirilmesi esnasında kullanılan sapan bağlantısı plan dökümanında mevcut mudur?**
   - *Cevap:* **Evet.** SPEC §4'te `levha SAPANLA iner — iki sapan, tek düşey kablo, kanca yüklü` ve SPEC §3 G2'de `levha A SAPANDA` kuralı kilitlenmiştir.
3. **Klip 8'deki havuz dolum hızı ve teknenin kaldırma kuvvetiyle yükselişi kurallara uygun hedeflenmiş midir?**
   - *Cevap:* **Evet.** SPEC §4 ve §5'te suyun menfezlerden dolarak tabanı örtmesi ve tekne su hattına ulaşınca omurga takozlarından +1.8 m yükselmesi tanımlanmıştır.

---

## 4. 📋 OLAY TABLOSU (EVENT LEDGER)

| Olay No | Zaman Kodu | Etkilenen Mercekler | Olay Tanımı | Karar |
|:---:|:---:|:---:|---|---|
| **E01** | `00:28.0` | ①, ②, ③, ④, ⑤, ⑪ | **Bitiş Kartı Sapması (The Most Damaging Intruder):** Ana kuru havuz ve tekne yerine raylı çekek yeri (slipway) ve farklı tekne içeren, üzerinde büyük metin olan statik kart gelmesi. | **KURGU DÜZELTME:** 00:28.0 sonrası bitiş kartı kesilip atılacak; video tekne uzaklaşırken (00:27.5–00:28.0) plana uygun olarak sonlanacak. |
| **E02** | `00:16.5` | ⑧ | **Kabin Camlarının Aniden Belirmesi:** 5 adet pencere camının montaj süreci (taşıma, vantuzla takma, fitil) gösterilmeden sert kesmeyle bitmiş olarak belirmesi. | **KABUL / GELECEK PLAN:** İlk geçiş için kabul edilebilir (7/8 MADE, ortalama 9.2); revizyonda S4 promptunda cam montaj fiili güçlendirilecek. |
| **E03** | `00:18.0` | ⑤ | **Ekipman Kaybolması (Dikiş 9):** Makaslı platform ve varillerin tahliye eylemi gösterilmeden yok olması; sol duvarda sahte seyyar merdiven türemesi. | **KABUL:** ⑤ skoru 9.7 ve SAME WORLD korunduğu için kritik kırıcı değildir. |
| **E04** | `00:07–00:10`| ⑫ | **Kamyon ve Yük Erimesi (Melting Body):** Rıhtımdaki kamyon ve güverte yüklerinin katı kütle transferi yerine fade/merge ile yer değiştirmesi, vinç eklem bükülmesi. | **KABUL:** ⑩ SEBEP merceği işgücü bağını (9.8/10) doğruladığı için AI difüzyon kütle esnemesi mevcut sürüm için tolere edilir. |
