# Dikey timelapse filmleri için kapak kılavuzu
**Instagram Reels öncelikli · TikTok ve YouTube Shorts uyarlaması**  
**16 Ekim 2026 · Türkçe uygulama / İngilizce üretim promptları**

## 0. 🔗 DEPO UYARLAMASI — bu kılavuz depoda nasıl bağlanır (ajan eki · 16.10.2026)

```
NE ZAMAN     dikey her filmde: PLAN aşamasında (GN kompozisyonu) + KAPAK dosyası + yayın öncesi prova.
             Yatay (16:9) kapak MUZIK_VE_KAPAK §2'de kalır.
ÖNCELİK      dikey kapak yerleşimi, başlık boyu ve kırpma provası için BU KILAVUZ geçerlidir;
             MUZIK_VE_KAPAK §2.3'ün y 500–1400 bandı · ≥154 px büyük harf · "düz bant, gradyan değil"
             satırları dikeyde bunun yerine geçer (iki satır 154 px, 720 × 210 başlık kutusuna sığmaz).
DEĞİŞMEYEN   ① kapak GN'den türer (sahip kuralı 19.09.2026 · DERS 30): VARSAYILAN, G<N> karesinin kendisi +
               başlık katmanı. §7 Prompt A (yeniden kompozisyon) yalnız GN çekirdek testinden geçmezse;
               o zaman da zincir_kontrol GN ↔ kapak koşulur — POOL ROOM'da ayrı üretilen kapak başka dünya
               oldu (alçak kamera, gündüz, fazladan saksılar · DERS 85).
             ② kapak her filmin SONUNDA kart olarak da vardır (sahip kuralı 16.10.2026) → YouTube Shorts'ta
               kapak "videodan kare seç" ile o karttan seçilir (§8 · K3); ayrı açılış afişi YOK.
             ③ öncesi/sonrası bölme YOK (sahip 19.09.2026) · sağ alt köşe boş (MUZIK_VE_KAPAK §4.2) ·
               renk: kanal paleti beyaz #E8E4DC (KANAL_KIMLIGI) — §5'teki palet örnektir.
PLANA İNEN   GN kompozisyonu kapak çekirdeğine göre kurulur (kadraj tablosunda "% alttan"):
             ana yapı + dönüşüm izi y %29–58 · x %14–86  ← §3 ana yapı kutusu (y 800–1360 px)
             başlık için SAKİN alan y %60–71 · x %17–83  ← §3 başlık kutusu (y 560–770 px)
             ⭐ 25.10.2026: bu kutu artık üç bandın biri (Ü). O (%45–55) ve A (%35–45) bantları, ışık varyantı ve
             başlık stili → KAPAK_STIL_KILAVUZU.md · sahip kuralı: başlık en üstte/en altta OLMAZ.
             KILAVUZ_REHBERI §2.1 kapak kuralı · plan KADRAJ KİLİTLERİ'ne "kapak çekirdeği" satırı.
ARAÇ         python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 merkez kırpmaları + 140 px
             küçükler + şablonlu kopya + PROVA_PANOSU.png · şablon: kilavuzlar/KAPAK_SAFE_AREA_1080x1920.png
             (§11'in tarifiyle ajan üretti; kılavuzla gelen dosya yoktu).
ÖLÇÜLDÜ      POOL ROOM kapağı (16.10.2026): başlık y ≈ 150–460 px — çekirdeğin ÜSTÜNDE; 4:5'te "THIS WAS"
             kesildi, 1:1'de yalnız "A POOL" kaldı [DERS 94]. Bu kılavuzun §3 kutusu bunu önlerdi.
             RAIN TOWER kapağı (17.10.2026): kutu PLANDA vardı, ama G8'de kule 1,5× uzun çıktı (tepe y ≈ 444, plan
             800) → başlık y ≈ 290–465'e kaydı, 4:5'te yarım, 1:1'de yok [DERS 99]. kapak_prova G8 ONAYINDAN önce,
             metinsiz G8'e koşulur.
```

## 1. Senin sorunun ve uygulanacak çözüm

Dikey kapağın tamamının profil önizlemesinde görünmemesi, çoğu durumda dosyanın bozulması değil, aynı görselin farklı oranlı bir kutuya sığdırılmasıdır. Tam ekran oynatma, profil ızgarası, akış önizlemesi ve paylaşım kartı aynı yüzey değildir. Kırpma ile videonun üzerine gelen düğme/yazıları ayrı kontrol et.

**Kullanacağımız sistem:**
- Ana dosya: **1080 × 1920 px / 9:16**.
- Başlık ve ana nesnenin tamamı: ortadaki **780 × 840 px** içinde.
- Bu merkez kutusu: **x = 150–930, y = 540–1380**.
- Üst ve alt kenarlar: gökyüzü, duvar, doku, karanlık alan gibi kaybı önemsiz arka plan.
- Film adı: İngilizce, büyük, tercihen 2–3 kelime; en çok iki satır.
- Kritik ayrıntı: başlığın altında, gözle hemen seçilecek büyüklükte.
- Yazıyı görüntü üretiminden sonra ayrı katmanda ekle.
- Son kontrol: gerçek Instagram kapak/profil önizlemesi + 3:4, 4:5 ve 1:1 kırpma provaları.

**Bu kutu benim korumacı tasarım önerimdir; Instagram'ın resmî, sabit veya bütün cihazları kapsayan safe-area ölçüsü değildir.** Aşağıdaki provalar merkezden kırpma varsayımıyla hesaplanmıştır. Önizleme kaydırılır veya yakınlaştırılırsa yeniden kontrol gerekir. Açılmış açıklama paneli gibi büyük arayüz katmanlarının altından her öğeyi kurtaran tek bir alan yoktur.

Amaç, tam ekran fotoğrafın her pikselini her yerde göstermek değil, **film adını, ana yapıyı ve dönüşümün ayırt edici ayrıntısını birlikte korumaktır.**

## 2. Güncel platform bilgisini doğru yorumla

Instagram'ın uzun profil ızgarasına geçişi Mosseri'nin resmî duyurusunda yer alıyor. Ayrıca 3:4 fotoğraf yükleme desteği ayrı bir duyuru olarak açıklandı. **Fotoğraf yükleme oranı ile Reels kapağının her yüzeydeki kırpılması aynı kural değildir.** [K1, K2]

Bu nedenle bu kılavuz “2026'da bütün hesaplarda kapak kesin şu oranla görünür” demez. 3:4'ü uzun profil önizlemesi için bir tasarım provası, 4:5 ve 1:1'i daha sıkı kırpma kontrolleri olarak kullanır. Bunlar birer test penceresidir; her birinin bütün hesaplarda fiilen gösterildiği iddiası değildir.

YouTube, Shorts kapağı için videodan kare seçimini mobil YouTube uygulamasında sunuyor; resmî yardım sayfası yüklemeden önce ve sonra düzenlemeyi anlatıyor. Studio ile mobil uygulamayı karıştırma. [K3]

TikTok'un yardım metni, kapak seçimini profil ve arama önizlemeleriyle ilişkilendiriyor. Hesabında ayrı resim yükleme seçeneği bulunduğunu varsayma; mevcut kapak seçicisini kontrol et. [K4]

TikTok'un reklam belgelerinde de safe area'nın açıklama ve yerleşime göre değiştiği belirtiliyor. **Reklam şablonlarını organik Reels/TikTok kapağı için evrensel bir piksel sınırı olarak kullanmıyoruz.** [K5]

## 3. Kesin ölçüler: merkezden kırpma hesabı

Koordinat başlangıcı görselin sol üst köşesidir. x sağa, y aşağıya büyür. 1080 × 1920 tuvalin merkezi **(540, 960)**.

| Test penceresi | Görünen alan | Ana dosyada x aralığı | Ana dosyada y aralığı | Üstten/alttan kayıp |
|---|---:|---:|---:|---:|
| Tam 9:16 | 1080 × 1920 | 0–1080 | 0–1920 | 0 / 0 |
| 3:4 prova | 1080 × 1440 | 0–1080 | 240–1680 | 240 / 240 |
| 4:5 prova | 1080 × 1350 | 0–1080 | 285–1635 | 285 / 285 |
| 1:1 prova | 1080 × 1080 | 0–1080 | 420–1500 | 420 / 420 |
| Önerilen içerik çekirdeği | **780 × 840** | **150–930** | **540–1380** | Tasarım payı |

Bu hesaplar, kaynak genişliği korunarak ve görüntü tam ortadan alınarak elde edilir. Örneğin 3:4 için yükseklik 1080 × 4 / 3 = 1440; üst pay (1920 − 1440) / 2 = 240 pikseldir.

**İçerik çekirdeği, merkezdeki kare kırpmanın içinde de kalır.** Kare kutusuna göre üstte/altta 120, kaynak kenarlarına göre solda/sağda 150 piksel pay bırakır. Bu paylar tasarım tamponudur; uygulama arayüzünün ölçümü değildir.

### Önerilen katman yerleşimi

| Katman | x | y | Genişlik × yükseklik | Görev |
|---|---:|---:|---:|---|
| Arka plan | 0 | 0 | 1080 × 1920 | Görsel atmosfer; bütün tuvali doldurur. |
| İçerik çekirdeği | 150 | 540 | 780 × 840 | Başlık + ana nesne burada kalır. |
| Film adı kutusu | 180 | 560 | 720 × 210 | 1–2 satır; resmin kritik ayrıntısını kapatmaz. |
| Ana yapı / dönüşüm | 150 | 800 | 780 × 560 | Ana nesnenin tanınması için gereken tamamı. |
| Yardımcı doku | Serbest | Serbest | Serbest | Kırpılınca hikâyeyi eksiltmeyen çevre. |

Film adı için ayrılan kutu, harfleri bu boyuta zorla esnetmek anlamına gelmez. Yazı gerçek sınırlarıyla ölçülür. Ana nesnenin uçları kutu dışına taşıyorsa nesneyi orantılı küçült veya yerleşimi yeniden kur.

Bir kule gibi çok uzun yapıda, tam silueti korumak için başlık kutusunun bir bölümünü görsele ayırabilirsin. Başlık ve yapıyı yine içerik çekirdeğinin içinde tut. Bu şema tek tip fotoğraf üretme zorunluluğu değildir.

## 4. Dikkat çekici timelapse kapağının görsel fikri

İzleyici küçük önizlemede üç şeyi anlayabilsin:

1. **Neye bakıyorum?** Havuz, değirmen, asansör, istasyon, köprü.
2. **Buradaki sıra dışı şey ne?** Havuzun içinde salon, uçurumda kırmızı kabin, denizin ortasında çalışan çark.
3. **Bu videoda hangi dönüşümü göreceğim?** Eski biçimini hâlâ belli eden, kullanıma geçmiş bir yapı.

İyi başlangıç düzeni: **tek ana yapı + eski kimliğinden kalan bir iz + büyük film adı.** Bu bir tasarım tercihi; virallik garantisi veya algoritma kuralı değildir.

### Timelapse için üç kapak yaklaşımı

| Yaklaşım | Ne gösterir? | Ne zaman seçilir? |
|---|---|---|
| Bitmiş yapı + eski iz | Yeni salon ve eski mavi havuz bordürü | Dönüşüm sonucunun kendisi güçlü olduğunda |
| Tamamlanmak üzere olan büyük iş | Yuvaya yaklaşan kubbe veya yerine gelen kabin | Tek bakışta anlaşılır büyük bir fiziksel iş varsa |
| Çalışan sonuç | Dönen çark, aydınlanan istasyon, kullanılan oda | İşlevin görüntüde okunması mümkünse |

Ana önerim ilk veya üçüncü yaklaşım. Final zaten güçlü ise onu kullan; sırf kapak için filmde olmayan bir yapı, mekanizma veya karakter ekleme. Bütün filmlere aynı “önce / sonra” bölmesini uygulamak zorunda değilsin.

### Örnek fikirler

| Film adı | Ana görüntü | Korunacak iz |
|---|---|---|
| THE POOL ROOM | Havuz çanağının içindeki sıcak salon | Mavi havuz bordürü ve eski basamaklar |
| THE CLIFF LIFT | Uçurum boyunca yükselen tek kırmızı kabin | Eski ray hattı ve kayalık |
| THE SEA MILL | Deniz ortasındaki taş yapı ve büyük çark | Su çizgisi ve eski taş temel |

Bunlar kapak yerleşimi örnekleridir; mevcut filmlerinin son durumuna ilişkin bir inceleme değildir.

**Küçük bir ayrıntıya bütün kapağı bağlama.** Camın altındaki ince bir çizgi yalnız tam ekranda görünüyorsa ana kanca olamaz. Ana dönüşüm önce okunur; o ayrıntı ikinci bakışta keşfedilir.

## 5. Tipografi, renk ve büyüklük

- Film adını tek ana metin yap. Uzun açıklama, “AI CINEMATIC TIMELAPSE”, bölüm tarihi ve üç farklı sloganı aynı kapağa yığma.
- Kısa adlarda bir satır, daha uzun adlarda iki satır kullan. Örneğin **THE POOL / ROOM**.
- 1080 genişlikte başlangıç denemesi: bir satırda yaklaşık 120–150 px; iki satırda yaklaşık 92–104 px yazı boyutu. Bunlar fonta göre değişir; gerçek yazı sınırları 720 × 210 kutuyu aşmasın.
- Kalın veya yarı kalın, sade bir yazı karakteri kullan. Çok ince çizgiler, aşırı geniş harf aralığı ve gösterişli dokular küçük önizlemede zayıflayabilir.
- Yazının altına ölçülü koyu geçiş koy. Tüm görseli siyaha gömmek yerine başlığın arkasındaki alanı sadeleştir.
- Örnek palet: koyu lacivert **#101820**, kırık beyaz **#F6F0E5**, tek vurgu rengi **#F0AA45**. Filmde baskın mavi veya kırmızı varsa vurguyu o renge göre değiştir.
- Ana yapı arka plandan ton veya renk olarak ayrışsın. Karanlık poster de okunur yüzeyler ve belirgin kenarlar ister.
- Kanal adı veya logo kullanılacaksa ikincil ölçekte kalsın; ana filmin adını küçültmesin.
- Kapağın İngilizce olması, açıklamanın da görselin içine yazılması anlamına gelmez. Açıklama platformun metin alanına gider.

**120–160 piksel genişlik testi:** Kapağı küçük göster. Film adı okunmuyor veya yapı seçilmiyorsa yazıyı büyüt, kelimeyi azalt, arka planı sadeleştir. Bu bir tasarım testi; belirli bir platformun sabit hücre ölçüsü değildir.

## 6. Elindeki yatay kapağı nasıl kurtarırsın?

Örneğin kaynak 1280 × 720, yani 16:9 olsun. Dikey alanı “doldur” komutuyla kaplatırsan iki yandan büyük kayıp olur. Tam yüksekliği koruyan merkez kırpmasında kaynağın yaklaşık **405 piksellik orta bölümü** kalır; yatay genişliğin yaklaşık **%31,6'sı** görünür.

Bu nedenle sorun yalnız dosya adını değiştirmek veya çözünürlüğü yükseltmekle çözülmez. Yeni çalışma tuvali gerçekten dikey olmalı.

### A. Tam kompozisyonu koruyan hızlı yöntem

1. 1080 × 1920 yeni tuval aç.
2. Kaynak resmi orantılı küçült; 780 piksel genişlikte 16:9 resim yaklaşık **780 × 439 px** olur.
3. Bu resmi ana görüntü alanına, örneğin **x = 150, y = 850** konumuna koy. Sağ sınır 930, alt sınır yaklaşık 1289 olur.
4. Üst ve alt alanları görselle uyumlu karanlık doku, yumuşak renk geçişi veya kontrollü arka plan uzatmasıyla tamamla.
5. Film adını üstteki merkez başlık kutusuna ayrı katmanda yerleştir.
6. Bütün kapağı küçük önizlemede kontrol et.

Ana resim ön planda keskin kalır. Arka plan uzatması veya bulanık kopya, ikinci bir bina ya da ikinci bir karakter gibi algılanmamalı. Keskin bir çerçeve istemiyorsan kenarları yumuşak geçişle bütünleştir.

### B. Daha güçlü, özel dikey düzen

Kaynak görseli referans al; ana yapıyı merkezde ve bütünü görünür olacak biçimde yeni dikey kompozisyonda yeniden düzenle. Arka planı üst ve alta uzat. Yeni çekim açısının filmdeki gerçek yapıyla çelişmemesine dikkat et.

Yazısı resme gömülmüş bir kaynakta metin ayrıca sorun çıkarır. Varsa yazısız sürümü kullan; film adını düzenleyicide yeniden ekle. AI'dan bütün harfleri koruyarak kusursuz piksel yerleşimi bekleme.

**1280 × 720 dosyayı aynı oranla bırakıp içine küçük bir dikey afiş koymak, dosyayı dikey yapmaz.** Çıkış dosyasının boyutunu da 1080 × 1920 yap.

## 7. Görsel üretimi ve yazı ekleme iş akışı

1. Filmden kapakta kullanılacak gerçek sonucu veya onaylı G karesini seç.
2. Ana yapıyı ve onu eski hâline bağlayan ayrıntıyı belirle.
3. 9:16 kompozisyonu yazısız üret ya da referansı düzenle.
4. Düzenleyicide 1080 × 1920 tuval oluştur; resmi esnetmeden yerleştir.
5. Ekteki **KAPAK_SAFE_AREA_1080x1920.png** dosyasını en üst katmana ekle. x = 0, y = 0; boyut tam 1080 × 1920. Katmanı kilitle.
6. Film adını ayrı metin katmanıyla ekle. Ana görsel ve metni merkez kutusuna göre ayarla.
7. Şablon katmanını kapat; temiz kapağı dışa aktar.
8. Kırpma provalarını ve uygulama içi gerçek önizlemeyi kontrol et.

Şablonun renkli çizgileri ve etiketleri yalnız çalışma kılavuzudur; yayımlanacak kapağın parçası değildir.

### Prompt A — Onaylı final karesinden dikey kapak

Onaylı final karesini referans olarak yükle. Köşeli parantezleri doldur.

~~~text
Use the attached approved final frame as the source of truth for the architecture, materials, colors, and completed transformation.

Create a clean vertical 9:16 cover image for the timelapse film [FILM TITLE]. Preserve [MAIN STRUCTURE] and its recognizable original feature [OLD IDENTITY DETAIL]. The visual promise is [ONE SENTENCE DESCRIBING THE REAL TRANSFORMATION].

Compose the complete recognizable main structure in the central part of the image. Reserve a calm, dark area immediately above it for a large two-line title to be added later. On a planned 1080 by 1920 canvas, the title and the essential subject will be placed inside the central box from x 150 to 930 and y 540 to 1380. Treat these coordinates as composition guidance, not printed content.

The upper and lower extensions contain only expendable environment: matching wall, sky, atmosphere, or restrained texture. Maintain clear subject edges, readable shadows, realistic materials, and one strong focal point. Preserve the film's actual design and scale.

Deliver the artwork without typography, logos, watermarks, frames, collages, or before-and-after panels. Do not introduce a result that does not appear in the film.
~~~

**Not:** Prompttaki koordinatlar niyeti anlatır. Gerçek piksel uyumu, düzenleyicide şablon katmanı ile yapılır.

### Prompt B — Yatay kapağın tamamını koruyarak dikeye yerleştirme

Yatay kapağın mümkünse yazısız sürümünü yükle.

~~~text
Use the attached landscape artwork as the exact visual reference. Create a new vertical 9:16 canvas while keeping the entire recognizable foreground composition intact and proportionally scaled.

Place the complete main artwork centrally, with every essential object visible. In the final 1080 by 1920 layout, the main image will occupy approximately x 150 to 930 and y 850 to 1290. Reserve the central area above it for a title added in editing.

Extend a subdued matching environment into the upper and lower canvas. Blend the surroundings softly into the central artwork. Keep the main subject sharp and dominant; background extensions must remain quiet and must not create duplicate buildings, people, or machinery.

Preserve original proportions, identities, architecture, and materials. Provide a clean image with no generated lettering, added symbols, logo, decorative border, or watermark. The final file must be portrait 9:16, not a landscape file containing a small portrait inset.
~~~

### Prompt C — Kapağı eleştirmek için kontrol promptu

Kapak görselini ve mümkünse Instagram'ın gerçek profil önizlemesini birlikte yükle.

~~~text
Review this vertical timelapse cover for readability, truthful visual promise, and cropping resilience.

Identify the actual canvas dimensions if available. Do not invent pixel measurements from an unknown-size screenshot. Evaluate centered 3:4, 4:5, and 1:1 crop simulations separately from interface overlays.

Check whether the full film title, the recognizable main structure, and the single transformation detail remain visible. If the supplied screenshot shows the real app interface, use that screenshot as stronger evidence than a generic safe-area template.

Evaluate the cover at a small thumbnail scale. Report the three most consequential problems, with the affected element, its location, the viewing surface, and one specific fix. Distinguish confirmed cropping from possible risks.

Do not predict guaranteed views, invent a click-through rate, or add objects that are absent from the film. Finish with a concrete revised placement recommendation.
~~~

## 8. Platforma göre uygulama

### Instagram Reels

- Dikey video için hazırladığın kapak dosyasını kullan. Yükleme akışındaki kapak seçimini ve varsa galeriden kapak ekleme seçeneğini kontrol et.
- Hesabında görünen “Kapağı düzenle / Edit cover” ve “Profil ızgarası / Adjust preview” benzeri kontroller varsa kapak seçimi ile profil kırpmasını ayrı ayrı ayarla. İsimler ve erişim sürüme göre farklı olabilir.
- Kapağı tam ekran görmek yeterli değil; profil önizlemesindeki film adını ve ana yapının uçlarını kontrol et.
- Otomatik yakınlaştırma veya “doldur” tercihi varsa bunun nesnenin uçlarını kesip kesmediğine bak. Kaydırma yaparsan merkezli prova hesabını yeniden değerlendir.
- Yayımlanmış gönderide düzenleme seçeneği mevcutsa onu kullan. Seçenek görünmüyorsa sırf bu kılavuzda adı geçti diye var kabul etme.
- Kapak, video açıldığında her zaman sabit bir ilk kare gibi gösterilmez. Videonun ilk hareketi kendi başına dikkat çekici olmalı.

### TikTok

- Kapak seçicinin sunduğu video karesini ve varsa metin seçeneklerini kullan. Ayrı fotoğraf yükleyebildiğini varsayma.
- Profil ve arama önizlemesinde görünen alan ile oynatma arayüzünü ayrı kontrol et.
- Kanalın görsel tutarlılığını film adı, yazı boyutu ve merkez yerleşimle kur. Görüntüyü sırf aynı renk olsun diye gereğinden fazla karartma.

### YouTube Shorts

- Mobil YouTube uygulamasında videodan kapak karesi seç; resmî yardım akışı yükleme sonrasında düzenlemeyi de anlatıyor. [K3]
- Bağımsız JPG'yi normal uzun video kapağı gibi yükleyebileceğini varsayma.
- Kapağa uygun bir final karesi videonun içinde gerçekten bulunsun. Yalnız kapak seçmek için açılışa uzun ve hareketsiz bir afiş ekleme.
- Kapak düzeni ile Shorts akışındaki ilk saniyeyi ayrı tasarla: seçilen kapak, videonun başlangıç hareketinin yerine geçmez.

## 9. Dışa aktarma ve kırpma provası

**Temiz kapak önerisi:** 1080 × 1920 px, sRGB, JPG; başlangıç kalite aralığı yaklaşık %88–95. Metin kenarları bozuluyorsa daha yüksek kalite veya uygun iş akışında PNG dene. **2 MB altı** taşınabilir bir çalışma hedefidir; burada bütün platformların zorunlu sınırı olarak sunulmuyor.

**Çalışma dosyası:** Katmanlı tasarım + yazısız ana görsel + ayrı kapak JPG'si. Şablon PNG'sini final resmine gömme.

### Prova sırası

1. Ana 9:16 görüntüyü tam boy kontrol et.
2. Merkezden 1080 × 1440 kırp: y = 240–1680.
3. Merkezden 1080 × 1350 kırp: y = 285–1635.
4. Merkezden 1080 × 1080 kırp: y = 420–1500.
5. Her sürümü 120–160 piksel genişlikte göster.
6. Uygulamanın gerçek kapak/profil önizlemesi ile karşılaştır.

Prova kırpmalarını ana kapak yerine yanlışlıkla yükleme. Bunlar kontrol dosyalarıdır. Orijinal kapak 9:16 kalır.

**Son karar üç soruyla verilir:**
- Film adını okuyabiliyor muyum?
- Ana yapının ne olduğunu anlıyor muyum?
- Dönüşümün sıra dışı tarafını açıklama olmadan seçebiliyor muyum?

Birinin yanıtı hayırsa yalnız yazıya daha fazla efekt ekleme. Öğelerin yerini veya büyüklüğünü değiştir.

## 10. “Viral” hedefini nasıl değerlendireceksin?

Kapak, profile veya seçilebilir bir önizlemeye bakan kişinin dikkatini çekebilir. Otomatik oynayan kısa video akışında ilk hareket ve hikâyenin ilerleyişi ayrıca önem taşır. Bu yüzden kapağın iyi olması tek başına izlenme garantisi değildir.

İki alternatif tasarlayacaksan tek bir farkı değiştir: örneğin aynı görüntüde film adının satır düzeni ya da aynı adla seçilen ana kare. Başlık, video, müzik ve paylaşım saatini birlikte değiştirip sonucu yalnız kapağa bağlama.

Kendi hesabında sunulan analitikleri kullan. Kapak gösterimi/tıklaması ayrı ölçülmüyorsa toplam izlenmeden “kapak CTR” uydurma. Farklı günlerde yayımlanan iki videonun izlenme farkı tek başına kontrollü A/B testi değildir.

## 11. Son kontrol listesi

- [ ] Çıkış tuvali gerçekten 1080 × 1920 / 9:16.
- [ ] Film adı İngilizce ve doğru yazılmış.
- [ ] Başlık ile ana nesne x 150–930, y 540–1380 çekirdeğinde.
- [ ] Başlık en fazla iki satır; küçük önizlemede okunuyor.
- [ ] Ana yapının tanınması için gereken uçları kırpılmıyor.
- [ ] Eski kimlik izi veya dönüşüm detayı başlık altında kaybolmuyor.
- [ ] Kapaktaki sonuç filmde gerçekten var.
- [ ] 3:4, 4:5 ve 1:1 merkez provaları kontrol edildi.
- [ ] Gerçek profil önizlemesi ve oynatma arayüzü ayrı kontrol edildi.
- [ ] Şablon çizgileri final dışa aktarımında kapalı.
- [ ] JPG esnetilmemiş; renk ve yazı kenarları düzgün.
- [ ] Kapak iyi diye ilk video karesi hareketsiz bir afişe dönüştürülmedi.

## 12. Kaynaklar ve doğrulama sınırı

**Kontrol tarihi: 16 Ekim 2026.** Platform ürün bilgileri aşağıdaki birincil kaynaklardan; merkez kutusu, font boyutları, kırpma matematiği ve yaratıcı seçimler bu kılavuzun tasarım önerileridir.

- **[K1] Adam Mosseri, “Profile roadmap / tall grid”.** Uzun profil ızgarası duyurusu. Resmî hesabın arama indeksindeki metni erişilebildi; tam gönderi açılışı hız sınırına takıldı. https://www.threads.com/@mosseri/post/DFBmq7ySDvi
- **[K2] Adam Mosseri, “Instagram now supports 3:4 aspect ratio photos”.** Fotoğraf oranı desteği; Reels kapağı için evrensel kırpma ölçüsü değildir. Resmî hesabın arama indeksindeki metni erişilebildi; tam gönderi açılamadı. https://www.threads.com/@mosseri/post/DKOIbJkRNIb
- **[K3] YouTube Help, “Create YouTube Shorts”, “Select a thumbnail”.** Resmî sayfanın güncel tam metni açıldı. https://support.google.com/youtube/answer/10343433?hl=en
- **[K4] TikTok Support, “Editing, posting, and deleting / Adding a video cover”.** Resmî yardım sayfasının arama özeti erişilebildi; güncel yönlendirme tam metin erişimini engelledi. https://support.tiktok.com/en/using-tiktok/creating-videos/editing-posting-and-deleting
- **[K5] TikTok Ads, “TikTok Auction In-Feed Ads”, Safe Zone.** Reklam dokümanı; organik kapaklara aynı ölçüler dayatılmadı. https://ads.tiktok.com/resources/help/article/tiktok-auction-in-feed-ads?redirected=1

Instagram'ın “Reel size and aspect ratios” yardım sayfası erişim sınırı / oturum duvarı nedeniyle tam doğrulanamadı. Eski 420 × 654 kapak önerisini güncel, evrensel bir yükleme zorunluluğu olarak aktarmıyoruz. Kullanıcının gerçek kapak/profil önizlemesi, bu şablondan daha güçlü uygulama kanıtıdır.

**Ek dosya:** KAPAK_SAFE_AREA_1080x1920.png, şeffaf çalışma şablonu. Ortadaki yeşil alan önerilen çekirdektir; sarı alan başlık, mavi alan ana görsel yerleşimidir. Kesik çizgiler yalnız merkezden kırpma provalarını gösterir.

