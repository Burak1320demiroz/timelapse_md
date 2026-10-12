# 📏 A21 — ÖLÇÜM ZEMİNİ: değerlendiricinin ölçemediğini makine ölçer

```
AMAÇ      Video-dil modelinin GÜVENİLMEZ olduğu ölçümleri (süre, oynatma
          hızı, klip/kesme sayısı, zaman damgası, kart var mı) ondan almak;
          makinede ölçüp rubriğe "ÖLÇÜLMÜŞ OLGULAR" bloğu olarak vermek —
          model yargıyı yapar, sayıyı yapmaz.
KARŞILIĞI 06.10.2026 QA denetimi:
          · 2x paylaşım kopyası "kesik" okundu — en az 6 film (BROKEN CLIMB ·
            STAR DOCK · STONE TOWER · DEEP STEP · BACK TO PLUMB · LAST LIFT ~1,5x);
            "56 sn yerine 32 sn'de bitiyor" → final vuruşu 0-3/10
          · aynı dosyada mercekler arası klip sayısı: DEEP STEP 1·7·9·12·17·18 ·
            STAR DOCK 2·8·23 · MOUNTAIN CROWN 7·8·12·16
          · aynı yatay dosyanın süresi üç mercekte 109 · 125 · 148 sn
          · 10 rubrik "dosya statik kartla biter" diyor — 2x'te 4 sn'lik
            7. klip kart sanılabilir
          · 2x beyanı yalnız paket başlığında, yapıştırılan rubriğin DIŞINDA
DÖNÜŞÜ    kilavuzlar/QA_OLCUM_ZEMINI_KILAVUZU.md (✅ 06.10.2026 yazıldı) ·
          araclar/qa_paket.sh (ÖLÇÜLMÜŞ OLGULAR bloğu) · kare_al.sh ·
          kesme_kontrol.sh · ihrac_kontrol.sh
          ⚠️ Sınır: A20 = değerlendiriciye NE gittiği · burası = değerlendiriciye
             hangi SAYININ hazır verileceği
KOŞU      ✅ 06.10.2026 yazıldı ve koşuldu · SONUCLAR/A21_GEMINI_HAM.md · denetim A20-A24_DENETIM.md
```

⛔ **Model videoyu saniyede bir kare gibi seyrek örnekliyor olabilir.** 2x'te
4 sn'lik bir klip o zaman 4 kareye düşer; kesme sayısını ve süreyi tahminle
dolduruyor. Bu bir rubrik sorunu değil, ölçüm aracının sınırıdır.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen çok kipli büyük dil modellerinin video anlama sınırları, zamansal temellendirme (temporal grounding) ve otomatik video ölçümü (ffmpeg/ffprobe, sahne kesme tespiti) üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat timelapse filmleri — dikey (9:16) filmler her zaman 7 klip × 8,0 sn = 56 sn olarak üretilip 2 kat hızda (~28 sn, her klip ekranda 4 sn) yayımlanıyor, yatay (16:9) filmler 12–18 klip × 8–10 sn olarak normal hızda yayımlanıyor, bazı filmlerin sonunda 4–5 sn'lik statik bir kart var bazılarında yok, kamera bütün kliplerde aynı noktada sabit ve klipler arası sert kesme var (geçiş efekti yok) — ve her film Gemini'nin sohbet arayüzüne video + yaklaşık 30 kare görüntüsü yüklenerek 12 İngilizce rubrikle puanlanıyor; rubrikler zaman damgası (m:ss.s), klip sayısı, kesme yerleri, final karesinin kaç saniye tutulduğu ve kartın varlığı gibi SAYISAL gözlemler istiyor.

Ölçülmüş arıza şu: değerlendirici 2 kat hızlı yayın kopyasını en az altı filmde "56 saniye yerine 32 saniyede bitiyor, final kesilmiş" diye okudu ve final vuruşuna 0–3/10 verdi (paket başlığında hız beyanı vardı ama yapıştırılan rubriğin dışında kaldı), aynı dosyada farklı rubrikler klip sayısını 1, 7, 9, 12, 17 ve 18 olarak saydı, aynı yatay dosyanın süresini üç rubrik 109, 125 ve 148 saniye olarak verdi, rubriklerin onu "dosya statik bir kartla biter" diye varsaydığı için 2x'te 4 saniyelik yedinci klibin kart sanılma riski var, ve dosya süresinden sonraya düşen zaman damgaları görüldü — yani model sayıyı ÖLÇMÜYOR, tahmin ediyor ve tahmini hükme çeviriyor.

Birinci görevin: Gemini (1.5, 2.0, 2.5 ve sonrası) başta olmak üzere çok kipli modellerin videoyu nasıl içeri aldığını belgelenmiş verilerle yaz — varsayılan kare örnekleme hızı (fps), API'deki fps ve medya çözünürlüğü (media resolution) ayarları, sohbet arayüzü ile API arasındaki fark, sesin işlenmesi, zaman damgası çözünürlüğü — ve bu modellerin süre tahmini, kesme/çekim sayma, olay sayma, zaman damgası doğruluğu, oynatma hızı (hızlandırılmış video) tespiti ve "video hallucination" üzerine ölçülmüş başarımını benchmark adıyla ve sayıyla tablo hâlinde ver (Video-MME, TempCompass, MVBench, VideoHallucer, Charades-STA / temporal grounding, sayma ve hız algılama çalışmaları); 4 saniyelik bir klibin seyrek örneklemede kaç kareye düştüğünü ve bunun sabit kameralı, yavaş değişen timelapse görüntüsünde kesme tespitine etkisini ayrıca yaz.

İkinci görevin: "makine ölçer, model yargılar" düzenini (hibrit değerlendirme, measured-facts grounding, tool-augmented evaluation) belgelenmiş örneklerle anlat — hangi ölçümlerin makineye devredilmesi gerektiğini (ffprobe süre/çözünürlük/kare hızı/ses akışı, ffmpeg scene skoru ya da PySceneDetect ile kesme zamanları ve klip sayısı, son N saniyede SSIM ile statik kart/final tutuşu tespiti, siyah kare, kareler arası kamera kayması, klip başına hareket miktarı), bu ölçümlerin modele hangi biçimde verildiğinde (rubriğin başında olgu bloğu, kesme listesi, kareye yakılmış zaman damgası, klip numaralı kare tablosu) modelin onlarla çelişmesinin azaldığını ölçülmüş verilerle yaz; ve hızlandırılmış kopya yerine normal hızlı ana dosyayı değerlendirmenin ya da ikisini birden vermenin artısını ve eksisini (izleyicinin gördüğü şey ile örnekleme yoğunluğu arasındaki takas) tablo hâlinde karşılaştır.

Üçüncü görevin: kare görüntüsü desteğini tasarla — klip başına kaç kare, hangi konumlardan (ilk, orta, son, kesmenin iki yanı), tek tek mi yoksa iletişim tabakası (contact sheet) hâlinde mi, karenin üstüne zaman damgası ve klip numarası yakmanın etkisi — bunlarla ilgili ölçülmüş çalışmaları yaz; ve model raporundaki her zaman damgasını makinenin kesme listesiyle otomatik karşılaştırıp uydurulmuş ya da dosya dışına düşen zaman damgasını yakalayan bir doğrulama yöntemini (tolerans, eşleme kuralı, hangi oranda hatada raporun reddedileceği) belgelenmiş benzerleriyle öner.

Rapor Türkçe olsun, araç, parametre ve benchmark adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, benchmark ya da resmi doküman var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · model/araç dokümanı · bağımsız karşılaştırma · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI, arXiv numarası ya da doküman adı + bölüm + tarih; kaynağı gösterilemeyen sayı ÖLÇÜLDÜ etiketi alamaz) yaz, model sürümleri arasında fark varsa sürüm sürüm yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) her rubriğin en başına yapıştırılacak İngilizce bir "MEASURED FACTS — do not re-estimate these" blok şablonu (dosya süresi, oynatma hızı ve 1x↔yayın zaman eşlemesi, klip sayısı ve her kesmenin zaman damgası, kart var/yok ve aralığı, final karesinin tutulduğu süre, ses akışı var/yok) ve (b) bu bloğun her satırını üreten, kopyalanıp çalıştırılabilir ffprobe, ffmpeg ve PySceneDetect komut satırlarını ver — her komutun çıktısının nasıl okunacağını tek cümleyle açıkla.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A21_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         VARSAYIMLAR.md · kuşak bölümüne (+ DİZİN satırı)  A21-a, A21-b…
3. KILAVUZ     kilavuzlar/QA_OLCUM_ZEMINI_KILAVUZU.md bu rapordan yazılır
4. KAPI        qa_paket.sh: MEASURED FACTS bloğu rubriğin İÇİNE, yapıştırma
               çizgisinin ALTINA yazılır · komutlar bu makinede koşmadan inmez
               [A5-A8 denetimi: iki ffmpeg komutu koşmadı]
```
