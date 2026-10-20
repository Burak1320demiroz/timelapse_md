# THE_HIDDEN_LOFT — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 8 × 8,0 sn = 64,0 sn (⚠️ sahip istisnası 18.10.2026) · paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn = 37,0 sn
plan: dikey_shorts/THE_HIDDEN_LOFT/THE_HIDDEN_LOFT_DIKEY_TIMELAPSE.md (18.10.2026 · 8 sahne · kart beyanlı · kapı BLOCK 0 · FIX 1)
üretim günlüğü: dikey_shorts/THE_HIDDEN_LOFT/THE_HIDDEN_LOFT_URETIM_GUNLUGU.md — ⛔ BOŞ → durum "ÜRETİLDİ · GÜNLÜKSÜZ" [DERS 28]
yayın dosyası: ~/Downloads/"the hıdden loft.mp4" (19.10.2026 00:32) · sha256 6cee1916ecb4 · 37,01 sn · 2160×3840 · 30 fps · ses var · 2x
kaynak klipler: ~/Downloads (18.10.2026 23:12–23:14) — S0 Workers_cleaning_and_renovating_… · S1 Workers_renovating_attic_room_1080p ·
              S2 Workers_laying_wooden_floor_planks (üçü 1080×1920) · S3 Workers_furnishing_attic_room · S4 Workers_furnishing_attic_room_ti… ·
              S5 Workers_arranging_furniture_in_room · S6 Workers_organizing_room_time_lapse · S7 Workers_uncovering_triangular_wi… (beşi 720×1280)
              · hepsi 8,0 sn, sesli
master: YOK (1x master dışa aktarılmadı; ❸ ❹ da 2x dosyayla koşuldu)
kapak: ~/Downloads/"Gizli çatı katı.png" (941×1672, 18.10.2026 23:11) — G8 + "THE HIDDEN / LOFT"; yayındaki kartla aynı görsel
koşu tarihleri: beş mercek sahip koşusu, çıktılar 19.10.2026'da yapıştırıldı · ajan ölçümü 19.10.2026

## ⭐ AJAN ÖLÇÜMÜ — merceklerden önce okunur
ffprobe · `klip_eslestir.py` (8 kaynak klip) · kare farkı (54×96 gri) · 1 sn ve klip başına 4 fps kare panosu · ses (1 sn RMS + tonallık,
kaynak klip sesiyle zarf korelasyonu) · kart kırpması. ⚠️ Kare kare inceleme sahip isteğiyle kısa tutuldu ("foto falan inceleme" — 19.10.2026);
`kapak_prova.py` ve gök bandı ölçümü koşulmadı. Dosyalar: scratchpad `hlqa/`.

```
YAYIN KURGUSU (2x)        kaynak                         ölçüm
 0,00 –  4,00  S0 BOŞALIR       tam                              ✅ klip_eslestir (zincir dikişleri görünmez — kare farkı tepesi yok)
 4,00 –  8,00  S1 BOYANIR       tam                              ✅
 8,00 – 12,00  S2 DÖŞENİR       tam                              ✅
12,00 – 16,00  S3 KÜTÜPHANE     tam                              ✅
16,00 – 20,00  S4 KANEPE        tam                              ✅
20,00 – 24,00  S5 OTURMA GRUBU  tam                              ✅
24,00 – 28,00  S6 RAFLAR VE TABLO tam                            ✅
28,00 – 31,87  S7 PENCERE AÇILIR (rejim G) · tutuş ≈ 30,75–31,75   ½ (işçi kapıdan 30,75'te çıktı — plan tutuşu 30,0–32,0)
31,75 – 32,25  ERİME: başlık S7'nin üstünde belirir (0,5 sn · plan "≤ 1 sn" ✅)
32,25 – 37,01  SABİT KART  G8 + "THE HIDDEN / LOFT" · fark 0,00–0,02 (donmuş kare) ✅
SES            her sahnenin sesi o klibin kendi Veo sesi, 2x (zarf korelasyonu S0–S7: 0,94 · 0,94 · 0,88 · 0,97 · 0,88 · 0,88 · 0,76 · 0,93)
               · S2 (8–12) seviyesi S1'den +15 dB · 32–37 sn −107 → −120 dB = DİJİTAL SESSİZLİK
```

```
⛔ PLAN ↔ DOSYA UYUŞMAZLIKLARI
① MÜZİK       plan "müzik yok · Veo müzik üretirse o klipte ses kurguda değiştirilir" · ❶ ❷ 8,0–12,0'da akustik gitar duydu; yayının sesi
              S2 klibinin ham üreteç sesi (ajan kulakla doğrulamadı — tonallık ölçümü müziği ayırmıyor).
② KART SESİ   plan "oda tonu sürer, kartın son saniyesinde söner" · dosya 32,0'dan sonra dijital sessizlik (RAIN TOWER E13'ün aynısı).
③ BAŞLIK      plan kutusu y 560–770 · kart ve kapakta y ≈ 397–614 (≈ 160 px yukarı). Kapak 941×1672 (1080×1920 değil). kapak_prova koşulmadı.
④ ÇÖZÜNÜRLÜK  teslim 1080×1920 olmalı · dosya 2160×3840 (üçüncü film).
⑤ KAYIT       günlük boş · qa_paket / ihrac_kontrol koşulmadı · beş mercek ölçülmüş olgular bloğu BOŞ koşuldu (❶ ❷ kendisi söyledi).
```

```
✅ TUTANLAR (ölçüldü)
· sekiz klibin sekizi yayında, sıra doğru, her biri 4,0 sn; kart 5,13 sn (DERS 86 ✅) · kart = G8 + başlık, son sahneyle aynı kadraj (DERS 85 ✅)
· kamera kilidi: ❶ CAMERA LOCK 10 — çatı, mahya, pencere kasası dokuz karede aynı (DERS 80 çatı terimi tuttu, "truss" sızmadı)
· iki işçi: ❹ CAST LIST 8 klibin 8'inde "human workers (2)" (DERS 89 sayım kilidi tuttu)
· geç teslimat 7/7 (DERS 92 3. ölçüm)
· ⭐ İŞLEV ANI (S7): iki işçi kâğıdı indirdi (28,0–29,25), uzun altın bantlar sola düştü (güneş 295°, pencere 275° — plan yönü ✅), işçiler merdivenle
  kapıdan çıktı, oda boş ve sabit (≈ 30,75–31,75). ❷ 8 LAST SECONDS 9 · C3 7 · ❺ (bağlayıcı değil) FINAL BEAT PASS.
· kütüphane modülleri kapıdan TEK TEK geldi (12,5–14,0), lambader kapıdan pencerenin soluna taşındı (13,75–14,5), berjerler tek tek (20,25 · 20,75),
  traverten tabla iki elde düz (21,75–22,25) — ❶'in "yerinde büyüdü" / "sıçradı" okumaları kısmen yanlış.
```

## ⭐ PROMPT ↔ EKRAN — sahne sahne (yayın 2x · ajan 4 fps panosu · rapor eşleşmesi)

| S | prompt ne istedi | ekranda ne oldu (yayın sn) | tuttu mu | rapor ne dedi | olay · ders |
|:-:|---|---|:-:|---|---|
| 0 | halı İLK KAREDE uzakta rulo, iki işçi kameraya doğru sarar · rulo omuzda kapıdan · sandık/tahta · boya takımı + kâğıt (son) | rulo 0,25–0,5'te kameranın dibine kadar geldi (alt bantta dev bulanık çubuk) · 0,75'te kendiliğinden açılıp DİK LEVHA oldu, iki işçi tutup geri taşıdı · sandıklar yerinde küçüldü, tahta yığını sağa saçıldı · boya takımı + merdiven 3,25 ✅ | ½ | ❶ "bar vanishes" · ❶ ❹ sandık/tahta | E01 · E02 |
| 1 | cam silinir, kâğıt bantlanır · rulolar şerit şerit sol → arka → sağ · meşe paketleri gelir | cam + kâğıt 4,0–5,0 ✅ · duvarlar 5,0–6,0 sol → arka → sağ, rulolu işçi görünür · meşe 6,75–7,75 ✅ | ✅ | ❶ ❹ "opacity fade-in" · ❹ ilk beliren parça | E03 |
| 2 | meşe ENİNE, sıra sıra kameradan arka duvara · süpürgelik · ambalaj araba ile çıkar | tahtalar BOYUNA, sağdan sola kama · 10,5→10,75 zemin yerinde ENİNE yeniden çizildi · 9,0–10,5 zeminde parlak çapraz leke · araba 10,75 ✅ | ❌ | ❶ ❷ ❹ "kesmede 90° döndü" (kesme değil) · ❷ "örtülü pencerede güneş" | E04 · E05 · DERS 102 · 104 |
| 3 | üç modül tek tek kapıdan, arkadan öne · lambader pencere soluna · halı rulosu kapı yanına | modüller ✅ · lambader ✅ · halı rulosu sağ yarıya çekildi, yarı açıldı (15,0–15,5), 15,75'te kapı yanında yeniden sarılı | ½ | ❶ "bookcase grows" (kısmen yanlış) · ❶ "rug pops in" | E06 |
| 4 | halı kameraya doğru açılır · yarı ① uzak yarıya, sırtı pencereye · yarı ② itilir · sehpa ayağı (son) | halı ✅ (16,25–17,25) · 17,75 arka duvarda küçük kanepe · 18,25–19,0 yarılar ORTADA, sırtı kameraya birleşti · 19,0→19,25 küçülüp 180° döndü, arka duvara sıçradı · ayak 19,5 ✅ | ❌ | ❶ THE BODY THAT MELTED WORST ✓ · ❷ · ❹ | E07 · DERS 103 |
| 5 | berjerler tek tek · ayak ortaya · tabla iki elde düz · koliler (son) | ✅ hepsi (20,25–23,25) · 20,25 kameraya yakın bulanık figür · 21,25–22,5 sol kenarda siyah ayak benzeri nesne | ✅ (küçük) | ❶ "tripod leg" ✓ | E08 |
| 6 | kitaplar · tablo · araba çıkar · zeytin ağacı · iki işçi kâğıtta | ✅ hepsi · kâğıt altına döndü ✅ · ⛔ kapı 24,75–26,25'te DIŞ BALKONA açıldı | ½ | ❶ Anchor 3 ✓ · ❹ "balcony" ✓ · ❷ "turuncu parıltı" | E09 · DERS 101 · 104 |
| 7 | kâğıt alt köşelerden TEPEDEN AŞAĞI iner · altın üçgen · kâğıt + merdiven kapıdan · tutuş 2 sn | kâğıt dikdörtgen sert levha gibi işçilerin başının üstüne kalktı (28,25–28,75, pencerenin alt kasası arkada kaldı), sonra eğilip indi (29,0) · bantlar 28,5'te · işçi 29,75–30,5 yine BALKONA çıktı · tutuş ≈ 1 sn | ✅ (levha ½) | ❶ "frame vanishes into yellow wall" · ❷ 8: 9 · ❺ PASS | E09 · E10 · E11 |
| kart | G8 + başlık y 560–770 · erime ≤ 1 sn · oda tonu sürer | G8 ✅ · erime 0,5 sn ✅ · başlık y ≈ 397–614 ❌ · sessizlik ❌ | ½ | ❶ C5 7 · ❹ C1 7 ("kartta kapı kapalı" — 31,6'da da kapalı) · ❺ C2 10 | E13 · E14 |

```
ÖZET   MEKÂN dili TUTTU (tek oda, çatı, pencere, kapı yeri, iki işçi, kamera). İŞLEV ANI TUTTU: kâğıt indi, güneş doğru yönden girdi, oda boş
       kaldı. GEÇ TESLİMAT 7/7. Kopanlar dört aile:
       ① GÖRÜNMEYEN MEKÂN — kapı arkası balkona döndü (DERS 101, S6 · S7);
       ② YÖN/İLERLEME — "across the width" parkeyi boyuna döşetti, son kare enine çizdirdi (DERS 102, S2);
       ③ UÇ KARE ↔ KLİP İÇİ YOL — kanepe ortada birleşip 180° dönerek sıçradı (DERS 103, S4) · halı rulosu geri sarıldı (S3) · S0 rulosu levhaya döndü;
       ④ ZAMAN OKUNMADI — kâğıt zaman taşıyıcısı kör ❷'de çalışmadı (DERS 104).
       Teslim kilitleri üçüncü filmde de kurguya inmedi (DERS 100 2. ölçüm); QA paketsiz koşuldu, iki mercek uydurma tam puan verdi (DERS 105).
```

## MERCEKLER
| mercek | durum | puan | hüküm | ham | en ağır üç bulgu (m:ss.s) · ajan notu |
|---|---|:-:|---|---|---|
| ❶ GÖRÜNTÜ | TAM (blok boş · D4 ✗) | 5,4 | TIMELAPSE · MELTING | THE_HIDDEN_LOFT_Q1_GORUNTU_HAM.md | 0:18–0:19 kanepe döndü/küçüldü (E07 ✓) · 0:25–0:29 kapı balkon (E09 ✓) · 0:10–0:11 parke 90° (E04 ✓, kesme değil S2 içi) · ⚠️ kesme listesi yanlış; kütüphane "büyüdü" ve kart kapısı okumaları kısmen yanlış |
| ❷ ZAMAN VE KESME | EKSİK (blok boş → 6 · 7 · C1 + üç hüküm NOT VERIFIABLE · D4 ✗) | — (bağlayıcı değil: 4,5) | WRONG DIRECTION | THE_HIDDEN_LOFT_Q2_ZAMAN_KESME_HAM.md | 0:04–0:28 örtülü pencere, mevsim taşıyıcısı yok (DERS 104 ✓) · 0:08–0:10 / 0:17 örtülü pencerede leke (E05 — S2 ✓, 17,0 bakılmadı) · 0:08–0:12 müzik (E12 ✓ kaynak) |
| ❸ ŞANTİYE | EKSİK + ŞİŞİK (D2 · D4 · D6) | — (bağlayıcı değil: 10,0) | SAME WORLD · WORKING | THE_HIDDEN_LOFT_Q3_SANTIYE_HAM.md | 32 × 1 sn klip uydurdu · 31/31 dikiş INTENDED · tavan lambası / "ışık yandı" ekranda yok · ⚠️ ❺ ile aynı uydurmalar |
| ❹ İNŞA | TAM (mod V · D4 ✗) | 5,4 | SAME · APPEARING · INVITED | THE_HIDDEN_LOFT_Q4_INSA_HAM.md | 0:18 kanepe döndü (E07 ✓) · 0:25 kapı balkon (E09 ✓) · 0:08 parke çözülerek (E04 ✓) · evre sınırları yanlış (0:03 · 0:06 · 0:11 …) |
| ❺ TESLİM | EKSİK + ŞİŞİK (D2 · D6) | — (bağlayıcı değil: 10,0) | ENDS | THE_HIDDEN_LOFT_Q5_TESLIM_HAM.md | final PASS (✓ ölçümle) · C1 MUSIC 10 (müzik var — ❶ ❷) · C2 kart 10 (sessizlik ve başlık yeri görülmedi) · ⚠️ ❸ ile aynı uydurmalar |
FİLM PUANI  5,4 · N=2 (❶ 5,4 · ❹ 5,4)          ÖLDÜRÜCÜ  — (❶ TIMELAPSE · ❹ SAME · ❸ REBUILT yok — ❸ bağlayıcı değil)
⚠️ PUAN BAĞLAYICI DEĞİL: kör üçlüden yalnız ❶ TAM; ❷ ❸ ❺ boş blok ve D-kaldılarıyla geçersiz. Hüküm satırları NONE değil:
❶ en kötü eriyen cisim (S4 kanepe) · ❹ ilk beliren parça (S1 duvar — boya rulolu işçiyle görünüyor, kabul) → S4 yeniden üretim adayıdır,
ortalama ne olursa olsun [AGENTS kart R 6].

## DOĞRULAMA
- Geri okuma: ❶ ✗ NOT SHOWN / NONE / 8+kart · ❷ ✓ the hıdden loft.mp4 / NONE / 8+kart · ❸ ✗ "THE HIDDEN LOFT" / NONE / 33 · ❹ ✓ / NONE (mod V) / 8 ·
  ❺ ✓ / NONE (mod V) / 33
- D1: dosya dışı damga yok ✓ · D2: ❸ ❺ 33 ✗, diğerleri 8 ✓ · D3: süre itirazı yok ✓ · D4: ❶ ❷ ❹ aynı yanlış kesme listesi 0:03 · 0:06 · 0:11 · 0:15 ·
  0:18 · 0:21 · 0:26 (dosyada 4,0 · 8,0 · 12,0 · 16,0 · 20,0 · 24,0 · 28,0 — klip_eslestir, sapma 1–3 sn) ✗ · ❸ her tam saniyede ✗ · D5: kart VAR, beşi de gördü ✓ ·
  D6: ❶ ❷ ❹ klip sayısı ve olaylar panoyla tutuyor, sınırlar tutmuyor (D4) · ❸ ❺ tutmuyor (32 × 1 sn · uydurma olay) → ŞİŞİK.
- Sızıntı taraması: ❶ ❷ ❸ temiz — plan sayısı, "G0…G8", "spec", "landing", "paper" (planın sözcükleri) yok; "truss" planın YASAK KELİMESİ,
  ekrandan okunmuş. ❸ ❺'in ortak uydurmaları (tavan lambası, ışığın yanması, 1 sn bölütleme) plandan değil → sızıntı değil, yalıtım şüphesi.

## DOKÜMAN

### ❶ GÖRÜNTÜ
1. **Blok değerleri:** hız 2x · 8 klip · yayında 4,0 sn · kesmeler 4,0 · 8,0 · 12,0 · 16,0 · 20,0 · 24,0 · 28,0 · END CARD = YES (31,75–37,0; erime 0,5 sn) · MÜZİK = YOK · 9:16 · 37,0 sn · final tutuşu planda 2 sn (30,0–32,0).
2. **Parke yönü:** Plan ENİNE (arka duvara paralel), sıralar kameradan arka duvara. Boyuna döşeme S2'nin içinde oldu; zemin 10,5–10,75'te yerinde enine yeniden çizildi — kesmede değil → E04 · DERS 102.
3. **Anchor 3:** Açık kapı, ardında loş merdiven sahanlığı (dokuz karede). Balkon ve kapanan kapı plan dışı → E09 · DERS 101.
4. **Ön plan çubuğu ve siyah ayak:** 0:00 çubuğu halı rulosu (plan: rulo kameraya doğru sarılır, ama bütün iş d ≥ 4,3 m'de kalmalıydı). 0:21 siyah ayak plan dışı; kadrajda sehpa/tripod yok → E08.
5. **Kütüphane:** Evet, üç modül tek tek, kapıdan yan yatık. Ekranda modüller bir işçiyle kapıdan geliyor (12,5–14,0); "2 → 6 bölme" üç modülün sırayla gelişi.

### ❷ ZAMAN VE KESME
1. **Blok:** yukarıdaki ❶-1.
2. **Güneş:** 21 Haziran, 41° K, güneş saati — G0 60°/+2,2° · G1 79°/+23,3° · G2 98°/+45,9° · G3 132°/+66,4° · G4 212°/+70,1° · G5 256°/+51,4° · G6 277°/+28,9° · G7–G8 295°/+7,2°. Pencere batıya (275°). S2'de güneş doğuda, evin arkasında: batı penceresinden sert ışın giremez. Kâğıt S1–S7 ışığı yayar, "ışık lekesi yok" → 8–10 ve 17,0 lekeleri plan dışı (E05).
3. **Mevsim:** tek gün, yaz dönümü. S2–S6 zaman taşıyıcısı kâğıdın rengi (beyaz → altın) — planın bilinçli kararı; kör mercekte çalışmadı → DERS 104.
4. **Süre:** S0–S6 2'şer saat (rejim B), S7 8 sn gerçek zaman (rejim G); 04:45 → 18:45 + 8 sn, tek gün. ⚠️ İki keyframe zincirinde zaman klibin İÇİNDE akar, kesme sıçrama değildir. Tutulan saat yok; S7 gerçek zamanlı tutuş.
5. **Müzik:** Hayır — plan müziksiz, diegetik ses tablosu. 8–12 sn müziği S2 klibinin ham üreteç sesi → E12.

### ❸ ŞANTİYE (rapor bağlayıcı değil — sorular yine cevaplanır)
1. **Eski döşeme:** Söküm yok; meşe eski tahtanın ÜSTÜNE döşenir (S2 "onto the old floorboards").
2. **Takvim:** tek gün, 04:45 → 18:45 + 8 sn.
3. **Tavan lambası:** Planda yok; ekranda da yok. Lambader sönük kalır; ışık yalnız pencereden. Rapordaki "ışık yandı" uydurma → DERS 105.
4. **Mobilya sırası:** fizik sırası, çevreden merkeze değil — kütüphane (S3) → halı + kanepe uzak yarıda (S4) → berjerler yakın yarıda, sonra ayak + tabla (S5) → kitap, tablo, ağaç (S6).
5. **Başka oda:** Hayır.

### ❹ İNŞA (mod V)
1. **Ölçüler:** iç 5,00 × 10,00 m · yan duvar +2,40 · mahya +4,60 · üçgen pencere taban 2,40 m (+0,40 → +2,90) · kapı 0,90 × 2,00 · açık meşe enine + beyaz süpürgelik · üç ceviz modül ≈ 1,0 m, +2,20 · konyak deri kanepe 2,80 m (iki yarı) · iki krem berjer · traverten tabla + siyah çelik ayak · soyut tablo ≈ 1,40 × 1,00.
2. **Belirme mi taşıma mı:** Taşıma ve montaj planlandı (modüller tek tek kapıdan, meşe sıra sıra, kanepe yarıları tek tek). Çözülme planlanmadı.
3. **Geçici işler:** katlı merdiven (S0 sonu gelir, S7'de çıkar) · koruma kâğıdı (S1 → S7) · boya takımı (S0 → S1) · el arabası (S2 · S5–S6). İskele yok.
4. **Ekip akışı:** iki işçi bütün film; S4 halı + kanepe yarıları · S5 berjerler + ayak + tabla · S6 kitaplar + tablo + ağaç · S7 kâğıt + merdiven çıkar.
5. **Kapı → balkon:** Planlanmadı — kapı dokuz karede açık, ardında loş sahanlık → E09 · DERS 101.

### ❺ TESLİM (rapor bağlayıcı değil)
1. **Bütçe:** Planda yok (kurgu film; açıklamada AI beyanı).
2. **Çatı güçlendirme:** Yok; çatı dokuz karede aynı eski koyu ahşap, hiç değişmez.
3. **Döşeme:** açık meşe.
4. **Stil:** dönem belirtilmedi — ceviz kütüphane, konyak deri, krem bukle; çağdaş salon.
5. **Kullanım:** özel salon (kurgu).

## OLAY TABLOSU
| olay | zaman (yayın 2x) | ne oldu (görünen) | mercekler | kanıt | karar |
|---|---|---|---|---|---|
| E01 | 0,25–1,25 (S0) | Halı rulosu kameranın dibine kadar yuvarlandı (alt bantta dev bulanık çubuk), 0,75'te kendiliğinden açılıp dik levha oldu; iki işçi levhayı geri taşıdı. Plan: rulo omuzda kapıdan, "kendiliğinden açılırsa klip atılır" | ❶ ❷ ❹ | k0 1. satır | S0 yeniden adayı (orta) — rulo d ≥ 7 m'de kalır, "the roll stays rolled tight on their shoulders all the way to the door" |
| E02 | 1,0–3,0 (S0) | Sandıklar yerinde küçüldü; sol duvardaki tahta yığını kayboldu, ortada saçıldı | ❶ ❷ ❹ | k0 | kabul (küçük) — S0 yeniden üretilirse birlikte |
| E03 | 5,0–6,0 (S1) | Duvarlar ≈ 1 sn'de beyaza döndü; rulolu işçi sol duvarda görünür. ❹ ilk beliren parça | ❶ ❷ ❹ | k1 | kabul — rejim B 900×'te duvar başına ≈ 0,75 sn; işçi ve sıra (sol → arka → sağ) görünür |
| E04 | 8,25–10,75 (S2) | ⭐ Meşe boyuna döşendi, sağdan sola kama; 10,5→10,75 zemin yerinde enine, farklı tonda yeniden çizildi | ❶ ❷ ❹ | k2 | ⛔ S2 yeniden — yön ve ilerleme ayrı cümle, G2'de enine ilk iki sıra [DERS 102] |
| E05 | 9,0–10,5 (S2) · 17,0 (❷) | Kâğıtlı pencerede zeminde parlak çapraz leke; güneş doğuda — imkânsız güneş ya da yeni meşede yansıma (ayrılamıyor) | ❷ ❶ (lens 2) | k2 | S2 ile birlikte: "soft even light, no sunlit patches on the floor while the paper is on" [DERS 104 ③] |
| E06 | 14,75–15,75 (S3) | Halı rulosu sağ yarıya çekildi, yarı açıldı, 15,75'te kapı yanında yeniden sarılı (G4 kilidi) | ❶ ❷ ❹ | k3 2. satır | kabul (düşük) — rulo doğrudan kapı yanına; istenirse S3 yalnız I2V |
| E07 | 17,75–19,25 (S4) | ⭐ Kanepe ortada, sırtı kameraya birleşti (≈ %12–88), 19,0→19,25 küçülüp 180° döndü, arka duvara sıçradı; 17,75'te arka duvarda erken bir kanepe | ❶ (en kötü) ❷ ❹ | k4 2. satır | ⛔ S4 yeniden (pilot c′ klibi) [DERS 103 · 89] |
| E08 | 20,25 · 21,25–22,5 (S5) | Kameraya yakın bulanık figür; sol kenarda siyah ayak benzeri nesne alt güvenli bantta | ❶ | k5 | kabul (düşük) — S5 yeniden üretilirse "no object stands near the camera" |
| E09 | 24,75–26,25 (S6) · 29,75–30,5 (S7) | ⭐ Kapı ardında dış balkon (korkuluk, gök, çam); arada kapalı kapı; S7'de işçi balkona çıktı | ❶ ❹ (❷ lens 1) | door_seq | S6 yeniden adayı (orta) — sahanlık penceresiz yazılır, kapı tek hâlde [DERS 101]; S7'de yalnız 0,75 sn, final korunur |
| E10 | 28,25–29,0 (S7) | Kâğıt sert dikdörtgen levha gibi işçilerin başının üstüne kalktı, pencerenin alt kasası arkada kaldı ("sarı duvar"), sonra eğilip indi; plan: alt köşelerden tepeden aşağı | ❶ ❷ ❹ | k7 1. satır | kabul — işlev anı okundu (❷ 8: 9 · C3 7); S7 yeniden üretilmez |
| E11 | 29,75–31,75 (S7) | Son işçi 30,75'te çıktı, tutuş ≈ 1 sn (plan 2 sn); başlık 31,75'te tutuşun üstüne eriyor | ❷ 8 (9) | kart.png | kabul — DERS 92 (ikinci yarı geç); kurguda başlık 32,0'dan sonra başlatılırsa tutuş 1,25 sn |
| E12 | 8,0–12,0 | Akustik gitar (❶ ❷); yayının sesi S2 klibinin ham Veo sesi | ❶ ❷ | ses ölçümü | yeniden kurgu — S2 sesi değiştirilir (plan §SES S2 imzası: parke klik + tokmak) [DERS 100] |
| E13 | 32,0–37,0 | Kartta dijital sessizlik (−107 → −120 dB); plan: oda tonu sürer, son saniyede söner | — (❺ C2 10 görmedi) | ses ölçümü | yeniden kurgu — S7 oda tonu + kuşlar 5 sn uzatılır, son 1 sn söner [RAIN TOWER E13] |
| E14 | kart · kapak | Başlık y ≈ 397–614 (plan 560–770); kapak 941×1672 | — | kart kırpması | kapak 1080×1920 yeniden dışa aktarım + kapak_prova [DERS 99 2. ölçüm] |
| E15 | tüm film | Teslim 2160×3840 (plan 1080×1920) | — | ffprobe | yeniden ihraç 1080×1920 [POOL ROOM E08 · RAIN TOWER E14] |
| E16 | kayıt | Günlük boş · qa_paket koşulmadı · beş mercek boş blokla · ❸ ❺ uydurma tam puan · ❶ ❷ ❹ aynı yanlış kesme listesi | ❶ ❷ (kendileri söyledi) · ❸ ❺ | ham künyeler | ❷ ❸ ❺ yeniden koşulur, blok dolu (ajan doldurur) [DERS 105] |

## KARAR

⭐ **SAHİP KARARI BEKLİYOR** — öldürücü hüküm yok; işlev anı ekranda tuttu (kâğıt iner, güneş doğru yönden girer, oda boş kalır).

- **Önce yeniden kurgu (klip üretimi yok):** S2 sesi müziksiz (E12) · kartta oda tonu (E13) · 1080×1920 ihraç (E15) · kapak 1080×1920 + `kapak_prova.py` (E14) · başlık erimesi 32,0'dan sonra (E11). Sonra `ihrac_kontrol.sh` + `klip_eslestir.py … --hiz 2 --kart 5`.
- **Yeniden üretim adayları (öncelik sırasıyla):**
  1. **S4 (E07)** — ❶'in en kötü eriyen cismi. Uç kareler (G4 · G5) kalır; I2V yeniden, DERS 103 kilitleriyle.
  2. **S2 (E04 · E05)** — parke yönü. G2'ye enine ilk iki sıra çizilirse G2 değişir → S1'in bitişi de değişir; yalnız I2V ile denenebilir (DERS 102 ①③).
  3. **S6 (E09)** — kapı balkonu. Yalnız I2V (DERS 101 ①②); G6 · G7'de kapı kapalı çizilirse daha sağlam, ama G7 rejim G karesi — S7 de etkilenir.
  4. **S0 (E01 · E02)** — rulo levhaya döndü; düşük-orta.
- **Kabul edilen:** E03 · E06 · E08 · E10 · E11.
- **Plan dersi (sonraki filmler):** tek pencereyi beş klip örtmek zamanı kör okuyucudan sakladı (DERS 104). Bu filmde değiştirilmez — işlev anı sahip seçimi ve ekranda çalıştı.
- **QA yeniden koşulur:** kurgu düzeldikten sonra beş mercek, blok ajanın doldurduğu değerlerle (kesmeler 4,0 · 8,0 … 28,0 · kart 32,0–37,0 · müzik yok); ❶ ❷ ❸ geçici sohbette belgesiz, AYRI sohbetlerde; ❹ ❺ plan + QA_SPEC (+ kapak) ile mod D.

## DERS
- DERS 92 — 3. ölçüm: geç teslimat 7/7, S7 tutuşu ≈ 1 sn (ek satır)
- DERS 99 — 2. ölçüm: başlık yine plan kutusunun ≈ 160 px üstünde; kapak 941×1672 (ek satır)
- DERS 100 — 2. ölçüm: çözünürlük, kart sesi, ham Veo sesi (müzik) — üçüncü film (ek satır)
- DERS 101 — Kapının arkası (görünmeyen sahanlık) her açılışta yeniden çizildi: balkon, gök, çam
- DERS 102 — "Across the width" ilerleme okundu: parke boyuna döşendi, klip sonunda enine yeniden çizildi
- DERS 103 — Kanepe ortada, sırtı kameraya birleşti; 180° döndü ve arka duvara ışınlandı
- DERS 104 — Kâğıtla örtülü pencere zamanı taşımadı: kör ❷ WRONG DIRECTION
- DERS 105 — Boş blokla koşulan iki mercek 1 sn'lik 32 klip uydurdu, her kategoriye 10 verdi
