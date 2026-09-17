# 🔍 THE HIDDEN OASIS — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM · ⑥ GEÇİŞ · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER).
> ⛔ ① KARE · ③ ZAMAN · ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET · ⑫ KATILIK merceklerine **VERİLMEZ** — o altısı
> dokümansız koşar [AGENTS değişmez ⑦]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit,
> kilit değildir; tariftir.

---

## 0. KÜNYE

```
FİLM          THE HIDDEN OASIS — duvarlı avluda terk edilmiş havuzun taş kenarlı gölete çevrilmesi
FORMAT        9:16 dikey · 1080×1920 · 30 fps

TESLİM YAPISI ⭐ SAHNE BLOĞU  7 sahne × 8,0 sn = 56,0 sn                  ← merceklerin konusu
              ⭐ KAPAK KARTI  1 × 5,0 sn        =  5,0 sn                  ← SAHNE DEĞİL
                 TOPLAM                           61,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR ve devamlılık karşılaştırmalarına GİRMEZ.
                 Ayrı denetlenir: "kart, S6'nın sonundaki göletin AYNISINI mı gösteriyor?"
              ⚠️ Kart AJAN KARARIYLA eklendi (16.09.2026); dış üretim planı kartsız 56,0 sn istiyordu.
                 Sahip kartsızlığı seçerse bu blok yeniden yazılır, boş bırakılmaz [DERS 4].

SAHNE SAATLERİ  S0 0,0–8,0 · S1 8,0–16,0 · S2 16,0–24,0 · S3 24,0–32,0
                S4 32,0–40,0 · S5 40,0–48,0 · S6 48,0–56,0
                KART 56,0–61,0
                (120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · her kesme ölçü başında)
⛔ DÜZ IZGARA   proje sahibinin kilidi (16.09.2026). ⑥ METRONOM hükmü BEKLENEN ve KABUL EDİLMİŞ
                risktir (plan §AŞAMA MERDİVENİ · DERS 24); hüküm gelirse "beklenen" diye kaydedilir,
                yeniden üretim sebebi sayılmaz. Ritim isteniyorsa SÜRE sütunu değişir, prompt değil.
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]:
   ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
   ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — her sahne 8,0 sn teslim → en büyük kutu ≥ 9,0 gerekir;
   {4,6,8} çıkarsa ARAÇ değişir ya da karar proje sahibine döner — ARA KARE YOK, her sahne tek klip.

YAPI          taş kenarlı bahçe göleti · eski yüzme havuzunun sınırında · üç kademeli çağlayan · sekiz dikim cebi · altı fener
SAHA          duvarlı Akdeniz avlusu — tek havuz + tek zeytin + kemerli niş + harpuşta çizgisi + teras yamacı (yeni kart)
ZAMAN YAYI    BİR GÜN mertebesi (06:20 → 18:30) · gerçek iş dört gün mertebesindedir — BİLİNÇLİ SIKIŞTIRMA, planda beyanlı
IŞIK          TEK GÜN 06:20 → 18:30 (6 klip × rejim B 2 saat + 1 klip × rejim A 10 dk = 12 sa 10 dk) · takvim YOK
KAMERA        MAIN STATION — tek istasyon, 7 sahne + usta kare · h +6,0 m · D_eksen 5,0 m · 0° · ⛔ tilt −40°
VİNÇ          ⛔ YOK — hiçbir yük havada taşınmaz; astar rulosu BEL HİZASINDA taşınır. Kadrajda vinç görülürse DAVETSİZDİR
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G7 usta kare → G6 → G5 → G4 → G3 → G2 → G1 → G0 · her kare zincir_kontrol.sh
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S6
SANİYE      0:55,0   (S6'nın 7,0. saniyesi — son 2,0 sn'lik TUTUŞUN içi [P2-i]; ışık yanık ve SABİT)
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① YANAN SU: kadrajın alt yarısında (%13–52) duran koyu ayna; altı sıcak nokta ve altlarında altı yansıma;
      ışık lambaların İÇİNDE ve taşın üstünde (huzme · koni · suda ışık yolu YOK).
   ② TAŞ KENAR + DİKİLİ BANT: havuzun sınırı G0'daki dikdörtgenin AYNISI; kenar tek sıra dolomit,
      uzak kenarda sekiz cepte bitki ve koyu malç bandı; çağlayan üç kademede akıyor.
   ③ BOŞ AVLU: merdiven YOK, mavi seramik YOK, alet/tekne/torba/saksı YOK; döşeme süpürülmüş, kapı KAPALI,
      kapak taşı filtrenin üstünde.
   + NİŞ aynı yerde aynı boyda (≈99 × 134 px) · ZEYTİN GÖVDESİ x %9,2 · harpuşta %78,7 düz ·
     güneş 18:30 (az 277°, ufkun 4° altında) — mavi saat, kare AYDINLIK [DERS 45].

KOMUT       ffmpeg -ss 55.0 -i teslim.mp4 -frames:v 1 final_kanit.jpg
⛔ ÜÇÜ BİRDEN GÖRÜNMÜYORSA TESLİM YOKTUR. Eksik olan madde adıyla günlüğe yazılır ve S6 yeniden üretilir.
⚠️ EN SIK BEKLENEN ARIZA: suyun aynası "havuz suyu mavisi"ne kayar (korpus baskısı). Gölet suyu KOYUDUR ve
   rengini yansımadan alır; camgöbeği/turkuaz gelirse kare ATILIR [DERS 42 · 54].
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=+6,0 · D_eksen=5,0 · ⛔ tilt −40°)

```
⛔ TILT SIFIR DEĞİL: KAMERA_ISTASYONU §3 formülü (yüzde = 50 + 66,7·(y−h)/D) BU FİLMDE GEÇMEZ.
   Kullanılan formül — kadrajın ALT kenarından, d = kameradan yatay mesafe (m):
        yüzde(d) = (76,87° − atan(6,0 / d)) / 73,74° · 100
   üst kenar 3,13° · alt kenar 76,87° · dikey görüş açısı 73,74° · ufuk kadrajın ÜSTÜNDE, kadrajda YOK.
   ⛔ Bu değerler TÜRETİLDİ, ÖLÇÜLMEDİ. Usta kare onaylanınca ölçülür ve bu tablo ÜSTÜNE yazılır.

| ne | d (m) | yükseklik (m) | yüzde (alttan) | px (alttan) |
|---|---:|---:|---:|---:|
| kadrajın alt kenarı zemine değer | 1,40 | 0 | %0 | 0 |
| havuz YAKIN kenarı | 2,50 | 0 | %12,9 | 248 |
| havuz ekseni | 5,00 | 0 | %36,1 | 693 |
| zeytin gövde dibi | 5,50 | 0 | %38,3 | 735 |
| havuz UZAK kenarı | 7,50 | 0 | %51,8 | 995 |
| duvar dibi | 10,00 | 0 | %62,2 | 1194 |
| niş eşiği | 10,00 | 0,90 | %67,6 | 1298 |
| niş kemer tepesi | 10,00 | 2,00 | %74,6 | 1432 |
| DUVAR TACI (harpuşta) | 10,00 | 2,60 | %78,7 | 1511 |
| zeytin taç ucu | 5,50 | 4,40 | %82,2 | 1578 |
| üst 1/8 sınırı (teras yamacı) | 22,40 | 0 | %87,5 | 1680 |

x KİLİTLERİ (yarı genişlik = 0,4219 · √(d² + 36))
| ne | d (m) | x (m) | yüzde (soldan) | px |
|---|---:|---:|---:|---:|
| zeytin gövdesi | 5,50 | −2,80 | %9,2 | 99 |
| kapı (sol duvar) | 9,00 | −3,20 | %14,9 | 161 |
| havuz sol kenarı | 5,00 | −1,50 | %27,3 | 295 |
| havuz sağ kenarı | 5,00 | +1,50 | %72,7 | 785 |
| NİŞ sol kenarı | 10,00 | +0,75 | %57,6 | 622 |
| NİŞ sağ kenarı | 10,00 | +1,65 | %66,8 | 721 |
| çağlayan | 10,00 | +1,50 | %65,2 | 704 |

⭐ ÖLÇEK ÇAPASI: NİŞ ≈ 99 px en × 134 px boy — SEKİZ karede aynı. Sapma > 4 px → kare ATILIR.
⛔ SHORTS UI: alt %0–13 ve sağ %87,5+ ilerleme kanıtı TAŞIMAZ. Havuzun sağ kenarı %72,7'de kalır ✓
⛔ ÜST 1/8: %87,5+ yalnız teras yamacı — sekiz karede aynı doku, aynı sıra.
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
havuz kabuğu    5,0 × 3,0 m · yuvarlatılmış köşe · derinlik sığ uç 1,0 m → derin uç 1,4 m
                açık mavi sırlı seramik · sığ uçta banyo basamağı (genişlik 0,4 m)
merdiven        paslanmaz · 3 basamak · yakın SOL köşe · 4 cıvata · S1'de sökülür
astar           gri koruyucu keçe (2 rulo) + tek parça siyah EPDM (bir sheet) · kenar harpuştaya kıvrık
taş kenar       kaba dolomit · 25–45 cm · TEK SIRA · harç yastığı · kapının yanındaki istif: 6 araba yükü
çağlayan        3 kademe · toplam düşü 0,35 m · sağ arka köşe · taş seki
çakıl           yıkanmış dere çakılı · sığ uçta sahanlık
dikim cepleri   8 adet · uzak kenar · eğrelti · saz · yer örtücü · koyu malç bandı
fener           6 adet · mat siyah · 0,5 m · sıcak ampul · sağ patika · kablo taş altında
filtre          nişin dibinde kutu + düz kapak taşı · boru taş kenarın altından
duvar           2,6 m · kuru taş + kireç sıva · düz taş harpuşta
niş             0,9 m en × 1,1 m boy · eşik 0,9 m · kemer tepesi 2,0 m
zeytin          1 ağaç · gövde Ø 0,6 m · boy 4,4 m · S4'te budanır (GÖVDE değişmez)
kapı            sol duvar, arka köşeye yakın · TEK giriş çıkış
kamera          +6,0 m · D_eksen 5,0 m · D_kenar 1,40 m · 24 mm · tilt −40° · bearing 0°
güneş           37°K · eylül ortası (δ +3°) · doğuş 05:51 · batış 18:09
```

### Saha durumu — kare kare (② İNŞA · ④ TESLİM · ⑩ SEBEP için)

| G | saat | havuzun içi | kenar | ekipman (geçici) | ışık |
|:-:|---|---|---|---|---|
| G0 | 06:20 | koyu yeşil su, yaprak salı | mosslu harpuşta, merdiven takılı | pompa + hortum · araba · kürek · kova | doğu duvarı gölgesi tüm avlu |
| G1 | 08:20 | boş, siyah silt + yaprak matı, derin uçta birikinti | merdiven takılı, harpuşta açık | pompa + hortum · 2 araba · atık yığını | uzun gölge sola |
| G2 | 10:20 | temiz açık mavi seramik, ıslak/kuru sınırı | 4 cıvata deliği, gri harç izleri | pompa + yıkayıcı · 2 araba | kısa gölge geriye |
| G3 | 12:20 | kuru MAT siyah astar (keçe altta) | astar kenarı harpuştada + taş ağırlıklar | filtre kutusu · rulo göbekleri · araba | en kısa gölge |
| G4 | 14:20 | kuru siyah astar + çakıl sahanlık | tek sıra dolomit KAPALI · çağlayan kuru · 8 açık cep | harç teknesi · torbalar · 2 blok | kısa-sert gölge sağa |
| G5 | 16:20 | hâlâ KURU siyah astar | dikili 8 cep · malç bandı · 6 SÖNÜK fener | dolum hortumu · saksı yüklü araba | uzun gölge sağa |
| G6 | 18:20 | SU: üçüncü taşta · duran yüzey · yansıma | taş + bitki tamam · çağlayan AKIYOR · fenerler SÖNÜK | araba + sarılan hortum | harpuştada sıcak bant |
| G7 | 18:30 | SU: üçüncü taşta · ayna · 6 yansıma | taş + bitki tamam · çağlayan akıyor · 6 fener YANIK | ⛔ HİÇBİRİ — avlu boş, kapı kapalı | mavi saat |

```
⛔ SU SEVİYESİ KİLİDİ: G6 ve G7'de su yakın kenarın ÜÇÜNCÜ taşının alt yüzündedir — iki karede AYNI.
   Seviye oynarsa ⑤ "su zıpladı" der; kare ATILIR. Klip içi ara seviyeler kareye bağlı DEĞİLDİR (beyanlı risk).
⛔ ASTAR ISLAKLIK KİLİDİ: G3 · G4 · G5'te astar KURU ve MAT, yansıma YOK. Parlarsa kare ATILIR [DERS 54 tersi].
⛔ FENER KİLİDİ: G0–G6'da hiçbir fener yanmaz; G5 ve G6'da takılı ama sönük. S6'dan önce ışık = DAVETSİZ [DERS 56].
```

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
⭐ AYNI YER NESNESİ   ① KEMERLİ NİŞ (99 × 134 px · x 622–721 · y 1298–1432 alttan)
                      ② ZEYTİN GÖVDESİ (x 99 px · gövde dibi y 735)
                      ③ HAVUZUN SINIRI (yakın kenar y 248 · uzak kenar y 995)
KONTROL               her zincir_kontrol.sh koşusundan SONRA, İKİ karede de ELLE:
                      □ niş aynı yerde mi (±4 px)  □ niş aynı boyda mı (±4 px)  □ niş TEK mi
                      □ zeytin gövdesi aynı x'te mi  □ havuz sınırı aynı dikdörtgen mi
                      □ harpuşta çizgisi %78,7'de düz mü  □ teras yamacı aynı mı
⛔ HERHANGİ BİRİ ✗ → KARE ATILIR, yeniden türetilir. "Yakın" yeterli değildir.
⚠️ ZEYTİN BUDAMASI (S4): TAÇ HACMİ değişir, GÖVDE ve ilk çatal DEĞİŞMEZ. Çapa gövdedir.
   G5 · G6 · G7 birbirinin AYNI budanmış tacını taşır; G0–G4 aynı budanmamış tacı.
```

---

## 5. ⑧ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynağı (kadrajda nereden geldi) | geçici desteği | ilk EKSİK görüldüğü kare | tamamlandığı kare |
|---|---|---|---|---|
| suyun boşalması | pompa + hortum, kapıdan dışarı | — | G0 (yüzey inmeye başlamış) | G1 |
| silt + yaprak | kova → araba → kapı | — | G1 | G2 |
| merdiven (söküm) | sökülüp kapıdan çıkar | 4 cıvata | G1 (takılı) | G2 (4 delik) |
| çatlak onarımı | harç, kova | — | G1 son 2 sn | G2 (gri izler) |
| boru + filtre | kapıdan, arabayla | harpuştanın üstünden | G2 (yok) | G3 |
| keçe | kapıdan, rulo | — | G2 | G3 (yalnız kenarı görünür) |
| astar | kapıdan, tek rulo, BEL HİZASINDA taşınır | taş ağırlıklar | G2 | G3 |
| taş kenar | kapı yanındaki istif, araba araba | harç yastığı | G3 | G4 |
| çağlayan | aynı istif | taş seki | G3 | G4 |
| çakıl | araba, sığ uca dökülür | — | G3 | G4 |
| bitkiler | saksılı, arabayla (16 → 0) | saksı | G4 | G5 |
| malç | torba | — | G4 | G5 |
| fenerler | kapıdan | toprağa çakılı kazık | G4 (yok) | G5 (takılı, SÖNÜK) |
| su | dolum hortumu (tek kaynak) | — | G5 (kuru) | G6 |
| ışık | fenerlerin içinde | — | G6 (sönük) | G7 |

```
⛔ HİÇBİR ELEMAN KADRAJDA BELİRMEZ. Her biri önce kapıdan geçer, sonra avluda görülür, sonra yerine oturur.
⛔ HİÇBİR ELEMAN KAYBOLMAZ. Giden her şey kapıdan ÇIKAR [P2-h].
⭐ EKSİLEN İSTİF: taş istifi (6 yük → 0, S3) · saksı (16 → 0, S4). BÜYÜYEN İSTİF: atık yığını (S1).
```

---

## 6. ⑥ GEÇİŞ — kesme listesi ve ses

```
KESMELER    8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0   (hepsi ölçü başında · 120 BPM)
⛔ Her kesmenin İKİ YAKASI AYNI KAREDİR: S(n)'in son karesi = G(n+1) = S(n+1)'in ilk karesi.
   kesme_kontrol.sh bunu ölçer; "PLANIN KENDİSİ DÜZ" uyarısı beklenen ve kabul edilmiştir.
IŞIK ATLAMAZ  kesmede saat 2 saat ilerler ama ışık SÜREKLİDİR (tek gün): 06:20 → 08:20 → … → 18:20 → 18:30.
              Gölge yönü ve boyu tabloya uyar; ters yönde gölge = ⑥ düşer.
SES         S0 pompa + boşalan su · S1 kürek/kova/cıvata/basınçlı su · S2 ⭐ FİLMİN EN SESSİZ ANI (kauçuk) ·
            S3 taş üstüne taş + çakıl · S4 toprak/makas/saksı · S5 dolan su → çağlayan · S6 yalnız çağlayan
            0,0–2,0 müziksiz pencere: duran su, ağustosböcekleri, uzakta pompa
            18,0–20,0 ikinci sessiz pencere (astar) — plan §MÜZİK dinamik haritasında
```

---

## 7. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI          ARAC_KARTLARI §4 sekiz ölçüm · üretim günlüğü §0 · kutu ≥ 9,0 şartı
⛔ ÖN GÖRSELLEŞTİRME    plan + yan kesit (balkon · avlu · havuz · duvar + niş · zeytin · teras)
⛔ YÜZDE VE PİKSELLER   §2 tablosu TÜRETİLMİŞTİR; usta kare onaylanınca ÖLÇÜLÜR ve üstüne yazılır
⛔ TILT KARTI           KAMERA_ISTASYONU'nda "aşağı bakış" alt kartı YOK — bu film onun ilk koşusu;
                        ölçüm çıkmadan kılavuza kural yazılmaz [DERS 12]
⛔ ÜRETİM GÜNLÜĞÜ       THE_HIDDEN_OASIS_URETIM_GUNLUGU.md §0 boşken tek kare üretilmez [DERS 28]
```
