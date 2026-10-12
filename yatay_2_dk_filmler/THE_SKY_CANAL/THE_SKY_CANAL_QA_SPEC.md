# 🔍 THE_SKY_CANAL — QA SPEC

> THE SKY CANAL · 16:9 · 20 × 8,0 sn · 160,0 sn · kart yok · müzik VAR (altta, sözsüz) · tek istasyon. **Bu dosya yalnız
> belgeli merceklere verilir: ❹ İNŞA · ❺ TESLİM** (beş mercekli QA, 06.10.2026 [DERS 64]).
> ⛔ **❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❸ ŞANTİYE'ye VERİLMEZ** — üçü kör koşar, ayrı geçici sohbette, proje dışında
> [`QA_KOSU_KILAVUZU` §1]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit değildir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_SKY_CANAL <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].
> Ham raporlar `QA/HAM/THE_SKY_CANAL/THE_SKY_CANAL_Q<n>_<AD>_HAM.md` · kayıt `QA/FILMLER/THE_SKY_CANAL.md` · `QA/TABLO.md`.

---

## 0. KÜNYE

```
FİLM          THE_SKY_CANAL — derin bir nehir vadisinin üstünde, hazır iki ayak ve iki mesnet arasına tekne taşıyan çelik
              kanal köprüsü kurulur: üç açıklık parçası vinçle oturur, enine kirişler, taban, iki duvar, kıyı bağlantıları,
              açık mavi iç kaplama, bakım yolu, korkuluk, kömür grisi dış boya; şantiye çekilir; oluk borudan soldan dolar,
              seviye kıyılarla eşitlenir, kapaklar kalkar; solda bekleyen kırmızı tekne köprüden karşıya geçer · MAIN STATION
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_2_dk_filmler · HIZ 1x · ⚠️ 160 sn bu klasörün 2:00 bandının dışı (beyanlı)
KANARYA       tillerfinch   ⛔ kör mercek raporunda bu kelime geçerse plan SIZMIŞTIR → koşu SIZINTI [QA_KOSU §3.1]

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

İSTASYON        tek — MAIN STATION, 20/20 klip · ❸ ikinci istasyon görürse bulgu yazar
TEK DOLUM       S13 + S14 + S15 (104,0–128,0) — aynı borudan, soldan sağa, kot yalnız artar; 112,0 ve 120,0'deki kesmeler dolumun
                ortasındadır, su cephesi ve seviye iki yakada aynı
TEK GEÇİŞ       S17 + S18 + S19 (136,0–160,0) — aynı tekne, aynı hız, aynı eksen; 144,0 ve 152,0'deki kesmeler yolculuğun
                ortasındadır, tekne iki yakada aynı yerde
YAPI          nehir vadisi üstünde çelik kanal köprüsü · 100 m · üç açıklık (30 + 40 + 30) · üstü açık oluk iç 8 m × 2 m · iki
              açık renkli beton ayak + iki kıyı mesnedi · yakın tarafta galvanizli bakım yolu + korkuluk + uçlarda basamak · iki
              uçta düşey kalkan çelik kapak · sol kıyıda dolum borusu (vana tekerleği)
SAHA          derin, ağaçlı nehir vadisi · 47° K · çapalar: ⭐ ÇAM (sağ yamaçta kaya çıkıntısında — kanıt) · iki ayak · nehir ·
              iki uzun ağaçlı sırt · ufuk %86 · sol havuz + sağ kanal kolu
ZAMAN YAYI    ≈5 ay üst yapı (geç ilkbahar → ekim) + tek dolum günü · film mertebe anlatır: "bir bahar parçalar, bir yaz oluk, bir
              sonbahar su ve tekne"
IŞIK          TEK GÜN 08:20 → 16:43 (altın saat) · Σ rejim 8 sa 23 dk · takvim SAHADAN (yamaçlardaki ağaçların rengi) ·
              bilinçli sıkıştırma (ÜSLUP BEYANI) · güneş hiçbir karede kadrajda değil
REJİM         A (10 dk) × 14 (S0–S2 · S4–S7 · S9 · S10 · S12–S16) · B (2 sa) × 3 (S3 · S8 · S11) · Y (≈1 dk · ≈8×) × 3 (S17–S19,
              tekne) — ⚠️ üç rejim, beyanlı · ⚠️ Y depoda YENİ, ölçülmedi
KAMERA        MAIN STATION — h 85,0 m (nehirden) · D_eksen 135,0 · D_kenar ≈107 · bakış 20° · tilt 17° AŞAĞI · roll 0° · köprü
              ekseni görüntü düzlemine 20°
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G20 usta kare → G19 → … → G0 · her kare zincir_kontrol
GÜNLÜK        THE_SKY_CANAL_URETIM_GUNLUGU.md — ⛔ boş (üretim başlamadı) → bu SPEC'in hükmü üretimle başlar
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı · ❺ FINAL BEAT

```
SAHNE       S19 (152,0–160,0)
FİNAL BEAT  152,0–156,0 olay: kırmızı tekne merkez açıklıktan sağ ayağın üstünden sağ kapağa gelir, yavaşlar, burnu kapak
            çerçevesinde durur; bakım yolundaki iki kişi yanında durur · 156,0–160,0 TUTUŞ: tekne kıpırtısız, iz söner,
            köprü, açık kapaklar ve kanal kolları değişmez; yalnız aşağıda nehir akar
SANİYE      159,0 (son 4,0 sn'lik TUTUŞUN içi [P2-i]; altın saat, okunur [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (beşi de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① sağ uçta kırmızı gövdeli, krem kabinli tekne, tamamı kadrajın İÇİNDE (x 1242–1368 · üstten 549–575)
   ② dolu oluğun su bandı (uzak duvarda su çizgisi ≈591, kıyı kanallarıyla aynı seviye) + iki kapak YUKARIDA
   ③ bütün köprü (kömür grisi, galvanizli korkuluk, mavi iç) iki ayağın üstünde (x 538 → 1398)
   ④ çok aşağıda nehir (merkez açıklığın altında x ≈1002 · üstten 888) — köprünün suyundan AYRI
   ⑤ AYNI çam (kanıt nesnesi: x 1475–1547 · tepe 622 · 72 px — G0 ile aynı konum ve boy) + sonbahar yamaçları + sırtlar
   + geçici ekipman GİTMİŞ: vinç, kamyon, palet, kalas, istif YOK (SÖKÜM satırı)
   + BEDEL görünür: iki ayağın arasındaki boşluk yok; yerinde suyla dolu köprü (G0 ↔ G20)

KOMUT
   ffmpeg -ss 159.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①–⑤'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP (biçim kafiyesi, ışık bilinçli farklı)
   ffmpeg -ss 0.3   -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 kanit_g20.jpg
   İki karede çam, iki ayak, iki mesnet ve ufuk aynı yerde; çam aynı x'te (1475–1547 ±2 px). G0'da tekne SOLDA havuzda
   (161–381), ayakların arası boş; G20'de AYNI tekne SAĞDA köprünün ucunda (1242–1368), köprü dolu.
   Işık: G0 serin sabah ↔ G20 altın saat · ağaçlar açık yeşil ↔ sonbahar (PLAN LOOP satırı) — kanıt çifti AYNI IŞIK
   iddiası taşımaz.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=85,0 · tilt 17° aşağı · iğne deliği izdüşümü · üstten px)

| nesne | kot (m) | x (soldan) | üstten | her karede |
|---|:-:|:-:|:-:|---|
| ufuk (tilt 17°) | — | bütün en | 149 (%86) | ✓ |
| iki uzun ağaçlı sırt | uzak | sol · sağ | ≈100–200 | ✓ siluet (⚠️ usta karede ölçülür) |
| sol mesnet duvar tepesi (yakın) | +37,0 | 538 | 670 | ✓ |
| sol kapak çerçevesi tepesi | +44 | 529 | 589 | ✓ · kapak G17+ yukarıda |
| sol ayak tepesi → dibi | +31,5 → +8 | 844 | 684 → 882 | ✓ |
| sağ ayak tepesi → dibi | +31,5 → +8 | 1182 → 1172 | 636 → 819 | ✓ |
| sağ mesnet duvar tepesi (yakın) | +37,0 | 1398 | 561 | ✓ |
| sağ kapak çerçevesi tepesi | +44 | 1383 | 497 | ✓ |
| oluk merkez: uzak duvar tepesi / uzak taban / yakın duvar tepesi | +37 / +35 / +37 | 992–1018 | 587 / 603 / 609 | G6+ (iki duvar) |
| oluk merkez: dolu su çizgisi (uzak duvarda) | +36,5 | 992 | 591 | G16+ |
| kiriş altı (merkez) | +31,5 | 1018 | 656 | G3+ |
| bakım yolu korkuluğu (merkez) | +37,9 | 1026 | 607 | G11+ |
| ⭐ kanıt nesnesi ÇAM | +30 → +48 | 1475–1547 | 622–819 | ✓ BİREBİR (72 px en, boy dâhil) · iğne yapraklı, değişmez |
| tekne (havuz) | +36,5 → +38,8 | 161–381 | 682–719 | G0–G17 |
| tekne (köprü, sol ayakta) | +36,5 | 620–796 | 631–653 | G18 |
| tekne (merkez açıklık) | +36,5 | 974–1121 | 590–609 | G19 |
| tekne (sağ uç, burnu sağ kapakta) | +36,5 → +38,8 | 1242–1368 | 549–575 | G20 |
| sol vinç tabanı | +37,2 | ≈413 | ≈609 | G0–G12 |
| sağ vinç tabanı | +37,2 | ≈1605 | ≈592 | G0–G12 |
| sağ parça istifi (pedde) | +38,5 | 1491–1687 | 543–569 | G0–G1 |
| merkez parça kalasta (nehrin üstü) | +4 → +7,5 | 839–1152 | 804–890 | G0–G2 |
| nehir (köprü altında · 300 m yukarıda) | 0 | 1002 · 981 | 888 · 514 | ✓ akar |
| havuz sonu · sağ kanal (s 70) | +36,5 | 65 · 1505 | 719 · 539 | ✓ |

```
KAMERA SABİTLİK  ilk/son kare kayması ≤ 2 px (1080p · KAMERA_ISTASYONU §7 · zincir_kontrol ESIK_KAYMA_ORAN) ·
                 üç nirengi: çam tepesinin sol ucu · sol ayak tepesinin yakın köşesi · sağ kapak çerçevesinin tepesi
OLUĞUN İÇİ       bakış 20,3° · yakın duvar tabanın 5,0 m'sini gizler → uzak 3,0 m taban + uzak duvarın iç yüzü görünür
                 (merkezde ≈16 + 6 px) — mavi bant ve su bandı İNCE ama boydan boya; ❶ "oluğun içi görünmüyor" demeden
                 önce bu bant ölçülür (hikâye SAPMA ④)
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
köprü s −50…+50 (100 m) · açıklıklar 30 + 40 + 30 · ayaklar s ±20 · mesnetler s ±50 · eksen görüntü düzlemine 20° · iki
ana kiriş off ±4 · +31,5 → +35,0 · oluk iç 8 m · taban +35,0 · duvar tepesi +37,0 · dolu su +36,5 (dörtte üç) · sığ su
≈ +35,2 (onda bir) · bakım yolu off −4,4…−6 · +36,8 · korkuluk +37,9 · kapak çerçeveleri +44 · kanallar +36,5 · sol havuz
s −50…−90 (16 m) · sağ kol s +50…+75 · tekne ≈18 × 3,5 m, kabin tepesi +38,8 · nehir ≈15 m, kot 0 · kamera (0, 0, 85) ·
köprü merkezi (5, 135) · çam (46, 98) +30 → +48
```

### Yapı yüzdesi ve saha durumu — sahne sahne (❹ İNŞA · ❺ TESLİM için)

| S | saat | yapı: eleman + ara hâl | su · tekne · kapak | geçici ekipman kadrajda | saha / mevsim |
|:-:|:-:|---|---|---|---|
| S00 | 08:20→08:30 | sol parça ASILI → oturur | kuru (oluk yok) · tekne havuzda · kapaklar kapalı | sol vinç (sol parça yükte) · sağ vinç (sağ parçaya bağlı) · kalaslar · kalas kamyonu · ekip | geç ilkbahar · sabah |
| S01 | 08:30→08:40 | sağ parça pedden → sağ açıklık | aynı | sağ vinç (sağ parça) · sol vinç (bom dışarıda → sonunda merkez parçaya bağlanır) · serbest kalas istifi | geç ilkbahar |
| S02 | 08:40→08:50 | ⭐ merkez parça kalastan DİMDİK yukarı → oturur · kıyılar birleşir | aynı | sol vinç (merkez parça, yayıcı kiriş) · sağ vinç (bom dışarıda) · kalas yığını nehir kıyısında · sonunda kiriş kamyonları | geç ilkbahar |
| S03 | 08:50→10:50 | enine kirişler %0 → %100 (iki uçtan) | aynı | iki vinç (kiriş demetleri) · kamyonlar · küçük kamyon (kalaslar) | geç ilkbahar |
| S04 | 10:50→11:00 | taban panelleri %0 → %100 | aynı | iki vinç (panel paletleri) · kamyonlar | ⭐ yaz |
| S05 | 11:00→11:10 | uzak duvar %0 → %100 | aynı | iki vinç (duvar panelleri) · kamyonlar | yaz |
| S06 | 11:10→11:20 | yakın duvar %0 → %100 · U oluk | aynı | iki vinç (duvar panelleri) · kamyonlar | yaz |
| S07 | 11:20→11:30 | uç parçaları → kapak çerçeveleri | aynı · kapaklar KAPALI | iki vinç (uç parçaları) · kamyonlar · conta paleti | yaz |
| S08 | 11:30→13:30 | ⭐ iç gri → açık mavi %0 → %100 (soldan) · KURU | oluk kuru, mat | sol vinç (varil paleti) · sağ vinç (bom dışarıda) · kamyon · hortumlar | yaz |
| S09 | 13:30→13:40 | bakım yolu + basamaklar %0 → %100 | aynı | iki vinç (bakım yolu parçaları) · kamyonlar | yaz |
| S10 | 13:40→13:50 | korkuluk %0 → %100 | aynı | iki vinç (korkuluk demetleri) · kamyonlar | yaz |
| S11 | 13:50→15:50 | dış astar → kömür grisi %0 → %100 (soldan) | aynı | sol vinç (varil paleti) · sağ vinç (bom dışarıda) · kamyonlar · ip hatları | yaz sonu · ilk sarı |
| S12 | 15:50→16:00 | (değişmez) · saha boşalır | aynı | iki vinç (boş paletler → kamyonlar) → bomlarını indirip çıkar · kamyonlar | ⭐ sonbahar |
| S13 | 16:00→16:10 | (değişmez) | ⭐ ilk su: borudan → sol ayağa (onda bir) | servis aracı · vanada iki kişi · bakım yolunda iki kişi | sonbahar |
| S14 | 16:10→16:20 | (değişmez) | su cephesi sol ayaktan → sağ kapağa (onda bir) | servis aracı · iki kişi | sonbahar |
| S15 | 16:20→16:30 | (değişmez) | onda bir → dörtte üç · kıyılarla eşit · vana kapanır | servis aracı · iki kişi | sonbahar |
| S16 | 16:30→16:40 | (değişmez) | kapaklar KALKAR · su sakin · teknede dümenci, halat çözülür | servis aracı (gider) · kapaklarda ekip | sonbahar · altın saat |
| S17 | 16:40→16:41 | (değişmez) | ⭐ tekne havuzdan → sol kapaktan → köprüye, burnu sol ayakta | servis aracı · iki kişi bakım yolunda | altın saat |
| S18 | 16:41→16:42 | (değişmez) | ⭐ tekne → merkez açıklığın ortası (DORUK) | servis aracı · iki kişi | altın saat |
| S19 | 16:42→16:43 | (değişmez) · TUTUŞ | tekne → sağ kapak, durur | servis aracı çıkar | altın saat |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   ÇAM — G0…G20 hepsinde x 1475–1547 · tepe 622 · dip 819 · 72 px en; zincirde her karede ELLE ✓/✗ (günlük §2) ·
                iğne yapraklı, mevsim taşımaz (çevresindeki yapraklı ağaçlar taşır)
İKİNCİ ÇAPA     iki ayak (x 844 · 1182 — G0'dan beri hazır) · üçüncü: ufuk 149 · dördüncü: nehir köprü altında x 1002
❸ İÇİN          dikiş = KARE (G1…G19): dikişin iki yakası aynı görsel; ❸ REBUILT hükmü zincir koşulmadı demektir
⚠️ NEHİR        her klipte akar (A'da yumuşak parıltı, B'de düz cam, Y'de hafif dalgacık) — YERİ ve GENİŞLİĞİ sabit; ❸ ve ❶ yüzey
                hareketini "arka plan değişti" saymamalı
⚠️ AĞAÇLAR      yamaçlardaki yapraklı ağaçlar mevsimle renk değiştirir (bilinçli taşıyıcı, PLAN §MEVSİM) — çam değiştirmez
```

---

## 5. ❹ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ajanı · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | ajan (taşıyan) | geçici destek | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|---|:-:|:-:|:-:|
| sol açıklık parçası | (önceden kaldırılmış) | sol vinç | dört sapan · kılavuz ip | G0 (asılı) | G1 | — |
| sağ açıklık parçası | sağ pedde kalaslar | sağ vinç | dört sapan · kalaslar | G1 (pedde) | G2 | kalaslar istife S1 |
| merkez açıklık parçası | vadi tabanında kalaslar (nehrin üstü) | sol vinç | dört uzun sapan · yayıcı kiriş · kalaslar | G2 (kalasta) | G3 | kalaslar S2 yığın → S3 küçük kamyon |
| enine kirişler | kamyonlar (iki ped) | iki vinç · ekip | sapan | G3 (açık) | G4 | — |
| taban panelleri | paletler, kamyonlar | iki vinç · ekip | sapan | G4 (ızgara) | G5 | — |
| uzak duvar | kamyonlar | iki vinç · ekip | sapan | G5 | G6 | — |
| yakın duvar | kamyonlar | iki vinç · ekip | sapan | G6 | G7 | — |
| uç bağlantıları | kamyonlar | iki vinç · ekip | sapan | G7 (açık derz) | G8 | — |
| mavi iç kaplama | sol pedde varil paletleri | sol vinç → oluğun içi · püskürtme ekibi | hortumlar | G8 (gri) | G9 | — |
| bakım yolu + basamaklar | kamyonlar | iki vinç · ekip | sapan · konsollar | G9 | G10 | — |
| korkuluk | kamyonlarda demetler | iki vinç · ekip | sapan | G10 | G11 | — |
| kömür grisi dış boya | varil paletleri | sol vinç → bakım yolu · ip hatlarında ekip | ip hatları · hortumlar | G11 (gri astar) | G12 | — |
| şantiye | pedler | iki vinç + kamyonlar | — | — | — | ⭐ S12: vinçler, paletler, kamyonlar çıkar |
| SU | sol havuz → dolum borusu (vana) | vanada ekip | — | G13 (kuru) | G16 (dörtte üç) | — |
| kapaklar | (gizli) vinç kabloları çerçevede | kapaklarda ekip | — | G16 (kapalı) | G17 (yukarıda) | — |
| tekne geçişi | sol havuz | dümenci | — | G17 (havuzda) | G20 (sağ kapakta) | — |

```
❹ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır):
   kanal köprüsü 1 · beton ayak 2 · mesnet 2 · çelik kapak 2 (çerçeveli) · dolum borusu 1 · sarı paletli vinç 2 (G0–G12) ·
   düz kasalı kamyonlar (değişen yükler) · vadi tabanında küçük kamyon (S3) · küçük servis aracı (G13–G19) · ekip (iz) ·
   dolum günü iki-dört kişi · teknede tek dümenci · kırmızı tekne 1 · çam 1 · nehir 1 · sol havuz + sağ kanal kolu ·
   kalaslar (G0–G3)
   ⛔ DAVETSİZ: ikinci köprü · taş kemer / Roma su kemeri · demiryolu viyadüğü · baraj · kilit odası · şelale (oluktan
      vadiye dökülen su) · ikinci tekne · nehirde tekne · gemi/feribot/yat · havuz merdiveni · kule vinç · yazı / işaret
      / tabela · drone gölgesi · parlayan su
❹ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: açıklıklar = S0–S2 vinçler · ızgara = S3 kiriş demetleri ·
                  taban = S4 paletler · duvarlar = S5–S6 paneller · bağlantı = S7 uç parçaları · mavi = S8 püskürtme ·
                  bakım yolu = S9 · korkuluk = S10 · kömür grisi = S11 · su = S13–S15 boru · açık kapaklar = (gizli) S16 ·
                  tekne yeri = S17–S19 dümenci
❹ ÇERÇEVE DEFTERİ köprü hattı 538 → 1398 sabit (G3 → G20) · ayaklar 844 · 1182 · çam 72 px sabit
❹ GİZLİ İŞ        cıvata ve conta → panel panel büyüyen yüzey · sızdırmazlık testi → S8–S12 kuru, mat kalan oluk · kapak
                  mekanizması → S16'da çerçevede kalkan kapaklar · seviye ölçümü → S15'te su çizgisine bakan iki kişi
❹ DECLARED WORLD  nehir vadisi · iki vinçli montaj (G0–G12) · tek dolum günü (G13–G20) · Y rejimi (S17–S19) · kış YOK · gece YOK
❸ PARKED GEREKÇESİ S19 (final tutuşu): yapı bitti; teknenin son metreleri dışında hareket yok — ödül ve sakin an, işsiz aralık
                  değil, beyanlı [P4-f · C1-d]
```

---

## 6. ❷ ZAMAN VE KESME — kesme listesi ve ses (❷ kör koşar; bu bölüm ❺ ve operatör içindir)

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_SKY_CANAL/THE_SKY_CANAL_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
REJİM KESMELERİ      24,0 (S2 A → S3 B) · 32,0 (S3 B → S4 A) · 64,0 (S7 A → S8 B) · 72,0 (S8 B → S9 A) · 88,0 (S10 A → S11 B)
                     · 96,0 (S11 B → S12 A) · 136,0 (S16 A → S17 Y) — rejim değişimi YALNIZ kesmede [P5-c]
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı, su seviyesi, tekne yeri ATLAMAZ ·
                     112,0 ve 120,0 (TEK DOLUM) · 144,0 ve 152,0 (TEK GEÇİŞ)
MÜZİK                ✅ VAR — altta, sözsüz, 120 BPM · 4 ölçü/sahne · diegetik yatak önde · THE_SKY_CANAL_MUZIK.md:
                     0–24 kanca (vinç motoru + çelik + nehir) · 24–104 montaj (metal, ritim) · 104–128 su (müzik sadeleşir) ·
                     128–152 kapaklar ve tekne (S18'de genişler) · 152–160 sönüm — ani kesilme yok
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G10 (S9 ↔ S10) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si (S9) G10 karesinde biter; G10 BOLUM_2'nin ilk görselidir.
ELLE KARE            ffmpeg -ss 80.0 -i teslim.mp4 -frames:v 1 sinir.jpg → oluk mavi kaplı, KURU · bakım yolu + uç basamakları
                     tamam · korkuluk YOK · dış gri astar · iki vinçte korkuluk demeti · kapaklar kapalı · tekne havuzda ·
                     gölge +9° · yaz
```

---

## 8. ❺ TESLİM — belgeli merceğin okuyacağı beyanlar

```
VAAT            Bir vadinin üstündeki hazır ayaklar, iki kıyıdaki kanalı birleştiren ve tekne taşıyan bir su köprüsüne dönüşür.
DİRENÇ          ① boşluk ve ağırlık — S0 (0,0–8,0) askıdaki sol parça · S1 (8,0–16,0) sağ parça · S2 (16,0–24,0) dimdik
                yükselen merkez parça · ② su — S13–S15 (104,0–128,0) borudan soldan dolum, seviye eşitlenmeden kapak açılmaz ·
                ③ tekne — S0–S16 (0,0–136,0) havuzda bekler
BEDEL           boşluk + şantiye: S2'de boşluk kapanır, S12'de vinçler ve istifler gider, S16'da kapaklar kalkar; G20'de aynı yerde
                dolu köprü ve üstünde tekne
AÇILIŞ          nesne: sol açıklığın üstünde askıdaki çelik parça · eylem: parça ilk karede iniyor · ipucu: solda havuzda
                bekleyen kırmızı tekne + kapalı kapak · MERAK SORUSU: "Bu tekne buradan nasıl geçecek?"
İŞLEV ANI       S13 (104,0–112,0) ilk su · S15 (120,0–128,0) seviye eşitlenir · S16 (128,0–136,0) kapaklar kalkar · S17
                (136,0–144,0) tekne köprüye girer · S18 (144,0–152,0) nehrin üstünden geçer · 156,0–160,0 tutuş
LOOP RHYME      aynı tekne kanal ekseninde, burnu sağa — G0'da solda havuzda, G20'de sağda köprünün ucunda · çam aynı x'te
OMURGA (20)     indirir · yerleştirir · birleştirir · bağlar · kapatır · yükseltir · tamamlar · bağlar · kaplar · kurar · çevirir ·
                boyar · toplar · akıtır · ilerletir · doldurur · açar · girer · geçer · varır
SES             MUSIC YES — low, wordless, 120 BPM, under the site sound (❷ C2 · ❺ C1)
TESLİM          END CARD NO · SPEED 1x · 160,0 sn · SECOND STATION NO · SLOW TIME (≈1 min/shot) S17–S19 declared
AI BEYANI       YAYIN_PAKETI §AÇIKLAMA sabit beyan bloğu + Studio "Altered content = EVET"
KAPAK           THE_SKY_CANAL_KAPAK.md — G20'den, bölünmüş yerleşim YOK · varsayılan YAZISIZ
PROMPT KAPISI   python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_SKY_CANAL → BLOCK 0 · FIX 9 (11.10.2026) —
                hepsi PLAN §ÜRETİM ÖNCESİ DURUM'da beyanlı (7 × rejim Y · araç kutu seti · düz ızgara)
```

---

## 9. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_SKY_CANAL_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  00_ANALIZ/02 §3 — kamera (h 85 · tilt 17°) · oluğun içi yakın duvarın üstünden bant olarak okunuyor mu ·
                  tekne havuzda ≈220 px mi · nehir merkez açıklığın altında mı · çam · iki ayak
⛔ PİLOT ÜÇLÜ     ① G20 + G19 + G18 + S18 + S19 · ② G2 + G3 + S2 · ③ G13 + G14 + S13 — PLAN §PİLOT ÜÇLÜ · sonra S0, S14, S15
⛔ USTA KARE      G20 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil); çam 72 ±2 px · ayaklar 844 / 1182 ±2 px
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a; 1920×1080 · 160,0 sn · kart YOK)
⛔ İHRAÇ          bash araclar/ihrac_kontrol.sh — süre 160,0 · kart YOK · müzik VAR · final tutuşu SSIM ≥ 0,90 [DERS 63]
⛔ KAPAK KANITI   ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
⛔ SÜRE / KLASÖR  160 sn yatay_2_dk bandının dışı — sahip kararı (hikâye SAPMA ②)
```
