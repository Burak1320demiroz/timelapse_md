# 📥 A34 — HAM SONUÇ (dokunulmadı)

```
KÜNYE
BOT        Gemini Deep Research (tahmin — sahip beyan etmedi; biçim önceki Gemini DR koşularıyla aynı)
TARİH      07.10.2026 (sohbete yapıştırıldığı gün)
PROMPT     arastirma/A34_KANAL_BUYUMESI_2026.md — "BURADAN AŞAĞISI YAPIŞTIRILIR" bloğu
KESİLDİ Mİ bilinmiyor — sohbete tek mesajda beş rapor olarak geldi; tablolar kısmen sekmeyle korunmuş · bazı atıf satırları boş satırla ayrılmış
SÜRE       bilinmiyor
DENETİM    arastirma/SONUCLAR/A30-A34_DENETIM.md
```

> ⛔ Bu dosya HAM kayıttır: tek karakter düzeltilmez [kart S]. Aşağısı yapıştırılan metnin birebir kopyasıdır
> (oturum kaydından çıkarıldı). Biçim bozuklukları (birleşik tablo satırları) kaynağındadır.

---

Yapay Zekâ Destekli İnşaat ve Dönüşüm Timelapse Kanalları İçin Büyüme ve Karar Protokolü: 2024-2026 Veri Analizi
Bu rapor, sıfır abone tabanından başlayan, üretim hattı ağır, yapay zekâ destekli sabit kamera timelapse (zaman atlamalı) inşaat ve dönüşüm filmleri üreten bir kanalın çok platformlu (YouTube, TikTok, Instagram Reels) büyüme stratejisini incelemektedir. Eldeki 37 filmlik stokun algoritmik dağıtım sistemlerinin (özellikle 2026'da güncellenen formata duyarlı keşif ve kullanıcı memnuniyeti odaklı mimarilerin) dinamiklerine uygun olarak nasıl yönetileceği, performansın hangi veri eşiklerine göre değerlendirileceği ve kanalın makro hedeflerine nasıl ulaşılacağı detaylandırılmıştır. Analiz, platformların resmi belgelerine, platform yöneticilerinin kamuya açık açıklamalarına ve büyük ölçekli bağımsız veri madenciliği araştırmalarına dayanmaktadır.

Bölüm 1: Kanıtların Toplanması ve Algoritmik Çerçeve
2024-2026 dönemi platform güncellemeleri, öneri sistemlerinin artık yalnızca tıklama oranlarına (Click-Through Rate - CTR) veya brüt izlenme süresine (Watch Time) dayanmadığını, bunun yerine "kullanıcı memnuniyeti", "format duyarlılığı" ve "özgünlük" sinyallerini temel aldığını göstermektedir. Bu bağlamda, kanalın üretim mimarisi olan "konuşmasız, anlatıcısız, sabit kamera ve yalnızca zaman atlamalı kesmeler" yapısının platformlar tarafından nasıl algılanacağı kritik bir öneme sahiptir.

1.1. Yükleme Sıklığı, Tutarlılık ve Kanal Büyümesi Korelasyonu
Yeni bir kanalın soğuk başlangıç (cold start) aşamasında, yükleme sıklığı makine öğrenimi modellerinin kanalı anlamlandırması için gereken temel veri akışını sağlar. Algoritmalar, hedef kitleyi belirlemek (seed audience) için tutarlı veri noktalarına ihtiyaç duyar. Bağımsız araştırma platformu vidIQ tarafından Nisan 2025 ile Mart 2026 tarihleri arasında 1.000'den fazla abonesi olan 10.210.278 YouTube kanalı üzerinde yapılan analiz, yükleme frekansı ile büyüme hızı arasındaki ilişkiyi açıkça ortaya koymaktadır (ETİKET: [ÖLÇÜLDÜ] 10.210.278 kanal analizi, KAYNAK SINIFI: Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://vidiq.com/research/youtube-upload-frequency-study/ + vidIQ upload frequency study + July 2026).   

Aylık Yükleme Sıklığı    Kanal Sayısı Kohortu    Medyan Aylık Görüntüleme Büyümesi    Medyan Aylık Abone Büyümesi
1'den az    1.889.839    %0.53    %0.00 (Durağan)
1 - 3 video    2.546.600    %0.89    %0.10
4 - 7 video    1.952.305    %1.32    %0.39
8 - 11 video    1.107.457    %1.70    %0.63
12 ve üzeri    2.714.077    %2.18    %0.91
Söz konusu veri seti incelendiğinde, ayda 12 ve üzeri video yükleyen kanalların, ayda 1'den az yükleyen kanallara kıyasla görüntüleme büyümesinde 4.1 kat, abone büyümesinde ise doğrusal bir artış yakaladığı görülmektedir. Planlanan yayın stratejisi (haftada 1 dikey, ayda 1 yatay video) kanalı ayda "4 - 7 video" segmentine yerleştirmektedir. Bu frekans, sıfır büyüme riskini ortadan kaldıran sürdürülebilir bir taban çizgisi sağlasa da, en agresif büyüme ivmesinin (12+ video) altında kalmaktadır.

İlk 1.000 aboneye ulaşma süreci incelendiğinde ise, 32.926.088 kanal verisi (Eylül 2026 itibarıyla), video stokunun hacmi ile başarı arasında doğrudan bir korelasyon olduğunu göstermektedir (ETİKET: [ÖLÇÜLDÜ] 32.926.088 kanal analizi, KAYNAK SINIFI: Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://vidiq.com/tr/research/youtube-uploads-1000-subscribers/ + vidIQ study + September 2026).   

Net Video Artışı (360 Günlük Pencere)    Kohorttaki Toplam Kanal    1.000 Aboneye Ulaşan Kanal Sayısı    Başarı Oranı (Share)
0 Video (Değişimsiz)    27.360.211    56.008    %0.20
1 - 11 Video    3.423.276    63.657    %1.86
12 - 51 Video    1.259.198    108.952    %8.65
52 ve Üzeri Video    883.403    271.792    %30.77
Eldeki 37 videoluk stok ve yıllık planlanan ~64 video (52 haftalık Shorts + 12 aylık Vlog) kapasitesi, kanalı istatistiksel olarak başarı şansı en yüksek (%30.77) kohortun içine sokmaktadır. Bu veriler ışığında, üretim hattının ağır olması bir dezavantaj gibi görünse de, bir yıllık perspektifte gerekli hacim barajını aşacak kapasitededir.

1.2. Yeni Kanalın Soğuk Başlangıcı (Cold Start) ve Platform Test Mekanizmaları
Kanalın hiçbir izleyici geçmişi, abonesi veya veri izi olmadığında, makine öğrenimi modelleri içeriği değerlendirmek için "soğuk başlangıç" protokollerini devreye sokar. 2026 mimarisinde her platformun bu süreci yönetme biçimi farklıdır ve yayın stratejisi bu farklılıklara göre şekillendirilmelidir.

YouTube, 2026 güncellemeleri itibarıyla yeni içerikleri haftalar yerine günler içinde agresif bir şekilde test eden bir model benimsemiştir (ETİKET: [ÖLÇÜLDÜ] Algoritma mimarisi açıklaması, KAYNAK SINIFI: Platform temsilcisinin kamuya açık açıklaması, ÇÖZÜMLENEBİLİR KAYNAK: https://outlierkit.com/resources/youtube-viewer-satisfaction-algorithm-2026/ + Todd Beaupré interview + September 2026). Shorts platformunda, sistem yeni bir videoyu önce 50 ila 500 kişilik rastgele ancak kategoriyle ilintili olabilecek bir "tohum kitleye" (seed audience) gösterir. Bu aşamada video "Görüntülenen vs. Kaydırılan" (Viewed vs. Swiped Away) oranında başarılı olursa (kaydırma oranı %50'nin altındaysa), sistem içeriği milyonlarca kişiye ulaşabilecek daha geniş havuzlara iter (ETİKET: [ÖLÇÜLDÜ] Algoritma test mekanizması, KAYNAK SINIFI: Pazarlama blogu, ÇÖZÜMLENEBİLİR KAYNAK: https://influenceflow.io/resources/optimizing-youtube-shorts-the-complete-2026-masterclass-for-creators-and-brands/ + Demystifying the YouTube Shorts Algorithm).   

Instagram Reels cephesinde ise, soğuk başlangıç sorunu "Trial Reels" (Deneme Reels) özelliği ile kurumsallaştırılmıştır. 2024 sonunda tanıtılan ve 2026'da zamanlanabilir hale gelen bu özellik, yaratıcıların içeriklerini yalnızca takipçi olmayan soğuk kitlelere 24 ila 72 saat boyunca göstermesine olanak tanır. Trial Reels, sistemin içerik performansını bağlı kitle (connected audience) önyargısı olmadan ölçmesini sağlar (ETİKET: [ÖLÇÜLDÜ] Özellik dokümantasyonu ve Vaka Analizi, KAYNAK SINIFI: Platform temsilcisi ve vaka analizleri, ÇÖZÜMLENEBİLİR KAYNAK: https://reshmashaji.com/blog-instagram-trial-reels-complete-guide/ + History of Trial Reels). Instagram başkanı Adam Mosseri'nin beyanlarına göre, Trial Reels genellikle normal Reels'lere göre daha az erişim alsa da, başarılı olanların otomatik olarak tüm kitleye yayıldığı (Auto Graduation) bir sistem mevcuttur (ETİKET: [ÖLÇÜLDÜ] Platform başkanı açıklaması, KAYNAK SINIFI: Platform temsilcisi açıklaması, ÇÖZÜMLENEBİLİR KAYNAK: https://postfa.st/blog/instagram-trial-reels + Do Trial Reels get less views).   

TikTok'un soğuk başlangıç modeli ise "gecikmeli patlama" (delayed explosion) etkisi ile karakterizedir. Algoritma, içeriği yayınlandıktan hemen sonra küçük bir kitleye sunar, ancak yeterli veri toplayamazsa veya içeriğin yaşam döngüsüne uygun bir trend yakalarsa, günler veya haftalar sonra videoyu yeniden "For You" (Sizin İçin) akışına sokabilir (ETİKET: [İDDİA] İçerik dağıtım davranışı, KAYNAK SINIFI: Bağımsız analiz / Pazarlama blogu, ÇÖZÜMLENEBİLİR KAYNAK: https://getkoro.app/blog/how-long-should-i-wait-to-post-another-tiktok + delayed explosion effect). Bu durum, düşük performans gösteren videoların erken silinmesinin platformda büyük bir hata olduğu anlamına gelir.   

1.3. Shorts İzleyicisinin Uzun Videoya Geçişi ve Etkileşim Dinamikleri
Stratejideki en temel varsayımlardan biri olan "aboneleri Shorts'tan beklemek, izlenme saatini ise bu abonelerin uzun formu izlemesiyle sağlamak" hipotezi, 2026 YouTube algoritmik yapısında geçersizdir. YouTube Keşif ve Büyüme Direktörü Todd Beaupré'nin Eylül 2026'daki detaylı açıklamalarına göre, platform artık "Formata Duyarlı Keşif" (Format-Aware Discovery) sistemini kullanmaktadır. Bu sisteme göre, bir kullanıcı yalnızca Shorts izleme alışkanlığına sahipse, abone olduğu kanalın uzun form videoları onun ana sayfasında gösterilmez. Aynı şekilde, uzun form izleyicisine de Shorts gösterilmez (ETİKET: [ÖLÇÜLDÜ] Algoritma mimarisi, KAYNAK SINIFI: Platform temsilcisinin kamuya açık açıklaması, ÇÖZÜMLENEBİLİR KAYNAK: https://outlierkit.com/resources/youtube-viewer-satisfaction-algorithm-2026/ + Format-aware discovery + September 2026). Bu ayrım, Shorts videolarının uzun form videoların Tıklama Oranını (CTR) organik olarak öldürmesini engellemek için yapılmıştır, ancak aynı zamanda formatlar arası organik çapraz geçişi de (cross-pollination) neredeyse imkânsız hale getirmiştir.   

Formatlar arası etkileşim uçurumunu ölçmek için 17 büyük kanaldaki 1.261 video (760 Shorts, 501 uzun form) üzerinde Eylül 2026'da yapılan bağımsız bir analiz, uzun form videoların Shorts videolarına kıyasla medyan bazda 1.91 kat daha fazla görüntüleme (2.363.444'e karşı 1.234.644) aldığını ortaya koymuştur (ETİKET: [ÖLÇÜLDÜ] 1.261 video analizi, KAYNAK SINIFI: Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://www.socialcrawl.dev/blog/youtube-shorts-vs-long-form + SocialCrawl study + September 2026).   

Metrik (Medyan Değerler)    Uzun Form Video    Shorts    Oran (Uzun / Shorts)
Medyan Görüntüleme    2.363.444    1.234.644    1.91x
Saniye Başına Görüntüleme    2.383    23.710    0.10x (Shorts 9.95x daha verimli)
Etkileşim Oranı (Beğeni+Yorum/Görüntüleme)    %2.18    %2.73    0.80x
Yorumların Beğeniye Oranı    %4.7    %1.2    3.91x
Veriler, saniye başına görüntüleme (views per second) açısından Shorts'un 9.95 kat daha verimli olduğunu, ancak derin etkileşim (yorum ve uzun süreli sadakat) açısından uzun formun üstünlüğünü koruduğunu göstermektedir. Bu tablo, izlenme saatinin (watch hours) yatay içerikten, geniş kitle erişiminin ise Shorts'tan beklenmesi gerektiği yönündeki stratejik kararı matematiksel olarak destekler niteliktedir.

Ancak, geçişin sağlanabildiği tek organik platform içi köprü olan "İlgili Video" (Related Video) bağlantısının dönüşüm oranı son derece düşüktür. Kaydırma (swipe) modundaki Shorts izleyicisi, uzun bir taahhüde girmek istemez (ETİKET: [İDDİA] Düşük dönüşüm oranı, KAYNAK SINIFI: Bağımsız vaka / Topluluk yorumu, ÇÖZÜMLENEBİLİR KAYNAK: https://www.reddit.com/r/NewTubers/comments/1pj2xau/anyone_have_experience_using_short_to_draw_viewer/ + Reddit User Ok_Print2643). Dönüşümü sağlamak için Shorts videosunun son 5 saniyesinde izleyiciye net bir "ödül" vaat edilmeli ve görsel olarak bağlantıya işaret edilmelidir (ETİKET: [ÖLÇÜLDÜ] Strateji yönergesi, KAYNAK SINIFI: Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://www.nbksocial.com/journal/convert-youtube-shorts-views-into-long-form-growth/ + Step 3: Earn the click). Geçişin başarıldığı senaryolarda, Shorts üzerinden uzun form videoya gelen izleyicilerin etkileşim oranının %40 daha yüksek olduğu ölçülmüştür (ETİKET: [ÖLÇÜLDÜ] Araştırma verisi, KAYNAK SINIFI: Pazarlama blogu / Influencer Marketing Hub 2026 araştırması, ÇÖZÜMLENEBİLİR KAYNAK: https://influenceflow.io/resources/youtube-shorts-and-long-form-video-strategy-the-complete-2026-creators-guide-1/ + Influencer Marketing Hub 2026 research).   

YouTube Partner Programı (YPP) şartlarına dair en kritik kural şudur: 4.000 geçerli izlenme saati kotasına, Shorts akışından elde edilen izlenme süreleri kesinlikle dahil edilmez (ETİKET: [ÖLÇÜLDÜ] Resmi Monetizasyon Kuralı, KAYNAK SINIFI: Platform dokümanı / Resmi temsilci, ÇÖZÜMLENEBİLİR KAYNAK: https://support.google.com/youtube/thread/247287077/watchtime-not-counting-in-yt-studio-in-earn-page?hl=en + PeggyK / YouTube Product Expert + 2024). İzlenme saati yalnızca uzun form (yatay) videolardan organik olarak toplanmalıdır.   

1.4. Yapay Zekâ, Şablon İçerik ve Özgünlük Politikaları (2025-2026)
Kanalın ürünü "sabit kameralı, anlatıcısız, konuşmasız ve yapay zekâ üretimi kliplerden" oluştuğu için, YouTube'un en güncel inorganik ve tekrarlayan içerik politikalarının tam merkezinde yer almaktadır.

YouTube'un 16 Temmuz 2026'da güncellediği "Özgün Olmayan İçerik" (Inauthentic Content) kuralı, içerik üreticilerini üç ana kategoride cezalandırmakta ve monetizasyon hakkını ellerinden almaktadır. Özellikle "toplu olarak üretilmiş şablonlar (templates made in bulk) veya benzersiz bir değer katmayan tekrarlayan yapıdaki videolar" doğrudan hedef alınmıştır. 1 Ekim 2026 tarihinde yürürlüğe giren Shorts Özgünlük Güncellemesi ile bu kural daha da sertleştirilmiş; salt ekrandakini tanımlayan seslendirmeler, teknik kesmeler veya ufak şablon değişiklikleri içeren videolar "orijinal" kabul edilmekten çıkarılmış ve algoritmanın bu kanalların Shorts akışındaki erişimini kısıtlayacağı resmi olarak duyurulmuştur (ETİKET: [ÖLÇÜLDÜ] Resmi Politika Güncellemesi, KAYNAK SINIFI: Platform Dokümanı, ÇÖZÜMLENEBİLİR KAYNAK: https://aituber.app/blog/youtube-algorithm-changes/ + YouTube Algorithm Changes 2026 + October 2026).   

Yapay zekâ beyanı (AI Disclosure Label) Mayıs 2026 itibarıyla zorunlu kılınmış olsa da, YouTube, AI etiketinin algoritma tavsiyelerini, erişimi veya para kazanmayı olumsuz etkilemediğini açıkça belirtmiştir (ETİKET: [ÖLÇÜLDÜ] Resmi Politika, KAYNAK SINIFI: Platform Dokümanı, ÇÖZÜMLENEBİLİR KAYNAK: https://aituber.app/blog/youtube-algorithm-changes/ + AI Disclosure Labels + May 2026).   

Buradaki asıl risk, yapay zekâ kullanımı değil; "tek sabit kamera ve sessiz ardışık klipler" yapısının makine öğrenimi modelleri tarafından "otomatize edilmiş düşük kaliteli şablon spam" (low-quality AI spam) olarak işaretlenme ihtimalidir. Bu majör engeli aşmanın tek stratejik yolu, ayda bir planlanan 8-15 dakikalık "Yapım Günlüğü" (Making-Of) vloglarıdır. Bu vloglar, içeriğe bir insan bağlamı, bir üretim hikâyesi ve analitik bir yorum katarak, kanalın algoritma nezdindeki "özgün yaratıcı" (authentic creator) kimliğini tesis edecek ve manuel moderasyon süreçlerinde kanalı koruyacaktır.

1.5. Timelapse ve Süreç Kanalları Üzerine Vaka Zaman Çizelgeleri
2024-2026 döneminde inşaat, mimari tasarım ve 3D otonom drone taramaları yapay zekâ entegrasyonuyla büyük bir endüstri standardı haline gelmiştir (Örn: Finch 3D, Airteam, Imerso platformları) (ETİKET: [ÖLÇÜLDÜ] Endüstri Analizi, KAYNAK SINIFI: Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://zekaiwork.com/professions/ai-construction-engineering-tools/ + AI Construction Engineering Tools).   

Bununla birlikte, yalnızca yapay zekâ ile üretilmiş inşaat timelapse süreci üzerine odaklanmış, milyon aboneye ulaşmış ve gün gün zaman çizelgesi (timeline) yayınlanmış spesifik bir YouTube bağımsız vaka analizi bulunmamaktadır (ETİKET: [BİLİNMİYOR], KAYNAK SINIFI: Yok, ÇÖZÜMLENEBİLİR KAYNAK: Yok). Literatürdeki AI inşaat makaleleri genellikle proje yönetimi, risk analizi ve BIM (Bina Bilgi Modellemesi) entegrasyonuna odaklanmaktadır (ETİKET: [ÖLÇÜLDÜ] Literatür Taraması, KAYNAK SINIFI: Akademik İnceleme, ÇÖZÜMLENEBİLİR KAYNAK: https://www.emerald.com/ecam/article/33/1/361/1259130/Review-of-artificial-intelligence-applications-in + Bibliometric analysis results). Bu nedenle, kanalın büyüme stratejisi spesifik bir niş vakadan ziyade, platformların makro-dağıtım kuralları üzerinden optimize edilmelidir.   

Bölüm 2: Stok ve Serinin Yönetimi
Eldeki 37 bitmiş film ve kanalın sıfır abone tabanı, ideal bir kontrollü deney ortamı sunmaktadır. 37 film, haftada 1 dikey yayın hızıyla yaklaşık 9 aylık bir yayın stoku demektir. Bu stokun stratejik yönetimi, algoritmanın öğrenme eğrisini şekillendirecektir.

2.1. Yayın Sırası, Hızı ve Toplu Yükleme Riskleri
Yayın hızı konusunda kesin kural: Toplu yükleme (batch upload) kesinlikle yapılmamalıdır.

Kısa süre içinde birden fazla video yüklemek, tüm modern sosyal medya algoritmalarının spam filtrelerini tetikler. Özellikle TikTok ve YouTube'da bu davranış "bot aktivitesi" veya "şablon içerik üretimi" olarak işaretlenir. TikTok'ta aynı günde birden fazla video yüklemek veya etkileşim almayan videoyu silip hemen yenisini koymak, hesabın "shadowban" (gölge yasak) statüsüne alınmasına ve "For You" (Sizin İçin) akışından dışlanmasına neden olur (ETİKET: [ÖLÇÜLDÜ] Platform kısıtlama tetikleyicisi, KAYNAK SINIFI: Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://www.tokportal.com/learn/tiktok-shadowban-what-it-is-how-to-detect-and-fix + TikTok Shadowban). Haftalık düzenli dağıtım, algoritmanın veriyi işlemesi, kitle davranışlarını analiz etmesi ve tohum kitleyi (seed audience matching) optimize etmesi için gereken en sağlıklı aralıktır.   

Yayın sırasına gelince; 37 filmin yapay zekâ değerlendiricisiyle puanlanmış olması değerli bir metriktir, ancak yapay zekâ skorları algoritmik insan tepkisini (duygusal kanca, merak unsuru) %100 yansıtmaz. Sıralama en iyiden en kötüye değil, "konu dönüşümlü" (topic rotation) olmalıdır. Ardışık haftalarda aynı renk paletine, aynı kamera açısına veya birbirine çok benzeyen yapılara sahip filmlerin yayınlanması, izleyicide "bu videoyu daha önce gördüm" yanılsaması (audience fatigue) yaratarak kaydırma (swiped away) oranını dramatik şekilde artırır.

2.2. Düşük Performanslı Videoyu Silme ve Yeniden Yükleme
Düşük performans gösteren bir videoyu silip yeniden yüklemek, 2026 yılı platform ekosistemindeki en büyük operasyonel hatadır.

YouTube Kuralları: YouTube Büyüme ve Keşif Direktörü Todd Beaupré'nin Mart 2024'te yaptığı kesin uyarıya göre: "Çok geçerli bir nedeniniz yoksa videoları silmeyin. Bir videoyu sildiğinizde, kanalınızın o videoyu izleyen kitleyle olan bağlantısını tamamen koparırsınız. Büyümenizi maksimize etmek istiyorsanız, videolarınızı herkese açık tutun veya çok gerekliyse liste dışı bırakın." (ETİKET: [ÖLÇÜLDÜ] Algoritma mimarı beyanı, KAYNAK SINIFI: Platform temsilcisinin kamuya açık açıklaması, ÇÖZÜMLENEBİLİR KAYNAK: https://www.searchenginejournal.com/youtube-warns-channels-against-deleting-videos/512126/ + Todd Beaupré statement on X + March 25, 2024).   

TikTok ve Instagram Kuralları: TikTok, aynı video dosyasının özet (hash) değerini okuyup kopya içerik (duplicate content) tespit sistemlerini çalıştırır. Bir videoyu silip aynı dosyayı tekrar yüklemek, algoritmanın ikinci yüklemeyi otomatik olarak basılamasına (suppress) ve hesabı şüpheli listesine almasına neden olur (ETİKET: [ÖLÇÜLDÜ] Platform kuralı, KAYNAK SINIFI: Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://getkoro.app/blog/how-long-should-i-wait-to-post-another-tiktok + Deleting and Reposting).   

Aksiyon: Performans ne kadar kötü olursa olsun hiçbir video silinmeyecektir. Eğer içerik akışta veya marka imajında onarılamaz bir zarar yaratıyorsa, işlem "Silmek" değil "Gizliye Almak" (Unlisted / Private) olmalı ve bu işlem dahi video yayınlandıktan en az 72 saat sonra yapılmalıdır.

2.3. Ekosistem Kurulumu: Kapaklar, Oynatma Listeleri ve Yönlendirmeler
Profilin görsel bütünlüğü, algoritmanın kanalı sınıflandırması ve kullanıcının abone olma kararı üzerinde doğrudan etkilidir.

Kapak (Thumbnail) Stratejisi: Bütün kapakların filmin son karesinden (dönüşümün veya inşaatın bittiği an) seçilmesi son derece doğru bir stratejidir. İzleyiciye "vaat edilen nihai sonuç" sunulması, merakı tetikleyerek Tıklama Oranını (CTR) artırır. 2026 optimizasyon standartları, profil ızgarasında karmaşayı önleyen, tek bir ana fikre sahip (One-Idea Thumbnail), yüksek kontrastlı ve mobil ekranda net okunan kapakları ödüllendirmektedir (ETİKET: [ÖLÇÜLDÜ] Optimizasyon kuralı, KAYNAK SINIFI: Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://vidiq.com/blog/post/understanding-youtube-algorithm/ + 7-Step Optimization Checklist).   

Oynatma Listeleri ve Seri Adlandırma: Algoritmanın kitleyi tanımlayabilmesi için içerikler yapı tipine göre (örn. "Cyberpunk Gökdelenler", "Ekolojik Kırsal Evler") mantıksal serilere ve oynatma listelerine ayrılmalıdır. Seri adlandırmaları, meta verilere (başlık, açıklama) ortak kelime dağarcığı olarak yansıtılmalıdır.   

Sabitlenmiş Yorum ve Uzun Forma Geçiş: Her dikey videonun altında, uzun forma yönlendiren ve değer katan (value-add) bir sabitlenmiş yorum (Pinned Comment) bulunmalıdır. Ancak, Shorts üzerinden asıl geçiş köprüsü, video açıklamasındaki linkler değil, YouTube Studio üzerinden kurulan "İlişkili Video" (Related Video) modülüdür. Bu özellik, 16:9 yapımdaki uzun versiyona doğrudan ve tıklanabilir bir platform içi köprü oluşturur.   

2.4. Üç Platform Arasında Senkronizasyon ve Yayın Aralığı
Farklı platformların algoritmik tepki süreleri, stratejik bir test alanı yaratır.

Eğer üretim hattı esnekliğe sahip olsaydı, Instagram'ın "Trial Reels" (Deneme Reels) özelliği kullanılarak aynı filmin iki farklı kurgusu (farklı ilk 3 saniye kancası ile) sadece takipçi olmayanlara 24 saatliğine yayınlanır ve kazanan versiyon tüm platformlara yüklenirdi (ETİKET: [ÖLÇÜLDÜ] Platform test özelliği, KAYNAK SINIFI: Platform Dokümanı / Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://postfa.st/blog/instagram-trial-reels + Trial Reels Auto Graduation + 2026).   

Ancak eldeki dosyalar (7 klip x 8 sn = ~28 sn) kilitli ve tamamlanmış olduğundan, A/B testi yapılamayacaktır. Bu durumda eşzamanlı (aynı gün) yükleme yapılması operasyonel olarak en verimli yoldur. Kritik kural: TikTok filigranı (watermark) veya başka bir uygulamanın damgasını taşıyan videolar, Instagram Reels algoritması tarafından otomatik olarak baskılanır (ETİKET: [ÖLÇÜLDÜ] Dağıtım cezası, KAYNAK SINIFI: Platform temsilcisi açıklaması, ÇÖZÜMLENEBİLİR KAYNAK: https://buffer.com/resources/instagram-algorithms/ + Adam Mosseri watermark rules). Bu nedenle her platforma aynı orijinal, saf (ham) dosya bağımsız olarak yüklenmelidir.   

Bölüm 3: Karar Protokolü ve Veri Değerlendirme
Sıfır aboneli küçük bir kanalda, tek bir filmi yargılamak, gürültüyü (noise) sinyalden ayırmak ve formatı değiştirmek için doğru eşiklerin beklenmesi hayati önem taşır. Aceleci kararlar, algoritmanın kitle eşleştirme sürecini bozar.

3.1. Karar İçin Gereken Minimum Veri Süreleri
Bir videonun başarısız olduğuna karar vermeden önce platformların doğal dağıtım sürelerine saygı duyulmalıdır:

YouTube Uzun Form: Yeni kanallarda arama motoru optimizasyonu (SEO) ve önerilen videolar trafiğinin oturması zaman alır. Bir uzun form videonun nihai performansını ölçmek için en az 30 gün beklenmelidir.   

YouTube Shorts: Başlangıçtaki tohum kitle testinden (50-500 kişi) geçtikten sonra, makro dağıtım kararları algoritma tarafından genellikle ilk 72 saat içinde şekillenir.

TikTok: Gecikmeli patlama etkisi nedeniyle, bir videonun performansı en az 14 gün boyunca ölü ilan edilmemelidir. Silme işleminden kaçınılmasının ana nedeni de bu gecikmeli değerlendirmedir.   

Instagram Reels: İzlenme ve etkileşim döngüleri (Trial Reels dahil) 24 ile 72 saat arasında tepe noktasına ulaşır.   

3.2. Gürültüyü Ayırma (Noise Filtering) Yolları
Kanalın verilerini analiz ederken dış piyasa metrikleriyle değil, kanal içi (intra-channel) verilerle kıyaslama yapılmalıdır.

Kanal İçi Kıyas (Kayan Pencere): Sektör CTR'si (%2 - %10) yeni kanalın performansını ölçmekte yetersizdir. YouTube Keşif Direktörü Todd Beaupré'nin belirttiği üzere, bir videonun CTR'ı ana sayfaya ve geniş kitleye çıkıldıkça doğal ve dramatik olarak düşer (ETİKET: [ÖLÇÜLDÜ] Metrik davranışı, KAYNAK SINIFI: Platform temsilcisi açıklaması, ÇÖZÜMLENEBİLİR KAYNAK: https://outlierkit.com/resources/youtube-click-through-rate/ + Todd Beaupré interview + September 2026). Bu nedenle "düşük CTR her zaman kötü videodur" varsayımı yanlıştır. Değerlendirme daima son 5 videonun medyanına (kayan pencere) göre ve sadece aynı trafik kaynağı (örn. Sadece Ana Sayfa veya Sadece Önerilenler) filtrelenerek yapılmalıdır.   

Aynı Anda Tek Değişken (İzolasyon): Eğer bir videonun performansı düşükse ve bir sonraki videoda değişiklik yapılacaksa, aynı anda hem kapak tasarımı, hem konu, hem de hız değiştirilmemelidir. 37 videonun hızı ve süresi sabit (~28 saniye, %200 hız) olduğundan, elimizdeki tek izole edilebilir değişken görsel konu ve renk paletidir.

3.3. Büyümeyi Öngören Erken Metrikler (Sinyal Hiyerarşisi)
2026 yılı itibarıyla dağıtımı tetikleyen ve kanalın büyümesini öngören "Kuzey Yıldızı" (North Star) metrikleri, basit izlenme sayılarından çok daha komplekstir. Algoritma hiyerarşisi şu şekildedir:

YouTube Shorts: En kritik iki metrik "Görüntülenen vs. Kaydırılan Oranı" (Viewed vs Swiped Away) ve "Ortalama Görüntülenme Yüzdesi"dir (APV).

Başarılı bir Shorts, kaydırma oranını %50'nin altında tutmalıdır. Sağlıklı bir eşik %60-70 arası izlenme tercihidir. APV ise, videonun sorunsuz bir şekilde tekrar başa sarması (seamless loop) sağlanarak %100'ün üzerine çıkarılmalıdır. Sistem %100 üzeri izlenmeyi devasa bir memnuniyet sinyali olarak okur (ETİKET: [ÖLÇÜLDÜ] Metrik eşiği, KAYNAK SINIFI: Pazarlama blogu, ÇÖZÜMLENEBİLİR KAYNAK: https://influenceflow.io/resources/optimizing-youtube-shorts-the-complete-2026-masterclass-for-creators-and-brands/ + Understanding viewed vs swiped away).   

YouTube Uzun Form: 2026 algoritmasında CTR (Tıklama Oranı) toplam ağırlıkta yalnızca 38 puana sahipken, "İlk 30 Saniye Tutma Oranı" 85, "Memnuniyet Anketleri" ise 95 ağırlığa sahiptir (ETİKET: [ÖLÇÜLDÜ] Algoritma sinyal hiyerarşisi, KAYNAK SINIFI: Bağımsız analiz / Platform açıklaması, ÇÖZÜMLENEBİLİR KAYNAK: https://outlierkit.com/resources/youtube-viewer-satisfaction-algorithm-2026/ + The 2026 Ranking Signal Stack). Bir uzun form videonun ilk 30 saniyesinde izleyicilerin %60'ından fazlası korunabiliyorsa, video büyümeye adaydır (ETİKET: [ÖLÇÜLDÜ] Bağımsız analiz eşiği, KAYNAK SINIFI: Bağımsız analiz, ÇÖZÜMLENEBİLİR KAYNAK: https://vidiq.com/blog/post/increase-audience-retention-youtube/ + vidIQ channel benchmark).   

TikTok: Tamamlama Oranı (Completion Rate) esastır. 2026 algoritması, virallik için gerekli olan eski %50 tamamlama sınırını %70'e çıkarmıştır (ETİKET: [ÖLÇÜLDÜ] Algoritma kuralı, KAYNAK SINIFI: Pazarlama blogu, ÇÖZÜMLENEBİLİR KAYNAK: https://www.socialync.io/blog/tiktok-algorithm-2026-what-works-now + 7 Key Changes in the 2026 TikTok Algorithm). 28 saniyelik bir video için izleyicinin en az 19 saniye içerikte kalması şarttır.   

Instagram Reels: DM Yoluyla Gönderme (Sends per reach). Adam Mosseri'nin açık beyanına göre, içeriklerin keşfete düşmesini sağlayan en güçlü sinyal "kullanıcıların videoyu mesaj olarak birbirine göndermesi"dir (ETİKET: [ÖLÇÜLDÜ] Platform başkanı açıklaması, KAYNAK SINIFI: Platform temsilcisi açıklaması, ÇÖZÜMLENEBİLİR KAYNAK: https://www.truefuturemedia.com/articles/instagram-reels-reach-2026-business-growth-guide + Three Ranking Factors).   

3.4. Aşama Hedefleri ve Formatı Sorgulama
İlk 10 Video Süreci: İlk 10 dikey videoda abone veya toplam izlenmeye odaklanılmaz. Bu süreç sadece "YouTube'un içeriği doğru kitleyle eşleştirip eşleştiremediğini" izleme (data gathering) aşamasıdır.

Format Sorgulama Noktası: Üst üste 5 videoda (yaklaşık 1 aylık veri periyodu) "Görüntülenen vs. Kaydırılan" oranı %40'ın altındaysa ve APV (Ortalama İzlenme Yüzdesi) %70'in altında kalıyorsa, mevcut format (kamera açısı, klip süresi, anlatıcısız yapı, müzik seçimi) kökten sorgulanmalıdır (ETİKET: [VARSAYIM] Optimizasyon eşiği, KAYNAK SINIFI: Çıkarım, ÇÖZÜMLENEBİLİR KAYNAK: Yok).

İlk 1.000 Abone ve Partner Programı: YouTube Partner Programı için yatay izlenmeden hedeflenen 4.000 saat hedefine odaklanırken, Shorts videoları sadece huninin üst ucunu (keşif ve marka bilinirliği) besleyen araçlar olarak görülmelidir. Ayda 1 yayınlanacak olan 8-15 dakikalık "Yapım Günlüğü" (Making Of) belgeselleri, tutma oranını yükseltip 4.000 saat kotalarını dolduracak, yapay zekâ şablon spam filtrelerini aşacak ve kanalın asıl motoru olacaktır.

Bölüm 4: Benim Varsayımlarımla Çelişenler
Durum analiziniz ile güncel pazar gerçekleri ve 2026 platform kuralları arasında zıtlık oluşturan kritik noktalar aşağıda sıralanmıştır:

"Aboneleri Shorts'tan bekleyip, bu abonelerin uzun formu izlemesi":
YouTube'un 2026 "Formata Duyarlı Keşif" (Format-Aware Discovery) mimarisine göre; Shorts izleyicileri uzun formları, uzun form izleyicileri de Shorts'ları organik olarak beslemez. Çapraz format geçiş oranı, kullanıcının doğrudan "İlgili Video" linkine tıklaması haricinde son derece düşüktür (ETİKET: [ÖLÇÜLDÜ] Kullanıcı davranışı, KAYNAK SINIFI: Platform açıklaması, ÇÖZÜMLENEBİLİR KAYNAK: https://outlierkit.com/resources/youtube-viewer-satisfaction-algorithm-2026/ + Format-aware discovery). Yani Shorts'tan gelen 1.000 abone, uzun videonuzu ana sayfalarında görmeyecek veya tıklamayacaktır. Uzun form videonuz, kendi bağımsız keşif metriklerini kendi kitle havuzunda oluşturmak zorundadır.   

"Haftada bir video yüklemek gerçekçi bir soğuk başlangıç hızıdır":
Büyük veri setleri (10.2 milyon kanal), en yüksek büyüme eşiğinin ayda 12+ video (haftada 3-4 video) yüklemelerle yakalandığını göstermektedir. Üretim hattının ağırlığı nedeniyle haftada 1 dikey kısıtlamasına uymak zorunlu olsa da, bu durumun büyüme eğrisini doğal olarak yataylaştıracağı ve 1.000 abone hedefine ulaşmanın istatistiksel olarak 6 ila 9 ay arasında bir zaman alabileceği kabul edilmelidir (ETİKET: [VARSAYIM] İstatistiksel büyüme projeksiyonu, KAYNAK SINIFI: Çıkarım, ÇÖZÜMLENEBİLİR KAYNAK: Yok).   

"Formatın (Sessiz, Salt Zaman Atlamalı Sabit Kamera) Platformlar Tarafından Doğal Olarak Destekleneceği":
2026'daki "Şablon İçerik" (Inauthentic Content) ve yapay zekâ güncellemeleri, insan bağlamı ve anlatımı olmayan, otomatize edilmiş ardışık klipleri "düşük değerli spam" riski grubuna itmektedir. Ayda bir eklenecek olan kamera arkası/yapım süreci (Vlog), bu cezadan kaçınmak ve kanalın arkasında gerçek bir yaratıcı vizyon olduğunu algoritmaya ve moderatörlere kanıtlamak için opsiyonel değil, yaşamsal bir zorunluluktur.   

Ek A: 90 Günlük Açılış Takvimi (37 Filmlik Stok ve Haftada 1 Yükleme Varsayımıyla)
Aşağıdaki takvim, stoku tüketmeden algoritmaya istikrarlı sinyal göndermeyi hedefler.

Hafta    Platform    Film Türü (Format)    Amaç Metriği (Kuzey Yıldızı)    Karar Noktası / Eylem
Hafta 1    YT/IG/TT    Dikey (Shorts/Reel) 1    Sistem test havuzuna girmek (Tohum Kitle)    İzleme: Sadece Görüntülenen vs. Kaydırılan oranına bak.
Hafta 2    YT/IG/TT    Dikey (Shorts/Reel) 2    Ortalama İzlenme Yüzdesi (APV)    Karar: Videolar arası APV farkını kaydet. Erken değişiklik yok.
Hafta 3    YT/IG/TT    Dikey (Shorts/Reel) 3    IG için Paylaşım (Sends), TT için %70 Tamamlama    İzleme: Hangi platformda daha hızlı algoritmik yayılım başladığını not et.
Hafta 4    Sadece YT    Yatay (Uzun Form) 1    İzlenme Süresi (Watch Time) ve İlk 30s (%60)    Karar: Uzun formun CTR'ını ölç. Tüm Dikey 1-3'e Related Video ekle.
Hafta 5    YT/IG/TT    Dikey (Shorts/Reel) 4    Oynatma Listesi sürekliliği ve Related Video Tıklaması    Sorgulama: Görüntülenen/Kaydırılan < %40 ise, 5. video için başı (hook) hızlandır.
Hafta 6    YT/IG/TT    Dikey (Shorts/Reel) 5    Kanalın medyan CTR'ını oluşturma (Kayan Pencere)    Karar: TikTok shadowban riski ölçümü (Görüntüleme aniden sıfıra düşerse eylem yapma).
Hafta 7    YT/IG/TT    Dikey (Shorts/Reel) 6    İlgili Videoya Geçiş Oranı    Eylem: Shorts'ların son 5 saniyesindeki metni (CTA) ve yönlendirmeyi güncelle.
Hafta 8    Sadece YT    Yatay (Vlog/Yapım) 2    Memnuniyet ve Geri Dönen İzleyici Sinyali    Kritik Karar Noktası: YPP inauthentic içerik filtresinden çıkış onayı ve güvenilirlik tesisi.
Hafta 9-12    YT/IG/TT    Dikey 7-10    Stabil Büyüme (Abone dönüşümü ve Kitle Oturması)    Pivot: Veriler ışığında 13. videodan itibaren montaj hızını veya kancayı (hook) kurgula.
Ek B: Karar Eşikleri Tablosu
Aşağıdaki tablo, bir filmi değerlendirmeden önce baz alınması gereken veriye dayalı asgari eşikleri listeler.

Metrik    Eşik    Kaynak / Etiket    Eylem (İhlal Durumunda)
YT Görüntülenen vs Kaydırılan (Shorts)    > %50 - %60 (İdeal %70)    
[ÖLÇÜLDÜ] Pazarlama vaka analizi

İlk 3 saniyedeki görsel sıçramayı (hook) artır.
YT Ortalama İzlenme Yüzdesi (APV)    > %100    
[ÖLÇÜLDÜ] Pazarlama vaka analizi

Döngü (loop) yaratacak şekilde filmin sonu ile başını pürüzsüz bağla.
YT CTR (Tıklama Oranı) (Uzun Form)    %2 - %10 (Kanal içi medyana göre kıyasla)    
[ÖLÇÜLDÜ] Platform açıklaması (Beaupré)

CTR medyanın altındaysa küçük resmi değiştir; üstündeyse İlk 30s tutmaya odaklan.
YT İlk 30 Saniye Tutma Oranı (Uzun Form)    > %60    
[ÖLÇÜLDÜ] Bağımsız analiz (vidIQ)

Başlangıçtaki yavaş girişi at, doğrudan tempolu inşaata gir.
TikTok Tamamlama Oranı (Completion)    > %70    
[ÖLÇÜLDÜ] Bağımsız analiz

Tamamlama düşükse videoyu 28 saniyeden 15 saniyeye (veya 3x hıza) kırp.
IG DM Paylaşım Oranı (Sends per reach)    [BİLİNMİYOR] (Açıklanmadı ancak birincil sinyal)    
[ÖLÇÜLDÜ] Platform temsilcisi (Mosseri)

"Sonucu görmek için gönder" gibi paylaşıma itecek mimari sürprizleri vurgula.
Shorts'tan Uzun Forma Dönüşüm Oranı    [BİLİNMİYOR]    [VARSAYIM] Sektörel tahminim: <%1    Shorts sonu 5 saniyeye net harekete geçirici mesaj (CTA) ekle.
  
Ek C: Seri ve Izgara Kartı
Kanalın markalaşması ve izleyici navigasyonu için her videonun paketlenmesinde aşağıdaki standart şablon kullanılacaktır.

Paketleme Unsuru    Format ve İçerik Kuralı    Amacı ve İşlevi
Seri Adı (Kavramsal)    "AI Build Timelapse: [Proje Tipi]" (Örn: AI Build Timelapse: Cyberpunk City, Rural Cabin)    Algoritmanın ve izleyicinin konu kümelerini tanıyıp eşleştirmesini sağlamak.
Oynatma Listesi Düzeni    
1. Shorts Akışı (Bölüm 1 - 10)


2. Tam Çekim Uzun Filmler (16:9)


3. Behind the Machine (Nasıl Üretildi Vlogları)

Kullanıcıları seans içinde tutarak (binge-watching) toplam izlenme süresini artırmak.
Kapak Düzeni (Thumbnail)    Kapak mutlaka inşaatın / dönüşümün bittiği final karesinden alınmalıdır. Tek fikir, temiz zemin, büyük yapı.    
İzleyiciye nihai sonucun ne olduğunu göstererek tıklama oranını (CTR) maksimize etmek.

Sabitlenmiş Yorum    "Did you spot the structural shift at 0:15? See the full architecture process and how AI built this frame-by-frame here 👉 [Uzun Form Bağlantısı]"    Kısa form izleyicisine entelektüel merak (value-add) katarak uzun forma (vloga) yönlendirmek.
Uzun Forma Bağlantı Köprüsü    Açıklama kısmına link yazmak yerine YT Studio içinden "İlişkili Video" (Related Video) modülü ile gömülmelidir.    
Tıklanabilir tek doğal yönlendirme aracı ile huniyi (funnel) tamamlamak.

  
Ek D: Haftalık Kontrol Listesi
Her video yayın döngüsünde istisnasız uygulanacak 12 maddelik işleyiş. Her kural ihlalinde tabloda belirtilen tekil eylem uygulanacaktır:

No    Kontrol Maddesi (Soru)    İhlalde Yapılacak Eylem
1    Kesmelerin sadece zamanı atladığından ve yapı bütünlüğünü bozmadığından emin olundu mu?    ERTELE
2    Dikey video 7 klip x 8sn hızlandırmayla tam 28 saniye, platform algoritma sürelerine uygun mu?    ERTELE
3    Videoda farklı bir platformun (örn: TikTok filigranı) logosu veya damgası var mı?    ERTELE
4    İlgili platformların "Yapay Zekâ ile Üretilmiştir" şeffaflık etiketi işaretlendi mi?    ERTELE
5    Kapak fotoğrafı (Thumbnail), filmin final (%100 tamamlanmış) anını, temiz ve tek odaklı gösteriyor mu?    ERTELE
6    Spam Sinyali Kontrolü: Son 48 saat içinde bu platforma başka bir video yüklendi mi? (Toplu yükleme engeli)    ERTELE
7    Köprüleme: Shorts yayınına girilmeden önce Studio'da "Related Video" ile Uzun form bağlandı mı?    ERTELE
8    Klibin son 5 saniyesinde izleyiciyi uzun videoya iten güçlü bir görsel/bağlamsal CTA (harekete geçirici mesaj) var mı?    FORMATI SORGULA
9    Kanal Sağlığı: Kötü performanslı olduğu düşünülen eski videolar silindi mi veya silinmesi planlanıyor mu?    ERTELE (Sadece Gizliye Al)
10    Metrik İzleme (APV): Son 3 Shorts'un Ortalama İzlenme Yüzdesi (APV) %70'in altında mı kalıyor?    FORMATI SORGULA
11    Metrik İzleme (Swiped Away): Son 3 Shorts'ta "Kaydırıp Geçen" oranı %60'ın üzerinde mi?    FORMATI SORGULA
12    Özgünlük Koruması: Bu ay kanala insan unsurunu kanıtlayan yatay "Yapım Günlüğü" (Vlog) eklendi mi?    YÜKLE (Yeni Shorts yerine önceliği Vlog'a ver)
