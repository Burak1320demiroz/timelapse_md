# 🔍 THE HIDDEN LOFT — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_HIDDEN_LOFT_DIKEY_TIMELAPSE.md` · Günlük: `THE_HIDDEN_LOFT_URETIM_GUNLUGU.md` · Kapak: `THE_HIDDEN_LOFT_KAPAK.md`

```
FİLM      THE HIDDEN LOFT · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 18.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "THE HIDDEN / LOFT") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ S7 "1×" ÜRETİM hızıdır; yayında S7 de 2x oynar (tutuş yayında 2 sn)
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 ⭐ G (gerçek zaman, 8 sn) — iki rejim
IŞIK      TEK GÜN: 04:45 → 06:45 → 08:45 → 10:45 → 12:45 → 14:45 → 16:45 → 18:45 → 18:45 + 8 sn (güneş saati) ·
          41° kuzey · 21 Haziran (δ +23,4°) · güneş 60°/+2,2° → 295°/+7,2° · pencere 275°'ye bakar, kamera 275°'ye, tilt 0 ·
          G2–G7 camda KORUMA KÂĞIDI (ışığı yayar) · final ALTIN SAAT: kâğıt iner, alçak güneş temiz camdan girer
AİLE      İÇ MEKÂN (bekleyen aile — POOL ROOM · TOTAL RESET · FIRST SLICE ile) · ufuk %50 · arka alın duvarı %39,0–70,6 ·
          üst alın üçgeni ve çatı eğimleri koyu ahşap (kapak başlık alanı)
TAKVİM    yok — tek gün (yenileme sıkıştırıldı, beyanlı); zaman taşıyıcısı pencerenin rengi (kirli cam → kâğıt → temiz cam)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① AÇIK PENCERE + ALTIN ÜÇGEN — üçgen pencerede kâğıt YOK, temiz camdan altın gök önünde çam tepeleri (taban x 406–674 ·
    268 px · y %41,7–58,9); pencereden SOLA kayarak uzanan uzun, eğik ALTIN IŞIK ÜÇGENİ zeminde, krem halıda, kanepenin
    sırtında ve kütüphanenin alt raflarında; kadrajın EN PARLAK şeyleri pencere ve bu üçgendir
  ② DOLU KÜTÜPHANE — sol duvarda üç ceviz modül (x 82–279), raflar soluk renkli düz sırtlı kitaplarla dolu
  ③ OTURMA GRUBU — krem halının uzak yarısında sırtı pencereye konyak deri kanepe (x 327–753 · 426 px, TEK parça) · yakın
    yarıda kanepeye dönük iki krem berjer (≈ 200 px) · arada traverten tablalı alçak sehpa
  ④ TANIKLAR — koyu ahşap çatı (mertekler, mahya, tahta kaplama — G0 ile AYNI) · açık meşe zemin + beyaz süpürgelik · kırık
    beyaz duvarlar · sağ duvarda soyut tablo · sol köşede zeytin ağacı · pencerenin solunda sönük lambader · kapı (x 701–802)
    loş sahanlığa açık · oda BOŞ: işçi yok, merdiven yok, kâğıt yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–58,0'da (2x: 28,0–29,0) kâğıt AŞAĞI kayarak iner ve ışık TEK YÖNDE açılır. Kâğıt solarak kaybolursa, ışık titrer ya da
   gidip gelirse [DERS 98], ya da yapay bir kaynak (tavan lambası, lambader, ekran) yanarsa → S7 atılır.
⛔ Işık girerken kanepe, berjerler, sehpa, kitaplar ya da tablo KAYARSA / yeni nesne belirirse (tavan lambası, ikinci bitki,
   şömine, ekran) → S7 atılır [DERS 91 ③].
⛔ Pencere öğle ışığına ya da geceye dönerse → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi +
   başlık, erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı
   [DERS 85]. klip_eslestir.py --kart 5 ile ölçülür.
⛔ Bir figürün yüzü okunursa ya da üçüncü figür belirirse S7 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | %50,0 — arka alın duvarının içinde (çizgi olarak görünmez) | — |
| ⭐ üçgen pencere kasası (x · y) | taban 406–674 px · %41,7 · tepe 540 px · %58,9 | ±0,5 puan · DOKUZ KAREDE (nirengi ①; G2–G7 camı kâğıt örter, KASA görünür) |
| ⭐ pencere taban eni | 268 px | KESİR ±6 px · DOKUZ KAREDE |
| ⭐ kapı (x · y) | 701–802 px · %39,0–52,8 | ±0,5 puan · DOKUZ KAREDE (nirengi ②) · hep LOŞ açıklık |
| ⭐ mahya + arka köşeler | mahya x 540 · %70,6 · diz duvarı üstü x 262 / 818 · %55,5 | ±0,5 puan · DOKUZ KAREDE (nirengi ③) |
| ⭐ ahşap çatı | mertekler, mahya kirişi, tahta kaplama, üst alın üçgeni | DOKUZ KAREDE AYNI — boyanmaz, temizlenmez, makas/çatı penceresi belirmez [DERS 80] |
| ⭐ G0 halı rulosu | 229–851 px · %35,4–39,5 · 622 px | YALNIZ G0 · iki ucunda iki işçi |
| ⭐ kütüphane | 82–279 px · alt %31,9–38,0 · üst %56,8–54,5 | G4→ · TAM ÜÇ modül · sol duvar |
| lambader | 337 px · %37,4–50,0 | G4→ · TEK · hep sönük |
| ⭐ kanepe | 327–753 px · %35,0–43,4 · 426 px | G5→ · TEK parça (iki modül birleşik) · sırtı pencereye |
| ⭐ berjerler | 138–339 · 741–942 px · %25,2–37,6 | G6→ · TAM İKİ |
| sehpa üstü | 424–643 px · %35,5–37,1 | G6→ · TEK |
| tablo | 891–969 px · %44,4–53,7 | G7→ · sağ duvar |
| zeytin ağacı | ≈ 299 px · %38,4–51,5 | G7→ · sol köşe |
| ⭐ işçiler G7 | ≈ 480 / 600 px · %38,4–51,1 · ≈ 243 px | İKİ · pencerenin dibinde, kâğıdın alt köşelerinde · sırtları kameraya |
| üst band | %87–100 | yalnız ahşap çatı · güneş HİÇBİR karede (pencereden de) |

## 3. ⭐ ODANIN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ kirli gri-kahve halı kameradan odanın ortasına, uzak ucu kalın RULO · iki işçi rulonun iki ucunda diz çökmüş ·
    rulonun ötesinde eski gri çam tahta · eski sandık sırası (sağ duvar) · eski tahta yığını (sol duvar) · lekeli gri sıva +
    kahverengi rutubet lekeleri · KİRLİ cam
G1  ⭐ halı, sandık, tahta YOK · ⭐ çıplak eski gri tahta, halının soluk bandı · ⭐ 2 boya kutusu + 2 saplı rulo + katlı merdiven
    + beyaz kâğıt rulosu kapının içinde · sıva ve cam AYNI (kirli) · iki işçi pencerede
G2  ⭐ yan duvarlar + alın duvarının alt kısmı KIRIK BEYAZ (çatı ve üst üçgen AHŞAP) · ⭐ camın tamamı BEYAZ KÂĞIT, kasanın
    içinde — parlayan üçgen · eski tahta, duvar diplerinde boya sıçraması · ⭐ meşe paketleri istifi kapının yanında
G3  ⭐ AÇIK MEŞE zemin (odanın enine) + beyaz süpürgelik · paketler YOK · meşe artığı istifi + merdiven · oda boş
G4  ⭐ ÜÇ ceviz modül sol duvarda, raflar BOŞ · ⭐ lambader pencerenin solunda (sönük) · ⭐ bağlı krem halı rulosu kapının yanında
G5  ⭐ krem halı serili · ⭐ TEK konyak kanepe halının uzak yarısında, sırtı pencereye · ⭐ sehpa ayağı kapının yanında ·
    kâğıt parlak, hafif sıcak
G6  ⭐ İKİ krem berjer kanepeye dönük · ⭐ traverten tablalı sehpa halının ortasında · ⭐ kitap kolili el arabası kapının içinde ·
    raflar BOŞ · kâğıt beyaz-altın
G7  ⭐ raflar DOLU · ⭐ sağ duvarda soyut tablo · ⭐ sol köşede zeytin ağacı · araba YOK · merdiven kapının içinde · ⭐ kâğıt
    KOYU ALTIN · oda loş sıcak · İKİ işçi pencerenin dibinde, kâğıdın alt köşelerinde, sırtları kameraya
G8  ⭐ kâğıt YOK — temiz cam, altın gök, çam tepeleri · ⭐ ALTIN ÜÇGEN zeminde, halıda, kanepe sırtında, alt raflarda · işçi,
    merdiven, kâğıt YOK
⛔ SAYIM: oda 1 · pencere 1 · kapı 1 · merdiven (0·1·1·1·1·1·1·1·0) · halı rulosu G0 (1·0·…) · kütüphane modülü
   (0·0·0·0·3·3·3·3·3) · lambader (0·0·0·0·1·1·1·1·1) · kanepe (0·0·0·0·0·1·1·1·1) · berjer (0·0·0·0·0·0·2·2·2) ·
   sehpa (0·0·0·0·0·0·1·1·1) · tablo (0·0·0·0·0·0·0·1·1) · zeytin ağacı (0·0·0·0·0·0·0·1·1) ·
   işçi (2·2·2·2·2·2·2·2·0) — kadro HİÇBİR klipte ikiyi aşmaz [DERS 89]
⛔ Pencere kasası, kapı, mahya, köşeler ve ahşap çatı dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  halı: zemin → rulo (kameraya doğru) → iki omuz → uçtan kapı · sandık: sağ duvar → el → kapı · tahta: sol duvar → kucak →
    kapı · boya takımı + kâğıt rulosu: sahanlık → kapı içi
S1  cam: bez → temiz · kâğıt: rulo → merdiven → cam (kenardan kenara, kasanın içinde) · boya: kutu → rulo → sıva (sol duvar →
    alın duvarı altı → sağ duvar) · boya takımı: → kapı · meşe paketleri: sahanlık → kapı yanı istif
S2  tahta: paket → el → eski tahtanın üstü (kameradan arka duvara, kapıda biter) · süpürgelik → duvar dibi · ambalaj: → el
    arabası → kapı
S3  ⭐ modül: sahanlık → kapı (YAN YATIK) → dik → sol duvar (arkadan kameraya) — TEK TEK · lambader: kapı → pencere solu · halı
    rulosu: sahanlık → kapı yanı
S4  ⭐ halı: rulo → zemin (kameraya doğru açılır) · kanepe yarısı ①: sahanlık → kapı → halının uzak yarısı · yarısı ②: aynı yol,
    ① yerindeyken → ①'e itilir — TEK TEK, iki işçi · sehpa ayağı: sahanlık → kapı yanı
S5  ⭐ berjer ① ②: sahanlık → kapı → halının yakın yarısı (TEK TEK) · ayak: kapı yanı → halı ortası · tabla: sahanlık → iki el,
    DÜZ → ayak · kitap kolili araba: sahanlık → kapı içi
S6  kitap: koli → el → raf (arkadan öne, alttan üste) · tablo: sahanlık → kapı → sağ duvar (tel + çivi) · boş araba: → kapı ·
    zeytin ağacı: sahanlık → kapı → sol köşe · iki işçi: → kâğıdın alt köşeleri
S7  kâğıt: cam → iki el → kapı · merdiven: kapı içi → kapı · ışık: güneş → temiz cam → zemin, halı, kanepe, raflar
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı kapı (sahanlık) ya da kapının yanındaki istif / araba [DERS 48 · 49].
⛔ Tavandan sarkan kaldırıcı, iskele ya da boya tabancası YOK [DERS 88 · 67]. Taş tabla havada asılı değil, iki elde düz.
⛔ Mobilya kendiliğinden kaymaz; her parça kapıdan girer ve TEK TEK yerine oturur [DERS 61 · 89].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISTASYON_VE_IC_MEKAN §4 · ISIK_FINALI]

```
G0     gri şafak (60°/+2,2°) · doğrudan güneş YOK · kirli camda soğuk gri, oda loş ve düz
G1     (79°/+23,3°) · güneş evin arkasında · kirli camdan serin, eşit ışık
G2     (98°/+45,9°) · ⭐ kâğıt camda: eşit beyaz parlar · oda yumuşak, eşit
G3     (132°/+66,4°) · kâğıt daha parlak beyaz
G4     (212°/+70,1°) · kâğıt en parlak düz beyaz (öğle)
G5     (256°/+51,4°) · ⭐ güneş kâğıda vurur: parlak, hafif sıcak · pencerenin önünde sıcak yıkama
G6     (277°/+28,9°) · güneş kâğıda dik: güçlü beyaz-altın · oda sıcak
G7     (295°/+7,2°) · kâğıt KOYU ALTIN · oda loş, sıcak
G8     aynı an · kâğıt yok: ALTIN ÜÇGEN içeride, pencereden SOLA kayarak · köşeler loş
⛔ Kâğıdın rengi beyazdan altına TEK YÖNDE döner (S4–S6); geri dönen renk = zaman ters → ❷ [DERS 98]
⛔ G0–G8 boyunca HİÇBİR yapay ışık yanmaz — lambader hep sönük; final ışığı güneştir [ISIK_FINALI §3'ün anahtarsız hâli]
⛔ Güneş HİÇBİR karede kadrajda yok — pencerenin görüş bandı az 268–282°, yükseklik −6,5…+7,6° [DERS 39 · 70] · eşit
   aydınlatılmış "vitrin render'ı" oda → ❶ CGI
```

## 6. ⭐ BİR ODA · BİR PENCERE · İKİ İŞÇİ KAPISI [DERS 55 · 89]

```
Korpus riski: "attic lounge" → çatı penceresi, ikinci pencere, şömine, ekran, avize, puf, ikinci kanepe · "bookcase" →
kütüphane merdiveni · "renovation" → iskele, kalabalık ekip (ÇIKARIM — bu odada ölçülmedi)
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ) · "Only two workers" her I2V'de · G8'de "No people are present."
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç kanepe modülü / kaç pencere
⛔ üçüncü işçi · üçüncü kanepe modülü · dördüncü kütüphane modülü · üçüncü berjer · ikinci bitki · tavan lambası · çatı
   penceresi · ikinci pencere → ⑧
⛔ Model pencereyi ya da kapıyı yeniden çizerse → ⑤ DEVAMLILIK (kasa ve kapı kimlik nesnesidir)
⛔ Kâğıtta, kolilerde, kitap sırtlarında, tabloda okunur yazı → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 sandıklar + tahtalar, boya takımı · S1 duvarlar beyazlar, meşe paketleri · S2 süpürgelik, ambalaj · S3 ikinci ve üçüncü
  modül, lambader, halı rulosu · S4 ikinci kanepe yarısı, sehpa ayağı · S5 tabla, kitap arabası · S6 tablo, ağaç, eller
  kâğıtta · S7 tutuş (kasıtlı durgunluk)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı yok · konuşma yok · oda tonu (ahşap çatı altı) yatak
· 0,0 halının sarılışı · 0–7 tahtalar, sandık · 8–15 bant yırtılması + rulo · 16–23 parke klik + tokmak · 23,0 testere ·
  24–31 modüllerin duvara oturuşu · 32–39 halı, deri, birleşme · 40–47 berjer ayakları, taşın çeliğe oturuşu · 48–55 kitaplar,
  çivi, saksı · ⭐ 56,0–58,0 kâğıdın yırtılarak inişi (KARE SENKRON ±2 kare) · 58–60 adımlar · 60,0–64,0 oda tonu + akşam kuşları
· KART 64,0–69,0: oda tonu sürer, kartın son saniyesinde söner → döngüde S0'ın halı sürtünmesine bağlanır
```

## 9. Zaman ve ışık

```
G0 04:45 60°/+2,2° · G1 06:45 79°/+23,3° · G2 08:45 98°/+45,9° · G3 10:45 132°/+66,4° · G4 12:45 212°/+70,1° ·
G5 14:45 256°/+51,4° · G6 16:45 277°/+28,9° · G7 18:45 295°/+7,2° · G8 18:45 + 8 sn aynı
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model)
· sabah doğrudan güneş yok (pencere 275°'ye bakar); G2–G7 kâğıt ışığı yayar; akşam alçak güneş camdan girer
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 sahne), beyanlı
① / ③ DİKİŞ     56,0 (B → G): iz figürlerden net, kâğıdı tutan iki figüre — beyanlı [P5-c]
① ZAMAN         S0–S1'de doğrudan güneş yok, S1–S6'da zamanı kâğıdın rengi taşır; beyanlı
⑤ DEVAMLILIK    renk değişimi (gri-kahve → gri tahta → kırık beyaz → meşe → ceviz → krem/konyak → altın) KASITLI; pencere
                kasası, kapı, mahya, ahşap çatı DEĞİŞMEZ · kâğıt G2–G7 KASITLI (camın koruması), G8'de iner
⑦ İŞ            S7'nin 4–8'inde iş yok (kasıtlı tutuş) · G8 boş oda (kasıtlı: işçisiz final, kapak kaynağı)
⑦ TEMPO         S6 sonu + S7 başı (eller kâğıtta) 2x'te ~0,5 sn durgunluk — beyanlı bekleyiş
❺ TESLİM        TOTAL RESET ile aynı iş sırası (boşalt → boya → döşe → eşya) ve kadro — fark: eğik ahşap çatı, üçgen pencere,
                kütüphane duvarı ve ANAHTARSIZ final (pencere açılır, güneş girer)
```
