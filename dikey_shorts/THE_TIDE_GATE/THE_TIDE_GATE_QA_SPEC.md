# 🔍 THE TIDE GATE — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦ ⑨ ⑪ ⑫).
> Plan: `THE_TIDE_GATE_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md` (üretimde açılır)

```
FİLM      THE TIDE GATE · 7 × 8,0 = 56,0 sn · KAPAK KARTI YOK · LOGO YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    56,0 sn / yok
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok
REJİM     S0–S5 B (2 sa) · S6 ⭐ G (gerçek zaman, 8 sn) — iki rejim, üçüncü yok (A YOK)
IŞIK      TEK GÜN: 06:15 → 08:15 → 10:15 → 12:15 → 14:15 → 16:15 → 18:15 → 18:15 + 8 sn · 48° kuzey · δ +15° modeli ·
          güneş 83°/14° → 283°/9° · kamera KUZEYE bakar · final alçak güneş fırtına bulutunun ALTINDA [DERS 45]
TAKVİM    BİR YIL — burun bitkileri (ölü eğrelti → sarı karaçalı → genç eğrelti → ilk funda → mor funda → pas eğrelti)
          + gök (fırtına → açık → ufukta bant → fırtına) [P1-c]
SU KOTU   her G karesinde kilitli: +6,0 · −3,0 · 0,0 · +3,0 · 0,0 · +2,0 · dış +5,5 / iç +2,0 · aynı
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 kanit_a.jpg
ffmpeg -ss 55.8 -i teslim.mp4 -frames:v 1 kanit_b.jpg

55,8 KARESİNDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① KÖPÜK SÜTUNU KAPAKLARIN ÜSTÜNDE — beyaz sütun set bandının (x %33–67) üstünden kule tepelerini (%58,1) ve
    ufku (%59,4) AŞMIŞ, ≈ %62–66'ya kadar göğe karşı; batı yüzü turuncu-beyaz
  ② İKİ KAPAK KAPALI, ÜÇ KULE AYAKTA — x %28–72'de üç kule (52 px en, sayılır), aralarında iki kapalı kapak;
    kapak / kule / kol 48,0'daki yerinden ± 2 px
  ③ İÇERİSİ DÜZ, RIHTIM KURU — liman suyu (y %20–49) koyu ve dalgasız (yalnız rüzgâr pürüzü); rıhtım üstü kuru; evlerin
    yüzünde kahverengi taşkın çizgisi (y ≈ %42,7) suyun 4 m ÜSTÜNDE; sarı muşambalı figür liman başında sırtı dönük

54,0 KARESİ: patlamadan ÖNCE — kabarma ağza yaklaşıyor, dikleşmiş, tepesi beyaz; kapakların önünde su çekilmiş.
⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 54,0 ve 55,8 AYNI görünüyorsa (patlama yok) S6 atılır — rejim G'nin durgunluk riski [P5-d].
⛔ Patlama İÇ LİMANA TAŞARSA (köpük kapakları aşıp içerideki suyu dalgalandırırsa) S6 atılır: kanıt içerinin DÜZ kalmasıdır.
⛔ 56,0'da film köpük YÜKSELİRKEN kesilir; sonrasında kart, logo, fade, müzik YOK.
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt −8°)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | %59,4 | ±0,5 puan · SEKİZ KAREDE DE (tilt −8° kanıtı) |
| ⭐ nişan taşı (x · y taban/tepe) | %13,8 · %71,6–74,5 | ±0,5 puan · SEKİZ KAREDE DE (nirengi ①) |
| ⭐ ufuk × doğu burun ağız yüzü (x) | ≈ %70 | ±1 puan · SEKİZ KAREDE DE (nirengi ②; G3'ten sonra doğu kulenin DOĞUSUNDAN okunur) |
| ⭐ liman feneri (x · y taban/tepe) | %74,5 · %44,3–50,0 | ±0,5 puan · SEKİZ KAREDE DE (nirengi ③ · KESİR 57 px ±6) |
| ⭐ rıhtım evleri (x · y taban/mahya, yakın) | %11–26 · %41,5 / %50,5 | ±1 puan · SEKİZ KAREDE DE ("aynı yer" nesnesi) |
| ⭐ taşkın çizgisi (G1→) | yakın evlerde y ≈ %42,7 · yatay · kahverengi | ±0,5 puan · G1–G7 AYNI; G0'da çizgi yerine SU |
| burun tepeleri (y) | %71,3 (her iki yan) | ±1 puan |
| ⭐ ağız / set hattı (x · y su hattı) | %27,8–72,2 · %49,0 (MSL) | ±1 puan · G0–G2 çıplak ağız |
| ⭐ kuleler (G3→) x · tepe y · kabin y | %28–33 · %47,5–52,5 · %67–72 · %58,1 · %60,7 | ±1 puan · her kule 52 px ±5 · SAYI 3 |
| kapak AÇIK (yalnız G5) | y %56,8–60,2 (ufku keser) | ±1 puan · 156 px en · SAYI 2 |
| kapak KAPALI (G4 batı · G6–G7 ikisi) | tepe y %52,7 | ±1 puan · fırtınada suyun üstünde ≈ 29 px |
| batardo halkaları (G2–G3) | x %28–33 · %46–54 · %67–72 · su hattının +2 m üstü | SAYI 3 · G4'te YOK (soluk yara) |
| jack-up (G1–G3) gövde / bacak tepesi | %60 · %52,3 / %61,5 | 4 bacak · G4'te YOK |
| sheerleg (G3–G4) A-çerçeve tepesi | %56 · %71,3 | G5'te YOK |
| tekneler | x %42–59 · y %38–43 | SAYI 3 · SEKİZ KAREDE DE (G1'de çamurda) |
| ⭐ figür (G6–G7) | x %58,4 · y %30,3–32,7 · 46 px | TEK · sırtı kameraya · yüz yok |
| gök bandı | %59,4 üstü + burunlar | B'de streak · G'de hold/roll · güneş diski HİÇBİR karede |

## 3. ⭐ YAPININ İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ağız ÇIPLAK · su +6,0 rıhtımın üstünde, ev önleri pencere denizliğine kadar · köpük şeritleri içeri · 3 tekne ipte
    (biri rıhtıma yatık) · yüzen enkaz · pompa · kule 0 · kapak 0 · makine 0
G1  LW −3,0 · tekneler ÇAMURDA ayaklarında · ⭐ TAŞKIN ÇİZGİSİ doğdu · jack-up doğu yarıda (4 bacak) · palplanş barcı
    yanında · kancada TEK palplanş (dik, ağız ortası) · halka 0
G2  3 KURU HALKA (batı · orta · doğu) + donatı kafesleri · jack-up orta–doğu arası · skip orta halka üstünde · 2 hortum ·
    su 0,0 · tekneler yüzüyor
G3  3 KULE (+22, kabinli) · halkalar diplerinde · son kalıp doğu kule tepesinde · jack-up doğu açıklıkta (çekiç halka
    palplanşında) · SHEERLEG dışarıda, KAPAK 1 barcın hemen üstünde · HW +3,0
G4  KAPAK 1 KAPALI batı açıklıkta · doğu açıklık açık · halka YOK · jack-up + barç YOK · sheerleg dışarıda, KAPAK 2
    barcın hemen üstünde · su 0,0
G5  İKİ KAPAK AÇIK (visor, kuleler arasında yatay) · silindirler kule yüzlerinde · makine YOK · ufukta fırtına bandı ·
    su +2,0 iki yanda eşit
G6  İKİ KAPAK KAPALI · dış +5,5 gri-beyaz · iç +2,0 düz koyu · figür liman başında · dalga geri çekiliyor
G7  aynı · ⭐ KÖPÜK SÜTUNU kulelerin üstünde
⛔ SAYIM: ağız 1 · kule (0·0·0·3·3·3·3·3) · kapak yerinde (0·0·0·0·1·2·2·2) · kapak kancada (0·0·0·1·1·0·0·0) ·
   halka (0·0·3·3·0·0·0·0) · jack-up (0·1·1·1·0·0·0·0) · sheerleg (0·0·0·1·1·0·0·0) · tekne (3 ×8) · figür (0·…·0·1·1)
⛔ Kule G3'ten sonra DEĞİŞMEZ; kapak G5'ten sonra yalnız DÖNER (açık → kapalı); taşkın çizgisi G1'den sonra DEĞİŞMEZ.
```

## 4. ⭐ YÜK YOLU KAPISI — S0 · S1 · S2 · S3 · S4 · S5 [FIZIK_VE_AGIRLIK §4 · DERS 57 · beş soru ②③]

```
S0  jack-up: römorkörle açık denizden → ağız (bacaklar YUKARIDA gelir, AŞAĞI iner, gövde sudan kalkar) · palplanş: barç → kanca
S1  palplanş: barç → kanca (dik) → vibro çekiç → dip · halkalar batıdan doğuya · hortumla kurutma · donatı: barç → kuru taban
S2  beton: barç → skip → halka · kule kat kat tırmanır kalıpla (ÜÇÜ BİRLİKTE) · sheerleg + barç: ufuk → ağız dışı
S3  ⭐ KAPAK 1: barç → sheerleg kancası → kulelerin ÜSTÜNDEN → batı açıklık (DÜŞEY iner) → alt kenar eşiğe, kollar
    mafsala (pim) · palplanş: dip → barç · jack-up: bacaklar kalkar → römorkörle doğu açıklıktan denize
S4  KAPAK 2: aynı yol → doğu açıklık · silindir: kule yüzü ↔ kol (pim) · sheerleg → denize · ⭐ kapaklar kollarında
    YUKARI döner (silindirle), yüzlerden su akar
S5  ⭐ kapaklar AŞAĞI döner (silindirle), aynı anda suya girer, eşiğe oturur, KİLİTLİ kalır (3,5 sn'den sonra ± 2 px)
⛔ DERS 57 TESTİ (pilot · S3): kapak havada (i) boy ve kavis sabit mi (ii) hedefte KOPYALANIYOR mu (üçüncü kapak)
   (iii) inerken kule kıpırdıyor mu (iv) kapak açıklığa GİRİYOR mu yoksa kulenin önünde mi asılı kalıyor.
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı (barç / römorkör / ufuk) bir önceki karede ya da klibin içinde görünür [DERS 48].
⛔ Sheerleg ağızdan İÇERİ girmez (A-çerçeve kapakların altından geçemez); hep DIŞARIDA (d 205) çalışır.
```

## 5. ⭐ GÖLGE KAPISI — üç yönlü süpürme [ZAMAN_VE_ISIK §2 · HAVA_VE_ATMOSFER]

```
G0–G2  gölgeler SOLA (güneş sağda, 83°→138°) · uzun → kısa · burunların doğu yüzleri aydınlık
G3     gölgeler İLERİ (denize doğru), en kısa (187°, el 57°) · kule yüzleri düz aydınlık
G4–G7  gölgeler SAĞA (232°→283°) · kısa → uzun · kulelerin batı yüzleri aydınlık, doğu yüzleri gölgede
⛔ Güneş diski HİÇBİR karede yok (bearing 0°, güneş 83°–283°: kadraj bandı 333°–27°'nin dışında) [DERS 39]
⛔ Döngü kesmesi (G7 → G0): ışık soldan-turuncudan sağdan-altına atlar, gök fırtınadan fırtınaya — okunur, beklenir
⛔ Final (G6–G7) AYDINLIK: güneş 9°, bulut kenarının ALTINDA; köpük + kule batı yüzleri turuncu-beyaz, gök koyu
   [DERS 45]. Final gri ve gölgesizse G7 yeniden.
⛔ S6 gölge KIPIRDAMAZ (8 sn) — kıpırdarsa rejim yanlış okunmuştur.
```

## 6. ⭐ BİR AĞIZ · ÜÇ KULE · İKİ KAPAK KAPISI [DERS 55]

```
Korpus riski: "storm surge barrier" → Thames bariyeri (10 ayak, gümüş kabuklar) · "harbour" → mendirek / dalgakıran
① sayım cümlesi her karede ve her I2V'de POZİTİF üst sınır ("no more than three towers and two gates … no other
  barrier, bridge or breakwater")
② biçim: "plain grey concrete towers … flat-topped with a small concrete cabin" — kubbe / gümüş kabuk çıkarsa ⑧
③ araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç kule / kaç kapak / kaç ağız
⛔ G0–G2'de kule YOK → model ağza ayak / köprü çizerse ⑧ APPEARED
⛔ Dördüncü kule · üçüncü kapak · ağız dışında ikinci set · limanda mendirek → ⑧
⛔ Tekne 3 (sekiz karede) · halka 3 · jack-up bacağı 4 — fazlası ⑧; tekne eksilirse ⑤
```

## 7. ⭐ REJİM G KAPISI — S6 [SANTIYE_HAREKETI §1 · P5-a…d]

```
· "moves at natural speed" · "Eight seconds pass" · gölge KIPIRDAMAZ · bulut "rolls slowly" / holds
· İNSAN: TEK figür, sırtı kameraya, yüz yok [P5-b] — iz YOK (1×'te fiziksel olarak yoktur)
· hareket eden = deniz (kabarma → patlama → köpük) · teknelerin hafif sallanması · iç suyun ürpermesi — YAPI KIPIRDAMAZ
· zamanlama: 0–2 geri çekilme · 2–5 kabarma gelir · ≈ 5,5 PATLAMA · 5,5–8,0 sütun yükselir (son kare = doruk)
· 48,0 kesmesi (B → G) filmin dikişi: deniz ipekten dalgaya, figür izden duruşa döner — ① / ③ hükmü BEKLENEN [P5-c]
⛔ Köpük hızlandırılmış görünürse (sütun 1 sn'de kalkıp iner) rejim yanlış: klip atılır
⛔ G6 ≈ G7 durgunluk (patlama yok) → S6 atılır, G6 kabarması daha açıkta yazılır [P5-d]
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–56,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı katman yok (dalga gürlemesi köpük hışırtısıyla çiftli) · konuşma / telsiz yok
· 0,0–2,0 fırtına + ağızdan giren su · 7,0 bacaklar dibe · 8,0–16,0 vibro çekiç nabzı · ~27,0 kapak eşiğe (tek derin
  vuruş) · 37,0–39,0 kapakların kalkışı (hidrolik + akan su) · 41,0–43,5 iniş + 43,5 kilit "gümm" · 44,0→ fırtına ·
  ⭐ 53,5 PATLAMA — S6'da görüntü de 1×: KARE SENKRON aranır (±2 kare)
· S0–S5: görüntü 900×, ses 1× — vuruşlar olaya ±0,5 sn
· 56,0'da ses kesilmez / fade yok — döngüde S0 rüzgârına bağlanır
```

## 9. Zaman ve ışık

```
G0 06:15 83°/14° · G1 08:15 106°/33° · G2 10:15 138°/51° · G3 12:15 187°/57° · G4 14:15 232°/47° ·
G5 16:15 261°/29° · G6 18:15 283°/9° · G7 18:15 + 8 sn 283°/9°   (48°K · δ +15° · yerel güneş saati · TÜRETİLMİŞ model)
· gölge YÖNÜ G0–G2 sola, G3 ileri, G4–G7 sağa — döngü kesmesinde sol ↔ sağ OKUNUR
· S6 gölge kıpırdamaz (8 sn); G6 ve G7 LIGHTING aynı açılar
· bulut: S0 dağılır · S1–S4 streak · S5 fırtına ufuktan koşar · S6 yavaş yuvarlanır — I2V'lerde yazılı
· ⚠️ sonbahar fırtınası + yaz güneş geometrisi BEYANLI tutarsızlık (plan tasarım kararı ⑧)
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      7 × 8,0 — sahip kuralı, beyanlı
① / ③ DİKİŞ     48,0 (B → G): deniz dokusu ve figür değişir — beyanlı [P5-c]
⑧ MADE          kapak ×2 sheerleg'den kulelerin ÜSTÜNDEN (DERS 57); kuleler S2'de üçü birden sudan yükselir
⑤ DEVAMLILIK    su kotu her karede farklı (kasıtlı, kilitli) — kot değişimi DEVAMLILIK hatası DEĞİLDİR; taşkın çizgisi,
                fener, evler, burunlar DEĞİŞMEZ. G0→G1 9 m iniş S0 içinde (kabarma + ebb, beyanlı sıkıştırma)
② GEOMETRİ      set bandı yalnız 175 px boy: model kuleleri uzatabilir (Thames korpusu) — kule tepesi %58,1 ± 1 puan
⑪ FİZİK         kapalı kapak dış suyu tutarken iç suyun AYNI kotta kalması (S5): model iki yanı "tek deniz" diye
                eşitleyebilir — kot farkı 27 px, KANIT DEĞİL; kanıt doku (beyaz dış · düz iç)
⑫ KATILIK       S6'da kapak / kule dalgayla eğilir mi — ± 2 px
⑦ İŞ            S5–S6'da makine yok (kasıtlı): ödül yapının işi; S5'te ekip iner, figür gelir [P8-f]
④ TESLİM        sesli-müziksiz teslim üçüncü kez: P8-e ölçümü tekrar
①               rampa + çatılar y %0–20 — alt UI bandı; kanıt taşımaz. Doğu burnu x > %80 — sağ UI bandı.
```
