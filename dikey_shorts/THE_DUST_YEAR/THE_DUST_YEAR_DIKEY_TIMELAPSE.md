# 🔴 THE DUST YEAR — DİKEY TIMELAPSE PLANI

```
PROJE          THE DUST YEAR
YAPI           Mars yüzeyinde robotik üs · insansız ön yerleşim
SAHA           düz toz ovası · 40°K (sığ yeraltı buzu bandı)
IZGARA         10 sahne · 60,0 sn sahne bloğu + 5,0 sn kapak kartı
YAY            667 sol ≈ 685 Dünya günü ≈ 1,00 Mars yılı (Ls 20 → Ls 19)
TARİH          08.09.2026 · kart A ile bu depoda yazıldı
DURUM          ⛔ ÜRETİLMEDİ — araç kapısı koşulmadı [ARAC_KARTLARI §4]
```

> ⛔ **BU PLAN ÜRETİME AÇIK DEĞİLDİR.** Kart A adım 7 (klip süresi ölçümü)
> koşulmadı: elde araç yok. §1'deki ARAÇ KUTU SETİ satırı ÖLÇÜLMEDEN
> tek kare üretilmez [DERS 23 · A7-a].

---

# 0. 🚪 KONSEPT KAPISI

```
VAAT     Bu ovada, insan gelmeden önce, bir basınçlı sığınak kurulacak:
         toprakla örtülmüş bir habitat, kendi gücünü üreten bir reaktör ve
         Dünya'yı gören bir direk.
DİRENÇ   TOZ. Mars'ın atmosferi Dünya'nınkinin %0,6'sı: toz kalkar ama
         yıkanmaz, biriktiği yerde kalır. Gezegen çapında bir toz fırtınası
         güneş panellerini öldürür. Ve aynı toz, elde bulunan TEK kalkan
         malzemesidir — düşman ile malzeme aynı şeydir.
         EKRANDA NASIL  S5→S6: fırtına bastırırken berm halkası yarıdan tama
         koşturulur; S6→S9: panellerdeki gri toz katmanı bir daha hiç incelmez.
BEDEL    Üssü kuran şey, üssü ilk kuran şeyi öldürür. İki güneş dizisi S1'de
         açılır, S2'de tam güç verir, S6'da gömülür ve S9'da hâlâ oradadır —
         açıldıkları yerde, bir yıllık tozun altında, ölü.
         Ve ova bir daha eski hâline dönmez: 17 metrelik ödünç çukuru ile bir
         yıllık tekerlek izleri kalıcıdır. Mars'ta iz silinmez.
```

```
① TEK KARE TESTİ       ✅ Tek karede berm yüksekliği kayanın yarığına göre,
                          direk bölüm sayısı sırt basamağına göre okunur.
② KİNETİK BAĞIMSIZLIK  ✅ Torba dizisi yükselir, çukur derinleşir, gölge
                          süpürür — metin gerekmez.
③ BAŞLIK ŞEMASI        ✅ "THE DUST YEAR" (3 kelime)
④ OMURGA CÜMLESİ       ✅ toprağı yarar → daireyi düzler → zemini camlaştırır →
                          silindiri şişirir → torbaları yığar → halkayı örer →
                          fırtına gömer → reaktörü indirir → paneli yayar →
                          direği diker
```

---

# 1. 📐 TESLİM YAPISI VE ARAÇ

```
SAHNE BLOĞU    10 sahne = 60,0 sn        ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn = 5,0 sn ← SAHNE DEĞİL · konusu DEĞİL
               ⛔ KONUM: teslimin SON 5 saniyesi [DERS 4 · A1-b]
─────────────────────────────────────────
TOPLAM                            65,0 sn

ARAÇ KUTU SETİ ⛔ ÖLÇÜLMEDİ — üretim günlüğü §0'da ffprobe ile doldurulacak
               Sahne tavanı = (en büyük kutu − 1,00 sn) [A7-b].
               ⚠️ Bu plandaki en uzun sahne 10,0 sn'dir. Ölçülen kutu seti
                  {4,6,8} çıkarsa tavan 7,00 sn olur ve S6 (10,0) ile S2/S9
                  (8,0) TEK KLİPTE ÜRETİLEMEZ; uzatma ya da iki klip dikişi
                  gerekir ve üretim günlüğüne yazılır. Kutu seti {5,10} ya da
                  {5,9} çıkarsa tavan 9,00 / 8,00 sn'dir ve yalnız S6 etkilenir.
ÜRETİM SÜRESİ  = TESLİM SÜRESİ + 1,00 sn (baş/son 10-15 kare kırpma) [A8]
```

```
⚠️ "HER SAHNE 6 SANİYE" İSTENDİ — IZGARA ÖYLE YAZILMADI, SEBEBİ ŞU:
   Düz ızgara bu depoda DÖRT KEZ ölçüldü ve dördünde de ⑥ METRONOM hükmü
   geldi [DERS 13 · 31]. prompt_kontrol.py eşit süreleri BLOCK eder.
   Toplam 60,0 sn ve 10 sahne KORUNDU — yalnız süreler ölçüye oturarak
   dağıtıldı (120 BPM · izinli 4·6·8·10 · toplam sabit).
```

---

# 2. 🔒 DEĞİŞMEZLER

```
┌─ KAMERA İSTASYONU (ana · tek istasyon, detay istasyonu YOK) ────────┐
│ lens          24 mm küresel · f/8 · ISO 100                          │
│ yükseklik     8,0 m — ova üstünde ölçüm direği ayağı                 │
│ mesafe        pad'in güney kenarından 27,5 m                         │
│ bakış açısı   348° (KKB) · tilt 0° · roll 0°                         │
│ ⛔ HESAPTAN ÇIKAR, SEÇİLMEZ [KAMERA_ISTASYONU §3]:                   │
│    D = (H − h) / 0,48 = (21,2 − 8,0) / 0,48 = 27,5 m                 │
│ ⭐ GÜNEŞ KAMERA ARKASINDA: bakış 348°, güneş 123-162° bandında —      │
│    disk hiçbir sahnede kadraja giremez [DERS 32].                     │
└──────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — üç, isimlendirilmiş, KALICI ──────────────────┐
│ ① sağda, pad kenarından 6,0 m doğuda, tepesi yarık 2,4 m'lik kaya    │
│ ② solda, 40 m çapında sığ krater; kenarı ovadan 1,8 m yüksek         │
│ ③ arkada ufukta, profilinde tek kare basamak olan alçak sırt         │
│ ⛔ Üçü de her karede aynı yerde, aynı boyutta, aynı şekilde.          │
│ ⭐ ⑤ "AYNI YER" NESNESİ: yarık tepeli kaya. 2,4 m = 112 piksel.       │
│    Her zincir_kontrol koşusunda ELLE doğrulanır [DERS 25].            │
└──────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE — hepsi hesaptan ──────────────────────────────────┐
│ ufuk çizgisi   %50,0 — tilt 0° geometrisinin sonucu                  │
│ zemin (pad)    %30,6   ·  berm tacı %37,9  ·  habitat tepesi %46,1   │
│ 3. direk flanşı %58,7  ·  5. flanş %74,2   ·  direk tacı %82,0       │
│ kadraj         23,2 m genişlik × 41,2 m yükseklik · 46,5 px/m        │
│ ⭐ OKUNABİLİRLİK EŞİĞİ 0,5 m = 23 px [INSAAT_YONTEMI §1]             │
│    Bundan küçük hiçbir nesne prompta yazılmadı.                       │
└──────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI taşır [DERS 19] ───────────────────┐
│ habitat        1 dikey silindir · Ø8,0 m · h 6,4 m                   │
│ berm           regolit torbası halkası · h 3,0 m · taban kalınlık 4,0 m│
│ çalışma pad'i  Ø30,0 m · sinterlenmiş koyu camsı kabuk               │
│ direk          6 bölüm × 3,2 m · taç 21,2 m · 2,0 m sinter ayak      │
│ gergi          3 tel · 12,0 m dışarıda ankraj                        │
│ çanak          Ø1,6 m · 5. bölümde                                   │
│ güç            1 fisyon ünitesi Ø2,2 m · habitatın 18,0 m doğusunda  │
│ radyatör       4 düz panel · her biri 2,4 × 4,0 m · tek sıra         │
│ güneş dizisi   2 dizi × 6 panel · habitatın 9,0 m batısında          │
│ ⭐ SAYI TESTİ: 6 bölüm · 4 panel · 3 tel · 2 dizi — hepsi SAYILABİLİR│
│ ⛔ GEÇİCİ EKİPMAN BU BLOKTA YOK [DERS 1]: kızak · sapan · iskele ·   │
│    torba ruloları · kablo makarası → SITE TEXTURE / ACTIVITY'de.      │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 3. 🪜 AŞAMA MERDİVENİ

| S | SÜRE | REJİM | AŞAMA | ELEMAN · ARA HÂL | EKRANDA VAR OLAN | YENİ OLAN | TEMSİL | MEVSİM TAŞIYICISI | KANIT NESNESİ | KİNETİK | İSTASYON |
|:-:|---:|:-:|---|---|---|---|---|---|---|---|---|
| 0 | 6,0 | B | İLK KESİK | pad %25 | çıplak ova | ilk ham kesik | başlangıç | krater gölgesinde sabah kırağısı | kesik kayanın 3,0 m berisinde biter | açar | ANA |
| 1 | 4,0 | B | DAİRE | pad %50 · dizi %50 | + ham kesik | 30 m daire + 3+3 panel | 50 sol | gölge 1 m çubukta 0,67 m | daire kenarı kayanın dibine ulaşır | düzler | ANA |
| 2 | 8,0 | B | CAM ZEMİN | pad %75 · çukur %25 | + düzlenmiş daire · diziler | camsı kabuk + ödünç çukuru | 55 sol | yılın en yüksek güneşi · gölge 0,46 m | camsı kabuk kayayı geçer — kaya artık cam üstünde | sinterler | ANA |
| 3 | 4,0 | A | SİLİNDİR | habitat %50 | + camsı pad · çukur | yarı şişmiş silindir | 65 sol | öğle gölgesi 0,35 m — yılın en kısası | yarım silindirin tepesi krater kenarı hizasında | şişer | ANA |
| 4 | 6,0 | B | İLK TORBALAR | habitat %75 · berm %25 | + silindir | gergin habitat + ilk torba sırası | 75 sol | ufukta ilk toz pusu | habitat tepesi krater kenarından 4,0 m yukarıda | yığar | ANA |
| 5 | 4,0 | B | YARIM HALKA | berm %50 · çukur %50 | + gergin habitat · ilk torbalar | 1,6 m berm | 65 sol | gökyüzü koyulaşıyor · toz mevsimi | berm tacı kayanın YARIĞINA ulaşır | örer | ANA |
| 6 | 10,0 | C | TOZ YILI | berm %75 · dizi gömülür | + yarım halka | 3,0 m kapalı halka | 70 sol | ⭐ gezegen çapında toz fırtınası · güneş kenarsız disk | berm tacı kaya tepesini 0,6 m aşar | gömer | ANA |
| 7 | 4,0 | B | TOZUN BIRAKTIĞI | reaktör %50 | + tam berm · gömülü diziler | fisyon ünitesi footingde | 60 sol | her yüzeyde YENİ ve kalıcı toz katmanı | sapanın sildiği temiz şerit sahadaki tek tozsuz yüzey | indirir | ANA |
| 8 | 6,0 | B | DÖRT PANEL, ÜÇ BÖLÜM | radyatör %75 · direk %50 | + reaktör | 4 radyatör + 3 bölüm | 60 sol | yılın en uzun gölgeleri · 1 m → 2,63 m | 3. direk flanşı sırt basamağını aşar | yayar | ANA |
| 9 | 8,0 | B | TOZ YILI KAPANIR | direk %75 · çanak %75 | + radyatörler · yarım direk | 6 bölüm + çanak + gergin teller | 160 sol | bir yıllık toz · panellerde gri örtü | direk tacı sırt basamağının dört kaya boyu üstünde | dikilir | ANA |

```
TOPLAM 60,0 sn · benzersiz süreler 4 · 6 · 8 · 10
KISA (4,0) dört sahne · UZUN (8,0) iki sahne · DORUK S6 = 10,0 sn
⭐ DORUK KONTRASTI: S5 = 4,0 → S6 = 10,0. En büyük değer dorukta [P2-f].
⭐ 120 BPM · ölçü 2,0 sn — dört sürenin dördü de ölçüye oturuyor.
⛔ Süre sütunu planda kalmaz: yayından önce kesme_kontrol.sh koşar [DERS 31].

KİNETİK İMZA  açar · düzler · sinterler · şişer · yığar · örer · gömer ·
              indirir · yayar · dikilir
              ✅ Ardışık iki satırda aynı fiil yok; onu da farklı [P1-f].

İLK 20 SANİYE (S0+S1+S2 = 18,0 sn) — üçü de FARKLI TÜRDEN değişim [P1-a]:
              S0 toprak YARILIR · S1 zemin ŞEKİLLENİR · S2 yüzey MADDE DEĞİŞTİRİR
              Test: S3'ün son karesi ile S0'ın ilk karesi yan yana → çıplak ova
              karşısında camsı pad üstünde basınçlı silindir. Yapının TÜRÜ okunur ✅
```

### Üç zorunlu satır

```
① KANIT NESNESİ   Her satırda yukarıda. ⑤ AYNI YER nesnesi: yarık tepeli kaya.
   ⛔ Her zincir_kontrol koşusunda iki karede de aynı yerde olduğu ELLE
      doğrulanır; değilse kare ATILIR — betik geçse bile [DERS 25].

② LOOP SATIRI     S9'un son karesi ile S0'ın ilk karesi AYNI kadrajdır.
   ⭐ IŞIK DA EŞLENDİ: S0 azimut 124° / yükselti 45°, S9 azimut 125° / 44°.
      Fark 1°. Bir Mars yılı sonra aynı mevsim, aynı sol saati [Ls 20 → Ls 19].
   Çıplak ova → tamamlanmış üs, aynı çerçeve, aynı ışık.

③ SÖKÜM SATIRI    geçici ekipman ne zaman kurulur, ne zaman sökülür:
   habitat kızağı   S3 kurulur → S4 SÖKÜLÜR ve pad'e düz istiflenir
   kaldırma sapanı  S7 takılır → S8 SÖKÜLÜR
   direk iskelesi   S8 kurulur → S9 SÖKÜLÜR
   ödünç çukuru     S2 açılır → S6'da 17,0 m'de DURUR → S9'da hâlâ orada
                    ⭐ sökülmez: BEDEL'in ekrandaki hâli
   güneş dizileri   S1 açılır → S6 gömülür → S9'da hâlâ orada, ölü
                    ⭐ sökülmez: BEDEL'in ikinci hâli
   ⛔ Hiçbiri kendiliğinden kaybolmaz; her biri I2V'de bir FİİL alır [P2-h].
```

---

# 4. ☀️ GÜNEŞ SAATİ — Mars 40°K · hesaplanmış

```
Mars sol = 24 sa 39 dk 35 sn · saat açısı 14,599°/sa (Dünya 15,000)
eksen eğikliği 25,19° · yıl 668,6 sol · dış merkezlik 0,0934
⛔ DÜNYA SAYISI KULLANILMADI. Gölge süpürmesi ve öğle yükseltileri bu
   parametrelerden hesaplandı; rejim tablosu buradan doğdu [A6-b].
```

| S | Ls | mevsim (kuzey) | öğle yükseltisi | sol saati | AZİMUT | YÜKSELTİ | 1 m gölge | rejim penceresinde gölge süpürmesi |
|:-:|---:|---|---:|---:|---:|---:|---:|---|
| 0 | 20 | northern spring | 58,4° | öğle−2,5 | 124° | 45° | 1.0 m | ~30° |
| 1 | 45 | late northern spring | 67,5° | öğle−2,0 | 123° | 56° | 0.67 m | ~40° |
| 2 | 70 | early northern summer | 73,6° | öğle−1,5 | 125° | 65° | 0.46 m | ~50° |
| 3 | 100 | midsummer in the northern hemisphere | 74,8° | öğle−1,0 | 137° | 70° | 0.35 m | ~5° (10 dk) |
| 4 | 135 | late northern summer | 67,5° | öğle−1,5 | 134° | 61° | 0.56 m | ~45° |
| 5 | 170 | northern autumn equinox | 54,2° | öğle−2,0 | 136° | 46° | 0.98 m | ~35° |
| 6 | 210 | northern autumn, global dust storm season | 37,7° | öğle−1,0 | 162° | 36° | 1.38 m | ~130° (9 sa) |
| 7 | 250 | early northern winter | 26,4° | öğle−1,5 | 158° | 23° | 2.33 m | ~30° |
| 8 | 290 | deep northern winter | 26,4° | öğle−2,0 | 151° | 21° | 2.63 m | ~25° |
| 9 | 19 | northern spring again, one Martian year on | 47,9° | öğle−2,5 | 125° | 44° | 1.04 m | ~30° |

```
⭐ Güneş TEK YÖNDE ilerler ve mevsim TEK YÖNDE döner: Ls 20 → 355 → 19.
⭐ Azimut bandı 123°-162°; kamera bakışı 348°. Güneş her sahnede kameranın
   ARKASINDADIR ve disk hiçbir promptta anılmaz [DERS 32].
⛔ S6'da gölge YOK — toz fırtınası ışığı düzleştirir. O sahnede zamanın
   taşıyıcısı gölge değil, BİRİKEN TOZDUR. Fizik bunu gerektirir.
```

---

# 5. 🎬 SAHNE PROMPTLARI

> ⛔ Her prompt kendi başına çalışır: köşeli parantez atfı yoktur [D-a].
> ⛔ YAPI BIBLE ve SITE / BACKGROUND blokları on promptta BİREBİR aynıdır.
> ⭐ İnsansız film: her promptta "No people are present." — koşullu cümle YOK
>   [DERS 33]. TIME RATE özne listesi SAHADAN yazıldı: gölge · toz · robotik
>   araç · mafsallı makine [P1-e].

## 🎬 SAHNE 0 — İLK KESİK

`6,0 sn` · `rejim B — REJİM B · yaklaşık 2 saat · 1200×` · `Ls 20` · `kinetik: açar`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 0 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: nothing of the base exists. The plain is bare dust. One line of cleated rover tracks crosses in from the right edge and ends in the middle of the frame, where a blade has opened one shallow raw cut 12 metres long and 0.4 metres deep, turning up darker material from beneath the surface dust. Beyond the cut the plain runs unbroken and unmarked to the horizon in every direction.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The raw cut ends 3.0 metres short of the split-top boulder, and its spoil ridge lies on the boulder side.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 124 degrees, elevation 45 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 1.0 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A pale butterscotch tan sky that whitens toward the horizon. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about thirty degrees across the plain.

ACTIVITY: A tracked dozer rover pushes dust along the cut while a second small rover drives across behind it, both smeared into a slow blur, and the cleated ruts they leave stay pressed into the dust after they pass. No people are present.

SITE TEXTURE: loose fine dust, cleated ruts, one low spoil ridge of pushed material, scattered small stones and a shallow drift of dust piled against the boulder's uphill side.

PHYSICS: The dozer rover rests its full weight on its tracks on firm ground. The spoil ridge lies at its natural angle of repose. Thrown dust rises low and falls back quickly in the thin air.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

A blade pushes forward along the cut and the raw cut lengthens metre by metre. A second rover drives in from the right, turns short of the boulder and drives out again, and each pass lays another cleated rut beside the last. Loose dust thrown off the blade rises low and drops back quickly. The spoil ridge beside the cut grows and slumps and grows again, and the shot ends with the cut running its full 12 metres and its spoil ridge unbroken along the boulder side.

The sun stays behind the camera at azimuth 124 degrees and elevation 45 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about thirty degrees across the plain.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 1 — DAİRE

`4,0 sn` · `rejim B — REJİM B · yaklaşık 2 saat · 1200×` · `Ls 45` · `kinetik: düzler`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 1 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: the work pad has been graded into a bare circle 30.0 metres across, its surface still loose dust, and a continuous spoil ridge of pushed material rings it. The two solar arrays stand half unfolded to the west with three of their six panels open on each. Inside the graded circle the dust lies bare and level, with nothing standing on it.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The graded circle edge has reached the base of the split-top boulder and stopped there.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 123 degrees, elevation 56 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 0.67 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A pale butterscotch tan sky that whitens toward the horizon. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about forty degrees across the plain.

ACTIVITY: A grader rover drives a slow arc around the pad edge while a loader rover crosses the circle and tips a load onto the spoil ridge, both drawn into a blur, and fresh cleated ruts cut across the dust inside the circle. No people are present.

SITE TEXTURE: loose fine dust, deep cleated ruts across the graded circle, a continuous spoil ridge, stacked flat panel crates west of the pad and untidy clutter around them.

PHYSICS: The solar array frames stand on staked feet in contact with the ground. The spoil ridge holds its angle of repose. Nothing is suspended.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

A grader rover drives a slow arc around the pad edge, doubles back and drives it again, and the bare circle widens outward with every pass. A loader rover crosses the circle, tips a load onto the spoil ridge and drives back for another, and the ridge closes further around the pad. West of the pad the solar array panels swing open one after another, and the shot ends with the graded circle closed at 30 metres and three panels open on each array.

The sun stays behind the camera at azimuth 123 degrees and elevation 56 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about forty degrees across the plain.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 2 — CAM ZEMİN

`8,0 sn` · `rejim B — REJİM B · yaklaşık 2 saat · 1200×` · `Ls 70` · `kinetik: sinterler`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 2 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: two thirds of the 30.0 metre pad has been sintered into a dark glassy crust and its leading edge still glows dull orange, while the remaining third is loose dust. The two solar arrays are fully unfolded with six panels each. A borrow pit has been opened 8.0 metres across and 1.2 metres deep off the pad's west side, its wall cut in one clean step. The rest of the fused crust lies bare and empty from edge to edge.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The sintered crust edge has passed the split-top boulder and the boulder now stands on dark glass instead of dust.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 125 degrees, elevation 65 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 0.46 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A bright butterscotch tan sky, the lightest it will be all year. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about fifty degrees across the plain.

ACTIVITY: A sintering rover crawls along the crust edge leaving a glowing line behind it while a loader rover drives out of the borrow pit and crosses the frame, both drawn into a blur, and the ruts they cut in the loose third of the pad stay visible. No people are present.

SITE TEXTURE: dark glassy crust on two thirds of the pad, loose dust on the rest, cleated ruts along the boundary between them, a stepped spoil heap beside the borrow pit and stacked bag rolls.

PHYSICS: The sintering rover sits on the crust it has already made. The pit wall stands at a stable step. Nothing is suspended above the ground.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

A sintering rover crawls forward along the crust edge and the ground behind it turns from pale dust to dark glass, glowing dull orange at the line and cooling to black behind. A loader rover drives up out of the borrow pit, crosses the loose third of the pad and drives back down, deepening the pit step by step. The remaining panels of both arrays swing open, and the shot ends with two thirds of the pad fused and both arrays fully unfolded at six panels each.

The sun stays behind the camera at azimuth 125 degrees and elevation 65 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about fifty degrees across the plain.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 3 — SİLİNDİR

`4,0 sn` · `rejim A — REJİM A · yaklaşık 10 dakika · 100×` · `Ls 100` · `kinetik: şişer`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 3 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: the habitat is half inflated: the white fabric cylinder has risen to about half its 6.4 metre height and its surface carries deep loose wrinkles that run the whole way around it, and it still sits inside its open metal cradle on the fused pad. The pad is fully sintered. The borrow pit is 8.0 metres across. Around the cylinder the crust lies bare and the ground east of it is smooth.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The top of the half inflated cylinder sits level with the crater rim line behind it.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 137 degrees, elevation 70 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 0.35 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A bright butterscotch tan sky. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About ten minutes pass across this shot: the shadow of the split-top boulder barely moves and the machines stay recognisable as machines.

ACTIVITY: A rover holds at the cradle while a robotic manipulator arm moves slowly along the cylinder skirt, both moving slowly enough to stay recognisable as machines, and the dust they lift settles back onto the fused crust behind them. No people are present.

SITE TEXTURE: dark glassy crust, a thin film of settled dust on it, cleated ruts leading in from the west, folded fabric offcuts and an open cradle frame beside the cylinder.

PHYSICS: The cylinder is held down by its cradle at the base while internal pressure lifts it. The fabric hangs slack where it is not yet pressurised.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

Gas fills the fabric and the cylinder rises slowly out of its cradle. The deep loose wrinkles in the fabric shift and travel around the drum as it lifts, never quite smoothing out. A manipulator arm moves along the skirt and checks it round, and a rover holds its position at the cradle. Dust lifted from the crust settles back within seconds, and the shot ends with the cylinder standing at about half its height with its wrinkles still deep and loose.

The sun stays behind the camera at azimuth 137 degrees and elevation 70 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About ten minutes pass across this shot: the shadow of the split-top boulder barely moves and the machines stay recognisable as machines.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 4 — İLK TORBALAR

`6,0 sn` · `rejim B — REJİM B · yaklaşık 2 saat · 1200×` · `Ls 135` · `kinetik: yığar`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 4 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: the habitat stands at its full 6.4 metre height with its white fabric drum tight and smooth, and its cradle has been stripped away and stacked flat on the pad. Around the foot of the habitat the first course of regolith bags is laid, reaching 0.8 metres up the wall on the south side only. The borrow pit is 11.0 metres across. At the centre of the pad a plain sintered disc 2.0 metres across lies flush with the crust.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The habitat top now stands 4.0 metres clear above the crater rim line behind it.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 134 degrees, elevation 61 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 0.56 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A butterscotch tan sky with a faint dust haze low over the ridge. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about forty-five degrees across the plain.

ACTIVITY: A loader rover hauls filled bags up from the borrow pit while a manipulator arm places them along the south wall, both drawn into a blur, and a widening fan of cleated ruts runs between the pit and the habitat. No people are present.

SITE TEXTURE: dark glassy crust dusted over, deep cleated ruts between pit and habitat, a stepped spoil heap at the pit mouth, the stripped cradle stacked flat and loose bag rolls.

PHYSICS: Each bag course rests on the course below it. The habitat fabric is taut under internal pressure. The loader carries its load low and in contact with its bed.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

A loader rover hauls filled bags up out of the borrow pit, drives to the south wall and sets them down, and a manipulator arm places each bag against the habitat foot. The first course closes along the south side and the second begins on top of it. The fabric above them stands drum tight and does not move. The rut fan between pit and habitat widens with every trip, and the shot ends with the bag course reaching 0.8 metres up the south wall only.

The sun stays behind the camera at azimuth 134 degrees and elevation 61 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about forty-five degrees across the plain.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 5 — YARIM HALKA

`4,0 sn` · `rejim B — REJİM B · yaklaşık 2 saat · 1200×` · `Ls 170` · `kinetik: örer`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 5 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: the regolith berm has reached 1.6 metres, half its final 3.0 metre height, and closes three quarters of the way around the habitat, while on the open quarter the bags lie in an unstacked heap. The borrow pit has grown to 14.0 metres across and 2.0 metres deep and is cut in two clear steps. At the centre of the pad a plain sintered disc 2.0 metres across lies flush with the crust.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The berm crown has reached the split in the top of the boulder.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 136 degrees, elevation 46 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 0.98 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A butterscotch tan sky darkening slightly as dust season begins. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about thirty-five degrees across the plain.

ACTIVITY: A loader rover drives up out of the deepening pit while a manipulator arm rolls a bag into place on the open quarter, both drawn into a blur, and the ruts between pit and berm have worn into a smooth polished track. No people are present.

SITE TEXTURE: polished rut track between pit and berm, a two step spoil heap, loose bags in an untidy heap on the open quarter and a thin dust film over the glassy crust.

PHYSICS: The berm holds a stable outward slope. The unstacked bags lie where they fell. The pit steps stand without support.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

A loader rover drives up out of the deepening pit, carries bags round the east side and drives back down, and the pit cuts a second step into its own floor. A manipulator arm rolls each bag into place and the berm closes further around the habitat, course by course. The unstacked heap on the open quarter shrinks as it is used, and the shot ends with the berm at 1.6 metres and closed three quarters of the way around.

The sun stays behind the camera at azimuth 136 degrees and elevation 46 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about thirty-five degrees across the plain.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 6 — TOZ YILI

`10,0 sn` · `rejim C — REJİM C · bir iş günü · 5400×` · `Ls 210` · `kinetik: gömer`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 6 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: a planet wide dust haze has closed over the site and the light is flat and almost shadowless. The regolith bags have been driven to the full 3.0 metre berm height all the way around the habitat, and the outer face is still rough where the bags were laid in a hurry. The six panels of each solar array are buried under an even grey dust layer. The borrow pit is 17.0 metres across. At the centre of the pad a plain sintered disc 2.0 metres across lies flush with the crust.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The finished berm crown stands 0.6 metres above the top of the split-top boulder.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 162 degrees, elevation 36 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 1.38 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A dark ochre sky flattened by a planet wide dust haze, the sun a dim disc with no edge. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. A full working day passes across this shot: the light stays flat and almost shadowless in the dust, the dust layer on the solar panels visibly deepens, and no vehicle stays in one place long enough to be seen — only the marks it leaves.

ACTIVITY: No machine holds still long enough to be seen in the haze: a dozer rover crosses the frame twice as a faint moving smudge and a loader rover drives up out of the pit, both drawn into a blur, while the ruts they cut fill with settling dust behind them and the dust layer on the solar panels visibly deepens. No people are present.

SITE TEXTURE: an even grey dust layer over every horizontal surface, half filled ruts, a rough outer berm face with bag ends showing, a drift of dust banked against the west side of the habitat and dust filling the borrow pit steps.

PHYSICS: The berm holds its own weight in a closed ring. Suspended dust dims the sun without moving the shadows. Nothing is suspended above the ground.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

The light flattens as dust thickens overhead and the shadows fade until the ground carries almost none. A dozer rover crosses the frame as a faint moving smudge and is gone; a loader rover drives up out of the pit and is swallowed by the haze. Bags go onto the berm faster than before and the ring closes and rises. Dust settles evenly onto every horizontal surface, the ruts fill in behind each pass, the solar panels grey over, and the shot ends with the berm at its full 3.0 metres all the way round and every panel buried under dust.

The sun stays behind the camera at azimuth 162 degrees and elevation 36 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. A full working day passes across this shot: the light stays flat and almost shadowless in the dust, the dust layer on the solar panels visibly deepens, and no vehicle stays in one place long enough to be seen — only the marks it leaves.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 7 — TOZUN BIRAKTIĞI

`4,0 sn` · `rejim B — REJİM B · yaklaşık 2 saat · 1200×` · `Ls 250` · `kinetik: indirir`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 7 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: the haze has cleared and every surface carries a new even dust layer: the habitat fabric has gone from white to pale tan and the six panels of each solar array stay grey and dead. The fission power unit has been set on its footing 18.0 metres east of the habitat and is still held in its lifting sling, and none of its four radiator panels is standing yet. At the centre of the pad the sintered disc lies flush with the crust under the new dust.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The clean line where the sling has wiped the dust off the power unit casing is the only unweathered surface left on the site.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 158 degrees, elevation 23 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 2.33 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A clearing butterscotch tan sky with long low light. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about thirty degrees across the plain.

ACTIVITY: A loader rover drives away from the power unit footing while a manipulator arm swings the first radiator panel up off its pallet, both drawn into a blur, and one clean set of fresh ruts cuts through the new dust layer between the pad and the footing. No people are present.

SITE TEXTURE: an even pale dust layer over the crust, one set of fresh dark ruts cut through it, stacked radiator pallets, coiled cable spools and the sling hanging loose on the power unit.

PHYSICS: The power unit rests on its footing and the sling above it is taut. The radiator panel hangs vertically from the manipulator arm and stays in contact with it.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

The haze thins and the low sun returns, and long shadows come back across the site. A loader rover drives away from the power unit footing and a manipulator arm swings the first radiator panel up off its pallet and holds it vertical. The fresh ruts they cut show dark through the new dust layer. The sling above the power unit stays taut and the dust wiped from its casing stays clean, and the shot ends with the power unit set on its footing and still slung.

The sun stays behind the camera at azimuth 158 degrees and elevation 23 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about thirty degrees across the plain.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 8 — DÖRT PANEL, ÜÇ BÖLÜM

`6,0 sn` · `rejim B — REJİM B · yaklaşık 2 saat · 1200×` · `Ls 290` · `kinetik: yayar`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 8 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: all four radiator panels stand in one row beside the fission power unit and the lifting sling has been taken off it. The communications mast is half built: three of its six sections are bolted together and stand 11.6 metres above the pad inside a temporary lattice scaffold, and the three guy wires lie coiled and slack on the ground around it.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The third mast flange now stands clear above the stepped ridge on the horizon.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 151 degrees, elevation 21 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 2.63 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A low butterscotch tan sky with the longest shadows of the year. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about twenty-five degrees across the plain.

ACTIVITY: A manipulator arm lifts the fourth mast section up the scaffold while a loader rover crosses to the anchor points with a guy wire spool, both drawn into a blur, and long winter shadows of the radiator panels sweep across the dusted crust. No people are present.

SITE TEXTURE: an even dust layer with fresh ruts cut through it, coiled guy wires on the ground, empty cable spools, offcut lattice sections stacked flat and a scaffold frame around the mast.

PHYSICS: The mast section hangs vertically from the manipulator arm and its lower flange is already seated. The scaffold carries the mast sideways only. The guy wires lie slack on the ground.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

A manipulator arm lifts one mast section up the scaffold, seats it on the flange below and returns for the next. A loader rover crosses to each anchor point carrying a guy wire spool and drives back. The four radiator panels stand still in their row while their long winter shadows sweep across the dusted crust. The coiled guy wires stay slack on the ground, and the shot ends with three sections standing at 11.6 metres inside the scaffold.

The sun stays behind the camera at azimuth 151 degrees and elevation 21 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about twenty-five degrees across the plain.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 9 — TOZ YILI KAPANIR

`8,0 sn` · `rejim B — REJİM B · yaklaşık 2 saat · 1200×` · `Ls 19` · `kinetik: dikilir`

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 9 of 10. Vertical time-lapse of a robotic surface base on a dust plain on Mars.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a survey mast footing on the plain, lens 8.0 metres above the pad surface, 27.5 metres from the south edge of the pad, bearing 348 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One robotic surface base on a flat dust plain. Complete, it is: one vertical inflatable habitat cylinder 8.0 metres across and 6.4 metres tall; one ring of regolith bags around it, 3.0 metres high and 4.0 metres thick at the base; one circular work pad 30.0 metres across, fused to a dark glassy crust; one lattice mast of six bolted sections, each 3.2 metres long, its head 21.2 metres above the pad on a 2.0 metre sintered footing, held by three guy wires anchored 12.0 metres out; one 1.6 metre dish on the fifth mast section; one fission power unit 2.2 metres across set 18.0 metres east of the habitat, with four radiator panels each 2.4 by 4.0 metres in one row beside it; and two solar arrays of six panels each, 9.0 metres west of the habitat. AT THIS STAGE: the base is complete. The mast stands with all six sections bolted and its head 21.2 metres above the pad, the temporary scaffold is gone, the three guy wires run dead straight and taut to their anchors, and the 1.6 metre dish is bolted to the fifth section. The habitat sits inside its closed 3.0 metre berm, the four radiator panels stand in their row, and the two solar arrays still stand to the west with six panels each, grey under a full year of dust.

SITE / BACKGROUND: The base sits on a flat dust plain that runs unbroken to the horizon. To frame right, 6.0 metres east of the pad edge, stands one boulder 2.4 metres tall with a split top, its two halves leaning apart. To frame left lies a shallow crater 40 metres across whose rim rises 1.8 metres above the plain, its inner north face permanently in shadow. Far behind the site the horizon carries a low ridge with one square step in its profile, one third of the way in from the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The mast head stands four boulder heights above the stepped ridge on the horizon, and the dead solar arrays stand exactly where they were unfolded.

COMPOSITION: Vertical 9:16. The pad surface sits at thirty-one percent of frame height and the mast head at eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: sun azimuth 125 degrees, elevation 44 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 1.04 metre shadow. The sun stays behind the camera for the whole shot; its only sign is the shadows. A pale butterscotch tan sky that whitens toward the horizon. It looks like a surface photograph from a hard-mounted engineering camera: flat tan light, fine even grain, no lens flare, no depth haze beyond the ridge, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about thirty degrees across the plain.

ACTIVITY: A dozer rover crosses the pad once and drives out of the right edge of the frame while the dish rotates slowly on its mount, both drawn into a blur, and the year of ruts across the crust has worn into one wide polished track. No people are present.

SITE TEXTURE: a full year of dust over the crust, one wide polished rut track, the abandoned borrow pit 17.0 metres across with dust filling its steps, stacked offcut bags and empty spools.

PHYSICS: The guy wires are straight under tension. The dish is bolted to the mast and turns on its own mount. Everything rests on the ground or on what carries it.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same base, same background in every frame: the horizon line, the split-top boulder, the crater rim and the stepped ridge never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; the habitat diameter, the pad diameter, the mast section length and the panel count stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the machinery, the rover, the module, the habitat, the panel, the mast, the radiator, the antenna, the dish, the spool, the cradle, the manipulator or the scaffolding. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no bag course without support beneath it, no machine hovering above the ground. Everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation. No subtitles, no captions, no title card, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No blue sky, no liquid water, no green plant, no bird, no aircraft, no daytime stars. This is a working robotic site: loose dust, cleated ruts, spoil ridges, stacked bags and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image.

The dish turns slowly on its mount and its shadow swings across the berm below. A dozer rover crosses the pad once and drives out of the right edge of the frame. The guy wires stay dead straight and do not move. Dust lifts off the crust in one low gust and settles again on the grey solar panels, and the shot ends with the whole base standing quiet: mast up, dish mounted, berm closed, arrays dead and dusted, and the plain around it marked with one year of ruts.

The sun stays behind the camera at azimuth 125 degrees and elevation 44 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the blowing dust, the robotic vehicles and the articulated machines all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the split-top boulder sweeps about thirty degrees across the plain.

The camera does not move at any point. The framing is identical in the first and last frame. The split-top boulder occupies exactly the same width of the frame at both ends of the shot, the crater rim keeps its shape and position, the stepped ridge on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No bag course appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 6. 🎵 MÜZİK VE KAPAK

```
BPM            120 · ölçü 2,0 sn · sahne süreleri (4·6·8·10) ölçüye oturur
MÜZİKSİZ       0,0 - 1,5 sn açılışta ses yok; ilk vuruş S0'ın ilk kesiğiyle
YATAK          diegetik değil: Mars'ta ses taşıyan atmosfer yok denecek kadar
               ince. Yatak, alçak bir uğultu ve toz fırtınasında bir basınç
               kabarması olarak kurulur — kaynak sesi TAKLİT EDİLMEZ.
KATMAN         katman sayısı berm sırasıyla artar: S4'te 1, S6'da 4, S9'da 2
               (fırtına geçtikten sonra katman ÇEKİLİR — bedelin sesi)
─────────────────────────────────────────────────────────────────
KAPAK          ⛔ S9'un usta karesinden türer [DERS 30]
BAŞLIK         "THE DUST YEAR" — İngilizce, 3 kelime
KAPAK KANITI   zincir_kontrol.sh s9_kaynak.jpg kapak.png → çıkış ≠ 2
               ⭐ s9_kaynak.jpg TESLİM dosyasından alınır, üretilen klipten
                 DEĞİL — kırpma kareleri kaydırır [KURGU_VE_TESLIM §2]
120 PX TESTİ   hem kapağa hem S0'ın 0. karesine (sips -Z 120)
```

---

## 7. 📦 PAKETLEME

```
BAŞLIK          One Martian Year, One Shelter
AÇIKLAMA        A robotic base builds itself on Mars across one Martian year.
                Fixed camera, no cuts inside a shot, no people on site.
                The solar arrays that powered the first half of the build are
                still standing at the end, dead under a year of dust.
HASHTAG         #mars #timelapse #construction #isru #robotics
SABİT YORUM     Everything in this film is generated. The base, the site and
                the machines do not exist.
⛔ GERÇEKLİK BEYANI + üç platformda AI beyanı elle [kart Y adım 5-6]
```

---

## 8. ⛔ ÜRETİMDEN ÖNCE KAPANMASI GEREKENLER

```
□ ARAÇ KAPISI       7 ölçüm · 5 klip · tek prompt [ARAC_KARTLARI §4-§5]
                    → kutu seti · sahne tavanı · kamera kayması · gölge dönüşü
                      · negatif sızması · prompt tavanı · ilk kare sadakati
□ KUTU SETİ         §1'deki satır doldurulur; S6 (10,0 sn) tavanı aşarsa
                    uzatma/dikiş kararı üretim günlüğüne yazılır
□ ÜRETİM GÜNLÜĞÜ    dikey_shorts/THE_DUST_YEAR/THE_DUST_YEAR_URETIM_GUNLUGU.md
□ PROMPT KAPISI     python3 araclar/prompt_kontrol.py <bu dosya>
□ ÜRETİM SIRASI     ⛔ TERS: S9 usta kare → geriye zincir → her kareden sonra
                    zincir_kontrol.sh + kaya ELLE doğrulanır
```
