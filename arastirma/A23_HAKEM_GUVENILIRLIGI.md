# ⚖️ A23 — HAKEM GÜVENİLİRLİĞİ VE KALİBRASYON

```
AMAÇ      Değerlendirici modelin kendisini ölçmek: aynı filme iki kez aynı
          puanı veriyor mu (test-tekrar), mercekler birbiriyle tutarlı mı,
          kusuru BİLİNEN bir videoda kusuru buluyor mu (tohumlanmış kusur
          seti), zamanla kayıyor mu — ve QA puanı izleyiciyle tutuyor mu.
KARŞILIĞI 06.10.2026 QA denetimi:
          · hiçbir film iki kez aynı mercekle koşulmadı — test-tekrar YOK
          · STONE DRAGON: iki denetim aynı filme RED ve ONAY dedi
          · DEEP STEP ⑪ "modern kamyon davetsiz" · ⑫ aynı kamyona "HOLDS"
          · BROKEN CLIMB ① 4,1 (kamera sıçraması) · ⑦ 10/10 "kusur yok"
          · ortalamalar 24-28.09'da 9,7-9,8 → 04-05.10'da 7,4-8,4; aynı
            haftada girdi koşulları değişti — film mi değişti hakem mi, bilinmiyor
          · QA_CAPRAZ_ANALIZ 18.09'da kaldı · izleyici verisiyle hiç karşılaştırılmadı
DÖNÜŞÜ    kilavuzlar/QA_KALIBRASYON_KILAVUZU.md (✅ 06.10.2026 yazıldı) ·
          apexait/IZLEYICI_DEFTERI.md §3 · QA/ARSIV_12_MERCEK/QA_CAPRAZ_ANALIZ/06
          ⚠️ Sınır: A22 = ölçeğin tasarımı · burası = ölçeği kullananın tutarlılığı
             ve ölçeğin dış geçerliliği
KOŞU      ✅ 06.10.2026 yazıldı ve koşuldu · SONUCLAR/A23_GEMINI_HAM.md · denetim A20-A24_DENETIM.md
```

⛔ **Kalibrasyon olmadan puan farkı bilgi değildir.** 9,8 ile 7,4 arasındaki
farkın ne kadarı film, ne kadarı hakem gürültüsü — bunu bilen tek sayı
test-tekrar sapmasıdır ve depoda yok.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen değerlendirici güvenilirliği (inter-rater ve test-retest reliability), büyük dil modellerinin hakem olarak kalibrasyonu ve kısa video izleyici metriklerinin istatistiksel analizi üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat timelapse filmleri — dikey (9:16) filmler 7 klip × 8,0 sn olarak üretilip 2 kat hızda (~28 sn) YouTube Shorts'ta yayımlanıyor, yatay filmler 2 dakika civarı — ve her film bir çok kipli model (Gemini, sohbet arayüzü) tarafından 12 ayrı İngilizce rubrikle 0–10 puanlanıyor; şimdiye kadar yaklaşık 30 film puanlandı, her film her rubrikle yalnız BİR kez koşuldu, ve kanal yeni olduğu için her film için yayından 7 gün sonra dört izleyici sayısı toplamayı planlıyoruz (izlemeyi seçenlerin oranı "viewed vs swiped away", ortalama izlenme yüzdesi, engaged views, videodan gelen abone).

Ölçülmüş arıza şu: hiçbir film aynı rubrikle iki kez koşulmadığı için değerlendiricinin kendi gürültüsünü bilmiyoruz, aynı filme iki ayrı denetim biri "RED" biri "ONAY" dedi, aynı filmin bir rubriği yoldaki modern kamyonları "davetsiz nesne" diye cezalandırırken başka bir rubrik aynı kamyona "fiziksel olarak tutarlı" puanı verdi, bir filmde kamera sıçraması için 4,1 veren rubrikle aynı filme "hiç kusur yok" diyerek 10/10 veren rubrik yan yana duruyor, film ortalamaları bir hafta içinde 9,7–9,8'den 7,4–8,4'e düştü ama aynı hafta değerlendiriciye verilen girdiler de değişti (hızlandırılmış kopya, eksik belge, yanlış belge) — yani düşüşün ne kadarının film ne kadarının hakem olduğunu ayıramıyoruz — ve QA puanının izleyici davranışını öngörüp öngörmediği hiç sınanmadı.

Birinci görevin: LLM hakem güvenilirliğinin nasıl ölçüldüğünü ve ölçülmüş büyüklüklerini yaz — aynı girdiyle tekrarlanan koşularda puan sapması (test-retest), farklı modeller arası uyum (Gemini, GPT, Claude), bunun için hangi istatistiğin kullanıldığı (ICC, Krippendorff alpha, Cohen/Fleiss kappa, Spearman) ve kabul eşikleri, güvenilir bir ortalama için kaç tekrar gerektiği, sıcaklık/örnekleme ayarının etkisi, ve bilinen sistematik yanlılıkların (puan şişmesi/leniency, belgeye çapalanma, uzunluk ve konum yanlılığı, kendini kayırma, video modellerinde halüsinasyon) literatürdeki ölçülmüş büyüklüklerini — özellikle çok kipli ve video hakemler için — sayıyla ve çalışma adıyla tablo hâlinde ver.

İkinci görevin: kalibrasyon setini tasarla — kusuru BİLİNEN çapa videolar (golden set) ve bilerek tohumlanmış kusurlar (sert bir kamera kayması, tek karede kaybolan bir nesne, iki klip arasında yapının boyunun değişmesi, 2 kat hızlandırılmış kopya, eksik son klip, sonradan eklenmiş yazı) ile her rubriğin yakalama oranını (duyarlılık) ve yanlış alarm oranını ölçen bir "bilinen cevaplı test" yöntemini, model sürümü değiştiğinde ya da rubrik değiştiğinde yeniden kalibrasyon kuralını ve zaman içinde hakem kaymasını izleyen kontrol grafiği (control chart) yaklaşımını belgelenmiş benzerleriyle (makine öğrenmesi değerlendirme kalibrasyonu, yayın QC eğitim setleri, tıbbi görüntüleme okuyucu çalışmaları) anlat; aynı filmin rubrikleri birbiriyle çeliştiğinde (bir rubrik kusur buluyor, öteki aynı anda "kusur yok" diyor) bunun otomatik tespiti ve hangi hükmün geçerli sayılacağı için kural öner.

Üçüncü görevin: iç kalite puanının DIŞ geçerliliğini nasıl sınayacağımı yaz — 20–40 filmlik küçük örnekte QA puanı ile Shorts izleyici metrikleri arasındaki ilişkinin hangi istatistikle (sıra korelasyonu, karma model) sınanacağı, belli bir etki büyüklüğünü görmek için kaç film gerektiği (güç analizi), yayın tarihi, konu, algoritmik dağıtım ve kanal büyümesi gibi karıştırıcıların nasıl kontrol edileceği, ve kısa dikey videolarda izlemeye devam etmeyi ve tekrar izlemeyi öngördüğü ölçülmüş görsel/yapısal özellikler hakkında (ilk saniyeler, döngü, son an, tempo) bağımsız veriyi YouTube'un resmi dokümanları ve akademik çalışmalarla ayırarak yaz.

Rapor Türkçe olsun, istatistik ve değerlendirme terimleri İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı ya da deney var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · platform/araç dokümanı · bağımsız karşılaştırma · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI, arXiv numarası ya da belge adı + bölüm; kaynağı gösterilemeyen sayı ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) sayılarıyla bir KALİBRASYON PROTOKOLÜ tablosu (hangi sıklıkla, kaç tekrar, hangi uyum eşiği, eşiğin altında tek eylem), (b) 10 tohumlanmış kusurluk bir test seti tarifi (her kusurun hangi rubrikçe yakalanması gerektiği ve her birini sağlam bir videodan üreten kopyalanıp çalıştırılabilir ffmpeg komutu) ve (c) QA puanı ile izleyici metriklerini yan yana tutacak tablo düzenini ve ilk anlamlı karşılaştırma için gereken asgari film sayısını ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A23_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A23-a, A23-b…
3. KILAVUZ     kilavuzlar/QA_KALIBRASYON_KILAVUZU.md bu rapordan yazılır
4. KAPI        tohumlanmış kusur seti bu makinede üretilir (komutlar koşmadan inmez) ·
               IZLEYICI_DEFTERI §3 ve QA_CAPRAZ_ANALIZ/06 tek plana birleşir
```
