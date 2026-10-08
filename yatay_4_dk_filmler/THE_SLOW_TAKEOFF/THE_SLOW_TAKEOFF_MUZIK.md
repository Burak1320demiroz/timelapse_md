# 🎶 THE_SLOW_TAKEOFF — MÜZİK

**Kaynak:** `MUZIK_VE_KAPAK.md` §1 · kart A adım 9 · ses hedefi `KURGU_VE_TESLIM` §4 · sahip senaryosu 07.10.2026 §SES VE MÜZİK

```
TEMPO         120 BPM — HESAPLANIR, seçilmez: ölçü 2,0 sn · 8,0 sn sahne = 4 ölçü · kesme ölçünün 1. VURUŞUNDA [A2-e]
              (ızgara dışı tempo 29 kesmenin hepsini hizasız bırakır; sahne süresi ölçünün TAM KATI)
SÜRE          240,0 s = sahne bloğu (kart YOK) — müzik 240,0'da doğal sönümle biter, ani kesilmez (sahip: "Son kareye
              ani ses kesilmesi uygulanmaz") — son akor 232,0'da basılır, 240,0'a kadar söner
KESMELER      8,0 · 16,0 · … · 232,0  (29 kesme, her 8,0 sn) — her biri ölçü başı, kurguda tek tek hizalanır [D-d]
MÜZİKSİZ PENCERE  0,0–8,0 s (S0 tamamı): yalnız vinç motoru, gergin halatın mekanik sesi, rüzgâr [A1-c · C2-h]
KATMAN = AŞAMA ⭐ [§1.2]  yedi katman; her biri bir ELEMANLA ve bir KESMEDE girer, söküm ve kışta biri ÇEKİLİR:
              8,0 temizlik → yumuşak nabız (keçeli piyano, tek nota ostinato)
              24,0 çerçeveler → ritim belirginleşir (ahşap tıkırtı, düşük perküsyon)
              40,0 ⭐ KALKIŞ → genişleme (alçak çello pedalı + yaylı akor) — vuruş noktası ①
              64,0 teras → sıcak orta armoni (harmonium)
              104,0 kokpit → tek celesta motifi (iç mekân — yalnız kokpit klibinde, sonra çekilir)
              136,0 ⭐ SÖKÜM → perküsyon ÇEKİLİR (vuruş noktası ②) · 144,0 kış → piyano + ped, tempo aynı
              152,0–176,0 yağmur ve su → müzik yalnız ped; ses yatağı öne (rüzgâr, yağmur, su)
              176,0 dönüş → nabız yeniden, hafif · 184,0 bahçe → çekilen telli (gitar, pizzicato)
              208,0 ⭐ IŞIKLAR → geniş, sakin çözülme akoru (vuruş noktası ③) · 224,0 kano → müzik incelir, kürek ve
              su sesi duyulur · 232,0 son akor tutulur → 240,0 sönüm
SUB-BASS      55 Hz + oktav eşlikçisi 110 Hz (telefon/dizüstü hoparlörü sub'ı çalmaz)
VURUŞ NOKTASI üç: 40,0 (kalkış — doruk) · 136,0 (söküm — ev ilk kez temiz) · 208,0 (ışıklar) — az olan güçlüdür
KIŞ           S18–S19 (144,0–160,0): katman incelir / tempo AYNI kalır (ızgara bozulmaz), doku değişir
KOKPİT        S13 (104,0–112,0) ve S21 (168,0–176,0): dış sesler camın ardından boğuk (yüksek frekans kesilir);
              S21'de yağmur cama vurur, içerisi kuru ve sakin
SES HEDEFİ    −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP · mono uyumlu (alt uç merkezde)
⚠️ LİSANS     POLITIKA_VE_RISK — müzik lisansının üç boşluğu (araç · lisans türü · kanıt) dolmadan müzikli video
              YAYINLANMAZ: ⬜ sahip doldurur
```

---

## 🎼 MÜZİK PROMPTU — tek parça, 240 saniye [§1.4 iskeleti]

```
TOOL: ⬜ (sahip seçer — lisansı ticari kullanıma açık olan)
GENRE: minimal documentary post-classical — felt piano, low strings, harmonium, soft wooden percussion, celesta
TEMPO: 120 BPM, 4/4, bar = 2.0 s, strict and bar-aligned. Duration 240 seconds. No tempo change.
No lyrics. No vocals. No melody line that sings over the picture; motifs are short and repeat.

INSTRUMENTATION — layers enter with the build, in this order, each one only on a bar line at a cut:
  1. site ambience only, no music                    (0–8 s)
  2. felt piano, one soft repeated note pulse          (8 s · the clean-up)
  3. soft wooden clicks and a low muted drum           (24 s · the steel frames go up)
  4. low cello pedal and a wide string chord           (40 s · the lift — the piece opens up here)
  5. warm harmonium in the middle register             (64 s · the timber terrace)
  6. one short celesta figure, alone                   (104 s · inside the cockpit; withdrawn at 112 s)
  7. plucked guitar and pizzicato strings              (184 s · the garden)

DYNAMIC MAP — scene grid, one line per 8 s clip (cuts on bar 1):
  0–8 s    (S0):  no music · crane motor, a taut cable creaking, wind
  8–24 s   (S1–S2): piano pulse, very low; pressure-washer hiss and earth-moving underneath
  24–40 s  (S3–S4): wooden clicks join; steady, quiet; bolts and steel underneath
  40–56 s  (S5–S6): ⭐ strings and cello open wide as the plane leaves the ground; crane-free, only the jacks' hum
  56–104 s (S7–S12): full but calm; harmonium enters at 64 s; timber and glass sounds mark each stage
  104–112 s (S13): everything drops to the celesta figure and a muffled room tone — inside the cockpit
  112–136 s (S14–S16): back to the full calm texture; harmonium leads
  136–144 s (S17): ⭐ percussion withdraws — the finished house stands clear
  144–152 s (S18): piano and pad only; wind, snow hush
  152–176 s (S19–S21): pad only; rain and rising water in front; at 168 s (inside the cockpit) rain on glass, muffled
  176–208 s (S22–S25): pulse returns gently; plucked strings from 184 s; water, spades, timber
  208–224 s (S26–S27): ⭐ a broad, calm resolving chord as the lights come on
  224–232 s (S28): music thins to a held tone; paddle strokes and water clearly heard
  232–240 s (S29): last chord held and left to decay naturally; water and a single paddle drip; no hard stop

SYNC RULE: every visual cut lands on beat 1 of a bar; a new layer enters only on a cut, never inside a shot.
The winter and rain blocks (144–176 s) thin the arrangement without changing tempo. The two cockpit clips
(104–112 s and 168–176 s) are heard from inside: outside sound muffled behind glass.

MIX: mono-compatible — low end centred; no wide stereo that collapses on a phone speaker. Every sub-bass element
below 150 Hz is doubled by its own upper harmonics at roughly 100, 150 and 200 Hz so the fundamental is implied
rather than required; the low end is never the only carrier of the weight.
Target −14 LUFS · −1.0 dBTP.

REFERENCE FEEL (feel only, never quoted): the patience of Jóhann Jóhannsson's documentary scores; the felt-piano
intimacy of Ólafur Arnalds.

NO vocals, NO lyrics, NO braam, NO riser, NO reversed cymbal, NO whoosh, NO tempo ramp, NO aircraft engine sound.
```

> Referans hissi verilebilir, **alıntı verilemez.**

---

## 🔊 SES YATAĞI — diegetik, müziğin altında sürer [A1-c]

```
00:00–00:32  vinç motoru · gergin halat · basınçlı su · sarmaşık ve dal sürtünmesi · iş makinesi · beton
00:32–00:56  kriko uğultusu (sürekli — kalkışı birleştirir) · çamurdan kopma sesi (yalnız görüntüde kopma varsa)
             ⛔ gösterilmeyen metal darbesi YOK · uçak motoru çalıştırma sesi YOK (sahip)
00:56–02:24  ahşap · bulon · cam · iç mekân işleri — her aşama kendi sesiyle; her kesmede aynı whoosh YOK
02:24–02:56  rüzgâr · kar sessizliği · yağmur · yükselen su; kokpitte (02:48) dış ses camın ardında boğuk
02:56–03:28  su · kürek/kazma · bahçe · ahşap iskele çakılması
03:28–04:00  akşam: su, uzak kuş, kürek; son karede ani kesilme YOK
KESME KÖPRÜSÜ ortam sesi kesmede ATLAMAZ (dikişin iki yakası aynı kare — ses de aynı yatak); kokpit kesmeleri
             içeri/dışarı filtre geçişidir, sıçrama değil
MAKİNE SESİ   rejim A klipte tanınır (motor · geri vites) · rejim B'de uğultuya iner · rejim G'de gerçek ses
```
