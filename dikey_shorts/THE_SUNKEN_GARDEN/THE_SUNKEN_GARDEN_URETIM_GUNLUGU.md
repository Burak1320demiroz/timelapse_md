# 🗒️ ÜRETİM GÜNLÜĞÜ — THE_SUNKEN_GARDEN

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md` · Kopyalandı: 2026-10-23

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki en uzun sahne: ____
② KAMERA        ilk/son kare kayması: ____ px
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
⑨ ÇÖZÜNÜRLÜK   ffprobe kaynak: ____ × ____ · YAKINLAŞMA TAVANI (genişlik / 1080) = ____×
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 1. USTA KARE

```
KARE    G7  (son klibin HEDEF karesi · sahne değil)
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    çapalar okunuyor mu · taç %'si · güvenli alan · yazı yok mu → geçti/düştü
FİNAL HİYERARŞİ  ateş çukuru (önce) · mavi saat ışığı · insanlar (arka) — sıra okunuyor mu
DOSYA   [kare dosya adı]
```

## 1b. ⛔ PİLOT ÜÇLÜ — FİNAL ÜRETİLEBİLİRLİK TESTİ

| parça | dosya | zincir_kontrol (önceki ↔ yeni · ana referans ↔ yeni) | 3 nirengi (px) | beş soru ✓ | sahip onayı (tarih) |
|---|---|---|---|:---:|---|
| (a) referans karesi G7 + 3 nirengi işaretli | | — | | — | |
| (b) ilk halka G7 → G6 | | geçti/düştü · geçti/düştü | | — | |
| (c) final I2V (G6 → G7) — ışıklar yanar, insanlar oturur | | geçti/düştü | | ✓/✗ | |
| (c′) en zor montaj hareketinin pilot klibi (S05 — krom dayanak sökümü + merdiven kaplaması) | | geçti/düştü | | ✓/✗ | |

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G6 → G0

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ | prompt birebir mi | zincir_kontrol | kanıt nesnesi elle | ara hâl elle | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|---|
| 6 | | | | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 5 | | | | | | | | |
| 4 | | | | | | | | |
| 3 | | | | | | | | |
| 2 | | | | | | | | |
| 1 | | | | | | | | |
| 0 | | | | | | | | |

## 3. VİDEO — I2V, klip başına TEK satır

| S | araç + ayar | rejim (A/B/C) | ilk kare G(n) | son kare G(n+1) | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son) | teslim süre | yüzey kanıtı | beş soru | baş/orta/son | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|:---:|:---:|---|
| 0 | | B | G0 | G1 | geçti/düştü | | | | | ✓/✗ | ✓/✗ | ✓✗✗ | |
| 1 | | A | G1 | G2 | | | | | | | | | |
| 2 | | A | G2 | G3 | | | | | | | | | |
| 3 | | A | G3 | G4 | | | | | | | | | |
| 4 | | A | G4 | G5 | | | | | | | | | |
| 5 | | A | G5 | G6 | | | | | | | | | |
| 6 | | B | G6 | G7 (usta kare) | | | | | | | | | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____
                 beklenen 1080,1920,30/1,h264
② SÜRE          ffprobe format=duration → ____ sn   (7 × 8,0 = 56,0 + kart)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 <plan> → çıkış: __
④ SES           ffmpeg -af ebur128=peak=true ...
                 I: ____ LUFS · Peak: ____ dBFS
                 ⛔ DİKEYDE MÜZİK YOK (sahip kuralı 21.09.2026)
⑤ AÇILIŞ        yalnız saha sesi (çekiç, çakıl, yaprak hışırtısı): evet/hayır
⑥ FLICKER       kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -sseof -0.05 → son_kare.jpg
                 SPEC §1: ateş çukuru · mavi saat · ip ışıklar · iki kişi görünüyor mu: __
                 KAPAK KAYNAĞI ffmpeg -ss ____ -i TESLİM.mp4 → s7_kaynak.jpg
                 KAPAK KANITI zincir_kontrol.sh s7_kaynak.jpg kapak.png → __
⑧ İHRAÇ         bash araclar/ihrac_kontrol.sh <film_klasoru> paylas_2x.mp4 --hiz 2 → __
```

## 5. PLANDAN SAPMALAR

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
```
