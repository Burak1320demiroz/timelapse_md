# 🧾 THE_GLASS_WALL — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — her satırı `04_UYARI_NOTLARI.md` ile `00_SAHNE_TABLOSU.md`
> içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.**

---

## 1. 🔒 DERS KİLİTLERİ — `kilavuzlar/DERSLER.md` ölçülmüş derslerden bu filme düşenler

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.

| ders | ölçülmüş arıza (tek cümle) | bu filmde kilit cümlesi | hangi sahnelere / karelere düşecek |
|---|---|---|---|
| 1 | Değişmezlere GEÇİCİ ekipman yazıldı | Koruma iskelesi (S5–S7) ve sarnıç şakülü (S0–S3) DEĞİŞMEZLER'e GİRMEZ — SITE TEXTURE bloğuna girer ve SÖKÜM satırında takip edilir | S5·S6·S7 görsel + I2V |
| 3 | Ters timelapse kancası vaat dışı | S0 AÇILIŞ sahnesi: maki budanıyor + sarnıç kazısı başlıyor — ilk iki saniye iş başlıyor | S0 I2V |
| 4 | Kapak kartı sahne sayıldı | TESLİM YAPISI: SAHNE BLOĞU 12 × 10,0 s = 120,0 s / KAPAK KARTI 1 × 5,0 s — QA_SPEC künyesinde SCENE BLOCK / END CARD ayrı | PLAN + QA_SPEC |
| 5 | Ters inşa yapılmazsa her klip başka bir yapı | G12 usta kare önce üretilir → image-to-image geriye G11 → G0; I2V her iki onaylı kareye kilitli | tüm üretim zinciri |
| 7 | Kar tek sahnede başlayıp bitemez | Bu film Mart–Ekim arası → KAR YOK. Mevsim taşıyıcısı ot rengi (yeşil→sarı→kahve→yeşil) ve deniz rengi | S0–S11 mevsim sütunu |
| 13 | Hız kesme sıklığı değil kesme varyansı | 12 × 10,0 s DÜZ IZGARA (sahip beyanı) — karşı kayıt ve kabul edilen risk PLAN §DÜZ IZGARA BEYANI'na yazılır; ritmi klip içindeki değişim büyüklüğü taşır | PLAN + BOLUM_1/2 |
| 18 | Hareket kuralı görsel promptta işe yaramıyor | TIME RATE (gölge süpürmesi, makine hareketi) yalnız I2V MOTION FOCUS paragrafına yazılır | tüm I2V promptları |
| 19 | Sayısız bible, bible değildir | Sera boyutları (24 × 10 m, h 5,5 m), ev boyutları (8 × 6 m), teras duvarı yüksekliği (0,9 m) her bible satırında SAYI ile | PLAN DEĞİŞMEZLER |
| 20 | Blok etiketi sözleşmedir | ### 📸 GÖRSEL ve ### 🎥 I2V etiketleri birebir — kapı bunları sayar | BOLUM_1 + BOLUM_2 |
| 22 | Kanca → ters I2V kanca + kaldırma yok | Bu filmde KULE VİNCİ YOK — cam panel vakumlu kaldırıcı (vacuum lifter) + el ile montaj; kaldırma riskinden muaf | — |
| 25 | Kanıt nesnesi zincirsiz ölür | Kanıt nesnesi: zeytin ağacı (sol · %x 8–15 · ≈180 px) — her zincir koşusunda elle ✓/✗ | üretim günlüğü |
| 28 | Üretim günlüğü yoksa QA arızayı adlandıramaz | THE_GLASS_WALL_URETIM_GUNLUGU.md ilk satır = araç kapısı; sonra klip başına tek satır | üretim öncesi açılmalı |
| 33 | "Yok" yazılan özne var oldu | İnsan yok ama ARAÇLAR VAR: cam montajcılar bulanık hareket çizgisi olarak yazılır — asla "no workers" yazılmaz; "workers move as blurred traces only" | tüm I2V ACTIVITY |
| 35 | Metin yasağı HER yüzeyi kapsar | İskele borusu, cam kenar etiketi, çiftlik evi kapı tabelası, sera oluğu üretici etiketi → "no text on any surface" negatif çekirdekte | negatif çekirdek |
| 36 | STRUCTURE bloğu yalnız o sahnede ayakta olanı tarif eder | Her görsel promptta "AT THIS STAGE" cümlesi: sadece o karedeki yapı durumu — "when finished this will be…" sadece bir kez, giriş cümlesi olarak | tüm görsel promptlar |
| 48 | Malzeme şantiyede yoktan var olamaz | Cam paneller nereden geliyor: şantiye kenarında yatay paletlerde istiflenir, birer birer vakumla alınır — kaynak G5'ten itibaren kadrajın kenarında | G5·G6·G7·G8 + I2V |
| 52 | Kesme iki şeyi birden değiştiremez | DEĞİŞMEZLER 1 numarası: istasyon değişen kesmede (varsa) yapı yüzdesi sabit — bu filmde tek istasyon, sorun yok; ama BÖLÜM SINIRI G6'da ışık ve yapı aynı yüzdede olmalı | G6 kapısı |
| 55 | Korpusu çoğul olan yapı çoğalır | "greenhouse" modelde çiftlik anlamına gelir ve model birden çok sera + ev çizer → "one steel-framed greenhouse … the only greenhouse on this hillside, every other ridge is bare scrubland" | tüm görsel + I2V |
| 57 | Uzun rijit yük havada taşınmaz | Cam panel kaldırma: panel palete yaslanır, vakum kaldırıcı tutulur, klip sonunda MONTAJ TAMAMLANMIŞ gösterilir — havada asılı panel sahnesi YOK | G6·G7·G8 I2V |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `QA/RAPORLAR/` + `QA/00_INDEX.md`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_MOUNTAIN_CROWN | ⑩ SEBEP | EKSİLTMELİ oyma: 8 elemandan 5'i MAGIC — modelin eksiltme yapamaması | Bu film ADDİTİF: her sahne eleman EKLER. Eksileme yok — muaf |
| THE_MOUNTAIN_CROWN | ⑤ DEVAMLILIK | Dikiş ihlali — istasyon 5,6/10 | Deniz ufuku + zeytin ağacı her karede sabit yüzde — sayıyla kilitleniyor |
| THE_EMPTY_RIDGE | ② İNŞA | HAYALET KULE kopyaları — çoğalma 0:21 ve 0:39 | "the only greenhouse on this hillside" + SAYIM testi araç kapısında |
| THE_EMPTY_RIDGE | ⑩ SEBEP | Segment · nasel · kanat kancasız pop — MAGIC × 3 | Cam panel havada asılı sahnesi YOK; panel palete yaslanır + vakum tutuşu |
| THE_LAST_HARBOR | ⑪ ENVANTER | 6 nesne sayıldı; liste QA_SPEC §7'de — her karede o listeye karşı okundu | Kadrajdaki nesne listesi QA_SPEC §7'ye yazılır: sera, ev, teras, zeytin, kayalık, deniz ufuku |
| THE_QUIET_FIELD | ① KARE | Başlık bindirmesi: üst %40 → Safe Area 8/10 | Kapak kartı sadece 120,0–125,0 s arası; S11 tutuşuna metin bindirmesi yok |
| THE_GLASS_CROSSING | — | ⛔ VİNÇ İHLALİ | Bu filmde kule vinci yok — cam panel vakumla montaj; vinç ihlali riski ortadan kalkar |

---

## 3. 📎 DEVRALINAN / DIŞ OKUMA VARSAYIMLARI — `DERSLER.md` D-x · A/P-x

| kod | varsayım | bu filmde nerede sınanacak |
|---|---|---|
| D-f | Kural kaldırmadan önce alternatif ölçülür | Geçici iskele → SITE TEXTURE bloğu (DERS 1 geçici/kalıcı ayrımı); ilk koşuda ① ANCHOR IDENTITY ölçüm |
| A4-a | Mevsim taşıyıcısı adlandırılabilir nesne | Ot rengi + deniz rengi; mevsim sütunu her sahne dolu olacak — ③ ZAMAN ölçer |
| A6-d | ACTIVITY iki hareket eden + bir yüzey kanıtı | Her I2V'de: cam montajcı (blurred) + araç (el kamyonu / vinç iş makinesi) + yüzey kanıtı (toprak / cam kenar / taş yüzey) | 
| C1-c | I2V'ye MOTION FOCUS paragrafı | Her I2V sonunda 3–4 cümle: ① malzeme nerede · ② hangi taşıyıcı · ③ nereye oturuyor · ④ ne değişti | 
| P1-c | Takvim sahadan okunur, ışıktan değil | Mertebe cümlesi: "approximately eight months, from early spring to late autumn" | 

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        19 adet
QA ARIZASI:         7 adet
VARSAYIM:           5 adet
⛔ EN PAHALI ÜÇÜ:   DERS 55 (çoğalma) · DERS 48 (malzeme kaynağı) · DERS 57 (cam panel kaldırma)
```
