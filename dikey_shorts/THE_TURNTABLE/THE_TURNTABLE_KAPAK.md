# 🖼️ THE TURNTABLE — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99]
METİN      THE TURNTABLE  (2 kelime · tek satır · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   tek nokta perspektifle uzanan bir kaya tüneli: ortada alttan beyaz parlayan buzlu cam platformun üstünde, farları yanık,
                  burnu kameraya dönük koyu grafit bir spor araç · üstte yumuşak beyaz altıgen ışık peteği ve koyu çelik kemer kaburgalar ·
                  sağda cam korkuluklu, sıcak ışıklı loca · solda ışıklı cam vitrinler · alt duvarlarda amber ışık · uzakta mavi saatte
                  açık portal · altta aracı yansıtan parlak koyu zemin · uzak kaya tonoz (başlık)
BAŞLIKTA YAZAN    THE TURNTABLE

KANCA             "bu nasıl yapıldı?" — kapak bitmiş, ışıklı galeriyi gösterir; görünmeyen şey başlangıçtır (karanlık, nemli kaya tüneli,
                  kancada asılı halka). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ IŞIKLI PLATFORM + ARAÇ — kadrajın en parlak şekli, koyu tünelin ortasında beyaz bir elips ve üstünde araç. 140 px'te bile
                  "yeraltında bir araba" okunur [P3-b: kontrast].
İKİNCİ OKUMA      kaya tonoz + çelik kaburgalar: "burası bir mağara"
ÜÇÜNCÜ OKUMA      loca ve vitrinler: "özel bir galeri"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① ham kaya ve kancadaki dev halka ② duvarların, zeminin ve tavanın katman katman gelişi ③ aracın inişi ve ışıkların yandığı an.
⛔ Kapak G7 DEĞİLDİR: G7'de araç rampada, ışıklar sönük, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   ⭐ ışık peteği (yanık)             0–533      x 300–780 uzak kenarda — kutunun ÜSTÜNDE
   uzak kaya tonoz + kaburgalar       495–704    eksende
   ⭐ BAŞLIK KUTUSU                   560–770    x 180–900 (kılavuz §3 "film adı kutusu") — uzak kaya tonoz (566–704) + portalın üstündeki
                                                alın duvarı (704–770) · koyu kaya, koyu çelik kaburgalar
   loca balkonu (sıcak)               640–911    x 706–1080 — kutunun sağ alt köşesine değer (x 706–900 · py 736–770, beyanlı)
   alın duvarı                        704–922    x 351–729
   ⭐ portal (mavi)                    922–1024   x 459–621
   vitrinler                         928–1120   x 108–310
   ⭐ araç                             1059–1292  x 400–680
   ⭐ platform (beyaz)                 1150–1354  x 140–940
   parlak koyu zemin (yansıma)       1354–1920  kadraj boyu
   alt UI bandı                      1440–1920  (zemin — yardımcı doku)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · araç ✅ · platform ✅ · portal ✅ · vitrinler ✅ · loca çekirdeğin sağ kenarında ·
   petek çekirdeğin üstünde — beyanlı
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, portalı, aracı, platformun tamamını ve peteğin uzak kenarını taşır · 4:5 (285–1635) ve 3:4
   (240–1680) peteğin daha çoğunu ve zemindeki yansımayı da taşır.
⚠️ Loca ışığı ve petek halesi başlık kutusuna taşmamalı — G8 elle kontrol, plan RİSK ve PİLOT (a).
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      THE TURNTABLE — TEK SATIR, ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — uzak kaya tonoz ve portalın üstündeki alın duvarı · yazı aracı, platformu ve portalı
           örtmez · satır y ≈ 610–720 (dikey ortası ≈ 665)
PUNTO      "THE TURNTABLE" 13 karakter: 720 px'lik kutuya ≈ 80–90 px yazı boyu sığar (kalın, dar olmayan sans-serif); gerçek yazı sınırları
           720 × 210'u AŞMAZ, aşarsa punto küçülür, harf aralığı daraltılmaz · tek ağırlık · parlama YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan koyu kaya → kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse başlığın arkasına
           ölçülü koyu geçiş [kılavuz §5]
           ⚠️ sağ alt köşede loca ışığı (x 706–900 · py 736–770) — prova metinsiz G8 ile ÖNCE yapılır; ışık yazıya değerse satır yukarı
           alınır (en çok y 570'e kadar — peteğin uzak kenarı 533)
⛔ Başka kelime yok: "AI" · "timelapse" · "supercar" · "VIP" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada parlak zemin var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "ışıklı platform + araç" ayrışıyor mu ⓑ THE TURNTABLE okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "karanlık tünel, kancada halka" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, araç ve platform TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "yeraltında özel bir araba galerisi" diyor mu — "render", "oyun ekranı", "otomobil fuarı" diyorsa G8
               yeniden; kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki araç = finaldeki araç [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + THE TURNTABLE   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ            G8 tam kare — sahip kararı
ⓒ METİNSİZ             ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (kırpmalar PROVA'dır — kapak_prova.py).
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/marka adı yok · ≤ 40 karakter.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     From Rock Tunnel to Car Gallery          (31)   ⭐ sahibin notunun başlığından, kısaltılmış
② SORU   What Will This Giant Ring Become?        (33)   ⭐ planın MERAK SORUSU
③ KISA   The Turntable                            (13)   ⭐ film adı
```

> ① sonucu söyler; ② merak sorusunu söyler (KILAVUZ_REHBERI §6: "BAŞLIK soruyu söyler"); ③ kısa ve gizemli — karar sahibin. Üçü de
> 40 karakterin altında. Notun kendi başlığı ("Yeraltı Kaya Mağarasından Lüks Süper Araç Galerisi ve VIP Lounge'a") Türkçe ve 40'ın
> üstünde; "luxury", "supercar", "VIP" kelimeleri başlığa ALINMADI (vaat şişirmesi · marka çağrışımı).

**Açıklama:**

```
A raw, damp rock tunnel under a hill. A small crane, a scissor lift and a crew of four fit it out stage by stage:
a steel ring sinks into a pit, steel ribs rise against the rock, the walls turn charcoal and the floor turns dark and glossy.
Then the evening comes.

Weeks of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real building, no real car maker, no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #undergroundgarage #interiordesign #cargarage #turntable
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> Açıklama aracı ve ışığı ANMAZ ("Then the evening comes.") — spoiler bütçesi. "Weeks of work" sahneler arası takvim atlamasının
> beyanıdır (plan TASARIM ⑪).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
underground garage, car turntable, rock tunnel, cave garage, garage build, interior fit out, construction timelapse, ai timelapse, ai video, timelapse, the turntable, undergrond garage, car turntabel
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("undergrond garage" · "car turntabel" bu yüzden bilerek var). Gerçek yer/firma/marka adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
A car turntable is usually built around a large slewing ring — the same kind of geared bearing that lets a crane turn — set into a
shallow pit, with a flat deck bolted on top and a small motor driving the gear. In rock caverns the rock is often left partly bare:
it is cleaned, bolted and sealed, and panels go only where people touch the walls or where the echo needs taming.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("usually · often"); belirli ürün, ölçü, yük ya da süre
> iddia edilmez (ÇIKARIM, genel bilgi). Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | tünelden galeriye (①), bir gizem (② ③) | nasıl, hangi sırayla, aracın gelişi |
| kapak | bitmiş, ışıklı galeri + araç + başlık | ham kaya, kancadaki halka, katmanların gelişi, aracın inişi |
| ilk 2 sn | karanlık tünel, kancada dev halka, gün ışıklı portal | halkanın neye dönüşeceği |
| açıklama | mini vinç, makaslı platform, dört kişilik ekip, halka, kaburgalar, kömür duvarlar, koyu zemin, "akşam gelir" | araç, ışıkların yanışı |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (mavi saatte araç rampadan iner, galeri yanar) kapak dışında söyleyemez → ✅
(taslak; kurgudan sonra tekrar). ⚠️ Kapak aracı gösterir; aracın GELİŞİ ve ışık anı yine saklıdır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: İÇ MEKÂN (bekleyen) ailesi — THE SKY VAULT (kömür oda, sıcak ışık), THE HIDDEN LOFT (lounge, ışıklı final), FIRST SLICE
   (garaj) ve UNDERWATER OBSERVATORY (kayaya oyulmuş salon, ışıklı final) ile ARDIŞIK YAYINLANAMAZ [YAYIN_PLANI §3].
