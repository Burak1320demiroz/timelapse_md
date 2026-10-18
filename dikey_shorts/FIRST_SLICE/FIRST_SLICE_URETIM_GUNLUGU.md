# 🗒️ FIRST SLICE — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · bu günlüğe tek satır yazılmadı · (17.10.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
⭐ PİLOT SIRASI (plan §PİLOT ÜÇLÜ): (a) G8 METİNDEN + kapak_prova METİNSİZ G8'e (onaydan ÖNCE) → (b) G8 → G7 →
        (c) S7 final (ilk dilim) + S0 açılış (lastik kafesi) + (c′) S3 fırın (S3·a + S3·b, 4 sn kutusu) — 7 görsel
        (G8 · G7 · G4 · G3a · G3 · G1 · G0), 4 klip; hepsi 2x'te izlenir
⭐ İHRAÇ — merceklerden ÖNCE ajan ölçer [DERS 100]: ffprobe (1080×1920) · ihrac_kontrol.sh (kart 5,0 sn) ·
        klip_eslestir.py <yayin.mp4> <S0 S1 S2a S2b S3a S3b S4 S5 S6 S7> --hiz 2 --kart 5 [DERS 86] · kapak_prova · kart ses kuyruğu
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`. Plan: `FIRST_SLICE_DIKEY_TIMELAPSE.md` · SPEC: `FIRST_SLICE_QA_SPEC.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 8 sahne = 9 kare (G0…G8) + ⭐ 2 ARA KARE (G2a · G3a) + 10 I2V (S2 · S3 ikişer 4 sn alt klip;
> araç 4 sn vermezse yedek 8 sn I2V → 8 klip) [KILAVUZ_REHBERI §2.7]. Izgara 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 17.10.2026 ·
> kural 7 × 8 · sahibin briefi 8), paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn.

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32 · A7-d]

> ⭐ 08.09.2026: üç soru SEKİZE çıktı. Yordam ve test promptu:
> `kilavuzlar/ARAC_KARTLARI.md` §4-§5. Kart doldurulmadan tek kare üretilmez.

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü — ⛔ araştırma raporundan alınmaz, A7-X2]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki en uzun sahne: ____
② KAMERA        ilk/son kare kayması: ____ px    (KAMERA_ISTASYONU §7 eşiğini aşıyorsa ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
                (almıyorsa ya da çıkış 2 ise BU FORMAT BU ARAÇTA ÜRETİLMEZ
                 — plan düşürülmez, araç değişir [KILAVUZ_REHBERI §2.7 ④])
⑨ ÇÖZÜNÜRLÜK   ffprobe kaynak: ____ × ____ · YAKINLAŞMA TAVANI (genişlik / 1080) = ____×
⭐ EK — 4 sn KUTUSU  araç 4,0 sn klip üretiyor mu: evet/hayır → hayırsa S2 · S3 yedek 8 sn I2V (plan) · G2a · G3a kontrol karesi
                ⭐ S0 geri çekilme açılışı planlandıysa BÜYÜTME ≤ tavan [KAMERA_HAREKETI §4.2]
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 1. USTA KARE

```
KARE    ⭐ G8 İLK üretilen kare (ilk dilim, ateş yanık, alacakaranlık · tasarım referansı + kapak kaynağı) — METİNDEN
        [§2.7 · DERS 85 · 91 · 99] · ⭐ ONAYDAN ÖNCE: kapak_prova.py METİNSİZ G8 → başlık kutusu (560–770) sakin mi ·
        fırın + ateş + pizza yapı kutusunda mı (800–1360) · pencereler mavi mi (gündüz değil)
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    çapalar okunuyor mu · taç %'si · güvenli alan · Dünya/yıldız yok mu → geçti/düştü
FİNAL HİYERARŞİ  [plandaki üç şey bu sırayla okunuyor mu — P1-h]
DOSYA   [kare dosya adı]
```


## 1b. ⛔ PİLOT ÜÇLÜ — FİNAL ÜRETİLEBİLİRLİK TESTİ [KILAVUZ_REHBERI §8 adım 2b · C1-b]

> Zincirin İLK halkası. Üçü onaylanmadan §2'nin kalanı üretilmez; (c) üretilemiyorsa
> kapsam daralır (sahne çıkar), prompt "düzeltilmez". Nirengi eşiği: KAMERA_ISTASYONU §7
> (`zincir_kontrol.sh` çıktısındaki px satırı).

| parça | dosya | zincir_kontrol (önceki ↔ yeni · ana referans ↔ yeni) | 3 nirengi (px) | beş soru ✓ | sahip onayı (tarih) |
|---|---|---|---|:---:|---|
| (a) referans karesi GN + 3 nirengi işaretli | | — | | — | |
| (b) ilk halka GN → G(N−1) | | geçti/düştü · geçti/düştü | | — | |
| (c) final I2V (G(N−1) → GN) — vaat edilen sonuç görünür | | geçti/düştü | | ✓/✗ | |
| (c′) en zor montaj hareketinin pilot klibi (hangi sahne: ____) | | geçti/düştü | | ✓/✗ | |

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G(N−1) → G0

> ⭐ Zincirli formatta N sahne = N+1 kare [KILAVUZ_REHBERI §2.7]. Usta kare
> (GN) §1'de kayıtlıdır; bu tablo ondan GERİYE inen kareleri tutar.

> ⭐ 05.10.2026 · DİKEY = 7 SAHNE [DERS 58] — bu filmde ⚠️ SAHİP İSTİSNASI 8 sahne: G8 §1'de; zincir G7 → G0 (G8'den geriye),
> ARA KARELER DAHİL (G3a · G2a — ⭐ elle: G3a'da kubbe YARIM, G2a'da zemin BETON).

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi (değilse ne) | zincir_kontrol | kanıt nesnesi elle | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|---|
| 7 | | G8 | | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 6 | | | | | | | | |
| 5 | | | | | | | | |
| 4 | | | | | | | | |
| 3a | | G4 | | | | | ⭐ kubbe YARIM | |
| 3 | | G3a | | | | | | |
| 2a | | G3 | | | | | ⭐ zemin BETON | |
| 2 | | G2a | | | | | | |
| 1 | | | | | | | | |
| 0 | | | | | | | | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o
   kare atılır, yeniden türetilir, satır yeniden yazılır. Düşen kareden
   türetilmiş bir alt kare bu tabloya giremez [DERS 12 · 25].
```

## 3. VİDEO — I2V, klip başına TEK satır

> ⭐ ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kutu setinden ÜST kutuyu
> iste, kurguda kırp. REJİM sütunu boş bırakılamaz [A6-a].

> ⛔ HER KLİP İKİ ONAYLI KAREYE KİLİTLİDİR: ilk kare G(n), son kare G(n+1).
> İki uç de I2V'de birebir cümleyle yazılır ve klip üretildikten SONRA
> son kare ↔ hedef görsel karşılaştırması koşulur [§2.7 · ARAC_KARTLARI ⑧].
>
> ⭐ **baş/orta/son** [C1-a]: klip üç noktada ELLE izlenir — başta malzeme kartın ① yerinde mi ·
> ortada taşıyıcıyla birlikte mi hareket ediyor (süzülmüyor, boyu değişmiyor) · sonda ④ farkı
> görünüyor mu. Üç ✓ olmayan klip, zincir_kontrol geçse bile yeniden üretilir.

| S | araç + ayar | rejim (A/B/C) | ilk kare G(n) | son kare G(n+1) | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | beş soru ✓/✗ | baş/orta/son | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|:---:|:---:|---|
| 0 | | B | G0 | G1 | geçti/düştü | | | 30/0 | | | ✓/✗ | ✓✗✗ | |
| 1 | | B | G1 | G2 | | | | | | | | | |
| 2·a | | B (1 sa · 4 sn) | G2 | G2a | | | | | | | | | |
| 2·b | | B (1 sa · 4 sn) | G2a | G3 | | | | | | | | | |
| 3·a | | B (1 sa · 4 sn) | G3 | G3a | | | | | | | | | |
| 3·b | | B (1 sa · 4 sn) | G3a | G4 | | | | | | | | | |
| 4 | | B | G4 | G5 | | | | | | | | | |
| 5 | | B | G5 | G6 | | | | | | | | | |
| 6 | | B | G6 | G7 | | | | | | | | | |
| 7 | | A (75×) | G7 | G8 (usta kare) | | | | | | | | | |
> ⛔ Yedek yolda (4 sn kutusu yok) 2·a+2·b → tek 2 (G2 → G3, 8 sn) · 3·a+3·b → tek 3 (G3 → G4, 8 sn).

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6]

> ⛔ Yedisi de koşmadan yayın yok. Boş satır = koşulmamış sayılır.

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____
                beklenen 1080,1920,30/1,h264 · tolerans SIFIR
② SÜRE          ffprobe format=duration → ____ sn   (1x master: 8 × 8,0 = 64,0 · yayın 2x: 32,0 + kart 5,0 = 37,0)
                ⭐ kartta ses: volumedetect 33–37 sn → ____ dB (dijital sessizlik −91 dB = DÜŞTÜ [DERS 100])
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 <plan>   → çıkış: __
                ⭐ betik top-N ile çalışır; AYIRIM marjı ____ kat çıktı
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary
                I: ____ LUFS (hedef −14 ±0,5) · Peak: ____ dBFS (≤ −1,0)
                müzik BPM ____
⑤ AÇILIŞ        ⛔ dikeyde MÜZİK YOK (sahip kuralı 21.09.2026) — yalnız saha sesi: evet/hayır
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF
                kesme dışında sıçrama var mı: evet/hayır
                ⛔ yalnız "-vf signalstats" HİÇBİR ŞEY BASMAZ [A8-b]
⑦ FİNAL + KAPAK ffmpeg -sseof -0.05 → son_kare.jpg
                SPEC §1'deki şeyler görünüyor mu: __
                KAPAK KAYNAĞI ffmpeg -ss ____ -i TESLİM.mp4 → s9_kaynak.jpg
                ⭐ kaynak TESLİM dosyasından alınır, üretilen klipten DEĞİL
                   (kırpma kareleri kaydırır) [KURGU_VE_TESLIM §2]
                KAPAK KANITI zincir_kontrol.sh s9_kaynak.jpg kapak.png → __
⑧ İHRAÇ         ⭐ 05.10.2026 [DERS 63] — PAYLAŞILACAK 2x dosyaya:
                bash araclar/ihrac_kontrol.sh <film_klasoru> paylas_2x.mp4 --hiz 2   → çıkış: __
                ① süre (32,0 + kart 5,0) __ · ② 1080×1920 __ · ③ final tutuşu SSIM __
                ④ müzik yok ✓/✗ · ⑤ okunur yazı/logo/"AI TIMELAPSE" yok ✓/✗ · ⑥ kart = GN dünyası ✓/✗/—
                QA paketi aynı dosyayla: bash araclar/qa_paket.sh --hiz 2 <film_klasoru> paylas_2x.mp4
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
```
