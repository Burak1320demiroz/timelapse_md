# 🔍 THE READING CAR — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_READING_CAR_DIKEY_TIMELAPSE.md` · Günlük: `THE_READING_CAR_URETIM_GUNLUGU.md` · Kapak: `THE_READING_CAR_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE READING CAR · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 25.10.2026 · kural 7 × 8 · sahibin briefi "8 × 8 sn, 9 G") · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "ABANDONED TRAIN CAR / BECOMES A BOOKSHOP") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 G (gerçek zaman, 1×) — tek dikiş 56,0'da
IŞIK      İÇ MEKÂN S0–S6 iki tripod iş lambası (soğuk beyaz, SABİT) + pencerelerden gün ışığı · SAAT TEK YÖNDE, açık gök: 05:55 → … → 19:55 →
          19:55:08 (güneş saati) · 41° kuzey · 21 Haziran (δ +23,4°) · kamera 0°'ye (kuzey) bakar, tilt 0, 24 mm · sağ pencereler doğu, sol
          pencereler batı · güneş HİÇBİR karede yok · zaman pencerelerden düşen lekelerde (sabah sol yana → öğle leke yok → akşam sağ yana)
          · final MAVİ SAAT: dört sarkıt + masa lambası TEK KAREDE yanar
AİLE      İÇ MEKÂN (bekleyen) · ana yapı = alın duvarı + kapı + uzak kitaplıklar + müşteri (py 849–1360) · başlık alanı yakın koyu ahşap tavan
TAKVİM    sahneler arasında haftalar (KESMEDE), sahne içinde 2 sa / 8 sn (beyanlı)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① MÜŞTERİ + KİTAP — TEK müşteri (uzun deve tüyü palto, geniş kenarlı şapka) sağ üçüncü kitaplığın önünde (x 569–615 · py 954–1171),
    yan profilde, elinde AÇIK kitap · yüz okunmuyor · rafta kitabın çekildiği küçük boşluk
  ② LAMBALAR — TAM dört koyu abajurlu sarkıt (py 868–917, eksende) ve tezgâhtaki pirinç masa lambası YANIK · ışık AŞAĞI, sıcak havuzlar
    zeminde ve raflarda · yakın ahşap tavan KOYU (başlık bandı py 560–770)
  ③ KİTAPÇI — TAM sekiz koyu yeşil kitaplık (4 + 4), hepsi dolu, sırtlar YAZISIZ · sol ilk pencerenin altında deri okuma koltuğu · sağda
    pirinç raylı kayar merdiven · kapının solunda meşe tezgâh · açık meşe zemin, tahtalar boyuna
  ④ TANIKLAR — dört + dört pencere sırası (koyu mavi) · koyu ahşap tavan + TAM beş kaburga · kırmızı acil fren kutusu (x 286–328 · py ≈ 901)
    · alın duvarı (x 432–648) + AÇIK kapı (x 505–575 · py 933–1115), ardında çakıl + tuğla duvar + koyu mavi gök · işçi yok, geçici eşya yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ ≈ 56,5'te (2x: 28,25) dört sarkıt + masa lambası TEK KAREDE birlikte yanar ve HEPSİ yanık kalır. Lamba lamba sırayla "dolarsa", titrer,
   söner, yeniden yanarsa → S7 atılır [ISIK_FINALI · DERS 98].
⛔ 56,5–59,5'te (2x: 28,25–29,75) müşteri kapının içinden sağ üçüncü kitaplığa SÜREKLİ yürüyüşle gelir. Işınlanır (eşik → raf tek adım),
   ikiye çıkar, kameraya döner ve yüzü okunursa → S7 atılır [DERS 96 · 15].
⛔ 59,0–60,0'da (2x: 29,5–30,0) TEK kitap raftan çekilir ve açılır; kitap erir, ikiye çıkar ya da raftan değil havadan gelirse → S7 atılır.
⛔ Işık yanarken kitaplık, koltuk, tezgâh, merdiven KAYARSA / yeni nesne belirirse (ikinci müşteri, işçi, tabela, kasa, yazılı kitap sırtı) →
   S7 atılır [DERS 91 ③].
⛔ Sarkıt ışığı yakın tavanı (başlık bandı py 560–770) aydınlatırsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: müşteri yerinde okur, hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık (iki satır),
   erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta lamba uğultusu + uzak akşam kuşları (dijital sessizlik DEĞİL) [DERS 100].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0 · 24 mm · h 1,7 m)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk / kaçış noktası | py 960 (%50) · kapının içinde | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ alın duvarı + kapı | duvar x 432–648 (216 px) · kapı x 505–575 · py 933–1115 | KESİR ±7 px · DOKUZ KAREDE AÇIK (nirengi ①) · kapalı kapı yok |
| ⭐ pencere sırası | sol 1 x 108–204 · sol 2 x 288–324 · sağ ayna · py 923–1253 (yakın) | DOKUZ KAREDE aynı yer ve aralık (nirengi ②) · 4 + 4 |
| ⭐ tavan + kaburgalar | kaburga tepeleri py 499 · 730 · 806 · 845 · 868 | DOKUZ KAREDE, TAM beş (nirengi ③) · tavan hiç değişmez |
| ⭐ fren kutusu | x 286–328 · py ≈ 880–922 | DOKUZ KAREDE aynı yer |
| ⭐ koltuklar | G0 altı bağlı + biri arabada · G1 dört (3. ve 4. pencereler) | G2→ yok · hep BÜTÜN |
| ⭐ zemin | G0–G1 çürük tahta · G2 çıplak çelik · G3 + kapı önünde 1 m meşe · G4 meşe ön kenarı py ≈ 1323 · G5→ tam meşe | tahtalar BOYUNA (önden arkaya) |
| ⭐ kitaplıklar | yakın ön yüz sol x 293–348 · py 849–1433 | G5→ TAM sekiz · G5 boş · G6 uzak dört dolu · G7→ sekizi dolu |
| ⭐ sarkıtlar | Y 6,25 · 8,75 · 11,25 · 13,25 · py 776 → 917 | G6→ TAM dört · G6–G7 SÖNÜK · G8 yanık · en yakın kablo py ≥ 776 |
| ⭐ tezgâh | x 427–500 · py 1027–1122 | G6→ |
| ⭐ okuma koltuğu | x 111–349 · py 1242–1685 | G7→ · sırtı duvara |
| ⭐ müşteri | G7 kapının içi x 523–557 · py 955–1120 · G8 x 569–615 · py 954–1171 | TEK · yüz yok · G0–G6 yok |
| iş lambaları | x ≈ 360 · 660 · py ≈ 939–946 | G0–G6 · G7→ yok |
| işçi | Y 6'da ≈ 373 px · Y 13'te ≈ 172 px | TAM İKİ · yüz yok, kameraya dönük kimse yok · G7–G8 yok |

## 3. ⭐ KİTAPÇININ İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ çürük koyu tahta (yaprak, kâğıt, cam kırığı) · soyulmuş gri-yeşil boya + pas · kırık cam dişleri · altı yırtık mavi-gri koltuk bağlı ·
    ilk sol pencerenin altı BOŞ · ⭐ ilk sağ koltuk el arabasında, iki işçi kaldırıyor · basamaklı merdiven kapının sağında · iki iş lambası
G1  ⭐ ilk ve ikinci pencerelerin altı iki yanda boş (cıvata delikleri) · dört koltuk uzakta · ⭐ üç siyah torba kapının içinde sağda · araba boş
G2  ⭐ koltuk yok · bütün zemin çıplak paslı çelik · ⭐ eski tahta yığını sağda kapının içinde · araba yarı dolu · iki işçi levyede
G3  ⭐ temiz soluk gri duvarlar · sekiz BOŞ çerçeve · ⭐ kapının önünde 1 m meşe (boyuna) · meşe demetleri sağda · fren kutusu yerinde
G4  ⭐ meşe kapıdan ikinci pencere çiftine · kameraya yakın çıplak çelik · ⭐ sekiz yeni cam · demetler küçük
G5  ⭐ tam meşe · ⭐ sekiz boş koyu yeşil kitaplık · pirinç ray + kayar merdiven · ambalaj demeti kapının yanında
G6  ⭐ uzak dört kitaplık dolu · ⭐ dört sarkıt (sönük) · ⭐ tezgâh + masa lambası · arabada altı kasa · basamaklı merdiven açık
G7  ⭐ sekiz kitaplık dolu · ⭐ okuma koltuğu · işçi, iş lambası, araba, kasa, merdiven YOK · ⭐ TEK müşteri kapının içinde · mavi saat · lambalar
    sönük
G8  ⭐ lambalar YANIK · ⭐ müşteri sağ üçüncü kitaplıkta, elinde açık kitap
⛔ SAYIM: vagon 1 · kapı 1 · pencere 8 · kaburga 5 · fren kutusu 1 (dokuz karede) · koltuk (7·4·0·…) · torba (0·3·0·…) · kitaplık (0·…·0·8·8·8·8)
   · dolu kitaplık (0·…·0·0·4·8·8) · sarkıt (0·…·0·4·4·4) · tezgâh (0·…·0·1·1·1) · okuma koltuğu (0·…·0·1·1) · el arabası (1·…·1·0·0) · iş lambası
   (2·…·2·0·0) · işçi (2·2·2·2·2·2·2·0·0) · müşteri (0·…·0·1·1) — kadro HİÇBİR klipte ikiyi aşmaz [DERS 89] · makine YOK
⛔ Pencere sırası, tavan, kaburgalar, fren kutusu, alın duvarı ve açık kapı dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  koltuk: cıvata → iki işçi → el arabası → koridor → kapı → dışarıdaki çakıl (BÜTÜN, tek tek, yakın üçü) · çöp: süpürge → torba → kapının
    içinde sağ köşe
S1  koltuk: cıvata → araba → kapı (kalan dördü) · torba: araba → kapı · tahta: levye → kucak → kapının içindeki yığın (kameradan kapıya)
S2  yığın: araba → kapı (iki sefer) · boya: kazıyıcı → fırça + nemli bez (uzaktan kameraya) · cam kırığı: el → çelik kova → kapı · meşe
    demeti: kapı → araba → takoz (sağ duvar) · ilk şerit: demet → kapının önü (koridorun tam eni)
S3  meşe: demet → zemin (kapıdan kameraya, ikinci pencere çiftine) · cam: kapı → iki el (dik) → çerçeve (uzaktan kameraya, sekiz)
S4  meşe: son demet → yakın zemin · kitaplık: kapı (YAN YATIK) → iki el → dik → duvar parçası → cıvata (uzaktan kameraya, 4 + 4) · ray: →
    sağ kitaplık tepesi · kayar merdiven: → ray
S5  ambalaj: → kapı · sarkıt: kutu → basamaklı merdiven → tavan kablosu (uzaktan kameraya) · kitap: kasa → araba → kucak → raf (uzak dört,
    raf raf) · tezgâh: kapı → iki el → alın duvarı (kapının solu)
S6  kitap: kasa → kucak → raf (yakın dört, raf raf) · okuma koltuğu: kapı → iki el (SIRTI ÖNDE) → ilk sol pencere (YERİNDE) · boş kasa +
    basamaklı merdiven + iki iş lambası: → araba → kapı · işçiler: → kapı · müşteri: kapı → eşiğin içi
S7  ışık: tek adım → kitapçı · müşteri: eşik → koridorun sağı → sağ üçüncü kitaplık · kitap: raf → iki el
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı kapı, demet, kasa ya da araba [DERS 48 · 49].
⛔ Tek parça büyük cam YOK, tavandan sarkan kaldırıcı YOK [DERS 88]. Kitaplık kapıdan dik GİRMEZ (kapı 2,0 m · kitaplık 2,1 m).
⛔ Basınçlı su, hortum, püskürtme YOK — duvar yalnız el aletiyle [DERS 67]. Kitaplık yerinde BOYANMAZ (boyalı gelir — sahip seçimi).
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI · DERS 104]

```
G0     05:55 (71,1°/+14,2°) · ⭐ sağ (doğu) pencerelerden alçak altın güneş, uzun bantlar zemini geçip sol duvara/koltuklara
G1     07:55 (89,2°/+36,4°) · bantlar zeminin sol yarısında, kısa
G2     09:55 (114,2°/+58,5°) · küçük lekeler sağ pencerelerin hemen altında
G3     11:55 (176,2°/+72,4°) · ⭐ doğrudan güneş YOK, eşit parlak gün ışığı
G4     13:55 (242,7°/+60,2°) · küçük lekeler sol pencerelerin hemen altında
G5     15:55 (269,1°/+38,3°) · lekeler sol pencerelerden zeminin sağ yarısına
G6     17:55 (287,4°/+16,0°) · ⭐ uzun altın bantlar sol pencerelerden sağ kitaplıklara
G7     19:55 (306,2°/−4,1°) · ⭐ erken mavi saat · pencereler ve kapı mavi · bütün lambalar SÖNÜK
G8     19:55:08 · ⭐ aynı mavi · dört sarkıt + masa lambası YANIK · yakın tavan KOYU
⛔ Pencere lekeleri TEK YÖNDE yürür (sol yana düşen sabah → leke yok → sağ yana düşen akşam); geri dönen kare = zaman ters → ❷ [DERS 98]
⛔ İş lambaları G0–G6 boyunca AYNI soğuk beyaz — iç ışığın rengi değişirse "grade" okunur [DERS 104]
⛔ G0–G7 boyunca hiçbir sarkıt / masa lambası yanmaz · ilk kez G8'e giden klipte, TEK KAREDE
⛔ Pencere ya da kapı patlarsa (beyaz düz alan, huş ağaçları / tuğla duvar okunmuyorsa) zaman taşıyıcısı ölür → kare yeniden
```

## 6. ⭐ BİR VAGON · İKİ İŞÇİ · TEK MÜŞTERİ · YAZISIZ KİTAP KAPISI [DERS 55 · 59 · 89 · 42]

```
Korpus riski: "bookshop" → kalabalık müşteri, kasa, tabela, kitap yığını kuleleri, yazılı sırtlar · "railway carriage" → ray, lokomotif, ikinci
vagon, peron kalabalığı (ÇIKARIM — bu filmde ölçülmedi). spray · hose · jet · fountain · locomotive · passengers · crowd · neon · signage ·
television promptta YOK.
① sayım cümlesi her karede POZİTİF ("one carriage with eight windows and one far door, and the only carriage in view") · "Only two workers are
  in view" her I2V'de · G7–G8'de "No workers are present" + TEK müşteri
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç pencere / kaç kaburga / kaç kitaplık
⛔ ikinci müşteri · üçüncü işçi · dokuzuncu pencere · altıncı kaburga · dokuzuncu kitaplık · beşinci sarkıt · ikinci kapı · ray · lokomotif · kasa
   (yazar kasa) · tabela · makine → ⑧
⛔ Model pencere sırasını, tavanı, kaburgaları, alın duvarını ya da kapıyı yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Kitap sırtlarında, tezgâhta, kapıda, duvarda okunur yazı (başlık, harf, numara, tabela) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 süpürme, üç torba · S1 tahtalar kalkar, yığın · S2 cam çıkar, meşe gelir, ilk şerit · S3 sekiz cam · S4 kitaplıklar, ray + merdiven ·
  S5 uzak raflar, tezgâh · S6 koltuk, ekip çıkar, müşteri eşikte · S7 tutuş (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · kalabalık sesi YOK · vagon-içi yankı + pencerelerden kuş ve uzak rüzgâr yatak · metal çarpışma,
  patlama YOK
· 0,0 cıvata sökümü, arabanın tekerleği · 8–15 levye, tahta çatırtısı · 16–23 kazıyıcı, fırça, cam kırığı · 24–31 lastik tokmak, cam · 32–39
  kitaplığın dikilişi, vida tabancası · 40–47 kitapların rafa konuşu, kasa kapakları · 48–55 kitaplar, koltuğun inişi, uzaklaşan tekerlekler ·
  ⭐ 55,5 eşikte tek adım · ⭐ 56,5 anahtar tıkı + lamba uğultusu (KARE SENKRON ±2 kare) · 56,5–59,5 ahşapta adımlar · ⭐ 59,0–60,0 kitabın raftan
  kayışı + kapak · 60,0–64,0 tek sayfa, uğultu
· KART 64,0–69,0: uğultu + uzak akşam kuşları sürer, kartın son saniyesinde söner → döngüde S0'ın anahtar sesine bağlanır
```

## 9. Zaman ve ışık

```
G0 05:55 71,1°/+14,2° · G1 07:55 89,2°/+36,4° · G2 09:55 114,2°/+58,5° · G3 11:55 176,2°/+72,4° · G4 13:55 242,7°/+60,2° ·
G5 15:55 269,1°/+38,3° · G6 17:55 287,4°/+16,0° · G7 19:55 306,2°/−4,1° · G8 19:55:08 (aynı)
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · açık gök · sahneler arası haftalar KESMEDE)
· zaman pencerelerden zemine düşen güneş lekeleriyle taşınır (sabah sağdan sol yana → öğle leke yok → akşam soldan sağ yana); final mavi saatte
  lambalarla
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 × 8), beyanlı
① KADRAJ        24 mm · tilt 0 · h 1,7 m · yan duvarlar Y < 2,8 m'de kadraj dışı · pencereler ve kitaplık ön yüzleri sıyırma açısında dar
                şerit (kitaplar RENK ŞERİDİ okunur) · kapı küçük (70 × 182 px) · müşterinin kitabı ≈ 30 px — beyanlı
⑤ DEVAMLILIK    zemin (tahta → çelik → meşe), duvar (boya → gri), cam (kırık → yok → yeni), raflar (yok → boş → dolu) KASITLI değişir; pencere
                sırası, tavan, kaburgalar, fren kutusu, alın duvarı, kapı DEĞİŞMEZ · el arabası ve iş lambaları G0–G6, müşteri G7–G8 KASITLI
❷ ZAMAN         zaman pencere lekelerinde ve pencerelerin rengindedir; iç ışık S0–S6 sabit · sahneler arasında haftalar, saat tek yön (beyanlı)
⑦ İŞ            S7'nin 4–8'inde iş yok (kasıtlı tutuş) · G7–G8 işçisiz (kasıtlı) · finalde hareket dükkânın kullanılmasıdır (ışık + müşteri)
                [SANTIYE_HAREKETI §4.7]
❺ TESLİM        işlev anı ışık — LAST STOP · GAME ON · TOTAL RESET · POOL ROOM · UNDERWATER OBSERVATORY · COLOSSUS · THE TURNTABLE · LIT AGAIN'de
                de var (DOKUZUNCU, sahip onayladı 25.10.2026) · fark: ilk müşteri bir kitap çeker · LAST STOP (araç içi) · THE TURNTABLE (aynı
                koridor kadrajı) ile akraba — beyanlı
⑬ BAŞLIK        kart başlığı 6 kelime, iki satır (sahip seçimi; KAPAK_STIL "1–3 kelime" der) — beyanlı
```
