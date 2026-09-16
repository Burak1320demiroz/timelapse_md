# 🌤️ HAVA VE ATMOSFER KILAVUZU — göğü yerle aynı saate bağlamak

> **Tek soru:** Gök ile yer aynı saatte mi akıyor, ve gök o hızda NASIL görünür?
> **Sahibi olduğu bloklar:** `TIME RATE` (gök cümlesi) + `LIGHTING` (gök, pus,
> hava) — ZAMAN_VE_ISIK güneşi tarif ediyordu, gökyüzünü iki satırda geçiyordu.
>
> ⛔ **Kaynak:** `arastirma/SONUCLAR/A12_GEMINI_HAM.md` · denetim `A9-A12_DENETIM.md`
> · dersler `DERSLER.md` A12-a…j · DERS 7 · 14 · 15 · 18 · 21 · 26 · 40 · 47 · 50
> · A4-c · A6-b (ÖLÇTÜM). **ÖLÇTÜM** = burada hesaplandı; diğerleri VARSAYIM/İDDİA.
>
> **Sınır:** ZAMAN_VE_ISIK = güneş ve mevsim (SAAT). SANTIYE_HAREKETI §1–2 = rejim
> (HIZ; gölge dönüş tablosu ORADADIR, burada tekrarlanmaz). Burası = göğün ve
> havanın o hızdaki GÖRÜNÜMÜ ve iki kare arasındaki tutarlılığı.

---

# 0. NEDEN BU KILAVUZ VAR — üç filmde üç kez ölçülen aynı arıza

```
③ TIME RATE 0/10 · CLOUD AND SKY düşüşleri
  "clouds race across the sky in heavy time-lapse, while the workers on the
   deck below move at near real-time speeds"                    [DERS 15]
  makineler motion blur ile akarken gölge klip boyunca oynamadı   [DERS 47]
  yıldızlar akarken araçlar ve toz cam gibi net kaldı            [DERS 50]
  beş klipte bulut hiç hareket etmedi · iki sahnede mevsim "indeterminate"
  kar tek klipte yağıp eridi                                      [DERS 7]

⭐ Raporun teşhisi (A12 — mekanizma, İDDİA): model gökyüzünü akışkan doku
   olarak sınırsız hızlandırır, makineyi ve insanı eğitim setindeki gerçek
   hızda tutar (anlamsal ayrışma). Prompt "timelapse" derken iki saat
   çalışır. Çözüm: gök ve yer AYNI cümlede, AYNI rejimde, iki karede de
   TUTARLI yazılır — ve göğün o rejimdeki görünümü ADIYLA verilir.
```

---

# 1. ÜÇ REJİM × GÖK — bulutun o hızdaki görünümü  [A12-a ÖLÇTÜM yol · görünüm VARSAYIM]

> Rejim tanımı ve gölge dönüşü SANTIYE_HAREKETI §1'dedir. Burada yalnız GÖK.
> ⛔ Raporun "kadraj geçişi %" yüzdeleri irtifayı yatay mesafe saydığı için
> 2–5 kat şişkindir; sayı DEĞİL, üç görünüm indi.

| Bulut (tipik irtifa · hız) | A · 100× (10 dk) | B · 1200× (2 saat) | C · 5400× (iş günü) |
|---|---|---|---|
| Cumulus (1,5 km · ~10 m/s) | 6 km yol · kaynayan, şekil değiştiren beyaz kümeler · yere KESKİN, gezen gölge | 72 km · formunu kaybedip yatay ŞERİTLERE uzar · gölgeler yanıp söner | 324 km · yüzlerce kez geçer, SİLİNİR: düz gri-beyaz tavan |
| Stratus (0,5 km · ~6 m/s) | kalın örtü kütle hâlinde yalar, yırtıklardan gök görünür | sürekli gri YIKANMA · yönlü gölge yok | pürüzsüz gri perde, şekil seçilmez |
| Cirrus (9 km · ~30 m/s) | ince fırça darbeleri saçaklanır · gölge yok | jilet gibi hızlı beyaz çizgiler | ufuktan ufka sabit beyaz izler |
| Cumulonimbus (1 km · ~15 m/s) | ekran hızla kararır, kütle üstte kaynar | dev kütle ekranı yutar · STROBE ışık | tamamen kararır, hücreler flaş üretir |
| Altostratus (4 km · ~18 m/s) | soluk gri doku yavaş dalgalanır · yumuşak gölge | tüm gök PULSASYON · gölge kontrastı iner çıkar | ışık TİTREMESİ · tek renk plaka |
| Sis / pus (≤100 m · ~2–3 m/s) | opak duvar lensin etrafında döner · kontrast sıfır | beyaz/gri perde | sabit beyaz ekran |

```
YER — aynı rejimde ne görünür [A12-c ÖLÇTÜM]
  kamyon (10 m/s)      A: kadrajı ~1 KAREDE geçer, saydam çizgi  · B/C: silinir; yalnız park hâli net
  ekskavatör kolu      A: gövde net, kol saydam yelpaze          · B: kol görünmez, şasi net · C: hayalet dizi
  yürüyen insan        A: ~5 kare saydam, titreşen silüet        · B/C: SİLİNİR [SANTIYE_HAREKETI §1 ile aynı]
  gölge                SANTIYE_HAREKETI §1 tablosu — ⛔ "saatte 15°" DEĞİL [A6-b ÖLÇTÜM; A12'nin
                       135°'si DÜŞTÜ]

KURAL  TIME RATE bloğu gök için o rejimin GÖRÜNÜMÜNÜ adıyla yazar:
       A → "clouds drift and boil" · B → "clouds stretch into long streaks" ·
       C → "the sky smooths into a flat moving haze". Yer cümlesi aynı rejimden
       gelir (SANTIYE_HAREKETI §2); ikisi TEK CÜMLEDE, "time-lapsed at the
       same rate" imzasıyla [DERS 15 — imza korunur].
```

---

# 2. ATMOSFERİK PERSPEKTİF — mesafe bandı × hava  [A12-d · İDDİA/VARSAYIM]

| Hava | 0–50 m | 50–200 m | 200–1000 m | Ufuk |
|---|---|---|---|---|
| Açık | keskin, yoğun siyah | siyahlar hafif kalkar | MAVİYE kayar, keskinlik düşer | mavi-gri silüet, gök tabanı açık mavi |
| Bulutlu | yumuşak gölge, doygun renk | renk solar, düz ışık | sınırlar yumuşar, mavi kayma az | gri gökle homojen birleşir |
| Sisli | kontrast yarı, kenarlarda hale | yalnız açık gri silüet | görüş yok | ufuk YOK, tam opaklık |
| Tozlu | sarı/kızıl ton, Mie saçılımı | keskinlik düşer, ışık ileri saçılır | kahverengi pus duvarı | toprak rengi perde, gök kirli sarı |
| Yağmurlu | ıslak yüzeyde AYNA yansıma | yağmur perdeleriyle kontrast dalgalanır | detay kaybolur | bulut tabanı yerle birleşir |
| Karlı | yerden dolgu ışığı, gölge açılır | kar kontrastı keser | whiteout, çok yönlü ışık | beyaz gök + beyaz yer, gölgesiz |

```
KURAL  LIGHTING bloğuna güneş satırının [ZAMAN_VE_ISIK §2] YANINA bir derinlik
       cümlesi gelir: uzak çapa (sırt · fener · kule) hangi tonda ve kontrastta.
       Derinlik cümlesi olmayan kadraj düz durur; ① SURFACE TRUTH "miniature
       appearance" bunu da sayar.
```

---

# 3. YAĞIŞ VE RÜZGÂRIN KLİP İÇİ SAATİ  [A12-f · VARSAYIM · kar ÖLÇTÜM]

```
YAĞMUR BAŞLARSA   beton 1–3 dakikada tamamen ıslanır: albedo düşer, gök yansır
                  A (100×): klibin 1. saniyesinde zemin koyulaşır · C: 1 karede POP
YAĞMUR BİTERSE    kuruma 30 dk – 4 saat (rüzgâr, nem, yüzey ısısı)
                  A: kuruma klibe yayılan yavaş solma · C: 1–2 saniyede eski renk
                  ⭐ ISLAK-KURU SINIRI zaman taşıyıcısıdır (§4)
KAR               3–5 cm/saat · 9 saatte 27–45 cm (ÖLÇTÜM) · 5 cm = 1,6 px
                  A (10 dk): yalnız ince tozlama · C (9 sa): 30–40 cm, köşeler yuvarlanır
                  ⛔ A rejiminde kar YAĞIP ERİYEMEZ [A12-j · DERS 7]; kış İKİ sahnedir
RÜZGÂR            bayrak 5 Hz salınır → B/C'de yarı saydam koni ya da silinir (Nyquist)
                  toz ve tente aynı yöne; yön klip boyunca SABİT [ZAMAN_VE_ISIK §3 ②]
```

---

# 4. GÖLGESİZ SAHNEDE ZAMAN — altı alternatif taşıyıcı  [A12-g · DERS 40'ın çıkışı]

```
Kapalı gök · gece · kutup · fırtına: güneş yoksa zamanı BAŞKA bir şey taşır.
Rejim C'nin gölgesiz klibi filmin EN UZUN klibi olamaz [DERS 40]; ama bir
klip gölgesiz kalacaksa şu altıdan EN AZ BİRİ yazılır:

  ① pus halesi          ışık kaynağının etrafındaki halenin büyüyüp şekil değiştirmesi
  ② toz duvarı          görünürlüğün klip boyunca düşmesi — uzak vinç pusta erir
  ③ ıslak-kuru sınırı   koyu lekenin kenarından küçülmesi (termodinamik saat)
  ④ projektör gölgesi   dönen/gezen yapay ışığın sert gölgesi
  ⑤ beton kürlenme      koyu griden açığa — yalnız günler mertebesinde [MALZEME §4]
  ⑥ yıldız izi          15,04°/saat → 2 saatte 30° (ÖLÇTÜM · A4-c ile aynı) — kutba yakın
                        iç içe yay, ekvatorda düz; "short trails" değil, DERECE yazılır

KURAL  Her klibin TIME RATE bloğu en az bir zaman taşıyıcısı adlandırır:
       gölge süpürmesi (varsayılan) ya da yukarıdaki altıdan biri.
```

---

# 5. HAVASIZ VE İNCE ATMOSFERLİ GÖK  [A12-e · İDDİA/VARSAYIM]

```
AY / HAVASIZ KAYAÇ   pus SIFIR · gök gündüz de siyah · yıldızlar sabit nokta
                     (izlenim: pozlama kısa) · gölge mutlak siyah, jilet keskin ·
                     ufuk YAKIN ve keskin · uzak tepe ön plan kadar kontrastlı ·
                     toz balistik, bulut yok [FIZIK §3 · INSAAT_YONTEMI §4]
MARS                 optik derinlik asılı tozdan · gök gündüz butterscotch/kızıl ·
                     gölgeler ılık dolgulu · ufukta pas rengi pus · gün batımında
                     güneşin etrafında MAVİ hale · toz fırtınası mümkün
BUZ GEZEGENİ         çoklu saçılım · whiteout · gölgesiz düz ışık · gök ile yer
                     sınırı silinir → zaman §4 ①–④ ile taşınır

⛔ Bu üçünde de "clouds streak" YAZILMAZ; Ay'da bulut fizik dışıdır, Mars'ta
   nadir ve ince (cirrus benzeri buz bulutu), buzda whiteout'tur.
⛔ Ay ve Mars için ③ merceği Mod V'de Dünya mevsimi okur (POLAR HABITAT'ta
   okudu) — planın "tek gün / bir Ay günü" MERTEBE beyanı [P1-c] burada da zorunlu.
```

---

# 6. ⭐ İKİ KARE ARASI PROJEKSİYON — G(n) ve G(n+1)'de gök  [A12-i · DERS 47]

```
Her klip iki onaylı kare arasında üretilir. Video o iki kareyi bağlar; gök ve
gölge iki karede AYNI çizilmişse model aradaki 6 saniyede ya güneşi durdurur
ya gölgeyi yerinde "morph" eder — DERS 47'nin ("gölgeler hiç oynamadı") sebebi
budur.

KURAL  G(n) ve G(n+1) görsel promptlarının LIGHTING satırı rejime göre
       FARKLI yazılır:
         gölge   B rejiminde iki kare arasında SANTIYE_HAREKETI §1 tablosunun
                 2 saatlik değeri kadar dönmüş (ekinoks ~45° · yaz ~84° · kış ~30°)
         bulut   G(n)'de solda duran cumulus, A rejiminde G(n+1)'de sağa kaymış;
                 B rejiminde KADRAJDAN ÇIKMIŞ, yerini başka bir bulut almış
         ıslak   yağmur klibi ise G(n) kuru, G(n+1) ıslak — ya da tersi; ikisi
                 aynı olamaz
       I2V'nin son cümlesi ("The shot ends exactly on the second provided image")
       bu farkı zorunlu kılar: fark yoksa zaman yoktur.
⭐ Bu, PROMPT_SABLONU §1 LIGHTING satırının iki-kare hâlidir; KARE TABLOSU
   [KILAVUZ_REHBERI §2.7] her görsel için gölge açısını ve bulut durumunu da taşır.
```

---

# 7. PROMPTA İNEN CÜMLELER — İngilizce · POZİTİF · rejim adıyla

> A12'nin beş cümlesinden; gölge dereceleri SANTIYE_HAREKETI §1'e göre düzeltildi
> ("thirty degrees" düştü), negatif kalıplar ("absolute absence", "devoid of")
> DERS 33 gereği pozitife çevrildi. Kapı imzası korunur.

```
A · 100× · CUMULUS · açık
  Everything in this frame is time-lapsed at the same rate: ten minutes pass.
  Scattered cumulus drift across the upper half of the frame from left to right,
  boiling and reshaping as they go; the crane's hard shadow creeps a few degrees
  across the slab; the sky grades from deep blue at the zenith to a pale, faintly
  hazy cyan at the horizon, and the ridge a kilometre away sits softer and bluer
  than the foreground.

B · 1200× · CIRRUS · açık
  Everything in this frame is time-lapsed at the same rate: two hours pass.
  High cirrus stretches into long horizontal streaks across the deep blue sky;
  every ground shadow sweeps steadily across the site as the sun moves; distant
  structures beyond a kilometre are washed in soft blue haze while the foreground
  stays sharp and high-contrast.

C · 5400× · STRATUS · kapalı
  Everything in this frame is time-lapsed at the same rate: a full working day
  passes. A low stratus deck flows across the frame as a seamless blurred grey
  river; the flat, diffuse daylight brightens from morning to midday and dims
  toward evening; on the ground the dark wet patches shrink to dry pale concrete
  from the edges inward.

SİS · her rejim
  A dense bank of fog rolls through and holds visibility under fifty metres; the
  far end of the site fades to a flat white field, the nearer crane stands as a
  grey silhouette, and the light is even and shadowless while its brightness
  drifts with the hour.

AY · havasız
  Everything in this frame is time-lapsed at the same rate. The sky is a hard
  black field with fixed pinpoint stars above the sunlit ground; razor-edged
  black shadows sweep across the pale regolith as the sun moves; the horizon is
  close and knife-sharp, and the far rim reads as crisp as the foreground.

MARS · ince atmosfer
  The daytime sky is a uniform dusty butterscotch; shadows carry a warm soft
  fill; a fine rust-coloured haze softens the horizon, and around the low sun a
  cool blue glow forms as it sets.
```

---

# 8. KAPI — bu kılavuz nerede zorlanır

```
prompt_kontrol.py §10d (11.09.2026):
  · I2V promptunda gök/atmosfer HAREKET cümlesi yok (cloud · sky · haze · fog ·
    star + drift · streak · sweep · roll · cross · stretch · flow · hold)    → FIX
  · (mevcut) TIME RATE imzası · rejim penceresi · güneş diski · rejim C insan

ELLE
  · KARE TABLOSU'nda G(n) ve G(n+1) için gölge açısı ve bulut durumu FARKLI mı (§6)
  · gölgesiz klipte §4'ten en az bir taşıyıcı adlandırılmış mı
  · havasız sahada bulut cümlesi YOK mu (§5)

ÖLÇÜLECEK
  · §1 görünüm sütunları — ③ CLOUD AND SKY ve TIME RATE ilk üretimde
  · §6 iki-kare projeksiyonu DERS 47'yi kapatıyor mu
  · A12-h "gerçek zamanlı üret, kurguda hızlandır" alternatifi — A3-e ile aynı,
    hiç koşulmadı
```
