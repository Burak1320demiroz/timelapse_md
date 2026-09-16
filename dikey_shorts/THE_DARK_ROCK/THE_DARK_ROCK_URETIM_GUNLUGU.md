# 🗒️ THE DARK ROCK — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · bu günlüğe tek satır yazılmadı · (15.09.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28 — dört filmde ölçüldü]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
        ⛔ OVER THE WALL ve THE EMPTY RIDGE bu günlük BOŞKEN üretildi; ikisinde de QA arızayı adlandıramadı.
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`. Plan: `THE_DARK_ROCK_DIKEY_TIMELAPSE.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 6 sahne = 7 kare (G0…G6) + 6 I2V · ara kare YOK, her sahne tek 8,0 sn klip [KILAVUZ_REHBERI §2.7].
> Izgara: ⛔ DÜZ 6 × 8,0 = 48,0 sn (proje sahibinin kilidi; ⑥ METRONOM beklenen risk — plan §AŞAMA MERDİVENİ).

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32 · A7-d]

> Yordam ve test promptu: `kilavuzlar/ARAC_KARTLARI.md` §4-§5. Kart doldurulmadan tek kare üretilmez.
> ⭐ Bu filmde ⑧ (iki kare) formatın kendisidir; almıyorsa araç değişir, plan düşürülmez.

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne: 8,0 (altısı da)
   ⛔ tavan ≥ 8,0 (kutu ≥ 9,0) ise tek klip: üret <kutu>, baştan (kutu − 8,0) kırp [A7-b].
   ⛔ tavan < 8,0 ise ({4,6,8}) bu araçta sahne tek 8,0 sn klip olamaz — ARA KARE YOK (15.09.2026):
      araç değişir ya da karar proje sahibine döner; karar buraya yazılır:
   KARAR         ____
② KAMERA        ilk/son kare kayması: ____ px    (>2 px ise ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5   (plan promptları 5.527–5.965 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
⑨ DENİZ TESTİ   (bu filme özel, ölçülmemiş) test klibinde sabit kayanın çevresinde deniz: köpük ALAN olarak mı
                okunuyor, ufuk %50'de sabit mi, su seviyesi kayada inip çıkıyor mu: __  — su seviyesi oynuyorsa
                SAHA 3.3 riski bu araçta geçerlidir, promptlar yeniden açılır
⑩ IŞIK TESTİ    (bu filme özel) "lamp lights · glow stays inside the glass" test klibinde huzme/koni çıktı mı: __
                — çıkıyorsa G6 ve S5 I2V yeniden yazılır (ödül ışığın belirmesidir, huzme değil)
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 0b. ÖN GÖRSELLEŞTİRME — usta kareden ÖNCE

```
PLAN + YAN KESİT  güney sütunu (+21 m) · kaya (kaide +8, apron +6) · kule (+48) · NEEDLE (90 m, 14 m) · uzak burun (~3 km)
ÇİZİLDİ Mİ        evet/hayır · dosya: ____
GÜNEŞ             07:00 az 92° → 19:00 az 290° kadraj dışında mı (kadraj az 337°–23°): ✓/✗
```

## 1. USTA KARE

```
KARE    G6 (son klibin HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    rüzgârgülü %82 · fener camı %73–77 YANIK ve ışık camın İÇİNDE · iskele/direk/yükleyici/gemi YOK · kaide düz ·
        apron boş + direk izi · rampa yuvada · NEEDLE x ≈ 761–832, ≈200 px · ufuk %50 · üst 1/8 boş → geçti/düştü
FİNAL HİYERARŞİ  ① yanan cam → ② tam granit kule → ③ kesilmiş kaide + boş apron + rampa — bu sırayla okunuyor mu [P1-h]
SAYIM   kule ____ (1) · sütun ____ (1)
PİKSEL  NEEDLE boy ____ px · en ____ px · x ____ · ufuk y ____ · burun sırtı y ____ → plana ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G5 → G4 → G3 → G2 → G1 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = NEEDLE + kayanın alt gövdesi (boy dâhil), elle ✓/✗ [DERS 25].
> ⛔ ARA KARE YOK (15.09.2026): her sahne iki onaylı kare arasında tek 8,0 sn klip; tavan < 8,0 ise §0 KARAR satırı.

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi (değilse ne) | zincir_kontrol | NEEDLE + alt gövde elle | kule/sütun sayımı | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|:---:|---|
| 5 | | G6 | ışık söndürülür · iskele 26. sıraya GERİ · direk +41, kabin dipte · yükleyici + 2 boru demeti · direk izi kaldırılır · balyalar · 17:00 | | geçti/düştü | ✓/✗ | 1/1 | ✓/✗ | |
| 4 | | G5 | fener + külah kaldırılır → çıplak galeri · galeri üstü iskele GERİ · ıslak bant (12. sıra) · birikintiler · gemi rampada · kabin ortada sandıkla · 15:00 | | | | | | |
| 3 | | G4 | rampa yuvada KALIR · gemi kaldırılır · kabin dipte, boş · yükleyici park + branda · ıslak bant ve birikintiler kaldırılır · köpük halkası geniş, apron açıkta · koyu tavan · tarla düz altın · 13:00 | | | | | | |
| 2 | | G3 | galeri + 13–30. sıralar kaldırılır → 12 sıra · iskele ve direk +23 · gök açık · gemi rampada · 4 palet · kabin tepede · 11:00 | | | | | | |
| 1 | | G2 | 12 sıra kaldırılır → çıplak kaide · iskele, direk, rampa, yükleyici, paletler, gemi kaldırılır · ekskavatör apronda · 09:00 | | | | | | |
| 0 | | G1 | kaide kaldırılır → iki çentikli tepe GERİ · apron + basamaklar → doğal omuz + seki · ekskavatör kırıcıyla taçta · gemi sekide + oluk · 07:00 | | | | | | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o kare atılır, yeniden
   türetilir, satır yeniden yazılır [DERS 12 · 25].
⚠️ G1 → G0 filmin tek "doğal şeyi GERİ KOYMA" editidir (taç): model tepeleri başka biçimde çizerse G0 atılmaz,
   ama G0'daki tepe profili kayda geçer — bedelin kanıtı G0 ↔ G6 çiftidir (SPEC §1).
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kırpma BAŞTAN [§2.7 ③]. Rejim hepsinde B.

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | ışık/huzme ✓/✗ | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|:---:|---|
| 0 | | B | G0 | G1 | geçti/düştü | | | | 8,0 | | — | |
| 1 | | B | G1 | G2 | | | | | 8,0 | | — | |
| 2 | | B | G2 | G3 | | | | | 8,0 | | — | |
| 3 | | B | G3 | G4 — ⚠️ klip ortasında rampa ÇAPRAZ göründü mü ✓/✗ | | | | | 8,0 | | — | |
| 4 | | B | G4 | G5 | | | | | 8,0 | | — | |
| 5 | | B | G5 | G6 (usta kare) | | | | | 8,0 | | huzme yok ✓/✗ | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6]

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____   (1080,1920,30/1,h264)
② SÜRE          ffprobe format=duration → ____ sn   (48,0 + 5,0 = 53,0)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 dikey_shorts/THE_DARK_ROCK/THE_DARK_ROCK_DIKEY_TIMELAPSE.md → çıkış: __
                beklenen kesmeler 8,0 · 16,0 · 24,0 · 32,0 · 40,0
                ("PLANIN KENDİSİ DÜZ" uyarısı beklenir — kabul edilmiş risk, çıkış kodunu değiştirmez)
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        müziksiz pencere 0,0–2,0 (dalga + martı) plana uygun mu: evet/hayır · 24,0–28,0 yalnız rüzgâr + deniz: __
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 47.0 -i teslim.mp4 -frames:v 1 kanit.jpg → SPEC §1 üçlüsü görünüyor mu: __
                KAPAK KAYNAĞI ffmpeg -ss 47.0 -i teslim.mp4 -frames:v 1 g6_kaynak.jpg
                KAPAK KANITI  bash araclar/zincir_kontrol.sh g6_kaynak.jpg kapak.png → __
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
```
