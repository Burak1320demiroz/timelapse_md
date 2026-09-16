# 🎞️ <FILM_ADI> — SAHNE SIRALAMASI (aşama merdiveninin türetildiği yer)

> **Bu dosya sıranın TÜRETİLDİĞİ ve DENETLENDİĞİ yerdir.** Sonuç `<FILM>_PLAN.md` §AŞAMA MERDİVENİ
> ve §KARE TABLOSU'na taşınır — orası sonucu taşır, burası hesabı.
> ⛔ Burada `## 🎬 SAHNE <n>` başlığı yoktur; sahneler TABLO satırıdır.
> Girdi: `02_KONSEPT_VE_RISK.md` (yapı kartı · kamera · ışık günü · risk) + onaylı sahne satırları.

---

## 1. 🧱 İNŞA SIRASI → <N> SATIR [YAPI_TIPI_KARTLARI · INSAAT_YONTEMI §2-§3]

```
KARTIN SIRASI      ① ⬜ ② ⬜ ③ ⬜ … (kartın kendi adımları — uydurulmaz)
<N> SATIRA AÇMA    her adım kaç sahne alıyor ve ara hâlleri (%25 / %50 / %75) hangi satırlar:
                   ① → S⬜–S⬜ · ② → S⬜–S⬜ · …
MONOTON BÜYÜME     hiçbir satır öncekinden az yapı göstermez ✓/✗ · ara hâl SİLUETİ değiştiriyor mu [DERS 37] ✓/✗
KIŞ                S⬜ (kar · döngü yavaşlar) + S⬜ (erime · çamur) — iki sahne [DERS 7 · 21]
DORUK              S⬜ — en büyük görünür değişim (düz ızgarada süre değil, KATMAN ve rejimle vurgulanır)
SÖKÜM              S⬜ — geçici ekipman ekranda gider
TERS AÇILIŞ YOK    S0 ileri yönlü kanca [DERS 3]: ⬜
```

## 2. 🗺️ SIRALAMA — <N> sahne, sırayla

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | AZ/EL | İSTASYON | KANIT NESNESİ (px) | onaylı satırla aynı mı |
|:-:|:-:|---|---|---|:-:|:-:|:-:|:-:|---|:-:|
<SIRALAMA_SATIRLARI>

## 3. 📐 DİKİŞ DENETİMİ — mekanik, göz kararı değil [§2.7 · DERS 52]

> Zincirli formatta dikiş bir KAREDİR: G(n+1) hem S(n)'in son karesi hem S(n+1)'in ilk karesi.
> Her dikişte yapı yüzdesi, gölge açısı, gök, çapalar AYNIDIR; değişen yalnız klibin içindedir.

| dikiş | kare | yapı yüzdesi | gölge açısı | gök | istasyon aynı mı | not |
|---|:-:|:-:|:-:|:-:|:-:|---|
| S0→S1 | G1 |  |  |  | ✓ |  |
| … |  |  |  |  |  |  |
| S<K_SON>→S<K> | G<K> ⭐ bölüm sınırı |  |  |  | ✓ | iki dosya, tek kare |

## 4. ☀️ IŞIK GÜNÜ TOPLAMI — rejim sütunu TOPLANIR

```
A × ⬜ = ⬜ dk · B × ⬜ = ⬜ h · C × ⬜ = ⬜ h   →  Σ = ⬜ saat   (≤ 14 ✓/✗ · gece yok/var)
SAAT SÜTUNU   S0 ⬜:00 → S<N_SON> ⬜:00 — monoton artar ✓/✗ · her G'nin azimut/yükseklik değeri KARE TABLOSU'na
REJİM C       yalnız gölgesiz klip; en uzun klip OLAMAZ [DERS 40] — düz ızgarada hepsi eşit → C kullanılıyorsa gerekçe: ⬜
```

## 5. ⭐ ÜÇ ZORUNLU SATIR — PLAN'a taşınacak

```
KANIT   ⬜ (nesne · x px · %y · boy px) — G0…G<N> birebir
LOOP    G<N> ↔ G0: kadraj aynı · ışık ⬜
SÖKÜM   S⬜ · ⬜ ekranda gider
```

## 6. 🔁 ONAYLI HİKÂYEYLE FARK

```
SAPMA: yok   /   S⬜: onaylı "⬜" → burada "⬜" — sebep ⬜ → 00_HIKAYE_ONAYI SAPMA'ya yazıldı, yeniden onay ⬜
```
