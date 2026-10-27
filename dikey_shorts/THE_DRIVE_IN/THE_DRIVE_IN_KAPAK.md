# 🖼️ THE DRIVE-IN — KAPAK + YAYIN PAKETİ

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
METİN      DEAD GAS STATION / TO DRIVE-IN CINEMA  (6 kelime · İKİ satır · İngilizce · sahip seçimi 26.10.2026)
           ⚠️ KAPAK_STIL_KILAVUZU §1 "film adı 1–3 kelime" der; bu film sahibin seçtiği yayın başlığını kartta taşır — beyanlı sapma.
              Kısa yedek (sahip isterse): THE DRIVE-IN (2 kelime, tek satır) — §5 ⓓ.
```

---

## 0. ⭐ STİL KARTI [KAPAK_STIL_KILAVUZU §7]

```
STİL KARTI  [KAPAK_STIL_KILAVUZU]
BANT        Ü · y 560–770 · x 180–900 · sakin alan: PERDENİN ÜSTÜNDEKİ KOYU MAVİ GÖK (mavi saat, −8,5°) — plan kadraj kilitleri
            ⚠️ pilonun tepesi bandın yüksekliğinde ama x 972–1065'te, kutunun DIŞINDA · perdenin üst kenarı py 781 (bandın 11 px altı)
IŞIK        reçete R1 (mavi saat + sıcak kaynak) · varyant I0 (GN'nin kendi ışığı) — en parlak şey perdedeki resim; bant KOYU kalır ("the sky
            there stays deep blue and dark")
STİL        S4 — iki satır · yazı tipi Anton (kılavuz varsayılanı; ⚠️ kanal yazı tipi sahip kararı bekliyor) · renk #E8E4DC · vurgu kelimesi —
METİN       DEAD GAS STATION / TO DRIVE-IN CINEMA (6 kelime · 2 satır) · büyük harf ≈ 80–84 px (≥ 78) — 18 karakterlik uzun satır 720 px'in
            %85–95'ini doldurur; iki satır + sıkı aralık ≈ 165–175 px ≤ 210
KONTRAST    ⬜:1 (≥ 4,5) — koyu mavi gökte yüksek beklenir; ölçülür (§4.4 betiği · x0 180 y0 560 x1 900 y1 770) · koyu geçiş: gerekirse
KANIT       zincir_kontrol ⬜ · nirengi ⬜ px · nesne sayımı ⬜ (bir perde · on iki araba · dört kanopi kolonu · altı direk)
PROVA       PROVA_PANOSU ⬜ · 1:1 başlık tam ⬜ · 140 px üç soru ⬜
```

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi saatte, eski bir benzin istasyonunun beyaz kanopisinin ardında yükselen dev perde: üzerinde alçak turuncu güneşin
                  altında sakin bir deniz · perdenin ışığı kanopi çatısına ve araba tavanlarına düşer · altta iki sıra park etmiş araba,
                  kaputlarında perdeye dönük seyirciler · kanopinin altında sıcak beyaz ışık şeridi · sağ kenarda koyu pilon siluet · üstte
                  koyu mavi gök (başlık)
BAŞLIKTA YAZAN    DEAD GAS STATION / TO DRIVE-IN CINEMA

KANCA             "bu bir benzin istasyonu muydu?" — başlık "dead gas station" der; kapak yanan bir perdeyi ve dolu bir parseli gösterir.
                  Görünmeyen şey ölü istasyondur (pompalar, otlar, sarkık panel). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64
                  saniyenin yolu verir.
KANIT NESNESİ     ⭐ YANAN PERDE — koyu mavi kadrajın ortasında turuncu-mavi parlak dikdörtgen; 140 px'te bile "açık hava sineması" okunur
                  [P3-b: kontrast].
İKİNCİ OKUMA      kanopi + boş adalar + pilon: "burası bir benzin istasyonuydu"
ÜÇÜNCÜ OKUMA      kaputlarda seyirciler: "gösteri başladı"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① otlu, paslı, sarkık kanopili ölü istasyon ② pompaların gidişi, iskeletin yükselişi, perdenin kaplanışı ③ perdenin yandığı an ve son
   arabanın gelişi.
⛔ Kapak G7 DEĞİLDİR: G7'de perde boş, son araba şeritte, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   açık gök (koyu mavi)                0–780      kadraj boyu
   ⭐ BAŞLIK KUTUSU                     560–770    x 180–900 — perdenin üstündeki koyu mavi gök
   pilon (tepe → kutu altı)             594–1234   x 972–1065 — kutunun DIŞINDA, sağ kenarda
   kavaklar (tepe)                     777        x ≈ 231
   ⭐ PERDE (durağan resim)             781–986    x 324–756 — iki kolonu x 313 / 767, yere kadar 1267
   ufuk                                960
   kanopi (çatı + alın şeridi + kolonlar) 1131–1335 x 324–756 · ışık şeridi alın şeridinin altında
   dükkân (kanopinin altından)          1190–1255  x 353–727
   ⭐ uzak araba sırası                  1367–1499  x 244–836 · son araba x ≈ 678
   yakın araba sırası                  1557–1813  x 72–1008
   alt UI bandı                        1440–1920  (yakın sıra — yardımcı doku)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · perde ✅ · kanopi ✅ · dükkân ✅ · uzak sıranın üst kenarı çekirdeğin sınırında —
   beyanlı
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, perdeyi, kanopiyi ve uzak sırayı taşır · 4:5 (285–1635) ve 3:4 (240–1680) yakın sıranın üst
   yarısını da taşır.
⚠️ Perdenin üst kenarı py 781 — başlığın alt satırı en çok py ≈ 760'a iner; perde ışığı göğü aydınlatırsa (bant açık renge dönerse) G8
   yeniden (plan PİLOT a).
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 + KAPAK_STIL_KILAVUZU §4 ölçüleriyle

```
METİN      DEAD GAS STATION / TO DRIVE-IN CINEMA — İKİ SATIR (S4), ORTALI, x = 540
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — perdenin üstündeki koyu mavi gök · satırlar y ≈ 578–662 ve ≈ 672–756 · yazı perdeyi,
           kanopiyi ve pilonu örtmez
PUNTO      Anton, büyük harf ≈ 80–84 px (≥ 78 eşiği) · uzun satır "TO DRIVE-IN CINEMA" (18 karakter, tire dahil) bant genişliğinin %85–95'i ·
           satır aralığı punto × 0,95 · gerçek yazı sınırları 720 × 210'u AŞMAZ, aşarsa punto küçülür; eşiğin altına düşerse kısa yedeğe
           geçilir (THE DRIVE-IN) — harf aralığı daraltılmaz · tek ağırlık · parlama / kontur YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan koyu mavi gök → kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse başlığın
           arkasına #101315 yumuşak koyu geçiş (%35–50) [KAPAK_STIL §4.4]
⛔ Başka kelime yok: "AI" · "timelapse" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada yakın sıranın sağ arabası var (yardımcı doku).
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "yanan perde + arabalar" ayrışıyor mu ⓑ başlık iki satırda okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "ölü benzin istasyonu" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, perde ve kanopi TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "eski bir benzin istasyonunda açık hava sineması" diyor mu — "otopark", "render", "reklam" diyorsa
               G8 yeniden (kanopi ve pilon okunmuyor demektir); kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki perde = finaldeki perde [MUZIK_VE_KAPAK §5]
⑦ KONTRAST     KAPAK_STIL §4.4 betiği · bant x 180–900 · y 560–770 → ≥ 4,5:1
```

## 5. Dört varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + DEAD GAS STATION / TO DRIVE-IN CINEMA   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur (sahip seçimi)
ⓑ BAŞLIKSIZ            G8 tam kare — sahip kararı
ⓒ METİNSİZ             ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
ⓓ KISA YEDEK           G8 + THE DRIVE-IN (tek satır, S1) — yalnız sahip isterse ya da ⓐ 78 px eşiğini tutturamazsa
⛔ DÖRDÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (kırpmalar PROVA'dır — kapak_prova.py).
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/marka adı yok · ≤ 40 karakter.
```

**Başlık — sahip seçti (26.10.2026):**

```
⭐ SEÇİLEN   Dead Gas Station to Drive-In Cinema          (35)   paketin ana önerisi · sahip seçimi
   yedek    Abandoned Gas Station Becomes a Movie Night (43)   paketin alternatifi — ⚠️ 40 karakteri AŞAR, kısaltılmadan kullanılmaz
   yedek    What Will This Dead Fuel Station Become?    (40)   planın MERAK SORUSU
```

> Seçilen başlık 40 karakterin altında; KILAVUZ_REHBERI §6'nın "≤ 5 kelime" testini bir kelimeyle aşar (beyanlı). "Gas station"
> YALNIZ başlıkta ve kartta durur; promptlarda istasyon "old roadside fuel station" diye geçer (marka korpusu — plan TASARIM ⑲).

**Açıklama:**

```
A dead roadside fuel station: rusty pumps, a sagging canopy, weeds in every crack. Two workers haul the pumps away, scrub the canopy
clean, patch the lot and raise a tall steel frame just behind it — then a wide white screen, panel by panel, and twelve bays in fresh paint.
Then the cars come.

Weeks of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real building, no real fuel station, no real cinema and no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #driveincinema #gasstation #renovation #movienight
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> Açıklama perdenin yanışını ve son arabayı ANMAZ ("Then the cars come.") — spoiler bütçesi. "Weeks of work" sahneler arası takvim
> atlamasının beyanıdır (plan SAHA satırı).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
drive-in cinema, gas station conversion, abandoned gas station, drive in theater, outdoor cinema, movie night, construction timelapse, ai timelapse, ai video, timelapse, the drive-in, drive in movie, gas staton
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("gas staton" bu yüzden bilerek var). Gerçek yer/firma/marka adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Old fuel stations are sometimes turned into car washes, cafés or event spaces. Before anything else the pumps and the fuel equipment have
to be taken out by specialists, and anything tall that goes up on the lot, like a big screen, usually needs its own foundations and
bracing against the wind rather than resting on the old canopy, which was only built to carry its own roof.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("sometimes · usually"); belirli ürün, ölçü, yük ya da süre
> iddia edilmez (ÇIKARIM, genel bilgi). Yeraltı tank sökümü filmde GÖSTERİLMEZ — yorum onu "specialists" diye anar, iddia etmez. Yorum tuzağı
> sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | ölü istasyondan arabalı sinemaya | nasıl, hangi sırayla, perdenin yanışı, son araba |
| kapak | yanan perde + dolu parsel + başlık | pompalar, otlar, iskeletin yükselişi, yanış anı |
| ilk 2 sn | paslı istasyon, taşınan pompa, ot biçen işçi | parselin neye dönüşeceği |
| açıklama | pompalar, kanopi, yama, çelik çerçeve, perde, park yerleri, "arabalar gelir" | perdenin yanışı, son araba |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (mavi saatte perde bir resimle yanar, son araba son boş yere girer) kapak dışında
söyleyemez → ✅ (taslak; kurgudan sonra tekrar). ⚠️ Kapak yanan perdeyi gösterir; yanış ANI ve son arabanın gelişi yine saklıdır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: KÜTLE ailesi — THE OPENING NIGHT (dolan çanak, alacakaranlık ışığı), THE TURNTABLE (arabalar gerçek zamanda), GAME ON (saha
   çizgisi, alacakaranlık ışığı) ve THE SUNKEN GARDEN (ip ışık, oturan insanlar) ile ARDIŞIK YAYINLANAMAZ [YAYIN_PLANI §3].
