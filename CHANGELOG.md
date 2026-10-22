# CHANGELOG

Bu dosya [Keep a Changelog](https://keepachangelog.com/tr-TR/1.1.0/) biçimini ve
[Semantic Versioning](https://semver.org/lang/tr/) numaralamasını izler.

Sayılar sürümün tarihindeki `bash araclar/sayac.sh` çıktısından alındı. Güncel sayı için sayacı çalıştırın
(depo kuralı: _"sayı tek yerde durur"_).

---

## [Unreleased]

_Henüz kayıt yok._

---

## [2.0.0] — 2026-10-22 · Hat v2

Hat v2 iki şey getiriyor: her film iki kare zincirinde planlanıyor ve QA artık 5 mercekle yapılıyor.
2.0.0'dan önceki QA kayıtları donduruldu ve yalnız arşiv olarak tutuluyor ([`SECURITY.md`](SECURITY.md) · "Legacy Pipeline").

### Eklendi

- **Filmler:** 3 filmden **66 film klasörüne** çıkıldı (52 dikey · 14 yatay). Planı olan 66, QA SPEC'i olan
  65, üretim günlüğü olan 37 film var. Son eklenenler COLOSSUS, GAME ON ve THE TURNTABLE.
- **Yatay format klasörleri:** `yatay_2_dk_filmler/`, `yatay_4_dk_filmler/`, `yatay_6_dk_filmler/`,
  `yatay_8_dk_filmler/` ve `yatay_12_dk_filmler/`.
- **5 mercekli QA:**
  - `QA/Q1_GORUNTU`, `Q2_ZAMAN_KESME`, `Q3_SANTIYE`, `Q4_INSA` ve `Q5_TESLIM` mercekleri.
  - Ham raporlar `QA/HAM/` içinde, film raporları `QA/FILMLER/` içinde, puan tablosu `QA/TABLO.md` içinde.
  - 15 film için 75 rapor işlendi.
- **Araçlar:** 4 betikten 11 betiğe çıkıldı. Yeni betikler:
  - `qa_paket.sh` ve `kesme_kontrol.sh` (08.09)
  - `ihrac_kontrol.sh` (08.10)
  - `klip_eslestir.py`, `kapak_prova.py`, `capraz_sayim.py` ve `film_klasoru_ac.sh`
- **Kılavuzlar:** 10 dosyadan 36 dosyaya (≈17.700 satır) çıkıldı. Bunlardan biri `KAMERA_DILI_KILAVUZU`
  (istasyon öncesi sorular); Kuşak 10 ve 11 kılavuzları da bu sürümde eklendi.
- **Dersler:** DERS 1–22'den **DERS 106**'ya çıkıldı (`kilavuzlar/DERSLER.md`). Bu dersler
  `VARSAYIMLAR.md` ve `PLAN_OKUMALARI.md` içindeki kodlu varsayımlardan ve plan okumalarından ayrı tutuluyor.
- **Araştırma:** 35 araştırma promptu ve 49 işlenmiş ham rapor (`arastirma/`).
- **Topluluk belgeleri:**
  - [`LICENSE`](LICENSE)
  - [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md) ve [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
  - İki dilli README ve 1280×640 Open Graph önizleme görseli (`images/readme_social_preview.png`)

### Değişti

- **İki kare zinciri her filmin hattı oldu.** Her klip iki sabit kare (Gₙ → Gₙ₊₁) arasında I2V ile
  üretiliyor; metinden video (T2V) yedeği yok. Planda son kare (GN) önce üretiliyor, öncekiler ondan
  geriye doğru düzenlenerek çıkarılıyor. Zincir `zincir_kontrol.sh` ile denetleniyor.
- **Dikey format:** 7 sahne × 8,0 sn (56 sn, 2x paylaşım). Bundan sapmak için proje sahibinin istisna
  vermesi gerekiyor. Müzik yerine diegetik SES tablosu kullanılıyor ve her film GN karesinden üretilen
  bir kapak kartıyla bitiyor.
- **Prompt kapısı:** `prompt_kontrol.py` yeni kontroller aldı: geçici ekipman,
  ACTIVITY, MOTION FOCUS, asılı yük–taşıyıcı ve uzunluk kontrolleri. Kayma eşiği 2 px (sahip kararı, 19.09.2026).

### Kaldırıldı

- **12 mercekli QA sistemi** donduruldu ve `QA/ARSIV_12_MERCEK/` altına taşındı: 393 ham rapor,
  37 film ve 31 film raporu. Bu arşiv salt okunur.
- Kullanılmayan dosyalar silindi: `prompt_kontrol.pyc`, `ig.html` ve `plan_updates.txt`.

---

## [1.0.0] — 2026-08-31 · İlk sürüm

İlk commit: `timelapse_md` kılavuzlar, QA sistemi ve üç ölçülmüş filmle açıldı.

### Eklendi

- **Ajan kontratı:** `AGENTS.md` ve `CLAUDE.md`.
- **Kılavuzlar** (10 dosya):
  - `KILAVUZ_REHBERI` ve `TIMELAPSE_SISTEM_PROMPTU`
  - `PROMPT_SABLONU` ve `KAMERA_ISTASYONU_KILAVUZU`
  - `ZAMAN_VE_ISIK_KILAVUZU`, `SAHA_VE_IKLIM_KARTLARI` ve `YAPI_TIPI_KARTLARI`
  - `MUZIK_VE_KAPAK` ve `BES_SAHNE_GPT_BRIEFI`
  - `DERSLER` (DERS 1–22)
- **QA:** 6 mercekli ilk sistem (`T1_KARE` … `T6_GECIS`), ham rapor ve film raporu klasörleri.
- **Araçlar:** `prompt_kontrol.py`, `zincir_kontrol.sh`, `sayac.sh` ve `kare_al.sh`.
- **Filmler** (dikey): THE CLOSING SPAN, THE LONG SHADOW ve THE NARROW LOT.
- **Yayın belgeleri:** `apexait/` altında kanal kimliği, yayın planı ve çapraz yayın; YouTube, TikTok ve
  Instagram klasörleri.
- **Araştırma:** `arastirma/` başlangıç promptları (A1 viral anatomi …).

[Unreleased]: ../../compare/v2.0.0...HEAD
[2.0.0]: ../../compare/v1.0.0...v2.0.0
[1.0.0]: ../../tree/v1.0.0
