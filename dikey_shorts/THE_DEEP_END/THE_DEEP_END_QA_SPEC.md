# 🔍 THE DEEP END — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦ ⑨ ⑪ ⑫).
> Plan: `THE_DEEP_END_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md` (üretimde açılır)

```
FİLM      THE DEEP END · 7 × 8,0 = 56,0 sn · KAPAK KARTI YOK · LOGO YOK · VİDEO ÜSTÜ YAZI YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    56,0 sn / yok · ⛔ öncesi/sonrası karşılaştırma YOK
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok
REJİM     S0–S5 B (2 sa) · S6 ⭐ G (gerçek zaman, 8 sn) — iki rejim, üçüncü yok
IŞIK      TEK GÜN: 08:30 → 10:30 → 12:30 → 14:30 → 16:30 → 18:30 → 20:30 → 20:30 + 8 sn · 40° kuzey · δ 0° ·
          güneş 100°/11° → 280°/−11,4° · kamera KUZEYE ve AŞAĞI bakar (tilt −38°) · final DENİZ ALACASI,
          ışığın tamamı kadrajın İÇİNDEN (perde + kademe armatürleri)
AİLE      ⭐ ZEMİN — ufuk %102,1, gök kadrajda YOK, siluet yok · üst %9,2 karaçam kütlesi
TAKVİM    yok — tek gün (haftalık iş sıkıştırıldı, beyanlı); mevsim taşıyıcısı ışık + çınarın sarısı + düşen yapraklar
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE DÖRDÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① PERDEDE GÖRÜNTÜ — uzak uç duvarında (x %40–60 · y %61,8–68,6 · 208 × 132 px) sakin gri-mavi deniz, alçak
    ufuklu, YAZISIZ; panel kadrajın en parlak yüzeyi
  ② HUZME — projektörden (x %74–79 · y %28–31) perdeye, havuzun boyunca; eksende y %29,5 → %65,1 arası soluk koni
  ③ DÖRT IŞIK ÇİZGİSİ — her nosing altında sıcak amber çizgi: y %38,3 · %49,5 · %56,5 · %61,3; koridor
    basamakları da aydınlık
  ④ OTURAN FİGÜR + TANIK — kademe 2'de, koridorun SOLUNDA (x %38,7–39,4 · y %42,7–47,8) sırtı dönük TEK figür ·
    coping altında kesintisiz turkuaz bant · çimende tramplen (x %40,1–59,9 · y %74,4 · 215 px)

⛔ Dördünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 51,5–52,5'te huzme perdeye ULAŞIYOR olmalı (görüntü açılıyor); 54,0'te oturulmuş ve durgun. Işıklar 48,0'de
   yanıksa rejim/sıra yanlış: S6 atılır.
⛔ 56,0'da film figür otururken kesilir; sonrasında kart, logo, fade, müzik, "before/after" YOK.
⛔ Figürün yüzü okunursa ya da ikinci figür belirirse S6 atılır [P5-b].
⛔ Bahçe (duvar üstü, çimen, çınar) AYDINLIKSA "gizli oda" yok: G7 yeniden. Işık yalnız çukurun içinden gelir.
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt −38°)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | **%102,1 — KADRAJ DIŞI** | gök hiçbir karede görünmez; görünürse ① İSTASYON |
| ⭐ krom korkuluk (x · y) | %80,2–84,0 · %17,0–23,5 | ±0,5 puan · SEKİZ KAREDE DE (nirengi ①) · biçim değişmez |
| ⭐ bahçe duvarı + çit (x · y) | %38–62 · %77,0 / %86,8 / %90,8 | ±1 puan · SEKİZ KAREDE DE (nirengi ②) · BROKEN CLIMB E04 riski |
| ⭐ yakın coping köşeleri (x · y) | %10,4 / %89,6 · %18,3 | ±0,5 puan · SEKİZ KAREDE DE (nirengi ③) |
| ⭐ uzak coping (x · y) | %34,5–65,5 · %69,4 | ±0,5 puan · SEKİZ KAREDE DE |
| ⭐ turkuaz bant (y yakın / uzak) | %16,4 / %67,9 | ±0,5 puan · SEKİZ KAREDE DE · kesintisiz, rengi sabit |
| ⭐ perde yüzeyi (x · y) | %40,0–60,0 · %61,8–68,6 | KESİR 208 px ±8 · G0–G5 çıplak gri, G6→ beyaz panel · BOYUT DEĞİŞMEZ |
| basamak seti (x · y) | %31,2–68,8 · %22,4 | ±1 puan · SEKİZ KAREDE DE |
| dört nosing hattı (y) | %38,3 · %49,5 · %56,5 · %61,3 | ±1 puan · G4'te üçü, G5→ dördü · sonra DEĞİŞMEZ |
| derin taban / eğim (y) | %60,3 · eğim %38,9→%55,0 | G0–G3'te görünür, G4'ten sonra güverte altında |
| ⭐ tramplen G0 (x · y) | %52 · %70,0–72,9 | yalnız G0 |
| ⭐ tramplen G1→ (x · y) | %40,1–59,9 · %74,4 · 215 px | G1–G7'de ÇİMENDE, YERİ DEĞİŞMEZ |
| ankraj plakası + soluk beton (x · y) | %51,9 · %69,9 | G1→ · G6–G7'de perdenin TAM ÜSTÜNDE |
| paslanmaz ızgara (x · y) | %50 · %57,8 | G3–G4 açık · G5→ menteşeli kapak altında (%58,4) |
| projektör (x · y) | %74,2–78,6 · %20,9–31,1 | G6 sönük · G7 yanık · G0–G5 YOK |
| iskele rampası (G1–G5) | sağ kenar · alt ucu %71,3 · %43,7 | G0'da YOK (S0'ın sonunda gelir) · G6–G7'de YOK |
| pompa + hortum (yalnız G0) | %45,0 · %64,3 | G1'den sonra YOK |
| römork (G2–G5) | teras, sağ alt | G6–G7'de YOK (terasta soluk iz) |
| bank / minder (G5→) | kademe 2 ve 3, iki yan | SAYI 4 bank · saksı 8 (6 coping + 2 kademe 4) |
| ⭐ figür G6 / G7 | %50 · %15,6–30,0 / %38,7–39,4 · %42,7–47,8 | TEK · sırtı kameraya |
| üst band (karaçam) | %90,8–100 | koyu kütle · gök YOK · güneş diski HİÇBİR karede |

## 3. ⭐ YAPININ İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  donuk YEŞİL su (−0,35) + yaprak salı · çatlak turkuaz bant · ⭐ TRAMPLEN coping'de suyun üstünde ·
    pompa derin uçta + hortum coping'den terasa · terasta 2 boş çuval + el arabası + hortum yumağı · RAMPA YOK
G1  çukur BOŞ ve ıslak · derin uçta SİYAH yaprak yığını · giderde birikinti · duvarlarda yeşil-siyah yosun +
    soluk eski su bandı · ⭐ TRAMPLEN ÇİMENDE · coping'de soluk beton dikdörtgen + çelik ankraj plakası ·
    ⭐ İSKELE RAMPASI sağda
G2  yaprak YOK · gider açık (silt halkası) · ⭐ temiz gri / yeşil-siyah SERT SINIR havuzun ORTASINDA ·
    yıkayıcı terasta, hortumu rampada · 2 dolu çuval + römork
G3  TEK GRİ kabuk (yosun yok, soluk hayaletler) · dolgulu çatlak çizgileri · uzak duvar dibinde GRİ YALITIM yaması ·
    ⭐ paslanmaz IZGARA · ⭐ DÖRT BANT plastik takoz · terasta larch kirişi + lata istifi · yıkayıcı YOK
G4  ⭐ ÜÇ KADEME larch (nosing %38,3 · %49,5 · %56,5) · kademe 4 ÇIPLAK GRİ + ızgara · son bağ kademe 4'te ·
    ortada 1,0 m KORİDOR BOŞLUĞU AÇIK · talaş + fire
G5  DÖRT kademe + menteşeli kapak · sığ basamaklı KORİDOR · 4 BANK + krem minder · SÖNÜK pirinç armatürler ·
    8 saksı · ⭐ UZAK UÇ DUVARI HÂLÂ ÇIPLAK GRİ · yüklü römork · rampa
G6  ⭐ BEYAZ PERDE panel (208 px) · SÖNÜK projektör taş kaidede · rampa + römork + çuval + istif YOK · teras
    süpürülmüş · deniz alacası, HİÇBİR ŞEY YANMIYOR · basamak başında TEK figür, eli korkulukta
G7  aynı · her nosing'de SICAK AMBER ÇİZGİ · huzme havuz boyunca · perdede sakin gri-mavi DENİZ ·
    kademe 2'de OTURAN figür · huzmede düşen yapraklar
⛔ SAYIM: havuz 1 · basamak seti 1 · korkuluk 1 · perde (0·0·0·0·0·0·1·1) · projektör (0·…·0·1·1) ·
   bank (0·…·0·4·4·4) · saksı (0·…·0·8·8·8) · kademe (0·0·0·0·3·4·4·4) · rampa (0·1·1·1·1·1·0·0) ·
   römork (0·0·1·1·1·1·0·0) · tramplen (1·1·1·1·1·1·1·1 — G0 coping'de, sonra çimende) · figür net (0·…·0·1·1)
⛔ Havuzun SINIRI ve coping hattı sekiz karede DEĞİŞMEZ; dört nosing hattı G5'ten sonra DEĞİŞMEZ; perde G6'dan
   sonra yalnız YANAR (G7).
```

## 4. ⭐ YÜK YOLU KAPISI [FIZIK_VE_AGIRLIK §4 · DERS 48 · beş soru ②③]

```
S0  su: havuz → dalgıç pompa → hortum → bahçe gideri · tramplen: coping → el (iki kişi) → çimen ·
    rampa: teras → yakın coping → sığ taban
S1  yaprak + silt: derin uç → kürek → çuval → el arabası → RAMPA → teras → römork · yıkayıcı: teras → hortum → rampa
S2  ızgara: teras → rampa → gider (eski kapak ters yönde çıkar) · takoz: istif → rampa → taban (dört bant)
S3  ⭐ larch: teras → RAMPA (yuvarlanarak) → tabanda istif → takoz üstünde kiriş → kiriş üstünde lata
S4  bank: teras → rampa → kademe 2 ve 3 (vidalı) · minder: bank üstü · armatür: nosing altı · saksı: coping + kademe 4
S5  ⭐ perde: teras → rampa (YAN çevrilerek, iki kişi) → larch çıta çerçevesi (önce çakılır) · projektör: teras →
    taş kaide · rampa: tahta tahta sökülür → römork · römork → bahçe kapısı
⛔ Vinç YOK (çukur) — model kule/mobil vinç çizerse ⑧ APPEARED.
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı bir önceki karede TERASTA ya da klibin içinde RAMPADA görünür [DERS 48].
⛔ Perde hiçbir karede 208 px'den büyük ya da küçük değildir — rampada yan çevrilirken bile aynı panel.
⛔ Armatürler G5'te TAKILI ve SÖNÜK, perde G6'da TAKILI ve SÖNÜK: ışık kaynağı yanmadan önce kadrajda vardır.
```

## 5. ⭐ GÖLGE KAPISI [ZAMAN_VE_ISIK §2]

```
G0–G1  gölgeler YUKARI-SOLA (güneş arkadan-sağdan, 100°→123°) · G0 sıyırıcı: yosun ve fayans dokusu kabartılı
G2     gölgeler TAM YUKARI, en kısa (157°, el 48°) · gri kabuk düz okunur
G3     gölgeler yukarı ve hafif SAĞA (203°, el 48°)
G4–G5  gölgeler SAĞA uzar (237°→260°) · ⭐ G4'te her kademe bir alttakine gölge atar — kademeler burada "doğar" ·
       G5 turuncu sıyırıcı: bank sırtları ve minderlerde keskin gölge bantları
G6–G7  doğrudan güneş YOK (−11,4°) · gölge yalnız armatürlerden ve huzmeden
⛔ Güneş diski HİÇBİR karede yok: kadrajın üst kenarı ufkun 1,14° ALTINDA ve güneş az 100°–280°, kadraj bandı
   333,4°–26,6° [DERS 39] — dikey ve yatay olarak iki kez dışarıda
⛔ GÖK hiçbir karede görünmez (ufuk %102,1). Görünürse ① İSTASYON: tilt kaymıştır.
⛔ Döngü kesmesi (G7 → G0): deniz alacasından sabah güneşine — okunur, beklenir
```

## 6. ⭐ BİR HAVUZ · BİR PERDE KAPISI [DERS 55]

```
Korpus riski: "outdoor cinema" → şezlong sırası, ip ampul, kalabalık, hoparlör kulesi · "swimming pool" → MAVİ su,
şişme oyuncak, ikinci havuz · "garden" → mobilya seti, havuz barı
① sayım cümlesi her karede POZİTİF ("one rectangular swimming pool with one flight of steps at the near end,
  one chrome handrail and one screen on the far end wall, and the only pool in view")
② mobilya sayıyla (4 bank · 8 saksı · 1 projektör) · perdedeki görüntü YAZISIZ · derinlik rakamı YOK
③ araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç havuz / kaç bank / kaç figür / kaç perde
⛔ İkinci havuz · şezlong · ip ampul · hoparlör · üçüncü figür · MAVİ su → ⑧
⛔ Model G2–G3'te "her şeyi temizler" ve turkuaz bandı da beyazlatırsa → ⑤ DEVAMLILIK (bant kimlik nesnesidir)
```

## 7. ⭐ REJİM G KAPISI — S6 [SANTIYE_HAREKETI §1 · P5-a…d]

```
· "moves at natural speed" · "Eight seconds pass" · gölge KIPIRDAMAZ · karaçamlar durur
· TEK figür, sırtı kameraya, yüz yok [P5-b] — iz YOK
· hareket eden = figür (el → anahtar, koridordan iner, oturur) · armatürler (SIRAYLA yanar) · projektör lambası ·
  huzme (açılır, perdeye ulaşır) · perdedeki görüntü (yavaş) · düşen yapraklar
· zamanlama: 0–1 anahtar · 1–2,5 armatürler sırayla · 2,5–3,5 lamba + koni · 3,5–4,5 huzme perdeye + deniz ·
  4,5–7 figür iner · 7–8 oturur (son kare = doruk)
· 48,0 kesmesi (B → G) dikiş: figür izden nete — ① / ③ hükmü BEKLENEN [P5-c]
⛔ Işık perdeye projektör yanmadan düşerse ⑩ SEBEP · armatürler tek seferde yanarsa ritim ölür → S6 atılır
⛔ G6 ≈ G7 durgunluk (hiçbir lamba yanmıyor) → S6 atılır [P5-d]
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–56,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı yok · konuşma yok · perdedeki dalga sesi GENİŞ BANT, sabit seviye, döngüsüz
· 0,0 pompa (tını alçalır) · 6,0 cıvata · 8–14 yaprak küreme + el arabası · 14–21 jet (tını uzaklaşır) ·
  21,5 taşlama · 23,0 ızgara çınlaması · 24–31 vidalama + tahta · 32–40 bank + minder + tornavida ·
  41,0 panel tınısı · 42,5 matkap · 44,0 rampa çeliği · 46,0 römork · ⭐ 48,5 anahtar "tık" · 49,0–50,5 armatür
  vızıltısı SIRAYLA · 51,0 projektör fanı · 52,0 dalga sesi açılır · 52,5–55,0 güvertede ayak sesi (uzaklaşır) ·
  55,2 bank gıcırtısı — S6'da görüntü 1×: KARE SENKRON aranır (±2 kare)
· S0–S5: vuruşlar olaya ±0,5 sn · 56,0'da ses kesilmez, döngüde S0'ın pompasına bağlanır
```

## 9. Zaman ve ışık

```
G0 08:30 100°/11° · G1 10:30 123°/33° · G2 12:30 157°/48° · G3 14:30 203°/48° · G4 16:30 237°/33° ·
G5 18:30 260°/11° · G6 20:30 280°/−11,4° · G7 20:30 + 8 sn aynı
(40°K · δ 0° ekinoks · saat = güneş saati + 1 sa 30 dk · TÜRETİLMİŞ model)
· gölge YÖNÜ G0–G1 yukarı-sola, G2 tam yukarı, G3–G5 sağa, G6–G7 yapay ışık
· S5 içinde gün batımı: turuncu kademe yüzlerinden YUKARI çekilir → çukur maviye soğur → bahçe siyaha iner
· armatürler ve projektör S6'da (gerçek zaman) yanar — S5'te TAKILI ve SÖNÜK
· gök taşıyıcısı YOK (ufuk kadraj dışı); I2V'lerde gök tek cümleyle dışarıda tutulur
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      7 × 8,0 — sahip kuralı, beyanlı
① / ③ DİKİŞ     48,0 (B → G): figür izden nete — beyanlı [P5-c]
① İSTASYON      S3'te gri kabuk ahşap kademeye döner: model havuzu YENİDEN ÇİZEBİLİR (sınır, coping, korkuluk) —
                pilot (c). Ayrıca S2'de "her şeyi temizler" riski turkuaz bandı tehdit eder
⑤ DEVAMLILIK    renk değişimi (yeşil → gri → larch → amber) KASITLI; havuz sınırı, coping, turkuaz bant, basamak,
                korkuluk, duvar, çit DEĞİŞMEZ
⑧ MADE          yıkayıcı S1 içinde terasa gelir (kaynağı kadraj dışı sağ, beyanlı); ızgara ve takozlar S2'de iner
⑦ İŞ            S6'da inşaat yok (kasıtlı): ödül yapının kendi ışığıdır [P8-f]. G7 ACTIVITY'si de zayıftır ve
                KASITLIDIR: saha bitmiştir, hareket eden yalnız huzme, perdedeki görüntü ve düşen yapraklardır
③ ZAMAN         gece finali: model bahçeyi de aydınlatırsa "gizli oda" kaybolur → G7 yeniden
④ TESLİM        beşinci müziksiz film · BROKEN CLIMB ④ dersi: 56,0 sn, kart yok, master'a yazı basılmaz
①               alt band y %0–25 (alt UI) yakın coping + basamak + korkuluk + projektör kaidesi + figürün bacakları —
                KASITLI: aşağı bakan istasyonda yakın kenar oradadır; kanıt kutusu y %25–87
⚠️ AİLE         ZEMİN — THE HIDDEN OASIS ile ARDIŞIK YAYINLANAMAZ (aynı aile VE aynı konu: havuz dönüşümü)
```
