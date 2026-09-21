# 🔍 THE QUIET FIELD — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦ ⑨ ⑪ ⑫).
> Plan: `THE_QUIET_FIELD_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md` (üretimde açılır)

```
FİLM      THE QUIET FIELD · 7 × 8,0 = 56,0 sn · KAPAK KARTI YOK · LOGO YOK · ⛔ MÜZİK YOK (diegetik yatak)
SCENE BLOCK / END CARD    56,0 sn / yok
FORMAT    İKİ KEYFRAME ZİNCİRİ · 8 görsel (G0…G7) + 7 I2V · T2V yok
REJİM     S0–S5 B (2 sa) · S6 ⭐ A (10 dk) — iki rejim, üçüncü yok · rejim C (bütün gece tek klip) REDDEDİLDİ
IŞIK      ⭐ ÇEMBER: 17:20 → 19:20 → 21:20 → 23:20 → 01:20 → 03:20 → 05:20 → 05:30 · 53° kuzey · haziran sonu ·
          günbatımı 21:40 (S2 içinde) · gece S3–S4 · gündoğumu 04:40 (S5 içinde) · final güneşli [DERS 45]
TAKVİM    yerden bir yıl (mayıs → kar → haziran) · kar YALNIZ güneşsiz karelerde (G3–G5)
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① ÇANAK DEVRİLMİŞ — kâsenin İÇİ kameraya bakıyor: elips y ≈ %57–77, yakın rim sırt kreti hizasında (%58),
    uzak rim kulelerin üstünde (%77), odak direği kameraya yatık (tepe %79)
  ② İÇİ GÜNEŞTE — kâsenin sol yarısı sıcak ışıkta, sağ yarısı kendi gölgesinde; gölgeler SOLA (sabah, güneş sağda)
  ③ KULELER · BEŞİK · RAY YERİNDE — kule tepeleri %62,5 · beşik %63 · ray elipsi %20–80 × %38–44; hiçbiri
    çanakla birlikte dönmemiş

⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 54,0'ta çanak HÂLÂ DÖNÜYOR olmalı: 54,0 ve 55,0 karelerinde yakın rim farklı y'de (≈ 1 puan ≈ 20 px);
   55,0–56,0 arasında durur. Duran çanak + duran ekip 54,0'ta = S6 atılır (rejim A'nın 6.–7. dakikası).
⛔ 56,0'da film çanak DURURKEN kesilir; sonrasında kart, logo, fade, müzik YOK.
⛔ Çanak elipsinin GENİŞLİĞİ (x %24–76 ≈ 513 px) S6 boyunca sabit; dönerken çap değişirse ② GEOMETRİ.
```

## 2. Kadraj kilitleri — her karede ölçülür (⚠️ TÜRETİLMİŞ — ön görselleştirmeden sonra ÖLÇÜLÜR · tilt 0 · KAMERA_ISTASYONU §3)

| ne | beklenen | tolerans |
|---|---|---|
| ufuk (y) | %50 | ±0,5 puan · SEKİZ KAREDE DE (tilt 0 kanıtı) |
| ⭐ sırt kreti (y) | %58 | ±1 puan · SEKİZ KAREDE DE · G7'de x %25–75 arası çanağın ARKASINDA (bedel) |
| ⭐ ambar (x · mahya y) | %15–25 · %42 | ±0,5 puan · SEKİZ KAREDE DE (I2V çapası · KESİR nesnesi 106 px ±10) |
| ⭐ saha kabinleri (x · y) | %29 · %34–37 | ±0,5 puan · SEKİZ KAREDE DE |
| çit / sırt eteği (y) | %46 | ±1 puan |
| teleskop ekseni (x) · zemin çizgisi (y) | %50 · %42 | ±1 puan · SEKİZ KAREDE DE |
| ray halkası (G2→) yakın / uzak / yan uçlar | y %38 / %44 · x %20 / %80 | ±1 puan · G2'den G7'ye YERİNDE |
| ⭐ kule tepeleri (G3→) sağ · sol (x · y) | %75 · %25 · %62,5 | ±1 puan · G3–G7 SABİT · bölüm sayısı 5 (80 px/bölüm) |
| ⭐ beşik (G4→) (y) | %63 | ±1 puan · kretin 5 puan ÜSTÜNDE, kretle çakışmaz |
| çanak ZENİT (G5–G6) elips (y) · odak direği tepesi | %66–76 · %79 | ±1 puan · G5 kafes, G6 yüzey — AYNI elips |
| ⭐ çanak G7 elips (y) · direk tepesi | %57–77 · %79 | ±2 puan · yakın rim kret hizasında |
| vinç gövdesi (G2–G5 · x) · bom tepesi | %69 · ≈%59–81 | ±3 puan · G6–G7'de vinç YOK |
| ikinci vinç (yalnız G3 · x) | %31 | G4'te YOK |
| projektör direkleri (G3–G7) | x %23 · %77 (yakın) | ±2 puan · G0–G2'de YOK · G6–G7'de sönük ama YERİNDE |
| kompaund (y) | %28–37 | alt UI bandının (%25) ÜSTÜNDE; istif değişir, kabin değişmez |
| gök bandı | %58–100 | G3–G4 yıldız yayı 30° · G5 sağdan gri · G6–G7 açık soluk mavi · güneş diski HİÇBİR karede |

## 3. ⭐ YAPININ İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  çayır · pegli daire · ÇEYREK yay hendek (sol-ön) · 3 ekskavatör · 2 damper · kazık makinesi merkezde ·
    kompaund: kabinler + ray istifi + donatı (tarpaulin) · kule 0 · vinç 0 · projektör 0 · ambar
G1  TAM halka hendek + donatı kafesleri + kalıp · hafriyat bankı sağda · merkez ayak diz boyu · 2 temel kafesi ·
    pompa kamyonu + mikser · ekskavatörler kompaund kenarında · ot biçilmiş · kule 0 · vinç 0
G2  beton halka + ÇELİK RAY (parlak daire) · 2 temel + boji çerçeveleri · pivot · paletli vinç sağda, ilk
    kafes bölümü 4 sapanda sağ temelin üstünde · kompaundda 5 bölüm + lowbed · anız + balya · son ışık
G3  GECE · 2 kule × 5 bölüm (tepe %62,5) · beşik takozlarda, 2 vinç sapanlarda gergin · 4 projektör yanık ·
    yıldız yayı · KAR · kompaund boş(a yakın)
G4  GECE · beşik KULELERDE (%63) · 1 vinç, ilk kaburga 2 sapanda göbek üstünde · kompaundda 4 kaburga ·
    halka içi sulusepken · kuzey bandı
G5  ŞAFAK BAŞI · kafes kâse zenit (%66–76) + odak direği (%79) · vinç panel demetiyle sağ rimde ·
    kompaundda panel istifleri · projektör yanık, gök sağdan gri · çamur + kar yaması
G6  SABAH · çanak YÜZEYLİ zenit · vinç YOK (tırtıl izi yola) · projektör sönük · manlift + pikap sağ kule
    dibinde · kompaund: kabin + boş palet · yeşil, sis kalkar · gölgeler SOLA
G7  SABAH · çanak 50° DEVRİLMİŞ (%57–77), içi sol yarı güneşte · kuleler · beşik · ray YERİNDE · 2 figür
    sırtı dönük · pikap · yeşil haziran çayırı · kret orta yarısı çanağın arkasında
⛔ SAYIM: kule 2 · bölüm 5+5 · beşik 1 · çanak 1 · halka 1 · ambar 1 · kabin 2 · vinç (0·0·1·2·1·1·0·0)
⛔ Kule yüksekliği G3'ten sonra ARTMAZ; çanak elipsi G5→G6 aynı, G6→G7 döner (genişlik aynı, yükseklik 20 puan)
```

## 4. ⭐ YÜK YOLU KAPISI — S2 · S3 · S4 · S5 [FIZIK_VE_AGIRLIK §4 · DERS 57 · beş soru ②③]

```
S2  bölüm: kompaund sırası → 4 sapan → temel/önceki bölüm üstüne · her bölüm DÜŞEY iner · kanca hep yüklü
S3  ⭐ BEŞİK: 80 m · takozlar → İKİ vinç (tandem) → kule tepesi yataklarına AYNI ANDA · beşik havada DÜZ
    (iki ucu aynı yükseklikte), boy değiştirmez, eğilmez · sapanlar oturduktan SONRA çözülür · ikinci vinç
    bomu İNDİRİP çıkar (kanca kadrajda boş görünmez: bom yatık, kadrajdan çıkarken)
S4  kaburga: kompaund → 2 sapan → göbek · her kaburga göbekten DIŞA doğru · rim en son
S5  panel demeti: kompaund → sapan → kaburgalar · yüzey göbekten DIŞA halka halka
⛔ DERS 57 TESTİ (pilot c): beşik havada (i) boy (540 px) sabit mi (ii) düz mü (iii) hedefte KOPYALANIYOR mu
   (iki beşik) (iv) kulelerin üstüne oturunca kuleler kıpırdıyor mu. Dördünden biri düşerse sahip kararı.
⛔ Hiçbir parça saydamlıktan belirmez: kaynağı (kamyon/kompaund) bir önceki karede görünür [DERS 48].
```

## 5. ⭐ GECE KAPISI — S2 · S3 · S4 · S5 [ZAMAN_VE_ISIK §5 · HAVA_VE_ATMOSFER §4 · DERS 16 · 45]

```
S2  günbatımı 21:40 (≈1,3 sn): gölgeler SÖNER · ≈3,0 sn projektörler SIRAYLA yanar (hep birden DEĞİL) ·
    yıldızlar sonra belirir · kar S2'nin son 2 sn'sinde gelir (takvim yerden)
S3  yıldız yayı 30° (2 sa) — yaylar üst kenarın üstündeki noktaya (kutup yıldızı x %32) merkezli, eş merkezli ·
    ⛔ "kısa iz" değil, DERECE · far izleri kesintisiz beyaz/kırmızı · vinç bom lambası rastgele tek piksel,
    sürekli kırmızı DEĞİL · kuzey ufkunda ince alacakaranlık bandı · havuz gölgeler sert ve SABİT
S4  aynı fizik · kuzey bandı biraz parlar (dip 01:00 geçti) · gök S4'ün SONUNDA sağdan grileşmeye başlar
S5  ≈2,0 sn projektörler SIRAYLA söner · ≈4,0 sn güneş sağda kadraj dışında doğar → gölgeler SOLA DOĞAR ·
    rim önce ışığı yakalar · yıldızlar 2,0'dan önce gitmiş olmalı
⛔ Güneş diski HİÇBİR karede yok (DERS 39): batış az 318° (kadrajın 27° solunda), doğuş az 45° (8° sağında)
⛔ Gece karelerinde LIGHTING "elevation N degrees below the horizon" — kapı sayı arar, sayı var
⛔ Gündüz karelerinde (G0–G2 · G6–G7) KAR YOK; gece karelerinde (G3–G5) güneş gölgesi YOK
⛔ Final (G7) AYDINLIK: sabah güneşi, gölgeler sola [DERS 45]; şafak mavisinde biten final = teslim değil
```

## 6. ⭐ TEK TELESKOP · İKİ KULE · TEK HALKA KAPISI [DERS 55]

```
Korpus riski: "radio telescope" → DİZİ (27 çanak, VLA) · "observatory" → kubbe · "dish" → çanak anteni tarlası
① sayım cümlesi her karede ve her I2V'de POZİTİF ("one telescope with one dish, two towers and one rail ring")
② kompozisyon: çanak %24–76 × %57–79, ikinci çanağa yer yok; sırt kreti ve gök BOŞ
③ araç kapısı ⑨ SAYIM TESTİ: test klibinde kaç çanak / kaç kule / kaç halka / kaç ambar
⛔ Kule bölümü 5 (80 px, sayılır): altıncı bölüm ya da üçüncü kule → ⑧ APPEARED
⛔ G5 kafes → G6 yüzey: model "ikinci kâse" eklerse ⑤ DEVAMLILIK — aynı elips, aynı direk
```

## 7. ⭐ REJİM A KAPISI — S6 [SANTIYE_HAREKETI §1]

```
· "Ten minutes pass" · "time-lapsed at the same rate" · figür bulanık ama okunur, sırtı kameraya
· dönen TEK ŞEY çanak (beşik yatakları çevresinde); kuleler · beşik · ray · ambar · kabinler ± 2 px
· çanak TEK RİJİT GÖVDE: elips genişliği 513 px sabit, yakın rim %76 → %57 (20 puan ≈ 380 px), uzak rim
  %66 → %77, direk tepesi %79 (zenitten 50°'ye eğilirken tepe yüksekliği ≈ aynı — kanıt: direk kameraya yatar)
· ışık 05:20 → 05:30: 5° → 6°, gölgeler sola, çok az kısalır; kâsenin içi döndükçe AYDINLANIR (sol yarı)
· 48,0 kesmesi (B → A): S5'in son 0,5 sn'sinde iz çözülmesi kabul, planlanmaz
⛔ Çanak S6'da "kalkıyor" gibi (yükselerek) dönerse yanlış: eksen SABİT (%63), rim iner/çıkar
```

## 8. Ses — müziksiz teslim kapısı

```
· 0,0–56,0 spektrumda müzik yok: melodi, nabız, akor yastığı → teslim değil
· 150 Hz altı tek taşıyıcı katman yok (telefon hoparlörü) · konuşma/telsiz yok
· 19,0–19,5 dört kontaktör "çak" (projektör) · 28,0 civarı tek çelik oturma sesi · 42,0 jeneratör susar ·
  44,0 ilk kuş · 48,0–49,0 yalnız rüzgâr + kuş · 49,0 motor girer · 55,0 motor durur · 55,0–56,0 rüzgâr
· Görüntü 900×/75×, ses 1×: kare senkron aranmaz; vuruşlar olaya ±0,5 sn
```

## 9. Zaman ve ışık

```
G0 17:20 265°/30° · G1 19:20 288°/15° · G2 21:20 316°/2° · G3 23:20 347°/−11° · G4 01:20 15°/−13° ·
G5 03:20 42°/−7° · G6 05:20 62°/5° · G7 05:30 64°/6°   (53°K · haziran sonu · TÜRETİLMİŞ model)
· gölge YÖNÜ G0–G2 sağa (güneş solda-arkada), G6–G7 SOLA (güneş sağda-önde) — döngü kesmesinde ters yön OKUNUR
· S2: gölge süpürmesi + ışıkların yanması = 2 olay · S5: ışıkların sönmesi + gündoğumu = 2 olay (bütçe tam)
· takvim: G0 mayıs → G1 ot sıraları → G2 anız + balya → G3–G4 kar → G5 çamur + yama → G6 sis + yeşil → G7 haziran
· 24,0 kesmesi (S2 → S3) ışık dikişi: G3 gece; S2'nin son 1,5 sn'si zaten gece — dikişte ışık ATLAMAZ
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM      7 × 8,0 — sahip kuralı, beyanlı
③ ZAMAN         gece iki klip GÖLGESİZ (S3 · S4): taşıyıcı yıldız yayı + far izi + kuzey bandı — ölçülmemiş
③ ZAMAN         bir yıl bir güne (takvim yerden, kar gece) — bilinçli sıkıştırma; EMPTY RIDGE 3 ay ile ölçülmüştü
② GEOMETRİ      76 m parabolik kafes (G5) — model kafesi bozabilir; usta kare + pilot (b) önce
⑧ MADE          beşik tandem kaldırma (S3, gece): DERS 57 · pilot (c) — en yüksek risk
⑤ DEVAMLILIK    G5 kafes → G6 yüzey aynı kâse; G2→G3 vinç 1→2; G3→G4 2→1
⑦ İŞ            S1 · S2 kalabalık (6–7 hareket eden, kapı INFO) — sahip "daha çok iş" istedi, kasıtlı [C1-d]
④ TESLİM        sesli-müziksiz teslim ilk kez: A1-c varsayımı ölçülecek (izlenme süresi)
①               ön çayır y %0–28 boş ot — DİKEY ailesinin bedeli; kanıt taşımaz
```
