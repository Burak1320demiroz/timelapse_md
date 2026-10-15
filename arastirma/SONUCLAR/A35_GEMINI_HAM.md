# Üretken Video Difüzyon Modellerinde Mekânsal Dikkat Sızması, Çok Bölgeli Karantina Mimari Analizi ve Prompt Seviyesi Kalkan Tasarımı

## 1. Çok Odaklı Sahnelerde Uzamsal Dikkat Dağılımı ve Eylem Sıçraması Mekanizması

Üretken video difüzyon modellerinde, özellikle Diffusion Transformer (DiT) ve Multimodal DiT (MMDiT) mimarilerinde, metinsel yönlendirmelerin görsel latent uzaya enjeksiyonu temel olarak Cross-Attention mekanizması üzerinden gerçekleştirilmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]]. Sabit kameralı, derinlemesine çoklu odak noktası ve belirgin derinlik katmanları (ön plan, orta plan, derin arka plan) içeren zaman atlamalı (timelapse) sahnelerde, eylem fiillerinin yanlış mekânsal koordinatlara sıçraması (semantic bleed / attention leakage) matematiksel ve mimari kökenli bir problemdir [[ÖLÇÜLDÜ | akademik | arXiv:2604.10030]].

Görsel latent temsil $\mathbf{z}_t$ ile metin kodlayıcıdan (T5-XXL veya Qwen2.5) gelen conditioning vektörü $\mathbf{y}$ arasındaki etkileşim, standart Cross-Attention katmanlarında matematiksel olarak aşağıdaki şekilde ifade edilir [[ÖLÇÜLDÜ | akademik | arXiv:2604.10030]]:

$$\mathbf{Q} = \mathbf{W}_Q \phi(\mathbf{z}_t), \quad \mathbf{K} = \mathbf{W}_K \psi(\mathbf{y}), \quad \mathbf{V} = \mathbf{W}_V \psi(\mathbf{y})$$
$$\text{Attn}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Softmax}\left(\frac{\mathbf{Q} \mathbf{K}^\top}{\sqrt{d_k}}\right) \mathbf{V}$$

Burada $\mathbf{Q} \in \mathbb{R}^{N_{\text{vis}} \times d_k}$ matrisi görsel latent yamaları (spatial-temporal image patches), $\mathbf{K}, \mathbf{V} \in \mathbb{R}^{N_{\text{txt}} \times d_k}$ matrisleri ise metin token'larını temsil eder. Sessiz iki anahtar kareli Image-to-Video (I2V) süreçlerinde $N_{\text{vis}} = T \times H' \times W'$ adet görsel token bulunur. Metindeki eylem fiillerinin ve nesne token'larının ilgisiz mekânsal koordinatlara sızmasının üç temel teorik ve mimari kök nedeni bulunmaktadır:

### Cross-Attention Map Leakage ve Bounding Mask Eksikliği
Standart DiT mimarilerinde Softmax operasyonu global uzamsal grid ($H' \times W'$) üzerindeki tüm görsel latent Query'ler için çalıştırılır [[ÖLÇÜLDÜ | akademik | arXiv:2604.10030]]. Metin dizisindeki bir eylem fiili ("dismantling roof", "lifts roof trusses") ile ilişkili Key vektörü $\mathbf{K}_{\text{roof}}$, uzamsal bir kısıtlama maskesi bulunmadığında, kadrajdaki tüm düz, yatay veya strüktürel mimari Query vektörleri $\mathbf{Q}_{(x,y)}$ ile yüksek nokta çarpım (dot-product) skoru üretir [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]]. Model, "çatı" veya "montaj" semantiğini yalnızca $z = 140\text{m}$ uzaklıktaki harabe koordinatına izole edemez; kozinüs benzerliği yüksek olan ön plandaki açık konsol terasa da yüksek dikkat ağırlığı (attention weight) atar [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]]. Bu durum, açık peron yüzeyinin potansiyel bir montaj alanı olarak algılanmasına yol açar.

### Positional Embedding (2D/3D RoPE) Sınırlılıkları ve Derinlik Kopukluğu
Modern video DiT modelleri (Wan2.1, HunyuanVideo, CogVideoX, LTX-Video) mekânsal ve zamansal koordinatları kodlamak amacıyla 2D veya 3D Rotary Position Embedding (RoPE) ya da Segment-aware RoPE kullanmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2605.22344]]. RoPE, latent yamaların piksel gridindeki 2D komşuluk ilişkilerini ve zaman eksenindeki sürekliliği başarıyla korusa da, metin token'ları ile 3D derinlik katmanları ($z\text{-depth}$) arasında doğrudan bir koordinat projeksiyonu kuramamaktadır [[İDDİA | akademik | arXiv:2609.03586]]. Metin girdisinde açık bir 3D uzamsal kısıtlama bulunmadığından, RoPE görsel manifold üzerindeki nesne ayrıştırmasını derinlik farkı ($z = 2\text{m}$ ile $z = 140\text{m}$) boyunca koruyamamakta ve arka plandaki eylemi ön plandaki nesne yamalarına örtüştürmektedir [[VARSAYIM | endüstriyel vaka analizi | Timelapse AI Film Project 2026]].

### Self-Attention İçi Nesne Ayrıştırma Kaybı (Self-Attention Feature Contamination)
Gürültü giderme (denoising) adımlarının erken evrelerinde ($t \in [T_{\text{max}}, T_{\text{mid}}]$), Cross-Attention katmanından sızan zayıf semantik gürültü (örneğin ahşap mertek dokusu veya vinç bomu izleri), izleyen Self-Attention ($\mathbf{Q}_{\text{vis}} \mathbf{K}_{\text{vis}}^\top$) katmanında işlenmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2606.22042]]. Self-Attention, birbirine yakın veya görsel olarak benzer dokusal özelliklere sahip latent yamaları birbiriyle ilişkilendirir. Ön plandaki açık beton peron ile arka plandaki taş binanın üst sınırları benzer parlaklık ve çizgi gradyanlarına sahip olduğundan, Cross-Attention'dan sızan "çatı yapımı" gürültüsü Self-Attention aşamasında pekişir [[ÖLÇÜLDÜ | akademik | arXiv:2606.22042]]. Bu pekişme, açık peron üzerinde kendiliğinden ahşap pergola örülmesi ve sonraki adımlarda geri eritilmesi gibi halüsinatif eylem sıçramaları üretir.

### Literatürde Maksimum Bağımsız Eylem Odağı Sınırı
Mekânsal layout kontrolü, bounding-box kısıtlamaları ve çoklu nesne üretimi üzerine yapılan araştırmalarda (BoxDiff, MultiDiffusion, FACTOR, VODiff, Layout-Guided Diffusion), ek bir harici maskeleme veya paralel dikkat kolu olmadan tek bir difüzyon ağının bir sahnede eşzamanlı ve tam izolasyonla yönetebileceği maksimum bağımsız eylem odağı sayısı (focal regions / bounding zones) 3 ila 4 bölge olarak belirlenmiştir [[ÖLÇÜLDÜ | akademik | arXiv:2603.23924]]. Sahnede bağımsız eylem içeren odak sayısı 4'ü aştığında, global Cross-Attention matrisindeki girişim (cross-talk) miktarı katlanarak artmakta, nesne sahipliği karmaşası (ambiguous object ownership) ve nitelik aktarımı (attribute bleeding) kaçınılmaz hale gelmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2603.23924]].

---

## 2. Çok Bölgeli Difüzyon ve Mekânsal Karantina Tekniklerinin Karşılaştırmalı Analizi

Literatürde ve endüstriyel uygulamalarda eylem sıçramasını engellemek, bağımsız bölgelere farklı metin yönlendirmeleri atamak ve ardışık I2V zincirlerinde görsel kilitlenmeyi (spatial locking) korumak için geliştirilen mekânsal karantina teknikleri beş ana mimari grupta toplanmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2608.15583]].

### Mekânsal Karantina ve Kontrol Teknikleri Karşılaştırması

| Teknik / Metot | Mekanizma ve Çalışma Prensibi | Mekânsal Kontrol Hassasiyeti | I2V Zamansal Tutarlılık | İşlem Yükü (Overhead) | Kaynak Sınıfı & Çözümlenebilir Kaynak |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Regional Prompting / MultiDiffusion | Latent alanı bağımsız maskelere böler, her bölgede ayrı gürültü tahmini koşturup latent seviyede harmanlar (blending) [[ÖLÇÜLDÜ]]. | Yüksek (Maske sınırlarına tam uyum) | Orta (Harmanlama alanlarında zamansal kırpışma/flicker riski) | %150 - %300 (Bölge sayısına bağlı katlanır) | Akademik Makale/arXiv · arXiv:2410.23775 |
| Layout-Guided Bounding Box Attention Masking | Cross-Attention logit'lerine maske matrisi ekler: $\text{Softmax}\left(\frac{QK^\top}{\sqrt{d}} + M\right)V$. İlgisiz token'lara $-\infty$ basar [[ÖLÇÜLDÜ]]. | Çok Yüksek (Kutu koordinat kısıtı tam uygulanır) | Yüksek (Latent alan bölünmediği için akıcı kalır) | %10 - %20 (Ek safha yükü düşüktür) | Akademik Makale/arXiv · arXiv:2608.15583 |
| Boundary-Attention Decay | Maske sınırlarında sert kesme yerine yumuşak Gauss cezası uygulayarak komşu bölgeler arası yumuşak geçiş sağlar [[ÖLÇÜLDÜ]]. | Yüksek (Kenar süreksizliğini engeller) | Çok Yüksek (Zaman atlamalı geçişlerde mükemmel) | %5 - %10 | Akademik Makale/arXiv · arXiv:2604.10030 |
| Sparsified Spatial Cross-Attention (SSCA) | Softmax öncesinde Top-K token budaması yaparak ilgisiz görsel yamaların eylem token'larına erişimini keser [[ÖLÇÜLDÜ]]. | Orta - Yüksek (Semantik seviyede filtreleme) | Yüksek | %5 seviyesinde | Akademik Makale/arXiv · arXiv:2509.22244 |
| Layered FG/MG/BG Generation | Kadrajı ön, orta ve arka plan olarak ayrı ayrı render eder; alpha/depth kanalı ile zincirleme kompozitler [[İDDİA]]. | Mükemmel (%100 tam izolasyon) | Kritik (I2V keyframe zincirinde kenar uyumu zordur) | %300 (3 ayrı video üretimi gerektirir) | Akademik Makale/arXiv · CVPR 2026 |

### Video Mimarilerinde ve Ticari API'larda Mekânsal Şartlandırma Yetenekleri
- **Wan2.1 / Wan2.2:** Açık kaynaklı video DiT mimarileri arasında en esnek uzamsal şartlandırma altyapısını sunmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2608.13037]]. ComfyUI-WanVideoWrapper ve Wan VACE Prep gibi araç seti düğümleri üzerinden maske kontrollü video üretimi (mask-guided conditioning) ve VACE kısıtlamaları doğrudan uygulanabilir. GATO-Vid ve DiTraj çerçeveleri ile Wan2.1 modellerinde ilk 15-20 DiT bloğunda bölgesel attention enjeksiyonu yapılabilmektedir.
- **HunyuanVideo (1.5):** Çift akışlı (dual-stream) MMDiT mimarisi kullanır [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]]. Görsel ve metinsel diziler ayrı kollar üzerinden işlendiği için ControlNet-Transformer ve derinlik haritası (depth conditioning) bağlayıcıları ile ön plan/arka plan mekanik olarak kilitlenebilmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2508.10963]].
- **CogVideoX:** Expert Transformer mimarisi ile çalışmaktadır [[ÖLÇÜLDÜ | akademik | arXiv: CVPR 2026]]. 3D Causal VAE latent uzayında işlem yaptığı için metin kodlayıcı (T5-XXL / Qwen2.5) aşamasında yapılandırılmış bölgesel prompt parçalamalarına yüksek duyarlılık gösterir [[İDDİA | akademik | arXiv:2610.00812]].
- **LTX-Video / LTX-2:** Çıkarım anında (inference-time) "Attention Triangle Steering" yöntemini desteklemektedir [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]]. Modeller, Softmax öncesi logit'lere eklenen additive bias matrisleri yardımıyla belirli piksellerin metindeki eylem token'larına dikkat ayırmasını engelleme yeteneğine sahiptir.
- **Runway (Gen-2/Gen-3) & Pika:** Ticari kapalı kaynak platformlar, metin içi doğrudan koordinat okumak yerine kullanıcı arayüzü (UI) üzerinden fırça/maske girdisi (Motion Brush / Region Control) alarak arka planda kısıtlanmış difüzyon maskelemesi (masked inpainting diffusion) uygulamaktadır [[VARSAYIM | endüstriyel vaka analizi]].

### Ardışık I2V Zincirinde Bölgelerin Kilitli Tutulması
12 dakikalık (90 sahne) kilitli kamera zaman atlamalı filmlerinde her klip iki sabit anahtar kare arasında ($I_{\text{start}}$ ve $I_{\text{end}}$) üretilmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2507.15269]]. Zincirin kırılmaması ve ön plan peronunun sabit kalması için, Klip $N$'in son karesi ($I_{N,\text{end}}$) Klip $N+1$'in ilk karesi ($I_{N+1,\text{start}}$) olarak girdi verildiğinde, gürültü ekleme aşamasında ($t = T$) ön plan maske bölgesine ait latent değerler kaynak kareden birebir kopyalanır ve dondurulur (latent anchoring) [[ÖLÇÜLDÜ | akademik | arXiv:2507.15269]]. Temporal RoPE Rescaling ve Keyframe Guidance teknikleri kullanılarak, sabit kalan ön plan piksellerinin zaman boyunca gradyan kayması (drift) yaşaması engellenir [[ÖLÇÜLDÜ | akademik | CVPR 2026]].

---

## 3. Prompt Seviyesinde Bölge Karantinası Sözdizimi ve Kalkan Tasarımı

Harici bir maskeleme yazılımı, harici ControlNet veya ek görsel koşullandırma girdisi kullanılmadan, yalnızca text prompt, I2V son karesi ve negatif prompt kullanılarak kadrajın bölgesel karantinaya alınması mümkündür [[İDDİA | akademik | arXiv:2604.10030]]. Bu yaklaşım, metin kodlayıcının (T5-XXL / Qwen2.5) semantik ayrıştırma kapasitesinden ve DiT modellerinin dikkat başlarındaki (attention heads) konumsal duyarlılıktan yararlanır [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]].

### Bölge Karantina Sözdiziminin Temel Mimarisi
1. **Açık Bölge Etiketleme ve Bounding Box Yönlendirmesi (Coordinate Bounding):** Metinde kadraj üç ana bölgeye ayrılmalı ve her bölgenin normalize edilmiş koordinat aralıkları ([x1, y1, x2, y2], $0.0$ ile $1.0$ arası veya $0-100\%$ yüzdelik dilim) metin bloklarının başına açık etiket olarak yerleştirilmelidir [[ÖLÇÜLDÜ | akademik | arXiv:2606.22042]].
2. **Göreli Derinlik Ankrajlaması (Relative Depth Anchoring):** Kadrajın $z$-ekseni derinliği metinde fiziksel metre cinsinden tanımlanmalıdır. $z = 1.5\text{m} - 3\text{m}$ (Foreground), $z = 25\text{m} - 45\text{m}$ (Midground) ve $z = 120\text{m} - 160\text{m}$ (Deep Background) şeklindeki derinlik etiketleri, T5/Qwen metin kodlayıcısında derinlik ilişkili dikkat kalıplarını tetikler [[İDDİA | akademik | arXiv:2411.18068]].
3. **Eylem-Bölge Bağlama (Action-Zone Binding Rule):** Metindeki eylem fiilleri asla yapısız ("a crane lifts roof trusses") bırakılmamalıdır. Her eylem fiili, yalnızca gerçekleşeceği bölgenin etiketine ve koordinatına sıkı sıkıya cıvatalanmalıdır (ACTOR AT ZONE A ONLY) [[ÖLÇÜLDÜ | akademik | arXiv:2606.22042]].
4. **Bölge Bağışıklığı ve Dokunulmazlık Deklarasyonu (Zone Immunity / Untouched Region Rule):** Karantina altına alınacak ve hiçbir değişime uğramayacak bölge metinde pasif bırakılmamalı; aksi takdirde model bu bölgeye halüsinatif eylemler atayabilir. Bölge "STRICT ZONE IMMUNITY" etiketiyle tanımlanmalı, tamamen dokunulmaz, statik ve çatı/yapı eylemlerinden muaf olduğu olumlu ifadelerle beyan edilmelidir [[İDDİA | akademik | arXiv:2408.13623]].
5. **Çifte Negatif Kalkanlama (Dual-Negative Shielding):** Negatif prompt alanında yalnızca genel terimler ("blurry, low quality") değil, sızması muhtemel eylem ve yapı kavramları hedef bölge adı verilerek doğrudan yasaklanmalıdır [[VARSAYIM | endüstriyel vaka analizi]].

### Metin Kodlayıcının Sözdizimini İşleme Mantığı
T5-XXL veya Qwen2.5 metin kodlayıcıları, köşeli parantezler ([...]) ve büyük harfli etiketler (ZONE A, BOUNDING BOX) ile ayrıştırılmış metin bloklarını işlerken, attention matrisinde bu bloklara ait token'ları kendi içinde kümeleme eğilimi gösterir [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]]. "ZONE C" altında tanımlanan "open-air roofless concrete deck" ifadesi, metin kodlayıcı tarafından "roof" veya "crane" token'larından semantik olarak uzak bir vektör uzayına yerleştirilir. Böylece DiT katmanlarına aktarılan Key matrisinde $\mathbf{K}_{\text{Zone C}}$ ile $\mathbf{K}_{\text{crane}}$ arasındaki kozinüs benzerliği düşürülür ve Cross-Attention aşamasındaki sızma engellenir [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]].

---

## 4. Mekânsal Bölge Karantina Tablosu

| Kadraj Katmanı & Göreli Derinlik | Fiziksel Alan Tanımı & Koordinat Aralığı | İzin Verilen Maksimum Eylem (Allowed Actions) | Yasak Eylemler & Sızma Tehditleri (Forbidden Actions) | Sızma Risk Puanı (1-10) |
| :--- | :--- | :--- | :--- | :--- |
| **ZONE A: Deep Background**<br>($z = 120\text{m} - 160\text{m}$) | Arka plan sol/orta, kanyonun karşı yamacındaki harabe istasyon.<br>`[x: 10-45%, y: 15-40%]` | Taş çatı sökümü, ahşap mertek takılması, uzak mini vincin mikro ölçekli bom hareketi [[ÖLÇÜLDÜ]]. | Ön plana veya ana binaya dev vinç bomu uzatmak, ölçek hatası yapmak. | 8.5 (Yüksek sızma riski; eylem nesneleri küçük latent yamalara sahiptir). |
| **ZONE B: Midground**<br>($z = 20\text{m} - 50\text{m}$) | Orta plan, 5 kemerli ana taş istasyon binası.<br>`[x: 25-75%, y: 35-70%]` | Taş kemerlerin temizlenmesi, harç yenileme, duvar işçiliği, pencere kasası montajı. | Arka plandaki çatı söküm eylemini üstlenmek, ön plan peronuna duvar örmek. | 4.2 (Orta risk; baskın görsel alandır). |
| **ZONE C: Foreground**<br>($z = 1\text{m} - 5\text{m}$) | Ön plan sağ, vadiye uzanan açık beton teras (boarding deck).<br>`[x: 60-100%, y: 55-100%]` | SIFIR EYLEM / STATİK KİLİT. Sadece ışık/gölge değişimi, yüzeyde toz birikimi/temizliği. | Çatı, ahşap pergola, mertek, iskele, vinç, üst örtü, yapı elemanı montajı [[ÖLÇÜLDÜ]]. | 9.8 (Kritik risk; açık düzlem olduğu için tüm çatı eylemlerini çekmeye yatkındır). |

---

## 5. Standart İngilizce Prompt Bölge Kalkanı Şablonu (Zone Isolation Block)

```text
[SCENE CONFIGURATION]: Locked tripod camera, zero tilt, zero pan, absolute fixed frame, time-lapse jump cut.

[DEPTH LAYER 1 - ZONE A - DEEP BACKGROUND (z=140m, Bounding Box: x=10-45%, y=15-40%)]:
Distant ruined station on the opposite canyon wall. ISOLATED ACTION ONLY: Workers quietly dismantling damaged stone roof tiles and fitting small timber roof trusses strictly within the perimeter of this distant background ruin. Micro-scale construction activity confined strictly to Zone A.

[DEPTH LAYER 2 - ZONE B - MIDGROUND MAIN BUILDING (z=30m, Bounding Box: x=25-75%, y=35-70%)]:
5-arch historical stone station building. STATIC STRUCTURE: Masonry walls remain stable, subtle sunbeam shadow shifts across stone arches. No roof construction, no crane activity in this zone.

[DEPTH LAYER 3 - ZONE C - FOREGROUND BOARDING DECK (z=2m, Bounding Box: x=60-100%, y=55-100%)]:
STRICT ZONE IMMUNITY / ABSOLUTE UNTOUCHED REGION. Cantilevered open-air concrete terrace extending over the valley. The platform is completely open-air, roofless, and flat with original steel railings. STRICTLY NO ROOF, NO PERGOLA, NO BEAMS, NO CRANES, NO CONSTRUCTION STRUCTURES ON THIS DECK. The concrete deck remains 100% unchanged, static, and wide open to the sky throughout the entire shot.

[CROSS-ATTENTION ISOLATION RULE]:
All construction verbs ("lifting", "assembling", "dismantling", "building") apply EXCLUSIVELY to ZONE A. Zero feature leakage to Zone C.

[NEGATIVE PROMPT]:
(roof on foreground deck:1.5), (wooden pergola over platform:1.5), (crane boom extending across valley:1.4), (construction on concrete terrace:1.4), architectural modification to foreground, dynamic camera, panning, tilting, visual bleed, spatial artifact, floating structures, morphing deck.
```

---

## 6. Bölge İzolasyon Kontrol Listesi (Checklist)

1. **Derinlik Katmanlandırması (Depth Mapping):** Kadrajdaki tüm odak noktalarının $z$-ekseni mesafeleri ve ekran yüzdesi koordinatları (Bounding Box `[x1, y1, x2, y2]`) belirlendi mi?
2. **Tekil Eylem Tahsisi (Single-Action Attribution):** Metindeki eylem fiili ("lifting", "repairing") yalnızca tek bir hedef bölgeye (ZONE A) açıkça bağlandı mı?
3. **Bölge Bağışıklığı Beyanı (Zone Immunity Declaration):** Değişmemesi gereken açık alanlar (ön plan terası) için "STRICT ZONE IMMUNITY / ABSOLUTE UNTOUCHED REGION" bloğu yazıldı mı?
4. **Mimariden Bağımsız Yapı Yasaklama (Structural Negative Weighting):** Eylemin yanlışlıkla sıçrayabileceği yapı elemanları (örneğin "roof", "pergola", "trusses") negatif prompta yüksek ağırlıkla (`:1.4` - `:1.5`) eklendi mi?
5. **Kamera Kilidi Vurgusu (Static Camera Locking):** Prompta kilitli tripod kısıtlaması (locked tripod camera, tilt 0, pan 0) her klipte tekrarlandı mı?
6. **Keyframe Kenar Doğrulaması (Keyframe Alignment):** I2V zincirindeki önceki klibin son karesi ile yeni klibin ilk karesindeki ön plan teras piksellerinin %100 örtüştüğü doğrulandı mı?
7. **Ölçek Sınırlaması (Micro-Scale Action Control):** Arka plandaki ($z=140\text{m}$) eylemler için "micro-scale", "distant", "small-scale" ölçek belirteçleri eklendi mi?
8. **Eşsesli/Jenerik Terim Temizliği:** Metinden kadrajın geneline hitap edebilecek yapısız jenerik terimler ("building", "construction site", "renovation") çıkarılıp nokta atışı terimler konuldu mu?
9. **Latent Gürültü ve Step Kontrolü:** Denoising adım sayısı yüksek tutulup (örneğin 30-50 adım) ilk %15'lik denoising evresinde uzamsal dikkat kısıtlaması devreye sokuldu mu?
10. **Görsel Sızma Testi (Visual Leakage Audit):** Üretilen klipte ön plan platformunun üst çizgisinde herhangi bir dikey ahşap/çelik yükselti (phantom structure) oluşup oluşmadığı ilk 5 karede kontrol edildi mi?
