# 🔍 THE CLOSING SPAN — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM).
> ⛔ ① KARE ve ③ ZAMAN merceklerine **VERİLMEZ** — o ikisi dokümansız koşar.
> Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit
> değildir; tariftir.

---

## 0. KÜNYE

```
FİLM          THE CLOSING SPAN — Kapanan Açıklık
FORMAT        9:16 dikey

TESLİM YAPISI ⭐ SAHNE BLOĞU  10 × 6,0 sn = 60,0 sn   ← merceklerin konusu
              ⭐ KAPAK KARTI   1 × 5,0 sn =  5,0 sn   ← SAHNE DEĞİL
                 TOPLAM                    65,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR ve devamlılık
                 karşılaştırmalarına GİRMEZ. Ayrı denetlenir:
                 "kart, son sahnedeki köprünün AYNISINI mı gösteriyor?"

SAHNE SAATLERİ  S0 0,0-6,0 · S1 6-12 · S2 12-18 · S3 18-24 · S4 24-30
                S5 30-36 · S6 36-42 · S7 42-48 · S8 48-54 · S9 54-60
                KART 60-65
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [D-d]:
   ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
   Ölçülen değer: __________

YAPI          kablo askılı köprü · 400 m ana açıklık · pilon +88 m / −40 m
SAHA          kaya vadisi · dağ/eğim + kış
ZAMAN YAYI    34 ay
KAMERA        hibrit — ANA (8 sahne) + PİLON (S1 · S4)
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: S9 usta kare → S8 → ... → S0
```

---

## 1. ⛔ FİNAL VURUŞ KANITI — teslimin tek kapısı

```
SAHNE       S9
SANİYE      0:57,5   (S9'un 3,5. saniyesi)
GÖRÜLMESİ GEREKEN ŞEY:
   Vadi tabanındaki eski yol KARANLIK ve üzerinde yalnız iki-üç ayrı,
   birbirinden uzak ışık var; köprünün tabliyesinde ise KESİNTİSİZ bir
   ışık akışı vadiyi baştan sona geçiyor.

KOMUT
   ffmpeg -ss 57.5 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede aşağısı karanlık ve yukarısı akan ışık DEĞİLSE film TESLİM
   EDİLMEMİŞTİR — klip sayısı 10, süre 65 sn ve kadraj sabitliği tutsa bile.
   Sebep: bu filmin BEDELİ tek bir karede yaşıyor ve kapı klip sayar,
   vuruş saymaz [D-e].

⭐ İKİNCİ ZORUNLU KARE — KANIT ÇİFTİ
   ffmpeg -ss 5.7  -i teslim.mp4 -frames:v 1 kanit_s0.jpg
   ffmpeg -ss 57.5 -i teslim.mp4 -frames:v 1 kanit_s9.jpg
   İki karenin IŞIĞI aynı olmalı (yaz akşamı · elevation ~8° · gölge doğu).
   Farklıysa karşılaştırma geçersizdir ve filmin merkezi iddiası çöker.
```

---

## 2. KADRAJ KİLİTLERİ — ana istasyon (S0·S2·S3·S5·S6·S7·S8·S9)

Formül: `kare yüzdesi = %50 + (y − 34) / (1,5 × D)` · tolerans **± %2**

| Ne | y (m) | D (m) | Beklenen | Hangi sahnelerde |
|---|---:|---:|---:|---|
| ufuk çizgisi | — | — | %50,0 | 8 sahnede de |
| yakın pilon tacı | +88 | 120 | %80,0 | S3-S9 |
| yakın pilon tabliye kotu | 0 | 120 | %31,1 | 8 sahnede de |
| ⭐ KAPANMA NOKTASI | 0 | 320 | **%42,9** | S7 · S8 · S9 |
| karşı pilon tacı | +88 | 520 | %56,9 | S3-S9 |
| karşı pilon tabliye kotu | 0 | 520 | %45,6 | 8 sahnede de |
| ikiz zirveli sırt | +150 | 2400 | %53,2 | 8 sahnede de |
| vadi tabanı / nehir | −140 | 320 | %13,7 | ⛔ arayüz kapatır |

```
⛔ ÜST SINIR   hiçbir yapı parçası %87,5'in üstünde olamaz
⛔ ALT SINIR   ilerlemeyi kanıtlayan hiçbir şey %25'in altında olamaz
⛔ SAĞ ŞERİT   kanıt nesnesi kare genişliğinin sağ %13'ünde duramaz
```

---

## 3. ⭐ BOŞLUK OKUMASI — bu filmin ana ölçüsü

Ana açıklık 400 m. Boşluk = 400 − (2 × kol uzunluğu).

| S | Kol (her yandan) | BOŞLUK | Ekranda ne görünmeli |
|:-:|---:|---:|---|
| S4 sonu | 20 m | **360 m** | iki uç pilondan yeni ayrıldı |
| S5 sonu | 70 m | **260 m** | kollar uzadı ama açıklığın yarısından fazlası duruyor |
| S6 sonu | 125 m | **150 m** | boşluk açıklığın üçte birinden biraz fazla |
| S7 sonu | 190 m | **20 m** | ⭐ boşluk ince bir YARIK — iki kör uç karşı karşıya |
| S8 sonu | — | **0** | ⭐ %42,9'da KESİNTİSİZ tek çizgi |

```
⛔ Boşluk MONOTON DARALIR. Bir sahnede genişleyen boşluk = BLOCK.
⛔ S8'de kapanma görünmüyorsa filmin doruğu üretilmemiş demektir.
```

---

## 4. DEĞİŞMEZLİK KİLİTLERİ

```
① KAMERA         10 sahnenin 10'unda kamera hareketi = 0 kare.
                 Pan/tilt/zoom/kayma/sarsıntı hiçbir karede yok.
② ANA İSTASYON   8 ana sahnede lens 24 mm · yükseklik +34 m · mesafe 120 m ·
                 bakış 095° · tilt 0°. Sekizi BİREBİR aynı.
③ PİLON İSTASYON S1 ve S4: 35 mm · −25 m · 60 m · 095° · tilt 6° yukarı.
                 İkisi BİREBİR aynı ve ikisi de çapa ①'i taşır.
④ ÇAPA ①         çentikli kaya burnu — 10 sahnenin 10'unda, aynı şekil
⑤ ÇAPA ②         ÜÇ koyu çam, tek küme — ana sahnelerde her karede
⑥ ÇAPA ③         ikiz zirveli sırt · sol zirve sağdan YÜKSEK · ~%53,2
⑦ ÇAPA ④         eski yol — zikzak + taş köprü, 10 sahnede AYNI YERDE.
                 ⛔ Değişen tek şey ÜSTÜNDEKİ IŞIKTIR.
⑧ UFUK           %50,0 · sapma ± %2
⑨ YAPI GEOMETRİSİ ana açıklık 400 m · pilon +88 m · tabliye 22 m ·
                 kablo 22 çift/pilon · aralık 12 m — hepsi sabit
⑩ VİNÇ           montaj vinci: mast kadrajın üstünden çıkar, BOM GÖRÜNMEZ.
                 ⛔ Kadrajda görünen bir kanca = FIX [DERS 8]
```

---

## 5. MONOTON BÜYÜME VE SÖKÜM

| Geçiş | İzin verilen | Yasak |
|---|---|---|
| S0→S1 | seki kesilir | vadinin şekli değişmesi |
| S1→S2 | pilonlar tabliye kotuna | seki kaybolması |
| S2→S3 | pilonlar +88 | pilon boyunun azalması |
| S3→S4 | pier table + konsol arabası | pilonun değişmesi |
| S4→S8 | kollar uzar, kablo eklenir | kolun kısalması |
| S8→S9 | asfalt · korkuluk · aydınlatma | açıklığın değişmesi |

```
SÖKÜM SATIRI — hiçbiri klip İÇİNDE kaybolmaz:
   tırmanan kalıp    S2 kurulur → S3 SONUNDA sökülür (klip içinde, planlı)
   konsol arabası    S4 kurulur → S8 SONUNDA sökülür (klip içinde, planlı)
   montaj vinci      S1 kurulur → S8 ile S9 ARASINDA sökülür
   platform/konteyner S0 var → S9'da YOK (S8-S9 arası)
⛔ Planlı olmayan bir kaybolma = BLOCK.
```

---

## 6. GÜNEŞ KİLİTLERİ

| S | Mevsim | Azimut | Yükseklik | Gölge yönü |
|:-:|---|---:|---:|---|
| 0 | Temmuz | 176° → 268° | 66° → 8° | kuzey → doğu |
| 1 | Eylül | 214° | 48° | doğu-kuzeydoğu |
| 2 | Ekim | 224° | 34° | doğu-kuzeydoğu |
| 3 | Kasım | 230° | 24° | doğu-kuzeydoğu |
| 4 | Aralık | 236° | 12° | doğu |
| 5 | Şubat | 232° | 16° | doğu |
| 6 | Nisan | 208° | 44° | kuzeydoğu |
| 7 | Mayıs | 204° | 56° | kuzeydoğu |
| 8 | Haziran | 178° | 66° | kuzey |
| 9 | Ağustos | 268° | 20° → 8° | doğu |

```
⛔ MEVSİM TEK YÖNDE: Tem→Eyl→Eki→Kas→Ara→Şub→Nis→May→Haz→Ağu ✅
⛔ KIŞ İKİ SAHNE [DERS 7]: S5 kar BİRİKİR · S6 kar ERİR ve çamura döner.
   S6'da erime görünmüyorsa mevsim yayı kırıktır.
⛔ Gölge boyu ↔ yükseklik tutarlı olmalı: boy / tan(yükseklik).
   S4'te (elevation 12°) gölge nesne boyunun ~4,7 katı olmalı.
```

---

## 7. METİN VE İNSAN

```
EKRAN METNİ (SAHNE BLOĞU)  0,0 saniye · 0,0-60,0 arasında okunur karakter YOK
EKRAN METNİ (KAPAK KARTI)  ⭐ 60,0-65,0 arasında BAŞLIK VARDIR ve bu meşrudur
YÜZEY SAYIMI               çit · tabela · vinç · makine · konteyner · yelek ·
                           kask · kamyon · iskele · kalıp · konsol arabası ·
                           tabliye · plaka — on üçün on üçü de temiz
İNSAN                      okunabilir yüz 0 kare · hepsi bulanık iz
ARAÇ                       net duran araç yok · hepsi leke/iz
```

---

## 8. RENDER ÇUKURU

```
Her ana sahnede kadrajda AYNI ANDA en az dört şey:
   ① kaya tozu veya çamur   ② su birikintisi / ıslak leke
   ③ istiflenmiş malzeme    ④ branda / kesme artığı
S5'te ayrıca: kar GRİ, izli, yığılmış, kısmen erimiş ve kapıda kahverengi
çamura kadar açılmış. Temiz beyaz kar = FIX [DERS 7].
⛔ Temiz, düzenli, boş şantiye = emlak render'ı = BLOCK.
```

---

## 9. KURGU KAPISI

```
a) klip sayısı        10 sahne + 1 kapak kartı = 11 segment
b) sahne bloğu süresi 10 × ölçülen klip süresi (± 0,5 sn)
c) kapak kartı        5,0 sn · hareketsiz · S9'un binasının AYNISI
d) kesme içi          her klipte 0 kesme · geçiş efekti 0
e) sahne sırası       S0 → S9 → KART
f) ekran metni        sahne bloğunda 0,0 sn · kartta başlık VAR
g) ⛔ FİNAL VURUŞ     §1 — 0:57,5 · ffmpeg ile kanıtlanır
h) ⭐ KANIT ÇİFTİ     §1 — 0:05,7 ile 0:57,5 aynı ışıkta mı
i) 120 PX TESTİ       kapak (siluet + kelime) ve S0'ın 0. karesi (boş vadi)
j) müzik hizası       160 BPM · 4 ölçü/sahne · kesmeler ölçü başında
k) ihraç              1440p+ · BT.709 · 48 kHz · −14 LUFS · −1,0 dBTP
l) AI beyanı          açıklamanın son satırı (İngilizce) + platform beyanı
```
