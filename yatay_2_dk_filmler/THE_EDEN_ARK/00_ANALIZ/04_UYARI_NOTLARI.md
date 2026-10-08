# ⚠️ THE_EDEN_ARK — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md` (bu filmde ne var).
> **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı. Her satır: hangi sahne/kare · hangi kayıt · ne yapılacak.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne / kare | ölçülmüş kayıt | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S5 sonu · G6 · S6 | DERS 57 · EMPTY RIDGE 0:21/0:39 | incir hedefte kopyalanır, kanca boş | kaldırma G6'da BİTER: kök topu mezarnanın 0,5 m üstünde (üstten 705), treyler BOŞ; S6 yalnız 0,5 m indirir | ✅ |
| 2 | G5–G7 | DERS 8 · 22 · NARROW LOT | halat göğe karşı erir | kanca +22,5 → üstten 555 (ufkun 15 px altı); "with a strapped root ball on the hook" · "carries a visible load" · "with a slack guiding sling on the hook" | ✅ |
| 3 | bütün G | DERS 55 · EMPTY RIDGE 0:39 | tersanede ikinci gemi | "The shipyard holds exactly one ship, in this dock…" 19 SITE'ta | ✅ |
| 4 | G0–G14 | DERS 56 | gemi erken yüzer | "floating" BIBLE'dan çıkarıldı; "floats/afloat" yalnız S14 I2V ve sonrası — taramayla doğrulandı | ✅ |
| 5 | S10 · S11 | DERS 49 · P15-g | cam saydamlıktan belirir | portal yürür; her bölme beyaz kemer + gök yansımasıyla; "never going back" | ✅ |
| 6 | S0 | DERS 3 · brief | ilk saniyede vinç kaldırması (kancalı ikinci sahne olurdu) | kapaklar zincirle YANA yuvarlanır — vinçsiz ilk saniye hareketi | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne / kare | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S14 | geometri (02 §3) | havuz suyu yakın duvar arkasında görünmez | üç vekil: uzak duvar ıslak bandı · kıç–kapı boşluğu · borda bandı 38 → 48 px — QA_SPEC §4 | ⚠️ ölçülecek |
| 2 | G18 · kapak | geometri | final gemi 329 px (kadrajın %17'si) | kabul; KAPAK §0 zayıflık ölçülerek yazıldı | ⚠️ |
| 3 | G5–G7 | DERS 22 | bom başı göğe karşı (üstten 455) | yalnız üç kare; kanca karaya karşı | ⚠️ |
| 4 | S7 | DERS 48 · 49 | ağaçlar ambarlarda "biter" | fidanlık sırası azalır (5 → 0), telehandler rampada | ⚠️ |
| 5 | S16 | ışık | lambalar yanarken model gemiyi değiştirir | yalnız lamba yanar; gövde, kubbe, taç aynı | ⚠️ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| DERS 34 · 42 | "ark / cruise / greenhouse ship / rainforest" konsept sanatı | kelimeler promptta YOK; "documentary shipyard photograph on colour negative film" |
| §2.8 ışık günü | Σ rejim tam 14,0 saat | gece yok; sabah 06:00 başlar; tek dakika ek pencere yok |
| hız | aylar → tek gün | beyanlı (PLAN üst satırı · YAYIN_PAKETI TIME SPAN) |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Üretim günlüğü tutulmadı | DERS 28 · 29 | üretim başlamadı | günlük iskeleti açık; qa_paket günlüksüz durur |
| 2 | Düz ızgara ⑥ METRONOM | DERS 13 · 24 · 31 · 44 | VAR — sahip ızgarası 18 × 8,0 | beyanlı; ritim rejim nabzına ve müzik katmanına taşındı |
| 3 | Kapak kartı beyansız | DERS 4 | yok | TESLİM YAPISI'nda 5,0 sn ayrı |
| 4 | Zincir koşulmadı | DERS 5 · 25 · 12 | üretimde | ters zincir G18 → G0, her karede zincir_kontrol |
| 5 | Kanıt nesnesi elle doğrulanmadı | DERS 25 | üretimde | tuğla baca 253 px, günlükte ✓/✗ |
| 6 | Kanca boş · bom dışarıdan · uzun yük havada | DERS 8 · 22 · 46 · 57 | VAR (tek kaldırma) | ⛔ satırı 1–2 |
| 7 | Çoğul korpus | DERS 55 · 42 | VAR (tersane) | ⛔ satırı 3 |
| 8 | "no X" özneyi üretti | DERS 33 · 35 | yok | AT THIS STAGE'ler pozitif; "no ship's name" yalnız metin yasağında |
| 9 | Güneş diski anıldı | DERS 39 | yok | "The sun stays outside the frame." |
| 10 | Kış tek klipte | DERS 7 · 21 · 26 | yok — tek gün | — |
| 11 | İstasyon değişen kesmede yapı da değişti | DERS 52 | yok — tek istasyon | brief'in üç açısı reddedildi (02 §1) |
| 12 | İş yüzeyi adsız | DERS 51 · 43 | önlendi | ACTIVITY'de "forward hold · middle hatch · aft coamings" |
| 13 | Ters açılış | DERS 3 | yok | S0 paslı gemiyle açılır |
| 14 | Etiketler nesre döndü | DERS 20 | yok | promptlar tek kaynaktan betikle türetildi |
| 15 | SÜRE sütunu planda kaldı | DERS 31 | üretimde | kesme_kontrol.sh QA_SPEC §6 |
| 16 | Kutu seti ölçülmeden ızgara | DERS 23 · 31 | VAR — ölçülmedi | beyanlı; üretim kapısı |
| 17 | Mekanizmayı "çalıştır" yazmak | DERS 56 | VAR (yüzme) | ⛔ satırı 4 |
| 18 | Gölge süpürmesi / donuk güneş | DERS 32 · 47 · 18 | önlendi | B'lerde 20°–65° süpürme yazılı |
| 19 | Malzeme yoktan / saydamlıktan | DERS 48 · 49 | önlendi | her malzemenin kaynağı G(n)'de (PLAN §Malzeme kaynağı) |
| 20 | Nehir yatağı havuz okundu | DERS 54 · 34 | ⚠️ ters yönde: KURU havuz suya dönüşür | S14'e kadar "dry dock floor" · "dusty" — su yalnız S14'te |
| 21 | YATAY — yanlar boş / çapalar tek yanda | §2.8 | önlendi | sol: baca · sağ: fener · alt: havuz kenarı |
| 22 | YATAY — Σ rejim > 14 h | §2.8 | sınırda (14,0) | 03 §4 |

---

## ✅ KAPI

```
✅ 🔴 ⛔ satırlarının hepsi kapatıldı
✅ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşındı (§4 görünmeyen su · §8 pilotlar)
✅ tekrar eden arıza tablosunun her satırı cevaplandı
```
