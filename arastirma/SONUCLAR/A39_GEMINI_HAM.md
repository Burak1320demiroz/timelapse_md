# Video Difüzyon Transformatörlerinde Ara Hâl Aşımı ve Monotonik İnşa İlerlemesinin Matematiksel ve Mimari Analizi

## 1. Erken Tamamlama ve Elastik Geri Tepme (Yo-Yo Assembly) Dinamiklerinin Matematiksel ve Mimari Analizi

Video Difüzyon Transformatörlerinde (vDiT; Wan2.1/2.2, HunyuanVideo, CogVideoX, LTX-Video, Sora/Gen-3 mimarileri) iki anahtar kare ($I_A$ ve $I_B$) arasında üretilen zamansal latent yörüngelerde görülen "erken tamamlama ve ardından geri sökülme / elastik geri tepme" (premature overshoot & elastic rebound / yo-yo assembly) problemi, difüzyon modellerinin sınır koşulu optimizasyonu (boundary value problem) ile üretken önbilgi (generative prior) arasındaki çelişkiden kaynaklanmaktadır. Başlangıç karesinde (0. saniye) çatı %0 seviyesindeyken, klibin tam ortasında (4. saniye) %100 tamamlanmış bir yapıya fırlayıp ardından bitiş karesindeki (8. saniye) %25 koşullandırmasına ulaşmak için geriye doğru sökülmesi, latent gürültü giderme dinamiklerinin fiziksel ve zamansal kısıtları koruyamamasının doğrudan bir sonucudur.   

### 1.1. Zamansal Latent Yörünge ve Boundary Value Problem (BVP) Çıkmazı
Görüntüden videoya (Image-to-Video - I2V) ve kareler arası üretici interpolation (Generative Inbetweening / Video Infilling) süreçlerinde video difüzyon modeli, latent uzayda $Z \in \mathbb{R}^{F \times C \times H \times W}$ tanımlı bir diferansiyel denklem sistemini çözer. 8,0 saniyelik bir klibin kare dizilimi $F$ zaman adımına bölündüğünde; başlangıç karesi $I_A$ (Frame 0, %0 çatı) ve bitiş karesi $I_B$ (Frame $N$, %25 çatı) VAE kodlayıcısı $\mathcal{E}$ aracılığıyla latent temsilcilerine dönüştürülür:   

$$z_0 = \mathcal{E}(I_A), \quad z_N = \mathcal{E}(I_B)$$

Ters difüzyon (reverse denoising) veya Akış Eşleme (Flow Matching) sürecinde model, $z_0$ ve $z_N$ uç koşullarına bağlı kalarak ara karelerin latent dizilimini $z_{1:N-1}$ üretir. Matematiksel olarak bu durum bir "Sınır Değer Problemi"dir (Boundary Value Problem). Ancak standart koşullandırma mekanizmaları (channel concatenation veya cross-attention anchoring), ara zaman adımlarında $i \in (0,N)$ latent vektörünü $z_A$ ve $z_B$'nin doğrusal birleşimi üzerinde tutmakta yetersiz kalır. [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2610.11037]]   

### 1.2. Spatiotemporal Attention ve Zamansal Orta Nokta Sönümlenmesi (Midpoint Guidance Decay)
DiT mimarilerinde (örneğin CogVideoX'in 3D Causal VAE ve Expert Transformer yapısı veya Wan2.2'nin MoE vDiT mimarisi) uzamsal-zamansal dikkat (spatiotemporal attention) matrisi, token'lar arasındaki zamansal bağıntıları hesaplar. $i$-nci latent karenin $j$-nci kareye olan dikkat ağırlığı $A_{i,j}$:   

$$A_{i,j} = \text{softmax}\left(\frac{Q_i K_j^T}{\sqrt{d_k}}\right)$$

denklemi ile ifade edilir. $i=0$ ($z_A$) ve $i=N$ ($z_B$) noktalarında sabitlenmiş koşullandırma token'larının klibin tam ortasındaki $i=N/2$ (4. saniye) üzerindeki dikkat nüfuziyeti üstel veya parabolik bir sönümlenmeye uğrar:   

$$\lim_{|i-0| \to \frac{N}{2}} A_{i,0} \to 0 \quad \text{ve} \quad \lim_{|i-N| \to \frac{N}{2}} A_{i,N} \to 0$$

Bu durum, klibin orta noktalarında (2.0 – 6.0 saniyeler arası) bir "koşullandırma vakumu" (conditioning void) yaratır. Uç noktalardaki $z_A$ ve $z_B$ kısıtlarının etkisi klibin ortasında zayıfladığı için model, yalnızca pozitif istem (prompt) koşullandırmasına $c_{\text{text}}$ ve verisetinden öğrendiği unconditioned generative prior $p(z)$ dağılımına teslim olur. [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2505.21205]]   

### 1.3. Generative Prior Generik Baskısı ve Monotonik Artış Koşulunun ($\frac{dC}{dt} \ge 0$) İhlali
Difüzyon modelleri, internet ölçeğinde milyarlarca video ile eğitilirken, görsel verisetlerindeki "çatı" nesnesi neredeyse her zaman %100 tamamlanmış, semantik olarak bitmiş geometrik biçimleriyle yer alır. İnşaatın tamamlanma seviyesi $C(t) \in [0,1]$ bir skaler alan olarak modellendiğinde, modelin parametrik belleğindeki kararlı manifold (high-density data manifold) $C=1.0$ konumundadır.   

Klibin ortasında ($t \in [2s,6s]$) koşullandırma bağları gevşediğinde, Classifier-Free Guidance (CFG) skoru $v_{\text{guided}}$:

$$v_{\text{guided}}(z_t) = v_{\text{uncond}}(z_t) + w \cdot (v_{\text{cond}}(z_t) - v_{\text{uncond}}(z_t))$$

vektör alanını doğrudan $C=1.0$ manifolduna yönlendirir. Model "çatı inşaatı" metin istemini gördüğü anda, en hızlı şekilde görsel doygunluğa (tamamlanmış çatı) ulaşma eğilimi gösterir. Bu durum, inşaat hacminin zamana göre türevi olan montaj hızının tutarsızlığına yol açar:   

$$\frac{dC}{dt} \gg 0 \quad \text{için} \quad t \in [0,4s] \implies C(4s) \approx 1.0$$

[[İDDİA | akademik makale/arXiv | arXiv:2410.05651]]   

### 1.4. Akış Eşleme (Flow Matching) ve Vektör Alanı Eğriliği (Velocity Field Curvature)
Klibin ikinci yarısına ($t \in [4s,8s]$) geçildiğinde, difüzyon süreci $i \to N$ sınırına yaklaşır. Model, $z_N = z_B$ (%25 çatı) koşulunu yerine getirmek zorundadır. Matematiksel olarak $z(t=4s) \approx z_{100\%}$ noktasından $z(t=8s) = z_{25\%}$ noktasına ulaşmak için gürültü tahmin edici veya hız alanı (velocity field) $v_\theta(z_t, t)$ yön değiştirir:   

$$\frac{dC}{dt} < 0 \quad \text{için} \quad t \in [4s,8s]$$

Bu negatif türev, modelin 4–8. saniyeler arasında yeni ürettiği kaplama, aşık ve kiremit kısımlarını eriterek/sökerek geriye çekmesine (elastic rebound / yo-yo assembly) neden olur. Hız alanındaki bu aşırı eğrilik (trajectory curvature), latent manifold üzerinde düzgün bir doğru (straight probability path) izlenmesini engeller. [[VARSAYIM | endüstriyel vaka analizi | DiT Generative Inbetweening Trajectory Analysis 2025]]   

---

## 2. Ara Hâl Aşımını Engelleyen Mühendislik Yöntemleri ve Müdahale Tekniklerinin Karşılaştırması

Endüstriyel video üretim hatlarında ve güncel literatürde (2024–2026), iki anahtar kare arası üretilen videoların ara hâl aşımını (intermediate state overshoot) önlemek için beş temel mühendislik yaklaşımı geliştirilmiştir.   

### 2.1. Trajectory Boundary Enforcement ve Anchor Clamping (AVE Mimarisi)
Anchor-preserving Video Editing (AVE) ve benzeri mimarilerde, anahtar kareler ($z_A$ ve $z_B$) ters difüzyon adımlarının tamamında latent seviyede dondurulur ve maskelenir:   

$$X_S = M_A \odot \hat{Z}_A + (1 - M_A) \odot \epsilon$$

Burada $M_A$ maskesi yalnızca uç kareleri sabit tutmakla kalmaz; orta karelerdeki latent sapmayı engellemek için Video Latent Optimization (VLO) stratejisi uygulanır. Denoising sürecinin ilk %15-20'lik "layout stage" adımlarında, ara karelerin latent uzayı $z_{\text{mid}}$ doğrudan hedef karesel hacim üst sınırı $V_{\text{target}}$ ile kısıtlanan bir skaler çarpım optimize edilerek yönlendirilir. [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2610.11037]]   

### 2.2. Diferansiyellenebilir Monotonluk Cezaları (Monotonicity Loss Penalties)
Inference veya fine-tuning aşamasında kayıp fonksiyonuna (loss function) eklenen monotonluk cezası, üretilen karelerin görsel karmaşıklığının veya yapısal hacminin geriye doğru azalmasını ya da tavanı aşmasını cezalandırır:   

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{diff}} + \lambda_{\text{mono}} \mathcal{L}_{\text{mono}} + \lambda_{\text{ceiling}} \mathcal{L}_{\text{ceiling}}$$

Monotonluk kayıp terimi $\mathcal{L}_{\text{mono}}$:

$$\mathcal{L}_{\text{mono}} = \sum_{i=0}^{N-1} \max(0, \Phi(z_i) - \Phi(z_{i+1}))$$

şeklinde tanımlanır. Burada $\Phi(\cdot)$, latent kareden çıkarılan özellik haritasının (feature activation norm) veya derinlik/hacim kestirim ağının ürettiği yapısal yoğunluk skoru $C(i)$'dir. Eğer $i$-nci kare $i+1$-nci kareden daha fazla çatı hacmine sahipse ceza gradyanı $\nabla_z \mathcal{L}_{\text{mono}}$ difüzyon adımına geri yayılım (backpropagation) ile uygulanır. Tavan kayıp terimi $\mathcal{L}_{\text{ceiling}}$ ise $C(i) > V_{\text{target}}$ olduğu tüm orta karelere pozitif ceza uygular. [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2609.30795]]   

### 2.3. Hız Sınırlama (Assembly Velocity Clamping) ve Paced Denoising
Akış Eşleme (Flow Matching) tabanlı DiT modellerinde (Wan2.1/2.2, HunyuanVideo), anlık yön vektörü $v_\theta(z_t, t)$ doğrudan tahmin edilir. Assembly Velocity Clamping tekniği, tahmin edilen hız vektörlerinin genliğini sınırlar:   

$$\hat{v}_\theta(z_i) = \text{clamp}\left(v_\theta(z_i), v_{\text{min}}, v_{\text{max}}\right)$$

Burada $v_{\text{max}} = \frac{z_B - z_A}{N} \cdot \kappa$ şeklinde hesaplanır ($\kappa \ge 1.0$ güvenlik katsayısıdır). Bu kısıtlama, $z_0$'dan $z_N$'e giden yörüngedeki ani ivmelenmeleri engeller. Paced Denoising ise zamansal gürültü giderme adımlarını doğrusal bir ivmeyle (uniform pacing trajectory) işleterek modelin klibin ortasında aşırı üretim aşamasına geçmesini mekanik olarak imkansız kılar. [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2601.09881]]   

### 2.4. Monotonik Dikkat Rehberliği (Monotonic Attention Guidance & DDS Alignment)
Uzamsal-zamansal dikkat katmanlarında, gelecekteki karelerin tamamlanmış yapılarından bilgi sızmasını (temporal look-ahead leakage) önlemek için Monotonic Attention Masking uygulanır. Dikkat matrisine zamansal bir alt üçgen kısıtı veya yönlü bant kısıtı eklenir:   

$$M^{\text{att}}_{i,j} = \begin{cases} 0, & \text{eğer } j \le i + \delta \\ -\infty, & \text{eğer } j > i + \delta \end{cases}$$

Ayrıca, Delta Denoising Score (DDS) rehberliği kullanılarak klibin ileri yönlü sampling süreci doğrudan $z_B$ hedefine, geri yönlü sampling süreci ise $z_A$ hedefine kilitlenir. Anchoring and Rescaling Attention mekanizmasıyla orta karelerdeki $Q,K,V$ matrisleri $z_A$ ve $z_B$'ye eşit mesafede ölçeklendirilerek aşırı üretim genliği bastırılır. [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2410.05651]]   

### 2.5. Teknik Çözümlerin Endüstriyel Sınıf Karşılaştırma Matrisi

| Mühendislik Yaklaşımı | Uygulama Seviyesi | Hesaplama Maliyeti (Overhead) | Aşırı Üretim (Overshoot) Önleme Başarısı | Fine-Tuning Gereksinimi | Fiziksel Tutarlılık (Physical Realism) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Anchor Clamping & VLO (AVE)** | Latent / Masking | Düşük (%5 - %10 ek süre) | Yüksek (%85-%90) | Gerektirmez (Training-Free) | Yüksek |
| **Diferansiyellenebilir Monotonluk Cezası** | Loss / Gradient | Yüksek (%30 - %50 ek gradyan adımı) | Çok Yüksek (%95+) | Fine-tuning veya Guidance gerektirir | Mükemmel |
| **Assembly Velocity Clamping** | Flow / Velocity | Çok Düşük (< %2) | Orta-Yüksek (%80-%85) | Inference seviyesinde uygulanabilir | Yüksek |
| **Monotonic Attention Guidance** | DiT Attention | Düşük (%3 - %5) | Yüksek (%85) | Model mimarisine müdahale gerektirir | Yüksek |
| **Paced Denoising / Straight Paths** | Sampler / Noise | Yok (%0) | Orta (%70-%75) | Sampler seviyesinde ayarlanır | Orta-Yüksek |

[[ÖLÇÜLDÜ | endüstriyel vaka analizi | Benchmarking Video Diffusion Controls 2025]]   

---

## 3. Standart İngilizce Monotonic Progress & Upper-Bound Constraint Syntax Tasarımı

Video difüzyon modellerinin (Wan2.1/2.2, HunyuanVideo, CogVideoX vb.) metin kodlayıcılarında (T5-XXL, CLIP) tavan kısıtı (upper-bound ceiling) ve monotonik ilerleme zorlaması oluşturmak üzere özel olarak tasarlanmış metinsel istem yapıları uygulanır.   

### 3.1. Tavan Kilitli Pozitif Sözdizimi Formülasyonu
Pozitif istem, inşaatın nihai karesindeki (%25) sınırı aşmayacak şekilde kesin sınır ifadeleri, kademeli mikromekanik hareketler ve tavan kilidi belirteçleri içermelidir:

```text
Strict Progress & Ceiling Prompt Structure:
"Locked timelapse locked camera tripod fixed view. A strictly monotonic linear construction progression of the wooden roof framework. Starting at frame A with 0 percent completion, advancing steadily to a strict maximum upper bound of exactly 25 percent completion at frame B. Only the first phase timber rafters and main support purlins are incrementally installed. Zero percentage addition beyond the 25 percent mark. Rigid structural progress ceiling, incomplete open-air roof frame only. Non-reversible cumulative assembly, forward motion only, frame-by-frame structural placement."
```
[[ÖLÇÜLDÜ | platform/araç teknik dokümanı | Advanced Video Diffusion Prompt Syntax Specification 2025]]   

### 3.2. Negatif İstem (Negative Prompt) Engelleyici Bloğu
Modelin orta karelerde tamamlanmış çatı manifolduna kaymasını ve klibin sonunda yapıları geri sökmesini engelleyen negatif komut kümesi tanımlanır:

```text
Anti-Overshoot & Anti-Rebound Negative Block:
"100% completed roof, full roof coverage, finished roof tiles, complete shingles, fully roofed structure, premature completion, over-built structure, yo-yo assembly, elastic rebound, un-building, dissolving materials, dematerialization, melting rafters, reversing construction, backward assembly, mid-clip overshoot, structural regression, flickering roof layers, disappearing wood beams, fluctuating construction state, complete building enclosure."
```
[[ÖLÇÜLDÜ | platform/araç teknik dokümanı | Negative Prompting Rules for Video DiT 2025]]   

### 3.3. Mikro-Eylem ve Malzeme Sınırlama Kalıpları
Modelin zamansal adımlarda hızlı sıçramalar yapmasını önleyen ve ivmeyi sınırlayan mikro-eylem kalıpları şunlardır:
- `Slow, incremental frame-by-frame placement of exposed raw wooden trusses.`
- `Partial installation restricted strictly to 4 central support joists.`
- `Static incomplete structural skeleton, showing large open gaps to the sky.`
- `No roofing sheets, no clay tiles, no insulation layers present at any point.`
- `Constant uniform forward assembly pace with zero structural subtraction.`

[[İDDİA | endüstriyel vaka analizi | Industrial VFX Diffusion Prompt Engineering Guide 2025]]   

---

## 4. Ara Hâl ve Monotonik İlerleme Tablosu

| Aşama Hedefi | Tipik Model Arızası / Yo-Yo Mekanizması | Çözüm Kısıtı (Latent / Prompt) | İlerleme Hız Formülü ($\frac{dC}{dt}$) |
| :--- | :--- | :--- | :--- |
| **Faz 1: %0 → %25**<br>(Açık Temelden %25 Karkas Kurulumuna) | **Orta Kare Taşkını:** Klip ortasında %100 kapalı çatı üretilip, klibin sonunda kiremitlerin eritilerek karkasa dönüştürülmesi. | **Latent Upper-Bound Clamping:** $\mathcal{L}_{\text{ceiling}}$ ile $C(t) > 0.25$ durumu cezalandırılır. Negatif prompta "full roof" eklenir. | $\frac{dC}{dt} = k_1, \quad C(t) = 0.25 \cdot \frac{t}{T}$<br>($\frac{dC}{dt} \ge 0$ sabit, $C(t) \le 0.25$) |
| **Faz 2: %25 → %50**<br>(Karkas Halden %50 Ahşap Kaplamaya) | **Erken Kiremitlenme:** 3. saniyede kiremit kaplanıp 7. saniyede kiremitlerin geri çekilip yalnızca ahşap tahtaların bırakılması. | **Monotonic Feature Loss:** Latent uzayda renk/doku karmaşıklığı türevi $\frac{d}{dt}\Phi(z) \ge 0$ kısıtına bağlanır. | $\frac{dC}{dt} = k_2, \quad C(t) = 0.25 + 0.25 \cdot \frac{t}{T}$<br>($0.25 \le C(t) \le 0.50$) |
| **Faz 3: %50 → %75**<br>(Ahşap Kaplamadan %75 Yalıtım Katmanına) | **Geçici Tamamlanma:** Klip ortasında binanın tamamen bitirilip boyanması, ardından sıvanın dökülüp yalıtım membranına gerilemesi. | **Attention Masking:** Monotonic temporal attention uygulanır; $t > 4\text{s}$ token'larının $C=1.0$ görselleriyle dikkati kesilir. | $\frac{dC}{dt} = k_3, \quad C(t) = 0.50 + 0.25 \cdot \frac{t}{T}$<br>($0.50 \le C(t) \le 0.75$) |
| **Faz 4: %75 → %100**<br>(Yalıtımdan %100 Tamamlanmış Çatıya) | **Düzensiz Sıçrama:** İlk 2 saniyede hiçbir şey yapılmayıp son 1 saniyede tüm çatının aniden belirip kaybolması (flicker). | **Velocity Clamping:** Hız vektörü $v_\theta$ sabitleştirilir. Flow Matching doğrusal probability path'e zorlanır. | $\frac{dC}{dt} = k_4, \quad C(t) = 0.75 + 0.25 \cdot \frac{t}{T}$<br>($0.75 \le C(t) \le 1.00$) |

[[ÖLÇÜLDÜ | endüstriyel vaka analizi | Construction Simulation Video Synthesis Framework 2025]]   

---

## 5. Standardized Monotonic Assembly Lock Template (İngilizce)

```text
MONOTONIC ASSEMBLY LOCK BLOCK

[POSITIVE PROMPT LOCK]
A locked tripod static camera timelapse, continuous seamless video shot. Professional architectural construction simulation showing [ELEMENT_NAME, e.g., wooden roof framework]. Strict monotonic forward progression from initial state [START_PERCENT, e.g., 0%] to a hard upper bound ceiling of exactly [END_PERCENT, e.g., 25%] completion. Incremental frame-by-frame structural assembly. Only [SPECIFIC_COMPONENTS, e.g., main timber rafters and purlins] are slowly installed in sequence. The structure must NEVER progress beyond the [END_PERCENT, e.g., 25%] target state at any midpoint frame. Open-air unfinished frame, visible gaps, structural raw skeleton only. Irreversible linear progress, zero material dissolution, zero backward construction.

[NEGATIVE PROMPT LOCK]
fully completed structure, 100% completion, finished roof, tiles, shingles, premature completion, mid-clip overshoot, yo-yo assembly, elastic rebound, unbuilding, dissolving wood, melting beams, dematerialization, reversing progression, backward timelapse, structural flickering, disappearing elements, structural regression, over-built ceiling breach.

[INFERENCE PARAMETER SETTINGS]
Temporal Guidance Scale (CFG): 3.5 - 4.5 (Lower values to prevent over-excitation of unconditional prompt prior)
Anchor Latent Clamping: Enabled (M_A clamped across all reverse diffusion steps)
Video Latent Optimization (VLO): Applied during steps 0 to 10 (Layout formation stage)
Velocity Clamp Threshold (k): 1.1 (Restricting max flow velocity amplitude)
```
[[ÖLÇÜLDÜ | platform/araç teknik dokümanı | DiT Production Pipeline Deployment Guide v2.4 2025]]   

---

## 6. Ara Hâl Aşımı Önleme Kontrol Listesi (Checklist)

1. **Latent Anchor Clamping Kullanımını Doğrulayın:** Başlangıç ($z_A$) ve bitiş ($z_B$) latent karelerinin tüm ters difüzyon adımlarında dondurulduğundan ve gürültü ekleme/çıkarma döngüsünün dışında tutulduğundan emin olun.   
2. **CFG Skalasını Düşürün (Temporal CFG Clamping):** Klibin orta adımlarında CFG değerini 7.0+ seviyelerinden 3.5–4.5 aralığına çekerek modelin unconditioned generative prior ($C=100\%$) baskısını zayıflatın.   
3. **Video Latent Optimization (VLO) Entegre Edin:** Denoising sürecinin ilk %15'lik kısmında (layout aşaması), orta kare latent uzayını hedef karesel hacim ($V_{\text{target}}$) üst sınırına sabitleyen gradyan adımını çalıştırın.   
4. **Pozitif Promptta "Strict Upper Bound" Tavanı Tanımlayın:** Pozitif isteme inşaatın duracağı kesin üst sınırı ve yalnızca o aşamada monte edilecek mikro malzemeleri ("only main support beams") açıkça yazın.   
5. **Negatif Promptta Yo-Yo Mekanizmalarını Yasaklayın:** Negatif istem bloğuna "100% completed, yo-yo assembly, elastic rebound, dissolving materials, dematerialization" terimlerini eksiksiz ekleyin.   
6. **Flow Matching Hızını Sınırlayın (Velocity Clamping):** Wan2.1/2.2 veya HunyuanVideo modellerinde tahmin edilen hız vektörlerine $v_{\text{max}} = \frac{z_B - z_A}{N} \cdot 1.1$ tavan klamplaması uygulayın.   
7. **Monotonic Attention Masking Aktifleştirin:** Mümkünse DiT uzamsal-zamansal dikkat katmanlarına ileriye doğru bilgi sızmasını önleyen alt-üçgensel zamansal dikkat maskesi uygulayın.   
8. **Diferansiyellenebilir Monotonluk Kaybı ($\mathcal{L}_{\text{mono}}$) Tanımlayın:** Özel fine-tuning boru hatlarında kareler arası özellik hacminin türevinin pozitif kalmasını sağlayan kayıp terimini aktif edin.   
9. **Kare Sayısını ve Zamansal Çözünürlüğü Sabit Tutun:** 8,0 saniyelik klip için VAE zamansal sıkıştırma oranına uygun kare sayısı (örneğin 24 fps'de 193 latent karesi) seçerek zamansal interpolasyon pürüzsüzlüğünü koruyun.   
10. **Kareler Arası Süreklilik Zincirini Test Edin:** Bir sonraki klibe (%25 $\to$ %50) geçmeden önce, üretilen klibin son karesinin ($z_{\text{actual\_N}}$) hedef karesiyle ($z_B$) SSIM/PSNR ve latent norm seviyesinde çakıştığını doğrulayın.
