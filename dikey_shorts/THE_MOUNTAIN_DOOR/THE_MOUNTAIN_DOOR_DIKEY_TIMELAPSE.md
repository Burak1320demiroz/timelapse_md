# 🚇 THE MOUNTAIN DOOR — Dağın Kapısı

> # ⛔ BU DOSYA **v1**'DİR — ÜRETİLDİ, ALTI MERCEKLE ÖLÇÜLDÜ, DÜŞTÜ.
>
> `① 1,1Ⓥ` · `② 1,5Ⓥ belgesiz` · `③ 3,6` · `④ 4,0Ⓥ belgesiz` ·
> `⑤ 0,2Ⓥ` · `⑥ 3,5Ⓥ belgesiz` — kayıt: `QA/ARSIV_12_MERCEK/RAPORLAR/THE_MOUNTAIN_DOOR.md`
>
> ⭐ **PROMPT KAPISINDAN GO ALAN TEK FİLM, ALTI MERCEĞİN BEŞİNDE DÜŞTÜ.**
> Kusur promptta değil, ÜRETİM AKIŞINDA: kamera beş klipte de push-in yaptı
> (araç ön ayarı), zincir tutmadı, kanıt nesnesi ilk dikişte kayboldu.
>
> ⛔ DÜŞEN: `① SIX SEPARATE SHOTS` · `② DIFFERENT · APPEARING` (4. kez) ·
> `③ PASSES BUT NOT IN ONE DIRECTION` · `④ NONE FOUND` (4. kez) ·
> `⑤ A SET REBUILT EACH TIME` + kanıt NONE FOUND · `⑥ NEXT · METRONOM` (3. kez)
>
> ⭐ GEÇEN: `③ SEASON CARRIER 10/10` · `VEGETATION 10/10` ·
> zaman tahmini "about 9 to 12 months" — plan 12 ay, İKİNCİ KEZ TUTTU.
>
> Bu filmden çıkan dersler: **23 · 24 · 25 · 26 · 27**
> ⛔ Yeniden ÜRETİLMEZ; önce üretim yordamı düzelir (kayıt §8).

---

Dikey Timelapse Production Document · **v1 · ÜRETİLDİ, ÖLÇÜLDÜ, DÜŞTÜ**
Format: **9:16 (DİKEY)** | Sahne: **5 × 6,0 sn** | Kapak kartı: **5,0 sn** | Toplam: **35,0 sn**
Prompt yapısı: 5 görsel + 5 I2V (birincil) + 5 T2V (yedek) = 15 prompt
Yapı: yol/tünel — dağ portalı (`YAPI_TIPI_KARTLARI §6`)
Saha: dağ/eğim (`SAHA §3.4`) + kar/kış şantiyesi (`SAHA §3.5`)
Zaman yayı: **12 ay** (Temmuz → Temmuz) → 30,0 saniye
Izgara kararı: `KILAVUZ_REHBERI §2.6` · ⚠️ düz ızgara, gerekçesi §2'de

_"Yolun sonu bir kaya duvarıydı. Bir yıl sonra duvarın içinden geçiliyordu —
ve üstündeki eski geçit yolu bir daha kullanılmadı."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     5 sahne × 6,0 sn = 30,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn  =  5,0 sn   ← SAHNE DEĞİL, ayrı denetlenir
──────────────────────────────────────────────
TOPLAM                             35,0 sn
```

⛔ **KAPAK KARTI BİR SAHNE DEĞİLDİR** [DERS 4]. Kart S4'ün usta karesinden
türer ve İngilizce başlık taşır (§11). Beyansız kart QA'yı çökertir.

⛔ **KLİP SÜRESİ HENÜZ ÖLÇÜLMEDİ** [D-d]. Üretimden önce tek test klibi:
```
ffprobe -v error -show_entries format=duration -of csv=p=0 test.mp4
```
Ölçülen 6,0 değilse (örn. 6,004) bu dokümandaki BÜTÜN zaman kodları ve
müzik ızgarası o sayıdan yeniden türetilir.

---

# 1. 🚪 KONSEPT KAPISI

```
VAAT     Vadinin tek çıkışı, kaya yüzünün üstünden dolanan bir geçit yoludur
         ve her kış kapanır. Dağın içinden 620 metrelik bir tünel açılacak.
DİRENÇ   Kaya · kış · eğim. Portal şevi kayanın içine kesilir, kar çizgisi
         vadi tabanına iner ve yılın üç ayında iş neredeyse durur.
BEDEL    ⭐ İKİ TANE, İKİSİ DE EKRANDA KALICI:
         ① Dağın yüzünde açık renkli, kalıcı bir yara: kesilen şev ve
            vadi tabanına dökülen pasa bermi — söküm listesinde YOKTUR,
            film bittiğinde de oradadır.
         ② Üstteki eski geçit yolu. Kadrajda AYNEN durur ama S4'te BOŞTUR;
            alt virajın ağzını açık renkli bir kum bariyeri kapatır.
            Kazanılan geçiş, kaybedilen yoldur.
```

**Üç kabul testi:**

```
① TEK KARE TESTİ       ✅ Kaya yüzündeki koyu dikdörtgen ağız ve altındaki
                          açık pasa bermi tek karede "dağ deliniyor" der;
                          ağzın kaç metre içeri gittiği aşamayı verir.
② KİNETİK BAĞIMSIZLIK  ✅ Sabit planın içinde kamyon damperinin bermiyi bir
                          adım öteye taşıması, kar çizgisinin yamaçta inip
                          çıkması ve gölgenin vadiyi süpürmesi metinsiz okunur.
③ BAŞLIK ŞEMASI        ✅ "THE MOUNTAIN DOOR" — 3 kelime, kapak kartına sığar.
```

---

# 2. ⚠️ DÜZ IZGARA KARARI — gerekçe ve telafi

`KILAVUZ_REHBERI §2.6` düz ızgarayı yasaklamaz ama iki ölçümle uyarır:
CLOSING SPAN ve NARROW LOT, eşit kesme aralığıyla **iki kez `⑥ METRONOM`**
aldı. Bu filmde ızgara **proje sahibi tarafından 5 × 6,0 olarak kilitlendi.**

```
GEREKÇE   Sahne başına tek ve KÜÇÜK bir iş adımı bütçesi korunuyor; süreleri
          bozmak yerine ızgara sabit bırakıldı ve varyans klibin İÇİNE alındı.
⛔ RİSK    ⑥ merceği yine METRONOM verebilir. Makine bunu YAKALAMAZ:
          prompt_kontrol.py süre eşitliğini yalnız 6+ satırlık tabloda BLOCK
          eder, 5 satırda eşik altındadır. Bu risk BİLE BİLE alınmıştır.
```

**⭐ TELAFİ — ritim kesmede değil, klibin içinde:** her sahnenin TEK iş adımı
başka bir saniyede patlar. Kesme aralığı sabit, vuruş yeri değişken.

| Sahne | İş adımının patladığı an | Ne patlar |
|---|---|---|
| S0 | 1,2 sn | kova ilk kez kayayı ısırır — kanca erken |
| S1 | 3,6 sn | bir damper pasa bermisini bir adım öteye taşır |
| S2 | 4,8 sn | kanopi kalıbına döküm — kış geç ve ağır |
| S3 | 2,4 sn | dolgu bir bölme birden seviyelenir — erime hızlandırır |
| S4 | 5,0 sn | ⭐ gölge sınırı portala ulaşır, güneş yeni yola düşer |

```
1,2 → 3,6 → 4,8 → 2,4 → 5,0     ⭐ dizi ne artan ne azalan
```

---

# 3. 🔒 DEĞİŞMEZLER TABLOSU

Her GÖRSEL promptta **birebir, kısaltmasız** tekrarlanır. Köşeli parantez
atfı yasaktır [D-a] — bu dokümandaki beş promptun beşi de aynı bloğu taşır.

```
┌─ KAMERA İSTASYONU (ANA · 5 sahnenin 5'i) ───────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100                          │
│ yükseklik     16,0 m — vadinin karşı yamacındaki kaya sekisi         │
│ mesafe        portaldaki kaya yüzünden 48 m                          │
│ bakış açısı   315° (kuzeybatı) · tilt 0° · roll 0°                   │
│ sabitleme     "a fixed tripod bolted to a rock bench"                │
│ ⛔ Sayılar KAMERA_ISTASYONU §3 formülünden ÇIKTI, seçilmedi:          │
│    kaya yüzü tacı H = 40,0 m · hedef taç ≈ %82                       │
│    D = (H − h) / 0,48 = (40,0 − 16,0) / 0,48 = 50 m                  │
│    Sahada seki 48 m'de → taç %83,3. Üst 1/8 (%87,5) sınırının        │
│    altında kaldığı için 48 m KABUL EDİLDİ.                           │
│ ⛔ DETAY İSTASYONU YOK — 5 sahnelik ızgaranın bedeli [§2.6].          │
└──────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — dördü de SAYILI [DERS 19] ────────────────────┐
│ ① sağda, yüzden ayrık duran çıplak gri KAYA BURNU: üzerinde TAM İKİ  │
│    düşey yarık · alt yarık ağzı 9,0 m · üst yarık ağzı 20,0 m        │
│ ② portalın üstünde kaya yüzünü kesen ESKİ GEÇİT YOLU: kadrajda TAM   │
│    İKİ viraj · alt viraj 30,0 m · üst viraj 37,0 m · kuru taş korkuluk│
│ ③ yol platformunun sol kenarında TEK, ÜSTÜ DÜZ GRANİT KAYA · 2,4 m   │
│    ⭐ ⑤ merceğinin "aynı yer" kanıt nesnesi. Taşınamayacak kadar     │
│       büyüktür ve beş sahnede de aynı yerdedir [NARROW LOT: bu satır │
│       iki filmde NONE FOUND'du].                                     │
│ ④ vadi tabanında TEK KEMERLİ TAŞ KÖPRÜ (tek ayak) + örgülü dere      │
│ ⑤ arkada uzak sırt hattı: geniş bir boyun + sağında TAM BİR kaya boynuzu│
│ ⛔ Beşi de HER karede aynı yerde, aynı boyutta, aynı kelimelerle.     │
└──────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ───────────────────────────────────────────────────┐
│ ufuk çizgisi   kare yüksekliğinin tam %50'sinde (tilt 0° geometrisi) │
│ kare yüzdesi   %50 + (y − 16,0) / 0,72     ← f=24 · h=16,0 · D=48    │
│ yol platformu  %27,8 · portal kemer tacı %40,3 · kaya tacı %83,3     │
│ ⛔ ilerlemeyi kanıtlayan hiçbir şey %25'in altına ve sağ %12,5'e girmez│
└──────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI taşır [DERS 19] ───────────────────┐
│ tüp            620 m uzunluk · 12,4 m kazı genişliği · 9,0 m kemer   │
│ trafik         2 × 3,65 m şerit                                      │
│ portal         21,0 m genişlik · 12,5 m yükseklik başlık duvarı      │
│ kaya sekisi    yüzün 4,0 m içine kesilmiş                            │
│ kanopi         ağzın üstünde 6,0 m derinlik                          │
│ yaklaşım       9,4 m platform · 210 m dolgu                          │
│ istinat duvarı 5,2 m yükseklik · 14 panel · 15,0 m aks aralığı       │
│ aydınlatma     62 lamba · 10,0 m aralık · tek sıra, tavandan         │
│ kaya yüzü      portalın üstünde 40,0 m                               │
│ ⛔ Sayısı olmayan satır bible'a YAZILMADI. NARROW LOT'ta "regular     │
│    structural bays" gibi sayısız tarif ② STRUCTURE IDENTITY'yi 2/10  │
│    yaptı; aynı filmde SAYILI çapa bloğu 10/10 aldı.                  │
└──────────────────────────────────────────────────────────────────────┘
```

⛔ **GEÇİCİ EKİPMAN DEĞİŞMEZ BLOĞA GİRMEZ** [DERS 1]: delici jumbo, kalıp,
kalıp arabası, havalandırma kanalı, konteyner, şantiye çiti ve beton pompası
`ACTIVITY` / `SITE TEXTURE` bloklarına yazıldı ve §5'in söküm satırında
takip ediliyor. Pasa bermisi geçici DEĞİLDİR — o BEDELDİR ve kalır.

---

# 4. 🪜 AŞAMA MERDİVENİ — 5 satır

| S | SÜRE | AŞAMA | EKRANDA VAR OLAN | YENİ OLAN | TEMSİL | MEVSİM TAŞIYICISI | KANIT NESNESİ | İSTASYON |
|:-:|---:|---|---|---|---|---|---|---|
| 0 | 6,0 | kırılmamış yüz · ilk şev kesiği | scree · alpin çim · eski geçit yolu | ilk şev kesiği açılır | 1 gün | yaz · koyu yeşil çim, kar çizgisi kadraj dışında | 12 m'lik ham açık yarık, alt yarığın tam altında | ANA |
| 1 | 6,0 | portal ağzı açılır (18 m) | + ağız · püskürtme beton · platform · pasa bermisi | tünelin AĞZI var olur | ~3 ay | sonbahar · pas kahvesi çim + boynuzda ilk kar | kemer tacı = kaya burnunun ALT yarığı (9,0 m) | ANA |
| 2 | 6,0 | KIŞ ① · başlık duvarı dökülür | + 12,5 m beton başlık duvarı · kanopi kalıbı | başlık duvarı + kanopi dökümü | ~3 ay | kış ① · kar çizgisi vadi tabanına İNER | duvar üstü, kemer tacının 3,5 m üstünde | ANA |
| 3 | 6,0 | KIŞ ② · delik geçilir · istinat duvarı | + kanopi · 14 panel duvar · kaplama halkası | istinat duvarı tamamlanır | ~3 ay | kış ② · kar çizgisi virajlara ÇEKİLİR + eriyik su | duvar harpuştası = taş köprü korkuluğu hizası | ANA |
| 4 | 6,0 | ⭐ teslim · tünel açık | + asfalt · bariyer · 62 lamba yanık | yol geçer, lambalar yanar | 1 gün | yaz · koyu yeşil çim (S0'ın ışığı) | kayaya doğru küçülen 62 lambalık dizi | ANA |

### Üç zorunlu satır

```
① KANIT NESNESİ  Her satırda bir NESNE var ve dördü de bir ÇAPAYA göre
                 ölçülüyor: alt yarık (9,0 m) · alt yarık + 3,5 m ·
                 taş köprü korkuluğu · lamba dizisi. "Tünel ilerledi"
                 kanıt değildir; tünelin İÇİ zaten görünmez.
                 ⭐ Bu filmin çözdüğü zorluk budur: bir tünelin ilerlemesi
                    kadrajda GÖRÜNMEZ. O yüzden ilerlemeyi taşıyan şey
                    tüp değil, PORTALIN ÖNÜNDE BÜYÜYEN YAPIDIR
                    (ağız → başlık duvarı → kanopi → istinat duvarı → yol)
                    ve VADİ TABANINDA BÜYÜYEN PASA BERMİSİDİR.

② LOOP SATIRI    S4'ün SON karesi = S0'ın İLK karesi.
                 S4 tam gün değil, şafaktan kuşluğa 2,5 saatlik bir yaydır
                 ve TAM S0'ın açılış ışığında biter: azimut 96° · yükseklik
                 30° · Temmuz · aynı yeşil yamaç. Değişen tek şey yapıdır.
                 ⛔ Bu yüzden S4'ün ışık yayı diğer dördünden farklıdır ve
                    bu bir tutarsızlık değil, LOOP'un bedelidir.

③ SÖKÜM SATIRI   kurulum ve söküm §5'te takvimli.
```

---

# 5. 🔧 SÖKÜM VE KURULUM TAKVİMİ

```
KURULAN
  şantiye çiti + konteyner      S0'da yok · S1'de var
  delici jumbo                  S1 (ağzın içinde)
  havalandırma kanalı           S1 · sarılı hâlde platformda
  beton pompası + duvar kalıbı  S2
  kaplama kalıp arabası         S3 (ağzın içinde, ray üstünde)

SÖKÜLEN — hepsi S4'ten ÖNCE, S4 karesinde HİÇBİRİ YOK
  delici jumbo · kalıp · kalıp arabası · havalandırma kanalı ·
  konteyner · şantiye çiti · beton pompası

⛔ SÖKÜLMEYEN — bu BEDELDİR, kalır [§1]
  pasa bermisi   S1'de doğar → S4'te düzeltilmiş kalıcı SEKİ olur
  şev yarası     S0'da açılır → hiçbir sahnede kapanmaz

ZEMİN DURUMU BİRİKİR (NARROW LOT'ta birikmedi — ⑤ WEAR 2/10):
  S0 kuru scree ve kaya tozu → S1 derin çamur ve pasa → S2 gri izli kar
  → S3 eriyik su ve sulusepken çamuru → S4 yeni asfalt + kenarda kurumuş
    açık renkli pasa kabuğu
```

---

# 6. ☀️ GÜNEŞ SAATİ

Her GÖRSEL prompt klibin **ilk karesinin** ışığını yazar; her I2V klibin
**başlangıç VE bitiş** açısını dereceyle yazar [DERS 18 — NARROW LOT'ta
açılar yalnız görselde kaldı ve ③ TIME RATE · SUN · CLOUD 0/10 geldi].

| S | Mevsim / an | Başlangıç azimut | Başlangıç yükseklik | Bitiş azimut | Bitiş yükseklik |
|:-:|---|---:|---:|---:|---:|
| 0 | yaz · Temmuz kuşluk | 96° | 30° | 262° | 26° |
| 1 | sonbahar · Ekim kuşluk | 136° | 24° | 224° | 18° |
| 2 | kış ① · Ocak geç kuşluk | 144° | 14° | 216° | 12° |
| 3 | kış ② · Mart kuşluk | 132° | 26° | 232° | 20° |
| 4 | yaz · Temmuz şafak → kuşluk | 72° | 12° | **96°** | **30°** |

```
⭐ S4'ün BİTİŞİ = S0'ın BAŞLANGICI. Loop buradan doğar.
⛔ Mevsim tek yönlü: yaz → sonbahar → kış① → kış② → yaz = 12 ay.
⛔ Kış yüksekliği ≤ 22° (S2: 14° · S3: 26° — S3 artık ilkbahar erimesidir).
⭐ MEVSİME GİRİŞ VE ÇIKIŞ, GİDEN KLİBİN İÇİNDE HAZIRLANIR [DERS 21]:
   S1'in son saniyesinde ilk kar istiflenmiş çelik profillerin üstüne düşer,
   zemin hâlâ ıslak ve koyudur.
   S3'ün son saniyesinde gri sulusepken bitmiş, platformdan ilk kuru toz
   kalkmıştır.
```

---

# 7. 🚫 NEGATİF ÇEKİRDEĞİN SAHA UYARLAMASI [DERS 16]

`KILAVUZ_REHBERI §7` çekirdeği şehir kulesi için yazılmıştır. Madde madde
dağ/tünel kartına karşı okundu; **değişenler ve gerekçeleri:**

```
① VİNÇ BLOĞU TAMAMEN ÇIKARILDI
   Sebep: dağ tünelinde kule vinci yoktur. Ve DERS 8 + DERS 22 aynı
   arızayı iki filmde ölçtü: halat gökyüzüne karşı kopuyor. Bu filmde
   kadrajda vinç YOK — arıza yüzeyi tasarımla kaldırıldı.
   ⛔ Metin yasağı yüzey listesinden de "crane" çıkarıldı, yerine
      "the drilling jumbo" değil, mevcut on yüzey bırakıldı (kapı en az
      sekiz yüzey arar; listede on tane var).

② "no floor slab without support beneath it" → "no rock overhang hanging
   without support"
   Sebep: burada çöken şey döşeme değil, portal ağzının üstündeki kayadır.

③ "the neighbouring buildings, the road, the trees" → beş çapa adıyla
   Sebep: çapa listesi filme özeldir; genel liste modelin çizmediği
   nesneleri kilitler.

④ SIRT HATTI EKLENDİ (SAHA §3.4): "the ridgeline silhouette is identical
   in every frame, the same peaks in the same places"

⑤ KAR EKİ yalnız S2 ve S3'te (SAHA §3.5): "the snow is grey, tracked,
   piled and partly melted — never clean, never uniform"

⑥ YILDIZ İZİ MADDESİ HİÇ KULLANILMADI
   Sebep: bu filmde GECE SAHNESİ YOK. CLOSING SPAN'de dağ vadisine
   şehir kuralı taşınmıştı ve ① C4 + ③ C1 birlikte 0/10 aldı.
```

---

# 8. 🏭 ÜRETİM SIRASI — ⭐ TERS İNŞA

```
1. ⭐ USTA KARE     S4 ÜRETİLİR (şafak · bitmiş portal · 62 lamba yanık).
                   ⛔ KAPI: kaya burnunun iki yarığı okunuyor mu, eski yolun
                      iki virajı görünüyor mu, taç %83'ün altında mı?
                      Hayırsa DİĞER DÖRT SAHNE ÜRETİLMEZ.

2. GERİYE İNŞA     Her sahne bir öncekinin KARESİNDEN türetilir:
                     S4 → asfaltı, bariyeri ve lambaları kaldır  → S3
                     S3 → istinat duvarını ve kanopiyi kaldır,
                          kar çizgisini virajlara koy             → S2
                     S2 → başlık duvarını kaldır, karı vadi
                          tabanına indir                          → S1
                     S1 → ağzı kapat, pasa bermisini küçült,
                          yaprakları pas kahvesine çevir          → S0
                   ⛔ S0'a inerken bermi TAMAMEN kalkar; şev yarası
                      12 m'ye iner ama SIFIRLANMAZ (S0'da zaten vardır).

3. ⛔ ZİNCİR KAPISI — HER KAREDEN SONRA [DERS 12]
                   bash araclar/zincir_kontrol.sh <onceki_onayli> <yeni>
                   Çıkış 2 = zincir kırıldı → kareyi AT, önceki onaylı
                   kareye dön. SONRAKİ SAHNELERİ ÜRETME.

4. VİDEO           Onaylanan her görselden I2V. T2V yalnız I2V tutmazsa.

5. KURGU           5 klip · sert kesme · geçiş efekti YOK · + kapak kartı
```

---

# 9. 🎬 SAHNELER

---

## 🎬 SAHNE 0 — DAĞIN YÜZÜ

_"Dağ kapalıydı ve yolun sonu bir kaya duvarıydı."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 0 of 5. Vertical time-lapse of a road tunnel portal in a narrow mountain valley.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a rock bench on the far side of the valley, lens 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One road tunnel driven into the south-east face of a rock ridge: one tube 620 metres long carrying two 3.65 metre lanes, excavated 12.4 metres wide and 9.0 metres high to the arch crown. The portal is one reinforced concrete headwall 21.0 metres wide and 12.5 metres high on a rock bench cut 4.0 metres back into the face, carrying a canopy slab 6.0 metres deep over the mouth. The approach is a 9.4 metre wide road platform on a 210 metre embankment held by a reinforced concrete retaining wall 5.2 metres high, 14 panels at 15.0 metre centres. Inside the tube one line of 62 lamp housings hangs from the crown at 10.0 metre centres. The rock face above the portal rises 40.0 metres above the road platform. AT THIS STAGE: nothing of the tunnel exists. The rock face is unbroken and the valley floor below it carries loose scree and coarse alpine grass. One tracked excavator at the foot of the face has just opened the first bench cut, a raw pale scar 12 metres wide and 2 metres deep in the scree, with a small spoil pile beside it. No portal, no headwall, no canopy, no retaining wall and no road platform exist anywhere.

SITE / BACKGROUND: A narrow mountain valley running from the lower left of the frame to the upper right. On frame right, standing clear of the face, one bare grey rock buttress with exactly two deep vertical clefts, the lower cleft mouth 9.0 metres and the upper cleft mouth 20.0 metres above the valley floor. Across the face above the portal runs the old pass road, a thin pale ledge with a low dry stone parapet, showing exactly two hairpin bends inside the frame, the lower 30.0 metres and the upper 37.0 metres above the valley floor. At the left edge of the platform lies one flat-topped granite boulder 2.4 metres across, too large to move. At the lower left a braided stream crosses the frame under a small single-arch stone bridge with one pier. Far behind the valley the ridge line carries a wide saddle notch with exactly one rock horn on its right side. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The first bench cut is the only progress proof. Its raw pale scar sits directly below the lower cleft of the rock buttress and is as wide as the stone bridge is long.

COMPOSITION: Vertical 9:16. The portal arch crown sits at about forty percent of frame height and the top of the rock face at about eighty-three percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: July, mid-morning. Sun azimuth 96 degrees, elevation 30 degrees, shadows long to the west. Neutral 5600K daylight, deep blue sky with sparse high cloud, the rock face fully lit, its clefts hard black lines. The snow line has retreated far above the frame and the alpine grass on the opposite slope is deep green.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: One tracked excavator works in the raw bench cut at the foot of the face and one tipper truck waits on the old gravel track below it. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere; vehicles render as smeared light and colour trails.

SITE TEXTURE: Dry rock dust hanging low over the cut, fresh pale spoil at its angle of repose, tyre ruts in the loose scree, one stack of pipe and untidy clutter.

PHYSICS: The excavator rests on its tracks on solid scree, its bucket physically connected to the hydraulic arm. The spoil lies at its natural angle of repose.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same valley, same rock, same background in every frame: the horizon, the clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, position, size or spacing, and the ridgeline silhouette is identical in every frame, the same peaks in the same places. The tunnel only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere — not on the hoarding, the safety signage, the machinery, the containers, the vests and helmets, the trucks, the scaffolding, the formwork or the portal facade, and nothing has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no rock overhang hanging without support, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no subtitles, no captions, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: rock dust, mud, tyre ruts, stacked material, offcuts, tarpaulins, puddles and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated summer day passes. The sun moves visibly across the sky during the shot: it starts at azimuth 96 degrees and elevation 30 degrees and ends at azimuth 262 degrees and elevation 26 degrees, so the shadow of the clefted buttress starts thrown long to the west across the scree and ends thrown long to the east, sweeping the whole valley floor from left to right, and the lit rock face falls into its own shadow in the last second. Thin high cloud streaks across the sky in long smooth trails, always from the north-west. At about one second and two tenths the excavator bucket takes its first full bite out of the face and the raw pale scar of the bench cut widens in one visible step; after that the machine settles into a slow repeating cycle and the spoil pile beside it grows. A tipper truck comes and goes on the old gravel track as a smeared colour trail.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the clefted rock buttress on frame right occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge with its saddle notch stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — A narrow mountain valley under a July morning sun; an unbroken grey rock face on the right of frame with a clefted buttress standing clear of it, two hairpin bends of an old pass road cut across the face above, a flat-topped boulder on the valley floor and a small stone arch bridge over a braided stream at the lower left.
At 1.2s — One tracked excavator takes its first full bite out of the foot of the face and a raw pale bench cut opens in the scree.
At 2.6s — Rock dust drifts low; a spoil pile grows beside the cut; a tipper truck comes and goes as a smeared trail.
At 4.0s — Shadows swing from west to east across the valley floor as the sun crosses; high cloud streaks from the north-west.
At 5.2s — The light warms and the rock face begins to fall into its own shadow.
By 6s — The valley is in shadow and the single pale scar of the first cut is the only mark on the mountain. Hard cut to Scene 1.

The camera never moves. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, size or position; the horizon stays at exactly half the frame height. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 1 — AĞIZ

_"Kaya bir kez delindikten sonra dağ artık kapalı değildir."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 1 of 5. Vertical time-lapse of a road tunnel portal in a narrow mountain valley.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a rock bench on the far side of the valley, lens 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One road tunnel driven into the south-east face of a rock ridge: one tube 620 metres long carrying two 3.65 metre lanes, excavated 12.4 metres wide and 9.0 metres high to the arch crown. The portal is one reinforced concrete headwall 21.0 metres wide and 12.5 metres high on a rock bench cut 4.0 metres back into the face, carrying a canopy slab 6.0 metres deep over the mouth. The approach is a 9.4 metre wide road platform on a 210 metre embankment held by a reinforced concrete retaining wall 5.2 metres high, 14 panels at 15.0 metre centres. Inside the tube one line of 62 lamp housings hangs from the crown at 10.0 metre centres. The rock face above the portal rises 40.0 metres above the road platform. AT THIS STAGE: the portal bench has been cut 4.0 metres back into the face and the mouth of the tube is open and driven 18 metres into the rock, a dark rectangle 12.4 metres wide and 9.0 metres high to its arch crown. The cut face around it is covered in grey sprayed concrete and rock bolt plates, and the 210 metre approach platform has been graded across the valley floor. No headwall, no canopy, no retaining wall and no lamp housings exist yet.

SITE / BACKGROUND: A narrow mountain valley running from the lower left of the frame to the upper right. On frame right, standing clear of the face, one bare grey rock buttress with exactly two deep vertical clefts, the lower cleft mouth 9.0 metres and the upper cleft mouth 20.0 metres above the valley floor. Across the face above the portal runs the old pass road, a thin pale ledge with a low dry stone parapet, showing exactly two hairpin bends inside the frame, the lower 30.0 metres and the upper 37.0 metres above the valley floor. At the left edge of the platform lies one flat-topped granite boulder 2.4 metres across, too large to move. At the lower left a braided stream crosses the frame under a small single-arch stone bridge with one pier. Far behind the valley the ridge line carries a wide saddle notch with exactly one rock horn on its right side. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The crown of the open portal arch now sits exactly level with the lower cleft of the rock buttress on frame right, 9.0 metres above the valley floor, where four months ago there was unbroken rock.

COMPOSITION: Vertical 9:16. The portal arch crown sits at about forty percent of frame height and the top of the rock face at about eighty-three percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: October, mid-morning. Sun azimuth 136 degrees, elevation 24 degrees, shadows long to the north-west. Warm-neutral 5000K daylight, broken low cloud, medium-hard shadows. The alpine grass on the opposite slope has turned rust-brown and the first snow of the season caps the rock horn on the far ridge.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: One drilling jumbo stands just inside the mouth, two tipper trucks work the graded platform, and a spoil bench of pale broken rock has been built out onto the valley floor. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere; vehicles render as smeared light and colour trails.

SITE TEXTURE: Deep mud and standing puddles across the platform, tyre ruts, pale muck tracked everywhere, stacked steel arches, tarpaulins, coiled ventilation duct and untidy clutter.

PHYSICS: The steel arches inside the mouth carry the rock above them and every one stands on the invert. The spoil bench lies at its natural angle of repose.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same valley, same rock, same background in every frame: the horizon, the clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, position, size or spacing, and the ridgeline silhouette is identical in every frame, the same peaks in the same places. The tunnel only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere — not on the hoarding, the safety signage, the machinery, the containers, the vests and helmets, the trucks, the scaffolding, the formwork or the portal facade, and nothing has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no rock overhang hanging without support, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no subtitles, no captions, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: rock dust, mud, tyre ruts, stacked material, offcuts, tarpaulins, puddles and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated autumn day passes. The sun moves visibly across the sky during the shot: it starts at azimuth 136 degrees and elevation 24 degrees and ends at azimuth 224 degrees and elevation 18 degrees, so the shadow of the clefted buttress sweeps across the muddy platform from left to right and lengthens, and the rock face falls into its own shadow in the last second. Broken low cloud streaks across the sky in long smooth trails, always from the north-west. Tipper trucks run in and out of the dark mouth as smeared colour trails and the pale spoil bench on the valley floor grows tip by tip. At about three seconds and six tenths one load is tipped over the edge of the spoil bench and the bench visibly steps outward in one movement. In the last second of the shot the first snow begins to settle on the stacked steel arches and along the top edge of the spoil bench, while the ground is still dark and wet.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the clefted rock buttress on frame right occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge with its saddle notch stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — An October morning; a dark open tunnel mouth in a grey rock face, its arch crown level with the lower cleft of the buttress on frame right, a graded muddy platform below it and a pale spoil bench built out onto the valley floor.
At 1.4s — A drilling jumbo works just inside the mouth; tipper trucks run in and out as smeared trails.
At 3.6s — One load is tipped over the edge of the spoil bench and the bench steps visibly outward.
At 4.6s — Shadows sweep left to right across the muddy platform and lengthen; low cloud streaks from the north-west.
By 6s — The first snow settles on the stacked steel arches while the ground is still dark and wet. Hard cut to Scene 2.

The camera never moves. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, size or position; the horizon stays at exactly half the frame height. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 2 — KIŞ ① — KAR VE KAYA

_"Dağ kışın karşılık verir: yılın en yavaş üç ayı."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 2 of 5. Vertical time-lapse of a road tunnel portal in a narrow mountain valley.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a rock bench on the far side of the valley, lens 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One road tunnel driven into the south-east face of a rock ridge: one tube 620 metres long carrying two 3.65 metre lanes, excavated 12.4 metres wide and 9.0 metres high to the arch crown. The portal is one reinforced concrete headwall 21.0 metres wide and 12.5 metres high on a rock bench cut 4.0 metres back into the face, carrying a canopy slab 6.0 metres deep over the mouth. The approach is a 9.4 metre wide road platform on a 210 metre embankment held by a reinforced concrete retaining wall 5.2 metres high, 14 panels at 15.0 metre centres. Inside the tube one line of 62 lamp housings hangs from the crown at 10.0 metre centres. The rock face above the portal rises 40.0 metres above the road platform. AT THIS STAGE: the tube has been driven 300 metres into the rock and the reinforced concrete headwall has been cast to its full height of 12.5 metres above the mouth, with the formwork for the canopy slab standing on it. The mouth, the sprayed concrete cut face and the graded platform are all still there. No retaining wall, no road surface and no lamp housings exist yet.

SITE / BACKGROUND: A narrow mountain valley running from the lower left of the frame to the upper right. On frame right, standing clear of the face, one bare grey rock buttress with exactly two deep vertical clefts, the lower cleft mouth 9.0 metres and the upper cleft mouth 20.0 metres above the valley floor. Across the face above the portal runs the old pass road, a thin pale ledge with a low dry stone parapet, showing exactly two hairpin bends inside the frame, the lower 30.0 metres and the upper 37.0 metres above the valley floor. At the left edge of the platform lies one flat-topped granite boulder 2.4 metres across, too large to move. At the lower left a braided stream crosses the frame under a small single-arch stone bridge with one pier. Far behind the valley the ridge line carries a wide saddle notch with exactly one rock horn on its right side. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The top edge of the new concrete headwall stands 3.5 metres above the crown of the portal arch, about a third of the way from the lower cleft of the buttress to the upper cleft.

COMPOSITION: Vertical 9:16. The portal arch crown sits at about forty percent of frame height and the top of the rock face at about eighty-three percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: January, late morning. Sun azimuth 144 degrees, elevation 14 degrees, shadows very long and blue to the north-west. Cold 6500K light under a flat white-grey sky, low contrast. The snow line has come down to the valley floor: snow lies on both hairpin bends of the old pass road, on the ledges of the clefted buttress and on the flat top of the granite boulder.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: One concrete pump stands against the headwall formwork and one tipper truck waits on the plowed track, its edges banked with grey ploughed snow. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere; vehicles render as smeared light and colour trails.

SITE TEXTURE: Grey tracked snow piled at the edges and partly melted, black mud under it, frozen tyre ruts, icicles along the sprayed concrete and tarpaulins weighed down with snow.

PHYSICS: The headwall formwork is propped against the rock bench and bears the weight of the fresh concrete. The pump boom is one continuous rigid arm resting on its outriggers.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same valley, same rock, same background in every frame: the horizon, the clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, position, size or spacing, and the ridgeline silhouette is identical in every frame, the same peaks in the same places. The tunnel only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere — not on the hoarding, the safety signage, the machinery, the containers, the vests and helmets, the trucks, the scaffolding, the formwork or the portal facade, and nothing has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no rock overhang hanging without support, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no subtitles, no captions, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: rock dust, mud, tyre ruts, stacked material, offcuts, tarpaulins, puddles and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain. The snow on the site is grey, tracked, piled and partly melted — never clean, never uniform.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated winter day passes, short and cold. The sun moves visibly across the sky during the shot: it starts at azimuth 144 degrees and elevation 14 degrees and ends at azimuth 216 degrees and elevation 12 degrees, so the very long blue shadow of the clefted buttress sweeps across the snow from left to right, and the valley falls into shadow early, in the last second and a half. Flat grey cloud streaks across the sky in long smooth trails, always from the north-west. Work is visibly slow: the concrete pump stands still for most of the shot and only one truck comes and goes. At about four seconds and eight tenths one pour runs into the canopy formwork on top of the headwall and the fresh grey concrete fills it in one visible step. Snow gathers grey and tracked at the edges through the whole shot.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the clefted rock buttress on frame right occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge with its saddle notch stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — A January morning under a flat white sky; snow down to the valley floor, on both hairpin bends of the old pass road and on the flat-topped boulder; a new concrete headwall stands across the rock face above the dark tunnel mouth.
At 1.6s — Very long blue shadows lie across the snow; almost nothing moves; one truck waits on the plowed track.
At 3.2s — Grey cloud streaks from the north-west; snow gathers tracked and grey at the edges of the platform.
At 4.8s — One pour runs into the canopy formwork on top of the headwall and fills it in one visible step.
By 6s — The valley falls into shadow early and the site goes quiet. Hard cut to Scene 3.

The camera never moves. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, size or position; the horizon stays at exactly half the frame height. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 3 — KIŞ ② — ERİME

_"Kar çekilince dağın içinden geçen delik göründü."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 3 of 5. Vertical time-lapse of a road tunnel portal in a narrow mountain valley.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a rock bench on the far side of the valley, lens 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One road tunnel driven into the south-east face of a rock ridge: one tube 620 metres long carrying two 3.65 metre lanes, excavated 12.4 metres wide and 9.0 metres high to the arch crown. The portal is one reinforced concrete headwall 21.0 metres wide and 12.5 metres high on a rock bench cut 4.0 metres back into the face, carrying a canopy slab 6.0 metres deep over the mouth. The approach is a 9.4 metre wide road platform on a 210 metre embankment held by a reinforced concrete retaining wall 5.2 metres high, 14 panels at 15.0 metre centres. Inside the tube one line of 62 lamp housings hangs from the crown at 10.0 metre centres. The rock face above the portal rises 40.0 metres above the road platform. AT THIS STAGE: the tube has been holed through over its full 620 metre length and the cast concrete lining is being placed inside it, a pale ring visible 20 metres in. The canopy slab has been struck and stands over the mouth, and the retaining wall on the valley side is complete: 14 panels at 15.0 metre centres, 5.2 metres high. No road surface, no barriers and no lamp housings exist yet.

SITE / BACKGROUND: A narrow mountain valley running from the lower left of the frame to the upper right. On frame right, standing clear of the face, one bare grey rock buttress with exactly two deep vertical clefts, the lower cleft mouth 9.0 metres and the upper cleft mouth 20.0 metres above the valley floor. Across the face above the portal runs the old pass road, a thin pale ledge with a low dry stone parapet, showing exactly two hairpin bends inside the frame, the lower 30.0 metres and the upper 37.0 metres above the valley floor. At the left edge of the platform lies one flat-topped granite boulder 2.4 metres across, too large to move. At the lower left a braided stream crosses the frame under a small single-arch stone bridge with one pier. Far behind the valley the ridge line carries a wide saddle notch with exactly one rock horn on its right side. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The coping of the finished retaining wall now runs unbroken from the portal to the left edge of the frame and sits exactly level with the parapet of the old stone bridge on the valley floor.

COMPOSITION: Vertical 9:16. The portal arch crown sits at about forty percent of frame height and the top of the rock face at about eighty-three percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: March, mid-morning. Sun azimuth 132 degrees, elevation 26 degrees, shadows long to the north-west. Changeable 5400K light with fast broken cloud. The snow line has retreated back up the slope to the two hairpin bends of the old pass road; below it the ground is bare, dark and running with meltwater.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: One mixer truck stands at the mouth feeding the lining formwork carriage inside the tube and one excavator trims the shoulder behind the new retaining wall. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere; vehicles render as smeared light and colour trails.

SITE TEXTURE: Grey slush along the edges, meltwater in every tyre rut and dripping off the canopy slab, deep black mud, standing puddles and stripped formwork panels stacked against the wall.

PHYSICS: The canopy slab bears on the headwall and on the rock bench behind it. The lining formwork carriage stands on rails on the tunnel invert. Meltwater runs downhill into the stream.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same valley, same rock, same background in every frame: the horizon, the clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, position, size or spacing, and the ridgeline silhouette is identical in every frame, the same peaks in the same places. The tunnel only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere — not on the hoarding, the safety signage, the machinery, the containers, the vests and helmets, the trucks, the scaffolding, the formwork or the portal facade, and nothing has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no rock overhang hanging without support, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no subtitles, no captions, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: rock dust, mud, tyre ruts, stacked material, offcuts, tarpaulins, puddles and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain. The snow on the site is grey, tracked, piled and partly melted — never clean, never uniform.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated spring day passes. The sun moves visibly across the sky during the shot: it starts at azimuth 132 degrees and elevation 26 degrees and ends at azimuth 232 degrees and elevation 20 degrees, so the shadow of the clefted buttress sweeps across the wet platform from left to right and shortens, and the rock face falls into shadow in the last second. Fast broken cloud streaks across the sky in long smooth trails, always from the north-west. At about two seconds and four tenths one bay of the road embankment behind the retaining wall is filled and levelled in one visible step, and after that the work runs on quickly: mixer trucks come and go as smeared colour trails and meltwater runs off the canopy slab in a steady line of drips. In the last second of the shot the grey slush at the edges has gone and the first dry dust lifts off the platform.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the clefted rock buttress on frame right occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge with its saddle notch stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — A March morning; the snow line has retreated up to the two hairpin bends of the old pass road, meltwater runs everywhere, a finished canopy slab stands over the tunnel mouth and a new retaining wall runs to the left edge of frame.
At 1.2s — Meltwater drips off the canopy slab in a steady line; grey slush lies along the edges.
At 2.4s — One bay of road embankment behind the retaining wall is filled and levelled in one visible step.
At 4.0s — Mixer trucks come and go as smeared trails; a pale concrete lining ring is visible inside the mouth.
By 6s — The slush is gone, the first dry dust lifts off the platform and the rock face falls into shadow. Hard cut to Scene 4.

The camera never moves. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, size or position; the horizon stays at exactly half the frame height. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 4 — ⭐ USTA KARE — KAPI AÇIK

_"Dağ açıldı. Üstündeki eski yol bir daha kullanılmadı."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 4 of 5. Vertical time-lapse of a road tunnel portal in a narrow mountain valley.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a rock bench on the far side of the valley, lens 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One road tunnel driven into the south-east face of a rock ridge: one tube 620 metres long carrying two 3.65 metre lanes, excavated 12.4 metres wide and 9.0 metres high to the arch crown. The portal is one reinforced concrete headwall 21.0 metres wide and 12.5 metres high on a rock bench cut 4.0 metres back into the face, carrying a canopy slab 6.0 metres deep over the mouth. The approach is a 9.4 metre wide road platform on a 210 metre embankment held by a reinforced concrete retaining wall 5.2 metres high, 14 panels at 15.0 metre centres. Inside the tube one line of 62 lamp housings hangs from the crown at 10.0 metre centres. The rock face above the portal rises 40.0 metres above the road platform. AT THIS STAGE: the tunnel is complete and open. The headwall and the canopy slab stand finished over the mouth, the road platform is surfaced and runs unbroken from the lower left of the frame into the tube, the 14 retaining wall panels carry a continuous safety barrier, and the line of 62 lamp housings inside the tube is lit and recedes into the rock as a shrinking string of warm points. Every temporary thing has gone: no drilling jumbo, no formwork, no ventilation duct, no hoarding. The pale spoil bench on the valley floor has been graded into a permanent terrace and stays.

SITE / BACKGROUND: A narrow mountain valley running from the lower left of the frame to the upper right. On frame right, standing clear of the face, one bare grey rock buttress with exactly two deep vertical clefts, the lower cleft mouth 9.0 metres and the upper cleft mouth 20.0 metres above the valley floor. Across the face above the portal runs the old pass road, a thin pale ledge with a low dry stone parapet, showing exactly two hairpin bends inside the frame, the lower 30.0 metres and the upper 37.0 metres above the valley floor. At the left edge of the platform lies one flat-topped granite boulder 2.4 metres across, too large to move. At the lower left a braided stream crosses the frame under a small single-arch stone bridge with one pier. Far behind the valley the ridge line carries a wide saddle notch with exactly one rock horn on its right side. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The surfaced road runs unbroken into the lit tube and the string of 62 lamps recedes into the rock; on the face above, both hairpin bends of the old pass road are empty and a bar of pale gravel closes the foot of the lower bend.

COMPOSITION: Vertical 9:16. The portal arch crown sits at about forty percent of frame height and the top of the rock face at about eighty-three percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: July one year later, first light. Sun azimuth 72 degrees, elevation 12 degrees, shadows very long to the west, the valley floor still in the shadow of the opposite slope. Cool 5200K light, clear pale sky, only the top of the rock face catching the sun. The snow line has retreated far above the frame again and the alpine grass is deep green.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: No machines and no site vehicles remain; a few road vehicles enter and leave the lit tube. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere; vehicles render as smeared light and colour trails.

SITE TEXTURE: New dark asphalt clean at the centre and dusted at the edges, dried pale spoil crusted along the foot of the retaining wall and gravel shoulders.

PHYSICS: The canopy slab bears on the headwall and on the rock bench. Every lamp housing hangs from the tunnel crown on its own bracket.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same valley, same rock, same background in every frame: the horizon, the clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, position, size or spacing, and the ridgeline silhouette is identical in every frame, the same peaks in the same places. The tunnel only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere — not on the hoarding, the safety signage, the machinery, the containers, the vests and helmets, the trucks, the scaffolding, the formwork or the portal facade, and nothing has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no rock overhang hanging without support, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no subtitles, no captions, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: rock dust, mud, tyre ruts, stacked material, offcuts, tarpaulins, puddles and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

Two and a half accelerated hours pass, from first light to mid-morning. The sun moves visibly across the sky during the shot: it starts at azimuth 72 degrees and elevation 12 degrees and ends at azimuth 96 degrees and elevation 30 degrees, so the shadow line of the opposite slope retreats down the rock face from the top towards the valley floor and the long western shadows shorten. Thin high cloud streaks across the sky in long smooth trails, always from the north-west. The 62 lamps inside the tube burn steadily throughout and read as a shrinking string of warm points receding into the rock. A few road vehicles enter and leave the mouth as smeared light trails; both hairpin bends of the old pass road above stay completely empty for the whole shot. At about five seconds the retreating shadow line reaches the portal and the sun lands on the headwall and on the new road surface for the first time, and the shot ends in exactly the light of the first frame of the film.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the clefted rock buttress on frame right occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge with its saddle notch stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — A July morning one year later at first light; the valley floor still in shadow, the top of the rock face just catching the sun, and a finished tunnel portal with a lit string of lamps receding into the rock.
At 1.4s — A few road vehicles enter and leave the lit mouth as smeared light trails; the old pass road above is empty.
At 2.8s — The shadow line of the opposite slope retreats down the rock face; high cloud streaks from the north-west.
At 5.0s — The sun reaches the portal and lands on the headwall and on the new road surface for the first time.
By 6s — The valley is in full morning light, the pale spoil terrace below the portal is permanent and the old road above carries nothing. Hard cut back to Scene 0.

The camera never moves. The clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, size or position; the horizon stays at exactly half the frame height. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

# 10. 🎶 MÜZİK — tek parça, 35,0 saniye

### 🎶 IZGARA VE KATMANLAR

```
BPM = 240 × (sahne başına ölçü) ÷ 6,0  →  120 BPM = 3 ölçü/sahne
sahne bloğu 15 ölçü (30,0 sn) · kapak kartı 2,5 ölçü (5,0 sn)
⛔ Izgara dışı tempo beş kesmenin beşini birden hizasız bırakır.
KATMAN = AŞAMA: 5 sahne, 5 katman, her sahnede bir tane eklenir, hiçbiri
çıkmaz. ⭐ Kış katmanı S2'de gelir ve bir daha gitmez.
```

### 🎶 MÜZİK PROMPTU

```
Instrumental score for a 35-second vertical construction time-lapse: a
30-second scene block of five 6-second shots, followed by a 5-second end card.
No lyrics, no voice, no melody line, no traditional song structure.

Genre: cold minimal orchestral-industrial, documentary, no drums kit.
Tempo: 120 BPM, strict and bar-aligned, three bars per 6-second shot.

Layers (one added every shot, none removed until the final bars):
1. S0  dry pulse on the first beat of each bar, close and small
2. S1  one low sustained bass note, motionless, no movement
3. S2  bowed string friction and a slow metallic scrape — the winter layer
4. S3  dripping water treated as rhythm, high and irregular against the pulse
5. S4  one wide warm chord pad opening underneath everything

Dynamic map across 35 seconds:
  0.0-1.5    silence — only the site's own ambience: wind in a rock valley,
             one distant machine, water over stones
  1.5-6.0    layer 1 alone
  6.0-12.0   layer 2 enters
  12.0-18.0  layer 3 enters — the coldest and widest moment
  18.0-24.0  layer 4 enters, the pulse quickens against it
  24.0-30.0  layer 5 enters, the stack sits together and opens
  30.0-35.0  end card: everything resolves and decays; the last 1.5 seconds
             carry only ambience

Reference feel: the restraint of Jóhann Jóhannsson and the granular texture
of Hildur Guðnadóttir — do not quote either, write new material.

Phone-speaker rule: Every sub-bass element below 150 Hz is doubled by its own
upper harmonics at roughly 100, 150 and 200 Hz so the fundamental is implied
rather than required; the low end is never the only carrier of the weight.
```

### ⛔ MÜZİKSİZ PENCERE

```
⛔ MÜZİKSİZ PENCERE 0,0-1,5 sn. Kanca diegetik sesle açılır: dağ rüzgârı +
   tek ekskavatör. Uzun enstrümantal intro elenir.
```

---

# 11. 🖼️ KAPAK KARTI

### 🖼️ KART ÖLÇÜLERİ

```
KAYNAK AN     S4 · 0:24,0 (klibin İLK karesi — usta kare)
              ⛔ Kapak SIFIRDAN üretilmez. NARROW LOT'ta kart hiç
                 üretilmedi ve ④ COVER AND CONTENT 0/10 aldı.
BAŞLIK        "THE MOUNTAIN DOOR"  (İngilizce · 3 kelime)
PUNTO         büyük harf yüksekliği ≥ %8 kare yüksekliği (≥154 px)
KONUM         y = 640-1180 bandı · sol 122 px ve sağ 242 px'e GİRMEZ
              ⭐ Bu bant şafak karesinde gölgedeki kaya yüzüdür: düz,
                 koyu ve düşük kontrastlı — başlık için hazır zemin.
KONTRAST      ≥ 4,5:1 · gerekirse metnin arkasına düz koyu bant (gradyan YOK)
ANİMASYON     yok · kart 5,0 sn hareketsiz
```

### 🖼️ KAPAK GÖRSEL PROMPTU

```
Photorealistic documentary construction photograph — Scene 4 of 5. Vertical time-lapse of a road tunnel portal in a narrow mountain valley.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a rock bench on the far side of the valley, lens 16.0 metres above the new road platform level, 48 metres from the rock face at the portal, bearing 315 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One road tunnel driven into the south-east face of a rock ridge: one tube 620 metres long carrying two 3.65 metre lanes, excavated 12.4 metres wide and 9.0 metres high to the arch crown. The portal is one reinforced concrete headwall 21.0 metres wide and 12.5 metres high on a rock bench cut 4.0 metres back into the face, carrying a canopy slab 6.0 metres deep over the mouth. The approach is a 9.4 metre wide road platform on a 210 metre embankment held by a reinforced concrete retaining wall 5.2 metres high, 14 panels at 15.0 metre centres. Inside the tube one line of 62 lamp housings hangs from the crown at 10.0 metre centres. The rock face above the portal rises 40.0 metres above the road platform. AT THIS STAGE: the tunnel is complete and open. The headwall and the canopy slab stand finished over the mouth, the road platform is surfaced and runs unbroken from the lower left of the frame into the tube, the 14 retaining wall panels carry a continuous safety barrier, and the line of 62 lamp housings inside the tube is lit and recedes into the rock as a shrinking string of warm points. Every temporary thing has gone: no drilling jumbo, no formwork, no ventilation duct, no hoarding. The pale spoil bench on the valley floor has been graded into a permanent terrace and stays.

SITE / BACKGROUND: A narrow mountain valley running from the lower left of the frame to the upper right. On frame right, standing clear of the face, one bare grey rock buttress with exactly two deep vertical clefts, the lower cleft mouth 9.0 metres and the upper cleft mouth 20.0 metres above the valley floor. Across the face above the portal runs the old pass road, a thin pale ledge with a low dry stone parapet, showing exactly two hairpin bends inside the frame, the lower 30.0 metres and the upper 37.0 metres above the valley floor. At the left edge of the platform lies one flat-topped granite boulder 2.4 metres across, too large to move. At the lower left a braided stream crosses the frame under a small single-arch stone bridge with one pier. Far behind the valley the ridge line carries a wide saddle notch with exactly one rock horn on its right side. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The surfaced road runs unbroken into the lit tube and the string of 62 lamps recedes into the rock; on the face above, both hairpin bends of the old pass road are empty and a bar of pale gravel closes the foot of the lower bend.

COMPOSITION: Vertical 9:16. The portal arch crown sits at about forty percent of frame height and the top of the rock face at about eighty-three percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: July one year later, first light. Sun azimuth 72 degrees, elevation 12 degrees, shadows very long to the west, the valley floor still in the shadow of the opposite slope. Cool 5200K light, clear pale sky, only the top of the rock face catching the sun. The snow line has retreated far above the frame again and the alpine grass is deep green.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: No machines and no site vehicles remain; a few road vehicles enter and leave the lit tube. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere; vehicles render as smeared light and colour trails.

SITE TEXTURE: New dark asphalt clean at the centre and dusted at the edges, dried pale spoil crusted along the foot of the retaining wall and gravel shoulders.

PHYSICS: The canopy slab bears on the headwall and on the rock bench. Every lamp housing hangs from the tunnel crown on its own bracket.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same valley, same rock, same background in every frame: the horizon, the clefted buttress, the two hairpin bends of the old pass road, the flat-topped boulder, the stone bridge and the far ridge never change shape, position, size or spacing, and the ridgeline silhouette is identical in every frame, the same peaks in the same places. The tunnel only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere — not on the hoarding, the safety signage, the machinery, the containers, the vests and helmets, the trucks, the scaffolding, the formwork or the portal facade, and nothing has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no rock overhang hanging without support, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no subtitles, no captions, no end card, no watermark. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: rock dust, mud, tyre ruts, stacked material, offcuts, tarpaulins, puddles and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Leave the upper middle third of the frame visually simple and low-contrast so that a title can be set over it: no structural detail, no strong edge and no bright object between roughly forty and seventy percent of frame height on the left two thirds of the picture.
Output: 9:16, 4K, no text, no watermark.
```

### ⭐ 120 PX POSTA PULU TESTİ

```
⛔ Prompt hâlâ "no text" der. Başlık modele YAZDIRILMAZ, post-prodüksiyonda
   dizilir — model yazdığı yazıyı bozar.

⭐ 120 PX POSTA PULU TESTİ — İKİ görüntüye birden:
     sips -Z 120 kapak.png --out kapak_120.png
     sips -Z 120 s0_kare0.png --out s0_120.png
   ⓐ SİLUET: gökyüzüne karşı koyu kaya kütlesi + sağında kaya burnu
   ⓑ BAŞLIK: üç kelimenin şekli hâlâ ayırt ediliyor mu
   ⛔ ⓐ kayboluyorsa kapak yeniden ÇERÇEVELENMEZ, S4 YENİDEN ÜRETİLİR.
```

---

# 12. 📣 PAKETLEME (İNGİLİZCE)

### 📣 PAKET METNİ

```
TITLES
1. They cut a door into the mountain      (33)
2. One year to open 620 metres            (27)
3. The old pass road went quiet           (28)

DESCRIPTION
The valley had one way out, and it closed every winter.
Over twelve months a 620-metre road tunnel is driven into the rock face:
the portal bench is cut, the mouth is opened, a 12.5-metre concrete headwall
is cast through the snow, and the string of 62 lamps is finally lit. The
mountain keeps the scar, and the old pass road above the portal keeps nothing.
Single locked-off camera, 48 metres from the face, for one year.

#timelapse #construction #engineering #tunnel #civilengineering
#roadconstruction #mountainroad #shotcrete #tunnelportal #rockcut
#infrastructure #satisfying

This video was generated with AI. It does not document a real project.

PINNED COMMENT
A rock tunnel is not dug in one pass. The face is drilled, charged and blasted
in rounds of a few metres, then the fresh rock is sealed with sprayed concrete
and held with rock bolts before anyone works under it again — which is why the
portal headwall and the canopy slab come long after the mouth is open: they
exist to stop what falls off the face above from landing on the road. The
spoil has to go somewhere, and on a valley site it usually goes into the
valley. That pale terrace under the portal is not construction leftovers being
tidied away; it is permanent.
```

```
⛔ GERÇEKLİK BEYANI: gerçek firma / proje / şehir iddiası YOK.
⛔ YÜKLEMEDE "ALTERED CONTENT" ÜÇ PLATFORMDA DA ELLE İŞARETLENİR —
   açıklamadaki cümle onun yerine geçmez [apexait/youtube/POLITIKA_VE_RISK §2].
```

---

# 13. 🔒 MASTER LOCK

### 🔒 MASTER LOCK METNİ

```
Photorealistic documentary construction photography. Locked-off tripod, one
continuous time-lapse shot, no camera movement of any kind. Physically accurate
daylight. Real weather, real dirt, real clutter. Natural motion blur on moving
people and vehicles. No architectural render look, no CGI aesthetic, no game
engine look, no miniature look, no tilt-shift. Every frame should look like a
real photograph taken from a camera that has been standing in the same place
for a year.
```

---

# 14. ⛔ BU PLANIN BİLİNEN AÇIKLARI

### ⛔ AÇIKLAR

```
· KLİP SÜRESİ ÖLÇÜLMEDİ [D-d]. 6,0 bir hedeftir, ölçüm değil.
· DÜZ IZGARA bilerek seçildi ve ⑥ METRONOM riski açıktır [§2].
· TÜNELİN İÇİ GÖRÜNMEZ. İlerlemeyi portal önündeki yapı ve pasa bermisi
  taşıyor; bu bir tasarım kararıdır ve ② merceğinde sınanmamıştır.
· S4'ün ışık yayı diğer dördünden farklıdır (2,5 saat · şafak → kuşluk).
  Loop'un bedelidir ve ③ merceğinde "tutarsız zaman" olarak okunabilir.
· TERS İNŞA bu depoda hâlâ hiç koşulmadı — en yüksek kaldıraçlı ve en az
  sınanmış adım.
```

---

**QA kilit listesi ve FİNAL KARE KANITI:** `THE_MOUNTAIN_DOOR_QA_SPEC.md`
