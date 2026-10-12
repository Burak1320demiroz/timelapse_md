# 🧮 THE_BURIED_KHAN — SAHNE TABLOSU (sahne başına BİR satır · 15 satır + usta kare)

> ✅ 09.10.2026 dolduruldu · BEŞ SORU 15/15 · promptlar `bolum_uretici.py`'den (bu tablo onun kaynağıdır)

> Sahne başına ayrı çalışma dosyası yazılmaz (kardeş depo ölçtü: 25 sahne × 120 satır → 747 KB,
> üretim 0 kare); **bu tablo** yazılır. Satırları betik damgalar (`| S00 |` …); elle satır
> eklenmez/silinmez. Her hücre TEK satır, boş hücre yok ("—" yazılır). Bir satırın KAPI'sı ✅
> olmadan o sahnenin promptu yazılmaz.
>
> ⛔ Burada `## 🎬 SAHNE <n>` başlığı ve 📸/🎥 prompt başlığı YAZILMAZ. Prompt yalnız bölüm dosyasında.

## Sütunlar

| sütun | ne yazılır | kaynak |
|---|---|---|
| **S** | sahne no (betik damgalar) · son satır G15 usta kare | `03_SAHNE_SIRALAMASI` |
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
| S00 | KAZAR · kumul sırtı +12 · üç uç · istif 0 → 1 | "a long smooth dune of pale gold sand … only three weathered stone tips stand out of its crest … a flatbed truck loaded with pale cut stone blocks" | ekskavatör (sırtta) + damperli + düz kasalı kamyon / 2. ekskavatör sağdan girer, damperli sağdan çıkar | A · 06:00 · 73°/10° | excavator tips the load into the dumper + crew unloads the stone blocks / tyre tracks · footprints · sand plume | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · çerçeve ucu 845–1075 · 368–425 | — (asılı yük yok; kova kumda) | DERS 3 · 49 · U-1 | kumul sırtında · çerçeve ucu açılır, istif 0 → 1 ✅ | ✅ |
| S01 | SIYIRIR · kum +12 → +9 · çerçeve %40 · set %20 | "round the top of the gateway frame a shallow pit has been dug, its raw cut faces stepped in small benches … a long conveyor belt has just been set up" | konveyör kurulur / kamyon sırası sağdan çıkar · düz kasalı kamyon gider | B · 06:10 · 74°/12° | excavators tip the sand into dumpers + conveyor drops the sand onto the heap / ruts · tracks · film of dust | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · kum sırtı 425 → 483 | — | DERS 49 · 61 · U-2 | kumul + konveyör · sırt 425 → 483, set %20 ✅ | ✅ |
| S02 | AÇAR · kum +9 → +5 · galeri soldan sağa · gedik belirir | "the straight top of the long wall shows along the whole front, sand still packed against it up to the brim, its raw cut face stepped in benches" | konveyör · kamyon sırası (sürer) | B · 08:10 · 87°/38° | excavators tip the sand into dumpers + crew clears each arch / bucket scrapes · gravel | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · kum 483 → 559 | — | DERS 37 · 51 · U-2 | duvar hizasında kum · galeri 12/16 + gedik ✅ | ✅ |
| S03 | ORTAYA ÇIKARIR · kum +5 → zemin · cephe tam boy · gedik + yığın | "the open arcade of round arches … broken right of the gateway by a wide gap … below it the lower storey is still buried" | konveyör · kamyon sırası (sürer) | B · 10:10 · 106°/63° | excavators tip the sand into dumpers + crew digs round the fallen blocks / pale scars · sand in joints | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · cephe 387–1533 · gedik 1189–1380 · 578 | — | DERS 37 · 61 · U-2 · U-8 | kemer tabanında kum · cephe tam boy + yığın ✅ | ✅ |
| S04 | TEMİZLER · avlu %0 → %100 · kapı ağzı boş · set %100 + çit | "a ramp of sand still slopes … over the buried forecourt, its raw cut face stepped in benches … bundles of dry palm fronds lie at the foot of the berm" | çit demetleri / 2 ekskavatör + damperli sağdan çıkar · konveyör katlanır | A · 12:10 · 193°/80° | excavators tip the sand into dumpers + crew lifts the palm fronds / paving through a film of sand | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · avlu 655–703 · set 1533 → sağ kenar | — | DERS 48 · 53 · U-2 | rampa + demetler · avlu açık, çit dikili ✅ | ✅ |
| S05 | KALDIRIR · iskele 0 → %100 · yığın → sıralar · vinç girer | "a flatbed truck loaded with steel scaffold tubes and boards stands on the forecourt left of the breach" | iskele kamyonu (solda gider) / mobil vinç sağdan girer | A · 12:20 · 205°/79° | crew lifts the scaffold tubes + second crew levers the fallen blocks / pale scars · bundles | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · gedik 1189–1380 | vinç G5'te YOK — klip içinde girer (U-6) | DERS 8 · 35 · U-6 · U-9 | kamyonda borular, yığında bloklar · iskele + sıralar ✅ | ✅ |
| S06 | ÖRER · gedik +4 → üzengi · ayaklar | "a small mobile crane stands on its outriggers … with a salvaged block slung on the hook" | — (vinç, iskele, sıralar, istif sahada) / sıralar biter | B · 12:30 · 216°/78° | crane lifts the salvaged blocks + masons bed them / mortar stains · stone dust | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · gedik dibi 578 → 559 | blok kancada iki sapanla · vinç ayaklarda | DERS 8 · 57 · 61 · U-10 · U-11 | sıralar + istif · duvar üzengide, ayaklar ✅ | ✅ |
| S07 | KAPATIR · 4 kemer · duvar +9 · kalıp sökülür | "four curved timber arch frames stand ready on the scaffold boards … a pallet of wedge-shaped arch stones on its hook" | kalıplar / kalıplar avluya indirilir | A · 14:30 · 262°/55° | crane lifts the arch stones + masons set the frames / fresh mortar · footprints | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · galeri 16/16 · 483 | palet kancada dört sapanla | DERS 49 · 61 · U-10 | palette kemer taşı · 4 kemer kapalı ✅ | ✅ |
| S08 | ASAR · kanat 0 → 2 · kapı kapalı · vinç gider | "a heavy dark timber door leaf slung upright on its hook, and the second leaf lies flat on timber bearers" | — / VİNÇ bomunu katlar, sağdan çıkar | A · 14:40 · 264°/53° | crane swings the first door leaf + crew guides it with taglines / mortar stains | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · kapı 912–1008 | kanat kancada iki sapanla, dik | DERS 8 · 46 · 57 | avluda kanatlar · kapı kapalı, vinç yok ✅ | ✅ |
| S09 | DİRENİR · rüzgâr · çitte kum · avlu süpürülür | "the doors close the pointed arch … the air is still" | el arabaları / — | B · 14:50 · 265°/50° | crew sweeps the drift sand + tips the barrows onto the heap / drift sand · broom streaks | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · masa dağı pusta soluk | — | P10-e · U-12 | çit boş · çitte kum, avlu temiz ✅ | ✅ |
| S10 | ASAR ② · fener 0 → 16 · oyma kuşak | "two wooden crates of iron lanterns and two tall ladders … a third tall ladder leans on the gateway frame" | fener sandıkları + merdivenler / sandıklar gider | A · 16:50 · 280°/25° | workers lift the iron lanterns + worker on the ladder brushes the band / dust · broom streaks | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 | fener demir kancada (vinç yok) | DERS 49 · U-13 | sandıkta fenerler · 16 fener asılı ✅ | ✅ |
| S11 | SÖKER · iskele → 0 · konveyör · istif → 0 | "a flatbed truck and a small tractor stand on the forecourt in front of the right part of the front" | — / iskele + istif kamyonla solda, konveyör traktörle sağda gider | A · 17:00 · 281°/22° | crew stacks the tubes on the truck + tractor tows the conveyor / drift sand | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 | — | DERS 1 · 48 · 61 | iskele + konveyör · saha boş ✅ | ✅ |
| S12 | BATAR · altın ışık → mavi saat · eklenen yok | "the site is clear; two workers with wide brooms and a hand cart stand at the right end of the forecourt" | el arabası / iki işçi gider | B · 17:10 · 282°/20° | crew sweeps the drift sand + tips the cart onto the heap / broom streaks · wind ripples | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 | — | DERS 33 · 40 · U-15 | ince kum · avlu temiz, güneş batar ✅ | ✅ |
| S13 | YAKAR · fener 0 → 16 yanık | "a lamplighter with a long pole stands under the first arch … a last ladder leans on the wall beside the gateway" | son merdiven + küçük araba / gider | A · 19:10 · 296°/−4° | lamplighter lights the lanterns + workers lift the last ladder onto a cart / broom streaks | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 | fener demir kancada | A28-b · DERS 45 · U-14 | sönük fenerler · 16 yanık ✅ | ✅ |
| S14 | AÇILIR · kapılar içe · ışık taşar · üç kişi · tutuş | "the doors are still closed. Three people pushing a loaded two-wheeled hand cart walk across the forecourt … no readable faces" | YOK | G · 19:20 · 297°/−6° | three people pull the loaded hand cart + doors swing / broom streaks · drift sand | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · kapı 912–1008 · kişiler 830 → 910 · ≈30 px | kanatlar demir pivotlarda | DERS 45 · 57 · P2-i · U-5 | kapalı kapı · açık kapı + eşikte üç kişi → tutuş ✅ | ✅ |
| G15 ⭐ | USTA KARE | "everything is finished … the two heavy timber doors stand open inward … three people stand still on the threshold" | söküm: hepsi gitti (ekskavatör · kamyon · konveyör · vinç · iskele · istif · merdiven) | G · 19:20 +8 sn · 297°/−6° | — (tutuş) / warm light on paving · drift sand | akasya 154–259 · masa dağı 1660–1840 · ufuk 540 · kapı 912–1008 · kişiler ≈910 | — | P1-h · DERS 45 | — | ✅ |
