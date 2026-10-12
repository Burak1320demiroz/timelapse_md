# 🔍 THE_HIDDEN_FALLS — QA SPEC

> THE HIDDEN FALLS · 16:9 · 15 × 8,0 sn · 120,0 sn · kart yok · müzik yok (ses tasarımı). **Bu dosya yalnız belgeli
> merceklere verilir: ❹ İNŞA · ❺ TESLİM** (beş mercekli QA, 06.10.2026 [DERS 64]).
> ⛔ **❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❸ ŞANTİYE'ye VERİLMEZ** — üçü kör koşar, ayrı geçici sohbette, proje dışında
> [`QA_KOSU_KILAVUZU` §1]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit değildir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_HIDDEN_FALLS <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].
> Ham raporlar `QA/HAM/THE_HIDDEN_FALLS/THE_HIDDEN_FALLS_Q<n>_<AD>_HAM.md` · kayıt `QA/FILMLER/THE_HIDDEN_FALLS.md` · `QA/TABLO.md`.

---

## 0. KÜNYE

```
FİLM          THE_HIDDEN_FALLS — kirli suyla dolu terk edilmiş bir kireçtaşı ocağı boşaltılır, uzak duvarın dibine cam
              cepheli bir yapı kurulur, çukur turkuaz suyla dolar ve salonun önünden şelale akar · MAIN STATION +
              SALON STATION (2 klip)
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_2_dk_filmler · HIZ 1x
KANARYA       slatefinch   ⛔ kör mercek raporunda bu kelime geçerse plan SIZMIŞTIR → koşu SIZINTI [QA_KOSU §3.1]

TESLİM YAPISI ⭐ SAHNE BLOĞU  15 sahne × 8,0 sn = 120,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  ⛔ YOK                                   ← son sahne S14 son saniyeye kadar SAHNEDİR
                 TOPLAM                          120,0 sn
              ⛔ 120,0 sn'den uzun dosya = plan dışı kart/siyah → ❺ "the plan declares NO card — report it"

SAHNE SAATLERİ  sahne n = n × 8,0 → (n+1) × 8,0   ·   S0 0,0–8,0 · … · S8 64,0–72,0 · S9 72,0–80,0 · … · S14 112,0–120,0
                (14 kesme, her 8,0 sn · müzik yok — ölçü ızgarası yok)
PART GRID       — (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)
⛔ DÜZ IZGARA   sahip senaryosu (08.10.2026) + sahip izinli 15 × 8,0 varyantı · ⚠️ bandın dışı (format 12 × 10,0). Eşit
                klipte ❷ RHYTHM NOT TRIGGERED; METRONOM hükmü beş mercekli rubrikte yok. Karşı kayıt [DERS 44].
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]: ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — {5,9} ya da {5,10}
   gerekir; {4,6,8} çıkarsa iki-klip hükmü (PLAN §DEĞİŞMEZLER) ve karar sahibe döner.

YAPI          iki katlı, tam cam cepheli yapı · 45 × 12 m · çatı +18,5 · sağ uçta çift yükseklikte cam salon (16 m) ·
              yükseltilmiş beton temel 49 × 20 m (+6 → +10) · ahşap teras · iki açıklıklı çelik yaya köprüsü (2 × 16 m) ·
              üst basamakta kanal · pompa evi + boru · şelale (perde 10 m en, camdan 2 m önde)
SAHA          terk edilmiş kireçtaşı ocağı 120 × 110 m · kenar +36 · 38° K · çapalar: şemsiye çam (sol üst) · yıkık kulübe
              (sağ üst) · uzak kenar + çapraz çatlak · ⭐ havzadaki kireçtaşı SÜTUN (orta, kanıt)
ZAMAN YAYI    ≈15 ay (ilkbahar → ertesi yaz başı) · film mertebe anlatır: "bir yaz inşaat, bir sonbahar bahçe, bir bahar dolum" [P1-c]
IŞIK          TEK GÜN 06:30 → 19:20 (mavi saat) · Σ rejim 12 sa 50 dk · takvim SAHADAN · bilinçli sıkıştırma (ÜSLUP BEYANI)
REJİM         A (10 dk) × 5 + salon S7 · B (2 sa) × 6 (S1 · S2 · S5 · S9 · S10 · S12) · G (gerçek zaman) × 3 (S11 · S13 · S14)
              — ⚠️ üç rejim, beyanlı
KAMERA        MAIN STATION — h 16,0 m (havza tabanından) · D 110,0 m (uzak duvarın dibine) · bakış 0° · tilt 0° · roll 0°
              ⭐ İKİNCİ İSTASYON BEYANI: SALON STATION — h 12,0 m · cama 10,0 m · bakış 180° · tilt 0° · YALNIZ S7 (56,0–64,0)
              ve S13 (104,0–112,0). S7, S8 ile AYNI on dakikadır; S13, S12'nin son sekiz saniyesidir; dıştaki yapı iki
              yakada aynı. Sahip senaryosu 08.10.2026 ("Cam salonun içindeyiz"). ❶ bunu SEPARATE IMAGES saymamalı: iki
              istasyon, ortak çapa (havzadaki sütun · kireçtaşı duvarlar).
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G15 usta kare → G14 → G12 → … → G0 · salon: G7′ → G7 · G13′ → G13 · her kare zincir_kontrol
GÜNLÜK        THE_HIDDEN_FALLS_URETIM_GUNLUGU.md — ⛔ boş (üretim başlamadı) → bu SPEC'in hükmü üretimle başlar
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı · ❺ FINAL BEAT

```
SAHNE       S14 (112,0–120,0)
FİNAL BEAT  112,0–116,0 olay: üç kişi köprünün yapı ucundan ≈5 m yürür, korkulukta durur ·
            116,0–120,0 TUTUŞ: üç kişi kıpırtısız, şelale akar, ışıklar yanık, başka hiçbir şey değişmez
SANİYE      119,0 (son 4,0 sn'lik TUTUŞUN içi [P2-i]; mavi saat, okunur [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (beşi de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① perdenin arkasında ışıklı salon (x 1130–1339 · üstten 507–619) — perde salonun sağ 10 m'sini örter, sol kısmı açık
   ② şelale perdesi + köpük (x 1213–1347 · 502 → 660) — çatının çelik dudağından suya
   ③ cam cephenin ışığı ve sudaki yansıması (üstten 703–808)
   ④ köprüde üç kişi, kadrajın İÇİNDE (x ≈619 · ≈25 px · yüz okunmaz)
   ⑤ AYNI sütun (kanıt nesnesi: x 922–1050 · tepe 668 · 128 px — G0 ile aynı konum ve boy; dibi turkuaz suda, 770)
   + geçici ekipman GİTMİŞ: vinç YOK · pompa ve hortum YOK · kamyon YOK (SÖKÜM satırı)
   + BEDEL görünür: kirli su ve paslı platform yerine turkuaz su ve ışıklı yapı (G0 ↔ G15)

KOMUT
   ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①–⑤'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP (biçim kafiyesi, ışık bilinçli farklı)
   ffmpeg -ss 0.3   -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 119.5 -i teslim.mp4 -frames:v 1 kanit_g15.jpg
   İki karede çam, kulübe, uzak kenar, çatlak ve sütun aynı yerde; sütun aynı x'te (922–1050 ±2 px).
   Işık: G0 06:30 sabah gölgesi ↔ G15 mavi saat (PLAN LOOP satırı) — kanıt çifti AYNI IŞIK iddiası taşımaz.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=16,0 · tilt 0 · yatay: yüzde = 50 + 118,5·(y−h)/D, ALT kenardan)

| nesne | y (m) | D (m) | yüzde (alt kenardan) | x (soldan) | px boy | her karede |
|---|:-:|:-:|:-:|:-:|:-:|---|
| ufuk (tilt 0, görünmez — kenarın altında) | — | — | 50,0 | — | — | ✓ |
| uzak kenar çizgisi (düz) | +36 | 110 | 71,5 (üstten 308) | bütün en | — | ✓ |
| uzak duvar üst basamağı · kanal | +30 | 111 | 64,9 (379) | kanal x ≈1050–1300 | — | kanal G8 (yarım) · G9–G15 |
| çatı | +18,5 | 98 | 53,0 (507) | 751–1339 | — | G6–G15 (G4–G5 iskelet tepesi) |
| salon çatı dudağı | +18,8 | 96 | 53,5 (502) | 1213–1347 | — | G6–G15 |
| temel üstü · teras · platform | +10 | 98 | 42,7 (619) | 751–1391 | — | G3–G15 |
| köprü güvertesi | +10,5 | 94 | 43,1 (615) | 306–742 | — | G5–G15 |
| su (dolu) · perdenin dibi | +7 | 96 | 38,9 (660) | — | — | yalnız G11–G15 |
| kirli su | +3 | 98 | 34,3 (710) | — | — | yalnız G0–G1 |
| havza tabanı | 0 | 98 | 30,7 (749) | — | — | G2–G10 kuru |
| ⭐ kanıt nesnesi SÜTUN | 0 → +11 | 50 | 12,1–38,2 (949–668) | 922–1050 | 128 × 281 | ✓ BİREBİR (boy dâhil) · su izi 872 / — / 770 |
| çapa ① ŞEMSİYE ÇAM (SOL ÜST) | +36 → +50 | 105 | 72,6 dip · 88,4 taç | ≈155 | taç ≈146 en | ✓ her dem yeşil |
| çapa ② YIKIK KULÜBE (SAĞ ÜST) | +36 → +40 | 100 | 73,7–78,4 (284–233) | 1741–1818 | 77 × 51 | ✓ |
| çapa ③ çapraz çatlak (uzak duvar) | +35 → +11 | 110 | 70,5 → 44,6 | 494 → 704 | — | ✓ |
| giriş terası (SOL) | +10 | 95 | 42,5 (621) | 151–313 | — | ✓ |
| vinç (paletli, kafes bom) | taban +10 | 100 | 42,9 | taban ≈268 | — | yalnız G0–G8 · S8'de gider |
| perde (şelale) | +18,8 → +7 | 96 | 53,5 → 38,9 | 1213–1347 | 134 × 158 | yalnız G12–G15 |
| üç kişi (köprüde) | +10,5 → +12,3 | 94 | 43,1 → 45,3 | 688 (G14) · 619 (G15) | ≈25 boy | yalnız G14–G15 (+ S12 son anı) |

```
SALON STATION    ufuk %50 (540) · cam kadrajın tüm enini %32,2'den (732) yukarı kaplar · kayıtlar dikey, eşit aralık ·
                 sütun camdan x 1347–1457 · tepe %48,0 (561) · su (+7) %39,8 (650) · S13'te perde kadrajın SOL x 106–1173'ünü
                 örter, sütun açık camda · mobilya alt üçte bir · S7 ve S13'te aynı (kamera hiç kıpırdamaz)
KAMERA SABİTLİK  ilk/son kare kayması ≤ 2 px (1080p · KAMERA_ISTASYONU §7 · zincir_kontrol ESIK_KAYMA_ORAN) ·
                 üç nirengi: sütun tepesi sol köşesi · kulübe kapı boşluğu · çatlağın üst ucu
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
ocak 120 × 110 m · kenar +36 · orta basamak +4 (D 75–92) · dip basamağı +6 (D 92–110) · üst basamak +30 · doğu bahçe
basamakları +14 · +20 · +26 · paslı platform 8 × 6 × 7 m (dört ayak, x 0…+8) · sütun 5 m en, tepe +11 (x −1,5…+3,5 · D 50)
temel 49 × 20 m (x −16…+33) · +6 → +10 · köprü ayağı 1,5 × 1,5 m (x −32 · D 94) · yapı 45 × 12 m (x −16…+29 · D 98–110) ·
zemin +10,5 · üst kat +14,5 · çatı +18,5 · 15 bölme × 3 m · salon x +13…+29 (16 m · 8 m çift yükseklik) · çatı dudağı
+18,8 (camdan 2 m ileri) · teras x −16…+13 × 8 m · köprü 2 × 16 m (x −48…−16) · güverte +10,5 · kanal x −5…+27 (+30) ·
çentik x +19…+29 · boru Ø 0,6 m (x +31 · +10 → +30) · pompa evi 4 × 6 m (x +29…+33) · perde 10 m en (x +19…+29) ·
kaya kademesi +30 → +18,5 · perde +18,8 → +7 · su: kirli +3 · kuru · turkuaz +7 · bahçe: 3 sıra · 3 zeytin · eğreltiotu ·
salon: 1 masa + 12 sandalye · kanepe + 2 koltuk · vinç: sarı paletli kafes bomlu (yalnız G0–G8)
```

### Yapı yüzdesi ve saha durumu — sahne sahne (❹ İNŞA · ❺ TESLİM için)

| S | saat | yapı: eleman + ara hâl | yapının tepesi | geçici ekipman kadrajda | saha / su / mevsim |
|:-:|:-:|---|:-:|---|---|
| S00 | 06:30→06:40 | — · paslı platform dipte → vinçte → kamyonda | — | vinç (platform yükte) · kamyon · ekskavatör | kirli su +3 · ilkbahar başı |
| S01 | 06:40→08:40 | — · su +3 → taban | — | vinç · kamyon (gider) · 2 pompa + hortum | su iner · basamaklar çıkar |
| S02 | 08:40→10:40 | temel 0 → %100 · köprü ayağı 0 → 1 | %42,7 | vinç (donatı yükte) · ekskavatör · damperli · beton pompası · kalıp | kuru · ilkbahar |
| S03 | 10:40→10:50 | iskelet 0 → %100 | %42,7 → %53,0 | vinç (çelik yükte) · 2 uzun kamyon · kalıp istifi (gider) | kuru · yaz başı |
| S04 | 10:50→11:00 | köprü 0 → 2 açıklık | %53,0 | vinç (açıklık yükte) · açıklık istifi | kuru · yaz başı |
| S05 | 11:00→13:00 | teras %0 → %100 · çatı kapanır · dudak | %53,0 | vinç (tahta paleti) · tahta + panel istifleri | kuru · yaz |
| S06 | 13:00→13:10 | cam 0 → 15 bölme (önce salon) | %53,0 | vinç (vakum çerçevesi + cam) · 2 kamyon (sandık) | kuru · yaz |
| S07 | 13:10→13:20 | 🪟 salon: boş → masa + 12 sandalye + oturma | — (salon) | — (salon: sarılı mobilya yığını) | kuru (camdan) · yaz |
| S08 | 13:10→13:20 | kanal %0 → %100 · boru · pompa evi | %53,0 | vinç (boru demeti → gider) · ip ekibi | kuru · yaz |
| S09 | 13:20→15:20 | bahçe 0 → 3 sıra · 3 zeytin · eğreltiotu | %53,0 | küçük ekskavatör · bitki paletleri · küçük kamyon | kuru · yaz sonu |
| S10 | 15:20→17:20 | su taban → +7 | %53,0 | 2 hortum (römorka) · pompa kamyonu (kenarda) · küçük kamyon | ⭐ dolum · sonbahar → ilkbahar |
| S11 | 17:20 +8 sn | şelale başlar | %53,0 | YOK (pompa evinde bir işçi, üst basamakta iki) | turkuaz · ilkbahar |
| S12 | 17:20→19:20 | ışıklar tek karede · 3 kişi köprü ucu | %53,0 | araba + küçük kamyon (son aletler, gider) | gün batımı → mavi saat |
| S13 | 19:20 (−8 sn) | 🪟 salon: perde · masa hazır · bir kişi | — (salon) | YOK | mavi saat (camdan) |
| S14 | 19:20 +8 sn | (değişmez) · üç kişi · TUTUŞ | %53,0 | YOK | derin mavi saat · yaz başı |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   kireçtaşı SÜTUN — G0…G15 (ana) hepsinde x 922–1050 · tepe 668 · 128 px en; zincirde her karede ELLE ✓/✗
                (günlük §2) · su izi: G0–G1 kirli su 872 · G2–G10 kuru (dip 949) · G11–G15 turkuaz 770 — GÖVDE değişmez ·
                salon karelerinde (G7 · G7′ · G13 · G13′) camdan x 1347–1457 — iki kameranın ortak nesnesi
İKİNCİ ÇAPA     yıkık kulübe x 1741–1818 · üçüncü: şemsiye çam x ≈155 · dördüncü: uzak kenar 308 + çatlak (494,319 → 704,598)
❸ İÇİN          dikiş = KARE (G1…G14 ana): dikişin iki yakası aynı görsel; ❸ REBUILT hükmü zincir koşulmadı demektir ·
                salon kesmeleri (S6 → S7 → S8 · S12 → S13 → S14) istasyon değişimidir, dış kare iki yakada AYNI
```

---

## 5. ❹ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ajanı · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | ajan (taşıyan) | geçici destek | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|---|:-:|:-:|:-:|
| paslı platform (GİDEN) | dip basamağı (x 0…+8) | paletli vinç → düz kasalı kamyon | dört sapan + iki kılavuz ip | G0 (vinçte) | — | G2 (kamyonla gider) |
| kirli su (GİDEN) | havza | iki dizel pompa · hortum | — | G1 | G2 (kuru) | pompalar G3'te yok |
| temel | vinçte donatı demeti · beton pompa kamyonu | ekip · pompa bomu · ekskavatör · damperli | kalıp · donatı kafesi | S2 içi | G3 | kalıp S3'te kamyona |
| köprü ayağı | aynı | aynı | kalıp | S2 içi | G3 | — |
| çelik iskelet | 2 uzun kamyon (giriş terası) | vinç · ekip | sapan · ankraj civataları | G3 (kancada) | G4 | kalıcı |
| köprü × 2 açıklık | giriş terasında istif | vinç · 4 kılavuz ip | kaldırma kirişi | G4 | G5 | kalıcı |
| teras + çatı + dudak | temelin önünde istifler | ekip · vinç (palet) | — | S5 içi (soldan sağa) | G6 | — |
| cam | 2 kamyonda sandık | vinç (vakum çerçevesi) · camcılar | vakum çerçevesi | G6 (kancada) | G8 | sandıklar S6'da gider |
| 🪟 salon mobilyası | yan kapıda sarılı yığın | iki işçi | — | G7 (boş) | G7′ | ambalaj yığını kalır |
| kanal + boru + pompa evi | vinçte boru demeti · üst basamakta ekip | ip ekibi · vinç | ip · kelepçe | G8 (yarım) | G9 | vinç S8'de gider |
| bahçe | giriş terasında paletler · küçük kamyon | bahçıvan ekibi · küçük ekskavatör | — | S9 içi (alttan üste) | G10 | paletler S9'da biter |
| dolum suyu | kenardaki pompa kamyonu · 2 hortum | — | — | S10 içi | G11 | hortumlar S10 sonunda römorka |
| şelale | gölden pompa evi → boru → kanal | pompa evinde işçi (vana) | — | G11 (kuru) | G12 | — |
| ışık | (gizli) elektrik | — | — | G12 (sönük) | G14 | — |

```
❹ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır):
   yapı 1 · paslı platform 1 (G0–G1) · sarı paletli vinç 1 (G0–G8) · düz kasalı kamyon 1 · uzun kamyon 2 · küçük kamyon ·
   dizel pompa 2 · beton pompa kamyonu 1 · kenarda pompa kamyonu 1 (S10) · ekskavatör 1 + küçük ekskavatör 1 · damperli 1 ·
   römork 1 · araba 1 (S12) · ekip (iz) · S11 üç işçi (küçük) · S13 bir kişi (sırtı kameraya) · S14–G15 üç kişi ·
   çam 1 · kulübe 1 · sütun 1 · köprü ayağı 1 · zeytin 3
   ⛔ DAVETSİZ: ikinci yapı · ikinci çukur · maden makinesi (konveyör, kırıcı, damperli kamyon filosu) · otel kulesi ·
      fayanslı yüzme havuzu · süs çeşmesi · tekne · su kaydırağı · yazı/işaret/tabela · kule vinç · ikinci şelale
❹ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: kuru havza = S1 pompalar · şelale = S8 kanal + boru +
                  pompa evi (S11'de vana) · turkuaz su = S10 hortumlar · ışık = (gizli) elektrik, S12'de tek karede
❹ ÇERÇEVE DEFTERİ yapı x 751–1339 sabit (G4 → G15) · çatı 507 · platform 619 · köprü 615 · su 660 (G11+) · sütun 128 px sabit
❹ GİZLİ İŞ        sol kısmın iç döşemesi → S12'de iki katın camlarında ışık · salon → SALON İSTASYONU (S7) · elektrik → S12 ·
                  devridaim → pompa evi + boru (S8) + S11 vana
❹ DECLARED WORLD  taş ocağı · kirli su (G0–G1) · kuru havza (G2–G10) · turkuaz göl (G11+) · şelale (G12+) · bahçe (G10+) ·
                  insanlı ekip · üç kişi (S12 sonu–G15) · salonda bir kişi (S13) · mavi saat (G13–G15) · kış görüntüsü YOK
❸ PARKED GEREKÇESİ S11 (şelale başlar, gerçek zaman) · S13 (salon, gerçek zaman) · S14 (final tutuşu): şantiye bitti; bunlar
                  ödül ve sakin anlardır — işsiz aralık değil, beyanlı [P4-f · C1-d]
```

---

## 6. ❷ ZAMAN VE KESME — kesme listesi ve ses (❷ kör koşar; bu bölüm ❺ ve operatör içindir)

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_HIDDEN_FALLS/THE_HIDDEN_FALLS_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
                     ⚠️ prompt_kontrol.py süre satırlarını tek haneli sahne numarasıyla okur (S10–S14 okunmaz) —
                        bilinen araç hatası; kesme_kontrol.sh iki haneyi okur
İSTASYON KESMELERİ   56,0 (ana → salon) · 64,0 (salon → ana) · 104,0 (ana → salon) · 112,0 (salon → ana)
REJİM KESMELERİ      88,0 (S10 B → S11 G) · 96,0 (S11 G → S12 B) · 104,0 (S12 B → S13 G) — rejim değişimi YALNIZ kesmede [P5-c]
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                ⛔ YOK (varsayım — sahip senaryosu SES tarif etti) · SES TABLOSU THE_HIDDEN_FALLS_MUZIK.md:
                     0–56 makine ve metal · 56–88 ahşap, cam, iç mekân · 88–104 su sesi büyür · 104–112 içeriden boğuk su ·
                     112–120 dışarıdan şelale ve akşam, ani kesilme yok
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G9 (S8 ↔ S9) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si (S8) G9 karesinde biter; G9 BOLUM_2'nin ilk görselidir (ANA istasyon).
ELLE KARE            ffmpeg -ss 72.0 -i teslim.mp4 -frames:v 1 sinir.jpg → yapı camlı · kanal + boru tamam · vinç YOK ·
                     havza kuru · gölge +43° · yaz sonu · giriş terasında bitki paletleri
SALON                S7 sınıra DÜŞMEZ (hikâye SAPMA ⑩ — betiğin 8/7 bölmesi yerine 9/6)
```

---

## 8. ❺ TESLİM — belgeli merceğin okuyacağı beyanlar

```
VAAT            Kirli suyla dolu ölü bir taş ocağını boşaltıp duvarının dibine cam cepheli bir yapı kurmak, çukuru turkuaz suyla
                doldurmak ve yapının salonunun önünden bir şelale akıtmak.
DİRENÇ          ① çukur — S0–S1 (0,0–16,0) vinçte paslı platform, inen kirli su · ② duvar — S3 (24,0–32,0) havzanın üstünden
                uzanan vinç kolu, S8 (64,0–72,0) ipteki ekip · ③ su kotu — S10 (80,0–88,0) su platformun 3 m altında durur
BEDEL           kirli su + paslı platform — S0 (0,0) platform gider; S1 (8,0–16,0) su gider; S10 (80,0–88,0) çukur turkuaz suyla
                dolar; G15'te aynı yerde ışıklı yapı ve şelale
AÇILIŞ          nesne: kirli sulu dev ocak (kadrajın tamamı) · eylem: vinç ilk karede platformu taşıyor · ipucu: duvarın dibindeki
                boş zemin · MERAK SORUSU: "Buraya ne yapıyorlar?"
İŞLEV ANI       S11 (88,0–96,0) şelale gerçek hızda akmaya başlar · S12 (96,0–104,0) ışıklar tek karede yanar · S13 (104,0–
                112,0) perdenin arkasından içerisi · S14 (112,0–116,0) üç kişi köprüde · 116,0–120,0 tutuş
LOOP RHYME      biçim ve konum: sütun aynı x'te (922–1050) · dibi kirli su → turkuaz su · duvarın dibinde platform → yapı
OMURGA (15)     platform · su gider · temel · iskelet · köprü · teras · cam · salon · kanal · bahçe · dolum · şelale · ışık ·
                perdenin arkası · köprüde üç kişi
SES             MUSIC NO — diegetik ses tasarımı (❷ C2 · ❺ C1)
TESLİM          END CARD NO · SPEED 1x · 120,0 sn
AI BEYANI       YAYIN_PAKETI §AÇIKLAMA sabit beyan bloğu + Studio "Altered content = EVET"
KAPAK           THE_HIDDEN_FALLS_KAPAK.md — G15'ten, bölünmüş yerleşim YOK
PROMPT KAPISI   python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_HIDDEN_FALLS → BLOCK 0 · FIX 11 (08.10.2026) —
                hepsi PLAN §ÜRETİM ÖNCESİ DURUM'da beyanlı
```

---

## 9. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_HIDDEN_FALLS_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  00_ANALIZ/02 §3 — kamera · temel · yapı · köprü · sütun · su kotları · perde · yansıma bandı
⛔ PİLOT ÜÇLÜ     ① G15 + G14 + S14 · ② G11 + G12 + S11 · ③ G10 + G11 + S10 (+ salon S13) — PLAN §PİLOT ÜÇLÜ
⛔ USTA KARE      G15 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil); sütun 128 ±2 px · yapı 751–1339 ±2 px
⛔ GÜNLÜK         klip başına satır (İSTASYON sütunu: ana/salon); günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a; 1920×1080 · 120,0 sn · kart YOK)
⛔ İHRAÇ          bash araclar/ihrac_kontrol.sh — süre 120,0 · kart YOK · müzik YOK · final tutuşu SSIM ≥ 0,90 [DERS 63]
⛔ KAPAK KANITI   ffmpeg -ss 119.5 -i teslim.mp4 -frames:v 1 g15_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g15_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
```
