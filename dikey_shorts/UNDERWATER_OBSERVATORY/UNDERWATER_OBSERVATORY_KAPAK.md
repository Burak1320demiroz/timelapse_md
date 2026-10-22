# 🖼️ UNDERWATER OBSERVATORY — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⭐ Paketin kapak promptu ("Create ONE cover image based on the supplied approved final frame … improve readable lighting")
              YENİDEN KOMPOZİSYONDUR — KAPAK_KILAVUZU §0 ①'e göre yalnız G8 çekirdek testinden geçmezse kullanılır; o zaman da
              zincir_kontrol G8 ↔ kapak koşulur. Varsayılan: G8'in kendisi + başlık katmanı.
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99: RAIN TOWER'da usta kare plandan büyük çıktı, başlık kaydı;
           HIDDEN LOFT'ta prova koşulmadı]
METİN      UNDERWATER / OBSERVATORY  (2 kelime · iki satır · İngilizce · film adı · paketin önerisi)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   gece, kayaya oyulmuş koyu bir salon: ortada dev yuvarlak bir pencere, ardında projektörlerle aydınlanmış berrak turkuaz su,
                  batmış kaya duvarları ve gümüş balık izleri · pencerenin iki yanında kehribar ışıklı ahşap çıtalar · önünde cam
                  korkuluklu çelik asma kat · altta kavisli gözlem masası ve bank · pencerenin üstünde düz kömür duvar (başlık)
BAŞLIKTA YAZAN    UNDERWATER / OBSERVATORY

KANCA             "bu nasıl yapıldı?" — kapak suyun içine bakan bitmiş odayı gösterir; görünmeyen şey başlangıçtır (yarım halkalı boş
                  delik, havadaki yay, kuru kanyon). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ TURKUAZ PENCERE — kadrajın en parlak şekli, koyu kömür duvarın ortasında tek daire. 140 px'te bile "denizin altına
                  bakan bir pencere" okunur [P3-b: kontrast].
İKİNCİ OKUMA      asma kat ve cam korkuluk: "içinde durulabilen bir oda"
ÜÇÜNCÜ OKUMA      kehribar çıtalar + masa: "gözlem odası, yaşayan bir yer"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① boş delik ve havadaki dev yay ② dev levhanın dışarıdan kayıp deliği kapatması ③ suyun camı tırmanıp ışıkların yandığı an.
⛔ Kapak G7 DEĞİLDİR: G7'de su %75'te, ışıklar sönük, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" /
   "BUILDWAKE" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   tavan + monoray                    0–473      kanıt yok
   pencere duvarının üst kenarı      473
   düz kömür duvar (pencerenin üstü) 473–783
   ⭐ BAŞLIK KUTUSU                   560–770    x 180–900 (kılavuz §3 "film adı kutusu") — pencerenin ÜSTÜNDEKİ düz kömür duvar
   ⭐ çelik halkanın dış üstü          783        kutunun 13 px altı
   ⭐ turkuaz pencere                  814–1305   x 321–759 (438 px)
   kehribar çıtalar (iki yanda)      ≈ 800–1300 x ≈ 210–290 · 790–870
   ⭐ cam korkuluk + asma kat kenarı   1215–1361  kadraj boyu
   servis kapısı (kapalı değil, loş) 1402–1668  x 108–386
   ⭐ gözlem masası + cyan şerit       1608–1747  x 351–721
   bank                              1706–1781  x 359–718
   alt UI bandı                      1440–1920  (masa, bank, zemin — yardımcı doku)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · pencere ✅ · halka (üstü 783, kutunun 17 px üstünde — beyanlı) · asma kat +
   korkuluk ✅ · çıtalar (x 210–290 · 790–870, çekirdeğin içinde) ✅ · kapı ve masa çekirdeğin altında — yardımcı doku, beyanlı
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, pencereyi, asma katı ve kapının üstünü taşır, masayı keser · 4:5 (285–1635) ve
   3:4 (240–1680) masanın üst kenarını da taşır.
⚠️ Kapı arkası (loş tünel) G8'de ışıksız kalmalı — kapı aydınlanırsa çekirdeğin altında dikkat dağıtır (G8 elle kontrol).
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      UNDERWATER OBSERVATORY — İKİ SATIR:  "UNDERWATER"  /  "OBSERVATORY"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — pencerenin üstündeki düz kömür duvar (sahip seçimi "kılavuz yerleşimi" 22.10.2026;
           paketin "pencerenin hemen üstü" isteğiyle aynı) · yazı pencereyi, suyu ve balıkları örtmez
           satır 1 "UNDERWATER"  y ≈ 575–665 · satır 2 "OBSERVATORY"  y ≈ 680–770
PUNTO      ⚠️ "OBSERVATORY" 11 harf: 720 px'lik kutuya ≈ 84–92 px yazı boyu sığar (kalın, dar olmayan sans-serif) — kılavuz §5 aralığının
           alt ucu; gerçek yazı sınırları 720 × 210'u AŞMAZ, aşarsa punto küçülür, harf aralığı daraltılmaz
           kalın sans-serif · tek ağırlık · ölçülü harf aralığı · parlama YOK (paketin "kırık beyaz, kehribar vurgu" isteğinden
           yalnız renk alındı; vurgu YOK — tek renk)
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan düz kömür duvar, gece → kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse
           başlığın arkasına ölçülü koyu geçiş [kılavuz §5]
           ⚠️ turkuaz pencerenin ışığı duvara yansırsa zemin açılır (plan RİSK ⑧) — prova metinsiz G8 ile ÖNCE yapılır; duvar açık
           çıkarsa G8 yeniden ("the plain wall above the window stays dark")
           ⚠️ "OBSERVATORY" satırının altı (py 770) halkanın üstüne (py 783) yakın — 13 px boşluk. Değiyorsa punto küçülür, satırlar
           yukarı alınır (en çok y 540'a kadar — çekirdeğin üstü).
⛔ Başka kelime yok: "AI" · "timelapse" · "canyon" · "before/after" · "BUILDWAKE" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada zemin ve merdivenin dibi var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "turkuaz yuvarlak pencere" ayrışıyor mu ⓑ iki satır okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "boş dev delik, havada yay" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, pencere ve asma kat TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "denizin altında bir gözlem odası" diyor mu — "akvaryum salonu", "bilimkurgu üssü" ya da "vitrin
               render'ı" diyorsa G8 yeniden; kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki pencere = finaldeki pencere [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + UNDERWATER OBSERVATORY   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ                     G8 tam kare — sahip kararı
ⓒ METİNSİZ                      ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok.
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse. (Paketteki "BUILDWAKE" kanal adı DEĞİLDİR — "by BUILDWAKE" ve #buildwake çıkarıldı.)
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma adı yok · ≤ 40 karakter.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     Dry Canyon to Underwater Observatory      (36)   ⭐ paketin ilk başlığının kısaltılmışı
② SORU   What Is This Giant Ring For?              (28)   ⭐ planın MERAK SORUSU
③ KISA   The Window That Holds Back the Sea        (34)
```

> ⚠️ Paketteki tam hâl "From Dry Rock Canyon to Giant Underwater Observatory | AI Timelapse" 69 karakter, ikinci seçenek "Watch a Giant
> Underwater Observatory Take Shape | AI Timelapse" 62 karakter — kanal tavanı 40 (MUZIK_VE_KAPAK §3); "| AI Timelapse" eki ancak sahibin
> açık onayıyla kalır (THE SLOW TAKEOFF emsali). Paketin Türkçe başlığı ("Kuru Kanyondan Dev Sualtı Gözlemevine Dönüşüm") kanal kuralına
> göre kullanılmaz — başlık İNGİLİZCE. ① sonucu söyler; ② merak sorusunu söyler (KILAVUZ_REHBERI §6: "BAŞLIK soruyu söyler") — karar
> sahibin. Üçü de 40 karakterin altında.

**Açıklama:**

```
An empty round hole in a raw concrete chamber, a giant steel arc already hanging over it. In a single day two workers close the
ring, slide a thick acrylic window into place from the outside, build a viewing deck in front of it and finish the room in
charcoal and timber. At dusk the gate at the far end of the canyon opens.

One day in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real home, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #underwaterarchitecture #observatory #interiordesign #transformation
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Paketin etiketlerinden "underwater architecture" · "architecture transformation"
> yapı-özel dörtlüye girdi; #buildwake ve "megalithic build" (yapıya uymuyor) çıkarıldı. Altbilginin iki dilli beyanı SİLİNMEZ,
> KISALTILMAZ.
> ⚠️ Paketin kısa açıklaması ("An AI-generated timelapse concept by BUILDWAKE. Created using an 8-scene start-to-end keyframe workflow.")
> kullanılmadı: kanal adı yanlış, iş akışı izleyiciye söylenmez. Açıklama suyu ve ışığı ANMAZ ("the gate … opens") — spoiler bütçesi.

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
underwater observatory, underwater room, acrylic window, underwater architecture, observatory build, room transformation, interior renovation, construction timelapse, renovation timelapse, ai timelapse, ai video, timelapse, underwater obsevatory, acrylic windo
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("underwater obsevatory" · "acrylic windo" bu yüzden bilerek var). Gerçek yer/firma adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
The big round windows you see in aquariums are not glass. They are usually thick cast acrylic, often made from several sheets
bonded together and polished until the joins disappear, because acrylic is clearer and much tougher than glass at that size.
The window is normally set on the water side of its frame, so the pressure of the water pushes it into its seat instead of
pulling it out, and the thickness grows with depth. Before any water goes in, the seal around the edge is the part that gets
checked most carefully.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("usually · often · normally"). Döküm akrilik, katmanların
> yapıştırılması ve levhanın su tarafına oturtulması yaygın bilgidir; belirli ürün, ölçü ya da kalınlık iddia edilmez (planın TASARIM ②
> fizik notuyla aynı — ÇIKARIM). Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | kuru kanyondan sualtı gözlemevine (①), ya da bir gizem (② ③) | nasıl, ne kadar sürede, su ve ışık anı |
| kapak | bitmiş, suya bakan ışıklı oda + başlık | boş delik, havadaki yay, levhanın kayışı, suyun yükselişi |
| ilk 2 sn | havadaki dev yay, boş yuvarlak delik, dışarıda sarılı levha | deliğin neye dönüşeceği |
| açıklama | iki işçi, halka, dışarıdan akrilik pencere, asma kat, kömür + ahşap, "kapak açılır" | suyun pencereyi kapatması, ışık |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (su pencereyi kapatır, ışıklar yanar) kapak dışında söyleyemez → ⚠️ başlık ①
seçilirse "underwater" sonucu verir; suyun geliş anı yine saklıdır (taslak; kurgudan sonra tekrar).

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: İÇ MEKÂN bekleyen ailesi — THE SKY VAULT · THE HIDDEN LOFT ile ARDIŞIK YAYINLANAMAZ; THE BLUE SILO (akrilik + su + sürü) ile
   araya en az iki film [YAYIN_PLANI §3].
