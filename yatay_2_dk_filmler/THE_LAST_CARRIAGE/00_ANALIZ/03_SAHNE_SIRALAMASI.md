# 🎞️ THE_LAST_CARRIAGE — SAHNE SIRALAMASI (aşama merdiveninin türetildiği yer)

> **Girdi:** `02_KONSEPT_VE_RISK.md` §2a iş sırası · onaylı 20 satır (TUR 1).
> **Çıktı:** 20 satır → PLAN §AŞAMA MERDİVENİ · monoton büyüme · rejim toplamı · bölüm sınırı · dikiş denetimi (istasyon kesmesi dâhil).

---

## 1. 🧱 İŞ SIRASI → 20 SATIR [02 §2a]

| gerçek iş adımı | sahip senaryosu | depo S | not |
|---|:-:|:-:|---|
| yerleştirme | S01 | S0 | ⭐ kanca: vagon ilk karede asılı, tabliyenin 1 m üstünde (DERS 57) |
| sabitleme + sapanların çözülmesi | S02 | S1 | vinç sola çekilir · vagon bir daha kalkmaz |
| eski camların sökümü | S03 | S2 | sekiz açıklık boşalır · eski koltuk iskeletleri konteynere |
| pas ve eski boyanın alınması | S04 | S3 | ⭐ kahverengi → gri (00:24–00:32) · B |
| koruyucu + son kat boya | S05 | S4 | ⭐ zümrüt + krem (00:32–00:40) · B |
| çatı kaplaması | S06 | S5 | bakır levhalar · tek vinç kaldırması |
| camlar | S07 | S6 | sekiz yeni cam, mevcut açıklıklara |
| sol geçit | S08 | S7 | ana konuk girişi · sönük lambalar |
| sağ geçit | S09 | S8 | servis + ikinci çıkış · taş basamaklar |
| teras çerçeveleri | S10 | S9 | üç modül · altından kanyon · bölüm sınırı G10 |
| ahşap döşeme | S11 | S10 | ⭐ orta BİLEREK açık · B · sonunda cam sehpası gelir |
| cam döşeme | S12 | S11 | ⭐ ikinci merak cevabı · 1 vinç + 2 el arabası |
| korkuluk | S13 | S12 | + sönük ışık şeridi |
| dış masalar | S14 | S13 | dört masa · cam orta ve kapı önleri boş |
| iç masa + bank | S15 | S14 | 🪟 İÇ İSTASYON · S13 ile aynı on dakika |
| saha temizliği | S16 | S15 | vinç + telehandler + kamyonlar + kasalar çıkar |
| ışıklar | S17 | S16 | alacakaranlık · üç grup sırayla |
| ilk konuklar | S18 | S17 | mavi saat · içerisi dolar |
| masalar canlanır | S19 | S18 | ⭐ gerçek zaman (G) · dış masalar |
| çift camda + tutuş | S20 | S19 | ⭐ gerçek zaman (G) · final |

## 2. 🗺️ SIRALAMA — monoton büyüme

```
S0  iniş                         → + vagon tabliyede (sapanlar bağlı)
S1  çözme                        → (yapı aynı) · − sapanlar, çapraz kiriş avluya
S2  söküm                        → (yapı aynı · yenilemenin ilk adımı) · − eski camlar (kasalarla) · − eski koltuk iskeletleri
S3  pas                          → (yapı aynı) · pas → gri çelik                 − pas (kum torbalarıyla)
S4  boya                         → + zümrüt gövde + krem şerit
S5  çatı                         → + bakır çatı
S6  camlar                       → + sekiz yeni cam
S7  sol geçit                    → + sol geçit (lambalar sönük)
S8  sağ geçit                    → + sağ geçit + taş basamaklar (lambalar sönük)
S9  çerçeveler                   → + üç teras çerçevesi (açık iskelet)
S10 döşeme                       → + ahşap yan bölümler + şerit (orta açık)
S11 cam                          → + üç cam panel
S12 korkuluk                     → + korkuluk (ışık şeridi sönük)
S13 dış masalar                  → (yapı aynı) · + dört masa
S14 🪟 iç (S13 ile paralel)      → + iç masalar + banklar + sarkıt lambalar (sönük)
S15 söküm                        → (yapı aynı) · − vinç, telehandler, kamyonlar, kasalar, konteyner
S16 ışıklar                      → (yapı aynı) · + lambalar YANIK (üç grup)
S17 ilk konuklar                 → (yapı aynı) · + içerisi dolu
S18 terasa çıkış                 → (yapı aynı) · + üç dış masa dolu
S19 çift                         → (yapı aynı) · + çift camda · TUTUŞ
⛔ Hiçbir satır öncekinden az YAPI göstermez ✅ (S2'de giden eski camlar yapının yenilenen parçasıdır, yenisi S6'da; S3'te giden pas
   yapı değil yüzeydir; S15'te giden yalnız şantiye ekipmanı — SÖKÜM; S16–S19 yapıyı KULLANIR)
```

## 3. 📐 DİKİŞ DENETİMİ — mekanik, göz kararı değil [§2.7 · DERS 52]

| dikiş | iki yaka aynı kare | değişen tek şey | kesmede atlamayan |
|---|---|---|---|
| G1 | ✅ ⭐ TEK KALDIRMA | vagon oturdu | sapanlar bağlı, çapraz kiriş kancada, kaya, gölge |
| G2 · G3 | ✅ | sapanlar çözük · camlar sökük | vagon yerinde, pas |
| G4 · G5 | ✅ | gri → yeşil | vinç DIŞ → YÜK (S4 sonu) |
| G6 … G9 | ✅ | sırasıyla çatı · camlar · sol geçit · sağ geçit | vinç 372 · yarık kaya 1649–1806 |
| G10 | ✅ ⭐ bölüm sınırı | teras iskeleti açık | bağıl güneş −111°, öğleden sonra, vinçte döşeme paleti |
| G11 · G12 · G13 | ✅ | ahşap · cam · korkuluk | orta açıklığın yeri ve boyu (679–922) |
| G13 → G15 | ✅ ⭐ İSTASYON KESMESİ (112,0 · 120,0) | dışarıda dört masa (S13'ün işi); S14 içeride, AYNI on dakika | dış yapı iki yakada aynı · iç klip dış büyüme taşımaz |
| G14 → G14′ | iç zincir | masa + bank + sarkıt lamba | sağ uç duvar 884–1079 · pencerede kaya |
| G15 · G16 | ✅ | saha boş | gün batımı, lambalar sönük |
| G16 · G17 | ✅ ⭐ TEK AKŞAM | lambalar sönük → yanık | masalar örtülü, boş |
| G17 · G18 | ✅ | içerisi dolu | lambalar yanık, konuk yerinde |
| G19 | ✅ ⭐ rejim A → G (144,0) | üç dış masa dolu | içerideki konuklar aynı |
| G20 | usta kare | çift camın ortasında | — |

## 4. ☀️ IŞIK GÜNÜ TOPLAMI — rejim sütunu TOPLANIR

```
A  S0 · S1 · S2 · S5 · S6 · S7 · S8 · S9 · S11 · S12 · S13 · S15 · S16 · S17           14 × 10 dk  =  140 dk
A🪟 S14 (S13 ile AYNI 17:10 → 17:20 — toplama EKLENMEZ)                                1 × 10 dk  =  (0)
B  S3 · S4 · S10                                                                     3 × 2 sa   =  6 sa
G  S18 · S19                                                                         2 × 8 sn   =  16 sn
Σ  = 8 sa 20 dk 16 sn ≤ 14 ✓  ·  09:30 → 17:50:16
```

## 5. ⭐ ÜÇ ZORUNLU SATIR — PLAN'a taşındı

```
KANIT   yarık kaya (x 1649–1806 · 157 px) — sağ rafta, tabliyenin sağ ucunun arkasında, tepeden dibe koyu çatlaklı, değişmez
LOOP    G20 ↔ G0: aynı kaya · aynı çam · aynı sırtlar · aynı vagon · G0 asılı paslı vagon ↔ G20 ışıklı restoran + camda çift ·
        sabah ↔ mavi saat
SÖKÜM   cıvata kamyonu (S0) · çapraz kiriş + sapanlar (S1 → avlu) · dolu kasalar + konteyner (S2 →) · kompresör (S3 sonu) · boya
        römorku · kamyonlar (her yük boşalınca gider) · cam sehpası (S11) · VİNÇ + TELEHANDLER + kamyonlar + kasalar + paletler +
        konteyner (S15)
```

## 6. 🔁 ONAYLI HİKÂYEYLE FARK

Bütün farklar `00_HIKAYE_ONAYI.md` SAPMA ①–⑱'de. Sıralamayı değiştiren yok: onaylı 20 satır birebir (sahibin S01–S20'si =
depo S0–S19). Senaryonun kendi metninden farkı yalnız yöntemde: iki kamera aynı 14° eğimle (SAPMA ③); vagon %56 (SAPMA ⑤); son
iki klip gerçek zamanda (SAPMA ⑦); vinç her klipte asılı yükle başlar (SAPMA ⑩); cam iki yoldan gelir (SAPMA ⑫); lambalar önce
sönük takılır (SAPMA ⑭); iç plan S13 ile aynı zaman (SAPMA ⑮).
