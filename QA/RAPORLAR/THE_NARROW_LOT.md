# 📋 THE NARROW LOT — QA KAYDI

```
KÜNYE      5 klip · 0:29,9 · sahne bloğu 5 klip · ⛔ KAPAK KARTI YOK
           ızgara: 5 × 6,0 (BES_SAHNE_GPT_BRIEFI'nin ilk koşusu)
           üretim: harici GPT (Restoration Timelapse) → OpenArt
           altı mercek koşuldu (6/6)
KARAR      ⚠️ YAYINLANMAZ — ama YENİDEN ÜRETİLMEZ, YENİDEN YAZILIR.
           Kök sebep bu sefer ÜRETİM SIRASI değil, PROMPT MİMARİSİDİR.
```

---

## 1. ALTI HÜKÜM

| Mercek | Skor | HÜKÜM |
|---|---:|---|
| ① KARE | 6,0/10 Ⓥ | ✅ **TIMELAPSE** |
| ② İNŞA | 2,6/10 Ⓥ | ⛔ **DIFFERENT** · ⛔ **APPEARING** |
| ③ ZAMAN | 4,2/10 | ✅ **PASSES** · zaman tahmini TUTTU |
| ④ TESLİM | 4,4/10 Ⓥ | ⚠️ ENDS — ama **NONE FOUND** |
| ⑤ DEVAMLILIK | 5,6/10 Ⓥ | ✅ **SAME WORLD** · kanıt nesnesi BULUNDU |
| ⑥ GEÇİŞ | 8,2/10 Ⓥ | ✅ **TIME** · ⛔ **METRONOM** |

```
DEPO GEÇMİŞİ    ①     ②     ③     ④     ⑤     ⑥
LONG SHADOW v1  3,3   0,4   4,3   2,7    —     —
CLOSING SPAN    1,0   0,0   1,3   5,4   0,0   1,6
NARROW LOT      6,0   2,6   4,2   4,4   5,6   8,2   ← altı merceğin beşi en iyi
```

---

## 2. ⭐ DÖRT HÜKÜM İLK KEZ GEÇTİ — deponun ilk gerçek ilerlemesi

Bu depoda iki film üretildi ve ikisinde de **hiçbir** hüküm geçmedi. Bu filmde
dördü birden geçti:

```
① IS THIS A TIME-LAPSE?              ✅ TIME-LAPSE
   (v1: ALTI AYRI GÖRÜNTÜ · CLOSING SPAN: AYRI AYRI GÖRÜNTÜLER)
   "framing, camera station, and background anchors are perfectly matched
    across all five clips" · VANTAGE GROUPS = 1 (CLOSING SPAN'de 8'di)

⑤ IS IT THE SAME WORLD?              ✅ SAME WORLD
⑤ THE OBJECT THAT PROVES IT:         ✅ "Coiled hose, 0:05.1 ve 0:18.0"
   (ikisinde de NONE FOUND'du — bu satır deponun en ağır satırıydı)

⑥ DOES THE CUT MEAN TIME OR NEXT?    ✅ TIME
   ANCHOR SURVIVAL 10/10 · JUMP LEGIBILITY 10/10 · DIRECTION 10/10

③ DOES TIME PASS?                    ✅ PASSES  (v1: yön kırık · CS: yanlış yönde)
③ TIME READ FROM THE FILM ALONE:     "about one year"
   ⭐ PLANLANAN ~12 AY. Deponun ilk kez KENDİ SÜRESİNİ ANLATABİLEN filmi.
      (CLOSING SPAN: plan 34 ay, okuma "yaklaşık bir yıl")
```

⭐ **Bu dördü aynı sebepten geçti:** brief'in **birebir tekrarlanmasını
zorunlu kıldığı cümleler harici bot tarafından birebir taşındı.** Ölçüldü:

| Brief'in dayattığı ifade | 5 promptun kaçında | Karşılığı |
|---|:---:|---|
| `The scene begins exactly as the provided image.` | **5/5** | ① FRAME IDENTITY 10 |
| `does not move at any point` | **5/5** | ① CAMERA LOCK 10 |
| `identical in the first frame and in the last frame` | **5/5** | ① CAMERA LOCK 10 |
| `occupies exactly the same width of the frame` | **5/5** | ① ANCHOR IDENTITY 10 |
| çapa bloğu **SAYIYLA** (6 kat · 3 baca · 5 pencere) | **5/5** | ⑤ SAME WORLD |

---

## 3. ⛔ KÖK SEBEP — ilk kez ÜRETİM SIRASI DEĞİL

İki filmde de kök sebep "ters inşa koşulmadı" idi. Burada zincir fiilen tuttu
(① 10/10 · ⑤ SAME WORLD · tek vantaj). Düşen şey başka:

### ⭐ TEK CÜMLEYLE: **hareketle ilgili her kural YANLIŞ PROMPTTAYDI.**

```
                              GÖRSEL promptta   I2V promptta    QA sonucu
TIME RATE bloğu                    5/5              0/5      ③ TIME RATE   0/10
                                                             ③ CLOUD/SKY   0/10
                                                             ③ SUN DIR.    0/10
insan kuralı ("none of them sharp") 0/5             3/5*     ① PEOPLE      0/10
kanca kararı (a) yüklü kanca        4/5              2/5     ① C1 CRANE    2/10
                                                             ② LOAD PATH   2/10
*yalnız zayıf hâli ("soft motion streaks") geçti; "none of them sharp,
 none of them facing the camera, no readable face anywhere" hiç yazılmadı.
```

⛔ **Görsel prompt TEK KAREYİ yönetir; hareketi I2V yönetir.** Bir hız
kuralını görsel prompta yazmak, onu hiç yazmamaktır: durağan bir görüntüye
"her şey aynı hızda hızlandırılmıştır" demenin karşılığı yoktur.

Bunun ölçülmüş sonucu, deponun gördüğü **en garip tek bulgu**:

```
③ 0:00.0 - 0:29.9
"people and machinery move at a highly accelerated time-lapse rate, while
 environmental time (sun, shadows, clouds) runs at a rate of zero"
```

⭐ Bu, DERS 15'in **TAM TERSİDİR.** CLOSING SPAN'de model gökyüzünü
hızlandırıp yeri gerçek zamanda bırakmıştı. Burada yeri hızlandırdı, gökyüzünü
DONDURDU. İki vaka birlikte tek kuralı veriyor: **modelin hız dağıtımı
rastgeledir ve hangi promptta yazıldığına bakar** [DERS 18].

---

## 4. ⛔ İKİNCİ KÖK SEBEP — sayısız bible bir bible değildir

② STRUCTURE IDENTITY **2/10** — ve sebebi aynı filmin içinde kanıtlı:

```
ARKA PLAN ÇAPALARI  sayıyla yazıldı:
   "six-storey ... exactly three rooftop chimneys"
   "four-storey ... exactly five evenly spaced upper-floor windows"
   → ① ANCHOR IDENTITY 10/10 · ⑤ SAME WORLD ✅

YAPI BIBLE          sayısız yazıldı:
   "narrow rectangular residential tower ... regular structural bays"
   ⛔ oturum ölçüsü YOK · aks sayısı YOK ("24 by 18" 0/5 · "6 by 4" 0/5)
   → ② STRUCTURE IDENTITY 2/10 ⛔
   ② 0:11.8 "Clip 3 occupies almost the entire width of the site …
              by Clip 5 the finished building has a drastically narrower
              footprint, rendering it a completely different structure"
```

Ve negatif çekirdek bu boşluğu **gizledi**: beş promptun beşinde de
`the column grid, the bay spacing, the floor height and the footprint stay
exactly as described` yazıyordu. ⭐ **"as described" bir İŞARETÇİDİR.**
Tarif sayısızsa işaretçi hiçbir şeyi göstermez ve cümle geçerli görünürken
boştur [DERS 19].

---

## 5. ⛔ ÜÇÜNCÜ SEBEP — etiketlenmiş bloklar nesre çevrildi

Harici bot brief'in `§C ÇIKTI İSKELETİ` sözleşmesini uygulamadı: blok
etiketlerini kaldırıp tek bir `SCENE LOCK` / `STAGE` / `DETAILS` düzenine
sıkıştırdı. İki sonucu birden ölçüldü:

```
KAPI KÖRLEŞTİ    araclar/prompt_kontrol.py → ⛔ BLOCK, 25 madde
                 'Camera:' satırı yok (0/5) · 'STRUCTURE:'/'AT THIS STAGE'
                 yok (0/5) · 'SITE / BACKGROUND:' yok (0/5)
                 → BİREBİR TEKRAR denetimi hiç KOŞULAMADI. Kapı, ②'nin
                   düştüğü şeyi tam olarak denetleyecek olan kapıydı.

DÜŞEN BLOK       COMPOSITION bloğu tamamen kayboldu (0/5).
                 "top eighth" 0/5 · "bottom quarter" 0/5 · "right eighth" 0/5
                 Yerine tek nesir cümlesi kondu: "the composition leaves the
                 main structural evidence inside the safe central frame".
                 → ① SAFE AREA 4/10, iki bulgunun ikisi de alt %25'te.
```

⭐ **Kapının okuyamadığı bir doküman, ölçülemeyen bir dokümandır.** Bu filmde
kapı koşuldu ve BLOCK verdi — ama üretimden SONRA. Koşulmayan kapı, kapı
değildir [DERS 12'nin metin tarafı] [DERS 20].

---

## 6. ⛔ RİTİM — METRONOM ikinci kez, ve bu sefer 5 kesmede

```
KESME ARALIKLARI  6,0 · 6,0 · 6,0 · 6,0   (⑥ CUT INTERVALS)
⑥ RHYTHM AND PATTERN            4/10
⑥ VERDICT                        METRONOM
"rigidly spaced 6.0-second intervals … establishing a mechanical metronome
 rhythm rather than an intentional narrative arc or release"
```

⭐ **BES_SAHNE_GPT_BRIEFI §1.2 bunu ÖNCEDEN yazmıştı** ve birincil ızgara
proje sahibinin kilidi olduğu için 5 × 6,0 olarak sipariş edildi. Uyarı tuttu.
Ritim varyantı (`6,0 · 4,0 · 6,0 · 4,0 · 10,0 = 30,0`) artık **seçenek değil,
varsayılan** olur — çünkü METRONOM hükmü iki filmde iki kez ölçüldü.

⚠️ Proje sahibinin okuması: *"daha hızlı bir inşaat olmalı."* ⑥ ve ③ birlikte
bunun İKİ ayrı sebebi olduğunu söylüyor:
```
(a) KESME VARYANSI yok   → ⑥ METRONOM        → çözüm PLANDA (süre sütunu)
(b) DÜNYA DURUYOR        → ③ TIME RATE 0/10  → çözüm I2V PROMPTUNDA
    Gölge, bulut ve güneş hiç kıpırdamıyor; hızlı olan yalnız işçiler.
    Film "yavaş" görünmüyor, ZAMANSIZ görünüyor.
```

---

## 7. ⛔ "HER ŞEYİN NASIL YAPILDIĞI GÖRÜNSÜN" — ② APPEARING

Proje sahibinin ikinci notu ölçümle birebir örtüşüyor: `② IS IT BEING BUILT?
APPEARING`. Sebep tek bir sahne aralığında:

```
② 0:18.0  "The sequence jumps from a bare concrete frame in Clip 4 directly
           to a fully finished, cladded, glazed, and landscaped tower in
           Clip 5, skipping all enclosure, finishing, and site-clearing"
```

S3 promptu cepheyi yazmıştı — ama **"one continuous controlled vertical
facade band"** kadar az yazmıştı ve o bant ekranda okunmadı. 5 sahnelik
ızgarada S3→S4 sıçraması filmin en tehlikeli yeridir: karkastan bitmiş binaya
tek kesmede geçilir. ⛔ v2'de S3 görselinde **cephe kulenin en az yarısını
kaplar**; "bir bant" bir aşama değildir.

Ayrıca yöntem cümleleri (kova döngüsü, kalıp döngüsü) I2V'de İYİ yazılmıştı —
ama geometri eridiği için (② GEOMETRIC STABILITY 2/10) yöntem okunmadı.

---

## 8. ⑤'İN DİKİŞ DENETİMİ — 4/4 dikişte DEFECT, ama YENİ bir tür

CLOSING SPAN'de dikişler "dünya yeniden kuruluyor" diye düşüyordu. Burada tam
tersi düştü: **dünya hiç değişmiyor.**

```
⑤ 0:11.2 → 0:12.0  "mud ruts and puddles … maintain that exact identical
                    fluid geometry despite the addition of snow and months"
⑤ 0:18.0 → 0:19.0  beyaz kamyonet kar altında ve kar eridikten sonra
                    TAM AYNI yerde park hâlinde
⑤ WEAR AND ACCUMULATION  2/10 — şantiye hiç yıpranmıyor
```

⭐ Yani birebir tekrar SAHAYI kurtardı ama **zamanı öldürdü.** Değişmez blok
"filmin ömrü boyunca değişmeyen" içindir; ÇAMUR, İZ, BİRİKİNTİ ve İSTİF
değişmez değildir — onlar `SITE TEXTURE`'dır ve **her sahnede FARKLI
yazılmalıdır.** Bu, DERS 1'in henüz yazılmamış ikinci yarısıdır.

Ve iki gerçek devamlılık hatası:
```
⑤ 0:11.2 → 0:12.0  vinç, kaidesi hiç hazırlanmadan aniden var
                    → SÖKÜM SATIRI'nın karşılığı olan KURULUM SATIRI eksik
⑤ 0:23.2 → 0:24.0  sağdaki tuğla bloğun tek katlı eki YOK OLUYOR
                    → çapa "altı katlı + üç baca" diye sayılmıştı; EK sayılmamıştı
                      Sayılmayan parça, korunmayan parçadır.
```

---

## 9. ⚠️ MOD DENETİMİ — beş mercek eksik girdiyle koştu

```
① KARE        kare grabları VERİLMEDİ    → RUN INCOMPLETE · Ⓥ
② İNŞA        QA_SPEC VERİLMEDİ           → mod V · skor tabloya YAZILMAZ [DERS 17]
③ ZAMAN       ✅ TAM KOŞTU — tek geçerli koşu
④ TESLİM      plan + kapak VERİLMEDİ      → mod V · skor tabloya YAZILMAZ
⑤ DEVAMLILIK  kare grabları VERİLMEDİ    → RUN INCOMPLETE · Ⓥ
⑥ GEÇİŞ       plan + SES VERİLMEDİ        → mod V · skor tabloya YAZILMAZ
              MUSIC ALIGNMENT ve END-CARD HAND-OVER hiç ölçülemedi
```

⭐ Dikkat: **tam koşan tek mercek ③'tür ve hükmü GEÇTİ.** Yani bu filmin en
güvenilir tek ölçümü olumludur — ve aynı ölçüm TIME RATE'e 0/10 vermiştir.

⛔ `araclar/kare_al.sh` koşulmadı. ① ve ⑤'in en zor sorusu bir MODELE değil
bir SAYIYA sorulacaktı; sorulmadı.

---

## 10. ①/③/⑤'İN "QUESTIONS FOR THE DOCUMENT" CEVAPLARI

```
①-1  Ufuk %50,0. Promptta yazılıydı ve TUTTU (ölçülen sapma %0).
①-2  ANA istasyon: 24 mm · yerden 24,0 m · yapının güneybatı yüzünden 72 m ·
     bakış 035° · tilt 0° · roll 0°. Beş sahnede de aynıydı ve aynı ölçüldü.
①-3  ⛔ FOTOĞRAFİK KAYIT. Mimari görselleştirme DEĞİL. Negatif çekirdek bunu
     dört ayrı cümleyle yasaklıyordu ve ① SURFACE TRUTH yine 2/10 geldi —
     yani yasak bu modelde TUTMUYOR. Çözüm yasakta değil, SITE TEXTURE'ın
     sahne sahne DEĞİŞMESİNDE (§8).

③-1  S0 azimut 236° / yükseklik 61° · S1 225°/42° · S2 202°/18° ·
     S3 214°/22° · S4 236°/61°. Beşi de promptta dereceyle YAZILIYDI.
     ⛔ Ve model hiçbirini uygulamadı: ③ bütün kliplerde ~45° ölçtü.
     Sebep: sayılar GÖRSEL promptta kaldı, I2V'ye hiç girmedi [DERS 18].
③-2  Yaz → sonbahar → kış① → kış② → yaz. Tek yönlü. Rapor bu sırayı
     birebir okudu (SEASON ORDER 10/10).
③-3  Klip içi geçen zaman: her klipte BİR GÜN. Promptta "one accelerated
     working day passes" olarak yazılıydı; ekranda hiç görünmedi.

⑤-1  ⛔ HAYIR. Tuğla bloğun tek katlı eki planlı bir yıkım DEĞİLDİ. Çapa
     tarifi "altı katlı + üç baca" diyordu; ek hiç sayılmamıştı. Bu bir
     PLAN eksiğidir, model hatası değil.
⑤-2  ⛔ HAYIR. Vinç kaidesi hiçbir sahnede hazırlanmadı. Kurulum sahnesi
     plana yazılmamıştı — SÖKÜM yazılıydı, KURULUM yazılmamıştı.
⑤-3  ⛔ HAYIR. Beyaz kamyonet plana hiç girmedi; birebir tekrar onu
     yanlışlıkla değişmez yaptı.
```

---

## 11. KARAR

```
⚠️ YAYINLANMAZ. Ama bu film ARŞİVLİK BİR BAŞARISIZLIK DEĞİL, bir DÖNÜM
   NOKTASIDIR: deponun üç filminde ilk kez kadraj, dünya ve kesme TUTTU.
   Düşen şey artık ÜRETİM SIRASI değil, PROMPT MİMARİSİDİR — ve prompt
   mimarisi metinle düzeltilebilir, yeniden çekimle değil.

v2 İÇİN ZORUNLU:
  ① ⭐ HAREKET KURALLARI I2V'YE TAŞINIR [DERS 18]
       TIME RATE · insan kuralı · kanca kararı · kar davranışı · güneş
       satırı: hepsi I2V'de de TAM METİN tekrarlanır.
  ② ⭐ YAPI BIBLE SAYILANIR [DERS 19]
       oturum (m × m) · aks sayısı (n × n) · aks aralığı (m) · kat yüksekliği
       Sayısı olmayan satır bible'a yazılmaz.
  ③ ⭐ BLOK ETİKETLERİ SÖZLEŞMEDİR [DERS 20]
       Camera: · STRUCTURE:/AT THIS STAGE: · SITE / BACKGROUND: · COMPOSITION:
       Kapı ÜRETİMDEN ÖNCE koşulur; BLOCK varsa bota geri gönderilir.
  ④ ⭐ MEVSİM DEĞİŞİMİ GİDEN KLİPTE HAZIRLANIR [DERS 21]
       S1'in son saniyelerinde İLK KAR · S3'ün son saniyelerinde İLK ERİME.
  ⑤ ⭐ KANCA (a) ŞIKKI KALDIRILDI [DERS 22]
       Vinçli her sahnede bom KADRAJ DIŞI. Yüklü kanca ikinci kez düştü.
  ⑥ RİTİM VARYANTI VARSAYILAN OLUR — 6,0 · 4,0 · 6,0 · 4,0 · 10,0 = 30,0
  ⑦ SITE TEXTURE HER SAHNEDE FARKLI YAZILIR — çamur ve iz BİRİKİR (§8)
  ⑧ S3'TE CEPHE KULENİN EN AZ YARISINI KAPLAR — "bir bant" aşama değildir (§7)
  ⑨ KAPAK KARTI ÜRETİLİR — S4 usta karesinden, İngilizce başlıkla
  ⑩ QA öncesi kare_al.sh KOŞULUR ve ② ④ ⑥'ya BELGE VERİLİR
```

## 12. BU FİLMDEN ÇIKAN DERSLER

`kilavuzlar/DERSLER.md` → **DERS 18 · 19 · 20 · 21 · 22**
