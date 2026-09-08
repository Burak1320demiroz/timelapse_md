# 🕳️ BEFORE NIGHTFALL — DİKEY TIMELAPSE PLANI

```
PROJE          BEFORE NIGHTFALL
YAPI           kara deliğin yörüngesindeki gezegende robotik röle istasyonu
               (gömülü basınçlı silindir + kuru örülmüş taş siper + çanaklı direk)
SAHA           havasız gri kayaç ova · deliğe gelgit kilitli yarıküre sınırı
IZGARA         8 sahne × 8,0 sn = 64,0 sn + 5,0 sn kapak kartı
               ⛔ DÜZ IZGARA — proje sahibinin kilidi · §1.2
FORMAT         ⭐ İKİ KEYFRAME ZİNCİRİ — 9 görsel · 8 klip · §2
               foto–video–foto · deponun formatı [KILAVUZ_REHBERI §2.7]
               ⭐ BU FORMATI İLK KOŞAN FİLM BUDUR
YAY            yerel 12,0 saat (tek gün ışığı · yıldız azimut 108° → 247°)
TARİH          08.09.2026 · kart A ile bu depoda yazıldı
DURUM          ⛔ ÜRETİLMEDİ — araç kapısı koşulmadı [ARAC_KARTLARI §4]
```

> ⛔ **BU PLAN ÜRETİME AÇIK DEĞİLDİR.** Kart A adım 7 (klip süresi ölçümü)
> koşulmadı. §1'deki ARAÇ KUTU SETİ satırı ÖLÇÜLMEDEN tek kare üretilmez
> [DERS 23 · A7-a]. 8,0 sn'lik teslim, kutusu {4,6,8} olan bir araçta
> TEK KLİPTE üretilemez (tavan 7,00 sn) — §1.1.

---

# 0. 🚪 KONSEPT KAPISI

```
VAAT     Bu ovada, gökyüzünde hiç kımıldamayan kara halkanın altında, gece
         çökmeden önce basınçlı bir sığınak kapatılacak: kayaya gömülü bir
         silindir, kuru örülmüş bir taş siper ve gökyüzüne nişan almış bir
         çanak. İş bir günün ışığına sığmak zorundadır.
DİRENÇ   GÜN 15,5 SAAT SÜRER VE GECE ÖLDÜRÜR. Hava yoktur; yıldız battığı
         anda yüzey ısısını saniyeler içinde kaybeder. Gömülmemiş bir tank,
         örülmemiş bir siper ve gerilmemiş bir direk geceyi çıkaramaz.
         Ve zemin sabit değildir: yörünge 0,04 eksantrikliktedir, gelgit
         gerilimi 15,5 saatte bir zirve yapar ve altta duran eski fay çalışır.
         EKRANDA NASIL  Saat GÖLGE BOYUDUR ve her sahnede sayıyla yazılıdır
         (2,87 → 0,53 → 2,25 metre/metre). S4'te vuruş gelir: toz duvarın
         tacından yelpaze hâlinde akar, sıradaki bir slab devrilir ve eğik
         taşın yanındaki çatlak 0,35 m'den 0,52 m'ye açılır. Yığın erirken
         gölge uzar — filmin iki ölçeği budur.
BEDEL    İNİŞ ARACI BİNANIN KENDİSİDİR. Tankı sığınak olur, dış paneli
         sığınağın örtüsü, güvertesi panel tablası. Günün sonunda ovada üç
         bacak ve boş bir halka kalır; geri dönüş taşınmıştır.
         Ve fay kapanmaz: üssün oturduğu çatlak 0,52 m'de, doğu ankrajının
         altından geçerek durur. Üs bitti; zemin bitmedi.
```

```
① TEK KARE TESTİ       ✅ Tek karede kaç kurs örülmüş, kaç direk bölümü
                          dikilmiş, tank açıkta mı gömülü mü ve gölge ne kadar
                          uzun — dördü de sayılabilir.
② KİNETİK BAĞIMSIZLIK  ✅ Gölge 23° süpürür ve boyu yarıya iner; slab dizilir,
                          yığın erir, panel dizisi yıldızı izler. Metin yok.
③ BAŞLIK ŞEMASI        ✅ "BEFORE NIGHTFALL" (2 kelime · 16 karakter)
④ OMURGA CÜMLESİ       ✅ daireyi süpürür → çukuru açar → taşı keser →
                          tankı indirir → duvarı örer → direği diker
```

---

# 1. 📐 TESLİM YAPISI VE ARAÇ

## 1.1 Teslim yapısı

```
SAHNE BLOĞU    8 sahne × 8,0 sn = 64,0 sn    ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn =  5,0 sn    ← SAHNE DEĞİL · konusu DEĞİL
               ⛔ KONUM: teslimin SON 5 saniyesi [DERS 4 · A1-b]
─────────────────────────────────────────
TOPLAM                            69,0 sn

ARAÇ KUTU SETİ ⛔ ÖLÇÜLMEDİ — üretim günlüğü §0'da ffprobe ile doldurulacak.
               Sahne tavanı = (en büyük kutu − 1,00 sn) [ARAC_KARTLARI §2].
               ⚠️ BU PLANIN HER SAHNESİ 8,0 sn'dir. Yani:
                  {4,6,8} kutusu → tavan 7,00 sn → ⛔ HİÇBİR SAHNE tek klipte
                     teslim edilemez. Uzatma ya da iki klip dikişi ZORUNLU
                     olur ve üretim günlüğüne yazılır.
                  {5,9}  kutusu → tavan 8,00 sn → ✅ sekiz sahne de tek klip.
                  {5,10} kutusu → tavan 9,00 sn → ✅ sekiz sahne de tek klip.
               ⭐ Yani araç kapısının ilk ölçümü BU FİLMİN ÜRETİLEBİLİRLİĞİDİR.
ÜRETİM SÜRESİ  = TESLİM SÜRESİ + 1,00 sn (baş/son kırpma) → 9,0 sn [A8 · A7-b]
               ⚠️ KIRPMA BU FİLMDE ASİMETRİKTİR — sebebi §2.4'te.
```

## 1.2 ⛔ DÜZ IZGARA — PROJE SAHİBİNİN KİLİDİ

```
prompt_kontrol.py bu planda TEK BİR BLOCK verir ve o BLOCK BİLEREK
oradadır: "AŞAMA MERDİVENİNDE bütün sahne süreleri aynı (8,0)" [DERS 13].

(a) GEREKÇE
    Proje sahibi altı sahnenin de 8,0 sn olmasını istedi ve seçenekler
    (48,0 sn'yi koruyan varyanslı ızgara · 8,0 sn üretip kırparak varyans)
    açıkça sunulduktan sonra düz ızgarada karar kıldı. KILAVUZ_REHBERI §2.6
    bunu meşru sayar: "proje sahibinin kilidi meşru bir sebeptir" — karşılığında
    plana yalnız gerekçe ve KABUL EDİLEN RİSK yazılır. Bu bölüm odur.
    ⭐ Teknik olarak da tutarlı: 120 BPM'de ölçü 2,0 sn ve 8,0 sn TAM DÖRT
       ÖLÇÜDÜR — sekiz kesme de vuruşun üstüne oturur [MUZIK_VE_KAPAK §1.1].

(b) KABUL EDİLEN RİSK
    ⑥ GEÇİŞ merceği METRONOM hükmü verebilir. Bu depoda METRONOM BEŞ KEZ
    geldi (CLOSING SPAN · NARROW LOT · LONG DAY · MOUNTAIN DOOR · DUST YEAR)
    ve hüküm skor ortalamasını yener [değişmez ⑩]. Risk kabul edilmiştir.

(c) ⭐ VE BU FİLM DERS 44'Ü SINAR — bedava gelen tek şey bu
    DERS 44 ölçtü: THE DUST YEAR'ın ızgarası DÜZ DEĞİLDİ (dört farklı süre,
    2,5 kat aralık) ve hüküm yine METRONOM oldu. Merceğin gerekçesi süreleri
    hiç anmadı: "anchor survival across the seams … the edits read as a
    slideshow". Yani ⑥ ⑤'İN ALTINDADIR.
    Bu film ⑤'i YAPISAL olarak çözüyor (§2: dikişin iki yakası AYNI KAREDİR).
    ⇒ Düz ızgara + kusursuz dikiş = DERS 44'ün tersten sınanması.
       Hüküm METRONOM gelmezse süre varyansı gerçekten YETER ŞART değildi.
       Gelirse düz ızgara yasağı ölçülmüş olarak KALIR ve bu film onun
       altıncı kanıtıdır. İki sonuç da bilgi.
```

## 1.3 ⚠️ FORMATTAN BİLİNÇLİ SAPMALAR — ikisi de sahibinin seçiminden doğdu

> ⭐ **08.09.2026: BİR SAPMA SAPMA OLMAKTAN ÇIKTI.** "Kesme artık zaman
> sıçraması değil" maddesi bu filmin özel tercihiydi; artık DEPONUN FORMATI
> [KILAVUZ_REHBERI §2.7 ①]. Gerekçesi, bedeli ve kapısı orada durur; burada
> yalnız bu filme düşen SONUCU yazılıdır:
> **film SÜREKLİDİR — 12,0 saatlik tek bir gün, sekiz pencereye bölünmüş.**
> Bu filmde bedeli somuttur: "aylar geçiyor" anlatısı düşer, yerine "bir gün"
> gelir — ve zaten filmin vaadi de odur.

```
① MEVSİM YAYI YOK, GÜN YAYI VAR
   Bu gezegende mevsim yoktur (delik ısı vermez, eksen eğikliği anlamsızdır).
   "Kış iki sahnedir" [DERS 7] burada karşılıksızdır. Yerine GÜNÜN KENDİSİ
   geçer: gölge oranı 2,87 → 0,53 (öğle) → 2,25 (akşam). Zamanın taşıyıcısı
   GÖLGE BOYUDUR ve altı sahnede de sayıyla yazılıdır.
② GECE KADRAJA GİRMEZ
   Gecede tek ışık kaynağı kalmaz ve arka plan çapaları görünmez olur —
   ⑤ için ölümcül. Gece filmin DİRENCİDİR, sahnesi değildir: yaklaştığı
   gölge boyundan okunur ve son karede henüz gelmemiştir.
```

---

# 2. 🔗 KARE TABLOSU — 7 GÖRSEL · 6 KLİP

> ⭐ **YÖNTEMİN KENDİSİ ARTIK KILAVUZDA:** `KILAVUZ_REHBERI §2.7` — sayılar,
> I2V'nin iki uç cümlesi, T2V'nin düşüşü, asimetrik kırpma, araç kapısının
> sekizinci sorusu ve formatın BEDELİ orada durur. Burada yalnız BU FİLMİN
> kareleri, çapası ve üretim notu vardır [değişmez ①].

```
G0 ──klip 0──▶ G1 ──klip 1──▶ G2 ──klip 2──▶ G3 ──klip 3──▶ G4 ──klip 4──▶ G5 ──klip 5──▶ G6 ──klip 6──▶ G7 ──klip 7──▶ G8
foto1   video1  foto2  video2  foto3  video3  foto4  video4  foto5  video5  foto6  video6  foto7  video7  foto8  video8  foto9

Her klip İKİ kareyle kilitlidir: ilk kare G(n), son kare G(n+1).
Her görsel İKİ kez kullanılır: bir klibin sonu, sonraki klibin başı.
⇒ 9 görsel · 8 video · 0 dikiş boşluğu.
```

| görsel | ne gösterir | hangi klipte | rolü |
|:--|:--|:--|:--|
| **G0** | çıplak ova · bütün iniş aracı · süpürülmüş ilk yay | klip 0 | İLK KARE |
| **G1** | kapanmış 26,0 m'lik süpürülmüş daire | klip 0 → 1 | dikiş |
| **G2** | çukur taslağı 0,6 m · ilk slab yığını · soyulmuş panel | klip 1 → 2 | dikiş |
| **G3** | tank kancada, çukurun üstünde asılı · çukur 1,4 m | klip 2 → 3 | dikiş |
| **G4** | tank çukurda · ilk taş kursu · direk taban plakası | klip 3 → 4 | dikiş |
| **G5** | duvar 4 kurs · tank örtülü · direk 3 bölüm iskelede | klip 4 → 5 | dikiş |
| **G6** | kapak gömülü · hatch görünüyor · direk 5 bölüm | klip 5 → 6 | dikiş |
| **G7** | kilitli hatch · sığınak kapalı · makineler çekiliyor | klip 6 → 7 | dikiş |
| **G8** | ⭐ USTA KARE — istasyon mühürlendi · gece başlıyor · gölgeler sonsuz | klip 7 | SON KARE |

```
⛔ ÜRETİM SIRASI TERSTİR VE DEĞİŞMEZ [KILAVUZ_REHBERI §8 · DERS 5 · 12]:
   1. G8 USTA KARE üretilir. İkna etmiyorsa DİĞER KARELER ÜRETİLMEZ.
   2. G8 → image-to-image → G7 → G6 → G5 → G4 → G3 → G2 → G1 → G0
      ⭐ ZİNCİR = EDİT [P2-a]: her kare bir öncekinin TARİHSEL sürümüdür.
        Üretim notu tek satır: "G8'den ne KALDIRILDI / ne EKLENDİ".
   3. HER KAREDEN SONRA, SONRAKİNE GEÇMEDEN:
        bash araclar/zincir_kontrol.sh <onceki_onayli> <yeni>
      Çıkış 2 = zincir kırıldı → kare ATILIR, önceki onaylıya dönülür.
   4. ⛔ VE HER KOŞUDA EĞİK TAŞ ELLE DOĞRULANIR [DERS 25]: iki karede de
      aynı yerde, aynı 12° eğimde mi? Değilse kare ATILIR — betik geçse bile.
   5. Dokuz kare onaylandıktan SONRA sekiz I2V koşulur; her I2V iki ONAYLI
      kare arasında üretilir. Somut hedef karesi olmayan I2V yazılmaz.

⚠️ BU FİLM ZİNCİR İDDİASINI DA SINAR [A3-a]: dış araştırma ardışık
   image-to-image'in hata BİRİKTİRDİĞİNİ söylüyor. Burada zincir dokuz karedir
   ve her adımı ölçülür; kırılırsa nerede kırıldığı ilk kez KAYITLI olur.
   ⭐ Formatın gerekçesi ve neden geometri kanalı olduğu: §2.7 "Neden".
```

## 2.4 ⚠️ KIRPMA ASİMETRİKTİR — artık kuralın kendisi

```
⭐ 08.09.2026: bu da kılavuza çıktı [KURGU_VE_TESLIM §2 · §2.7 ③]. Baştan
   25-30 kare, sondan 0-5 kare — son kare HEDEFTİR, atılırsa dikiş gider.
BU FİLMDE SAYISI: 9,0 sn üretilen klipten 30 kare BAŞTAN, 0-5 kare SONDAN.
⛔ VE ÖLÇÜLECEK: kuralın dayandığı "son karesi kilitli klipte uç erimez"
   varsayımı hiç sınanmadı. Üretim günlüğüne her klibin son 5 karesi ile
   hedef görsel arasındaki zincir_kontrol çıktısı yazılır — bu filmin
   ölçümü, kuralın ilk kanıtı olacak.
```

---

# 3. 🔒 DEĞİŞMEZLER

```
┌─ KAMERA İSTASYONU (ANA · tek istasyon · detay istasyonu YOK) ────────┐
│ lens          24 mm küresel · f/8 · ISO 100                          │
│ yükseklik     h = 6,0 m — ovanın güneyindeki kaya çıkıntısı          │
│ D_kenar       27,0 m — süpürülmüş dairenin güney kenarı (güvenli alan)│
│ D_eksen       40,0 m — saha ekseni = direk ekseni ⭐ BÜTÜN YÜZDELER   │
│               bu mesafeden hesaplandı [DERS 38]                       │
│ bakış açısı   000° (kuzey · halka tam karşıda) · tilt 0° · roll 0°    │
│ kadraj        33,75 m geniş × 60,0 m yüksek · 32,0 px/m               │
│               ⭐ genişlik = 36×(9/16)×D/f = 0,84375 × 40,0 [08.09]    │
│ alt çeyrek    D_alt = 24×6,0/9 = 16,0 m — en yakın saha nesnesi 27,0 m│
│               ✅ hiçbir iş kadrajın alt çeyreğine düşmez              │
│ ⚠️ TAÇ %82 HEDEFİ TUTMADI VE SEBEBİ YAZILI [KAMERA_ISTASYONU §3]:     │
│    D = (H−h)/0,48 = (15,0−6,0)/0,48 = 18,75 m ister; 18,75 m'de kadraj│
│    15,8 m geniştir ve 26,0 m'lik daire SIĞMAZ. Geniş sahada kadrajı   │
│    GENİŞLİK kurar: D_eksen 40,0 m seçildi, direk tacı %64,0'ta durur. │
│ ⭐ YILDIZ HER SAHNEDE KAMERANIN ARKASINDA: azimut bandı 108°–247°,    │
│    kadraj 337,1°–022,9° arası. Yıldız hiçbir karede kadraja giremez   │
│    [DERS 32]. LIGHTING bloğunda "disk" kelimesi HİÇ geçmez [DERS 39]. │
└──────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — üç, isimlendirilmiş, KALICI ──────────────────┐
│ ① KARA HALKA — gökyüzünde SABİT. Gezegen deliğe gelgit kilitli       │
│    olduğu için delik hiç doğmaz, hiç batmaz: merkezi tam ufuk        │
│    çizgisinde. GÖLGE ÇAPI 46,57° [sin α = √27(M/r)√(1−2M/r), r=12M]   │
│    → kadraj genişliğinin %102,0'si: halka İKİ KENARDAN DA TAŞAR ve    │
│    görünen şey bir YAY'dır. Tepesi kare yüksekliğinin %78,7'sinde.    │
│    İçi düz siyah, kenarı jilet gibi keskin, çevresi tek ince halka.   │
│    ⭐ 08.09.2026 DÜZELTİLDİ: plan %88 genişlik + %81,6 tepe diyordu;  │
│      9:16'da ufka oturan daire için tepe% = 50 + 0,28125 × genişlik%  │
│      — ikisi aynı anda olamaz. Fizik doğruydu, izdüşüm yanlıştı.      │
│      r_px = 1280·tan(23,284°) = 551 px [DERS 38: üretilemeyen yüzde]  │
│    ⛔ PROMPTTA ADI GEÇMEZ [DERS 42]: "black hole" korpusu turuncu     │
│       yığılma diskidir. Prompta yalnız GEOMETRİ iner.                │
│ ② EĞİK TAŞ — 3,0 m boy · 0,8 m kalınlık · 12° kuzeye eğik · D 34 m   │
│    ⭐ ⑤ "AYNI YER" NESNESİ. 3,0 m = 96 piksel. Her zincir_kontrol     │
│      koşusunda ELLE doğrulanır [DERS 25].                            │
│ ③ FAY SARPI — ufku boydan boya kesen düz basamak, tepesi ovadan      │
│    4,0 m yüksek, kadrajın sol kenarına yakın bir kez alçalır.        │
│ ⛔ Üçü de her karede aynı yerde, aynı boyutta, aynı şekilde.          │
└──────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE — hepsi D_eksen = 40,0 m'den hesaplandı ───────────┐
│ ufuk çizgisi        %50,0 — tilt 0° geometrisinin sonucu             │
│ süpürülmüş taban    %39,0  ·  dairenin yakın kenarı (D 27 m) %35,2   │
│ tank tacı           %42,0  ·  duvar tacı (3,2 m) %44,8               │
│ eğik taşın tepesi   %44,1  ·  fay sarpı %49,3                        │
│ çanak merkezi       %59,0  ·  direk tacı %64,0                       │
│ ⭐ OKUNABİLİRLİK EŞİĞİ 0,5 m = 16 px [INSAAT_YONTEMI §1]             │
│    Bundan küçük hiçbir nesne prompta yazılmadı.                       │
│ güvenli alan  üst 200-254 px · alt 484 px · sağ 242 px · sol 122 px  │
│    ✅ ilerlemeyi kanıtlayan hiçbir şey sağ 1/8'e ve alt 1/4'e düşmez │
└──────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI taşır [DERS 19] ───────────────────┐
│ süpürülmüş daire   Ø26,0 m · kabuk sıyrılmış, çıplak açık kayaç      │
│ çukur              13,0 × 5,0 m · derinlik 1,4 m · yakın ucu iki     │
│                    basamaklı                                          │
│ sığınak            yatık çelik silindir · Ø4,2 m · boy 12,0 m · düz  │
│                    dairesel kapaklar · üstünde 1,6 m'lik kare kapak  │
│                    kutusu · üç çift taş takoz üstünde                │
│ siper duvarı       kuru örülmüş kesme taş · 4 kurs × 0,80 m = 3,2 m ·│
│                    boy 18,0 m · her kurs 0,30 m geri çekilir         │
│ direk              cıvatalı üç ayaklı gergili kule · 5 bölüm × 3,0 m │
│                    · taç 15,0 m · 3 gergi teli, 9,0 m dışarıda ankraj│
│ çanak              Ø2,4 m parabolik yansıtıcı · 4. bölümde           │
│ panel dizisi       tek sırada 8 düz panel · 12,8 m genişlik · iniş   │
│                    aracının sökülmüş güvertesi üstünde · yıldızı izler│
│ ⭐ SAYI TESTİ: 4 kurs · 5 bölüm · 3 tel · 8 panel · 3 bacak — hepsi  │
│    kadrajda SAYILABİLİR (32 px/m).                                   │
│ ⛔ GEÇİCİ EKİPMAN BU BLOKTA YOK [DERS 1]: sapan · kablo kancası ·    │
│    iskele kafesi · takozlar · slab yığını → SITE TEXTURE / ACTIVITY. │
│ ⛔ AD DEĞİL GEOMETRİ [DERS 42]: "kubbe" · "sondaj kulesi" · "kum     │
│    torbası" korpuslarına düşmemek için her satır ölçüsüyle yazıldı.  │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 4. 🪜 AŞAMA MERDİVENİ

| S | SÜRE | REJİM | AŞAMA | ELEMAN · ARA HÂL | EKRANDA VAR OLAN | YENİ OLAN | TEMSİL | MEVSİM TAŞIYICISI | KANIT NESNESİ | KİNETİK | İSTASYON |
|:-:|---:|:-:|---|---|---|---|---|---|---|---|---|
| 0 | 8,0 | B | DAİREYİ SÜPÜRÜR | daire %25 | çıplak ova · bütün iniş aracı | 8,0 m süpürülmüş yay | 2 saat | gölge oranı 2,87 → 1,16 (sabah) | süpürülmüş yay eğik taşın dibine ulaşır | süpürür | ANA |
| 1 | 8,0 | B | ÇUKURU AÇAR | daire %100 · çukur %25 | + kapalı daire · spoil sırtı | 13,0 × 5,0 m çukur taslağı 0,6 m | 2 saat | gölge oranı 1,16 → 0,68 | daire eğik taşı iki yandan geçer | açar | ANA |
| 2 | 8,0 | B | TAŞI KESER | çukur %100 · slab stoğu | + 0,6 m çukur · 6 slab | 1,4 m çukur · ~30 slab · sökülmüş panel | 2 saat | gölge oranı 0,68 → 0,53 ⭐ günün en kısası | slab dizisi çukur boyu kadar uzar | keser | ANA |
| 3 | 8,0 | B | TANKI İNDİRİR | sığınak %50 | + çukur · slab dizisi · asılı tank | tank çukurda, takozlarda | 2 saat | gölge oranı 0,53 → 0,62 (öğle döndü) | tank tacı süpürülmüş tabandan 1,4 m yukarıda | indirir | ANA |
| 4 | 8,0 | B | DUVARI ÖRER | duvar %100 · sığınak %75 | + oturmuş tank · ilk kurs | 4 kurs · 3,2 m · örtülü tank | 2 saat | gölge oranı 0,62 → 1,01 · ⭐ VURUŞ | duvar tacı eğik taşın tepesiyle aynı hizada | örer | ANA |
| 5 | 8,0 | A | DİREĞİ DİKER | direk %100 · dizi %100 | + duvar · 3 bölüm iskelede | 5 bölüm · çanak · gergi · 8 panel | 10 dakika | gölge oranı 1,01 → 2,25 | direk tacı eğik taşın beş katı yüksekte | diker | ANA |
| 6 | 8,0 | B | KAPAĞI KAPATIR | sığınak %100 | + çanak · gergi · 8 panel | 1 saat | gölge oranı 2,25 → 4,70 | gölge çukurun sınırını aşar | kapatır | ANA |
| 7 | 8,0 | B | ÜSSÜ MÜHÜRLER | istasyon %100 | + örtülü sığınak · kilitli hatch | 45 dakika | gölge oranı 4,70 → 19,0 ⭐ gece başlıyor | gölgeler kadrajdan taşar | mühürler | ANA |

```
TOPLAM 64,0 sn · sekiz sahne de 8,0 sn — ⛔ DÜZ IZGARA, sahibinin kilidi (§1.2)
120 BPM · ölçü 2,0 sn → her sahne TAM 4 ÖLÇÜ · sekiz kesme de vuruş üstünde.

⚠️ "MEVSİM TAŞIYICISI" SÜTUNU BU GEZEGENDE MEVSİM TAŞIMAZ: bu dünyada mevsim
   yoktur (§1.3②). Sütun GÜNÜN taşıyıcısını taşır — gölge oranı — ve altı
   satırın altısında da sayıyla doludur. Sütun adı kapı ile aynı kalsın diye
   değiştirilmedi [prompt_kontrol §10b].

KİNETİK İMZA  süpürür · açar · keser · indirir · örer · diker
              ✅ Sekiz fiil de farklı; ardışık iki satırda tekrar yok [P1-f].

İLK 20 SANİYE (S0+S1+S2 = 24,0 sn) — üçü de FARKLI TÜRDEN değişim [P1-a]:
              S0 yüzey SIYRILIR · S1 zemin OYULUR · S2 malzeme ÜRETİLİR
              Test: S2'nin son karesi ile S0'ın ilk karesi yan yana → çıplak
              ovaya karşı, açık çukur + otuz kesme taş + sökülmüş iniş aracı.
              Yapının TÜRÜ okunur ✅

⭐ REJİM: beş sahne B (2 saat · 1200×), yalnız S5 A (10 dakika · 100×).
   İki rejim — kılavuzun izin verdiği üst sınır [SANTIYE_HAREKETI §2].
   S5'in A olmasının sebebi P2-i: usta kare klibinin son ≥2,0 saniyesi bir
   TUTUŞTUR; yapı ve ışık durur, yalnız toz akar. Rejim B'de bu tutuş,
   beyan edilen gölge süpürmesiyle çelişirdi.
⛔ DERS 40 kapısı bu filmde açılmaz: gölgesiz sahne YOK — altı sahnenin
   altısında da gölge oranı sayıyla yazılı ve altısı da farklı.
```

### Üç zorunlu satır

```
① KANIT NESNESİ   Her satırda yukarıda. ⑤ AYNI YER nesnesi: EĞİK TAŞ
   (3,0 m · 0,8 m kalınlık · 12° eğim · 96 px).
   ⛔ Her zincir_kontrol koşusunda iki karede de aynı yerde ve aynı eğimde
      olduğu ELLE doğrulanır; değilse kare ATILIR [DERS 25].
   ⭐ İKİNCİ KANIT — FAY ÇATLAĞI: eğik taşın dibinde 0,35 m; S4'teki vuruştan
      sonra 0,52 m. Genişlik taşın KALINLIĞINA göre okunur (0,8 m): önce
      yarısından az, sonra üçte ikisi. Bu, hem zamanın hem BEDEL'in nesnesi.

② LOOP SATIRI     G6 ile G0 AYNI KADRAJDIR: aynı istasyon, aynı çapa
   boyutları, aynı ufuk. ⛔ IŞIK AYNI DEĞİLDİR VE OLAMAZ: iki keyframe
   zinciri ışığı sürekli kılar (§1.3①), film tek bir günün 12 saatidir.
   Sabah 19° / gölge 2,87 → akşam 24° / gölge 2,25: yön ters, boy benzer.
   Çıplak ova → kapanmış istasyon, aynı çerçeve, düşen ışık.

③ SÖKÜM SATIRI    geçici ekipman ne zaman kurulur, ne zaman sökülür —
   hiçbiri kendiliğinden kaybolmaz, her biri I2V'de FİİL alır [P2-h]:
   iniş aracı dış paneli  S1'de sökülür → S4'te tankın örtüsü olur
   kablo kancası + sapan  S2'de gerilir → S3'te boşalır ve yukarı çekilir
   iniş aracı güvertesi   S4'te sökülür → panel dizisinin tablası olur
   direk iskele kafesi    S4'te kurulur → S5'te sökülüp duvarın dibine
                          düz istiflenir
   slab yığını            S1'de doğar → S5'te BİTER (eksilen istif = iş kanıtı)
   ⛔ SÖKÜLMEYENLER — bunlar BEDEL'dir, kaybolurlarsa film yalan söyler:
      iniş aracının üç bacağı ve boş halka çerçevesi  S0 → G6'da hâlâ ayakta
      fay çatlağı                                     0,35 → 0,52 m, açık
      spoil sırtı ve kesme yüzü                       daire kenarında kalır
```

---

# 5. ☀️ IŞIK VE ZAMAN — hesaplanmış

```
DELİK        1,0 × 10⁸ M☉ · GM/c² = 1,477×10¹¹ m · GM/c³ = 493 s
YÖRÜNGE      r = 12 GM/c² = 1,772×10¹² m = 11,85 AU
             ISCO = 6 GM/c² → yörünge ISCO'nun İKİ KATI, kararlı.
YIL          uzaktan 35,7 saat · YEREL 31,0 saat  [√(1−3M/r) = 0,866]
ZAMAN        yerel 1 saat = uzakta 1,155 saat. Filmin 12,0 yerel saati,
             uzakta 13,9 saattir.
GÜN = YIL    Gezegen deliğe gelgit kilitlidir: bir gün bir yıla eşittir ve
             delik gökyüzünde HİÇ KIMILDAMAZ. Gündüz yarısı 15,5 saat.
GELGİT       2GM/r³ = 4,8×10⁻⁹ s⁻² → 12,0 m'lik tank boyunca 5,7×10⁻⁸ m/s².
             Yapısal olarak SIFIR. ⭐ Delik bu yüzden SÜPERKÜTLELİ seçildi:
             yıldız kütleli bir delikte aynı yörüngede gelgit (M/r³) gezegeni
             parçalar. Ama e = 0,04 eksantriklik gerilimi yörünge başına iki
             kez değiştirir → alttaki eski fay 15,5 saatte bir çalışır (VURUŞ).
IŞIK         ⛔ DELİK IŞIK VERMEZ ve veremez: 11,85 AU'da Eddington'ın
             milyonda biri kadar bir yığılma bile yüzeye 3,3×10⁷ W/m² basar
             (Dünya güneş sabitinin 24.000 katı) — gezegen kalmaz.
             ⇒ Delik SESSİZDİR. Işığı, aynı deliğin çevresinde çok daha geniş
             yörüngede duran mavi dev yıldız verir (≈430 AU): yer ışınımı
             Dünya'nın ≈%6'sı, yaklaşık 8.000 lüks. Sert gölge, kara gökyüzü.
HALKA        Görünen ince parlak halka, yıldızın ışığının deliğin çevresinde
             bükülmüş hâlidir — yığılma diski DEĞİL. Bu yüzden incedir,
             sabittir ve renksizdir.
YILDIZ SAATİ 360° / 31,0 saat = 11,61°/saat. Bir klip (2,0 saat) = 23,2°.
```

| S | TUR | pencere | AZİMUT baş→son | YÜKSELTİ baş→son | 1 m gölge | gölge yönü | rejim |
|:-:|:-:|---|---|---|---|---|:-:|
| 0 | 1 | 0:00–2:00 | 108° → 131° | 19° → 41° | 2,87 → 1,16 m | batı-kuzeybatı | B |
| 1 | 1 | 2:00–4:00 | 131° → 154° | 41° → 56° | 1,16 → 0,68 m | kuzeybatı | B |
| 2 | 1 | 4:00–6:00 | 154° → 178° | 56° → 62° | 0,68 → 0,53 m | kuzey-kuzeybatı | B |
| 3 | 1 | 6:00–8:00 | 178° → 201° | 62° → 58° | 0,53 → 0,62 m | kuzey | B |
| 4 | 1 | 8:00–10:00 | 201° → 224° | 58° → 45° | 0,62 → 1,01 m | kuzey-kuzeydoğu | B |
| 5 | 1 | 10:00–12:00 | 224° → 247° | 45° → 24° | 1,01 → 2,25 m | kuzeydoğu | A |
| 6 | 1 | 12:00–13:00 | 247° → 259° | 24° → 12° | 2,25 → 4,70 m | kuzey-kuzeydoğu | B |
| 7 | 1 | 13:00–13:45 | 259° → 267° | 12° → 3° | 4,70 → 19,0 m | doğu-kuzeydoğu | B |

```
KİLİTLER
 · Yıldız yolu modeli: yükselti = 62° × sin(azimut − 90°). Doğuda 90°'de
   doğar, güneyde 180°'de 62° ile tepeye çıkar, batıda 270°'de batar.
 · AZİMUT BANDI 108°–247°, kamera bakışı 000° → YILDIZ HER SAHNEDE
   KAMERANIN ARKASINDA ve hiçbir karede kadrajda DEĞİL [DERS 32].
 · Gölge TEK YÖNDE döner: batı-kuzeybatı → kuzey → doğu. Geri dönmez.
 · ⭐ ÖĞLE S2/S3 SINIRINDADIR (azimut 178°, gölge 0,53 m): günün ortası
   ekranda SAYILABİLİR bir olaydır ve filmin ortasına denk gelir.
 · Gölge boyu günün saatidir: 2,87 → 0,53 → 2,25. Gece 15:30'da başlar;
   film 13:45'te biter — ekranda kalan pay 15 dakikadır ve gölge onu söyler.
 · ⛔ LIGHTING bloğunda "güneş" · "disk" kelimeleri HİÇ geçmez [DERS 39].
   Işık yalnız açı · gölge yönü · gölge oranı · gökyüzü rengiyle anılır.
```

---

# 6. 🎬 SAHNE PROMPTLARI

> ⛔ Her prompt kendi başına çalışır: köşeli parantez atfı yoktur [D-a].
> ⛔ WHEN COMPLETE cümlesi, SITE / BACKGROUND ve NEGATIVE blokları yedi
>   promptta BİREBİR aynıdır (tek kaynaktan üretildi).
> ⭐ STRUCTURE tam-hâl tarifi TEK CÜMLEDİR ve AT THIS STAGE'den KISADIR
>   [DERS 36] — bu depoda oranı 1'in ALTINA inen İLK film budur (§9①).
> ⭐ İnsansız film: her promptta "No people are present." + makinelerin
>   gövdesi POZİTİF kapatılır [DERS 33 · 41]. Makine adlarında elle kullanılan
>   makine adı (dozer · loader · greyder · ekskavatör) HİÇ geçmez.
> ⛔ T2V YEDEĞİ YOK: formatın kendisi öyle diyor [KILAVUZ_REHBERI §2.7 ②].
>   Bir klip düşerse yedek, AYNI İKİ KAREDEN yeniden koşmaktır.

## 🎬 SAHNE 0 — DAİREYİ SÜPÜRÜR

`8,0 sn` · `rejim B — 2 saat · 1200×` · `yerel saat 0:00–2:00` · `kinetik: süpürür`

### 📸 GÖRSEL PROMPT — G0

```
Photorealistic documentary construction photograph — Scene 0 of 8. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: the plain is bare rock and grit. One line of cleated ruts comes in from the right edge and ends in the middle of the frame, where a blade has swept one raw curved strip 8.0 metres long clean down to pale bedrock, marking the first quarter of a circle 26.0 metres across. The swept strip reads bright against the dark weathered crust around it, and the material pushed off it lies in a low spoil ridge along its near side. Eighteen metres to the left the cargo lander stands whole on three legs 4.0 metres tall, its flat deck carrying one plain steel cylinder 4.2 metres across and 12.0 metres long, strapped down under taut slings. An old fissure runs from the swept strip past the foot of the leaning slab toward the camera; its lips are spalled and rubble-filled and it measures 0.35 metres across at the slab, less than half the thickness of the slab itself.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The swept strip has reached the foot of the leaning slab and stopped there, and the morning shadow of the slab is nearly three times its own height.

COMPOSITION: Vertical 9:16. The plain sits at forty percent of frame height and the top of the leaning slab at forty-four percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 108 degrees, elevation 19 degrees, shadows falling to the west-north-west, a 1 metre rod casting a 2.87 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and shortens from nearly three times the slab's height to a little over one.

ACTIVITY: A tracked rover pushes the swept strip forward along the marked arc and tips a load of loose crust onto the spoil ridge, while a cutting rig trims the far end of the same arc, both smeared into a slow blur, and the cleated ruts they leave stay pressed into the grit after they pass. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: loose grey grit, deep cleated ruts, one low spoil ridge of pushed crust, angular offcuts scattered along the swept strip, and a shallow drift of grit banked against the uphill side of the leaning slab.

PHYSICS: The rover rests its full weight on its tracks on firm rock. The spoil ridge holds its natural angle of repose. Grit thrown off the blade flies in a clean parabola and lands at once; nothing stays above the ground.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT — KLİP 0 (G0 → G1)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

A tracked rover pushes the swept strip forward along the marked arc, pass after pass, and the bare bedrock strip lengthens and closes into a full circle 26.0 metres across. A cutting rig trims the circle's edge behind it and drops the trimmed pieces onto the spoil ridge, which grows and slumps and grows again along the near side. Every pass lays another cleated rut across the fresh rock, and the pale swept surface widens against the dark crust until the whole circle is bare. The lander stands untouched throughout, its cylinder still strapped down.

The star stays behind the camera and moves from azimuth 108 degrees to azimuth 131 degrees across the shot, its elevation going from 19 to 41 degrees; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and shortens from nearly three times the slab's height to a little over one.

The camera does not move at any point. The framing is identical in the first and last frame. The leaning slab occupies exactly the same width of the frame at both ends of the shot, the black circle and its bright ring keep their size and position, the scarp on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No course of stone appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 1 — ÇUKURU AÇAR

`8,0 sn` · `rejim B — 2 saat · 1200×` · `yerel saat 2:00–4:00` · `kinetik: açar`

### 📸 GÖRSEL PROMPT — G1

```
Photorealistic documentary construction photograph — Scene 1 of 8. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: a circle 26.0 metres across has been swept clean down to pale bedrock and its whole rim is ringed by a continuous low spoil ridge of pushed crust. In the middle of the circle a cutting rig has opened the outline of a rectangular trench 13.0 metres long and 5.0 metres wide, cut 0.6 metres deep so far, its near end stepped into one shallow bench and its cut faces bright against the swept floor. Six cut slabs, each about a metre wide and 0.8 metres thick, stand stacked on edge beside the north rim of the circle. Eighteen metres to the left the cargo lander stands whole on three legs 4.0 metres tall, its flat deck carrying one plain steel cylinder 4.2 metres across and 12.0 metres long, strapped down under taut slings. The old fissure runs past the foot of the leaning slab toward the camera, 0.35 metres across at the slab.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The swept circle now reaches past the leaning slab on both sides, and the slab's shadow has shortened to a little over its own height.

COMPOSITION: Vertical 9:16. The swept floor sits at thirty-nine percent of frame height and the top of the leaning slab at forty-four percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 131 degrees, elevation 41 degrees, shadows falling to the north-west, a 1 metre rod casting a 1.16 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and shortens from a little over the slab's height to two thirds of it.

ACTIVITY: A cutting rig drops a fresh slab out of the trench face and a tracked rover hauls the loose spoil out to the rim, both drawn into a blur, and the stack of cut slabs beside the north rim grows course by course while new ruts fan out around the trench mouth. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: bare swept bedrock scored with cleated ruts, a continuous spoil ridge around the rim, angular offcuts and rock dust banked along the trench lip, and a growing stack of cut slabs on edge.

PHYSICS: The cutting rig stands with its full weight on the swept floor and its head in contact with the rock it cuts. The stacked slabs lean against one another on their long edges. Cut chips fly in a clean parabola and land at once.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT — KLİP 1 (G1 → G2)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

A cutting rig works its way around the trench outline and the trench deepens step by step from 0.6 metres to a full 1.4 metres, its long walls squaring up and its near end stepping down in two clean benches. A tracked rover hauls every load of spoil out to the rim, and the ridge there thickens with each pass. Slab after slab is drawn out of the trench face and set on edge beside the north rim, and the stack grows from six slabs to about thirty. Beside the lander a manipulator arm unbolts the outer skin panels one after another and lays them flat on the rock, and the lander's frame is left bare with the cylinder still strapped on its deck.

The star stays behind the camera and moves from azimuth 131 degrees to azimuth 154 degrees across the shot, its elevation going from 41 to 56 degrees; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and shortens from a little over the slab's height to two thirds of it.

The camera does not move at any point. The framing is identical in the first and last frame. The leaning slab occupies exactly the same width of the frame at both ends of the shot, the black circle and its bright ring keep their size and position, the scarp on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No course of stone appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 2 — TAŞI KESER

`8,0 sn` · `rejim B — 2 saat · 1200×` · `yerel saat 4:00–6:00` · `kinetik: keser`

### 📸 GÖRSEL PROMPT — G2

```
Photorealistic documentary construction photograph — Scene 2 of 8. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: a trench 13.0 metres long, 5.0 metres wide and 1.4 metres deep is cut into the middle of the swept circle, its long walls square and its near end stepped into two clean benches. About thirty cut slabs, each about a metre wide and 0.8 metres thick, stand stacked on edge along the north rim of the circle, and the spoil ridge outside the rim has thickened. Eight flat skin panels stripped from the lander lie stacked on the rock beside it. The lander itself stands on three legs 4.0 metres tall with its frame bare, still carrying one plain steel cylinder 4.2 metres across and 12.0 metres long strapped to its flat deck under taut slings. The old fissure runs past the foot of the leaning slab toward the camera, 0.35 metres across at the slab.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The stack of cut slabs beside the north rim now stands as long as the trench itself, and the leaning slab's shadow has shrunk to two thirds of its height.

COMPOSITION: Vertical 9:16. The swept floor sits at thirty-nine percent of frame height and the top of the leaning slab at forty-four percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 154 degrees, elevation 56 degrees, shadows falling to the north-north-west, a 1 metre rod casting a 0.68 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and shortens from two thirds of the slab's height to half of it, the shortest of the day.

ACTIVITY: A cutting rig drops a fresh slab out of the trench wall while a tracked rover stacks a cut slab onto the row beside the north rim, both blurred into streaks, and the fresh saw-cut faces stand out pale against the darker weathered rock around them. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: rock dust banked along the trench lip, deep cleated ruts crossing the swept floor, angular offcuts, a thickening spoil ridge outside the rim and a long row of slabs stacked on edge.

PHYSICS: The cylinder rests its full weight on the lander deck under taut slings. The stacked slabs lean on their long edges against one another. Cut chips fly in a clean parabola and land at once; nothing stays above the ground.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT — KLİP 2 (G2 → G3)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

A cutting rig works along the trench walls and the last benches are squared off, while a tracked rover stacks slab after slab onto the row beside the north rim until the row runs the full length of the trench. Beside the lander a cable hoist takes up the slack on its slings until they stand dead straight, lifts the steel cylinder clear of the deck and swings it slowly out over the trench, where it hangs level and still. The shot ends with the cylinder hanging squarely above the open trench on taut vertical slings, its shadow lying short and sharp on the swept floor below it.

The star stays behind the camera and moves from azimuth 154 degrees to azimuth 178 degrees across the shot, its elevation going from 56 to 62 degrees; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and shortens from two thirds of the slab's height to half of it, the shortest of the day.

The camera does not move at any point. The framing is identical in the first and last frame. The leaning slab occupies exactly the same width of the frame at both ends of the shot, the black circle and its bright ring keep their size and position, the scarp on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No course of stone appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 3 — TANKI İNDİRİR

`8,0 sn` · `rejim B — 2 saat · 1200×` · `yerel saat 6:00–8:00` · `kinetik: indirir`

### 📸 GÖRSEL PROMPT — G3

```
Photorealistic documentary construction photograph — Scene 3 of 8. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: the steel cylinder 4.2 metres across and 12.0 metres long hangs level above the open trench on four taut vertical slings from the cable hoist, one metre clear of the trench floor. The trench below it is 13.0 metres long, 5.0 metres wide and 1.4 metres deep, benched at its near end, and two pairs of cut stone chocks are already bedded on its floor. About thirty cut slabs stand stacked on edge along the north rim of the swept circle, and eight flat skin panels lie stacked beside the lander, whose bare frame now stands empty on its three legs. The old fissure runs past the foot of the leaning slab toward the camera, 0.35 metres across at the slab.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The hanging cylinder is exactly as long as the trench is deep multiplied nine times over, and it hangs one metre clear of the floor; the noon shadows are the shortest they will be all day.

COMPOSITION: Vertical 9:16. The swept floor sits at thirty-nine percent of frame height and the crown of the hanging cylinder at forty-six percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 178 degrees, elevation 62 degrees, shadows falling to the north, a 1 metre rod casting a 0.53 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and lengthens again from half the slab's height to two thirds of it.

ACTIVITY: A cable hoist lowers the cylinder into the trench on taut slings while a manipulator arm beds a pair of stone chocks under its flank, both slowed into a blur, and the swept floor around the trench mouth fills with fresh cleated ruts and dropped rock dust. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: rock dust and grit around the trench mouth, cleated ruts across the swept floor, offcuts kicked to the rim, the long stack of slabs on edge and the flat pile of stripped skin panels.

PHYSICS: The slings stay dead straight and vertical while the load hangs, and the load path runs unbroken from the cylinder to the slings to the hoist frame to the ground. Once seated, the cylinder rests its full weight on two pairs of stone chocks bedded on the trench floor.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT — KLİP 3 (G3 → G4)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

The cable hoist lowers the steel cylinder into the trench, slowly and squarely, and the slings stay dead straight until the cylinder is seated on the two pairs of stone chocks on the trench floor. A manipulator arm beds a third pair of chocks under its far flank, the slings go slack and are drawn back up to the hoist frame. A tracked rover then hauls the first cut slabs off the row and a manipulator arm sets them into a level course along the north side of the trench, and the shot ends with one full course of stone laid 18.0 metres along the trench and a base plate bolted flat on the rock east of it, three guy wires lying coiled and loose around it.

The star stays behind the camera and moves from azimuth 178 degrees to azimuth 201 degrees across the shot, its elevation going from 62 to 58 degrees; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and lengthens again from half the slab's height to two thirds of it.

The camera does not move at any point. The framing is identical in the first and last frame. The leaning slab occupies exactly the same width of the frame at both ends of the shot, the black circle and its bright ring keep their size and position, the scarp on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No course of stone appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 4 — DUVARI ÖRER

`8,0 sn` · `rejim B — 2 saat · 1200×` · `yerel saat 8:00–10:00` · `kinetik: örer`

### 📸 GÖRSEL PROMPT — G4

```
Photorealistic documentary construction photograph — Scene 4 of 8. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: the steel cylinder lies seated in the trench on three pairs of stone chocks, its bare crown standing 1.4 metres above the swept floor. Along its north side one course of dry-stacked cut slabs runs 18.0 metres, 0.8 metres thick and level along its top. East of the trench a base plate is bolted flat to the bedrock with three guy wires lying coiled and loose around it. The row of cut slabs along the north rim has been drawn down to about twenty and the stack of eight stripped skin panels still lies flat beside the empty lander frame. The old fissure runs past the foot of the leaning slab toward the camera, 0.35 metres across at the slab.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The first course of stone reaches the same height as the crown of the cylinder behind it, and the afternoon shadows have grown back to the height of the leaning slab.

COMPOSITION: Vertical 9:16. The swept floor sits at thirty-nine percent of frame height and the crown of the first stone course at forty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 201 degrees, elevation 58 degrees, shadows falling to the north-north-east, a 1 metre rod casting a 0.62 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and lengthens from two thirds of the slab's height to the slab's full height.

ACTIVITY: A tracked rover hauls a cut slab off the row and a manipulator arm sets a slab onto the second course and beds it flat with a shove, both smeared into streaks, and the row of stacked slabs along the rim visibly shrinks as the wall grows. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: rock dust ground into the swept floor, crossing cleated ruts, offcuts and chips fallen at the foot of the wall, the shrinking row of slabs on edge and the flat stack of stripped skin panels.

PHYSICS: Each stone course carries its full weight on the course beneath it, stepped back 0.30 metres, and no slab overhangs more than a third of its own width. The cylinder rests on its chocks in continuous contact with the trench floor.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT — KLİP 4 (G4 → G5)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

A tracked rover hauls slab after slab off the row while a manipulator arm sets them into level courses, and the wall along the north side grows from one course to four, each course stepped back a little from the one below until its top stands 3.2 metres above the swept floor. Partway through the shot the ground beats once: a shiver runs across the plain, dust jumps off the crown of the wall and slides down its face in a fan, one stacked slab topples off the end of the row, and the old fissure beside the leaning slab opens visibly wider, from 0.35 to 0.52 metres. The work carries straight on. A manipulator arm then lays the stripped skin panels over the back of the cylinder and a rover spreads swept grit across them, and the shot ends with the wall closed at four courses, the cylinder covered except for its hatch box, three tower sections standing bolted inside a scaffold cradle east of the trench, and the old lander deck lying flat on the rock to the west carrying four flat panels in a row.

The star stays behind the camera and moves from azimuth 201 degrees to azimuth 224 degrees across the shot, its elevation going from 58 to 45 degrees; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadow of the leaning slab sweeps about twenty-three degrees across the plain and lengthens from two thirds of the slab's height to the slab's full height.

The camera does not move at any point. The framing is identical in the first and last frame. The leaning slab occupies exactly the same width of the frame at both ends of the shot, the black circle and its bright ring keep their size and position, the scarp on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No course of stone appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 5 — DİREĞİ DİKER

`8,0 sn` · `rejim A — 10 dk · 100×` · `yerel saat 10:00–12:00` · `kinetik: diker`

### 📸 GÖRSEL PROMPT — G5

```
Photorealistic documentary construction photograph — Scene 5 of 8. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: the wall stands closed at four dry-stacked courses, 3.2 metres high and 18.0 metres long, each course stepped back 0.30 metres from the one below. Behind it the steel cylinder lies buried under the stripped skin panels and a spread of swept grit, with only its raised hatch box and one flat end cap left showing. East of the trench three bolted tower sections stand 9.0 metres high inside a scaffold cradle, their three guy wires connected and still slack. To the west the lander's stripped deck lies flat on the rock as a bearing, carrying four flat panels in a single row with four empty places beside them. The lander's own frame stands empty on its three legs. A fresh fan of dust lies at the foot of the wall and one toppled slab lies at the end of the row; the old fissure at the leaning slab has opened to 0.52 metres.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The crown of the wall now stands level with the top of the leaning slab, and the shadows have grown past the slab's own height as the light falls.

COMPOSITION: Vertical 9:16. The swept floor sits at thirty-nine percent of frame height, the crown of the wall at forty-five percent and the top of the standing tower at fifty-seven percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 224 degrees, elevation 45 degrees, shadows falling to the north-east, a 1 metre rod casting a 1.01 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. Roughly ten minutes pass across this shot: the shadows barely move and only lengthen a little, and the machines run fast but stay recognisable as machines.

ACTIVITY: A manipulator arm clamps the last guy wire to its anchor block while a tracked rover hauls the final capping slab up onto the fourth course and beds it flat, and the row of stacked slabs along the rim is emptied to the last one. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: a fan of fresh dust at the foot of the wall, one toppled slab at the end of the empty row, cleated ruts crossing the swept floor, offcuts and rock dust, and the long shadows of the wall and the tower running across the bare circle.

PHYSICS: The tower carries its weight through a bolted base plate on the bedrock and is held by three straight tensioned wires anchored 9.0 metres out. The panels rest on the old deck in continuous contact with it. The stone courses bear on one another.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT — KLİP 5 (G5 → G6)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

A cable hoist lifts the fourth and fifth tower sections into line one after the other and a manipulator arm bolts them home, and the tower rises from 9.0 metres to 15.0 metres. The hoist then lifts a 2.4 metre parabolic reflector up to the fourth section and the arm bolts it there. The three guy wires are drawn up one by one until all three stand dead straight and taut, and the scaffold cradle is unbolted piece by piece and stacked flat beside the wall. To the west a rover sets the four remaining flat panels into their places on the old deck and the whole row turns together to face the low star. For the last part of the shot nothing more is built: the site holds still, the long shadows creep, and a thin drift of grit slides down the face of the wall.

The star stays behind the camera at azimuth 224 degrees and elevation 45 degrees for the whole shot; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. Roughly ten minutes pass across this shot: the shadows barely move and only lengthen a little, and the machines run fast but stay recognisable as machines.

The camera does not move at any point. The framing is identical in the first and last frame. The leaning slab occupies exactly the same width of the frame at both ends of the shot, the black circle and its bright ring keep their size and position, the scarp on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No course of stone appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 6 — KAPAĞI KAPATIR

`8,0 sn` · `rejim B — 1 saat · 600×` · `yerel saat 12:00–13:00` · `kinetik: kapatır`

### 📸 GÖRSEL PROMPT — G6

```
Photorealistic documentary construction photograph — Scene 6 of 8. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: the station is finished. The wall stands closed at four dry-stacked courses, 3.2 metres high and 18.0 metres long, each course stepped back 0.30 metres and capped level. Behind it the steel cylinder lies buried under panels and swept grit with only its raised hatch box and one flat end cap showing. East of the trench a bolted three-leg tower stands 15.0 metres high in five sections, carrying a 2.4 metre parabolic reflector on its fourth section and held by three straight tensioned wires anchored 9.0 metres out; the cradle that raised it lies unbolted and stacked flat against the wall. To the west eight flat panels stand in a single row on the lander's stripped deck, all of them turned to face the low star. Eighteen metres to the left the lander's three bare legs and its empty ring frame still stand where they landed, stripped down to bare metal. The row of cut slabs along the north rim is empty and the old fissure runs 0.52 metres wide past the leaning slab and on under the eastern anchor block. Every shadow runs long to the north-east.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The tower head stands nearly five times the height of the leaning slab, the crown of the wall is level with the slab's top, and every shadow is more than twice the height of what casts it.

COMPOSITION: Vertical 9:16. The swept floor sits at thirty-nine percent of frame height, the crown of the wall at forty-five percent and the tower head at sixty-four percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 247 degrees, elevation 24 degrees, shadows falling to the north-east, a 1 metre rod casting a 2.25 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. Roughly ten minutes pass across this shot: the shadows barely move and only lengthen a little, and the machines run fast but stay recognisable as machines.

ACTIVITY: A tracked rover hauls the last capping slab up onto the fourth course and beds it flat, a manipulator arm swings its head down to rest against the wall, and the panel row turns a few degrees further to hold the falling star; the emptied slab row and the fan of dust at the foot of the wall stay exactly as the day made them. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: a fan of fresh dust at the foot of the wall, one toppled slab at the end of the empty row, cleated ruts crossing the swept floor, offcuts and rock dust, and long shadows running across the bare circle.

PHYSICS: The tower carries its weight through a bolted base plate on the bedrock and is held by three straight tensioned wires anchored 9.0 metres out. The stone courses bear on one another and the buried cylinder rests on its chocks. Nothing stands above the ground without support.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT — KLİP 6 (G6 → G7)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

A tracked rover pushes the last loads of rock and grit over the buried steel cylinder, sealing the end cap entirely beneath the surface, until only the raised hatch box stands above the rough floor. The manipulator arm reaches down and pulls the hatch cover shut, locking it tight. The machines then start to roll back, pulling away from the closed shelter toward the edge of the swept circle.

The star stays behind the camera and moves from azimuth 247 degrees to azimuth 259 degrees across the shot, its elevation falling from 24 to 12 degrees; its only sign is the shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadows stretch rapidly to more than double their length as the light drops.

The camera does not move at any point. The framing is identical in the first and last frame. The leaning slab occupies exactly the same width of the frame at both ends of the shot, the black circle and its bright ring keep their size and position, the scarp on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No course of stone appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎬 SAHNE 7 — ÜSSÜ MÜHÜRLER

`8,0 sn` · `rejim B — 45 dk · 337×` · `yerel saat 13:00–13:45` · `kinetik: mühürler`

### 📸 GÖRSEL PROMPT — G7

```
Photorealistic documentary construction photograph — Scene 7 of 8. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: the station is sealed. The wall stands closed at four dry-stacked courses, 3.2 metres high and 18.0 metres long, capped level. Behind it the steel cylinder lies completely buried under panels and swept grit with only its closed hatch box showing above the surface; the end cap is gone. East of the trench a bolted three-leg tower stands 15.0 metres high in five sections, carrying a 2.4 metre parabolic reflector and held by three straight tensioned wires; the cradle that raised it lies unbolted and stacked flat against the wall. To the west eight flat panels stand in a single row on the lander's stripped deck, turned to face the setting star. Eighteen metres to the left the lander's three bare legs and its empty ring frame still stand where they landed. The machines have pulled back toward the edges of the swept circle.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The shadows are stretched enormously long; the shadow of the leaning slab reaches almost five times the slab's own height.

COMPOSITION: Vertical 9:16. The swept floor sits at thirty-nine percent of frame height, the crown of the wall at forty-five percent and the tower head at sixty-four percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 259 degrees, elevation 12 degrees, shadows falling to the east-north-east, a 1 metre rod casting a 4.70 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadows stretch extremely fast and the machines run fast but stay recognisable as machines.

ACTIVITY: A tracked rover pulls a loose slab out of the pit and a manipulator arm reverses toward the rim of the swept circle and power down, their tracks leaving deep ruts in the grit. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: a fan of fresh dust at the foot of the wall, one toppled slab at the end of the empty row, deep cleated ruts crossing the swept floor, and very long shadows running across the bare circle.

PHYSICS: The tower carries its weight through a bolted base plate on the bedrock and is held by three straight tensioned wires anchored 9.0 metres out. The stone courses bear on one another and the buried cylinder rests on its chocks. Nothing stands above the ground without support.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT — KLİP 7 (G7 → G8)

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

The machines withdraw completely to the edges of the swept circle, stop moving, and power down. The panel array turns the last few degrees to hold the setting star. For the rest of the shot, nothing moves except the shadows: as the star drops toward the horizon, the shadows stretch endlessly across the plain, covering the station and sliding out of the frame. The hatch remains sealed tight, and the empty legs of the lander stand dead in the long shadows.

The star stays behind the camera and moves from azimuth 259 degrees to azimuth 267 degrees across the shot, its elevation dropping from 12 degrees to just 3 degrees above the horizon; its only sign is the massive shadows on the ground. Everything in this frame is time-lapsed at the same rate: the shadows, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadows stretch extremely fast to nineteen times the height of the objects.

The camera does not move at any point. The framing is identical in the first and last frame. The leaning slab occupies exactly the same width of the frame at both ends of the shot, the black circle and its bright ring keep their size and position, the scarp on the horizon stays where it is, and the horizon stays at exactly half the frame height throughout. Nothing already built is removed, moved or resized. No course of stone appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 🎯 USTA KARE — G8 · SAHNE DEĞİLDİR

`klip 7'nin HEDEF karesi` · `yerel saat 13:45` · `üretim sırasında EN ÖNCE üretilir`

> ⛔ Bu blok bir sahne değildir: G8, klip 7'nin son karesidir ve prompt kapısı onu
> saymaz (sekiz sahne · sekiz görsel · sekiz I2V). Ama üretimde İLK üretilen kare budur
> [KILAVUZ_REHBERI §8 adım 2] ve zincir buradan geriye iner.

### 🖼️ USTA KARE PROMPTU (G8)

```
Photorealistic documentary construction photograph — Scene 8 of 8. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: the station is finished and sealed. The wall stands closed at four dry-stacked courses, 3.2 metres high and 18.0 metres long, capped level. Behind it the steel cylinder lies completely buried under panels and swept grit with only its closed hatch box showing above the surface. East of the trench a bolted three-leg tower stands 15.0 metres high in five sections, carrying a 2.4 metre parabolic reflector and held by three straight tensioned wires anchored 9.0 metres out; the cradle that raised it lies unbolted and stacked flat against the wall. To the west eight flat panels stand in a single row on the lander's stripped deck, turned to face the setting star. Eighteen metres to the left the lander's three bare legs and its empty ring frame still stand where they landed, stripped down to bare metal. The old fissure runs 0.52 metres wide past the leaning slab and on under the eastern anchor block. Every shadow stretches massively off the frame to the east-north-east.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The star is nearly setting and the shadows are virtually infinite; the shadow of the leaning slab extends nineteen times its own height, stretching far off the right side of the frame.

COMPOSITION: Vertical 9:16. The swept floor sits at thirty-nine percent of frame height, the crown of the wall at forty-five percent and the tower head at sixty-four percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 267 degrees, elevation 3 degrees, shadows falling to the east-north-east, a 1 metre rod casting a 19.0 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. About two hours pass across this shot: the shadows stretch extremely fast and the machines run fast but stay recognisable as machines.

ACTIVITY: The machines have withdrawn to the far edges of the swept circle and powered down. The panel array is angled steeply to catch the dying light. Nothing moves; the station is locked in absolute stillness as night begins to fall. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: a fan of dust at the foot of the wall, one toppled slab at the end of the empty row, deep cleated ruts crossing the swept floor, and endless shadows burying the bare circle.

PHYSICS: The tower carries its weight through a bolted base plate on the bedrock and is held by three straight tensioned wires anchored 9.0 metres out. The stone courses bear on one another and the buried cylinder rests on its chocks. Nothing stands above the ground without support.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.

Output: 9:16, 4K, no text, no watermark.
```


## 🏁 BİTİŞ VİDEOSU (KLİP 8)

### 🎥 VİDEO PROMPTU

```
The scene begins exactly as the provided image. There is no target image; the action plays out freely from the first frame to the end of the shot.

The star finally sets below the horizon and the last light leaves the plain. The massive shadows swallow the entire site and disappear as the scene goes pitch black, leaving only the razor-thin bright ring of the black hole glowing in the dark sky. The sealed station stands in absolute stillness against the vacuum of the night.

The camera does not move at any point. The framing is identical to the provided image. The leaning slab, the black circle and its bright ring keep their position and size in the sky. Nothing already built is removed or moved.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```


---


# 7. 🎵 MÜZİK VE KAPAK

```
BPM        120 · ölçü 2,0 sn · her sahne TAM 4 ÖLÇÜ · sahne bloğu 24 ölçü
           kapak kartı 2,5 ölçü (5,0 sn) · toplam 53,0 sn
           ⭐ Düz ızgaranın tek bedava kazancı budur: altı kesme de ölçünün
             1. vuruşunun ÜSTÜNE düşer (0,0 · 8,0 · 16,0 · 24,0 · 32,0 · 40,0)
             ve kaydırma birikmez [A2-e].
           ⛔ Klip süresi ffprobe'la 8,004 gibi ölçülürse ızgara O SAYIDAN
             türer ve her kesme tek tek hizalanır [D-d].

KATMAN = KURS — dört katman, hiçbiri çıkmaz
  S0-S1  ① kuru nabız · her ölçünün 1. vuruşu, taş üstünde metal            1
  S2-S3  ② alçak sürekli dron + 15,5 saatlik VURUŞUN sesteki karşılığı:
            8 ölçüde bir gelen tek alçak darbe (gelgit)                      2
  S4     ③ istifleme perküsyonu — slab kursunun ritmi ⭐ VURUŞ SAHNESİ       3
  S5     ④ geniş sıcak akor yastığı, altında dron durur — ışık düşerken      4
  KART   hepsi çözülür ve söner; son 1,5 saniye yalnız ortam sesi

ZORUNLU  söz yok · melodi hattı yok · şarkı yapısı yok
         müziksiz pencere 0,0-1,5 sn — kanca diegetik sesle açılır
         ⚠️ AMA BU FİLMDE DİEGETİK SES YOKTUR: havasız yüzeyde ses taşınmaz.
            ⭐ Karşılığı YAPISALDIR ve filmin lehinedir: 0,0-1,5 sn TAM
              SESSİZLİKTİR, sonra ses YAPININ İÇİNDEN gelir (temas sesi:
              kaya üstünde palet, çelik üstünde çelik). Ses tasarımı bunu
              böyle beyan eder; "uzayda ses" hatası kanalın en kolay
              yakalanan yalanıdır.
         TELEFON HOPARLÖRÜ KURALI: "Every sub-bass element below 150 Hz is
         doubled by its own upper harmonics at roughly 100, 150 and 200 Hz so
         the fundamental is implied rather than required."
```

### 🎼 MÜZİK PROMPTU

```
Instrumental score for a 53-second vertical construction time-lapse: a
48-second scene block of six 8-second shots, followed by a 5-second end card.
No lyrics, no voice, no melody line, no traditional song structure.

Genre: slow industrial minimalism, dry and mechanical, no strings swell.
Tempo: 120 BPM, strict and bar-aligned, four bars per 8-second shot.

Layers (one added every one or two shots, none removed until the final bars):
1. [shots 1-2] a dry pulse on the first beat of every bar, metal struck on stone
2. [shots 3-4] a low continuous drone plus one deep pulse every eight bars
3. [shot 5]    stacking percussion, the rhythm of stone courses being laid
4. [shot 6]    one wide warm chord pad over the drone as the light falls

Dynamic map across 53 seconds:
  0.0-1.5    complete silence — this world has no air and carries no sound
  1.5-16.0   layer 1 alone
  16.0-32.0  layer 2 enters
  32.0-40.0  layer 3 enters — the densest and hardest moment
  40.0-48.0  layer 4 enters, the stack sits together and begins to open
  48.0-53.0  end card: everything resolves and decays; the last 1.5 seconds
             carry only the contact bed
Phone-speaker rule: every sub-bass element below 150 Hz is doubled by its own
upper harmonics at roughly 100, 150 and 200 Hz so the fundamental is implied
rather than required; the low end is never the only carrier of the weight.
```

```
KAPAK — ⛔ G8'İN KARESİNDEN TÜRER [DERS 30]
  görüntü   G8'in son karesi: mühürlenmiş istasyon, dikilmiş direk, sonsuz gölgeler,
            arkada kara halka. İniş aracının boş çerçevesi solda görünür.
  metin     BEFORE NIGHTFALL — ⛔ İNGİLİZCE · İKİ SATIR (BEFORE / NIGHTFALL)
            ⭐ punto · konum · renk · ölçüm: BEFORE_NIGHTFALL_KAPAK.md §3-§4
              — sayı iki yerde durmaz [değişmez ①]
  kart      teslimin SON 5,0 saniyesi · hareketsiz · zoom/kayma YOK
  ⛔ KAPAK KANITI: ffmpeg -ss <G8 karesi> -i teslim.mp4 -frames:v 1 s5.jpg
     bash araclar/zincir_kontrol.sh s5.jpg kapak.png → çıkış 2 = TESLİM YOK
  ⛔ 120 PX TESTİ: hem kapağa hem S0'ın 0. karesine (sips -Z 120).
     Testin sorusu: 120 px'te kara halkanın yayı ve direğin silueti
     BİRBİRİNDEN ayırt ediliyor mu?
```

---

# 8. 📦 PAKETLEME

```
⛔ Başlık, açıklama, hashtag ve sabit yorum İNGİLİZCEDİR.

BAŞLIK        Before Nightfall — one day to close the shelter      (46 krk)
              (alternatif ≤40: "Before Nightfall: one day to close")
AÇIKLAMA      A robotic relay station is built on a planet locked to a black
              hole, in the twelve hours of daylight it has. The hole never
              moves in the sky; the star crosses it in thirty-one hours; the
              night that follows would kill anything not buried, walled and
              tied down. The lander that brought the station is taken apart
              into it — its tank becomes the shelter, its skin becomes the
              cover, its deck becomes the panel bed. What is left standing at
              dusk is three legs and an empty frame.
              Fixed camera, no cuts inside the shots, one continuous day.
              ⛔ GERÇEKLİK BEYANI (aynen): This film is generated with AI. It
              does not document a real project, company, mission or place.
HASHTAG       #timelapse #construction #blackhole #spacebase #vertical
              #scifi #worldbuilding #ai
SABİT YORUM   The day here lasts thirty-one hours and is also the year: the
              planet is tidally locked to the hole it circles. Everything you
              see has to be finished before the star sets. Made with AI.
⛔ AI BEYANI ÜÇ PLATFORMDA DA ELLE İŞARETLENİR [değişmez ⑫]:
   YouTube Studio → Altered content · TikTok → AIGC · Instagram → AI içerik.
   Açıklamadaki beyan bunun YERİNE GEÇMEZ.
⛔ GERÇEK FİRMA / MİSYON / AJANS ADI KULLANILMAZ [§9.8]. Bu istasyon hiçbir
   gerçek programın kopyası değildir.
```

---

# 9. ⛔ ÜRETİMDEN ÖNCE KAPANMASI GEREKENLER

```
① ⛔ ARAÇ KAPISI — YEDİ ÖLÇÜM [ARAC_KARTLARI §4]
   Ve bu filmde ilk ölçüm bir VAR/YOK sorusudur: kutu seti {4,6,8} çıkarsa
   8,0 sn tek klipte teslim EDİLEMEZ (tavan 7,00 sn) ve ya uzatma ya iki klip
   dikişi gerekir. Bu, ızgaranın kendisini yeniden açar.
   ⭐ VE BU ARAÇTA SEKİZİNCİ BİR SORU VAR: araç İKİ KAREYLE (ilk + son)
     çalışıyor mu? Çalışmıyorsa §2'nin yöntemi bu araçta YÜRÜMEZ ve plan
     tek kareli I2V'ye düşer — o zaman dikiş garantisi kaybolur ve ⑤ riski
     geri gelir. Bu soru üretim günlüğünün ilk satırıdır.

② ⛔ ÜRETİM GÜNLÜĞÜ [DERS 28]
   dikey_shorts/BEFORE_NIGHTFALL/BEFORE_NIGHTFALL_URETIM_GUNLUGU.md
   (şablon: dikey_shorts/URETIM_GUNLUGU_SABLONU.md). Günlüksüz filme QA
   paketi açılmaz (qa_paket.sh durur).

③ ⚠️ prompt_kontrol.py'nin BU PLANDA VERECEĞİ ÇIKTI — üçü de biliniyor:
   ⛔ BLOCK ×1  "bütün sahne süreleri aynı (8,0)" → §1.2, sahibinin kilidi.
      Üretim kapısını proje sahibi ELLE açar; kapı yanılmıyor, kilit bilinçli.
   ⚠️ FIX ×1   "ARAÇ KUTU SETİ ÖLÇÜLMEDİ" → madde ①.
   ⚠️ FIX ×7   "metin yasağı KAPSAMSIZ — 0 yüzey sayılmış" → ⭐ BU FIX
      ⭐ 08.09.2026: altıydı, YEDİ oldu — kapı artık USTA KAREYİ de denetliyor
        (zincirli formatta o da bir görsel promptudur, §2.7). Altı sahne + G6.
      BİLEREK KABUL EDİLDİ VE BİR ÇELİŞKİYİ İŞARET EDİYOR:
      prompt_kontrol §9, metin yasağının içinde en az 8 NESNE ADI sayar;
      DERS 35 ise (ölçülmüş) yasağın içindeki nesne adının EKRANA GELDİĞİNİ
      söyler ve adı ANMAYAN bir yasak yazdırır. İkisi aynı anda sağlanamaz.
      Ölçülmüş ders (DERS 35) ölçülmemiş ödülü (§9) yener [kart S §3].
      ⇒ Prompt DERS 35'in onaylı cümlesini birebir taşır; §9 FIX'i durur.
      ⭐ Kapıya not: §9'un, DERS 35 biçimi kullanıldığında SUSMASI gerekir.

④ ⛔ ZİNCİR — bu depoda BEŞ filmde de koşulmadı [AGENTS §6]
   Bu filmde zincir yalnız bir tavsiye değil, formatın kendisidir (§2).
   Yedi karenin altı geçişinde de zincir_kontrol.sh + EĞİK TAŞ elle.

⑤ ⚠️ ÜÇ ŞEY BU DEPODA HİÇ ÖLÇÜLMEDİ, ÜÇÜ DE BU FİLMDE İLK KEZ KOŞUYOR
   (a) DERS 36'nın oran kapısı: tam hâl / ara hâl oranı 1'in ALTINDA olan
       ilk film. Altı filmde oran 1,08–2,58 idi ve altısında da ② hükmü
       DIFFERENT · APPEARING geldi. Bu filmin ② hükmü dersi ya kanıtlar ya
       düşürür — karşı örnek ilk kez üretiliyor.
   (b) İki keyframe kilidi (§2). Kamera kilidinin GEOMETRİ kanalından
       geçtiği ilk film [A3-d].
   (c) DERS 44'ün tersi: kusursuz dikişte düz ızgara ⑥'yı düşürür mü (§1.2c).

⑥ ⚠️ BU FİLMİN KENDİ AÇIKLARI — üretimden önce bilinen
   (a) KORPUS İDDİASI ÖLÇÜLMEDİ [DERS 34]: "1970s Apollo surface photograph
       … chest-mounted 70mm film camera" gerçek bir külliyattır (Hasselblad
       yüzey kareleri) ama bu depoda ölçülmedi. ① SURFACE TRUTH'tan okunur.
   (b) KARA HALKA BİR RİSKTİR: adı prompta girmiyor (DERS 42) ama geometrisi
       tarif edilirken model yine de turuncu bir yığılma diski üretebilir.
       ⛔ Ölçüm: G6 usta karesinde halka İNCE ve RENKSİZ değilse kare atılır
       ve prompt "one razor-thin bright ring" cümlesiyle daraltılır.
   (c) HAVASIZ FİZİK ÖLÇÜLMEDİ: "toz parabol çizip düşer, havada kalmaz"
       cümlesi beş promptta da var; modelin toz bulutu üretip üretmediği
       ① ve ⑦'den okunacak.
   (d) SAHA KARTI YOK: SAHA_VE_IKLIM_KARTLARI'nda havasız kayaç ova kartı
       yoktur. Bu filmin saha bilgisi §3 ve §5'te durur; ilk üretimden sonra
       kart yazılır ya da yazılmaz — ölçüm karar verir.
   (e) SÜREKLİ ZAMAN BİR SAPMADIR (§1.3①). ③ merceğinin "TIME READ FROM THE
       FILM ALONE" satırı bu filmde "bir gün · sabahtan ikindiye" demelidir.
       ⭐ Plan bunu MERTEBE olarak beyan eder [P1-c]: bir günün ışığı.
       Rapor "aylar" derse film kendi süresini anlatamamış demektir.
   (f) ⭐ DİKEY YÜZDELERDE ±1 PUANLIK KAYMA — 08.09.2026 ÖLÇÜLDÜ, DÜZELTİLMEDİ
       §3'ün kendi formülü (%50 + 66,67 × (y − 6,0) / D) üç satırı tutmuyor:
            süpürülmüş taban   plan %39,0  →  formül %40,0   (y=0,0 · D=40)
            duvar tacı         plan %44,8  →  formül %45,3   (y=3,2 · D=40)
            direk tacı         plan %64,0  →  formül %65,0   (y=15,0 · D=40)
       Tutanlar: eğik taş %44,1 ✅ · dairenin yakın kenarı %35,2 ✅ — ikisi de
       h = 6,0 m ile çıkıyor. ⭐ Kayan üçü h = 6,6 m ile tam kapanıyor (39,0 ve
       64,0 birebir): planda İKİ kamera yüksekliği karışmış. Promptlarda ve
       istasyon satırında beyan edilen h 6,0 m'dir.
       ⛔ BU DERS 38'İN TAM SINIFI: COMPOSITION bloğu modele "the tower head at
          sixty-four percent" diyor; beyan edilen istasyon %65,0 üretir. DUST
          YEAR'da aynı cins sapma 11,3 puandı ve ① STATION IDENTITY 0/10 aldı.
          Burada 1,0 puan — küçük, ama kaynağı aynı.
       KARAR PROJE SAHİBİNİN:
          (a) h = 6,0 kalır → üç yüzde ve İKİ İngilizce cümle düzelir
              ("thirty-nine" → "forty" · "sixty-four" → "sixty-five")
          (b) h = 6,6 m olur → yedi promptun kamera satırı değişir
       ⛔ Üretimden önce biri seçilir; ikisi birden duramaz [değişmez ①].
   (g) ⭐ KAPAK BAŞLIĞI GÜVENLİ ALANA %8 BÜYÜK HARFLE SIĞMIYOR — ölçüldü.
       "NIGHTFALL" 9 harftir. Makinedeki EN DAR kesimde (DIN Condensed Bold)
       düz tepeli harfin 154 px olduğu punto 216'dır ve orada satır 719 px
       tutar; güvenli genişlik 716 px'tir (1080 − 122 − 242).
       Karar: punto 214 → satır 714 px ✅ · düz tepeli harf 153 px (%7,97) ·
       kelimenin mürekkep kutusu 155 px (%8,07). Deponun kendi ölçüm yordamı
       (kelimeyi TRIM et) 155 px okur ve %8 tabanından GEÇER; sapma yalnız
       düz tepeli okumada ve 1 px'tir. Ölçüm komutu, yerleşim ve iki sapmanın
       gerekçesi BEFORE_NIGHTFALL_KAPAK.md §3-§4'te durur.
       ⭐ Bu, konsept kapısı ③'ün (başlık şeması) SAYMADIĞI bir sınırdır:
          kapı KELİME sayar, HARF saymaz. 154 px'te sığan en uzun kelime 8 harf.
```

---

# 10. 📁 DOSYALAR

```
dikey_shorts/BEFORE_NIGHTFALL/
├── BEFORE_NIGHTFALL_DIKEY_TIMELAPSE.md   ⭐ bu dosya (plan + 13 prompt)
├── BEFORE_NIGHTFALL_QA_SPEC.md           kilit listesi + FİNAL KARE KANITI
├── BEFORE_NIGHTFALL_KAPAK.md             ⭐ kaynak kare + kapak promptu +
│                                            başlığın dizilişi (sayıyla)
└── BEFORE_NIGHTFALL_URETIM_GUNLUGU.md    ⛔ AÇILMADI — üretim günü açılır

KOMUTLAR
   python3 araclar/prompt_kontrol.py dikey_shorts/BEFORE_NIGHTFALL/BEFORE_NIGHTFALL_DIKEY_TIMELAPSE.md
   bash araclar/zincir_kontrol.sh <onceki_kare> <yeni_kare>     ⛔ her karede
   bash araclar/kesme_kontrol.sh teslim.mp4 <plan>              ⛔ yayından önce
   bash araclar/qa_paket.sh dikey_shorts/BEFORE_NIGHTFALL teslim.mp4 kapak.png
```
