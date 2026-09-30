# 🏗️ THE_IRON_BRIDGE — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **12 × 10,0 sn = 120,0 sn** | Kapak kartı: **5,0 sn** | Toplam: **125,0 sn**
Prompt yapısı: ⭐ **12 sahne → 13 görsel (G0…G12) + 12 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G6**
Yapı: **Tek açıklıklı çelik kemer yaya köprüsü — [`YAPI_TIPI_KARTLARI` §3]** · Saha: **Ilıman ormanlık dağ vadisi — [`SAHA_VE_IKLIM_KARTLARI` §2]**
Zaman yayı: **Nisan → Temmuz (yaklaşık 15 ay) → 120 saniye** · film mertebe anlatır: *"about a year"* [P1-c]
Işık günü: **08:00 → 18:00 · Σ rejim penceresi ≈ 3,5 saat ≤ 14** — kesmede ışık atlamaz [§2.7 ①]
Kamera mimarisi: **MAIN STATION** — tek istasyon, 12 sahne + usta kare (detay istasyonu yok) [`KAMERA_ISTASYONU` §1]
Izgara: ⛔ **DÜZ — 12 × 10,0** · sahip beyanı (14.09.2026) · karşı kayıt ve kabul edilen risk §AŞAMA MERDİVENİ'nde
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY 2026-09-30
Havuz kaydı: `apexait/YAYIN_PLANI.md` §5 · siluet ailesi: GEÇİŞ / BAĞLANTI

*"Ormanlık bir vadide, iki yakayı ayıran nehir üstüne çelik kemer köprü kurulur — orta açıklık kapanana dek."*

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     12 sahne × 10,0 sn                       = 120,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn                           =   5,0 sn   ← SAHNE DEĞİL, ayrı denetlenir
               ⛔ KONUM: teslimin SON 5 saniyesi (120,0–125,0) [A1-b]
──────────────────────────────────────────────────────────────
TOPLAM                                                     125,0 sn
BÖLÜM DOSYASI   BOLUM_1 = S0–S5 (0–60,0)  ·  BOLUM_2 = S6–S11 + USTA KARE (60,0–120,0)
QA BİRİMİ       FİLM (tek master × 12 mercek)
```

⛔ Kapak kartı **usta kareden (G12)** türetilir ve üstüne **İngilizce başlık** dizilir: `THE IRON BRIDGE` (`THE_IRON_BRIDGE_KAPAK.md`).
⚠️ Son sahnenin (S11) son ≥2,0 sn'lik TUTUŞU final kanıtıdır (`QA_SPEC` §1); kart hareketsiz ve yazılıdır — iki ayrı iş.

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Ormanlık vadide nehrin iki yakası çelik kemer yaya köprüsüyle birleşir
DİRENÇ   ① Nehir taşkını — S5–S6: su seviyesi yükselir, şantiye durur, bariyer sualtı
         ② Orta açıklık boşluğu — S7–S8: iki konsol arasında yalnızca 2 m, kapanması filmin doruğu
         ③ Orman kesimi — S0: iki yakada ağaç kesilmek zorunda; bedeli son karede görünür
         EKRANDA NASIL [P1-b]:  S5–S6 · nehir yüksekliği ve sarı-çıplak ağaçlar   ·   S7 · 2 m boşluk yakın plan   ·   S0 · kesim alanı
BEDEL    G0'daki kesintisiz yoğun orman — G12'de köprünün iki yanında kesim açıklığı ve genç filizler.
         Okuma bilinçli: "vahşi geçit kazanıldı" değil, "el değmemiş orman gitti".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            İki kıyıdaki kesintisiz yoğun orman                her karede görünür
  □ kadrajda görünüyor mu?    ✓ G0: %x 0–100 yaprak örtüsü · G12: kesim açıklığı her iki yanda
  □ cevap "zaman geçiyor" mu? ✗ — cevap: "karşıya geçme imkânı doğdu, ama orman bedel ödedi"
```

### Dört kabul testi

```
① TEK KARE TESTİ        G4 karesi donmuş: "çelik kemer iki yakadan ortaya büyüyor, henüz yarıda" → 1 sn ✅
② KİNETİK BAĞIMSIZLIK   Sabit kadrajda: kemer büyüyor + yaprak rengi değişiyor + nehir seviyesi değişiyor ✅
③ BAŞLIK ŞEMASI         "THE IRON BRIDGE" · 14 karakter ≤ 40 ✅
④ OMURGA CÜMLESİ [P1-k] keser → kazar → döker → diker → kaynar → direnir → bekler → uzanır → KAPANIR → döşer → söker → teslim
```

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera  ② kanıt nesnesi: meşe ağacı (SOL · %x 12–20 · ≈200 px · 13 karede birebir)
                          ③ çapa: kayalık (SAĞ · %x 78–88 · ≈160 px)  ④ nehir bandı (orta · %y 38–48)
                          ⑤ tek yapı, yalnız kemer KAZANIR: ankraj → destek kulesi → kemer → tabliye → korkuluk
                          ⑥ vinç/kaldırma: 15 m mobil vinç — yük hedefte belirir, kaldırma karede biter [DERS 57]
                          ⑦ ayrı insan figürü yok (streak cümlesi · rejim)
                          ⑧ tek ölçek çapası: meşe ağacı (≈200 px boy)
P1.5 · fırsat buldukça   mevsim taşıyıcısı yaprak döngüsü · nehir seviyesi + rengi · çamur/nem yüzeyi
SPEC · yalnız belge      güneş azimut/yükseklik dereceleri — kapı şartı
```

**Malzeme kimliği (her promptta):** *pale grey concrete · dark red-brown weathered steel · natural oak timber planks* — korpus cümlesi [DERS 34] · yapı CGI okunmasın.
**İnsan kararı:** İnsanlar VAR — kabinli vinç + blur işçi izleri + platform blur. ⛔ "No people" beyanı yok [DERS 33].
**Vinç / kaldırma kararı [DERS 57]:** 15 m mobil vinç · yük hedef üstünde asılı klipte biter (G(n) yük havada) → G(n+1) oturmuş. Kanca boş sarkmaz.
**Korpus kararı [DERS 55]:** "one single pedestrian footbridge spanning a 40-metre river gap … the only crossing visible, every other reach of the river is bare and unbridged."

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 10,0 sn teslim → SAHNE TAVANI ≥ 10,0,
                 yani en büyük kutu ≥ 11,0 (üret 11,0 → baştan 1,0 kırp [A7-b]; kutu tam 10,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 12 sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.

┌─ KAMERA İSTASYONU (ANA · tek istasyon) ─────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 · tam kare YATAY (36 mm kare eni,  │
│               16:9 kırpma → kare boyu 20,25 mm)                               │
│ yükseklik     h = 3,50 m (sağ kıyı kayalık platform üzeri)                   │
│ mesafe        D_eksen = 55,0 m (köprü merkezine) · D_kenar = 35,0 m           │
│ bakış açısı   350° · tilt 0° · roll 0°                                        │
│ sabitleme     "bolted to solid rock outcrop on south bank, absolutely zero movement"│
│ ⛔ HESAP (KILAVUZ_REHBERI §2.8 · f=24 · yatay · yüzde ALT kenardan):          │
│    yüzde(y) = 50 + 118,5·(y − h)/D         x(m, eksenden) → %50 + 66,7·x/D  │
│    yapı tabanı  y=0    → %43,7  ✓ alt çeyreğin üstünde                       │
│    ufuk (tilt 0)        → %50,0 = GÖZ ÇİZGİSİ                               │
│    kemer tepe   y=8,0  → %66,7  ✓ üst sekizin altında                        │
│    kemer inşaat orta (4m) y=4,0 → %57,7                                       │
│    geçici kule tepesi (10m) y=10 → %70,5                                      │
│    kanıt nesnesi meşe       → %56,2 · x ≈ %12–20 sol · ≈200 px boy           │
│    sol çapa meşe x=−18 m   → %12–20 sol   ·  sağ çapa kayalık x=+22 m → %78–88│
│ ⛔ ÖN GÖRSELLEŞTİRME zorunlu: kamera · yapı · çapalar · ufuk yan kesiti;      │
│    vinç bom başı y≈14 m → %82,7 (gökyüzünde · arka planda ağaçlar önünde)    │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① Büyük meşe ağacı (SOL · x ≈ %12–20 · ≈200 px boy · ≈90 px gövde)  KANIT   │
│ ② Kayalık çıkıntı (SAĞ · x ≈ %78–88 · ≈160 px geniş)                        │
│ ③ Nehir yüzey bandı (orta · %y 38–48)                                         │
│ Kanıt nesnesi [DERS 25]: büyük meşe ağacı — zincirde ELLE ✓/✗               │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ ufuk %50 (tilt 0) · kemer tepe ≤ %67 · tabliye ≈ %49 · yanlar: orman örtüsü  │
│ güvenli alan 16:9 — kanıt nesnesi alt 100 px'e ve sağ üst 300×100 px'e girmez│
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ tip: tek açıklıklı çelik kemer yaya köprüsü                                  │
│ açıklık: 40,0 m · toplam uzunluk: 55,0 m (yaklaşım dahil)                    │
│ kemer yüksekliği H = 8,0 m (nehir yüzeyinden tepesi)                         │
│ tabliye genişliği: 2,4 m · tabliye yüksekliği: 2,0 m (nehir tabanı üstü)    │
│ korkuluk: 1,1 m · çelik boru galvaniz                                        │
│ ankraj bloğu: 3,0 × 4,0 × 2,0 m (iki yakada) · beton C30                    │
│ malzeme: koyu kırmızı-kahve weathered çelik kemer (IPE-400) + doğal meşe      │
│          ahşap tabliye + galvaniz çelik korkuluk borusu                       │
│ geçici ekipman: iki çelik destek kulesi H≈10 m (S3–S10) · 15 m mobil vinç    │
│ (S3–S10) · kutu perde (S0–S7) — DEĞİŞMEZLER'E GİRMEZ [DERS 1]               │
│ STRUCTURE bloğunun İngilizce tam hâli BOLUM_1 S0'da yazılır; değişen AT THIS │
│ STAGE                                                                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 12 satır [`KILAVUZ_REHBERI` §4]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az yapı göstermez.
> Kış İKİ sahne [DERS 7]: S5 (sonbahar→kış geçişi) · S6 (tam kış taşkın).

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | İSTASYON | KANIT NESNESİ |
|:-:|:-:|---|---|---|:-:|:-:|:-:|---|
| 0 | 10,0 | KESER | Arazi temizliği + geçici yol · kemer %0 | Nisan | B | 08:00 | ANA | meşe yeşil · ≈200 px |
| 1 | 10,0 | KAZAR | Ankraj kazısı açık · donatı görünür · %0 | Nisan | B | 09:00 | ANA | meşe yeşil |
| 2 | 10,0 | DÖKER | Ankraj betonu döküldü · kalıp yerinde · %5 | Mayıs | B | 10:00 | ANA | meşe yeşil |
| 3 | 10,0 | DİKER | 2 destek kulesi dikili · vinç geldi · %10 | Haziran | B | 10:30 | ANA | meşe koyu yeşil |
| 4 | 10,0 | KAYNAR | Kemer %40 · iki yakadan ortaya · boşluk ~24 m | Temmuz | B | 11:00 | ANA | meşe koyu yeşil |
| 5 | 10,0 | DİRENİR | Kemer %65 · yaprak sarı-turuncu · nehir yüksek | Kasım | B | 09:30 | ANA | meşe sarı |
| 6 | 10,0 | BEKLER | Kemer %80 · nehir TAŞKIN · iş durdu | Ocak | A | 09:00 | ANA | meşe çıplak dal |
| 7 | 10,0 | UZANIR | Kemer %95 · boşluk 2 m · tomurcuklar | Mart | B | 10:00 | ANA | meşe tomurcuk |
| 8 | 10,0 | KAPANIR ⭐ | Kemer %100 · orta açıklık kapandı | Nisan | B | 11:00 | ANA | meşe yeşil |
| 9 | 10,0 | DÖŞER | Tabliye %60 · askı çubukları · %100 kemer | Mayıs | B | 10:30 | ANA | meşe koyu yeşil |
| 10 | 10,0 | SÖKER | Tabliye + korkuluk %100 · kuleleri sökülüyor | Haziran | A | 16:00 | ANA | meşe koyu yeşil |
| 11 | 10,0 | TESLİM | Köprü tam · genç filizler · altın saat | Temmuz | A | 17:30 | ANA | meşe koyu yeşil (kesim alanında filiz) |

```
IZGARA          120 BPM · ölçü 2,0 sn · 5 ölçü/sahne · kesmeler 10,0 · 20,0 · 30,0 · 40,0 · 50,0 · 60,0 · 70,0 · 80,0 · 90,0 · 100,0 · 110,0
DÜZ IZGARA BEYANI  (a) gerekçe: sahip beyanı (14.09.2026) — modül merdiveni, 12 × 10,0
                   (b) ritim klip İÇİNE nasıl taşınır: katman = aşama (her sahnede yeni eleman girer / çıkar);
                       mevsim rengi değişimi (yaprak döngüsü) her kesmeyi görsel olarak işaretler;
                       S5–S6 kış bloğu tempo yavaşlar hissi verir (karmaşık doku + gri)
                   (c) kabul edilen risk: ⑥ METRONOM hükmü beklenir [DERS 13 · 24]
IŞIK GÜNÜ       Σ pencere = 3 × 10 dk (A) + 9 × ~20 dk (B) ≈ 3,5 saat  ≤ 14 ✓
BÖLÜM SINIRI    G6 — S5 son karesi = S6 ilk karesi; yapı yüzdesi %80 · Ocak gri gökyüzü · çıplak dal [DERS 52]
```

### Üç zorunlu satır

```
KANIT   büyük meşe ağacı (sol kıyı) — G0'da ve usta karede (G12) aynı konum (x ≈ %12–20 · ≈200 px boy) [DERS 25]
LOOP    G12 ↔ G0: aynı kadraj · aynı çapalar · ışık BİLİNÇLİ FARKLI: G0 Nisan sabah (08:00 serin mavi) / G12 Temmuz akşam (17:30 altın)
SÖKÜM   destek kuleleri S10'da sökülür (vinç kaldırır · klipte gerilerek yükselir); kutu perde S7 sonunda kalkar; G12'de hiç biri yok
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
ankraj donatısı → sağ kıyı malzeme deposu (düz demet) → G1
çelik IPE kemer profilleri → sol kıyı geçici deposu (yatay istif, kırmızı-kahve) → G3'te gelir · G4'ten itibaren azalır
ahşap tabliye tahtaları → sağ kıyı deposu (istiflenmiş) → G8'de görünür
korkuluk boruları → sağ kıyı deposu → G9
GİZLİ İŞ: kemer profilleri fabrikada biçildi → GÖRÜNÜR VEKİL: sol kıyı deposunda markalı çelik istifi
GİZLİ İŞ: kutu perde perdelerin üstü → GÖRÜNÜR VEKİL: nehir kıyısında çamur bariyeri görünür S5'te
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① Köprü eksiksiz ayakta (tabliye + korkuluk + taş patika) — tüm geçici ekipman gitmiş
② Meşe ağacı aynı yerde (x ≈ %12–20 · ≈200 px) — köprü öncesindeki dünyayla aynı çapa
③ Kesim alanında genç filizler görünür — BEDEL okunuyor
FİNAL KARE KANITI  ffmpeg -ss 118.5 -i teslim.mp4 -frames:v 1 kanit.jpg   (S11 tutuşu içinde · altın saat [DERS 45])
```

---

## 🖼️ KARE TABLOSU — N+1 = 13 görsel

> Her kare bir öncekinin karesinden türetilir (ters inşa): G12 önce, G11 → … → G0.
> Güneş satırı her karede ve her I2V'de [DERS 18]; gölge açısı G(n) ile G(n+1)'de FARKLI.

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| 0 | 08:00 | 085° | 22° | uzun, batıya | açık mavi, serin | meşe koyu yeşil · nehir mavi düşük | arazi temizliği başlıyor — ağaç kütükleri sol kıyıda, sağda kazı izi |
| 1 | 09:00 | 105° | 36° | güneybatıya | açık mavi | meşe koyu yeşil · nehir mavi | ankraj kazısı açık · donatı kafesi sol çukurda görünür |
| 2 | 10:00 | 128° | 50° | güneye | açık mavi + küçük bulut | meşe koyu yeşil | her iki ankraj blok döküldü · sol kalıp henüz yerinde |
| 3 | 10:30 | 155° | 60° | güneybatıya | açık mavi · yaz bulutu | meşe koyu yeşil · nehir blaue | iki geçici kule dikili · sol kıyıda çelik istifi · vinç montaj pozisyonunda |
| 4 | 11:00 | 185° | 65° | kuzeye | kobalt mavi · az bulut | meşe koyu yeşil · S4 sonunda sararmaya başlıyor | kemer %40 · her iki yakadan ortaya büyüyor · boşluk ~24 m |
| 5 | 09:30 | 160° | 40° | kuzeybatıya | gri bulutlu · serin | meşe sarı-turuncu · nehir yükselmiş | kemer %65 · nehir kıyısı çamurlanmış · bariyer su kenarında |
| 6 ⭐ | 09:00 | 145° | 28° | güneybatıya | kapalı gri · düz | meşe ÇIPLAK DAL · nehir TAŞKIN kahverengi | kemer %80 · nehir taşmış · kutu perde kısmen sualtı · iş durdu |
| 7 | 10:00 | 125° | 40° | güneye | soluk gri-mavi · seyrelen bulut | meşe ilk tomurcuk · nehir çekilmiş | kemer %95 · iki uç arasında 2 m boşluk · sol kıyı deposu son profiller |
| 8 | 11:00 | 185° | 62° | kuzeye | açık mavi · yaz başı | meşe yeni yeşil yaprak | kemer %100 KAPANDI · kaynak izi orta noktada taze · destek kuleler hâlâ yerinde |
| 9 | 10:30 | 170° | 58° | kuzeye | açık mavi + beyaz bulut | meşe koyu yeşil | kemer tam · tabliye %60 döşenmiş · çelik askı çubukları görünür |
| 10 | 16:00 | 255° | 35° | kuzeye | altın saate geçiş · uzun gölgeler | meşe koyu yeşil | tabliye + korkuluk %100 · destek kuleler vinçle SÖKÜLÜYOR · patika başlıyor |
| 11 | 17:30 | 275° | 18° | uzun kuzeye | altın saat pembe-turuncu | meşe koyu yeşil · kesim alanında genç filiz | köprü tamam · tüm geçici ekipman gitti · taş patika iki kıyıyı birleştiriyor |
| 12 | 17:30 | 275° | 18° | uzun kuzeye | altın saat | meşe koyu yeşil + genç filiz | ⭐ USTA KARE — köprü eksiksiz · altın saat · yeni dünya |

```
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G12 usta kare → G11 (destek kuleleri yeni söküldü) → … → G6 (bölüm sınırı) → … → G0
   sonra I2V S0 (G0→G1) … S11 (G11→G12) — her klip iki uca kilitli, üretim 11,0 sn, baştan 1,0 kırp
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2]

```
ENLEM / YÖN     45°N · kamera bakışı 350° (kuzeye) → güneş sol üstten sağa geçer · kadrajda nadiren
MEVSİM YAYI     Nisan → Temmuz (~15 ay) · taşıyıcı: yaprak döngüsü (yeşil → sarı → çıplak → tomurcuk → yeşil)
                + nehir seviyesi (düşük → yüksek/taşkın → düşük) + nehir rengi (mavi → kahverengi → mavi)
GÖLGE SÜPÜRMESİ rejim B klipte ~60°–130° arası · rejim A (S6) klipte fark edilmez → nehir yüzeyi taşıyıcı
KIŞ             S5 (sonbahar → kış geçişi, yaprak sarı-turuncu, nehir yükseliyor) [başlangıç]
                S6 (tam kış taşkın, çıplak dal, nehir kahverengi) [bitiş] — tek klipte başlayıp bitmez [DERS 7]
GECE            yok (S11 altın saat ≥18° yükseklik — zifir değil [DERS 45])
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   h 3,50 m · D 55,0 m · bakış 350° · tilt 0°
YAPI     açıklık 40,0 m · kemer H 8,0 m · taç %66,7 · tabliye %48,7 · ankraj 3×4×2 m
ÇAPALAR  ① meşe ağacı %x 12–20 · ≈200 px boy  ② kayalık %x 78–88 · ≈160 px  ③ nehir bandı %y 38–48
IZGARA   12 × 10,0 · 120 BPM · kesmeler 10,0 · 20,0 · 30,0 · 40,0 · 50,0 · 60,0 · 70,0 · 80,0 · 90,0 · 100,0 · 110,0
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
⬜ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_IRON_BRIDGE   → GO / FIX / BLOCK: ⬜
⬜ FIX'ler: kutu seti ölçülmedi (beyanlı) · süreler eşit (beyanlı)
✅ 00_ANALIZ altı dosya tamamlandı · hikâye onayı 2026-09-30
⬜ ARAÇ KAPISI koşulmadı → THE_IRON_BRIDGE_URETIM_GUNLUGU.md §0
```
