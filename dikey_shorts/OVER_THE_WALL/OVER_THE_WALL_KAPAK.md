# 🖼️ OVER THE WALL — KAPAK KARTI

> ⛔ **KAPAK SIFIRDAN ÜRETİLMEZ.** Usta kareden (G8) türetilir [DERS 30 · MUZIK_VE_KAPAK §2.2].
> Zincirli formatta G8 üretimde İLK üretilen karedir; kapak teslim dosyası ortada yokken hazırdır.
> Aşağıdaki prompt G8 promptunun birebir kopyasıdır; tek ek, başlık bandını boş bırakan satırdır.
> Kapak filmin negatif çekirdeğinin HER maddesini taşır [P1-i]: afiş estetiği, ekstra gök, ekstra
> kontrast serbest değildir.

---

## 0. İKİ İŞ, TEK GÖRÜNTÜ

```
① IZGARA KAPAĞI   kanal ızgarası · "izlemeye devam et" kartı
② KAPAK KARTI     teslim dosyasının SON 5,0 saniyesi (64,0–69,0) · SAHNE DEĞİL [DERS 4]
KAYNAK KARE       G8 (usta kare) — yedek: ffmpeg -ss 62.5 -i teslim.mp4 -frames:v 1 g8_kaynak.jpg
                  ⭐ kaynak kare TESLİM dosyasından alınırsa kırpma sonrası kare kullanılır [KURGU §7]
HAREKET           yok — kart 5 saniye boyunca hareketsiz
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G8 + başlık bandı satırı)

```text
Photorealistic documentary construction photograph — master cover frame, derived from G8. Vertical time-lapse of a concrete gravity dam rising in a narrow mountain gorge, seen from downstream; a construction-progress photograph from a fixed 24 mm site camera, hard daylight, film grain.
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge on the east canyon wall, lens 15.0 metres above the gorge floor, 120 metres from the downstream face of the dam axis, bearing 350 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a straight concrete gravity dam with a stepped downstream face whose crest meets the road bench cut into the east canyon wall. AT THIS STAGE: the dam is complete and overflowing. The stepped concrete wall spans the gorge, its crest meets the road bench on the east wall at the same height, and the two raised shoulders at the ends of the crest stand dry; between them a smooth sheet of water pours over the rounded lip of the wide middle section and breaks into a full cascade of white water covering the whole stepped face from lip to floor, with a bank of white mist at its foot. The black outlet arch on the west wall is dry. At the bottom of the frame the old three-arch bridge is almost buried in white foam and turbulent water, only its parapet line showing. A white water tanker vehicle and a parked yellow dump truck stand on the road bench beside the east shoulder.

SITE / BACKGROUND: To frame left the west canyon wall rises as bare grey-brown layered rock; at mid-height on it sits the black semicircular mouth of the diversion tunnel outlet, ten metres wide, its arch crown exactly on the horizon line. To frame right the east canyon wall rises as the same rock. Beyond the site the two walls meet the sky in a fixed notched skyline. In the lower middle the old three-arch stone bridge stands on the gorge floor, its parapet level. The horizon sits at exactly half the frame height.

THE TIME MOMENT: The river now comes over the wall — a white cascade fills the stepped face between two dry shoulders, the outlet arch is dry and black, and the old bridge is buried in white water at the bottom of the frame.

COMPOSITION: Vertical 9:16. The horizon runs exactly through the crown of the tunnel outlet arch at half the frame height. The old three-arch bridge spans about 460 pixels of frame width — three sevenths — and keeps that width and position in every frame. The crest runs level at about eighty-two percent of frame height, continuous with the road bench on the right; the white cascade fills the middle of the frame from about eighty-one down to forty-two percent; the drowned bridge sits between roughly thirty-six and forty-two percent. The crown of the structure sits below the top eighth of the frame, the working level above the bottom quarter, and nothing that proves progress falls into the right eighth.

LIGHTING: Sun azimuth 247 degrees, elevation 10 degrees, late afternoon golden light, very long shadows falling to the east-north-east. The sun stays behind the camera for the whole shot; its only sign is the shadows. Late October: clear warm sky with a few cirrus streaks, tawny autumn scrub on both slopes, a dusting of snow on the notched skyline, softer and bluer than the near rock.

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the water, the machines and the trucks all move at the same accelerated speed. Two hours pass across this shot: the canyon wall's shadow edge sweeps across the floor, high cirrus streaks drift slowly across the warm autumn sky, and every moving machine smears into heavy motion blur. Nothing in the frame moves at normal speed.

ACTIVITY: The water pours over the lip and down the stepped face as a continuous cascade and churns white around the drowned bridge; the tanker vehicle crawls along the bench and the parked truck stands still; the dry crest is scored with old ruts and roller tracks under a dust film. Crew register only as faint soft motion streaks beside their machines, never as sharp figures, no readable face anywhere; a parked truck stays sharp.

SITE TEXTURE: The dry shoulders and crest dark cured concrete under a dust film, crossed by old ruts and roller tracks; the wet stepped face dark and glossy with white foam streaks on every step; a bank of white mist at the foot of the wall; turbulent water with foam streaks and floating debris around the bridge; a pale flood line and loose scree along the foot of both walls.

PHYSICS: The finished wall bears on the bedrock as one rigid mass and every lift rests on the lift beneath it; the water sheet rests on the rounded lip and the cascade runs down the steps in continuous contact with the concrete. The old bridge rests on its abutments and piers founded on bedrock, unmoved by the water. The tanker and the truck stand on their tyres on the road bench.

NEGATIVE: Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts; the framing is identical from the first frame to the last. The two canyon walls, the tunnel outlet arch, the old bridge, the road bench and the skyline never change shape, position, size or spacing. The dam is one single rigid concrete wall that only ever gains material — nothing already built is removed, moved, resized or redesigned; no opacity fades, no fading into existence. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface: machinery, truck, licence plate, signage, hoarding, container, helmet, vest included. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades, no transitions. No architectural visualisation look, no CGI aesthetic, no miniature or toy look, no tilt-shift blur. No captions, no watermark. Photorealistic documentary photography, 35mm film grain.
Leave the band between roughly twenty-eight and forty percent of frame height visually simple on the left two thirds of the picture: soft white mist and foam with no strong edge and no bright object, so that a title can be set over it in post-production.
Output: 9:16, 4K, no text, no watermark.
```

⛔ Prompt hâlâ `no text` der. Başlık kadraja MODELE yazdırılmaz — post-prodüksiyonda dizilir.

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon)

```
METİN         OVER THE WALL
DİL           İngilizce · 3 kelime
YÜKSEKLİK     büyük harf yüksekliği ≥ kare yüksekliğinin %8'i (≥154 px) — 120 px'te ~10 px kalır
KONUM         y = 1150–1350 px bandı (üstten) — köpük/sis bölgesi, alt-orta · sol 122 px'e ve
              sağ 242 px'e girmez · dudak ve çağlayan ÖRTÜLMEZ
KONTRAST      ≥ 4,5:1 — köpük beyaz olduğu için metnin arkasına DÜZ KOYU BANT (#101315, kanal
              paleti) konur; gradyan yok
YAZI TİPİ     tek ağırlık, geniş harf aralığı, gölge/kontur/parlama YOK; renk #E8E4DC (beton açık)
ANİMASYON     yok
⚠️ Bant köprüyü kapatır — yalnız KAPAKTA. Filmde köprü görünür kalır; kapağın iki işi silüet +
   başlıktır (MUZIK_VE_KAPAK §2.5), bedel filmin işidir.
```

---

## 🔍 KONTROL VE KANITLAR

- [ ] **FİNAL HİYERARŞİ** kapakta da okunuyor mu: ① çağlayan → ② siyah kemer → ③ (bant altında kalsa da) köprü bandı
- [ ] **120 PX TESTİ** — iki görüntüye birden: `sips -Z 120 kapak.png --out kapak_120.png` ve `sips -Z 120 g0.png --out g0_120.png`
      ⓐ silüet: iki duvar arasında beyaz dikey çağlayan kütlesi, üstte düz kret çizgisi seçiliyor mu?
      ⓑ başlık: "OVER THE WALL" kelime şekilleri ayırt ediliyor mu? Kaybolursa punto büyür ya da
         kelime sayısı düşer — "olsun" denmez
- [ ] **KAPAK KANITI** [DERS 30]: `ffmpeg -ss 62.5 -i teslim.mp4 -frames:v 1 g8_kaynak.jpg` →
      `bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak.png` → çıkış 2 = kapak başka bir dünya → TESLİM YOK
- [ ] **SÜRE / KONUM**: kart teslim dosyasının 64,0–69,0 sn'sinde, hareketsiz
- [ ] **GERÇEKLİK**: kapakta logo, firma, proje adı, gerçek yer iddiası YOK
