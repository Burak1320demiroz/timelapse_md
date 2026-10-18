# 💧 SU VE YANSIMA KILAVUZU — su filmin saati olduğunda

> Su bu depoda en sık tekrar eden ve en çok bozulan ögedir: fırtına kabarması (TIDE GATE) · batırılan
> kutu (LAST HARBOR) · su alıp gemiyi yüzdüren havuz (EDEN ARK) · dolan kilit (EMPTY LOCK) · taşkın
> (OVER THE WALL · IRON BRIDGE) · sel ve gölet (THE SLOW TAKEOFF). Bu kılavuz suyun **kotunu, yönünü,
> yansımasını, rengini ve üstündeki hareketi** sayıya bağlar.
>
> Kaynak: A27 · 07.10.2026 (`arastirma/SONUCLAR/A27_GEMINI_HAM.md`) · denetim `A25-A29_DENETIM.md` §3.
> ⭐ Rapordan inen: **yansıma geometrisi** x = D·h/(h+y) (bu makinede yeniden hesaplandı — tablo birebir
> tuttu) · **Fresnel**: dik bakışta %2, sıyırma açısında →%100 (n = 1,333 · Hale & Querry 1973 ✅) ·
> Brewster ≈ 53° · rüzgâr–eğim ilişkisi (Cox & Munk 1954 ✅) · bulanık taşkın suyunun opak ve kahve
> okunması · tanık çizgi (silt bandı) · **kano hızı** 4 / 6 / 8 km/sa → 8 sn'de 8,9 / 13,3 / 17,8 m.
> ⛔ İnmeyen: "dalgacık 2–3 m/s'de başlar" (Beaufort'a göre pul dalgacık Kuvvet 1'de, 0,3–1,5 m/s ✅) ·
> VideoPhy-2 "%47,7" (gerçek en iyi %32,6 · zor alt kümede %22 ✅) · Physics-IQ "diğerleri < %45"
> (zirve 64,5 doğru, 2.–6. sıra %56–63) · taşkın yükselişi "2–5 cm/sa" (kaynaksız) · çayır infiltrasyonu
> "14,7 cm/sa" (kaynak bir arama sayfası) · raporun rejim ifade tablosundaki "jump-cut water level rise" ·
> "fast-sweeping harsh sunlight glare" (sıçrama ve parlama DAVET eder — §5).

---

# 0. 🚪 KURAL

```
Su bir YAPI ELEMANIDIR: kotu her karede yazılır, kendiliğinden gelmez, kendiliğinden gitmez.
  · kot SABİT bir nesneye göre kesirle yazılır ("touches one third of the height of the near column")
    ve SU KOTU DEFTERİ'ne (§8) girer — kare kilidi [P10-e]
  · su bir YÖNDEN gelir ve o yöne çekilir; yükselme ve çekilme AYRI kliplerdir, ikisi de kademeli
  · en yüksek kot kalıcı bir TANIK ÇİZGİ bırakır (silt bandı, ıslak iz) ve sonraki her karede o
    yükseklikte kalır [P10-g · TIDE GATE]
  · yansıma GEOMETRİDEN gelir (§1): görünmesi isteniyorsa su o mesafeye kadar uzanır
  · ⛔ su gelmeden önceki karelerde durgun su YOK — ıslak beton + su "havuz" okunur [DERS 54]
  · su üstündeki taşıtın yolu HESAPLANIR (§7); kadrajda KALIR
```

Ölçülmüş bedeli (arşiv · 12 mercek):

| film | ne oldu | hangi kural yoktu |
|---|---|---|
| OVER THE WALL | nehir tek karede kurudu; ıslak beton + nehir "havuz" okundu | kademeli çekilme · DERS 54 |
| THE DEEP STEP | taban suyu saydamlıktan kaynayarak belirdi ("en kötü eriyen") | su bir yönden gelir |
| THE MOUNTAIN CROWN | su açılınca ışık günbatımından öğleye sıçradı; su makinelerin üstüne döküldü | ışık zinciri suyla da sürer |
| THE IRON BRIDGE (yatay) | taşkın klibinde kemer silindi, 4 sn sonra sıfırdan kuruldu | yapı su altında da "unchanged" |
| BACK TO WATER | tekne finalde kadrajdan çıktı (döngü 3/10) | taşıt rotası |
| ✅ THE TIDE GATE | su kotu her karede yazılı, taşkın çizgisi tanık nesne — iyi okundu | — |

---

# 1. 🪞 YANSIMA GEOMETRİSİ — kamera yüksekliği nereyi görür

Sakin su bir aynadır. Nesnenin bir noktasının yansıması, kameraya **x** mesafesindeki suda görünür:

```
   x = D · h / (h + y)          h = kameranın SU YÜZEYİNDEN yüksekliği · y = noktanın su yüzeyinden yüksekliği
                                D = noktanın kameraya yatay mesafesi
   kadrajda yeri (24 mm · 16:9 · tilt 0):   ufkun ALTINDA  118,5 · (h + y) / D   yüzde      (dikey 9:16'da 66,7)
   suya değen tabanın yansıması x = D'de, ufkun 118,5·h/D altında
   ⭐ YÜKSELTİLMİŞ nesnenin ALT kenarı da x = D·h/(h+y_alt)'ta yansır — tabanı suda değilse yansıması D'ye uzanmaz
```

Tablo (bu makinede hesaplandı — rapor tablosuyla birebir; y = 10 m, nesnenin tabanı suda):

| h (kamera) | D | yansıma su bandı | ufkun altında | kadrajda |
|:-:|:-:|---|---|---|
| 2 m | 30 m | 5,0 – 30 m | %7,9 – %47,4 | ✓ |
| 2 m | 50 m | 8,3 – 50 m | %4,7 – %28,4 | ✓ |
| 2 m | 100 m | 16,7 – 100 m | %2,4 – %14,2 | ✓ (ince) |
| 3 m | 30 m | 6,9 – 30 m | %11,8 – %51,4 | tepe kadraj dışı |
| 3 m | 50 m | 11,5 – 50 m | %7,1 – %30,8 | ✓ |
| 3 m | 100 m | 23,1 – 100 m | %3,6 – %15,4 | ✓ (ince) |
| 5 m | 30 m | 10,0 – 30 m | %19,8 – %59,2 | tepe kadraj dışı |
| 5 m | 50 m | 16,7 – 50 m | %11,8 – %35,5 | ✓ |
| 5 m | 100 m | 33,3 – 100 m | %5,9 – %17,8 | ✓ |
| 10 m | 30 m | 15,0 – 30 m | %39,5 – %79,0 | tepe kadraj dışı |
| 10 m | 50 m | 25,0 – 50 m | %23,7 – %47,4 | ✓ |
| 10 m | 100 m | 50,0 – 100 m | %11,8 – %23,7 | ✓ |

⭐ **Çalışılmış örnek — THE SLOW TAKEOFF** (kamera çayırdan 3,0 m · gölet −0,3 → h = 3,3 · D = 50):

```
   gövde altı +6,0 (y 6,3)  → x 17,2 m · üstten 786 px
   gövde üstü +9,8 (y 10,1) → x 12,3 m · üstten 883 px
   kuyruk tepesi +16,5 (y 16,8) → x 8,2 m · üstten 1054 px — gölet 10 m'den başladığı için YANSIMAZ
   ⇒ gölet kameraya 12 m'ye kadar uzanmasaydı ışıklı gövdenin yansıması hiç görünmeyecekti; plan bu yüzden
     değişti (SAPMA ④). İlk yazımda 794–891 yazılmıştı — denetimde düzeltildi.
```

```
KURAL    "the pond mirrors the house" yazmadan ÖNCE hesap: x bandı suyun içinde mi?
         değilse: (a) su kameraya doğru uzar · (b) kamera alçalır · (c) yansıma prompttan ÇIKAR
⛔       yansımayı suyun olmadığı yere yazmak (çimen, çamur) — model ya suyu uydurur ya yansımayı
```

---

# 2. 🌊 FRESNEL VE DALGACIK — ayna ne zaman ayna

```
YANSITIRLIK  dik bakışta ≈ %2 · sıyırma açısında → %100 (n = 1,333)        [Hale & Querry 1973 ✅ · hesap]
             Brewster ≈ 53° (bu açıda p-polarize yansıma 0)                  [hesap ✅]
             tilt 0 kadrajda: uzak su (ufka yakın) ayna gibi gökyüzünü yansıtır; yakın su suyun KENDİ rengini,
             bulanıklığını ve dibini gösterir → yakın suda yansıma her zaman daha soluktur
DALGACIK     pul görünümlü dalgacık Beaufort Kuvvet 1'de (0,3–1,5 m/s) başlar; Kuvvet 2'de (1,6–3,3 m/s)
             küçük dalgalar — ayna yansıma dağılır, dikey ışık sütunlarına döner [NOAA Beaufort ✅]
             eğim varyansı rüzgârla doğrusal artar: σ² = 0,003 + 5,12·10⁻³·U (temiz yüzey) [Cox & Munk 1954 ✅]
YAZIM        ayna yansıma isteniyorsa:   "the water is calm and glassy, without wind"
             ışık sütunu isteniyorsa:     "a light breeze ruffles the surface into small ripples"
             ⛔ ikisini aynı karede yazmak (ayna + dalgacık) — model birini seçer, kare kareye değişir
```

---

# 3. 🟤 SU TÜRÜ — berrak, bulanık, ıslak beton

| su | görünüş | yansıma | karışma riski | yazım |
|---|---|---|---|---|
| berrak göl/deniz | mavi-yeşil, derinlik okunur | güçlü (uzakta) | gökyüzü, cam | "clear lake water" |
| taşkın / sel | opak, kahve-sarı, dip görünmez | zayıf, matlaşmış | **ıslak beton, çamur** | "opaque brown-grey floodwater with drifting twigs and foam lines" |
| yağmur birikintisi | ince, parlak, kenarı düzensiz | gök lekesi | ıslak asfalt | "a thin puddle in the tyre rut" |
| ıslak beton (SU DEĞİL) | koyu gri, mat, kalıp kenarlı | yok | **su, havuz** | "dry matte light-grey concrete" — su gelmeden önce kuru yazılır [DERS 54] |

⚠️ "Islak beton ve bulanık su aynı spektral dağılımda, model sınırı kaybedince birleştirir" raporun
kendi çıkarımıdır [A27-c · VARSAYIM]; bizim ölçümümüz (OVER THE WALL) sonucu doğrular, mekanizmayı değil.

---

# 4. 🏞️ HİDROLOJİ — taşkın nasıl gelir, nasıl gider

```
YÖN          su bir kaynaktan gelir (göl kıyısı · nehir · savak · kapı) — kaynağı ilk karede kadrajda olur;
             kıyı çizgisi kaynağın tarafından ilerler (THE SLOW TAKEOFF: sağ arkadan, kayıkhane kazıkları)
HIZ          yükselme ve çekilme hızının tipik sayısı BİLİNMİYOR (rapordaki 2–5 cm/sa kaynaksız) — film
             mertebe anlatır: yükselme bir klip, doruk bir klip, çekilme bir klip (en az üç kare: başlangıç ·
             doruk · geri çekilmiş) [P16-c iki yönlü]
             çekilme yükselmeden YAVAŞ okunur: geride ıslak kalan çukur, silt çizgileri, sürüklenmiş dal
TANIK ÇİZGİ  doruktan sonraki her karede, sabit nesnelerin (kolon dibi · kazık · duvar) aynı yüksekliğinde
             soluk silt bandı — "a faint silt stain low on the columns" [P10-g]
YAPI         su altındaki ya da suyun çevrelediği yapı "unchanged" yazılır, HOUSE/YAPI cümlesi birebir
             [IRON BRIDGE dersi]; ev, köprü, kemer su klibinde yeniden TARİF EDİLMEZ, aynen tekrarlanır
IŞIK         su girince ışık değişmez: KARE TABLOSU'nun saati aynen sürer [MOUNTAIN CROWN dersi]
```

---

# 5. ⏩ REJİM BAŞINA SU — ekranda ne görünür

> Bir karenin temsil ettiği gerçek süre: A (10 dk / 240 kare) = **2,5 sn** · B (2 sa / 240 kare) =
> **30 sn** · G = gerçek zaman. Uzun pozlamayla çekilmiş "ipek su" görünümü gerçek timelapse
> pratiğidir (ND filtre, 1–2 sn pozlama [A27-f · İDDİA, fotoğraf pratiği]).

| konu | A (≈75×) | B (≈900×) | G (1×) |
|---|---|---|---|
| yüzey | "the water surface is smoothed to a soft sheen" | "the water lies flat and glassy, its level changing steadily" | "small natural ripples move across the water" |
| yükselen kot | "the water line climbs the near columns steadily, never dropping" | "the water spreads across the low meadow in one slow sheet" | — (gerçek zamanda kot görünür değişmez) |
| çekilme | "the water line slides back, uncovering wet grass and silt lines" | aynı, daha geniş | — |
| yağmur | "dark wet patches spread across the ground; puddles grow in the ruts" | "the ground darkens under the rain and dries again in bands" | "distinct raindrops ring the puddles" |
| yansıma | "the reflections soften and shift with the clouds" | "the reflections hold still as the light changes" | "the reflections tremble in the ripples" |
| taşıt | iz ("the boat leaves a faint streak of wake") | taşıt yazılmaz (görünmez hızda) | "glides at a slow even pace, its wake spreading in two thin lines" |

⛔ Yazılmaz: "jump-cut water level rise" (sıçrama ister) · "fast-sweeping harsh sunlight glare" (parlama
ister) · "boiling water" (kaynama — DEEP STEP arızası) · "the water appears" (belirme fiili [DERS 61]).

---

# 6. 🤖 YAPAY ZEKÂNIN SUYLA BİLİNEN ARIZALARI

| arıza | bizde ölçülen | ölçülmüş genel durum | önlem |
|---|---|---|---|
| su belirir/kaybolur, kaynar | DEEP STEP · OVER THE WALL | fizik benchmark'larında akışkan/sıvı en zayıf alanlardan [VideoPhy-2: en iyi model %32,6 · zor alt kümede %22 ✅] | kot defteri · kaynak + yön · "never dropping" |
| kot karede zıplar | OVER THE WALL (4 kez kar/su) | — | kesirli kot + tanık çizgi [A27-d] |
| boşalan su SİLİNİR, tabanda gider deliği belirir | POOL ROOM S0 (2→3 sn) [DERS 93] | — | ara kot keyframe'i (G1'de sığ su) · rıht rıht inen su çizgisi · tabanın kesintisiz çini tarifi (pozitif) |
| görünmeyen hazneye dolum → su görünen zemine fışkırır, hazne avluda açılıp kapanır | RAIN TOWER S1–S2 (eşik arkasındaki çukur, tilt 0) [DERS 95] | — | hazne iki uç karede ≥ 40 px görünür ya da dolum yalnız görünen taşıyıcıyla (eşik üstünde yükselen koyu bant) yazılır |
| su gelince ışık değişir | MOUNTAIN CROWN | — | KARE TABLOSU saati birebir |
| su gelince yapı silinir | IRON BRIDGE | — | yapı cümlesi birebir, "unchanged" |
| taşıt eylemsizliksiz kaçar | BACK TO WATER | Physics-IQ: en iyi modeller ~%57–64 (2026 tablosu) · özgün 2025 makalesinde en iyi ~%29,5 ✅ | rota hesabı (§7) · "without ever leaving the frame" [VARSAYIM] |
| yansıma sahneyle tutmaz | — (ölçülmedi) | PhyGenBench: 27 yasa · en iyi Gen-3 0,51 ✅ | yansıma keyframe'de çizilir (önce usta kare) |

⚠️ Raporun mekanizma adları ("temporal denoising failure" · "conditional collapse" · "momentum
hallucination") açıklayıcıdır, ölçülmüş değil [A27-f · VARSAYIM].

---

# 7. 🛶 SU ÜSTÜNDE TAŞIT — yol hesaplanır

```
HIZ (kano)   hafif 4 km/sa = 1,11 m/s → 8 sn'de 8,9 m · normal 6 km/sa = 1,67 m/s → 13,3 m · güçlü 8 km/sa → 17,8 m
             sprint üst sınırı ≈ 4 m/s (yarış) — film için kullanılmaz   [A27 · spor bilimi/blog · aritmetik ✅]
KURAL        G (gerçek zaman) klibinde taşıtın yolu ≤ 13 m; daha uzun rota iki klibe bölünür ya da kısaltılır
             (THE SLOW TAKEOFF: iskele → gövdenin altı → su yolu ağzı, 2 × ≈13 m — göle VARMAZ, göle dönük durur)
KADRAJ       son karede taşıt kadrajın İÇİNDE (x, y, px boyu PLAN'da) [BACK TO WATER dersi · P25-c]
KAYNAK       taşıt önceden kadrajda: bağlı, yanaşmış ya da taşınırken görülmüş [P24-e]
İZ           G'de iki ince dümen suyu çizgisi, yansımayı kırar; tutuşta yavaşça söner
YASAK KELİME uçak/su filmlerinde "floats · seaplane · landing" — taşıt "lies on / sits on the water" [DERS 59]
```

---

# 8. 📒 SU KOTU DEFTERİ — kare başına (su olan her filmde PLAN'a)

| kare | sabit nesneye göre kot (kesir) | kadraj yüzdesi | durum | tanık çizgi |
|:-:|---|:-:|---|---|
| G<n> | ⬜ (ör. "near column: water at one third of its height") | %⬜ | yükseliyor / doruk / çekiliyor / sabit | ⬜ (ör. "silt band at 0,4 m on every column") |

Örnek — THE SLOW TAKEOFF:

| kare | kot | durum | tanık |
|:-:|---|---|---|
| G0–G19 | göl kendi kıyısında; çayırda durgun su YOK | sabit | — |
| G20 | su sağdan çayıra girdi, çukurun uzak kenarında | yükseliyor | — |
| G22 | bütün alçak çayır, kolon dipleri, kamera sırtının dibi | doruk | silt bandı başlar |
| G23 | çukur + önündeki alçak alan ıslak havuz | çekiliyor | kolon diplerinde silt bandı |
| G24–G30 | gölet −0,3 m + su yolu, göl kotunda | sabit (yeni yapı) | silt bandı aynı yükseklikte |

---

# 9. ✅ KONTROL LİSTESİ (ihlalde TEK eylem)

| # | madde | ihlal → eylem |
|:-:|---|---|
| 1 | su olan her karede kot sabit bir nesneye göre kesirle yazılı | → KOTU YENİDEN YAZ |
| 2 | suyun kaynağı ve yönü ilk karede kadrajda | → SAHNEYİ YENİDEN TASARLA |
| 3 | yükselme · doruk · çekilme ayrı karelerde | → SAHNE EKLE |
| 4 | su gelmeden önceki karelerde durgun su ve "ıslak" beton yok | → KAREYİ YENİDEN ÜRET |
| 5 | yapı su klibinde birebir aynı cümleyle ("unchanged") | → BLOĞU YENİDEN YAZ |
| 6 | ışık saati su gelince değişmiyor | → KAREYİ YENİDEN ÜRET |
| 7 | doruktan sonra tanık çizgi her karede aynı yükseklikte | → KOTU YENİDEN YAZ |
| 8 | yansıma yazıldıysa §1 hesabı yapıldı ve su o banda uzanıyor | → ROTAYI/GÖLETİ DEĞİŞTİR ya da yansımayı çıkar |
| 9 | ayna ile dalgacık aynı karede yazılmadı | → BLOĞU YENİDEN YAZ |
| 10 | G klibinde taşıt yolu ≤ 13 m ve son karede kadrajda | → ROTAYI KISALT |
| 11 | taşıtın kaynağı önceden kadrajda | → SAHNE EKLE |
| 12 | "appears · boiling · jump · glare · floats" kelimeleri yok | → KELİMEYİ ÇIKAR |

---

# 10. 📎 İNMEYENLER

```
⛔ dalgacık eşiği 2–3 m/s          Beaufort Kuvvet 1 (0,3–1,5 m/s) — rapor muhtemelen knot ile karıştırdı
⛔ VideoPhy-2 %47,7                 yok; %32,6 / %22 ✅
⛔ Physics-IQ "diğerleri < %45"     yanlış; 2026 tablosunda 2.–6. sıra %56–63
⛔ taşkın 2–5 cm/sa · infiltrasyon 14,7 cm/sa   kaynaksız / alakasız
⛔ "Snippet 57 · Özel Optik Hesaplama"         kaynak değil — formül ders kitabı geometrisidir, burada hesaplandı
⛔ raporun SLOW TAKEOFF yorumu      "17 m göletin bittiği yer" dedi — yanlış: 17,2 m gövde ALTININ yansımasıdır
⚠️ ND / 1–2 sn pozlama "ipek su"    fotoğraf pratiği [İDDİA] — prompt dilinde "soft sheen" kullanılır, kamera
                                    ayarı yazılmaz
```
