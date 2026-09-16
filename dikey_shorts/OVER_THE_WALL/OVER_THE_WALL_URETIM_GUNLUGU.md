# 🗒️ OVER THE WALL — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · bu günlüğe tek satır yazılmadı · (12.09.2026 plan yazıldı · 14.09.2026 ızgara 8 × 8,0'a çekildi)
        ⛔ 14.09.2026: FİLM BU GÜNLÜK TUTULMADAN ÜRETİLDİ ve 12 mercekle ölçüldü [DERS 28 · üçüncü kez].
           Kurgu 7 klip (7,8·8,0·10,7·10,0·8,0·13,0·6,0), hiçbir plan sürümüne oturmuyor; hangi araç, hangi
           prompt, zincir koşuldu mu — BİLİNMİYOR. Aşağıdaki tablolar o üretim için DOLDURULAMAZ (sonradan
           hatırlanarak yazılmaz). Sonuç: QA/RAPORLAR/OVER_THE_WALL.md · ham: QA/HAM_RAPORLAR/OVER_THE_WALL/
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`. Plan: `OVER_THE_WALL_DIKEY_TIMELAPSE.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 8 sahne = 9 kare (G0…G8) + 8 I2V [KILAVUZ_REHBERI §2.7].
> Izgara: ⛔ DÜZ 8 × 8,0 = 64,0 sn (proje sahibinin kilidi; ⑥ METRONOM beklenen risk — plan §AŞAMA MERDİVENİ).

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32 · A7-d]

> Yordam ve test promptu: `kilavuzlar/ARAC_KARTLARI.md` §4-§5. Kart doldurulmadan tek kare üretilmez.
> ⭐ Bu filmde ⑧ (iki kare) formatın kendisidir; almıyorsa araç değişir, plan düşürülmez.

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne: 8,0 (sekizi de)
   ⛔ tavan ≥ 8,0 (kutu ≥ 9,0) ise tek klip: üret <kutu>, baştan (kutu − 8,0) kırp [A7-b].
   ⛔ tavan < 8,0 ise ({4,6,8}) SEKİZ sahnenin sekizi iki zincirli klip (4,0 + 4,0, ara kare Gn′) —
      sekiz ara kare; plan §DEĞİŞMEZLER · ARAÇ KUTU SETİ satırı. Bu durumda ızgara kararı proje
      sahibine döner; karar buraya yazılır:
   KARAR         ____
② KAMERA        ilk/son kare kayması: ____ px    (>2 px ise ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5   (plan promptları 5.560–6.000 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 1. USTA KARE

```
KARE    G8 (son klibin HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    çıkış kemeri okunuyor mu (siyah, tacı %50) · köprü %36–42 · kret = yol sekisi (%81,7) ·
        üst 1/8 boş · çağlayan orta bölümde, omuzlar kuru → geçti/düştü
FİNAL HİYERARŞİ  ① çağlayan → ② siyah kemer → ③ köpükteki köprü — bu sırayla okunuyor mu [P1-h]
PİKSEL  köprü genişliği ____ px · kemer yüksekliği ____ px → plana ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G7 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = derivasyon ÇIKIŞ KEMERİ, elle ✓/✗ [DERS 25].
> ⛔ Sahne tavanı 8,0'ı taşımıyorsa her G(n) ile G(n+1) arasına Gn′ satırı açılır (G0′ … G7′).

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi (değilse ne) | zincir_kontrol | kemer elle | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|---|
| 7 | | G8 | çağlayan + köpük kaldırıldı · dudak kuru · yatak taş · 15:20 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 6 | | G7 | jet yarım eklendi · köprü altına su · tanker kaldırıldı · silindir + damper döşekte · 14:15 | | | | | |
| 5 | | G6 | kret + dudak kaldırıldı → 52 m, tepe ıslak · dozer döşeğe · jet orta · 13:10 | | | | | |
| 4 | | G5 | 45 m · gök kapalı, ıslak · yamaç ıslak yeşil · jet şişkin · sel köprüde · 12:10 | | | | | |
| 3 | | G4 | 8 m · gök açık · slush · kahve jet · 11:10 | | | | | |
| 2 | | G3 | duvar kaldırıldı · taban temiz kaya · dozer + silindir + kasası inik damper batı dayanağında · kar tabana kadar · 10:05 | | | | | |
| 1 | | G2 | seki kaldırıldı · yalnız ilk yara · yatak çakıl + birikinti · kar yalnız çentikte · 09:00 | | | | | |
| 0 | | G1 | jet kaldırıldı · kemerler kuru · nehir yatakta · sed ¾ · 08:00 | | | | | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o kare atılır, yeniden
   türetilir, satır yeniden yazılır [DERS 12 · 25].
⚠️ Zincir bu depoda ilk kez koşuluyor [AGENTS §6]. Kırılırsa sebep uygulama hatası OLMAYABİLİR
   (A3-a hata birikimi) — buraya not düşülür.
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kırpma BAŞTAN [§2.7 ③]. Rejim hepsinde B.

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|---|
| 0 | | B | G0 | G1 | geçti/düştü | | | | 8,0 | | |
| 1 | | B | G1 | G2 | | | | | 8,0 | | |
| 2 | | B | G2 | G3 | | | | | 8,0 | | |
| 3 | | B | G3 | G4 | | | | | 8,0 | | |
| 4 | | B | G4 | G5 | | | | | 8,0 | | |
| 5 | | B | G5 | G6 | | | | | 8,0 | | |
| 6 | | B | G6 | G7 | | | | | 8,0 | | |
| 7 | | B | G7 | G8 (usta kare) — ya da G7 → G7′ + G7′ → G8 | | | | | 8,0 | | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6]

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____   (1080,1920,30/1,h264)
② SÜRE          ffprobe format=duration → ____ sn   (64,0 + 5,0 = 69,0)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 dikey_shorts/OVER_THE_WALL/OVER_THE_WALL_DIKEY_TIMELAPSE.md → çıkış: __
                beklenen kesmeler 8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0 · 56,0
                ("PLANIN KENDİSİ DÜZ" uyarısı beklenir — kabul edilmiş risk, çıkış kodunu değiştirmez)
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        müziksiz pencere 0,0–2,0 (nehir sesi) plana uygun mu: evet/hayır
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 62.5 -i teslim.mp4 -frames:v 1 kanit.jpg → SPEC §1 üçlüsü görünüyor mu: __
                KAPAK KAYNAĞI ffmpeg -ss 62.5 -i teslim.mp4 -frames:v 1 g8_kaynak.jpg
                KAPAK KANITI  bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak.png → __
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
14.09.2026  hepsi  ızgara 10 × (3,0…9,0) = 60,0 → 8 × 8,0 = 64,0; KESER+AÇAR → AÇAR, BÜYÜR+DEVLEŞİR → BÜYÜR;
            160 → 120 BPM  ·  proje sahibinin kilidi  ·  plana yazıldı ✓ (üretim öncesi değişiklik, klip yok)
14.09.2026  hepsi  film günlüksüz üretildi ve QA'ya girdi — 7 klip, plan dışı ikinci istasyon (klip 5), S3 BÜYÜR
            klibi yok, makineler köprüde  ·  sebep bilinmiyor (günlük yok)  ·  plana YAZILMADI; dersler 51-54 kılavuza indi
```
