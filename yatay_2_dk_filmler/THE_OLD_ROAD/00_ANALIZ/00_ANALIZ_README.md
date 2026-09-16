# 🔬 00_ANALIZ — yazımdan ÖNCEKİ iş burada durur

> **Bu klasör filmin defteridir, filmin kendisi değildir.** Buradaki hiçbir dosya bir üretim
> promptu taşımaz ve hiçbiri kapı betiklerine girmez. Film dosyaları (`PLAN` · `BOLUM_*` ·
> `KAPAK` · `MUZIK` · `YAYIN_PAKETI` · `QA_SPEC` · `URETIM_GUNLUGU`) bir üst seviyededir.

**Neden ayrı bir klasör (14.09.2026 · sahip kararı, `film_md` şablonundan):** analiz PLAN'ın
içine gömülünce plan 800 satır oluyor ve kimse geri dönüp bakmıyor. Bu deponun kendi ölçümü
aynı yönde: DERS 28 — "günlük tutulur" cümlesi AGENTS'ta dururken dört filmde dört kez
tutulmadı; şablon DOSYA olunca kapı ona bağlanabildi. Ayrı dosya, görünür borçtur.

---

## Sıra — üstten aşağı, atlanmaz

| # | dosya | ne yapar | bitmeden geçilmez |
|:--:|---|---|---|
| 0 | `00_HIKAYE_ONAYI.md` | ⭐ hikâye (VAAT · DİRENÇ · BEDEL · 15 sahne satırı) düz Türkçe, **sahip onaylar**, onaylı metin buraya işlenir — `onay-once-uretim` kuralının dosyası | `ONAY:` tarihli değilse hiçbir dosya yazılmaz |
| 1 | `00_OKUMA_CIZELGESI.md` | betikten: kılavuzlar · DERSLER (ölçülmüş + devralınan) · QA/RAPORLAR · rubrikler · apexait çekirdeği — okundu ⬜ → ✅, bu filme düşen kilit sütunu | ⬜ kalan satır varken 2'ye geçilmez; "hepsi —" sahtedir |
| 2 | `01_QA_DERS_HASADI.md` | okunanlardan BU filme düşen DERS kilitleri + QA arızaları + devralınan varsayımlar | sıfır satırla 3'e geçilmez (57 ölçülmüş ders var) |
| 3 | `02_KONSEPT_VE_RISK.md` | konsept kapısı (VAAT/DİRENÇ/BEDEL + dört test) · yapı + saha kartı · kamera hesabı · vinç · ışık günü · yapı kartının RİSK satırları | konsept kapısı üçü ✅ olmadan 4'e geçilmez |
| 4 | `03_SAHNE_SIRALAMASI.md` | inşa sırası → 15 satır: eleman · ara hâl · rejim · saat · süre; monoton büyüme · kış iki sahne · Σ rejim ≤ 14 h · bölüm sınırı; onaydan sapıyorsa `SAPMA:` | 5'in girdisidir |
| 5 | `04_UYARI_NOTLARI.md` | sıralamanın tetiklediği ölçülmüş arızalar + bu deponun tekrar eden arıza tablosu | ⛔ satırı açıkken 6'ya geçilmez |
| 6 | `05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md` | sahne başına BİR satır (betik damgalar): AT THIS STAGE cümlesi · geçici ekipman · iki hareket eden + yüzey kanıtı · kanıt nesnesi px · KAPI | her satır KAPI ✅ olmadan o sahnenin promptu yazılmaz |

Hepsi bittikten SONRA film yazımı başlar: `THE_OLD_ROAD_PLAN.md` → `THE_OLD_ROAD_BOLUM_2.md` USTA KARE →
`THE_OLD_ROAD_BOLUM_1.md` / `_BOLUM_2.md` sahneler → KAPAK · MUZIK · YAYIN_PAKETI → QA_SPEC → prompt kapısı.

---

## ⛔ Kapı betiklerine girmeme kuralı

`araclar/prompt_kontrol.py` klasör modunda YALNIZ `*_PLAN.md` + `*_BOLUM_1.md` + `*_BOLUM_2.md`
okur; bu klasör okunmaz. Bunun **bozulmaması** için burada:

```
⛔ "## 🎬 SAHNE <n>" biçiminde başlık YAZILMAZ — sahne burada TABLO satırıdır.
⛔ "### 📸 GÖRSEL PROMPT" / "### 🎥 I2V PROMPT" başlıkları YAZILMAZ — prompt yalnız bölüm dosyasında.
⛔ "TESLİM YAPISI" / "USTA KARE" başlıkları YAZILMAZ — kapı bunları PLAN ve BOLUM_2'de arar.
```

## ⛔ Boş dosya silinmez

`⬜ BEKLİYOR` satırıyla durur. Var olan boş dosya görünür borçtur; olmayan dosya borç değil, unutmadır.
