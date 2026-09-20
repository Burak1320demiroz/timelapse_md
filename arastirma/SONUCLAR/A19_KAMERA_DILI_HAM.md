# 🔬 A19 HAM — Viral timelapse videoları için kamera ve çekim kılavuzu

```
KÜNYE — kart S §1 · beş satır
BOT            ⛔ BEYAN EDİLMEDİ (proje sahibi depo köküne VIRAL_TIMELAPSE_KAMERA_KILAVUZU.md
               adıyla bıraktı; hangi araç/model olduğu yazılmadı — metin "Araştırma tarihi:
               20 Eylül 2026" ve PAGEBREAK/FIGURE işaretleriyle bir derin-araştırma PDF çıktısıdır)
TARİH          20.09.2026 (depoya giriş günü = metnin kendi araştırma tarihi)
KESİLDİ Mİ     hayır — dosyanın tamamı · 72.428 karakter · 896 satır · kökten buraya TAŞINDI,
               içerik değişmedi
PROMPT         ⛔ YOK. Bu depoda yazılmış bir A<n> promptuna cevap değil; sipariş metni bilinmiyor
               ⇒ neyin DIŞARIDA BIRAKILDIĞI da bilinmiyor (A13–A18 ile aynı körlük).
KAYNAK SINIFI  ⭐ üretici beyanı (5 YouTube sayfası · matjoez.com) + araç/platform dokümanı
               (Nikon ×2 · Google Veo prompt rehberi · YouTube Yardım) + ticari site (zeitraffer.biz)
               + erişilemeyen 1 (GoPro 403). 11 kaynağın 10'u bu makinede çekildi ve iddiaya
               AİT çıktı → arastirma/SONUCLAR/A19_DENETIM.md §1. Metnin kendisi de üç bilgi
               sınıfını (doğrulanan · yorum · reçete) ayırır ve reçetelerinin ÖLÇÜLMEDİĞİNİ yazar.
DENETİM        arastirma/SONUCLAR/A19_DENETIM.md
KILAVUZ        kilavuzlar/KAMERA_DILI_KILAVUZU.md
```

⛔ **BURADAN AŞAĞISI HAM ÇIKTIDIR — DOKUNULMAZ.** Düzenleme · kısaltma · özetleme YOK.

---

# Viral timelapse videoları için kamera ve çekim kılavuzu

Gerçek çekim ve yapay zekâ üretimi için açı lens hareket kurgu ve uygulama rehberi

Araştırma tarihi: 20 Eylül 2026

**Temel karar:** Önce izleyicinin fark etmesini istediğin değişimi seç. Sonra bu değişimi en açık gösterecek kamera konumunu belirle. Hareket, yeni bir bilgi açıyorsa eklenmeli. Sabit bir kamera; büyüme, temizlik ve inşaat gibi süreçlerde güçlü bir başlangıç seçeneğidir. Yolculuk ve mekân keşfinde ise kontrollü hareket anlam kazanır.

Bu kılavuz, yüksek izlenmeli timelapse yayınlarından doğrulanabilen bilgileri çekim önerilerine dönüştürür. Kamera gövdesi, lens, bakış açısı, çekim ölçeği, kamera hareketi ve zaman sıkıştırma birbirinden ayrı ele alınır. Böylece “sinematik olsun” gibi belirsiz bir isteğin yerine uygulanabilir bir çekim tarifi yazabilirsin.

**Hızlı başlangıç önerisi:** Dikey bir dönüşüm videosunda yüksekten çapraz ana kadraj, 24-35 mm eşdeğeri lens görünümü ve sabit kamera ile başla. İlk karede sorun, orta bölümde gözle görülür ilerleme, sonda işlevini kazanan sonuç bulunsun. Bu bir üretim önerisidir; doğrulanmış bir viral başarı formülü değildir.

## Kılavuzu nasıl kullanmalısın

| İhtiyacın | Önce bakılacak bölüm |
| --- | --- |
| Hangi gerçek örnekler referans alındı | 1 ve 2 |
| Kamera açıları arasındaki fark | 3 ve 4 |
| Lens ve kamera türü seçimi | 5 ve 6 |
| Sabit çekim mi hareketli çekim mi | 7 ve 8 |
| Gerçek çekimde interval ve pozlama | 9 ve 10 |
| Reels ve TikTok için dikey kadraj | 11 |
| İzlenebilir hikâye ve kurgu | 12 ve 13 |
| Yapay zekâ ve sahne sürekliliği | 14 ve 15 |
| Hazır İngilizce promptlar | 16 |
| Sorun çözme ve yayın öncesi kontrol | 17 ve 18 |
| Kendi kanalında hangi açı daha iyi | 19 |

**Bu metindeki sayısal çekim reçeteleri**, kaynakta açıkça belirtilmedikçe önerilen başlangıç değerleridir. İncelenen videoların gerçek EXIF veya kamera yerleşim ölçümleri olarak okunmamalıdır.

<!-- PAGEBREAK -->

## 1 Araştırmanın kapsamı ve kanıt düzeyi

Örneklem, farklı görsel problemleri kapsayan beş yüksek izlenmeli YouTube yayını ile bir yapımcının hyperlapse çalışmasına ilişkin açıklamasından oluşur. Bu, günün en viral videolarını sıralayan bir liste değildir. Uzun yıllar izlenmiş örnekler, kamera dilini karşılaştırmak için seçilmiştir.

YouTube sayfalarında görünen toplam sayılar aşağıda araştırma tarihindeki değerleriyle kaydedildi. Abone sayısı, konu, yayın yaşı, dağıtım, müzik ve kurgu da sonucu etkiler. Bu tablo tek başına belirli bir kamera açısının izlenmeye neden olduğunu göstermez.

| Yayın ve üretici | Yayın tarihi | Sayfada görülen izlenme | Referans alınan süreç |
| --- | --- | --- | --- |
| 30 Days Timelapse at Sea - JeffHK | 9 Eylül 2017 | 33.248.495 | Deniz yolculuğu ve hava değişimi |
| Official 11 Year Time-Lapse Movie of One World Trade Center - EarthCam | 29 Mayıs 2015 | 28.363.993 | Uzun süreli inşaat |
| TOP 10 time-lapses - 859 Days in 8 minutes - Boxlapse | 9 Aralık 2021 | 11.953.614 | Bitki büyümesi derlemesi |
| TEMPONAUT Top 10 Timelapses 2021 | 19 Aralık 2021 | 22.812.181 | Gıda değişimi ve karınca deneyleri |
| THE LONGEST WAY 1.0 - Christoph Rehage | 20 Mart 2009 | 52.105.043 | Yolculuk boyunca kişisel değişim |

Kaynaklar: [JeffHK](https://www.youtube.com/watch?v=AHrCI9eSJGQ), [EarthCam](https://www.youtube.com/watch?v=NbA89YbWoL8), [Boxlapse](https://www.youtube.com/watch?v=3Z2249JGbf4), [TEMPONAUT](https://www.youtube.com/watch?v=Sw60Ehm1b5c), [Christoph Rehage](https://www.youtube.com/watch?v=5ky6vgQfU24).

**Erişim ve yöntem:** Yayın başlıkları, izlenme sayaçları, açıklamalar ve bölüm işaretleri incelendi. Video akışları bu araştırmada güvenilir biçimde oynatılamadığı için kare kare izleme, kesin açı ölçümü ve tüm sahneleri kapsayan hareket sayımı yapılmış kabul edilmez. Aşağıdaki kamera önerileri, doğrulanan süreçlerden türetilmiş uygulama önerileridir. Süresi verilen kaynak bölümleri, yapımcıların yayınladığı bölüm işaretleridir.

**Üç bilgi sınıfı:** “Doğrulanan bilgi” üretici açıklaması veya resmi dokümana dayanır. “Yorum” bu bilginin üretim açısından anlamıdır. “Reçete” ise kendi çekiminde deneyebileceğin, burada önerilen ayardır. Özellikle kamera modeli ve milimetre bilgisi bu ayrım gözetilerek kullanılmalıdır.

<!-- PAGEBREAK -->

## 2 Yüksek izlenmeli örneklerden uygulanabilir dersler

### 2A JeffHK ile hareketli platforma bağlı kamera

**Doğrulanan bilgi:** Yaklaşık 80.000 fotoğrafın birleştirildiği belirtiliyor. Açıklama, kullanılan ekipmanı Nikon D750 ve Rokinon 12 mm f/2.8 olarak veriyor. Yapımcının bölüm işaretleri arasında 00:32 Samanyolu, 01:45 yük operasyonu, 02:08 yağmur altında limandan ayrılış ve 03:13 şimşekli hava bulunuyor. [Video ve teknik açıklama](https://www.youtube.com/watch?v=AHrCI9eSJGQ)

**Yorum:** Aynı yolculuk, gökyüzü, hava ve liman faaliyetleriyle farklı görsel evreler üretebilir. “Kamera sabit” derken neye göre sabit olduğunu belirtmek gerekir: gemiye bağlı bir kamera karaya göre hareket eder.

**Uyarlama reçetesi:** Araç veya platformun küçük fakat tanınabilir bir parçasını ön planda tut. Dış dünyanın akışı ve hava değişimi bu referans çevresinde okunsun. Düz çizgilerin korunması gereken mimari çekimde balıkgözü görünümünü otomatik kopyalama; 12 mm balıkgözü ile 12 mm doğrusal lens aynı geometrik sonucu vermez.

**AI karşılığı:** “Camera rigidly mounted to the vessel; the vessel remains fixed within the composition while the coastline and sky move relative to it.” Bu, dünyaya sabit tripod talimatından farklıdır.

### 2B EarthCam ile inşaatın okunabilir ilerlemesi

**Doğrulanan bilgi:** Üretici, Ekim 2004 ile 2015 Memorial Day arasındaki ilerlemenin yüz binlerce yüksek çözünürlüklü görüntüyle kaydedildiğini ve yaratıcı ekip tarafından kurgulandığını açıklıyor. Kaynak, şantiye kameralarından söz ediyor; incelenen açıklamada kesin kamera modeli veya lens verilmiyor. [Video ve üretici açıklaması](https://www.youtube.com/watch?v=NbA89YbWoL8)

**Yorum:** Yıllar süren bir dönüşümde güçlü sonuç, yalnızca bütün görüntüleri art arda koymaktan gelmez. İnşaat evreleri arasındaki farkın anlaşılması gerekir.

**Uyarlama reçetesi:** Nihai yapının sığacağı genişlik ve yüksekliği baştan hesapla. Sabit ana kadrajda değişmeyen iki çevre referansı bırak. Temel, taşıyıcı, kaplama ve kullanıma açılma evrelerini ayır. İşçilerin hızlı hareketi binanın gerçekten ilerlemesinin yerini tutmasın.

**AI karşılığı:** Önce yapı geometrisini ve bitmiş halini tanımla. Ara görüntüler bu hedefe doğru tutarlı ilerlesin; bina tek karede belirmesin veya her klipte başka bir yapıya dönüşmesin.

<!-- PAGEBREAK -->

### 2C Boxlapse ile küçük değişimin büyük hikâyesi

**Doğrulanan bilgi:** 2021 derlemesinin bölüm listesinde 00:00 kırmızı ayçiçeği, 02:30 avokado, 04:08 patates ve başka bitkiler yer alıyor. İncelenen video açıklaması kamera modeli ve lensi belirtmiyor. [Video ve bölüm listesi](https://www.youtube.com/watch?v=3Z2249JGbf4)

**Yorum:** Konu bir bina kadar büyük olmak zorunda değildir. Köklenme, filizlenme, yaprak açma ve meyve verme birbirinden anlaşılır evrelerdir. Derlemedeki toplam izlenme, her bitki bölümünün ayrı ayrı aynı performansı gösterdiği anlamına gelmez.

**Uyarlama reçetesi:** Bitkinin son büyüklüğünü hesaba katarak yukarıda ve yanlarda büyüme alanı bırak. Işığı ve arka planı denetle. Toprak altı süreci önemliyse şeffaf bir kesit görünümü planla; yalnızca yukarıdan bakmak kök gelişimini gizleyebilir. Netliği, süreç boyunca önemli olacak derinliğe göre ayarla.

**AI karşılığı:** Aynı saksı, aynı toprak seviyesi, aynı gövde kökü ve aynı arka plan sürsün. Bir bitkinin başka türe dönüşmesini önlemek için tür ve büyüme evresi açıkça belirtilsin.

### 2D TEMPONAUT ile dönüşümün sınırını göstermek

**Doğrulanan bilgi:** Derlemede 00:00 siyah tabakta yumurta, 05:08 tartı üzerindeki meyve ve 11:18 mavi sıvı içen karıncalar gibi bölüm işaretleri bulunuyor. Üreticinin teknik sitesinde çalışmaların tekil fotoğraflardan oluşturulduğu açıklanıyor. İncelenen yayın belirli bir kamera gövdesini doğrulamıyor. [Video](https://www.youtube.com/watch?v=Sw60Ehm1b5c), [üretim yöntemi](https://www.zeitraffer.biz/)

**Yorum:** İzleyicinin takip edeceği görünür bir sınır yararlıdır: azalan sıvı, küçülen nesne, değişen renk veya genişleyen alan. Karıncaların hareketiyle nesnenin değişimi aynı şey değildir; esas dönüşüm ayrı okunmalıdır.

**Uyarlama reçetesi:** Yüzey alanı değişiyorsa tepeden, yükseklik veya hacim değişiyorsa yandan ya da çaprazdan çek. Tek bir ana nesne ve sade çevre kullan. Arka planın da hareket etmesi, küçük değişimleri takip etmeyi zorlaştırabilir.

**AI karşılığı:** Nesnenin başlangıç sınırı ve değişim yönü tanımlansın. Malzeme yalnızca biçim değiştiriyorsa yok olmasın; gerçekten uzaklaştırılıyorsa çıkış yolu görülsün.

<!-- PAGEBREAK -->

### 2E Christoph Rehage ile değişmeyen görsel referans

**Doğrulanan bilgi:** Üretici, Çin yürüyüşü sırasında saç ve sakalını uzattığını belirtiyor. Ayrıca videonun katı bir “her gün tek fotoğraf” dizisi olmadığını; dönüşler ve arka planda olanlar için ilave hareket kullandığını açıklıyor. [Video ve açıklama](https://www.youtube.com/watch?v=5ky6vgQfU24)

**Yorum:** Zamanı anlaşılır kılmak için kadrajın her parçasının aynı kalması gerekmez. İzleyicinin değişimi karşılaştıracağı baskın bir referansın tutarlı olması yeterli olabilir.

**Uyarlama reçetesi:** İnsan olmayan bir dönüşümde de aynı mantığı kullanabilirsin: aynı kapı eşiği, aynı kaya, aynı tezgâh köşesi veya aynı bitki gövdesi. Nesnenin ekrandaki büyüklüğünü mümkün olduğunca sabit tutarak çevredeki değişimi görünür kıl.

### 2F Matjoez ile hareket ve kurgu birlikteliği

**Doğrulanan bilgi:** Matthew Vandeputte, 20 Şubat 2025 tarihli yazısında hyperlapse showreel için o tarihte TikTok'ta 200, Instagram'da 20.000 ve Reddit'te 2,7 milyon görüntüleme bildirmiştir. Maskeleme, hareket animasyonu, hız geçişleri ve ses efektleri kullandığını anlatır. Bunlar üreticinin geçmiş tarihli beyanıdır; güncel sayaç değildir. [Yapımcının açıklaması](https://www.matjoez.com/2025/02/20/five-edits-i-did-to-blow-up-my-showreel/)

**Yorum:** Aynı çalışma, farklı platformlarda çok farklı sonuç verebilir. Görüntüde hissedilen hareketin tamamı çekim sırasında kameranın yaptığı hareket olmayabilir; kurgu da hareket algısını oluşturabilir.

**Uyarlama reçetesi:** Önce anlaşılır bir kamera güzergâhı üret. Sonra hızlanma, yavaşlama ve ses vurgularını görüntüdeki gerçek değişim noktalarına yerleştir. Bir kısa videoda aynı anda orbit, zoom, kamera eğimi ve hız sıçraması kullanmak yerine tek bir ana hareketi test et.

### Bu örneklerin ortak uygulama sonucu

Bir çekim kararı vermeden önce “Ne değişiyor, değişmeyen referans ne, değişimi hangi açı gösteriyor?” sorularını cevapla. Büyüme için son boyuta yer bırakmak, inşaat için aynı geometrinin ilerlemesini korumak, yolculuk için platform ile çevreyi ayırmak, deney için değişim sınırını göstermek farklı çözümlerdir. Hepsini tek bir “viral kamera açısı” altında toplamak yanıltır.

<!-- PAGEBREAK -->

## 3 Bir çekimi tarif eden altı ayrı karar

| Karar | Ne belirler | Örnek |
| --- | --- | --- |
| Kamera türü | Kayıt sistemi ve çalışma olanakları | Telefon, aynasız, aksiyon kamerası |
| Lens | Görüş alanı ve optik özellikler | 24 mm eşdeğeri geniş açı |
| Kamera konumu ve açısı | Nereden ve hangi yönde bakıldığı | Zeminden 3 m yüksek, 30 derece aşağı |
| Çekim ölçeği | Konunun kadrajda ne kadar yer kapladığı | Genel plan, yakın plan |
| Kamera hareketi | Konumun veya yönün zamanla değişimi | Sabit, yana kayış, dolly out |
| Zaman yöntemi | Sürecin nasıl sıkıştırıldığı | Aralıklı fotoğraf, hızlandırılmış video |

“Drone açısı” tek başına yeterli tarif değildir. Drone yerden 15 m yüksekte çapraz bakabilir veya 80 m yüksekte tam aşağı bakabilir. “Makro” da kamera açısı değildir; yakın çekim ve büyütme ile ilgili optik bir kullanımdır. Tripod, slider, gimbal ve vinç kamera gövdesi değil destek veya hareket sistemidir.

### Zaman yöntemini doğru adlandır

**Klasik timelapse:** Aralıklı çekilen fotoğraflar bir video dizisine dönüştürülür. Kamera sabit veya programlanmış bir düzenek üzerinde olabilir. Saatler, günler ve aylar süren süreçlerde uygundur.

**Hızlandırılmış video:** Kesintisiz video çekilir, kurguda hızlandırılır. Dakikalar süren işlem ve gerektiğinde gerçek hıza dönme için kullanışlıdır. Dosya hacmi ve uzun çekimde ısınma hesaba katılmalıdır.

**Hyperlapse:** Zaman sıkıştırılırken kamera mekân içinde belirgin mesafe kat eder. Bir referans noktasının kontrollü takibi, düzgün güzergâh ve stabilizasyon önemlidir. Her hızlı kamera hareketi hyperlapse değildir.

**Sentetik timelapse:** Yapay zekâ, animasyon veya görsel efekt ile zaman geçişi üretilir. Gerçekte aylar süren bir olay kaydedilmiş olduğu anlamına gelmez. Aynı görsel ilkeler kullanılabilir; fizik ve süreklilik ayrıca denetlenir.

Nikon, aralıklı fotoğraflarla çalışma ve kamera içinde timelapse video üretme yöntemlerini ayrı iş akışları olarak açıklar. Fotoğraf dizisi, tek kareleri düzenleme esnekliği sunar. [Nikon teknik rehberi](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/time-lapse-tips-and-tricks-using-nikon-mirrorless-cameras)

<!-- PAGEBREAK -->

## 4 Kamera açısı atlası

### 4A Yükseklik ve bakış yönü

<!-- FIGURE:angles -->
<!-- TEXT-ONLY START -->

| Bakış | Kamera ile konu arasındaki ilişki | Görünen özellik |
| --- | --- | --- |
| Konu hizası | Kamera ana değişimle aynı seviyede | Profil ve yükseklik |
| Alçak açı | Kamera aşağıdan yukarı bakar | Yükselme ve büyüklük |
| Yüksek çapraz | Kamera yukarıdan eğimli bakar | Yüzey alanı ve hacim |
| Tam tepeden | Kamera doğrudan aşağı bakar | Plan, sınırlar ve yüzey düzeni |

<!-- TEXT-ONLY END -->

Bu karşılaştırma aynı konunun farklı yükseklik ve bakış yönlerinden çekilmesini açıklar. PDF'deki çizim ölçülü bir çekim planı değildir.

**Göz hizası veya konu hizası:** Kamera, esas dönüşümün olduğu seviyeye yakın bakar. Bitki gövdesi, masa üzerindeki nesne ve duvar restorasyonu için anlaşılırdır. İnsan bulunmayan sahnede “göz hizası” yerine “saksı ağzı hizası” gibi somut referans yaz. Örnek: 50 mm eşdeğeri, nesneden 1,5 m uzakta, optik eksen yatay.

**Alçak açı:** Kamera konunun altından yukarı bakar. Yükselen yapı, kule, büyüyen bitki veya üstte gerçekleşen hareketi vurgulayabilir. Zemin üstündeki çalışma alanını gizleyebilir. Örnek: kamera 0,4 m yüksekte, 24 mm eşdeğeri, 10 derece yukarı bakış. Bu değerler sahneye göre değiştirilir.

**Yüksek açı:** Kamera yukarıdan aşağı eğimli bakar. Zemindeki düzeni ve nesnenin hacmini birlikte göstermek için kullanışlıdır. Yol onarımı, oda dönüşümü ve küçük şantiye için ilk denenecek seçeneklerden biridir. Örnek: 3 m yükseklik, 8 m uzaklık, 30 derece aşağı eğim, 28 mm eşdeğeri.

**Tam tepeden:** Optik eksen zemine diktir. Plan görünümü; mozaik, temizlik sınırı, tezgâh düzeni, sıvı alanı ve yol çizgileri için güçlüdür. Düşey derinlik zayıf görünür; çukurun derinliği kritikse çapraz açıya ihtiyaç doğar. Tepeden çekim tripod koluyla da yapılabilir; drone zorunlu değildir.

<!-- PAGEBREAK -->

### 4B Nesneye göre yön ve konum

| Açı veya konum | En iyi gösterdiği şey | Başlıca sınırlama |
| --- | --- | --- |
| Cepheden | Simetri, kapı, duvar, raf ve aynı yüzeyin değişimi | Hacim ve derinlik azalabilir |
| Üç çeyrek çapraz | Ön yüz ile yan yüz, alan ile derinlik | Ön plandaki nesne arkayı örtebilir |
| Tam yandan | Yükseklik, su seviyesi, profil ve katman | Geniş alanın diğer tarafı görünmeyebilir |
| Köşeden iç mekân | Odanın iki duvarı ve zemini | Ultra geniş lens köşeleri uzatabilir |
| Araç veya nesneye bağlı | Sabit platform çevresinde geçen dünya | Platform titreşimi büyütülür |
| İş yapan kişinin bakışı | Alet ile yüzeyin teması, işlem hissi | Eller esas değişimi kapatabilir |
| Camdan kesit görünümü | Kök, katman, dolum, erime veya çökelme | Yansıma ve cam kenarları dikkat dağıtabilir |
| Ufku aşağıda bırakan bakış | Bulut ve gökyüzü gelişimi | Zemin dönüşümü küçülür |
| Ufku yukarıda bırakan bakış | Tarla, yol, gölge veya su akışı | Gökyüzü değişimi arka planda kalır |
| Eğik ufuk | Tasarlanmış dengesizlik hissi | Dönüşümü karşılaştırmak güçleşebilir |

**Çapraz açı ne zaman varsayılan seçim olmalı?** Hem zemindeki ilerlemeyi hem de nesnenin yüksekliğini görmen gerekiyorsa. Örneğin havuz dolumunda tepeden açı suyun kapladığı alanı, yan açı seviyeyi, çapraz açı ikisini birlikte gösterebilir. Seçim, videonun sorduğu soruya bağlıdır.

**Konuya bağlı kamera ne zaman seçilmeli?** Çevrenin akışı hikâyenin parçasıysa. Bir tekerlek üstüne kamera koymakla yere tripod koymak aynı süreklilik problemini çözmez. AI promptunda kameranın bağlandığı referans nesne açıkça adlandırılmalıdır.

**Eğik ufuk neden temkinli kullanılmalı?** İzleyici bir yapının gerçekten eğilip eğilmediğini anlamak zorundaysa kamera eğimi ölçütü bozar. Mimari dönüşümde önce düz ufuklu versiyonu dene. Gerilim için eğik kadraj kullanılabilir, ancak bunu fiziksel çökme kanıtı gibi sunma.

<!-- PAGEBREAK -->

### 4C Çekim ölçeğini açıdan ayrı seç

**Çok geniş plan:** Çevrenin tamamı ve ana dönüşümün yeri anlaşılır. Şantiye, kıyı, bulut ve şehir için uygundur. Telefonda bakıldığında ana değişim seçilemiyorsa gereğinden geniştir.

**Genel plan:** Ana nesnenin tamamı ve ihtiyaç duyulan yakın çevre görünür. Kısa dönüşüm videolarının ana planı için kullanışlıdır. Başlangıçta küçük olan nesnenin son hali de kadraja sığmalıdır.

**Orta plan:** Bir faaliyet alanını veya nesnenin bölümünü izletir. Tamir, düzenleme, saksı ve masa üstü süreçlerde ayrıntı ile bağlamı dengeler.

**Yakın plan:** Boya yüzeyi, pas, tomurcuk, dikiş, su çizgisi ve bağlantı gibi kritik değişimleri gösterir. Sonucun bütününü göstermek için ayrıca genel plana ihtiyaç olabilir.

**Çok yakın ve makro çekim:** Küçük bir değişimi görünür hale getirir. Netlik derinliği ve hareket toleransı daralabilir. Her ayrıntının flu olduğu bir çekimde “makro sinematik” görünüm, sürecin anlaşılmasını engelleyebilir.

### Aynı konu için üç farklı ölçek

| Konu | Genel planın sorusu | Yakın planın sorusu | Finalin sorusu |
| --- | --- | --- | --- |
| Yol onarımı | Neresi bozuk | Yüzey nasıl düzeliyor | Yol kullanılabilir mi |
| Bitki | Nereye kadar büyüyecek | İlk filiz nasıl çıkıyor | Son evre neye dönüştü |
| Restorasyon | Nesnenin hali ne | Malzeme nasıl değişiyor | Nesne çalışıyor mu |
| Havuz dolumu | Hangi alan dolacak | Su seviyesi nereye geldi | Alan bütünüyle doldu mu |

**Tek çekim tercihi varsa:** Bütün bu soruları ayrı kameralarla cevaplamak zorunda değilsin. Genel kadrajı, işlem ve sonuç aynı görüntüde okunacak şekilde kur. Yakın planı yalnızca gerçekten gerekli ayrıntı için kullan. Sahne içinde zorunlu olmayan açı değişimi, başlangıç ile sonucu karşılaştırmayı güçleştirir.

**120 piksel kontrolü:** İlk ve son görüntüyü yaklaşık küçük resim boyutuna indir. Ne değiştiğini bu boyutta seçemiyorsan ana nesneyi büyüt, arka planı sadeleştir veya değişimi daha belirgin bir evreden başlat. Bu pratik bir okunurluk kontrolüdür; bir platformun resmi değerlendirme ölçütü değildir.

<!-- PAGEBREAK -->

## 5 Lens seçimi ve perspektif

Aşağıdaki odak uzaklıkları **35 mm tam kare eşdeğeri görüş alanı** olarak verilmiştir. Sensör boyutu farklı bir kamerada lens üzerinde yazan milimetreyi doğrudan eşitleme. AI üretiminde bu sayılar yaklaşık görsel yönlendirmedir; gerçek optik kalibrasyon garantisi vermez.

| Lens görünümü | Başlangıç aralığı | Uygun kullanım | Dikkat edilecek konu |
| --- | --- | --- | --- |
| Ultra geniş doğrusal | 14-20 mm | Dar oda, büyük yapı, yakın ön plan | Kenarda uzama ve küçük kalan ana nesne |
| Geniş | 24-35 mm | Yol, şantiye, oda, mekân keşfi | Çok yaklaşınca ön plan baskınlaşır |
| Normal | 40-60 mm | Nesne, bitki, cephe, masa üstü | Dar alanda geri çekilme ihtiyacı |
| Kısa tele | 70-105 mm | Doku, sıkı mimari detay, uzaktan nesne | Titreşim ve netlik daha görünür olur |
| Tele | 135-300 mm ve üzeri | Uzak bulut katmanları, yoğun şehir ayrıntısı | Atmosfer ve tripod titreşimi |
| Makro özellikli lens | Sıkça 60-105 mm | Tohum, kristal, küçük yüzey değişimi | Büyütme oranı ve çalışma mesafesi |
| Balıkgözü | Modele göre değişir | Bilinçli geniş gökyüzü ve çevre kapsama | Eğrilen çizgiler optik tasarımın parçasıdır |

**Perspektifi belirleyen esas değişken kamera konumudur.** Aynı konumda geniş lensten teleye geçmek görüş alanını daraltır. Kadrajı eşitlemek için kamera geri çekildiğinde yakın ve uzak nesnelerin göreli büyüklüğü değişir. “Tele her durumda mekânı sıkıştırır” cümlesi bu konum değişikliğini atlar.

**Fiziksel yaklaşma ile zoom aynı değildir.** Dolly in sırasında ön ve arka planın birbirine göre konumu değişir; paralaks oluşur. Optik zoom veya dijital büyütme, kamera yer değiştirmediği için aynı paralaksı oluşturmaz. Dijital büyütme ayrıca kullanılabilir piksel sayısını azaltır.

**Netlik derinliği kararı:** Tüm dönüşümün anlaşılması gereken inşaat ve oda videolarında geniş net alanı hedefle. Tomurcuk gibi küçük konularda arka planı yumuşatabilirsin; ancak büyümenin ilerleyeceği bölge netlik alanından çıkmamalıdır. f/8 gibi değerler bir başlangıç denemesidir, her sensör ve makro büyütme için evrensel değildir.

**Lens seçim sırası:** Önce uygun kamera mesafesi, sonra kadrajı kapsayan görüş alanı, sonra netlik derinliği. Lens adını başa yazarak sahne geometrisini ona uydurmaya çalışma.

<!-- PAGEBREAK -->

## 6 Kamera türleri ve hangi işte kullanılacakları

| Kamera türü | Güçlü olduğu iş | Seçerken kontrol et |
| --- | --- | --- |
| Telefon | Hızlı deneme, oda ve masa üstü süreç | Pozlama ve netlik kilidi, güç, ısınma, lens geçişi |
| Kompakt kamera | Küçük ve sabit bir kurulum | Interval desteği, harici güç, manuel kontrol |
| DSLR | Aralıklı fotoğraf dizisi ve değişebilir lens | Deklanşör kullanımı, interval, güç, RAW |
| Aynasız kamera | Kontrollü fotoğraf dizisi ve esnek lens | Elektronik deklanşör davranışı, ışıkta bantlanma |
| Aksiyon kamerası | Dar alan, araç üstü, dış ortam | Görüş alanı bozulması, gece kalitesi, montaj |
| Özel şantiye timelapse sistemi | Haftalar veya aylar süren kayıt | Enerji, hava koruması, saat planı, uzaktan kontrol |
| Drone kamerası | Tepeden alan okuma ve kısa hava güzergâhı | Rüzgâr, pil, konum kararlılığı, tekrar edilebilirlik |
| 360 derece kamera | Çekimden sonra yön seçmek | Yeniden kadrajda ayrıntı kaybı, birleşim çizgileri |
| Sinema kamera sistemi | Video ile karma çekim ve kontrollü prodüksiyon | Uzun kayıt, depolama, güç ve iş akışı |
| Sanal kamera | AI veya 3B üretimde tasarlanan hareket | Geometri, referans tutarlılığı, komutun uygulanması |

Bu tablo model sıralaması veya satın alma listesi değildir. Başarılı bir örnekte kullanılan eski kamera, aynı görüntü dilini üretmek için bugün zorunlu değildir. Bir kamera seçimini; çözünürlükten önce kayıt süresi, enerji ve kontrol gereksinimi üzerinden yap.

### Üç başlangıç kurulumu

**En az ekipman:** Mevcut telefon, sağlam tripod ve sabit ışık. Önce 20-30 dakikalık bir nesne veya masa dönüşümü denemesi yap. Otomatik pozlama, lens değiştirme ve ekran uyku davranışını kısa kayıtta kontrol et.

**Kontrollü üretim:** RAW kaydedebilen kamera, uygun lens, interval kontrolü, harici güç ve sağlam destek. Gün batımı veya uzun süreli büyüme gibi zor koşullarda düzenleme esnekliği sağlar.

**Uzun süreli dış ortam:** Hava korumalı sabit kurulum, yeterli enerji, kayıt takvimi ve düzenli kontrol. Aylar süren süreç için drone'u havada sabit tutma fikri pratik bir ana kayıt çözümü değildir; drone daha çok kısa ek planlara uygundur.

GoPro'nun resmi açıklamasında Time Lapse sabit çekimle, TimeWarp ise stabilizasyonlu hareketli çekimle ilişkilendirilir. Mod ve özellikler modele göre ayrıca kontrol edilmelidir. [GoPro rehberi](https://gopro.com/en/us/news/how-to-make-time-lapse-video)

<!-- PAGEBREAK -->

## 7 Kamera destekleri ve hareketli düzenekler

| Düzenek | Ne sağlar | Timelapse için kritik ayrıntı |
| --- | --- | --- |
| Tripod veya sabit bağlantı | Değişmeyen kamera konumu | Ayakların ve zeminin süreç boyunca oynamaması |
| Tepeden çekim kolu | Masa veya yüzeye dik bakış | Uzun kolun esnememesi ve gölge yapmaması |
| Slider | Kısa doğrusal yer değiştirme | Çok yavaş hareketin aralıklı çekimle eşleşmesi |
| Motorlu pan ve tilt kafası | Kontrollü yön değişimi | Panın yer değiştirme sanılmaması |
| Gimbal | Yürüyüşte yön ve titreşim kontrolü | Konumu kilitlemez; operatörün yolu hâlâ önemlidir |
| Dolly | Zeminde ileri, geri veya yana hareket | Düzgün zemin, yol temizliği ve hız tutarlılığı |
| Jib veya vinç | Yükseklik ve geniş yay hareketi | Hareket yolunun sahneyle uyumu |
| Araç bağlantısı | Platforma göre sabit bakış | Gövde titreşimi ve bağlantı güvenilirliği |

### Hareketli timelapse için iki kayıt yöntemi

**Hareket et dur çek:** Motor konumu değiştirir, durur, titreşim sönünce fotoğraf çekilir. Özellikle uzun pozlamalı slider çekimlerinde kullanılabilir. Bir sonraki kareye geçmeden önce hareket, bekleme, pozlama ve yazma süreleri interval içine sığmalıdır.

**Kesintisiz hareket:** Kamera çekim sırasında da ilerler. Ortaya çıkan bulanıklık hem konu hem kamera hareketinden etkilenir. Çok yakın ön plan ve uzun pozlama birlikte kullanıldığında ayrıntı hızla kaybolabilir. Kısa bir test dizisiyle kontrol et.

### Tripod gerçekten sabit mi

Tripod toprağa gömülüyorsa, güneşte genleşen bir yüzeye bağlıysa veya rüzgârda sallanıyorsa “locked-off” plan bozulabilir. Kadrajda iki sabit çevre noktası seçerek kısa testte yer değiştirip değiştirmediklerini incele. Otomatik netlik ve lensin odak soluması da kamera hareket ediyormuş hissi yaratabilir.

Nikon'un temel timelapse önerileri arasında sağlam tripod ile manuel pozlama ve netlik kullanımı bulunur. Işık büyük ölçüde değişiyorsa pozlama yaklaşımı ayrıca planlanmalıdır; sabit pozlama her koşula uygun değildir. [Nikon temel çekim rehberi](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/top-tips-for-capturing-time-lapse-video-with-a-dslr)

<!-- PAGEBREAK -->

## 8 Kamera hareketi sözlüğü

| Hareket | Fiziksel olarak ne olur | Hangi bilgiyi açar |
| --- | --- | --- |
| Sabit çekim | Konum ve yön değişmez | Aynı yerdeki değişim |
| Pan | Kamera yerinde yatay döner | Alanın başka tarafı |
| Tilt | Kamera yerinde yukarı veya aşağı döner | Yükseklik veya zemindeki ayrıntı |
| Dolly in | Kamera konuya yaklaşır | Kritik ayrıntı ve artan yoğunluk |
| Dolly out | Kamera konudan uzaklaşır | Sonucun bütünü ve çevresi |
| Truck | Kamera yana yer değiştirir | Yüzey boyunca ilerleme, paralaks |
| Pedestal | Kamera düşey yer değiştirir | Engel arkasındaki alan veya yükseklik |
| Arc veya orbit | Kamera konu çevresinde yay çizer | Nesnenin farklı yüzleri |
| Takip | Kamera hareket eden konuya eşlik eder | İşlem ile konu arasındaki ilişki |
| Optik zoom | Lensin odak uzaklığı değişir | Yer değiştirmeden kadraj daralması |
| Dijital büyütme | Görüntü kurguda kırpılıp büyütülür | Küçük kadraj vurgusu |
| Crane reveal | Kamera yükselerek veya yay çizerek alan açar | Başta görünmeyen büyük sonuç |

**Hareketin gerekçesini bir cümlede yaz:** “Kamera geri çekilir; temizlenen küçük parçanın büyük bir avlunun parçası olduğu anlaşılır.” Sadece “daha epik görünür” gerekçesi, hareketin ne kazandıracağını açıklamaz.

**Tek hareket kuralı bir başlangıç yöntemidir:** Kısa klipte önce yalnızca bir ana hareket dene. Yeni bilgi açmayan pan, süreçteki küçük değişimleri izlemeyi zorlaştırabilir. Kamera ve konu aynı anda çok hızlı hareket ediyorsa hangisinin takip edilmesi gerektiği belirsizleşir.

**Yaklaş ve geri çekil:** İlk bölümde ayrıntıya yaklaş, ikinci bölümde geri çekilirken yeni sonucu göster. Kamera yalnızca başlangıç noktasına dönüyor ve yeni bilgi açmıyorsa hareket bir döngüden ibaret kalır. Bunu her videoda otomatik kullanma.

Google'ın video prompt rehberi, sabit çekim, pan, tilt, dolly, truck, pedestal ve zoom gibi komutları ayrı tarif eder; gelişmiş açı ve lens komutlarının güvenilirliğinin değişebileceğini de belirtir. [Google resmi kamera rehberi](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)

<!-- PAGEBREAK -->

### 8A Hareketi sayısal ve uygulanabilir tarif et

<!-- FIGURE:motion -->
<!-- TEXT-ONLY START -->

| Hareket | Kamera konumu | Bakış yönü |
| --- | --- | --- |
| Pan | Sabit | Yatay olarak döner |
| Dolly | İleri veya geri gider | Örnekte aynı yönü korur |
| Truck | Yana gider | Örnekte aynı yönü korur |
| Orbit | Konunun çevresinde yay çizer | Konuya dönük kalır |

<!-- TEXT-ONLY END -->

Kameranın yer değiştirmesi ile yerinde yön değiştirmesi farklıdır. PDF'deki oklar hareket türünü açıklar; gerçek çekim için ölçülmüş bir güzergâh oluşturmaz.

| Önerilen reçete | Kamera tarifi | Kullanım |
| --- | --- | --- |
| Sabit ana plan | Konum, yön, odak ve görüş alanı sabit | İnşaat, temizlik, büyüme |
| Küçük yaklaşma | 8 saniyede 0,4 m ileri, aynı yükseklik | Bir ayrıntıya dikkat çekmek |
| Sonucu açan geri çekilme | 10 saniyede 1,5 m geri, son 2 saniye duruş | Restorasyon veya tamamlanan oda |
| Yana kayış | 8 saniyede 0,8 m sağa, 35 mm görünümü | Ön ve arka planı ayırmak |
| Kısa yay | 10 saniyede 15 derece, sabit yarıçap | Nesnenin ikinci yüzünü göstermek |
| Yavaş pan | 10 saniyede 10 derece, kamera konumu sabit | Geniş bir alanı taramak |
| Kısa yükselme | 8 saniyede 0,7 m yukarı, yön kontrollü | Ön engelin arkasındaki sonucu açmak |
| Kurguda hafif büyütme | Ölçek 1,00'dan 1,06'ya | Sabit çekime sınırlı vurgu |

Bu değerler öneridir. 0,4 m yaklaşma bir makro sahnede çok büyük, geniş bir şantiyede fark edilmeyecek kadar küçük olabilir. Hareketi konuya uzaklık ve kadrajdaki değişimle birlikte değerlendir.

**İki ayrı zaman yaz:** “10 saniyelik çıktı boyunca 1,5 m kamera hareketi; sahnede yaklaşık 2 saatlik işlem sıkıştırılır.” Gerçek çekimde motor hareketi 2 saate yayılır. AI üretiminde aynı ayrım, kameranın da kontrolsüz biçimde hızlanmasını önlemeye yardımcı olabilir.

**Kısa yay, tam turdan önce denenmeli:** Bir nesnenin bilinmeyen arka yüzünü sürekli göstermek; gerçek çekimde kapatma, AI üretiminde geometri değişimi sorunlarını artırır. Önce küçük yay ile bilgi kazanımını ölç.

<!-- PAGEBREAK -->

## 9 Interval süre ve kare hesabı

Timelapse hızını yalnızca “çok hızlı” diyerek belirleme. Son videonun süresi, oynatma kare hızı ve çekilen sürecin süresi birlikte hesaplanmalıdır.

**Değişkenler:** N fotoğraf sayısı, f çıktı kare hızı, L çıktı süresi, delta iki pozlamanın başlangıçları arasındaki süre, T yaklaşık toplam çekim süresi olsun.

```text
N = L × f
L = N / f
T yaklaşık N × delta
delta yaklaşık T / (L × f)
Zaman hızlandırma katsayısı yaklaşık delta × f
```

Planlama hesabında T yaklaşık alınır. İlk pozlamadan son pozlamanın bitişine kadar tam süre yaklaşık (N - 1) × delta + pozlama süresidir. Bazı cihazlar intervali pozlamalar arası bekleme olarak tanımlar; menüdeki anlamı kontrol et.

| Hedef çıktı | Kare hızı | Fotoğraf sayısı | Örnek çekim aralığı | Yaklaşık çekim süresi |
| --- | --- | --- | --- | --- |
| 8 saniye | 30 fps | 240 | 5 saniye | 20 dakika |
| 10 saniye | 30 fps | 300 | 6 saniye | 30 dakika |
| 10 saniye | 24 fps | 240 | 15 saniye | 60 dakika |
| 56 saniye | 30 fps | 1.680 | 5 saniye | 2 saat 20 dakika |
| 60 saniye | 30 fps | 1.800 | 10 saniye | 5 saat |

### Konuya göre ilk denenecek interval

Hızlı yaya veya araç akışı için yaklaşık 0,5-2 saniye; hızlı bulut için 1-3 saniye; yavaş bulut veya gün batımı için 3-10 saniye; kısa iş süreçleri için 2-10 saniye başlangıç denemesi yapılabilir. Bitki büyümesi dakikalar, uzun inşaat ise dakikalar veya daha seyrek örnekleme gerektirebilir. Bunlar tek doğru değerler değildir.

**Karar testi:** Bir önceki ve sonraki karede ana nesne takip edilemeyecek kadar yer değiştiriyorsa interval fazla uzundur. İşçiler bir karede beliren lekeler gibi görünüyorsa daha sık örnekle. Yapı günlerce aynı kalıyorsa çıktıda bu evreye daha az süre ayır.

**Düzensiz örnekleme:** Yalnızca mesai saatleri veya her gün aynı saatte kayıt alınabilir. Bu durumda tek bir sabit “gerçek zaman hızı” tüm videoya uygulanamaz. Özellikle gölge ve mevsim değişiminde zaman atlamaları görünür olur.

<!-- PAGEBREAK -->

## 10 Pozlama netlik ve görüntü sürekliliği

### Pozlama süresi ile interval aynı şey değildir

Interval 4 saniye iken her fotoğrafın pozlaması 1/250 saniye, 0,5 saniye veya 2 saniye olabilir. Kısa pozlama hareketi keskin, uzun pozlama hareket izlerini daha yumuşak gösterir. “30 fps çıktı alıyorum, her kare 1/60 saniye olmalı” düşüncesi timelapse için zorunlu değildir.

Akıcı hareket için pozlamayı intervalin yaklaşık yarısı çevresinde denemek bir seçenektir. Ancak bitkiyi her 10 dakikada bir çekiyorsan 5 dakika pozlama gerekmez. Konunun hareketi, ışık ve hedeflenen görünüm belirleyicidir. Pozlama, kayıt ve varsa motor hareketi interval içine sığmalıdır.

### Sabit ışık ile değişen ışığı ayır

**Sabit ışık:** Manuel pozlama, sabit beyaz dengesi ve kilitli netlik ile başla. Komşu karelerde otomatik ayarların değişmesi parlaklık veya renk sıçraması yaratabilir. LED ışıklarda kısa bir test dizisiyle titreme ve bantlanma kontrolü yap.

**Gündüzden geceye geçiş:** Başlangıç pozlamasını saatlerce sabit bırakmak geceyi kullanılamaz hale getirebilir. Kontrollü pozlama değişimi, uygun otomasyon ve sonradan parlaklık yumuşatma birlikte planlanır. Görüntüyü gelişigüzel otomatiğe bırakmak ile kontrollü geçiş kurmak aynı şey değildir.

**Netlik:** İşlem gören bölge büyüyüp yer değiştiriyorsa netliğin kapsadığı alanı baştan belirle. Kamera her karede yeniden netlik aradığında bulanıklık ve görüş alanı değişimi oluşabilir. Makro çekimde konuya çarpan küçük titreşimler bile önemlidir.

### Pratik kontrol tablosu

| Belirti | Önce kontrol et | İlk düzeltme |
| --- | --- | --- |
| Parlaklık titremesi | Otomatik pozlama, diyafram, ışık kaynağı | Ayarları ve ışığı denetle; uygun deflicker uygula |
| Renk atlaması | Otomatik beyaz dengesi | Sabit WB ve ortak renk düzenleme |
| Karelerin keskinliği değişiyor | Otomatik netlik veya konu hareketi | Netliği kilitle veya net alanı genişlet |
| Düzenli yatay bant | Işık titreşimi ve deklanşör etkileşimi | Pozlama ve kayıt modu testi |
| Ani görüş alanı değişimi | Telefon lens geçişi, dijital stabilizasyon | Lens ve ilgili otomatik ayarları kilitle |
| Kayıp kare veya uzun boşluk | Güç, depolama, işlem süresi | Interval bütçesini ve kayıt güvenilirliğini düzelt |

Nikon kılavuzu, intervalin pozlamaya yeterli süre bırakmasını ve konu hızına göre seçilmesini vurgular. Model özelindeki ayar davranışını kendi cihazının kılavuzundan doğrula. [Nikon interval açıklaması](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/time-lapse-tips-and-tricks-using-nikon-mirrorless-cameras)

<!-- PAGEBREAK -->

## 11 Dikey kadraj ve kırpılma hesabı

<!-- FIGURE:crop -->
<!-- TEXT-ONLY START -->

| Geometri | Piksel ölçüsü |
| --- | --- |
| Yatay kaynak | 1280 × 720 |
| Yüksekliği koruyan 9:16 alan | 405 × 720 |
| Merkez kırpmada soldan çıkarılan genişlik | Yaklaşık 437,5 piksel |
| Merkez kırpmada sağdan çıkarılan genişlik | Yaklaşık 437,5 piksel |
| Korunan yatay genişlik | Yaklaşık yüzde 31,6 |

<!-- TEXT-ONLY END -->

1280 × 720 yatay görüntüden, yüksekliği koruyarak 9:16 merkez kırpma yapılırsa kullanılabilen genişlik **405 pikseldir**. Merkezde yaklaşık x = 437,5 ile x = 842,5 aralığı kalır. Yatay genişliğin yaklaşık yüzde 31,6'sı korunur. Bu geometrik hesaptır; her uygulamanın tüm yüzeylerde mutlaka böyle kırptığı anlamına gelmez.

**Bu yüzden sonradan ortayı almak çoğu zaman yetmez.** Ana nesne, işlem ve finalin anlamlı parçası baştan dikey alana göre yerleştirilmelidir. Yanlarda kalan kritik vinç, ikinci nesne veya sonuç kırpıldığında hikâye eksik kalabilir.

### Üç teslim yaklaşımı

**Baştan dikey çekim veya üretim:** Reels, TikTok ve Shorts için ayrı 9:16 kompozisyon kur. Ana dönüşüm dikey çerçevede yeterince büyük kalsın. Örneğin 1080 × 1920 bir teslim hedefi olabilir; çekim ana dosyanı daha yüksek çözünürlükte tutabilirsin.

**Yüksek çözünürlüklü yatay kaynaktan kırpma:** 3840 × 2160 görüntünün 9:16 merkez alanı 1215 × 2160 olur. Bu alan, 1080 × 1920 çıktıya küçültülebilir. Buna karşılık 1280 × 720 kaynaktaki 405 × 720 alanı 1080 × 1920'ye büyütmek ayrıntı üretmez.

**Yatay görüntüyü dikey tuvale bütünüyle yerleştirme:** Üst ve altta boşluk veya tasarlanmış arka plan kalır. Görüntünün tamamı korunur fakat konu daha küçük görünür. Bu, merkez kırpmadan farklı bir tasarım tercihidir.

### Kadraj kontrolü

1. İlk, orta ve son kareyi aynı 9:16 çerçevede kontrol et.
2. Kamera hareketi sırasında ana değişimin çerçevenin dışına çıkmadığını doğrula.
3. Başlangıç için kritik ayrıntılara kenarlardan yaklaşık yüzde 10 boşluk bırak; bunu resmi güvenli alan ölçüsü sayma.
4. Açıklama, düğme ve profil görünümlerini gerçek uygulama önizlemesinde ayrıca kontrol et.
5. Kapak ile video kadrajını ayrı değerlendir. Videoya uygun bir kare, profil ızgarasında farklı kırpılabilir.

<!-- PAGEBREAK -->

## 12 İzleyicinin takip edebileceği zaman akışı

Viral olmayı yalnızca hızlı kurgu ile eşitleme. İzleyici başlangıcı anlayamıyorsa hız değişimi bilgi vermez. Bu bölümdeki süreler, 8-10 saniyelik AI klipleri ve kısa dönüşüm videoları için önerilen kurgu denemeleridir.

### Bir klibin üç işi

**Başlangıç:** Nesnenin ne olduğu ve neyin değişeceği anlaşılmalı. Bozuk zemin, boş saksı veya kirli yüzey ilk görüntüde seçilsin. Uzun logo veya açıklama kartı zorunlu değildir.

**İlerleme:** Her bölümde kalıcı bir fark oluşsun. Temizlenen alan genişlesin, taşıyıcı yükselsin, su seviyesi artsın. Etrafta çok sayıda işçinin dolaşması ilerleme yerine geçmez.

**Sonuç:** İzleyici beklenen farkı karşılaştırabilsin. Son görüntüyü anında kesmek yerine anlaşılacak kadar tutmayı dene. Örneğin 8 saniyelik klipte 0-1 saniye başlangıç, 1-6 saniye dönüşüm, 6-8 saniye sonuç bir başlangıç taslağıdır.

### İlk görüntü için dört uygulanabilir yaklaşım

| Yaklaşım | Görsel soru | Örnek |
| --- | --- | --- |
| Açık sorun | Burası nasıl düzelecek | Çatlamış yol veya otlarla kapanmış geçit |
| Beklenen sonuç | Bu küçük başlangıç neye dönüşecek | Tek tohum ve boş büyüme alanı |
| Görünür sınır | Sınır nereye kadar ilerleyecek | Temiz yüzey ile kirli yüzeyin keskin ayrımı |
| Ölçek merakı | Bu ayrıntı neyin parçası | Küçük bir metal parça, sonra bütünü açan kadraj |

**Sonucu önden göstermek:** Güçlü bir sonuç karesi merak oluşturabilir fakat bütün sürprizi de tüketebilir. Aynı videonun sonucu önden gösteren ve sorundan başlayan iki açılışını test et. Her konu için tek doğru açılış yoktur.

**Döngü:** İlk ve son görüntü arasında biçimsel bağlantı kurulabilir. Ancak bitmiş bir binayı bir anda boş arsaya çevirmek doğal süreklilik değildir. Böyle bir dönüşü bilinçli kurgu olarak kullan veya başlangıca dönüşün nedenini görünür yap.

**Ses:** Timelapse çekim, sürecin senkron sesini doğal olarak taşımaz. Kurgu seslerini işlem sınırlarıyla eşleştir; çok hızlandırılmış gerçek ses zorunlu değildir. AI üretiminde ses talimatını kamera talimatından ayrı cümleyle yaz.

<!-- PAGEBREAK -->

## 13 Konuya göre çekim reçeteleri

Bu reçeteler, kaynak videoların birebir kamera ölçüleri değildir. Kendi sahneni tasarlaman için önerilen kombinasyonlardır.

### Yol onarımı ve küçük şantiye

**Ana plan:** Yüksekten üç çeyrek bakış, 24-35 mm eşdeğeri, sabit kamera. Hem çalışma yüzeyini hem malzemenin giriş çıkışını göster. İlk durumun izleri kayboldukça geometrik sınırlar sabit kalsın. **Ek plan:** Sıkıştırma veya kaplama ayrıntısı. **Final:** Ana kadraja dönüş ve tamamlanan işlev. İş makinelerinin çok küçük kalması veya malzemenin yoktan belirmesi başlıca sorundur.

### Oda dönüşümü

**Ana plan:** Köşeden, 20-28 mm eşdeğeri, 1,5-2 m yükseklik. Kamera son durumda mobilyanın kapatacağı yerde olmasın. Pencere, kapı ve tavan çizgileri sabit referans sağlar. **Hareket:** Ana dönüşümde sabit; tamamlanan mekânı göstermek için ayrı kısa geri çekilme. AI'da pencere sayısı ve duvar ölçülerini özellikle koru.

### Temizlik

**Ana plan:** Yüzeyin alanını gösteren tepeden veya yüksek çapraz bakış. Temizlenen sınır ekranda izlenebilir olsun. **Lens:** Alan büyüklüğüne göre 28-50 mm eşdeğeri. **Hareket:** Önce sabit; hareketli versiyonda temizlik sınırıyla aynı yönde sınırlı takip. Temizlenen bölgenin yeniden kirlenmesi veya aletin dokunmadığı yerin birden temizlenmesi süreç mantığını bozar.

### Nesne restorasyonu

**Ana plan:** 45 derece civarı çapraz bakış, 40-70 mm eşdeğeri. **Detay:** Yüzey veya mekanizma için 70-105 mm görünümü ya da makro. **Final:** Nesnenin çalıştığını göster. Sadece parlak bir son görünüm, işlevsel dönüşümün yerine geçmez. Tek çekim hedefinde kritik işlem ve sonuç aynı masada görülebilsin.

### Bitki ve kök büyümesi

**Ana plan:** Konu hizasında veya hafif yüksek, 40-85 mm eşdeğeri. Kök önemliyse cam kesitli yan görünüm; yaprak örtüsü önemliyse yüksek açı kullan. **Hareket:** Sabit. **Işık:** Sürece uygun kontrollü düzen. Bitkiyi aydınlatma kararı ile kameranın görüntü pozlamasını ayrı düşün; büyüme koşullarını yalnızca görüntü uğruna rastgele değiştirme.

<!-- PAGEBREAK -->

### Bulut ve fırtına gelişimi

**Ana plan:** Geniş gökyüzü gerekiyorsa 16-24 mm eşdeğeri ve altta sabit arazi referansı. Uzak katman ayrıntısı gerekiyorsa daha dar görüş alanı. **Hareket:** Önce sabit çekim; bulutun sahneden çıkmasını önlemek için kontrollü pan seçilebilir. Her şeyi hızlandırmak, gelişimin biçimini yok ediyorsa intervali kısalt. Yakın ağaçların titreşimi veya dal hareketi gökyüzünden daha baskın hale gelmesin.

### Şehir ve yolculuk hyperlapse

**Ana plan:** 24-35 mm eşdeğeri, belirli bir mimari veya coğrafi hedefe bağlı güzergâh. Kamera aralıklarla ilerlesin; seçilen hedef kadrajda kontrollü yer tutsun. **Hareket:** Tek doğrultuda yaklaşma, yana geçiş veya kısa yay. Yürüyüş yolu ile kameranın baktığı yönü ayrı tarif et. Güzergâhı sürekli değiştirmek stabilizasyonu ve mekân algısını zorlaştırır.

### Su dolumu ve alanın ortaya çıkması

**Ana plan:** Su yüzeyi alanı için tepeden, seviye için yandan, ikisi birlikte gerekiyorsa çaprazdan bak. **Lens:** Yaklaşık 24-50 mm eşdeğeri. **Hareket:** Sabit. **Referans:** Sabit bir duvar çizgisi veya basamak. Su, ışık yansıması değiştiği için yükselmiş gibi görünmesin; gerçek seviye karşılaştırılabilsin.

### Büyük nesnenin ölçeğini açıklama

**Ana plan:** Ayrıntıya yakın başla, tek bir dolly out veya yükselme ile bütünü göster. **Lens:** 24-35 mm eşdeğeri ve değişmeyen odak uzaklığı, görüş alanını tutarlı tarif etmek için iyi bir başlangıçtır. **Referans:** Büyüklüğü tanınan kapı, korkuluk veya araç. Kamera hareketiyle birlikte nesnenin de büyümesi istenmiyorsa AI promptunda boyutun sabit kaldığını yaz.

### Her konu için bir karar cümlesi

“İzleyici [değişen özellik] farkını görecek. [Sabit referans] aynı kalacak. Kamera [konum ve açı] üzerinden bakacak. [Hareket] yalnızca [yeni bilgi] açmak için kullanılacak.” Bu cümle dolmadan ekipman veya görsel stil seçimini kesinleştirme.

<!-- PAGEBREAK -->

## 14 Yapay zekâ ile timelapse üretim sistemi

AI'da “cinematic, epic, viral, 8K” yazmak; kamera konumunu, fiziği veya sürekliliği tanımlamaz. Promptu görünür kararlar üzerinden kur. Marka ve gövde adı yerine, sahnede gerçekten fark edilmesini istediğin görüş alanı, netlik, ışık ve hareket daha kullanışlı başlangıçlardır.

### Her klip için kayıt kartı

| Alan | Yazılması gereken |
| --- | --- |
| Başlangıç durumu | İlk karedeki nesne, miktar ve tamamlanma evresi |
| Bitiş durumu | Klip sonunda görülecek tek kalıcı ilerleme |
| Değişmeyecekler | Nesne kimliği, çevre geometrisi, sabit referanslar |
| Kamera | Yükseklik, uzaklık, bakış yönü, çekim ölçeği |
| Lens görünümü | Eşdeğer görüş alanı, netlik alanı, odak davranışı |
| Hareket | Tek ana hareket veya açıkça sabit kamera |
| Zaman | Çıktı süresi ile temsil edilen süreç süresi ayrı |
| Fizik | Malzeme nereden gelir, nasıl hareket eder, nereye gider |
| Işık | Sabit kaynak veya planlanan gün ışığı değişimi |
| Geçiş | Sonraki klibe aktarılacak durum ve referans görüntü |

### Görsel referans zinciri

Önce tamamlanmış sahnenin geometrisini belirle. Ardından başlangıç ve ara evreleri aynı çevre üzerinde tasarla. Araç destekliyorsa önceki klibin son karesini sonraki klibin başlangıç referansı olarak kullan. İlk ve son kare desteği varsa ikisini de süreçle uyumlu seç. Özelliğin kullanılabilirliğini kullandığın araç ve model için kontrol et.

**G0, G1, G2 zinciri:** Bir klip G0'dan G1'e, sonraki G1'den G2'ye ilerler. Bu yöntem çelişki riskini azaltabilir; kusursuz eşleşmeyi garanti etmez. Netlik, perspektif, ışık ve nesne sayısı yine gözle kontrol edilmelidir.

**İki kamera ailesi:** Sabit bir ana kamera A ve ayrıntı kamerası B kullanıyorsan her birinin ayrı referanslarını tut. A görüntüsünü B'nin son karesine dönüştürerek görünmez geçiş varsayma. A'dan B'ye geçmek kurgu kesmesidir; her klibin tek çekim olması filmin tamamının tek çekim olması demek değildir.

**Süre:** 8 ve 10 saniye aşağıdaki planlarda zaman çizelgesi hedefleridir. Kullandığın araç hedef süreyi üretmiyorsa uygun klip üretimi ve kurgu gerekir. Desteklenmeyen bir süreyi yalnızca prompta yazmak onu garanti etmez.

<!-- PAGEBREAK -->

### 14A Süreklilik ve fizik kuralları

**Kimlik:** Aynı nesne aynı malzeme, renk, temel biçim ve işaretleri korusun. Kamera değiştiğinde nesne değişmesin. Bitkinin türü, binanın kat düzeni ve aracın aks sayısı rastgele dönüşmemelidir.

**Geometri:** Sabit duvar, pencere, yol kenarı ve arka plan kayaları süreç boyunca yerinde kalsın. Kamera hareketi varsa görünen farklılık bakış noktasından kaynaklanmalı; mekân kendi kendine esnememelidir.

**Nedensellik:** Boya yüzeye uygulandıkça kaplasın. Moloz kaldırılıyorsa araçla veya elle taşınsın. Su belirli bir girişten dolsun. Çatı elemanı bir taşıma ve yerleştirme aşaması olmadan belirmesin.

**Zaman:** Kamera 8 saniyede yavaş ilerlerken inşaat zamanı hızlandırılabilir. “Her şey çok hızlı” yerine hangi sürecin sıkıştırıldığını yaz. Önemli bir bağlama veya açılma anını kısmen gerçek hızda göstermek, işlemin anlaşılmasına yardım edebilir.

**Işık:** Hızlandırılmış gün döngüsü istemiyorsan güneşi veya gölgeleri gelişigüzel döndürme. Gün-gece geçişi isteniyorsa bunu ayrı ve açık bir dönüşüm olarak tarif et. Kaynaksız parlamalar ilerlemenin yerini almasın.

### Çelişen komutları temizle

| Sorunlu tarif | Düzeltilmiş tarif |
| --- | --- |
| Static camera, slow dolly in | Bu klip için sabit çekim veya dolly in seçeneklerinden birini seç |
| Fixed 35mm lens, dramatic optical zoom | Sabit lensle fiziksel yaklaşma veya ayrı zoom talimatı kullan |
| Top-down view, visible deep vertical front wall | Tepeden görünüm yerine yüksek çapraz bakış seç |
| Same framing, full orbit around the object | Aynı ekran ölçeği korunarak değişen bakış yönünü açıkla |
| Whole process in one instant | Görünür ve sıralı ara evreler tanımla |
| Empty site, dozens of workers everywhere | Kadrodaki insan ve araç sayısını tutarlı belirle |

**Negatif prompt:** Aracın ayrı negatif alanı varsa istenmeyen unsurları kısa listele: “camera drift, flicker, warped geometry, object duplication, teleporting materials, jump cuts, text overlays, logos”. Ana promptta olumlu ve somut davranışı tanımla. Google rehberi negatif alanda “no” ve “don't” ile başlayan talimatlar yerine istenmeyen öğelerin adlarını kullanmayı önerir. [Resmi negatif prompt rehberi](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)

<!-- PAGEBREAK -->

## 15 Örnek çekim planları

### 15A Yedi klip ile 56 saniyelik dönüşüm

**Özgün uygulama örneği:** Otlarla kapanmış taş avlunun temizlenmesi, derzlerinin onarılması ve yeniden kullanılır hale gelmesi. Bu bir gerçek viral videonun çözümlemesi değil, kılavuzun ilkelerini birleştiren üretim taslağıdır.

**Format:** 9:16, 7 × 8 saniye. **Kamera A:** Sabit yüksek çapraz bakış, 3 m yükseklik, yaklaşık 7 m uzaklık, 28 mm eşdeğeri. Kapı, duvar ve avlu sınırları aynı kalır. Her klip kendi içinde kesmesizdir; klip birleşimlerinin ayrıca eşleştirilmesi gerekir.

| Klip | Zaman | Başlangıç ve kalıcı ilerleme | Kamera |
| --- | --- | --- | --- |
| 1 | 00-08 | Otlu avluda ilk taş sınırı açılır; sorun hemen anlaşılır | A sabit |
| 2 | 08-16 | Otların büyük kısmı kaldırılır; malzeme belirli çıkıştan taşınır | A sabit |
| 3 | 16-24 | Yıkama sınırı ilerler; taş dokusu ortaya çıkar | A sabit |
| 4 | 24-32 | Hasarlı taşlar sırayla çıkarılıp yenileri yerleştirilir | A sabit |
| 5 | 32-40 | Derzler belirgin bir yönde tamamlanır | A sabit |
| 6 | 40-48 | Atıklar ve aletler toplanır; alan bitmiş hale ulaşır | A sabit |
| 7 | 48-56 | Avlu kullanımını gösterir; son 2 saniye sonuç okunur | A sabit |

**Neden bütün plan sabit?** Başlangıç ile sonuç aynı geometri üzerinden karşılaştırılabilir. Değişen malzeme, iş ve yüzeydir; kamera bu karşılaştırmanın ölçütü olur.

**Hareketli alternatif:** Yalnızca yedinci klipte kamera 1 m kadar geri çekilip durur. Bu durumda hareket G6'daki başlangıç kadrajından başlamalı ve avlunun daha önce görünmeyen anlamlı bir bölümünü açmalıdır. Yeni bilgi açmıyorsa sabit finali koru.

**Süreklilik kontrolü:** G1-G6 karelerinde temizlenmiş alan yeniden kirlenmesin; kaldırılan taşlar yanlış yerde geri gelmesin; ışığın yönü tutarlı kalsın. Her klipte tek büyük ilerleme hedefle. Yedi klibin tamamında aynı anda yıkama, döşeme, taşıma ve dekorasyon yaptırma.

<!-- PAGEBREAK -->

### 15B Altı klip ile 60 saniyelik hareketli anlatım

**Özgün uygulama örneği:** Paslı bir mekanik saatin restorasyonu. **Format:** 6 × 10 saniye, 9:16. Bu plan kontrollü kesmeler içerir; filmin bütünü tek çekim değildir.

| Klip | Süre | Görünür iş | Kamera seçimi |
| --- | --- | --- | --- |
| 1 | 00-10 | Saatin işlemeyen hali ve ilk açma işlemi | Genel çapraz, 50 mm görünümü, sabit |
| 2 | 10-20 | Parçalar aynı tezgâh üzerinde düzenli sökülür | Tepeden, 50 mm görünümü, sabit |
| 3 | 20-30 | Bir metal parçanın yüzeyi temizlenir | Yakın plan, 85 mm görünümü, sabit |
| 4 | 30-40 | Mekanizma sıralı şekilde birleştirilir | İlk çapraz açıya dönüş, sabit |
| 5 | 40-50 | Mekanizma çalışır; sonuç işlevle doğrulanır | Yakın plan, kısa ve yavaş yaklaşma |
| 6 | 50-60 | Tamamlanan saat ve tezgâhın bütünü açılır | 1 m geri çekilme; sonda duruş |

**Neden açı değişiyor?** Her değişim başka bir soruya cevap veriyor: nesne ne, parçalar nasıl düzenleniyor, yüzey nasıl değişiyor, mekanizma çalışıyor mu? Farklılık yalnızca görüntü çeşidi üretmek için kullanılmıyor.

### 15C Tek bir on saniyelik klibin hareket planı

**Konu:** Tamamlanmış bir ahşap köprünün ayrıntısından bütününe açılma. İlk 2 saniye bağlantı ayrıntısı; 2-8 saniye aynı yükseklikte yavaş geri çekilme; 8-10 saniye köprünün tamamını tutma. Odak uzaklığı değişmez. Kamera hareketi sırasında köprü inşa edilmez; önceki klipteki sonuç korunur.

**Alternatif tek çekim:** Köprünün tamamı baştan görülsün ve 10 saniye boyunca yalnızca son korkuluğun yerleştirilmesi izlensin. Aynı klipte hem tüm köprüyü inşa etmek hem ayrıntıya yaklaşmak hem yukarı uçmak yerine tek bir görsel iş seç.

### İki plan arasında nasıl seçim yapılır

Süreç, genel kadrajda anlaşılabiliyorsa 56 saniyelik sabit sistem daha kolay denetlenir. Kritik işlem küçük ayrıntılara bağlıysa 60 saniyelik çok açılı sistem daha açıklayıcı olabilir. AI üretiminde bakış yönü değiştirmek süreklilik maliyetini artırır; bu yüzden açı değişiminin sağladığı bilgiyi açıkça tanımla.

<!-- PAGEBREAK -->

## 16 Kullanıma hazır İngilizce promptlar

Bu sekiz prompt özgün üretim taslaklarıdır. Belirli bir modelin süre, çözünürlük veya hareket garantisi değildir. Aracın desteklediği süreyi ve en-boy oranını ayrıca seç. “28 mm equivalent” gibi ifadeler AI için görsel hedef, gerçek çekimde ise ekipman planıdır. Aynı sahnenin devamında önceki klibin son karesini, araç destekliyorsa başlangıç referansı olarak kullan.

### 16A Yüksek çapraz açı: avlu temizliği

**Kullanım:** Tek bir yüzeyde görünür ilerleme. **Önerilen süre:** 8 saniye.

```text
Vertical 9:16 photorealistic time-lapse of an overgrown stone courtyard being cleared. One continuous shot. A locked camera is mounted 3 meters above the ground, looking diagonally down across the entire courtyard, with a 28mm full-frame-equivalent field of view. Keep the doorway, boundary walls and stone pattern identical throughout. Two adult workers remove weeds in a clear progression from the near-left corner toward the far-right corner, carrying the collected material through the same doorway. Cleared areas remain clear. Use stable overcast daylight. The last two seconds hold on the visibly improved courtyard. The camera position, orientation and focal length remain constant.
```

**Değiştirilecek öğeler:** Avlunun referans görüntüsü, işin yönü, işçi sayısı ve bitiş evresi. Bu klipte taş döşeme, boyama ve mobilya yerleştirme gibi başka işler ekleme.

### 16B Tepeden açı: temizleme sınırı

**Kullanım:** Kirli ve temiz yüzeyin aynı anda karşılaştırılması. **Önerilen süre:** 8 saniye.

```text
Vertical 9:16 overhead time-lapse of a rectangular stone slab being cleaned on a workbench. One continuous shot from a locked camera looking straight down, with a natural 50mm-equivalent field of view. Keep all four slab corners visible and stationary. A single adult operator's gloved hands move a cleaning brush in overlapping passes from left to right. Dirt is removed only where the brush has passed, leaving a clear advancing boundary between the dark surface and the pale clean stone. Maintain the same stone grain, workbench, soft lighting and hand identity. The final two seconds show the completed clean surface with the brush resting beside it.
```

**Kontrol:** Fırçanın geçmediği yerler kendiliğinden temizlenmemeli. “Daha dramatik olsun” diye aynı anda kamerayı döndürmek bu karşılaştırmayı zayıflatabilir.

<!-- PAGEBREAK -->

### 16C Yandan bakış: bitki büyümesi

**Kullanım:** Yüksekliğin ve yaprak açılımının okunması. **Önerilen süre:** 10 saniye.

```text
Vertical 9:16 studio time-lapse of one bean seedling growing in a small terracotta pot. Use a locked side-view camera at pot-rim height, with a natural 70mm-equivalent field of view. Frame the pot in the lower third and reserve generous space above for growth. Show a plausible sequence: the shoot rises, the cotyledons open, then the first true leaves expand. Preserve the same pot, soil level, stem origin and plant species throughout. Use a plain charcoal background and consistent soft side lighting. Growth is gradual and connected, with each new leaf emerging from the plant. End with a two-second stable view of the young seedling.
```

**Kontrol:** Bu bir görsel büyüme tarifi; modelin botanik doğruluğunu ayrıca değerlendir. Kök gelişimi gösterilecekse başka bir şeffaf kap ve kesit planı gerekir.

### 16D Sabit geniş açı: yaklaşan bulut sistemi

**Kullanım:** Gökyüzünde yön ve ölçek. **Önerilen süre:** 10 saniye.

```text
Vertical 9:16 landscape time-lapse from a firmly locked tripod on a hillside, using a 24mm-equivalent field of view. A small solitary tree and the distant ridge remain fixed in the lower third. A layered bank of dark clouds travels steadily from frame left to frame right, gradually shading the valley. Keep the terrain, tree shape and horizon geometry consistent. The landscape becomes dimmer smoothly as cloud cover increases, without abrupt exposure jumps. One continuous shot with constant camera position and focal length. Let the cloud movement provide the motion; end with the valley under an evenly overcast sky.
```

**Kontrol:** Bulut akışı ile kamera pan hareketini karıştırma. Ufuk ve ağacın ekran konumu oynamıyorsa değişim daha kolay okunur.

<!-- PAGEBREAK -->

### 16E Yana kayış: mekânın derinliğini açmak

**Kullanım:** Ön plan ve arka plan arasındaki konum farkı. **Önerilen süre:** 8 saniye.

```text
Vertical 9:16 time-lapse of evening activity inside a glass greenhouse. One continuous shot with a 35mm-equivalent lens. The camera travels smoothly 40 centimeters to the right on a straight level slider over the full eight seconds, keeping its orientation and focal length constant. Foreground leaves pass gently across the frame while the greenhouse doorway remains visible in the background. Two adult gardeners move along the aisle and water the existing plants; plant sizes and structures remain unchanged. Preserve all greenhouse beams and aisle geometry. Evening light changes gradually. The camera follows only this lateral path at a steady speed.
```

**Kontrol:** “Yana kayma” talimatını pan ile eşitleme. Kamera sağa giderken sağa dönmek ayrı bir harekettir. Gerçek çekimde 40 cm güzergâh, çıktıdaki 8 saniyeye sıkıştırılan toplam kayıt süresine yayılır.

### 16F Kısa orbit: bitmiş yapının hacmi

**Kullanım:** Dönüşümden sonra yapının çevreyle ilişkisi. **Önerilen süre:** 10 saniye. Bu bir sonuç planıdır; tek başına timelapse olması gerekmez.

```text
Vertical 9:16 photorealistic reveal of a completed circular stone reservoir in a rural landscape. One continuous aerial shot with a 28mm-equivalent field of view. The camera follows a slow 20-degree clockwise arc around the reservoir, at a constant altitude of 15 meters and a constant horizontal radius of 25 meters. Keep the reservoir centered and fully inside the frame while its surroundings shift with natural parallax. Preserve the reservoir's circular geometry, stone texture and water level. Use steady soft morning light. The orbit is the only camera movement; gently stop during the final two seconds for a clear view of the finished structure.
```

**Kontrol:** Bu rakamlar kılavuzun örnek güzergâhıdır. Dronun gerçek kullanımında konum, erişim ve çevre koşullarına göre planlanmalıdır. AI üretiminde önce kısa bir yay denemek, tam turdaki görünmeyen yüzlerin tutarlılığını çözme yükünü azaltır.

<!-- PAGEBREAK -->

### 16G Geri çekilme: ayrıntıdan bütüne sonuç

**Kullanım:** Önceki klibin tamamlanmış halini daha geniş bağlamda göstermek. **Önerilen süre:** 10 saniye.

```text
Vertical 9:16 cinematic final reveal of a completed wooden garden bridge. Start from the supplied reference frame showing a close view of the near handrail joint. Hold for two seconds, then move the camera smoothly backward by 1.5 meters over six seconds at a constant height, using the same 35mm-equivalent lens throughout. Reveal the full bridge and its connection to the garden path. Preserve every plank, railing post, joint and background feature from the reference. The structure remains complete and unchanged during the move. Stop and hold the wide composition for the last two seconds. One continuous shot with a single straight camera path.
```

**Kontrol:** Bu hareket perspektifi değiştirir. Yalnızca dijital olarak görüntüyü küçültmek aynı sonuç değildir. Başlangıç karesinde köprü kimliğini belirleyen ayrıntılar bulunmalı.

### 16H Platforma bağlı kamera: deniz yolculuğu

**Kullanım:** Hareket eden taşıtın sabit referans oluşturması. **Önerilen süre:** 10 saniye.

```text
Vertical 9:16 maritime time-lapse from a camera rigidly mounted to the upper deck of a cargo vessel, with a 24mm-equivalent rectilinear field of view. Keep a small recognizable section of the ship's bow fixed in the bottom of the composition. The vessel advances through a wide channel as the coastline and distant harbor move relative to it. Clouds travel consistently across the sky and water flows naturally alongside the ship. Preserve the vessel's structure and the coastline's continuity. The camera remains fixed to the vessel with constant orientation and focal length; all viewpoint travel comes from the ship's forward motion. One continuous shot with gradual daylight change.
```

**Kontrol:** “Tripod locked to the ground” ekleme; zemin burada geminin güvertesidir. Kamera için aynı anda “dünyaya sabit” ve “gemiyle ilerleyen” iki farklı referans verme.

### Promptu kendine uyarlamanın kısa sırası

Önce değişecek şeyi ve kalıcı olacak nesneleri yaz. Sonra kamera konumu, bakış yönü ve görüş alanını ekle. Ardından tek hareketi, hareket mesafesini ve zamanlamasını tanımla. Son cümlede sonucun nasıl görüleceğini belirt. Araçta ayrı negatif alan varsa 14. bölümdeki kısa listeyi yalnızca ihtiyaç duyulan maddelerle kullan.

<!-- PAGEBREAK -->

## 17 Sık görülen hatalar ve doğrudan düzeltmeleri

| Belirti | Olası neden | İlk düzeltme |
| --- | --- | --- |
| Çok hareket var, ilerleme anlaşılmıyor | İnsan ve araç hareketi esas dönüşümü örtüyor | Her klip için tek kalıcı değişim belirle; başlangıç ve bitiş karesini karşılaştır |
| Bina eğiliyor, duvarlar değişiyor | Fazla geniş görünüm veya AI geometri hatası | Daha uzak kamera ve daha dar görüş alanı dene; aynı yapı referansını kullan |
| Temizlenen bölüm yeniden kirleniyor | Klip durumları aktarılmıyor | Önceki bitiş karesini sonraki başlangıca bağla; tamamlanan alanları tanımla |
| Aletler ve malzeme birden kayboluyor | Taşıma ve çıkış eylemi belirtilmemiş | Giriş, işleme ve çıkarma yönlerini açıkça yaz |
| Gerçek çekimde parlaklık titreşiyor | Otomatik ayarlar veya ışık kaynağı dalgalanması | Önce örnek dizi incele; pozlama ve beyaz ayarını kararlı hale getir |
| Görüntü sıçrıyor | Destek kayması veya hyperlapse hizalama hatası | Sabit referans üzerinden hizala; ağır hatalı kareleri ve kurulum sorununu ayır |
| Bitki tepeden kesiliyor | Son büyüklük hesaba katılmamış | Bitmiş boyutu baştan kadrajla; büyüme boşluğu bırak |
| Makro ayrıntı netlikten çıkıyor | Süreç dar netlik bölgesinden uzaklaşıyor | Çekim mesafesini ve alan derinliğini yeniden kur; deneme evresini kaydet |
| Dikey videoda işlem görünmüyor | Yatay kadrajın merkezi gerekli eylemi içermiyor | Çekimden önce 9:16 alanı işaretle; eylemi bu alana taşı |
| Geri çekilmede perspektif değişmiyor | Model dijital zoom üretmiş | Kameranın başlangıç ve bitiş konumlarını belirt; ön plan referansı ekle |
| Orbit sırasında nesnenin arkası değişiyor | Görülmeyen yüz için yeterli referans yok | Yayı küçült; ek görünüm referansı kullan veya sabit çapraz plana dön |
| Kamera durmadan yön değiştiriyor | Bir promptta çok sayıda hareket talimatı var | Bir konum yolu seç; pan, zoom ve yükselmeyi ayrı kliplere ayır |
| Klipler birleşince nesne zıplıyor | Ekran ölçeği, yön veya bitiş durumu eşleşmiyor | Birleşme noktalarının iki karesini yan yana kontrol et |
| Final acele bitiyor | Sonucun görülmesine zaman ayrılmamış | Önemsiz tekrarları kısalt; tamamlanmış görünümü tut |
| Aynı videonun ikinci sürümü daha az izleniyor | Konu, izleyici veya dağıtım da değişmiş olabilir | Tek yayından açı sonucu çıkarma; benzer birkaç süreçte yeniden dene |

**Düzeltme sırası:** Önce fiziksel ve görsel sürekliliği, sonra kadrajı, sonra ritmi, en son süsleyici hareket ve efektleri ele al. Anlaşılmayan dönüşümü yalnızca müzik veya daha hızlı kurgu ile çözmeye çalışma.

<!-- PAGEBREAK -->

## 18 Çekimden yayına uygulama kontrolü

### Çekim veya üretim öncesi

- Dönüşümü tek cümlede anlatabiliyorum: başlangıç durumu, yapılan iş, bitiş durumu.
- Seçtiğim açı değişimin önemli boyutunu gösteriyor: alan, yükseklik, derinlik veya yolculuk.
- Son durum kadraja sığıyor; dikey sürümde ana eylem görünür kalıyor.
- Kamera türünü, lens görünümünü, yüksekliğini ve bakış yönünü ayrı tanımladım.
- Sabit çekimde karşılaştırma referansı, hareketli çekimde yol ve hedef belirli.
- Gerçek çekimde güç, depolama ve interval süresi deneme çekimiyle kontrol edildi.
- AI üretiminde başlangıç referansı ve tamamlanmış durum hazır; çelişen kamera komutları temizlendi.

### Çekim veya üretim sırasında

- Küçük deneme dizisinde netlik, titreme, pozlama değişimi ve kadraj sınırlarını izledim.
- Her evrede kalıcı ilerleme görülüyor; yalnızca kalabalık ve hızlı hareket üretilmiyor.
- Aynı nesnenin biçimi, sayısı, yönü ve malzemesi süreç boyunca tutarlı.
- Hareketli çekimde ilerleme hızı, görüş yönü ve konuya uzaklık planla uyuşuyor.

### Kurgu ve dışa aktarma öncesi

- İlk kare mobil ekranda konuyu anlaşılır kılıyor.
- Tekrarlanan veya ilerleme göstermeyen bölümler çıkarıldı.
- Klip birleşimlerinde aynı yapı ve nesneler aynı durumu sürdürüyor.
- Finalde neyin tamamlandığı ve gerekiyorsa nasıl çalıştığı açık.
- Ses, görüntüdeki vurguya uyuyor; sessiz izleyince de süreç anlaşılabiliyor.
- Son dosya hedef uygulamanın önizlemesinde açıldı; düğme, açıklama ve kırpma alanları kontrol edildi.

### Pratik çalışma akışı

**1. Hikâye kartı:** “Kirli avlu temizlenir” kadar belirgin bir değişim yaz. **2. Kamera testi:** Aynı başlangıç durumunu iki açıyla dene. **3. Kısa örnek:** Gerçek çekimde küçük bir dizi, AI üretiminde bir klip üret. **4. Süreklilik:** Başlangıç, orta ve son kareyi karşılaştır. **5. Tam üretim:** İşleyen kamera tarifini koru. **6. Kurgu:** Durakları kısalt, dönüşüm evrelerini koru. **7. Yayın:** Önizlemeyi kontrol et ve sonucu kaydet.

Bu liste bir “viral puanı” üretmez. Ama izlenmeyi değerlendirmeden önce görüntünün ne anlattığını ve nasıl üretildiğini denetlenebilir hale getirir.

<!-- PAGEBREAK -->

## 19 Kendi kanalında açı ve hareketi test et

Bir kaynaktaki milyonlarca izlenme, o açıya ait bağımsız bir performans ölçümü değildir. Kendi konunda hangi kadrajın daha iyi çalıştığını öğrenmek için tek seferde bir ana değişkeni test et.

### Altı sürümlük küçük deneme matrisi

| Sürüm | Ana bakış | Kamera davranışı | Denenen soru |
| --- | --- | --- | --- |
| A1 | Yüksek çapraz | Baştan sona sabit | İşin bütünü anlaşılır mı? |
| A2 | Yüksek çapraz | Yalnızca finalde geri çekilme | Geniş bağlam sonucu güçlendiriyor mu? |
| B1 | Tam tepeden | Baştan sona sabit | Değişim sınırı daha kolay okunuyor mu? |
| B2 | Tam tepeden | Yalnızca finalde dikey yükselme | Çevreyi açmak anlamlı bilgi katıyor mu? |
| C1 | Alçak çapraz | Baştan sona sabit | Yükseklik ve doku daha etkili mi? |
| C2 | Alçak çapraz | Yalnızca finalde geri çekilme | Sonucun hacmi daha açık mı? |

Bu matris, bütün altı sürümü peş peşe yayımlama talimatı değildir. Önce düşük maliyetli önizlemeleri karşılaştır; konuyu yanlış gösteren açıları ele. Sonra benzer süreçlerde iki güçlü seçeneği birkaç kez dene. Platform rastgele izleyici atamıyorsa sonuç, kontrollü laboratuvar deneyi sayılmaz.

**Karşılaştırmada mümkün olduğunca koru:** Konu, toplam süre, ilk karedeki sorun, dönüşümün büyüklüğü, final süresi, ses ve başlık. Açıyla birlikte bunları da değiştirirsen hangi unsurun etkili olduğunu ayıramazsın. Hareket eklenince konu ölçeğinin değişmesi gibi kaçınılmaz farkları ayrıca not et.

### Hangi göstergeleri kaydetmeli

| Gösterge | Nasıl okunur | Dikkat |
| --- | --- | --- |
| İlk saniyelerde izlemeye devam etme | Konu ve başlangıç anlaşılır mı? | Platformların ölçüm adı ve eşiği farklı olabilir |
| Ortalama izleme süresi | Videonun ne kadarı izleniyor? | Farklı uzunluklar için süreyle birlikte yüzdesine de bak |
| Tamamlama | İzleyici sonucu görüyor mu? | Aynı uzunluktaki videolarla karşılaştır |
| Tekrar izleme veya döngü davranışı | Süreç yeniden izlenmek isteniyor mu? | Her panel tekrarları ayrı göstermeyebilir |
| Paylaşma ve kaydetme | Video başkasına gösteriliyor veya saklanıyor mu? | Oran hesaplıyorsan paydanın ne olduğunu sabit tut |

YouTube, 31 Mart 2025'ten itibaren Shorts görüntülemelerini videonun başlaması veya yeniden başlaması üzerinden, asgari izleme süresi olmadan saydığını açıklar. İzlemeyi sürdürenleri değerlendirmek için “engaged views” göstergesi korunur. Bu nedenle farklı dönem ve platformların ham sayaçları doğrudan eşit kabul edilmemeli. [YouTube'un resmi açıklaması](https://support.google.com/youtube/answer/10059070?hl=en)

**Kayıt satırı:** Tarih • konu • süre • açı • hareket • ilk kare • final • kullanılan gösterge ve payda • aynı zaman aralığındaki sonuç • bir sonraki değişiklik. Evrensel bir başarı yüzdesi yerine kendi benzer videolarındaki tekrar eden farkı ara.

<!-- PAGEBREAK -->

## Başvuru kartı: hangi durumda hangi kamera dili?

| Göstermek istediğin şey | İlk denenecek açı ve lens görünümü | İlk kamera davranışı |
| --- | --- | --- |
| Bir yüzeyin temizlenmesi veya kaplanması | Tepeden ya da yüksek çapraz, 35-60 mm eşdeğeri | Sabit |
| Bina, oda veya avlunun dönüşmesi | Yüksek çapraz, 24-35 mm eşdeğeri | Sabit ana plan |
| Bitkinin uzaması | Yandan veya hafif çapraz, 50-100 mm eşdeğeri | Sabit; büyümeye yer bırak |
| Küçük parçanın işlenmesi | Yakın çapraz veya tepeden; gereken büyütmeye uygun makro lens | Sabit, kontrollü netlik |
| Bulut ve hava değişimi | Ufku referans alan geniş bakış, 16-35 mm eşdeğeri | Sabit |
| Yolculuk ve çevrenin akışı | Platforma bağlı geniş bakış, 20-35 mm eşdeğeri | Platformla birlikte ilerleme |
| Bir mekânın keşfi | Referans hedefli geniş veya normal bakış, 24-50 mm eşdeğeri | Kontrollü hyperlapse |
| Bitmiş nesnenin ayrıntıdan bütüne açılması | Yakın çaprazdan genel plana, sabit 35-50 mm görünümü | Geri çekilme ve son duruş |

**Bu değerler öneridir.** Mekânın boyutu, kamera mesafesi, sensör ve son kadraj birlikte değerlendirilmelidir. “50 mm” tek başına yakınlık, açı veya doğru perspektif garantisi vermez.

### Çekim tarifini tek paragrafta kur

“9:16 kadrajda [süreç]; [başlangıç durumu] aşama aşama [bitiş durumuna] dönüşür. Kamera [konum ve yükseklik] noktasından [bakış yönü] ile bakar; görüş alanı [eşdeğer odak uzaklığı] gibidir. Kamera [sabit kalır / tek tanımlı yolu izler]. [Kalıcı referanslar] aynı kalır. [Değişim yönü ve ara evreler] açıkça görülür. Son [süre] boyunca [tamamlanmış sonuç] okunur.”

Önce değişimi görünür kıl. Ardından açı, lens ve hareketin her birine belirli bir görev ver. Bir kamera hareketi bu görevi yerine getirmiyorsa tariften çıkarıp iki sürümü karşılaştır.

<!-- PAGEBREAK -->

## Kaynaklar ve doğrulama notları

**Erişim tarihi: 20 Eylül 2026.** Sayısal izlenme bilgileri canlı sayaçların o günkü görünümüdür; zamanla değişir. Kaynaklarda açıklanmayan kamera gövdesi, lens veya kamera mesafesi bu rehberde kesin bilgi olarak sunulmaz. Çekim şemaları kaynak videoların ölçülmüş kamera yerleşimleri değil, rehber için hazırlanmış açıklayıcı çizimlerdir.

### Örnek yayınlar ve yapımcı anlatımları

1. [JeffHK — 30 Days Timelapse at Sea](https://www.youtube.com/watch?v=AHrCI9eSJGQ): İzlenme, yayın tarihi, ekipman, fotoğraf sayısı ve bölüm işaretleri için yayın sayfası.
2. [EarthCam — Official 11 Year Time-Lapse Movie of One World Trade Center](https://www.youtube.com/watch?v=NbA89YbWoL8): İzlenme, yayın tarihi, kayıt dönemi ve üretim açıklaması.
3. [Boxlapse — TOP 10 time-lapses, 859 Days in 8 minutes](https://www.youtube.com/watch?v=3Z2249JGbf4): İzlenme, yayın tarihi ve bitki bölümleri.
4. [TEMPONAUT — Top 10 Timelapses 2021](https://www.youtube.com/watch?v=Sw60Ehm1b5c): İzlenme, yayın tarihi ve deney bölümleri. [Üreticinin teknik sitesi](https://www.zeitraffer.biz/): Fotoğraflardan timelapse üretme yöntemi.
5. [Christoph Rehage — THE LONGEST WAY 1.0](https://www.youtube.com/watch?v=5ky6vgQfU24): İzlenme, yayın tarihi ve fotoğraf dizisinin nasıl oluşturulduğuna ilişkin açıklama.
6. [Matthew Vandeputte — Five edits I did to blow up my showreel](https://www.matjoez.com/2025/02/20/five-edits-i-did-to-blow-up-my-showreel/): Yapımcının 20 Şubat 2025 tarihli performans beyanı ve kurgu açıklaması.

### Teknik başvuru kaynakları

7. [Nikon — Top Tips for Capturing Time Lapse Video with a DSLR](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/top-tips-for-capturing-time-lapse-video-with-a-dslr): Sabit destek, pozlama, netlik ve kayıt yaklaşımı.
8. [Nikon — Time-Lapse Tips and Tricks Using Nikon Mirrorless Cameras](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/time-lapse-tips-and-tricks-using-nikon-mirrorless-cameras): Interval, hareket ve fotoğraf dizisi ile kamera içi üretim ayrımı.
9. [GoPro — How to Make a Time Lapse Video](https://gopro.com/en/us/news/how-to-make-time-lapse-video): Time Lapse, TimeWarp ve kayıt modu ayrımları. Buradaki model örnekleri güncel satın alma tavsiyesi olarak kullanılmamıştır.
10. [Google Cloud — Video generation prompt guide](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide): Kamera açısı, hareket, kompozisyon ve negatif prompt terminolojisi. Bu rehberdeki örnek promptlar özgündür.
11. [YouTube Help — Get started creating YouTube Shorts](https://support.google.com/youtube/answer/10059070?hl=en): Shorts görüntüleme sayımındaki 31 Mart 2025 değişikliği ve engaged views ayrımı.

**Araştırmanın sınırı:** Çalışma, yayın metinleri ve üretici kaynaklarından doğrulanabilen bilgiler üzerine kuruludur. Video akışlarına güvenilir erişim sağlanamadığından bütün sekanslar kare kare incelenmiş değildir. Bu nedenle kamera açılarına ilişkin sayısal yaygınlık, belirli hareketlerin başarı oranı veya bir açının viralliğe neden olduğu yönünde istatistiksel iddia içermez.
