# 🔍 TOTAL RESET — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `TOTAL_RESET_DIKEY_TIMELAPSE.md` · Günlük: `TOTAL_RESET_URETIM_GUNLUGU.md` · Kapak: `TOTAL_RESET_KAPAK.md`

```
FİLM      TOTAL RESET · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 16.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "TOTAL RESET") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ S7 "1×" ÜRETİM hızıdır; yayında S7 de 2x oynar (tutuş yayında 2 sn)
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G7 → G8 (ışık) → G6…G0
REJİM     S0–S5 B (2 sa) · S6 ⭐ A (10 dk, mavi saat) · S7 ⭐ G (gerçek zaman, 8 sn) — üç rejim
IŞIK      TEK GÜN: 06:15 → 08:15 → 10:15 → 12:15 → 14:15 → 16:15 → 18:15 → 18:25 → 18:25 + 8 sn (güneş saati) ·
          41° kuzey · 23 Eylül (δ 0°) · güneş 93°/+2,8° → 274°/−4,7° · pencere 213°'ye bakar, kamera 193°'ye, tilt 0 ·
          final GEÇ ALACAKARANLIK: pencere koyu mürekkep mavisi, içeride halka + başlık şeridi sıcak
AİLE      İÇ MEKÂN (bekleyen aile — POOL ROOM ile) · ufuk %50 · arka duvar %29,6–65,3 · üstünde tavan (kapak başlık alanı)
TAKVİM    yok — tek gün (haftalık yenileme sıkıştırıldı, beyanlı); zaman taşıyıcısı pencere ışığı ve tabandaki leke
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① YANAN IŞIK — ceviz panelin üstündeki şerit (y %48,7–48,9 · x 565–1015) ve tavandaki siyah halka (x 332 · y %72,9–74,1)
    SICAK yanar; zeytin duvar panelin üstünde kehribar yıkanır; kadrajın EN PARLAK şeyleri bunlardır
  ② HAZIR YATAK — ceviz bazada beyaz nevresim, iki beyaz yastık, ayakucunda koyu yeşil örtü (ayakucu x 518–921 · 403 px);
    iki ceviz komodin panelin iki ucunda
  ③ PENCERE — beyaz kasa (x 324–523 · 199 px) iki yanda tavandan yere açık renk keten perdeler arasında; dışarısı KOYU MAVİ
    (gündüz değil, zifiri değil); altında meşe masa + siyah sandalye
  ④ TANIKLAR — açık meşe zemin + beyaz süpürgelik · koyu zeytin arka duvar + kırık beyaz sol duvar + beyaz tavan · beyaz
    klima (x 698–875 · y %55,2–59,2) · sol duvarda kapı (x 133–240) ve önünde TEK işçi, sırtı kameraya, eli inmiş

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 57,0'da (2x: 28,5) anahtar; halka ve şerit AYNI ANDA yanar. Biri yanmazsa, ikisi ayrı anlarda yanarsa ya da başka bir
   kaynak (abajur, ekran, tavan spotu) yanarsa → S7 atılır.
⛔ Işık yanarken yatak, perde, masa ya da komodin KAYARSA / yeni nesne belirirse (abajur, halı, tablo) → S7 atılır [DERS 91 ③].
⛔ Pencere gündüze dönerse → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi +
   başlık, erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı
   [DERS 85]. klip_eslestir.py --kart 5 ile ölçülür.
⛔ Figürün yüzü okunursa ya da ikinci figür belirirse S7 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | %50,0 — arka duvarın içinde (çizgi olarak görünmez) | — |
| ⭐ pencere beyaz kasası (x · y) | 324–523 px · %42,4–59,3 | ±0,5 puan · DOKUZ KAREDE (nirengi ①; G0–G1'de tül örter) |
| ⭐ pencere eni | 199 px | KESİR ±6 px · DOKUZ KAREDE |
| ⭐ kapı (x · y) | 133–240 px · %30,6–56,1 | ±0,5 puan · DOKUZ KAREDE (nirengi ②) · hep KARANLIK açıklık |
| ⭐ arka köşelerin tavan noktaları | x 274 / 1015 · y %62,0 / %65,3 | ±0,5 puan · DOKUZ KAREDE (nirengi ③) |
| ⭐ ışık noktası (x · y) | 332 px · %72,9–74,1 | AYNI YER nesnesi · ±4 px · G0–G4 kubbe · G5–G8 halka |
| anahtar | 105 px · %43,7 | DOKUZ KAREDE |
| ⭐ klima | 698–875 px · %55,2–59,2 · 177 px | G4→ · TEK |
| ⭐ ceviz paneller | 565–1015 px · %32,3–48,7 | G5→ · yalnız arka duvarın SAĞ yarısı |
| ⭐ yatak ayakucu | 518–921 px · %30,9–33,2 · 403 px | G6→ · TEK |
| masa üstü | 274–472 px · %39,8–40,5 | G6→ · pencerenin altında |
| perde rayı | 295–557 px · %61,9–63,0 | G7→ |
| ⭐ koltuk G0 | 229–342 px · 113 px | YALNIZ G0 · kapıda, odayı kapatmaz |
| ⭐ işçi G7–G8 | 163 px · %29,5–51,9 · 430 px | TEK · sırtı kameraya · anahtarda |
| üst band | %87–100 | yalnız tavan · güneş diski HİÇBİR karede (pencereden de) |

## 3. ⭐ ODANIN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ lekeli kahverengi halı + çöp yığınları (ambalaj, karton, torba, şişe) · sararmış çiçekli kâğıt (arka + sol) · kirli
    bej tül eğri çubukta, pencereyi örter · sararmış lekeli tavan + buzlu cam kubbe · ⭐ yırtık koltuk iki işçinin elinde
    kapıda · torba rulosu + katlı merdiven kapının içinde
G1  ⭐ çöp ve koltuk YOK · ⭐ tozlu gri şap, tutkal lekeleri · ⭐ halı rulosu sol duvara yaslı, kapının önünde · kâğıt,
    tül, tavan, kubbe AYNI
G2  ⭐ kâğıt YOK: çıplak gri sıva, çatlaklar · ⭐ tül + çubuk YOK: pencere çıplak, gün ışığı · rulo YOK · şap süpürülmüş ·
    ⭐ toz örtüsü + 4 beyaz + 1 zeytin kutu + 2 rulo kapının yanında · tavan ve kubbe AYNI
G3  ⭐ tavan BEYAZ · sol duvar KIRIK BEYAZ · arka duvar baştan başa KOYU ZEYTİN (kasa beyaz) · kubbe AYNI · ⭐ 3 meşe paketi +
    süpürgelik demeti · şap çıplak
G4  ⭐ AÇIK MEŞE zemin + beyaz süpürgelik · ⭐ beyaz KLİMA arka duvarın sağ yarısında, tavanın altında · boya takımı YOK ·
    ⭐ 3 ceviz panel + kapak çıtası kapının yanında · kubbe AYNI
G5  ⭐ CEVİZ BAŞLIK sağ yarıda, yerden ~1,5 m, üstte SÖNÜK şerit · ⭐ kubbe YOK, siyah HALKA (sönük) · ⭐ İKİ komodin
G6  ⭐ ceviz BAZA + çıplak beyaz ŞİLTE komodinlerin arasında · ⭐ meşe MASA + siyah SANDALYE pencerenin altında · pencere
    çıplak · gün battı, mavi · ışıklar SÖNÜK · iki işçi kapıda bohçalarla
G7  ⭐ tavandan yere keten PERDELER, iki yanda açık · ⭐ yatak HAZIR (nevresim, iki yastık, koyu yeşil örtü) · merdiven YOK ·
    TEK işçi anahtarda, eli kalkık · ışıklar SÖNÜK · pencere koyu mürekkep mavisi
G8  aynı · ⭐ HALKA + ŞERİT YANIK · işçinin eli inmiş
⛔ SAYIM: oda 1 · pencere 1 · kapı 1 · ışık noktası 1 · merdiven (1·1·1·1·1·1·1·0·0) · koltuk (1·0·0·0·0·0·0·0·0) ·
   klima (0·0·0·0·1·1·1·1·1) · komodin (0·0·0·0·0·2·2·2·2) · yatak (0·0·0·0·0·0·1·1·1) · masa + sandalye (0·0·0·0·0·0·1·1·1) ·
   işçi (2·2·2·2·2·2·2·1·1) — kadro HİÇBİR klipte ikiyi aşmaz [DERS 89]
⛔ Pencere kasası, kapı, anahtar, köşeler, ışık noktası ve karşı cephe dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  koltuk: iki el → kapı · çöp: zemin → torba → el arabası → kapı · halı: zemin → rulo → sol duvar (kapının önü)
S1  rulo: → kapı · tül + çubuk: pencere → merdiven → kapı · kâğıt: duvar → torba → kapı · boya takımı: kapı → örtü
S2  boya: kutu → tepsi → rulo → tavan / sol duvar / arka duvar · meşe paketleri + süpürgelik: kapı → sol duvar
S3  tahta: meşe paketi → el → şap (arka duvardan kameraya) · süpürgelik: demet → duvar dibi · klima: kapı → merdiven → braket ·
    boya takımı: → kapı · ceviz paneller: kapı → sol duvar
S4  panel: sol duvar → iki el → arka duvar sağ yarı · kubbe: tavan → merdiven → kapı · halka: kapı → merdiven → ışık noktası ·
    komodin: kapı → panel ucu (her işçi bir tane)
S5  ⭐ baza (yan yatırılmış) → kapı → döner → panellerin önü · şilte → kapı → baza · masa (sandalye ters üstünde) → kapı →
    pencere altı — TEK TEK, iki işçi · bohçalar: kapı
S6  perde: bohça → merdiven → tavan rayı · nevresim: bohça → yatak · merdiven: → kapı · işçi: → anahtar
S7  akım: anahtar → halka + şerit · taşınan malzeme yok
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı kapı (koridor) ya da kapının yanındaki istif [DERS 48 · 49].
⛔ Tavandan sarkan kaldırıcı, iskele ya da boya tabancası YOK [DERS 88 · 67].
⛔ Mobilya kendiliğinden kaymaz; her parça kapıdan girer ve TEK TEK yerine oturur [DERS 61 · 89].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISTASYON_VE_IC_MEKAN §4 · ISIK_FINALI]

```
G0     gri şafak (93°/+2,8°) · doğrudan güneş YOK · tül ardında soğuk gri, oda loş ve düz
G1     (114°/+24,8°) · güneş odaya girmez · tül soluk parlar
G2     (143°/+42,6°) · ⭐ ilk dar leke pencerenin SAĞINDA, arka duvarın dibinde · pencere parlak
G3     (186°/+48,9°) · leke pencerenin önünde, 1–2 m, biraz sağda
G4     (226°/+38,9°) · uzun leke kameraya doğru, biraz sola
G5     (252°/+19,5°) · ⭐ turuncu uzun leke SOLA, sol duvara tırmanır
G6     (273°/−2,8°) · güneş battı · pencere koyu mavi · oda loş, serin · lamba SÖNÜK
G7–G8  (274°/−4,7°) · koyu mürekkep mavisi · G7 = G8 dışarıda birebir; G8'de yalnız halka + şerit yanık
⛔ Leke sağdan sola TEK YÖNDE döner; geri dönen leke = zaman ters → ❷
⛔ Lamba yalnız S7'de yanar ve yanık kalır; G0–G7'de hiçbir yapay ışık yok [ISIK_FINALI §3]
⛔ Güneş diski HİÇBİR karede yok — pencerenin görüş bandı az 181–192° [DERS 39 · 70] · eşit aydınlatılmış "vitrin render'ı"
   oda → ❶ CGI
```

## 6. ⭐ BİR ODA · İKİ İŞÇİ · BİR IŞIK NOKTASI KAPISI [DERS 55 · 89]

```
Korpus riski: "bedroom suite" → ikinci yatak, abajur, halı, tablo, ekran, banyo kapısı · "renovation" → iskele, kalabalık
ekip · "air conditioner" → ikinci ünite
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ) · "Only two workers" her I2V'de
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç yatak / kaç pencere
⛔ üçüncü işçi · ikinci yatak · abajur · halı (G4→) · tablo · ekran · ikinci klima · ikinci pencere → ⑧
⛔ Model pencereyi ya da kapıyı yeniden çizerse → ⑤ DEVAMLILIK (kasa ve kapı kimlik nesnesidir)
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92 · eleştiri ①]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 halı sarılır · S1 kâğıt şeritleri iner · S2 arka duvar zeytin olur · S3 klima asılır · S4 halka + komodinler ·
  S5 masa + gün batımı · S6 yastıklar + örtü, el anahtara · S7 tutuş (kasıtlı durgunluk)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı yok · konuşma yok · oda tonu yatak
· 0,0 koltuk kapı kasasında · 0–7 torba hışırtısı · halının sarılışı · 8,0 perde çubuğu · 8–15 kâğıt yırtılması · 16–23 rulo ·
  24–31 parke klik + tokmak · 29,5 matkap · 32–39 panel + merdiven · 37,0 kubbe camı · 40–47 baza + şilte + masa ·
  48–55 perde halkaları + nevresim · 55,0 ayak sesi · ⭐ 57,0 anahtar TIK (KARE SENKRON ±2 kare) · 57,5–64,0 oda tonu
· KART 64,0–69,0: oda tonu sürer, kartın son saniyesinde söner → döngüde S0'ın hışırtısına bağlanır
```

## 9. Zaman ve ışık

```
G0 06:15 93°/+2,8° · G1 08:15 114°/+24,8° · G2 10:15 143°/+42,6° · G3 12:15 186°/+48,9° · G4 14:15 226°/+38,9° ·
G5 16:15 252°/+19,5° · G6 18:15 273°/−2,8° · G7 18:25 274°/−4,7° · G8 18:25 + 8 sn aynı
(41°K · δ 0° · güneş saati · TÜRETİLMİŞ model)
· sabah doğrudan güneş yok (pencere 213°'ye bakar); 10:00'dan sonra leke sağdan sola döner; akşam mavi saat
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 sahne), beyanlı
① / ③ DİKİŞ     48,0 (B → A): yoğun izden yumuşak ize · 56,0 (A → G): iz figürlerden duran figüre — beyanlı [P5-c]
① ZAMAN         S0–S1'in ilk yarısında doğrudan güneş yok — zamanı pencere parlaklığı taşır; beyanlı
⑤ DEVAMLILIK    renk değişimi (kahve/sarı → gri → zeytin/beyaz → meşe → ceviz → keten → sıcak ışık) KASITLI; pencere
                kasası, kapı, köşeler, ışık noktası DEĞİŞMEZ
⑦ İŞ            S7'de iş yok (kasıtlı): ödül odanın kendi ışığıdır · G7/G8 ACTIVITY'si kasıtlı olarak zayıf
⑦ TEMPO         S6 sonu + S7 başı (el anahtarda) 2x'te ~1 sn durgunluk — beyanlı bekleyiş
❺ TESLİM        THE POOL ROOM ile aynı mekanizma (anahtar → ışık) — fark: sıradan oda, bütün yüzeyler değişir, sıcak ışık
                + mavi saat (POOL ROOM: turkuaz eski lambalar + gece)
⚠️ ⑥⑦           ⑥ şap temizliği ve ⑦ çatlak dolgusu DENEMEDİR — görünmezlerse kusur değildir (18 kilit + 2 deneme)
```
