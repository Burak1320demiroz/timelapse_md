# ⚠️ THE_OLD_ROAD — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md` (bu filmde ne var).
> **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.
>
> ⛔ Bu dosya genel tavsiye taşımaz. Her satır ÜÇ şeyi birden taşır: **hangi sahne/kare · hangi
> ölçülmüş kayıt · ne yapılacak.** Üçünden biri yoksa satır yazılmamıştır.
> ⛔ Kaynağı olmayan uyarı yazılmaz — "dikkat edilmeli" bir uyarı değildir.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

```
⛔ 1  ARAÇ KUTU SETİ ÖLÇÜLMEDİ — 8,0 s teslim için en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp).
      Ölçülmeden tek kare üretilmez [DERS 23]. → günlük §0 ①
⛔ 2  İTME TESTİ KOŞULMADI — araç uzun bir gövdeyi yatay kaydırabiliyor mu, yoksa hedefte kopyalayıp
      kaynağı siliyor mu [DERS 57 mekanizması]. Bu filmin 1 numaralı riski. → günlük §0 ⑨
⛔ 3  ÖN GÖRSELLEŞTİRME ÇİZİLMEDİ — plan + yan kesit: mahmuz · beş ayak · tabliye kotu · taş köprü ·
      zirve silüeti; burun ucunun her karedeki ayak hizası işaretlenir. Usta kareden ÖNCE.
⛔ 4  A2 SAĞ ŞERİT — kenar ayağı %86,9, sağ sekiz %87,5'te başlıyor. Usta karede ölçülür; taşarsa
      D 380 → 400 m ve bütün yüzdeler yeniden yazılır.
⛔ 5  ÜRETİM GÜNLÜĞÜ BOŞ — dört filmde dört kez ölçülen arıza [DERS 28]; üretim başlamadan §0 dolar.
```

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

```
⚠️ 1  DÜZ IZGARA — 14 eşit kesme; ⑥ METRONOM hükmü beklenir ve kabul edilmiştir (sahip beyanı).
⚠️ 2  DOKUZ A KLİBİ — gölge durur; ③ ZAMAN "donuk" okuyabilir. Her A karesinde mevsim taşıyıcısı +
      eski yol trafiği zorunlu [DERS 47].
⚠️ 3  ÖLÇEK — 3,37 px/m; insan 6 px, araba 15 px. İş büyük makineyle ve BANT'la kanıtlanır [A9-d].
⚠️ 4  İKİ YÜZEY — eski taş köprü ile yeni tabliye; makine hazır olana kaçabilir [DERS 51]. Taş köprü
      her promptta pozitif boş yazılır.
⚠️ 5  SEL KARESİ — su seviyesi kare kare kilitli; taş köprü kemer doğuşuna kadar suda kalır, ÜSTÜ boş
      kalır ve kaybolmaz (çapa).
⚠️ 6  UÇ EKRANI — yalnız son 5 sn kartta; S13–S14 kapanmaz.
```

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

```
· 16 karede SITE / BACKGROUND ve STRUCTURE birebir aynı kelimeler [DERS 20 · 36]
· Her karede iki hareket eden + bir yüzey kanıtı [A6-d]; eski yolda trafik her karede var
· Her karede mevsim taşıyıcısı: melez rengi · kar çizgisi · nehrin rengi/debisi · beton yaşı
· Işık tek gün (üsluplu), takvim yerden okunur; "tek günde çekildi" iddiası hiçbir yerde yok
· Geçici ekipmanın hepsi bir FİİLLE gider; şantiye izleri finalde tamamen silinmez
```

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır "bakılmadı" demektir.
> Kaynak: `DERSLER.md` + `QA/ARSIV_12_MERCEK/00_INDEX.md` film blokları. Tablo BÜYÜR — yeni koşu yeni tekrar
> eden arıza bulursa satır ŞABLONA eklenir, tek filme değil.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Üretim günlüğü tutulmadı → QA arızayı adlandıramadı (dört filmde dört kez) | DERS 28 · 29 · LONG DAY · CROSSING · OVER THE WALL · EMPTY RIDGE | ⛔ AÇIK | günlük §0 doldurulmadan tek kare üretilmez; qa_paket.sh kapısı |
| 2 | Düz ızgara ⑥ METRONOM (üç kez) · varyanslı kurgu RHYTHM (üç kez) — sahip beyanı düz | DERS 13 · 24 · 31 · 44 | ⚠️ KABUL | düz 15 × 8,0 sahip beyanı (16.09.2026) · karşı kayıt PLAN'da · telafi müzik katmanlarında, SÜRE sütununda değil |
| 3 | Kapak kartı beyansız → son sahne sanıldı, ① ve ④ düştü | DERS 4 | ✅ KAPALI | kart 120,0–125,0 · PLAN §TESLİM YAPISI + SPEC künyesi |
| 4 | Zincir koşulmadı → her klip başka bina (⑤ REBUILT · ⑧ APPEARED) | DERS 5 · 25 · 12 | ⛔ AÇIK | zincir üretimde koşulacak: 16 kare, her kareden sonra zincir_kontrol.sh + elle kanıt |
| 5 | Kanıt nesnesi YAZILDI ama zincirde ELLE doğrulanmadı → ilk dikişte öldü | DERS 25 (EMPTY RIDGE'de TUTTU: meşe) | ⛔ AÇIK | kanıt: taş köprü (64 × 21 px) + viraj geometrisi; itme sahnelerinde ilk kesitin koyu döküm derzi |
| 6 | Vinç kancası boş sarktı / bom kadraj dışından / uzun yük havada taşınmadı, hedefte kopyalandı | DERS 8 · 22 · 46 · 57 | ✅ KAPALI | tabliye İTİLİR; vinç yalnız döküm alanında/nehir düzlüğünde, kanca yüklü ve alçak, bom zirve silüetinin altında |
| 7 | Korpusu çoğul yapı tek yazılsa da çoğaldı (türbin → çiftlik) | DERS 55 · 42 | ✅ KAPALI | "exactly one new elevated crossing and one existing stone arch bridge" + günlükte sayım (köprü 1 · viyadük 1) |
| 8 | "no X" / "there is no X" / koşullu cümle özneyi ÜRETTİ | DERS 33 · 35 | ✅ KAPALI | olmayan özne yazılmaz; boş yüzey pozitif tarif edilir ("the deck stays bare") |
| 9 | Güneş diski LIGHTING'de anıldı → kadraja girdi | DERS 39 | ✅ KAPALI | kadraj az 323°–37°, güneş 75°→281° — disk hiçbir karede kadrajda; LIGHTING yalnız açı/gölge/gök |
| 10 | Kış tek klipte başlayıp bitti → izleyici iki kış saydı, süre şişti | DERS 7 · 21 · 26 | ✅ KAPALI | kar vadiye yağmaz; kar çizgisi S6'da iner, S7'de erir — iki sahne, iki kare |
| 11 | İstasyon değişen kesmede yapı yüzdesi de değişti → ③ ⑤ ⑥ aynı saniyede düştü | DERS 52 | ✅ KAPALI | tek istasyon, 16 kare; istasyon değişikliği yok |
| 12 | İki iş yüzeyi varken makine hazır olana gitti (köprü/yol) → iş yüzeyi adsız | DERS 51 · 43 | ⚠️ İZLENİR | iş yüzeyi adıyla + yüzdeyle ("the launched deck top at forty-five percent"); taş köprü her karede pozitif boş; ağır makine taş köprüden geçmez |
| 13 | Ters açılış (bitmiş yapıyla açılıp sökme) vaadi sabote etti | DERS 3 | ✅ KAPALI | S0 ileri yönlü; bitmiş köprü erken görünmez |
| 14 | Blok etiketleri nesre döndü → hem kural hem kapı düştü | DERS 20 | ⛔ AÇIK | sekiz blok etiketi birebir; kapı klasör modunda koşulacak |
| 15 | SÜRE sütunu planda kaldı, kurgu düz kesti | DERS 31 · kesme_kontrol.sh | ⛔ AÇIK | kurgu SÜRE sütunundan kesilir; kesme_kontrol.sh yayından önce koşar (beklenen: PLANIN KENDİSİ DÜZ uyarısı) |
| 16 | Kutu seti ölçülmeden ızgara yazıldı → araç 6,0 verdi, plan 4–10 yazmıştı | DERS 23 · 31 · A7-a | ⛔ AÇIK | kutu seti ÖLÇÜLMEDİ; 8,0 s teslim → kutu ≥ 9,0; ölçüm günlük §0 |
| 17 | Montajda mekanizmayı "çalıştır" yazmak yapıyı çalıştırdı (göbek → rotor) | DERS 56 | ✅ KAPALI | "only the deck slides; the piers stand still" · ışık yalnız S13'te yanar, yapı hareketi yazılmaz |
| 18 | Gölge süpürmesi üretilmedi / güneş donuk (frozen sun) | DERS 32 · 47 · 18 | ⚠️ İZLENİR | altı B klibinde gölge süpürmesi zorunlu; dokuz A klibinde gölge durur ama mevsim taşıyıcısı ve trafik hareketi taşır |
| 19 | Malzeme yoktan var oldu / saydamlıktan belirdi | DERS 48 · 49 | ✅ KAPALI | her kesit döküm alanında doğar, priz alır, sonra itilir; gövdenin önünde hiçbir parça belirmez |
| 20 | Nehir yatağında ilk kaldırma havuz okundu (saha korpusu) | DERS 54 · 34 | ⚠️ İZLENİR | nehir ve ıslak beton havuz okunabilir: kaideler ve döküm yatağı "dry, matte, formed concrete"; sel suyu kahverengi ve AKAR |
| 21 | ⭐ YATAY (ilk film) — kadrajın yanları boş kaldı / çapalar yalnız bir yanda; güvenli alan 16:9 ölçülmedi | KILAVUZ_REHBERI §2.8 (varsayım) | ⚠️ İZLENİR | sol çapa şapel (%28,1) · sağ çapa kaya kulesi (%89,7) · A2 %86,9 sağ sekize çok yakın — usta karede ölçülür |
| 22 | ⭐ YATAY (ilk film) — Σ rejim > 14 h → ışık günü kesmede atladı ya da gece girdi | §2.8 ışık günü kuralı (varsayım) | ✅ KAPALI | Σ = 13,5 h (6 B + 9 A) ≤ 14 · gece yok · G0 −5°, G15 −1° alacakaranlık |

---

## ✅ KAPI

```
□ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
□ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
□ tekrar eden arıza tablosunun HER satırı cevaplandı (tablo büyür, sayı buraya yazılmaz)
→ üçü de ✅ ise 05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md doldurulabilir
```
