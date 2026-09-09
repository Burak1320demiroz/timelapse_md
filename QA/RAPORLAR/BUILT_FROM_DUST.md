# 📋 BUILT FROM DUST — QA KAYDI

```
FİLM        BUILT FROM DUST — Tozdan Doğan
FORMAT      9:16 · 6 sahne (0:24.0, 0:24.0, 0:08.0, 0:08.0, 0:08.0, 0:10.0) = 1:22,0 + kapak 5,0 sn = 1:27,0
ÖLÇÜM       8/8 TAM MERCEK KOŞULDU (ek olarak ⑨ FAALİYET ve ⑩ SEBEP koşuldu)
            ham çıktılar: QA/HAM_RAPORLAR/BUILT_FROM_DUST_*_HAM.md
KARAR      ⛔ YAYINLANMAZ.
```

---

## 1. TÜM MERCEK HÜKÜMLERİ

| Mercek | Mod | Ham ort. | VERDICT |
|---|:---:|---:|---|
| ① KARE | Ⓥ ⚠️ karesiz | 1,1Ⓥ/10 | ⛔ **SIX SEPARATE SHOTS** |
| ② İNŞA | ⛔ Ⓥ belgesiz | 2,8Ⓥ/10 | ⛔ **DIFFERENT · APPEARING** |
| ③ ZAMAN | Ⓥ **V** | 3,3Ⓥ/10 | ⛔ **PASSES BUT NOT IN ONE DIRECTION** |
| ④ TESLİM | ⛔ Ⓥ belgesiz | 2,5Ⓥ/10 | ⛔ **STOPS** · **FAIL** (Final Beat) · NONE FOUND |
| ⑤ DEVAMLILIK | Ⓥ ⚠️ karesiz | 1,6Ⓥ/10 | ⛔ **A SET REBUILT EACH TIME** · kanıt: 3 dağ zirvesi (5/5 dikiş DEFECT) |
| ⑥ GEÇİŞ | ⛔ Ⓥ belgesiz | 4,5Ⓥ/10 | ⛔ **NEXT** · ⛔ **METRONOME** |
| ⑦ İŞ | Ⓥ ⚠️ karesiz | 1,8Ⓥ/10 | ⛔ **PARKED** · büyüme: 0:24.0 (habitat) · boş: 10,0 sn (%100) |
| ⑧ YÖNTEM | ⛔ Ⓥ belgesiz | 0,0Ⓥ/10 | ⛔ **APPEARED** · ilk beliren: foundation grid (0:05.0) · en iyi: NONE |
| ⑨ FAALİYET | Ⓥ ⚠️ karesiz | 3,5Ⓥ/10 | ⛔ **IDLE ANIMATION** · amaçsız hareket: 0:24.0 dairesel damperli kamyonlar |
| ⑩ SEBEP | ⛔ Ⓥ belgesiz | — | ⛔ RUN INCOMPLETE (QA_SPEC verilmedi) |

---

## 2. ⚠️ MOD DENETİMİ — TÜM MERCEKLER EKSİK GİRDİYLE KOŞTU

```
① KARE        ⛔ kare grabı verilmedi (kare_al.sh koşulmadı — STILL FRAMES SUPPLIED: 0)
② İNŞA        ⛔ QA_SPEC / plan verilmedi (mode V)
③ ZAMAN       ⛔ plan verilmedi (mode V)
④ TESLİM      ⛔ plan ve kapak verilmedi (mode V)
⑤ DEVAMLILIK  ⛔ kare grabı verilmedi (STILL FRAMES SUPPLIED: 0)
⑥ GEÇİŞ       ⛔ plan verilmedi (mode V)
⑦ İŞ          ⛔ kare grabı verilmedi (STILL FRAMES SUPPLIED: 0)
⑧ YÖNTEM      ⛔ QA_SPEC verilmedi (mode V)
⑨ FAALİYET    ⛔ kare grabı verilmedi (STILL FRAMES SUPPLIED: 0)
⑩ SEBEP       ⛔ QA_SPEC verilmedi (RUN INCOMPLETE)
```

Merceklerin tamamı dokümansız / karesiz (Mod V) koşmuştur. Skorlar ön koşudur; **VERDICT sonuçları bağlayıcıdır**.

---

## 3. EN AĞIR BULGULAR VE KÖK SEBEPLER

```
① KAMERA KİLİDİ SERBEST (0/10)
   Bütün klipler boyunca yavaş push-in / pull-back / pan / tilt hareketi mevcut.
   Kamera sabit tutulamadığı için arka plan jeolojisi ve nesneler morfluyor.

② YAPI VE YÖNTEM ÇÖKMÜŞ (APPEARING)
   - Temel ızgarası yapay bir biçimde parlayarak (fading in) beliriyor [0:05.0].
   - Ana habitat balon gibi şişerek yukarı doğru genişliyor [0:24.0].
   - İletişim kulesi ve yan tüp geçit hiçbir inşa safhası olmadan aniden beliriyor [0:48.0, 1:04.0].
   - S5'te takılan çatı güneş paneli S6'da tamamen kayboluyor (yapılan işin silinmesi).
   - Yük hattı kopuk: Vinç paneli havada asılı tutuyor, kablo/kanca bağlantısı yok.

③ ZAMAN VE HIZ ÇELİŞKİSİ (TIME RATE 0/10)
   - Araçlar gerçek zamanlı hızda ilerlerken gökyüzü ve yıldızlar aşırı zaman atlamalı (time-lapse) dönüyor [0:02.0, 1:04.0].
   - S3'te (0:48.0) renk aniden siyah-beyaza düşüyor; zaman sıçraması yerine stilistik renk değişimi algılanıyor.
   - Saniye bazında okunan zaman: ~2 gün.

④ FİNAL VURUŞU VE DÖNGÜ BAŞARISIZ (STOPS)
   - Film tamamlanmış bir yapıya ulaşamadan, tüp inflated durumdayken aniden duruyor (Final Beat: FAIL).
   - İlk ve son kareler eşleşmiyor (Loop: 0/10).

⑤ DEVAMLILIK VE DÜNYA KORUNAMIYOR (5/5 DİKİŞ DEFECT)
   - Her dikişte dünya ve araçlar yeniden kuruluyor: küçük roverlar dozere (0:48.0), dozer vince (0:56.0) dönüşüyor.
   - Vinç S5 (1:04.0) dikişinde aniden yok oluyor (teleportation).
   - Yer hafızası yok: tekerlek izleri ve zemin dokusu her dikişte tamamen sıfırlanıyor.

⑥ KESMELER ZAMAN DEĞİL "SIRADAKİ" HİSSİ VERİYOR (METRONOME)
   - Kesmeler zamansal ilerleme yerine visual reset işlevi görüyor.
   - Siyah-beyaz renk değişimi zamansal sıçrama değil "farklı render stili" olarak okunuyor.
   - Ritim aniden 24 saniyelik bloklardan 8 saniyelik bloklara düşüyor (nedensiz ivmelenme).

⑦ İŞ VE MAKİNE EYLEMİ (PARKED · THE GROWTH NOBODY MADE: 0:24.0)
   - Yapıların tamamı (temel ızgarası, habitat, kule, tüp geçit) makinelerin müdahalesi olmadan otonom olarak beliriyor/şişiyor.
   - Araçlar etrafta daireler çizerek hareketli dekor gürültüsü üretiyor fakat hiçbir inşa işi yapmıyor.
   - S5'teki dev vinç klip boyunca donmuş/statik duruyor.
   - S6 (1:12.0-1:22.0) tamamen boş/parked (%100 idle).

⑧ İNŞA YÖNTEMİ SIFIR (0.0/10 · APPEARED)
   - Filmed hiçbir eleman fiziksel bir inşa yöntemiyle (kalıp, döküm, kaldırma, montaj) üretilmiyor.
   - 0/5 eleman yapıldı (MADE: 0). Temel ızgarası, iletişim kulesi, çatı paneli doğrudan tamamlanmış olarak beliriyor.

⑨ FAALİYET VE AMAÇSIZ HAREKET (IDLE ANIMATION)
   - Damperli kamyonlar ve roverlar yük taşıyıp boşaltmak yerine habitat çevresinde sürekli dairesel döngülerde dönüyor [0:00.0, 0:24.0].
   - İş makineleri üretim yerine kinetik dekorasyon işlevi görüyor.
```

---

## 4. DOKÜMAN CEVAPLARI (QUESTIONS FOR THE DOCUMENT)

```
①-1  Sürekli kamera kayması (push-in/pull-back) kasten mi istendi?
     -> HAYIR. Bütün klipler sabit vantaj kilidi taşımalıydı.
①-2  Araçların zaman atlamalı çizgi (motion streak) yerine net video objesi olarak görünmesi kasten mi istendi?
     -> HAYIR. Araçlar timelapse hareket bulanıklığı taşımalıydı (DERS 50 ihlali).
①-3  Sağdaki büyük kayanın ilk iki vantaj arasında değişmesi planlandı mı?
     -> HAYIR. Arka plan çapa nesneleri sabit kalmalıydı.

③-1  Beyan edilen mevsimler ve klip başına geçen süre neydi?
     -> Doküman verilmediği için doğrulanamadı (~2 gün okundu).
③-2  Güneş açılarının klip içinde şafaktan alacakaranlığa süpürülmesi planlanırken araçların gerçek hızda gitmesi istendi mi?
     -> HAYIR. Time rate çelişkisi modelin gökyüzü ile yeri ayırmasından kaynaklandı.

⑤-1  İnşa makinelerinin safhalar arasında tamamen tür değiştirmesi planlandı mı?
     -> HAYIR. Araç kimliği ve şantiye filosu klipler arasında korunmalıydı.
⑤-2  Vincin çatı paneli gösterildikten hemen sonra aniden yok olması planlandı mı?
     -> HAYIR. Söküm veya sahadan ayrılma süreci gösterilmeliydi.

⑥-1  Her bir kesmenin temsil ettiği zaman aralığı neydi?
     -> Doküman verilmediği için doğrulanamadı.
⑥-2  0:48.0'daki siyah-beyaz kesme belirli bir kronolojik fazı mı temsil ediyordu?
     -> Siyah-beyaz stil değişimi timelapse dikiş fiziğini bozdu.

⑦-1  Ana habitatın inşaat makineleri kullanılmadan otonom olarak şişmesi planlandı mı?
     -> HAYIR. Her mimari büyüme bir makine veya iş kolunun eylemiyle ilişkilendirilmeliydi (THE GROWTH NOBODY MADE).
⑦-2  S5'teki vincin solar paneli tutarken tamamen statik kalması planlandı mı?
     -> HAYIR. Makine hareket döngüsü (slewing/hoisting) görünmeliydi.

⑧-1  İletişim kulesinin belirmesi S3 aşama merdiveninde modellenmiş bir göreve atanmış mıydı?
     -> Doküman verilmediği için doğrulanamadı.
⑧-2  Temel ızgarası ve solar paneller için malzeme teslimatı diziden bilerek mi çıkarıldı?
     -> Malzeme akışı ve montaj yöntemi olmadan inşaat anlatısı kurulamaz.

⑨-1  Rover ve kamyonların yük taşıması mı planlanmıştı yoksa dekoratif dairesel sürüş mü?
     -> Üretken olmayan dairesel sürüşler "aimless movement" olarak skorlandı.
⑨-2  Son gece klipinde şantiyenin tamamen parked olması planlanmış mıydı?
     -> S6 %100 idle stretch olarak kaydedildi.
```

---

## 5. KARAR

```
⛔ YAYINLANMAZ.
Yeniden kurgu veya renk düzeltmesi filmi kurtarmaz.
Tüm klipler ikili keyframe zinciri (foto1-video1-foto2) ve sıkı araç kapısı denetimiyle yeniden üretilmelidir.
```

---

## 6. BU ÖLÇÜMDEN ÇIKARILAN DERSLER

`kilavuzlar/DERSLER.md` → **DERS 49** (Opaklık/Fading in yasağı) ve **DERS 50** (Time Rate cümlelerinde Motion Blur şartı).
