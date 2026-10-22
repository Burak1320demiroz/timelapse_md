# 🖼️ GAME ON — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⭐ Paketin isteği "G8'in işçisiz final karesi: kömür zemin, amber pota altı, beyaz yaylar, ahşap tribün, büyük amber daire;
              pota üst-ortada, saha merkezde baskın" — G8 budur (pota ve daire orta eksende, kadrajın üst yarısının altında).
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99: RAIN TOWER'da usta kare plandan büyük çıktı, başlık kaydı;
           HIDDEN LOFT'ta prova koşulmadı]
METİN      GAME / ON  (2 kelime · iki satır · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi alacakaranlıkta duvarlarla çevrili bir arsa: projektör ışığında kömür renkli bir saha, amber pota altı, beyaz
                  çizgiler ve yay · arkada kırık beyaz duvar bandında dev amber daire, önünde tek pota · iki yanda koyu tel çit ve
                  ışık direkleri · solda alçak ahşap tribün · üstte koyu tuğla ve çatı hattının ötesinde mavi gök
BAŞLIKTA YAZAN    GAME / ON

KANCA             "bu saha nereden çıktı?" — başlık oyunun BAŞLADIĞINI söyler, kapak sahayı gösterir; görünmeyen şey başlangıçtır
                  (molozla dolu arsa, havadaki kova). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ IŞIKLI SAHA + AMBER DAİRE — kadrajın en parlak şekli (ışıklı saha ve bant) koyu tuğla ve mavi göğün altında; amber
                  pota altı ve daire orta eksende üst üste. 140 px'te bile "ışıklı bir sokak sahası" okunur [P3-b: kontrast].
İKİNCİ OKUMA      tek pota ve yay: "yarım saha, sokak basketbolu"
ÜÇÜNCÜ OKUMA      soldaki dolu konteyner (alt bant): "burası bir şantiyeydi" — kapağın içindeki tek "önce" izi, öncesi/sonrası bölmesi
                  DEĞİL (aynı karede, aynı dünyada duran gerçek nesne)

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① molozla dolu arsa ve havadaki kova ② duvarın beyaza, dairenin ambere dönüşü ③ potanın oturup ışıkların yandığı an.
⛔ Kapak G7 DEĞİLDİR: G7'de ışıklar sönük, pota yerinde değil, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" /
   "BEFORE-AFTER" / "BUILDWAKE" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   uzak çatılar + mavi gök            0–390      kanıt yok
   arka binanın çatı hattı           390
   koyu tuğla                        390–785
   ⭐ BAŞLIK KUTUSU                   560–770    x 180–900 (kılavuz §3 "film adı kutusu") — sıva bandının ÜSTÜNDEKİ koyu tuğla
   ⭐ kırık beyaz bandın üstü          785        kutunun 15 px altı
   ⭐ amber daire                      798–948    x 469–611
   ışık direği başları               833        x 50–122 · 870–927 (kutunun 63 px altı)
   ⭐ pota (pano + çember + taban)     914–1040   x 501–578
   ⭐ pota altı (amber)                1046–1230  x 425–655
   serbest atış dairesi + yay tepesi 1165–1305  x 455–625 · yay uçları 296–784
   tribün                            1083–1481  x 9–235
   çitler                            892–1730   kenarlarda
   yarı saha çizgisi                 1543       x 143–937
   alt UI bandı                      1440–1920  (yarı saha, ön bant, konteyner, ön duvarlar — kanıt yok)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · daire ✅ · pota ✅ · pota altı ✅ · serbest atış dairesi + yay tepesi ✅ ·
   ışık direkleri (sağ ✅, sol x 50–122 çekirdeğin solunda — tanık, beyanlı) · tribün (x 9–235, çekirdeğin sol kenarından taşar —
   beyanlı) · yarı saha ve konteyner çekirdeğin altında — yardımcı doku, beyanlı
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, daireyi, potayı, pota altını, yayı ve tribünün çoğunu taşır, yarı saha çizgisini keser ·
   4:5 (285–1635) ve 3:4 (240–1680) yarı saha çizgisini ve ön bandın bir kısmını da taşır.
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      GAME ON — İKİ SATIR:  "GAME"  /  "ON"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — sıva bandının üstündeki koyu tuğla; paketin "merkeze yakın iki satır" isteği kılavuz
           yerleşimine çevrildi (sahip seçimi 20.10.2026): yazı daireyi, potayı ve pota altını örtmez
           satır 1 "GAME"  y ≈ 580–670 · satır 2 "ON"  y ≈ 680–770
PUNTO      ⭐ iki satırda ≈ 92–104 px yazı boyu (kılavuz §5); gerçek yazı sınırları 720 × 210'u AŞMAZ
           kalın sans-serif · tek ağırlık · ölçülü harf aralığı · parlama YOK (paketin "kalın ve sade; logo, rozet, uzun slogan,
           filigran yok" isteğiyle aynı)
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan koyu tuğla, mavi saatte daha da koyu → kontrast iyi beklenir; ölçülür,
           4,5:1'i geçmezse başlığın arkasına ölçülü koyu geçiş [kılavuz §5]
           ⚠️ projektör ışığı tuğlaya vurursa zemin açılır (plan RİSK ⑧) — prova metinsiz G8 ile ÖNCE yapılır; tuğla açık çıkarsa G8
           yeniden ("the dark brick above stays dark")
           ⚠️ "ON" satırının altı (py 770) kırık beyaz bandın üstüne (py 785) yakın — 15 px boşluk. Değiyorsa punto küçülür, satırlar
           yukarı alınır (en çok y 540'a kadar — çekirdeğin üstü).
⛔ Başka kelime yok: "basketball" · "court" · "rubble" · "makeover" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada sağ çit ve ön bant var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "ışıklı sokak sahası, amber daire" ayrışıyor mu ⓑ iki satır okunuyor mu ⓒ sağ alt köşe boş
               mu · ⭐ aynı test G0'a: "molozla dolu arsa, havada kova" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, daire, pota ve pota altı TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "akşam oynanacak bir mahalle sahası" diyor mu — "stadyum" ya da "vitrin render'ı" diyorsa G8
               yeniden; kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki saha = finaldeki saha [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + GAME ON          yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
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
① İŞ     From Rubble to a Basketball Court         (33)   ⭐ sahibin paketindeki başlık, "| AI Timelapse" eki olmadan
② SORU   What Are They Building in This Lot?       (35)
③ KISA   One Rubble Lot, One Street Court          (32)
```

> ⚠️ Paketteki tam hâl "From Rubble to a Basketball Court | AI Timelapse" 48 karakter — kanal tavanı 40 (MUZIK_VE_KAPAK §3);
> ek ancak sahibin açık onayıyla kalır (THE SLOW TAKEOFF emsali). ① sonucu söyler (saha); ② merak sorusunu söyler
> (KILAVUZ_REHBERI §6: "BAŞLIK soruyu söyler") — karar sahibin. Üçü de 40 karakterin altında.

**Açıklama:**

```
Rubble up to the back wall and the first bucket already in the air. In a single day two workers clear the lot, lay new
asphalt, paint a giant amber circle on the wall, fence both sides and mark out the ground strip by strip. At dusk the last
piece rolls in through the entrance.

One day in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real home, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #basketballcourt #streetball #urbanrenewal #transformation
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Paketin etiketlerinden #BasketballCourt ve #Transformation yapı-özel
> dörtlüye girdi, #AITimelapse kanal kalıbında #aivideo; #BUILDWAKE çıkarıldı (kanal adı değil). Altbilginin iki dilli beyanı SİLİNMEZ,
> KISALTILMAZ.
> ⚠️ Paketin "Who would you bring for the first game?" satırı ÇIKARILDI: "tag a friend" türü yorum tuzağı [A33-b · KILAVUZ_REHBERI
> §6 YORUM TUZAĞI YOK].
> ⚠️ Açıklama potayı ve ışığı ANMAZ ("the last piece rolls in through the entrance") — spoiler bütçesi (aşağıda). Paketin İngilizce kısa
> açıklaması ("Rubble cleared. Lines painted. Game on.") başlığı tekrar ettiği ve yolu verdiği için kullanılmadı.

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
basketball court build, street court, rubble to court, court renovation, urban renewal, outdoor basketball court, court painting, half court, renovation timelapse, construction timelapse, ai timelapse, ai video, timelapse, basketbal court, basketball cort
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("basketbal court" · "basketball cort" bu yüzden bilerek var). Gerçek yer/firma adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
An outdoor court is mostly about the layer you never see. Old asphalt is usually patched and given a fresh, smooth surface
first, because every crack under the paint comes back as a crack in the court. The colour coats are normally an acrylic court
surfacing laid in thin layers, often with fine sand mixed in for grip, and each colour is kept to its own zone with tape. The
lines go on last, taped and rolled, so they stay crisp. And the hoop here is a portable one: its base is filled with water or
sand for weight, which is why it can be rolled in on two wheels and then sit firmly without being bolted to the ground.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("usually · normally · often"). Akrilik saha kaplaması
> ve kum katkısı, taşınabilir potanın su/kumla doldurulan tabanı yaygın bilgidir; belirli ürün ya da ölçü iddia edilmez. Promptta
> "water" geçmez — bu yalnız yorumdur. Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | molozdan basketbol sahasına (①), ya da bir gizem (② ③) | nasıl, ne kadar sürede, ışık |
| kapak | bitmiş, ışıklı saha + başlık | molozla dolu arsa, havadaki kova, ışığın yandığı an |
| ilk 2 sn | havadaki dolu kova, moloz yığını, ilk temiz şerit | arsanın neye dönüşeceği |
| açıklama | iki işçi, asfalt, amber daire, çit, şerit şerit boya, "son parça kapıdan gelir" | potanın ve ışığın ne olduğu |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (pota oturur, ışıklar yanar) kapak dışında söyleyemez → ⚠️ başlık ①
seçilirse "basketball court" sonucu verir; ışığın anı yine saklıdır (taslak; kurgudan sonra tekrar).

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: ⭐ ZEMİN ailesi — HIDDEN OASIS · SWALLOWED BUS · EMPTY LOCK · DEEP END · VANISHING ROOM · FIRST GUEST · LAST STOP ile
   ARDIŞIK YAYINLANAMAZ (aynı aile) [YAYIN_PLANI §3].
