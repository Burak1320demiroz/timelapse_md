# 🧪 A26 — İKİNCİ İSTASYON VE İÇ MEKÂN

```
AMAÇ      Sabit kameralı timelapse'e İKİNCİ bir sabit kameranın (iç mekân · yakın iş · detay) ne
          zaman, kaç klip, filmin neresinde ve hangi kurallarla girebileceğini ölçülebilir hâle
          getirmek: "aynı yer" okumasını koruyan ortak çapa, iki kamera arasında kare zincirinin
          nasıl kurulacağı (paralel zaman, iki ayrı kare), iç mekânın kendi timelapse dili ve
          değerlendiriciye beyan.
KARŞILIĞI 07.10.2026 THE SLOW TAKEOFF + arşiv ölçümleri:
          · kural çelişkisi: "detay istasyonu ≤2 sn ek, merdiven satırı almaz" ↔ "bir filmde en fazla iki
            detay SAHNESİ, aynı istasyondan" ↔ sahibin iki tam 8 sn kokpit klibi (sahip kararı)
          · OVER THE WALL: plan dışı ikinci istasyon (ufuk %92 ↔ %73) → değerlendirici "SIX SEPARATE SHOTS",
            aynı kesmede üç mercek düştü · THE LONG SHADOW: üç vantaj → "ALTI AYRI GÖRÜNTÜ" ·
            THE CLOSING SPAN: ikinci istasyon farklı lens + kendi SITE metniyle → film parçalandı (0,77) ·
            THE BROKEN CLIMB: 4 vantaj + push-in → SIX SEPARATE SHOTS
          · zincir sorunu: istasyon değişen kesmede iki yaka aynı kare olamaz → iki ayrı kare + paralel
            zaman beyanı; prompt kapısı kokpit karesini ana kareyle eşleştirip yanlış alarm verdi
          · iç mekân ana kameradan OKUNMAZ: kabin penceresi ≈8 px; kokpit kamerası batıya bakıyor,
            S21'de güneş kadraj içinde (bulut arkasına yazıldı)
DÖNÜŞÜ    kilavuzlar/ISTASYON_VE_IC_MEKAN_KILAVUZU.md (✅ 07.10.2026 yazıldı) · KAMERA_ISTASYONU §1 güncellemesi ·
          araclar/prompt_kontrol.py istasyon farkındalığı · QA ❶ beyan satırı
          ⚠️ Sınır: A3 (zincir ve tutarlılık) tek istasyonluydu; A13/A19 kamera hareketi idi — burası
             İKİ SABİT kamera arasında geçiş
KOŞU      ✅ 07.10.2026 yazıldı ve koşuldu · SONUCLAR/A26_GEMINI_HAM.md · denetim A25-A29_DENETIM.md
```

⛔ **Kamera hareketi bu raporun konusu DEĞİL** — iki kamera da kendi içinde kımıldamaz. Rapor
"tracking shot · gimbal · drone" önerirse soru yanlış okunmuştur.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen kurgu kuramı (mekânsal süreklilik, establishing shot, insert ve cutaway), uzun süreli inşaat timelapse kameraları ve yapay zekâ ile görüntü/video üretiminde çok bakışlı tutarlılık (multi-view / cross-shot consistency) üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — kamera bütün filmde tek ve kilitli (tilt 0, hiç kıpırdamaz), her kesme yalnızca zamanı atlar, ve her klip İKİ sabit görüntü arasında üretilir: bir klibin son karesi bir sonraki klibin ilk karesidir (iki keyframe zinciri; kareler filmin son karesinden geriye doğru image-to-image türetilir), yani dikişte ışık, gölge ve yapı hiç atlamaz — ve şimdi ilk kez filme ikinci bir sabit kamera ekledim: yolcu uçağından göl evine dönüşen 4 dakikalık (30 klip × 8 sn) bir filmde 28 klip dışarıdaki ana kameradan, 2 klip uçağın kokpitinin içine sabitlenmiş bir kameradan (ön camdan göl, meşe ve karşı kıyı görünüyor).

Ölçülmüş arıza ve açık sorun şu: önceki filmlerde plansız ikinci bir kamera konumu, bir kesmede ufuk çizgisi %92'den %73'e kayınca yapay zekâ değerlendiricisi filmi "altı ayrı çekim" diye okudu ve aynı saniyede üç ayrı rubrik düştü, üç vantajlı bir film "altı ayrı görüntü" sayıldı, farklı lensli ve kendi arka plan tarifiyle yazılmış ikinci kamera filmi parçaladı; kendi kurallarım çelişiyor (bir yerde "detay kamerası en fazla 2 saniyelik bir ek, aşama taşımaz", başka yerde "filmde en fazla iki detay sahnesi"), ikinci kameraya geçilen kesmede iki tarafın aynı kare olması imkânsız olduğu için iki ayrı kare ve "dışarıdaki aynı on dakikanın içeriden görüntüsü" diye paralel bir zaman beyanı yazdım ama bunun izleyiciye ve değerlendiriciye nasıl okunacağını bilmiyorum; ayrıca iç mekân dönüşümü ana kameradan hiç okunmuyor (kabin pencereleri kadrajda yaklaşık 8 piksel), bu yüzden mutfak ve yatak gibi işleri yalnızca eksilen sandıklar ve merdivenden taşınan parçalarla anlatıyorum.

Birinci görevin: gerçek yapımlarda iki sabit kamera arasında "aynı yer" okumasının nasıl korunduğunu belgelenmiş kaynaklarla yaz — süreklilik kurgusu kuramı (180° kuralı, eksen, establishing → insert → geri dönüş, match on action, cutaway; dikkat ve olay bölütleme üzerine bilişsel film çalışmaları), uzun süreli inşaat kamerası hizmetlerinin ve iç mekân tadilat timelapse'lerinin dış ve iç kameraları nasıl kurduğu ve kurguda nasıl birleştirdiği, iki görüntüde de görünen ortak çapa nesnesinin (pencereden görünen ağaç, ufuk çizgisi, karşı kıyı) uzamsal yönelimi korumadaki rolü, izleyicinin kaç farklı bakış açısını "tek yer" olarak tolere ettiği ve ikinci kameraya geçişin filmin neresinde (doruk, bölüm sınırı, final) yapılmaması gerektiği — her iddianın etiketiyle.

İkinci görevin: yapay zekâ üretiminde iki bakış açısı arasında aynı dünyayı korumanın yollarını tarihli kaynaklarla karşılaştır — çok bakışlı tutarlılık araştırması (multi-view diffusion, reference-image conditioning, IP-Adapter benzeri yöntemler, "consistent scene across shots" özellikleri), ticari araçların ilk/son kare ve çoklu referans görsel desteği (2025–2026 sürümleri), bilinen arızalar (ikinci bakışta başka bir dünya, nesne sayısının değişmesi, ışığın tutmaması), ikinci kameranın ilk karesini ana kameranın onaylı karesinden TÜRETMENİN yolları (aynı aşamanın dış karesini referans vermek, pencereden görünen dış dünyayı ana kareyle eşlemek) ve iç mekân timelapse'inin görsel dili (pencereden düşen ışık lekesinin kayması, mobilya akışı, iz bırakan ama yüzü okunmayan insan, iç/dış pozlama ve beyaz dengesi farkı, pencere patlaması).

Üçüncü görevin: zinciri ve ölçümü yaz — istasyon değişen kesmede kare adlandırma ve zincir şeması (ana kare iki yakada aynı kalırken iç klibin kendi iki karesi), paralel zamanın ışık sürekliliğiyle nasıl tutarlı kılınacağı (dışarıda 10 dakika ≈ güneş 2,5°), iki bakış arasında "aynı yer"i otomatik doğrulamanın yolları (ortak çapa üzerinde öznitelik eşleme — feature matching —, SSIM/DINO benzerliği, ufuk yüksekliği ölçümü) ve bunların ölçülmüş güvenilirliği, ve yapay zekâ değerlendiricisine (filmi planı görmeden okuyan kör bir rubrik) ikinci kameranın BEYAN edilip edilmemesinin körlüğe ve puana etkisi — belgelenmiş verilerle.

Rapor Türkçe olsun, kurgu terimleri, araç ve yöntem adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, ölçüm ya da resmi belge var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · araç/platform dokümanı · bağımsız karşılaştırma · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI ya da belge adı + bölüm + tarih; araç davranışı için tarihli sürüm notu — kaynağı gösterilemeyen iddia ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) bir KARAR TABLOSU (ikinci kamera ne zaman izinli: klip sayısı · süre · filmdeki konum · YASAK konumlar · ortak çapa şartı), (b) istasyon değişimi için kare adlandırma ve zincir ŞEMASI şablonu, (c) ikinci kamera görsel promptu için İngilizce blok şablonu (Camera satırı: lens, yükseklik, mesafe, bakış derecesi, tilt, roll; ana kamerayla birebir paylaşılan arka plan cümlesi; iç mekân zaman hızı cümlesi) ve (d) en fazla 12 maddelik bir kontrol listesi ver — her madde için ihlalde yapılacak tek eylem (KAMERAYI KALDIR · KAREYİ YENİDEN ÜRET · BEYAN EKLE).

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A26_<BOT>_HAM.md — dokunulmadan [kart S]
2. DENETİM     SONUCLAR/A25-A29_DENETIM.md
3. KOD         DERSLER.md · DEVRALINAN bölümüne  A26-a, A26-b…
4. KILAVUZ     kilavuzlar/ISTASYON_VE_IC_MEKAN_KILAVUZU.md · KAMERA_ISTASYONU §1 çelişkisi kapanır
5. KAPI        prompt_kontrol.py: istasyon farkındalığı (DERS 61 eşleştirmesi kokpit karesini atlar) ·
               ikinci istasyon beyanı SPEC künyesinde zorunlu
```
