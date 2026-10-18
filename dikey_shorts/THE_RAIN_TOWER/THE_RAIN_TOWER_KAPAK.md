# 🖼️ THE RAIN TOWER — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Logo yok, müzik yok. YouTube Shorts'ta kapak "videodan kare seç" ile
   bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi [DERS 30 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
METİN      THE RAIN TOWER  (3 kelime · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR — geçmiş ile bugün aynı karede

```
KAPAKTA GÖRÜNEN   altın akşam ışığında eski bir fabrika avlusu; paslı beton kolonlar ve bağ kirişleriyle üç katlı bir
                  asansör kulesi · kuyunun içinde cep cep yeşil bir kaya duvarı · ortasında tepedeki taş ağızdan koyu
                  çukura düşen TEK BEYAZ ŞERİT · iki yanında iki paslı kılavuz ray · sağda takozlarda paslı yük kabini ·
                  pompanın yanında sırtı dönük tek işçi
BAŞLIKTA YAZAN    THE RAIN TOWER

KANCA             geçmiş (paslı kabin, raylar, kolonlar) ve bugün (yeşil + su) aynı karede — bölme olmadan. Merak "ne
                  olacak?"tan "nasıl oldu?"ya kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ BEYAZ ŞERİT — kadrajın en parlak şeyi, kulenin ortasında dikey (y 861–1312). 140 px'te bile "yeşil
                  bir kulenin ortasından düşen beyaz çizgi" okunur [P3-b: piksel değil, kontrast].
İKİNCİ OKUMA      takozdaki paslı kabin: "burası bir asansör kulesiydi"
ÜÇÜNCÜ OKUMA      ölçek: işçi 97 px — kulenin üç kat olduğunu verir

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① kabinin kuyudan inişi ② çukurun dolup suyun nereden geldiği ③ kanalın neden kuru bırakıldığı ve düğme anı.
⛔ Kapak G7 DEĞİLDİR: G7'de kanal kuru, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   açık gök                0–800      (uzak baca x 900–936, tepesi 388)
   ⭐ BAŞLIK KUTUSU         560–770    x 180–900 (kılavuz §3 "film adı kutusu")
   kule tepesi             800–821    x 378–702
   ⭐ taş ağız              861        x ≈ 540
   fabrika saçağı          946
   bağ kirişi 2            981–1003
   bağ kirişi 1            1179–1200
   ⭐ şelale                861–1312   x 517–563
   kabin                   1261–1400  x 728–831
   işçi                    1319–1416  x ≈ 700
   su yüzü / eşik          1312 / 1371
   ön kolon dipleri        1397
   alt UI bandı            1436–1920  (kanıt yok)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · kule ✅ · şelale ✅ · kabin (1400'e kadar — alt 20 px çekirdek
   dışında, 1:1 kırpmada (420–1500) görünür) ✅
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı ve şelaleyi tam taşır · 4:5 (285–1635) ve 3:4 (240–1680) baca tepesini de taşır.
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      THE RAIN TOWER — İKİ SATIR:  "THE RAIN"  /  "TOWER"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — yalnız AÇIK GÖK üstünde; kulenin tepesi (800) kutunun 30 px altında
           satır 1 "THE RAIN"  y ≈ 580–670 · satır 2 "TOWER"  y ≈ 680–770
PUNTO      ⭐ iki satırda ≈ 92–100 px yazı boyu (kılavuz §5); gerçek yazı sınırları 720 × 210'u AŞMAZ
           kalın sans-serif · tek ağırlık · ölçülü harf aralığı · parlama YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan sıcak akşam göğü → kontrast ölçülür; 4,5:1'i geçmezse
           başlığın arkasına ölçülü koyu geçiş (bütün gökyüzü karartılmaz) [kılavuz §5]
⛔ Başka kelime yok: "waterfall" · "garden" · "elevator" CEVABI verir, kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada avlu var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "yeşil kulenin ortasında beyaz şerit" ayrışıyor mu ⓑ iki satır okunuyor mu
               ⓒ sağ alt köşe boş mu · ⭐ aynı test G0'a: "boş kuyu + havada kabin" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM ve şelale TAM mı [DERS 94]
③ GEÇMİŞ–BUGÜN kapağa 3 sn bakan biri "burası eskiden asansör kulesi miydi?" diyor mu — demiyorsa kabin ve raylar
               okunmuyordur → G8 yeniden (kapak yeniden ÇERÇEVELENMEZ)
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki kule = finaldeki kule [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + THE RAIN TOWER   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
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
① İŞ     We Turned an Abandoned Elevator Tower Into a Waterfall   (54)   ⭐ sahibin paketindeki başlık
② KISA   An old elevator tower becomes a waterfall              (41)
③ SORU   What would you put in an empty elevator shaft?          (46)
```

> ⚠️ ① "We" der: kanal gerçek bir ekip işi gösteriyormuş gibi okunabilir — altbilgideki AI beyanı bu yüzden silinmez.
> 40 karakter tavanı (POOL ROOM paketi) ①'de aşılıyor; sahip paketi bu başlıkla verdi — karar sahibin.

**Açıklama:**

```
An abandoned freight-lift tower in an old factory yard: the car comes out, the pit is cleared and flooded, and the
empty shaft is lined with a rock wall and planted pocket by pocket — with one dry channel left down the middle.

The water comes from the old lift pit itself. A pump draws it up the back corner to a stone lip at the top, and it
falls ten metres back into the pit it came from.

One day in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real site, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #renovation #verticalgarden #waterfall
```

> Hashtag: 3 geniş + 5 niş (sabit) + 3 yapı-özel = 11 ✅ (8–12). Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
elevator tower, abandoned elevator, freight elevator, elevator shaft, abandoned factory, factory renovation, vertical garden, living wall, green wall, indoor waterfall, waterfall wall, rock wall, recirculating waterfall, adaptive reuse, industrial renovation, renovation timelapse, construction timelapse, ai timelapse, ai video, timelapse, elevater shaft, waterfal
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan
> aramalarda işe yarar ("elevater shaft" · "waterfal" bu yüzden bilerek var). Gerçek yer/firma adı yok.

**Sabit yorum (yapının arkasındaki gerçek mühendislik · tek paragraf):**

```
A recirculating waterfall never needs a river — it needs a sump. The old lift pit holds the water; a pump lifts it
about eleven metres to the lip and gravity brings it back, so the only water the system loses is what evaporates and
splashes out. That is why the pit was filled first and the level never changes in the last shot: a pump cannot start
from an empty basin, and a basin that drains while the fall is running will run the pump dry. Lifting water is cheap
in physics terms — raising one litre eleven metres takes about 108 joules — so even a steady fall of several litres a
second needs well under a kilowatt of useful pumping power; real systems spend more than that on friction in the pipe
and on pump losses. The rock panels are lightweight castings bolted to a steel grid standing off the old wall, which
keeps the wet planting and the concrete apart.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). Sayı tek: 1 kg × 9,81 × 11 m ≈ 108 J (fizik, hesaplanabilir).
> Yorum tuzağı sorusu YOK [A33-b].

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: THE BLUE SILO ile ardışık DEĞİL [YAYIN_PLANI §3].
