# 🗒️ THE EMPTY RIDGE — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · bu günlüğe tek satır yazılmadı · (14.09.2026 plan yazıldı)
        ⛔ 14.09.2026: FİLM BU GÜNLÜK TUTULMADAN ÜRETİLDİ ve 12 mercekle ölçüldü [DERS 28 · dördüncü kez].
           Kurgu 8 klip varyanslı (4,9·3,6·6,3·7,0·10,0·8,1·7,9·8,0), plana oturmuyor; ① dört istasyon grubu +
           push-in. Hangi araç, hangi prompt, zincir koşuldu mu — BİLİNMİYOR. Tablolar o üretim için
           DOLDURULAMAZ. Sonuç: QA/ARSIV_12_MERCEK/RAPORLAR/THE_EMPTY_RIDGE.md · ham: QA/ARSIV_12_MERCEK/HAM_RAPORLAR/THE_EMPTY_RIDGE/
           Yeniden üretimden ÖNCE plana üç düzeltme girer (DERS 55 · 56 · 57 — RAPORLAR §9).
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28 — üç filmde ölçüldü]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`. Plan: `THE_EMPTY_RIDGE_DIKEY_TIMELAPSE.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 7 sahne = 8 kare (G0…G7) + 7 I2V [KILAVUZ_REHBERI §2.7].
> Izgara: ⛔ DÜZ 7 × 8,0 = 56,0 sn (proje sahibinin kilidi; ⑥ METRONOM beklenen risk — plan §AŞAMA MERDİVENİ).

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32 · A7-d]

> Yordam ve test promptu: `kilavuzlar/ARAC_KARTLARI.md` §4-§5. Kart doldurulmadan tek kare üretilmez.
> ⭐ Bu filmde ⑧ (iki kare) formatın kendisidir; almıyorsa araç değişir, plan düşürülmez.

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne: 8,0 (yedisi de)
   ⛔ tavan ≥ 8,0 (kutu ≥ 9,0) ise tek klip: üret <kutu>, baştan (kutu − 8,0) kırp [A7-b].
   ⛔ tavan < 8,0 ise ({4,6,8}) YEDİ sahnenin yedisi iki zincirli klip (4,0 + 4,0, ara kare Gn′) —
      yedi ara kare; plan §DEĞİŞMEZLER · ARAÇ KUTU SETİ satırı. Bu durumda ızgara kararı proje
      sahibine döner; karar buraya yazılır:
   KARAR         ____
② KAMERA        ilk/son kare kayması: ____ px    (>2 px ise ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5   (plan promptları 5.740–5.980 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
⑨ VİNÇ TESTİ    (bu filme özel, ölçülmemiş) test klibinde kafes bom + kısa sapanlı yük DAĞA karşı: yük yolu
                koptu mu / bom eridi mi: __   — kopuyorsa DERS 22 bu araçta da geçerlidir, plan yeniden açılır
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 0b. ÖN GÖRSELLEŞTİRME — usta kareden ÖNCE [plan §DEĞİŞMEZLER · KAMERA]

```
YAN KESİT       kamera (+100 m · 320 m) · spur · kule (100 m) · bom (120 m · ~82°) · uzak sıradağ (≥ +6°)
ÇİZİLDİ Mİ      evet/hayır · dosya: ____
YÜK YOLU        segment 1–4 → arka plan: ____ (dağ/gök) · nasel+göbek → ____ · yatay kanat → ____ · dik kanat ucu → gök (kabul)
SAHA ŞARTI      sıradağ silueti kameradan ____° (≥ +6° gerekli) → ✓/✗ — ✗ ise istasyon yeniden seçilir, prompt değil
```

## 1. USTA KARE

```
KARE    G7 (son klibin HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    göbek göz çizgisinde (%50) · kanat ucu %65 · bom/vinç YOK · pad boş (palet izi + takoz) · meşe x ≈ 742,
        64 px · sıradağ %57 · üst 1/8 boş · rotor dönüyor (uç izi) → geçti/düştü
FİNAL HİYERARŞİ  ① dönen rotor → ② boş pad + yol izi → ③ aynı meşe — bu sırayla okunuyor mu [P1-h]
PİKSEL  meşe boy ____ px · taç ____ px · x ____ · duvar ____ px · silüet y ____ → plana ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G6 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = MEŞE + DUVAR (boy dâhil), elle ✓/✗ [DERS 25].
> ⛔ Sahne tavanı 8,0'ı taşımıyorsa her G(n) ile G(n+1) arasına Gn′ satırı açılır (G0′ … G6′). S4 ve S5 için
> ara kare kutudan bağımsız da açılabilir; karar buraya yazılır.

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi (değilse ne) | zincir_kontrol | meşe+duvar elle | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|---|
| 6 | | G7 | rotor durdurulur (Y) · vinç GERİ (bom dik, kanca pad'de) · yardımcı vinç · boş raflar · tarla çıplak anız · 18:00 | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 5 | | G6 | üç kanat kaldırılır → çıplak göbek · kanatlar raflara (3) · kanat aparatı · 16:00 | | | | | |
| 4 | | G5 | nasel+göbek kaldırılır → çıplak flanş · nasel çerçeveye · tulum YATAY · meşe savrulur · balyalar · 14:00 | | | | | |
| 3 | | G4 | segment 2-3-4 kaldırılır → segment 1 · 3 segment pad'e · nasel + kanatlar kaldırılır · biçerdöver · 12:00 | | | | | |
| 2 | | G3 | segment 1 kaldırılır → açık temel · bom YATIRILIR, parçalar sırada · 4 segment treylere · altın buğday · 10:00 | | | | | |
| 1 | | G2 | temel kaldırılır → çukur + pasa · pad kaldırılır → ot · parçalar/treylerler kaldırılır · ekskavatör · 08:00 | | | | | |
| 0 | | G1 | yol kaldırılır (ilk metreler hariç) · çukur → ot + koyun yolu · tulum kaldırılır · dozer + greyder sol altta · 06:00 | | | | | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o kare atılır, yeniden
   türetilir, satır yeniden yazılır [DERS 12 · 25].
⚠️ Zincir bu depoda ilk kez koşuluyor [AGENTS §6]. Kırılırsa sebep uygulama hatası OLMAYABİLİR
   (A3-a hata birikimi) — buraya not düşülür.
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kırpma BAŞTAN [§2.7 ③]. Rejim hepsinde B.

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | vinç yük yolu ✓/✗ | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|:---:|---|
| 0 | | B | G0 | G1 | geçti/düştü | | | | 8,0 | | — | |
| 1 | | B | G1 | G2 | | | | | 8,0 | | | |
| 2 | | B | G2 | G3 | | | | | 8,0 | | | |
| 3 | | B | G3 | G4 | | | | | 8,0 | | | |
| 4 | | B | G4 | G5 — ya da G4 → G4′ + G4′ → G5 | | | | | 8,0 | | | |
| 5 | | B | G5 | G6 — ya da G5 → G5′ + G5′ → G6 | | | | | 8,0 | | | |
| 6 | | B | G6 | G7 (usta kare) — ya da G6 → G6′ + G6′ → G7 | | | | | 8,0 | | | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6]

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____   (1080,1920,30/1,h264)
② SÜRE          ffprobe format=duration → ____ sn   (56,0 + 5,0 = 61,0)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 dikey_shorts/THE_EMPTY_RIDGE/THE_EMPTY_RIDGE_DIKEY_TIMELAPSE.md → çıkış: __
                beklenen kesmeler 8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0
                ("PLANIN KENDİSİ DÜZ" uyarısı beklenir — kabul edilmiş risk, çıkış kodunu değiştirmez)
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        müziksiz pencere 0,0–2,0 (rüzgâr + tarla kuşu) plana uygun mu: evet/hayır · 32,0–36,0 yalnız rüzgâr: __
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 54.5 -i teslim.mp4 -frames:v 1 kanit.jpg → SPEC §1 üçlüsü görünüyor mu: __
                KAPAK KAYNAĞI ffmpeg -ss 54.5 -i teslim.mp4 -frames:v 1 g7_kaynak.jpg
                KAPAK KANITI  bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png → __
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
14.09.2026  hepsi  film günlüksüz üretildi ve QA'ya girdi — 8 klip, dört istasyon, push-in, S2–S4 tek klipte,
            rüzgâr bekleyişi yok, rotor montajda döndü, 0:21 / 0:39 hayalet kuleler · sebep bilinmiyor (günlük yok)
            · plana YAZILMADI; dersler 55-57 kılavuza indi, plan düzeltmesi yeniden üretimden önce
```
