# ⚠️ THE_BORROWED_HILL — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md` (bu filmde ne var).
> **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.
>
> ⛔ Bu dosya genel tavsiye taşımaz. Her satır ÜÇ şeyi birden taşır: **hangi sahne/kare · hangi
> ölçülmüş kayıt · ne yapılacak.** Üçünden biri yoksa satır yazılmamıştır.
> ⛔ Kaynağı olmayan uyarı yazılmaz — "dikkat edilmeli" bir uyarı değildir.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne / kare | ölçülmüş kayıt (DERS n / film · saniye) | risk | ne yapılacak (cümle, yüzde, px) | durum |
|:--:|---|---|---|---|:--:|
| 1 | S⬜ / G⬜ |  |  |  | ⬜ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne / kare | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S⬜ |  |  |  | ⬜ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| ⬜ |  |  |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır "bakılmadı" demektir.
> Kaynak: `DERSLER.md` + `QA/00_INDEX.md` film blokları. Tablo BÜYÜR — yeni koşu yeni tekrar
> eden arıza bulursa satır ŞABLONA eklenir, tek filme değil.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Üretim günlüğü tutulmadı → QA arızayı adlandıramadı (dört filmde dört kez) | DERS 28 · 29 · LONG DAY · CROSSING · OVER THE WALL · EMPTY RIDGE | ⬜ | ⬜ |
| 2 | Düz ızgara ⑥ METRONOM (üç kez) · varyanslı kurgu RHYTHM (üç kez) — sahip beyanı düz | DERS 13 · 24 · 31 · 44 | ⬜ | ⬜ |
| 3 | Kapak kartı beyansız → son sahne sanıldı, ① ve ④ düştü | DERS 4 | ⬜ | ⬜ |
| 4 | Zincir koşulmadı → her klip başka bina (⑤ REBUILT · ⑧ APPEARED) | DERS 5 · 25 · 12 | ⬜ | ⬜ |
| 5 | Kanıt nesnesi YAZILDI ama zincirde ELLE doğrulanmadı → ilk dikişte öldü | DERS 25 (EMPTY RIDGE'de TUTTU: meşe) | ⬜ | ⬜ |
| 6 | Vinç kancası boş sarktı / bom kadraj dışından / uzun yük havada taşınmadı, hedefte kopyalandı | DERS 8 · 22 · 46 · 57 | ⬜ | ⬜ |
| 7 | Korpusu çoğul yapı tek yazılsa da çoğaldı (türbin → çiftlik) | DERS 55 · 42 | ⬜ | ⬜ |
| 8 | "no X" / "there is no X" / koşullu cümle özneyi ÜRETTİ | DERS 33 · 35 | ⬜ | ⬜ |
| 9 | Güneş diski LIGHTING'de anıldı → kadraja girdi | DERS 39 | ⬜ | ⬜ |
| 10 | Kış tek klipte başlayıp bitti → izleyici iki kış saydı, süre şişti | DERS 7 · 21 · 26 | ⬜ | ⬜ |
| 11 | İstasyon değişen kesmede yapı yüzdesi de değişti → ③ ⑤ ⑥ aynı saniyede düştü | DERS 52 | ⬜ | ⬜ |
| 12 | İki iş yüzeyi varken makine hazır olana gitti (köprü/yol) → iş yüzeyi adsız | DERS 51 · 43 | ⬜ | ⬜ |
| 13 | Ters açılış (bitmiş yapıyla açılıp sökme) vaadi sabote etti | DERS 3 | ⬜ | ⬜ |
| 14 | Blok etiketleri nesre döndü → hem kural hem kapı düştü | DERS 20 | ⬜ | ⬜ |
| 15 | SÜRE sütunu planda kaldı, kurgu düz kesti | DERS 31 · kesme_kontrol.sh | ⬜ | ⬜ |
| 16 | Kutu seti ölçülmeden ızgara yazıldı → araç 6,0 verdi, plan 4–10 yazmıştı | DERS 23 · 31 · A7-a | ⬜ | ⬜ |
| 17 | Montajda mekanizmayı "çalıştır" yazmak yapıyı çalıştırdı (göbek → rotor) | DERS 56 | ⬜ | ⬜ |
| 18 | Gölge süpürmesi üretilmedi / güneş donuk (frozen sun) | DERS 32 · 47 · 18 | ⬜ | ⬜ |
| 19 | Malzeme yoktan var oldu / saydamlıktan belirdi | DERS 48 · 49 | ⬜ | ⬜ |
| 20 | Nehir yatağında ilk kaldırma havuz okundu (saha korpusu) | DERS 54 · 34 | ⬜ | ⬜ |
| 21 | ⭐ YATAY (ilk film) — kadrajın yanları boş kaldı / çapalar yalnız bir yanda; güvenli alan 16:9 ölçülmedi | KILAVUZ_REHBERI §2.8 (varsayım) | ⬜ | ⬜ |
| 22 | ⭐ YATAY (ilk film) — Σ rejim > 14 h → ışık günü kesmede atladı ya da gece girdi | §2.8 ışık günü kuralı (varsayım) | ⬜ | ⬜ |

---

## ✅ KAPI

```
□ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
□ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
□ tekrar eden arıza tablosunun HER satırı cevaplandı (tablo büyür, sayı buraya yazılmaz)
→ üçü de ✅ ise 05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md doldurulabilir
```
