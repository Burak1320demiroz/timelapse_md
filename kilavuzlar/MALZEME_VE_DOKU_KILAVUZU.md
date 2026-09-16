# 🧱 MALZEME VE DOKU KILAVUZU — yüzeyin fotoğraf olduğunu göstermek

> **Tek soru:** Yüzey fotoğraf mı, render mı?
> **Sahibi olduğu blok:** `SITE TEXTURE` (görsel prompt) — bu kılavuz olmadan
> o blok her filmde aynı tek cümleydi ve Ay yüzeyinde bile "puddles" yazıyordu.
>
> ⛔ **Kaynak:** `arastirma/SONUCLAR/A9_GEMINI_HAM.md` · denetim `A9-A12_DENETIM.md`
> · dersler `DERSLER.md` A9-a…g · DERS 34 · DERS 42 · A4-a · A5-c.
> Aşağıda **ÖLÇTÜM** yazan sayılar bu depoda hesaplandı; **VARSAYIM** yazanlar
> rapordan devralındı ve ilk üretimden sonra ya derse döner ya düşer.
>
> **Sınır:** SANTIYE_HAREKETI §3 "sekiz yüzey kanıtı" = İŞİN yüzeyde bıraktığı iz.
> ZAMAN_VE_ISIK §6 = malzemenin ZAMAN TAŞIYICISI olarak kuralı.
> INSAAT_YONTEMI §4.4 = yapı ADININ korpusu. Burası = yüzeyin KENDİ doğruluğu:
> hangi malzeme gerçek fotoğrafta nasıl görünür, kirlilik nerede, yaşlanma nasıl.

---

# 0. NEDEN BU KILAVUZ VAR — ölçülmüş arıza

```
① SURFACE TRUTH   0/10 iki filmde · 3/10 POLAR HABITAT
   "the entire site is a CGI rendering displaying miniature appearance,
    artificial architectural visualization lighting, and completely clean,
    uniform textures rather than a photographic working site"
Promptlarda "photorealistic documentary construction photograph" YAZIYORDU.
Kelime vardı; kelimenin bağlandığı YÜZEY BİLGİSİ yoktu.

⭐ Raporun teşhisi (A9 "çelişenler"): "photorealistic" bir stil etiketi değil,
   bir MALZEME LİSTESİDİR. Model beton için "beton" bilmez; "koyu ıslak gri,
   kusma suyu parıltısı, perdah izi, döküm sınırı" bilir.
```

---

# 1. KORPUS CÜMLESİ — hangi külliyat, hangi alet, hangi ışık  [DERS 34 · A9-a]

```
⛔ KORPUSU OLMAYAN SAHA CGI'YE DÜŞER [DERS 34 — ölçüldü].
   "a hard-mounted engineering camera" diye bir fotoğraf külliyatı YOKTUR;
   ① SURFACE TRUTH 0/10 geldi. Prompt VAR OLAN bir külliyatı ALETİYLE anar.

KURAL  Korpus cümlesi ÜÇ şey taşır: külliyat · alet (film/sensör + lens) · ışık.
       Üçü de gerçek olmak zorundadır.
       ✅ "a Mars rover mast camera frame: flat butterscotch light, fine sensor
           grain, slightly crushed blacks, no lens flare"
       ✅ "a 1970s surface photograph from a hand-held 70 mm film camera: flat
           grey regolith, blown highlights, razor-edged black shadows, slight
           grain, no haze"
       ✅ Dünya şantiyesi: "a construction-progress photograph from a fixed
           24 mm full-frame site camera at f/8, midday sun, hard shadows,
           dust on the front element"
TEST   Külliyatın adını arama motoruna yaz — FOTOĞRAF mı çıkıyor, konsept
       sanatı mı? Çıkmıyorsa külliyat yoktur.
⚠️ A9 raporunun "Concrete Pouring Field Archive / Canon EOS R5, 35mm f/2.8"
   gibi külliyat adları TANIMDIR, arşiv adı değil; testten geçmez. Ayakta kalan
   kısım ALET + IŞIK sütunudur (Mastcam-Z · Kodak KAI-2020 CCD gerçektir).

⭐ Negatif çekirdekteki "working construction site" cümlesi pozitif hâliyle
   her prompt gövdesinde tekrarlanır: çamur, lastik izi, su birikintisi,
   istiflenmiş malzeme, branda, kesme artığı [D-c] — AMA §3'teki SAHA
   sütunundan; havasız sahada bu liste başkadır.
```

---

# 2. ⭐ BANT KURALI — 0,5 m eşiği nesne içindir, çizgi aşar  [A9-d · ÖLÇTÜM]

```
Kadraj 33,75 × 60,0 m · 32 px/m · 1 px = 3,125 cm  (24 mm · 40 m · 9:16)

NESNE (tek başına)       okunur mu     BANT / ALAN                       okunur mu
yağ damlası 5–15 cm     2–5 px ✗       pas akıntısı 0,2 m × 1–3 m       6 × 32–96 px ✓ (çizgi)
cıvata, halat aşınması  <5 px  ✗       çamur yolu 1,5–3 m genişlik      48–96 px ✓ (koyu bant)
tek kaynak yanığı       ✗              şerbet lekesi 1–2,5 m            32–80 px ✓ (açık alan)
tek taş sıçraması (Ay)  0,3–1,6 px ✗   ejecta yelpazesi 2–8 m           64–256 px ✓ (koyu yelpaze)
                                       naylon örtülü palet 1,2 × 1,2 m   38 × 38 px ✓ (doygun blok)
                                       birikinti 2–5 m                  64–160 px ✓ (gök yansıması)

KURAL  SITE TEXTURE cümlesi NESNE SAYMAZ, BANT ve ALAN yazar:
       ✗ "oil drips, frayed rope, bolt rust"
       ✓ "a wide band of wet mud from the gate to the pump, rust streaks running
          down the steel, a pale slurry apron around the pour point"
       Sebep: 0,5 m altındaki nesne 16 px'in altındadır ve token harcar
       [INSAAT_YONTEMI §1 · prompt_kontrol.py 0,5 m kapısı]; aynı malzeme
       ÇİZGİ ya da ALAN olarak yazıldığında 40 metreden okunur.
```

---

# 3. MALZEME KARTLARI — gerçek görünüm · AI'nin yanlışı · pozitif cümle

> Kaynak: A9 Section 1. Etiket sütunu raporundur; standart adları gerçek,
> bölüm numaraları çekilmedi → sayılar VARSAYIM. RGB/L* değerleri mertebedir.

| Malzeme | Gerçek şantiye fotoğrafında | AI / ArchViz'in tipik yanlışı | Etiket |
|---|---|---|---|
| Taze beton | koyu ıslak gri (RGB ~45–65) · kusma suyu parıltısı · perdah izi · döküm sınırı | plastik homojen gri parlaklık · sınır yok | VARSAYIM (ACI 308R adı doğru) |
| 7–28 gün kürlenen | 7 gün alacalı nemli gri · 28 gün mat kemik grisi (L* ~75) · tebeşirimsi kür kimyasalı izi | tek ton mat gri · kür izi yok | VARSAYIM (ASTM C309 adı doğru) |
| Yaşlanmış beton | karbonatlaşma · dikey su akıntı lekesi · kılcal çatlak ağı · beyaz tuz kusması | yönsüz rastgele kir dokusu · akıntı hattı yok | VARSAYIM (MDPI atfı çekilmedi) |
| Çelik (boyasız/astar/boya/pas) | mavi-gri hadde kabuğu · mat kiremit astar · pullanan turuncu-kahve pas · çukurlaşma | pürüzsüz turuncu kaplama · nakliye çiziği yok | VARSAYIM (ISO 8501-1 adı doğru) |
| Kalıp panosu (yeni/kullanılmış) | koyu kahve fenolik parlaklık · ek yerinde kurumuş şerbet · yağ lekesi · kenar şişmesi | kusursuz kontrplak · şerbet sızıntısı yok | VARSAYIM (PERI adı doğru) |
| Cam + alüminyum giydirme | toz filmi (yansıma %15–30 düşer) · silikon derz · vantuz izi · eloksal ton farkı | ayna gibi kusursuz yansıma | VARSAYIM · kaynak yok |
| Kazılmış toprak / şev | kepçe tırnak izi · kayma çatlağı · dipte koyu nemli, üstte açık kuru · serbest kaya | homojen kahverengi gürültü | VARSAYIM · kaynak yok |
| Ay / Mars regoliti | Ay: koyu gri (albedo ~0,12), keskin gölge, pus yok · Mars: kızıl-turuncu ince toz · kazıda alttan çıkan KOYU katman | yumuşak atmosferik gölge · Dünya kumulu dokusu | İDDİA (Mastcam-Z belgesi adı doğru) |
| Sıkışmış kar / permafrost | kar üstünde gri-siyah egzoz kırıntısı ve çamur · kesitte yarı saydam MAVİ buz · rüzgâr örtüsü | köpük gibi homojen beyaz | VARSAYIM · kaynak yok |
| Membran / şişirilebilir kumaş | gergin çift eğrili form · kaynak dikişinde renk farkı · alçak kıvrımda toz · kısmi ışık geçirgenliği | sert parlak plastik kubbe | VARSAYIM · kaynak yok |
| Asfalt (taze/soğumuş) | zift siyahı + yağlı parıltı + BUHAR · soğuyunca füme gri, agrega taneleri, silindir hattı | buharsız düz gri | VARSAYIM · kaynak yok |
| Tuğla + harç | derzden taşan harç · döküntü lekesi · harman ton farkı · beyaz tuz kusması | kusursuz dizilim · lekesiz derz | VARSAYIM · kaynak yok |
| Ahşap | kaba biçim kıymığı · budak · reçine kusması · dışta gümüş-gri patina | cilalı mobilya dokusu | VARSAYIM · kaynak yok |

```
⭐ ORTAK MEKANİZMA (13 satırda aynı): AI yüzeyi "çok pürüzsüz · çok homojen ·
   çok parlak · çok doygun · aynı dokunun tekrarı" üretir. Pozitif cümle bu
   beşin tersini SOMUT NESNEYLE yazar: leke, akıntı, sınır, ton farkı, kir bandı.
```

---

# 4. MALZEME = SAAT — yaşlanma takvimi ve üç zaman yayı  [A9-b · A9-c · A9-e]

> Taşıyıcı KURALI (beton renk sınırı bir saattir) ZAMAN_VE_ISIK §6'dadır ve
> orada kalır. Burada yalnız malzemenin o yaştaki GÖRÜNÜMÜ ve hangi yayda
> okunduğu vardır.

```
BETON KÜRLENME (VARSAYIM · ACI 308R-16 / ASTM C309 adı doğru, sayı çekilmedi)
   0–1 gün   koyu ıslak arduvaz grisi · CIE Y %15–20 · su filmi parıltısı
   1–3 gün   ALACALI: ıslak koyu + kurumaya başlayan orta gri · kalıp yağı izi
   3–7 gün   Y %35–45 · ⭐ 3 gün ara ile dökülmüş iki aks EKRANDA ayrılır
   7–28 gün  kemik grisi · Y %60–70 · L* ~75 · tebeşirimsi kür kimyasalı izi
   28+ gün   renk kararlı
PAS (VARSAYIM · ISO 9223 sınıfları)
   C1–C2 şehir içi: görünür pas noktası AYLAR alır
   C5–CX kıyı / endüstri: 80–200 µm/yıl · kumlanmış açık çelikte flash rust SAATLER
RÜZGÂRSIZ DÜNYA (A9-f · P1-d ile aynı)
   toz yalnız FAALİYETLE birikir — araç geçişi, kazı, ejecta; faaliyet
   durunca yüzey değişimi durur. "Zamanla tozlanan iniş aracı" fizik dışıdır.
```

| Zaman yayı | 32 px/m'de GÖZLE GÖRÜLÜR | AYIRT EDİLEMEZ |
|---|---|---|
| **1–3 yıl** | ilk faz beton ile yeni döküm arasındaki YAŞ FARKI + dikey su akıntı çizgileri · açık çeliğin turuncudan koyu kahveye geçişi (C3–C5) · zeminin topraktan asfalta dönmesi · cam cephede toz → yansıma kaybı | <1 mm kılcal çatlak · membran UV solması · alüminyumda kılcal çizik |
| **birkaç ay** | taze döşemenin koyu ıslaktan 28 günlük kemik grisine dönmesi · zift siyahının füme griye soğuması · nakliye yolunda iz DERİNLİĞİNİN artması · kür örtüsü serilip sökülmesi ve altındaki alacalı leke | C1–C2 çelikte korozyon (<2 µm) · yağmursuz dönemde cam tozu |
| **TEK GÜN** | döküm anındaki ıslak parlaklığın ilk 6 saatte MATLAŞMASI · taze asfalt BUHARI ve zift parıltısı · makine geçişiyle o gün açılan YENİ iz · birikintinin güneşle küçülmesi | ⛔ betonun kürlenme RENGİ (1. gün ile 2. gün 40 m'de okunmaz) · atmosferik pas · kumaş/cam tozu |

```
KURAL  Aşama merdiveninin zaman yayına göre SITE TEXTURE'a yalnız o yayda
       OKUNAN değişim yazılır. Tek günlük filme "cured pale grey slab" yazmak
       (POLAR HABITAT · THE LONG DAY tipi) yalan söyler: o gün beton hâlâ koyudur.
```

---

# 5. SAHA KARTI — kirlilik katmanları saha tipine göre  [A9 Section 2 · ÖLÇTÜM px]

| Saha | Uzaktan OKUNAN katman (bant/alan) | px @32 px/m | Yalnız yakın planda var olan (YAZILMAZ) |
|---|---|---|---|
| Şehir içi | kapıdan pompaya ÇAMUR YOLU 1,5–3 m · şerbet ve döküntü alanı 1–2,5 m · mavi/yeşil naylon örtülü paletler 1,2 m · gökyüzünü yansıtan birikinti 2–5 m | 48–96 · 32–80 · 38 · 64–160 | yağ damlası, halat aşınması, cıvata pası (2–5 px) |
| Kırsal | palet/teker çukuru (0,8 m geniş, 0,2 m derin — GÖLGE hattıyla okunur) · kahverengi su dolu rut · açık toprakta iz yolları · kesme artığı + donatı istifi | 25 · 64–160 | — |
| Kıyı | çelikten aşağı DİKEY PAS AKINTISI (0,2 m × 1–3 m) · rüzgârın temele yığdığı nemli kum · tuz | 6 × 32–96 | — |
| Dağ / kar | kar üstünde egzoz kurumu ve çamur BANTLARI 1–4 m · kırağı tutmuş çelik · bariyere yığılan kar | 32–128 | — |
| Çöl | yapı dibinde rüzgârla yığılan açık kum 0,5–1,5 m · duran her ekipmanda toz filmi · sert güneş, keskin gölge | 16–48 | — |
| Ay / Mars | kazı çevresinde KOYU alt regolit ejecta örtüsü 2–8 m · keskin tekerlek izi · ⛔ su, çamur, birikinti YOK | 64–256 | mikrometeorit izi, tek taş (0,3–1,6 px) |
| Buzul / permafrost | buz duvarında koyu silt KATMAN BANTLARI 0,5–2 m · termokarst gölcüğü (koyu buz tabanı) · sert zemine donmuş makine izi | 16–64 | — |

```
⛔ SAHA ÇELİŞKİ KAPISI [A9-g]: görsel prompt "vacuum · airless · regolith ·
   no atmosphere" diyorsa SITE TEXTURE'da "mud · puddle · standing water ·
   rain" olamaz → prompt_kontrol.py BLOCK. Beş filmde aynı cümle Dünya'dan
   Ay'a taşındı; fizik dışıydı ve model saçmaladı.
```

---

# 6. PROMPTA İNEN CÜMLELER — İngilizce · POZİTİF · kopyalanır

> A9 Section 4'ten alındı; negatif kalıplar ("zero haze", "absolute absence")
> DERS 33 gereği pozitif hâle çevrildi. Her cümle BANT/ALAN kuralına uyar.

```
MALZEME
Fresh concrete   The wet freshly poured slab shows a dark grey glossy sheen with
                 pools of bleed water reflecting the sky and faint float-trowel swirls.
Cured concrete   The cured slab is pale bone-grey and matte, mottled with darker damp
                 patches, with a visible pour seam against the adjacent bay and chalky
                 white curing-compound streaks.
Aged concrete    The older concrete carries dark vertical water run-down stains below
                 every drip edge, a fine network of surface crazing and powdery white
                 efflorescence at the joints.
Steel            The steel members show flaking blue-grey mill scale, patches of matte
                 red-oxide primer, bright scratches where bare metal shows, and orange
                 rust streaks running down from the flange edges.
Formwork         The phenolic formwork panels are dark brown and glossy, crusted with
                 dried grey slurry along every joint, streaked with release oil and
                 swollen at the edges.
Glass cladding   A thin film of construction dust dulls the glass so the reflections
                 read soft, with dark silicone bead lines and slight tone differences
                 between neighbouring aluminium mullions.
Excavation       The cut slope carries steep bucket-tooth grooves, dark moist soil at
                 the base grading to pale dry silt at the crest, loose clods and shear
                 cracks along the face.
Regolith         The regolith is fine grey powder under razor-sharp black shadows, with
                 dark freshly turned material fanning out from the excavation in ejecta
                 rays and crisp angular wheel tread prints; the surface is dry to the horizon.
Snow / ice       The compacted snow apron is banded with dark grey gravel and exhaust
                 grime along the haul route, and the trench walls expose translucent blue
                 layered ice under a crust of wind-packed drift.
Membrane         The membrane is stretched into taut double-curved panels, its heat-welded
                 seams a shade darker, with dust settled in the lower folds and a matte,
                 weather-dulled surface.
Asphalt          The fresh asphalt is pitch black with a wet bitumen sheen and rising
                 steam, cooling behind the roller into charcoal grey with visible
                 aggregate and compaction lines.
Brick            The brickwork shows rough mortar squeeze-out along the bed joints,
                 shade variation between courses and powdery white efflorescence patches.
Timber           The timber members are rough-sawn with open grain, dark knots, resin
                 bleed and a silver-grey weathered face on the exposed side.

SAHA
Urban            A wide band of wet mud runs from the gate to the pump, a pale slurry
                 apron surrounds the pour point, blue tarpaulins are strapped over the
                 pallets and standing rainwater mirrors the buildings.
Rural            Deep tyre ruts hold brown standing water, crawler track paths cross the
                 open soil, and timber offcuts lie beside the stacked reinforcement.
Coastal          Orange salt-spray rust streaks run down the steel, damp wind-blown sand
                 has drifted against the concrete footings, and the light is hard and maritime.
Mountain / snow  Dark diesel-grime lanes cut through the compacted snow, the steel is
                 frosted, and drifts have piled high against the temporary barriers.
Desert           Fine pale sand has drifted against every windward base, a dust film
                 dulls the parked plant, and the shadows are crisp and hard.
Moon / Mars      Dark disturbed regolith blankets the ground around the pits, rover
                 tread prints are deep and sharp-edged, and the ground is dry powder to
                 the horizon under razor-sharp shadows.
Glacier          Dark silt bands are locked inside the exposed ice walls, meltwater
                 ponds sit on dark ice beds, and heavy track impressions are frozen hard
                 into the ground.
```

---

# 7. KAPI — bu kılavuz nerede zorlanır

```
prompt_kontrol.py §10d (11.09.2026):
  · SITE TEXTURE bloğunda ≥5 somut yüzey nesnesi/bandı yoksa            → FIX
  · görsel prompt havasız/regolit dünyası beyan ediyor ve SITE TEXTURE
    "mud · puddle · standing water · rain" içeriyorsa [A9-g]             → BLOCK
  · 0,5 m altı nesne adı (mevcut kapı, INSAAT_YONTEMI §1)               → FIX

ELLE
  · korpus cümlesindeki külliyat adı arama motoruna yazılır; fotoğraf çıkmıyorsa
    kare üretilmez [DERS 34]
  · zaman yayı ile SITE TEXTURE'ın yaşlanma satırı §4 tablosuna karşı okunur:
    tek günlük filme kürlenmiş beton yazılmaz

ÖLÇÜLECEK (ilk üretimden sonra)
  · A9-b kürlenme sayıları · A9-c pas hızları · §3 kartlarının 13 satırı —
    ① SURFACE TRUTH skoru bu kılavuzla 3/10'un üstüne çıkıyor mu?
```
