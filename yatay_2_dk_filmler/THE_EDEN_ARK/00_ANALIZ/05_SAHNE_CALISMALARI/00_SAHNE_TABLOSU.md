# 🧮 THE_EDEN_ARK — SAHNE TABLOSU (sahne başına BİR satır · 18 satır + usta kare)

> Sahne başına ayrı çalışma dosyası yazılmaz (kardeş depo ölçtü: 25 sahne × 120 satır → 747 KB,
> üretim 0 kare); **bu tablo** yazılır. Satırları betik damgalar (`| S00 |` …); elle satır
> eklenmez/silinmez. Her hücre TEK satır, boş hücre yok ("—" yazılır). Bir satırın KAPI'sı ✅
> olmadan o sahnenin promptu yazılmaz.
>
> ⛔ Burada `## 🎬 SAHNE <n>` başlığı ve 📸/🎥 prompt başlığı YAZILMAZ. Prompt yalnız bölüm dosyasında.

## Sütunlar

| sütun | ne yazılır | kaynak |
|---|---|---|
| **S** | sahne no (betik damgalar) · son satır G18 usta kare | `03_SAHNE_SIRALAMASI` |
| **AŞAMA FİİLİ · ELEMAN %** | `AÇAR · yol %60` — fiil + eleman + ara hâl yüzdesi; ara hâl silueti değiştiriyor mu | `INSAAT_YONTEMI` §2-§3 · DERS 37 |
| **AT THIS STAGE (İng.)** | kameranın GÖRDÜĞÜ kadarı, POZİTİF, geçici destek kelimesiyle (sling · formwork · scaffold · rebar · roller …); "there is no X" YASAK | `INSAAT_YONTEMI` §5 · DERS 33 · 35 · 36 |
| **GEÇİCİ EKİPMAN giren/çıkan** | bu karede kadraja giren ya da çıkan geçici şey + nereden geldi / nereye gitti | DERS 1 · 48 |
| **REJİM · SAAT · AZ/EL** | `B · 10:00 · 108°/48°` — TIME RATE ve LIGHTING satırlarının kaynağı | `SANTIYE_HAREKETI` §1-§2 · `ZAMAN_VE_ISIK` §2 |
| **İKİ HAREKET EDEN + YÜZEY KANITI** | makine + fiil + NESNE × 2 · bir yüzey izi (ruts · spoil · dust band …) | DERS 43 · A6-d · `SANTIYE_HAREKETI` §3 |
| **KANIT NESNESİ · ÇAPALAR** | kanıt nesnesi px + konum; sol/sağ çapa yüzdesi — her karede aynı | DERS 25 · PLAN §DEĞİŞMEZLER |
| **KALDIRMA / FİZİK** | asılı yük var mı → neye bağlı; kaldırma karede bitiyor mu (G(n) yük hedefin üstünde) | DERS 8 · 22 · 46 · 57 · `FIZIK_VE_AGIRLIK` §5 |
| **KİLİT / UYARI** | bu sahneye düşen DERS n + `04_UYARI_NOTLARI` satır no; en çok 3 | `01_QA_DERS_HASADI` |
| **BEŞ SORU ①/④** | `istiften · yol %40→%60` — ① malzeme başlangıçta nerede (G(n)'de görünür) · ④ klip sonunda ne değişti (G(n+1) farkı); ②③⑤ komşu sütunlarda; beşi tamsa ✅ | `SAHNE_PLAN_KARTI` §1-§2 · C1-a |
| **KAPI** | ⬜ → ✅ satır tam, yüzdeler PLAN ile aynı, kesir cümlesi px'i var | — |

Doldurulmuş satır nasıl görünür (örnek; gerçek satırlar aşağıda betik damgalıdır):

```
S02 · KURAR · bom %100, segment 1 %100 · "the lattice boom stands raised …, the first tower section
stands upright on the foundation on a short sling, its top flange bare" · vinç bomu KALKTI (pad'de
yatıktan) / segment 2 rafta · B · 10:00 · 108°/48° · crawler crane swings … + assist crane holds … /
crushed-stone ruts · meşe 64 px x≈742 · duvar sol %28 · segment sapanda, bom başında · DERS 57 · U-3 · pad istifinden · segment 1 %100→2 %100 ✅ · ✅
```

---

## 📋 TABLO

| S | AŞAMA FİİLİ · ELEMAN % | AT THIS STAGE (İng.) | GEÇİCİ EKİPMAN giren/çıkan | REJİM · SAAT · AZ/EL | İKİ HAREKET EDEN + YÜZEY KANITI | KANIT NESNESİ · ÇAPALAR | KALDIRMA / FİZİK | KİLİT / UYARI | BEŞ SORU ①/④ | KAPI |
|:--:|---|---|---|---|---|---|---|---|---|:--:|
| S00 | AÇAR · ambar 0 → 3 açık | "three long hatches shut under rusted steel covers" | iskele kuleleri · rampa · fidanlık · toprak yığını (G0'dan) | A · 06:00 · 73°/16° | deck winch pulls the cover · workers lift locking bars / dust haze | baca x 100 253 px · havuz kenarı · fener | kapak rayda, zincirle — asılı yok | DERS 3 · 22 · U-6 | kapaklar ambar üstünde · 3 ambar açık | ✅ |
| S01 | SÖKER · kapak + 2 direk → hurda | "three hatches stand open … covers rolled aside" | + 4 hurda konteyneri · telehandler | B · 06:10 · 75°/18° | torches slice the cover · telehandler drops pieces / spark + rust dust | aynı | konteyner rıhtımda · direk güverteye kaynaklı | DERS 48 · 47 | kapak/direk güvertede · güverte çıplak | ✅ |
| S02 | YAMAR · delik → levha | "ragged dark hole … welding screen" | kaynak perdesi | A · 08:10 · 95°/39° | welder cuts the plate · telehandler lifts a new plate / sparks | yama x 908 47 px | levha telehandler çatalında | DERS 49 | telehandler çatalında · gri astar yama | ✅ |
| S03 | SOYAR·BOYAR · pas %100 → 0 | "grey primer patch … dust sheets for blasting" | raspa düzeneği · hortumlar · toz örtüsü | B · 08:20 · 97°/41° | blasters spray grit · pump drives hoses / red grit dust band | renk sınırı x 172 → 1249 | hortum kenarda — asılı yok | DERS 47 | raspa düzeneğinde · lacivert/gri/beyaz | ✅ |
| S04 | DONATIR · çerçeve %100 · vinç gelir | "repainted … bundles of grey steel planting frames" | + kamyonlu vinç · treyler | A · 10:20 · 129°/60° | telehandler lifts a bundle · mobile unit drives in / tyre tracks | demet 6 → 0 | demet kerestede | DERS 51 · 43 | rıhtımda demet · çerçeve ambarda, vinç ayakta | ✅ |
| S05 | DOLDURUR · toprak %100 · incir askıya | "truck-mounted mobile crane … with a strapped root ball on the hook" | konveyör (G5'te açık) | B · 10:30 · 133°/62° | conveyor carries soil · worker pulls the strap / soil dust | yığın x 461 → 0 | ⭐ kaldırma S5 6,5–8,0 sn · G6'da asılı biter | DERS 57 · 22 · U-1 · U-2 | rıhtım yığını · incir asılı, treyler boş | ✅ |
| S06 | İNDİRİR · incir askıdan toprağa | "the crane carries a visible load … half a metre above the middle hatch" | vinç · sapan | A · 12:30 · 198°/67° | crane lowers the fig · workers steady with tag ropes / leaf flutter | incir tepesi 620 · x 806 | kanca → kısa sapan → kök topu; kablo bom başına | DERS 57 · 22 | askıda · dikili, gergi telli | ✅ |
| S07 | YEŞERTİR · yeşil ambar 1 → 3 | "with a slack guiding sling on the hook" | vinç, treyler, konveyör ÇIKAR | B · 12:40 · 204°/67° | telehandler lifts a palm · worker unties the sling / leaf debris | fidanlık 5 → 0 | sapan gevşek, kancada | DERS 48 · 49 · U-4 | fidanlık · üç ambar yeşil | ✅ |
| S08 | SULAR · ilk sulama | "all three holds are green … sprinkler pipes" | + kemer ve cam istifi (kıç ucu) | A · 14:40 · 250°/51° | workers set the sprinkler heads · telehandler carries pots / wet patches | yeşil bant 560 px | boru mezarnaya kelepçeli | — | boru mezarnada · ıslak taçlar | ✅ |
| S09 | KURAR · portal + kemer 1 | "the gardens are watered … parts of a steel gantry portal" | portal parçaları | A · 14:50 · 252°/49° | workers carry the portal legs · telehandler lifts a beam / wet footprints | kemer 1 x ≈ 1067 | kemer konsol braketine cıvatalı | DERS 57 · P23-a | istifte · portal + kemer 1 | ✅ |
| S10 | ÖRTER · kemer 1 → 18 | "first white steel arch … bare and unglazed" | portal · telehandler | B · 15:00 · 254°/48° | portal hoists the arch · telehandler carries a crate / steel dust | ⭐ baş kenar x 1067 → 470 | portal raylarda | DERS 49 · U-5 | istif · %90 kubbe | ✅ |
| S11 | KAPATIR · kemer 20 · cam %100 | "eighteen white steel arches … last two bays open" | portal | A · 17:00 · 277°/27° | portal lifts the arch · workers set a glass panel / reflections | son panel x 416 | kemer braketlerde | DERS 49 | portalda · kubbe tam | ✅ |
| S12 | DÖŞER · teras + lamba | "glass vault is complete … glass-cleaning gantry" | — | A · 17:10 · 279°/25° | workers bolt the railing · worker pulls a lamp line / dust stains | korkuluk baş kasarada | korkuluk kenara cıvatalı | — | güvertede · korkuluk + lamba hattı | ✅ |
| S13 | ARINDIRIR · iskele 6 → 0 | "railing … strings of small lamps … scaffold towers still stand" | iskele ve rampa ÇIKAR | A · 17:20 · 280°/23° | workers roll the scaffold tower · telehandler pulls the ramp / wheel tracks | iskele 6 → 0 | iskele tekerlekte | DERS 48 | bordada · borda serbest | ✅ |
| S14 | YÜZER · havuz −7,0 → 0 | "free of its scaffolding … still rests on its keel blocks" | — | B · 17:30 · 282°/22° | workers pull the sluice levers · pump draws a hose / wet stains | ⭐ borda bandı 38 → 48 px | mooring halatları babalara | DERS 56 · U-4 | limanda · gemi yüzüyor | ✅ |
| S15 | AÇILIR · kapı + römorkör | "the dock is full and the ship floats" | römorkör (havza) | A · 19:30 · 302°/2° | workers turn the gate winches · tug moves in / haze | kapı kanatları | halat babaya · kapı yuvasında | P24-e | kapalı kapı · açık kapı, römorkör bağlı | ✅ |
| S16 | ÇEKER · 0 → +60 m · ışık | "gates are open and the tug is fast" | — | A · 19:40 · 304°/1° | workers lift the mooring ropes · tug pulls the towline / rope pile | baş x 172 → 846 | çekme halatı kıç babalarına | U-5 | havuzda · yarı dışarıda, ışık yanık | ✅ |
| S17 | SÜZÜLÜR · +60 → +150 m | "ship is leaving the dock … lamps lit warm" | — | A · 19:50 · 305°/−1° | tug pulls the ship · workers pull the rope aboard / wake | ⭐ baş x 846 → 1328 | çekme halatı | DERS 45 | kapı eşiğinde · kapı dışında | ✅ |
| G18 ⭐ | USTA KARE | "back on the water … just beyond the open dock gates" | söküm: hepsi gitti · portal KALICI · römorkör bağlı | A (S17) · 20:00 · 307°/−2° | tug pulls the ship · worker pays out the towline / wake + haze | baca x 100 · gemi x 1328 → 1657 | çekme halatı | DERS 45 · 30 | — | ✅ |
