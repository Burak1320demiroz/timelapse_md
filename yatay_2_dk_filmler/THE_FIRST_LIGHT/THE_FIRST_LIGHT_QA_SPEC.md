# 🔍 THE_FIRST_LIGHT — QA SPEC

> FIRST LIGHT · 16:9 · 20 × 8,0 sn · 160,0 sn · kart yok · müzik VAR (düşük, sözsüz) · tek iç klip (S17). **Bu dosya yalnız
> belgeli merceklere verilir: ❹ İNŞA · ❺ TESLİM** (beş mercekli QA, 06.10.2026 [DERS 64]).
> ⛔ **❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❸ ŞANTİYE'ye VERİLMEZ** — üçü kör koşar, ayrı geçici sohbette, proje dışında
> [`QA_KOSU_KILAVUZU` §1]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit değildir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_FIRST_LIGHT <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].
> Ham raporlar `QA/HAM/THE_FIRST_LIGHT/THE_FIRST_LIGHT_Q<n>_<AD>_HAM.md` · kayıt `QA/FILMLER/THE_FIRST_LIGHT.md` · `QA/TABLO.md`.

---

## 0. KÜNYE

```
FİLM          THE_FIRST_LIGHT — bulut denizinin üstündeki dağ zirvesinde eski bir gözlemevi: kubbe ve teleskop tüpü vinçle
              sökülür, taş temizlenir, bakır kaplama, halka ray ve iç zemin yenilenir, tüp bakımdan geçip geri gelir ve ilk
              kez hareket eder, kapak değişir, kubbe iki klipte yerine oturur, yol ve korkuluk yapılır, şantiye çekilir;
              mavi saatte kapak açılır, teleskop hizalanır, kubbe döner · MAIN STATION + KUBBE (S17)
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_2_dk_filmler · HIZ 1x · ⚠️ 160 sn bu klasörün 2:00 bandının dışı (beyanlı)
KANARYA       cloudpipit   ⛔ kör mercek raporunda bu kelime geçerse plan SIZMIŞTIR → koşu SIZINTI [QA_KOSU §3.1]

TESLİM YAPISI ⭐ SAHNE BLOĞU  20 sahne × 8,0 sn = 160,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  ⛔ YOK                                   ← son sahne S19 son saniyeye kadar SAHNEDİR
                 TOPLAM                          160,0 sn
              ⛔ 160,0 sn'den uzun dosya = plan dışı kart/siyah → ❺ "the plan declares NO card — report it"

SAHNE SAATLERİ  sahne n = n × 8,0 → (n+1) × 8,0   ·   S0 0,0–8,0 · … · S9 72,0–80,0 · S10 80,0–88,0 · … · S19 152,0–160,0
                (19 kesme, her 8,0 sn · müzik 120 BPM → her kesme ölçü başında, 4 ölçü/sahne)
PART GRID       — (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)
⛔ DÜZ IZGARA   sahip senaryosu (hikâye SAPMA ②) · ⚠️ bandın dışı (format 12 × 10,0 · 2:00). Eşit klipte ❷ RHYTHM NOT
                TRIGGERED. Karşı kayıt [DERS 44].
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]: ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — {5,9} ya da {5,10}
   gerekir; {4,6,8} çıkarsa iki-klip hükmü (PLAN §DEĞİŞMEZLER) ve karar sahibe döner.

İKİNCİ İSTASYON BEYANI  S17 (136,0–144,0) KUBBE İSTASYONU — S16'nın son 8 sn'si içeriden, gerçek hız · ortak çapa TAŞ ÖRGÜSÜ
                cümlesi · dış büyüme taşımaz · ❸ bunu "plan dışı istasyon" SAYMAZ; kesme 136,0 ve 144,0'te mekân değişir
                (dış ↔ iç)
EKRAN BİNDİRMESİ S17'de masadaki büyük ekrana gözlem görüntüsü kurguda yerleşir (139,0 sn'den sonra) — üretilmiş görüntü
                değildir; ❶ ekranda ÜRETİLMİŞ yazı/şekil görürse bulgu yazar
TEK OLAY        S10 + S11 (80,0–96,0) kubbenin kalkışı ve oturuşu — 88,0'deki kesme olayın ortasındadır; G11'de kubbe davulun
                üstünde asılı, iki yakada aynı yükseklik ve yön
YAPI          dağ zirvesinde gözlemevi · Ø 24 m alçak granit davul (4 m) · Ø 24 m bakır kubbe (tek yarık, tek kapak, halka ray
              üstünde döner) · çatallı teleskop (koyu gri çatal, soluk beyaz tüp Ø 2,4 × 9 m) · iç zemin · giriş basamakları
              ve taş yol · uçurum terası (eski döşeme, yeni çelik korkuluk) · alçak yol lambaları
SAHA          dağ zirvesi, bulut denizinin üstü · 30° K · çapalar: ⭐ DAĞ ÇAMI (sağ, kaya çıkıntısında — kanıt) · iki uzak
              tepe (ikiz doruk sol · uzun düz sırt sağ) · ufuk %77,4 · bulut denizinin düzeyi
ZAMAN YAYI    ≈1 yıl (kış → ertesi sonbahar) · film mertebe anlatır: "bir kış söküm, bir bahar bakım, bir yaz kubbe, bir sonbahar ilk ışık"
IŞIK          TEK GÜN 07:35 → 18:05 (koyu mavi saat) · Σ rejim 10 sa 30 dk · takvim SAHADAN (gök + bakırın rengi) · bilinçli
              sıkıştırma (ÜSLUP BEYANI) · güneş bütün gün kameranın ARKASINDA · gün batımı S14'ün içinde
REJİM         A (10 dk) × 15 (S0 · S1 · S4 · S6–S13 · S15 · S16 · S18 · S19) · B (2 sa) × 4 (S2 · S3 · S5 · S14) · G (gerçek zaman)
              × 1 (S17, iç klip, S16 içinde ∥) — ⚠️ üç rejim, beyanlı
KAMERA        MAIN STATION — h 28,0 m · D_eksen 64,0 · D_kenar 52,0 · bakış 0° · tilt 13° AŞAĞI · roll 0° · KUBBE — h 2,0 (kattan) ·
              bakış 160° · tilt 0°
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G20 usta kare → G19 → G18 → G16 → … → G0 · iç kareler G17′ → G17 ayrı · her kare zincir_kontrol
GÜNLÜK        THE_FIRST_LIGHT_URETIM_GUNLUGU.md — ⛔ boş (üretim başlamadı) → bu SPEC'in hükmü üretimle başlar
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı · ❺ FINAL BEAT

```
SAHNE       S19 (152,0–160,0)
FİNAL BEAT  152,0–156,0 olay: iki kişi kapıyı kapatıp terastan korkuluğa yürür, küçük servis aracı sol yoldan çıkar ·
            156,0–160,0 TUTUŞ: kubbe durgun, yarık kameraya açık, kırmızı ışık sabit, iki kişi korkulukta kıpırtısız; yalnız
            bulut denizi akar, yıldızlar parlar
SANİYE      159,0 (son 4,0 sn'lik TUTUŞUN içi [P2-i]; koyu mavi saat, okunur [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (beşi de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① kameraya açık yarık + içinde loş kırmızı ışık (x 1125–1195 · üstten 487 → 807)
   ② yarığın içinde göğe dönük soluk beyaz tüp
   ③ bütün kubbe (kahve bakır) davulun üstünde + temiz granit davul (x 920–1400 · ön dip 890) + açık renkli yol ve basamaklar
   ④ korkulukta iki küçük kişi, kadrajın İÇİNDE (x ≈1600 · ≈30 px · yüz okunmaz)
   ⑤ AYNI çam (kanıt nesnesi: x 1652–1805 · taç 551 · 153 px — G0 ile aynı konum ve boy) + iki uzak tepe + bulut denizi
   + geçici ekipman GİTMİŞ: vinç, iskele kuleleri, sehpa, beşik, istif, kamyon, servis aracı YOK (SÖKÜM satırı)
   + BEDEL görünür: yeşil kubbe ve kirli, sarmaşıklı taş yok; yerinde kahve bakır ve temiz taş (G0 ↔ G20)

KOMUT
   ffmpeg -ss 159.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①–⑤'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP (biçim kafiyesi, ışık bilinçli farklı)
   ffmpeg -ss 0.3   -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 kanit_g20.jpg
   İki karede çam, iki tepe ve ufuk aynı yerde; çam aynı x'te (1652–1805 ±2 px). Davul iki karede AYNI yerde (920–1400 ·
   ön dip 890): G0'da üstünde havada yeşil kubbe, G20'de oturmuş kahve kubbe.
   Işık: G0 sabah ↔ G20 koyu mavi saat (PLAN LOOP satırı) — kanıt çifti AYNI IŞIK iddiası taşımaz.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=28,0 · tilt 13° aşağı · KAMERA_DILI §3 · yüzde ALT kenardan)

| nesne | y (m) | d (m) | yüzde (alt kenardan) | x (soldan) | px boy | her karede |
|---|:-:|:-:|:-:|:-:|:-:|---|
| ufuk (tilt 13°) | — | — | 77,4 (244) | bütün en | — | ✓ |
| ikiz doruklu tepe · uzun düz sırt | uzak | ≈5 km | ≈78–82 | sol · sağ | — | ✓ siluet (⚠️ usta karede ölçülür) |
| kubbe tepesi (havada G0) | +18 | 63 | 58,2 (451) | 716–1204 | — | yalnız G0 |
| kubbe tepesi (asılı G11) | +19 | 64 | 60,4 (428) | 920–1400 | — | yalnız G11 · taban 39,3 (656) |
| kubbe tepesi (davulda) | +16 | 64 | 54,9 (487) | 920–1400 | — | G12+ |
| kubbe tepesi (sehpada) | +13,5 | 62 | 49,7 (544) | 382–877 | — | G1–G10 |
| tüp tepesi (dik) | +12 | 64 | 47,9 (563) | 1136–1184 | 48 en | G0–G1 · G9–G11 |
| tüp (yatay) | +5,5 | 64 | 36,8 (683) | 1070–1250 | 180 en | yalnız G8 |
| davul duvar tepesi (arka) | +4 | 76 | 40,6 (641) | — | — | ✓ (kubbesiz G0–G11) |
| çatal kolu tepesi | +6,5 | 64 | 38,4 (665) | ≈1090–1230 | — | G0–G11 (kubbesiz) |
| iç zemin (arka → kaide) | 0 | 76 → 64 | 35,0 → 27,8 (702 → 780) | ≈940–1380 | ≈105 boy | G0–G11 · G6'dan sonra açık panel |
| davul duvar tepesi (ön) | +4 | 52 | 25,3 (807) | 920–1400 | — | ✓ · G5'ten sonra parlak ray bandı |
| kapı tepesi | +3 | 52 | 23,3 (828) | 1175–1237 | — | ✓ |
| davul dibi (ön) | 0 | 52 | 17,6 (890) | — | — | ✓ |
| yol + basamaklar | 0 | ≈49 | 14,3 (925) | ≈800–1240 | — | G13'ten sonra açık plaka |
| ⭐ kanıt nesnesi ÇAM | +2 → +16 | 50 | 19,4–49,0 (870–551) | 1652–1805 | 153 × 319 | ✓ BİREBİR (boy dâhil) · iğne yapraklı, değişmez |
| beşik (önde sol) | 0 → +2 | 50 | 15,5–19,4 (913–870) | 140–371 | — | G0–G14 |
| istif alanı | 0 → +2 | 50 | 15,5–19,4 (913–870) | 601–755 | — | G0–G14 (büyür) |
| iskele kuleleri | 0 → +7 | 58 | → 35,6 (695) | 872–938 · 1424–1490 | — | G0–G14 |
| teras + korkuluk | 0 → +1 | 56–72 | 21,4 → 34,3 | 1486–1829 | — | korkuluk G14+ |
| vinç | taban 0 · bom kadraj dışı | 84 | 38,7 taban (662) | ≈914 | — | G0–G15 · S15'te çıkar |
| yarık (sehpada, sağ önde) | +1,5 → | 62 | 21,8 → | ≈750–810 (taban) | — | G1–G10 kapalı |
| yarık (davulda, sağ önde) | +4 → +16 | ≈53–64 | 26,0 → 54,9 | ≈1275–1340 (taban) | — | G11–G18 (G18'de açık) |
| yarık (önde) | +4 → +16 | ≈52–64 | 25,4 → 54,9 | ≈1125–1195 | — | G19–G20 açık |
| iki kişi | 0 → +1,7 | ≈51 · ≈60 | — | ≈1200 (G19) · ≈1600 (G20) | ≈35 · ≈30 boy | G16–G20 |

```
KAMERA SABİTLİK  ilk/son kare kayması ≤ 2 px (1080p · KAMERA_ISTASYONU §7 · zincir_kontrol ESIK_KAYMA_ORAN) ·
                 üç nirengi: çam tacının sol ucu · ikiz doruğun sol zirvesi · davulun sol dip köşesi
KUBBE İSTASYONU  büyük ekran x 140–780 · %12–50 · çatal x 900–1260 · yarık x 1300–1480 (≈180 px · %64 → üst kenar) · iki kişi
                 masanın sağ ucunda — ⚠️ tarif edildi, hesaplanmadı; G17′ usta iç karede ölçülür
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
davul Ø 24 m (x −2…+22 · eksen d 64) · 4 m · tek kemerli kapı (≈2,5 × 3) · duvar tepesinde halka ray · iç zemin Ø 22 · kubbe
Ø 24 m · tepe +16 · yarık ≈3 m · tek bakır kapak (yukarı kayar) · teleskop kaide Ø 3 · +2 · çatal kolları +6,5 · tüp Ø 2,4 × 9 m
(eksen +5,5 · dik parkta tepe +12) · teras x +23…+38 · d 56–72 · yol d ≈49 · ped x −45…0 · bakım sehpası Ø 24 (yürüme yolu)
· beşik 9 m (x −32…−23 · d 50) · istif alanı (x −14…−8 · d 50) · iki iskele kulesi ≈7 m · paletli vinç (x −3 · d 84 ·
G0–G15) · çam x +27…+33 · d 50 · dip +2 · tepe +16
```

### Yapı yüzdesi ve saha durumu — sahne sahne (❹ İNŞA · ❺ TESLİM için)

| S | saat | yapı: eleman + ara hâl | kubbe · teleskop | geçici ekipman kadrajda | saha / gök / mevsim |
|:-:|:-:|---|---|---|---|
| S00 | 07:35→07:45 | — · eski yüz (kir, sarmaşık, yeşil bakır, paslı ray, koyu zemin, çatlak yol) | kubbe havada → sehpada · tüp çatalda dik | vinç (kubbe yükte) · düz kasalı kamyon (boş kasalar) · 2 kule · sehpa · beşik · ekip | kış · sabah |
| S01 | 07:45→07:55 | — | tüp çataldan → beşiğe | vinç (tüp yükte) · küçük kamyon (kasalar) | kış |
| S02 | 07:55→09:55 | taş temiz %0 → %100 (soldan) | — | 2 kule (yıkama) · kasalar → istif · küçük kamyon · vinç (bom dışarıda) | kış |
| S03 | 09:55→11:55 | — | kubbe yeşil → yeni bakır · eski kapak kalır | vinç (bakır paleti) · düz kasalı kamyon · yeşil panel istifi | bahar |
| S04 | 11:55→12:05 | ray paslı → yeni %100 | — | vinç (ray parçası) · düz kasalı kamyon · eski ray istife | bahar · bakır pembe |
| S05 | 12:05→14:05 | iç zemin koyu → açık %100 (arkadan) | — | vinç (zemin paleti) · kamyon · eski tahta istife | bahar |
| S06 | 14:05→14:15 | — | beşikte tüp panelleri kirli → yeni | vinç (panel paleti) · kamyon · eski panel istife | bahar |
| S07 | 14:15→14:25 | — | tüp beşikten → çatala, yatay | vinç (tüp + çerçeve) · beşik boşalır | bahar |
| S08 | 14:25→14:35 | — | ⭐ tüp yatay → dik (ilk hareket) | vinç (boş çerçeve → kamyon) · ikinci kamyon (yeni kapak gelir) | ⭐ yaz |
| S09 | 14:35→14:45 | — | eski yeşil kapak → yeni bakır kapak | vinç (kapak) · kamyon · eski kapak istife | yaz |
| S10 | 14:45→14:55 | — | ⭐ kubbe sehpadan → davulun üstünde ASILI | vinç (kubbe) · yürüme yolu tahtaları istife | yaz |
| S11 | 14:55→15:05 | — | ⭐ kubbe asılı → halka rayda (DORUK) | vinç (kubbe) · kamyon (taş plakalar gelir) | yaz |
| S12 | 15:05→15:15 | yol + basamaklar eski → yeni %100 · lambalar | — | vinç (plaka paleti) · kamyon · eski basamak istife | yaz · bakır kahveye döner |
| S13 | 15:15→15:25 | korkuluk %0 → %100 | — | vinç (korkuluk demeti) · kamyon | yaz |
| S14 | 15:25→17:25 | (değişmez) · gün batımı | — | 2 kule söküm · sehpa + beşik + istif kamyonlarla gider · vinç (bom sonunda dışarıda) | ⭐ sonbahar · gün batımı |
| S15 | 17:25→17:35 | (değişmez) · yol lambaları belli belirsiz yanar | — | vinç (bomu yatar → çıkar) · küçük kamyon (alet kasaları) | sonbahar |
| S16 | 17:35→17:45 | (değişmez) | kapak kapalı → açık (sağ önde) · tüp yarığa | servis aracı gelir · iki kişi (küçük sandık) | sonbahar · mavi saat |
| S17 | 17:45 +8 sn | (iç) | teleskop son salınım → hizalı | — (iç: masa, büyük ekran, iki kişi sırtı dönük) | yarıkta koyu mavi gök |
| S18 | 17:45→17:55 | (değişmez) | kubbe ≈30° döner: yarık sağ önden → öne | servis aracı · iki kişi (ikinci sandık) | ilk yıldızlar |
| S19 | 17:55→18:05 | (değişmez) · TUTUŞ | — | servis aracı çıkar | koyu mavi saat |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   DAĞ ÇAMI — G0…G20 (G17 hariç) hepsinde x 1652–1805 · taç 551 · dip 870 · 153 px en; zincirde her karede ELLE
                ✓/✗ (günlük §2) · iğne yapraklı, mevsim taşımaz (çapa)
İKİNCİ ÇAPA     ikiz doruklu tepe (siluet) · üçüncü: ufuk 244 · dördüncü: davulun ön dibi 890 (G0'dan G20'ye aynı yerde)
İÇ KLİP         ortak cümle TAŞ ÖRGÜSÜ (uzun alçak sıralar, ince koyu derz) — dışarıda davulun ön yüzü, içeride iç duvar; çam
                yarıktan GÖRÜNMEZ (yarık 159°, çam 125°) · ölçülebilir çapa yarığın genişliği (≈180 px)
❸ İÇİN          dikiş = KARE (G1…G19): dikişin iki yakası aynı görsel; ❸ REBUILT hükmü zincir koşulmadı demektir · S17 iç
                klibi beyanlı ikinci istasyon (künye)
⚠️ BULUT DENİZİ yüzeyi her klipte akar (B'de yuvarlanır) — DÜZEYİ sabit; ❸ ve ❶ yüzey hareketini "arka plan değişti" saymamalı
```

---

## 5. ❹ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ajanı · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | ajan (taşıyan) | geçici destek | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|---|:-:|:-:|:-:|
| kubbe (söküm) | davulun üstü | paletli vinç | dört sapan · kılavuz ip · bakım sehpası | G0 (havada) | G1 (sehpada) | sehpa S14 |
| tüp (söküm) | çatal | vinç | dört sapan · çelik beşik | G1 (sapanda) | G2 (beşikte) | beşik S14 |
| temiz taş | — (sarmaşık + yıkama) | 2 iskele kulesi + basınçlı su · ekip | kuleler | G2 (kirli) | G3 | kuleler S14 · kasalar istife |
| bakır kaplama | düz kasalı kamyonda paletler | vinç → sehpanın yürüme yolu · ekip | yürüme yolu | G3 (yeşil) | G4 | yeşil panel istife · istif S14 |
| halka ray | düz kasalı kamyon | vinç · ekip | sapan · kuleler | G4 (paslı) | G5 | eski ray istife |
| iç zemin | düz kasalı kamyonda paletler | vinç · ekip | sapan | G5 (koyu) | G6 | eski tahta istife |
| tüp panelleri | düz kasalı kamyonda paletler | vinç · ekip | beşik | G6 (kirli) | G7 | eski panel istife |
| tüp (geri) | beşik (çerçevede) | vinç | çerçeve · dört sapan | G7 (beşikte) | G8 (çatalda yatay) | çerçeve S8 kamyonla |
| ilk hareket | (gizli) motor | — | — | G8 (yatay) | G9 (dik park) | — |
| kapak | S8 sonunda kamyonla | vinç · ekip | sapan · yürüme yolu | G9 (yeşil kapak) | G10 | eski kapak istife |
| kubbe (montaj) | sehpa | vinç | dört sapan · kılavuz ip · kuleler | G10 (sehpada) | G12 (rayda) | yürüme yolu S10 · sehpa S14 |
| yol + basamaklar | S11 sonunda kamyonla plaka paletleri | vinç · ekip | — | G12 (eski) | G13 | eski basamak istife |
| korkuluk | kamyonda demetler | vinç · ekip | — | G13 (çıplak kenar) | G14 | — |
| yarık açılışı | (gizli) motor | — | kapak kızakları | G16 (kapalı) | G18 | — |
| kubbe dönüşü | (gizli) motor | — | halka ray | G18 (yarık sağ önde) | G19 (önde) | — |

```
❹ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır):
   gözlemevi 1 (davul + kubbe) · teleskop 1 · sarı paletli vinç 1 (G0–G15) · düz kasalı kamyon (değişen yükler) · küçük kamyon
   · iki çelik iskele kulesi (G0–G14) · kubbe bakım sehpası 1 (G0–G14) · çelik beşik 1 (G0–G14) · istif alanı (G0–G14) ·
   küçük servis aracı (G16–G19) · ekip (iz) · S16–S20 iki kişi · S17 iç: masa, büyük karanlık ekran, kırmızı lambalar, kısa
   merdiven · çam 1 · iki uzak tepe · bulut denizi
   ⛔ DAVETSİZ: ikinci kubbe/gözlemevi · zirve oteli · şapel/dini yapı · anten ormanı · kule vinç · göğe ışık sütunu ·
      dış gökte gezegen/ay · uçak izi · yazı / işaret / tabela · ikinci teleskop · ekranda üretilmiş yazı
❹ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: temiz taş = S2 kuleler + yıkama · yeni bakır = S3 yürüme
                  yolu + paletler · yeni ray = S4 vinç + kamyon · zemin = S5 vinç + paletler · temiz tüp = S6 paletler ·
                  tüp çatalda = S7 vinç · dik tüp = (gizli) S8 motor · yeni kapak = S9 vinç · kubbe = S10–S11 vinç · yol =
                  S12 plakalar · korkuluk = S13 demetler · açık yarık = (gizli) S16 · dönüş = (gizli) S18
❹ ÇERÇEVE DEFTERİ davul x 920–1400 sabit (G0 → G20) · ön dip 890 · ön duvar tepesi 807 · çam 153 px sabit
❹ GİZLİ İŞ        optiğin bakımı → beşikte panel panel yenilenen tüp (S6) · motor/elektrik → S8 dikilen tüp, S16 kapak +
                  lambalar, S18 dönüş · gözlem → S17 ekran (kurguda bindirme)
❹ DECLARED WORLD  dağ zirvesi · bulut denizi · ekipli söküm-montaj · vinç (G0–G15) · iç klip (S17) · iki kişi (G16–G20) · mavi
                  saat (G16–G20) · kış görüntüsü YOK · gezegen dış gökte YOK
❸ PARKED GEREKÇESİ S19 (final tutuşu): şantiye bitti; iki kişinin yürüyüşü ve aracın çıkışı dışında hareket yok — ödül ve
                  sakin an, işsiz aralık değil, beyanlı [P4-f · C1-d]
```

---

## 6. ❷ ZAMAN VE KESME — kesme listesi ve ses (❷ kör koşar; bu bölüm ❺ ve operatör içindir)

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_FIRST_LIGHT/THE_FIRST_LIGHT_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
REJİM KESMELERİ      16,0 (S1 A → S2 B) · 32,0 (S3 B → S4 A) · 40,0 (S4 A → S5 B) · 48,0 (S5 B → S6 A) · 112,0 (S13 A → S14 B)
                     · 120,0 (S14 B → S15 A) · 136,0 (S16 A → S17 G · dış → iç) · 144,0 (S17 G → S18 A · iç → dış) — rejim
                     ve istasyon değişimi YALNIZ kesmede [P5-c]
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı ATLAMAZ · 136,0 ↔ 144,0 iç klip:
                     dış kare G18 iki yakada aynı · 88,0 kubbe asılı (TEK OLAY)
MÜZİK                ✅ VAR — düşük seviyeli, sözsüz, 120 BPM · 4 ölçü/sahne · diegetik yatak önde · THE_FIRST_LIGHT_MUZIK.md:
                     0–16 kanca (vinç + rüzgâr) · 16–80 bakım · 80–96 kubbe (müzik genişler) · 96–128 tamamlama ve çekilme ·
                     128–152 açılış, iç, dönüş · 152–160 sönüm — ani kesilme yok
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G10 (S9 ↔ S10) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si (S9) G10 karesinde biter; G10 BOLUM_2'nin ilk görselidir.
ELLE KARE            ffmpeg -ss 80.0 -i teslim.mp4 -frames:v 1 sinir.jpg → teleskop dik park (kubbesiz davulda) · kubbe
                     sehpada pembe bakır, YENİ kapak, dört sapanı vince bağlı · beşik boş · kuleler yerinde · yol eski · teras
                     çıplak · gölge +47° · yaz
```

---

## 8. ❺ TESLİM — belgeli merceğin okuyacağı beyanlar

```
VAAT            Bulutların üstündeki eski bir gözlemeviyi söküp onarmak ve yeniden göğe baktırmak.
DİRENÇ          ① ağırlık — S0 (0,0–8,0) havadaki kubbe · S1 tüp · S7 (56,0–64,0) tüp geri · S10–S11 (80,0–96,0) kubbe ·
                ② yıpranma — S0–S2 kir, sarmaşık, yeşil bakır, paslı ray · S2 (16,0–24,0) şerit şerit temizlik · S3 (24,0–
                32,0) sökülen yeşil paneller · S5 (40,0–48,0) aşınmış zemin · ③ hassas makine — S6–S8 (48,0–72,0) tüp bakımı,
                dönüşü, ilk hareketi
BEDEL           eski yüz — yeşil bakır ve kirli, sarmaşıklı taş: S2, S3 ve S9'da gider; G20'de aynı yerde kahve bakır ve temiz taş
AÇILIŞ          nesne: vinçte asılı yeşil kubbe · eylem: kubbe ilk karede sola kayıyor · ipucu: açık davulda tozlu teleskop ·
                MERAK SORUSU: "Bu terk edilmiş gözlemevi yeniden çalışacak mı?"
İŞLEV ANI       S8 (64,0–72,0) tüp ilk kez hareket eder · S16 (128,0–136,0) kapak açılır, kırmızı ışık · S17 (136,0–144,0)
                içeride teleskop hizalanır, ekranda ilk görüntü · S18 (144,0–152,0) kubbe döner, yarık kameraya gelir ·
                156,0–160,0 tutuş
LOOP RHYME      biçim ve konum: kubbenin yarım küresi davulun üstünde — G0'da havada ve yeşil, G20'de oturmuş, yarığı açık ·
                çam aynı x'te (1652–1805)
OMURGA (20)     kubbe kalkar · tüp çıkar · taş temizlenir · bakır kaplanır · ray yenilenir · zemin döşenir · tüp bakımı · tüp
                geri · test · kapak değişir · kubbe kalkar · oturur · yol · korkuluk · şantiye gider · vinç gider · yarık
                açılır · teleskop hizalanır · kubbe döner · göğe bakar
SES             MUSIC YES — low, wordless, 120 BPM, under the site sound (❷ C2 · ❺ C1)
TESLİM          END CARD NO · SPEED 1x · 160,0 sn · SECOND STATION YES (S17, declared) · SCREEN INSERT YES (S17, post)
AI BEYANI       YAYIN_PAKETI §AÇIKLAMA sabit beyan bloğu + Studio "Altered content = EVET"
KAPAK           THE_FIRST_LIGHT_KAPAK.md — G20'den, bölünmüş yerleşim YOK
PROMPT KAPISI   python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_FIRST_LIGHT → BLOCK 0 · FIX 2 (10.10.2026) —
                hepsi PLAN §ÜRETİM ÖNCESİ DURUM'da beyanlı
```

---

## 9. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_FIRST_LIGHT_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  00_ANALIZ/02 §3 — kamera (h 28 · tilt 13°) · iç zemin ön duvarın üstünden görünüyor mu · sehpa · beşik ·
                  istif · kuleler · çam · iki tepe
⛔ PİLOT ÜÇLÜ     ① G20 + G19 + G18 + S18 · ② G0 + G1 + S0 · ③ G17 + G17′ + S17 — PLAN §PİLOT ÜÇLÜ · sonra S10 + S11
⛔ USTA KARE      G20 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil); çam 153 ±2 px · davul 920–1400 ±2 px
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ EKRAN BİNDİRMESİ görüntü seçimi + kaynak/lisans (günlük §5) · dört köşe takibi S17'de 139,0–144,0
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a; 1920×1080 · 160,0 sn · kart YOK)
⛔ İHRAÇ          bash araclar/ihrac_kontrol.sh — süre 160,0 · kart YOK · müzik VAR · final tutuşu SSIM ≥ 0,90 [DERS 63]
⛔ KAPAK KANITI   ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
⛔ SÜRE / KLASÖR  160 sn yatay_2_dk bandının dışı — sahip kararı (hikâye SAPMA ②)
```
