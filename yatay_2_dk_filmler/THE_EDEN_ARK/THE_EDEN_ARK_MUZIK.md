# 🎶 THE_EDEN_ARK — MÜZİK

**Kaynak:** `MUZIK_VE_KAPAK.md` §1 · kart A adım 9 · ses hedefi `KURGU_VE_TESLIM` §4
**Karar:** sahip 05.10.2026 — yatay formatın müziği (dikey shorts'taki "müzik yok" kuralı bu filme UYGULANMAZ;
o kural dikey hatta kaldı). Müzik ses yatağının ÜSTÜNE oturur, onu silmez.

```
TEMPO         120 BPM — HESAPLANIR, seçilmez: ölçü 2,0 sn · 8,0 sn sahne = 4 ölçü · kesme ölçünün 1. VURUŞUNDA [A2-e]
SÜRE          149,0 s = sahne bloğu 144,0 + kapak kartı 5,0 (kartta piyano akoru tutulur, son 1,5 sn yalnız liman sesi)
KESMELER      8,0 · 16,0 · … · 136,0  (17 kesme, her 8,0 sn)   (her biri ölçü başı — kurguda tek tek hizalanır [D-d])
MÜZİKSİZ PENCERE  0,0–8,0 s (S0: sabah limanı — martı bir kez, uzak dalga, zincirlerin gıcırtısı ve kapakların
              tekerlek sesi) · ⭐ İKİNCİ PENCERE 112,0–120,0 (S14 başı: savakların suyu — müzik çekilir, yalnız su)
KATMAN = AŞAMA ⭐ [§1.2]  18 sahnede 6 katman; her katman bir ELEMANLA girer:
              ① 8,0 (S1 · hurda) → düşük, kuru vurmalı nabız (metal)
              ② 24,0 (S3 · boya) → sub-bass dronu (gövde yenilenir)
              ③ 48,0 (S6 · incir) → marimba/kalimba motifi (ilk canlı şey) — ⭐ VURUŞ 1: incirin oturduğu an (≈ 53 sn)
              ④ 72,0 (S9 · ilk kemer) → yaylılar, açık beşli (çatı yükselir) — bölüm sınırında İŞARET YOK
              ⑤ 104,0 (S13 · iskele çekilir) → katman ÇEKİLİR: ① ve ② susar; S14 başında 8 sn müziksiz pencere
              ⑥ 120,0 (S15 · kapı açılır) → piyano + yaylılar geri gelir, tempo AYNI, doku genişler —
                 ⭐ VURUŞ 2: ışıkların yandığı an (≈ 133 sn) · S17 son 2 sn tutulan akor → kartta söner
SUB-BASS      55 Hz + 110–160 Hz oktav eşlikçisi (telefon/dizüstü hoparlörü sub'ı çalmaz)
VURUŞ NOKTASI 2 — ≈ 53 sn (incir oturur) · ≈ 133 sn (ışıklar yanar) — az olan güçlüdür
KIŞ           YOK
SES HEDEFİ    −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP · mono uyumlu (alt uç merkezde)
```

---

## 🎼 MÜZİK PROMPTU — tek parça, 149 saniye [§1.4 iskeleti]

```
TOOL: any instrumental music generator that accepts duration and tempo
GENRE: documentary / minimal / warm organic electronic
TEMPO: 120 BPM, 4/4, bar = 2.0 s. Duration 149 seconds. No tempo change.

INSTRUMENTATION — layers enter with the build, in this order:
  1. silence — harbour ambience only  (0–8 s)
  2. dry low metallic percussion pulse  (8 s)
  3. deep sub-bass drone at 55 Hz with an octave above  (24 s)
  4. soft marimba / kalimba motif, five notes  (48 s; first accent at 53 s)
  5. warm strings, open fifths  (72 s)
  → at 104 s percussion and drone drop out; 112–120 s no music at all
  6. piano and strings return, wider  (120 s; accent at 133 s), held chord from 142 s
  7. end card 144–149 s: the held piano chord decays, last 1.5 s ambience only

DYNAMIC SPREAD — one line per 8 s block (cuts on bar 1):
  0–8 s    (S0):  no music
  8–24 s   (S1–S2): pulse alone, sparse
  24–48 s  (S3–S5): pulse + drone, steady
  48–72 s  (S6–S8): + marimba; accent at 53 s; gentle lift at S8
  72–104 s (S9–S12): + strings; fullest steady texture   [72 s bölüm sınırı — müzikte İŞARETSİZ]
  104–112 s (S13): pulse and drone withdraw, strings thin
  112–120 s (S14 first half): silence — water only
  120–142 s (S14 end–S17): piano + strings, slow and wide; accent at 133 s
  142–144 s (S17): last ≥2 s hold — sustained chord
  144–149 s (END CARD): chord decays to ambience

SYNC RULE: every visual cut lands on beat 1 of a bar; a new layer enters only on a cut, never inside a shot.

MIX: mono-compatible — low end centred; no wide stereo that collapses on a phone speaker.
Target −14 LUFS · −1.0 dBTP.

NO vocals, NO lyrics, NO braam, NO riser, NO reversed cymbal, NO whoosh, NO tempo ramp.
```

> Referans hissi verilebilir, **alıntı verilemez.**

---

## 🔊 SES YATAĞI

```
ORTAM         tersane ve liman: hafif rüzgâr · uzak dalga · bir kez martı · havuz duvarlarında yankı
KESME KÖPRÜSÜ ortam sesi kesmede ATLAMAZ (dikişin iki yakası aynı kare — ses de aynı yatak)
MAKİNE SESİ   rejim A klipte tanınır: zincir ve tekerlek (S0) · torç ve kaynak (S2) · vinç motoru, sapanın gerilişi (S6) ·
              yağmurlama tıslaması (S8) · portal motoru, cam "tok"ları (S9 · S11) · kapı menteşesi (S15) · römorkör
              dizeli ve halatın gerilişi (S16) · rejim B klipte uğultu (hurda tangırtısı · raspa · konveyör · su)
⭐ SES KANITI  ilk ses PAS (gıcırdayan zincir), son ses SU (geminin bordasına vuran dalgacık) — müzik akorunun altında
```
