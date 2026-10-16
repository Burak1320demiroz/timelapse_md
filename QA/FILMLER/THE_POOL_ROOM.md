# THE_POOL_ROOM — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 8 × 8,0 sn = 64,0 sn (⚠️ sahip istisnası 16.10.2026) · paylaşım 2x → 32,0 sn
plan: dikey_shorts/THE_POOL_ROOM/THE_POOL_ROOM_DIKEY_TIMELAPSE.md (16.10.2026 · 8 sahne · KAPAK KARTI YOK)
üretim günlüğü: dikey_shorts/THE_POOL_ROOM/THE_POOL_ROOM_URETIM_GUNLUGU.md — ⛔ BOŞ (tek satır yazılmadı)
yayın dosyası: ~/Downloads/THE_POOL_ROOM.mp4 · sha256 df429568b21f · 32,02 sn · 2160×3840 · 30 fps · ses var · 2x
kaynak klipler: ~/Downloads — 8 × 8,0 sn (24 fps) · S0–S2 1080×1920 · S3–S7 720×1280 (⚠️ karışık çözünürlük)
master: YOK (1x master dışa aktarılmadı; klipler doğrudan 2x kurguya girdi)
kapak: ~/Downloads/"Bu Havuz Ev Salonuna Dönüştü.png" (941×1672) — G8'den DEĞİL, aynı görsel yayında kart olarak var
koşu tarihleri: 16.10.2026 (beş mercek, sahip koşusu) · ajan ölçümü 16.10.2026

## ⭐ AJAN ÖLÇÜMÜ — merceklerden ÖNCE okunur
ffprobe · kare farkı (54×96 gri) · `araclar/klip_eslestir.py` (bu kayıtla yazıldı) · kare panoları ajan gözüyle.

```
YAYIN KURGUSU (2x)        kaynak                         ölçüm
0,00 –  2,70   S0 BOŞALTIR    kaynağın son ~2 sn'si KIRPILMIŞ   klip_eslestir ⚠️ (%90 noktası yok)
3,00 –  6,97   S1 TEMİZLER    tam                              ✅
7,00 – 10,97   S2 DİZER       tam                              ✅
11,00 – 14,97  S3 DÖŞER       tam                              ✅
—              S4 CAMLAR      ⛔ YAYINDA YOK (5 noktadan 1'i — yalnız ortak zincir karesi G5)
15,00 – 18,97  S5 DÖŞENİR     tam                              ✅
18,37 – 22,53  S6 YANAR       tam · TIK 19,70 TEK KAREDE (parlaklık 78 → 87, bir kare) ✅
22,83 – 27,03  S7 KARARIR     tam ama 4–8 sn tutuşu erimeyle örtülü
25,1  – 27,2   ERİME (dissolve) S7 → kart · parlaklık 56 → 118
27,2  – 32,02  ⛔ SABİT KART  "THIS WAS A POOL" · 4,8 sn · fark 0,0 (donmuş kare)
```

```
⛔ PLAN ↔ DOSYA UYUŞMAZLIKLARI
① KART       ⭐ SAHİP KARARI (16.10.2026: "videoyu 2x yaptım ve sona kapak koydum") — ama plan "⛔ KAPAK KARTI YOK"
             diyor, beyan güncellenmedi · dosyada 2,1 sn erime + 4,8 sn yazılı kart. Kart G8 değil: alçak kamera, gün
             ışığı, geniş merdiven, saksılar, kanal suyla dolu gibi — başka dünya [DERS 30 · 63]. Finalin tutuşu
             (S7 4–8 sn = yayında 24,8–26,8) erimenin içinde kaldı.
② KLİP       8 klip üretildi, 7'si kurguda (sahip beyanında geçmiyor — kasıtlı mı soruldu). S4 CAMLAR (filmin özgün anı) yok → 14,97'de açık kanal, 15,00'te cam
             yerinde: iş BELİRİR. S4 kaynak klibinin kendisi arızalı (aşağıda E04) — düşürülmüş, yeniden üretilmemiş.
③ ÇÖZÜNÜRLÜK teslim 1080×1920 olmalı · dosya 2160×3840 · kaynaklar 1080×1920 ve 720×1280 karışık (plan: "aynı
             model/çözünürlük/fps") → ihrac_kontrol ② BLOCK verirdi.
④ SÜRE       sahne bloğu ≈ 25–27 sn (plan 32,0) · kart eklenince dosya 32,0'a "denk" geliyor — süre ölçümü uyumsuzluğu
             saklıyor.
⑤ KAYIT      üretim günlüğü boş · ihrac_kontrol / kesme_kontrol / qa_paket koşulmamış (ölçülmüş olgular bloğu yok).
```

```
✅ TUTANLAR (ölçüldü)
· kadraj kilidi — dokuz karede uzak duvar, kapı, kemerler, kobalt bant aynı (❶ 10 · ❸ 10 ile uyumlu)
· S6 tık TEK KAREDE (19,70) · üç lamba SAYI 3 · cam koşuda lacivert şerit gece net okunuyor (lit21 karesi)
  → plan §PİLOT (a) telefon testi bu kadrajda GEÇMEYE ADAY (gerçek telefonla yine bakılmalı)
· G1'den sonra çanakta mavi su YOK → plan RİSK ② ("pool" → su) bu filmde GERÇEKLEŞMEDİ (1 film, kural değil)
· zaman tek yönde: sabah sağ lekeler → öğle → ikindi sol → mavi saat → gece (❷ PASSING ile uyumlu)
```

## ⭐ PROMPT ↔ EKRAN — sahne sahne (kaynak klip, 8 sn · ajan kare panosu · rapor eşleşmesi)

| S | prompt ne istedi (MOTION FOCUS / saniye) | ekranda ne oldu (kaynak sn) | tuttu mu | rapor ne dedi | olay · ders |
|:-:|---|---|:-:|---|---|
| 0 | pompa halkası ilk karede · su 1–5 sn rıht rıht iner · üç lamba birlikte çıkar · tanık çizgi · 6,5–8 palet | su 0–2 sabit, **2→3 sn'de silindi** · tabanda iki siyah GİDER deliği · halka/tanık çizgi/lamba çıkışı yok · palet 5–7 ✅ | ❌ / teslimat ✅ | ❶ cat 6 "drained without pumping" ✓ | E11 · DERS 92 · 93 |
| 1 | pompa 0–2 sn arabayla çıkar · torbalar 2–4 · temiz bant 4–7 sn yakından uzağa | torbalar ✅ · **2→3 sn'de bütün çanak temiz** · 4–8 sn iki işçi palette bekliyor | ❌ zaman | ❶ cat 6 "rapid" ✓ · ❸ "no idle" ✗ | E10 · DERS 92 |
| 2 | kasetler sıra sıra 1–5 · kanal açık · LED + priz 6–7 · meşe bağı 7–8 | açık çelik ızgara **2,0–3,5 sn**'de tamam · "yalıtım" gevşek kutu, sonra kayboldu · kanal ✅ · meşe arabası 6 ✅ | ❌ malzeme + zaman / teslimat ✅ | ❶ ❷ ❸ "grid instantly" ✓ · ❹ "section by section" ½ | E03 · DERS 87 · 92 |
| 3 | meşe 1–6 sn yakından uzağa · lip · sandık 7–8 takozlara | meşe **≈ 4 sn**'de bitti, SAĞDAN sola yayıldı · lip ✅ · sandık 6 sn'de ÇUKURA indirildi (plan: çevrede) · 0–3 sn uzak duvar tepesinde prompt dışı yanan spotlar | ½ | ❹ "progressively" ✓ | E10 · E12 · DERS 92 |
| 4 | üç panel vantuzla, merdivenden, lip'e · 5,5–7 son panel · modüller 7–8 | kanaldan kat kat geniş TEK levha · aşıktan sarkan kaldırıcı · klip başa döndü → **kurgudan çıkarıldı** | ❌ | ❶ cat 8 / ❹ "source NONE" (kesmeyi okudular) | E02 · E04 · DERS 86 · 88 |
| 5 | iki işçi modülleri TEK TEK · eşya 4–6 · araba + sandık + bir işçi çıkar · gün batımı | **4 işçi**, iki modül aynı anda · modül sol yana konup kalktı · araba çukura indi · oda ≈ 4 sn'de tamam · gün batımı 3–8 ✅ | ½ | ❶ "sofa pops" ✓ | E05 · DERS 89 · 92 |
| 6 | el 0–2 · TIK 2,0 tek kare · akkor ~1 sn · tutuş 4–8 | TIK ≈ 1 sn (kaynak), yayında 19,70 **tek kare** ✅ · işçi sırtı dönük, sabit ✅ · üç lamba, mavi çizgi, lambader ✅ | ✅ | ❷ cat 5 dikiş sıçraması ½ · ❺ "final beat PASS" ✓ | E06 (kabul) |
| 7 | işçi 0–1 çıkar · gök 1–4 koyu laciverte · camlarda yansıma · 4–8 tutuş · G8 GECE | işçi 0–2 çıktı (kapı kanadı açıldı, ardı aydınlık) · gök koyulaşmadı, yansıma yok · **6–8 sn ışıklar söndü, gök ağardı, saksılar + battaniye belirdi** (G8 gündüz) | ❌ | hiçbiri (erime + kart örttü) | E09 · E07 · DERS 91 |
| kurgu | 8 × 4 sn @2x, kart YOK | 7 klip, S0 kırpık, +2,1 sn erime +4,8 sn kart (sahip kararı) | — | ❹ ❺ kartı gördü · ❶ ❷ ❸ görmedi | E01 · DERS 85 · 90 |

```
ÖZET   Prompt'un MEKÂN dili (kadraj · çapalar · sayım: üç lamba, bir merdiven, bir kapı) TUTTU — dokuz karede kayma yok.
       ZAMAN dili (saniye takvimi) TUTMADI — ana iş her klipte erken bitti (DERS 92). MALZEME dili iki yerde koptu:
       "framed cassette + infill" (DERS 87) · ölçüsüz "glass panel" (DERS 88). KADRO dili bir yerde koptu (DERS 89).
       Uç kare G8 plana bağlanmadı (DERS 91). Prompt'un ışık finali (S6) tam tuttu.
```

## MERCEKLER
| mercek | durum | puan | hüküm | ham | en ağır üç bulgu (m:ss.s) · ajan notu |
|---|---|:-:|---|---|---|
| ❶ GÖRÜNTÜ | YANLIŞ GİRDİ (D1) + SIZINTI | — | TIMELAPSE · MELTING | THE_POOL_ROOM_Q1_GORUNTU_HAM.md | "0:16 grid appears instantly" (gerçek: yayında 7,5→8,0 · E03 ✓) · "0:32 sofa pops" (E05 ✓) · ⛔ C5 kartı görmedi · "no figures" yanlış |
| ❷ ZAMAN VE KESME | EKSİK (ilk üç satır yok) | — | PASSING · TIME | THE_POOL_ROOM_Q2_ZAMAN_KESME_HAM.md | "0:20 exposure jump" (ölçülen 18,83 dikiş sıçraması 76 → 72 ✓ yakın) · ⛔ 0:28–0:32 "night hold" = kart |
| ❸ ŞANTİYE | SIZINTI (QA_SPEC kapı sayısı) | — | SAME WORLD · WORKING | THE_POOL_ROOM_Q3_SANTIYE_HAM.md | 0 kusurlu dikiş dedi · ⛔ kartı ve düşen S4'ü görmedi · S5'teki 4 işçiyi saymadı — ⚠️ ŞİŞİK |
| ❹ İNŞA | YANLIŞ GİRDİ (PNG adı · 27 klip) | — | SAME · BUILT · INVITED | THE_POOL_ROOM_Q4_INSA_HAM.md | ⭐ kartı ve metnini DOĞRU gördü · "glass source seen NONE" (E02 ✓) |
| ❺ TESLİM | TAM | 10,0 | ENDS | THE_POOL_ROOM_Q5_TESLIM_HAM.md | kartı gördü, C2 10/10 verdi (kart başka dünya → ajan itirazı E01) · 27 "klip" (D2) — ⚠️ ŞİŞİK |
FİLM PUANI  10,0 · N=1 (yalnız ❺)          ÖLDÜRÜCÜ  — (hiçbir mercek öldürücü hüküm vermedi)
⚠️ PUAN BAĞLAYICI DEĞİL: tek TAM mercek (❺) 10/10 verdi; ajan ölçümü üç plan uyuşmazlığı (kart · düşen klip · çözünürlük)
ve iki üretim arızası (E03 · E05) buldu. Karar ölçüme göre verilir, puana göre değil [DERS 90].

## DOĞRULAMA
- Geri okuma: ❶ ✗ (satırlar yok) · ❷ ✗ (satırlar yok) · ❸ ✓ THE_POOL_ROOM.mp4 / NONE / 8 · ❹ ✗ input_file_0.png / NONE / 27 · ❺ ✓ THE_POOL_ROOM.mp4 / NONE / 27
- D1: ❶ 1:04.0 > 32,02 sn → YANLIŞ GİRDİ · D2: ❹ ❺ 27 klip (saniye sayılmış) · ❸ ❷ 8 klip (7 + kart, kabul) · D4: kesme
  damgaları ölçülemedi (zincir dikişleri görünmez; klip_eslestir sınırları kullanıldı) · D5: plan KART YOK ama dosyada kart
  VAR — mercek değil dosya hatalı.
- Sızıntı taraması: ⛔ ❶ ANCHORS / FRAME TABLE satırları QA_SPEC §2 sayılarını birebir veriyor (kapı x %23,7–34,4 ·
  y %58,7–72,1 · kemerler %45/%59,5/%73,8 · %86,1 · kobalt %26,9/%54,1 · ufuk %74,3 · coping %13,4/%86,6 · üst band
  %92,5–100) ve ❸ aynı kapı aralığını yazdı. Bu sayılar planın tilt formülünden TÜRETİLDİ, videodan ölçülemez →
  ❶ ❸ SIZINTI. Kör mercekler planı/SPEC'i gördü: aynı Gem/proje ya da aynı sohbet kullanılmış olmalı [QA_KOSU §1].
  ⚠️ ❷ sayı alıntılamadı ama aynı ortamda koşulduysa körlüğü de şüpheli.

## DOKÜMAN

### ❶ GÖRÜNTÜ
1. **Boşaltma ve kuruma takvimi:** S0 (06:30–08:30) pompa suyu iner, iki birikinti kalır; S1 (08:30–10:30) el fırçası ve bezle temizlik, çanak kurur. Yayında S0'ın son ~2 sn'si kırpıldı, temizlik kaynakta ~2,5 sn'de bitti → "hızlı" okuması haklı.
2. **Izgara parça parça mı:** Parça parça — "rows from the near end back toward the steps", 0–5 sn. Kaynak klipte ızgara 2,0–3,5 sn'de yayıldı (yayında 0,75 sn) → E03.
3. **Mobilya önceden mi, kapıdan mı:** Kapıdan, arabayla; modüller G5'te arabada beklemeliydi. G5 yayında yok (S4 düştü) → modüller önceden görünmedi.
4. **Geceye geçiş:** S6 18:30 + 8 sn gerçek zaman (gök sabit) · S7 rejim A 10 dk, güneş −5,7° → −7,6°.
5. **Kanal LED'i lambalarla aynı anda mı:** Evet, tek düğme, tek kare (S6 2,0 sn). Ölçüldü: 19,70'te tek kare ✅.

### ❷ ZAMAN VE KESME
1. **Güneş açıları:** G0 95°/+5,7° · G1 116°/+27,8° · G2 147°/+45,1° · G3 192°/+49,4° · G4 230°/+37,4° · G5 255°/+17,0° · G6–G7 275°/−5,7° · G8 277°/−7,6°.
2. **Sabah havası:** Açık ekinoks sabahı, ışık cam çatıdan serin; bulut yazılmadı.
3. **Kesme aralıkları:** S0–S5 2 saat · S6 8 sn (gerçek zaman) · S7 10 dk.
4. **Tutulan saat:** S6 (rejim G) — gök değişmez, yalnız yapay ışık.
5. **Işık takvimi:** S6 2,0 sn: üç lamba + LED tek kare · lambader ~1 sn ısınma.

### ❸ ŞANTİYE
1. **Boşaltma süresi:** 2 saat (S0) + temizlik 2 saat (S1).
2. **Izgara modülleri:** Hazır kasetler paletle gelir, yerinde sıra sıra dizilir (S2).
3. **Teslim yolu:** Her parça servis kapısından arabayla girer, eski çini merdivenden elle iner; araba çevrede (terrazzo) kalır. Yayında araba 16,5'te çukura indi → E05.
4. **Işık takvimi:** S6 tek düğme (yukarıda).
5. **Final tutuşu işçi çıktıktan sonra sabit mi:** Evet — S7 4–8 sn oda boş, ışıklar sabit. Yayında bu tutuş erime + kartla örtüldü → E01.

### ❹ İNŞA (mod V — sorular mühendislik; plan kapsamı dışı olanlar işaretli)
1. **Taşıma sınırı:** Planda sayı yok; sabit yorum: 1,5 m su ≈ 14,7 kN/m², oda yükü bunun küçük bir kesri.
2. **Nem bariyeri:** Planda yok — kasetlerin altında havalandırılan boşluk sabit yorumda.
3. **Lamba güç yolu:** Planda yok; sabit yorum: düşük voltajlı, sızdırmaz niş armatürleri.
4–5. **Tuğla/cam nem işlemi · havalandırma:** Planda yok.

### ❺ TESLİM
1. **İmar/yük şartı:** Plan kapsamı dışı.
2. **Süre ve tempo:** 8 × 8 sn, 2x; iş temposu S0–S5 B rejimi, S6 gerçek zaman tık, S7 gece.
3. **Ses:** Müzik yok, diegetik yatak (plan §SES) — yayının sesi dinlenmedi (ELLE kontrol bekliyor).
4. **Kanal ışığı alternatifi:** Pilot (a) telefon testi düşerse cam çıkar, final yalnız üç lambayla kalır.
5. **Dağıtım:** Apex AI Timelapse — YouTube Shorts · TikTok · Instagram (KAPAK dosyası §YAYIN PAKETİ).

## OLAY TABLOSU
| olay | zaman (yayın 2x) | ne oldu (görünen) | mercekler | kanıt | karar |
|---|---|---|---|---|---|
| E01 | 25,1–32,0 | ⭐ SAHİP KARARI: kapak sona kart olarak eklendi (2,1 sn erime + 4,8 sn "THIS WAS A POOL"). Kart başka kameradan başka dünya (gün ışığı, geniş merdiven, saksılar); erime S7'nin gündüze sıçrayan son 2 sn'sini örttü | ❹ ❺ gördü · ❶ ❷ ❸ görmedi | sheet_1s 27–31 · kart = "Bu Havuz Ev Salonuna Dönüştü.png" | plan TESLİM YAPISI'na beyan edilir (kart + erime + kaynak) — kalıcı format mı, sahibe soruldu [DERS 85] |
| E02 | 14,97 → 15,00 | Açık kanal → cam yerinde, tek kesmede; S4 CAMLAR kurguda yok (sahip bilerek çıkardı — klip arızalı) | ❶ (cat 8) · ❹ (glass source NONE) | klip_eslestir S4 ⛔ | kabul — yeniden üretim yok (sahip) · ders [DERS 86] |
| E03 | 7,5 → 8,0 (kaynak S2 2,0–3,5) | Kaset ızgarası 1,5 sn'de (kaynak) bütün çanağı kapladı; "kaset + yalıtım" açık çelik ızgara + gevşek kutu oldu, kutular klip sonunda kayboldu | ❶ (cat 8) · ❷ (cat 8) · ❸ (cat 8) | s2.png | S2 yeniden — tek rijit panel adı + aktif cephe ≥ 4 sn [DERS 87] |
| E04 | — (kaynak S4 1–5 sn, yayında yok) | Cam: kanaldan kat kat geniş TEK levha meşenin üstünde kaydı; tavandan sarkan zincirli kaldırıcı ve sehpa belirdi; klip başladığı hâle döndü | — (kurguya girmedi) | s4b.png | S4 yeniden — panel ölçüsü kanal açıklığına kilitli, el vantuzu [DERS 88] |
| E05 | 15,0–16,5 | S5'te 4 işçi (plan 2), iki modül aynı anda taşındı; bir modül sol tarafa konup kalktı; mavi araba çukura, meşenin üstüne indi | ❶ (cat 8 "pops") | crops.png alt · half2 16,0–16,5 | S5 yeniden — iki işçi, tek modül, araba çevrede [DERS 89] |
| E06 | 18,83 | S5 → S6 dikişinde parlaklık sıçraması (76 → 72) | ❷ (cat 5 · 0:20) | raw fark | kabul — rejim dikişi B → G beyanlı [P5-c] |
| E07 | 23,0–24,0 | S7'de işçi çıkarken kapıda kanat açılıp kapandı, kapı ardı aydınlık; plan "open doorway, dark beyond" | — | half2 23,0–23,5 | kabul (küçük) — sonraki üretimde "the doorway stays open and dark" |
| E09 | kaynak S7 6,0–8,0 (yayında ≈ 26–27, erime altında) | G8 gündüz üretilmiş (plan: gece) → son 2 sn'de lambalar söndü, gök ağardı, 4 saksı + battaniye + yuvarlak sehpa belirdi | — (örtüldü) | g8kars.png (S6 son · S7 6 sn · S7 son · g8_2K) | G8 G7'den düzenlemeyle GECE yeniden → S7 yeniden [DERS 91] |
| E10 | S0–S3 · S5 | Ana dönüşüm her klipte 2–4 sn'de bitti, kalan süre bekleme/ışık; 2x'te ana iş 0,5–1,5 sn ekranda | ❶ cat 6/8 · ❷ cat 8 | k01 · s2 · k35 | plan ritmi yeniden: ana iş 0–4, ikinci iş 4–8; gerekirse G ara hâl [DERS 92] |
| E11 | kaynak S0 2→3 | Su bir saniyede silindi, tabanda iki gider deliği belirdi, pompa halkası yok | ❶ cat 6 | k01 üst satır | G1'de sığ su ara kotu + rıht rıht su çizgisi [DERS 93] |
| E12 | kaynak S3 0–3 | Uzak duvar tepesinde prompt dışı yanan spotlar belirip kayboldu | — | k35 üst satır | küçük — S3 yeniden üretilirse "the far wall carries no fittings above the windows" |
| E13 | kapak | Kapak provası: başlık y ≈ 150–460 (çekirdek dışı) · 4:5'te "THIS WAS" kesik · 1:1'de yalnız "A POOL" · dosya 941×1672 | — | kapak_prova PROVA_PANOSU | kabul (yeniden üretim yok) · ders [DERS 94] |
| E08 | tüm film | Kaynak çözünürlüğü karışık (1080×1920 ↔ 720×1280), teslim 2160×3840 | — | ffprobe | ihraç yeniden: tek çözünürlük, 1080×1920 [DERS 85] |

## KARAR

⭐ **SAHİP KARARI 16.10.2026: YENİDEN ÜRETİM YOK — yeni filme geçiliyor.** Film bu hâliyle kapandı; aşağıdaki
"yeniden üretilecekler" listesi uygulanmayacak, kayıt olarak kalır. Dersler 85–93 yeni filmlerin planına iner.
S4 düşürmesi bilinçliydi (sahip: "işçiler kocaman camı getirip yere bıraktı, sahne sonunda cam bir anda yok oldu ve
ortaya cam geldi"). Kapak kartı yeni kalıcı kuraldır: her filmin sonunda kapak.

- **Yayın durumu:** Kart sahip kararıdır (E01) — plan beyanı güncellenince teslim uyuşmazlığı kalkar. Kalan teslim sorunları: düşen S4 (E02), çözünürlük (E08), kartın G8'den değil kapak görselinden gelmesi.
- **Yeniden üretilecekler:** G8 (gece, G7'den düzenleme — E09) → S7 · S4 (cam — E04, plan §PİLOT c′'nin öngördüğü en zor klip) · S2 (ızgara — E03) · S5 (kadro — E05) · S0 (su — E11, G1 ara kotla). Zincir: G4/G5 aynı kalırsa S4 tek başına yeniden koşulur; S2 ve S5 için uç kareler korunur [ONARIM §3].
- **Yeniden kurgu:** kart çıkarılır (ya da planda beyan edilip G8'den üretilir) · S0 tam boy · S4 eklenir · tek çözünürlük 1080×1920 · `klip_eslestir.py` + `ihrac_kontrol.sh` + `kesme_kontrol.sh` sırayla.
- **Kabul edilen:** E06 (beyanlı dikiş) · E07 (küçük).
- **QA yeniden koşulur:** kurgu düzeldikten sonra `qa_paket.sh --hiz 2` ile; ❹ ❺ plan + QA_SPEC + kapakla (mod D); ❶ ❸ yalıtım kontrolüyle (sızıntı şüphesi).
- **Tutanlar:** kadraj · tık · üç lamba · cam koşu gece okunurluğu · su risk ② gerçekleşmedi.

## DERS
- DERS 85 — Kapak sona kart olarak eklendi (sahip kararı) ama planda beyan yok, kart başka dünyadan, finalin kusurunu örttü
- DERS 86 — Arızalı klip kurgudan düşürüldü, zincirde iş "belirdi": klip ↔ yayın eşleşmesi (`klip_eslestir.py`)
- DERS 87 — "Çerçeve + dolgu" iki nesne oldu, ızgara tek desen olarak yayıldı: rijit tek panel adı, ≥ 4 sn aktif cephe
- DERS 88 — Cam panel: kanaldan geniş tek levha ve tavandan sarkan kaldırıcı
- DERS 89 — İki kişilik yük × çok parça: kadro ikiye katlandı, araba çukura indi
- DERS 90 — Ölçülmüş olgular olmadan koşulan mercekler kartı kaçırdı ve 10/10 verdi
- DERS 91 — Usta kare plana uymadı (gece → gündüz); son klip farkı son 2 saniyeye yığdı
- DERS 92 — Ana dönüşüm klibin ilk yarısında biter; saniye takvimi tutmaz, geç teslimat tutar
- DERS 93 — Su seviyesi inmedi, silindi; tabanda prompt dışı gider delikleri belirdi
- DERS 94 — Kapak başlığı üst bantta: profil kırpmasında film adı kesildi
