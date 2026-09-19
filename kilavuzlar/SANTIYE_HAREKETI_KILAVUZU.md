# 🚜 ŞANTİYE HAREKETİ KILAVUZU — ekranda İŞ olduğunu göstermek

> THE LONG DAY'de beş büyüme olayının beşi için denetçi "o noktada görünen iş:
> HAYIR" yazdı. En uzun işsiz aralık **bir klibin tamamı — %100.** Hüküm
> ⑦ **PARKED.** Aynı filmde ① merceği **ekranda insan 0** ve **yüzey
> gerçekliği 0** ölçtü; görüntü sentetik okundu [DERS 34].
> Daha önceki bir filmde ise gökyüzü timelapse hızında koşarken işçiler ve
> kamyonlar gerçek zamanlı hızda yürüdü [DERS 15].
>
> Üç arıza tek bir eksiğin üç yüzü: **klibin hangi hızda aktığı hiç
> seçilmemişti.** Model gökyüzünü sıkıştırıp yeri sıkıştırmadı, çünkü ona
> kimse tek bir sıkıştırma oranı vermedi.
>
> Kaynak: `arastirma/SONUCLAR/A6_GEMINI_HAM.md` (denetim: `A5-A8_DENETIM.md`)
> ⚠️ Raporun sıkıştırma aritmetiği doğruydu ve teyit edildi; **gölge sayısı
> yanlıştı ve kendi tablosuyla çelişiyordu.** İkisi de aşağıda düzeltilmiştir.

---

# 1. ⭐ SIKIŞTIRMA REJİMİ — klip başına SEÇİLİR ve BEYAN EDİLİR

Bu kılavuzun tek yeni kavramı budur. Bir klipte gökyüzü, gölge, insan, makine
ve toz **aynı saate** tabidir. Rejim seçilmezse model her birine ayrı hız verir
— ve ⑦ ile ① aynı anda düşer.

```
REJİM = bir klibin kapsadığı GERÇEK ZAMAN PENCERESİ.
Ay atlaması KESMEDE olur; rejim KLİBİN İÇİNDEDİR. İkisi karıştırılmaz.
```

**6 saniyelik klip · 30 fps (180 kare) · 40°N için ölçüldü:**

| rejim | pencere | oran | sn/kare | gölge dönüşü (öğle) | insan | bulut |
|---|---:|---:|---:|---|---|---|
| **A · SAAT** | 10 dk | 100× | 3,3 | 2,6°–8,0° · fark edilmez | ⭐ **görünür**, hızlı ama tanınır | yumuşak akış |
| **B · YARIM GÜN** | 2 saat | 1200× | 40 | 30°–84° · ⭐ **bariz süpürme** | iz (streak) ve strobo | uzayan şerit |
| **C · İŞ GÜNÜ** | 9 saat | 5400× | 180 | 116°–191° · ⭐⭐ tam süpürme | ⛔ **tamamen kaybolur** | silinir, gök homojenleşir |
| **G · GERÇEK ZAMAN** ⚠️ | 8 sn | 1× | 0,033 | 0° · yok | ⭐ tam görünür — iz YOK, sırtı kameraya, yüz okunmaz | durur ("holds") |

```
⭐ REJİM G (18.09.2026 · ONE MORE TURN · ⚠️ ÖLÇÜLMEDİ): klip sıkıştırılmaz; ödül,
   filmin nesnesinin DOĞAL HIZDA hareket etmesidir (su çarkın ilk turu). Kural:
   · TIME RATE cümlesi "moves at natural speed … eight seconds pass" — "time-lapsed" YAZILMAZ
   · gölge süpürmesi YOK → ışık günü toplamına 0 dk girer; ışık, G'den önceki kesmede sabitlenir
   · insan izi (streak) fiziksel olarak yoktur → tek figür, sırtı kameraya, yüz okunmaz [DERS 15]
   · yalnız filmin SON sahnelerinde ve yalnız hareket ÖDÜLSE; süreç sahnesi G'de anlatılmaz
   · ⛔ A/B'den G'ye kesmede dere/su dokusu ipekten dalgaya döner — beyanlı dikiş
   Kapı: prompt_kontrol.py "moves at natural speed" imzasını REJİM olarak tanır.
```

```
Gölge sütunu ölçüldü, iddia değil (40°N, öğle ortalı pencere):
                   ekinoks    yaz     kış
   10 dk             3,9°     8,0°    2,6°
   30 dk            11,6°    23,9°    7,7°
    1 saat          23,1°    46,3°   15,3°
    2 saat          45,3°    83,7°   30,4°
    3 saat          65,6°   111,3°   44,9°
    9 saat         150,2°   190,7°  115,9°

⛔ "GÜNEŞ SAATTE 15° GİDER" DEME. 15°/saat SAAT AÇISIDIR, gölge açısı değil.
   Gölgenin dönüş hızı enleme ve mevsime bağlıdır ve öğle civarında yazın
   46°/saate çıkar — yani 15°'in ÜÇ KATI. Bu, DERS 32'nin (gölge süpürmesi
   üç kez üretilmedi) sayısal karşılığıdır ve rapordan gelen 135° yanlıştı.
```

**⛔ REJİM ÇELİŞKİSİ — raporun kendi tablosuna düştüğü tuzak [A6-X2]:**

```
Rapor bir yandan "5400x'te insan tamamen kaybolur" diyor, öte yandan yedi
promptunun yedisinde "motion streak hâlinde işçi ve kamyon" istiyor.
İkisi aynı klipte olamaz. Dahası 180 sn aralıkla çekilen bir karede gündüz
"long exposure streak" fiziksel olarak yoktur.

⭐ KURAL: REJİM C'DE İNSAN İSTENMEZ. C'de iş, YÜZEYLE kanıtlanır (§3).
   İnsan ve makine hareketi isteniyorsa rejim A ya da B seçilir.
   İkisini aynı klipte isteyen prompt ⛔ BLOCK'tur.
```

---

# 2. REJİMİ PROMPTA YAZMAK — TIME RATE bloğu

```
Her görsel ve I2V promptu TEK bir TIME RATE cümlesi taşır [DERS 15 · DERS 18].
Cümle üç şeyi birden bağlar: gök · gölge · yer.

REJİM A   TIME RATE: roughly ten minutes pass across this shot; clouds drift
          in a smooth continuous flow, shadows stay almost where they are,
          and people and machines move fast but stay recognisable.

REJİM B   TIME RATE: about two hours pass across this shot; the shadow of the
          tower sweeps roughly forty degrees across the ground, clouds stretch
          into long streaks, and every moving machine is smeared into a blur.

REJİM C   TIME RATE: a full working day passes across this shot; the tower
          shadow sweeps more than a hundred and twenty degrees across the site,
          the sky goes smooth and featureless, and no person or vehicle stays
          in one place long enough to be seen — only the marks they leave.

⛔ Gölge derecesini uydurma. §1 tablosundan, sahnenin MEVSİMİNE bakarak al.
⛔ Bir filmde üç rejim birden kullanılmaz. En fazla İKİ rejim, ve rejim
   değişimi merdivende gerekçelendirilir (örn. kış sahnesi B, yaz sahnesi C).
```

---

## ⭐ 2.3 GÖLGESİZ SAHNE EN UZUN SAHNE OLAMAZ  [DERS 40]

```
THE DUST YEAR S6: rejim C · 10,0 sn · filmin doruğu · toz fırtınası.
Fizik doğru okunmuştu — fırtına ışığı düzleştirir, gölge kalmaz — ve
taşıyıcı olarak "biriken toz" seçilmişti. Ekranda ne toz birikti ne gölge
süpürdü: ⑦ o klipte 9,0 sn · %100 boş, ④ "the storm is decorative".

NEDEN  DERS 15: model GÖKYÜZÜNÜ hızlandırır, YERİ hızlandırmaz. Gölge, bu
       araçta çalıştığı ölçülmüş TEK taşıyıcıdır — çünkü gökyüzüne aittir.
       "Biriken toz" bir YER olayıdır.
KURAL  Gölge süpürmesi olmayan sahnede:
   ① filmin EN UZUN sahnesi olamaz — en kısa banda iner
   ② taşıyıcı GÖKYÜZÜNDEN ödünç alınır: pus kadraj boyunca YÖN DEĞİŞTİRİR
      ("the haze thickens from the left edge across the frame")
   ③ ekranda SAYILABİLİR bir kayıp olur: "toz birikir" değil,
      "panelin alt sırası kaybolur"
⚠️ Bu kural REJİM C hakkında DEĞİL, GÖLGESİZLİK hakkındadır. Dünya'da
   "one accelerated working day" gölgeyi kaldırmaz, tersine en güçlü
   taşıyıcıdır [ölçüldü: THE NARROW LOT]. Kapı ikisini ayırır.
```

# 3. ⭐ YÜZEY KANITI — insansız "burada iş oldu"

⑦ İŞ merceği insan saymaz, **iş sayar.** Rejim C'de insan olmadığı için
kanıtın tamamı yüzeydedir. Sekiz kanıt vardır; **bir klipte en az İKİSİ** olur.

```
① TEKERLEK VE PALET İZİ   ruts and tracks
   Makine gitse de iz kalır. Saatlerce, günlerce durur. En ucuz ve en güçlü kanıt.
② EKSİLEN İSTİF           depleting stockpile
   Kalıp yığını, palet, donatı bağı klip boyunca AZALIR. Malzeme binaya gitti
   demektir. ⭐ Bu tek başına "büyüme oldu ama kimse yapmadı"yı çözer.
③ ÇAMURUN KURUMASI        wet mud drying to pale dust
   Islak koyu çamur açık gri-kahve tozlu dokuya döner. Rejim B ve C'de görünür.
④ HORTUM VE KABLO GÜZERGÂHI   hoses and cables rerouted
   Zemindeki esnek hatlar gün içinde yol değiştirir. İnce iş aşamalarının kanıtı.
⑤ SÖKÜLMÜŞ KALIP YIĞINI   stripped formwork stacked aside
   Kalıp duvardan indi ve yere istiflendi: iki farklı iş bir arada.
⑥ TOZ VE DUMAN            dust plume · steam off fresh asphalt
   Ancak bir şey hareket ettiyse vardır. Rejim C'de bile kalıcı bir sis olarak durur.
⑦ SAHA AYDINLATMASI       site lighting on, hard pooled shadows
   Gece vardiyası kanıtı. Gölgeler sert ve havuzludur, güneş gölgesinden farklıdır.
⑧ YÜZEY DÖNÜŞÜMÜ          gravel → asphalt · dirt → hydroseed · matte → wet
   Zeminin dokusu değişir. Nesne eklenmeden iş kanıtlanır.

GECE          ⑦ + kaynak kıvılcımı + far izleri
ROBOTİK       lazer hizalama izleri · tekerlek sapma işaretleri · sabit tarama deseni
AY / VAKUM    ⭐ rüzgâr yok: palet izi bozulmadan GÜNLERCE kalır ·
              donanım üstünde koyulaşan ince toz tabakası ·
              iniş tozunun süpürdüğü krater dokusu ·
              regolit torbalarının yatayda büyümesi
              ⛔ Ay'da toz havada asılı kalmaz; parabol çizip düşer.
```

> ⛔ **TOZ VE EGZOZ ÜRETİM KANITI DEĞİLDİR [C1-d].** Yüzey kanıtı, YAPIDA ya da
> MALZEMEDE kalıcı bir değişimdir (iz · eksilen istif · dökülen tabaka). Toz
> bulutu, egzoz dumanı, dönen mikser tamburu hareketin GÖRÜNÜMÜDÜR, işin sonucu
> değil — ⑦ İŞ "THE GROWTH NOBODY MADE" satırı tozdan ikna olmaz. 05_NIHAI_RAPOR'un
> ilk sürümündeki "araçların en az %50'si egzoz/toz izi taşısın" önerisi bu
> gerekçeyle alınmadı.

---

# 4. AŞAMA BAŞINA HAREKET — ACTIVITY cümleleri

> ⭐ Kural: her ACTIVITY cümlesi **en az iki hareket kaynağı** ve **en az bir
> yüzey kanıtı** taşır. Rejime göre seçilir: A/B'de hareket görünür,
> C'de hareket İZ olarak görünür.
> ⛔ Sayı yazma. Rapor "2 ekskavatör, 5 kamyon, 17-22 kişi" verdi ama tek bir
> kaynak göstermedi [A6-X3]. Mertebe yazılır, adet yazılmaz.

> ⭐ **İŞE BAĞLI HAREKET [C1-d · 18.09.2026].** İki hareket kaynağı kuralı KALIR
> ama ölçüsü değişti: sayılan şey hareketin ANA İŞE HİZMETİDİR, hareket eden
> adedi değil. OVER_THE_WALL ölçtü: ⑪ ENVANTER 9,3 (ekipman sahada, hareketli),
> ⑧ YÖNTEM 0,0 (yapıyı o ekipman yapmadı) — "daha fazla araç ekle" yaklaşımının
> neden yetmediğinin en net verisi (QA/QA_CAPRAZ_ANALIZ/02).
> · Ana işi yapan araç DERS 43'ün geçişli fiil + NESNESİNİ alır (§4.5) ve
>   MOTION FOCUS'un taşıyıcısıdır (SAHNE_PLAN_KARTI ②).
> · Yükü tutan vincin BEKLEMESİ doğrudur — yük havadayken vinç PARKED değildir;
>   ⑦ merceği "kancada yük var mı"ya bakar, kola değil.
> · İnsan: az sayıda, ana işi destekleyen görevli. Kalabalık okunurluğu düşürür
>   (PROMPT_SABLONU §5 "kalabalık şantiye"). Kapı: ACTIVITY'de 4'ten fazla farklı
>   hareket eden → INFO "hepsi ana işe bağlı mı?"
> · Finalde şantiye hareketi ARANMAZ → §4.7.

```
KAZI       B  an excavator swings in the lower third while a loader crosses the
              pad twice, both smeared into motion streaks, and the tracked ruts
              they leave stay visible after they pass
           C  no machine is in frame, but fresh crossing track ruts cover the
              whole pad, the excavated pile has grown and changed texture, and
              a low dust haze still hangs over the cut

TEMEL      B  a concrete pump boom sweeps across the trench in blurred arcs
              while mixer trucks pulse in and out of the upper frame, and the
              stacked rebar bundles beside them visibly shrink
           C  the pour is finished and no vehicle remains: half the slab is
              still wet and glossy, the other half has dried matte, and the
              rebar stockpile that stood at the edge is nearly gone

KARKAS     B  the tower crane jib rotates across the upper frame like a blurred
              propeller while a hoist runs up the core leaving a vertical
              streak, and the pile of modular formwork on the ground shrinks
           C  the crane stands still with its sling hanging loaded, the
              formwork pile has moved from the ground to the upper floor, and
              stripped panels are stacked in a new place beside the core

CEPHE      B  mast climber platforms glide up the elevation as continuous
              streaks while a telehandler darts along the ground, and pallets
              of cladding panels disappear from the staging area
           C  the staging area is empty where full pallets stood, the platform
              has moved three floors up the facade, and the protective film on
              the newly hung panels catches the light differently

ÇATI       B  a mobile crane lifts blurred bundles onto the deck while roofers
              streak across the trusses, and the membrane roll unwinds further
              across the exposed ribs
           C  no one is on the roof, the membrane now covers two thirds of the
              deck, the empty roll cores are stacked at the parapet, and the
              roof structure shadow has swept far across the floor below

SAHA       B  an asphalt paver and a roller move in overlapping smeared
              streaks along the perimeter road, and grey steam rises off the
              fresh black strip behind them
           C  the road is finished and empty: the gravel section has turned to
              smooth black asphalt, roller tracks are pressed into its shoulder,
              and the muddy puddle by the gate has dried to pale crust

DEVREYE    A  testing engineers walk between static grey switchgear cabinets
ALMA          while a tool cart is wheeled across the floor, and thick red and
              yellow test cables run in a new route across the slab
           C  the cabinets have not moved at all, but the test cable route
              across the floor has completely changed and the tool cart now
              stands at the far end of the room

AY / ISRU  C  no rover is in frame, yet fresh cleated track ruts cut across the
              regolith in a new direction, a thin dust layer has darkened the
              lander leg, and the stack of filled regolith bags is one course
              higher than before
```

---

## ⭐ 4.5 GEÇİŞLİ FİİL + NESNE — yoksa makine daire çizer  [DERS 43]

```
THE DUST YEAR · ⑦ 1,3/10 PARKED · on klibin SEKİZİ %100 boş ·
④ "Clips 2, 3, 5, 6 and 7 are almost functionally identical: a small rover
driving in circles". Kapı ÖZNE ve FİİL sayıyordu, NESNE saymıyordu.

   ⛔ "A loader rover drives up out of the deepening pit"
      özne var · fiil var · NESNE YOK → geriye yalnız yörünge kalır
   ✅ "A loader rover lifts a filled tube out of the pit and sets it onto
      the fourth course of the berm"

KURAL  Her ACTIVITY cümlesinde en az bir makine, O SAHNEDE BÜYÜYEN ELEMANI
       dilbilgisel NESNE olarak alır. Nesne, aşama merdivenindeki
       ELEMAN · ARA HÂL sütununun adıdır.
   GEÇİŞLİ  lifts · sets · bolts · places · fills · tips · welds · pulls ·
            unrolls · lowers · hauls · stacks · pours · spreads · hoists
   ⛔ TEK BAŞINA YETMEZ  drives · crosses · moves · orbits · circles ·
      travels · runs — bunlar bir ACTIVITY cümlesi KURAMAZ.
⭐ ⑦ ile ⑧ aynı arızanın iki yüzüdür: makine malzemeye dokunmuyorsa eleman
   da büyümüyor demektir ("GROWTH TABLE: NO — none", beş kez).
```

## ⭐ 4.6 İŞ YÜZEYİ ADIYLA VE YÜZDESİYLE — iki "deck" varsa makine hazır olana gider  [DERS 51 · 53]

```
OVER THE WALL · ⑦ WORKING FRONT 3/10 · ⑩ PROXIMITY WITHOUT WORK 2/10 · ⑫ MELTING.
Plan makineyi "onto the deck" yazdı (barajın taze kaldırma yüzeyi); kadrajda
ikinci bir deck vardı — eski taş köprünün tabliyesi. Beş mercek makineleri
köprüde saydı, duvarda çalışma cephesi YOK; köprüde çift giden damperler
birbirinin içinden geçti.

KURAL  ① İş yüzeyi = ELEMAN ADI + KADRAJ YÜZDESİ: "on the top surface of the
          dam lift itself — the fresh dark-grey band at forty-six percent of
          frame height, above and behind the old bridge".
       ② Kadrajda aynı adı alabilecek ikinci yüzey varsa POZİTİF BOŞ yazılır:
          "the stone bridge below stays empty, its roadway bare stone from
          parapet to parapet".
       ③ Dar yüzeyde (köprü · seki · kret yolu · döşek) aynı anda TEK hareketli
          araç; A6-d'nin ikinci hareket edeni BAŞKA yüzeyde ya da PARK hâlinde
          [DERS 53]: "one dump truck at a time crosses the crest road; the
          second stands parked at the east end until the first has left the
          frame, and the roller works on the lift below".
   ⛔ "deck" · "platform" · "the road" tek başına ACTIVITY yüzeyi KURAMAZ.
   ④ YAPININ KENDİ HAREKETİ montaj sahnesinde YAZILMAZ [DERS 56]: THE EMPTY RIDGE'de "the hub
      is turned one third of a turn" → rotor işletme hızında döndü, kanatlar dönen göbeğe
      sıçradı (② 4 · ⑦ · ⑨ · ⑩). Parçaya yazılan hareket fiili, bağlı olduğu yapının korpus
      hareketini çağırır. Montajda: "the hub stays locked and does not turn while any blade
      flange is bare"; dönme · açılma · sarkma · akma yalnız FİNAL sahnesinde.
```

## ⭐ 4.7 FİNAL SAHNESİ İSTİSNASI — ödül yapının çalışmasıdır  [C1-d]

```
FİNALDE sürekli şantiye hareketi ARANMAZ. Filmin ödülü tamamlanmış yapının
ÇALIŞMASIDIR (çark döner · su geçer · kapı kapanır · ışık yanar) — §4.6 ④'ün
"yalnız FİNAL sahnesinde" dediği hareket budur ve REJİM G (§1) bunun için var.
   · İki hareket kaynağı kuralı finalde YAPININ hareketiyle karşılanabilir;
     kapı usta kare için zaten yumuşak (FIX + "kasıtlıysa planda gerekçelendir").
   · Şantiye kalıntısı (vinç · iskele · pad) finalde SÖKÜLMÜŞTÜR [merdiven SÖKÜM
     satırı]; "iş devam ediyor" görünümü vaadi yalanlar (F09 · ④ TESLİM).
   · Çalışan sonucu ANLAMAYA fırsat verecek süre: tutuş kuralı KILAVUZ_REHBERI
     §8 adım 9 [P2-i]; kusursuz döngü aranmaz → KURGU_VE_TESLIM §7.
KALDIRDIĞI: finalde "hâlâ çalışan şantiye" ile ölçek göstermek. Karşılığı,
            kapak/başlık vaadinin filmde gerçekleşmiş olmasıdır.
```

# 5. KAPI — bu kılavuz nerede zorlanır

```
① PLANDA        Aşama merdivenine ⭐ REJİM sütunu eklenir (A · B · C).
                ⛔ Sütun boşsa merdiven kabul edilmez.
                ⛔ Bir filmde ikiden fazla farklı rejim varsa gerekçe yazılır.

② PROMPTTA      ⛔ prompt_kontrol.py:
                   · TIME RATE bloğunda rejim penceresi ("ten minutes" /
                     "two hours" / "working day") yoksa → BLOCK
                   · Rejim C beyanı ile aynı promptta görünür insan/araç
                     cümlesi varsa → BLOCK  [DERS 33 · A6-X2]
                   · ACTIVITY cümlesinde iki hareket kaynağı + bir yüzey
                     kanıtı yoksa → FIX
                   · Gölge derecesi yazılmışsa §1 tablosunun ±%25 bandı
                     dışındaysa → FIX

③ ÜRETİM        Üretim günlüğü §3 satırına "rejim" ve "yüzey kanıtı ✓/✗"
   GÜNLÜĞÜNDE   sütunları eklenir.

④ QA'DA         ⑦ İŞ merceği "en uzun işsiz aralık" ölçer. §3'teki sekiz
                kanıttan hiçbiri o aralıkta yoksa PARKED gelir — ve artık
                hangi kanıtın eksik olduğu adlandırılabilir.
```

> ⭐ **KALDIRDIĞI:** rejim kuralı "her klipte bol bol işçi ve kamyon olsun"
> serbestliğini kaldırır. Rejim C seçilen bir sahnede artık insan istenemez.
> Bedeli: kalabalık, canlı şantiye görüntüsü yalnız A ve B rejiminde mümkün.
> Karşılığı: gökyüzü ile yerin aynı saate tabi olması — ve ⑦'nin insan
> olmadan da geçebilmesi.
