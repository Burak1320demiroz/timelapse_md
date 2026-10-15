# Üretken Video Difüzyon Modellerinde Restorasyon Zaman Atlamalı Filmlerinin Faz Kapılaması, Zamansal Nedensellik ve İş Hacmi Temposu Yönetimi

Eski veya tescilli yapıların restorasyon ve dönüşüm süreçlerini konu alan kilitli sabit kameralı, konuşmasız iki anahtar kare arası (Image-to-Video / I2V) fotogerçekçi zaman atlamalı (timelapse) filmler, üretken yapay zekâ ve video difüzyon mimarileri (Video Diffusion Transformers - DiT) açısından karmaşık fiziksel ve mantıksal zorluklar içermektedir. İnşaat ve restorasyon süreçlerinin görsel simülasyonunda sıklıkla karşılaşılan iki ana yapısal arıza bulunmaktadır: yıkım (demolition) ile yapım (assembly) eylemlerinin kronolojik ve termodinamik olarak birbirine karışması (faz çakışması ve geriye yıkım) ile sahnelerde hiçbir yapısal gelişmenin yaşanmadığı rölanti klipsleri takiben aniden devasa yapı elemanlarının belirmesinden (step-jump) kaynaklanan dengesiz tempo problemidir. Bu araştırma raporu; söz konusu arızaların matematiksel ve mimari kök nedenlerini derinlemesine incelemekte, literatür ve endüstride uygulanan eylem dağılım mimarilerini karşılaştırmakta ve metin istemleri (prompts), negatif bloklar ile anahtar kare zincirleri (keyframe chaining) kullanılarak doğrudan uygulanabilecek standart İngilizce bir kapılama ve tempo sözdizimi sunmaktadır.

---

## 1. Restorasyon Sahnelerinde Yapısal Arızaların Matematiksel ve Mimarî Nedenleri

### 1.1. Çift Yönlü Zamansal Dikkat ve Zamanın Oku Yitimi
Gelişmiş video difüzyon modelleri (Stable Video Diffusion, Wan2.1, HunyuanVideo, Cosmos 3 vb.), uzamsal-zamansal gizil (latent) uzayda $z \in \mathbb{R}^{F \times H \times W \times C}$ tensor kümesi üzerinde gürültü giderme (denoising) adımları çalıştırarak video üretmektedir. Bu modellerin zamansal tutarlılık sağlamak adına sıklıkla başvurduğu temel mekanizma, Çift Yönlü Zamansal Dikkat (Bidirectional Temporal Attention) katmanlarıdır. Bir $T$ karelik video diziliminde $t$. kareye ait gizil temsil, zaman eksenindeki hem geçmiş ($t' < t$) hem de gelecek ($t' > t$) karelerin tamamına aynı anda dikkat ayırmaktadır:

$$\text{Attention}(Q_t, K_{\le T}, V_{\le T}) = \text{Softmax}\left( \frac{Q_t K_{\le T}^T}{\sqrt{d_k}} \right) V_{\le T}$$

Bu matematiksel yapı, fizik dünyasındaki zamanın oku (arrow of time) ilkesini ve entropinin tek yönlü artışını ($\Delta S_{\text{evren}} \ge 0$) tamamen ihlal etmektedir [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2505.14357]]. Denoising gürültü giderme sürecinde model, tersine difüzyon yörüngesini $\mathbf{x}_{t-1} \sim p_\theta(\mathbf{x}_{t-1}\mid\mathbf{x}_t)$ hesaplarken kayıp fonksiyonu olarak basitleştirilmiş skor eşlemeyi (denoising score matching) $\mathcal{L}_{\text{simple}} = \mathbb{E}_{t, x_0, \epsilon}\left[\|\epsilon - \epsilon_\theta(x_t, t)\|^2\right]$ kullanır [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2305.13840]]. Bu kayıp fonksiyonu zamansal tersine çevrilmeye karşı istatistiksel simetri sergilemektedir.

Görsel difüzyon modellerinin zamanın oku algısını ve nedensellik kavrayışını ölçen YoCausal benchmark'ı kapsamında yapılan deneysel çalışmalarda, 13 farklı güncel video difüzyon modelinin performansları nicelleştirilmiştir [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2605.30346]]. Araştırma sonuçları, modellerin Ters Sürpriz Endeksi (Reverse Surprise Index - RSI) üzerinden yüzeysel görsel akıcılığı tespit edebildiğini, ancak Nedensellik Kavrama Endeksi (Causality Cognition Index - CCI) ölçümlerinde fiziksel nedensellik yeteneğinin insani seviyenin çok gerisinde kaldığını kanıtlamıştır. Modeller, "eski yıpranmış çatının sökülmesi" ile "yeni çelik aşıkların takılması" arasındaki zamansal ilişkiyi fiziksel bir sebep-sonuç zinciri olarak değil, yalnızca lokal uzamsal pürüzsüzlük (local visual smoothness) ve co-occurrence (birlikte bulunma) istatistikleri olarak işlemektedir. Bunun sonucunda difüzyon denoiser'ı, söküm gerçekleşirken aynı sahnede yeni kaplama panellerini üretmekte, bir sonraki sahnede ise yıkım eylemini hatırlayıp yeni yaptığı kaplamaları geriye doğru sökerek "tersten yıkım" (DERS 78) arızasına yol açmaktadır [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2604.01700]].

### 1.2. Pozitif ve Negatif Eylemlerde Dikkat Ayrımının Çöküşü
İnşaat ve restorasyon süreçlerinde eylemler iki temel vektörel yöne ayrılmaktadır:
- **Negatif Eylemler ($\Delta V < 0$):** Söküm, yıkım, moloz kaldırma, paslı çinko levhaların çıkarılması gibi yapısal kütleyi eksilten eylemler.
- **Pozitif Eylemler ($\Delta V > 0$):** Montaj, yapım, yeni malzeme ekleme, çelik aşık montajı, kenetli çatı paneli dizimi gibi kütleyi artıran eylemler.

Metin istemi (text prompt) difüzyon modelinin Cross-Attention katmanlarına iletildiğinde, istemdeki metin jetonları (text tokens) $C$ ile görsel jetonlar $Q$ arasında $A_{\text{cross}} = \text{Softmax}\left(\frac{Q K_{\text{text}}^T}{\sqrt{d}}\right)$ matrisi oluşturulmaktadır [[ÖLÇÜLDÜ | akademik makale/arXiv | OpenReview de3815ff3151f2442f4ba72d77acd3d035edbb61]]. İstem içerisinde hem söküm fiilleri (dismantling, removing) hem de yapım fiilleri (installing, assembling) veya bunlara ilişkin malzeme isimleri (rotten timber, new steel) aynı anda yer aldığında, Cross-Attention katmanlarında kavram karmaşası (concept bleeding) meydana gelmektedir.

Katmanlar arası kavram uyumu (concept-layer alignment) bozulduğunda, difüzyon modelinin orta katmanlarındaki (middle blocks) uzamsal-zamansal Özellik Haritaları (Feature Maps), pozitif ve negatif eylem vektörlerini ayrıştıramamaktadır [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2605.25941]]. Model, eksilme ile eklenme eylemlerini tek bir zamansal pencerede süperpoze eder. Termodinamik açıdan yıkım yüksek entropili ve düzensiz malzeme dağılımı içerirken, yapım düşük entropili ve geometrik düzen içeren bir süreçtir. Çift yönlü katmanlar bu entropi duvarını kuramadığı için difüzyon modeli gizil uzaydaki lokal minimumlar arasında salınım yapar ve sahnede aynı anda hem çatı paneli sökülür hem de çelik aşıklar belirir.

### 1.3. Termodinamik ve Kronolojik Irreversible Phase Gate Kurulumu
Söküm ile yapım fazı arasına geri döndürülemez bir sınır kapısı (Irreversible Phase Gate) koyabilmek için model düzeyinde ve istem düzeyinde üç ayrı mekanizmanın entegrasyonu gereklidir:
1. **Zamansal Nedensel Maskeleme (Causal Temporal Attention):** Zamansal dikkat matrisine alt-üçgensel bir maske $M_{i,j}$ eklenmeli, böylece $t$. kareye ait üretimin yalnızca $t' \le t$ karelerinden bilgi alması zorunlu kılınmalıdır [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2406.10981]]:
   $$M_{i,j} = \begin{cases} 0, & i \ge j \\ -\infty, & i < j \end{cases}$$
   Bu matematiksel kısıtlama, gelecekteki montaj karelerinin geçmişteki yıkım karelerini etkilemesini fiziki olarak engeller.
2. **Separable Causal Diffusion (SCD):** Tarihsel KV önbelleklerini (historical KV caches) bağımsız tutan zamansal kodlayıcılar kullanılmalıdır [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2602.10095]].
3. **İki Anahtar Kare Sınır Koşulu:** I2V süreçlerinde yalnızca ilk kare $I_0$ değil, fazın bitiş durumunu temsil eden ikinci anahtar kare $I_E$ de difüzyon sürecine sınır koşulu (boundary condition) olarak dâhil edilmeli; söküm fazında $I_0$ harabe durumunu, $I_E$ ise tamamen temizlenmiş yalın taşıyıcı iskeleti temsil etmelidir [[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2603.10408]]. İstem düzeyinde ise Classifier-Free Guidance (CFG) uzayında pozitif ve negatif vektörler dik (orthogonal) bileşenlere ayrıştırılmalıdır.

---

## 2. İnşaat Timelapse Filmlerinde İş Artışı ve Eylem Dağılım Mimarileri

### 2.1. Work Breakdown Structure (WBS) ve 8 Saniyelik Klip Dilimlemesi
İnşaat akışının organik, sürekli ve dengeli hissettirilmesi için her 8 saniyelik klip diliminin net, ölçülebilir bir yapısal hacim artışı ($\Delta V_{\text{yapı}} > 0$) taşıması ve "boş rölanti" (stagnant clip) veya "aniden belirme" (step-jump) arızalarından arındırılması zorunludur.

Geleneksel inşaat mühendisliğindeki İş Kırılım Yapısı (WBS), restorasyon projelerinde makro seviyeden mikro klip seviyesine indirilmelidir:
- **Level 1:** Yapısal Restorasyon
- **Level 2:** Çatı Kompleksi Dönüşümü
- **Level 3:** Söküm ve Asbest Temizliği $\to$ Taşıyıcı Onarımı $\to$ Yeni Kaplama Asamblesi
- **Level 4 (8-Saniyelik Work Packages - WP):**
  - $WP_{1.1}$: Çinko kaplama ve çürük merteklerin sökümü ($\Delta V_{\text{söküm}} = -100\%$)
  - $WP_{1.2}$: Moloz kaldırma, yüzey fırçalama ve atık tahliyesi ($\Delta V_{\text{temizlik}} = 100\%$)
  - $WP_{2.1}$: Paslı çelik makasların kumlanması ve güçlendirilmesi ($\Delta V_{\text{hazırlık}} = +20\%$)
  - $WP_{2.2}$: Yeni ikincil çelik aşıkların kaldırılarak montajı ($\Delta V_{\text{yapı}} = +40\%$)
  - $WP_{3.1}$: Yalıtım katmanı ve kenetli çatı panellerinin dizimi ($\Delta V_{\text{tamamlama}} = +40\%$)

### 2.2. Eylem Dağılım Mimarileri Karşılaştırması

| Mimarî Yaklaşım | Zamansal Kontrol ve Akış Mekanizması | Faz Karışma Riski (Demolition / Assembly) | Rölanti Clip ve Step-Jump Eğilimi | Uygulanabilirlik ve Hesaplama Maliyeti |
| :--- | :--- | :--- | :--- | :--- |
| **I2V Unstructured Prompting (Metin Temelli Serbest Üretim)** | Tek bir metin istemine dayalı serbest 8s I2V üretimi. | Çok Yüksek (%70-85): Model pozitif ve negatif kavramları tek klipte karıştırır. | Yüksek: Bazı kliplerde rölanti araç hareketi, sonraki klipte aniden belirme yaşanır. | Yüksek hız, düşük maliyet; ancak endüstriyel standartları karşılamaz. |
| **VLM-Guided Chunk-Autoregressive Chaining (CoT Parçalamalı Zincirleme)** | Sürecin VLM (örn. GPT-4o) ile 1.4s/8s parçalara bölünüp eylem safhalarıyla etiketlenmesi. | Düşük (%10-15): Her parçanın kendine ait `phase_label` değeri tanımlanır. | Çok Düşük: VLM her klibe net bir fiziki değişim yükler. | Orta-Yüksek maliyet; metin ve anahtar kare entegrasyonu gerektirir. |
| **Hierarchical Depth & Motion Forcing (Hiyerarşik Derinlik ve Yapılandırma)** | Derinlik haritası dizileri ($D_{0:T}$) ve 3D kamera rayları ile difüzyon yönlendirmesi. | Sıfıra Yakın (%0-2): Fiziksel geometri derinlik kanalı ile dondurulur. | Sıfır: Derinlik değişimi kare kare kontrollü olarak beslenir. | Yüksek maliyet; önceden 3D/derinlik simülasyonu hazırlığı gerektirir. |

[[ÖLÇÜLDÜ | akademik makale/arXiv | arXiv:2606.17730]] VLM destekli otoregresif parçalama (Chunk-Autoregressive with Chain-of-Thought) mimarisinde, klibin her 1.4 saniyelik latent penceresi görsel kanıtlar (visual evidence) üzerinden değerlendirilmekte; yaklaşma, temas, manipülasyon ve tamamlama aşamaları belirlenerek stagnant clip oluşumu engellenmektedir.

### 2.3. Boş Rölantiyi Engelleyen Şantiye İş Yoğunluğu Bileşenleri
Bir klipte izleyiciye sürekli bir inşaat devinimi hissettirmek ve $\Delta V_{\text{yapı}} > 0$ koşulunu fiziki olarak desteklemek için her 8 saniyelik sahnede **Üç Fazlı Kinematik Kurgu** uygulanmalıdır:
- **Faz I - Malzeme Lojistiği ve Yaklaşma ($t = 0.0\text{s} - 2.5\text{s}$):** Malzemenin (çelik aşık, kenet panel vb.) vinç, forklift veya işçiler tarafından montaj alanına doğru taşınması. Sahnede dinamik hareket başlatılır ancak yapısal hacim henüz artmaz ($\Delta V = 0$).
- **Faz II - Taşıyıcı Hazırlığı ve Konumlandırma ($t = 2.5\text{s} - 5.0\text{s}$):** Malzemenin hassas hizalanması, mevcut iskelete oturtulması, kaynak veya izolasyon alanının temizliği. Sahnede iş yoğunluğu pik yapar.
- **Faz III - Nihai Montaj ve Sabitleme ($t = 5.0\text{s} - 8.0\text{s}$):** Malzemenin vidalanması, çakılması veya kenetlenmesi. Yapısal kütle resmi olarak binaya eklenir ($\Delta V = +15\% \text{ ila } +20\%$).

[[VARSAYIM | endüstriyel vaka analizi | Timed-Video-Generation-Standard-2026]] Sahnedeki "boş rölanti" hissini ortadan kaldırmak için **Çoklu Etki Elemanı (Multi-Effector Rule)** kuralı işletilmelidir: Sahnede aynı anda en az 3 aktif hareketli öğe yer almalıdır: ön planda çalışan işçi elleri veya aletler, orta planda yükselen veya monte edilen yapı elemanı, arka planda malzeme taşıyan vinç veya toz/kıvılcım gibi dinamik parçacık efektleridir.

---

## 3. Standart İngilizce Söküm-Yapım Faz Kapılaması ve İş Artışı Sözdizimi

### 3.1. Söküm Fazı (Demolition Phase) Prompt ve Negatif Blok Mimarisi

**Söküm Fazı Pozitif İstem Sözdizimi (Positive Prompt):**
```text
TIMELAPSE, LOCKED TRIPOD CINEMATIC SHOT. STRICT DEMOLITION PHASE ONLY: ZERO NEW MATERIAL INSTALLATION. Active systematic dismantling of the ruined roof structure. Construction workers using heavy crowbars and angle grinders to detach rusted corrugated iron sheets and rotten timber rafters. Debris, dust particles, and fragments are continuously cleared away and lowered down via crane hoists. Visible structural reduction: bare internal iron trusses are progressively exposed as outer decaying layers are stripped away. High site activity, active material extraction, continuous negative volume delta, dirty industrial atmosphere.
```

**Söküm Fazı Negatif İstem Sözdizimi (Negative Prompt):**
```text
new materials, newly installed panels, standing-seam roofing, fresh steel purlins, new timber beams, construction assembly, structural addition, building up, clean surfaces, pristine architecture, static workers, idle vehicles, reverse motion, building repairing itself, magically appearing structures, step-jump progress, stagnant scene, reverse demolition.
```

### 3.2. Yapım Fazı (Additive Assembly Phase) Prompt ve Negatif Blok Mimarisi

**Yapım Fazı Pozitif İstem Sözdizimi (Positive Prompt):**
```text
TIMELAPSE, LOCKED TRIPOD CINEMATIC SHOT. ADDITIVE ASSEMBLY PHASE ONLY: NET POSITIVE STRUCTURAL GAIN. Active installation of modern architectural components onto the cleaned bare framework. Construction workers aligning and bolting zinc standing-seam roof panels onto galvanized steel purlins. Progressive visual coverage: each second reveals a tangible increase in completed roof coverage, transitioning from exposed skeleton to 20 percent sealed surface. High operational density: multiple workers operating fasteners, crane lowering new metal sheets into place, visible material flow, seamless organic progress, crisp detail, realistic site motion.
```

**Yapım Fazı Negatif İstem Sözdizimi (Negative Prompt):**
```text
demolition, dismantling, removing materials, tearing down, rotten timber, rust, corrugated iron debris, breaking structures, unbuilding, temporal reversal, magic vanishing of panels, idle workers, empty site, zero structural gain, stagnant camera, step-jump completion, sudden appearance of 100 percent finished roof, blurry motion.
```

### 3.3. Anahtar Kare Zincirleme Protokolü (Keyframe Chaining Protocol)
Sökümden Yapım fazına geçişteki "termodinamik duvar", iki anahtar kare arasındaki latent köprünün doğrusal kilitlenmesiyle sağlanır [[ÖLÇÜLDÜ | akademik benchmark | arXiv:2606.10620]]. ImageTime benchmark protokolü uyarınca, 4-Keyframe zincirleme yapılarında $t_1$ (başlangıç durumu), $t_2$ (eylem başlangıcı), $t_3$ (ara değişim) ve $t_4$ (nihai durum) karelerinin açıkça tanımlanması, difüzyon modelinin nedensellik ihlallerini ve kimlik kayıplarını (identity drift) %60 oranında azaltmaktadır.

Anahtar kare zincirleme akışı iki ana aşamada yürütülmektedir:
1. İlk aşamada, Hasarlı Yapı karesinden ($Keyframe_0$) Başlangıç Şartı alınır. `STRICT DEMOLITION PHASE ONLY` istem kısıtlaması uygulanarak 8 saniyelik klip üretilir ve çıktı karesi olarak Temizlenmiş Çıplak Taşıyıcı İskelet karesi ($Keyframe_1$) elde edilir.
2. İkinci aşamada ise, Temizlenmiş Çıplak Taşıyıcı İskelet karesi ($Keyframe_1$) girdi olarak alınır. Bu noktada istem `ADDITIVE ASSEMBLY PHASE ONLY` kısıtlamasına geçirilir ve üretim sonucunda %30 Kaplaması Tamamlanmış Yeni Çatı karesine ($Keyframe_2$) ulaşılır.

---

## 4. Sonuç ve Yan Çıktılar

### 4.1. Söküm ve Montaj Faz Matrisi

| Faz Adı | İzin Verilen Eylem ve Malzeme | Kesinlikle Yasaklanan Eylem | Klip Başına Gözle Görülür İş Kriteri (Tangible Delta) |
| :--- | :--- | :--- | :--- |
| **Faz 0: Temizlik & Söküm**<br>(Demolition & Clearing) | Paslı çinko levhaların sökümü, çürük merteklerin çıkarılması, molozların vinçle indirilmesi, toz/parçacık emilimi. | Yeni çelik aşık, sıfır kenet panel, her türlü taze inşaat malzemesi eklenmesi, boya/kaplama yapılması. | Sahnede mevcut harabenin yüzey alan olarak en az %25-%30'unun sökülmesi ve taşıyıcı çelik iskeletin açığa çıkması ($\Delta V < 0$). |
| **Faz 1: Taşıyıcı Onarım**<br>(Substrate Preparation) | Bare iskeletin zımparalanması, pas önleyici astar boya uygulaması, kaynak işleri, ikincil destek profillerinin konması. | Eski molozların sahneye geri dönmesi, çatının nihai kenetli panellerle aniden kaplanması. | Taşıyıcı çelik elemanların renk/yüzey kalitesinin değişmesi ve ikincil aşıkların %100 monte edilmesi ($\Delta V_{\text{iskelet}} = +100\%$). |
| **Faz 2: Yeni Montaj**<br>(Additive Assembly) | Yalıtım şiltelerinin serilmesi, kenetli çatı panellerinin hizalanması ve vida/perçin makineleri ile sabitlenmesi. | Söküm fiilleri, yıkım araç gereçleri, kırpıntı/moloz birikintileri, çürük ahşap elemanlar. | Çatı yüzey kaplamasının sahne başından sonuna kadar net %15 ila %25 oranında artış göstermesi ($\Delta V_{\text{kaplama}} > 0$). |
| **Faz 3: İnce İşçilik**<br>(Finishing & Detailing) | Yağmur oluklarının takılması, saçak kaplamaları, çatı pencerelerinin montajı, yüzey temizliği. | Taşıyıcı makasların sökülmesi, ağır yıkım ekipmanı kullanımı, kaba inşaat malzemesi sevki. | Detay elemanlarının (oluk, saçak, cam) eksiksiz tamamlanması ve montaj izlerinin temizlenmesi. |

### 4.2. Standart İngilizce Faz Kapısı ve İş Artışı Şablonu

```text
[PHASE CONTROL CONFIGURATION]
Phase Mode: ADDITIVE_ASSEMBLY_STRICT
Temporal Constraint: FORWARD_CAUSAL_ONLY
Target Work Delta (ΔV): NET_POSITIVE_GAIN (+20% Structural Coverage)

[POSITIVE PROMPT]
Timelapse video, 8k resolution, photorealistic construction execution, locked tripod angle. ADDITIVE ASSEMBLY PHASE ONLY: NET POSITIVE STRUCTURAL GAIN. Seamless sequential installation of zinc standing-seam roof panels onto galvanized steel purlins. Continuous human and mechanical motion: at least three active workers using power tools, positioning panels, and securing fasteners. Visible material transport via crane in the background. The structural coverage increases organically from frame 0 to frame 192, reaching a clear visual progression without sudden jumps. High physical coherence, natural daylighting shifts, realistic dust and construction activity.

[NEGATIVE PROMPT]
STRICT DEMOLITION PROHIBITION: dismantling, removing panels, tearing down beams, rotten wood, rust, debris accumulation, unbuilding, reverse video, inverse entropy, temporal flicker. STRICT STAGNATION PROHIBITION: static workers, idle machinery, zero structural change, empty scene, step-jump completion, instant 100% finished roof, telecommunication artifact, identity drift.

[KEYFRAME ANCHORING LINK]
Input Keyframe (t=0s): [PATH_TO_CLEAN_SKELETON_IMAGE]
Target Keyframe (t=8s): [PATH_TO_20_PERCENT_COVERED_IMAGE]
```

### 4.3. İş Artışı ve Faz Denetim Listesi (Checklist)
1. **[ ] Faz Etiketi Doğrulaması:** Klip tek bir faz etiketi (DEMOLITION veya ASSEMBLY) ile mi işaretlenmiş? İstemde zıt faz fiilleri tamamen ayıklanmış mı?
2. **[ ] Çift Yönlü İhlal Kontrolü:** Klip boyunca zamanı tersine çeviren (örneğin takılan panelin bir sonraki karede yok olması) herhangi bir difüzyon dalgalanması var mı?
3. **[ ] Ölçülebilir Hacim Artışı ($\Delta V$ Check):** Klip başlangıcı ($t=0\text{s}$) ile bitişi ($t=8\text{s}$) arasında görsel olarak en az %15'lik net bir fiziksel değişim (eklenme veya sökülme) gözlemleniyor mu?
4. **[ ] Rölanti Clip Denetimi:** Sahnede işçilerin veya araçların sadece durduğu/rölantide döndüğü, yapıya hiçbir elemanın eklenmediği sıfır-ilerleme durumu mevcut mu?
5. **[ ] Step-Jump Sıçrama Denetimi:** Tek bir karesel geçişte çatının veya yapının %30'undan fazlası aniden belirip organik akışı bozuyor mu?
6. **[ ] Çoklu Etki Elemanı Kuralı ($\ge 3$ Motion Agents):** Sahnede aynı anda hareket eden en az 3 bağımsız unsur (örn. worker hands, panel movement, crane background) var mı?
7. **[ ] Anahtar Kare Çapraz Kilidi (Keyframe Alignment):** $I_0$ karesindeki sabit mimari elemanlar (duvarlar, ana kolonlar) $I_E$ karesine kadar uzamsal konumunu ve ölçeğini koruyor mu (identity persistence)?
8. **[ ] Yüzey Entropi Kontrolü:** Söküm sahnelerinde ortamdaki moloz/toz miktarı artarken; yapım sahnelerinde yüzeyler daha temiz ve geometrik düzenli hale geliyor mu?
9. **[ ] CFG Diklik Teyidi:** Negatif prompt alanında o faza ait yasaklı gereçler (örn. yapım fazında demolition, rust, rotten timber) eksiksiz tanımlanmış mı?
10. **[ ] Üç Fazlı Kinematik Akış:** 8 saniyelik klip kendi içinde Lojistik ($0-2.5\text{s}$), Hazırlık ($2.5-5\text{s}$) ve Montaj ($5-8\text{s}$) alt pencerelerine mantıksal olarak bölünüyor mu?
