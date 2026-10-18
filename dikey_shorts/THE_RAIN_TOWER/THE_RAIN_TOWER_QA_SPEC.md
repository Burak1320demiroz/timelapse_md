# 🔍 THE RAIN TOWER — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_RAIN_TOWER_DIKEY_TIMELAPSE.md` · Günlük: `THE_RAIN_TOWER_URETIM_GUNLUGU.md` · Kapak: `THE_RAIN_TOWER_KAPAK.md`

```
FİLM      THE RAIN TOWER · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 16.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "THE RAIN TOWER") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok
REJİM     S0 ⭐ A (10 dk) · S1–S6 B (2 sa) · S7 ⭐ G (gerçek zaman, 8 sn) — üç rejim
IŞIK      TEK GÜN: 05:40 → 05:50 → 07:50 → 09:50 → 11:50 → 13:50 → 15:50 → 17:50 → 17:50 + 8 sn (güneş saati) ·
          41° kuzey · 20 Ağustos (δ +12,1°) · güneş 78°/+4,2° → 278°/+9,8° · kamera KKD'ye (20°) bakar, tilt 0 ·
          final ALTIN AKŞAM: kolonların sol kenarları altın, kuyu yumuşak gölgede
AİLE      KULE · ufuk %50 · kule %27,2–58,3 · üstünde açık gök (kapak başlık alanı)
TAKVİM    yok — tek gün (haftalık iş sıkıştırıldı, beyanlı); zaman taşıyıcısı gölgelerin soldan sağa dönüşü + kuyudaki güneş
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① ŞELALE — tek beyaz şerit TAŞ AĞIZDAN (x ≈ 515–565 · y 861) kuru kayadan oyulmuş kanal boyunca (x 517–563 · 46 px)
    çukura (y 1312) iner; 46 × 451 px; kadrajın EN PARLAK şeyi; su YALNIZ taş ağızdan çıkar
  ② HAZNE — şelalenin dibinde köpük halkası ve halkalar; su seviyesi eşiğin BİR TAŞ SIRA altında (y %31,7), eşiğin üst
    sırası KURU; avluda su YOK
  ③ YEŞİL KAYA YÜZÜ — raylar arasında (x 426–654) sudan taş ağza kadar her cep yeşil, üst ceplerden sarkan saplar; iki
    paslı ray kayanın İKİ YANINDA açıkta
  ④ TANIKLAR — iki beton kolon (x 378 / 702) ve iki bağ kirişi pası ve boya kabuğuyla · sağda paslı kabin takozlarda
    (x 728–831) · pompa + kumanda kutusu, yanında TEK işçi sırtı kameraya · sepetli platform katlı, kapı yanında · altın akşam
    ışığı kolonların sol kenarlarında

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 57,0'da (2x: 28,5) düğme; 57,0–58,5 su taş ağızdan taşar; 58,5–60,0 kanaldan YUKARIDAN AŞAĞI iner. Su aşağıda belirip
   yukarı "dolarsa" ya da tek karede tamamı belirirse → S7 atılır.
⛔ Su borudan, kirişten, raydan, kolondan, kabinden ya da havadan fışkırırsa → S7 atılır [DERS 67].
⛔ 60,0–64,0 FİNAL TUTUŞU: akış sabit, seviye aynı, işçi kıpırdamaz; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63]
   (⚠️ akan su SSIM'i düşürür — eşik akış bölgesi dışında ölçülür; QA kaydına not).
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi +
   başlık, erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı
   [DERS 85]. klip_eslestir.py --kart 5 ile ölçülür.
⛔ Figürün yüzü okunursa ya da ikinci figür belirirse S7 atılır [P5-b].
⛔ G1'den sonra kuyunun İÇİNDE kabin, halat ya da asansör makinesi belirirse → ⑧ APPEARED [DERS 84].
⛔ G5–G7'de kanalda SU varsa "waterfall" kelimesi suyu erken çağırmıştır → kare atılır [plan RİSKLER ④].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | %50,0 — fabrika duvarının ve kulenin içinde (çizgi olarak görünmez) | — |
| ⭐ ön kolon dipleri (x · y) | 378 / 702 px (%35,0 / %65,0) · %27,2 | ±0,5 puan · DOKUZ KAREDE (nirengi ①) |
| ⭐ kule tepesi (y) | %57,2–58,3 (821–800 px) | ±0,5 puan · DOKUZ KAREDE (nirengi ①) |
| ⭐ fabrika kapısı (x · y) | 251–342 px · %30,8–40,6 | ±0,5 puan · DOKUZ KAREDE (nirengi ②) · hep KARANLIK açıklık |
| ⭐ uzak baca tepesi (x · y) | ≈ 918 px · %79,8 | ±1 puan · DOKUZ KAREDE (nirengi ③) |
| ⭐ kule ön yüz eni | 324 px | KESİR ±8 px · DOKUZ KAREDE |
| bağ kirişleri (y) | %37,5–38,6 · %47,8–48,9 | ±0,5 puan · SAYI 2 |
| ⭐ iki paslı ray (x) | 426 / 654 px | AYNI YER nesnesi · ±4 px · SAYI 2 · dokuz karede açıkta |
| çukur eşiği üstü (y) | %28,6 | DOKUZ KAREDE · G3→ üst taş sırası KURU |
| ⭐ su yüzü (y) | %31,7 (arka duvarda) · görünür bant 60 px | G3–G8 SABİT · G0–G2 YOK |
| ⭐ kanal (x) | 517–563 px · 46 px | G5→ · BOYUT DEĞİŞMEZ · G5–G7 KURU |
| ⭐ taş ağız (y) | %55,2 (861 px) | G4→ DEĞİŞMEZ |
| ⭐ kabin (x · y) | 728–831 px · G0 %33,8–41,0 (asılı) · G1→ %27,1–34,3 (takozda) | TEK · G1→ hareket etmez |
| pompa + kumanda kutusu | 642–678 · 704–718 px | G4→ |
| ⭐ işçi G7–G8 | ≈ 690–715 px · %26,2–31,3 · 97 px | TEK · sırtı kameraya |
| sepetli platform (park) | 278–352 px · ≤ %32,4 | G3–G6 çalışır · G7–G8 katlı, kapı yanında |
| vinç | sağ kenar, bom ucu %72,6 | YALNIZ G0 · G1'den sonra YOK |
| üst band | %87–100 | yalnız gök · güneş diski HİÇBİR karede |

## 3. ⭐ YAPININ İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  paslı kabin vinçte, sağ kolonun hemen sağında asılı (taban takozların ~2,5 m üstü) · kuyu BOŞ, KARANLIK · raylar arası
    boş · çukurda moloz, kablo, hurda · sarı vinç sağ kenarda, bom kulenin üstünden, kanca kabinin üstünde YÜKLÜ ·
    kapı yanında iki el arabası + kalas rampa + kısa boru · iki işçi takozlarda
G1  ⭐ kabin TAKOZLARDA, kafes kapı kameraya, zincirler tavanında · VİNÇ YOK (payanda izleri, teker izi) · moloz yığını ·
    kapı yanında + katlı big-bag yığını · dört işçi eşikte
G2  ⭐ çukur TEMİZ, KURU · eski taş sıraları görünür · ⭐ kısa gri boru vanadan eşiğin üstünden çukura, ucu aşağı ·
    rampa fabrika duvarına yaslı · arabalar kapıda + üç dolu torba
G3  ⭐ SU +0,40 (eşiğin bir sıra altı), arka duvarı yansıtır · vana kapalı · ⭐ katlı sepetli platform solda ·
    ⭐ ızgara + boru paleti (braket sandığı üstte) · rampa ve arabalar YOK
G4  ⭐ galvaniz IZGARA raylar arasında · ⭐ gri BORU sağ arka köşeden tepeye ve ortaya · ⭐ koyu TAŞ AĞIZ tepede ortada ·
    ⭐ POMPA + kumanda kutusu vananın yanında, emme suya · ⭐ kaya paneli paleti · su aynı
G5  ⭐ KAYA YÜZÜ raylar arasında suyun üstünden taş ağza · ızgara HİÇ görünmez · ⭐ ortada KURU kanal · boş topraklı
    cepler · ⭐ bitkili tepsi paleti · su aynı
G6  ⭐ ALT BANTLAR YEŞİL (sudan 2. bağ kirişine) · üst bant çıplak · kanal kuru · boş tepsi yığını + iki toprak torbası ·
    ⭐ sarkan modül paleti
G7  ⭐ BÜTÜN YÜZ YEŞİL, üstten sarkan saplar · kanal KURU · platform katlı, kapı yanında · avluda palet YOK, süpürülmüş ·
    ⭐ TEK işçi pompada, eli kumanda kutusunda · altın akşam
G8  aynı · ⭐ ŞELALE taş ağızdan çukura · köpük halkası + halkalar · seviye AYNI · işçinin eli inmiş
⛔ SAYIM: kule 1 · kuyu 1 · çukur 1 · ray 2 · bağ kirişi 2 · kabin 1 (dokuz karede) · vinç (1·0·0·0·0·0·0·0·0) ·
   sepetli platform (0·0·0·1·1·1·1·1·1) · pompa (0·0·0·0·1·1·1·1·1) · taş ağız (0·0·0·0·1·1·1·1·1) · şelale
   (0·0·0·0·0·0·0·0·1) · su (0·0·0·1·1·1·1·1·1, seviye sabit) · işçi (2·4·2·2·2·2·2·1·1)
⛔ Kolonlar, kirişler, raylar, eşik, fabrika duvarı, kapı ve baca dokuz karede DEĞİŞMEZ; su seviyesi G3'ten sonra DEĞİŞMEZ;
   kaya yüzü G5'ten sonra yalnız YEŞERİR (G6–G7) ve G8'de ıslanır.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK §4 · DERS 48 · beş soru ②③]

```
S0  kabin: vinç kancası → dört zincir → takozlar (düşey, ~2,3 m) · vinç: → sağ kenar → DIŞARI
S1  moloz: çukur → kürek → el arabası → RAMPA → fabrika kapısı · boru: kapı yanı → vana → eşik
S2  su: avlu vanası → sabit boru → çukur (yüzeyin altından) · rampa + arabalar: → kapı · platform + palet: kapı → avlu (sol)
S3  ızgara: palet → sepet → braket · boru: palet → sepet → sağ arka köşe → tepe · taş ağız: sepet → tepe · pompa: kapı →
    vana yanı · kaya paleti: kapı → avlu
S4  ⭐ kaya paneli: palet → sepet → ızgara (aşağıdan yukarı) · oluk: palet → sepet → kanal · tepsi paleti: kapı → avlu
S5  bitkili modül: palet → el → sepet → alt cep · boş tepsi: → yığın · sarkan modül paleti: kapı → avlu
S6  sarkan modül: palet → sepet → üst cep · platform: kule önü → kapı yanı (park) · palet + tepsi + torba: → kapı
S7  su: çukur → pompa → boru → taş ağız → kanal → çukur (devridaim) · taşınan malzeme yok
⛔ Vinç YALNIZ S0'da — G1'den sonra model vinç, kanca ya da tavandan sarkan yük çizerse ⑧ APPEARED [DERS 88].
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı bir önceki karede KAPI YANINDA ya da klibin içinde SEPETTE görünür [DERS 48 · 49].
⛔ Aynı anda tek hareketli makine: S0 vinç · S2 sonu–S6 sepetli platform [DERS 69].
⛔ Bitki kendiliğinden büyümez: her yeşil cep bir sepet hareketinden sonra dolar [DERS 76].
```

## 5. ⭐ IŞIK / GÖLGE KAPISI [ZAMAN_VE_ISIK §2 · DERS 40]

```
G0     ilk ışık sağda alçak (78°/+4,2°) · kabinin ve sağ kolonun sağ yüzü soluk altın · ön yüz ve kuyu SOĞUK GÖLGE
G1     sağdan sıyıran ışık (79°/+6,0°) · avluda SOLA uzun gölgeler
G2     sağdan, biraz önden (99°/+28,6°) · ön yüz ve çukur hâlâ gölgede
G3     güneş kuyuya girer: arka duvarın SOL kısmı aydınlık, sağ yan duvarın çapraz gölgesi (126°/+49,5°)
G4     bütün kuyu aydınlık · üst kirişin sert gölge bandı arka duvarın tepesinde (175°/+61,0°)
G5     sol yan duvarın gölgesi kaya yüzünün sol kısmında (228°/+52,4°)
G6     kaya yüzünün çoğu gölgede, sağında sıcak bant · avluda SAĞA uzun gölgeler (257°/+32,3°)
G7–G8  ⭐ ALTIN AKŞAM (278°/+9,8°) · kolonların ve kirişlerin sol kenarları parlar, kabin turuncu · kuyu yumuşak gölge ·
       G7 = G8 ışık birebir
⛔ Gölgeler soldan sağa TEK YÖNDE döner; geri dönen gölge = zaman ters → ❷
⛔ Güneş diski HİÇBİR karede yok [DERS 39 · 70] · eşit aydınlatılmış "render" kule → ❶ CGI
```

## 6. ⭐ BİR KULE · BİR KABİN · BİR ŞELALE KAPISI [DERS 55 · 84]

```
Korpus riski: "freight lift" → kuyuya yeni kabin, halat, makine dairesi · "waterfall" → kanyon, sis, ikinci akış ·
"factory yard" → ikinci kule, silo
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ)
② şelale TEK şerit, TEK taş ağız
③ araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç kabin / kaç akış / kaç ray / kaç figür
⛔ G1→ kuyuda kabin · ikinci kabin · ikinci akış · sis bulutu · kanyon · ikinci kule · üçüncü ray → ⑧
⛔ Model kayayı kulenin dışına taşırır ya da kolonları kayaya gömerse → ⑤ DEVAMLILIK (kolonlar kimlik nesnesidir)
```

## 7. ⭐ SU KAPISI — S2 ve S7 [SU_VE_YANSIMA §5–§6 · DERS 67 · 93]

```
S2 (rejim B · 2 sa → 8 sn)
· 0–0,5 vana · 0,5–5,5 su taş sıra taş sıra YÜKSELİR (görünür bant 60 px) · 5,5–6,5 eşiğin bir sıra altında DURUR
⛔ su tek saniyede belirir / çukurdan avluya taşar / borudan fışkırır → S2 atılır (çözüm ara kare G2′ — sahibe sorulur)
S7 (rejim G · 8 sn · 1×)
· "moves at natural speed" · "Eight seconds pass" · gök ve güneş DEĞİŞMEZ
· TEK figür, sırtı kameraya, yüz yok [P5-b] — iz YOK · figür YÜRÜMEZ
· zamanlama: 0–1 düğme · 1,0–2,5 taş ağızdan taşma · 2,5–4,0 kanaldan iniş + köpük halkası · 4–8 TUTUŞ (son kare = doruk)
· 56,0 kesmesi (B → G) dikiş: işçiler izden nete — ① / ③ hükmü BEKLENEN [P5-c]
⛔ G7 ≈ G8 durgunluk (su akmıyor) → S7 atılır [P5-d]
⛔ seviye değişir / avluya taşar / ikinci akış / sis kuyuyu örter → S7 atılır
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı yok · konuşma yok · avlu yankısı yatak
· 0,0 vinç dizeli + zincir · 4,5 kabin oturuşu · 6,5 vinç uzaklaşır · 8–15 kürek + el arabası · 16–22 vana + dolan su ·
  22,5 platform · 24–30 somun sıkma · 30,5 pompa deneme · 32–38 kaya oturuşu · 40–47 toprak + yaprak · 53,0 geri vites bip ·
  ⭐ 57,0 düğme TIK + pompa (KARE SENKRON ±2 kare) · 57,5 ilk şıpırtı · 60–64 ŞELALE SESİ sabit
· KART 64,0–69,0: şelale sesi sürer, kartın son saniyesinde söner → döngüde S0'ın kuşlarına bağlanır
```

## 9. Zaman ve ışık

```
G0 05:40 78°/+4,2° · G1 05:50 79°/+6,0° · G2 07:50 99°/+28,6° · G3 09:50 126°/+49,5° · G4 11:50 175°/+61,0° ·
G5 13:50 228°/+52,4° · G6 15:50 257°/+32,3° · G7 17:50 278°/+9,8° · G8 17:50 + 8 sn aynı
(41°K · δ +12,1° · güneş saati · TÜRETİLMİŞ model)
· kuyu sabah gölgede (açılış), öğlen aydınlık, akşam yumuşak gölgede; kolonların sol kenarı akşam altın
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 sahne), beyanlı
① / ③ DİKİŞ     8,0 (A → B): yumuşak izden yoğun ize · 56,0 (B → G): iz figürlerden duran figüre — beyanlı [P5-c]
① İSTASYON      S3 (çıplak duvar → ızgara) ve S4 (ızgara → kaya): model kuyuyu YENİDEN ÇİZEBİLİR — pilot (c′) ve günlük
⑤ DEVAMLILIK    renk değişimi (gri → koyu su → galvaniz → kaya → yeşil → beyaz su) KASITLI; kolonlar, kirişler, raylar,
                eşik, kapı, baca DEĞİŞMEZ
⑦ İŞ            S7'de inşaat yok (kasıtlı): ödül yapının kendi suyudur · G7/G8 ACTIVITY'si kasıtlı olarak zayıf
⑦ TEMPO         S6 sonu + S7 başı (el düğmede) 2x'te ~1 sn durgunluk — beyanlı bekleyiş
❺ TESLİM        THE BLUE SILO ile aynı ödül ailesi (paslı dikey kabuk + su) — fark: kabuk korunur, ödül akan su
①               su bandı 60 px — telefonda ince; kanıt şelalenin kendisidir, hazne ikincildir
⚠️ AİLE         KULE — THE BLUE SILO ile ARDIŞIK YAYINLANAMAZ
```
