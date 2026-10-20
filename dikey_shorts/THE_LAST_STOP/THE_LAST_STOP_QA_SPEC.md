# 🔍 THE LAST STOP — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_LAST_STOP_DIKEY_TIMELAPSE.md` · Günlük: `THE_LAST_STOP_URETIM_GUNLUGU.md` · Kapak: `THE_LAST_STOP_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      THE LAST STOP · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 19.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "THE LAST / STOP") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 ⭐ A (10 dk) — iki rejim
IŞIK      TEK GÜN, TAM KAPALI GÖK: 07:30 → 09:30 → 11:30 → 13:30 → 15:30 → 17:30 → 19:30 → 21:30 → 21:40 (güneş saati) ·
          57° kuzey · 21 Haziran (δ +23,4°) · güneş 95°/+31,7° → 328°/−4,3° · kamera 335°'ye bakar, tilt 54° aşağı, gök yok ·
          final MAVİ SAAT: cam oturur, iç ışık yanar
AİLE      ⭐ ZEMİN (aşağı bakan istasyon, gök ve ufuk YOK) · otobüs %31,3–59,5 · başlık alanı otobüsün ötesindeki koyu orman zemini
TAKVİM    yok — tek gün (dönüşüm sıkıştırıldı, beyanlı); zaman taşıyıcısı ışığın parlaklığı ve rengi (serin gri → beyaz → gri-altın →
          mavi) + finalde iç ışık
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① CAM TAVAN + İÇ IŞIK — tavanın ortasındaki açıklıkta TEK siyah çerçeveli cam, dört şeffaf bölme (x 342–687 · 345 px ·
    y %43,4–56,1); altında SICAK IŞIKTA krem örtülü çift kişilik yatak (iki yastık) ve krem kanepe camdan okunur; sıcak ışık
    yolcu pencerelerinden terasa ve çimene düşer; kadrajın EN PARLAK şeyleri cam ve pencerelerdir
  ② BORDO OTOBÜS — tek katlı otobüs, gövde koyu bordo; siyah pencere çerçeveleri, ön cam, iki görünür tekerlek; dört yolcu
    penceresi + önde tek katlanır kapı (x 716–809); otobüs x 213–888 (675 px) · y %31,3–59,5
  ③ TERAS — kapının önünde dört modülden TEK alçak ahşap teras (x 418–781), üstünde İKİ açık sandalye
  ④ TANIKLAR — solda takozlarda paslı eski tavan paneli (G0'da havadaydı) · solda katlanmış bomlu kamyon (bom dayanağında,
    kanca bloğu bağlı) · otobüsün ardında BOŞ ahşap kızak · tavanın ön/arka kapağı ve kenar çerçevesi (G0 ile AYNI) · mavi
    alacakaranlıkta koyu orman zemini · işçi yok, merdiven yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–58,0'da (2x: 28,0–29,0) cam açıklığın 1 m üstünden DÜZ iner ve oturur; sapanlar ANCAK oturduktan sonra gevşer. Cam
   açıklıkta "belirirse", kopyalanırsa ya da kancasız oturursa → S7 atılır [DERS 57 · 96].
⛔ 58,0'da (2x: 29,0) ışık TEK ADIMDA yanar ve yanık kalır. Titrer, söner ya da yeniden yanarsa [DERS 98] · far ya da dize lamba
   gibi başka bir kaynak yanarsa → S7 atılır.
⛔ Işık yanarken yatak, kanepe, sehpa, lambader, teras ya da sandalyeler KAYARSA / yeni nesne belirirse (dize lamba, ateş çukuru,
   sıcak küvet, ikinci lambader, ekran) → S7 atılır [DERS 91 ③].
⛔ Gök gündüze dönerse ya da camın yansıması iç ışığı boğarsa → sebep G8; KARE yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi +
   başlık, erime ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after" YOK. Kart G8 ile aynı dünya değilse → E kaydı
   [DERS 85]. klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta orman tonu (dijital sessizlik DEĞİL) [DERS 100].
⛔ Bir figürün yüzü okunursa ya da üçüncü figür belirirse S7 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 54°)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk / gök | kadraj DIŞI (%145) — hiçbir karede gök yok | gök bandı belirirse kamera kaydı |
| ⭐ otobüs (bütün gövde) | 213–888 px · %31,3–59,5 · 675 px | KESİR ±7 px · DOKUZ KAREDE |
| ⭐ tavan açıklığı | 342–687 px · %43,4–56,1 · 345 px | ±0,5 puan · DOKUZ KAREDE (G0–G6 boş · G7 üstünde cam · G8 cam) |
| ⭐ ön cam + kapı | ön cam 809–881 · kapı 716–809 px · %32,4–45,6 | ±0,5 puan · DOKUZ KAREDE (nirengi ①) |
| ⭐ tavanın ön/arka kapağı | açıklığın iki ucu, x 342 / 687 | DOKUZ KAREDE AYNI — kesilmez, şeffaflaşmaz (nirengi ②) |
| ⭐ arka tekerlek + 1. pencere | 318–376 · 256–362 px · %42,0–50,1 | ±0,5 puan · DOKUZ KAREDE (nirengi ③) |
| dört yolcu penceresi | 256–705 px · %36,8–50,1 | sayı DÖRT · çerçeveler SİYAH (boyanmaz) |
| ⭐ kamyon (kasa arkası + bom kaidesi) | 11–284 px · %49,0–62,0 | gövde ±20 px [DERS 96 ①] · TEK kamyon · G0 · G7 bom açık, diğerleri katlı |
| ⭐ G0 asılı panel | ≈ 17–305 px · ≈ %28–47 | YALNIZ G0 · takozların TAM üstünde, sapanlar gergin |
| ⭐ panel takozlarda | 17–304 px · %26,3–45,3 | G1→ · ±20 px |
| ⭐ cam kızakta | 678–968 px · %46,5–57,5 (kısmen otobüsün ardında) | G0–G6 · G7–G8 kızak BOŞ |
| ⭐ G7 asılı cam | 329–696 px · %46,0–59,3 · 367 px | YALNIZ G7 · açıklığın TAM üstünde, ölçüsü açıklıkla aynı [DERS 88] |
| ⭐ yatak üstü | 361–513 px · %44,1–52,1 | G5→ · TEK · karşı yarısı tavandan okunur |
| ⭐ kanepe | 558–677 px · %43,5–49,9 | G6→ · TEK parça · sırtı karşı yanda |
| sehpa / lambader | 571–620 / ≈ 681 px | G6→ · TEK · lambader G6–G7 sönük, G8 yanık |
| ⭐ teras | 418–781 px · %20,2–38,6 | G7→ · TEK (dört modül) · iki sandalye |
| işçi (zeminde) | ≈ 82 px boy | İKİ · yüz yok |
| üst band | %87–100 | yalnız gölgeli orman zemini ve ladin gövdeleri |

## 3. ⭐ OTOBÜSÜN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ otobüs soluk açık gri-yeşil, kahverengi pas şeritleri · kapaklarda yosun · yakın yanda tekerlek göbeğine kadar uzun ot ·
    ⭐ tavanın ortası AÇIK, içeride DÖRT eski koltuk grubu (ikişer mavi-gri koltuk) · ⭐ paslı panel takozların TAM üstünde dört
    gergin sapanda asılı, bom açık · cam tavan kızakta · iki işçi (biri kumandalı, biri halatlı)
G1  ⭐ panel takozlarda, gevşek sapanlar üstünde · ⭐ bom katlı, kanca bloğu bağlı · ⭐ ot kısa biçilmiş, tekerlekler açık ·
    koltuklar AYNI (dört) · ⭐ el arabası + boş çuval yığını kapının yanında
G2  ⭐ koltuk YOK — eski gri zemin kaplaması boş, tozlu · ⭐ yakın yanın arka ucu (1. pencerenin sonuna kadar) mat çıplak GRİ metal ·
    gövdenin geri kalanı soluk + pas · zımpara + katlı merdiven arka köşede
G3  ⭐ bütün gövde KOYU BORDO (siyah çerçeveler, ön cam, lastikler aynı) · iç boş · ⭐ naylonlu meşe demetleri kapının yanında
G4  ⭐ AÇIK MEŞE zemin, her tahta otobüsün ENİNE · iç boş · ⭐ iki naylonlu kaide modülü kapının yanında
G5  ⭐ açıklığın arka ucunda TEK çift kişilik yatak, krem örtü, iki yastık · kaide şeridi SÖNÜK · ⭐ iki naylonlu kanepe yarısı kapıda
G6  ⭐ karşı yanda TEK krem kanepe (sırtı karşı yanda) · ⭐ ceviz sehpa · ⭐ ince lambader (SÖNÜK) · ⭐ dört teras modülü + iki katlı
    sandalye kapının sağında istif
G7  ⭐ kapının önünde TEK teras (dört modül), iki açık sandalye · ⭐ cam tavan açıklığın 1 m TAM üstünde asılı, bom açık · ⭐ kızak
    BOŞ · mavi alacakaranlık, iç KARANLIK · merdiven yakın yanda · iki işçi (biri kapıda halatla, biri kamyonda kumandayla)
G8  ⭐ cam açıklıkta · ⭐ kaide şeridi + lambader SICAK YANIK, yatak ve kanepe camdan okunur · ⭐ bom katlı · işçi, merdiven YOK
⛔ SAYIM: otobüs 1 · kapı 1 · yakın yan penceresi 4 · görünür tekerlek 2 · kamyon 1 · bom 1 · koltuk grubu (4·4·0·…) ·
   panel askıda/takozda (askı·takoz·…) · cam (kızak ×7 · askı · açıklık) · yatak (0·0·0·0·0·1·1·1·1) ·
   kanepe (0·0·0·0·0·0·1·1·1) · sehpa (0·…·1·1·1) · lambader (0·…·1·1·1) · teras (0·0·0·0·0·0·0·1·1) · sandalye (0·…·2·2) ·
   işçi (2·2·2·2·2·2·2·2·0) — kadro HİÇBİR klipte ikiyi aşmaz [DERS 89]
⛔ Otobüsün biçimi, pencere ve kapı sayısı, tekerlekler, ön cam ve tavan kapakları dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  panel: askı (takozların tam üstü) → bom son metre indirir → takozlar · sapan: gergin → gevşek (ANCAK oturunca) → çözülür ·
    bom: açık → kamyonun üstüne döner → dayanağı · ot: biçme makinesi → kucak → sağ kenardaki yol · el arabası + çuvallar: yol → kapı
S1  koltuk grubu (×4, TEK TEK): iç → iki el → kapı → çimen → sağ kenardaki yol · çöp: süpürge → çuval → el arabası → yol · pas:
    zımpara → çıplak gri metal (arka köşeden öne)
S2  pas: zımpara → gri metal (pencere pencere öne, ön cam çevresi, kenar çerçevesi merdivenden) · astar / bordo: kutu → rulo →
    gövde (dikey şerit şerit, arkadan öne) · boya takımı: → yol · meşe demetleri: yol → kapı yanı istif
S3  tahta: demet → el → eski kaplamanın üstü (ENİNE, sıralar arkadan kapıya) · eşik çıtası → kapı · ambalaj: → yol · kaide
    modülleri: yol → kapı yanı
S4  ⭐ modül ①: kapı yanı → kapı → açıklığın arka ucu (DOĞRUDAN yerine) · modül ②: aynı yol, ① yerindeyken → yanına — TEK kaide ·
    şilte: yol (rulo) → kapı → kaide (açılır) · örtü, yastıklar → yatak · kanepe yarıları: yol → kapı yanı
S5  ⭐ yarı ①: kapı yanı → kapı (SIRT ÖNDE) → karşı yan (DOĞRUDAN yerine, sırtı karşı yanda) · yarı ②: aynı yol → yanına — TEK
    kanepe · sehpa, lambader: yol → kapı → yer · teras modülleri + sandalyeler: yol → kapının sağı istif
S6  modül (×4, TEK TEK): istif → iki el → kapının önü (2 × 2, kenar kenara) · sandalye: istif → açılır → teras · cam: kızak →
    dört sapan → bom → otobüsün üstü → açıklığın TAM üstünde asılı
S7  cam: askı → bom son metre indirir → açıklığın kenar çerçevesi · sapan: gergin → gevşek (ANCAK oturunca) → merdivenden
    çözülür · ışık: kapıdaki düğme → kaide şeridi + lambader → cam + pencereler · bom: açık → dayanağı · merdiven: → yol
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı sağ kenardaki yol, kapının yanındaki istif ya da kızak [DERS 48 · 49].
⛔ Kanca hiçbir karede BOŞ sallanmaz: G0 · G7 yüklü, diğerleri bom katlı ve kanca bloğu bağlı [DERS 8 · 46]. İkinci kaldırıcı,
   iskele, boya tabancası YOK [DERS 67 · 69].
⛔ Mobilya kendiliğinden kaymaz; her parça kapıdan girer ve TEK TEK, DOĞRUDAN yerine oturur — ortada birleşip dönme yok
   [DERS 61 · 89 · 103].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI]

```
G0     07:30 (95°/+31,7°) · ⭐ serin gri sabah, kapalı gök · gölgesiz, eşit · orman koyu
G1     09:30 (125°/+46,9°) · parlak gri
G2     11:30 (168°/+56,0°) · ⭐ en parlak, en düz beyaz kapalı gök (öğle)
G3     13:30 (215°/+52,7°) · parlak, nötr
G4     15:30 (251°/+39,6°) · hafif sıcak, yumuşar
G5     17:30 (277°/+23,5°) · ılık gri, loşlaşmaya başlar
G6     19:30 (301°/+8,2°) · ⭐ gri-altın akşam · orman kararır · bordo derinleşir
G7     21:30 (326°/−3,6°) · ⭐ mavi alacakaranlık · iç KARANLIK
G8     21:40 (328°/−4,3°) · aynı mavi · ⭐ iç SICAK IŞIKTA — cam ve pencereler parlar
⛔ G3 → G7 ışık TEK YÖNDE kararır (S5–S7); geri aydınlanan kare = zaman ters → ❷ [DERS 98 · 104]
⛔ G0–G7 boyunca HİÇBİR yapay ışık yanmaz — kaide şeridi ve lambader G8'e kadar sönük; far HİÇBİR karede yanmaz
⛔ Güneş HİÇBİR karede yok (gök kapalı, kadraj gök göstermez) · sert gölge belirirse → bulut yırtıldı, kare yeniden
```

## 6. ⭐ BİR OTOBÜS · BİR KAPI · İKİ İŞÇİ KAPISI [DERS 55 · 89]

```
Korpus riski: "bus conversion" → ikinci otobüs, karavan, sarı okul otobüsü, tavan çadırı · "forest retreat" → dize lamba, ateş
çukuru, sıcak küvet, kulübe · "renovation" → iskele, kalabalık ekip · "boom truck" → sepetli platform (ÇIKARIM — bu filmde ölçülmedi)
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ) · "Only two workers" her I2V'de · G8'de "No people are present."
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç kanepe yarısı / kaç pencere / kaç kaldırıcı
⛔ ikinci otobüs · ikinci kapı · beşinci pencere · üçüncü işçi · ikinci kaldırıcı · üçüncü kanepe yarısı · ikinci teras ·
   üçüncü sandalye · ikinci lambader · dize lamba · ateş çukuru · sıcak küvet → ⑧
⛔ Model kapıyı, pencereleri ya da tavan kapaklarını yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Gövdede, panelde, kamyonda okunur yazı (plaka, hat tabelası) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 ot biçilir, el arabası · S1 çuvallar, gri yama · S2 bordo şeritler, meşe demetleri · S3 son sıralar, eşik, kaide modülleri ·
  S4 şilte, örtü, kanepe yarıları · S5 ikinci yarı, sehpa, lambader, teras istifi · S6 sandalyeler, cam havaya · S7 tutuş (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · ladin ormanında rüzgâr + kuşlar yatak
· 0,0 bom hidroliği · panelin takoza oturuşu · biçme makinesi · 8–15 koltukların kapıya değmesi, çuvallar · 15,0 zımpara · 16–23
  zımpara → rulo · 24–31 parke klik + tokmak · 32–39 naylon, modüller, şilte · 40–47 kanepe yarıları, istif · 48–55 teras
  modülleri, sandalye klikleri · 54,0 bom hidroliği · ⭐ 57,0–58,0 camın contaya oturuşu (KARE SENKRON ±2 kare) · 58,0 düğme ·
  58–60 bom, adımlar · 60,0–64,0 alacakaranlık ormanı
· KART 64,0–69,0: orman tonu sürer, kartın son saniyesinde söner → döngüde S0'ın bom uğultusuna bağlanır
```

## 9. Zaman ve ışık

```
G0 07:30 95°/+31,7° · G1 09:30 125°/+46,9° · G2 11:30 168°/+56,0° · G3 13:30 215°/+52,7° · G4 15:30 251°/+39,6° ·
G5 17:30 277°/+23,5° · G6 19:30 301°/+8,2° · G7 21:30 326°/−3,6° · G8 21:40 328°/−4,3°
(57°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · gök tam kapalı)
· gölge yok (kapalı gök); zaman ışığın parlaklığı ve rengiyle taşınır; final mavi saatte, iç ışıkla
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 sahne), beyanlı
① / ③ DİKİŞ     56,0 (B → A): uzun izli figürlerden kısa izli, tanınır figürlere; ışık mavi saatte sabitlenir — beyanlı [P5-c]
① ZAMAN         kapalı gök: gölge süpürmesi yok, zaman parlaklık ve renkle taşınır; beyanlı (DERS 47 tetiklenmez)
① KADRAJ        tilt 54° — keystone, ladin gövdeleri üst kenara doğru açılır; gök yok (ZEMİN ailesi); beyanlı
⑤ DEVAMLILIK    renk değişimi (soluk gri-yeşil → gri metal → bordo) ve iç değişim KASITLI; otobüs biçimi, pencereler, kapı,
                tekerlekler, ön cam, tavan kapakları, kamyon gövdesi DEĞİŞMEZ · bom G0 · G7'de açık, diğerlerinde katlı KASITLI
⑦ İŞ            S7'nin 4–8'inde iş yok (kasıtlı tutuş) · G8 boş otobüs (kasıtlı: işçisiz final, kapak kaynağı)
⑦ TEMPO         S6 sonu + S7 başı (askıda cam) 2x'te ~0,5 sn durgunluk — beyanlı bekleyiş
❺ TESLİM        işlev anı ışık — TOTAL RESET · POOL ROOM ile aynı mekanizma (sahip bilerek seçti 19.10.2026); fark: dış mekân, araç,
                ışık camdan dışarı taşar
```
