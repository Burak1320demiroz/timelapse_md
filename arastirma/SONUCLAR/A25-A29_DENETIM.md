# 🔎 A25–A29 DENETİM — film yazımından doğan beş kılavuz · 07.10.2026

> Kaynak: `A25_GEMINI_HAM.md` … `A29_GEMINI_HAM.md` (beş rapor · proje sahibi tek mesajda verdi · bot
> beyan edilmedi, biçim Gemini Deep Research) · promptlar `arastirma/A25…A29_*.md` (07.10.2026 · altı
> cümle · BU DEPODA YAZILDI · tetikleyen: THE SLOW TAKEOFF yazımı).
> Yordam: `arastirma/00_README.md §3` — etiket · kaynak sınıfı · çelişki · ölçüm.

```
⭐ BU KUŞAĞIN FARKI
   ① SORULAR BİR FİLMİN YAZIMINDAN DOĞDU (THE SLOW TAKEOFF): uzun form · ikinci istasyon · su · ışık · onarım.
      Raporlar bizim verdiğimiz sayıları (8–17 m yansıma bandı · 10–13 m kano · 75×/900×) yeniden hesapladı —
      ikisi tuttu, birinde BİZİM hatamız çıktı (§3).
   ② KAYNAKÇA ÇEKİLDİ (§6): 33 atıf satırı · 20 ✅ · 8 ⚠️ · 5 ❌. Üç arXiv numarası BAŞKA makalelere ait,
      iki atfın başlığı uydurma; bir sayı (VideoPhy-2 %47,7) hiçbir kaynakta yok.
   ③ HESAPLAR BU MAKİNEDE KOŞTU (§1–§4): alacakaranlık tablosu 9/9 · yansıma tablosu 12/12 · Fresnel ·
      Brewster · kano mesafesi · kare süresi · dip → sahne eşlemesi.
   ④ A25'in YouTube iddiaları bu kuşağın en sağlamı: yedi platform kuralı resmi sayfalardan çekildi ✅.
⇒ Kılavuza inen: platform kuralları + bu makinede sınanmış ARİTMETİK + iki akademik bulgu (Loewenstein 1994 ·
  Magliano & Zacks 2011) + NegT2IBench'in yönü. Raporun kendi "ÖLÇÜLDÜ" etiketli yüzdelerinin çoğu inmedi.
```

---

# 1. A25 — UZUN FORM ANLATI · en sağlam rapor

| iddia | denetim | hüküm |
|---|---|---|
| key moments ≥ 60 sn · ≥ 100 izlenme · Intro = 30. sn | YouTube Help 9314415 ✅ | iner |
| spike = tekrar izleme/paylaşım · dip = atlama/terk | aynı sayfa ✅ | iner |
| typical = benzer uzunluktaki son 10 video | aynı sayfa ✅ ("SEE MORE" ile tüm YouTube kıyası da var) | iner |
| bölüm: ≥ 3 damga · ilki 0:00 · her biri ≥ 10 sn | YouTube Help 9884579 ✅ (rapor ikincil kaynağa atfetti) | iner |
| son ekran son 5–20 sn | YouTube Help 6388789 ✅ · video ≥ 25 sn | iner |
| A/B testi izlenme süresi payını ölçer | YouTube Help 16391400 ✅ · sonuç Winner / Performed same / Inconclusive · adı artık "A/B test titles & thumbnails" | iner |
| bilgi boşluğu kuramı | Loewenstein 1994 Psych Bull 116(1):75–98 ✅ | iner (kuram) |
| Cutting ve ark. 2012 olay algısı | JEP:HPP 38(6):1476–90 ✅ · 24 film, film başına 3 izleyici, ~%90 uyum · rapor DOI vermedi | iner (yön) |
| tutma kıyas yüzdeleri (< 5 dk %65–75 …) | Prepublish/Lenostube — üçüncü taraf, örneklem karışık | ⛔ inmez |
| "her 5–10 sn desen kesintisi" | pazarlama, örneklem yok (rapor da İDDİA dedi) | ⛔ inmez |
| YAPI ÇİZELGESİ (ilk sonuç 25 sn · doruk %85 · tutuş 20 sn) | kuramdan türetildi, etiketsiz | başlangıç değeri olarak iner (UZUN_FORM §2), kural değil |
| merak zinciri örneği (su çarkı · şömine) | filmde yok — rapor uydurdu | ⛔ |
| bölümlerin tutmaya etkisi | iki kaynak ters yönde (AVD düşer ↔ etkileşim %220 artar) | Ç — ortalama alınmaz |
| dip → klip: 132 / 8 = 16,5 → 17. klip | bu makinede: S16 (0'dan) = 17. klip ✅ | iner (0'dan sayımla) |

# 2. A26 — İKİNCİ İSTASYON · fikir iyi, ayrıntı bizim geometriye uymuyor

| iddia | denetim | hüküm |
|---|---|---|
| EST: mekân/zaman değişimi olay sınırı yaratır | ⚠️ ölçülmüş kaynak TERSİNİ söylüyor: Magliano & Zacks 2011 (Cog Sci 35(8) ✅) — eylem kesintisi bölütlemeyi güçlü etkiler, mekân-zaman kesintisi etkilemez | ters yönüyle iner (A26-a) |
| giriş · doruk · final'de ikinci kamera yok | kaynaklı değil, kuram yorumu | VARSAYIM olarak iner |
| ≤ 2 sn "flash" ek yasak | P2-e (dikey "detay ≤ 2 sn ek") ile çelişir — Ç2 | yatay/dikey ayrımıyla iner |
| ufuk ±%5 | tilt 0'da iki kamerada ufuk %50 — kendiliğinden tutar | ⛔ boş kural |
| pencereye ana kareyi kompozit et | yalnız aynı bakış yönünde geçerli; THE SLOW TAKEOFF'ta kameralar 90° farklı | koşullu iner (§3 ①) |
| VBench/ViCLIP için `[CUT TO: …]` beyanı | kategori hatası: bizim QA'mız Gemini rubriği, VBench değil; kör merceğe plan girmez | ⛔ |
| PySceneDetect eşiği 27 | scenedetect docs ✅ | doğru ama bizim değerlendiricimiz değil |
| LightGlue · ViewCrafter | arXiv 2306.13643 ✅ · 2409.02048 ✅ | yöntem notu |
| ConsiStory arXiv:2412.07750 | ❌ o numara "Motion by Queries"; ConsiStory = 2402.03286 | ⛔ atıf |
| Runway Gen-4.5 · Kling 4.0 · "Seedance 2.5" | Gen-4.5 1 Ara 2025 ✅ · Kling 4.0 duyuru 30 Eyl 2026, tam sürüm Ekim (10 keyframe · 3–30 sn) ✅ · Seedance 2.5 doğrulanmadı | araç kapısında ölçülür |
| prompt şablonu (14 mm · 1,6 m · ufuk %90 · meşe sağda) | bizim geometriyle çelişir | ⛔ — yerine THE SLOW TAKEOFF blokları |

# 3. A27 — SU VE YANSIMA · fizik doğru, benchmark sayıları yanlış, BİZİM hatamızı buldu

```
ÖLÇTÜM (bu makinede, Python)
  x = D·h/(h+y) · ufkun altında 118,5·(h+y)/D   → raporun 12 satırlık tablosu 12/12 tuttu (±0,1 yuvarlama)
  Fresnel dik geliş R = ((n−1)/(n+1))² = %2,04 (rapor "%2–4": %4 cam içindir) · Brewster = atan(1,333) = 53,1° ✅
  kano 4 / 6 / 8 km/sa → 8 sn'de 8,9 / 13,3 / 17,8 m ✅
  ⭐ THE SLOW TAKEOFF (h 3,3 · D 50): gövde altı 17,2 m → üstten 786 · gövde üstü 12,3 m → 883 · kuyruk 8,2 m → 1054
     PLAN/SPEC'te "794–891" yazılmıştı (kadraj yüzdesinde 0,3 m fazla alınmış) → DÜZELTİLDİ (beş dosya)
     raporun yorumu "17 m göletin bittiği yer" YANLIŞ: 17,2 m yükseltilmiş gövdenin ALT kenarının yansımasıdır
```

| iddia | denetim | hüküm |
|---|---|---|
| n = 1,333 · Hale & Querry | Appl Opt 12(3):555, **1973** (rapor 1972, başlıkta "mm") ⚠️ | değer iner |
| Cox–Munk doğrusal | özgün JOSA 1954: σ² = 0,003 + 5,12·10⁻³·U ✅ (rapor ikincil makaleyi gösterdi) | iner |
| dalgacık 2–3 m/s'de başlar | ❌ NOAA Beaufort: pul dalgacık Kuvvet 1'de (0,3–1,5 m/s) | ⛔ — Beaufort iner |
| VideoPhy-2 en iyi %47,7 | ❌ gerçek: %32,6 (tüm set) · %22 (zor) | düzeltilmiş hâliyle iner |
| Physics-IQ zirve 64,5 · diğerleri < %45 | ⚠️ zirve doğru; 2.–6. sıra %56–63; özgün 2025 makalesinde en iyi ~%29,5 | düzeltilmiş iner |
| PhyGenBench 27 yasa | ✅ arXiv 2410.05363 · 160 prompt · en iyi Gen-3 0,51 | iner |
| taşkın 2–5 cm/sa · infiltrasyon 14,7 cm/sa | kaynaksız / arama sayfası | ⛔ |
| rejim ifade tablosu | "jump-cut water level rise" · "fast-sweeping harsh sunlight glare" sıçrama ve parlama davet eder | ayıklanarak iner (SU §5) |

# 4. A28 — IŞIK FİNALİ · tablo doğru ama yanlış etiketli, NegT2IBench gerçek ama sayı karışık

```
ÖLÇTÜM
  alacakaranlık (−2 / −4 / −6°) 35° · 45° · 55° × üç tarih: raporun 9 satırı, GÖRÜNÜR BATIŞTAN (−0,833°) hesaplanınca
  9/9 birebir. Rapor "0° geometrik" dedi — o referansla değerler 4–8 dk daha uzun (ör. 45° Haz −6°: 43,2 ↔ 37,5)
  ⇒ tablo iner, referans düzeltilerek
  1 kare süresi: A 2,5 sn · B 30 sn ✅ · mavi saat ekranda A ≈ 24 sn, B ≈ 2 sn ✅
  THE SLOW TAKEOFF 47° · δ +12°: batış 18:53 · −4,4° 19:20 ✅ (pencere içinde)
```

| iddia | denetim | hüküm |
|---|---|---|
| NegT2IBench: 11 modelin 9'u kötüleşir · %43,8 ters etki | ⚠️ makale var (arXiv 2610.03084, 2 Eki 2026); 9/11 ✅; 43,8 = en büyük PUAN DÜŞÜŞÜ; "yasaklananı çizme" oranı **%41,5**; ışık etkisi ölçülmedi (renk, uzamsal) | doğru sayıyla, DERS 59 desteği olarak iner |
| VBench temporal flickering = kareler arası ortalama mutlak fark | ✅ (yalnız durağan sahnede) | iner (yöntem notu) |
| WCAG 4,5:1 | ✅ SC 1.4.3 | iner (zaten MUZIK_VE_KAPAK'ta) |
| LRTimelapse deflicker · Holy Grail | ✅ | arka plan |
| I2VEdit arXiv:2508.14609 · Animate Anyone 2607.25275 | ❌ ikisi de başka makale (I2VEdit = 2405.16537) | ⛔ atıf; "önce ışıklı final" fikri zaten bizim kuralımız |
| gök 10.000–15.000 K · EV tablosu | hesap sitesi, film için gereksiz | ⛔ |
| "kademeli yanma yalnız kurgu illüzyonu" | abartı — farklı anlarda açılan gruplar gerçek sıralı yanmadır | nüansla iner (IŞIK §2) |

# 5. A29 — ONARIM · yol iyi, yüzdeler uydurma

| iddia | denetim | hüküm |
|---|---|---|
| onarım matrisi başarı yüzdeleri (%80 · %95 …) "ÖLÇÜLDÜ" | hiçbir hücrede kaynak yok | ⛔ yüzdeler — sıralama mantığı iner |
| video inpainting zincirde dikişi kırar · kare düzenle + yeniden koş | atfın başlığı uydurma (2511.03272 başka başlık) ⚠️; mantık bizim zincir kuralımızla aynı | VARSAYIM olarak iner |
| klibi ara kareyle böl | araç dokümanı/rehberler (zayıf) · bizde Gn′ zaten tanımlı | iner |
| warping error zamansal bozulmaya duyarlı | ✅ TRAJAN (arXiv 2505.00209 — rapor başlığı uydurdu) | yöntem notu |
| LPIPS < 0,02 dikiş eşiği | sınanmadı | ⛔ |
| durma kuralı 3 deneme | kaynaksız ama makul | VARSAYIM (3/6) |
| Luma Ray 3.2 "Eylül 2026" · 16 keyframe · EXR | ⚠️ duyuru 9 Haziran 2026; özellikler ✅ | araç kapısında ölçülür |
| Kling 4.0 10 keyframe · 30 sn | ✅ (tam sürüm Ekim 2026) | araç kapısında ölçülür |
| Netflix sürüm adı örneği | ⚠️ gerçek örnek AGM_104_065_010_comp_NFX_v005 (rapor "TCC" uydurdu) | mantık iner |
| EBU Tech 3320 | ✅ var (değerler doğrulanamadı) | arka plan |
| "$0,20 · 2 dk / koşu" · "Bursa'daki ekibiniz" | kaynaksız · uydurma | ⛔ |

# 6. KAYNAKÇA — 33 satır

```
✅ 20  YouTube Help ×5 · Loewenstein 1994 · Cutting 2012 · Magliano & Zacks 2011 · ViewCrafter · LightGlue ·
       PySceneDetect · Kling 4.0 · Cox–Munk · PhyGenBench · VBench · VBench++ · WCAG · LRTimelapse · AceVFI · EBU 3320
⚠️  8  NegT2IBench (sayı karışık) · Hale & Querry (yıl) · Physics-IQ (sıralama) · Runway Gen-4.5 (özellikler) ·
       Netflix ad örneği · Luma Ray 3.2 (tarih) · 2511.03272 (başlık) · 2505.00209 (başlık)
❌  5  I2VEdit numarası · Animate Anyone numarası · ConsiStory numarası · VideoPhy-2 %47,7 · Beaufort eşiği
```

# 7. ÇELİŞKİLER

| # | konu | iki taraf | karar |
|:-:|---|---|---|
| Ç1 | THE SLOW TAKEOFF kalkışı 0:40 | sahip (YouTube "güçlü anı öne al") ↔ A25 (bilgi boşluğu: erken doruk merakı bitirir) | ölçüm sorusu: 0:56 sonrası düşüş (UZUN_FORM §2) · sahip kararı korunur |
| Ç2 | detay ek süresi | P2-e "≤ 2 sn ek" ↔ A26 "2 sn flash yasak" | dikey EK · yatay KLİP (ISTASYON §1) |
| Ç3 | istasyon kesmesi bölütler mi | A26 (EST yorumu: evet) ↔ Magliano & Zacks 2011 (ölçüm: mekân kesintisi hayır, eylem kesintisi evet) | ölçüm kazanır |
| Ç4 | dalgacık eşiği | A27 2–3 m/s ↔ NOAA Beaufort 0,3–1,5 m/s | Beaufort |
| Ç5 | sıralı ışık yanması | A28 "illüzyon" ↔ fiziksel olarak ayrı anlarda açılan gruplar | nüans: fade yok, sıra var |
| Ç6 | final tutuşu | A25 "olay bitimden 15–20 sn önce" ↔ kartsız 4 sn tutuş (BORROWED HILL · SLOW TAKEOFF) | son ekran yok / gök bandı; uzun tutuş 6/8 dk'da sahip isterse |

# 8. NE İNDİ, NE İNMEDİ

```
İNDİ    UZUN_FORM_ANLATI_KILAVUZU · ISTASYON_VE_IC_MEKAN_KILAVUZU · SU_VE_YANSIMA_KILAVUZU ·
        ISIK_FINALI_KILAVUZU · ONARIM_VE_YENIDEN_URETIM_KILAVUZU  (kilavuzlar/ · 07.10.2026)
        DERSLER.md · A25-a … A29-e (VARSAYIM; ilk sınavı THE SLOW TAKEOFF üretimi ve yayını)
        THE SLOW TAKEOFF düzeltmesi: yansıma bandı 786–883 (PLAN · SPEC · 00_ANALIZ/01 · 02)
İNMEDİ  her raporun kendi "ÖLÇÜLDÜ" yüzdeleri (tutma kıyasları · onarım başarı oranları · benchmark sayıları
        düzeltilmeden) · uydurma atıflar · bizim formata uymayan şablonlar (A26 prompt şablonu · A27 rejim
        ifadelerinin üçte biri)
```
