# 🖼️ TOTAL RESET — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (G7'den yalnız ışık düzenlemesiyle üretilmiş)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⛔ GPT paketindeki "film ismini son görüntünün üzerine" önerisi KART olarak karşılandı: başlık canlı sahnenin
              üstüne değil, tutuştan sonraki sabit karta yazılır (sahnelerde yazı yasağı sürer).
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
METİN      TOTAL RESET  (2 kelime · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   geç alacakaranlıkta küçük bir yatak odası: koyu mavi pencere iki yanında açık renk keten perdeler ·
                  koyu zeytin duvarın önünde sıcak ışıkla yıkanan ceviz başlık ve beyaz nevresimli, koyu yeşil örtülü
                  yatak · tavanda yanan siyah halka · açık meşe zemin · kapıda sırtı dönük tek işçi, eli anahtarda inmiş
BAŞLIKTA YAZAN    TOTAL RESET

KANCA             "bu oda nasıl bu hâle geldi?" — başlık bir SIFIRLAMA vaat eder; kapakta görünmeyen şey başlangıçtır.
                  Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ SICAK BAŞLIK ŞERİDİ + MAVİ PENCERE — kadrajın en parlak bandı ile en koyu mavi dikdörtgeni yan yana
                  (y 981 ↔ 782–1106). 140 px'te bile "mavi pencerenin yanında sıcak ışıklı yatak" okunur [P3-b: kontrast].
İKİNCİ OKUMA      kapıdaki işçi: "biri bunu az önce bitirdi"
ÜÇÜNCÜ OKUMA      tavandaki yanan halka: ışığın odanın kendisinden geldiği

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① çöple tıkalı ilk oda ② yüzeylerin teker teker soyulup değişmesi ③ anahtar anı.
⛔ Kapak G7 DEĞİLDİR: G7'de ışık sönük, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   tavan                   0–730      (kameraya yakın tavan üstte)
   ⭐ halka lamba (yanık)   498–521    x ≈ 235–430 (elips)
   ⭐ BAŞLIK KUTUSU         560–770    x 180–900 (kılavuz §3 "film adı kutusu")
   tavan–arka duvar çizgisi 666–730   (sağda 666, solda 730)
   perde rayı + perde başı 710–732    x 295–557
   pencere üst kasası      782        x 324–523
   klima                   784–860    x 698–875
   kapı üstü               844–859    x 133–240
   işçi başı               923        x ≈ 163
   ⭐ başlık şeridi (yanık)  981–984    x 565–1015
   pencere alt kasası      1106
   masa üstü               1142–1156  x 274–472
   yatak başı / ayakucu    1179–1199 / 1282–1327   x 518–927
   panel altı              1300
   işçi ayağı              1354
   alt UI bandı            1440–1920  (meşe zemin — kanıt yok)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · pencere ✅ · panel + şerit ✅ · yatak ✅ · klima ✅ · işçi (x 163) ✅
   · halka lamba çekirdeğin 20–40 px ÜSTÜNDE — 1:1 kırpmada (420–1500) görünür ✅
⭐ KIRPMA HESABI: 1:1 (y 420–1500) halkayı, başlığı, pencereyi ve yatağı tam taşır · 4:5 (285–1635) ve 3:4 (240–1680) meşe
   zeminin bir kısmını da taşır.
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      TOTAL RESET — İKİ SATIR:  "TOTAL"  /  "RESET"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — üst zeytin duvar + tavan çizgisi + tavanın alt şeridi üstünde;
           halka lamba (521) kutunun 39 px ÜSTÜNDE, klima ve pencere (782–784) 12–14 px ALTINDA
           satır 1 "TOTAL"  y ≈ 580–670 · satır 2 "RESET"  y ≈ 680–770
PUNTO      ⭐ iki satırda ≈ 92–100 px yazı boyu (kılavuz §5); gerçek yazı sınırları 720 × 210'u AŞMAZ
           kalın sans-serif · tek ağırlık · ölçülü harf aralığı · parlama YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · ⚠️ arka plan İKİ TONLU: alt satır koyu zeytin üstünde (kontrast iyi),
           üst satırın üst kenarı halkanın aydınlattığı açık tavana yakın → kontrast ölçülür; 4,5:1'i geçmezse başlığın
           arkasına ölçülü koyu geçiş (bütün tavan karartılmaz) [kılavuz §5]
⛔ Başka kelime yok: "bedroom" · "makeover" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada meşe zemin var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "mavi pencere + sıcak yatak" ayrışıyor mu ⓑ iki satır okunuyor mu
               ⓒ sağ alt köşe boş mu · ⭐ aynı test G0'a: "tıkalı, sararmış oda" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, pencere ve yatak TAM mı [DERS 94]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "bitmiş, sıcak bir oda" diyor mu — "vitrin render'ı" diyorsa G8 (aslında G7)
               yeniden; kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki oda = finaldeki oda [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + TOTAL RESET      yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ             G8 tam kare — sahip kararı
ⓒ METİNSİZ              ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok.
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma adı yok.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     This Filthy Room Became a Luxury Suite      (38)   ⭐ sahibin paketindeki başlık
② KISA   A filthy room, reset in one day             (31)
③ SORU   What would you do with this room?           (33)
```

> ⚠️ ① "Luxury Suite" bitmiş odayı abartabilir (oda küçük bir yatak odası); izleyici yorumu buna takılabilir — karar
> sahibin. Üçü de 40 karakter tavanının altında.

**Açıklama:**

```
A filthy, cluttered room is stripped back in a single day: the rubbish and the old armchair go out, the carpet and
the wallpaper come up, and the walls take on a deep olive and a warm white. Oak goes down, a walnut headboard goes up,
the bed and the desk come in through the one door — and at dusk one switch brings the room to life.

One day in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real home, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #renovation #roomrenovation #bedroommakeover #interiordesign
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
room renovation, bedroom makeover, room transformation, dirty room cleaning, filthy room, bedroom renovation, extreme room makeover, wallpaper removal, oak floor installation, walnut headboard, olive green bedroom, hotel style bedroom, interior renovation, renovation timelapse, construction timelapse, ai timelapse, ai video, timelapse, bedrom makeover, room transformaton
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan
> aramalarda işe yarar ("bedrom makeover" · "room transformaton" bu yüzden bilerek var). "hotel style" yalnız etikettedir —
> promptlarda yok (plan tasarım ⑪). Gerçek yer/firma adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Renovations run top-down and dirty-to-clean for a reason: the ceiling is painted before the walls and the floor goes
down last, so drips and dust always land on a surface that is about to be covered. Stripping the wallpaper first also
shows the cracks the paper was hiding, which is why the plaster gets filled before any colour goes on. The air
conditioner went exactly where the old connection point was because a split unit is only half a machine: the box on
the wall is joined by two insulated refrigerant pipes and a condensate drain to an outdoor unit, and those runs are the
hardest part to move. The new lighting is LED — a ring on the ceiling and a strip hidden under the headboard rail —
which together draw roughly what one old 60-watt bulb did.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). Son cümle tahmindir (halka ~30 W + 2,3 m şerit × ~10 W/m ≈ 50–55 W);
> "roughly" bu yüzden yazılı. Yorum tuzağı sorusu YOK [A33-b].

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: THE POOL ROOM ile arka arkaya ÖNERİLMEZ (aynı anahtar → ışık mekanizması; öneri, kural değil) ·
   THE RAIN TOWER ile arası açılır (iki G finali) [YAYIN_PLANI §3].
