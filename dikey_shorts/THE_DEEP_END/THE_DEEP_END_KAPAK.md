# 🖼️ THE DEEP END — KAPAK

```
⛔ FİLMDE KAPAK KARTI YOKTUR. Logo yok, kart yok, müzik yok. Bu dosya yalnız platforma YÜKLENEN
   küçük resmi tanımlar; teslim videosunun sonuna hiçbir şey eklenmez [TESLİM YAPISI].
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G7 — S6'nın hedef karesi, filmin SON karesi [DERS 30 · MUZIK_VE_KAPAK §2.2]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026, bütün
              timelapse'ler için geçerli. Kapak tek kare, tek durum, tek kanıt.
KANIT      bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
BAŞLIK     An Abandoned Pool Becomes a Hidden Cinema | AI Timelapse
           (öneri — sahip onayı bekliyor; ⛔ İNGİLİZCE, PAKETLEME §10)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA VİRAL — çelişki kancası

```
KAPAKTA GÖRÜNEN   karanlık bir bahçede, ZEMİNİN ALTINDA yanan bir oda: dört ahşap kademe, her kenarında sıcak amber
                  çizgi · uzak duvarda parlayan perdede sakin gri-mavi deniz · havuz boyunca uzanan soluk huzme ·
                  kademe 2'de sırtı dönük tek figür · coping'in altında kesintisiz TURKUAZ FAYANS BANDI ·
                  üstte çimende yatan TRAMPLEN · üst bantta siyah karaçamlar
BAŞLIKTA YAZAN    THE DEEP END

KANCA = ÇELİŞKİ   Kapakta iki nesne aynı anda okunur ve birbirini yalanlar: TURKUAZ FAYANS + TRAMPLEN "burası bir
                  yüzme havuzu" der; IŞIKLI PERDE + MİNDERLİ KADEMELER "burası bir salon" der. Soru kapakta doğar:
                  "Bir havuzun içine sinema mı yapmışlar? Suyu nereye gitti?" — cevabı yalnız film verir.
                  Başlık da ikinci bir çelişki taşır: "deep end" hem havuzun derin ucu hem "başının üstünde iş".
KANIT NESNESİ     ⭐ TRAMPLEN — kadrajın üst üçte birinde, çimende, 215 px eninde, karanlık çimde SOLUK bir çubuk.
                  120 px'te bile "aşağıda parlayan dikdörtgen + yukarıda yatay soluk çubuk" okunur. Tramplen
                  kapağın ikinci cümlesidir: buranın havuz olduğunu perdeye bakmadan söyler [P3-b: piksel değil,
                  kontrast].
İKİNCİ OKUMA      huzme: projektörden perdeye uzanan soluk koni, karanlıkta tek diyagonal. "Gerçekten film
                  oynuyor" — durağan bir mekân fotoğrafı değil, ÇALIŞAN bir yer.
ÜÇÜNCÜ OKUMA      tek figür: 99 px, sırtı dönük, kademe 2'de. Ölçek verir (kademeler insan boyunda) ve yalnızlık
                  değil MAHREMİYET okutur — "gizli oda".

⛔ Kapak G5 ya da G6 DEĞİLDİR: G5 aydınlıktır ve daha "okunur"dur ama cevabı (perde) taşımaz; G6'da perde vardır
   ama SÖNÜKTÜR ve kare ölü görünür [DERS 30 · sahip kararı: kapak yalnız GN].
⛔ Kırmızı ok / çember / "50 SECONDS" yazısı YOKTUR [MUZIK_VE_KAPAK §4.4 · KANAL_KIMLIGI palet].
⛔ Tıklatıp tutmayan kapak kaybeder [§4.3]: kapağın vaat ettiği tek şey (havuzun içinde sinema) S6'da 8 saniye
   boyunca görünür — spoiler bütçesi aşılmaz, çünkü NASIL olduğu 48 saniyedir.
```

## 2. Yerleşim — G7 tam kare, kırpma yok

```
KAYNAK DOSYA   G7 usta kare çıktısı (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz
⛔ Kapak için ayrı görsel ÜRETİLMEZ; G7'nin kendisidir [DERS 30]. Kadraj HOME'dur → zincir_kontrol geçer.
⛔ Yakınlaştırma / kırpma yok: SSIM kenar şeritlerini ölçer; kırpılmış kare "başka yer" okunur.

KARE İÇİNDE NE NEREDE (alttan % · G7 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   karaçam bandı      y %90,8–100                           → üstten 0–176 px      ⭐ METİN BURAYA
   çit tepesi         y %90,8                               → üstten 176 px
   bahçe duvarı       y %77,0–86,8                          → üstten 253–441 px
   ⭐ tramplen         x %40,1–59,9 · y %74,4                → üstten ≈ 491 px · 215 px en
   ankraj plakası     x %51,9 · y %69,9                     → üstten 579 px
   uzak coping        x %34,5–65,5 · y %69,4                → üstten 588 px
   ⭐ PERDE            x %40,0–60,0 · y %61,8–68,6           → üstten 602–734 px · 208 × 132 px
   kademe 4 nosing    y %61,3                               → üstten 743 px
   kademe 3 nosing    y %56,5                               → üstten 835 px
   kademe 2 nosing    y %49,5                               → üstten 970 px
   ⭐ oturan figür     x %38,7–39,4 · y %42,7–47,8           → üstten 1002–1101 px · 99 px boy
   kademe 1 nosing    y %38,3                               → üstten 1185 px
   projektör          x %74,2–78,6 · y %28,3–31,1           → üstten 1323–1376 px
   krom korkuluk      x %80,2–84,0 · y %17,0–23,5           → üstten 1469–1595 px
   yakın coping       x %10,4–89,6 · y %18,3                → üstten 1569 px
   teras              y %0–18,3                             → üstten 1569–1920 px · karanlık, boş
KANIT KUTUSU   x %10–90 · y %25–87 → perde ✅ · dört nosing ✅ · huzme ✅ · figür ✅ · tramplen ✅ kutunun İÇİNDE
```

## 3. Metin

```
METİN      THE DEEP END    (3 kelime · TEK satır · 0–3 kelime kuralı [MUZIK_VE_KAPAK §2.3])
           ⛔ Başka kelime yok: "pool" · "cinema" · "hidden" gibi CEVABI veren kelime kapağa girmez [P6].
              Çelişkiyi resim kurar; başlık yalnız ikinci anlamı ("deep end") ekler.
YER        ⭐ ÜST BANT — yalnız karaçam kütlesi: çit tepesi üstten 176 px'te. Metin en geç 160 px'te biter →
           çit hattıyla 16 px pay. SOL hizalı, sol kenardan 90 px, 900 px yazı alanı (x 90–990).
           ⛔ Tramplenin (üstten 491) ve duvarın (253) üstüne inmez.
PUNTO      ⭐ büyük harf yüksekliği 120 px (kare boyunun %6,3 — 120 px'te ≈ 8 px kalır [§2.3])
           TEK SATIR → y 40–160 px ✅
           dar (condensed) kalın sans-serif · tek ağırlık · geniş harf aralığı
           "THE DEEP END" 12 harf (boşluk dâhil) × ≈ 0,6 × 120 ≈ 864 px < 900 ✅ — dar kesim ŞART
⭐ BANT GEREKMEZ: arka plan siyaha yakın karaçam kütlesidir (deniz alacasında en koyu alan) ve beyaz metinle
   kontrast 4,5:1'i rahat geçer. Bant konursa kadrajın tek "yapay" öğesi olur — konmaz.
RENK       beyaz #E8E4DC [KANAL_KIMLIGI palet] · gradyan yok, kontur yok, gölge yok, parlama yok [§2.3]
⛔ AMBER KULLANILMAZ: karede zaten dört amber çizgi ve sıcak perde ışığı var; ikinci vurgu vurguyu öldürür.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketinin bandı (≈120 × 35 px) [MUZIK_VE_KAPAK §4.2]. Sağ alt köşe karanlık terastır.
```

## 4. Testler — geçmeden yüklenmez

```
① 120 PX       sips -Z 120 kapak.png → ⓐ "karanlıkta parlayan dikdörtgen + ona inen basamaklar + yukarıda yatay
               soluk çubuk" ayrışıyor mu ⓑ üç kelime KELİME ŞEKLİ olarak ayırt ediliyor mu (harf değil)
② SAĞ ALT      köşeye siyah kutu koy: kaybolan bir şey var mı [MUZIK_VE_KAPAK §4.2] (karanlık teras — hayır)
③ ⭐ ÇELİŞKİ    kapağa 3 sn bakan biri "bu bir havuz mu?" diye soruyor mu — sormuyorsa TURKUAZ BANT ve TRAMPLEN
               yeterince okunmuyordur → G7 yeniden (kapak yeniden ÇERÇEVELENMEZ [§2.5])
④ KAPAK KANITI zincir_kontrol.sh g7_kaynak.jpg kapak.png [DERS 30] — ⓒ varyantla koşulur (metinsiz)
⑤ KARANLIK MOD koyu temada perde ile karaçam bandı, amber çizgiler ile larch, figür ile minder ayrışıyor mu ·
               ⭐ en kritik test: kare "gece fotoğrafı" değil "yanan oda" okunmalı
⑥ ÖLÇEK        oturan figür kademelerin yanında okunuyor mu — okunmazsa çukur "maket" olur; kapak final değildir
⑦ ÜÇ NOKTA     açılış karesi (G0: yeşil su, yaprak salı, tramplen coping'de) · final (G7) · kapak (G7 + metin) yan
               yana: kapaktaki yapı = finaldeki yapı, fazlası yok eksiği yok [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant — A/B için hazır [MUZIK_VE_KAPAK §4.3]

```
ⓐ G7 + BAŞLIK        yukarıdaki yerleşim · ANA VARYANT · tam kare
ⓑ ALT BAŞLIK YOK     G7 tam kare · metin yerine hiçbir şey; yalnız parlayan çukur · ⭐ bu varyant "ne bu?" sorusunu
                     en saf hâlde sorar ama başlıksız kapak arama sonucunda zayıftır — sahip kararı
ⓒ METİNSİZ           G7 tam kare · zincir_kontrol'ün koşulduğu varyant (ⓑ ile aynı görsel, ayrı dosya adı)
⛔ ÜÇÜ DE YALNIZ G7'DEN TÜRER. G0 ve ara kareler hiçbir varyantta yoktur; öncesi/sonrası yoktur.
⛔ KIRPMA VARYANTI YOK: perdeye yakın plan çekmek turkuaz bandı ve trampleni kadrajdan çıkarır — çelişki ölür.
⚠️ Kısa dikey formatta platform A/B aracı ÇALIŞMAZ [A17-c]; üçü hazır durur.
```
