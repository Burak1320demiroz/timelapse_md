# 🗒️ THE_LAST_CARRIAGE — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · bu günlüğe tek satır yazılmadı · (12.10.2026 klasör açıldı · TUR 1)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28 — dört filmde dört kez tutulmadı]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `kilavuzlar/FILM_KLASOR_SABLONU/FILM_URETIM_GUNLUGU.md` (dikey karşılığı `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`).
> Plan: `THE_LAST_CARRIAGE_PLAN.md` · promptlar `THE_LAST_CARRIAGE_BOLUM_1.md` · `_BOLUM_2.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 20 sahne = 21 kare (G0…G20; G14 iç) + iç son kare G14′ + 20 I2V [KILAVUZ_REHBERI §2.7 · ISTASYON §2] ·
> iki istasyon (MAIN 19 klip · CARRIAGE yalnız S14, S13 ile paralel zaman).
> Kart YOK · müzik VAR (0–24 sn yok, sonra büyür, S11 hafifler, S18–S19 ana tema) · 160,0 sn · rejim A × 14 (+1 iç) · B × 3 · G × 2.
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
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5   (plan promptları 5368–5993 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
⑨ İKİ İSTASYON  ⭐ bu filme özel: ana (337°) ve iç (90°) kamerada tilt 14° AYNI tutuluyor mu — uzak sırtlar iki karede de
                üstten ≈168 px: ana __ px · iç __ px · fark ≤ 20 px mı: __ · iç karede pencereden yarık kaya ana karedekiyle aynı
                ton ve çatlak mı: __ (ELLE — kompozit yok, yönler farklı) · 16:9 · kırpma/letterbox yok: __
⑩ REJİM G       ⭐ bu filme özel: "moves at natural speed … Eight seconds pass" klibinde konuklar iz bırakmadan, küçük ve yüzsüz
                mi · çift camın üstüne normal adımla mı geliyor (koşma, sarkma yok) · gök ve çam dalları gerçek hızda mı:
                __/__/__ (PİLOT ① ile)
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 1. USTA KARE

```
KARE    G20 (son klibin HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir BOLUM_2 §USTA KARE'den / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    final hiyerarşisi ① ışıklı sekiz pencere + zümrüt gövde + bakır çatı ② cam orta bölüm + çift ③ dış masalarda konuklar
        + korkuluk ışığı ④ iki geçit + tabliye + kanyon gölgesi + mavi gök ⑤ yarık kaya + çatallı çam bu sırayla okunuyor mu ·
        kanıt nesnesi x 1649–1806 / 157 px · TEK vagon, SEKİZ pencere, İKİ vestibül · tekerlek/ray YOK · geçici ekipman YOK
        (bir minibüs hariç) · sırtlar %84 · gök mavi ve okunur (siyah değil) · cam: kenar + yansıma + altında kanyon (ayna ya
        da delik değil) · havai fişek/hale/sis yok → geçti/düştü
PİKSEL  kanıt nesnesi __ px · vagon __–__ px · cam bölüm __–__ px · teras ön kenarı __ → __ px → PLAN ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 1b. ⛔ PİLOT ÜÇLÜ — FİNAL ÜRETİLEBİLİRLİK TESTİ [KILAVUZ_REHBERI §8 adım 2b · C1-b]

> Zincirin İLK halkası. Üçü onaylanmadan §2'nin kalanı üretilmez; (c) üretilemiyorsa
> kapsam daralır (sahne çıkar), prompt "düzeltilmez". Nirengi eşiği: KAMERA_ISTASYONU §7
> (`zincir_kontrol.sh` çıktısındaki px satırı).

| parça | dosya | zincir_kontrol (önceki ↔ yeni · ana referans ↔ yeni) | 3 nirengi (px) | beş soru ✓ | sahip onayı (tarih) |
|---|---|---|---|:---:|---|
| (a) referans karesi G20 + 3 nirengi işaretli (yarık kayanın tepesi · vagonun sol çatı köşesi · sol kiriş mesnedi) | | — | | — | |
| (b) ilk halka G20 → G19 → G18 | | geçti/düştü · geçti/düştü | | — | |
| (c) final I2V S18 (G18 → G19, konuklar terasa) + S19 (çift camda + tutuş) — rejim G ilk kez | | geçti/düştü | | ✓/✗ | |
| (c′) en büyük değişikliğin pilot klibi S0 (G0 → G1 — asılı vagon yalnız son metreyi iner, kopyalanmaz, sallanmaz · DERS 57 · PLAN PİLOT ②) | | geçti/düştü | | ✓/✗ | |
| (c″) cam pilotu S11 (G11 → G12 — üç cam panel, kenar + yansıma, altında kanyon · PLAN PİLOT ③) | | geçti/düştü | | ✓/✗ | |
| (d) pilot sonrası ilk: S3 · S4 (pas → gri → yeşil, B) + S14 (iç istasyon, G14′ → G14) + S16 (üç ışık grubu) | | geçti/düştü | | ✓/✗ | |

## 2. GERİYE ZİNCİR — KARE başına TEK satır, sıra: G19 → G18 → … → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = YARIK KAYA (x 1649–1806 · tepe 405 · 157 px), elle ✓/✗ [DERS 25].
> ⛔ Sahne tavanı 8,0'ı taşımıyorsa her G(n) ile G(n+1) arasına Gn′ satırı açılır.
> ⭐ G10 bölüm sınırı karesidir: BOLUM_2'nin ilk görseli, BOLUM_1'in son I2V hedefi — tek kare, tek satır.
> 🪟 G14 ve G14′ İÇ ZİNCİRDİR (aşağıda ayrı tablo): ana zincirde G15'ten sonra G13 gelir; ana kare ile iç kare zincir_kontrol'e
> VERİLMEZ [ISTASYON §2].
> ⚠️ G19 → G17 adımlarında KONUKLAR AZALIR: oturanlar yer değiştirmeden seyrelir. G17 → G16 adımında lambalar SÖNER (ters
> zincirde), G16 → G15'te vinç, telehandler, kamyonlar GERİ GELİR. G1 → G0 adımında vagon tabliyenin 1 m ÜSTÜNE kalkar: boyu, pencere
> sayısı ve yeri aynı kalır, alt şasinin ortası üstten 642 (PLAN §KADRAJ) — elle ölçülür.

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi (değilse ne) | zincir_kontrol | kanıt nesnesi elle | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|---|
| 19 | | G20 | | | geçti/düştü | ✓/✗ | ✓/✗ |  |
| 18 | | G19 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ çift camda değil · üç dış masa dolu |
| 17 | | G18 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ dış masalar boş |
| 16 | | G17 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ içerisi BOŞ, lambalar yanık |
| 15 | | G16 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ lambalar SÖNÜK · vinç, telehandler, kamyonlar geri |
| 13 | | G15 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ dış masalar yok (G14 iç — ayrı tablo) |
| 12 | | G13 | | | geçti/düştü | ✓/✗ | ✓/✗ | korkuluk yok |
| 11 | | G12 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ cam yok, orta AÇIK · sehpada iki panel |
| 10 | | G11 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ bölüm sınırı karesi — ahşap yok, açık iskelet |
| 9 | | G10 | | | geçti/düştü | ✓/✗ | ✓/✗ | iskelet yok, dirsekler |
| 8 | | G9 | | | geçti/düştü | ✓/✗ | ✓/✗ | sağ geçit yok |
| 7 | | G8 | | | geçti/düştü | ✓/✗ | ✓/✗ | sol geçit yok |
| 6 | | G7 | | | geçti/düştü | ✓/✗ | ✓/✗ | camlar yok, açıklıklar boş |
| 5 | | G6 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ çatı gri |
| 4 | | G5 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ gövde gri, krem yok |
| 3 | | G4 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ pas |
| 2 | | G3 | | | geçti/düştü | ✓/✗ | ✓/✗ | eski camlar yerinde |
| 1 | | G2 | | | geçti/düştü | ✓/✗ | ✓/✗ | sapanlar bağlı, kiriş kancada |
| 0 | | G1 | | | geçti/düştü | ✓/✗ | ✓/✗ | ⭐ vagon 1 m yukarıda asılı |

### 🪟 İÇ ZİNCİR — CARRIAGE STATION (G14′ önce, G14 ondan)

| G | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ | prompt birebir mi | zincir_kontrol (yalnız iç ↔ iç) | pencerede kaya elle | sırtlar ≈168 px | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|---|
| 14′ | | (yeni — ana G15'in saati ve ışığıyla) | | | — | ✓/✗ | ✓/✗ | ⭐ dolu salon, lambalar sönük |
| 14 | | G14′ | masa + bank + sarkıt lamba geri alındı, kapıda istif | | geçti/düştü | ✓/✗ | ✓/✗ | boş salon |

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
> 🏗️ S0: vagonun alt şasisi baş/orta/son'da üstten kaç px (642 → 685) — sallanıyor, kopyalanıyor ya da sapan kopuyorsa klip düşer.
> 🔍 S11: cam paneller kenar + yansımayla mı okunuyor, açıklık boya gibi mi kapanıyor — kanyon altta görünüyor mu.
> 👥 S17–S19: oturan sayısı baş/orta/son — kimse koltukta belirmiyor, oturan kaybolmuyor; cam S19'a kadar boş.
> 🏮 S16: üç grup hangi saniyede yanıyor — sıra iç → geçitler → korkuluk mu, her biri tek karede mi.

| S | araç + ayar | rejim | İSTASYON | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | beş soru ✓/✗ | baş/orta/son | dosya |
|:-:|---|:-:|:-:|---|---|:---:|---|---:|---|---:|:---:|:---:|:---:|---|
| 0 | | A | ANA | G0 | G1 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 1 | | A | ANA | G1 | G2 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 2 | | A | ANA | G2 | G3 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 3 | | B | ANA | G3 | G4 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 4 | | B | ANA | G4 | G5 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 5 | | A | ANA | G5 | G6 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 6 | | A | ANA | G6 | G7 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 7 | | A | ANA | G7 | G8 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 8 | | A | ANA | G8 | G9 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 9 | | A | ANA | G9 | G10 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 10 | | B | ANA | G10 | G11 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 11 | | A | ANA | G11 | G12 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 12 | | A | ANA | G12 | G13 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 13 | | A | ANA | G13 | G15 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 14 | | A | İÇ 🪟 | G14 | G14′ | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 15 | | A | ANA | G15 | G16 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 16 | | A | ANA | G16 | G17 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 17 | | A | ANA | G17 | G18 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 18 | | G | ANA | G18 | G19 | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |
| 19 | | G | ANA | G19 | G20 (usta kare) | geçti/düştü | | | 30/0 | 8,0 | | ✓/✗ | ✓✗✗ | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6] — TAM master

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____   (1920,1080,30/1,h264 · tolerans SIFIR)
② SÜRE          ffprobe format=duration → ____ sn   (160,0 · kart YOK)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_LAST_CARRIAGE/THE_LAST_CARRIAGE_PLAN.md → çıkış: __
                beklenen kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn)
                ("PLANIN KENDİSİ DÜZ" uyarısı beklenir — kabul edilmiş risk, çıkış kodunu değiştirmez)
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary → I: ____ LUFS · Peak: ____ dBFS · müzik VAR (24 sn'den)
⑤ AÇILIŞ        ses tablosu (MUZIK.md) plana uygun mu — 0–24 sn müziksiz, ilk karede rüzgâr + vinç: evet/hayır · açılış yazısı YOK: evet/hayır
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF → kesme dışında sıçrama: evet/hayır (S16 ışık grupları
                BEKLENEN üç sıçramadır — saniyeleri IŞIK DEFTERİ ile karşılaştır · 112,0 ve 120,0 istasyon kesmesi)
⑦ FİNAL + KAPAK ffmpeg -ss ____ -i teslim.mp4 -frames:v 1 kanit.jpg → SPEC §1 beşlisi görünüyor mu: __ (-ss 159.0)
                KAPAK KAYNAĞI ffmpeg -ss ____ -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                KAPAK KANITI  bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png → __
BÖLÜM SINIRI    ffmpeg -ss 80.0 -i teslim.mp4 -frames:v 1 sinir.jpg → SPEC §7 ile aynı mı: __ (G10)
TEK KALDIRMA    ffmpeg -ss 7.9 / 8.0 → vagon iki yakada aynı yerde, sapanlar bağlı mı: __
İSTASYON        ffmpeg -ss 111.9 · 112.0 · 119.9 · 120.0 → 111,9 ile 120,0 aynı dış kare mi (dış büyüme yok): __
TEK AKŞAM       ffmpeg -ss 135.9 / 136.0 · 143.9 / 144.0 · 151.9 / 152.0 → lambalar ve oturanlar iki yakada aynı mı: __
```

### 4b. QA MASTERLARI (yalnız 6/8 dk · QA birimi BÖLÜM)

```
— uygulanmaz: 2 dk hattında QA birimi FİLM (tek master × 5 mercek)
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
⬜ MÜZİK: kaynak · lisans · BPM ölçüldü mü (120) · restoran/kalabalık ortam kayıtlarının kaynağı
⬜ SES EFEKTİ kütüphanesi (kullanılırsa): kaynak · lisans
⬜ AÇILIŞ YAZISI kullanıldı mı ("DINNER ABOVE THE DROP.") — evet ise saniye ve konum
⬜ REJİM G ölçümü (PİLOT ①): konuk görünümü · çiftin yürüyüşü · çam dalları — DERS adayı mı
⬜ İKİ İSTASYON aynı tilt (14°) ölçümü (⑨) — İSTASYON §0 ① "tilt 0" kuralına karşı ilk kayıt · DERS adayı mı
⬜ DERS 57 vagon ölçümü (PİLOT ②): vagon kopyalandı mı · sapan koptu mu · iniş kaç px
```
