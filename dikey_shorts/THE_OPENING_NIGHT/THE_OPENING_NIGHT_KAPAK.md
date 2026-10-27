# 🖼️ THE OPENING NIGHT — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7·b'nin 60,0–64,0 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden; G7a ile aynı dosya)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⛔ Paketin "havai fişekli kapak" fikri UYGULANMAZ: kıvılcım S7·b'de bir kez geçer ve söner; G8'in göğü DÜZ derin mavidir
              (başlık zemini) — kapak kıvılcımsız G8'dir.
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 63.5 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99]
METİN      OPENING NIGHT  (2 kelime · tek satır · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   gece, yukarıdan ve uzaktan bir futbol stadyumu: çatı kenarı boyunca parlak beyaz projektör sırası · altında kırmızı alt teras
                  ve sarı üst terası örten kalabalık, düz kırmızı-sarı pankartlar · solda düz beyaz ekran · parlak, şeritli yeşil saha ·
                  orta çizgide dizilmiş iki takım · üstte düz derin mavi gök (başlık)
BAŞLIKTA YAZAN    OPENING NIGHT

KANCA             "bu stadyum nasıl doldu?" — başlık "açılış" der; kapak dolu, ışıklı çanağı gösterir, görünmeyen şey BOŞLUKTUR (gri beton,
                  toprak saha). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ IŞIKLI SAHA + DOLU TERASLAR — kadrajın en parlak alanı saha, üstünde alacalı kalabalık bandı; 140 px'te bile "dolu, ışıklı
                  stadyum" okunur [P3-b: kontrast].
İKİNCİ OKUMA      projektör sırası ve çatı: "gece maçı"
ÜÇÜNCÜ OKUMA      orta çizgideki takımlar: "maç başlamak üzere"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① şafakta boş gri beton çanak ve toprak saha ② çimin, kırmızının ve sarının cephe cephe gelişi ③ kalabalığın vomitoryumlardan taşması ve
   projektörlerin yandığı an.
⛔ Kapak G7 DEĞİLDİR: G7'de projektörler sönük, saha boş, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
⛔ Kapakta gerçek kulüp, arma, sponsor, forma yazısı YOKTUR (paketin kuralı · plan TESLİM YAPISI).
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   açık gök (derin mavi)              0–560      kadraj boyu · merdiven kulesinin tepesi solda ≈ 740 (kutunun DIŞINDA, x ≈ 105–150)
   ⭐ BAŞLIK KUTUSU                   560–770    x 180–900 (kılavuz §3 "film adı kutusu") — uzak çatının üstündeki DÜZ derin mavi gök
   ⭐ çatı arka kenarı + üç makas      772        kadraj boyu — kutunun 2 px altı (⚠️ SINIRDA)
   çatı sırtı                         772–810
   ⭐ projektör sırası (YANIK)         810–828    kadraj boyu
   ⭐ ekran (düz beyaz)                828–898    x 260–436
   ⭐ üst teras + kalabalık (sarı)     834–968
   iki vomitoryum                     936–968    x 372–420 · 660–708
   ⭐ alt teras + kalabalık (kırmızı)  968–1103
   tünel + körük + iki kulübe         1077–1113  x 434–646
   uzak kale çizgisi + kale           1107–1129  x 228–852
   ⭐ ışıklı saha (uzak yarı)          1129–1348
   ⭐ orta çizgi + iki takım           ≈ 1324–1348
   saha (yakın yarı)                  1348–1920  — alt UI bandı (1440–1920) yardımcı doku: boş, şeritli çim

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · projektör sırası ✅ · ekran ✅ · iki teras ✅ · tünel ✅ · orta çizgideki takımlar ✅
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, çatıyı, iki terası, sahanın uzak yarısını ve takımları taşır · 4:5 (285–1635) ve 3:4 (240–1680) daha
   çok gök ve yakın saha taşır.
⚠️ Çatı arka kenarı (772) kutunun alt kenarına (770) değiyor — yazının GERÇEK sınırları kutunun üst yarısında kalır (satır y ≈ 600–700);
   projektör parıltısı (810) kutuya taşmamalı — G8 elle kontrol, plan RİSK ⑥ ve PİLOT (a).
⚠️ Merdiven kulesinin tepesi (≈ 740) kutunun SOLUNDA, dışında (x < 180) — yazı x 180'den başlar, kuleyi örtmez.
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      OPENING NIGHT — TEK SATIR, ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — uzak çatının üstündeki düz derin mavi gök · yazı çatıyı ve projektörleri örtmez · satır
           y ≈ 600–700 (dikey ortası ≈ 650)
PUNTO      "OPENING NIGHT" 13 karakter: 720 px'lik kutuya ≈ 85–95 px yazı boyu sığar (kalın, dar olmayan sans-serif); gerçek yazı sınırları
           720 × 210'u AŞMAZ, aşarsa punto küçülür, harf aralığı daraltılmaz · tek ağırlık · parlama YOK
           ⚠️ İki satır ("OPENING / NIGHT") yalnız 85 px altı punto 140 px testini geçmezse — ikinci satır çatıya inmeden y 560–770'e sığmalı
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan derin mavi gök → kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse başlığın
           arkasına ölçülü koyu geçiş [kılavuz §5]
⛔ Başka kelime yok: "AI" · "timelapse" · "stadium" · "before/after" · sayı kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada yalnız şeritli çim var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "dolu, ışıklı stadyum" ayrışıyor mu ⓑ OPENING NIGHT okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "boş gri beton çanak" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, çatı + iki teras + orta çizgi TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "açılış gecesi, dolu stadyum" diyor mu — "kart-postal", "render", "oyun ekranı" (futbol oyunu!) diyorsa
               G8 yeniden; kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki çanak = finaldeki çanak [MUZIK_VE_KAPAK §5]
⑦ ARMA/YAZI    kapakta pano, ekran, pankart, forma — hiçbirinde okunur yazı ya da arma yok (büyütülmüş G8'de elle)
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + OPENING NIGHT   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ            G8 tam kare — sahip kararı
ⓒ METİNSİZ             ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (kırpmalar PROVA'dır — kapak_prova.py).
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/marka/kulüp adı yok · ≤ 40 karakter.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     Empty Concrete Bowl to Opening Night       (36)   ⭐ sahibin paketinin başlığı
② SORU   Will This Empty Concrete Bowl Ever Fill?   (40)   ⭐ planın MERAK SORUSU
③ KISA   From Bare Concrete to a Full House         (34)   ⭐ ajan önerisi
```

> ① sonucu söyler; ② merak sorusunu söyler (KILAVUZ_REHBERI §6: "BAŞLIK soruyu söyler"); ③ kısa ve yaylı — karar sahibin. Üçü de
> 40 karakterin altında ya da sınırında. Kapak kartının metni her durumda film adı "OPENING NIGHT" kalır.
> ⛔ Paketin alternatifi "Stadium Opening Night in 64 Seconds" ALINMADI: sayı yemi kuralına aykırı ve paylaşılan 2x kopya 32 sn'dir — başlık
> yanlış olurdu.

**Açıklama:**

```
An empty concrete stadium at dawn: bare grey terraces, an earth pitch, not a single seat.
Crews roll out the turf, bolt in the red and yellow seats row by row, raise the lights
and mark the pitch. Then the gates open.

Weeks of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real stadium, no real club, no real place, no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #stadium #football #openingnight #fitout
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). "before/after" etiketi bilerek YOK (sahip kuralı 19.09.2026). Altbilginin iki dilli
> beyanı SİLİNMEZ, KISALTILMAZ; "no real club" bu filme eklendi (paketin gerçek kulüp kuralı). Açıklama ışığın yanışını ve kıvılcımı ANMAZ
> ("Then the gates open.") — spoiler bütçesi. "Weeks of work" sahneler arası takvim atlamasının beyanıdır (plan TASARIM ⑪).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
stadium timelapse, stadium construction, football stadium, opening night, stadium seats installation, turf installation, construction timelapse, ai timelapse, ai video, timelapse, stadum timelapse, stadium timelaps
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("stadum timelapse" · "stadium timelaps" bu yüzden bilerek var). Gerçek yer/firma/marka/kulüp adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Stadium pitches are often laid from large rolls of turf grown elsewhere, unrolled strip by strip with tight joints and then rolled so the
roots knit into the base. The light and dark stripes are not two kinds of grass: the mower bends the blades toward or away from you, and
they catch the light differently.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("often"); belirli ürün, ölçü, süre ya da stadyum iddia
> edilmez (ÇIKARIM, genel bilgi). Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | açılış gecesi (①), bir soru (②), bir yay (③) | nasıl, hangi sırayla, ışığın anı |
| kapak | dolu, ışıklı stadyum + başlık | boş çanak, çim/koltuk cepheleri, kalabalığın girişi, projektörlerin yanışı |
| ilk 2 sn | şafakta boş gri çanak, toprak saha, ilk çim şeridi ve onu açan yükleyici | çanağın neye dönüşeceği |
| açıklama | çim, kırmızı-sarı koltuklar, ışıklar, çizgi, "kapılar açılır" | kalabalığın taşması, projektörlerin yanışı, kıvılcım |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (alacakaranlıkta projektörler tek karede yanar, kıvılcım bir kez geçer) kapak dışında
söyleyemez → ✅ (taslak; kurgudan sonra tekrar). ⚠️ Kapak yanık ışığı gösterir; YANIŞ ANI yine saklıdır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: KÜTLE ailesi — COLOSSUS (beton çanak → stadyum, ışıklı final), THE LAST LIFT (stadyum) ve GAME ON (saha çizgisi, ışık) ile
   ARDIŞIK YAYINLANAMAZ [YAYIN_PLANI §3].
