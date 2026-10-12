# 🖼️ THE_SUNKEN_STAGE — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30] · sahip kararı 19.09.2026 (kapak yalnız GN
karesinden, öncesi/sonrası bölme YOK) · sahip senaryosu ("Kapak: S20'nin son karesi. Açık taş yaylar, sıcak sahne kabuğu, seyirci
ve mavi akşam birlikte görünür. Önce/sonra bölmesi kullanılmaz. İmkânsız bir ikinci tiyatro veya videoda bulunmayan bir dev yapı
eklenmez. Tiyatro küçük kalıyorsa ayrı bir kamera icat etmek yerine ana kadraj üretim başında sıkılaştırılır.") — depoda G20

## 0. TEK İŞ: KÜÇÜK RESİM (video içi kapak kartı YOK)

```
KAYNAK KARE     G20 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Aşağıda usta kare (G20) promptunun kopyası;
                BAŞLIKLI sürümde tek ek cümle (başlık bandı). Model başlığı YAZMAZ; tipografi post-prodüksiyon.
KAPAK KARTI     ⛔ YOK — teslim 160,0 sn, son kare G20 (hikâye SAPMA ②). Bu dosya yalnız PLATFORM KÜÇÜK RESMİDİR (1280×720).
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
VARSAYILAN      ⭐ BAŞLIKLI — "THE SUNKEN STAGE" (İngilizce · 3 kelime) — depo kuralı kapağa İngilizce başlık ister; senaryo
                kapakta yazı demedi (hikâye SAPMA ⑮). Başlık sahnenin ve kabuğun ÜSTÜNDE, kaya ile çamlar arasındaki koyu
                orman bandında.
YEDEK           YAZISIZ — kare kendisi söyler: mavi akşamda ışıklı sahne, bakır kabuk, dolu yaylar
ÖLÇÜ            16:9 · küçük resim 1280×720 (kaynak 1920×1080 G20 karesi) · ⛔ öncesi/sonrası bölme YOK (sahip 19.09.2026 + senaryo)
⛔ YASAK        ikinci tiyatro · videoda olmayan dev yapı · havai fişek · lazer · sahte ok/daire · yazı/logo (senaryo "Kapak"
                satırı) · antik harabe görünümü
```

---

## 📸 KAPAK GÖRSEL PROMPTU — YAZISIZ (G20 kopyası)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.
> ⭐ Tercih: önce teslim dosyasının 159,5. saniyesindeki kare kullanılır; yalnız o kare uygun değilse aşağıdaki prompt
> G20'den image-to-image koşulur (G20 referans).
> Metin `bolum_uretici.py`'nin ürettiği usta kare promptundan betikle kopyalandı (12.10.2026); tek fark baş satır.

```
Photorealistic documentary site photograph — cover frame made from master frame G20. Horizontal 16:9 time-lapse of a restored open-air theatre in a forest hollow on its opening evening; a photograph from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 1600.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: all twelve stone terraces carry continuous warm brown timber seat boards between the three stair aisles of steps; a broad warm timber stage floor covers the whole stone stage platform; the fan-shaped acoustic shell stands complete over the rear third of the stage, warm copper-coloured on its upper outer face and pale timber on its curved inner face; two compact dark steel towers stand at the left and right sides of the stage, hung with black loudspeaker and lighting units; two broad pale paved paths lined with low lamps lead from the lower left and lower right edges of the frame to the entrances at the top of the left and right aisles; a small ensemble of musicians sits on chairs among music stands across the front of the stage, playing under the full warm light of the main stage lights on both towers; the step lamps along the three aisles, the warm light inside the shell and the low path lamps are lit. Most seats on the twelve terraces are taken by a seated audience, small distant figures with their backs to the camera, the three aisles clear, a few people in the front rows standing and clapping. The hardstand lies raked and empty.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Ten to six on an autumn evening, deep blue hour: the restored theatre is full, and the music has begun.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The shell rises to about 75 percent of frame height above the middle of the stage. The two towers stand at about 689 and 1231 pixels from the left, their tops at about 68 percent of frame height. The lit stage and shell are the brightest things in the frame. Nothing that proves progress falls into the top-right corner of the frame.

LIGHTING: Sun azimuth 262 degrees, elevation 5 degrees below the horizon, behind the camera on the left: deep clear blue hour, the sky still readable, the stone, the timber seats, the shell and the trees clearly visible; the air is clear and dry, and the lit lamps are small warm points with crisp edges. The sun is below the horizon, outside the frame.

TIME RATE: Everything in this frame moves at natural speed: the people, the trees and the sky. Eight seconds pass across this shot: the light holds, the clouds hold still, the treetops sway slightly in a light breeze, and people move in small natural ways.

ACTIVITY: The ensemble plays and the audience applauds; a stage crew moves along the right tower platform, and the treetops sway slightly. People are small distant figures, the audience seated with their backs to the camera, the musicians far away on the stage, no readable faces.

SITE TEXTURE: Clean pale stone, warm timber seat boards with a soft sheen, cables taped along the edge of the stage, fallen leaves in the corners of the steps, raked gravel with the faint print of tyre tracks. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The towers stand bolted on their footings beside the stage, the shell is bolted to its ribs on base plates anchored in the stone platform, and the audience sits on the timber seat boards bolted to the stone terraces.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

## 📸 KAPAK GÖRSEL PROMPTU — BAŞLIKLI (başlık bandı)

> Tek fark: COMPOSITION'ın sonuna başlık bandı cümlesi. Varsayılan sürüm budur; başlık post-prodüksiyonda konur.

```
Photorealistic documentary site photograph — cover frame made from master frame G20. Horizontal 16:9 time-lapse of a restored open-air theatre in a forest hollow on its opening evening; a photograph from a fixed 16 mm site camera.
Lens: 16 mm rectilinear, f/8, ISO 1600.
Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.

STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two paved audience paths. AT THIS STAGE: all twelve stone terraces carry continuous warm brown timber seat boards between the three stair aisles of steps; a broad warm timber stage floor covers the whole stone stage platform; the fan-shaped acoustic shell stands complete over the rear third of the stage, warm copper-coloured on its upper outer face and pale timber on its curved inner face; two compact dark steel towers stand at the left and right sides of the stage, hung with black loudspeaker and lighting units; two broad pale paved paths lined with low lamps lead from the lower left and lower right edges of the frame to the entrances at the top of the left and right aisles; a small ensemble of musicians sits on chairs among music stands across the front of the stage, playing under the full warm light of the main stage lights on both towers; the step lamps along the three aisles, the warm light inside the shell and the low path lamps are lit. Most seats on the twelve terraces are taken by a seated audience, small distant figures with their backs to the camera, the three aisles clear, a few people in the front rows standing and clapping. The hardstand lies raked and empty.

SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand beside the left end of the stage platform.

THE TIME MOMENT: Ten to six on an autumn evening, deep blue hour: the restored theatre is full, and the music has begun.

COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about 90 percent of frame height. The split pale rock spans about 98 pixels of frame width, from about 286 to 384 pixels from the left, its top at about 91 percent, and keeps that width and position in every frame. The seating bowl spans from about 266 to 1654 pixels from the left at its widest, its near rim lowest at about 21 percent of frame height in the middle; the stage platform lies at the upper centre, its front edge from about 719 to 1201 pixels at about 50 percent. The shell rises to about 75 percent of frame height above the middle of the stage. The two towers stand at about 689 and 1231 pixels from the left, their tops at about 68 percent of frame height. The lit stage and shell are the brightest things in the frame. Nothing that proves progress falls into the top-right corner of the frame. The dark forested slope above the back wall, between the split rock and the two pines, from about a tenth to about a fifth of the frame height below the top edge, stays calm and even in tone, with no bright object in it — an empty band.

LIGHTING: Sun azimuth 262 degrees, elevation 5 degrees below the horizon, behind the camera on the left: deep clear blue hour, the sky still readable, the stone, the timber seats, the shell and the trees clearly visible; the air is clear and dry, and the lit lamps are small warm points with crisp edges. The sun is below the horizon, outside the frame.

TIME RATE: Everything in this frame moves at natural speed: the people, the trees and the sky. Eight seconds pass across this shot: the light holds, the clouds hold still, the treetops sway slightly in a light breeze, and people move in small natural ways.

ACTIVITY: The ensemble plays and the audience applauds; a stage crew moves along the right tower platform, and the treetops sway slightly. People are small distant figures, the audience seated with their backs to the camera, the musicians far away on the stage, no readable faces.

SITE TEXTURE: Clean pale stone, warm timber seat boards with a soft sheen, cables taped along the edge of the stage, fallen leaves in the corners of the steps, raked gravel with the faint print of tyre tracks. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The towers stand bolted on their footings beside the stage, the shell is bolted to its ribs on base plates anchored in the stone platform, and the audience sits on the timber seat boards bolted to the stone terraces.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split rock, the two pines, the back wall and the service road never change shape, position, size or spacing. The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Kamera 27° aşağı baktığı için gök bandı dar (ufuk üstten 105, ağaç çizgisi ≈105). Başlık bu yüzden göğe değil, gök bandının
ALTINDAKİ koyu orman yamacına konur: üstten ≈120–230 px, x ≈520–1400 — solda yarık kaya (x 286–384 · üstten 94–201), sağda çamlar
(x 1490–1557) bandın DIŞINDA; kabuğun tepesi (üstten 267) ve kuleler (349) bandın ALTINDA. Üst 60 px oynatıcı bandına ve sağ üst
300×100 px'e girmez · süre damgası sağ alttadır; sahne, kabuk ve dolu sıralar ona düşmez [A15-c]. ⚠️ Orman yamacının gerçek tonu
usta karede ölçülür; bant çok parlak ya da karışıksa yazısız kapak kullanılır.

---

## 🔤 BAŞLIK DİZGİSİ (BAŞLIKLI sürüm · post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        THE SUNKEN STAGE (büyük harf · tek satır · 3 kelime)
YÜKSEKLİK    büyük harf ≈ 88–92 px @1080 (≈ %8,3 — §2.3'ün ≥ 86 px kuralı ✓) · 120 px'e küçülünce ≈ 10 px: kelime seçilir
KONUM        x ≈ 520–1400 px (genişlik ≈ 880 px) · y ≈ 130–222 px (1080 ölçeğinde) · kaya ile çamların arasında · kabuğun ve
             kulelerin üstünde · sağ üst 300×100 px'e ve alt 100 px'e girmez
RENK         sıcak amber #F2A03D (kanal vurgusu — KANAL_KIMLIGI) · mavi saatte koyu orman yamacına karşı kontrast ≥ 4,5:1 (yetmezse
             bandın arkasına %35 opaklıkta düz koyu şerit — gradyan değil)
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ silüet (koyu mavi çerçevede açık renkli eş merkezli yaylar + üst
                 ortada sıcak ışık kümesi: sahne + bakır kabuk) okunuyor mu · ⓑ başlık (BAŞLIKLI) seçiliyor mu · ⓒ sağ alta
                 kara kutu (süre damgası) konunca kaybolan bir şey var mı: YOK olmalı
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez
                 ⭐ aynı test S0'ın 0. karesine de: kahverengi suyun içinden çıkan iki açık renkli yay (120 px'te ≈2 px kalınlıkta
                    iki eş merkezli çizgi) ve sol üstteki sarı pompalar okunuyor mu? (açılış nesnesi)
                 ⚠️ seyirci 120 px'te tek tek okunmaz — yaylar üstünde DOKU olarak okunur; ışık KÜME olarak okunur [ISIK_FINALI §6]
② KAPAK KANITI  zincir_kontrol.sh g20_kaynak.jpg kapak.png → çıkış: ⬜ (üretimden sonra)   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → yabancı dönüm noktasını (suyun altından tiyatronun
                çıkışı + aynı akşam konser) söyleyebiliyor mu: kısmen — kapak bitmiş, dolu tiyatroyu gösterir (sahip kuralı:
                kapak = GN) ve başlık "su basmış tiyatro" der; suyun nasıl çekildiği, çamur, onarım ve kabuğun kuruluşu saklı
                kalır [§3.3].
④ BAŞLIK = VAAT  kapak: "mavi akşamda ışıklı, dolu bir orman tiyatrosu" · başlık: "su basmış tiyatro hayata dönüyor" — vaat aynı ✓
```
