# 🔍 THE_LAST_CARRIAGE — QA SPEC

> THE LAST CARRIAGE · 16:9 · 20 × 8,0 sn · 160,0 sn · kart yok · müzik VAR (24 sn'den) · iki istasyon (S14 iç). **Bu dosya
> yalnız belgeli merceklere verilir: ❹ İNŞA · ❺ TESLİM** (beş mercekli QA, 06.10.2026 [DERS 64]).
> ⛔ **❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❸ ŞANTİYE'ye VERİLMEZ** — üçü kör koşar, ayrı geçici sohbette, proje dışında
> [`QA_KOSU_KILAVUZU` §1]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit değildir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_LAST_CARRIAGE <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].
> Ham raporlar `QA/HAM/THE_LAST_CARRIAGE/THE_LAST_CARRIAGE_Q<n>_<AD>_HAM.md` · kayıt `QA/FILMLER/THE_LAST_CARRIAGE.md` · `QA/TABLO.md`.

---

## 0. KÜNYE

```
FİLM          THE_LAST_CARRIAGE — dar ve derin hayalî bir kanyonu iki kaya rafı arasında aşan hazır çelik tabliyeye paslı eski bir
              yolcu vagonu vinçle indirilir; sapanlar çözülür; eski camlar sökülür; pas kumlanır; gövde zümrüt yeşili + krem şerit,
              çatı bakır renkli, sekiz yeni cam; iki kısa çelik geçit; önüne çelik çerçeveli teras, iki yanı ahşap, ortası üç büyük
              cam panel, şeffaf korkuluk; dört dış masa; içeride ahşap masalar + deri banklar (iç kamera); şantiye çekilir; akşam
              ışıklar yanar, konuklar gelir, terasa çıkar; bir çift camın üstünde durur · MAIN STATION + CARRIAGE STATION (S14)
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_2_dk_filmler · HIZ 1x · ⚠️ 160 sn bu klasörün 2:00 bandının dışı (beyanlı)
KANARYA       rivetlark   ⛔ kör mercek raporunda bu kelime geçerse plan SIZMIŞTIR → koşu SIZINTI [QA_KOSU §3.1]

TESLİM YAPISI ⭐ SAHNE BLOĞU  20 sahne × 8,0 sn = 160,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  ⛔ YOK                                   ← son sahne S19 son saniyeye kadar SAHNEDİR
                 TOPLAM                          160,0 sn
              ⛔ 160,0 sn'den uzun dosya = plan dışı kart/siyah → ❺ "the plan declares NO card — report it"
              ⛔ ekranda YAZI yok (açılış cümlesi yalnız kurguda ve yalnız sahip seçerse — günlük §5)

SAHNE SAATLERİ  sahne n = n × 8,0 → (n+1) × 8,0   ·   S0 0,0–8,0 · … · S9 72,0–80,0 · S10 80,0–88,0 · … · S19 152,0–160,0
                (19 kesme, her 8,0 sn · müzik 120 BPM → her kesme ölçü başında, 4 ölçü/sahne)
PART GRID       — (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)
⛔ DÜZ IZGARA   sahip senaryosu (hikâye SAPMA ②) · ⚠️ bandın dışı (format 12 × 10,0 · 2:00). Eşit klipte ❷ RHYTHM NOT
                TRIGGERED. Karşı kayıt [DERS 44].
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]: ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — {5,9} ya da {5,10}
   gerekir; {4,6,8} çıkarsa iki-klip hükmü (PLAN §DEĞİŞMEZLER) ve karar sahibe döner.

⭐ İKİNCİ İSTASYON BEYANI [ISTASYON_VE_IC_MEKAN §6]
                ad CARRIAGE STATION (iç) · h +3,1 (tabliyeden) · bakış 90° · tilt 14° · 28 mm · yalnız S14 (112,0–120,0) ·
                PARALEL ZAMAN: S13 ile aynı on dakika (17:10 → 17:20) · dış yapı iki yakada aynı · sahip kararı: TUR 1 (12.10.2026)
                ❹ DAVETLİ listesinde iç mekân eşyası var (§5) · ❶ ❷ ❸ için olgu satırı ⬜ EKLENMEDİ (İSTASYON §6 sahip kararı
                bekliyor) — ❶ SEPARATE IMAGES verirse önce gerekçesindeki saniye okunur: 112,0 / 120,0 mı, gerçek kayma mı
TEK KALDIRMA    S0 + S1 (0,0–16,0) — aynı vinç, aynı çapraz kiriş, aynı dört sapan; vagon S0 sonunda oturur, S1'de sapanlar çözülür;
                vagon bir daha kalkmaz, sallanmaz, kaymaz
TEK AKŞAM       S16 → S19 (128,0–160,0) — yanan lamba bir daha sönmez, oturan konuk yerinde kalır; 144,0'de rejim A → G (gerçek
                zaman) — bu kesmede konukların "iz" görünümü küçük, net figüre döner (beyanlı dikiş)
YAPI          kanyonu aşan çelik tabliye (iki derin kiriş · yürüme yolları · ön kirişte dirsekler — G0'dan) · tek eski yolcu vagonu
              (≈24 m · yuvarlak çatı · her yanda 8 geniş pencere · 2 uç vestibül · tekerleksiz alt şasi) · sonradan: zümrüt + krem
              boya · bakır renkli çatı · 8 yeni cam · iki kısa çelik geçit · 15 × 6 m teras (3 çelik çerçeve · ahşap yanlar · ortada
              3 cam panel · korkuluk) · dört dış masa · iç masa + bank · lambalar
SAHA          gri-kahverengi kayalık dar kanyon · iki kaya rafı · 47° K · çapalar: ⭐ YARIK KAYA (sağ rafta — kanıt) · çatallı çam
              (sol raf kenarı) · uzak mavi sırtlar · servis yolu + çakıllı avlu
ZAMAN YAYI    ≈3–5 ay (kaldırma bir sabah · restorasyon + teras aylar · açılış akşamı) · film mertebe anlatır: "bir sabah vagon iner,
              bir mevsim boya, bakır ve cam, bir akşam ilk konuklar"
IŞIK          TEK GÜN 09:30 → 17:50 (mavi saat, güneş −4,9°) · Σ rejim 8 sa 20 dk · mevsim SABİT (sonbahar) · bilinçli sıkıştırma
              (sahip: "tek günde yapılabildiği iddiası değildir") · güneş hiçbir karede kadrajda değil
REJİM         A (10 dk) × 14 ana + 1 iç (paralel) · B (2 sa) × 3 (S3 · S4 · S10) · G (8 sn · gerçek zaman) × 2 (S18 · S19, final) —
              ⚠️ üç rejim, beyanlı · ⚠️ G depoda ölçülmedi
KAMERA        MAIN STATION — 28 mm · h 11,0 m (tabliyeden) · D_eksen 32,3 · bakış 337° · tilt 14° AŞAĞI · roll 0° · üç çeyrek (≈23°)
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G20 usta kare → G19 → … → G15 → G13 → … → G0 · iç zincir ayrı: G14′ → G14 · her kare zincir_kontrol
GÜNLÜK        THE_LAST_CARRIAGE_URETIM_GUNLUGU.md — ⛔ boş (üretim başlamadı) → bu SPEC'in hükmü üretimle başlar
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı · ❺ FINAL BEAT

```
SAHNE       S19 (152,0–160,0)
FİNAL BEAT  152,0–156,0 olay: bir yetişkin çift sol ahşap bölümden cam orta bölüme sakin adımlarla yürür ve ortasında durur, vadiye
            döner; bir garson masaya sürahi bırakır · 156,0–160,0 TUTUŞ: çift camın üstünde durur, içerideki ve terastaki konuklar
            küçük doğal hareketler yapar, çam dalları hafif sallanır; yapıda HİÇBİR şey değişmez — kare donmaz, olay da büyümez
SANİYE      159,0 (son 4,0 sn'lik TUTUŞUN içi [P2-i]; mavi saat, okunur [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (beşi de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① ışıklı sekiz pencere + zümrüt gövde + bakır çatı (x 503–1586 · üstten 456–770) — en parlak
   ② cam orta bölüm (x 679–922 · üstten 708–843) ve üstündeki çift (≈85 px, yüzü okunmaz) — camın altında kanyon
   ③ dış masalarda konuklar + korkuluk dibindeki ışık şeridi + korkuluk
   ④ iki geçit ve lambaları (382 · 617 / 1765 · 821) + tabliye + kanyon gölgesi + MAVİ gök ve uzak sırtlar (168) — siyah değil
   ⑤ AYNI yarık kaya (kanıt nesnesi: x 1649–1806 · tepe 405 · 157 px — G0 ile aynı konum ve boy) + çatallı çam (x ≈196–260)
   + geçici ekipman GİTMİŞ: vinç, telehandler, kamyon, kasa, palet, konteyner YOK (yalnız bir beyaz minibüs — SÖKÜM satırı)
   + BEDEL görünür: pas yok; yerinde ışıklı restoran (G0 ↔ G20)

KOMUT
   ffmpeg -ss 159.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①–⑤'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP (biçim kafiyesi, ışık bilinçli farklı)
   ffmpeg -ss 0.3   -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 kanit_g20.jpg
   İki karede kaya, çam, tabliye ve sırtlar aynı yerde; kaya aynı x'te (1649–1806 ±2 px); vagon aynı enle (503–1586). G0'da paslı
   vagon tabliyenin 1 m üstünde, vinçte asılı; G20'de aynı vagon tabliyede, ışıklı, önündeki camın üstünde bir çift.
   Işık: G0 sabah ↔ G20 mavi saat (PLAN LOOP satırı) — kanıt çifti AYNI IŞIK iddiası taşımaz.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=28 · h=11,0 · tilt 14° aşağı · bakış 337° · iğne deliği izdüşümü · üstten px)

| nesne | kot (m) | x (soldan) | üstten | her karede |
|---|:-:|:-:|:-:|---|
| uzak sırtlar / ufuk | — | bütün en | 168 (%84) | ✓ |
| ⭐ kanıt nesnesi YARIK KAYA | −1 → +5,5 | 1649–1806 | 405–673 | ✓ BİREBİR (157 px en, boy dâhil) · tek kaya, koyu çatlak |
| çatallı çam dip → tepe | 0 → +13 | 196–260 | 77–622 | ✓ (G'de dalları hafif sallanır) |
| vagon çatısı sol → sağ | +4,2 | 503 → 1586 | 456 → 554 | G1+ (G0'da 1 m yukarıda) |
| vagon alt şasisi sol → sağ | 0 | 515 → 1563 | 621 → 770 | G1+ |
| G0 asılı vagon alt şasisi (orta) | +1,0 | 965 | 642 | yalnız G0 |
| pencere bandı | +1,9…+2,9 | 548 → 1507 | 532 → 641 | ✓ (8 açıklık) |
| sol geçit avlu ucu · sağ geçit raf ucu | 0 | 382 · 1765 | 617 · 821 | G8+ · G9+ |
| kiriş mesnetleri sol · sağ | −1,8 | 519 · 1481 | 716 · 882 | ✓ |
| teras ön kenarı sol → sağ | 0 | 455 → 1222 | 755 → 900 | G10+ |
| cam orta bölüm ön · arka | 0 | 679–922 · 812–1027 | 798–843 · 708–741 | G12+ cam · G10–G11 açık |
| mobil vinç (avlu) | 0 | ≈372 | ≈517 | G0–G15 |
| avlu · servis yolu | 0 → +1 | 376 · sol kenar | 558 · ≈511 | ✓ |
| insan (1,7 m) | — | — | cam bölümde 85 px · sol geçitte 66 px · teras masasında 79 px | ölçek |

### İÇ İSTASYON (CARRIAGE · f=28 · h=3,1 · tilt 14° · bakış 90°) — yalnız G14 · G14′

| nesne | x (soldan) | üstten | her iç karede |
|---|:-:|:-:|---|
| sağ uç duvar (üst) | 884–1079 (195 px) | 108 → dibi 318 | ✓ BİREBİR |
| cam kapı | 949–1013 | 175 → 318 | ✓ |
| yarık kaya (uzak sol pencereden) | ≈399 | ≈233 | ✓ (ana karedeki kayayla aynı ton ve çatlak — ELLE) |
| uzak sırtlar (pencerelerden) | — | 168 (%84) | ✓ (ana kamerayla AYNI yükseklik) |

```
KAMERA SABİTLİK  ilk/son kare kayması ≤ 2 px (1080p · KAMERA_ISTASYONU §7 · zincir_kontrol ESIK_KAYMA_ORAN) ·
                 üç nirengi: yarık kayanın tepesi · vagonun sol çatı köşesi · sol kiriş mesnedi
                 iç: sağ uç duvarın iki üst köşesi + cam kapının üstü
28 MM            yatay görüş 65,5° — kenar gerilmesi küçük; ❶ "kamera değişti" derse önce 112,0 / 120,0 istasyon kesmesi mi diye bakılır
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
O = vagon tabanının ortası, tabliyenin üstü (z 0) · +x doğu (vagon ekseni) · +y kuzey · vagon x ±12,2, y ±1,45, çatı +4,2 (orta +4,6),
iç taban +1,0, pencere bandı +1,9…+2,9 · raflar x ±9 (boşluk ≈18 m), −1,8 · tabliye kirişleri x ±16, yakın kiriş y −3, alt −1,8 ·
geçitler x ±15,5 · teras x ±7,5, y −3…−9 · cam x ±2,4, y −4…−9 (3 panel) · avlu x −16…−28 · vinç (−24, 6) · çam (−18, −4) +13 ·
kaya (14…17,5, 10) −1 → +5,5 · ana kamera (12, −30, +11) · iç kamera (−10,6, 0,3, +3,1)
```

### Yapı yüzdesi ve saha durumu — sahne sahne (❹ İNŞA · ❺ TESLİM için)

| S | saat | yapı: eleman + ara hâl | gövde · teras · konuk · ışık | geçici ekipman kadrajda | ışık evresi |
|:-:|:-:|---|---|---|---|
| S00 | 09:30→09:40 | ⭐ vagon asılı → tabliyede | pas · eski camlar | vinç (vagon) · halat ekipleri · cıvata kamyonu | sabah |
| S01 | 09:40→09:50 | (değişmez) · sapanlar çözülür | aynı | vinç (kiriş → avlu → bom dik) · telehandler · kasa kamyonu | sabah |
| S02 | 09:50→10:00 | (yenileme) · eski camlar sökülür | sekiz açıklık boş | kasalar · konteyner · telehandler · sonda kompresör | sabah |
| S03 | 10:00→12:00 | (değişmez) · ⭐ pas gider | pas → gri çelik | kompresör · kum haznesi · brandalar · sonda boya römorku | sabah → öğle |
| S04 | 12:00→14:00 | ⭐ zümrüt + krem | gri → yeşil | boya römorku · varil paletleri · sonda bakır kamyonu | öğle → öğleden sonra |
| S05 | 14:00→14:10 | bakır çatı, soldan | çatı gri → bakır | vinç (palet) · çatıcılar · sonda cam sehpası | öğleden sonra |
| S06 | 14:10→14:20 | sekiz cam, soldan | açıklıklar → cam | vinç (sehpa) · camcılar · sonda geçit kamyonu | öğleden sonra |
| S07 | 14:20→14:30 | sol geçit + sönük lambalar | — | vinç (geçit) · çakıl kamyonu | öğleden sonra |
| S08 | 14:30→14:40 | sağ geçit + basamaklar + sönük lambalar | — | vinç (geçit) · basamak istifi · sonda çerçeve kamyonu | öğleden sonra |
| S09 | 14:40→14:50 | üç teras çerçevesi, soldan | açık iskelet | vinç (çerçeve) · uzun kamyon (3 → 0) | öğleden sonra |
| S10 | 14:50→16:50 | ⭐ ahşap yanlar + şerit · orta AÇIK | — | vinç (döşeme paleti) · kamyonlar · sonda A-çerçeve sehpa | → alçalan güneş |
| S11 | 16:50→17:00 | ⭐ üç cam panel | orta → cam | vinç (cam panel) · sehpa · cam el arabası · sonda korkuluk sandığı | altın saat |
| S12 | 17:00→17:10 | korkuluk + sönük ışık şeridi | — | vinç (sandık → bom dik) · sonda masa kamyonu | altın saat |
| S13 | 17:10→17:20 | (değişmez) · dört dış masa | — | masa kamyonu · vinç DIŞ → sonda kasa demeti | gün batımı |
| S14 🪟 | 17:10→17:20 | (dış değişmez) · iç masa + bank + sönük sarkıt lambalar | — | iç: istif · el arabası · merdiven | gün batımı (içeride güneş şeritleri) |
| S15 | 17:20→17:30 | (değişmez) · saha boşalır | — | ⭐ vinç, telehandler, kamyonlar, kasalar, paletler, konteyner ÇIKAR · sonda minibüs | gün batımı |
| S16 | 17:30→17:40 | (değişmez) | ⭐ iç → geçitler → korkuluk YANAR | şalter kutusu · minibüs · garsonlar | alacakaranlık |
| S17 | 17:40→17:50 | (değişmez) | ⭐ ilk konuklar → içerisi çoğu dolu | garsonlar · el arabası | mavi saat |
| S18 | 17:50:00→17:50:08 | (değişmez) | ⭐ konuklar terasa, üç masa | garsonlar · servis arabası | derin mavi · G |
| S19 | 17:50:08→17:50:16 | (değişmez) · TUTUŞ | çift camda | — | derin mavi · G |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   YARIK KAYA — G0…G20 (ana) hepsinde x 1649–1806 · tepe 405 · dip 655–673 · 157 px en; zincirde her karede ELLE ✓/✗
                (günlük §2) · tek kaya, tepeden dibe koyu çatlak — rengi ve biçimi değişmez · iç karede uzak sol pencereden
İKİNCİ ÇAPA     çatallı çam (x ≈196–260) · üçüncü: uzak sırtlar 168 · dördüncü: tek vagon + sekiz pencere + iki vestibül (SAYI ve yer)
❸ İÇİN          dikiş = KARE (G1…G19, G14 hariç): dikişin iki yakası aynı görsel; ❸ REBUILT hükmü zincir koşulmadı demektir ·
                112,0 ve 120,0 İSTASYON kesmesidir — iki yakası aynı kare DEĞİL, beyanlı
⚠️ VAGON        S0'da vagon İNER — bu yapının yerine gelişidir; ❸ "nesne havada belirdi" saymamalı · vagon tek, boyu ve pencere
                sayısı her karede aynı
⚠️ CAM          S2'de eski camlar SÖKÜLÜR (yenilemenin ilk adımı), S6'da yenisi takılır — ❸ "yapı geriye gitti" saymamalı
⚠️ IŞIK         S16'da üç ışık grubu TEK KAREDE yanar (A rejimi, beyanlı) — ❶ "flicker" saymamalı
⚠️ AĞAÇ         S18–S19 gerçek zamanda çam dalları hafif sallanır (rüzgâr) — yer ve boy sabit
```

---

## 5. ❹ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ajanı · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | ajan (taşıyan) | geçici destek | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|---|:-:|:-:|:-:|
| vagon | vinç kancası (G0'da asılı) | vinç → halat ekipleri → cıvata ekibi | çapraz kiriş + dört sapan · kılavuz ipler | G0 (asılı) | G1 (tabliyede) | kiriş S1 avluya |
| eski camlar (giden) | sekiz açıklık | camcılar (vakumlu tutucu) → avludaki kasalar → telehandler → kamyon | kasalar | G2 | G3 (boş) | kasalar S15 |
| pas (giden) | gövde + çatı | kumlama ekipleri (kompresör + kum haznesi) | brandalar · torbalar | G3 | G4 (gri) | kompresör S3 sonu |
| boya | boya römorku + varil paletleri | püskürtme ekipleri | brandalar | G4 (gri) | G5 | römork S5 başında gitmiş |
| bakır çatı | kamyon → vinçte palet | vinç → çatıcılar | çatıdaki beşik · emniyet halatları | G5 (gri) | G6 | — |
| camlar | kamyon → vinçte sehpa | vinç → camcılar (vakumlu tutucu) | sehpa (yürüme yolunda) | G6 (boş) | G7 | sehpa S6 sonunda avluya |
| sol geçit | kamyon | vinç → montajcılar · kaynakçılar | kılavuz ipler | G7 | G8 | — |
| sağ geçit + basamaklar | kamyon · sağ raftaki istif | vinç → montajcılar · taş ustaları | harç | G8 | G9 | — |
| teras çerçeveleri | uzun kamyon (3) | vinç → montajcılar · kaynakçılar | kılavuz ipler | G9 (dirsekler) | G10 | — |
| ahşap döşeme | kamyon → vinçte paletler | vinç → marangozlar | emniyet halatları · çelik kenar çerçeve | G10 | G11 (orta açık) | — |
| cam paneller | vinçte vakumlu çerçeve (1) + A-çerçeve sehpa (2) | vinç · camcılar · cam el arabası | kauçuk taşıyıcılar | G11 (açık) | G12 | sehpa S11 içinde |
| korkuluk + ışık şeridi | vinçte sandık | camcılar · elektrikçi | — | G12 | G13 | sandık S12 sonunda avluya |
| dış masalar | kamyon (avlu) | ekipler (sol geçitten) | — | G13 | G15 | kamyon S13 |
| iç masa + bank + sarkıt lamba | sağ cam kapının önündeki istif | iç ekipler · el arabası · elektrikçi | merdiven | G14 | G14′ | — |
| şantiye | avlu | vinç + kamyonlar + telehandler | — | — | — | ⭐ S15: vinç, telehandler, kamyonlar, kasalar, paletler, konteyner çıkar |
| lambalar yanık | şalter kutusu (avlu kenarı) | elektrik ekibi | — | G16 (sönük) | G17 | — |
| konuklar | servis yolu (sol kenar) → avlu → sol geçit | — (yürür) | garsonlar | G17 (boş) | G19 (dış masalar) | — |

```
❹ DAVETLİ LİSTESİ (sahada olması BEKLENEN her şey — olmayan INTRUDER'dır):
   tek eski yolcu vagonu 1 (8 pencere/yan · 2 vestibül · tekerleksiz) · çelik tabliye 1 · kısa çelik geçit 2 · teras 1 (3 çerçeve ·
   ahşap yanlar · 3 cam panel · korkuluk) · dış masa 4 + sandalyeler · sarı mobil vinç 1 (G0–G15) · çapraz kiriş + 4 sapan
   (G0–G2) · sarı telehandler 1 · düz kasalı kamyonlar (değişen yükler) · ahşap kasalar · çelik atık konteyneri 1 · kompresör
   römorku + kum haznesi (S2 sonu–S3) · boya römorku + varil paletleri (S3 sonu–S4) · cam sehpası · A-çerçeve sehpa + cam el
   arabası · korkuluk sandığı · beyaz minibüs 1 (S15 sonu–S19) · şalter kutusu · lamba direkleri 4 · ekipler (iz) · garsonlar ·
   konuklar · bir yetişkin çift · yarık kaya 1 · çatallı çam 1 · uzak sırtlar
   İÇ (S14): ahşap taban · açık panel duvarlar · krem tavan · 8 pencere/yan · cam kapı · ahşap masalar · deri banklar · sarkıt
   lambalar · el arabası · merdiven · ambalaj filmi
   ⛔ DAVETSİZ: ikinci vagon / tren dizisi · lokomotif · ray · tekerlek · istasyon peronu · kanyonu aşan büyük köprü · şelale ·
      nehir · sis · ayna gibi cam · yüzeysiz delik · iki katlı vagon · havai fişek · konfeti · lazer · hale · drone gölgesi ·
      yazı / afiş / tabela / logo / menü · kule vinç · ikinci teras · kaza / düşen nesne / kırılan cam
❹ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: vagonun yeri = S0 vinç · boş açıklıklar = S2 camcılar · gri =
                  S3 kumlama · yeşil = S4 boya ekipleri · bakır = S5 palet + çatıcılar · camlar = S6 sehpa · geçitler = S7–S8 vinç ·
                  iskelet = S9 · ahşap = S10 · cam = S11 · korkuluk = S12 · masalar = S13 kamyon · iç = S14 istif · boş saha = S15 ·
                  ışıklar = S16 şalter kutusu · konuklar = S17 servis yolu
❹ ÇERÇEVE DEFTERİ vagon 503 → 1586 sabit · kaya 157 px sabit · pencere sayısı 8 · vestibül 2
❹ GİZLİ İŞ        tabliyenin hesabı → G0'da hazır kirişler ve pedler · elektrik → lamba direkleri, ışık şeridi, sarkıt lambalar (sönük
                  takılır) · mutfak → S16'da mutfak ekibinin taşıdığı erzak kasaları
❹ DECLARED WORLD  kanyonda tek vagon · tek vinçli yerleştirme ve montaj (G0–G15) · tek akşam (G16–G20) · G rejimi (S18–S19) · iç
                  istasyon (S14) · kış YOK · gece YOK
❸ PARKED GEREKÇESİ S19 (final tutuşu): yapı bitti; yalnız çift, konuklar ve rüzgâr — ödül ve yaşayan an, işsiz aralık değil, beyanlı
                  [P4-f · C1-d]
```

---

## 6. ❷ ZAMAN VE KESME — kesme listesi ve ses (❷ kör koşar; bu bölüm ❺ ve operatör içindir)

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_LAST_CARRIAGE/THE_LAST_CARRIAGE_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
REJİM KESMELERİ      24,0 (S2 A → S3 B) · 40,0 (S4 B → S5 A) · 80,0 (S9 A → S10 B) · 88,0 (S10 B → S11 A) · 144,0 (S17 A → S18 G)
                     — rejim değişimi YALNIZ kesmede [P5-c] · (32,0: S3 B → S4 B, rejim aynı)
İSTASYON KESMELERİ   112,0 (ana → iç) · 120,0 (iç → ana) — beyanlı; dış yapı iki yakada aynı
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE (istasyon kesmeleri hariç); kesmede ışık, gölge, yapı, lamba, konuk
                     ATLAMAZ · 8,0 (TEK KALDIRMA) · 136,0 · 144,0 · 152,0 (TEK AKŞAM)
MÜZİK                ✅ VAR — 120 BPM · 4 ölçü/sahne · THE_LAST_CARRIAGE_MUZIK.md: 0–24 müzik YOK (rüzgâr, vinç, halat, cıvata, cam)
                     · 24–88 müzik doğar ve büyür (motif 40,0'da) · 88–96 hafifler, üç cam vurgusu · 96–120 geri gelir · 120–144
                     çekilir (rüzgâr, sonra iç uğultu) · 144–160 ana tema — ani kesilme yok
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G10 (S9 ↔ S10) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si (S9) G10 karesinde biter; G10 BOLUM_2'nin ilk görselidir.
ELLE KARE            ffmpeg -ss 80.0 -i teslim.mp4 -frames:v 1 sinir.jpg → üç teras çerçevesi dirseklerde, açık iskelet, ortası açıklık,
                     döşemesiz · iki geçit + sönük lambalar · vagon yeşil + bakır + camlı · vinçte döşeme paleti · öğleden sonra
```

---

## 8. ❺ TESLİM — belgeli merceğin okuyacağı beyanlar

```
VAAT            Paslı eski bir yolcu vagonu kanyonun üstündeki çelik tabliyeye indirilir, yenilenir, önüne cam tabanlı bir teras
                kurulur ve aynı akşam restoran olarak açılır.
DİRENÇ          ① boşluk — S0 (0,0–8,0) vagon havada · ② pas ve harap gövde — S2 (16,0–24,0) · S3 (24,0–32,0) · S4 (32,0–40,0) ·
                ③ erişim ve teras yok — S7–S8 (56,0–72,0) · S9–S11 (72,0–96,0) · ④ boş restoran — S0–S16 (0,0–136,0)
BEDEL           pas + şantiye: S2'de eski camlar, S3'te pas, S15'te vinç + telehandler + kamyonlar + kasalar gider; G20'de aynı yerde
                ışıklı restoran
AÇILIŞ          nesne: vinçte asılı paslı vagon · eylem: ilk karede iniyor · ipucu: hazır tabliye + önündeki dirsekler · MERAK
                SORUSU: "Bu vagonu neden buraya koyuyorlar?" · İKİNCİ SORU: "Önündeki boş çerçeve neye dönüşecek?"
İŞLEV ANI       S16 (128,0–136,0) ışıklar · S17 (136,0–144,0) ilk konuklar · S18 (144,0–152,0) terasa çıkış · S19 (152,0–156,0) çift
                camda · 156,0–160,0 tutuş
LOOP RHYME      G0 vagonun altındaki 1 m boşluk ↔ G20 çiftin altındaki cam ve uçurum · kaya aynı x'te
OMURGA (20)     indirir · çözer · söker · sıyırır · boyar · kaplar · camlar · bağlar · bağlar · çatar · döşer · camlar · çevirir ·
                döşer · donatır · boşaltır · yakar · getirir · canlandırır · tamamlar
SES             MUSIC YES — none 0–24 s, rises 24–88, lightens for the glass 88–96, steps back 120–144, main theme 144–160 (❷ C2 · ❺ C1)
TESLİM          END CARD NO · SPEED 1x · 160,0 sn · SECOND STATION YES (S14, 112–120, declared) · REAL TIME (S18–S19) declared ·
                ON-SCREEN TEXT NO
AI BEYANI       YAYIN_PAKETI §DESCRIPTION (sahibin "This is a cinematic architectural concept, not footage of a real construction
                project.") + sabit beyan bloğu + Studio "Altered content = EVET"
KAPAK           THE_LAST_CARRIAGE_KAPAK.md — G20'den, bölünmüş yerleşim YOK · varsayılan "THE LAST CARRIAGE" başlıklı, yazısız yedek
PROMPT KAPISI   python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_LAST_CARRIAGE → BLOCK 0 · FIX 2 (12.10.2026) — ikisi de
                PLAN §ÜRETİM ÖNCESİ DURUM'da beyanlı (araç kutu seti · düz ızgara)
```

---

## 9. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) + ⑨ iki istasyon tilt eşleşmesi + ⑩ rejim G · sonuç günlük §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  00_ANALIZ/02 §3 — kamera (28 mm · h 11 · tilt 14°) · vagon %56 · cam yukarıdan okunuyor mu · kanyon derin mi ·
                  kaya (157 px) · iç kamerada pencereden kaya
⛔ PİLOT ÜÇLÜ     ① G20 + G19 + G18 + S18 + S19 · ② G0 + G1 + S0 · ③ G11 + G12 + S11 — PLAN §PİLOT ÜÇLÜ · sonra S3, S4, S14, S16
⛔ USTA KARE      G20 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu · gök mavi mi (siyah değil) · cam okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil); kaya 157 ±2 px · vagon 503 / 1586 ±2 px · iç kareler
                  yalnız birbirine
⛔ GÜNLÜK         klip başına satır + İSTASYON sütunu; günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a; 1920×1080 · 160,0 sn · kart YOK)
⛔ İHRAÇ          bash araclar/ihrac_kontrol.sh — süre 160,0 · kart YOK · müzik VAR · yazı YOK · final tutuşu SSIM ≥ 0,90 [DERS 63]
⛔ KAPAK KANITI   ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
⛔ SÜRE / KLASÖR  160 sn yatay_2_dk bandının dışı — sahip kararı (hikâye SAPMA ②)
```
