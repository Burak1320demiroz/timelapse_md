# 🔍 THE_SLOW_TAKEOFF — QA SPEC

> THE SLOW TAKEOFF · 16:9 · 30 × 8,0 sn · 240,0 sn · kart yok · müzik var. **Bu dosya yalnız belgeli merceklere
> verilir: ❹ İNŞA · ❺ TESLİM** (beş mercekli QA, 06.10.2026 [DERS 64]).
> ⛔ **❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❸ ŞANTİYE'ye VERİLMEZ** — üçü kör koşar, ayrı geçici sohbette, proje dışında
> [`QA_KOSU_KILAVUZU` §1]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit değildir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_4_dk_filmler/THE_SLOW_TAKEOFF <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].
> Ham raporlar `QA/HAM/THE_SLOW_TAKEOFF/THE_SLOW_TAKEOFF_Q<n>_<AD>_HAM.md` · kayıt `QA/FILMLER/THE_SLOW_TAKEOFF.md` · `QA/TABLO.md`.

---

## 0. KÜNYE

```
FİLM          THE_SLOW_TAKEOFF — çayırda yatan emekli bir yolcu jeti iki çelik çerçeveyle yerden kaldırılıp göl evine
              dönüşür · göl kıyısı çayırı · MAIN STATION + COCKPIT STATION (2 klip)
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_4_dk_filmler · HIZ 1x
KANARYA       copperlark   ⛔ kör mercek raporunda bu kelime geçerse plan SIZMIŞTIR → koşu SIZINTI [QA_KOSU §3.1]

TESLİM YAPISI ⭐ SAHNE BLOĞU  30 sahne × 8,0 sn = 240,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  ⛔ YOK                                   ← son sahne S29 son saniyeye kadar SAHNEDİR
                 TOPLAM                          240,0 sn
              ⛔ 240,0 sn'den uzun dosya = plan dışı kart/siyah → ❺ "the plan declares NO card — report it"

SAHNE SAATLERİ  sahne n = n × 8,0 → (n+1) × 8,0   ·   S0 0,0–8,0 · … · S14 112,0–120,0 · S15 120,0–128,0 · … · S29 232,0–240,0
                (120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · her kesme ölçü başında · 29 kesme)
PART GRID       — (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)
⛔ DÜZ IZGARA   sahip senaryosu (07.10.2026) · ⚠️ bandın dışı (format 24 × 10,0). Eşit klipte ❷ RHYTHM NOT TRIGGERED;
                METRONOM hükmü beş mercekli rubrikte yok. Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]: ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — {5,9} ya da {5,10}
   gerekir; {4,6,8} çıkarsa iki-klip hükmü (PLAN §DEĞİŞMEZLER) ve karar sahibe döner.

YAPI          emekli, markasız dar gövde yolcu jeti · boy 33,0 m · kanat açıklığı 29,0 m · gövde Ø 3,8 m · kuyruk +10,5 m
              (gövde altından) · 2 kırmızı çelik çerçeve (4 kolon + 2 üst kiriş) · 2 semer · teras 9 × 7 m · merdiven
SAHA          ılıman göl kıyısı çayırı 47° K · çapalar: meşe (sol) · kayıkhane (sağ, kanıt) · karşı kıyı + tepe sırtı · kaya
ZAMAN YAYI    ≈10 ay (yaz sonu → ertesi yaz başı) · film mertebe anlatır: "bir sonbahar, bir kış, bir bahar seli" [P1-c]
IŞIK          TEK GÜN 07:40 → 19:20 (mavi saat) · Σ rejim 11 sa 40 dk · takvim SAHADAN · bilinçli sıkıştırma (ÜSLUP BEYANI)
REJİM         A (10 dk) × 22 · B (2 sa) × 4 (S2 · S9 · S18 · S19) · G (gerçek zaman) × 2 (S28 · S29) — ⚠️ üç rejim, beyanlı
KAMERA        MAIN STATION — h 3,0 m · D_eksen 50,0 m · bakış 0° · tilt 0° · roll 0°
              ⭐ İKİNCİ İSTASYON BEYANI: COCKPIT STATION — h 8,2 m · ön cama 2,4 m · bakış 270° · tilt 0° · YALNIZ S13 (104,0–112,0)
              ve S21 (168,0–176,0). İki kokpit klibi bir önceki ana klibin AYNI on dakikasıdır; dıştaki yapı iki yakada aynı.
              Sahip kararı 07.10.2026 ("tek kamera + 2 kokpit"). ❶ bunu SEPARATE IMAGES saymamalı: iki istasyon, ortak çapa.
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G30 usta kare → G29 → … → G0 · kokpit: G13′ → G13 · G21 → G21′ · her kare zincir_kontrol
GÜNLÜK        THE_SLOW_TAKEOFF_URETIM_GUNLUGU.md — ⛔ boş (üretim başlamadı) → bu SPEC'in hükmü üretimle başlar
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı · ❺ FINAL BEAT

```
SAHNE       S29 (232,0–240,0)
FİNAL BEAT  232,0–236,0 olay: kano gövdenin altından çıkar, ikinci çerçeveyi geçer, su yolu ağzına varır ·
            236,0–240,0 TUTUŞ: kano su yolu ağzında yavaşça durulur, ışıklar yanık, başka hiçbir şey değişmez
SANİYE      239,0 (son 4,0 sn'lik TUTUŞUN içi [P2-i]; mavi saat, okunur [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (dördü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① ışıklı ev: kokpit + gövde boyunca pencere sırası + teras ve merdiven lambaları — gövde altı %57,1, kuyruk %82,0
   ② göletteki yansıma (üstten 786–883) — gövdenin eskiden yattığı yer SU
   ③ kano su yolu ağzında, kadrajın İÇİNDE (x ≈1293 · üstten 624 · 128 px) — çıkmadı [BACK TO WATER dersi]
   ④ AYNI kayıkhane (kanıt nesnesi: x 1548–1698 · üstten 510–593 · 150 × 83 px — G0 ile aynı konum ve boy)
   + geçici ekipman GİTMİŞ: vinç YOK · kriko YOK · iskele kulesi YOK · kamyon YOK (SÖKÜM satırı)
   + BEDEL görünür: çamurlu yatak yerine su (G0 üstten 617 çamur ↔ G30 su + yansıma)

KOMUT
   ffmpeg -ss 239.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①–④'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP (biçim kafiyesi, ışık bilinçli farklı)
   ffmpeg -ss 0.3   -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 239.5 -i teslim.mp4 -frames:v 1 kanit_g30.jpg
   İki karede meşe gövdesi, kayıkhane, kaya ve karşı kıyı aynı yerde; uçak aynı x'te (537–1383 ±2 px).
   Işık: G0 07:40 sabah ↔ G30 mavi saat (PLAN LOOP satırı) — kanıt çifti AYNI IŞIK iddiası taşımaz.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=3,0 · D=50,0 · tilt 0 · yatay: yüzde = 50 + 118,5·(y−h)/D, ALT kenardan)

| nesne | y (m) | yüzde (alt kenardan) | x (soldan) | px boy | her karede |
|---|:-:|:-:|:-:|:-:|---|
| ufuk = karşı kıyı çizgisi (tilt 0) | — | 50,0 | — | — | ✓ |
| gövde altı (G0–G5) | 0 | 42,9 (üstten 617) | 537–1383 | — | ✓ G0–G5 |
| gövde altı (G6) | +3,0 | 50,0 (540) | 537–1383 | — | ⭐ yalnız G6 — kıyı çizgisinde |
| gövde altı (G7–G30) | +6,0 | 57,1 (463) | 537–1383 | — | ✓ G7–G30 (geri inmez) |
| kuyruk tepesi | +10,5 → +16,5 | 67,8 → 74,9 → 82,0 | ≈1350 | — | G0–G5 · G6 · G7–G30 |
| gövde boyu | — | — | 537–1383 | 846 px en | ✓ BİREBİR ±2 px [P21-c] |
| çelik çerçeve kolonları (yakın) | 0 → +11,5 | — | 740 · 1180 | — | G4–G30 |
| çerçeve üst kirişi | +11,5 | 70,1 (322) | 740–1180 | — | G4–G30 |
| ⭐ kanıt nesnesi KAYIKHANE | −0,5 → +5,0 | 45,1–52,8 (510–593) | 1548–1698 | 150 × 83 | ✓ BİREBİR (boy dâhil) |
| çapa ① MEŞE gövdesi (SOL) | +1,0 → +17 | 44,7 taban · 86,9 taç | ≈163 | taç ≈455 en | ✓ gövde; taç mevsimle değişir |
| çapa ③ tepe sırtı (uzak) | — | ≈61,2 (419) | bütün en | — | ✓ |
| çapa ④ KAYA (sağ alt) | 0 → +1,5 | 14,4–32,2 (732–924) | ≈1728 | ≈190 | ✓ |
| vinç bom başı / en yüksek kaldırma | ≈+15 | ≈78 | ≈1300 | — | yalnız G0–G4 · S3'te üst kiriş göğe karşı (beyanlı) [DERS 22] |
| kano (G28 · G29 · G30) | −0,3 | 37 · 36 · 36 (646 · 628 · 624) | 608 · 960 · 1293 | 160 · 133 · 128 | yalnız G25–G30 |

```
KOKPİT STATION   ufuk %50 · altı ön cam ≈1500 px en, kadrajın üst-orta bandı · meşe tacı sol camlarda · tepe sırtı
                 ve karşı kıyı ön camdan · mobilya alt üçte bir · S13 ve S21'de aynı (kamera hiç kıpırdamaz)
KAMERA SABİTLİK  ilk/son kare kayması ≤ 2 px (1080p · KAMERA_ISTASYONU §7 · zincir_kontrol ESIK_KAYMA_ORAN) ·
                 üç nirengi: meşe gövdesi · kayıkhane sağ köşesi · kaya tepesi
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
uçak 33,0 m · kanat 29,0 m · gövde Ø 3,8 m · kuyruk +10,5 (gövde altından) · 6 kokpit camı · tek sıra kabin penceresi ·
ön kabin kapısı (burundan 3,5 m) · kanat üstü çıkış · motor 2 (öndeki S0'da gider; arkadaki gövde arkasında, görünmez)
gövde altı 0,0 (G0–G5) → +3,0 (G6) → +6,0 (G7–G30)
temel 4 × (2,0 × 2,0) beton · çerçeve 2 × (2 kolon + 1 üst kiriş +11,5) kırmızı astar · strand jack 4 (S3 → S17)
semer 2 (kavisli çelik, kolon braketlerine pimli +5,7) · teras 9 × 7 m, kot +7,2, 4 dikme · korkuluk + lamba dizisi
merdiven 2 kesit + ara platform (kapı +8,0 → kuru sırt +1,0) · gölet ≈30 × 40 m (−0,3) · su yolu ≈25 m · iskele 6 m ·
kano 5,0 m koyu yeşil ahşap · vinç: sarı mobil teleskopik (yalnız G0–G4)
```

### Yapı yüzdesi ve saha durumu — sahne sahne (❹ İNŞA · ❺ TESLİM için)

| S | saat | yapı: eleman + ara hâl | taç (kuyruk) yüzdesi | geçici ekipman kadrajda | saha / mevsim taşıyıcısı |
|:-:|:-:|---|:-:|---|---|
| S00 | 07:40→07:50 | uçak yerde · motor 2 → 1 (öndeki vinçte) | %67,8 | vinç (motor yükte) · kamyon · ekskavatör | yaz sonu · sabah sisi |
| S01 | 07:50→08:00 | motor 1 (görünür 0) · sarmaşık %100 → %0 | %67,8 | vinç (gider) · kamyon (gider) · 2 platform · yıkama arabası | yaz sonu |
| S02 | 08:00→10:00 | temel 0 → 4 | %67,8 | ekskavatör · mikser · donatı yığını · S2 sonu vinç + uzun kamyon | yaz sonu → erken güz |
| S03 | 10:00→10:10 | çerçeve 0 → 2 · kriko 0 → 4 | %67,8 | vinç (kolon yükte) · uzun kamyon · telehandler | erken güz |
| S04 | 10:10→10:20 | semer 0 → 2 · halat gergin | %67,8 | vinç (semer yükte → gider) · ekskavatör | erken güz |
| S05 | 10:20→10:30 | gövde altı 0 → +3,0 m | %67,8 | 4 kriko + halat · telehandler · 2 platform | erken güz |
| S06 | 10:30→10:40 | gövde altı +3,0 → +6,0 m | %74,9 | aynı | erken güz |
| S07 | 10:40→10:50 | yük çerçevede · halat gevşek | %82,0 | aynı · pim paleti | erken güz |
| S08 | 10:50→11:00 | teras çerçevesi %100 | %82,0 | kriko (gevşek halat) · uzun kamyon · kazık makinesi · 2 platform | erken güz |
| S09 | 11:00→13:00 | teras döşemesi %0 → %100 | %82,0 | kriko · kamyon (döşeme istifi) · telehandler | meşe yeşil → altın |
| S10 | 13:00→13:10 | merdiven %100 | %82,0 | kriko · kamyon (merdiven) · telehandler | meşe altın |
| S11 | 13:10→13:20 | cam %0 → %100 | %82,0 | kriko · 2 iskele kulesi · kamyon (cam) · telehandler | meşe bronz |
| S12 | 13:20→13:30 | (iç) yalıtım + zemin · palet 4 → 0 | %82,0 | kriko · 2 iskele · kamyon (4 palet) · telehandler | meşe bronz |
| S13 | 13:20→13:30 | 🪟 kokpit köşesi %100 | — (kokpit) | — (kokpit: el arabası) | meşe bronz (camdan) |
| S14 | 13:30→13:40 | (iç) mutfak · sandık 3 → 0 | %82,0 | kriko · 2 iskele · kamyon (3 sandık) · telehandler | meşe bronz |
| S15 | 13:40→13:50 | (iç) yatak · yük 2 → 0 | %82,0 | kriko · 2 iskele · küçük kamyon (yatak) | meşe bronz, seyrek |
| S16 | 13:50→14:00 | korkuluk + lamba dizisi + bank + saksı | %82,0 | kriko · 2 iskele · kamyon (korkuluk) · telehandler | meşe kahve |
| S17 | 14:00→14:10 | kriko 4 → 0 · iskele 2 → 0 | %82,0 | kriko 4 → 0 · iskele 2 → 0 · telehandler · kamyon (gider) | gri gök · meşe kahve |
| S18 | 14:10→16:10 | ev tamam · kar | %82,0 | teslimat aracı · küçük yükleyici | kış ①: yaprak düşer · kar |
| S19 | 16:10→18:10 | ev tamam · erime · su girer | %82,0 | yükleyici · pompa · kum torbası | kış ②: erime · su sağdan |
| S20 | 18:10→18:20 | ev tamam · su yatağı kaplar | %82,0 | yükleyici · pompa · kum torbası | bahar seli · yeşil pus |
| S21 | 18:10→18:20 | 🪟 kokpit (değişmez) | — (kokpit) | — | yağmur (camdan) |
| S22 | 18:20→18:30 | ev tamam · su çekilir | %82,0 | pompa · yükleyici (torbaları götürür) | taşkın doruğu → çekilme |
| S23 | 18:30→18:40 | gölet + su yolu | %82,0 | ekskavatör · damperli kamyon · taş paleti | bahar · ıslak çayır |
| S24 | 18:40→18:50 | kıyı bitkisi + basamak taşı | %82,0 | yükleyici · römork · toprak yığını | bahar → yaz başı |
| S25 | 18:50→19:00 | yürüyüş iskelesi + kano | %82,0 | küçük kamyon · telehandler (gider) | yaz başı · gün batımı |
| S26 | 19:00→19:10 | ışık 4 grup | %82,0 | YOK | yaz başı · mavi saat |
| S27 | 19:10→19:20 | (değişmez) · bir kişi iner | %82,0 | YOK | mavi saat |
| S28 | 19:20 +8 sn | (değişmez) · kano | %82,0 | YOK | derin mavi saat |
| S29 | 19:20 +8 sn | (değişmez) · kano · TUTUŞ | %82,0 | YOK | derin mavi saat |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   KAYIKHANE — G0…G30 (ana) hepsinde x 1548–1698 · üstten 510–593 · 150 × 83 px; zincirde her karede ELLE ✓/✗
                (günlük §2) · taşkında (G20 · G22) yalnız kazıkları ıslanır; G22 → G30 kazıklarda soluk silt bandı AYNI yükseklikte
İKİNCİ ÇAPA     meşe GÖVDESİ x ≈163 (taç değil — mevsimle değişir) · üçüncü: kaya x ≈1728 · dördüncü: karşı kıyı %50
❸ İÇİN          dikiş = KARE (G1…G29 ana): dikişin iki yakası aynı görsel; ❸ REBUILT hükmü zincir koşulmadı demektir ·
                kokpit kesmeleri (S12 → S13 → S14 · S20 → S21 → S22) istasyon değişimidir, dış kare iki yakada AYNI
```

---

## 5. ❹ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ajanı · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | ajan (taşıyan) | geçici destek | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|---|:-:|:-:|:-:|
| öndeki motor (GİDEN) | kanat altı | sarı mobil vinç → kamyon | iki sapan + iki kılavuz ip | G0 (vinçte) | — | G2 (kamyonla gider) |
| sarmaşık + kir (GİDEN) | gövde | ekip, iki platform, yıkama arabası | branda yığını · römork | G1 | — | G2 |
| temel × 4 | ekskavatör yanında donatı kafesi yığını · mikser | ekskavatör · ekip · mikser | kalıp kenarı · donatı kafesi | S2 içi | G3 | — |
| çelik çerçeve × 2 | uzun kamyon (S2 sonu) | vinç · riggers | kısa sapan · ankraj bulonları | G3 (ilk kolon kancada) | G4 | kalıcı |
| strand jack × 4 + halat | aynı kamyon | telehandler | — | G4 | G4 | G18 (S17'de telehandler indirir) |
| semer × 2 | aynı kamyon | vinç (hendekten geçirir) · ekskavatör | sapan · hendek | G4 (kancada) | G5 | kalıcı |
| kalkış (gövde) | — | 4 strand jack | 4 gergin halat | G5 (gergin, yerde) | G7 (+6,0) | — |
| yük aktarımı | telehandler pim paleti | riggers | pim + braket | G7 | G8 | halat gevşer G8 |
| teras çerçevesi | uzun kamyon + kazık makinesi | telehandler · riggers | kazık · dikme | S8 içi | G9 | kalıcı |
| teras döşemesi | kamyonda yüksek istif | telehandler · marangozlar | — | S9 içi (burundan kuyruğa) | G10 | — |
| merdiven | kuru sırtta kamyon | telehandler · riggers | kısa sapan | S10 içi | G11 | kalıcı |
| cam (yeni) | kamyonda sandıklar | camcılar · iskele kuleleri · telehandler | iskele kulesi × 2 | S11 içi (burundan kuyruğa) | G12 | iskele G18 |
| (gizli) yalıtım + zemin | merdiven dibinde 4 palet | işçiler (merdiven) · telehandler | — | G12 (4 palet) | G14 (palet 0) | kamyon gider |
| 🪟 kokpit köşesi | kabinden el arabası | işçiler | — | G13 (boş) | G13′ | — |
| (gizli) mutfak | sağda kamyonda 3 sandık + tezgâh | telehandler → kanat kapısı · ekip | alçak araba | G14 | G15 (sandık 0) | boş sandık S15 |
| (gizli) yatak | merdiven dibinde küçük kamyon | işçiler (merdiven) | — | G15 | G16 | kamyon gider |
| korkuluk + lamba dizisi + bank + saksı | sağda kamyon | telehandler · montajcılar | — | G16 | G17 | — |
| kum torbası (GEÇİCİ) | yükleyici paleti | yükleyici · işçiler | — | S19 içi | G20 | S22 (palete, yükleyici götürür) |
| gölet + su yolu | ıslak çukur · işaretli hat | ekskavatör → damperli kamyon · ekip | taş paleti | G23 | G24 | — |
| kıyı bitkisi + basamak taşı | römork · toprak yığını · taş paleti | bahçıvanlar · yükleyici · ekip | — | G24 | G25 | — |
| yürüyüş iskelesi + kano | merdiven dibinde küçük kamyon | ekip · telehandler | sapan (kano) | G25 | G26 | kamyon gider |
| ışık (4 grup) | S16'da takılan sönük lamba dizisi + kabin | — (elektrik — gizli iş) | — | G26 | G27 | — |

```
❹ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır):
   uçak 1 · sarı mobil vinç 1 (G0–G4) · kamyon (düz kasa/uzun/küçük) · ekskavatör 1 · mikser 1 · kazık makinesi 1 ·
   telehandler 1 · iş platformu 2 · yıkama arabası 1 · iskele kulesi 2 · teslimat aracı 1 · küçük yükleyici 1 · pompa 1 ·
   damperli kamyon 1 · römork 1 · ekip (iz) · S27 bir kişi (iz) · S28–S29 kanoda bir kişi (siluet) · kano 1 (G25+) ·
   meşe 1 · kayıkhane 1 · kaya 1 · ışık grubu 4 (kabin önü · orta · arka · teras + merdiven lambaları)
   ⛔ DAVETSİZ: ikinci uçak · gökte uçak · tekne (kano dışında) · su kuşu sürüsü · deniz uçağı şamandırası · iniş takımı ·
      havalimanı ögesi · yazı/işaret · gantri vinci · kule vinç
❹ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: kalkış = S4'te gerilen halatlar · su = S19'da kıyıdan
                  gelen sel · gölet = S22'de çukurda kalan su · ışık = S16'da takılan sönük lamba dizisi (P11-d)
                  (kaldırma karede biter — DERS 57: G6 yarım, G7 tam; kalkış YALNIZ düşey)
❹ ÇERÇEVE DEFTERİ (framing ledger) gövde altı üstten 617 (G0–G5) → 540 (G6) → 463 (G7–G30) · kuyruk 348 → 271 → 194 ·
                  teras kotu %63 · iskele kotu %36–37 · gölet bandı alt %43 · gövde boyu 846 px sabit
❹ GİZLİ İŞ        yalıtım · mutfak · yatak → görünür vekil: eksilen palet/sandık/yük + merdiven ve kanat kapısı trafiği ·
                  elektrik → ışık grupları · temel kazıkları → kazık makinesi
❹ DECLARED WORLD  göl kıyısı çayırı · göl · sel (S19–S22) · gölet + su yolu (S23+) · kıyı bitkileri · insanlı ekip · kano ·
                  tek kişi (S27–S29) · kış (S18–S19) · mavi saat (S26–S30)
```

---

## 6. ❷ ZAMAN VE KESME — kesme listesi ve ses (❷ kör koşar; bu bölüm ❺ ve operatör içindir)

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 232,0  (29 kesme, her 8,0 sn — DÜZ, hepsi ölçü başı)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_4_dk_filmler/THE_SLOW_TAKEOFF/THE_SLOW_TAKEOFF_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
İSTASYON KESMELERİ   104,0 (ana → kokpit) · 112,0 (kokpit → ana) · 168,0 (ana → kokpit) · 176,0 (kokpit → ana)
REJİM KESMESİ        216,0 (S27 A → S28 G gerçek zaman) — rejim değişimi YALNIZ kesmede [P5-c]
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                ✅ VAR · 120 BPM · müziksiz pencere 0,0–8,0 (S0) · katman girişleri: 8,0 (nabız) · 24,0 (ritim belirginleşir) · 40,0 (kalkış — genişler) ·
                     136,0 (kış — incelir) · 152,0 (yağmur, su — yalnız dokular) · 176,0 (dönüş) · 208,0 (mavi saat) ·
                     final tutulan akor 232,0–240,0, ani kesilme yok · diegetik yatak müziğin altında sürer
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G15 (S14 ↔ S15) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si (S14) G15 karesinde biter; G15 BOLUM_2'nin ilk görselidir (ANA istasyon).
ELLE KARE            ffmpeg -ss 120.0 -i teslim.mp4 -frames:v 1 sinir.jpg → gövde altı %57,1 · gölge +39° · ince yüksek bulut ·
                     meşe bronz · kriko + iki iskele kulesi kadrajda · küçük kamyon merdiven dibinde (yatak)
KOKPİT               S13 sınıra DÜŞMEZ (SAPMA ⑧) — sınır iki kameraya bölünmez
```

---

## 8. ❺ TESLİM — belgeli merceğin okuyacağı beyanlar

```
VAAT            Göl kıyısında çürüyen bir yolcu uçağını bütünüyle yerden kaldırıp altında su, üstünde hayat olan bir göl evine dönüştürmek.
DİRENÇ          ① ağırlık — S5–S6 (40,0–56,0) gergin halatlar, çamurdan kopan gövde · ② su — S19–S20 (152,0–168,0) kıyı çizgisi
                sağdan yürür, kolon diplerini sarar, ev kuru · ③ kış — S18 (144,0–152,0) kar
BEDEL           çamurlu yatağında yatan ölü uçak — S5 (40,0) kalkar, yatak izi kalır; S20 (160,0) su altına girer; S23 (184,0)
                gölete çevrilir; G30'da yalnız su + yansıma
AÇILIŞ          nesne: çamurdaki uçak (kadraj eninin ≈%44'ü) · eylem: vinç ilk karede motoru taşıyor · ipucu: çayırdaki istif ·
                MERAK SORUSU: "Bu uçağa ne yapıyorlar?"
İŞLEV ANI       S26 (208,0) ışıklar gruplar hâlinde yanar · S28 (224,0–232,0) kano gerçek hızda gövdenin altından geçer ·
                S29 (232,0–236,0) su yolu ağzına varır · 236,0–240,0 tutuş
LOOP RHYME      biçim ve konum: uçak aynı x'te (537–1383) · gövde altının yeri çamur → su · kayıkhane, meşe, kaya aynı
OMURGA (30)     motor · sarmaşık · temel · çerçeve · beşik · yarı · tepe · oturur · teras çatısı · döşeme · merdiven · cam ·
                yalıtım · kokpit · mutfak · yatak · korkuluk · söküm · kar · erime · sel · yağmur · çekilme · gölet · yeşil ·
                iskele · ışık · iniş · kano · durulma
SES             MUSIC YES — kesmeler ölçü başında · müziksiz pencere 0,0–8,0 sn (S0 tamamı) (❷ C2 · ❺ C1)
TESLİM          END CARD NO · SPEED 1x · 240,0 sn
AI BEYANI       YAYIN_PAKETI §AÇIKLAMA sabit beyan bloğu + Studio "Altered content = EVET"
KAPAK           THE_SLOW_TAKEOFF_KAPAK.md — G30'dan, bölünmüş yerleşim YOK
```

---

## 9. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_SLOW_TAKEOFF_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  00_ANALIZ/02 §3 — kamera · gövde · çerçeve · çapalar · gölet · yansıma bandı · kano rotası
⛔ PİLOT ÜÇLÜ     ① G30 + G29 + S29 · ② G5–G7 + S5–S6 · ③ G20 + G22 + S20 (+ kokpit S13) — PLAN §PİLOT ÜÇLÜ
⛔ USTA KARE      G30 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil); gövde boyu 846 ±2 px
⛔ GÜNLÜK         klip başına satır (İSTASYON sütunu: ana/kokpit); günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a; 1920×1080 · 240,0 sn · kart YOK)
⛔ İHRAÇ          bash araclar/ihrac_kontrol.sh — süre 240,0 · kart YOK · müzik VAR · final tutuşu SSIM ≥ 0,90 [DERS 63]
⛔ KAPAK KANITI   ffmpeg -ss 239.5 -i teslim.mp4 -frames:v 1 g30_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g30_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
```
