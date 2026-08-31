# 📤 THE NARROW LOT v2 — GPT SİPARİŞİ (yapıştırılacak)

> **Bu bir kılavuz değil, bir FORMDUR.** v1 ölçümünün tek cümlelik dersi şuydu:
> *brief'in BİREBİR dayattığı her cümle 10/10 aldı; anlattığı ama dayatmadığı
> her şey ya kısaldı ya kayboldu ya yanlış prompta düştü.*
> Bu yüzden v2'de değişmez blokların İngilizce SON HÂLİ aşağıda verilmiştir.
> Bota kalan iş: sahneye özel altı alanı doldurmak.
>
> Genel kılavuz: `kilavuzlar/BES_SAHNE_GPT_BRIEFI.md` (bota YAPIŞTIRILMAZ —
> uzun metin, botun kendi düzenini kurmasına davetiye çıkarıyor [DERS 20]).
> v1 kaydı: `QA/RAPORLAR/THE_NARROW_LOT.md` · Dersler: 18-22
>
> ⛔ **Dönüşte ÜRETİMDEN ÖNCE:** `python3 araclar/prompt_kontrol.py <dosya>`

---

# ⬇️⬇️⬇️ BURADAN AŞAĞISI KOPYALANIR ⬇️⬇️⬇️

---

# 0. ⛔ SÖZLEŞME — önce bunu oku, sonuna kadar uy

Sen dikey (9:16) inşaat timelapse filmleri için prodüksiyon dokümanı yazan bir
sinematograf-prompt mühendisisin. Aşağıdaki sipariş **eksiksiz doldurulmuş bir
formdur.** Senden istenen tek şey, boş bırakılan sahneye özel alanları
doldurup dokümanı yazmaktır.

```
⛔ 1  BLOK ETİKETLERİNİ DEĞİŞTİRME. Aşağıda büyük harfle ve iki nokta ile
      verilen her etiket (Camera: · STRUCTURE: · AT THIS STAGE: ·
      SITE / BACKGROUND: · THE TIME MOMENT: · COMPOSITION: · LIGHTING: ·
      TIME RATE: · ACTIVITY: · SITE TEXTURE: · PHYSICS: · NEGATIVE:)
      prompt gövdesinde AYNEN, satır başında, aynı sırayla yer alır.
      Bunları birleştirme, yeniden adlandırma, nesre çevirme.
      SEBEP: bu etiketler bir makine tarafından okunuyor. v1'de nesre
      çevrildiler ve kapı dokümanı hiç okuyamadı.

⛔ 2  "BİREBİR" YAZAN HER BLOĞU KOPYALA-YAPIŞTIR. Kısaltma, güzelleştirme,
      eşanlamlıyla değiştirme YOK. Bir kelimeyi değiştirmek, o kuralı
      kaldırmaktır. v1'de "soft motion streaks" → "soft motion-blurred
      figures" diye değiştirildi ve o kategori 0/10 aldı.

⛔ 3  BEŞ GÖRSEL PROMPTUN BEŞİNİ DE TAM YAZ. "yukarıdaki gibi", "aynısı",
      "[DEĞİŞMEZLER]" gibi atıf YASAK. Model belgeyi okumaz, promptu çizer.

⛔ 4  HAREKETLE İLGİLİ HER KURAL I2V PROMPTUNDA DA TAM METİN TEKRARLANIR.
      Görsel promptta olması onu muaf tutmaz. Görsel prompt tek kareyi
      yönetir; hareketi I2V yönetir.

⛔ 5  ÇIKTI TÜRKÇE BELGE + İNGİLİZCE PROMPT. Kod bloklarının içi İngilizce,
      dışı Türkçe. Başlık/açıklama/hashtag/kapak metni de İngilizce.

⛔ 6  GÖRSEL ÜRETME. Bu koşunun çıktısı yalnız METİNDİR.

⛔ 7  Soru sorma, onay bekleme, bölüm atlama. Tam dokümanı tek seferde üret.
```

---

# 1. ÇIKTI İSKELETİ — başlıklar birebir böyle

```
# 🏙️ THE NARROW LOT — Dar Parsel
   format satırı · tagline
## 📦 TESLİM YAPISI
## 🚪 KONSEPT KAPISI
## 🔒 DEĞİŞMEZLER TABLOSU
## 📐 KADRAJ DEFTERİ
## 🪜 AŞAMA MERDİVENİ — 5 satır
## ☀️ GÜNEŞ SAATİ
## 🎬 SAHNE 0 — [Kısa Türkçe Başlık]
### 📸 GÖRSEL PROMPT
### 🎥 I2V PROMPT ⭐ BİRİNCİL
### 🎥 T2V PROMPT (yedek)
## 🎬 SAHNE 1 — …   (aynı üç alt blok)
## 🎬 SAHNE 2 — …
## 🎬 SAHNE 3 — …
## 🎬 SAHNE 4 — ⭐ USTA KARE · …
## 🎶 MÜZİK PROMPTU
## 🖼️ KAPAK KARTI
### 🖼️ KAPAK PROMPTU
## 📣 PAKETLEME
## 🔒 MASTER LOCK
## 🔍 QA SPEC
```

Her prompt üç tırnaklı kod bloğunun İÇİNDE durur.

---

# 2. 📦 TESLİM YAPISI — dokümanın ilk sayfasına aynen yaz

```
SAHNE BLOĞU   S0 6,0 · S1 4,0 · S2 6,0 · S3 4,0 · S4 10,0  = 30,0 sn
KAPAK KARTI   1 kart × 5,0 sn                              =  5,0 sn
──────────────────────────────────────────────────────────────────
TOPLAM                                                        35,0 sn

⛔ KAPAK KARTI BİR SAHNE DEĞİLDİR ve ayrı denetlenir.
⛔ SÜRELER EŞİT DEĞİLDİR ve bu bir tercih değil, ölçülmüş bir zorunluluktur:
   v1'de beş kesme de 6,0 sn'ydi ve denetim "METRONOM" hükmü verdi.
   120 BPM'de ölçü 2,0 sn → 6,0=3 ölçü · 4,0=2 · 10,0=5 · toplam 15 ölçü.
   Kesmeler: 0:06,0 · 0:10,0 · 0:16,0 · 0:20,0 · bitiş 0:30,0
```

---

# 3. 🚪 KONSEPT KAPISI — bu üçünü aynen yaz

```
VAAT:    Yıkımdan kalmış, komşularına sıfır dayalı dar bir parselde on sekiz
         katlı bir konut kulesi dikilecek. Parsel 20 × 16 metre; her şey tek
         vinçten ve tek dar giriş şeridinden geçmek zorunda.
DİRENÇ:  ⭐ Bir kış. Kat döngüsü kasım–şubat arasında yavaşlar, kalıp buzda
         bekler, saha çamura gömülür. Kule kışın içinden geçerek çıkar.
BEDEL:   ⭐ Sağdaki ALTI KATLI KIRMIZI TUĞLA BLOĞUN ikindi güneşi.
         S0'da o cephe kaldırımdan çatı sırtına kadar aydınlık.
         S4'te kulenin gölgesi tam üstünde. Kimse bir şey söylemiyor.

① TEK KARE TESTİ       ✅ Tek karede kaç kata gelindiği, tuğla bloğun çatı
                       sırtına bakılarak bir saniyede okunur.
② KİNETİK BAĞIMSIZLIK  ✅ Değişimin tamamı sabit kadrajda görülür.
③ BAŞLIK ŞEMASI        ✅ "Whose sun did it take?" (≤5 kelime)
```

⛔ Bu üç satır v1'de HİÇ yazılmamıştı ve denetim *"THE ONE THING THIS FILM
DOES THAT NOTHING ELSE DOES: NONE FOUND"* dedi. Bir film, yazılmamış bir
bedeli teslim edemez. **S4'ün THE TIME MOMENT satırı BEDELİ taşımak zorundadır.**

---

# 4. 🔒 DEĞİŞMEZLER — İngilizce son hâli. BEŞ GÖRSEL PROMPTA BİREBİR KOPYALA

## 4.1 `Camera:` satırı — beş promptta kelimesi kelimesine aynı

```
Camera: MAIN STATION — fixed tripod bolted to the roof parapet of the block across the street, lens 24.0 metres above street level, 72 metres from the south-west face of the site, bearing 035 degrees, tilt 0 degrees, zero roll. The camera never moves.
```

⛔ Satır başında, `Camera:` ile başlar. Beş sahnenin beşi de ANA istasyondur;
detay istasyonu YOKTUR.

## 4.2 `STRUCTURE:` — YAPI BIBLE · beş promptta kelimesi kelimesine aynı

```
STRUCTURE: A single reinforced-concrete residential tower, 18 storeys and 58.7 metres tall to the top of its parapet when complete, standing on a 20 by 16 metre footprint, with a 6 by 5 column grid at 4.0 metre centres in both directions, a floor-to-floor height of 3.20 metres, one central reinforced-concrete core measuring 8 by 6 metres, a facade of charcoal-grey metal spandrel bands alternating with warm pale-stone vertical panels and floor-to-ceiling glazing, and a flat roof with a 1.10 metre parapet carrying one mechanical enclosure. AT THIS STAGE: [bu sahnede ne kadarı yapılmış — kaç kat, hangi hizaya kadar, hangi malzeme takılı, hangisi HENÜZ takılı DEĞİL]
```

⛔ `AT THIS STAGE:` ayracından ÖNCEKİ metin beş promptta harfi harfine aynıdır.
Değişen tek şey ayraçtan SONRASIDIR.

⭐ Bu blokta her satır bir SAYI taşır. v1'de bina "narrow rectangular … regular
structural bays" diye sayısız tarif edildi ve denetim şunu ölçtü: *"by Clip 5
the finished building has a drastically narrower footprint, rendering it a
completely different structure"* (STRUCTURE IDENTITY 2/10). Aynı filmde SAYIYLA
yazılan arka plan çapaları 10/10 aldı.

## 4.3 `SITE / BACKGROUND:` — beş promptta kelimesi kelimesine aynı

```
SITE / BACKGROUND: To frame right stands a six-storey dark-red brick apartment block with exactly three chimneys on its roof, its roof ridge 19.2 metres above street level, and a single-storey brick annex attached to it at street level on its near side. To frame left stands a four-storey pale-stone building with exactly five evenly spaced windows on its top floor, its parapet 12.8 metres above street level. Behind the site runs a continuous tree-covered ridge with an unchanging profile. The horizon sits at exactly half the frame height. An asphalt access lane enters the frame at the lower right corner and runs along the front of the site.
```

⛔ Bu blok v1'de 10/10 aldı ve filmin "aynı yer" hissini tek başına taşıdı.
**Tek kelimesini değiştirme.** Eklenen tek şey `single-storey brick annex`:
v1'de o ek sayılmamıştı ve 0:24,0'ta kayboldu. Sayılmayan parça, korunmayan
parçadır.

⛔ Bu bloğa GEÇİCİ EKİPMAN GİRMEZ: vinç, çit, iskele, konteyner, kalıp
`ACTIVITY` ya da `SITE TEXTURE` bloğuna yazılır.

## 4.4 `TIME RATE:` — beş görsel promptta VE beş I2V promptunda birebir

```
TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.
```

## 4.5 İnsan kuralı — `ACTIVITY` bloğunun sonuna VE I2V'ye birebir

```
Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles entering and leaving the site render as smeared light and colour trails.
```

⛔ Bu cümle v1'de kısaltıldı ("soft motion-blurred figures") ve denetim şunu
yazdı: *"All moving workers and vehicles render as sharp, distinct figures
without motion blur"* (0/10). Kısaltma, kuralı kaldırmaktır.

## 4.6 Vinç — S2 ve S3'te, görsel VE I2V promptunda birebir

```
The tower crane is a grey flat-top tower crane: one continuous rigid steel lattice mast standing on a concrete base at ground level, with an unbroken load path from the mast to the base to the ground. The jib and the hook stay above the top edge of the frame; only the vertical lattice mast is visible. The mast never floats, never bends and never changes height within a shot.
```

⛔ **BOM VE KANCA KADRAJ DIŞINDADIR.** Yüklü kanca iki filmde iki kez denendi
ve iki kez koptu (*"crane cables intermittently disappear or merge into the
background sky"*). Halat ince, uzun ve gökyüzüne karşı düşük kontrastlı.
Boş kanca hiçbir promptta yazılmaz; yüklü kanca da yazılmaz.

## 4.7 `NEGATIVE:` — beş görsel promptun sonuna birebir, tek paragraf

```
NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same building, same background in every frame: the horizon line, the neighbouring buildings, the annex, the access lane, the trees and the ridge behind them never change shape, position, size, count or spacing. The structure is one single rigid building that only ever gains material — nothing already built is removed, moved, resized or redesigned; the 20 by 16 metre footprint, the 6 by 5 column grid at 4.0 metre centres and the 3.20 metre floor-to-floor height stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hoarding, the safety signage, the cranes, the machinery, the shipping containers, the workers' vests and helmets, the trucks, the scaffolding, the formwork or the facade. Nothing in this frame has been branded, labelled, numbered or annotated by anyone: no company logos, no flags, no floor numbers, no licence plates, no warning pictograms, no measurement or survey marks. No shop signs, no billboards, no street name plates, no shop-front lettering anywhere in the frame. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no crane hanging from nothing, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: mud, tyre ruts, stacked material, offcuts, tarpaulins, puddles and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
```

⭐ Dikkat: bu çekirdek v1'den iki yerde değişti — `count` eklendi (çapa parça
sayısı için) ve `stay exactly as described` cümlesine SAYILAR gömüldü.
"as described" bir işaretçidir; tarif sayısızsa hiçbir şeyi göstermez.

---

# 5. 📐 KADRAJ DEFTERİ — dokümana aynen yaz, hesaplama yapma

Formül: `kare yüzdesi = %50 + 24 × (y − 24) / (36 × 72)` → `%50 + (y − 24)/1,08`

| Ne | y (m) | Kare yüzdesi | Nerede kullanılır |
|---|---:|---:|---|
| yapı tabanı / sokak kotu | 0 | **%27,8** | 5 sahnede de |
| 3. döşeme | 9,6 | %36,7 | S1 kanıtı |
| taş binanın parapeti (çapa ②) | 12,8 | %39,6 | 5 sahnede de |
| ⭐ tuğla bloğun çatı sırtı (çapa ①) | 19,2 | **%45,6** | 5 sahnede de |
| ⭐ 6. döşeme — çapa ① ile AYNI HİZA | 19,2 | **%45,6** | S2 kanıtı |
| ufuk çizgisi (tilt 0° sonucu) | 24,0 | **%50,0** | 5 sahnede de |
| 8. döşeme — ufku geçiş | 25,6 | %51,5 | — |
| arkadaki sırt hattı (çapa ③) | 28,0 | %53,7 | 5 sahnede de |
| 18. döşeme / çatı | 57,6 | %81,1 | S3 · S4 |
| taç parapet | 58,7 | **%82,1** | S3 · S4 |

```
⭐ ÜÇ SAYI FİLMİN OMURGASIDIR:
   19,2 m  tuğla bloğun çatı sırtı = 6. döşeme  → S2'nin kanıtı
   57,6 m  18. döşeme = TAM ÜÇ KATI (3 × 19,2) → S3'ün kanıtı
   58,7 m  taç → %82,1, üst 1/8 sınırı olan %87,5'in ALTINDA ✅

⛔ ÜST SINIR %87,5 · ALT SINIR %25 · SAĞ ŞERİT sağ %13
   v1'de COMPOSITION bloğu hiç yazılmadı ve ilerlemeyi kanıtlayan şeyler
   alt %25'e düştü (SAFE AREA 4/10). Bu blok her promptta zorunludur.
```

---

# 6. 🪜 AŞAMA MERDİVENİ — dokümana aynen yaz

| S | SÜRE | AŞAMA | YENİ OLAN | TEMSİL | MEVSİM TAŞIYICISI | KANIT NESNESİ | İSTASYON |
|:-:|---:|---|---|---|---|---|---|
| 0 | 6,0 | yıkım artığı parsel · ilk kazı | ilk ekskavatör yarığı | 1 gün (temmuz) | yaz · sokak ağaçları tam yapraklı, tuğla cephe baştan sona aydınlık | ilk kesik parselin TAM 20 m genişliğinde | ANA |
| 1 | 4,0 | radye + bodrum + zemin podyumu + ⭐ VİNÇ KAİDESİ | podyum sokak kotuna çıkar | 3 ay (ağu→eki) | sonbahar · yapraklar sarardı | podyum üst kotu taş binanın kaide hizasında · %27,8 | ANA |
| 2 | 6,0 | ⭐ DİRENÇ · vinç kurulur · 6 kat | çekirdek + 6 döşeme | 4 ay (kas→şub) | kış ① · kar birikiyor, dallar çıplak | ⭐ 6. döşeme kenarı tuğla bloğun ÇATI SIRTIYLA TAM AYNI HİZADA · %45,6 | ANA |
| 3 | 4,0 | karkas tamamlanır + cephenin YARISI | 18 kat + taç + cephe alt yarı | 3 ay (mar→may) | kış ② · kar erir, çamur, ilk yeşil | ⭐ 18. döşeme tuğla bloğun çatı sırtının TAM ÜÇ KATI yükseklikte · %81,1 | ANA |
| 4 | 10,0 | ⭐ USTA KARE · cephe kapanır · teslim | cephe tamam, vinç YOK, peyzaj | 1 gün (temmuz, +1 yıl) | yaz · ağaçlar yeniden tam yapraklı, S0 ile AYNI IŞIK | ⭐ BEDEL: kulenin gölgesi tuğla bloğun cephesinde, kaldırımdan çatı sırtına | ANA |

## 6.1 Üç zorunlu satır

```
① KANIT NESNESİ  yukarıdaki tabloda, her sahnede, bir ÇAPAYA GÖRE ölçülmüş.
② LOOP           S4'ün son karesi ile S0'ın ilk karesi AYNI kadraj, AYNI saat,
                 AYNI mevsim ışığı (azimut 252° · yükseklik 34°). Tek fark yapı.
③ SÖKÜM VE KURULUM
                 vinç kaidesi   S1'de DÖKÜLÜR ve S1 karesinde GÖRÜNÜR
                 vinç           S2'de kurulur → S4'ten ÖNCE sökülür
                 şantiye çiti   S0'da kurulur → S4'ten ÖNCE sökülür
                 kalıp/iskele   S1-S3        → S4'ten ÖNCE sökülür
                 ⛔ S4'te söküm "no crane remains anywhere on the plot"
                    kalıbıyla yazılır; "the crane has been dismantled" YAZILMAZ.
```

⛔ v1'de KURULUM satırı yoktu ve denetim şunu buldu: *"a fully erected tower
crane clipping through the structure"* — vincin kaidesi hiçbir sahnede
hazırlanmamıştı.

## 6.2 ⛔ MEVSİM HAZIRLIĞI — giden klibin SON SANİYESİNDE

```
S1'in son saniyesi   ilk kar, istif malzemenin üstüne ve çitin üst kenarına
                     düşmeye başlar; zemin hâlâ koyu ve ıslak
S2'nin son saniyesi  kenardaki kar griye döner, ilk erime suyu izlere sızar
S3'ün son saniyesi   son gri sulu kar kaybolur, sokak ağaçlarında ilk yeşil
```

⛔ Kış İKİ sahne olmak YETMEDİ. v1'de mevsim sırası doğruydu (10/10) ama
denetim şunu yazdı: *"cuts instantly from a clear, dry site to deep winter
snow with no transitional cues in the preceding footage."* Hazırlık **giden**
klibin içinde yaşar. Mevsim bir anahtar değil, bir süreçtir.

## 6.3 ⛔ CEPHE BİR BANT DEĞİLDİR

v1'in tek en ağır hükmü `APPEARING` idi: *"jumps from a bare concrete frame
directly to a fully finished, cladded, glazed and landscaped tower, skipping
all enclosure."* S3'te cephe "bir bant" diye yazılmıştı ve ekranda okunmadı.

```
S3 GÖRSELİNDE cephe kulenin EN AZ ALT YARISINI (1.-9. katlar) kaplar ve
   üst yarı çıplak karkas olarak kalır. Sınır YATAY ve NET bir hattır.
S4'TE o hat tepeye kadar çıkmıştır. Aradaki tek iş adımı budur.
```

---

# 7. ☀️ GÜNEŞ SAATİ — dokümana aynen yaz, her promptta dereceyle tekrarla

| S | Mevsim / saat | Azimut | Yükseklik | Gölge yönü | ⭐ gölge / boy oranı |
|:-:|---|---:|---:|---|---:|
| 0 | yaz · ikindi | 252° | 34° | doğu-kuzeydoğu | **1,5×** |
| 1 | sonbahar · öğleden sonra | 225° | 30° | kuzeydoğu | 1,7× |
| 2 | kış · öğle sonrası | 196° | 18° | kuzey-kuzeydoğu | **3,1×** |
| 3 | geç kış / erken ilkbahar | 214° | 26° | kuzeydoğu | 2,1× |
| 4 | yaz · ikindi — **S0 ile BİREBİR** | 252° | 34° | doğu-kuzeydoğu | **1,5×** |

```
⭐ SON SÜTUN DENETLENİYOR. Rubrik bir nesnenin boyunu gölgesine bölüp
   ima edilen güneş yüksekliğini hesaplıyor. v1'de bütün kliplerde ~45°
   ölçüldü — yani kışla yaz aynı gölgeyi verdi (SHADOW VS SUN HEIGHT 2/10).
   Kışta gölge nesnenin boyunun ÜÇ KATIDIR; yazda bir buçuk katı.
   Bu farkı prompta AÇIKÇA yaz: "the shadow of the crane mast is three times
   its own height" gibi.

⛔ SAHNE İÇİ: her klipte BİR GÜN geçer, güneş TEK YÖNDE ilerler ve gölge
   kadrajı SÜPÜRÜR. v1'de beş klibin beşinde de gölge açı değişimi 0 derece
   ölçüldü — çünkü bu sayılar yalnız görsel promptta kaldı, I2V'ye hiç
   girmedi. Videoyu üreten prompt I2V'dir.
⛔ MEVSİM tek yönlü: yaz → sonbahar → kış① → kış② → yaz.
```

---

# 8. 📸 GÖRSEL PROMPT — beş sahnenin beşi için, bu sırayla

Blokların arasında **boş satır** bırak. Hedef uzunluk 4.500-5.500 karakter.
`Camera:` · `STRUCTURE:`+`AT THIS STAGE:` · `SITE / BACKGROUND:` · `TIME RATE:`
· vinç bloğu · insan kuralı · `NEGATIVE:` yukarıdan BİREBİR kopyalanır.
Senin yazacağın alanlar köşeli parantezle işaretli.

```
Photorealistic documentary construction photograph — Scene [N] of 5. Vertical time-lapse of a high-rise residential tower on a tight urban infill site.
Lens: 24mm spherical, f/8, ISO 100.
[§4.1 Camera: satırı — BİREBİR]

[§4.2 STRUCTURE: bloğu — BİREBİR] AT THIS STAGE: [bu sahnede ne kadarı yapılmış]

[§4.3 SITE / BACKGROUND: bloğu — BİREBİR]

THE TIME MOMENT: [§6 tablosundaki KANIT NESNESİ, bir çapaya göre ölçülmüş tek cümle]

COMPOSITION: Vertical 9:16. [taban ve çalışma seviyesi §5'teki kare yüzdesiyle] The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the bottom quarter or the right eighth of the frame.

LIGHTING: [mevsim, saat]. Sun azimuth [§7] degrees, elevation [§7] degrees, shadows falling to the [§7 yön] and running [§7 oran] times the height of the objects that cast them. [renk sıcaklığı · gökyüzü · gölge sertliği]

[§4.4 TIME RATE: bloğu — BİREBİR]

ACTIVITY: [bu sahnedeki makineler ve konumları — TEK iş adımı] [S2/S3 ise §4.6 vinç bloğu — BİREBİR] [§4.5 insan kuralı — BİREBİR]

SITE TEXTURE: [⛔ BEŞ SAHNEDE FARKLI — §9'a bak]

PHYSICS: [neyin neye oturduğu · neyin temas hâlinde olduğu · desteksiz hiçbir şey yok]

[§4.7 NEGATIVE: bloğu — BİREBİR]
Output: 9:16, 4K, no text, no watermark.
```

---

# 9. ⛔ SITE TEXTURE — beş sahnede FARKLI ve BİRİKEN

v1'de bu blok beş sahnede aynıydı ve denetim şunu ölçtü: *"mud ruts and
puddles maintain that exact identical fluid geometry despite the addition of
snow and months of time passing"* (WEAR AND ACCUMULATION 2/10). Şantiye
birebir aynı kalınca film "aynı yer" oldu ama "geçen zaman" olmadı.

```
S0  kuru kırık beton, moloz yığınları, dağınık toprak, birkaç lastik izi,
    sığ toz, tek bir sığ birikinti
S1  derin çamur, geniş ve üst üste binmiş lastik izleri, büyük birikintiler,
    ıslak beton sıçraması, donatı demeti istifi, kalıp kerestesi
S2  kirli çamurun üstünde gri, ezilmiş kar; trafik yollarında kar yok, koyu
    çamur var; buzlanmış birikinti kenarları; brandalar karla ağırlaşmış
S3  ⭐ filmin en dağınık hâli: eriyen sulu kar, izlerde akan su, geniş ve
    bulanık birikintiler, cephe paneli kasaları, mastik ekipmanı, artık yığını
S4  yeni kaldırım; kaldırım taşı kenarında kalmış kurumuş çamur, tek bir
    artık malzeme istifi duvar dibinde, son giriş izleri
```

⛔ Bu blok "değişmez" DEĞİLDİR. Çamur, iz, birikinti, istif, kar: hepsi
`SITE TEXTURE`'a girer ve sahne sahne BİRİKİR.

---

# 10. 🎥 I2V PROMPT — ⭐ FİLMİN GERÇEK PROMPTU BUDUR

## 10.1 Paragraf sırası — sıra da bir kuraldır

```
1 AÇILIŞ CÜMLESİ      birebir, tek başına
2 ⭐ ZAMAN VE GÖKYÜZÜ  ilk anlatılan hareket GÖKYÜZÜ ve GÖLGE olmalı
3 İŞ ADIMI            tek adım, yöntemiyle + zemin durumu + mevsim hazırlığı
4 DEĞİŞMEYECEKLER     birebir
5 KAPANIŞ             kamera + master lock
```

⛔ 2. paragraf 3.'den ÖNCE gelir. v1'de iş adımı önce, gölge sonra anlatıldı;
model önce anlatılanı canlandırdı, sonra anlatılanı DONDURDU. Denetim:
*"people and machinery move at a highly accelerated time-lapse rate, while
environmental time (sun, shadows, clouds) runs at a rate of zero."*

## 10.2 İskelet

```
The scene begins exactly as the provided image.

Everything in this shot is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed. The sun moves visibly across the sky during these [süre] seconds: it stands at azimuth [§7] degrees and elevation [§7] degrees at the start and drops to azimuth [+14°] degrees and elevation [−8°] degrees at the end, so the shadow of the six-storey brick block starts [nerede — ölçülebilir] and ends [nerede — ölçülebilir], sweeping [yön] across [yüzey], and it stays [§7 oran] times the height of the block that casts it. Clouds cross the entire frame in long smooth streaks, always from the north-west, and the sky is never still for a single frame.

[temsil süre] passes on the ground. [TEK BİR iş adımı, yöntemiyle: hangi makine, hangi döngü, ne takılıyor, neye oturuyor]. [malzeme geliyor]. [§4.5 insan kuralı — BİREBİR] [zemin durumu §9'a göre DEĞİŞİR]. [S1/S2/S3 ise §6.2 mevsim hazırlığı — son saniyede].

The framing is identical in the first frame and in the last frame: the six-storey dark-red brick apartment block with its three chimneys occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The camera does not move at any point. The brick block with its annex, the four-storey pale-stone building and the tree-covered ridge behind the site stay exactly where they are, at exactly the same size, shape and count, for the whole shot. Nothing already built is removed, moved or resized, and no new floor appears without support beneath it. [S2/S3 ise: The jib and the hook stay above the top edge of the frame; only the vertical lattice mast is visible, standing on its concrete base at ground level.]

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## 10.3 ⛔ I2V'de OLMAYACAKLAR

```
· Yapıyı, sahayı ve arka planı YENİDEN TARİF ETME — görsel zaten içeriyor.
· Şu üç ifade GEÇMEZ: "column grid" · "bay spacing" · "footprint".
· Olumsuz hız yasağı TEK BAŞINA yazılmaz. v1'de iki I2V'de "no normal-speed
  motion" yazılıydı ve dünya yine dondu. Yasak modele ne YAPACAĞINI söylemez.
· İki iş adımı. Bir klip = bir gün + BİR görünür adım.
```

---

# 11. 🎥 T2V PROMPT (yedek) — 5-7 vuruş, her vuruş TEK zaman olayı

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, [süre] seconds. Lens: 24mm on a fixed tripod, 24.0 metres above street level, 72 metres from the south-west face of the site, bearing 035 degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — [açılış durumu + üç çapa]
At [x]s — [makine döngüsü]
At [x]s — [gölge süpürmesi ve bulut çizgileri]
At [x]s — [⭐ İŞ ADIMI: kanıt nesnesi ekranda değişir]
At [x]s — [ışık döner, gölge uzar]
By [süre]s — [kapanış] Hard cut to Scene [N+1].

The camera never moves. The six-storey brick block with its three chimneys and its annex, the four-storey pale-stone building and the tree-covered ridge never change shape, size, count or position; the horizon stays at exactly half the frame height. No readable text, letters, digits or logos anywhere. No architectural render look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

# 12. 🎶 MÜZİK — tek parça, 35 saniye

```
Instrumental score for a 35-second vertical construction time-lapse: a 30-second scene block of five shots lasting 6.0, 4.0, 6.0, 4.0 and 10.0 seconds, followed by a 5-second end card.
No lyrics, no voice, no melody line, no traditional song structure.

Genre: [tür]
Tempo: 120 BPM, strict and bar-aligned. One bar is 2.0 seconds, so the shots are 3, 2, 3, 2 and 5 bars long and every cut falls on a bar line.

Layers (one added per shot, none removed until the final bars):
1. [S0 — dry pulse on the first beat of each bar]
2. [S1 — low bass note, motionless]
3. [S2 — the winter layer: bowed string friction, cold and wide. It never leaves]
4. [S3 — metallic percussion, the formwork and hammer rhythm]
5. [S4 — broad warm chord bed under everything]

Dynamic map across 35 seconds:
  0.0-1.5    silence — only the site's own ambience
  1.5-6.0    layer 1 alone
  6.0-10.0   layer 2 enters
  10.0-16.0  layer 3 enters — the coldest and widest moment
  16.0-20.0  layer 4 enters
  20.0-30.0  layer 5 enters, the stack sits together
  30.0-35.0  end card: everything resolves and decays; the last 1.5 seconds
             carry only ambience

Phone-speaker rule: Every sub-bass element below 150 Hz is doubled by its own upper harmonics at roughly 100, 150 and 200 Hz so the fundamental is implied rather than required; the low end is never the only carrier of the weight.
Reference feel: [iki gerçek besteci — ALINTI ÜRETME]
```

---

# 13. 🖼️ KAPAK KARTI — v1'de ÜRETİLMEDİ, bu sefer zorunlu

```
S4 GÖRSEL PROMPTUNUN BİREBİR KOPYASI + şu ek satır:
```

```
Leave the upper middle third of the frame visually simple and low-contrast so that a title can be set over it: no structural detail, no strong edge and no bright object between roughly forty and seventy percent of frame height on the left two thirds of the picture.
Output: 9:16, 4K, no text, no watermark.
```

```
BAŞLIK   İngilizce, en fazla 3 kelime · büyük harf yüksekliği ≥ %8 (≥154 px)
         y = 500-1400 bandı · sağ 242 px ve sol 122 px'e girmez
         kontrast ≥ 4,5:1 · tek ağırlık · gölge/kontur/parlama YOK
         ⛔ Kart 5 saniye HAREKETSİZ. Metin post-prodüksiyonda dizilir;
            prompt hâlâ "no text" der.
⛔ Kapak S4'ten TÜRETİLİR, sıfırdan üretilmez. v1'de kart hiç yoktu ve
   ④ COVER AND CONTENT 0/10 aldı.
```

---

# 14. 📣 PAKETLEME — İngilizce

```
TITLES
1. [≤40 chars — merak sorusu, spoiler yok]
2. [≤40 chars]
3. [≤40 chars]

DESCRIPTION
[hook line — one sentence, the promise]
[2-3 sentences: what was built, what resisted, one measured fact]
[8-12 hashtags: 3 broad · 5 niche · 2-4 structure-specific]

This video was generated with AI. It does not document a real project.

PINNED COMMENT
[the real engineering behind it, one paragraph, no company names]
```

---

# 15. 🔒 MASTER LOCK — dokümanın sonuna, değişmeden

```
Photorealistic documentary construction photography. Locked-off tripod, one continuous time-lapse shot, no camera movement of any kind. Physically accurate daylight. Real weather, real dirt, real clutter. Natural motion blur on moving people and vehicles. No architectural render look, no CGI aesthetic, no game engine look, no miniature look, no tilt-shift. Every frame should look like a real photograph taken from a camera that has been standing in the same place for a year.
```

---

# 16. 🔍 QA SPEC — dokümanın son bölümü

```
0. KÜNYE      film · 9:16 · 5 sahne (6,0/4,0/6,0/4,0/10,0 = 30,0) + kart 5,0
              yapı · saha · zaman yayı 12 ay · kamera · üretim sırası TERS
1. ⛔ FİNAL VURUŞ KANITI
   SAHNE   S4      SANİYE  0:29,0
   GÖRÜLMESİ GEREKEN ŞEY: Kulenin gölgesi, kadrajın sağındaki ALTI KATLI
     KIRMIZI TUĞLA BLOĞUN cephesini KALDIRIMDAN ÇATI SIRTINA kadar kaplıyor,
     ve arkasındaki gökyüzü hâlâ aydınlık. Parselde hiçbir vinç yok.
   KOMUT   ffmpeg -ss 29.0 -i teslim.mp4 -frames:v 1 kanit.jpg
2. KADRAJ KİLİTLERİ   §5 tablosu · tolerans ± %2 · üst %87,5 · alt %25 · sağ %13
3. DEĞİŞMEZLİK KİLİTLERİ  kamera 0 kare hareket · istasyon 6 alanı birebir ·
   çapa ① 6 kat + 3 baca + EK · çapa ② 4 kat + 5 pencere · çapa ③ profil ·
   ufuk %50,0 · yapı 20×16 m + 6×5 aks + 3,20 m kat + antrasit/taş cephe
4. MONOTON BÜYÜME KİLİDİ  sahne sahne EKLENEN ve SÖKÜLEN
5. SÖKÜM VE KURULUM TAKVİMİ  §6.1 ③
6. GÜNEŞ KİLİDİ  §7 tablosu + gölge/boy oranları
```

---

# 17. ⛔ ÖZ DENETİM — dokümanı teslim etmeden önce tek tek işaretle

```
 1 □ "TESLİM YAPISI" ve "KAPAK KARTI" satırları var.
 2 □ Aşama merdiveninde "| S | SÜRE |" başlığı ve "MEVSİM TAŞIYICISI" sütunu var.
 3 □ Sahne başlıkları "## 🎬 SAHNE N — …", N = 0,1,2,3,4.
 4 □ Alt başlıklar birebir: "### 📸 GÖRSEL PROMPT" · "### 🎥 I2V PROMPT ⭐
     BİRİNCİL" · "### 🎥 T2V PROMPT (yedek)".
 5 □ 5 görsel + 5 I2V + 5 T2V = 15 prompt, hepsi kod bloğu içinde.
 6 □ Görsel promptun ilk satırında "Scene N of 5", N sahne sırasıyla aynı.
 7 □ "Camera:" satırı SATIR BAŞINDA ve §4.1'in birebir kopyası (5/5).
 8 □ "STRUCTURE:" + "AT THIS STAGE:" var; ayraçtan ÖNCESİ 5 promptta
     KELİMESİ KELİMESİNE aynı ve §4.2'nin kopyası.
 9 □ "SITE / BACKGROUND:" 5 promptta KELİMESİ KELİMESİNE aynı, §4.3'ün kopyası,
     ve arkasından BOŞ SATIR geliyor.
10 □ "COMPOSITION:" bloğu 5/5 var ve "top eighth" · "bottom quarter" ·
     "right eighth" ifadelerini taşıyor.
11 □ "sun azimuth NNN degrees, elevation NN degrees" 5/5, §7 tablosuyla aynı,
     ve gölge/boy oranı yazılı.
12 □ "TIME RATE:" bloğu 5 GÖRSEL promptta VAR.
13 □ ⭐ TIME RATE cümlesi 5 I2V promptunda DA VAR, ve I2V'de güneşin
     BAŞLANGIÇ ve BİTİŞ azimut/yüksekliği dereceyle yazılı.
14 □ ⭐ I2V'de gökyüzü/gölge paragrafı İŞ ADIMI paragrafından ÖNCE.
15 □ İnsan kuralı (§4.5) TAM METİN, 5 görselde VE 5 I2V'de.
16 □ Vinç görünen sahnelerde §4.6 bloğu birebir; bom KADRAJ DIŞI.
     "empty hook" ve gökyüzüne karşı yüklü kanca hiçbir yerde yok.
17 □ Vinç kaidesi S1'de dökülüyor ve S1 görselinde görünüyor.
18 □ S4'te söküm "no crane remains anywhere on the plot" kalıbıyla.
19 □ "NEGATIVE:" bloğu §4.7'nin birebir kopyası (5/5).
20 □ SITE TEXTURE beş sahnede FARKLI ve §9'a göre birikiyor.
21 □ Mevsim hazırlığı S1, S2 ve S3'ün I2V'sinde son saniyede var (§6.2).
22 □ S3 görselinde cephe kulenin ALT YARISINI kaplıyor (§6.3).
23 □ I2V ilk cümlesi tam olarak "The scene begins exactly as the provided
     image." · ayrıca "does not move at any point" · "identical in the first
     frame and in the last frame" · "occupies exactly the same width of the
     frame" geçiyor.
24 □ I2V'de "column grid" · "bay spacing" · "footprint" GEÇMİYOR.
25 □ I2V ve T2V'de "zero movement" ya da "never moves" geçiyor.
26 □ Hiçbir promptta köşeli parantez atfı yok.
27 □ Olumlu kamera hareketi kelimesi yok (pan/tilt/zoom/dolly/orbit/push in);
     yalnız "no/never/zero" ile ya da "tilt 0 degrees" olarak geçebilir.
28 □ Görsel prompt uzunlukları 2.000-6.000 karakter bandında.
29 □ Süre sütunu 6,0 · 4,0 · 6,0 · 4,0 · 10,0 ve toplamı 30,0.
30 □ Kapak kartı bölümü VAR ve S4'ten türetilmiş.
31 □ Müzik promptunda 120 BPM ve 3/2/3/2/5 ölçü dağılımı yazılı.
32 □ Paketlemede AI beyanı satırı var.
```

**Dokümanın en sonuna tek satır yaz:** `ÖZ DENETİM: 32/32 ✅`
Eksik varsa madde numaralarını yaz ve eksiği tamamla.

# ⬆️⬆️⬆️ BURAYA KADAR KOPYALANIR ⬆️⬆️⬆️
