# 🔍 FIRST SLICE — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1 · DERS 100: RAIN TOWER'da ❶ ❷'ye SPEC eklendi).
> Plan: `FIRST_SLICE_DIKEY_TIMELAPSE.md` · Günlük: `FIRST_SLICE_URETIM_GUNLUGU.md` · Kapak: `FIRST_SLICE_KAPAK.md`

```
FİLM      FIRST SLICE · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 17.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "FIRST SLICE") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
KLİPLER   ⭐ 10 klip / 8 sahne: S2 = S2·a + S2·b · S3 = S3·a + S3·b (4,0 + 4,0 sn; ara kareler G2a · G3a). Yedek yolda 8 klip.
          Kurgu kesmeleri (1x): 8 · 16 · 20 · 24 · 28 · 32 · 40 · 48 · 56 — 20 ve 28 SAHNE KESMESİ DEĞİL, ara kare dikişi.
          ⭐ Ölçülmüş olgular bloğunda CLIP COUNT "8 scenes (10 clips)" ve CUT TIMESTAMPS dokuz kesme yazılır [DERS 90 · 100].
FORMAT    İKİ KEYFRAME ZİNCİRİ · 11 görsel (G0…G8 + G2a + G3a) + 10 I2V (yedek 8) · T2V yok · ⭐ üretim sırası G8 → G7 … G0
YOĞUNLUK  ⭐ her sahnede ÜÇ VURUŞ (sahip isteği "20 sahne 8'e sıkışmış") — 26 görünür iş
REJİM     S0–S6 B (2 sa; S2 · S3 alt klipleri 1'er sa) · S7 ⭐ A (10 dk, alacakaranlık) — iki rejim
IŞIK      TEK GÜN: 05:30 → 07:30 → 09:30 (10:30) → 11:30 (12:30) → 13:30 → 15:30 → 17:30 → 19:30 → 19:40 (güneş saati) ·
          41° kuzey · 21 Haziran (δ +23,4°) · güneş 67°/+9,8° → 304°/−1,8° · garaj kapısı 270°'ye (B) açık, kamera 74°'ye, tilt 0 ·
          final ALACAKARANLIK: yüksek pencereler koyu mavi, içeride fırın ateşi + iki sarkıt lamba
AİLE      İÇ MEKÂN (bekleyen aile — POOL ROOM · TOTAL RESET ile) · ufuk %50 · arka duvar %35,1–64,9 · üstünde koyu tavan (kapak başlık alanı)
TAKVİM    yok — tek gün (haftalık dönüşüm sıkıştırıldı, beyanlı); zaman taşıyıcısı ışık lekesi ve yüksek pencerelerin rengi
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① ATEŞ — kırmızı mozaik kubbenin (x 212–387) kemerli ağzında turuncu odun ateşi (x 259–329 · y %43,5–47,0); kadrajın EN
    PARLAK şeyi; ateş ağzın DIŞINA taşmaz, duman kadrajı örtmez
  ② İLK DİLİM — tezgâh tablasındaki (x 64–664 · y %32,3–35,1) yuvarlak tahtada dilimlenmiş TEK pizza (x 422–539 · kabarık altın
    kenar, kırmızı domates, beyaz peynir) + yanındaki küçük beyaz tabakta TEK dilim (x ≈ 590–625)
  ③ DÜKKÂN — sağ duvarda iki kırmızı bank + krem masa, üstünde iki SICAK sarkıt lamba · arka duvarda mutfak hattının üstünde
    kırmızı-krem çizgili tente · yüksek pencereler KOYU MAVİ (gündüz değil, zifiri değil)
  ④ TANIKLAR — siyah-krem dama zemin · koyu tavan · kırmızı üst duvar + krem alt bant · beyaz seramikli arka sol köşe ·
    koyu kırmızı servis kapısı (x 757–877, açıklığı aynı) · TEK figür hazırlık tezgâhında, sırtı kameraya

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ S7'de pizza fırına TAŞINARAK girmeli ve TAŞINARAK çıkmalı (kürekte); tezgâhta "belirirse" → S7 atılır [DERS 61].
⛔ İkinci pizza, ikinci tabak, ikinci figür, müşteri belirirse → S7 atılır [DERS 55 · 89].
⛔ Yüksek pencereler gündüze dönerse → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: pizza ve dilim AYNI, yalnız ateş titrer; ihrac_kontrol final tutuşu SSIM ≥ 0,90 (ateş bölgesi
   maskelenerek) [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık,
   erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
⛔ KARTTA SES: ateş çıtırtısı + dükkân tonu sürer, son saniyede söner — dijital sessizlik → E kaydı [DERS 100].
⛔ Figürün yüzü durduğu karede okunursa S7 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | %50,0 — arka duvarın içinde (çizgi olarak görünmez) | — |
| ⭐ servis kapısı (x · y) | 757–877 px · %35,8–53,2 · 120 px | ±0,5 puan · ON BİR KAREDE (nirengi ①) · KESİR ±6 px |
| ⭐ arka köşelerin tavan noktaları | x 238 / 947 · y %62,3 / %64,9 | ±0,5 puan · ON BİR KAREDE (nirengi ②) |
| ⭐ yüksek pencere sırası | x 949–988 · y %57,6–67,6 | ON BİR KAREDE (nirengi ③) · parlak |
| ⭐ lastik kafesi | 620–792 px · 172 px | YALNIZ G0 · hareket hâlinde, kapıya yakın |
| eski saclar üstü | y %51,4–51,6 | G0 · G1'de yok |
| beyaz seramik üstü | x 238–718 · y %52,7–53,1 | G2a→ |
| ⭐ fırın kubbesi | 212–387 px · %46,0–50,4 · 175 px | G3a'da arka yarı · G4→ bütün · TEK |
| ⭐ fırın ağzı / ateş | 259–329 px · %43,5–47,0 | G4→ karanlık · G7→ ateş |
| baca dirseği | y %56,4 (py 837) | G4→ · başlık kutusunun ALTINDA |
| buzdolabı | 465–548 px · %36,0–51,5 | G6→ · TEK |
| hazırlık tezgâhı · raflar | 560–718 px · %42,7 · %50,8 | G6→ · raf İKİ |
| tente | 447–731 px · %53,5–56,3 | G7→ · başlık kutusunun ALTINDA |
| ⭐ tezgâh tablası | 64–664 px · %32,3–35,1 | G5→ · TEK |
| cam vitrin üstü | 134–285 px · %42,4–42,7 | G5→ · fırın ağzının ALTINDA (15 px pay) |
| ⭐ pizza tahtası | 422–539 px · 117 px | G7 hamur · G8 pizza |
| ⭐ ilk dilim tabağı | ≈ 590–625 px · %34,1 | YALNIZ G8 |
| banklar · masa · lambalar | 850–961 px · %33–55 | G7→ · bank İKİ · lamba İKİ |
| ⭐ figür G8 | 626 px · %35,1–49,6 · ~280 px | TEK · sırtı kameraya · hazırlık tezgâhında |
| üst band | %87–100 | yalnız tavan · güneş diski HİÇBİR karede |

## 3. ⭐ MEKÂNIN İLERLEYİŞİ — kare kare, elle sayılır

```
G0  ⭐ yağ lekeli beton + parça · ⭐ arka duvarda ezik gri saclar (+2,0) · ⭐ iki paslı tezgâh (sol yarı) · ⭐ lastik kafesi
    HAREKETLİ, kapıya yakın · kirli gri üst duvar · gri tavan + iki floresan · paslı kapı açık · yassı araba
G1  ⭐ kafes, tezgâh, sac YOK · ⭐ çıplak gri briket, cıvata delikleri · ⭐ sac istifi arabada + boru demeti + kanal rulosu
G2  ⭐ bakır boru + gri kanal diz hizasında · soluk yamalar · ⭐ üst duvar KIRMIZI, alt bant KREM · ⭐ kapı koyu kırmızı ·
    zemin beton · tavan gri + floresan · ⭐ panel + seramik arabası + katlı merdiven
G2a ⭐ tavan KOYU panel, floresan YOK · ⭐ sol köşe + arka duvarın sol kısmı BEYAZ SERAMİK · ⭐ ZEMİN HÂLÂ BETON · yer karosu
    paleti
G3  ⭐ DAMA zemin, düz sıra · köşe BOŞ · ⭐ blok + şamot + DÖRT kubbe parçası kapıda
G3a ⭐ KAİDE + ocak + şamot · ⭐ kubbenin ARKA yarısı (iki parça) · iki parça hâlâ palette
G4  ⭐ BÜTÜN kubbe, ağız kameraya, içi KARANLIK · ⭐ siyah baca dirsekle arka duvara · ⭐ tezgâh gövdeleri + tabla kapıda
G5  ⭐ TEZGÂH: iki kırmızı gövde + krem tabla + sol uçta alçak vitrin · ⭐ buzdolabı transpalette kapıda · fırın soğuk
G6  ⭐ MUTFAK HATTI: buzdolabı + hazırlık tezgâhı + iki raf · ⭐ bank + masa + tente rulosu arabada · fırın soğuk
G7  ⭐ iki kırmızı BANK + krem masa · ⭐ TENTE · ⭐ iki sarkıt lamba YANIK · ⭐ ATEŞ ağızda + kütük istifi · ⭐ tahtada HAMUR ·
    TEK figür fırında, kürekle · araba, merdiven, ikinci işçi YOK · pencereler mavi-mor
G8  aynı · ⭐ tahtada dilimli PİZZA + tabakta İLK DİLİM · figür hazırlık tezgâhında · kürek kaideye yaslı
⛔ SAYIM: garaj 1 · servis kapısı 1 · yüksek pencere sırası 1 · fırın (0·0·0·0·0·½·1·1·1·1·1) · tezgâh (0·0·0·0·0·0·0·1·1·1·1) ·
   buzdolabı yerinde (G6→ 1) · bank (G7→ 2) · lamba (G7→ 2) · pizza (G8 1) · tabak (G8 1) ·
   işçi (2·2·2·2·2·2·2·2·2·1·1) — kadro HİÇBİR klipte ikiyi aşmaz [DERS 89] · sıra: G0 G1 G2 G2a G3 G3a G4 G5 G6 G7 G8
⛔ Servis kapısının açıklığı, yüksek pencereler, köşeler ve tavan yüksekliği on bir karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · 96 · beş soru ②③]

```
S0   kafes: tekerlek → servis kapısı · tezgâh: iki el → kapı (TEK TEK) · sac: duvar → yassı araba · boru + kanal: kapı yanı
S1   sac istifi: araba → kapı · boru: demet → kelepçe → arka duvar · kanal: rulo → köşe · boya: kova → rulo → duvar · panel arabası: kapı
S2·a panel: araba → merdiven → ızgara · seramik: kutu → yapıştırıcı → köşe · karo paleti: kapı
S2·b karo: palet → yapıştırıcı → zemin (arka duvardan kameraya) · fırın paletleri: transpalet → kapının içi
S3·a blok: palet → kaide · ocak tablası → kaide · şamot → ocak · kubbe parçası ×2: palet → iki el → ocak (arka)
S3·b kubbe parçası ×2: palet → iki el → ocak (ön) · baca: → kubbe tepesi → arka duvar · tezgâh gövdeleri: araba → kapının içi
S4   gövde ×2: araba → iki el → zemin · tabla: kapı yanı → gövde · vitrin: araba → tabla · buzdolabı: transpalet → kapının içi
S5   buzdolabı: transpalet → arka duvar · hazırlık tezgâhı: araba → duvar · raf ×2: → duvar · bank arabası: kapı
S6   bank ×2: araba → sağ duvar · masa: → bankların arası · tente: rulo → arka duvar · lamba ×2: → tavan · kütük: araba → ağız ·
     hamur: → tezgâh · araba + ikinci işçi: → kapı
S7   hamur: tahta → kürek → ateş → tahta · dilim: tahta → tabak · kürek: → kaide
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı servis kapısı ya da kapının içindeki istif [DERS 48 · 49 · 95].
⛔ Tavandan sarkan kaldırıcı, iskele, boya tabancası YOK [DERS 88 · 67] · kubbe parçası havada uzun yol taşınmaz [DERS 57].
⛔ Bir makine (transpalet / yassı araba) bir klipte tek iş noktası [DERS 96].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISTASYON_VE_IC_MEKAN §4]

```
G0  05:30 (67°/+9,8°)   · doğrudan güneş YOK · serin düz gün ışığı · pencereler soluk gri-mavi
G1  07:30 (85°/+31,7°)  · doğrudan güneş yok · parlak düz · pencereler beyaz
G2  09:30 (108°/+54,1°) · yüksek pencerelerden sağ duvar dibine dar eğik lekeler
G2a 10:30 (126°/+64,2°) · lekeler kısalır
G3  11:30 (158°/+71,3°) · lekeler dik, sağ duvarın hemen dibinde
G3a 12:30 (202°/+71,3°) · lekeler arkaya kayar
G4  13:30 (234°/+64,2°) · lekeler sağ duvarın arka ucunda
G5  15:30 (265°/+43,0°) · ⭐ garaj kapısından sıcak leke zeminin altında ve tezgâh önünde
G6  17:30 (284°/+20,6°) · ⭐ uzun altın leke arka duvarın dibine, tezgâhın gölgesi fırına doğru
G7  19:30 (302°/−0,2°)  · gün batımı · pencereler mavi-mor · içeride ateş + iki lamba · önde mavi
G8  19:40 (304°/−1,8°)  · aynı, biraz koyu
⛔ Lekeler TEK YÖNDE ilerler; geri dönen leke ya da S6'da maviden altına geri dönen gök = zaman ters → ❷ [DERS 98] ·
   ajan ölçümü: yüksek pencere bandının mavi−kırmızı farkı her klipte TEK YÖNDE
⛔ Lamba ve ateş yalnız S6'nın sonunda yanar; G0–G6'da yapay ışık yok
⛔ Güneş diski HİÇBİR karede yok [DERS 39 · 70] · eşit aydınlatılmış "vitrin render'ı" dükkân → ❶ CGI
```

## 6. ⭐ BİR GARAJ · İKİ İŞÇİ · BİR FIRIN · YAZI YOK KAPISI [DERS 55 · 89]

```
Korpus riski: "pizza shop" → tabela, menü panosu, fiyat yazısı, logo, ikinci fırın, kola dolabı, kasa, müşteri ·
"renovation" → iskele, kalabalık ekip
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ) · "Only two workers" her I2V'de · S7 "Only one figure"
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç fırın
⛔ üçüncü işçi · ikinci fırın · tabela · menü · yazılı kutu · müşteri · ikinci tezgâh → ⑧
⛔ Model servis kapısını ya da yüksek pencereleri yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
```

## 7. ⭐ KLİP İÇİ ÜÇ VURUŞ KAPISI [DERS 92 · sahip isteği]

```
Her klipte ÜÇ görünür iş olmalı (2x'te ~0–1,5 · 1,5–3 · 3–4 sn):
  S0 kafes · tezgâhlar · saclar   S1 boru · yama · boya   S2·a tavan · seramik   S2·b dama · fırın paletleri
  S3·a kaide · arka kubbe yarısı   S3·b ön yarı · baca · gövdeler   S4 gövdeler · tabla · vitrin
  S5 buzdolabı · hazırlık tezgâhı · raflar   S6 banklar · tente · lamba + ateş   S7 hamur · fırın · dilim + tutuş
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92). Kusur: bir vuruşun
   HİÇ görünmemesi ya da üç vuruşun aynı anda patlaması (DERS 87).
⛔ G2a'da zemin beton, G3a'da kubbe YARIM değilse → ara kare tutmadı: zincir_kontrol + elle, klip üretilmeden önce.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı yok · konuşma yok · garaj yankısı → dükkân tonu
· 0,0 kafes tekerlekleri · 0–7 tezgâh + sac · 8–15 kelepçe, mala, rulo · 16–20 panel · 20–24 karo · 24–28 blok + mala ·
  28–32 kubbe parçaları + baca kelepçesi · 32–39 gövde, tabla, cam · 40–47 transpalet + çelik · 48–55 bank, tente ·
  53,0 kibrit + odun · 55,5 lamba anahtarı · ⭐ 56–64 ATEŞ ÇITIRTISI (süren) + kürek + bıçak · 59,5 tabak
· KART 64,0–69,0: ateş çıtırtısı + dükkân tonu SÜRER, son saniyede söner [DERS 100]
```

## 9. Zaman ve ışık

```
G0 05:30 67°/+9,8° · G1 07:30 85°/+31,7° · G2 09:30 108°/+54,1° · G2a 10:30 126°/+64,2° · G3 11:30 158°/+71,3° ·
G3a 12:30 202°/+71,3° · G4 13:30 234°/+64,2° · G5 15:30 265°/+43,0° · G6 17:30 284°/+20,6° · G7 19:30 302°/−0,2° ·
G8 19:40 304°/−1,8°   (41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model)
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 sahne), beyanlı
① / ③ DİKİŞ     56,0 (B → A): iz figürlerden yavaş figüre — beyanlı [P5-c] · 20,0 ve 28,0 ara kare dikişleri (sahne kesmesi değil)
① ZAMAN         S0–S1'de doğrudan güneş yok — zamanı pencere parlaklığı taşır; beyanlı
⑤ DEVAMLILIK    renk değişimi (gri/pas → kırmızı/krem → koyu tavan + beyaz → dama → kırmızı kubbe → çelik → ateş) KASITLI;
                servis kapısının RENGİ G2'de değişir, açıklığı DEĞİŞMEZ
⑦ İŞ            S7'nin 4–8 tutuşunda iş yok (kasıtlı): ödül ilk dilimdir
⑦ YOĞUNLUK      2x'te vuruş başına ~1–1,5 sn — sahip isteği, beyanlı ("20 sahne 8'e sıkışmış")
❺ TESLİM        TOTAL RESET ile aynı başlık kalıbı + üçüncü ardışık iç mekân — yayın sırası (öneri, kural değil)
⚠️ TENTE        sahibin "tezgâh üstünde" seçimi arka duvara, mutfak hattının üstüne uygulandı (başlık kutusu) — beyanlı
```
