# 🗒️ THE_OLD_ROAD — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · bu günlüğe tek satır yazılmadı · (16.09.2026 klasör açıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28 — dört filmde dört kez tutulmadı]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `kilavuzlar/FILM_KLASOR_SABLONU/FILM_URETIM_GUNLUGU.md` (dikey karşılığı `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`).
> Plan: `THE_OLD_ROAD_PLAN.md` · promptlar `THE_OLD_ROAD_BOLUM_1.md` · `_BOLUM_2.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 15 sahne = 16 kare (G0…G15) + 15 I2V [KILAVUZ_REHBERI §2.7].
> Izgara: ⛔ DÜZ 15 × 8,0 = 120,0 sn (sahip beyanı; ⑥ METRONOM beklenen risk — PLAN §AŞAMA MERDİVENİ).
> ⛔ Prompt dosyaları ÜRETİMDEN SONRA GÜNCELLENMEZ: üretilmiş filmin promptu kanıttır; QA onu ölçer. Sapma §5'e.

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32 · A7-d]

> Yordam ve test promptu: `kilavuzlar/ARAC_KARTLARI.md` §4-§5. Kart doldurulmadan tek kare üretilmez.
> ⭐ ⑧ (iki kare) formatın kendisidir; almıyorsa araç değişir, plan düşürülmez.

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü — araştırma raporundan alınmaz, A7-X2]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne: 8,0
   ⛔ tavan ≥ 8,0 (kutu tam 8,0 kırpmasız ya da 9,0 → baştan 1,0 kırp [A7-b]) ise tek klip.
   ⛔ tavan < 8,0 ise 15 sahnenin hepsi iki zincirli klip (ara kare Gn′) — ızgara kararı
      proje sahibine döner; karar buraya yazılır:
   KARAR         ____
② KAMERA        ilk/son kare kayması: ____ px    (>2 px ise ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5   (plan promptları 5.700–6.000 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
⑨ 16:9          araç 1920×1080 (ya da 16:9 4K) veriyor mu: __ · kırpma/letterbox yok: __
⑨ ⭐ İTME TESTİ  (bu filme özel · 1 numaralı risk) test klibinde uzun bir gövde kadraj içinde YATAY kaydırılıyor mu,
                yoksa hedefte kopyalanıp kaynağı siliniyor mu [DERS 57 mekanizması]: ____
                ⛔ kopyalıyorsa bu film o araçta üretilmez — plan değil ARAÇ değişir
⑩ 16:9 ÇIKIŞ    araç 1920×1080 veriyor mu (yatay master) · kırpma/ölçekleme yapıyor mu: ____
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 1. USTA KARE

```
KARE    G15 (son klibin HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir BOLUM_2 §USTA KARE'den / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    final hiyerarşisi ① ② ③ bu sırayla okunuyor mu · taç %__ · kanıt nesnesi %__ / __ px ·
        geçici ekipman YOK · ufuk %50 · üst sekiz boş · yanlarda çapalar → geçti/düştü
PİKSEL  kanıt nesnesi __ px · çapa ① __ px → PLAN ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G14 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = ESKİ TAŞ KEMER KÖPRÜ (x %44,4 · y %34,2 · 64 × 21 px) + eski yolun viraj geometrisi, elle ✓/✗ [DERS 25].
> ⭐ İTME KARELERİNDE (G4–G12) AYRICA: ilk dökülen kesitin KOYU DÖKÜM DERZİ hâlâ en önde mi ve gövde bir ayaktan
> fazlasını atlamadı mı — elle [DERS 57 mekanizması]. Her karede sayım: viyadük 1 · taş köprü 1 [DERS 55].
> ⛔ ARA KARE YOK (sahip kararı): tavan < 8,0 ise araç değişir ya da karar sahibe döner — §0 KARAR satırı.
> ⭐ G8 bölüm sınırı karesidir: BOLUM_2'nin ilk görseli, BOLUM_1'in son I2V hedefi — tek kare, tek satır.

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi (değilse ne) | zincir_kontrol | kanıt nesnesi elle | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|---|
| 14 | | G15 | lambalar söner · asfalt, korkuluk, direkler kaldırılır → çıplak beton üst yüzey · hangar ve şantiye yolu GERİ · 18:15 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 13 | | G14 | çelik burun ve geçici destek GERİ · kaya apronu geri · tabliye itme mesnetlerine yükselir · hangar + itme yatağı GERİ · 16:15 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 12 | | G13 | beton gövde P5'e çekilir (ucu %76,3) · burun A2 sekisinde kalır · kriko takımı geri · 16:05 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 11 | | G12 | gövde P4'e çekilir (ucu %63,2) · burun A2'den ayrılır → son açıklık · kuyruktaki iki kesit hangara geri · 15:55 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 10 | | G11 | su YÜKSELİR (sel tepe) · menfez ve yeni çaprazlar sökülür · sürüntü matı ve aşılmış berm GERİ · 13:55 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 9 | | G10 | su bir kademe iner · geçici geçiş GERİ · berm sağlam · plant yüksek alanda · 13:45 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 8 | | G9 | gövde P3'e kısalır (ucu %50) · berm kaldırılır · nehir normale · kış girer · 11:45 | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ bölüm sınırı karesi |
| 7 | | G8 | gövde P2'ye kısalır (ucu %36,8) · geçici destek KALKAR · kış çıkar, sonbahar girer · 09:45 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 6 | | G7 | gövde P1'e kısalır (ucu %23,7) · bir kesit hangara geri · 09:35 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 5 | | G6 | gövde döküm alanına çekilir · burun A1 ucuna (%17) · 09:25 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 4 | | G5 | hangar, itme yatağı ve burun KALKAR · beş ayak tam kalır · 07:25 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 3 | | G4 | ayaklar iner → kazık başları · tırmanır kalıplar kalkar · geçici geçiş ve haul road kalır · 07:15 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 2 | | G3 | temeller kalkar → işaretli yaklaşım alanları · kazık makinesi girer · 05:15 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 1 | | G2 | şantiye yolu ve geçici geçiş kalkar → dokunulmamış vadi tabanı · kesi kısalır · 05:05 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 0 | | G1 | kesi ilk 20 m'ye iner · low-loader ve ekskavatör çıkar · dozer taze kesinin başında · şafak | | geçti/düştü | ✓/✗ | ✓/✗ | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o kare atılır, yeniden
   türetilir, satır yeniden yazılır [DERS 12 · 25]. Düşen kareden türetilmiş alt kare tabloya giremez.
⚠️ 16 karelik zincirde hata birikimi (A3-a) beklenir: her ~10 karede G(n) ↔ G15 yan yana konur
   (çapa ① ② ve kanıt nesnesi px) — kayma ≥ 2 px ise zincir usta kareden yeniden alınır.
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kırpma BAŞTAN [§2.7 ③]. REJİM sütunu boş bırakılamaz [A6-a].
> ⛔ HER KLİP İKİ ONAYLI KAREYE KİLİTLİDİR: ilk kare G(n), son kare G(n+1); klip üretildikten SONRA
> son kare ↔ hedef görsel zincir_kontrol koşulur [§2.7 · ARAC_KARTLARI ⑧].

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|---|
| 0 | | | G0 | G1 | geçti/düştü | | | 30/0 | 8,0 | | |
| 1 | | | G1 | G2 | geçti/düştü | | | 30/0 | 8,0 | | |
| 2 | | | G2 | G3 | geçti/düştü | | | 30/0 | 8,0 | | |
| 3 | | | G3 | G4 | geçti/düştü | | | 30/0 | 8,0 | | |
| 4 | | | G4 | G5 | geçti/düştü | | | 30/0 | 8,0 | | |
| 5 | | | G5 | G6 | geçti/düştü | | | 30/0 | 8,0 | | |
| 6 | | | G6 | G7 | geçti/düştü | | | 30/0 | 8,0 | | |
| 7 | | | G7 | G8 | geçti/düştü | | | 30/0 | 8,0 | | |
| 8 | | | G8 | G9 | geçti/düştü | | | 30/0 | 8,0 | | |
| 9 | | | G9 | G10 | geçti/düştü | | | 30/0 | 8,0 | | |
| 10 | | | G10 | G11 | geçti/düştü | | | 30/0 | 8,0 | | |
| 11 | | | G11 | G12 | geçti/düştü | | | 30/0 | 8,0 | | |
| 12 | | | G12 | G13 | geçti/düştü | | | 30/0 | 8,0 | | |
| 13 | | | G13 | G14 | geçti/düştü | | | 30/0 | 8,0 | | |
| 14 | | | G14 | G15 (usta kare) | geçti/düştü | | | 30/0 | 8,0 | | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6] — TAM master

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____   (1920,1080,30/1,h264 · tolerans SIFIR)
② SÜRE          ffprobe format=duration → ____ sn   (120,0 + 5,0 = 125,0)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_OLD_ROAD/THE_OLD_ROAD_PLAN.md → çıkış: __
                beklenen kesmeler 8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn)
                ("PLANIN KENDİSİ DÜZ" uyarısı beklenir — kabul edilmiş risk, çıkış kodunu değiştirmez)
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        müziksiz pencere 0,0–__ plana uygun mu: evet/hayır
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 kanit.jpg → SPEC §1 üçlüsü görünüyor mu: __
                KAPAK KAYNAĞI ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 g15_kaynak.jpg
                KAPAK KANITI  bash araclar/zincir_kontrol.sh g15_kaynak.jpg kapak.png → __
BÖLÜM SINIRI    ffmpeg -ss 64.0 -i teslim.mp4 -frames:v 1 sinir.jpg → SPEC §7 ile aynı mı: __
```

### 4b. QA MASTERLARI (yalnız 6/8 dk · QA birimi BÖLÜM)

```
B1  ffmpeg -i teslim.mp4 -t 64 -c copy b1.mp4        → ffprobe süre ____ (64,0)
B2  ffmpeg -ss 64 -i teslim.mp4 -c copy b2.mp4       → ffprobe süre ____ (125 − 64)
b1_son.jpg ↔ b2_ilk.jpg zincir_kontrol → __   (dikiş = G8)
QA paketi bölüm başına: bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_OLD_ROAD b1.mp4 · … b2.mp4 (ham dosya adı B1_/B2_ eki alır)
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
```
