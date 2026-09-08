# 🔍 BEFORE NIGHTFALL — QA SPEC

> ⛔ **BU SPEC ÜRETİMDEN ÖNCE YAZILDI.** Buradaki her kilit, plandaki yedi
> görsel ve altı I2V promptunun içinde İngilizce olarak YAZILIDIR. Ölçülmemiş
> olanlar §8'de açıkça AÇIK durur.
>
> ⭐ VE BELGE YETMEZ [DERS 27 · 29]: her mercek koşusundan ÖNCE tek satır
> yazılır ve raporun başına yapıştırılır: `verilen girdiler: <dosya adları>`.
> Koşu `araclar/qa_paket.sh` ile PAKETLENİR.

---

## 0. KÜNYE

```
FİLM          BEFORE NIGHTFALL
FORMAT        9:16 dikey · 6 sahne × 8,0 sn = 48,0 sn  ⛔ DÜZ IZGARA
              (proje sahibinin kilidi · plan §1.2 · prompt kapısı BLOCK verir)
KAPAK KARTI   5,0 sn · SAHNE DEĞİL · teslimin SON 5 sn'si · G6'dan türer
              ⭐ kaynak kare · kapak promptu · başlığın dizilişi (sayıyla)
                ve dört test: BEFORE_NIGHTFALL_KAPAK.md
TOPLAM        53,0 sn
FORMAT (2)    ⭐ İKİ KEYFRAME ZİNCİRİ — 7 görsel · 6 klip · her klip iki
              onaylı kareyle kilitli. Dikişin iki yakası AYNI KARE.
              foto–video–foto · deponun formatı [KILAVUZ_REHBERI §2.7]
              ⭐ BU FORMATI İLK KOŞAN FİLM BUDUR (plan §2 · kare tablosu)
YAPI          robotik röle istasyonu: Ø26,0 m süpürülmüş daire + 13,0×5,0×1,4 m
              çukur + yatık silindir Ø4,2×12,0 m + 4 kurs × 0,80 m (3,2 m) kuru
              örgü taş duvar (18,0 m) + 5×3,0 m gergili direk (taç 15,0 m) +
              Ø2,4 m çanak (4. bölüm) + tek sırada 8 panel (12,8 m)
SAHA          havasız gri kayaç ova · kara deliğe gelgit kilitli · SAHA KARTI YOK
ZAMAN YAYI    ⭐ TEK GÜN · yerel 12,0 saat (yıldız azimut 108° → 247°)
              ⛔ MEVSİM YOK, GÜN VAR. Zamanın taşıyıcısı GÖLGE BOYUDUR.
KAMERA        tek istasyon — ANA (altı sahnenin altısı) · detay istasyonu YOK
              h 6,0 m · D_eksen 40,0 m · D_kenar 27,0 m · bearing 000° ·
              tilt 0° · roll 0° · kadraj 33,75 × 60,0 m · 32,0 px/m
ÜRETİM SIRASI ⛔ TERS: G6 usta kare → G5 → G4 → G3 → G2 → G1 → G0
              her kareden sonra zincir_kontrol.sh + EĞİK TAŞ elle
KAPI          python3 araclar/prompt_kontrol.py → ⛔ BLOCK ×1 (süre eşitliği ·
              BİLİNÇLİ) + ⚠️ FIX ×8 (7'si DERS 35 çelişkisi · 1'i kutu seti)
              ⭐ yedinci FIX usta karenindir: kapı artık G6'yı da denetliyor
⛔ ARAÇ KAPISI KOŞULMADI. Kutu seti bilinmiyor; {4,6,8} çıkarsa 8,0 sn'lik
   HİÇBİR sahne tek klipte teslim edilemez (tavan 7,00 sn) [ARAC_KARTLARI §2].
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S5 (sahne bloğu 40,0–48,0)
SANİYE      0:47,6   (S5 klibinin son 0,4 saniyesi)

GÖRÜLMESİ GEREKEN ŞEY — YEDİSİNİN YEDİSİ birden:
   ① TAM DİREK: BEŞ bölüm sayılabiliyor, taç kadrajın %64'ünde, ÜÇ gergi teli
      DÜMDÜZ ve gergin, Ø2,4 m çanak DÖRDÜNCÜ bölümde. İSKELE KAFESİ YOK —
      sökülmüş ve duvarın dibine düz istiflenmiş olarak görünüyor.
   ② KAPALI DUVAR: DÖRT kurs sayılabiliyor, tacı 3,2 m'de ve EĞİK TAŞIN
      TEPESİYLE aynı hizada, her kurs bir öncekinden 0,30 m geride, boydan
      boya 18,0 m, üstü kapak taşıyla düz. Duvarda açıklık YOK.
   ③ GÖMÜLÜ SIĞINAK: silindirin yalnız kare kapak kutusu ve BİR düz uç kapağı
      görünüyor; gövdenin kalanı panel + serilmiş grit altında.
   ④ SEKİZ PANEL tek sırada, iniş aracının sökülmüş güvertesi üstünde, hepsi
      AYNI yöne — alçalan yıldıza — dönük.
   ⑤ ⭐ BEDEL ①: iniş aracının ÜÇ BACAĞI ve BOŞ HALKA ÇERÇEVESİ hâlâ solda,
      18 m'de, ayakta. ⛔ Sökülmüş, temizlenmiş ya da kadraj dışına alınmış
      OLMAMALI. Tank, dış panel ve güverte üstünde DEĞİL.
   ⑥ ⭐ BEDEL ②: fay çatlağı eğik taşın dibinde 0,52 m — taşın kalınlığının
      (0,8 m) yaklaşık üçte ikisi — ve doğu ankraj bloğunun ALTINDAN geçiyor.
      Yanında: BOŞALMIŞ slab dizisi + duvarın dibinde toz yelpazesi + devrilmiş
      tek slab. ⛔ Üçü de S4'teki vuruşun izidir; silinmiş olamazlar.
   ⑦ IŞIK: gölgeler kuzeydoğuya, 1 m çubuk → 2,25 m gölge (yükselti 24°).
      ⛔ Yıldız kadrajda GÖRÜNMEZ. Kara halka her zamanki yerinde: merkezi
         ufuk çizgisinde, tepesi kare yüksekliğinin %78,7'sinde, tek ince
         parlak halka — turuncu/kalın/girdaplı bir disk DEĞİL.

KOMUT
   ffmpeg -y -sseof -5.4 -i teslim.mp4 -frames:v 1 kanit.jpg
   ⭐ Kare TESLİM dosyasından alınır, üretilen klipten DEĞİL [KURGU_VE_TESLIM §2].
⛔ Yedisinden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
```

---

## 2. KADRAJ KİLİTLERİ — ANA istasyon (altı sahnenin altısı)

```
ufuk                 %50,0 — YEDİ karede de
süpürülmüş taban     %39,0   ·  dairenin yakın kenarı (D 27 m) %35,2
tank tacı            %42,0   ·  duvar tacı (3,2 m) %44,8
eğik taşın tepesi    %44,1   ·  fay sarpı %49,3
çanak merkezi        %59,0   ·  direk tacı %64,0
kara halka           merkez %50,0 · tepe %78,7 · genişlik kadrajın %102'si
                     ⭐ İKİ KENARDAN DA TAŞAR — görünen şey bir YAY
                     r_px = 1280·tan(23,284°) = 551 px [08.09 düzeltildi]
kadraj               33,75 m geniş × 60,0 m yüksek · 32,0 px/m
                     genişlik = 36×(9/16)×D/f = 0,84375 × 40,0

⭐ YÜZDELER D_eksen = 40,0 m'DEN HESAPLANDI, saha kenarından değil [DERS 38].
   Formül: %50 + 66,67 × (y − 6,0) / D    [KAMERA_ISTASYONU §3, f=24]
⭐ ALT ÇEYREK EŞİĞİ: D_alt = 24 × 6,0 / 9 = 16,0 m. En yakın saha nesnesi
   27,0 m'de → hiçbir iş kadrajın alt %25'ine düşmez. (DUST YEAR bu sınırın
   6,2 m ötesindeydi ve ① SAFE AREA 0/10 aldı.)
⚠️ TAÇ %82 HEDEFİ TUTMADI VE SEBEBİ PLANDA YAZILI (§3): 26,0 m'lik daire
   18,75 m'lik kadraja sığmıyor; geniş sahada kadrajı GENİŞLİK kurar.

⭐ OKUNABİLİRLİK EŞİĞİ 0,5 m = 16 px [INSAAT_YONTEMI §1]
   Kontrol: promptlarda 0,5 m'den küçük hiçbir nesne adı GEÇMEMELİ.

KAMERA KİLİDİ ÖLÇÜLEBİLİR YAZILDI [DERS 6]:
   "The leaning slab occupies exactly the same width of the frame at both ends
    of the shot ... the horizon stays at exactly half the frame height."
   ⛔ Ölçüm: ilk ve son karede eğik taşın piksel genişliği. Fark > 2 px ise
      kamera kilidi DÜŞTÜ ve klip atılır [ARAC_KARTLARI §4 ölçüm 2].
   ⭐ BU FİLMDE İKİNCİ BİR KİLİT VAR: son kare zaten hedef görseldir. Klibin
      son karesi ile hedef görsel arasında zincir_kontrol.sh koşar; çıkış 2
      ise araç iki kareli modu taşımıyor demektir (plan §9①).
```

---

## 3. DEĞİŞMEZLİK KİLİTLERİ — kareler arası

```
ARKA PLAN ÇAPALARI — üçü de YEDİ karede aynı yerde, aynı boyutta:
   ① KARA HALKA · merkezi tam ufukta · çapı kadraj genişliğinin %102'si —
      iki kenardan da TAŞAR, görünen şey bir YAY · tepesi %78,7 ·
      içi düz siyah · çevresi TEK İNCE parlak halka
      ⛔ RENK VE KALINLIK KİLİDİ: halka ince ve renksizdir. Turuncu, girdaplı
         ya da kalın bir disk çıkarsa kare ATILIR — o, deliğin adının korpusudur
         ve prompt onu ADLANDIRMIYOR [DERS 42].
   ② EĞİK TAŞ · 3,0 m · 0,8 m kalınlık · 12° kuzeye eğik · 96 px
   ③ FAY SARPI · ufku boydan boya kesen düz basamak · tepesi 4,0 m · %49,3

⭐ ⑤ "AYNI YER" NESNESİ: EĞİK TAŞ.
   ⛔ ÜRETİM KAPISI [DERS 25]: her zincir_kontrol koşusunda iki karede de
      AYNI YERDE ve AYNI 12° EĞİMDE olduğu ELLE doğrulanır. Kaybolduysa ya
      eğimi değiştiyse kare ATILIR — betik geçse bile.
   ⭐ İKİNCİ NESNE (zaman): FAY ÇATLAĞI. G0–G4'te 0,35 m, G5–G6'da 0,52 m.
      Genişlik taşın KALINLIĞINA göre okunur: önce yarısından az, sonra
      üçte ikisi. ⛔ Çatlak hiçbir karede DARALAMAZ.

WHEN COMPLETE cümlesi · SITE / BACKGROUND · NEGATIVE — yedi promptta BİREBİR
aynı (tek kaynaktan üretildi; prompt_kontrol denetliyor).

MONOTON BÜYÜME — geri alınan tek şey GEÇİCİ EKİPMANDIR ve §6'da takvimlidir:
   ⛔ süpürülmüş daire küçülemez · çukur dolamaz · duvar kurs kaybedemez ·
      direk bölüm kaybedemez · panel sayısı azalamaz · çatlak kapanamaz
```

---

## 4. YILDIZ SAATİ KİLİDİ — tek gün · 12,0 yerel saat

```
Yıldız gökyüzünde 11,61°/saat ilerler (gün = yıl = 31,0 yerel saat).
Yol modeli: yükselti = 62° × sin(azimut − 90°). Doğuş 90°, tepe 180°, batış 270°.

G0 108°/19°  G1 131°/41°  G2 154°/56°  G3 178°/62°  G4 201°/58°
G5 224°/45°  G6 247°/24°

1 m çubuk gölgesi: 2,87 → 1,16 → 0,68 → 0,53 → 0,62 → 1,01 → 2,25 m
gölge yönü:        BKB → KB → KKB → K → KKD → KD → KD

KİLİTLER
 · Azimut bandı 108°–247°, kamera bakışı 000°, kadraj 337,1°–022,9°.
   ⇒ YILDIZ HİÇBİR KAREDE KADRAJDA DEĞİL [DERS 32].
   ⛔ Ölçüm: yedi karede de parlak nokta aranır; bulunursa kare ATILIR.
 · LIGHTING bloğunda "güneş" ve "disk" kelimeleri HİÇ geçmiyor [DERS 39].
 · Gölge TEK YÖNDE döner ve GERİ DÖNMEZ: BKB → K → KD.
 · ⭐ ÖĞLE S2/S3 SINIRINDA (azimut 178°, gölge 0,53 m — günün en kısası).
   Filmin ortası, günün ortasıdır ve bu ekranda sayılabilir.
 · ⭐ FİLMİN SÜRESİ GÖLGEDEN OKUNMALI: ③ merceğinin "TIME READ FROM THE FILM
   ALONE" satırı "bir gün · sabahtan ikindiye" demeli. "Aylar" ya da "bir yıl"
   derse film kendi süresini anlatamamış demektir [DERS 14].
 · ⛔ IŞIK SÜREKLİDİR VE KESMEDE ATLAMAZ (plan §1.3①): G(n) hem klibin sonu
   hem sonraki klibin başıdır. Kesmede ışık sıçraması GÖRÜLÜRSE dikiş
   bozulmuş demektir.
```

---

## 5. SIKIŞTIRMA REJİMİ KİLİDİ

```
S0 B · S1 B · S2 B · S3 B · S4 B · S5 A          — iki rejim (üst sınır)

REJİM B (2 saat · ~900×)  beş sahne — gölge 23° süpürür ve boyu belirgin
                          değişir, makineler bulanık iz hâlinde
REJİM A (10 dk · ~75×)    S5 — makineler MAKİNE olarak tanınır, gölge kıpırdamaz
                          ⭐ Sebep P2-i: usta kare klibinin son ≥2,0 sn'si bir
                            TUTUŞTUR. Rejim B'de bu tutuş, beyan edilen gölge
                            süpürmesiyle çelişirdi.
⛔ Bir klipte gök, gölge, toz ve makine AYNI SAATE tabidir. Ölçüm: gölge
   süpürürken makine gerçek zamanda yürüyorsa ③ TIME RATE düşer, klip atılır.
⛔ REJİM C YOK: bu filmde gölgesiz sahne yoktur, dolayısıyla DERS 40 kapısı
   açılmaz.
⚠️ HAVASIZ FİZİK KİLİDİ: atılan grit PARABOL çizip düşer; havada toz bulutu,
   pus ya da duman KALMAZ. Beş promptta da yazılı; ① ve ⑦'den okunacak.
```

---

## 6. ARA HÂL VE SÖKÜM TAKVİMİ

```
⑧ YÖNTEM MERCEĞİ HER ELEMANI TEK TEK İZLER. Hiçbiri tamamlanmış doğmamalıdır.

eleman            ara hâl (hangi karede)         geçici ekipman / kanıt
──────────────────────────────────────────────────────────────────────────
① süpürülmüş daire %25 G0 (8,0 m yay) · %100 G1   bıçak izi · spoil sırtı
② çukur            %25 G2 (0,6 m) · %100 G3       basamak · kesme yüzü
③ slab stoğu       6 adet G2 · ~30 G3 · 0 G6      ⭐ EKSİLEN İSTİF = iş kanıtı
④ sığınak          %50 G3 (kancada asılı/oturmuş) taş takoz · gergin sapan
                   %75 G5 (örtülü) · %100 G6      panel örtüsü + serilmiş grit
⑤ siper duvarı     %25 G4 (1 kurs) · %100 G5      kurs kademesi 0,30 m
⑥ direk            %25 G4 (taban plakası + kıvrık gergi telleri)
                   %60 G5 (3 bölüm, iskele kafesi içinde) · %100 G6
⑦ çanak            G5'te yok → G6'da 4. bölümde   kablo kancasıyla kaldırılır
⑧ panel dizisi     %50 G5 (4/8 panel) · %100 G6   sökülmüş güverte = tabla

⛔ ÜÇ ELEMAN ARA HÂLİNİ YALNIZ KLİBİN İÇİNDE GÖSTERİR (kareler arasında değil):
   duvarın 2. ve 3. kursu (klip 4) · direğin 4. ve 5. bölümü (klip 5) ·
   çanağın havada asılı hâli (klip 5). ⑧ merceği bunları VİDEODA arar;
   görünmezlerse "APPEARED" hükmü gelir ve o klip yeniden üretilir.

SÖKÜM TAKVİMİ — hiçbiri kendiliğinden kaybolmaz, her biri I2V'de FİİL alır
   iniş aracı dış paneli   klip 1'de sökülür → klip 4'te tankın örtüsü olur
   kablo kancası + sapan   klip 2'de gerilir → klip 3'te boşalır, yukarı çekilir
   iniş aracı güvertesi    klip 4'te sökülür → panel dizisinin tablası olur
   direk iskele kafesi     klip 4'te kurulur → klip 5'te sökülüp duvar dibine
                           düz istiflenir
   ⛔ SÖKÜLMEYENLER — bunlar BEDEL'dir, kaybolurlarsa film yalan söyler:
      iniş aracının üç bacağı + boş halka çerçevesi   G0 → G6'da hâlâ ayakta
      fay çatlağı                                     0,35 → 0,52 m, açık
      spoil sırtı ve kesme yüzü                       daire kenarında kalır
      devrilmiş slab + toz yelpazesi (vuruşun izi)    G5 → G6
```

---

## 7. ⛔ ZİNCİR KAPISI — yedi kare, altı geçiş

```
ÜRETİM SIRASI (ters):  G6 → G5 → G4 → G3 → G2 → G1 → G0
Her adımda:
   bash araclar/zincir_kontrol.sh <onceki_onayli> <yeni>     → çıkış 2 = ATıLIR
   + EĞİK TAŞ elle: aynı yerde mi, aynı 12° eğimde mi        → değilse ATıLIR
   + üretim notu tek satır: "G6'dan ne KALDIRILDI / ne EKLENDİ" [P2-a]

⭐ USTA KARE KAPISI: G6 ikna etmiyorsa DİĞER ALTI KARE ÜRETİLMEZ.
   Üç şey bu sırayla okunmalı [P1-h]: (1) kapanmış duvar ve dikilmiş direk,
   (2) uzayan gölgeler — günün bittiği, (3) solda boş iniş aracı çerçevesi.

KLİP KAPISI (I2V, altı kez):
   klip n'in SON karesi ile G(n+1) arasında zincir_kontrol.sh
   ⛔ çıkış 2 = araç iki kareli modu taşımıyor → yöntem düşer, plan §9① açılır
```

---

## 8. ⛔ BU SPEC'İN KENDİ AÇIKLARI — üretimden önce bilinen

```
① ARAÇ KUTU SETİ ÖLÇÜLMEDİ. Altı sahnenin altısı 8,0 sn. {4,6,8} çıkarsa
   HİÇBİRİ tek klipte teslim edilemez (tavan 7,00 sn) → uzatma ya da iki klip
   dikişi zorunlu olur ve üretim günlüğüne yazılır.
② İKİ KAREYLE ÇALIŞAN ARAÇ ŞART. Araç yalnız tek kare (ilk kare) alıyorsa
   plan §2'nin dikiş garantisi düşer ve ⑤ riski geri gelir.
③ DÜZ IZGARA BLOCK'U BİLİNÇLİDİR (plan §1.2). ⑥ METRONOM hükmü gelebilir;
   risk kabul edildi. ⭐ Ama önce ⑤ okunur [DERS 44]: ⑤ hükmü "SAME WORLD"
   ise ⑥'nın gerekçesi ızgaraya yazılamaz.
④ KARA HALKA ÖLÇÜLMEDİ. Prompt adı anmıyor, geometriyi tarif ediyor [DERS 42];
   modelin yine de yığılma diski üretip üretmediği G6'da görülecek.
⑤ APOLLO KORPUSU İDDİA EDİLDİ, ÖLÇÜLMEDİ [DERS 34]. "1970s Apollo surface
   photograph … chest-mounted 70mm film camera" gerçek bir külliyattır ama bu
   depoda ölçülmedi. ① SURFACE TRUTH'tan okunacak ilk şey budur.
⑥ SÜREKLİ ZAMAN BİR SAPMADIR (plan §1.3①). Kesme artık ay atlamıyor. ⑥
   merceği bunu "sahneler arası fark yok" diye okuyabilir; ④ ise "vaat
   ilerliyor mu" diye. İkisi de plandan cevaplanır, promptla değil.
⑦ DERS 36'NIN ORAN KAPISI İLK KEZ 1'İN ALTINDA. Tam hâl 97 karakter, ara hâl
   700-900 karakter (oran ≈ 0,12). Altı filmde oran 1,08–2,58 idi ve altısında
   da ② hükmü DIFFERENT · APPEARING geldi. Bu filmin ② hükmü DERS 36'yı ya
   kanıtlar ya düşürür.
⑧ HAVASIZ KAYAÇ OVA SAHA KARTI YOK. Saha bilgisi planın §3 ve §5'inde durur.
⑨ prompt_kontrol §9 ile DERS 35 ÇELİŞİYOR (plan §9③). Altı FIX bilerek
   kabul edildi; ölçülmüş ders ölçülmemiş ödülü yener.
```

---

## 9. KOŞULACAK MERCEKLER

```
⛔ HEPSİ qa_paket.sh ile koşar; üretim günlüğü yoksa paket AÇILMAZ [DERS 28].
⛔ Her koşunun başına: "verilen girdiler: <dosya adları>" [DERS 27].
⛔ bash araclar/kare_al.sh teslim.mp4 10  → ① ve ⑤'ten ÖNCE koşulur.

① KARE        mod V   ⭐ SURFACE TRUTH (Apollo korpusu) ve PEOPLE burada
                      okunur. Film insansız beyanlıdır: PEOPLE 0 bir KUSUR
                      DEĞİL, beyanın teyididir.
③ ZAMAN       mod V   TAM KURGU · ⭐ "bir gün · sabahtan ikindiye" bekleniyor
⑤ DEVAMLILIK  mod V   ⭐ "aynı yer" nesnesi: EĞİK TAŞ · dikişler kare eşlemeli
⑦ İŞ          mod V   ⭐ eksilen slab istifi + izler + vuruşun bıraktıkları
② İNŞA        mod D   SPEC §3 · §6 verilir
④ TESLİM      mod D   plan §0 (VAAT/DİRENÇ/BEDEL) verilir
⑥ GEÇİŞ       mod D   plan §4 SÜRE sütunu + kesme_kontrol.sh çıktısı
⑧ YÖNTEM      mod D   SPEC §6 ara hâl tablosu — sekiz eleman tek tek

⭐ SIRA: doküman körlüğü isteyen dördü (① ③ ⑤ ⑦) ÖNCE koşulur.
⛔ ASGARİ SET: ① + ② + ⑤. Bu üçü koşulmadan film YAYINLANMAZ.
```
