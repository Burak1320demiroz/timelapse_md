# 🖼️ THE_GRAND_REVIVAL — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30] · sahip kuralları 19.09.2026 (öncesi/sonrası yok) ve 16.10.2026 (sonda kart)

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 720,0–725,0, erime ≤ 1 sn, S89'un
   4–8 tutuşundan SONRA. Kart 5,0 sn (sahip seçimi). Logo yok · müzik tutulan akorla sürer, kartın sonunda söner.
BOYUT      küçük resim 1280 × 720 (16:9) · JPG · ≤ 2 MB · kart 1920 × 1080
KAYNAK     ⭐ YALNIZ G90 — S89'un hedef karesi, filmin SON karesi, zincirin İLK üretilen karesi (metinden) [DERS 30 · 91 · 99]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026 (GPT paketi bölünmüş kapak önerdi — ALINMADI).
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⭐ Başlık alanı G90 promptunda kuruldu: COMPOSITION "Keep the upper left of the frame … plain ceiling and plain
           wall, low in contrast" (G89 ve G90'da birebir).
KANIT      ffmpeg -ss 719.5 -i teslim.mp4 -frames:v 1 g90_kaynak.jpg
           bash araclar/zincir_kontrol.sh g90_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
METİN      THE GRAND REVIVAL  (3 kelime · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi saatte büyük bir yemek odası: bronz lineer avize yanık, altında on sandalyeli uzun ceviz masa; masanın
                  uzak ucunda iki kişi ilk yemeğe oturmuş · arkada üç uzun cam kapı, ardında ışıklı veranda ve koyu mavi bahçe ·
                  sağda büfe + tablo ve cam kapaklı dolap · solda keten perdeli iki pencere
BAŞLIKTA YAZAN    THE GRAND REVIVAL

KANCA             "bu ev neydi?" — başlık bir DİRİLİŞ vaat eder; kapakta görünmeyen şey başlangıçtır (sarmaşıklı, kırık camlı
                  harabe). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 12 dakikanın yolu verir.
KANIT NESNESİ     ⭐ YANIK AVİZE + İKİ KİŞİ — kadrajın en parlak noktası (avize, merkez ekseni) masanın ucundaki iki kişinin
                  üstünde, aynı dikey bantta. 120 px'te "ışıklı oda + sofra" okunur [P3-b: kontrast].
İKİNCİ OKUMA      on sandalye — "bu ev kalabalık için kuruldu"
ÜÇÜNCÜ OKUMA      cam kapıların ardındaki ışıklı veranda — "ev dışarıya kadar bitti"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① sarmaşıklı harabe ve kapıdan çıkan çürük kanepe ② ağır parçaların tek kapıdan girişi ③ oda oda yapılan dokuz mekân.
```

---

## 2. 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon — model başlığı YAZMAZ)

```
METİN        THE GRAND / REVIVAL (büyük harf · iki satır · 3 kelime)
KONUM        SOL ÜST: x ≈ 64–720 px · y ≈ 60–300 px (1080 ölçeğinde) — tavan ve sol duvarın üst bölümü (pencere üstlerinin
             üstü), avizenin solu · ⛔ sağ alt süre damgası alanına (≈ x 1620–1920 · y 980–1080) ve alt 100 px'e GİRMEZ
YÜKSEKLİK    büyük harf ≥ %8 kare boyu = ≥ 86 px @1080 (1280×720'de ≥ 58 px)
RENK         sıcak krem #F3E6CF ya da kanal amberi #F2A03D (KANAL_KIMLIGI) · zemin koyu tavan → kontrast ≥ 4,5:1
             (yetmezse başlığın arkasına %35 opaklıkta düz koyu plaka — gradyan değil)
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK (kartta yalnız erime ≤ 1 sn)
```

⚠️ Yatayda masa ve avize ORTADA, cam kapılar x 501–1419: boş kalan sade yer sol üstteki tavan ve duvardır — başlık oraya
konur. Masanın ucundaki iki kişi (orta, kapıların önü) başlığın altında KALMAZ.

---

## 3. 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ ışıklı oda + masa + iki kişi okunuyor mu ·
                 ⓑ KELİME şekli ayırt ediliyor mu · ⓒ sağ alta kara kutu (süre damgası) konunca kaybolan bir şey var mı: YOK olmalı
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez; ⓑ kayboluyorsa punto büyür
                 ⭐ aynı test S0'ın 0. karesine de: sarmaşıklı cephe + kapıdaki kanepe 120 px'te okunuyor mu (açılış nesnesi)
② KAPAK KANITI  zincir_kontrol.sh g90_kaynak.jpg kapak_metinsiz.png → çıkış: ⬜ (üretimden sonra)   [DERS 30]
③ PROVA         ⭐ İKİ KEZ [DERS 99]: (1) METİNSİZ G90'a, G90 ONAYINDAN ÖNCE · (2) bitmiş kapağa, yüklemeden önce
                 (kapak_prova.py dikey oranlar içindir; yatayda 1280×720 + 120 px küçük + sağ alt kutu yeter)
④ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → yabancı yolu söyleyebiliyor mu: HAYIR olmalı [§3.3]
⑤ BAŞLIK = VAAT  kapak: "harap bir ev yeniden yaşıyor" · başlık: "büyük diriliş" — aynı vaat ✓
⑥ ÜÇ NOKTA      açılış (G0) · final (G90) · kart (G90 + metin) yan yana: karttaki oda = finaldeki oda [MUZIK_VE_KAPAK §5]
```

---

## 4. KART — 720,0–725,0

```
GÖRÜNTÜ      G90 karesi (S89'un son karesi) donar + başlık sol üstte erir (≤ 1 sn)
SES          S89'un tutulan akoru kartın içinde söner · diegetik yatak (tabak tıkırtısı, uzak ağustosböceği) 723,0'da kısılır
⛔ YOK        logo · abone ol yazısı · ok/işaret · ikinci görüntü
SON EKRAN    platform son ekranı yalnız bu kartta ve başlığın dışında (sağ üst ya da sağ alt dışındaki alt bant); iki kişinin üstüne konmaz
```
