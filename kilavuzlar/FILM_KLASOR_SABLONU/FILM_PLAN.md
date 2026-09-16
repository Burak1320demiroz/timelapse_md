# 🏗️ <FILM_ADI> — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **<N> × <KLIP>,0 sn = <SURE>,0 sn** | Kapak kartı: **5,0 sn** | Toplam: **<TOPLAM>,0 sn**
Prompt yapısı: ⭐ **<N> sahne → <N1> görsel (G0…G<N>) + <N> I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G<K>**
Yapı: ⬜ **[yapı tipi — `YAPI_TIPI_KARTLARI` §⬜]** · Saha: ⬜ **[saha — `SAHA_VE_IKLIM_KARTLARI` §⬜]**
Zaman yayı: ⬜ **[takvim: haftalar / aylar / yıllar → <SURE> saniye]** · film mertebe anlatır: *"⬜"* [P1-c]
Işık günü: ⬜ **[06:00 → ⬜ · Σ rejim penceresi ⬜ saat ≤ 14]** — kesmede ışık atlamaz [§2.7 ①]
Kamera mimarisi: **MAIN STATION** — tek istasyon, <N> sahne + usta kare (detay istasyonu ⬜ yok / ≤2 klip, üç koşul) [`KAMERA_ISTASYONU` §1]
Izgara: ⛔ **DÜZ — <N> × <KLIP>,0** · sahip beyanı (14.09.2026) · karşı kayıt ve kabul edilen risk §AŞAMA MERDİVENİ'nde
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ⬜ <gg.aa.yyyy> — onaysız plan yazılmaz
Havuz kaydı: `apexait/YAYIN_PLANI.md` §5 #⬜ · siluet ailesi ⬜

_"⬜ tek cümle — filmin ilk ve son karesi arasındaki fark, okuyana söylenen hâliyle."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     <N> sahne × <KLIP>,0 sn                       = <SURE>,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn                           =   5,0 sn   ← SAHNE DEĞİL, ayrı denetlenir
               ⛔ KONUM: teslimin SON 5 saniyesi (<SURE>,0–<TOPLAM>,0) [A1-b]
──────────────────────────────────────────────────────────────
TOPLAM                                                     <TOPLAM>,0 sn
BÖLÜM DOSYASI   BOLUM_1 = S0–S<K_SON> (0–<B1_SURE>,0)  ·  BOLUM_2 = S<K>–S<N_SON> + USTA KARE (<B1_SURE>,0–<SURE>,0)
QA BİRİMİ       <QA_BIRIMI>   (2/4 dk: FİLM · 6/8 dk: BÖLÜM — iki yarım master, SPEC künyesinde PART GRID)
```

⛔ Kapak kartı **usta kareden (G<N>)** türetilir ve üstüne **İngilizce başlık** dizilir: `⬜` (`<FILM_ADI>_KAPAK.md`).
⚠️ Son sahnenin (S<N_SON>) son ≥2,0 sn'lik TUTUŞU final kanıtıdır (`QA_SPEC` §1); kart hareketsiz ve yazılıdır — iki ayrı iş.

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     ⬜ [video başlamadan önce de var olan İŞ — "boş arsa ŞU oluyor"; "zaman geçiyor" vaat değildir]
DİRENÇ   ① ⬜   ② ⬜   ③ ⬜        [YAPI_TIPI kartının DİRENÇ satırından; en az üç]
         EKRANDA NASIL [P1-b]:  S⬜ · ⬜   ·   S⬜ · ⬜   ·   S⬜ · ⬜
BEDEL    ⬜ [G0'da olup usta karede (G<N>) olmayan şey — kadrajda GÖRÜNÜR, sahne numarasıyla: S⬜]
         Okuma bilinçli: "⬜" değil, "⬜".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            ⬜                                       ⬜
  □ kadrajda görünüyor mu?    ⬜ (yüzde ve piksel ile)                 ⬜
  □ cevap "zaman geçiyor" mu? hayır olmalı                             ⬜
```

### Dört kabul testi

```
① TEK KARE TESTİ        ⬜ donmuş karede izleyici "⬜, şu kadar kaldı" diyebiliyor mu (sayılabilir parça)
② KİNETİK BAĞIMSIZLIK   ⬜ sabit kadrajda, metinsiz, anlatıcısız — hangi hareket kanıtlıyor
③ BAŞLIK ŞEMASI         ⬜ kapak ≤3 kelime · başlık ≤40 karakter (YAYIN_PAKETI)
④ OMURGA CÜMLESİ [P1-k] ⬜ → ⬜ → ⬜ → … (<N> vuruş, her biri ≤4 kelime; merdiven bundan türer)
```

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera  ② kanıt nesnesi ⬜ (konum · px · <N1> karede birebir)  ③ çapa ⬜  ④ çapa ⬜
                          ⑤ tek parça yapı, yalnız parça KAZANIR: ⬜ → ⬜ → ⬜   ⑥ ⬜ (vinç/kaldırma kuralı)
                          ⑦ ayrı insan figürü yok (streak cümlesi · rejim)   ⑧ tek ölçek çapası: ⬜ (⬜ px)
P1.5 · fırsat buldukça   ⬜ mevsim taşıyıcısı · ⬜ saha takvimi · ⬜ yıpranma katmanı
SPEC · yalnız belge      ⬜ sayılar (promptta olan ama P0 olmayan: azimut/yükseklik dereceleri — kapı şartı)
```

**Malzeme kimliği (her promptta):** *⬜ · ⬜ · ⬜* — korpus cümlesi [DERS 34 · 42] · yapı CGI okunmasın.
**İnsan kararı:** ⬜ [insansız saha DEĞİL: kabinli makineler + streak cümlesi + rejim] · ⛔ "No people are present" beyanı yalnız gerçekten insansız sahada [DERS 33].
**Vinç / kaldırma kararı [DERS 8 · 22 · 46 · 57]:** ⬜ [vinç var mı · yük hep görünür · kaldırma yolu KAREDE biter: G(n) yük hedefin üstünde asılı, klip yalnız oturtur · kanca boş sarkmaz]
**Korpus kararı [DERS 55]:** yapı korpusu çoğulsa (türbin · konut bloğu · silo · direk) etraf POZİTİF BOŞ yazılır: "⬜ is the only ⬜ in view …".

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne <KLIP>,0 sn teslim → SAHNE TAVANI ≥ <KLIP>,0,
                 yani en büyük kutu ≥ <KLIP1>,0 (üret <KLIP1>,0 → baştan 1,0 kırp [A7-b]; kutu tam <KLIP>,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa <N> sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.

┌─ KAMERA İSTASYONU (ANA · tek istasyon) ─────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 · tam kare YATAY (36 mm kare eni,  │
│               16:9 kırpma → kare boyu 20,25 mm)                               │
│ yükseklik     h = ⬜ m (⬜ referans seviyesinden — nereye kurulu)              │
│ mesafe        D_eksen = ⬜ m (yapı eksenine) · D_kenar = ⬜ m [DERS 38]         │
│ bakış açısı   ⬜° · tilt 0° · roll 0°                                          │
│ sabitleme     "bolted to ⬜, absolutely zero movement"                         │
│ ⛔ HESAP (KILAVUZ_REHBERI §2.8 · f=24 · yatay · yüzde ALT kenardan):            │
│    yüzde(y) = 50 + 118,5·(y − h)/D         x(m, eksenden) → %50 + 66,7·x/D    │
│    D = (H − h)/0,27  (taç %82)             px = 1280·boy(m)/D  (1080p)        │
│    yapı tabanı  y=0    → %⬜    ✓ alt çeyreğin üstünde                        │
│    ufuk (tilt 0)        → %50,0 = GÖZ ÇİZGİSİ (tercih değil, geometri)         │
│    taç          y=H    → %⬜    ✓ üst sekizin altında                          │
│    kanıt nesnesi        → %⬜ · x ≈ ⬜ px · ≈ ⬜ px boy                           │
│    sol çapa ⬜  x=−⬜ m  → %⬜ (soldan)   ·   sağ çapa ⬜  x=+⬜ m → %⬜             │
│ ⛔ ÖN GÖRSELLEŞTİRME zorunlu: kamera · yapı · çapalar · ufuk yan kesiti; vinç │
│    bom başı ve her kaldırma hangi yüzdeye çıkıyor — gök mü, kara mı [DERS 22] │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① ⬜ (SOL · x ≈ ⬜ px · %⬜ · ≈⬜ px)   ② ⬜ (SAĞ · …)   ③ ⬜ (uzak · silüet %⬜)  │
│ + yol / duvar / ağaç … kalıcı olan her şey; her promptun SITE / BACKGROUND    │
│   bloğunda BİREBİR aynı kelimeler. Kanıt nesnesi [DERS 25]: ⬜ — zincirde ELLE │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ ufuk %50 (tilt 0) · taç ≤ %82 · çalışma seviyesi ≥ %25 · yanlar: ⬜            │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ (KILAVUZ_REHBERI §2.8 varsayılanı) — kanıt nesnesi │
│ alt 100 px'e ve sağ üst 300×100 px'e girmez                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ tip ⬜ · toplam yükseklik H = ⬜ m · taban ⬜ m · eleman sayısı ⬜ (⬜ × ⬜ m) ·   │
│ malzeme ⬜ · renk ⬜ · çatı/taç ⬜ · geçici ekipman: ⬜ (vinç tipi · bom ⬜ m) ·  │
│ STRUCTURE bloğunun İngilizce tam hâli BOLUM_1 S0'da yazılır ve <N1> promptta   │
│ BİREBİR tekrarlanır; değişen yalnız AT THIS STAGE                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — <N> satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az yapı göstermez. İnşa sırası
> `YAPI_TIPI_KARTLARI`'ndan gelir, uydurulmaz; sahne sayısı arttıkça aşama incelir (ara hâl
> %25 / %50 / %75 kendi satırını alır [DERS 37]). Kış İKİ sahne [DERS 7]. SÜRE sütununun en
> büyüğü doruktadır [P2-f] — düz ızgarada hepsi <KLIP>,0 (aşağıdaki beyan). Gölgesiz (rejim C)
> klip en uzun klip olamaz [DERS 40].

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | İSTASYON | KANIT NESNESİ (px) |
|:-:|:-:|---|---|---|:-:|:-:|:-:|---|
<MERDIVEN_SATIRLARI>

```
IZGARA          120 BPM · ölçü 2,0 sn · <OLCU> ölçü/sahne · kesmeler <KESMELER>
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: ⬜ [sahip beyanı 14.09.2026 — modül merdiveni, <N> × <KLIP>,0]
                   (b) ritim klip İÇİNE nasıl taşınır: ⬜ [katman = aşama · her blok yeni ses · rejim değişimi]
                   (c) kabul edilen risk: ⑥ METRONOM hükmü beklenir [DERS 13 · 24]; karşı kayıt: varyanslı
                       kurgu üç filmde RHYTHM aldı [DERS 44 · THE CROSSING · OVER THE WALL · THE EMPTY RIDGE]
IŞIK GÜNÜ       Σ pencere = ⬜ A × 10 dk + ⬜ B × 2 h (+ ⬜ C × 9 h) = ⬜ saat  ≤ 14 ✓/✗   (03_SAHNE_SIRALAMASI §4)
BÖLÜM SINIRI    G<K> — sahne S<K_SON> son karesi = sahne S<K> ilk karesi; yapı yüzdesi, gölge açısı, gök aynı [DERS 52]
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: ⬜ — G0'da ve usta karede (G<N>) aynı konum (x ≈ ⬜ px · %⬜) ve aynı boy (≈⬜ px) [DERS 25]
LOOP    G<N> ↔ G0: aynı kadraj · aynı çapalar · ışık ⬜ [aynı saat (loop) / farklı saat (bilinçli, sebep: ⬜)]
SÖKÜM   geçici ekipman ekranda GİDER: ⬜ (S⬜'de vinç/iskele/kalıp çıkar; usta karede YOK) — yoktan yok olmaz [DERS 48]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
⬜ → ⬜ → G⬜
GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL (prompta yalnız vekil girer): ⬜ → ⬜
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① ⬜ (ilk okunan)  →  ② ⬜  →  ③ aynı ⬜ (kanıt nesnesi)
FİNAL KARE KANITI  ffmpeg -ss ⬜ -i teslim.mp4 -frames:v 1 kanit.jpg   (son sahne S<N_SON> tutuşu içinde · aydınlık [DERS 45])
```

---

## 🖼️ KARE TABLOSU — N+1 = <N1> görsel [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Her kare bir öncekinin karesinden türetilir (ters inşa §8): G<N> usta kare önce, sonra G<N_SON> → … → G0.
> Güneş satırı her karede ve her I2V'de [DERS 18]; güneş DİSKİ anılmaz [DERS 39]; gölge açısı G(n) ile
> G(n+1)'de FARKLI [DERS 32 · 47].

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
<KARE_SATIRLARI>

```
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G<N> usta kare → G<N_SON> (master'dan ⬜ KALDIRILDI) → … → G<K> (bölüm sınırı) → … → G0
   sonra I2V S0 (G0→G1) … S<N_SON> (G<N_SON>→G<N>) — her klip iki uca kilitli, üretim <KLIP1>,0 sn, baştan 1,0 kırp
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     ⬜°N · kamera bakışı ⬜° → güneş kadrajda ⬜ (hangi saatlerde gökte, hangi saatlerde kadraj dışı)
MEVSİM YAYI     ⬜ [ay → ay] · taşıyıcı: ⬜ (ağaç / tarla / kar / su seviyesi — sahaya göre §6)
GÖLGE SÜPÜRMESİ rejim B klipte ⬜°–⬜° (40°N tablosu) · rejim A klipte fark edilmez → yüzeyle kanıtlanır
KIŞ             S⬜ (kar yağar · döngü yavaşlar) · S⬜ (erir · çamur · döngü hızlanır) — tek klipte başlayıp bitmez [DERS 7 · 21]
GECE            yok / S⬜ (sahip kararı · §5 · final zifirde bitmez [DERS 45])
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   h ⬜ · D ⬜ · bakış ⬜° · tilt 0
YAPI     H ⬜ m · taç %⬜ · taban %⬜ · eleman ⬜ × ⬜ m
ÇAPALAR  ① ⬜ %⬜ · ② ⬜ %⬜ · ③ ⬜ %⬜ · kanıt nesnesi ⬜ px
IZGARA   <N> × <KLIP>,0 · 120 BPM · kesmeler <KESMELER>
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
⬜ prompt kapısı  python3 araclar/prompt_kontrol.py <FMT>/<FILM_ADI>   → GO / FIX / BLOCK: ⬜
⬜ FIX'ler ve beyanları: kutu seti ölçülmedi (beyanlı) · süreler eşit (beyanlı) · ⬜
⬜ 00_ANALIZ altı dosya ✅ · hikâye onayı ⬜ tarih
⬜ ARAÇ KAPISI koşulmadı → <FILM_ADI>_URETIM_GUNLUGU.md §0
```
