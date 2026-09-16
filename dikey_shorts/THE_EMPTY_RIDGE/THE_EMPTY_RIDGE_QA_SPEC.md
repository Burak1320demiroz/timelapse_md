# 🔍 THE EMPTY RIDGE — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM · ⑥ GEÇİŞ · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER).
> ⛔ ① KARE · ③ ZAMAN · ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET · ⑫ KATILIK merceklerine **VERİLMEZ** — o altısı
> dokümansız koşar [AGENTS değişmez ⑦]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit,
> kilit değildir; tariftir.

---

## 0. KÜNYE

```
FİLM          THE EMPTY RIDGE — çıplak ot sırtında rüzgâr türbini, güneydeki yüksek sırttan
FORMAT        9:16 dikey · 1080×1920 · 30 fps

TESLİM YAPISI ⭐ SAHNE BLOĞU  7 sahne × 8,0 sn = 56,0 sn                  ← merceklerin konusu
              ⭐ KAPAK KARTI  1 × 5,0 sn        =  5,0 sn                  ← SAHNE DEĞİL
                 TOPLAM                           61,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR ve devamlılık karşılaştırmalarına GİRMEZ.
                 Ayrı denetlenir: "kart, S6'nın sonundaki türbinin AYNISINI mı gösteriyor?"

SAHNE SAATLERİ  S0 0,0–8,0 · S1 8,0–16,0 · S2 16,0–24,0 · S3 24,0–32,0
                S4 32,0–40,0 · S5 40,0–48,0 · S6 48,0–56,0
                KART 56,0–61,0
                (120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · her kesme ölçü başında)
⛔ DÜZ IZGARA   proje sahibinin kilidi (14.09.2026). ⑥ METRONOM hükmü BEKLENEN ve KABUL EDİLMİŞ
                risktir (plan §AŞAMA MERDİVENİ · DERS 24); hüküm gelirse "beklenen" diye kaydedilir,
                yeniden üretim sebebi sayılmaz. Ritim isteniyorsa SÜRE sütunu değişir, prompt değil.
                (Karşı kanıt notu planda: OVER THE WALL varyanslı kurguda RHYTHM aldı.)
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]:
   ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
   ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — ölçülünce buraya ve plana yazılır; her sahne 8,0 sn teslim
   → en büyük kutu ≥ 9,0 gerekir; {4,6,8} çıkarsa yedi sahnenin yedisi iki zincirli klip
   (plan §DEĞİŞMEZLER · ARAÇ KUTU SETİ satırı).

YAPI          karasal rüzgâr türbini · göbek 100 m · 4 segmentli boru kule · rotor 140 m · kanat ucu 170 m
SAHA          kırsal / boş arazi — ot sırtı + buğday tarlası + geniş vadi + uzak sıradağ (SAHA_VE_IKLIM §3.2)
ZAMAN YAYI    ~9,5 hafta (Temmuz ortası → Eylül sonu) · film mertebe anlatır: "yaklaşık iki ay" [P1-c]
IŞIK          TEK GÜN 06:00 → 20:00 (7 klip × rejim B 2 saat = 14 saat) · takvim tarladan · bilinçli sıkıştırma
KAMERA        MAIN STATION — tek istasyon, 7 sahne + usta kare · h +100,0 m · D_eksen 320 m · 350° · tilt 0°
              ⛔ SAHA ŞARTI: uzak sıradağ silueti kameradan ≥ +6° (≈ %57) — kaldırmalar dağa karşı [DERS 22 · 52]
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G7 usta kare → G6 → … → G0 · her kare zincir_kontrol.sh
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S6
SANİYE      0:54,5   (S6'nın 6,5. saniyesi — son ≥2,0 sn'lik TUTUŞUN içi [P2-i]; tutuşta rotor DÖNER)
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① DÖNEN ROTOR: üç kanat, göbek kadraj ekseninde göz çizgisinde (%50), kanat uçlarında hafif hareket izi,
      bir kanat ucu sıradağ siluetinin (%57) ÜSTÜNDE gökte (uç ≈ %65).
   ② BOŞ PAD: kulenin solunda kırma taş, palet izi, takoz — vinç YOK, bom YOK, treyler YOK, raf YOK.
   ③ AYNI MEŞE: eksenin sağında (x ≈ 742 px), %29–32, ≈64 px boy — G0'daki ile aynı konum ve boy;
      kule gölgesi sırt boyunca sağa uzanır.
   + tarla sürülmüş kahve şeritler · tulum düşük · güneş 20:00 (az 296°, +7°), aydınlık [DERS 45].

KOMUT
   ffmpeg -ss 54.5 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede rotor DURUYORSA, vinç/bom kadrajdaysa, göbek %50'de değilse ya da meşe boyu/konumu G0'dan
   sapmışsa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP
   ffmpeg -ss 0.3  -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 54.5 -i teslim.mp4 -frames:v 1 kanit_g7.jpg
   İki karede: meşe (x ≈ 742 · y %29–32 · 64 px), duvar (sol · %28–30 · ≈300 px), sıradağ silueti (%57)
   tam aynı yerde. Işık aynı DEĞİLDİR (06:00 gölge sola → 20:00 gölge sağa, bilinçli — plan LOOP satırı).
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h_kam=+100 · D=320 · tilt 0 · yüzde = 50 + 66,7·(y−100)/D, ALT kenardan)

| Ne | Beklenen (kare yüksekliği) | Tol. | Hangi sahnelerde |
|---|---|---|---|
| göz çizgisi = BİTMİŞ KULENİN ÜST FLANŞI / GÖBEK | %50,0 | ±%1,0 | G4–G7 (tepe) · G0–G7 (çizgi, sıradağ alt yamacı) |
| sırt çizgisi / pad / kule tabanı | %29,2 | ±%1,0 | G0–G7 |
| meşe (taban → tepe) | %29–32,5 · x ≈ 742 px · ≈64 px boy · ≈47 px taç | ±%0,5 · ±10 px | G0–G7 (hepsi — ⛔ boy sabit) |
| kuru taş duvar | %28–30 · x ≈ 240–540 px (≈300 px) | ±%1,0 · ±15 px | G0–G7 |
| uzak sıradağ silueti | %57 (düz) | ±%1,5 | G0–G7 |
| segment 1 tepesi (25 m) | %34,4 | ±%1,5 | G3 |
| kule tepesi (100 m) | %50,0 | ±%1,0 | G4–G7 |
| nasel üstü (104 m) | %50,8 | ±%1,0 | G5–G7 |
| bom başı (≈122 m) | %54,6 · x ≈ 422 px — SİLÜETİN ALTINDA | ±%1,5 | G3–G6 (G7'de YOK) |
| kanat ucu dik (170 m) | %64,6 · alt uçlar %42,9 · x 341 / 739 px | ±%1,5 | G6 (Y duruşu) · G7 (döner) |
| rüzgâr tulumu | pad kenarı, direk %29–33 · G4 YATAY · diğerleri düşük/slack | — | G1–G7 |

```
⛔ ÜST SINIR   hiçbir yapı parçası %87,5'in üstünde olamaz (kanat ucu %64,6 — 23 puan pay)
⛔ ALT SINIR   ilerlemeyi kanıtlayan hiçbir şey %25'in altında olamaz (pad %29,2'de) — tarlanın alt bandı
               (%0–25) yalnız mevsim taşıyıcısıdır (biçerdöver, balya, sürüm) ve UI altında kalabilir
⛔ SAĞ ŞERİT   kanıt nesnesi kare genişliğinin sağ %13'ünde (x > 945 px) duramaz (meşe x ≈ 742 ✓)
⛔ D_kenar     kadrajın alt kenarı kameradan 133 m'de tarlaya iner; 133–267 m arası UI bandıdır
⭐ PİKSEL      meşe, duvar ve silüet USTA KARE onaylanınca ölçülür, buraya ve plana yazılır
               [PERSPEKTIF §4]; yukarıdaki sayılar formül tahminidir.
⛔ ÖN GÖRSELLEŞTİRME  usta kareden önce yan kesit: her yükün kaldırma yolu boyunca arka plan DAĞ mı GÖK mü
               işaretlenir; segmentler · nasel · yatay kanat → dağ; dik kanat ucu → gök (kaldırma değil, duruş)
⚠️ S3 tek klipte üç segment (%34 → %50), S5 tek klipte üç kanat — filmin en yoğun iki klibi; ① merceği
   bu kliplerde MEŞE BOYUNU (64 px) özellikle ölçer: kule büyürken meşe küçülmüş mü? [DERS 51 · bedel cümlesi]
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
türbin         karasal 4,5 MW sınıfı · üç kanatlı · rotor yüzü KAMERAYA (hâkim rüzgâr güneyden)
kule           boru çelik · 4 segment × 25 m = 100 m göbek · taban çapı 4,5 m · tepe 3,0 m · beyaz · cıvatalı flanş
nasel          ~15 m × 4 m · gri-beyaz · göbek pad'de nasele cıvatalanır → TEK KALDIRMA (S4)
rotor          140 m çap · kanat 68 m · göbek burnu 4 m · kanat ucu 170 m · Y duruşu G6 · saat yönü G7
temel          dairesel 20 m çap · 3 m derin · donatı kafesi + ankraj halkası 4,5 m · beton koyu → açık (S1)
pad            kırma taş 60 × 30 m · kulenin batısı · silindirle sıkıştırılmış · palet izi G7'de kalır
yol            6 m çakıl · tarlanın sol alt köşesinden çapraz · geniş viraj · pasa şeritleri kenarlarda
ana vinç       1000 t sınıfı kafes bomlu paletli · 120 m ana bom (rüzgâr konfig.) · ~82° · eksenin 35 m batısı
               MARKA YOK · S1 sonu parça parça gelir · S2 kendi bomunu kaldırır · S6 bom iner, yoldan çıkar
yardımcı vinç  250 t sınıfı teleskopik · segment kuyruklama · kanat tagline · S6'da sürülerek çıkar
meşe           16 m boy · 14 m taç · eksenin 60 m doğusu · ⛔ SEKİZ KAREDE AYNI PİKSEL
duvar          kuru taş · ~1,2 m yüksek · sırt boyunca eksenin batısı · ~90 m görünür
kamera         h +100,0 m · D_eksen 320 m · D_kenar 133 m · 350° · tilt 0° · roll 0° · 24 mm tam kare dikey
makineler      paletli dozer · greyder · paletli ekskavatör · sarı damper (ölçek çapası) · mikser · pompa ·
               silindir · low-loader · biçerdöver · traktör + römork · pulluk · servis kamyonu · pikap
```

### Türbin yüksekliği ve saha durumu — sahne sahne (② İNŞA · ④ TESLİM · ⑩ SEBEP için)

| G | kule | nasel/rotor | vinç | pad'de yatan | tarla | gözle görülmesi gereken ilerleme |
|:-:|---:|---|---|---|---|---|
| G0 | 0 | — | — | — | altın buğday | sol altta dozer + greyder, ilk yol metreleri; sırt çıplak |
| G1 | 0 | — | — | — | altın | yol tamam · çukur + pasa halkası · tulum direği |
| G2 | 0 (temel açık gri) | — | yatık parçalar | 4 segment treylerde | altın | temel + ankraj halkası · pad · vinç parçaları sıralı |
| G3 | 1 segment (%34) | — | bom DİK | 3 segment | biçiliyor | ilk segment dik · bom dağa karşı |
| G4 | 4 segment (%50) | — · üst flanş çıplak | bom dik · kanca pad'de | nasel+göbek · 3 kanat | anız + balya | kule tam · tulum YATAY |
| G5 | 4 | nasel + çıplak göbek (%51) | bom dik · sapanda | 3 kanat | çıplak anız | nasel oturmuş · tulum düşük |
| G6 | 4 | rotor tam · Y · durur | bom dik | — (raflar boş) | çıplak anız | üç kanat · vinç hâlâ yerinde |
| G7 | 4 | rotor DÖNER | YOK | — (takoz, izler) | sürülmüş | final |

⛔ Monoton büyüme: G(n) ≤ G(n+1) türbinde her satırda. Sökülen ekipman YALNIZ S6'da ve YOLDAN çıkar.

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
NESNE        YALNIZ MEŞE — sırt üstü, eksenin 60 m doğusu, 64 px boy, x ≈ 742 · + KURU TAŞ DUVAR (sol)
KONTROL      her zincir_kontrol.sh koşusunda ELLE: iki karede de aynı yerde, aynı boyda, aynı dal biçimi mi? ✓/✗
             ✗ ise kare ATILIR — betik geçse bile. Meşe KÜÇÜLÜRSE de ✗ (bedel cümlesi: ölçek değişir, ağaç değil).
İKİNCİ       uzak sıradağ silueti (%57) · üçüncü (G1+): yol · dördüncü (G1+): tulum direği
⛔ NONE FOUND gelirse film aynı yerde geçmiyor demektir — yeniden üretim sebebi (kart R 6b).
```

---

## 5. ⑧ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| Eleman | Hammaddesi nereden/nasıl geldi | Geçici destek / ara hâl kanıtı | İlk EKSİK görüldüğü kare | Tamam |
|---|---|---|---|:-:|
| yol | dozer keser, greyder serer, damper çakıl getirir (S0 içinde) | raw cut scar · spoil windrow | G0 (ilk metreler) | G1 |
| temel çukuru | ekskavatör kazar, pasa halkası büyür (S0 içinde) | bucket teeth marks · spoil ring | G0 (%0 — ot) | G1 |
| temel | flatbed donatı → kafes inişi → mikser sırası + pompa (S1 içinde); koyu → açık renk sınırı | rebar cage · anchor ring · backfill | G1 (açık çukur) | G2 |
| pad | damper kırma taş, dozer serer, silindir ezer (S1 içinde) | roller drum marks | G1 (ot) | G2 |
| ana vinç | low-loader'la parça parça (S1 sonu) → kendi bomunu kaldırır (S2) | boom sections in a row · pendant ropes | G2 (yatık) | G3 |
| kule segmentleri | treylerle gelir (S1 sonu), pad'de sıralı; kuyruklama + kısa sapan; flanşa cıvata | slings · taglines · timber blocks · sayım 4→3→0 | G2 (treylerde) · G3 (1/4) | G4 |
| nasel + göbek | heavy trailer (S3), çerçevede bekler (G4), spreader beam ile tek kaldırma (S4) | transport frame · spreader beam | G4 (yerde) | G5 |
| kanatlar | uzun treylerle (S3), raflarda (G4–G5), kanat aparatıyla yatay, göbek ⅓ tur (S5) | blade yoke · taglines · sayım 3→0 | G4 (rafta) | G6 |
| ilk dönüş | devreye alma (kadraj dışı) — vekil: rotorun dönmesi (S6), vinç gittikten sonra | uç izi | G6 (durur) | G7 |

```
GİZLİ İŞ + GÖRÜNÜR VEKİL [P2-g]
  temelin kürlenmesi (S1 ikinci yarı)  → koyu → açık beton renk sınırı
  flanş cıvatalama / tork              → crew streak flanşta + tagline
  şebeke bağlantısı, devreye alma       → S6'da rotorun DÖNMESİ
⛔ Sahada kaynağı olmayan parça "APPEARED" hükmü yer; yukarıdaki dokuz satır kaynak beyanıdır.
⚠️ S0 iki elemanı (yol + çukur), S1 üç işi (temel · pad · teslimat) aynı klipte taşır — düz ızgaranın
   katlama bedeli, plan §AŞAMA MERDİVENİ (c). ⑧ ayrı ayrı sorar.
⚠️ ⑪ ENVANTER için davetli liste: dozer · greyder · ekskavatör · damper · flatbed · mikser · pompa · silindir ·
   low-loader · paletli vinç · teleskopik vinç · treyler · biçerdöver · balya traktörü · servis kamyonu ·
   pulluk traktörü · pikap · tulum · meşe · duvar · buğday/anız/balya/sürüm · vadi · sıradağ. Bunların
   dışında görünen her şey DAVETSİZDİR (ikinci türbin · kule vinci · bina · insan figürü · ikinci ağaç).
```

---

## 6. ⑥ GEÇİŞ — kesme listesi ve ses

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0   (6 kesme, hepsi ölçü başı — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 dikey_shorts/THE_EMPTY_RIDGE/THE_EMPTY_RIDGE_DIKEY_TIMELAPSE.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE (G1…G6); kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                120 BPM · müziksiz pencere 0,0–2,0 (rüzgâr + tarla kuşu) · 32,0–36,0 yalnız rüzgâr (bekleyiş)
                     · 48,0 sub swell (vinç gider) · 48–56 dönen pad (üç vuruşlu) · 54–56 tutulan akor
                     ⭐ düz ızgarada yay katmanlarla taşınır: her 8 sn'lik blok bir öncekinden farklı sesler
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_EMPTY_RIDGE_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse iki-klip hükmü YEDİ sahneye (plan)
⛔ ÖN GÖRSELLEŞTİRME  kamera · spur · kule · bom · sıradağ yan kesiti; SAHA ŞARTI (+6°) burada doğrulanır
⛔ USTA KARE      G7 önce; kapı: dönen rotor · boş pad · aynı meşe bu sırayla okunuyor mu · göbek %50
⛔ ZİNCİR         her karede zincir_kontrol.sh + MEŞE ve DUVAR ELLE (boy dâhil)
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28 — üç kez ölçüldü]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4
⛔ KAPAK KANITI   ffmpeg -ss 54.5 -i teslim.mp4 -frames:v 1 g7_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
```
