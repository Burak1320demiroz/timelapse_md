# 🧠 THE_EDEN_ARK — KONSEPT VE RİSK

> Girdi: `00_HIKAYE_ONAYI.md` (onaylı 05.10.2026) + `01_QA_DERS_HASADI.md`.
> Bu dosya onaylı hikâyeyi İYİLEŞTİRİR, değiştirmez; üç netleştirme 00_HIKAYE_ONAYI SAPMA'da.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI

```
① KONU:       sahip verdi (05.10.2026 · "terk edilmiş yük gemisinden yüzen yağmur ormanına" · THE EDEN ARK)
② FORMAT:     yatay_2_dk_filmler → KILAVUZ_REHBERI §2.8 · 18 sahne · 2 bölüm (S0–S8 · S9–S17) · QA birimi FİLM
③ SAHNE:      ⚠️ BANDIN DIŞI — 18 × 8,0 = 144,0 sn (format 12 × 10,0). Sahip izni: sohbette "onaylıyorum"
              (05.10.2026), sahibin kendi önerisi. Gerekçe: sahibin 8,0 sn üretim düzeni + THE OLD ROAD emsali
              (yatay_2'de 15 × 8,0). Toplam 144,0 + 5,0 kart = 149,0 sn.
④ YAPI KARTI: ⛔ KART YOK — YAPI_TIPI_KARTLARI'nda gemi DÖNÜŞÜMÜ yok; en yakın: liman (saha) + kule/kabuk
              yenileme (BLUE DOOR · BLUE SILO emsali: eski gövde soyulur, yeniden giydirilir). Kart adayı [AGENTS H].
⑤ SAHA KARTI: SAHA_VE_IKLIM_KARTLARI kıyı — mevsim taşıyıcısı: tek haziran günü (mevsim yok, ışık günü var) ·
              negatif eki: tersanede tek gemi · korpus cümlesi: "documentary shipyard progress photograph"
⑥ ARAÇ:       ⛔ kutu seti ÖLÇÜLMEDİ — tavan ≥ 8,0 gerekir (en büyük kutu ≥ 9,0; üret 9,0 → baştan 1,0 kırp)
⑦ HİKÂYE ONAYI: ONAY ✅ 05.10.2026 · TUR 1/3
```

## 1. 🎯 SAHİBİN TALEBİ — birebir (özet; tam metin sohbette)

```
TALEP: "Kuru havuzda paslanmış dev bir yük gemisi… İşçiler gövdeyi onarıyor, boş ambarlara bahçeler
        yerleştiriliyor, güvertenin üzerinde uzun bir cam sera yükseliyor. Finalde kuru havuz suyla doluyor
        ve içi yemyeşil olan gemi yeniden yüzmeye başlıyor." · 16:9 · 2:24 · 18 klip · üç kamera açısı ·
        "Vinçler yetişkin ağaçları indiriyor" · "çelik kemerler takılıyor" · final mavi saat, römorkör ·
        kapak: bitmiş geminin çapraz açıdan tamamı + römorkör
```

| sahibin isteği | fiziksel / inşa sorunu | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| 18 × 8 sn = 2:24 | format 12 × 10,0 | bant dışı, sahip onayıyla | §0 ③ |
| üç kamera açısı | tek istasyon kuralı; değişen kesmede yapı yüzdesi sabit olmalı | TEK ana istasyon, çapraz yüksek bakış | DERS 52 · KAMERA_ISTASYONU §1 |
| ilk karede vinç ambar kapağı kaldırır | kancalı yük yalnız TEK sahnede; kapak uzun rijit yük | kapaklar zincirle YANA YUVARLANIR — vinçsiz ilk saniye hareketi | DERS 22 · 57 |
| vinçler ağaçları indirir (çoğul) | aynı | TEK kaldırma: 13 m'lik incir (S5 sonu–S6); diğer ağaçlar teleskopik yükleyiciyle rampadan | DERS 22 · 57 |
| çelik kemerler vinçle | uzun rijit yük havada kopyalanır | kıçtan başa yürüyen montaj portalı, kemerleri YERİNDE diker | DERS 57 · P23-a |
| ambarlara toprak, ağaçlar | gemi yüzmez (≈ 10 000 t) | basamaklı çelik bahçe çerçeveleri + ince toprak (≤ 1,5 m); ağırlık aşağıda | fizik |
| final: römorkör gemiyi dışarı çeker | gemi kadrajdan çıkarsa kapak gemisiz kalır | kamera çapraz; gemi kameradan UZAKLAŞIR ve kapıdan geçtiği anda (+150 m) hâlâ kadrajda (x 1328 → 1657) | kapak = GN |

## 2. 🚪 KONSEPT KAPISI — VAAT / DİRENÇ / BEDEL [KILAVUZ_REHBERI §6]

```
VAAT      Terk edilmiş paslı bir yük gemisini kuru havuzda yüzen bir bahçeye dönüştürüp denize indirmek.  ✅
DİRENÇ    ① pas ve çürüme (delik borda, paslı kapaklar ve direkler) ② ağırlık (toprak + ağaç; yüzme payı)
          ③ su (ancak havuz dolunca yüzer, ancak seviye eşitlenince kapı açılır)
          ekranda: S1 kıvılcım + hurda konteyneri · S2 kesilen ve kaynaklanan levha · S6 tek, yavaş kaldırma ·
                   S14 yükselen su + kalkan gemi · S15 açılan kapılar                                          ✅
BEDEL     Paslı, karanlık, boş üç ambar — G1'de üç kara açıklık (x 570 · 806 · 988, üstten 690–735); G8'de üçü de
          yeşil taç; G18'de üç ambar cam altında orman. + paslı gövde (S3'te lacivertin altında kaybolur).        ✅
KANAL TEZİ  ne kayboluyor: pas ve boşluk · kadrajda: üç ambar açıklığı, 150 px'lik üç dikdörtgen · cevap "zaman
            geçiyor" değil, "boşluk doluyor ve gemi denize geri dönüyor"                                    ✅
DÖRT TEST   ① tek kare ✅ (ambar kaç yeşil · sera ne kadar ilerledi · su nerede · gemi nerede)
            ② kinetik ✅ (her klipte makine ya da su ya da gemi hareket eder) ③ "THE EDEN ARK" 3 kelime ✅
            ④ omurga 18 vuruş ✅ (03 §1)
```

## 3. 🎥 KAMERA HESABI — 16:9 [KILAVUZ_REHBERI §2.8 · KAMERA_ISTASYONU §3 · DERS 38]

```
GİRDİ      gemi en yüksek nokta baca +21,5 · sera tepesi +18,5 · güverte +5,5 · havuz kenarı +1,5 · havuz suyu 0
           h = +24,00 m (havuzun yanındaki eski tersane ofisinin düz çatısı) · tilt 0 · bearing 10°
⭐ D FORMÜLDEN DEĞİL, İKİ EŞİTSİZLİKTEN ÇIKTI: tilt 0 ve h güverte üstünde → bütün gemi ufkun ALTINDADIR (taç
           kuralı %82 burada bağlayıcı değil). Bağlayıcı olan "çalışma seviyesi ≥ %25": (h − güverte)/d ≤ 0,211 →
           baş bodoslamada d ≥ 87 m. Kapak şartı: +150 m çekilmiş gemi kadrajda. Betikle tarandı (P23-e):
           havuz ekseni bakışa 48° · gemi ortası optik eksende d 135,0 m, eksenin 8,0 m solunda.
YÜZDE(y)   = 50 + 118,5·(y − h)/d
           baş kasara +8,0 (d 91,5) %29,3 · güverte orta (d 127,6) %32,8 · baca +21,5 (d 168,5) %48,2
           sera tepe +18,5: baş ucu (d 102,9) %43,7 · kıç ucu (d 153,7) %45,8
YANLAR     x = %50 + 66,7·l/d → baş x 172 px · kıç x 1249 px (gemi G0'da kadraj eninin %56'sı) ·
           final (+150 m) baş x 1328 · kıç x 1657 · römorkör x 1685–1728
ÇAPALAR    ① tuğla baca (uzak rıhtım) x 100 · üstten 418 → 671 · ② yakın havuz kenarı (babalar) üstten 892 → 711
           ③ mendirek feneri x 1850 · üstten 577 → 620 + ufuk %50 (540)
GÖLGE      bakış 10° · güneş 73° (06:00) → 307° (20:00) · sabah sağ-önden, akşam sol-önden; kadraj −27° … +47°
           → güneş hiçbir karede kadrajda değil (en yakın: G0 +63°, G18 −63°)
KALDIRMA   tek kaldırma: kanca +22,5 → üstten 555 (ufkun 15 px ALTI) ✅ alt yarı · bom başı +32 → üstten 455 (göğe
           karşı) ⚠️ · halat 100 px göğe karşı — beyanlı [DERS 22]
GÖRÜNÜRLÜK ⚠️ yakın havuz duvarı, gövdenin kenar seviyesinin (+1,5) altını örter: borda yalnız +1,5 → +5,5 arası
           (4 m · ≈ 38 px) görünür. Havuz suyu yalnız UZAK duvarın iç yüzünde ve kıç–kapı arasındaki 20 m'lik
           boşlukta okunur. Ambarların İÇİ 10–12°'lik bakışta görünmez — bahçe mezarnanın ÜSTÜNE çıkan
           taçlarla okunur (basamaklı çerçeve bu yüzden var).
⛔ ÖN GÖRSELLEŞTİRME: yan kesit ve plan betikle hesaplandı (ajan scratchpad · edenark/final.py); çizim yok.
```

## 4. 🏗️ VİNÇ / GEÇİCİ EKİPMAN KARARI [DERS 1 · 8 · 22 · 46 · 48 · 57]

```
GEÇİCİ EKİPMAN  ① kamyonlu mobil vinç (S4'te gelir · G5–G7 · S7'de gider) — bom ≈ 35 m
                ② tekerlekli iskele kuleleri borda boyunca (S1 → S13) ③ rampa köprüsü rıhtım → güverte (S1 → S13)
                ④ hurda konteynerleri (S1) ⑤ toprak konveyörü (S5 · S7'de gider)
                ⑥ teleskopik yükleyici (S4 · S7) ⑦ montaj portalı (S9 → kalıcı: cam temizleme portalı olur)
KANCA           kancalı yük TEK: S5'in son 1,5 sn'si → S6. G5: "with a strapped root ball on the hook" (ağaç treylerde);
                G6: ağaç ambar 2'nin 0,5 m üstünde ASILI; G7: "with a slack guiding sling on the hook" (gövde hâlâ
                bağlı). G0–G4 ve G8–G18'de kadrajda vinç YOK.
KAYNAK          hurda → yakın rıhtımdaki konteynerler · toprak → yakın rıhtım yığını (x 461) · ağaçlar → fidanlık (x 972,
                beş sıra) · incir → yassı treyler · kemer ve cam → kıç tarafta rıhtım istifi (S9) · boya → iskele kuleleri
SÖKÜM           vinç S7 · konveyör S7 · iskele kuleleri ve rampa S13 · portal KALIR (kalıcı) · mooring halatları S16
```

## 5. ☀️ IŞIK GÜNÜ VE TAKVİM [ZAMAN_VE_ISIK §2 · §6 · §7 · SANTIYE_HAREKETI §1]

```
IŞIK GÜNÜ   06:00 → 20:00 · Σ = 12 × A (10 dk = 2 h) + 6 × B (2 h = 12 h) = 14,0 saat ≤ 14 ✓ (sınırda, tam)
TAKVİM      45,3° K · 21 haziran (δ +23,4°) · doğuş 04:10 · batış 19:50 (güneş saati) · mertebe: "tek bir uzun
            haziran günü, sabahtan mavi saate" [P1-c] — gerçekte aylar; beyanlı hız kabulü
GECE        yok · final mavi saat, güneş −2,3° [DERS 45]
GÜNEŞ DİSKİ hiçbir LIGHTING bloğunda anılmaz [DERS 39] · gölge G(n)↔G(n+1) farklı [DERS 32 · 47]
```

## 6. ⚠️ RİSK

| risk | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| DERS 57 ağaç kopyası | ✅ | 13 m'lik ağaç havada | kaldırma G6'da biter; S6 yalnız 0,5 m indirir | ⚠️ orta |
| DERS 22 halat | ✅ | bom başı göğe karşı | kanca alt yarıda, tek sahne | ⚠️ orta |
| DERS 55 tersane çoğul gemi | ✅ | tersane korpusu | sayım cümlesi 19 kez | ⚠️ |
| DERS 49 cam/bitki belirmesi | ✅ | şeffaf panel, yeşillik | portal yürür, cam beyaz kemerle gelir; ağaçlar yükleyiciyle | ⚠️ |
| DERS 56 erken yüzme | ✅ | "floating" fiili | "rests on its keel blocks" G0–G14; "floats" yalnız S14 I2V sonrası | ⚠️ düşük |
| korpus: "ark / cruise / greenhouse ship" | ✅ | kavram sanatı | kelimeler promptta yok; belgesel tersane fotoğrafı | ⚠️ |
| görünmeyen su (havuz duvarı) | ✅ | 10–12°'lik bakış | uzak duvar + kıç–kapı boşluğu + geminin kalkışı | ⚠️ yüksek — QA_SPEC §4 |
| final gemi küçük (329 px) | ✅ | gemi uzaklaşır | kabul; kapak 120 px testinde ölçülür | ⚠️ |

### ⭐ 1 NUMARALI RİSK SAYIYLA YAZILIR

```
RİSK       S5 sonu–S6: model 13 m'lik inciri hedefte kopyalar (treylerde bir ağaç kalır, ambarda bir ağaç belirir)
           ya da kancayı boş bırakıp ağacı "pop" ettirir.
SAYI       G6'da ağacın kök topu ambar 2 mezarnasının 0,5 m üstünde (üstten 705), tepesi üstten 620, kanca 555;
           treyler G6'da BOŞ (x ≈ 890, üstten ≈ 815).
ÖLÇÜM      ② İNŞA ve ⑩ (MAGIC) — S6'nın 0,0 · 4,0 · 8,0 sn kareleri; G5 → G6 dikişinde treylerin boşalması.
```
