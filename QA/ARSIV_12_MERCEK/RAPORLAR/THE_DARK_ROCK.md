# 📋 THE DARK ROCK — QA KAYDI

```
KÜNYE      14/15 segment · 0:47,0 sahne bloğu · kapak 5,0 sn · toplam 0:52,0
           on iki mercek koşuldu (12/12) — ① KARE, ② İNŞA, ③ ZAMAN, ④ TESLİM, ⑤ DEVAMLILIK, ⑥ GEÇİŞ, ⑦ İŞ, ⑧ YÖNTEM, ⑨ FAALİYET, ⑩ SEBEP, ⑪ ENVANTER, ⑫ KATILIK (hepsi Mode V / belgesiz koşuldu)
KARAR      ⛔ YAYINLANMAZ.
```

---

## 1. ON İKİ HÜKÜM

| Mercek | Skor | HÜKÜM |
|---|---:|---|
| ① KARE | 4,9/10 Ⓥ | ⛔ **SIX SEPARATE SHOTS** |
| ② İNŞA | 3,8/10 Ⓥ | ⛔ **DIFFERENT** · ⛔ **APPEARING** |
| ③ ZAMAN | 2,8/10 Ⓥ | ⛔ **PASSES BUT NOT IN ONE DIRECTION** |
| ④ TESLİM | 6,1/10 Ⓥ | ⚠️ **ENDS** · COST/FINAL BEAT PASS |
| ⑤ DEVAMLILIK | 3,1/10 Ⓥ | ⛔ **A SET REBUILT EACH TIME** · NONE FOUND |
| ⑥ GEÇİŞ | 2,9/10 Ⓥ | ⛔ **NEXT** · ⛔ **METRONOM** |
| ⑦ İŞ | 5,1/10 Ⓥ | ⛔ **PARKED** |
| ⑧ YÖNTEM | 4,5/10 Ⓥ | ⛔ **APPEARED** |
| ⑨ FAALİYET | 4,3/10 Ⓥ | ⛔ **IDLE ANIMATION** |
| ⑩ SEBEP | 3,8/10 Ⓥ | ⛔ **MAGICAL APPEARANCE** |
| ⑪ ENVANTER | 7,5/10 Ⓥ | ⛔ **INTRUDERS** |
| ⑫ KATILIK | 2,4/10 Ⓥ | ⛔ **MELTING** |

```
İnceleme Notu: Raporlar belgesiz (Mode V) ön koşu olarak alınmıştır. 
On iki merceğin on ikisi de RUN INCOMPLETE bayrağıyla dönmüştür.
```

---

## 2. KÖK SEBEP VE EN AĞIR BULGULAR

```
KANIT      ① VANTAGE GROUPS = 4 (Plan TEK MAIN STATION diyordu)
              A = clips 1,2,3,5,8 · B = clip 4 · C = clip 6 · D = clip 7
           ① 00:04,0 Kayanın çentikli tacı tek karede hazır beton kaideye dönüştü.
           ① 00:35,0 Deniz kayalığı ve ufuk kayboldu, saman balyalı kara tarlasına dönüştü.
           ① 00:41,0 Fener külahından 4 kollu robotik örümcek kolları / vinç aparatı fırladı.
           ② 00:32,0 Tamamlanan fener odası yok oldu, bina beton şafta geriledi.
           ② 00:19,0 İskele tümüyle kayboldu, 00:22,0'de tekrar belirdi.
           ③ 00:16,0 Mevsim ve ışık yazdan sert kış fırtınasına düştü, 00:21,0'de yaz güneşine döndü.

MEKANİZMA  Ters inşa zinciri ve iki keyframe bağlama mantığı üretilmeyen test kurgusunda 
           bağımsız jenerasyonlar halinde üretilmiştir. Makine ve iskele mantığı korunmamış, 
           kadraj tek deniz kayalığı yerine karadaki saman balyalı tarlalara kaymıştır.
```

---

## 3. EN AĞIR BEŞ ARIZA

```
① KAYA TACI 00:04,0  Kayanın çentikli tacı kesilme ve kırma aşaması görünmeden anında hazır
                     pürüzsüz beton platforma dönüştü.
① KARA TARLASI 00:35,0 Deniz ufku ve THE NEEDLE sütunu silindi; kadraj saman balyalı karadaki
                     çiftlik tarlasına sıçradı (Vantaj Group D hatası).
① ROBOT KOLLAR 00:41,0 Fener külahının üstünden gerçek dışı 4 kollu robotik örümcek vinç
                     mekanizması fırladı (FİLMDE VİNÇ YOK kuralı ihlali).
② ŞAFT GERİLEMESİ 00:32,0 00:27'de tamamlanan fener odası ve galeri yok oldu, kule çıplak
                     beton şafta geriledi.
③ MEVSİM DÖNGÜSÜ     Yaz → Kış Fırtınası → Yaz → Sonbahar Hasadı → Yaz sırasında düzensiz
                     zaman sıçramaları gerçekleşti.
```

---

## 4. ①, ③, ⑤, ⑦, ⑨ VE ⑫'NİN "QUESTIONS FOR THE DOCUMENT" CEVAPLARI

```
①-1  HAYIR. S0 planında ekskavatör (hidrolik kırıcı) çentikli taç tepelerini kademe kademe
     indirir (%39 → %34,5 kaide), apron ve basamaklar oyulur. Anında hazır beton platforma
     dönüşme jenerasyon arızasıdır.
①-2  HAYIR. Plan TEK İSTASYON (MAIN STATION: 24 mm küresel, +21 m yükseklik, tilt 0°, 0° bakış)
     kilitlidir. Vantaj B, C, D sapmaları jenerasyon/kamera kayması arızasıdır.
①-3  JENERASYON ARIZASI. Plandaki çapa kuzeybatıdaki sabit Uzak Burun tarlasıdır (x 0-430 px,
     %49,5-%52,9). Açık deniz kayalığının tamamen karadaki saman balyalı tarlaya sıçraması
     kabul edilemez model sapmasıdır.
①-4  HAYIR. Plan §DEĞİŞMEZLER ve §YAPI BIBLE gereği FİLMDE VİNÇ VEYA ROBOTİK GÖVDE YOKTUR
     [DERS 8 · 22 · 46 · 57]. Tek taşıyıcı raylı asansör kabinidir (rack-and-pinion). Fener
     külahından çıkan robot kollar prompt ve plan ihlalidir.
①-5  Kamera mimarisine göre (h=21m, tilt 0°), 28-56m arasındaki deniz ve kayalık ayağı kadrajın
     alt %25 bandındadır (%0–25). Çıkarma gemisi, rampa ve ekskavatör burada çalışır. Üst çeyrek
     (%87,5+) ise boş gök alanıdır.

③-1  ~6 ay (Mart başı → Eylül başı), 6 sahne × 8,0 sn = 48,0 sn sahne bloğu.
③-2  Güneş geometrisi 48°K ağustos geometrisidir (tek ışık günü 07:00 → 19:00). Fırtına yalnız
     S3 (Clip 3/4) fırtına tavanındadır. Işığın aniden karanlık kış fırtınasına düşüp tekrar dik
     yaz güneşine zıplaması prompt ve model arızasıdır.
③-3  Clip 11 (planda S4/S5 aşaması) uzak burundaki tek tarlanın anız + balya dönemidir (Ağustos
     sonu/Eylül başı). Karadaki tarlanın arka plan yerine ana mekan haline gelmesi modelin
     kadraj hatasıdır.

⑤-1  JENERASYON ARIZASI. Deniz ortasındaki bir kayalığın anakara tarla manzarasına sıçraması kabul edilemez görsel hatadır.
⑤-2  Turuncu çelik rampa (apron kenarındaki yuvasında) KALICIDIR. Film boyunca (S1'den S5'e kadar) durmalıdır; S3 fırtınasında yerinden kayar ve sonra geri çekilip pimlenir. Sökülmesi planlanmamıştır.
⑤-3  HAYIR. Planda VİNÇ YOKTUR, ne kule vinci ne de tepeden asılı quad-hook gantry (DERS 8/22). Fener parçaları raylı asansör kabiniyle (rack-and-pinion) taşınır. 00:41'deki gantry aparatı prompt/model uydurmasıdır.

⑦-1  S1-S2 arasında temel dökümü PLANLANMIŞTIR ancak model atlamıştır (görünmeyen büyüme).
⑦-2  Planda kule vinç YOKTUR. Raylı asansör (hoist) vardır.
⑦-3  HAYIR. Planda fırtınada çalışmanın sürdüğü ve direncine rağmen yapının yükseldiği (RESISTANCE) belirtilmiştir. Park edilmesi arızadır.
⑦-4  HAYIR.
⑦-5  HAYIR. Planda yoktur.

⑨-1  Prompt/Model uydurmasıdır.
⑨-2  Kılavuz gereği her araç İŞ YAPAR, dekoratif ortam trafiği yoktur. Yanaşmaları beklenirdi.
⑨-3  Planda ekskavatör yalnızca S1/S2'de çalışır, sonrasında sahadan ayrılır. S6/S7 fırtınasında orada unutulması (parked) model hatasıdır.

⑫-1  Jenerasyon arızasıdır (Vantage D / A SET REBUILT EACH TIME hatası).
⑫-2  Planda öyle bir vinç (rig) yoktur, geçici veya kalıcı değildir; modelin uydurmasıdır.
⑫-3  Fener bileşenleri, kılavuz gereği gövdedeki raylı asansör kabiniyle (rack-and-pinion) taşınır. Havada doğrudan belirmesi hatalıdır.
⑫-4  Üniform prekast (hazır döküm) beton şaft halkalarıdır.
⑫-5  Kırılmış doğal kaya parçalarını (moloz) gemiye dökmek içindir.
```

---

## 5. KARAR VE GELECEK KOŞU

```
⛔ YAYINLANMAZ.
Yeniden üretim öncesinde:
  1. Üretim günlüğü açılmalı ve Araç Kapısı testleri (8 ölçüm) koşulmalıdır.
  2. Ters inşa zinciri (GN → G0) ve iki keyframe kilitli I2V üretimi birebir uygulanmalıdır.
  3. Fener tepesinde vinç/robotik kol üreten prompt kelimeleri temizlenmelidir.
```
