# A22 — RUBRİK TASARIMI VE PUAN BİRLEŞTİRME · HAM RAPOR

```
KÜNYE
BOT          Gemini Deep Research (TAHMİN — metindeki "[cite: n]" işaretleri o aracın
             imzasıdır; proje sahibi doğrular)
TARİH        06.10.2026 — proje sahibi ajana bu tarihte verdi (beş rapor tek mesajda)
PROMPT       arastirma/A22_RUBRIK_TASARIMI.md · v1 · altı cümle
KESİLDİ Mİ   BİLİNMİYOR — proje sahibi doldurur
SÜRE         BİLİNMİYOR — proje sahibi doldurur
BİÇİM NOTU   Yapıştırmada tablo yapısı kısmen düştü; hücreler bitişik metin olarak geldi.
             Aşağısı geldiği gibidir — düzenleme · kısaltma · özetleme YOK [kart S].
             Denetim: SONUCLAR/A20-A24_DENETIM.md
```

---

Çok Kipli Dil Modelleri İçin Kapsamlı Değerlendirme ve Psikometrik Ölçek Tasarımı Raporu
Büyük dil modellerinin (LLM) değerlendirici hakem olarak (LLM-as-a-judge) kullanıldığı sistemler, özellikle yapılandırılmamış çok kipli verilerin (inşaat timelapse filmleri) kalite kontrolünde büyük bir potansiyel sunmakla birlikte, ölçme ve değerlendirme teorisinin temel ilkeleri göz ardı edildiğinde ciddi geçerlilik ve güvenilirlik krizleri yaratır. Gözlemlenen %31 oranındaki kanıtsız kusursuz puanlama (leniency/ceiling effect), aynı kusurun dört farklı boyutta puan düşürmesi (construct overlap) ve modelin kendi verdiği kategorik puanlarla çelişen nihai hükümler (verdict) üretmesi, sistemin psikometrik mimarisindeki yapısal hataların doğrudan bir sonucudur. Bu rapor, söz konusu problemleri gidermek üzere psikometri, rubrik tasarımı ve yapılandırılmış LLM çıktı yönetimi üzerine literatürdeki en güncel ölçümleri ve mimari standartları sentezlemektedir.

Birinci Boyut: Rubrik Mimarisi ve Ölçek Tasarımı Üzerine Psikometrik Analiz
Ölçme araçlarının tasarımı, değerlendiricinin (insan veya yapay zekâ) bilişsel süreçlerini doğrudan şekillendirir. Geleneksel 0-10 veya 1-5 aralıklı Likert ölçekleri, puanların sınırlarını ve anlamlarını yoruma açık bıraktığı için, LLM'ler yüksek puan verme eğilimine (leniency bias) kapılırlar. Bu durum, modelin risk almaktan kaçınması ve ince taneli kusurları tespit etmek için gereken akıl yürütme maliyetinden (reasoning tax) kaçmasıyla açıklanır. Analitik rubrikler, performansı alt bileşenlere bölerek (kamera stabilitesi, zamanın geçişi, aktivite vb.) her birini ayrı puanlarken, bütüncül (holistic) rubrikler tek bir genel puan üretir. LLM-as-a-judge sistemlerinde analitik yaklaşımlar daha yüksek güvenilirlik sunar, ancak ölçek mimarisinin doğru tasarlanmaması durumunda model, boyutlar arasında ayrım yapamayarak (halo effect) tüm kategorilere aynı yüksek puanı basma eğilimi gösterir. [ETİKET: [ÖLÇÜLDÜ] LLM'lerin Likert ölçeklerinde yüksek kaliteli metinleri ayırt etmede başarısız olduğu ve bunun düşük değerlendirici anlaşmasına (IEA) yol açtığı saptanmıştır · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: arXiv:2403.18771]   

Davranışsal Çapalı Derecelendirme Ölçekleri (BARS) ve Leniency Kontrolü
0-10 veya 1-5 skalalarının yarattığı boşlukları kapatmak için Davranışsal Çapalı Derecelendirme Ölçekleri (BARS - Behaviorally Anchored Rating Scales) kullanılır. BARS, her bir puan seviyesini spesifik, gözlemlenebilir davranışsal kanıtlarla tanımlar. İnsan değerlendiriciler üzerinde yapılan çalışmalarda, BARS kullanımının geleneksel Likert ölçeklerine kıyasla değerlendiriciler arası güvenilirliği (inter-rater reliability) ve ölçüm kesinliğini anlamlı düzeyde artırdığı kanıtlanmıştır. [ETİKET: [ÖLÇÜLDÜ] Ambiguite (belirsizlik) açısından yapılan testlerde, katılımcılar Likert ölçeğine 2.30, BARS enstrümanına ise 4.34 puan vererek BARS'ın belirsizliği istatistiksel olarak anlamlı ölçüde azalttığını belirtmiştir · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: Journal of University Teaching & Learning Practice, Vol 16, Issue 3]   

LLM bağlamında tavan etkisini (ceiling effect) ve puan şişmesini önlemenin en kesin yolu, yüksek puanları koşullu kanıt zorunluluğuna bağlamaktır. Modelin serbestçe 10 vermesini engellemek için "zaman damgalı kanıt kuralı" (timestamped evidence constraint) uygulanır. Eğer rubrik, "Açık bir zaman damgası ve görseldeki spesifik bir eylemin betimlemesi yoksa, verilebilecek maksimum puan 7'dir" şeklinde yapılandırılırsa, LLM'in halüsinatif varsayımlarla mükemmel puan atama eğilimi kırılır. [ETİKET: [VARSAYIM] LLM'lerin kanıt sunmadan 10 verme eğilimini kırmak için yüksek puanlar deterministik kanıt sağlama zorunluluğuna (extractive justification) bağlanmalıdır · KAYNAK SINIFI: psikometrik prensip · ÇÖZÜMLENEBİLİR KAYNAK: BARS tasarımı genel teorisi]

Geçti/Kaldı Kontrol Listeleri ve İkili (Boolean) Değerlendirme Çerçeveleri
Son dönem araştırmaları, sürekli ölçekler (continuous scales) yerine değerlendirmeyi atomik alt sorulara bölen "Checklist-based" (CheckEval) yöntemlerin LLM yargı sistemlerinde devrim yarattığını göstermektedir. G-Eval gibi sistemler, zincirleme akıl yürütme (Chain-of-Thought) ve olasılık ağırlıklı puanlama kullansalar da, sürekli ölçeklerde kravat (tie) sorunları ve tutarsızlıklar yaşarlar. CheckEval ise karmaşık rubrikleri evet/hayır (Boolean) sorularına indirgeyerek modelin soyut "8 mi 9 mu?" kararsızlığını ortadan kaldırır ve kararları %100 izlenebilir kılar. [ETİKET: [ÖLÇÜLDÜ] CheckEval, Likert tabanlı G-Eval ve SEEval sistemlerine kıyasla LLM'ler arası varyansı düşürmüş ve daha yüksek değerlendiriciler arası anlaşma (IEA) sağlamıştır · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: arXiv:2403.18771]   

Ayrıca, LLM değerlendirmelerinde pozisyon önyargısını (position bias) hafifletmek için tasarlanan TICK sistemi ve hizalama beceri setlerini ince taneli olarak (FLASK) analiz eden yöntemler, modelin belirli bağlamlara aşırı odaklanmasını önler. [ETİKET: [İDDİA] TICK mekanizması, modellerin sunulan seçeneklerden ilkine yönelme eğilimini (position bias) hafifletir · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: arXiv:2603.14473]   

Değerlendirme Yaklaşımı    Ölçek Mimarisi ve Format    İnsan Yargısıyla Uyum (Korelasyon / Anlaşma)    Özellikler ve Saptanan Etkiler    Etiket ve Kaynak Çözümlemesi
G-Eval (GPT-4)    1-5 veya 0-10 (Olasılık ağırlıklı)    Spearman 0.514 (SummEval üzerinde)    Puan yığılması yaşanır, yüksek kaliteli verilerde ayrım zorlaşır.    
[ETİKET: [ÖLÇÜLDÜ] SummEval verisetinde Spearman korelasyonu 0.514 · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: arXiv:2303.16634]

[cite: 8]

CheckEval    İkili (Boolean / Geçti-Kaldı)    Pearson/Spearman ~0.53 - 0.58    Karar matrisini atomik birimlere bölerek varyansı düşürür, Fleiss' Kappa değerini artırır.    
[ETİKET: [ÖLÇÜLDÜ] G-Eval'e göre daha yüksek insan korelasyonu ve daha düşük model varyansı · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: arXiv:2403.18771]

[cite: 6, 12]

FLASK    1-5 (Beceri seti bazlı ince taneli)    Spearman ~0.55 - 0.60    Bilişsel yetenekleri (Mantıksal Düşünme, Arka Plan Bilgisi) alt metriklere ayırır.    
[ETİKET: [ÖLÇÜLDÜ] RLHF ayarlı modellerde model-insan uyumu ölçüldü · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: arXiv:2307.10928]

[cite: 9, 13]

Prometheus    1-5 (Dinamik/Özel Rubrik)    BİLİNMİYOR (Doğrudan eşleştirilmiş bir sayı verilmedi, ancak baselinelardan yüksek)    Doğrudan değerlendirme ve ikili karşılaştırma metriklerini destekler.    
[ETİKET: [İDDİA] İnce taneli rubrik kapasitesi sağlar · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: arXiv:2310.08491]

[cite: 14]

İkinci Boyut: Puan Birleştirme (Aggregation) ve Psikometrik Mimari
Mevcut sistemde tespit edilen, ikisi 4, biri 6, dokuzu 8 kategori taşıyan rubriklerin eşit ağırlıkla genel film ortalamasına girmesi, alt-kategori seviyesinde büyük bir matematiksel asimetri yaratır. 4 kategorili bir rubrikteki her bir alt kategori, 8 kategorili bir rubrikteki alt kategoriden toplam puana etki bakımından iki kat daha fazla ağırlığa sahip olmaktadır. Bu tür dengesizlikleri çözmek için puan birleştirme mekanizmalarının yeniden kurgulanması zorunludur.

Telafi Edici (Compensatory) ve Telafi Etmeyen (Conjunctive) Modeller
Psikometrik puanlamada iki temel yaklaşım vardır:

Telafi Edici (Compensatory) Model: Bir boyuttaki zayıf performans, başka bir boyuttaki yüksek performansla kompanse edilebilir. Basit ortalama alma (average) işlemleri bu sınıfa girer.   

Telafi Etmeyen (Conjunctive) Model: Genel bir geçer not almak için, her bir alt bileşenden belirlenen "kesme puanını" (cut score) geçmek zorunludur. Kritik hatalar sistemi doğrudan durdurur. [ETİKET: [ÖLÇÜLDÜ] Conjunctive modeller, adayların zayıf yönlerini diğer alanlarla telafi edememesi için her bir bileşende asgari kesme puanı gerektirir · KAYNAK SINIFI: eğitim ve psikometri dokümanı · ÇÖZÜMLENEBİLİR KAYNAK: Cogn-IQ Psychometrics / Eğitim Materyali]   

Gerçek dünya kalite kontrol (QC) ve değerlendirme sistemleri bu iki yaklaşımın melez bir versiyonunu kullanır:

Yayın Teknik QC'si (Netflix Post Technology Alliance, Interra Baton): Telafi edici olmayan katı bir (pass/fail) sistemidir. Bir "Auto-fail" kuralı ihlal edilirse (örneğin siyah kare limiti), videonun renk doğruluğunun mükemmel olması bir anlam ifade etmez ve dosya reddedilir.   

Oyun Sertifikasyonu (TRC / Lotcheck): Kapı (gate) ve öldürücü hata (fatal error) sistemidir. Teknik zorunluluklardan (Technical Requirement Checklist) biri sağlanmazsa oyun yayınlanamaz.

Hakemli Spor Puanlaması (ISU Artistik Patinaj): LLM leniency'sine benzer şekilde hakem önyargılarını engellemek için, 9 hakemli bir panelde en yüksek ve en düşük puanlar sistemden atılır (Trimmed mean / Kırpılmış ortalama) ve kalanların ortalaması alınır.   

Mevcut inşaat filmi projesinde, "Vaat teslim edildi mi?" veya "Aynı yapı mı?" gibi unsurlar öldürücü kategori olarak tanımlanmalı ve bunlardan alınan düşük puanlar telafi edilemez (conjunctive) kabul edilerek filmin doğrudan reddedilmesini (FAIL) sağlamalıdır.

Hüküm (Verdict) ile Kategori Çelişkisi ve Koşullu Kategoriler
"Hüküm ile kategoriler çelişirse hüküm kazanır" kuralı, ölçümün doğasına terstir. Kategoriler, hükmü inşa eden kanıtlardır. Profesyonel karar destek sistemlerinde hüküm (verdict), LLM'in bağımsız olarak uydurabileceği bir alan değil, alt kategorilerin deterministik bir hesaplamasıdır. LLM'in final kategorisinde "3/10" verip hükümde "Kusursuz" diyebilmesi, modelin bağlamı kaybetmesi (hallucination) anlamına gelir.

Koşullu ("NOT TRIGGERED") kategoriler ise LLM'e ortalama hesabı yaptırılarak çözülemez. Eğer bir video müziksiz ise, LLM müzik kategorisine "NOT_TRIGGERED" damgası vurmalı ve bu kategori, harici kodda hesaplanan payda (bölen) sayısından çıkartılmalıdır. Model içinde ortalama hesaplatmak, matematiksel halüsinasyonlara davetiye çıkarmaktır.

Çift Sayımın (Double Counting) Önlenmesi: Ayırt Edici Geçerlilik
Büyüyen bir yapının yanında boşta duran bir ekskavatörün dört farklı rubrikte ceza yaratması, psikometride Campbell ve Fiske (1959) tarafından tanımlanan "Multitrait-Multimethod" (MTMM) matrisi ve "Ayırt Edici Geçerlilik" (Discriminant Validity) eksikliği ile açıklanır. Eğer iki farklı ölçüt aynı kusuru ölçüyorsa, bu ölçütler bağımsız değildir.   

Modern yapısal eşitlik modellemelerinde bu örtüşmeyi tespit etmek için Henseler ve arkadaşları (2015) tarafından geliştirilen Heterotrait-Monotrait (HTMT) oranı kullanılır. [ETİKET: [ÖLÇÜLDÜ] İki yapı arasındaki HTMT oranının 0.85 (katı eşik) veya 0.90 (esnek eşik) üzerinde olması, bu yapıların ampirik olarak ayırt edilemez olduğunu ve aynı şeyi ölçtüklerini kanıtlar · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: Journal of the Academy of Marketing Science, 2015 (Henseler et al.)].   

Bu çift sayımı önlemek (Construct Fencing) için her bir rubriğe sınır talimatları yazılmalıdır. Eğer ekskavatör hareketsizse, bu kusurun "sahibi" yalnızca Activity_and_Inventory kategorisidir. Diğer kategorilere (örneğin Continuous_World) "Ekipman hareketsizliği Aktivite boyutunda değerlendirilmiştir, burada tekrar ceza uygulama" şeklinde dışlayıcı komutlar (negative constraints) verilmelidir.

Üçüncü Boyut: Formata Koşullanan Rubrik ve Yapılandırılmış LLM Çıktısı
Format değiştiği halde (müziksiz veya dikey) rubriğin hala müzik temposu sorması veya yatay altı çekim beklemesi, statik prompt (prompt staleness) sorunudur. Ayrı rubrik versiyonları yazmak yerine, rubriğin en üstüne dinamik bir değişken bloğu (Variable Block) enjekte etmek ve LLM'i bu bloğa göre koşullandırmak modern pipeline mimarilerinin standardıdır.

Yapılandırılmış Çıktı (JSON Schema) Vergisi ve Aritmetik Hatalar
LLM'in yapılandırılmış JSON çıktısı üretmeye zorlanması (Structured Output), eksik kategori sorununu şema doğrulama (schema validation) yoluyla teknik olarak sıfıra indirir. Ancak son akademik çalışmalar, JSON şeması dayatmasının modelin akıl yürütme (reasoning) kapasitesini düşürdüğünü ortaya koymuştur. Buna "Yapılandırma Vergisi" (Formatting Tax) denir. [ETİKET: [ÖLÇÜLDÜ] Zorlu görevlerde eşzamanlı JSON formatlaması ve akıl yürütme dayatması, GPT-4o-mini ve Haiku gibi modellerde isabet oranını %28 ila %36 oranında düşürmüştür · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: arXiv:2606.09410].   

Bu vergiden kaçınmak için "Gecikmeli Yapılandırma" (Delayed Structure) kullanılır: Modelden öncelikle her bir kategori için doğal dilde analizini ve zaman damgalı kanıtlarını (Chain of Thought) yazması istenir, ardından JSON formatında puanlamayı basması talep edilir. Ortalama hesabı ise kesinlikle LLM'in inisiyatifine bırakılmamalı; modelin ürettiği geçerli (NOT_TRIGGERED olmayan) puanların havuzlanmış ortalaması (Micro-averaging) harici bir Python/Node kodunda yapılmalıdır.   

Mimari Değişiklik    Beklenen Etki (Ölçülmüş / Mantıksal)    Etiket ve Kaynak Çözümlemesi
Dinamik Değişken Bloğu Ekleme    Rubrik enflasyonunu önler, halüsinasyon riskini (müzik arama) sıfırlar.    [ETİKET: [VARSAYIM] Bağlam penceresi başında verilen değişkenlerin şarta bağlı dallanmayı iyileştirdiği LLM instruction-following prensibidir · KAYNAK SINIFI: sistem mimarisi]
Gecikmeli JSON (Önce CoT, sonra Schema)    JSON formatlamasının yarattığı %30'a varan akıl yürütme kaybını engeller, aritmetik hataları azaltır.    
[ETİKET: [ÖLÇÜLDÜ] Phase 1 doğal dil, Phase 2 JSON ayrımının kapasite sorununu çözdüğü deneylerle sabitlenmiştir · KAYNAK SINIFI: akademik · ÇÖZÜMLENEBİLİR KAYNAK: arXiv:2606.09410]

[cite: 28]

Zaman Damgalı Kanıt Zorunluluğu (Leniency Önlemi)    Kanıtsız %31'lik 10.0 puan yığılmasını dağıtır, modeli kanıt bulamazsa puanı 7'de kesmeye zorlar.    [ETİKET: [VARSAYIM] Extractive kanıt zorunluluğu modelin rastgele yüksek puan basmasını teknik olarak engeller · KAYNAK SINIFI: BARS / Prompt Engineering]
Ortalamayı Kodda Hesaplama    "Final 3/10 ama hüküm geçiyor" gibi model hesaplama tutarsızlıklarını matematiksel olarak sıfırlar.    [ETİKET: [VARSAYIM] LLM'ler otoregresif metin üreteçleridir, sembolik mantık ve deterministik ortalama için harici kod execution şarttır · KAYNAK SINIFI: bilgisayar bilimleri temeli]
BENİM VARSAYIMLARIMLA ÇELİŞENLER
"Hüküm (Verdict) ile kategoriler çelişirse hüküm kazanır" kuralınız:
Bu kural psikometrik geçerliliğe taban tabana zıttır. Kategoriler, bir videonun kalitesini belirleyen ampirik veri noktalarıdır. LLM'in bu veri noktalarına düşük puan verip, genel hükümde "video harika" demesi, modelin akıl yürütme yeteneğinin (reasoning) çöktüğünü gösterir. Gerçek sistemlerde alt-denetimler başarısızken üst hüküm başarılı sayılamaz. Hüküm, LLM'in bağımsız fikri değil; kategorik puanların kod tarafından hesaplanmış deterministik sonucu olmalıdır.

"12 rubriğin ortalaması karşılaştırma için kullanılıyor" kuralınız:
Farklı sayıda (4, 6, 8) kategori barındıran rubriklerin önce kendi içlerinde, sonra birbirleriyle eşit ağırlıkta ortalanması (Macro-averaging), ciddi bir matematiksel asimetri yaratır. 4 kategorili rubrikteki bir hatanın toplam puana etkisi, 8 kategorili rubrikteki bir hatanın etkisinden iki kat daha fazladır. Doğru yöntem, tetiklenen (NOT_TRIGGERED olmayan) tüm kategorilerin havuzlanıp toplam puanın geçerli kategori sayısına bölünmesi (Micro-averaging) ile elde edilen değerin kullanılmasıdır.

İngilizce RUBRİK İSKELETİ
You are an expert video quality control analyst. Evaluate the provided construction timelapse video strictly according to the criteria below.
You must first process the DYNAMIC CONTEXT VARIABLES. If a category asks about an element that contradicts the context variables, score it as "NOT_TRIGGERED".

DYNAMIC CONTEXT VARIABLES
Playback_Speed: {{SPEED}}

Clip_Count: {{CLIP_COUNT}}

Aspect_Ratio: {{ASPECT_RATIO}}

Has_Music: {{HAS_MUSIC}}

Has_End_Card: {{HAS_END_CARD}}

EVALUATION RULES
NOT TRIGGERED: Any category relying on a false context variable MUST be scored "NOT_TRIGGERED".

DOUBLE COUNTING PREVENTION: Assign defects strictly to their defined domain. Idle equipment is penalized ONLY under 'Activity_and_Inventory', NOT under 'Continuous_World'.

CEILING EFFECT (MAX 7): To assign any score higher than 7, you MUST provide explicit, timestamped evidence (e.g., "At 0:04..."). Without this, the maximum score is 7.

KILLER CATEGORY: If the 'Promise_Delivered' score is less than 5, the entire video fails, regardless of other scores.

CATEGORY DEFINITION
CATEGORY: Time_Passage
Evaluates whether chronological progression is clearly visible in the construction structure.

SCORE 0: No passage of time is evident; visually static.

SCORE 3: Slight shifts in lighting/movement, but structure progress is ambiguous.

SCORE 5: Noticeable progression, but with discontinuous jumps.

SCORE 7: Clear progression of time and structure. (Maximum allowable score if no timestamped evidence is provided).

SCORE 10: Flawless temporal progression. Evidence MUST explicitly cite a specific timestamp showing progression.

OUTPUT FORMAT
Provide your evaluation in the following JSON schema:json
{
"$schema": "http://json-schema.org/draft-07/schema#",
"type": "object",
"properties": {
"Time_Passage": {
"type": "object",
"properties": {
"score": { "type": ["integer", "string"], "description": "0-10, or 'NOT_TRIGGERED'" },
"evidence": { "type": "string", "description": "Mandatory timestamped evidence for scores > 7" }
},
"required": ["score", "evidence"]
},
"Music_Pacing": {
"type": "object",
"properties": {
"score": { "type": ["integer", "string"] },
"evidence": { "type": "string" }
},
"required": ["score", "evidence"]
},
"Promise_Delivered": {
"type": "object",
"properties": {
"score": { "type": "integer" },
"evidence": { "type": "string" }
},
"required": ["score", "evidence"]
},
"Verdict": {
"type": "string",
"enum": ["PASS", "FAIL"],
"description": "Must be FAIL if Promise_Delivered < 5"
}
},
"required": ["Time_Passage", "Music_Pacing", "Promise_Delivered", "Verdict"]
}


---

## Kategori, Rubrik ve Film Puanı Birleştirme Formülü

Bu tablo, harici kodda (Python/Node vb.) çalıştırılacak olan birleştirme matematiğini ve HTMT (çift sayımı önleme) bariyerlerini tanımlar. Rubrik seviyesindeki ortalamalar kaldırılmış, tüm maddeler film havuzuna çekilmiştir.

| Kusur Tipi (Gözlem) | Sahiplenen Rubrik / Kategori | Çift Sayımı Önleme (Discriminant) Kuralı | Matematiksel Ağırlığı ve Ortalama Etkisi (Kodda) |
| :--- | :--- | :--- | :--- |
| **Boşta duran / çalışmayan iş makinesi** | `Activity_and_Inventory` | Yalnızca bu kategoriden puan kırılır. `Continuous_World` veya `Reason` kategorileri bu durumu "zaman süreksizliği" olarak değerlendirip tekrar puan kıramaz. | Havuzlanmış Alt-Kategori Ağırlığı. Etki = Puan / (Geçerli Kategori Sayısı N) |
| **Bina değişiyor (Farklı yapı)** | `Same_Structure` | Yalnızca burada cezalandırılır. `Cuts` (Kesmeler) kategorisi bina değiştiği için ayrıca "kötü kesme" cezası veremez. | **ÖLDÜRÜCÜ KATEGORİ:** Eğer bu puan < 5 ise, diğer 11 rubriğin sonucu ne olursa olsun `Film Puanı` iptal edilir ve VEDICT otomatik `FAIL` olur. |
| **Gündüz/Gece aydınlatma kopukluğu** | `Time_Passage` | Aydınlatma farklılıkları sadece burada değerlendirilir. `Camera_Stable` veya `Solidness` bu durumu ceza gerekçesi yapamaz. | Havuzlanmış Alt-Kategori Ağırlığı. Etki = Puan / N |
| **Son Kartın (End Card) Statik Olması** | `Format_Compliance` | Değişken bloğunda `Has_End_Card: False` beyan edilmişse, bu kusur aranamaz ve kategori `NOT_TRIGGERED` olur. | Puan `NOT_TRIGGERED` ise paydaya (bölen sayı N'ye) DAHİL EDİLMEZ. Hesaplama `N - 1` üzerinden yapılır. |

**Deterministik Birleştirme (Micro-Averaging) Formülü (Kod İçinde):**
1. Gelen JSON çıktısındaki tüm kategoriler taranır. `score: "NOT_TRIGGERED"` olanlar diziden çıkarılır.
2. Kalan kategorilerin sayısı `N` (Geçerli Kategori Sayısı) olarak atanır.
3. Kalan kategorilerin puanları toplanarak `Toplam_Puan` elde edilir.
4. `Film Ham Puanı = Toplam_Puan / N`
5. Eğer `Promise_Delivered` veya `Same_Structure` puanı < 5 ise, Film Ham Puanı geçersiz sayılır ve Nihai Hüküm `FAIL` atanır. Aksi halde Nihai Hüküm `PASS` olur.
