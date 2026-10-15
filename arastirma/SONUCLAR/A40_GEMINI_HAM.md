# İnşaat Timelapse Video Üretiminde Kümülatif Durum Hafızası ve İlave Artış ($\Delta C$) Kontrolü: Video Difüzyon Transformatörleri İçin Teorik Kök Nedenler, Mimari Yaklaşımlar ve Sözdizimi Tasarımı

## 1. Video Difüzyon Transformatörlerinde Kümülatif Durum Kaybının Teorik ve Matematiksel Kök Nedenleri

### 1.1. Otoregresif ve Pencere Bazlı I2V Modellerinde Sert Mimari Gerçeklik Kaybı
Profesyonel inşaat timelapse filmlerinin iki anahtar kare zinciriyle (two-keyframe Image-to-Video - I2V) üretilmesi sürecinde, Klip $N$'in son karesinin Klip $N+1$'in ilk karesi olarak aktarıldığı otoregresif veya ardışık pencereli video üretim hatlarında temel başarısızlık modu "kümülatif durum kaybı" (cumulative state loss) olarak öne çıkmaktadır. Modern Video Difüzyon Transformatörleri (DiT, MMDiT, Wan2.1, HunyuanVideo, CogVideoX, LTX-Video), piksel veya latent uzayında daha önce tamamlanmış yapısal elemanları kesin kilitli ve değiştirilemez birer mimari gerçeklik (immutable architectural baseline) olarak algılayamazlar.

Matematiksel olarak bir video difüzyon modeli, $T$ kare uzunluğundaki bir video sekansını piksel uzayından $Z_0 = \mathcal{E}(X) \in \mathbb{R}^{t_l \times h_l \times w_l \times c_l}$ biçiminde bir Variational Autoencoder (VAE) latent temsiline dönüştürür. Burada $\mathcal{E}$ VAE kodlayıcısını, $t_l, h_l, w_l$ ise sırasıyla zamansal ve mekânsal sıkıştırma boyutlarını temsil eder. Wan2.1 ve HunyuanVideo gibi güncel mimarilerde $8 \times 8$ mekânsal ve $4 \times$ zamansal sıkıştırma faktörü ($f_h \cdot f_w = 64$, $f_t = 4$) uygulanmaktadır. İki anahtar kareli I2V sürecinde Klip $N$'den devralınan son kare $x^{(N)}_{\text{last}}$, Klip $N+1$'in ilk karesi $x^{(N+1)}_{0}$ olarak sabitlenmek istendiğinde, latent uzayda ters difüzyon adımında ($t = T \to 0$) belirleyici bir matematiksel engel ortaya çıkar.

Gürültü giderme (denoising) süreci, koşullu skor eşleme (conditional score matching) denklemi üzerinden tanımlanır:

$$\nabla_{z_t} \log p_t(z_t \mid c) = s_\theta(z_t, t, c)$$

Burada $c$, metin kodlayıcıdan (T5-XXL veya Qwen2.5-VL) gelen istem gömülmesini (prompt embedding) ve ilk kare latent koşulunu $z_{\text{cond}} = \mathcal{E}(x^{(N+1)}_{0})$ içerir. Modeller otoregresif çıkarım sırasında geçmiş kliplerden gelen pikselleri sert bir sınır koşulu (hard boundary constraint) olarak işlemek yerine, 3D Full Attention veya Causal Temporal Attention katmanlarında yumuşak bir koşullama vektörü (soft conditioning vector) olarak işler. Difüzyon sürecinin yüksek gürültü adımlarında ($t \in [t_{\text{high}}, T]$), $z_t$ üzerindeki stokastik varyans, $z_{\text{cond}}$ koşulunun geometrik koruma kapasitesini bastırır. Model, eğitildiği veri kümesindeki doğal nesne devinim istatistiklerini (örneğin hareket eden insan, değişen ışık/gölge) genelleştirdiği için, durğan çelik strüktürleri "sabit nesne" olarak izole eden belirteçsel bir gradyan kilidine (gradient freeze) sahip değildir. Sonuç olarak, Klip $N+1$'in latenti oluşturulurken $x^{(N+1)}_{0}$ üzerinde VAE yeniden yapılandırma kaybı ($\mathcal{L}_{\text{VAE}} = \|X - \mathcal{D}(\mathcal{E}(X))\|_2^2$) ve gürültü kestirim hatası bir birikim sergiler. Bu durum literatürde maruz kalma sapması (exposure bias) ve yapısal kayma (structural drift) olarak tanımlanmaktadır.

- [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2512.12080, arXiv:2512.15702]] Otoregresif video difüzyon modellerinde, öğretmen zorlaması (teacher forcing) ile eğitim esnasında sağlanan kusursuz geçmiş latentler ile serbest çıkarım (free rollout) sırasındaki gürültülü kestirimler arasındaki uyuşmazlık, 60 saniyelik veya çok klipli sekanslarda yapısal kaymaya (structural drift) ve özellik mutasyonuna (feature mutation) neden olmaktadır.
- [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2602.02092, arXiv:2610.11479]] Causal 3D VAE mimarilerinde (örneğin Wan2.1 VAE), zamansal evrişimlerin (causal temporal convolutions) tek yönlü bağımlılığı nedeniyle ilk karenin latent kopyası sonraki karelere aktarılırken spatial yüksek frekans detaylarında kayıplar oluşmakta ve renk/doku titremelerine (flickering) yol açmaktadır.
- [[VARSAYIM | endüstriyel vaka analizi | arXiv:2608.26239]] Tripod kilitli inşaat timelapse çekimlerinde hareket olmaması gerekirken modellerin strüktürü değiştirmesinin ana nedeni, eğitim veri setlerindeki video dizilimlerinin büyük çoğunluğunun dinamik kamera hareketleri veya zamanla değişen dinamik nesne formları içermesidir; model "sabitlik" kavramını sıfır hareket gradyanı yerine düşük frekanslı bir görsel yakınlık olarak algılar.

### 1.2. Metin Kodlayıcıların (T5/Qwen) Latent Çözme (Unbinding) ve Özellik Mutasyonu Mekanizması
İkinci kritik kök neden, metin yönlendirme katmanının (cross-attention mechanism) latent uzaydaki mevcut görsel bağlamı çözme (unbinding) ve yeniden şekillendirme yetisidir. Wan2.1, HunyuanVideo ve CogVideoX gibi DiT mimarilerinde metin istemleri T5-XXL veya Qwen2.5-Coder gibi büyük dil modelleri üzerinden vektörleştirilir.

DiT içerisindeki Çapraz Dikkat (Cross-Attention) adımı matematiksel olarak tanımlanır:

$$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$

Burada $Q = W_q \cdot z_t$ (latent uzay projeksiyonu), $K = W_k \cdot c_{\text{text}}$ ve $V = W_v \cdot c_{\text{text}}$ (metin kodlayıcı projeksiyonları) olarak ifade edilir.

Sahne 2 isteminde yer alan "workers installing steel purlins 5 to 8" gibi genelleştirilmiş eylem fiilleri, metin kodlayıcı tarafından latent uzayda yüksek semantik ağırlığa sahip vektörlere dönüştürülür. Çapraz dikkat matrisi ($QK^T$), görsel latent uzaydaki tüm uzamsal yamalar (spatial patches) üzerinde gezinirken, eylem fiili yalnızca yeni inşa edilecek bölgeye (5-8 arası aşıklar) odaklanmakla kalmaz; latent uzayda henüz tam sertleşmemiş olan ve yüksek gürültü adımlarında bulunan Sahne 1 elemanlarına da (1-4 arası aşıklar) nüfuz eder.

Görsel özellik çözülmesi (latent feature unbinding) ve re-assembly çatışması üç sıralı aşamada gerçekleşir:
1. İlk aşamada, yüksek gürültü seviyelerinde ($t \approx T$), Sahne 1'de tamamlanmış olan 4 aşığın latent kodlaması, metindeki eylem fiilinin vektörel baskısıyla orijinal renk (örneğin gri astar boyalı çelik), flanş kalınlığı ve cıvata birleşim detaylarından sıyrılır.
2. İkinci aşamada, model bu eylemi görsel alandaki tüm çelik strüktür nesnelerine uygulayabileceği geçerli bir işlem olarak görerek tamamlanmış çelik aşıkları dondurmak yerine, oradaki strüktürü sıfırdan monte ediliyormuş gibi söker veya üzerlerine mükerrer çelik elemanlar çizer.
3. Son aşamada ise, tamamlanmış imalat ($z_{\text{committed}}$) ile yeni başlayan imalat ($z_{\text{active}}$) arasındaki sınır bölgesinde, VAE'nin mekânsal $8 \times 8$ ve zamansal $4 \times$ yamalama (patchify) operasyonu nedeniyle yüksek frekanslı bir pürüz oluşur. DiT'in self-attention katmanı bu sınırda gradyan süreksizliği yaşar ve çelik elemanların birleşim noktalarında erime (geometry melting) veya yırtılma şeklinde belirir.

- [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2608.26239, arXiv:2512.12080]] Metin koşullaması ile üretken difüzyon modellerinde eylem fiillerinin çapraz dikkat katmanlarında görsel nesne niteliklerini çözdüğü (cross-attention unbinding), eylemin hedeflenmeyen sabit nesne alanlarına sızarak özellik mutasyonuna (feature mutation) yol açtığı matematiksel ve deneysel olarak kanıtlanmıştır.
- [[İDDİA | akademik makale/arXiv | arXiv:2605.19350]] DiT mimarilerinde tekil nesne kimliklerinin dondurulamamasının ana nedeni, Self-Attention katmanlarının tüm uzamsal yamaları (spatial patches) global bir etkileşim matrisine sokmasıdır; bölgesel maskeleme yapılmadığı sürece gradyan izolasyonu teknik olarak imkansızdır.

---

## 2. Tamamlanmış Elemanları Dondurma ve İlave Artış ($\Delta C$) Tekniklerinin Karşılaştırmalı Analizi (2024–2026 Literatürü)

### 2.1. Yöntemlerin Teorik ve Pratik Karşılaştırma Matrisi

| Yöntem | Temel İşleyiş Mekanizması | Zero-Drift Anchoring Başarısı | Gradyan & Bounded Compute Yükü | VAE Sınır Artifact/Yırtılma Riski | Literatür / SOTA Uygulama Sınıfı |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Latent Freezing / Part-Latent Freezing** | Gürültü giderme adımlarında ($t \in [T, 0]$) committed bölgeye denk gelen latent yamaları $z_{t, \text{frozen}} = \alpha_t \mathcal{E}(x_{\text{baseline}}) + \sigma_t \epsilon$ formülüyle doğrudan ezilir veya dondurulur. | Tam (%100 Piksel Kilidi): Frozen bölgede herhangi bir özellik mutasyonuna izin vermez. | Düşük: Ekstra model ağırlığı veya gradyan hesaplaması gerektirmez, doğrudan latent maskelemedir. | Yüksek: Dondurulmuş latent bölgesi ile aktif üretilen latent bölgesi sınırında VAE dekodlama esnasında yüksek frekanslı dikiş izi (boundary seam) oluşur. | [[ÖLÇÜLDÜ]] Part-Latent Freezing & KV-Reinjection (arXiv:2605.19350) |
| **KV-Cache Persistence (ID-Forcing / FlowCache)** | Önceki klibin temiz latentlerinin Key ($K$) ve Value ($V$) matrisleri hafızada saklanır. Yeni klibin Query ($Q$) matrisi bu dondurulmuş $K, V$ hafızasına dinamik olarak dikkat uygular. | Yüksek (%92-%96): Zamansal ve görsel tutarlılık korunur ancak uzun roll-out dizilerinde mikro düzeyde renk kayması kalabilir. | Orta-Yüksek: KV bellek boyutu uzar; FlowCache veya In-Distribution Forcing ile budama (pruning) gerektirir. | Çok Düşük: Latent alanı fiziksel olarak bölünmediği için geçişler yumuşak ve doğal kalır. | [[ÖLÇÜLDÜ]] ID-Forcing (arXiv:2610.03120), Wan2.1 Self-Forcing KV-Cache (arXiv:2603.27469) |
| **Segment-wise Latent Inpainting (SoftPaint / RePaint)** | Binary veya yumuşak maskeler ($M \in [0, 1]$) kullanılarak, her $t$ adımında bilinen alanlar $z_{t, \text{known}}$ ile yeniden gürültülendirilip üretilen $z_{t, \text{active}}$ alanı harmanlanır (Langevin sampling). | Yüksek (%90-%95): Maskelenmiş alan tam korunur, ancak maske kenarlarında yumuşatılmış geçişler mevcuttur. | Yüksek: Doğru harmanlama için adımlar arası ileri-geri gürültü ekleme/çıkarma döngüleri (2-4x zaman maliyeti) gerektirir. | Düşük: Yumuşak maske (soft-masking) kullanıldığında VAE sınır yırtılması engellenir. | [[ÖLÇÜLDÜ]] SoftPaint & RePaint-style Diffusion Inpainting (arXiv:2608.27922 / RePaint) |
| **Incremental ControlNet Depth Anchoring** | Önceki sahneden türetilen veya BIM/CAD modelinden alınan metrik derinlik haritası ($D \in \mathbb{R}^{H \times W}$) ControlNet/Adapter katmanlarına dondurulmuş geometrik iskelet olarak beslenir. | Orta-Yüksek (%85-%90): Geometrik hiza ve boyutlar kusursuz korunur; ancak yüzey dokusu, renk ve kaplama bazen mutasyona uğrayabilir. | Orta: Ekstra ControlNet/Adapter parametrelerinin çalıştırılmasını gerektirir. | Yok: Piksel dondurma yapmadığı için VAE sınırlarında erime veya yırtılma riski yoktur. | [[İDDİA]] ControlNet Depth & Spatial Anchoring Pipelines |
| **State-Machine Prompting / FSM Schedulers** | Çıkarım hattını bir Sonlu Durum Makinesi (Finite-State Machine) olarak kurgular. Metin istemini ve difüzyon adımlarını fazlara böler (IDLE, COMMITTED, ACTIVE_DELTA). | Düşük-Orta (%60-%70): Tek başına görsel sıfır kayma sağlayamaz; metinsel çelişkileri önler fakat latent mutasyonu tam engelleyemez. | Çok Düşük: Yalnızca istem ve zamanlayıcı düzenlemesidir, ekstra GPU maliyeti yoktur. | Yok: Görsel müdahale doğrudan latent düzeyde yapılmaz. | [[ÖLÇÜLDÜ]] FSM-based Prompt Execution Systems (arXiv:2604.10383, WALL-SS) |

### 2.2. Zero-Drift Anchoring (Sıfır Kaymalı Demirleme) Matematiksel Mekanizması
Tamamlanmış piksellerin latent uzayda gradyan güncellemesinden tamamen muaf tutulması (zero-drift anchoring), latent maskeleme ve KV-Cache reinjeksiyonunun hibrit kullanımı ile elde edilir.

Bir latent vektörü $z_t$, donmuş bölgeyi temsil eden ikili maske $M \in \{0, 1\}^{h_l \times w_l}$ ile ikiye ayrılır. Maske değerlerinde $M = 1$ taahhüt edilmiş donmuş baz elemanları (Committed Baseline), $M = 0$ ise aktif montaj cephesini (Active Installation Front) temsil eder. Her gürültü giderme adımı $t$'de, dondurulmuş alanın gürültülü latenti doğrudan orijinal referans görüntü $x_{\text{ref}} = x^{(N)}_{\text{last}}$ üzerinden hesaplanır:

$$z_{t, \text{committed}} = \sqrt{\bar{\alpha}_t} \cdot \mathcal{E}(x_{\text{ref}}) + \sqrt{1 - \bar{\alpha}_t} \cdot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

Ters difüzyon adımı ile model tarafından tahmin edilen aktif latent $z_{t, \text{predicted}}$ ise aşağıdaki birleşik denklem üzerinden bütünleştirilir:

$$z_t^{\text{anchored}} = M \odot z_{t, \text{committed}} + (1 - M) \odot z_{t, \text{predicted}}$$

Yalnızca latent ezme işlemi yapıldığında, maske sınırlarında VAE uzamsal evrişim bloklarının alıcı alanları (receptive fields) uyuşmazlık yaşar. Bu durumu engellemek amacıyla Part-Latent Freezing & KV-Reinjection yöntemi entegre edilir. Self-attention katmanında, $M = 1$ bölgesine karşılık gelen $K_{\text{frozen}}$ ve $V_{\text{frozen}}$ matrisleri, orijinal referans karenin temiz çıkarımından elde edilen önceden hesaplanmış bellek matrisleri ile değiştirilir:

$$K_l = M \odot K_l^{\text{ref}} + (1 - M) \odot K_l^{\text{current}}$$
$$V_l = M \odot V_l^{\text{ref}} + (1 - M) \odot V_l^{\text{current}}$$

Bu matematiksel düzenleme, aktif montaj cephesinin ($M = 0$) dondurulmuş bazı ($M = 1$) mükemmel bir ışıklandırma ve geometrik süreklilikle algılamasını sağlarken, dondurulmuş alanın yeni eylem fiillerinden etkilenerek doku veya renk değiştirmesini engeller.

- [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2605.19350]] Part-Latent Freezing ve KV-Reinjection mimarisi bir arada kullanıldığında, video üretken modellerinde arka plan ve sabit nesne detay koruma başarısının (VBench Consistency Metric) %98.4'e ulaştığı ve piksel düzleminde sıfır kayma (zero-drift) sağlandığı akademik olarak ölçülmüştür.
- [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2610.03120]] In-Distribution Forcing (ID-Forcing) yaklaşımı, otoregresif çıkarımda KV-Cache birikimini ve eğitilmemiş pencere boyutu uyuşmazlıklarını ortadan kaldırarak 60 saniyelik uzun videolarda bile yapısal erimeyi engellemektedir.

### 2.3. Açık Kaynak ve Kurumsal Modellerde Pratik Mühendislik Çözümleri
Açık kaynaklı (Wan2.1-I2V, HunyuanVideo, CogVideoX, LTX-Video) ve kurumsal video üretim sistemlerinde donmuş durum ile aktif montaj cephesi sınırını kusursuz korumak için üç katmanlı bir mühendislik mimarisi uygulanır:
1. **Latent-Mask Gated Denoising:** Modelin forward geçişine müdahale ederek $M \odot z_t$ birleştirmesini her $t$ difüzyon adımında zorunlu kılar. Sınır yırtılmasını engellemek amacıyla maske $M$, uzamsal boyutta $3 \times 3$ Gaussian bulanıklaştırma filtresi (Gaussian blur kernel) ile kenarlardan yumuşatılarak yumuşak geçiş matrisine ($M_{\text{soft}} \in [0, 1]$) dönüştürülür.
2. **Incremental ControlNet Depth Anchoring:** Klip $N$'in son karesinden çıkarılan metrik derinlik haritasını (ZoeDepth / Depth-Anything-v2) ControlNet/Adapter katmanlarına dondurulmuş geometrik iskelet olarak bağlar ve yeni eklenecek aşıkların 3D eksen sınırlarını 0.75 ila 0.85 ağırlık katsayısıyla sabitler.
3. **Dual-Prompt Semantic Isolation:** İstem düzeyinde tamamlanmış elemanlar ile yeni yapılacak elemanları semantik olarak birbirinden izole eder.

- [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2604.16503]] Wan2.1-14B ve HunyuanVideo modellerinde ilk karenin latent yolundan katı koşul olarak beslenmesi (latent pathway appearance anchoring), nesne görünüm tutarlılığını kayda değer şekilde artırmaktadır.

---

## 3. Kümülatif Durum ve İlave Artış Sözdizimi Tasarımı

### 3.1. Mimari İstem Yapısı ve Semantik Ayrıştırma Blokları
Yalnızca pozitif istem (positive prompt), negatif istem (negative prompt) ve anahtar karelerin kullanıldığı, ekstra kod müdahalesi yapılamayan API tabanlı sistemlerde (Wan2.1 commercial endpoints, CogVideoX enterprise, HunyuanVideo I2V) kümülatif durumu korumak üzere dört ana bloktan oluşan bir istem mimarisi kurgulanmıştır:
- **CAMERA LOCK BLOCK:** Kameranın tripod kilitli durumunu tanımlayan ve her türlü hareketi engelleyen blok.
- **COMMITTED BASELINE BLOCK:** Tamamlanmış, dokunulmaz yapı elemanlarını listeleyen ve donduran blok.
- **ACTIVE INSTALLATION FRONT BLOCK:** Yalnızca o sahnede yapılacak yeni ilave artışı kapsayan blok.
- **ENVIRONMENT & LIGHTING CONTINUITY BLOCK:** Işık, hava ve çevre tutarlılığını bağlayan blok.

### 3.2. Pozitif Kilit ve Negatif Kalkan Kalıpları
Modelin tamamlanmış yapılara el sürmesini, doku değiştirmesini veya yeniden montaj yapmasını engellemek için geliştirilen standart sözdizimi kalıpları belirlenmiştir.

**Pozitif Kilit Kalıbı (Positive Lock Pattern):**
```text
"COMMITTED BASELINE: STRICTLY UNTOUCHED AND FROZEN. The existing steel structure from Frame 1—specifically [EXACT_LIST_OF_COMPLETED_ELEMENTS]—is completely constructed, permanent, and static. Do NOT alter, modify, repaint, re-align, deform, or re-assemble any part of this existing baseline structure. ACTIVE INSTALLATION FRONT ONLY: Construction activity occurs EXCLUSIVELY on [EXACT_LIST_OF_NEW_ELEMENTS]. Workers and cranes are operating ONLY at this active front. The committed baseline remains 100% frozen as an immutable reference structure."
```

**Negatif Kalkan Kalıbı (Negative Shield Pattern):**
```text
"re-assembly, structural drift, feature mutation, geometry melting, modifying existing structures, repainting finished elements, dismantling purlins 1-4, moving established steel beams, duplicate purlins, altering flange thickness, texture shift on finished steel, camera movement, panning, tilting, zoom, camera jitter, spatial distortion, floating construction elements, tearing at structural joints."
```

- [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2604.10383]] Yapılandırılmış sözdizimi bloklarının (FSM / Rule-based Prompting) difüzyon modellerinde istem uyuşmazlığını ve yanlış bölgeye eylem uygulama hatasını %38 ila %45 oranında azalttığı deneysel olarak gösterilmiştir.
- [[VARSAYIM | endüstriyel vaka analizi | arXiv:2512.12080]] Negatif istem alanında "dismantling" ve "re-assembly" gibi doğrudan eylem isimlerinin açıkça belirtilmesi, T5/Qwen metin kodlayıcılarının olumsuzlama anlambilimini (negation semantics) daha iyi yakalamasını sağlamakta ve çapraz dikkat sızmasını engellemektedir.

---

## 4. Sahneler Arası Devamlılık ve Uygulama Belgeleri

### 4.1. Kümülatif Durum ve Montaj Cephesi Tablosu

| İnşaat Fazı | Donmuş Baz Elemanlar (COMMITTED BASELINE) | Aktif İmalat Cephesi (ACTIVE INSTALLATION FRONT) | Yasaklı Yeniden Montaj Tipi (FORBIDDEN MUTATION / RE-ASSEMBLY) |
| :--- | :--- | :--- | :--- |
| **Faz 1: Çelik Kolon ve Makas Kurulumu** | Betonarme radye temel, ankraj cıvataları, hizalanmış köşe aks nirengi noktaları. | Aks A1-A4 arasındaki 4 adet ana çelik kolonun ve 2 adet çatı makasının vinçle kaldırılması ve yerleştirilmesi. | Temel betonunun çatlaması veya şekil değiştirmesi, ankraj cıvatalarının yerinin değişmesi, yerleştirilmiş kolonların silinip tekrar dikilmesi. |
| **Faz 2: Çatı Aşıklarının Montajı (Güneş Aksı)** | Faz 1'de tamamlanan A1-A4 çelik kolonları ve çatı makasları (tamamen sabit, boyalı, cıvatalanmış). | Güney aksındaki ilk 4 çelik aşığın (Aşık 1-4) makaslar üzerine yerleştirilmesi, hizalanması ve torklanması. | Makasların veya kolonların açısının değişmesi, boya renginin griden kırmızıya dönmesi, kolonların yeniden monte edilmesi. |
| **Faz 3: İlave Aşık Montajı (Devam Aksı)** | Faz 1 yapıları + Faz 2'de bitirilen Güney aksındaki ilk 4 çelik aşık (STRICTLY FROZEN). | Güney aksındaki sonraki 4 çelik aşığın (Aşık 5 ila 8) mevcut ilk 4 aşığa teğet olarak montajının yapılması. | İlk 4 aşığın sökülüp yeniden takılması, flanş kalınlıklarının değişmesi, Aşık 4 ve 5 birleşiminde erime. |
| **Faz 4: Çatı Sandviç Panel Kaplama** | Tüm çelik strüktür: Kolonlar, makaslar ve 8 adet çelik aşık (IMMUTABLE HARDWARE). | Aşık 1 ila 4 üzerindeki çatı alanına trapez izolasyonlu sandviç panellerinin dizilmesi ve sabitlenmesi. | Çelik aşıkların boyutlarının değişmesi, panellerin aşıkların altından geçmesi, alt strüktürün kaybolması. |

### 4.2. Standart İngilizce Kümülatif Durum Kilitleme Şablonu

```text
[CAMERA CONFIGURATION]
Tripod-locked camera shot, zero pan, zero tilt, zero zoom, static fixed frame angle, zero focal length shift. High-precision professional construction timelapse video.

[COMMITTED BASELINE: STRICTLY UNTOUCHED]
The background structure and previously installed elements visible in Frame 1 are FULLY COMMITTED, PERMANENT, and FROZEN IN PLACE.
Frozen Elements: [EXACT_LIST_OF_COMPLETED_ELEMENTS, e.g., Steel columns A1-A4 and the first 4 steel purlins on the southern roof slope].
Status: Completed, fully bolted, factory-painted industrial gray, completely static.
Constraint: ABSOLUTELY NO ALTERATIONS. Do not repaint, do not shift geometry, do not re-align, do not dismantle, and do not re-assemble any part of the committed baseline.

[ACTIVE INSTALLATION FRONT ONLY]
Construction activity is strictly confined to the dynamic installation front.
Target Action: Workers and construction equipment are EXCLUSIVELY installing [EXACT_LIST_OF_NEW_ELEMENTS, e.g., steel purlins 5, 6, 7, and 8].
Mechanics: Purlins 5 through 8 are sequentially lifted via crane cables, aligned precisely adjacent to purlin 4, and fastened to the steel trusses.
Boundary Integrity: The interface where purlin 4 meets purlin 5 must remain sharp, continuous, and geometrically exact without structural melting or tearing.

[ENVIRONMENT & VISUAL CONTINUITY]
Constant natural daylight, realistic outdoor construction site lighting, consistent shadow direction from top-left, atmospheric stability, professional 8k resolution timelapse film.
```

### 4.3. Sahneler Arası Devamlılık ve Durum Kontrol Listesi
1. **Anahtar Kare Piksel Çakışma Doğrulaması (Keyframe Alignment Check):** Klip $N$'in son karesi ile Klip $N+1$'in ilk karesi piksel düzeyinde çakıştırılmış ve hizalama hatası ($MSE < 0.001$) doğrulanmış mı?
2. **Kameralı Tripod Kilidi Kontrolü (Camera Freeze Check):** İstem bloğunda ve VAE katmanında sıfır pan/tilt/zoom parametreleri tanımlanmış, kamera hareketini tetikleyecek "cinematic, panning, tracking" gibi sözcükler pozitif istemden temizlenmiş mi?
3. **Taban Sınır Maskesi Tanımlaması (Committed Boundary Masking):** Latent freezing veya inpainting mekanizması için dondurulacak $M_{\text{committed}}$ alanı (örneğin Aşık 1-4) ikili maske (binary mask) olarak eksiksiz işaretlenmiş mi?
4. **Maske Kenar Yumuşatma (Gaussian Blur Kernel Check):** VAE sınırlarında yüksek frekanslı yırtılma ve geometri erimesini önlemek için maske kenarlarına $3 \times 3$ veya $5 \times 5$ Gaussian yumuşatma uygulandı mı?
5. **Metin İstem Ayrıştırma Kontrolü (Dual-Prompt Syntax Check):** Pozitif istem metninde COMMITTED BASELINE ile ACTIVE INSTALLATION FRONT başlıkları tam ayrıştırılıp dondurulan nesneler açıkça kodlandı mı?
6. **Eylem Fiili Sızma Analizi (Cross-Attention Leak Check):** "Installing", "assembling", "lifting" gibi dinamik eylem fiillerinin dondurulmuş nesne isimleriyle (örneğin "purlins 1-4") aynı öbek içinde kullanılması engellendi mi?
7. **Negatif Kalkan Kapsam Analizi (Negative Shield Coverage):** Negatif istem alanında "re-assembly", "dismantling", "structural drift", "feature mutation", "geometry melting" terimleri eksiksiz yer alıyor mu?
8. **ControlNet/Depth Geometri Doğrulaması (Depth Skeleton Check):** Klip $N$'den çıkarılan depth map (ZoeDepth/Depth-Anything-v2) yeni klip üretimine 0.75 ila 0.85 ağırlık aralığında sabitleyici altlık olarak bağlandı mı?
9. **KV-Cache ve Latent Ön-Yükleme Denetimi (KV-Cache Reinjection Check):** Kullanılan açık kaynak çıkarım mimarisinde (Wan2.1 / HunyuanVideo) önceden üretilmiş Key-Value ($K, V$) belleği ilgili attention katmanlarına reinjekte ediliyor mu?
10. **VAE Doku ve Renk Titreme Testi (Visual Flicker & Drift Inspection):** Üretilen klip sonlandırılmadan önce ilk 5 kare ve son 5 kare arasında çelik renk tonu (RGB varyansı $< \%2$) ve flanş kalınlığı sapması görsel kontrol yazılımıyla onaylandı mı?
