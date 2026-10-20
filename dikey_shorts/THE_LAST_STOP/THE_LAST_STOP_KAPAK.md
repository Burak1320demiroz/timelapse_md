# 🖼️ THE LAST STOP — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⭐ Paketin isteği "bordo otobüs kadrajı doldurur; camın altındaki yatak okunur" — G8 budur; "kadrajı doldurur" kapak
              kılavuzunun ana yapı bandına göre (sahip seçimi 19.10.2026: kılavuz yerleşimi).
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99: RAIN TOWER'da usta kare plandan büyük çıktı, başlık kaydı;
           HIDDEN LOFT'ta prova koşulmadı]
METİN      THE LAST / STOP  (3 kelime · iki satır · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi alacakaranlıkta bir orman açıklığı: ortada çapraz yatan koyu bordo bir otobüs, tavanının ortasında siyah
                  çerçeveli CAM, camın altında SICAK IŞIKTA krem örtülü yatak ve krem kanepe · yolcu pencerelerinden terasa düşen
                  sıcak ışık, terasta iki sandalye · solda takozlarda paslı eski tavan paneli ve katlanmış bomlu kamyon ·
                  otobüsün ötesinde koyu yosunlu orman zemini
BAŞLIKTA YAZAN    THE LAST / STOP

KANCA             "bu otobüs nasıl bu hâle geldi, neden burada duruyor?" — başlık bir yolculuğun SONUNU söyler, kapak yolculuğun
                  bittiği yeri gösterir; görünmeyen şey başlangıçtır (otun sardığı paslı otobüs, açılan tavan). Merak "ne
                  olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ YANAN CAM TAVAN + BORDO GÖVDE — kadrajın en parlak şekli (cam ve pencereler) koyu bordo ve mavi ormanın
                  ortasında. 140 px'te bile "ormanda içi yanan bir otobüs" okunur [P3-b: kontrast].
İKİNCİ OKUMA      camın altındaki yatak: "burada biri uyuyacak"
ÜÇÜNCÜ OKUMA      soldaki paslı panel: "bu tavan oradan söküldü" — kapağın içindeki tek "önce" izi, öncesi/sonrası bölmesi DEĞİL
                  (aynı karede, aynı dünyada duran gerçek nesne)

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① otun sardığı paslı otobüs ve havadaki panel ② gövdenin rengi değiştiren boyası ③ camın oturup ışığın yandığı an.
⛔ Kapak G7 DEĞİLDİR: G7'de cam havada, iç karanlık, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   orman zemini + ladin gövdeleri  0–560      koyu, gölgeli (30–50 m)
   ⭐ BAŞLIK KUTUSU                 560–770    x 180–900 (kılavuz §3 "film adı kutusu") — otobüsün ötesindeki koyu yosunlu zemin
   kamyon (kasa arkası + bom)      729–980    x 11–284 — bom kaidesi kutunun sol alt köşesine ≈ 40 px değer (x 155–225)
   ⭐ otobüs çatısının arka köşesi  778        x 308 — kutunun 8 px altı
   boş kızak                       ≈ 830–1028 x 678–968 (otobüsün ardında, kısmen gizli)
   ⭐ cam tavan                     843–1087   x 342–687 (345 px)
   yatak / kanepe (camdan)         919–1084   x 361–513 / 558–677
   yolcu pencereleri               958–1213   x 256–705
   paslı panel (takozlarda)        1050–1415  x 17–304
   kapı                            1185–1298  x 716–809
   teras + sandalyeler             1178–1533  x 418–781
   ⭐ otobüsün alt kenarı           1318       x 789 (ön)
   alt UI bandı                    1440–1920  (terasın yakın kenarı, çimen, kaya sırtının dibi — kanıt yok)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · cam tavan ✅ · yatak/kanepe ✅ · pencereler ✅ · kapı ✅ · terasın büyük
   kısmı ✅ · paslı panel (x 17–304) çekirdeğin sol kenarından ≈ 130 px taşar — tanıktır, kanıt değil, beyanlı
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, camı, yatağı, pencereleri, kapıyı ve terası tam taşır · 4:5 (285–1635) ve 3:4
   (240–1680) orman zemininin ve çimenin bir kısmını da taşır.
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      THE LAST STOP — İKİ SATIR:  "THE LAST"  /  "STOP"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — otobüsün ötesindeki koyu orman zemininin üstünde; paketin "ortadaki koyu
           gövde alanı" isteği kılavuz yerleşimine çevrildi (sahip seçimi 19.10.2026): yazı gövdeyi, camı ve yatağı örtmez
           satır 1 "THE LAST"  y ≈ 580–670 · satır 2 "STOP"  y ≈ 680–770
PUNTO      ⭐ iki satırda ≈ 92–104 px yazı boyu (kılavuz §5); gerçek yazı sınırları 720 × 210'u AŞMAZ
           kalın sans-serif · tek ağırlık · ölçülü harf aralığı · parlama YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan koyu, mavi saatte gölgeli yosun → kontrast iyi beklenir; ölçülür,
           4,5:1'i geçmezse başlığın arkasına ölçülü koyu geçiş [kılavuz §5]
           ⚠️ "STOP" satırının altı otobüs çatısının arka köşesine (x 308, py 778) yakın — yazı x 380–700 arasında, çatı kenarı
           orada py ≥ 808: ≥ 38 px boşluk. Değiyorsa punto küçülür.
           ⚠️ kamyonun bom kaidesi (x 155–225) "THE LAST" satırının solunda — satır x ≈ 240'tan başlar, değmez.
⛔ Başka kelime yok: "bus" · "glamping" · "makeover" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada çimen ve kaya sırtının dibi var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "ormanda içi yanan bordo otobüs" ayrışıyor mu ⓑ iki satır okunuyor mu ⓒ sağ alt köşe
               boş mu · ⭐ aynı test G0'a: "otun sardığı paslı otobüs, tavanı havada" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, cam tavan ve kapı TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "ormanda bir gece geçirilecek sıcak bir otobüs" diyor mu — "karavan reklamı" ya da "vitrin
               render'ı" diyorsa G8 yeniden; kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki otobüs = finaldeki otobüs [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + THE LAST STOP    yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ             G8 tam kare — sahip kararı
ⓒ METİNSİZ              ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok.
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma adı yok · ≤ 40 karakter.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     Rusty Bus to Glass-Roof Retreat           (31)   ⭐ sahibin paketindeki başlık, "| AI Timelapse" eki olmadan
② SORU   Why Cut the Roof Off This Old Bus?        (34)
③ KISA   One Old Bus, One Glass Roof               (27)
```

> ⚠️ Paketteki tam hâl "Rusty Bus to Glass-Roof Retreat | AI Timelapse" 46 karakter — kanal tavanı 40 (MUZIK_VE_KAPAK §3);
> ek ancak sahibin açık onayıyla kalır (THE SLOW TAKEOFF emsali). ① sonucu söyler (cam tavan); ② merak sorusunu söyler
> (KILAVUZ_REHBERI §6: "BAŞLIK soruyu söyler") — karar sahibin. Üçü de 40 karakterin altında.

**Açıklama:**

```
Nobody had moved this bus in years. Grass up to the wheel hubs, rust through the paint, and the middle of its roof already
lifted off on the boom. In a single day two workers clear it out, sand it back to bare metal, paint it deep burgundy, lay
an oak floor and carry a bed and a sofa in through one narrow door. At dusk the opening in the roof gets something new.

One day in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real home, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #busconversion #tinyhouse #forestcabin #renovation
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Paketin üç etiketi (#AITimelapse #BusConversion #TinyHouse)
> kanal kalıbına çevrildi; #skoolie KULLANILMADI (okul otobüsü değil). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> ⚠️ Paketin "Would you spend a night here?" satırı ÇIKARILDI: A33-b listesindeki kalıplardan değil, ama açıklamanın tek işi
> yorum istemek olurdu; sahip isterse sabit yorumun sonuna değil açıklamanın sonuna geri eklenir — karar sahibin.
> ⚠️ Açıklama camı ANMAZ ("the opening in the roof gets something new") — spoiler bütçesi (aşağıda). Paketin İngilizce kısa
> açıklaması ("An old bus becomes a glass-roof forest retreat…") finali verdiği için kullanılmadı.

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
bus conversion, bus to tiny house, bus renovation, glass roof, skylight bus, forest cabin, tiny house build, old bus restoration, bus makeover, renovation timelapse, construction timelapse, ai timelapse, ai video, timelapse, bus convertion, buss conversion
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("bus convertion" · "buss conversion" bu yüzden bilerek var). Gerçek yer/firma adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
A bus roof is part of its structure, not a lid. The roof skin and the hoops under it tie the two sides together, so cutting a
skylight usually means keeping a frame around the opening and stiffening it before the glass goes in — that is why the edge
of the roof stays in place here. Glass overhead is normally toughened or laminated safety glass, set into a gasket so it can
move a little as the body flexes and warms. And the lights at the end are not only for show: glass reflects some of the sky
whatever you do, so from outside you only see clearly into a room once it is brighter inside than out — which, in a forest,
happens at dusk.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("usually · normally · some of the sky");
> çatı hoop'larının taşıyıcılığı otobüs dönüşümlerinde yaygın bilgidir, belirli bir model iddia edilmez. Yansıma cümlesi
> fiziktir (cam her yüzeyde ışığın birkaç yüzdesini yansıtır; içerisi dışarıdan parlak değilse yansıma baskın okunur).
> Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | bir otobüsün dönüşeceği ve cam tavan (①), ya da bir gizem (② ③) | nasıl, ne kadar sürede, ışık |
| kapak | bitmiş, içi yanan otobüs + başlık | otun sardığı ilk otobüs, havadaki panel, ışığın yandığı an |
| ilk 2 sn | havadaki paslı panel, açık tavan, eski koltuklar | içeri girecek her şey |
| açıklama | iki işçi, tek kapı, bordo, yatak ve kanepe, "tavana yeni bir şey" | camın ne olduğu, ışık |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (cam oturur, içerisi yanar) kapak dışında söyleyemez → ⚠️ başlık ①
seçilirse cam verilmiş olur; ışık yine saklıdır (taslak; kurgudan sonra tekrar).

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: ⭐ ZEMİN ailesi — HIDDEN OASIS · SWALLOWED BUS · EMPTY LOCK · DEEP END · VANISHING ROOM · FIRST GUEST ile ARDIŞIK
   YAYINLANAMAZ (aynı aile) · SWALLOWED BUS ile ayrıca "otobüs" tekrarı · beş iç mekândan sonra dış mekân — HIDDEN LOFT'un arkasına
   önerilir (öneri, kural değil) [YAYIN_PLANI §3].
