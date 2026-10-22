# 🔍 GAME ON — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `GAME_ON_DIKEY_TIMELAPSE.md` · Günlük: `GAME_ON_URETIM_GUNLUGU.md` · Kapak: `GAME_ON_KAPAK.md`
> ⭐ QA koşusundan ÖNCE ajan ölçüm bloğunu ffprobe + klip_eslestir ile ELLE doldurur; mercekler ayrı sohbetlerde koşulur
> [DERS 105 · QA_KOSU §4].

```
FİLM      GAME ON · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 20.10.2026 · kural 7 × 8 · sahibin briefi 8) · KAPAK KARTI SONDA 5,0 sn (sahip kuralı 16.10.2026 · erime ≤ 1 sn) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / 5,0 sn (G8 + "GAME / ON") · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
          ⭐ yayın dosyası 1080 × 1920 [DERS 100]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok · ⭐ üretim sırası G8 (metinden) → G7 … G0 (geriye)
REJİM     S0–S6 B (2 sa) · S7 ⭐ A (10 dk) — iki rejim
IŞIK      TEK GÜN, AÇIK GÖK: 05:45 → 07:45 → 09:45 → 11:45 → 13:45 → 15:45 → 17:45 → 19:45 → 19:55 (güneş saati) ·
          41° kuzey · 21 Haziran (δ +23,4°) · güneş 69,6°/+12,5° → 306,2°/−4,1° · kamera 0°'ye (kuzey) bakar, tilt 31° aşağı ·
          güneş HİÇBİR karede kadrajda değil · final MAVİ SAAT: pota oturur, projektörler yanar
AİLE      ⭐ ZEMİN (yukarıdan bakılan saha, siluet yok) · arka duvar %47,5–79,7 · başlık alanı sıva bandının üstündeki koyu tuğla
TAKVİM    yok — tek gün (dönüşüm sıkıştırıldı, beyanlı); zaman taşıyıcısı gölgeler (sol → arka → sağ) + üst banttaki gök rengi
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① IŞIKLI SAHA — iki ışık direğinin projektörleri YANIK (x 50–122 · 870–927, baş py 833); sıcak beyaz ışık altında kömür oyun
    alanı (x 143–937 önde · 289–791 arkada), amber pota altı (x 425–655 · py 1046–1230), açık gri çevre bandı ve el eni beyaz
    çizgiler (dış sınır · pota altı kenarları · serbest atış çizgisi + tam daire · TEK üç sayı yayı · yarı saha çizgisi) okunur;
    kadrajın EN PARLAK şeyi ışıklı saha ve kırık beyaz bant
  ② POTA — TEK tekerlekli pota, orta eksende: ağırlıklı taban arka çizginin ardında gri bantta, beyaz pano (x 502–579) amber
    dairenin alt yarısının önünde, amber çember (x 530–550) pota altının uzak ucunun üstünde
  ③ DUVAR + SINIRLAR — sıva bandı kırık beyaz (x 233–847 · py 785–1008), ortasında TEK amber daire (x 469–611); üstü koyu tuğla,
    çatı hattı py 390 · iki yanda koyu tel çit · sol şeritte üç modüllü alçak ahşap tribün (x 9–235), beyaz sınırın dışında
  ④ TANIKLAR — solda molozla tepeleme konteyner (x 56–281 · G0'da üstünde ilk dolu kova vardı) · ön alçak duvarlar ve açık giriş ·
    çatı hattının ötesinde uzak çatılar ve mavi gök · işçi yok, el arabası yok, araç yok

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 56,0–58,0'da (2x: 28,0–29,0) pota yerinin 1 m önünden DÜZ geri gelir ve tabanına iner. Kopyalanırsa / ikinci çember belirirse /
   direk bükülürse / yerinde "belirirse" → S7 atılır [DERS 57 · 96 · paketin S08 kontrolü].
⛔ 58,0'da (2x: 29,0) iki projektör TEK ADIMDA birlikte yanar ve yanık kalır. Titrer, söner ya da biri ötekinden sonra yanarsa → S7
   atılır [DERS 98].
⛔ Işık yanarken pota, tribün, boya ya da çizgiler KAYARSA / yeni nesne belirirse (top, oyuncu, seyirci, skor tabelası, duvar yazısı,
   ikinci pota) → S7 atılır [DERS 91 ③].
⛔ Gök gündüze dönerse / ışık sahayı beyaza boğup çizgileri silerse / koyu tuğlayı (başlık zemini) aydınlatırsa → sebep G8; KARE
   yeniden üretilir, klip değil [DERS 91].
⛔ 60,0–64,0 FİNAL TUTUŞU: hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı 64,0–69,0 (yayında 32,0–37,0): kaynak G8'in kendisi + başlık, erime
   ≤ 1 sn, tutuşun DIŞINDA — logo, müzik, "before/after", "BUILDWAKE" YOK. Kart G8 ile aynı dünya değilse → E kaydı [DERS 85].
   klip_eslestir.py --kart 5 ile ölçülür. ⭐ Kartta şehir uğultusu (dijital sessizlik DEĞİL) [DERS 100].
⛔ Bir figürün yüzü okunursa ya da üçüncü figür belirirse S7 atılır [P5-b].
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 31°)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk | %90 (py 190) — arka binanın ardında; üst bantta uzak çatılar + gök | ±0,5 puan · kayarsa kamera kaydı |
| ⭐ çatı hattı + koyu tuğla | py 390 · 390–785 | DOKUZ KAREDE (nirengi ①) · koyu tuğla HİÇ boyanmaz |
| ⭐ sıva bandı | 233–847 px · %47,5–59,1 · 613 px | KESİR ±7 px · DOKUZ KAREDE (nirengi ②) · G0–G2 gri lekeli · G3→ kırık beyaz |
| ⭐ amber daire | 469–611 px · merkez x 540 · py 798–948 | G3→ · TEK · orta eksende |
| ⭐ ön duvarlar + giriş + konteyner | giriş 325–755 · konteyner 56–281 · py 1509–1773 | ±20 px [DERS 96 ①] · DOKUZ KAREDE (nirengi ③) |
| ⭐ G0 kova + yükleyici | kova 76–210 (konteynerin TAM üstü) · yükleyici 269–442 | YALNIZ G0 |
| ⭐ G0 moloz yığını | 206–874 px · py 983–1424 | YALNIZ G0 · önde tek temiz şerit |
| ⭐ çitler + ışık direkleri | sol 0–189 · sağ 817–1080 · direkler 50–122 / 870–927 | G4→ · iki yanda · giriş AÇIK · direk TAM İKİ |
| ⭐ pota altı (amber) | 425–655 px · %35,9–45,5 | G5→ · amber YALNIZ burada |
| ⭐ oyun alanı + çevre bandı | 143–937 (önde) · 289–791 (arkada) · bant 90–990 | G5→ · sınırlar G8 ile aynı |
| ⭐ çizgiler | serbest atış dairesi 455–625 · yay uçları 296–784 · yay tepesi x 540 · yarı saha py 1543 | G6→ · TEK yay · TEK daire · tam saha DEĞİL |
| ⭐ tribün | 9–235 px · %22,9–43,6 | G7→ · üç modül uç uca · beyaz sınırın dışında |
| ⭐ pota G7 / G8 | G7 500–580 · py 940–1067 · G8 501–578 · py 914–1040 | G7 → G8 TAM 1 m geri, orta eksende · TEK pota |
| işçi | ≈ 70–85 px boy | İKİ · yüz yok |
| üst band | %80–100 | yalnız uzak çatılar + gök |

## 3. ⭐ ARSANIN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ⭐ duvarın dibine kadar moloz yığını (kırık asfalt plakaları, beton, tuğla, toz), önde TEK temiz şerit (çatlak eski asfalt) ·
    ⭐ kompakt yükleyici girişin içinde, dolu kovası konteynerin TAM üstünde havada · sıva bandı gri, lekeli, dökük · iki işçi (biri
    kabinde, biri şeridin kenarında)
G1  ⭐ moloz YOK — bütün arsa çatlak, yamalı eski gri asfalt · ⭐ konteyner tepeleme · ⭐ damper (taze asfalt) + yürüyerek kullanılan
    silindir sağ altta · yükleyici YOK
G2  ⭐ girişten duvarın dibine TEK düz koyu gri yeni asfalt · ⭐ makaslı platform duvarın dibinde, boya kutuları, rulolar, ip · damper
    ve silindir YOK
G3  ⭐ sıva bandı kırık beyaz + TEK amber daire (orta eksen) · koyu tuğla AYNI · ⭐ çit istifi + iki yatık direk sağ altta
G4  ⭐ iki yanda ≈ 3 m koyu tel çit, giriş açık · ⭐ iki ışık direği (sönük) · ⭐ el arabası (boya + bant) · platform YOK
G5  ⭐ kömür oyun alanı · ⭐ amber pota altı (YALNIZ orada) · ⭐ açık gri çevre bandı (solda geniş) · çizgi YOK · ⭐ el arabası (çizgi takımı)
G6  ⭐ beyaz çizgiler (dış sınır · pota altı kenarları · serbest atış çizgisi + daire · TEK yay · yarı saha) · pota yeri BOŞ · ⭐ ilk
    tribün modülü alçak tekerlekli arabada
G7  ⭐ sol şeritte üç tribün modülü uç uca · ⭐ pota pota altında, yerinin 1 m TAM önünde, dik · iki işçi tabanında · projektörler SÖNÜK ·
    mavi alacakaranlık · boş el arabası girişte
G8  ⭐ pota yerinde · ⭐ iki projektör YANIK · işçi, el arabası YOK
⛔ SAYIM: arsa 1 · arka duvar 1 · giriş 1 · konteyner 1 · yükleyici (1·0·…) · damper + silindir (0·1·0·…) · platform (0·0·1·1·0·…) ·
   çit (0·0·0·0·2·2·2·2·2) · direk (0·0·0·2y·2·2·2·2·2 — y = yerde) · daire (0·0·0·1·1·1·1·1·1) · yay (0·…·1·1·1) ·
   tribün modülü (0·…·0·1a·3·3 — a = arabada) · pota (0·…·0·1·1) · işçi (2·2·2·2·2·2·2·2·0) — kadro HİÇBİR klipte ikiyi aşmaz [DERS 89]
⛔ Arka duvarın tuğlası, çatı hattı, sıva bandının sınırları, ön duvarlar, giriş, konteyner dokuz karede DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK · DERS 48 · beş soru ②③]

```
S0  moloz: yığın → kova → konteyner (yük yük, önden arkaya) · ilk yük: kova (konteynerin tam üstü) → konteyner · gevşek parça: el →
    el arabası → konteyner · yükleyici: → giriş (çıkar) · damper + silindir: giriş → sağ alt (yükleyici ÇIKTIKTAN sonra) [DERS 69]
S1  asfalt: damper → kürek → çatlak/çukur → silindir · damper → yığın (duvarın dibi) → tırmık → şerit → silindir (arkadan öne) ·
    damper + silindir: → giriş · platform: giriş → duvarın dibi (TEK TEK)
S2  kir: süpürge → yer · kırık beyaz: kutu → rulo → bant (şerit şerit, soldan sağa) · daire: ip (bandın ortasına iğneli) → iz → amber
    rulo · çit + direkler: giriş → el arabası → sağ alt
S3  modül (TEK TEK): istif → iki el → bordürdeki direkler (önden arkaya; önce sol, sonra sağ) · direk: yer → dik → taban plakası ·
    platform: → giriş · el arabası (boya + bant): giriş → sağ alt
S4  bant: rulo → bölge kenarı · kömür: kutu → uzun saplı rulo → oyun alanı (arkadan öne) · amber: → YALNIZ pota altı (bant içinde) ·
    açık gri: → çevre bandı · bant: sökülür · el arabası: → çizgi takımı
S5  beyaz: kutu → küçük rulo → bantlı çizgi (cetvel boyunca) · yay ve daire: şerit metre (pota altının ortası) → iz → rulo · bant:
    sökülür · ilk tribün modülü: giriş → alçak tekerlekli araba → sağ alt
S6  modül (×3, TEK TEK): araba → sol şerit (DOĞRUDAN yerine) → cıvata (uç uca) · pota: giriş → tekerlekler → orta eksen → pota altı
    (yerinin 1 m önü, dik)
S7  pota: pota altı → 1 m geri → tekerleklerden ağırlıklı tabana (gri bant) · ışık: düğme → iki projektör → saha · işçiler + el
    arabası: → giriş
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı ön giriş, damper, el arabası, istif ya da tekerlekli araba [DERS 48 · 49].
⛔ Araçlar AYNI ANDA hareket etmez: S0 · S1 sonlarında biri çıkar, sonra öteki girer [DERS 69]. Vinç, ikinci yükleyici, çizgi makinesi,
   basınçlı yıkayıcı YOK [DERS 67].
⛔ Tribün modülleri kendiliğinden kaymaz; her biri arabayla gelir, TEK TEK, DOĞRUDAN yerine oturur [DERS 61 · 89].
```

## 5. ⭐ IŞIK KAPISI [ZAMAN_VE_ISIK · ISIK_FINALI]

```
G0     05:45 (69,6°/+12,5°) · ⭐ alçak sabah güneşi sağda önde · duvar gölgede · uzun gölgeler solda, kameraya doğru
G1     07:45 (87,6°/+34,6°) · parlak sabah · duvar yalanır · gölgeler solda
G2     09:45 (111,4°/+56,8°) · duvar eğik ışıkta · kısa gölgeler solda
G3     11:45 (168,7°/+72,2°) · ⭐ en düz ışık, duvar tam ışıkta · gölgeler tabanda
G4     13:45 (239,4°/+61,9°) · kısa gölgeler sağa, ileri
G5     15:45 (267,4°/+40,2°) · ılık · sol çitin file gölgesi sahanın soluna
G6     17:45 (285,9°/+17,8°) · ⭐ altın akşam · duvar gölgede · uzun çit gölgeleri sağa
G7     19:45 (304,5°/−2,6°) · ⭐ mavi alacakaranlık · çatı hattının üstünde solda sönen pembe · projektörler SÖNÜK
G8     19:55 (306,2°/−4,1°) · daha koyu mavi · ⭐ iki projektör YANIK
⛔ Gölgeler TEK YÖNDE döner (sol → arka → sağ); G5 → G8 gök TEK YÖNDE kararır; geri aydınlanan kare = zaman ters → ❷ [DERS 98 · 104]
⛔ G0–G7 boyunca HİÇBİR yapay ışık yanmaz — projektörler G8'e kadar sönük
⛔ Güneş diski HİÇBİR karede yok (kadraj azimutu −16,6° … +36,6°, güneş 58° → 302°) [DERS 39 · 70] · disk belirirse kare yeniden
```

## 6. ⭐ BİR ARSA · BİR POTA · İKİ İŞÇİ KAPISI [DERS 55 · 89 · 42]

```
Korpus riski: "basketball court" → oyuncu, top, kalabalık, skor tabelası, tam saha (iki pota), duvar yazısı · "street" → grafiti ·
"construction" → kalabalık ekip, ikinci makine (ÇIKARIM — bu filmde ölçülmedi). "basketball" yalnız YAPI BIBLE'da; players · crowd ·
scoreboard · graffiti · mural promptta YOK.
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ) · "Only two workers" her I2V'de · G8'de "No people are present."
② araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç işçi / kaç pota / kaç araç aynı anda / kaç tribün modülü
⛔ ikinci pota · ikinci daire · ikinci yay · tam saha çizgileri · top · oyuncu · seyirci · üçüncü işçi · aynı anda iki araç · dördüncü
   tribün modülü · üçüncü direk · duvar yazısı → ⑧
⛔ Model arka duvarı, çatı hattını, ön duvarları ya da konteyneri yeniden çizerse → ⑤ DEVAMLILIK (kimlik nesneleri)
⛔ Duvarda, panoda, konteynerde, tribünde okunur yazı (numara, logo, tabela) → ❶ metin [negatif çekirdek "on any surface"]
```

## 7. ⭐ KLİP İÇİ ZAMAN KAPISI [DERS 92]

```
Her klipte İKİNCİ YARIDA görünür bir ilerleme olmalı (2x'te 2,0–4,0 sn):
  S0 son yükler, yükleyici çıkar, damper girer · S1 yeni asfalt öne yaklaşır, platform gelir · S2 amber daire, çit istifi · S3 sağ çit,
  direkler, el arabası · S4 amber + gri, bant sökülür · S5 daire, yay, yarı saha, tribün modülü · S6 gün batımı, pota gelir · S7 tutuş
  (kasıtlı)
⛔ 2x'te 2,0–4,0 arası tamamen durgun klip → ⑦ TEMPO bulgusu BEKLENEN DEĞİL; pilotta ölçülür, ara kare kararı sahibe.
⛔ Saniye damgaları HEDEFTİR; mercek "iş planlanandan erken bitti" derse ölçülmüş davranıştır (DERS 92), kusur sayılmaz —
   kusur, ikinci yarının BOŞ kalmasıdır.
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil · ⭐ her klibin Veo sesi ayrıca dinlenir [DERS 100]
· 150 Hz altı tek taşıyıcı yok · konuşma yok · uzak şehir uğultusu yatak · top sesi YOK · basınçlı yıkama sesi YOK
· 0,0 molozun konteynere dökülüşü · yükleyici motoru · 7,0 yükleyici uzaklaşır · 8–15 kürek, tırmık, silindir titreşimi · 16–23
  süpürge → rulo, platform motoru · 24–31 çit modülleri, cıvatalar, direk tabanları · 32–39 bant, uzun saplı rulo · 40–47 bant
  sökülüşü, şerit metre · 48–55 araba tekerleği, ahşap modüller · 55,0 pota tekerlekleri · ⭐ 56,5–57,8 tabanın yere inişi ·
  ⭐ 58,0 şalter + projektör vızıltısı (KARE SENKRON ±2 kare) · 58–60 adımlar · 60,0–64,0 alacakaranlık sokağı
· KART 64,0–69,0: şehir uğultusu sürer, kartın son saniyesinde söner → döngüde S0'ın moloz dökülüşüne bağlanır
```

## 9. Zaman ve ışık

```
G0 05:45 69,6°/+12,5° · G1 07:45 87,6°/+34,6° · G2 09:45 111,4°/+56,8° · G3 11:45 168,7°/+72,2° · G4 13:45 239,4°/+61,9° ·
G5 15:45 267,4°/+40,2° · G6 17:45 285,9°/+17,8° · G7 19:45 304,5°/−2,6° · G8 19:55 306,2°/−4,1°
(41°K · δ +23,4° · güneş saati · TÜRETİLMİŞ model · açık gök · SKY VAULT ile aynı gün modeli)
· zaman gölgeler (sol → arka → sağ) ve üst banttaki gök rengiyle taşınır; final mavi saatte, projektörlerle
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (brief 8 sahne), beyanlı
① / ③ DİKİŞ     56,0 (B → A): uzun izli figürlerden kısa izli, tanınır figürlere; ışık mavi saatte sabitlenir — beyanlı [P5-c]
① KADRAJ        tilt 31° · 16 m — paketin 5 m'sinden sapma (geometri, plan TASARIM ③); keystone: çitler ve direkler alt kenara doğru
                açılır; işçiler küçük (≈ 70–85 px); G0 açılış hareketi alt bantta (py 1440–1720) — beyanlı
⑤ DEVAMLILIK    zemin (moloz → çatlak → düz → renk → çizgi) ve duvar bandının rengi KASITLI değişir; arka duvarın tuğlası, çatı hattı,
                bant sınırları, ön duvarlar, giriş, konteyner DEĞİŞMEZ · araçlar yalnız G0–G3'te KASITLI
⑦ İŞ            S7'nin 4–8'inde iş yok (kasıtlı tutuş) · G8 boş saha (kasıtlı: işçisiz final, kapak kaynağı)
⑦ TEMPO         S6 sonu + S7 başı (yerinin önünde duran pota) 2x'te ~0,5 sn durgunluk — beyanlı bekleyiş
❺ TESLİM        işlev anı ışık — LAST STOP ile aynı yapı (oturur → ışık yanar), TOTAL RESET · POOL ROOM da ışık (sahip bilerek seçti
                20.10.2026); fark: dış saha, ışık direklerden sahaya dökülür
```
