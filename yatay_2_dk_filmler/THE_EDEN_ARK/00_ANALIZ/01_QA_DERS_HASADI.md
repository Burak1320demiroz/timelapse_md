# 🧾 THE_EDEN_ARK — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — her satırı `04_UYARI_NOTLARI.md` ile `00_SAHNE_TABLOSU.md`
> içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — `kilavuzlar/DERSLER.md` ölçülmüş derslerden bu filme düşenler

| ders | ölçülmüş arıza (tek cümle) | bu filmde kilit cümlesi | hangi sahnelere / karelere düşecek |
|---|---|---|---|
| 3 | ters açılış vaadi sabote etti | S0 ileri yönlü: paslı gemi kapakları AÇILIR, bitmiş gemiyle açılmaz | S0 · G0 |
| 4 | beyansız kapak kartı son sahne sanıldı | TESLİM YAPISI'nda 5,0 sn kart AYRI beyan | PLAN · KAPAK · QA_SPEC §1 |
| 5 · 12 · 25 | zincir koşulmadı → her klip başka yapı | 19 karede baca (kanıt nesnesi) ELLE doğrulanır | bütün G |
| 7 | kış tek klipte | KIŞ YOK — tek haziran günü | — (gerekçe: tek ışık günü) |
| 8 · 22 · 46 | kanca boş sarktı / halat koptu / bom kadraj dışından | TEK yüklü kanca sahnesi (S6); G5'te "with a strapped root ball on the hook", G7'de "with a slack guiding sling on the hook"; G0–G4 ve G8+ kadrajda vinç YOK | G5 · G6 · G7 · S5 · S6 |
| 13 · 24 · 44 | düz ızgara METRONOM | sahip beyanı 18 × 8,0; ritim rejim değişimine ve müzik katmanına taşınır | PLAN · MUZIK |
| 15 · 50 | rejim B'de donuk insan | "Crew register only as faint soft motion streaks" — A'da hızlı ama tanınır | bütün G |
| 18 · 32 · 47 | güneş donuk / gölge süpürmedi | her G'de azimut + yükseklik; B kliplerinde gölge 20°–65° süpürür | bütün G · B I2V'leri |
| 19 · 36 | BIBLE sayısız | BIBLE: 130 m · üç ambar · 20 kemer · 18 m en · 13 m yükseklik · 13 m'lik incir | 19 görsel |
| 20 | etiketler nesre döndü | blok etiketleri birebir | bütün promptlar |
| 23 · 31 | kutu seti ölçülmeden ızgara | ARAÇ KUTU SETİ ÖLÇÜLMEDİ beyanı · tavan ≥ 8,0 | PLAN · GÜNLÜK |
| 33 · 35 | "no X" özneyi üretti | AT THIS STAGE pozitif; "no ship"/"no crane" yazılmaz | bütün G |
| 34 · 42 | korpus CGI'ye / yanlış yapıya düşer | "ark", "cruise", "greenhouse ship", "rainforest" promptta YOK; gemi biçimle yazılır; belgesel tersane fotoğrafı korpusu | bütün G |
| 39 | güneş diski anıldı → kadraja girdi | "The sun stays outside the frame" — disk anılmaz | bütün G |
| 45 | final zifirde | G18 güneş −2,3°, mavi saat; her parça okunur | G17 · G18 |
| 48 · 49 | malzeme yoktan · saydamlıktan beliren | her malzemenin kaynağı kadrajda: hurda konteyneri · fidanlık · toprak yığını · cam sandıkları · portal | S1 · S5 · S7 · S10 |
| 51 · 43 | iş yüzeyi adsız, makine hazır olana gider | ACTIVITY'de iş yüzeyi ambar numarası ve elemanla | S4 · S5 · S7 |
| 52 | istasyon değişen kesmede yapı da değişti | TEK istasyon; bölüm sınırı G9 tek kare | G9 |
| 55 | çoğul korpus (tersane = çok gemi) | "The shipyard holds exactly one ship, in this dock" — SITE'ta 19 kez | bütün G |
| 56 | montajda "çalıştır" yazmak yapıyı çalıştırdı | gemi S14'e kadar "rests on its keel blocks"; "floats" yalnız S14 I2V'sinden sonra | G0–G14 |
| 57 | uzun rijit yük havada taşınmadı, hedefte kopyalandı | büyük ağaç kaldırma yolu G6'da BİTER (ağaç ambarın üstünde asılı); kemerler havada taşınmaz, portal yerinde dikilir | S5 sonu · S6 · S9–S11 |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `QA/ARSIV_12_MERCEK/RAPORLAR/` + `QA/ARSIV_12_MERCEK/00_INDEX.md`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE EMPTY RIDGE 0:39 | ② ⑤ ⑧ ⑪ | iki tam boy türbin belirdi (çoğul korpus) | tersane sayım cümlesi; "one ship" + "harbour craft" yalnız römorkör için |
| THE EMPTY RIDGE 0:21 · 0:39 | ⑩ | kanca boş, yük "pop" | ağaç G6'da asılı başlar, S6 yalnız indirir |
| THE NARROW LOT 0:11–0:18 | ① ② | halat göğe karşı eridi | kancalı yük yalnız S5 sonu–S6'da; kanca +22,5 m → üstten 555, ufkun (540) 15 px ALTINDA — kanca alt yarıda; halat bom başına (üstten 455) kadar 100 px göğe karşı — ⚠️ beyanlı |
| THE STAR DOCK | ④ | FINAL BEAT FAIL | S17 son ≥ 2,0 sn TUTUŞ — gemi kapı dışında, ışıklar yanık |
| THE STONE DRAGON | ④ | BİTİŞ KARTI İHLALİ | kart 144,0–149,0, sahne bloğuna karışmaz |
| THE OLD ROAD (yatay 15 × 8,0) | — | ölçülmedi — aynı bant dışı ızgaranın emsali | ızgara gerekçesi aynı kalıpta |

## 3. 📎 DEVRALINAN / DIŞ OKUMA VARSAYIMLARI — `DERSLER.md` D-x · A/P-x

| kod | varsayım | bu filmde nerede sınanacak |
|---|---|---|
| §2.8 güvenli alan | 16:9 güvenli alan ölçülmedi — alt 100 px ve sağ üst 300×100 px | kanıt nesneleri bu bölgelerin dışında (QA_SPEC §7) |
| P3-d | akış tarifi kaynak · hedef · görünürlük ister | konveyör: toprak yığını (x 461) → ambar 1 mezarnası (x 613); S5 |
| P15-g | şeffaflık çerçeveyle kanıtlanır | camın beyaz kemerleri ve gök yansıması; S10–S11 |
| P24-e | canlı/ilk kez gelen şeyin taşıyıcısı önceki klipte gelir | römorkör S15'te gelir, S16'da halatı alır |
| P23-a | ardışık montaj havada değil yerinde | kemerler portalda yerinde dikilir |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        22 satır (31 ders)
QA ARIZASI:         6
VARSAYIM:           5
⛔ EN PAHALI ÜÇÜ:   DERS 57 (ağaç kaldırma) · DERS 22 (halat bom başına kadar 100 px göğe karşı) ·
                    DERS 49 (cam ve bitki saydamlıktan belirmesi)
```
