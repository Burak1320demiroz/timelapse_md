# 🗒️ THE_SKY_CANAL — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · bu günlüğe tek satır yazılmadı · (11.10.2026 klasör açıldı · TUR 1)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28 — dört filmde dört kez tutulmadı]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `kilavuzlar/FILM_KLASOR_SABLONU/FILM_URETIM_GUNLUGU.md` (dikey karşılığı `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`).
> Plan: `THE_SKY_CANAL_PLAN.md` · promptlar `THE_SKY_CANAL_BOLUM_1.md` · `_BOLUM_2.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 20 sahne = 21 kare (G0…G20) + 20 I2V [KILAVUZ_REHBERI §2.7] · tek istasyon (MAIN, %100).
> Kart YOK · müzik VAR (altta, sözsüz, 120 BPM) · 160,0 sn · rejim A × 14 · B × 3 · Y × 3 (tekne, ≈1 dk/klip — YENİ).
> Izgara: ⛔ DÜZ 20 × 8,0 = 160,0 sn (sahip senaryosu, hikâye SAPMA ②; ⑥ METRONOM beklenen risk — PLAN §AŞAMA MERDİVENİ).
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
   ⛔ tavan < 8,0 ise 20 sahnenin hepsi iki zincirli klip (ara kare Gn′) — ızgara kararı
      proje sahibine döner; karar buraya yazılır:
   KARAR         ____
② KAMERA        ilk/son kare kayması: ____ px    (KAMERA_ISTASYONU §7 eşiğini aşıyorsa ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5   (plan promptları 5700–6000 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
⑨ 16:9          araç 1920×1080 (ya da 16:9 4K) veriyor mu: __ · kırpma/letterbox yok: __
⑩ REJİM Y       ⭐ bu filme özel: "About one minute passes" klibinde tekne düz, sabit hızda gidiyor mu · insan iz değil,
                küçük figür mü · gölge sabit mi: __/__/__ (PİLOT ① ile birlikte)
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 1. USTA KARE

```
KARE    G20 (son klibin HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir BOLUM_2 §USTA KARE'den / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    final hiyerarşisi ① tekne ② dolu oluk + kalkık kapaklar ③ köprü ④ nehir ⑤ çam bu sırayla okunuyor mu ·
        kanıt nesnesi x 1475–1547 / 72 px · geçici ekipman YOK · ufuk %86 · oluğun içi bant olarak görünüyor mu ·
        su vadiye akmıyor · tek tekne → geçti/düştü
PİKSEL  kanıt nesnesi __ px · tekne __–__ px · ayaklar __ / __ px → PLAN ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 1b. ⛔ PİLOT ÜÇLÜ — FİNAL ÜRETİLEBİLİRLİK TESTİ [KILAVUZ_REHBERI §8 adım 2b · C1-b]

> Zincirin İLK halkası. Üçü onaylanmadan §2'nin kalanı üretilmez; (c) üretilemiyorsa
> kapsam daralır (sahne çıkar), prompt "düzeltilmez". Nirengi eşiği: KAMERA_ISTASYONU §7
> (`zincir_kontrol.sh` çıktısındaki px satırı).

| parça | dosya | zincir_kontrol (önceki ↔ yeni · ana referans ↔ yeni) | 3 nirengi (px) | beş soru ✓ | sahip onayı (tarih) |
|---|---|---|---|:---:|---|
| (a) referans karesi G20 + 3 nirengi işaretli (çam tepesi · sol ayak tepesi · sağ kapak çerçevesi) | | — | | — | |
| (b) ilk halka G20 → G19 → G18 | | geçti/düştü · geçti/düştü | | — | |
| (c) final I2V S18 (G18 → G19, tekne merkez açıklıkta) + S19 tutuşu — rejim Y ilk kez | | geçti/düştü | | ✓/✗ | |
| (c′) en büyük değişikliğin pilot klibi S2 (G2 → G3 — merkez parça dimdik yukarı · PLAN PİLOT ②) | | geçti/düştü | | ✓/✗ | |
| (c″) su pilotu S13 (G13 → G14 — kuru oluğa ilk sığ su · PLAN PİLOT ③) | | geçti/düştü | | ✓/✗ | |
| (d) pilot sonrası ilk: S0 (açılış) + S14 + S15 (tek dolumun devamı) | | geçti/düştü | | ✓/✗ | |

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G19 → G18 → … → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = ÇAM (x 1475–1547 · tepe 622 · 72 px), elle ✓/✗ [DERS 25].
> ⛔ Sahne tavanı 8,0'ı taşımıyorsa her G(n) ile G(n+1) arasına Gn′ satırı açılır.
> ⭐ G10 bölüm sınırı karesidir: BOLUM_2'nin ilk görseli, BOLUM_1'in son I2V hedefi — tek kare, tek satır.
> ⚠️ G16 → G13 adımlarında SU ÇEKİLİR: oluk her adımda kuru ve mat çizilir, ıslak iz bırakılmaz [DERS 54]. G13 → G12
> adımında iki vinç, kamyonlar ve palet istifleri GERİ GELİR. G3 → G2 → G1 → G0 adımlarında parçalar KALKAR: merkez parça
> vadi tabanındaki kalaslara, sağ parça sağ pede döner, sol parça sol açıklığın bir metre üstüne asılır — iki kopya
> çizilmez, px (PLAN §KADRAJ) her adımda elle ölçülür. Tekne G17 → G16 adımında yine havuzda bağlıdır.

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi (değilse ne) | zincir_kontrol | kanıt nesnesi elle | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|---|
| 19 | | G20 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 18 | | G19 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 17 | | G18 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 16 | | G17 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ kapaklar KAPALI, su dörtte üç |
| 15 | | G16 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 14 | | G15 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 13 | | G14 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ oluk KURU, mat (ters zincirde su çekilir — ıslak iz yok) |
| 12 | | G13 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 11 | | G12 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 10 | | G11 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ bölüm sınırı karesi |
| 9 | | G10 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 8 | | G9 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 7 | | G8 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 6 | | G7 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 5 | | G6 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 4 | | G5 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 3 | | G4 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ üç açıklık birleşik |
| 2 | | G3 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ merkez parça kalasta |
| 1 | | G2 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 0 | | G1 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ sol parça ASILI |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o kare atılır, yeniden
   türetilir, satır yeniden yazılır [DERS 12 · 25]. Düşen kareden türetilmiş alt kare tabloya giremez.
⚠️ 20 karelik zincirde hata birikimi (A3-a) beklenir: her ~10 karede G(n) ↔ G20 yan yana konur
   (3 nirengi px · KAMERA_ISTASYONU §7) — kayma eşiği aşıyorsa zincir usta kareden yeniden alınır;
   ⭐ her koşuda üçüncü argüman GN verilir: zincir_kontrol.sh <onceki> <yeni> <GN>.
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kırpma BAŞTAN [§2.7 ③]. REJİM sütunu boş bırakılamaz [A6-a].
> ⛔ HER KLİP İKİ ONAYLI KAREYE KİLİTLİDİR: ilk kare G(n), son kare G(n+1); klip üretildikten SONRA
> son kare ↔ hedef görsel zincir_kontrol koşulur [§2.7 · ARAC_KARTLARI ⑧].
>
> ⭐ **baş/orta/son** [C1-a]: klip üç noktada ELLE izlenir — başta malzeme kartın ① yerinde mi ·
> ortada taşıyıcıyla birlikte mi hareket ediyor (süzülmüyor, boyu değişmiyor) · sonda ④ farkı
> görünüyor mu. Üç ✓ olmayan klip, zincir_kontrol geçse bile yeniden üretilir.
> 💧 S13–S15: su cephesi baş/orta/son'da nerede (x px) — geri çekiliyor ya da sıçrıyorsa klip düşer.
> 🛶 S17–S19: tekne baş/orta/son'da nerede (x px) — hız sabit mi, dönüyor mu, ikinci tekne var mı.

| S | araç + ayar | rejim | İSTASYON | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | beş soru ✓/✗ | baş/orta/son | dosya |
|:-:|---|:-:|:-:|---|---|:---:|---|---:|---|---:|:---:|:---:|:---:|---|
| 0 | | A | ANA | G0 | G1 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 1 | | A | ANA | G1 | G2 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 2 | | A | ANA | G2 | G3 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 3 | | B | ANA | G3 | G4 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 4 | | A | ANA | G4 | G5 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 5 | | A | ANA | G5 | G6 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 6 | | A | ANA | G6 | G7 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 7 | | A | ANA | G7 | G8 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 8 | | B | ANA | G8 | G9 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 9 | | A | ANA | G9 | G10 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 10 | | A | ANA | G10 | G11 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 11 | | B | ANA | G11 | G12 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 12 | | A | ANA | G12 | G13 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 13 | | A | ANA | G13 | G14 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 14 | | A | ANA | G14 | G15 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 15 | | A | ANA | G15 | G16 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 16 | | A | ANA | G16 | G17 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 17 | | Y | ANA | G17 | G18 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 18 | | Y | ANA | G18 | G19 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 19 | | Y | ANA | G19 | G20 (usta kare) | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6] — TAM master

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____   (1920,1080,30/1,h264 · tolerans SIFIR)
② SÜRE          ffprobe format=duration → ____ sn   (160,0 · kart YOK)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_SKY_CANAL/THE_SKY_CANAL_PLAN.md → çıkış: __
                beklenen kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn)
                ("PLANIN KENDİSİ DÜZ" uyarısı beklenir — kabul edilmiş risk, çıkış kodunu değiştirmez)
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary → I: ____ LUFS · Peak: ____ dBFS · müzik VAR (altta)
⑤ AÇILIŞ        ses tablosu (MUZIK.md) plana uygun mu — 0–1,5 sn müziksiz, vinç motoru + nehir: evet/hayır
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss ____ -i teslim.mp4 -frames:v 1 kanit.jpg → SPEC §1 beşlisi görünüyor mu: __ (-ss 159.0)
                KAPAK KAYNAĞI ffmpeg -ss ____ -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                KAPAK KANITI  bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png → __
BÖLÜM SINIRI    ffmpeg -ss 80.0 -i teslim.mp4 -frames:v 1 sinir.jpg → SPEC §7 ile aynı mı: __ (G10)
TEK DOLUM       ffmpeg -ss 111.9 / 112.0 ve 119.9 / 120.0 → su cephesi ve seviye iki yakada aynı mı: __
TEK GEÇİŞ       ffmpeg -ss 143.9 / 144.0 ve 151.9 / 152.0 → tekne iki yakada aynı yerde mi: __
```

### 4b. QA MASTERLARI (yalnız 6/8 dk · QA birimi BÖLÜM)

```
— uygulanmaz: 2 dk hattında QA birimi FİLM (tek master × 5 mercek)
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
⬜ MÜZİK: kaynak · lisans · BPM ölçüldü mü (120)
⬜ SES EFEKTİ kütüphanesi (kullanılırsa): kaynak · lisans
⬜ REJİM Y ölçümü (PİLOT ①): tekne hızı px/sn · insan görünümü · gölge — DERS adayı mı
```
