# 🌿 THE SUNKEN GARDEN — DİKEY TİMELAPSE PLANI

> **Format:** 9:16 dikey short · **Izgara:** 7 sahne × 8,0 sn = 56,0 sn
> **Tarih:** 2026-10-23
> ⛔ **SAHİP UYARISI:** Brief 8 sahne önerdi → **Plan 7 sahne ile yazıldı** (§2.1 · DERS 58 kesin kuralı). Kapı 7 dışını BLOCK'lar.

---

# 0. KONSEPT KAPISI — VAAT / DİRENÇ / BEDEL [§6]

```
VAAT:    Terk edilmiş, yaprak dolu beton havuz 56 saniyede oturma alanı,
         merdiven ve ateş çukuru olan mavi saatte insanlı batık bahçeye dönüşür.

DİRENÇ:  Havuzun çukur geometrisi (≈ 1,5 m derinlik) her malzemeyi aşağıya indirmeyi
         zorlaştırır — tüm kalas, toprak, ateş çukuru taşı ve saksı BASAMAKLARDAN
         taşınır; basamaklar S00'dan S06'ya her kesmede görünür giriş yolu olarak
         ekranda aktiftir. Her şey tepeden aşağı iner, yukarı çıkmaz.
         EKRANDA NASIL: her sahnede malzeme dolu çuval / kasa / kol basamaklar
         boyunca harekette; S01'de mini yükleyici basamak ağzına kadar gelip
         geri döner (çukura inemez — bu direnç).

BEDEL:   Krom merdiven dayanağı S05'te sökülür (değişmeyen işaretin listeden
         çıkışı budur ve plana not düşülmüştür). Eski havuzun kimliği gidiyor;
         yerine başka bir şey geliyor.
```

**Kabul testleri:**

```
① TEK KARE TESTİ    S03 donmuş karesi: ahşap karkas havuzun tabanında,
                     etrafı çakıl, basamaklarda işçi — tür (dönüşüm) VE
                     aşama (yapı kuruldu, bitirmedi) 1 sn'de okunur: ✅
② KİNETİK BAĞIMSIZLIK  Her sahne metin/anlatıcı olmadan görülür değişim taşır:
                     yaprak yığını → temiz beton → çakıl → karkas →
                     hardwood planking → merdiven+ateş → bitkiler+insanlar: ✅
③ BAŞLIK ŞEMASI    "From Dead Pool to Sunken Garden" ≤5 kelime: ✅
④ OMURGA CÜMLESİ  Yaprak yığını açılır → taban yıkanır → çakıl serilir →
                   karkas oturur → hardwood planking + kasalar → merdiven + ateş →
                   bitkiler + insanlar: 7 vuruş, 7 sahne ✅
```

---

# 1. KÜNYE

```
IZGARA         7 sahne × 8,0 sn = 56,0 sn
SAHNE BLOĞU    7 sahne × 8,0 sn = 56,0 sn
KAPAK KARTI    1 kart × 5,0 sn (sonda · erime ≤0,5 sn · kaynak G7)
MÜZİK          ⛔ YOK — diegetik ses yatağı (çakıl, çekiç, ateş)
YASAK KELİME   crane · hoist · jib · derrick · truss · deck
               (deck eşsesli; yerine "hardwood planking" kullanılır)
PAYLAŞIM       2x — ~28,0 sn sahne bloğu + kart
ARAÇ KUTU SETİ {5, 10} sn (ölçüldü: 10,0 sn · tavan 9,00 sn ≥ 8,0 sn) — [ARAC_KARTLARI §2]

İŞLEV ANI:     S06 — ateş çukuru yakılır, ip ışıklar açık; iki kişi oturur
AÇILIŞ NESNESİ: G0 — havuzun derin ucunda yaprak yığını + kürek dalan işçi
DÖNGÜ KAFİYESİ: G0 boş beton havuz orta kadraj → G7 aynı orta kadrajda
                ateş çukuru + insanlar; merak orada doğdu, cevap orada
MERAK SORUSU:  "Bu havuza ne yapıyorlar?"

TAVAN (ara hâl): %25 (MONOTONIK_ILERLEME §1 · yo-yo engeli)
COMMITTED BASELINE: G0'dan sonra açığa çıkan temiz beton taban — bir daha
                    örtülmez, kaybolmaz. Her G'de görünür kalır.

AÇILIŞ DÜZENİ (S0): ① kürek yaprak yığınına dalmış (NESNE)
   ② eylem ilk karede (DOKUNUŞ: çuval dolduruluyor)
   ③ ipucu: basamak ağzında boş kasa (GELECEĞİN BİR PARÇASI)
   ④ S01 ilk kesmede basamaklar yarı boş (ÖLÇEK)
```

---

# 2. DEĞİŞMEZLER TABLOSU [§3] — her promptta birebir kopyalanır

```
┌─ KAMERA İSTASYONU (A) ──────────────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100                                 │
│ yükseklik     1,2 m — havuzun derin-uç kenar beton kaidesi üzerinde         │
│               (kamera havuzu dışında, kenar üstünde duruyor)                │
│ mesafe        havuzun sığ-uç ön duvarından 8,5 m                            │
│ bakış açısı   bearing 0° (kuzeye) · tilt −15° aşağı bakış · roll 0°        │
│ sabitleme     "bolted to a fixed tripod, absolutely zero movement"          │
│                                                                             │
│ Tilt formülü (KAMERA_DILI §3): değişim YÜKSEKLİK + ALAN                    │
│   δ = (h_kamera − h_zemin) / D = (1,2 − 0) / 8,5 = 0,141                 │
│   tilt = arctan(0,141) ≈ −8°; pratik −15° (derin uç tabanı dahil)         │
│   ⭐ Tilt ≠ 0 → KAMERA_DILI §3 formülü uygulandı                           │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — 3 sabit ──────────────────────────────────────────────┐
│ ① sığ-uç beton basamaklar (3 basamak) — kadrajın üst-orta bandında,         │
│   her kesmede görünür; malzeme giriş rotası                                 │
│ ② sol kenarda eski krom merdiven dayanağı — S00'dan S04'e dek görünür;     │
│   S05'te İŞÇİLER TARAFINDAN SÖKÜLÜYOR (I2V'de FİİLLE yazılır)             │
│   ⛔ S05'ten sonra bu çapa listesinden ÇIKAR                                 │
│ ③ arka tuğla duvar (köşede eski taşma kanalı borusuyla) — filmin tüm       │
│   sahnelerinde aynı yerde, aynı boyutta                                     │
│                                                                             │
│ ⛔ Çapalar her promptta BİREBİR aynı kelimelerle yazılır.                    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ───────────────────────────────────────────────────────────┐
│ kadraj        9:16 dikey · tilt −15° nedeniyle ufuk üst üçte birde          │
│ havuz tabanı  kare yüksekliğinin ~%55'inde                                  │
│ basamak tepesi kare yüksekliğinin ~%22'sinde (güvenli alan içinde)          │
│ havuz duvarı  kare genişliğinin tamamına yakın — ring etkisi                │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — tamamlanmış hâlin sabit geometrisi ───────────────────────────┐
│ havuz formu   dikdörtgen, yaklaşık 7 m × 4 m · derinlik 1,5 m (derin uç)   │
│ duvar malzeme eski beton, üstü çatlamış · pas izleri derin uçta            │
│ basamaklar    sığ uçta 3 basamak · her biri ≈ 35 cm yükseklik · beton     │
│ taşma kanalı  sağ arka köşede paslanmış boru ucu · boru 10 cm çaplı        │
│ tuğla duvar   arka duvarda sarı-kahve pişmiş tuğla · 10 sıra görünür       │
│ tamamlanmış:  hardwood planking + ateş çukuru + 6 saksı kasası +            │
│               yeni ahşap merdiven + ip ışıklar + bambu + oturma grubu      │
│ "When finished this will be a sunken garden courtyard."                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 3. GÜNEŞ SAATİ KİLİDİ [§5]

```
G0  sabah gri · azimut 112° · elevation 18° · gölge uzun, KB'ya
G1  öğle öncesi · azimut 142° · elevation 38° · kısa gölge, K'ya
G2  öğle geçmiş · azimut 182° · elevation 42° · hafif gölge, KB'ya
G3  öğlenden sonra · azimut 215° · elevation 32° · gölge BKB'ya
G4  ikindi · azimut 238° · elevation 22° · gölge uzun, KB
G5  akşamüstü · azimut 255° · elevation 12° · altın saat
G6  erken alacakaranlık · azimut 268° · elevation 4° · warm amber
G7  MAVİ SAAT · güneş ufkun −3° altında · ip ışıklar + ateş ana aydınlatma

⛔ Sahne içi: güneş TEK YÖNDE ilerler.
⛔ Sahneler arası: G0→G7 sabahtan mavi saate tek yön.
⭐ G7 zifiri değildir: tuğla duvar, basamaklar, ufuk silüeti okunur.
```

---

# 4. AŞAMA MERDİVENİ [§4]

## Söküm / Geçici Ekipman

- **Krom merdiven dayanağı:** G0'da sol kenarda → S05 I2V'sinde FİİLLE sökülen → G6'dan sonra yok.
- **Mini yükleyici:** Yalnız S01'de basamak ağzında → S01 sona erince çerçeve dışı.
- **Çuvallar / el arabası:** S00–S02 boyunca → S03'te temiz.

## Loop Satırı

G7 ile G0 aynı kadrajda: boş/dolu havuz farkı aynı perspektiften okunur. Ateş çukuru G0'daki küreğin tam yerine geliyor.

## Monoton Büyüme Yasası

Her aşama öncekinin her şeyini + yeni iş taşır.
COMMITTED BASELINE: G1'den itibaren açığa çıkan temiz beton taban donmuştur.

| S | SÜRE | AŞAMA | EKRANDA VAR OLAN | YENİ OLAN | MEVSİM TAŞIYICISI | KANIT NESNESİ | TAVAN |
|:-:|---:|---|---|---|---|---|:-:|
| 0 | 8,0 | Temizlik I | Yaprak yığını + krom dayanak + basamaklar + tuğla duvar | Kürekle çuval dolduruluyor; basamaktan çıkıyor | Sonbahar yaprakları | Derin uçta ~1 m² temiz beton | %25 |
| 1 | 8,0 | Temizlik II + yıkama | +açık beton taban | Basınçlı yıkama; taban koyu gri ıslak; çatlak çizgiler | Islak beton dokusu | Taban rengi açık→koyu | %50 |
| 2 | 8,0 | Drenaj çakılı | +temiz beton zemin | Çakıl basamaklardan sepetlerle iniyor; tırmıkla düzleniyor | Çakıl yığını basamak dibinde | Çakıl tabanın %40'ında | %75 |
| 3 | 8,0 | Ahşap karkas | +çakıl zemin | Kare ahşap karkas derin uca konumlandırılıyor; vida | Kare form tabanın %40'ında | Karkas grid çizgileri | %25 |
| 4 | 8,0 | Hardwood planking + saksı kasaları | +karkas | Ahşap plankalar karkasa vida; 3 saksı kasası iniyor | Açık ahşap yüzey rengi | Planking %75 tamamlandı | %75 |
| 5 | 8,0 | Merdiven + ateş çukuru + krom dayanak sökümü | +planking + kasalar; ⛔ krom ÇIKIYOR | PHASE A: krom dayanak sökülüp kenara; PHASE B: basamaklara ahşap kaplama + taş ateş çukuru | Yeni merdiven ahşap rengi | Ahşap merdiven + taş halka tamam | %50 |
| 6 | 8,0 | Bitkiler + oturma + ip ışık + insanlar | +merdiven + ateş çukuru | Bambular kasalara; 2 bank + minder; ip ışık; işçiler çıkıyor; 2 kişi iniyor; ateş yakılıyor | Mavi saat + ateş ışığı | Ateş alevleri + ip ışık kümeleri | — |

> ⭐ S06 son klibi = 4 sn OLAY + 4 sn TUTUŞ [DERS 85 · C2-b]

---

# 5. KARE TABLOSU — 8 görsel (G0…G7), 7 I2V

| G | ROL | EKRANDA NE GÖRÜNÜR | AYDINLATMA |
|:-:|---|---|---|
| G0 | İlk kare (S00 başı) | Derin uçta yaprak yığını; kürek dalan işçi; basamakta çuval taşıyan ikinci işçi; krom dayanak sol; tuğla duvar arka | Sabah gri, uzun gölge |
| G1 | S00 sonu / S01 başı | Taban büyük ölçüde açık, koyu ıslak beton; sığ uçta küçük yaprak yığını; mini yükleyici çekti | Öğle öncesi, kısa gölge |
| G2 | S01 sonu / S02 başı | Tamamen temiz ıslak taban; çatlak çizgiler; derin uçta küçük çakıl yığını; krom dayanak solda | Öğle geçmiş, minimal gölge |
| G3 | S02 sonu / S03 başı | Tabanın %40'ı çakıl kaplı; sığ uçta çakıl sepetleri; krom dayanak solda | İkindi öncesi, orta gölge |
| G4 | S03 sonu / S04 başı | Çakıl tüm tabanda; ahşap karkas derin uca oturmuş; krom dayanak solda | İkindi, uzun gölge |
| G5 | S04 sonu / S05 başı | Hardwood planking tamamlanmış; 3 saksı kasası sağda toprakla dolu; krom dayanak solda | Akşamüstü altın |
| G6 | S05 sonu / S06 başı | Ahşap merdiven + taş ateş çukuru halkası; krom dayanak YOK; 6 saksı kasası dolu; ip ışıklar sönük duvarda | Erken alacakaranlık |
| G7 | ⭐ USTA KARE — S06 sonu | Bambu + süs otları kasalarda; 2 bank + minderler; ip ışıklar açık; ateş çukurunda alevler; 2 kişi oturmuş | Mavi saat · −3° |

---

# 6. SAHNE PLAN KARTLARI — BEŞ SORU [SAHNE_PLAN_KARTI §1]

### S00 — Temizlik I

| Soru | Cevap |
|---|---|
| ① MALZEME NEREDE? | Derin uçta yaprak + moloz yığını (G0'da görünür) |
| ② HANGİ ARAÇ / KİŞİ? | 2 işçi (kürek + eller) + el arabası; çuvallarla basamaktan taşıma |
| ③ NEREYE OTURUYOR? | Çuvallar basamakları çıkıp kadraj dışına |
| ④ KLİP BİTTİĞİNDE NE DEĞİŞTİ? | G1: derin uç temiz, sığ uçta küçük yığın |
| ⑤ SABİT KALAN? | Kamera · krom dayanak · basamaklar · tuğla duvar · taşma kanalı |

### S01 — Temizlik II + Basınçlı Yıkama

| Soru | Cevap |
|---|---|
| ① MALZEME NEREDE? | Basınçlı yıkama makinesi basamak ağzına inmiş (G1'de görünür) |
| ② HANGİ ARAÇ / KİŞİ? | 1 işçi + yıkama tabancası; taban soldan sağa taranıyor |
| ③ NEREYE OTURUYOR? | Su tabandan drenaj ızgarasına akıyor |
| ④ KLİP BİTTİĞİNDE NE DEĞİŞTİ? | G2: tamamen temiz koyu gri taban; çatlak çizgiler okunur |
| ⑤ SABİT KALAN? | Kamera · krom dayanak · basamaklar · tuğla duvar · taşma kanalı |

### S02 — Drenaj Çakılı

| Soru | Cevap |
|---|---|
| ① MALZEME NEREDE? | Çakıl basamak ağzında büyük yığın + el arabası (G2'de görünür) |
| ② HANGİ ARAÇ / KİŞİ? | 2 işçi: biri el arabasıyla taşıyor, biri tırmıkla düzlüyor |
| ③ NEREYE OTURUYOR? | Derin uçtan başlayarak beton tabana yayılıyor |
| ④ KLİP BİTTİĞİNDE NE DEĞİŞTİ? | G3: tabanın %40'ı çakıl kaplı; sığ uçta henüz yok |
| ⑤ SABİT KALAN? | Kamera · krom dayanak · basamaklar · tuğla duvar · temiz beton (kalan kısım) |

### S03 — Ahşap Karkas

| Soru | Cevap |
|---|---|
| ① MALZEME NEREDE? | Ahşap traversler basamak ağzına yığılmış (G3'te görünür) |
| ② HANGİ ARAÇ / KİŞİ? | 2 işçi: biri kiriş tutuyor, biri akülü tornavidayla sabitliyor |
| ③ NEREYE OTURUYOR? | Derin uç çakıl üstüne kare karkas; çakıl üzerinde yükseltilmiş |
| ④ KLİP BİTTİĞİNDE NE DEĞİŞTİ? | G4: karkas grid görünür; çakıl tüm tabanda COMMITTED |
| ⑤ SABİT KALAN? | Kamera · krom dayanak · basamaklar · tuğla duvar · çakıl taban |

### S04 — Hardwood Planking + Saksı Kasaları

| Soru | Cevap |
|---|---|
| ① MALZEME NEREDE? | Ahşap plankalar basamak ağzına istiflenmiş (G4'te görünür) |
| ② HANGİ ARAÇ / KİŞİ? | 2 işçi: biri planka hizalıyor, biri vidayla sabitliyor |
| ③ NEREYE OTURUYOR? | Karkas çıtaları üstüne — "planks seat onto the frame joists" |
| ④ KLİP BİTTİĞİNDE NE DEĞİŞTİ? | G5: açık ahşap planking yüzeyi tamamlanmış; 3 saksı kasası sağda |
| ⑤ SABİT KALAN? | Kamera · krom dayanak · basamaklar · tuğla duvar · çakıl + karkas |

### S05 — Merdiven + Ateş Çukuru + Krom Dayanak Sökümü

| Soru | Cevap |
|---|---|
| ① MALZEME NEREDE? | Ahşap kaplama plakaları + taş halkası kayaları basamak ağzında (G5'te görünür) |
| ② HANGİ ARAÇ / KİŞİ? | SERİ: PHASE A) 2 işçi krom dayanak söküyor; PHASE B) aynı 2 işçi merdiven + ateş çukuru |
| ③ NEREYE OTURUYOR? | Kaplama → eski basamakların üstüne; taş halka → hardwood planking ortasına |
| ④ KLİP BİTTİĞİNDE NE DEĞİŞTİ? | G6: merdiven yeni, taş halka tamam, krom dayanak YOK |
| ⑤ SABİT KALAN? | Kamera · basamaklar · tuğla duvar · hardwood planking · kasalar |

> **⛔ FAZ KAPISI [MONOTONIK_ILERLEME §3]:** I2V'de PHASE A (0–3 sn) söküm biter, SONRA PHASE B (3–8 sn) montaj başlar. İki eylem ayrı BÖLGE ve ayrı zaman penceresi.

### S06 — Bitkiler + Oturma + İp Işık + İnsanlar

| Soru | Cevap |
|---|---|
| ① MALZEME NEREDE? | Bambu fidanlar basamak ağzında (G6'da görünür); bank ve minderler basamak üstünde |
| ② HANGİ ARAÇ / KİŞİ? | 2 işçi bambuları dikiyor → çıkıyor; 2 misafir iniyor → oturuyor |
| ③ NEREYE OTURUYOR? | Bambu → kasalara; banklar → hardwood planking kenarına; misafirler → banklara |
| ④ KLİP BİTTİĞİNDE NE DEĞİŞTİ? | G7: yeşillik + oturma + ateş + ip ışık + 2 insan |
| ⑤ SABİT KALAN? | Kamera · basamaklar · tuğla duvar · hardwood planking + ateş çukuru + tüm COMMITTED |

**⭐ FİNAL KLİBİ = 4 sn OLAY + 4 sn TUTUŞ:**
- 0–4 sn: ateş yakılır, ip ışıklar açılır, 2 kişi iner ve oturur
- 4–8 sn: ateş ve ışıklar sabit; figürler sakin; mavi saat rengi

---

# 7. IŞIK FİNALİ NOTLARI [ISIK_FINALI_KILAVUZU]

```
G7 IP IŞIĞI:   armatürler G5'te sönük hâlde duvarda görünür (malzeme olarak takıldı)
               G6'da sönük ama kadrajda · G7'de TEK KAREDE açık [A28-b]
               "first the string lights switch on, then the fire pit ignites"

ATEŞ ÇUKURU:  "a small bundle of kindling ignites from a single match; the flame
               grows steadily and orange light pools across the stone ring"
               → pozitif FİİLLE yazılır; "no bloom, no haze" negatifte

MAVİ SAAT:    güneş −3° · enlem ~37° · Ekim → batıştan ~17 dk sonra
               zifiri değildir: tuğla duvar, basamak, ufuk silüeti okunur
               Üç ışık kaynağı: ① ip ışıklar (warm white)
                                ② ateş çukuru (orange)
                                ③ mavi saat gökyüzü (cool blue)

⭐ "Işık bir MALZEMEDİR — kaynağı önceden kadrajda" [ISIK_FINALI §0]
```

---

# 8. MEKANSAL İZOLASYON [MEKANSAL_IZOLASYON §1]

```
ZONE A: HAVUZ TABANI (z = 0 m · y: %40-%100 kadrajda)
        → tüm inşaat eylemleri buraya kilitli
        STRICT ZONE IMMUNITY: çakıl yayıldıktan sonra taban kaybolmaz;
        hardwood planking oturunca çakıl COMMITTED olarak dondurulur

ZONE B: BASAMAKLAR (z = 0-1,5 m · y: %20-%40 kadrajda)
        → yalnız malzeme GEÇİŞ ROTASI; inşaat eylemi OLMAZ
        STRICT ZONE IMMUNITY (yapı yok, yalnız taşıma trafiği)

ZONE C: ÜSTÜ / ÇEVRE (z > 1,5 m · y: %0-%20 kadrajda)
        → krom dayanak S05 sökümü geçici; sonra BOŞ
        STRICT ZONE IMMUNITY (mini yükleyici basamak dışına çıkmaz; vinç yok)

⛔ TEK HAREKETLİ AKTÖR N_max = 1: her klipte yalnız TEK aktif araç [MEKANSAL §4]
   S01: yalnız basınçlı yıkama makinesi; el arabası durur
   S02: yalnız el arabası; tırmık aynı işçinin elinde (2 kişi OK, 2 araç ⛔)
```

---

# 9. RİSK ANALİZİ VE PİLOT

| Risk | Sahne | Neden | Önlem |
|---|---|---|---|
| Hardwood planking "birden beliriyor" | S03→S04 | Karkas S03'te; kaplama S04'te; yo-yo tuzağı | %25 tavan kilidi; COMMITTED; S03 sonunda karkas grid görünür |
| Krom dayanak sessizce kayboluyor | S05 | "Değişmeyen işaret" listeden çıkıyor | I2V'de FİİLLE: "two workers unbolt and carry the chrome rail bracket beyond frame left" |
| Mavi saatte "yavaş yanan ışık" | S06 | Model "gradually glowing" üretir | "TEK KAREDE yanar" · "gently/slowly" yasak |
| İki araç eş zamanlı | S05 | N_max=1 ihlali | I2V seri: söküm BITER, SONRA merdiven başlar; paralel değil |
| "deck" terimi | Tüm | YASAK KELİME listesinde | Yerine "hardwood planking" veya "timber floor boards" |

## 🧪 PİLOT ÜÇLÜ [DERS 62 · KILAVUZ_REHBERI §8 adım 2b]

- **(a) Referans:** G7 USTA KARE + 3 nirengi piksel: ① tuğla duvar sol köşe ② taşma kanalı sağ köşe ③ basamak sol ayak
- **(b) İlk halka:** S0 (G0 → G1) — açılış nesnesi ve ilk temizlik vuruşu [C2-h]
- **(c) FİNAL klip S6:** (G6 → G7) — ateş yakılır; ip ışıklar açık; 2 kişi iner ve oturur — 4+4 bütçe [C2-b]
- **(c′) En zor montaj:** S5 — krom dayanak söküm + merdiven kaplama seri (iki bölge, faz kapısı kritik)

---

# 10. TESLİM YAPISI

```
SAHNE BLOĞU   7 sahne × 8,0 sn = 56,0 sn
KAPAK KARTI   1 kart × 5,0 sn (sonda · erime ≤0,5 sn · kaynak G7)
──────────────────────────────────────────
TOPLAM        61,0 sn

KAPAK KAYNAĞI: G7 · merkez ateş çukuru + mavi saat + ip ışık kümeleri
BAŞLIK:        "From Dead Pool to Sunken Garden"
               Alternatif: "Abandoned Pool → Fire Pit Courtyard"
KADRAJ KİLİTLERİ:
  - kapak çekirdeği: ateş çukuru y %45-65; başlık y %10-25 (tuğla duvar bandı)
  - 3:4 provası: ateş + merdiven kadrajda ✓
  - 1:1 provası: ateş çukuru ortalı ✓
```

---

# 11. NOTLAR VE AÇIK SORULAR

```
1. "deck" kelimesi YASAK KELİME listesine eklendi; tüm promptlarda
   "hardwood planking" veya "timber floor boards" kullanılacak.

2. S05'teki krom dayanak sökümü ile merdiven montajı aynı klipte —
   FAZ KAPISI SERİ yazımı zorunlu (söküm biter, sonra montaj başlar).

3. Işık armatürleri (ip ışıklar) G5'te sönük hâlde sahaya giriyor
   [ISIK_FINALI §0 "malzeme olarak önceden takıldı" kuralı].

4. Mini yükleyici S01'de YALNIZ basamak ağzında duruyor — havuza inemez.
   Direnç anı: "the mini loader reaches the top step but cannot descend
   into the pool; it tips its load and reverses".

5. Araç kutu seti {5, 10} sn olarak beyan edildi (tavan 9,00 sn ≥ 8,0 sn).
```

---

## 🎬 SAHNE 0 — TEMİZLİK I: YAPRAK YIĞINI VE TABAN AÇMA

### GÖRSEL PROMPT (G0)

```
Scene 0 of 7 — G0 Keyframe
An abandoned sunken concrete pool basin filled with deep autumn leaf debris in an enclosed courtyard.

STRUCTURE: When completed, this structure is a modern sunken garden courtyard created within an abandoned 7-metre by 4-metre rectangular sunken concrete pool basin, featuring a raised hardwood planking terrace platform, a central circular stacked-stone fire pit, six built-in timber planter boxes filled with lush bamboo, matching hardwood-clad entrance steps, two cushioned outdoor timber benches, and warm bistro string lights along the weathered yellow-brown rear brick wall. AT THIS STAGE: The abandoned concrete pool basin is heavily clogged with a deep mound of wet decaying brown autumn leaves, broken twigs, and garden spoil in the deep end. The aged cast-concrete floor slab is mostly obscured by the debris pile, with only one square metre of damp cracked raw cut concrete visible near the shallow end. The three raw concrete entrance steps at the shallow end show muddy shoe prints and weathered lichen patches. On the left perimeter wall, an old chrome ladder bracket remains bolted to the concrete face. Two workers in durable canvas workwear and safety boots stand in the basin: one worker plunges a square-nosed steel transfer shovel into the dense leaf pile, while the second worker holds open a heavy burlap sack to receive the spoil. Three filled burlap sacks and an empty wooden crate sit stacked on the first concrete step.

SITE / BACKGROUND: MAIN STATION. An enclosed private courtyard featuring a sunken rectangular concrete pool basin measuring 7 metres long by 4 metres wide and 1.5 metres deep. At the shallow end, three wide weathered cast-concrete steps lead down into the basin from a paved garden apron. The perimeter pool walls are cast concrete with visible shrinkage cracks and light mineral efflorescence. Directly behind the pool basin, a permanent yellow-brown kiln-fired brick boundary wall with weathered mortar joints and a small 10-centimetre rusted cast-iron overflow pipe in the right corner stands under the open sky. The rear brick wall, the shallow-end entrance steps, and the concrete perimeter coping remain permanent physical anchors across all stages.

SITE TEXTURE: Aged concrete floor with shrinkage cracks and mineral efflorescence patches, damp grey slurry and dried mud tracks from rubber work boots, weathered yellow-brown brick wall with dark soot stains and rust streaks beneath the overflow pipe, crushed pea gravel spill along the basin footing, wooden timber offcuts and tool pallets on the perimeter apron, and fallen autumn leaf debris along wall corners.

PHYSICS: The heavy decaying leaf pile rests compacted against the concrete basin floor while two workers stand firmly planted on the slab bearing their weight into shovels. Burlap sacks filled with damp leaves sit placed against the first concrete step. The cast-concrete basin walls and foundation footing bear structural soil loads directly into the surrounding earth.

COMPOSITION: Eye-level perspective looking down into the sunken pool courtyard at a 15-degree downward angle. The three concrete entrance steps span 216 pixels of frame width — one fifth — and keep that width throughout. The pool basin floor anchors the lower two thirds of the vertical 9:16 frame, the shallow steps occupy the mid-ground, and the rear weathered brick wall with the open sky spans the upper third.

LIGHTING: Early morning clear directional sunlight from the east, azimuth 112 degrees, elevation 18 degrees. Crisp morning shadows cast long dark silhouettes diagonally across the concrete floor toward the northwest wall.

Camera: fixed static position, 1.2 metres above the pool terrace rim, 8.5 metres from the pool shallow end wall, bearing 0 degrees, tilt 15 degrees down, roll 0 degrees.

TIME RATE: time-lapsed at the same rate across the entire frame: clouds, shadows, and workers move accelerated as two hours pass in eight seconds.

ACTIVITY: A crew of two workers fills a heavy burlap sack with decaying leaves while a hand cart moves along the apron, clearing the deep end floor and scattering damp mulch and dust. Two workers move with soft motion streaks, backs turned to the camera with no readable facial features.

NEGATIVE: No readable text, letters, digits, logos, labels, serial numbers, numbers, or brand markings anywhere in the frame, on any surface, clothing, container, tool, or equipment. The camera never pans, tilts, zooms, shakes, or changes position. The rear brick wall, shallow steps, and pool perimeter never change shape, position, size, or profile. No architectural visualisation look, no 3D rendering style, no digital plastic sheen. No cuts, no dissolves, no camera transitions.
```

### I2V PROMPT (S0)

```
The scene begins exactly as the provided image.
Camera: fixed static position, zero movement, never moves at any point. The camera does not move at any point.
The framing remains identical in the first frame and in the last frame. The three concrete entrance steps occupy exactly the same width of the frame in the first and last frame.
The sky shows soft autumn clouds that drift steadily from east to west across the courtyard.

From the first frame to about one second, the two workers drive shovels into the leaf pile and lift heavy loads into burlap sacks.
MOTION FOCUS: From the first frame to the final seconds, two workers shovel wet decaying leaves from the deep end pile into burlap sacks and haul them up the steps to the outside staging apron, uncovering the bare grey concrete slab of the pool floor beneath.

A crew of two workers continuously carries filled burlap sacks from the leaf pile up the steps to the cart. Time-lapsed at the same rate across the entire frame: cloud shadows sweep across the brick wall, and workers move in rapid continuous purposeful motion as two hours pass in eight seconds. Soft motion streaks appear on the moving workers whose backs remain turned to the camera with no readable facial features. By the final seconds, the bulk of the leaf pile is hauled out of the pool basin, revealing the damp stained concrete floor.

The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame.
```

---

## 🎬 SAHNE 1 — TEMİZLİK II: BASINÇLI YIKAMA VE YÜZEY HAZIRLIĞI

### GÖRSEL PROMPT (G1)

```
Scene 1 of 7 — G1 Keyframe
Pressure washing in progress across the damp concrete floor of the cleared pool basin.

STRUCTURE: When completed, this structure is a modern sunken garden courtyard created within an abandoned 7-metre by 4-metre rectangular sunken concrete pool basin, featuring a raised hardwood planking terrace platform, a central circular stacked-stone fire pit, six built-in timber planter boxes filled with lush bamboo, matching hardwood-clad entrance steps, two cushioned outdoor timber benches, and warm bistro string lights along the weathered yellow-brown rear brick wall. AT THIS STAGE: The leaf pile has been cleared, exposing the aged concrete pool floor slab with dark soil stains, fine shrinkage cracks, and water drainage lines. A compact yellow mini-loader sits parked on the paved apron above the steps, unable to enter the sunken basin, resting as an unmoving staging station. Down inside the basin, one worker in rubber safety boots holds a high-pressure washer wand, spraying a powerful fan jet of water that strips layers of dark grime and algae from the floor slab. The high-pressure water reveals the raw cut light grey concrete beneath, channeling dark grey slurry and water runoff toward the deep-end floor drain. A coiled heavy-duty high-pressure hose stretches from the apron down the three concrete steps onto the basin floor. The old chrome ladder bracket remains bolted to the left wall.

SITE / BACKGROUND: MAIN STATION. An enclosed private courtyard featuring a sunken rectangular concrete pool basin measuring 7 metres long by 4 metres wide and 1.5 metres deep. At the shallow end, three wide weathered cast-concrete steps lead down into the basin from a paved garden apron. The perimeter pool walls are cast concrete with visible shrinkage cracks and light mineral efflorescence. Directly behind the pool basin, a permanent yellow-brown kiln-fired brick boundary wall with weathered mortar joints and a small 10-centimetre rusted cast-iron overflow pipe in the right corner stands under the open sky. The rear brick wall, the shallow-end entrance steps, and the concrete perimeter coping remain permanent physical anchors across all stages.

SITE TEXTURE: Aged concrete floor with shrinkage cracks and mineral efflorescence patches, damp grey slurry and dried mud tracks from rubber work boots, weathered yellow-brown brick wall with dark soot stains and rust streaks beneath the overflow pipe, crushed pea gravel spill along the basin footing, wooden timber offcuts and tool pallets on the perimeter apron, and fallen autumn leaf debris along wall corners.

PHYSICS: The pressure washer wand rests clamped in the operator's grip while the worker stands braced on the wet concrete slab. The mini-loader sits securely parked on the paved apron above the steps, bearing its weight on four rubber tires without descending into the pool. High-pressure water spray presses into surface grime and drains toward the floor outlet. The concrete foundation slab bears hydrostatic and earth pressures.

COMPOSITION: Eye-level perspective looking down into the sunken pool courtyard at a 15-degree downward angle. The three concrete entrance steps span 216 pixels of frame width — one fifth — and keep that width throughout. The pool basin floor anchors the lower two thirds of the vertical 9:16 frame, the shallow steps occupy the mid-ground, and the rear weathered brick wall with the open sky spans the upper third.

LIGHTING: Mid-morning clear directional sunlight, azimuth 142 degrees, elevation 38 degrees. Sharp shadows fall from the pool perimeter wall onto the wet concrete floor, highlighting surface texture and water sheen.

Camera: fixed static position, 1.2 metres above the pool terrace rim, 8.5 metres from the pool shallow end wall, bearing 0 degrees, tilt 15 degrees down, roll 0 degrees.

TIME RATE: time-lapsed at the same rate across the entire frame: clouds, shadows, and workers move accelerated as two hours pass in eight seconds.

ACTIVITY: A crew of two workers operates a high-pressure washer and sweeps the water jet across the concrete floor while the mini-loader unrolls fresh hose coils along the paved apron, pushing wet slurry toward the drainage grate. Two workers move with soft motion streaks, backs turned to the camera with no readable facial features.

NEGATIVE: No readable text, letters, digits, logos, labels, serial numbers, numbers, or brand markings anywhere in the frame, on any surface, clothing, container, tool, or equipment. The camera never pans, tilts, zooms, shakes, or changes position. The rear brick wall, shallow steps, and pool perimeter never change shape, position, size, or profile. No architectural visualisation look, no 3D rendering style, no digital plastic sheen. No cuts, no dissolves, no camera transitions.
```

### I2V PROMPT (S1)

```
The scene begins exactly as the provided image.
Camera: fixed static position, zero movement, never moves at any point. The camera does not move at any point.
The framing remains identical in the first frame and in the last frame. The three concrete entrance steps occupy exactly the same width of the frame in the first and last frame.
The sky shows soft autumn clouds that drift steadily from east to west across the courtyard.

From the first frame to about one second, the worker sweeps the high-pressure spray across the concrete floor, lifting dark algae and grime.
MOTION FOCUS: From the first frame to the final seconds, the worker sweeps the high-pressure water spray across the concrete slab from the shallow end to the deep end drain, washing away dark grime and silt into the drainage outlet.

A crew of two workers continuously carries washing tools from the staging cart down the steps to the floor. Time-lapsed at the same rate across the entire frame: cloud shadows sweep across the brick wall, and workers move in rapid continuous purposeful motion as two hours pass in eight seconds. Soft motion streaks appear on the moving workers whose backs remain turned to the camera with no readable facial features. By the final seconds, the entire concrete pool floor is thoroughly washed clean, glistening wet with distinct concrete cracks visible under daylight.

The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame.
```

---

## 🎬 SAHNE 2 — DRENAJ ÇAKILI VE ZEMİN DÜZLEME

### GÖRSEL PROMPT (G2)

```
Scene 2 of 7 — G2 Keyframe
Spreading washed drainage pea gravel across the clean concrete floor of the pool basin.

STRUCTURE: When completed, this structure is a modern sunken garden courtyard created within an abandoned 7-metre by 4-metre rectangular sunken concrete pool basin, featuring a raised hardwood planking terrace platform, a central circular stacked-stone fire pit, six built-in timber planter boxes filled with lush bamboo, matching hardwood-clad entrance steps, two cushioned outdoor timber benches, and warm bistro string lights along the weathered yellow-brown rear brick wall. AT THIS STAGE: The concrete floor is clean and dry. Drainage pea gravel installation is in active progress across the deep end of the basin, covering roughly 40 percent of the floor slab to a depth of 10 centimetres. A large stockpile of washed grey and amber pea gravel sits on the paved apron above the steps. Two workers in canvas trousers and work boots are in the basin: one worker tips a heavy two-wheeled garden cart to deposit fresh pea gravel onto the concrete slab, while the second worker uses a wide steel landscaping rake to spread and grade the gravel into a flat, compacted drainage layer. Several empty woven poly bags and a hand tamper rest neatly stacked against the shallow concrete steps. The chrome ladder bracket remains bolted to the left concrete wall.

SITE / BACKGROUND: MAIN STATION. An enclosed private courtyard featuring a sunken rectangular concrete pool basin measuring 7 metres long by 4 metres wide and 1.5 metres deep. At the shallow end, three wide weathered cast-concrete steps lead down into the basin from a paved garden apron. The perimeter pool walls are cast concrete with visible shrinkage cracks and light mineral efflorescence. Directly behind the pool basin, a permanent yellow-brown kiln-fired brick boundary wall with weathered mortar joints and a small 10-centimetre rusted cast-iron overflow pipe in the right corner stands under the open sky. The rear brick wall, the shallow-end entrance steps, and the concrete perimeter coping remain permanent physical anchors across all stages.

SITE TEXTURE: Aged concrete floor with shrinkage cracks and mineral efflorescence patches, damp grey slurry and dried mud tracks from rubber work boots, weathered yellow-brown brick wall with dark soot stains and rust streaks beneath the overflow pipe, crushed pea gravel spill along the basin footing, wooden timber offcuts and tool pallets on the perimeter apron, and fallen autumn leaf debris along wall corners.

PHYSICS: The spreading pea gravel bed rests directly on the cleaned concrete floor slab, distributing granular dead loads across the basin. The steel cart sits planted on its rubber wheels and support legs, tipped to discharge its payload. The two workers stand braced on the gravel and concrete surface handling rakes and shovels. The pool basin walls bear surrounding ground loads rigidly.

COMPOSITION: Eye-level perspective looking down into the sunken pool courtyard at a 15-degree downward angle. The three concrete entrance steps span 216 pixels of frame width — one fifth — and keep that width throughout. The pool basin floor anchors the lower two thirds of the vertical 9:16 frame, the shallow steps occupy the mid-ground, and the rear weathered brick wall with the open sky spans the upper third.

LIGHTING: Midday clear direct sunlight, azimuth 182 degrees, elevation 42 degrees. Minimal shadows cast along the south-facing basin wall, illuminating the warm amber and grey pebbles of the drainage bed.

Camera: fixed static position, 1.2 metres above the pool terrace rim, 8.5 metres from the pool shallow end wall, bearing 0 degrees, tilt 15 degrees down, roll 0 degrees.

TIME RATE: time-lapsed at the same rate across the entire frame: clouds, shadows, and workers move accelerated as two hours pass in eight seconds.

ACTIVITY: A crew of two workers pours fresh pea gravel from a two-wheeled cart onto the concrete floor and spreads the gravel bed evenly with rakes, leaving a neat gravel stockpile by the steps. Two workers move with soft motion streaks, backs turned to the camera with no readable facial features.

NEGATIVE: No readable text, letters, digits, logos, labels, serial numbers, numbers, or brand markings anywhere in the frame, on any surface, clothing, container, tool, or equipment. The camera never pans, tilts, zooms, shakes, or changes position. The rear brick wall, shallow steps, and pool perimeter never change shape, position, size, or profile. No architectural visualisation look, no 3D rendering style, no digital plastic sheen. No cuts, no dissolves, no camera transitions.
```

### I2V PROMPT (S2)

```
The scene begins exactly as the provided image.
Camera: fixed static position, zero movement, never moves at any point. The camera does not move at any point.
The framing remains identical in the first frame and in the last frame. The three concrete entrance steps occupy exactly the same width of the frame in the first and last frame.
The sky shows soft autumn clouds that drift steadily from east to west across the courtyard.

From the first frame to about one second, the worker tips the cart to discharge fresh pea gravel onto the concrete slab.
MOTION FOCUS: From the first frame to the final seconds, two workers wheel pea gravel from the delivery stockpile at the top steps down into the basin and rake the gravel across the concrete slab into a uniform level layer.

A crew of two workers continuously delivers pea gravel from the stockpile down the steps to the spreading bed. Time-lapsed at the same rate across the entire frame: cloud shadows sweep across the brick wall, and workers move in rapid continuous purposeful motion as two hours pass in eight seconds. Soft motion streaks appear on the moving workers whose backs remain turned to the camera with no readable facial features. By the final seconds, the pea gravel bed is fully graded and tamped across the deep end, creating a firm and level drainage base.

The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame.
```

---

## 🎬 SAHNE 3 — TAŞIYICI AHŞAP KARKAS MONTAJI

### GÖRSEL PROMPT (G3)

```
Scene 3 of 7 — G3 Keyframe
Assembly of the structural timber subframe grid over the leveled pea gravel bed.

STRUCTURE: When completed, this structure is a modern sunken garden courtyard created within an abandoned 7-metre by 4-metre rectangular sunken concrete pool basin, featuring a raised hardwood planking terrace platform, a central circular stacked-stone fire pit, six built-in timber planter boxes filled with lush bamboo, matching hardwood-clad entrance steps, two cushioned outdoor timber benches, and warm bistro string lights along the weathered yellow-brown rear brick wall. AT THIS STAGE: The pea gravel drainage layer now spans the entire concrete basin floor, fully compacted and level. Construction of the treated structural timber subframe is actively underway across the deep half of the basin. Heavy pressure-treated timber beams (100 mm × 100 mm square section) form a rigid grid of joists resting upon concrete leveling blocks embedded within the pea gravel. Two carpenters in tool belts work together on the grid: one carpenter aligns a longitudinal timber joist against a cross-brace, while the second kneels and drives structural zinc-coated screws through galvanized corner brackets using a cordless impact driver. A stack of uncut timber beams, a carpenter's spirit level, and an open wooden crate of structural hardware sit staged on the shallow-end gravel bed. The chrome ladder bracket remains bolted on the left wall.

SITE / BACKGROUND: MAIN STATION. An enclosed private courtyard featuring a sunken rectangular concrete pool basin measuring 7 metres long by 4 metres wide and 1.5 metres deep. At the shallow end, three wide weathered cast-concrete steps lead down into the basin from a paved garden apron. The perimeter pool walls are cast concrete with visible shrinkage cracks and light mineral efflorescence. Directly behind the pool basin, a permanent yellow-brown kiln-fired brick boundary wall with weathered mortar joints and a small 10-centimetre rusted cast-iron overflow pipe in the right corner stands under the open sky. The rear brick wall, the shallow-end entrance steps, and the concrete perimeter coping remain permanent physical anchors across all stages.

SITE TEXTURE: Aged concrete floor with shrinkage cracks and mineral efflorescence patches, damp grey slurry and dried mud tracks from rubber work boots, weathered yellow-brown brick wall with dark soot stains and rust streaks beneath the overflow pipe, crushed pea gravel spill along the basin footing, wooden timber offcuts and tool pallets on the perimeter apron, and fallen autumn leaf debris along wall corners.

PHYSICS: The structural timber joists rest securely upon concrete leveling blocks footed into the compacted pea gravel bed. The corner brackets sit clamped and bolted with structural screws into the timber members, transferring dead loads through the subframe to the gravel foundation. The two carpenters kneel and stand planted firmly on timber beams and gravel.

COMPOSITION: Eye-level perspective looking down into the sunken pool courtyard at a 15-degree downward angle. The three concrete entrance steps span 216 pixels of frame width — one fifth — and keep that width throughout. The pool basin floor anchors the lower two thirds of the vertical 9:16 frame, the shallow steps occupy the mid-ground, and the rear weathered brick wall with the open sky spans the upper third.

LIGHTING: Early afternoon sunlight from the southwest, azimuth 215 degrees, elevation 32 degrees. Diagonal shadows cast by the perimeter wall begin stretching across the gravel bed and timber joist grid.

Camera: fixed static position, 1.2 metres above the pool terrace rim, 8.5 metres from the pool shallow end wall, bearing 0 degrees, tilt 15 degrees down, roll 0 degrees.

TIME RATE: time-lapsed at the same rate across the entire frame: clouds, shadows, and workers move accelerated as two hours pass in eight seconds.

ACTIVITY: A crew of two carpenters carries square timber beams from a hand cart and bolts the joist frames into rigid alignment with cordless impact drivers, checking levels and securing angle brackets. Two workers move with soft motion streaks, backs turned to the camera with no readable facial features.

NEGATIVE: No readable text, letters, digits, logos, labels, serial numbers, numbers, or brand markings anywhere in the frame, on any surface, clothing, container, tool, or equipment. The camera never pans, tilts, zooms, shakes, or changes position. The rear brick wall, shallow steps, and pool perimeter never change shape, position, size, or profile. No architectural visualisation look, no 3D rendering style, no digital plastic sheen. No cuts, no dissolves, no camera transitions.
```

### I2V PROMPT (S3)

```
The scene begins exactly as the provided image.
Camera: fixed static position, zero movement, never moves at any point. The camera does not move at any point.
The framing remains identical in the first frame and in the last frame. The three concrete entrance steps occupy exactly the same width of the frame in the first and last frame.
The sky shows soft autumn clouds that drift steadily from east to west across the courtyard.

From the first frame to about one second, the carpenter positions a timber joist and fastens the corner bracket with an impact driver.
MOTION FOCUS: From the first frame to the final seconds, two workers carry square timber beams from the staging pile at the steps down onto the gravel bed and assemble the structural joist frame with cordless impact drivers.

A crew of two workers continuously carries timber beams from the staging pile down the steps onto the joist grid. Time-lapsed at the same rate across the entire frame: cloud shadows sweep across the brick wall, and workers move in rapid continuous purposeful motion as two hours pass in eight seconds. Soft motion streaks appear on the moving workers whose backs remain turned to the camera with no readable facial features. By the final seconds, the structural timber subframe grid is fully assembled, leveled, and securely fastened over the gravel bed.

The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame.
```

---

## 🎬 SAHNE 4 — HARDWOOD PLANKING VE SAKSI KASALARI

### GÖRSEL PROMPT (G4)

```
Scene 4 of 7 — G4 Keyframe
Installation of the warm hardwood planking platform and initial timber planter boxes.

STRUCTURE: When completed, this structure is a modern sunken garden courtyard created within an abandoned 7-metre by 4-metre rectangular sunken concrete pool basin, featuring a raised hardwood planking terrace platform, a central circular stacked-stone fire pit, six built-in timber planter boxes filled with lush bamboo, matching hardwood-clad entrance steps, two cushioned outdoor timber benches, and warm bistro string lights along the weathered yellow-brown rear brick wall. AT THIS STAGE: The structural timber subframe grid is fully anchored, and the installation of the premium hardwood planking surface is three-quarters complete across the platform. Rich golden-brown hardwood planks (140 mm wide) are laid edge-to-edge in straight parallel lines over the joists, secured with countersunk stainless steel screws. Two carpenters are actively working: one carpenter clamps a fresh hardwood plank in alignment, while the second kneels with an electric drill securing the board to the underlying timber joists. Along the right perimeter wall, three newly assembled rectangular timber planter boxes made of matching hardwood stand in position, filled halfway with dark potting soil. Stacks of precut hardwood planks and a carpenter's mitre saw stand on the remaining bare gravel section at the shallow end. The old chrome ladder bracket still remains on the left concrete wall. The shallow entrance steps remain raw concrete.

SITE / BACKGROUND: MAIN STATION. An enclosed private courtyard featuring a sunken rectangular concrete pool basin measuring 7 metres long by 4 metres wide and 1.5 metres deep. At the shallow end, three wide weathered cast-concrete steps lead down into the basin from a paved garden apron. The perimeter pool walls are cast concrete with visible shrinkage cracks and light mineral efflorescence. Directly behind the pool basin, a permanent yellow-brown kiln-fired brick boundary wall with weathered mortar joints and a small 10-centimetre rusted cast-iron overflow pipe in the right corner stands under the open sky. The rear brick wall, the shallow-end entrance steps, and the concrete perimeter coping remain permanent physical anchors across all stages.

SITE TEXTURE: Aged concrete floor with shrinkage cracks and mineral efflorescence patches, damp grey slurry and dried mud tracks from rubber work boots, weathered yellow-brown brick wall with dark soot stains and rust streaks beneath the overflow pipe, crushed pea gravel spill along the basin footing, wooden timber offcuts and tool pallets on the perimeter apron, and fallen autumn leaf debris along wall corners.

PHYSICS: The hardwood planks rest fastened directly across the timber subframe joists with stainless steel screws, bearing the dynamic loads of workers and tools. The three timber planter boxes sit heavily planted along the right wall edge, transferring soil weight through the hardwood planking into the structural joists below. The carpenters kneel planted on the secured hardwood surface.

COMPOSITION: Eye-level perspective looking down into the sunken pool courtyard at a 15-degree downward angle. The three concrete entrance steps span 216 pixels of frame width — one fifth — and keep that width throughout. The pool basin floor anchors the lower two thirds of the vertical 9:16 frame, the shallow steps occupy the mid-ground, and the rear weathered brick wall with the open sky spans the upper third.

LIGHTING: Late afternoon directional sunlight, azimuth 238 degrees, elevation 22 degrees. Warm amber sunlight rakes across the newly laid hardwood planks, casting rich elongated shadows across the timber platform and brick wall.

Camera: fixed static position, 1.2 metres above the pool terrace rim, 8.5 metres from the pool shallow end wall, bearing 0 degrees, tilt 15 degrees down, roll 0 degrees.

TIME RATE: time-lapsed at the same rate across the entire frame: clouds, shadows, and workers move accelerated as two hours pass in eight seconds.

ACTIVITY: A crew of two carpenters clamps a fresh hardwood plank in alignment from a hand cart and fastens the board into the joists, setting timber planter boxes along the wall. Two workers move with soft motion streaks, backs turned to the camera with no readable facial features.

NEGATIVE: No readable text, letters, digits, logos, labels, serial numbers, numbers, or brand markings anywhere in the frame, on any surface, clothing, container, tool, or equipment. The camera never pans, tilts, zooms, shakes, or changes position. The rear brick wall, shallow steps, and pool perimeter never change shape, position, size, or profile. No architectural visualisation look, no 3D rendering style, no digital plastic sheen. No cuts, no dissolves, no camera transitions.
```

### I2V PROMPT (S4)

```
The scene begins exactly as the provided image.
Camera: fixed static position, zero movement, never moves at any point. The camera does not move at any point.
The framing remains identical in the first frame and in the last frame. The three concrete entrance steps occupy exactly the same width of the frame in the first and last frame.
The sky shows soft autumn clouds that drift steadily from east to west across the courtyard.

From the first frame to about one second, the carpenters lay down a fresh hardwood plank and drive screws into the subframe joists.
MOTION FOCUS: From the first frame to the final seconds, two workers carry hardwood planks and timber planter boxes from the steps onto the timber joist frame, fastening the boards into a level hardwood platform and setting three planter boxes against the side wall.

A crew of two workers continuously brings hardwood planks from the staging stack down the steps onto the platform. Time-lapsed at the same rate across the entire frame: cloud shadows sweep across the brick wall, and workers move in rapid continuous purposeful motion as two hours pass in eight seconds. Soft motion streaks appear on the moving workers whose backs remain turned to the camera with no readable facial features. By the final seconds, the hardwood planking is completely laid and finished across the platform, and the first three planter boxes are fully secured.

The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame.
```

---

## 🎬 SAHNE 5 — MERDİVEN KAPLAMA, ATEŞ ÇUKURU VE SÖKÜM

### GÖRSEL PROMPT (G5)

```
Scene 5 of 7 — G5 Keyframe
The completed hardwood platform ready for step cladding, fire pit installation, and ladder bracket removal.

STRUCTURE: When completed, this structure is a modern sunken garden courtyard created within an abandoned 7-metre by 4-metre rectangular sunken concrete pool basin, featuring a raised hardwood planking terrace platform, a central circular stacked-stone fire pit, six built-in timber planter boxes filled with lush bamboo, matching hardwood-clad entrance steps, two cushioned outdoor timber benches, and warm bistro string lights along the weathered yellow-brown rear brick wall. AT THIS STAGE: The hardwood planking terrace platform is fully laid and clean across the pool basin floor, creating a level timber platform. Along the right perimeter wall, three rectangular timber planter boxes stand in position, filled halfway with dark potting soil. Two workers in tool belts stand on the platform: one worker uses a cordless drill to fasten the final perimeter trim board, while the second worker places an unlit bistro string light cable along the base of the rear brick wall. The three raw concrete entrance steps remain exposed at the shallow end, ready for finishing. On the left wall, the old chrome ladder bracket remains bolted in place. Stacks of stone blocks for the fire pit ring sit staged on a hand cart near the steps.

SITE / BACKGROUND: MAIN STATION. An enclosed private courtyard featuring a sunken rectangular concrete pool basin measuring 7 metres long by 4 metres wide and 1.5 metres deep. At the shallow end, three wide weathered cast-concrete steps lead down into the basin from a paved garden apron. The perimeter pool walls are cast concrete with visible shrinkage cracks and light mineral efflorescence. Directly behind the pool basin, a permanent yellow-brown kiln-fired brick boundary wall with weathered mortar joints and a small 10-centimetre rusted cast-iron overflow pipe in the right corner stands under the open sky. The rear brick wall, the shallow-end entrance steps, and the concrete perimeter coping remain permanent physical anchors across all stages.

SITE TEXTURE: Aged concrete floor with shrinkage cracks and mineral efflorescence patches, damp grey slurry and dried mud tracks from rubber work boots, weathered yellow-brown brick wall with dark soot stains and rust streaks beneath the overflow pipe, crushed pea gravel spill along the basin footing, wooden timber offcuts and tool pallets on the perimeter apron, and fallen autumn leaf debris along wall corners.

PHYSICS: The completed hardwood planking platform bears static loads across the underlying timber subframe joists. The three timber planter boxes sit firmly along the right wall edge. The staged masonry stones rest securely on the wooden bed of the hand cart. The workers stand planted on the secure hardwood surface.

COMPOSITION: Eye-level perspective looking down into the sunken pool courtyard at a 15-degree downward angle. The three concrete entrance steps span 216 pixels of frame width — one fifth — and keep that width throughout. The pool basin floor anchors the lower two thirds of the vertical 9:16 frame, the shallow steps occupy the mid-ground, and the rear weathered brick wall with the open sky spans the upper third.

LIGHTING: Golden hour sunset light, azimuth 255 degrees, elevation 12 degrees. Low golden light washes across the yellow-brown brick wall, glowing on the warm hardwood planking and highlighting the textured stone fire pit materials.

Camera: fixed static position, 1.2 metres above the pool terrace rim, 8.5 metres from the pool shallow end wall, bearing 0 degrees, tilt 15 degrees down, roll 0 degrees.

TIME RATE: time-lapsed at the same rate across the entire frame: clouds, shadows, and workers move accelerated as two hours pass in eight seconds.

ACTIVITY: A crew of two masons lifts a textured stone block from a hand cart and beds the masonry stones into the circular fire pit ring, while fastening timber cladding to the steps. Two workers move with soft motion streaks, backs turned to the camera with no readable facial features.

NEGATIVE: No readable text, letters, digits, logos, labels, serial numbers, numbers, or brand markings anywhere in the frame, on any surface, clothing, container, tool, or equipment. The camera never pans, tilts, zooms, shakes, or changes position. The rear brick wall, shallow steps, and pool perimeter never change shape, position, size, or profile. No architectural visualisation look, no 3D rendering style, no digital plastic sheen. No cuts, no dissolves, no camera transitions.
```

### I2V PROMPT (S5)

```
The scene begins exactly as the provided image.
Camera: fixed static position, zero movement, never moves at any point. The camera does not move at any point.
The framing remains identical in the first frame and in the last frame. The three concrete entrance steps occupy exactly the same width of the frame in the first and last frame.
The sky shows soft autumn clouds that drift steadily from east to west across the courtyard.

From the first frame to about one second, two workers use socket wrenches to unbolt the old chrome ladder bracket from the left wall.
MOTION FOCUS: From the first frame to about three seconds, two workers unbolt the old chrome ladder bracket from the left wall and carry it up the steps out of the frame; then from three seconds to the final seconds, the workers carry stone blocks and timber risers from the top steps onto the platform, building the circular stone fire pit ring and cladding the entrance steps.

A crew of two workers continuously delivers stone blocks from the delivery stack down the steps to the fire pit ring. Time-lapsed at the same rate across the entire frame: cloud shadows sweep across the brick wall, and workers move in rapid continuous purposeful motion as two hours pass in eight seconds. Soft motion streaks appear on the moving workers whose backs remain turned to the camera with no readable facial features. By the final seconds, the chrome bracket is gone, the steps are fully clad in hardwood cladding, and the center stone fire pit ring stands completed.

The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame.
```

---

## 🎬 SAHNE 6 — BİTKİLER, MOBİLYA, IŞIK VE İNSANLAR

### GÖRSEL PROMPT (G6)

```
Scene 6 of 7 — G6 Keyframe
Planting bamboo, staging patio furniture, and preparing for the evening debut.

STRUCTURE: When completed, this structure is a modern sunken garden courtyard created within an abandoned 7-metre by 4-metre rectangular sunken concrete pool basin, featuring a raised hardwood planking terrace platform, a central circular stacked-stone fire pit, six built-in timber planter boxes filled with lush bamboo, matching hardwood-clad entrance steps, two cushioned outdoor timber benches, and warm bistro string lights along the weathered yellow-brown rear brick wall. AT THIS STAGE: The sunken courtyard structure is fully built, with hardwood planking, hardwood-clad entrance steps, six timber planter boxes, and the circular stacked-stone fire pit ring complete. The site has been swept clean of all construction debris and tools. In the late golden afternoon light, the courtyard is being dressed and planted: lush tall bamboo stalks (Phyllostachys aurea) and fountain grasses stand planted in the six timber planter boxes, providing a vibrant green natural perimeter. Two contemporary low-profile outdoor timber benches with dark charcoal weatherproof cushions are placed flanking the central stone fire pit. The string of warm bistro lights is neatly suspended in graceful scallops along the rear brick wall, currently switched off. The courtyard is immaculate, prepared for its functional debut.

SITE / BACKGROUND: MAIN STATION. An enclosed private courtyard featuring a sunken rectangular concrete pool basin measuring 7 metres long by 4 metres wide and 1.5 metres deep. At the shallow end, three wide weathered cast-concrete steps lead down into the basin from a paved garden apron. The perimeter pool walls are cast concrete with visible shrinkage cracks and light mineral efflorescence. Directly behind the pool basin, a permanent yellow-brown kiln-fired brick boundary wall with weathered mortar joints and a small 10-centimetre rusted cast-iron overflow pipe in the right corner stands under the open sky. The rear brick wall, the shallow-end entrance steps, and the concrete perimeter coping remain permanent physical anchors across all stages.

SITE TEXTURE: Aged concrete floor with shrinkage cracks and mineral efflorescence patches, damp grey slurry and dried mud tracks from rubber work boots, weathered yellow-brown brick wall with dark soot stains and rust streaks beneath the overflow pipe, crushed pea gravel spill along the basin footing, wooden timber offcuts and tool pallets on the perimeter apron, and fallen autumn leaf debris along wall corners.

PHYSICS: The two outdoor timber benches rest securely bearing their static weight upon the level hardwood planking platform. The six planted timber boxes sit firmly along the perimeter walls, supported by the subframe. The dry-stone fire pit ring rests planted firmly in the center. The bamboo root balls sit embedded inside the potting soil beds.

COMPOSITION: Eye-level perspective looking down into the sunken pool courtyard at a 15-degree downward angle. The three concrete entrance steps span 216 pixels of frame width — one fifth — and keep that width throughout. The pool basin floor anchors the lower two thirds of the vertical 9:16 frame, the shallow steps occupy the mid-ground, and the rear weathered brick wall with the open sky spans the upper third.

LIGHTING: Sunset dusk twilight, azimuth 268 degrees, elevation 4 degrees. Soft warm amber sky overhead, with warm ambient reflections filling the sunken courtyard before twilight arrives.

Camera: fixed static position, 1.2 metres above the pool terrace rim, 8.5 metres from the pool shallow end wall, bearing 0 degrees, tilt 15 degrees down, roll 0 degrees.

TIME RATE: time-lapsed at the same rate across the entire frame: clouds, shadows, and workers move accelerated as two hours pass in eight seconds.

ACTIVITY: A crew of two landscapers places two cushioned benches beside the fire pit from a hand cart and seats the potted bamboo into the planter boxes, sweeping the hardwood planks clean of soil dust. Two workers move with soft motion streaks, backs turned to the camera with no readable facial features.

NEGATIVE: No readable text, letters, digits, logos, labels, serial numbers, numbers, or brand markings anywhere in the frame, on any surface, clothing, container, tool, or equipment. The camera never pans, tilts, zooms, shakes, or changes position. The rear brick wall, shallow steps, and pool perimeter never change shape, position, size, or profile. No architectural visualisation look, no 3D rendering style, no digital plastic sheen. No cuts, no dissolves, no camera transitions.
```

### I2V PROMPT (S6)

```
The scene begins exactly as the provided image.
Camera: fixed static position, zero movement, never moves at any point. The camera does not move at any point.
The framing remains identical in the first frame and in the last frame. The three concrete entrance steps occupy exactly the same width of the frame in the first and last frame.
The sky holds a deep blue twilight while soft clouds drift across the courtyard.

From the first frame to about two seconds, two workers carry bamboo plants from the steps into the planter boxes and position two cushioned timber benches before walking up the steps.
MOTION FOCUS: From the first frame to about two seconds, two workers carry bamboo plants from the steps into the planter boxes and position two cushioned timber benches before walking up the steps; then two guests walk down the steps and sit by the fire pit as the string lights switch on and the fire pit ignites with golden flames.

Time-lapsed at the same rate across the entire frame: twilight deepens smoothly, shadows dissolve, and the fire pit ignites as ten minutes pass in eight seconds. Two guests walk down the steps and take their seats on the cushioned benches. At the two-second mark, the warm white bistro string lights switch on in a single step across the rear brick wall, and a bright golden-orange flame ignites in the center stone fire pit.

From about four seconds to the eighth second, the string lights stay on, the fire pit flames hold steady, the two figures remain seated quietly in conversation, and nothing else changes.

The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame.
```

---

## 🌟 USTA KARE (G7)

### GÖRSEL PROMPT ⭐ USTA KARE (G7)

```
Scene 7 of 7 — G7 Master Keyframe
The fully completed luxury sunken garden courtyard alive with warm fire and lights at deep blue hour.

STRUCTURE: When completed, this structure is a modern sunken garden courtyard created within an abandoned 7-metre by 4-metre rectangular sunken concrete pool basin, featuring a raised hardwood planking terrace platform, a central circular stacked-stone fire pit, six built-in timber planter boxes filled with lush bamboo, matching hardwood-clad entrance steps, two cushioned outdoor timber benches, and warm bistro string lights along the weathered yellow-brown rear brick wall. AT THIS STAGE: The completed sunken garden courtyard stands fully activated in deep blue hour twilight. Warm amber and soft white bistro string lights glow brilliantly along the weathered yellow-brown rear brick wall, casting luminous reflections across the rich hardwood planking terrace floor. In the center, the circular stacked dry-stone fire pit burns with steady, vibrant golden-orange flames, casting a warm radial glow over the stone ring and surrounding timber platform. Lush, healthy green bamboo stalks and fountain grasses fill all six perimeter timber planter boxes, rustling gently in the cool evening air. Two relaxed people in warm casual evening attire sit comfortably on the cushioned outdoor timber benches, enjoying the warmth of the fire. The hardwood-clad entrance steps lead gracefully up to the garden apron. The entire sunken courtyard radiates welcoming warmth, intimacy, and sophisticated craftsmanship.

SITE / BACKGROUND: MAIN STATION. An enclosed private courtyard featuring a sunken rectangular concrete pool basin measuring 7 metres long by 4 metres wide and 1.5 metres deep. At the shallow end, three wide weathered cast-concrete steps lead down into the basin from a paved garden apron. The perimeter pool walls are cast concrete with visible shrinkage cracks and light mineral efflorescence. Directly behind the pool basin, a permanent yellow-brown kiln-fired brick boundary wall with weathered mortar joints and a small 10-centimetre rusted cast-iron overflow pipe in the right corner stands under the open sky. The rear brick wall, the shallow-end entrance steps, and the concrete perimeter coping remain permanent physical anchors across all stages.

SITE TEXTURE: Aged concrete floor with shrinkage cracks and mineral efflorescence patches, damp grey slurry and dried mud tracks from rubber work boots, weathered yellow-brown brick wall with dark soot stains and rust streaks beneath the overflow pipe, crushed pea gravel spill along the basin footing, wooden timber offcuts and tool pallets on the perimeter apron, and fallen autumn leaf debris along wall corners.

PHYSICS: The stone fire pit ring bears heavy static dead load firmly upon the hardwood planking and underlying timber joists. The two outdoor benches rest securely on the level timber boards. The two relaxed figures sit seated with weight bearing onto cushions and bench frames. The perimeter brick wall supports the anchored string light fixtures.

COMPOSITION: Eye-level perspective looking down into the sunken pool courtyard at a 15-degree downward angle. The three concrete entrance steps span 216 pixels of frame width — one fifth — and keep that width throughout. The pool basin floor anchors the lower two thirds of the vertical 9:16 frame, the shallow steps occupy the mid-ground, and the rear weathered brick wall with the open sky spans the upper third.

LIGHTING: Blue hour twilight, azimuth 285 degrees, elevation 0 degrees. Deep cobalt blue twilight sky overhead. The primary illumination comes from the glowing warm white bistro string lights, the vibrant dancing golden-orange fire pit flames, and subtle architectural wall grazing, casting rich warm highlights across the hardwood grain and brick texture.

Camera: fixed static position, 1.2 metres above the pool terrace rim, 8.5 metres from the pool shallow end wall, bearing 0 degrees, tilt 15 degrees down, roll 0 degrees.

TIME RATE: time-lapsed at the same rate across the entire frame: twilight sky, glowing string lights, and flickering fire pit flames move accelerated as ten minutes pass in eight seconds.

ACTIVITY: Two people sit seated on the cushioned benches conversing quietly by the fire pit while a third person walks down the hardwood steps carrying a tray, moving with soft motion streaks, backs turned to the camera with no readable facial features. The fire pit flames dance continuously.

NEGATIVE: No readable text, letters, digits, logos, labels, serial numbers, numbers, or brand markings anywhere in the frame, on any surface, clothing, container, tool, or equipment. The camera never pans, tilts, zooms, shakes, or changes position. The rear brick wall, shallow steps, and pool perimeter never change shape, position, size, or profile. No architectural visualisation look, no 3D rendering style, no digital plastic sheen. No cuts, no dissolves, no camera transitions.
```

---

# 🎥 G7 CANLI FİNAL / AMBIENT VİDEO PROMPTU (FİNAL TUTUŞ / CANLI KART)

> **Kullanım Amacı:** 
> Depo standardında dikey timelapse 7 sahnelik zincirde **S6 (G6 → G7)** ile tamamlanır; G7 bu zincirin hedef usta karesidir.
> Bu ek video promptu, tamamlanan bahçeyi (G7) YouTube Shorts / Instagram Reels son ekranında 5–8 saniyelik yaşayan final tutuşu (ambient hold / living card loop) olarak sunmak için hazırlanmıştır. Tek görsel referans olarak onaylı **G7 Usta Karesi** kullanılır.

### G7 CANLI VİDEO (FİNAL TUTUŞ DÖNGÜSÜ)

```
Input Image: Approved G7 Master Keyframe.

The video begins exactly as the provided image (G7).
Camera: fixed static position, locked-off tripod, zero movement, never moves at any point. The camera does not move at any point. No pan, no tilt, no zoom, no camera drift.
The framing remains 100% identical throughout the entire 8 seconds. The three hardwood-clad entrance steps maintain precisely 216 pixels of frame width from the first frame to the last frame.
The sky holds a deep cobalt blue hour twilight while delicate, faint evening wisps drift imperceptibly over the yellow-brown rear brick boundary wall.

From the first frame to the final frame, the completed sunken courtyard lives in serene evening warmth and intimate ambient motion.

MOTION FOCUS:
In the center, the circular stacked dry-stone fire pit burns continuously with vibrant, dancing golden-orange flames, casting rhythmic warm light flickers across the stone coping and hardwood terrace floor. Warm white bistro string lights along the rear brick wall glow steadily, creating luminous golden halos against the textured masonry. In the six perimeter timber planter boxes, tall green bamboo stalks rustle with subtle organic micro-sways in the gentle evening breeze.

Two relaxed adult guests in casual autumn evening attire sit comfortably on the cushioned timber benches flanking the fire pit, conversing with natural micro-movements, warm gestures, and calm postures. In the background, a third person in dark work-casual clothing walks down the hardwood entrance steps carrying a wooden tray with two cups, stepping smoothly onto the terrace platform to join the group.

TIME RATE:
Time-lapsed at a subtle ambient rate across the entire frame: twilight deepens very slightly, flame ripples flicker continuously, and the intimate courtyard atmosphere breathes with photorealistic life across 8 seconds.

HOLD & LOOP:
From the 4th second through the 8th second, the lighting levels remain steady, the fire pit flames maintain their bright golden glow, the seated figures remain relaxed in conversation, and the serene architectural balance holds completely steady, perfectly suited for an infinite ambient loop or final card hold.

NEGATIVE:
No camera movement, no panning, no tilting, no zoom, no handheld shake. The rear brick wall, entrance steps, pool basin perimeter, planter boxes, and terrace platform never shift, morph, warp, or change position. No readable text, letters, numbers, watermarks, or logos anywhere on any surface or clothing. No CGI plastic sheen, no 3D rendering look, no flickering artifacts. No cuts, no dissolves, no camera transitions.
```


