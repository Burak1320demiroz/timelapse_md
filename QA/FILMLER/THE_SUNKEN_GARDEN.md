# THE_SUNKEN_GARDEN — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 7 × 8,0 sn = 56,0 sn (kural dikey 7×8) · paylaşım 2x → 28,0 sn sahne bloğu + 5,0 sn kart = 33,0 sn (videoda 0:00.0–0:41.0: 7 klip + 5,0 sn statik kart)
plan: dikey_shorts/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_DIKEY_TIMELAPSE.md (23.10.2026 · 7 sahne · İKİ KEYFRAME ZİNCİRİ)
QA SPEC: dikey_shorts/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_QA_SPEC.md
üretim günlüğü: dikey_shorts/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_URETIM_GUNLUGU.md
yayın dosyası: raporda `THE_SUNKEN_GARDEN.mp4` · 0:41.0 (7 klip: 0:00.0–0:35.0 + 0:36.0–0:41.0 5.0 sn statik end card) · 9:16 dikey · tek sabit kamera istasyonu (−15° tilt)
master: bilinmiyor (beş mercek de 2x yayın kopyasıyla koşuldu)
kapak: ❺ "cover: NOT SUPPLIED" (0:36.0'deki statik kart incelendi)
koşu tarihleri: 25.10.2026 · sahip koşusu (Gemini) · ajan inceleme ve kaydı 25.10.2026

---

## ⭐ AJAN ÖLÇÜMÜ VE MERCEK DEĞERLENDİRMESİ

Video modele 41 saniyelik, 7 sahneli ve sonunda 5 saniyelik statik bir başlık kartı bulunan kopya olarak girmiştir. Beş mercek de kör/yarı-kör modda çalıştırılmıştır.

Kamera kadrajı, arka tuğla duvar ve çam ağacı nirengileri sabit kalmış; terk edilmiş bir yüzme havuzunun modern bir batık bahçeye dönüştürülmesi anlatısı başarıyla iletilmiştir. Ancak üç kritik noktada ağır kural ve fizik ihlalleri kaydedilmiştir:
1. **Zaman Saatinin Kırılması (Timelapse $\rightarrow$ 1x Gerçek Zaman):** 0:25.0'de video hızla akan bir timelapse olmaktan çıkıp insanların normal yürüyüş hızında basamaklardan indiği, kahve tepsisi taşıdığı ve dudak hareketleriyle konuşma/diyalog seslerinin duyulduğu 1x gerçek zamanlı bir videoya dönüşmüştür (`ONE CLOCK 2/10`, `WRONG DIRECTION`).
2. **Kapak Kartında Zamanın Geri Sarılması:** 0:36.0'daki statik başlık kartı, son karenin (0:35.0) dondurulması yerine sahnenin 0:30.0'daki eski hâlini (kahve taşıyan adamın basamakların tepesinde olduğu kareyi) geri getirmiştir (`THE LAST SECONDS 3/10`, `END CARD SHOWS LAST SCENE: DIFFERENT`).
3. **Şantiye ve İnşa Süreksizliği (Rebuilt Every Shot):** Her kesmede malzemeler taşınarak değil havadan belirerek veya yok olarak değişmiştir (0:03.5 yaprak torbaları yok olup skid-steer belirdi; 0:07.5 skid-steer kaybolup çakıl torbaları geldi; 0:12.5 çakıl zemin aniden tam montajlı ahşap karkas ızgarayla yer değiştirdi).

```
YAYIN KURGUSU (7 Klip · 0:00.0 – 0:41.0)
 0:00.0 – 0:03.5  Klip 1:  Boş, ıslak yaprak dolu beton havuz tabanının süpürülmesi ve torbalanması
 0:03.5 – 0:07.5  Klip 2:  Basınçlı suyla beton havuz tabanının yıkanması (skid-steer solda belirir)
 0:07.5 – 0:12.5  Klip 3:  Tabana çakıl serilmesi (beyaz dökme çuvallardan zemin kaplama)
 0:12.5 – 0:14.5  Klip 4:  Ahşap karkas taşıyıcı ızgara sisteminin yerleştirilmesi
 0:14.5 – 0:19.5  Klip 5:  Ahşap zemin tahtalarının (decking) vidalanması ve saksı kasalarının montajı
 0:19.5 – 0:23.5  Klip 6:  Dairesel taş ateş çukurunun örülmesi ve taş istifleme
 0:23.5 – 0:35.0  Klip 7:  FİNAL VURUŞU: Akşam mavi saatinde ateş çukurunun yanması, ip ışıklar, kahve servisi ve insanların toplanması (⚠️ 0:25.0'ten itibaren 1x gerçek zaman + diyalog)
 0:36.0 – 0:41.0  End Card: "THE SUNKEN GARDEN" statik kartı (⚠️ 0:30.0 karesine geri sarım)
```

```
✅ TUTANLAR
· ANLATI VAADİ VE FİNAL VURUŞU (❺ 10/10 PASS): Terk edilmiş beton havuzun 7 adımda ateş çukuru ve ahşap güverteli modern bir bahçeye dönüşmesi vaadi eksiksiz gerçekleşmiştir.
· GÜN VE MEVSİM DÖNGÜSÜ (❷ 10/10): Sarı-kahve sonbahar yaprakları ve çalışanların ceketleri tek bir sonbahar gününün sabahından alacakaranlık mavi saatine geçişini başarıyla taşımıştır.
· SABİT KADRAJ VE NİRENGİ: Arka tuğla duvar (%85 yükseklik) ve çam ağacı (%96 yükseklik) istasyonun sabitliğini korumuştur.
```

```
⛔ ÖLDÜRÜCÜ VE AĞIR KUSURLAR
① REBUILT EVERY SHOT ⛔ (❸ 0/10): 6 kesmenin 6'sında da malzeme ve makineler taşınmadan havadan değişmiş; karkas ızgara (0:12.5) tek bir montaj adımı gösterilmeden bitmiş olarak belirmiştir.
② WRONG DIRECTION / ZAMAN SAATİNİN KIRILMASI (❷ 2/10): 0:25.0'de timelapse hız rejimi çökmüş; gerçek zamanlı insan yürüyüşü ve konuşma diyalogları başlamıştır.
③ KAPAK KARTI GERİ SARIMI (❷ 3/10 · ❶ C5 5/10 · ❺ C2 5/10): 0:36.0'daki statik başlık kartı son sahnenin (0:35.0) dondurulması kuralını çiğneyerek sahneyi 6 saniye geriye (0:30.0) sarmıştır.
④ MELTING VE ANİ BELİRMELER (❶ 4/10 · ❹ 4/10): Ateş çukuru taşları (0:21.0) eriyerek oturmuş, tezgâh palet krikosuna dönüşmüş (0:20.0), aletler havadan buharlaşmıştır.
```

---

## MERCEKLER

| mercek | durum | puan | hüküm | ham | en ağır bulgu (m:ss.s) · not |
|---|---|:-:|---|---|---|
| **❶ GÖRÜNTÜ** | TAM | **5,3** | TIMELAPSE · MELTING | [THE_SUNKEN_GARDEN_Q1_GORUNTU_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q1_GORUNTU_HAM.md) | Ateş çukuru eriyerek belirme (0:21.0); 0:27.0 insan figürlerinin net ve gerçek zamanlı hareketi (3/10); kart 0:30.0'a geri sarıyor |
| **❷ ZAMAN VE KESME** | TAM | **6,3** | WRONG DIRECTION | [THE_SUNKEN_GARDEN_Q2_ZAMAN_KESME_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q2_ZAMAN_KESME_HAM.md) | 0:25.0'de timelapse 1x gerçek zamana düştü; gök dondu (One Clock 2/10); 0:36.0 kartı sahneyi 0:30.0'a geri sardı (3/10) |
| **❸ ŞANTİYE** | TAM | **5,1** | **REBUILT EVERY SHOT ⛔** · WORKING | [THE_SUNKEN_GARDEN_Q3_SANTIYE_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q3_SANTIYE_HAM.md) | Seam audit 0/10 (6 dikişin 6'sında kusur); 0:12.5 ahşap karkas montajsız belirdi (The Growth Nobody Made); araç giriş rotası yok |
| **❹ İNŞA** | TAM (Mod V) | **5,6** | SAME · APPEARING · INVITED | [THE_SUNKEN_GARDEN_Q4_INSA_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q4_INSA_HAM.md) | Karkas ızgara ve bambular aniden oluştu (Nothing is born complete 4/10); çakıl çuvalları nakliyesiz belirdi (4/10) |
| **❺ TESLİM** | TAM (Mod V) | **8,4** | ENDS | [THE_SUNKEN_GARDEN_Q5_TESLIM_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q5_TESLIM_HAM.md) | Final Beat PASS (0:24.0 yanan ateş çukuru ve akşam buluşması); kurgu ve anlatı vaadi tam; kart geri sarımı 5/10 |

```
FİLM PUANI:     6,1 (N=5) ⛔ DÜŞTÜ        [ (5,3 + 6,3 + 5,1 + 5,6 + 8,4) / 5 ]
ÖLDÜRÜCÜ HÜKÜM: REBUILT EVERY SHOT (❸)    [KILAVUZ_REHBERI §4.3 — telafi etmeyen kapı]
OLUMSUZ HÜKÜM:  MELTING (❶) · WRONG DIRECTION (❷) · REBUILT (❸) · APPEARING (❹)
SONUÇ:          ⛔ DÜŞTÜ (FAIL — Şantiye süreksizliği ve zaman saatinin kırılması)
```

---

## DOĞRULAMA (D1–D6)

- **Geri okuma**: ❶ ✓ (boş / NONE / 7) · ❷ ✓ (THE_SUNKEN_GARDEN.mp4 / NONE / 7) · ❸ ✓ (THE_SUNKEN_GARDEN.mp4 / NONE / 7) · ❹ ✓ (THE_SUNKEN_GARDEN.mp4 / NONE / 7) · ❺ ✓ (THE_SUNKEN_GARDEN.mp4 / NONE; cover: NOT SUPPLIED / 7).
- **D1 (Dosya dışı damga)**: Yok. Zaman damgaları 0:00.0 – 0:41.0 aralığındadır.
- **D2 (Klip sayısı)**: 7 sahne klibi eksiksiz izlenmiştir.
- **D3 (Süre itirazı)**: Yok. 41 saniyelik videonun tamamı taranmıştır.
- **D4 (Kesme damgası)**: Makine ölçüm bloğu verilmediği ve yer tutucular (`{SPEED}`, `{CUTS}`) kaldığı için ❷ kesme tablosunu NOT VERIFIABLE olarak işaretlemiştir.
- **D5 (Kart)**: 0:36.0'deki statik başlık kartı tespit edilmiş, ancak 0:30.0 karesine geri sarım yaptığı için C1/C5/C2'de puan kırılmıştır.
- **D6 (Kurgu tablosu)**: 7 sahnenin dönüşüm sırası planla kronolojik olarak örtüşmektedir.

---

## ❓ MERCEKLERİN SORULARI VE PLANDAN CEVAPLAR (Questions for the Document)

### ❶ GÖRÜNTÜ (Lens 1)
1. **Format değişkenleri neden yer tutucu olarak kaldı?**
   - *Plandan Cevap*: Model doğrudan ham video ile test edilmiştir; plan değerleri: Hız 2x, 7 sahne × 8,0 sn (paylaşım 28 sn sahne + 5 sn kart), en-boy 9:16 (`THE_SUNKEN_GARDEN_QA_SPEC.md`).
2. **0:25.0'de timelapse hızından gerçek zamanlı diyaloga geçiş planlandı mı?**
   - *Plandan Cevap*: **HAYIR.** Planda son sahne (S6) Rejim A (10 dk temsil) olarak tanımlanmıştır (`SANTIYE_HAREKETI §2`); insanların rahatça oturması istense de konuşma ve 1x gerçek zamanlı diyalog **YASAKTIR**. Depo kuralları gereği timelapse tek bir hız rejimini korumalıdır.
3. **0:36.0'daki kapak kartı neden son kare (0:35.0) yerine 0:30.0 karesini kullandı?**
   - *Plandan Cevap*: Bu bir kurgu ve model kusurudur. Kural (`KILAVUZ_REHBERI §2.7 ④`, `DERS 63`), kapak kartının videonun en son karesini (G7) tam dondurması gerektiğini söyler. Sahneyi geriye sarmak zaman sürekliliğini bozar.

### ❷ ZAMAN VE KESME (Lens 2)
1. **Klip başına beyan edilen güneş yönü ve yüksekliği nedir?**
   - *Plandan Cevap*: Sabah 08:00'den (112°/18°) akşam 19:15 mavi saate (285°/0°) kadar tek bir sonbahar gününün yay çizgisidir. Kamera kuzeye (0°) bakar, tilt 15° aşağıdır; güneş hiçbir zaman kadraja girmez.
2. **Klip başına geçen süre ve hız rejimi nedir?**
   - *Plandan Cevap*: S0–S5 Rejim B (sahne başına 2 saat temsil, master 8 sn / 2x'te 4 sn); S6 Rejim A (10 dakika temsil).
3. **0:25.0'teki 1x hız düşüşü planlı mıydı?**
   - *Plandan Cevap*: Hayır; model Rejim A'yı yanlış yorumlayarak 1x gerçek zamana düşmüş ve diyalog eklemiştir.

### ❸ ŞANTİYE (Lens 3)
1. **Kesmeler arasındaki ani araç ve malzeme takasları planlı mıydı?**
   - *Plandan Cevap*: Hayır; planda havuz çukuruna her şeyin basamaklardan indirilmesi (direnç şartı) açıkça yazılmıştır. Skid-steer'ın birden belirmesi ve karkasın tek adımda bitmesi AI süreksizlik zaafıdır.
2. **Tabandaki suyun kaybolması tahliye olarak mı planlandı?**
   - *Plandan Cevap*: Evet; S1'de basınçlı yıkama suyunun havuz dip süzgecinden tahliyesi öngörülmüştü.
3. **Bambuların ve minderlerin 0:23.5'te aniden belirmesi planlı mıydı?**
   - *Plandan Cevap*: Planda bunların basamaklardan sırayla taşınması hedeflenmişti.

### ❹ İNŞA (Lens 4)
1. **Ahşap karkas ızgara ve saksı kasalarının parça parça montajı planlandı mı?**
   - *Plandan Cevap*: **EVET.** `INSAAT_YONTEMI_KILAVUZU §3` gereği karkas kirişlerinin sırayla dizilmesi ve vidalanması gerekirdi. Model ara aşamaları atlayarak karkası birden bitmiş üretmiştir (`Nothing is born complete 4/10`).
2. **Mini yükleyici ve dökme çakıl torbalarının sahaya ulaşım rotası neydi?**
   - *Plandan Cevap*: Arka servis yolundan basamak başına kadar; basamaklardan aşağıya ise işçiler tarafından el arabası ve kovalarla indirilmesi planlanmıştı.

### ❺ TESLİM (Lens 5)
1. **Açılış kancası ve final sahnesi hedefleri nelerdi?**
   - *Plandan Cevap*: Açılış: Yaprak dolu, ıslak ve çirkin bir terk edilmiş havuz ("Dead Pool"). Final: Mavi saatte ip ışıkların yandığı, ortasında taş ateş çukurunda alevlerin titreştiği lüks bir batık bahçe ("Sunken Garden"). Vaat tam yerine getirilmiştir.
2. **Ses tasarımı nasıl planlandı?**
   - *Plandan Cevap*: Planda müzik yasaktır (`⛔ MÜZİK YOK`); sesin diegetik yaprak hışırtısı, basınçlı yıkama sesi, çekiç/vida sesleri ve finalde ateş çatırtısı olması hedeflenmiştir. Gerçek insan konuşması planlanmamıştır.

---

## 🔬 İKİNCİ KOŞU (K2 — 27.10.2026 · 37 Klip Serbest Dilimleme Testi)

> **DİKKAT — PUAN BAĞLAYICI DEĞİLDİR:** Bu koşuda modele `qa_paket.sh` makine ölçüm bloğu verilmemiş (`{SPEED}`, `{CLIP_COUNT}`, `{CUTS}` yer tutucuları boş gitmiş); model 41 saniyelik videoyu 1'er saniyelik adımlarla (37 klip) örneklemiştir (`DERS 105 / 106`, `GAME ON` ve `TOTAL RESET` emsali).
> 1 saniyelik adımlarda dikişler arası kesme farkları kaybolduğu için model tüm merceklerde 10/10 şişik puan vermiştir. **Resmî geçerli ölçüm K1 (7 sahne · 6,1 ⛔ DÜŞTÜ) koşusudur.**

### K2 Mercek Puanları

| mercek | durum | puan | hüküm | ham | en ağır bulgu (m:ss.s) · not |
|---|---|:-:|---|---|---|
| **❶ GÖRÜNTÜ** | EKSİK · ŞİŞİK (D2 ✗) | — (rapor: 10,0) | TIMELAPSE · SOLID | [THE_SUNKEN_GARDEN_Q1_GORUNTU_HAM_K2.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q1_GORUNTU_HAM_K2.md) | 100/10 · kadraj ve nirengi sabit · eriyen cisim YOK (`NONE FOUND`) · ⚠️ 37 klip 1 sn dilimlemesi |
| **❷ ZAMAN VE KESME** | EKSİK · ŞİŞİK (D2 ✗) | — (rapor: 10,0) | PASSING · TIME | [THE_SUNKEN_GARDEN_Q2_ZAMAN_KESME_HAM_K2.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q2_ZAMAN_KESME_HAM_K2.md) | 90/9 · güneş açısı 53°→24° · The cut that carries: 0:24.0 · 33 kesmenin tümü TIME · ⚠️ 37 klip dilimlemesi |
| **❸ ŞANTİYE** | EKSİK · ŞİŞİK (D2 ✗) | — (rapor: 10,0) | SAME WORLD · WORKING | [THE_SUNKEN_GARDEN_Q3_SANTIYE_HAM_K2.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q3_SANTIYE_HAM_K2.md) | 33 dikişin 33'ü hatasız (0 kusur) · tuğla duvar kanıt (0:00 ve 0:34) · rölanti yok · ⚠️ 37 klip dilimlemesi |
| **❹ İNŞA** | EKSİK · ŞİŞİK (mod V · D2 ✗) | — (rapor: 10,0) | SAME · BUILT · INVITED | [THE_SUNKEN_GARDEN_Q4_INSA_HAM_K2.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q4_INSA_HAM_K2.md) | Temizlik → yıkama → çakıl → karkas → deck → ateş çukuru sırası tam · davetsiz nesne yok (`NONE FOUND`) |
| **❺ TESLİM** | YANLIŞ GİRDİ (mod V · D2 ✗) | — (rapor: 10,0) | ENDS | [THE_SUNKEN_GARDEN_Q5_TESLIM_HAM_K2.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_SUNKEN_GARDEN/THE_SUNKEN_GARDEN_Q5_TESLIM_HAM_K2.md) | Vaat tam çıktı · 0:25.0 yanan ateş çukuru ve ip ışıklar final beat (`PASS`) · 0:36.5 kart tam (Cat 7 NV) |

```
K2 FİLM PUANI:   — · N=0 (rapor-içi ortalama: 10,0)
HÜKÜM:           ⚠️ BAĞLAYICI DEĞİL (Ölçülmüş olgular bloğu olmadan 1'er saniyelik dilimleme ile koşuldu)
GEÇERLİ KAYIT:   K1 KOŞUSU (6,1 ⛔ DÜŞTÜ · REBUILT EVERY SHOT 0/10 · WRONG DIRECTION 2/10)
```

### K2 Soruları ve Plandan Cevaplar

#### ❶ GÖRÜNTÜ (Lens 1)
1. **Hardwood decking tahtaları için belirlenen malzeme şartnamesi nedir?**
   - *Plandan Cevap*: 21×145 mm dış mekân dayanımlı sert ahşap (Garapa / Cumaru), gizli klipsli paslanmaz çelik vidalama sistemi ve UV koruyucu tik yağı cilası.
2. **Havuz temizliğinden ahşap güverte montajına kadar olan inşaat sırası tek bir sürekli iş akışı olarak mı planlandı?**
   - *Plandan Cevap*: Evet; tek bir sonbahar gününde 7 sahneli kronolojik akış (S0 yaprak süpürme $\rightarrow$ S1 basınçlı yıkama $\rightarrow$ S2 çakıl serme $\rightarrow$ S3 karkas kurma $\rightarrow$ S4 tahta vidalama $\rightarrow$ S5 taş ateş çukuru $\rightarrow$ S6 akşam kullanımı).
3. **Çakıl tabakasının altındaki batık havuz tabanı için hangi drenaj gereksinimleri belirlendi?**
   - *Plandan Cevap*: Havuzun orijinal dip tahliye sifonu açık tutulmuş; üzerine 15 cm'lik 10–20 mm kırmataş drenaj agregası serilerek suyun serbest tahliyesi sağlanmıştır.
4. **Dış mekân ip ışıkları ve ateş çukuru peyzaj mimarisinin birincil aşamasına dahil miydi?**
   - *Plandan Cevap*: Evet; S5'te ateş çukuru taşları örülmüş, S6'da ip ışıklar yakılarak alan oturma ve yaşam alanına dönüştürülmüştür.

#### ❷ ZAMAN VE KESME (Lens 2)
1. **İnşaat dizisi sırasında her klip için beyan edilen güneş yönü ve yükseklik takvimi nedir?**
   - *Plandan Cevap*: Sabah 08:00'den (112°/18°) akşam 19:15 mavi saate (285°/0°) uzanan tek bir sonbahar günü yay çizgisi; kamera kuzeye bakar (−15° tilt), güneş doğrudan kadraja girmez.
2. **Havuz temizliğinden akşam sosyal kullanımına geçiş için belirlenen mevsimsel takvim nedir?**
   - *Plandan Cevap*: Tek bir sonbahar günü (Ekim sonu; dökülen sarı yapraklar, çalışanların montları ve erken gün batımı bu takvimi taşır).
3. **Her kesme aralığında ve toplam film süresinde temsil edilen beyan edilmiş geçen süre nedir?**
   - *Plandan Cevap*: S0–S5 arası sahne başına 2 saat (toplam ~10-11 saat gündüz inşası), S6 akşamında 10 dakikalık mavi saat (Rejim A); toplam ~11 saatlik bir gün.
4. **Işık değişimlerini vurgulamak için herhangi bir klip held hour olarak planlandı mı?**
   - *Plandan Cevap*: S6'nın son saniyeleri (2x'te 2 sn, master'da 4 sn) mavi saat ışık tutuşu olarak planlanmıştır.
5. **Proje ilerleme aşamaları için hedeflenen tempo neydi?**
   - *Plandan Cevap*: Başlangıçta kaba temizlik adımları, ortada yoğun marangozluk ve taşçılık, finalde sakinleşen ve işlevi sergileyen bir tempo eğrisi.

#### ❸ ŞANTİYE (Lens 3)
1. **Ağır havuz temizliğinden ince ahşap işçiliğine ve peyzaja geçiş takvimi neydi?**
   - *Plandan Cevap*: S0–S1 sabah (temizlik ve yıkama), S2 öğle (çakıl yatağı), S3–S4 öğleden sonra (ahşap karkas ve zemin döşeme), S5 ikindi (taş örme), S6 akşam (peyzaj ve oturma).
2. **Çakıl tabanı ve ahşap güverte için malzeme miktarları havuz boyutlarına göre tam hesaplandı mı?**
   - *Plandan Cevap*: Evet; ~10×4,5 m taban alanı için ~7 m³ çakıl agrega, ~45 m² karkas ızgarası ve zemin tahtası planlanmıştır.
3. **Perimetre ip ışıkları ve duvara monte armatürler için hangi aydınlatma entegrasyon planı belirlendi?**
   - *Plandan Cevap*: Arka tuğla duvara pirinç aplikler ve üst parapet boyunca sıcak ışıklı edison ampullü ip aydınlatma hattı çekilmiştir.
4. **Akşam ağırlama dizisi peyzaj uygulamasının ayrılmaz bir tamamlanma aşaması olarak mı planlandı?**
   - *Plandan Cevap*: Evet; ancak diyalogsuz ve Rejim A timelapse hızında olması şarttı (1x gerçek zamana düşüş ve konuşmalar modelin kural ihlalidir).
5. **Ahşap güvertenin altındaki batık bahçe yatağı için hangi drenaj hükümleri belirlendi?**
   - *Plandan Cevap*: Çalışır durumdaki havuz dip sifonu üzerine jeotekstil keçe ve çakıl yatağı serilerek ahşap kirişlerin suya temas etmesi önlenmiştir.

#### ❹ İNŞA (Lens 4)
1. **Alt zemin karkası ve güverte tahtaları için hangi kereste türü ve işlem şartnameleri belirlendi?**
   - *Plandan Cevap*: Taşıyıcı karkasta 50×100 mm basınçlı emprenye çam kalaslar; zemin kaplamasında 21×145 mm dış mekân yağlı Garapa sert ahşap.
2. **Ahşap güvertenin altındaki çakıl alt taban için tam yük taşıma hesapları neydi?**
   - *Plandan Cevap*: 15 cm sıkıştırılmış kırmataş dolgu, karkas takozlarının yükünü havuz tabanına eşit dağıtır.
3. **Taş ateş çukuru duvar üniteleri yapı mühendisliği planında kuru yığma mı yoksa harçlı mı belirlendi?**
   - *Plandan Cevap*: Ateşe dayanıklı refrakter harçlı iç çekirdek, dış yüzeyde kuru yığma görünümlü andezit bloklar.
4. **Entegre ahşap saksı kasaları için hangi toprak ve drenaj gereksinimleri belirlendi?**
   - *Plandan Cevap*: İç kısımlar EPDM yalıtımlı, tabanda çakıl drenaj filtresi ve bambular için hafifletilmiş torf-ponza karışımı.
5. **Akşam ağırlama dizisi mimari peyzaj projesi için resmî tamamlanma kilometre taşı mıydı?**
   - *Plandan Cevap*: Evet; mekanın başarıyla teslim edildiğini ve çalıştığını kanıtlayan Final Beat adımıdır.

#### ❺ TESLİM (Lens 5)
1. **Batık bahçe dönüşümü için hedeflenen duygusal ton veya yaşam tarzı anlatısı neydi?**
   - *Plandan Cevap*: Terk edilmiş, çürümüş bir beton çukurun sıcak, davetkâr ve huzurlu bir akşam sığınağına dönüşümünün getirdiği estetik doyum ("Dead Pool to Sunken Garden Lounge").
2. **Akşam toplanması ve kahve servisi videonun birincil anlatı getirisi olarak mı planlandı?**
   - *Plandan Cevap*: Evet; yanan ateş, yanan ışıklar ve mekândan yararlanan insanlar vaadin gerçekleştiğinin kanıtıdır.
3. **Gündüz ağır inşaatından akşam dinlencesine geçiş için hangi tempo tasarlandı?**
   - *Plandan Cevap*: Hızlı tempolu inşaattan (Rejim B), dinginleşen ve süresi uzayan mavi saat işlev anına (Rejim A) geçiş.
4. **Görsel ilerlemeye eşlik etmesi için hangi ortam ses tasarımı unsurları hedeflendi?**
   - *Plandan Cevap*: Diegetik şantiye sesleri (yaprak tırmığı, basınçlı yıkama, çekiç, vidalama, ateş çıtırtısı); müzik ve konuşma yasaktır.
5. **Bu video varlığı için hangi tanıtım veya platform yayın paketi planlandı?**
   - *Plandan Cevap*: 9:16 Shorts/Reels/TikTok dikey video, "THE SUNKEN GARDEN" kapak kartı, organik diegetik ses miksi.

