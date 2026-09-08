# 🌕 THE LONG DAY — Uzun Gün

> # ⛔ BU DOSYA **v0**'DIR — ÜRETİLDİ, SEKİZ MERCEKLE ÖLÇÜLDÜ, DÜŞTÜ.
>
> `① 6,4Ⓥ karesiz` · `② belgesiz` · `③ 7,0` · `④ belgesiz` · `⑤ 5,8Ⓥ karesiz` ·
> `⑥ belgesiz` · `⑦ 4,4Ⓥ karesiz` · `⑧ belgesiz` — kayıt: `QA/RAPORLAR/THE_LONG_DAY.md`
>
> ⭐ GEÇEN: `① TIME-LAPSE` (kamera·kadraj·çapa·istasyon 10/10) · `⑤ SAME WORLD` +
> kanıt nesnesi BULUNDU (kaya + krater) · `④ ONE THING` ilk kez bulundu · `⑥ TIME`
> ⛔ DÜŞEN: `② DIFFERENT · APPEARING` · `③ NOT IN ONE DIRECTION` · `⑥ METRONOM` ·
> `⑦ PARKED` · `⑧ APPEARED 1/9` · beş mercekte END CARD DIFFERENT
>
> ⛔ EKRANDAKİ FİLM BU PLANIN FİLMİ DEĞİL: astronot, kadrajda güneş, dikey habitat,
> ikiz kule, düz 10 × 6,0 kurgu, afiş kapak. Üretim günlüğü yok — sebebi kayıtta
> değil [DERS 28]. Bu filmden çıkan dersler: **28 · 29 · 30 · 31 · 32 · 33 · 34**
> ⛔ Yeniden ÜRETİLMEZ; yeni film bu derslerle yazılır.
> Uzay saha kartı hâlâ YOK (§7 bu planın uyarlaması; ölçüldü, karta inmedi).

---

Dikey Timelapse Production Document · **v0 · ÜRETİLDİ, ÖLÇÜLDÜ, DÜŞTÜ**
Format: **9:16 (DİKEY)** | Sahne: **10 × 6,0 sn üretim hedefi** · kurgu süreleri §2 | Kapak kartı: **5,0 sn** | Toplam: **65,0 sn**
Prompt yapısı: 10 görsel + 10 I2V (birincil) + 10 T2V (yedek) = 30 prompt
Yapı: yüzey üssü — iki gömülü habitat modülü + üç direk (yeni tip · `YAPI_TIPI_KARTLARI §10` şablonu, §3'te sayıyla)
Saha: 🌕 Ay yüzeyi · mare ovası · 20° kuzey enlemi (kart YOK — §7 bu planın uyarlaması)
Zaman yayı: **19 Ay günü ≈ 19 ay** (her sahne bir Ay günü · aralar §4'te) → 60,0 saniye
Izgara kararı: `KILAVUZ_REHBERI §2.2` · ⭐ varyanslı ızgara, gerekçesi §2'de

_"Ova üç milyar yıldır dokunulmamıştı. On dokuz uzun gün sonra üstünde bir üs vardı —
ve ilk sabah açılan tekerlek izi hâlâ oradaydı, çünkü burada hiçbir şey silinmez."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     10 sahne = 60,0 sn   (6,0 · 4,0 · 6,0 · 4,0 · 6,0 · 6,0 · 8,0 · 4,0 · 6,0 · 10,0)
                                      ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn = 5,0 sn   ← SAHNE DEĞİL, ayrı denetlenir
                ⛔ KONUM: teslimin SON 5 saniyesi (0:60,0 – 1:05,0) [A1-b]
──────────────────────────────────────────────
TOPLAM                             65,0 sn
```

⛔ **KAPAK KARTI BİR SAHNE DEĞİLDİR** [DERS 4]. Kart S9'un usta karesinden
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
VAAT     Boş bir Ay ovasına, insan gelmeden önce robotlarla, iki gömülü
         modül ve üç direkten oluşan bir yüzey üssü kurulacak. Video
         başlamadan önce de var olan iş: ilk kargo iniş aracı yere inmiş,
         rampası inmiş, ilk rover rampanın tepesinde bekliyor.
DİRENÇ   ⭐ REGOLİT + UZUN GÜN. Kalkan olacak toprak yerinden kürekle
         taşınır: 12 m'lik bir silindirin üstüne 2,5 m örtü ≈ 900 ton
         regolit, tek bir paletli araçla, yük yük. Ve her 14 günlük
         gündüzün ardından 14 günlük −170 °C gece gelir; iş durur.
         Sahneler bu yüzden Ay GÜNLERİDİR — her sahne bir gündüz, aradaki
         geceler kesmenin içinde geçer.
BEDEL    ⭐ İKİ TANE, İKİSİ DE EKRANDA KALICI:
         ① DOKUNULMAMIŞ OVA. Ay'da rüzgâr yok: açılan hiçbir iz silinmez.
            S0'da tek çift tekerlek izi, S9'da ova baştan başa iz yumağı —
            ve ilk çift hâlâ altta. Üç milyar yıllık yüzey bir daha
            eski hâline dönmez.
         ② İLK İNİŞ ARACI. S0'da bembeyaz, S9'da tepesine kadar toz grisi.
            Kadrajda AYNEN durur, hiç dokunulmaz; üssü getiren araç orada
            grileşerek kalır.
```

**Üç kabul testi:**

```
① TEK KARE TESTİ       ✅ Düz tepeli regolit tümseği + önünde yuvarlak kapaklı
                          uç + direkler tek karede "Ay üssü" der; tümseğin
                          silindiri ne kadar örttüğü aşamayı verir.
② KİNETİK BAĞIMSIZLIK  ✅ Sabit planın içinde kaya gölgesinin saat ibresi gibi
                          soldan sağa süpürmesi, güneşi izleyen panellerin
                          dönmesi ve bir yük regolitin tümseğe boşalması
                          metinsiz okunur.
③ BAŞLIK ŞEMASI        ✅ "THE LONG DAY" — 3 kelime, kapak kartına sığar.
                          Filmin saati Ay günüdür; başlık saati adlandırır.
```

**Kanal tez kapısı** (`apexait/KANAL_KIMLIGI.md §2.1`): kaybolan şey
dokunulmamış yüzey · kadrajda görülüyor (iz yumağı + grileşen araç) ·
cevap "zaman geçiyor" değil ✅.

---

# 2. ⭐ IZGARA KARARI — 6,0 üretim · varyanslı kurgu

Proje sahibinin isteği **10 sahne × 6 saniye.** Bu, deponun varsayılan
üretim ızgarasıdır (`KILAVUZ_REHBERI §2.1`) ve her klip **6,0 sn hedefiyle**
üretilir. Ama KURGU süresi eşit olamaz: düz ızgara üç filmde üç kez
`⑥ METRONOM` aldı [DERS 13 · 24] ve `prompt_kontrol.py` on satırlık
tabloda süre eşitliğini **BLOCK** eder. Bu yüzden:

```
ÜRETİM     her klip aracın 6,0 sn ayarıyla (S6 ve S9 için 10 sn ayarı)
KURGU      120 BPM · ölçü 2,0 sn · izinli süreler 4 · 6 · 8 · 10

  S0   S1   S2   S3   S4   S5   S6   S7   S8   S9
  6,0  4,0  6,0  4,0  6,0  6,0  8,0  4,0  6,0  10,0   = 60,0 sn
   3    2    3    2    3    3    4    2    3    5     ← ölçü sayısı

KISA   S1 · S3 · S7  (düşük yeni bilgi: düzleme, yığın, direk) [A2-c]
UZUN   S6 (8,0 · gömme — filmin direnç sahnesi, kışın karşılığı)
       S9 (10,0 · doruk — gece biter, LOOP burada kapanır)
KONTRAST  S5 6,0 → S6 8,0 → S7 4,0 → … → S8 6,0 → S9 10,0
KESME ANLARI  0 · 6 · 10 · 16 · 20 · 26 · 32 · 40 · 44 · 50 · 60 · (kart) 65
              hepsi 2,0 sn ölçünün 1. VURUŞUNDA [A2-e]
```

```
KIRPMA KURALI   4,0'lık sahneler 6,0'lık klipten SONDAN kırpılır. Bu yüzden
                her I2V'de TEK iş adımı klibin İLK YARISINA yazılmıştır;
                kırpılan kuyrukta kaybolan şey akşam ışığıdır, kanıt değil.
                S6 (8,0) aracın 10 sn klibinden sondan kırpılır; S9 (10,0)
                kırpılmaz — LOOP klibin SON karesindedir.
⛔ ARAÇ 10 sn VERMİYORSA   S6 ve S9 için ızgara aracın ölçüsünden yeniden
                yazılır (§8 adım 0). Plan bunu şimdiden bilmiyor.
⚠️ DÜZ İSTENİRSE  SÜRE sütunu 6,0'a çekilir; kapı BLOCK verir ve
                ⑥ METRONOM hükmü KABUL EDİLİR [DERS 24: telafi yazılmaz].
```

---

# 3. 🔒 DEĞİŞMEZLER TABLOSU

Her GÖRSEL promptta **birebir, kısaltmasız** tekrarlanır. Köşeli parantez
atfı yasaktır [D-a] — bu dokümandaki on promptun onu da aynı bloğu taşır.

```
┌─ KAMERA İSTASYONU (ANA · 10 sahnenin 10'u) ──────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100                          │
│ yükseklik     3,0 m — üssün güneyindeki alçak kaya çıkıntısı         │
│ mesafe        habitat tümseğinin güney ucundan 40 m                  │
│ bakış açısı   350° (kuzey) · tilt 0° · roll 0°                       │
│ sabitleme     "a fixed tripod bolted to a low rock outcrop"          │
│ ⛔ Sayılar KAMERA_ISTASYONU §3 formülünden ÇIKTI, seçilmedi:          │
│    en yüksek taç = iletişim direği H = 22,0 m · hedef taç ≈ %82      │
│    D = (H − h) / 0,48 = (22,0 − 3,0) / 0,48 = 39,6 m → 40 m          │
│    Taç %81,7 → üst 1/8 (%87,5) sınırının altında. KABUL.             │
│ ⭐ BAKIŞ KUZEYE: 20° kuzey enleminde güneş doğuda doğar, GÜNEYDE 70°'ye│
│    çıkar, batıda batar — kamera arkasında. Güneş HİÇBİR karede        │
│    kadraja girmez; gölge kadrajı soldan sağa süpürür.                 │
│ ⛔ DETAY İSTASYONU YOK — tek istasyon. Ana istasyondan görünmeyen     │
│    hiçbir şey yok; ikinci vantaj yalnız "aynı yer" borcu üretirdi.   │
└──────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — dördü de SAYILI [DERS 19] ────────────────────┐
│ ① arkada, 1,9 km'de, 400 m yükselen KRATER SIRTI: kadraj boyunca     │
│    kesintisiz tek çizgi · merkezin solunda TAM BİR derin V çentiği · │
│    merkezin sağında TAM BİR yuvarlak tepe                            │
│ ② solda, üsle aynı derinlikte, ev boyunda GRİ KAYA: 6,0 m yüksek ·   │
│    9,0 m geniş · yarı gömülü · "too large to move"                   │
│    ⭐ ⑤ merceğinin "aynı yer" kanıt nesnesi VE filmin saat ibresi:   │
│       gölgesi her klipte kadrajı süpürür.                            │
│ ③ sağ ön planda, 18 m'de, TAZE KRATER: 14 m çap · parlak ejekta      │
│    halkalı yüksek kenar                                              │
│ ④ sağ kenarda İLK İNİŞ ARACININ İNİŞ KADEMESİ: sekizgen gövde ·      │
│    5,2 m yüksek · dört ayak 8,0 m açıklık · indiği yerde KALIR       │
│    ⚠️ RENGİ değişir (beyaz → toz grisi = zaman nesnesi), SİLUETİ     │
│       değişmez. Renk SITE bloğuna değil SITE TEXTURE'a yazılır.      │
│ ⛔ Dördü de HER karede aynı yerde, aynı boyutta, aynı kelimelerle.    │
│ ⛔ DÜNYA KADRAJDA DEĞİL. Bu sahada Dünya batı-güneybatıda ~40°        │
│    yükseklikte, kameranın ARKASINDA kalır. Model onu çizmeye         │
│    yatkındır; negatif çekirdek "no Earth" der.                       │
└──────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ───────────────────────────────────────────────────┐
│ ufuk çizgisi   kare yüksekliğinin tam %50'sinde (tilt 0° geometrisi) │
│ kare yüzdesi   %50 + (y − 3,0) × 1,667     ← f=24 · h=3,0 · D=40     │
│ ova (y=0)      %45,0 · kaya tepesi %55,0 · tümsek tacı %56,5         │
│ krater sırtı   %64,2 (11,8° yükseklik açısı · 400 m / 1,9 km)       │
│ güç direkleri  %75,0 · iletişim direği %81,7                         │
│ ⛔ ilerlemeyi kanıtlayan hiçbir şey %25'in altına ve sağ %12,5'e girmez│
│ YERLEŞİM (soldan sağa, x yüzdesi): iletişim direği %14 · kaya %26 · │
│    yol sol alt köşeden hava kilidine · tümsek A %35-58 · tümsek B    │
│    arkada sağa kaymış · güç direkleri %64 ve %74 · iniş aracı %84 ·  │
│    taze krater sağ ön plan %70-90                                    │
└─────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI taşır [DERS 19] ───────────────────┐
│ modül          2 adet · yatay silindir · 12,0 m boy · 4,4 m çap      │
│ ayak           6 kriko ayak · 0,8 m                                  │
│ yerleşim       paralel · eksenler kameradan uzağa · merkezden 12,0 m │
│                · ikinci modül 8,0 m geride, 10,0 m sağda             │
│ tünel          6,0 m boy · 2,0 m çap                                 │
│ tümsek         2,5 m kalınlık · 17,0 × 9,4 m taban · taç 6,9 m       │
│ istinat        regolit torbası duvar · 5,0 m · yalnız güney uçta     │
│ hava kilidi    1,2 m yuvarlak kapak · üstünde 0,6 m lumboz           │
│ güç direği     2 adet · 18,0 m · 14 m aralık · panel 6,0 × 3,0 m    │
│ iletişim       1 kafes direk · 22,0 m · çanak 2,4 m                  │
│ yol            sıkıştırılmış regolit · 4,0 m · sol alt köşe → kilit  │
│ ⛔ Sayısı olmayan satır bible'a YAZILMADI [DERS 19].                  │
└─────────────────────────────────────────────────────────────────────┘
```

⛔ **GEÇİCİ EKİPMAN DEĞİŞMEZ BLOĞA GİRMEZ** [DERS 1]: paletli araç, açık
rover, regolit yığını, torba istifi, ambalaj çerçeveleri, kablo `ACTIVITY` /
`SITE TEXTURE` bloklarında ve §5'in söküm satırında. İniş aracı geçici
DEĞİLDİR — o BEDELDİR ve kalır. Tekerlek izleri de kalır: Ay'da silinmez.

⛔ **VİNÇ YOK.** DERS 8 ve DERS 22 aynı arızayı iki filmde ölçtü (halat
gökyüzüne karşı kopuyor). Bu üste her şey ya kendi kendine yükselir
(teleskopik direkler) ya da paletli aracın kasasıyla indirilir. Arıza
yüzeyi tasarımla kaldırıldı; "crane" kelimesi hiçbir promptta geçmez.

---

# 4. 🪜 AŞAMA MERDİVENİ — 10 satır

Her sahne BİR AY GÜNÜDÜR (14 Dünya günü gündüz). Temsil süresi
"iniş sonrası Ay günü" sayısıyla verilir; bir Ay günü ≈ 29,5 Dünya günü ≈ 1 ay.

| S | SÜRE | AŞAMA | EKRANDA VAR OLAN | YENİ OLAN | TEMSİL | MEVSİM TAŞIYICISI | KANIT NESNESİ | İSTASYON |
|:-:|---:|---|---|---|---|---|---|---|
| 0 | 6,0 | iniş günü · ilk iz | dokunulmamış ova · kaya · krater · beyaz iniş aracı | ⭐ rover rampadan iner, İLK İZ | gün 0 | — mevsim YOK · güneş azimutu tek saat · zaman nesnesi: izsiz ova · bembeyaz araç | ova izsiz; tek yeni nesne iniş aracı, patlama halkası = taze krater genişliği | ANA |
| 1 | 4,0 | düzleme | + 20 × 12 m düz pad · alçak yığın sırtı | pad tamamlanır | gün 2 | — · zaman nesnesi: ilk çift iz üstüne paletli izleri | pad uzak kenarı = kayanın eteği; uzun kenar = 2 kaya genişliği | ANA |
| 2 | 6,0 | ilk güç direği | + direk 6 m'de katlı · kablo · yığın 1,5 m | ⭐ direk 6 → 18 m teleskoplanır | gün 3 | — · zaman nesnesi: yığın büyüyor | katlı direk tepesi = kaya tepesi → 3 kaya boyu | ANA |
| 3 | 4,0 | yığın | + ikinci direk · yığın 3,0 m | yığın tepesi bir kademe çıkar | gün 5 | — · zaman nesnesi: araç ayakları grileşiyor | yığın tepesi = kayanın YARISI | ANA |
| 4 | 6,0 | silindir | + modül A araç kasasında · 6 temel pedi | ⭐ kasa modülü ayaklarına indirir | gün 8 | — · zaman nesnesi: iz yoğunluğu | kasadaki silindir tepesi = kaya tepesi → ayaklarda kayanın hemen altı | ANA |
| 5 | 6,0 | gömme başlar | + yanlarda 2,6 m regolit · 5,0 m torba duvar · kilit + lumboz | regolit çizgisi bir kademe çıkar | gün 10 | — · zaman nesnesi: yığın küçülüyor (1,0 m) | regolit çizgisi = silindir yüksekliğinin YARISI · yığın üçte bire indi | ANA |
| 6 | 8,0 | ⭐ GÖMÜLDÜ (direnç) | + tümsek tacı 6,0 m · yığın bitti · araç ayaklara kadar gri | ⭐ taç 6,0 → 6,9 m: kayayı geçer | gün 14 | — · zaman nesnesi: araç gövdesi çizgili gri · iz yumağı | tümsek tacı ilk kez KAYADAN YÜKSEK (0,9 m) | ANA |
| 7 | 4,0 | anten | + iletişim direği 10 m'de · çanak aşağı kilitli | direk 10 → 22 m teleskoplanır | gün 15 | — · zaman nesnesi: araç tepeye kadar gri | direk tepesi sırt ÇENTİĞİNİN üstünde, iki güç direğinden yüksek | ANA |
| 8 | 6,0 | ikinci tepe | + modül B ayaklarında · tünel tümseği · B tümseği 2,6 m · yol | B tacı A ile eşitlenir | gün 18 | — · zaman nesnesi: yol dışında her yer iz | İKİ taç aynı yükseklikte, arada tünel tümseği | ANA |
| 9 | 10,0 | ⭐ USTA KARE · uzun gün biter | + basınçlı rover kilitte · lumboz yanık · projektör · geçici ekipman YOK | ⭐ gece biter, güneş doğar, çanak Dünya'ya döner | gün 19 (gece → sabah) | — · zaman nesnesi: iz yumağı + ilk çift iz altta + araç tepeye kadar gri | çanak sol üste kilitli; S0 ışığında (100° · 15°) bitmiş üs | ANA |

```
⭐ MEVSİM TAŞIYICISI SÜTUNU "—" DİYOR VE BU BİR BOŞLUK DEĞİL, KARARDIR
   [DERS 14 · seçenek (b)]: Ay'da mevsim yoktur. Her sahne mevsim beyan
   etmez; güneş azimutu tek saattir. Karşılığında A4-a'nın ruhuyla her
   satıra bir ZAMAN NESNESİ yazıldı — iz yoğunluğu ve toz grileşmesi.
   Ay'da izler SİLİNMEZ: iz yoğunluğu, beton kürlenmesinin bu sahadaki
   karşılığıdır — monoton birikir, geriye gitmez.
⛔ ③ MERCEĞİNİN "TIME READ FROM THE FILM ALONE" satırı bu filmde
   MEVSİMDEN okunamaz. Beklenen okuma: "many lunar days". Planın 19 ay
   iddiasını ekrandan doğrulayacak tek şey iz yoğunluğu ve toz. Bu, bu
   planın bilinen açığıdır (§14).
```

### Üç zorunlu satır

```
① KANIT NESNESİ  Her satırda bir NESNE var ve hepsi KAYAYA (6,0 m) ya da
                 SIRT ÇENTİĞİNE göre ölçülüyor: kaya eteği · kaya tepesi ·
                 kayanın yarısı · kayadan 0,9 m yüksek · çentiğin üstü.
                 ⛔ ⑤ İÇİN "AYNI YER" NESNESİ: sol taraftaki 6,0 m KAYA.
                    Bu bir prompt maddesi değil ÜRETİM KAPISI maddesidir
                    [DERS 25]: zincir_kontrol.sh'in her koşusunda kayanın
                    iki karede de aynı yerde ve aynı boyutta olduğu ELLE
                    doğrulanır. Kaybolduysa kare ATILIR.
                 ⭐ İkinci "aynı yer" nesnesi: sağ ön plandaki taze krater.
                    Hiçbir araç içine girmez; kenarı hiçbir sahnede ezilmez.

② LOOP SATIRI    S9'un SON karesi = S0'ın İLK karesi.
                 S9 tam gün değil: gecenin son saatinden sabaha, ve TAM
                 S0'ın açılış ışığında biter: azimut 100° · yükseklik 15° ·
                 kayanın gölgesi sola uzun. Değişen tek şey üstür ve ovadaki
                 izlerdir. ⛔ S9'un ışık yayı diğer dokuzdan farklıdır ve bu
                 bir tutarsızlık değil, LOOP'un bedelidir (MOUNTAIN DOOR S4
                 ile aynı karar).

③ SÖKÜM SATIRI   kurulum ve söküm §5'te takvimli.
```

---

# 5. 🔧 SÖKÜM VE KURULUM TAKVİMİ

```
KURULAN
  açık rover                    S0 (rampadan iner) → S8'e kadar iniş aracının yanında park
  paletli araç (bıçak + kasa)   S1'de belirir (iniş aracından indi) → S8
  regolit yığını (sırt)         S1'de doğar · S3'te 3,0 m · S5'te 1,0 m · S6'da BİTER
  torba istifi + ambalaj çerçeveleri  S1 → S8
  kablo hatları                 S2 (yüzeyde) → S3'ten sonra yarı gömülü, KALIR
  temel pedleri                 S4 · pad yüzeyine gömülü, KALIR

SÖKÜLEN — hepsi S9'dan ÖNCE, S9 karesinde HİÇBİRİ YOK
  paletli araç · açık rover · torba istifi · ambalaj çerçeveleri ·
  yığından kalan son tümsek (S6'da sıfırlanır)

⛔ SÖKÜLMEYEN — bu BEDELDİR, kalır [§1]
  iniş aracının iniş kademesi   S0'da iner → S9'da tepeye kadar toz grisi, YERİNDE
  tekerlek izleri               S0'da ilk çift → S9'da yumak; İLK ÇİFT ALTTA HÂLÂ VAR

ZEMİN DURUMU BİRİKİR — ve Ay'da GERİ GİTMEZ:
  S0 izsiz ova + patlama halkası → S1 ilk çift iz + bıçak izleri → S3 pad
  baştan başa iz → S6 araç–kaya arası iz yumağı, pad gri churned → S8 yol
  dışında her yer iz, yol düz ve koyu → S9 iz yumağı + bot izleri + duvarlar gri
  ⛔ "Temiz regolit" S0 dışında hiçbir promptta yazılmaz.
```

---

# 6. ☀️ GÜNEŞ SAATİ — Ay günü

Her GÖRSEL prompt klibin **ilk karesinin** ışığını yazar; her I2V klibin
**başlangıç VE bitiş** açısını dereceyle yazar [DERS 18]. Fizik: 20° kuzey
enleminde güneş azimut 90°'de doğar, öğlen GÜNEYDE 70°'ye çıkar, 270°'de
batar; bir Ay günü 29,5 Dünya günüdür, gündüz yarısı 14 gün. Kamera 350°'ye
baktığı için güneş hep ARKADADIR; gölgeler sabah SOLA (kuzeybatı), öğlen
UZAĞA (kuzey, kısa), akşam SAĞA (kuzeydoğu) düşer.

| S | An | Başlangıç azimut | Başlangıç yükseklik | Bitiş azimut | Bitiş yükseklik | Yay |
|:-:|---|---:|---:|---:|---:|---|
| 0 | gün 0 · sabah → akşam | 100° | 15° | 260° | 15° | tam gün |
| 1 | gün 2 · geç sabah → akşam | 130° | 40° | 250° | 25° | yarım gün (4,0) |
| 2 | gün 3 · sabah → akşam | 100° | 15° | 260° | 15° | tam gün |
| 3 | gün 5 · erken öğleden sonra → akşam | 150° | 55° | 265° | 12° | yarım gün (4,0) |
| 4 | gün 8 · erken sabah → akşam | 95° | 10° | 255° | 20° | tam gün |
| 5 | gün 10 · geç sabah → akşam | 120° | 32° | 262° | 13° | tam gün |
| 6 | gün 14 · sabah → akşam | 100° | 15° | 262° | 13° | tam gün (8,0) |
| 7 | gün 15 · erken öğleden sonra → akşam | 160° | 62° | 258° | 18° | yarım gün (4,0) |
| 8 | gün 18 · sabah → akşam | 105° | 22° | 262° | 13° | tam gün |
| 9 | gün 19 · GECE → sabah | 85° | 6° ufkun ALTINDA | **100°** | **15°** | gece + şafak (10,0) |

```
⭐ S9'un BİTİŞİ = S0'ın BAŞLANGICI (100° · 15°). LOOP kapısı budur.
⛔ KLİP İÇİ: her klipte gölge kadrajı SÜPÜRÜR; açı değişimi 0° OLAMAZ
   [DERS 18]. On I2V'nin onunda da başlangıç ve bitiş açısı dereceyle var.
⛔ Ay'da atmosfer yok: gölge kenarı jilet, gölge içi yalnız yerden yansıyan
   ışıkla aydınlanır. Alacakaranlık YOK — güneş doğduğu anda gündüzdür.
   S9'da ışık önce direk tepelerine, sonra taçlara, sonra ovaya düşer;
   bu bir "gradyan" değil, yükseklik sırasıdır.
⭐ GECE FİZİĞİ (S9, yalnız gece bölümü): gökyüzü 27,3 günde bir tur döner
   → saatte 0,55°. Gece bölümü ~3 Dünya günü → yıldızlar ~40° kayar.
   Her tek karede yıldız NOKTADIR (kare aralığı dakikalar), klip boyunca
   birlikte kayar. İz YAZILMAZ; kayma DERECEYLE yazıldı [A4-c'nin Ay hâli].
   Gündüz gökyüzünde yıldız YOK (pozlama güneşli zemine göre) — model
   bunu bozmaya en yatkın olduğu yerdir, negatif çekirdek adıyla yasaklar.
```

---

# 7. 🚫 NEGATİF ÇEKİRDEĞİN SAHA UYARLAMASI [DERS 16] — 🌕 AY YÜZEYİ

`KILAVUZ_REHBERI §7` çekirdeği şehir kulesi için yazılmıştır ve altı saha
kartının hiçbiri Ay'ı tanımlamaz. Madde madde okundu; **değişenler ve
gerekçeleri:**

```
① VİNÇ BLOĞU TAMAMEN ÇIKARILDI (§3 gerekçesi). "crane" kelimesi 30 promptun
   hiçbirinde geçmez; metin yasağı yüzey listesi dokuz yüzeyle kalır
   (signage · machinery · containers · vests · helmets · truck ·
   scaffolding · formwork · facade — kapı en az sekiz arar).

② ATMOSFER MADDELERİ TERSİNE ÇEVRİLDİ. Çekirdek "real weather" ve bulut
   çizgisi ister; Ay'da hava yoktur. Yeni madde: "No atmosphere of any
   kind: no blue sky, no haze, no clouds, no dust hanging in the air, no
   wind, no lens flare, no glow along the horizon." TIME RATE cümlesi
   kapı imzası için birebir korunur ve altına tek cümle eklenir: bulut ve
   insan bu ovada yoktur, cümle gölge · makine · panel · araç için geçerlidir.

③ "no star trails" → "in sunlight it holds no stars and no Earth"
   Sebep: Apollo fotoğraflarında yıldız görünmez (pozlama). Model uzay
   deyince yıldızlı gökyüzü ve dev Dünya çizer; ikisi de bu kadrajda
   fiziksel yalandır. S9'un gece karesinde yıldız NOKTA olarak serbesttir.

④ "mud, tyre ruts, puddles, tarpaulins" → "churned regolith, crossing
   wheel tracks, bootprints, half-buried cable runs, stacked regolith
   bags, discarded packing frames" — render çukuru [§9.1] Ay'da da vardır:
   model temiz, parlak, "konsept sanat" üssü çizer. Kirlilik nesnesi
   burada İZDİR.

⑤ "no floor slab without support" → "no floating module, no module
   hanging without support beneath it". Çöken şey döşeme değil silindir.

⑥ TOZ FİZİĞİ EKLENDİ: "Thrown regolith flies in clean ballistic arcs and
   falls at once; no dust cloud lingers." Havasız ortamda toz asılı
   kalmaz — Dünya şantiyesinin toz bulutu burada AI imzasıdır.

⑦ "no science-fiction film look" EKLENDİ render yasağına. Bu sahada
   modelin varsayılan estetiği emlak render'ı değil, bilimkurgu afişidir.

⑧ İNSAN: S0-S8 robotik inşa, kadrajda insan YOK (DERS 15: sayıyı azalt —
   sıfıra indirildi). "soft motion streaks" cümlesi "where any suited
   figure appears" koşuluyla korunur; S9'da bile figür yok, yalnız park
   etmiş basınçlı rover.

KALDIRDIĞI  Çekirdeğin en güçlü gerçeklik taşıyıcıları: bulut çizgisi,
            çamur, insan silueti. Karşılığı: gölge süpürmesi Ay'da
            Dünya'dakinden daha sert ve daha okunur bir saattir, ve iz
            yoğunluğu geri gitmeyen bir takvimdir. [D-f]
```

---

# 8. 🏭 ÜRETİM SIRASI — ⭐ TERS İNŞA

```
0. ⛔ ARAÇ KAPISI  Tek test klibi (S9 usta karesinden) · ffprobe süre ·
                   kamera hareket ediyor mu · geometrik kilit kanalı var mı
                   [DERS 23 · A3-d]. Ediyorsa ARAÇ değişir. Ayrıca bu
                   filme özel üçüncü soru: araç 10 sn klip veriyor mu?
                   (S6 · S9 için). Vermiyorsa §2 ızgarası yeniden yazılır.

1. ⭐ USTA KARE     S9 ÜRETİLİR (gece · bitmiş üs · lumboz yanık · projektör).
                   ⛔ KAPI: sırtın çentiği ve tepesi okunuyor mu, kaya
                      solda 6 m mi, iniş aracı sağda mı, taç %82'nin
                      altında mı, gökyüzü siyah ve DÜNYASIZ mı?
                      Hayırsa DİĞER DOKUZ SAHNE ÜRETİLMEZ.

2. GERİYE İNŞA     Her sahne bir öncekinin KARESİNDEN türetilir:
                     S9 → gündüze çevir, roveri, projektörü kaldır,
                          çanağı aşağı kilitle                    → S8
                     S8 → B tümseğini 2,6 m'ye indir (B kalır)    → S8 ilk kare
                     S8 → B modülünü, tünelı, yolu kaldır         → S7
                     S7 → iletişim direğini 10 m'ye indir         → S7 ilk kare
                     S7 → iletişim direğini kaldır, tacı 6,0'a    → S6
                     S6 → tümseği 2,6 m'ye indir, yığını geri koy → S5
                     S5 → regoliti kaldır, silindiri kasaya koy   → S4
                     S4 → silindiri kaldır, yığını 3,0 m yap      → S3
                     S3 → ikinci direği kaldır, ilkini 6 m'ye katla→ S2
                     S2 → direği kaldır, pad'i bırak              → S1
                     S1 → pad'i sil, izleri sil, roveri rampaya   → S0
                   ⛔ S0'a inerken İZLER TAMAMEN silinir (S0'ın ilk karesi
                      izsizdir); iniş aracı BEYAZA döner. Kaya, krater,
                      sırt hiçbir adımda dokunulmaz.

3. ⛔ ZİNCİR KAPISI — HER KAREDEN SONRA [DERS 12]
                   bash araclar/zincir_kontrol.sh <onceki_onayli> <yeni>
                   Çıkış 2 = zincir kırıldı → kareyi AT, önceki onaylı
                   kareye dön. SONRAKİ SAHNELERİ ÜRETME.
                   ⛔ VE HER KOŞUDA ELLE [DERS 25]: 6 m KAYA iki karede de
                      aynı yerde mi? Taze krater aynı yerde mi? Sırt
                      çentiği aynı x'te mi? Değilse kare ATILIR.

4. VİDEO           Onaylanan her görselden I2V. T2V yalnız I2V tutmazsa.
                   ⛔ S9 ve S6 aracın 10 sn ayarıyla.

5. KURGU           10 klip · sert kesme · geçiş efekti YOK · §2 kesme
                   anları ölçü vuruşunda · + kapak kartı (SON 5 sn)
                   %4 kırpma payı [DERS 6]: kayan klip pay içinde kilitlenir.
```

---

# 9. 🎬 SAHNELER

---
## 🎬 SAHNE 0 — AYAK İZİNDEN ÖNCE

_"Ova üç milyar yıldır dokunulmamıştı. İlk tekerlek izi bu sabah açıldı."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 0 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: nothing of the base exists and the regolith between the lander and the boulder is untouched, without a single track. The first cargo lander has just landed, its legs in the pale blast-cleared ring its engine made, its body bright white, its cargo ramp lowered towards the boulder with one four-wheeled open rover at the top of the ramp. No pad, no mast, no module, no berm and no road exist.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: There is no progress yet, and that is the point of this frame: the regolith between the ramp foot and the boulder carries no mark of any kind, and the only new object on the plain is the lander, whose blast ring is exactly as wide as the fresh crater.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar morning, the first day of the build. Sun azimuth 100 degrees, elevation 15 degrees, behind the camera to the right; shadows pitch black, thrown long to the left and away.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: One open rover stands at the top of the lander's ramp; nothing else moves. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: Untouched regolith pitted with small craters, scattered fist-sized rocks, the pale blast ring under the lander, bright ejecta rays from the fresh crater.

PHYSICS: The lander stands on four legs with its footpads pressed into the regolith; the ramp rests on the ground; the rover's wheels sit on the ramp.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black and in sunlight it holds no stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated lunar day passes — fourteen Earth days of sunlight compressed into the shot. The sun moves visibly across the sky behind the camera: it starts at azimuth 100 degrees and elevation 15 degrees and ends at azimuth 260 degrees and elevation 15 degrees, passing 70 degrees high behind the camera at noon, so the pitch-black shadow of the boulder starts thrown long to the left, shrinks to a short stub pointing away from the camera, and ends thrown long to the right, sweeping the whole plain like a clock hand. At about one second the rover rolls down the lander's ramp and cuts the first pair of wheel tracks into the untouched regolith, driving in a slow straight line towards the boulder and back; by the end of the shot those two tracks, and only those two, run from the ramp foot to the boulder and back, and the thrown regolith behind the wheels falls at once in clean arcs.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — An untouched grey lunar plain under a black sky at lunar morning; one white cargo lander at the right edge with its ramp down and a small rover at the top of the ramp; a house-sized boulder on the left; a fresh crater in the right foreground; a crater rim ridge with one notch and one summit across the horizon.
At 1.0s — The rover rolls down the ramp and cuts the first pair of wheel tracks into the regolith, heading for the boulder.
At 2.5s — The boulder's pitch-black shadow shortens and swings from pointing left to pointing away from the camera as the sun climbs behind it.
At 4.0s — The rover returns along its own tracks; thrown regolith falls at once in clean arcs; no dust hangs.
At 5.2s — The shadows lengthen again and swing to the right as the sun sinks towards the west behind the camera.
By 6s — Two wheel tracks are the only marks on the plain between the lander and the boulder. Hard cut to Scene 1.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 1 — DÜZLÜK

_"Önce yer düzlenir. Uzayda bile."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 1 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: one flat rectangular pad 20.0 by 12.0 metres has been graded to firm regolith in the centre of the frame, its long side running away from the camera, with the loose regolith pushed into a low ridge along its far edge. The six-wheeled crawler with a front blade and a flatbed works on the pad; the open rover stands by the bright white lander. No mast, no module, no berm and no road exist yet.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The far edge of the graded pad sits exactly level with the foot of the boulder, and the pad's long side is exactly two boulder-widths long; the first pair of rover tracks from Scene 0 is still there, now crossed by the crawler's wider tracks.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar late morning, two lunar days after landing. Sun azimuth 130 degrees, elevation 40 degrees, behind the camera to the right; shadows pitch black, medium length, to the left and away.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: One six-wheeled crawler pushes regolith across the pad; the open rover stands parked by the lander. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: Crossing wheel tracks between the lander, the pad and the boulder, blade scrape marks across the pad, one low pale ridge along the pad's far edge, one stack of folded regolith bags.

PHYSICS: The crawler's six wheels press into the regolith and its blade touches the ground; the pushed regolith lies at its natural angle of repose.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black and in sunlight it holds no stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

Half an accelerated lunar day passes — the second half of a fourteen-day lunar afternoon. The sun moves visibly across the sky behind the camera: it starts at azimuth 130 degrees and elevation 40 degrees and ends at azimuth 250 degrees and elevation 25 degrees, so the pitch-black shadow of the boulder swings from pointing left and away to pointing right and away, lengthening as it goes. At about one and a half seconds the crawler's blade pushes the last loose strip of the pad flat in one visible pass and the rectangle of the pad reads as complete; after that the crawler makes slow repeating passes carrying regolith to the ridge along the far edge, which grows by a small step each time, and the thrown regolith falls at once in clean arcs.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 4.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Lunar late morning; a flat graded rectangle in the centre of the plain, its far edge level with the boulder's foot, a low pale ridge along that edge, a six-wheeled crawler on the pad and the white lander on the right.
At 1.5s — The crawler's blade pushes the last loose strip of the pad flat in one pass.
At 2.5s — The crawler carries regolith to the far ridge in slow repeating passes; the ridge grows by a small step each time.
By 4s — The boulder's shadow has swung from left to right and lengthened; the pad is a complete flat rectangle. Hard cut to Scene 2.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 2 — İLK DİREK

_"Güneşten önce hiçbir şey çalışmaz. Direk önce dikilir."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 2 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the pad is graded and the first power mast stands on its anchored base plate 14 metres right of the pad, still collapsed at 6.0 metres, exactly the boulder's height, its array folded flat at its top, one cable on the regolith from its base to the lander; the ridge along the pad's far edge is 1.5 metres high; the lander is bright white. No second mast, no module, no berm and no road exist yet.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The collapsed mast top sits exactly level with the top of the boulder on the other side of the frame; by the end of the shot it will stand three boulder-heights tall.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar morning, three lunar days after landing. Sun azimuth 100 degrees, elevation 15 degrees, behind the camera to the right; shadows pitch black, thrown long to the left and away.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: The crawler stands beside the mast base plate; the open rover stands parked by the lander. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: Crossing wheel tracks thickening between the lander, the pad and the mast base, the growing pale ridge along the pad's far edge, one cable on the surface, a stack of regolith bags and two packing frames.

PHYSICS: The mast base plate is anchored with four ground screws and the collapsed mast stands vertical on it with the folded array latched to its top; the cable lies on the ground along its whole length.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black and in sunlight it holds no stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated lunar day passes — fourteen Earth days of sunlight compressed into the shot. The sun moves visibly across the sky behind the camera: it starts at azimuth 100 degrees and elevation 15 degrees and ends at azimuth 260 degrees and elevation 15 degrees, passing 70 degrees high behind the camera at noon, so the pitch-black shadows of the boulder and of the mast start thrown long to the left, shrink to short stubs pointing away from the camera, and end thrown long to the right, sweeping the plain like clock hands. At about two seconds the mast telescopes upward in one continuous motion from 6.0 to 18.0 metres and its solar array unfolds flat at the top; from then on the array slowly turns to follow the sun behind the camera. The crawler makes slow passes to the ridge along the pad's far edge, which grows by a small step each time.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Lunar morning; a collapsed power mast the height of the boulder stands on a base plate right of the graded pad, its array folded, a cable on the ground to the white lander.
At 2.0s — The mast telescopes up in one continuous motion to three times the boulder's height and its solar array unfolds flat at the top.
At 3.0s — The array slowly turns to follow the sun; the mast's long shadow shortens and swings from left to pointing away.
At 4.5s — The crawler carries regolith to the far ridge in slow passes; thrown regolith falls at once.
By 6s — The shadows have swung long to the right and the mast stands full height with its array facing west. Hard cut to Scene 3.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 3 — YIĞIN

_"Kalkan olacak toprağı önce biriktirmek gerekir."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 3 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the pad is graded, both power masts stand at full height 18.0 metres, 14 metres apart, right of the pad with their arrays open, and the regolith stockpile ridge along the pad's far edge has grown into a long mound 3.0 metres high, exactly half the boulder's height. The lander is bright white above and faintly grey on its legs. No module, no berm, no communications mast and no road exist yet.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The crest of the stockpile ridge reaches exactly half the height of the boulder, and the second power mast now stands where there was only a cable run three lunar days ago.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar early afternoon, five lunar days after landing. Sun azimuth 150 degrees, elevation 55 degrees, high behind the camera; shadows pitch black, short, pointing away and slightly left.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: The crawler tips regolith onto the stockpile ridge; the open rover stands parked by the lander. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: Dense crossing wheel tracks over the pad and between the lander and the boulder, the long pale stockpile mound, two half-buried cables, a stack of regolith bags and packing frames.

PHYSICS: Both masts stand vertical on anchored base plates with the arrays fixed to their tops; the stockpile lies at its natural angle of repose; the crawler's wheels press into the ground.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black and in sunlight it holds no stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

Half an accelerated lunar day passes — a fourteen-day lunar afternoon into evening. The sun moves visibly across the sky behind the camera: it starts at azimuth 150 degrees and elevation 55 degrees and ends at azimuth 265 degrees and elevation 12 degrees, so the short pitch-black shadows of the boulder and of the two masts swing from pointing away to pointing right and stretch across the plain, and both solar arrays turn slowly to follow the sun. At about one and a half seconds the crawler tips one more load onto the stockpile ridge and the crest steps up by one visible increment; after that the crawler makes slow repeating trips from the pad edge to the ridge, and the thrown regolith falls at once in clean arcs.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 4.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Lunar early afternoon; two full-height power masts with open arrays right of the pad, a long pale stockpile mound half the boulder's height along the pad's far edge, the crawler at the mound.
At 1.5s — The crawler tips one load onto the mound and its crest steps up by one visible increment.
At 2.5s — Both arrays turn slowly to follow the sun; the short shadows swing from pointing away to pointing right and stretch.
By 4s — The shadows are long to the right and the mound reads as half the boulder's height. Hard cut to Scene 4.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 4 — SİLİNDİR

_"Ev geldi. Tek parça, beyaz, çıplak."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 4 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the pad is graded, both power masts stand with arrays open, the stockpile ridge along the pad's far edge is 3.0 metres high, and the first module — one white cylinder 12.0 metres long and 4.4 metres in diameter — rests on the flatbed of the crawler standing on the pad, its six jack legs folded under it, above six foundation pads set flush into the pad; the lander is white above and grey on its legs. No berm, no bag wall, no communications mast, no second module and no road exist yet.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The top of the cylinder on the crawler bed sits exactly level with the top of the boulder; by the end of the shot the cylinder will stand on its own six legs on the pad, its top just below the boulder's top.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar early morning, eight lunar days after landing. Sun azimuth 95 degrees, elevation 10 degrees, behind the camera to the right; shadows pitch black, thrown very long to the left and away.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: The crawler stands on the pad with the white cylinder on its flatbed; the open rover stands by the lander. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: Dense crossing wheel tracks over the pad and between the lander and the boulder, the long pale stockpile mound, half-buried cables, a stack of regolith bags.

PHYSICS: The cylinder rests on the flatbed, the flatbed on its six wheels on the pad, the six foundation pads flush beneath; nothing is suspended.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black and in sunlight it holds no stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated lunar day passes — fourteen Earth days of sunlight compressed into the shot. The sun moves visibly across the sky behind the camera: it starts at azimuth 95 degrees and elevation 10 degrees and ends at azimuth 255 degrees and elevation 20 degrees, passing 70 degrees high behind the camera at noon, so the pitch-black shadows of the boulder, the masts and the cylinder start thrown very long to the left, shrink to short stubs pointing away from the camera, and end thrown long to the right. At about two seconds the crawler's flatbed lowers the cylinder in one slow continuous motion until its six jack legs stand on the six foundation pads, and the crawler drives out from under it and away; from then on the cylinder stands alone on the pad on its own legs and does not move. Both solar arrays turn slowly to follow the sun.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Lunar early morning; a white habitat cylinder on the flatbed of a six-wheeled crawler on the pad, its top level with the boulder's top, two power masts on the right, a long stockpile mound behind.
At 2.0s — The flatbed lowers the cylinder in one slow motion onto six jack legs standing on six foundation pads.
At 3.2s — The crawler drives out from under the cylinder and away; the cylinder stands alone and does not move.
At 4.5s — The very long shadows shorten, swing to pointing away, then stretch to the right; the arrays follow the sun.
By 6s — The bare white cylinder stands on its legs on the pad in long evening shadow. Hard cut to Scene 5.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 5 — GÖMME BAŞLAR

_"Radyasyona karşı tek kalkan, üstüne yığılan toprak."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 5 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the first module stands on its six legs on the pad and its burial has begun: regolith is pushed against both flanks to a line 2.6 metres up the cylinder, exactly half its height, and the bag wall stands at its full 5.0 metres around the exposed south end-cap with hatch and porthole; both arrays open; the stockpile behind has shrunk to 1.0 metre; the lander is white above and grey on its legs. No completed berm, no communications mast, no second module and no road exist yet.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The regolith line on the module's flank sits at exactly half the cylinder's height, and the stockpile behind has shrunk to a third of what it was three lunar days ago — the pile is turning into the berm.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar late morning, ten lunar days after landing. Sun azimuth 120 degrees, elevation 32 degrees, behind the camera to the right; shadows pitch black, medium length, to the left and away.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: The crawler pushes regolith up a ramp against the module's west flank; the open rover stands by the lander. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: Dense crossing wheel tracks between the lander, the pad, the stockpile and the boulder, two pale regolith ramps against the flanks, the shrinking stockpile, half-buried cables.

PHYSICS: The regolith against the flanks lies at its natural angle of repose on the pad; the bag wall stands in courses; the module stands on its six legs.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black and in sunlight it holds no stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated lunar day passes — fourteen Earth days of sunlight compressed into the shot. The sun moves visibly across the sky behind the camera: it starts at azimuth 120 degrees and elevation 32 degrees and ends at azimuth 262 degrees and elevation 13 degrees, passing 70 degrees high behind the camera at noon, so the pitch-black shadows of the boulder, the masts and the half-buried module swing from pointing left and away, through short stubs pointing away, to thrown long to the right. At about two and a half seconds the crawler pushes one more ramp of regolith up the west flank and the regolith line on the module steps visibly higher in one movement; after that the crawler makes slow repeating trips from the stockpile to the flanks, the stockpile shrinks a little with each trip, and the thrown regolith falls at once in clean arcs. Both arrays turn to follow the sun.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Lunar late morning; the white module half buried under regolith pushed against both flanks to half its height, a bag wall around its exposed south end with a round hatch and a porthole, two power masts on the right, a shrinking stockpile behind.
At 2.5s — The crawler pushes one more ramp of regolith up the west flank and the regolith line steps visibly higher.
At 3.5s — Slow repeating trips from the stockpile to the flanks; the stockpile shrinks a little each time; thrown regolith falls at once.
At 5.0s — The shadows stretch long to the right as the sun sinks behind the camera; the arrays follow it.
By 6s — The module is half buried and the stockpile is small. Hard cut to Scene 6.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 6 — GÖMÜLDÜ

_"Silindir kayboldu. Yerinde bir tepe var — ve ilk kez kayadan yüksek."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 6 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the first module is almost fully buried: the berm covers it to a flat crest 6.0 metres above the plain, exactly the boulder's height, and only the south end-cap with hatch and porthole shows inside the bag wall; the stockpile is gone and one last low heap lies beside the berm; both arrays open; the lander is dust-grey to the top of its legs and grey-streaked above. No communications mast, no second module and no road exist yet.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The flat crest of the berm sits exactly level with the top of the boulder; by the end of the shot the last loads will lift it 0.9 metres higher, above the boulder for the first time. The stockpile behind it has gone into the berm.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar morning, fourteen lunar days after landing. Sun azimuth 100 degrees, elevation 15 degrees, behind the camera to the right; shadows pitch black, thrown long to the left and away.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: The crawler carries the last heaps of regolith up the berm's flank ramp; the open rover stands by the lander. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: The plain between the lander and the boulder is a dense tangle of crossing wheel tracks, the pad churned grey, one low heap beside the berm, the berm's flank ramp, half-buried cables.

PHYSICS: The berm lies at its natural angle of repose over the module on the pad; the bag wall stands in courses; the crawler's wheels press into the ramp.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black and in sunlight it holds no stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated lunar day passes — fourteen Earth days of sunlight compressed into the shot, and the work is slow. The sun moves visibly across the sky behind the camera: it starts at azimuth 100 degrees and elevation 15 degrees and ends at azimuth 262 degrees and elevation 13 degrees, passing 70 degrees high behind the camera at noon, so the pitch-black shadows of the boulder, the masts and the berm start thrown long to the left, shrink to short stubs pointing away from the camera, and end thrown long to the right, sweeping the plain like clock hands. At about three seconds the crawler tips the load that lifts the flat crest of the berm above the top of the boulder for the first time, one visible step; after that the crawler makes slow repeating trips with the last heaps, the low heap beside the berm shrinks to nothing, and the crest is smoothed flat. Both arrays turn to follow the sun. The lander stands still and grows no whiter.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 8.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Lunar morning; a long flat-topped regolith berm exactly the boulder's height where the white module was, its south end-cap with hatch and porthole showing inside a bag wall, a last low heap beside it, two power masts on the right.
At 3.0s — The crawler tips the load that lifts the berm crest above the boulder's top for the first time.
At 4.5s — Slow repeating trips with the last heaps; the heap beside the berm shrinks to nothing; the crest is smoothed flat.
At 6.0s — The shadows swing from pointing away to long on the right; the arrays follow the sun.
By 8s — The berm stands higher than the boulder and the plain around it is one tangle of tracks. Hard cut to Scene 7.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 7 — ANTEN

_"Ses dünyaya buradan gider."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 7 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the first module is fully buried under its completed berm, crest 6.9 metres above the plain, end-cap showing inside the bag wall; both power masts stand with arrays open; the communications mast stands on its anchored base plate left of the berm, telescoped to 10.0 metres so far, its dish latched pointing straight down at its top; the lander is dust-grey to its top. No second module, no tunnel and no road exist yet.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The half-raised communications mast already stands above the berm crest; by the end of the shot its top will rise above the notch in the crater rim and stand higher than both power masts.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar early afternoon, fifteen lunar days after landing. Sun azimuth 160 degrees, elevation 62 degrees, high behind the camera; shadows pitch black, short, pointing away.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: The crawler stands beside the communications mast base plate; the open rover stands parked by the lander. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: A dense tangle of crossing wheel tracks over the whole plain, churned grey around the berm and the masts, half-buried cables, a stack of regolith bags and packing frames.

PHYSICS: The communications mast base plate is anchored with four ground screws and the mast stands vertical on it with the dish latched to its top; the berm bears on the pad.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black and in sunlight it holds no stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

Half an accelerated lunar day passes — a fourteen-day lunar afternoon into evening. The sun moves visibly across the sky behind the camera: it starts at azimuth 160 degrees and elevation 62 degrees and ends at azimuth 258 degrees and elevation 18 degrees, so the short pitch-black shadows of the boulder, the berm and the three masts swing from pointing away to pointing right and stretch across the plain, and both solar arrays turn slowly to follow the sun. At about one and a half seconds the communications mast telescopes upward in one continuous motion from 10.0 to 22.0 metres and locks, its top rising above the notch in the crater rim; the dish stays latched pointing down. The crawler stands still beside the base plate.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 4.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Lunar early afternoon; a completed berm with its end-cap showing, two power masts on the right, and a lattice communications mast half raised to the left of the berm with a dish latched pointing down.
At 1.5s — The communications mast telescopes up in one motion and locks, its top rising above the notch in the crater rim.
At 2.5s — The short shadows swing from pointing away to pointing right and stretch; the arrays follow the sun.
By 4s — Three masts stand, the tallest on the left, in long evening shadow. Hard cut to Scene 8.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 8 — İKİNCİ TEPE

_"Bir tepe üs değildir. İki tepe ve aralarındaki tünel, üstür."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 8 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the first module is fully buried, crest 6.9 metres; the communications mast stands at its full 22.0 metres with the dish latched pointing down; both arrays open; the second module is in place behind and right of the first on its six legs, joined by the tunnel whose low mound shows between them, its berm at a line 2.6 metres up its flanks, half its height, inside its own bag wall; the compacted road runs to the first airlock; the lander is dust-grey to its top.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: Two crests are now in the frame, the second behind and right of the first at half its final height; by the end of the shot both will stand at the same height, 0.9 metres above the boulder top, with the tunnel mound between them.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar morning, eighteen lunar days after landing. Sun azimuth 105 degrees, elevation 22 degrees, behind the camera to the right; shadows pitch black, thrown long to the left and away.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: The crawler carries regolith up the second module's flank ramp; the open rover stands by the lander. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: A dense tangle of crossing wheel tracks everywhere except the compacted road, smooth and darker, the second berm's flank ramp, half-buried cables.

PHYSICS: Both modules stand on their six legs; both berms and the tunnel mound lie at their natural angle of repose on the pad; both bag walls stand in courses.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black and in sunlight it holds no stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One accelerated lunar day passes — fourteen Earth days of sunlight compressed into the shot. The sun moves visibly across the sky behind the camera: it starts at azimuth 105 degrees and elevation 22 degrees and ends at azimuth 262 degrees and elevation 13 degrees, passing 70 degrees high behind the camera at noon, so the pitch-black shadows of the boulder, the three masts and the two berms start thrown long to the left, shrink to short stubs pointing away from the camera, and end thrown long to the right. At about two and a half seconds the crawler tips the load that brings the second berm's crest level with the first, one visible step; after that the crawler makes slow repeating trips and smooths the second crest flat. Both arrays turn to follow the sun.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Lunar morning; a completed berm in front, a second half-buried module behind and to the right joined by a low tunnel mound, three masts, a smooth compacted road entering from the lower left to the first airlock.
At 2.5s — The crawler tips the load that brings the second crest level with the first.
At 3.5s — Slow repeating trips; the second crest is smoothed flat; thrown regolith falls at once.
At 5.0s — The long shadows swing from left to right across the plain; the arrays follow the sun.
By 6s — Two flat crests at the same height with the tunnel mound between them. Hard cut to Scene 9.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---
## 🎬 SAHNE 9 — ⭐ USTA KARE — UZUN GÜN BİTER

_"On dört günlük gece bitiyor. Işık önce direklere düşer. Ovadaki hiçbir iz silinmemiştir."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 9 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the base is complete and occupied: both modules fully buried under berms with crests 6.9 metres above the plain, the tunnel mound between them; the near porthole glows warm; one white floodlight at the top of the communications mast throws a hard pool on the road and the airlock, where one pressurised rover stands parked with its docking collar against the hatch; the dish is latched pointing down; no crawler, no stockpile and no bag stacks remain; the lander is dust-grey to its top.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The plain between the lander and the boulder is one tangle of wheel tracks, the very first pair from the ramp foot still there under all the others; the lander is dust-grey to its top.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar night, nineteen lunar days after landing. Sun azimuth 85 degrees, elevation 6 degrees below the horizon behind the camera; no sunlight in the frame. Earthshine from the upper left behind the camera lights the plain dim blue-grey with faint soft shadows to the right; black sky, sharp point stars above the ridge, no Earth.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: Nothing moves. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: A dense tangle of wheel tracks and bootprints over the whole plain, the road smooth and darker, the bag walls dust-grey.

PHYSICS: Both modules stand on their legs under berms; the pressurised rover stands on its wheels against the hatch; the dish and floodlight are fixed to the mast.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black; in this night frame it holds sharp point stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

The long lunar night ends. For the first four seconds of the shot it is still night: the plain is dimly lit blue-grey by earthshine from the upper left behind the camera, the porthole glows warm, the floodlight at the top of the communications mast throws its hard white pool on the road and the airlock, and the sharp point stars above the ridge drift slowly together across the black sky, about forty degrees over the night portion, with no trails in any frame. At about four seconds the sun rises behind the camera to the right, at azimuth 88 degrees: the first sunlight strikes the top of the communications mast, then the two solar arrays, then the two berm crests, and then floods across the plain from the right, throwing pitch-black shadows long to the left; the stars vanish the moment the sky is lit, the floodlight and the porthole fade into daylight, and both arrays turn to face the sun. At about seven seconds the dish at the top of the communications mast unlatches and swings up in one slow motion to point high to the upper left, and locks. The sun climbs from the horizon to azimuth 100 degrees and elevation 15 degrees by the last frame, so the shot ends in exactly the light of the first frame of the film, the boulder's shadow thrown long to the left, with a finished base standing where the plain was untouched.

The camera does not move at any point. The framing is identical in the first frame and in the last frame: the boulder on frame left occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no module appears without support beneath it. Everything in this shot is time-lapsed at the same rate: the shadows, the machines, the arrays and the vehicles all move at the same accelerated speed; nothing in the frame moves at normal speed. The sky stays pure black throughout.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 10.0 seconds.
Lens: 24mm on a fixed tripod, 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Lunar night; a finished base of two flat-crested regolith berms, three masts and a parked pressurised rover at a lit airlock, the plain blue-grey under earthshine, sharp point stars above the crater rim, a warm porthole and one hard floodlight pool.
At 2.0s — The stars drift slowly together across the black sky; nothing on the ground moves.
At 4.0s — The sun rises behind the camera to the right: first light strikes the top of the communications mast, then the arrays, then the berm crests.
At 5.0s — Sunlight floods the plain from the right, throwing pitch-black shadows long to the left; the stars vanish; the floodlight and porthole fade into daylight.
At 7.0s — The dish unlatches and swings up in one slow motion to point high to the upper left, and locks.
By 10s — Lunar morning, exactly the light of Scene 0: long shadows to the left, the plain one tangle of tracks, the lander dust-grey. Hard cut back to Scene 0.

The camera never moves. The crater rim ridge with its one notch and one summit, the boulder, the fresh crater and the first lander never change shape, size or position; the horizon stays at exactly half the frame height. The sky is pure black with no atmosphere. No readable text, letters, digits or logos anywhere. No architectural visualisation look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

# 10. 🎶 MÜZİK — tek parça, 65,0 saniye

### 🎶 IZGARA VE KATMANLAR

```
BPM = 240 × (sahne başına ölçü) ÷ 6,0  →  120 BPM = ölçü 2,0 sn
sahne bloğu 30 ölçü (60,0 sn) · kapak kartı 2,5 ölçü (5,0 sn)
sahne başına ölçü: 3 · 2 · 3 · 2 · 3 · 3 · 4 · 2 · 3 · 5  (§2)
kesmeler 0 · 6 · 10 · 16 · 20 · 26 · 32 · 40 · 44 · 50 · 60 — hepsi
ölçünün 1. VURUŞUNDA [A2-e].
KATMAN = KAT: beş katman, her iki sahnede bir tane eklenir, hiçbiri çıkmaz.
⭐ Direnç katmanı S6'da (gömme) gelir ve bir daha gitmez.

⛔ DİEGETİK SES: Ay'da hava yok, ses yok. Bu filmin "ortam sesi" iki
   şeydir ve ikisi de fiziksel olarak savunulabilir: (a) tripoda bolt'lu
   kameraya ZEMİNDEN gelen temas sesi — aracın geçişi, boşalan regolit,
   direğin kilitlenmesi, boğuk ve düşük; (b) telemetri hışırtısı. Rüzgâr,
   uzak trafik, kuş: HİÇBİRİ yok. 0,0-1,5 sn müziksiz pencere BU ikisidir.
```

### 🎶 MÜZİK PROMPTU

```
Instrumental score for a 65-second vertical construction time-lapse on the
lunar surface: a 60-second scene block of ten shots of unequal length
(6, 4, 6, 4, 6, 6, 8, 4, 6 and 10 seconds), followed by a 5-second end card.
No lyrics, no voice, no melody line, no traditional song structure.

Genre: cold minimal electronic-orchestral, documentary, no drum kit, no
science-fiction synth cliché, no choir.
Tempo: 120 BPM, strict and bar-aligned; every shot is a whole number of
2-second bars (3, 2, 3, 2, 3, 3, 4, 2, 3, 5 bars), and every cut lands on
the first beat of a bar.

Layers (one added every two shots, none removed until the final bars):
1. shots 0-1   one dry, close, small pulse on the first beat of each bar
2. shots 2-3   one low sustained bass note, motionless
3. shots 4-5   slow metallic ticks and a single struck pipe, sparse, like
               structure-borne contact sound through a tripod
4. shots 6-7   a wide, cold, bowed-glass drone — the burial layer, the
               widest and coldest moment of the piece
5. shots 8-9   one warm sustained chord pad opening underneath everything,
               resolving as light returns

Dynamic map across 65 seconds:
  0.0-1.5    silence — only faint structure-borne contact sound and a thin
             telemetry hiss; no wind, no air, no room tone
  1.5-10.0   layer 1 alone
  10.0-20.0  layer 2 enters
  20.0-32.0  layer 3 enters
  32.0-44.0  layer 4 enters — the coldest and widest moment
  44.0-50.0  layer 5 enters, the stack sits together
  50.0-54.0  the stack thins to layers 2 and 4 under the lunar night
  54.0-60.0  everything returns and opens as sunlight reaches the plain
  60.0-65.0  end card: everything resolves and decays; the last 1.5 seconds
             carry only the telemetry hiss

Reference feel: the restraint of Jóhann Jóhannsson and the sustained
textures of William Basinski — do not quote either, write new material.

Phone-speaker rule: Every sub-bass element below 150 Hz is doubled by its own
upper harmonics at roughly 100, 150 and 200 Hz so the fundamental is implied
rather than required; the low end is never the only carrier of the weight.
```

### ⛔ MÜZİKSİZ PENCERE

```
⛔ MÜZİKSİZ PENCERE 0,0-1,5 sn. Kanca diegetik sesle açılır: telemetri
   hışırtısı + rampadan inen roverin zeminden gelen boğuk teması.
   Uzun enstrümantal intro elenir.
```

---

# 11. 🖼️ KAPAK KARTI

### 🖼️ KART ÖLÇÜLERİ

```
KAYNAK AN     S9 · 0:54,0 (klibin 4. saniyesi — ilk ışık iletişim direğinin
              tepesine düştüğü kare: gece zemin + aydınlanmış direk tepeleri)
              ⛔ Kapak SIFIRDAN üretilmez. S9'un onaylı karesinden türer.
              ⚠️ Bu kare klibin İÇİNDEN alınır (ffmpeg -ss 54.0); usta
                 kare görseli (gece) değil. Görsel promptu aşağıda yine de
                 tam verildi — I2V tutmazsa kart bu görselden dizilir.
BAŞLIK        "THE LONG DAY"  (İngilizce · 3 kelime · İKİ SATIR: THE LONG / DAY)
TİPOGRAFİ     ⛔ punto · konum · renk · yazı tipi · dizme komutu TEK YERDE:
              THE_LONG_DAY_KAPAK.md — burada tekrarlanmaz.
ANİMASYON     yok · kart 5,0 sn hareketsiz
```

### 🖼️ KAPAK GÖRSEL PROMPTU

```
Photorealistic documentary construction photograph — Scene 9 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the base is complete and occupied: both modules fully buried under berms with crests 6.9 metres above the plain, the tunnel mound between them; the near porthole glows warm; one white floodlight at the top of the communications mast throws a hard pool on the road and the airlock, where one pressurised rover stands parked with its docking collar against the hatch; the dish is latched pointing down; no crawler, no stockpile and no bag stacks remain; the lander is dust-grey to its top.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The plain between the lander and the boulder is one tangle of wheel tracks, the very first pair from the ramp foot still there under all the others; the lander is dust-grey to its top.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar night, nineteen lunar days after landing. Sun azimuth 85 degrees, elevation 6 degrees below the horizon behind the camera; no sunlight in the frame. Earthshine from the upper left behind the camera lights the plain dim blue-grey with faint soft shadows to the right; black sky, sharp point stars above the ridge, no Earth.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: Nothing moves. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: A dense tangle of wheel tracks and bootprints over the whole plain, the road smooth and darker, the bag walls dust-grey.

PHYSICS: Both modules stand on their legs under berms; the pressurised rover stands on its wheels against the hatch; the dish and floodlight are fixed to the mast.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black; in this night frame it holds sharp point stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Leave the black sky above the crater rim visually simple so that a title can be set over it: no structural detail, no strong edge and no bright object between roughly sixty-five and eighty-seven percent of frame height on the left two thirds of the picture, apart from the thin shaft and top of the communications mast at the far left.
Output: 9:16, 4K, no text, no watermark.
```

### ⭐ 120 PX POSTA PULU TESTİ

```
⛔ Prompt hâlâ "no text" der. Başlık modele YAZDIRILMAZ, post-prodüksiyonda
   dizilir — model yazdığı yazıyı bozar.

⭐ 120 PX POSTA PULU TESTİ — İKİ görüntüye birden:
     sips -Z 120 kapak.png --out kapak_120.png
     sips -Z 120 s0_kare0.png --out s0_120.png
   ⓐ SİLUET: siyah gökyüzüne karşı iki düz tepe + üç dikey direk + solda
      kaya kütlesi; sağda iniş aracı
   ⓑ BAŞLIK: üç kelimenin şekli hâlâ ayırt ediliyor mu
   ⛔ ⓐ kayboluyorsa kapak yeniden ÇERÇEVELENMEZ, S9 YENİDEN ÜRETİLİR.
```

---

# 12. 📣 PAKETLEME (İNGİLİZCE)

### 📣 PAKET METNİ

```
TITLES
1. Nothing here ever blows away          (30)
2. One camera, nineteen lunar days       (32)
3. They buried the house on purpose      (34)

DESCRIPTION
On the Moon, the first tyre track you make is there forever.
Over nineteen lunar days a robot crew builds a surface base on an untouched
plain: the pad is graded, two 18-metre power masts go up, a 12-metre habitat
cylinder is set on its legs and then buried under two and a half metres of
regolith for shielding, a second module joins it, and the long night ends
with the lights on. No wind, no weather, no seasons — only the shadow of one
boulder sweeping the ground like a clock hand, fourteen days of sunlight per
shot. The plain keeps every track. The lander that brought it all stays
where it landed, going grey.
Single locked-off camera, 40 metres from the berm, for nineteen lunar days.

#timelapse #construction #engineering #moonbase #lunar #space
#regolith #habitat #civilengineering #spaceengineering #satisfying #moon

This video was generated with AI. It does not document a real project or any
real space agency's plans.

PINNED COMMENT
Why bury the house? On the lunar surface there is no atmosphere and no
magnetic field, so a bare pressurised module takes the full dose of cosmic
rays and solar particle events, and a 14-day night at around minus 170 °C
on the outside. Two to three metres of loose regolith over the module is
the cheapest shielding there is — it is already on site, it only has to be
moved. That is also why the build is slow: roughly nine hundred tonnes of
material goes onto a single module, load by load, with one machine, and
nothing can be done in the dark. And because there is no wind, every track
that machine makes will still be there in a million years.
```

```
⛔ GERÇEKLİK BEYANI: gerçek ajans / program / görev / firma iddiası YOK.
   "Artemis", "NASA", "ESA", "Gateway" gibi adlar hiçbir yüzeyde geçmez.
⛔ YÜKLEMEDE "ALTERED CONTENT" ÜÇ PLATFORMDA DA ELLE İŞARETLENİR —
   açıklamadaki cümle onun yerine geçmez [apexait/youtube/POLITIKA_VE_RISK §2].
```

---

# 13. 🔒 MASTER LOCK

### 🔒 MASTER LOCK METNİ

```
Photorealistic documentary construction photography. Locked-off tripod, one
continuous time-lapse shot, no camera movement of any kind. Physically accurate
sunlight in vacuum: hard black shadows, no atmosphere, black sky. Real dirt,
real tracks, real clutter. Natural motion blur on moving machines and
vehicles. No architectural render look, no CGI aesthetic, no science-fiction
film look, no game engine look, no miniature look, no tilt-shift. Every frame
should look like a real photograph taken from a camera that has been standing
in the same place for nineteen lunar days.
```

---

# 14. ⛔ BU PLANIN BİLİNEN AÇIKLARI

### ⛔ AÇIKLAR

```
· SAHA KARTI YOK. Ay yüzeyi altı saha kartının hiçbirinde değil; §7 bu
  planın kendi uyarlamasıdır ve HİÇBİR maddesi ölçülmedi. İlk üretimden
  sonra kart H ile SAHA §3.8'e iner ya da düşer.
· KLİP SÜRESİ ÖLÇÜLMEDİ [D-d]. 6,0 bir hedeftir. S6 (8,0) ve S9 (10,0)
  aracın 10 sn ayarını VARSAYAR; araç vermiyorsa §2 yeniden yazılır.
· MEVSİM YOK → ③ merceğinin süre tahmini mevsimden okunamaz. Planın 19 ay
  iddiasını ekrandan taşıyan tek şey iz yoğunluğu ve toz grileşmesi; ikisi
  de A4-a'nın Ay çevirisidir ve bu depoda hiç ölçülmedi.
· MODEL DÜNYA VE YILDIZ ÇİZER. Negatif çekirdek adıyla yasaklıyor; tutup
  tutmadığı ① C4 ve ③ C1'den okunacak. Tutmazsa ilk aday ders budur.
· 1/6 g: fırlayan regolitin parabolü ve aracın yavaşlığı I2V'de yazılı;
  modelin Dünya fiziğiyle çizmesi beklenir. Ölçülecek, düzeltilmeyecek.
· S9'UN IŞIK YAYI FARKLI (gece → şafak). Loop'un bedelidir; ③ bunu
  "tutarsız klip içi zaman" okuyabilir (MOUNTAIN DOOR S4 ile aynı risk).
· İNSAN YOK (S0-S8 robotik). ① PEOPLE kategorisi "no people" okuyabilir;
  bu tasarım kararıdır. Ölçek referansı kaya (6 m) ve araçla verilir.
· TERS İNŞA bu depoda hâlâ hiç koşulmadı — en yüksek kaldıraçlı ve en az
  sınanmış adım; A3-a'nın hata birikimi iddiası bu filmde ilk kez sınanır.
· 4,0'lık sahneler 6,0 klipten SONDAN kırpılır: I2V'de yazılan bitiş
  ışığı o üç sahnede ekrana GELMEZ. ③ SUN DIRECTION bunu okuyabilir.
```

---

**QA kilit listesi ve FİNAL KARE KANITI:** `THE_LONG_DAY_QA_SPEC.md`
