# 🖼️ THE CROSSING — KAPAK KARTI PROMPTU

> ⛔ **KAPAK SIFIRDAN ÜRETİLMEZ.** S7 usta karesinden (G8) türetilir [DERS 30].
> Bu prompt, G8 usta kare promptunun birebir aynısıdır, sadece başlık boşluğu için bir ek satır içerir.

---

## 📸 KAPAK GÖRSEL PROMPTU

```text
Photorealistic documentary construction photograph — Master Cover Frame. Vertical time-lapse of a completed cable-stayed bridge on a coastal maritime site.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to the observation platform cliff edge, lens 22.0 metres above sea level, 140 metres from the pylon A face of the site, bearing 045 degrees, tilt -2 degrees, zero roll. The camera never moves.

STRUCTURE: When complete, this structure is a twin H-frame reinforced concrete cable-stayed bridge spanning a 400 m maritime channel with 130 m pylons, 32 stay cables per pylon, and a 600 m deck. AT THIS STAGE: Bridge is 100 percent complete and fully operational; twin 130-metre H-frame pylons stand fully cured in pale grey concrete, 64 white stay cables radiate in crisp geometric symmetry, dark asphalt deck carries painted white lines, and active evening traffic flows beneath illuminated LED lamp posts.

SITE / BACKGROUND: To frame right stands Basalt Headland with vertical dark basalt columns. To frame left stands Lighthouse Ridge with a whitewashed 19th-century lighthouse. Across the background runs the sea horizon at exactly 48 percent frame height.

THE TIME MOMENT: The master completion frame — all temporary construction equipment is cleared, the coastal landscape is fully restored, and the cable-stayed bridge stands fully illuminated against the twilight sky.

COMPOSITION: Vertical 9:16. The horizon sits at exactly 48 percent of frame height. Pylon A crown sits at 82 percent and Pylon B crown sits at 68 percent. The completed bridge deck sits at forty-eight percent of frame height; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: Sun azimuth 280 degrees, elevation 8 degrees, shadows falling to the east-southeast. Sunset twilight dusk light, deep magenta and amber sky, warm bridge pole lights illuminated with long vehicle light streaks.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Two hours pass. Each object retains physically correct relative motion under that shared compression. Moving highway traffic renders as continuous white and red light trails. Nothing in the frame moves at normal speed.

ACTIVITY: Vehicle traffic moves smoothly across the deck as light trails; a coastal ferry crosses the water far below leaving a white wake. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: The twin 130-metre pylons and 600-metre deck stand in static tension equilibrium; all stay cables hold constant load paths. No construction cranes or temporary supports remain.

NEGATIVE: Fixed tripod perspective, absolute zero movement, never pans, tilts, zooms or dollys; distant anchors never change shape, position, size or relative distance. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No architectural visualisation look, no unreal clean CGI render look, no video game graphics, no 3D animation feel. No cuts, no dissolves, no transitions, no morphing, no temporal jitter. No people standing static, no sharp unblurred human faces. No cranes present in frame.

Leave the upper middle third of the frame visually simple and low-contrast so that a title can be set over it: no structural detail, no strong edge and no bright object between roughly forty and seventy percent of frame height on the left two thirds of the picture.
Output: 9:16, 4K, no text, no watermark.
```

---

## 🔤 BAŞLIK DİZGİSİ (Post-Prodüksiyon)

> ⛔ **Başlık modele yazdırılmaz.** Üretilen temiz G8 kapak görselinin üzerine dizilir.

```text
METİN         THE CROSSING
DİL           İngilizce
YÜKSEKLİK     Büyük harf yüksekliği ≥ kare yüksekliğinin %8'i (≥154 px)
KONUM         y = 500-1400 px bandı · sağ 242 px'e girmez · sol 122 px'e girmez
KONTRAST      En az 4,5:1 (gerekiyorsa düz koyu renk bant konur, gradyan değil)
YAZI TİPİ     Tek ağırlık, geniş harf aralığı, gölge/kontur/parlama YOK
ANİMASYON     YOK
```

## 🔍 KONTROL VE KANITLAR

- [ ] **120 PX TESTİ:** Kapak dosyası `sips -Z 120 <dosya>` ile küçültüldüğünde dikey siluet + "THE CROSSING" kelime şekilleri okunabiliyor mu?
- [ ] **KAPAK KANITI:** Teslim dosyasından (G8 kaynak) `bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak.png` koşulduğunda aynı yer/bina olduğu doğrulanıyor mu (çıkış 2 olmamalı)?
- [ ] **SÜRE:** Kapak kartı teslim dosyasının son 5 saniyesine (60.0 - 65.0 sn) eklendi mi?
