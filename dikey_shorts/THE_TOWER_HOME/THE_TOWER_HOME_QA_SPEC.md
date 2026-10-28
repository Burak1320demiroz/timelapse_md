# 🔍 THE TOWER HOME — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_TOWER_HOME_DIKEY_TIMELAPSE.md` · Günlük: `THE_TOWER_HOME_URETIM_GUNLUGU.md` · Kapak: `THE_TOWER_HOME_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE TOWER HOME · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 27.10.2026 · kural 7 × 8 · sahibin briefi "8 × 8 sn, tek zincir, 9 G, tek adam") · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "OLD WATER TOWER / BECOMES A HOME") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 G (gerçek zaman, 1×) — tek dikiş 56,0'da
IŞIK      DIŞ MEKÂN · SAAT TEK YÖNDE, ince yüksek bulutlu açık gök: 06:25 → … → 20:25 → 20:25:08 (güneş saati) · 41° kuzey · 21 Haziran
          (δ +23,4°) · kamera 0°'ye (kuzey) bakar, tilt 0, 24 mm, h 1,5 m · güneş HİÇBİR karede yok · zaman gölgelerde (sabah sola → öğle
          altta → akşam sağa) ve tankın renginde · final MAVİ SAAT (−8,5°): pencereler S7'de TEK KAREDE yanar
AİLE      KULE · ana yapı = tank + teras + ayaklar (py 326–1057) · başlık alanı kulenin önündeki çıplak çakıl (A bandı, py 1060–1240)
TAKVİM    sahneler arasında günler (KESMEDE), sahne içinde 2 sa / 8 sn (beyanlı)
EKİP      ⚠️ TEK ADAM (sahibin briefi) — kapının "≥ 3 el" FIX'i beyanlı; yoğunluk akışla (pikap kasası · yığın · tankın yüzeyi) · İSKELE YOK
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① PENCERELER — TAM üç yuvarlak pencere, tankın ön yüzünde yan yana, 3. ve 4. bandın arasında (x 457 · 540 · 623 · py 456–515), içeriden
    sıcak sarı YANIK · açık kapı (x 576–625 · py 522–640) aynı ışıkla · ışık teras tahtalarına ve korkuluğa düşer · dördüncü pencere,
    teras lambası, ip ışık YOK
  ② ADAM — TAM bir insan, terasın sağ önünde kapının yanında oturuyor, bacakları korkuluğun altında, yüzü sağdaki tarlaya, yüz okunmuyor
  ③ KULE EV — koyu parlak kahve tank (x 417–663) · TAM beş koyu gri bant (ikincisi kapının çelik çerçevesinde biter) · konik çatı +
    havalandırma kapağı · halka teras + korkuluk (x 358–722) · sağ önde sarmal merdiven (x 681–767) · koyu gri dört ayak
  ④ TANIKLAR — meşe · pompa evi köşesi · çakıl yol (tekerlek izleri) · meşenin altında çıplak toprak · solda TAM iki güneş paneli,
    kameraya eğik · düz ufuk · koyu mavi gök · pikap YOK, yığın YOK, ip YOK, merdiven YOK, su YOK

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ ≈ 56,5'te (2x: 28,25) üç pencere ve kapı TEK KAREDE yanar ve YANIK kalır. Sırayla "dolar"sa, titrer, söner, yeniden yanarsa → S7 atılır
   [ISIK_FINALI · DERS 98].
⛔ 56,5–60,0'da (2x: 28,25–30,0) adam kapı ağzından terasa SÜREKLİ hareketle çıkar ve oturur. Işınlanır, ikiye çıkar ya da yüzü kameraya
   dönerse → S7 atılır [DERS 96 · 15].
⛔ Işık yanarken tank, merdiven, teras, paneller KAYARSA / yeni nesne belirirse (ikinci insan, teras lambası, dördüncü pencere, araç) →
   S7 atılır [DERS 91 ③].
⛔ Pencerelerin ışığı başlık bandını (py 1060–1240) aydınlatırsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: pencereler aynı, adam oturuyor, hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık (iki satır),
   erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta rüzgâr + cırcır böcekleri (dijital sessizlik DEĞİL) [DERS 100].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0 · 24 mm · h 1,5 m)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk | py 960 (%50) | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ tank silueti + çatı | x 417–663 (245 px) · çatı tepesi py 349 · havalandırma 326 | KESİR ±7 px · DOKUZ KAREDE (nirengi ①) · biçim aynı, yüzey değişir |
| ⭐ beş bant | py 389 · 448 · 514 · 579 · 645 (ön yüz) | DOKUZ KAREDE TAM beş · G5→ ikincisi kapı çerçevesinde biter |
| ⭐ dört ayak | dip x 420 / 660 (ön) · 442 / 638 (arka) · py 1057 / 1039 | DOKUZ KAREDE TAM dört · DİK (tilt 0, yakınsama yok) |
| ⭐ meşe + yol | gövde x 144 · taç tepesi py 512 | DOKUZ KAREDE (nirengi ②) |
| ⭐ pompa evi + ufuk | x 964–1080 · py 878–1097 · ufuk 960 | DOKUZ KAREDE (nirengi ③) |
| ⭐ ayak rengi | G0 paslı (sol ön yarı çıplak) · G1 çıplak gri · G2→ koyu gri | tek yön |
| kırık eski merdiven | x ≈ 397 · py 666–1058 | G0–G1 · G2→ yığında |
| alüminyum merdiven | G1–G2 tanka (yerden) · G3 terasta · G4→ pikapta | TEK |
| ⭐ sarmal merdiven | x 681–767 · py 672–1056 | G2→ · TEK · orta direkli · beton tabanlı |
| ⭐ halka teras | x 358–722 · ön kenar py 680 · küpeşte 575 | G3→ · sekiz konsol · merdivende açıklık |
| ⭐ tank yüzeyi | G0 gri, 2 boşluk · G1–G3 gri, 6 boşluk · G4 ham açık · G5 + 4 açıklık · G6→ koyu kahve | tek yön |
| ⭐ üç pencere + kapı | x 457 · 540 · 623 · py 456–515 · kapı x 576–625 · py 522–640 | G5 karanlık delik · G6–G7 cam (G7 sönük) · G8 yanık |
| ⭐ ip + oturak | havalandırma → tank önü → teras | G4–G5 · G6 pikapta sarılı · G7→ yok |
| ⭐ pikap | x 748–935 · py 940–1034 | G0 yolda · G1–G6 park, aynı yer ±20 px · G7→ YOK (iz) |
| ⭐ çürük ahşap yığını | x ≈ 180–280 · py ≈ 988–1031 | G0 küçük → G5 büyük → G7→ yok (çıplak toprak) |
| ⭐ güneş panelleri | x 256–369 · py 953–1061 | G7→ TAM iki, kameraya eğik |
| adam | yerde ≈ 112 px · terasta ≈ 121 px · oturunca ≈ 75 px | TAM BİR · yüz yok |

## 3. ⭐ KULENİN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ gri tank, iki boşluk · paslı ayaklar, sol ön yarı çıplak · KIVILCIM · kırık merdiven sol ön ayakta · yığında iki tahta · pikap YOLDA,
    kasası dolu
G1  ⭐ dört ayak çıplak gri · altı boşluk · alüminyum merdiven tanka dayalı · pikap PARK, kapağı açık · yığın büyüdü
G2  ⭐ ayaklar koyu gri · ⭐ sarmal merdiven tank tabanına · kırık merdiven yığında · pikapta konsollar
G3  ⭐ sekiz konsol + halka teras + korkuluk · alüminyum merdiven terasta, çatı kenarına · tank hâlâ gri, altı boşluk
G4  ⭐ tank ham açık, bütün · bantlar koyu gri çelik · ⭐ ip + oturak havalandırmadan · alüminyum merdiven pikapta · yığın büyüdü
G5  ⭐ üç yuvarlak + kapı boşluğu, içi KARANLIK · çelik kapı çerçevesi · ⭐ üç disk + kapı paneli yığında · terasta talaş
G6  ⭐ tank koyu parlak kahve · ⭐ üç cam (altın gök yansıması) · ⭐ kapı (kapalı) · ip pikapta · pikapta iki panel · adam çerçeve taşıyor
G7  ⭐ iki panel solda, kablo · yığın YOK (çıplak toprak) · pikap YOK (iz) · kapı açık · pencereler SÖNÜK · mavi saat
G8  ⭐ pencereler + kapı YANIK · ⭐ adam terasta oturuyor
⛔ SAYIM: kule 1 · ayak 4 · bant 5 · meşe 1 · pompa evi 1 · adam 1 (dokuz karede) · pikap (1·1·1·1·1·1·1·0·0) · kırık merdiven (1·1·0…) ·
   alüminyum merdiven (pikapta·tankta·tankta·terasta·pikapta·pikapta·pikapta·0·0) · sarmal merdiven (0·0·1·1·1·1·1·1·1) · konsol
   (0·0·0·8·…·8) · yuvarlak pencere (0·…·0·3·3·3·3) · kapı (0·…·0·1·1·1·1) · ip (0·0·0·0·1·1·pikapta·0·0) · panel (pikapta…·2·2) — ikinci
   insan HİÇBİR klipte yok [DERS 89] · iskele, vinç, makine YOK
⛔ Ayakların ve tankın BİÇİMİ, bantlar, çatı, meşe, pompa evi, yol ve ufuk dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  pas: taşlama → ayak → toz · pikap: yol → kulenin sağı (park) · alüminyum merdiven: pikap kasası → tank önü · çürük tahta: tank → çakıl →
    meşenin altındaki yığın
S1  kırık merdiven: sol ön ayak → çakıl → yığın · boya: fırça → ayaklar (alttan üste) · merdiven parçası: pikap → sağ ön ayağın yanı →
    beton taban + orta direk (ALTTAN ÜSTE) · konsol: pikap → merdiven
S2  konsol: pikap → merdiven → ayak başı + tank tabanı (sekiz) · tahta demeti: pikap → merdiven → konsollar (merdivenden İKİ YÖNE) ·
    korkuluk: pikap → teras kenarı · alüminyum merdiven: çakıl → teras
S3  ip: adam → alüminyum merdiven → havalandırma kapağı → tank önü · alüminyum merdiven: teras → merdiven → pikap · yeni tahta: pikap →
    teras → boşluk · eski tahta: tank → çakıl → yığın · zımpara: ip oturağı (yukarıdan aşağı)
S4  disk: tank → ip → teras → merdiven → yığın (üç) · kapı paneli: aynı yol · çelik çerçeve: → ikinci bandın kesik uçları
S5  yağ: fırça → tank (yukarıdan aşağı) · cam: pikap → merdiven → yuvarlak açıklık (üç) · kapı: pikap → çerçeve menteşesi · ip: çatı →
    pikap · çerçeve: pikap → çakıl
S6  çerçeve: → sahanın solu · panel: pikap → çerçeve (iki) · kablo: panel → merdivenin dibi · ahşap: yığın → pikap kasası · pikap: → yol
    → kadraj dışı · adam: yol → merdiven → kapı
S7  ışık: tek adım → üç pencere + kapı · adam: kapı ağzı → teras (oturur)
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı pikap kasası; sökülen her şey yığına, yığın pikaba [DERS 48 · 49 · 95].
⛔ İskele, vinç, kanca, makine YOK — her şey sarmal merdiven, teras, alüminyum merdiven ve iple [plan TASARIM ③].
⛔ Pencereler KESİLİR: diskler yığında görünür, açıklıkların içi karanlık [plan TASARIM ⑥].
⛔ Basınçlı su, sprey YOK — yağ fırçayla [DERS 67]. Tankta su, sızıntı YOK [DERS 42].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI · DERS 45 · 98]

```
G0     06:25 (75,6°/+19,7°) · ⭐ sağdan alçak altın ışık, ince yüksek bulut, ayakların gölgeleri uzun SOLA · kıvılcım
G1     08:25 (94,3°/+42,1°) · sağdan, gölgeler kısalır · çıplak metal parlar
G2     10:25 (124,2°/+63,5°) · sağ-arkada yüksek, kısa gölgeler · ıslak boya parlar
G3     12:25 (198,5°/+71,7°) · ⭐ tepede, kameranın arkasında · terasın altında koyu gölge halkası
G4     14:25 (251,2°/+55,0°) · soldan yüksek, ham tankın solu sıcak, kısa gölgeler SAĞA
G5     16:25 (273,9°/+32,7°) · soldan, açıklıklar içi karanlık, gölgeler SAĞA
G6     18:25 (291,9°/+10,7°) · ⭐ altın akşam, yağlı tank sıcak parlar, camlarda altın gök, uzun gölgeler SAĞA
G7     20:25 (311,6°/−8,5°) · ⭐ mavi saat, doğrudan ışık yok · ufukta solda son ışık · pencereler SÖNÜK
G8     20:25:08 · ⭐ aynı mavi · pencereler + kapı YANIK · başlık bandı koyu çakıl
⛔ Gölgeler TEK YÖNDE döner (sola → altta → sağa); geri dönen kare = zaman ters → ❷ [DERS 98]
⛔ G6'da camlar YALNIZ gökyüzünü yansıtır, içeriden ışık yok · ilk ışık G8'e giden klipte, TEK KAREDE
⛔ G7–G8 zifiri karanlık değildir: tank, ayaklar, teras, paneller, adam okunur [DERS 45]; okunmuyorsa kare yeniden
```

## 6. ⭐ BİR KULE · TEK ADAM · İSKELESİZ · YAZISIZ YÜZEY KAPISI [DERS 42 · 55 · 59 · 69 · 89]

```
Korpus riski: "water tower" → su, ikinci kule, depo · "tower + light" → deniz feneri · "home" → çiçekli balkon, ikinci kat pencere sırası
(ÇIKARIM — SKY VAULT'ta "water tank" ölçüldü, DERS 42). crane · hoist · scaffold · silo · lighthouse · spray · hose · fountain · neon ·
beam · drone · bunker · cabin promptta YOK (YASAK KELİME).
① sayım cümlesi her karede POZİTİF ("This is one gravel yard with one water tower and one man, the only person in view") · "Only one man is
  in view for the whole shot — no one else ever appears — and he does one job at a time" her S0–S6 I2V'de
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç insan / kaç ayak / kaç bant / kaç pencere
⛔ ikinci kule · su · iskele · vinç · ikinci insan · dördüncü pencere · ikinci kapı · ikinci sarmal merdiven · teras lambası · üçüncü panel →
   ⑧
⛔ Model ayakları, tankın biçimini, çatıyı, meşeyi ya da pompa evini yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Pikapta, pompa evinde, tankta ya da panellerde okunur yazı (harf, rakam, logo, plaka) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 alüminyum merdiven + çürük tahtalar · S1 sarmal merdiven yükselir · S2 korkuluk + merdiven terasa · S3 zımpara yukarıdan aşağı · S4 kapı
  + diskler yığına · S5 cam + kapı, ip iner · S6 pikap çıkar, adam kapıya · S7 tutuş (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · RÜZGÂR ve tarlada otlar bütün filmin yatağı · motor yalnız pikap (S0 gelir · S6 gider)
· 0,0 taşlama çığlığı + pikabın motoru · 8–15 çelik parçaların çınlaması, anahtar, fırça · 16–23 matkap, tahtaların konsollara düşüşü ·
  24–31 ip, zımpara, tel fırça · 32–39 dekupaj testere (×3), diskin terasa düşüşü · 40–47 fırça, camın oturuşu, menteşe · 48–55 cıvata,
  ahşabın kasaya düşüşü, uzaklaşan motor, merdivende ayak sesleri · ⭐ 56,5 tek düğme tıkı (KARE SENKRON ±2 kare) · 56,5–60,0 teras
  tahtalarının gıcırtısı · 60,0–64,0 cırcır + rüzgâr
· KART 64,0–69,0: cırcır + rüzgâr sürer, kartın son saniyesinde söner → döngüde S0'ın taşlama çığlığına bağlanır
⛔ Müzik ya da konuşma → teslim değil (sahip kuralı 21.09.2026)
```

## 9. Zaman ve ışık

```
G0 06:25 75,6°/+19,7° · G1 08:25 94,3°/+42,1° · G2 10:25 124,2°/+63,5° · G3 12:25 198,5°/+71,7° · G4 14:25 251,2°/+55,0° ·
G5 16:25 273,9°/+32,7° · G6 18:25 291,9°/+10,7° · G7 20:25 311,6°/−8,5° · G8 20:25:08 (aynı)
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · ince yüksek bulutlu açık gök · sahneler arası günler KESMEDE)
· zaman gölgelerle ve tankın rengiyle taşınır (sabah sağdan sola → öğle altta → akşam soldan sağa); final mavi saatte üç pencere
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 × 8), beyanlı
① KADRAJ        24 mm · tilt 0 · h 1,5 m · tank 245 px (%23) · pencere Ø 50 px · bant ≈ 6 px · adam ≈ 112–121 px — beyanlı
⑤ DEVAMLILIK    ayak rengi (pas → çıplak → koyu gri), tank yüzeyi (gri → ham → koyu), açıklıklar (yok → delik → cam), erişim (kırık merdiven →
                sarmal + teras), pikap ve yığın (gelir → gider) KASITLI değişir; ayakların ve tankın biçimi, bantlar, çatı, meşe, pompa
                evi, yol, ufuk DEĞİŞMEZ
❷ ZAMAN         zaman gölgelerde ve tankın renginde; sahneler arasında günler, saat tek yön (beyanlı) · rejim dikişi 56,0'da
⑦ İŞ            ⚠️ TEK ADAM (sahibin briefi) — "tek el, düşük yoğunluk" denebilir; yoğunluk akışla taşınır · S6'da adam pikabı sürüp
                yürüyerek döner (beyanlı) · S7'nin 4–8'inde iş yok (kasıtlı tutuş) · finalde hareket evin kullanılmasıdır (ışık + oturan
                adam) [SANTIYE_HAREKETI §4.7]
❺ TESLİM        işlev anı ışık — YAYIN_PLANI'na göre ON İKİNCİ (… THE DRIVE-IN · THE RIVER HUT), plana girmemiş OPENING NIGHT · SUNKEN GARDEN ·
                MENDED SPAN ile on beşinci · üretimde üst üste üçüncü · THE SKY VAULT (paslı depo → ışıklı oda) ile akraba — beyanlı
⑬ BAŞLIK        kart başlığı 6 kelime, iki satır (sahip seçimi; KAPAK_STIL "1–3 kelime" der) — beyanlı
```
