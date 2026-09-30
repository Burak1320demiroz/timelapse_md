# 🔬 THE LAST LIFT — QA ŞARTNAMESİ

```
KAPSAM     10 sahne × 6,0 sn = 60,0 sn · 11 görsel (G0…G10) + 10 I2V · tek istasyon (HOME)
AMAÇ       Bu dosya "güzel mi" diye sormaz. Tek soru: ⭐ 60.000 KİŞİLİK STADYUM ÇANAĞI VE 260 M'LİK
           ÇELİK ÇATI, UFUK ÇİZGİSİNE VE GEOMETRİK MERDİVENE GÖRE DOĞRU YERDE Mİ — on bir karede,
           ±2 piksel içinde ve doğru inşaat mantığıyla mı üretildi.
DURUM      ⛔ ÜRETİLMEDİ — bu şartname ÖLÇÜM BEKLİYOR. Aşağıdaki sayılar plandan türetilmiş HEDEFTİR.
TARİH      28.09.2026
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
ZAMAN        58,0 – 60,0 sn aralığı (S9'un son 2,0 saniyesi)
KAYNAK       ⭐ YALNIZ G10 (USTA KARE) — teslimin tek referans karesi
TUTUŞ        S9'un son ≥2,0 saniyesi sabit KADRAJ (HOME), sabit YAPI (+52,0 m taç çatı),
             sabit IŞIK (altın saat günbatımı) [DERS 30]. FİNAL KARE KANITI 0:59,0'dan alınır.

KANIT LİSTESİ — tek karede beş nesne doğrulanır:
  ① ⭐ 260 M ÇELİK TAÇ ÇATI: +52,0 m kotunda, 32 çelik kolon başlığına oturmuş ve kaynaklanmış.
     Tepe noktası ufuk çizgisinin tam 45 px ALTINDA (−45 ± 2 px). PTFE membran gergin.
  ② ⭐ 60.000 MONOBLOK KOLTUK: 32 prekast tribün bay'i boyunca kırmızı, beyaz ve lacivert sıralar
     geometrik ve tam dolu. Boşluksuz çanak ovali (%100 kapalı).
  ③ ⭐ NİZAMİ HİBRİT ÇİM SAHA: 105 × 68 m ebadında, iki tonlu biçilmiş yeşil şeritler,
     tebeşir beyazı taç/kale çizgileri, orta yuvarlak ve iki beyaz çelik kale direği.
  ④ ⭐ GEÇİCİ STRAND JACK KULELERİ YOK: S5–S7'de ufku 85 px aşan dört köşe kulesi TAMAMEN
     SÖKÜLMÜŞTÜR. Ufku kesen hiçbir geçici kule veya vinç kafesi kalmamıştır.
  ⑤ ⭐ DEĞİŞMEYEN ÇAPALAR: Kuzey-kuzeybatı orman sırtı (ufkun 90 px üstü, 1647 px tabandan),
     iki şeritli asfalt karayolu (120 px en) ve ufuk çizgisi (tabandan 1557 px, %81,09).

⛔ DÜŞME ŞARTI: Final karesinde bu beş kanıttan biri eksikse, çatı havada askıda kalmışsa,
               çim deseni yapay bir leke gibi görünüyorsa veya geçici kuleler sökülmemişse film DÜŞER.
```

---

## 2. §1 DEFTER KAPISI — yapı tepe kotu ve ufuk mesafesi

```
ÖLÇÜLEN    Her karede: stadyumun en üst yapı elemanının y pikseli  −  ufuk çizgisinin y pikseli (1557 px)
YÖNTEM     ① Ufuk çizgisi: kadrajın sol ve sağ kenarlarında ayrı ayrı ölçülür (1557 px tabandan)
           ② Yapı tepesi: stadyum merkez ekseninde en yüksek yapı elemanı sınırı
           ③ Fark işaretli olarak yazılır (tepe ufkun üstündeyse +)

HEDEF      G0      G1      G2      G3      G4      G5      G6      G7      G8      G9     G10
          −667    −715    −685    −580    −245    +85     +85     +85     −45     −45     −45   px
TOLERANS   ±2 px [sahip kararı 19.09.2026]

⭐ ÜÇ YASA:
   YASA A   G1 → G4 arasında defter HER ADIMDA ARTAR (−715 → −685 → −580 → −245 px).
            Yapı çukurdan yükselip ufka doğru tırmanır.
   YASA B   G5'te strand jack kuleleri dikilerek UFUK ÇİZGİSİNİ KESER (+85 px) ve G7'ye kadar sabit kalır.
   YASA C   G8'de çatı kolonlara kilitlenir, kuleler sökülür ve defter −45 px'e OTURUR.
            G8, G9 ve G10'da defter KESİNLİKLE SABİTTİR (−45 px).

⛔ DÖRT DÜŞME ŞARTI:
   ① G5–G7 arasında kule tepesi ufkun altına inerse (+85 px tutmazsa)
   ② G8–G10 arasında çatı kotu −45 px'ten 2 px'ten fazla saparsa
   ③ G4'te kolonlar dikilmeden çatı görünürse
   ④ Ufuk çizgisi sağ ve sol kenarda 1 px'ten fazla ayrışırsa (roll hatası)
```

---

## 3. §2 ÇAPRAZ DEFTER — tribün bay sayısı ve çatı açıklığı

```
ÖLÇÜLEN    1) Prekast tribün tamamlanma yüzdesi / bay sayısı (32 bay tam çanak)
           2) 260 m çelik uzay kafes çatının düşey konumu

HEDEFLER:
   G0-G2   Tribün bay: 0 bay (%0) · Çatı: YOK
   G3      ⭐ Tribün bay: 14 bay (%43,75 dolu — güney crescent) · Çatı: YOK
   G4      ⭐ Tribün bay: 32 bay (%100 kapalı çanak) · 32 dış kolon (+38 m)
   G5      Tribün bay: 32 bay (karlı) · 4 köşe kulesi (+65 m) · Çatı: sahada parça modüller
   G6      Tribün bay: 32 bay · 4 köşe kulesi · ⭐ Çatı: yerde tek parça 260 m oval halka (+6 m)
   G7      ⭐ ÇATI KALDIRMA: 260 m çatı yerden 4 m havalanmış (askıda, zeminle temas kesik)
   G8      ⭐ ÇATI KİLİTLİ: 32 kolona kaynaklı (+52 m) · kuleler sökülmüş · 60.000 koltuk
   G9-G10  Teslim: çim serilmiş, çizgiler çekilmiş, çevre düzenlemesi tamam

⛔ DÜŞME ŞARTI: G4'te çanak ovali kapanmamışsa, G6'da çatı yerde birleşik değilse,
               G7'de çatı ile zemin arasında 4 metrelik açık boşluk görünmüyorsa klip düşer.
```

---

## 4. §3 IŞIK VE MEVSİM KAPISI

```
MEVSİM DÖNGÜSÜ (24 Ay):
   G0-G1   Yaz 1. Yıl (Ay 1-3)   → parlak sert yaz ışığı, kuru toprak, kısa gölgeler (az 125°-150°, el 52°-61°)
   G2-G3   Sonbahar 1. Yıl (Ay 6-9) → sararan bitki örtüsü, uzun yatay gölgeler (az 195°-215°, el 48°-38°)
   G4      Kış başı (Ay 12)       → soğuk soluk gök, düşük açılı güneş (az 160°, el 26°)
   G5      ⭐ KIŞ ① (Ay 14)       → karlı zemin ve tribün basamakları, donuk kış ışığı (az 180°, el 24°)
   G6      ⭐ KIŞ ② (Ay 16)       → karlar erir, çamurlu su göletleri, ilkbahar nemi (az 185°, el 44°)
   G7      İlkbahar sonu (Ay 18)  → taze yeşil dağ sırtı, berrak gök, dik bahar güneşi (az 205°, el 56°)
   G8      Erken Yaz 2. Yıl (Ay 21)→ beyaz PTFE membrandan süzülen parlak ışık (az 240°, el 47°)
   G9-G10  ⭐ Yaz 2. Yıl (Ay 24)  → akşam altın saat ve alacakaranlık, amber çatı yansıması (az 265°-280°, el 26°-12°)

⛔ DÜŞME ŞARTI: Güneş hiçbir sahnede kadraja girmez (bearing 315° KB bakış).
               Kış sahnelerinde (G5-G6) kar veya erime izi görünmezse mevsim taşıyıcısı düşer [DERS 14].
```

---

## 5. §4 FİZİK VE YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK §5]

```
YÜK YOLLARI:
   G0-G1   Ekskavatör ve tır ağırlıkları → geniş paletler ve lastikler → sıkışmış kil zemin
   G2      Radyenin devasa kütlesi → 200+ adet betonarme fore kazık → ana kaya
   G3      Prekast tribün basamakları → neopren mesnetler → eğik raker kirişleri → kolonlar → radye
   G4      Çelik kolonlar → taban plakaları ve ankraj bulonları → çevre kazık başlıkları
   G5-G6   4 strand jack kulesi → köşe kazık grupları; yerde çatı → çelik shoring sehpaları
   G7      ⭐ ASILI ÇATI: 260 m çatı yükü → 4 gruptaki yüksek mukavemetli çelik halatlar →
           4 kafes kuledeki hidrolik strand jack üniteleri → köşe kazık temelleri
   G8-G10  ⭐ KİLİTLİ ÇATI: 260 m çatı yükü → 32 çelik kolon başlığı → çevre kolonları → radye → zemin

⛔ DÜŞME ŞARTI: G7'de çatının kablosuz havada süzülmesi ("floating roof" hatası) kesin ret sebebidir.
               Yük yolu her karede fiziksel olarak açık ve doğrulanabilir olmalıdır.
```

---

## 6. §5 HAREKET VE ŞANTİYE İŞİ KAPISI [SANTIYE_HAREKETI §4]

```
REJİMLER:
   S0–S6   rejim B (2 saat / 6,0 sn = 1200×) — gölgeler döner, bulutlar kayar, makineler ve tırlar akar
   S7      ⭐ rejim A (10 dakika / 6,0 sn = 100×) — çatı kaldırma başlangıcı; hidrolik adımlar net okunur
   S8–S9   rejim B (2 saat / 6,0 sn = 1200×) — çevre düzenlemesi, koltuk montajı, çim serme

DENETİM:
   ① Klip boyunca en az 2 hareket eden araç/makine çalışır vaziyette olmalıdır (stands/waits sayılmaz).
   ② S7'de çatı 4 metre yükselirken strand jack kabloları gergin ve titreşimsiz kalmalıdır.
   ③ İnsanlar yalnızca "soft motion streaks" olarak görünür; net yüz veya durağan figür YASAKTIR.
```

---

## 7. §6 KAMERA VE İSTASYON SABİTLİĞİ [KAMERA_ISTASYONU §7]

```
İSTASYON:  h = 45,0 m · D_kenar = 120,0 m · D_eksen = 220,0 m · bearing 315° · tilt 25° aşağı · roll 0°
ÖLÇÜM:     bash araclar/zincir_kontrol.sh <onceki_kare.jpg> <sonraki_kare.jpg> G10_usta.jpg
TOLERANS:  Arka plan nirengi noktalarında piksel kayması |Δ| ≤ 2 px.
           Orman sırtının en yüksek tepesi (tabandan 1647 px) her karede ±1 px içinde kalmalıdır.
           İki şeritli karayolu sağ kenarda 120 px genişliğini asla değiştirmemelidir.
```

---

## 8. §7 ON BÜYÜK RİSK VE ÖNLEMLER

```
①  ⛔ MODEL ÇELİK ÇATIYI YERDE BİRLEŞTİRMEDEN HAVADA BELİRTİR (F05 Sıvı Büyüme):
     Önlem: S5 ve S6'da çatı modülleri ve birleşen halka sahada yerde açıkça gösterildi.
②  ⛔ STRAND JACK KABLOLARI KOPAR VEYA GÖRÜNMEZ (Havada Süzülen Çatı):
     Önlem: G7'de 4 kuleden inen gergin çelik halat demetleri fizik bloğunda açıkça kilitlendi.
③  ⛔ STADYUM ÇANAĞI DİKEY KADRAJA SIĞMAZ VEYA BOŞLUK ÜRETİR:
     Önlem: h=45 m ve tilt −25° kadraj hesabı çanağı tam %63 frame width ile doldurur.
④  ⛔ KIŞ SAHNESİNDE İŞİN DURMASI VEYA İZLERİN KAYBOLMASI:
     Önlem: S5 ve S6'da karda palet izleri, kaynak parlaklıkları ve aktif shoring yazıldı.
⑤  ⛔ ÇİMİN BİR ANDA YEŞİL BOYAYA DÖNMESİ:
     Önlem: S8 ve S9'da rulo çim serme makineleri, şerit çizgileri ve kum rootzone katmanı yazıldı.
⑥  ⛔ ÇATI KİLİTLENDİKTEN SONRA KULELERİN KADRAJDA KALMASI:
     Önlem: S8'de kulelerin vinçlerle parça parça söküldüğü ve sahadan çıkarıldığı kilitlendi.
⑦  ⛔ GÜNEŞİN KADRAJA GİRMESİ VE PARLAMA YAPMASI:
     Önlem: Bearing 315° (KB) seçildi; güneş daima kameranın arkasında veya solunda kalır.
⑧  ⛔ ROLL KAYMASI İLE UFUK ÇİZGİSİNİN EĞİLMESİ:
     Önlem: Roll 0° kilidi ve sol-sağ bant kontrolü (≤1 px fark) şart koşuldu.
⑨  ⛔ TRİBÜN SEGMENTLERİNİN SAYISININ KARIŞMASI:
     Önlem: Tek tek segment değil, 32 bay'lik çanak doluluk oranı (%40 → %100) kilitlendi.
⑩  ⛔ S7'DE IŞIK VEYA HIZ TİTREMESİ:
     Önlem: Rejim A (10 dakika / 6,0 sn) beyan edildi; gölgeler neredeyse sabit, mekanik kaldırma akıcı.
```
