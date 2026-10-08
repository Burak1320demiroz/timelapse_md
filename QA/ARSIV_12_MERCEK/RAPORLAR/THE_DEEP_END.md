# 🔍 THE DEEP END — QA RAPORU

```
FİLM          THE DEEP END — atıl yüzme havuzu → açık hava amfi sineması dönüşümü (7 × 8,0 sn = 56,0 sn)
TARİH         24.09.2026
DURUM         ⭐ ÜRETİLDİ VE TÜM ON İKİ MERCEK TAMAMLANDI (12/12)!
              ⭐ YEDİ TANE 10/10 KUSURSUZ TAM PUAN:
                 ② İNŞA 10,0/10 (Mod D) — SAME · BUILT (Sıfır hata "No defects found", 6 nirengide %0,0 sapma)
                 ③ ZAMAN 10,0/10 Ⓥ (Mod V) — PASSES (12 saatlik tek gün diurnal güneş yayı ve gölge süpürmesi kusursuz)
                 ⑤ DEVAMLILIK 10,0/10 Ⓥ (Mod V) — SAME WORLD (0/6 dikiş kusuru, krom korkuluk nirengi kanıtı)
                 ⑧ YÖNTEM 10,0/10 (Mod D) — MADE (10/10 yapı elemanı sıfırdan yapıldı, ilk beliren: NONE)
                 ⑩ SEBEP 10,0/10 (Mod D) — CAUSED BY LABOUR (Sihirli beliren: NONE FOUND, tam işçi nedenselliği)
                 ⑪ ENVANTER 10,0/10 Ⓥ (Mod V) — INVITED (Zararlı davetsiz misafir: NONE FOUND)
                 ⑫ KATILIK 10,0/10 Ⓥ (Mod V) — SOLID (Eriyen gövde: NONE FOUND, rijit kenar ve kütle tam)
              ⭐ BEŞ ADET 9,0+ ÜST DÜZEY SKOR:
                 ④ TESLİM 9,9/10 (Mod D) — ENDS · ⭐ FINAL BEAT PASS (10/10) (0:54.0 doruk kanıtı eksiksiz)
                 ⑨ FAALİYET 9,75/10 Ⓥ (Mod V) — PRODUCTIVE WORK (Amaçsız aktivite: NONE FOUND)
                 ① KARE 9,6/10 Ⓥ (Mod V) — TIME-LAPSE (Kamera/istasyon 10/10, zemin tilti tam kilit)
                 ⑥ GEÇİŞ 9,4/10 (Mod D) — TIME · ⚠️ METRONOME (0:48.0 Rejim B→G doruk geçişi, taşıyıcı kesme)
                 ⑦ İŞ 9,3/10 Ⓥ (Mod V) — WORKING (Nedensiz büyüme: NONE, Klip 6 teslimat geçişi 3.5 sn)
              ⭐ GENEL ORTALAMA: 9,83 / 10 (Deponun en yüksek genel skorlu üretimlerinden biri!)
              🚨 KURGU DÜZELTME NOTU:
                 00:56.0–01:00.0 arasına eklenen 4 saniyelik statik "THE DEEP END" başlık kartı kurguda atılmalıdır.
                 Film 56,0 sn'de figür oturmuşken sert kesilmelidir (SPEC §0 / §1 gereği).
HAM           QA/HAM_RAPORLAR/THE_DEEP_END/ — 12 dosya (1_KARE … 12_KATILIK)
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|---:|---|---|
| **① KARE** | V | **9,6**/10 Ⓥ | ✅ **TIME-LAPSE** | Kamera kilidi 10 · İstasyon 10 · Ankor 10 · Çerçeve kimliği 10 · Metin/Logo 10 · Gece 10 · Güvenli Alan 9 (yakın coping/basamaklar y %17-22 alt bant) · İnsan/Araç 7 (S6 doğal hızda net figür) |
| **② İNŞA** | D | **10,0**/10 | ✅ **SAME · BUILT** | **Kusursuz tam puan.** Sıfır hata ("No defects found") · 6 nirengide ölçek sapması %0,0 · Yük yolu, yapı kimliği, monoton büyüme, geçici ekipman tahliyesi tam |
| **③ ZAMAN** | V | **10,0**/10 Ⓥ | ✅ **PASSES** | **Kusursuz zaman koşusu.** Okunan süre: "one single day (morning to night, ~08:30 to 20:30)" plana DAKİKASINA KADAR TUTTU · Gölge süpürmesi 1:5.1 (11°) → 1:0.9 (48°) → 1:4.8 (12°) · Gün batımı ve alacakaranlık projektör/LED açılışı tam uyumlu |
| **④ TESLİM** | D | **9,9**/10 | ✅ **SONA ERİYOR (ENDS)** | ⭐ **FINAL BEAT PROOF: BAŞARILI (PASS — 10/10)**. 00:54.0'te perdede sakin deniz videosu, projektör huzmesi, basamak altı 4 amber LED çizgisi ve bankta oturan tek figür tam kilit koordinatlarında · 4 sn bitiş kartı ve döngü sıçraması (9/10) |
| **⑤ DEVAMLILIK** | V | **10,0**/10 Ⓥ | ✅ **SAME WORLD** | **Kusursuz tam puan.** 6/6 dikiş hatasız (0 defects) · Yakın basamak krom korkuluğu (00:00 ve 00:55) aynı dünyanın kanıtı · Tramplen, rampa ve malzeme akışı kesintisiz |
| **⑥ GEÇİŞ** | D | **9,4**/10 | ✅ **TIME · ⚠️ METRONOME** | 7/7 sert kesim (`HARD`, 10/10) · Sabit nirengi dayanımı 10/10 · Eşit süreler metronomik olsa da ⭐ **THE CUT THAT CARRIES: 00:48.0 Kesmesi** (Rejim B timelapse'den Rejim G doğal hıza geçiş ana vuruş) · Müziksiz diegetik ses yatağı |
| **⑦ İŞ** | V | **9,3**/10 Ⓥ | ✅ **WORKING** | ⭐ Kimsenin yapmadığı büyüme: NONE · Sahadaki 8 ilerleme olayının tamamı doğrudan işçi ve ekipmanların görünür çalışmasıyla gerçekleşti · Klip 6 teslimat geçişinde 3.5 sn boşluk (%43.8) |
| **⑧ YÖNTEM** | D | **10,0**/10 | ✅ **MADE · 10/10 MADE** | **Kusursuz tam puan.** 10 ana yapı elemanının tamamı sıfırdan yapıldı · ⭐ İlk beliren parça: NONE · En iyi parça: Ahşap Kademe Amfi Yapısı (plastik takozlar → kirişler → kaplama tahtaları → 4 kademe amfi) |
| **⑨ FAALİYET** | V | **9,75**/10 Ⓥ | ✅ **PRODUCTIVE WORK** | Rölanti 10 · Animasyon döngüsü 10 · İnsan emeği 10 · Amaçsız hareket 9 (00:38 el arabası manevrası) · ⭐ En amaçsız aktivite: NONE FOUND |
| **⑩ SEBEP** | D | **10,0**/10 | ✅ **CAUSED BY LABOUR** | **Kusursuz tam puan.** 15 yapı elemanının tamamı görünür insan emeği ve araçlarla taşındı, üretildi veya monte edildi · ⭐ Sihirli beliren: NONE FOUND |
| **⑪ ENVANTER** | V | **10,0**/10 Ⓥ | ✅ **INVITED** | **Kusursuz tam puan.** Klip 1–7 arasındaki tüm aletler, makineler, malzemeler ve yapay ışık kaynakları konut havuzu dünyasının mantığı içinde · Zararlı davetsiz misafir: NONE FOUND |
| **⑫ KATILIK** | V | **10,0**/10 Ⓥ | ✅ **SOLID** | **Kusursuz tam puan.** 11/11 kategori 10/10 · En kötü eriyen gövde: NONE FOUND · Havuz kütlesi, korkuluk, ahşap güverte, perde paneli ve ışık huzmesi rijitliğini milimetrik korudu |

---

## 2. ⛔ HÜKÜM OKUMA SIRASI

```
12 MERCEK HÜKÜMLERİNİN 12'Sİ DE TAM VE EKSİKSİZ GEÇTİ:
⑤ SAME WORLD (10,0/10 Ⓥ) ✅
⑧ MADE 10/10 (10,0/10) ✅
⑦ WORKING (9,3/10 Ⓥ) ✅
⑨ PRODUCTIVE WORK (9,75/10 Ⓥ) ✅
⑫ SOLID (10,0/10 Ⓥ) ✅
② SAME & BUILT (10,0/10) ✅
③ PASSES (10,0/10 Ⓥ) ✅
⑥ TIME · METRONOME (9,4/10) ✅
④ ENDS · FINAL BEAT PASS (9,9/10) ✅
① TIME-LAPSE (9,6/10 Ⓥ) ✅
⑩ CAUSED BY LABOUR (10,0/10) ✅
⑪ INVITED (10,0/10 Ⓥ) ✅

ANALİZ:
1. ŞANTİYE VE İNŞAAT FİZİĞİNDE TARİHİ BAŞARI (YEDİ TANE 10/10):
   - ② İNŞA: Sıfır kusur ("No defects found"), 6 nirengide %0,0 sapma.
   - ⑧ YÖNTEM & ⑩ SEBEP: 10/10 elemanın tamamı sahadaki işçilerin elleriyle, rampadan indirilerek ve vidalanarak inşa edildi. Sihirli belirme: SIFIR.
   - ⑫ KATILIK: Hiçbir gövde erimedi, deforme olmadı veya saydamlaşmadı.
   - ③ ZAMAN: 12 saatlik güneş yayı (08:30–20:30), gölge boyları (1:5.1 → 1:0.9 → 1:4.8) ve alacakaranlık açılışı kusursuz işlendi.
2. REJİM G VE FİNAL VURUŞU (④ 9,9 & ⑥ 9,4):
   - 00:48.0'de timelapse hızından 1× doğal hıza geçiş (Rejim G) filmin doruk noktası oldu.
   - 00:54.0 Final Beat Proof (perdede sakin deniz, projektör huzmesi, basamak altı amber LED hatları, tek figürün oturması) 10/10 tam puanla tescillendi.
3. KURGU EYLEMİ:
   - 00:56.0–01:00.0 arasına eklenen 4 saniyelik statik başlık kartı kurguda kesilmeli; video tam 56,0 sn'de figür oturmuşken sonlandırılmalıdır.
```

---

## 3. 🚨 EN AĞIR BULGULAR VE EYLEM PLANI

1. **[Şartname Dışı Bitiş Kartı — KESİLECEK]:**
   - *Bulgu:* 00:56.0–01:00.0 arasına "THE DEEP END" başlıklı statik kart eklenmiş; video süresi 60 sn'ye uzamıştır. SPEC §0 ve §1 gereğince filmde kapak kartı yoktur.
   - *Eylem:* Master video 00:56.0'da (figür oturmuş vaziyetteyken) sert kesilerek teslim edilecektir.
2. **[Klip 6 Sonu Teslimat Geçişi (00:44.5–00:48.0)]:**
   - *Bulgu:* 3.5 sn'lik durgunluk süresi (⑦ İŞ 9,3). Şantiye temizliği bittiği ve teslimata geçildiği için doğal bir duraklamadır, yeniden üretime gerek yoktur.
3. **[Alt Bant Güvenli Alanı (y %17–22)]:**
   - *Bulgu:* Sabit kameranın çukura bakan yüksek açısı (tilt −38°) nedeniyle yakın basamaklar alt güvenli alan bandına taşmaktadır. Zemin ailesi mimari perspektif gereği planlıdır.

---

## 4. ⏱️ ZAMAN TAHMİNİ

```
③ "TIME READ FROM THE FILM ALONE: one single day (morning to night, ~08:30 to 20:30)"
Taşıyıcı: Kesintisiz yönlü gölge süpürmesi (1:5.1 → 1:0.9 → 1:4.8), 00:37 gün batımı parlaması, 00:42 alacakaranlık ışık düşüşü ve gece projektör/LED huzmesi.
PLAN: 12 saat (08:30 G0 → 20:30 G6/G7).
✅ DAKİKASINA KADAR TAM TUTTU.
```

---

## 5. ❓ DOKÜMAN SORULARININ CEVAPLARI

### ① KARE
1. **Hedef Ufuk % ve Arka Plan Çit Yüksekliği:** SPEC §2 gereği Ufuk hattı %102,1 (Kadraj Dışı, tilt −38°). Arka plan bahçe duvarı/çiti %77,0 / %86,8 / %90,8 kilitlidir.
2. **Rejim G Geçişi (00:48–00:56):** Tamamen planlı ve beyanlıdır (SPEC §0 ve §7: S0–S5 Rejim B timelapse, S6 Rejim G 1× doğal hız).
3. **Net İnsan Figürü (S6):** Kasıtlı anlatı doruğudur (SPEC §1 ve §7). Figür basamaklardan iner ve oturur.
4. **Alt Güvenli Alan Taşması:** Sabit yüksek açılı kamera geometrisi gereği havuzun ön ucu alt banttadır; ana aksiyon ve dönüşüm havuz ortasında ve perdede güvenli alandadır.

### ③ ZAMAN
1. **Güneş Açıları (Azimut / Yükseklik):**
   - G0 (08:30): 100° / 11° | G1 (10:30): 123° / 32° | G2 (12:30): 157° / 48° (zenith) | G3 (14:30): 203° / 48° | G4 (16:30): 237° / 32° | G5 (18:30): 260° / 11° | G6–G7 (20:30): 280° / −11,4° (gece yapay aydınlatma).
2. **Takvim:** Çok günlük havuz restorasyonu 12 saatlik tek bir diurnal güneş yayına sıkıştırılmıştır (SPEC §0 beyanlı).
3. **Rejim G Süresi:** Tam olarak 8,0 saniyedir (0:48.0 – 0:56.0).

### ⑤ DEVAMLILIK
1. **İskele Rampası Kaldırılma Zamanı:** Klip 4'te değil, S5 içinde (G5'ten G6'ya geçerken, 0:40–0:48) ahşap taşımacılığı bittikten sonra sökülmüştür.
2. **Römorkun Sahada Kalması:** Hayır; G6 ve G7 akşam sekansında sahadan tamamen tahliye edilmiş ve teras süpürülmüştür.
3. **8 Saksının Sahaya Girişi:** Klip 5'te (0:32–0:40) ahşap kademeler tamamlandıktan sonra ince işler donatısı olarak yerleştirilmiştir.

### ⑦ İŞ & ⑨ FAALİYET
1. **Klip 6 Sonu - Klip 7 Başı Zaman Farkı:** S5 (18:30–20:30) ile S6 (20:30 açılışı) arasındaki zaman atlaması yaklaşık 2 saattir.
2. **Ahşap Malzeme Stok Sahası:** Evet, tüm larch kiriş ve tahtalar üst terasta istiflenip rampayla çukura indirilmiştir.
3. **Taban Harcı Kürlenme Süresi:** Çok günlük takvim tek güne sıkıştırıldığı için kürlenme süreci kesme aralığında geçilmiştir.
4. **Havuz Taban Drenaj Detayı:** Eski dip süzgeci korunmuş, paslanmaz ızgara ve menteşeli kapak yapılmıştır; karkas plastik takozlar üzerinde yükseltilerek serbest su tahliyesi sağlanmıştır.
5. **Aydınlatma Altyapı Entegrasyonu:** Eski havuz tesisatı ve kablo buatları ahşap karkas altındaki servis boşluğundan armatür ve projektöre bağlanmıştır.

### ⑫ KATILIK
1. **Tramplen Taşınması:** İki işçi tarafından sökülüp arka bahçe çimenine elle taşınması planlanmış ve uygulanmıştır.
2. **Bank ve Saksıların Niteliği:** 4 bank ahşap güverte karkasına vidalı sabit imalattır; 8 saksı coping ve güverte üzerine dizilmiş peyzaj elemanlarıdır.
3. **Beyaz Perde Paneli:** İki işçi tarafından rampadan yan çevrilerek indirilen 208 px boyutunda rijit tek paneldir.
4. **LED Hatlarının Sırayla Yanması:** Anlatı ritmi ve elektrik devre sırası gereği kademeli olarak açılması planlanmıştır.
