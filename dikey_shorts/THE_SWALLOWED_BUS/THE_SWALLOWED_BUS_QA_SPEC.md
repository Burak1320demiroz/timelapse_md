# 🔍 THE SWALLOWED BUS — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦ ⑨ ⑪ ⑫).
> Plan: `THE_SWALLOWED_BUS_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md`

```
FİLM      THE SWALLOWED BUS · 7 × 8,0 = 56,0 sn · KAPAK KARTI YOK · LOGO YOK
SCENE BLOCK / END CARD    56,0 sn / yok
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok
REJİM     S0 A (10 dk) · S1–S5 B (2 sa) · S6 ⭐ G gerçek zaman 1× — depoda ikinci koşu, ölçülmedi
SAHNE SAATLERİ  07:20 → 07:30 → 09:30 → 11:30 → 13:30 → 15:30 → 17:30 → +8 sn (tek gün)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① YAMA BÜTÜN — siyah asfalt dikdörtgeni, dikişleri sağlam, beyaz çizgi düz; ÜSTÜNDE HİÇBİR
    ŞEY YOK (otobüs geçmiş)
  ② OTOBÜS SOL KENARDA — arkası kadrajda, ARKA TEKER batı dikişinin (x %22) solunda, yolda
  ③ tek figür çınarın dibinde, sırtı dönük; bariyer yerde

⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 54,0'ta otobüs HAREKET HÂLİNDE olmalı: 54,0 ve 55,0 karelerinde arka teker farklı x'te
   (≈ 3,5 m = ~170 px). Duran otobüs = S6 atılır.
⛔ 56,0'da film otobüs ÇIKARKEN kesilir; sonrasında kart, logo, fade YOK.
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR)

| ne | beklenen | tolerans |
|---|---|---|
| çukur / yama yakın kenarı (y) | %36,2 | ±1 puan · SEKİZ KAREDE DE |
| çukur / yama uzak kenarı (y) | %49,2 | ±1 puan · SEKİZ KAREDE DE |
| çukur / yama sol ucu (x) | %22,1 | ±1 puan · SEKİZ KAREDE DE |
| çukur / yama sağ ucu (x) | %59,3 | ±1 puan · SEKİZ KAREDE DE |
| çukur açıklığı (px) | 402 px | ±25 px |
| ⭐ kemerli giriş (x) | %60,4 | ±0,5 puan · SEKİZ KAREDE DE (I2V çapası) |
| ⭐ trafik lambası direği (x) | %73,7 | ±0,5 puan · SEKİZ KAREDE DE |
| ⭐ çınar gövdesi (x) | %24,5 | ±0,5 puan |
| uzak kaldırım (y) | %55,8 | ±0,5 puan |
| cephe dibi (y) | %61,1 | ±0,5 puan |
| yağmur ızgarası (x) | %18,4 | ±1 puan |
| gök | YOK | üst kenar cepheyi keser; gök görünüyorsa istasyon KAYMIŞTIR |
| boru (G3) | uzak yarıda, %38–42 bandı · 337 × 65 px | ±20 px |
| çelik bant (G4) | %47,7–49,9 · ~42 px | ±10 px |
| G0 otobüs arka teker (x) | %71,2 · YOLDA | ±2 puan |
| G7 otobüs arka teker (x) | ≤ %22 (batı dikişinin solunda) | — |

## 3. ⭐ ÇUKURUN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  otobüs ÇUKURDA (burnu −3,5 m'de, arka teker yolda) · kapılar 3 açık · sapanlar gergin,
    kanca yüklü · lowbed uzak şeritte boş · çukur kenarı YIRTIK · çelik 0 · boru 0
G1  otobüs LOWBED'DE (sapan hâlâ bağlı) · çukur BOŞ · dipte moloz + su · iki kırık boru ucu
    (sol + sağ duvar) · pompa dipte, hortum uzak kenardan ızgaraya · ⛔ çukurda hayalet otobüs YOK
G2  çelik dört duvar, üstü +0,3 · kenar testere kesim · taban çakıl · hortum çalışıyor · boru
    uçları BİLEZİKLİ · ilk boru sapanda tırın üstünde · ikinci boru tırda · ekskavatör uzak şerit
G3  boru SÜREKLİ (sol duvar → sağ duvar, iki bilezik) · hortum YOK, pompa YOK · silindir vinç
    zincirinde · tır boş · damper 1 yakın kenarda, kasa inik
G4  dolgu ¾ (−0,7) · boru GÖMÜLÜ · ÇELİK BANT ~1 m dört kenarda · silindir dolguda uzak duvar
    dibinde · damper 2 kasa kalkık · vinç YOK (mat + palet izi) · ekskavatör uzak şerit
G5  çelik YOK · perdeler tırda istif, sonuncusu kıskaçta · taban düz gri (−0,15) · tandem
    silindir yamanın sağ ucunda · koni-bariyer hâlâ yakın şeritte
G6  SİYAH YAMA yol seviyesinde · dikişler açık renk · BİR beyaz şerit · makine 0 · koni 0
    (uzak kaldırımda istif) · otobüs ÖNÜ sağ kenarda (üçte biri kadrajda) · figür 1, sırtı dönük
G7  otobüs ARKASI sol kenarda, arka teker dikişin 2 m ötesinde · yama BÜTÜN, üstünde soluk
    teker izi · figür 1 · bariyer yerde

⛔ GERİ GİDİŞ YOK: çakılan perde sonraki karede eksilmez (G2→G4); çekilen perde geri gelmez (G5→).
⛔ IŞINLANMA YOK: lowbed yalnız S1'in İÇİNDE çıkar; vinç yalnız S3'ün İÇİNDE çıkar; tır +
   ekskavatör + finişer + silindir + koni + mat yalnız S5'in İÇİNDE çıkar.
⛔ BORU HAVADA BELİRMEZ (F08): G2 sapanda → S2 iner → G3 bileziklerde. Sapansız süzülen boru = KLİP ATILIR.
```

## 4. ⭐ YÜK YOLU KAPISI — S0 ve S2 [FIZIK_VE_AGIRLIK §4 · beş soru ②③]

```
S0  ① otobüs SAPANLA kalkar — sapan iki, gövdenin altında, kablo düşey, kanca yüklü
    ② kaldırış sırasında otobüs BOYUNU KORUR (12 m ≈ 600 px @ d 17,5); kısalır/uzarsa klip atılır
    ③ lowbed'e OTURUR — G1'de tekerler kasada, sapan hâlâ bağlı (boş kanca YOK — DERS 8)
S2  ① boru tırdan/sapandan iner — kaynak ve hedef aynı kadrajda
    ② iki boru uç uca, dış uçlar ESKİ HATTIN BİLEZİĞİNE — bilezik G2'de var, G3'te dolu
    ③ hortum ancak boru bağlandıktan sonra gider (sıra: bağlantı → pompa çıkar)
⛔ Otobüs sapansız yükselirse, boru sapansız inerse: ARAÇ sorgulanır, prompt değil.
```

## 5. ⭐ KATMAN VE CETVEL KAPISI — S3 · S4 [dış değerlendirme ③]

```
① ÜÇ KATMAN     S3 klibinde dolgu üç basamakta yükselir (boru sırtı → yarı → −0,7); tek
                hamlede dolan çukur = F05 sıvı büyüme → klip atılır
② CETVEL        G4'te çelik bant GÖRÜNÜR (~1 m, 42 px) — dolgu çeliğin üstüne çıkmaz
③ BAĞLI SÖKÜM   S4 klibinde perde çekildikçe ARKASINA katman dökülür; perdeler bir anda
                kaybolup dolgu bir anda tamamlanırsa klip atılır
④ SIKIŞTIRMA    silindir her katmanın üstünde en az bir geçiş yapar (iz: tread pattern)
```

## 6. ⭐ TEK ÇUKUR · TEK OTOBÜS KAPISI [DERS 55]

```
SAYIM   çukur 1 · otobüs (kadrajda) G0: 1 · G1: 1 (lowbed'de) · G2–G5: 0 · G6: 1 (önü) · G7: 1 (arkası)
        boru G3: 1 sürekli hat · cephe 1 · çınar 1 · trafik lambası 1 — SEKİZ KAREDE DE
⛔ İkinci çukur, ikinci yama, caddede başka çöküntü, ikinci otobüs (G6–G7'de aynı anda iki)
   = KARE ATILIR.
⛔ G1'de çukur BOŞ: hayalet otobüs, hayalet boru = KARE ATILIR.
⛔ G6 (önü sağda) ve G7 (arkası solda) AYNI otobüstür: livery koyu kırmızı, üç kapı — farklı
   renk/kapı sayısı = ⑤ DEVAMLILIK düşer, kare atılır.
⛔ Araç kapısının ⑨ SAYIM TESTİ'yle ÖNCEDEN ölçülür; kapıda çıkarsa ARAÇ DEĞİŞİR.
```

## 7. ⭐ REJİM G KAPISI — S6 [SANTIYE_HAREKETI §1 · ikinci koşu]

```
① GÖLGE SABİT     G6 · G7'de cephe balkon gölgeleri aynı açıda (0° fark)
② İZ YOK          motion streak, bulanık ekip, hayalet nesne YOK; otobüs NET
③ FİGÜR           tek · sırtı kameraya · yüz okunmaz · G6 bariyer elinde, G7 bariyer yerde
④ HIZ             1×: otobüs ~3,5 m/s (8 sn'de ~28 m); ön teker doğu dikişi ≈ 1,0 sn,
                  arka teker batı dikişi ≈ 4,5 sn (günlük §4'e ölçülür)
⑤ RİJİT GÖVDE     otobüs 0 · 4 · 8 sn'de aynı boy, üç kapı, altı teker; kadrajdan çıkarken
                  kesilen kısım kesilir, KISALMAZ
⛔ Bunlardan biri düşerse S6 yeniden üretilir; ölçüm günlük §4'e, sonra DERSLER'e (kart D).
```

## 8. Zaman ve ışık

```
IŞIK GÜNÜ   07:20 → 17:30 = 10 sa 10 dk · 1×A + 5×B + 1×G (G ışık gününe 0 dk) ≤ 14 sa
GÜNEŞ       kadrajda HİÇ görünmez — gök yok, bakış kuzey · disk anılmaz [DERS 39]
GÖLGE       07:20 sola-uzağa uzun · 09:30 kısalır · 11:30 kısa uzağa · 13:30 kısa hafif sağa ·
            15:30 sağa uzar · 17:30 uzun turuncu sağa
KAMERA BLOĞU gölgesi yakın şeritlerde (alt bant), çukur/yama gün boyu GÜNEŞTE
G6–G7       IŞIK AYNI — LIGHTING bloğu iki karede birebir; gölge kıpırdamaz
MEVSİM      eylül ortası · tek gün · çınar tam yapraklı
⛔ KIŞ YOK — tek günlük film [DERS 7 · 26]
```

## 9. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM        süreler eşit (7 × 8,0) — proje sahibinin kesin kuralı, beyanlı
① / ③ İKİ DİKİŞ   8,0 (A → B: okunur figür → iz) ve 48,0 (B → G: iz → net) — beyanlı;
                  müziksiz 46,0–48,0 penceresi ikinciyi taşır; yeniden üretim sebebi DEĞİLDİR
⑦ S6 "İŞSİZ"      S6'da iş yoktur, ÖDÜL vardır — usta kare kasıtlı [plan §KONSEPT KAPISI]
① KEYSTONE        −40° tilt'te cephenin düşey çizgileri yakınsar — sekiz karede AYNI olduğu
                  sürece istasyon kayması DEĞİLDİR
⚠️ İKİNCİ ÇUKUR    beklenen DEĞİL — çıkarsa §6 gereği araç değişir
⚠️ SIVI DOLGU      beklenen DEĞİL — çıkarsa §5 gereği klip atılır
⚠️ SAPANSIZ YÜK    beklenen DEĞİL — çıkarsa §4 gereği araç sorgulanır
```
