# 🎶 THE_GRAND_REVIVAL — MÜZİK

**Kaynak:** `MUZIK_VE_KAPAK.md` §1 · kart A adım 9 · ses hedefi `KURGU_VE_TESLIM` §4 · yatay hat müzikli (sahip 05.10.2026)

```
TEMPO         120 BPM — HESAPLANIR, seçilmez: ölçü 2,0 sn · 8,0 sn sahne = 4 ölçü · kesme ölçünün 1. VURUŞUNDA [A2-e]
SÜRE          725,0 s = 720,0 sahne bloğu + 5,0 kart — son akor 712,0'da (S89) basılır, kart boyunca tutulur, 725,0'da söner;
              ani kesilme YOK
KESMELER      8,0 · 16,0 · … · 712,0 (89 kesme) — her biri ölçü başı · 12 oda kesmesi: 80 · 136 · 240 · 336 · 432 · 528 ·
              584 · 640 · 688 · 696 · 704 · 712
MÜZİKSİZ PENCERE  0,0–8,0 s (S0 tamamı): yalnız kanepe ayaklarının taşa sürtmesi, arabanın tekerleği, ağustosböceği, rüzgâr
KATMAN = ODA ⭐ [§1.2]  her oda kesmesi yeni bir ses rengi getirir; oda içinde katman DEĞİŞMEZ (12 dk'da 9 renk):
              0,0   ön cephe     → müziksiz, 8,0'da keçeli piyano nabzı (tek nota)
              80,0  hol          → + yumuşak ahşap tıkırtı (düşük perküsyon)
              136,0 salon        → + sıcak orta armoni (harmonium)
              240,0 yemek odası  → + alçak çello pedalı · BÖLÜM 2
              336,0 mutfak       → + kısa marimba figürü (ritmik, tezgâh işinin altında)
              432,0 yatak odası  → perküsyon ÇEKİLİR · piyano + çello, daha yumuşak
              528,0 giyinme      → + pizzicato yaylılar
              584,0 banyo        → + celesta (su yok — yalnız renk)
              640,0 veranda      → + çekilen gitar · altın saat genişliği
              688,0 AKŞAM        → ⭐ İNCELİR: önce perküsyon, sonra marimba ve pizzicato çekilir — yalnız piyano + ped
              712,0 ilk yemek    → tek sakin çözülme akoru, kart boyunca tutulur
SUB-BASS      55 Hz + oktav eşlikçisi 110 Hz (telefon hoparlörü sub'ı çalmaz)
VURUŞ NOKTASI dört: 8,0 (sarmaşık iner — ilk büyük sonuç) · 208,0 (S26 ilk ağır yük, gerçek zaman — müzik nefes alır) ·
              480,0 (S60 king yatak — BÖLÜM 3 açılışı) · 712,0 (ilk yemek — çözülme) — az olan güçlüdür
G KLİPLERİ    S26 · S34 · S48 · S60 · S77 (gerçek zaman): katman eklenmez, müzik bir ölçü boyunca incelir, ağır yükün sesi öne
SON 32 SN     S86–S89: avize · lambalar · mavi saat · yemek — her ışık bir kesmede, müzik her kesmede bir katman AZALIR
SES HEDEFİ    −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP · mono uyumlu (alt uç merkezde)
⚠️ LİSANS     POLITIKA_VE_RISK — müzik lisansının üç boşluğu (araç · lisans türü · kanıt) dolmadan müzikli video
              YAYINLANMAZ: ⬜ sahip doldurur
```

---

## 🎼 MÜZİK PROMPTU — tek parça, 725 saniye [§1.4 iskeleti]

```
TOOL: ⬜ (sahip seçer — lisansı ticari kullanıma açık olan; 12 dakikalık tek parça veremiyorsa oda bloklarıyla üretilir,
      her blok ölçü başında birleşir, tempo ve ton aynı)
GENRE: warm minimal documentary post-classical — felt piano, harmonium, low cello, marimba, pizzicato strings, celesta, nylon guitar
TEMPO: 120 BPM, 4/4, bar = 2.0 s, strict and bar-aligned. Duration 725 seconds. No tempo change. One key throughout.
No lyrics. No vocals. No melody line that sings over the picture; motifs are short and repeat.

INSTRUMENTATION — one new colour per room, entering only on the bar line of that room's cut:
  1. site ambience only, no music                          (0–8 s)
  2. felt piano, one soft repeated note pulse                (8 s · the ivy comes down)
  3. soft wooden clicks, a low muted drum                    (80 s · the entrance hall)
  4. warm harmonium in the middle register                   (136 s · the living room)
  5. low cello pedal                                         (240 s · the dining room)
  6. a short dry marimba figure                              (336 s · the kitchen)
  7. percussion withdraws; piano and cello only, softer      (432 s · the bedroom)
  8. pizzicato strings                                       (528 s · the dressing room)
  9. a light celesta colour                                  (584 s · the bathroom)
 10. plucked nylon guitar, wider and golden                  (640 s · the veranda at sunset)
 11. thinning: percussion, marimba, pizzicato drop out       (688–712 s · the lights come on, one room per cut)
 12. one calm resolving chord, held through the end card      (712–725 s)

DYNAMIC MAP — one line per room (cuts on bar 1):
  0–80 s    front: no music for 8 s, then the piano pulse under scraping, brushing and tile sounds
  80–136 s  hall: clicks join; plaster, tile and ladder sounds underneath
  136–240 s living room: harmonium; at 208 s the music breathes out for one bar while four people carry a stone table
  240–336 s dining room: cello pedal; at 272 s the long table comes in at real pace — one bar of near silence
  336–432 s kitchen: marimba figure; at 384 s the stone worktop is lowered on slings — the figure stops for one bar
  432–528 s bedroom: softer, no percussion; at 480 s the bed base is carried in at real pace
  528–584 s dressing room: pizzicato, light and even
  584–640 s bathroom: celesta colour; at 616 s the bathtub is carried in at real pace
  640–688 s veranda: guitar, golden and wide as the sun sets
  688–712 s evening: one layer leaves at each cut as the hall, the living room and the front windows light up
  712–725 s first dinner and end card: one held chord, chairs drawn on stone, a plate set down; natural decay, no hard stop

SYNC RULE: every visual cut lands on beat 1 of a bar; a new layer enters only on a room cut, never inside a shot.
The six real-time clips (208, 272, 384, 480, 616, 712 s) never add a layer; they thin the music so the weight is heard.

MIX: mono-compatible — low end centred; every element below 150 Hz is doubled by its own upper harmonics at roughly
100, 150 and 200 Hz so the fundamental is implied rather than required. Target −14 LUFS · −1.0 dBTP.

REFERENCE FEEL (feel only, never quoted): the patience of Jóhann Jóhannsson's documentary scores; the warmth of
Ólafur Arnalds' felt piano.

NO vocals, NO lyrics, NO braam, NO riser, NO reversed cymbal, NO whoosh, NO tempo ramp, NO fireplace crackle.
```

> Referans hissi verilebilir, **alıntı verilemez.**

---

## 🔊 SES YATAĞI — diegetik, müziğin altında sürer [A1-c]

```
00:00–01:20  ön cephe: kanepe ayaklarının taşa sürtmesi · sarmaşık yırtılması · fırça ve kova · kiremit · cam ünite · taş yol
01:20–04:00  hol ve salon: sıva malası · traverten · boya rulosu · parke çekici · halı rulosu · kumaş hışırtısı
04:00–07:12  yemek odası ve mutfak: taş zemin · avize zinciri · sandalye ayakları (her biri ayrı) · dolap menteşesi · taş üstüne taş
07:12–10:40  yatak, giyinme, banyo: yumuşak sesler — şilte, kumaş, ahşap kapak, seramik; ağustosböceği öğleden sonra artar
10:40–11:28  veranda: ahşap döşeme · dış mobilya · akşam kuşları
11:28–12:05  akşam: kapının tok sesi · elektrik düğmesi YOK (ışık sessiz yanar) · sandalyelerin taşta hafif sürtmesi, tabak tıkırtısı
KESME KÖPRÜSÜ oda kesmesinde ortam sesi bir ölçü içinde değişir (iç ↔ dış filtresi) — sıçrama değil; aynı oda içinde yatak sürer
İNSAN SESİ    konuşma YOK · ekip yalnız anlaşılmaz uğultu · S89'da iki kişinin sesi yok, yalnız sofra sesleri
```
