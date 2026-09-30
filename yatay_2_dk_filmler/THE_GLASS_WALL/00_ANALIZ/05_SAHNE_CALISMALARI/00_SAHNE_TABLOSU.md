# 🧮 THE_GLASS_WALL — SAHNE TABLOSU (sahne başına BİR satır · 12 satır + usta kare)

> Sahne başına ayrı çalışma dosyası yazılmaz (kardeş depo ölçtü: 25 sahne × 120 satır → 747 KB,
> üretim 0 kare); **bu tablo** yazılır. Satırları betik damgalar (`| S00 |` …); elle satır
> eklenmez/silinmez. Her hücre TEK satır, boş hücre yok ("—" yazılır). Bir satırın KAPI'sı ✅
> olmadan o sahnenin promptu yazılmaz.
>
> ⛔ Burada `## 🎬 SAHNE <n>` başlığı ve 📸/🎥 prompt başlığı YAZILMAZ. Prompt yalnız bölüm dosyasında.

## Sütunlar

| sütun | ne yazılır | kaynak |
|---|---|---|
| **S** | sahne no (betik damgalar) · son satır G12 usta kare | `03_SAHNE_SIRALAMASI` |
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
| S00 | AÇAR · arazi temizliği + sarnıç kazısı %100 | The hillside is wild scrubland: maquis, dry grass, loose stones. A mechanical arm is cutting back shrub growth along the upper terrace line; a trench for the cistern is open at the right, its spoil mounded beside it. | kazıcı kol SAHAya girdi (sağ alt · makineden) · maki yığınları sol kenarda | B · 09:00 · 105°/45° | kazıcı kol döner + el arabası ilerler / toprak sıyrılmış şerit yüzey kanıtı | zeytin ağacı sol %x8–15 ≈180 px · kayalık sağ %x82–90 ≈200 px · deniz ufuku %50 | kaldırma yok | DERS 3 (açılış iş başlıyor) · DERS 35 (metin yok) · U-1 | maki yığınları sol kenarda · S0 sonu sarnıç kapalı değil açık | ✅ |
| S01 | ÖRER · alt teras duvarı %25 (ilk 2–3 sıra) | At the lower edge of the site a dry-stone retaining wall has risen three courses high over about twelve metres; the stone rubble pile beside it is still large. Workers carry single stones along the line. | el arabası devam · taş yığını (istif· sağ alt) | B · 10:00 · 115°/50° | iki taş taşıyıcı + el arabası ilerler / toprak sıyrılmış teras yüzeyi | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 | kaldırma yok | DERS 48 (taş kaynağı yığında görünür) · U-7 | taş yığınından · teras %25→%50 | ✅ |
| S02 | ÖRER · alt + üst teras duvarı %75 (iki bant görünür) | Two retaining terraces are now visible: the lower wall stands at full height over its full run, the upper wall is three-quarters complete with its rubble supply nearly exhausted. The levelled terrace surface is bare brown soil. | el arabası çıktı · taş yığını neredeyse bitti | B · 11:00 · 125°/55° | iki taşçı devam + taş yığını eksilme yüzey kanıtı | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 | kaldırma yok | DERS 36 (sadece bu sahnede ayakta olan) · U-8 (ters inşa) | yığından · teras %75→%100 ikinci teras | ✅ |
| S03 | DÖKER · çiftlik evi temeli + taş duvar %50 (2 sıra) | The upper terrace holds the farmhouse footprint: two courses of rough stone wall enclose the ground floor on three sides; the fourth side is open. A concrete mixer sits on the lower terrace; the cistern lid is set in the ground. | beton mikser KALDI (alt teras · kamyondan) · kiremit paleti görünmüyor henüz | B · 10:30 · 118°/52° | beton mikser döner + iki duvarci / ıslak harç yüzey kanıtı | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 | kaldırma yok | DERS 19 (ev 8×6 m sayi) · U-7 | mikserden · ev duvarı %50→%75 | ✅ |
| S04 | ÖRTER · çiftlik evi çatısı tam + sera zemin %0→%100 | The farmhouse now has a full terracotta-tiled roof; its four stone walls stand complete. On the lower terrace beside it, a fresh concrete strip — the greenhouse floor slab — has just been poured and is still dark and wet. | beton mikser çıktı · cam paleti henüz YOK | B · 09:30 · 107°/47° | tiler çatıda + betoncu sera zeminde / ıslak beton şeridi yüzey kanıtı | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 · kiremit çatı taban %56,6 | kaldırma yok | DERS 1 (çatı geçici değil kalıcı) · DERS 48 | kemer paleti yok henüz · ev %100 tamamlandı | ✅ |
| S05 | DİKER · sera çelik çerçeve %50 (6/12 kemer) | Six dark-green painted steel arched frames stand on the concrete slab; the other six anchor bolts wait in a row. A temporary wind-protection frame of steel tube and clips encloses the right side of the structure. Workers tighten bolts at the base of each arch. | iskele KALDI (sağdan) · cam paleti henüz yok | B · 10:00 · 115°/50° | iki montajcı cıvata + çelik kemer dikilme / beton zemin taze-mat yüzey kanıtı | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 | kaldırma yok (elle kurulum) | DERS 55 (yalnız tek sera) · U-1 | kemer paletten · çerçeve %50→%75 | ✅ |
| S06 | DİKER+KAPER · çerçeve %100 + cam panel %12 (8/64) | All twelve dark-green steel arched frames stand complete across the full 24-metre span. Eight glass panels have been set into the south-facing lower run; their edges show the metal glazing bar clearly. The temporary scaffold still stands. On the right terrace edge, a flat pallet of glass panels lies horizontal. | cam paleti KALDI (sağ kenara · kamyondan) | B · 11:00 · 125°/55° | vakum lifter çalışır + cam taşıyıcı yürür / cam kenar sızdırmazlık bandı yüzey kanıtı | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 · 8 panel kadrajda | vakum lifter tutuşu visible, panel palete yaslanmış kalkıyor | DERS 57 (panel pop yok) · DERS 55 · U-2 | palet sağ kenarda · çerçeve %100 + panel %12 | ✅ |
| S07 | KAPER · cam panel %62 (40/64) | Forty of the sixty-four glass panels have been glazed in; the dark-green steel frames are partly hidden behind the installed glass. Workers on the scaffold are sliding a new panel onto the glazing bars. The scaffold is still fully in place. The pallet on the right edge is about half emptied. | iskele devam · palet yarı azaldı | B · 10:30 · 118°/52° | vakum lifter + panel taşıyıcı / cam kenar lastikten sızdırmazlık bant izi | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 · 40 panel görünür | vakum lifter panel yüzeyinde, taut suction cups | DERS 57 · DERS 4 (cam yansıma değil saydam) | yarı palet → panel %62 | ✅ |
| S08 | TAMAMLAR+SÖKÜM · cam panel %100 (64/64) + iskele kalktı | All sixty-four glass panels are in place; the greenhouse is now fully glazed. The temporary scaffold has been removed — its steel tubes lie stacked on the lower terrace ready for collection. The glass pallet on the right is empty. | iskele ÇIKTI (tüm borular alt terasta yığılmış) · boş palet görünür | B · 09:00 · 103°/43° | söküm ekibi boru taşır + yağmur damlaları cama düşüyor / ıslak beton zemin yüzey kanıtı | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 · tüm panel dolu | kaldırma yok (söküm) | DERS 1 (iskele DEĞİŞMEZLER'de değil) · U-5 SÖKÜM | boruları söküm alanına · panel %100 + iskele YOK | ✅ |
| S09 | DONATIR · iç raf + dış tarhlar | Inside the greenhouse, growing benches and a drip-irrigation header pipe run along the length of the space; green plants are not yet visible. On the outside terraces, timber edging boards mark out six vegetable bed outlines in fresh dark soil. | raf monte ekibi iç · tarh çizici dış | B · 10:00 · 115°/50° | iç ekip raf yerleştirir + dış ekip tarh çizer / tarh kenarları taze toprak | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 | kaldırma yok | DERS 33 (işçi bulanık iz olarak) · U-6 | raflar iç · tarh çerçeveleri dış | ✅ |
| S10 | EKİN+BAĞLAR · ilk fidanlar + oluk + sarnıç | Young seedlings stand in rows on the growing benches inside the greenhouse; their cotyledons are just visible through the glass. The farmhouse roof gutter has been connected to the downpipe leading into the buried cistern. A drip-tape reel lies at the bed edge. | damlama hortumu rulosu · oluk aparatı | A · 16:00 · 228°/28° | fidancı sera içi + bağlantı ustası çatıda / taze toprak tarhları yüzey kanıtı | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 | kaldırma yok | DERS 36 (sadece bu karedeki durum) | damlama rulosundan · fidanlar ekili | ✅ |
| S11 | TESLİM · USTA KARE G12 | The greenhouse is full of green leafy plants in organised rows; a wooden harvest crate sits on the stone path in front of the entrance. Smoke rises from the farmhouse chimney. The path from the terrace to the door is paved with flat stones. The sea horizon is level and still. | — | A · 17:00 · 242°/20° | — / taş döşeli patika yüzey kanıtı | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 | kaldırma yok | DERS 4 (kapak kartı ayrı 5,0 s) · U-9 | — · teslim tam | ✅ |
| G12 ⭐ | USTA KARE | Sera içi yeşil dolu · hasat kasası seranın önünde · evin bacasından duman · taş döşeli patika · zeytin ağacı sol · kayalık sağ · deniz ufuku tam %50 | söküm: hepsi gitti | A · 17:00 · 242°/20° | — | zeytin ağacı sol %x8–15 · kayalık sağ · deniz ufuku %50 | — | DERS 5 (G12 önce üretilir) | — | ✅ |

