# 🖼️ THE LONG DAY — KAPAK

> Kapak iki iş yapar (`MUZIK_VE_KAPAK §2.1`): kanal ızgarasındaki kapak VE
> teslim dosyasının SON 5 saniyesindeki kapak kartı. İkisi AYNI görüntüdür.
> **Film adı kapağın üstündedir** — ama modele yazdırılmaz, post-prodüksiyonda
> dizilir [`MUZIK_VE_KAPAK §2.4`]. Bu belge üç şeyi tek yerde tutar:
> **kaynak kare · görsel prompt (metinsiz) · başlığın dizilişi (sayıyla).**
>
> Plan §11 punto/konum/renk için BURAYA işaret eder; sayılar iki yerde durmaz.

---

## 0. KÜNYE

```
FİLM        THE LONG DAY — Uzun Gün
ÖLÇÜ        1080 × 1920 px · 9:16 · PNG (ızgara) + aynı kare 5,0 sn kart olarak
BAŞLIK      THE LONG DAY   ← kapakta OKUNUR hâlde, iki satır: THE LONG / DAY
KAYNAK      S9 · 0:54,0 — ilk güneş ışığının iletişim direğinin tepesine
            düştüğü kare: zemin hâlâ gecede (dünya ışığı), direk tepeleri ve
            panel kenarları güneşte, gökyüzü siyah, yıldızlar hâlâ görünür.
            ⛔ Kapak SIFIRDAN üretilmez. Onaylı S9 klibinden ya da onaylı S9
               usta karesinden türer; başka bir üs çıkar [DERS 4].
PALET       başlık #E8E4DC (beton açık) · kanal paleti, KANAL_KIMLIGI §5.1
            ⛔ amber (#F2A03D) kapakta KULLANILMAZ: karede tek vurgu zaten var
               (lumbozun sıcak ışığı). İkinci vurgu, vurgu olmaktan çıkar.
```

---

## 1. KAYNAK KAREYİ AL

Birincil yol — S9 klibi onaylıysa klibin içinden:

```
ffmpeg -ss 54.0 -i teslim.mp4 -frames:v 1 -update 1 kapak_kaynak.png
```

Yedek yol — S9 klibi tutmadıysa, §2'deki görsel prompt kapak için üretilir.
Bu prompt S9 usta karesinin promptudur; tek farkı sondaki "başlık bandını
boş bırak" cümlesidir. Gece karesidir: zemin dünya ışığında, lumboz yanık.

---

## 2. GÖRSEL PROMPT — metinsiz (İngilizce · modele yapıştırılır)

⛔ Prompt "no text" der ve öyle kalır. Başlık §3'te dizilir.

```
Photorealistic documentary construction photograph — Scene 9 of 10. Vertical time-lapse of a surface base being built on a lunar mare plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — a fixed tripod bolted to a low rock outcrop, lens 3.0 metres above the plain, 40 metres from the south end of the habitat berm, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: One crewed surface base on a lunar mare plain at 20 degrees north. Two identical pressurised habitat modules, each a horizontal white cylinder 12.0 metres long and 4.4 metres in diameter on six jack legs 0.8 metres high, lie parallel and end-on to the camera, 12.0 metres apart centre to centre, the second 8.0 metres further back and 10.0 metres further right, joined by one tunnel 6.0 metres long and 2.0 metres in diameter. Each module is buried under a regolith berm 2.5 metres thick, 17.0 by 9.4 metres at its base, with a flat crest 6.9 metres above the plain; only each south end-cap stays exposed inside a wall of stacked regolith bags 5.0 metres high, and the near end-cap carries one round airlock hatch 1.2 metres across with one round porthole 0.6 metres across above it. Right of the berms stand two power masts 18.0 metres tall, 14 metres apart, each topped by one flat sun-following solar array 6.0 by 3.0 metres. Left of the berms stands one lattice communications mast 22.0 metres tall with one dish 2.4 metres across. One compacted regolith road 4.0 metres wide runs from the lower left corner to the airlock hatch. AT THIS STAGE: the base is complete and occupied: both modules fully buried under berms with crests 6.9 metres above the plain, the tunnel mound between them; the near porthole glows warm; one white floodlight at the top of the communications mast throws a hard pool on the road and the airlock, where one pressurised rover stands parked with its docking collar against the hatch; the dish is latched pointing down; no crawler, no stockpile and no bag stacks remain; the lander is dust-grey to its top.

SITE / BACKGROUND: A flat grey lunar mare plain under a pure black sky. Behind the base, 1.9 kilometres away, a crater rim 400 metres high crosses the whole frame as one continuous ridge line with exactly one deep V-shaped notch left of centre and exactly one rounded summit right of centre. On frame left, at the same distance as the base, lies one house-sized grey boulder 6.0 metres tall and 9.0 metres across, half sunk into the regolith, too large to move. On frame right, in the foreground 18 metres from the camera, lies one small fresh crater 14 metres across with a raised rim of bright ejecta; behind it at the right edge of the frame stands the descent stage of the first cargo lander, an octagonal body 5.2 metres tall on four splayed legs 8.0 metres across, which stays where it landed. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The plain between the lander and the boulder is one tangle of wheel tracks, the very first pair from the ramp foot still there under all the others; the lander is dust-grey to its top.

COMPOSITION: Vertical 9:16. Plain foot at about forty-five percent of frame height, crater rim at about sixty-four percent, communications mast top at about eighty-two percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Lunar night, nineteen lunar days after landing. Sun azimuth 85 degrees, elevation 6 degrees below the horizon behind the camera; no sunlight in the frame. Earthshine from the upper left behind the camera lights the plain dim blue-grey with faint soft shadows to the right; black sky, sharp point stars above the ridge, no Earth.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: Nothing moves. Any suited figure appears only as soft motion streaks, no readable face; vehicles render as smeared trails.

SITE TEXTURE: A dense tangle of wheel tracks and bootprints over the whole plain, the road smooth and darker, the bag walls dust-grey.

PHYSICS: Both modules stand on their legs under berms; the pressurised rover stands on its wheels against the hatch; the dish and floodlight are fixed to the mast.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. In every frame the horizon, the crater rim ridge, the boulder, the fresh crater and the first lander never change shape, position, size or spacing. The base only ever gains material — nothing already built is removed, moved, resized or redesigned; every number written above holds. No readable text, letters, digits, numbers or symbols anywhere — not on the safety signage, the machinery, the containers, the vests and helmets, the flatbed crawler truck, the scaffolding, the formwork, the lander or the module facade; nothing has been branded, labelled, numbered or annotated by anyone: no agency logos, no flags. No atmosphere: no blue sky, no haze, no clouds, no dust hanging in the air, no wind, no lens flare; the sky is pure black; in this night frame it holds sharp point stars and no Earth. No melting or warping geometry, no floating module, no module without support beneath it, no machine hovering above the ground; everything obeys gravity. No cuts, no dissolves, no fades, no transitions, no angle change, no captions, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction film look, no tilt-shift blur. This is a working construction site: tracks, cables, bags and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
Leave the black sky above the crater rim visually simple so that a title can be set over it: no structural detail, no strong edge and no bright object between roughly sixty-five and eighty-seven percent of frame height on the left two thirds of the picture, apart from the thin shaft and top of the communications mast at the far left.
Output: 9:16, 4K, no text, no watermark.
```

---

## 3. BAŞLIĞIN DİZİLİŞİ — sayıyla

Kare düzeni (plan §3 · kare yüksekliği yüzdesi ALTTAN, piksel ÜSTTEN):

```
y (üstten px)   ne var
   0 –  254     ⛔ üst arayüz (sekmeler · profil) — hiçbir şey konmaz
 254 –  687     ⭐ SİYAH GÖKYÜZÜ — krater sırtının üstü · başlık BURAYA
                   (sırt %64,2 → 1920 × (1 − 0,642) = 687 px)
 687 – 1056     sırt · direk tepeleri · tümsek taçları · kaya tepesi
1056 – 1436     ova · yol · hava kilidi · rover
1436 – 1920     ⛔ alt arayüz — görünmez

x (soldan px)   ne var
   0 –  122     ⛔ sol arayüz
 122 –  190     iletişim direği şaftı (x ≈ %14 = 151 px) — başlık bunun SAĞINDA
 200 –  838     ⭐ BAŞLIK ALANI (638 px geniş)
 838 – 1080     ⛔ sağ arayüz (beğen · paylaş · yorum)
```

### Ölçüler

```
METİN          THE LONG          (1. satır)
               DAY               (2. satır)
BÜYÜK HARF     154 px yüksek     = kare yüksekliğinin %8,0 [MUZIK_VE_KAPAK §2.3]
                                  ⛔ altına inilmez: 120 px'te ~10 px kalır,
                                     okunma eşiği budur.
PUNTO          ~220 px            (çoğu yazı tipinde büyük harf ≈ 0,70 × punto;
                                   §4'teki ölçümle DOĞRULANIR, varsayılmaz)
SATIR ARASI    30 px              satır 1 tabanı → satır 2 tepesi
YAZI TİPİ      tek ağırlık · DAR/CONDENSED kalın sans · gölge YOK · kontur YOK
               · parlama YOK. Öneri: Barlow Condensed Bold ya da Oswald Bold.
               Neden dar: 154 px büyük harfle "THE LONG" normal genişlikte
               ~1000 px tutar ve 638 px'lik alana sığmaz. Dar kesimde ~600 px.
HARF ARALIĞI   +2 % (dar kesimde "geniş aralık" kuralı ölçülü uygulanır;
               daha fazlası satırı taşırır)
HİZA           SOLA · x = 200 px
KONUM          satır 1 tepesi  y = 330 px
               satır 2 tepesi  y = 330 + 154 + 30 = 514 px
               satır 2 tabanı  y = 668 px   ← sırtın (687) üstünde kalır ✅
RENK           #E8E4DC · opaklık %100
ARKA BANT      YOK. Zemin siyah gökyüzüdür; kontrast ≥ 4,5:1 zaten sağlanır.
               Gradyan konmaz [MUZIK_VE_KAPAK §2.3].
ANİMASYON      YOK. Kart 5,0 sn hareketsiz.
```

### Dizme komutu

Yazı tipi yolu makineye göre değişir; büyük harf yüksekliği §4'te ölçülür ve
`fontsize` ona göre düzeltilir.

```
FONT=/Library/Fonts/BarlowCondensed-Bold.ttf   # kendi yolunu yaz

ffmpeg -i kapak_kaynak.png -vf "\
drawtext=fontfile=$FONT:text='THE LONG':fontcolor=0xE8E4DC:fontsize=220:x=200:y=330,\
drawtext=fontfile=$FONT:text='DAY':fontcolor=0xE8E4DC:fontsize=220:x=200:y=514" \
-frames:v 1 -update 1 kapak.png
```

Kapak KARTI (teslimin son 5 saniyesi) aynı PNG'den:

```
ffmpeg -loop 1 -i kapak.png -t 5.0 -r 30 -pix_fmt yuv420p -vf scale=1080:1920 kapak_karti.mp4
```

---

## 4. TESTLER — makineyle, gözle değil

```
① BÜYÜK HARF YÜKSEKLİĞİ ≥ 154 px
   Yalnız "THE LONG" satırını siyah zemine dizip dikey sınırlarını ölç:
     ffmpeg -f lavfi -i color=black:s=1080x1920 -vf "drawtext=fontfile=$FONT:\
       text='THE LONG':fontcolor=white:fontsize=220:x=200:y=330" -frames:v 1 -update 1 olcum.png
     magick olcum.png -trim -format "%h px büyük harf\n" info:
   Çıkan sayı 154'ün altındaysa fontsize büyütülür, konum yeniden hesaplanır
   (satır 2 tepesi = 330 + harf + 30). Satır 2 tabanı 687'yi GEÇEMEZ; geçerse
   yazı tipi daha dar bir kesime değişir, harf küçültülmez.

② SATIR GENİŞLİĞİ ≤ 638 px
     magick olcum.png -trim -format "%w px genişlik\n" info:
   638'i geçiyorsa harf aralığı sıfırlanır; hâlâ geçiyorsa daha dar kesim.

③ 120 PX POSTA PULU TESTİ — İKİ görüntüye [MUZIK_VE_KAPAK §2.5]
     sips -Z 120 kapak.png    --out kapak_120.png
     sips -Z 120 s0_kare0.png --out s0_120.png
   ⓐ SİLUET  siyah gökyüzüne karşı iki düz tepe + üç dikey direk + solda
             kaya kütlesi + sağda iniş aracı hâlâ ayırt ediliyor mu?
   ⓑ BAŞLIK  "THE LONG / DAY" kelime ŞEKLİ olarak hâlâ okunuyor mu?
   ⛔ ⓐ kayboluyorsa kapak yeniden ÇERÇEVELENMEZ, S9 YENİDEN ÜRETİLİR.
   ⛔ ⓑ kayboluyorsa punto büyütülür; asla "ızgarada büyük görünür" denmez.

④ GÜVENLİ ALAN
   Başlığın hiçbir pikseli y < 254, y > 1436, x < 122, x > 838 bandına girmez.
   Yukarıdaki sayılarla: y 330–668 · x 200–~800 ✅ (② ölçümüyle doğrulanır).

⑤ METİN YALNIZ BAŞLIK
   Kaynak karede modelin yazdığı hiçbir harf/rakam/logo yok (negatif çekirdek).
   Varsa kare ATILIR; başlığın altına gizlenmez.
```

---

## 5. SPOILER BÜTÇESİ — kapak ne verir, ne vermez

```
VERİR    bitmiş üssün silueti (iki tepe · üç direk) + başlık + gece/şafak ışığı
VERMEZ   sürecin nasıl geçtiğini · yığını · silindirin gömülüşünü · ilk izi
TEK CÜMLE TESTİ: başlık + kapak + ilk 2 sn + açıklama yan yana → bir yabancı
"silindiri toprağa gömüyorlar" diyemez. ✅ (kapakta silindir görünmez, tepe görünür)
```
