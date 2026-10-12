# 🧮 THE_SKY_CANAL — SAHNE TABLOSU (sahne başına BİR satır · 20 satır + usta kare)

> ✅ 11.10.2026 dolduruldu (TUR 1 · 20 sahne) · BEŞ SORU 20/20 · promptlar `bolum_uretici.py`'den (bu tablo onun kaynağıdır)

> Sahne başına ayrı çalışma dosyası yazılmaz (kardeş depo ölçtü: 25 sahne × 120 satır → 747 KB,
> üretim 0 kare); **bu tablo** yazılır. Satırları betik damgalar (`| S00 |` …); elle satır
> eklenmez/silinmez. Her hücre TEK satır, boş hücre yok ("—" yazılır). Bir satırın KAPI'sı ✅
> olmadan o sahnenin promptu yazılmaz.
>
> ⛔ Burada `## 🎬 SAHNE <n>` başlığı ve 📸/🎥 prompt başlığı YAZILMAZ. Prompt yalnız bölüm dosyasında.

## Sütunlar

| sütun | ne yazılır | kaynak |
|---|---|---|
| **S** | sahne no (betik damgalar) · son satır G20 usta kare | `03_SAHNE_SIRALAMASI` |
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
| S00 | OTURTUR · sol parça asılı → yatakta %100 | "The left span section … already hangs level on four taut slings from the left crane a metre above its bearings" | giren: kalas kamyonu / çıkan: — | A · 08:20 · 123°/16° | sol vinç lowers the left span section + ekip guides it with taglines / tyre ruts, timber blocking stacks | çam 72 px x 1475–1547 · ayaklar 844 / 1182 | parça kancada dört taut sapan · hedefin 1 m üstünde (DERS 57) | DERS 3 · 8 · 57 · U-1 | asılı (G0) · sol açıklık oturdu ✅ | ✅ |
| S01 | YERLEŞTİRİR · sağ parça pedden → sağ açıklık %100 | "The right span section lies on timber blocking on the right work pad, four slings rising taut from it to the hook of the second crane" | giren: — / çıkan: kalaslar istife (sağ ped) | A · 08:30 · 125°/17° | sağ vinç lifts the right span section + ekip stacks the freed blocking / ruts, blocking pile | çam 72 px · sağ istif 1491–1687 | sağ parça dört sapan · kısa yol · sol bom DIŞ → sonda merkez parçaya bağlanır | DERS 8 · 57 · U-1 · U-3 | sağ pedde · sağ açıklık oturdu ✅ | ✅ |
| S02 | BİRLEŞTİRİR · merkez parça kalastan DİMDİK → yatakta %100 · ⭐ kıyılar birleşir | "the long centre span section lies on timber cribbing on the gravel flats far below … four long slings rising taut from it to a steel spreader beam" | giren: kiriş kamyonları (sonda) / çıkan: kalaslar nehir kıyısında yığın | A · 08:40 · 127°/19° | sol vinç lifts the centre span section + ekip pulls the freed timbers / timber pile beside the river | çam 72 px · merkez kalasta 839–1152 · nehir 1002 | dört uzun sapan + yayıcı kiriş · yalnız düşey · sağ bom DIŞ | DERS 8 · 57 · U-2 | vadi tabanında · boşluk kapandı ✅ | ✅ |
| S03 | BAĞLAR · enine kirişler %0 → %100 iki uçtan | "two deep steel girders in light grey primer run side by side over both piers, open between them" + "with a bundle of steel cross beams on the hook on taut slings" | giren: kiriş kamyonları · panel kamyonları (sonda) / çıkan: kalaslar küçük kamyonla | B · 08:50 · 129°/20° | iki vinç lift the bundles + ekip sets the beams / stacks of beams, rust stains | çam 72 px · köprü hattı 538–1398 | demetler iki sapanla kancada | DERS 37 · 51 · U-6 | kamyonlarda · ızgara ✅ | ✅ |
| S04 | KAPATIR · taban panelleri %0 → %100 | "tied together by evenly spaced steel cross beams, the river still showing far below between them" | giren: panel paletleri / çıkan: boş kamyonlar | A · 10:50 · 160°/32° | iki vinç lift the pallets + ekip lays the panels / pallets, scuffed patches | çam 72 px · nehir aralıkları | paletler dört sapanla kancada | DERS 61 · U-6 | paletlerde · kuru taban ✅ | ✅ |
| S05 | YÜKSELTİR · uzak duvar %0 → %100 | "carrying one continuous flat steel floor in light grey primer, open to the sky" + "with a tall steel wall panel on the hook" | giren: duvar paneli kamyonları / çıkan: boş kamyonlar | A · 11:00 · 162°/32° | iki vinç lift the tall steel wall panels + ekip bolts them upright / boot prints, offcuts | çam 72 px · uzak duvar tepesi 587 | panel iki sapanla kancada | DERS 51 · 61 | kamyonlarda · uzak duvar ✅ | ✅ |
| S06 | TAMAMLAR · yakın duvar %0 → %100 · U oluk | "with a tall steel wall along its far edge" | giren: uç parçası kamyonları (sonda) / çıkan: boş kamyonlar | A · 11:10 · 165°/33° | iki vinç lift the tall steel wall panels + ekip bolts them / boot prints, pallets | çam 72 px · yakın duvar tepesi 609 | panel iki sapanla kancada | DERS 51 · U-7 | kamyonlarda · U oluk ✅ | ✅ |
| S07 | BAĞLAR · uç parçaları → kapak çerçeveleri %100 · kapaklar kapalı | "at each end a short open joint still separates it from the gate frame on the abutment" | giren: varil kamyonu (sonda) / çıkan: boş kamyonlar · sağ bom DIŞ | A · 11:20 · 168°/33° | iki vinç lower the end sections + ekip carries seal strips from a pallet / offcuts, dust | çam 72 px · çerçeveler 529 / 1383 | uç parçası dört sapanla kancada | DERS 61 · U-8 | kamyonlarda · uçlar bağlı ✅ | ✅ |
| S08 | KAPLAR · iç gri → açık mavi %0 → %100 soldan · KURU | "inside it the floor and walls are bare grey primer, dry" + "with a pallet of coating drums on the hook" | giren: varil paletleri · bakım yolu kamyonları (sonda) / çıkan: boş kamyon | B · 11:30 · 171°/34° | ekip sprays the pale lining + sol vinç lowers the pallets of drums / overspray streaks, drums on pallets | çam 72 px · mavi bant 587–609 | palet dört sapanla · sağ bom DIŞ | DERS 54 · U-3 · U-9 | varillerde · ⭐ mavi bant ✅ | ✅ |
| S09 | KURAR · bakım yolu + uç basamakları %0 → %100 | "lined inside from end to end with a dry matte pale blue lining" + "with a walkway section on the hook on taut slings" | giren: korkuluk kamyonları (sonda) / çıkan: boş kamyonlar | A · 13:30 · 206°/31° | iki vinç lift the galvanised walkway sections + ekip bolts them / dust film, pallets | çam 72 px · korkuluk hattı 607 | parça dört sapanla kancada | DERS 33 · 61 | kamyonlarda · bakım yolu ✅ | ✅ |
| S10 | ÇEVİRİR · korkuluk %0 → %100 | "a galvanised walkway on brackets runs along its near wall, with steel access steps at each end" | giren: varil kamyonu (sonda) / çıkan: boş kamyonlar · sağ bom DIŞ | A · 13:40 · 209°/30° | iki vinç lift the bundles of railing modules + ekip bolts the modules / galvanised sheen, offcuts | çam 72 px · korkuluk hattı 607 | demet iki sapanla kancada | DERS 52 (G10 bölüm sınırı) | kamyonlarda · korkuluk ✅ | ✅ |
| S11 | BOYAR · dış astar → kömür grisi %0 → %100 soldan | "and a railing along its outer edge" + "with a pallet of coating drums on the hook" | giren: boş kamyonlar / çıkan: — | B · 13:50 · 211°/29° | ekip sprays the dark top coat + sol vinç lowers pallets of drums / overspray streaks | çam 72 px · köprü 538–1398 rengi | palet dört sapanla · sağ bom DIŞ | DERS 37 · U-10 | varillerde · kömür grisi ✅ | ✅ |
| S12 | TOPLAR · paletler + iki vinç ÇIKAR · saha boşalır | "deep charcoal grey outside" + "with a bundle of empty pallets on the hook on taut slings" + "stacks of empty pallets and spare slings" | giren: — / çıkan: iki vinç · paletler · kamyonlar | A · 15:50 · 239°/14° | iki vinç lift the last empty pallets + ekip rakes the pads / raked gravel, tyre tracks | çam 72 px · vinçler 413 / 1605 → 0 | demet dört sapanla · bomlar inerken kanca boş (beyanlı, P7-e) | DERS 8 · 48 · U-10 | pedlerde · saha boş ✅ | ✅ |
| S13 | AKITIR · ⭐ ilk su: borudan → sol ayağa (onda bir) | "its inside dry from end to end … Two people stand at the valve wheel of the filling pipe" | giren: servis aracı / çıkan: — | A · 16:00 · 241°/13° | ekip turns the valve wheel + ekip sets a crate of tools / raked gravel, dust | çam 72 px · su cephesi 538 → 844 | asılı yük YOK · boru çerçeveye cıvatalı | DERS 54 · 61 · U-4 | boruda (G0'dan) · sığ su sol yarı ✅ | ✅ |
| S14 | İLERLETİR · su cephesi sol ayaktan → sağ kapağa (onda bir) | "shallow clear water about a tenth of the wall height deep covers its floor from the left gate to about the left pier" | giren: — / çıkan: — | A · 16:10 · 243°/11° | boru fills the trough + ekip walks beside the edge + servis aracı / dry matte band ahead | çam 72 px · su cephesi 844 → 1398 | — | DERS 52 · 54 · U-4 · U-11 | sol yarıda · bütün boy ✅ | ✅ |
| S15 | DOLDURUR · onda bir → dörtte üç · kıyılarla eşit · vana kapanır | "shallow clear water about a tenth of the wall height deep covers its floor from the left gate to the right gate" | giren: — / çıkan: — | A · 16:20 · 245°/10° | boru fills the trough + ekip checks the water line / sheen of sky, dust film | çam 72 px · su çizgisi 591 | — | DERS 52 · U-4 · U-11 | sığ · dörtte üç ✅ | ✅ |
| S16 | AÇAR · iki kapak kalkar %100 · geçiş açık | "calm clear water stands in it at three quarters of the wall height, level with the canal arms" + "both steel gates stand closed" | giren: — / çıkan: servis aracı | A · 16:30 · 247°/8° | ekip lifts the steel gate + ekip carries crates / dust film, raked gravel | çam 72 px · çerçeveler 529 / 1383 | kapaklar çerçevede vinç kablosunda · çerçeve cıvatalı | DERS 56 · U-12 | çerçevede · yukarıda ✅ | ✅ |
| S17 | GİRER · tekne havuzdan → köprüye, burnu sol ayakta | "both steel gates are raised high … One small red canal boat … its mooring line cast off" | giren: — / çıkan: — | Y · 16:40 · 249°/7° | dümenci + ekip pulls the mooring line + servis aracı / thin wake | çam 72 px · tekne 161–381 → 620–796 | tekne suda, ağırlığı suda | U-5 · U-13 · U-14 | havuzda · köprüde ✅ | ✅ |
| S18 | GEÇER · ⭐ DORUK: tekne → merkez açıklık | "moves along the middle of the trough, its hull low in the water, its bow near the left pier" | giren: — / çıkan: — | Y · 16:41 · 249°/7° | dümenci swings the tiller + ekip walks + servis aracı / thin wake | çam 72 px · tekne 974–1121 · nehir 1002 | tekne suda | U-5 · U-13 | sol ayakta · merkezde ✅ | ✅ |
| S19 | VARIR · tekne → sağ kapak, durur · TUTUŞ (4–8 sn) | "moves along the middle of the trough over the centre span, its hull low in the water" | giren: — / çıkan: servis aracı | Y · 16:42 · 250°/6° | dümenci swings the tiller + ekip stops beside it + servis aracı / fading wake | çam 72 px · tekne 1242–1368 | tekne suda · son 4 sn tutuş | U-5 · U-15 | merkezde · sağ uçta ✅ | ✅ |
| G20 ⭐ | USTA KARE | "The same small red canal boat … lies still on the water at the right end of the trough, its bow at the open right gate" | söküm: hepsi gitti (vinçler, kamyonlar, paletler, kalaslar) | Y · 16:43 · 250°/6° | — (tutuş) / raked gravel, faint tyre tracks | çam 72 px x 1475–1547 · tekne 1242–1368 | tekne suda | P1-h · U-15 | — | ✅ |
