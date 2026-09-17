# 📊 00_INDEX — PROJEDEKİ TEK SAYAÇ

> ⛔ Sayılar buraya ELLE yazılır ama `bash araclar/sayac.sh` ile
> KARŞILAŞTIRILIR. Betik uyuşmazlığı ekrana basar. Bir sayıyı iki yerde
> tutmak, birini yanlış tutmaktır.

---

## SAYIM

```
TOPLAM FİLM       17
ÖLÇÜLEN FİLM      12
TAM ÖLÇÜLEN       0     (8 merceğin 8'i de koşulmuş — ⑦ ⑧ 07.09.2026'da açıldı)
SEKİZ MERCEKLE    8     (THE LONG DAY · THE DUST YEAR · BUILT FROM DUST · POLAR HABITAT · THE CROSSING · OVER THE WALL · THE EMPTY RIDGE · THE DARK ROCK)
ON İKİ MERCEKLE   3     (OVER THE WALL · THE EMPTY RIDGE · THE DARK ROCK — ⑨ ⑩ ⑪ ⑫ dâhil)
ALTI MERCEKLE TAM 3     (⑦ ⑧ öncesi tamlık)
ÜRETİLEN FİLM     11
YAZILDI, ÜRETİLMEDİ 5   (BEFORE NIGHTFALL · THE OLD ROAD · THE HIDDEN OASIS · THE NARROW GORGE · THE LAST CIRCLE — plan + SPEC hazır, araç kapısı koşulmadı)
```

## TAMLIK MATRİSİ

Bir film "tam ölçüldü" sayılmak için sekiz merceğin sekizini de görmelidir.
⑦ ve ⑧ 07.09.2026'da açıldı; önceki dört filmin hiçbiri bu ikisiyle ölçülmedi.

| Film | ① KARE | ② İNŞA | ③ ZAMAN | ④ TESLİM | ⑤ DEVAM | ⑥ GEÇİŞ | ⑦ İŞ | ⑧ YÖNTEM | Tam |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **THE LONG DAY** | Ⓥ 6,4 karesiz | ⛔ belgesiz | **7,0** | ⛔ belgesiz | Ⓥ 5,8 karesiz | ⛔ belgesiz | Ⓥ 4,4 karesiz | ⛔ belgesiz | **8/8** · 8'i de RUN INCOMPLETE |
| **THE MOUNTAIN DOOR** | Ⓥ 1,1 | ⛔ belgesiz | **3,6** | ⛔ belgesiz | Ⓥ 0,2 | ⛔ belgesiz | ❌ | ❌ | **6/8** |
| **THE NARROW LOT** | Ⓥ 6,0 | ⛔ belgesiz | **4,2** | ⛔ belgesiz | Ⓥ 5,6 | ⛔ belgesiz | ❌ | ❌ | **6/8** |
| THE LONG SHADOW v1 | Ⓥ 3,3 | Ⓥ 0,4 | Ⓥ 4,3 | Ⓥ 2,7 | ❌ | ❌ | ❌ | ❌ | **4/8** |
| THE CLOSING SPAN | 1,0 | Ⓥ 0,0 | 1,3 | Ⓥ 5,4 | Ⓥ 0,0 | Ⓥ 1,6 | ❌ | ❌ | **6/8** |
| **THE DUST YEAR** | Ⓥ 1,3 karesiz | ⛔ belgesiz 0,9 | 4,0 | ⛔ belgesiz 2,1 | Ⓥ 4,0 karesiz | ⛔ belgesiz 6,6 | Ⓥ 1,3 karesiz | ⛔ belgesiz **0,0** | **8/8** · 7'si RUN INCOMPLETE |
| **BUILT FROM DUST** | Ⓥ 1,1 karesiz | ⛔ belgesiz 2,8 | Ⓥ 3,3 | ⛔ belgesiz 2,5 | Ⓥ 1,6 karesiz | ⛔ belgesiz 4,5 | Ⓥ 1,8 karesiz | ⛔ belgesiz **0,0** | **8/8** · 8'i de RUN INCOMPLETE |
| **THE CROSSING** | Ⓥ 8,4 | ⛔ belgesiz 6,4 | **10,0** | ⛔ belgesiz 7,9 | Ⓥ 5,8 karesiz | ⛔ belgesiz **10,0** | Ⓥ 8,8 karesiz | ⛔ belgesiz **2,8** | **8/8** · 4'ü RUN INCOMPLETE |
| BEFORE NIGHTFALL | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ |
| THE OLD ROAD ⭐ yatay | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 16.09.2026 · ilk 16:9 film) |
| THE HIDDEN OASIS | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 16.09.2026 · ilk restorasyon) |
| THE NARROW GORGE | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 16.09.2026 · ilk kurgu yakınlaşması) |
| THE LAST CIRCLE | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 17.09.2026 · ilk kayar kalıp · tek hareket S6'da) |
| **THE DARK ROCK** | ⛔ V karesiz 4,9 | ⛔ belgesiz 3,8 | Ⓥ 2,8 | ⛔ belgesiz 6,1 | Ⓥ 3,1 karesiz | ⛔ belgesiz 2,9 | ⛔ karesiz 5,1 | ⛔ belgesiz 4,5 | **8/8** + ⑨⑩⑪⑫ · 12'si de RUN INCOMPLETE |
| **THE EMPTY RIDGE** | Ⓥ 2,8 | ⛔ belgesiz 5,2 | **5,4** | ⛔ belgesiz 3,4 | Ⓥ 7,2 karesiz | ⛔ belgesiz 7,6 | Ⓥ 7,0 karesiz | ⛔ belgesiz **9,1** | **8/8** + ⑨⑩⑪⑫ · 11'i RUN INCOMPLETE · ⛔ günlüksüz üretim |
| **OVER THE WALL** | Ⓥ 5,8 | ⛔ belgesiz 3,8 | Ⓥ 6,0 | ⛔ belgesiz 5,3 | Ⓥ 3,0 karesiz | ⛔ belgesiz 7,0 | Ⓥ 3,8 karesiz | ⛔ belgesiz **0,0** | **8/8** + ⑨⑩⑪⑫ · 11'i RUN INCOMPLETE · ⛔ günlüksüz üretim |
| **POLAR HABITAT** | Ⓥ 7,7 | ⛔ belgesiz | Ⓥ 9,8 | ⛔ belgesiz | Ⓥ 10,0 | ⛔ belgesiz | Ⓥ 7,9 | Ⓥ 8,2 | **8/8** |

```
⚠️ THE LONG SHADOW v1'in ⑤ ve ⑥'sı KOŞULMADI çünkü o iki mercek film
   ölçüldükten SONRA açıldı. v1 arşivdir ve yeniden ölçülmeyecek — ama
   raporlarında ikisinin de malzemesi zaten var:
     ⑤'in konusu: "crane switches from grey flat-top to blue saddle jib"
                   (② kat.7) · "materials and vehicles morph" (① kat.8)
     ⑥'nın konusu: "cut 1 to cut 2 reverses time entirely" (③ kat.7)
   İki mercek de v1'de ayrı ayrı sorulsaydı bu bulgular DAHA ERKEN ve
   DAHA NET çıkardı. Açılma sebepleri budur.

⚠️ ⑦ İŞ ve ⑧ YÖNTEM dört filmin dördünde de KOŞULMADI — 07.09.2026'da,
   proje sahibinin isteğiyle açıldılar: "durmadan inşa" ve "her parça
   sıfırdan, yapımı görünerek". Malzemeleri eski raporlarda zaten var:
     ⑦'nin konusu: "workers hold frozen poses for the whole clip" (① kat.8)
     ⑧'in konusu: ② APPEARING hükmü dört filmde dört kez — ama hangi PARÇA
                  belirdi, hiçbir rapor adıyla yazmadı. ⑧ onu adıyla yazar.
```

```
⭐ THE NARROW LOT — DEPONUN İLK GEÇEN HÜKÜMLERİ
   ① TIMELAPSE ✅ · ③ PASSES ✅ · ⑤ SAME WORLD ✅ + kanıt nesnesi BULUNDU ·
   ⑥ TIME ✅.  Üç filmde ilk kez kadraj, dünya ve kesme aynı anda tuttu.
   ⛔ Düşen: ② DIFFERENT · APPEARING (üçüncü kez) · ⑥ METRONOM (ikinci kez) ·
      ④ NONE FOUND (üçüncü kez) · ③ TIME RATE 0/10 (gökyüzü ve gölge DONDU).
   ⭐ TAM KOŞAN TEK MERCEK ③'TÜR ve hükmü GEÇTİ. Beş mercek eksik girdiyle
      koştu: ① ve ⑤'e kare grabı, ② ④ ⑥'ya belge verilmedi.
```

```
🔴 THE DUST YEAR — ALTINCI FİLM · İLK MARS SAHASI · ⑧ DEPONUN EN DÜŞÜK SKORU
   ⛔ Film ARAÇ KAPISI KOŞULMADAN üretildi; üretim günlüğü hâlâ "DURUM ⛔ BOŞ".
      İzi ölçülebilir: ① dört istasyon grubu (tek istasyon beyan edilmişti) ·
      teslim ızgarası 6·8·4·4·6·4·10·4·6·10 = 62,0 sn, plan 60,0 idi
      (S1↔S2 yer değiştirmiş, S9 8,0 → 10,0).
   ⛔ Düşen: ⑧ APPEARED 0,0/10 — SEKİZ elemanın SEKİZİ "INCOMPLETE at NEVER".
      Yeni INSAAT_YONTEMI kılavuzunun bütün amacı buydu ve plan ona uymuştu;
      sonuç THE LONG DAY'den (1/9 MADE) DAHA KÖTÜ → DERS 36.
      ② DIFFERENT·APPEARING (altıncı kez) · ⑦ PARKED (on klibin sekizi %100
      boş) · ⑤ A SET REBUILT EACH TIME · ⑥ METRONOM (BEŞİNCİ kez — ızgara
      varyanslı olduğu hâlde → DERS 44) · ④ COST/FINAL BEAT FAIL.
   ⭐ Tutan: ⑥ TEXT AND BRANDING 10/10 · ⑤ VEGETATION AND WATER 10/10 ·
      ⑥ CUT MECHANICS 10/10 · DIRECTION 10/10 · ③ "About one year" —
      filmden okunan süre plandaki 1 Mars yılını TUTTU.
   ⭐ Kimse yürüyen insan bildirmedi: DERS 33'ün pozitif yarısı ("No people
      are present.") TUTTU. İnsan makinenin içinden geldi → DERS 41.
   → DERSLER.md: DERS 35-44 · DERS 34'ün kilidi ölçüldü ve düştü.
```

```
🔴 OVER THE WALL — DOKUZUNCU ÜRETİLEN FİLM · İLK BARAJ · 14.09.2026 · ON İKİ MERCEK
   ⛔ Film ÜRETİM GÜNLÜĞÜ TUTULMADAN üretildi (günlük "DURUM ⛔ BOŞ" — DUST YEAR
      ve LONG DAY'den sonra ÜÇÜNCÜ kez [DERS 28]). Kurgu 7 klip · 7,8·8,0·10,7·
      10,0·8,0·13,0·6,0 = 63,5 + kart 4,5 = 68,0 sn; ne 14.09 planına (8 × 8,0)
      ne 12.09 planına (10 sahne) oturuyor. Hangi promptlardan üretildiği
      bilinmiyor. 12 merceğin 11'i RUN INCOMPLETE; yalnız ① kare aldı (69).
   ⛔ Düşen: ⑤ A SET REBUILT EACH TIME (6/6 dikiş) + ⑧ APPEARED 0/4 → film
      "zincir koşulmadı" diye kapanır [kart R 6a]. ② DIFFERENT · APPEARING
      (SEKİZİNCİ kez; POLAR ve CROSSING'in BUILT'inden sonra geri düşüş) ·
      ① SIX SEPARATE SHOTS (plan dışı İKİNCİ İSTASYON, klip 5) · ③ NOT IN ONE
      DIRECTION (kar 4 kez gidip geldi; okunan süre 1,5–2 yıl, plan 1 yıl) ·
      ⑦ PARKED · CAUSE AND EFFECT 0 (duvarda çalışma cephesi YOK, makineler
      köprüde) · ⑩ MAGICAL APPEARANCE · ⑪ INTRUDERS (havuz · derrick kule) ·
      ⑫ MELTING (köprüde çift araç birbirinin içinden geçti).
   ⭐ Tutan: 12/12 END CARD SAME (DERS 30 ilk kez bütün merceklerde) · ① CAMERA
      LOCK 9 · ③ SEASON CARRIER 10 · ④ ENDS + FINAL BEAT PASS + ONE THING
      BULUNDU · ⑥ TIME · ⭐ RHYTHM — ⑤ REBUILT iken İLK KEZ; kurgu varyanslıydı.
      DERS 44'ün tersi ölçüldü; 8 × 8,0 düz kilide karşı kanıt (RAPORLAR §7).
   → DERSLER.md: DERS 51-54 · RAPORLAR/OVER_THE_WALL.md · HAM_RAPORLAR/OVER_THE_WALL/
```

```
⭐ THE EMPTY RIDGE — ONUNCU ÜRETİLEN FİLM · İLK TÜRBİN · 14.09.2026 · ON İKİ MERCEK · DEPONUN EN İYİ ÖLÇÜMÜ
   ⛔ Plan ve üretim aynı gün; günlük TUTULMADI (dördüncü film [DERS 28]). Kurgu 8 klip, varyanslı
      (4,9·3,6·6,3·7,0·10,0·8,1·7,9·8,0); plan 7 × 8,0. ① dört istasyon grubu + klip 1–2 push-in;
      plan tek sabit istasyon. 12 merceğin 11'i RUN INCOMPLETE; ③ tam girdiyle koştu.
   ⭐ İLK KEZ AYNI ANDA: ⑤ SAME WORLD (kanıt = plana konan yalnız meşe — planlı çapa ilk kez bulundu)
      · ⑧ MADE 6/6 · 9,1 (deponun en yüksek ⑧; ilk beliren parça YOK) · ⑫ SOLID (ilk SOLID) ·
      ⑥ TIME · RHYTHM (varyanslı kurgu, 3. kez) · ③ PASSES + süre tahmini "2–3 ay" TUTTU (plan 9,5 hf)
      · ⑨ PRODUCTIVE · 12/12 END CARD SAME.
   ⛔ Düşen: ① SIX SEPARATE SHOTS (kamera hareketi, dört istasyon, SURFACE 1) · ② DIFFERENT (yapı BUILT,
      ama 0:21 ve 0:39'da HAYALET KULE kopyaları) · ⑩ MAGICAL APPEARANCE (segment · nasel · kanat kancasız
      pop; dağ arka planı halatı kurtarmadı) · ⑪ INTRUDERS · ④ NONE FOUND (5.) · RESISTANCE 2 (rüzgâr
      bekleyişi okunmadı) · rotor montajda döndü.
   → DERSLER.md: DERS 55 (çoğul korpus) · 56 (göbek döndürme → rotor döner) · 57 (yük havada taşınmaz;
     DERS 22 mekanizması düştü) · DERS 25 ✅ tuttu · DERS 44 tersi 3. kez · RAPORLAR/THE_EMPTY_RIDGE.md
```

```
✅  koşuldu, skor tabloda
Ⓥ   koşuldu ama mod V (ön koşu) — tamlık için sayılır, skor bağlayıcı değil
❌  koşulmadı
—   üretim yapılmadı, koşulamaz
```

## DURUM

```
THE NARROW GORGE — ON ALTINCI FİLM · İLK BARAJ · YAZILDI 16.09.2026 · ÜRETİLMEDİ ⛔
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK (sahip kararı) · zincirli · 8 kare + 7 I2V
   YAPI: dar boğazda çift eğrilikli beton KEMER BARAJI · kapaklı dolusavak · dip savak · enerji kırıcı havuz
   ⭐ İKİNCİ VİNÇSİZ PLAN: beton BANT KONVEYÖRLE gelir ve OLUKTAN düşer; havada asılı yük yok [DERS 8 · 22 · 46 · 57]
   ⭐⭐ DEPONUN İLK KAMERA HAREKETİ — KURGU YAKINLAŞMASI (proje sahibinin kararı, 16.09.2026):
      HOME ana kadraj · S0 1,55× · S1 2,0× · S3 1,7× · S6 2,0× · S2/S4/S5 sabit · her sahne HOME'da başlar ve biter
      ⛔ KILAVUZ_REHBERI §1.2 ("format kimliği sabit kameradır") ve DERSLER P2-l ② ("crop push-in ALINMADI")
         AÇIKÇA GEÇERSİZ KILINDI. Karar sahibindir, ÖLÇÜLMEMİŞTİR; ① KARE ve ⑤ DEVAMLILIK hükümleri
         BEKLENEN sayılacak. Promptlar sabit kamera ister; yakınlaşma yalnız KURGUDA.
      ⛔ FORMAT ŞARTI: kaynak klipler ≥ 2160 × 3840 (2,0× için). Araç vermiyorsa tavan düşer — araç kapısı ⑨.
   ⭐ Eleştiri turundan sekiz düzeltme işlendi: ilk saniyede kırıcı kayada · bedel "denetime alınan akış +
     söğütlü kıyının kaybı" · üç su sistemi ayrıldı (geçici tünel ÇIKIŞI köprünün aşağısında · dip savak ·
     kapaklı dolusavak) · S3 kanıtı GÖZ ÇİZGİSİ (%50) oldu (köprü hizası kadrajda gerçekleşmiyordu) ·
     final "ilk kontrollü salım" (kapak S4'te yerleşir, S6'da açılır; hazne dolumu S5→S6 kesmesinde) ·
     S4 TAMAMLAR · kart kaldırıldı · finalde krette doğrudan altın ışık istenmiyor (mavi saat)
   BEDEL: dolaşan doğal akış + söğütlü çakıl bariyerleri + değirmen arkının suyu · AYNI YER: tek gözlü taş köprü
   Işık tek gün 05:30 → 19:30 (7 × rejim B = 14,0 saat ⚠️ üst sınırın TAM üstünde) · takvim KESMELERDE geçer
   plan ✅ · QA_SPEC ✅ (§7 KURGU KAPISI) · KAPAK ✅ (kart yok; bölünmüş küçük resim G0 + G7) · günlük açıldı ⛔ BOŞ
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0
   ⚠️ AÇIK KARARLAR: ışık günü 14,0 saat mi 12,5 mi · GİZLİ VAHA'nın kartı da kalksın mı · S6 fiziksel
     hareket denemesi üretilsin mi · siluet ailesi KÜTLE
   → dikey_shorts/THE_NARROW_GORGE/

THE HIDDEN OASIS — ON BEŞİNCİ FİLM · İLK RESTORASYON · YAZILDI 16.09.2026 · ÜRETİLMEDİ ⛔
   dikey_shorts · ızgara 7 × 8,0 = 56,0 + kart 5,0 = 61,0 sn · ⛔ DÜZ IZGARA (sahip kilidi) · zincirli · 8 kare + 7 I2V
   ⛔ ARA KARE YOK: her sahne tek 8,0 sn klip
   ⭐ İLK YIKIM-DEĞİL-DÖNÜŞTÜRME: yapı sıfırdan kurulmaz, VAR OLAN havuz başka bir şeye çevrilir
   ⭐ İLK AŞAĞI BAKAN İSTASYON: tilt −40° · KAMERA_ISTASYONU §3 formülü GEÇMEZ, plan kendi formülünü yazar
     (yüzde(d) = (76,87° − atan(6,0/d)) / 73,74°) · ufuk ve gök kadrajda YOK → kılavuza yeni alt kart borcu
   ⭐ KİNETİK PAKET: THE DARK ROCK'tan dokuz araç devralındı (kenar geçişi · dikey süpürme · gölge süpürmesi ·
     bulut gölgesi · üç vuruş · ödülün gecikmesi · yüzey sınırı · iz bırakan araç · ekip lekesi) + onuncu olarak
     YANSIMA. ⛔ Kamera hareketi DEVRALINMADI — DARK ROCK'ta da yoktur (sahip düzeltmesi, 16.09.2026)
   BEDEL: havuzun havuz olması (açık mavi seramik + merdiven + hacim) · AYNI YER: kemerli niş (≈99 × 134 px)
   Işık tek gün 06:20 → 18:30 · 6 × B + 1 × A = 12 sa 10 dk ≤ 14 · takvim YOK (film BİR GÜN anlatır, beyanlı)
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ (bölünmüş ızgara kapağı + G7 kartı) · üretim günlüğü açıldı ⛔ BOŞ
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0
   ⚠️ AJAN KARARLARI sahibin onayına açık: kapak kartı eklendi (dış plan kartsızdı) · rejim B+A · S1 yükü ·
     siluet ailesi "ZEMİN" önerildi (yeni aile) · tilt kartı ölçülmedi
   → dikey_shorts/THE_HIDDEN_OASIS/

THE OLD ROAD — ⭐ DEPONUN İLK YATAY (16:9) FİLMİ · YAZILDI 16.09.2026 · ÜRETİLMEDİ ⛔
   yatay_2_dk_filmler · ızgara 15 × 8,0 = 120,0 + kart 5,0 = 125,0 sn · ⛔ DÜZ IZGARA (sahip beyanı, modül 12 × 10,0)
   zincirli · 16 kare (G0…G15) + 15 I2V · ara kare YOK · bölüm sınırı G8 · QA birimi FİLM
   YAPI: itmeli beton viyadük — 420 m, 7 açıklık, 5 ayak; ⭐ tabliye KALDIRILMAZ, İTİLİR → DERS 8 · 22 · 46 · 57
     devre dışı kalır; 1 numaralı risk gövdenin sıçraması, araç kapısına ⑨ İTME TESTİ eklendi
   BEDEL: eski yolun trafiği — G0'da 14 virajda far izleri, G15'te viyadükte tek düz çizgi, virajlar boş ama OKUNUR
   DİRENÇ: kar erimesi seli — S7'de su yükselirken itme sürer ve kaya bermi dökülür, S8'de sel geçişi ve bermi
     götürür (itme DURUR), S9'da hat yeniden kurulur: çalışan hat → kopuk hat → yeniden kurulan hat
   IŞIK: tek gün 05:05 → 18:35 · 9 A + 6 B = 13,5 h ≤ 14 · ⚠️ üsluplu sıkıştırma beyanı (tek günde çekilmedi)
   TAKVİM: 627 gün ≈ 20,6 ay · iki kış, iki yaz · kar YALNIZ kar çizgisiyle (vadiye kar yağmaz)
   00_ANALIZ altı dosya ✅ · PLAN ✅ · BOLUM_1/2 ✅ · KAPAK ✅ · MUZIK ✅ · YAYIN_PAKETI ✅ · QA_SPEC ✅ · günlük ⛔ BOŞ
   ⛔ KAPI (klasör modu): BLOCK 0 · FIX 2 — kutu seti ölçülmedi · süreler eşit (ikisi de beyanlı)
   ⭐ YATAY (16:9) ilk kez: kadraj formülü, güvenli alan ve ışık günü toplamı ÖLÇÜLMEDİ — bu film onların ilk ölçümü
   ⭐ Siluet ailesi YATAY (EMPTY RIDGE · DARK ROCK DİKEY'den sonra sıradaki aile) · havuz #4
   → yatay_2_dk_filmler/THE_OLD_ROAD/

THE DARK ROCK — ON ÜÇÜNCÜ FİLM · İLK FENER · YAZILDI 15.09.2026 · ÜRETİLMEDİ ⛔
   ızgara 6 × 8,0 = 48,0 sn + kapak 5,0 · ⛔ DÜZ IZGARA (proje sahibi kilidi) · zincirli · 7 kare + 6 I2V
   ⛔ ARA KARE YOK (proje sahibi, 15.09.2026): her sahne tek 8,0 sn klip · S3'te kopan hat yalnız klip ortasında — kabul edilen risk
   ⭐ İLK VİNÇSİZ PLAN: tek düşey taşıyıcı raylı asansör kabini; uzun rijit yük havada taşınmaz [DERS 8 · 22 · 46 · 57]
   ⭐ Eleştiri turundan yedi düzeltme işlendi: fırtına = iniş hattı arızası (rampa kayar → yeniden oturur) · gövde
     fırtınadan önce biter · 900× dili (köpük ALANI, ıslak BANT) · üst iskele sökümü S4 sonunda tepeden · martı
     yalnız atmosfer · ödül ilk ışığın BELİRMESİ (huzme yok) · loop iddiası yok, 7,0 sn sonuç ekranı riski beyanlı
   BEDEL: kayanın çentikli tacı (%39 → kaide %34,5) · AYNI YER: THE NEEDLE (tek sütun, ≈200 px)
   Işık tek gün 07:00 → 19:00 (6 × rejim B = 12 saat) · takvim tarladan + deniz renginden (~6 ay) · kış yok
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ (başlık iki satır, alt bantta — ⚠️ sahip kararı) · üretim günlüğü açıldı ⛔ BOŞ
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0
   ⚠️ DİKEY siluet ailesi — THE EMPTY RIDGE ile ARDIŞIK yayınlanamaz (YAYIN_PLANI §3) · havuz #11
   → dikey_shorts/THE_DARK_ROCK/

THE EMPTY RIDGE — ON İKİNCİ FİLM · İLK TÜRBİN · ÜRETİLDİ ✅ (günlüksüz ⛔) · 12/12 mercek ✅ · 11'i RUN INCOMPLETE ⛔
   ızgara 7 × 8,0 = 56,0 sn + kapak 5,0 · ⛔ DÜZ IZGARA (proje sahibi kilidi) · zincirli · 8 kare + 7 I2V
   ⛔ Kurgu 8 klip varyanslı, plana oturmuyor; kesme_kontrol.sh koşulamadı (teslim.mp4 depoda yok)
   ⭐ GEÇEN: ⑤ SAME WORLD (meşe) · ⑧ MADE 9,1 · ⑫ SOLID · ⑥ RHYTHM · ③ PASSES (tahmin tuttu) · ⑨ · 12/12 kart SAME
   ⛔ DÜŞEN: ① SIX SEPARATE SHOTS (push-in + 4 istasyon) · ② DIFFERENT (hayalet kuleler) · ⑩ MAGIC · ⑪ · ④
   → KARAR: yayınlanmaz · YENİDEN ÜRETİLİR (yeniden yazılmaz): plan tutuyor, üç cümle düzeltilir
     (DERS 55 · 56 · 57) — önce ARAÇ KAPISI (⑨ vinç testi) + ÖN GÖRSELLEŞTİRME + GÜNLÜK · tek istasyon.
     RAPORLAR/THE_EMPTY_RIDGE.md §9 · kapak başlığı üst %12,5'te → KAPAK.md bandına çekilir
   ⭐ DİKEY siluet ailesi (YAYIN_PLANI §3 sırası: OVER THE WALL KÜTLE → DİKEY) · havuz #5
   ⭐ DERS 22'yi İSTASYONLA çözen ilk vinçli plan: kamera pad'in +100 m üstünde, göz çizgisi = göbek (%50),
     bom başı %55 < uzak sıradağ silueti %57 → bütün kaldırmalar DAĞA karşı; SAHA ŞARTI (+6°) ve ön
     görselleştirme adımı plana yazıldı. DERS 51 (iş yüzeyi adı + yüzde) · 52 (tek istasyon) · 53 (dar
     yüzeyde tek araç) · 54 (kuru katlı ilk hâl) bu planın doğduğu gün kılavuza indi ve uygulandı.
   ⭐ Işık tek gün 06:00 → 20:00 (7 × rejim B 2 saat = 14 saat, TUTARLI) · takvim tarladan (9,5 hafta) ·
     bilinçli sıkıştırma beyanlı. Kış yok.
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ · üretim günlüğü açıldı ⛔ BOŞ
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı)
   ⚠️ Plan bu ölçümden sonra DÜZELTİLMEDİ — üç cümle (S5 göbek · SITE "only turbine" · S2–S5 kaldırma
     yolu) yeniden üretimden önce plana yazılır; kart A adım 8 yeniden koşulur.
   → dikey_shorts/THE_EMPTY_RIDGE/

OVER THE WALL — DOKUZUNCU ÜRETİLEN FİLM · İLK BARAJ · 14.09.2026
   plan 8 × 8,0 = 64,0 + kapak 5,0 (14.09 · ⛔ DÜZ · proje sahibi kilidi) · zincirli · 9 kare + 8 I2V
   ÜRETİLDİ ✅ (günlüksüz ⛔) · 12/12 mercek koşuldu ✅ · 11'i RUN INCOMPLETE ⛔ · kapak kartı VAR
   ⛔ Kurgu 7 klip, hiçbir plan sürümüne oturmuyor; kesme_kontrol.sh koşulamadı (teslim.mp4 depoda yok)
   ⛔ Zincir hükümleri düştü: ⑤ REBUILT 6/6 · ⑧ APPEARED 0/4 · ② APPEARING (8.) · ⑦ PARKED · ⑩ MAGIC
   ⭐ GEÇEN: ⑥ TIME · RHYTHM (varyanslı kurgu) · 12/12 END CARD SAME · ① CAMERA LOCK 9 · ③ CARRIER 10
   → KARAR: yayınlanmaz · yeniden ÜRETİLMEZ — önce ARAÇ KAPISI + GÜNLÜK + ZİNCİR.
     Yeniden üretilecek: S2 (kuru katlı platform) · S3 BÜYÜR (filmde yok) · S4–S5 (döşekte makine) ·
     tek istasyon · dar yüzeyde tek araç. Dersler 51-54 · RAPORLAR/OVER_THE_WALL.md §9
   ⚠️ IZGARA: ⑥ varyanslı kurguda RHYTHM dedi (CROSSING'den sonra 2. kez) — 8 × 8,0 düz kilit
     proje sahibine geri soruldu; plan DEĞİŞTİRİLMEDİ.

BEFORE NIGHTFALL — YEDİNCİ FİLM · ⛔ HENÜZ ÜRETİLMEDİ
   ızgara 6 × 8,0 = 48,0 sn + kapak 5,0 · ⛔ DÜZ IZGARA (proje sahibi kilidi)
   ⭐ İLK KARA DELİK SAHASI · havasız kayaç ova · saha kartı YOK
   ⭐ FORMATI İLK KOŞAN FİLM: İKİ KEYFRAME ZİNCİRİ — 7 görsel · 6 klip · her
     klip iki onaylı kareye kilitli; dikişin iki yakası AYNI KARE.
     08.09.2026'da bu yöntem DEPONUN FORMATI oldu [KILAVUZ_REHBERI §2.7];
     bu film onun ilk uygulamasıdır. Kesme artık zaman sıçraması değil:
     film TEK GÜNDÜR (12,0 yerel saat).
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ · üretim günlüğü ⛔ AÇILMADI (üretim günü açılır)
   ⛔ KAPI: BLOCK ×1 (süre eşitliği — BİLİNÇLİ, plan §1.2) + FIX ×8
     (7'si prompt_kontrol §9 ↔ DERS 35 çelişkisi · 1'i ölçülmemiş kutu seti)
   ⛔ ÜRETİM AÇILMAZ: araç kapısı yedi ölçümü koşulmadı [ARAC_KARTLARI §4].
     İlk ölçüm bu filmde VAR/YOK sorusudur — kutu seti {4,6,8} çıkarsa 8,0 sn
     tek klipte teslim edilemez (tavan 7,00 sn) ve ızgara yeniden açılır.
     ⭐ SEKİZİNCİ SORU ARTIK KILAVUZDA [ARAC_KARTLARI §4 ölçüm 8]: araç İKİ
     KAREYLE (ilk+son) çalışıyor mu? Çalışmıyorsa bu FORMAT o araçta
     üretilmez — plan düşürülmez, araç değişir.
   ⭐ BU FİLM ÜÇ ÖLÇÜLMEMİŞ ŞEYİ İLK KEZ SINAR: DERS 36'nın oran kapısı
     (tam hâl/ara hâl < 1) · zincirin GEOMETRİ kanalı [A3-d] · DERS 44'ün
     tersi (kusursuz dikişte düz ızgara ⑥'yı düşürür mü).
   → dikey_shorts/BEFORE_NIGHTFALL/ · ölçüm yok, satır yok: mercek tablolarına
     film ÜRETİLMEDEN satır yazılmaz [kart Q ön koşulu].

THE LONG DAY
   ızgara 10 sahne · plan 6·4·6·4·6·6·8·4·6·10 · ⛔ KURGU 10 × 6,0 DÜZ kesildi
   ⭐ İLK UZAY SAHASI · İLK SEKİZ MERCEKLİ ÖLÇÜM · kapı üretimden ÖNCE ✅ GO
   ÜRETİLDİ ✅ · 8/8 mercek koşuldu ✅ · ⛔ SEKİZİ DE RUN INCOMPLETE (karesiz/belgesiz)
   ⛔ ÜRETİM GÜNLÜĞÜ YOK — plan ile film ayrıştı (astronot · güneş kadrajda ·
     dikey habitat · ikiz kule) ve sebebi kayıtta değil [DERS 28]
   ⭐ GEÇEN: ① TIMELAPSE (kamera·kadraj·çapa·istasyon 10/10) · ⑤ SAME WORLD +
     kanıt nesnesi BULUNDU (kaya + krater) · ④ ONE THING ilk kez bulundu ·
     ③ SEASON CARRIER 10 mevsimsiz sahada · ⑥ TIME
   ⛔ DÜŞEN: ② DIFFERENT·APPEARING (5.) · ③ NOT IN ONE DIRECTION (güneş
     kadrajda, gölge donuk) · ⑥ METRONOM (4.) · ⑦ PARKED · ⑧ APPEARED 1/9 ·
     ① PEOPLE 0 · SURFACE 0 · beş mercekte END CARD DIFFERENT
   → KARAR: yayınlanmaz · yeniden üretilmez · Dersler 28-34 ·
     RAPORLAR/THE_LONG_DAY.md §5

THE MOUNTAIN DOOR
   ızgara 5 × 6,0 (DÜZ — proje sahibi kilidi) · depo İÇİNDE yazıldı, GPT yok
   ⭐ KAPI ÜRETİMDEN ÖNCE KOŞULDU: ✅ GO — deponun dört filminde İLK KEZ
   ÜRETİLDİ ✅ · 6/6 mercek koşuldu ✅ · kapak kartı VAR
   ⛔ ALTI HÜKMÜN ALTISI DA DÜŞTÜ:
        ① SIX SEPARATE SHOTS   ② DIFFERENT · APPEARING (4. kez)
        ③ PASSES BUT NOT IN ONE DIRECTION
        ④ ENDS · NONE FOUND (4. kez)
        ⑤ A SET REBUILT EACH TIME · kanıt NONE FOUND
        ⑥ NEXT · METRONOM (3. kez)
   ⭐ GEÇEN: ③ SEASON CARRIER 10/10 · VEGETATION 10/10 · SHADOW/SUN 8/10 ·
     zaman tahmini "9-12 ay" — plan 12 ay, İKİNCİ KEZ TUTTU.
   ⛔ KÖK SEBEP DEĞİŞTİ — artık prompt mimarisi DEĞİL, ÜRETİM AKIŞI:
     ① CAMERA LOCK 0/10 · beş klipte de push-in. Ölçülebilir çapa cümlesi
     beş I2V'de de VARDI; NARROW LOT'ta aynı cümle 10/10 almıştı → araç
     ön ayarı [DERS 23]. Zincir tutmadı: 4/4 dikişte kusur, plana kasten
     konan kanıt nesnesi İLK dikişte kayboldu [DERS 25].
   ⛔ ÖLÇÜLEN HİPOTEZ DÜŞTÜ: klip içi vuruş varyansı metronomu kırmadı —
     ⑥ RHYTHM 0/10, deponun en düşüğü [DERS 24].
   ⛔ DERS 17 İKİNCİ KEZ: SPEC üretimden ÖNCE hazırdı ve mercekler yine
     belgesiz koştu (6'nın 5'i eksik girdi). Eksik olan belge değil,
     koşu YORDAMI [DERS 27].
   → KARAR: yayınlanmaz. Yeniden ÜRETİLMEZ — önce ARAÇ KAPISI ve ZİNCİR.
     Dersler 23-27 · RAPORLAR/THE_MOUNTAIN_DOOR.md §8

THE NARROW LOT
   ızgara 5 × 6,0 · MOTOR_5_SAHNE'nin ilk koşusu · harici GPT
   promptlar ✅ · ⛔ KAPI KOŞULMADI (üretimden sonra koşuldu: 25 madde BLOCK)
   ÜRETİLDİ ✅ · 6/6 mercek koşuldu ✅ · kapak kartı ÜRETİLMEDİ
   ⭐ DÖRT HÜKÜM İLK KEZ GEÇTİ: ① TIMELAPSE · ③ PASSES · ⑤ SAME WORLD · ⑥ TIME
     ⑤ "THE OBJECT THAT PROVES IT IS THE SAME PLACE: coiled hose" — bu satır
     iki filmde de NONE FOUND'du ve deponun en ağır satırıydı.
     ③ zaman tahmini "about one year" — plan ~12 ay. İlk kez TUTTU.
   ⛔ KÖK SEBEP DEĞİŞTİ: artık üretim sırası değil, PROMPT MİMARİSİ.
     Hareketle ilgili her kural GÖRSEL promptta kaldı, I2V'ye hiç girmedi:
     TIME RATE 5/5 görselde · 0/5 I2V'de → ③ TIME RATE · CLOUD · SUN = 0/10.
     Ve YAPI BIBLE sayısız yazıldı ("regular structural bays", oturum yok)
     → ② STRUCTURE IDENTITY 2/10. Aynı filmde SAYILI çapa bloğu 10/10 aldı.
   ⚠️ ⑥ METRONOM: kesmeler 6,0 · 6,0 · 6,0 · 6,0. Brief bunu ÖNCEDEN
     uyarmıştı; ritim varyantı artık varsayılan.
   → KARAR: yayınlanmaz. Yeniden ÜRETİLMEZ, yeniden YAZILIR.
     Dersler 18-22 · RAPORLAR/THE_NARROW_LOT.md §11

THE CLOSING SPAN
   promptlar ✅ · kapı GO ✅ · ÜRETİLDİ ✅ · 6/6 mercek koşuldu ✅
   ⛔ ALTI HÜKMÜN BEŞİ DÜŞTÜ:
        ① AYRI AYRI GÖRÜNTÜLER   ② FARKLI · APPEARING
        ③ YANLIŞ YÖNDE GEÇİYOR   ⑤ HER ÇEKİMDE YENİDEN KURULMUŞ · NONE FOUND
        ⑥ SIRADAKİ · METRONOM    ④ BİTİYOR (tek geçen) ama NONE FOUND
   ⭐ TEK BÜYÜK KAZANIM: ① CAMERA LOCK 10/10 (v1'de 4/10) — DERS 6 tuttu.
   ⛔ KÖK SEBEP YİNE AYNI: ters inşa zinciri koşulmadı → 8 ayrı vantaj,
     9/9 dikiş DEFECT. DERS 5 yazılıydı ve KAPI ilan edilmişti; yazılı
     kural kapı değildir [DERS 12].
   ⚠️ ② ④ ⑥ BELGESİZ koşuldu (mod V) — sözleşme sorusu hiç sorulmadı [DERS 17].

THE LONG SHADOW v1
   promptlar yazıldı ✅ · prompt kapısı GO ✅ · ÜRETİLDİ ✅ · 4/4 mercek koşuldu ✅
   ⛔ DÖRT HÜKMÜN DÖRDÜ DE DÜŞTÜ:
        ① ALTI AYRI GÖRÜNTÜ   ② FARKLI · APPEARING
        ③ GEÇİYOR (yön kırık)  ④ DURUYOR · NONE FOUND
   → KARAR: v1 YAYINLANMAZ. Yeniden planlanıp yeniden üretilir.
     Sebepler ve dersler: RAPORLAR/THE_LONG_SHADOW.md · DERSLER 3-9
   ⭐ ÖLÇÜMÜN DEĞERİ: dört mercek de dokümansız (mod V) koştu ve
     dördü de birbirinden bağımsız olarak AYNI kök sebebe işaret etti —
     ters inşa üretim sırası koşulmadı. Varsayım ölçüme dönüştü [DERS 5].
```

## KURAL

```
· Bir film ÜRETİLMEDEN hiçbir mercek koşulmaz. Rubrik promptu değil VİDEOYU
  eleştirir; plana koşulan bir rubrik prompt kapısının işini tekrar eder.
· ③ ve ④ TAM KURGU ister. Tek klibe koşulmuş bir ③ raporu GEÇERSİZDİR.
· ① · ③ · ⑤'e doküman VERİLMEZ (QA/00_README §1).
· ⑥ SESLİ kurgu ister — ölçü hizasını sessiz bir dosyada denetleyemez.
· ASGARİ SET: ① + ② + ⑤. Bu üçü koşulmadan film yayınlanmaz.
· VERDICT satırı skor ortalamasından bağımsızdır ve çeliştiğinde KAZANIR.
```
