# 🔬 THE SEA MILL — QA SPEC

```
⛔ Bu dosya PLANIN DEĞİL, TESLİMİN kapısıdır. Her madde TEK KAREDE ya da TEK KLİPTE ölçülür.
   Ölçülemeyen bir madde bu dosyaya yazılmaz.
KAYNAK  dikey_shorts/THE_SEA_MILL/THE_SEA_MILL_DIKEY_TIMELAPSE.md
IZGARA  6 × 8,0 = 48,0 sn · 7 görsel (G0–G6) + 6 I2V · ⭐ REJİM B × 5 → G × 1 (saat son kesmede durur)
SCENE BLOCK / END CARD   48,0 sn sahne bloğu · ⛔ KAPAK KARTI YOK
DURUM   ⛔ ÜRETİLMEDİ — hiçbir madde henüz KOŞULMADI
```

---

## 1. ⭐ FİNAL KARE KANITI — 47,95 sn (S5'in son karesi)

```
KOMUT    ffmpeg -ss 47.95 -i teslim.mp4 -frames:v 1 kanit.jpg
O KAREDE GÖRÜNMESİ GEREKEN — yedisi birden:
  ① ⭐ dört bezli yelken DİK HAÇ duruşunda: üst uç x 495 · üstten 481 ± 4 · alt uç üstten 1002 ± 4 · sol uç x 237 ·
     sağ uç x 706 (469 ± 4 px en) · göbek x 495 · üstten 741
  ② ⭐ DÖRT SICAK IŞIK: kapının yanında fener (x ≈ 455 · üstten ≈ 1060) + gövdenin sol yüzünde üst üste üç pencere
     (x 390 · 397 · 404 · üstten 1022 · 950 · 879)
  ③ tekne iskelede: x 153 → 334, su hattı üstten 1375 → 1325; kıçında TEK figür, sırtı kameraya
  ④ mavna YOK; deniz ufka kadar boş
  ⑤ teras korkuluğu, koyu ahşap kapı, dört yelkenin bezi yerinde
  ⑥ mavi saat: gök koyu mavi, sağda ufkun üstünde soluk pembe bant; değirmenin her parçası OKUNUR (DERS 45)
  ⑦ üç çapa yerinde: kamera adacığının kıyısı (alt %5,5) · deniz ufku %50 · iki uzak adacık (x ≈ 173 / 907)
⛔ Yedisinden biri yoksa FİLM TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.
⛔ TUTUŞ YOK: bu filmin finali HAREKETİN KENDİSİDİR (rejim G · P5-a). Kanıt karesi son karedir ve G6'nın
   birebir kendisidir; yelkenler bu karede DİK HAÇTA olmalıdır.
```

---

## 2. ⭐ DÖNEN HAÇ KAPISI — filmin en ağır hareketi, üretimin İLK sınavı [DERS 56 · P5-d]

```
NEREDE   S5 (G5 → G6). Haç G3'ten G5'e kadar X duruşunda KİLİTLİDİR; yalnız S5'te döner.
NEDİR    dört kafes yelken (12,5 m · ≈ 2,4 m en · bezli) tek rijit haç olarak göbek çevresinde.

  ① DÖRT KOL, HER KAREDE. S5'in hiçbir karesinde yelken sayısı 4'ten farklı değildir.
     ⛔ Üç ya da beş kol, kolların birleşmesi, bulanık disk = klip düşer.
  ② HAÇ RİJİT. Kollar arası açı her karede 90° (±3°); kol boyu sabit (dik haçta yatay kollar 237 / 706,
     X'te uçlar 318 / 648 — uzak kol perspektifle KISA görünür, ⛔ dönerken boy değiştirmez).
  ③ YÖN TEK: önden bakışta saat yönünün TERSİ. Sol üst kol yukarı, dikeye doğru gider.
     ⛔ Ters yön, durup geri dönme ya da salınım = klip düşer.
  ④ AÇI: 0,0–1,0 sn 0° (fren kapalı) · sonra monoton artar · 8,0 sn'de tam 45° (dik haç).
     Ölçüm (sol üst kolun ucundan): 0 · 2 · 4 · 6 · 8 sn → 0° · küçük · artan · artan · 45°. Azalan değer = düşer.
     ⛔ 45°'yi aşıp geri dönmek ya da 90°'ye varmak = klip düşer (G6 dik haç DEĞİLDİR).
  ⑤ ALT YELKEN teras korkuluğunun ÜSTÜNDEN geçer (dik haçta alt uç +14,0 m, korkuluk +11,1 m). Kesişme = düşer.
  ⑥ BEZ YERİNDE: dönerken bez yırtılmaz, uçmaz, kafesten ayrılmaz.
⭐ IŞIK SIRASI (aynı klipte): fener ≈ 1,5 sn · alt pencere ≈ 3,0 · orta ≈ 4,5 · üst ≈ 6,0. Aşağıdan yukarı.
   ⛔ Bir ışığın sönmesi ya da sıranın tersine dönmesi = klip düşer.
⛔ YEDEK: S5 tutmazsa KAPSAM DARALIR — G6 = G5 + dört ışık (açı aynı), dönüş vuruşu düşer. ⚠️ Fikrin ana vaadi
   kaybolur; sahip kararı.
```

---

## 3. ⭐ BAŞLIK KAPISI — tek kaldırma [DERS 57 · 8 · 46 · 49]

```
NEREDE   S2'nin son 1,5 saniyesi (G2 → G3) ve S3'ün ilk 3 saniyesi (G3 → G4).
  ① G2'de başlık (sivri başlık + X duruşunda dört ÇIPLAK direk) mavnadaki sehpanın ÜSTÜNDEDİR: göbek x 779 ·
     üstten 1032 · üst uçlar 662 → 884. Sheerleg'in kancası kısa dört kollu sapanla başlığa ZATEN bağlıdır.
  ② BAŞLIK KOPYALANMAZ. Hiçbir karede iki başlık yoktur; hedefte bir kopya belirip sehpadaki silinmez.
     ⛔ Aynı karede iki başlık = klip düşer. ⛔ Saydamlıktan beliren başlık = klip düşer [DERS 49].
  ③ HAÇ HAVADA DÖNMEZ. Sehpada X'tir, havada X'tir, oturunca X'tir. Taşıma YALNIZ ötelemedir.
  ④ YÜK YOLU HER KAREDE: A-çerçeve (pruvaya pimli) → kanca bloğu → kısa gergin sapan → başlık.
     G3'te kanca üstten 610 · A-çerçeve başı 555 · başlık göbeği 720 (gövde tepesinin 1 m üstü).
  ⑤ S3 0,0–1,5 sn: başlık DÜZ aşağı iner ve oturur; sapan ANCAK oturduktan sonra gevşer.
  ⑥ BOŞ KANCA YOK: G0, G1 ve G4'te A-çerçeve güverteye YATIK, kanca bloğu güverteye bağlıdır. Havada sarkan boş
     kanca görülen kare düşer [DERS 8].
⭐ KORPUS KONTROLÜ: "windmill|turbine|wind farm|crane|sailing|sailboat|yacht" desenleri yedi görselin ve altı I2V'nin
   İNGİLİZCE metninde 0 olmalı (plan Türkçesinde DEĞİL — orada uyarı olarak geçer).
   ⭐ KOŞULACAK (yalnız PROMPTLAR bölümünün kod blokları):
      sed -n '/^# 🎥 PROMPTLAR/,/^# 🎞️ KURGU/p' <plan.md> | awk '/^```$/{f=!f;next} f' \
        | grep -ciE "\b(windmills?|turbines?|wind ?farms?|cranes?|sailing|sailboats?|yachts?)\b"     → 0
   ⚠️ DESEN FİLMİN KENDİ SÖZLÜĞÜNE KARŞI TEST EDİLDİ [P18-g · P22-e]: bölüm sınırı olmadan aynı grep planın
      Türkçe uyarılarını da okuyor ve 8 yanlış pozitif veriyor; bölüm sınırıyla 0.
   ⭐ "boat" yalnız 4 blokta (S4 I2V · G5 · S5 I2V · G6); "turn/turns/turning" yalnız 2 blokta (S5 I2V · G6):
      sed -n '/^# 🎥 PROMPTLAR/,/^# 🎞️ KURGU/p' <plan.md> \
        | awk '/^```$/{f=!f; if(f) n++; next} f && tolower($0) ~ /(^|[^a-z])boats?([^a-z]|$)/ {print n}' | sort -u | wc -l   → 4
      (aynı komut (turn|turns|turning) ile → 2 blok: 12 ve 13)
      ⚠️ BSD awk "\b" tanımaz; ilk deneme 0 döndürdü — kelime sınırı karakter sınıfıyla yazıldı [P18-g].
⛔ YEDEK: S2 tutmazsa KAPSAM DARALIR — sehpa mavnanın kadraj dışındaki kıç tarafına alınır, başlık kadraja ZATEN
   HAVADA sağ kenardan girer; G2'nin "başlık güvertede bekliyor" vuruşu düşer.
```

---

## 4. ⭐ DEFTER KAPISI — YAPININ EN YÜKSEK BAĞLI NOKTASI + MAVNA YÜKÜ + KUMMEL

```
KUMMEL (bedel tanığı)  G0 53 × 78 px (x 424 → 477 · üstten 1112 → 1190) → G1 0 px
  ⛔ G1'den sonra kayanın üstünde beyaz taş kümesi YOKTUR. Taşları mavnada beyaz yığındır (x ≈ 711 · üstten ≈ 1178)
     ve G1–G4'te orada DURUR; G5'te mavnayla birlikte yoktur.

EN YÜKSEK BAĞLI NOKTA (üstten px · askıdaki yük SAYILMAZ)
  kare      G0   G1     G2     G3    G4    G5    G6
  hedef     —    1193   1077   785   527   527   481
  tolerans  —    ±4     ±3     ±3    ±3    ±3    ±3
  ⛔ DÜŞME ① herhangi bir karede bir öncekinden YÜKSEK px (= alçak yapı) ise o kare düşer.
  ⛔ DÜŞME ② G4 ve G5 arasında haç açısı değişirse kare düşer (fren kilidi — S4'te dönüş YOK).
  ⭐ G5 → G6'daki 46 px'i inşaat değil DÖNÜŞ ekler.

MAVNA YÜKÜ (DEFTER-2 · tek karede sayılır)
  kare           G0   G1   G2   G3   G4   G5
  granit sırası   4    4    0    0    0    —   (mavna yok)
  kereste yığını  3    3    3    0    0    —
  sehpada başlık  —    —    ✓    —    —    —   (G1'de sandık + 4 direk, G2'de başlık)
  beyaz yığın     —    ✓    ✓    ✓    ✓    —
  ⛔ Hiçbir sayı bir sonraki karede ARTMAZ. Mavna G5'te kadrajda görülürse kare düşer.

YELKEN (S3 · S4)
  S3: ızgara 0 → 4, sıra sol alt → sağ alt → sağ üst → sol üst (≈ 3,0 · 4,25 · 5,5 · 6,75 sn başlar)
  S4: bez 0 → 4, 0,0–2,5 sn · her bez iç uçtaki rulodan dışa açılır
  ⛔ Izgara ya da bez bir anda tümüyle belirirse (saydamlıktan) klip düşer [DERS 49].
```

---

## 5. ⭐ IŞIK VE ZAMAN KAPISI — iki saat

```
S0–S4 — GÖLGE SÜPÜRMESİ (rejim B · her klip ≈ 35°)
  kare   saat    azimut   yükseklik   gölge (kadrajda: 0 uzağa · − sol · + sağ)
  G0     09:00   128,4°   26,3°       −81°
  G1     11:00   161,7°   34,8°       −47°
  G2     13:00   198,3°   34,8°       −11°
  G3     15:00   231,6°   26,3°       +23°
  G4     17:00   260,0°   12,8°       +51° · gövde gölgesi 110 m, mavnanın üstünde
  —      18:50   283,9°   −0,8°       batış — S4 içinde ≈ 7,33 sn
  ⛔ DÜŞME ① gölge yönü hiçbir karede geri dönmez (soldan sağa monoton).
  ⛔ DÜŞME ② B kliplerinde gölgeler DONMAZ [DERS 47]: işçi ve araç izse gölge süpürür.
  ⛔ DÜŞME ③ G4'te değirmenin gölgesi mavnanın üstüne düşmüyorsa ışık yönü yanlıştır.

S5 — SAAT DURUR, IŞIK SAYILIR (rejim G)
  G5  güneş −2,0° · ışık 0      G6  güneş −2,0° · ışık 4 (fener + 3 pencere)
  ⛔ DÜŞME ④ S5'te gök rengi değişirse (kararma ya da aydınlanma) saat durmamıştır — rejim kaçağı.
  ⭐ DÜŞME ⑤ G6 zifiri karanlıksa ya da değirmen siyah siluetse film düşer [DERS 45].
⛔ GÜNEŞ HİÇBİR KAREDE KADRAJDA DEĞİL (azimut 128° → 286°, kadraj 6,1° … 51,9°). Kadrajda disk, huzme ya da güneş
   parlaması görünürse istasyon yanlıştır [DERS 32 · 39].
```

---

## 6. ⛔ G5 = G6 KİMLİĞİ — kapak kanıtının kendisi

```
ARADA SEKİZ SANİYE VAR. Altı şey BİREBİR aynı olmalı:
  ① kaya, kaide, teras korkuluğu, gövde, başlık, kapı, üç pencerenin yeri, iskele (±2 px)
  ② dört yelkenin boyu, eni, bezi; göbek x 495 · üstten 741
  ③ ışık: gök koyu mavi, sağda soluk pembe bant — kararmaz
  ④ teknenin yeri (x 153 → 334 ± 6 — dalga payı)
  ⑤ ÜÇ ÇAPA ±2 px: kamera adacığının kıyısı · deniz ufku · iki uzak adacık
  ⑥ deniz boş, mavna yok
İZİN VERİLEN DÖRT FARK — başka hiçbiri değil:
  ⓐ yelkenler 45° döner (X → dik haç, saat yönünün tersi)
  ⓑ fener ve üç pencere yanar
  ⓒ teknedeki figürün duruşu
  ⓓ dalga ve köpük deseni
⛔ Beşinci bir fark varsa kapak kanıtı düşer [DERS 30].
⭐ KOŞ:  bash araclar/zincir_kontrol.sh g6_kaynak.jpg kapak.png   → çıkış 0 olmalı
```

---

## 7. KADRAJ KİLİTLERİ — ±2 px [sahip kararı 19.09.2026]

```
⭐ SIRA ÖNEMLİ: önce ÜÇ ÇAPAYA bak. Üçü tutmuyorsa geri kalanı ölçme, İSTASYON oynamıştır.
  ① KAMERA ADACIĞININ KIYISI  alt %5,53 (üstten 1814'ün altı) · kenardan kenara
  ② DENİZ UFKU                %50,00 (960 px) · kenardan kenara · EĞİM SIFIR
  ③ İKİ UZAK ADACIK           x ≈ 173 ve x ≈ 907 · ufkun hemen üstü
SONRA yapı kilitleri:
  kaya su hattı           x 219 → 708 (489 px) · en alçak üstten 1330
  değirmen ekseni         x 450 · teras 1077 · gövde tepesi 785 · başlık tepesi 678
  kaide                   x 323 → 576 (253 px) · 1193 → 1077
  gövde                   ayak 357 → 543 · tepe 397 → 504
  göbek                   x 495 · üstten 741
  X uçları (G3–G5)        318 / 648 · üstten 527 / 583 (üst) · 923 / 928 (alt)
  dik haç (G6)            üst 481 · alt 1002 · sol 237 · sağ 706
  tekne (G5–G6)           x 153 → 334 · su hattı 1375 → 1325 · köşk üstü 1261
⛔ GÜVENLİ ALAN: kanıt nesnelerinin hiçbiri y 1436'nın altına ya da x 838'in sağına geçmez.
   ⚠️ Tekne başı sol sınıra 31 px; sehpadaki başlığın sağ kolu (G2, geçici) sağ beşte bire 20 px taşar — beyanlı.
⛔ SU SEVİYESİ KİLİT DEĞİLDİR ama SABİTTİR: Baltık'ta gelgit santimetre mertebesindedir; kaya su hattı yedi karede
   aynı yerde durur. Su hattı > 3 px oynarsa kare düşer (THE TIDE GATE'in kot tablosu bu filmde GEREKMEZ).
```

---

## 8. YÜK YOLU VE FİZİK KAPISI [FIZIK_VE_AGIRLIK · DERS 8 · 46 · 57]

```
  S0   kummel taşları → elle → paletli taşıyıcı → çelik köprü → mavna güvertesi
       beton → karıştırıcı → hortum → kalıp → düzlenmiş kaya; ankraj demirleri delinmiş deliklerde
  S1   granit blok → paletli taşıyıcı → köprü → halka temel → ankraj → kaya; iskele (jetty) → çelik kazık → deniz tabanı
  S2   kereste → taşıyıcı → iskele vinci (scaffold hoist) → teras; başlık → sapan → kanca → A-çerçeve → pruva → mavna
  S3   başlık → gövde tepesi → köşe direkleri → taban kirişi → taş teras → kaide → halka temel → kaya
  G6   yelkenler → göbek → mil → başlık → gövde → kaide → temel → kaya
  ⛔ Her karede en az ÜÇ temas cümlesi. Asılı tek cisim başlıktır ve TEK bir sapana bağlıdır.
  ⛔ FREN KİLİDİ: G3, G4 ve G5'te haç X açısında AYNIDIR (±1°). S3 ve S4'te haç hareket ederse klip düşer [DERS 56].
  ⛔ Mavna ve tekne yüzer; ikisi de halatla bağlıdır. Mavnanın yeri G0–G4'te SABİTTİR (±3 px, dalga payı).
```

---

## 9. SAYIM KAPISI [DERS 55]

```
Yedi karenin yedisinde de kadrajda ŞUNLAR VARDIR:
  ① kaya ② deniz ufku ③ iki uzak adacık ④ kamera adacığının kıyısı
Yedi karenin hiçbirinde kadrajda ŞUNLAR YOKTUR:
  ⛔ ikinci değirmen · rüzgâr türbini · deniz feneri · ikinci kule
  ⛔ yelkenli tekne · ikinci tekne · G5'ten önce balıkçı teknesi (tekne S4'ün 6,5. sn'sinde SOLDAN girer)
  ⛔ G5–G6'da mavna (S4'ün 5,5–7,0 sn'sinde SAĞDAN çıkar)
  ⛔ uzak adacıklarda yapı ya da ışık
⚠️ EN OLASI MODEL ARIZASI: değirmen korpusu ÇOĞULDUR (Kinderdijk); "mill + sea" ayrıca rüzgâr çiftliği çağırır.
   Her kare bu listeye karşı okunur.
```

---

## 10. ⭐ REJİM KAPISI — B × 5 → G × 1

```
  S0–S4  rejim B · 2 sa / 8 sn = 900× · işçiler YUMUŞAK İZ (2–4 kişi) · dalga tepeleri yumuşak beyaz şerit ·
                                         kayanın çevresinde beyaz köpük YAKASI · bulutlar ufka doğru akar ve uzar ·
                                         gölge ≈ 35° süpürür
  S5     rejim G · 8 sn / 8 sn =   1× · ⭐ GERÇEK dalga (keskin tepe, köpük, sıçrayan su) · tek figür, sırtı kameraya,
                                         yüz okunmaz, İZ YOK · bulutlar DURUR · gölge yok (güneş battı)
  ⛔ B kliplerinde net, donmuş figür = rejim kaçağı [DERS 15 · 50].
  ⛔ G klibinde iz bırakan figür, akan bulut ya da süt gibi deniz = rejim kaçağı.
  ⭐ 40,0'DEKİ DİKİŞ BEYANLIDIR [P5-c · P10-b]: deniz dokusu ipekten dalgaya döner. ③ ZAMAN ve ⑤ DEVAMLILIK bu
     kesmeyi kusur saymaz; saymazsa ölçülmesi gereken şey, dalganın yalnız BU kesmede değişmesidir.
⭐ ÖLÇÜLMEDİ: rejim G depoda ikinci kez yapının kendi hareketi için koşuluyor (ilk: ONE MORE TURN — ölçülmedi).
   ⑥ merceği B → G kesmesini ritim mi kopukluk mu okuyacak, ilk üretimde görülecek.
```

---

## 11. ⭐ SES KAPISI — DİEGETİK

```
⛔ MÜZİK YOK. Yatak: dalga ve rüzgâr, baştan sona.
  ① ⭐ İLK SES (0,0–1,0): bir taşın düşüşü — kummelin tepe taşı.
  ② 8,0–16,0 keskinin granite düzenli vuruşu — filmin ilk ritmik sesi.
  ③ ⭐ 24,0–25,5 başlığın oturuşu: ilk yarının EN YÜKSEK sesi; tek, derin, ahşap.
  ④ 32,0–40,0 mavnanın dizeli SAĞA uzaklaşır, küçük bir motor SOLDAN yaklaşır ve susar.
  ⑤ ⭐ 40,0–41,0 SESSİZLİK PENCERESİ: motor yok, yalnız gerçek dalga ve rüzgâr. ⛔ Buraya efekt konmaz.
  ⑥ ⭐ 41,0 fren boşalışı: tek, tok, metalik "tak". Ölçüm: bu 0,2 saniyenin tepe seviyesi önceki 1,0 saniyenin
     RMS'inden en az 12 dB yüksek.
  ⑦ ⭐ 41,0–48,0 ahşap gıcırtısı + dişli gümbürtüsü + yelken "vuuş"ları. SES KANITI: ilk ses bir DÜŞÜŞ, son ses
     bir DÖNÜŞ.
  ⛔ Anlatıcı, konuşma, "epik" vurgu efekti, tekne düdüğü YOK · martı en fazla bir kez · 150 Hz altında tek taşıyıcı yok.
```

---

## 12. ZAMAN VE IŞIK GÜNÜ

```
REJİM      5 × B (2 sa) + 1 × G (8 sn) = 10 sa 0 dk 8 sn
PENCERE    09:00 → 19:00:08 (yerel güneş saati) · 60,2° kuzey · 5 eylül · δ +6,2° · batış 18:50
IŞIK GÜNÜ  ≤ 14 sa ✓ · gece yok · final mavi saatte, güneş −2,0° (DERS 45 — okunur)
⭐ MERTEBE BEYANI [HAVA_VE_ATMOSFER §5 · P1-c]: "tek bir eylül günü, sabahtan alacakaranlığa". ③ merceğinin
   "TIME READ FROM THE FILM ALONE" satırı bununla karşılaştırılır. ⚠️ Gerçekte bu iş haftalar sürer — film onu
   tek günün ışığına sıkıştırır; "haftalar" okunursa bu bir hata değil, beyanlı hız bedelinin görünmesidir.
```

---

## 13. ⚠️ BİLİNEN RİSKLER — üretimden önce oku

```
① ⭐ EN BÜYÜK RİSK — DÖNEN HAÇ (§2). Pilot S5. ⛔ Pilot üçlü geçmeden kalan klipler üretilmez.
② ⭐ İKİNCİ RİSK — BAŞLIĞIN KALDIRILIŞI (§3). İkinci pilot S2.
③ KORPUS: rüzgâr türbini, yelkenli tekne, ikinci değirmen (§9).
④ FREN KAÇAĞI: S3–S4'te haç dönebilir (§8).
⑤ PENCERE YELKEN ARKASINDA: G5'te üst pencere ile X'in sol alt yelkeni arasında 10 px var; örtülürse G5'te 2 pencere
   görünür (kusur değil), G6'da 3 pencere görünmek ZORUNDADIR.
⑥ DONUK İŞÇİ (§10) · ⑦ KARANLIK FİNAL (§5 ⑤) · ⑧ DENİZ DOKUSU DİKİŞİ (§10 — beyanlı)
⑨ HIZ: tek günde bir değirmen — beyanlı bedel; ④ / ⑧ "bu kadar hızlı olmaz" derse kusur değildir.
⑩ ⭐ KAPAKTA SPOİLER. Kapak bitmiş değirmeni gösterir (sahip kuralı: kapak = GN). Beyanlıdır [KAPAK §1].
```
