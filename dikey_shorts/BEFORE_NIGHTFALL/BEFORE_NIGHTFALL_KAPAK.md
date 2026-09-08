# 🖼️ BEFORE NIGHTFALL — KAPAK

> Kapak iki iş yapar (`MUZIK_VE_KAPAK §2.1`): kanal ızgarasındaki kapak VE
> teslim dosyasının SON 5 saniyesindeki kapak kartı. İkisi AYNI görüntüdür.
> **Film adı kapağın üstündedir** — ama modele yazdırılmaz, post-prodüksiyonda
> dizilir [`MUZIK_VE_KAPAK §2.4`]. Bu belge üç şeyi tek yerde tutar:
> **kaynak kare · görsel prompt (metinsiz) · başlığın dizilişi (sayıyla).**
>
> Plan §7 punto/konum/renk için BURAYA işaret eder; sayı iki yerde durmaz.
>
> ⚠️ **BU FİLMDE KAPAĞIN KAYNAĞI TESLİM DOSYASI DEĞİLDİR.** Ters üretimde
> G6 usta karesi EN ÖNCE üretilir (plan §2); kapak ondan türer ve teslim
> dosyası daha ortada yokken hazırdır. Teslimden kare almak yalnız YEDEK yoldur.

---

## 0. KÜNYE

```
FİLM        BEFORE NIGHTFALL — Gece Çökmeden
ÖLÇÜ        1080 × 1920 px · 9:16 · PNG (ızgara) + aynı kare 5,0 sn kart olarak
BAŞLIK      BEFORE NIGHTFALL   ← iki satır: BEFORE / NIGHTFALL
KAYNAK      ⭐ G6 USTA KARESİ — istasyon tamam, gölgeler kuzeydoğuya 2,25 m,
            duvar dört kurs kapalı, direk beş bölüm, solda iniş aracının üç
            bacağı ve boş halka çerçevesi. Teslimde karşılığı 0:47,96 (S5'in
            son karesi); kapak kartı 48,0–53,0 arasında bu karenin üstünde durur.
            ⛔ Kapak SIFIRDAN üretilmez. Üretilirse kart, filmin bitirdiği
               istasyondan başka bir istasyon gösterir [DERS 4 · DERS 30].
PALET       başlık #E8E4DC (beton açık) · kanal paleti, KANAL_KIMLIGI §5.1
            ⛔ amber (#F2A03D) kapakta KULLANILMAZ: bu karede zaten tek parlak
               şey var (halkanın yayı). İkinci vurgu, vurgu olmaktan çıkar.
ARKA BANT   ⛔ YOK. Zemin siyah gökyüzüdür; kontrast zaten ≥ 4,5:1. Bant
            koymak halkanın yayını kapatır ve kart filmden BAŞKA bir dünya
            gösterir — beş mercekte END CARD: DIFFERENT bu şekilde geldi
            [DERS 30 · P1-i].
```

---

## 1. KAYNAK KAREYİ AL

Birincil yol — **onaylı G6 usta karesi** (üretimde İLK üretilen görsel):

```
cp g6_usta.png kapak_kaynak.png
```

Yedek yol — S5 klibi yeniden üretildiyse, klibin SON karesi alınır:

```
ffmpeg -y -sseof -0.04 -i s5.mp4 -frames:v 1 -update 1 kapak_kaynak.png
```

⛔ **KAPAK KANITI koşulmadan teslim yok** [DERS 30]:

```
bash araclar/zincir_kontrol.sh g6_usta.png kapak.png
```

Çıkış 2 = kapak G6'dan türememiş → TESLİM YOK. Başlık bandı SSIM'i düşürür;
kenar şeritleri (eğik taş · fay sarpı · halkanın yayı) tutmalıdır.

---

## 2. GÖRSEL PROMPT — metinsiz (İngilizce · modele yapıştırılır)

⛔ Prompt "no text" der ve öyle kalır. Başlık §3'te dizilir.
⛔ **Bu blok planın §6 G6 promptunun BİREBİR kopyasıdır.** Tek fark, sondan
bir önceki satırdır (başlık bandı). Plan §6 değişirse burası da değişir —
iki yerde duran metin, birinde eskiyen metindir.

```
Photorealistic documentary construction photograph — Scene 5 of 6. Vertical time-lapse of a small robotic relay station on an airless grey rock plain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted into a rock outcrop south of the site, lens 6.0 metres above the plain, 40.0 metres from the axis of the site and 27.0 metres from its near edge, bearing 000 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be one small pressurised relay station on this plain. AT THIS STAGE: the station is finished. The wall stands closed at four dry-stacked courses, 3.2 metres high and 18.0 metres long, each course stepped back 0.30 metres and capped level. Behind it the steel cylinder lies buried under panels and swept grit with only its raised hatch box and one flat end cap showing. East of the trench a bolted three-leg tower stands 15.0 metres high in five sections, carrying a 2.4 metre parabolic reflector on its fourth section and held by three straight tensioned wires anchored 9.0 metres out; the cradle that raised it lies unbolted and stacked flat against the wall. To the west eight flat panels stand in a single row on the lander's stripped deck, all of them turned to face the low star. Eighteen metres to the left the lander's three bare legs and its empty ring frame still stand where they landed, stripped down to bare metal. The row of cut slabs along the north rim is empty and the old fissure runs 0.52 metres wide past the leaning slab and on under the eastern anchor block. Every shadow runs long to the north-east.

SITE / BACKGROUND: The site sits on a level grey rock plain that runs unbroken to the horizon. Due north, its centre exactly on the horizon line, stands a black circle so wide that it runs off both side edges of the frame, rising to four fifths of the frame height, drawn by one razor-thin bright ring; the inside of the circle is flat, even black and its edge is perfectly sharp. To frame right, nearer than the site, one pale rock slab 3.0 metres tall and 0.8 metres thick stands upright, leaning twelve degrees to the north. Behind the site a straight scarp crosses the whole horizon, its top edge 4.0 metres above the plain, stepping down once near the left edge of the frame. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The tower head stands nearly five times the height of the leaning slab, the crown of the wall is level with the slab's top, and every shadow is more than twice the height of what casts it.

COMPOSITION: Vertical 9:16. The swept floor sits at thirty-nine percent of frame height, the crown of the wall at forty-five percent and the tower head at sixty-four percent. The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: star azimuth 247 degrees, elevation 24 degrees, shadows falling to the north-east, a 1 metre rod casting a 2.25 metre shadow. Every shadow edge is razor sharp and its inside is solid black. The sky is black and empty from horizon to zenith, exposed for the sunlit rock. It looks like a 1970s Apollo surface photograph taken on a chest-mounted 70mm film camera: flat grey rock, blown highlights, fine even grain, no haze, no depth fog, no rim light.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the shadows, the thrown grit, the robotic units and the marks they leave all move at the same accelerated speed. Nothing in the frame moves at normal speed. Roughly ten minutes pass across this shot: the shadows barely move and only lengthen a little, and the machines run fast but stay recognisable as machines.

ACTIVITY: A tracked rover hauls the last capping slab up onto the fourth course and beds it flat, a manipulator arm swings its head down to rest against the wall, and the panel row turns a few degrees further to hold the falling star; the emptied slab row and the fan of dust at the foot of the wall stay exactly as the day made them. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail. No people are present.

SITE TEXTURE: a fan of fresh dust at the foot of the wall, one toppled slab at the end of the empty row, cleated ruts crossing the swept floor, offcuts and rock dust, and long shadows running across the bare circle.

PHYSICS: The tower carries its weight through a bolted base plate on the bedrock and is held by three straight tensioned wires anchored 9.0 metres out. The stone courses bear on one another and the buried cylinder rests on its chocks. Nothing stands above the ground without support.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same station, same background in every frame: the horizon line, the black circle and its bright ring, the leaning slab and the scarp behind the site never change shape, position, size or spacing. The station only ever gains material — nothing already built is removed, moved, resized or redesigned. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No melting or warping geometry, no swimming texture, no course of stone without support beneath it; everything stays in continuous contact with the rock. No cuts, no dissolves, no fades, no transitions, no jump cuts. No subtitles, no captions, no title card, no watermark. No architectural visualisation look, no CGI aesthetic, no science-fiction concept-art look, no tilt-shift blur. The air is absent: nothing hangs above the ground, no haze, no smoke, no blue sky. This is a working robotic site: loose grit, cleated ruts, cut offcuts, stacked slabs, spoil ridges and untidy clutter are present.
Leave the black sky between roughly sixty-five and eighty-seven percent of frame height clear so that a title can be set over it: no structure, no machine, no bright object and no marking there, apart from the single thin bright arc that crosses it.
Output: 9:16, 4K, no text, no watermark.
```

⭐ Başlık bandı cümlesi `MUZIK_VE_KAPAK §2.4`'ün iskeletinden **bu karenin
geometrisine göre** değiştirildi: iskeletteki "üst orta üçte bir" bandı bu
filmde kara halkanın yayının tam üstüne düşüyor ve yayı YASAKLIYOR. Yay
kilitli bir arka plan çapasıdır; kapakta da durur. Cümle bu yüzden yayı
tek istisna olarak adıyla korur.

---

## 3. BAŞLIĞIN DİZİLİŞİ — sayıyla

Kare düzeni (px ÜSTTEN · yüzde ALTTAN · plan §3'ten):

```
y (üstten px)   ne var
   0 –  254     ⛔ üst arayüz (sekmeler · profil) — hiçbir şey konmaz
 254 –  285     ⛔ Instagram profil ızgarasının 4:5 kırpması burayı kesiyor
                   [CAPRAZ_YAYIN §3.2: ızgarada görünen bant y = 285–1635]
 285 –  409     kara gökyüzü — halkanın yayının ÜSTÜ (yay tepesi y=409,2)
 409 –  672     ⭐ HALKANIN İÇİ — düz siyah · BAŞLIK BURAYA
                   yay bu bandın içinden geçer (aşağıda tam yeri var)
 672            direk tacı (%65,0)   ⚠️ plan %64,0 diyor → y=691; ikisi de
                   yerleşimin altındadır, yerleşim ikisinde de güvenlidir
 787            çanak merkezi (%59,0)
 960            ufuk (%50,0) — halkanın merkezi tam burada
1050 · 1073     duvar tacı (%45,3) · eğik taşın tepesi (%44,1)
1152            süpürülmüş taban (%40,0)
1436 – 1920     ⛔ alt arayüz — görünmez

x (soldan px)   ne var
   0 –  122     ⛔ sol arayüz
 122 –  836     ⭐ BAŞLIK ALANI — NIGHTFALL tam 714 px ile buraya oturur
 838 – 1080     ⛔ sağ arayüz (beğen · paylaş · yorum)
 540            direk ekseni — başlık direğin TACINDAN yukarıda durduğu için
                   şaft, gergi telleri ve çanak başlığın altında kalır ✅
```

### Ölçüler — ⭐ HEPSİ ÖLÇÜLDÜ, HİÇBİRİ VARSAYILMADI

```
METİN          BEFORE            (1. satır)
               NIGHTFALL         (2. satır)
YAZI TİPİ      DIN Condensed Bold  (/System/Library/Fonts/Supplemental/)
               ⭐ Makinede ölçülen EN DAR kesim budur; sığdıran tek kesim de o.
PUNTO          214 px            ⛔ güvenli alana sığan EN BÜYÜK punto
                                 215'te NIGHTFALL 717 px → sağ kenar 839 ⛔
BÜYÜK HARF     153 px (%7,97)    düz tepeli harf (H) mürekkep yüksekliği
               155 px (%8,07)    kelimenin mürekkep kutusu (O ve G taşırır)
                                 ⭐ Deponun ölçüm yordamı kelimeyi TRIM eder
                                   [LONG DAY KAPAK §4] — o yordam 155 px okur
                                   ve MUZIK_VE_KAPAK §2.3'ün 154 px tabanını
                                   GEÇER. Düz tepeli ölçüde 1 px altındadır.
HARF ARALIĞI   0 %               ⚠️ §2.3 "geniş aralık" der; burada 2 px pay
                                 var, aralık açılırsa satır güvenli alanı taşar
SATIR 1        BEFORE     510 px geniş × 155 px  ·  x 122–632 · y 290–445
SATIR 2        NIGHTFALL  714 px geniş × 155 px  ·  x 122–836 · y 508–663
SATIR ARASI    63 px             (1. satırın tabanı 445 → 2. satırın tepesi 508)
HİZA           SOLA · x = 122 (sol güvenli sınır)
RENK           #E8E4DC · opaklık %100
ARKA BANT      ⛔ YOK (§0)
ANİMASYON      YOK. Kart 5,0 sn hareketsiz.
```

### ⚠️ İKİ SAPMA — ikisi de ölçüldü, ikisinin de gerekçesi burada

```
① BÜYÜK HARF TABANI — MUZIK_VE_KAPAK §2.3 ≥154 px (%8) ister
   ÖLÇÜLDÜ: "NIGHTFALL" DOKUZ harftir ve güvenli genişlik 716 px'tir
   (1080 − 122 − 242). Punto 214'te satır 714 px; punto 216 (düz tepeli
   harfin 154 px olduğu punto) 719 px ister ve güvenli alanı 3 px taşar.
   ⇒ İki sert kapıdan biri kırılacaktı. Kırılan, tabanın DÜZ TEPELİ okuması
     oldu: 153 px (%7,97) — %8'in 0,03 puan altı. Deponun kendi ölçüm
     yordamı (kelimeyi trim et) 155 px okur ve tabandan GEÇER.
   ⭐ 120 px posta pulunda karşılığı: 154 px → 9,63 px · 153 px → 9,56 px.
     Tabanın gerekçesi ("120 px'te ~10 px kalmalı") 0,07 px'lik bu farkla
     bozulmaz; bozulan güvenli alan olsaydı ikon bandına yazı girerdi.
   ⛔ BU BİR EMSAL DEĞİLDİR: sebebi başlığın 9 harfli kelimesidir. Yeni
     filmde çözüm puntoyu düşürmek değil, BAŞLIĞI KISALTMAKTIR (§6 ③).

② KONUM BANDI — MUZIK_VE_KAPAK §2.3 başlığı y = 500–1400'e koyar
   1. satır y = 290'da, yani bandın 210 px yukarısında duruyor.
   SEBEP: 500–1400 bandının ALTINDA bu filmde yer yok. y = 500'ün altında
   sırasıyla direk tacı (672), çanak (787), ufuk (960), duvar (1050), eğik
   taş (1073) ve süpürülmüş taban (1152) var. Başlık oraya inerse direğin
   siluetini kapatır — ve 120 px testinin ⓐ maddesi tam onu arar.
   ⭐ BANDIN İKİ GEREKÇESİ DE 290'DA SAĞLANIYOR:
       üst arayüz  ≤ 254  → 290 dışında ✅
       IG 4:5 ızgara kırpması y = 285–1635 [CAPRAZ_YAYIN §3.2] → 290 içinde ✅
     500 sayısı bu iki sınırın ikisinden de muhafazakârdır; kuralın HARFİ
     kırıldı, GEREKÇESİ kırılmadı.
```

### ⭐ HALKANIN YAYI BAŞLIĞIN ARKASINDAN GEÇER — kaçınılmaz, ölçüldü

```
Yay: merkez (540, 960) · r = 551 px · tepe (540, 409). Başlık alanında (x
122–836) yayın y'si 409 (ortada) ile 601 (sol kenarda) arasında dolaşır.
İki satır + 154 px'lik harf, o bandı KESMEDEN yerleştirilemez:
   yayın üstündeki temiz bant   285–409 = 124 px  → tek satır bile sığmaz
   yayın altındaki temiz bant   601–672 =  71 px  → sığmaz
⇒ Karar: yay başlığın ARKASINDAN geçer, üstü ÖRTÜLMEZ, bant konmaz.

NEREDE, TAM OLARAK
   1. satırda  x 344–632 arasında, y 409–445 bandında — F O R E harflerinin
               altından geçer, sonra iki yandan aşağı iner
   satır arası x 225–855 arasında AÇIKTA görünür (yayın tepesi dâhil)
   2. satırda  yalnız x 122–225 — N harfinin ve I'nın başının arkasından
   ⛔ Sağ kolu (x 855) başlık alanının dışındadır, satır 2'ye değmez.
⭐ İki satır arasındaki 63 px'lik boşluk bu yüzden vardır: yayın tepesi
   oradan görünür. Boşluk kapatılırsa çapa kaybolur.
```

### Dizme komutu

⚠️ Bu makinedeki `ffmpeg` **freetype'sız derlenmiş** — `drawtext` filtresi
yok (`ffmpeg -buildconf | grep freetype` boş döner). Başlık bu yüzden
Python/PIL ile dizilir; betik aynı zamanda ÖLÇER ve taşarsa durur.

```python
#!/usr/bin/env python3
# /usr/bin/python3 basli_diz.py kapak_kaynak.png kapak.png
import sys
from PIL import Image, ImageDraw, ImageFont

FONT  = "/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf"
PUNTO = 214                      # buyuk harf 153 px (duz tepeli) / 155 (murekkep)
RENK  = (0xE8, 0xE4, 0xDC)       # #E8E4DC
X, SAG = 122, 838                # sol / sag guvenli sinir
SATIR = (("BEFORE", 290), ("NIGHTFALL", 508))    # metin, murekkep tepesi

kaynak, hedef = sys.argv[1], sys.argv[2]
im = Image.open(kaynak).convert("RGB")
assert im.size == (1080, 1920), f"kare 1080x1920 degil: {im.size}"
d, f = ImageDraw.Draw(im), ImageFont.truetype(FONT, PUNTO)

for metin, y in SATIR:
    x0, y0, x1, y1 = d.textbbox((0, 0), metin, font=f)
    d.text((X - x0, y - y0), metin, font=f, fill=RENK)
    g, h = x1 - x0, y1 - y0
    assert X + g <= SAG, f"{metin} guvenli alani tasiyor: {X+g} > {SAG}"
    print(f"  {metin:10s} {g:4d} x {h:3d} px  ·  x {X}-{X+g}  ·  y {y}-{y+h}")
im.save(hedef)
```

Beklenen çıktı:

```
  BEFORE      510 x 155 px  ·  x 122-632  ·  y 290-445
  NIGHTFALL   714 x 155 px  ·  x 122-836  ·  y 508-663
```

---

## 4. TESTLER — makineyle, gözle değil

```
① ÖLÇÜ TESTİ  §3'teki betik zaten ölçer ve taşarsa assert ile DURUR.
   Yazı tipi değişirse yeniden ölçülür — punto DEĞİL, satır genişliği bağlar.
   ⛔ Başka bir kesim kullanılacaksa önce şu koşulur:

     /usr/bin/python3 - <<'EOF'
     from PIL import Image, ImageDraw, ImageFont
     F = "<yeni yazi tipi>"
     d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
     for p in range(200, 240):
         f = ImageFont.truetype(F, p)
         x0, y0, x1, y1 = d.textbbox((0, 0), "NIGHTFALL", font=f)
         h = d.textbbox((0, 0), "H", font=f)[3]
         if 122 + (x1 - x0) <= 838:
             print(p, x1 - x0, "duz tepeli", h)
     EOF

   En büyük punto seçilir; düz tepeli yükseklik 154'ün altındaysa §3'teki
   sapma ① yeniden yazılır. ⛔ Harf küçültülerek sığdırılmaz — daha dar
   kesim aranır.

② 120 PX POSTA PULU — İKİ görüntüye [MUZIK_VE_KAPAK §2.5]
     sips -Z 120 kapak.png    --out kapak_120.png
     sips -Z 120 s0_kare0.png --out s0_120.png
   ⓐ SİLUET  siyah gökyüzüne karşı halkanın YAYI ile direğin silueti
             BİRBİRİNDEN ayırt ediliyor mu? (ikisi de x≈540'ta buluşur)
             Yanında: solda iniş aracının boş çerçevesi, sağda eğik taş.
   ⓑ BAŞLIK  "BEFORE / NIGHTFALL" kelime ŞEKLİ olarak hâlâ okunuyor mu?
   ⛔ ⓐ kayboluyorsa kapak yeniden ÇERÇEVELENMEZ, G6 YENİDEN ÜRETİLİR.
   ⛔ ⓑ kayboluyorsa punto büyütülemez (§3 ①) — kelime kısaltılır (§6 ③).
   ⭐ ⓑ 08.09.2026 KOŞULDU VE GEÇTİ — düz siyah zemine dizilmiş başlık,
     sips -Z 120 ile 67×120 px'e indirildi: "BEFORE" ve "NIGHTFALL" kelime
     ŞEKLİ olarak ayırt ediliyor (harfler değil, kelimeler). %7,97'lik büyük
     harf tabanı bu ölçüde okunuyor.
     ⛔ ⓐ KOŞULMADI ve koşulamaz: G6 üretilmedi, zeminde henüz siluet yok.

③ GÜVENLİ ALAN
   Başlığın hiçbir pikseli x < 122, x > 838, y < 285, y > 1436 bandına girmez.
   §3'ün sayılarıyla: x 122–836 · y 290–663 ✅
   ⚠️ y < 500 bir SAPMADIR ve gerekçesi §3 ②'de yazılıdır.

④ KAPAK KANITI [DERS 30]
     bash araclar/zincir_kontrol.sh g6_usta.png kapak.png
   Çıkış 2 = kapak G6'dan türememiş → TESLİM YOK.

⑤ METİN YALNIZ BAŞLIK
   Kaynak karede modelin yazdığı hiçbir harf/rakam/logo yok (negatif çekirdek
   "No readable text, letters, digits, numbers or symbols anywhere in the
   frame, on any surface" der). Varsa kare ATILIR; başlığın altına gizlenmez.

⑥ HALKA KİLİDİ [plan §9 ⑥(b)]
   Kapakta halka İNCE ve RENKSİZ mi? Turuncu, kalın ya da girdaplı bir disk
   çıktıysa kare atılır — o, deliğin ADININ korpusudur ve prompt onu
   adlandırmıyor [DERS 42].
```

---

## 5. SPOİLER BÜTÇESİ — kapak ne verir, ne vermez

```
VERİR    kapanmış duvar + dikilmiş direk silueti · halkanın yayı · uzun
         gölgeler (günün bittiği) · solda iniş aracının BOŞ çerçevesi (bedel)
VERMEZ   dairenin süpürülüşünü · çukurun açılışını · tankın inişini · taşın
         kesilişini · fay çatlağının açılışını (0,35 → 0,52 m)
TEK CÜMLE TESTİ: başlık + kapak + ilk 2 sn + açıklama yan yana → bir yabancı
"iniş aracını söküp binaya çeviriyorlar" diyemez. ✅ Kapakta yalnız SONUÇ var:
boş çerçeve orada duruyor ama neyin söküldüğü görünmüyor.
⭐ Kapağın kendi cümlesi: "gece geliyor ve bu bitmiş."
```

---

## 6. ⛔ BU DOSYANIN AÇIKLARI — üretimden önce bilinen

```
① KAYNAK KARE HENÜZ YOK. G6 üretilmedi; §3'ün bütün y sayıları PLANIN
   geometrisinden türedi, üretilmiş bir kareden ölçülmedi. G6 gelince
   ⛔ ilk iş yayın tepesini ve direk tacını KAREDE ölçmektir:
     /usr/bin/python3 -c "from PIL import Image; im=Image.open('g6_usta.png'); \
       print(im.size)"   # 1080x1920 değilse bütün yüzdeler yeniden hesaplanır
   Yay tepesi 409 ± 20 px dışına düşerse satır tepeleri kaydırılır.

② DİREK TACI İKİ SAYI TAŞIYOR. Plan §3 "%64,0" der, planın kendi formülü
   %65,0 verir [plan §9 ⑥(f)]. Yerleşim ikisinde de güvenlidir (672 ve 691'in
   ikisi de 2. satırın tabanının — 663 — altındadır) ama sayı düzeltilene
   kadar bu dosya İKİSİNİ birden yazar. ⛔ Düzelten, ikisini de düzeltir.

③ BAŞLIK BU FORMAT İÇİN UZUN. Ölçüldü: düz tepeli harfin 154 px olduğu
   puntoda (216) "NIGHTFALL" 719 px tutar — harf başına ~80 px. Güvenli
   genişlik 716 px olduğuna göre bu formatta sığan en uzun kelime SEKİZ
   harftir (~640 px). "NIGHTFALL" dokuzdur. Konsept kapısı ③ (KILAVUZ_REHBERI §6) yalnız
   KELİME sayar; harf saymaz ve bu sınır hiçbir kılavuzda yazılı değildir.
   ⇒ Öneri (bu filmin dışında): kapıya "en uzun kelime ≤ 8 harf" satırı.
      Burada uygulanmadı çünkü film adı konsept kapısından geçmiş durumda.

④ YAZI TİPİ MAKİNEYE BAĞLI. DIN Condensed Bold macOS'ta sistem yazı tipidir;
   başka makinede yoksa §4 ①'in taraması koşulur. Daha dar bir kesim
   (Oswald · Barlow Condensed) kurulursa sapma ① tamamen kapanabilir —
   ölçülmedi, çünkü ikisi de bu makinede yüklü değil.

⑤ IG 4:5 IZGARA KIRPMASI HESAPLANDI, ÖLÇÜLMEDİ. y = 285–1635 bandı
   CAPRAZ_YAYIN §3.2'nin hesabıdır ve o dosya "ikincil kaynaklardan kuruldu,
   ölçülmedi" der. Başlığın tepesi 290'da, sınırın 5 px içinde. ⛔ İlk
   yüklemede ızgara görüntüsü ekran görüntüsüyle doğrulanır.
```
