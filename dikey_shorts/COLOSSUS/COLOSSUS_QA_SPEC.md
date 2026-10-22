# 🔍 COLOSSUS — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `COLOSSUS_DIKEY_TIMELAPSE.md` · Günlük: `COLOSSUS_URETIM_GUNLUGU.md` · Kapak: `COLOSSUS_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      COLOSSUS · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 22.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "COLOSSUS") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK ("MUD TO MATCHDAY" düştü)
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 A (10 dk) — tek dikiş 56,0'da
IŞIK      SAAT TEK YÖNDE, AÇIK GÖK: 05:55 → 07:55 → 09:55 → 11:55 → 13:55 → 15:55 → 17:55 → 19:55 → 20:05 (güneş saati) ·
          41° kuzey · 21 Haziran (δ +23,4°) · güneş 71,1°/+14,2° → 308,0°/−5,6° · kamera 0°'ye (kuzey) bakar, tilt 27° AŞAĞI, 20 mm ·
          güneş HİÇBİR karede kadrajda değil · final MAVİ SAAT: iki direğin projektörleri yanar
AİLE      ⭐ZEMİN · saha %29,5–55,4 · başlık alanı uzak alçak tribünün ardındaki park + ağaç kuşağı
TAKVİM    sahneler arasında haftalar (KESMEDE), sahne içinde 2 sa / 10 dk (beyanlı); zaman taşıyıcısı tribün gölgesi (sağ → ayak → sol) + gök
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① IŞIKLI SAHA — TEK dikdörtgen yeşil saha (yakın kale çizgisi x 171–909 · py 1354 · uzak x 367–713 · py 857), hafif açık/koyu enine
    bantlar, TEK beyaz çizgi düzeni (tek merkez dairesi, iki ceza alanı, iki kale alanı) · kadrajın EN PARLAK şeyi saha
  ② DONANIM — TAM İKİ beyaz kale (ağlı) iki kale çizgisinin ortasında, ağızları birbirine bakar · TAM DÖRT sarı köşe bayrağı · kaleler
    kameraya doğru yumuşak gölge atar
  ③ TRİBÜNLER — iki uzun yanda iki katlı kobalt mavi koltuk blokları, iki uçta tek alçak mavi kat · merdiven aralıkları gri · koltuklarda
    harf / arma / desen YOK · koltuklar BOŞ
  ④ TANIKLAR — kadrajda TAM İKİ direk, lamba başları beyaz yanık (x 161–196 · 884–919 · py 517–556) · tünel ağzı sol altta karanlık ve boş
    (x 104–184) · uzak tribünün ardında KOYU park + ağaç kuşağı · koyu mavi gök · insan yok, makine yok, geçici eşya yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–58,0'da (2x: 28,0–29,0) iki saha görevlisi el arabasıyla tünele girer, kadrajdan çıkar.
⛔ 58,0'da (2x: 29,0) sol direk, 59,0'da (2x: 29,5) sağ direk yanar ve İKİSİ DE yanık kalır. Titrer, söner, yeniden yanarsa → S7 atılır
   [DERS 98].
⛔ Işık yanarken kaleler, bayraklar, çizgiler, koltuklar KAYARSA / yeni nesne belirirse (seyirci, oyuncu, top, hakem, skorbord, ekran, çatı,
   havai fişek, lazer huzmesi, üçüncü direk) → S7 atılır [DERS 91 ③].
⛔ Projektör ışığı tribünleri ya da kaleleri karartırsa (paketin kontrolü) / park + ağaç kuşağı aydınlanırsa (başlık zemini) → sebep G8;
   KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: hiçbir şey değişmez (yalnız bayraklar ve ağlar kıpırdar); ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık, erime
   ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after", "BUILDWAKE" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta akşam rüzgârı + projektör vızıltısı (dijital sessizlik DEĞİL) [DERS 100].
⛔ Bir figürün yüzü okunursa ya da üçüncü figür belirirse S7 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 27° aşağı · 20 mm)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk | py ≈ 417 (%78,3) | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ uzak alçak tribünün üst kenarı + ağaç kuşağı | py 740 · ağaç 611–679 | DOKUZ KAREDE (nirengi ①) |
| ⭐ saha dikdörtgeni | yakın x 171–909 · py 1354 · uzak x 367–713 · py 857 | KESİR ±7 px · DOKUZ KAREDE (nirengi ②) · ⚠️ yakın köşeler kadrajda değilse lens kaymıştır (20 → 24 mm) → G8 yeniden |
| ⭐ tünel ağzı | x 104–184 · py 1348–1408 | ±20 px · DOKUZ KAREDE (nirengi ③) · hiçbir karede kapanmaz |
| ⭐ iki direk | x 176–217 · 863–904 · py 517–804 | TAM İKİ · G0–G7 sönük · G8 yanık |
| uzak alçak tribün | py 740–835 · tek kat | DOKUZ KAREDE tek kat |
| yakın alçak tribün | py 1457–1666 · kadraj boyu | tek kat · G3→ mavi |
| ⭐ yan tribünlerin üst katı (uzak yarı) | üst kenar x 41–109 · 971–1039 · py 674–714 | G0–G1 çıplak kiriş · G2 gri basamak · G3→ mavi |
| ⭐ vinçler | taban ≈ x 127 / 953 · py ≈ 823 (uzak köşelerin dışı) | G0–G2 · kanca HER KAREDE YÜKLÜ · G3→ yok |
| ⭐ buldozer (G0) | x 416–475 · py 1179–1239 | YALNIZ G0 sahada · bıçak çamurda |
| ⭐ makineler tünel ağzında | x ≈ 65–184 · py ≈ 1340–1445 | G0 ekskavatör + kamyon · G1 buldozer + ekskavatör · G4–G6 yükleyici |
| ⭐ ilk mavi sıra (G2) | yakın tribünün önü, orta (x ≈ 480–600 · py ≈ 1450) | TEK kısa sıra |
| ⭐ çim paletleri (G4) | uzak kale çizgisinin arkası (py ≈ 840–850) | uzak uçta |
| ⭐ ilk beyaz çizgi (G5) | yakın sol köşeden yakın kale çizgisi boyunca kısa | TEK parça |
| ⭐ kaleler | yakın x 500–580 · py 1331–1354 · uzak x 521–559 · py 843–857 | G7→ TAM İKİ |
| işçi | ≈ 12–16 px | DÖRT (S7'de iki görevli) · yüz yok |

## 3. ⭐ STADYUMUN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ koyu kahve çamur, alçak yığınlar, tekerlek izleri · ⭐ buldozer yakın üçte birde, bıçağı çamurda, arkasında TEK açık şerit ·
    ekskavatör (kovası dolu) + damperli kamyon tünel ağzında · alt katlar bitmiş çıplak gri beton · ⭐ iki uzun yanda üst kat yalnız çıplak
    eğik kiriş · ⭐ uzak köşelerin dışında iki vinç (kancada spreader kirişi) + prekast istifleri · küçük ekip · direkler sönük
G1  ⭐ saha tek düz açık kahve tesviye tabanı (ince paralel bıçak izleri) · yığın YOK · kamyon YOK · buldozer + ekskavatör tünel ağzında
    park · ⭐ her vinçte istifin hemen üstünde bir prekast basamak birimi · dört işçi sol üst kat kirişlerinin uzak ucunda
G2  ⭐ iki uzun yanda üst kat sürekli gri prekast basamak · istifler bitti · vinçlerde spreader kirişi · buldozer + ekskavatör YOK · tünel
    ağzında iki koltuk paleti + el transpaleti · ⭐ yakın tribünün önünde TEK kısa mavi sıra
G3  ⭐ bütün tribünlerde kobalt mavi bloklar · merdivenler GRİ · vinç YOK · tünel ağzında boş palet + torba + film · saha hâlâ tesviye
G4  ⭐ açık bej kum kök tabakası (sürükleme izleri) · yükleyici tünel ağzında · ⭐ çim paletleri uzak kale çizgisinin arkasında
G5  ⭐ saha tamamen yeşil, ENİNE açık/koyu bantlar · yükleyici + serme çerçevesi, artık rulolar, boş paletler, boya varilleri, el silindiri
    tünel ağzında · ⭐ çizgi arabası yakın sol köşede + TEK kısa beyaz çizgi
G6  ⭐ TAM çizgi düzeni (tek daire, iki ceza alanı, iki kale alanı, yaylar, noktalar) · araba tünel ağzında, varillerle
G7  ⭐ iki kale + dört bayrak · servis şeridi BOŞ · iki saha görevlisi + el arabası tünel ağzında · erken mavi saat · direkler sönük
G8  ⭐ iki direk YANIK · saha beyaz ışıkta · insan YOK
⛔ SAYIM: stadyum 1 · saha 1 · tünel 1 · kadrajda direk 2 (sönük ×8 · yanık G8) · vinç (2·2·2·0·…) · buldozer (1·1·0·…) · ekskavatör (1·1·0·…) ·
   kamyon (1·0·…) · yükleyici (0·0·0·0·1·1·1·0·0) · çizgi arabası (0·…·1·1·0·0) · kale (0·…·0·2·2) · bayrak (0·…·0·4·4) ·
   işçi (ekip·4·4·4·4·4·4·2·0) — kadro HİÇBİR klipte dördü aşmaz [DERS 89] · hareketli araç HİÇBİR anda birden fazla değil [DERS 69]
⛔ Sahanın dış çizgisi, tribün iskeleti ve merdiven aralıkları, tünel ağzı, iki direk, park ve ağaç kuşağı dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  çamur: saha → buldozer bıçağı (geniş şeritler, uzaktan yakın sola) → tünel ağzındaki yığın → ekskavatör kovası → kamyon kasası → kamyon
    tünelden çıkar · makineler SIRAYLA
S1  prekast birim: uzak köşedeki istif → vinç kancası (spreader + dört sapan) → DÜŞEY iniş → iki üst kat kirişi → cıvata · vinçler SIRAYLA ·
    baylar uzak köşelerden kameraya · buldozer, ekskavatör: → tünel · koltuk paleti: tünel → el transpaleti → servis şeridi
S2  vinç: köşe → dış yol → kadraj dışı (sırayla) · koltuk sırası: palet → ekip → merdiven → beton basamak (yakın tribünün önünden yukarı,
    çanak boyunca) · boş palet + film: → tünel ağzında istif
S3  kum: tünel → yükleyici kovası → tesviyeli taban (uzak kale çizgisinden kameraya) → tesviye kutusu · çim paleti: tünel → yükleyici →
    servis şeridi → uzak kale çizgisinin arkası · boş palet: ekip → tünel
S4  çim rulosu: palet (uzak uç) → serme çerçevesi → kök tabakası (enine şerit, uzaktan yakına) · yükleyici: → tünel ağzı · çizgi arabası:
    → yakın sol köşe
S5  boya: varil → araba → çim (yalnız arabanın ardında) · yeni varil: istif → işçi → araba · araba: → tünel ağzı
S6  kale: tünel → alçak kale arabası → saha boyunca → kale çizgisi (önce uzak, sonra yakın) · bayrak: el → köşe (×4) · araba, variller, rulolar,
    paletler: yükleyici → tünel · kale arabaları + el silindiri: ekip → tünel
S7  iki görevli + el arabası: tünel ağzı → tünel · ışık: iki adım → sol direk → sağ direk
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı tünel ağzı, uzak köşelerdeki istif, palet ya da araba [DERS 48 · 49].
⛔ Uzun rijit yük havada uzun yol TAŞINMAZ [DERS 57]: prekast birim istiften kirişe kısa salınım + DÜŞEY iniş. Bütün tribün tek parça
   gökten İNMEZ [DERS 79].
⛔ Çimden sonra ağır makine sahaya GİRMEZ (paketin kuralı): S4'te serme çerçeveli kompakt yükleyici yalnız serme sırasında; S6'da yükleyici
   yalnız servis şeridinde.
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI]

```
G0     05:55 (71,1°/+14,2°) · ⭐ serin sabah · sağ tribünün uzun gölgesi sahanın sağında · sol tribün sıcak ışıkta · solgun gök
G1     07:55 (89,2°/+36,4°) · parlak sabah · sağ gölge touch çizgisi boyunca bant
G2     09:55 (114,2°/+58,5°) · sağ tribünün ayağında kısa gölge
G3     11:55 (176,2°/+72,4°) · ⭐ en düz, en parlak · en kısa gölgeler
G4     13:55 (242,7°/+60,2°) · sol tribünün ayağında kısa gölge
G5     15:55 (269,1°/+38,3°) · ılık · sol gölge touch çizgisi boyunca bant
G6     17:55 (287,4°/+16,0°) · ⭐ altın akşam · sol tribünün uzun gölgesi sahanın solunda · sağ tribün altın
G7     19:55 (306,2°/−4,1°) · ⭐ erken mavi saat · gölgesiz · sol ufukta solgun kehribar · direkler SÖNÜK
G8     20:05 (308,0°/−5,6°) · ⭐ mavi saat · iki direk YANIK · park + ağaçlar KOYU
⛔ Tribün gölgesi TEK YÖNDE döner (sağ → ayak → sol); G6 → G7 gök TEK YÖNDE kararır; geri aydınlanan kare = zaman ters → ❷ [DERS 98 · 104]
⛔ G0–G7 boyunca HİÇBİR projektör yanmaz
⛔ Güneş diski HİÇBİR karede yok (kadraj ±31°, güneş 71° → 306°) [DERS 39 · 70] · disk belirirse kare yeniden
```

## 6. ⭐ BİR STADYUM · İKİ KALE · DÖRT İŞÇİ · TEK HAREKETLİ ARAÇ KAPISI [DERS 55 · 69 · 89 · 42]

```
Korpus riski: "football stadium" → seyirci kalabalığı, oyuncu, top, hakem, skorbord, dev ekran, çatı, havai fişek, çok sayıda direk ·
"construction" → kalabalık ekip, ikinci makine (ÇIKARIM — bu filmde ölçülmedi). crowd · spectators · players · referee · ball · scoreboard ·
screen · roof · fireworks · laser · sprinkler · fountain promptta YOK.
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ) · "Only four workers" ve "Exactly one vehicle moves at a time" her I2V'de · G8'de
  "No people are present."
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç makine aynı anda / kaç direk / kaç kale
⛔ ikinci saha · Amerikan futbolu çizgisi · ikinci merkez dairesi · üçüncü kale · beşinci bayrak · üçüncü direk · seyirci · oyuncu · top ·
   çatı · ekran · beşinci işçi · aynı anda iki hareketli araç · iki makinenin birbirinin içinden geçmesi → ⑧
⛔ Model saha dikdörtgenini, tribün iskeletini, tünel ağzını ya da direkleri yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Koltuklarda, tribün cephesinde, direklerde okunur yazı (numara, logo, kulüp adı, koltuk deseni) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 ekskavatör yükler, kamyon tünelden çıkar · S1 buldozer + ekskavatör çıkar, ilk mavi sıra · S2 mavi bloklar çanak boyunca · S3 tesviye
  kutusu, çim paletleri uzak uca · S4 son şeritler yakına, ilk çizgi parçası · S5 daire + ceza alanları · S6 bayraklar, temizlik, mavi saat ·
  S7 tutuş (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · SEYİRCİ SESİ YOK · açık hava rüzgârı + uzak kent yatak · metal çarpışma, patlama YOK
· 0,0 dizel motor + bıçak · 4–6 kova boşaltma · 6–8 kamyon tünelde · 8–15 vinç motoru, basamakların oturuşu (tok ×çok) · 16–23 koltuk tıkırtısı,
  cıvata, film · 24–31 yükleyici, kum, tesviye kutusu · 32–39 rulo açılışı, el silindiri · 40–47 çizgi arabası, boya · 48–55 kale arabası,
  kalenin oturuşu (×2), bayraklar (×4) · 56–58 adımlar, tünelde yankı · ⭐ 58,0 röle + vızıltı (sol) · ⭐ 59,0 röle (sağ) (KARE SENKRON ±2
  kare) · 60,0–64,0 akşam rüzgârı, bayrak dalgalanması, alçak vızıltı
· KART 64,0–69,0: rüzgâr + vızıltı sürer, kartın son saniyesinde söner → döngüde S0'ın motor homurtusuna bağlanır
```

## 9. Zaman ve ışık

```
G0 05:55 71,1°/+14,2° · G1 07:55 89,2°/+36,4° · G2 09:55 114,2°/+58,5° · G3 11:55 176,2°/+72,4° · G4 13:55 242,7°/+60,2° ·
G5 15:55 269,1°/+38,3° · G6 17:55 287,4°/+16,0° · G7 19:55 306,2°/−4,1° · G8 20:05 308,0°/−5,6°
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · açık gök · sahneler arası haftalar KESMEDE)
· zaman tribün gölgesiyle (sağ → ayak → sol) ve gökle taşınır; final mavi saatte, iki direğin projektörleriyle
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 sahne), beyanlı
① KADRAJ        20 mm · tilt 27° aşağı · yan tribünler yalnız uzak yarıda (kenarlarda kama) · uzak ceza alanı basık (≈ 40 px) · yakın direkler
                kadraj dışı · insan 12–16 px, bayrak ≈ 8 px — beyanlı
⑤ DEVAMLILIK    saha yüzeyi (çamur → tesviye → kum → çim → çizgi) ve tribün rengi (gri → mavi) KASITLI değişir; dış çizgi, tribün iskeleti,
                tünel, direkler DEĞİŞMEZ · vinçler yalnız G0–G2'de KASITLI
③ ŞANTİYE       S2'de vinçler kadrajın kenarından dış yola çıkar (plan RİSK ③) — yol uzak tribünün ardında görünür, beyanlı
⑦ İŞ            S7'nin 4–8'inde iş yok (kasıtlı tutuş) · G8 boş stadyum (kasıtlı: insansız final, kapak kaynağı) · insanlar iş KANITI değil,
                ölçek — iş yüzeyin ilerleyen sınırıyla okunur
❷ ZAMAN         sahneler arasında haftalar geçer ama saat tek yönde ilerler (beyanlı sıkıştırma) — mercek "aynı gün mü?" diyebilir
❺ TESLİM        işlev anı ışık — LAST STOP · GAME ON · TOTAL RESET · POOL ROOM · UNDERWATER OBSERVATORY'de de var (sahip bilerek onayladı
                22.10.2026, altıncı) · THE LAST LIFT ile konu akrabası (stadyum) — beyanlı
```
