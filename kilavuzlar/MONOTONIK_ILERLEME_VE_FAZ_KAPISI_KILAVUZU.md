# ⏳ MONOTONİK İLERLEME, KÜMÜLATİF DURUM VE FAZ KAPISI KILAVUZU — ara hâl aşımı (yo-yo), durum kaybı ve sabit kadrajda büyüleyici tutunma

> Video Difüzyon Transformatörleri (vDiT: Wan2.1/2.2, HunyuanVideo, CogVideoX, LTX-Video, Sora/Gen-3) ile üretilen
> iki anahtar kare zincirli (I2V Keyframe Chaining) sabit kameralı inşaat ve dönüşüm timelapse filmlerinde
> en sık rastlanan dört kritik başarısızlık modu şunlardır:
> 1. **Ara Hâl Aşımı ve Elastik Geri Tepme (Yo-Yo Assembly):** Hedef %25 çatı iken modelin klibin 4. saniyesinde
>    %100 bitmiş çatıya fırlayıp 8. saniyede hedef karesine oturabilmek için yaptığı kaplamaları geriye doğru sökmesi.
> 2. **Kümülatif Durum Kaybı ve Çapraz Dikkat Çözülmesi (Cross-Attention Unbinding):** Klip 1'de tamamlanan
>    taşıyıcıların Klip 2'de dondurulamayıp eylem fiillerinin baskısıyla yeniden montaj çatışmasına girip erimesi (structural drift).
> 3. **Faz Çakışması ve Zamanın Oku Yitimi (Demolition/Assembly Bleeding):** Çift yönlü zamansal dikkat nedeniyle
>    söküm ($\Delta V < 0$) ile yapımın ($\Delta V > 0$) aynı klipte karışması; taze imalatın tersten yıkılması (DERS 78).
> 4. **Sabit Kadrajda Görsel Donukluk ve Dikkat Dağılması:** Kamera hareketsizken (0 pan, 0 tilt, 0 zoom) izleyiciyi
>    büyüleyen nöroestetik mekanizmaların, 5.5–7.0 sn mikro-doyum vuruşlarının ve 7–8 sn merak tohumlarının eksikliği.
>
> Kaynak: A39–A42 · 15.10.2026 (`arastirma/SONUCLAR/A39…A42_GEMINI_HAM.md` · denetim `arastirma/SONUCLAR/A39-A42_DENETIM.md`).
> 28 akademik ve endüstriyel kaynak incelendi (23 ✅ · 4 ⚠️ · 1 ❌). Rapordan doğrudan türetilen kurallar bu kılavuza işlenmiştir.

---

# 0. 🚪 KURAL — DÖRT TEMEL İNŞA VE İZLEYİCİ DEĞİŞMEZİ

```
1. MONOTONİK İLERLEME ŞARTI (dC/dt ≥ 0):
   Hiçbir inşaat klibinde tamamlanma seviyesi geriye gidemez. Model ara karelerde hedef karesinin (B)
   tavanını (%25) ASLA aşamaz. Tavan kilitlenir; 4. saniyede %100'e uçup geri sökülmek (yo-yo) yasaktır [A39-b].

2. DONDURULMUŞ BAZ (COMMITTED BASELINE) DOKUNULMAZDIR:
   Önceki klipte bitirilen elemanlar yeni klibin başlangıç karesinde (A) dondurulur; metindeki yeni eylem fiilleri
   yalnızca AKTİF MONTAJ CEPHESİNE (Active Installation Front) dokunabilir. Bitmiş eleman yeniden sökülemez veya boyanamaz [A40-d].

3. SÖKÜM İLE YAPIM ARASINDA GERİ DÖNDÜRÜLEMEZ FAZ DUVARI (IRREVERSIBLE PHASE GATE):
   Söküm klibi (ΔV < 0) ile montaj klibi (ΔV > 0) ASLA aynı klipte birleştirilmez. Söküm fazı temizlenmiş çıplak
   iskelet anahtar karesinde (Keyframe_clean) biter; montaj fazı bu kareden başlar (DERS 78 · A41-b).

4. 8 SANİYELİK MİKRO-DOYUM VE MERAK ZİNCİRİ:
   Her 8 saniyelik klip: 0–5.0 sn Gerilim/Birikim → 5.5–7.0 sn Mekanik Mikro-Doyum Vuruşu (keystone kilitlenmesi,
   derz kenetlenmesi, speküler parlama) → 7.0–8.0 sn İleriye Merak Tohumu (Visual Forward Hook) taşır [A42-c · A42-d].
```

---

# 1. 📈 MONOTONİK İLERLEME VE ARA HÂL AŞIMI (YO-YO SÖKÜM ENGELİ) [A39]

## 1.1. Matematiksel Kök Neden: Sınır Değer Problemi (BVP) ve Midpoint Guidance Decay
İki anahtar kare ($I_A$ ve $I_B$) arasında I2V veya Generative Inbetweening üretimi yaparken video difüzyon modeli latent uzayda bir Sınır Değer Problemi (Boundary Value Problem - BVP) çözer:
$$z_0 = \mathcal{E}(I_A), \quad z_N = \mathcal{E}(I_B)$$

Uzamsal-zamansal dikkat katmanlarında ($A_{i,j} = \text{softmax}(Q_i K_j^T / \sqrt{d_k})$), başlangıç ($i=0$) ve bitiş ($i=N$) kısıtlarının klibin orta noktası ($i = N/2$, 4. saniye) üzerindeki etkisi üstel olarak sıfıra yaklaşır:
$$\lim_{|i-0| \to \frac{N}{2}} A_{i,0} \to 0 \quad \text{ve} \quad \lim_{|i-N| \to \frac{N}{2}} A_{i,N} \to 0$$

Bu durum klibin ortasında (2.0–6.0 sn) bir **koşullandırma vakumu (conditioning void)** yaratır [arXiv:2505.21205].

## 1.2. Generative Prior Baskısı ve Negatif Türev ($\frac{dC}{dt} < 0$)
Koşullandırma gevşediğinde model, internet ölçeğinde eğitildiği veri kümesindeki yüksek yoğunluklu kararlı manifolda ($C = 1.0$, %100 bitmiş çatı) teslim olur. Metindeki "roof construction" kelimesini gördüğü anda 4. saniyede $C(4\text{s}) \approx 1.0$ seviyesine fırlar. 

Ancak difüzyon süreci $i \to N$ sınırına yaklaştığında $z_N = z_B$ (%25 çatı) şartını sağlamak zorundadır. Bu nedenle hız alanı (velocity field) yön değiştirir:
$$\frac{dC}{dt} < 0 \quad \text{için } t \in [4\text{s}, 8\text{s}]$$
Model yeni yaptığı kiremitleri ve aşıkları eriterek geriye doğru söker (yo-yo assembly / elastic rebound) [arXiv:2410.05651].

## 1.3. Mühendislik ve Çıkarım Çözümleri
1. **Assembly Velocity Clamping:** Akış Eşleme (Flow Matching) modellerinde tahmin edilen hız vektörü sınırlandırılır:
   $$\hat{v}_\theta(z_i) = \text{clamp}\left(v_\theta(z_i), v_{\min}, v_{\max}\right), \quad v_{\max} = \frac{z_B - z_A}{N} \cdot 1.1$$
   ani ivmelenmeler ve erken tamamlama mekanik olarak engellenir [arXiv:2601.09881].
2. **Temporal Guidance Scale (CFG) Clamping:** Orta adımlarda CFG değeri 7.0+ seviyelerinden **3.5–4.5** aralığına çekilir; unconditioned prior'ın ($C=100\%$) baskısı kırılır.
3. **Diferansiyellenebilir Monotonluk Cezası ($\mathcal{L}_{\text{mono}}$):**
   $$\mathcal{L}_{\text{mono}} = \sum_{i=0}^{N-1} \max\left(0, \Phi(z_i) - \Phi(z_{i+1})\right)$$
   ve tavan kayıp terimi $\mathcal{L}_{\text{ceiling}} = \max\left(0, \Phi(z_i) - V_{\text{target}}\right)$ ile yapısal hacmin geriye düşmesi veya tavanı aşması cezalandırılır [arXiv:2609.30795].

## 1.4. Tavan Kilitli Pozitif ve Negatif Sözdizimi
Ekstra kod müdahalesi yapılamayan standart API ve çıkarım ortamlarında prompt düzeyinde kesin tavan kilidi uygulanır:

```
[STRICT MONOTONIC PROGRESS & CEILING PATTERN]
"Locked timelapse locked camera tripod fixed view. A strictly monotonic linear construction progression
of the [ELEMENT_NAME]. Starting at frame A with [START_%] completion, advancing steadily to a strict
maximum upper bound of exactly [END_%] completion at frame B. Only the first phase [SPECIFIC_COMPONENTS]
are incrementally installed. Zero percentage addition beyond the [END_%] mark. Rigid structural
progress ceiling, incomplete open-air structure only. Non-reversible cumulative assembly, forward
motion only, frame-by-frame structural placement."

[ANTI-OVERSHOOT & ANTI-REBOUND NEGATIVE BLOCK]
"100% completed structure, fully completed roof, finished tiles, shingles, premature completion,
mid-clip overshoot, yo-yo assembly, elastic rebound, un-building, dissolving materials, dematerialization,
melting rafters, reversing construction, backward assembly, structural regression, flickering roof layers,
disappearing wood beams, fluctuating construction state, complete building enclosure."
```

---

# 2. 🧱 KÜMÜLATİF DURUM HAFIZASI VE DONMUŞ BAZ ELEMANLAR [A40]

## 2.1. Matematiksel Kök Neden: VAE Maruz Kalma Sapması ve Cross-Attention Unbinding
Ardışık pencereli veya otoregresif I2V üretim hatlarında Klip $N$'in son karesi Klip $N+1$'in ilk karesi olarak bağlandığında model, geçmiş pikselleri sert bir sınır koşulu yerine yumuşak bir koşullama vektörü olarak algılar (exposure bias) [arXiv:2512.12080].

Klip 2 isteminde geçen "workers installing steel purlins 5 to 8" eylem fiili, büyük dil modelleri (T5-XXL / Qwen2.5) üzerinden vektörleştirildiğinde çapraz dikkat matrisi ($QK^T$) görsel alandaki tüm çelik strüktür yamalarına nüfuz eder. Henüz sertleşmemiş yüksek gürültü adımlarında Klip 1'de tamamlanan aşıklar (1-4) niteliklerini kaybeder (latent feature unbinding) [arXiv:2608.26239]. Model bu aşıkları dondurmak yerine sıfırdan monte ediyormuş gibi söker veya mükerrer aşıklar çizer (structural drift / feature mutation).

## 2.2. Sıfır Kaymalı Demirleme (Zero-Drift Anchoring)
Tamamlanmış elemanların mutasyona uğramasını engellemek için üç katmanlı mimari uygulanır:
1. **Part-Latent Freezing & KV-Reinjection:** Taahhüt edilmiş donmuş bölge ($M=1$) ile aktif montaj cephesi ($M=0$) latent düzeyde ayrıştırılır. $M=1$ bölgesine karşılık gelen Key ve Value matrisleri orijinal referans kareden önceden hesaplanmış bellek matrisleriyle değiştirilir:
   $$K_l = M \odot K_l^{\text{ref}} + (1 - M) \odot K_l^{\text{current}}, \quad V_l = M \odot V_l^{\text{ref}} + (1 - M) \odot V_l^{\text{current}}$$
   Bu yöntemle arka plan ve sabit nesne detay koruma başarısı (VBench Consistency) **%98.4** seviyesine ulaşır [arXiv:2605.19350].
2. **Gaussian Sınır Yumuşatma:** VAE uzamsal evrişim bloklarının alıcı alan uyuşmazlığından doğan dikiş yırtılmalarını önlemek için maske kenarlarına $3 \times 3$ veya $5 \times 5$ Gaussian blur kernel uygulanır.
3. **Incremental ControlNet Depth Anchoring:** Klip $N$'den çıkarılan metrik derinlik haritası yeni klibe $0.75 - 0.85$ ağırlık katsayısıyla geometrik iskelet altlığı olarak bağlanır.

## 2.3. Semantik İzolasyon ve Standart Prompt Sözdizimi
İstem düzeyinde tamamlanmış elemanlar ile yeni yapılacak elemanlar kesin semantik bloklarla ayrıştırılır:

```
[COMMITTED BASELINE BLOCK: STRICTLY UNTOUCHED]
"COMMITTED BASELINE: STRICTLY UNTOUCHED AND FROZEN. The existing structure from Frame 1—specifically
[EXACT_LIST_OF_COMPLETED_ELEMENTS]—is completely constructed, permanent, and static. Do NOT alter,
modify, repaint, re-align, deform, or re-assemble any part of this existing baseline structure."

[ACTIVE INSTALLATION FRONT BLOCK ONLY]
"ACTIVE INSTALLATION FRONT ONLY: Construction activity occurs EXCLUSIVELY on [EXACT_LIST_OF_NEW_ELEMENTS].
Workers and cranes are operating ONLY at this active front. The committed baseline remains 100% frozen
as an immutable reference structure."

[NEGATIVE SHIELD PATTERN]
"re-assembly, structural drift, feature mutation, geometry melting, modifying existing structures,
repainting finished elements, dismantling [COMPLETED_ELEMENTS], moving established steel beams,
duplicate elements, altering flange thickness, texture shift on finished steel, camera movement,
spatial distortion, floating construction elements, tearing at structural joints."
```

---

# 3. 🚧 SÖKÜM VE MONTAJ FAZ KAPISI (IRREVERSIBLE PHASE GATE) VE İŞ HACMİ TEMPOSU [A41]

## 3.1. Çift Yönlü Zamansal Dikkat ve Zamanın Oku Yitimi
Video difüzyon modellerinin Çift Yönlü Zamansal Dikkat (Bidirectional Temporal Attention) mekanizması, bir kareyi üretirken hem geçmişe ($t' < t$) hem de geleceğe ($t' > t$) aynı anda dikkat ayırır:
$$\text{Attention}(Q_t, K_{\le T}, V_{\le T}) = \text{Softmax}\left(\frac{Q_t K_{\le T}^T}{\sqrt{d_k}}\right) V_{\le T}$$

Bu matematiksel yapı termodinamik zamanın okunu ($\Delta S \ge 0$) ihlal eder [arXiv:2505.14357]. YoCausal benchmark'ında modellerin nedensellik kavrama endeksi (CCI) çökmektedir [arXiv:2605.30346]. Metinde hem söküm fiilleri ("dismantling") hem de montaj fiilleri ("installing") yer aldığında, model iki eylemi süperpoze eder; yeni yaptığı kaplamayı bir sonraki karede geriye doğru yıkar (DERS 78).

## 3.2. Termodinamik Duvar: Kesin Faz Ayrımı
Söküm ile montaj arasına geri döndürülemez bir duvar koymak için:
- **Causal Temporal Attention:** Dikkat matrisine alt-üçgensel maske ($M_{i,j} = 0 \text{ if } i \ge j \text{ else } -\infty$) uygulanır.
- **İki Ayrı Anahtar Kare Zinciri:** Söküm fazı $Keyframe_0$ (Harabe) ile başlar, $Keyframe_1$ (Temizlenmiş Çıplak İskelet) ile biter. Montaj fazı $Keyframe_1$ girdisiyle başlar, $Keyframe_2$ (%30 Yeni Çatı) ile devam eder. İki faz ASLA tek promptta ya da tek klipte birleştirilmez [arXiv:2606.10620].

## 3.3. 8 Saniyelik Work Breakdown Structure (WBS) ve Work Packages
Her 8 saniyelik klip, boş rölanti (stagnant clip) veya aniden belirme (step-jump) olmaksızın ölçülebilir bir yapısal hacim değişimi ($\Delta V \ge %15-%20$) taşımak zorundadır:

| Faz Adı | İzin Verilen Eylem ve Malzeme | Kesinlikle Yasaklanan Eylem | Klip Başına Net Değişim ($\Delta V$) |
| :--- | :--- | :--- | :--- |
| **Faz 0: Temizlik & Söküm** | Paslı çinko sacların sökümü, çürük merteklerin çıkarılması, moloz tahliyesi. | Yeni malzeme ekleme, çelik montajı, kaplama yapılması. | Yüzeyin en az %25-%30'unun sökülmesi, iskeletin açığa çıkması ($\Delta V < 0$). |
| **Faz 1: Taşıyıcı Onarımı** | İskeletin kumlama/zımparalanması, astar boya, takviye plakaları, ikincil aşıklar. | Molozların geri dönmesi, çatının nihai panellerle kaplanması. | Taşıyıcı elemanların renk/yüzey değişimi, ikincil aşıkların montajı ($\Delta V_{\text{iskelet}} = +100\%$). |
| **Faz 2: Yeni Montaj** | Yalıtım şiltesi serimi, kenetli çatı panellerinin dizimi, vidalama/kenetleme. | Söküm fiilleri, yıkım araçları, moloz birikintisi, çürük malzeme. | Çatı kaplamasının net %15 ila %25 oranında artış göstermesi ($\Delta V_{\text{kaplama}} > 0$). |
| **Faz 3: İnce İşçilik** | Yağmur oluğu, saçak kaplaması, mahya çıtası, çatı pencereleri, son temizlik. | Ağır yıkım ekipmanı, kaba taşıyıcı sökümü, kaba beton sevki. | Detay elemanlarının eksiksiz tamamlanması, şantiye kalıntısının temizlenmesi. |

## 3.4. Üç Fazlı Kinematik Kurgu ve Çoklu Etki Elemanı ($\ge 3$)
Her 8 saniyelik montaj klibinde iş akışı üç kinematik alt pencereye bölünür:
1. **Faz I — Malzeme Lojistiği ve Yaklaşma ($0.0\text{s} - 2.5\text{s}$):** Malzemenin vinç, manlift veya işçilerle montaj alanına taşınması ($\Delta V = 0$). Sahneye dinamik hareket girer.
2. **Faz II — Taşıyıcı Hazırlığı ve Konumlandırma ($2.5\text{s} - 5.0\text{s}$):** Malzemenin iskelete oturtulması, hassas hizalama. İş yoğunluğu zirve yapar.
3. **Faz III — Nihai Montaj ve Sabitleme ($5.0\text{s} - 8.0\text{s}$):** Malzemenin cıvatalanması veya kenetlenmesi. Yapısal kütle binaya eklenir ($\Delta V = +15\% \text{ ila } +20\%$).

**Çoklu Etki Elemanı Kuralı (Multi-Effector Rule):** Sahnede aynı anda en az 3 aktif hareketli unsur bulunmalıdır:
- Ön planda çalışan işçi elleri / el aletleri (fasteners, angle grinders)
- Orta planda monte edilen yapı elemanı (panel positioning, beam alignment)
- Arka planda malzeme taşıyan vinç / araç veya dinamik parçacıklar (dust, welding sparks)

---

# 4. 🧠 SABİT KADRAJDA NÖROESTETİK TUTUNMA VE MİKRO-DOYUM MİMARİSİ [A42]

## 4.1. Sabit Tripod Büyüsü (0 Pan, 0 Tilt, 0 Zoom)
Kamera hareketinin tamamen sıfırlandığı (0 pan, 0 tilt, 0 zoom, locked frame) bir kurguda izleyicinin görsel korteksi (V5/MT alanı) kamera sarsıntısını işlemekten kurtulur ve tüm bilişsel kaynaklarını nesnenin içsel dönüşümüne (allocentric transformation) yönlendirir [DOI: 10.1093/oso/9780197513620.001.0001].

## 4.2. Gestalt Tamamlama ve Entropi Düşüşü
- **Öngörüsel Kodlama ve Gestalt Tamamlama:** Eksik bir mimari form (örneğin yarım kemer veya açık çatı iskeleti) beyinde bilişsel gerilim (cognitive tension) ve öngörü hatası üretir [DOI: 10.1017/S0140525X19001213]. Elemanın yerine oturmasıyla zihinsel model tamamlanır (closure principle); birikmiş gerilim boşalır.
- **Entropi Düşüşü (Kaostan Nizama):** Dağınık ham şantiye malzemeleri yüksek kenar-yönelim entropisine (Edge-Orientation Entropy) sahiptir [DOI: 10.1371/journal.pone.0316555]. İnşaat ilerledikçe çizgilerin ortogonal (yatay ve dikey) simetriye kavuşması entropiyi düşürür [DOI: 10.3390/e23020153]; beyin daha az enerji harcayarak yüksek bilgi işler ve derin görsel rahatlama yaşar.

## 4.3. fMRI Ödül Devreleri ve Mikro-Dopamin Salınımı (Micro-Payoff)
Ritmik süreç ve tamamlama videoları beyinde **nucleus accumbens (ödül merkezi)** ve **middle frontal gyrus (odaklanma alanı)** bölgelerini aktive eder [DOI: 10.3389/fnins.2023.1025745]. Kusursuz toleransla oturan her eleman ve pürüzsüzleşen yüzey striatal mikro-dopamin salınımı üretir.

## 4.4. 8 Saniyelik Sahne Anatomisi (Payoff & Forward Hook)
Her 8 saniyelik klip kapalı bir mikro-tatmin ve bir sonraki klibe uzanan merak köprüsü olarak ölçeklenir:

```
0.0s ────────────────────────────── 5.0s ───────── 5.5s ────────── 7.0s ───────── 8.0s
│                                      │             │                │             │
│        GERİLİM VE BİRİKİM            │             │  MİKRO-DOYUM   │ İLERİYE     │
│   (Tension & Work Accumulation)      │             │  VURUŞ ANI     │ MERAK       │
│                                      │             │ (Micro-Payoff) │ TOHUMU      │
│  · Malzeme taşınır ve hizalanır      │             │ · Kilit taşı   │ · Filiz     │
│  · İş yoğunluğu zirve yapar          │             │   oturur       │   demirler  │
│  · Entropi yüksektir                 │             │ · Panel keneti │ · Sıvasız   │
│                                      │             │   parlar       │   köşe      │
│                                      │             │ · Harç düzleşir│ · Boşluk    │
```

> ⚠️ **ÖLÇÜM (DERS 92 · THE POOL ROOM, 16.10.2026):** altı klipte ana dönüşüm 2–4 sn'de bitti; 5,5–7 sn'ye
> yazılan doyum anları oraya düşmedi. Bu anatomi bir HEDEFTİR, model davranışı değil: doyum bir nesneye bağlanır
> (son panelin oturması) ve pilotun 2x kopyasında ölçülür; geç bitiş vaadi yazılmaz. Klip sonu teslimatlar (7–8 sn
> merak tohumu) TUTTU.

- **5.5–7.0 sn — Mikro-Doyum Vuruşu (Micro-Payoff):** Kemerin kilit taşı yerine oturur; kenetli çatı sacı güneş parlamasıyla kilitlenir; pürüzlü sıva mala darbesiyle mat pürüzsüzlüğe kavuşur.
- **7.0–8.0 sn — İleriye Merak Tohumu (Visual Forward Hook):** Kadrajın kenarında henüz tamamlanmamış bir sonraki aşama elemanı belirir (örneğin kolon tepesindeki filiz demirler, kaplama bekleyen açık aşık boşluğu, hizalanmamış oluk braketi) [DOI: 10.1098/rstb.2022.0411]. Beyinde bilgi boşluğu (Information Gap) açılır; izleyici videoyu kaydırmayıp sonraki sahneye kilitlenir.

---

# 5. 📋 STANDART İNGİLİZCE ENTEGRE SÖZDİZİMİ VE ŞABLONLAR

## 5.1. Monotonik İnşa ve Tavan Kilidi Bloğu
```
[POSITIVE PROMPT: MONOTONIC PROGRESS & CEILING LOCK]
Timelapse video, photorealistic 8k, locked tripod angle, zero camera movement.
A strictly monotonic forward construction progression of the [ELEMENT_NAME].
Advancing steadily from initial state [START_%] to a hard upper bound ceiling of exactly [END_%] completion.
Incremental frame-by-frame structural assembly. Only [SPECIFIC_COMPONENTS] are slowly installed in sequence.
The structure must NEVER progress beyond the [END_%] target state at any midpoint frame.
Open-air unfinished frame, visible structural gaps, raw skeleton only.
Irreversible linear progress, zero material dissolution, zero backward construction.

[NEGATIVE PROMPT: ANTI-OVERSHOOT & ANTI-REBOUND]
fully completed structure, 100% completion, finished roof, tiles, shingles, premature completion,
mid-clip overshoot, yo-yo assembly, elastic rebound, unbuilding, dissolving wood, melting beams,
dematerialization, reversing progression, backward timelapse, structural flickering, disappearing elements,
structural regression, over-built ceiling breach.
```

## 5.2. Kümülatif Durum ve Donmuş Baz Bloğu
```
[COMMITTED BASELINE: STRICTLY UNTOUCHED]
The background structure and previously installed elements visible in Frame 1 are FULLY COMMITTED,
PERMANENT, and FROZEN IN PLACE.
Frozen Elements: [EXACT_LIST_OF_COMPLETED_ELEMENTS, e.g., Steel columns A1-A4 and first 4 steel purlins].
Status: Completed, fully bolted, factory-painted industrial gray, completely static.
Constraint: ABSOLUTELY NO ALTERATIONS. Do not repaint, do not shift geometry, do not re-align,
do not dismantle, and do not re-assemble any part of the committed baseline.

[ACTIVE INSTALLATION FRONT ONLY]
Construction activity is strictly confined to the dynamic installation front.
Target Action: Workers and construction equipment are EXCLUSIVELY installing [EXACT_LIST_OF_NEW_ELEMENTS].
Mechanics: Purlins 5 through 8 are sequentially lifted via crane cables, aligned precisely adjacent
to purlin 4, and fastened to the steel trusses.
Boundary Integrity: The interface where purlin 4 meets purlin 5 must remain sharp, continuous,
and geometrically exact without structural melting or tearing.

[NEGATIVE PROMPT: ANTI-MUTATION SHIELD]
re-assembly, structural drift, feature mutation, geometry melting, modifying existing structures,
repainting finished elements, dismantling purlins 1-4, moving established steel beams, duplicate purlins,
altering flange thickness, texture shift on finished steel, camera movement, spatial distortion,
floating construction elements, tearing at structural joints.
```

## 5.3. Söküm ve Montaj Faz Kapısı Bloğu
```
[PHASE MODE: STRICT_DEMOLITION_ONLY]
TIMELAPSE, LOCKED TRIPOD CINEMATIC SHOT. STRICT DEMOLITION PHASE ONLY: ZERO NEW MATERIAL INSTALLATION.
Active systematic dismantling of the ruined roof structure. Construction workers using heavy crowbars
and angle grinders to detach rusted corrugated iron sheets and rotten timber rafters. Debris, dust
particles, and fragments are continuously cleared away and lowered down via crane hoists.
Visible structural reduction: bare internal iron trusses are progressively exposed as outer decaying
layers are stripped away. High site activity, active material extraction, continuous negative volume delta.

[NEGATIVE PROMPT: DEMOLITION PHASE]
new materials, newly installed panels, standing-seam roofing, fresh steel purlins, new timber beams,
construction assembly, structural addition, building up, clean surfaces, pristine architecture,
static workers, idle vehicles, reverse motion, building repairing itself, magically appearing structures,
step-jump progress, stagnant scene, reverse demolition.

[PHASE MODE: ADDITIVE_ASSEMBLY_ONLY]
TIMELAPSE, LOCKED TRIPOD CINEMATIC SHOT. ADDITIVE ASSEMBLY PHASE ONLY: NET POSITIVE STRUCTURAL GAIN.
Active installation of modern architectural components onto the cleaned bare framework.
Construction workers aligning and bolting zinc standing-seam roof panels onto galvanized steel purlins.
Progressive visual coverage: each second reveals a tangible increase in completed roof coverage,
transitioning from exposed skeleton to 20 percent sealed surface. High operational density: multiple
workers operating fasteners, crane lowering new metal sheets into place, visible material flow.

[NEGATIVE PROMPT: ADDITIVE ASSEMBLY PHASE]
demolition, dismantling, removing materials, tearing down, rotten timber, rust, corrugated iron debris,
breaking structures, unbuilding, temporal reversal, magic vanishing of panels, idle workers, empty site,
zero structural gain, stagnant camera, step-jump completion, sudden appearance of 100 percent finished roof.
```

## 5.4. Büyüleyici Mikro-Doyum ve Merak Tohumu Bloğu
```
[HYPNOTIC VISUAL PAYOFF & FORWARD HOOK BLOCK]
[CAMERA_ANCHOR]: Absolute fixed tripod shot, zero camera movement, zero pan, zero tilt, zero zoom,
stationary static angle, hyper-stable photorealistic frame.
[ACTION_HYPERLAPSE]: Ultra-accelerated time-lapse footage of [INSERT_ARCHITECTURAL_ELEMENT].
[TACTILE_TRANSFORMATION]: Raw tactile materials rapidly assembling, [INSERT_SPECIFIC_TRANSFORMATION,
e.g., interlocking metal standing-seam panels clicking securely into galvanized purlins].
[LIGHTING_SWEEP]: Cinematic diurnal sunbeams sweeping diagonally across the scene, casting dynamic
rhythmic shadows that evolve across the masonry.
[MICRO_PAYOFF_MOMENT]: At 6 seconds, [INSERT_MICRO_RESOLUTION, e.g., the final fastener locks into place
and the metal surface catches a crisp specular sunlight reflection].
[FORWARD_HOOK_SEED]: In the frame margin at 7 seconds, [INSERT_UNANSWERED_SEED, e.g., exposed vertical
rebars await the next level / an adjacent unplastered wall section remains wet].
[QUALITY_BLOCK]: Photorealistic 8k, raw material realism, sharp architectural lines, zero distortion,
perfectly locked spatial coordinates.
```

---

# 6. 🎯 ÜRETİM VE DENETİM KONTROL LİSTESİ (12 MADDELİK TEKNİK CHECKLIST)

Her ardışık I2V klibi üretime gönderilmeden ve teslim edilmeden önce bu denetimden geçer:

- [ ] **1. Tavan Kilidi Kontrolü:** İstemde kesin üst sınır ("strict maximum upper bound of exactly X%") tanımlanmış mı?
- [ ] **2. Anti-Overshoot Negatifi:** Negatif istemde "yo-yo assembly, elastic rebound, un-building, dissolving materials" eksiksiz var mı?
- [ ] **3. Baz / Cephe Ayrımı:** Pozitif istemde `COMMITTED BASELINE` ile `ACTIVE INSTALLATION FRONT` başlıkları açıkça ayrıştırılmış mı?
- [ ] **4. Donmuş Eleman Yasakları:** Negatif alanda tamamlanmış elemanların adı verilerek "re-assembly, repainting, dismantling [ELEMENT]" kalkanı çekilmiş mi?
- [ ] **5. Faz İzolasyonu:** Klip tek bir faza (DEMOLITION veya ASSEMBLY) mı ait? İstemde zıt faz fiilleri ve malzemeleri tamamen elenmiş mi?
- [ ] **6. Anahtar Kare Çapraz Kilidi:** $Keyframe_0$ ile $Keyframe_E$ arasındaki sabit nirengi noktaları (duvarlar, temel) piksel düzeyinde çakışıyor mu?
- [ ] **7. Ölçülebilir Hacim Artışı ($\Delta V$):** Klip başlangıcı ile bitişi arasında gözle görülür en az %15-%20 net fiziksel değişim garanti edilmiş mi?
- [ ] **8. Üç Fazlı Kinematik Akış:** 8 saniyelik klip Lojistik ($0-2.5\text{s}$), Hazırlık ($2.5-5\text{s}$) ve Montaj ($5-8\text{s}$) pencerelerine oturuyor mu?
- [ ] **9. Çoklu Etki Elemanı ($\ge 3$):** Sahnede aynı anda çalışan en az 3 bağımsız hareketli unsur (işçi elleri, montaj parçası, vinç/kıvılcım) tanımlı mı?
- [ ] **10. 6. Saniye Mikro-Doyum Vuruşu:** 5.5–7.0 saniye aralığında Gestalt tamamlanması veya speküler parlama vuruşu planlanmış mı?
- [ ] **11. 7. Saniye Merak Tohumu:** Klibin son saniyesinde bir sonraki sahneye devreden çözülmemiş bir görsel ipucu kadraj kenarına bırakılmış mı?
- [ ] **12. CFG ve Hız Klamplama:** Çıkarım parametrelerinde Temporal CFG 3.5–4.5 aralığına çekilmiş ve akış hızı klamplaması ($v_{\max}$) aktif edilmiş mi?

---

# 7. 🚪 KAPI VE DEPO ENTEGRASYONU — bu kurallar nerede zorlanır

```
① PLANDA        Aşama merdiveninde söküm satırları ile yapım satırları AYRI FAZ bloklarında toplanır.
                Her satıra 'TAVAN: %X' damgası vurulur. Planda 'COMMITTED' listesi beyan edilir.

② PROMPTTA      ⛔ prompt_kontrol.py:
                   · I2V bloğunda ara hâl aşımını engelleyecek tavan ("upper bound" / "ceiling") yoksa → BLOCK
                   · Negatif istemde 'yo-yo assembly' veya 'elastic rebound' eksikse → BLOCK
                   · Aynı klipte hem söküm ("dismantle/tear down") hem yapım ("install/assemble") fiili varsa → BLOCK
                   · COMMITTED BASELINE tanımlanmadan ikinci klip yazılmışsa → BLOCK
                   · ACTIVITY bloğunda el < 3 ise → FIX (§3.4)
                   · 6. sn mikro-doyum veya 7. sn merak tohumu tanımlı değilse → FIX (§4.4)

③ ÜRETİM        Üretim günlüğünde her klip için:
   GÜNLÜĞÜNDE      - Gerçekleşen tavan doğrulaması (% aşımı var mı? Evet → KLİBİ AT)
                   - Donmuş baz bütünlüğü (Önceki elemanlar eridi mi? Evet → KLİBİ AT)
                   - 6. sn mikro-doyum ve 7. sn merak kancası kontrolü (✓/✗)

④ QA'DA         ❹ İNŞA ve ❺ TESLİM mercekleri:
                   - Q4: Ara hâl aşımı (yo-yo), geriye yıkım ve donmuş baz mutasyonu kontrol edilir.
                   - Q5: 6. sn mikro-doyum vuruşu ve kesmedeki bilişsel merak akışı denetlenir.
```
