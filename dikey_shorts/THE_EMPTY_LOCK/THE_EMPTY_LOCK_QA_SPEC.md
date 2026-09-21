# 🔍 THE EMPTY LOCK — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦ ⑨ ⑪ ⑫).
> Plan: `THE_EMPTY_LOCK_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md` (üretimde açılır)

```
FİLM      THE EMPTY LOCK · 7 × 8,0 = 56,0 sn · KAPAK KARTI YOK · LOGO YOK
SCENE BLOCK / END CARD    56,0 sn / yok
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok
REJİM     S0–S4 B (2 sa) · S5–S6 ⭐ A (10 dk) — iki rejim, üçüncü yok · rejim G YOK (doluş 1×'te okunmaz)
SAHNE SAATLERİ  07:20 → 09:20 → 11:20 → 13:20 → 15:20 → 17:20 → 17:30 → 17:40 (tek gün)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① HAZNE DOLU — su merdivenin 4.–5. basamağında (y ≈ %61–62 @ x %55), yüzey düz, bisiklet YOK
  ② TEKNE YÜKSELMİŞ — beyaz gövde + koyu yeşil tente haznede (d 23–30), tente üstü coping çizgisinin
    (%57 @ d 26,5) ÜSTÜNDE ya da hizasında, gövde tek parça
  ③ YENİ KAPI KURU — sarı meşenin GÜNEY yüzü mitreden alt suya kadar kuru; alt su durgun; kanat
    yüzünde ıslak leke / fışkırma YOK

⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 54,0'ta su HÂLÂ YÜKSELİYOR olmalı: 54,0 ve 55,0 karelerinde merdivendeki su çizgisi farklı y'de
   (≈ 0,4 basamak ≈ 9 px). Duran su + duran tekne = S6 atılır (rejim A'da 10 dk'nın 6.–7. dakikası).
⛔ 56,0'da film su DURULURKEN kesilir; sonrasında kart, logo, fade YOK.
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt formülü KAMERA_DILI §3)

| ne | beklenen | tolerans |
|---|---|---|
| alt kapı BATI topuk (x) | %33 | ±1 puan · SEKİZ KAREDE DE |
| alt kapı DOĞU topuk (x) | %52 | ±1 puan · SEKİZ KAREDE DE |
| kapı üstü (y) / eşik (y) | %51 / %42 | ±1 puan · SEKİZ KAREDE DE (kanat varken üst, yokken eşik) |
| hazne ağzı (px) | 185 px | ±15 px |
| ⭐ kulübe yakın köşe (x · y) | %42 · %76 | ±0,5 puan · SEKİZ KAREDE DE (I2V çapası) |
| ⭐ rıhtım geçidi (x · y) | %72 · %72 | ±0,5 puan · SEKİZ KAREDE DE |
| ⭐ doğu babası d 26 (x · y) | %55 · %58 | ±0,5 puan |
| ⭐ merdiven (x) · basamak 0 / 6 (y) | %55 · %56 / %64 | ±0,5 puan · basamak sayısı 7, HİÇ gömülmez (6 coping'de) |
| üst kapı üstü (y) | %75 | ±1 puan · sekiz karede KAPALI |
| gök | YOK | üst kenar kavakları keser; gök görünüyorsa istasyon KAYMIŞTIR |
| kapama tahtası üstü (G1–G4 · y) | %35 · yuva d 15 (x %27–49) | ±1 puan · coping'in ALTINDA (eşik görünür kalır) |
| su yüzeyi G0 (basamak 3) | merdivende y ≈ %60 | ±1 puan |
| su yüzeyi G5–G6 (basamak 1) | y ≈ %57 | ±1 puan |
| su yüzeyi G7 (basamak 5) | y ≈ %62 | ±1 puan |
| eski kanat 1 / 2 (yol · G2→ / G3→) | x %26–35 · y %57–62 / %63–67 | ±2 puan · G7'ye kadar YERİNDE |
| tekne G5 pruva (y) | %41 · alt suda | ±2 puan |
| tekne G6 / G7 tente üstü (y) | %55 / %61 | ±2 puan · fark ≥ 4 puan (yükseliş kanıtı) |

## 3. ⭐ KİLİDİN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  kara çift · batı kanat bilezikten düşük (üstü doğudan 0,5 m aşağıda) · mitre YARIK · fışkırma alt
    suya · hazne basamak 3 · üst eşikte plume · vinç: ilk tahta sapanda · lowbed'de 2 sarı kanat ·
    pompalar coping'de · tekne 0
G1  tahtalar yuvada (5, üstü −2,75) · hazne + apron KURU · silt taban + birikinti + bisiklet · kara
    çift hâlâ hatta, mitre kuru · pompalar tabanda, hortum coping'de · sapan üst tahtada · plume YOK
G2  batı kara kanat YOLDA (sapan bağlı) · doğu kanat tek başına dik · batı eşik açık, çanak siltli ·
    tahtalar yuvada · pompalar çalışıyor · kova avluda
G3  hat BOŞ (kanat 0) · eşik + iki çanak temiz ıslak taş · taban ilk 6 m taş · yolda 2 kara kanat ·
    kova siltle yığın üstünde sapanda · hafriyat yığını avluda · lowbed'de 2 sarı kanat
G4  batı hattında SARI kanat dik + bilezik + denge kirişi (sapan bağlı) · doğu yarı açık · coping'de
    hortum YOK · tabanda ince su · lowbed'de 1 sarı kanat · yığın · kova
G5  SARI çift KAPALI (mitre) · savak açık · tahtalar avluda istif (5) · yuva boş · alt su kapının dibinde ·
    hazne basamak 1, bisiklet gidonu çıkık · avluda MAKİNE 0, iz var · tekne alt suda, pruva kapıya 1 m
G6  SARI çift KAPALI · savak kapalı · tekne HAZNEDE (d 23–30), basamak 1, tente kapı üstü hizasında ·
    alt suda tekne 0 · tek görevli doğu coping'de sırtı dönük · üst kapı kapalı
G7  hazne basamak 5 · tekne coping hizasında · kapı güney yüzü KURU · alt su durgun · plume durmuş ·
    bisiklet GÖMÜLÜ · yolda 2 kara kanat · avlu: tahta istifi + yığın + kova + iz

⛔ GERİ GİDİŞ YOK: çıkan kanat geri gelmez (G2→); oturan kanat kıpırdamaz (G4→); tahta G5'ten sonra
   yuvaya dönmez; su G6→G7 yalnız YÜKSELİR.
⛔ IŞINLANMA YOK: pompa + hortum yalnız S3'ün İÇİNDE çıkar; tahtalar + lowbed + vinç yalnız S4'ün
   İÇİNDE çıkar; tekne yalnız S4'ün İÇİNDE (kadrajın altından) gelir.
⛔ KANAT HAVADA BELİRMEZ (F08): G3'te lowbed'de → S3'te sapanda iner → G4'te çanakta dik.
   Sapansız süzülen kanat = KLİP ATILIR. G3'te hatta HAYALET KANAT = KARE ATILIR.
```

## 4. ⭐ YÜK YOLU KAPISI — S1 · S3 · S4 [FIZIK_VE_AGIRLIK §4 · DERS 57 · beş soru ②③]

```
S1  ① kanat SAPANLA kalkar — iki sapan başta, kablo düşey, kanca yüklü; iki güdüm halatı
    ② kaldırış boyunca kanat BOYUNU KORUR (5 m ≈ 177 px @ d 20) ve DİK kalır; döner/kısalır → klip atılır
    ③ yola YATAR — G2'de yolda, sapan hâlâ bağlı (boş kanca YOK — DERS 8)
S3  ① sarı kanat lowbed'den kalkar — kaynak ve hedef aynı kadrajda (avlu → hat)
    ② çanağa DÜŞEY iner; kanat havada TEK (hedefte ikinci kanat belirirse = DERS 57 kopyalama → klip atılır)
    ③ G4'te dik, bilezik coping'de, denge kirişi coping'de, sapan bağlı
S4  ① ikinci kanat aynı yol · ② mitre KAPANIR (iki kanat V) · ③ tahtalar çıktıktan SONRA su gelir —
    sıra: kanat → tahta → su → tekne; su tahtadan ÖNCE gelirse mantık kopmuştur, klip atılır
⛔ Kanat sapansız yükselirse ya da hedefte kopyalanırsa: ARAÇ sorgulanır (pilot üçlü c), prompt değil.
```

## 5. ⭐ SU CETVELİ VE KAPI KAPISI — S0 · S5 · S6 [tasarım kararı ③ · P6-c]

```
① CETVEL        merdiven basamakları her karede sayılır; su seviyesi basamak numarasıyla okunur:
                G0 3 · G1–G3 0 · G4 0 (+ince tabaka) · G5–G6 1 · G7 5. Basamak gömülmez (6 coping'de)
② BOŞALMA (S0)  su ÖNCE kendi iner (3→1, mitre sızıntısı), SONRA pompayla (1→0); tahta üstü coping
                ALTINDA kalır — eşik G1'de görünür. Tahta coping'e çıkarsa eşik kaybolur → kare atılır
③ DOLUŞ (S6)    su basamak basamak yükselir (5 basamak / 6 sn); tek hamlede dolan hazne = F05 → klip atılır
④ KURU YÜZ      S6 boyunca yeni kapının güney yüzünde ıslak leke, sızıntı, fışkırma YOK; alt su durgun.
                Bir kare bile fışkırma = VAAT DÜŞTÜ → S6 yeniden
⑤ ISLAK BANT    duvarlardaki koyu ıslak bant S0'da suyla iner, S6'da suyla çıkar — seviyenin ikinci izi
```

## 6. ⭐ TEK KİLİT · TEK TEKNE KAPISI [DERS 55]

```
SAYIM   hazne 1 · kapı hattı 2 (üst KAPALI sekiz karede) · alt kapı kanadı hatta: G0–G1 2 · G2 1 · G3 0 ·
        G4 1 · G5–G7 2 · yolda kara kanat: G2 1 · G3–G7 2 · lowbed'de sarı kanat: G0–G3 2 · G4 1 ·
        tekne: G0–G4 0 · G5 1 (alt su) · G6–G7 1 (hazne) · kulübe 1 · merdiven 1 · baba 1
⛔ İkinci hazne, merdiven kilit (staircase), ikinci kanal kolu, üst kapı AÇIK = KARE ATILIR.
⛔ G3'te hatta hayalet kanat = KARE ATILIR. G5–G7'de iki tekne = KARE ATILIR.
⛔ Aynı tekne: beyaz gövde · koyu yeşil tente · 7 m — farklı renk/boy = ⑤ DEVAMLILIK düşer.
⛔ Araç kapısının ⑨ SAYIM TESTİ'yle ÖNCEDEN ölçülür; kapıda çıkarsa ARAÇ DEĞİŞİR.
```

## 7. ⭐ REJİM A KAPISI — S5 · S6 [SANTIYE_HAREKETI §1]

```
① GÖLGE         G5 → G6 → G7 güneş 17° → 15° → 13°: gölge yönü aynı (sağa), boy ~%15 uzar; sıçrama YOK
② FİGÜR         bulanık ama okunur; yüz YOK; sırtı dönük tek görevli doğu coping'de (G5–G7)
③ HIZ (S5)      kapı açılışı 0–2 sn · tekne girişi 2–6 sn (~12 m) · kapanış 6–8 sn (günlük §4'e ölçülür)
④ HIZ (S6)      basamak 1→5 arası 1–7 sn (≈1,5 sn/basamak) · tente coping çizgisini ≈ 5. sn'de geçer
⑤ RİJİT GÖVDE   tekne 0 · 4 · 8 sn'de aynı boy; suyla YÜKSELİR, büyümez
⑥ KADRAJ BOŞ    G5–G7'de vinç · lowbed · pompa · hortum YOK; varsa S4 çıkışı gerçekleşmemiştir
⛔ Bunlardan biri düşerse ilgili sahne yeniden üretilir; ölçüm günlük §4'e, sonra DERSLER'e (kart D).
```

## 8. Zaman ve ışık

```
IŞIK GÜNÜ   07:20 → 17:40 = 10 sa 20 dk · 5×B + 2×A ≤ 14 sa
GÜNEŞ       kadrajda HİÇ görünmez — gök yok, bakış kuzey · disk anılmaz [DERS 39]
GÖLGE       07:20 batı duvar üstü aydınlık, taban gölge, sola · 09:20 batı duvar tabana yakın aydınlık ·
            11:20 taban aydınlık, doğu dibinde şerit · 13:20 taban aydınlık, batı dibinde şerit ·
            15:20 doğu duvar aydınlık, sağa · 17:20–17:40 doğu duvarın üst bandı turuncu, sağa uzun
DEĞİRMEN    gölgesi sabah alt suda (alt bant), hazne ve kapı gün boyu GÜNEŞTE
KULÜBE      gölgesi G5–G7'de üst kapı ÜSTÜNDEN üst havuza — hazneye girmez
G6 → G7     ışık 10 dk ilerler (15° → 13°) — LIGHTING iki karede AYRI; birebir aynı DEĞİL
MEVSİM      eylül ortası · tek gün · kavaklar tam yapraklı
⛔ KIŞ YOK — tek günlük film [DERS 7 · 26] · ⚠️ BULUT TAŞIYICI YOK (gök yok) — ③ ZAMAN'ın açık sorusu
```

## 9. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM        süreler eşit (7 × 8,0) — proje sahibinin kesin kuralı, beyanlı
① / ③ DİKİŞ       40,0 (B → A: iz → okunur figür) — beyanlı; müziksiz 38,0–40,0 penceresi taşır
⑦ S6 "İŞSİZ"      S6'da makine yoktur, SU vardır — ödül yapının çalışmasıdır [SANTIYE_HAREKETI §4.7]
③ GÖK YOK         bulut taşıyıcısı yok — zaman gölge + su cetveliyle; SWALLOWED BUS P6-d aynı soru
① KEYSTONE        −38° tilt'te kulübe ve kavakların düşey çizgileri yakınsar — sekiz karede AYNI
                  olduğu sürece istasyon kayması DEĞİLDİR
⚠️ İKİNCİ HAZNE    beklenen DEĞİL — çıkarsa §6 gereği araç değişir
⚠️ SIVI DOLUŞ      beklenen DEĞİL — tek hamlede dolan hazne §5 gereği klip atılır
⚠️ SAPANSIZ KANAT  beklenen DEĞİL — çıkarsa §4 gereği araç sorgulanır
⚠️ KOPYA KANAT     beklenen DEĞİL (DERS 57) — pilot üçlü (c) S3'te önce sınanır; çıkarsa kapsam daralır
```
