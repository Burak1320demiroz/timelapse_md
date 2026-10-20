# 🖼️ THE HIDDEN LOFT — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⭐ Paketin isteği "G8'in işçisiz finali; pencere, kanepe ve kütüphane birlikte" — G8 tam olarak budur.
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99: RAIN TOWER'da usta kare plandan büyük çıktı, başlık kaydı]
METİN      THE HIDDEN / LOFT  (3 kelime · iki satır · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   altın saatte bir çatı katı salonu: koyu ahşap çatının altında temiz üçgen pencere, dışarıda altın gök önünde
                  çam tepeleri · pencereden içeri yatan uzun, eğik ALTIN IŞIK ÜÇGENİ krem halıda, konyak kanepenin sırtında
                  ve sol duvardaki dolu ceviz rafların alt sıralarında · iki krem berjer, traverten sehpa · sağda soyut tablo,
                  sol köşede zeytin ağacı · oda boş
BAŞLIKTA YAZAN    THE HIDDEN / LOFT

KANCA             "bu çatı katı nasıl bu hâle geldi?" — başlık GİZLİ bir yer vaat eder; kapakta görünmeyen şey başlangıçtır
                  (kirli halı, kirli cam). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ ALTIN ÜÇGEN + KOYU AHŞAP ÇATI — kadrajın en parlak şekli ile en koyu alanı üst üste (y 788–1118 pencere ↔
                  y 0–770 ahşap). 140 px'te bile "ahşap çatının altında güneşli bir oda" okunur [P3-b: kontrast].
İKİNCİ OKUMA      dolu ceviz raflar: "burada birisi okuyacak"
ÜÇÜNCÜ OKUMA      üçgen pencere: çatı katı olduğunun tek işareti, siluetin kendisi

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① kirli halılı, sandıklı ilk oda ② camın beş sahne boyunca kâğıtla kapalı kalması ③ kâğıdın inip güneşin girdiği an.
⛔ Kapak G7 DEĞİLDİR: G7'de kâğıt camda, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   ahşap çatı (eğimler)        0–560      mertekler ve tahta kaplama, aynı koyu ton
   ⭐ BAŞLIK KUTUSU             560–770    x 180–900 (kılavuz §3 "film adı kutusu") — üst alın üçgeni + iki çatı eğimi, KOYU AHŞAP
   mahya (arka)                564        x 540 — kutunun üst kenarı
   ⭐ pencere tepesi            788        x 540 — kutunun 18 px ALTINDA
   kütüphane üstü              830–874    x 82–279
   diz duvarı üstü (köşeler)   854        x 262 / 818
   tablo                       889–1068   x 891–969
   kapı üstü                   907        x 701–802
   zeytin ağacı / lambader     932–1201   x ≈ 299 / 337
   kanepe sırtı                1086       x 327–753
   ⭐ pencere tabanı            1118       x 406–674 (268 px)
   arka duvar tabanı           1171       x 262–818
   berjerler                   1198–1437  x 138–339 · 741–942
   sehpa üstü                  1208–1239  x 424–643
   ⭐ altın üçgen               ≈ 1150–1450 zeminde + kütüphanenin alt rafları (1190–1307)
   alt UI bandı                1440–1920  (meşe zemin + halının yakın kenarı — kanıt yok)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · pencere ✅ · kanepe ✅ · altın üçgen ✅ · berjerlerin üst kısmı ✅ ·
   kütüphane (x 82–279) çekirdeğin sol kenarından 70 px taşar — kapakta kanıtı modüllerin arka ikisi taşır, beyanlı
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, pencereyi, kanepeyi, berjerleri ve üçgeni tam taşır · 4:5 (285–1635) ve 3:4
   (240–1680) ahşap çatının ve meşe zeminin bir kısmını da taşır.
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      THE HIDDEN LOFT — İKİ SATIR:  "THE HIDDEN"  /  "LOFT"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — üst alın üçgeni ve çatı eğimleri (koyu ahşap) üstünde; mahya kutunun
           üst kenarında (564), pencere tepesi kutunun 18 px ALTINDA (788) — paketin "ortaya yakın" isteği budur: kutu merkez
           kare kırpmanın (420–1500) içinde, kanıtın hemen üstünde
           satır 1 "THE HIDDEN"  y ≈ 580–670 · satır 2 "LOFT"  y ≈ 680–770
PUNTO      ⭐ iki satırda ≈ 92–104 px yazı boyu (kılavuz §5); gerçek yazı sınırları 720 × 210'u AŞMAZ
           kalın sans-serif · tek ağırlık · ölçülü harf aralığı · parlama YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan TEK TONLU koyu ahşap (altın saatte ışık yalnız aşağıda) →
           kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse başlığın arkasına ölçülü koyu geçiş [kılavuz §5]
           ⚠️ satır 2'nin alt kenarı pencere tepesinin parlaklığına 18 px yakın — "LOFT" pencereye DEĞMEZ; değiyorsa punto küçülür
⛔ Başka kelime yok: "attic" · "makeover" · "luxury" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada meşe zemin ve sağ berjer var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "ahşap çatının altında güneşli oda" ayrışıyor mu ⓑ iki satır okunuyor mu
               ⓒ sağ alt köşe boş mu · ⭐ aynı test G0'a: "kirli, unutulmuş çatı katı" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, pencere ve kanepe TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "güneşli, sıcak bir okuma odası" diyor mu — "vitrin render'ı" diyorsa G8 yeniden;
               kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki oda = finaldeki oda [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + THE HIDDEN LOFT  yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
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
① İŞ     Abandoned Attic to Luxury Lounge          (32)   ⭐ sahibin paketindeki başlık, "| AI Timelapse" eki olmadan
② SORU   What Was Hiding Under This Roof?          (32)
③ KISA   One Attic, One Door, One Day              (28)
```

> ⚠️ Paketteki tam hâl "Abandoned Attic to Luxury Lounge | AI Timelapse" 47 karakter — kanal tavanı 40 (MUZIK_VE_KAPAK §3);
> ek ancak sahibin açık onayıyla kalır (THE SLOW TAKEOFF emsali). ⚠️ "Luxury" bitmiş odayı abartabilir ve yem kelimelere
> yakın; "Abandoned" çatı katı için güçlü ama doğru (G0 terk edilmiş görünür) — karar sahibin. Üçü de 40 karakterin altında.

**Açıklama:**

```
Nobody had been up here in years: a dirty rug over the old boards, stained walls, a row of forgotten crates and one grimy
triangular window. In a single day two workers empty the attic, paint it, lay an oak floor and carry everything in
through one narrow door — three walnut bookcases, a leather sofa, two armchairs and a stone table. The window stays
papered over until the very end.

One day in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real home, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #renovation #atticrenovation #interiordesign #homelibrary
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> ⚠️ Açıklama kâğıdı ANAR ama inişini ve güneşi vermez — spoiler bütçesi (aşağıda).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
attic renovation, attic makeover, attic transformation, loft conversion, abandoned attic, attic room, home library, walnut bookshelves, reading room, interior renovation, renovation timelapse, construction timelapse, ai timelapse, ai video, timelapse, atic renovation, loft converson
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("atic renovation" · "loft converson" bu yüzden bilerek var). Gerçek yer/firma adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Turning an attic into a room is mostly a question of what the floor can carry. Attic floors are often built only for light
storage, while a living room needs more, and a full bookcase is one of the heaviest things in a house: two metres of
shelves packed with books can weigh several hundred kilograms. Heavy pieces are safest close to a wall that carries the
floor, which is one reason the bookcases stand along the side wall. The paper on the window is ordinary practice: glass is
masked before painting and floor work, because spatter and fine dust are far easier to keep off than to clean off. And the
light at the end is geometry — on a midsummer evening the sun sets far to the north-west and so low that its rays travel
several metres across the floor for every metre they drop.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). "Several hundred kilograms" tahmindir (≈ 1 m × 2,2 m modül, 6 raf, dolu
> raf ≈ 40–60 kg/m → modül başına ≈ 250–350 kg); "several" bu yüzden yazılı. Son cümle hesaptır: el 7° → tan 7° ≈ 0,12 →
> 1 m inişe ≈ 8 m yol. Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | bir çatı katının dönüşeceği (① ③) ya da bir gizem (②) | nasıl, ne kadar sürede, finali |
| kapak | bitmiş salon, altın ışık + başlık | kirli ilk oda, kâğıtlı pencere, ışığın girdiği an |
| ilk 2 sn | kameraya doğru gelen kirli halı rulosu | içeri girecek her şey |
| açıklama | iki işçi, tek kapı, büyük parçalar, "pencere sona kadar kâğıtlı" | kâğıdın inişi, güneş |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (kâğıt iner, güneş girer) söyleyemez → ✅ (taslak; kurgudan sonra
tekrar).

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: TOTAL RESET ile arka arkaya ÖNERİLMEZ (aynı iş sırası ve kadro) · beşinci ardışık iç mekân — araya dış mekân
   filmi önerilir (öneri, kural değil) · RAIN TOWER ve TOTAL RESET ile arası açılır (G finali) [YAYIN_PLANI §3].
