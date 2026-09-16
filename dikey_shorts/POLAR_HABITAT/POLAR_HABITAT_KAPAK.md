# 🖼️ POLAR HABITAT — KAPAK

> Kapak iki iş yapar (`MUZIK_VE_KAPAK §2.1`): kanal ızgarasındaki kapak VE teslim dosyasının SON 5 saniyesindeki kapak kartı. İkisi AYNI görüntüdür.
> **Film adı kapağın üstündedir** — ama modele yazdırılmaz, post-prodüksiyonda dizilir (`MUZIK_VE_KAPAK §2.4`). Bu belge üç şeyi tek yerde tutar:
> **kaynak kare · görsel prompt (metinsiz) · başlığın dizilişi (sayıyla).**

---

## 0. KÜNYE

```
FİLM        POLAR HABITAT — Kutup Yaşam Alanı
ÖLÇÜ        1080 × 1920 px · 9:16 · PNG (ızgara) + aynı kare 5,0 sn kart olarak
BAŞLIK      THE POLAR DOME   ← tek/iki satır: THE POLAR / DOME
KAYNAK      ⭐ G6 USTA KARESİ — tamamlanmış habitat, iç sıcak turuncu ışıklar ve 18m kule cyan parıltısı aktif.
            Teslimde karşılığı 0:47,6 (S5'in son karesi); kapak kartı 48,0–53,0 arasında bu karenin üstünde durur.
PALET       başlık #FFFFFF (Stark White) · alt başlık #F2A03D (Amber Glow)
SAFE AREA   y=450 - y=1200 arası merkezlenmiştir. Güvenli alan zarfı korunmuştur.
```

---

## 1. KAYNAK KAREYİ AL

Birincil yol — **onaylı G6 usta karesi** (üretimde İLK üretilen görsel):

```bash
cp g6_usta.png kapak_kaynak.png
```

Yedek yol — S5 klibi yeniden üretildiyse, klibin SON karesi alınır:

```bash
ffmpeg -y -sseof -0.04 -i s5.mp4 -frames:v 1 -update 1 kapak_kaynak.png
```

⛔ **KAPAK KANITI koşulmadan teslim yok** [DERS 30]:

```bash
bash araclar/zincir_kontrol.sh g6_usta.png kapak.png
```

---

## 2. GÖRSEL PROMPT — metinsiz (İngilizce · modele yapıştırılır)

```
Scene 6 of 6.
STRUCTURE: When finished this will be a modular polar survival habitat dome. AT THIS STAGE: The habitat construction is 100 percent complete. The structure consists of a 24-metre diameter hexagonal geothermal foundation ring embedded into permafrost, supported by 6 anchored corner pylons. Rising from the ring is a 12-column heavy steel lattice dome exoskeleton reaching a 14-metre apex height. The shell is fully enclosed with double-layer composite thermal insulation panels in matte stark-white and hazard-amber trim. A dual pressurized cylindrical airlock module projects 4 metres from the southern corner with active warm amber interior lighting visible through heavy portholes. Piercing the apex of the dome is a central 18-metre vertical geothermal energy spire with four radiating thermal-exchange fins, emitting a steady cyan operational energy glow. Surrounding the windward northern side is a 3.5-metre high stepped ice-block breakwater wall set 6 metres from the outer perimeter.

SITE / BACKGROUND: Frozen polar glacial plateau with crystalline ice crust and dark permafrost patches. In the background, a massive jagged blue-ice ridgeline silhouette stretches horizontally across the upper framing between bearing 320 degrees and 040 degrees, keeping exactly the same profile and height in every frame. Thin atmospheric polar haze over the distant horizons.

Camera: fixed ground station mounted on heavy tripod, 6.5 metres above ground, 28.0 metres from near foundation edge, 40.0 metres from central structure axis, bearing 145 degrees SE, tilt 12 degrees down, roll 0 degrees.

LIGHTING: Late afternoon crisp polar sunlight from azimuth 210 degrees, elevation 22 degrees. Casting long cool-blue shadows across the white ice crust toward the northeast. High contrast scene, deep cobalt-blue sky with faint polar cirrus haze. Warm internal habitat glow contrasting with cold exterior ambient light.

TIME RATE: Two hours pass. Cloud movement, shadow progression, and drifted snow particles are all time-lapsed at the same rate.

ACTIVITY: The construction site is clean and complete. A heavy robotic crawler rig and a secondary utility rover rest at the perimeter edge, having withdrawn outside the ring. The crawler boom carries a visible load on its parked sling. The crane arm always carries a visible load on its sling. A gentle steam plume rises from the geothermal spire vent. Fine snow dust drifts softly across track ruts. No workers are present.

NEGATIVE: No changes to background mountain silhouette. The camera position never pans, tilts, zooms or alters focal length. Background ridgeline elements never change shape, position, size or distance. No readable text, letters, digits or brand logos on any surface, including rover, lander, module, habitat, panel, mast, antenna, airlock, spool, container, helmet, crane, scaffolding, facade, or vest. No architectural visualisation look, no CGI renders, no oversaturated cartoonish style. No cuts, no dissolves, no camera transitions within the scene. Every machine is a sealed robotic unit with no cab, no window, no seat and no handrail.

SITE TEXTURE: Rough wind-scoured ice crust, dark exposed permafrost gravel, smooth snow drifts around the ice wall base, clean frozen ground without construction clutter.
```

---

## 3. BAŞLIĞIN DİZİLİŞİ VE TİPOGRAFİ

```
ANA BAŞLIK:     "THE POLAR DOME"
FONT:           Inter / Roboto / Outfit Bold (Stark White #FFFFFF)
PUNTO:          60 px · Drop shadow: rgba(0,0,0,0.8), offset (0, 4px), blur 12px
KONUM:          y = 520 px (Merkezlenmiş)

ALT BAŞLIK:     "EXTREME PLANETARY TIMELAPSE"
FONT:           Inter / Roboto Medium (Amber Glow #F2A03D)
PUNTO:          28 px · Letter spacing: 2px
KONUM:          y = 600 px (Merkezlenmiş)
```

---

## 4. 120 PX MOBİL GÖRÜNÜRLÜK TESTİ

```bash
sips -Z 120 kapak.png --out kapak_120.png
```

*Test Kriteri:* 120px mobil önizlemede "THE POLAR DOME" başlığı okunabiliyorsa ve 18m enerji kulesinin cyan parıltısı belirginse kapak görseli onaylanır.
