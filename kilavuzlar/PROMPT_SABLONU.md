# 🧩 PROMPT ŞABLONU — Görsel · İKİ UÇLU I2V

> Üç iskelet, sabit sırayla. Her prompt **kendi başına** çalışır: belge atfı
> (`[DEĞİŞMEZLER]`, `[YAPI BIBLE]`) yasaktır — model belgeyi okumaz, promptu
> çizer. Uzunluk hedefi: görsel promptu 2.000-4.000 karakter [P2-j] — kapı
> eşiği hâlâ 6.000 (DERS 2); ilk üretimden sonra ölçülüp daraltılır.

---

# 1. 📸 GÖRSEL PROMPT İSKELETİ

Sıra sabittir. Bir bloğu atlamak, modelin o bloğu kendi uydurması demektir.

```
Photorealistic documentary construction photograph — Scene [N] of 10. Vertical
time-lapse of [yapı tipi] on [saha].
Lens: [f]mm spherical, f/[X], ISO [X].
Camera: [İSTASYON ADI] — fixed tripod bolted to [neye], lens [h] metres above
[neyin] level, [D] metres from [neyin] face of the site, bearing [X]°, tilt
[X]°, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — bitmiş hâlin geometrisi] + AT THIS STAGE:
[bu aşamada ne kadarı yapılmış · kaç kat · hangi hizaya kadar · hangi malzeme
takılı · hangisi HENÜZ takılı değil]

SITE / BACKGROUND: [arka plan çapaları tam metni — ①②③ · ufuk · çit · yol]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + neye göre ölçüldüğü]

COMPOSITION: Vertical 9:16. [taç ve çalışma seviyesi kare yüzdesiyle] The crown
of the structure sits below the top eighth of the frame and the working level
sits above the bottom quarter of the frame; nothing that proves progress falls
into the right eighth of the frame.

LIGHTING: sun azimuth [X]°, elevation [X]°, shadows falling to the [yön].
[mevsim rengi · gökyüzü · gölge sertliği]

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds,
the shadows, the machines, the people and the vehicles all move at the same
accelerated speed. Each object retains physically correct relative motion under that
shared compression. Moving vehicles render with heavy motion blur and streaking.
Nothing in the frame moves at normal speed.

ACTIVITY: [makineler ve konumları] Workers appear only as soft motion streaks
and blurred figures, none of them sharp, none of them facing the camera, no
readable face anywhere. Vehicles render as smeared light and colour trails.
          ⛔ İNSANSIZ FİLMDE bu cümle YAZILMAZ; yerine "No people are present."
          [DERS 33 — koşullu cümle astronot üretti]

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts,
tarpaulins and untidy clutter across the working area.

PHYSICS: [neyin asılı olduğu · yük yolu · neyin temas hâlinde olduğu]

NEGATIVE: [KILAVUZ_REHBERI §7 negatif çekirdek tam metni + varsa vinç bloğu +
saha kartı eki + yapı kartı eki]

Output: 9:16, 4K, no text, no watermark.
```

### ⛔ İki blok asla kısaltılmaz
```
STRUCTURE'ın YAPI BIBLE kısmı  → ON promptta BİREBİR aynı kelimeler
SITE / BACKGROUND              → ON promptta BİREBİR aynı kelimeler
Değişen tek şey: "AT THIS STAGE" cümlesi ve THE TIME MOMENT.
Izgara 10 sahnedir; sayı değişirse "Scene N of X" hepsinde birlikte değişir.
```

### ⭐ TIME RATE ÖZNE LİSTESİ SAHADAN YAZILIR [P1-e]
```
İMZA KORUNUR   "time-lapsed at the same rate" — kapı bunu arar
LİSTE DEĞİŞİR  yalnız o kadrajda VAR OLAN özneler: şehir kulesinde bulut ·
               gölge · makine · insan · araç; Ay ovasında gölge · robotik
               araç · mafsallı makine · güneşi izleyen panel.
⛔ Negatifte yasaklanan özne (no clouds · no people) pozitif listeye GİRMEZ —
   istenmeyeni modele hatırlatmaktır.
⭐ VE PROMPT YALNIZ MODELİN ÜRETECEĞİNİ TAŞIR [P1-j]: kırpma payı, kesme anı,
   başlık, söküm takvimi insanın işidir ve planda kalır.
```

### ⛔ KORPUS CÜMLESİ — fotoğrafı olmayan sahada [DERS 34]
```
Ay · derin deniz · kutup içi: "photorealistic documentary" boş işaretçidir.
Gerçek bir korpus POZİTİF adlandırılır: "looks like a 1970s surface photograph
from a hand-held 70 mm film camera: flat grey regolith, blown highlights,
razor-edged black shadows, slight grain, no haze, no depth fog, no rim light."
⚠️ Kilit ölçülmedi; ilk uzay filminde ① SURFACE TRUTH'tan okunur.
```

### ⛔ AT THIS STAGE YALNIZ KAMERANIN GÖRDÜĞÜNÜ YAZAR [P2-g]
```
"the tube has been driven 300 metres" ekranda yoktur; prompta girmez.
Görünmeyen ilerleme SPEC'te "gizli iş + görünür vekil" satırıdır (⑧ C1);
prompta yalnız VEKİL girer (portal önü · pasa sekisi · başlık duvarı).
```

### ⛔ SITE / BACKGROUND'a GEÇİCİ EKİPMAN GİRMEZ [DERS 1]
```
GİRER      komşu yapı · ağaç · sırt hattı · ufuk · yol · kalıcı duvar
GİRMEZ     şantiye çiti · vinç · iskele · konteyner · kalıp · platform
           → bunlar SITE TEXTURE ya da ACTIVITY bloğuna yazılır
Sebep: bu nesneler sökülür. Değişmez bloğa yazılırlarsa, söküldükleri
sahnede blok kendiliğinden değişir ve on promptun birebir tekrarı kırılır.
```

### ⛔ KAMERA KİLİDİ POZİTİF VE ÖLÇÜLEBİLİR YAZILIR [DERS 6]
```
YETMEZ   "no zoom, no pan, no tilt"      → v1'de bütün klip push-in yaptı
YETER    "the framing is identical in the first frame and in the last frame:
          the red brick block occupies exactly the same width of the frame at
          both ends of the shot, and the horizon stays at exactly half the
          frame height throughout."
Yasak modele NE YAPACAĞINI söylemez; ölçülebilir bir çapa söyler.
```

### ⛔ VİNÇ KANCASI: YÜKLÜ VEYA KADRAJ DIŞI [DERS 8]
```
Her sahnede ikisinden biri yazılır:
  (a) "the hook block hangs vertically on a taut cable and carries a visible
       load"                                    ← boş kanca ASLA yazılmaz
  (b) "the jib stays above the top edge of the frame; only the mast is visible"
Vinç TİPİ (renk + flat-top/saddle jib) değişmezler bloğunda durur.
```

### ⭐ BETON RENK SINIRI — THE TIME MOMENT'IN İKİNCİ TAŞIYICISI [A4-a]

```
THE TIME MOMENT bloğu bugün tek bir kanıt taşıyor: yapının bir arka plan
çapasına göre nerede olduğu ("the twelfth slab edge now sits level with the
roof ridge"). Beton kürlenmesi İKİNCİ bir kanıt verir ve o kanıt çapaya
değil, ZAMANA bağlıdır — ardışık dökümler arasında kaç ay geçtiğini gösterir.

KİLİT  "The lower floors are pale bone-grey fully cured concrete, while the
        slab poured most recently is still dark, wet and blotchy — the colour
        boundary between them sits exactly at the seventh floor slab edge."

⭐ NEREDE İŞE YARAR: mevsim taşıyıcısı olmayan sahada (çöl · kaya vadisi)
   tek çalışan taşıyıcıdır ve ③ SEASON CARRIER'ın "Indeterminate" hükmünü
   [DERS 14] doğrudan hedefler. Fizik ve tam metin: ZAMAN_VE_ISIK §6.
⛔ SINIR HANGİ KATTA, SAYIYLA yazılır. "Alt katlar daha açık" bir tarif
   değildir — DERS 19'un beton hâli olur.
```

### ⭐ GECE FİZİĞİ — üç kilit, yalnız şehir DIŞI sahalarda [A4-c · d · e]

```
⛔ Bu üçü negatif çekirdeğin "no star trails" maddesi saha kartıyla
   çeliştiğinde kullanılır [DERS 16]. Şehir gecesinde çekirdek geçerlidir.

① "The stars render as concentric arcs about thirty degrees long, centred on
    the pole star, consistent with a two-hour exposure."
   ⛔ Yay DERECESİ ve pozlama SAATİ birlikte — "short" bir sayı değildir.
② "The obstruction light at the crane mast head reads as a single bright red
    pixel in some frames and is completely dark in others, never a
    continuous glow."
③ "Vehicles on the site road leave unbroken white and red light trails that
    run the full length of their path across the frame."

Sayı tablosu ve gerekçeleri: ZAMAN_VE_ISIK §5.
```

---

## ⭐ 08.09.2026 — THE DUST YEAR ÖLÇÜMÜ: İSKELETİN ÜÇ SATIRI DEĞİŞTİ

```
① STRUCTURE SIRASI TERSİNE DÖNDÜ  [DERS 36]
   ⛔ ESKİ  STRUCTURE: bitmiş yapının tam tarifi … AT THIS STAGE: bu sahne
   ✅ YENİ  STRUCTURE: yalnız BU SAHNEDE AYAKTA OLAN, sayılarıyla
            WHEN COMPLETE: tek cümle, yalnız TÜR — "When finished this will
            be a pressurised surface base."
   Ölçüldü: altı filmin altısında tam-hâl tarifi ara hâlden UZUN
   (1,08x … 2,58x) ve altısında da ② hükmü DIFFERENT · APPEARING.
   KAPI  prompt_kontrol.py §10c — tam hâl > ara hâl ise BLOCK.

② METİN YASAĞI NESNE ADI ANMAZ  [DERS 35]
   ⛔ "No readable text … not on the machinery, the rover, the module,
      the habitat, the panel, the mast, the radiator…"
   ✅ "No readable text, letters, digits, numbers or symbols anywhere in
      the frame, on any surface. Nothing here has been branded, labelled,
      numbered or annotated by anyone."
   Ölçüldü: "module" on promptun onunda YALNIZ bu listede geçti; ekranda
   "utility modules" belirdi, dört saniye durdu, kayboldu.
   KAPI  prompt_kontrol.py §10c — 'not on the X, the Y…' → BLOCK.

③ İNSANSIZ SAHADA MAKİNE ADI  [DERS 41]
   ⛔ dozer · bulldozer · loader · grader · excavator · digger
      ('rover' eki gövdeyi değiştirmiyor — ölçüldü)
   ✅ tracked blade unit · bucket unit · regolith hauler · sintering
      crawler · manipulator arm
   + gövde bir kez POZİTİF kapatılır:
      "Every machine is a sealed robotic unit with no cab, no window,
       no seat and no handrail."
   KAPI  prompt_kontrol.py §10c — insansız beyan + elle-kullanılan ad → BLOCK.
```

# 2. 🎥 I2V PROMPT İSKELETİ ⭐ TEK VİDEO PROMPTU

Bu akışın **tek** video promptu budur: iki görsel önce üretilir ve onaylanır,
video ikisinin ARASINDA doğar [KILAVUZ_REHBERI §2.7].

⛔ **İKİ UÇ DA BİREBİR CÜMLEYLE KİLİTLENİR.** İlk cümle klibin İLK karesini,
ikinci cümle SON karesini bağlar; ikisi de prompt kapısının aradığı imzadır
ve nesre çevrilirse kapı BLOCK verir [DERS 20].

```
The scene begins exactly as the provided image. The shot ends exactly on the
second provided image: its last frame is that image, matched frame for frame —
same framing, same light, same objects in the same places.

[ZAMAN GEÇİŞİ — düz nesir, zaman damgasız, akıcı paragraf:]
Time passes across [temsil süre]. The shadow of [çapa] sweeps [yön] across
[yüzey] as the sun climbs and falls. Clouds streak across the sky in long
smooth trails, always from the [yön]. [makine döngüsü]. [iş adımı — TEK BİR
adım]. [araç izleri].

[DEĞİŞMEYECEKLER — zorunlu paragraf:]
The camera does not move at any point. The framing is identical in the first
and last frame. [çapa ①], [çapa ②] and [çapa ③] stay exactly where they are,
at exactly the same size and shape, for the whole shot. Nothing already built
is removed, moved or resized. No new floor appears without support beneath it.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom,
no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No
cuts. Photorealistic documentary time-lapse cinematography.
```

> ⭐ **I2V FİİL AĞIRLIKLIDIR [P2-d]:** zaman paragrafı bir DÖNGÜ olarak yazılır
> (makine adımı → malzeme adımı → sonuç → tekrar). Hedef durumu ANLATMAK artık
> gerekmez — hedef KAREDİR ve promptun ikinci cümlesi onu zaten bağlar.
> "Four months pass" taşıyıcı değildir; güneş açıları [DERS 18] kalır.
>
> ⛔ **I2V'de yapıyı, sahayı ve arka planı YENİDEN TARİF ETME.** Görsel zaten
> içeriyor; yeniden tarif edersen model görseli kullanmak yerine yeniden inşa
> etmeye çalışır ve kadraj kayar. Yalnız **zamanın geçişi** ve
> **değişmeyecekler** yazılır.

---

# 3. ⛔ T2V PROMPT İSKELETİ — 08.09.2026'DA KALDIRILDI

> **Bu bölümde bir iskelet vardı ve silindi.** Sebep formatın kendisidir
> [KILAVUZ_REHBERI §2.7 ②]: metinden üretilen bir klip iki uca kilitlenemez —
> ne ilk karesi bir önceki görseldir, ne son karesi bir sonraki. Zinciri
> taşımaz ve dikişi tam da beş filmde beş kez kırıldığı yerde kırar.

```
YEDEK ARTIK ŞUDUR: bir klip tutmazsa AYNI İKİ KAREDEN yeniden koşulur.
Kare değişmez, prompt değişmez, tohum değişir.
⛔ Tutmayan klip için metin yolu AÇILMAZ — o yol dikişi geri getirir.
⛔ prompt_kontrol.py planda T2V bloğu görürse BLOCK verir.
KALDIRDIĞI: referans görsel olmadan çekim yapabilme imkânı. Karşılığı,
            dikişin yapısal olarak kapanmasıdır [§2.7 "BEDELİ"].
```

---

# 4. ✍️ DOLDURULMUŞ ÖRNEK — S3 (kat yığılması, kış)

### 📸 GÖRSEL PROMPT

```
Photorealistic documentary construction photograph — Scene 6 of 10. Vertical time-lapse of a high-rise tower on a tight urban infill site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the roof parapet of the block across the street, lens 24.0 metres above street level, 72 metres from the south face of the site, bearing 215 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: A single reinforced-concrete tower, 18 storeys and 58 metres tall when complete, on a 24 by 18 metre footprint, with a 6 by 4 column grid at 4.0 metre centres, a floor-to-floor height of 3.20 metres, one concrete core in the north-east corner, an anthracite aluminium curtain wall with light grey glass, a flat roof with a 1.10 metre parapet and a single mechanical enclosure. AT THIS STAGE: twelve floors of bare grey concrete frame stand, the core runs two floors above the topmost slab, the top slab carries yellow-brown timber formwork tables and a forest of steel props, and no cladding of any kind has been fitted anywhere — every floor is open to the weather.

SITE / BACKGROUND: To frame right stands a five-storey red brick apartment block with two chimneys on its roof. To frame left stands a single leaning cypress tree. Behind the site runs a low ridge line carrying a scattered silhouette of small buildings. The horizon sits at exactly half the frame height. A blue hoarding panel fence encloses the site, and an asphalt road enters the frame at the lower right corner.

THE TIME MOMENT: The twelfth slab edge now sits exactly level with the roof ridge of the red brick block to frame right — three floors higher than the last time this camera looked.

COMPOSITION: Vertical 9:16. The base of the tower sits at about twenty-eight percent of frame height and the topmost slab at about sixty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Winter. Sun azimuth 196 degrees, elevation 19 degrees, shadows falling long to the north-east. Flat white-grey sky, cold 6500K light, low contrast, long blue shadows across the site.

ACTIVITY: A tower crane stands against the north face with its jib over the top slab. A concrete pump sits inside the hoarding. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: Grey tracked snow piled at the edges and partly melted, mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The crane is one continuous rigid steel lattice mast standing on a concrete base at ground level, with an unbroken load path from the hook to the trolley to the jib to the mast to the ground. The hook block hangs vertically under the trolley on a single taut cable. Every slab rests on props and columns beneath it; nothing is unsupported.

NEGATIVE: [KILAVUZ_REHBERI §7 negatif çekirdek + vinç bloğu + §3.1 şehir eki + §3.5 kar eki]
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 I2V PROMPT

```
The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.

Four months pass. The long blue shadow of the red brick block sweeps slowly across the site from the north-east to the north-west as the low winter sun crosses the sky, and thin grey cloud streaks across the frame in long smooth trails, always from the north-west. The tower crane slews slowly back and forth over the top slab and its hook block rises and falls on a taut cable. Two more floors of bare grey concrete frame appear at the top of the tower, each one arriving as a completed slab with props beneath it, and the formwork tables move up with them. Snow gathers grey and tracked at the edges of the site and partly melts. Trucks enter and leave the hoarding as smeared colour trails.

The camera does not move at any point. The framing is identical in the first and last frame. The red brick block with its two chimneys, the leaning cypress tree and the ridge line behind the site stay exactly where they are, at exactly the same size and shape, for the whole shot. The horizon stays at exactly half the frame height. Nothing already built is removed, moved or resized, and no new floor appears without support beneath it. The crane mast never floats, never bends and never changes height.

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

# 5. ⚠️ SIK YAPILAN HATALAR

| Hata | Sonuç | Çözüm |
|---|---|---|
| Bible'ı kısaltmak / atıf vermek | her sahnede farklı bina | birebir kopyala |
| Çapayı farklı kelimeyle yazmak | arka plan kayar | tek cümle, altı kez aynı |
| I2V'de sahneyi yeniden tarif | kadraj kayar, görsel kullanılmaz | yalnız zaman + değişmeyecekler |
| Güneş satırını atlamak | ışık rastgele, saat ölür | dereceyle yaz |
| Bir klipte iki iş adımı | geometri erir | bir klip = bir iş adımı |
| "no logo" tek nesneye bağlı | tabelada/yelekte yazı çıkar | yüzey yüzey say |
| Temiz şantiye | emlak render'ı | SITE TEXTURE bloğu zorunlu |
| Net işçi yüzü | tekinsiz vadi + AI algısı | bulanık çizgi olarak yaz |
| Hızı öznelere tek tek yazmak | gökyüzü hızlanır, yer gerçek zamanda kalır | TIME RATE bloğu — tek cümle, tüm özneler [DERS 15] |
| Kalabalık şantiye | ne kadar çok insan/araç, o kadar çok bozulma | sayıyı AZALT |
| Negatif çekirdeği olduğu gibi taşımak | şehir kuralı dağda yanlış olur | saha kartına karşı oku [DERS 16] |
| Betonu tek renk yazmak | ardışık dökümlerin arasındaki aylar okunmaz | renk sınırını KATLA yaz [A4-a] |
| "Short star trails" | sayısız iz tarifi = boş işaretçi | yay derecesi + pozlama saati [A4-c] |
| Vinç tepe ışığını sürekli yazmak | timelapse yalanlanır | çakan ve bazen karanlık [A4-d] |
