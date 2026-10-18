# 🏛️ THE_GRAND_REVIVAL — Yatay 12 Dakika Timelapse Planı (oda oda · sahne sahne)

> **Bu dosyada PROMPT YOKTUR.** 193 prompt oda klasörlerindedir:
> `ODA_01_ON_CEPHE/THE_GRAND_REVIVAL_ODA_01.md` … `ODA_10_AKSAM/THE_GRAND_REVIVAL_ODA_10.md`
> (her sahnenin başında Türkçe **"önceki sahneye göre değişen"** notu, her odanın sonunda `🚪 ODA SON KARESİ`).
> Plan ile prompt ayrı durur (kapı betiği promptu başlıktan sayar). Sahibin yapıştırdığı GPT paketinin İngilizce
> promptları ALINMADI; hepsi deponun PROMPT_SABLONU iskeletiyle yeniden yazıldı. Tek kaynak:
> `00_ANALIZ/05_SAHNE_CALISMALARI/grv_gen.py` + `grv_data.py` + `grv_istasyon.py` (ortak bloklar harfi harfine aynı [DERS 20]).
> Sahne tablosu (BEŞ SORU): `00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md` · onay metni: `00_ANALIZ/00_HIKAYE_ONAYI.md`.

```
DURUM         📝 PROMPTLAR YAZILDI · 18.10.2026 · 10 oda klasörü · 103 görsel + 90 I2V · üretim AÇILMADI
HİKÂYE ONAYI  ✅ 17.10.2026 · sahip · TUR 1/3 — 90 sahnelik dağılım onaylı. Sahip kararları: kamera = paketteki
              9 istasyon (İSTİSNA) · süre 90 × 8,0 + 5 sn kart · final = ışıklar yanar + ilk akşam yemeği ·
              aynasız · kadro iki işçi, ağır yükte dört
⛔ ÜRETİM     ARAÇ KUTU SETİ ölçülmeden ve PİLOT ÜÇLÜ geçmeden tek kare üretilmez
```

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **90 × 8,0 sn = 720,0 sn** | Kapak kartı: **5,0 sn (sonda)** | Toplam: **725,0 sn (12:05)**
Prompt yapısı: ⭐ **90 sahne → 103 görsel + 90 I2V = 193 prompt · T2V YOK** [`KILAVUZ_REHBERI` §2.7]
  görsel = G0…G89 (sahne görseli) + **12 ODA SON KARESİ** (G10′ G17′ G30′ G42′ G54′ G66′ G73′ G80′ G86′ G87′ G88′ G89′) + **G90 = USTA KARE**
  bölüm sınırı kareleri **G30** (oda kesmesine denk: G30′ salon sonu ↔ G30 yemek odası başı) · **G60** (yatak odası zincirinin içinde)
Yapı: **tek katlı, ≈500 m² kireçtaşı villa, yıllardır terk edilmiş** — ön cephe, giriş holü, salon, yemek odası, mutfak,
  ana yatak odası, giyinme odası, banyo, arka veranda · yeniden yapım **oda oda**: her oda harabe açılır, aynı kamerada biter
Saha: **kuru, ılık tepe ülkesi · zeytin ve servi · 38° K · yaz başı (21 Haziran)** — gerçek bir yer, mimar, marka, mağaza ADI YOK (kurgusal)
Zaman yayı: **gerçekte ≈1 restorasyon sezonu → 12 dakika** · ÜSLUP BEYANI: takvim tek bir yaz gününün ışığına sıkıştırıldı —
  "tek günde yapıldı" iddiası DEĞİLDİR; her oda günün bir dilimini alır, kesmede saat geri gitmez
Işık günü: **06:00 → 20:00 · Σ rejim penceresi 14 sa 00 dk ≤ 14** · 84 klip A (10 dk) + **6 klip G** (gerçek zaman, 0 dk)
Kamera mimarisi: ⚠️ **9 SABİT İSTASYON — sahip istisnası 17.10.2026** (kural: en çok 2 · ana ≥ %85) · her oda kendi kamerasında,
  kendi zincirinde; oda sınırı bir KESMEDİR · §ÇOK İSTASYON BEYANI
Izgara: ⛔ **DÜZ — 90 × 8,0** (sahip seçimi) · §DÜZ IZGARA BEYANI
Bölüm (QA/montaj birimi): **BOLUM_1 = S0–S29 (0:00–4:00) · BOLUM_2 = S30–S59 (4:00–8:00) · BOLUM_3 = S60–S89 + USTA KARE + KART (8:00–12:05)**
Prompt dosyası: **ODA_01 … ODA_10** (oda uzunlukları 10 · 7 · 13 · 12 · 12 · 12 · 7 · 7 · 6 · 4 sahne)

_"İlk karede iki işçi çürümüş büyük bir kanepeyi sarmaşıkla örtülü taş kemerden dışarı taşıyor; son karede, mavi akşamda,
aynı evin yemek odasında bronz avize yanık, on sandalyeli ceviz masanın ucunda iki kişi ilk akşam yemeğine oturmuş —
cam kapıların ardında ışıklı veranda."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     90 sahne × 8,0 sn                       = 720,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn (sonda · G90 + başlık "THE GRAND REVIVAL" · tutuştan sonra, erime ≤ 1 sn)
                                                          =   5,0 sn   ← QA dışı · ihrac_kontrol.sh --kart 5,0
──────────────────────────────────────────────────────────────
TOPLAM                                                     725,0 sn (12:05)
HIZ             1x (yatay hat 2x'e çevrilmez [DERS 58])
MÜZİK           ✅ VAR — yatay hat (sahip 05.10.2026) · 120 BPM (8,0 sn = 4 ölçü) · müziksiz pencere 0,0–8,0 (S0) ·
               katman = oda (her oda kesmesi yeni bir ses rengi) · S86–S89 (son 32 sn) incelir, kart tutulan akorla
               biter · ayrıntı THE_GRAND_REVIVAL_MUZIK.md
SES             diegetik yatak her sahnede (tablolarda SES sütunu) · konuşma YOK · ekip sesi yalnız anlaşılmaz uğultu
YAZI            ⛔ YOK — hiçbir yüzeyde okunur yazı, tabela, numara, marka · tek yazı KAPAK KARTI'ndaki başlık
YASAK KELİME    crane · hoist · mirror · television · screen · pool · swimming · fireplace · candle · flame · smoke ·
               fog · mist · haze · glow · bloom · rays · beam · flare · neon · signboard
               (17.10.2026 kesin · üretici denetler — HİÇBİR promptta, negatifte bile geçmez [DERS 59])
               ⭐ "crane · hoist" iç mekâna vinç sokar (ağır yük KAPIDAN, elle ya da sapanla) · "mirror" (sahip kararı:
                  aynasız) yansımada ikinci oda ve kamera üretir · "television · screen" siyah dikdörtgen ve okunur
                  ekran · "pool · swimming" lüks villa korpusundan havuz çağırır · "fireplace · candle · flame · smoke"
                  akşam sahnesini ateşe çevirir · ışık etki adları pozitif tarifle: "lit warm" · "comes on all at
                  once and stays on" [ISIK_FINALI §5]
KELİME KİLİDİ   (uygulandı — üretici denetler) kadro = "the two workers in dark blue shirts and grey trousers" ·
               ağır yük = "four workers in the same dark blue shirts and grey trousers" · ev sahipleri = "two people
               in simple evening clothes" (S86'dan) · araba = "low flat cart" · ön yol = "flagstones" · hol zemini
               = "travertine tiles" · "stone slabs" yalnız banyo duvarında · dış cephe cümlesi "The villa's …"
PROMPT DOSYASI  ODA_01 … ODA_10 — oda sınırı bir KESMEDİR; ODA SON KARESİ (G(n)′) o odanın son klibinin hedefidir
QA BÖLÜMÜ       BOLUM_1 = S0–S29 (0–240,0) · BOLUM_2 = S30–S59 (240,0–480,0) · BOLUM_3 = S60–S89 + USTA KARE (480,0–720,0) + KART
QA BİRİMİ       BÖLÜM — üç bölüm masterı (her biri 240 s) × 5 mercek = 15 ham rapor (yatay_12_dk_filmler/README)
```

⭐ Platform küçük resmi (kapak) **G90'dan** gelir — öncesi/sonrası bölme YOK (sahip kararı 19.09.2026) · `THE_GRAND_REVIVAL_KAPAK.md`.
⛔ Platform son ekranı kartın üstüne konmaz; kullanılacaksa yalnız 720,0–725,0 kartında, başlığın dışında (sağ alt süre alanı boş).

### ⭐ İZLEYİCİ KAPISI [C2 · KILAVUZ_REHBERI §6 · UZUN_FORM §1]

```
İŞLEV ANI         S89 (GERÇEK ZAMAN): iki kişi avizenin altında on sandalyeli masanın ucuna oturur (0–4 sn), 4–8 sn tutuş.
                  Ev "bitti" değil, "yaşanıyor": ilk akşam yemeği. Önceki üç klip ışıkları yakar (S86 hol · S87 salon · S88 dış)
AÇILIŞ NESNESİ    G0: kapı eşiğinde, iki işçinin elinde yarısı dışarıda çürük büyük kanepe + kemeri ve iki pencereyi örten sarmaşık
AÇILIŞ DÜZENİ     ① NESNE kanepe/kemer (0 sn) · ② DOKUNUŞ "from the first frame the sofa is already half out of the door" ·
                  ③ İPUCU kırık pencerelerin ardında karanlık iç (S0) · ④ İLK BÜYÜK SONUÇ sarmaşık iner, kemer açılır (0:08–0:16, S1)
                  AÇILIŞ GERİ ÇEKİLMESİ ⛔ YOK (sabit geniş)
AÇILIŞ–FİNAL      G0 ↔ S88 (G88 → G89′) AYNI KADRAJ (MAIN STATION): sarmaşıklı, kırık pencereli ev, sabah 06:00 ↔ aynı cephe mavi
KAFİYESİ          saatte, iki pencere ışıklı, yol lambaları yanık. Final kare (G90) içeride — kafiye bir klip önce kapanır
MERAK SORUSU      Bu harap villa neye dönüşecek — ve içinde kim yaşayacak?
```

### 🔗 MERAK ZİNCİRİ [UZUN_FORM §3 · 12 dk: 6–7 soru]

| # | soru (izleyicinin kafasında) | açılır | cevaplanır | ekranda |
|:-:|---|:-:|:-:|---|
| 1 | Bu harap villa kurtarılabilir mi? | S0 | S9 | ön cephe yeni: temiz taş, yeni çatı, iki pencere, ceviz kapı, taş yol, bahçe |
| 2 | Kapının ardında ne var? | S9 (içerisi gösterilmedi) | S10 | kesme: holün içi harabe — film içeri girer |
| 3 | Ağır parçalar tek kapıdan nasıl girecek? | S25 (taş sehpa açıklıkta bekler) | S26 · S34 · S48 · S60 · S77 | dört işçi, gerçek zaman, yük yavaş okunur |
| 4 | On kişilik masaya on sandalye gelecek mi? | S34–S35 (masa + 2) | S40 | 2 → 6 → 10, her yük tek sandalye |
| 5 | Mutfak adası tek parça taşla kapanacak mı? | S47 (taş tezgâh kapının içinde) | S48 | taş, sapanlarla adaya iner |
| 6 | Küvet banyoya sığacak mı? | S76 (küvet arabada, kapının içinde) | S77 | gerçek zamanda pencerenin önüne oturur |
| 7 | Bu ev kimin için — biri gelecek mi? | S86 (iki kişi sandıkla girer) | S89 | ilk akşam yemeği |

```
KURAL   ✅ her soru cevaplanmadan bir sonraki açık (③ S25'ten S77'ye kadar zinciri taşır; ⑦ yalnız S86'da açılır)
        ✅ en son cevaplanan soru (⑦) ilk büyük sonuçtan (S1) zayıf değil — insan + ışık + gerçek zaman
        ✅ ilk büyük sonuç 0:16 (12 dk hedefi ≤ 1:00) · doruk S85–S89 = %94–99 (hedef %75–88 ÜSTÜNDE — §UYARILAR U-12)
```

### ⚓ YENİDEN KANCA — oda kesmeleri + oda içi kancalar

Her oda kesmesi bir kancadır: yeni mekân **harabe** açılır (kontrast), kapı çapası bitmiş komşuyu gösterir.
Oda kesmeleri: **80 · 136 · 240 · 336 · 432 · 528 · 584 · 640 · 688 · 696 · 704 · 712 sn**. Oda içi kancalar (tablolarda ⚓):

| oda | kancalar |
|---|---|
| ÖN CEPHE | S0 açılış nesnesi · S1 ilk büyük sonuç · S3 çatı açılır · S5 ilk yeni pencere · S9 içerisi henüz yok |
| HOL | S10 kapının ardı · S12 traverten · S14 avize |
| SALON | S17 · S19 parke · S21 ilk ışık armatürü · S23 ilk kanepe · S25 taş sehpa açıklıkta · S26 G |
| YEMEK | S30 · S32 · S33 masa kapıda · S34 G · S38 sayım · S40 on sandalye |
| MUTFAK | S42 · S45 · S47 tezgâh kapıda · S48 G · S50 |
| YATAK | S54 · S57 başlık · S59 yatak gövdesi kapıda · S60 G · S62 |
| GİYİNME | S66 · S69 · S71 |
| BANYO | S73 · S75 · S76 küvet kapıda · S77 G |
| VERANDA | S80 · S83 · S85 ışıklar |
| AKŞAM | S86 avize · S87 lambalar · S88 kafiye · S89 yemek |

En uzun kancasız dizi 3 klip — UZUN_FORM §4 eşiği tutar. Direnç anları: ağır yük G klipleri (S26 · S34 · S48 · S60 · S77).

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Terk edilmiş büyük bir taş villayı oda oda yeniden yaşanır bir eve çevirmek ve ilk akşam yemeğini o evde yemek.
DİRENÇ   ① ölçek (≈500 m², dokuz mekân, ≈60 büyük parça)  ② TEK KAPI — her odada yük tek bir açıklıktan girer; ağır
         parçalar (taş sehpa · on kişilik masa · taş tezgâh · king yatak gövdesi · küvet) dört işçiyle, gerçek zamanda,
         kapıdan girer, gerekirse modüllerle  ③ çürüme (sarmaşık, nem lekesi, dökülmüş sıva, kırık cam)
         ④ sayım (on sandalye · iki kanepe · iki berjer · dört tabure — model sayıyı bozar)
BEDEL    ⭐ Sarmaşığın yeşil alacakaranlığı — G0'da kemeri ve iki pencereyi örten sarmaşık evin "masal" hâlidir; S1'de
         şerit şerit sökülür, gizem gider, yerine ışık gelir. Bedel bir kez ödenir ve geri dönmez: S88'de aynı kadrajda
         sarmaşık yok, iki pencere ışıklı. Okuma: "ev yenilendi" değil, "AYNI ev yeniden yaşanıyor".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            toz, sarmaşık, çürük eşya — ve evin BOŞLUĞU                                ✅
  □ kadrajda görünüyor mu?    her odanın ilk karesi harabe, son karesi bitmiş; kapılardan komşu oda okunur  ✅
  □ cevap "zaman geçiyor" mu? hayır — "ev yaşanır oldu: ilk yemek"                                       ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: hangi oda · zemin ne · kaç parça mobilya · kaç sandalye/tabure · ışık yanık mı
② KİNETİK BAĞIMSIZLIK   ✅ her klipte iki işçi bir yükü kaynaktan hedefe taşır; G'de dört işçi; finalde ışık ve iki kişi
③ BAŞLIK ŞEMASI         ✅ kapak "THE GRAND REVIVAL" (3 kelime) — YAYIN_PAKETI
④ OMURGA CÜMLESİ        ✅ kanepe çıkar → sarmaşık → cephe → çatı → iki pencere → ceviz kapı → taş yol → bahçe → hol →
                           traverten → avize → konsol → salon → parke → panel → kanepeler → taş sehpa → yemek odası →
                           masa → on sandalye → mutfak → ada → taş tezgâh → yatak odası → king yatak → giyinme →
                           gardıroplar → banyo → küvet → veranda → ışıklar → ev sahipleri → lambalar → mavi saat → yemek
```

---

## 🔒 DEĞİŞMEZLER — kamera, çapalar, yapı [`KILAVUZ_REHBERI` §3]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 ile [DERS 23 · 31]. 8,0 sn teslim → en büyük kutu ≥ 9,0
                 (üret 9,0 → baştan 1,0 kırp). Bu plan yazılabilir, üretim açılamaz.

LENS (hepsi)   24 mm küresel · tam kare YATAY · tilt 0° · roll 0° · göz hizası = ufuk %50
               dış (A · T): f/8 · ISO 100 → akşam ISO 400–800 · iç: f/5.6 · ISO 400 → akşam ISO 800
⛔ HESAP        x_px = 960 + 1280·x/D · y_px(üstten) = 540 − 1280·(y − h)/D · yüzdeler ALT kenardan
⛔ ÖN GÖRSELLEŞTİRME YOK — sayılar yaklaşık; pilot karede ölçülür, fark ≥ 2 px ise üretici düzeltilir
```

| kod | istasyon | konum · h · D · bakış | ⭐ ölçü çapası (her karede aynı genişlik) | yapı çizgileri | sahneler |
|:-:|---|---|---|---|---|
| A | **MAIN STATION** · ön cephe | ön çim · h 1,6 · D 26 m (cephe) · 270° | taş kuş banyosu **86 px** (x 1397–1483) | cephe x 222–1698 · taban %43 · saçak %63 · kemer x 881–1039 | S0–S9 · S88 |
| H | HALL STATION · giriş holü | holün iç ucu · h 1,5 · D 7,0 · 90° | taş kemer **584 px** (x 668–1252) | uzak duvar x 411–1509 · zemin %25 · tavan %96 | S10–S16 · S86 |
| L | SALON STATION · salon | kuzey duvarı · h 1,5 · D 8,5 · 180° | hol açıklığı **542 px** (x 689–1231) | uzak duvar x 207–1713 · zemin %29 · tavan %92 | S17–S29 · S87 |
| D | DINING STATION · yemek odası | doğu duvarı · h 1,5 · D 8,5 · 270° | üç cam kapı **918 px** (x 501–1419) | zemin %29 · kapı üstü %71 | S30–S41 · S89 · G90 |
| K | KITCHEN STATION · mutfak | güney duvarı · h 1,5 · D 7,3 · 0° | yemek odası kapısı **420 px** (x 1031–1451) | uzak duvar x 302–1618 · zemin %26 · tavan %87 · servis kapısı x 329–504 | S42–S53 |
| M | BEDROOM STATION · ana yatak odası | kuzey duvarı · h 1,5 · D 8,0 · 180° | koridor kapısı **192 px** (x 400–592) | uzak duvar x 352–1568 · zemin %28 · tavan %87 | S54–S65 |
| W | DRESSING STATION · giyinme odası | doğu duvarı · h 1,5 · D 8,2 · 270° | yatak odası kapısı **250 px** (x 835–1085) | uzak duvar x 601–1319 · zemin %28 · tavan %77 | S66–S72 |
| B | BATH STATION · banyo | kuzey duvarı · h 1,5 · D 6,0 · 180° | pencere **512 px** (x 704–1216) | denizlik %38 · lento %82 | S73–S79 |
| T | VERANDA STATION · arka bahçe | arka çim · h 1,6 · D 12 m (arka duvar) · 90° | soldan 2. taş kolon **64 px** (x 654–718) | veranda kenarı %31 · çatı kenarı %80 · arka duvar tam en | S80–S85 |

```
┌─ ORTAK ÇAPA CÜMLESİ — A ve sekiz iç istasyonun SITE bloğunda BİREBİR [DERS 10 · ISTASYON §0 ②] ─────────────┐
│ "Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the horizon  │
│  at exactly half the frame height."                                                                        │
│ T (veranda) A ile "Two old olive trees with silver-grey leaves stand …" dizisini paylaşır (≥ 6 kelime)        │
│ ⭐ GÖRSEL BAĞ = KAPI ÇAPALARI: sonraki oda öncekini açıklıktan görür —                                      │
│    salon → bitmiş hol · mutfak → bitmiş yemek odası · giyinme → bitmiş yatak odası · banyo → bitmiş giyinme   │
│    odası · veranda → camlardan bitmiş salon ve yemek odası. Bitmemiş komşu harabe görünür (yemek odası →      │
│    harap mutfak ve veranda · yatak odası → eski giyinme odası · salon → harap veranda)                       │
│ KORPUS KİLİDİ (A · T): "There is exactly one house here, this villa" · her oda: "keeps exactly these openings" │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ─────────────────────────────────────────────────────────────┐
│ ortak STRUCTURE cümlesi (103 karede birebir): "When finished this will be a single-storey limestone villa of   │
│   about five hundred square metres, its high rooms finished in oak, walnut, travertine and bronze."           │
│ ön cephe: uzun alçak kireçtaşı cephe · ortada yuvarlak taş kemer + ceviz çift kanat · kemerin iki yanında     │
│   birer büyük pencere · düz yol kemere · yolun sağında kuş banyosu · iki uçta iki yaşlı zeytin              │
│ hol: 6 m genişlik · yüksek düz tavan · kemer + iki dar pencere · yan duvarlar düz                           │
│ salon: 10 × 9 m · uzak duvarda hol açıklığı · sağ duvar 3 cam kapı (veranda) · sol duvar 1 büyük pencere     │
│ yemek odası: 9 × 6 m · uzak duvar 3 cam kapı (veranda = yük yolu) · sol duvar 2 pencere + mutfak kapısı ·    │
│   sağ duvar düz · masa 10 kişilik, boyu kameraya dönük · sandalye 1 + 1 baş, iki yanda dörder = 10           │
│ mutfak: 7,5 m · uzak duvarda sol uçta camlı servis kapısı (yük yolu) + sağda yemek odası kapısı · sol duvar   │
│   tezgâh üstü geniş pencere · sağ duvar düz + buzdolabı nişi · ada ortada · tabure 4                         │
│ yatak odası: 7,5 m · uzak duvarın sol ucunda koridor kapısı · sağ duvar uzun pencere · sol duvar giyinme kapısı │
│ giyinme odası: 4,5 m genişlik, uzun · uzak duvarda yatak odası kapısı · sol duvarda yüksek şerit pencere ·     │
│   iki uzun duvar = iki gardırop duvarı (düz ceviz kapaklı, AYNASIZ) · orta ada                              │
│ banyo: 6 × 6 m · uzak duvarda geniş pencere · sol duvarda duş nişi · sağ duvarın ucunda giyinme kapısı ·     │
│   bağımsız küvet pencerenin önünde · çift lavabo + iki aplik (AYNASIZ)                                      │
│ veranda: 12 × 5 m · düz ahşap çatı · dış kenarda 4 kare taş kolon · alçak taş basamak · arka duvarda solda    │
│   salonun, sağda yemek odasının üçer cam kapısı                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 🎥 ÇOK İSTASYON BEYANI — sahip istisnası 17.10.2026

```
KARAR        Sahip: "Paketteki 9 kamera" (önerilen tek ana kamera yerine). Kural ISTASYON_VE_IC_MEKAN §1: en çok 2 klip,
             ana istasyon ≥ %85. Bu filmde ana dış istasyon (A) 11 klip (%12); 79 klip sekiz iç/arka istasyonda.
ÖLÇÜLMÜŞ     dört film: OVER THE WALL · THE LONG SHADOW · THE CLOSING SPAN · THE BROKEN CLIMB — çok vantaj
BEDEL        → "SIX SEPARATE SHOTS / ALTI AYRI GÖRÜNTÜ" · bir filmde parçalanma 0,77. Bu risk kabul edilmiş risktir.
DÖRT ŞART    ① SABİT ve tilt 0      ✅ her istasyon kendi içinde kilitli · ufuk her istasyonda %50
             ② ORTAK ÇAPA           ✅ biçimsel (tepe cümlesi + zeytin cümlesi) · görsel: kapı çapaları
             ③ DIŞ BÜYÜME TAŞIMAZ   ✗ KASITLI — istasyonlar paralel değil SIRALI: her oda kendi büyümesini taşır
                                      (film "oda oda" anlatır). Saat zinciri kesmede sürer, geri gitmez
             ④ BEYANLI              ✅ bu bölüm + QA_SPEC künyesi + günlükte İSTASYON sütunu
KARŞI ÖNLEM  ① her oda tam bir zincir (6–13 klip) — kesme bir olay sınırıdır, kararsız ara değil · ② her oda aynı
             kalıpla açılır (harabe → boşaltma → kabuk → zemin → ışık → mobilya) · ③ kapı çapası bitmiş komşuyu
             gösterir · ④ aynı kadro, aynı kıyafet, aynı araba her odada · ⑤ ışık lekesi saatle kayar
❶ AÇIK KARAR  QA merceklerine (kör) "film dokuz sabit kamerayla oda oda çekildi" nötr gerçek satırı verilsin mi?
             Verilirse ② merceği kesmeyi ihlal saymaz; verilmezse ölçüm dürüst kalır ama ALTI AYRI GÖRÜNTÜ beklenir.
             Varsayılan: VERİLMEZ (kör mercek ilkesi) — sahip seçer.
```

### 📒 DEFTERLER — sahne aralığına bağlı hâller

| defter | hâl | kareler |
|---|---|---|
| **KADRO** | iki işçi, koyu mavi gömlek + gri pantolon — her A klibinde hareket bulanığı, yüz yok | S0–S88 |
| | dört işçi, aynı kıyafet — geç teslimat klibinin sonunda iki işçi daha katılır (S25 · S33 · S47 · S59 · S76), ağır yükü G klibinde dördü taşır; sonraki A klibinde yine iki | S25–S26 · S33–S34 · S47–S48 · S59–S60 · S76–S77 |
| | iki kişi, sade akşam kıyafeti (ev sahipleri) — S86'da sandıkla girer | S86 · S89 · G90 |
| | insansız: ODA SON KARELERİ ("stands quiet") | G10′ … G89′ |
| **ARABA** | tek alçak düz araba — her odada kapı/açıklıkta; S88'de yoldan kadraj dışına çıkar | S0–S88 |
| **GEÇ TESLİMAT** | ağır yük bir önceki klibin hedef karesinde kapının içinde, arabada BEKLER | G26 sehpa · G34 masa · G48 tezgâh · G60 yatak gövdesi · G77 küvet |
| **SANDALYE** | 0 → 2 (G36) → 6 (G39) → 10 (G41+) · iki baş + iki yanda dörder | S35 · S38 · S40 |
| **SALON** | kanepe 1 (G24) → 2 (G25) · berjer 2 (G26) · taş sehpa (G27) · yan sehpa 2 (G29) | S23–S29 |
| **TABURE** | 2 (G53) → 4 (G54′) | S52 · S53 |
| **MEMBRAN** | gri koruma membranı her odada döşeme sonrası yürüme hattında → oda sonunda rulo | oda içi |
| | ⛔ final karelerde YOK (G87′ · G88′ · G89 · G90) | S86–S89 |
| **IŞIK** | hol avizesi asılı sönük (G15–G86) → yanık (G87′+) · salon halka ışık sönük (G22–G88) → yanık (G88′) · | |
| | veranda aplikleri yanık (G86′+) · yemek odası avizesi yanık (G89 · G90) · ön pencereler: sağ yanık (G88) → ikisi + yol (G89′) | |
| **KAPI ÇAPASI** | salonun açıklığında bitmiş hol (S17+) · mutfak kapısından bitmiş yemek odası (S42+) · giyinme kapısından bitmiş yatak odası (S66+) · banyo kapısından bitmiş giyinme odası (S73+) · veranda camlarından bitmiş salon + yemek odası (S80+) | |
| **VERANDA (camlardan)** | harap (L ve D zincirlerinde) → bitmiş, aplikler yanık (L2 · D2) | |
| **ÖRTÜ** | salon mobilyası toz örtülü (G87) → örtüler kalkar (G88′) | S87 |

---

## ☀️ IŞIK GÜNÜ VE REJİM [ZAMAN_VE_ISIK · SANTIYE_HAREKETI §1 · HAVA_VE_ATMOSFER]

```
GÜN        21 Haziran · 38° K · güneş saati · doğum ≈04:41 · batım ≈19:19 (az ≈300°)
GÜNEŞ      06:00 az 71° el 14° → 13:00 öğle el 75° → 19:19 batım → 20:00 az 307° el −7° (mavi saat)
           her istasyonun bakışı başka: güneş her odada kendi penceresinden girer, ışık lekesi zeminde saatle kayar
           — iç mekânın zaman taşıyıcısı [ISTASYON_VE_IC_MEKAN §1 ışık]. Güneş hiçbir karede kadraja girmez
REJİM      A (≈10 dk / klip)  84 klip  = 14 sa 00 dk
           G (gerçek zaman)    6 klip  =  0 dk  → S26 · S34 · S48 · S60 · S77 (ağır yük) · S89 (ilk yemek)
           B · C               YOK (Σ 14 sınırında)
Σ          06:00 → 20:00 = 14 sa 00 dk ≤ 14 ✅ · G klibinin saati bir sonraki A klibinin başlangıcıdır (S26 = S27 = 10:20)
ODA SAATİ  A 06:00–07:40 sabah · H 07:40–08:50 · L 08:50–10:50 · D 10:50–12:40 öğle · K 12:40–14:30 · M 14:30–16:20 ·
           W 16:20–17:30 · B 17:30–18:30 altın saat · T 18:30–19:30 batım · AKŞAM 19:30–20:00 alacakaranlık → mavi saat
MEVSİM TAŞIYICISI  tek yaz günü [DERS 14]: güneş azimutu 71° → 307° · iç mekânda pencere lekesinin yönü ve boyu (sabah
           uzun ve alçak → öğle kısa, dik → akşam uzun, sıcak) · pencereden görünen gök (sabah açık mavi → öğle derin
           mavi + küçük kümülüs → akşam altın → mavi saat) · dış kliplerde gölge süpürmesi (A sabah · T akşam) ·
           bahçe yeşili (S9) · ağustosböceği sesi öğleden sonra (SES)
⚠️ G DİKİŞLERİ  A → G → A (S25→S26→S27 · S33→S34→S35 · S47→S48→S49 · S59→S60→S61 · S76→S77→S78): ışık lekesi G'de
           durur, A'da yürür — beyanlı dikiş · S88 → S89 hem istasyon kesmesi hem A → G
```

---

## 🪜 AŞAMA MERDİVENİ — oda düzeyi · DÜZ IZGARA BEYANI

| ODA | S | SÜRE | saat | aşama fiilleri | MEVSİM TAŞIYICISI |
|---|---|---|---|---|---|
| ODA 01 ön cephe | S0–S9 | 10 × 8,0 = 80,0 sn | 06:00–07:40 | boşalt → sarmaşık → yıka → çatı sök/kapat → iki pencere → kapı → yol → bahçe | uzun sabah gölgeleri sağdan sola kısalır |
| ODA 02 hol | S10–S16 | 7 × 8,0 = 56,0 sn | 07:40–08:50 | boşalt → sıva → traverten → boya → avize → konsol → bank + tablo | dar pencerelerden giren leke yükselir |
| ODA 03 salon | S17–S29 | 13 × 8,0 = 104,0 sn | 08:50–10:50 | boşalt → boya → parke → panel → ışık → halı → kanepeler → berjerler → **taş sehpa (G)** → konsol → yan sehpalar → lambader | sol pencere lekesi zeminde kısalır |
| ODA 04 yemek | S30–S41 | 12 × 8,0 = 96,0 sn | 10:50–12:40 | boşalt → boya → taş zemin → avize → **masa (G)** → 2 → büfe → dolap → 6 → perde → 10 → tablo + çiçek | öğle: leke en kısa, gök derin mavi |
| ODA 05 mutfak | S42–S53 | 12 × 8,0 = 96,0 sn | 12:40–14:30 | söküm → boya → zemin → kiler → alt dolaplar → ada → **taş tezgâh (G)** → paneller → buzdolabı → fırın → 2 → 4 tabure | leke sol pencereden tezgâha döner |
| ODA 06 yatak | S54–S65 | 12 × 8,0 = 96,0 sn | 14:30–16:20 | boşalt → boya → parke → başlık → perde → halı → **king yatak (G)** → şilte → komodinler → bank → şezlong → konsol | sağ pencereden uzayan ikindi lekesi |
| ODA 07 giyinme | S66–S72 | 7 × 8,0 = 56,0 sn | 16:20–17:30 | raflar sökülür → boya → zemin → sol gardırop → sağ gardırop → ada → bank | şerit pencereden ısınan ışık |
| ODA 08 banyo | S73–S79 | 7 × 8,0 = 56,0 sn | 17:30–18:30 | moloz → taş duvar → taş zemin → lavabolar → **küvet (G)** → batarya → bank + havlu | altın saat, pencere sıcak |
| ODA 09 veranda | S80–S85 | 6 × 8,0 = 48,0 sn | 18:30–19:30 | döşeme → dış kanepe → iki koltuk → sehpa → bank → saksılar + ışıklar | batım: gölgeler uzar, gök altından maviye |
| ODA 10 akşam | S86–S89 | 4 × 8,0 = 32,0 sn | 19:30–20:00 | hol avizesi → salon lambaları → dış cephe mavi saat → **ilk yemek (G)** | alacakaranlık → mavi saat, yapay ışık devralır |

```
DÜZ IZGARA BEYANI  Her sahne 8,0 sn (sahip seçimi · KILAVUZ_REHBERI §2.2 karşı kayıt · C1-e). ⑥ METRONOM riski kabul
                   edilmiş risktir. Ritim klip İÇİNDE ve kesmede taşınır: ① oda kesmesi (12 kez, düzensiz aralık:
                   48–104 sn) · ② rejim nabzı A → G → A (beş ağır yük + final) · ③ müzik katmanı oda başına ·
                   ④ yoğun sahnede üç vuruş (sahip 17.10.2026: her klipte üç iş)
```

---

## 🎞️ SAHNE SAHNE PLAN — 10 oda · 90 sahne

> Okuma: **İŞ** klibin içinde ne olduğunu (ve neyin TAŞIDIĞINI — DERS 61: her yeni eleman bir taşıyıcıyla gelir);
> **SAHNE SONU** klibin bittiği hedef kareyi tarif eder (aynı oda: G(n+1) · oda sonu: G(n+1)′). Saat = klibin başındaki ışık.
> Tablolar betikten üretilir — elle düzenlenmez, `grv_data.py` düzenlenip `grv_gen.py` koşulur.

<!-- ÜRETİCİ: SAHNE PLANI BAŞI -->
### 🎬 ODA 1 · ÖN CEPHE — KANEPE ÇIKAR, SARMAŞIK GİDER, CEPHE YENİLENİR

`S0–S9` · #01–10 · **00:00–01:20** · ışık 06:00 → 07:40 · prompt dosyası `ODA_01_ON_CEPHE/THE_GRAND_REVIVAL_ODA_01.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S0** · #01 | 00:00–00:08 · 06:00 · A · A | İki işçi büyük eski kanepeyi kapıdan çıkarıp yoldaki arabaya yükler; ardından kırık koltuk gelir. | G1: Kanepe ve kırık koltuk arabada · sarmaşıklı kemer, kırık pencereler, hasarlı çatı görünür | müziksiz pencere · kanepe ayaklarının taşa sürtmesi, kesik nefes, kuş, uzak köpek | AÇILIŞ NESNESİ · 'from the first frame' · kuşkulu yük yok |
| **S1** · #02 | 00:08–00:16 · 06:10 · A · A | Kemeri ve iki pencereyi örten sarmaşık şerit şerit çekilir, demetler arabaya yüklenir; kemer açığa çıkar. | G2: Kemer ve iki pencere açıklığı sarmaşıksız · taş hâlâ kirli gri · İLK BÜYÜK SONUÇ (0:16) | yaprak hışırtısı, kopan dal çıtırtısı, araba tekerleği | İLK BÜYÜK SONUÇ · açıklık sayısı sabit |
| **S2** · #03 | 00:16–00:24 · 06:20 · A · A | Taş cephe fırça ve kovayla soldan sağa bölge bölge temizlenir; koyu kir aşağı akar. | G3: Bütün cephe açık bej taş · geometri aynı | fırça sürtmesi, kova şıngırtısı, su damlası | yalnız renk değişir |
| **S3** · #04 | 00:24–00:32 · 06:30 · A · A | Kırık kiremitler bölüm bölüm sökülür, kovalarla arabaya iner; çatı altlığı aynı eğimde görünür. | G4: Bütün çatı soyulmuş: gri altlık ve çıtalar aynı eğimde | kiremit kırılması, kova sesi, iskele tıkırtısı | çatı eğimi ve yüksekliği sabit |
| **S4** · #05 | 00:32–00:40 · 06:40 · A · A | Koyu antrasit çatı panelleri sıra sıra döşenir; çatı aynı eğim ve yükseklikte yenilenir. | G5: Çatı yeni, koyu antrasit, aynı siluet çizgisi | vida tabancası, panel tıkırtısı | çatı siluet çizgisi sabit |
| **S5** · #06 | 00:40–00:48 · 06:50 · A · A | Sol büyük pencerenin eski çerçevesi çıkar; yeni bronz çerçeveli cam ünite aynı açıklığa takılır. | G6: Sol pencere yeni, sağ eski | cam sesi, matkap | açıklık ölçüsü sabit |
| **S6** · #07 | 00:48–00:56 · 07:00 · A · A | Sağ büyük pencere aynı ölçüyle yenilenir; iki pencere eşleşir. | G7: İki pencere yeni ve eş | cam, vida | iki pencere aynı ölçü |
| **S7** · #08 | 00:56–01:04 · 07:10 · A · A | Eski kapı sökülür; büyük çift kanatlı ceviz kapı aynı kemer açıklığına takılır. | G8: Ceviz kapı yerinde, kanatlar kapalı · kemer korunur | menteşe, ahşabın tok sesi | kemer korunur |
| **S8** · #09 | 01:04–01:12 · 07:20 · A · A | Eski beton yol kırılır; açık taş plakalar kapıdan dışa döşenir, kenarlara yol lambaları dikilir. | G9: Taş yol tamam, aynı genişlik ve çizgi · kenarlarda sönük yol lambaları | taş üstüne taş, lastik tokmak | yol başı, sonu, genişliği sabit |
| **S9** · #10 | 01:12–01:20 · 07:30 · A · A | İki bitki yatağı temizlenir, kazılır, lavanta ve şimşirle dikilir; sonda araba kadrajdan çekilir. | G10′: Dış cephe ilk tamamlanmış hâlinde · içerisi henüz gösterilmedi | kürek, toprak, kuş | ön cephe bölümünün sonu |

### 🎬 ODA 2 · GİRİŞ HOLÜ — TRAVERTEN, AVİZE, KONSOL

`S10–S16` · #11–17 · **01:20–02:16** · ışık 07:40 → 08:50 · prompt dosyası `ODA_02_GIRIS_HOLU/THE_GRAND_REVIVAL_ODA_02.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S10** · #11 | 01:20–01:28 · 07:40 · A · H | Kırık eski konsol ve döküntü kapıdan dışarı taşınır; hol boşalır. | G11: Hol boş · kemer, kapı, iki dar pencere sabit | kürek sürtmesi, el arabası, kapıdan kuş sesi | kemer + ceviz kapı = A ile ortak çapa |
| **S11** · #12 | 01:28–01:36 · 07:50 · A · H | Bozuk duvar yüzeyleri sıvayla onarılır; duvarlar düz, henüz boyasız. | G12: Duvarlar düz, gri-beyaz, boyasız | mala sürtmesi, kova | — |
| **S12** · #13 | 01:36–01:44 · 08:00 · A · H | Büyük traverten zemin plakaları kapı eşiğinden kameraya doğru döşenir. | G13: Açık traverten zemin kesintisiz | lastik tokmak, mala | — |
| **S13** · #14 | 01:44–01:52 · 08:10 · A · H | Duvarlar sıcak kırık beyaza boyanır. | G14: Duvarlar sıcak kırık beyaz · hol aydınlık | rulo, merdiven tıkırtısı | — |
| **S14** · #15 | 01:52–02:00 · 08:20 · A · H | Büyük bronz avize iki işçi ve sabit merdivenle mevcut bağlantıya takılır. | G15: Avize asılı, sönük | zincir şıkırtısı, merdiven | avize kendi zincirinde · ek kaldırma düzeni yok |
| **S15** · #16 | 02:00–02:08 · 08:30 · A · H | Üç metrelik traverten konsol parça parça taşınıp sol duvara kurulur; üstüne tek vazo konur. | G16: Tek konsol sol duvarda, üstünde tek vazo | taşın taşa oturuşu | tek konsol |
| **S16** · #17 | 02:08–02:16 · 08:40 · A · H | Uzun döşemeli bank sağ duvara, konsolun üstüne büyük tablo; kapı kapanır. Hol tamam. | G17′: Hol tamam: konsol, vazo, tablo, bank, avize | kapı kapanışının tok sesi | ayna yok — tablo (sahip kararı) |

### 🎬 ODA 3 · SALON — PARKE, HALI, İKİ KANEPE, İKİ BERJER, TAŞ SEHPA

`S17–S29` · #18–30 · **02:16–04:00** · ışık 08:50 → 10:50 · prompt dosyası `ODA_03_SALON/THE_GRAND_REVIVAL_ODA_03.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S17** · #18 | 02:16–02:24 · 08:50 · A · L | Kalan eski koltuk ve döküntü hol açıklığından çıkarılır; salon boşalır. Açılıştaki kanepe yeniden görünmez. | G18: Salon boş · açıklıktan bitmiş hol görünür | sürtme, el arabası | açılış kanepesi geri dönmez · hol = ortak çapa |
| **S18** · #19 | 02:24–02:32 · 09:00 · A · L | Duvarlar sıcak fildişine boyanır. | G19: Duvarlar fildişi · pencere, tavan, duvar sınırları aynı | rulo | — |
| **S19** · #20 | 02:32–02:40 · 09:10 · A · L | Geniş açık meşe parke uzak duvardan kameraya doğru, tek yönde döşenir. | G20: Meşe zemin tek yönde | testere, tokmak | döşeme yönü sabit |
| **S20** · #21 | 02:40–02:48 · 09:20 · A · L | Hol açıklığının solundaki duvar bölümüne ceviz paneller takılır. | G21: Ceviz panel yalnız sol bölümde | matkap | açıklık ve duvarın kalanı değişmez |
| **S21** · #22 | 02:48–02:56 · 09:30 · A · L | Bronz halka tavan aydınlatması belirlenen bağlantı noktasına kurulur. | G22: Halka ışık asılı, sönük · yüksekliği sabit | zincir | — |
| **S22** · #23 | 02:56–03:04 · 09:40 · A · L | Büyük krem halı boş zeminin ortasına serilir; köşeleri bundan sonra sabit. | G23: Halı ortada, köşeleri sabit | halının yumuşak düşüşü | halı köşeleri kilit |
| **S23** · #24 | 03:04–03:12 · 09:50 · A · L | Dört kişilik ana kanepe hol açıklığından getirilip halının sol kenarına konur. | G24: Tek ana kanepe | ahşap ayakların meşeye konuşu | tek kanepe |
| **S24** · #25 | 03:12–03:20 · 10:00 · A · L | İkinci büyük kanepe halının karşı kenarına konur. | G25: İki kanepe, aralarında geniş geçiş | ayak sesi, kumaş | iki kanepe |
| **S25** · #26 | 03:20–03:28 · 10:10 · A · L | İki deri berjer uzak köşelere; sonda iki işçi daha katılır, taş sehpa açıklığa gelir. | G26: İki berjer · taş sehpa arabada, açıklığın içinde | deri gıcırtısı, tekerlek | her yük tek berjer · geç teslimat |
| **S26** · #27 | 03:28–03:36 · 10:20 · G · L | GERÇEK ZAMAN · dört işçi taş orta sehpayı arabadan alıp halının ortasına yavaşça indirir. | G27: Sehpa halının ortasında, ayakları halıya basar, kanepelere değmez | taşın yumuşak inişi, nefes | GERÇEK ZAMAN · ağırlık yavaş okunur |
| **S27** · #28 | 03:36–03:44 · 10:20 · A · L | Uzun alçak ceviz konsol ceviz panelin önüne konur. | G28: Konsolun ayak izi sabit | ahşap | — |
| **S28** · #29 | 03:44–03:52 · 10:30 · A · L | İki küçük yan sehpa sırayla, her seferinde tek yük, kanepelerin uçlarına konur. | G29: Tam iki yan sehpa | ayak sesi | sayı 2 |
| **S29** · #30 | 03:52–04:00 · 10:40 · A · L | Lambader sağ kanepenin yanına; büyük taş saksıda genç zeytin cam kapıların yanına. Salon tamam. | G30′: Salon tamam — ilk iç mekân zirvesi · BÖLÜM 1 sonu | saksının taşa oturuşu | BÖLÜM 1 sonu (240,0 sn) |

### 🎬 ODA 4 · YEMEK ODASI — ON KİŞİLİK MASA, 2 → 6 → 10 SANDALYE

`S30–S41` · #31–42 · **04:00–05:36** · ışık 10:50 → 12:40 · prompt dosyası `ODA_04_YEMEK_ODASI/THE_GRAND_REVIVAL_ODA_04.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S30** · #31 | 04:00–04:08 · 10:50 · A · D | Eski masa ve sandalyeler cam kapılardan verandadaki arabaya taşınır; oda boşalır. | G31: Oda boş · mutfak kapısından harap mutfak, camlardan harap veranda | sürtme, tekerlek | yük yolu = cam kapılar (veranda) |
| **S31** · #32 | 04:08–04:16 · 11:00 · A · D | Duvarlar sıcak greje boyanır; tavan ve pencere geometrisi korunur. | G32: Duvarlar grej | rulo | — |
| **S32** · #33 | 04:16–04:24 · 11:10 · A · D | Mat açık taş zemin plakaları cam kapılardan kameraya doğru döşenir. | G33: Taş zemin · desen bundan sonra aynı | lastik tokmak | zemin deseni kilit |
| **S33** · #34 | 04:24–04:32 · 11:20 · A · D | Bronz avize asılır; sonda iki işçi daha katılır, ceviz masa orta cam kapıdan gelir. | G34: Avize merkez ekseninde · masa arabada, kapının içinde | zincir, tekerlek | geç teslimat |
| **S34** · #35 | 04:32–04:40 · 11:30 · G · D | GERÇEK ZAMAN · dört işçi on kişilik ceviz masayı avizenin altına koyar. | G35: Tek masa, tek sabit konum | ahşabın taşa inişi, nefes | GERÇEK ZAMAN · ağırlık yavaş okunur |
| **S35** · #36 | 04:40–04:48 · 11:30 · A · D | İki baş sandalyesi sırayla masanın iki ucuna; toplam iki. | G36: Toplam iki sandalye | ayak sesi | sayı 2 |
| **S36** · #37 | 04:48–04:56 · 11:40 · A · D | Uzun servis büfesi sağ duvara; iki sandalye yerinde, geçiş açık. | G37: Büfe sağ duvarda · iki sandalye aynı yerde | ahşap | büfe geçişi kapatmaz |
| **S37** · #38 | 04:56–05:04 · 11:50 · A · D | Ahşap çerçeveli yüksek sergileme dolabı büfenin ötesine; masa, büfe, iki sandalye korunur. | G38: Tek yeni dolap | cam kapakların hafif tıkırtısı | tek dolap |
| **S38** · #39 | 05:04–05:12 · 12:00 · A · D | Dört yan sandalye tek tek sol yana; toplam altı. SAYIM PİLOTU. | G39: Toplam altı sandalye: iki baş + solda dört | sandalye ayaklarının taşa konuşu ×4 | SAYIM PİLOTU · her yük tek sandalye (DERS 89) |
| **S39** · #40 | 05:12–05:20 · 12:10 · A · D | Tavandan yere perdeler iki pencereye asılır; altı sandalye değişmez. | G40: Perdeler asılı · altı sandalye aynı | halka şıkırtısı | pencere konumu sabit |
| **S40** · #41 | 05:20–05:28 · 12:20 · A · D | Kalan dört sandalye tek tek sağ yana; toplam on. | G41: Toplam on sandalye: iki baş + iki yanda dörder | sandalye ayakları ×4 | sayı 10 · her yük tek sandalye |
| **S41** · #42 | 05:28–05:36 · 12:30 · A · D | Büfenin üstüne büyük tablo; sonda masaya tek çiçek aranjmanı. Oda tamam. | G42′: Masa, on sandalye, büfe, dolap, perde, avize tamam | kapının kapanışı | yemek odası sonu |

### 🎬 ODA 5 · MUTFAK — DOLAPLAR, ADA, TAŞ TEZGÂH, DÖRT TABURE

`S42–S53` · #43–54 · **05:36–07:12** · ışık 12:40 → 14:30 · prompt dosyası `ODA_05_MUTFAK/THE_GRAND_REVIVAL_ODA_05.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S42** · #43 | 05:36–05:44 · 12:40 · A · K | Eski alt dolaplar sökülüp servis kapısından çıkarılır; tesisat duvarı ve kapı açıklıkları değişmez. | G43: Sol duvar çıplak · kapılar aynı | levye, kırılan sunta | tesisat duvarı sabit |
| **S43** · #44 | 05:44–05:52 · 12:50 · A · K | Duvar yüzeyleri onarılıp krem bitiş rengine getirilir. | G44: Duvarlar krem · sınırlar aynı | mala, rulo | — |
| **S44** · #45 | 05:52–06:00 · 13:00 · A · K | Büyük mat taş zemin plakaları döşenir; tezgâh ve ada yerleri boş. | G45: Taş zemin · ada yeri boş | lastik tokmak | — |
| **S45** · #46 | 06:00–06:08 · 13:10 · A · K | Yüksek kiler dolabı bankası modül modül uzak duvara yerleştirilir. | G46: Yüksek dolaplar tek duvarda | matkap, menteşe | tek duvar |
| **S46** · #47 | 06:08–06:16 · 13:20 · A · K | Taş tezgâhlı alt dolap modülleri sol duvar boyunca dizilir; dolap sayısı ve kapak bölümleri sabit kalır. | G47: Alt dolaplar ve tezgâh sol duvarda | tıkırtı, matkap | kapak bölümleri kilit |
| **S47** · #48 | 06:16–06:24 · 13:30 · A · K | Büyük ada gövdesi ortaya getirilir; sonda iki işçi daha katılır, taş tezgâh arabada yanına gelir. | G48: Ada gövdesi ortada, üstü boş · taş tezgâh arabada yanında | tekerlek, nefes | geç teslimat |
| **S48** · #49 | 06:24–06:32 · 13:40 · G · K | GERÇEK ZAMAN · dört işçi kalın taş tezgâhı sapanlarla gövdeye indirir. PİLOT. | G49: Ada tek parça; tezgâh kenarı, kalınlığı, boyu sabit | taşın ahşaba oturuşu, nefes | GERÇEK ZAMAN · PİLOT |
| **S49** · #50 | 06:32–06:40 · 13:40 · A · K | Tezgâh arası taş paneller sol duvara takılır. | G50: Taş paneller yerinde | taş, yapıştırıcı | taş deseni sabit |
| **S50** · #51 | 06:40–06:48 · 13:50 · A · K | Büyük buzdolabı sağ duvardaki boşluğa yerleştirilir. | G51: Buzdolabı yerinde · ön yüzü dolap çizgisinde | tekerlek, tık | dolap çizgisi |
| **S51** · #52 | 06:48–06:56 · 14:00 · A · K | Çift fırın ünitesi ayrılmış dolap yuvasına yerleştirilir; yeni dolap oluşmaz. | G52: Tek fırın ünitesi | metal kızak | yeni dolap yok |
| **S52** · #53 | 06:56–07:04 · 14:10 · A · K | İlk iki bar taburesi adanın oturma kenarına; tam iki. | G53: Tam iki tabure | ayak sesi | sayı 2 |
| **S53** · #54 | 07:04–07:12 · 14:20 · A · K | İkinci tabure çifti gelir; sonda tek kahve makinesi tezgâha konur. Mutfak tamam. | G54′: Dört tabure · ada, kiler, cihazlar, tezgâh tamam | servis kapısının kapanışı | sayı 4 · mutfak sonu |

### 🎬 ODA 6 · ANA YATAK ODASI — BAŞLIK, KING YATAK, KOMODİNLER

`S54–S65` · #55–66 · **07:12–08:48** · ışık 14:30 → 16:20 · prompt dosyası `ODA_06_YATAK_ODASI/THE_GRAND_REVIVAL_ODA_06.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S54** · #55 | 07:12–07:20 · 14:30 · A · M | Eski yatak çerçevesi koridor kapısından çıkarılır; yatak duvarı, pencere ve kapılar aynı. | G55: Oda boş · kapı, pencere, giyinme kapısı aynı | demir şangırtısı | — |
| **S55** · #56 | 07:20–07:28 · 14:40 · A · M | Duvarlar onarılıp sakin sıcak greje getirilir. | G56: Duvar bitişi tamam | mala, rulo | — |
| **S56** · #57 | 07:28–07:36 · 14:50 · A · M | Meşe parke uzak duvardan kameraya doğru döşenir. | G57: Meşe zemin, bu kameraya göre sabit yön | testere, tokmak | döşeme yönü |
| **S57** · #58 | 07:36–07:44 · 15:00 · A · M | Geniş döşemeli başlık paneli uzak duvarın ortasına monte edilir. | G58: Başlık duvarı ölçüsü değişmez | matkap | başlık ortalı |
| **S58** · #59 | 07:44–07:52 · 15:10 · A · M | Tavandan yere perdeler sabit kornişe asılır; pencere ölçüsü ve konumu değişmez. | G59: Perdeler asılı | halka şıkırtısı | pencere ölçüsü sabit |
| **S59** · #60 | 07:52–08:00 · 15:20 · A · M | Büyük halı serilir; sonda iki işçi daha katılır, yatak gövdesi kapıdan gelir. Bölüm 2 sonu. | G60: Halı yerinde · yatak gövdesi arabada, kapının içinde · BÖLÜM 2 sonu (480,0 sn) | halı, nefes | BÖLÜM SINIRI KARESİ G60 · geç teslimat |
| **S60** · #61 | 08:00–08:08 · 15:30 · G · M | GERÇEK ZAMAN · dört işçi king yatak gövdesini başlığa ortalar. | G61: Yatak gövdesi başlığa ortalı | ahşabın halıya inişi, nefes | GERÇEK ZAMAN · BÖLÜM 3 ilk sahnesi |
| **S61** · #62 | 08:08–08:16 · 15:30 · A · M | Şilte gövdeye konur; sonda nevresim ve yastıklar düzenlenir. | G62: Tek yatak, sabit örtü düzeni | kumaş | yatak ölçüsü sabit |
| **S62** · #63 | 08:16–08:24 · 15:40 · A · M | İki komodin sırayla yatağın iki yanına; sonda iki abajur. Toplam iki + iki. | G63: İki komodin, iki abajur | ayak sesi | sayı 2 + 2 |
| **S63** · #64 | 08:24–08:32 · 15:50 · A · M | Yatak ucuna uzun döşemeli bank; geçişler açık. | G64: Bank yatak ucunda, geçişler açık | ahşap | — |
| **S64** · #65 | 08:32–08:40 · 16:00 · A · M | Pencere yanına büyük şezlong; dinlenme köşesi oluşur. | G65: Dinlenme köşesi | kumaş | — |
| **S65** · #66 | 08:40–08:48 · 16:10 · A · M | Makyaj konsolu ve tek pufu sırayla sol duvara; yatak odası tamam. | G66′: Yatak, komodinler, bank, şezlong, makyaj alanı tamam | kapının kapanışı | ayna yok · oda sonu |

### 🎬 ODA 7 · GİYİNME ODASI — İKİ GARDIROP DUVARI, ORTA ADA

`S66–S72` · #67–73 · **08:48–09:44** · ışık 16:20 → 17:30 · prompt dosyası `ODA_07_GIYINME_ODASI/THE_GRAND_REVIVAL_ODA_07.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S66** · #67 | 08:48–08:56 · 16:20 · A · W | Eski açık raflar sökülüp yatak odası kapısından çıkarılır; iki uzun duvar boşalır. | G67: İki uzun duvar boş | çivi gıcırtısı, tahta | — |
| **S67** · #68 | 08:56–09:04 · 16:30 · A · W | Duvarlar sıcak açık renge boyanır; iki uzun duvar aynı. | G68: Duvarlar açık renk | rulo | — |
| **S68** · #69 | 09:04–09:12 · 16:40 · A · W | Meşe zemin döşenir; orta ada yeri boş. | G69: Meşe zemin · ada yeri boş | testere, tokmak | — |
| **S69** · #70 | 09:12–09:20 · 16:50 · A · W | Sol yüksek gardırop modülleri yerleştirilir; modül adedi ve raf düzeni sabit kalır. | G70: Sol gardırop duvarı tam | menteşe, matkap | modül sayısı kilit |
| **S70** · #71 | 09:20–09:28 · 17:00 · A · W | Sağ gardırop bankası düz ceviz kapaklarla yerleştirilir (aynasız). | G71: İki gardırop duvarı eş · ayna yok | menteşe | ayna yok (sahip kararı) |
| **S71** · #72 | 09:28–09:36 · 17:10 · A · W | Geniş çekmeceli orta ada getirilir; iki gardıroba eşit geçiş. | G72: Ada ortada, eşit geçişler | ahşap | eşit geçiş |
| **S72** · #73 | 09:36–09:44 · 17:20 · A · W | Oturma bankı adanın önüne; sonda katlı kıyafetler ve kutular açık raflara. Giyinme odası tamam. | G73′: Bank ve ada ayrı · raflarda sabit sayıda grup | kumaş | raflar çoğalmaz · oda sonu |

### 🎬 ODA 8 · BANYO — TAŞ DUVARLAR, ÇİFT LAVABO, BAĞIMSIZ KÜVET

`S73–S79` · #74–80 · **09:44–10:40** · ışık 17:30 → 18:30 · prompt dosyası `ODA_08_BANYO/THE_GRAND_REVIVAL_ODA_08.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S73** · #74 | 09:44–09:52 · 17:30 · A · B | Önceden boşaltılmış banyoda kalan moloz çıkarılır; küvet ve dolap yerleri boş, duş nişi yerinde. | G74: Zemin temiz · duş nişi yerinde | kürek, kova | duş nişi sabit |
| **S74** · #75 | 09:52–10:00 · 17:40 · A · B | Büyük taş duvar plakaları monte edilir; damarlar ve duş nişi sabitlenir. | G75: Duvarlar taş · damarlar sabit | taş, yapıştırıcı | duvar damarları kilit |
| **S75** · #76 | 10:00–10:08 · 17:50 · A · B | Mat taş zemin döşenir; yön ve derz çizgileri sabit kalır. | G76: Zemin taş · derz yönü kilit | lastik tokmak | derz çizgileri |
| **S76** · #77 | 10:08–10:16 · 18:00 · A · B | Çift lavabolu dolap, üstüne iki aplik (ayna yerine); sonda iki işçi daha katılır, küvet gelir. | G77: Tek dolap bankası, iki lavabo, iki aplik · küvet arabada kapının içinde | tekerlek, nefes | ayna yok — aplik (sahip kararı) · geç teslimat |
| **S77** · #78 | 10:16–10:24 · 18:10 · G · B | GERÇEK ZAMAN · dört işçi bağımsız küveti pencerenin önüne koyar. | G78: Tek küvet, sabit yer | seramiğin taşa inişi, nefes | GERÇEK ZAMAN |
| **S78** · #79 | 10:24–10:32 · 18:10 · A · B | Küvet yanındaki zemin bataryası mevcut çıkışa monte edilir; su gösteri değildir. | G79: Batarya tek ve sabit | anahtar tıkırtısı | su akışı yok |
| **S79** · #80 | 10:32–10:40 · 18:20 · A · B | Döşemeli banyo bankı sol duvara; sonda katlı havlular. Banyo tamam. | G80′: Küvet, dolap, aplikler, bank, duş nişi tamam | kumaş | banyo sonu |

### 🎬 ODA 9 · VERANDA — AHŞAP DÖŞEME, DIŞ MEKÂN OTURMA GRUBU, IŞIKLAR

`S80–S85` · #81–86 · **10:40–11:28** · ışık 18:30 → 19:30 · prompt dosyası `ODA_09_VERANDA/THE_GRAND_REVIVAL_ODA_09.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S80** · #81 | 10:40–10:48 · 18:30 · A · T | Mevcut üstü örtülü verandaya ahşap döşeme sıralar hâlinde serilir; kolonlar ve tavan değişmez. | G81: Ahşap veranda · kolonlar ve tavan aynı | testere, tokmak, akşam kuşları | kolon ve tavan sabit |
| **S81** · #82 | 10:48–10:56 · 18:40 · A · T | Büyük dış mekân kanepesi modülleri sırayla getirilir; tek oturma grubu oluşur. | G82: Tek oturma grubu | kumaş, ayak sesi ahşapta | tek grup |
| **S82** · #83 | 10:56–11:04 · 18:50 · A · T | İki geniş dış mekân koltuğu sırayla; tam iki. | G83: Tam iki koltuk | ayak sesi | sayı 2 |
| **S83** · #84 | 11:04–11:12 · 19:00 · A · T | Büyük dış mekân orta sehpası oturma grubunun ortasına. | G84: Sehpa grubun merkezinde | ahşap | — |
| **S84** · #85 | 11:12–11:20 · 19:10 · A · T | Uzun ahşap bank arka duvarın önüne; açık geçiş korunur. | G85: Bank arka duvarda · geçiş açık | ahşap | geçiş açık |
| **S85** · #86 | 11:20–11:28 · 19:20 · A · T | İki büyük saksı sırayla; sonda güneş batarken mevcut veranda aydınlatması yanar. | G86′: Tamamlanmış veranda, sıcak ışık, bütün mobilya aynı karede | taş, akşam ağustosböcekleri | ışık tek karede yanar (ISIK_FINALI) |

### 🎬 ODA 10 · AKŞAM — IŞIKLAR YANAR, İLK AKŞAM YEMEĞİ

`S86–S89` · #87–90 · **11:28–12:00** · ışık 19:30 → 20:00 · prompt dosyası `ODA_10_AKSAM/THE_GRAND_REVIVAL_ODA_10.md`

| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |
|---|---|---|---|---|---|
| **S86** · #87 | 11:28–11:36 · 19:30 · A · H | Alacakaranlık: ekip son merdiveni çıkarır, ev sahipleri yemek sandığıyla girer; kapı kapanır, hol avizesi yanar. | G87′: Hol avizesi yanık · kapı kapalı | kapının tok sesi, uzak ağustosböceği · müzik inceliyor | ışık tek karede yanar · sahip kararı: final ışıklar |
| **S87** · #88 | 11:36–11:44 · 19:40 · A · L | Son örtüler kanepelerden kalkar, araba dışarı; lambader ve halka ışık yanar. | G88′: Salon lambalı · örtü yok | kumaş hışırtısı · müzik ince | ışık tek karede yanar |
| **S88** · #89 | 11:44–11:52 · 19:50 · A · A | Açılışla aynı açı: ekip arabayı yoldan çıkarır; yol lambaları ve yemek odası penceresi yanar. | G89′: İki pencere yanık, yol ışıkları yanık · açılışla aynı kadraj, karşıt hâl | ağustosböceği, uzak köpek | AÇILIŞ–FİNAL KAFİYESİ · ışık tek karede |
| **S89** · #90 | 11:52–12:00 · 20:00 · G · D | İki kişi avizenin altında masaya oturur (gerçek hız, 0–4 sn), sonra tutuş. İlk akşam yemeği. | G90: USTA KARE G90 — iki kişi sofrada, avize yanık, on sandalye, camların ardında yanık veranda | sandalyelerin taşta hafif sürtmesi, tabak tıkırtısı · müzik tutulan akorla biter | İŞLEV ANI · 4 + 4 · kapak kaynağı |

<!-- ÜRETİCİ: SAHNE PLANI SONU -->

---

## 🌟 USTA KARE — G90 (kapak kaynağı)

```
KADRAJ    DINING STATION, değişmezler aynen · 20:00 mavi saat (güneş ≈ −7°) · göz hizası %50
ODA       grej duvarlar · açık taş zemin · uzun bronz lineer avize iki zincirde, YANIK · on kişilik ceviz masa, boyu kameraya
          dönük · on döşemeli sandalye (iki baş + iki yanda dörder) · sağ duvarda alçak ceviz büfe + üstünde büyük tablo ·
          büfenin ötesinde cam kapaklı ceviz sergi dolabı · sol duvarın iki penceresinde keten perdeler · masa ortasında
          alçak çiçek · mutfak kapısından yumuşak ışıklı bitmiş mutfak
SOFRA     masanın uzak ucu iki kişilik: iki tabak, iki bardak, sürahi, ekmek sepeti · iki kişi uç sandalyenin iki yanındaki
          sandalyelerde karşılıklı oturuyor (yandan, yüz okunmaz)
CAMLAR    üç cam kapı (918 px) — ardında aplikleri yanık veranda, koyu mavi bahçe, ufukta son soluk sıcak bant
⛔ YOK     işçi · araba · membran · merdiven · ayna · mum · ateş · ekran · yazı · ışık huzmesi
```

---

## 🧪 PİLOT ÜÇLÜ — üretimden önce

| # | sahne | neden | geçme ölçütü |
|:-:|---|---|---|
| ① | **S89** (final · G90 dahil) | işlev anı + kapak kaynağı; iki kişi + on sandalye + yanık avize aynı karede | 10 sandalye sayılır · iki kişi oturur, yüz okunmaz · avize yanık · cam kapılar 918 px ± 2 |
| ② | **S38** (sayım pilotu) | 2 → 6 sandalye; DERS 89 "her yük tek sandalye" | G39'da tam altı sandalye · masa yerinde · kapı çapası 918 px |
| ③ | **S48** (taş tezgâh, G) | ağır yük + sapan + dört işçi, gerçek zaman | taş adaya tek parça oturur · kopyalanmaz · eller ve sapan okunur |
| — | S0 (sonra) | açılış nesnesi + MAIN STATION | kuş banyosu 86 px · kanepe ilk karede yarı dışarıda |

İki pilot (①, ②) aynı D zincirindedir: istasyon çapası tek pilotla ölçülür, ikinci pilot sayım riskini ayrı okur.

---

## ✂️ KURGU · KESMELER · BÖLÜMLER

```
KESMELER     oda kesmesi = istasyon kesmesi: 80 · 136 · 240 · 336 · 432 · 528 · 584 · 640 · 688 · 696 · 704 · 712 sn
             kesmede geçiş efekti YOK (düz kesme) · ışık ve saat sürer · ODA SON KARESİ (G(n)′) kesmeden önceki son karedir
BÖLÜM        BOLUM_1 0–240 (A · H · L) — sınır = oda kesmesi (G30′ ↔ G30) · BOLUM_2 240–480 (D · K · M ilk yarı) —
             sınır = G60, yatak odası zincirinin içinde (aynı istasyon, aynı kare) · BOLUM_3 480–720 + KART 720–725
ZİNCİR       her istasyon kendi zinciri: G(n) → I2V → G(n+1) · odanın son klibi → G(n+1)′ · sonraki oda yeni zincirle
             açılır · dönüş istasyonları (H2 · L2 · A2 · D2) kendi istasyonunun son karesinden türetilir (günlük §kare)
KART         720,0–725,0 · G90 + başlık "THE GRAND REVIVAL" sol üst · erime ≤ 1 sn · müzik tutulan akorda
```

---

## ⚠️ UYARILAR VE RİSKLER — onaydan önce bilinmesi gerekenler

| # | risk | nerede | ne yapılacak |
|:-:|---|---|---|
| U-1 | **Dokuz istasyon → "ayrı görüntüler"** (ölçülmüş: dört film) | her oda kesmesi | §ÇOK İSTASYON BEYANI · kapı çapaları · aynı kalıp · ❶ açık karar |
| U-2 | **Sandalye sayısı bozulur** (2 → 6 → 10) [DERS 89] | S35 · S38 · S40 · G90 | her yük tek sandalye · sayı AT THIS STAGE'de · S38 pilot |
| U-3 | **Mobilya teleport olur:** A'da 10 dk'lık taşıma 0,2 sn'de biter | her mobilya klibi | yük kaynağı ilk karede (araba/kapı), taşıyıcı (iki işçi) her klipte; "appear/vanish" yazılmaz |
| U-4 | **Ağır yük havada kopyalanır** [DERS 57] | S26 · S34 · S48 · S60 · S77 | geç teslimat: yük önceki hedef karede kapıda bekler · G klibi gerçek zaman · S48 pilot |
| U-5 | **Cam ayna olur / içeriyi yansıtır** | D cam kapıları · L cam kapıları · K servis kapısı | "clear glass, the … visible through it" · "mirror" YASAK · aynasız sahip kararı |
| U-6 | **G dikişi:** A ↔ G'de ışık lekesi ve hareket hızı değişir | beş ağır yük · S89 | beyanlı dikiş · G klibinin saati bir sonraki A ile aynı |
| U-7 | **Kadro kimliği** odadan odaya değişir (kıyafet, sayı) | 79 iç klip | KELİME KİLİDİ: aynı kadro cümlesi · dört işçi yalnız geç teslimat sonu + G |
| U-8 | **Işık "yavaşça" yanar ya da her şey birden** | S85–S89 | her armatür kendi klibinde, "comes on all at once and stays on" · glow/rays/beam YASAK |
| U-9 | **Kapı çapası tutmaz:** bitmiş komşu oda farklı görünür | S17+ · S42+ · S66+ · S73+ · S80+ | komşunun tarifi o odanın bitmiş defterinden · pilot sonrası elle bakılır |
| U-10 | **Final karede inşaat artığı** | G87′–G90 | membran, araba, merdiven final karelerden düşürüldü · USTA KARE ⛔ listesi |
| U-11 | **Düz ızgara → METRONOM** [DERS 13 · 44] | bütün film | §DÜZ IZGARA BEYANI |
| U-12 | **Doruk geç:** işlev anı %99'da (hedef %75–88) | S86–S89 | sahip kararı (final = ışık + yemek) · ağır yük G'leri ortada direnç taşır |
| U-13 | **Yüz okunur** — S89 iki kişi yandan, 8 m'de | S89 · G90 | "seen from the side, no readable face" · pilot ①'de ölçülür |

---

## 🧭 SAPMALAR — GPT paketinden farklar (sahip onayladı 17.10.2026)

| # | paket | bu plan | neden |
|:-:|---|---|---|
| ① | 96 sahne × 8 = 12:48 | **90 × 8,0 = 12:00 + 5 sn kart** | yatay 12 dk formatı (sahip seçimi) · 96 → 90 birleştirme: benzer kısa işler tek klipte |
| ② | sahneler 01–96 | **S0–S89** · tablolarda # sütunu 01–90 | depo standardı (G0…G90 zinciri) |
| ③ | hol aynası · gardırop aynalı kapakları · banyo aynası | **aynasız**: hol → tablo · gardırop → düz ceviz kapak · banyo → iki aplik | sahip kararı · ayna ikinci oda ve kamera yansıtır |
| ④ | kapakta öncesi/sonrası | **yalnız G90** | sahip kuralı 19.09.2026 |
| ⑤ | kart yok | **5,0 sn kapak kartı sonda** | sahip kuralı 16.10.2026 |
| ⑥ | durağan "bitmiş oda" finalleri | **ışıklar yanar + ilk akşam yemeği** (S86–S89) | sahip seçimi · işlev anı |
| ⑦ | kalabalık ekip | **iki işçi + ağır yükte dört** | sahip seçimi · kimlik ve sayım riski düşer |
| ⑧ | rejim belirtilmemiş | **6 G klibi** (5 ağır yük + final) | 90 × A = 15 sa sınırı aşar; G ağırlığı okutur |
| ⑨ | ışık belirtilmemiş | **tek yaz günü 06:00 → 20:00** · ÜSLUP BEYANI | kesmede ışık atlamaz, Σ ≤ 14 sa [§2.7 ①] |
| ⑩ | 9 kamera | **9 kamera korundu** — sahip istisnası | önerilen tek kamera reddedildi; risk §ÇOK İSTASYON BEYANI'nda |
| ⑪ | şömine, TV, havuz | **yok** — YASAK KELİME | ateş, siyah ekran ve havuz korpusu çağırır |

---

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ HİKÂYE ONAYI (17.10.2026)        00_ANALIZ/00_HIKAYE_ONAYI.md · TUR 1/3
✅ sahne sahne plan                  bu dosya — 90 sahne · 10 oda · defterler · ışık günü
✅ PROMPTLAR                         ODA_01 … ODA_10 · 103 görsel + 90 I2V · üretici 00_ANALIZ/05_SAHNE_CALISMALARI/
✅ PROMPT KAPISI (18.10.2026)         0 BLOCK · 4 FIX — hepsi BEKLENEN:
                                     ① ARAÇ KUTU SETİ ölçülmedi (üretim günü)
                                     ② S89 "ACTIVITY zayıf" — USTA KARE klibi: iki kişi oturur ve 4–8 sn tutuşta
                                        durur; final kasıtlı olarak iş taşımaz
                                     ③ S89 "GEÇİCİ EKİPMAN yok" — yapım bitti; final karede araba, membran, merdiven
                                        bilerek YOK (U-10)
                                     ④ S87 "G88'de yeni eleman: arch, roof" [DERS 61] — YANLIŞ ALARM: G88 başka
                                        istasyonun (A2, ön cephe) ilk karesidir; kemer ve çatı S0–S9'da yapıldı.
                                        Kapı istasyon kesmesini tanımıyor
                                     Koşu: klasör modu 12 dk'yı ve ODA klasörlerini tanımadığı için birleşik dosyayla —
                                     cat THE_GRAND_REVIVAL_PLAN.md ODA_*/THE_GRAND_REVIVAL_ODA_*.md > $TMP/grv.md
                                     python3 araclar/prompt_kontrol.py $TMP/grv.md
⬜ araçlar 12 dk'yı ve çok istasyonu tanımıyor   film_klasoru_ac.sh · sayac.sh · prompt_kontrol.py (BOLUM_3 · ODA · ′ kareler) ·
                                     qa_paket.sh (--bolum 3) · zincir_kontrol (istasyon başına zincir)
⬜ ARAÇ KUTU SETİ                     üretim günü ölçülür (≥ 9,0 sn kutu)
⬜ PİLOT ÜÇLÜ                         S89 · S38 · S48 (sonra S0)
✅ KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC · URETIM_GUNLUGU   bu klasörde
```
