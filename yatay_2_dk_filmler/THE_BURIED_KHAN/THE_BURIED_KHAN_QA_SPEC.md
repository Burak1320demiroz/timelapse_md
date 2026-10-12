# 🔍 THE_BURIED_KHAN — QA SPEC

> THE BURIED KHAN · 16:9 · 15 × 8,0 sn · 120,0 sn · kart yok · müzik yok (ses tasarımı). **Bu dosya yalnız belgeli
> merceklere verilir: ❹ İNŞA · ❺ TESLİM** (beş mercekli QA, 06.10.2026 [DERS 64]).
> ⛔ **❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❸ ŞANTİYE'ye VERİLMEZ** — üçü kör koşar, ayrı geçici sohbette, proje dışında
> [`QA_KOSU_KILAVUZU` §1]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit değildir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_BURIED_KHAN <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].
> Ham raporlar `QA/HAM/THE_BURIED_KHAN/THE_BURIED_KHAN_Q<n>_<AD>_HAM.md` · kayıt `QA/FILMLER/THE_BURIED_KHAN.md` · `QA/TABLO.md`.

---

## 0. KÜNYE

```
FİLM          THE_BURIED_KHAN — çölde 12 m'lik bir kum tepesinin altındaki taş kervansaray kumdan çıkarılır, yıkık bölümü
              örülür, kapısı asılır, fenerleri yakılır ve kapıları içeriden açılır · MAIN STATION (tek istasyon)
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_2_dk_filmler · HIZ 1x
KANARYA       sandwren   ⛔ kör mercek raporunda bu kelime geçerse plan SIZMIŞTIR → koşu SIZINTI [QA_KOSU §3.1]

TESLİM YAPISI ⭐ SAHNE BLOĞU  15 sahne × 8,0 sn = 120,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  ⛔ YOK                                   ← son sahne S14 son saniyeye kadar SAHNEDİR
                 TOPLAM                          120,0 sn
              ⛔ 120,0 sn'den uzun dosya = plan dışı kart/siyah → ❺ "the plan declares NO card — report it"

SAHNE SAATLERİ  sahne n = n × 8,0 → (n+1) × 8,0   ·   S0 0,0–8,0 · … · S7 56,0–64,0 · S8 64,0–72,0 · … · S14 112,0–120,0
                (14 kesme, her 8,0 sn · müzik yok — ölçü ızgarası yok)
PART GRID       — (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)
⛔ DÜZ IZGARA   format varsayımı (hikâye SAPMA ⑬) + sahip izinli 15 × 8,0 varyantı · ⚠️ bandın dışı (format 12 × 10,0). Eşit
                klipte ❷ RHYTHM NOT TRIGGERED; METRONOM hükmü beş mercekli rubrikte yok. Karşı kayıt [DERS 44].
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]: ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — {5,9} ya da {5,10}
   gerekir; {4,6,8} çıkarsa iki-klip hükmü (PLAN §DEĞİŞMEZLER) ve karar sahibe döner.

YAPI          iki katlı kumtaşı kervansaray · 60 m cephe · alt kat 0 → +5 · 16 kemerli galeri +5 → +9 · kapı çerçevesi 12 m en,
              +15 · sivri kemer 5 × 8 m · iki kanatlı ahşap kapı · iki kubbe başlıklı köşe kulesi (Ø 6 · +13) · gedik 10 m
              (x +12…+22, +4'e kadar, 4 kemer) · ön avlu 60 × 20 m taş döşeme · set + hurma dalı çit · 16 demir fener
SAHA          sıcak çöl, düz kum ve çakıl · 30° K · çapalar: ⭐ kuru AKASYA (sol, kaya yükseltisinde — kanıt) · MASA DAĞI (sağ
              ufuk) · ufuk düz %50 · ⚠️ kumul çapa DEĞİL (bedel)
ZAMAN YAYI    ≈11 ay (kış → ertesi sonbahar) · film mertebe anlatır: "bir kış kum, bir bahar taş, bir yaz rüzgâr, bir sonbahar ışık" [P1-c]
IŞIK          TEK GÜN 06:00 → 19:20 (mavi saat) · Σ rejim 13 sa 20 dk · takvim SAHADAN (gök pusu + yeni taşın rengi) ·
              bilinçli sıkıştırma (ÜSLUP BEYANI)
REJİM         A (10 dk) × 8 (S0 · S4 · S5 · S7 · S8 · S10 · S11 · S13) · B (2 sa) × 6 (S1 · S2 · S3 · S6 · S9 · S12) ·
              G (gerçek zaman) × 1 (S14) — ⚠️ üç rejim, beyanlı
KAMERA        MAIN STATION — h 6,0 m (çöl zemininden) · D 67,0 m (cepheye) · bakış 20° · tilt 0° · roll 0° · tek istasyon
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G15 usta kare → G14 → G13 → … → G0 · her kare zincir_kontrol
GÜNLÜK        THE_BURIED_KHAN_URETIM_GUNLUGU.md — ⛔ boş (üretim başlamadı) → bu SPEC'in hükmü üretimle başlar
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı · ❺ FINAL BEAT

```
SAHNE       S14 (112,0–120,0)
FİNAL BEAT  112,0–116,0 olay: iki kapı kanadı gerçek hızda içe açılır, sıcak ışık yelpazesi avluya düşer, yük arabalı üç kişi
            son 5 m'yi yürüyüp eşikte durur · 116,0–120,0 TUTUŞ: kapılar açık, üç kişi kıpırtısız, fenerler yanık, başka
            hiçbir şey değişmez
SANİYE      119,0 (son 4,0 sn'lik TUTUŞUN içi [P2-i]; mavi saat, okunur [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (beşi de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① açık kapıdan taşan sıcak ışık (x 912–1008 · üstten 502–655 → avluda yelpaze 655–703)
   ② yanık 16 fener (galeri x 444–1476 · 483–559) — her kemerde bir
   ③ eşikte üç kişi + yük arabası, kadrajın İÇİNDE (x ≈910 · ≈30 px · yüz okunmaz)
   ④ bütün cephe: galeri kesintisiz, gedik (1189–1380) açık renkli yeni taşla örülü, iki kule
   ⑤ AYNI akasya (kanıt nesnesi: x 154–259 · taç 495 · 105 px — G0 ile aynı konum ve boy) + masa dağı (1660–1840)
   + geçici ekipman GİTMİŞ: ekskavatör, kamyon, konveyör, vinç, iskele, istif, merdiven YOK (SÖKÜM satırı)
   + BEDEL görünür: kum tepesi yok; yerinde açık kapılı kervansaray (G0 ↔ G15)

KOMUT
   ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①–⑤'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP (biçim kafiyesi, ışık bilinçli farklı)
   ffmpeg -ss 0.3   -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 119.5 -i teslim.mp4 -frames:v 1 kanit_g15.jpg
   İki karede akasya, masa dağı ve ufuk aynı yerde; akasya aynı x'te (154–259 ±2 px). Kapı çerçevesinin düz tepesi iki
   karede AYNI yerde (845–1075 · 368): G0'da kumdan çıkan uç, G15'te çerçevenin tepesi.
   Işık: G0 06:00 sabah ↔ G15 mavi saat (PLAN LOOP satırı) — kanıt çifti AYNI IŞIK iddiası taşımaz.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=6,0 · tilt 0 · yatay: yüzde = 50 + 118,5·(y−h)/D, ALT kenardan)

| nesne | y (m) | D (m) | yüzde (alt kenardan) | x (soldan) | px boy | her karede |
|---|:-:|:-:|:-:|:-:|:-:|---|
| ufuk (tilt 0, düz) | — | — | 50,0 (540) | bütün en | — | ✓ |
| kapı çerçevesi tepesi | +15 | 67 | 65,9 (368) | 845–1075 | — | ✓ (G0–G1 yalnız uç, kumdan 57 px) |
| kumul sırtı (orta · uçlar) | +12 · +10 | 67 | 60,6 (425) · 57,1 (464) | 272–1648 | — | yalnız G0–G1 |
| kule kubbesi | +13 | 67 | 62,4 (406) | 329–444 · 1476–1591 | — | ✓ |
| duvar tepesi | +9 | 67 | 55,3 (483) | 387–1533 | — | G2'de kum hizası · G3+ açık |
| kapı kemeri tepesi | +8 | 67 | 53,5 (502) | 912–1008 | — | G3+ |
| galeri kemer tabanı | +5 | 67 | 48,2 (559) | 444–1476 | — | G3'te kum hizası |
| gedik dibi | +4 | 67 | 46,5 (578) | 1189–1380 | — | G3–G6 (G7'de üzengide, G8+ örülü) |
| cephe dibi (zemin) | 0 | 67 | 39,4 (655) | — | — | G4+ |
| avlu ön kenarı | 0 | 47 | 34,9 (703) | — | — | G5+ açık |
| ⭐ kanıt nesnesi AKASYA | +3 → +9 | 85 | 45,8–54,2 (585–495) | 154–259 | 105 × 90 | ✓ BİREBİR (boy dâhil) · hiç yaprak açmaz |
| çapa MASA DAĞI (SAĞ UFUK) | ≈150 m · ≈8 km | — | 50,0–52,0 (540–518) | 1660–1840 | 180 × 22 | ✓ siluet aynı (yazın pusta solgun) |
| set | +4 | 85 | 47,2 (570) | 1533 → sağ kenar | — | G1 %20 · G2 %50 · G4+ %100 |
| taş istifi (sol ön) | 0 → +1,5 | 38 | 31,3–36,0 (742–692) | ≈286 | — | G0–G11 (azalır) |
| mobil vinç | taban 0 · bom +14 | 52 | 68,2 bom ucu (343) | ≈1157 | — | yalnız G6–G8 · S5'te girer · S8'de gider |
| üç kişi | 0 → +1,7 | 66 | 38,1 → 41,5 | ≈830 (G14) · ≈910 (G15) | ≈30 boy | yalnız G14–G15 |

```
KAMERA SABİTLİK  ilk/son kare kayması ≤ 2 px (1080p · KAMERA_ISTASYONU §7 · zincir_kontrol ESIK_KAYMA_ORAN) ·
                 üç nirengi: akasya tacının sol ucu · masa dağının sol omzu · kapı çerçevesinin sol üst köşesi
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
kervansaray 60 m cephe (x −30…+30 · D 67) · alt kat 0 → +5 · galeri +5 → +9 · 16 kemer (8 + 8, ≈2,6 m) · duvar tepesi +9 ·
kapı çerçevesi 12 m (x −6…+6) · +15 · sivri kemer 5 × 8 m (x −2,5…+2,5) · oyma geometrik kuşak · iki kanat (2,5 × 8 m) ·
kuleler Ø 6 m (x ±27…±33) · kubbe +13 · gedik x +12…+22 · +4 · 4 kemer · ön avlu 60 × 20 m (D 47–67) · kumul x −36…+36 ·
sırt +12 / +10 · topuk D 40 · set x +38…+62 · D 75–95 · +4 · akasya x −53,5…−46,5 · D 85 · kaya +3 · taç +9 · masa dağı
≈8 km · ≈150 m · mobil vinç (yalnız G6–G8) · 16 demir fener · iskele (G6–G11) · konveyör (G1–G11)
```

### Yapı yüzdesi ve saha durumu — sahne sahne (❹ İNŞA · ❺ TESLİM için)

| S | saat | yapı: eleman + ara hâl | kum | geçici ekipman kadrajda | saha / gök / mevsim |
|:-:|:-:|---|:-:|---|---|
| S00 | 06:00→06:10 | — · üç taş uç | sırt 425 | ekskavatör (sırtta) · damperli · kamyon (yeni taş) · kürekli ekip | kış · berrak |
| S01 | 06:10→08:10 | çerçeve + kubbeler kumdan çıkar | 425 → 483 | 2 ekskavatör · kamyon sırası · konveyör (kurulur) · istif | kış · set %20 |
| S02 | 08:10→10:10 | galeri soldan sağa · gedik belirir | 483 → 559 | 2 ekskavatör · kamyon · konveyör · istif | kış · set %50 |
| S03 | 10:10→12:10 | ⭐ cephe tam boy · gedik + yığın | 559 → zemin + rampa | 2 ekskavatör · kamyon · konveyör · istif | bahar · hafif pus |
| S04 | 12:10→12:20 | avlu döşemesi · kapı ağzı boşalır | rampa → 0 | 2 ekskavatör (gider) · kamyon (gider) · konveyör (katlanır) · çit demetleri | bahar · set %100 + çit |
| S05 | 12:20→12:30 | iskele · yığın → sıralar | — | iskele kamyonu (gider) · mobil vinç (girer) · istif | bahar |
| S06 | 12:30→14:30 | gedik duvarı +4 → üzengi · ayaklar | — | vinç (blok yükte) · iskele · blok sıraları (biter) · istif (azalır) | bahar |
| S07 | 14:30→14:40 | 4 kemer · duvar +9 · kalıplar sökülür | — | vinç (kemer taşı paleti) · iskele · ahşap kalıplar | bahar · yeni taş parlak |
| S08 | 14:40→14:50 | iki kapı kanadı · kapı kapalı | — | vinç (kanat yükte → gider) · iskele | bahar |
| S09 | 14:50→16:50 | (değişmez) · rüzgâr · süpürme | çitte birikir · avluda dil → süpürülür | iskele · konveyör (katlı) · el arabaları | ⭐ yaz · beyaz pus |
| S10 | 16:50→17:00 | 16 fener (sönük) · oyma kuşak temiz | — | merdivenler · fener sandıkları (el arabasında) · iskele | yaz |
| S11 | 17:00→17:10 | (değişmez) | — | iskele (sökülür) · konveyör (traktörle gider) · kamyon (gider) | yaz · yeni taş tozlu |
| S12 | 17:10→19:10 | (değişmez) · gün batımı | son ince kum süpürülür | el arabası + iki işçi | gün batımı → mavi saat |
| S13 | 19:10→19:20 | fenerler yanar (soldan sağa) | — | son merdiven + küçük araba (gider) | sonbahar · berrak |
| S14 | 19:20 +8 sn | kapılar açılır · TUTUŞ | — | YOK | derin mavi saat |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   kuru AKASYA — G0…G15 hepsinde x 154–259 · taç 495 · kaya üstü 585 · 105 px en; zincirde her karede ELLE ✓/✗
                (günlük §2) · hiç yaprak açmaz (mevsim taşımaz — çapa)
İKİNCİ ÇAPA     masa dağı x 1660–1840 (siluet; yazın pusta solgun, biçimi aynı) · üçüncü: ufuk 540 düz · dördüncü: kapı
                çerçevesinin tepesi 368 (G0'dan G15'e aynı yerde — kum sırtında uç, sonra çerçeve)
❸ İÇİN          dikiş = KARE (G1…G14): dikişin iki yakası aynı görsel; ❸ REBUILT hükmü zincir koşulmadı demektir
⚠️ KUMUL        çapa değildir (SAHA §3.6) — G0'dan G4'e değişmesi BEDELDİR, ❸ ve ❶ bunu "arka plan değişti" saymamalı
```

---

## 5. ❹ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ajanı · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | ajan (taşıyan) | geçici destek | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|---|:-:|:-:|:-:|
| kum (GİDEN) | kumul | 2 ekskavatör → damperli kamyonlar (sağdan) · konveyör → set | — | G0 | G5 (avlu açık) | ekskavatörler S4'te gider |
| set (GELEN, kalıcı) | konveyör | konveyör · çit ekibi | hurma dalı demetleri | G1 (%20) | G5 | konveyör S11'de gider |
| kapı çerçevesi · galeri · cephe (AÇILAN) | kumun içi | ekskavatör · kürekli ekip | — | G0 (uç) | G4 | — |
| yeni taş | düz kasalı kamyon → sol önde istif | ekip | ahşap takoz | G0 (kamyonda) | — | istif S11'de biter |
| iskele | iskele kamyonu (avlunun solu) | ekip | taban plakaları · duvara bağ | S5 içi | G6 | S11 (kamyona) |
| kurtarılmış bloklar | gediğin dibindeki yığın | mobil vinç · demir çubuklu ekip | sapan | G3 (yığın) | G6 (sıralar) | sıralar S6'da biter |
| gedik duvarı + ayaklar | sıralar + istif | vinç · masonlar | iskele · kireç harcı | G6 (+4) | G7 (üzengi) | — |
| 4 kemer | vinçte kemer taşı paleti | vinç · masonlar | ahşap kalıp | G7 | G8 | kalıplar S7'de sökülür |
| kapı kanatları × 2 | vinçte bir kanat · avluda takozlu ikinci | vinç · kılavuz ipli ekip | sapan · kılavuz ip | G8 | G9 | vinç S8'de gider |
| fener × 16 | el arabasında iki sandık | iki işçi · merdiven | merdiven | G10 | G11 | sandıklar S10'da gider |
| ışık | fener yakıcının alevi | fener yakıcı | uzun sırık | G13 (sönük) | G14 | — |
| kapı açılışı | (gizli) içeriden | (gizli) | demir pivotlar | G14 (kapalı) | G15 | — |

```
❹ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır):
   kervansaray 1 · kumul 1 (G0–G3) · sarı paletli ekskavatör 2 (G0–G4) · damperli kamyon (sıra) · düz kasalı kamyon 1 (G0) ·
   konveyör 1 (G1–G11) · iskele kamyonu 1 (G5) · mobil vinç 1 (G6–G8) · iskele 1 (G6–G11) · flatbed + küçük traktör (G11) ·
   el arabası / küçük araba · merdiven 2–3 · fener sandığı 2 · ekip (iz) · fener yakıcı (iz) · S14–G15 üç kişi + yük arabası ·
   akasya 1 · masa dağı 1 · set 1 + çitler
   ⛔ DAVETSİZ: ikinci yapı · harabe alanı / sütun ormanı · köy · çadır · palmiye · havuz / vaha · deve ya da herhangi bir
      hayvan · minare · burç / kale dişi · kule vinç · kazı ızgarası / ip ağı · yazı / işaret / tabela · ikinci kapı
❹ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: açılan cephe = S0–S3 ekskavatörler · set = S1 konveyör ·
                  örülü gedik = S5 iskele + vinç + S6 masonlar · kemerler = S7 kalıplar · kapı = S8 vinç · fener = S10 merdiven ·
                  ışık = S13 fener yakıcı · açık kapı = (gizli) içeriden, S14
❹ ÇERÇEVE DEFTERİ cephe x 387–1533 sabit (G3 → G15) · kuleler 329–444 / 1476–1591 · duvar tepesi 483 · zemin 655 · akasya 105 px sabit
❹ GİZLİ İŞ        avlunun ve odaların onarımı → S14'te açık kapıdan taşan ışık · menteşe → "iron pivots set in the threshold stone"
❹ DECLARED WORLD  çöl · kumul (G0–G3) · ekipli kazı · yıkık bölüm (G3–G6) · onarım · rüzgâr (S9) · 16 fener (G11+, yanık G14+) ·
                  üç kişi (G14–G15) · mavi saat (G13–G15) · kış görüntüsü YOK · hayvan YOK
❸ PARKED GEREKÇESİ S12 (gün batımı — yalnız iki işçi süpürür) · S14 (final tutuşu): şantiye bitti; bunlar ödül ve sakin anlardır
                  — işsiz aralık değil, beyanlı [P4-f · C1-d]
```

---

## 6. ❷ ZAMAN VE KESME — kesme listesi ve ses (❷ kör koşar; bu bölüm ❺ ve operatör içindir)

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_BURIED_KHAN/THE_BURIED_KHAN_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
                     ⚠️ prompt_kontrol.py süre satırlarını tek haneli sahne numarasıyla okur (S10–S14 okunmaz) —
                        bilinen araç hatası; kesme_kontrol.sh iki haneyi okur
REJİM KESMELERİ      8,0 (S0 A → S1 B) · 32,0 (S3 B → S4 A) · 48,0 (S5 A → S6 B) · 56,0 (S6 B → S7 A) · 72,0 (S8 A → S9 B) ·
                     80,0 (S9 B → S10 A) · 96,0 (S11 A → S12 B) · 104,0 (S12 B → S13 A) · 112,0 (S13 A → S14 G) — rejim
                     değişimi YALNIZ kesmede [P5-c]
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                ⛔ YOK (varsayım — hikâye SAPMA ⑫) · SES TABLOSU THE_BURIED_KHAN_MUZIK.md:
                     0–40 kum (kova, kürek, konveyör) · 40–72 taş (iskele, keski, harç, kapı) · 72–88 rüzgâr ·
                     96–104 akşamın nefesi · 104–120 fenerler, kapı gıcırtısı, içeriden boğuk ses — ani kesilme yok
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G8 (S7 ↔ S8) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si (S7) G8 karesinde biter; G8 BOLUM_2'nin ilk görselidir.
ELLE KARE            ffmpeg -ss 64.0 -i teslim.mp4 -frames:v 1 sinir.jpg → galeri 16/16 kesintisiz · gedik açık renkli taşla
                     örülü · kapı ağzı eşiğe kadar boş · bir kanat vinçte, biri avluda · iskele gedikte · gölge +64° · bahar
```

---

## 8. ❺ TESLİM — belgeli merceğin okuyacağı beyanlar

```
VAAT            Çölün yuttuğu bir kervansarayı kumdan çıkarıp onarmak ve kapılarını yeniden açmak.
DİRENÇ          ① kum — S0–S4 (0,0–40,0) ekskavatörler, kamyon sırası, sete kum döken konveyör · ② rüzgâr — S0–S2 sırttan
                tüten kum, S3 (24,0–32,0) kapıya geri kayan kum, S9 (72,0–80,0) çitlerde biriken kum ve süpürülen avlu ·
                ③ yıkık bölüm — S3 gedik ve yığın, S5–S7 (40,0–64,0) iskele, yeni taş, ahşap kalıp
BEDEL           kum tepesi — S0–S4 (0,0–40,0) kova kova gider; set olarak sağda kalır; G15'te yerinde açık kapılı kervansaray
AÇILIŞ          nesne: kum tepesi + üç taş uç · eylem: ekskavatör kovası ilk karede sırtı ısırıyor · ipucu: sol önde yeni taş
                yüklü kamyon · MERAK SORUSU: "Kumun altında ne var?"
İŞLEV ANI       S13 (104,0–112,0) fenerler kemer kemer yanar · S14 (112,0–116,0) kapılar gerçek hızda içe açılır, ışık taşar,
                üç kişi eşiğe gelir · 116,0–120,0 tutuş
LOOP RHYME      biçim ve konum: kapı çerçevesinin tepesi aynı yerde (845–1075 · 368) — G0'da kumdan çıkan uç, G15'te ışıklı
                kapının çerçevesi · akasya aynı x'te (154–259)
OMURGA (15)     üç uç · tepe sıyrılır · galeri · cephe · avlu · iskele · gedik · kemerler · kapı · rüzgâr · fener · söküm ·
                gün batımı · fenerler yanar · kapılar açılır
SES             MUSIC NO — diegetik ses tasarımı (❷ C2 · ❺ C1)
TESLİM          END CARD NO · SPEED 1x · 120,0 sn
AI BEYANI       YAYIN_PAKETI §AÇIKLAMA sabit beyan bloğu + Studio "Altered content = EVET"
KAPAK           THE_BURIED_KHAN_KAPAK.md — G15'ten, bölünmüş yerleşim YOK
PROMPT KAPISI   python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_BURIED_KHAN → BLOCK 0 · FIX 3 (09.10.2026) —
                hepsi PLAN §ÜRETİM ÖNCESİ DURUM'da beyanlı
```

---

## 9. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_BURIED_KHAN_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  00_ANALIZ/02 §3 — kamera · kumul · cephe · gedik · akasya · masa dağı · set
⛔ PİLOT ÜÇLÜ     ① G15 + G14 + S14 · ② G1 + G2 + S1 · ③ G9 + G10 + S9 — PLAN §PİLOT ÜÇLÜ
⛔ USTA KARE      G15 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil); akasya 105 ±2 px · cephe 387–1533 ±2 px
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a; 1920×1080 · 120,0 sn · kart YOK)
⛔ İHRAÇ          bash araclar/ihrac_kontrol.sh — süre 120,0 · kart YOK · müzik YOK · final tutuşu SSIM ≥ 0,90 [DERS 63]
⛔ KAPAK KANITI   ffmpeg -ss 119.5 -i teslim.mp4 -frames:v 1 g15_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g15_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
```
