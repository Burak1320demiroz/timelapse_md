# 🔍 THE QUIET FIELD — QA RAPORU

```
FİLM          THE QUIET FIELD — kırsal çayırda 76 m radyo teleskopu (Lovell tipi, sıfırdan)
TARİH         21.09.2026
DURUM         ⭐ ÜRETİLDİ VE ON İKİ MERCEKLE ÖLÇÜLDÜ (12/12 TAM KOŞU)
              ⭐ ASGARİ SET EKSİKSİZ TAMAMLANDI (① KARE 9,8 · ② İNŞA 10,0 · ⑤ DEVAMLILIK 10,0)
              ⭐ Deponun ilk belgeli 10/10 İNŞA ve 10/10 YÖNTEM skorları (8/8 eleman yapıldı, 0 beliren parça)
              ⭐ Deponun ilk 10/10 ZAMAN, 10/10 DEVAMLILIK, 10/10 GEÇİŞ, 10/10 FAALİYET, 10/10 ENVANTER ve 10/10 KATILIK skorları
              ⭐ 12/12 HÜKÜMLERİN TAMAMI EKSİKSİZ GEÇTİ (Depo tarihinin en kusursuz filmi)
              ⚠️ Tek kurgusal kusur: 0:48–0:56 arasında planda olmayan başlık bindirmesi (Safe Area 8/10)
HAM           QA/HAM_RAPORLAR/THE_QUIET_FIELD/ — 12 dosya, dokunulmaz
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|---:|---|---|
| **① KARE** | V (58 kare) | **9,8**/10 Ⓥ | ✅ **TIME-LAPSE** | Kamera kilidi 10 · İstasyon 10 · Nirengi 10 · Zemin gerçeği 10 · Vinç 10 · Kar 10 · Gece 10 · Safe Area 8/10 (0:48–0:56 üst %40 başlık bindirmesi) |
| **② İNŞA** | D | **10,0**/10 | ✅ **SAME · BUILT** | Deponun ilk tam puanlı İnşa koşusu · 7 milestonedaki ölçek kilit sapması %0,0 · Halka hendekten 50° çanak devrilmesine kusursuz montaj sırası |
| **③ ZAMAN** | V (tam kurgu) | **10,0**/10 Ⓥ | ✅ **PASSES** | Deponun ilk 10/10 Zaman koşusu · Filmden okunan süre: "about one year" (plan: 1 yıl) TAM TUTTU · 360° mevsim çemberi + gece yıldız izi + gündüz gölge süpürmesi |
| **④ TESLİM** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 8,4) | ✅ **ENDS** | FINAL BEAT PASS (9/10) · ONE THING BULUNDU · Plan ve kapak verilmedi · 0:54.0 çanağın 50° güneşe devrilişi doğrulandı |
| **⑤ DEVAMLILIK** | ⛔ V karesiz | *karesiz — TEKRARLANACAK* (ham 10,0) | ✅ **SAME WORLD** | 0/6 dikiş kusursuz · ⭐ Kanıt nesnesi: Taş ambar (0:00.0 ve 0:56.0) · Ekipman geçişleri, zemin izleri ve kar örtüsü tam tutarlı |
| **⑥ GEÇİŞ** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 10,0) | ✅ **TIME · ⭐ RHYTHM** | 0 kusur · Eşit süreye (8,0 sn) rağmen RHYTHM hükmü kazandı · THE CUT THAT CARRIES: Cut 2 (0:16.0 gündüzden karlı geceye geçiş) · Plan ve ses verilmedi |
| **⑦ İŞ** | ⚠️ V karesiz | **9,0**/10 Ⓥ | ✅ **WORKING** | Çalışma cephesi 10/10 · Sebep-sonuç 10/10 · En uzun boşluk 2,0s (%25) · ⭐ Kimsenin yapmadığı büyüme: NONE |
| **⑧ YÖNTEM** | D | **10,0**/10 | ✅ **MADE · 8/8 MADE** | Deponun ilk belgeli 10/10 Yöntem skoru · 8 elemanın 8'i de sıfırdan inşa edildi · ⭐ İlk beliren parça: NONE · En iyi parça: Beşik tandem kaldırma |
| **⑨ FAALİYET** | ⛔ V | **10,0**/10 Ⓥ | ✅ **PRODUCTIVE WORK** | Boşta bekleme 10 · Amaçsız hareket 10 · Döngü 10 · İnsan emeği 10 · ⭐ Amaçsız aktivite: NONE FOUND · Plan verilmedi |
| **⑩ SEBEP** | ⛔ V | **9,5**/10 Ⓥ | ✅ **CAUSED BY LABOUR** | Nedensellik bağı 10 · İşsiz yakınlık 10 · Emeğin ölçeği 9 · Malzeme kaynağı 9 · ⭐ Sihirli belirme: NONE FOUND · SPEC verilmedi |
| **⑪ ENVANTER** | ⛔ V | **10,0**/10 Ⓥ | ✅ **INVITED** | Makineler 10 · Yapılar 10 · Işık/enerji 10 · Kurallar 10 · Gece/fırtına 10 · ⭐ Davetsiz misafir: NONE FOUND · Gelmeyen davetli: NONE |
| **⑫ KATILIK** | ⛔ V karesiz | **10,0**/10 | ✅ **SOLID** | Kenar ve siluet 10 · Sayım 10 · Kimlik 10 · Boyut 10 · Geçiş/birleşme 10 · Yük yolu 10 · ⭐ En kötü eriyen gövde: NONE FOUND |

---

## 2. ⛔ HÜKÜM OKUMA SIRASI [kart R 6a, 6e]

```
12/12 HÜKÜMLERİN HEPSİ TUTTU:
⑤ SAME WORLD ✅ + ⑧ MADE 8/8 ✅ + ⑦ WORKING ✅ + ⑩ CAUSED BY LABOUR ✅ + ⑪ INVITED ✅ + ⑫ SOLID ✅ + ① TIMELAPSE ✅ + ② BUILT ✅ + ③ PASSES ✅ + ⑥ RHYTHM ✅ + ④ ENDS ✅

⭐ TARİHİ BİR EŞİK AŞILDI:
   1. ⑤ SAME WORLD (Taş ambar 0:00 ve 0:56) + ⑧ MADE (8/8 parça sıfırdan, 0 beliren parça):
      Depoda ilk kez iki zincir kilit hükmü aynı anda tam puanla (10/10) tuttu!
   2. ⑦ WORKING (GROWTH NOBODY MADE: NONE) + ⑩ CAUSED (MAGICAL APPEARANCE: NONE):
      Depoda ilk kez tek bir karede dahi "açıklanamayan hayalet büyüme" veya "kendiliğinden beliren malzeme"
      görülmedi. Her cıvata ve kiriş doğrudan çalışan makinelerin veya işçilerin eliyle monte edildi.
   3. ⑪ INVITED (INTRUDER: NONE) + ⑫ SOLID (MELTED: NONE):
      Depoda ilk kez hiçbir yabancı nesne kadraja sızmadı; makineler ve devasa çanak rijit katılıklarını
      (geometrik kilit) 56 saniye boyunca milimetrik olarak korudu.
   4. ASGARİ SET (① 9,8 · ② 10,0 · ⑤ 10,0):
      Kamera sabit, yapı kimliği tek ve monoton, dünya kesintisiz.
   5. RİTİM (⑥ 10,0):
      Eşit süreli 8,0 sn ızgaranın METRONOM tuzağı, Cut 2'deki ışık/mevsim vuruşuyla aşıldı.
   6. DEVRİLME ÖDÜLÜ (④ ENDS · FINAL BEAT PASS):
      3 000 tonluk çanak 0:54.0'ta 50° güneşe devrilerek vaadini yerine getirdi.
```

---

## 3. 🚨 EN AĞIR BULGULAR

1. **[① KARE & ④ TESLİM — Safe Area 8/10 & Kurgu Uyuşmazlığı]:** 0:48.0–0:56.0 arasında ekranda beliren statik başlık bindirmesi (`THE QUIET FIELD`) çerçevenin üst %40'lık bölümünü (y ≈ %60–95) kaplamış ve üst sekizlik (%87.5–100) güvenli alan rezerv bandına taşmıştır. Oysa plan §TESLİM YAPISI açıkça `KAPAK KARTI YOK`, `LOGO YOK`, `0,0–56,0 boyunca klip üstüne metin bindirilmez` şartını koymuştur. Başlık dizgisi platform küçük resmi (thumbnail) için `THE_QUIET_FIELD_KAPAK.md` dosyasında ayrı tutulmuştur. Kurguda bu metin katmanı kaldırılmalıdır.
2. **Kusursuz Alanlar (Kusur Yok):** 
   - Kamera kilit ve nirengi stabilitesi: 10/10
   - Yapı montaj ve yük yolu fiziği: 10/10
   - Zaman, güneş yönü ve mevsim çemberi: 10/10
   - Dünya devamlılığı ve 6 dikişin tamamı: 10/10
   - Şantiye emeği ve sebep-sonuç ilişkisi: 10/10
   - 8 yapı elemanının tamamının sıfırdan yapımı: 10/10
   - İnsan ve makine faaliyetinin gerçekliği: 10/10
   - Kadraj envanteri ve davetsiz misafir sıfırlığı: 10/10
   - Katı gövde rijitliği ve erime sıfırlığı: 10/10

---

## 4. ⏱️ ZAMAN TAHMİNİ [kart R 6]

```
③ "TIME READ FROM THE FILM ALONE: about one year"
Taşıyıcı: Zemin bitki örtüsünün tam mevsimsel döngüsü (yaz çayırı → sonbahar hasat çizgileri → kış kar örtüsü
→ ilkbahar çamuru → yaz yeşil çayırı), gece inşaat aşamalarındaki sürekli yıldız izleri ve hendek kazısından
tamamlanmış 50° devrik çanağa yapısal ilerleme.
PLAN: 1 yıl (Mayıs çayırı G0 → Haziran çayırı G7).
✅ TAM VE EKSİKSİZ TUTTU — Depoda bir yıllık döngüyü modele ekrandan tam okutan ilk film.
```

---

## 5. ❓ DOKÜMAN SORULARININ CEVAPLARI

### ① KARE
1. **Grup A için hedef ufuk yüzdesi spesifikasyonu nedir?**
   - *Cevap:* Planda ufuk tam **%50,0** (y = 50.0%) olarak kilitlenmiştir (tilt 0° kanıtı, KAMERA_ISTASYONU §3). Tolerans ±0,5 puandır. Ölçülen %50,0 değeri planla birebir örtüşmektedir.
2. **Son bölümde üst güvenli alana yerleştirilen büyük başlık tipografisi proje briefinde planlanmış mıydı?**
   - *Cevap:* **Hayır.** Planda başlıklı bitiş kartı veya video üzeri metin bindirmesi (overlay) kesinlikle yasaklanmıştır (`KAPAK KARTI YOK`, `LOGO YOK`, SWALLOWED BUS / BACK TO WATER / EMPTY LOCK teslim kuralı). Başlık yalnızca platforma yüklenecek statik kapak görseli (`THE_QUIET_FIELD_KAPAK.md`) için tasarlanmıştır. Kurgudaki metin katmanı teslimat hatasıdır ve kaldırılmalıdır.
3. **Tek kilitli kamera açısının tüm 56 saniye boyunca ikincil açı olmadan statik kalması planlanmış mıydı?**
   - *Cevap:* **Evet.** Plan tek ve sabit istasyon şart koşmuştur: güney çayır tepeciği (h 20 m, teleskop eksenine 160 m, bakış 10°, tilt 0°). 56,0 saniye boyunca kamera sıfır hareketle kilitli kalacak şekilde tasarlanmıştır.

### ③ ZAMAN
1. **Her sahne bloğu için beyan edilen güneş yükseklik ve azimut hedefleri nedir?**
   - *Cevap:* Plan §9 Zaman ve Işık tablosu (53° Kuzey enlemi, Haziran sonu ışık çemberi):
     - G0 (Klip 1 başı, 17:20): Azimut 265°, Yükseklik +30°
     - G1 (Klip 2 başı, 19:20): Azimut 288°, Yükseklik +15°
     - G2 (Klip 3 başı, 21:20): Azimut 316°, Yükseklik +2° (günbatımı 21:40 Klip 2 sonu / Klip 3 başı)
     - G3 (Klip 4 başı, 23:20): Azimut 347°, Yükseklik −11° (gece, yıldız izleri 30° / 2 sa, kutup yıldızı merkezli)
     - G4 (Klip 5 başı, 01:20): Azimut 15°, Yükseklik −13° (gece dip noktası, kuzey ufku alacakaranlık bandı)
     - G5 (Klip 6 başı, 03:20): Azimut 42°, Yükseklik −7° (şafak başlangıcı, gündoğumu 04:40 Klip 6 içinde)
     - G6 (Klip 7 başı, 05:20): Azimut 62°, Yükseklik +5° (sabah güneşi)
     - G7 (Klip 7 sonu, 05:30): Azimut 64°, Yükseklik +6° (operasyonel çanak devrilmesi sonu)
     Gölgeler Klip 1–2'de sağa/doğuya; Klip 6–7'de sola/batıya uzanır.
2. **Tam proje zaman çizelgesi için beyan edilen toplam takvim süresi nedir?**
   - *Cevap:* Planda beyan edilen toplam inşaat takvim süresi **1 yıldır (12 ay)** (Mayıs'ta zemin kazısı → kışın karlı gece montajı → ertesi Haziran'da çanağın operasyonel devrilmesi).
3. **Her klip boyunca uygulanan beyan edilmiş zaman sıkıştırma oranı ve kare aralığı nedir?**
   - *Cevap:*
     - Klip 1–6 (S0–S5): **Rejim B (900× sıkıştırma)** — Her 8,0 saniyelik klip sahada 2 saatlik (7200 sn) inşaat çalışmasını temsil eder.
     - Klip 7 (S6): **Rejim A (75× sıkıştırma)** — 8,0 saniyelik klip sahada 10 dakikalık (600 sn) çanak devrilme hareketini temsil eder.

### ⑤ DEVAMLILIK
1. **Klip 2 (0:16.0) ile Klip 3 (0:16.0) Arasındaki Geçiş:**
   - *Cevap:* **Evet.** Zemin takvimi 1 yıllık inşaatı temsil eder (Mayıs'ta kazı → sonbaharda anız → kışın karlı gece montajı → ilkbahar çamur ve erime → ertesi Haziran operasyon). Klip 2'den Klip 3'e geçişte yaz/sonbahardan kış gecesine sıçrama planlı bir takvim adımıdır.
2. **Klip 3'te Kurulan Dört Projektör Direği:**
   - *Cevap:* **Evet.** `QA_SPEC §2` satır 54 açıkça: *"projektör direkleri (G3–G7) ... G6–G7'de sönük ama YERİNDE"* kuralını koymuştur. Direkler gece kurulduktan sonra kalıcı saha altyapısı olarak gündüz karelerinde de yerinde kalır.
3. **Klip 7'de Vinçlerin Sahadan Ayrılması:**
   - *Cevap:* **Evet.** `QA_SPEC §2` satır 52 ve `§3` satır 73: *"G6 SABAH: vinç YOK (tırtıl izi yola)"*. Ağır paletli ve mobil vinçler kaplama tamamlandıktan sonra sahayı terk eder; S6'daki operasyonel devrilme sırasında kadrajda vinç bulunmaması planlı ve zorunludur.

### ⑦ İŞ
1. **Klip 3 ile 4 Arasındaki Vinç Değişimi (Tek Vinç ➔ Tandem Çift Vinç):**
   - *Cevap:* **Evet.** Plan §4 Yük Yolu ve QA_SPEC §3/§4: 80 metrelik dev beşik kirişinin iki kule tepesine montajı gerçek ağır kaldırma mühendisliği gereği iki paletli vinçle eşzamanlı (tandem) olarak kaldırılır. Beşik oturduktan sonra tek vince dönülür.
2. **Klip 4'teki Kar ve Don Döneminde Çalışma:**
   - *Cevap:* **Evet.** S3 ve S4 gece inşaatı 23:20–01:20 ve 01:20–03:20 arasındaki tek bir kesintisiz kış vardiyasını temsil eder. Şantiye projektörler altında durmaksızın çalışır.
3. **Klip 6'daki Katı Çanak Kaplama Panellerinin Lojistiği:**
   - *Cevap:* **Evet.** QA_SPEC §3 G5/G6 ve Plan S5: Paneller sahaya önceden üretilmiş paketler (bundles) hâlinde kompaundda istiflenmiş olarak gelir ve vinçle doğrudan göbekten dışa doğru halka halka monte edilir.

### ⑨ FAALİYET
1. **Gece Vardiyasında Vinç Kaldırmaları Arasında Bekleme:**
   - *Cevap:* Plan §4 ve FIZIK_VE_AGIRLIK: Vinç kancası havada boş sallanmaz; her kaldırma döngüsü doğrudan kompaunddan kule tepesine düşey iniş-çıkış olarak tasarlanmıştır.
2. **Klip 7'de Sağ Kule Dibindeki Pikap:**
   - *Cevap:* **Evet.** QA_SPEC §3 G6/G7: *"pikap sağ kule dibinde ... 2 figür sırtı dönük ... çanak devrilmesini izler"*. Çanağın 50° devrilme hareketini denetleyen yer kontrol mühendislerinin aracı olarak planlanmıştır.
3. **Gündüz Hafriyatında Destek Araçları:**
   - *Cevap:* **Evet.** G0'da 3 ekskavatör, kazık makinesi ve 2 damperli kamyon; G1'de beton mikserleri ve pompa kamyonu planda birebir şart koşulmuştur.

### ⑫ KATILIK
1. **Gece Kule ve Tandem Beşik Kaldırmasının CAD Modellemesi:**
   - *Cevap:* **Evet.** QA_SPEC §4 Yük Yolu ve Beş Sorunun ③'ü uyarınca kule kafes bölümleri 5 modül (her biri 10 m, 80 px) ve beşik 80 m rijit kutu kiriş olarak tanımlanmıştır.
2. **Kar ve Erime Hızı:**
   - *Cevap:* 53° Kuzey enlemi haziran/yaz gecesi kısa döngüsünde (gece 5 saat, hava sıcaklığı geçişleri) yerel zemin takvimine tam oturtulmuştur.
3. **Çanak Devrilme Ekseni Toleransı:**
   - *Cevap:* QA_SPEC §1 ve §7: Çanak devrilme ekseni +52 m (y = %63) seviyesinde sabit kilitlenmiş, devrilme açısı 50° ve çanak çapı 513 px ±2 px toleransla tanımlanmıştır.

---

## 6. 📋 OLAY TABLOSU [C1 · QA/00_README §8]

| Olay | Zaman | Ne oldu (görünen) | Mercekler | Kanıt karesi | Karar |
|---|---|---|---|---|---|
| E01 | 0:48.0–0:56.0 | "THE QUIET FIELD" başlık metni video üzerine bindirilmiş, üst %40 alanı kaplayarak güvenli alanı ihlal etmiş | ① KARE (Safe Area) · ④ TESLİM | Klip 7 (0:48.0) | Kurguda metin katmanı kaldırılacak; son sahne temiz video olarak teslim edilecek (plan §TESLİM YAPISI kuralı). |

---

## 7. 🎯 KARAR VE EYLEM PLANI

```
1. YAYIN DURUMU: ✅ ASGARİ SET GEÇTİ (① 9,8 · ② 10,0 · ⑤ 10,0).
   ✅ ON İKİ MERCEK TAMAMLANDI (12/12).
   Depo tarihinin EN YÜKSEK SKORLU, EN TEMİZ ve TEK BİR HAYALET PARÇA BİLE ÜRETMEYEN İLK FİLMİDİR.
2. KURGU DÜZELTMESİ (ZORUNLU):
   0:48.0–0:56.0 arasındaki "THE QUIET FIELD" başlık bindirmesi derhal kaldırılmalı ve son klip temiz
   görüntüyle kapatılmalıdır. Kapak metni yalnızca platform küçük resminde (thumbnail) yer alacaktır.
3. KABUL EDİLEN KUSUR: Yoktur.
```
