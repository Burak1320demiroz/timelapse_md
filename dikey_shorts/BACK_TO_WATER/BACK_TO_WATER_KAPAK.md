# 🖼️ BACK TO WATER — KAPAK

```
⛔ FİLMDE KAPAK KARTI YOKTUR. Logo yok, kart yok. Bu dosya yalnız platforma YÜKLENEN
   küçük resmi tanımlar; teslim videosunun sonuna hiçbir şey eklenmez [TESLİM YAPISI].
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G7 — S6'nın hedef karesi, filmin SON karesi [DERS 30 · MUZIK_VE_KAPAK §2.2]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026, bütün
              timelapse'ler için geçerli. Sahibin senaryosundaki "ilk karedeki paslı tekne" kapağı
              bu kararla DÜŞTÜ. Kapak tek kare, tek durum, tek kanıt.
KANIT      bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
BAŞLIK     This Rusted Boat Finally Floats Again | AI Timelapse   (proje sahibinin metni · İNGİLİZCE)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA VİRAL — eşik anı + boş havuz

```
KAPAKTA GÖRÜNEN   açık kapının ötesinde, denize çıkmış kırmızı-lacivert tekne · kıçından kapıdan
                  içeri giren beyaz V iz · altında DOLU ve BOŞ havuz: iki beton duvar, koyu gelgit
                  çizgisi, yarısı suda sarı merdiven · turuncu akşam ışığı · tek figür sırtı dönük
BAŞLIKTA YAZAN    BACK TO WATER

KANCA = EŞİK      Tekne ne içeride ne uzakta: kapının hemen ötesinde, izi hâlâ havuza bağlı. Kapak
                  "gidiş anı"dır — izleyicinin sorusu "nereden çıktı, neden oradaydı?"; cevabı
                  yalnız film verir. Öncesi/sonrası bölmede bu soru kapakta CEVAPLANIR ve tıklama
                  sebebi kalmaz; tek karede soru AÇIK kalır.
KANIT NESNESİ     boş havuz: kadrajın alt üçte ikisi. Su altındaki takozlar görünmez ama duvarlar,
                  gelgit çizgisi ve yarısı batmış merdiven "burası kuruydu, burada bir şey vardı"
                  izidir; 120 px'te bile koyu dikdörtgen + sarı çizgi olarak kalır.
İKİNCİ OKUMA      YouTube başlığı "rusted" der, resimdeki tekne pırıl pırıl: ikinci çelişki
                  başlık-kapak arasında — kapak vaadi filmin finaliyle birebir aynı [MUZIK_VE_KAPAK §5].

⛔ Kapak "paslı tekne" GÖSTERMEZ, "kuru havuz" GÖSTERMEZ, kırmızı ok / çember / alev YOKTUR
   [MUZIK_VE_KAPAK §4.4 · KANAL_KIMLIGI palet]. Şok efekt yerine eşik: gerçeklik beyanıyla uyumlu.
⛔ Tıklatıp tutmayan kapak kaybeder [§4.3]: kapağın vaat ettiği tek şey (tekne suda, gidiyor) S6'da
   8 saniye boyunca gerçek hızda görünür — spoiler bütçesi aşılmaz, vaat boşa çıkmaz.
⚠️ TEKNE KAPAKTA KÜÇÜKTÜR (≈ 200 × 270 px): bu bilinerek seçildi — kapağın nesnesi tekne değil,
   teknenin ARKASINDA BIRAKTIĞI havuzdur (BEDEL). 120 px testi ⓐ bunu ölçer.
```

## 2. Yerleşim — G7 tam kare, kırpma yok

```
KAYNAK DOSYA   G7 usta kare çıktısı (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz
⛔ Kapak için ayrı görsel ÜRETİLMEZ; G7'nin kendisidir. Ayrı üretilen kapak başka havuz, başka tekne
   çıkarır [DERS 30]. Kadraj HOME'dur: kenarlar G7 ile aynı → zincir_kontrol geçer.
⛔ Yakınlaştırma / kırpma yok: SSIM kenar şeritlerini ölçer; kırpılmış kare "başka yer" okunur.

KARE İÇİNDE NE NEREDE (alttan % · G7 kilitleri · ⚠️ TÜRETİLMİŞ, ölçülecek):
   tekne (su hattı)  y %61–67 · kabin çatısı %74 · x %26–45      → üstten y ≈ 500–750 px
   iz (V)            kapıdan (y %47) tekneye (y %61) · x %30–45
   kapı kuleleri     x %12 ve %59 · üst kenar y %68
   ufuk              y %80 → üstten 384 px · gök bandı üstten 0–384 px
   havuz suyu        y %13–47 (alt yarı) · duvarlar iki yanda · merdiven x %71 · y %43–60 (üst 3 basamak)
   babalar + halat   batı x %10 · doğu x %68 · y %61
   figür             doğu rıhtımı, x ≈ %66, y ≈ %62, sırtı dönük
KANIT KUTUSU   x %11–78 · y %25–87 → tekne, iz, merdiven, kapı kutunun İÇİNDE ✅
```

## 3. Metin

```
METİN      BACK TO / WATER    (3 kelime · İKİ satır · 0–3 kelime kuralı [MUZIK_VE_KAPAK §2.3])
           ⛔ Başka kelime yok: "dry dock" · "restoration" · "rusted" gibi bilgi isteyen kelime
              kapağa girmez [P6]. Eşiği resim kurar, metin yalnız yönü söyler.
YER        ⭐ GÖK BANDI · üstten y 36–374 px (ufuk 384'ün ÜSTÜNDE) · sol hizalı, sol kenardan 90 px ·
           sağ kenara 90 px kalır → 900 px yazı alanı
           ⛔ Ufkun altına (üstten > 384) İNMEZ; teknenin (üstten 500+) ve kabin çatısının (üstten
              ≈ 500) üstüne HİÇ inmez.
PUNTO      ⭐ büyük harf yüksekliği 154 px (kare boyunun %8'i — 120 px'te ≈ 10 px kalır [§2.3])
           satır aralığı 30 px → 2 × 154 + 30 = 338 px → y 36–374 ✅
           dar (condensed) kalın sans-serif · tek ağırlık · geniş harf aralığı
           "BACK TO" 7 karakter · "WATER" 5 harf × ≈ 0,6 × 154 ≈ 460 px < 900 ✅ — bol yer var;
           istenirse tek satır "BACK TO WATER" 13 karakter ≈ 1200 px ✗ SIĞMAZ → iki satır kalır
RENK       beyaz #E8E4DC [KANAL_KIMLIGI palet] · arkasında DÜZ antrasit bant #101315 · %85 opaklık ·
           gradyan yok, kontur yok, gölge yok, parlama yok [§2.3]
           Sebep: akşam göğü ufka doğru soluk ve sıcak pusludur; çıplak beyaz 4,5:1'i tutmaz.
           Bant metin kutusundan 40 px taşar: x 50–940 · y 0–414 (üstten) — ⚠️ bant ufku 30 px
           örter; kabul (ufuk çapası kapakta değil filmde ölçülür)
           ALTERNATİF: bantsız antrasit #101315 metin; kontrast ölçülüp ≥ 4,5:1 ise tercih edilir
           (gök daha temiz kalır) — ölçüm günlük §5 ⑦'ye yazılır
⛔ AMBER KULLANILMAZ: karede zaten turuncu akşam ışığı var; ikinci vurgu vurguyu öldürür.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketinin bandı (≈120 × 35 px) [MUZIK_VE_KAPAK §4.2].
   Sağ alt köşe havuzun doğu duvarı dibindeki sudur (alt %25); kanıt taşımaz.
```

## 4. Testler — geçmeden yüklenmez

```
① 120 PX       sips -Z 120 kapak.png → ⓐ koyu havuz dikdörtgeni + sarı merdiven çizgisi kalıyor mu;
               tekne parlak denizde koyu LEKE olarak seçiliyor mu ⓑ iki kelime KELİME ŞEKLİ olarak
               ayırt ediliyor mu (harf değil)
② SAĞ ALT      köşeye siyah kutu koy: kaybolan bir şey var mı [MUZIK_VE_KAPAK §4.2]
③ ⭐ EŞİK       kapağa 3 sn bakan biri "tekne nereden çıkıyor?" diye soruyor mu — sormuyorsa iz
               kapıdan içeri okunmuyordur → G7 yeniden (kapak yeniden ÇERÇEVELENMEZ [§2.5])
④ KAPAK KANITI zincir_kontrol.sh g7_kaynak.jpg kapak.png [DERS 30] — ⓒ varyantla koşulur
               (metinsiz); ⓐ'da bant üst %22'yi kapatır, kenar SSIM'i düşürür; beklenir
⑤ KARANLIK MOD koyu temada havuz suyu ile duvarlar ayrışıyor mu (gelgit çizgisi + sarı merdiven
               ayrımı taşır); tekne ile deniz ayrışıyor mu (lacivert borda × turuncu su)
⑥ TEKNE        kıçı eşiğin ÖTESİNDE mi, iz kapıdan İÇERİ giriyor mu — "çıktı" tek kanıt budur;
               tekne kapının içindeyse kapak final değildir
⑦ ÜÇ NOKTA     açılış karesi (G0: kabuklu tekne kuru havuzda) · final (G7) · kapak (G7 + metin) yan
               yana: kapaktaki yapı = finaldeki yapı, fazlası yok eksiği yok [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant — A/B için hazır [MUZIK_VE_KAPAK §4.3]

```
ⓐ G7 + BAŞLIK        yukarıdaki yerleşim · ANA VARYANT · tam kare
ⓑ BEDELİN NESNESİ    G7'nin 4K çıktısından 1080 × 1920 1:1 KIRPMA (2× yakın plan, ölçekleme yok):
                     merkez = BOŞ HAVUZ + açık kapı + iz (x %15–65 · y %30–80 bandı); tekne kadrajın
                     üst kenarında küçük · metin yok
                     ⚠️ kırpma zincir_kontrol'den geçmez — bu varyantın kanıtı gözle: merdiven,
                        kuleler ve iz G7 ile aynı mı
ⓒ METİNSİZ           G7 tam kare · turuncu ışıkta denize çıkmış tekne, kapıdan içeri iz, dolu havuz ·
                     zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G7'DEN TÜRER. G0 hiçbir varyantta yoktur; öncesi/sonrası yoktur.
⚠️ Kısa dikey formatta platform A/B aracı ÇALIŞMAZ [A17-c]; üçü hazır durur.
```

## 6. Paketleme — ⛔ İNGİLİZCE [apexait/youtube/PAKETLEME_SABLONU · proje sahibinin metni]

```
BAŞLIK     This Rusted Boat Finally Floats Again | AI Timelapse
AÇIKLAMA   A rusted fishing boat. An empty dry dock. One chance to return to the water.

           Watch the transformation unfold in 56 seconds, from the first cleaning pass to the
           moment the boat floats and heads out to sea.

           An AI-generated cinematic restoration, told through one fixed camera.

           #Timelapse #BoatRestoration #AIFilm
BEYAN      "AI-generated" açıklamada açık — GERÇEKLİK BEYANI [MUZIK_VE_KAPAK §3.2 · A4]
⚠️ Açıklamadaki "56 seconds" TESLİM SÜRESİYLE birebir olmalı; kart eklenirse (61,0) düzeltilir.
```
