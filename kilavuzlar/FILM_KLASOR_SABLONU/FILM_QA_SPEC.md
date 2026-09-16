# 🔍 <FILM_ADI> — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM · ⑥ GEÇİŞ · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER).
> ⛔ ① KARE · ③ ZAMAN · ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET · ⑫ KATILIK merceklerine **VERİLMEZ** — o altısı
> dokümansız koşar [AGENTS değişmez ⑦ · QA/00_README mod sistemi]. Yorum yok, yalnız ölçülebilir kilitler.
> Sayıya çevrilemeyen kilit, kilit değildir; tariftir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh <FMT>/<FILM_ADI> <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].

---

## 0. KÜNYE

```
FİLM          <FILM_ADI> — ⬜ [yapı · saha · istasyon tek cümle]
FORMAT        16:9 yatay · 1920×1080 · 30 fps · <FMT>

TESLİM YAPISI ⭐ SAHNE BLOĞU  <N> sahne × <KLIP>,0 sn = <SURE>,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  1 × 5,0 sn          =   5,0 sn              ← SAHNE DEĞİL
                 TOPLAM                          <TOPLAM>,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR ve devamlılık karşılaştırmalarına GİRMEZ.
                 Ayrı denetlenir: "kart, son sahnenin (S<N_SON>) sonundaki yapının AYNISINI mı gösteriyor?"

SAHNE SAATLERİ  sahne n = n × <KLIP>,0 → (n+1) × <KLIP>,0   ·   S0 0,0–<KLIP>,0 · … · S<N_SON> ⬜–<SURE>,0 · KART <SURE>,0–<TOPLAM>,0
                (120 BPM · ölçü 2,0 sn · 5 ölçü/sahne · her kesme ölçü başında)
PART GRID       <PART_GRID>
⛔ DÜZ IZGARA   sahip beyanı (14.09.2026). ⑥ METRONOM hükmü BEKLENEN ve KABUL EDİLMİŞ risktir (PLAN §AŞAMA
                MERDİVENİ · DERS 13 · 24); gelirse "beklenen" diye kaydedilir, yeniden üretim sebebi sayılmaz.
                Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]: ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — ölçülünce
   buraya ve PLAN'a yazılır; {5,10} gerekir, {4,6,8} çıkarsa iki-klip hükmü (PLAN §DEĞİŞMEZLER).

YAPI          ⬜ [tip · H · eleman sayısı × boy · malzeme]
SAHA          ⬜ [saha kartı · çapalar]
ZAMAN YAYI    ⬜ [takvim] · film mertebe anlatır: "⬜" [P1-c]
IŞIK          TEK GÜN ⬜ → ⬜ · Σ rejim ⬜ saat · takvim SAHADAN · bilinçli sıkıştırma
KAMERA        MAIN STATION — tek istasyon · h ⬜ m · D ⬜ m · bakış ⬜° · tilt 0°   (detay istasyonu: yok / S⬜ S⬜)
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G<N> usta kare → G<N_SON> → … → G0 · her kare zincir_kontrol.sh + kanıt nesnesi ELLE
GÜNLÜK        <FILM_ADI>_URETIM_GUNLUGU.md — ⬜ dolu / ⛔ boş (boşsa bu SPEC'in hükmü yoktur)
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S<N_SON>
SANİYE      ⬜ (son sahne S<N_SON>, ⬜. saniye — son ≥2,0 sn'lik TUTUŞUN içi [P2-i]; aydınlık [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① ⬜ (yapı tamam: taç %⬜ · ⬜ eleman sayılabilir)
   ② ⬜ (geçici ekipman GİTMİŞ: vinç YOK · iskele YOK · ⬜ YOK — SÖKÜM satırı)
   ③ AYNI ⬜ (kanıt nesnesi: x ≈ ⬜ px · %⬜ · ≈⬜ px — G0 ile aynı konum ve boy)
   + BEDEL görünür: ⬜

KOMUT
   ffmpeg -ss ⬜ -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①②③'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP
   ffmpeg -ss 0.3  -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss ⬜   -i teslim.mp4 -frames:v 1 kanit_g<N>.jpg
   İki karede çapalar ① ② ③ ve kanıt nesnesi tam aynı yerde. Işık: ⬜ [aynı / bilinçli farklı — PLAN LOOP satırı].
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=⬜ · D=⬜ · tilt 0 · yatay: yüzde = 50 + 118,5·(y−h)/D, ALT kenardan)

| nesne | y (m) | yüzde (alt kenardan) | x (soldan) | px boy | her karede |
|---|:-:|:-:|:-:|:-:|---|
| ufuk (tilt 0) | — | 50,0 | — | — | ✓ |
| yapı tabanı | 0 | ⬜ | ⬜ | — | ✓ |
| taç (bitmiş) | ⬜ | ⬜ | ⬜ | — | yalnız G<N> (ara karelerde AT THIS STAGE yüzdesi — aşağıdaki tablo) |
| kanıt nesnesi ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ✓ BİREBİR (boy dâhil) |
| çapa ① ⬜ (SOL) | ⬜ | ⬜ | ⬜ | ⬜ | ✓ |
| çapa ② ⬜ (SAĞ) | ⬜ | ⬜ | ⬜ | ⬜ | ✓ |
| çapa ③ ⬜ (uzak) | — | ⬜ | — | — | ✓ |
| vinç bom başı / en yüksek kaldırma | ⬜ | ⬜ | ⬜ | — | gök mü kara mı: ⬜ [DERS 22] |

```
KAMERA SABİTLİK  ① için: ilk/son kare kayması ≤ 2 px (araç kapısı ②) · film boyunca çapa ① ② konumu ±2 px
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
⬜ tip · H ⬜ m · taban ⬜ m · eleman ⬜ × ⬜ m · malzeme ⬜ · geçici ekipman ⬜ (bom ⬜ m · kapasite ⬜ t)
```

### Yapı yüzdesi ve saha durumu — sahne sahne (② İNŞA · ④ TESLİM · ⑩ SEBEP için)

| S | saat | yapı: eleman + ara hâl (%) | taç yüzdesi (kadraj) | geçici ekipman kadrajda | saha / mevsim taşıyıcısı |
|:-:|:-:|---|:-:|---|---|
<SPEC_SATIRLARI>

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   ⬜ — G0…G<N> hepsinde x ≈ ⬜ px · %⬜ · ≈⬜ px boy; zincirde her karede ELLE ✓/✗ (günlük §2)
İKİNCİ ÇAPA     ⬜
⑤ İÇİN          dikiş = KARE (G1…G<N_SON>): dikişin iki yakası aynı görsel; ⑤ REBUILT hükmü zincir koşulmadı demektir
```

---

## 5. ⑧ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | geçici destek (sling / formwork / scaffold …) | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|:-:|:-:|:-:|
| ⬜ | | | G⬜ | G⬜ | G⬜ |

```
⑪ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır): ⬜ · ⬜ · ⬜
⑩ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: ⬜ (kaldırma karede biter — DERS 57)
```

---

## 6. ⑥ GEÇİŞ — kesme listesi ve ses

```
PLAN KESMELERİ (sn)  <KESMELER>   (<N_SON> kesme, hepsi ölçü başı — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 <FMT>/<FILM_ADI>/<FILM_ADI>_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                120 BPM · müziksiz pencere 0,0–⬜ · katman girişleri: ⬜ · final tutulan akor ⬜–<SURE>,0
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G<K> (S<K_SON> ↔ S<K>) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si G<K> karesinde biter; G<K> BOLUM_2'nin ilk görselidir.
ELLE KARE            ffmpeg -ss <B1_SURE>.0 -i teslim.mp4 -frames:v 1 sinir.jpg → yapı yüzdesi %⬜ · gölge ⬜° · gök ⬜
                     (6/8 dk: b1_son.jpg ↔ b2_ilk.jpg zincir_kontrol.sh — çıkış 2 = dikiş kırık)
⑤ İÇİN               6/8 dk'da bu dikişi hiçbir yarım master GÖREMEZ — bu satır onun yerine geçer.
```

---

## 8. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç <FILM_ADI>_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne <KLIP>,0 sn → en büyük kutu ≥ <KLIP1>,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  kamera · yapı · çapalar · ufuk yan kesiti; kaldırmalar gök/kara burada doğrulanır
⛔ USTA KARE      G<N> önce; kapı: final hiyerarşisi bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil)
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28 — dört kez ölçüldü]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a)
⛔ KAPAK KANITI   ffmpeg -ss ⬜ -i teslim.mp4 -frames:v 1 g<N>_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g<N>_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
```
