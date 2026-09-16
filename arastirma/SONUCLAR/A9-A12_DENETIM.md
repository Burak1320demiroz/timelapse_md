# 🔍 A9–A12 DENETİMİ — üçüncü kuşak dört raporun doğruluk teyidi

> Kart S §2 (etiket) · §2b (kaynak sınıfı) · §3 (çelişki) · §4 (iki rapor) uygulanmıştır.
> Ham dosyalar: `A9_GEMINI_HAM.md` · `A10_…` · `A11_…` · `A12_…` (11.09.2026)
>
> ⛔ Bu dosya raporları DEĞİŞTİRMEZ. Ham çıktı kanıttır ve dokunulmamıştır.
> ⭐ "ÖLÇTÜM" satırları bu depoda, bu makinede hesaplanmıştır (python3 · 11.09.2026).
>    "KAYNAK DOĞRULANDI" satırları için kaynağın kendisi çekilip başlığı ve özeti
>    raporun iddiasıyla karşılaştırılmıştır. Rapordan gelen hiçbir sayı, biri
>    yapılmadan ölçülmüş sayılmaz.

---

## 0. DÖRDÜNÜN ORTAK DURUMU — bu kuşakta ne değişti

```
O1  TEK BOT, ÜÇÜNCÜ KEZ. Dördü de aynı bota koşuldu (künye: Gemini DR, tahmin).
    Kart S §4'ün çelişki görünürlüğü yine YOK.

O2  ⭐ ÇÖZÜMLENEBİLİR KAYNAK BU KEZ VAR — ve bu, A5–A8'e göre gerçek bir
    ilerleme. v2 promptları "URL / DOI / belge adı + bölüm" şart koştu; A11
    on beş DOI, A9 standart adı + bölüm, A10 standart adı verdi.
    ⛔ AMA KAYNAKLARIN BİR KISMI YANLIŞ ATIF. 12 kaynağı çektim:
       7 tutuyor · 4 başka makaleye çıkıyor · 1 erişilemedi (403).
       Yeni arıza sınıfı: A1'de kaynak ZAYIFTI, burada kaynak VAR ama İDDİAYA
       AİT DEĞİL. Etiket yine kaynağı ölçer; doğrulanmamış DOI, DOI değildir.

O3  ⛔ "Python Script Snippet" KAYNAK DEĞİLDİR. A12 kendi hesabını kaynak
    olarak yazıp ÖLÇÜLDÜ etiketledi. Hesap bu depoda yeniden yapıldı (§4);
    tutan satırlar "HESAP DOĞRULANDI", tutmayanlar "DÜŞTÜ" aldı.

O4  ⛔ İKİ RAPOR KENDİ TABLOSUYLA ÇELİŞTİ. A11'in örnek cümleleri kendi
    piksel tablosuyla tutmuyor (§3.3); A12'nin gölge satırı bu deponun
    ölçümüyle çelişiyor (§4.2).

O5  ✅ A9 BİLMEDİĞİNE "BİLİNMİYOR" YAZDI — 13 malzemenin 8'inde, 12 kirlilik
    katmanının 8'inde kaynak sütunu boş. Kart S'nin istediği dürüstlük bu;
    o satırlar VARSAYIM olarak kodlandı, ÖLÇÜLDÜ olarak değil.
```

---

## 1. KAYNAK DOĞRULAMA — 12 çekim

| Raporun atfı | Çekilen kaynak | Sonuç |
|---|---|---|
| A11 · T2I-CompBench++ · arXiv 2307.06350 | T2I-CompBench++ (8.000 kompozisyon promptu) | ✅ TUTUYOR — "size anchoring" alt iddiası özette yok → o kısım İDDİA |
| A11 · GenScale · arXiv 2609.00525 | GenScale: A Benchmark for Relative Object Scale (1.643 ölçek ilişkisi) | ✅ TUTUYOR |
| A11 · NumBench · arXiv 2608.28206 | NumBench: Diagnosing Counting Failures in T2I (640.000 prompt · 1–100) | ✅ TUTUYOR |
| A11 · hata birikimi · arXiv 2607.27110 | FreqForcing: AR uzun video, "color drift, motion stagnation, visual collapse" | ✅ TUTUYOR |
| A11 · attention sink · arXiv 2509.25161 | Rolling Forcing: ilk karelerin KV durumu küresel çapa | ✅ TUTUYOR |
| A11 · FlexEControl · arXiv 2405.04834 | FlexEControl (Uni-ControlNet'e göre %41 az parametre) | ✅ TUTUYOR — ⛔ aynı DOI MLSD için de verilmiş; MLSD bu makale değil |
| A11 · SpatialGenEval · arXiv 2601.20354 | Everything in Its Place (1.230 prompt · **21** model) | ⚠️ KISMEN — rapor 23 model dedi; "%90 sağ/sol karıştırıyor" özette yok → İDDİA |
| A11 · Depth Anything V2 · arXiv 2510.04723 | Vahşi yaşam kamera-tuzağı benchmark'ı; MAE 0,454 m | ⚠️ KISMEN — sayı doğru, bağlam şantiye değil orman |
| A11 · VINs / MAWE · arXiv 2503.17539 | Video Interface Networks; optik akış anılıyor, MAWE < 2,0 özette yok | ⚠️ KISMEN → İDDİA |
| A11 · CameraCtrl · arXiv 2601.16214 | **CamPilot** (3D Gaussian ödül) — CameraCtrl/Plücker değil | ❌ YANLIŞ ATIF (iddia A3-d ile aynı yönde; kaynak başka) |
| A11 · layout bias · arXiv 2505.13219 | **PiT: Progressive Diffusion Transformer** — kompozisyon önyargısıyla ilgisiz | ❌ YANLIŞ ATIF → "1/3 kuralı ufku iter" VARSAYIM |
| A11 · pinhole ufuk · arXiv 2211.12432 | Multi-task Learning for Camera Calibration — ufuk/pitch ilişkisi yok | ❌ YANLIŞ ATIF (geometri formülden zaten çıkıyor, KAMERA §3) |
| A11 · IP-Adapter · arXiv 2412.02912 | **ShapeWords** — IP-Adapter değil | ❌ YANLIŞ ATIF (iddia A3-c ile aynı; kaynak başka) |
| A11 · kule vinç 3D · DOI 10.3390/s23104851 | MDPI 403 verdi | ⛔ ERİŞİLEMEDİ |
| A9 · ACI 308R-16 · ASTM C309 · ISO 8501-1 · ISO 9223 · PERI · Mastcam-Z | Standart ve belge adları gerçek; bölüm numaraları çekilmedi | ⚠️ AD DOĞRU, SAYI DOĞRULANMADI |
| A10 · BS 5975 · EN 12812 · EN 12811 · EN 1090-2 · PAS 8812 · EC7 | Standart adları gerçek; satır içerikleri çekilmedi | ⚠️ AD DOĞRU, SAYI DOĞRULANMADI |
| A10 · PhysBench · VideoPhy · PhyParam-Bench · Morpheus · FC-VFI | Yalnız ad, DOI yok | ⛔ İDDİA — etkinlik dereceleri ("çok etkili / zayıf") kaynaksız |

```
KURAL (bu kuşaktan): bir DOI'nin yanında ÖLÇÜLDÜ yazması için DOI'nin
ÇEKİLMİŞ ve iddiaya AİT olması gerekir. Kılavuza yalnız ✅ satırlar
"kaynaklı" iner; ⚠️ ve ❌ satırlar VARSAYIM/İDDİA olarak DERSLER'e girer.
```

---

## 2. ÖLÇTÜM — kadraj ve piksel aritmetiği

```
f = 24 mm · tam kare 36 mm dikey · D = 40 m · 9:16
  dikey FOV   73,74°     yatay FOV (9:16 kırpımı)  45,75°
  kadraj      33,75 × 60,00 m    → 32,00 px/m   → 1 px = 3,125 cm
✅ A9 · A10 · A11 · A12 dördünün kadraj sayıları TUTUYOR (A5-c ile aynı).

Makine piksel tablosu (A10 Tablo 2) — 15 satırın 15'i yeniden hesaplandı, TUTUYOR:
  CAT 320 palet 0,79 m → 25 px · iz 3,65 m → 117 px · LTM kriko 7,2 m → 230 px ·
  kule temel 5 m → 160 px · IPEx palet 0,20 m → 6 px · manipülatör ayağı 0,5 m → 16 px
  ⚠️ Makine ölçüleri (0,79 · 3,30 · 7,2 …) ekipman belgesinden; belge çekilmedi.

Kirlilik piksel tablosu (A9 Section 2) — 12 satırın 12'si TUTUYOR:
  çamur yolu 1,5–3,0 m → 48–96 px · pas akıntısı 0,2 m → 6 px · yağ damlası 0,05–0,15 m → 2–5 px
  ⭐ ÖLÇTÜM'ün asıl bulgusu: 0,5 m eşiği NESNE içindir; kesintisiz BANT eşiği aşar.
     0,2 m genişlikte bir pas akıntısı 6 px'tir ama 1–3 m uzunlukta bir ÇİZGİ
     olarak okunur. SITE TEXTURE bant ve alan yazar, nesne saymaz.

Referans nesne tablosu (A11 §1.1) — 7 satırın 7'si TUTUYOR (1,5 m → 48 px … 15 m → 480 px).
Sarkaç (A10): √6 = 2,449 ✅.   Kar (A12): 3–5 cm/sa × 9 sa = 27–45 cm ✅ · 5 cm = 1,6 px ✅.
Yürüyen işçi (A12): 33,75 / 1,5 = 22,5 s → 100×'te 0,225 s ≈ 5 kare ✅.
Kamyon 10 m/s: 3,4 s → 100×'te 0,034 s ≈ 1 kare ✅.
Yıldız izi 2 saat: 15,04°/sa × 2 = 30,1° ✅ (sidereal — bu satır DOĞRU).
```

---

## 3. RAPORLARIN KENDİ İÇİNDEKİ ÇELİŞKİLER

### 3.1 A12 — gölge dönüşü ⛔ DÜŞTÜ (deponun ölçümüyle çelişiyor)
```
Rapor: "Saat açısı gereği Dünya dönüşü saatte 15° · 2 saatte tam 30,0° ·
        9 saatte 135,0°"  [ÖLÇÜLDÜ etiketli]
A6-b ÖLÇTÜM (08.09.2026): 15°/saat SAAT AÇISIDIR, gölgenin azimutu değil.
        40°N · 9 saatte azimut: ekinoks 150,2° · yaz 190,7° · kış 115,9°;
        öğle civarı hız ekinoks 23,1°/sa · yaz 46,3°/sa · kış 15,3°/sa.
⇒ A12'nin gölge satırı ve 2 numaralı örnek cümlesindeki "a full thirty
   degrees" DÜŞTÜ. Kılavuz SANTIYE_HAREKETI §1 tablosunu kullanır.
⭐ Aynı hata iki kuşakta iki bottan geldi (A6 · A12) — "15°/saat" bu
   konunun standart yanlış cevabıdır; kapıda değil kılavuzda uyarı olarak durur.
```

### 3.2 A12 — bulut geometrisi basitleştirilmiş (mertebe, sayı değil)
```
Rapor "1500 m irtifada kadraj genişliği 1265 m" diyor: irtifayı yatay
mesafe saymış (0,8437 × 1500). Tilt 0° kamerada bulut ufkun 0–37° üstünde
görünür; 20° yükseklikteki 1500 m'lik bulut 4,1 km uzaktadır ve o mesafede
kadraj 3,5 km'dir. ⇒ "kadraj geçişi %474" gibi yüzdeler 2–5 kat şişkin.
✅ NİTEL SONUÇ AYAKTA: 100×'te şerit · 1200×'te akış · 5400×'te silinme.
   Kılavuza yüzde DEĞİL, üç rejim × üç görünüm iner.
```

### 3.3 A11 — örnek cümleler kendi tablosuyla tutmuyor ⛔
```
Tablo: pencere sövesi 1,5 m → 48 px   → kadraj genişliğinin 1/22,5'i
Cümle: "spans one tenth of the total frame width"        → 108 px = 3,4 m
Tablo: meşe gövdesi 1,0 m → 32 px    → 1/33,7   Cümle: "one twentieth" → 54 px
Tablo: fener kaidesi 5,0 m → 160 px  → 1/6,7    Cümle: "one eighth"    → 135 px
⇒ Kesir cümlesi tablodan değil, USTA KAREDE ÖLÇÜLEN pikselden yazılır.
   Kılavuz kuralı: kesir = ölçülen px / 1080; yuvarlama en yakın "one nth".
```

### 3.4 A10 — "6 sn yerine 2 sn × 3 klip" önerisi formatla çelişiyor ⛔ ALINMADI
```
Format: klip = iki onaylı kare arasında tek video, sahne içinde kesme yok
[KILAVUZ_REHBERI §2.7]. Üç klip zincirlemek iki iç dikiş açar; ⑥ sayar.
⭐ Geriye kalan ölçülebilir soru araç kapısına gider: aynı iki kare için
   4 sn ve 8 sn klipte ⑫ KATILIK skoru farklı mı? [ARAC_KARTLARI §4'e aday]
```

### 3.5 A12 — "yeniden bağlama" cümlesi imzayı bozuyor ⛔ ALINMADI
```
Rapor: "All vehicles, moving workers, and machines are reduced to invisible,
ghostly transparent motion blur streaks …; the rigid ground is static, while
clouds race overhead."
⛔ "the rigid ground is static" makineyi de durdurur; "workers" insansız
   sahada özne üretir [DERS 33]; kapı imzası "time-lapsed at the same rate"
   [DERS 15] korunur. Cümle alınmadı; bulut cümleleri ayrı iner (§5).
```

---

## 4. DEPONUN ÖLÇÜMLERİYLE KARŞILAŞTIRMA — "ÇELİŞENLER" bölümleri

```
A9  "hard-mounted engineering camera" külliyat değil     → DERS 34 (ölçülmüştü) ✅ doğrular
A9  malzeme ADI korpus çağırır (regolith bags → sandbag)  → DERS 42 ✅ doğrular
A9  evrensel SITE TEXTURE havasız sahada fizik dışı       → YENİ · kapı olur (A9-g)
A9  0,5 m altı detay kayıp                                → A5-c ÖLÇTÜM ✅ doğrular
A9  beton homojen değil, döküm sınırı görünür             → A4-a ✅ doğrular, sayı ekler (VARSAYIM)
A10 "Everything rests on the ground" asılı yükü yalanlar  → YENİ · PHYSICS kuralı (A10-i)
A10 A karesinde hammadde + söküm başlangıcı zorunlu       → DERS 48 + P2-a + P2-h ✅ doğrular
A10 excavator/dozer robotik sahada oksimoron              → DERS 41 ✅ doğrular, sözlük ekler
A11 tilt 0° → ufuk %50; %58 imkânsız                      → KAMERA §3 ✅ (formül); ⚠️ planlar
                                                            ±2° tilt beyan edebilir, o zaman
                                                            ufuk formülden hesaplanır
A11 sayı prompta yazılmakla kamera kilitlenmez            → DERS 23 + A3-d ✅ doğrular
A12 gök–yer ayrı saat üç kez ölçüldü                       → DERS 15 · 47 · 50 ✅ mekanizma ekler
A12 100× rejimde kar yağıp eriyemez                        → DERS 7 ✅ fizikle doğrular
A12 gölge 15°/saat                                         → A6-b ⛔ DÜŞTÜ (§3.1)
```

---

## 5. KILAVUZA NE İNDİ, NE İNMEDİ

```
İNDİ (kod · etiket · kılavuz)
  A9-a…g   → MALZEME_VE_DOKU_KILAVUZU    (korpus üçlüsü · bant kuralı · yaşlanma × üç yay)
  A10-a…i  → FIZIK_VE_AGIRLIK_KILAVUZU   (yük yolu · söküm fiili · istif · robotik sözlük · ihlal sözlüğü)
  A11-a…l  → PERSPEKTIF_VE_OLCEK_KILAVUZU (referans defteri · kesir kuralı · sayı testi · kanal)
  A12-a…j  → HAVA_VE_ATMOSFER_KILAVUZU   (üç rejim × gök · yer tablosu · alternatif taşıyıcı · iki kare)
İNMEDİ
  A10 "2 sn × 3 klip"            → araç kapısına ölçüm sorusu
  A12 gölge 15°/saat              → düştü; SANTIYE_HAREKETI §1 geçerli
  A12 "ground is static" cümlesi  → imzayı bozar
  A11 ❌ atıflı dört madde        → VARSAYIM olarak DERSLER'de, kılavuzda "kaynaksız" işaretli
  A9/A10 standart bölüm numaraları → belge çekilmedi; sayılar VARSAYIM
```
