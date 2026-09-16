# 🔍 THE EMPTY RIDGE — QA RAPORU

```
FİLM          THE EMPTY RIDGE — çıplak ot sırtında rüzgâr türbini
TARİH         14.09.2026 (plan ve üretim aynı gün)
DURUM         ⛔ ÜRETİLDİ VE ON İKİ MERCEKLE ÖLÇÜLDÜ — ÜRETİM GÜNLÜĞÜ TUTULMADI (DURUM ⛔ BOŞ · DÖRDÜNCÜ film)
              ⛔ 12 merceğin 11'i RUN INCOMPLETE; yalnız ③ tam girdiyle koştu (tam kurgu), ① 37 kare aldı
              ⛔ Kurgu plana oturmuyor: ⑥ kesme listesi 4,9 · 8,5 · 14,8 · 21,8 · 31,8 · 39,9 · 47,8 · 55,8 →
                 8 klip (4,9·3,6·6,3·7,0·10,0·8,1·7,9·8,0) + kart ≈ 4,2 sn = 60,0. Plan: 7 × 8,0 + 5,0 = 61,0.
                 ① dört istasyon grubu saydı ve klip 1–2'de push-in; plan TEK sabit istasyon.
                 Hangi araç, hangi prompt, zincir koşuldu mu — BİLİNMİYOR [DERS 28].
HAM           QA/HAM_RAPORLAR/THE_EMPTY_RIDGE/ — 12 dosya, dokunulmaz
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|:---:|---|---|
| **① KARE** | V (37 kare) | **2,8**/10 Ⓥ | ⛔ SIX SEPARATE SHOTS | CAMERA LOCK 2 (klip 1–2 push-in, klip 4 tilt) · DÖRT istasyon grubu · ANCHOR 1 · SURFACE 1 · C1 CRANE 2 (halat yükten koptu 0:28–0:38) |
| **② İNŞA** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 5,2) | ⛔ DIFFERENT · ✅ **BUILT** | ilk kez DIFFERENT + BUILT: yapı yapılıyor ama 0:21 ve 0:39'da HAYALET KULE KOPYALARI; rotor montajda döndü; kanatlar kuleden geçti |
| **③ ZAMAN** | V (tam girdi) | **5,4**/10 | ✅ PASSES | okunan süre **"about 2 to 3 months"** — plan 9,5 hafta ✅ TUTTU · SEASON ORDER 7 · gölge donuk, bulut akıyor (1 · 5) · meşe sonbaharda yeşil (C4) |
| **④ TESLİM** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 3,4) | ⚠️ ENDS · COST/FINAL BEAT **FAIL** | belge verilmediği için FAIL yazdı; NONE FOUND (5. kez) · **RESISTANCE 2** — rüzgâr bekleyişi ekranda okunmadı · kapak verilmedi |
| **⑤ DEVAMLILIK** | ⛔ V karesiz | *karesiz — TEKRARLANACAK* (ham 7,2) | ✅ **SAME WORLD** | ⭐ kanıt nesnesi = **plana konan yalnız meşe** (00:00,5 ve 00:54,5) — planlı çapa İLK KEZ ⑤'te bulundu · 5/9 dikiş DEFECT (kopya kuleler · bom yok olur) |
| **⑥ GEÇİŞ** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 7,6) | ✅ TIME · ⭐ **RHYTHM** | kurgu varyanslı · üçüncü kez (CROSSING · OVER THE WALL · EMPTY RIDGE) · ANCHOR SURVIVAL 6 (istasyon kayması) |
| **⑦ İŞ** | ⛔ V karesiz | *karesiz — TEKRARLANACAK* (ham 7,0) | ✅ WORKING | CAUSE AND EFFECT 3 · GROWTH NOBODY MADE: 0:26,5 iki dik kule segmenti, kanca boş · en uzun boşluk klip 12 %70 (dönen türbin, bilinçli) |
| **⑧ YÖNTEM** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham **9,1**) | ✅ **MADE · 6/6** | deponun en yüksek ⑧ · FIRST PIECE APPEARED: NONE · en iyi parça: beton temel (donatı → döküm → ankraj) |
| **⑨ FAALİYET** | ⛔ V karesiz | ham 8,8 Ⓥ | ✅ PRODUCTIVE WORK | en amaçsız: asılı kanadın hızlı dönmesi (0:33,5) · köprü yok, ping-pong yok |
| **⑩ SEBEP** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 3,8) | ⛔ MAGICAL APPEARANCE | toprak + temel CAUSED (4/7) · segment · nasel · kanat MAGIC: "kanca boş ve bağlantısız" 0:21,5 · 0:30,5 · 0:42,5 |
| **⑪ ENVANTER** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 9,0) | ⛔ INTRUDERS | iki davetsiz: 0:21 iki şaft · 0:39 iki tam türbin; gelmeyen davetli YOK; insan yok 10/10 |
| **⑫ KATILIK** | ⛔ V karesiz | ham 8,9 Ⓥ | ✅ **SOLID** | deponun ilk SOLID'i · PASS-THROUGH 10 · BORN BY FADE 10 · LOAD PATH BODY 8 — halat gövde olarak tuttu |

```
⛔ MOD DENETİMİ [DERS 17]: ② ④ ⑥ ⑧ ⑩ ⑪ belgesiz — skorlar tabloya YAZILMADI. ⑤ ⑦ ⑨ ⑫ karesiz.
   qa_paket.sh koşulmadı; koşulamazdı — günlük boş [DERS 28 · 29]. SPEC ve plan üretimden ÖNCE hazırdı ve
   yine verilmedi [DERS 27 — dördüncü film].
⭐ END CARD: 12/12 SAME (DERS 30 ikinci kez bütün merceklerde). ⚠️ ① 5: kartın başlığı ÜST %12,5 bandında —
   KAPAK.md bandı %72–84 (alt kenardan) demişti; dizgi plana uymadı.
```

## 2. ⛔ HÜKÜM OKUMA SIRASI [kart R 6a]

```
⑤ SAME WORLD ✅ + ⑧ MADE ✅ → zincir hükümleri İLK KEZ İKİSİ BİRDEN TUTTU. Diğer skorlar yorumlanır.
Ama ① SIX SEPARATE SHOTS: kamera klip 1–2'de push-in, dört istasyon grubu, odak değişimi (geniş → tele).
Bu, ⑤'in "aynı dünya"sıyla çelişmez: dünya aynı (meşe + duvar + sıradağ), KAMERA aynı değil. Plan tek
sabit istasyon yazdı; üretim başka açılar ekledi [DERS 52 ikinci kez · DERS 23]. Günlük olmadığı için
sebep bilinmiyor.
② DIFFERENT'ın sebebi de yapı değil KOPYA: yapı BUILT, ama iki kez yanına hayalet kule geldi → DERS 55.
```

## 3. 🚨 EN AĞIR ÜÇ BULGU

1. **[② ⑤ ⑧ ⑪ — 0:21 ve 0:39 · HAYALET KULELER]** Alt segment yerleştirilirken temelin yanında iki dik şaft belirdi ve kayboldu (0:21 → 0:24); 0:39'da meranın üstünde iki TAM türbin belirdi ve bir kesme sonra yok oldu. Dört mercek birbirinden bağımsız aynı iki anı yazdı. Yapı tek yazılmıştı ("a single wind turbine", "one rigid steel structure") ve yine çoğaldı → **DERS 55** (korpusu çoğul olan yapı) · 0:21'deki şaftlar için ikinci mekanizma **DERS 57** (uzun rijit yük hedefte kopyalanır).
2. **[⑩ ⑦ ① — kaldırma anı kancasız]** Segment (0:21,5), nasel (0:30,5) ve kanatlar (0:42,5) yerine "pop" etti, vinç kancası o anda boş/bağlantısız; ① halatın yükten koptuğunu yazdı (0:28–0:38). Dağ arka planı (plan §Vinç kararı) halatı KURTARMADI — ama ⑧ C3 LIFTED-IN 9/10 ve ⑫ LOAD PATH 8/10: halat gövde olarak tuttu, model OTURTMA ANINI kancasız çizdi → DERS 22 hüküm notu + **DERS 57**.
3. **[② ⑦ ⑨ ⑩ — rotor montajda döndü]** Kanatlar takılırken rotor yüksek hızda döndü (0:33 → 0:42), kanatlar dönen göbeğe "sıçradı", kuleden geçti (② 8). Plan S5 I2V'sinde "the hub is turned one third of a turn on its own gear" yazıyordu — hareket fiili göbekten rotora sıçradı → **DERS 56**.

## 4. 🎞️ KURGU ↔ PLAN EŞLEMESİ — günlük yok, eşleme TAHMİNİDİR

| Film klibi (⑥) | Süre | Ekranda | Plandaki sahne | Not |
|:-:|---:|---|---|---|
| 1 | 0:00,0–0:04,9 | yol açılır, dozer + greyder (⛔ yerden, push-in) | S0 AÇAR (ilk yarı) | istasyon plan dışı |
| 2 | 0:04,9–0:08,5 | çukur kazılır (⛔ push-in) | S0 AÇAR (ikinci yarı) | istasyon plan dışı |
| 3 | 0:08,5–0:14,8 | donatı, mikser, pompa, temel | S1 DÖKER | ✅ ⑧ "en iyi yapılan parça" |
| 4 | 0:14,8–0:21,8 | pad, vinç parçaları, segmentler (⛔ vantaj değişir, tilt) | S1 sonu · S2 KURAR | bom kalkışı okunmadı; hayalet şaftlar 0:21 |
| 5 | 0:21,8–0:31,8 | segmentler, kule tam, nasel (10,0 s) | S2 · S3 · S4 | üç sahne tek klipte; rüzgâr bekleyişi YOK (④ RESISTANCE 2) |
| 6 | 0:31,8–0:39,9 | kanatlar (rotor dönerken), hayalet türbinler 0:39 | S5 TAKAR | DERS 56 · 55 |
| 7 | 0:39,9–0:47,8 | türbin döner, vinçler toplanır | S6 DÖNER (ilk yarı) | bom 0:48'de yok olur (⑤ 9) |
| 8 | 0:47,8–0:55,8 | boş pad, sürülmüş tarla, dönen türbin | S6 DÖNER (ikinci yarı) · G7 | ✅ final ekranda; meşe aynı |

## 5. ⏱️ ZAMAN TAHMİNİ [kart R 6]

```
③ "TIME READ FROM THE FILM ALONE: about 2 to 3 months (late summer through autumn)" — taşıyıcı: hasat,
sürüm, montaj aşamaları. PLAN: 9,5 hafta (Temmuz ortası → Eylül sonu), hedef "yaklaşık iki ay" [P1-c].
✅ TUTTU — tarla takvimi (altın → balya → sürüm) tek başına doğru mertebeyi taşıdı; kışsız yapıda ilk kez.
⛔ Tutmayan: gölge donuk (③ 1 · 5 — bulut akarken gölge sabit: DERS 32/47 DÖRDÜNCÜ kez), meşe yeşil kaldı
(plan: kenarları bronz — üretilmedi).
```

## 6. ❓ DOKÜMAN SORULARININ CEVAPLARI

### ① KARE
1. **Grup A–D koordinatları?** — Plan TEK istasyon: güney sırttaki kaya çıkıntısı, pad'in +100,0 m üstü, kule eksenine 320 m, bakış 350°, tilt 0°, 24 mm. **Grup A (yerden), B ve C planda YOK.** Grup D planın istasyonuna en yakın olan; onun bile ufku %62–67 (plan: göz çizgisi %50, sıradağ %57) ve 4,6 puan kaymış.
2. **Push-in planlı mı?** — Hayır. "bolted to a rock outcrop, absolutely zero movement", NEGATIVE ve I2V'de "the camera does not move at any point". Push-in araç ön ayarıdır [DERS 23] ya da klipler plandan üretilmedi; günlük yok.
3. **Çapa koruma şartı?** — Meşe 64 px · x ≈ 742 · %29–32, duvar ≈300 px, sıradağ silueti %57 — sekiz karede birebir; geniş/tele geçişi planda yok.
4. **Nasel üstündeki yazı?** — Planlı değil; NEGATIVE her yüzeyde metni yasaklar. DERS 35 tekrar.

### ③ ZAMAN
1. **Toplam süre?** — 9,5 hafta; ışık tek gün 06:00 → 20:00 (7 × rejim B).
2. **Klip 1 · 3 · 5 güneş açıları?** — Planın S0 · S2 · S4'ü: G0 06:00 az 63° / 8° · G2 10:00 az 108° / 48° · G4 14:00 az 210° / 66°; klip içinde 2 saat süpürme.
3. **Tarım takvimi?** — altın buğday (S0–S1) → biçim (S2) → anız + balya (S3) → balya toplanır (S4) → çıplak anız (S5) → sürülmüş (S6); Temmuz ortası → Eylül sonu.

### ⑤ DEVAMLILIK
1. **0:21'deki ek segmentler planlı depolama mı?** — Hayır. Segmentler pad'de **yatık**, takozlarda, sayım 4 → 0; temelin yanında dik duran hiçbir şey planda yok. Hayalet.
2. **0:39'daki türbinler komşu çiftlik mi?** — Hayır. Tek türbin; "the only turbine" kilidi bu ölçümden sonra yazıldı [DERS 55]. Davetsiz.
3. **Vinç sökümü?** — S6 (48,0–56,0): bom yere iner, parça parça çözülür, low-loader'lar yoldan çıkarır, paletli gövde son, yardımcı vinç sürülerek gider — hepsi ekranda. Filmde bom 0:48'de bir karede yok oldu.

### ⑦ İŞ
1. **Klip 7'de vinç kurulumu planlı mı?** — Evet: S2 "bom kendi vinciyle yerden kalkar, dağa karşı blur yay", sonra segment 1 kuyruklamayla. S3'te 2 · 3 · 4 "kısa sapanda düşey iz". Filmde bom kalkışı okunmadı, segmentler pop etti.
2. **İkiz kule → tek kule?** — Planda yok; tek kule, dört segment, sayım 3 → 0.
3. **Kanat montajı dönen göbekte mi?** — Hayır; ama planın S5 I2V'si "the hub is turned one third of a turn" yazdı → model rotoru döndürdü [DERS 56]. Plan cümlesi düzeltilecek.

### ⑨ FAALİYET
1. **Yol kenarındaki kamyonlar?** — Aktif: damper çakıl (S3), low-loader bom parçası (S2), servis kamyonu (S4–S6); "a parked truck stays sharp" tek park araç.
2. **Hasat takvimi?** — Biçerdöver S2 (vinç kurulurken), balya S3, römork S4, pulluk S6 — teslimatlarla eşzamanlı, plana yazılı.
3. **Vinç sökümü sırası?** — ⑤ 3 ile aynı; rotor vinç gittikten SONRA döner.

### ⑫ KATILIK
1. **0:33,5'teki dönüş?** — Planlı değil: rotor yalnız S6'da, üç kanat cıvatalandıktan ve vinç gittikten sonra döner. Kaynağı planın "hub turned one third" cümlesi [DERS 56].
2. **Yol kenarı kamyonlar statik mi?** — Hareket edenler renk izi (blur); tek park araç keskin (streak cümlesi).
3. **Toz?** — "dust drifts off the gravel behind the truck" (S2, S4, S6), S4'te "dust streams off the pad" — yazılıydı.

## 7. 🥁 IZGARA NOTU — proje sahibine ⚠️

```
Kurgu yine VARYANSLI: 4,9 · 3,6 · 6,3 · 7,0 · 10,0 · 8,1 · 7,9 · 8,0. ⑥: TIME · RHYTHM · CUT MECHANICS 10.
ÜÇÜNCÜ KEZ (CROSSING · OVER THE WALL · EMPTY RIDGE): anlam taşıyan kesme + varyanslı süre = RHYTHM.
⑥'nın tek düşük satırı ANCHOR SURVIVAL 6 — sebebi ızgara değil istasyon kayması (①).
Plan 7 × 8,0 düz; üretilen kurgu planı hiç kullanmadı. Karar proje sahibinin: düz kilit mi kalacak, yoksa
ölçülmüş üç RHYTHM'in ızgarası mı yazılacak. Plan DEĞİŞTİRİLMEDİ; DERS 44 notu güncellendi.
```

## 8. 📚 DERSLER — yeni, tutan, tekrar

```
YENİ  [kart D → DERSLER.md]
  DERS 55  ⭐ Korpusu ÇOĞUL olan yapı tek yazılsa da çoğalır (türbin → çiftlik): 0:39 iki hayalet türbin
  DERS 56  ⭐ Montajda "göbeği döndür" yazmak rotoru döndürür — hareket fiili parçadan yapıya sıçrar
  DERS 57  Uzun rijit yük havada taşınmaz: model hedefte kopyalar (0:21) ve oturtma anını kancasız çizer (⑩ ×3);
           dağ arka planı halatı kurtarmadı → DERS 22 mekanizma notu (kontrast değil, taşıma)
TUTAN (ilk kez)
  DERS 25  planlı kanıt nesnesi ⑤'te BULUNDU — meşe 00:00,5 ↔ 00:54,5 ✅ (MOUNTAIN DOOR'da kaya ölmüştü)
  DERS 53  dar yüzeyde tek araç → ⑫ SOLID · PASS-THROUGH 10/10 ✅ (OVER THE WALL'da 5/10 MELTING)
  DERS 48 · 36  ⑧ MADE 6/6 · 9,1 — parçalar yerde görüldü, sayıldı, sonra kalktı ✅ (deponun en yüksek ⑧)
  DERS 30  12/12 END CARD SAME ✅ · DERS 45  final aydınlık, dönen rotor ekranda ✅
  ③ zaman tahmini TUTTU (4. film: MOUNTAIN DOOR · NARROW LOT · DUST YEAR · EMPTY RIDGE)
TEKRAR (sayaç arttı)
  DERS 28  günlüksüz üretim — 4. kez · DERS 27 · 29  belgesiz/karesiz koşu — 11/12
  DERS 23 · 52  kamera hareketi + plan dışı istasyonlar (dört grup) — ① SIX SEPARATE SHOTS
  DERS 32 · 47  gölge donuk, bulut akıyor — 4. kez · DERS 34  SURFACE TRUTH 1 (plastik toprak, gölgesiz parçalar)
  DERS 35  nasel üstünde yazı · DERS 26 (zayıf)  meşe kenarı bronz üretilmedi
  ④ NONE FOUND — 5. kez (mod V) · ④ RESISTANCE 2 — rüzgâr bekleyişi EKRANDA okunmadı (ölçülemedi: klip yok)
```

## 9. 🎯 KARAR VE EYLEM PLANI

```
1. YAYINLANMAZ: ① SIX SEPARATE SHOTS (kamera hareketi + dört istasyon) · ② DIFFERENT (hayalet kuleler) ·
   ⑩ MAGIC. Ama bu, deponun ÖLÇÜLMÜŞ EN İYİ FİLMİ: ⑤ SAME WORLD + ⑧ MADE + ⑫ SOLID + ⑥ RHYTHM + ③ PASSES
   aynı anda — ilk kez.
2. YENİDEN ÜRETİLİR (yeniden YAZILMAZ) — plan tutuyor; düzeltilecek üç cümle:
   · S5 I2V: "hub is turned one third of a turn" → göbek KİLİTLİ, kanat sıradaki flanşa [DERS 56]
   · her AT THIS STAGE / SITE: "the only turbine on the ridge … every other crest bare" [DERS 55]
   · S2–S5 I2V: kaldırma yolu yerine G(n)'de yük hedefin üstünde asılı, klipte yalnız oturur [DERS 57]
   Önce ARAÇ KAPISI (⑨ vinç testi dâhil) + ÖN GÖRSELLEŞTİRME + GÜNLÜK. Tek istasyon; push-in yok.
3. Belgeli TEKRAR: ② ⑧ ⑩ ← QA_SPEC · ④ ⑥ ⑪ ← plan (+ kapak, + ses) · ⑤ ⑦ ⑨ ⑫ ← kare_al.sh.
4. Kapak dizgisi: başlık üst %12,5'te — KAPAK.md bandına (%72–84) çekilir.
5. Izgara kararı (§7) proje sahibine.
6. Kabul edilen kusur: klip 12'nin %70 "boşluğu" (dönen türbin, bilinçli tutuş) — kabul.
```
