# 🖼️ THE SWALLOWED BUS — KAPAK

```
⛔ FİLMDE KAPAK KARTI YOKTUR. Logo yok, kart yok. Bu dosya yalnız platforma YÜKLENEN
   küçük resmi tanımlar; teslim videosunun sonuna hiçbir şey eklenmez [TESLİM YAPISI].
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G7 — S6'nın hedef karesi, filmin SON karesi [DERS 30 · MUZIK_VE_KAPAK §2.2]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026, bütün
              timelapse'ler için geçerli. Kapak tek kare, tek durum, tek kanıt.
KANIT      bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
BAŞLIK     A Bus Fell Into This Street. By Evening Another One Drove Over It | AI Timelapse
           (öneri — sahip onayı bekliyor; ⛔ İNGİLİZCE, PAKETLEME §10)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA VİRAL — çelişki kancası

```
KAPAKTA GÖRÜNEN   düz bir cadde · ortasında simsiyah bir yama · üstünde beyaz çizgi · sol kenarda
                  çıkan otobüsün arkası · turuncu akşam ışığı · tek figür sırtı dönük
BAŞLIKTA YAZAN    THE SWALLOWED BUS

KANCA = ÇELİŞKİ   Başlık "yutulmuş otobüs" der; resimde otobüs yolun ÜSTÜNDE ve gidiyor,
                  yol bütün. İzleyicinin sorusu kapakta doğar: "Nerede yutuldu? Bu çukur
                  neredeydi?" — cevabı yalnız film verir. Öncesi/sonrası bölmede bu soru
                  kapakta CEVAPLANIR ve tıklama sebebi kalmaz; tek karede soru AÇIK kalır.
KANIT NESNESİ     yama: karenin en koyu şeyi ("the scar of the patch is the darkest thing in
                  the frame" — G7 promptu). Yamanın 8 × 6 m'lik dikdörtgeni "burada bir şey
                  oldu" izidir; 120 px'te bile siyah leke olarak kalır.
İKİNCİ OKUMA      otobüs yamanın ötesinde, arka teker dikişin 2 m gerisinde: "geçti" —
                  kapak vaadi filmin finaliyle birebir aynı [MUZIK_VE_KAPAK §5].

⛔ Kapak "çöken otobüs" GÖSTERMEZ, "çukur" GÖSTERMEZ, kırmızı ok / çember / alev YOKTUR
   [MUZIK_VE_KAPAK §4.4 · KANAL_KIMLIGI palet]. Şok efekt yerine çelişki: gerçeklik beyanıyla
   uyumlu tek viral yol budur [§3.2].
⛔ Tıklatıp tutmayan kapak kaybeder [§4.3]: kapağın vaat ettiği tek şey (yama otobüs taşıdı)
   S6'da 8 saniye boyunca gerçek hızda görünür — spoiler bütçesi aşılmaz, vaat boşa çıkmaz.
```

## 2. Yerleşim — G7 tam kare, kırpma yok

```
KAYNAK DOSYA   G7 usta kare çıktısı (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz
⛔ Kapak için ayrı görsel ÜRETİLMEZ; G7'nin kendisidir. Ayrı üretilen kapak başka cadde
   çıkarır [DERS 30]. Kadraj HOME'dur: kenarlar G7 ile aynı → zincir_kontrol geçer.
⛔ Yakınlaştırma / kırpma yok: SSIM kenar şeritlerini ölçer; kırpılmış kare "başka yer" okunur.

KARE İÇİNDE NE NEREDE (alttan % · G7 kilitleri):
   yama              x %22,1–59,3 · y %36,2–49,2  → üstten y ≈ 975–1225 px · en 402 px
   beyaz şerit       yamanın ortasından soldan sağa
   otobüs arkası     sol kenar · x %0–31,1 · y ≈ %34–46 → üstten y ≈ 1040–1270 px
   figür + çınar     x %24,5 · dip y %59 (üstten ≈ 790 px)
   kemerli giriş     x %60,4 · y %61–67          trafik lambası  x %73,7 · y %56–70
   cephe             y %61–100 = üstten 0–749 px · turuncu ışık, balkon gölgeleri sağa
   yakın şeritler    y %0–36 = üstten 1225–1920 px · boş asfalt, iz ve mıcır
KANIT KUTUSU   x %11–78 · y %25–87 → yama ve otobüs arkası kutunun İÇİNDE ✅
```

## 3. Metin

```
METİN      THE / SWALLOWED / BUS    (3 kelime · ÜÇ satır · 0–3 kelime kuralı [MUZIK_VE_KAPAK §2.3])
           ⛔ Başka kelime yok: "sinkhole" · "sewer" · "repair" gibi bilgi isteyen kelime
              kapağa girmez [P6]. Çelişkiyi "swallowed" tek başına kurar.
YER        ⭐ CEPHE BANDI · üstten y 80–640 px (kat 3–5 · %82'nin ÜSTÜ ve çevresi) · sol hizalı,
           sol kenardan 90 px · sağ kenara 90 px kalır → 900 px yazı alanı
           ⛔ Yamanın üstüne (üstten 975–1225) ve otobüsün üstüne (1040–1270) HİÇ inmez.
           ⛔ Kemerli giriş (üstten ≈ 630–750 px, x %60) ve çınar tepesi (x %15–35, üstten
              ≈ 350–790) metnin ALTINDA kalır; metin 640'ta biter.
PUNTO      ⭐ büyük harf yüksekliği 154 px (kare boyunun %8'i — 120 px'te ≈ 10 px kalır [§2.3])
           satır aralığı 40 px → 3 × 154 + 2 × 40 = 542 px → y 80–622 ✅
           dar (condensed) kalın sans-serif · tek ağırlık · geniş harf aralığı
           "SWALLOWED" 9 harf × ≈ 0,6 × 154 ≈ 830 px < 900 ✅ — dar kesim ŞART, geniş kesim taşar
RENK       beyaz #E8E4DC [KANAL_KIMLIGI palet] · arkasında DÜZ antrasit bant #101315 · %85
           opaklık · gradyan yok, kontur yok, gölge yok, parlama yok [§2.3]
           Sebep: cephe turuncu ışıkta açık renktir; çıplak beyaz 4,5:1'i tutmaz.
           Bant metin kutusundan 40 px taşar: x 50–940 · y 40–662 (üstten)
⛔ AMBER KULLANILMAZ: karede zaten turuncu akşam ışığı var; ikinci vurgu vurguyu öldürür.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketinin bandı (≈120 × 35 px) [MUZIK_VE_KAPAK §4.2].
   Sağ alt köşe yakın şerittir (alt %25), boş asfalt; kanıt taşımaz.
```

## 4. Testler — geçmeden yüklenmez

```
① 120 PX       sips -Z 120 kapak.png → ⓐ siyah yama düz caddede LEKE olarak kalıyor mu
               ⓑ üç kelime KELİME ŞEKLİ olarak ayırt ediliyor mu (harf değil)
② SAĞ ALT      köşeye siyah kutu koy: kaybolan bir şey var mı [MUZIK_VE_KAPAK §4.2]
③ ⭐ ÇELİŞKİ    kapağa 3 sn bakan biri "otobüs nerede yutuldu?" diye soruyor mu — sormuyorsa
               yama yeterince koyu değildir → G7 yeniden (kapak yeniden ÇERÇEVELENMEZ [§2.5])
④ KAPAK KANITI zincir_kontrol.sh g7_kaynak.jpg kapak.png [DERS 30] — ⓒ varyantla koşulur
               (metinsiz); ⓐ'da bant üst %32'yi kapatır, kenar SSIM'i düşürür; beklenir
⑤ KARANLIK MOD koyu temada yama ile eski asfalt ayrışıyor mu (yama daha siyah, dikiş açık
               renk, beyaz şerit parlak — ayrışma dikiş + şeritten okunur)
⑥ OTOBÜS       sol kenarda otobüsün ARKASI ve arka tekerin dikişin batısında olduğu görünüyor mu
               — "geçti" tek kanıt budur; otobüs yamanın ÜSTÜNDE ise kapak final değildir
⑦ ÜÇ NOKTA     açılış karesi (G0: otobüs çukurda) · final (G7) · kapak (G7 + metin) yan yana:
               kapaktaki yapı = finaldeki yapı, fazlası yok eksiği yok [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant — A/B için hazır [MUZIK_VE_KAPAK §4.3]

```
ⓐ G7 + BAŞLIK        yukarıdaki yerleşim · ANA VARYANT · tam kare
ⓑ BEDELİN NESNESİ    G7'nin 4K çıktısından 1080 × 1920 1:1 KIRPMA (2× yakın plan, ölçekleme
                     yok): merkez = yama + otobüsün arka tekeri (x %0–50 · y %25–75 bandı);
                     siyah yama, beyaz şerit, teker izi, dikişteki mıcır · metin yok
                     ⚠️ kırpma zincir_kontrol'den geçmez — bu varyantın kanıtı gözle: yama
                        dikişleri ve beyaz şerit G7 ile aynı mı
ⓒ METİNSİZ           G7 tam kare · turuncu ışıkta siyah yama, beyaz çizgi, sol kenarda otobüs
                     arkası · zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G7'DEN TÜRER. G0 hiçbir varyantta yoktur; öncesi/sonrası yoktur.
⚠️ Kısa dikey formatta platform A/B aracı ÇALIŞMAZ [A17-c]; üçü hazır durur.
```
