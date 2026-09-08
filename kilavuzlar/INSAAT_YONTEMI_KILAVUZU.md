# 🧱 İNŞAAT YÖNTEMİ KILAVUZU — bir şeyin YAPILDIĞINI göstermek

> Bu depodaki en ağır ve en tekrarlı arıza burada tarif ediliyor.
> THE LONG DAY'de dokuz yapı elemanı tek tek izlendi ve **dokuzun sekizi
> ekranda TAMAMLANMIŞ hâlde doğdu:** "graded pad: NEVER made on screen",
> "central mast: NEVER", "twin towers: NEVER", "access road: NEVER".
> Hüküm ⑧ **APPEARED · 1/9 MADE** oldu. Aynı arıza ② merceğinde
> **beş filmin BEŞİNDE** "DIFFERENT · APPEARING" hükmüyle tekrarlandı.
>
> Sebep tek cümlede: **plan aşamaları yazıyordu, ara hâlleri yazmıyordu.**
> Bir eleman ya yoktu ya vardı. Arada hiçbir şey yoktu — ve inşaat tam olarak
> o aradadır.
>
> Kaynak: `arastirma/SONUCLAR/A5_GEMINI_HAM.md` (denetim: `A5-A8_DENETIM.md`)
> ⚠️ Raporun üç standart atfı yanlıştı ve kadraj hesabı düştü; ikisi de
> aşağıda düzeltilmiş hâliyle duruyor. Rapordan tek bir SAYI alınmadı.

---

# 1. KADRAJ NE GÖSTERİR — önce bu, sonra her şey

Bir ara hâl ancak **görünüyorsa** işe yarar. Kadraj hesabı göz kararı değildir.

```
GİRDİ    24 mm eşdeğeri · 40 m mesafe · 9:16 dikey · 1080×1920
HESAP    uzun kenar FOV 73,7°  →  2 × 40 × tan(36,85°) = 60,0 m
ÇIKTI    ⭐ KADRAJ = 33,7 m GENİŞ × 60,0 m YÜKSEK · 32,0 px/m
         60 m = 3 m'lik katla YİRMİ kat.
```

**Piksel karşılıkları — prompta ne yazılabileceğini bu tablo belirler:**

| nesne | gerçek boy | ekranda | hüküm |
|---|---:|---:|---|
| ekskavatör / kule vinç bomu | 6,0 m | 192 px | tartışmasız |
| kat yüksekliği | 3,0 m | 96 px | tartışmasız |
| **insan** | 1,8 m | **58 px** | ⭐ **GÖRÜNÜR** |
| kalıp panosu kenarı | 0,6 m | 19 px | şekil olarak okunur |
| donatı çapı · civata · fitil | 0,1 m | 3 px | ⛔ görünmez |

```
⭐ OKUNABİLİRLİK EŞİĞİ ≈ 0,5 m.
   Bundan küçük nesne prompta YAZILMAZ — token harcar, kadraja inmez.
   ⛔ Prompta "torque marks", "sealant bead", "curing test cylinder" yazma.

⭐ VE ŞU YANLIŞ: "insan 40 metrede görünmez."
   İnsan 58 piksel — görünür. İnsanı yok eden MESAFE değil ZAMAN
   SIKIŞTIRMASIDIR. O ayrı bir konudur → SANTIYE_HAREKETI_KILAVUZU §2.

⛔ Mesafe 40 m değilse bu tablo GEÇERSİZ. Yeniden hesapla:
   yükseklik = 2 × mesafe × tan(36,85°) · px/m = 1920 / yükseklik
```

---

# 2. TEMEL KURAL — her sahne bir elemanı ARA HÂLDE gösterir

```
⛔ YASAK      "the foundation is complete"        → beliren
⛔ YASAK      "the tower has twelve floors"       → beliren
✅ ZORUNLU    "the third column is half poured: its steel formwork is still
              clamped around the lower two metres while the bare rebar cage
              stands above it"                    → yapılan

ÜÇ ARA HÂL SABİTTİR:  %25 · %50 · %75
Her ara hâl bir GEÇİCİ EKİPMANLA tanımlanır. Geçici ekipman yoksa ara hâl
yoktur — yalnız bitmiş bir nesne vardır.

GEÇİCİ EKİPMAN SÖZLÜĞÜ (ara hâlin tek kanıtı bunlardır)
   kalıp (formwork) · donatı kafesi (rebar cage) · iskele (scaffold) ·
   dikme/payanda (shoring prop) · tırmanır kalıp (climbing formwork) ·
   kür örtüsü (curing blanket) · vinç sapanı (crane sling) ·
   vakumlu kaldırıcı (vacuum lifter) · geçici gergi (temporary guy)
```

**⭐ ÜÇ TARTIŞMASIZ İŞ KANITI** — 40 m'de okunur, fizikle bağlıdır, hiçbir
araç bunları "tamamlanmış" diye halüsine edemez:

```
① GERGİN SAPAN     crane sling taut
   Bir kolon, kiriş ya da panel yerine konmuş olsa bile sapan gerginse
   izleyici onun O AN yerleştirildiğini anlar. Eleman henüz kendi ayakları
   üstünde değildir. ⛔ Boş kanca yazılmaz [DERS 8].
② TOZ BULUTU        lingering dust cloud
   Kazı, silindir, greyder. Toz ancak BİR ŞEY HAREKET ETTİYSE vardır.
③ ISLAK BETON PARLAKLIĞI   wet concrete gloss
   Taze döküm ışığı ayna gibi yansıtır; kurumuş mat betondan bir bakışta
   ayrılır. Aynı karede yarısı parlak yarısı mat zemin = döküm sürüyor.
```

---

## ⭐ 2.4 ARA HÂL SİLUETİ DEĞİŞTİRİR — yüzeyi değil  [DERS 37]

```
THE DUST YEAR'da pad'in ara hâlleri şöyleydi:
   %25 ham kesik · %50 DÜZLENMİŞ daire · %75 SİNTERLENMİŞ camsı kabuk
%50 ile %100 arasındaki fark YÜZEY MALZEMESİDİR: aynı çap, aynı kenar.
⑧ merceği %50'yi "first seen COMPLETE" diye yazdı — ve haklıydı.

KURAL  Her ara hâl silueti ölçülebilir biçimde değiştirir, üçünden biriyle:
   ① SAYI       kaç parça duruyor      3/6 panel · 3/6 direk bölümü
   ② YÜKSEKLİK  taç kaç metrede        berm 1,6 m → 3,0 m
   ③ KAPSAM     kenar nereye ulaştı    daire kayanın dibine
⛔ Yalnız malzeme/renk/doku değişen hâl ARA HÂL SAYILMAZ — kendi sahnesini
   hak etmez, bir üst hâle katlanır. §1'in 0,5 m eşiği nesnenin BOYUTU
   içindir; bu, ara hâlin FARKI içindir.
⚠️ Tek başına yetmez: aynı filmde "three of their six panels open on each"
   SAYI değiştiriyordu ve yine COMPLETE geldi. DERS 36 ile BİRLİKTE koşar.
```

# 3. ELEMAN KARTLARI — önkoşul · üç ara hâl · süre

> Sıra bağlayıcıdır: bir elemanın %25'i, önkoşulunun en az %75'i olmadan
> ekrana giremez. Bu merdivenin ihlali ⑤ DEVAMLILIK'ta dikiş kusuru olarak
> çıkar. Süreler MERTEBEDİR, ölçüm değildir — merdiven aralığı için vardır.

```
┌── KAZI VE ŞEV ──────────────── önkoşul: arsa temizliği · 10-15 gün ──┐
│ %25  yüzey sıyrılmış, ham toprak, kepçe diş izleri                    │
│ %50  teraslanmış basamaklar, şev açısı belirgin, toz                  │
│ %75  şev yüzeyinde çelik hasır + püskürtme beton + ankraj başlıkları  │
└───────────────────────────────────────────────────────────────────────┘
┌── RADYE / KAZIKLI TEMEL ────── önkoşul: kazı %75 · 20-30 gün ────────┐
│ %25  fore kazık makinesi dikey, burgu toprakta, çevresinde ıslak çamur│
│ %50  groboton mat gri + üstünde adım atılamayacak sıklıkta donatı ızgarası│
│ %75  çevre kalıbı kapalı, taze beton ayna gibi parlıyor               │
└───────────────────────────────────────────────────────────────────────┘
┌── KOLON ────────────────────── önkoşul: radye/döşeme %75 · 2-4 gün/kat┐
│ %25  döşemeden yukarı filizlenen ÇIPLAK donatı kafesi, etrafı boş     │
│ %50  kalıp panoları donatının etrafına kapanmış, kuşak ve payandalar  │
│ %75  kalıp sökülmüş, beton koyu ve nemli, şeffaf kür örtüsü sarılı    │
└───────────────────────────────────────────────────────────────────────┘
┌── PERDE / ÇEKİRDEK ─────────── önkoşul: radye %75 · 5-7 gün/kat ─────┐
│ %25  arkası görünmeyecek kadar sık donatı duvarı, uçlarda demir yığılması│
│ %50  tırmanır kalıbın devasa panelleri duvarı kapatmış, dış iskele    │
│ %75  kalıbın alt yarısı açık, üst panel vincin GERGİN sapanında asılı │
└───────────────────────────────────────────────────────────────────────┘
┌── DÖŞEME ───────────────────── önkoşul: kolon/perde %75 · 14-21 gün ─┐
│ %25  altında orman gibi sık teleskopik dikme + yatay taşıyıcı kirişler│
│ %50  plywood yüzey kapalı, üstünde hasır çelik seriliyor              │
│ %75  beton pompası hortumu sahnede, zeminin yarısı parlak yarısı mat  │
└───────────────────────────────────────────────────────────────────────┘
┌── ÇELİK KOLON-KİRİŞ / MAKAS ── önkoşul: temel %75 · 1-2 gün/birleşim ┐
│ %25  kolon havada, sapanlar gergin, ankraj bulonlarına iniyor         │
│ %50  kiriş bağlanmış ama SAPAN HÂLÂ GERGİN, yanında sepetli vinç      │
│ %75  birleşimde kaynak kıvılcımı, kanca boşa çıkmış sapan sarkıyor    │
└───────────────────────────────────────────────────────────────────────┘
┌── CEPHE / GİYDİRME ─────────── önkoşul: karkas %75 · 3-5 gün/kat ────┐
│ %25  döşeme alınlarına ankrajlı ÇIPLAK dikey profiller, iskelet ızgara│
│ %50  yatay profiller takılı, aralarda yalıtım panelleri, CAM YOK      │
│ %75  vakumlu kaldırıcı devasa cam paneli cepheye yaklaştırıyor        │
└───────────────────────────────────────────────────────────────────────┘
┌── ÇATI ─────────────────────── önkoşul: üst kat karkası · 10-15 gün ─┐
│ %25  çıplak makaslar/mertekler havaya açılı, altı tamamen boş         │
│ %50  örtünün alt katmanı yarı serilmiş, kalan iskelet görünüyor       │
│ %75  membran rulosu yarı açılmış, ucunda turuncu pürmüz alevi         │
└───────────────────────────────────────────────────────────────────────┘
┌── SAHA YOLU ────────────────── önkoşul: ağır iş bitti · 5-7 gün ─────┐
│ %25  greyder hatta çalışıyor, zemin düzleşmiş, derin tekerlek izleri  │
│ %50  gri kırma taş serilmiş, titreşimli silindir üstünde, ince toz    │
│ %75  siyah taze asfalt sericiden dökülüyor, üstünden buhar tütüyor    │
└───────────────────────────────────────────────────────────────────────┘
┌── TOPRAK BERM / DOLGU ──────── önkoşul: saha hazırlığı · 3-5 gün ────┐
│ %25  gevşek toprak sırtı, düzeltilmemiş, tekerlek izleriyle dalgalı   │
│ %50  silindir şev üstünde, yüzeyde dalgalı sıkışma izleri             │
│ %75  geometrik şev açısı netleşmiş, yeşil tohumlu su püskürtülüyor    │
└───────────────────────────────────────────────────────────────────────┘
┌── ÇELİK DİREK ──────────────── önkoşul: temel %75 · 2-4 gün ─────────┐
│ %25  yalnız taban flanşı bağlı, gergi telleri yerde KIVRIK duruyor    │
│ %50  alt üç parça flanşlarla bağlı, dördüncüsü kancada havada         │
│ %75  gergi telleri bağlı, DÜMDÜZ ve gergin; kanca direkten ayrılmış   │
└───────────────────────────────────────────────────────────────────────┘
┌── ANTEN / ÇANAK ────────────── önkoşul: direk %75 · 1-2 gün ─────────┐
│ %25  direğin tepesinde BOŞ kelepçeler, çanak kadrajda yok             │
│ %50  çanak havada, altından yönlendirme halatları sarkıyor            │
│ %75  çanak bağlı, vinç yok, koaksiyel kablolar direk boyunca iniyor   │
└───────────────────────────────────────────────────────────────────────┘
```

```
⛔ STANDART ADI YAZMA. Rapor üç yerde yanlış standart gösterdi (ASTM A325/
   A490 2015'te F3125 altında birleşti · EN 13830 montaj sırası şart koşmaz ·
   ASTM D698 laboratuvar deneyidir, saha tabaka kalınlığını yazmaz) [A5-X1..X3].
   Ekrana inen görüntü standart numarasından bağımsızdır. Prompta standart
   yazılmaz; GÖRÜNEN ŞEY yazılır.
```

---

# 4. AY VE UZAY — donanımı olan ile konsept olan ayrılır

```
⭐ TRL AYRIMI ZORUNLU. Uçmuş/test edilmiş donanım ile konsept çizimi aynı
   filmde eşit ağırlıkta gösterilemez; gösterilirse ④ TESLİM'de "bu ne
   zaman oluyor" sorusu cevapsız kalır.

UÇMUŞ / TEST EDİLMİŞ            → ana aşama olabilir
  şişirilebilir modül (ISS'te uçtu) · robotik matkap ve rover paletleri ·
  dozer bıçağıyla regolit itme · sinterlenmiş/eritilmiş zemin karosu
LABORATUVAR / KONSEPT           → ⛔ ana aşama OLAMAZ, en fazla arka plan
  otonom robot sürüsüyle yapısal montaj · biyomimetik çoklu ajan

┌── İNİŞ PEDİ DÜZLEME ────────────────────────────────────────────────┐
│ %25  paletli rover izleri; dozer bıçağı regoliti itiyor, kalkan toz  │
│      ⭐ ATMOSFER YOK: toz havada asılı KALMAZ, parabol çizip düşer   │
│ %50  alan dairesel kazınmış ve düzleşmiş                             │
│ %75  pedin çevresinde egzoz kontrolü için dairesel derin hendek      │
└──────────────────────────────────────────────────────────────────────┘
┌── ISRU / SİNTERLEME ────────────────────────────────────────────────┐
│ %25  robotik ayırıcı toprağı eliyor, koni yığınlar                   │
│ %50  sinterleme ucu zeminde geziyor, altında AKKOR kırmızı parlama   │
│      ⛔ "püskürten 3D yazıcı ucu" yazma — ERİTEN ve PARLAYAN yaz     │
│ %75  altıgen karolar dizili; ortası koyu gri, kenarları hâlâ turuncu │
└──────────────────────────────────────────────────────────────────────┘
┌── REGOLİT BERM / RADYASYON SİPERİ ──────────────────────────────────┐
│ %25  robotik matkap yüzeyi deliyor, sert regolit parçaları çıkıyor   │
│ %50  robotik kol regolitle şişmiş polimer torbayı yüzeyden kaldırıyor│
│ %75  torbalar tuğla gibi istiflenmiş, modülün çevresinde bel hizası  │
└──────────────────────────────────────────────────────────────────────┘
┌── AÇILIR YAPI (deployable) ─────────────────────────────────────────┐
│ %25  buruşuk kumaş paket iniş aracının yanına kayışlanmış            │
│ %50  modül şişmeye başlamış: yüzeyde DERİN ve GEVŞEK kırışıklıklar   │
│ %75  tam basınç: kumaş davul derisi gibi GERGİN ve pürüzsüz          │
└──────────────────────────────────────────────────────────────────────┘
```

---

## ⭐ 4.4 KORPUS: ADIN KENDİSİ YAPIYI DEĞİŞTİRİR  [DERS 42 · 34]

```
THE DUST YEAR · ölçülmüş üç sapma — üçü de yalnız ADDAN doğdu:
   "regolith bags"                → sandbag wall (askerî mevzi; ⑤'te söküldü)
   "lattice mast + spools"        → drilling rig / drilling tower
   "inflatable habitat cylinder"  → hemispherical dome
"dome" · "cladding" · "drill" · "sandbag" kelimelerinin DÖRDÜ de plan
metninde SIFIR kez geçiyor. Model onları ADDAN türetti.

KURAL  Her YAPI BIBLE adı için tek soru: bu ad en sık NEYİN yanında geçer?
       Ad istenen GEOMETRİYİ taşımıyorsa ad değil GEOMETRİ yazılır:
   ⛔ regolith bags        ✅ stacked regolith-filled tubes laid in level
                             courses, each course stepped back 0.3 m
   ⛔ lattice mast         ✅ bolted three-leg guyed tower, six sections,
                             a 1.6 m parabolic reflector on the fifth
   ⛔ inflatable cylinder  ✅ upright fabric drum, flat circular roof,
                             vertical sides, 8.0 m across and 6.4 m tall
⛔ NEGATİF DEĞİL GEOMETRİ: "no dome" yazmak DERS 33'tür. Kubbeyi engelleyen
   şey "flat circular roof, vertical sides"tır.

🔻 §4'ÜN KORPUS CÜMLESİ ÖLÇÜLDÜ VE DÜŞTÜ  [DERS 34]
   "a hard-mounted engineering camera" diye bir fotoğraf külliyatı YOKTUR;
   ① SURFACE TRUTH 0/10 geldi. Korpus VAR OLAN bir külliyatı ALETİYLE anar:
   ✅ "a Mars rover mast camera frame: flat butterscotch light, fine sensor
      grain, slightly crushed blacks, no lens flare"
   TEST: adı arama motoruna yaz — fotoğraf mı çıkıyor, konsept sanatı mı?
```

# 5. PROMPTA İNEN CÜMLELER — İngilizce · POZİTİF · kopyalanır

> ⛔ Bunlar yasak cümlesi değildir. Yasak özne üretir [DERS 33].
> Her cümle ölçülebilir bir çapadır [DERS 11] ve `AT THIS STAGE` bloğuna girer.
> Cümleyi kısaltma: geçici ekipman adı düşerse ara hâl düşer.

```
KAZI      %25  the site topsoil is fully stripped to raw brown earth, and deep
               excavator bucket teeth marks are cut into the exposed ground
          %50  the pit is terraced into stepped dirt benches where crawler
               excavators rest, wrapped in a thick lingering dust cloud
          %75  the slope face is covered by steel wire mesh over rough grey
               shotcrete, pierced by rows of metallic soil nail anchor heads

TEMEL     %25  a tall piling rig stands vertical on the dirt with its steel
               auger buried in the ground and wet grey mud spilled around it
          %50  a flat matte layer of lean concrete carries a rusty rebar grid
               so dense that no footing space is left between the bars
          %75  the raft is being poured inside wooden formwork planks, and the
               fresh concrete reflects the sky with a mirror-like glossy sheen

KOLON     %25  bare vertical rebar cages sprout straight out of the concrete
               slab below and stand unsupported with empty space around them
          %50  tall rectangular steel formwork panels are clamped around the
               rebar and braced by diagonal shoring props down to the floor
          %75  the formwork is stripped off and the dark wet concrete pillar
               is wrapped tight in transparent plastic curing blankets

PERDE     %25  a dense steel rebar mesh wall stands vertical, its boundary
               edges packed so tightly with bars that no light passes through
          %50  a large climbing formwork system encases the core wall with
               exterior scaffold platforms and safety rails along its outside
          %75  the lower half of the wall formwork is stripped to dark wet
               concrete while the upper panel hangs from a taut crane sling

DÖŞEME    %25  a dense forest of vertical telescopic shoring props fills the
               floor below a grid of horizontal timber beams, with no decking
          %50  a flat plywood deck covers the props and large rectangular
               grids of welded steel wire mesh are being laid across it
          %75  a concrete pump hose discharges wet glossy concrete onto one
               half of the slab while the other half shows matte screed marks

ÇELİK     %25  a steel column hangs in mid-air on taut crane slings, lowering
               toward the protruding anchor bolts set in the concrete below
          %50  a steel beam is bolted to the column while the crane slings
               stay fully taut and an elevated manlift basket sits at the joint
          %75  bright welding sparks fall from the beam-to-column joint while
               the crane hook hangs empty with loose slings beside it

CEPHE     %25  bare vertical aluminium mullion profiles are anchored in
               straight lines along the slab edges, forming an empty grid
          %50  horizontal transom profiles join the mullions and rockwool
               insulation squares fill the openings, with no glass in place
          %75  a large glass panel hangs in mid-air on a vacuum lifter fixed
               to a taut crane cable, reflecting the sky as it swings in

ÇATI      %25  bare diagonal steel trusses point at the sky and open air is
               visible all the way through the triangular skeleton
          %50  raw corrugated metal decking covers half the roof skeleton
               while the bare trusses stay exposed on the other half
          %75  a roll of black waterproofing membrane is unrolled halfway
               across the deck with an orange torch flame at its leading edge

YOL       %25  a motor grader drives the access road line, leaving deep tire
               ruts pressed into the flattened dirt subgrade
          %50  a thick layer of grey crushed stone covers the road while a
               vibratory steel roller runs over it, raising a low dust haze
          %75  an asphalt paver lays a fresh glossy black strip and grey steam
               rises straight off the hot surface behind it

BERM      %25  a loose brown soil ridge lies uncompacted and uneven, deeply
               scored by fresh tire tracks along its length
          %50  a compaction roller drives across the angled berm and leaves
               wavy compressed tire patterns on the smoothed slope
          %75  the berm holds a clean geometric slope and green hydroseeding
               liquid is being sprayed across its bare dirt face

DİREK     %25  a heavy steel base plate is bolted down and coiled guy wires
               lie loose and flat on the concrete pads around it
          %50  the lower three lattice sections are bolted together inside a
               temporary scaffold tower while the next section hangs above
          %75  the mast stands with its diagonal guy wires anchored down,
               every wire dead straight and taut under tension

ANTEN     %25  empty metal U-brackets and mounting clamps are bolted near the
               mast top and no dish is present on them
          %50  a white satellite dish hangs in mid-air on a taut crane cable
               with loose tagline ropes swinging below it
          %75  the dish is bolted to the mast with no crane in sight and thick
               black coaxial cables drape down the pole

AY        ped %50   a robotic dozer blade pushes grey regolith and the thrown
               dust flies in a clean airless parabola straight back to the ground
          sinter %50  a lunar sintering head crosses the ground and the regolith
               directly beneath it glows red hot as it melts
          berm %75   regolith-filled polymer bags are stacked like bricks into a
               waist-high protective wall around the lander
          şişme %50  the habitat fabric is half inflated and its surface carries
               deep loose wrinkles across the whole cylinder
```

---

# 6. KAPI — bu kılavuz nerede zorlanır

```
① PLANDA        Aşama merdiveninin her satırı bir ELEMAN ve bir ARA HÂL
                (%25/%50/%75) taşır. "temel biter" satırı kabul edilmez.
                Bir satırın elemanı, bir önceki satırın önkoşulunu sağlamalıdır.

② PROMPTTA      Her görsel promptun AT THIS STAGE bloğu §5'ten en az BİR
                cümle taşır ve o cümle geçici ekipman adı içerir.
                ⛔ prompt_kontrol.py: AT THIS STAGE bloğunda geçici ekipman
                   sözlüğünden hiçbir kelime yoksa → FIX.
                ⛔ 0,5 m'den küçük nesne adı geçiyorsa → FIX (§1).

③ ÜRETİM        Üretim günlüğü §2 satırına "ara hâl elle doğrulandı ✓/✗"
   GÜNLÜĞÜNDE   sütunu eklenir. ✗ olan kare atılır.

④ QA'DA         ⑧ YÖNTEM merceği "ilk beliren parça" sorar. §3'teki ara hâl
                kartı o parçanın hangi hâlinin atlandığını gösterir.
```

> ⭐ **KALDIRDIĞI:** bu kılavuz "bina bir ayda bu kadar büyüdü" diyen serbest
> sıçramaları kaldırır. Artık her sıçrama bir önkoşul zincirine borçlu. Bedeli:
> merdiven yazmak zorlaşır, iki sahne arasına bazen üçüncü bir sahne girmek
> ister. Karşılığı: yapı ekranda BÜYÜR, belirmez.
