# 🧠 THE_OLD_ROAD — KONSEPT VE RİSK

> Bu dosya PLAN'ın §KONSEPT KAPISI ve §DEĞİŞMEZLER kutularının TÜREDİĞİ yerdir.
> Buradaki her sayı plana ve QA_SPEC'e aynen taşınır; iki yerde farklı sayı = bir yerde yanlış sayı.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI

```
① FORMAT      yatay 16:9 · yatay_2_dk_filmler · ⛔ BANDIN DIŞI ızgara: 15 × 8,0 (modül 12 × 10,0)
              gerekçe: sahibin talebi (16.09.2026) — toplam süre aynı (120,0 + 5,0), kesme sayısı 11 → 14
② YAPI        beton kutu kesitli viyadük, İTME (incremental launching) yöntemiyle — yeni tip,
              YAPI_TIPI_KARTLARI §10 şablonu; §6 (yol/tünel) ve §3 (köprü) kartlarından uyarlandı
③ SAHA        dağ / eğim (SAHA_VE_IKLIM §3.4) + melez ormanı yamaçları · vadi tabanında nehir
④ IZGARA      ⛔ DÜZ 15 × 8,0 — sahip beyanı · karşı kayıt PLAN §DÜZ IZGARA BEYANI'nda
⑤ QA BİRİMİ   FİLM (tek master × 12 mercek) — 2 dk hattı
⑥ ARAÇ        ⬜ kutu seti ÖLÇÜLMEDİ; 8,0 s teslim için en büyük kutu ≥ 9,0 gerekir (günlük §0)
```

---

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
15.09.2026  "ara kareyi kaldır her sahne 8 saniye 15 sahne yani iki dk aynı dikey shorts mantığı ama
             yatayda yapcaz önce tema konu ve sahneleri anlatan bir rapor yaz bana"
16.09.2026  rapor güncellendi (yedi maddelik eleştiri işlendi) → "bu filmi yapalım"
TALEBİN İÇİNDEKİ KİLİTLER
  · 15 sahne × 8,0 sn · ara kare YOK · zincirli format (dikey shorts mantığı) · yatay kadraj
  · ilk itme 32. saniyede · eski yol film boyunca canlı · sel bir AKIŞ olayı · kavuşma iki adımlı
  · final karanlık değil · eşit süre otomatik ritim hatası sayılmaz, yük müzik katmanlarında
```

---

## 2. 🚪 KONSEPT KAPISI — VAAT / DİRENÇ / BEDEL [KILAVUZ_REHBERI §6]

```
VAAT     Vadiyi on dört virajla geçen eski yolun yerine, karşıdan karşıya İTİLEN 420 m'lik düz bir viyadük.
DİRENÇ   ① derinlik (orta ayak 60 m) ② boşluk (tabliye desteksiz itilir, burun konsolda) ③ nehir (kar erimesi seli)
         EKRANDA NASIL: S2 · ayaklar tırmanır kalıpla yükselir   S4–S6 · burun boşlukta ayaktan ayağa
         S7–S9 · nehir kabarır, geçici geçiş kopar, itme durur, çamur çizgisi kalır
BEDEL    Eski yolun trafiği. G0'da virajlarda araçlar ve far izleri; G15'te son araç çıkmış, kıvrımlar boş
         ama OKUNUR (asfalt bandı + korkuluk). Bedel taş köprünün ayrıntısına yüklenmez: taş köprü 320 px'lik
         önizlemede ≈11 px'tir; anlamı virajların geometrisi + trafiğin varlığı/yokluğu taşır.
KANAL TEZİ  ne kayboluyor? eski yolun trafiği ✅ · kadrajda mı? evet, iki yamaçta sabit kamerada ✅
            cevap "zaman geçiyor" mu? hayır ✅
```

---

## 3. 🎥 KAMERA HESABI — 16:9 [KILAVUZ_REHBERI §2.8 · KAMERA_ISTASYONU §3 · DERS 38]

```
İSTASYON   MAIN — vadi ağzındaki kaya mahmuzunun düz tepesi · 24 mm · f/8 · ISO 100 · tam kare yatay
h = 80,0 m (nehir kotundan)   D_eksen = 380 m (viyadük ekseni)   D_kenar = 190 m (alt kenar ışını zemine)
bakış 0° (kuzey, vadi yukarı) · tilt 0° · roll 0°
FORMÜL     yüzde(y) = 50 + 118,5·(y − 80)/D        yüzde(x) = 50 + 66,7·x/D        px/m = 1280/D
           D = 380 → 3,37 px/m · kadraj genişliği 570 m · kadraj yüksekliği 320 m

DİKEY      nehir / P3 dibi %25,1 · P2 %28,8 · P4 %28,2 · P1 %34,4 · P5 %33,8
           tabliye altı %43,8 · ⭐ TABLİYE ÜSTÜ %45,0 · lamba direkleri (+12 m) %48,8
           taş köprü (D 600) %34,2 · şapel (D 700) %61,9 · kaya kulesi (D 420) %45,9–57,5 · ikiz zirve %82,4
YATAY      A1 %13,1 · P1 %23,7 · P2 %36,8 · P3 %50,0 · P4 %63,2 · P5 %76,3 · A2 %86,9
           döküm alanı %0–10,5 · taş köprü %44,4 · şapel %28,1 · kaya kulesi %89,7 · geçici geçiş %46,9
PİKSEL     P3 ayağı 202 px · tabliye derinliği 13 px · kamyon 40 px · araba 15 px · taş köprü 64 × 21 px
           şapel çan kulesi 33 px · kaya kulesi 122 px
⛔ SAĞ ŞERİT UYARISI: A2 %86,9'da — sağ sekizde (%87,5) ÇOK YAKIN. Usta karede ölçülür; %87,5'i geçerse
   D 380 → 400 m'ye çekilir (yapı %13,1–%86,9 → %14,4–%85,6), plan ve SPEC güncellenir.
⛔ ÖN GÖRSELLEŞTİRME: plan + yan kesit — mahmuz · ayaklar · tabliye kotu · taş köprü · zirve silüeti;
   itme boyunca burun ucunun hangi ayak hizasında olduğu her kare için işaretlenir.
```

---

## 4. 🏗️ VİNÇ / GEÇİCİ EKİPMAN KARARI [DERS 1 · 8 · 22 · 46 · 48 · 57]

```
⛔ TABLİYE KALDIRILMAZ, İTİLİR. Hiçbir karede beton gövde havada taşınmaz: gövde her an ya döküm
   yatağında ya ayak mesnetlerinde durur; ilerleme SÜRTÜNME ve KRİKO ile olur.
⭐ AMA "vinç yok" bütün montaja yayılmaz [sahip uyarısı 16.09.2026]:
   · döküm alanında (sol plato, kamera kotunun altında) bir MOBİL VİNÇ vardır — donatı kafesi, kalıp
     panosu ve çelik burun parçalarını kısa ve ALÇAK kaldırır; bomu hiçbir karede zirve silüetinin
     üstüne çıkmaz, kanca her karede YÜKLÜ ve düşeydir
   · nehir düzlüğündeki geçici çelik desteği bir PALETLİ VİNÇ kurar (S6) ve söker (S12); aynı kural
   · ayak gövdelerinde vinç YOKTUR: tırmanır kalıp kendi krikosuyla yükselir, beton POMPA hattıyla çıkar
⛔ Ağır makine ESKİ TAŞ KÖPRÜDEN geçmez: taş köprünün taşıma kapasitesi bilinmez, film bunu varsaymaz.
   Her promptta taş köprü POZİTİF BOŞ yazılır: "the stone arch bridge carries only light traffic; its
   deck stays bare of plant". Sel sonrası erişim, geçici geçiş onarılana kadar beklenir.
GEÇİCİ EKİPMAN LİSTESİ (SITE/BACKGROUND'a GİRMEZ [DERS 1]): tırmanır kalıp · döküm hangarı · itme yatağı ·
   çelik burun · geçici çelik destek · geçici menfez geçişi · şantiye yolu · mobil vinç · paletli vinç ·
   beton pompası · mikser · damper · finişer · silindir
```

---

## 5. ☀️ IŞIK GÜNÜ VE TAKVİM [ZAMAN_VE_ISIK §2 · §6 · §7 · SANTIYE_HAREKETI §1]

```
IŞIK GÜNÜ  05:05 → 18:35 · Σ = 6 × B (2 sa) + 9 × A (10 dk) = 12,0 + 1,5 = 13,5 saat ≤ 14 ✓
           REJİM DAĞILIMI  B: S1 · S3 · S6 · S7 · S9 · S12   A: S0 · S2 · S4 · S5 · S8 · S10 · S11 · S13 · S14
           gerekçe [SANTIYE §2]: B = gölge süpürmesi ve gök hareketi gereken sahneler · A = makinenin,
           aracın ve suyun okunması gereken sahneler. A dizisi hiçbir yerde ikiden fazla art arda değil
           (yalnız S13–S14 alacakaranlıkta üçlü: ışığın kendisi hızla değişiyor).
GÜNEŞ      45°K · δ +7° geometrisi · kadraj yatayda 323°–37° · güneş 75° → 281°: disk hiçbir karede kadrajda
           DEĞİL [DERS 39]. G0 şafak (−5°), G15 gün batımından hemen sonra (−1°) — gök aydınlık [DERS 45].
TAKVİM     10 Mart (yıl 1) → 26 Kasım (yıl 2) = 627 gün ≈ 20,6 ay · iki kış, iki yaz
TAŞIYICILAR yamaç melezleri (Larix decidua — yaprak DÖKER: yeşil → altın → çıplak) · zirvelerde kar çizgisi ·
           nehrin rengi ve debisi · tarla/çayır bantları · beton yaşı (yeni dökülen kesit koyu, eskiler açık)
⛔ VADİYE KAR YAĞDIRILMAZ: tek ışık günü ve A/B rejimleri kar yağıp erimesini taşımaz [HAVA §3 · DERS 7].
   Kış YALNIZ kar çizgisinin yamaçta inmesiyle ve çıplak melezlerle okunur (G6 → G7 iki kare).
⚠️ ÜSLUP BEYANI: 20 aylık takvim tek bir günün ışığına sıkıştırılmıştır. Bu bilinçli bir kurgudur;
   film hiçbir yerde "tek günde çekildi" demez ve paketlemede de böyle sunulmaz.
```

---

## 6. ⚠️ RİSK — yapı kartının RİSK satırları + bu deponun tekrar eden arızaları

```
① İTME SIÇRAR      model gövdeyi kaydırmak yerine ileride kopyalar, arkayı siler [DERS 57 mekanizması]
② DÜZ IZGARA       14 eşit kesme → ⑥ METRONOM beklenir [DERS 13 · 24 · 44]
③ İKİ YÜZEY        makine hazır yüzeye kaçar: eski taş köprü vs. yeni tabliye [DERS 51 · 53]
④ ÇOĞALMA          "viaduct" korpusu otoyol dizisidir; ikinci köprü/ayak sırası belirebilir [DERS 55]
⑤ SU SEVİYESİ      nehir seli kare kare kilitlenmezse su iner-çıkar; taş köprü sel karesinde kaybolabilir
⑥ ÖLÇEK            3,37 px/m — insan 6 px; iş büyük makineyle ve yüzey iziyle kanıtlanır [A6-d]
⑦ A REJİMİ DİZİSİ  gölge donuk okunabilir [DERS 47]; her karede mevsim taşıyıcısı zorunlu
⑧ SAĞ ŞERİT        A2 %86,9 — güvenli alan 16:9 ölçülmedi, usta karede doğrulanır
```

### ⭐ 1 NUMARALI RİSK SAYIYLA YAZILIR

```
İTME SIÇRAMASI. Klip başına itme ≤ 90 m (kadrajın %15,8'i); her karede burun ucu ADI VERİLEN bir ayağın
üstünde; izlenen kanıt: ilk dökülen kesitin koyu döküm derzi — 16 karede aynı kesit, hep en önde.
Önlem cümlesi (her I2V'de): "only the deck slides forward as one piece; the piers, the abutments and the
temporary support stand still, and no new section appears ahead of the nose."
Araç kapısına ÖZEL ÖLÇÜM eklendi (günlük §0 ⑨): test klibinde uzun bir gövde yatay kaydırılıyor mu,
yoksa hedefte kopyalanıp kaynak siliniyor mu.
```
