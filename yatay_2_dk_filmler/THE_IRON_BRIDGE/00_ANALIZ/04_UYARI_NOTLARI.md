# ⚠️ THE_IRON_BRIDGE — UYARI NOTLARI

> Kart Y2 §00_ANALIZ adım 04.
> Her satır 01_QA_DERS_HASADI veya 02_KONSEPT_VE_RISK'ten düşer.
> Üretimde bu listeyi takip et. Satır kapatılınca ✅ yaz.

---

## 🔴 KRİTİK (üretim öncesi çözülmezse BLOCK)

| # | Uyarı | Kaynak | Çözüm | Durum |
|:-:|---|---|---|:-:|
| U1 | "bridge" korpusu ikinci köprü doğurur | DERS 55 + R1 | Tüm promptlarda: "one single pedestrian footbridge … the only crossing visible" | ⬜ |
| U2 | Kemer konsolu havada asılı çizilir | DERS 57 + R2 | Her I2V'de: "arch rests on the temporary support tower — not suspended in air" | ⬜ |
| U3 | G0–G2 nehir yatağı su havuzu okunur | DERS 54 + R3 | Görsel promptlarda: "dry and sandy riverbed, no standing water" | ⬜ |
| U4 | S8 orta açıklık sahnesine başka aşama sıkıştırıldı | Köprü kartı §3 | S8 yalnız son kaynak anını içerir; başka ilerleme yok | ⬜ |
| U5 | Blok etiketleri birebir değil | DERS 20 | ### 📸 GÖRSEL ve ### 🎥 I2V — kapı bunları sayar | ⬜ |

---

## 🟡 ÖNEMLİ (üretimde sahne sahne kontrol)

| # | Uyarı | Kaynak | Çözüm | Durum |
|:-:|---|---|---|:-:|
| U6 | Mevsim değişimi aniden atlıyor | DERS 7 prensip | S4 son saniyelerinde yaprak sararmaya başlar; S5 açılışında tam sarı-turuncu | ⬜ |
| U7 | İşçi görünmüyor ya da netleşiyor | DERS 33 | "workers move as blurred motion traces only, never sharp or stationary" | ⬜ |
| U8 | Metin yüzeylerde (kiriş / beton / kule) | DERS 35 | Negatif çekirdekte: "no text, no markings, no labels on any surface" | ⬜ |
| U9 | AT THIS STAGE cümlesi o karedeki durumu değil genel yapıyı tarif ediyor | DERS 36 | Her görsel promptta AT THIS STAGE: o anki kemer yüzdesi + tabliye durumu | ⬜ |
| U10 | Kemer parçaları kaynak deposunda görünmüyor | DERS 48 | G3'ten itibaren sol kıyı deposunda çelik profil istifi kadrajın kenarında | ⬜ |
| U11 | Nehir yüzeyi + tabliye iki yatay "deck" oluşturuyor | DERS 51 | Her promptta nehir "river surface" olarak adlandırılır; tabliye "footbridge deck" | ⬜ |
| U12 | G6 bölüm sınırı kare ışık veya yapı atlıyor | DERS 52 | G6 kontrol listesi 03_SAHNE_SIRALAMASI §3'te — her iki bölüm dosyasında aynı değerler | ⬜ |
| U13 | Geçici kule ve kutu perde DEĞİŞMEZLER'e yazılmış | DERS 1 | SITE TEXTURE blokuna + SÖKÜM satırına taşı | ⬜ |
| U14 | Kanıt nesnesi (meşe) zincirsiz kalıyor | DERS 25 | Her üretim adımında zincir_kontrol.sh + ELLE ✓/✗ | ⬜ |

---

## 🔵 MEVSİM KONTROL LİSTESİ (üretimde sahne sahne işaretle)

| S | Beklenen | Nehir | Gökyüzü | Ağaçlar | ✓ |
|:-:|---|---|---|---|:-:|
| S0 | Nisan sabahı | mavi, düşük, berrak | açık mavi | koyu yeşil yaprak | ⬜ |
| S1 | Nisan | mavi, düşük | açık mavi | koyu yeşil | ⬜ |
| S2 | Mayıs | mavi-yeşil, düşük | açık mavi | koyu yeşil | ⬜ |
| S3 | Haziran | mavi-yeşil, normal | açık mavi + beyaz bulut | koyu yeşil | ⬜ |
| S4 | Temmuz | mavi, normal | kobalt mavi | koyu yeşil + S4 sonunda SAR! | ⬜ |
| S5 | Kasım | kahverengi-gri, YÜKSEK | gri bulutlu | sarı-turuncu yaprak | ⬜ |
| S6 | Ocak | TAŞKIN kahverengi çamurlu | gri kapalı | çıplak dal, kar yok | ⬜ |
| S7 | Mart | kahverengi, çekilmiş | soluk gri-mavi | ilk tomurcuk (çok az) | ⬜ |
| S8 | Nisan | mavi, normal | açık mavi | koyu yeşil (yeni yaprak) | ⬜ |
| S9 | Mayıs | mavi, normal | açık mavi | koyu yeşil | ⬜ |
| S10 | Haziran akşamüstü | mavi, düşük | altın saate geçiş | koyu yeşil | ⬜ |
| S11 | Temmuz akşamı | mavi, düşük, yavaş | altın saat pembe-turuncu | koyu yeşil + kesim alanında genç filiz | ⬜ |
