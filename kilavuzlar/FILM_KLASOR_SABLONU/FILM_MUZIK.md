# 🎶 <FILM_ADI> — MÜZİK

**Kaynak:** `MUZIK_VE_KAPAK.md` §1 · kart A adım 9 · ses hedefi `KURGU_VE_TESLIM` §4

```
TEMPO         120 BPM — HESAPLANIR, seçilmez: ölçü 2,0 sn · <KLIP>,0 sn sahne = <OLCU> ölçü · kesme ölçünün 1. VURUŞUNDA [A2-e]
              (ızgara dışı tempo <N_SON> kesmenin hepsini hizasız bırakır; sahne süresi ölçünün TAM KATI olmalı)
SÜRE          <TOPLAM>,0 s = sahne bloğu <SURE>,0 + kapak kartı 5,0 (kartta akor tutulur / sessizlik — ⬜)
KESMELER      <KESMELER>   (her biri ölçü başı — kurguda tek tek hizalanır [D-d])
MÜZİKSİZ PENCERE  0,0–⬜ s (S0: ⬜ ortam sesi — rüzgâr / nehir / trafik / kuş) · ⛔ her filmde EN AZ BİR
KATMAN = AŞAMA ⭐ [§1.2]  <N> sahnede ⬜ katman; her katman bir ELEMANLA girer (temel → sub · karkas → ritim ·
              cephe → armoni · söküm → katman ÇEKİLİR · teslim → tutulan akor). Düz ızgarada ritim buradan taşınır
              (PLAN §DÜZ IZGARA BEYANI (b)).
SUB-BASS      ⬜ Hz + 90-160 Hz oktav eşlikçisi (telefon/dizüstü hoparlörü sub'ı çalmaz)
VURUŞ NOKTASI ⬜ — kaç tane, hangi saniyede (doruk S⬜ · söküm S⬜ · teslim S<N_SON>) — az olan güçlüdür
KIŞ           S⬜–S⬜: katman incelir / tempo AYNI kalır (ızgara bozulmaz), doku değişir
SES HEDEFİ    −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP · mono uyumlu (alt uç merkezde)
```

---

## 🎼 MÜZİK PROMPTU — tek parça, <TOPLAM> saniye [§1.4 iskeleti]

```
TOOL: ⬜
GENRE: ⬜ (documentary / minimal / ⬜)
TEMPO: 120 BPM, 4/4, bar = 2.0 s. Duration <TOPLAM> seconds. No tempo change.

INSTRUMENTATION — layers enter with the build, in this order:
  1. ⬜  (0–⬜ s · site ambience only, no music)
  2. ⬜  (⬜ s · S⬜ · ⬜ [eleman])
  3. ⬜
  4. ⬜
  5. ⬜  (<SURE> s · end card: ⬜ held chord / silence)

DYNAMIC SPREAD — scene grid, one line per 10 s block (cuts on bar 1):
  0–10 s   (S0): ⬜
  10–20 s  (S1): ⬜
  …
  <B1_SURE>–⬜ s (S<K>): ⬜   [bölüm sınırı — müzikte İŞARETSİZ: kesme değil, kare]
  …
  ⬜–<SURE> s (S<N_SON>): ⬜   [final: last ≥2 s hold]
  <SURE>–<TOPLAM> s (END CARD): ⬜

SYNC RULE: every visual cut lands on beat 1 of a bar; a new layer enters only on a cut, never inside
a shot. Winter block (S⬜–S⬜) thins the arrangement without changing tempo.

MIX: mono-compatible — low end centred; no wide stereo that collapses on a phone speaker.
Target −14 LUFS · −1.0 dBTP.

NO vocals, NO lyrics, NO braam, NO riser, NO reversed cymbal, NO whoosh, NO tempo ramp.
```

> Referans hissi verilebilir, **alıntı verilemez.**

---

## 🔊 SES YATAĞI

```
ORTAM         ⬜ [sahaya göre: rüzgâr · su · uzak trafik · kuş · makine uğultusu] — S0 açılışı müziksiz, yalnız bu
KESME KÖPRÜSÜ ortam sesi kesmede ATLAMAZ (dikişin iki yakası aynı kare — ses de aynı yatak)
MAKİNE SESİ   rejim A klipte tanınır (motor · geri vites) · rejim B/C'de uğultuya iner — rejimle uyumlu
```
