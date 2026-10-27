# 🖼️ THE MENDED SPAN — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7·b'nin 60,0–64,0 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ — YIKIK KÖPRÜ KAPAKTA HİÇ GÖRÜNMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⛔ Paketin "başlık üst üçte birde, gökyüzünde" yerleşimi UYGULANMAZ: y < 560 yasak bölge (sahip kuralı · DERS 94); bu kamerada
              gök bandı (0–345) zaten yasak bölgede. Başlık köprünün ÖNÜNDEKİ sakin suda (A bandı).
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 63.5 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99] — A bandı sakin değilse G8 yeniden üretilir
METİN      THE MENDED SPAN  (3 kelime · kademe: küçük THE + tek satır MENDED SPAN · İngilizce · film adı)
```

### 🎨 STİL KARTI [KAPAK_STIL_KILAVUZU §7]

```
STİL KARTI  [KAPAK_STIL_KILAVUZU]
BANT        A · y 1060–1240 · x 240–840 · sakin alan: köprünün ÖNÜNDEKİ açık su (kameradan 163–229 m)
            ⭐ neden A: Ü bandını (560–770) karşı kule, kablo kavisi ve tabliye keser; O bandını (860–1060) yakın kulenin dibi, burun ve
            lamba yansımaları keser. A bandı lamba yansımalarının ALTINDA (en alt yansıma py 1024 · 36 px pay) [plan TASARIM ②]
IŞIK        reçete R3 (tek parlak kanıt: geç mavi saat, yalnız lambalı tabliye ışıklı, başlığın arkası koyu düz su) · varyant I0 (G8'in
            kendisi; ileri saat yok)
STİL        S3 kademe — küçük "THE" (ana satırın %35–45'i), altında "MENDED SPAN" · yazı tipi Anton (varsayılan · ⚠️ kanal yazı tipi sahip
            kararı bekliyor) · renk #E8E4DC · vurgu kelimesi — (S2 adayı "MENDED", bkz. §5 ⓓ)
METİN       THE MENDED SPAN (3 kelime · kademe: 2 satır) · büyük harf ⬜ px (≥ 78) — "MENDED SPAN" 11 karakter, Anton'da 600 px'e ≈ 80–85 px
            büyük harf sığar (TAHMİN — ölçülür; 78'in altına düşerse S4'e: "MENDED" / "SPAN", THE yine küçük üstte)
KONTRAST    ⬜:1 (≥ 4,5 · koyu su üstünde #E8E4DC yüksek beklenir) · koyu geçiş beklenmez · opaklık —
KANIT       zincir_kontrol ⬜ · nirengi ⬜ px · nesne sayımı ⬜ (köprü 1 · araba 1)
PROVA       PROVA_PANOSU ⬜ · 1:1 başlık tam ⬜ · 140 px üç soru ⬜
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   gece, yüksekten bir asma köprü: solda kayalık burnun üstünde boylu boyunca koyu gri kule, ondan sağ üste karşı kuleye
                  uzanan iki sıra sıcak beyaz lamba · uzun kavisli iki kablo ve ince askılar · kulenin portalından çıkmış TEK arabanın farları ·
                  altta koyu, sakin su (başlık) · üstte derin mavi gök, karşıda birkaç sıcak pencere
BAŞLIKTA YAZAN    THE MENDED SPAN

KANCA             "bu köprü neden onarıldı?" — başlık "onarılmış açıklık" der; kapak bitmiş, ışıklı köprüyü gösterir, görünmeyen şey KIRIKLIKTIR
                  (suya düşmüş tabliye, kopuk kablolar). Merak "ne olacak?"tan "ne oldu?"ya kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ LAMBALI TABLİYE — kadrajın en parlak şeyi, kuleden kuleye tek köşegen ışık çizgisi; 140 px'te bile "ışıklı köprü" okunur
                  [P3-b: kontrast].
İKİNCİ OKUMA      tek araba farları: "açıldı, ilk kez geçiliyor"
ÜÇÜNCÜ OKUMA      kule + kablo kavisi: "asma köprü"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① şafakta iki kule arasında boşluk ve sudan kalkan kırık çelik ② yürüme yollarının ve kabloların kuleden kuleye açılışı ③ tabliyenin
   ortadan iki kuleye asılması ve kapanışı.
⛔ Kapak G7 DEĞİLDİR: G7'de lambalar sönük, araba yok, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
⛔ Kapakta gerçek köprü, boğaz ya da kent ima eden hiçbir öğe YOKTUR (plan TESLİM YAPISI · kurgusallık kuralı).
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   derin mavi gök                         0–345      ⛔ yasak bölge (y < 560) — başlık YOK
   karşı tepelerin sırtı (sağ)            345–360    x 560–1080
   ufuk (solda açık boğaz)                390
   ⭐ karşı kule                           419–614    x 830–878 (tepe 1:1 kırpma çizgisinde — SINIRDA)
   ⭐ yakın kule + üç çapraz bağ           455–869    x 64–189
   ⭐ lambalı tabliye (köşegen)            706 → 534  yakın kuleden karşı kuleye · kablolar 455 → 577 → 419
   ⭐ ilk araba                            ≈ 664      x ≈ 298
   karşı kıyı çizgisi + pencereler        568–602    x 465–860
   köprünün altındaki su + kısa yansımalar 614–1024  (yansımaların en alt ucu py 1024, x ≥ 240)
   kayalık burun                          851–869    x 109–202
   ⭐ BAŞLIK BANDI A                       1060–1240  x 240–840 — köprünün önündeki koyu, sakin su
   açık su                                1240–1510
   kameranın altındaki yamaç              1510–1920  — alt UI bandı (1440–1920) yardımcı doku: koyu çalı ve kaya

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · lambalı tabliye ✅ (karşı ucu py 534 — çekirdeğin 6 px üstü) · ilk araba ✅ ·
   yakın kule ⚠️ (x 64–189: çekirdeğin sol kenarını taşar; 1:1'de tam)
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, yakın kuleyi, tabliyeyi, arabayı taşır — karşı kulenin tepesi (419) çizgide · 4:5 (285–1635) ve
   3:4 (240–1680) daha çok gök ve yamaç taşır.
⚠️ Lamba yansıması bandın 36 px üstünde biter (durgun su HESABI) — gerçek suda dalgacık yansımayı aşağı uzatır; G8 METİNSİZ provada A bandı
   (240–840 × 1060–1240) ölçülür: medyan koyu, içinde parlak çizgi yoksa geçer [plan RİSK ⑦].
⚠️ Yakın kulenin yansıması py 1191'e iner ama x 164–227'de — bandın SOLUNDA (x < 240); başlık x 240'tan başlar, örtmez.
```

## 3. Metin — KAPAK_STIL_KILAVUZU §4 ölçüleriyle

```
METİN      THE MENDED SPAN — S3 KADEME, ORTALI (eksen x = 540)
           küçük "THE" (büyük harf ≈ 30–36 px) üstte · "MENDED SPAN" tek satır altta
YER        ⭐ A bandı x 240–840 · y 1060–1240 — köprünün önündeki koyu, sakin su · yazı yansımaları ve kuleyi örtmez · "THE" satırı y ≈ 1085–1120,
           ana satır y ≈ 1130–1215
PUNTO      "MENDED SPAN" bandın %80–100'ünü doldurur (480–600 px) · büyük harf ≥ 78 px [KAPAK_STIL §4.3] · gerçek yazı sınırları 600 × 180'i
           AŞMAZ, aşarsa punto küçülür → 78'in altına düşerse S4 ("MENDED" / "SPAN") · harf aralığı daraltılmaz · tek ağırlık · parlama YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan koyu su → kontrast yüksek beklenir; ölçülür (KAPAK_STIL §4.4 betiği, bant
           240 1060 840 1240), 4,5:1'i geçmezse başlığın arkasına ölçülü koyu geçiş
⛔ Başka kelime yok: "AI" · "timelapse" · "bridge" · "before/after" · sayı kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada yalnız koyu yamaç var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "ışıklı köprü" ayrışıyor mu ⓑ THE MENDED SPAN okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "iki kule arasında boşluk, suda kırık çelik" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, yakın kule + tabliye + araba TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "gece, ışıklı köprü, ilk araba" diyor mu — "kart-postal", "render", "oyun ekranı" diyorsa G8 yeniden;
               kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki köprü = finaldeki köprü [MUZIK_VE_KAPAK §5]
⑦ KURGUSALLIK  büyütülmüş G8'de karşı kıyı: kent silueti, tanınır kule, ikinci köprü YOK · teknede/tabelada okunur yazı YOK
```

## 5. Varyantlar [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + THE MENDED SPAN (S3)   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ                   G8 tam kare — sahip kararı
ⓒ METİNSİZ                    ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
ⓓ S2 DENEMESİ (isteğe bağlı)  "MENDED" amber #F2A03D (dönüşüm sıfatı) — yalnız kontrast ölçümü geçerse; tek stil seçilir, kart ile kapak
                              AYNI stilde kalır (sahip kararı)
⛔ HEPSİ YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (kırpmalar PROVA'dır — kapak_prova.py).
⛔ A bandı G8'de tutmazsa: önce G8 yeniden (daha durgun su) → olmazsa ışık varyantı I1 (mavi saat, gök daha açık) SAHİBE SORULUR — başlık
   yansımanın üstüne "sığdırılmaz" [plan RİSK ⑦].
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse (paketteki "BUILDWAKE" kanal adı DEĞİLDİR).
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/marka/köprü/boğaz adı yok · ≤ 40 karakter.
⛔ Gerçek bir felaketi ima eden başlık YOK — köprü kurgusaldır.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     A Broken Bridge Rebuilt, Span by Span      (37)   ⭐ ajan önerisi — paketin vaadi, felaket kelimesi olmadan
② SORU   Will This Wreck Become a Bridge Again?     (38)   ⭐ planın MERAK SORUSU
③ KISA   From Broken Span to First Car              (29)   ⭐ ajan önerisi — finalin kendisi
```

> ① sonucu söyler; ② merak sorusunu söyler (KILAVUZ_REHBERI §6: "BAŞLIK soruyu söyler"); ③ kısa ve yaylı — karar sahibin. Üçü de
> 40 karakterin altında. Kapak kartının metni her durumda film adı "THE MENDED SPAN" kalır.
> ⚠️ Paketin başlıkları ALINMADI, sahibe aday olarak bırakıldı:
> · "Collapsed Bridge Rebuilt Over the Strait" (40) — "Collapsed" + "Strait" Türk izleyicide Boğaz'daki gerçek köprüleri çağırır;
>   fotogerçekçi bir yıkık köprü karesiyle birleşince gerçek bir felaket haberi gibi okunabilir. Kapak yıkığı göstermese de ilk 2 sn
>   gösterir. ÖNERİLMEZ.
> · "From Wreck to Night Traffic" (27) — finalde trafik yok, tek araba var (sahip seçimi); başlık yanlış olur.

**Açıklama:**

```
Dawn over a strait: two bare towers stand, and the span between them lies broken in the water.
A floating crane lifts the steel out, walkways are strung from tower to tower, the cables
are spun, and a new deck is hung segment by segment until the gap closes. Then night falls.

Months of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is a fictional bridge, not a record of a real project:
no real bridge, no real strait, no real place, no real event and no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Köprü kurgusaldır; gerçek bir köprüyü, yeri ya da olayı belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #bridge #suspensionbridge #bridgeconstruction #engineering
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). "before/after" etiketi bilerek YOK (sahip kuralı 19.09.2026). Altbilginin iki dilli
> beyanı SİLİNMEZ, KISALTILMAZ; "fictional bridge · no real strait · no real event" bu filme eklendi (paketin "Fictional bridge, AI-generated
> concept" notu, kanal adıyla değil). Açıklama lambaların yanışını ve ilk arabayı ANMAZ ("Then night falls.") — spoiler bütçesi.
> "Months of work" sahneler arası takvim atlamasının beyanıdır (plan IŞIK GÜNÜ · TAKVİM).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
bridge timelapse, suspension bridge construction, bridge construction, bridge rebuild, cable spinning, bridge deck lifting, construction timelapse, ai timelapse, ai video, timelapse, brige timelapse, bridge timelaps
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("brige timelapse" · "bridge timelaps" bu yüzden bilerek var). Gerçek yer/firma/marka/köprü adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
The main cables of a suspension bridge are often not lifted into place in one piece: they are spun in the air. A wheel runs back and
forth along a temporary walkway between the towers, laying one wire on each trip, and thousands of wires are then squeezed into one round
cable. The deck usually comes last, lifted in segments from barges below and hung from the cables.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("often" · "usually"); belirli köprü, ölçü, süre iddia edilmez
> (ÇIKARIM, genel bilgi — havada eğirme yöntemi; bazı köprülerde hazır halat demetleri de kullanılır). Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | onarılmış köprü (①), bir soru (②), ilk araba (③) | nasıl, hangi sırayla, ışığın anı |
| kapak | ışıklı, bitmiş köprü + ilk araba + başlık | kırık açıklık, yürüme yolları, kablo eğirme, tabliyenin kapanışı, lambaların yanışı |
| ilk 2 sn | şafakta iki kule, boşluk, kopuk kablolar, sudan kalkan kırık çelik | açıklığın nasıl kapanacağı |
| açıklama | vinç, yürüme yolları, kablolar, segment segment tabliye, "boşluk kapanır" | lambaların yanışı, ilk araba |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (alacakaranlıkta lambalar tek karede yanar, ilk araba portaldan çıkar) kapak dışında
söyleyemez → ✅ (taslak; kurgudan sonra tekrar). ⚠️ Kapak yanık ışığı ve arabayı gösterir; YANIŞ ANI ve arabanın ÇIKIŞI yine saklıdır.
⚠️ ③ başlığı ("… to First Car") finali söyler — seçilirse spoiler bütçesi bilerek harcanır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6]. Bu filmde ZORUNLU ve
öncelikli: gerçekçi bir yıkık köprü görüntüsü içerir.
⛔ Yayın sırası: DİKEY ailesi — THE CROSSING (deniz, köprü, kapanış), THE CLOSING SPAN, THE IRON BRIDGE (köprü), THE SWALLOWED BUS (felaketten
   onarım), LIT AGAIN (harabeden ışıklı final) ve THE OPENING NIGHT (ışık finali) ile ARDIŞIK YAYINLANAMAZ [YAYIN_PLANI §3].
