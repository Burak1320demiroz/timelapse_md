# 🔍 THE_OLD_ROAD — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM · ⑥ GEÇİŞ · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER).
> ⛔ ① KARE · ③ ZAMAN · ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET · ⑫ KATILIK merceklerine **VERİLMEZ** — o altısı
> dokümansız koşar [AGENTS değişmez ⑦ · QA/00_README mod sistemi]. Yorum yok, yalnız ölçülebilir kilitler.
> Sayıya çevrilemeyen kilit, kilit değildir; tariftir.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_OLD_ROAD <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].

---

## 0. KÜNYE

```
FİLM          THE_OLD_ROAD — derin bir dağ vadisine İTİLEREK kurulan 420 m'lik beton viyadük; vadi ağzındaki kaya
              mahmuzundan tek sabit istasyon, eski yolun on dört virajı ve taş kemer köprü kadrajda
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_2_dk_filmler

TESLİM YAPISI ⭐ SAHNE BLOĞU  15 sahne × 8,0 sn = 120,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  1 × 5,0 sn          =   5,0 sn              ← SAHNE DEĞİL
                 TOPLAM                          125,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR ve devamlılık karşılaştırmalarına GİRMEZ.
                 Ayrı denetlenir: "kart, son sahnenin (S14) sonundaki yapının AYNISINI mı gösteriyor?"

SAHNE SAATLERİ  sahne n = n × 8,0 → (n+1) × 8,0   ·   S0 0,0–8,0 · … · S14 112,0–120,0 · KART 120,0–125,0
                (120 BPM · ölçü 2,0 sn · 5 ölçü/sahne · her kesme ölçü başında)
PART GRID       — (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)
⛔ DÜZ IZGARA   sahip beyanı (14.09.2026). ⑥ METRONOM hükmü BEKLENEN ve KABUL EDİLMİŞ risktir (PLAN §AŞAMA
                MERDİVENİ · DERS 13 · 24); gelirse "beklenen" diye kaydedilir, yeniden üretim sebebi sayılmaz.
                Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]: ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — ölçülünce
   buraya ve PLAN'a yazılır; {5,10} gerekir, {4,6,8} çıkarsa iki-klip hükmü (PLAN §DEĞİŞMEZLER).

YAPI          itmeli beton kutu kesitli viyadük · 420 m · 7 açıklık (60+75+75+75+75+60) · 5 ayak (30/48/60/50/32 m)
              tabliye üstü +64 m · kesit derinliği 4 m · çelik burun 45 m · döküm kesiti 25 m
SAHA          dağ / eğim vadisi (SAHA_VE_IKLIM §3.4) · çapalar: taş kemer köprü · eski yolun 14 virajı · şapel (sol) ·
              kaya kulesi (sağ) · ikiz zirve silüeti · nehir yatağı
ZAMAN YAYI    10 Mart yıl 1 → 23 Kasım yıl 2 = 627 gün ≈ 20,6 ay · film mertebe anlatır: "yaklaşık iki yıl, iki kış" [P1-c]
IŞIK          TEK GÜN 05:05 → 18:35 · Σ rejim 13,5 saat (9 A + 6 B) · takvim SAHADAN (melez rengi · kar çizgisi ·
              nehir · beton yaşı) · ⚠️ ÜSLUPLU SIKIŞTIRMA: "tek günde çekildi" iddiası YOK
KAMERA        MAIN STATION — tek istasyon · h +80,0 m · D_eksen 380 m · D_kenar 190 m · bakış 0° · tilt 0°  (detay istasyonu: YOK)
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G15 usta kare → G14 → … → G0 · her kare zincir_kontrol.sh + kanıt nesnesi ELLE
GÜNLÜK        THE_OLD_ROAD_URETIM_GUNLUGU.md — ⛔ BOŞ (dolmadan bu SPEC'in hükmü yoktur) [DERS 28]
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S14
SANİYE      119,0 (son sahne S14'ün 7,0. saniyesi — son 2,0 sn'lik TUTUŞUN içi [P2-i]; güneş −1°, gök aydınlık [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① VİYADÜKTE AKAN TRAFİK (tabliye çizgisi %45,0 · iki kesintisiz far izi · lamba direkleri %48,8 yanık;
      yapı tamam: beş ayak + kesintisiz tabliye A1 %13,1 → A2 %86,9)
   ② BOŞALMIŞ AMA OKUNUR ESKİ YOL (iki yamaçta 14 viraj, asfalt bandı ve korkuluk seçilir, üstünde araç YOK;
      geçici ekipman GİTMİŞ: çelik burun YOK · geçici destek YOK · döküm hangarı YOK · şantiye yolu kaldırılmış,
      yalnız pale izi kalmış)
   ③ AYNI TAŞ KEMER KÖPRÜ (kanıt nesnesi: x ≈ %44,4 · y %34,2 · ≈64 × 21 px — G0 ile aynı konum ve boy)
   + BEDEL görünür: virajlarda ARAÇ YOK; G0'daki far izi zikzakının yerini viyadükteki tek düz çizgi almış

KOMUT
   ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①②③'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP
   ffmpeg -ss 0.3  -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 kanit_g15.jpg
   İki karede çapalar ① ② ③ ve kanıt nesnesi tam aynı yerde. Işık: BİLİNÇLİ FARKLI (G0 05:05 şafak · G15 18:35 alacakaranlık — tek ışık günü süpürülür; PLAN LOOP satırı).
   ⚠️ Kesintisiz döngü İDDİA EDİLMEZ; bu bir açılış–kapanış kafiyesidir.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=+80 m · D=380 m · tilt 0 · yatay: yüzde = 50 + 118,5·(y−h)/D, ALT kenardan)

| nesne | y (m) | yüzde (alt kenardan) | x (soldan) | px boy | her karede |
|---|:-:|:-:|:-:|:-:|---|
| ufuk (tilt 0) | — | 50,0 | — | — | ✓ |
| ayak kaideleri (nehir kotu) | 0 m | %25,1 | ±%1,0 | — | ✓ G2–G15 |
| tabliye üstü | +64 m | **%45,0** | ±%0,8 | A1 %13,1 → A2 %86,9 | ✓ G5–G15 (uç konumu sahneye göre) |
| lamba direkleri (yapı tacı) | +76 m | %48,8 | ±%1,0 | — | yalnız G14–G15 |
| ikiz zirve silüeti (kadraj tacı) | 3 km | %82,4 | ±%1,5 | orta | ✓ hepsi |
| ⭐ kanıt nesnesi: TAŞ KEMER KÖPRÜ | D 600 m | %34,2 | ±%0,5 | x %44,4 · 64 × 21 px | ✓ BİREBİR (boy dâhil) |
| çapa ① ŞAPEL (SOL) | D 700 m | %61,9 | ±%1,0 | x %28,1 · ≈33 px | ✓ |
| çapa ② KAYA KULESİ (SAĞ) | D 420 m | %45,9–57,5 | ±%1,0 | x %89,7 · ≈122 px | ✓ · göz çizgisi (%50) alt üçte birinden geçer |
| çapa ③ ESKİ YOLUN 14 VİRAJI | iki yamaç | %30–70 bandı | — | asfalt bandı + korkuluk | ✓ hepsi · G15'te BOŞ ama okunur |
| mobil vinç bom başı (döküm alanı) | ≈ +25 m | ≤ %50 | ±%2 | x %0–10 | KARAYA karşı (yamaç) — göğe çıkmaz [DERS 22] |
| paletli vinç bom başı (nehir düzlüğü) | ≈ +20 m | ≤ %40 | ±%2 | x %50–60 | KARAYA karşı — göğe çıkmaz |
| ⛔ tabliye ve kesitler | — | — | — | — | HİÇBİR KAREDE KALDIRILMAZ — itilir [DERS 57] |

```
KAMERA SABİTLİK  ① için: ilk/son kare kayması ≤ 2 px (araç kapısı ②) · film boyunca çapa ① ② konumu ±2 px
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
itmeli beton kutu kesitli viyadük · uzunluk 420 m · tabliye üstü +64 m · kesit derinliği 4 m · genişlik 12 m ·
7 açıklık (60+75+75+75+75+60) · 5 ayak çifti (30/48/60/50/32 m) · döküm kesiti 25 m · çelik burun 45 m ·
geçici çelik destek (x +37,5 m) · geçici menfez geçişi · döküm hangarı + itme yatağı · tırmanır kalıp ·
mobil vinç (döküm alanı) · paletli vinç (nehir düzlüğü) · beton pompası · mikser · damper · finişer · silindir
```

### Yapı yüzdesi ve saha durumu — sahne sahne (② İNŞA · ④ TESLİM · ⑩ SEBEP için)

| S | saat | yapı: eleman + ara hâl (%) | taç yüzdesi (kadraj) | geçici ekipman kadrajda | saha / mevsim taşıyıcısı |
|:-:|:-:|---|:-:|---|---|
| S00 | yapı yok · ilk toprak kesisi | — | eski yol trafiği · taze kesi | dozer | şafak far izleri |
| S01 | kesi uzadı · iki yakada kesi | — | kesi uzunluğu | dozer + low-loader | ilk ışık |
| S02 | temeller · 5 kazık başı | — | kazık başları %25–34 | kazık makinesi · mikser · ekskavatör | geçici geçiş kuruldu |
| S03 | 5 ayak tam + başlıklar | — | ayak başları %43,8 tek hat | pompa · mikser · damper | tırmanır kalıp |
| S04 | döküm alanı + ilk kesit + burun | burun %17 | burun ucu A1'de | mobil vinç · mikser | koyu döküm derzi |
| S05 | tabliye P1 | %23,7 / burun %31,5 | tabliye ucu P1'de | kriko · mikser | ilk itme |
| S06 | tabliye P3 + geçici destek | %50,0 / burun %57,9 | destek %56,6 kuruldu · kar çizgisi iner | kriko · paletli vinç · mikser | kış |
| S07 | tabliye P4 | %63,2 / burun %71,1 | iki itme · kaya bermi dökülür | kriko · damper · ekskavatör | su yükselir, plant çekilir |
| S08 | aynı (itme durdu) | %63,2 sabit | geçici geçiş YOK · berm aşılmış | ekskavatör (bankadan kaya) | sel tepe |
| S09 | aynı | %63,2 sabit | menfez + çapraz + apron yeniden · 2 hazır kesit | ekskavatör · damper · silindir · mikser | hat onarıldı |
| S10 | tabliye P5 | %76,3 / ⭐ burun A2'de %86,9 | iki kesit eklendi, iki itme · burun TEMAS | kriko · damper | burun karşı kenarda |
| S11 | tabliye A2 — beton hat tamam | %86,9 / burun %94,8 | kesintisiz beton çizgi | kriko | ⭐ kavuşma · 2 sn tutuş |
| S12 | burun + destek + hangar SÖKÜLÜR | — | tabliye kalıcı mesnetlere iner | mobil vinç · paletli vinç · low-loader | üç söküm bir arada |
| S13 | üst yapı %0 → %100 | — | membran + asfalt + korkuluk + lamba (%48,8) | finişer · silindir · telehandler | şantiye yolu kalkar |
| S14 | üst yapı tam · lambalar yanık | — | asfalt + korkuluk + direk %48,8 | finişer · silindir · servis kamyonu | şantiye toplandı |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   TAŞ KEMER KÖPRÜ — G0…G15 hepsinde x ≈ %44,4 · y %34,2 · ≈64 × 21 px; zincirde her karede ELLE ✓/✗ (günlük §2)
İKİNCİ ÇAPA     ESKİ YOLUN VİRAJ GEOMETRİSİ (iki yamaçta aynı çizgi) · ÜÇÜNCÜ: kaya kulesi (%89,7) ·
                ⭐ İTME SAHNELERİNDE (G4–G12): ilk dökülen kesitin KOYU DÖKÜM DERZİ — hep en önde, her itmede sağa kayar
⑤ İÇİN          dikiş = KARE (G1…G14): dikişin iki yakası aynı görsel; ⑤ REBUILT hükmü zincir koşulmadı demektir
```

---

## 5. ⑧ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | geçici destek (sling / formwork / scaffold …) | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|:-:|:-:|:-:|
| ayak betonu | mikser + pompa hattı, şantiye yolundan | tırmanır kalıp kademeleri, koyu/açık lift bandı | G2 | G3 | G3 |
| tabliye kesiti | döküm alanında donatı kafesi + kalıp; sel durmasında İKİ kesit birikir (G10) | koyu döküm derzi, itme yatağı, sürtünme mesnedi | G4 | G5–G12 | G12 |
| çelik burun | parçalar döküm alanında, mobil vinç birleştirir | cıvatalı ek plakaları, konsol | G4 | G12 (sökülür) | — |
| geçici destek | parçalar yoldan, paletli vinç kurar; selden sonra YENİ çaprazlar | çapraz bağlantılar, kaya apronu | G7 | G12 (sökülür) | — |
| kaya bermi / apron | damperler dökerek, ekskavatör şekillendirir (S7 · S9) | selde aşılır, sonra apron olur | G8 | G13 (raspalanır) | — |
| kaplama + korkuluk | kamyon + finişer, sol yaklaşımdan | koyu asfalt bandı, kerb çizgisi | G13 | G14 | G14 |

```
⑪ DAVETLİ LİSTESİ: vadi · nehir · taş kemer köprü · eski yol + trafik · şapel · kaya kulesi · ikiz zirve ·
   melez ormanı · beş ayak + tabliye · döküm hangarı + itme yatağı · çelik burun · geçici çelik destek ·
   geçici menfez geçişi · şantiye yolu · tırmanır kalıp · mobil vinç · paletli vinç · pompa · mikser · damper ·
   ekskavatör · silindir · finişer · low-loader · dozer · sürüklenmiş ağaç · korkuluk · lamba direkleri · crew streak
   ⛔ DAVETSİZ SAYILIR: ikinci köprü · ikinci viyadük · kule vinci · tabliyeyi HAVADA taşıyan herhangi bir makine ·
   taş köprüde ağır iş makinesi · vadi tabanında kar · keskin insan figürü · yazı/logo
⑩ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: kesit döküm alanında doğar → itme onu ileri taşır;
                  hiçbir parça gövdenin ÖNÜNDE belirmez; kaldırma yok — ilerleme SÜRTÜNMEYLE olur [DERS 57 · 48]
```

---

## 6. ⑥ GEÇİŞ — kesme listesi ve ses

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn)   (14 kesme, hepsi ölçü başı — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_OLD_ROAD/THE_OLD_ROAD_PLAN.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                120 BPM · müziksiz pencere 0,0–2,0 · katman girişleri 32,0 (pulse) · 48,0 (yaylı) · 88,0 (akor) ·
                     64,0–80,0 katmanlar ÇEKİLİR (sel) · final tutulan akor 112,0–120,0
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G8 (S7 ↔ S8) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si G8 karesinde biter; G8 BOLUM_2'nin ilk görselidir.
ELLE KARE            ffmpeg -ss 64.0 -i teslim.mp4 -frames:v 1 sinir.jpg → tabliye ucu P4 (%63,2) · burun %71,1 ·
                     güneş az 172°/52° · gök kapalı gri tavan — iki yakada AYNI
                     (6/8 dk: b1_son.jpg ↔ b2_ilk.jpg zincir_kontrol.sh — çıkış 2 = dikiş kırık)
⑤ İÇİN               6/8 dk'da bu dikişi hiçbir yarım master GÖREMEZ — bu satır onun yerine geçer.
```

---

## 8. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_OLD_ROAD_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ ÖN GÖRSELLEŞTİRME  kamera · yapı · çapalar · ufuk yan kesiti; kaldırmalar gök/kara burada doğrulanır
⛔ USTA KARE      G15 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kanıt nesnesi ELLE (boy dâhil)
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28 — dört kez ölçüldü]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a)
⛔ KAPAK KANITI   ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 g15_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g15_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
```
