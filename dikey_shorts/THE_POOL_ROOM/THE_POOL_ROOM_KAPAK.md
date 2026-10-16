# 🖼️ THE POOL ROOM — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film). Logo yok, müzik yok.
   ⚠️ Yayında kullanılan kapak ("Bu Havuz Ev Salonuna Dönüştü.png") G8'den türemedi: başka kamera, gündüz,
   fazladan saksılar — aşağıdaki §2 yerleşimi G8 içindir; sonraki filmlerde kart = GN + başlık [DERS 85].
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G8 — S7'nin (GECE) hedef karesi, filmin SON karesi [DERS 30 · MUZIK_VE_KAPAK §2.2]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
METİN      ONCE A POOL  (3 kelime · İngilizce · sahip v2 önerisinde gördü, 16.10.2026)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR — geçmiş ile bugün aynı karede

```
KAPAKTA GÖRÜNEN   gece başında boş bir tuğla salon; çanağın İÇİNDE sıcak bir meşe oda · sol çanak duvarında turkuaz yanan
                  ÜÇ ESKİ HAVUZ LAMBASI · zeminin ortasında camın altından mavi yanan kulvar çizgisi · krem kanepe ve
                  sıcak lambader · coping'in altında kesintisiz kobalt bant · üst iki çini basamak · koyu lacivert cam
                  çatı ve kemerler, camlarında odanın soluk yansıması
BAŞLIKTA YAZAN    ONCE A POOL

KANCA             ⭐ Eleştiri notu (16.10.2026): bu bir "çelişki" değil, geçmiş ile bugünün KARŞILAŞTIRMASIDIR. Kare bugünü
                  (oda), lambalar + bant + şerit geçmişi (havuz) gösterir; başlık ikisini bağlar. Merak "ne olacak?"tan
                  "nasıl oldu?"ya kayar [P21-f] — cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ ÜÇ TURKUAZ LAMBA — kadrajın en parlak üç noktası, sol duvarda merdiven gibi yükselir (y %37–48).
                  120 px'te bile "karanlıkta üç turkuaz nokta + ortada mavi çizgi" okunur [P3-b: piksel değil, kontrast].
İKİNCİ OKUMA      cam koşudaki mavi çizgi: "zeminin altında bir şey var" — filmin özgün ayrıntısı
ÜÇÜNCÜ OKUMA      ölçek: G8'de figür YOK (S7'de çıktı) — ölçeği kanepe, basamaklar ve kapı açıklığı verir
                  ⚠️ G7 kapağında işçi 172 px ile ölçek veriyordu; maket okunursa ölçek testi (§4 ③) bunu yakalar

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez (sahip kuralı kapağı GN'ye bağlar). Kapakta görünmeyen ve
   filmi taşıyan üç şey: ① suyun çekilip lambaların sudan çıkması ② ortada AÇIK bırakılan kanalın neden açık kaldığı
   ③ son camın oturuşu ve tık.
⛔ Kapak G5, G6 ya da G7 DEĞİLDİR: G5 aydınlıktır ama oda boştur; G6'da her ışık sönüktür; G7 artık son kare
   değildir (sahip kuralı kapağı GN'ye bağlar — 8. sahneden sonra GN = G8).
⛔ Kırmızı ok / çember / "28 SECONDS" yazısı / emoji YOKTUR [MUZIK_VE_KAPAK §4.4 · KANAL_KIMLIGI palet].
```

## 2. Yerleşim — G8 tam kare, kırpma yok

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   cam çatı + aşık        0–144
   kemer tepeleri         267        (x %45 / %59,5 / %73,8)
   kapı üstü              537        (x %23,7–34,4)
   (işçi YOK — G7'de başı 627 px'teydi)
   kemer eşikleri         678
   uzak duvar dibi        792
   bitki tepesi           815        (x %36,4)
   lambader abajuru       847        (x %64,7)
   uzak coping            854
   ⭐ lamba 3 / 2 / 1      1001 / 1087 / 1208   (x %31,9 / %28,9 / %24,5)
   ⭐ cam koşu             1064–1311  (x %44,3–55,7)
   kanepe sırtı           979–1201   (x %69,5–78,4)
   yakın coping           1348
   alt UI bandı           1436–1920  (kanıt yok)
```

## 3. Metin — MUZIK_VE_KAPAK §2.3 ölçüleriyle

```
METİN      ONCE A POOL — İKİ SATIR:  "ONCE A"  /  "POOL"
           ⛔ Başka kelime yok: "room" · "living" · "lights" CEVABI verir, kapağa girmez.
YER        ⭐ y 520–860 px (§2.3 bandı 500–1400'ün ÜST kısmı) — uzak tuğla duvar, kapı ve kemerlerin alt yarısı üstünde
           satır 1 "ONCE A"  y 520–674 · satır 2 "POOL"  y 706–860 · SOL hizalı, x 122'den başlar
           "ONCE A" ≈ 6 × 0,6 × 154 ≈ 554 px → x 122–676 · "POOL" ≈ 370 px → x 122–492  · sağ 242 px'e GİRMEZ ✅
           ⭐ KANIT ALANINI ÖRTMEZ: üç lamba (≥ 1001 px), cam koşu (≥ 1064 px), lambader (x %64,7 — "POOL" satırı x %45'te
           biter) metnin DIŞINDA kalır. Örtülen: karanlık kapı, kemerlerin alt yarısı, bitkinin tepesi — kapağın kanıtı
           değil. ⚠️ "ONCE A" satırı kemerlerin alt yarısını örter: camlardaki yansıma (filmin gece ayrıntısı) kısmen
           kapanır — kabul edilebilir, kanıt lambalar + çizgidir.
PUNTO      ⭐ büyük harf yüksekliği 154 px (%8 — 120 px'te ≈ 10 px kalır [§2.3])
           dar kalın sans-serif · tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK
RENK       beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan gece başında koyu tuğla + koyu lacivert kemer camları →
           kontrast 4,5:1'i G7'den de rahat geçmesi BEKLENİR; ölçülür, geçmezse arkasına DÜZ koyu bant (gradyan değil) [§2.3]
⛔ TURKUAZ / AMBER KULLANILMAZ: karede zaten turkuaz lambalar ve sıcak lambader var; metin üçüncü bir vurgu olmaz.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada yalnız terrazzo ve galeri kenarı var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der [§2.4].
```

## 4. Testler — geçmeden yüklenmez

```
① 120 PX       sips -Z 120 kapak.png → ⓐ "karanlık salonda üç turkuaz nokta + ortada mavi çizgi + sıcak lamba" ayrışıyor mu
               ⓑ iki satır KELİME ŞEKLİ olarak ayırt ediliyor mu ⓒ sağ alt süre köşesi boş mu
               ⭐ aynı test S0'ın 0. karesine (G0: suyun altında üç sönük disk) — açılış nesnesi 120 px'te "havuz" mu
② ⭐ TELEFON    gerçek telefonda tam ekran: camın altındaki çizgi açıklamasız "havuz şeridi" okunuyor mu — PİLOT (a) ile AYNI
               test; geçmezse kapak değil G8 yeniden [§2.5 · plan §PİLOT]
③ GEÇMİŞ–BUGÜN kapağa 3 sn bakan biri "burası eskiden havuz muydu?" diyor mu — demiyorsa bant, basamaklar ve lambalar
               yeterince okunmuyordur → G8 yeniden (kapak yeniden ÇERÇEVELENMEZ) · ⭐ figürsüz kapakta "maket mi?"
               sorusu da sorulur
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30] — ⓒ varyantla
⑤ ⭐ KARANLIK MOD koyu temada kare "karanlık fotoğraf" değil "gecede yanan oda" okunmalı [DERS 45] — G8 gece karesi
               olduğu için bu test artık KAPIDIR: kemer kenarları ve tuğla seçilmiyorsa G8 yeniden (güneş −6,5°)
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kapak (G8 + metin) yan yana: kapaktaki oda = finaldeki oda [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + ONCE A POOL   yukarıdaki yerleşim · ANA VARYANT
ⓑ BAŞLIKSIZ          G8 tam kare — "ne bu?" sorusunu en saf hâlde sorar; arama sonucunda zayıf (BLUE SILO emsali) — sahip kararı
ⓒ METİNSİZ           ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (yakın plan bandı ve kemerleri keser).
⚠️ Kısa dikey formatta platform A/B aracı ÇALIŞMAZ [A17-c]; üçü hazır durur. Açılış testi yapılacaksa YALNIZ kapak
   değişir — başlık, açıklama ve kapak aynı anda değiştirilmez (hangi tercihin işe yaradığı belirsizleşir).
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse (GPT paketindeki "BUILDWAKE" kanal adı DEĞİLDİR).
⛔ Başlık ≤ 40 karakter · büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma adı yok.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① SORU   What would you build in an old pool?        (36)
② KAYIP  This pool will never hold water again        (38)
③ İŞ     A living room inside an old pool              (32)   ⭐ öneri
```

> ⭐ Öneri ③: eleştiri haklı — sonucu söyleyen başlık hata değildir; merak "nasıl?"dan gelir. Tek cümle testi geçer:
> başlık + kapak + ilk 2 sn + açıklama yan yana konunca dönüm noktası (açık kanal → cam → eski lambaların yanması)
> söylenemez [MUZIK_VE_KAPAK §3.3].

**Açıklama:**

```
An abandoned indoor pool is drained, cleaned and floored — but the old blue tiles stay.

The basin is 7 by 3.5 metres and one and a half metres deep. The new oak floor stops at the level of the third step,
so the room stays sunk inside the old pool instead of filling it, and one strip of the original floor is left under glass.

One day in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real site, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #renovation #interiordesign #pool
```

> Hashtag: 3 geniş + 5 niş (sabit) + 3 yapı-özel = 11 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle · 366/500 karakter):**

```
pool conversion, pool renovation, indoor pool, abandoned pool, abandoned swimming pool, sunken living room, pool into living room, living room in a pool, conversation pit, old pool lights, underwater pool lights, renovation timelapse, construction timelapse, interior renovation, ai timelapse, ai video, timelapse, swiming pool, swimmingpool, sunken lounge, pit room
```

> ⚠️ Depoda Studio etiketi kuralı YOK (16.10.2026) — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış
> yazılan aramalarda işe yarar ("swiming pool" · "swimmingpool" bu yüzden bilerek var). Gerçek yer/firma adı yok.

**Sabit yorum (yapının arkasındaki gerçek mühendislik · tek paragraf):**

```
Turning a pool into floor space is mostly a water problem, not a weight problem. The basin was built to carry a metre
and a half of water — roughly fifteen kilonewtons on every square metre — while a living room asks for a fraction of
that, so a raised floor on cassettes is structurally easy. The hard part is what the pool was designed to resist: an
empty shell sitting in wet ground can be pushed up by groundwater, which is why real conversions check the hydrostatic
relief valve in the floor before the water ever leaves. The cassettes also leave a ventilated void over the old tiles,
because a tiled basin keeps giving off damp for months. The original underwater lamps are typically low-voltage
fittings in sealed wall niches, which is what makes keeping them possible at all.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). Sayı tek: 1,5 m su ≈ 14,7 kN/m² (fizik, hesaplanabilir). Yorum tuzağı
> sorusu YOK [A33-b]; GPT paketindeki "Would you keep the original blue pool tiles?" eklenecekse ayrı bir yorum olarak ve
> sahip kararıyla.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: THE DEEP END · THE HIDDEN OASIS · THE VANISHING ROOM ile ardışık DEĞİL [YAYIN_PLANI §3].
