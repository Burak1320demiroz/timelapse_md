# 🗒️ BACK TO WATER — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · (19.09.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md` · Plan: `BACK_TO_WATER_DIKEY_TIMELAPSE.md`
> Format: 7 sahne = 8 kare (G0…G7) + 7 I2V · her sahne tek 8,0 sn klip.
> Izgara: ⛔ DÜZ 7 × 8,0 = 56,0 sn — proje sahibinin kesin kuralı; ⑥ METRONOM beyanlı risk.
> ⭐ S0 REJİM A · S6 REJİM G (gerçek zaman 1×, depoda üçüncü koşu) · ⭐ AŞAĞI BAKIŞ + UFUK istasyonu.

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32]

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne 8,0
   ⛔ tavan < 8,0 ise bu araçta üretilmez; karar sahibine döner:   KARAR ____
② KAMERA        ilk/son kare kayması: ____ px    (KAMERA_ISTASYONU §7 eşiğini aşıyorsa ÜRETİLMEZ;
                eşik zincir_kontrol.sh çıktısının "3 nirengi" satırında)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
   ⭐ üç nirengi bu filmde: batı kapı kulesi (%12,4) · doğu kapı kulesi (%59,0) · sarı merdiven (%70,7)
   ⭐ dördüncü ölçüm: UFUK y %79,8 ve eğimi 0° — kıyı çapası, eğilirse istasyon kaymıştır
③ GÖLGE         ilk/son kare açı farkı: ____°    (rejim B test klibinde 0° ise ÜRETİLMEZ)
                bu filmde gölge ölçüsü: doğu/batı duvar gölgesinin taban/su üstündeki KENARI (m)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5
⑤ PROMPT TAVANI ____ karakter · son nesne göründü mü: __/5  (plan promptları 5.916–5.997 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol: ____

⭐ ⑨ SAYIM TESTİ [DERS 55]
   Test promptuna plandaki sayım cümlesi birebir konur. Beş klipte:
   kaç tekne / kaç havuz / ufukta kaç gemi: __/__/__/__/__      hedef: hepsinde 1 / 1 / 0 (G0 promptu)
   G7 test karesinde BOŞ havuza hayalet tekne kondu mu: __
   "dry dock" korpusu tersane (çoklu havuz · rıhtım vinçleri) doğurdu mu: __
   ⛔ Herhangi bir klipte 2+ tekne ya da ikinci havuz çıkarsa ARAÇ DEĞİŞİR, plan düşürülmez.
   KARAR         ____

⑩ ÇÖZÜNÜRLÜK    bu filmde UYGULANMAZ — kurgu hareketi yok, kırpma yok [plan §KURGU]

⑪ AŞAĞI BAKIŞ + UFUK TESTİ (bu filme özel · KAMERA_ISTASYONU "AVLU / AŞAĞI BAKIŞ" üçüncü koşu)
   G0 test karesinde havuz TABANI, takozlar ve teknenin iskele bordası görünüyor mu: __
   kapı ÜSTÜNDEN deniz görünüyor mu (kapı üstü %68 · ufuk %80 — arada 12 puan deniz): __
   gök üst %20'de mi, ufuk yatay mı: __ · keystone sekiz karede aynı mı: __
   — taban ya da deniz görünmüyorsa h/D/tilt yeniden hesaplanır, plan §DEĞİŞMEZLER güncellenir
⑫ SAPAN TESTİ (bu filme özel · SPEC §4)
   S2 test klibinde levha SAPANLA mı indi, süzüldü mü: __ · açıklığa oturdu mu: __
   kesik parçalar + torbalar kamyon KASASINA gitti mi (bedel gitti mi): __
   — sapansız iniyorsa DERS 8 / F08 tetiklenmiştir; araç sorgulanır
⑬ SU TESTİ (bu filme özel · SPEC §5)
   S5 test klibinde su MENFEZDEN mi geldi, "yoktan" mı yükseldi: __
   merdiven basamakları SIRAYLA mı battı, tek hamlede mi doldu (F05): __
   tekne kırmızı örtülünce mi KALKTI, erken mi yükseldi: __ · takozdan ayrılış görüldü mü: __
⑭ KAPI TESTİ (bu filme özel · SPEC §5 ④)
   keson DOĞU kulesine mi kaydı (yukarı kalkmadı, menteşeyle açılmadı): __
   G6 test karesinde iç/dış su TEK yüzey mi (basamak, şelale yok): __

⭐ ⑮ GERÇEK HIZ GEÇİŞ TESTİ — rejim G'nin bu filmdeki kapısı (SPEC §7)
   "moves at natural speed ... the boat drives itself ... through the open gate" test klibinde:
   tekne NET mi (iz yok): __ · gölge sabit mi: __ · deniz dalgalı mı (ipek değil): __
   0/4/8 sn'de boy ve cam sayısı: __/__/__
   baş eşiği ____ sn · kıç eşiği ____ sn (plan ≈ 2,0 / 7,0) · 8 sn'de kıç eşiğin ötesinde mi: __
   iz kapıdan İÇERİ döndü mü, havuz suyu çalkalandı mı: __
   — biri düşerse rejim G bu araçta yok; S6 için karar sahibine döner (ikinci kabul: SPEC §1)

KARAR           bu araçla üretilir / üretilmez — sebep
```

## 0b. ÖN GÖRSELLEŞTİRME — usta kareden ÖNCE [plan §DEĞİŞMEZLER · sahip düzeltmesi ⑤]

```
PLAN + YAN KESİT  istasyon (+12,0 m · batı rıhtımı başı · x −6 · bearing 20° · tilt −22°) · havuz
                  (d 0–26 · x ±6 · −6 m) · tekne (d 9–23 · 14 m · takozda omurga +1,2) · delikler
                  (d 12 y 2,4 · d 18 y 3,0) · kabin (d 15–19 · çatı 7,5) · merdiven (x +6 · d 20) ·
                  babalar (x ±6,5 · d 22/24) · kapı (d 26 · üstü +8) · rampa (baş duvarı · sol alt) ·
                  kamyon (doğu rıhtımı · d 22) · S5 su +5,0 · S6 yolu (d 9 → 27 · kapı arası)
ÇİZİLDİ Mİ        evet/hayır · dosya: ____
⭐ KANIT KUTUSU    delikler · boya sınırı · merdiven · kapı · G7 tekne kutunun (x %11–78 · y %25–87) içinde mi: __
⭐ TEKNE BÜYÜK MÜ  G0'da güverte hattı %33–56 (451 px), iskele bordası okunuyor mu: __
⭐ DENİZ           kapı üstünden ufka kadar deniz bandı (%68–80) görünüyor mu: __
⭐ G7 TEKNE        kapının ötesinde %61–74 · x %26–45 · iz kapıdan içeri okunuyor mu: __
GÖK               ufuk %80'de, gök %20 — kapak başlığı (y üstten 36–374) ufkun üstünde kalıyor mu: ✓/✗
GÜNEŞ             bakış 20° — güneş gün boyu kameranın arkasında; disk hiç girmiyor: ✓/✗
GÖLGE             07:00 doğu duvarı gölgesi havuzu örtüyor mu · 17:10 batı duvarı gölgesi suyun batı
                  3 m'sinde, tekne su üstü aydınlık mı: ✓/✗
```

## 1. USTA KARE

```
KARE    G7 (S6'nın HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne, neden]
SEED    [varsa]
KAPI    havuz 1 · havuzda tekne 0 · denizde tekne 1 (kıç eşiğin ötesinde) · iz kapıdan içeri · kapı
        AÇIK (keson doğu yuvasında) · üst 3 basamak kuru · figür 1 sırtı dönük · halat sarılı ·
        ufuk %79,8 yatay · batı kule %12,4 · doğu kule %59,0 · merdiven %70,7 → geçti/düştü
FİNAL HİYERARŞİ  ① tekne kapının ötesinde → ② havuz dolu ve boş → ③ figür + halat sarılı [SPEC §1]
PİKSEL  ufuk y ____ · kule x ____ / ____ · merdiven x ____ · tekne kıç y ____ · kabin çatısı y ____
        → plana ve SPEC §2'ye yazıldı mı: __
KAPAK   gök bandı (üstten 0–384) düz ve nesnesiz mi — başlık için: __
DOSYA   [kare dosya adı]
```

## 1b. ⛔ PİLOT ÜÇLÜ — FİNAL ÜRETİLEBİLİRLİK TESTİ [KILAVUZ_REHBERI §8 adım 2b · C1-b]

> Zincirin İLK halkası. Üçü onaylanmadan §2'nin kalanı üretilmez; (c) üretilemiyorsa
> kapsam daralır (sahne çıkar), prompt "düzeltilmez". Nirengi eşiği: KAMERA_ISTASYONU §7.
> ⭐ Bu filmde (c′) = S5 dolum + kalkış + kapı; öncelik sırası: S6 çıkış · S5 yüzme · S2 levha.

| parça | dosya | zincir_kontrol (önceki ↔ yeni · ana referans ↔ yeni) | 3 nirengi (px) | beş soru ✓ | sahip onayı (tarih) |
|---|---|---|---:|:---:|---|
| (a) referans karesi G7 + 3 nirengi işaretli (batı kule · doğu kule · merdiven) + ufuk | | — | | — | |
| (b) ilk halka G7 → G6 (tekne havuza, kıç d 9; iz kalkar; halat ele; ışık AYNI) | | geçti/düştü · geçti/düştü | | — | |
| (c) final I2V (G6 → G7) — tekne kapıdan çıkar, iz içeri, havuz boş | | geçti/düştü | | ✓/✗ | |
| (c′) en zor klip: S5 dolum + kalkış + kapı I2V (G5 → G6) | | geçti/düştü | | ✓/✗ | |
| (c″) S2 levha I2V (G2 → G3) — sapanla, açıklığa, kaynak | | geçti/düştü | | ✓/✗ | |

## 2. GERİYE ZİNCİR — KARE başına TEK satır · G6 → G5 → G4 → G3 → G2 → G1 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = ufuk + iki kule + merdiven, elle ✓/✗ [DERS 25].

| G | araç + ayar | kaynak kare | master'dan ne KALDIRILDI / EKLENDİ | prompt birebir mi | zincir_kontrol (önceki · ana) | ufuk + nirengi elle | tekne/havuz sayımı | ⭐ su / kapı / gövde elle | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|:---:|---|
| 6 | | G7 | tekne denizden HAVUZA (kıç d 9, yüzer, güverte %42) · iz kalkar, pervane suyu kıçta · halat figürün eline, batı halatı gevşek · ışık AYNI | | geçti/düştü · geçti/düştü | ✓/✗ | 1 / 1 | dolu / açık / boyalı | |
| 5 | | G6 | su ÇEKİLİR → kuru taban, takozlar, merdiven kuru · tekne takoza (güverte %33) · kapı KAPALI · menfezden ilk su · kıç halatları · 2 işçi · ışık 15:10 | | | | 1 / 1 | ilk su / kapalı / boyalı | |
| 4 | | G5 | kabin krem → GRİ + ilk krem bandı · camlar ÇIKAR (kasada) · platform kabinde · variller + kasa güvertede · boş variller rampa dibi · güverte dağınık · ışık 13:10 | | | | 1 / 1 | yok / kapalı / boyalı | |
| 3 | | G4 | boya kalkar → GRİ çelik + 2 levha dikişli · maske bandı · palet kıçta · platform kıçta · sprey ünitesi · ışık 11:10 | | | | 1 / 1 | yok / kapalı / gri+levha | |
| 2 | | G3 | levhalar kalkar → 2 KARE açıklık · levha A SAPANA (kamyon doğu rıhtımı, kanca yüklü), B kasaya · branda + 3 torba + 2 kesik parça · kazan batı · ışık 09:10 | | | | 1 / 1 | yok / kapalı / gri+delik | |
| 1 | | G2 | gri kalkar → kıç 2/3 PAS bandı + ön 1/3 KABUK · delikler YIRTIK · kamyon + kazan + branda kalkar · yıkama ünitesi + hortumlar · taban ıslak · ışık 07:10 | | | | 1 / 1 | yok / kapalı / pas+kabuk | |
| 0 | | G1 | pas bandı kalkar → KABUK bütün gövde · yalnız 1 m pale şerit kıç iskelede · delikler kabuk altında GİZLİ · ışık 07:00 | | | | 1 / 1 | yok / kapalı / kabuk | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTI boş kalır — kare atılır, yeniden türetilir.
⭐ Her kare hem ÖNCEKİ onaylıyla hem ANA REFERANSLA (G7) karşılaştırılır: zincir_kontrol.sh <önceki> <yeni> G7 [C1-f].
⭐ G7 → G6 filmin en riskli editidir: tekneyi denizden havuza taşırken BOY (451 px) ve kabin
   biçimi korunur; model yeni tekne çizerse "the same boat" cümlesi öne alınarak tekrar denenir.
⭐ G6 → G5 "suyu çekme" editidir: takozlar, merdivenin 20 basamağı ve kuru taban geri gelmeli.
⭐ G1 → G0 "kabuğu geri koyma" editidir; delikler kabuğun ALTINDA kalmalı (görünmez).
⛔ Her karede TEK TEKNE sayılır [SPEC §6].
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn. Kırpma BAŞTAN [§2.7 ③].
> ⭐ baş/orta/son [C1-a]: başta malzeme kartın ① yerinde mi · ortada taşıyıcıyla birlikte mi
> (süzülmüyor, boyu değişmiyor) · sonda ④ farkı görünüyor mu. Üç ✓ olmayan klip yeniden üretilir.

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef | prompt birebir mi | ffprobe süre | kırpma | teslim | yüzey kanıtı | beş soru ✓/✗ | baş/orta/son | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|:---:|:---:|---|
| 0 | | **A** | G0 | G1 — ⛔ şerit İLK SANİYEDE uzadı mı ✓/✗ · kabuk KALKARAK mı açıldı (belirmedi) ✓/✗ · iki delik göründü mü ✓/✗ | geçti/düştü | | | | 8,0 | | ✓/✗ | ✓✗✗ | |
| 1 | | B | G1 | G2 — ⭐ yıkama ünitesi rampadan ÇIKTI mı ✓/✗ · gri çelik kıçtan öne mi ✓/✗ · delikler KARE kesildi mi ✓/✗ · kamyon sağdan geldi mi ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 2 | | B | G2 | G3 — ⭐ levha sapanla İNDİ mi ✓/✗ · açıklığa oturdu mu ✓/✗ · kesik parçalar KASAYA ✓/✗ · kamyon sağdan ÇIKTI mı ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 3 | | B | G3 | G4 — ⭐ kırmızı kıçtan başa ✓/✗ · lacivert ikinci geçiş ✓/✗ · su hattı TEK çizgi ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 4 | | B | G4 | G5 — ⭐ 5 cam kasadan açıklığa ✓/✗ · kabin krem ✓/✗ · platform rampadan ÇIKTI mı ✓/✗ · taban boş ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 5 | | B | G5 | G6 — ⭐ su menfezden ✓/✗ · basamaklar sırayla ✓/✗ · tekne kırmızı örtülünce KALKTI mı ✓/✗ · kapı seviye sonrası KAYDI mı ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 6 | | **G** | G6 | G7 (usta kare) — ⭐ kıç eşiği geçti mi ✓/✗ · iz kapıdan içeri ✓/✗ · net, iz yok ✓/✗ · uzaklaşırken bitti mi ✓/✗ | | | | | 8,0 | | ✓/✗ | | |

## 4. ⭐ REJİM G ÖLÇÜMÜ — S6, depoda üçüncü koşu

```
GÖLGE            G6/G7 batı duvarı gölgesinin su üstündeki kenarı farkı: ____ px (hedef 0)
İZ               motion streak ya da hayalet nesne: var/yok
DENİZ            G6–G7'de dalga var mı (ipek değil): ✓/✗ · 48,0 dikişinde ipek → dalga geçişi: rahatsız edici mi ✓/✗
FİGÜR            sırtı dönük kaldı mı: ✓/✗ · yüz okundu mu: ✓/✗
BAŞ EŞİĞİ        kaç saniyede geçti: ____ (plan ≈ 2,0)
KIÇ EŞİĞİ        kaç saniyede geçti: ____ (plan ≈ 7,0) · 8 sn'de kıç eşiğin ötesinde mi: ✓/✗
                 ötesinde değilse İKİNCİ KABUL (kıç eşiğin üstünde, baş açıkta): ✓/✗ → SPEC §1
BOY              tekne 0/4/8 sn: ____ / ____ / ____ px (perspektif küçülmesi hariç, KISALMAMALI) · cam 5/5/5: ✓/✗
İZ / SU          iz kapıdan içeri döndü mü: ✓/✗ · havuz suyu duvarlara çarptı mı: ✓/✗
8,0 DİKİŞİ       rejim A'nın okunur figürleri → rejim B izleri: rahatsız edici mi: ✓/✗
⭐ ONE MORE TURN ve SWALLOWED BUS'tan sonra üçüncü gerçek zaman ölçümü. Sonuç DERSLER.md'ye (kart D) yazılır.
```

## 5. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM §6]

```
① BİÇİM         ffprobe → ____   (1080,1920,30/1,h264)
② SÜRE          ffprobe format=duration → ____ sn   (56,0 · kart YOK · logo YOK)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 <plan> → __
                beklenen kesmeler 8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0
                ("PLANIN KENDİSİ DÜZ" uyarısı BEKLENİR — sahip kuralı)
④ SES           ebur128 → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        0,0–0,8 müziksiz pencere (jet + dökülen su): __
                46,0–48,0 müziksiz pencere (dikiş: durulmuş su, açık kapı): __ · 48,0 motor · 50,0'da müzik girdi mi: __
⑥ FLICKER       signalstats YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 54.0 → SPEC §1 üçlüsü görünüyor mu: __
                54,0 ↔ 55,0 kıç y farkı: ____ px
                KAPAK KANITI zincir_kontrol.sh g7_kaynak.jpg kapak.png → __
                KAPAK KONTRAST başlık/gök: ____ : 1 (≥ 4,5 → bantsız; altı → antrasit bant) [KAPAK §3]
```

## 6. PLANDAN SAPMALAR

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
19.09.2026 — plan, proje sahibinin senaryosunun (S1–S7) depo formatına çevrilmiş hâlidir; yedi
             değişiklik plana §KONSEPT KAPISI altına yazıldı ve sahip onayladı. Sapma değil, ilk
             sürümün kendisi budur.
```
