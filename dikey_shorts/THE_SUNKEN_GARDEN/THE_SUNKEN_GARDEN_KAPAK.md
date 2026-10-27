# 🖼️ THE SUNKEN GARDEN — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 56,0–61,0 (yayında 28,0–33,0),
   erime ≤ 0,5 sn, S6'nın 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G7 — S6'nın hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
KANIT      bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 54.0 -i teslim_1x.mp4 -frames:v 1 g7_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G7 İLE, G7 ONAYINDAN ÖNCE [DERS 99]
METİN      THE SUNKEN / GARDEN  (3 kelime · iki satır · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR (VİRAL ANATOMİ)

```
KAPAKTA GÖRÜNEN   Mavi saat alacakaranlığında terkedilmiş beton havuz çukurunun içine inşa edilmiş modern batık bahçe:
                  merkezde doğal taş ateş çukurunda canlı altın-turuncu alevler · arka sarı-kahve tuğla duvar boyunca
                  parlayan sıcak beyaz bistro ip ışıkları · bal rengi hardwood ahşap zemin · çevredeki 6 ahşap kasada
                  yükselen yemyeşil bambular · minderli bankta dinlenen iki kişi.
BAŞLIKTA YAZAN    THE SUNKEN / GARDEN

VİRAL KANCA       ① DÖNÜŞÜM VAADİ VE MERAK — Terk edilmiş, moloz dolu çukur havuzun lüks bir batık bahçeye dönüştüğünü
                    kapaktaki zengin detaylar hemen müjdeler; ancak "bunu nasıl yaptılar?" sorusu videoyu sonuna dek izletir.
                  ② SICAK-SOĞUK IŞIK TEZADI — Derin mavi saat gökyüzünün soğuk kobalt tonu ile merkezdeki canlı ateş çukurunun
                    sıcak kehribar alevi ve duvardaki ampullerin parıltısı insan gözünü 0,2 saniyede yakalar.
                  ③ COZY SUNKEN MEKÂN DUYGUSU — Zemin kotunun 1,5 metre altında korunaklı, samimi, özel bir sığınak hissi.

140 PX TESTİ      140 px genişliğinde (Instagram Reels profil ızgarası veya Shorts önerilenler kutusu):
                  - Merkezdeki canlı ateş çukuru ve duvardaki bistro ışıkları güçlü birer parlak odak noktası oluşturur.
                  - Yeşil bambu siluetleri ve sıcak ahşap taban net seçilir.
                  - Üstteki "THE SUNKEN / GARDEN" başlığı sakin gökyüzü bandında okunur.

⚠️ SPOİLER BÜTÇESİ — BEYANLI: Kapak nihai lüks sonucu verir, yapım yolunu vermez. Kapakta görünmeyen üç kritik an:
   ① Havuzun içi yaprak ve balçık doluyken kürekle çuvallara doldurulan açılış anı (G0).
   ② Basınçlı yıkamayla eski betonun griye döndüğü ve çakılın serildiği an.
   ③ Eski krom dayanağın söküldüğü ve ateş çukurunun ilk yakıldığı an.
⛔ Kırmızı ok / çember / abartılı emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

---

## 2. Yerleşim — G7 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G7 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G7 kilitleri):
   alacakaranlık gökyüzü              0–280      sakin kobalt mavi gökyüzü bandı
   ⭐ BAŞLIK KUTUSU                   220–440    x 180–900 (tuğla duvarın üstü ve sakin gökyüzü bandı)
   arka tuğla duvar ve bistro ışıklar 280–680    sarı-kahve tuğla dokusu, parlayan ampul dizileri
   hardwood kaplı giriş basamakları   460–780    x 216–864 — yukarı bağlanan temiz ahşap basamaklar
   bambu fidanları ve saksı kasaları  680–1350   yeşil yapraklar, doğal bitki paravanı
   ⭐ merkez taş ateş çukuru ve alev  1180–1460  x 420–660 — canlı yanan altın alevler ve dairesel taş halka
   minderli oturma bankları ve 2 kişi 1150–1520  ateşin iki yanında rahat oturan figürler
   hardwood planking teras tabanı     820–1750   sıcak ahşap dokusu ve ateş yansımaları
   alt UI bandı                       1440–1920  (güvenli alan — alt zemin tahtaları)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 480–1500):
   - Başlık kutusu ✅ (y 220–440)
   - Bistro ip ışıkları ve tuğla duvar ✅ (y 280–680)
   - Bambular ve saksı kasaları ✅ (y 680–1350)
   - Canlı yanan ateş çukuru ve oturan figürler ✅ (y 1180–1500)
   - Hardwood platform tabanı ✅

⭐ KIRPMA HESABI:
   - 1:1 kare kırpma (y 420–1500): Ateş çukurunu, bankları, bambuları, ahşap terası ve ışıkları merkezde tutar.
   - 4:5 dikey akış (y 285–1635): Başlık kutusunun büyük kısmını ve tüm batık bahçe mimarisini taşır.
   - 3:4 profil ızgarası (y 240–1680): Başlığı, duvarı, ışıkları ve zemini eksiksiz korur.
```

---

## 3. Tipografi — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      THE SUNKEN GARDEN — İKİ SATIR:  "THE SUNKEN"  /  "GARDEN"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 220–440 — tuğla duvarın hemen üstündeki sakin akşam gök bandı
           satır 1: "THE SUNKEN"  y ≈ 240–325 (yükseklik ≈ 85 px)
           satır 2: "GARDEN"      y ≈ 340–430 (yükseklik ≈ 90 px)
PUNTO      Kalın sans-serif (Inter / Montserrat / Neue Haas Grotesk benzeri) · tek ağırlık · ölçülü harf aralığı.
           720 × 220 px kutu sınırını aşmaz.
RENK       Kırık beyaz #E8E4DC [KANAL_KIMLIGI paleti].
           Arka plan koyu alacakaranlık göğü olduğu için kontrast 5:1'in üzerindedir.
⛔ Başka metin yok: "AI", "timelapse", "transformation", "before-after" kapağa ASLA girmez.
⛔ SAĞ ALT KÖŞE BOŞ: Süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — sağ altta karanlık ahşap köşe dokusu kalır.
```
