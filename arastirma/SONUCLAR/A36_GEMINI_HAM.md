# Üretken Yapay Zekâ Metin-Video Modellerinde Mimari Semantik Sızma, Çapraz Dikkat Özellik Bağlama Başarısızlıkları ve Tipoloji Kilitleme Metodolojisi

## 1. Çapraz Dikkat Katmanlarında Mimari Terminolojinin Ayrıştırılması ve Semantik Sızma Mekanizması

### Metin Kodlayıcıların (CLIP ViT-L/14, T5-XXL, Llama-3/VLM) Mimari Asimetrisi ve Düzeyli Kodlama Sınırları
Üretken video difüzyon modellerinde (Diffusion Transformer - DiT, Stable Video Diffusion, Gen-3, Sora mimarisi, Wan2.1 vb.) metin şartlandırması (text conditioning), metin kodlayıcıların ürettiği vektör gömmelerinin (embeddings) çapraz dikkat (cross-attention) katmanları üzerinden görsel latent uzaya iz düşürülmesiyle gerçekleştirilmektedir. Farklı metin kodlayıcı mimarilerinin teknik ve mimari terminolojiyi işleme yetenekleri, modellerin içsel dizilim mekanizmalarından kaynaklanan köklü matematiksel farklılıklar sergilemektedir.   

CLIP ViT-L/14 (Contrastive Language-Image Pre-training) mimarisi, otoregresif yapısı ve nedensel maskeleme kullanımı sebebiyle metin dizilimindeki sonraki token'larda, önceki sıfat ve isimlerin anlamsal birikimini taşımaktadır. CLIP, metin dizilimini tek bir sabit uzunluktaki vektöre sıkıştırmak üzere dizi sonu (<EOS>) token'ından yararlanmaktadır. Bu durum, <EOS> gömmelerinin cümledeki tüm nesne ve özellikleri tek bir darboğazda toplamasına ve dolayısıyla "truss", "deck", "rafter" gibi birbirine yakın mimari terimler arasında yüksek derecede anlamsal dolaşıklık (embedding entanglement) oluşturmasına yol açmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2412.04715]].   

T5-XXL (Text-to-Text Transfer Transformer) mimarisi ise yalnızca kodlayıcı içeren maskeli dil modeli yapısı sayesinde her bir token'ı, sağ ve solundaki tüm bağlamı iki yönlü olarak işleyerek kodlamaktadır. T5-XXL, karmaşık dilbilgisi bağıntılarını ve teknik terim hiyerarşilerini CLIP'e kıyasla belirgin şekilde daha yüksek sentaktik sadakatle temsil etmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2212.05032]]. Bununla birlikte, doğrudan karşılaştırmalı bir görsel-metin hizalama eğitimi (contrastive vision-text loss) görmediği için, teknik mimari ifadelerin görsel uzaydaki hassas geometrik sınırlarını tek başına garanti etmekte yetersiz kalabilmektedir [[İDDİA | teknik doküman | Google T5 Technical Report]].   

Llama-3 ve multimodal VLM (Vision-Language Model) tabanlı metin kodlayıcılar (Wan2.1 MoRoute, Qwen3.5-9B gibi) geniş ölçekli ön eğitim veri kümelerindeki anlamsal ilişki öndağılımlarını latent uzaya aktarmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2501.06638]]. Nadir kullanılan hassas mimari terimler ("pitched rafter system", "cantilevered steel girder"), modelin dil katmanlarındaki istatistiksel önceller nedeniyle daha yüksek frekansta eğitilmiş genel kavramlara ("pyramidal roof", "wooden deck") doğru çekilme eğilimi göstermektedir [[VARSAYIM | analiz | Analiz - DERS 80]].   

### Cross-Attention Bağlama Başarısızlığı ve Semantik Sızmanın Matematiksel Mekanizması
Video difüzyon transformatörlerinde bir latent $z_t \in \mathbb{R}^{B \times C \times T \times H \times W}$ karesi için çapraz dikkat mekanizması, görsel latent özellik eşleminin Sorgu ($Q_t$) vektörlerine dönüştürülmesi ve metin kodlayıcıdan gelen gömmelerin Anahtar ($K_p$) ile Değer ($V_p$) vektörlerine iz düşürülmesiyle çalışmaktadır:   

$$Q_t = f_Q(z_t) \in \mathbb{R}^{N \times (T \cdot H \cdot W) \times d_k}$$
$$K_p = f_K(e_{\text{text}}) \in \mathbb{R}^{N \times L \times d_k}, \quad V_p = f_V(e_{\text{text}}) \in \mathbb{R}^{N \times L \times d_v}$$

Çapraz dikkat ağırlık haritası $A_t$ ve katman çıktısı $O_t$ şu eşitliklerle türetilmektedir:   

$$A_t = \text{softmax}\left(\frac{Q_t K_p^T}{\sqrt{d_k}}\right) \in \mathbb{R}^{N \times (T \cdot H \cdot W) \times L}$$
$$O_t = A_t V_p$$

"Attribute Binding Failure" ve "Semantic Bleed" olgusu, metin gömmelerindeki $e_{\text{text}}$ dolaşıklığı nedeniyle $K_p$ Anahtar matrisindeki farklı token vektörlerinin kosinüs benzerliğinin aşırı yükselmesiyle tetiklenmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2412.04715]]. Örneğin "cantilevered platform deck" ve "roof decking sheathing" ifadeleri aynı istemde bulunduğunda, metin kodlayıcı çıktısındaki $K_{\text{deck1}}$ ve $K_{\text{deck2}}$ vektörleri latent uzayda çakışmaktadır. Çatı bölgesindeki mekânsal Sorgu vektörleri $Q_{\text{roof}}$, zemin platformu Anahtar vektörüne $K_{\text{deck}}$ yüksek dikkat katsayısı ($A_t[\text{roof}, \text{deck}] > \epsilon$) atamaktadır. Bu süreç sonucunda Hedef İçi Sızma Skoru (Target-Internal Leakage Score - TILS) ve Hedef Dışı Sızma Skoru (Target-External Leakage Score - TELS) değerleri belirgin biçimde yükselmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2412.04715]]:   

$$\text{TILS} = \frac{1}{N(N-1)} \sum_{i \neq j}^{N} \text{CLIP}(x_{\text{tgt}} \odot m_j, y_i^{\text{tgt}})$$
$$\text{TELS} = \frac{1}{N} \sum_{i=1}^{N} \text{CLIP}\left(x_{\text{tgt}} \odot \left(1 - \bigcup_{j=1}^N m_j\right), y_i^{\text{tgt}}\right)$$

### Teknik Terimlerin Anomali ve Mutasyon Analizi
"Truss" (makas) token'ı, eğitim verisetlerinde çoğunlukla "space frame" (uzay kafes), "triangular steel structure" ve "pyramidal truss tower" yapılarıyla eş dizilim göstermektedir [[ÖLÇÜLDÜ | akademik | arXiv:2501.06638]]. Modeller tekil bir "truss" gördüğünde, cross-attention $A_t$ haritaları üçgensel ve dikine sivrilen vektör kümelerine odaklanmaktadır. Ardışık sahnelerde "rafter" veya "pitched roof" kullanıldığında, Anahtar matrisindeki $K_{\text{truss}}$ rezonansı görsel latent uzayı aniden dört adet sivri piramidal köşke (pavilions) doğru bükerek geometrik mutasyona uğratmaktadır [[VARSAYIM | analiz | Analiz - DERS 80]].   

"Deck" token'ı çok anlamlı (polysemous) bir yapıya sahiptir. "Timber deck" (zemin ahşap döşemesi) ile "roof decking" (çatı kaplama tahtası) ifadelerindeki ortak "deck" kökü, metin kodlayıcının otoregresif katmanlarında $e_{\text{deck}}$ vektörünün çakışmasına sebep olmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2412.04715]]. Modeller, zemin elemanı için yazılan "cantilevered platform / deck" kelimesindeki "deck" Anahtar vektörünü çatı bölgesinin mekânsal Sorgu $Q$ vektörüne bağlamakta ve seyir peronunun üstüne çatı inşa etmektedir [[VARSAYIM | analiz | Analiz - DERS 80]].   

DiT modellerinde öne çıkan görsel belirginlik (saliency bias) mekanizması, kadraj köşesindeki çıplak kaya sivrisini ("rock pinnacle") izole bir dikey geometrik kütle olarak algılamaktadır. Metin isteminde bu kayalığa açık bir negatif kalkan uygulanmadığında, modelin semantik öndağılımları dikey kütleleri insan yapısı "statue pedestal" veya "watchtower" olarak etiketlemekte ve üzerine devasa bir insan figürü yerleştirmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2610.11286]].   

Video difüzyon modellerinde metin şartlandırması hem görsel hem de işitsel latent uzayları eşzamanlı yönetebilmektedir. İstem içerisindeki "acoustic guitar enters" veya "orchestral sound" gibi müzikal ifadeler, Üçgen Dikkat (Attention Triangle: Text-Video-Audio) yüzeyinde görsel Sorgu $Q_{\text{video}}$ vektörlerinin metindeki müzik Anahtarlarına $K_{\text{audio}}$ çapraz bağlanmasına yol açmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]]. Bu durum, kesintisiz bir fon müziği oluşturmak yerine visual latent uzayda 8 saniyelik kopuk parazit seslere ve görüntüde fiziksel müzik enstrümanı illüzyonlarına neden olmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]].   

---

## 2. Kontrollü Mimari Sözlük ve Kavramsal İzolasyon Stratejileri
Semantik sızmayı ve tipolojik mutasyonları engellemek amacıyla dilsel açıdan izole edilmiş Kontrollü Mimari Sözlük (Controlled Architectural Vocabulary) standartları geliştirilmiştir. Yüksek sızma riskine sahip esnek/genel terimlerin kullanımı sınırlandırılmalı, bunların yerine geometrik ve imalat hatlarını katı bir biçimde tanımlayan Birebir Güvenli İfadeler (Strict Unambiguous Tokens) yerleştirilmelidir.   

### Tipolojik Ayrıştırma ve İzolasyon Eşleştirmeleri

| Mimari Yapı Elemanı | Tehlikeli / Yüksek Sızma Riskli Terim | Risk Mekanizması ve Mutasyon Tipi | Kontrollü Güvenli Karşılık (Strict Token) | Negatif İstem Kalkanı (Negative Shield) |
| :--- | :--- | :--- | :--- | :--- |
| Çatı Taşıyıcı İskeleti | truss, timber frame | Piramidal uzay kafes ve köşk formlarını tetikler [[VARSAYIM \| analiz \| Analiz - DERS 80]]. | parallel dual-chord steel I-beam rafters, steel purlin system | pyramidal roof, space frame, pavilion, gazebo, wood truss |
| Çatı Kaplama Yüzeyi | roof decking, decking | Zemin döşemesi ile çapraz bağlanarak peron üretir [[ÖLÇÜLDÜ \| akademik \| arXiv:2412.04715]]. | corrugated steel roof sheathing, standing seam metal roof panels | timber decking, wood planks, floor deck, terrace platform |
| Zemin / Seyir Terası | cantilevered deck, platform | Çatı örtüsü örmeye başlar [[VARSAYIM \| analiz \| Analiz - DERS 80]]. | reinforced cast-in-place concrete ground-level boarding slab | roof structure, overhead pergola, roof rafters, trusses |
| Eğimli Çatı Elemanı | pitched roof, rafter | Beşik çatı ile piramidal çatı arasında kararsızlık [[VARSAYIM \| analiz \| Analiz - DERS 80]]. | dual-sloped straight gable roof with horizontal ridge beam | hip roof, mansard roof, pavilion, pointed timber spire |
| Geçici İnşaat İskeleleri | scaffold, staging | Bina cephesini kalıcı demir kafese dönüştürür. | modular exterior tubular steel construction scaffolding | permanent steel grid, cage facade, structural frame |
| Açık Yürüyüş Yolu | walkway, boardwalk | Ahşap çatı karkası ile karışır [[ÖLÇÜLDÜ \| akademik \| arXiv:2412.04715]]. | crushed stone pedestrian path, concrete paved walkway | timber deck, raised wooden boardwalk, roof catwalk |
| Saha Doğal Yapısı | rock pinnacle, cliff horn | Heykel kaidesi veya kule sanılıp insan dikilir [[ÖLÇÜLDÜ \| akademik \| arXiv:2610.11286]]. | barren natural monolithic granite cliff face, natural bedrock | statue, monument pedestal, watchtower, carved human figure |

### Sözdizimsel Hizalama Yöntemleri: SynGen, DisCLIP ve Focused Cross-Attention (FCA)
Metin-görsel uyumsuzluklarını gidermek üzere literatürde öne çıkan üç ana algoritmik kontrol mekanizması bulunmaktadır:   

SynGen (Syntactic Alignment Loss) yaklaşımı, dilbilgisel bağımlılık ayrıştırması (dependency parsing) kullanarak sıfatlar ile isimler arasındaki çapraz dikkat haritalarının çakışmasını zorunlu tutmaktadır. Niteleyici dikkat haritası $A_{\text{modifier}}$ ile isim dikkat haritası $A_{\text{noun}}$ arasındaki örtüşme özel bir kayıp fonksiyonu ile artırılırken, ilgisiz nesneler arasındaki çakışmalar cezalandırılmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2306.08877]].   

Focused Cross-Attention (FCA) ve DisCLIP mimarisi, metin istemini bağımlılık matrisine $D \in \{0,1\}^{n \times n}$ dönüştürmektedir. Yalnızca ilgili nesnenin bulunduğu bölgeye dikkatin odaklanmasını sağlayan ikili bir odak maskesi $F_{\text{mask}} = \delta(A^* D^T)$ uygulanarak dikkat işlemi şu şekilde gerçekleştirilmektedir:   

$$\text{FCA}(Q, K, V, F_{\text{mask}}) = \text{softmax}\left(F_{\text{mask}} + \frac{QK^T}{\sqrt{d_k}}\right)V$$

Bu yöntem, nesneye ait olmayan niteliklerin ilgisiz mekânsal bölgelere sızmasını engellemektedir [[ÖLÇÜLDÜ | akademik | arXiv:2404.13766]].   

ALE (Addressing Text Embedding Leakage - ICCV 2025) yaklaşımı ise CLIP kodlayıcısındaki otoregresif semantik kirlenmeyi engellemek amacıyla her nesneye özel Nesneye Göre İzafi Gömmeler (Object-wise Relative Embedding - ORE) üretmekte ve Bölge Güdümlü Harmanlama (Region-Guided Blending for Cross-Attention Masking - RGB-CAM) tekniğini kullanmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2412.04715]].   

---

## 3. Semantik Bağlama ve Tipoloji Kilidi Sözdizimi
I2V (Image-to-Video) ve keyframe zinciriyle üretilen inşaat timelapse projelerinde kameranın sabit kalması, geometrinin mutasyona uğramaması ve sahneler arası görsel sürekliliğin korunması amacıyla "Tipoloji Kilidi Sözdizimi" (Typology Lock Syntax) uygulanmaktadır.   

### Tipoloji Kilitleme Sözdizim Yapısı
Tipoloji kilitli bir I2V istem şablonu katı bir hiyerarşik sıralamayı takip etmelidir:
1. Kamera ve Kadraj Kilidi bileşeni ile sabit tripod açısı ve sıfır kamera hareketi tanımlanır.
2. Ana Yapısal Zarf Kilidi bileşeni ile yapının genel hacimsel sınırları belirlenir.
3. Bileşen Düzeyinde Malzeme ve Geometri Dondurma bileşeni ile çatı, döşeme ve taşıyıcı Elemanların geometrik detayları sabitlenir.
4. Zamansal İmalat Eylemi bileşeni ile profil değiştirilmeden yapılacak inşaat adımı belirtilir.
5. Negatif Sızma Kalkanı bileşeni ile istem dışı formlar engellenir.

### Akustik Metin İzolasyonu ve Çevresel Ses Sınırlamasının Ölçülmüş Etkisi
Metin dışı modalitelerin (müzik, atmosferik ses tanımları) video istemlerinden arındırılarak yalnızca diegetik çevre seslerine ("ambient wind on construction site", "distant mechanical hum") sınırlandırılmasının etkileri literatürde deneysel olarak ölçülmüştür [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]]:   

- Görsel Nesne Halüsinasyonlarının Önlenmesi kapsamında, prompt metninden müzikal ifadelerin çıkarılması görsel çapraz dikkat katmanlarındaki parazit aktivasyonları %100 oranında engellemektedir [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]].   
- Zamansal Tutarlılık (Fréchet Video Distance - FVD) İyileşmesi doğrultusunda, işitsel token sızmasının durdurulması karesel görsel sürekliliği artırmakta ve FVD skorlarında belirgin iyileşme sağlayarak kesmeler arası geometrik sıçramaları engellemektedir [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586, arXiv:2412.17042]].   
- Parazit Seslerin Kesilmesi neticesinde, işitsel latent uzaydaki dalgalanmalar önlenmekte ve sahneler arası pürüzsüz akustik geçişler elde edilmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]].   

---

## 4. Ek Dokümantasyon ve Denetim Seti

### (a) Yüksek Sızma Riskli Mimari Terimler ve Güvenli Karşılıkları Tablosu

| Tehlikeli Terim | Neden Mutasyon Doğurur | Güvenli Kilit İfadesi (Strict Lock Token) |
| :--- | :--- | :--- |
| truss | Piramidal uzay kafes ve gazeboları tetikler [[VARSAYIM \| analiz \| DERS 80]]. | parallel dual-chord steel I-beam girders or horizontal steel purlins |
| deck / decking | Zemin ile çatı kaplamasını birbirine karıştırır [[ÖLÇÜLDÜ \| akademik \| arXiv:2412.04715]]. | corrugated steel roof sheathing (roof) / concrete boarding slab (ground) |
| rafter | Beşik çatıdan sivri ahşap pavilyona sıçrar [[VARSAYIM \| analiz \| DERS 80]]. | linear steel roof purlins along longitudinal slope |
| timber frame | Rustik kulübe ve ahşap dikme illüzyonu yaratır. | prefabricated modular heavy timber glulam posts |
| platform | Askıdaki platformu çatı kütlesine dönüştürür [[VARSAYIM \| analiz \| DERS 80]]. | cast-in-place reinforced concrete slab terrace |
| pinnacle | Doğal kayayı heykel kaidesi yapar [[ÖLÇÜLDÜ \| akademik \| arXiv:2610.11286]]. | barren natural granite cliff face, sheer mountain rock |
| scaffold | Bütün binayı kalıcı demir kafese hapseder. | temporary exterior steel pipe scaffolding |
| beam | Kolon, kiriş ve çatı çıtasını karıştırır [[ÖLÇÜLDÜ \| akademik \| arXiv:2412.04715]]. | horizontal steel lintel (wall) / roof purlin (roof) |

### (b) Standart İngilizce Tipoloji Kilidi Şablonu

```text
CAMERA_LOCK: Ultra-high-resolution architectural timelapse, fixed single locked-off tripod perspective, zero camera pan/tilt/zoom, stationary frame.

PRIMARY_TYPOLOGY_LOCK:
ROOF_STRUCTURE: Locked typology: Dual-sloped steel purlin gable roof. No pyramidal roofs, no trusses, no timber rafters.
FLOOR_SLAB: Locked typology: Ground-level cast-in-place reinforced concrete slab. No timber decking, no elevated platform floors.
SCAFFOLDING: Locked typology: Temporary modular tubular steel perimeter scaffolding, partially enclosing the facade.
MECHANICAL_COMPONENTS: Locked typology: Visible galvanized steel HVAC ductwork running linearly along the ceiling plane.

TEMPORAL_ACTION_LOCK: Time-lapse construction sequence between Frame A and Frame B. The geometry of the roof, slab, and scaffolding remains strictly stationary; only material installation progress occurs over time.

NEGATIVE_PROMPT_SHIELD: pyramid roof, gazebo, pavilion, roof decking, timber rafters, space frame, statue, pedestal, watchtower, camera motion, cross-fading structural types, acoustic guitar, orchestral music.
```

### (c) Semantik Sızma ve Sözlük Denetim Listesi
1. **Polysemous Token Hijyen Denetimi:** İstem içerisinde deck, beam, frame gibi çok anlamlı kök kelimelerin tekil kullanımından kaçınılmalı; her biri malzeme ve işlev ön ekiyle (reinforced concrete floor slab) sabitlenmelidir [[ÖLÇÜLDÜ | akademik | arXiv:2412.04715]].   
2. **"Truss" Kelimesinin Tamamen Çıkarılması:** Eğimli ve düz çatı istemlerinde truss kelimesi kullanılmamalı, yerine parallel dual-chord steel I-beam girders veya steel purlins ifadeleri tercih edilmelidir [[VARSAYIM | analiz | Analiz - DERS 80]].
3. **Çatı ve Döşeme Anlamsal İzolasyonu:** Çatı kaplaması için asla decking kelimesi kullanılmamalı; bunun yerine corrugated steel roof sheeting veya roof panels ifadeleri yerleştirilmelidir [[ÖLÇÜLDÜ | akademik | arXiv:2412.04715]].   
4. **Kadraj Köşesi Doğal Kütle Kalkanı:** Kadrajda yer alan kayalık veya tepe yapıları için rock pinnacle terimi yerine barren natural granite cliff face ifadesi kullanılmalı ve negatif isteme statue, pedestal, human figure, watchtower eklenmelidir [[ÖLÇÜLDÜ | akademik | arXiv:2610.11286]].   
5. **Akustik ve Müzikal Metin Temizliği:** Video istem metinlerinden guitar, orchestral, music enters, soundtrack gibi tüm müzikal ve atmosferik ses adlandırmaları tamamen çıkarılmalıdır [[ÖLÇÜLDÜ | akademik | arXiv:2609.03586]].   
6. **Kamera Sabitlik İfadesi:** İstem başına mutlak fixed single locked-off tripod perspective ifadesi eklenerek kesmeler arasındaki kamera hareketi kaynaklı geometrik bozulmalar önlenmelidir.   
7. **İskele (Scaffolding) Geçicilik Kilidi:** İskele tanımlarında temporary exterior tubular steel pipe scaffolding bileşimi kullanılmalı ve negatif isteme permanent steel grid, cage facade terimleri yerleştirilmelidir.   
8. **I2V Keyframe Süreklilik Kontrolü:** Zincirleme I2V üretkenliğinde, önceki sahnenin son karesindeki (Frame B) baskın geometrik matris yeni sahnenin (Frame A) ilk karesi olarak birebir sabitlenmelidir.   
9. **Negatif Kalkan Zenginleştirmesi:** Her mimari öğe için karşıt tipoloji negatif istem kalkanına eklenmelidir (örneğin beşik çatı için negatif: hip roof, pyramid roof, mansard) [[VARSAYIM | analiz | Analiz - DERS 80]].
10. **Metin Kodlayıcı EOS Sıkıştırma Denetimi:** Metin istemleri 75 token sınırının altında tutularak CLIP/T5 <EOS> gömmelerindeki semantik çakışma ve sızma riski en aza indirilmelidir [[ÖLÇÜLDÜ | akademik | arXiv:2412.04715]].
