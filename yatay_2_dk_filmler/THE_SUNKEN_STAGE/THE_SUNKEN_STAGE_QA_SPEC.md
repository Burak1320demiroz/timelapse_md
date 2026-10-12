# 🔍 THE_SUNKEN_STAGE — QA SPEC

> THE SUNKEN STAGE · 16:9 · 20 × 8,0 sn · 160,0 sn · kart yok · müzik VAR (56 sn'den, sonda sahneden) · tek istasyon. **Bu dosya
> yalnız belgeli merceklere verilir: ❹ İNŞA · ❺ TESLİM** (beş mercekli QA, 06.10.2026 [DERS 64]).
> ⛔ **❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❸ ŞANTİYE'ye VERİLMEZ** — üçü kör koşar, ayrı geçici sohbette, proje dışında
> [`QA_KOSU_KILAVUZU` §1]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit değildir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_SUNKEN_STAGE <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].
> Ham raporlar `QA/HAM/THE_SUNKEN_STAGE/THE_SUNKEN_STAGE_Q<n>_<AD>_HAM.md` · kayıt `QA/FILMLER/THE_SUNKEN_STAGE.md` · `QA/TABLO.md`.

---

## 0. KÜNYE

```
FİLM          THE_SUNKEN_STAGE — ormandaki bir çukurda su basmış, terk edilmiş hayalî bir açık hava tiyatrosu: su pompalarla üç
              klipte çekilir, on iki taş yay ve üç merdiven ortaya çıkar, sahne çamurdan çıkar; çamur makinelerle, silt basınçlı
              suyla gider; kırık sol merdiven onarılır; ahşap oturma tahtaları, ahşap sahne, bakır kaplı yelpaze kabuk, iki teknik
              kule, iki taş yol; şantiye çekilir; akşam lambalar yanar, seyirci gelir, sahne ışıkları yükselir, konser ve alkış ·
              MAIN STATION
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_2_dk_filmler · HIZ 1x · ⚠️ 160 sn bu klasörün 2:00 bandının dışı (beyanlı)
KANARYA       mossbellow   ⛔ kör mercek raporunda bu kelime geçerse plan SIZMIŞTIR → koşu SIZINTI [QA_KOSU §3.1]

TESLİM YAPISI ⭐ SAHNE BLOĞU  20 sahne × 8,0 sn = 160,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  ⛔ YOK                                   ← son sahne S19 son saniyeye kadar SAHNEDİR
                 TOPLAM                          160,0 sn
              ⛔ 160,0 sn'den uzun dosya = plan dışı kart/siyah → ❺ "the plan declares NO card — report it"
              ⛔ ekranda YAZI yok (açılış cümlesi yalnız kurguda ve yalnız sahip seçerse — günlük §5)

SAHNE SAATLERİ  sahne n = n × 8,0 → (n+1) × 8,0   ·   S0 0,0–8,0 · … · S9 72,0–80,0 · S10 80,0–88,0 · … · S19 152,0–160,0
                (19 kesme, her 8,0 sn · müzik 120 BPM → her kesme ölçü başında, 4 ölçü/sahne)
PART GRID       — (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)
⛔ DÜZ IZGARA   sahip senaryosu (hikâye SAPMA ②) · ⚠️ bandın dışı (format 12 × 10,0 · 2:00). Eşit klipte ❷ RHYTHM NOT
                TRIGGERED. Karşı kayıt [DERS 44].
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]: ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — {5,9} ya da {5,10}
   gerekir; {4,6,8} çıkarsa iki-klip hükmü (PLAN §DEĞİŞMEZLER) ve karar sahibe döner.

İSTASYON        tek — MAIN STATION, 20/20 klip · ❸ ikinci istasyon görürse bulgu yazar
TEK TAHLİYE     S0 + S1 + S2 (0,0–24,0) — aynı pompalar, aynı hortumlar; su yalnız ALÇALIR; 8,0 ve 16,0'daki kesmeler tahliyenin
                ortasındadır, su çizgisi iki yakada aynı terasın dibinde
TEK AKŞAM       S15 → S19 (120,0–160,0) — yanan lamba bir daha sönmez, oturan seyirci yerinde kalır; 144,0'de rejim A → G (gerçek
                zaman) — bu kesmede seyircinin "iz" görünümü küçük, net figüre döner (beyanlı dikiş)
YAPI          açık hava tiyatrosu · 12 eş merkezli yarım daire taş teras (16,0 → 30,4 m · basamak 1,2 × 0,6) · 3 radyal merdiven
              (φ −30 · 0 · +30) · 26 × 13 m taş sahne platformu (+1,2) · sonradan: ahşap oturma tahtaları · çelik ızgara + ahşap
              sahne · yedi kaburgalı yelpaze kabuk (arka üçte bir, bakır dış · ahşap iç) · iki koyu teknik kule · iki taş yol ·
              basamak, kabuk ve yol lambaları
SAHA          sonbahar karışık ormanında derin çukur · 47° K · çapalar: ⭐ YARIK KAYA (sol üst — kanıt) · iki çam (sağ üst) · arka
              duvar + şev · servis yolu + hardstand · ağaç çizgisi %90
ZAMAN YAYI    ≈4–5 ay (tahliye birkaç gün · onarım ve donatım ≈3–4 ay · açılış akşamı) · film mertebe anlatır: "bir sabah su
              çekilir, bir mevsim taş ve ahşap, bir akşam konser"
IŞIK          TEK GÜN 09:20 → 17:50 (mavi saat, güneş −4,9°) · Σ rejim 8 sa 30 dk · orman rengi SABİT (sonbahar) · bilinçli
              sıkıştırma (sahip ÜSLUP BEYANI — "tek günde yapıldı" iddiası yok) · güneş hiçbir karede kadrajda değil
REJİM         A (10 dk) × 15 · B (2 sa) × 3 (S4 · S6 · S10) · G (8 sn · gerçek zaman) × 2 (S18 · S19, final) — ⚠️ üç rejim,
              beyanlı · ⚠️ G depoda ölçülmedi
KAMERA        MAIN STATION — 16 mm · h 22,0 m (orkestradan) · D_eksen 44,0 · D_kenar ≈16 · bakış 15° · tilt 27° AŞAĞI · roll 0° ·
              tiyatronun ekseninde (simetrik)
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G20 usta kare → G19 → … → G0 · her kare zincir_kontrol
GÜNLÜK        THE_SUNKEN_STAGE_URETIM_GUNLUGU.md — ⛔ boş (üretim başlamadı) → bu SPEC'in hükmü üretimle başlar
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı · ❺ FINAL BEAT

```
SAHNE       S19 (152,0–160,0)
FİNAL BEAT  152,0–156,0 olay: topluluk çalar, müzik ilk güçlü yükselişini yapar, seyirci alkışa başlar, ön sıralarda birkaç kişi
            ayağa kalkar · 156,0–160,0 TUTUŞ: sahne ışıkta kalır, seyirci yumuşakça alkışlamayı sürdürür, ağaç tepeleri hafif
            sallanır; yapıda HİÇBİR şey değişmez — kare donmaz, olay da büyümez
SANİYE      159,0 (son 4,0 sn'lik TUTUŞUN içi [P2-i]; mavi saat, okunur [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (beşi de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① ışıktaki sahne + küçük topluluk + bakır kabuk (sahne ön kenarı x 719–1201 · kabuk tepesi üstten 267) — en parlak
   ② on iki yayın çoğu dolu seyirci (sırtı kameraya, küçük) + yanık basamak lambaları + üç AÇIK koridor
   ③ iki koyu kule (x 689 · 1231, tepe 349) + iki ışıklı taş yol (alt solda · alt sağda)
   ④ arka duvar (344) + mavi saatte sonbahar ormanı + MAVİ gök bandı (üstten 0–105) — siyah değil
   ⑤ AYNI yarık kaya (kanıt nesnesi: x 286–384 · tepe 94 · 98 px — G0 ile aynı konum ve boy) + iki çam (x 1490–1557)
   + geçici ekipman GİTMİŞ: vinç, pompa, tank, kamyon, palet, kalas YOK (SÖKÜM satırı)
   + BEDEL görünür: çanakta su yok; yerinde dolu, ışıklı tiyatro (G0 ↔ G20)

KOMUT
   ffmpeg -ss 159.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①–⑤'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP (biçim kafiyesi, ışık bilinçli farklı)
   ffmpeg -ss 0.3   -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 kanit_g20.jpg
   İki karede kaya, çamlar, arka duvar ve ufuk aynı yerde; kaya aynı x'te (286–384 ±2 px). G0'da kahverengi su 11. terasın
   dibinde, yalnız iki üst yay dışarıda, sol üstte pompalar; G20'de aynı on iki yay seyirciyle dolu, ışıklı.
   Işık: G0 sabah ↔ G20 mavi saat (PLAN LOOP satırı) — kanıt çifti AYNI IŞIK iddiası taşımaz.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=16 · h=22,0 · tilt 27° aşağı · iğne deliği izdüşümü · üstten px)

| nesne | kot (m) | x (soldan) | üstten | her karede |
|---|:-:|:-:|:-:|---|
| ufuk / ağaç çizgisi (200 m) | — | bütün en | 105 (%90) | ✓ |
| ⭐ kanıt nesnesi YARIK KAYA | +13 → +23 | 286–384 | 94–201 | ✓ BİREBİR (98 px en, boy dâhil) · tek kaya, koyu çatlak |
| iki çam | +12 → +34 | 1490–1557 | 22–173 | ✓ (G'de tepeleri hafif sallanır) |
| arka duvar | +7 | 479–1441 | 344 | ✓ |
| sahne platformu ön / arka kenar | +1,2 | 719–1201 / 767–1153 | 539 / 451 | ✓ (G3'ten görünür; G0–G2 su altında) |
| kabuk tabanı / ön dudak / tepe | +1,6 / +11 / +13,2 | 785–1135 | 470 / 319 / 267 | G10 kaburgalar · G11+ kabuk |
| kuleler (sol · sağ) dip → tepe | +1,2 → +10,2 | 689 · 1231 | 500 → 349 | G12+ |
| dış kenar en geniş (φ ±60) | +7,2 | 266 · 1654 | 543 | ✓ |
| dış kenar orta (φ 0) | +7,2 | 960 | 858 | ✓ |
| orkestra kenarı (orta) | 0 | 960 | 708 | G3+ (G0–G2 su altında) |
| sol giriş · sağ giriş (merdiven tepesi φ ±30) | +7,2 | 383 · 1537 | 736 | ✓ |
| giriş yolları kadraj kenarında | +8 | 109 · 1811 | 892 | G13+ taş · öncesi toprak iz |
| sol merdiven hasarı (4.–6. teras) | +1,8 → +3,0 | 656–708 | 687–695 | G2–G5 kırık · G6+ tam |
| su çizgisi orta / yanlar | +6,1 · +4,1 · +1,5 | 445–1475 · 542–1378 · 636–1284 | 814 / 433 · 748 / 467 · 717 / 510 | G0 · G1 · G2 |
| mobil vinç (hardstand) | 0 | ≈578 | ≈465 | G5–G13 |
| pompalar · tanklar | +7 → +9 | ≈232 · 178–372 | ≈344 · 309–330 | G0–G13 |
| servis yolu · hardstand | +11 → 0 | sol kenar (≈326) → 587 | → 471 | ✓ |
| insan (1,7 m) | — | — | sahnede 26 px · 6. terasta 41 px · dış kenarda 58 px | ölçek |

```
KAMERA SABİTLİK  ilk/son kare kayması ≤ 2 px (1080p · KAMERA_ISTASYONU §7 · zincir_kontrol ESIK_KAYMA_ORAN) ·
                 üç nirengi: yarık kayanın tepesi · arka duvarın orta noktası · orta merdivenin tepesi (dış kenar ortası)
16 MM            yatay görüş 96,7° — yanlarda doğrusal gerilme BEKLENİR (dış yaylar kenarlarda uzar); ❶ bunu "balık gözü" ya da
                 "kamera değişti" saymamalı — çizgiler DÜZ kalmalı (rectilinear)
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
O = orkestra zemini (z 0) · +y sahneye · eksen bearing 15° · teraslar k = 1…12: ön kenar 16,0 + 1,2·(k−1), üst +0,6·k · dış
kenar 30,4 · yarım daire φ −90…+90 · merdivenler φ −30 · 0 · +30 (1,6 m) · üst geçit 30,4–32,0 · girişler φ ±30 · sahne x ±13,
y −3…+10, +1,2 · yeni sahne +1,6 · kabuk y +5,7…+10, taban ±11, tepe +13,2, yedi kaburga · kuleler x ±16, y +2, +1,2 → +10,2 ·
arka duvar y +16, +6,5 tabanlı · hardstand x −20…−30, y +2…+14 · pompalar (−48, 12, +8) · tanklar (−56…−44, 18–20) · su +6,1 /
+4,1 / +1,5 / 0 · kamera (0, −44, +22) · kaya (−64, 52) +13 → +23 · çamlar (88, 110) · (96, 118) · kapasite ≈1.600
```

### Yapı yüzdesi ve saha durumu — sahne sahne (❹ İNŞA · ❺ TESLİM için)

| S | saat | yapı: eleman + ara hâl | su · taş · seyirci · ışık | geçici ekipman kadrajda | ışık evresi |
|:-:|:-:|---|---|---|---|
| S00 | 09:20→09:30 | (yapı su altında, açığa çıkar) | su 11. → 7. terasın dibi · taş siltli ıslak | pompalar · tanklar · hortumlar · ekipler · hortum kamyonu | sabah |
| S01 | 09:30→09:40 | alt teraslar + üç merdiven açığa · sol hasar görünür | su 7. teras → sahnenin 0,3 m üstü | aynı · el arabaları | sabah |
| S02 | 09:40→09:50 | ⭐ sahne platformu çamurdan çıkar | su → yok · çamur | aynı · kalas yolları · sonda yükleyiciler + damperliler | sabah |
| S03 | 09:50→10:00 | (değişmez) · çamur gider | çamur → yüzey açık, silt filmli | yükleyiciler · damperliler · ekipler · kalaslar istife · sonda tanker | sabah |
| S04 | 10:00→12:00 | (değişmez) · ⭐ silt gider | kirli → temiz, ISLAK (yukarıdan aşağı) | tanker · yıkama ekipleri · pompalar · sonda VİNÇ + taş kamyonu | sabah → öğle |
| S05 | 12:00→12:10 | sol merdiven + teras uçları %0 → %100 | taş kuruyor | vinç (taş paleti) · harç makinesi · sonda tahta kamyonu | öğle |
| S06 | 12:10→14:10 | ⭐ ahşap tahtalar 12 sıra, alttan | taş kuru | vinç (tahta demetleri) · istifler · sonda ızgara kamyonu | öğle → öğleden sonra |
| S07 | 14:10→14:20 | çelik ızgara sahneye, soldan | — | vinç (modül) · ekipler · sonda panel kamyonu | öğleden sonra |
| S08 | 14:20→14:30 | ahşap sahne, önden arkaya | — | vinç (palet) · skip · sonda kaburga kamyonu | öğleden sonra |
| S09 | 14:30→14:40 | yedi kaburga, soldan | — | vinç (kaburga) · makaslı platform · sonda sandık kamyonu | öğleden sonra |
| S10 | 14:40→16:40 | ⭐ bakır dış + ahşap iç kabuk, aşağıdan | armatürler sönük | vinç (sandık) · iki makaslı platform · sonda kule kamyonu | → alçalan güneş |
| S11 | 16:40→16:50 | iki kule + sönük basamak lambaları | — | vinç (kule çerçevesi → bom dik) · sonda damperler | altın saat |
| S12 | 16:50→17:00 | iki taş yol + sönük yol lambaları | — | vinç DIŞ → sonda palet demeti · silindir · damperler | altın saat |
| S13 | 17:00→17:10 | (değişmez) · saha boşalır | — | ⭐ vinç, pompalar, tanklar, paletler, kalaslar ÇIKAR · sonda minibüs | altın saat |
| S14 | 17:10→17:20 | (değişmez) | topluluk sahnede · sıralar boş | minibüs · sahne ekibi · el arabası | son güneş |
| S15 | 17:20→17:30 | (değişmez) | ⭐ basamak → kabuk → yol lambaları YANAR · ana ışık sönük | şalter panosu · minibüs gider | gün batımı |
| S16 | 17:30→17:40 | (değişmez) | ⭐ ilk seyirci ≈⅓ (alt + orta) | görevliler · el arabası | mavi saat |
| S17 | 17:40→17:50 | (değişmez) | sıraların çoğu dolu · koridorlar açık | görevliler · sahne ekibi | mavi saat |
| S18 | 17:50:00→17:50:08 | (değişmez) | ⭐ ana ışık karanlıktan tama (≈3 sn) · müzik başlar | ışık ekibi (kule platformu) | derin mavi · G |
| S19 | 17:50:08→17:50:16 | (değişmez) · TUTUŞ | alkış · ön sırada birkaç kişi ayakta | — | derin mavi · G |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   YARIK KAYA — G0…G20 hepsinde x 286–384 · tepe 94 · dip 201 · 98 px en; zincirde her karede ELLE ✓/✗ (günlük §2) ·
                tek kaya, tepeden dibe koyu çatlak — rengi ve biçimi değişmez
İKİNCİ ÇAPA     iki çam (x 1490–1557) · üçüncü: arka duvar 344 · dördüncü: on iki teras + üç merdiven (SAYI ve yer)
❸ İÇİN          dikiş = KARE (G1…G19): dikişin iki yakası aynı görsel; ❸ REBUILT hükmü zincir koşulmadı demektir
⚠️ SU           S0–S2'de çanaktaki su çizgisi İNER — bu yapı değişimi değil, yapının açığa çıkmasıdır; ❸ "bina yeniden kuruldu"
                saymamalı · teras SAYISI ve yeri her karede aynı
⚠️ IŞIK         S15'te üç ışık grubu TEK KAREDE yanar (A rejimi, beyanlı) — ❶ "flicker" saymamalı; S18'de ana ışık ≈3 sn'de
                yükselir (G rejimi)
⚠️ AĞAÇLAR      S18–S19 gerçek zamanda ağaç tepeleri hafif sallanır (rüzgâr) — yer ve boy sabit
```

---

## 5. ❹ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ajanı · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | ajan (taşıyan) | geçici destek | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|---|:-:|:-:|:-:|
| SU (giden) | çanak → hortumlar | iki römork pompa → üç çökeltme tankı → boru (sol kenar) | hortumlar · ekipler | G0 (11. teras) | G3 (yok) | pompalar · tanklar S13 |
| çamur (giden) | sahne + orkestra | küçük paletli yükleyici → tekerlekli yükleyici → damperliler | kalas yolları | G3 | G4 | kalaslar S3 istif → S13 |
| silt (giden) | 12 teras · 3 merdiven | yıkama ekipleri (mızrak) · tanker · pompalar | hortumlar | G4 (kirli) | G5 (temiz, ıslak) | tanker S5 başında gitmiş |
| sol merdiven | kamyonda taş blok paletleri | vinç → taş ustaları | harç makinesi | G2–G5 (kırık) | G6 | — |
| ahşap oturma tahtaları | kamyonda demetler → orkestrada istif | vinç → marangozlar (merdivenlerden) | çelik konsollar | G6 | G7 | istifler S6 içinde biter |
| çelik ızgara | kamyonda modüller | vinç → montaj ekibi | ayar ayakları | G7 | G8 | — |
| ahşap sahne | kamyonda panel paletleri | vinç → marangozlar | skip (artıklar) | G8 | G9 | — |
| kaburgalar | uzun kamyon | vinç → teçhizat ekibi (kılavuz ip) | taban plakaları · makaslı platform | G9 | G10 | — |
| kabuk kaplaması | kamyonda sandıklar | vinç → makaslı platformlardaki ekip | iki makaslı platform | G10 (çıplak) | G11 | platformlar S11 sonrası yok |
| kuleler + üniteler | kamyonda çerçeve + sandıklar | vinç → teçhizat ekibi | makaslı platform | G11 | G12 | — |
| basamak lambaları | (ekip, el) | elektrik ekibi | — | G11 | G12 (sönük) | — |
| taş yollar + yol lambaları | küçük damperler → paletler (yol kenarı) | döşeme ekipleri · silindir · elektrik ekibi | toprak iz | G12 (toprak) | G13 | paletler S12 içinde biter |
| şantiye | hardstand + lay-by | vinç + kamyonlar + römork | — | — | — | ⭐ S13: vinç, pompalar, tanklar, paletler, kalaslar çıkar |
| sandalye / sehpa / kutu | beyaz minibüs | sahne ekibi · el arabası | yan rampa | G14 | G15 | minibüs S15 |
| lambalar yanık | şalter panosu (sahnenin solu) | elektrik ekibi | — | G15 (sönük) | G16 | — |
| seyirci | iki taş yol (kadraj kenarından) | — (yürür) | görevliler | G16 (boş) | G18 (çoğu) | — |
| ana ışık | kulelerdeki üniteler | ışık ekibi (kule platformu) | — | G18 (sönük) | G19 (tam) | — |

```
❹ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır):
   açık hava tiyatrosu 1 (12 teras · 3 merdiven · 1 sahne) · yelpaze kabuk 1 · teknik kule 2 · taş yol 2 · sarı römork pompa 2 ·
   gri tank 3 (G0–G13) · siyah hortumlar · kamyon (hortum) · küçük paletli yükleyici 1 + tekerlekli yükleyici 1 + damperli 2
   (S2 sonu–S3) · beyaz su tankeri 1 (S3 sonu–S4) · sarı mobil vinç 1 (G5–G13) · düz kasalı kamyonlar (değişen yükler) · harç
   makinesi · makaslı platform ≤2 · küçük silindir + küçük damperler (S12) · beyaz minibüs 1 (S13 sonu–S15) · şalter panosu ·
   ekipler (iz) · küçük topluluk (≈12) · seyirci (≈1.600'e kadar) · görevliler · yarık kaya 1 · çam 2 · arka duvar
   ⛔ DAVETSİZ: ikinci tiyatro / ikinci tribün · antik harabe · Roma amfitiyatrosu görünümü · sütun / heykel / tapınak · stadyum
      · göl / gölet / yüzme havuzu (su basmış çanak) · tekne · fıskiye (yıkama püskürtmesi) · havai fişek · konfeti · lazer ·
      sahne dumanı · hale · drone gölgesi · yazı / afiş / tabela / logo · kule vinç · ikinci kabuk
❹ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: açığa çıkan yaylar = S0–S2 pompalar · temiz yüzey = S3 yükleyiciler
                  · açık taş = S4 yıkama · merdiven = S5 taş blokları · tahtalar = S6 · ızgara = S7 · sahne = S8 · kaburgalar =
                  S9 · kabuk = S10 · kuleler + basamak lambaları = S11 · yollar = S12 · boş saha = S13 · topluluk = S14 minibüs ·
                  ışıklar = S15 şalter panosu · seyirci = S16–S17 yollar · ana ışık = S18 kule platformu
❹ ÇERÇEVE DEFTERİ dış kenar 266 → 1654 sabit · kaya 98 px sabit · teras sayısı 12 · merdiven sayısı 3
❹ GİZLİ İŞ        suyun arıtılması → gri tanklar + sol kenara giden boru · harç kuruması → yeni blokların açık derzleri · elektrik
                  tesisatı → ekiplerin kulelere ve lambalara döşediği kablolar · ses kontrolü → sahnenin solundaki şalter panosu
❹ DECLARED WORLD  sonbahar ormanında çukur · tek vinçli onarım (G5–G13) · tek akşam (G15–G20) · G rejimi (S18–S19) · kış YOK · gece YOK
❸ PARKED GEREKÇESİ S19 (final tutuşu): yapı bitti; yalnız alkış, müzik ve rüzgâr — ödül ve yaşayan an, işsiz aralık değil, beyanlı
                  [P4-f · C1-d]
```

---

## 6. ❷ ZAMAN VE KESME — kesme listesi ve ses (❷ kör koşar; bu bölüm ❺ ve operatör içindir)

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_SUNKEN_STAGE/THE_SUNKEN_STAGE_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
REJİM KESMELERİ      32,0 (S3 A → S4 B) · 40,0 (S4 B → S5 A) · 48,0 (S5 A → S6 B) · 56,0 (S6 B → S7 A) · 80,0 (S9 A → S10 B) ·
                     88,0 (S10 B → S11 A) · 144,0 (S17 A → S18 G) — rejim değişimi YALNIZ kesmede [P5-c]
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı, su çizgisi, lamba, seyirci ATLAMAZ ·
                     8,0 ve 16,0 (TEK TAHLİYE) · 128,0 · 136,0 · 144,0 · 152,0 (TEK AKŞAM)
MÜZİK                ✅ VAR — 120 BPM · 4 ölçü/sahne · THE_SUNKEN_STAGE_MUZIK.md: 0–56 müzik YOK (su, pompa, çamur, yıkama, taş,
                     ahşap) · 56–104 müzik doğar ve büyür (motif 72,0'de) · 104–144 müzik çekilir (orman, adımlar, akort, seyirci;
                     ≈114'te motif bir kez sahneden) · 144–160 motif sahnedeki topluluğun açılış parçası, 152'den alkış — ani
                     kesilme yok
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G10 (S9 ↔ S10) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si (S9) G10 karesinde biter; G10 BOLUM_2'nin ilk görselidir.
ELLE KARE            ffmpeg -ss 80.0 -i teslim.mp4 -frames:v 1 sinir.jpg → yedi çıplak kaburga sahnenin arkasında, kabuk KAPLANMAMIŞ ·
                     ahşap sahne tamam · 12 sırada ahşap tahta · vinçte kabuk paneli sandığı · iki makaslı platform · pompalar yolda ·
                     gölge +29° · öğleden sonra
```

---

## 8. ❺ TESLİM — belgeli merceğin okuyacağı beyanlar

```
VAAT            Ormandaki su basmış bir çukurun altından dev bir açık hava tiyatrosu çıkar, onarılır ve aynı akşam konserle açılır.
DİRENÇ          ① su — S0–S2 (0,0–24,0) pompalarla, tek yönde · ② çamur ve kir — S3 (24,0–32,0) · S4 (32,0–40,0) · ③ hasar ve
                eksik — S1'de görünen kırık merdiven (S5, 40,0–48,0) · çıplak sahne (S7–S8) · kabuk yok (S9–S10) · ışık yok (S15) ·
                ④ boş sıralar — S0–S15 (0,0–128,0)
BEDEL           su + şantiye: S2'de su, S3'te çamur, S4'te kir, S13'te vinç + pompalar + tanklar + paletler gider; G20'de aynı yerde
                ışıklı, dolu tiyatro
AÇILIŞ          nesne: kahverengi suyun içinden çıkan iki taş yay · eylem: su ilk karede alçalıyor · ipucu: yayların aynı merkezli
                olması + sol üstte pompalar · MERAK SORUSU: "Suyun altında ne var?"
İŞLEV ANI       S15 (120,0–128,0) lambalar · S16–S17 (128,0–144,0) seyirci · S18 (144,0–152,0) ana ışık + müzik · S19 (152,0–156,0)
                alkış · 156,0–160,0 tutuş
LOOP RHYME      su çizgisinin yayı (G0) ↔ ön sıradaki seyircinin yayı (G20), aynı merkez · kaya aynı x'te
OMURGA (20)     boşaltır · açığa çıkarır · kurutur · temizler · yıkar · onarır · oturtur · çatar · kaplar · diker · kaplar · kurar ·
                döşer · boşaltır · yerleştirir · yakar · getirir · doldurur · açar · alkışlatır
SES             MUSIC YES — none 0–56 s, rises 56–104, steps back 104–144, comes FROM THE STAGE 144–160 with applause (❷ C2 · ❺ C1)
TESLİM          END CARD NO · SPEED 1x · 160,0 sn · SECOND STATION NO · REAL TIME (S18–S19) declared · ON-SCREEN TEXT NO
AI BEYANI       YAYIN_PAKETI §DESCRIPTION (sahibin "This is a cinematic visualization, not footage of a real restoration.") + sabit
                beyan bloğu + Studio "Altered content = EVET"
KAPAK           THE_SUNKEN_STAGE_KAPAK.md — G20'den, bölünmüş yerleşim YOK · varsayılan "THE SUNKEN STAGE" başlıklı, yazısız yedek
PROMPT KAPISI   python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_SUNKEN_STAGE → BLOCK 0 · FIX 2 (12.10.2026) — ikisi de
                PLAN §ÜRETİM ÖNCESİ DURUM'da beyanlı (araç kutu seti · düz ızgara)
```

---

## 9. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) + ⑨ 16 mm + ⑩ rejim G · sonuç THE_SUNKEN_STAGE_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  00_ANALIZ/02 §3 — kamera (16 mm · h 22 · tilt 27°) · 12 yay ve 3 merdiven sayılıyor mu · sahne üst ortada mı ·
                  gök bandı (0–105) okunuyor mu · kaya (98 px) · yanlarda gerilme
⛔ PİLOT ÜÇLÜ     ① G20 + G19 + G18 + S18 + S19 · ② G0 + G1 + S0 · ③ G15 + G16 + S15 — PLAN §PİLOT ÜÇLÜ · sonra S1, S2, S10, S16
⛔ USTA KARE      G20 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu · gök mavi mi (siyah değil)
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil); kaya 98 ±2 px · dış kenar 266 / 1654 ±2 px
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a; 1920×1080 · 160,0 sn · kart YOK)
⛔ İHRAÇ          bash araclar/ihrac_kontrol.sh — süre 160,0 · kart YOK · müzik VAR · yazı YOK · final tutuşu SSIM ≥ 0,90 [DERS 63]
⛔ KAPAK KANITI   ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
⛔ SÜRE / KLASÖR  160 sn yatay_2_dk bandının dışı — sahip kararı (hikâye SAPMA ②)
```
