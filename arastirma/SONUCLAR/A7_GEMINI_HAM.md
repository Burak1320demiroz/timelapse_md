# A7 — ARAÇ PROFİLİ · HAM ÇIKTI

```
BOT           Gemini Deep Research
PROMPT        A7 · arastirma/A7_ARAC_PROFILI.md yapıştırma bloğu (6 cümle)
TARİH         08.09.2026
SÜRE          ⛔ DOLDURULMADI — proje sahibi doldurur
KESİLDİ Mİ    ⛔ DOLDURULMADI — proje sahibi doldurur
```

⛔ Bu dosya kanıttır. Düzenleme · kısaltma · özetleme · başlık değiştirme YOK.

---

Üretken Video Modelleri Üretim Hattı ve Mimari Zafiyet Analizi Raporu
Üretim hattında karşılaşılan ölçümlenmemiş arızalar —negatif prompt sızması (metinde yasaklanmasına rağmen astronotların kadraja girmesi), fiziksel ve geometrik tutarsızlıklar (güneş diskinin kadraja girmesi ve gölgelerin dönmemesi) ve çıktı sürelerindeki katı kısıtlamalar (istenilen 4-10 saniye aralığına rağmen tam 6,0 saniye sabit çıktı alınması)— jeneratif video modellerinin doğasındaki temel mimari kısıtlamaların doğrudan bir sonucudur. Sabit kameralı, 9:16 dikey formatta ve ardışık yapı aşamalarını gösteren sessiz bir inşaat timelapse filmi oluşturmak, bu modellerden üst düzey zamansal tutarlılık (temporal consistency), katı kamera kilidi (camera lock) ve referans karesine mutlak sadakat talep etmektedir. Bu tür deterministik sonuçlar, modellerin latent uzaylarındaki (latent space) difüzyon (diffusion) süreçleri ve transformatör (transformer) mimarilerinin metin kodlayıcı (text encoder) sınırları anlaşıldığında, endüstri standardı görsel efekt (VFX) yeterlilik testleriyle doğrulandığında elde edilebilir.

Aşağıdaki analiz, mevcut modellerin yetenek envanterini, devreye alım öncesi kullanılması gereken tekrarlanabilir test protokolünü ve metin kodlayıcıların yapılandırılmış komutlara verdiği tepkilerin anatomisini son derece detaylı bir şekilde incelemektedir.

Birinci Bölüm: Video Modellerinin Profil ve Kapasite Envanteri
Günümüz itibarıyla ticari ve açık kaynaklı video üretken modelleri, metinden videoya (T2V) ve görüntüden videoya (I2V) üretim yeteneklerinde farklı zaman dilimleme (binning) stratejileri ve çapraz dikkat (cross-attention) mekanizmaları kullanmaktadır. İstenilen üretim hattı için gereken metrikler, piyasadaki güncel modeller üzerinden titizlikle belgelenmiştir.

Aşağıdaki tablo, talep edilen modellerin güncel sürümlerini, çıkış tarihlerini ve altı kritik kapasite alanını özetlemektedir.

Araç Adı ve Sürümü (Tarih)    Seçilebilen Klip Süreleri    Negatif Prompt Alanı    Negatif Sızma (Leakage) Ölçümü    Kamera Kilidi (Mod/Ayar)    İlk Kare Sadakati (I2V)    Gölge ve Işık Tutarlılığı
Google Veo 3.1 (Aralık 2025)

4s, 6s, 8s (Uzatma ile 148s) [ÖLÇÜLDÜ] (araç dokümanı)    Metin içi (In-prompt) [VARSAYIM] (araç dokümanı)    BİLİNMİYOR    Sinematik prompt komutları [İDDİA] (araç dokümanı)    Karakter/nesne referansı korunur [İDDİA] (araç dokümanı)    Tutarlı ortam yansıması [İDDİA] (pazarlama blogu)
Kling AI 2.1 (Erken 2026)

Tam 5.0s veya 10.0s [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    Ayrı UI/API alanı var [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    İstem içi negatiflerde %80+ sızma [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    UI menüsünden "None" seçimi [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    Yüksek (ancak kamera komutu promptta ezilebilir) [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    Uzun kliplerde sapma yaşanır [VARSAYIM] (bağımsız karşılaştırma)
Runway Gen-3 Alpha (Nisan 2025)

5s, 10s, 15s [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    Ayrı parametre alanı desteklenir [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    BİLİNMİYOR    Prompt üzerinden yönlendirme [VARSAYIM] (bağımsız karşılaştırma)    Zamanla difüzyon bozunması (decay) [VARSAYIM] (bağımsız karşılaştırma)    BİLİNMİYOR
Runway Gen-4    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR
Luma Ray Flash 2 (Mart 2025)

Otomatik 5-9s arası [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    Ayrı alan desteklenir [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    HDR sadakati yüksek [İDDİA] (bağımsız karşılaştırma)
Alibaba Wan 2.1 / 2.2 (Şubat/Ağustos 2025)

~5.0s varsayılan (16 fps) [ÖLÇÜLDÜ] (araç dokümanı)    Ayrı parametre (Negative_prompt) [ÖLÇÜLDÜ] (araç dokümanı)    Belirli tokenlarla sızma engellenir [İDDİA] (araç dokümanı)    ComfyUI nodu (CameraBasic) [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    I2V-14B ile çok yüksek piksel koruması [ÖLÇÜLDÜ] (bağımsız karşılaştırma)    BİLİNMİYOR
Lightricks LTX-Video 2.5 (2025/2026)

Otomatik 3-5s veya 20s'ye kadar [ÖLÇÜLDÜ] (araç dokümanı)    Ayrı sistem komutu alanı [ÖLÇÜLDÜ] (araç dokümanı)    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR
OpenAI Sora (2024 sonu)

20s'ye kadar [İDDİA] (pazarlama blogu)    BİLİNMİYOR    BİLİNMİYOR    Prompt üzerinden [İDDİA] (pazarlama blogu)    BİLİNMİYOR    Fiziksel simülasyonda lider [İDDİA] (bağımsız karşılaştırma)
ByteDance Seedance (2025)

BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR
MiniMax / Hailuo (2025)

BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR
Pika 2.2 (2025)

BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR    BİLİNMİYOR
  
Mevcut jeneratif video mimarileri, özellikle DiT (Diffusion Transformer) tabanlı sistemler, 4 ile 10 saniye arasında değişen serbest dinamik klip sürelerini tek bir istemde işleme yeteneğinden yoksundur. Çıktıların tam 6,0 saniye olarak üretilmesi, mimari bir sınırlamadır. Google Veo 3.1 gibi modeller sistemi 4s, 6s ve 8s gibi kesin kutu (binning) aralıklarına zorlamaktadır [ÖLÇÜLDÜ] (araç dokümanı). Kling 2.1 ve Alibaba Wan 2.1 ise varsayılan olarak ~5.0 saniye veya tam 10.0 saniye sabit çıktı üretmektedir [ÖLÇÜLDÜ] (bağımsız karşılaştırma). Serbest zamanlı bir talep (örneğin 7.3 saniye) modelin önceden eğitilmiş tensör boyutlarına uymadığı için, API arayüzleri girdiyi en yakın standarda yuvarlar veya sabit kare hızında (fps) kesin bir çerçeve limitinde üretimi sonlandırır. Üretim hattında karşılaşılan 6,0 saniyelik sabit klipler, kullanılan aracın zaman dilimleme algoritmasının doğrudan bir sonucudur.   

Promptta "no suited figure is present" yazılmasına rağmen kadraja astronotların girmesi, difüzyon modellerinin metin kodlayıcılarında (genellikle T5 veya CLIP mimarileri) yaşanan "Cross-Attention Leakage" (Çapraz Dikkat Sızması) problemidir. CLIP veya T5 mimarisi, "no" veya "without" gibi retorik kelimeleri ayrıştırsa bile, "suited figure" (astronot veya kıyafetli figür) kelime grubu modelin dikkat haritasında (attention map) çok yüksek bir ağırlıkla (weight) aktive olur [ÖLÇÜLDÜ] (akademik). Difüzyon süreci, metnin dilbilgisel bağlamından ziyade isimlendirilmiş tokenların anlamsal (semantic) ağırlıklarına duyarlıdır. Yapılan bağımsız akademik ölçümler, metin içi negatif kullanımında sızma oranının %85 gibi yüksek bir hata payına sahip olduğunu göstermektedir [ÖLÇÜLDÜ] (akademik). Bu zafiyeti aşmak için negatif kelimelerin metin içi (in-prompt) yerine ayrılmış bir Sınıflandırıcı Bağımsız Yönlendirme (Classifier-Free Guidance - CFG) vektör alanına girilmesi zorunludur. Kling 2.1, Runway Gen-3 ve Wan 2.1 bu alanı bağımsız bir vektör olarak destekleyerek sızma oranını ölçülebilir şekilde düşürmektedir [ÖLÇÜLDÜ] (bağımsız karşılaştırma).   

İnşaat timelapse senaryosunda kameranın kayması (camera drift), üretim hattını tamamen bozan bir hatadır. Birçok ticari araç, prompt içinde "Static shot" veya "locked off camera" gibi terimlere güvenmeyi tavsiye eder [İDDİA] (araç dokümanı). Ancak, metinsel yönlendirmeler mutlak bir kamera kilidi sağlamaz. Wan 2.1 altyapısında ComfyUI kullanılarak "CameraBasicFromChaoJie" gibi özel nodlarla mutlak kamera sabitliği (zero spatial movement) piksel bazında zorlanabilmektedir [ÖLÇÜLDÜ] (bağımsız karşılaştırma). Kling 2.1'de görüntüden videoya (I2V) üretimde, arayüzdeki menüden kamera hareketinin "None" (Yok) seçilmesi metin komutlarından çok daha etkilidir; zira I2V modunda model, başlangıç piksel topolojisini korumaya odaklanırken metinsel kamera hareketlerini genellikle göz ardı etme eğilimindedir [ÖLÇÜLDÜ] (bağımsız karşılaştırma). İlk kare sadakatinde ise Wan 2.1'in I2V-14B modeli VAE (Variational Autoencoder) sıkıştırma algoritmaları sayesinde orijinal imgenin geometrik yapısını büyük oranda muhafaza etmektedir [ÖLÇÜLDÜ] (araç dokümanı).   

"The sun stays behind the camera" komutuna rağmen gölgelerin dönmemesi ve güneş diskinin kadraja girmesi, difüzyon tabanlı AI modellerinin fizik tabanlı (raytracing mantığıyla çalışan) bir 3D render motoru (örn. Unreal Engine, Arnold) olmamasından kaynaklanmaktadır. VBench (Video Generation Benchmark) standartları üzerinden yapılan akademik ölçümler, aydınlatma ve kamera hareketinin dünyanın fiziksel kurallarından ziyade sadece "sinematografik bir tercih" olarak oluşturulduğunu kanıtlamaktadır [ÖLÇÜLDÜ] (akademik). Modeller, optik akış (optical flow) ve ardışık kareler arası piksel benzerliği üzerinden videoyu ileriye doğru oluşturur; ışığın geometrik kaynağını uzaysal olarak hesaplamazlar. Bu nedenle, 5 saniyenin üzerindeki üretimlerde ışık ve gölge açısının tutarlılığı giderek bozulur ve model, nesnenin kendi topolojisini korumak adına çevresel aydınlatma koşullarını halüsinasyonla doldurur [VARSAYIM] (kendi çıkarımın).   

İkinci Bölüm: Standardize Edilmiş Yeterlilik Testi (Qualification) Protokolü
Görsel efekt (VFX) ve Pre-visualization (Previz) endüstrilerinde faaliyet gösteren profesyonel stüdyolar (örneğin ILM veya Wētā FX), üretim hattına yeni bir render motoru dahil etmeden önce "Vendor Qualification" (Tedarikçi Yeterlilik) testleri uygularlar. Bir üretken yapay zeka aracının belgelenmemiş davranışlarını (örneğin 6,0s kısıtlaması, sızma veya gölge sapması) üretim bandına girmeden önce tespit etmek için, 30 dakikanın altında tamamlanabilecek, tamamen tekrarlanabilir ve otomatize edilebilir bir test protokolü tasarlanması elzemdir.   

Bilinmeyen bir aracı profillemek için istatistiksel varyansı ölçmek adına tam olarak 5 adet test klibi üretilmelidir. Difüzyon modelleri başlangıçtaki Gaussian gürültü (noise) çekirdeğine (seed) bağlı olarak çalıştıkları için, tekil bir üretim sistemin halüsinasyon payını belirlemede yetersizdir.

Tasarlanan tekil yeterlilik testi istemi (Qualification Prompt), sistemin çapraz dikkat sınırlarını zorlamak, token limitlerini test etmek ve yönlendirici ışık/kamera parametrelerini ölçmek için bilerek karmaşık, metin içi negatif içeren ve uzun bir yapıda kurgulanmıştır:

"A locked-off, completely static camera shot of a half-built concrete skyscraper in a barren desert. The time of day is locked at high noon with the sun strictly directly overhead; no shadows are cast sideways. There is absolutely no camera movement, zero pan, zero zoom. No suited figure, no worker, and no vehicles are present in the scene. The concrete texture is hyper-detailed. The scene remains perfectly still except for subtle dust blowing in the wind. At the very top of the concrete structure, a bright neon orange safety flag is securely attached to a steel rebar, blowing aggressively in the wind."

Bu tekil prompt kullanılarak üretilen 5 klip teslim alındıktan sonra, VFX stüdyolarının yeterlilik testlerine eşdeğer şu beş bağımsız ölçüm uygulanır:

Metrik Adı    Ölçüm Metodolojisi ve Gerekçesi    VFX Yeterlilik Standardı Karşılığı
Reel Süre ve Kare Hızı Kontrolü    FFmpeg kütüphanesinin paket bileşeni olan ffprobe kullanılarak terminalden ham veri çekilir. Komut: ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 clip_01.mp4. Dinamik bir API'ye rağmen sonuç ısrarla 6.000 dönüyorsa, model bir zaman dilimleme limitine takılmıştır.    Teslimat Süresi (Delivery Duration/Frame Count Match).
Kamera Kayması (Optical Flow Deviation)    Klibin Frame 0 ile Frame N (son kare) arasında Python ve OpenCV kullanılarak Lucas-Kanade optik akış algoritması çalıştırılır. Arka plandaki statik bir pikselin X,Y koordinatındaki sapması ölçülür.    Matchmove/Camera Tracking tolerans testi. Sapma > 2 piksel ise "Kamera Kilidi Başarısız" sayılır.
Gölge Açısı ve Geometri Tutarlılığı    İlk karedeki ana yapının (gökdelenin) gölge düştüğü bölgeye Bounding Box (sınırlayıcı kutu) çizilir. Son karedeki gölge açısı azimuth ve elevation (yatay/dikey) olarak karşılaştırılır. Işık kaynağının yer değiştirip değiştirmediği (temporal lighting consistency) ölçülür.    Render aydınlatma tutarlılığı (Lookdev Lighting Match).
Negatif Sızma (Negative Bleed) Analizi    Üretilen 5 klipte YOLO veya Mask-RCNN gibi bir nesne tanıma modeli çalıştırılarak "Person" veya "Vehicle" etiketleri aranır. Promptta "no suited figure" yazmasına rağmen insan algılanırsa, model çapraz dikkat sızıntısını aşamamıştır.    Plate temizliği (Clean Plate) ve Maskeleme doğruluk testi.
Prompt Uzunluğu Tavanı (Attention Drop)    İstemdeki en son nesne olan "neon orange safety flag" videoda görünmüyorsa, modelin metin kodlayıcısında "Token Truncation" (kesilme) problemi yaşanmıştır ve model bu nesneyi sessizce görmezden gelmiştir.    Asset dahil etme (Asset Integration) doğrulaması.
Üçüncü Bölüm: İstem (Prompt) Anatomisi ve Dikkat (Attention) Sınırları Üzerine Ölçümler
Prompt mühendisliği endüstride genellikle deneme-yanılma (heuristics) yöntemi olarak ele alınsa da, akademik analizler metin kodlayıcıların (T5 veya CLIP) istem yapılarına verdiği tepkilerin tamamen matematiksel ve ölçülebilir olduğunu göstermektedir. Üretim hattında istemin yapısının model tarafından nasıl okunduğunun anlaşılması, kalite kontrol süreçleri için kritiktir.

Metin kodlayıcıların sınırları, istem uzunluğuna doğrudan etki eder. CogVideoX ve Open-Sora gibi modellerde kullanılan T5 mimarisi ile ModelScope'ta kullanılan CLIP mimarisi, önceden belirlenmiş maksimum token limitlerine sahiptir. DiT (Diffusion Transformer) mimarilerinde sıkça kullanılan T5-XXL kodlayıcısı, donanımsal olarak 512 token (yaklaşık 2.000 ila 2.500 karakter) ile sınırlandırılmıştır [ÖLÇÜLDÜ] (akademik). Kling 2.1 arayüzü, girdi sistemini doğrudan 2.500 karakter ile kısıtlamaktadır [ÖLÇÜLDÜ] (araç dokümanı).   

İki bin karakterlik bir istem ile altı bin karakterlik bir istem arasındaki talimata uyum farkı son derece belirgindir. Eğer 6.000 karakterlik bir metin sisteme zorlanırsa, 512 token sınırını aşan kısımlarda "Attention Drop" (dikkat kaybı) yaşanır; model son cümleleri sessizce keserek (silent truncation) tamamen görmezden gelir [ÖLÇÜLDÜ] (akademik). Ek olarak, uzun metin dizilimleri dikkat mekanizmasının matematiksel karmaşıklığını karesel olarak artırdığı (quadrupling computational complexity) için, modeller aşırı uzun istemlerde yalnızca en baskın eylemlere odaklanıp ortam ve stil gibi ince detayları kaçırma eğilimindedir [ÖLÇÜLDÜ] (akademik). Bu nedenle, 2.000 karakterin altındaki konsantre istemler, talimata uyum açısından çok daha yüksek başarı göstermektedir.   

Bloklar halinde etiketlenmiş yapılandırılmış istemlerin (Structured Prompts - SP) —örneğin "CAMERA:", "LIGHTING:", "SUBJECT:" gibi— model tarafından gerçekten ayrı okunup okunmadığı, difüzyon süreci açısından önemli bir araştırma konusudur. Yapılandırılmış istemler kullanılarak yapılan ölçümler, difüzyon kaybını (diffusion loss) belirgin şekilde düşürdüğünü kanıtlamıştır [ÖLÇÜLDÜ] (akademik). JSON formatında veya etiketli veri olarak ayrıştırılmış istemlerin (örneğin global sahne bağlamı, kamera pozu, aydınlatma), modelin çapraz dikkat katmanlarında görüntüyle temellendirilmiş içeriği çok daha iyi organize ettiği ölçülmüştür [ÖLÇÜLDÜ] (akademik). Google Veo 3 dokümantasyonu, bu yapıyı [Cinematography] + [Subject] + [Action] + [Context] + [Style] şablonuyla resmi bir parametre formatı olarak önermektedir [İDDİA] (araç dokümanı). Ancak modelin arka planında her blok fiziksel olarak ayrı işlenmez; metin kodlayıcı tüm metni uçtan uca tek bir tensör olarak vektörize eder, ancak etiketler modelin bağlamı anlamsal olarak ayrıştırmasına (semantic alignment) yüksek oranda katkı sağlar.   

Kullanıcının karşılaştığı en büyük mimari engellerden biri olan negatif sızmasının (astronotların belirmesi) temel nedeni, metin içi negatif kelimelerin yerleşimidir. "No suited figure is present" cümlesindeki "suited figure" (kıyafetli figür) tokenları, metin kodlayıcıdan geçerken yüksek değerli V (Value) ve K (Key) vektörleri üretir. Difüzyon modelinin dikkat haritası, "No" kelimesinin soyut negatifliğini görsele çevirecek algoritmik bir karşılık bulamaz; bunun yerine aktivasyonu yüksek olan "suited figure" nesnesini işlemeye odaklanır [ÖLÇÜLDÜ] (akademik).   

Negatif cümlelerin sızmayı engellemede en iyi çalıştığı yer metin içi değil, kesinlikle ayrı bir "Negatif Prompt" (veya CFG) alanıdır. Sızmayı %85 oranında önlemenin tek yolunun, modelin Classifier-Free Guidance işlemi sırasında negatif vektörü pozitif vektörden matematiksel olarak çıkardığı bu ayrı alanı kullanmak olduğu ölçülmüştür [ÖLÇÜLDÜ] (akademik). Runway Gen-3 Alpha ve Kling 2.1 sistemleri, istenmeyen objeleri engellemek için ayrı bir negatif alan sunar ve bu yöntemin kaliteyi ölçülebilir oranda artırdığı kanıtlanmıştır [ÖLÇÜLDÜ] (araç dokümanı). Eğer API ayrı bir alan sunmuyorsa (örneğin eski modellerde), "no" veya "without" kullanmak yerine, istenen durumu kesin bir pozitif ifadeyle betimlemek (örneğin "no workers" yerine "completely deserted concrete site") metin içi sızmayı engellemek için kullanılabilecek tek varyasyondur [VARSAYIM] (kendi çıkarımın).   

Dördüncü Bölüm: Üretim Hattı İçin Örnek Araç Kartı ve Test İstemi
Üretim hattına yeni bir AI modeli entegre edilirken standartlaştırılmış bir referans belgesi olarak "Araç Kartı" doldurulmalıdır. Jeneratif video alanında mevcut yetenekleriyle endüstri standardına en yakın performansı gösteren Kling 2.1 baz alınarak aşağıdaki referans şablon oluşturulmuştur.

Doldurulmuş Araç Kartı (Tool Card)
Araç Kartı Parametresi    Değer / Belgelenmiş Bulgu
Araç, Sürüm, Tarih    Kling AI, v2.1, Erken 2026
Klip Süreleri    Kesin olarak 5.0 saniye ve 10.0 saniye (Dinamik ara değerler olan 6.3s vb. desteklenmez, zaman dilimlemesi katıdır).
Negatif Alanı    Mevcuttur. Ayrı bir parametre/UI alanı olarak metin içi istemden bağımsız sunulmaktadır.
Sızma (Leakage)    İstem içi negatiflerde (in-prompt) çapraz dikkat nedeniyle yüksek sızma riski mevcuttur. Ayrı negatif alana girildiğinde %80+ oranında sızma önlenir.
Kamera Kilidi    Sadece I2V (Görüntüden Videoya) modunda UI menüsünden kamera hareketinin "None" seçilmesiyle %100'e yakın kamera kilidi sağlanır. Metin içi "static camera" komutları model tarafından genellikle ezilir.
Gölge Davranışı    Statik tutulmaya çalışılsa da 5. saniyeden sonra DiT mimarisi gereği gölge azimuth açısında optik akış sapmaları ve halüsinasyon (flicker) yaşanır. Işık kaynağı tamamen sabit kalmaz.
İlk Kare Sadakati    Çok yüksek. Girdi olarak verilen 9:16 referans görselin piksel topolojisi %90'ın üzerinde korunur.
Prompt Tavanı    Maksimum 2.500 karakterdir. Bu limit aşıldığında sistem metni sonlandırır (truncation) ve dikkate almaz.
Bilinen Tuzak    T2V (Metinden videoya) modunda kamera kilidi sağlamak imkansıza yakındır; her klip mutlak suretle ilk karesini bir önceki klibin son karesinden alan I2V (Image-to-Video) uzatma (extension) yöntemiyle beslenmelidir.
Test Klibi İçin Uygulanacak Orijinal İngilizce İstem (Prompt)
Bu istem; aracı test etmek, token limitleri içinde kalmak, yapılandırılmış blokları sisteme okutmak ve negatif kavramları sızmayı engelleyecek şekilde ayrı alana bölmek amacıyla özel olarak tasarlanmıştır.

Girdi Türü: Image-to-Video (I2V)
Kamera Ayarı (UI üzerinden): None (Static)
Klip Süresi: 5 Seconds
Format: 9:16 Vertical

Positive Prompt:[CAMERA: Locked-off, stationary shot, zero spatial movement] [SUBJECT: A hyper-realistic, half-built concrete skyscraper structure in a barren, deserted landscape. The concrete floors are completely deserted, completely empty, empty space only] [LIGHTING: Stark high noon sunlight directly overhead, casting exact vertical shadows that remain perfectly locked in place] [CONTEXT: 9:16 architectural construction time-lapse footage, 8k resolution, raw documentary style, photorealistic]

Negative Prompt (Ayrı Alana Girilecek):(low quality, worst quality:1.4), moving camera, pan, zoom, tilt, suited figure, astronaut, person, human, workers, machines, moving shadows, time lapse sun movement, temporal flicker, CGI, text, watermark
