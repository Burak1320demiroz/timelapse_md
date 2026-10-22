# 🖼️ THE CLIFF POOL — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99]
METİN      THE CLIFF / POOL  (3 kelime · iki satır · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR (VİRAL ANATOMİ)

```
KAPAKTA GÖRÜNEN   Alacakaranlıkta 45 metrelik derin bir deniz kanyonu uçurumunun boşluğuna 6 metre uzanan siyah çelik konsol teras:
                  ucunda 80 mm kalınlığında şeffaf akrilik ön cam, içinden taşan ve boşluğa çarşaf gibi dökülen berrak turkuaz
                  sonsuzluk havuzu · terasın merkezindeki gömme bazalt oturma alanında canlı altın alevlerle yanan doğrusal ateş çukuru ·
                  koyu bazalt taşlar ve tik güverte boyunca yanan sıcak kehribar (#F2A43A) mimari LED çizgileri · üstte minimalist pergola.
BAŞLIKTA YAZAN    THE CLIFF / POOL

VİRAL KANCA       ① İKİ ZIT ELEMENT: SU VE ATEŞ — Uçurum boşluğuna taşan buz mavisi turkuaz su ile havuzun hemen dibindeki
                    gömme salonda parlayan sıcak altın ateş çukuru tek karede buluşur. Zıt elementlerin bu lüks tezatı insan gözünü
                    0.2 saniyede durdurur (visual stop power).
                  ② YÜKSEKLİK KORKUSU VE MÜHENDİSLİK CESARETİ (VERTIGO HOOK) — Altında hiçbir kolon veya ayak olmayan, 45 metrelik
                    boşluğa uzanan konsol bir cam havuz. İzleyicideki ilk refleks: "Bu nasıl taşır? Uçurumun ucunda nasıl duruyor?"
                  ③ "NASIL YAPILDI?" MERAKI — Kapak nihai lüks sonucu gösterir; ancak boşluğa uzanan çeliklerin ve akrilik camın
                    hangi aşamalardan geçtiğini göstermez. Merak "ne olacak?"tan "bunu buraya nasıl koydular?"a kayar [P21-f].

140 PX TESTİ      140 px genişliğinde (Instagram Reels profil ızgarası veya Shorts önerilenler kutusu):
                  - Turkuaz parlayan havuz ve şeffaf cam kenardan dökülen su anında parlar (yüksek luma kontrastı).
                  - Merkezdeki altın sarısı ateş çukuru koyu bazaltın ortasında net bir nokta olarak seçilir.
                  - Üstteki "THE CLIFF / POOL" başlığı koyu akşam gökyüzünde temiz okunur.

⚠️ SPOİLER BÜTÇESİ — BEYANLI: Kapak sonucu verir, İNŞAAT YOLUNU vermez. Kapakta görünmeyen ve videoyu izleten üç kritik an:
   ① Uçurumun çıplak kayasında boş bekleyen beton ankrajlar ve vincin sarkıttığı dev ilk çelik I-kiriş.
   ② 80 mm'lik dev akrilik camın vakumlu kaldırıcı vantuzlarla havadan uçurum ucuna indirilişi.
   ③ Su pompasının dolumu ve ateş çukurunun aniden parlayıp ışıkların tek karede yandığı 58. saniye vuruşu.
⛔ Kırmızı ok / çember / abartılı emoji / "AI TIMELAPSE" / "BEFORE-AFTER" YOKTUR.
```

---

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   alacakaranlık gökyüzü + uzak headland 0–480      sakin gökyüzü ve uzak deniz kanyonu ufku
   ⭐ BAŞLIK KUTUSU                   560–770    x 180–900 (kılavuz §3 "film adı kutusu") — gökyüzü ve uzak kanyon silueti üstü
   pergola üst taşıyıcıları           520–680    sol üstten konsol uzanan siyah çelik profiller
   ⭐ taşan akrilik sonsuzluk havuzu   820–1180   x 310–680 — turkuaz su, şeffaf akrilik cam ve dökülen su çarşafı
   ⭐ gömme ateş çukuru ve lounge     1080–1420  x 420–740 — canlı yanan doğrusal alev ve koyu bazalt oturma grubu
   tik güneşlenme güvertesi           980–1480   zengin tik ahşap dokusu ve kehribar ışık yansımaları
   ⭐ beton ankraj ve bazalt anakaya   1380–1750  x 120–420 — yapının kayaya kilitlendiği masif temel
   sağ masif bazalt kaya burnu        320–1650   x 780–1080 — kadrajın sağını kilitleyen doğal nirengi
   alt UI bandı                       1440–1920  (anakaya, çakıllı platform — kayıp önemsiz yardımcı doku)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380):
   - Başlık kutusu ✅ (y 560–770)
   - Taşan akrilik cam havuz ✅ (y 820–1180)
   - Yanan ateş çukuru ve gömme lounge ✅ (y 1080–1380)
   - Pergola ve cam korkuluklar ✅
   - Anakaya ve temel ankrajı çekirdeğin altında kalır — güvenli yardımcı doku ✅

⭐ KIRPMA HESABI:
   - 1:1 kare kırpma (y 420–1500): Başlığı, havuzu, akrilik camı, yanan ateş çukurunu ve tik terası eksiksiz taşır!
   - 4:5 dikey akış (y 285–1635): Pergolanın tamamını ve anakaya ankrajını da içine alır.
   - 3:4 profil ızgarası (y 240–1680): Terasın tüm mimari bağlamını korur.
```

---

## 3. Tipografi — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      THE CLIFF POOL — İKİ SATIR:  "THE CLIFF"  /  "POOL"   ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — havuzun ve pergolanın hemen üstündeki sakin alacakaranlık gök bandı
           satır 1: "THE CLIFF"  y ≈ 575–660 (yükseklik ≈ 85 px)
           satır 2: "POOL"       y ≈ 675–765 (yükseklik ≈ 90 px)
PUNTO      Kalın sans-serif (Inter / Montserrat / Neue Haas Grotesk benzeri) · tek ağırlık · ölçülü harf aralığı.
           720 × 210 px kutu sınırını aşmaz.
RENK       Kırık beyaz #E8E4DC [KANAL_KIMLIGI paleti].
           Arka plan koyu alacakaranlık göğü ve lacivert kanyon olduğu için kontrast 5:1'in üzerindedir.
           Gerektiğinde harflerin arkasına %15 hafif koyu gradyan taban eklenebilir.
⛔ Başka metin yok: "AI", "timelapse", "luxury", "infinity", "before-after" kapağa ASLA girmez.
⛔ SAĞ ALT KÖŞE BOŞ: Süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — sağ altta karanlık bazalt kayalık dokusu kalır.
```

---

## 4. Testler — Geçmeden Yayınlanmaz

```
① 140 PX KÜÇÜK ÖNİZLEME TESTİ
   - 140 px genişlikte "uçurum kenarında turkuaz taşan cam havuz" hemen seçiliyor mu? ✅
   - Merkezdeki altın sarısı ateş çukuru ışığı parlıyor mu? ✅
   - "THE CLIFF / POOL" başlığı iki satır olarak okunuyor mu? ✅
   - Sağ alt köşe süre sayacı için boş mu? ✅

② KIRPMA PROVALARI (kapak_prova.py)
   - 1:1 karede havuz + ateş çukuru + başlık kutusu tam mı? ✅
   - 4:5 akış formatında üstten/alttan kritik eleman kesiliyor mu? ✅ (Sıfır kayıp)
   - 3:4 profil önizlemesinde pergoladan temele kadar tüm kompozisyon duruyor mu? ✅

③ VİRAL İÇERİK VAADİ DOĞRULAMASI
   - Görsel 3 saniye içinde "Ben burada olmalıyım" arzusu (aspirational lifestyle) ve
     "Bunu boşluğa nasıl oturttular?" merakı (engineering awe) uyandırıyor mu? ✅
   - G0 açılışı (vinçteki ilk çelik I-kiriş) bu vaadin tam zıttı ve başlangıcı olarak kurgulandı mı? ✅
```
