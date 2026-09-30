# 🧾 THE_IRON_BRIDGE — QA + DERS HASADI

> **Girdi:** Dersler.md'nin bu filme düşen kilitleri.
> **Çıktı:** aşağıdaki üç tablo — her satırı `04_UYARI_NOTLARI.md` ile `00_SAHNE_TABLOSU.md`
> içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.**

---

## 1. 🔒 DERS KİLİTLERİ

| ders | ölçülmüş arıza (tek cümle) | bu filmde kilit cümlesi | hangi sahnelere / karelere düşecek |
|---|---|---|---|
| 1 | Değişmezlere GEÇİCİ ekipman yazıldı | Destek kuleleri (S3–S10) ve kutu perde (S5–S7) DEĞİŞMEZLER'e GİRMEZ — SITE TEXTURE'a girer, SÖKÜM satırında takip edilir | S3·S4·S5·S10 görsel + I2V |
| 3 | Ters timelapse kancası vaat dışı | S0 AÇILIŞ: ağaç kesimi + geçici yol açma — iş başlıyor, köprü gelmemiş henüz | S0 I2V MOTION FOCUS |
| 4 | Kapak kartı sahne sayıldı | TESLİM YAPISI: SAHNE BLOĞU 12 × 10,0 s / KAPAK KARTI 1 × 5,0 s ayrı beyan | PLAN + QA_SPEC |
| 5 | Ters inşa yapılmazsa her klip başka yapı | G12 usta kare önce → I2V geriye G11 → G0; her I2V iki kareye kilitli | tüm üretim zinciri |
| 7 | Kar tek sahnede başlayıp bitemez | Bu film Nisan–Temmuz arası; KAR YOK. Mevsim taşıyıcısı yaprak rengi + nehir seviyesi | S0–S11 mevsim sütunu |
| 13 | Hız kesme sıklığı değil kesme varyansı | 12 × 10,0 s DÜZ IZGARA (sahip beyanı); ritmi klip içindeki değişim büyüklüğü taşır | PLAN + BOLUM_1/2 |
| 18 | Hareket kuralı görsel promptta işe yaramıyor | TIME RATE yalnız I2V MOTION FOCUS'a yazılır; gölge süpürmesi + nehir hareketi + işçi blur | tüm I2V |
| 19 | Sayısız bible bible değildir | Köprü boyutları (40 m açıklık, 8 m kemer H, 2,4 m tabliye) her bible satırında SAYI ile | PLAN DEĞİŞMEZLER |
| 20 | Blok etiketi sözleşmedir | ### 📸 GÖRSEL ve ### 🎥 I2V etiketleri birebir — kapı bunları sayar | BOLUM_1 + BOLUM_2 |
| 21 | Mevsim değişimi GİDEN klibin içinde hazırlanır | S4→S5 geçişi: yapraklar sararmaya başlıyor S4'ün SON saniyelerinde; S5 açılışında tamamen sarı | G4→G5 I2V |
| 25 | Kanıt nesnesi zincirsiz ölür | Kanıt nesnesi: büyük meşe ağacı (sol kıyı · %x 12–20 · ≈200 px) — her zincirde ELLE ✓/✗ | üretim günlüğü |
| 28 | Üretim günlüğü yoksa QA arızayı adlandıramaz | THE_IRON_BRIDGE_URETIM_GUNLUGU.md araç kapısından başlar | üretim öncesi |
| 33 | "Yok" yazılan özne var oldu | İşçiler VAR; "workers move as blurred traces only" — asla "no workers" | tüm I2V ACTIVITY |
| 35 | Metin yasağı HER yüzeyi kapsar | Köprü kirişi, korkuluk tüpü, beton ankraj yüzeyi, geçici kule gövdesi → no text on any surface | negatif çekirdek |
| 36 | STRUCTURE bloğu yalnız o sahnede ayakta olanı tarif eder | Her görsel promptta AT THIS STAGE: o karedeki köprü durumu + eleman yüzdesi | tüm görsel promptlar |
| 48 | Malzeme şantiyede yoktan var olamaz | Çelik kemer parçaları nereden geliyor: S3'ten itibaren sol kıyı geçici deposunda istiflenir, vinçle alınır | G3·G4·G5·G7·G8 |
| 51 | İki "deck" varsa makine hazır olana gider | Bu filmde TEK tabliye; ama nehir yüzeyi + tabliye iki yatay yüzey → nehir yüzeyi AYIRT EDİLİR yazılır | tüm görsel + I2V |
| 52 | Kesme iki şeyi birden değiştiremez | Tek istasyon — istasyon değişikliği yok; ama BÖLÜM SINIRI G6'da ışık + yapı yüzdesi ATLAMAZ | G6 bölüm sınırı |
| 54 | Nehir yatağındaki ilk kaldırma SU HAVUZU okundu | G0–G2 kuru nehir yatağında kutu perde kurulumu: "the riverbed is dry and sandy, no standing water" | G0·G1·G2·G3 görsel |
| 55 | Korpusu çoğul olan yapı çoğalır | "bridge" korpusu depoda çok köprü doğurdu (THE CLOSING SPAN tecrübesi); "one single pedestrian footbridge … the only crossing visible" | tüm görsel + I2V |
| 57 | Uzun rijit yük havada taşınmaz | Kemer parçaları (IPE profil, ~8 m) geçici destek üzerinde OTURUR — havada asılı değil; I2V'de "rests on the temporary support tower" | G4·G5·G7·G8 I2V |

---

## 2. 🏗️ YAPI KARTI KİLİTLERİ — Köprü (§3)

| kart maddesi | bu filmde uygulaması |
|---|---|
| Orta açıklık kapanışı filmin FİNAL VURUŞUDUR | S8 = son konsolun kaynaklandığı sahne — AYRI sahne, başka aşamayla birleştirilemez |
| Model konsolu havada yüzen tabliye çizer | Her promptta yük yolu: "supported continuously back to the anchor block via the steel arch above" |
| Tabliye iki yakadan ortaya ilerler | Her karede tabliye yüzdesi sayıyla: %0 (G0) → %25 (G4) → ... → %100 (G9) |
| Mevsim KÖPRÜ kartında güçlü | Yaprak döngüsü S0 yaz yeşili → S5 sonbahar → S6 kış çıplak dal → S11 yaz yeşili (yeni) |

---

## 3. 🧠 DEVRALINAN VARSAYIMLAR (araştırmadan · A kodu)

| kod | varsayım | kaynak |
|---|---|---|
| A3-c | Aynı kamera açısı + aynı kanıt nesnesi zinciri, izleyicinin "aynı yer" güvenini kurar | THE CLOSING SPAN ⑤ 9/10 vs MOUNTAIN DOOR ⑤ 0,2/10 |
| A6-a | Nehir yüzeyi bir mevsim taşıyıcısıdır: renk + seviye + hız (yaz=mavi+düşük · kış=kahve+taşkın) | araştırma; ölçülmedi |
| A8-c | Orta açıklık kapanışı için ayrı sahne ve ayrı usta kare hazırlanır | köprü timelapse analizi |
