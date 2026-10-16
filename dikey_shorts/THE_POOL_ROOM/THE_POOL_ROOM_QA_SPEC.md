# 🔍 THE POOL ROOM — QA SPEC

> Kilit listesi. Kör mercekler bu dosyayı GÖRMEZ (❶ ❷ ❸ · QA_KOSU §1).
> Plan: `THE_POOL_ROOM_DIKEY_TIMELAPSE.md` · Günlük: `THE_POOL_ROOM_URETIM_GUNLUGU.md`

```
FİLM      THE POOL ROOM · 8 × 8,0 = 64,0 sn (⚠️ SAHİP İSTİSNASI 16.10.2026 · kural 7 × 8) · KAPAK KARTI SONDA (sahip kuralı 16.10.2026; yayında 4,8 sn + 2,1 sn erime) · LOGO YOK · SAHNELERDE YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    64,0 sn / yok · ⛔ öncesi/sonrası karşılaştırma YOK · ⛔ açılış yazısı YOK
PAYLAŞIM  2x — 32,0 sn · QA paketi 2x kopyayla, ❸ ❹ 1x master'la [qa_paket.sh --hiz 2 --master]
FORMAT    İKİ KEYFRAME ZİNCİRİ · 9 görsel (G0…G8) + 8 I2V · T2V yok
REJİM     S0–S5 B (2 sa) · S6 ⭐ G (gerçek zaman, 8 sn) · S7 ⭐ A (10 dk, GECE) — üç rejim
IŞIK      TEK GÜN: 06:30 → 08:30 → 10:30 → 12:30 → 14:30 → 16:30 → 18:30 → 18:30 + 8 sn → 18:40 + 8 sn (güneş saati) ·
          40° kuzey · δ 0° · güneş 95°/+5,7° → 277°/−7,6° · kamera GÜNEYE bakar, tilt 20° aşağı · final GECE BAŞI (sahip
          kararı): gök koyu lacivert ama renk, ışığın tamamı çanağın İÇİNDEN
AİLE      İÇ MEKÂN (YAYIN_PLANI §3'te yok — öneri KÜTLE, sahip kararı) · ufuk %74,3 tuğlanın içinde · gök yalnız cam çatı şeridinde
TAKVİM    yok — tek gün (haftalık iş sıkıştırıldı, beyanlı); zaman taşıyıcısı kemer lekelerinin sağdan sola süpürmesi
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 kanit.jpg          (2x paylaşım kopyasında: -ss 31.0)

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① ÜÇ ESKİ LAMBA YANIK — sol çanak duvarında (x %24,5 / %28,9 / %31,9 · y %37,1 / %43,4 / %47,9 · Ø 47/39/33 px) açık
    TURKUAZ, her birinin çevresindeki çinide yumuşak turkuaz yelpaze; kadrajın en parlak üç noktası
  ② CAM KOŞUDA MAVİ ÇİZGİ — zeminin ortasında (x %44,3–55,7 · y %31,7–44,6 · 123 × 247 px) camın altından yanan
    lacivert kulvar şeridi; telefon boyutunda açıklamasız okunur
  ③ BİTMİŞ ODA — meşe zemin, sağ duvar boyunca krem kanepe (x %69,5–78,4), koşunun ucunda sehpa, kanepenin uzak ucunda
    SICAK yanan lambader (abajur y %55,9), sol uzak köşede bitki
  ④ TANIKLAR + GECE — coping altında kesintisiz kobalt bant · üst iki çini basamak + meşede 3. basamağın çini
    şeridi · cam çatı ve üç kemer KOYU LACİVERT (siyah değil, kemer kenarları tuğladan seçilir) · camlarda odanın soluk
    yansıması · salonda KİMSE YOK, kapı açıklığı karanlık

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 50,0'da (2x: 25,0) ışıklar TEK KAREDE yanıyor olmalı; 48,0'de yanıksa sıra yanlış → S6 atılır. Lambalar sırayla
   ya da "solarak" yanarsa → S6 atılır [ISIK_FINALI §2].
⛔ 52,0–56,0 S6 tutuşu: ışıklar yanık, figür sabit (işlev kanıtı; 2x: 26,0–28,0).
⛔ 56,0–57,0 işçi kameradan UZAKLAŞARAK kapıdan çıkar; 57,0–60,0 gök laciverte iner; ışıklar S7 boyunca SABİT —
   söner, titrer ya da parlaklığı değişirse S7 atılır.
⛔ 60,0–64,0 FİNAL TUTUŞU: oda boş, hiçbir şey değişmez; ihrac_kontrol final tutuşu SSIM ≥ 0,90 [DERS 63].
⛔ Sahne bloğu S7 tutuşuyla biter; ardından YALNIZ kapak kartı (GN'den, erime ≤ 1 sn, tutuşun dışında) — logo,
   müzik, "before/after" YOK. (Yayında: 2,1 sn erime tutuşu örttü · kart GN değil → QA kaydı E01 · E09.)
⛔ Figürün yüzü okunursa ya da ikinci figür belirirse S6 / S7 atılır [P5-b].
⛔ Çanakta SU varsa (G1'den sonra herhangi bir karede) "pool" kelimesi suyu çağırmıştır → kare atılır [plan RİSKLER ②].
⛔ G8'de gök SİYAHSA ya da oda okunmuyorsa DERS 45: final okunur olmalı → G8 yeniden (güneş −6,5°, sahibe sorulur).
⛔ G8'de yıldız, ay, yeni ışık kaynağı ya da camda oda dışında yansıma varsa → ⑧ APPEARED.
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 20°)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | %74,3 — tuğla duvarın içinde (çizgi olarak görünmez) | — |
| ⭐ yakın coping köşeleri (x · y) | %13,4 / %86,6 · %29,8 | ±0,5 puan · DOKUZ KAREDE (nirengi ①) |
| ⭐ servis kapısı (x · y) | %23,7–34,4 · %58,7–72,1 | ±0,5 puan · DOKUZ KAREDE (nirengi ②) · hep AÇIK |
| ⭐ üç kemer tepesi (y · merkez x) | %86,1 · %45 / %59,5 / %73,8 | ±1 puan · DOKUZ KAREDE (nirengi ③) · SAYI 3 |
| ⭐ uzak coping (x · y) | %34,6–65,4 · %55,5 · 333 px | KESİR 333 px ±8 · DOKUZ KAREDE |
| ⭐ kobalt bant alt kenarı (y yakın / uzak) | %26,9 / %54,1 | ±0,5 puan · DOKUZ KAREDE · kesintisiz, rengi sabit |
| ⭐ üç lamba yuvası (x · y) | %24,5 / %28,9 / %31,9 · %37,1 / %43,4 / %47,9 | AYNI YER nesnesi · ±0,5 puan · Ø 47/39/33 px · SAYI 3 |
| uzak duvar dibi | %58,7 · köşeler %20,8 / %79,2 | ±1 puan |
| G0 su yüzü uzak kenar | %53,0 (kot −0,45) | yalnız G0 |
| eski taban uzak kenar | %47,4 | G1–G2 görünür · G3'ten sonra ızgara altında |
| meşe uzak kenar (3. basamak) | %48,0 | G4→ · sonra DEĞİŞMEZ |
| kalan iki basamak | %50,7–55,5 · x %41–59 | G4→ DEĞİŞMEZ · merdivenin üst başlangıcı DOKUZ KAREDE aynı |
| ⭐ kanal / cam koşu (x · y) | %44,3–55,7 · %31,7–44,6 · 123 × 247 px | G3–G4 açık kanal · G5→ cam · BOYUT DEĞİŞMEZ |
| kanepe sırtı (x · y) | %69,5–78,4 · %37,5–49,0 | G6→ · sırt kobalt bandın ALTINDA |
| sehpa / lambader / bitki | %50 · %49,0 / %63,8–64,7 · %44,9–55,9 / %36,4–36,9 · %49,4–57,6 | G6→ · SAYI birer |
| ⭐ işçi G6–G7 (x · y) | %37,5–38,1 · %58,4–67,4 · 172 px | TEK · sırtı kameraya · G8'de YOK |
| palet → sandık (G1–G5) | kapı yanı, x %39 · y %58–62 | G1–G2 palet · G3 boş palet + meşe bağları · G4–G5 sandık · G6–G8 YOK |
| pompa (G0–G1) | %46,6 · %38,3 | G2'den sonra YOK |
| üst band (cam çatı + aşık) | %92,5–100 | gök yalnız burada ve kemer camlarında · güneş diski HİÇBİR karede |

## 3. ⭐ YAPININ İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  bulanık gri-yeşil su −0,45 (2. rıhtın ortası, 1. basma kuru) · üç lamba SU ALTINDA sönük · kobalt bantta eski kot çizgisi ·
    pompa ortada + siyah boşaltma borusu sol coping'den kapıya · yaprak + kasalar suda · iki işçi + boş araba kapı yanında
G1  çanak BOŞ ve nemli · iki birikinti · silt + yaprak · ⭐ lacivert ŞERİT ortada · lambalar kuru sönük, kir halkalı ·
    ⭐ −0,45'te kahverengi tanık çizgi · pompa yerinde · ⭐ streçli kaset paleti kapı yanında takozlarda
G2  TEMİZ, KURU, MAT beyaz çini · şerit net · lamba camları silinmiş · tanık çizgi SİLİNMİŞ · pompa + boru YOK ·
    palet (film kesiliyor) + kova + iki fırça + katlı torbalar
G3  ⭐ koyu kaset IZGARASI (üst −0,92) · 4. basamak + alt rıht örtülü · ortada AÇIK KANAL 3,00 × 0,90 · dibinde şerit ·
    kanal kenarında sönük LED şerit · sağ uzakta gri priz kutusu · boş palet · ⭐ meşe bağları kapı yanında
G4  ⭐ MEŞE zemin (−0,90 = 3. basma) · 3. basamak meşede ÇİNİ ŞERİT · kanal açık, meşe lip · pirinç priz plakası ·
    arabada fire + kayış · ⭐ yastıklı cam sandığı kapı yanında
G5  ⭐ CAM KOŞU — üç panel lip üstünde, meşeyle aynı düzlem · şerit camdan GÜN IŞIĞINDA net · açık sandık + iki vantuz ·
    ⭐ arabada üç sarılı kanepe modülü
G6  düz krem KANEPE (sağ duvar) · sehpa (koşunun ucu) · lambader (kanepenin ucu, kablo prize) · bitki (sol uzak köşe) ·
    araba + sandık + ikinci işçi YOK · çevre süpürülmüş · mavi saat, HİÇBİR IŞIK YANMIYOR · kapının sağında TEK işçi
G7  aynı · üç lamba TURKUAZ · cam koşuda MAVİ çizgi · lambader SICAK · işçi eli düğmede · gök G6 ile aynı mavi
G8  aynı oda, üç ışık AYNI parlaklıkta · ⭐ gök KOYU LACİVERT · camlarda odanın yansıması · işçi YOK · kapı karanlık
⛔ SAYIM: çanak 1 · merdiven 1 · kapı 1 · kemer 3 · lamba yuvası 3 (dokuz karede) · kanal/cam (0·0·0·1·1·1·1·1·1 — G3–G4
   açık, G5→ cam, panel 3) · kanepe (0·…·0·1·1·1, modül 3) · sehpa/lambader/bitki (0·…·0·1·1·1) · araba
   (1·1·1·1·1·1·0·0·0) · işçi (2·2·2·2·2·2·1·1·0) · ⛔ halı 0 · su (1·birikinti·0·0·0·0·0·0·0)
⛔ Çanağın SINIRI, coping hattı, kobalt bant, lamba yuvaları, kapı ve kemerler dokuz karede DEĞİŞMEZ; meşe kotu G4'ten
   sonra DEĞİŞMEZ; cam koşu G5'ten sonra yalnız YANAR (G7) ve G8'de AYNI yanar.
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK §4 · DERS 48 · beş soru ②③]

```
S0  su: çanak → dalgıç pompa → boşaltma borusu → servis kapısı · palet: araba → kapı yanı takozlar
S1  pompa + boru: taban → araba → kapı · yaprak + silt: taban → torba → MERDİVEN → araba → kapı
S2  kaset: palet → iki el → MERDİVEN → eski taban (yakından uzağa) · LED + priz: kanal kenarı · meşe bağları: araba → kapı yanı
S3  meşe: bağ → iki el → MERDİVEN → kaset üstü (yakından uzağa) · fire: araba · sandık: araba → takozlar
S4  ⭐ cam: sandık → iki vantuz + iki işçi → MERDİVEN (düz taşınır) → kanalın meşe lip'i · modüller: araba → kapı yanı
S5  modül: araba → MERDİVEN → sağ çanak duvarı · sehpa/lambader/bitki: araba → yerine · kablo → priz · araba + sandık +
    ikinci işçi: → kapı → DIŞARI [MEKANSAL §3 Exit Before Swap]
S7  son işçi: düğme → kapı → DIŞARI (kameradan uzaklaşır) · taşınan malzeme yok
⛔ Vinç YOK — model vinç, kanca ya da tavandan sarkan yük çizerse ⑧ APPEARED.
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı bir önceki karede KAPI YANINDA ya da klibin içinde ARABADA görünür [DERS 48 · 49].
⛔ Aynı anda tek hareketli taşıyıcı: tek araba [DERS 69 · MEKANSAL §4].
⛔ Lambader kablosu prize gitmeden lambader yanmaz [DERS 84]; LED şerit G3'te takılı ve sönüktür.
```

## 5. ⭐ IŞIK / GÖLGE KAPISI [ZAMAN_VE_ISIK §2 · DERS 40]

```
G0     doğrudan leke YOK (95°/+5,7° · pencereye 85° geliş) · cam çatıdan serin ışık · kemerler parlak, iç serin
G1     üç uzun eğik leke SAĞDA (uzak çevrenin sağ yarısı + sağ duvar) (116°/+27,8°)
G2     kısa lekeler uzak çevre + üst basamaklar, pencerenin biraz sağında (147°/+45,1°)
G3     lekeler TAM kameraya doğru: çevre, basamaklar, ızgaranın uzak ucu (192°/+49,4°)
G4     lekeler SOLDA, kapı çevresinde (230°/+37,4°)
G5     uzun ince sıcak lekeler sola uzar, sol duvara tırmanır (255°/+17,0°)
G6–G7  doğrudan güneş YOK (−5,7°) · cam çatı + kemerler koyu mavi · G7'de ışık yalnız lambalardan
G8     GECE BAŞI (−7,6°) · gök koyu lacivert, kemer kenarları seçilir · camlarda üç turkuaz nokta + mavi çizgi yansır
⛔ Lekeler sağdan sola TEK YÖNDE süpürür; geri dönen leke = zaman ters → ❷
⛔ Güneş diski HİÇBİR karede yok [DERS 39] · eşit aydınlatılmış "showroom" iç mekân → ❶ CGI
```

## 6. ⭐ BİR ÇANAK · ÜÇ LAMBA KAPISI [DERS 55]

```
Korpus riski: "swimming pool" → mavi su, kulvar ipi, atlama bloğu, şezlong · "living room" → halı, TV, şömine, ikinci koltuk
① sayım cümlesi her karede POZİTİF (plan §SAYIM KİLİDİ)
② mobilya sayıyla: 1 kanepe (3 modül) · 1 sehpa · 1 lambader · 1 bitki · ⛔ halı yok
③ araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç havuz / kaç lamba / kaç kemer / kaç figür
⛔ G1→ mavi su · ikinci havuz · halı · TV · üçüncü figür · dördüncü lamba → ⑧
⛔ Model G2'de "her şeyi temizler" ve kobalt bandı beyazlatırsa → ⑤ DEVAMLILIK (bant kimlik nesnesidir)
```

## 7. ⭐ REJİM G KAPISI — S6 [SANTIYE_HAREKETI §1 · P5-a…d]

```
· "moves at natural speed" · "Eight seconds pass" · gök ve cam çatı ışığı DEĞİŞMEZ
· TEK figür, sırtı kameraya, yüz yok [P5-b] — iz YOK · figür YÜRÜMEZ, OTURMAZ (DEEP END'den ayrışma)
· hareket eden = el (tuğladan düğmeye) · üç lamba + LED (tek kare) · lambader akkoru (~1 sn ısınma)
· zamanlama: 0–2 el · 2,0 TIK · 2–3 akkor ısınır · 3–4 oturma · 4–8 TUTUŞ (son kare = doruk)
· 48,0 kesmesi (B → G) dikiş: işçiler izden nete — ① / ③ hükmü BEKLENEN [P5-c]
⛔ G6 ≈ G7 durgunluk (hiçbir lamba yanmıyor) → S6 atılır [P5-d]
```

## 7b. ⭐ GECE KAPISI — S7 (rejim A · 10 dk → 8 sn) [ISIK_FINALI §1–§2 · DERS 45]

```
· "Ten minutes pass at nightfall" · "time-lapsed at the same rate" · güneş −5,7° → −7,6°
· 0–1 işçi çıkar (kısa iz, sırtı kameraya) · 1–4 gök koyulaşır, camlarda yansıma belirir · 4–8 TUTUŞ
· 56,0 kesmesi (G → A) ikinci dikiş: duran figür hızlanmış göğe döner — ① / ③ hükmü BEKLENEN
⛔ gök siyah · yıldız · ay · ışıkların sönmesi/titremesi/parlaklık değişimi · ikinci figür → S7 atılır
⛔ G7 ≈ G8 durgunluk (gök aynı, işçi yerinde) → S7 atılır
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–64,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı yok · konuşma yok · salon yankısı yatak
· 0,0 pompa (tını alçalır) · 7,0 araba · 8–16 fırça + torba · 16–24 kaset oturuşu · 24–30 meşe vuruşu · 31,0 sandık ·
  32–37 vantuz + cam · ⭐ 37,0 son panel + yarım saniye sessizlik · 40–46 kumaş + priz klik · ⭐ 50,0 düğme TIK (KARE SENKRON
  ±2 kare) · 50–51 akkor vızıltısı · 51–56 sessiz yankı · 56–57 ayak sesi kapıya uzaklaşır · 57–64 boş salon yankısı
· S0–S5: vuruşlar olaya ±0,5 sn · 64,0'da ses kesilmez, döngüde S0'ın pompasına bağlanır
```

## 9. Zaman ve ışık

```
G0 06:30 95°/+5,7° · G1 08:30 116°/+27,8° · G2 10:30 147°/+45,1° · G3 12:30 192°/+49,4° · G4 14:30 230°/+37,4° ·
G5 16:30 255°/+17,0° · G6 18:30 275°/−5,7° · G7 18:30 + 8 sn aynı · G8 18:40 + 8 sn 277°/−7,6°
(40°K · δ 0° · güneş saati · TÜRETİLMİŞ model)
· gün batımı S5'in içinde: lekeler turuncu, sol duvara tırmanır, söner; cam çatı ve kemerler altından maviye
· lambalar S6'da (gerçek zaman) yanar — G1–G6 kuru ve SÖNÜK, G0'da su altında · S7'de yanık ve SABİT
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      8 × 8,0 — sahip kuralı + sahip istisnası (8. sahne), beyanlı
① / ③ DİKİŞ     48,0 (B → G): işçi izden nete · 56,0 (G → A): duran figürden hızlanmış göğe — beyanlı [P5-c]
① İSTASYON      S2 (beyaz → koyu ızgara) ve S3 (ızgara → meşe): model çanağı YENİDEN ÇİZEBİLİR — pilot (c′) ve günlük
⑤ DEVAMLILIK    renk değişimi (gri-yeşil → beyaz → koyu → meşe → turkuaz) KASITLI; sınır, coping, bant, lamba yuvaları,
                kapı, kemerler DEĞİŞMEZ
⑦ İŞ            S6 ve S7'de inşaat yok (kasıtlı): ödül havuzun kendi ışığıdır, S7 onun gecesidir · G7/G8 ACTIVITY'si
                kasıtlı olarak zayıf
⑦ TEMPO         S6 tutuşu + S7 yavaş kararma arka arkaya (2x'te ~5,5 sn az hareket) — beyanlı risk, plan RİSKLER ⑨
❺ TESLİM        THE DEEP END ile aynı fikrin ikinci yorumu (havuz → gömme oda) — ödül farklı (eski lambalar · figür oturmaz)
①               alt band y %0–25: galeri önündeki terrazzo + yakın kobalt bant — kanıt taşımaz; kanıt kutusu y %25–87
⚠️ AİLE         İÇ MEKÂN — THE DEEP END · THE HIDDEN OASIS · THE VANISHING ROOM ile ARDIŞIK YAYINLANAMAZ
```
