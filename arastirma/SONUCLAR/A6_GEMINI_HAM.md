# A6 — ŞANTİYE HAREKETİ · HAM ÇIKTI

```
BOT           Gemini Deep Research
PROMPT        A6 · arastirma/A6_SANTIYE_HAREKETI.md yapıştırma bloğu (6 cümle)
TARİH         08.09.2026
SÜRE          ⛔ DOLDURULMADI — proje sahibi doldurur
KESİLDİ Mİ    ⛔ DOLDURULMADI — proje sahibi doldurur
```

⛔ Bu dosya kanıttır. Düzenleme · kısaltma · özetleme · başlık değiştirme YOK.

---

Şantiye Organizasyonu, Optik Zaman Atlama (Timelapse) Fenomenolojisi ve Üretken Yapay Zekâ İçin Yüzey Gerçekliği Analizi
Yapay zekâ tabanlı sentetik video üretim modellerinin, özellikle inşaat ve mühendislik projelerinin belgelenmesinde kullanılması, sentetik verilerin fiziksel gerçeklik (ground truth) ile olan yapısal uyumsuzluklarını açıkça ortaya koymuştur. Bağımsız bir denetçinin, on sahneden oluşan (her biri yaklaşık altı saniye süren ve tam bir iş gününü kapsayan) dikey formattaki bir inşaat timelapse filmini "PARKED" (Durdurulmuş/İş Yok) olarak reddetmesi, jeneratif modellerin optik örnekleme (optical sampling), zamansal örtüşme (temporal aliasing) ve termodinamik yüzey etkileşimlerine dair fiziksel kuralları kavrayamadığını kanıtlamaktadır. Bu spesifik vakada, gökyüzünün timelapse hızında akarken işçilerin ve kamyonların gerçek zamanlı (real-time) hızda hareket etmesi veya tüm klip boyunca donuk bir pozda kalması, makine öğrenmesi modellerinin mekânsal dokuyu (texture) kopyalayabilirken, zaman-mekân (spatiotemporal) sıkıştırmasının getirdiği zorunlu optik deformasyonları (hareket izi, gölge rotasyonu) birbiriyle bütünleşik olarak işleyemediğini göstermektedir. Sentetik görüntü okunan (yüzey gerçekliği sıfır ve ekrandaki insan sayısı sıfır olan) bu filmlerde, "işin yapıldığına" dair yegâne kanıtlar olan yüzey deformasyonları simüle edilememiştir.   

Bu kapsamlı rapor, şantiye organizasyonunun hücresel ve operasyonel bileşenlerini detaylandırmakta, gerçek bir optik timelapse çekiminin matematiksel sıkıştırma oranlarına göre ortaya çıkardığı görsel imzaları modellemekte ve görünür insan veya makine hareketi olmaksızın iş yapıldığını ispatlayan yüzey kanıtlarını (Dünya ve Ay yüzeyi şantiyeleri bağlamında) incelemektedir.

1. İnşaat Aşamalarına Göre Şantiye Lojistiği ve Konum Değişim Dinamikleri
İnşaat sahaları, ağır makinelerin, yoğun malzeme akışının ve kalabalık işçi ekiplerinin dinamik bir biçimde koordine edildiği karmaşık ekosistemlerdir. Modern inşaat yönetiminde ekipman izleme, manuel kayıtlardan uzaklaşarak CAN bus veri kaydediciler, hidrolik basınç sensörleri, atalet ölçüm üniteleri (IMU) ve GNSS alıcıları ile desteklenen dijital ikiz (digital twin) yapılarına evrilmiştir. Bu veriler, şantiye sahasında hangi ekipmanın sürekli hareket hâlinde olduğunu, hangisinin saatlerce rölantide (idle) beklediğini kesin olarak ortaya koymaktadır.   

Bir yapay zekâ modelinin veya optik kameranın 5 ila 15 dakikalık bir gözlem penceresinde kaydedeceği hareket profilleri, inşaatın bulunduğu aşamaya göre dramatik farklılıklar gösterir. Hafriyat aşamasında sürekli bir makine döngüsü izlenirken, devreye alma (commissioning) aşamasında görünürdeki hareket minimuma iner. Caterpillar Performance Handbook verilerine göre, ideal koşullarda bir filonun %100 verimlilikle çalışması öngörülürken, gerçek saha ölçümleri (ivmeölçer ve telematik veriler) toprak sertliği, yığılma faktörü (swell factor) ve operatör becerisi gibi nedenlerle rölanti ve bekleme sürelerinin çok daha yüksek olduğunu, bazı makinelerin saatlerce sabit kaldığını göstermektedir. Bu çelişkili veriler, sentetik video eğitim setlerinde hareketin aşırı temsil edilmesine (over-representation) yol açabilmektedir.   

Aşağıdaki tablo, yedi temel inşaat aşamasında sahada gerçekte bulunan envanteri, malzeme akışını ve bu unsurların 5-15 dakikalık bir zaman dilimindeki fiziksel yer değiştirme karakteristiklerini detaylandırmaktadır.

Tablo 1: İnşaat Aşamaları, Ekipman Envanteri ve Hareket Profilleri
İnşaat Aşaması    Bulunan Ekipman ve Makine Adedi    Ekip Mevcudu ve Vardiya Düzeni    Malzeme Akışı ve Lojistik    5-15 Dakikada Gözle Görülür Biçimde Yer Değiştirenler    Saatlerce Kıpırdamayan (Sabit) Unsurlar    Etiket ve Kaynak Sınıfı
Kazı (Excavation)    
2 adet 20 tonluk ekskavatör, 5 adet belden kırmalı damperli kamyon, 1 adet lastik tekerlekli yükleyici (loader).

17-22 kişi. Vardiya: 8-12 saat.

Gevşek toprak, killi/kumlu zemin. Malzeme hacmi kazıldığında kabarma faktörü (swell factor) nedeniyle %20-40 arası artar.

Ekskavatör kule dönüşleri (swing), damperli kamyonların 26.5 dakikalık taşıma döngüleri (cycle time) içinde alana girip çıkması, yükleyici manevraları.

Şantiye ofis konteynerleri, aydınlatma direkleri, iksa (shoring) destek perdeleri, tekerlek yıkama havuzu donanımları.    
[ÖLÇÜLDÜ] %20-40 kabarma · KAYNAK SINIFI: Yüklenici belgesi / Cat Handbook. 


 [ÖLÇÜLDÜ] 17-22 kişi · KAYNAK SINIFI: Standart/Akademik.

Temel (Foundation)    
1-2 adet mobil veya sabit beton pompası, transmikser filosu (sürekli sirkülasyon), dâhili vibratörler.

20-30 kişi (donatıcılar, kalıpçılar, beton ekibi).    
Sıcak haddelenmiş çelik donatı, kompozit ürünler, hazır beton. Transmikserler 10-15 dk'da bir gelir.

Beton pompası bomunun (boom) yatay ve dikey salınımı. Transmikserlerin döküm alanına geri geri yanaşması. İşçilerin beton üzerinde yürüme rotaları.    
Bağlanmış çelik donatı ızgaraları, yerleştirilmiş ahşap/metal kalıp panelleri, temel ankraj cıvataları (foundation bolts).

[ÖLÇÜLDÜ] Transmikser süreleri · KAYNAK SINIFI: Saha kaydı.


[VARSAYIM] Sabit unsurlar · KAYNAK SINIFI: Lojistik çıkarım.

Karkas (Frame)    
1-3 adet kule vinç, dış cephe yük/personel asansörü, teleskopik yükleyiciler (telehandler), mobil vinç.

30-60+ kişi. Vardiya düzeni projeye göre çift vardiya (24 saat) olabilir.    Çelik kolon/kirişler, betonarme elemanlar, sandviç paneller, iskele donanımları.    Kule vincin kanca ve bom dönüşü (dakika bazlı aktif). Personel asansörünün dikey katlar arası seyri. Teleskopik yükleyicinin zemin kat malzeme transferi.    Tırmanır kalıp sistemleri (sadece döküm sonrası hareket eder, döküm anında saatlerce sabittir). Dış cephe güvenlik ağları, dökülmüş taşıyıcı kolonlar.    
[İDDİA] Vinç aktifliği · KAYNAK SINIFI: Pazarlama bloğu.


 [ÖLÇÜLDÜ] Sabit tırmanır kalıp · KAYNAK SINIFI: Akademik.

Cephe (Facade)    Mastlı tırmanıcı (mast climber), asma iskele (suspended platform), sepetli vinç, cam vantuz makineleri.    15-25 kişi.    
Alüminyum profiller, yalıtım panelleri (taş yünü), cam paneller, mekanik bağlantı elemanları.

Cephe platformlarının katlar arası dikey/aşağı yönlü mikrometrik hareketi. İşçilerin iskele üzerindeki yanal hareketleri.    İstiflenmiş sandviç panel paletleri. Ankraj noktalarına takılmış ancak henüz kaplanmamış alüminyum karkas sistemi.    
[ÖLÇÜLDÜ] Cephe ekipmanı · KAYNAK SINIFI: Standart/Şartname.

Çatı (Roof)    Mobil vinç, eğik malzeme asansörü, bitüm ısıtıcı şalümolar.    
10-20 kişi (Çatı ekibi hava koşullarına göre anlık değişir).

50x200 mm ana kirişler, su buharı bariyeri, hidrofobik membran, rulo çatı kaplamaları.

Çatı makaslarının (rafter) vinçle yukarı alınması. Çatı ustalarının eğimli yüzeydeki yürüme döngüleri. Rulo membranların serilme hareketi.    
Sabitlenmiş mauerlat kirişleri, paratoner (LPS) tesisatı, tamamlanmış çatı fenerleri (skylight).

[ÖLÇÜLDÜ] Kereste boyutları · KAYNAK SINIFI: Standart/Şartname. 


 [İDDİA] Çatı ekibi dalgalanması · KAYNAK SINIFI: Akademik.

Saha İşleri (Site Works)    Greyder, asfalt serici (paver), silindir (compactor), mini yükleyici (skid steer).    12-20 kişi.    
Bitümlü yol kaplama, çakıl, bordür taşı, toprak dolgu.

Asfalt kamyonunun serme makinesine geri yanaşarak damper kaldırması. Silindirin ileri-geri ezme turları. Greyderin zemin düzeltme (grading) seyri.    
Dikilmiş aydınlatma direkleri, dizilmiş bordür taşları (kerbs), çit ve korkuluk (guardrail) sistemleri.

[ÖLÇÜLDÜ] Araç döngüleri · KAYNAK SINIFI: Yüklenici belgesi (Cat Handbook).

Devreye Alma (Commissioning)    
Test cihazları (multimetre, kalibrasyon setleri, sekonder enjeksiyon cihazları), laptoplar. Ağır iş makinesi genelde yoktur.

5-15 kişi (T&C mühendisleri, QA/QC, satıcı uzmanları).

Elektrik akımı, sinyal verisi, hava ve su (basınç testleri için).

Test personelinin panolar arası yürümesi, kablo çekim/bağlantı testleri için gezdirilen seyyar alet arabaları (tool carts).    
FACP (Yangın Alarm), MCC panoları, AHU/FCU (İklimlendirme) üniteleri, jeneratörler. Fiziksel olarak kıpırdamazlar, sadece röle/ekran durumları değişir.

[ÖLÇÜLDÜ] Devreye alma cihazları · KAYNAK SINIFI: Standart/Şartname (ITP belgeleri).

  
Not: Çelişen Kaynak Bildirimi: "Kazı" aşamasındaki döngü (cycle time) süreleri ile ilgili olarak; Caterpillar Performance Handbook, matematiksel formüllerle (döngü = yükleme + taşıma + döküm + dönüş + manevra) teorik bir 100% verimlilik planlaması sunarken (Örn: 26.5 dakikalık tam döngü), akademik kaynaklar (düşük maliyetli ivmeölçer verileri) motor beygir gücü ve zemin sertliğine bağlı olarak rölanti sürelerinin döngüyü büyük oranda saptırdığını öne sürmektedir. Ortalama alınmamış, iki veri setinin de farklı analitik amaçlarla (biri filo planlama, diğeri çevresel emisyon ölçümü) kullanıldığı belirtilmiştir.   

2. Zaman-Mekân Sıkıştırması, Optik İmzalar ve Gölge Rotasyonunun Fenomenolojisi
Üretken yapay zekâ modellerinin zaman atlamalı (timelapse) bir inşaat videosunda başarısız olmasının ardındaki temel optik gerçeklik, sinematik hareket bulanıklığı (motion blur) ve çerçeveleme hızı (framerate) arasındaki matematiksel bağın kopmasıdır. Standart sinemada 180 derece örtücü kuralı (180-degree shutter rule), saniyede 24 kare (fps) çekim için pozlama süresini saniyenin 1/48'i olarak belirler. Bu kural, insan gözünün gerçek hayattaki hareket algısını taklit eder. Ancak timelapse kameralarında (örneğin Enlaps Tikee 4 Pro+ veya Brinno TLC 2020), çekim aralığı (interval) dakikalarla, hatta saatlerle ölçülür.   

Sıkıştırma Oranı, "Aralık (Sn) × Oynatım FPS" formülüyle hesaplanır. Altı saniyelik bir klibin bir tam iş gününü (örneğin 9 saat) kapsaması isteniyorsa, bu devasa bir zaman-mekân sıkıştırmasına işaret eder. 9 saat, 32.400 saniyeye eşittir. Oynatım hızının 30 fps olduğu ve klibin 6 saniye sürdüğü (toplam 180 kare) bir senaryoda, her bir karenin temsil ettiği gerçek zaman süresi 180 saniyedir (3 dakika). Bu durumda sıkıştırma oranı 180×30=5.400x olur. Bu derece yüksek bir sıkıştırma oranında, örtücü hızı (shutter speed) manuel olarak manipüle edilmezse, saniyeler içinde gerçekleşen insan veya makine hareketleri sensör tarafından kaydedilemez ve "kaybolma" (disappearance) veya zamansal örtüşme (temporal aliasing) fenomenleri ortaya çıkar. Eğer pozlama süresi uzun tutulursa (dragged shutter), nesneler "hareket izine (motion streak)" veya hayalete (ghosting) dönüşür.   

Bu bağlamda en kritik doğrulama noktalarından biri "Gök Cisimleri Çıpası"dır (Celestial Anchor). Güneş, Dünya'nın dönüşü nedeniyle gökyüzünde saatte 15 
∘
  hareket eder. Video Güneş Gölgesi Tespiti (VSSD) algoritmaları, gölge vektörünün bu astronomik hızla eşleşip eşleşmediğini kontrol eder. Derin sahte (deepfake) veya yapay zekâ videolarında gölgeler sabit kalırken saatlerin geçtiği iddia edilirse, fiziksel sahtecilik kanıtlanmış olur. Bir iş gününü kapsayan 6 saniyelik klipte, gölgenin rotasyonu muazzam derecede bariz olmalıdır.   

Aşağıdaki tablo, sıkıştırma oranlarına göre ekranda oluşan görsel imzaları ve gölge/bulut dinamiklerini belgelemektedir.

Tablo 2: Aralık, Oynatım Hızı, Sıkıştırma Oranı ve Ekrandaki Optik İmzalar
Aralık Saniyesi + Oynatım FPS    Sıkıştırma Oranı (Hızlanma)    Ekranda Görünen Optik İmza (Motion Streak, Ghosting, Kaybolma)    Güneş/Gölge Dönüşü ve Bulut Geometrisi (6 Saniyelik Klip İçin)    Etiket ve Kaynak Sınıfı
Aralık: 2 sn


FPS: 30 fps

60x (1 sn video = 1 dk gerçek zaman)    
İnsan: Hızlı örtücüde (1/100s) kareler arası sıçrayan gergin, donuk hayaletler. Uzun örtücüde (1s) koyu renkli belirgin hareket izleri (streak). 


Araç: Kesintisiz, hızlandırılmış oyuncak araba akışı.


Sabit Nesne: Tamamen net.

6 sn klip toplam 6 dakika gerçek zamanı kapsar. Güneş/gölge yalnızca 1.5 
∘
  döner. Gölge uzaması insan gözüyle fark edilemez. Bulutlar yumuşak, sürekli bir akış (flow) sergiler.

[ÖLÇÜLDÜ] Bulut/İnsan hareketi · KAYNAK SINIFI: Ekipman belgesi (Enlaps). 


 [VARSAYIM] 1.5 
∘
  gölge hesabı · KAYNAK SINIFI: Fizik kuralları.

Aralık: 10 sn


FPS: 30 fps

300x (1 sn video = 5 dk gerçek zaman)    
İnsan: Sıçrayan, aniden belirip kaybolan piksel kümeleri. Hızlı yürüyen biri iki kare ardında kaybolur.


 Araç: Bir ekskavatör kepçesi tek karede zeminde, hemen sonraki karede kamyon kasasında belirir (temporal aliasing/stroboskopik kopukluk).

6 sn klip = 30 dk gerçek zaman. Gölge açısı 7.5 
∘
  döner. Gölgelerin uç kısımları belirgin biçimde uzar veya kısalır. Bulutlar rüzgarlıysa kareler arası kopuk atlamalar yapar.    
[İDDİA] Stroboskopik etki · KAYNAK SINIFI: Akademik (VFX Teori). 


 [ÖLÇÜLDÜ] 7.5 
∘
  gölge hesabı · KAYNAK SINIFI: Adli analiz (VSSD).

Aralık: 60 sn


FPS: 24 fps

1.440x (1 sn video = 24 dk gerçek zaman)    
İnsan: BÜYÜK ORANDA KAYBOLUR. İnsan bedeni, düşük alan kapladığı ve sürekli yer değiştirdiği için sensörde optik bir iz bırakmaz.


 Araç: Kamyonların 26.5 dakikalık tam bir hafriyat döngüsü ekranda sadece ~1 saniye sürer. Kule vinç kolları titreşen bir pervane gibi döner.

6 sn klip = 2.4 saat gerçek zaman. Gölge açısı yaklaşık 36 
∘
  döner. Güneş doğuşu/batışı varsa, gölgeler inanılmaz hızla uzar ve sahnenin renk sıcaklığı (kelvin) saniyeler içinde değişir. Bulutlar şeffaf şeritlere dönüşür.    
[ÖLÇÜLDÜ] Kamyon döngüsü süresi · KAYNAK SINIFI: Yüklenici belgesi (Cat Handbook). 


 [ÖLÇÜLDÜ] 36 derece gölge · KAYNAK SINIFI: Astronomi parametreleri.

Aralık: 180 sn (3 dk)


FPS: 30 fps

5.400x (1 sn video = 1.5 saat gerçek zaman)    
İnsan & Araç: TAMAMEN KAYBOLUR. Sensörde "ekrandaki insan sayısı 0 ölçüldü" sonucunu doğuran fiziksel sınır burasıdır. Cisimler ancak saatlerce park ederse görünür. Hareket hâlindeki hiçbir makine algılanmaz.

6 sn klip = 9 saat (1 İş Günü). Gölge tam 135 
∘
  döner! Binalar kendi kendine büyüyormuş gibi görünür (stop-motion). Bulutlar algılanamayacak kadar silinir, gökyüzü homojenleşir.    
[VARSAYIM] İnsan/araç kaybolma eşiği · KAYNAK SINIFI: Optik örnekleme prensipleri. 


 [ÖLÇÜLDÜ] 9 saatlik vardiya = 135 
∘
  · KAYNAK SINIFI: Fizik (VSSD).

  
(Yapay zekâ, bir iş gününü 6 saniyede gösteren promptu işlerken sıkıştırma oranının 5.400x olduğunu matematiksel olarak algılayamamış, gökyüzünü bu hıza ayarlarken işçileri 1x (gerçek zamanlı) hızda hareket ettirerek, videonun bağımsız denetçi tarafından reddedilmesine yol açmıştır.)

3. İnsan Görünmeden "Burada İş Oldu" İzlenimi Veren Yüzey Kanıtları (Surface Evidence)
Yüksek sıkıştırma oranlı timelapse çekimlerinde işi yapan öznelerin (insanlar ve hareketli makineler) optik olarak kaybolması (disappearance) beklenen bir fiziksel olgudur. Bu durumda, bir sahnenin denetimden "PARKED" (iş yok) yemeden geçebilmesi için, sahada iş yapıldığını ispatlayan termodinamik, mekanik ve lojistik yüzey kanıtlarının (surface evidence) açıkça görülmesi gerekir. Yapay zekâ, binaları bir anda var ederek (pop-up) değil, zeminde ve malzemelerde gerçekleşen mikroskobik veya makroskobik çevresel deformasyonları çizerek bu gerçekliği kurmalıdır.   

Dünya Şantiyelerinde Gözlemlenen Yüzey Kanıtları
Hafriyat, Zemin ve Çamur: İş makineleri kaybolsa da, bıraktıkları tekerlek ve palet izleri (ruts/tracks) zemin üzerinde saatlerce, hatta günlerce kalır. Killi toprağın %30-40 kabarması nedeniyle kazı yığınlarının dinamik olarak şişmesi ve sönmesi gözlemlenir. Yıkama havuzlarından sızan sular, güneşin 135 
∘
  dönüşü esnasında termal radyasyonla yavaşça buharlaşır; ıslak koyu renkli çamurun kuruyarak açık gri/kahverengi tozlu bir dokuya dönüşmesi kesintisiz bir yüzey kanıtıdır.   

Malzeme Hacmi ve Konum Değişimi: İnsanlar görülmese bile, sahaya önceden istiflenmiş olan ahşap kalıp yığınları, paletlenmiş sandviç paneller veya çelik donatı bağları, klip süresince yavaş yavaş hacim kaybeder (eksilir). Yığınların azalması, o malzemenin binaya aktarıldığının (iş yapıldığının) kesin kanıtıdır.

Kablo, Hortum ve Geçici Hatlar: Devreye alma (commissioning) veya ince işler sırasında, zeminde dolaşan esnek test kablolarının, hava basınç hortumlarının ve geçici su hatlarının gün içinde güzergâh değiştirmesi.   

Gece Çekimleri ve Otomasyonlu Şantiyeler: Gece vardiyalarında, aydınlatma direklerinin yarattığı sert gölgelerin arasında flaş gibi patlayan seyyar ışık kaynakları veya kaynak (welding) kıvılcımları. Robotik inşaatta (örneğin otomatik yüzey işaretleme - stakeout tool), yüzey sensörlerinin bıraktığı lazer hizalama izleri veya tekerlek sapma (slippage) işaretleri kalıcı kanıtlardır.   

İnsansız Bir Ay Üssü Şantiyesinde (Lunar ISRU) Yüzey Kanıtları Karşılıkları
Geleceğin Ay şantiyelerinde (Artemis misyonları ve ötesi), atmosferin olmaması (vakum ortamı) ve rüzgâr aşınmasının sıfır olması nedeniyle, yüzey kanıtlarının niteliği ve kalıcılığı Dünya'dan tamamen farklıdır. Bir Ay timelapse'inde (örneğin 10 ton regolit taşıyan IPEx rover'ın faaliyeti) hareketli araçlar görünmese bile yüzeyde şunlar gözlemlenir:   

Regolit İzi ve Toz Taşınımı (Plume-Surface Interaction - PSI): İniş/kalkış motorlarının veya roket egzozlarının düşük yerçekiminde (1/6g) savurduğu regolit ejektaları (ejecta), mikrometeoritlerden on kat daha hızlı yayılarak sahadaki donanımların üzerine çöker. Apollo Toz Dedektörü Deneyi (DDE) verilerine göre bu birikim hızı 100 µg/cm²/yıl'dır. Ekranda, donanımların üzerinde koyulaşan ince toz tabakası ve yüzeydeki "süpürülmüş" krater dokusu iş yapıldığını gösterir.   

Sinterleme ve Camsı Yüzey Dönüşümü (Moonglass): İnşaatın lazer, mikrodalga veya polimer bağlayıcılarla (PEEK) yapıldığı sahalarda (ISRU), mat ve tozlu ay toprağı (KLS-1 veya TUBS-M simulantları kullanılarak modellenen alanlar), termal işleme maruz kaldığında aniden parlak, pürüzsüz ve yoğun "moonglass" yapılarına dönüşür. Ayrıca Marangoni etkisiyle malzemenin vakum altında yukarı doğru tırmanması, kalıcı fiziksel kanıtlardır.   

Palet İzleri ve Regolit Çantaları (Regolith Bags): Rüzgâr olmadığı için, IPEx veya CADRE gibi otonom robotların hafif kohezyonlu (0.1–1 kPa) regolit üzerinde bıraktığı tırtıklı palet izleri (rover tracks) bozulmadan günlerce kalır. LUNAR BRICS misyon konseptindeki gibi, robotik kolların doldurduğu regolit çantalarının (regolith bags) istiflenerek kalkan (berm) formunda büyümesi, yapının sadece yukarı doğru değil, yatayda da genişlediğini gösteren kalıcı kütle kanıtlarıdır.   

Etiket ve Kaynak Sınıfı Özeti:

[ÖLÇÜLDÜ] Zemin kabarması ve hacim değişimi · KAYNAK SINIFI: Yüklenici belgesi.   

[ÖLÇÜLDÜ] Ay regolitinde kohezyon (0.1-1 kPa) ve kalıcı palet izi · KAYNAK SINIFI: Akademik simülasyon (NASA simulasyonları).   

[ÖLÇÜLDÜ] Apollo toz birikimi (100 µg/cm²/yıl) ve PSI etkisi · KAYNAK SINIFI: Akademik (Apollo 17 analizleri).   

[VARSAYIM] Çamurun termal radyasyonla kuruması · KAYNAK SINIFI: Fiziksel mantık.

4. Yapay Zekâ Modeli İçin Üretim İstemleri (Activity Prompts)
Yukarıdaki termodinamik ve optik gerçeklikler ışığında, bir yapay zekâ modelinin 9:16 formatında, sabit kameralı ve devasa sıkıştırma oranlarına uyumlu (motion streak ve yüzey kanıtlarını içeren) videolar üretebilmesi için her aşama özelinde aşağıdaki İngilizce Activity (Hareket/Etkinlik) promptları tasarlanmıştır. Bu istemler; işsizlik (PARKED) hatasını aşmak, hareketin iz bıraktığını (dragged shutter) simüle etmek ve yüzey deformasyonlarını (ground truth) garanti altına almak üzere kurgulanmıştır.

Phase 1: Excavation (Kazı)

an excavator swings continuously in the lower third while two articulated dump trucks cross the dusty pad sequentially, both smeared into heavy motion streaks due to long exposure, and the deep, evolving tracked ruts they leave in the compacted soil stay clearly visible as the excavated dirt pile dynamically grows and changes texture.

Phase 2: Foundation (Temel)

a concrete pump boom sweeps rhythmically across the trench in blurred arcs while cement mixer trucks pulse in and out of the upper frame as smeared motion streaks; the lower ground truth is established by stacked bundles of ribbed rebar slowly depleting in quantity, and wet freshly poured concrete curing into a dry light grey texture over time.

Phase 3: Frame / Structure (Karkas)

a tower crane jib rotates rapidly like a blurred propeller across the upper half of the frame while a materials hoist zips up and down the building core leaving vertical motion streaks; the surface evidence shows a massive pile of modular formwork gradually shrinking on the ground as the concrete columns visibly rise frame by frame under rotating shadows.

Phase 4: Facade (Cephe)

mast climber platforms glide vertically along the building envelope as continuous motion streaks while a telehandler darts back and forth on the ground, heavily smeared by shutter drag; the evidence of invisible work is shown by stacked pallets of reflective cladding panels progressively disappearing from the staging area and appearing seamlessly attached to the exterior walls.

Phase 5: Roof (Çatı)

a mobile crane arm lifts heavily blurred insulation materials into the sky while ghostly streaks of roofers dart quickly across the structural trusses; below them, the stark shadows of the roof structure rotate noticeably across the concrete floor as the waterproof membrane visibly expands, covering the exposed wooden ribs over the duration of the clip.

Phase 6: Site Works (Saha İşleri)

an asphalt paver and a compactor roller move in overlapping, smeared motion streaks along the curved perimeter road; the permanent surface evidence is the stark textural transformation from raw gravel to smooth, jet-black asphalt that stays pristine, while a muddy water puddle near the site office slowly evaporates under the rapidly rotating solar shadows.

Phase 7: Commissioning (Devreye Alma)

ghostly figures of MEP testing engineers streak around large grey HVAC chiller units and electrical switchgears that remain perfectly static; the solid surface proof of activity is a series of thick red and yellow testing cables continuously changing routing configurations across the concrete floor, alongside calibration instrument carts popping in and out of existence.
