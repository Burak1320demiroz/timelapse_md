# 🔍 THE_GLASS_WALL — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM · ⑥ GEÇİŞ · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER).
> ⛔ ① KARE · ③ ZAMAN · ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET · ⑫ KATILIK merceklerine **VERİLMEZ** — o altısı
> dokümansız koşar [AGENTS değişmez ⑦ · QA/00_README mod sistemi]. Yorum yok, yalnız ölçülebilir kilitler.
> Sayıya çevrilemeyen kilit, kilit değildir; tariftir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_GLASS_WALL <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].

---

## 0. KÜNYE

```
FİLM          THE_GLASS_WALL — çelik çerçeve cam sera 24×10×5,5 m + taş ev + kuru taş teras · kıyı tepe · tek istasyon bakış 190°
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_2_dk_filmler

TESLİM YAPISI ⭐ SAHNE BLOĞU  12 sahne × 10,0 sn = 120,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  1 × 5,0 sn          =   5,0 sn              ← SAHNE DEĞİL
                 TOPLAM                          125,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR ve devamlılık karşılaştırmalarına GİRMEZ.
                 Ayrı denetlenir: "kart, son sahnenin (S11) sonundaki yapının AYNISINI mı gösteriyor?"

SAHNE SAATLERİ  sahne n = n × 10,0 → (n+1) × 10,0   ·   S0 0,0–10,0 · … · S11 110,0–120,0 · KART 120,0–125,0
                (120 BPM · ölçü 2,0 sn · 5 ölçü/sahne · her kesme ölçü başında)
PART GRID       — (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)
⛔ DÜZ IZGARA   sahip beyanı (14.09.2026). ⑥ METRONOM hükmü BEKLENEN ve KABUL EDİLMİŞ risktir (PLAN §AŞAMA
                MERDİVENİ · DERS 13 · 24); gelirse "beklenen" diye kaydedilir, yeniden üretim sebebi sayılmaz.
                Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]: ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — ölçülünce
   buraya ve PLAN'a yazılır; {5,10} gerekir, {4,6,8} çıkarsa iki-klip hükmü (PLAN §DEĞİŞMEZLER).

YAPI          çelik çerçeve cam sera H 5,50 m · 24×10 m · 12 kemer + 64 cam panel + taş ev H 4,50 m · 2 teras
SAHA          kıyı tepe +85 m · zeytin SOL %8-15 · kayalık SAĞ %82-90 · deniz ufuku %50,00
ZAMAN YAYI    Mart → Ekim (8 ay) · film mertebe anlatır: "approximately eight months" [P1-c]
IŞIK          TEK GÜN 09:00 → 17:00 · Σ rejim ~20 dk/sahne (bile · takvim SAHADAN · bilinçli sıkıştırma
KAMERA        MAIN STATION — tek istasyon · h 2,00 m · D 45,00 m · bakış 190° · tilt 0°   (detay istasyonu: yok)
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G12 usta kare → G11 → … → G0 · her kare zincir_kontrol.sh + kanıt nesnesi ELLE
GÜNLÜK        THE_GLASS_WALL_URETIM_GUNLUGU.md — ⬜ dolu / ⛔ boş (boşsa bu SPEC'in hükmü yoktur)
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S11
SANİYE      118,5 (son sahne S11, 118,5. saniye — son ≥2,0 sn'lik TUTUŞUN içi [P2-i]; aydınlık [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① Sera içi yeşil bitkiler + hasat kasası (taç %59,2 · 76 eleman sayılabilir)
   ② Geçici ekipman GİTMİŞ: vinç YOK · iskele YOK · palet YOK — SÖKÜM satırı)
   ③ AYNI zeytin ağacı (kanıt nesnesi: %x 8-15 sol · ≈80 px gövde · ≈180 px boy — G0 ile aynı konum ve boy)
   + BEDEL görünür: maki yaban doğası gitti — düzenli çiftlik

KOMUT
   ffmpeg -ss 118.5 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①②③'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP
   ffmpeg -ss 0.3  -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 118.5 -i teslim.mp4 -frames:v 1 kanit_g12.jpg
   İki karede çapalar ① ② ③ ve kanıt nesnesi tam aynı yerde. Işık: BİLİNÇLİ FARKLI — G0 Mart sabahı / G12 Ekim akşamı.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=2,00 · D=45,00 · tilt 0 · yatay: yüzde = 50 + 118,5·(y−h)/D, ALT kenardan)

| nesne | y (m) | yüzde (alt kenardan) | x (soldan) | px boy | her karede |
|---|:-:|:-:|:-:|:-:|---|
| ufuk (tilt 0) | — | 50,0 | — | — | ✓ |
| yapı tabanı (sera slab) | 0 | 44,7 | %32–68 | 808 px geniş | ✓ |
| taç (sera 5,50 m) | 5,50 | 59,2 | — | — | yalnız G12 (ara karelerde AT THIS STAGE yüzdesi — aşağıdaki tablo) |
| kanıt nesnesi zeytin ağacı | ≈2,8 | ≈56,2 | %x 8–15 | ≈80 px gövde / ≈180 px boy | ✓ BİREBİR (boy dâhil) |
| çapa ① zeytin ağacı (SOL) | ≈2,8 | ≈56,2 | %x 8–15 | ≈80 px gövde | ✓ |
| çapa ② kayalık (SAĞ) | ≈1,5 | ≈52,0 | %x 82–90 | ≈200 px geniş | ✓ |
| çapa ③ deniz ufuku (uzak) | — | 50,0 | — | — | ✓ |
| vinç bom başı / en yüksek kaldırma | — | N/A (vinç yok — elin lifter) | — | — | N/A |

```
KAMERA SABİTLİK  ① için: ilk/son kare kayması ≤ KAMERA_ISTASYONU §7 eşiği (araç kapısı ②) · film boyunca 3 nirengi konumu aynı eşik içinde
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
çelik çerçeve cam sera · H 5,50 m · taban 24×10 m · eleman 12 kemer + 64 cam panel + 2 kuru taş teras + 1 taş ev · malzeme koyu yeşil boyalı çelik / kireçtaşı kuru duvar / kiremit çatı · geçici ekipman: iskele G5–G8 · el vakum lifter G6–G8 · beton mikser G3–G4 (vinç yok)
```

### Yapı yüzdesi ve saha durumu — sahne sahne (② İNŞA · ④ TESLİM · ⑩ SEBEP için)

| S | saat | yapı: eleman + ara hâl (%) | taç yüzdesi (kadraj) | geçici ekipman kadrajda | saha / mevsim taşıyıcısı |
|:-:|:-:|---|:-:|---|---|
| S00 | 09:00 | zemin temizlendi · sarnıç açık | yapı yok | kazıcı + el arabası | Mart · maki yeşil + sarı çiçek |
| S01 | 10:00 | alt teras %25 (3 sıra 12 m) | yapı yok | taş yığını + el arabası | Mart sonu · yeşil |
| S02 | 11:00 | alt teras %100 · üst teras %75 | yapı yok | taş yığını son |
| S03 | 10:30 | ev temeli %100 · duvar %50 | ev taç %51 | beton mikser | Nisan · maki çiçek |
| S04 | 09:30 | ev çatı %100 · sera zemin %100 | ev taç %56,6 | mikser sol + beton zemin yaş | Mayıs · ot kurumaya baş. |
| S05 | 10:00 | sera çerçeve %50 (6/12 kemer) | sera taç %59,2 | iskele sağdan · cam paleti sağ kenar | Haziran · ot altın |
| S06 | 11:00 | çerçeve %100 · cam %12 (8/64) | sera taç %59,2 | iskele · cam paleti dolu | Temmuz · kobalt deniz |
| S07 | 10:30 | cam panel %62 (40/64) | sera taç %59,2 | iskele · palet yarı boş | Ağustos · kuru altın |
| S08 | 09:00 | cam %100 (64/64) · iskele kalktı | sera taç %59,2 | iskele boru yığını alt terasta (geçici) | Eylül · ilk yağmur |
| S09 | 10:00 | iç raf %100 · dış tarhlar %100 | sera taç %59,2 | — | Eylül sonu · yeşil |
| S10 | 16:00 | fidanlar ekili · oluk · sarnıç bağlı | sera taç %59,2 | damlama hortum rulosu | Ekim · altın saat |
| S11 | 17:00 | TES LİM — hasat kasası · duman · taş patika | sera taç %59,2 | — | Ekim sonu · sonbahar |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   zeytin ağacı — G0…G12 hepsinde x ≈ %8–15 sol · ≈80 px gövde genişliği · ≈180 px boy; zincirde her karede ELLE ✓/✗ (günlük §2)
İKİNCİ ÇAPA     kayalık sağ %82–90 · ≈200 px · deniz ufuku %50,00 her karede
⑤ İÇİN          dikiş = KARE (G1…G11): dikişin iki yakası aynı görsel; ⑤ REBUILT hükmü zincir koşulmadı demektir
```

---

## 5. ⑧ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | geçici destek (sling / formwork / scaffold …) | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|:-:|:-:|:-:|
| kuru taş teras duvarı (×2) | sol kenar taş yığını (G0 moloz) | — (kuru taş, destek yok) | G0 | G2 | N/A (kalıcı) |
| çiftlik evi taş duvar + çatı | beton mikser + taş yığını | beton mikser G3'te satın alındı, G4'te çıktı | G3 | G4 | mikser G4'te söküldü |
| sera beton zemini | beton mikser (G4) | süpaj/gönleme tablası (geçici) | G4 | G4 | — |
| sera çelik çerçeve (12 kemer) | demet paket sağ slab (G4'te teslim) | geçici çelik prop (G5) | G5 | G6 | prop G6'da kalktı |
| cam paneller (64 adet) | sağ kenar palet (G5) | iskele (G5–G8) | G6 | G8 | iskele S8'de söküldü |
| iç raf + damlama | sol arka terasta istif (G8'den sonra) | — | G9 | G9 | N/A |
| çatı oluğu + sarnıç bağlantısı | downpipe G10'da görünür | — | G10 | G10 | N/A |

```
⑪ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır): kuru taş teras duvarı · taş ev · sera çelik çerçevesi · cam palet · iskele (geçici G5–G8) · beton mikser (geçici G3–G4) · vakum lifter (geçici G6–G8) · iç raf + damlama (G9) · downpipe (G10) · hasat kasası (G12)
⑩ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: kemer paketi G4'te teslim · cam paleti G5'te görünür · vakum lifter G6'dan itibaren · iskele G8'de söküldü (kaldırma olmadığından DERS 57 N/A)
```

---

## 6. ⑥ GEÇİŞ — kesme listesi ve ses

```
PLAN KESMELERİ (sn)  10,0 · 20,0 · 30,0 · 40,0 · 50,0 · 60,0 · 70,0 · 80,0 · 90,0 · 100,0 · 110,0   (11 kesme, hepsi ölçü başı — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_GLASS_WALL/THE_GLASS_WALL_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                120 BPM · müziksiz pencere 0,0–8,0 s · katman girişleri: 8 s (sub) · 20 s (gitar) · 50 s (strings) · 110 s (piyano) · final tutulan akor 110,0–120,0
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G6 (S5 ↔ S6) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si G6 karesinde biter; G6 BOLUM_2'nin ilk görselidir.
ELLE KARE            ffmpeg -ss 60.0 -i teslim.mp4 -frames:v 1 sinir.jpg → yapı yüzdesi %50 (sera çerçeve %100, cam başlıyor) · gölge 134° · gök açık Temmuz mavi
                     (6/8 dk: b1_son.jpg ↔ b2_ilk.jpg zincir_kontrol.sh — çıkış 2 = dikiş kırık)
⑤ İÇİN               6/8 dk'da bu dikişi hiçbir yarım master GÖREMEZ — bu satır onun yerine geçer.
```

---

## 8. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_GLASS_WALL_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 10,0 sn → en büyük kutu ≥ 11,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  kamera · yapı · çapalar · ufuk yan kesiti; kaldırmalar gök/kara burada doğrulanır
⛔ USTA KARE      G12 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil)
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28 — dört kez ölçüldü]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a)
⛔ KAPAK KANITI   ffmpeg -ss 118.0 -i teslim.mp4 -frames:v 1 g12_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g12_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
```
