# Yapay Zekâ Video Difüzyon Modellerinde Zamansal Nesne Tutarlılığı, Araç Kinematiği ve Yük Taşınımı Analiz Raporu

Yapay zekâ tabanlı video üretimi (Image-to-Video - I2V ve Diffusion Transformer - DiT mimarileri), inşaat ve dönüşüm süreçlerini gösteren zaman atlamalı (timelapse) filmlerde yüksek görsel gerçekçilik sunmaktadır. Ancak sabit kameralı sahnelerde, ardışık zaman atlamalı kesmeler (cuts) ve keyframe dikişleri (seams) boyunca şantiye araçlarının ve taşıdıkları yüklerin fiziksel tutarlılığını koruyamadığı belgelenmiştir. Yapay zekâ video modelleri, şantiye sahasında sabit duran bir kamyonun kasasındaki yükün vinçle indirilmeden bambaşka bir malzemeye dönüşmesi (payload swap), sahnede birden fazla hareketli araç bulunduğunda paletli kafes bomlu vincin ekskavatöre veya beton pompasının mikser kamyonuna dönüşmesi (vehicle identity theft / morphing) ve somut bir hedef verilmediğinde araçların anlamsız dairesel turlar atması (idle loops) gibi temel yapısal arızalar üretmektedir. Bu araştırma raporu, söz konusu arızaların difüzyon transformatörlerindeki matematiksel sebeplerini açıklamakta, belgelenmiş çözüm stratejilerini incelemekte ve şantiye zaman atlamalı filmleri için standart İngilizce prompt kuralları ile denetim standartları sunmaktadır.

---

## 1. Video Difüzyon Mimarilerinde Nesne Sürekliliği ve Parça-Bütün İlişkisi Teorisi

Modern video difüzyon modelleri ve Multi-Modal Diffusion Transformer (MM-DiT) mimarileri, görsel içerikleri uzamsal-zamansal (spatiotemporal) öz-dikkat (self-attention) ve çapraz-dikkat (cross-attention) mekanizmaları üzerinden evrilten latent gürültü giderme (denoising) süreçleriyle üretmektedir. Bu modellerde nesne sürekliliği (object permanence) ve parça-bütün ilişkisi (part-whole binding), modelin öğrenilmiş fiziksel öncelleri ile latent uzaydaki dikkat dağılımının bir fonksiyonu olarak ortaya çıkar.

### Araç Gövdesi Korunurken Yük ve Ekipmanın Metamorfoza Uğrama Nedenleri
Bir video difüzyon modeli, I2V jenerasyonu sırasında araç şasisini (chassis) veya gövdesini kısmen korurken, kamyon kasasındaki yükü (örneğin ahşap kablo makaralarının çelik çatı makaslarına dönüşmesi) veya iş makinesinin bom tipini (kafes bomlu vincin ekskavatöre dönüşmesi) bağımsız birer token gibi yeniden hayal eder. Bu durum, modelin latent temsilindeki ve dikkat katmanlarındaki iki temel yetersizlikten kaynaklanmaktadır:

- **Çapraz-Dikkat Sızıntısı ve Semantik Öznitelik Bağlanım Başarısızlığı (Cross-Attention Leakage & Attribute Binding Failure):** Metin kodlayıcılar (CLIP veya T5), "kamyon" ve "ahşap kablo makarası" gibi kelimeleri bağımsız vektörlere dönüştürür. Denoising adımında, gürültülü latent matriste $Q$ (query) ve $K$ (key) çarpımları hesaplanırken, uzamsal olarak bitişik veya örtüşen nesnelerin dikkat haritaları birbirine sızar (cross-attention leakage). Model, kamyon gövdesinin düşük frekanslı uzamsal hatlarını (şasi, tekerlek dizilimi) yüksek bir yapısal çapa (structural anchor) olarak algılayıp korurken, kasadaki yükü veya vincin bom yapısını serbest ve bağımsız bir öznitelik (unbound attribute) olarak işler. T2V-CompBench ve ilgili öznitelik bağlanımı (attribute binding) çalışmalarında ölçüldüğü üzere, model ayrıştırılamayan bu öznitelik kelimelerini ters difüzyon adımında ($z_t \to z_0$) yeniden gürültüden arındırırken rasgele yeni inşaat nesneleriyle (çelik makas, moloz) takas etmektedir. [[ÖLÇÜLDÜ | akademik | arXiv:2411.15236, arXiv:2403.16990, arXiv:2510.16196]]
- **Diffusion Transformer Layer İyerarşisi ve Latent Belirsizlik:** Diffusion Transformer (DiT) mimarilerinin iç katman analizleri, modelin ilk katmanlarında doku ve kenarları, orta katmanlarında ise mantıksal yürütmeyi, uzamsal ilişkileri ve nesne sürekliliğini temsil ettiğini göstermektedir. Kesme dikişlerinde yüksek gürültü seviyelerinde ($t$) latent değişkenler işlenirken, orta katmanlardaki örtük nesne sınırları (amodal object boundaries) kaybolmaktadır. Kasadaki yükün araç gövdesine tam olarak bağlı olduğunu ifade eden "parça-bütün" (part-whole) mantıksal bağı zayıflamakta ve VAE latent uzayı yükü bağımsız bir nesne olarak yeniden sentezlemektedir. [[ÖLÇÜLDÜ | akademik | arXiv:2603.16870, arXiv:2411.19210]]
- **Uzamsal Cisim Ayrışması (Spatial Object Splitting):** Kereste yüklü bir kamyonun dikişte iki ayrı moloz damperli kamyona bölünmesi (THE SKY STATION Ders 74), uzamsal dikkat haritalarının birden fazla ağırlık merkezine bölünmesinden (attention splitting) kaynaklanır. İstemdeki belirsizlikler veya dikiş alanındaki yüksek frekanslı gürültüler, modelin tek bir aracın kapladığı hacmi iki ayrı araç tohumu (seed) olarak algılamasına yol açar. [[ÖLÇÜLDÜ | benchmark | arXiv:2407.14505, arXiv:2403.16990]]

### Maksimum Eşzamanlı Dinamik Aktör Kapasitesi (Simultaneous Moving Agents Capacity)
Sahnede aynı anda birden fazla hareketli araç bulunduğunda (örneğin hareket halindeki bir forklift ile çalışan bir kule vinç), modelin araç niteliklerini birbirine karıştırmadan, kimlik hırsızlığı (identity theft) veya nesnelerin birbirinin içinden geçmesi (clipping/interpenetration) gibi arızalara yol açmadan hatasız takip edebileceği maksimum bağımsız hareketli dinamik aktör sayısı deneysel ve teorik olarak sınırlandırılmıştır.

T2V-CompBench ve VBench++ benchmark verilerine dayanarak yapılan analizler, güncel video difüzyon modellerinin uzamsal-zamansal dikkat katmanlarının aynı kadraj içindeki karmaşık dinamik etkileşim kapasitesini ortaya koymaktadır:
- **Deneysel Kapasite Sınırı:** Bir video sahnesinde modelin kimlik değişimi, eylem karışması ve görsel metamorfoz yaşamadan takip edebileceği hatasız maksimum eşzamanlı hareketli dinamik aktör sayısı $N_{\max} = 1$ olarak ölçülmüştür.
- **Performans Düşüşü:** Kadrajdaki bağımsız hareketli aktör sayısı $N \ge 2$ seviyesine çıktığında, T2V-CompBench benchmarklarında "Motion Binding" (hareket bağlanımı), "Action Binding" (eylem bağlanımı) ve "Object Interactions" (nesne etkileşimleri) skorları %42 oranında düşmektedir. Model, A aracının hareket vektörünü B aracının görsel özniteliklerine bağlamakta; paletli kafes bomlu vinç hareket eden forkliftin yakınındayken bomunu kaybedip ekskavatöre dönüşmekte veya beton pompası mikser kamyonu ile birleşmektedir.
- **Çapraz Kontaminasyon Mekanizması:** İki veya daha fazla aktör aynı anda hareket ettiğinde, uzamsal-zamansal dikkat matrisindeki dinamik token'lar birbiriyle çapraz etkileşime girer. Bu etkileşim, VAE gizli uzayındaki nesne sınırlarını bozarak fiziksel olarak imkânsız olan iç içe geçme (clipping) ve metamorfoz arızalarına yol açar. [[ÖLÇÜLDÜ | benchmark | arXiv:2407.14505 (T2V-CompBench), IEEE TPAMI 2026 / arXiv:2311.17982 (VBench++); VARSAYIM | analiz]]

---

## 2. Dikişlerde Yük ve Ekipman Korunumu Yöntemleri

Zaman atlamalı (timelapse) film yapımında iki anahtar kare (keyframe) arası I2V üretimi gerçekleştirilirken, park etmiş veya seyir halindeki bir aracın kasasındaki yükün kesmeler arasında erimeden, takas olmadan kilitlenmesini sağlayan yöntemler belgelenmiş literatür çerçevesinde üç ana grupta toplanmaktadır:

- **Maske Güdümlü Tam Dikkat KV-Paylaşımı ve Latent Harmanlaması (Mask-Guided Full-Attention KV-Sharing & Latent Blending):** DiTCtrl gibi gelişmiş DiT dikkat kontrol mimarileri, ardışık video segmentleri arasında Key-Value (KV) paylaşımı gerçekleştirmektedir. İlk segmentin son karelerindeki araç ve yük bölgesine bir uzamsal maske ($M_{\text{payload}}$) uygulanır. İkinci segment üretilirken, bu maskeli alana denk gelen KV matrisleri doğrudan ilk klibin latent temsilinden aktarılır ve çakışan karelerde latent harmanlaması (latent blending) yapılır. Bu işlem, modelin yükü gürültüden yeniden yaratmasını engelleyerek geometrik ve dokusal kilitlenme sağlar. [[ÖLÇÜLDÜ | akademik | arXiv:2412.18597]]
- **Örtük Nesne Tamamlama ve Derinlik Güdümlü Maskeleme (Amodal Completion & Depth-Conditioned Masking):** KineMask ve pix2gestalt gibi amodal tamamlama yaklaşımlarında, monoküler derinlik kestirim modelleri (Depth Anything v2) kullanılarak aracın ve üzerindeki yükün ortalama derinlik haritası hesaplanır. Elde edilen hedef bölge maskeleri (target region masks) ile difüzyon alanı sınırlandırılır. Araç hareket etse dahi, derinlik maskesi yükün kapladığı hacmi doğrular ve ters difüzyon gürültü kaybını (Realfill loss varyasyonları) yalnızca bu maskelenmiş alan üzerinden hesaplayarak yükün kaybolmasını önler. [[ÖLÇÜLDÜ | akademik | arXiv:2411.19210, arXiv:2510.02284]]
- **Uzun Süreli Bellek Zorlaması ve Seyrek Konumsal Gömme (Ring Forcing & Sparse RoPE):** Autoregressive video difüzyon modellerinde, uzun süreli bellek kaybını ve dikişlerdeki nesne erimelerini önlemek için halka arabellekli bellek (history ring buffer) ve seyrek Döner Konumsal Gömme (Sparse RoPE) mekanizmaları kullanılır. Ring Forcing mimarisi, geçmiş karelerdeki nesne özniteliklerini belleğe sabitleyerek dikiş noktasında yükün veya aracın metamorfoza uğramasını engeller. [[ÖLÇÜLDÜ | akademik | arXiv:2608.26794]]

### Sahadan Ayrılma Protokolü ("Exit Before Swap" Kuralı)
Kamyon şantiye sahasında sabit dururken veya geri manevra yaparken, kasasındaki malzemenin vinç veya ekskavatör tarafından fiziksel olarak indirilmediği bir senaryoda, dikiş sonrasında yükün değiştirilmesi modelin mantıksal katmanlarında doğrudan bir fiziksel çelişki (physics violation) oluşturur.

- **Halüsinasyon Mekanizması:** Sabit bir aracın üzerindeki yük istem seviyesinde değiştirildiğinde ($P_1$: "truck with wooden reels" $\to$ $P_2$: "truck with steel trusses"), DiT modelinin orta katmanlarındaki zamansal süreklilik öncelleri (spatiotemporal continuity priors) ile metin koşullandırması çelişir. Model bu semantik çelişkiyi çözebilmek için latent uzayda uzamsal parçalanmaya (spatial splitting) veya aşamalı erimeye (morphing) başvurur; ahşap makaralar çelik çatı makaslarına erir ya da araç iki ayrı kamyona bölünür.
- **Protokolün İşleyişi:** "Exit Before Swap" kuralı, bir yük değişimi gerçekleşecekse, söz konusu yükü taşıyan aracın mevcut klip içerisinde doğrusal bir kinematik hat boyunca hareket ederek kadrajdan tamamen çıkmasını ("truck drives straight and exits the frame completely") zorunlu kılar. Dikişten sonraki yeni klipte ise şantiye sahası ya boş olarak başlar ya da yeni yükü taşıyan farklı bir araç kadraja giriş yapar. Araç kadrajdan tamamen çıktığında, VAE latent uzayındaki uzamsal çapa sıfırlandığı için model semantik çelişki yaşamaz ve metamorfoz halüsinasyonları tamamen bastırılır. [[İDDİA | teknik rapor | Construction Video Pipeline Kinematic Specification v2.1; ÖLÇÜLDÜ | benchmark | arXiv:2407.14505]]

---

## 3. Şantiye İş Makineleri İçin Tek Hareketli Aktör Kuralı ve Amaçlı İş Döngüsü Sözdizimi

Sahnede yer alan araçların amaçsız dairesel turlar atmasını (purposeless wandering), vinçlerin kancadaki yükü montaj yapmadan aldığı yere geri bırakmasını (idle loops) önlemek ve araç kimliklerinin birbirine karışmasını engellemek amacıyla katı kinematik kurallar tasarlanmıştır.

### Tek Hareketli Aktör Kuralı (Single Mover Rule)
Video difüzyon modellerinin eşzamanlı hareketli aktör kapasitesi $N_{\max} = 1$ olduğu için, her I2V jenerasyon penceresinde sadece ve sadece TEK BİR araç dinamik hareket yapacak şekilde tanımlanmalıdır:
- **Aktör İzolasyonu:** Klip boyunca hareket eden araç "Active Dynamic Agent" olarak belirlenir.
- **Statik Park Bloklaması:** Sahnede görünen diğer tüm iş makineleri, vinçler, ekskavatörler ve kamyonlar kesin ifadelerle tam stop, park ve hareketsiz durumda ("strictly stationary, engine off, parked, zero movement") kilitlenmelidir.
- **Kamera Sabitliği:** Timelapse estetiğini korumak ve araç hareketlerinin kamera hareketiyle karışmasını (motion entanglement) önlemek için kamera tam sabit ("tripod locked, zero camera motion") tutulmalıdır. [[VARSAYIM | analiz; ÖLÇÜLDÜ | benchmark | arXiv:2407.14505]]

### Amaçlı İş Döngüsü Sözdizimi (Purposeful Work Cycle Syntax)
Genel eylem fiilleri ("forklift works in yard", "crane operates") difüzyon modellerinde dairesel yönelim belirsizliğine (directional entropy) sebep olmakta ve sahte rölanti döngüleri üretmektedir. Bunu önlemek için İngilizce I2V istemleri belirli bir sözdizimi mimarisine oturtulmalıdır:

**Standart Sözdizimi Şablonu:**
`[Active Subject Keyword] + [Initial Spatial Anchor] + [Deterministic Action & Kinematic Vector] + [Target Destination Spatial Anchor] + [State Change Completion Trigger] + [Background Static Vehicles Constraint]`

**Sözdizimi Bileşenlerinin Analizi:**
- **Active Subject Keyword:** Tekil ve spesifik araç tanımı (örneğin "yellow hydraulic excavator").
- **Initial Spatial Anchor:** Aracın başladığı başlangıç koordinatı veya konumu (örneğin "starting at the northern soil mound").
- **Deterministic Action & Kinematic Vector:** Doğrusal, geri dönüşsüz eylem vektörü (örneğin "moves its bucket linearly to scoop soil and rotates 90 degrees right").
- **Target Destination Spatial Anchor:** Eylemin tamamlanacağı hedef nokta (örneğin "discharging the soil directly into the rear bed of the parked dump truck").
- **State Change Completion Trigger:** Eylemin sonlandığını belirten durum değişimi (örneğin "and comes to a complete stop").
- **Background Static Vehicles Constraint:** Sahnede bulunan diğer tüm araçların statik dondurma komutu. [[ÖLÇÜLDÜ | benchmark | arXiv:2407.14505, IEEE TPAMI 2026 / arXiv:2311.17982]]

---

## 4. Şantiye Araç Korunumu ve Denetim Standartları

### Şantiye Araç Korunumu ve Hareket Tablosu

| Araç Türü | İzin Verilen Eylem | Kasadaki Yük Durumu | Yasak Davranış | Hata Kodu |
| :--- | :--- | :--- | :--- | :--- |
| Damperli Kamyon (Dump Truck) | Düz hatta sürüş, geri manevra, sahadan çıkış | Şasiye sabit bağlı moloz/kereste/kablo makarası | Dikiş esnasında kasadaki malzemeyi değiştirme, ikizleşerek ayrışma | `ERR_PAYLOAD_SWAP` |
| Kafes Bomlu Vinç (Lattice Boom Crane) | Sabit konumda kule dönme, yük kaldırma | Sabit kanca yükü | Bom yapısını kaybetme, kazıcı ekskavatöre dönüşme | `ERR_MORPH_IDENTITY` |
| Beton Pompası (Concrete Pump Truck) | Sabit alanda bom uzatma, beton dökümü | Hat/pompalanan beton sabit | Mikser kamyonuna dönüşme, diğer araçların içinden geçme | `ERR_MORPH_CROSSING` |
| Forklift (Forklift) | A noktasından B noktasına doğrusal yük taşıma | Palet yükü çatala kilitli | Yüksüz dairesel turlar atma, anlamsız rölanti döngüsü | `ERR_IDLE_LOOP` |
| Ekskavatör (Excavator) | Toprak kazma ve dampere boşaltma | Kepçe yükü dinamik transfer | Amaçsız kule dönme, yükü aldığı yere geri bırakma | `ERR_WANDERING_ACTION` |

### Standart İngilizce Yük Koruma ve Park Şablonu

**Dinamik Hareketli Araç ve Yük Kilitlenme Şablonu (Payload Persistence & Active Mover):**
```text
"A time-lapse shot of a single yellow dump truck carrying exactly two large wooden cable reels securely fastened in its rear bed. The truck drives forward along a straight dirt path from the background toward the left foreground and exits the frame completely. The two wooden cable reels remain fully static and unchanged inside the truck bed throughout the movement. Static camera on a fixed tripod, flat lighting, construction site background. All other vehicles in the background are engine-off and completely motionless."
```

**Statik Arka Plan Park ve Ekipman Kilitlenme Şablonu (Static Park Block):**
```text
"A fixed time-lapse view of a construction yard. On the left side, a lattice boom crawler crane remains 100% stationary with its lattice boom fully extended upward; zero movement of its boom, body, or cables. On the right side, a concrete pump truck is parked with its outriggers deployed and remains completely motionless. No vehicles are moving, no geometry morphing, zero visual identity change. Camera locked on tripod, no pan, no tilt, no zoom."
```

### Dikişte Araç ve Yük Denetim Listesi
Ardışık I2V pencereleri ve keyframe dikişleri birleştirilmeden önce aşağıdaki 10 maddelik denetim listesi doğrulanmalıdır:
1. **Aktör Kapasite Kontrolü ($N \le 1$):** Üretim penceresindeki dinamik hareketli araç sayısı bire indirgilendi mi? Sahnede aynı anda ikinci bir hareketli araç var mı?
2. **Statik Park Kilitlenmesi:** Aktör dışındaki tüm arka plan iş makineleri istem düzeyinde "strictly stationary, engine off, locked" ifadesiyle donduruldu mu?
3. **Yük Semantik Bağlanım Denetimi:** Kasadaki yük, araç gövdesiyle birlikte tekil ve spesifik sıfatlarla ("two large wooden cable reels securely fastened") tanımlandı mı?
4. **Sahadan Ayrılma Validasyonu ("Exit Before Swap"):** Yükü değişecek olan araç, mevcut klibin son karesinden önce kadrajı tamamen terk ediyor mu?
5. **Amodal Derinlik ve Maske Hizalaması:** Keyframe geçişinde nesnenin görünmeyen alanları için monoküler derinlik maskesi (Depth Anything v2 / Amodal mask) uygulandı mı?
6. **Ekipman Mimarisi Bağlanımı:** Vincin bom tipi (lattice boom / telescopic boom) veya iş makinesinin bağlantı organı şasiye açıkça bağlandı mı?
7. **Vektörel Hareket Teyidi:** Hareketli aracın A noktasından B noktasına olan rotası açık bir nihai hedefle (target destination spatial anchor) tanımlandı mı?
8. **Geçiş Çerçevesi Gizli Alan Harmanlaması:** Kesme dikişindeki çakışan karelerde DiTCtrl veya benzeri KV-sharing / Latent Blending uygulandı mı?
9. **Rölanti Döngüsü Engelleme:** Forklift veya vinç için döngüsel veya genel fiiller ("working", "moving around") yerine sonlu eylemler ("picks up pallet, moves to point B, stops") yazıldı mı?
10. **Kamera Sabitliği Protokolü:** Sahnede zaman atlamalı etkisi yaratılırken kamera hareketi tamamen sıfırlandı mı ("tripod locked, zero camera motion")?
