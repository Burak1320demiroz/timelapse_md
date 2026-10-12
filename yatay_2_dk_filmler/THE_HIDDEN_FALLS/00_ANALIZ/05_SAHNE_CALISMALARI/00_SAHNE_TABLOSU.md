# 🧮 THE_HIDDEN_FALLS — SAHNE TABLOSU (sahne başına BİR satır · 15 satır + usta kare)

> ✅ 08.10.2026 dolduruldu · BEŞ SORU 15/15 · promptlar `bolum_uretici.py`'den (bu tablo onun kaynağıdır) · 🪟 = salon istasyonu

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
| S00 | KALDIRIR · platform dipte → kamyonda %100 | "a rusty steel loading hopper … hangs from the hook of a yellow crawler crane … murky green-brown water about three metres deep" | vinç + kamyon + ekskavatör giriş terasında (nakliye yolundan) / platform kamyona | A · 06:30 · 82°/15° | vinç swings the hopper + ekskavatör scrapes rubble / rubble heaps · tyre tracks | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · su sütunda 872 | platform kancada dört sapanla · G1'de kamyon kasasında gevşek sapan | DERS 3 · 8 · 57 · U-1 | dip basamağında · platform dipte → kamyonda ✅ | ✅ |
| S01 | BOŞALTIR · su +3 → taban · basamaklar %100 | "two diesel pumps stand on the middle bench … fat black hoses laid into the water" | 2 pompa + hortum (orta basamak) / platformlu kamyon nakliye yolundan çıkar | B · 06:40 · 84°/17° | pumps pull the murky water + truck carries the hopper / scum line · silt | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · su 872 → kuru 949 | — (asılı yük yok; kanca G1 başında boşalır) | DERS 16 · P10-e · U-2 | havzada su · su → birikinti ✅ | ✅ |
| S02 | DÖKER · temel 0 → %100 · ayak 0 → 1 | "stakes with orange tape mark a long rectangle along the foot of the far wall … rebar cages on the hook" | ekskavatör · damperli · beton pompa kamyonu · kalıp giriyor | B · 08:40 · 104°/40° | crane swings the rebar cages + pump boom pours / formwork · ruts · silt patches | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 | donatı demeti kancada iki sapanla | DERS 48 · 1 · U-3 | vinçte demet · temel 0 → %100 ✅ | ✅ |
| S03 | DİKER · iskelet 0 → %100 · sağ uç çift yükseklik | "a long raised concrete base … stands finished … a bundle of dark grey steel members on its hook" | 2 uzun kamyon (çelik) giriyor / kalıp kerestesi kamyona | A · 10:40 · 137°/61° | crane lifts the steel members + crew bolts / formwork stack shrinks | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · iskelet 619 → 507 | çelik demet kancada · kolonlar ankraj civatalarında | DERS 61 · 36 · U-4 | kamyonlarda · iskelet %0 → %100 ✅ | ✅ |
| S04 | YERLEŞTİRİR · köprü 0 → 2 açıklık | "a stack of two finished steel footbridge spans … a lifting beam already shackled to the top one" | açıklık istifi terasta / istif biter | A · 10:50 · 141°/62° | crane lifts the first span + 4 kılavuz ip / timber bearers | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · köprü 306–742 · 615 | kaldırma kirişi dört sapanla · açıklık karede OTURUR (G5) | DERS 57 · 22 · U-5 | terasta istif · köprü 0 → 2 ✅ | ✅ |
| S05 | KAPLAR · teras %0 → %100 · çatı + dudak | "stacks of pale timber decking boards and bundles of dark grey roof panels wait on the raised base" | tahta + panel istifleri / istifler biter | B · 11:00 · 146°/63° | crew lifts the pale boards + roof crew lays panels / stacks shrink · sawdust | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 | tahta paleti kancada dört sapanla | DERS 37 · 48 · U-6 | temelde istif · teras soldan sağa ✅ | ✅ |
| S06 | CAMLAR · cam 0 → 15 bölme (önce salon) | "two trucks loaded with tall crates of glass panes … the first tall pane on a vacuum lifting frame" | 2 kamyon (sandık) + vakum çerçevesi / kamyonlar gider | A · 13:00 · 214°/64° | crane lifts the tall glass panes + glaziers set / crates empty | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · I2V hedefi G8 | cam vakum çerçevesinde kancada | DERS 61 · 16 · U-7 | sandıklarda · cam %0 → %100 ✅ | ✅ |
| S07 | 🪟 DÖŞER · salon boş → masa + 12 sandalye + oturma | "the salon is glazed and floored but empty … a pile of wrapped furniture … by the side door" | — (salon: sarılı yığın kapıda) | A · 13:10 · 219°/62° (∥ S8) | two workers carry + set the table top / wrapping heap · shoe prints | sütun camdan 1347–1457 · cam kadrajın %32'sinden yukarı | — (asılı yük yok) | DERS 10 · 52 · U-8 | kapıdaki yığında · salon boş → döşeli ✅ | ✅ |
| S08 | YOLLAR · kanal %0 → %100 · boru · vinç gider | "a crew has begun a narrow concrete channel along the bench edge … first sections of a dark steel pipe" | ip ekibi giriyor / VİNÇ nakliye yolundan çıkar | A · 13:10 · 219°/62° | rope crew bolts the pipe + crane lifts the last sections / pipe bundle | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · kanal 379 · boru x ≈1321 | boru demeti kancada iki sapanla · boru kayaya kelepçeli | DERS 61 · 1 · U-9 | vinçte demet · kanal yarım → tam ✅ | ✅ |
| S09 | DİKER ② · bahçe 0 → 3 sıra · 3 zeytin | "pallets of young shrubs, three small olive trees with wrapped root balls and bags of soil wait on it" | bitki paletleri + küçük kamyon / paletler biter | B · 13:20 · 223°/61° | crews carry the shrubs + small excavator lifts the first olive tree / soil · pallets | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 | — (zeytin kök topuyla, ekskavatör kovasında) | DERS 37 · 48 · U-10 | terasta palet · basamaklar gri → yeşil ✅ | ✅ |
| S10 | DOLDURUR · su taban → +7 (%100) · platform kuru | "two large hoses come down the haul road from the rim and end at the edge of the entrance terrace" | 2 hortum + kenarda pompa kamyonu / hortumlar römorka | B · 15:20 · 256°/40° | water pours from the hoses + workers pull the two hoses / tyre tracks | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · su sütunda dipten → 770 | — (hortum uçları ağırlıkla terasa oturur) | P10-e · P16-c · U-11 | hortumlarda · kuru → +7 turkuaz ✅ | ✅ |
| S11 | AKAR · şelale kuru → perde → su (%100 · G) | "the channel is still dry and the rock face below the notch is bare and dry" | — (pompa evinde bir işçi · üst basamakta iki) | G · 17:20 · 276°/17° | worker pulls the valve lever + water runs / wet streak on rock | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · perde 1213–1347 · 502 → 660 | — (su kanaldan çentiğe, kayadan çatıya, dudaktan suya) | A27 · DERS 15 · U-12 | kanalda (pompa evinden) · kuru → perde ✅ | ✅ |
| S12 | YANAR · ışıklar tek karede · 3 kişi köprü ucu | "the waterfall runs … the lights of the building are all still off" | araba + küçük kamyon (son aletler) / gider | B · 17:20 · 276°/17° | crew lifts the last tools onto a cart + truck drives / fresh tyre tracks | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · yansıma 703–808 · I2V hedefi G14 | — | DERS 45 · ISIK_FINALI §3 · U-13 | pompa evinde aletler · sönük → yanık ✅ | ✅ |
| S13 | 🪟 IŞIR · perde akar · masa hazır · bir kişi | "one person sits in the right armchair with a book, back to the camera … a thin curtain of falling water" | YOK | G · 19:20 (−8 sn) · 294°/−6° | curtain falls + person turns a page / droplet band on panes | sütun camdan 1347–1457 · perde x 106–1173 | lambalar tavandan birer kabloyla | DERS 33 · 52 · U-14 | — (sakin an, malzeme yok) · perde kıvrımı ✅ | ✅ |
| S14 | DURULUR · üç kişi 5 m · tutuş | "three people have just stepped onto the right end of the footbridge … no readable faces" | YOK | G · 19:20 · 294°/−6° | three people walk + stop / foam band · wet stain | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · kişiler 688 → 619 · 25 px | — | DERS 45 · P2-i · U-15 | köprü ucunda · yürüyüş → tutuş ✅ | ✅ |
| G15 ⭐ | USTA KARE | "everything is finished. all the lights are on … three people stand still at the footbridge railing" | söküm: hepsi gitti (vinç · pompa · hortum · kamyon) | G · 19:20 +8 sn · 294°/−6° | — (tutuş) / foam band · reflections | sütun 922–1050 · çam ≈155 · kulübe 1741–1818 · perde 1213–1347 · salon 1130–1339 | — | P1-h · DERS 45 | — | ✅ |
