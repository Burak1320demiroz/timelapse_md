# 🗒️ THE_GRAND_REVIVAL — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · bu günlüğe tek satır yazılmadı · (18.10.2026 klasör açıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28 — dört filmde dört kez tutulmadı]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `kilavuzlar/FILM_KLASOR_SABLONU/FILM_URETIM_GUNLUGU.md`.
> Plan: `THE_GRAND_REVIVAL_PLAN.md` · promptlar `ODA_01_ON_CEPHE/…` … `ODA_10_AKSAM/…`.
> Format: ⭐ DOKUZ İSTASYON, ON ÜÇ ZİNCİR — 90 sahne = 90 sahne görseli (G0…G89) + 12 ODA SON KARESİ (G10′ … G89′) +
> G90 USTA KARE + 90 I2V [KILAVUZ_REHBERI §2.7]. Her oda kendi istasyonunda kendi zinciridir; oda sınırı bir KESMEDİR.
> Izgara: ⛔ DÜZ 90 × 8,0 = 720,0 sn + KAPAK KARTI 5,0 sn = 725,0 sn (sahip seçimi 17.10.2026 — PLAN §DÜZ IZGARA BEYANI).
> ⭐ İSTASYON sütunu boş bırakılamaz: A · H · L · D · K · M · W · B · T. zincir_kontrol YALNIZ aynı istasyonun iki karesi
>   arasında koşulur; istasyon kesmesinin iki yakası (G(n)′ ↔ G(n)) KARŞILAŞTIRILMAZ — farklı kameradır.
> ⭐ Dönüş klipleri (S86 H2 · S87 L2 · S88 A2 · S89 D2) kendi istasyonunun ODA SON KARESİ'nden türetilir
>   (G86 ← G17′ · G87 ← G30′ · G88 ← G10′ · G89 ← G42′): aynı kadraj, akşam ışığı, ek eşyalar (PLAN §DEFTERLER).
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
   ⛔ tavan < 8,0 ise 90 sahnenin hepsi iki zincirli klip (ara kare Gn″) — ızgara kararı proje sahibine döner:
   KARAR         ____
② KAMERA        ilk/son kare kayması: ____ px    (KAMERA_ISTASYONU §7 eşiğini aşıyorsa ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ IŞIK LEKESİ   iç mekânda ilk/son kare pencere lekesi kayması: ____   (0 ise iç mekânın zaman taşıyıcısı yok)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5   (plan promptları 3920–5220 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: ____
⑨ 16:9          araç 1920×1080 (ya da 16:9 4K) veriyor mu: __ · kırpma/letterbox yok: __
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 1. USTA KARE

```
KARE    G90 (son klibin HEDEF karesi · sahne değil) [§2.7] · DINING STATION
ARAÇ    [görsel model + ayar]
PROMPT  birebir ODA_10 §USTA KARE'den / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    final hiyerarşisi ① iki kişi oturuyor ② avize yanık + 10 sandalye ③ üç cam kapı 918 px — bu sırayla mı ·
        işçi/araba/membran/merdiven YOK · ayna YOK · ufuk %50 · sol üst başlık bölgesi sade → geçti/düştü
PİKSEL  cam kapılar __ px (x ____–____) → PLAN ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

### 1a. ODA USTA KARELERİ — her istasyonun ilk üretilen karesi (metinden)

| istasyon | kare | ölçü çapası px (plan → ölçülen) | kapı çapası (komşu oda) elle | sahip onayı | dosya |
|:-:|---|---|---|---|---|
| D | G90 (yukarıda) · G42′ | 918 → | mutfak (harap/bitmiş) · veranda | | |
| A | G89′ · G10′ | 86 → | — | | |
| H | G87′ · G17′ | 584 → | — | | |
| L | G88′ · G30′ | 542 → | bitmiş hol | | |
| K | G54′ | 420 → | bitmiş yemek odası | | |
| M | G66′ | 192 → | eski giyinme odası | | |
| W | G73′ | 250 → | bitmiş yatak odası | | |
| B | G80′ | 512 → | bitmiş giyinme odası | | |
| T | G86′ | 64 → | bitmiş salon + yemek odası | | |

## 1b. ⛔ PİLOT ÜÇLÜ — FİNAL ÜRETİLEBİLİRLİK TESTİ [KILAVUZ_REHBERI §8 adım 2b · C1-b]

> Zincirin İLK halkası. Üçü onaylanmadan §2'nin kalanı üretilmez; üretilemeyen kapsam daralır (sahne çıkar),
> prompt "düzeltilmez". Nirengi eşiği: KAMERA_ISTASYONU §7.

| parça | dosya | zincir_kontrol | 3 nirengi (px) | beş soru ✓ | sahip onayı (tarih) |
|---|---|---|---|:---:|---|
| ① G90 + G89 + S89 (final · gerçek zaman · iki kişi oturur) | | geçti/düştü | | ✓/✗ | |
| ② G39 + G38 + S38 (sayım: 2 → 6 sandalye) | | geçti/düştü | | ✓/✗ | |
| ③ G49 + G48 + S48 (taş tezgâh · dört işçi · sapan · G) | | geçti/düştü | | ✓/✗ | |
| — sonra G1 + G0 + S0 (açılış nesnesi · MAIN STATION) | | geçti/düştü | | ✓/✗ | |

## 2. GERİYE ZİNCİR — KARE başına TEK satır, istasyon istasyon, sıra: son kare → ilk kare

> Her kare bir öncekinin üstünde EDİT [P2-a]. Ölçü çapası elle (px) her karede [DERS 25].
> ⛔ Sahne tavanı 8,0'ı taşımıyorsa her G(n) ile G(n+1) arasına Gn″ satırı açılır.
> ⭐ G30 ve G60 bölüm sınırı kareleridir — G30 yemek odası zincirinin ilk karesi, G60 yatak odası zincirinin içinde.
> Betikten üretilir (`grv_gen.py`) — satır silinmez, sütunlar üretimde doldurulur.

<!-- ÜRETİCİ: KARE ZİNCİRİ BAŞI -->
| G | istasyon | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ | prompt birebir mi | zincir_kontrol | ölçü çapası elle | dosya |
|:-:|:-:|---|---|---|---|:---:|:---:|---|
| **G90** | D | | — (metinden · KAPAK KAYNAĞI) | | | | | |
| G89 | D | | | | | | | |
| **G89′** | A | | — (metinden · ODA USTA KARESİ) / A akşam karesinden | | | | | |
| G88 | A | | | | | | | |
| **G88′** | L | | — (metinden · ODA USTA KARESİ) / L akşam karesinden | | | | | |
| G87 | L | | | | | | | |
| **G87′** | H | | — (metinden · ODA USTA KARESİ) / H akşam karesinden | | | | | |
| G86 | H | | | | | | | |
| **G86′** | T | | — (metinden · ODA USTA KARESİ) / T akşam karesinden | | | | | |
| G85 | T | | | | | | | |
| G84 | T | | | | | | | |
| G83 | T | | | | | | | |
| G82 | T | | | | | | | |
| G81 | T | | | | | | | |
| G80 | T | | | | | | | |
| **G80′** | B | | — (metinden · ODA USTA KARESİ) / B akşam karesinden | | | | | |
| G79 | B | | | | | | | |
| G78 | B | | | | | | | |
| G77 | B | | | | | | | |
| G76 | B | | | | | | | |
| G75 | B | | | | | | | |
| G74 | B | | | | | | | |
| G73 | B | | | | | | | |
| **G73′** | W | | — (metinden · ODA USTA KARESİ) / W akşam karesinden | | | | | |
| G72 | W | | | | | | | |
| G71 | W | | | | | | | |
| G70 | W | | | | | | | |
| G69 | W | | | | | | | |
| G68 | W | | | | | | | |
| G67 | W | | | | | | | |
| G66 | W | | | | | | | |
| **G66′** | M | | — (metinden · ODA USTA KARESİ) / M akşam karesinden | | | | | |
| G65 | M | | | | | | | |
| G64 | M | | | | | | | |
| G63 | M | | | | | | | |
| G62 | M | | | | | | | |
| G61 | M | | | | | | | |
| G60 | M | | | | | | | |
| G59 | M | | | | | | | |
| G58 | M | | | | | | | |
| G57 | M | | | | | | | |
| G56 | M | | | | | | | |
| G55 | M | | | | | | | |
| G54 | M | | | | | | | |
| **G54′** | K | | — (metinden · ODA USTA KARESİ) / K akşam karesinden | | | | | |
| G53 | K | | | | | | | |
| G52 | K | | | | | | | |
| G51 | K | | | | | | | |
| G50 | K | | | | | | | |
| G49 | K | | | | | | | |
| G48 | K | | | | | | | |
| G47 | K | | | | | | | |
| G46 | K | | | | | | | |
| G45 | K | | | | | | | |
| G44 | K | | | | | | | |
| G43 | K | | | | | | | |
| G42 | K | | | | | | | |
| **G42′** | D | | — (metinden · ODA USTA KARESİ) / D akşam karesinden | | | | | |
| G41 | D | | | | | | | |
| G40 | D | | | | | | | |
| G39 | D | | | | | | | |
| G38 | D | | | | | | | |
| G37 | D | | | | | | | |
| G36 | D | | | | | | | |
| G35 | D | | | | | | | |
| G34 | D | | | | | | | |
| G33 | D | | | | | | | |
| G32 | D | | | | | | | |
| G31 | D | | | | | | | |
| G30 | D | | | | | | | |
| **G30′** | L | | — (metinden · ODA USTA KARESİ) / L akşam karesinden | | | | | |
| G29 | L | | | | | | | |
| G28 | L | | | | | | | |
| G27 | L | | | | | | | |
| G26 | L | | | | | | | |
| G25 | L | | | | | | | |
| G24 | L | | | | | | | |
| G23 | L | | | | | | | |
| G22 | L | | | | | | | |
| G21 | L | | | | | | | |
| G20 | L | | | | | | | |
| G19 | L | | | | | | | |
| G18 | L | | | | | | | |
| G17 | L | | | | | | | |
| **G17′** | H | | — (metinden · ODA USTA KARESİ) / H akşam karesinden | | | | | |
| G16 | H | | | | | | | |
| G15 | H | | | | | | | |
| G14 | H | | | | | | | |
| G13 | H | | | | | | | |
| G12 | H | | | | | | | |
| G11 | H | | | | | | | |
| G10 | H | | | | | | | |
| **G10′** | A | | — (metinden · ODA USTA KARESİ) / A akşam karesinden | | | | | |
| G9 | A | | | | | | | |
| G8 | A | | | | | | | |
| G7 | A | | | | | | | |
| G6 | A | | | | | | | |
| G5 | A | | | | | | | |
| G4 | A | | | | | | | |
| G3 | A | | | | | | | |
| G2 | A | | | | | | | |
| G1 | A | | | | | | | |
| G0 | A | | | | | | | |
<!-- ÜRETİCİ: KARE ZİNCİRİ SONU -->

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o kare atılır, yeniden türetilir,
   satır yeniden yazılır [DERS 12 · 25]. Düşen kareden türetilmiş alt kare tabloya giremez.
⚠️ En uzun zincir 14 kare (salon G17–G29 + G30′): her ~7 karede G(n) ↔ oda son karesi yan yana konur
   (3 nirengi px) — kayma eşiği aşıyorsa zincir oda son karesinden yeniden alınır.
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kırpma BAŞTAN [§2.7 ③]. REJİM sütunu boş bırakılamaz [A6-a].
> ⛔ HER KLİP İKİ ONAYLI KAREYE KİLİTLİDİR: ilk kare G(n), son kare hedef (G(n+1) ya da G(n+1)′); klip üretildikten
> SONRA son kare ↔ hedef görsel zincir_kontrol koşulur [§2.7 · ARAC_KARTLARI ⑧].
> ⭐ **baş/orta/son** [C1-a]: başta yük kaynağında mı · ortada taşıyıcıyla birlikte mi (süzülmüyor, boyu değişmiyor) ·
> sonda fark görünüyor mu. Üç ✓ olmayan klip, zincir_kontrol geçse bile yeniden üretilir.

<!-- ÜRETİCİ: KLİPLER BAŞI -->
| S | istasyon | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma | teslim süre | baş/orta/son | dosya |
|:-:|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|---|
| S0 | A | | A | G0 | G1 | | | | | | | |
| S1 | A | | A | G1 | G2 | | | | | | | |
| S2 | A | | A | G2 | G3 | | | | | | | |
| S3 | A | | A | G3 | G4 | | | | | | | |
| S4 | A | | A | G4 | G5 | | | | | | | |
| S5 | A | | A | G5 | G6 | | | | | | | |
| S6 | A | | A | G6 | G7 | | | | | | | |
| S7 | A | | A | G7 | G8 | | | | | | | |
| S8 | A | | A | G8 | G9 | | | | | | | |
| S9 | A | | A | G9 | G10′ | | | | | | | |
| S10 | H | | A | G10 | G11 | | | | | | | |
| S11 | H | | A | G11 | G12 | | | | | | | |
| S12 | H | | A | G12 | G13 | | | | | | | |
| S13 | H | | A | G13 | G14 | | | | | | | |
| S14 | H | | A | G14 | G15 | | | | | | | |
| S15 | H | | A | G15 | G16 | | | | | | | |
| S16 | H | | A | G16 | G17′ | | | | | | | |
| S17 | L | | A | G17 | G18 | | | | | | | |
| S18 | L | | A | G18 | G19 | | | | | | | |
| S19 | L | | A | G19 | G20 | | | | | | | |
| S20 | L | | A | G20 | G21 | | | | | | | |
| S21 | L | | A | G21 | G22 | | | | | | | |
| S22 | L | | A | G22 | G23 | | | | | | | |
| S23 | L | | A | G23 | G24 | | | | | | | |
| S24 | L | | A | G24 | G25 | | | | | | | |
| S25 | L | | A | G25 | G26 | | | | | | | |
| S26 | L | | G | G26 | G27 | | | | | | | |
| S27 | L | | A | G27 | G28 | | | | | | | |
| S28 | L | | A | G28 | G29 | | | | | | | |
| S29 | L | | A | G29 | G30′ | | | | | | | |
| S30 | D | | A | G30 | G31 | | | | | | | |
| S31 | D | | A | G31 | G32 | | | | | | | |
| S32 | D | | A | G32 | G33 | | | | | | | |
| S33 | D | | A | G33 | G34 | | | | | | | |
| S34 | D | | G | G34 | G35 | | | | | | | |
| S35 | D | | A | G35 | G36 | | | | | | | |
| S36 | D | | A | G36 | G37 | | | | | | | |
| S37 | D | | A | G37 | G38 | | | | | | | |
| S38 | D | | A | G38 | G39 | | | | | | | |
| S39 | D | | A | G39 | G40 | | | | | | | |
| S40 | D | | A | G40 | G41 | | | | | | | |
| S41 | D | | A | G41 | G42′ | | | | | | | |
| S42 | K | | A | G42 | G43 | | | | | | | |
| S43 | K | | A | G43 | G44 | | | | | | | |
| S44 | K | | A | G44 | G45 | | | | | | | |
| S45 | K | | A | G45 | G46 | | | | | | | |
| S46 | K | | A | G46 | G47 | | | | | | | |
| S47 | K | | A | G47 | G48 | | | | | | | |
| S48 | K | | G | G48 | G49 | | | | | | | |
| S49 | K | | A | G49 | G50 | | | | | | | |
| S50 | K | | A | G50 | G51 | | | | | | | |
| S51 | K | | A | G51 | G52 | | | | | | | |
| S52 | K | | A | G52 | G53 | | | | | | | |
| S53 | K | | A | G53 | G54′ | | | | | | | |
| S54 | M | | A | G54 | G55 | | | | | | | |
| S55 | M | | A | G55 | G56 | | | | | | | |
| S56 | M | | A | G56 | G57 | | | | | | | |
| S57 | M | | A | G57 | G58 | | | | | | | |
| S58 | M | | A | G58 | G59 | | | | | | | |
| S59 | M | | A | G59 | G60 | | | | | | | |
| S60 | M | | G | G60 | G61 | | | | | | | |
| S61 | M | | A | G61 | G62 | | | | | | | |
| S62 | M | | A | G62 | G63 | | | | | | | |
| S63 | M | | A | G63 | G64 | | | | | | | |
| S64 | M | | A | G64 | G65 | | | | | | | |
| S65 | M | | A | G65 | G66′ | | | | | | | |
| S66 | W | | A | G66 | G67 | | | | | | | |
| S67 | W | | A | G67 | G68 | | | | | | | |
| S68 | W | | A | G68 | G69 | | | | | | | |
| S69 | W | | A | G69 | G70 | | | | | | | |
| S70 | W | | A | G70 | G71 | | | | | | | |
| S71 | W | | A | G71 | G72 | | | | | | | |
| S72 | W | | A | G72 | G73′ | | | | | | | |
| S73 | B | | A | G73 | G74 | | | | | | | |
| S74 | B | | A | G74 | G75 | | | | | | | |
| S75 | B | | A | G75 | G76 | | | | | | | |
| S76 | B | | A | G76 | G77 | | | | | | | |
| S77 | B | | G | G77 | G78 | | | | | | | |
| S78 | B | | A | G78 | G79 | | | | | | | |
| S79 | B | | A | G79 | G80′ | | | | | | | |
| S80 | T | | A | G80 | G81 | | | | | | | |
| S81 | T | | A | G81 | G82 | | | | | | | |
| S82 | T | | A | G82 | G83 | | | | | | | |
| S83 | T | | A | G83 | G84 | | | | | | | |
| S84 | T | | A | G84 | G85 | | | | | | | |
| S85 | T | | A | G85 | G86′ | | | | | | | |
| S86 | H | | A | G86 | G87′ | | | | | | | |
| S87 | L | | A | G87 | G88′ | | | | | | | |
| S88 | A | | A | G88 | G89′ | | | | | | | |
| S89 | D | | G | G89 | G90 | | | | | | | |
<!-- ÜRETİCİ: KLİPLER SONU -->

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6] — TAM master

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____   (1920,1080,30/1,h264 · tolerans SIFIR)
② SÜRE          ffprobe format=duration → ____ sn   (725,0 = 720,0 sahne + 5,0 kart)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 yatay_12_dk_filmler/THE_GRAND_REVIVAL/THE_GRAND_REVIVAL_PLAN.md → çıkış: __
                beklenen kesmeler 8,0 · 16,0 · … · 712,0 (89 kesme) + kart 720,0
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        müziksiz pencere 0,0–8,0 (S0) plana uygun mu: evet/hayır
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 718.0 -i teslim.mp4 -frames:v 1 kanit.jpg → SPEC §1 üçlüsü görünüyor mu: __
                KAPAK KAYNAĞI ffmpeg -ss 719.5 -i teslim.mp4 -frames:v 1 g90_kaynak.jpg
                KAPAK KANITI  bash araclar/zincir_kontrol.sh g90_kaynak.jpg kapak_metinsiz.png → __
KART            ffmpeg -ss 722.5 -i teslim.mp4 -frames:v 1 kart.jpg → G90 + başlık, sol üst · erime ≤ 1 sn: __
```

### 4b. QA MASTERLARI — üç bölüm (QA birimi BÖLÜM)

```
B1  ffmpeg -i teslim.mp4 -t 240 -c copy b1.mp4            → ffprobe süre ____ (240,0)
B2  ffmpeg -ss 240 -i teslim.mp4 -t 240 -c copy b2.mp4    → ffprobe süre ____ (240,0)
B3  ffmpeg -ss 480 -i teslim.mp4 -t 240 -c copy b3.mp4    → ffprobe süre ____ (240,0 · KART YOK)
b1_son.jpg ↔ b2_ilk.jpg — İSTASYON KESMESİ (G30′ ↔ G30): zincir_kontrol KOŞULMAZ, saat sürüyor mu elle: __
b2_son.jpg ↔ b3_ilk.jpg zincir_kontrol → __   (dikiş = G60, aynı istasyon)
QA paketi bölüm başına: bash araclar/qa_paket.sh yatay_12_dk_filmler/THE_GRAND_REVIVAL b<n>.mp4 (⚠️ --bolum 3 henüz yok)
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
```
