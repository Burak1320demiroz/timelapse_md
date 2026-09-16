# 🎶 THE_OLD_ROAD — MÜZİK

**Kaynak:** `MUZIK_VE_KAPAK.md` §1 · kart A adım 9 · ses hedefi `KURGU_VE_TESLIM` §4

```
TEMPO         120 BPM — HESAPLANIR, seçilmez: ölçü 2,0 sn · 8,0 sn sahne = 4 ölçü · kesme ölçünün 1. VURUŞUNDA [A2-e]
              (ızgara dışı tempo 14 kesmenin hepsini hizasız bırakır; sahne süresi ölçünün TAM KATI olmalı)
SÜRE          125,0 s = sahne bloğu 120,0 + kapak kartı 5,0 (kartta tek tutulan akor söner, son 1,5 sn yalnız ortam)
KESMELER      8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn)   (her biri ölçü başı — kurguda tek tek hizalanır [D-d])
MÜZİKSİZ PENCERE  0,0–2,0 s (S0: uzaktan gelen ortam — vadi rüzgârı, aşağıda nehir, virajlardan geçen tek aracın sesi) · ⛔ her filmde EN AZ BİR
KATMAN = AŞAMA ⭐ [§1.2]  15 sahnede 5 katman; her katman bir ELEMANLA girer (temel → sub · karkas → ritim ·
              cephe → armoni · söküm → katman ÇEKİLİR · teslim → tutulan akor). Düz ızgarada ritim buradan taşınır
              (PLAN §DÜZ IZGARA BEYANI (b)).
SUB-BASS      45–60 Hz + 90-160 Hz oktav eşlikçisi (telefon/dizüstü hoparlörü sub'ı çalmaz)
VURUŞ NOKTASI ÜÇ — 32,0 (ilk itme · S4 başı) · 88,0 (kavuşma · S11 başı) · 112,0 (trafik geçer · S14 başı) — başka vuruş yok
KIŞ / SEL     S6 (kış: doku soğur) ve S7–S9 (sel: katmanlar ÇEKİLİR, tempo AYNI kalır — ızgara bozulmaz)
SES HEDEFİ    −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP · mono uyumlu (alt uç merkezde)
```

---

## 🎼 MÜZİK PROMPTU — tek parça, 125 saniye [§1.4 iskeleti]

```
TOOL: [müzik aracı adı + sürüm — lisans satırı YAYIN_PAKETI'ne]
GENRE: documentary / minimal alpine industrial — distant, wide, air between the sounds
TEMPO: 120 BPM, 4/4, bar = 2.0 s. Duration 125 seconds. No tempo change.

INSTRUMENTATION — layers enter with the build, in this order:
  1. Low sustained drone, one note per bar   (0–32 s · S0–S3 · valley air, distant traffic)
  2. Dry percussive pulse on the first beat   (32–64 s · S4–S7 · the launching jacks — enters with the first push)
  3. Wide low strings, slow swell             (48–64 s · S6–S7 · the deck reaching over the river)
  4. Thin metallic texture, no pulse          (64–80 s · S8–S9 · the flood — layers 2 and 3 drop out)
  5. Warm sustained chord over the pulse      (88–120 s · S11–S14 · the crossing closes and opens)
     END CARD: the chord resolves and decays; the last 1,5 seconds carry only valley air.

Dynamic map across 125 seconds:
  0–2 s              site ambience only: wind over the valley, the river far below, one car on the hairpins
  2–32 s   (S0–S3)   layer 1 alone; earth-moving and drilling under it, the sound always DISTANT
  32–40 s  (S4)      ⭐ layer 2 enters on the first push — the pulse names the method
  40–48 s  (S5)      pulse continues, one added bar of metallic detail as a segment is joined
  48–64 s  (S6–S7)   layer 3 swells as the deck crosses the river; at 56 s the mix cools (winter)
  64–72 s  (S8)      ⭐ pulse and strings DROP OUT; water, wind and one metallic groan remain
  72–80 s  (S9)      near silence: dripping, distant machinery, the drone thin
  80–88 s  (S10)     the pulse returns, alone at first, then the drone under it
  88–96 s  (S11)     ⭐ layer 5 opens as the nose lands; the last two seconds sit on a held chord
  96–112 s (S12–S13) the arrangement thins again: single sustained notes under the dismantling and paving
  112–120 s (S14)    the chord opens once more, the pulse fades out under it, the last two seconds are held
  120–125 s (CARD)   resolve and decay to valley air

a shot. The flood block (S8–S9) thins the arrangement to almost nothing without changing the tempo.

MIX: mono-compatible — low end centred; no wide stereo that collapses on a phone speaker.
Target −14 LUFS · −1.0 dBTP.

NO vocals, NO lyrics, NO braam, NO riser, NO reversed cymbal, NO whoosh, NO tempo ramp.
```

> Referans hissi verilebilir, **alıntı verilemez.**

---

## 🔊 SES YATAĞI

```
ORTAM         vadi rüzgârı · aşağıda nehir (selde gürler) · virajlardan geçen araçların uzak uğultusu · kuş
              ⭐ KAMERA 380 m UZAKTA: bütün sesler uzaktan gelir — rüzgârla süzülmüş, gecikmeli, yankılı; yakın plan
              makine sesi (kabin içi, çelik çınlaması) KULLANILMAZ — S0 açılışı müziksiz, yalnız bu
KESME KÖPRÜSÜ ortam sesi kesmede ATLAMAZ (dikişin iki yakası aynı kare — ses de aynı yatak)
MAKİNE SESİ   rejim A klipte tanınır (motor · geri vites) · rejim B/C'de uğultuya iner — rejimle uyumlu
```
