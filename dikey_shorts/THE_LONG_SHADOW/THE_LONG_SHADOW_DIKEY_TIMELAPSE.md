> # ⛔ BU DOSYA **v1**'DİR — ÜRETİLDİ, ÖLÇÜLDÜ, DÜŞTÜ. YENİDEN ÜRETME.
>
> Dört merceğin dördü de hüküm düşürdü:
> `① ALTI AYRI GÖRÜNTÜ` · `② FARKLI · APPEARING` · `③ GEÇİYOR (yön kırık)` · `④ DURUYOR · NONE FOUND`
> Skorlar 3,3 / 0,4 / 4,3 / 2,7 · kayıt: `QA/ARSIV_12_MERCEK/RAPORLAR/THE_LONG_SHADOW.md`
>
> **Kök sebep:** ters inşa üretim sırası koşulmadı → altı kare bağımsız
> üretildi → üç farklı bina [DERS 5]. Yeniden kurgu, renk ya da müzik bunu
> KURTARMAZ; düşen şey teslim değil ÜRETİM SIRASIDIR.
>
> **Bu dosya kanıt olarak duruyor.** v2 yeni ızgarayla yazılacak:
> 10 sahne × 6 sn + 5 sn kapak kartı = 65 sn · ters açılış YOK · kış İKİ
> sahne · zincirli üretim KAPI · başlıklı İngilizce kapak.
> Zorunlu değişiklikler: `QA/ARSIV_12_MERCEK/RAPORLAR/THE_LONG_SHADOW.md` §7 · `DERSLER 3-9`
>
> ⛔ Prompt kapısı bu dosyada artık BLOCK veriyor (TESLİM YAPISI beyanı yok) —
> bu doğrudur ve düzeltilmez; dosya arşivdir.

---

# 🌇 THE LONG SHADOW — Uzayan Gölge

Dikey Timelapse Production Document
Format: **9:16 (DİKEY)** | Sahne: 6 (Kanca + 5 aşama) | Süre: her sahne **10 sn**, toplam **60 sn**
Prompt yapısı: her sahne için **1 görsel + 2 video promptu** (I2V birincil · T2V yedek)
Yapı: **şehir içi kule** (`YAPI_TIPI_KARTLARI` §1) · Saha: **şehir içi dar parsel** (`SAHA_VE_IKLIM` §3.1 + §3.5 kar eki)
Zaman yayı: **14 ay → 60 saniye**
Kamera mimarisi: **hibrit** — 4 ana istasyon + 2 detay (`KAMERA_ISTASYONU` §1)

_"Boş bir arsa on sekiz kat yükseldi. Ve karşı bloğun güneşini aldı."_

---

## 🚪 KONSEPT KAPISI

```
VAAT:    Yıkımdan kalmış dar bir arsaya 18 katlı bir kule dikilecek.
         (video başlamadan önce de var olan iş — birinin sözleşmesi)
DİRENÇ:  Parsel dar ve komşuya sıfır: her şey tek vinçten geçmek zorunda.
         Üstüne bir kış giriyor ve kat döngüsü 5 günden 9 güne çıkıyor.
BEDEL:   ⭐ Karşıdaki beş katlı tuğla bloğun ikindi güneşi. S0'da o cephe
         baştan sona aydınlık; S5'te kulenin gölgesi tam üstünde duruyor.
         Kimse bir şey söylemiyor — kadraj söylüyor.
```

### Üç kabul testi

```
① TEK KARE TESTİ        ✅ Tek donmuş karede (a) bir kule yapıldığı ve
                        (b) kaç kata gelindiği, karşı bloğun çatı hizasına
                        ve arkadaki sırt hattına bakılarak 1 saniyede okunur.
② KİNETİK BAĞIMSIZLIK   ✅ Değişimin tamamı sabit bir kadrajda görülür:
                        gölge süpürür, kat belirir, cephe tırmanır.
                        Metin yok, anlatıcı yok, tarih kartı yok.
③ BAŞLIK ŞEMASI         ✅ "Kimin güneşini aldı?" (≤5 kelime)
```

⛔ **VAAT KONTROLÜ:** "yükseliyor / büyüyor / tamamlanıyor" yazılmadı —
bunlar formatın kendisidir. Vaat bir İŞTİR, bedel bir KAYIPTIR.

---

## 🔒 DEĞİŞMEZLER TABLOSU

> ⛔ Bu dört kutu altı GÖRSEL promptta **birebir, kısaltmasız** tekrarlanır.
> Köşeli parantez atfı yasak — model belgeyi okumaz, promptu çizer [D-a].

```
┌─ KAMERA İSTASYONU (ANA) ────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100                         │
│ yükseklik     24,0 m — güneybatıdaki bloğun çatı parapeti           │
│ mesafe        yapının güneybatı yüzünden 72 m                       │
│ bakış açısı   035° (kuzeydoğu) · tilt 0° · roll 0°                  │
│ sabitleme     bolted to a fixed tripod, absolutely zero movement    │
│ ⛔ Sayılar seçilmedi, KAMERA_ISTASYONU §3'ten türedi:                │
│    D = (H − h) / 0,48  →  (58,7 − 24) / 0,48 = 72,3 ≈ 72 m          │
│ ⛔ Bakış KUZEYDOĞUdur: ikindi güneşi kameranın ARKASINDA kalır,      │
│    yapı önden aydınlanır ve gölgeler doğu-kuzeydoğuya, yani KARŞI   │
│    BLOĞUN ÜSTÜNE düşer. Filmin bedeli bu açı seçiminden doğuyor.    │
└─────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — üç tane, isimlendirilmiş ────────────────────┐
│ ① kadrajın SAĞINDA beş katlı kırmızı tuğla apartman, çatısında iki  │
│    baca, çatı sırtı yerden 15,5 m                                   │
│ ② kadrajın SOLUNDA tek bir servi ağacı, gövdesi hafif eğik, 19 m    │
│ ③ ARKADA alçak bir sırt hattı, üzerinde dağınık alçak yapı silueti  │
│ ⛔ Üçü de HER karede aynı yerde, aynı boyutta, aynı şekildedir.      │
│    Timelapse'i timelapse yapan şey yapının değişmesi DEĞİL,          │
│    arkasındakinin değişmemesidir.                                    │
│ ⭐ ① aynı zamanda filmin BEDELİDİR — S0'da aydınlık, S5'te gölgede.  │
└─────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ──────────────────────────────────────────────────┐
│ ufuk çizgisi   kare yüksekliğinin tam %50'sinde — tilt 0° geometrisi│
│ yapı tabanı    %27,8   ·   yapı tacı (58,7 m) %82,1                 │
│ tuğla blok sırtı %42,1  ·  servi tepesi %45,4  ·  sırt hattı ~%47   │
│ şantiye sınırı mavi panel çit, kadrajın %25-28 bandında             │
│ yol            sağ alt köşeden kadraja giren asfalt, sabit          │
└─────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — tamamlanmış hâlin sabit geometrisi ──────────────────┐
│ kat sayısı     18                                                   │
│ oturum         24 × 18 m                                            │
│ kat yüksekliği 3,20 m → çatı 57,6 m · parapet 1,10 m → taç 58,7 m   │
│ aks düzeni     6 × 4 kolon, 4,0 m aralık                            │
│ çekirdek       kuzeydoğu köşede tek betonarme çekirdek              │
│ cephe          antrasit alüminyum çerçeve + açık gri cam            │
│ taç            düz çatı · 1,10 m parapet · tek mekanik hacim        │
│ ⛔ Bu satırlar S0'da da geçerlidir: S0'da bina YOKTUR ama ters       │
│    üretimin referansı budur ve S0 bu binadan geriye inilerek üretilir│
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📐 KADRAJ DEFTERİ — her sayı iki girdiden türedi

Formül (`KAMERA_ISTASYONU` §3): `kare yüzdesi = %50 + f × (y − h) / (36 × D)`
Bu filmde `f = 24`, `h = 24,0`, `D = 72` → **kare yüzdesi = %50 + (y − 24) / 108**

| Ne | Yükseklik y | Kare yüzdesi | Nerede kullanılır |
|---|---:|---:|---|
| çukur tabanı | −13,0 m | **%15,7** | ⛔ arayüzün altında — S1 bu yüzden ÇUKUR istasyonundan çekilir |
| yapı tabanı | 0 m | %27,8 | altı sahnede de aynı |
| 5. döşeme | 16,0 m | %42,6 | ⭐ tuğla blok sırtıyla (%42,1) AYNI HİZA → S2 kanıtı |
| tuğla blok sırtı | 15,5 m | %42,1 | çapa ① |
| servi tepesi | 19,0 m | %45,4 | çapa ② |
| sırt hattı | ~21 m | ~%47 | çapa ③ |
| ufuk (göz hizası) | 24,0 m | %50,0 | tilt 0° sonucu |
| 8. döşeme | 25,6 m | **%51,5** | ⭐ kulenin ufku GEÇTİĞİ kat → S3 dönüm anı |
| 12. döşeme | 38,4 m | %63,3 | S3 orta kanıt |
| 18. döşeme | 57,6 m | %81,1 | S3 bitiş |
| taç (parapet) | 58,7 m | %82,1 | ⛔ üst 1/8 sınırı %87,5 — altında ✅ |

⭐ **Bu tablonun tek işi şu:** "bina büyüdü" bir kanıt değildir. Bu filmde
her sahnenin kanıtı, yapının bir parçasının **arka plan çapalarından birine
göre nerede durduğudur** — ve o karşılaştırma kamera sabit olduğu için
matematiksel olarak geçerlidir.

---

## 🪜 AŞAMA MERDİVENİ

| S | AŞAMA | EKRANDA VAR OLAN | YENİ OLAN | TEMSİL | GÜNEŞ / MEVSİM | KANIT NESNESİ | İSTASYON |
|:-:|---|---|---|---|---|---|---|
| 0 | kanca · boş arsa | çit · konteyner · moloz · ot | — (ters açılış: kule geriye sökülür) | 1 gün | Temmuz · sabah→ikindi | ⭐ tuğla blok TAMAMEN AYDINLIK | ANA |
| 1 | kazı + temel | + 13 m çukur · iksa · ekskavatör | radye donatısı | 3 ay | Ağustos–Ekim | çukur tabanı 4 kat aşağıda | ÇUKUR |
| 2 | çekirdek + ilk katlar | + çekirdek · 5 kat karkas · vinç | kule vinci kuruldu | 2 ay | Kasım–Aralık | ⭐ 5. döşeme = tuğla blok çatı sırtı | VİNÇ |
| 3 | kat yığılması | + 18 kat karkas | kalıp döngüsü, kışta yavaşlar | 4 ay | Ocak–Nisan · KAR | ⭐ 8. katta ufku geçer, 18'de gökyüzünde | ANA |
| 4 | cephe | + cephe zeminden tepeye sarılır | antrasit + gri cam | 3 ay | Mayıs–Temmuz | cephe hattının tırmanışı | ANA |
| 5 | teslim | + tamamlanmış kule | ışıklar · peyzaj | 1 gün | Eylül · sabah→ikindi→akşam | ⭐ GÖLGE tuğla bloğun üstünde | ANA |

### Üç zorunlu satır

```
① KANIT NESNESİ   Her sahnede ilerleme, çapa ①②③'ten birine göre ÖLÇÜLÜR
                  (kadraj defteri). "Bina büyüdü" cümlesi hiçbir promptta yok.

② LOOP SATIRI     İKİ AYRI DÖNGÜ VAR, ikisi de tutmak zorunda:
                  ⓐ KADRAJ DÖNGÜSÜ — S5'in son karesi ile S0'ın ilk karesi
                    aynı kadrajdır (ikisi de bitmiş kule, ana istasyon).
                    Video başa sarınca kesme görünmez.
                  ⓑ KANIT ÇİFTİ ⭐ — S0'ın SON karesi (boş arsa · ikindi ·
                    tuğla blok baştan sona AYDINLIK) ile S5 · 0:57,5
                    (kule · aynı ikindi ışığı · tuğla blok baştan sona
                    GÖLGEDE). Aynı kadraj, aynı mevsim, aynı saat; tek fark
                    ortada bir kule olması. Filmin bedeli bu çiftte okunur
                    ve bu yüzden iki karenin ışığı AYNI olmak zorundadır.

③ SÖKÜM SATIRI    şantiye çiti  S0'da var → S5'te yok (S4 ile S5 ARASINDA sökülür)
                  kule vinci    S2'de kurulur → S4'te var → S5'te YOK
                                (S4 ile S5 ARASINDA sökülür — klip İÇİNDE değil)
                  konteynerler  S0'da var → S5'te yok
                  ⛔ Hiçbiri bir klibin ORTASINDA kaybolmaz. Söküm sahne
                     ARASINDA olur; model bir klip içinde nesne yok ederse
                     devamlılık ölür.
```

---

## ☀️ GÜNEŞ SAATİ

```
İKİ SAAT AYRI ÇALIŞIR (ZAMAN_VE_ISIK §1):
  SAHNE İÇİ      her klipte 1 gün geçer — gölge kadrajı süpürür
  SAHNELER ARASI 14 ay geçer — mevsim ve güneş yüksekliği değişir
```

| S | Mevsim | Öğle yüksekliği | Klibin bittiği an | Gölge yönü | Renk |
|:-:|---|---:|---|---|---|
| 0 | Temmuz | 68° | ikindi · elevation 22° | doğu-kuzeydoğu | 5600 K nötr |
| 1 | Eylül | 52° | öğle sonrası | kuzeydoğu | 5200 K sıcak |
| 2 | Aralık | 26° | erken alacakaranlık | doğu · uzun | 5000 K sıcak-alçak |
| 3 | Şubat | 19° | ikindi | doğu · çok uzun · mavi | 6500 K soğuk |
| 4 | Haziran | 66° | ikindi | doğu-kuzeydoğu | 5600 K |
| 5 | Eylül | 52° | ikindi → akşam | ⭐ doğu-kuzeydoğu | 5200 K → alacakaranlık |

```
⛔ İKİ YÖN KURALI TUTUYOR:
   Mevsim tek yönde ilerliyor:  yaz → sonbahar → kış → ilkbahar → yaz → sonbahar
   Her klipte güneş tek yönde ilerliyor: doğudan batıya, geri dönmüyor.

⭐ S0 ve S5 AYNI SAATTE, AYNI MEVSİM IŞIĞINDA biter (ikindi, elevation ~22°,
   gölge doğu-kuzeydoğu). Bu bir tercih değil, KANITIN ŞARTIDIR: iki kare
   arasındaki tek farkın kule olması için ışığın aynı olması gerekir.
```

---

## 🎬 SAHNE PROMPTLARI — okuma notu

```
Her sahnenin ÜÇ bloğu var:
  📸 GÖRSEL PROMPT   → önce üretilir ve ONAYLANIR
  🎥 I2V (BİRİNCİL)  → görselin karesinden başlar; yapıyı/sahayı/arka planı
                        YENİDEN TARİF ETMEZ, yalnız zamanın geçişini yazar
  🎥 T2V (YEDEK)     → referans görsel yoksa

⭐ ÜRETİM SIRASI TERSTİR (KILAVUZ_REHBERI §8):
   1. S5 USTA KARE üretilir. ⛔ KAPI: kule ikna edici değilse, üç çapa
      okunmuyorsa ya da taç %82'ye oturmuyorsa DİĞER BEŞ SAHNE ÜRETİLMEZ.
   2. S5 → image-to-image ile geriye: S4 → S3 → S0
   3. Detay istasyonları (S1 çukur · S2 vinç) ayrı üretilir ama YAPI BIBLE
      ve çapa ① aynen taşınır.
   4. Onaylanan her görselden I2V.
```

---

## 🎬 SAHNE 0 — KANCA: GERİYE SÖKÜLÜYOR

_"On sekiz kat, on saniyede geri alındı."_

> ⭐ **TERS TIMELAPSE AÇILIŞI.** Klip bitmiş kuleyle açılır ve boş arsaya
> iner. Vaat ilk karede verilir, döngü kendiliğinden kurulur.
> ⛔ **SPOILER BÜTÇESİ:** S0 SİLUETİ harcar, BEDELİ harcamaz. Bu klip öğle
> ışığındadır — gölge kısa ve kuzeye düşer, tuğla bloğa değmez. Kulenin
> gölgesinin tuğla bloğun üstüne oturduğu an yalnız S5'te görülür.
> ⚠️ **ÜRETİM RİSKİ VE GERİ ÇEKİLME PLANI:** ters sökülme bu deponun en az
> sınanmış hamlesidir. Model yapıyı eritirse (kat kat inmek yerine
> bulanıklaşırsa) S0, düz bir boş arsa gün süpürmesine döner ve vaadin
> tamamı kapağa biner. Karar S0'ın ilk üretiminde verilir, sonra değil.

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 0 of 6. Vertical time-lapse of a high-rise tower on a tight urban infill site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the roof parapet of the block to the south-west, lens 24.0 metres above street level, 72 metres from the south-west face of the site, bearing 035 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: A single reinforced-concrete tower, eighteen storeys and 58.7 metres tall to the top of its parapet when complete, on a 24 by 18 metre footprint, with a 6 by 4 column grid at 4.0 metre centres, a floor-to-floor height of 3.20 metres, one concrete core in the north-east corner, an anthracite aluminium curtain wall with light grey glass, a flat roof with a 1.10 metre parapet and a single mechanical enclosure. AT THIS STAGE: the tower is complete. Every floor is clad, the glass is clean, the parapet is finished and the mechanical enclosure sits on the roof. No crane, no hoarding, no scaffolding, no site huts remain.

SITE / BACKGROUND: To frame right stands a five-storey red brick apartment block with two chimneys on its roof and a roof ridge 15.5 metres above the ground. To frame left stands a single leaning cypress tree 19 metres tall. Behind the site runs a low ridge line carrying a scattered silhouette of small low buildings. The horizon sits at exactly half the frame height. An asphalt road enters the frame at the lower right corner.

THE TIME MOMENT: This is the last frame of the story shown as the first frame of the film. The tower stands finished and the ground around it is finished with it.

COMPOSITION: Vertical 9:16. The base of the tower sits at about twenty-eight percent of frame height and the top of its parapet at about eighty-two percent. The roof ridge of the red brick block sits at about forty-two percent and the top of the cypress at about forty-five percent. The crown of the structure sits below the top eighth of the frame and the ground level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: July, midday. Sun azimuth 178 degrees, elevation 68 degrees, shadows short and falling almost straight to the north. Neutral 5600K daylight, deep blue sky with high thin cloud. The south-west face of the red brick block is fully lit from top to bottom and carries no shadow from anything.

ACTIVITY: The street is live. Vehicles render as smeared light and colour trails along the road. People appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere.

SITE TEXTURE: Newly laid paving, young planting still staked, a faint line in the asphalt where the site access used to be.

PHYSICS: The tower stands on its own foundations and every element is in continuous contact with what carries it. Nothing floats, nothing is suspended.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same building, same background in every frame: the horizon line, the neighbouring buildings, the road, the trees and the ridge behind them never change shape, position, size or spacing. The structure is one single rigid building — the column grid, the bay spacing, the floor height and the footprint stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hoarding, the safety signage, the crane, the machinery, the shipping containers, the workers' vests and helmets, the trucks, the scaffolding, the formwork or the facade, and not on any shop front, billboard, street plate or licence plate. Nothing in this frame has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

The building comes apart backwards, in the order it was built, and the day runs forward at the same time. First the grey glass and the anthracite framing peel away downward, floor by floor from the parapet to the ground, leaving bare grey concrete frame behind them. Then the floors themselves come off the top downward, one slab at a time, and as they go a tower crane grows down beside the building until it too is gone. The last columns drop into a rectangular pit that opens in the ground, and the pit closes over and fills back to street level, leaving a flat empty lot behind a blue hoarding fence with two site huts and a heap of rubble on it. While all of this happens the sun swings from midday to late afternoon: the shadows lengthen and turn toward the east-north-east, the light warms, and by the end of the shot the south-west face of the red brick block to frame right is lit from top to bottom with nothing standing in front of it.

The camera does not move at any point. The framing is identical in the first and last frame. The five-storey red brick block with its two chimneys, the leaning cypress tree and the ridge line behind the site stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly half the frame height. The road, the pavement and the neighbouring buildings never change.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 10 seconds. Lens: 24mm on a fixed tripod, 24.0 metres above street level, 72 metres from the site, bearing 035 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — A finished eighteen-storey tower with an anthracite and grey glass facade stands on a tight urban site at midday, a five-storey red brick block with two chimneys to frame right, a leaning cypress to frame left, a low ridge line behind.
At 1.5s — The glass and framing peel away downward from the parapet, floor by floor, leaving bare grey concrete frame.
At 3.5s — The floors come off the top downward, eighteen down to eight, and a tower crane grows down beside the building.
At 5.5s — The remaining floors and the crane go, down to bare columns, and a rectangular pit opens in the ground beneath them.
At 7.0s — The pit closes and fills to street level, leaving a flat empty lot behind a blue hoarding fence with two site huts and rubble.
At 8.0s — The sun swings west, the shadows lengthen and turn east-north-east, the light warms.
By 10s — The empty lot sits in late afternoon light and the south-west face of the red brick block is lit from top to bottom with nothing in front of it. Hard cut to Scene 1.

The camera never moves. The brick block, the cypress and the ridge line never change shape, size or position. No readable text, letters, digits or logos anywhere. No architectural render look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 1 — ÇUKUR

_"Önce yukarı değil, aşağı gitti."_

> İstasyon değişir: **ÇUKUR.** Sebebi kadraj defterinde yazılı — çukur
> tabanı ana istasyondan kare yüksekliğinin %15,7'sinde kalır, yani
> platform arayüzünün ALTINDA. Ana istasyondan bu sahne fiziksel olarak
> görülemez. Çapa ① kadrajın üstünde tutulur.

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 1 of 6. Vertical time-lapse of a high-rise tower on a tight urban infill site.
Lens: 35mm spherical, f/8, ISO 100.
Camera: PIT STATION — fixed tripod clamped to the site guardrail at the south edge of the excavation, lens 1.50 metres above street level, 18 metres from the far wall of the pit, bearing 040 degrees, tilt 8 degrees down, zero roll. The camera never moves.

STRUCTURE: A single reinforced-concrete tower, eighteen storeys and 58.7 metres tall to the top of its parapet when complete, on a 24 by 18 metre footprint, with a 6 by 4 column grid at 4.0 metre centres, a floor-to-floor height of 3.20 metres, one concrete core in the north-east corner, an anthracite aluminium curtain wall with light grey glass, a flat roof with a 1.10 metre parapet and a single mechanical enclosure. AT THIS STAGE: nothing of the tower stands above ground. Below ground there is a rectangular excavation 13 metres deep on the exact 24 by 18 metre footprint, its walls held by a grey shotcrete retaining wall with regular steel waler beams, and on its floor a dense flat mat of steel reinforcement bars tied in a grid, ready for the raft.

SITE / BACKGROUND: Above and beyond the pit, to frame right, stands the five-storey red brick apartment block with two chimneys on its roof and a roof ridge 15.5 metres above the ground. An asphalt road passes behind the top edge of the excavation.

THE TIME MOMENT: The pit floor sits four storeys below street level — an excavator standing on it reads as a small shape against the retaining wall, and the brick block beyond the hoarding towers over the whole opening.

COMPOSITION: Vertical 9:16. The pit fills the lower two thirds of the frame, the hoarding line crosses at about sixty-five percent, and the red brick block occupies the upper right. The working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: September, early afternoon. Sun azimuth 218 degrees, elevation 44 degrees, shadows falling to the north-east. Warm 5200K light. Half the pit floor is in hard shadow from its own south wall and half is in direct sun; the cut between them is sharp.

ACTIVITY: A tracked excavator stands on the pit floor and a second sits on a ramp against the east wall. A rebar cage stack and bundles of bar lie on the floor. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Trucks on the road above render as smeared colour trails.

SITE TEXTURE: A blue hoarding panel fence runs along the top edge of the excavation. Wet clay, deep tyre ruts, standing puddles on the pit floor, mud tracked up the ramp, stacked material, offcuts, tarpaulins and untidy clutter along the edges.

PHYSICS: The retaining wall carries the earth behind it and every waler beam is in contact with the wall. The excavators rest on their tracks on the pit floor. Nothing floats, nothing is suspended.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same background in every frame: the red brick block, the hoarding line and the road never change shape, position, size or spacing. Nothing already excavated or built is removed, moved or resized. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hoarding, the safety signage, the machinery, the shipping containers, the workers' vests and helmets, the trucks or any shop front, billboard, street plate or licence plate. Nothing in this frame has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: mud, tyre ruts, puddles, stacked material, offcuts, tarpaulins and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

Three months pass. The hard shadow cast by the south wall of the excavation swings slowly across the pit floor from west to east as the sun crosses the sky, and thin cloud streaks across the top of the frame in long smooth trails, always from the north-west. The two excavators work in slow repeating cycles, the bucket rising and falling, and their tracks cut new ruts in the clay. The flat steel reinforcement mat on the pit floor grows denser and spreads out to the walls of the excavation until it covers the whole pit floor. Trucks pass along the road above the hoarding as smeared colour trails. Rain darkens the clay once and dries again.

The camera does not move at any point. The framing is identical in the first and last frame. The five-storey red brick block with its two chimneys, the hoarding line and the road stay exactly where they are, at exactly the same size and shape, for the whole shot. The pit never gets deeper or shallower and its walls never move. Nothing already built is removed, moved or resized.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 10 seconds. Lens: 35mm on a fixed tripod clamped to a site guardrail, 1.50 metres above street level, 18 metres from the far wall of a 13 metre deep rectangular excavation, bearing 040 degrees, tilt 8 degrees down. Absolutely zero camera movement.

At 0s — A rectangular excavation four storeys deep, grey shotcrete retaining walls with steel waler beams, a five-storey red brick block with two chimneys standing beyond the blue hoarding at the top of the frame.
At 2.0s — The hard shadow of the south wall begins to swing across the pit floor from west to east; cloud streaks across the top of the frame.
At 4.0s — Two tracked excavators work in slow repeating cycles at the bottom, cutting fresh ruts in the wet clay.
At 6.0s — A flat mat of tied steel reinforcement bars spreads across the pit floor, growing denser and reaching the walls.
At 8.0s — Rain darkens the clay and dries again; trucks pass above the hoarding as smeared colour trails.
By 10s — The reinforcement mat covers the whole footprint and the pit floor is in full shadow. Hard cut to Scene 2.

The camera never moves. The brick block, the hoarding line and the road never change shape, size or position. The pit never gets deeper or shallower. No readable text, letters, digits or logos anywhere. No architectural render look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 2 — KOMŞUSUNA YETİŞTİ

_"Beşinci döşeme, karşı bloğun çatısıyla aynı hizaya geldi."_

> İstasyon: **VİNÇ.** Görevi ölçektir (`KAMERA_ISTASYONU` §4.3). Çapa ①
> kadrajın sağ kenarında tutulur ve sahnenin kanıtı odur.

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 2 of 6. Vertical time-lapse of a high-rise tower on a tight urban infill site.
Lens: 50mm spherical, f/5.6, ISO 100.
Camera: CRANE STATION — fixed tripod bolted to the ground 40 metres from the base of the tower crane, lens 1.60 metres above street level, bearing 020 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: A single reinforced-concrete tower, eighteen storeys and 58.7 metres tall to the top of its parapet when complete, on a 24 by 18 metre footprint, with a 6 by 4 column grid at 4.0 metre centres, a floor-to-floor height of 3.20 metres, one concrete core in the north-east corner, an anthracite aluminium curtain wall with light grey glass, a flat roof with a 1.10 metre parapet and a single mechanical enclosure. AT THIS STAGE: five completed slabs of bare grey concrete frame stand on the footprint, 16.0 metres above the ground, the concrete core rises two floors above the topmost slab, the top slab carries yellow-brown timber formwork tables and a dense forest of steel props, and there is no cladding of any kind anywhere — every floor is open to the weather.

SITE / BACKGROUND: At the right edge of the frame stands the five-storey red brick apartment block with two chimneys on its roof and a roof ridge 15.5 metres above the ground. An asphalt road passes behind the site.

THE TIME MOMENT: The fifth slab now sits exactly level with the roof ridge of the red brick block at the right edge of the frame — the tower has reached the height of its neighbour. Above it the crane mast still rises three times that height again.

COMPOSITION: Vertical 9:16. The concrete base of the crane sits at about thirty percent of frame height, the five-slab frame occupies the middle of the picture, and the crane mast runs up through the whole upper half and out of the top of the frame. The red brick block reads at the right edge with its roof ridge level with the fifth slab. The working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: December, mid-afternoon. Sun azimuth 226 degrees, elevation 17 degrees, long shadows falling to the east-north-east. Warm low 5000K light raking across the concrete, a flat pale sky, the west faces of the columns brightly lit and the east faces in deep shadow.

ACTIVITY: The tower crane slews slowly with a bundle of formwork on the hook. A concrete pump stands inside the hoarding with its boom folded. Workers appear only as soft motion streaks and blurred figures on the top slab, none of them sharp, none of them facing the camera, no readable face anywhere, and they read as tiny against the frame. Trucks on the road render as smeared colour trails.

SITE TEXTURE: A blue hoarding panel fence runs across the foreground. Mud, deep tyre ruts, standing puddles, stacked timber and rebar bundles, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The tower crane is one continuous rigid steel lattice mast standing on a concrete base at ground level, with an unbroken load path from the hook to the trolley to the jib to the mast to the ground. The mast never floats, never bends and never changes height within the shot, and the jib stays perfectly straight. The hook block hangs vertically under the trolley on a single taut cable and never swings faster than a slow pendulum. Every slab rests on props and columns beneath it; nothing is unsupported.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same building, same background in every frame: the red brick block, the hoarding line and the road never change shape, position, size or spacing. The structure is one single rigid building that only ever gains material — nothing already built is removed, moved, resized or redesigned; the column grid, the bay spacing, the floor height and the footprint stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hoarding, the safety signage, the crane, the machinery, the shipping containers, the workers' vests and helmets, the trucks, the scaffolding, the formwork or any shop front, billboard, street plate or licence plate. Nothing in this frame has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no crane hanging from nothing, no machine hovering above the ground. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: mud, tyre ruts, puddles, stacked material, offcuts, tarpaulins and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

Two months pass. The long low shadows rake across the concrete and swing slowly to the east-north-east as the winter sun crosses low across the sky, and pale cloud streaks across the frame in long smooth trails, always from the north-west. The tower crane slews slowly back and forth, and its hook block rises and falls on a taut cable, carrying formwork and rebar bundles up to the top slab. Two more slabs of bare grey concrete frame arrive on top of the five, each one appearing as a completed slab with props already beneath it, and the formwork tables climb with them. The concrete core keeps its two-floor lead above the topmost slab. Workers move on the top slab as soft blurred streaks and the trucks below smear into colour trails.

The camera does not move at any point. The framing is identical in the first and last frame. The five-storey red brick block with its two chimneys at the right edge, the hoarding line and the road stay exactly where they are, at exactly the same size and shape, for the whole shot. Nothing already built is removed, moved or resized, and no new slab appears without props beneath it. The crane mast never floats, never bends and never changes height.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 10 seconds. Lens: 50mm on a fixed tripod, 1.60 metres above street level, 40 metres from the base of a tower crane, bearing 020 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Five slabs of bare grey concrete frame stand on a tight urban site with a concrete core two floors above them, a tower crane rising through the upper half of the frame, and a five-storey red brick block at the right edge with its roof ridge level with the fifth slab.
At 2.0s — Long low winter shadows rake across the concrete and begin to swing to the east-north-east; pale cloud streaks from the north-west.
At 4.0s — The crane slews slowly and the hook block rises with a bundle of formwork.
At 6.0s — A sixth slab arrives complete with props beneath it and the formwork tables climb with it.
At 8.0s — A seventh slab arrives; the core keeps its two-floor lead above the top slab.
By 10s — The frame stands seven slabs high, well above the roof ridge of the brick block. Hard cut to Scene 3.

The camera never moves. The brick block, the hoarding line and the road never change shape, size or position. Nothing already built is removed or resized. The crane mast never floats or bends. No readable text, letters, digits or logos anywhere. No architectural render look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 3 — KIŞ VE KATLAR (⭐ DİRENÇ SAHNESİ)

_"Ufku sekizinci katta geçti. Kışın her kat dört gün geç geldi."_

> Ana istasyona dönülür ve filmin en uzun temsil süresi buradadır: **4 ay.**
> Kadraj defterinin dönüm satırı bu sahnede ekrana çıkar — **8. döşeme
> (%51,5) kameranın ufkunu geçer.** O andan sonra kule artık sırt hattının
> önünde değil, gökyüzünün önündedir. Kanıt bu.

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 3 of 6. Vertical time-lapse of a high-rise tower on a tight urban infill site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the roof parapet of the block to the south-west, lens 24.0 metres above street level, 72 metres from the south-west face of the site, bearing 035 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: A single reinforced-concrete tower, eighteen storeys and 58.7 metres tall to the top of its parapet when complete, on a 24 by 18 metre footprint, with a 6 by 4 column grid at 4.0 metre centres, a floor-to-floor height of 3.20 metres, one concrete core in the north-east corner, an anthracite aluminium curtain wall with light grey glass, a flat roof with a 1.10 metre parapet and a single mechanical enclosure. AT THIS STAGE: seven completed slabs of bare grey concrete frame stand on the footprint, the concrete core rises two floors above the topmost slab, the top slab carries yellow-brown timber formwork tables and a dense forest of steel props, and there is no cladding of any kind anywhere — every floor is open to the weather.

SITE / BACKGROUND: To frame right stands a five-storey red brick apartment block with two chimneys on its roof and a roof ridge 15.5 metres above the ground. To frame left stands a single leaning cypress tree 19 metres tall. Behind the site runs a low ridge line carrying a scattered silhouette of small low buildings. The horizon sits at exactly half the frame height. An asphalt road enters the frame at the lower right corner.

THE TIME MOMENT: The seventh slab stands just below the horizon line of the picture — the tower is still read against the ridge behind it, not yet against the sky.

COMPOSITION: Vertical 9:16. The base of the tower sits at about twenty-eight percent of frame height and the seventh slab at about forty-nine percent, just under the horizon. The roof ridge of the red brick block sits at about forty-two percent and the top of the cypress at about forty-five percent. The crane mast runs out of the top of the frame. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: February, mid-afternoon. Sun azimuth 232 degrees, elevation 16 degrees, very long blue shadows falling to the east-north-east. Cold 6500K light under a flat white-grey sky, low contrast, the concrete reading almost blue in shadow.

ACTIVITY: The tower crane stands against the north face with its jib over the top slab and the hook block hanging on a taut cable. A concrete pump stands inside the hoarding. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: A blue hoarding panel fence encloses the site. Grey tracked snow piled at the edges and partly melted, never clean and never uniform, mud, deep tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The tower crane is one continuous rigid steel lattice mast standing on a concrete base at ground level, with an unbroken load path from the hook to the trolley to the jib to the mast to the ground. The mast never floats, never bends and never changes height within the shot, and the jib stays perfectly straight. Every slab rests on props and columns beneath it; nothing is unsupported.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same building, same background in every frame: the horizon line, the neighbouring buildings, the road, the trees and the ridge behind them never change shape, position, size or spacing. The structure is one single rigid building that only ever gains material — nothing already built is removed, moved, resized or redesigned; the column grid, the bay spacing, the floor height and the footprint stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hoarding, the safety signage, the crane, the machinery, the shipping containers, the workers' vests and helmets, the trucks, the scaffolding, the formwork or any shop front, billboard, street plate or licence plate. Nothing in this frame has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no crane hanging from nothing, no machine hovering above the ground. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. The snow on the site is grey, tracked, piled and partly melted — never clean, never untouched, never uniform. This is a working construction site: mud, tyre ruts, puddles, stacked material, offcuts, tarpaulins and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

Four months pass. The very long blue shadow of the tower swings slowly across the site to the east-north-east as the low winter sun crosses the sky, and grey cloud streaks across the frame in long smooth trails, always from the north-west. The tower crane slews slowly back and forth over the top slab and its hook block rises and falls on a taut cable. Slab after slab of bare grey concrete frame arrives on top of the seven, each one appearing complete with steel props already beneath it and the timber formwork tables climbing with it, and the concrete core keeps its two-floor lead the whole way. Around the eighth slab the top of the frame rises past the ridge line behind the site and from then on the tower stands against open sky. Snow gathers grey and tracked at the edges of the site, is walked through, and partly melts. By the end the frame stands eighteen slabs high and the crane has climbed with it.

The camera does not move at any point. The framing is identical in the first and last frame. The five-storey red brick block with its two chimneys, the leaning cypress tree and the ridge line behind the site stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly half the frame height. Nothing already built is removed, moved or resized, no floor height changes, and no new slab appears without props beneath it. The crane mast never floats, never bends and never leans.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 10 seconds. Lens: 24mm on a fixed tripod, 24.0 metres above street level, 72 metres from the site, bearing 035 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — Seven slabs of bare grey concrete frame stand on a tight urban site under a flat white winter sky, a tower crane rising out of the top of the frame, a five-storey red brick block to frame right, a leaning cypress to frame left, a low ridge line behind.
At 2.0s — Very long blue shadows swing across the site to the east-north-east; grey cloud streaks from the north-west.
At 4.0s — Slabs arrive one after another on top of the frame, each complete with steel props beneath it, the crane slewing and lifting between them.
At 5.5s — The top of the frame passes the ridge line behind the site and the tower now stands against open sky.
At 7.5s — Grey tracked snow gathers at the edges of the site, is walked through and partly melts.
By 10s — The bare concrete frame stands eighteen slabs high with the crane climbed alongside it. Hard cut to Scene 4.

The camera never moves. The brick block, the cypress, the ridge line and the horizon never change shape, size or position. Nothing already built is removed or resized and no floor height changes. The crane mast never floats or bends. No readable text, letters, digits or logos anywhere. No architectural render look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 4 — DERİ

_"Aşağıdan yukarı sarıldı. Karkas kayboldu."_

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 4 of 6. Vertical time-lapse of a high-rise tower on a tight urban infill site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the roof parapet of the block to the south-west, lens 24.0 metres above street level, 72 metres from the south-west face of the site, bearing 035 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: A single reinforced-concrete tower, eighteen storeys and 58.7 metres tall to the top of its parapet when complete, on a 24 by 18 metre footprint, with a 6 by 4 column grid at 4.0 metre centres, a floor-to-floor height of 3.20 metres, one concrete core in the north-east corner, an anthracite aluminium curtain wall with light grey glass, a flat roof with a 1.10 metre parapet and a single mechanical enclosure. AT THIS STAGE: the concrete frame is complete to eighteen storeys and the roof parapet is cast, every floor is still bare grey concrete open to the weather, and the first two floors above ground carry the beginnings of the anthracite aluminium curtain wall with its light grey glass.

SITE / BACKGROUND: To frame right stands a five-storey red brick apartment block with two chimneys on its roof and a roof ridge 15.5 metres above the ground. To frame left stands a single leaning cypress tree 19 metres tall. Behind the site runs a low ridge line carrying a scattered silhouette of small low buildings. The horizon sits at exactly half the frame height. An asphalt road enters the frame at the lower right corner.

THE TIME MOMENT: A sharp horizontal line divides the tower: dark clad glass below it and bare grey concrete above it. The line stands two floors up, well below the roof ridge of the red brick block.

COMPOSITION: Vertical 9:16. The base of the tower sits at about twenty-eight percent of frame height and the roof parapet at about eighty-two percent. The cladding line crosses the tower at about thirty-four percent. The roof ridge of the red brick block sits at about forty-two percent and the top of the cypress at about forty-five percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: June, mid-afternoon. Sun azimuth 248 degrees, elevation 38 degrees, shadows falling to the east-north-east. Neutral 5600K daylight, a clear sky with high thin cloud, the new glass on the lower floors reading as a dark cool band against the pale concrete above it.

ACTIVITY: The tower crane stands against the north face with its jib over the roof and a curtain wall unit hanging on the hook. A mast climbing platform runs up the south-west face. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: A blue hoarding panel fence encloses the site. Dried mud, tyre ruts, stacked cladding crates, pallets, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The tower crane is one continuous rigid steel lattice mast standing on a concrete base at ground level, with an unbroken load path from the hook to the trolley to the jib to the mast to the ground. The mast never floats, never bends and never changes height within the shot, and the jib stays perfectly straight. The climbing platform is bolted to the face of the building. Every element is in continuous contact with what carries it.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same building, same background in every frame: the horizon line, the neighbouring buildings, the road, the trees and the ridge behind them never change shape, position, size or spacing. The structure is one single rigid building that only ever gains material — nothing already built is removed, moved, resized or redesigned; the column grid, the bay spacing, the floor height and the footprint stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hoarding, the safety signage, the crane, the machinery, the shipping containers, the workers' vests and helmets, the trucks, the scaffolding, the cladding crates or any shop front, billboard, street plate or licence plate. Nothing in this frame has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no crane hanging from nothing, no machine hovering above the ground. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: mud, tyre ruts, puddles, stacked material, offcuts, tarpaulins and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

Three months pass. The shadow of the tower swings across the site to the east-north-east as the high summer sun crosses the sky, and thin cloud streaks across the frame in long smooth trails, always from the north-west. The sharp horizontal line between dark glass and bare grey concrete climbs steadily up the building, floor by floor, as the anthracite aluminium curtain wall is fitted from the bottom upward. The line passes the roof ridge of the red brick block, then the top of the cypress, then the horizon, and keeps going until the whole tower is clad to the parapet and no bare concrete is left. The tower crane slews slowly and lifts curtain wall units to the working level, and the climbing platform rises up the face with the cladding line. Trucks deliver crates below as smeared colour trails.

The camera does not move at any point. The framing is identical in the first and last frame. The five-storey red brick block with its two chimneys, the leaning cypress tree and the ridge line behind the site stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly half the frame height. The tower does not grow taller, the parapet stays at the same height, and nothing already fitted is removed or changed. The crane mast never floats, never bends and never leans.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 10 seconds. Lens: 24mm on a fixed tripod, 24.0 metres above street level, 72 metres from the site, bearing 035 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — An eighteen-storey bare grey concrete frame stands complete to its parapet with only the first two floors clad in dark anthracite framing and grey glass; a tower crane against the north face, a five-storey red brick block to frame right, a leaning cypress to frame left.
At 2.0s — The shadow of the tower swings east-north-east under a high summer sun; thin cloud streaks from the north-west.
At 4.0s — The sharp horizontal line between glass and concrete climbs floor by floor and passes the roof ridge of the brick block.
At 6.0s — The line passes the top of the cypress and then the horizon; the crane lifts cladding units to the working level.
At 8.0s — A climbing platform rises up the face with the cladding line.
By 10s — The tower is clad to the parapet and no bare concrete is left. Hard cut to Scene 5.

The camera never moves. The brick block, the cypress, the ridge line and the horizon never change shape, size or position. The tower does not grow taller and the parapet stays at the same height. No readable text, letters, digits or logos anywhere. No architectural render look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎬 SAHNE 5 — İKİNDİ (⭐ BEDEL · DÖNGÜ · FİNAL VURUŞ)

_"Kule bitti. Ve karşı bloğun ikindisi bitti."_

> ⭐ **FİLMİN ÖDEMESİ BURADA.** Klip sabahla açılır, ikindiye gelir ve
> **kulenin gölgesi tuğla bloğun güneybatı yüzüne oturur** — S0'ın son
> karesinde baştan sona aydınlık olan yüz. Aynı kadraj, aynı mevsim, aynı
> saat; tek fark ortada bir kule olması.
> ⛔ **FİNAL VURUŞ KANITI: 0:57,5** — gölge o karede tuğla bloğun üstünde
> görünmüyorsa film TESLİM EDİLMEMİŞTİR (`QA_SPEC`).
> **Vinç ve çit S4 ile S5 ARASINDA söküldü** — klip içinde kaybolmadı.

### 📸 GÖRSEL PROMPT ⭐ USTA KARE — İLK BU ÜRETİLİR

```
Photorealistic documentary construction photograph — Scene 5 of 6. Vertical time-lapse of a completed high-rise tower on a tight urban infill site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the roof parapet of the block to the south-west, lens 24.0 metres above street level, 72 metres from the south-west face of the site, bearing 035 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: A single reinforced-concrete tower, eighteen storeys and 58.7 metres tall to the top of its parapet when complete, on a 24 by 18 metre footprint, with a 6 by 4 column grid at 4.0 metre centres, a floor-to-floor height of 3.20 metres, one concrete core in the north-east corner, an anthracite aluminium curtain wall with light grey glass, a flat roof with a 1.10 metre parapet and a single mechanical enclosure. AT THIS STAGE: the tower is complete. Every floor is clad, the glass is clean, the parapet is finished and the mechanical enclosure sits on the roof. There is no crane, no hoarding, no scaffolding, no climbing platform and no site huts anywhere.

SITE / BACKGROUND: To frame right stands a five-storey red brick apartment block with two chimneys on its roof and a roof ridge 15.5 metres above the ground. To frame left stands a single leaning cypress tree 19 metres tall. Behind the site runs a low ridge line carrying a scattered silhouette of small low buildings. The horizon sits at exactly half the frame height. An asphalt road enters the frame at the lower right corner.

THE TIME MOMENT: Morning. The tower stands finished and its shadow falls to the west, away from the red brick block, whose south-west face is lit from top to bottom.

COMPOSITION: Vertical 9:16. The base of the tower sits at about twenty-eight percent of frame height and the top of its parapet at about eighty-two percent. The roof ridge of the red brick block sits at about forty-two percent and the top of the cypress at about forty-five percent. The crown of the structure sits below the top eighth of the frame and the ground level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: September, mid-morning. Sun azimuth 112 degrees, elevation 30 degrees, shadows falling to the west-north-west. Warm 5200K light, a clear sky with thin high cloud, the grey glass of the tower catching the low sun in flat panels.

ACTIVITY: The street is live. Vehicles render as smeared light and colour trails along the road. People appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere.

SITE TEXTURE: New paving at the base of the tower, young planting still staked, a faint line in the asphalt where the site access used to be.

PHYSICS: The tower stands on its own foundations and every element is in continuous contact with what carries it. Nothing floats, nothing is suspended.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same building, same background in every frame: the horizon line, the neighbouring buildings, the road, the trees and the ridge behind them never change shape, position, size or spacing. The structure is one single rigid building — the column grid, the bay spacing, the floor height and the footprint stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the facade, the machinery, the trucks, the scaffolding, the hoarding, the signage, the containers, the vests or the helmets, and not on any shop front, billboard, street plate or licence plate. Nothing in this frame has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no floating structure, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. Photorealistic documentary photography, 35mm film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT ⭐ BİRİNCİL

```
The scene begins exactly as the provided image.

One day passes. The sun crosses from the east to the west and the shadow of the tower swings slowly around its base, shortening toward the middle of the day and then lengthening again, and thin high cloud streaks across the frame in long smooth trails, always from the north-west. As the afternoon goes on the shadow turns to the east-north-east and reaches out across the ground toward the five-storey red brick block at frame right. It climbs the brick block's south-west face from the bottom upward, and by late afternoon that whole face is in shadow from the pavement to its roof ridge while the sky behind it is still bright. Then the light fails into dusk, and the windows of the tower come on floor by floor from the bottom upward until the whole building is lit. Traffic on the road smears into long colour trails.

The camera does not move at any point. The framing is identical in the first and last frame. The five-storey red brick block with its two chimneys, the leaning cypress tree and the ridge line behind the site stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly half the frame height. The tower does not change in any way — same height, same parapet, same facade — only the light on it and the shadow it casts change.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. No light streaks in the sky, no star trails, no neon, no illuminated signage, no readable window content. Photorealistic documentary time-lapse cinematography.
```

### 🎥 T2V PROMPT (yedek)

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 10 seconds. Lens: 24mm on a fixed tripod, 24.0 metres above street level, 72 metres from the site, bearing 035 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — A finished eighteen-storey tower with an anthracite and grey glass facade stands in mid-morning light; a five-storey red brick block with two chimneys to frame right lit from top to bottom, a leaning cypress to frame left, a low ridge line behind.
At 2.5s — The sun climbs, the tower's shadow shortens and swings around its base; thin cloud streaks from the north-west.
At 5.0s — The afternoon shadow lengthens and turns to the east-north-east, reaching across the ground toward the brick block.
At 7.0s — The shadow climbs the brick block's south-west face from the bottom upward.
At 7.5s — That whole face is in shadow from the pavement to its roof ridge while the sky behind is still bright.
By 10s — The light fails into dusk and the tower's windows come on floor by floor from the bottom upward. Hard cut to Scene 0 (loop).

The camera never moves. The brick block, the cypress, the ridge line and the horizon never change shape, size or position. The tower does not change — only the light on it and the shadow it casts. No light streaks in the sky, no star trails, no neon, no illuminated signage. No readable text, letters, digits or logos anywhere. No architectural render look.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

## 🎶 MÜZİK PROMPTU (tek global tema — 60 sn)

> BPM ızgaradan seçildi (`MUZIK_VE_KAPAK` §1.1): **96 BPM = 4 ölçü/sahne.**
> Altı sahne geçişinin altısı da ölçü başına denk gelir.
> Katman mantığı: **katman = kat** — her sahnede bir katman eklenir, hiçbiri
> çıkmaz; son iki saniyede hepsi birden çekilir.

```
Instrumental score for a 60-second vertical construction time-lapse. No lyrics,
no voice, no melody line, no traditional song structure. Rhythm, texture and
accumulation only.

Genre: modern minimalism with industrial percussion and a slow harmonic floor.
Tempo: 96 BPM, strict and bar-aligned, four bars per ten seconds, no rubato.

Layers — one added every ten seconds, none ever removed until the final bar:
1. A dry low pulse on the first beat of every bar, close and unreverberated,
   like a distant pile driver heard through a wall.
2. A sustained low synth bass note, unmoving in pitch, entering underneath.
3. Struck metal: a short scaffold-tube tone on the third beat of every second
   bar, left to ring, never louder than the pulse.
4. A bowed string cluster with audible bow friction, cold and unresolved —
   this is the winter layer and it never leaves once it arrives.
5. A quiet repeating arpeggio figure, sixteen notes to the bar, mechanical and
   even, like a facade being fitted panel by panel.
6. A wide warm chord pad that finally gives the harmony a floor.

Dynamic map across 60 seconds:
  0.0-1.5   silence — the mix carries only the site's own ambience: distant
            traffic and a faint wind. The score does not enter.
  1.5-10.0  layer 1 alone, quiet, four bars.
  10.0-20.0 layer 2 enters underneath.
  20.0-30.0 layer 3 enters; the low pulse tightens very slightly.
  30.0-40.0 layer 4 enters — the coldest and widest moment of the piece.
  40.0-50.0 layer 5 enters; the texture becomes busy and even.
  50.0-58.0 layer 6 enters and the whole stack sits together, warm and full.
  58.0-60.0 everything withdraws in one bar and leaves only the ambience.

Reference feel: the patient accumulation of Nils Frahm's minimal piano work and
the industrial restraint of Jóhann Jóhannsson's textures. Do not quote, sample
or reproduce any existing composition.

Phone-speaker rule: every sub-bass element below 150 Hz is doubled by its own
upper harmonics at roughly 100, 150 and 200 Hz so the fundamental is implied
rather than required; the low end is never the only carrier of the weight.
```

```
⛔ MÜZİKSİZ PENCERE: 0,0-1,5 sn. Kanca diegetik sesle açılır (uzak trafik,
   rüzgâr). Uzun enstrümantal intro ELENDİ — ilk 1,5 saniyede müzik varsa
   ters sökülmenin görsel şoku müziğin altında kalır.
```

---

## 🖼️ KAPAK PROMPTU (1080×1920)

> **Kaynak an: S5 · 0:57,5** — filmin final vuruşuyla birebir aynı kare
> (`MUZIK_VE_KAPAK` §2.1: kapak uydurulmaz, filmin içinden çıkar).
> ⭐ Kapak iki zamanı tek karede taşır: bitmiş kule + üstündeki gölgenin
> düştüğü komşu. Merak boşluğu budur.

```
Photorealistic documentary photograph, vertical 9:16, 1080 by 1920.
Lens: 24mm spherical, f/8, ISO 100. Fixed tripod 24.0 metres above street level, 72 metres from the building, bearing 035 degrees, tilt 0 degrees.

A finished eighteen-storey reinforced-concrete tower with an anthracite aluminium curtain wall and light grey glass stands on a tight urban site, 58.7 metres to the top of its flat roof parapet, with a single mechanical enclosure on the roof. There is no crane, no hoarding and no scaffolding anywhere.

To frame right stands a five-storey red brick apartment block with two chimneys on its roof and a roof ridge 15.5 metres above the ground. To frame left stands a single leaning cypress tree 19 metres tall. Behind the site runs a low ridge line carrying a scattered silhouette of small low buildings. The horizon sits at exactly half the frame height.

Late September afternoon. Sun azimuth 258 degrees, elevation 20 degrees. The long shadow of the tower reaches to the east-north-east and lies across the entire south-west face of the red brick block, from the pavement to its roof ridge, while the sky behind it is still bright and the upper floors of the tower itself are lit warm by the low sun. The line between the shadowed brick face and the lit sky is sharp.

The base of the tower sits at about twenty-eight percent of frame height and the top of its parapet at about eighty-two percent. Nothing story-critical falls into the bottom quarter or the right eighth of the frame.

No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the facade, the vehicles, the street or any sign, plate or shop front. No people with readable faces. No crane, no hoarding. No architectural visualisation look, no real-estate render look, no CGI aesthetic, no miniature look, no tilt-shift blur, no lens flare, no bloom, no vignette, no logo, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

```
⭐ 120 PX POSTA PULU TESTİ — İKİ GÖRÜNTÜYE koşulur
   ① bu kapak karesi        ② S0'ın 0. karesi
   sips -Z 120 <dosya> --out <test>
   Beklenen tek şekil: GÖKYÜZÜNE KARŞI DİK BİR KOYU DİKDÖRTGEN ve onun
   sağında ALÇAK, GÖLGEDE BİR KÜTLE.
   ⛔ Siluet arka planla karışıyorsa kapak yeniden ÇERÇEVELENMEZ, SAHNE
      YENİDEN ÜRETİLİR — kaybolan şey kompozisyon değil, filmin vaadidir.
   ⛔ Elle "bence okunuyor" demek bu testi geçmek sayılmaz.
```

---

## 📣 BAŞLIK VE AÇIKLAMA PAKETİ

**Başlık alternatifleri (≤40 karakter):**

```
1. Kimin güneşini aldı?
2. 14 ay, 60 saniye, tek kamera
3. Bu arsa 18 kat oldu
```

**Açıklama (ilk satır kancadır):**

```
On dört ay boyunca kamera hiç yerinden oynamadı.
Boş bir yıkım arsası on sekiz kata çıktı: 13 metrelik çukur, bir kış, tek
vinç ve aşağıdan yukarı sarılan bir cephe. Kulenin beşinci döşemesi karşı
bloğun çatısıyla aynı hizaya geldiğinde işin yarısı bitmişti.
Son sahnede ikindi güneşine bakın.
#insaat #timelapse #mimari #muhendislik #santiye #kule #shorts #ai
#zamanlanmisfotograf #yapi

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
```

**Sabitlenecek yorum:**

```
Kamera 14 ay boyunca tek noktada durdu: 24 metre yükseklikte, yapıdan 72
metre uzakta, 24 mm. Mesafe seçilmedi, hesaplandı — bir binanın tamamının
dikey kadraja sığması için D = (H − h) / 0,48. Filmdeki her "ne kadar
ilerledi" sorusunun cevabı da aynı sabitlikten geliyor: 5. döşeme karşı
bloğun çatı sırtıyla aynı hizada, 8. döşeme kameranın ufkunda, 18. döşeme
gökyüzünde. Kamera oynasaydı bu ölçümlerin hiçbiri geçerli olmazdı. 🏗️
```

### 🤐 SPOILER BÜTÇESİ — dört yüzey, tek bütçe

| Yüzey | Ne verir | Ne vermez |
|---|---|---|
| Başlık | bedelin SORUSUNU ("kimin güneşi") | cevabı, hangi komşu olduğunu |
| Kapak | bitmiş kuleyi + gölgeyi | sürecin nasıl geçtiğini, kışı, çukuru |
| İlk 2 sn | siluet vaadini (ters sökülme) | bedeli — S0 öğle ışığındadır, gölge tuğla bloğa değmez |
| Açıklama | ölçüyü ve süreci | son sahnenin ne gösterdiğini ("ikindiye bakın" der, ne olduğunu demez) |

```
TEK CÜMLE TESTİ: dört yüzey yan yana konunca bir yabancı, videoyu izlemeden
sürecin dönüm noktasını söyleyebiliyor mu?
→ HAYIR. Dördü de "bir kule yapıldı" der; hiçbiri kulenin gölgesinin karşı
  bloğun cephesini baştan sona kapattığını söylemez. ✅ bütçe tutuyor.
```

---

## 🔒 MASTER LOCK

```
Photorealistic documentary construction photography. Locked-off tripod, one
continuous time-lapse shot, no camera movement of any kind. Physically accurate
daylight. Real weather, real dirt, real clutter. Natural motion blur on moving
people and vehicles. No architectural render look, no CGI aesthetic, no game
engine look, no miniature look, no tilt-shift. Every frame should look like a
real photograph taken from a camera that has been standing in the same place
for a year.
```

**🌇 THE LONG SHADOW — Uzayan Gölge**
_"Boş bir arsa on sekiz kat yükseldi. Ve karşı bloğun güneşini aldı."_
