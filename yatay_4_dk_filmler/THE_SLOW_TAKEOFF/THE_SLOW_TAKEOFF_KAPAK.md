# 🖼️ THE_SLOW_TAKEOFF — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30]

## 0. TEK İŞ: KÜÇÜK RESİM (video içi kapak kartı YOK)

```
KAYNAK KARE     G30 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Prompt aşağıda usta kare (G30) promptunun
                kopyası + tek ek satır (başlık bandı). Model başlığı YAZMAZ; tipografi post-prodüksiyon.
KAPAK KARTI     ⛔ YOK — sahip senaryosu 07.10.2026 ("Ayrı beş saniyelik afiş bu revizyona eklenmemiştir"). Teslim
                240,0 sn, son kare G30. Bu dosya yalnız PLATFORM KÜÇÜK RESMİDİR (1280×720).
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 239.5 -i teslim.mp4 -frames:v 1 g30_kaynak.jpg
                bash araclar/zincir_kontrol.sh g30_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
BAŞLIK          "THE SLOW TAKEOFF" (İngilizce · 3 kelime) — YAYIN_PAKETI başlığıyla aynı vaadi söyler: uçak "kalkar"
                ama yalnız altı metre, yavaşça (soru başlıkta, cevap filmde)
ÖLÇÜ            16:9 · küçük resim 1280×720 (kaynak 1920×1080 G30 karesi) · ⛔ öncesi/sonrası bölme YOK (sahip 19.09.2026)
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G30 + başlık bandı satırı)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.
> ⭐ Tercih: önce teslim dosyasının 239,5. saniyesindeki kare kullanılır; yalnız o kare bant için uygun değilse
> aşağıdaki prompt G30'dan image-to-image koşulur (G30 referans, değişen tek şey bandın sadeliği).

```
Photorealistic documentary site photograph — cover frame made from master frame G30. Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow made into a lake house; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 400.
Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, 33 metres long, with a timber terrace round its near wing. AT THIS STAGE: everything is finished. The retired airliner stands fixed at its final height, its belly six metres above the ground, on two curved steel saddle beams pinned to two red steel frames; a pale timber terrace with slim steel railings, two benches and four planters surrounds the near wing root; a grey steel stair with timber steps runs from the dry rise under the oak to the forward cabin door; all its windows are clear dark glass. All its lights are on — warm light in the cockpit and along the whole row of cabin windows, small warm lamps along the terrace railings and down the stair — and they are doubled in the calm pond that fills the low ground beneath and in front of the house. A line of flat stepping stones leads from the stair foot to the short timber walkway with pale decking, reeds and low shrubs line the pond banks, and a narrow channel leaves the right end of the pond and curves back to the lake shore beside the boathouse. In the mouth of the channel, just past the tail, the dark green canoe rests on the calm water, its bow towards the open lake, with one person in it, seen small from the side, no readable face. Below the house, where the airliner once lay in its muddy bed, there is only water and reflected light.

SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in view, and the shore and the hills carry only grass, reeds and trees.

THE TIME MOMENT: Twenty past seven, deep blue hour, early summer: the house is lived in.

COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of frame width, from a little over a quarter to a little under three quarters of the frame width, its belly at about fifty-seven percent of frame height, above the far shoreline, the top of its fuselage at about sixty-six percent and the top of its tail fin at about eighty-two percent, below the top eighth of the frame. The canoe spans about 130 pixels of frame width at about two thirds of the frame width. The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth or the top-right corner of the frame. Leave a horizontal band between roughly 83 and 93 percent of frame height, across the middle of the frame above the tail fin and right of the oak crown, visually simple and low-contrast so that a title can be set over it: no structural detail, no strong edge and no bright object inside that band — open evening sky only.

LIGHTING: Sun azimuth 293 degrees, elevation 4 degrees below the horizon, on the left outside the frame, so there is no direct sun: deep blue hour, the sky deep clear blue with a last pale band low on the left and a few high thin clouds. Early summer. The sun stays outside the frame.

TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the water ripples, the reflections tremble and the canoe glides at its real pace; nothing is accelerated.

ACTIVITY: The canoe rests at the mouth of the channel, its last ripples spreading and fading; the reflections of the lit windows tremble in the pond and settle. The person in the canoe stays a small dark silhouette, no readable face.

SITE TEXTURE: Calm dark water with trembling reflections, dew on the new grass, damp dark timber on the walkway, a thin haze and a film of mist low over the lake, faint tyre tracks on the gravel track, faint silt stains on the lower columns, a band of young reeds round the pond. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The airliner rests on its saddle beams, which rest on the brackets of the red frame columns standing in the pond on their footings. The stair stands on its footing on the dry rise, and the terrace bears on its four slim posts. The canoe sits on the channel, pressed into the water by the weight of one person.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Yatayda yapı ORTADA (x 537–1383), sol kenarda meşe, sağda kayıkhane: boş kalan yer üst ortadaki akşam göğüdür —
bant oraya konur (üst 60 px oynatıcı bandının altında, kuyruk tepesinin, üstten 194, üstünde). Sağ üst 300×100 px'e
girmez · süre damgası sağ alttadır, kano (x ≈1293 · üstten 624) ona düşmez [A15-c].

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        THE SLOW TAKEOFF (büyük harf · tek satır · 3 kelime)
YÜKSEKLİK    büyük harf ≥ %8 kare boyu = ≥ 86 px @1080 (1280×720'de ≥ 58 px; 120 px'e küçülünce ≈ 10 px — okunma eşiği)
KONUM        x ≈ 430–1490 px (meşe tacının sağı, kuyruk bölgesinin solu dahil orta bant) · y ≈ 75–180 px (1080 ölçeğinde) ·
             sağ üst 300×100 px'e ve alt 100 px'e girmez
RENK         sıcak amber #F2A03D (kanal vurgusu — KANAL_KIMLIGI) · mavi saat göğüne karşı kontrast ≥ 4,5:1
             (yetmezse bandın arkasına %35 opaklıkta düz koyu lacivert şerit — gradyan değil)
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ silüet (yüksekteki uçak + çerçeveler + yansıma) okunuyor mu ·
                 ⓑ KELİME şekli ayırt ediliyor mu · ⓒ sağ alta kara kutu (süre damgası) konunca kaybolan bir şey var mı: YOK olmalı
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez; ⓑ kayboluyorsa punto büyür ya da kelime azalır
                 ⭐ aynı test S0'ın 0. karesine de: çamurdaki uçak 120 px'te uçak mı? (açılış nesnesi)
② KAPAK KANITI  zincir_kontrol.sh g30_kaynak.jpg kapak.png → çıkış: ⬜ (üretimden sonra)   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → yabancı dönüm noktasını (sel + kano) söyleyebiliyor mu:
                HAYIR olmalı [§3.3]. ⚠️ kapak bitmiş evi gösterir (kanal kuralı: kapak = GN) — vaat budur, dönüm noktası değil.
④ BAŞLIK = VAAT  kapak: "bu uçak bir ev oldu ve havada" · başlık: "yavaş kalkış" — aynı vaat ✓
```
