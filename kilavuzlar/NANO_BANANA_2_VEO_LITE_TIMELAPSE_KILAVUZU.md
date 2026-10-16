# Nano Banana 2 + Veo 3.1 Lite ile timelapse üretim kılavuzu

**BUILDWAKE için · Türkçe uygulama notları / İngilizce üretim promptları**  
**Sürüm 1.0 · Resmî özellik kontrolü: 15 Ekim 2026**  
**Temel format:** Her klip 8 saniye. Aynı kamera zincirinde `G0 → G1 = V1`, `G1 → G2 = V2`.

Bu kılavuz ev yapımı, oda yenileme, büyük yapı restorasyonu ve çevre düzenleme filmleri için hazırlanmıştır. Görseller Nano Banana 2 ile oluşturulur; onaylanmış iki komşu görsel Veo'nun başlangıç ve bitiş kareleri olur. Anlatım Türkçe, doğrudan kullanılacak promptlar İngilizcedir.

Ürün özellikleri kaynak numaralarıyla belirtilmiştir. Kamera düzeni, iş bölümü, örnekler, kalite ölçütleri ve prompt şablonları bu iş akışı için önerilen üretim yöntemidir. Bu hazırlıkta modellerde gerçek görsel/video üretimi yapılmadı; promptların çıktıları deneme klipleriyle değerlendirilmelidir. Kılavuz bir mimari uygulama veya mühendislik projesi değildir.

## 1. Önce sistemi doğru kur

**Her G bir durumdur; her V iki durum arasındaki iştir.**

| Dosya | Anlamı | Kullanımı |
|---|---|---|
| G000 | İlk durum | V001'in başlangıç karesi |
| G001 | Birinci iş tamamlandıktan sonraki durum | V001'in bitişi ve V002'nin başlangıcı |
| G002 | İkinci iş tamamlandıktan sonraki durum | V002'nin bitişi ve V003'ün başlangıcı |
| V001 | G000'dan G001'e geçiş | 8 saniye |
| V002 | G001'den G002'ye geçiş | 8 saniye |

G001'i iki kullanım için ayrı ayrı üretme. **Aynı onaylı dosyayı** hem V001'in End alanına hem V002'nin Start alanına ver. Böylece iki klibin ortak hedefi aynı olur. Bu, model çıktılarının sınırda piksel piksel aynı olacağını garanti etmez; birleşimi yine gözle kontrol edeceğiz.

İlk uygulama sırası:

1. Tek oda veya tek dış cephe seç; kamerayı ve değişmeyecek mimariyi yaz.
2. G000, G001, G002 ve G003'ün hangi durumları göstereceğini belirle.
3. G000'ı metinden üret ve onayla.
4. G001'i G000'ın düzenlemesi, G002'yi G001'in düzenlemesi olarak oluştur. Aynı yöntemi G003'e uygula.
5. Görseller arasında pencere, duvar, ufuk ve perspektif kayması bulunmadığını kontrol et.
6. Üç ayrı 8 saniyelik video üret: V001, V002, V003.
7. Bunları kesmeyle birleştir; toplam 24 saniyeyi görüntü ve ses açısından izle.
8. Sistem çalışıyorsa sonraki üretim bloklarına geç. Çalışmıyorsa ilk sorunun kaynağını düzelt; 150 klibi aynı hatayla üretme.

## 2. Model ve arayüz ayrımı

Bu kılavuzdaki **Veo Lite**, Google'ın **Veo 3.1 Lite** modelidir. Başka bir hizmetin aynı adla sunduğu ürünün ayarları farklı olabilir.

| Araç / özellik | Doğrulanan durum | Bu kılavuzdaki kullanım |
|---|---|---|
| Nano Banana 2 | Gemini 3.1 Flash Image; güncel model kodu `gemini-3.1-flash-image` [K1–K2] | G görsellerini üretme ve referanslı düzenleme |
| Nano Banana 2.1 | Google belgelerinde ayrı güncellenmiş sürüm olarak listeleniyor [K2] | Arayüzde bu isim varsa sürümü kaydet; aynı proje içinde fark etmeden model değiştirme |
| Nano Banana 2 Lite | Ayrı bir görsel modeli; Nano Banana 2 ile aynı model değil [K2] | İsimdeki Lite nedeniyle yanlışlıkla seçme |
| Flow / Veo 3.1 Lite | First and last frames; yatay ve dikey; 8 saniye destekleniyor [K3] | Ana önerilen kullanıcı arayüzü |
| Gemini API / Veo 3.1 Lite | `image` + `lastFrame` destekleniyor [K5] | API kullananlar için aynı iki kare mantığı |
| Veo Lite çıkış | 720p veya 1080p; 1080p için 8 saniye; 24 fps [K5–K6] | Deneme 720p, final tercihen 1080p |
| Veo Lite 4K | Yerel 4K üretim desteklenmiyor [K6] | Sonradan büyütülmüş dosyayı yerel 4K üretim diye sunma |

**Flow ve API belgelerini birbirinin yerine kullanma.** Kontrol tarihinde Flow, Lite için Ingredients/References ve Extend özelliklerini listeliyor. Gemini API tablosu ise Lite için `referenceImages` ve video uzatmayı desteklenmiyor olarak gösteriyor. Bu kılavuz iki yüzeyde de doğrulanan **başlangıç–bitiş karesi** yöntemine dayanır. [K3, K5]

Nano Banana'daki görsel referansı, Veo'daki Start/End alanları ve Veo Ingredients modu farklı işler yapar. İki resmi Ingredients alanına yüklemek, bunları başlangıç ve bitiş karesi olarak atamak anlamına gelmez.

Flow'un güncel görsel model listesinde Nano Banana 2.1, 2 Lite ve Pro görünebilir. Özellikle Nano Banana 2 ile çalışacaksan onu gerçekten sunan arayüzü veya ilgili API modelini kullan; indirdiğin G görsellerini Flow'a yükleyebilirsin. Bu kılavuz Nano Banana 2 ile 2 Lite'ı eşdeğer kabul etmez. [K2–K3]

## 3. Süre ve görsel sayısı hesabı

Tek kesintisiz zincirde:

`Klip sayısı N = toplam saniye / 8`  
`Görsel sayısı = N + 1`

| Film süresi | 8 saniyelik klip | Tek zincirde G sayısı |
|---|---:|---:|
| 56 saniye | 7 | 8 |
| 2 dakika | 15 | 16 |
| 2 dakika 40 saniye | 20 | 21 |
| 10 dakika | 75 | 76 |
| 12 dakika | 90 | 91 |
| 20 dakika | 150 | 151 |

**Oda değişince hesap değişir.** Her bağımsız kamera zincirinin kendi başlangıç görseli gerekir. B adet ayrı zincirde toplam N klip varsa ve zincirler başlangıç görsellerini paylaşmıyorsa:

`Toplam G sayısı = N + B`

Örneğin 10 ayrı zincir × 15 klip = 150 klip = 20 dakika. Her zincir 16 görsel ister; toplam **160 onaylı uç kare** gerekir. Deneme varyasyonları, yerleşim referansları ve kapak bunun dışındadır.

Filmi 8 saniyelik kliplerle tam 20 dakika teslim edeceksen başa logo, sona afiş ekleyip süreyi fark etmeden uzatma. Görüntü bindirmeli geçişler de toplamı kısaltabilir. Süreyi son kurgu zaman çizelgesinden doğrula.

## 4. Oda değişiminde zinciri doğru kes

Salonun son karesini mutfağın başlangıç karesiyle tek video içinde bağlamak, modele bütün mimariyi değiştirmesini söylemek olur. Duvarlar eriyebilir, dolaplar koltuktan çıkabilir, kamera kendiliğinden yürüyebilir.

Her oda için ayrı adlandırma kullan:

| Zincir | Görseller | Klipler |
|---|---|---|
| A — dış cephe | `A_G000`, `A_G001`, … | `A_V001`, `A_V002`, … |
| B — salon | `B_G000`, `B_G001`, … | `B_V001`, `B_V002`, … |
| C — mutfak | `C_G000`, `C_G001`, … | `C_V001`, `C_V002`, … |

Kurgu, A'nın son videosundan B'nin ilk videosuna normal kesmeyle geçer. **`A_son_görsel → B_ilk_görsel` için ayrıca bir dönüşüm videosu üretme.** Bu kesme ek süre gerektirmez.

Odaların aynı eve ait olması için önceden ortak bir yerleşim planı oluştur. Bir planda soldaki kapı salona açılıyorsa karşı planda aynı bağlantı doğru yerde olmalı. Ortak tuğla, pencere doğraması, dış manzara, zemin yönü ve tavan yüksekliği bu bağın kanıtlarıdır.

Yeniden dış cepheye döndüğünde iç mekânda tamamlanmış işlerle çelişme. Örneğin içeride yeni camlar görünürken dışarıda pencereler hâlâ kırık olmamalı. Aynı kamera konumuna daha sonra dönsen bile aradaki büyük zaman atlaması yeni bir zincir olarak planlanabilir.

## 5. Konuyu ve ilk 32 saniyeyi üretime göre tasarla

Güçlü konu üç şeyi birlikte taşımalı: ilk karede anlaşılır bir sorun, belirgin bir fiziksel dönüşüm, kullanıma geçen bir sonuç. Oda oda yapılan bir evde her bölümün ayrı bir görsel kazanımı olsun.

G000 boş ve hareketsiz olmak zorunda değil. Kaldırılacak panel sapanlara bağlı, temizlik makinesi ilk şeridin başında, taşınacak dolap kapının yanında olabilir. İlk işin başlamasına uzun hazırlık gerekmesin.

Önerilen açılış ritmi bir kurgu tercihidir; model veya algoritma kuralı değildir:

| Klip | İşlev | Örnek |
|---|---|---|
| V001 — 0–8 sn | Ölçeği ve işi hemen göster | Yüklü vinç ilk paslı paneli kaldırır |
| V002 — 8–16 sn | Neyin dönüşeceğini açığa çıkar | Panelin altındaki büyük yapı görünür |
| V003 — 16–24 sn | İlk belirgin ilerlemeyi verir | Yüzey geniş şeritler halinde temizlenir |
| V004 — 24–32 sn | Sonraki işi merak ettirir | Yeni parçanın yerleşeceği boşluk ve hazır parça aynı karede görünür |

Bir önceki klipte bitmiş işi tekrar başlatma. G001 zaten temiz duvarı gösteriyorsa V002'de o duvarı tekrar temizletme.

Uzun filmde her 6–10 klip civarında belirgin bir ara sonuç planlamak yararlı bir başlangıç yaklaşımıdır. Tam sayı zorunluluğu yoktur. Bir kapı, bir zemin, bir mutfak adası, bir çalışan su öğesi gibi görünür kazanımlar kullan. Sonuca ulaşmak için gerçek görüntüde fark yaratmayan işlerle süre doldurma.

## 6. Üretimden önce sabitlenecek proje kartı

Her kamera zinciri için bu kartı doldur. Kamera değiştikçe yeni kart aç; aynı kartın değerlerini üretim sırasında keyfî değiştirme.

| Alan | Yazılacak bilgi |
|---|---|
| Proje ve zincir | Örn. `POOL_HOUSE / C_KITCHEN` |
| Kadraj | 16:9 veya 9:16; bütün uç karelerde aynı |
| Kamera yeri | Odanın hangi köşesi, hangi yöne bakıyor? |
| Kamera yüksekliği | Örn. 2,2 m; bütün zincirde sabit |
| Lens karakteri | Örn. 28 mm eşdeğer, düz çizgileri koruyan geniş açı |
| Görsel sabitler | Pencere sayısı, kapı yeri, kirişler, havuz kenarı, dağ silueti |
| Aydınlatma | Sabit yumuşak gündüz veya planlı, kademeli ışık değişimi |
| Malzemeler | Tuğla, doğrama, ahşap, taş ve metal renkleri |
| İşçi yaklaşımı | Az sayıda yetişkin, uzak/orta uzak ölçekte; sabit kıyafet dili |
| Malzeme giriş yolu | Kapı, rampa, açık çatı veya servis yolu |
| Sökülen malzeme alanı | Kadraj içinde bir köşe veya görünen taşıma güzergâhı |
| Son hedef | Bu zincirde bitirilecek tek alan |

**Lens ve metre değerleri bir tarif aracıdır; kesin kamera kalibrasyonu sağlamaz.** Asıl denetim, onaylı referanstaki çizgilerin ve yerleşimin korunmasıdır.

Mimari timelapse için derin netlik, okunur gölgeler ve sınırlı doku daha kullanışlıdır. Yoğun film greni, aşırı sığ alan derinliği ve karanlık köşeler küçük tutarsızlıkların kontrolünü zorlaştırabilir. Film görünümü isteniyorsa renk ve hafif gren son kurguda bütün filme uygulanabilir.

## 7. G görsellerini yazmadan önce durum tablosu oluştur

Her satır bir **bitiş durumunu** tarif etsin. Görsel promptuna uzun bir hareket listesi yazma; hareket V promptunda yer alacak.

| Alan | Örnek |
|---|---|
| Önceki durum | Çatıdaki dört panelin tamamı paslı |
| Tek ana değişim | Soldaki bir panel sökülmüş |
| Yeni durum | Soldaki açıklık görünür, diğer üç panel yerinde |
| Malzemenin konumu | Sökülen panel sol zemindeki paletin üzerinde |
| Aynı kalanlar | Taş duvar, beş pencere, vinç tabanı, kamera |
| Henüz olmaması gerekenler | Yeni çatı, cam cephe, aydınlatma |
| Videoda yapılacak iş | Vinç paneli açıklıktan kaldırıp palete indirir |

Bir klip için “duvar temizlensin, çatı değişsin, camlar takılsın, mobilya gelsin” yazmak fazla büyük bir değişimdir. Bu işleri ayrı G aralıklarına böl. Değişim kolayca görünmeli ama iki uç arasında fiziksel bir süreç kurulabilmeli.

“Yüzde 35 tamamlandı” yerine **hangi kısmın** tamamlandığını belirt: “Arka duvardaki dört dolabın soldaki ikisi kurulu, sağdaki ikisinin yeri boş.” Böylece kontrol edilebilir bir sonuç oluşur.

İş sırasını kurarken görünmeyen ortak işleri de düşün. Oda kaplamalarından önce gerekli altyapı; sabit dolaplardan önce bunların arkasına erişim; büyük parçaları içeri aldıktan sonra kapatılan açıklıklar. Tek bir oda bloğu bütün inşaat sürecinin teknik kaydı olmak zorunda değildir; hangi hazırlıkların daha önce yapıldığını durum kartında belirt.

## 8. Nano Banana 2: G000 metinden görsel üretimi

G000 bütün zincirin görsel temelidir. Önce iki veya üç aday arasından doğru mimariyi seçmek, sonraki karelerde yanlış bir pencereyi sürekli düzeltmekten daha verimlidir.

İlk üretimde kontrol et:

- İşin tamamı kadrajdan görülebiliyor mu?
- Malzemelerin giriş ve çıkışı için görünen bir yol var mı?
- Sonraki yapı elemanları ön plandaki bir duvarın arkasında kaybolacak mı?
- Dikey veya yatay kadraj, dönüşümü gerçekten gösterebiliyor mu?
- Model aynı cepheye gereksiz pencere, kiriş veya kapı eklemiş mi?

**Metinden görsel şablonu — köşeli parantezleri doldur:**

```text
Create one photorealistic architectural worksite photograph for the first
keyframe of a continuous construction timelapse. [16:9 landscape / 9:16 portrait].

LOCATION AND ARCHITECTURE:
[Describe one specific building or room, including the exact visible openings,
structural elements, materials, and background landmarks.]

CAMERA:
One fixed [28 mm equivalent rectilinear] camera at [position and height],
looking toward [direction]. Deep focus, straight architectural lines,
level roll, unchanged perspective across the planned sequence.

CURRENT STATE:
[Describe only what is already present at this first stage.]
The next operation is prepared: [visible tool, material, access route,
or supported load that makes the first action immediately understandable].

COMPOSITION:
Keep [main work area] clearly visible. Keep [access route] open.
Place stored materials at [specific location] and removed materials at
[specific location]. [Describe any workers, their scale and clothing.]

LIGHT AND FINISH:
[One consistent lighting condition]. Realistic material texture,
natural restrained color, readable shadows, documentary photography.

Produce one clean full-frame photograph. No collage, inset, diagram,
captions, added signage, branding, or decorative frame.
Do not include later-stage elements: [specific exclusions].
```

Görsel modelinin farklı oran ve çözünürlük seçenekleri bulunur; referanslı, çok turlu düzenleme de desteklenir. [K2] Bu proje için önerim **2K görseller ve sabit en-boy oranı**. Arayüzde “2K” seçmek otomatik olarak 1920×1080 dosya aldığın anlamına gelmez; indirilen boyutu kontrol et. Aynı zincirde farklı kırpma veya esnetme uygulama.

## 9. G001 ve sonrası: bağımsız üretim yerine referanslı düzenleme

G001'i yalnızca “aynı mutfak, zemin yapılmış” diye sıfırdan üretmek kamera ve mimariyi yeniden yorumlatır. **Önceki onaylı kareyi yükleyip sadece gerekli değişikliği yaptır.**

Önerilen referans rolleri:

1. **Image 1:** Bir önceki onaylı G; mevcut inşaat durumunun kaynağı.
2. **Image 2:** G000 veya aynı açıdaki onaylı mimari ana referans; yalnız sabit geometriyi denetlemek için.
3. Gerekliyse ayrıca malzeme/parça referansı; rolünü açıkça belirt.

Her kare için bütün referansları eklemek zorunda değilsin. İlk düzenlemelerde tek önceki kare yeterli olabilir. Birden çok referans kullanıyorsan farklı tamamlanma seviyeleri model için çelişki yaratmasın.

**Düzenleme şablonu:**

```text
Edit Image 1 to create the next construction-state keyframe.
Image 1 is authoritative for the current work progress and object placement.
[If attached: Image 2 is only the fixed architectural and camera reference.
Do not restore its earlier unfinished construction state.]

Make only this next-stage change:
[Describe one clearly visible physical change and its exact location.]

The resulting image must show:
[State the completed result of that change, including where materials,
tools, removed parts and workers now are.]

Preserve the exact framing, viewpoint, lens perspective, room proportions,
opening locations, structural geometry and all completed work from Image 1.
Preserve [list the most important visual anchors].
Keep [lighting and unchanged materials] consistent.

Do not add later-stage elements: [specific items].
Return one full-frame photograph in the same aspect ratio and composition.
```

Bu promptta bütün odanın tasarımını tekrar anlatma. Uzun bir yeniden tasarım tarifi, “sadece bir değişiklik” talebini zayıflatabilir.

Her birkaç onaylı karede ve büyük yapı değişiminden sonra G000/ana referans ile yan yana karşılaştır. Bu bir öneridir; katı bir tekrar sayısı yoktur. Kayma varsa yanlış kareden devam ederek hatayı büyütme.

### Önceden final görseli üretmek

Final konseptini erkenden denemek yararlıdır: konu gerçekten etkileyici mi, son kadraj okunuyor mu? Ancak bu görseli `LOOK_TARGET` olarak ayır. Ara G karelerine sürekli referans vermek mobilya, ışık ve bitmiş yüzeylerin erkenden gelmesine neden olabilir. Zincirin son onaylı karesi, ara aşamalarla gerçekten tutarlı hale getirildikten sonra final olur.

## 10. Veo Lite: başlangıç ve bitiş karesiyle üretim

Flow'da güncel temel yol: proje içindeki model seçicisinden Video ve Frames seç; Start alanına başlangıç görselini, End alanına bitiş görselini ekle. Metin alanına iki kare arasında yapılacak işi yaz; model, oran ve süreyi kontrol ederek üret. Arayüzün yerleşimi değişebilir. [K4]

| Ayar | V001 örneği |
|---|---|
| Model | Veo 3.1 Lite |
| Mod | Frames / First and last |
| Start frame | `A_G000_v01.png` |
| End frame | `A_G001_v01.png` |
| Duration | 8 seconds |
| Aspect ratio | Görsellerle aynı; uzun yatay filmde 16:9 |
| Resolution | Deneme 720p; arayüzde sunuluyorsa onaylı final için 1080p tercihi |
| Prompt | G000'dan G001'e ulaşmak için yapılan fiziksel iş |

V002'de Start=`A_G001_v01.png`, End=`A_G002_v01.png` olur. Yükledikten sonra küçük önizlemeleri kontrol et: start/end sırasını ters çevirmek sökülmüş parçayı geri getirebilir.

Yalnızca prompta “G0'dan G1'e git” yazmak yeterli değildir. Dosyalar gerçekten ilgili alanlara yüklenmelidir. Veo önceki klibin ne yaptığını dosya adından veya başka bir sohbetten öğrenmez.

### Ana video prompt şablonu

```text
Create one continuous 8-second documentary construction timelapse between
the supplied START FRAME and END FRAME. One locked-off camera throughout.

The start frame shows [current physical state].
The end frame shows [the next completed physical state].

ACTION:
[Workers or machinery] perform [one main task] at [precise location].
[Describe the visible physical method, material source, travel direction
and destination in a short, logical sequence.]
Work progresses in accelerated time and reaches the supplied end state.

CONTINUITY:
Keep the same framing, perspective, structural geometry, background,
lighting direction and all previously completed work.
Only [allowed changing elements] change.
Materials are carried, placed, removed or assembled through visible actions.
Rigid objects keep their shape. Existing architecture remains stable.

SOUND:
[Relevant work sounds] with a low continuous [room / outdoor] ambience.
No dialogue or music.

Single uninterrupted shot. No camera movement, reframing, cuts,
cross-dissolves, architectural morphing or spontaneous material appearance.
Match the supplied end state without adding another construction phase.
```

Promptu yaklaşık 120–200 İngilizce kelimelik, tek ana işi anlatan bir metin olarak tutmak pratik bir başlangıçtır. Bu aralık bir model şartı değildir. Detay eklemek gerekiyorsa önce hareketin neden belirsiz kaldığını belirle.

“No morphing” tek başına çözüm değildir. İki karede perspektif farklıysa veya bina bütünüyle değişmişse önce görselleri düzelt. Çok sayıda yasak yerine net bir fiziksel iş ve uyumlu uç kareler daha güçlü bir üretim temeli sağlar.

## 11. Sekiz saniyenin hareket düzeni

Önerilen ritim: iş ilk anda başlar; klibin çoğu görünür ilerlemeye ayrılır; son bölümde iş doğal biçimde hedef konumuna ulaşır. İlk iki saniyeyi boş bekleme, son iki saniyeyi donmuş görüntü yapma.

Saniye saniye koreografi yerine üç aşama kullan:

1. **Başlangıç:** İşçi, araç veya malzeme doğru konumda; iş hemen okunur.
2. **İlerleme:** Tek fiziksel değişim belirgin biçimde büyür.
3. **Son:** Sonuç G bitiş karesiyle uyumludur; başka bir iş başlamaz.

“Tam 3,25. saniyede kilit kapanacak” gibi hassas talimatları güvenilir üretim garantisi sayma. ⭐ Ölçüldü
(DERS 92 · THE POOL ROOM, 6/7 klip): ana dönüşüm 8 sn'lik klibin ilk 2–4 sn'sinde bitti; klip sonundaki teslimat
cümleleri ise tuttu. Ana işi 0–4'e, küçük ikinci işi 4–8'e koy. Kilit kapanması hikâyenin kanıtıysa daha kolay görünen bir sonuç seç: yükün desteğe oturması, kapının kapalı konumu veya tamamlanan yüzey.

İşçi hareketi hızlandırılmış olabilir; duvarların ve ağır parçaların biçimi kararlı kalmalıdır. Araçların duvardan geçmesi, dolabın zeminden büyümesi veya bütün malzemelerin tek anda belirmesi kabul edilebilir bir timelapse kısaltması değildir.

Veo videoyla birlikte ses üretir. [K5] Müziksiz prompt kullanmak tamamen sessiz bir dosya ayarı değildir. İstenmeyen konuşma veya müzik oluşursa ses katmanını kurguda ayırıp değiştir; görüntüyü sırf bu nedenle yeniden üretmek gerekmeyebilir.

## 12. Uygulamalı örnek: mutfakta G000–G006 / altı klip

Bu 48 saniyelik örnek, **zemin ve alt dolapların kurulumu** içindir. Tam bir mutfak inşaatını altı klibe sıkıştırmaz. Duvar onarımları, camlar ve gerekli kaba altyapı bu bölüm başlamadan tamamlanmıştır. Üst dolaplar, evyeler ve cihazlar daha sonraki zincir aşamalarına aittir.

Sabit mimari: dikdörtgen oda, arka duvarda tek geniş siyah çerçeveli pencere, sağ duvarda tek kapı açıklığı, sol duvarda bir tuğla şerit, üstte tek koyu kiriş. Kamera ön sol köşede, 2,2 m yüksekte, 28 mm eşdeğer geniş açı. Yumuşak gündüz ışığı bütün altı klipte aynı kalır.

| Görsel | Onaylanacak durum | Bir sonraki iş |
|---|---|---|
| G000 | Zemin çıplak beton; dolap yok | Arka yarıya ahşap zemin |
| G001 | Zeminin arka yarısı ahşap; ön yarı beton | Ön yarıyı tamamlamak |
| G002 | Ahşap zemin tamam; dolap yok | Soldaki iki alt dolap gövdesi |
| G003 | Arka duvarda soldaki iki dolap gövdesi var | Sağdaki iki gövde |
| G004 | Dört alt dolap gövdesi aynı hizada | Dört yeşil kapak |
| G005 | Dört yeşil kapak takılı; tezgâh yok | Ceviz tezgâh tablası |
| G006 | Tezgâh dört dolabın üstüne oturmuş | Bu örneğin sonu |

### 12.1 G000 — metinden ilk görsel

```text
Create one photorealistic documentary photograph of a kitchen renovation,
landscape 16:9. The room is rectangular, approximately 6 by 4.5 metres.
One wide black-framed window is centered on the rear wall. There is one
open doorway on the right wall, a vertical exposed red-brick strip on
the left wall, and one dark ceiling beam. The remaining walls are
finished in warm off-white plaster. Windows and rough-in services are
already complete. The dry concrete floor is still entirely uncovered.
There are no cabinets or countertops installed.

The camera is fixed in the front-left corner, 2.2 metres above the floor,
with a 28 mm equivalent rectilinear lens, deep focus and level roll.
The entire rear wall and most of the floor are visible.

Pale oak floorboards and unassembled cabinet materials are staged just
outside the visible right-hand doorway, leaving a clear access path.
Two adult installers wear navy workwear and yellow hard hats.
One is positioning the first oak board at the rear-left floor edge;
the other carries another board from the doorway. Faces are small.
Soft daylight enters through the rear window, with readable shadows.
Natural restrained color, crisp architectural detail.
One full-frame photograph, no inset, captions or added branding.
```

G000'daki dört mimari sabiti onayla: pencere, sağ kapı, sol tuğla şerit, üst kiriş. G001'e geçerken bu dosyayı yükle.

### 12.2 G001 — zeminin arka yarısı

**Yükle:** G000'ın onaylı sürümü.

```text
Edit the supplied photograph into the next renovation state.
Cover only the rear half of the concrete floor with pale oak floorboards,
progressing from the rear wall toward the camera. The boundary between
oak and exposed concrete is one straight line parallel to the rear wall.
The front half remains bare concrete. Both installers are working at
this boundary; their clothing remains unchanged.
Keep the exact camera view, window, doorway, left brick strip, ceiling
beam, wall finish and daylight. Keep the material staging outside the
right doorway. No cabinets, countertop or appliances yet.
Return one photograph with the same framing and aspect ratio.
```

### 12.3 G002 — zemin tamam

**Yükle:** G001'in onaylı sürümü.

```text
Edit the supplied photograph. Extend the existing pale oak floorboards
across the remaining front half of the room so the floor is fully laid.
Match the installed boards' width, direction, color and seam pattern.
Preserve the already completed rear floor. The installers are near
the right doorway, with the access path clear and surplus material
remaining outside. Keep all architecture, camera geometry and daylight
unchanged. There are still no installed cabinets, countertop or appliances.
Return one full-frame photograph in the same aspect ratio.
```

### 12.4 G003 — soldaki iki alt dolap

**Yükle:** G002'nin onaylı sürümü.

```text
Edit the supplied photograph. Add exactly two unfinished pale plywood
base-cabinet carcasses against the rear wall, occupying the left half
of the planned four-unit cabinet run below the window. Their tops are
level and their open fronts face the camera. The right half of the run
remains empty. The installers are beside the two placed units.
Preserve the completed oak floor, window, doorway, brick strip, beam,
camera view and lighting. Keep unused cabinet components outside the
right doorway. No door fronts, countertop or upper cabinets yet.
```

### 12.5 G004 — dört gövde tamam

**Yükle:** G003'ün onaylı sürümü.

```text
Edit the supplied photograph. Add two matching plywood base-cabinet
carcasses immediately to the right of the existing pair, completing
one straight run of exactly four equal-width units below the window.
Keep the original left pair unchanged. All four open fronts face the
camera and their tops align. Keep the installers near the right pair.
Preserve the floor, architecture, framing and daylight exactly.
There are no door fronts, countertop, upper cabinets or appliances yet.
Return one photograph with the same composition.
```

### 12.6 G005 — yeşil kapaklar

**Yükle:** G004'ün onaylı sürümü.

```text
Edit the supplied photograph. Fit one flat matte forest-green door
front to each of the four existing base-cabinet units. All four doors
are closed and aligned, each with the same small dark handle.
Keep the four cabinet boxes in exactly the same positions and sizes.
Their top remains unfinished because no countertop is installed yet.
The installers stand beside the cabinet run, without covering the doors.
Preserve all other objects, the oak floor, architecture, camera and
daylight. No upper cabinets, countertop, sink or appliances.
```

### 12.7 G006 — tezgâh tablası

**Yükle:** G005'in onaylı sürümü.

```text
Edit the supplied photograph. Add one continuous finished walnut
countertop resting horizontally on the four existing base cabinets.
It follows the full straight cabinet run below the window, with a
small even front overhang and square ends. Its surface is solid and
uninterrupted, with no sink or appliance cutouts. The two installers
stand at opposite ends, having just finished positioning it.
Preserve the exact green doors, cabinet dimensions, floor, room geometry,
camera and daylight. No additional furniture or decoration.
Return one full-frame photograph in the same aspect ratio.
```

### 12.8 Altı Veo klibi için yükleme tablosu

| Klip | Başlangıç | Bitiş | Süre | Tek ana iş |
|---|---|---|---:|---|
| V001 | G000 | G001 | 8 sn | Arka yarıya zemin |
| V002 | G001 | G002 | 8 sn | Ön yarıya zemin |
| V003 | G002 | G003 | 8 sn | İki dolap gövdesini yerleştirme |
| V004 | G003 | G004 | 8 sn | Kalan iki gövdeyi yerleştirme |
| V005 | G004 | G005 | 8 sn | Dört kapağı takma |
| V006 | G005 | G006 | 8 sn | Tezgâhı taşıyıp oturtma |

Aşağıdaki her İngilizce blok ayrı klibe aittir. İlgili iki resmi mutlaka Start ve End alanlarına yükle.

**V001:**

```text
One continuous 8-second locked-camera renovation timelapse between
the supplied start and end frames. The two adult installers in navy
workwear and yellow hard hats lay pale oak floorboards, starting at
the rear wall and advancing toward the center. Boards are carried
through the right doorway and physically placed in aligned rows.
Finish with only the rear half covered, matching the end frame;
the foreground remains bare concrete. Preserve the exact architecture,
camera, daylight and material appearance. Accelerated work, rigid
boards, stable walls. Wood placement and light tool sounds, no speech
or music. No cuts, zoom, dissolves, extra construction or morphing.
```

**V002:**

```text
Create an 8-second continuous fixed-camera construction timelapse.
Keep the existing rear-half oak flooring unchanged. The two installers
continue the same rows toward the foreground, carrying boards from
the right doorway until the remaining concrete floor is covered.
They finish near the doorway, matching the supplied end frame.
Preserve board direction, room geometry, framing and soft daylight.
Only flooring and worker positions change; no cabinets appear.
Natural wood and tool sounds with quiet room ambience, no speech
or music. No camera motion, cuts, dissolves or material morphing.
```

**V003:**

```text
One locked-off 8-second renovation timelapse from the supplied start
frame to the end frame. The two installers bring two plywood cabinet
carcasses through the right doorway on a small hand trolley, unload
them and position them side by side against the rear wall below the
left half of the window area. The trolley returns through the doorway.
Leave the right half of the cabinet run empty. Preserve the completed
floor and every architectural feature. Rigid cabinet shapes, visible
carrying and placement. Soft wheel and wood-contact sounds, no speech
or music. No camera movement, cuts, extra furniture or spontaneous assembly.
```

**V004:**

```text
Create one continuous 8-second locked-camera timelapse. Leave the two
existing left cabinets untouched. The installers bring two matching
carcasses through the right doorway and position them immediately
beside the first pair, completing a straight row of four units.
They align the new units to the existing height and withdraw the trolley
through the same doorway. Match the supplied end frame. Keep the room,
floor, camera and daylight stable. No door fronts or countertop yet.
Natural handling sounds, no speech or music. No cuts, zoom, dissolves,
stretching cabinets or changing architecture.
```

**V005:**

```text
One 8-second continuous locked-off renovation timelapse. The installers
bring the four finished forest-green cabinet doors from the right
doorway and fit them one by one to the four existing base units.
Each door is positioned physically, then closes into alignment.
End with all four doors closed and the countertop still absent,
matching the supplied end frame. Preserve cabinet geometry, the oak
floor, architecture, camera and daylight. Workers move in accelerated
time while the building stays rigid. Light tool and hinge sounds,
no speech or music. No cuts, camera movement or morphing.
```

**V006:**

```text
Create one continuous 8-second fixed-camera renovation timelapse.
The two installers bring one rigid walnut countertop through the
right doorway, support it at opposite ends, turn it to align with
the cabinet run and lower it onto the four existing base cabinets.
Finish with the slab resting level, matching the supplied end frame.
Preserve all cabinet doors, floorboards, architecture and daylight.
The countertop retains one constant shape and thickness throughout.
Soft footsteps, wood handling and a muted contact sound as it settles.
No speech or music. No camera movement, cuts, dissolves or added fixtures.
```

**Önemli:** Bu örnekte kamera tezgâhın kapıdan gelişini göremiyorsa hareketi promptla zorlamadan önce yerleşimi düzelt. Gövde büyüklüğü kapıya sığmıyorsa daha küçük, gerçekçi bir parça seç veya montajı iki aşamaya böl. Uç kareler arasındaki fiziksel geçiş, görsel kompozisyonun parçasıdır.

## 13. İş türüne göre hareket tarifleri

Aşağıdaki kısa blokları ana Veo şablonunun ACTION bölümüne ekle. Tamamını tek videoda kullanma.

| İş | Güçlü hareket tarifi | Uç karede aranacak kanıt |
|---|---|---|
| Temizlik | Kirin belirli bir taraftan ilerleyen şeritlerle kalkması | Temiz ve kirli alan sınırı |
| Söküm | Parçanın bağlantıdan ayrılıp belirli bir yere taşınması | Boş kalan yer ve sökülen parça |
| Vinç | Yüklü kanca, kısa kontrollü rota, açık iniş noktası | Yükün destek üstünde durması |
| Boya | Yüzeyde rulo geçişleriyle genişleyen yeni renk | Eski/yeni yüzey sınırı |
| Duvar örme | Aynı duvar hattında sıra sıra yükselen yapı | Pencere ve kapı boşlukları korunmuş yükseklik |
| Mobilya | Kapıdan taşınma, zemine indirme, son konuma alma | Aynı mobilyanın belirlenen yerde durması |
| Peyzaj | Toprak, kaplama ve bitkilerin ayrı işlerde yerleşmesi | Her klipte tek belirgin çevre değişimi |
| Su öğesi | Hazır ve tamamlanmış haznenin kontrollü dolması | Yeni yapılar belirmeden yükselen su seviyesi |

**Vinç için ACTION örneği:**

```text
The crane lifts the already rigged roof panel, moves it a short distance
to the left and lowers it onto the visible support rack. The lifting
cables remain attached and taut while the load is suspended. The crane
base and the remaining roof structure do not move.
```

**Temizlik için ACTION örneği:**

```text
Workers clean the stone facade in adjacent vertical passes from left
to right. Each pass exposes the same stone beneath the dirt. The window
openings and mortar pattern stay fixed, and runoff moves downward.
```

**Boya için ACTION örneği:**

```text
The workers apply warm off-white paint with rollers in overlapping
vertical passes. The new color spreads only where the rollers work.
Keep the wall shape, window frame, floor and ceiling unchanged.
```

**Mobilya için ACTION örneği:**

```text
Two workers carry the same assembled sofa through the visible double
door and lower it onto the marked seating area. The sofa keeps its
dimensions, upholstery and orientation as they place it.
```

Kaldırma, dönme ve hassas kilitleme aynı klipte zorlaşıyorsa parçayı başlangıçta hedefe daha yakın konumlandır. Örneğin bir sonraki G aralığı yalnız “son hizalama ve indirme” işi olabilir. Hikâyenin temel kanıtını görünmeyen küçük bağlantılara yükleme.

## 14. Kamera ve malzeme kaymasını azaltma

### Kamera kayması

İki G'yi art arda açıp pencere köşeleri, dikeyler ve ufuk çizgisine bak. Referans çizgileri hareket ediyorsa V üretmeden düzelt. Gerekirse bir görüntü düzenleyicide iki kareyi yarı saydam üst üste getir; bu kontrolü üretim görseline gömme.

“Locked camera” yazılmış olması yeterli değildir. Kamera sözde sabitken odanın eni değişiyorsa sorun uç karelerdedir. Kadrajı sonradan büyüterek her hatayı gizlemek görüntü kaybı yaratır ve nesne geometrisini onarmaz.

### Malzeme ve mimari kayması

Değişmeyecek öğeleri kısa bir liste halinde tut: `one rear window / one right doorway / left brick strip / one ceiling beam`. Listeyi hem düzenleme hem videoda gerektiği kadar tekrarla. Sabit olmayan inşaat parçalarını bu listeye yanlışlıkla ekleme.

### Referans zincirinin bozulması

Hatalı G014'ten G015 üretirsen G014'ün yanlış penceresi yeni normal haline gelebilir. Son doğru kareye dön, değişimi yeniden uygula ve sonraki bağımlı görselleri kontrol et.

Kare onaylandıktan sonra ayrı bir sürüm adıyla sakla. `G014_v02` düzeltmesi yapıldığında bu kareyi kullanan **V014 ve V015** yeniden değerlendirilmelidir. G015 ve sonrası G014_v01 üzerinden üretildiyse görsel zincir de etkilenmiş olabilir.

### Son video karesini otomatik olarak yeni G yapma

Veo'nun son çıktısını her seferinde yeni başlangıç yapmak, zincirdeki küçük deformasyonları biriktirebilir. Varsayılan kaynak **onaylı G dosyası** olsun. Çıktıdan alınan son kareyi kullanmak gerekiyorsa onu yeni bir görsel sürümü olarak incele, onayla ve bağımlılıkları güncelle; sessizce değiştirme.

## 15. Işık, hava ve zaman yönetimi

Bir oda zincirinde sabit yumuşak gündüz, üretimi daha kolay denetlenebilir hale getirir. Aynı G çiftinde hem büyük inşaat değişimi hem gündüzden geceye geçiş istemek daha fazla değişken yaratır.

Uzun film için iki açık seçenek var:

- **Bölüm başına sabit ışık:** Her oda kendi tutarlı ışığında tamamlanır. Bölümler arası kesmeler farklı çalışma zamanlarını temsil edebilir.
- **Planlı zaman ilerlemesi:** Sabah, öğle, akşam değişimi ayrı G durumlarıyla kademeli yürütülür. Büyük ışık geçişi sakin bir fiziksel iş sırasında yapılır.

Gerçekte haftalar sürecek yenilemeyi görsel zaman sıkıştırmasıyla anlatırken “bir günde gerçekten yapıldı” diye sunma. Aynı mantık hava için de geçerli: yağmurda ıslak zemin, bir sonraki karede açıklamasız şekilde kuru ve tertemiz olmamalı.

Örnek sabit ışık cümlesi:

```text
Soft overcast daylight from the same window direction, fixed white balance,
consistent exposure, readable shadows and no change in weather.
```

Akşam finali kullanılacaksa yapı ve mobilyalar karanlıkta kaybolmasın. İç aydınlatmaların ne zaman takıldığı ve açıldığı durum planında belli olsun.

## 16. Kalite kontrol: videoya para harcamadan önce

### G çiftini onaylama

| Kontrol | Kabul koşulu |
|---|---|
| Kamera | Aynı kadraj, perspektif ve ufuk |
| Mimari | Sabit pencere, kapı, kiriş ve duvar çizgileri korunmuş |
| İlerleme | Tamamlanmış iş geri alınmamış |
| Değişim | Tek ana iş açıkça görülebiliyor |
| Geçiş olasılığı | Nesne kadraja girebiliyor, yerine ulaşabiliyor |
| Malzeme | Gelen ve sökülen parçaların konumu açıklanabiliyor |
| Işık | İki karede uyumlu veya bilinçli planlanmış |
| Sonraki aşama | Mobilya, cam, ışık gibi öğeler erken gelmemiş |

⭐ **DERS 91 (THE POOL ROOM, ölçüldü):** her G, Veo'ya girmeden önce planın KARE TABLOSU ve IŞIK DEFTERİ satırıyla
karşılaştırılır (saat · ışık · sayım · "henüz olmaması gerekenler"). Gece istenen G8 gündüz üretildi ve kontrolsüz
bitiş karesi oldu → S7 son 2 sn'de lambalar söndü, saksılar belirdi. Işık karesi metinden değil, önceki onaylı
kareden düzenlemeyle üretilir.

### V klibini onaylama

1. Normal hızda izle: yapılan iş ilk bakışta anlaşılıyor mu?
2. Başlangıç, orta ve son bölümden kareler kontrol et: arada bükülme veya erime var mı?
3. Son görüntüyü hedef G ile karşılaştır: planlanan sonuç gerçekten geldi mi?
4. Sonraki kliple birleşimini izle: mimari sıçrama veya ışık çakması var mı?
5. Sesi kontrol et: görünmeyen çarpışma, konuşma, müzik veya ani ortam değişimi var mı?
6. Dosyanın gerçek süresini, çözünürlüğünü ve kare hızını kontrol et.

Kritik hata: duvarın kayması, işin tersine dönmesi, yükün şekil değiştirmesi, yanlış bitiş, pencere sayısının değişmesi. Bunları “hızlı geçiyor, görünmez” diye kabul etme. Küçük uzak işçi hareketindeki ayrıntıyı ise filmdeki önemiyle birlikte değerlendir.

## 17. Hata → neden → düzeltme tablosu

| Sorun | Olası neden | İlk düzeltme |
|---|---|---|
| Kamera yavaşça yaklaşır | G kareleri farklı ölçekli veya promptta sinematik hareket çağrısı var | Kareleri hizala; hareketli kamera ifadelerini kaldır |
| Salon mutfağa dönüşür | Farklı odalar aynı Start/End çiftinde | Ayrı zincir ve kurgu kesmesi |
| Yapı bir anda belirir | Uçlar arasında fazla iş var | Araya daha küçük durumlar koy; klip planını yeniden say |
| Duvar erir | Mimari uyuşmazlığı veya büyük malzeme değişimi | G'yi düzelt; işin fiziksel yöntemini belirt |
| Vinç yükü biçim değiştirir | Parça uçlarda farklı veya rota karmaşık | Parçayı eşleştir; hareket mesafesini kısalt |
| Zemin tekrar sökülür | Prompt önceki aşamayı tekrar anlatıyor | Başlangıç durumunu güncelle; tamamlanan bölümü koru |
| Mobilya camdan geçer | Giriş yolu görünmüyor veya mobilya sığmıyor | Kapı ve eşya ölçüsünü düzenle; uygun giriş planla |
| Gece finali okunmaz | Aşırı karanlık bitiş karesi | Gece G'sini okunur ışıkla düzelt |
| Kare birleşiminde sıçrama | Aynı adlı farklı G sürümleri veya çıktı sapması | İki klipte aynı dosyayı kullan; hatalı klibi yeniden üret |
| 8 saniyenin yarısı donuk | Fazla uzun final tutuşu veya iş çok küçük | Daha erken başlayan, klibe yayılan hareket yaz |
| Fazla eşya / kalabalık | Genel “busy construction site” gibi belirsiz tarif | Gerekli az sayıda araç, kişi ve parça tanımla |
| Sadece ses hatalı | Modelin ses üretimi uygunsuz | Ses katmanını kurguda değiştir |
| Her odada aynı hareket | Tek şablon bütün işlere kopyalanmış | Temizlik, taşıma, yüzey, montaj ve kullanım işlerini çeşitlendir |

Düzeltirken aynı anda model, kamera, ışık, kadraj ve promptu değiştirme. Önce en belirgin tek nedeni düzelt; sonucu karşılaştır. Aynı hatayı tekrar tekrar üretmek yerine uç kareleri veya işin kapsamını yeniden ele al.

## 18. Dosyalar, sürümler ve üretim kartı

Klasör adlarını kısa ve düzenli tut:

| Klasör | İçerik |
|---|---|
| `00_PLAN` | Konu, yerleşim, durum tablosu, kamera kartları |
| `01_REFERENCE` | Sabit mimari ve malzeme referansları |
| `02_KEYFRAMES/A_EXTERIOR` | A zincirinin onaylı G dosyaları |
| `02_KEYFRAMES/B_LIVING` | B zincirinin onaylı G dosyaları |
| `03_VIDEO` | Üretilen V klipleri ve alternatifleri |
| `04_AUDIO` | Ortam, iş sesleri ve varsa müzik |
| `05_EDIT` | Kurgu projesi ve çalışma çıktıları |
| `06_DELIVERY` | Yayımlanacak son dosyalar |

Örnek adlar:

```text
C_G000_v01.png
C_G001_v03.png
C_G002_v01.png
C_V001_G000v01_G001v03_take02.mp4
C_V002_G001v03_G002v01_take01.mp4
```

Kareyi yalnız “final.png” diye saklama. Hangi G sürümünden hangi videonun üretildiğini dosya adı veya üretim tablosu açıkça göstersin. Orijinal indirilen dosyayı koru; mesajlaşma uygulamasından tekrar indirilmiş, kırpılmış veya sıkıştırılmış kopyayı zincire sokma.

Her klip için bu kartı doldur:

```text
PROJECT:
GLOBAL_CLIP_NUMBER:
CHAIN_ID:
LOCAL_CLIP_ID:
DURATION: 8 seconds
ASPECT_RATIO:
MODEL_AND_INTERFACE:
RESOLUTION:
START_IMAGE_EXACT_FILENAME:
END_IMAGE_EXACT_FILENAME:
START_STATE:
SINGLE_MAIN_CHANGE:
PHYSICAL_ACTION:
MATERIAL_ENTRY_AND_EXIT:
FIXED_ARCHITECTURAL_ANCHORS:
LIGHTING:
AUDIO:
FORBIDDEN_LATER_STAGE_ELEMENTS:
OUTPUT_FILENAME:
STATUS: planned / frames_ready / video_review / accepted / revise
REVISION_NOTE:
```

`GLOBAL_CLIP_NUMBER`, filmdeki sıralamadır. `LOCAL_CLIP_ID`, kendi odasındaki zincir sırasıdır. Bu ayrım, odaların üretimini farklı günlerde yaparken kurguyu korur.

## 19. Kurgu: kesintisiz görünüm ve tam süre

1. **Proje ayarlarını baştan belirle.** Yatay final için 1920×1080, dikey için 1080×1920 çalışma alanı seçilebilir. Videolar 24 fps geliyorsa 24 fps zaman çizelgesiyle ilerlemek basittir. Bunlar teslim tercihleridir; dosyaların gerçek özelliklerini kontrol et.
2. **Klipleri durum sırasına koy.** Aynı zincirde V001, V002, V003… Her oda geçişi editörde ayrı kesmedir.
3. **Birleşimleri önce geçiş efekti olmadan incele.** Uyumlu karelerin arasına sürekli dissolve eklemek çift duvar, hayalet işçi ve yumuşayan mimari oluşturabilir.
4. **Hatalı görüntüyü sabit kareyle örtme.** Birleşime tek G eklemek göz kırpması yaratabilir. Önce yanlış video üretimini veya yanlış sürüm kullanımını düzelt.
5. **Sesi ortak ortamla bağla.** Aynı odada sürekli bir düşük ortam katmanı kullan. Klip seslerinin kesme noktalarına kısa ses geçişleri yapılabilir; bu, görüntü kliplerinin süresini değiştirmeyi gerektirmez.
6. **Müzik varsa bütün film için kurgula.** Her 8 saniyede yeniden başlayan müzik isteme. İş sesleri görünen eylemle eşleşsin.
7. **Rengi bütün olarak eşleştir.** Küçük pozlama farkları düzeltilebilir; farklı gölge yönü veya eksik pencere renk düzenlemeyle onarılamaz.
8. **Süreyi son dosyada kontrol et.** 150 adet gerçek 8 saniyelik klip, boşluk ve bindirme olmadan 1200 saniyedir.

24 fps ve tam 8 saniyelik bir klip 192 kareye karşılık gelir; 150 klip toplam 28.800 karedir. Konteynerdeki süre/kare hızı farklıysa bu hesabı doğrudan kabul etme, dosyayı kontrol et.

Bir klibi kırpmak gerekiyorsa toplam süre değişir. Her klibin 8 saniye kalması şartını korumak için önce aynı işi doğru 8 saniyelik üretimle çöz. Rastgele donuk kare eklemek veya bütün filmi hızlandırmak zincirdeki hareket ritmini bozabilir.

Yatay filmi otomatik merkez kırpmayla dikeye çevirmek, vinci veya işin sonucunu dışarıda bırakabilir. Dikey sürüm ayrı kompozisyon ister; yalnız ana hareket gerçekten merkezde kalıyorsa mevcut görüntüden uyarlama yap.

## 20. Yirmi dakikalık bir ev filmi için üretim düzeni

**150 klip bir süre hesabıdır; 150 ayrı fikrin gerekli olduğu anlamına gelmez.** İşleri odalar ve ana değişimler halinde grupla. Her oda için başlangıç durumunu, tamamlanma hedefini ve görüntüdeki ayırt edici öğeyi belirle.

Örnek bölüm bütçesi:

| Bölüm | Klip | Süre | Ana kazanım |
|---|---:|---:|---|
| Açılış ve ilk büyük söküm | 4 | 00:32 | Dönüşecek yapının açığa çıkması |
| Ortak yapı ve hazırlık | 14 | 01:52 | Temiz, onarılmış ve çalışılabilir yapı |
| Salon | 15 | 02:00 | Ev kimliğinin ilk büyük kanıtı |
| Mutfak ve yemek alanı | 24 | 03:12 | Günlük yaşam alanlarının kurulması |
| Yatak odası ve giyinme | 22 | 02:56 | Daha sıcak ve kişisel mekânlar |
| Banyo ve spa | 14 | 01:52 | Taş, cam ve suyla farklı bir dönüşüm |
| Kütüphane ve sinema | 20 | 02:40 | Farklı işlev ve ışık düzenleri |
| İç bahçe | 14 | 01:52 | Yapıya doğanın katılması |
| Dış cephe ve peyzaj | 15 | 02:00 | Evin çevresiyle tamamlanması |
| Kullanım ve final | 8 | 01:04 | İşlerin çalıştığının görülmesi |
| **Toplam** | **150** | **20:00** | |

Bu tablodaki bölüm sayısı kamera zinciri sayısıyla aynı olmak zorunda değildir. Mutfak ve yemek alanı farklı sabit açılarsa iki zincir oluşturur. Finalde sekiz farklı açı kullanılacaksa bu üretimleri de ayrı zincirler/planlar olarak say. Toplam görsel ihtiyacını gerçek kamera planından hesapla.

Önerilen üretim sırası:

1. Tüm filmin yazılı durum planını çıkar; her G'yi hemen üretme.
2. Açılış için G000–G003 ve üç kliplik 24 saniyelik pilot hazırla.
3. Finalin güçlü olup olmadığını görmek için ayrı bir konsept görseli dene.
4. İlk oda zincirini 5–8 kliplik kontrol edilebilir partilerle ilerlet.
5. Her partiyi izle, onaylanan ortak G dosyasıyla sonraki partiye bağla.
6. Oda tamamlanınca kısa kurgu kontrolü yap; ardından yeni odaya geç.
7. Bütün odalar hazır olduğunda dış cephe dönüşleri ve final ile zaman uyumunu kontrol et.

Parti sınırı, zinciri otomatik olarak yeniden başlatmaz. Aynı kamera ve aynı iş ilerliyorsa önceki partinin son G'si yenisinin ilk G'sidir; fazladan görsel gerekmez.

Üç kliplik pilotun amacı gerçek kamera sabitliğini, uç karelere uyumu ve hareketin okunmasını görmek. Başarılı pilot, sonraki bütün kliplerin sorunsuz olacağının kanıtı değildir; yeni ve daha zor işler kendi kontrollerini gerektirir.

## 21. Maliyet ve tekrar üretimi planlama

**Bu rakamlar Gemini API'nin 15 Ekim 2026'da erişilen standart ücretleridir; Flow kredisi veya başka platform paketinin fiyatı değildir.** Veo 3.1 Lite için 720p saniye başına 0,05 USD, 1080p 0,08 USD listeleniyor. [K7]

| Yalnız video | 720p | 1080p |
|---|---:|---:|
| Bir 8 saniyelik üretim | 0,40 USD | 0,64 USD |
| 150 üretim / 20 dakika | 60 USD | 96 USD |
| 225 üretim / kabul edilen 150 klip için ortalama 1,5 deneme örneği | 90 USD | 144 USD |

Nano Banana 2'nin 2K görsel çıkışı için yaklaşık 0,101 USD listeleniyor. Örneğin 160 ilk üretimin yalnız görsel çıkışı yaklaşık **16,16 USD** olur. Girdi, ek metin/işleme maliyetleri, tekrarlar, vergi ve aracı hizmet ücretleri bu basit hesaba dahil değildir. [K7]

Tekrar katsayısı gerçek başarı oranı iddiası değildir. Kendi pilotundaki ücretli üretim sayısını kabul edilen klip sayısına bölerek başlangıç tahmini elde edebilirsin. Düşük çözünürlükte denediğin bir işi 1080p'de yeniden üretmek de yeni üretimdir; toplam bütçeye ekle.

Hesap:

`Video bütçesi = ücretli üretim sayısı × 8 × seçilen saniye ücreti`

Flow kullanıyorsan aynı hesabı o anda seçili modelin klip başına kredi bedeliyle yap. Hesabındaki üretim ekranının fiyatını esas al.

## 22. API kullanacaksan alan eşlemesi

Arayüzden çalışıyorsan bu bölümü atlayabilirsin. Bu tablo çalıştırılan bir program değil, doğru uç karelerin hangi alanlara karşılık geldiğini gösterir. [K5]

| Amaç | Gemini Python SDK alanı | REST / JavaScript karşılığı |
|---|---|---|
| Model | `model` | `model` |
| Başlangıç görseli | `image` | `image` |
| Bitiş görseli | `config.last_frame` | `lastFrame` — REST'te instance, JS'te config alanı |
| Süre | `config.duration_seconds` | `durationSeconds` |
| Oran | `config.aspect_ratio` | `aspectRatio` |
| Çözünürlük | `config.resolution` | `resolution` |

Model kimliği: `veo-3.1-lite-generate-preview`. G000 ve G001 gerçek resim nesneleri/verileri olmalı; düz dosya adları görsel yüklemek yerine geçmez. API çağrısı biçimini kullandığın SDK sürümünün güncel dokümanıyla eşleştir. Aynı istek için seçilen seed, aynı çıktıyı kesin olarak tekrar üretme garantisi değildir. [K5–K6]

## 23. Yeni film planlatmak için kopyalanabilir ana prompt

Bu metni bir sonraki konu için planlama asistanına verebilirsin. Henüz görsel üretmez; görsel ve video işlerini düzenli hale getirir.

```text
Act as a construction timelapse director and continuity planner.

PROJECT: [Describe the transformation and final use.]
FORMAT: [16:9 horizontal / 9:16 vertical]
TOTAL DURATION: [seconds]
CLIP DURATION: exactly 8 seconds
IMAGE MODEL: Nano Banana 2
VIDEO MODEL: Veo 3.1 Lite, first-and-last-frame generation

Build a practical production plan using this rule:
Within each continuous camera chain, G000 to G001 produces V001,
G001 to G002 produces V002, and so on. The shared keyframe must be
the same approved image file. A change of room or camera angle starts
a new chain and is joined with an editorial cut, not an AI morph.

First define the story promise, the first four clips, the final payoff,
the room layout, the camera chains and the fixed architectural anchors.
Calculate the clip count and the keyframe count for the actual number
of independent chains. Do not assume every film needs only N+1 images.

For every keyframe, provide:
- ID and camera chain.
- Current visible construction state.
- One change from the previous state.
- Objects and architecture that must remain unchanged.
- Material, tool and worker locations.
- Elements that must not appear yet.
- An English Nano Banana prompt. Generate the first frame from text;
  derive subsequent frames by editing the previous approved image.

For every clip, provide:
- Global sequence number and local clip ID.
- Exact start-image and end-image IDs.
- Duration: 8 seconds.
- One main physical task.
- A visible material source, route and destination when applicable.
- An English Veo prompt describing accelerated continuous work.
- Camera and continuity constraints, appropriate sound, and the
  visible result used to confirm that the task is complete.

Keep completed work intact. Preserve fixed camera geometry within
each chain. Use short understandable physical actions and large visible
changes. Keep heavy objects rigid. Avoid close-up hand choreography,
hidden mechanical actions, abrupt architecture changes and multiple
unrelated jobs in one clip.

Use a practical construction order and record work already completed
before each room sequence. Ensure interior and exterior states agree.
Do not add future furnishings early. Describe still-image states in
image prompts and motion only in video prompts.

Deliver Turkish planning notes and English generation prompts.
Flag contradictions and resolve routine staging choices before drafting
the full prompt set. Separate verified model capabilities from creative
production recommendations. Do not promise viral performance.
```

## 24. Üretim öncesi kısa kontrol kartı

- [ ] Seçili model gerçekten Nano Banana 2 / hedeflenen sürüm mü?
- [ ] Veo modeli ve mod doğru mu: Lite, Frames, Start + End?
- [ ] Her klip 8 saniye mi; toplam klip sayısı süreye uyuyor mu?
- [ ] Her kamera zincirinin G000'ı ve sabit mimari kartı var mı?
- [ ] Sonraki G, önceki onaylı G'nin düzenlemesi mi?
- [ ] Paylaşılan G, komşu iki klipte aynı dosya ve sürüm mü?
- [ ] Her klipte tek ana iş ve görünür bir sonuç var mı?
- [ ] Giriş yolu, malzeme hareketi ve iniş/yerleşme alanı mümkün mü?
- [ ] Pencere, kapı, duvar, kiriş ve arka planlar tutarlı mı?
- [ ] Başlangıç ve bitiş ışığı uyumlu mu?
- [ ] Yeni odaya kurgu kesmesiyle mi geçiliyor?
- [ ] Klip sonu hedef G'ye uyuyor mu; birleşim izlendi mi?
- [ ] Sesler görünen işle uyuşuyor mu?
- [ ] Final yapının kullanımını gösteriyor mu?
- [ ] Son dosyanın oranı, süresi ve çözünürlüğü doğrulandı mı?

## Kaynaklar

Erişim ve kontrol tarihi: **15 Ekim 2026**. Ürün yüzeyi, hesap ve model sürümü değişebileceğinden üretim ekranındaki gerçek seçenekleri kontrol et. Buradaki resmî özellikler ile önerilen yaratıcı yöntemler birbirinden ayrılmıştır.

- **K1:** [Google AI for Developers — Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image)
- **K2:** [Google AI for Developers — Nano Banana image generation](https://ai.google.dev/gemini-api/docs/image-generation)
- **K3:** [Google Flow Help — Models and supported features](https://support.google.com/flow/answer/16352836?hl=en)
- **K4:** [Google Flow Help — Create videos / start and end frames](https://support.google.com/flow/answer/16353334?hl=en)
- **K5:** [Google AI for Developers — Veo generation and parameter tables](https://ai.google.dev/gemini-api/docs/veo?hl=en)
- **K6:** [Google AI for Developers — Veo 3.1 Lite](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=en)
- **K7:** [Google AI for Developers — Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing?hl=en)
- **Ek:** [Google Flow Help — Image creation and editing](https://support.google.com/flow/answer/16729550?hl=en)



