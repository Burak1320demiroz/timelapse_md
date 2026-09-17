# 💧 THE HIDDEN OASIS — Dikey Timelapse Planı

Dikey Timelapse Production Document
Format: **9:16 (DİKEY)** | Sahne: **7 × 8,0 sn = 56,0 sn** | Kapak kartı: **5,0 sn** | Toplam: **61,0 sn**
Prompt yapısı: ⭐ **7 sahne → 8 görsel (G0…G7) + 7 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7]
Yapı: **terk edilmiş yüzme havuzu → taş kenarlı bahçe göleti** (yeni tip · `YAPI_TIPI_KARTLARI` §10 şablonu, §DEĞİŞMEZLER'de sayıyla) · Saha: **duvarlı avlu, Akdeniz** (yeni kart · `SAHA_VE_IKLIM` §3.1 şehir içi varyantı)
Zaman yayı: **bir iş günü mertebesi** (06:20 → 18:30) → 56 saniye · film *"bir gün"* okutur; gerçek iş dört gün mertebesindedir ve bu BİLİNÇLİ SIKIŞTIRMADIR [P1-c · §2.7 ①]
Kamera mimarisi: **MAIN STATION** — tek istasyon, 7 sahne + usta kare (detay istasyonu YOK) [P2-e · DERS 52]
Izgara: ⛔ **DÜZ — 7 × 8,0** · proje sahibinin kilidi (16.09.2026) · gerekçe ve kabul edilen risk §AŞAMA MERDİVENİ'nde
Havuz kaydı: `apexait/YAYIN_PLANI.md` §5 · siluet ailesi **ZEMİN** (yeni aile — DİKEY ve YATAY'dan sonra üçüncü tür; §3)

_"Yıllardır kimsenin dokunmadığı bir havuz, bir günde havuz olmaktan çıkar."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     7 sahne × 8,0 sn                        = 56,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn                        =  5,0 sn   ← SAHNE DEĞİL, ayrı denetlenir
               ⛔ KONUM: teslimin SON 5 saniyesi (56,0–61,0) [A1-b]
──────────────────────────────────────────────────────────────
TOPLAM                                                   61,0 sn
```

⛔ Kapak kartı **usta kareden (G7)** türetilir ve üstüne **İngilizce başlık** dizilir: `THE HIDDEN OASIS` (`THE_HIDDEN_OASIS_KAPAK.md`).
⚠️ **AJAN KARARI — proje sahibinin onayına açık (16.09.2026):** dış plan 56,0 sn ve kartsızdı. Depo formatı kartı ZORUNLU tutar
[§2.1 · DERS 4] ve `prompt_kontrol.py` kartsız planı BLOCK eder. Kart eklendi, süre 61,0 sn oldu. Sahip kartsızlığı isterse tek
satırlık beyan yeter — ama o zaman TESLİM YAPISI bloğu "KAPAK KARTI YOK, gerekçe: …" diye yazılır, boş bırakılmaz.
⚠️ **Kapanış süresi dürüst beyan:** S6'nın son 2,0 sn tutuşu + 5,0 sn kart = **7,0 sn (%11)** sonuç ekranı. Tutunma riski
KABUL EDİLDİ ve ölçülecek (A1-a).
⚠️ **Döngü iddiası YOK:** G7 → G0'da havuz geri gelmez ve akşam sabaha döner. Aynı kadraj bir **açılış–kapanış kafiyesidir**;
paketlemede "perfect loop" denmez.
⚠️ **Metin yalnız KURGUDA:** "CAN THIS BE SAVED?" / "BURASI KURTULUR MU?" kancası ve kapak yazısı **post prodüksiyondur**.
Negatif çekirdek her karede okunabilir metni yasaklar; promptlara hiçbir yazı girmez [D-b · DERS 33].

---

## 🚪 KONSEPT KAPISI

```
VAAT     Duvarlı bir avluda yıllardır boşaltılmamış, yosun tutmuş bir yüzme havuzu bir gün içinde boşaltılır,
         temizlenir, kaplanır, taşla çevrilir, dikilir, doldurulur ve akşam ilk kez ışıkları yanar.
DİRENÇ   ① TEK KAPI — avlunun sol duvarındaki kapı tek giriş çıkıştır: her kova, her taş, her saksı ve her
            atık O KAPIDAN geçer; hat kalabalıklaşınca iş durur [DARK ROCK'ın "tek iniş rampası" düğümü]
         ② ESKİ KABUK — çatlamış seramik ve kaygan siyah dip: astar serilmeden önce yüzey temiz ve kuru olmalı;
            ıslak kalan her bölge sonraki işi bekletir
         ③ SU — dolum en sonda ve TEK YÖNDE olur; seviye bir kez yükseldi mi taş, bitki ve kablo işi biter
         EKRANDA NASIL [P1-b]:
           S0 · pompa çalışır, yeşil yüzey iner, duvardaki yosun bandı sırayla açığa çıkar
           S1 son 2 sn · temiz/kirli sınırı dibi süpürür, merdiven kapıdan çıkar
           S2 · ⭐ BEDEL ANI: astar açılır, mavi seramik kare kare kaybolur
           S5 son 2 sn · hortum çıkar, yüzey durulur — su AYNAYA döner
BEDEL    HAVUZUN HAVUZ OLMASI. G0'da açık mavi seramik, paslı merdiven ve içine girilen hacim vardır;
         G3'te seramik astarın altında kalır, merdiven çoktan gitmiştir, G7'de havuz bir göletdir.
         Kadrajda: aynı dikdörtgen sınır, içi başka bir şey. Okuma bilinçli: "bozuldu" değil,
         "yüzülen yer → bakılan yer".

KANAL TEZİ KAPISI [KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            havuzun kendisi — mavi seramik, merdiven, yüzülebilir hacim          ✅
  □ kadrajda görünüyor mu?    evet — G0 seramik + merdiven, G3 astar, G7 taş + su · sabit kamera   ✅
  □ cevap "zaman geçiyor" mu? hayır                                                                ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ Donmuş karede: taş kenarlı siyah çanak, sol üstte yaşlı zeytin, arka duvarda kemerli niş,
                           kenarda açık dikim cepleri → "eski havuz gölete çevriliyor, şu kadar kaldı" bir saniyede.
② KİNETİK BAĞIMSIZLIK   ✅ Sabit kadrajda su iner, temiz/kirli sınırı süpürür, astar açılır, taş halkası kapanır,
                           su yükselir, ışık yanar — metinsiz, anlatıcısız.
③ BAŞLIK ŞEMASI         ✅ Kapak: "THE HIDDEN OASIS" (3 kelime) · Başlık: "A Pool Nobody Had Touched in Years"
④ OMURGA CÜMLESİ        water drawn down → basin scraped clean → tile buried under liner → stone rim closes
   [P1-k]               → pockets planted → water climbs the third stone → six lights come on
                        (7 vuruş, her biri ≤6 kelime; merdiven bundan türedi)
```

### ⭐ KİNETİK PAKET — THE DARK ROCK'tan devralınan dokuz araç (16.09.2026, proje sahibinin isteği)

```
⛔ ÖNCE DÜZELTME: THE DARK ROCK'ta KAMERA HAREKETİ YOKTUR. Yedi görselin yedisinde de kamera satırı
   "The camera never moves", altı I2V'nin altısında "absolutely zero movement, no shake, no drift, no zoom,
   no pan, no tilt" yazar. Beğenilen şey kameranın hareketi değil, SABİT KADRAJIN İÇİNDEKİ HAREKETTİR.
   Depo kamera hareketini üç kez ölçtü ve üçünde de film düştü: ① SIX SEPARATE SHOTS (dört istasyon +
   push-in) · ① CAMERA LOCK 0/10 (beş klipte push-in) · DERS 52 (istasyon değişen kesmede yapı sıçradı).
   Bu yüzden istenen şey ARAÇ ARAÇ devralınır, kamera kilidi açılmaz.

① KENAR GEÇİŞİ      DARK ROCK: çıkarma gemisi her sahnede SOL KENARDAN girer ve çıkar.
                     BURADA: sol duvardaki KAPI. Her sahnede bir şey o kapıdan geçer — hortum (S0),
                     kova ve merdiven (S1), astar rulosu (S2), taş (S3), saksı (S4), dolum hortumu (S4 sonu),
                     el arabası (S5 sonu). Kadrajı kat eden yatay hareket buradan gelir.
② DİKEY SÜPÜRME     DARK ROCK: sarı kabin direkte iner-çıkar (dikey kadrajın ekseni).
                     BURADA: SU SEVİYESİ — S0'da iner, S5'te çıkar. Dikey formatın ekseni suyun kendisidir.
③ GÖLGE SÜPÜRMESİ   DARK ROCK: gölge sabah aprona düşer, öğlen kısalır, akşam denize döner.
                     BURADA: doğu duvarının gölgesi G0'da bütün avluyu örter, gün boyunca çekilir,
                     akşam batı duvarının gölgesi avluyu yeniden kapatır. Filmin zaman taşıyıcısı budur.
④ GÖK OLAYI         DARK ROCK: alçak bulut tavanı soldan girer, deniz kararır.
                     BURADA: gök kadrajda YOK — yerine BULUT GÖLGESİ. S3'ün ilk 2 saniyesinde bir bulut
                     gölgesi avluyu soldan sağa geçer ve kadrajdan çıkar. Sabit kadrajda "kamera kaydı"
                     hissine en yakın meşru araç budur.
⑤ ÜÇ VURUŞ          DARK ROCK: her klip "First … Then … Finally" (2 sn · 4 sn · 2 sn).
                     BURADA: birebir aynı; sahne tablosunda üç sütun hâlinde yazılı.
⑥ ÖDÜLÜN GECİKMESİ  DARK ROCK: fener ancak SON klibin son çeyreğinde yanar, sonra 2 sn tutuş.
                     BURADA: altı bahçe feneri ancak S6'nın orta bölümünde yanar, sonra 2 sn tutuş.
                     ⛔ Daha önceki hiçbir promptta "lights / alight / glow" fiili geçmez [DERS 56].
⑦ YÜZEY SINIRI      DARK ROCK: ıslak koyu bant yukarıdan aşağı kurur.
                     BURADA: temiz/kirli sınırı (S1) ve ıslak/kuru sınırı (S1 sonu → G2) dibi süpürür.
⑧ İZ BIRAKAN ARAÇ   DARK ROCK: yükleyicinin paletleri taş tozunda çizgi bırakır.
                     BURADA: el arabasının lastikleri avlu tozunda çizgi bırakır; izler S3–S5'te birikir,
                     S5'te süpürülür, G7'de zemin temizdir.
⑨ EKİP LEKESİ       DARK ROCK: "Crew register only as faint soft motion streaks, never as sharp figures."
                     BURADA: birebir aynı cümle, rejim B (2 saat / 8 sn). İnsan silinmez, İZ olarak vardır.
+  ONUNCU ARAÇ — YANSIMA (bu filme özel): su dolduktan sonra yüzey duvarı, nişi ve zeytini TAŞIR.
   Gök kadrajda olmadığı için filmin tek gökyüzü SUYUN İÇİNDEDİR. Final ödülü de oradan okunur.
```

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera  ② KEMERLİ NİŞ — arka duvarda, sağ merkezde, ≈99 × 134 px, sekiz karede birebir
                          ③ ZEYTİN GÖVDESİ — solda, x %9,2, taban %38,3, taç %82,2
                          ④ duvar harpuşta çizgisi %78,7, kesintisiz düz · arkasında teras yamacı
                          ⑤ HAVUZUN SINIRI — yuvarlatılmış köşeli dikdörtgen; yakın kenar %12,9, uzak kenar %51,8;
                             sekiz karede AYNI, yalnız içi ve kenar dokusu değişir (bedelin kanıtı budur)
                          ⑥ TEK KAPI: sol duvarda, x %14,9 · her malzeme oradan girer, her atık oradan çıkar
                          ⑦ ayrı insan figürü yok (streak cümlesi) · ⑧ tek ölçek çapası: KEMERLİ NİŞ
P1.5 · fırsat buldukça   gölgenin avluyu süpürmesi · el arabası izleri · eksilen taş istifi · eksilen saksı sayısı ·
                          ıslak/kuru sınırı · yansımanın büyümesi
SPEC · yalnız belge      havuz 5,0 × 3,0 m · derinlik 1,0 → 1,4 m · duvar 2,6 m · niş 0,9 × 1,1 m · zeytin 4,4 m ·
                          kamera +6,0 m · D_eksen 5,0 m · tilt −40° · 37°K eylül ortası güneş dereceleri
```

**Malzeme kimliği (her promptta):** *weathered limestone flagstones · dry-stone wall under worn lime plaster · glazed pale blue pool tile · dry matte black rubber liner · rough dolomite boulders, warm grey with orange lichen · washed river gravel · dark bark mulch · matt-black low garden lamps with warm bulbs* — "garden pond" korpusu parlak koi göleti ve peyzaj render'ı çeker; bizimki AVLU İŞİDİR ve bu POZİTİF yazılır (taş, sıva, toz, kireç), negatifte render adı anılmaz [DERS 42 · DERS 33].

**İnsan kararı:** insansız saha DEĞİL. Ekip streak cümlesiyle (§9.4) + rejim B. `"No people are present"` yalnız G7'de yazılır — orada avlu gerçekten boştur ve o kare hiçbir streak cümlesi taşımaz [DERS 33 · kapı §10].

**Vinç kararı [DERS 8 · 22 · 46 · 57]:** ⛔ **FİLMDE VİNÇ YOK.** Uzun rijit yük hiçbir karede havada taşınmaz: astar rulosu dört streak tarafından BEL HİZASINDA taşınır, kayalar el arabasıyla gelir, hiçbir şey askıda değildir. Prompt metninde "crane" kelimesi hiç geçmez (kapı §12b).

**Lamba kararı [DERS 56]:** S0–S5'te lambalar TAKILIDIR ama SÖNÜKTÜR ve promptta yalnız "their heads dark" diye geçer. Işık yalnız S6'nın orta bölümünde belirir ve SABİT kalır. "turn on / switch / rotate" fiilleri yazılmaz; yazılan fiil *"come alight one after another"* ve *"hold steady"*dir.

**Çoğalma kararı [DERS 55]:** "swimming pool", "garden pond" ve "olive tree" korpusları çoğuldur (havuz dizileri, zeytinlikler). SITE / BACKGROUND ve her I2V: *"one rectangular pool"* · *"the only tree inside the walls"* · *"one arched niche"* · I2V kilidi: *"This is one pool in one walled courtyard and the only one in view."* Günlükte havuz = 1, ağaç = 1, niş = 1, lamba = 6 sayımı.

**Su korpusu kararı [DERS 54 — tersi]:** THE DARK ROCK'ta risk "kuru kaide ıslak okunur"du; burada risk **"kuru astar dolu okunur"**. G3–G5'te astar her promptta *"dry and matte and absorbs the light"* / *"no sheen"* yazılır; ıslaklık ancak S5'te gelir. Bu üç karede yüzeyde YANSIMA YOKTUR — yansıma filmin ödülüdür, erken verilmez.

---

## 🔒 DEĞİŞMEZLER TABLOSU

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz.
                 ⭐ Düz ızgaranın araç şartı: her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0, yani en büyük
                 kutu ≥ 9,0 sn (üret 9,0 → baştan 1,0 kırp [A7-b]; {5,10} kutusunda üret 10,0 → baştan 2,0 kırp).
                 Kutu seti {4,6,8} çıkarsa tavan 7,0 < 8,0: o araçta bir sahne tek 8,0 sn klip olamaz →
                 ARAÇ değişir ya da karar proje sahibine döner. ⛔ ARA KARE YOK: plan ara kareye BÖLÜNMEZ.
```

```
┌─ KAMERA İSTASYONU (ANA · tek istasyon) ─────────────────────────────────────┐
│ konum         avlunun güney kenarındaki evin birinci kat balkon korkuluğu    │
│ objektif      24 mm · f/8 · ISO 100 · tam kare · DİKEY 9:16 (1080 × 1920)    │
│ yükseklik     h = +6,0 m (avlu döşemesinden)                                 │
│ mesafe        D_eksen = 5,0 m (havuzun merkezi) · D_kenar = 1,40 m (kadrajın │
│               alt kenarının zemine değdiği yer) [DERS 38 — iki mesafe]       │
│ bakış açısı   0° (kuzey) · tilt −40° (AŞAĞI) · roll 0°                       │
│ ⛔ TILT SIFIR DEĞİL — §3 FORMÜLÜ GEÇMEZ. Ufuk kadrajın ÜSTÜNDE kalır ve       │
│    kadraja hiç girmez; yüzdeler ZEMİN DERİNLİĞİNDEN hesaplanır:              │
│      yüzde(d) = (76,87° − atan(6,0 / d)) / 73,74°   · d = kameradan yatay m   │
│      (üst kenar 3,13° · alt kenar 76,87° · dikey görüş açısı 73,74°)          │
│    KAMERA_ISTASYONU'na yeni bir alt kart borcu doğdu: "AVLU / AŞAĞI BAKIŞ"   │
│    — ölçülmeden kılavuza yazılmaz, bu plan onun ilk koşusudur.               │
│ ⛔ YÜZDELER (kadrajın ALT kenarından):                                        │
│    zemin alt kenar (1,40 m) %0 · havuz yakın kenarı (2,5 m) %12,9            │
│    havuz ekseni (5,0 m) %36,1 · zeytin gövde dibi (5,5 m) %38,3              │
│    havuz uzak kenarı (7,5 m) %51,8 · duvar dibi (10,0 m) %62,2               │
│    niş eşiği %67,6 · niş kemer tepesi %74,6 · DUVAR TACI (2,6 m) %78,7       │
│    zeytin taç ucu (4,4 m boy, 5,5 m) %82,2 · üst 1/8 (%87,5) = 22,4 m'deki   │
│    teras yamacı — hiç değişmez                                               │
│ ⛔ x (kadraj genişliği · yarı genişlik = 0,4219 · √(d² + 36)):                │
│    havuz ekseninde kadraj eni 6,59 m → havuz (3,0 m) kadrajın %45,5'i        │
│    havuz sol kenarı %27,3 · sağ kenarı %72,7 · zeytin gövdesi %9,2           │
│    KAPI (sol duvar, d ≈ 9 m) %14,9 · NİŞ %57,6–66,8 · çağlayan (d=10) %65,2  │
│ ⛔ PİKSEL (1080 × 1920): NİŞ ≈ 99 × 134 px (en = kadraj eninin ONDA BİRİ +    │
│    biraz; prompta "one eleventh" olarak girer) · havuz uzak kenarı y ≈ 995 px│
│    (alttan) · duvar tacı y ≈ 1511 px (alttan)                                │
│ ⛔ SHORTS UI: alt %0–13 (avlu ön döşemesi, boş) ve sağ %87,5+ ilerleme        │
│    KANITI TAŞIMAZ; havuzun sağ kenarı %72,7'de kalır [MUZIK_VE_KAPAK §2.4]   │
│ ⛔ ÖN GÖRSELLEŞTİRME (zorunlu adım, usta kareden ÖNCE): plan + yan kesit —    │
│    balkon · avlu · havuz · arka duvar + niş · zeytin · teras yamacı;         │
│    G7 onaylanınca yüzdeler ve pikseller ÖLÇÜLÜR, buraya ve QA_SPEC §2'ye     │
│    yazılır. Buradaki sayılar TÜRETİLMİŞTİR, ölçülmemiştir.                   │
│ güneş         tek ışık günü, 37°K, eylül ortası geometrisi (δ +3°):          │
│               06:20 az 91° → 18:30 az 277°; kadraj yatayda az 337°–23° →      │
│               disk hiçbir karede kadrajda değil [DERS 32 · 39]               │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — 3 kalıcı + 1 üretilen [SAHA 3.3: en az üç] ────────────┐
│ ① KEMERLİ NİŞ  arka duvarda, sağ merkezde · x %57,6–66,8 · y %67,6–74,6 ·    │
│    ≈99 × 134 px · ⭐ ⑤ merceğinin "AYNI YER" NESNESİ — zincir_kontrol.sh'in   │
│    her koşusunda iki karede de aynı yerde, aynı boyda mı — ELLE ✓/✗ [DERS 25]│
│    ⛔ EN PİKSELİ SEKİZ KAREDE AYNI; sağ UI bandına (x > %87,5) girmez         │
│ ② ZEYTİN GÖVDESİ  solda · x %9,2 · gövde dibi %38,3 · taç ucu %82,2 ·        │
│    ⛔ S4'te BUDANIR: taç HACMİ değişir, GÖVDE ve ilk çatal DEĞİŞMEZ —         │
│    çapa gövdedir, taç değil (budama G5'ten sonra sabittir)                   │
│ ③ DUVAR HARPUŞTA ÇİZGİSİ  %78,7 · kadrajı kesintisiz kat eder · ⭐ ufuk       │
│    olmadığı için filmin tek düz yatay çizgisi budur, en güçlü çapa           │
│ ④ HAVUZUN SINIRI  yuvarlatılmış dikdörtgen · yakın kenar %12,9 · uzak kenar  │
│    %51,8 · sekiz karede AYNI — içi seramik → siyah astar → taş kenarlı su    │
│ + TERAS YAMACI  %78,7–100 arası, 17,6 m'den öteye · kuru ot ve zeytin sırası │
│ ⛔ Piksel değerleri usta kare onaylanınca ÖLÇÜLÜR [PERSPEKTIF §1 · §4]        │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ────────────────────────────────────────────────────────────┐
│ ufuk           ⛔ KADRAJDA YOK (tilt −40°) — göz çizgisi kadrajın üstünde      │
│                kalır. Yatay kilit DUVAR TACIDIR (%78,7).                     │
│ gök            ⛔ KADRAJDA YOK. Filmin tek gökyüzü SUYUN YANSIMASIDIR (S5'ten │
│                sonra). Bulut, GÖLGE olarak girer (S3 ilk 2 sn).              │
│ avlu zemini    %0–12,9 (ön) ve %52–62 (havuzla duvar arası)                  │
│ havuz          %12,9–51,8 · kadraj eninin %45,5'i · filmin merkezi           │
│ duvar          %62,2–78,7 · niş %67,6–74,6                                   │
│ teras yamacı   %78,7–100 · üst 1/8 hep yamaç — hiç değişmez                  │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — tamamlanmış hâlin sabit geometrisi (SAYIYLA · DERS 19) ────────┐
│ tip            taş kenarlı bahçe göleti · eski yüzme havuzunun sınırında     │
│ havuz kabuğu   5,0 × 3,0 m · yuvarlatılmış köşe · derinlik 1,0 → 1,4 m ·     │
│                açık mavi sırlı seramik · sığ uçta banyo basamağı             │
│ merdiven       paslanmaz, üç basamak, yakın sol köşe · S1'de SÖKÜLÜR         │
│ astar          gri koruyucu keçe + tek parça siyah kauçuk astar (EPDM) ·     │
│                kuru ve mat · kenar harpuştanın üstüne kıvrılır               │
│ taş kenar      kaba dolomit bloklar, 25–45 cm · tek sıra · harç yastığı      │
│ çağlayan       üç kademe · 0,35 m toplam düşü · sağ arka köşede taş sekide   │
│ çakıl sahanlık sığ uçta · yıkanmış dere çakılı                               │
│ dikim cepleri  8 adet · uzak kenarda bloklar arasında · koyu malç bandı      │
│ aydınlatma     6 mat siyah bahçe feneri · 0,5 m · sıcak ampul · sağ patika   │
│ filtre         nişin dibinde kutu + düz kapak taşı · boru taş kenarın altında│
│ duvar          2,6 m · kuru taş + yıpranmış kireç sıva · düz taş harpuşta    │
│ niş            0,9 m en × 1,1 m yükseklik · eşik 0,9 m · kemer tepesi 2,0 m  │
│ zeytin         tek yaşlı zeytin · gövde 0,6 m çap · 4,4 m boy · solda        │
│ kapı           sol duvarda, arka köşeye yakın · tek giriş çıkış              │
│ ⭐ SAYI TESTİ [P2-b]: prompta giren → "one rectangular pool" · "the only tree"│
│    · "one arched niche" · "about 99 pixels" · "one eleventh" · "three steps" │
│    · "eight pockets" · "six lamps" · "the third boulder" · yüzdeler          │
│    (13 · 52 · 58 · 67 · 68 · 75 · 79)                                        │
│    SPEC'te kalan → 5,0 × 3,0 m · 1,0/1,4 m · 2,6 m · 0,9 × 1,1 m · 4,4 m ·   │
│    +6,0 m · 5,0 m · 0,35 m · 37°K güneş dereceleri                           │
│ ⛔ Promptta STRUCTURE tek cümledir [DERS 36]; sayılar QA_SPEC §3'tedir.       │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 7 satır

Her satır bir ELEMAN + ARA HÂL taşır [A5-a]; tek fiil, ardışık satırda tekrar yok [P1-f]; REJİM iki tanedir (B · 2 saat ×6, A · 10 dakika ×1) ve bu §2.2'nin "en fazla iki rejim" sınırındadır [A6-a].
G(n) = klip n'in İLK karesi (o sahnenin görsel promptu) · klip = G(n) → G(n+1) · her sahne TEK 8,0 sn klip, ara kare YOK.
İlk 2 sn · orta 4 sn · son 2 sn dağılımı THE DARK ROCK'tan devralındı [KİNETİK PAKET ⑤].

| S | SÜRE | FİİL | EKRANDA VAR OLAN (G(n)) | YENİ OLAN (klipte) | ELEMAN · ARA HÂL | TEMSİL | MEVSİM TAŞIYICISI | KANIT NESNESİ | REJİM | İSTASYON |
|:-:|---:|---|---|---|---|---|---|---|:-:|:-:|
| 0 | 8,0 | **ÇEKİLİR** | koyu yeşil suyla dolu eski havuz · yaprak salı · seramikte kuru yosun bandı · paslanmaz merdiven · dipteki dalgıç pompa, hortum kapıya · el arabası + kürek + kova | ilk 2 sn: pompa basar, yüzey iner, seramikte ıslak koyu halka açılır · orta 4 sn: seviye sıra sıra iner, yapraklar dibe çöker, merdivenin ayakları ve banyo basamağı çıkar, doğu duvarının gölgesi çekilir ve dip ilk kez ışık alır · son 2 sn: son su derin uçta siyah birikinti, kapıdan ikinci araba girer, kürekler rıhtıma bırakılır | SU %100 → 0 · YOSUN BANDI gizli → açık · DİP görünmez → siyah silt | havuzun tamamı | doğu duvarı gölgesinin çekilmesi | yosun bandı (eski su çizgisi) | B | ANA |
| 1 | 8,0 | **TEMİZLER** | boş seramik kutu · siyah silt + yaprak matı · derin uçta birikinti ve pompa · merdiven duruyor · iki araba + kova · kapının yanında ilk atık yığını | ilk 2 sn: silt ve yaprak kovalara küreklenir, kovalar arabaya boşalır, araba soldan kapıdan çıkar · orta 4 sn: merdiven sökülüp kapıdan taşınır (dört boş cıvata deliği kalır); basınçlı su seramikte temiz şeritler açar ve temiz/kirli sınırı duvarları ve dibi süpürür; kirli su derin uçta toplanır, pompa dışarı basar · son 2 sn: iki çatlak açılıp gri harçla sıvanır, dip süpürülür, seramik sığ uçtan kurumaya başlar | KİR %100 → 0 · MERDİVEN %100 → 0 · ÇATLAK açık → sıvalı | temizlik + söküm | gölgenin kısalması · ıslak/kuru sınırı | temiz/kirli sınırının dipteki yeri | B | ANA |
| 2 | 8,0 | **KAPLAR** | temiz açık mavi seramik · kuruyan dip, derin uç hâlâ ıslak · gri harç izleri · dört cıvata deliği · pompa + basınçlı yıkayıcı · kapıda iki araba | ilk 2 sn: siyah boru derin uçtan sağ kenar boyunca harpuştaya, oradan nişin dibindeki filtre kutusuna çekilir · orta 4 sn: gri koruyucu keçe dibe ve duvarlara serilir, bindirilir; tek parça siyah astar dört streak tarafından BEL HİZASINDA taşınıp sığ uçtan açılır, köşelere bastırılır — mavi seramik sıra sıra KAYBOLUR · son 2 sn: astar kenarı harpuştanın üstüne kıvrılır ve düz taş ağırlıklarla tutturulur | SERAMİK %100 → 0 · ASTAR 0 → %100 · TESİSAT 0 → %100 | ⭐ BEDEL SAHNESİ | gölgenin en kısa hâli (tepe noktası) | kıvrılan astar kenarı + taş ağırlıklar | B | ANA |
| 3 | 8,0 | **DİZER** | kuru mat siyah çanak · harpuştada kıvrık astar + taş ağırlıklar · nişin dibinde filtre kutusu · duvarda boş ruloların göbekleri · kapıda araba | ilk 2 sn: BULUT GÖLGESİ avluyu soldan sağa geçer ve kadrajdan çıkar; ilk dolomit yükü kapıdan girer · orta 4 sn: kenar taşları soldan saat yönünde tek tek harç yastığına oturur ve astar kenarını kapatır; sağ arka köşede üç kademeli çağlayan taş sekide kurulur; yıkanmış çakıl sığ uca dökülüp sahanlık hâline taraklanır; arabanın lastikleri tozda çizgi bırakır · son 2 sn: son taş yakın kenarı kapatır, uzak kenarda sekiz dikim cebi açık bırakılıp koyu toprakla doldurulur, boşalan taş istifi kapıdan çıkar | TAŞ KENAR 0 → %100 · ÇAĞLAYAN 0 → %100 · ÇAKIL 0 → %100 | kenar + çağlayan | bulut gölgesinin geçişi · gölgelerin sağa dönmesi | eksilen taş istifi (kapının yanı) | B | ANA |
| 4 | 8,0 | **DİKER** | taş kenarlı siyah çanak · kuru çağlayan · çakıl sahanlık · sekiz açık toprak cebi · harç teknesi + torbalar · kapıda son iki blok | ilk 2 sn: saksılı eğrelti, saz ve yer örtücü dolu araba kapıdan girer, ilk bitkiler çağlayanın arkasındaki ceplere oturur · orta 4 sn: sekiz cep sırayla dolar, torbalardan malç dökülüp taşların arkasına koyu bant hâlinde serilir, sağ patikaya altı mat siyah fener çakılır ve kabloları taşların altına sokulur — BAŞLIKLAR SÖNÜK · son 2 sn: zeytin budanır, kesik dallar ve boş saksılar arabaya yüklenip kapıdan çıkar, dolum hortumu kapıdan girip uzak kenara asılır | DİKİM 0 → %100 · MALÇ 0 → %100 · FENER 0 → takılı (sönük) | dikim + donanım | zeytin tacının hafiflemesi · gölgelerin uzaması | eksilen saksı sayısı (16 → 0) | B | ANA |
| 5 | 8,0 | **DOLAR** | dikili uzak kenar · koyu malç bandı · altı sönük fener · uzak kenara asılı hortum · hâlâ KURU mat siyah çanak · budanmış zeytin | ilk 2 sn: hortumdan su gelir, derin uçtan bir tabaka yayılır, astar mattan koyu aynaya döner · orta 4 sn: seviye blokların iç yüzünü tırmanır — birinci, ikinci, ÜÇÜNCÜ taş — çakıl sahanlık alt kenarından su altında kalır; duvarın, nişin ve zeytinin yansıması yüzeyde açılır ve büyür; çağlayan çalışır, üç kademeden ince bir tabaka iner; güneş batı duvarının arkasına iner ve avlu düz gölgeye girer · son 2 sn: hortum çıkarılır ve kapıdaki arabaya sarılır, yüzey durulur | SU 0 → %100 · YANSIMA 0 → %100 · ÇAĞLAYAN kuru → akar | ⭐ DÖNÜŞ SAHNESİ | güneşin batı duvarının arkasına inmesi | su seviyesi ↔ yakın kenarın ÜÇÜNCÜ taşı | B | ANA |
| 6 | 8,0 | **YANAR** | dolu gölet, su üçüncü taşta · duran yüzey, yansıma açık · çağlayan akıyor · altı fener SÖNÜK · kapıda araba ve hortumu saran iki streak | ilk 2 sn: araba kapıdan çıkar, kapı kanadı kapanır, harpuştadaki son sıcak bant söner · orta 4 sn: altı fener sırayla YANAR; sıcak havuzcuklar taş kenara, eğreltilere ve suyun yakın kenarına düşer; duran yüzey her birini ikiye katlar; suyun taşıdığı renk altından koyu maviye iner · son 2 sn: TUTUŞ — yalnız çağlayanın ince tabakası ve aynada yayılan halkalar değişir | IŞIK sönük → yanık · AVLU dolu → boş | ⭐ ÖDÜL | mavi saate geçiş | yanan altı fener + yansımaları | A | ANA |

```
⭐ IZGARA — 120 BPM · ölçü 2,0 sn · 28 ölçü = 56,0 sn [MUZIK_VE_KAPAK §1.1 · A2-e]
   8,0 · 8,0 · 8,0 · 8,0 · 8,0 · 8,0 · 8,0
   ölçü:  4     4     4     4     4     4     4
   kesme anları: 8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0 — hepsi ölçünün 1. vuruşunda

⛔ DÜZ IZGARA BEYANI [KILAVUZ_REHBERI §2.6 · DERS 13 · DERS 24 · DERS 44]
   (a) GEREKÇE          proje sahibinin kilidi (16.09.2026): yedi sahne, sahne başına 8,0 sn. Yedi vuruş omurgadan
                        doğrudan türedi; bedel tek sahneye (S2) ve ödül son sahneye toplandı.
   (b) KABUL EDİLEN RİSK  ⑥ METRONOM hükmü beklenmektedir ve kabul edilmiştir. Düz ızgara iki kez koşuldu, iki kez
                        düştü (CLOSING SPAN · NARROW LOT); klip içi vuruş varyansı metronomu kırmadı (MOUNTAIN DOOR,
                        DERS 24). ⛔ Bu plana TELAFİ YAZILMAZ.
                        ⚠️ KARŞI KANIT NOTU [DERS 44 🔻]: THE CROSSING · OVER THE WALL · THE EMPTY RIDGE ⑥ RHYTHM aldı —
                        üçü de VARYANSLI kesildi. Düz ızgaranın kendisi hâlâ hiç RHYTHM almadı. Not düşüldü, ızgara
                        değişmedi — karar proje sahibinin.
   (c) İKİNCİ RİSK        S1 üç işi tek klipte taşır (atık + söküm + yıkama) ve §9.5 bütçesini zorlar; bu yüzden çatlak
                        onarımı S2'den ALINIP S1'in son 2 saniyesine verildi (ajan kararı, 16.09.2026).
   (d) ÜÇÜNCÜ RİSK        S5'te su seviyesi tek klipte 0'dan tam dolu hâle çıkar. Seviye KAREYE değil, adı konmuş bir
                        nesneye kilitlidir (yakın kenarın ÜÇÜNCÜ taşı); klip ortasındaki ara seviyeler kareye bağlı
                        değildir. Bu depoda "klibin içinde yazılan ara durum" üç kez atlandı [HAVA §6 · DERS 26 · 57];
                        risk kabul edildi, ⑦ ve ⑩ S5'te su seviyesini ayrıca sorar.
   prompt_kontrol.py bu ızgarayı FIX ile işaretler (BLOCK değil); FIX satırı bu beyanla kapanır.
   kesme_kontrol.sh "PLANIN KENDİSİ DÜZ" uyarısını basar; beklenen, kabul edilmiş.

⭐ İLK 24 SANİYE [P1-a]: S0–S2 üç FARKLI türden değişim taşır — su çekilmesi · yüzey temizliği + söküm · kaplama.
   Test: G3 ile G0 yan yana → işin türü (havuz gölete çevriliyor) okunuyor ✓.
⭐ KİNETİK İMZA: çekilir · temizler · kaplar · dizer · diker · dolar · yanar — ardışık tekrar yok [P1-f].
⭐ SEYİRCİ TAŞ SAYMAZ: ilerleme ÜÇ eşikle okunur — yosun bandı (S0) · astarın mavi seramiği kapatması (S2) ·
   suyun ÜÇÜNCÜ taşa gelmesi (S5). Kova, saksı ve blok sayımı üretim kontrolüdür (QA_SPEC · günlük).
```

### Üç zorunlu satır

```
① KANIT NESNESİ   her sahnede tabloda. ⭐ "AYNI YER" NESNESİ = KEMERLİ NİŞ (≈99 × 134 px) + ZEYTİN GÖVDESİ +
                  HAVUZUN SINIRI. zincir_kontrol.sh'in her koşusunda üçü de iki karede aynı yerde, aynı boyda mı —
                  ELLE ✓/✗ [DERS 25]. Niş küçüldüyse, kaydıysa ya da ikiye çoğaldıysa kare ATILIR.
② LOOP SATIRI     ⚠️ LOOP DEĞİL, AÇILIŞ–KAPANIŞ KAFİYESİ: G7 ↔ G0 aynı kadraj · aynı niş · aynı harpuşta · aynı
                  havuz sınırı. Havuz geri gelmez VE sabah akşama döner — kesintisiz döngü iddia edilmez.
                  Işık bilinçli: zincirli formatta ışık kesmede atlamaz [§2.7 ①], film TEK IŞIK GÜNÜNÜ süpürür
                  (6 × 2 saat + 1 × 10 dakika = 12 saat 10 dakika ≤ 14). Takvim YOK: film bir GÜN anlatır,
                  gerçek iş dört gün mertebesindedir — BİLİNÇLİ SIKIŞTIRMA, planda beyanlı.
③ SÖKÜM SATIRI    SÖKÜLEN GEÇİCİ EKİPMAN: dalgıç pompa + hortum (S0 dipte → S3 başında kapıdan çıkar) ·
                  paslanmaz merdiven (S1 ortası, kapıdan) · basınçlı yıkayıcı (S2 başı) · taş ağırlıklar
                  (S3'te kenar taşlarıyla değiştirilir) · rulo göbekleri (S3) · harç teknesi + torbalar (S4 sonu) ·
                  saksılar + kesik dallar (S4 sonu) · dolum hortumu (S4 sonunda gelir → S5 sonunda çıkar) ·
                  el arabası (S6 ilk 2 sn, en son çıkan şey).
                  KALANLAR: taş kenar · çağlayan · çakıl · bitkiler · malç · altı fener · nişin dibinde filtre
                  kutusu + kapak taşı. ⭐ POMPA İHTİYAÇ BİTENE KADAR KALIR: yıkama suyu çıkmadan pompa sökülmez.
                  Hiçbir şey KAYBOLMAZ [P2-h]; her giden şey KAPIDAN çıkar.
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
HAMMADDE   her parça KAPIDAN girer, avluyu geçer ve yerine konmadan ÖNCE görülür: keçe ve astar ruloları (S2,
           arabayla) · dolomit bloklar (S3, kapının yanındaki istif yük yük eksilir) · çakıl (S3, arabayla dökülür) ·
           toprak ve malç torbaları (S4) · saksılı bitkiler (S4, arabada 16 saksı → 0) · fenerler (S4) ·
           su (S5, hortumdan — tek kaynak). Atık ters yönde: yaprak ve silt (S1, kova kova) · merdiven (S1) ·
           boş saksı ve kesik dal (S4). "eksilen istif" = taş istifi ve saksı sayısı; ⑧ defteri: QA_SPEC §5.
GİZLİ İŞ   ① keçenin astar altında kalması → vekil: rulonun kadrajı geçmesi ve köşede görünen gri kenar (G3)
           ② taş kenarın altındaki boru → vekil: S2'de çekilen boru + nişin dibindeki filtre kutusu
           ③ fener kablosu → vekil: S4'te taşların altına sokulan kablo
           ④ harç prizi → vekil: yastıktan taşan taze harç (G4 dokusu)
           ⛔ Dördü de prompta İŞ olarak yazılmaz; yalnız vekil yazılır [P2-g].
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① YANAN SU — duran yüzey, altı sıcak nokta ve yansımaları, kadrajın alt yarısı (%13–52)
② TAŞ KENAR + DİKİLİ BANT — havuzun sınırı aynı, kenarı artık taş ve yeşil
③ BOŞ AVLU — merdiven yok, seramik yok, alet yok; döşeme süpürülmüş, kapı kapalı
Kapı: usta kare bu üçü bu sırayla okutmuyorsa kare yeniden — kompozisyonla, nesne ekleyerek değil.
Tutuş: S6'nın son 2,0 sn'si sabit KADRAJ, sabit YAPI, sabit IŞIK [P2-i]; FİNAL KARE KANITI 0:55,0'ten alınır
(QA_SPEC §1). Işık tutuşta yanıyor ama DEĞİŞMİYOR — tutuşta hareket yalnız çağlayanın tabakası ve halkalar.
⛔ FİNAL KARANLIK DEĞİL [DERS 45]: mavi saat, güneş ufkun 4° altında; duvar, taş ve bitki hâlâ okunur.
```

---

## 🖼️ KARE TABLOSU — N+1 = 8 görsel [KILAVUZ_REHBERI §2.7]

Işık TEK GÜNDÜR (kesme zaman atlamaz): 06:20 → 18:30; ilk altı kare 2 saat aralıklı (rejim B × 6), son aralık
10 dakikadır (rejim A). Güneş geometrisi 37°K, eylül ortası (δ +3°); gün doğumu 05:51, batımı 18:09 —
G6 ve G7 batıştan SONRADIR ve final AYDINLIKTIR [DERS 45]. Takvim yoktur; film bir günü anlatır.

| G | rol | saat | azimut / yükseklik | gölge yönü | havuz | avlu · kapı | çapa (niş · zeytin · harpuşta) |
|:-:|---|---|---|---|---|---|---|
| G0 | S0 ilk · filmin ilk karesi | 06:20 | 91° / 6° | doğu duvarı gölgesi bütün avluyu örter | koyu yeşil su, yaprak salı, yosun bandı gizli, merdiven takılı | pompa dipte, hortum kapıya · araba + kürek + kova | niş gölgede, harpuştanın üstü ilk ışıkta |
| G1 | S0 son · S1 ilk | 08:20 | 110° / 29° | uzun, sola | boş seramik kutu, siyah silt, ıslak derin uç, merdiven duruyor | iki araba, kovalar, kapının yanında atık yığını | zeytin uzun kırık gölge bırakır |
| G2 | S1 son · S2 ilk | 10:20 | 140° / 49° | kısa, geriye | temiz açık mavi seramik, ıslak/kuru sınırı, gri harç izleri, dört cıvata deliği | pompa + yıkayıcı, kapıda iki araba, süpürülmüş ıslak izler | niş tam ışıkta |
| G3 | S2 son · S3 ilk | 12:20 | 189° / 56° | en kısa, kuzeye | kuru MAT siyah astar, harpuştada kıvrık kenar + taş ağırlıklar | nişin dibinde filtre kutusu, duvarda rulo göbekleri | harpuşta düz, yamaç parlak |
| G4 | S3 son · S4 ilk | 14:20 | 232° / 43° | kısa-sert, sağa | taş kenar kapalı, kuru çağlayan, çakıl sahanlık, sekiz açık cep | harç teknesi + torbalar, kapıda son iki blok, tozda lastik izleri | bloklar nişin altında sıralanır |
| G5 | S4 son · S5 ilk | 16:20 | 257° / 22° | uzun, sağa | hâlâ KURU siyah çanak, dikili uzak kenar, koyu malç, altı SÖNÜK fener | uzak kenara asılı dolum hortumu, kapıda saksı yüklü araba | zeytin BUDANMIŞ (gövde aynı), duvar sıcak |
| G6 | S5 son · S6 ilk | 18:20 | 275° / ufkun 2° altında | yön yok, düz gölge; harpuştada sıcak bant | dolu gölet, su ÜÇÜNCÜ taşta, duran yüzey, yansıma açık, çağlayan akıyor, fenerler SÖNÜK | kapıda araba, hortum sarılıyor, döşeme süpürülmüş | niş ve zeytin SUDA da görünür |
| G7 | ⭐ USTA KARE · S6 son · kapak kaynağı | 18:30 | 277° / ufkun 4° altında | mavi saat, altı sıcak havuzcuk | dolu gölet, duran ayna, altı fener YANIK + yansımaları, çağlayan akıyor | avlu BOŞ, kapı kapalı, kapak taşı filtrenin üstünde | niş, zeytin ve harpuşta suda ikinci kez |

```
⛔ Üretim sırası TERS ve ZİNCİRLİ [§8]: G7 önce → G6 → G5 → G4 → G3 → G2 → G1 → G0, her kare bir öncekinin
   üstünde EDİT (master'dan ne KALDIRILDI / ne EKLENDİ) [P2-a]:
     G7 → G6   fenerler SÖNDÜRÜLÜR (başlıklar mat siyah, su yalnız duvarı ve zeytini taşır); kapı AÇILIR;
               kapıya araba + sarılan hortum + iki streak; harpuştaya sıcak bant; kapak taşı filtrenin YANINA; 18:20
     G6 → G5   su BOŞALTILIR → kuru mat siyah astar + pale çakıl; yansıma kalkar; çağlayan kurur; hortum uzak
               kenara ASILIR; kapıya saksı yüklü araba; gölgeler uzar ve sağa döner; 16:20
     G5 → G4   bitkiler, malç ve altı fener KALDIRILIR → sekiz açık toprak cebi; zeytin BUDANMAMIŞ hâle (taç
               daha dolu, gövde aynı); harç teknesi + torbalar duvara; kapıya son iki blok; 14:20
     G4 → G3   taş kenar, çağlayan ve çakıl KALDIRILIR → çıplak astar; harpuştaya taş ağırlıklar GERİ;
               duvara rulo göbekleri; tozda lastik izleri silinir; gölgeler kısalır; 12:20
     G3 → G2   astar ve keçe KALDIRILIR → temiz açık mavi seramik + gri harç izleri + dört cıvata deliği;
               filtre kutusu kaldırılır, boru kaldırılır; pompa + yıkayıcı GERİ; 10:20
     G2 → G1   temizlik GERİ ALINIR → siyah silt + yaprak matı + derin uçta birikinti; merdiven GERİ; harç izleri
               kaldırılır; kapının yanına atık yığını; 08:20
     G1 → G0   su GERİ KONUR → koyu yeşil dolu havuz + yaprak salı; yosun bandı suyun ÜSTÜNDE kalan kısma iner;
               ikinci araba kaldırılır; doğu duvarının gölgesi bütün avluya; 06:20
   ⛔ HER KAREDEN SONRA: bash araclar/zincir_kontrol.sh <önceki_onaylı> <yeni>  → çıkış 2 = AT
   ⛔ VE NİŞ + ZEYTİN GÖVDESİ + HAVUZ SINIRI iki karede de aynı yerde, aynı boyda mı — ELLE ✓/✗ [DERS 25]
   ⛔ Havuz = 1 · ağaç = 1 · niş = 1 · fener = 6 sayımı ELLE [DERS 55]
   ⚠️ G1 → G0 filmin tek "GERİ KOYMA" editidir (su). Model yeşil suyu başka tonda çizerse G0 atılmaz, ama
      G0'daki su rengi ve yosun bandının yüksekliği kayda geçer — bedelin kanıtı G0 ↔ G7 çiftidir (SPEC §1).
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM

```
· Kamera 0°'ye (kuzeye) bakar; güneş 91° → 277°. Kadraj yatayda az 337°–23°: disk hiçbir karede kadrajda değil;
  sabah sağdan (doğu duvarı avluya uzun gölge atar), öğle arkadan (gölgeler en kısa, kuzeye), akşam soldan
  (batı duvarı avluyu kapatır). LIGHTING güneşi yalnız açı · gölge yönü · gök rengiyle anar [DERS 39].
· ⭐ MEVSİM TAŞIYICISI YOKTUR ÇÜNKÜ MEVSİM YOKTUR [DERS 14'ün sınır hâli]: film bir GÜN anlatır. Taşıyıcı
  GÖLGEDİR ve merdiven tablosunda sütun sütun yazılıdır: doğu duvarı gölgesinin çekilmesi → kısalma → en kısa →
  sağa dönme → uzama → batı duvarının kapatması → mavi saat. Bu, ③ merceğinin "TIME READ FROM THE FILM ALONE"
  hedefinde MERTEBE olarak "bir gün" verir [P1-c] ve plan bunu açıkça iddia eder.
· ⚠️ BİLİNÇLİ SIKIŞTIRMA BEYANI: gerçek iş (boşaltma · temizlik · astar · taş · dikim · dolum) dört gün
  mertebesindedir. Film onu tek ışık gününe sıkıştırır; bu bir üslup kararıdır, planda beyanlıdır ve QA'ya
  "gerçekçilik hatası" olarak sayılmaz — ③ merceği filmin KENDİ iddiasına bakar.
· Sahne içi saat: rejim B (2 saat) — gölge boyu ve yönü her karede tabloda. S6 rejim A'dır (10 dakika):
  10 dakikada gölge yoktur, taşıyıcı IŞIĞIN RENGİDİR (altın → derin mavi) ve fenerlerin yanmasıdır.
· ⚠️ S6 GÖLGESİZDİR. DERS 40 kapısı açılmaz çünkü süreler eşittir ve S6 filmin en uzun sahnesi değildir;
  ayrıca rejim C değil A'dır — 10 dakikada su ve ışık gerçekçi hızda okunur.
· ⭐ BULUT: gök kadrajda olmadığı için bulut yalnız GÖLGE olarak vardır. S3'ün ilk 2 saniyesinde bir bulut
  gölgesi avluyu soldan sağa geçer [KİNETİK PAKET ④]. Başka hiçbir sahnede bulut gölgesi YAZILMAZ — iki kez
  yazılırsa ritim aracı olmaktan çıkar, hava olayına döner.
· ⭐ SU YÜZEYİ 1200×'te: dalga yazılmaz. S5'te seviye YÜKSELİR (bant), yansıma AÇILIR (alan); S6'da (100×)
  çağlayanın tabakası ve halkalar ipeksidir [SANTIYE §1 · DERS 50].
```

---

# 🎥 PROMPTLAR

> Her prompt kendi başına çalışır; belge atfı yok [D-a]. YAPI BIBLE (tek cümle), SITE / BACKGROUND, kamera satırı,
> COMPOSITION çapa cümlesi ve NEGATIVE sekiz karede BİREBİR aynıdır. Değişen: AT THIS STAGE · THE TIME MOMENT ·
> COMPOSITION eki · LIGHTING · ACTIVITY · SITE TEXTURE · PHYSICS. I2V: iki uç birebir cümleyle kilitli [§2.7];
> klip n = G(n) → G(n+1).

---
## 🎬 SAHNE 0 — ÇEKİLİR  ·  0,0 – 8,0 sn  ·  06:20 → 08:20  ·  rejim B

### 📸 GÖRSEL PROMPT (G0)

```
Photorealistic documentary construction photograph — Scene 0 of 7. Vertical time-lapse of one abandoned swimming pool rebuilt as a stone-edged garden pond inside a walled courtyard, seen from a balcony above it; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod clamped to the balcony rail of the house on the south side, lens 6.0 metres above the courtyard floor, 5.0 metres from the centre of the pool, bearing 0 degrees, tilt 40 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single stone-edged garden pond in the footprint of the old pool, with a three-step cascade in its far right corner, a gravel beach at its near end and planted pockets along its far rim. AT THIS STAGE: the pool is still the old swimming pool and it is full of standing water, dark green and opaque, with a raft of fallen olive leaves on it. A band of dried green algae marks the glazed pale blue tile above the surface and the tile below it reads green-black. A stainless three-step bathing ladder is bolted to the near left corner, its feet rusted, and the bathing step inside the shallow end shows as a pale ledge under the water. A submersible pump has just been lowered into the deep end at the far right, its black hose running over the coping and out through the gate, and a garden cart with two shovels and a stack of buckets stands at the near rim.

SITE / BACKGROUND: A single walled courtyard fills the frame, its floor laid with weathered limestone flagstones, and one rectangular pool with rounded corners lies in the middle of it. One old olive tree stands on the left, the only tree inside the walls, its trunk rising from the flagstones at about nine percent of frame width and its canopy across the upper left corner. The rear wall runs straight across the frame, dry stone under worn lime plaster, capped with a flat stone coping level at about seventy-nine percent of frame height, with one arched niche set into it right of centre and a gate in the left-hand wall beside it. Beyond the coping a terraced hillside of olive rows and dry grass climbs to the top of the frame. Apart from the work inside the walls, the courtyard, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge.

THE TIME MOMENT: The pool exactly as the years left it, on the first morning anyone has come back to it.

COMPOSITION: Vertical 9:16. The arched niche sits right of centre, between fifty-eight and sixty-seven percent of frame width and between sixty-eight and seventy-five percent of frame height; it spans about 99 pixels of frame width — one eleventh — and keeps that width and position in every frame. The near rim of the pool crosses at about thirteen percent of frame height and the far rim at about fifty-two percent, and nothing that proves progress falls into the right eighth or the bottom eighth of the frame. The green water fills the pool between thirteen and fifty-two percent of frame height and holds the darkest area in the frame; the ladder and the cart stand at the near left corner.

LIGHTING: Sun azimuth 91 degrees, elevation 6 degrees, first light from the right and very low, the shadow of the east wall lying right across the courtyard and the pool, a wedge of warm light on the rear wall above the coping and on the hillside behind it. The sun stays outside the frame for the whole shot; its only sign is the shadows. Mid-September, the end of a dry summer: the hillside grass bleached, the olive canopy dusty and unpruned.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows on the courtyard floor, the cloud shadows on the wall, the water, the crew and the cart all move at the same accelerated speed. Two hours pass across this shot: shadows sweep across the flagstones and every moving thing smears into heavy motion blur. Nothing in the frame moves at normal speed.

ACTIVITY: The pump drops the first centimetres of the green surface and drives a rope of dirty water out along the hose through the gate, opening a wet dark ring on the tile; the crew push the cart the length of the near rim and drop two shovels against it. Crew register only as faint soft motion streaks at the near rim and by the gate, never as sharp figures.

SITE TEXTURE: A dried green algae band across the upper tile courses; black silt and a leaf mat showing through the water at the deep end; moss patches in the coping joints and dust and weed in the flagstone joints; rust streaks down the ladder feet; a pale efflorescence bloom on the plaster under the niche; cart tracks printed in the dust across the flagstones; stone debris along the foot of the rear wall.

PHYSICS: The pump sits on the tiled floor at the deep end under the water and its hose rests over the stone coping and runs slack to the gate; the ladder is bolted to the coping and its feet are seated on the tile; the cart stands on its two wheels with its legs planted on the flagstones; the olive trunk is rooted in an open square of earth in the paving.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The walls, the coping, the arched niche, the olive trunk and the hillside never change shape, position, size or spacing; the outline of the pool never changes. Nothing already built is removed, moved or resized; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, container, panel, facade, hoarding, signage, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G0 → G1)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across an early September morning. Everything in this shot is time-lapsed at the same rate: the shadow of the east wall pulls back across the courtyard as the sun climbs, cloud shadows sweep over the wall and the hillside, and every moving thing is smeared into a blur. First the pump drives a steady rope of dirty water out along the hose and through the gate, and the green surface drops away from the coping, leaving a wet dark ring on the tile that dries to a hard green band. Then the water goes on falling course by course, the raft of leaves settling onto the floor as a black mat, the feet of the ladder coming clear, the bathing step at the shallow end rising out of the water, and the light reaches the tiled floor for the first time as the wall shadow slides back. Then the last water is a shallow black puddle around the pump at the deep end. Finally a second cart is pushed in through the gate, shovels and buckets are dropped at the near rim, and a first heap of wet leaves is left beside the gate. The walls, the coping, the niche, the olive trunk and the hillside do not change. The sky stays out of the frame; its only signs are the light that grades across the courtyard floor, the cloud shadows that sweep over the wall and across the stone, and the light the water holds.

The camera does not move at any point. The framing is identical in the first and last frame. The courtyard walls, the wall coping, the arched niche, the olive trunk and the terraced hillside stay exactly where they are, at exactly the same size and shape, for the whole shot. The wall coping stays level at exactly seventy-nine percent of the frame height. The arched niche occupies exactly the same width of the frame in the first and last frame. The outline of the pool never changes. Apart from the work inside the walls, the courtyard floor, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge. This is one pool in one walled courtyard and the only one in view. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 1 — TEMİZLER  ·  8,0 – 16,0 sn  ·  08:20 → 10:20  ·  rejim B

### 📸 GÖRSEL PROMPT (G1)

```
Photorealistic documentary construction photograph — Scene 1 of 7. Vertical time-lapse of one abandoned swimming pool rebuilt as a stone-edged garden pond inside a walled courtyard, seen from a balcony above it; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod clamped to the balcony rail of the house on the south side, lens 6.0 metres above the courtyard floor, 5.0 metres from the centre of the pool, bearing 0 degrees, tilt 40 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single stone-edged garden pond in the footprint of the old pool, with a three-step cascade in its far right corner, a gravel beach at its near end and planted pockets along its far rim. AT THIS STAGE: the water is gone and the pool is an empty tiled box. Its floor carries a black silt layer and a flattened leaf mat, deepest at the far right where a shallow puddle still stands around the pump. The glazed pale blue tile is exposed for the first time: the dried green algae band across its upper courses, a stained field below it, and the pale ledge of the bathing step along the shallow end. The stainless ladder still stands at the near left corner and the pump lies in the last of the water with its hose over the coping. Two carts now stand at the near rim with shovels and buckets, and a first spoil heap of wet leaves has been dropped beside the gate.

SITE / BACKGROUND: A single walled courtyard fills the frame, its floor laid with weathered limestone flagstones, and one rectangular pool with rounded corners lies in the middle of it. One old olive tree stands on the left, the only tree inside the walls, its trunk rising from the flagstones at about nine percent of frame width and its canopy across the upper left corner. The rear wall runs straight across the frame, dry stone under worn lime plaster, capped with a flat stone coping level at about seventy-nine percent of frame height, with one arched niche set into it right of centre and a gate in the left-hand wall beside it. Beyond the coping a terraced hillside of olive rows and dry grass climbs to the top of the frame. Apart from the work inside the walls, the courtyard, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge.

THE TIME MOMENT: The morning the basin is seen empty for the first time, with the silt still on its floor.

COMPOSITION: Vertical 9:16. The arched niche sits right of centre, between fifty-eight and sixty-seven percent of frame width and between sixty-eight and seventy-five percent of frame height; it spans about 99 pixels of frame width — one eleventh — and keeps that width and position in every frame. The near rim of the pool crosses at about thirteen percent of frame height and the far rim at about fifty-two percent, and nothing that proves progress falls into the right eighth or the bottom eighth of the frame. The empty basin reads as a pale blue box with a black floor between thirteen and fifty-two percent of frame height, the carts at its near rim and the spoil heap by the gate.

LIGHTING: Sun azimuth 110 degrees, elevation 29 degrees, morning light from the right, long shadows falling west, toward the left of the frame, the rear wall lit and the olive throwing a long broken shadow across the flagstones. The sun stays outside the frame for the whole shot; its only sign is the shadows. Mid-September, the end of a dry summer: the hillside grass bleached, the olive canopy dusty and unpruned.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows on the courtyard floor, the cloud shadows on the wall, the water, the crew and the cart all move at the same accelerated speed. Two hours pass across this shot: shadows sweep across the flagstones and every moving thing smears into heavy motion blur. Nothing in the frame moves at normal speed.

ACTIVITY: The crew lift a filled bucket out of the basin and tip it into the cart, and the cart crosses the flagstones and goes out through the gate as a grey blur; the pump drives the last of the dirty water out along the hose. Crew register only as faint soft motion streaks in the basin and along the path to the gate, never as sharp figures.

SITE TEXTURE: Black silt and a flattened leaf mat across the tiled floor; a shallow puddle standing around the pump at the deep end; the dried algae band above a stained field of glazed tile; crack lines running down two tile courses; rust streaks at the ladder feet; a growing spoil heap of wet leaves by the gate; cart tracks printed through the dust.

PHYSICS: The pump rests on the tiled floor in the last of the water and its hose rests over the coping; the ladder is bolted to the coping with its feet seated on the tile; the two carts stand on their wheels with their legs planted on the flagstones; the shovels lean against the coping and the spoil heap bears on the flagstones beside the gate.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The walls, the coping, the arched niche, the olive trunk and the hillside never change shape, position, size or spacing; the outline of the pool never changes. Nothing already built is removed, moved or resized; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, container, panel, facade, hoarding, signage, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G1 → G2)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across a clear September morning. Everything in this shot is time-lapsed at the same rate: the long shadows on the flagstones shorten and swing away from the camera as the sun climbs, cloud shadows cross the wall and the hillside, and every moving thing is smeared into a blur. First the silt and the leaf mat are shovelled into buckets, the buckets are tipped into the carts and the carts cross the frame to the left and out through the gate, load after load, and the heap beside the gate rises and goes down again. Then the stainless ladder is unbolted and carried out through the gate, leaving four dark bolt holes at the near left corner. Then a pressure washer opens clean pale stripes across the glazed tile, stripe beside stripe, and the boundary between dirty and clean sweeps down the walls and across the floor while the dirty water gathers at the deep end and the pump lifts it out along the hose. Finally two cracks are cut open and struck flush with grey mortar, the floor is swept toward the deep end, and the tile begins to dry from the shallow end back. The walls, the coping, the niche, the olive trunk and the hillside do not change. The sky stays out of the frame; its only signs are the light that grades across the courtyard floor, the cloud shadows that sweep over the wall and across the stone, and the light the water holds.

The camera does not move at any point. The framing is identical in the first and last frame. The courtyard walls, the wall coping, the arched niche, the olive trunk and the terraced hillside stay exactly where they are, at exactly the same size and shape, for the whole shot. The wall coping stays level at exactly seventy-nine percent of the frame height. The arched niche occupies exactly the same width of the frame in the first and last frame. The outline of the pool never changes. Apart from the work inside the walls, the courtyard floor, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge. This is one pool in one walled courtyard and the only one in view. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 2 — KAPLAR  ·  16,0 – 24,0 sn  ·  10:20 → 12:20  ·  rejim B

### 📸 GÖRSEL PROMPT (G2)

```
Photorealistic documentary construction photograph — Scene 2 of 7. Vertical time-lapse of one abandoned swimming pool rebuilt as a stone-edged garden pond inside a walled courtyard, seen from a balcony above it; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod clamped to the balcony rail of the house on the south side, lens 6.0 metres above the courtyard floor, 5.0 metres from the centre of the pool, bearing 0 degrees, tilt 40 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single stone-edged garden pond in the footprint of the old pool, with a three-step cascade in its far right corner, a gravel beach at its near end and planted pockets along its far rim. AT THIS STAGE: the basin is empty, washed and drying. The glazed tile is pale and clean from the coping down, the algae band gone, and the drying boundary crosses the floor as a soft edge with the deep end still dark and wet. Two crack lines have been cut open and struck flush with grey mortar, darker than the tile around them, and the bathing step at the shallow end reads as a clean pale ledge. Four empty bolt flanges mark the near left corner. The pump lies in the deep end with its hose over the coping, a pressure washer stands on the flagstones with its lance across the coping, and the two carts wait by the gate on swept stone that carries wet tracks.

SITE / BACKGROUND: A single walled courtyard fills the frame, its floor laid with weathered limestone flagstones, and one rectangular pool with rounded corners lies in the middle of it. One old olive tree stands on the left, the only tree inside the walls, its trunk rising from the flagstones at about nine percent of frame width and its canopy across the upper left corner. The rear wall runs straight across the frame, dry stone under worn lime plaster, capped with a flat stone coping level at about seventy-nine percent of frame height, with one arched niche set into it right of centre and a gate in the left-hand wall beside it. Beyond the coping a terraced hillside of olive rows and dry grass climbs to the top of the frame. Apart from the work inside the walls, the courtyard, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge.

THE TIME MOMENT: Mid-morning, the tile clean and the last wet patch drying off the deep end.

COMPOSITION: Vertical 9:16. The arched niche sits right of centre, between fifty-eight and sixty-seven percent of frame width and between sixty-eight and seventy-five percent of frame height; it spans about 99 pixels of frame width — one eleventh — and keeps that width and position in every frame. The near rim of the pool crosses at about thirteen percent of frame height and the far rim at about fifty-two percent, and nothing that proves progress falls into the right eighth or the bottom eighth of the frame. The clean blue basin holds the brightest area in the lower half of the frame between thirteen and fifty-two percent of frame height, the wet-dry boundary crossing its floor diagonally.

LIGHTING: Sun azimuth 140 degrees, elevation 49 degrees, late-morning light from behind and to the right, short shadows falling north-north-west, away from the camera, the wet tile at the deep end throwing a hard sheen. The sun stays outside the frame for the whole shot; its only sign is the shadows. Mid-September, the end of a dry summer: the hillside grass bleached, the olive canopy dusty and unpruned.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows on the courtyard floor, the cloud shadows on the wall, the water, the crew and the cart all move at the same accelerated speed. Two hours pass across this shot: shadows sweep across the flagstones and every moving thing smears into heavy motion blur. Nothing in the frame moves at normal speed.

ACTIVITY: The crew spread a fresh skim of mortar along the last open crack and sweep the drying floor toward the deep end; the cart is pushed out through the gate with the last buckets of spoil and the pump lifts the washings out along the hose. Crew register only as faint soft motion streaks on the basin floor and at the gate, never as sharp figures.

SITE TEXTURE: Clean glazed tile with a wet sheen at the deep end and a dry chalky bloom at the shallow end; the wet-dry boundary crossing the floor as a soft band; two grey mortar streaks where the cracks were struck; four dark bolt holes at the near left corner; splash stains up the plaster of the rear wall; wet cart tracks and hose drag marks on the flagstones.

PHYSICS: The pressure washer stands on its feet on the flagstones and its lance rests across the stone coping; the pump rests on the tiled floor at the deep end; the carts stand on their wheels with their legs planted on the flagstones by the gate; the buckets are stacked one inside another against the foot of the rear wall.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The walls, the coping, the arched niche, the olive trunk and the hillside never change shape, position, size or spacing; the outline of the pool never changes. Nothing already built is removed, moved or resized; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, container, panel, facade, hoarding, signage, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G2 → G3)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across the middle of a clear September day. Everything in this shot is time-lapsed at the same rate: the shadows shorten to almost nothing as the sun crosses behind the camera, cloud shadows sweep across the courtyard floor, and every moving thing is smeared into a blur. First a black flexible pipe is laid from the deep end along the right-hand edge of the basin, over the coping and across the flagstones, and a filter box is set down at the foot of the rear wall under the arched niche. Then rolls of grey protective membrane come in on the cart and are unrolled across the floor and up the walls of the basin, overlapped and pressed into the corners, and the pale blue tile goes under them. Then four soft streaks carry in a single heavy roll of black rubber liner at waist height, lay it at the shallow end and unroll it the length of the basin, pushing it into the corners and folding it flat at the ends until the tile is gone and the basin is one dry matte black bowl. Finally the edge of the liner is folded over the stone coping all round and dropped under flat stone weights, the empty roll cores are stood against the rear wall and the cart is pushed out. The walls, the coping, the niche, the olive trunk and the hillside do not change. The sky stays out of the frame; its only signs are the light that grades across the courtyard floor, the cloud shadows that sweep over the wall and across the stone, and the light the water holds.

The camera does not move at any point. The framing is identical in the first and last frame. The courtyard walls, the wall coping, the arched niche, the olive trunk and the terraced hillside stay exactly where they are, at exactly the same size and shape, for the whole shot. The wall coping stays level at exactly seventy-nine percent of the frame height. The arched niche occupies exactly the same width of the frame in the first and last frame. The outline of the pool never changes. Apart from the work inside the walls, the courtyard floor, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge. This is one pool in one walled courtyard and the only one in view. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 3 — DİZER  ·  24,0 – 32,0 sn  ·  12:20 → 14:20  ·  rejim B

### 📸 GÖRSEL PROMPT (G3)

```
Photorealistic documentary construction photograph — Scene 3 of 7. Vertical time-lapse of one abandoned swimming pool rebuilt as a stone-edged garden pond inside a walled courtyard, seen from a balcony above it; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod clamped to the balcony rail of the house on the south side, lens 6.0 metres above the courtyard floor, 5.0 metres from the centre of the pool, bearing 0 degrees, tilt 40 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single stone-edged garden pond in the footprint of the old pool, with a three-step cascade in its far right corner, a gravel beach at its near end and planted pockets along its far rim. AT THIS STAGE: the pale blue tile has gone under a lining. A grey protective membrane has been unrolled across the floor and up the walls of the basin, and over it a single sheet of black rubber liner runs from the shallow end to the deep end, pushed into the corners and folded flat at the ends; the liner is dry and matte and absorbs the light, and the bathing step reads now only as a soft ledge under the rubber. Its edge is folded over the stone coping all round and held down with flat stone weights. A black pipe runs from the deep end along the right-hand edge, over the coping and across to a filter box seated under the arched niche, with a flat cover stone beside it. Two empty roll cores lean against the rear wall and the cart waits at the gate.

SITE / BACKGROUND: A single walled courtyard fills the frame, its floor laid with weathered limestone flagstones, and one rectangular pool with rounded corners lies in the middle of it. One old olive tree stands on the left, the only tree inside the walls, its trunk rising from the flagstones at about nine percent of frame width and its canopy across the upper left corner. The rear wall runs straight across the frame, dry stone under worn lime plaster, capped with a flat stone coping level at about seventy-nine percent of frame height, with one arched niche set into it right of centre and a gate in the left-hand wall beside it. Beyond the coping a terraced hillside of olive rows and dry grass climbs to the top of the frame. Apart from the work inside the walls, the courtyard, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge.

THE TIME MOMENT: Midday, the hour the old pool is covered over and stops being a pool.

COMPOSITION: Vertical 9:16. The arched niche sits right of centre, between fifty-eight and sixty-seven percent of frame width and between sixty-eight and seventy-five percent of frame height; it spans about 99 pixels of frame width — one eleventh — and keeps that width and position in every frame. The near rim of the pool crosses at about thirteen percent of frame height and the far rim at about fifty-two percent, and nothing that proves progress falls into the right eighth or the bottom eighth of the frame. The lined basin reads as one matte black field between thirteen and fifty-two percent of frame height, the darkest area in the frame, and the stone weights make a broken pale line round its rim.

LIGHTING: Sun azimuth 189 degrees, elevation 56 degrees, midday light from behind the camera, the shortest shadows of the day falling north, away from the camera, the black liner reading as a flat light-absorbing field with no sheen. The sun stays outside the frame for the whole shot; its only sign is the shadows. Mid-September, the end of a dry summer: the hillside grass bleached, the olive canopy dusty and unpruned.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows on the courtyard floor, the cloud shadows on the wall, the water, the crew and the cart all move at the same accelerated speed. Two hours pass across this shot: shadows sweep across the flagstones and every moving thing smears into heavy motion blur. Nothing in the frame moves at normal speed.

ACTIVITY: The crew unroll the last of the black liner up the far wall of the basin and drop a flat stone weight onto its folded edge, working along the coping; the cart is pushed in through the gate with the cover stone and pushed out empty. Crew register only as faint soft motion streaks along the coping and on the basin floor, never as sharp figures.

SITE TEXTURE: Matte black rubber with fold creases across the floor and slack in the corners; a grey membrane edge showing under the liner at the near left corner; flat stone weights along the coping; chalk dust, rubber offcuts and tape debris on the flagstones; boot prints and a drag mark where the pipe was pulled through the dust; splash stains up the rear wall plaster; grit patches in the coping joints.

PHYSICS: The liner rests on the membrane and the membrane rests on the tiled floor, both lying slack in the corners; the folded edge is clamped over the stone coping under flat weights that bear on it all round; the filter box is seated on the flagstones under the niche and the pipe rests over the coping; the roll cores lean against the wall.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The walls, the coping, the arched niche, the olive trunk and the hillside never change shape, position, size or spacing; the outline of the pool never changes. Nothing already built is removed, moved or resized; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, container, panel, facade, hoarding, signage, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G3 → G4)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across a clear September afternoon. Everything in this shot is time-lapsed at the same rate: the shadows begin to lengthen toward the right as the sun goes west, a cloud shadow crosses the whole courtyard from left to right and slides off the frame, and every moving thing is smeared into a blur. First the cart comes in through the gate loaded with rough dolomite boulders and the stack beside the gate is worked down load by load. Then the rim is laid stone by stone, each boulder bedded on a fresh pad of mortar over the folded liner edge and worked round the coping from the left, and the three-step cascade is built up in the far right corner on a shelf of the same stone. Then washed gravel is tipped into the shallow end and raked out into a beach, and the tyres of the cart print lines through the dust across the flagstones. Finally the last boulder closes the near rim, eight pockets are left open along the far rim and filled with dark soil, and the empty stone stack is swept away beside the gate. The walls, the coping, the niche, the olive trunk and the hillside do not change. The sky stays out of the frame; its only signs are the light that grades across the courtyard floor, the cloud shadows that sweep over the wall and across the stone, and the light the water holds.

The camera does not move at any point. The framing is identical in the first and last frame. The courtyard walls, the wall coping, the arched niche, the olive trunk and the terraced hillside stay exactly where they are, at exactly the same size and shape, for the whole shot. The wall coping stays level at exactly seventy-nine percent of the frame height. The arched niche occupies exactly the same width of the frame in the first and last frame. The outline of the pool never changes. Apart from the work inside the walls, the courtyard floor, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge. This is one pool in one walled courtyard and the only one in view. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 4 — DİKER  ·  32,0 – 40,0 sn  ·  14:20 → 16:20  ·  rejim B

### 📸 GÖRSEL PROMPT (G4)

```
Photorealistic documentary construction photograph — Scene 4 of 7. Vertical time-lapse of one abandoned swimming pool rebuilt as a stone-edged garden pond inside a walled courtyard, seen from a balcony above it; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod clamped to the balcony rail of the house on the south side, lens 6.0 metres above the courtyard floor, 5.0 metres from the centre of the pool, bearing 0 degrees, tilt 40 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single stone-edged garden pond in the footprint of the old pool, with a three-step cascade in its far right corner, a gravel beach at its near end and planted pockets along its far rim. AT THIS STAGE: the lined basin has been given a stone rim. Rough dolomite boulders, warm grey with orange lichen, are bedded in a single course all round the coping, hiding the folded liner edge, and a three-step cascade has been built up in the far right corner on a shelf of the same stone, dry and unfed. Washed river gravel has been tipped into the shallow end and raked into a beach. Eight planting pockets are left open along the far rim between the boulders, each filled with dark soil. The pump and its hose have gone out through the gate; a mixing tub and a row of mortar bags stand against the rear wall, and the stone stack beside the gate is down to its last two boulders.

SITE / BACKGROUND: A single walled courtyard fills the frame, its floor laid with weathered limestone flagstones, and one rectangular pool with rounded corners lies in the middle of it. One old olive tree stands on the left, the only tree inside the walls, its trunk rising from the flagstones at about nine percent of frame width and its canopy across the upper left corner. The rear wall runs straight across the frame, dry stone under worn lime plaster, capped with a flat stone coping level at about seventy-nine percent of frame height, with one arched niche set into it right of centre and a gate in the left-hand wall beside it. Beyond the coping a terraced hillside of olive rows and dry grass climbs to the top of the frame. Apart from the work inside the walls, the courtyard, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge.

THE TIME MOMENT: Early afternoon, the rim closed and the pockets waiting for planting.

COMPOSITION: Vertical 9:16. The arched niche sits right of centre, between fifty-eight and sixty-seven percent of frame width and between sixty-eight and seventy-five percent of frame height; it spans about 99 pixels of frame width — one eleventh — and keeps that width and position in every frame. The near rim of the pool crosses at about thirteen percent of frame height and the far rim at about fifty-two percent, and nothing that proves progress falls into the right eighth or the bottom eighth of the frame. The stone rim draws the pool's outline as an unbroken pale line round a black field between thirteen and fifty-two percent of frame height, the cascade against the right-hand end of the rear wall.

LIGHTING: Sun azimuth 232 degrees, elevation 43 degrees, afternoon light from behind and to the left, shadows falling east-north-east, toward the right of the frame, each boulder throwing a short hard shadow onto the black liner. The sun stays outside the frame for the whole shot; its only sign is the shadows. Mid-September, the end of a dry summer: the hillside grass bleached, the olive canopy dusty and unpruned.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows on the courtyard floor, the cloud shadows on the wall, the water, the crew and the cart all move at the same accelerated speed. Two hours pass across this shot: shadows sweep across the flagstones and every moving thing smears into heavy motion blur. Nothing in the frame moves at normal speed.

ACTIVITY: The crew bed the last boulder into a fresh pad of mortar on the near rim and tamp a cartload of gravel into the beach at the shallow end; the cart is pushed in from the stone stack and back out through the gate, its tyres printing lines through the dust. Crew register only as faint soft motion streaks on the rim and at the mixing tub, never as sharp figures.

SITE TEXTURE: Rough dolomite with orange lichen patches and fresh mortar squeezed out at the bedding joints; washed grey gravel with rake marks still in it; dark soil in the open pockets; mortar spatter and a grey slurry stain round the mixing tub; cart tracks printed through the stone dust; torn mortar bags against the rear wall; matte black liner still showing across the basin floor.

PHYSICS: Each boulder is bedded on a pad of mortar that bears on the stone coping over the folded liner edge, and the boulders lean on one another all round the rim; the three cascade steps are bedded one on the next on a shelf of stone founded on the flagstones; the gravel beach rests on the liner; the mixing tub and the bags stand on the flagstones.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The walls, the coping, the arched niche, the olive trunk and the hillside never change shape, position, size or spacing; the outline of the pool never changes. Nothing already built is removed, moved or resized; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, container, panel, facade, hoarding, signage, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G4 → G5)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across a September afternoon going into evening. Everything in this shot is time-lapsed at the same rate: the shadows of the boulders stretch out to the right as the sun drops toward the west wall, high cloud drifts and thins over the hillside, and every moving thing is smeared into a blur. First a cart comes in through the gate loaded with potted ferns, sedges and a low creeping ground cover, and the first plants are set into the pockets behind the cascade. Then pocket after pocket is filled along the far rim, bark mulch is tipped from bags and spread into a dark band behind the stone, and six low matt-black lamps are pushed into the ground along the right-hand path with their cable tucked under the rim stones; their heads stay dark. Then the olive is pruned and its canopy opens and lightens, and the cut branches are carried out through the gate. Finally the empty pots are stacked on the cart and pushed out, and a filling hose is dragged in through the gate and hooked over the far rim. The walls, the coping, the niche, the olive trunk and the hillside do not change. The sky stays out of the frame; its only signs are the light that grades across the courtyard floor, the cloud shadows that sweep over the wall and across the stone, and the light the water holds.

The camera does not move at any point. The framing is identical in the first and last frame. The courtyard walls, the wall coping, the arched niche, the olive trunk and the terraced hillside stay exactly where they are, at exactly the same size and shape, for the whole shot. The wall coping stays level at exactly seventy-nine percent of the frame height. The arched niche occupies exactly the same width of the frame in the first and last frame. The outline of the pool never changes. Apart from the work inside the walls, the courtyard floor, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge. This is one pool in one walled courtyard and the only one in view. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 5 — DOLAR  ·  40,0 – 48,0 sn  ·  16:20 → 18:20  ·  rejim B

### 📸 GÖRSEL PROMPT (G5)

```
Photorealistic documentary construction photograph — Scene 5 of 7. Vertical time-lapse of one abandoned swimming pool rebuilt as a stone-edged garden pond inside a walled courtyard, seen from a balcony above it; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod clamped to the balcony rail of the house on the south side, lens 6.0 metres above the courtyard floor, 5.0 metres from the centre of the pool, bearing 0 degrees, tilt 40 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single stone-edged garden pond in the footprint of the old pool, with a three-step cascade in its far right corner, a gravel beach at its near end and planted pockets along its far rim. AT THIS STAGE: the far rim is planted. Ferns, sedges and a low creeping ground cover have been set into all eight pockets between the boulders and bedded in dark bark mulch that runs in a band behind the stone, and the olive has been pruned so its canopy is lighter and opens over the left of the courtyard. Six low matt-black garden lamps stand in the ground along the right-hand path, their heads dark, their cable tucked under the rim stones. The basin below is still dry: matte black liner, pale gravel at the near end, the cascade steps dry. A filling hose has been dragged in through the gate and hooked over the far rim, and empty pots and emptied soil bags are stacked on the cart by the gate.

SITE / BACKGROUND: A single walled courtyard fills the frame, its floor laid with weathered limestone flagstones, and one rectangular pool with rounded corners lies in the middle of it. One old olive tree stands on the left, the only tree inside the walls, its trunk rising from the flagstones at about nine percent of frame width and its canopy across the upper left corner. The rear wall runs straight across the frame, dry stone under worn lime plaster, capped with a flat stone coping level at about seventy-nine percent of frame height, with one arched niche set into it right of centre and a gate in the left-hand wall beside it. Beyond the coping a terraced hillside of olive rows and dry grass climbs to the top of the frame. Apart from the work inside the walls, the courtyard, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge.

THE TIME MOMENT: Late afternoon, everything in place and the basin still dry.

COMPOSITION: Vertical 9:16. The arched niche sits right of centre, between fifty-eight and sixty-seven percent of frame width and between sixty-eight and seventy-five percent of frame height; it spans about 99 pixels of frame width — one eleventh — and keeps that width and position in every frame. The near rim of the pool crosses at about thirteen percent of frame height and the far rim at about fifty-two percent, and nothing that proves progress falls into the right eighth or the bottom eighth of the frame. A green planted band runs along the far rim just under the wall, and the dry black basin still holds the frame between thirteen and fifty-two percent of frame height.

LIGHTING: Sun azimuth 257 degrees, elevation 22 degrees, low afternoon light from the left, long shadows falling east, toward the right of the frame, the rear wall and the boulders warm and the basin floor in shadow. The sun stays outside the frame for the whole shot; its only sign is the shadows. Mid-September, the end of a dry summer: the hillside grass bleached, the olive canopy freshly pruned and lighter.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows on the courtyard floor, the cloud shadows on the wall, the water, the crew and the cart all move at the same accelerated speed. Two hours pass across this shot: shadows sweep across the flagstones and every moving thing smears into heavy motion blur. Nothing in the frame moves at normal speed.

ACTIVITY: The crew set the last fern into its pocket and spread a fresh cartload of bark mulch along the planted band, then hook the filling hose over the far rim; the cart is pushed out through the gate stacked with empty pots and cut branches. Crew register only as faint soft motion streaks along the planted band and at the gate, never as sharp figures.

SITE TEXTURE: Dark bark mulch banded along the far rim with soil crumbs spilled over the boulders; pale cut ends where the olive was pruned and leaf debris under it; matte black liner and pale raked gravel in the dry basin; lichen patches on the dolomite; a hose drag mark through the dust across the flagstones; emptied soil bags stacked on the cart.

PHYSICS: Each plant is bedded in soil that rests in a pocket between the boulders and the mulch lies packed over it; the six lamp spikes are planted in the ground along the path with their cable tucked under the rim stones; the filling hose is hooked over the far rim and hangs down the inside face of the stone, held by its own bend over the boulder; the cart stands on its wheels on the flagstones.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The walls, the coping, the arched niche, the olive trunk and the hillside never change shape, position, size or spacing; the outline of the pool never changes. Nothing already built is removed, moved or resized; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, container, panel, facade, hoarding, signage, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G5 → G6)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Two hours pass across the last of a September afternoon. Everything in this shot is time-lapsed at the same rate: the shadows run out long to the right and then dissolve as the sun goes behind the west wall, the light on the hillside grades from gold to a flat even shade, and every moving thing is smeared into a blur. First water runs from the hose and a sheet of it spreads out across the black floor from the deep end, and the liner goes from matte to a dark mirror wherever the water reaches. Then the level climbs the inside faces of the boulders, past the first, the second and the third stone of the near rim, the gravel beach goes under at its lower edge, and the reflection of the rear wall, the arched niche and the olive canopy opens out across the surface and grows as the water rises. Then the cascade starts and a thin sheet comes down all three steps, sending slow rings out across the pond. Finally the hose is lifted out and coiled onto the cart at the gate, and the surface settles until it is still. The walls, the coping, the niche, the olive trunk and the hillside do not change. The sky stays out of the frame; its only signs are the light that grades across the courtyard floor, the cloud shadows that sweep over the wall and across the stone, and the light the water holds.

The camera does not move at any point. The framing is identical in the first and last frame. The courtyard walls, the wall coping, the arched niche, the olive trunk and the terraced hillside stay exactly where they are, at exactly the same size and shape, for the whole shot. The wall coping stays level at exactly seventy-nine percent of the frame height. The arched niche occupies exactly the same width of the frame in the first and last frame. The outline of the pool never changes. Apart from the work inside the walls, the courtyard floor, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge. This is one pool in one walled courtyard and the only one in view. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 6 — YANAR  ·  48,0 – 56,0 sn  ·  18:20 → 18:30  ·  rejim A

### 📸 GÖRSEL PROMPT (G6)

```
Photorealistic documentary construction photograph — Scene 6 of 7. Vertical time-lapse of one abandoned swimming pool rebuilt as a stone-edged garden pond inside a walled courtyard, seen from a balcony above it; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod clamped to the balcony rail of the house on the south side, lens 6.0 metres above the courtyard floor, 5.0 metres from the centre of the pool, bearing 0 degrees, tilt 40 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single stone-edged garden pond in the footprint of the old pool, with a three-step cascade in its far right corner, a gravel beach at its near end and planted pockets along its far rim. AT THIS STAGE: the pond is full. Water stands to the third boulder of the near rim and reaches the lower edge of the gravel beach, and the surface is dark and still enough to carry the rear wall, the arched niche and the olive canopy as a reflection. The cascade is running and a thin sheet of water comes down all three steps, sending slow rings out across the pond. The planted band along the far rim is watered and dark and the six lamps along the path are still dark. The filling hose has been lifted out and is being coiled onto the cart at the gate; the flagstones have been swept and the mixing tub, the pots and the bags have gone out.

SITE / BACKGROUND: A single walled courtyard fills the frame, its floor laid with weathered limestone flagstones, and one rectangular pool with rounded corners lies in the middle of it. One old olive tree stands on the left, the only tree inside the walls, its trunk rising from the flagstones at about nine percent of frame width and its canopy across the upper left corner. The rear wall runs straight across the frame, dry stone under worn lime plaster, capped with a flat stone coping level at about seventy-nine percent of frame height, with one arched niche set into it right of centre and a gate in the left-hand wall beside it. Beyond the coping a terraced hillside of olive rows and dry grass climbs to the top of the frame. Apart from the work inside the walls, the courtyard, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge.

THE TIME MOMENT: The last minutes of daylight, the pond full and the work finished.

COMPOSITION: Vertical 9:16. The arched niche sits right of centre, between fifty-eight and sixty-seven percent of frame width and between sixty-eight and seventy-five percent of frame height; it spans about 99 pixels of frame width — one eleventh — and keeps that width and position in every frame. The near rim of the pool crosses at about thirteen percent of frame height and the far rim at about fifty-two percent, and nothing that proves progress falls into the right eighth or the bottom eighth of the frame. The water holds the brightest area in the lower half of the frame between thirteen and fifty-two percent of frame height and carries the only piece of sky in the picture as a reflection.

LIGHTING: Sun azimuth 275 degrees, elevation 2 degrees below the horizon, the sun down behind the west wall, no direct light left in the courtyard, an even warm afterglow along the wall coping and the hillside and a cool shade below. The sun stays outside the frame for the whole shot; its only sign is the fading warm band along the coping. Mid-September, the end of a dry summer: the hillside grass bleached, the olive canopy freshly pruned.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light on the wall coping, the colour the water carries, the falling sheet on the cascade and the rings it sends out all move at the same accelerated speed. Ten minutes pass across this shot: the warm band drains off the coping and the moving water smooths into a soft blur.

ACTIVITY: The pump lifts a thin sheet of water over the top step of the cascade and the rings it sets off cross the pond and fade against the gravel beach; the crew coil the filling hose onto the cart at the gate and push it out. Crew register only as faint soft motion streaks at the gate beside the cart, never as sharp figures.

SITE TEXTURE: A dark still water surface carrying the reflection of the wall and the olive; a wet band on the boulders just above the waterline; pale gravel going under at its lower edge; a thin film of water on the three cascade steps; dark watered mulch along the planted band; lichen patches on the dry dolomite; a swept flagstone floor with a last hose drag mark in the dust.

PHYSICS: The water bears on the liner and stands against the inside faces of the boulders, and the boulders bear on their mortar pads on the coping; the cascade steps are bedded one on the next on their shelf of stone, and the thin sheet rests on each step before it falls to the next; the filter box is seated on the flagstones under the niche; the cart stands on its wheels at the gate.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The walls, the coping, the arched niche, the olive trunk and the hillside never change shape, position, size or spacing; the outline of the pool never changes. Nothing already built is removed, moved or resized; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, container, panel, facade, hoarding, signage, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT (G6 → G7)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Ten minutes pass across the end of the same September evening. Everything in this shot is time-lapsed at the same rate: the warm band drains off the wall coping, the light on the hillside and the colour the water carries fade together from gold to deep blue, and the falling water smooths into a soft blur. First the cart is pushed out through the gate and the gate leaf swings shut behind it, and the courtyard is left to itself. Then the six lamps along the right-hand path come alight one after another, their warm pools opening on the stone rim, on the ferns along the far rim and on the near edge of the water, and the still surface doubles each of them. Then the blue deepens and the warm points hold steady against it. Finally, for the last seconds, nothing changes but the thin sheet coming down the three cascade steps and the slow rings it sends out across the mirror. The walls, the coping, the niche, the olive trunk and the hillside do not change. The sky stays out of the frame; its only signs are the light that grades across the courtyard floor, the cloud shadows that sweep over the wall and across the stone, and the light the water holds.

The camera does not move at any point. The framing is identical in the first and last frame. The courtyard walls, the wall coping, the arched niche, the olive trunk and the terraced hillside stay exactly where they are, at exactly the same size and shape, for the whole shot. The wall coping stays level at exactly seventy-nine percent of the frame height. The arched niche occupies exactly the same width of the frame in the first and last frame. The outline of the pool never changes. Apart from the work inside the walls, the courtyard floor, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge. This is one pool in one walled courtyard and the only one in view. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🌟 USTA KARE — G7  ·  S6'nın HEDEF karesi  ·  kapak kaynağı

### 📸 USTA KARE PROMPT (G7)

```
Photorealistic documentary construction photograph — master frame G7, the target frame of the last shot. Vertical time-lapse of one abandoned swimming pool rebuilt as a stone-edged garden pond inside a walled courtyard, seen from a balcony above it; a construction-progress photograph from a fixed 24 mm site camera.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod clamped to the balcony rail of the house on the south side, lens 6.0 metres above the courtyard floor, 5.0 metres from the centre of the pool, bearing 0 degrees, tilt 40 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a single stone-edged garden pond in the footprint of the old pool, with a three-step cascade in its far right corner, a gravel beach at its near end and planted pockets along its far rim. AT THIS STAGE: the courtyard is finished and empty. The pond stands full to the third boulder of the near rim, its surface still, carrying the rear wall, the arched niche, the olive canopy and six warm points of light as a reflection. The six low lamps along the right-hand path are alight, steady and warm, and their light lies on the stone rim, on the ferns along the far rim and on the near edge of the water. The cascade runs down all three steps and its rings spread across the pond. The gate in the left-hand wall is shut, the flagstones are swept clean, and the flat cover stone is down over the filter box under the niche.

SITE / BACKGROUND: A single walled courtyard fills the frame, its floor laid with weathered limestone flagstones, and one rectangular pool with rounded corners lies in the middle of it. One old olive tree stands on the left, the only tree inside the walls, its trunk rising from the flagstones at about nine percent of frame width and its canopy across the upper left corner. The rear wall runs straight across the frame, dry stone under worn lime plaster, capped with a flat stone coping level at about seventy-nine percent of frame height, with one arched niche set into it right of centre and a gate in the left-hand wall beside it. Beyond the coping a terraced hillside of olive rows and dry grass climbs to the top of the frame. Apart from the work inside the walls, the courtyard, the walls and the hillside carry only stone, plaster, dust and dry grass from edge to edge.

THE TIME MOMENT: Blue hour on the first evening, the lights on and nobody left in the courtyard.

COMPOSITION: Vertical 9:16. The arched niche sits right of centre, between fifty-eight and sixty-seven percent of frame width and between sixty-eight and seventy-five percent of frame height; it spans about 99 pixels of frame width — one eleventh — and keeps that width and position in every frame. The near rim of the pool crosses at about thirteen percent of frame height and the far rim at about fifty-two percent, and nothing that proves progress falls into the right eighth or the bottom eighth of the frame. The lit water holds the lower half of the frame between thirteen and fifty-two percent of frame height and the six warm points and their reflections make the brightest marks in the picture.

LIGHTING: Sun azimuth 277 degrees, elevation 4 degrees below the horizon, blue hour, no direct light, an even deep blue sky light over the courtyard with the last warm trace above the hillside, and six warm lamp pools on the stone and the water. The sun stays outside the frame for the whole shot; its only sign is the fading light above the hillside. Mid-September, the end of a dry summer: the hillside grass bleached, the olive canopy freshly pruned.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the light on the wall coping, the colour the water carries, the falling sheet on the cascade and the rings it sends out all move at the same accelerated speed. Ten minutes pass across this shot: the warm band drains off the coping and the moving water smooths into a soft blur.

ACTIVITY: The pump lifts a thin sheet of water over the top step of the cascade and the rings it sets off cross the pond and fade against the gravel beach, and the six lamps hold a steady warm glow with their reflections holding under them. No people are present in the courtyard.

SITE TEXTURE: A still dark water surface carrying the reflection of the wall, the olive and six warm points; a wet band on the boulders above the waterline; a thin film of water on the three cascade steps; pale gravel going under at its lower edge; dark watered mulch along the planted band; lichen patches on the dry dolomite; a faint sheen on the stone where the cascade splashes and a pale efflorescence stain on the plaster under the niche; a swept flagstone floor.

PHYSICS: The water bears on the liner and stands against the inside faces of the boulders, and each boulder bears on its mortar pad on the stone coping; the cascade steps are bedded one on the next on their shelf of stone; the six lamp spikes are planted in the ground along the path with their cable tucked under the rim stones; the flat cover stone rests over the filter box.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms or drifts; the framing is identical from the first frame to the last. The walls, the coping, the arched niche, the olive trunk and the hillside never change shape, position, size or spacing; the outline of the pool never changes. Nothing already built is removed, moved or resized; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, container, panel, facade, hoarding, signage, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur.
Output: 9:16, 4K, no text, no watermark.
```

---

# 🎶 MÜZİK

### 🎶 MÜZİK PROMPTU

```
Instrumental score for a 61-second vertical construction time-lapse: a 56-second scene block of
seven shots of equal length (8.0 seconds each), followed by a 5-second end card. No lyrics, no voice,
no melody line, no traditional song structure.

Genre: warm Mediterranean ambient — dry stone, water, cicada air, one warm tone that arrives only at
the end. Tempo: 120 BPM, strict and bar-aligned; one bar is 2.0 seconds, every shot is exactly four
bars, and every cut lands exactly on the first beat of a bar (cuts at 8.0, 16.0, 24.0, 32.0, 40.0 and
48.0 seconds). Because the cuts are evenly spaced, the arc is carried by the layers and the dynamics,
not by the cut rhythm: every eight-second block must sound different from the one before it.

Layers (one added roughly every shot; the liner block thins the stack):
1. 0.0-8.0     a dry low pulse on the first beat of every bar under a real courtyard bed — a pump
               running somewhere off frame, water falling into a drain, cicadas far off
2. 8.0-16.0    a muted stone-and-metal percussion pattern enters — shovel, bucket, a bolt coming free
3. 16.0-24.0   the stack THINS to the pulse and a single low drone as the liner goes down; the site
               bed almost disappears (this is the moment the pool stops being a pool)
4. 24.0-32.0   the percussion returns harder and lower as the stone rim is laid — one stone per bar
5. 32.0-40.0   a soft high texture enters over the drone as the planting goes in; the percussion
               softens to brushed stone
6. 40.0-48.0   a slow rising figure in steps as the water climbs; at 46.0 the cascade enters as real
               falling water and stays
7. 48.0-56.0   the stack pares back to the drone and the water, then at 53.0 a single warm sustained
               chord opens with the first lights and is held
56.0-61.0      end card: everything resolves and decays; the last 2.0 seconds carry only the cascade

Dynamic map across 61 seconds:
  0.0-2.0    silence from the score — only the site's own ambience: still water, cicadas, a pump
  2.0-8.0    layer 1 alone; the water level falling under it
  8.0-16.0   layer 2 enters; buckets, a pressure washer far back in the mix
  16.0-24.0  near silence from 18.0: the pulse and the drone only, one dry rustle of rolled rubber
  24.0-32.0  percussion back, stone on stone, one hit per bar
  32.0-40.0  brightens; soil, mulch, the trolley, distant birds
  40.0-48.0  the rising figure; running water enters at 46.0 and never leaves
  48.0-53.0  pared back to water and drone
  53.0-56.0  the warm chord opens with the lights and is held
  56.0-61.0  end card resolve and decay to the cascade

Reference feel: [two real composers — no quotation, no imitation of any specific work]
Phone-speaker rule: every sub-bass element below 150 Hz is doubled by its own upper harmonics at
roughly 100, 150 and 200 Hz so the fundamental is implied rather than required; the low end is
never the only carrier of the weight.
```

⭐ **SES YATAĞI SAHNE SAHNE** [MUZIK_VE_KAPAK §1.3]: S0 pompa + boşalan su · S1 kürek, kova, cıvata, basınçlı su ·
S2 kauçuğun açılışı (film boyunca EN SESSİZ an) · S3 taş üstüne taş, çakıl · S4 toprak, makas, saksı · S5 dolan su,
sonra çağlayan · S6 yalnız çağlayan + akşam böcekleri. ⛔ Martı/kuş sayısı ve hareketi GÖRÜNTÜYE yazılmaz.

---

# 📣 PAKETLEME — İNGİLİZCE

```
TITLES (≤40 chars)
1. A Pool Nobody Had Touched in Years      (34)   ⭐ kanca merak, bedeli söylemez
2. One Day Inside a Walled Courtyard       (33)
3. The Pool That Became a Garden           (29)   ⚠️ dönüşü söyler — spoiler bütçesini zorlar

DESCRIPTION
A walled courtyard, one camera on the balcony, seven locked-off shots: the green water drawn down,
the basin scraped back to its tile, the tile buried under a liner, a stone rim closed around it,
eight pockets planted, the water brought back to the third stone, and the first evening the lights
come on. The pool is still there — you just cannot swim in it any more.
#timelapse #beforeandafter #pond #gardendesign #landscaping #courtyard #stonework #satisfying
#renovation #water #restoration

This video was generated with AI. It does not document a real project.

PINNED COMMENT
How this actually works: an old tiled pool makes a good pond shell because the structure is already
there — the work is in what goes over it. The basin is drained and scraped back to sound tile, sharp
cracks are struck flush so nothing can cut the lining, and a soft protective layer goes down before
a single rubber sheet is laid in one piece, pushed into the corners and folded rather than cut. The
sheet is held at the top by the weight of the coping stones, which is why the rim is laid last and
why nothing is trimmed until the water is in. Planting pockets sit above the waterline in soil, not
in the pond, and the pump and filter live outside the basin under a cover stone.

⛔ LOOP İDDİASI YOK · spoiler bütçesi [MUZIK_VE_KAPAK §3.3]: başlık bedeli (mavi seramiğin gömülmesi) SÖYLEMEZ;
   açıklama gömmeyi anar ama merdivenin sökülüşünü ve ışıkları anmaz — TEK CÜMLE TESTİ: HAYIR.
⭐ TÜRKÇE ALTERNATİF (kanal ikinci dilde yayınlarsa): başlık "Yıllardır Kimsenin Dokunmadığı Havuz" ·
   kapak yazısı "AYNI HAVUZ MU?" · açılış kancası "BURASI KURTULUR MU?" — üçü de KURGUDA eklenir, promptta değil.
⭐ ÖLÇÜM (yayından sonra, YAYIN_PLANI §6): "önce–sonra havuz videoları yayılır" bir VARSAYIMDIR, veri değil.
   Dış plandan devralınan izlenme sayıları (Mr.Heang · Havesomevision · Milly · thep00lguy) DOĞRULANMADI;
   bu depoda ders sayılmazlar, yalnız varsayım olarak kayıtlıdır [AGENTS §6]. Shorts'ta üç metrik BİRLİKTE
   okunur — izlemeye devam edenler · ortalama izlenme süresi · ortalama izlenme yüzdesi — ve 7,0 sn'lik
   sonuç ekranı (tutuş + kart) tutunma eğrisinde 49–61 sn aralığından okunur [A1-a].
```

---

# 🔒 MASTER LOCK

```
Photorealistic documentary construction photography. Locked-off tripod, one continuous time-lapse
shot, no camera movement of any kind. Physically accurate daylight. Real stone, real dust, real water,
real lime plaster. Natural motion blur on moving people and on the cart. No architectural render look,
no CGI aesthetic, no game engine look, no miniature look, no tilt-shift. Every frame should look like
a real photograph taken from a camera that has been clamped to the same balcony rail all day.
```

---

# 🚦 ÜRETİM ÖNCESİ DURUM

```
□ Konsept kapısı            ✅ dört test · dış üretim planı depo kurallarına göre yeniden yazıldı (16.09.2026)
□ Kanal tezi kapısı         ✅ kaybolan: havuzun havuz olması (mavi seramik + merdiven + hacim)
□ Kart seçimi               ✅ yeni tip (bahçe göleti restorasyonu) + yeni saha (duvarlı avlu) — ikisi de
                               YAPI_TIPI_KARTLARI ve SAHA_VE_IKLIM'e ÖLÇÜMDEN SONRA yazılır
□ Değişmezler               ✅ dört kutu · D_kenar / D_eksen [DERS 38] · ⛔ tilt ≠ 0 beyanı + kendi formülü
□ Aşama merdiveni           ✅ 7 satır · üç zorunlu satır · mevsim yok (gün) · VİNÇ YOK
                            ⛔ DÜZ IZGARA (7 × 8,0) — proje sahibinin kilidi · gerekçe + kabul edilen risk +
                               karşı kanıt notu yazıldı [§2.6 · DERS 24 · 44]
□ Kare tablosu              ✅ 8 görsel · ara kare YOK · tek ışık günü 06:20 → 18:30 (12 sa 10 dk)
□ Promptlar                 ✅ 8 görsel + 7 I2V · T2V yok · her sahne tek 8,0 sn klip
□ Kinetik paket             ✅ THE DARK ROCK'tan dokuz araç + yansıma (onuncu) · ⛔ kamera hareketi YOK
□ Müzik + kapak + paket     ✅ 120 BPM (4 ölçü/sahne) · THE_HIDDEN_OASIS_KAPAK.md · İngilizce
□ QA_SPEC                   ✅ THE_HIDDEN_OASIS_QA_SPEC.md · FİNAL KARE KANITI satırı
□ Prompt kapısı             ✅ koşuldu 16.09.2026: python3 araclar/prompt_kontrol.py dikey_shorts/THE_HIDDEN_OASIS/THE_HIDDEN_OASIS_DIKEY_TIMELAPSE.md
                            → FIX ×2, ikisi de beyanlı (kutu seti ölçülmedi · süreler eşit) · BLOCK 0
⛔ ARAÇ KAPISI              KOŞULMADI — sekiz ölçüm (ARAC_KARTLARI §4) · günlük §0 · kutu ≥ 9,0 şartı
⛔ ÖN GÖRSELLEŞTİRME        ÇİZİLMEDİ — balkon · avlu · havuz · duvar + niş · zeytin · teras; usta kareden önce
⛔ ÖLÇÜLMEMİŞ TÜRETİM       yüzdeler ve pikseller tilt −40° formülünden TÜRETİLDİ, ölçülmedi (Değişmezler kutusu)
⛔ Üretim günlüğü           THE_HIDDEN_OASIS_URETIM_GUNLUGU.md açıldı, ⛔ BOŞ
```

---

## 📎 AJAN KARARLARI — proje sahibinin onayına açık (16.09.2026)

```
① KAPAK KARTI       dış plan kartsız 56,0 sn istiyordu → depo formatı gereği 5,0 sn kart eklendi (61,0 sn).
                    Sahip kartsızlığı seçerse: TESLİM YAPISI'na gerekçeli beyan yazılır, kapak yalnız
                    yüklenen Shorts küçük resmi olur.
② REJİM             S0–S5 rejim B (2 saat), S6 rejim A (10 dakika). Gerekçe: 1200×'te insan silinir ve iz
                    bırakır — referans havuz timelapse'lerinin gerçek görünümü budur; 100× yalnız son
                    sahnede, ışığın yerleşmesi için. Sahip "işçiler net görünsün" derse bütün film A'ya
                    iner ve ışık günü 1 saate düşer: gölge süpürmesi kaybolur, ③ merceği zayıflar.
③ S1'İN YÜKÜ        çatlak onarımı S2'den alınıp S1'in son 2 saniyesine verildi; S2 artık tek iş taşıyor
                    (tesisat + kaplama).
④ SİLUET AİLESİ     yeni aile "ZEMİN" önerildi (yukarıdan avlu). Sahip KÜTLE'ye yazmayı seçerse
                    YAYIN_PLANI §3 değişmez, yalnız bu filmin satırı güncellenir.
⑤ KAMERA KARTI      tilt ≠ 0 istasyon KAMERA_ISTASYONU'nda YOK. Kılavuza yeni alt kart borcu doğdu;
                    ölçülmeden yazılmaz — bu film onun ilk koşusudur.
```
