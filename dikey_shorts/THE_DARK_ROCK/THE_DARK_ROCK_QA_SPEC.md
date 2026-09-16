# 🔍 THE DARK ROCK — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM · ⑥ GEÇİŞ · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER).
> ⛔ ① KARE · ③ ZAMAN · ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET · ⑫ KATILIK merceklerine **VERİLMEZ** — o altısı
> dokümansız koşar [AGENTS değişmez ⑦]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit,
> kilit değildir; tariftir.

---

## 0. KÜNYE

```
FİLM          THE DARK ROCK — açık deniz kayasında granit fener, güneydeki komşu sütundan
FORMAT        9:16 dikey · 1080×1920 · 30 fps

TESLİM YAPISI ⭐ SAHNE BLOĞU  6 sahne × 8,0 sn = 48,0 sn                  ← merceklerin konusu
              ⭐ KAPAK KARTI  1 × 5,0 sn        =  5,0 sn                  ← SAHNE DEĞİL
                 TOPLAM                           53,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR ve devamlılık karşılaştırmalarına GİRMEZ.
                 Ayrı denetlenir: "kart, S5'in sonundaki fenerin AYNISINI mı gösteriyor?"

SAHNE SAATLERİ  S0 0,0–8,0 · S1 8,0–16,0 · S2 16,0–24,0 · S3 24,0–32,0
                S4 32,0–40,0 · S5 40,0–48,0
                KART 48,0–53,0
                (120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · her kesme ölçü başında)
⛔ DÜZ IZGARA   proje sahibinin kilidi (15.09.2026). ⑥ METRONOM hükmü BEKLENEN ve KABUL EDİLMİŞ
                risktir (plan §AŞAMA MERDİVENİ · DERS 24); hüküm gelirse "beklenen" diye kaydedilir,
                yeniden üretim sebebi sayılmaz. Ritim isteniyorsa SÜRE sütunu değişir, prompt değil.
                (Karşı kanıt notu planda: üç film varyanslı kurguyla RHYTHM aldı — DERS 44 🔻.)
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]:
   ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
   ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — her sahne 8,0 sn teslim → en büyük kutu ≥ 9,0 gerekir;
   {4,6,8} çıkarsa ARAÇ değişir ya da karar proje sahibine döner — ARA KARE YOK, her sahne tek klip.

YAPI          açık deniz kaya feneri · boyasız granit gövde 30 sıra · galeri · çelik fener odası · bakır külah · +48 m
SAHA          kıyı / açık deniz kayalığı — tek kaya + tek deniz sütunu (NEEDLE) + deniz ufku + uzak burun (SAHA_VE_IKLIM §3.3)
ZAMAN YAYI    ~6 ay (Mart başı → Eylül başı) · film mertebe anlatır: "yaklaşık yarım yıl / bir çalışma sezonu" [P1-c]
IŞIK          TEK GÜN 07:00 → 19:00 (6 klip × rejim B 2 saat = 12 saat) · takvim tarladan + deniz renginden · bilinçli sıkıştırma
KAMERA        MAIN STATION — tek istasyon, 6 sahne + usta kare · h +21,0 m · D_eksen 56 m · 0° · tilt 0°
VİNÇ          ⛔ YOK — tek düşey taşıyıcı raylı asansör kabini (rack-and-pinion); kadrajda vinç görülürse DAVETSİZDİR
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G6 usta kare → G5 → G4 → G3 → … → G0 · her kare zincir_kontrol.sh
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S5
SANİYE      0:47,0   (S5'in 7,0. saniyesi — son 2,0 sn'lik TUTUŞUN içi [P2-i]; ışık yanık ve SABİT)
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① YANAN FENER CAMI: kadraj ekseninde %73–77, sabit sıcak beyaz; ışık camın İÇİNDE (huzme · koni · denizde
      ışık yolu YOK); bakır külah ve rüzgârgülü ucu %82.
   ② TAM GRANİT KULE: boyasız açık gri, yatay derz çizgili, iskele YOK, asansör direği YOK; batı (sol) yüzü
      altın, doğu (sağ) yüzü mavi gölgede.
   ③ KESİLMİŞ KAİDE + BOŞ APRON + RAMPA: kaide düz (%34,5), iki çentikli tepe YOK; apron boş, direk tabanının
      açık renkli izi; turuncu rampa yuvasında; yükleyici ve gemi YOK.
   + NEEDLE aynı yerde aynı boyda · deniz koyu arduvaz, ipeksi · güneş 19:00 (az 290°, +1°), aydınlık [DERS 45].

KOMUT
   ffmpeg -ss 47.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ışık YANMIYORSA, ışık camın dışına taşıyorsa, iskele/direk/yükleyici/gemi kadrajdaysa, kaidede tepe
   varsa ya da NEEDLE boyu/konumu G0'dan sapmışsa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — AÇILIŞ–KAPANIŞ KAFİYESİ (LOOP DEĞİL)
   ffmpeg -ss 0.3  -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 47.0 -i teslim.mp4 -frames:v 1 kanit_g6.jpg
   İki karede: NEEDLE (x ≈ 761–832 · y %34–45 · ≈200 px), deniz ufku (%50), uzak burnun sırtı (sol, %53),
   kayanın alt gövdesi + yosun bandı tam aynı yerde. Taç G0'da çentikli (%39), G6'da düz kaide (%34,5) — BEDEL.
   Işık aynı DEĞİLDİR (07:00 sağdan → 19:00 soldan, bilinçli — plan LOOP satırı).
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=+21 · D=56 · tilt 0 · yüzde = 50 + 66,7·(y−21)/D, ALT kenardan)

| Ne | Beklenen (kare yüksekliği) | Tol. | Hangi karelerde |
|---|---|---|---|
| deniz ufku = GÖZ ÇİZGİSİ | %50,0 (kulenin sağında düz) | ±%0,5 | G0–G6 (hepsi) |
| uzak burun sırtı | %52,9 · x 0–430 px · düz | ±%1,0 | G0–G6 |
| NEEDLE (deniz → tepe) | %34,4–44,8 · x ≈ 761–832 px · ≈200 px boy · ≈71 px en | ±%0,5 · ±10 px | G0–G6 (hepsi — ⛔ boy sabit) |
| kayanın ön ayağı (deniz) | %18,2 | ±%1,5 | G0–G6 |
| doğal taç tepeleri | %39,3 (iki tepe, çentik) | ±%1,0 | yalnız G0 |
| kaide (kesilmiş taç) | %34,5 · düz | ±%1,0 | G1–G6 |
| apron + rampa başı | %30,0 · x ≈ 146–343 px (apron) · rampa ≈ 213 px | ±%1,0 · ±15 px | G1–G6 |
| gövde tepesi sıra 12 | %48,8 (NEEDLE tepesinin ÜSTÜNDE, ufkun ALTINDA) | ±%1,0 | G2 |
| galeri korkuluğu | %72,0 · gövde tepesi %70,2 | ±%1,0 | G3–G6 |
| asansör direği tepesi | G2 %52,4 · G3–G5 %73,8 · x ≈ 369 px | ±%1,5 | G2–G5 (G6'da YOK) |
| kabin (sandıkla) | %52 | ±%3 | G4 |
| iskele tepesi | G2 %50,6 · G3–G4 galerinin üstü · G5 %65,5 | ±%1,5 | G2–G5 (G6'da YOK) |
| fener camı | %72,6–77,4 · x ≈ 489–591 px | ±%1,0 | G5 (karanlık) · G6 (yanık) |
| rüzgârgülü ucu = TAÇ | %82,2 | ±%1,0 | G5–G6 |
| gövde genişliği | taban 403–677 px · tepe 471–609 px | ±15 px | G2–G6 |

```
⛔ ÜST SINIR   hiçbir yapı parçası %87,5'in üstünde olamaz (rüzgârgülü %82,2 — 5,3 puan pay; UI üst 254 px = %86,8)
⛔ ALT SINIR   ilerlemeyi kanıtlayan hiçbir şey %25'in altında olamaz (apron %30) — alt bant (%0–25) yalnız deniz,
               köpük ve gemi gövdesidir; S3 ortasında rampanın AYAĞI %22'ye iner, BAŞI %30'da kanıttır
⛔ SAĞ ŞERİT   kanıt nesnesi x > 838 px'e (sağ UI) giremez — NEEDLE x ≤ 832 ✓; x > 945 (sağ 1/8) yalnız deniz ve gök
⛔ D_kenar     kadrajın alt kenarı kameradan 28 m'de denize iner; 28–56 m arası deniz UI bandıdır
⭐ PİKSEL      NEEDLE, ufuk ve uzak burun USTA KARE onaylanınca ölçülür, buraya ve plana yazılır [PERSPEKTIF §4];
               yukarıdaki sayılar formül tahminidir.
⚠️ S2 tek klipte 18 sıra + galeri (%48,8 → %72) — filmin en yoğun klibi; ① merceği bu klipte NEEDLE BOYUNU ölçer:
   kule büyürken sütun küçülmüş ya da kaymış mı?
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
fener          açık deniz kaya feneri · TEK kule · boyasız açık gri granit · beyaz boya ve renkli bant YOK
kaide          kayanın çentikli tacı (+12 m, iki tepe) kesilir → düz kaide +8,0 m · kademeli kenar · yarım delgi izleri
gövde          30 sıra × 1,0 m = +8 → +38 m · taban çapı 12 m → tepe 6 m · konik · kırlangıç kuyruklu blok (görünmez)
galeri         konsol korniş + döşeme +38 → +39,5 · siyah çelik korkuluk
fener odası    siyah çelik çerçeve · 12 dik kayıt · 12 cam pano · +40 → +44 · çap 4,5 m
külah          yeni bakır, dilimli · havalandırma topu · rüzgârgülü ucu +48 m
lamba          S5 son çeyrekte yanar · SABİT sıcak beyaz · optik dönmez görünür (900×) · ışık camın içinde
apron          kayaya oyulmuş +6,0 m · kulenin batısı (sol) · ~8 × 7 m
basamaklar     +1 → +6 m · apronun önünde · ilk seki +3 (G0'da doğal)
rampa          turuncu boyalı çelik · 10 × 2,5 m · menteşeli · zincirle kayaya bağlı · yuvası apron kenarında · KALICI
asansör        galvaniz rack-and-pinion direk · x −7,5 m · sarı kapalı kabin · G2 +23 · G3–G5 +41 · S5'te tepeden söküm
iskele         galvaniz boru halka iskele · ahşap döşeme · gövdeye bağlı · S4 son 2 sn → S5 ilk 2 sn TEPEDEN söküm
makineler      S0: paletli kompakt ekskavatör + hidrolik kırıcı (tek) · S1–S5: kompakt paletli yükleyici + palet çatalı (tek)
               ⛔ apronda aynı anda TEK makine [DERS 53] — ekskavatör S1 başında gemiye iner, SONRA yükleyici çıkar
gemi           küçük gri çıkarma gemisi · menteşeli baş rampası · ⛔ YAZI YOK · her gelişte ve gidişte SOL KENARDAN
kamera         h +21,0 m · D_eksen 56 m · D_kenar 28 m · 0° · tilt 0° · roll 0° · 24 mm tam kare dikey
NEEDLE         tek deniz sütunu · kameradan 90 m · eksenin 18 m doğusu · 14 m boy · 5 m en · tepede guano izi
güneş          48°K · δ +14° (ağustos ortası geometrisi) · 07:00 92°/20° → 19:00 290°/1°
```

### Kule yüksekliği ve saha durumu — kare kare (② İNŞA · ④ TESLİM · ⑩ SEBEP için)

| G | taç / gövde | galeri · fener | iskele · direk | iniş hattı | apron | gözle görülmesi gereken ilerleme |
|:-:|---|---|---|---|---|---|
| G0 | iki çentikli tepe (%39) | — | — | doğal seki · gemi + oluk | yok (doğal omuz) | kırıcı taçta, sol tepede ilk taze kesik |
| G1 | düz kaide (%34,5) · 0 sıra | — | — | yok · gemi yok | ekskavatör park | taç GİTTİ · apron + basamak oyulmuş |
| G2 | 12 sıra (%48,8) | — | halka · direk +23 · kabin tepede | rampa yuvada · gemi rampada | yükleyici + 4 palet | NEEDLE tepesi geçildi, ufkun altında |
| G3 | 30 sıra (%70) | galeri + korkuluk (%72) | galeri üstü · direk +41 · kabin dipte | rampa yuvada · gemi yok | yükleyici park, branda | ufuk geçildi · gök kapalı · iş durdu |
| G4 | aynı · ıslak bant | aynı | aynı · kabin ortada sandıkla | rampa YUVADA · gemi rampada | birikintiler · yükleyici kabin dibinde | hat yeniden kurulu, ilk yük yolda |
| G5 | aynı · kuru | fener + külah (%82) · cam KARANLIK | iskele 26. sıraya (%65) · direk +41 | rampa yuvada · gemi yok | yükleyici + 2 boru demeti | fener tam, söküm başladı |
| G6 | aynı · kuru | fener · cam YANIK | — | rampa yuvada (kalıcı) · gemi yok | BOŞ · direk izi | final |

⛔ Monoton büyüme: G(n) ≤ G(n+1) kulede her satırda. Kaldırılan tek doğal şey TAÇTIR (S0). Sökülen geçici ekipman
YALNIZ S0–S1 (ekskavatör · oluk) ve S4 sonu–S5 (iskele · direk · yükleyici · gemi) içinde ve FİİLLE çıkar.

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
NESNE        THE NEEDLE — tek deniz sütunu, sağda, x ≈ 761–832, ≈200 px boy · + KAYANIN ALT GÖVDESİ (yosun bandı)
KONTROL      her zincir_kontrol.sh koşusunda ELLE: iki karede de aynı yerde, aynı boyda, aynı profilde mi? ✓/✗
             ✗ ise kare ATILIR — betik geçse bile. Sütun ÇOĞALIRSA (iki sütun) da ✗ [DERS 55].
İKİNCİ       deniz ufku (%50) · üçüncü: uzak burnun düz sırtı (%53) · dördüncü (G1+): kaide + apron + basamaklar
SAYIM        kule = 1 · sütun = 1 — her karede ELLE (günlük §2)
⛔ NONE FOUND gelirse film aynı yerde geçmiyor demektir — yeniden üretim sebebi (kart R 6b).
```

---

## 5. ⑧ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| Eleman | Hammaddesi nereden/nasıl geldi | Geçici destek / ara hâl kanıtı | İlk EKSİK görüldüğü kare | Tamam |
|---|---|---|---|:-:|
| kaide (taç kesimi) | kırıcı tepeleri kademe kademe indirir; kırık taş OLUKTAN gemiye (S0) | taze kesik yüz · bench · spoil chute | G0 (sol tepede ilk kesik) | G1 |
| apron + basamaklar | aynı ekskavatör, sol omuz (S0 ikinci yarı) | raw cut steps · spoil drift | G0 (doğal omuz) | G1 |
| rampa | gemiyle gelir, yuvasına oturur (S1 ilk 2 sn) | zincir · pim | G1 (yok) | G2 |
| asansör direği | gemiyle parça parça, apronda cıvatalanır (S1) · S2'de uzar | kabin · bağlantılar | G1 (yok) · G2 (+23) | G3 |
| granit gövde | paletler gemiden → rampa → apron (sayım ≤ 6) → kabin → güverte → sıra (S1–S2) | halka iskele · güverte · crew streak | G2 (12/30) | G3 |
| galeri | konsol korniş taşları aynı hatla; korkuluk cıvatalı (S2 sonu) | iskele galerinin üstünde | G2 (yok) | G3 |
| iniş hattının yeniden kurulması | rampa zincirde kalır (kaybolmaz), zincir çekmeleriyle yuvaya (S3 son 2 sn) | chain hoists · pim · crew streak | S3 ortası (çapraz — KARE DEĞİL, ⑦ ⑩ klipte arar) | G4 |
| fener çerçevesi + camlar | çelik sandıklarda: ilk sandık G4'te kabinde, kalanı gemiyle (S4) | sandık · kabin · galeri güvertesi | G4 (çıplak galeri) | G5 |
| bakır külah + rüzgârgülü | dilimler sandıklarda, kabinle (S4 orta) | iskele galeri üstünde | G4 | G5 |
| iskele sökümü | TEPEDEN; borular kabinle apronda DEMET (S4 son 2 sn → S5 ilk 2 sn) | boru demeti sayımı 0 → 2 → gemiye | G5 (%65'e inmiş) | G6 (yok) |
| direk sökümü | iskeleden SONRA, tepeden, her parça kabinle (S5) | direk parçaları apronda | G5 (+41) | G6 (açık iz) |
| ilk ışık | lamba/optik montajı fener odasının içinde (görünmez) — vekil: camın YANMASI (S5 son çeyrek) | — | G5 (cam karanlık) | G6 |

```
GİZLİ İŞ + GÖRÜNÜR VEKİL [P2-g]
  harç prizi ve derz işçiliği      → güverte kenarında crew streak + yatay derz çizgileri
  lamba ve optik montajı           → S5'te camın YANMASI
  rampa yuvasının pim/ankrajı      → yuvaya oturan rampa + başında crew streak (G4)
⛔ Sahada kaynağı olmayan parça "APPEARED" hükmü yer; yukarıdaki on iki satır kaynak beyanıdır.
⚠️ S2 iki elemanı (18 sıra + galeri) ve hava değişimini, S5 dört çıkışı (iskele · direk · yükleyici · gemi) ve ışığı
   aynı klipte taşır — düz ızgaranın katlama bedeli, plan §AŞAMA MERDİVENİ (c). ⑧ ayrı ayrı sorar.
⚠️ ⑪ ENVANTER için davetli liste: kaya · kaide · apron · basamaklar · NEEDLE · deniz · köpük · uzak burun + tarla ·
   paletli ekskavatör (kırıcılı) · çelik oluk · gri çıkarma gemisi · turuncu rampa + zincir · asansör direği + sarı
   kabin · halka iskele · kompakt paletli yükleyici · granit paletleri · çelik sandıklar · boru demetleri · branda ·
   fener odası · bakır külah · rüzgârgülü · crew streak. Bunların dışında görünen her şey DAVETSİZDİR
   (ikinci kule · ikinci sütun · VİNÇ · kule vinci · ışık huzmesi · beyaz boyalı/kırmızı bantlı gövde · ikinci gemi ·
   bina · keskin insan figürü · havuz).
```

---

## 6. ⑥ GEÇİŞ — kesme listesi ve ses

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · 24,0 · 32,0 · 40,0   (5 kesme, hepsi ölçü başı — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 dikey_shorts/THE_DARK_ROCK/THE_DARK_ROCK_DIKEY_TIMELAPSE.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE (G1 · G2 · G3 · G4 · G5); kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                120 BPM · müziksiz pencere 0,0–2,0 (dalga + martı) · 24,0–28,0 yalnız rüzgâr ve ağır deniz ·
                     28,0 çelik sürtünme + zincir → perküsyon geri · 46,0 sıcak akor ışıkla açılır ve tutulur
                     ⭐ düz ızgarada yay katmanlarla taşınır: her 8 sn'lik blok bir öncekinden farklı sesler
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_DARK_ROCK_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse ARAÇ değişir ya da karar proje sahibine (plan)
⛔ ÖN GÖRSELLEŞTİRME  güney sütunu · kaya · kule · NEEDLE · uzak burun planı + yan kesiti
⛔ USTA KARE      G6 önce; kapı: yanan cam · tam kule · kesilmiş kaide + boş apron + rampa bu sırayla · ışık camın içinde
⛔ ZİNCİR         her karede zincir_kontrol.sh + NEEDLE ve kayanın alt gövdesi ELLE (boy dâhil) + kule/sütun sayımı
⛔ ARA KARE YOK  her sahne iki onaylı kare arasında TEK 8,0 sn klip (proje sahibinin kararı, 15.09.2026)
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28 — dört kez ölçüldü]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4
⛔ KAPAK KANITI   ffmpeg -ss 47.0 -i teslim.mp4 -frames:v 1 g6_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g6_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
```
