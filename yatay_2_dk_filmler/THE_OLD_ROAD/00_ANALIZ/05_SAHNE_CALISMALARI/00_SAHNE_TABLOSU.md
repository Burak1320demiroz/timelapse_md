# 🧮 THE_OLD_ROAD — SAHNE TABLOSU (sahne başına BİR satır · 15 satır + usta kare)

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
| **KAPI** | ⬜ → ✅ satır tam, yüzdeler PLAN ile aynı, kesir cümlesi px'i var | — |

Doldurulmuş satır nasıl görünür (örnek; gerçek satırlar aşağıda betik damgalıdır):

```
S02 · KURAR · bom %100, segment 1 %100 · "the lattice boom stands raised …, the first tower section
stands upright on the foundation on a short sling, its top flange bare" · vinç bomu KALKTI (pad'de
yatıktan) / segment 2 rafta · B · 10:00 · 108°/48° · crawler crane swings … + assist crane holds … /
crushed-stone ruts · meşe 64 px x≈742 · duvar sol %28 · segment sapanda, bom başında · DERS 57 · U-3 · ✅
```

---

## 📋 TABLO

| S | AŞAMA FİİLİ · ELEMAN % | AT THIS STAGE (İng.) | GEÇİCİ EKİPMAN giren/çıkan | REJİM · SAAT · AZ/EL | İKİ HAREKET EDEN + YÜZEY KANITI | KANIT NESNESİ · ÇAPALAR | KALDIRMA / FİZİK | KİLİT / UYARI | KAPI |
|:--:|---|---|---|---|---|---|---|---|:--:|
| S00 | AÇAR · YENİ GÜZERGÂH 0 → ilk kesi (%2) | nothing of the new crossing exists; first 20 m earth bench cut | dozer girer / — | A · 05:05 · 75° / −5° | dozer pushes a bench + drops spoil / dust band | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | kaldırma yok | DERS 3 · 33 · U-1 | ✅ |
| S01 | KAZAR · YAKLAŞIM + TEMELLER 0 → %100 · geçici geçiş kurulur | bench a few hundred metres, matching cut opposite | low-loader + ekskavatör girer / — | B · 05:15 · 98° / 18° | dozer drops a windrow + low-loader sets the excavator / dust | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | kaldırma yok | DERS 1 · 25 | ✅ |
| S02 | YÜKSELİR · AYAKLAR %0 → %100 + başlıklar | approaches and five shored pier pits, haul road + culvert crossing | kazık makinesi, mikser, pompa girer / — | A · 07:15 · 99° / 20° | rig bores a pile + excavator pours a lift / mud band | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | kaldırma yok · donatı kafesi yerde | DERS 48 · 51 | ✅ |
| S03 | KURAR · DÖKÜM ALANI 0 → %100 · ilk kesit + çelik burun | five piers at full height with heads, climbing rings under them | tırmanır kalıp / kalıplar S2 sonunda iner | B · 07:25 · 127° / 39° | pump lifts a fresh lift + crew strike the ring / dust band | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | pompa hattı — kaldırma yok | DERS 37 · 19 | ✅ |
| S04 | İTER · TABLİYE %0 → %14 (A1 → P1) | casting shed, launching bed, first segment, steel nose past abutment | hangar + burun + mobil vinç girer / — | A · 09:25 · 129° / 41° | crane lifts a rebar cage + truck fills the formwork / slurry patch | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | mobil vinç: kanca YÜKLÜ ve düşey | DERS 8 · 22 · 48 | ✅ |
| S05 | EKLER · TABLİYE %14 → %32 (P1 → P2) | deck on pier 1, nose over span 2 | — / — | A · 09:35 · 131° / 42° | jacks push the deck + truck fills the formwork / dust | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | ⛔ tabliye İTİLİR, kaldırılmaz | DERS 57 · 43 | ✅ |
| S06 | UZANIR · TABLİYE %32 → %50 (P2 → P3) · geçici destek kurulur | deck on pier 2 → pier 3; trestle built; snow line down | geçici destek girer / — | B · 09:45 · 172° / 52° | jacks push the deck + crane bolts the trestle diagonals + shed joins a segment / steel lines | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | paletli vinç: kanca YÜKLÜ | DERS 7 · 57 | ✅ |
| S07 | ZORLAR · TABLİYE %50 → %63 (P3 → P4) · su yükselirken itme sürer | deck on pier 4; rock berm around pad and pier feet; river rising | kaya bermi girer / plant yüksek alana | B · 11:45 · 219° / 46° | jacks push twice + trucks tip rock onto the berm / wet band | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | kanca YÜKLÜ (berm) | DERS 54 · 43 | ✅ |
| S08 | TAŞAR · HAT KOPAR — geçici geçiş ve berm gider | flood peak; crossing torn out; berm overtopped; deck static | — / geçici geçiş GİDER | A · 13:45 · 222° / 45° | flood drops a raft of branches + excavator tips rock into the scour / foam lines | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | kaldırma yok | DERS 54 · 33 | ✅ |
| S09 | ONARIR · HAT YENİDEN KURULUR · döküm alanı iki kesit biriktirir | water down; line rebuilt; two segments waiting in the shed | menfez + çapraz + apron GERİ / sürüntü bankaya | B · 13:55 · 252° / 27° | excavator stacks timber + truck tips gravel + mixer fills the formwork / silt line | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | kaldırma yok | DERS 48 · 21 | ✅ |
| S10 | SÜRER · TABLİYE %63 → %76 (P4 → P5) · burun KARŞI KENARA DEĞER | deck on pier 5; ⭐ nose shoe on the far abutment shelf | — / bekleyen kesitler kuyruğa eklendi | A · 15:55 · 254° / 25° | jacks push twice + truck carries panels away + crew pack the nose / dust | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | ⛔ itme — kaldırma yok | DERS 57 · 43 | ✅ |
| S11 | KAVUŞUR · TABLİYE %76 → %100 — beton hat tamam | unbroken concrete line abutment to abutment | — / kriko takımı sökülür | A · 16:05 · 256° / 23° | jacks push the deck + crew set the packing at the front face / steel lines | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | ⛔ itme — kaldırma yok | DERS 57 · 45 | ✅ |
| S12 | SÖKER · BURUN + DESTEK + HANGAR → 0 · kalıcı mesnetler | nose, trestle and casting shed all coming down | — / burun + destek + hangar ÇIKAR | B · 16:15 · 278° / 2° | crane lifts a nose panel + crawler lowers a trestle section + crew set the bearings / rake marks | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | iki vinç: kanca YÜKLÜ | DERS 48 · 53 | ✅ |
| S13 | DÖŞER · ÜST YAPI %0 → %100 · şantiye toplanır | deck alone on permanent bearings; finishing materials laid out | membran/korkuluk/direk girer / hangar GİTTİ | A · 18:15 · 279° / 1° | low-loader carries sections + telehandler sets a bundle on the deck / rake marks | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | telehandler: çatal altında yük | DERS 48 · 49 | ✅ |
| S14 | AKAR · TRAFİK ESKİ YOL → YENİ YOL | surfacing, barriers, lit columns; yard gone; hairpins still busy | — / hangar + şantiye yolu ÇIKAR | A · 18:25 · 281° / −1° | truck carries a barrier section + crew lift barriers / dust over the scar | taş köprü %34,2 (64 px) · şapel %28,1 · kaya kulesi %89,7 | kaldırma yok | DERS 45 · 33 | ✅ |
| G15 ⭐ | USTA KARE | crossing open and lit; hairpins empty but readable | — / hepsi gitti | A · 18:35 · 281° / −1° | traffic streams across the deck + trails fade on the hairpins / haul-road scar | taş köprü %34,2 (64 px) · kıvrımlar %30–70 | kaldırma yok | DERS 30 · 45 | ✅ |
