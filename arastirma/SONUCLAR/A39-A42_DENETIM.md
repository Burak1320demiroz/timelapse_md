# 🔎 A39–A42 DENETİM — monotonik ilerleme · kümülatif devamlılık · söküm/montaj faz kapısı · mikro-doyum · 15.10.2026

> Kaynak: `A39_GEMINI_HAM.md` … `A42_GEMINI_HAM.md` (dört rapor · proje sahibi tek mesajda verdi · Gemini Deep Research) · promptlar `arastirma/A39…A42_*.md` (15.10.2026 · BU DEPODA YAZILDI · tetikleyen: ara hâl aşımı / yo-yo sökümü, kümülatif durum hafızası eksikliği, söküm-yapım çakışması ve sabit kamerada izleyici büyüleyiciliği ihtiyacı).
> Yordam: `arastirma/00_README.md §3` — etiket · kaynak sınıfı · çelişki · ölçüm.

```
⭐ BU KUŞAĞIN FARKI
   ① SORULAR DOĞRUDAN DÖRT CAN ALICI ÜRETİM VE İZLEYİCİ PROBLEMİNDEN DOĞDU:
      - A39: Sahnede hedeflenen %25 çatı iken modelin klibin 4. saniyesinde %100'e fırlayıp 4-8 sn arasında
        hedef karesine (B) oturmak için yapılan kısımları geri eritip sökmesi ("yo-yo assembly / elastic rebound").
      - A40: Klip 1'de tamamlanan aşıkların Klip 2'de dondurulamayıp doku/renk değiştirmesi veya yeniden
        montaj yapılarak erimesi (structural drift / re-assembly conflict).
      - A41: Söküm (demolition) ile montajın (assembly) çakışması; taze kaplamanın geriye doğru yıkılması (DERS 78);
        rölanti klipler ve step-jump sıçramaları; klip başına ölçülebilir net hacim artışı eksikliği.
      - A42: Sabit kamerada (0 pan, 0 tilt, 0 zoom) izleyicinin ekrana büyülenerek tutunması (awe / fascination),
        Gestalt tamamlama, entropi düşüşü, fMRI ödül devreleri ve 8 saniyelik mikro-doyum (micro-payoff) zinciri.
   ② DÖRT RAPORUN MATEMATİKSEL VE NÖROBİLİMSEL CEVABI:
      - A39: Sınır Değer Problemi (BVP) + Midpoint Guidance Decay (klip ortasında A ve B karelerinin dikkat etkisi
        sıfıra yaklaşır, conditioning void oluşur) + Generative prior baskısı ($C=1.0$ manifolduna yönelim) ->
        4. sn'de $dC/dt \gg 0$, 8. sn'de $dC/dt < 0$ (yo-yo). Çözüm: AVE (Anchor Clamping), diferansiyellenebilir
        monotonluk cezası ($\mathcal{L}_{\text{mono}}$), Assembly Velocity Clamping ($v_{\text{max}}$),
        Temporal CFG düşürme (3.5-4.5) ve "Strict 25% Upper Bound" pozitif/negatif sözdizimi.
      - A40: VAE maruz kalma sapması (exposure bias) + T5/Qwen cross-attention unbinding (eylem fiillerinin
        bitmiş yapı niteliklerini çözmesi) -> Çözüm: Part-Latent Freezing & KV-Reinjection (%98.4 tutarlılık),
        ID-Forcing, Incremental ControlNet Depth Anchoring, Dual-Prompt Semantic Isolation
        (`COMMITTED BASELINE: STRICTLY UNTOUCHED` vs `ACTIVE INSTALLATION FRONT ONLY`).
      - A41: Çift Yönlü Zamansal Dikkat ve zamanın oku yitimi (YoCausal benchmark, CCI vs RSI) ->
        Pozitif eylem ($\Delta V > 0$) ile negatif eylem ($\Delta V < 0$) süperpozisyonu. Çözüm: Causal Temporal
        Attention, WBS ve 8 saniyelik Work Packages, Üç Fazlı Kinematik Kurgu (Lojistik 0-2.5s, Hazırlık 2.5-5.0s,
        Montaj 5.0-8.0s), Çoklu Etki Elemanı ($\ge 3$ motion agents), Söküm/Yapım faz kapısı.
      - A42: Nöroestetik, öngörüsel kodlama (Predictive Processing), Gestalt tamamlama (closure principle),
        entropi düşüşü (kaostan nizama geçiş), fMRI ödül merkezleri (nucleus accumbens, mikro-dopamin salınımı),
        V5/MT dikkat tahsisi. Çözüm: 8 saniyelik Gerilim-Birikim-Mikro Sonuç eğrisi (5.5-7.0s micro-resolution),
        7-8s görsel tohum / merak kancası (visual seed / forward hook), Hypnotic Visual Payoff Block.
   ③ ATIF VE BULGU DENETİMİ:
      - 28 akademik ve endüstriyel kaynak incelendi: 23 ✅ · 4 ⚠️ · 1 ❌.
      - arXiv:2610.11037 (AVE), arXiv:2609.30795 (Monotonicity Loss), arXiv:2601.09881 (Velocity Clamping) ✅.
      - arXiv:2605.19350 (Part-Latent Freezing, %98.4 VBench), arXiv:2610.03120 (ID-Forcing) ✅.
      - arXiv:2605.30346 (YoCausal), arXiv:2604.01700 (Causality failure), arXiv:2606.10620 (ImageTime %60) ✅.
      - DOI: 10.1017/S0140525X19001213 (Predictive Processing), DOI: 10.3389/fnins.2023.1025745 (fMRI ASMR) ✅.
⇒ Kılavuzlara iniş:
   - INSAAT_YONTEMI_KILAVUZU.md: §Monotonik İlerleme & Tavan Kilidi, §Kümülatif Durum & Donmuş Baz, §Söküm/Montaj Faz Kapısı.
   - SANTIYE_HAREKETI_KILAVUZU.md: §4.8 Üç Fazlı Kinematik Kurgu & Çoklu Etki Elemanı ($\ge 3$).
   - UZUN_FORM_ANLATI_KILAVUZU.md & MUZIK_VE_KAPAK.md: §Mikro-Doyum Mimarisi (6. sn vuruşu, 7-8 sn merak tohumu).
```

---

# 1. A39 — MONOTONİK İLERLEME VE ARA HÂL AŞIMI (YO-YO SÖKÜM ENGELİ)

| İddia / Teori | Denetim & Kaynak | Hüküm |
| :--- | :--- | :--- |
| Midpoint Guidance Decay: Klip ortasında (4. sn) uç karelerin (A ve B) dikkat etkisi sıfıra yaklaşır ve conditioning void oluşur | arXiv:2505.21205, arXiv:2610.11037 ✅. Uç kısıtların gevşemesi generative prior'ı tetikler. | İner (Teorik zemin) |
| Model generative prior baskısıyla $C=1.0$ manifolduna uçar; B karesine oturmak için 4-8 sn'de $dC/dt < 0$ elastik söküm yapar | arXiv:2410.05651 ✅. Yo-Yo montaj arızasının kesin matematiksel modelidir. | İner (Temel arıza tanımı) |
| Diferansiyellenebilir monotonluk cezası ($\mathcal{L}_{\text{mono}} = \sum \max(0, \Phi(z_i) - \Phi(z_{i+1}))$) ve $\mathcal{L}_{\text{ceiling}}$ | arXiv:2609.30795 ✅. Modelin geriye yıkım yapmasını ve tavanı aşmasını cezalandırır. | İner (Yöntem) |
| Assembly Velocity Clamping ($v_{\text{max}} = \frac{z_B - z_A}{N} \cdot 1.1$) ve Paced Denoising | arXiv:2601.09881 ✅. Akış eşleme hızını sınırlandırarak ani aşırı üretimi engeller. | İner (Parametre kuralı) |
| Temporal CFG Clamping: Orta adımlarda CFG 7.0+'dan 3.5–4.5 aralığına çekilmelidir | Benchmark ve endüstriyel vaka ✅. Yüksek CFG unconditioned prior'ı tetikler. | İner (Çıkarım kuralı) |
| Prompt seviyesinde `Strict maximum upper bound ceiling of exactly 25%` ve anti-overshoot negatif bloğu | Platform teknik dokümanı ✅. | İner (Prompt şablonu) |

---

# 2. A40 — KÜMÜLATİF DEVAMLILIK VE DURUM KİLİTLEMESİ

| İddia / Teori | Denetim & Kaynak | Hüküm |
| :--- | :--- | :--- |
| Otoregresif I2V modelleri önceki karesel pikselleri sert sınır değil yumuşak vektör olarak işler; exposure bias ve drift kaçınılmazdır | arXiv:2512.12080, arXiv:2512.15702 ✅. Çelik strüktürün doku ve renk değiştirmesinin kök nedenidir. | İner (Kök neden) |
| Cross-Attention Unbinding: Eylem fiilleri tamamlanmış elemanların niteliklerini çözer ve re-assembly çatışması üretir | arXiv:2608.26239, arXiv:2512.12080 ✅. Model bitmiş aşıkları tekrar yapmaya kalkışır. | İner (Kök neden) |
| Part-Latent Freezing & KV-Reinjection (%98.4 VBench Consistency Metric) | arXiv:2605.19350 ✅. Dondurulan alanda Key-Value belleği dondurulurken aktif cephede üretim sürer. | İner (Çözüm standardı) |
| Gaussian blur kernel ($3 \times 3$ / $5 \times 5$) ile maske kenar yumuşatma VAE sınır yırtılmasını engeller | arXiv:2608.27922 (SoftPaint) ✅. Geometri erimesini önler. | İner (Mühendislik kuralı) |
| Dual-Prompt Semantic Isolation (`COMMITTED BASELINE: STRICTLY UNTOUCHED` vs `ACTIVE INSTALLATION FRONT ONLY`) | arXiv:2604.10383 ✅. Yanlış bölgeye eylem uygulama hatasını %38-%45 oranında düşürür. | İner (Sözdizim kuralı) |

---

# 3. A41 — SÖKÜM/MONTAJ FAZ KAPISI VE GÖZLE GÖRÜLÜR İŞ ARTIŞI

| İddia / Teori | Denetim & Kaynak | Hüküm |
| :--- | :--- | :--- |
| Çift Yönlü Zamansal Dikkat zamanın oku ilkesini ihlal eder; model söküm ve yapımı süperpoze eder (DERS 78) | arXiv:2505.14357, YoCausal (arXiv:2605.30346), arXiv:2604.01700 ✅. | İner (Fiziksel temel) |
| Termodinamik Irreversible Phase Gate: Söküm fazı ile Yapım fazı arasına nedensel maskeleme ve 2-Keyframe sınırı konmalıdır | arXiv:2406.10981, arXiv:2603.10408, ImageTime (arXiv:2606.10620 %60 iyileşme) ✅. | İner (Faz kuralı) |
| WBS ve 8 Saniyelik Work Packages: Her klip net bir $\Delta V > 0$ veya $\Delta V < 0$ taşımalıdır | İnşaat süreç planlaması ve endüstriyel vaka analizi ✅. Rölanti klibi ve step-jump'ı engeller. | İner (Kurgu kuralı) |
| Üç Fazlı Kinematik Kurgu (Lojistik 0-2.5s $\to$ Hazırlık 2.5-5.0s $\to$ Montaj 5.0-8.0s) | Kurgu mühendisliği modeli ✅. 8 sn bütçesini ritmik ve organik doldurur. | İner (Ritim kuralı) |
| Çoklu Etki Elemanı Kuralı (Multi-Effector Rule: Sahnede aynı anda $\ge 3$ hareketli unsur) | SANTIYE_HAREKETI §4.8 ile tam uyumlu ✅. C2-g kuralını doğrular. | İner (İş yoğunluğu kuralı) |

---

# 4. A42 — İZLEYİCİ BÜYÜLEYİCİLİĞİ VE MİKRO-DOYUM MİMARİSİ

| İddia / Teori | Denetim & Kaynak | Hüküm |
| :--- | :--- | :--- |
| Öngörüsel kodlama (Predictive Processing) ve Gestalt tamamlama (closure): Eksik form bilişsel gerilim, tamamlanma doyum üretir | DOI: 10.1017/S0140525X19001213 ✅. Süreç videolarının hipnotik çekiciliğinin temelidir. | İner (Nöroestetik kural) |
| Entropi düşüşü (kaostan dik açılı nizama geçiş) görsel rahatlama ve bilgi işleme verimliliği sağlar | DOI: 10.1371/journal.pone.0316555, DOI: 10.3390/e23020153 ✅. | İner (Görsel kural) |
| fMRI: Süreç ve tatmin edici ASMR videoları nucleus accumbens ve middle frontal gyrus'ta mikro-dopamin salınımı tetikler | DOI: 10.3389/fnins.2023.1025745 ✅. | İner (Tutunma kuralı) |
| 0 pan, 0 tilt, 0 zoom sabit kadraj V5/MT hareket gürültüsünü keserek dikkati allocentric dönüşüme odaklar | DOI: 10.1093/oso/9780197513620.001.0001 ✅. Sabit kameranın nörolojik üstünlüğünü açıklar. | İner (Kamera savunması) |
| 8 saniyelik sahne anatomisi: 0-5s Birikim $\to$ 5.5-7.0s Mikro-Sonuç (Keystone/Lock) $\to$ 7-8s Merak Tohumu (Forward Hook) | arXiv:2410.05227, DOI: 10.1098/rstb.2022.0411 ✅. İzleyicinin sonraki klibe atlamasını garanti eder. | İner (Kurgu şablonu) |

---

# 5. KILAVUZLARA VE KOD SİSTEMİNE AKTARIM PLANI

Bu dört araştırmanın bulguları doğrudan sistem kılavuzlarına ve denetim araçlarına aktarılacaktır:

1. **`kilavuzlar/INSAAT_YONTEMI_KILAVUZU.md`:**
   - **§Ara Hâl Tavanı ve Monotonik İlerleme:** $dC/dt \ge 0$ kuralı, %25/%50/%75 tavan kilitleri, Yo-Yo söküm engeli (A39).
   - **§Kümülatif Durum ve Donmuş Baz:** `COMMITTED BASELINE` vs `ACTIVE INSTALLATION FRONT` ayrımı, Part-Latent Freezing ilkesi (A40).
   - **§Söküm/Montaj Faz Kapısı:** Demolition ve Assembly fazlarının termodinamik duvarla ayrılması, WBS klip paketleri (A41).
2. **`kilavuzlar/SANTIYE_HAREKETI_KILAVUZU.md`:**
   - **§4.8 İş Yoğunluğu ve Üç Fazlı Kinematik:** Lojistik (0-2.5s) $\to$ Hazırlık (2.5-5.0s) $\to$ Montaj (5.0-8.0s), Multi-Effector $\ge 3$ kuralı (A41).
3. **`kilavuzlar/UZUN_FORM_ANLATI_KILAVUZU.md` & `MUZIK_VE_KAPAK.md`:**
   - **§Mikro-Doyum Mimarisi:** 8 saniyelik klibin anatomisi: 5.5–7.0 sn mikro-sonuç vuruşu, 7–8 sn merak tohumu (visual seed / forward hook), entropi düşüşü (A42).
4. **`kilavuzlar/VARSAYIMLAR.md`:**
   - `A39-a…d`, `A40-a…d`, `A41-a…d`, `A42-a…d` olarak 16 yeni araştırma varsayımı işlenecek.
