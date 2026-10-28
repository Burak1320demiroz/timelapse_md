# 🖼️ THE HIDDEN LAWN — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7·b'nin tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ Paketin "kapak G7'den (açık kapak, içeri ışıklı)" önerisi UYGULANMAZ — kapak yalnız GN'den (sahip kuralı 19.09.2026); onun yerine
              finalin kendisi okunur kılındı: kapak bir karış ARALIK, ince ışık çizgisi + çimde ışık havuzu (sahip seçimi "Kapak aralık, ışık
              kaması").
           ⛔ G0 kapağa GİRMEZ — ipli kare, çukur, makineler KAPAKTA HİÇ GÖRÜNMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 63.5 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99] — Ü bandı sakin değilse G8 yeniden üretilir
METİN      THE HIDDEN LAWN  (3 kelime · kademe: küçük THE + tek satır HIDDEN LAWN · İngilizce · film adı)
```

### 🎨 STİL KARTI [KAPAK_STIL_KILAVUZU §7]

```
STİL KARTI  [KAPAK_STIL_KILAVUZU]
BANT        Ü · y 560–770 · x 180–900 · sakin alan: kapağın ÜSTÜNDEKİ arka çim (kameradan 11,5–19,1 m)
            ⭐ neden Ü: O bandını (860–1060) kapak (1095–1180) ve boru (908–1022) sınırlar, kaplar; A bandını (1060–1240) kapak, aralık çizgisi
            ve ışık havuzu doldurur. Ü bandı G7'den itibaren düz yeni çim; elma gövdesi (x ≈ 165), kapı (x ≈ 985), çit dibi (py 545) bandın
            DIŞINDA [plan DEĞİŞMEZLER · BAŞLIK ZEMİNİ]
IŞIK        reçete R3 (tek parlak kanıt: mavi saat, yalnız aralık çizgisi + ışık havuzu ışıklı, başlığın arkası koyu düz çim) · varyant I0 (G8'in
            kendisi; ileri saat yok)
STİL        S3 kademe — küçük "THE" (ana satırın %35–45'i), altında "HIDDEN LAWN" · yazı tipi Anton (varsayılan · ⚠️ kanal yazı tipi sahip
            kararı bekliyor) · renk #E8E4DC · vurgu kelimesi — (S2 adayı "HIDDEN", bkz. §5 ⓓ)
METİN       THE HIDDEN LAWN (3 kelime · kademe: 2 satır) · büyük harf ⬜ px (≥ 78) — "HIDDEN LAWN" 11 karakter, Anton'da 720 px'e ≈ 95–105 px
            büyük harf sığar (TAHMİN — ölçülür)
KONTRAST    ⬜:1 (≥ 4,5 · mavi saatte koyu çim üstünde #E8E4DC yüksek beklenir) · koyu geçiş beklenmez · opaklık —
KANIT       zincir_kontrol ⬜ · nirengi ⬜ px · nesne sayımı ⬜ (kapak 1 · boru 1 · insan 0)
PROVA       PROVA_PANOSU ⬜ · 1:1 başlık tam ⬜ · 140 px üç soru ⬜
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi saatte yukarıdan sıradan bir arka bahçe: altta taş patio ve bir bahçe sandalyesi, ortada bütün bir çim; çimin tam
                  ortasında neredeyse kapalı, üstü çimli kare bir kapak — yakın kenarından ince sıcak turuncu bir çizgi ve çime yayılan ılık
                  bir ışık havuzu · yanında kısa gri bir boru · üstte koyu sakin çim (başlık), arka çit, elma ağacı, bungalov çatıları,
                  derin mavi gök şeridi
BAŞLIKTA YAZAN    THE HIDDEN LAWN

KANCA             "çimin altında ne var?" — başlık "gizli çim" der; kapak sıradan bir bahçe gösterir, AMA çimin ortasından ışık sızar. Görünmeyen
                  şey ODADIR. Merak "ne olacak?"tan "orada ne var?"a kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ IŞIK ÇİZGİSİ + HAVUZ — kadrajın en parlak şeyi, koyu çimin ortasında sıcak turuncu tek leke; 140 px'te bile "çimden ışık
                  sızıyor" okunur [P3-b: kontrast].
İKİNCİ OKUMA      kare kapak + boru: "altında bir oda var"
ÜÇÜNCÜ OKUMA      sandalye + patio + çit: "sıradan bir ev bahçesi"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu ima eder, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① iki adam boyu çukur ve dipteki beton ② blok duvarlar ve kapanan döşeme ③ odanın toprakla gömülüp çimin geri dönmesi.
⛔ Kapak G7 DEĞİLDİR: G7'de ağız karanlık, ışık yok, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
⛔ Kapakta askerî beton, zırhlı kapı, kamuflaj ya da "kıyamet sığınağı" ima eden hiçbir öğe YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   derin mavi gök şeridi                  0–111      ⛔ yasak bölge (y < 560) — başlık YOK
   bungalov çatıları + arka duvarları     111–419
   ⭐ elma ağacı tepesi (sol)              96–442     x −68…304
   ⭐ arka çit                             419–545    x 163–917
   ⭐ BAŞLIK BANDI Ü                       560–770    x 180–900 — kapağın üstündeki koyu, sakin arka çim
   elma gövdesi · kapı                    442–602 · 520–660   x ≈ 165 · x ≈ 985–1011 (bandın DIŞINDA)
   orta çim (yeni rulo derzleri)          770–1095
   ⭐ boru                                 908–1022   x 715–726
   ⭐ kapak + aralık çizgisi               1095–1180  x 471–609 · çizgi py ≈ 1164
   ⭐ ışık havuzu                          1180–1312  x ≈ 470–610
   yakın çim                              1312–1613
   patio + sandalye                       1613–1920  — alt UI bandı (1440–1920) yardımcı doku: taş derzleri, sandalye (x ≈ 218)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · kapak + çizgi ✅ · ışık havuzu ✅ · boru ✅ · arka çit ✅
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, kapağı, havuzu, boruyu taşır — çitin tepesi (419) çizgide; patio ve sandalye kırpılır (beyanlı)
   · 4:5 (285–1635) ve 3:4 (240–1680) çatıları ve patio kenarını da taşır.
⚠️ Elma gövdesi bant kenarına 15 px, çit dibi bant üstüne 15 px (HESAP) — G8 METİNSİZ provada Ü bandı (180–900 × 560–770) ölçülür: medyan
   koyu-yeşil, içinde gövde/çit/parlak nokta yoksa geçer [plan RİSK ⑥ · ⑪].
⚠️ Işık havuzu bandın ≈ 410 px ALTINDA (HESAP) — huzme/sütun çizilirse bant bozulur → G8 yeniden [plan RİSK ⑥].
```

## 3. Metin — KAPAK_STIL_KILAVUZU §4 ölçüleriyle

```
METİN      THE HIDDEN LAWN — S3 KADEME, ORTALI (eksen x = 540)
           küçük "THE" (büyük harf ≈ 35–45 px) üstte · "HIDDEN LAWN" tek satır altta
YER        ⭐ Ü bandı x 180–900 · y 560–770 — kapağın üstündeki koyu, sakin çim · yazı kapağı, havuzu, çiti örtmez · "THE" satırı y ≈ 590–635,
           ana satır y ≈ 650–750
PUNTO      "HIDDEN LAWN" bandın %80–100'ünü doldurur (576–720 px) · büyük harf ≥ 78 px [KAPAK_STIL §4.3] · gerçek yazı sınırları 720 × 210'u
           AŞMAZ, aşarsa punto küçülür → 78'in altına düşerse S4 ("HIDDEN" / "LAWN") · harf aralığı daraltılmaz · tek ağırlık · parlama YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan mavi saatte koyu çim → kontrast yüksek beklenir; ölçülür (KAPAK_STIL §4.4 betiği,
           bant 180 560 900 770), 4,5:1'i geçmezse başlığın arkasına ölçülü koyu geçiş
⛔ Başka kelime yok: "AI" · "timelapse" · "bunker" · "secret" · "before/after" · sayı kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada yalnız patio taşları var (kesek paleti G6'dan sonra YOK).
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "çimden ışık sızıyor" ayrışıyor mu ⓑ THE HIDDEN LAWN okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "çimde ipli kare, bir adam, bir makine" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, kapak + çizgi + havuz + boru TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "akşam, bahçe, çimin altından ışık" diyor mu — "lamba", "pencere", "UFO", "render" diyorsa G8 yeniden;
               kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki bahçe = finaldeki bahçe [MUZIK_VE_KAPAK §5]
⑦ KURGUSALLIK  büyütülmüş G8'de kimse yok · big-bag, makine, tabela YOK · çimde cam/kubbe/ikinci kapak YOK
```

## 5. Varyantlar [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + THE HIDDEN LAWN (S3)   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ                   G8 tam kare — sahip kararı
ⓒ METİNSİZ                    ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
ⓓ S2 DENEMESİ (isteğe bağlı)  "HIDDEN" amber #F2A03D (ışık çizgisinin rengi) — yalnız kontrast ölçümü geçerse; tek stil seçilir, kart ile kapak
                              AYNI stilde kalır (sahip kararı)
⛔ HEPSİ YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (kırpmalar PROVA'dır — kapak_prova.py).
⛔ Ü bandı G8'de tutmazsa: önce G8 yeniden (daha düz çim, gövde bant dışında) → olmazsa ışık varyantı I1 (daha geç mavi saat, çizgi daha
   parlak — KAPAK_STIL §3.2) SAHİBE SORULUR.
⚠️ Kart metni yedeği: "UNDER THE LAWN" (S3: küçük "UNDER THE" + "LAWN") — "HIDDEN" THE HIDDEN LOFT · THE HIDDEN OASIS'te de var (plan AÇIK
   KALANLAR ④). Sahip seçer.
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/marka/kişi adı yok · ≤ 40 karakter.
⛔ Gerçek bir kişiyi ya da olayı belgeliyormuş gibi okunan başlık YOK — adam ve bahçe kurgusaldır.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     A Secret Room Under an Ordinary Lawn       (36)   ⭐ ajan önerisi — paketin vaadi, "bunker" kelimesi olmadan
② SORU   What Is He Building Under His Lawn?        (35)   ⭐ planın MERAK SORUSUna yakın ("What is he burying under his lawn?")
③ KISA   Dug, Built, Buried, Back to Lawn           (32)   ⭐ ajan önerisi — filmin omurgası, döngü
```

> ① sonucu ima eder; ② merak sorusunu söyler (KILAVUZ_REHBERI §6: "BAŞLIK soruyu söyler"); ③ kısa ve ritmik — karar sahibin. Üçü de
> 40 karakterin altında. Kapak kartının metni her durumda film adı "THE HIDDEN LAWN" kalır.
> ⚠️ ② "He" ile gerçek bir kişiyi ima eder — "Altered content" beyanıyla kabul edilebilir, ama ① ve ③ bu riski taşımaz.
> ⚠️ Paketin başlıkları ALINMADI, sahibe aday olarak bırakıldı:
> · "He Hid a Bunker Under His Lawn" (30) — "He Hid" gerçek bir kişinin gerçek bir sırrı gibi okunur (haber/ifşa kalıbı); "Bunker" TUR_HARITASI'nın
>   "sığınak / hayatta kalma (yapay zekâ) — keskin düşüş" satırına doğrudan girer (iddia kaynaksız, BİLİNMİYOR). Fotogerçekçi bir bahçeyle
>   birleşince gerçek bir olay gibi algılanabilir. ÖNERİLMEZ.
> · "Secret Backyard Bunker, Dig to Hidden" (37) — "Dig to Hidden" İngilizcede kırık; "Bunker" aynı tür sinyali. ÖNERİLMEZ.

**Açıklama:**

```
Dawn in an ordinary back garden: a square is pegged out in the lawn and the first turf comes up.
A small digger opens a pit twice a man's height, a concrete floor goes in at the bottom, block walls
rise, and a roof closes the room. Then the earth goes back and the lawn is laid again.

Weeks of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is a fictional garden and a fictional builder, not a record of a
real project: no real person, no real place, no real event and no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Bahçe ve adam kurgusaldır; gerçek bir kişiyi, yeri ya da olayı belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #backyard #undergroundroom #excavation #blockwork
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). "before/after" etiketi bilerek YOK (sahip kuralı 19.09.2026). "bunker" etiketi
> bilerek YOK (tür sinyali — plan RİSK ⑰). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ; "fictional builder · no real person" bu filme
> eklendi. Açıklama ışığın yanışını ve kapağın inişini ANMAZ ("the lawn is laid again") — spoiler bütçesi. "Weeks of work" sahneler arası
> takvim atlamasının beyanıdır (plan IŞIK GÜNÜ · TAKVİM).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
backyard timelapse, underground room, hidden room, backyard build, excavation timelapse, block wall, mini excavator, construction timelapse, ai timelapse, ai video, timelapse, backyard timelaps
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("backyard timelaps" bu yüzden bilerek var). Gerçek yer/firma/marka/kişi adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Small rooms below ground are often roofed with a "beam and block" floor rather than one big slab: slim precast concrete joists are laid
across the walls and light blocks are fitted between them, so each piece is light enough to place without a large crane. A waterproof
membrane and a layer of soil usually go on top, and the soil is heavy when wet, so the roof is normally sized by an engineer.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("often" · "usually" · "normally"); belirli ölçü, yük, süre
> iddia edilmez (ÇIKARIM, genel bilgi — kiriş-blok döşeme). Yapım tavsiyesi gibi okunmaması için "kendin yap" dili YOK. Yorum tuzağı
> sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | çimin altında bir oda (①), bir soru (②), sıra (③) | ne kadar derin, nasıl kapandığı, ışığın anı |
| kapak | bütün çim + aralık kapaktan ışık + boru + başlık | çukur, duvarlar, döşeme, gömme, ışığın yanışı, adamın inişi |
| ilk 2 sn | şafakta ipli kare, ilk çim şeridi, tek adam, ekskavatör | ne kazılacağı |
| açıklama | çukur, beton taban, blok duvar, çatı, toprak geri, çim yeniden | ışığın yanışı, kapağın inişi |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (mavi saatte ağız tek karede yanar, adam kapağı üstüne çeker) kapak dışında söyleyemez
→ ✅ (taslak; kurgudan sonra tekrar). ⚠️ Kapak sızan ışığı gösterir; YANIŞ ANI ve kapağın İNİŞİ yine saklıdır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6]. Bu filmde ZORUNLU ve
öncelikli: gerçekçi bir kişinin gerçekçi bir bahçede gizli bir oda inşa ettiği izlenimini verir.
⛔ Yayın sırası: DİKEY ailesi — THE POOL ROOM · THE DEEP END (çukur), THE HIDDEN LOFT (gizli oda, "HIDDEN"), THE MENDED SPAN · THE OPENING NIGHT
   (ışık finali) ile ARDIŞIK YAYINLANAMAZ [YAYIN_PLANI §3].
