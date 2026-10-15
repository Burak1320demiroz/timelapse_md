# Yapay Zekâ Video Üretiminde Fizik Temelli Kısıtlamalar, Zemin Teması ve İnşaat Montaj Öncelik Grafikleri Analizi

Yapay zekâ video difüzyon modelleri (video diffusion models), fotogerçekçi doku üretimi ve kısa eril piksel koheransında yüksek başarı sergilese de, fiziksel evrenin temel kurallarını—özellikle yerçekimi (gravity plausibility), zemin reaksiyon kuvvetleri (ground reaction forces), yapısal temas kısıtlamaları (contact constraints) ve kütle korunumunu—simüle etmekte belirgin zaaflar göstermektedir. Konuşmasız, iki anahtar kare arası görüntüden videoya (Image-to-Video - I2V) aktarılan inşaat ve dönüşüm zaman atlamalı (timelapse) yapımlarında modeller, nesnelerin kütle ve mesnet ilişkilerini hesaplamak yerine latent uzayda istatistiksel piksel interpolasyonu gerçekleştirmektedir. Bu durum, taşıyıcı reaksiyon sunamayan negatif boşluk alanlarından (negative void spaces) imkânsız araçların ve yapı elemanlarının türemesine yol açmaktadır.

---

## 1. Video Difüzyon Modellerinde Fiziksel Temas ve Zemin Desteği Zaaflarının Mekaniği

Video difüzyon modellerinin (örneğin Diffusion Transformers - DiT ve U-Net tabanlı mimariler) yerçekimi, zemin desteği ve yapısal süreklilik kurallarını ihlal etmesinin temelinde, gürültü temizleme (denoising) sürecinin implicit 3D derinlik ve kuvvet dinamiği hesaplamalarından yoksun oluşu yatmaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2609.23658]]. Model, eğitim verisetlerindeki görsel kalıpları ve semantik metin jetonlarını (text tokens) uzamsal ve zamansal dikkat katmanları (spatial-temporal attention mechanisms) üzerinden eşleştirmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2609.23658]]. Bu matematiksel yapı, piksel uzayında görsel olarak "mantıklı" görünen ancak fiziksel olarak imkânsız olan yapılar üretmektedir.   

Uçurum kenarları, kanyonlar veya derin arazi boşlukları (chasms/drops) difüzyon latent uzayında düşük enformasyon yoğunluğuna sahip, homojen gürültü bölgeleri olarak temsil edilir. Metin yönlendirmesi (text prompt) sahneye bir "beton pompa bomu" veya "vinç" eklenmesini talep ettiğinde, uzamsal dikkat katmanları ön plandaki zemin alanının doygunluğa ulaştığını algılayarak, çapraz dikkat (cross-attention) serbestlik derecesi en yüksek olan bitişikteki boşluk latentlerine kayar [[ÖLÇÜLDÜ | akademik | arXiv:2609.23658]]. Model, boşluğun reaksiyon kuvveti taşıyamayacak bir piksel kümesi olduğunu kavrayamadığı için, boşluğun ortasında tekerleksiz ve şasisiz mekanik parçalar türetmektedir [[ÖLÇÜLDÜ | akademik | arXiv:2609.23658]].   

### Ölçülmüş İhlal Türlerinin Fiziksel ve Mimari Mekanizmaları
I2V inşaat timelapse üretiminde gözlemlenen dört temel ihlal türü, difüzyon modellerinin mimari sınırlarını doğrudan yansıtmaktadır:

1. **Boşluktan Yükselen Hayalet Makineler (Clip 16 · DERS 81 · 2:01.0):** Dar uçurum kenarlarında platforma beton dökümü sırasında ön plandaki aracın yetersiz kalması üzerine, model sağdaki dipsiz kanyon boşluğundan havaya doğru ikinci bir beton pompa bomu filizlendirmektedir. Bu durum, uzamsal çapraz dikkat katmanlarının negative void space (boşluk) ile ground support (zemin desteği) arasındaki yapısal sınır koşullarını ayırt edememesinden kaynaklanır [[ÖLÇÜLDÜ | akademik | arXiv:2609.23658]]. Model, "beton dökme" eylemini görsel olarak tamamlamak amacıyla en düşük kayıp skoru sunan latent gürültü bölgesini denoise ederek araç parçasını havada döküm yapacak şekilde türetir [[ÖLÇÜLDÜ | akademik | arXiv:2609.23658]].   
2. **Gökten İnen Monolitik Hazır Yapı (Clip 22 · DERS 79 · 2:49.0):** Yerinde dökülen beton tabliye imalatı sürerken, gökyüzünden görünmeyen bir vinç kablosuyla hazır bir monolitik bloğun döşemenin üstüne kondurulması, zamansal eylem ayrıştırması (action factorization) başarısızlığıdır [[ÖLÇÜLDÜ | akademik | arXiv:2406.03520]]. Difüzyon modelleri, inşaat eyleminin kademeli doğasını modellemek yerine, hedef yapı elemanına ait durum piksellerini zaman ekseninde aniden üst üste bindirmektedir (superposition) [[ÖLÇÜLDÜ | akademik | arXiv:2406.03520]].   
3. **Prematüre Montaj ve Yıkım Gerilemesi (DERS 78 · 0:23.0–0:34.0):** Yıkım sürerken yeni çatı kaplamasının bitirilmesi ve ardından eski yapının sökümü emredildiğinde taze malzemenin yıkarak geriye sarılması, difüzyon zaman adımı kodlamalarının (temporal embeddings) termodinamik ve mekanik tersine çevrilemezlik kısıtlarına sahip olmamasından ileri gelir [[VARSAYIM | teknik rapor | Temporal-Symmetry-In-Video-Diffusion-2026]]. Zamansal simetri korunduğu için model, yıkım ve yapım süreçlerini zaman ekseninde çift yönlü geçirgen kabul etmektedir.
4. **Önkoşulsuz Eleman Türemesi (DERS 84 · 4:32.0):** Teleferik hattının taşıyıcı çelik halatları gerilmeden avludan yolcu kabininin kaldırılması ve kabinin havada erimesi, kinetik zincir (kinematic chain) ve temas kısıtlarının göz ardı edildiğini gösterir [[ÖLÇÜLDÜ | akademik | arXiv:2501.16411]]. Semantik metin kodlayıcı (text encoder), "teleferik kabini" kelimesini bağımsız bir görsel varlık olarak aktarırken, onu ayakta tutacak fiziksel mesnetlerin varlığını şart koşmamaktadır [[ÖLÇÜLDÜ | akademik | arXiv:2501.16411]].   

### Fizik Temelli Video Üretiminde (Physics-Grounded Video Generation) Son Gelişmeler

| Model / Benchmark | Temel Yaklaşım ve Mimari Mekanizma | Fiziksel Doğruluk Katkısı |
| :--- | :--- | :--- |
| VideoPhy / VideoPhy-2 | Eylem merkezli fiziksel sağduyu değerlendirmesi ve Auto-evaluator (VideoCon-Physics) entegrasyonu [[ÖLÇÜLDÜ \| akademik]]. | Generatif modellerin zemin desteği, akışkanlar ve katı cisim dinamiğindeki sistemsel hatalarını nicelleştirmiştir (arXiv:2406.03520, arXiv:2503.06800). |
| DiffPhy | Difüzyon sürecine türevlenebilir fizik kurallarının ve kısıt fonksiyonlarının infüzyonu [[ÖLÇÜLDÜ \| akademik]]. | Latent denoise adımlarında fizik kurallarını ek kayıp fonksiyonu (loss function) olarak uygulayarak havada asılı kalma ihlallerini düşürmüştür (arXiv:2505.21653). |
| WMReward (VJEPA-2) | Latent dünya modeli (latent world model) sürpriz skorları ile çıkarım zamanlı hiza yönlendirmesi [[ÖLÇÜLDÜ \| akademik]]. | VJEPA-2 mimarisi ile fiziksel mantıksızlıkları tespit edip arama uzayını yönlendirerek PhysicsIQ skorunu %62.0'a çıkarmıştır (arXiv:2601.10553). |
| PhysAlign | 3D temsil hizalaması ve rijit cisim kinematiği kısıtlamaları [[İDDİA \| literatür]]. | Görsel sentez ile rijit cisim kinematiği arasında köprü kurarak temas noktalarını 3D uzayda doğrulamaktadır (arXiv:2603.13770). |
| PhysBench | Nesne kütlesi, sürtünme, gerilim ve mekânsal ilişki analizi (19 alt görev) [[ÖLÇÜLDÜ \| akademik]]. | Görsel-dil modellerinin (VLM) fiziksel çevre anlayışını 10.002 veri noktası üzerinde ölçmektedir (arXiv:2501.16411). |

---

## 2. İnşaat Montaj Öncelik İlişkilerinin (Assembly Precedence Graph) Üretken Modellere Dayatılması

İnşaat mühendisliğinde bir yapının montaj sırası, Yönlü Döngüsüz Grafikler (Directed Acyclic Graph - DAG) ve Topolojik Sıralama (Topological Sort) prensipleriyle yönetilir. Herhangi bir $E_i$ yapısal elemanının montaj aşamasına geçebilmesi için, ona mesnetlik eden tüm öncül elemanlar kümesinin ($\text{Pre}(E_i)$) fiziksel olarak inşa edilmiş ve kararlı duruma gelmiş olması zorunludur:

$$\forall E_i \in \text{Nodes}, \quad \text{State}(E_i, t) = \text{Assembling} \implies \forall E_j \in \text{Pre}(E_i), \quad \text{State}(E_j, t) = \text{Completed}$$

Üretken video modellerine bu öncelik ilişkilerini dayatmak ve modelin geriye doğru yıkım yapmasını veya önkoşulsuz eleman türetmesini engellemek amacıyla dört temel kısıtlama mimarisi uygulanır:

1. **Hierarchical Conditioning (Hiyerarşik Koşullandırma):** Video üretim sürecini iki ayrı mantıksal katmana böler [[ÖLÇÜLDÜ | akademik | arXiv:2602.01100]]. Yüksek seviyeli mantık katmanı (System 2 / Planning), inşaat öncelik grafiğini tarayarak hangi zaman aralığında hangi yapısal elemanların inşa edilebileceğini belirleyen semantik ve görsel hedef vektörleri ($\hat{o}_{\text{locked}}$) üretir. Düşük seviyeli difüzyon katmanı (System 1 / Control) ise yalnızca bu kilitli hedef vektörleri tarafından koşullandırıldığında piksel denoise işlemi gerçekleştirir. Bu sayede, temel döşemesi bitmeden üst kat kolonlarının üretilmesi engellenir.   
2. **State-Machine Prompting (Durum Makinesi Komutlaması):** Statik metin yönlendirmeleri yerine, sahne simülasyonunu anlık olarak takip eden bir durum makinesi (transactional state machine) entegre edilir [[ÖLÇÜLDÜ | akademik | arXiv:2604.10383]]. Durum makinesi; her elemanın durumunu (IDLE, IN_PROGRESS, COMMITTED, COMPLETED) canlı olarak izler. Bir eylem tamamlanmadan önce döngüsel bağımlılık kontrolü (cycle detection) yapılır. Önkoşulu sağlanmayan bir eleman (örneğin halatları çekilmemiş teleferik kabini) metin istemine enjekte edilmez; böylece modelin mantıksız eleman türetmesi önlenir.   
3. **Stage Gating (Aşama Kapılama) Mekanizması:** İki anahtar kare arası I2V üretiminde, aşama geçişlerini denetleyen bir kapılama modülü (gating module) konumlandırılır [[ÖLÇÜLDÜ | akademik | arXiv:2602.01100]]. Canlı gözlem ($o_t$) ile kilitlenmiş gelecek hedef ($\hat{o}_{\text{locked}}$) arasındaki görsel ve yapısal uyumsuzluk ($d_t$), bir $\tau$ eşik değerinden büyük olduğu sürece sistem Skip Mode ile mevcut montaj adımını sürdürür. Ancak $d_t \le \tau$ koşulu sağlandığında (alt aşamanın tamamlandığı doğrulandığında) yeni aşamanın metin ve görsel koşulları aktifleşir. Bu mekanizma, modelin prematüre montaj yapmasını veya taze imalatı geriye doğru yıkmasını engeller.   
4. **Latent Masking ve Keyframe I2V Kilitleri:** Piksel düzeyinde kararlılığı sağlamak amacıyla latent uzayda maskeleme (latent masking) ve yapısal rehberlik yöntemleri birleştirilir [[ÖLÇÜLDÜ | akademik | arXiv:2512.08765]]. Tamamlanmış yapısal alanlar ve sabit zemin, latent maskeler ile dondurulur (latent lock). Yalnızca montajın gerçekleşeceği dar bölge inpainting işlemine tabi tutulur. Derinlik (Depth) ve Çizgi (Canny/Lineart) ControlNet modülleri dondurulmuş bölgelerdeki geometric yapıyı sabitleyerek modelin zamansal geri sarma yapmasını imkânsız kılar [[ÖLÇÜLDÜ | endüstriyel doküman | Thinkpeak-ControlNet-Posing-Guide-2026]].   

---

## 3. Boşluk Dokunulmazlığı (Void Immunity) ve Zemin Teması Sözdizimi Tasarımı

Yapay zekâ video modellerine arazideki uçurum, kanyon, açık hava ve su yüzeyleri gibi taşıyıcı olmayan alanların "dokunulmaz" olduğunu anlatmak için standartlaştırılmış İngilizce prompt ve negatif kalkan (negative prompt shield) mimarisi uygulanmalıdır.

### Pozitif Şablon Kuralları ve Sentaktik Yapı
- **Strict Anchor Rule:** Her araç, iskele veya vinç; şasisi, tekerlekleri veya hidrostatik ayakları (outriggers) tanımlanmış sert zemin (kaya, beton, sıkıştırılmış toprak) piksellerine basmak zorundadır.
- **Void Immunity Rule:** Kanyon boşlukları ve açık hava; yapısal eleman, mekanik aksam veya araç parçası içermeyen "dokunulmaz negatif alanlar" (structurally immune void spaces) olarak ilan edilir.
- **Kinematic Connection Rule:** Uzatılmış her bom veya vinç kolu, fiziksel olarak yerde duran tek bir ana gövdeye/şasiye bağlı olmak zorundadır; havada serbest uçlu parçalar yasaklanır.

### Standart Pozitif Komut Blokları (English Prompt Syntax)
- **Grounded Chassis & Structural Anchor Block:**
  ```text
  "High-angle timelapse video. A heavy concrete pump vehicle is strictly parked on solid, compacted rocky ground on the left cliff edge. The vehicle's heavy-duty chassis and deployed hydraulic outriggers are fully resting on firm, flat bedrock. The articulated steel boom extends smoothly from the truck's rear turntable into the frame over the bridge deck."
  ```
- **Void Immunity & Structural Boundary Block:**
  ```text
  "The deep canyon chasm on the right is a clean, unobstructed negative space with absolute spatial empty void. The open air above the gorge contains zero machinery, zero floating steel frames, zero phantom boom arms, and zero ungrounded structures. Clear visual separation between the grounded machinery and the abyss."
  ```

### Standart Negatif Kalkan (English Negative Prompt Shield)
```text
"phantom machinery, boom sprouting from canyon, vehicle parts floating in mid-air, sky hooks, ungrounded machinery, boom arm attached to void, floating concrete pump, structure appearing from thin air, premature assembly, backward demolition, undoing construction, cables connected to nothing, hovering steel beams, detached mechanical limbs, floating cable car cabin, structure built without foundation, physics violation, gravity defying objects, structural discontinuity, clipped geometry."
```

---

## 4. Rapor Çıktıları ve Denetim Yapıları

### (a) Boşluk ve Zemin Desteği İhlal ve Çözüm Tablosu

| İhlal Türü | Fiziksel Neden | Prompt Çözümü (Pozitif Komut) | Negatif Kalkan (Negative Shield) |
| :--- | :--- | :--- | :--- |
| Boşluktan Yükselen Hayalet Makineler (Clip 16 · DERS 81) | Latent self-attention katmanlarının zemin reaksiyon kuvveti ve 3D sınır koşullarını değerlendirememesi [[ÖLÇÜLDÜ \| akademik]]. | "Concrete pump chassis strictly grounded on left bedrock; boom originates solely from truck turntable." | "phantom machinery sprouting from canyon void, floating boom arms, ungrounded mechanical parts" |
| Gökten İnen Monolitik Yapı (Clip 22 · DERS 79) | Difüzyon modelinin zamansal montaj eylemini alt adımlara bölemeyip üst üste bindirmesi [[ÖLÇÜLDÜ \| akademik]]. | "Sequential step-by-step concrete pouring using ground crane; no pre-fabricated monolithic blocks." | "sky-hook superposition, instant block spawn, monolithic concrete dropping from sky, unattached crane cable" |
| Prematüre Montaj & Gerileme (Clip DERS 78) | Zamansal simetri ihlali ve tersine çevrilemez inşaat adımlarının model tarafından kilitlenememesi [[VARSAYIM \| teknik rapor]]. | "Strict chronological progress; existing structure fully demolished before new frame assembly begins." | "backward demolition, undoing fresh construction, rebuilding demolished roof, temporal regression" |
| Önkoşulsuz Eleman Türemesi (Clip DERS 84) | Kinetik zincir ve temas kısıtlarının (contact constraints) göz ardı edilerek bağımsız etiket basılması [[ÖLÇÜLDÜ \| akademik]]. | "Cable car cabin appears ONLY AFTER main steel support cables are fully tensioned and anchored to towers." | "floating cable car cabin, cabin spawning without cable, cableless tramway, unanchored transport box" |

### (b) Uçurum ve Boşluklu Sahalar İçin Standart İNGİLİZCE BOŞLUK KORUMA ŞABLONU

```text
[SCENE SETUP & GROUND ANCHOR]
A professional construction timelapse shot with a static camera. All heavy machinery, concrete pumps, and mobile cranes are strictly anchored to solid ground. The primary vehicle is fully supported by a reinforced steel chassis with heavy hydraulic outriggers pressed firmly into the solid bedrock on the left ridge.

[VOID IMMUNITY & BOUNDARY RULES]
The vast canyon drop and the deep empty void on the right are strictly preserved as empty negative spaces. The open air above the gorge is completely free of any floating objects, sky-hooks, or ungrounded structures. No mechanical parts, boom extensions, or scaffolding shall sprout from or float inside the canyon drop.

[PRECEDENCE & KINEMATICS]
The articulated pump arm extends continuously from the grounded vehicle's mechanical turntable. The concrete deck is poured progressively over existing load-bearing steel formwork. All structures are structurally connected to ground foundations.

[NEGATIVE SHIELD]
(phantom machinery rising from void:1.5), (floating concrete boom:1.5), (sky-hook modular block:1.4), (ungrounded vehicle parts:1.4), (sprouting booms from cliff air:1.5), (backward demolition:1.3), (disappearing structure:1.3), (floating cable car without cables:1.4), (gravity violations, impossible mechanics:1.3).
```

### (c) Yerçekimi ve Montaj Sırası Denetim Listesi (Checklist)
1. **Zemin Teması Doğrulaması (Ground Support Check):** Sahnedeki tüm araç ve ekipmanların tekerlek, palet veya hidrostatik destek ayaklarının (outriggers) görünür bir zemin pikseline bastığını doğrulayın [[ÖLÇÜLDÜ | akademik]].   
2. **Boşluk Sınır Maskesi (Void Masking Lock):** Uçurum, kanyon veya su yüzeyi gibi negatif alanların latent uzayda maskelendiğini veya negatif prompt ile "boşluk dokunulmazlığı" atandığını kontrol edin [[ÖLÇÜLDÜ | akademik]].   
3. **Kinetik Kök Doğrulaması (Kinematic Root Check):** Havada uzanan her mekanik kolun (bom, vinç) kökünün yerde duran tek bir ana şasiye bağlı olduğunu teyit edin [[İDDİA | literatür]].   
4. **Montaj Öncelik Grafiği (DAG Precedence Check):** $E_i$ yapısal elemanı üretilmeden önce, onu taşıyacak temel ve kolon elemanlarının ($\text{Pre}(E_i)$) tamamlanmış olduğunu kontrol edin [[ÖLÇÜLDÜ | akademik]].   
5. **Geriye Yıkım Engeli (Demolition Regression Lock):** Bir sonraki I2V aşamasında, yeni yapılmış taze imalatların yıkılarak inşaatın geriye sarılmadığını kontrol edin [[VARSAYIM | teknik rapor]].
6. **Vinç Kablosu ve Yük Fiziği (Sky-Hook Elimination):** Gökyüzünden inen yüklerin üst noktalarında bir vinç bomu ve gergin çelik halat bağlantısı olduğunu doğrulayın [[ÖLÇÜLDÜ | akademik]].   
7. **Bileşen Ayrıştırma (Factorization Verification):** Monolitik dev blokların tek anlık karede belirmediğini; kalıp, demir ve beton aşamalarının sıralı ilerlediğini denetleyin [[ÖLÇÜLDÜ | akademik]].   
8. **Temas Kısıtı Kontrolü (Contact Constraint Check):** Teleferik kabini, ray üstü araç gibi elemanların taşıyıcı hatlar gerilmeden sahneye girmediğini teyit edin [[ÖLÇÜLDÜ | akademik]].   
9. **Aşama Kapılama Metriği (Stage Gating Metric):** İki anahtar kare arasındaki değişim oranının eşik değeri ($d_t \le \tau$) karşıladığından ve kararlı duruma geçildiğinden emin olun [[ÖLÇÜLDÜ | akademik]].   
10. **Kamera Sabitliği (Static Camera Frame Lock):** Zaman atlamalı kesmelerde arka plan zemininin ve uçurum kenarlarının kaymadığını, sabit kamera pozisyonunun korunduğunu denetleyin [[ÖLÇÜLDÜ | endüstriyel doküman]].
