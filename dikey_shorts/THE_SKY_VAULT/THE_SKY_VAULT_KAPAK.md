# 🖼️ THE SKY VAULT — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⭐ Paketin isteği "G8'in işçisiz finali: koyu sekizgen kabuk, amber iç ışık, krem koltuklar ve şehir silueti tek görüntüde" —
              G8 budur. "Gerçek filmde bulunmayan dev manzara, yeni kat veya fazladan yapı eklenmez" — paketle aynı kural.
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99: RAIN TOWER'da usta kare plandan büyük çıktı, başlık kaydı;
           HIDDEN LOFT'ta prova koşulmadı]
METİN      THE SKY / VAULT  (3 kelime · iki satır · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi alacakaranlıkta bir şehir çatısı: ortada koyu kömür sekizgen bir depo, üç ön yüzünde temiz cam, camların
                  arkasında SICAK AMBER ışıkta iki krem berjer ve yuvarlak traverten sehpa · meşe döşeli platform, alçak siyah
                  korkuluk, iki köşede koyu saksı · solda rafta üç paslı eski panel · sağda merdiven evi · arkada pencereleri
                  yanan üç bina
BAŞLIKTA YAZAN    THE SKY / VAULT

KANCA             "bir çatı deposunun içinde oda mı var?" — başlık bir kasa (vault) söyler, kapak kasanın içini gösterir; görünmeyen
                  şey başlangıçtır (paslı depo, havadaki panel, borular). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı
                  64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ ÜÇ YANAN CAM + KÖMÜR GÖVDE — kadrajın en parlak şekli (üç cam) koyu kömür kabuk ve mavi göğün ortasında. 140 px'te
                  bile "çatıda içi yanan küçük bir oda" okunur [P3-b: kontrast].
İKİNCİ OKUMA      camın arkasındaki iki berjer: "burada biri oturup şehre bakacak"
ÜÇÜNCÜ OKUMA      soldaki paslı paneller: "bu yüzler oradan söküldü" — kapağın içindeki tek "önce" izi, öncesi/sonrası bölmesi DEĞİL
                  (aynı karede, aynı dünyada duran gerçek nesne)

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① paslı depo ve havadaki panel ② kabuğun renk değiştiren boyası ③ süt beyazı filmin soyulup odanın çıktığı an.
⛔ Kapak G7 DEĞİLDİR: G7'de camlar filmli, oda görünmez, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" /
   "BUILDWAKE" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   açık gök (koyu mavi → mavi)       0–560      kanıt yok
   ⭐ BAŞLIK KUTUSU                   560–770    x 180–900 (kılavuz §3 "film adı kutusu") — deponun ÜSTÜNDEKİ sakin mavi alacakaranlık gök
   ⭐ konik çatının tepesi             802        x 540 — kutunun 32 px altı
   üç bina (tepeler)                 815–842    x 14–105 · 201–255 · 862–939 — kutunun ≥ 45 px altı
   raf + üç paslı panel              952–1200   x 99–236
   ⭐ üç cam yüz                       905–1340   x 309–498 · 498–727 · 727–796
   merdiven evi                      998–1294   x 884–1080
   ⭐ berjerler / sehpa (camdan)       1162–1303  x 391–464 · 565–641 / 492–562
   saksılar                          1138–1343  x 143–236 · 871–941
   korkuluk                          1193–1431  x 151–939 (basamakta açık)
   ⭐ deponun alt kenarı (platform üstü) 1356
   platform + basamaklar             1185–1585  x 151–939 · basamak 588–825
   alt UI bandı                      1440–1920  (basamakların dibi, çatı çakılı — kanıt yok)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · depo ✅ · üç cam ✅ · berjerler + sehpa ✅ · korkuluğun büyük kısmı ✅ ·
   sağ saksı ✅ · sol saksı (x 143–236) çekirdeğin sol kenarından 7 px taşar · raf (x 99–236) ≈ 50 px taşar — tanıktır, kanıt değil,
   beyanlı · basamaklar (py 1397–1585) çekirdeğin altında — yardımcı doku, beyanlı
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, depoyu, camları, berjerleri, korkuluğu, saksıları ve rafı tam taşır, basamakların üstünü
   keser · 4:5 (285–1635) ve 3:4 (240–1680) basamakları ve çatının bir kısmını da taşır.
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      THE SKY VAULT — İKİ SATIR:  "THE SKY"  /  "VAULT"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — deponun üstündeki açık gök; paketin "ortada iki satır" isteği kılavuz yerleşimine
           çevrildi (sahip seçimi 20.10.2026): yazı camı, berjerleri ve binaları örtmez
           satır 1 "THE SKY"  y ≈ 580–670 · satır 2 "VAULT"  y ≈ 680–770
PUNTO      ⭐ iki satırda ≈ 92–104 px yazı boyu (kılavuz §5); gerçek yazı sınırları 720 × 210'u AŞMAZ
           kalın sans-serif · tek ağırlık · ölçülü harf aralığı · parlama YOK (paketin "düz ve temiz tipografi; ikon, rozet, üç boyutlu
           efekt yok" isteğiyle aynı)
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] — paketin #E8E2D8'i neredeyse aynı ama BUILDWAKE paletinden; kanal paleti geçerli ·
           arka plan mavi saatte koyu mavi gök → kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse başlığın arkasına ölçülü koyu geçiş
           [kılavuz §5]
           ⚠️ gök ufka doğru açılır: "VAULT" satırının altı (py 770) ufuktan 8,4° yukarıda, soldaki sönen pembe bandın üstünde — prova
           metinsiz G8 ile ÖNCE yapılır; bant kutuya giriyorsa punto küçülmez, G8 yeniden (güneş −4° tutulur)
           ⚠️ "VAULT" satırının altı konik çatının tepesine (x 540, py 802) yakın — 32 px boşluk. Değiyorsa punto küçülür.
⛔ Başka kelime yok: "tank" · "rooftop" · "lounge" · "makeover" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada çatı çakılı ve basamakların sağı var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "çatıda içi yanan kömür renkli küçük oda" ayrışıyor mu ⓑ iki satır okunuyor mu ⓒ sağ alt
               köşe boş mu · ⭐ aynı test G0'a: "paslı depo, paneli havada" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, üç cam ve berjerler TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "şehrin üstünde oturulacak sıcak bir oda" diyor mu — "otel reklamı" ya da "vitrin render'ı"
               diyorsa G8 yeniden; kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki depo = finaldeki depo [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + THE SKY VAULT    yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ             G8 tam kare — sahip kararı
ⓒ METİNSİZ              ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok.
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse. (Paketteki "BUILDWAKE" kanal adı DEĞİLDİR — "by BUILDWAKE" ve #BUILDWAKE çıkarıldı.)
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma adı yok · ≤ 40 karakter.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     Rusty Water Tank to Rooftop Lounge        (34)   ⭐ sahibin paketindeki başlık, "| AI Timelapse" eki olmadan
② SORU   What's Inside This Old Rooftop Tank?      (36)
③ KISA   One Rusty Tank, One Glass Front           (31)
```

> ⚠️ Paketteki tam hâl "Rusty Water Tank to Rooftop Lounge | AI Timelapse" 49 karakter — kanal tavanı 40 (MUZIK_VE_KAPAK §3);
> ek ancak sahibin açık onayıyla kalır (THE SLOW TAKEOFF emsali). ① sonucu söyler (oda); ② merak sorusunu söyler
> (KILAVUZ_REHBERI §6: "BAŞLIK soruyu söyler") — karar sahibin. Üçü de 40 karakterin altında.
> ⚠️ "Lounge" yalnız başlıkta — promptta YASAK KELİME (bar/kulüp korpusu).

**Açıklama:**

```
Nobody had opened this tank in years. Rust through the paint, old pipes and sludge inside, and one of its front panels
already hanging from a small crane. In a single day two workers empty it, brush it back to bare steel, paint it charcoal,
lay an oak floor and carry everything up three short steps from the rooftop door. By dusk its new glass is still hidden
behind white film.

One day in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real home, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #rooftop #adaptivereuse #renovation #transformation
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Paketin dört etiketinden #Architecture zaten kalıpta,
> #Transformation yapı-özel dörtlüye girdi, #AITimelapse kanal kalıbında #aivideo; #BUILDWAKE çıkarıldı (kanal adı değil).
> Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> ⚠️ Paketin "Would you watch the sunset from here?" satırı ÇIKARILDI: ① bu kadrajda camlar kameraya (güneye) bakar, güneş deponun
> solunda, arkasında batar — oda gün batımına sırtını döner, soru filmin göstermediği şeyi vaat ederdi ② açıklamanın tek işi yorum
> istemek olurdu (LAST STOP'taki gerekçe). Sahip isterse "Would you sit here after dark?" gibi filmle uyumlu bir soru eklenir.
> ⚠️ Açıklama odayı ANMAZ ("its new glass is still hidden behind white film") — spoiler bütçesi (aşağıda). Paketin İngilizce kısa
> açıklaması ("…becomes a glass-fronted lounge… ivory seating and amber light") finali verdiği için kullanılmadı.

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
water tank conversion, rooftop room, rooftop lounge, tank renovation, adaptive reuse, glass room, old tank restoration, rooftop makeover, renovation timelapse, construction timelapse, ai timelapse, ai video, timelapse, watertank conversion, water tank convertion
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("watertank conversion" · "water tank convertion" bu yüzden bilerek var). Gerçek yer/firma adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
A rooftop tank this size can hold tens of tonnes of water when full, so it usually sits on a steel frame or platform built to
spread that load — which is also why an empty one can often take a small room's weight, though an engineer would still check.
Cutting openings into its side means keeping the corner posts and the rings at the top and bottom: once the panels come off,
they are what hold the shape. The white film on new glass is a protective layer left on until the messy work around it is
finished, then peeled last so paint, dust and boots never touch the glass. And the room only shows from outside once it is
brighter inside than out — glass always reflects some of the sky.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("usually · often · would still check"). Hacim
> hesabı: yüzden yüze 4,5 m sekizgen ≈ 16,8 m² × 3 m ≈ 50 m³ ≈ 50 t su — "tens of tonnes" doğru. Koruyucu film cümlesi cam
> montajında olağan uygulamadır, belirli bir ürün iddia edilmez. Yansıma cümlesi fiziktir (LAST STOP ile aynı mekanizma, başka
> cümle). Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | bir deponun odaya dönüşeceği (①), ya da bir gizem (② ③) | nasıl, ne kadar sürede, filmin soyulduğu an |
| kapak | bitmiş, içi yanan depo + başlık | paslı ilk depo, havadaki panel, film |
| ilk 2 sn | havadaki paslı panel, karanlık delik, eski borular | içeri girecek her şey |
| açıklama | iki işçi, kömür boya, meşe, basamaklar, "cam beyaz filmin arkasında" | odanın ne olduğu, berjerler, ışık |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (film soyulur, sıcak oda çıkar) kapak dışında söyleyemez → ⚠️ başlık ①
seçilirse "lounge" sonucu verir; filmin anı yine saklıdır (taslak; kurgudan sonra tekrar).

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: ⭐ KÜTLE ailesi — BLUE DOOR · BACK TO WATER · ONE MORE TURN · NARROW GORGE ile ARDIŞIK YAYINLANAMAZ (aynı aile) ·
   ⛔ THE LAST STOP ve THE HIDDEN LOFT ile de ardışık YAYINLANMAZ (içerik akrabası — açılış, iş sırası, örtülü cam) [YAYIN_PLANI §1 · §3].
