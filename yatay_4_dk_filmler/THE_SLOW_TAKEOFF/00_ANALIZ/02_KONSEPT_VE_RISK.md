# 🧠 THE_SLOW_TAKEOFF — KONSEPT VE RİSK

> Girdi: `00_HIKAYE_ONAYI.md` (onaylı 07.10.2026) + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.
> Bu dosya onaylı hikâyeyi İYİLEŞTİRİR, değiştirmez; bozulan yerler 00_HIKAYE_ONAYI SAPMA ①–⑧'de.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI

```
① KONU:       ajan önerdi (TUR 1: uçaktan göl evi), sahip yeniden yazdı (TUR 2). Gerekçe: C2-e — var olanı dönüştürmek
              sıfırdan inşadan iyi okundu (④ ≈7,8 · ≈6,2; değerlendirici yargısı, izleyici verisi DEĞİL); iki yatay film
              "bitmiş yapı durur" finaliyle düştü (GLASS WALL · IRON BRIDGE) → bu filmde final ÇALIŞIR (ışık + kano)
② FORMAT:     yatay_4_dk_filmler → KILAVUZ_REHBERI §2.8 · 30 sahne · 2 bölüm (S0–S14 · S15–S29) · QA birimi FİLM (tek master × 5 mercek)
③ SAHNE:      30 × 8,0 — ⚠️ bandın dışı (modül 24 × 10,0); sahip senaryosu 07.10.2026 ("30 klip × 8 saniye")
④ YAPI KARTI: kart YOK → §10 şablonuyla aşağıda §2a. Emsal: LAST LIFT (strand jack, rejim A kaldırma) · QUIET FIELD
              (tandem beşik) · EDEN ARK (dönüştürülmüş taşıt). SÜRE ≈10 ay → 30 satır ara hâllerle
⑤ SAHA KARTI: kart YOK → §3.7 şablonuyla aşağıda §2b (kırsal §3.2 + kıyı §3.3 + kar §3.5). Mevsim taşıyıcısı meşe yaprağı ·
              korpus "documentary site photograph on colour negative film" [DERS 34]
⑥ ARAÇ:       bilinmiyor — kutu seti ÖLÇÜLMEDİ; 8,0 sn teslim için {5,9} ya da {5,10} gerekir; kokpit için ikinci referans
⑦ HİKÂYE ONAYI: ONAY ✅ 07.10.2026 · TUR 2/3
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "planı güncelle ve yap" + yapıştırılan senaryo (THE SLOW TAKEOFF — 16:9, 4 dakika, 30 × 8 saniye; "uçak artık
        00:40'ta yerden kalkmaya başlıyor; finalde ise eskiden yattığı yerden bir kano geçiyor") + kamera seçimi
        "Tek kamera + 2 kokpit (Önerilen)"
```

| sahibin isteği | fiziksel / inşa / format sorunu | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| dört kamera (A · B · C · D) | sabit kamera + kare zinciri formatın kendisidir; açı değişimi her kesmede zinciri kırar | B ve D ana kadraja; C'nin ikisi (S13 · S21) kokpit istasyonu; dördü dışarıdan vekil | sahip seçimi 07.10.2026 · HİKÂYE SAPMA ②③ |
| iç mekân dönüşümü (4 klip) | kabin penceresi ana kadrajda ≈8 px — iç ilerleme OKUNMAZ [A5-c · P2-g] | yalıtım, mutfak, yatak: eksilen palet/sandık + merdiven ve kanat kapısı trafiği; kokpit köşesi kokpit kamerasında | SAPMA ③ |
| kokpit klibi senaryoda 15. sırada (mutfaktan sonra) | birinci bölüm S14'te biter; kokpit S14 olursa sınır karesi iki kameraya bölünür [DERS 52] | kokpit S13, mutfak S14 | SAPMA ⑧ |
| "Su sağ arkadaki gölden çayıra" + finalde yansıma | 3 m'lik kameradan gövdenin altındaki dar gölet evi yansıtamaz (yansıma kameraya yakın sudan gelir) [P25-b] | gölet gövdenin altından kameraya doğru genişler (D 10 → 55 m); yansıma bandı üstten 786–883 | SAPMA ④ |
| "Sonbahar, kış, bahar aynı gün gibi gösterilmez" | kesmede ışık atlamaz (§2.7 ①) — ışık tek gün olmak zorunda | ışık 07:40 → 19:20 tek gün; mevsim meşe, kar, yağmur, su ve gökle; kış/bahar klipleri kapalı gök | SAPMA ⑤ · ÜSLUP BEYANI |
| kışta "pencerelerde hafif sıcak ışık" | final ışık anını önceden tüketir [P11-d] | tek pencere: kokpit lambası | SAPMA ⑥ |
| kano "göle bağlı geçitten" | canlı ödülün kaynağı önceden kadrajda olmalı [P24-e] | kano S25'te kamyonla gelir, telehandler suya indirir | SAPMA ⑦ |
| "Kano aynı yönde açık göle ilerler" (S29) | gerçek hızda kano 8 sn'de ≈10–13 m gider; gövdenin altından açık göle (≈45 m) tek klipte varamaz [P6-f] | S28 iskele → gövdenin ortası · S29 → su yolu ağzı, göle dönük durulur; kadrajda KALIR | DERS hasadı P6-f |
| "Son sekiz saniye normal hızda" | rejim G → üçüncü rejim (A · B · G), SANTIYE §2 sınırı iki | beyanlı: G yalnız S28–S29, geçiş kesmede | PLAN §REJİM SAYISI |
| ayrı 5 sn afiş yok | yatay iskelet kart öngörür | KAPAK KARTI ⛔ YOK · 240,0 sn (BORROWED HILL emsali) | TESLİM YAPISI |
| başlık "They Lifted an Abandoned Plane Into a Lake House \| AI Timelapse" | kanal kuralı ≤ 40 karakter (63) | sahip başlığı korunur, ≤40 üç seçenek yazıldı | YAYIN_PAKETI |

## 2. 🚪 KONSEPT KAPISI — VAAT / DİRENÇ / BEDEL [KILAVUZ_REHBERI §6]

```
VAAT      Göl kıyısında çürüyen bir yolcu uçağını bütünüyle yerden kaldırıp altında su, üstünde hayat olan bir göl
          evine dönüştürmek. (Video başlamadan önce de var olan iş: terk edilmiş uçak, kaldırılacak yük.)        ✅
DİRENÇ    ① ağırlık  ② su (taşkın alanı)  ③ çürüme  ④ kış — ekranda: S5–S6 gergin halatlar, çamurdan kopan gövde ·
          S19–S20 sağdan yürüyen su, kolon dipleri · S1 şerit şerit sökülen sarmaşık · S18 kar [P1-b]                ✅
BEDEL     çamurlu yatağında yatan ölü uçak — G0'da gövde altı üstten 617 (çayırda, ≈%43); usta karede (G30) orada su +
          yansıma; gidiş S5 (40,0 sn), su altına S20, gölete S23                                                  ✅
KANAL TEZİ  ne kayboluyor: çamurlu yatak + ölü gövde · kadrajda: 154 px kalkış, alt %43 bandı · cevap "zaman geçiyor"
          değil: "yattığı yer su oldu"                                                                              ✅
DÖRT TEST   ① tek kare ✅ (yerde mi havada mı · çerçeve · teras · su · kano) ② kinetik ✅ (her klipte makine/su/kano)
            ③ başlık ✅ (kapak 3 kelime; ⚠️ platform başlığı 63 krk) ④ omurga ✅ (30 vuruş — PLAN)
```

### 2a. 🧱 YAPI KARTI — UÇAK KALDIRMA / DÖNÜŞÜM (YAPI_TIPI_KARTLARI §10 şablonu · bu film için)

```
İNŞA SIRASI   motor sökümü → temizlik → temel (4) → çelik çerçeve (2 × 2 kolon + kiriş) → semer + halat → KALKIŞ (iki
              aşama) → yük aktarımı (pim) → teras çerçevesi → döşeme → merdiven → cam → iç (yalıtım · kokpit · mutfak ·
              yatak) → korkuluk + lamba → kaldırma donanımı sökümü → (kış · sel) → gölet + su yolu → bahçe → iskele + kano
SÜRE          ≈10 ay (yaz sonu → yaz başı); kalkışın kendisi yarım gün (strand jack ≈6–10 m/sa)
MAKİNE        sarı mobil teleskopik vinç (yalnız motor + çerçeve + semer) · 4 strand jack · telehandler · ekskavatör ·
              mikser · kazık makinesi · iki iş platformu · iki iskele kulesi · küçük yükleyici · pompa · damperli kamyon
KADRAJ        tek ana istasyon, gövde yandan; kokpit istasyonu iki klip (detay)
DİRENÇ        ağırlık (tek parça kalkış) · su (taşkın alanı) · çürüme · kış
RİSK          (stadyum §5) kaldırma anı tek seferliktir, doruk, ayrı sahne — burada iki ara kare (G6 · G7) ·
              (türbin §8) DERS 55 çoğalır → tek uçak kilidi; DERS 56 hareket fiili parçadan yapıya sıçrar; DERS 57
              kaldırma pop eder → her kaldırma bir ara kare · (baraj §4) su seviyesi kademeli; hangi çapanın su altında
              kalacağı yazılı (kolon dipleri, kayıkhane kazıkları); alçak düz platform + ıslak yüzey havuz okunur [DERS 54]
```

### 2b. 🌾 SAHA KARTI — GÖL KIYISI ÇAYIRI (SAHA_VE_IKLIM_KARTLARI §3.7 şablonu)

```
IŞIK          ılıman 47° K · tek gün 07:40 → 19:20 · kamera kuzeye bakar, güneş hiçbir karede kadrajda değil
TEK KİRLİLİK  çamur (G0 yatağı · S2 temel · S19–S22 sel) — S19'dan önce durgun su YOK
ÇAPALAR       meşe (sol) · kayıkhane (sağ, kanıt) · karşı kıyı + tepe sırtı (uzak) · kaya (sağ alt) — dört, üç bantta [P14-b]
HAVA RİTMİ    yaz sabahı sisi → güz açık gök → kapalı gri → kar → yağmur, kırık bulut → altın akşam → mavi saat
ZAMAN NESNESİ meşe yaprağı (yeşil → altın → bronz → kahve → çıplak → yeşil pus → tam yaprak) · çayır rengi · su kotu ·
              silt çizgisi (G22 → G30)
NEGATİF EK    "The meadow holds exactly one aircraft…" · kıyı ekinin "no boats appearing" maddesi TERS: kano beyanlı ödüldür
              (S25'ten sonra), başka tekne yok — negatifte TEKNE ADI GEÇMEZ [DERS 59]
RİSK          (kırsal) ufuk kayar → ufuk = karşı kıyı çizgisi, her I2V'de %50 · (kıyı) su seviyesi karede oynar → su kotu
              kare kilidi · (kar) kartpostal kar → izli, ince, gri kar + çalışan araç
```

## 3. 🎥 KAMERA HESABI — 16:9 [KILAVUZ_REHBERI §2.8 · KAMERA_ISTASYONU §3 · DERS 38]

```
GİRDİ      H = 16,5 m (kuyruk tepesi, kalkış sonrası) · h = 3,0 m (çayırın güneyindeki alçak çimen sırtında beton kaide) ·
           hedef taç %82
D          = (H − h)/0,27 = 50,0 m (gövde eksenine) → arada çayır; görüş açık · D_kenar = 35,5 m (yakın kanat ucu)
YÜZDE(y)   = 50 + 118,5·(y − h)/D → gövde altı %42,9 → %50,0 (G6) → %57,1 · kuyruk %67,8 → %82,0 · kayıkhane %45,1–52,8
           (≈ 1280·10/85 = 150 px en)
YANLAR     x(m) → %50 + 66,7·x/D → meşe (SOL) x −28 m, D 45 → %8,5 · kayıkhane (SAĞ) x +44, D 85 → %84,5 · uçak %28,0–72,0
GÖLGE      kamera bakışı 0° · güneş 100° → 293° → gölge sabah sola-uzağa (−80°), öğle uzağa, akşam sağa-yakına (+113°)
KALDIRMA   vinç bom başı ≈+15 m → %78 → GÖĞE karşı (S3 üst kiriş) — kısa sapan, kabul edilen risk [DERS 22]; gövdeyi
           vinç değil kirişteki jack'ler kaldırır (kancasız kalkış)
⭐ DORUK ÇİZGİSİ [P4-b]: h = 3,0 m seçildi ki G6'da (gövde altı +3,0) gövdenin altı tam KARŞI KIYI ÇİZGİSİNE oturur (%50):
           önce çizginin altında (çamurda), sonra üstünde (havada) — kalkış görünür bir çizgiyi geçer
YANSIMA    gölet −0,3; ayna noktası y' = −0,6 − y · ışın suya D_su = D·(h+0,3)/(h − y') → gövde altı → D 17,2 (üstten 786) ·
           gövde üstü → D 12,3 (883) · kuyruk tepesi → D 8,2 (1054 — gölet 10 m'den başladığı
           için yansımaz) → gölet kameraya D ≈ 10 m'ye kadar uzanır (SAPMA ④) · ⭐ 07.10.2026 A27 denetimi:
           ilk hesapta kadraj yüzdesinde (y′ − h) yerine (y′ − h − 0,3) alınmıştı → 794–891 yazılmıştı, düzeltildi
KANO       5,0 m · D 40–50 → 160–128 px · G'de 8 sn ≈ 13 m → G28 (x 608) → G29 (960) → G30 (1293)
KOKPİT     h 8,2 m · bakış 270° · ön cama 2,4 m · altı cam ≈1500 px · meşe tacı sol camlarda (≈10 m) · tepe sırtı
⛔ ÖN GÖRSELLEŞTİRME: betikle (scratchpad geo2.py) — kamera · gövde · çerçeve · çapalar · ufuk · gölet · yansıma · kano;
           sayılar PLAN §DEĞİŞMEZLER ve SPEC §2'de
```

## 4. 🏗️ VİNÇ / GEÇİCİ EKİPMAN KARARI [DERS 1 · 8 · 22 · 46 · 48 · 57]

```
GEÇİCİ EKİPMAN  sarı mobil vinç (G0–G4) · 4 strand jack + halat (G4–G17) · 2 iş platformu · 2 iskele kulesi (G11–G17) ·
                telehandler · kamyonlar · kum torbaları (S19–S22) — DEĞİŞMEZLER'e GİRMEZ [DERS 1]
KANCA           yük hep görünür: G0 motor · G1 motor (kamyon üstünde) · G3 kolon · G4 semer; G2 ve G5'ten sonra vinç YOK;
                S1 ve S4'te bomunu toplayıp kadrajdan çıkar · bom kadraj dışından sarkmaz [DERS 46]
KALKIŞ          vinçsiz: dört gergin halat, iki semer; G5 gergin (yerde) → G6 +3,0 → G7 +6,0 → G8 pimli; yalnız düşey [DERS 57]
KAYNAK          her eleman bir önceki karede istifte (PLAN §Malzeme kaynağı) [DERS 48]
SÖKÜM           S1 vinç + kamyon · S4 vinç · S17 jack + halat + iskele kuleleri (telehandler, işçiler) · S22 kum torbaları ·
                S25 kamyon + telehandler — usta karede hiçbiri YOK; çerçeve, semer, teras, merdiven KALICI
```

## 5. ☀️ IŞIK GÜNÜ VE TAKVİM [ZAMAN_VE_ISIK §2 · §6 · §7 · SANTIYE_HAREKETI §1]

```
IŞIK GÜNÜ   07:40 → 19:20 · Σ pencere = 22×A (10 dk) + 4×B (2 sa) + 2×G (8 sn) = 11 sa 40 dk ≤ 14 ✓
            (kokpit ekleri S13 ∥ S12 · S21 ∥ S20 toplama girmez; kesmede ışık atlamaz [§2.7 ①])
TAKVİM      yaz sonu → yaz başı (≈10 ay) · taşıyıcı: meşe yaprağı · KIŞ S18 + S19 [DERS 7 · 21] · mertebe cümlesi:
            "bir sonbahar, bir kış, bir bahar seli" [P1-c] · ÜSLUP BEYANI (OLD ROAD): takvim tek günün ışığına sıkıştırıldı
GECE        yok · mavi saat S26–S30 (sahip kararı) · final zifirde bitmez [DERS 45]
GÜNEŞ DİSKİ hiçbir LIGHTING bloğunda anılmaz [DERS 39] · gölge G(n)↔G(n+1) farklı [DERS 32 · 47] · S21 kokpitte güneş
            bakış yönünde (280°) → "hidden behind the dark rain clouds"
```

## 6. ⚠️ RİSK — yapı kartının RİSK satırları + bu deponun tekrar eden arızaları

| risk | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| kalkışta gövde pop eder / kopyalanır [DERS 57 · EMPTY RIDGE] | ✅ | 33 m tek rijit yük | iki ara kare (G6 · G7), salt düşey, aynı x, PİLOT ② | 🟠 |
| istasyon kesmesi ❶ SEPARATE IMAGES [DERS 52 · OVER THE WALL] | ✅ | iki kokpit klibi | ortak çapa cümleleri, dış kare iki yakada aynı, beyan SPEC künyede | 🟠 |
| taşkında yapı geriler [IRON BRIDGE 00:51] | ✅ | S19–S22 su | her sel karesinde HOUSE birebir; PİLOT ③ | 🟠 |
| okunur yazı/logo gövdede [EMPTY LOCK · LAST LIFT] | ✅ | uçak korpusu işaretlidir | 'on any surface' + pozitif tek boya cümlesi; YASAK: livery · registration · airline | 🟡 |
| ikinci uçak / mezarlık [DERS 55] | ✅ | uçak korpusu çoğul | "exactly one aircraft" 33 görselde | 🟡 |
| deniz uçağı / suya iniş korpusu [P23-b] | ✅ | aircraft × lake × flood | YASAK: seaplane · floats · landing · takeoff · flight | 🟡 |
| iç ilerleme okunmaz [A5-c · P2-g] | ✅ | pencere ≈8 px | vekil: eksilen yük, merdiven/kanat kapısı trafiği; kokpit istasyonu | 🟡 |
| kano kadrajdan çıkar [BACK TO WATER] | ⛔ | rota hesaplandı | G30'da su yolu ağzında, x 1293 | 🟢 |
| net figür gerçek hızda [DEEP END · BLUE DOOR] | ✅ | S28–S29 G | küçük siluet, "no readable face" | 🟡 |
| ışık bloom/hale [POLAR · FIRST GUEST] | ✅ | mavi saat ışıkları | "warm", gruplar, hale cümlesi yok | 🟡 |
| üç rejim beyansız [BACK TO WATER] | ✅ | A · B · G | PLAN §REJİM SAYISI beyanı | 🟢 |
| düz ızgara METRONOM | ⛔ | beş mercekte RHYTHM eşit klipte tetiklenmez | — | 🟢 |

### ⭐ 1 NUMARALI RİSK SAYIYLA YAZILIR

```
RİSK       kalkışta (S5–S6) model gövdeyi kaydırır, büyütür ya da ikinci gövde üretir — "uçak kalkar" görüntüsü uçuşa döner
SAYI       gövde x 537–1383 (846 px ±2) G5 · G6 · G7'de aynı; gövde altı 617 → 540 → 463; kuyruk 348 → 271 → 194;
           dört halat düşey; kolonlar x 740 · 1180 sabit
ÖLÇÜM      ❹ İNŞA (Cat 2 monoton · SCALE) ve ❶ GÖRÜNTÜ (Cat 7 sayım · SOLID/MELTING) · bakılan saniye 40,0–56,0
```
