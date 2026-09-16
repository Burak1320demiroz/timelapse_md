# 🏗️ THE_OLD_ROAD — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **15 × 8,0 sn = 120,0 sn** | Kapak kartı: **5,0 sn** | Toplam: **125,0 sn**
Prompt yapısı: ⭐ **15 sahne → 16 görsel (G0…G15) + 15 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G8** · ara kare YOK
Yapı: **itmeli (incremental launching) beton kutu kesitli viyadük — 420 m, 7 açıklık, 5 ayak** (yeni tip · `YAPI_TIPI_KARTLARI` §10 şablonu; §3 köprü ve §6 yol kartlarından uyarlandı) · Saha: **dağ / eğim vadisi — melez ormanı yamaçlar, nehir, eski taş kemer köprü** (`SAHA_VE_IKLIM_KARTLARI` §3.4)
Zaman yayı: **627 gün ≈ 20,6 ay (10 Mart yıl 1 → 26 Kasım yıl 2) → 120 saniye** · film mertebe anlatır: *"yaklaşık iki yıl, iki kış"* [P1-c]
Işık günü: **05:05 → 18:35 · Σ = 9 × A (10 dk) + 6 × B (2 sa) = 13,5 saat ≤ 14** — kesmede ışık atlamaz [§2.7 ①]
⚠️ **ÜSLUP BEYANI:** 20 aylık takvim TEK BİR GÜNÜN ışığına sıkıştırılmıştır. Bu bilinçli bir kurgudur; ne planda ne pakette "tek günde çekildi" denir.
Kamera mimarisi: **MAIN STATION** — tek istasyon, 15 sahne + usta kare (detay istasyonu YOK) [`KAMERA_ISTASYONU` §1 · DERS 52]
Izgara: ⛔ **DÜZ — 15 × 8,0** · sahip beyanı (16.09.2026) · karşı kayıt ve kabul edilen risk §AŞAMA MERDİVENİ'nde
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 16.09.2026 — "bu filmi yapalım"
Havuz kaydı: `apexait/YAYIN_PLANI.md` §5 #4 THE OLD ROAD · siluet ailesi **YATAY**

_"On dört virajda dolanan ışık, iki dakikada tek düz çizgiye dönüşür."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     15 sahne × 8,0 sn                       = 120,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn                           =   5,0 sn   ← SAHNE DEĞİL, ayrı denetlenir
               ⛔ KONUM: teslimin SON 5 saniyesi (120,0–125,0) [A1-b]
──────────────────────────────────────────────────────────────
TOPLAM                                                     125,0 sn
BÖLÜM DOSYASI   BOLUM_1 = S0–S7 (0–64,0)  ·  BOLUM_2 = S8–S14 + USTA KARE (64,0–120,0)
QA BİRİMİ       FİLM (tek master × 12 mercek)   (2/4 dk: FİLM · 6/8 dk: BÖLÜM — iki yarım master, SPEC künyesinde PART GRID)
```

⛔ Kapak kartı **usta kareden (G15)** türetilir ve üstüne **İngilizce başlık** dizilir: `THE OLD ROAD` (`THE_OLD_ROAD_KAPAK.md`).
⚠️ S14'ün son ≥2,0 sn'lik TUTUŞU final kanıtıdır (`QA_SPEC` §1); kart hareketsiz ve yazılıdır — iki ayrı iş.
⭐ Uç ekranı YALNIZ karta (120,0–125,0) konur; S13–S14'ün üstü kapanmaz.

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Eski yolun on dört virajla indiği derin vadiye, karşıdan karşıya İTİLEN 420 m'lik düz bir viyadük kurulur
         ve trafik virajlardan çıkıp bu çizgiye geçer. (Video başlamadan önce de var olan iş: güzergâhı seçmek,
         kayaya oturan beş ayağı ölçmek, vadinin iki yakasına yaklaşımı kazmak.)
DİRENÇ   ① DERİNLİK — orta ayak vadi tabanından 60 m; ayaklar tırmanır kalıpla kendi kendine yükselir
         ② BOŞLUK — tabliye kaldırılmaz, İTİLİR; çelik burun ayaklar arasında desteksiz ilerler
         ③ NEHİR — kar erimesi seli şantiyenin geçici geçişini koparır ve itmeyi durdurur
         EKRANDA NASIL [P1-b]:
           S2  · beş ayak tırmanır kalıpla yükselir; pompa hattı gövdede, aşağıda eski yolda trafik sürer
           S4–S6 · burun boşlukta ayaktan ayağa geçer; her itmede gövdenin ucu bir sonraki mesnede oturur
           S7–S9 · nehir kabarır, son kamyon geçişten çıkar, sel geçişi götürür, çamur çizgisi ve sürüntü kalır
BEDEL    ESKİ YOLUN TRAFİĞİ. G0'da on dört virajda araçlar dolanır (şafakta far izleri), taş köprüden geçer.
         S14'te son araç virajlardan çıkar ve akış viyadüğe geçer; kıvrımlar BOŞ ama OKUNUR kalır — asfalt bandı,
         korkuluk ve yamaçtaki çizgi G0'daki gibi görünür. Kaybolan yol değil, üstündeki hayattır.
         ⛔ Bedel taş köprünün ayrıntısına yüklenmez: taş köprü 320 px'lik önizlemede ≈11 px'tir; anlamı
         virajların geometrisi + trafiğin varlığı/yokluğu birlikte taşır.
         Okuma bilinçli: "doğa bozuldu" değil, "vadi bir saat kazandı, bir yol kaybetti".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            eski yolun trafiği ve taş köprünün işlevi                       ✅
  □ kadrajda görünüyor mu?    evet — iki yamaçta viraj bandı, sabit kamera, G0 ↔ G15 karşılaştırması  ✅
  □ cevap "zaman geçiyor" mu? hayır                                                            ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ Donmuş karede: beş ayak, yarı itilmiş beton gövde ve önünde boşlukta duran çelik burun
                           → "köprü karşıya geçiyor, şu kadar kaldı" bir saniyede (burun ucu hangi ayakta, sayılabilir).
② KİNETİK BAĞIMSIZLIK   ✅ Sabit kadrajda: gövde sağa kayar, kalıplar tırmanır, su kabarıp çekilir, far izleri
                           virajdan viyadüğe geçer — metinsiz, anlatıcısız.
③ BAŞLIK ŞEMASI         ✅ Kapak: "THE OLD ROAD" (3 kelime) · yayın başlığı: "They Pushed a Bridge Across This Valley"
④ OMURGA CÜMLESİ        traffic still winds → rims cut open → five piers rise → yard and nose ready →
   [P1-k]                first push clears pier one → segment added, push repeats → deck reaches mid-valley →
                         river rises, work withdraws → flood takes the crossing → water drops, damage shows →
                         push resumes toward last span → nose lands, concrete arrives → nose and props come down →
                         surface, rails and lights → traffic moves, hairpins empty
                         (15 vuruş, her biri ≤4 kelime; merdiven bundan türedi)
```

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera  ② ESKİ TAŞ KEMER KÖPRÜ — vadi tabanı, %34,2 · x %44,4 · 64 × 21 px,
                          16 karede birebir (kanıt nesnesi)  ③ sol çapa: tek şapel (%61,9 · x %28,1)
                          ④ sağ çapa: tek kaya kulesi (%45,9–57,5 · x %89,7)  ⑤ eski yolun on dört virajı,
                          iki yamaçta aynı çizgi — ve HER KAREDE trafik  ⑥ tek parça beton gövde, yalnız UZAR:
                          A1 → P1 → P2 → P3 → (dur) → P5 → A2  ⑦ ⛔ tabliye KALDIRILMAZ, İTİLİR
                          ⑧ ayrı insan figürü yok (streak cümlesi · rejim)  ⑨ ikiz zirve silüeti %82,4
P1.5 · fırsat buldukça   melez rengi (yeşil → altın → çıplak) · kar çizgisinin yamaçta inip çıkması ·
                          nehrin rengi ve debisi · beton yaşı (yeni kesit koyu, eskiler açık) · çamur çizgisi
SPEC · yalnız belge      420 m · 7 açıklık (60 + 5 × 60/75 + 60) · ayak boyları 30/48/60/50/32 m · tabliye
                          üstü +64 m · kutu kesit derinliği 4 m · burun 45 m · h 80 m · D 380 m · azimut/yükseklik
```

**Malzeme kimliği (her promptta):** *grey formed concrete with horizontal form-tie bands · a darker pour joint on the first-cast segment · galvanised climbing formwork · a rust-red steel launching nose · pale gravel haul road · dark wet river gravel* — korpus cümlesi [DERS 34 · 42]: yapı "otoyol görseli" değil, ŞANTİYE fotoğrafı; viyadük tek, betonu ham ve lekelidir.

**İnsan kararı:** insansız saha DEĞİL. Kabinli makineler + ekip streak cümlesi; B kliplerinde silinir, A kliplerinde küçük ve bulanık kalır. ⛔ "No people are present" YAZILMAZ [DERS 33].

**Vinç / kaldırma kararı [DERS 8 · 22 · 46 · 57]:** ⛔ **BETON GÖVDE HİÇBİR KAREDE HAVADA TAŞINMAZ** — ya döküm yatağında ya ayak mesnetlerinde durur, ilerleme krikoyladır. Vinç VARDIR ama yalnız iki yerde: döküm alanında **mobil vinç** (donatı kafesi, kalıp panosu, burun parçaları — kanca her karede YÜKLÜ ve düşey, bom zirve silüetinin ALTINDA) ve nehir düzlüğünde **paletli vinç** (geçici desteği kurar S6, söker S12). Ayaklarda vinç yoktur: tırmanır kalıp kendi krikosuyla, beton pompa hattıyla çıkar.

**Korpus kararı [DERS 55]:** "viaduct" korpusu otoyol dizisidir. Her SITE / BACKGROUND ve her I2V: *"the valley carries exactly one new elevated crossing and one existing stone arch bridge; no other bridge, mast or tower stands anywhere from edge to edge."* Günlük §2'ye sayım sütunu (viyadük = 1 · taş köprü = 1).

**İki yüzey kararı [DERS 51 · 53]:** iş yüzeyi adıyla ve yüzdesiyle yazılır ("the launched deck top at forty-five percent of frame height"). Eski taş köprü her karede POZİTİF BOŞ: *"the stone arch bridge carries only light traffic; its deck stays bare of plant."* ⛔ Ağır makine taş köprüden geçmez — kapasitesi bilinmez, film varsaymaz.

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0,
                 yani en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp [A7-b]; kutu tam 8,0 ise kırpma payı YOK).
                 ⛔ Tavan < 8,0 ise plan ara kareye BÖLÜNMEZ (sahip kararı 15.09.2026): araç değişir ya da
                 karar proje sahibine döner.
                 ⭐ BU FİLME ÖZEL DOKUZUNCU ÖLÇÜM: İTME TESTİ — araç uzun bir gövdeyi kadraj içinde yatay
                 kaydırabiliyor mu, yoksa hedefte kopyalayıp kaynağı siliyor mu [DERS 57 mekanizması].

┌─ KAMERA İSTASYONU (ANA · tek istasyon) ─────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 · tam kare YATAY (36 mm kare eni,  │
│               16:9 kırpma → kare boyu 20,25 mm)                               │
│ yükseklik     h = +80,0 m (nehir kotundan) — vadi ağzındaki kaya mahmuzunun tepesi │
│ mesafe        D_eksen = 380 m (viyadük ekseni) · D_kenar = 190 m [DERS 38]      │
│ bakış açısı   0° (kuzey · vadi yukarı) · tilt 0° · roll 0°                     │
│ sabitleme     "bolted to the flat top of a rock spur, absolutely zero movement" │
│ ⛔ HESAP (KILAVUZ_REHBERI §2.8 · f=24 · yatay · yüzde ALT kenardan):            │
│    yüzde(y) = 50 + 118,5·(y − 80)/D        yüzde(x) = 50 + 66,7·x/D            │
│    px/m = 1280/D → D=380'de 3,37 px/m · kadraj 570 m × 320 m                   │
│    nehir / P3 kaidesi  y=0     → %25,1  ✓ alt çeyreğin üstünde                 │
│    P2 kaidesi %28,8 · P4 %28,2 · P1 %34,4 · P5 %33,8                           │
│    tabliye altı (+60)          → %43,8 · ⭐ TABLİYE ÜSTÜ (+64) → %45,0          │
│    lamba direkleri (+76)       → %48,8  (S13'ten sonra)                        │
│    ufuk (tilt 0)               → %50,0 = GÖZ ÇİZGİSİ — kaya kulesinin alt üçte  │
│                                  birinden geçer (nesneye bağlı çapa)           │
│    taş köprü (D 600)           → %34,2 · x %44,4 · 64 × 21 px ⭐ kanıt nesnesi   │
│    şapel (D 700)               → %61,9 · x %28,1 · çan kulesi 33 px (SOL çapa)  │
│    kaya kulesi (D 420)         → %45,9–57,5 · x %89,7 · 122 px (SAĞ çapa)       │
│    ikiz zirve (3 km)           → %82,4 = TAÇ ✓ üst sekizin altında              │
│    x: A1 %13,1 · P1 %23,7 · P2 %36,8 · P3 %50,0 · P4 %63,2 · P5 %76,3 · A2 %86,9 │
│       döküm alanı %0–10,5 · geçici geçiş %46,9 · geçici destek %56,6            │
│ ⛔ A2 %86,9 — sağ sekiz %87,5'te başlar; usta karede ÖLÇÜLÜR, taşarsa D 400 m'ye │
│    çekilir ve bütün yüzdeler yeniden yazılır.                                   │
│ ⛔ ÖN GÖRSELLEŞTİRME zorunlu: plan + yan kesit; her karede burun ucunun hangi    │
│    ayak hizasında olduğu işaretlenir (itme cetveli).                            │
│ güneş         45°K · δ +7° geometrisi · 05:05 az 75° → 18:35 az 281°;           │
│               kadraj yatayda 323°–37° → disk hiçbir karede kadrajda değil [DERS 39] │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① ESKİ TAŞ KEMER KÖPRÜ  vadi tabanı · %34,2 · x %44,4 · 64 × 21 px ⭐ "AYNI YER" │
│    nesnesi [DERS 25] — zincirin her koşusunda ELLE; sel karesinde kemer doğuşuna │
│    kadar suda kalır, ÜSTÜ görünür (kaybolmaz)                                   │
│ ② ESKİ YOL — iki yamaçta on dört viraj, açık asfalt bandı + korkuluk; her karede │
│    aynı çizgi, G15'te BOŞ ama okunur                                            │
│ ③ ŞAPEL (SOL · %61,9 · x %28,1) · ④ KAYA KULESİ (SAĞ · %45,9–57,5 · x %89,7)     │
│ ⑤ İKİZ ZİRVE SİLÜETİ (%82,4) · ⑥ NEHİR — yatağı sabit, rengi ve debisi taşıyıcı  │
│ + melez ormanı yamaçlar (renk taşıyıcısı) · üst kotta sabit yeşil ladin bandı    │
│ ⛔ Beş ayak G3'ten sonra ÇAPA değil YAPI'dır; SITE/BACKGROUND'a girmez.          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ ufuk %50 (tilt 0, kaya kulesinin alt üçte biri) · taç (zirve) %82,4 · yapı tacı  │
│ (tabliye + lamba) %48,8 · çalışma seviyesi %25,1–45,0 ✓ ≥ %25                    │
│ yanlar: SOL şapel %28,1 · SAĞ kaya kulesi %89,7 — iki yanda da çapa var [§2.8]   │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ (§2.8 varsayılanı): üst 60 px · alt 100 px ·      │
│ sağ üst 300×100 px · son ekran 5–20 sn → KART. Kanıt nesnesi (taş köprü %34,2)   │
│ alt 100 px'in (%9,3) üstünde ✓; A2 sağ şerit uyarısı yukarıda.                   │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ tip       itmeli beton kutu kesitli viyadük · 7 açıklık · toplam 420 m         │
│ açıklık   60 + 75 + 75 + 75 + 75 + 60 m (A1–P1–P2–P3–P4–P5–A2)                 │
│ ayaklar   P1 30 m · P2 48 m · P3 60 m · P4 50 m · P5 32 m (vadi tabanından)    │
│ tabliye   üst kot +64,0 m · kutu kesit derinliği 4,0 m · genişlik 12,0 m       │
│ burun     çelik launching nose 45 m · pas kırmızısı · S3'te monte, S12'de sökülür │
│ kesit     her döküm 25 m · döküm alanı sol platoda · ilk kesit koyu döküm derzli │
│ geçici    tırmanır kalıp · döküm hangarı · itme yatağı · geçici çelik destek     │
│           (x +37,5 m) · geçici menfez geçişi · şantiye yolu · mobil/paletli vinç │
│ eski yol  14 viraj · asfalt bandı 6 m · korkuluk · taş kemer köprü tek gözlü 30 m │
│ STRUCTURE bloğunun İngilizce tam hâli BOLUM_1 S0'da yazılır ve 16 promptta     │
│ BİREBİR tekrarlanır; değişen yalnız AT THIS STAGE                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 15 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az yapı göstermez. İnşa sırası
> `YAPI_TIPI_KARTLARI`'ndan gelir, uydurulmaz; sahne sayısı arttıkça aşama incelir (ara hâl
> %25 / %50 / %75 kendi satırını alır [DERS 37]). Kış İKİ sahne [DERS 7]. SÜRE sütununun en
> büyüğü doruktadır [P2-f] — düz ızgarada hepsi 8,0 (aşağıdaki beyan). Gölgesiz (rejim C)
> klip en uzun klip olamaz [DERS 40].

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | İSTASYON | KANIT NESNESİ (px) |
|:-:|:-:|---|---|---|:-:|:-:|:-:|---|
| 0 | 8,0 | **AÇAR** | YENİ GÜZERGÂH 0 → ilk kesi (%2) | 1 gün | A | 05:05→05:15 | ANA | sol yamaçta taze toprak kesisi (≈40 px bant) |
| 1 | 8,0 | **KAZAR** | YAKLAŞIM + TEMELLER 0 → %100 · geçici geçiş kurulur | 8 hf | B | 05:15→07:15 | ANA | iki yakada kenar ayağı basamakları (%45 kotunda iki çentik) |
| 2 | 8,0 | **YÜKSELİR** | AYAKLAR %0 → %100 + başlıklar | 16 hf | A | 07:15→07:25 | ANA | P3 ayağı 202 px — tepesi tabliye kotunda (%43,8) |
| 3 | 8,0 | **KURAR** | DÖKÜM ALANI 0 → %100 · ilk kesit + çelik burun | 8 hf | B | 07:25→09:25 | ANA | çelik burun ucu A1'in 20 m ötesinde (%17) |
| 4 | 8,0 | **İTER** | TABLİYE %0 → %14 (A1 → P1) | 3 hf | A | 09:25→09:35 | ANA | tabliye ucu P1'de (%23,7) · burun %31,5 |
| 5 | 8,0 | **EKLER** | TABLİYE %14 → %32 (P1 → P2) | 4 hf | A | 09:35→09:45 | ANA | tabliye ucu P2'de (%36,8) · burun %44,7 |
| 6 | 8,0 | **UZANIR** | TABLİYE %32 → %50 (P2 → P3) · geçici destek kurulur | 19 hf | B | 09:45→11:45 | ANA | tabliye ucu P3'te (%50) · geçici destek %56,6 |
| 7 | 8,0 | **ZORLAR** | TABLİYE %50 → %63 (P3 → P4) · su yükselirken itme sürer | 3 hf | B | 11:45→13:45 | ANA | tabliye ucu P4'te (%63,2) · burun %71,1 · su çizgisi ayak dibinde |
| 8 | 8,0 | **TAŞAR** | HAT KOPAR — geçici geçiş ve berm gider | 2 gün | A | 13:45→13:55 | ANA | geçici geçiş YOK (%46,9 boş) · sürüntü matı geçici destekte · berm aşılmış |
| 9 | 8,0 | **ONARIR** | HAT YENİDEN KURULUR · döküm alanı iki kesit biriktirir | 4 hf | B | 13:55→15:55 | ANA | yeni menfez + yeni çapraz + temizlenmiş pabuç · hangarda 2 hazır kesit |
| 10 | 8,0 | **SÜRER** | TABLİYE %63 → %76 (P4 → P5) · burun KARŞI KENARA DEĞER | 6 hf | A | 15:55→16:05 | ANA | tabliye ucu P5'te (%76,3) · ⭐ burun ucu A2'de (%86,9) |
| 11 | 8,0 | **KAVUŞUR** | TABLİYE %76 → %100 — beton hat tamam | 4 hf | A | 16:05→16:15 | ANA | kesintisiz beton çizgi A1 → A2 (%13,1 → %86,9) |
| 12 | 8,0 | **SÖKER** | BURUN + DESTEK + HANGAR → 0 · kalıcı mesnetler | 6 hf | B | 16:15→18:15 | ANA | burun yok · destek yok · hangar yok · tabliye mesnetlerde |
| 13 | 8,0 | **DÖŞER** | ÜST YAPI %0 → %100 · şantiye toplanır | 8 hf | A | 18:15→18:25 | ANA | su yalıtımı + asfalt + korkuluk + lamba (%48,8) · yol izi |
| 14 | 8,0 | **AKAR** | TRAFİK ESKİ YOL → YENİ YOL | 1 gün | A | 18:25→18:35 | ANA | viyadükte far izi çizgisi (%45) ↔ virajlarda son araç |

```
IZGARA          120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · kesmeler 8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn)
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: sahip beyanı 16.09.2026 — 15 × 8,0; iki dakikalık yatay hat, on beş vuruş
                       omurgadan doğrudan türedi (her vuruş bir aşama), toplam modül süresini değiştirmez.
                   (b) ritim klip İÇİNE nasıl taşınır: olay yoğunluğu ve MÜZİK KATMANI değişir — ilk itmede
                       (S4) ritim belirginleşir, selde (S7–S9) katmanlar çekilir, yeniden başlamada (S10) döner,
                       eski yol boşalırken (S14) sadeleşir. ⛔ SÜRE sütunuyla telafi YAPILMAZ [DERS 24].
                   (c) kabul edilen risk: ⑥ METRONOM hükmü beklenir [DERS 13 · 24]; karşı kayıt: varyanslı
                       kurgu üç filmde RHYTHM aldı [DERS 44 · THE CROSSING · OVER THE WALL · THE EMPTY RIDGE] —
                       üçü de planındaki düz ızgarayı KULLANMADI. Düz ızgara henüz hiç RHYTHM almadı.
                   (d) sahibin notu (16.09.2026): "eşit süreyi otomatik ritim hatası saymam; asıl sorun her
                       sahnede aynı yoğunluk ve aynı müzikal vurgudur" — (b) maddesi bunun karşılığıdır.
IŞIK GÜNÜ       Σ pencere = 9 A × 10 dk + 6 B × 2 h = 1,5 + 12,0 = 13,5 saat  ≤ 14 ✓   (03_SAHNE_SIRALAMASI §4)
                B: S1 · S3 · S6 · S7 · S9 · S12   ·   A: S0 · S2 · S4 · S5 · S8 · S10 · S11 · S13 · S14
                gerekçe: B = gölge ve gök hareketi gereken sahneler · A = makinenin, aracın ve suyun okunması
                gereken sahneler [SANTIYE §2]; A dizisi üçten uzun değil.
BÖLÜM SINIRI    G8 — S7'nin son karesi = S8'in ilk karesi; yapı yüzdesi (tabliye ucu P4 %63,2, burun %71,1), gölge
                açısı ve gök AYNI [DERS 52]. Sel bu karede henüz tepe yapmamıştır: su yüksek, berm sağlam, itme durmuş.
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: ESKİ TAŞ KEMER KÖPRÜ — G0'da ve usta karede (G15) aynı konum (x ≈ %44,4 · y %34,2)
        ve aynı boy (≈64 × 21 px) [DERS 25]. İkinci kanıt: eski yolun viraj geometrisi (iki yamaçta aynı çizgi).
        ⭐ İtme sahnelerinde üçüncü kanıt: İLK DÖKÜLEN KESİT — koyu döküm derzi ve kalıp izleriyle tanınır;
        16 karede aynı kesittir, hep en öndedir ve her itmede sağa kayar (gövde sıçramadı mı — elle).
LOOP    G15 ↔ G0: aynı kadraj · aynı çapalar · ışık FARKLI (05:05 şafak → 18:35 alacakaranlık) — bilinçli,
        sebep: tek ışık günü süpürülür [§2.7 ①] ve trafik yön değiştirir. ⚠️ Kesintisiz döngü İDDİA EDİLMEZ;
        bu bir açılış–kapanış kafiyesidir (zikzak ışık → düz ışık).
SÖKÜM   geçici ekipman ekranda GİDER: tırmanır kalıplar (S2 sonunda iner) · geçici menfez geçişi (S1 kurulur →
        S8 SEL GÖTÜRÜR → S9 yeniden serilir → S13 kaldırılır) · çelik burun (S3 kurulur → S12 parça parça sökülür,
        yoldan çıkar) · geçici çelik destek (S6 kurulur → S12 sökülür) · döküm hangarı + itme yatağı (S3 → S13) ·
        şantiye yolu (S1 → S13 toplanır, İZİ KALIR). Usta karede hiçbiri yok; hiçbiri yoktan yok olmadı [DERS 48].
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
kazık/temel betonu   → mikserler şantiye yolundan iner, pompa hattı ayak dibinde                  → G2
ayak betonu          → aynı hat; tırmanır kalıp her dökümde bir kademe yükselir (ara hâl siluette) → G2 → G3
tabliye kesitleri    → SOL PLATODAKİ DÖKÜM ALANI: donatı kafesi istifi, kalıp panosu, hangarda tek
                       kesit; her kesit orada doğar, priz alır ve ancak sonra itilir                → G4
çelik burun          → parçalar döküm alanında istiflenir, mobil vinç birleştirir                   → G4
geçici çelik destek  → parçalar şantiye yolundan gelir, paletli vinç kurar                          → G7
korkuluk · asfalt    → kamyonlar A1 yaklaşımından girer, finişer soldan sağa ilerler                 → G14
⛔ HİÇBİR PARÇA GÖVDENİN ÖNÜNDE BELİRMEZ: vadinin üstünde yalnız İTİLEN gövde ve burun vardır.

GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL (prompta yalnız vekil girer)
  betonun priz alması ve gerdirme → döküm alanında bekleyen kesit + hangarın kapağının açılıp kapanması
  kriko döngüsü (santim santim)   → gövdenin bir ayaktan diğerine geçmesi ve burun ucunun yer değiştirmesi
  mesnet değişimi / kaynak        → S12'de gövdenin birkaç santim İNMESİ ve desteklerin çıkması
  devreye alma / işaretleme       → S13'te lambaların yanması, S14'te trafiğin geçmesi
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① VİYADÜKTE AKAN TRAFİK — tabliye çizgisi (%45) boyunca far izleri, soldan sağa tek düz çizgi
② BOŞALMIŞ ESKİ YOL — iki yamaçtaki on dört viraj araçsız ama OKUNUR (asfalt bandı + korkuluk + taş köprü)
③ AYNI TAŞ KÖPRÜ — %34,2 · x %44,4 · 64 px, G0'daki ile aynı (kanıt nesnesi) · vadi tabanında şantiye izi
Kapı: usta kare bu üçünü bu sırayla okutmuyorsa kare yeniden — kompozisyonla, nesne ekleyerek değil.
FİNAL KARE KANITI  ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 kanit.jpg   (S14 tutuşunun içi · güneş −1°,
                   gök aydınlık [DERS 45] · viyadükte ışık akıyor, virajlarda araç YOK ama yol görünür)
```

---

## 🖼️ KARE TABLOSU — N+1 = 16 görsel [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Her kare bir öncekinin karesinden türetilir (ters inşa §8): G15 usta kare önce, sonra G14 → … → G0.
> Güneş satırı her karede ve her I2V'de [DERS 18]; güneş DİSKİ anılmaz [DERS 39]; gölge açısı G(n) ile
> G(n+1)'de FARKLI [DERS 32 · 47].

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|---|---|---|---|
| G0 | 05:05 | 75° | −5° (şafak) | BGB, çok uzun, sola | berrak şafak, batıda son yıldızlar | çıplak melez · kar çizgisi en kalın · 10 Mart y1 | yapı YOK · sol yamaçta ilk toprak kesisi (%2) · virajlarda far izleri |
| G1 | 05:15 | 77° | −3° (ilk ışık) | BGB, uzun, sola | ilk ışık, zirveler pembe | aynı · nehir düşük ve berrak | kesi uzamış; iki yakada yaklaşım alanı işaretli, şantiye yolu başlıyor |
| G2 | 07:15 | 98° | 18° | B, uzun, sola | sabah kümülüsleri sıralı | ilk yeşil, kar çizgisi yükseliyor · 5 Mayıs | iki yakada kenar ayağı basamakları + beş kazık başı (%25–34) · geçici menfez geçişi kurulu |
| G3 | 07:25 | 99° | 20° | B, uzun, sola | açık, yüksek sirrus | tam yeşil yamaç · 25 Ağustos | BEŞ AYAK TAM BOY + başlıklar + mesnetler (P3 202 px, tepesi %43,8) |
| G4 | 09:25 | 127° | 39° | KB, kısalan, sola-geriye | açık, tek tük kümülüs | melezler altın · 20 Ekim | döküm hangarı + itme yatağı · ilk kesit dökülmüş (koyu derz) · çelik burun A1 ucunda (%17) |
| G5 | 09:35 | 129° | 41° | KB, kısa, geriye | açık | yaprak dökümü · 10 Kasım | tabliye ucu P1'de (%23,7) · burun %31,5 · hangarda yeni kesit |
| G6 | 09:45 | 131° | 42° | KB, kısa, geriye | ince sirrus | çıplak melez, zirvede ilk kar · 8 Aralık | tabliye ucu P2'de (%36,8) · burun %44,7 |
| G7 | 11:45 | 172° | 52° | K, en kısa, geriye | kapalı, alçak gri tavan | kar çizgisi EN DÜŞÜK, tomurcuk · 20 Nisan y2 | tabliye ucu P3'te (%50) · burun %57,9 · geçici çelik destek (%56,6) kurulu ⭐ BÖLÜM SINIRI |
| G8 | 13:45 | 219° | 46° | KKD, uzayan, sağa | yırtık yağmur bulutu | kar hızla eriyor, nehir kahverengi ve kabarık · 11 Mayıs y2 | tabliye ucu P4'te (%63,2) · burun %71,1 · ayak diplerine ve destek pabucuna KAYA BERMİ · plant yüksek alanda ⭐ BÖLÜM SINIRI |
| G9 | 13:55 | 222° | 45° | KKD, sağa | koyu tavan, batıda ince aydınlık | SEL — su en yüksek · 13 Mayıs | aynı (itme durdu) · GEÇİCİ GEÇİŞ YOK · berm aşılmış · sürüntü matı destekte · taş köprü kemer doğuşuna kadar suda |
| G10 | 15:55 | 252° | 27° | D, uzun, sağa | yırtılan bulut, açılan mavi | taze yeşil, nehir çekilmiş · 10 Haziran | aynı · silt çizgisi (%26) · sürüntü iki istif · yeni çapraz + kaya apronu · menfez yeniden · hangarda 2 HAZIR KESİT |
| G11 | 16:05 | 254° | 25° | D, uzun, sağa | açık, kümülüs | yaz yeşili · 22 Temmuz | tabliye ucu P5'te (%76,3) · ⭐ BURUN UCU KARŞI KENAR AYAĞINDA (%86,9) — beton henüz gelmedi |
| G12 | 16:15 | 256° | 23° | D, uzun, sağa | açık, sıcak ton | koyu yaz yeşili · 19 Ağustos | ⭐ KESİNTİSİZ BETON ÇİZGİ A1 → A2 (%13,1–%86,9) · burun yaklaşım platformunda (%94,8) · destek duruyor |
| G13 | 18:15 | 278° | 2° | D, çok uzun, sağa | altın batı, ince sirrus | yaz sonu, ilk sararma · 30 Eylül | burun YOK · destek YOK · hangar ve itme yatağı SÖKÜLDÜ · tabliye kalıcı mesnetlerde · üst yüzey çıplak · platformda membran/korkuluk/direk istifi |
| G14 | 18:25 | 279° | 1° | D, çok uzun, sağa | alacakaranlık, batıda turuncu | melezler tam altın, zirvede kar · 25 Kasım | su yalıtımı + asfalt + korkuluk + lamba direkleri yanık (%48,8) · yaklaşım bağlantıları · şantiye yolu kaldırılmış, izi kalmış |
| G15 | 18:35 | 281° | −1° (gün batımından sonra) | ışık bitiyor, gölge yok | alacakaranlık mavisi, zirvelerde son pembe | altın-kahve yamaç · 26 Kasım y2 | ⭐ USTA KARE — viyadükte far izleri akıyor, virajlar boş ama okunur, lambalar yanık |

```
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G15 usta kare → G14 (lambalar söner, asfalt ve korkuluk kalkar → çıplak beton; hangar, şantiye yolu ve menfez
     GERİ) → G13 (çelik burun ve geçici destek GERİ, kaya apronu geri, tabliye itme mesnetlerine yükselir) →
   G12 (beton gövde P5'e çekilir; burun A2 sekisinde kalır) → G11 (gövde P4'e; burun A2'den ayrılıp son açıklığa;
     kuyruğa eklenen iki kesit hangara geri) → G10 (su YÜKSELİR, sürüntü matı ve breş GERİ, menfez ve çaprazlar
     sökülür) → G9 (sel tepe: geçici geçiş kalkar, berm aşılır) → G8 (su iner, geçici geçiş GERİ, berm sağlam,
     plant yüksek alanda) → G7 (gövde P3'e kısalır, berm kalkar, kış girer) → G6 (gövde P2'ye, geçici destek
     KALKAR) → G5 (gövde P1'e) → G4 (gövde döküm alanına, burun A1 ucuna) → G3 (hangar ve burun kalkar) →
   G2 (ayaklar iner → kazık başları) → G1 (temeller kalkar → işaretli alanlar) → G0 (şantiye yolu ve kesi kalkar)
   sonra I2V S0 (G0→G1) … S14 (G14→G15) — her klip iki uca kilitli, üretim 9,0 sn, baştan 1,0 kırp
⛔ HER KAREDEN SONRA: taş köprü + viraj geometrisi ELLE ✓/✗ [DERS 25] · viyadük 1 · taş köprü 1 sayımı [DERS 55]
⛔ İTME KARELERİNDE (G4–G12) AYRICA: ilk kesitin koyu döküm derzi bir önceki karedekiyle aynı kesit mi ve
   gövde bir ayaktan fazlasını atlamadı mı — elle [DERS 57 mekanizması]
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     45°K · kamera bakışı 0° (kuzey) · kadraj yatayda az 323°–37°
                güneş 05:05'te az 75°, 18:35'te az 281° → DİSK HİÇBİR KAREDE KADRAJDA DEĞİL [DERS 39]
                sabah sağdan (doğu), öğle arkadan (güney), akşam soldan (batı) aydınlatır
MEVSİM YAYI     10 Mart yıl 1 → 23 Kasım yıl 2 (627 gün ≈ 20,6 ay) · iki kış, iki yaz
                taşıyıcılar [§6 dağ + kırsal]: ⭐ kar çizgisinin yamaçta inip çıkması · melez ormanının rengi
                (yeşil → altın → çıplak → yeşil) · nehrin rengi ve debisi · beton yaşı (yeni kesit koyu)
                ⛔ MELEZ (Larix decidua) YAPRAK DÖKER — üst kottaki sabit yeşil ladin bandı ayrı yazılır;
                iki tür karıştırılmaz (yaprak dökmeyen bir çamla mevsim anlatılamaz).
GÖLGE SÜPÜRMESİ rejim B klipte 26°–50° (45°K, bahar/yaz penceresi) — S1 · S3 · S6 · S7 · S9 · S12
                rejim A klipte gölge fark edilmez; zaman YÜZEYLE ve trafikle kanıtlanır [SANTIYE §3]
KIŞ             S6 (kar çizgisi yamaçta İNER, döküm yavaşlar) · S7 (erir, nehir kabarır) — tek klipte
                başlayıp bitmez [DERS 7 · 21] · ⛔ VADİYE KAR YAĞMAZ: tek ışık günü ve A/B rejimi taşımaz [HAVA §3]
GECE            yok. G0 şafak (−5°) ve G15 gün batımından hemen sonrası (−1°) alacakaranlıktır; gök aydınlık,
                yapı ve eski yol okunur [DERS 45]. Far izleri ARAÇ HAREKETİYLE oluşur — sabit neon şerit değildir.
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   h +80,0 m · D_eksen 380 m · D_kenar 190 m · bakış 0° · tilt 0° · roll 0° · 24 mm · 16:9
YAPI     420 m · 7 açıklık · 5 ayak (30/48/60/50/32 m) · tabliye üstü +64 m · kesit derinliği 4 m ·
         burun 45 m · tabliye üstü %45,0 · zirve (taç) %82,4 · çalışma seviyesi %25,1–45,0
ÇAPALAR  ① taş köprü %34,2 · x %44,4 · 64 × 21 px (kanıt nesnesi) · ② eski yol viraj bandı (iki yamaç) ·
         ③ şapel %61,9 · x %28,1 · ④ kaya kulesi %45,9–57,5 · x %89,7 · ⑤ ikiz zirve %82,4
IZGARA   15 × 8,0 · 120 BPM · kesmeler 8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn)
IŞIK     05:05 → 18:35 · 9 A + 6 B = 13,5 h · güneş az 75° → 281°, disk kadraj dışı
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ 00_ANALIZ altı dosya yazıldı · hikâye onayı ✅ 16.09.2026
✅ konsept kapısı (dört test) · kanal tezi kapısı
✅ değişmezler: dört kutu · D_eksen/D_kenar ayrı [DERS 38] · iki yanda çapa [§2.8]
✅ aşama merdiveni 15 satır · üç zorunlu satır · düz ızgara beyanı (a)(b)(c)(d)
✅ kare tablosu 16 satır · ışık günü 13,5 h ≤ 14 · ara kare YOK
✅ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_OLD_ROAD (klasör modu) — 16.09.2026
   → BLOCK 0 · FIX 2, ikisi de beyanlı: ARAÇ KUTU SETİ ölçülmedi · bütün sahne süreleri eşit (düz ızgara)
⛔ ARAÇ KAPISI koşulmadı → THE_OLD_ROAD_URETIM_GUNLUGU.md §0 (sekiz ölçüm + ⑨ İTME TESTİ)
⛔ ÖN GÖRSELLEŞTİRME çizilmedi → itme cetveli (her karede burun ucu hangi ayakta)
⛔ ÜRETİM GÜNLÜĞÜ boş
```
