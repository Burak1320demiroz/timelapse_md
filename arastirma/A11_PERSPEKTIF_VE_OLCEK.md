# 📐 A11 — PERSPEKTİF VE ÖLÇEK

```
AMAÇ      Ölçek tutarlılığını kurmak: referans nesneleriyle ölçeğin sahneler
          arası sabitlenmesi, perspektif kuralları, piksel-metre dönüşümü,
          zincirde ölçek kayması.
KARŞILIĞI ① KARE  ⛔ STATION IDENTITY 0/10 · "horizon sits at roughly 58% … shifts to 68%"
          ② İNŞA  SCALE LOCK 0 · 4 · 7/10 — beş filmde yapı boyutu değişti
          DERS 5  (her klip başka bina = ölçek kayması)
          DERS 6  (kamera kayması — zoom/pan)
          DERS 19 (sayılı çapa 10/10, sayısız bible 2/10 — aynı filmde)
          DERS 38 (D_kenar vs D_eksen — mesafe hesabı yanlış)
          P2-b (sayı testi: izleyici SAYABİLİYOR mu) · A3-c (seed ve referans
          görsel geometriyi taşımaz) · A5-c ÖLÇTÜM (33,7 × 60,0 m · 32 px/m)
DÖNÜŞÜ    kilavuzlar/PERSPEKTIF_VE_OLCEK_KILAVUZU.md (HENÜZ YOK — bu prompt
          onu yazdıracak) · PROMPT_SABLONU COMPOSITION bloğu · prompt_kontrol.py
          ⚠️ KAMERA_ISTASYONU §3 ile sınır: KAMERA = kameranın sayıları,
             burası = modelin o geometriyi TUTMASI
KOŞU      ⛔ koşulmadı — v1 08.09.2026 · v2 11.09.2026
SÜRÜM v2  altı cümleye tamamlandı (A5 kalıbı) · sayılabilir/sayılamaz sayı
          bulgusu eklendi · iki-keyframe I2V'de klip içi ölçek eklendi · ölçülmüş
          kadraj sayıları (34 × 60 m · 32 px/m) verildi · ÇÖZÜMLENEBİLİR KAYNAK
          şartı eklendi · örnek cümlenin piksel hesabı düzeltildi
```

⛔ **Kamera sabit, ama model ölçeği sahneden sahneye sürüklüyor.** KAMERA_ISTASYONU
kadraj formülünü veriyor; ölçeği TUTAN referans nesneleri sistematik değil.
Gerçek timelapse'te ölçek hiç değişmez çünkü sahne fiziksel olarak sabit.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen görüntü ölçeği, perspektif geometri, sabit kamera fotogrametrisi ve üretken görüntü modellerinde geometrik tutarlılık üzerine çalışan bir araştırmacısın; benim ürünüm 9:16 dikey, konuşmasız, yapay zekâ ile üretilmiş bir inşaat timelapse filmi: 10 sahne, her sahne yaklaşık 6 saniye, kamera on sahnede aynı noktada sabit (24 mm eşdeğeri, yapıya ~40 m mesafe, tilt 0°, kadraj yaklaşık 34 × 60 m, yani 1080×1920 karede ~32 piksel/metre), her klip iki onaylı SABİT görsel arasında image-to-video ile üretiliyor (ilk kare ve son kare birer fotoğraf, video ikisini bağlıyor), sahne görselleri bir usta kareden geriye doğru türetiliyor ve her film bağımsız bir denetçi tarafından zaman damgalı rubriklerle puanlanıyor.

Ölçülmüş arıza şu: kamera her promptta sayıyla (lens, yükseklik, mesafe, bakış açısı, tilt) sabitlenmişken denetçi altı filmin beşinde ölçeğin kaydığını ölçtü — "the horizon sits at roughly 58% of the frame, but shifts to 68% at 0:18", "the horizon line shifts upward by 5 percentage points compared to the previous clip in the same vantage group", "the camera perspective and horizon line shift across the cut, breaking the anchor lock and causing the scene to read as a new location", SCALE LOCK puanları 0, 4 ve 7/10 — ve aynı filmin içinde iki karşıt sonuç birlikte ölçüldü: SAYILABİLİR çapalar ("exactly three rooftop chimneys", "exactly five evenly spaced upper-floor windows") on sahnede 10/10 tuttu, SAYISIZ tarif ("regular structural bays", "as described") 2/10 aldı ve yapının oturumu bir kareden diğerine bariz daraldı; ardışık kare türetmede ölçek her halkada biraz daha kaydı.

Birinci görevin: sabit kamera timelapse'te ölçeğin KAYMASINI engelleyen REFERANS NESNELERİNİ saha tipine göre (şehir içi, kırsal, kıyı, dağ, çöl, Ay/Mars yüzeyi, buzul) tablo hâlinde yaz — her nesne için gerçek boyut (metre), benim kadrajımda (24 mm eşdeğeri, 40 m, 1080×1920, ~32 piksel/metre) piksel karşılığı, film boyunca DEĞİŞMEMESİ gerektiği (ufuk çizgisi, komşu bina, tek ağaç, kaya, krater kenarı, sırt hattı, deniz feneri), aynı yerde aynı boyutta her karede görünür olma şartı — ve ÖLÇEĞİ DEĞİŞEN nesnelerin (yapının kendisi, iskele, vinç, berm, malzeme yığını) neden referans OLAMAYACAĞINI açıkla; ayrıca gerçek uzun dönem timelapse kurulumlarından (Brinno, Enlaps Tikee, EarthCam, Canon EOS tabanlı sabit kurulumlar) alınan kadraj geometrisi verilerini ve "aynı kare mi" doğrulama pratiklerini (kenar çakıştırma, referans çizgileri, piksel farkı) aktar.

İkinci görevin: tilt 0° sabit kameranın perspektif geometri kurallarını — ufuk çizgisinin kare yüksekliğinin tam yarısında olması, kaçış noktası sabitliği, yakın/uzak nesne oranının sabitliği, paralaks yokluğu, dikey çizgilerin dik kalması, atmosferik perspektif (uzaktaki nesnenin daha açık ve düşük kontrastlı olması) — ve bu kuralların bir görüntü üretim promptuna NASIL yazılacağını ver; özellikle "model ufku neden kaydırıyor", "model yapıyı neden bir sonraki karede daha büyük ya da daha dar çiziyor", "tek görselde bir nesnenin yerini kare yüzdesi ya da piksel olarak vermek işe yarıyor mu, hangi modellerde ölçüldü" ve "iki görsel arasında üretilen videoda ölçek klip İÇİNDE kayıyor mu, kayıyorsa nasıl ölçülür" sorularını hakemli kaynak ve araç dokümanıyla yanıtla.

Üçüncü görevin: AI görüntü ve video üretiminde ölçek tutarlılığı için prompt ve iş akışı tekniklerini araştır — boyut çapası (bir nesneyi başka nesneyle karşılaştırarak tanımlama: "the boulder is one third of the habitat height"), göreli oran, kare yüzdesiyle kompozisyon, SAYILABİLİR sayı (modellerin hangi sayıları tutabildiği: "three chimneys" evet, "sixty-two lamps" hayır — sayı sadakati ve nesne sayma üzerine ölçülmüş çalışmalar, hangi sayıya kadar), negatif ölçek cümlesi ile pozitif çapanın karşılaştırması — ve her tekniğin ölçülmüş etkinliğini (varsa) yaz; ardışık kare türetmede (bir kareden sonrakini image-to-image ile türetme) ölçek hatasının nasıl BİRİKTİĞİNİ ve bunu engelleyen yöntemleri (depth/canny/MLSD kontrol kanalı, 3D kaba kütle referansı, seed ve IP-Adapter/referans görselin neyi taşıyıp neyi taşımadığı) belgelenmiş örneklerle açıkla.

Rapor Türkçe olsun, geometri terimleri ve parametre adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, ölçüm ya da deney var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · araç dokümanı · standart/şartname · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI ya da belge adı + bölüm; kaynağı gösterilemeyen sayı ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç ve yukarıda yanlış bulduğun her şeyi orada topla; en sonda her saha tipi için üretim promptuna doğrudan yapıştırılacak, İngilizce ve POZİTİF (yasak cümlesi değil, ölçülebilir betimleme) birer COMPOSITION ölçek cümlesi ver, örneğin "the split-top boulder to frame right spans 108 pixels of frame width — one tenth of the frame — and keeps that width from the first frame to the last; the horizon sits at exactly half the frame height throughout".

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A11_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         VARSAYIMLAR.md · kuşak bölümüne (+ DİZİN satırı)  A11-a, A11-b…
3. KILAVUZ     kilavuzlar/PERSPEKTIF_VE_OLCEK_KILAVUZU.md bu rapordan yazılır
               (ya da proje sahibi kararıyla KAMERA_ISTASYONU §7–§9)
4. KAPI        prompt_kontrol.py: COMPOSITION bloğunda ≥1 ölçek referansı + piksel
```
