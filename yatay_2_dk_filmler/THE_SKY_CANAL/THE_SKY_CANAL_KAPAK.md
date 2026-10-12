# 🖼️ THE_SKY_CANAL — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30] · sahip kararı 19.09.2026 (kapak yalnız GN
karesinden, öncesi/sonrası bölme YOK) · sahip senaryosu ("Kapak: G20 / S20'nin bitmiş son kaynak karesi … İlk öneri yazısız
kapaktır; film adı gerekiyorsa THE SKY CANAL kurgu sırasında küçük ve okunur biçimde eklenir") — depoda G20

## 0. TEK İŞ: KÜÇÜK RESİM (video içi kapak kartı YOK)

```
KAYNAK KARE     G20 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Aşağıda usta kare (G20) promptunun kopyası;
                YEDEK sürümde tek ek cümle (gök bandı). Model başlığı YAZMAZ; tipografi post-prodüksiyon.
KAPAK KARTI     ⛔ YOK — teslim 160,0 sn, son kare G20 (hikâye SAPMA ②). Bu dosya yalnız PLATFORM KÜÇÜK RESMİDİR (1280×720).
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 159.5 -i teslim.mp4 -frames:v 1 g20_kaynak.jpg
                bash araclar/zincir_kontrol.sh g20_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
VARSAYILAN      ⭐ YAZISIZ (sahibin ilk tercihi · hikâye SAPMA ⑭) — kare kendisi söyler: vadinin üstünde suyla dolu kanal
                köprüsü, ucunda kırmızı tekne, çok aşağıda nehir
YEDEK           "THE SKY CANAL" (İngilizce · 3 kelime) gök bandında, küçük — ⚠️ MUZIK_VE_KAPAK §2.3'ün ≥ %8 punto kuralının
                ALTINDA kalır (gök bandı dar, ≈100 px); sahip "küçük ve okunur" dedi → beyanlı
ÖLÇÜ            16:9 · küçük resim 1280×720 (kaynak 1920×1080 G20 karesi) · ⛔ öncesi/sonrası bölme YOK (sahip 19.09.2026)
⛔ YASAK        sahte düşüş oku, kırık tekne, filmde olmayan kaza, ikinci tekne, yazı/logo (sahip senaryosu "Kapak" satırı) ·
                Roma kemerli su kemeri görünümü
```

---

## 📸 KAPAK GÖRSEL PROMPTU — VARSAYILAN (G20 kopyası, yazısız)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.
> ⭐ Tercih: önce teslim dosyasının 159,5. saniyesindeki kare kullanılır; yalnız o kare uygun değilse aşağıdaki prompt
> G20'den image-to-image koşulur (G20 referans).
> Metin `bolum_uretici.py`'nin ürettiği usta kare promptundan betikle kopyalandı (11.10.2026); tek fark baş satır.

```
Photorealistic documentary site photograph — cover frame made from master frame G20. Horizontal 16:9 time-lapse of a steel canal bridge built high across a green river valley; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge high on the left valley slope, lens 85 metres above the river, 135 metres from the middle of the bridge along the lens axis, bearing 20 degrees, tilt 17 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a navigable steel canal bridge: an open-topped steel water trough 100 metres long, 8 metres wide inside and 2 metres deep, carried high over the valley on three spans by two tall pale concrete piers and two bank abutments, with a walkway and railing along its near side and a vertical-lift steel gate at each end where it meets the canal on each bank. AT THIS STAGE: the open-topped steel trough runs from bank to bank over both piers, deep charcoal grey outside, its ends joined to the gate frames, lined inside from end to end with a dry matte pale blue lining; a galvanised walkway on brackets runs along its near wall, with steel access steps at each end and a railing along its outer edge; calm clear water stands in it at three quarters of the wall height, level with the canal arms. The two tall pale concrete piers stand on the lower slopes either side of the river, the two abutments at the bank edges, both steel gates are raised high in their frames, so the trough lies open to the canal arm on each bank. The same small red canal boat with a cream cabin lies still on the water at the right end of the trough, its bow at the open right gate, its hull low in the water, a helmsman at its stern; two people stand on the walkway beside it, small figures, no readable faces. The work pads lie raked and empty.

SITE / BACKGROUND: A deep green river valley with steep wooded slopes, seen from high on its left side looking up the valley. A natural river about fifteen metres wide runs down the valley floor between pale gravel flats towards the camera, far below the line of the bridge, a rough track beside it. Upstream two long wooded ridges meet a level skyline. On the left bank a short water-filled canal arm along the hillside widens into a basin before the left gate frame, and a fixed steel filling pipe with a large valve wheel runs from the basin over that frame. On the right bank a short water-filled canal arm leads from the right gate frame into the trees. Gravel service roads come in from both side edges to a work pad on each bank. A single tall dark pine with a flat crown stands on a rock outcrop on the right slope below the right bank.

THE TIME MOMENT: Seventeen minutes to five in the afternoon, golden hour, autumn: the boat has crossed the valley on the canal bridge.

COMPOSITION: Horizontal 16:9, the camera looking down 17 degrees, the level skyline at about 86 percent of frame height. The dark pine spans about 72 pixels of frame width, from about 1475 to 1547 pixels from the left, its crown top at about 42 percent, and keeps that width and position in every frame. The abutments stand at about 538 and 1398 pixels, the piers at about 844 and 1182 pixels from the left. The bridge runs in one straight line from about 538 to 1398 pixels from the left, its near top edge falling gently from about 38 to 48 percent of frame height. The river passes under the centre span at about 1002 pixels from the left. The red boat lies at the right end of the trough from about 1242 to 1368 pixels from the left, at about 48 percent of frame height. Nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.

LIGHTING: Sun azimuth 250 degrees, elevation 6 degrees, low behind the camera on the left, outside the frame: warm golden late light on the bridge, the slopes and the water, the valley floor already in soft shade, long shadows to the right. Autumn: the woods on the slopes are turning gold, orange and rust; the pine stays dark green. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate, gently: clouds, shadows, water, the boat and people all move about eight times faster than normal. About one minute passes across this shot: shadows stay put, clouds drift slowly, the water moves gently.

ACTIVITY: The red boat lies still at the open right gate; the two people stand still on the walkway, and the river runs far below. People are small figures with only faint soft motion streaks as they move, backs to the camera, no readable faces.

SITE TEXTURE: Calm clear water over the pale blue lining with a soft sheen of sky, a narrow dry band of lining above the water line, charcoal coating with a satin sheen, a film of dust on the walkway gratings, raked gravel with the faint print of tyre tracks, dark water stains below the pier tops. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The boat sits on the water at the right end of the trough, its weight carried by the water. The trough rests on its bearings on the piers, and the railing posts are bolted to the walkway. The gates sit raised in their frames.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The valley slopes, the river, the skyline ridges, the roads, the canal arms and the pine never change shape, position, size or spacing. The valley holds exactly one canal bridge, this one, on exactly two piers, and exactly one boat. Nothing already built is removed or resized; no opacity fades. Water stays inside the canal arms and the trough. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

## 📸 KAPAK GÖRSEL PROMPTU — YEDEK (başlık için gök bandı)

> Tek fark: COMPOSITION'ın sonuna gök bandı cümlesi. Yalnız yazılı kapak seçilirse koşulur.

```
Photorealistic documentary site photograph — cover frame made from master frame G20. Horizontal 16:9 time-lapse of a steel canal bridge built high across a green river valley; a progress photograph from a fixed 24 mm site camera.
Lens: 24 mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to a rock ledge high on the left valley slope, lens 85 metres above the river, 135 metres from the middle of the bridge along the lens axis, bearing 20 degrees, tilt 17 degrees down, zero roll. The camera never moves.

STRUCTURE: When finished this will be a navigable steel canal bridge: an open-topped steel water trough 100 metres long, 8 metres wide inside and 2 metres deep, carried high over the valley on three spans by two tall pale concrete piers and two bank abutments, with a walkway and railing along its near side and a vertical-lift steel gate at each end where it meets the canal on each bank. AT THIS STAGE: the open-topped steel trough runs from bank to bank over both piers, deep charcoal grey outside, its ends joined to the gate frames, lined inside from end to end with a dry matte pale blue lining; a galvanised walkway on brackets runs along its near wall, with steel access steps at each end and a railing along its outer edge; calm clear water stands in it at three quarters of the wall height, level with the canal arms. The two tall pale concrete piers stand on the lower slopes either side of the river, the two abutments at the bank edges, both steel gates are raised high in their frames, so the trough lies open to the canal arm on each bank. The same small red canal boat with a cream cabin lies still on the water at the right end of the trough, its bow at the open right gate, its hull low in the water, a helmsman at its stern; two people stand on the walkway beside it, small figures, no readable faces. The work pads lie raked and empty.

SITE / BACKGROUND: A deep green river valley with steep wooded slopes, seen from high on its left side looking up the valley. A natural river about fifteen metres wide runs down the valley floor between pale gravel flats towards the camera, far below the line of the bridge, a rough track beside it. Upstream two long wooded ridges meet a level skyline. On the left bank a short water-filled canal arm along the hillside widens into a basin before the left gate frame, and a fixed steel filling pipe with a large valve wheel runs from the basin over that frame. On the right bank a short water-filled canal arm leads from the right gate frame into the trees. Gravel service roads come in from both side edges to a work pad on each bank. A single tall dark pine with a flat crown stands on a rock outcrop on the right slope below the right bank.

THE TIME MOMENT: Seventeen minutes to five in the afternoon, golden hour, autumn: the boat has crossed the valley on the canal bridge.

COMPOSITION: Horizontal 16:9, the camera looking down 17 degrees, the level skyline at about 86 percent of frame height. The dark pine spans about 72 pixels of frame width, from about 1475 to 1547 pixels from the left, its crown top at about 42 percent, and keeps that width and position in every frame. The abutments stand at about 538 and 1398 pixels, the piers at about 844 and 1182 pixels from the left. The bridge runs in one straight line from about 538 to 1398 pixels from the left, its near top edge falling gently from about 38 to 48 percent of frame height. The river passes under the centre span at about 1002 pixels from the left. The red boat lies at the right end of the trough from about 1242 to 1368 pixels from the left, at about 48 percent of frame height. Nothing that proves progress falls into the bottom tenth or the top-right corner of the frame. The sky above the two wooded ridges, from the top edge down to about a tenth of the frame height, stays clear, calm and even, with no cloud edges — an empty band.

LIGHTING: Sun azimuth 250 degrees, elevation 6 degrees, low behind the camera on the left, outside the frame: warm golden late light on the bridge, the slopes and the water, the valley floor already in soft shade, long shadows to the right. Autumn: the woods on the slopes are turning gold, orange and rust; the pine stays dark green. The sun stays outside the frame.

TIME RATE: Everything in this frame is time-lapsed at the same rate, gently: clouds, shadows, water, the boat and people all move about eight times faster than normal. About one minute passes across this shot: shadows stay put, clouds drift slowly, the water moves gently.

ACTIVITY: The red boat lies still at the open right gate; the two people stand still on the walkway, and the river runs far below. People are small figures with only faint soft motion streaks as they move, backs to the camera, no readable faces.

SITE TEXTURE: Calm clear water over the pale blue lining with a soft sheen of sky, a narrow dry band of lining above the water line, charcoal coating with a satin sheen, a film of dust on the walkway gratings, raked gravel with the faint print of tyre tracks, dark water stains below the pier tops. A documentary site photograph on colour negative film, true colour, fine grain.

PHYSICS: The boat sits on the water at the right end of the trough, its weight carried by the water. The trough rests on its bearings on the piers, and the railing posts are bolted to the walkway. The gates sit raised in their frames.

NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The valley slopes, the river, the skyline ridges, the roads, the canal arms and the pine never change shape, position, size or spacing. The valley holds exactly one canal bridge, this one, on exactly two piers, and exactly one boat. Nothing already built is removed or resized; no opacity fades. Water stays inside the canal arms and the trough. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Kamera 17° aşağı baktığı için gök bandı dar: ufuk üstten 149'da, iki ağaçlı sırt onun biraz üstüne çıkar (≈100–149). Bant
sırtların ÜSTÜNE konur (üst 60 px oynatıcı bandının altında, üstten ≈62–110). Tekne (x 1242–1368 · üstten 549–575), köprü
(538–1398) ve çam (1475–1547 · 622–819) bandın çok altında. Sağ üst 300×100 px'e girmez · süre damgası sağ alttadır; tekne
ve köprü ona düşmez [A15-c]. ⚠️ Sırtların gerçek yüksekliği usta karede ölçülür; bant sırtlara değiyorsa yazılı kapak
düşer, yazısız kapak kullanılır.

---

## 🔤 BAŞLIK DİZGİSİ (yalnız YEDEK · post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        THE SKY CANAL (büyük harf · tek satır · 3 kelime)
YÜKSEKLİK    büyük harf ≈ 44–48 px @1080 (≈ %4,3) — ⚠️ §2.3'ün ≥ 86 px kuralının altında (bant dar · sahip "küçük")
             · 120 px'e küçülünce ≈ 5 px: küçük resimde KELİME okunmaz, yalnız bant olarak görünür
KONUM        x ≈ 640–1280 px · y ≈ 62–110 px (1080 ölçeğinde) · iki sırtın üstünde · sağ üst 300×100 px'e ve alt 100
             px'e girmez
RENK         sıcak amber #F2A03D (kanal vurgusu — KANAL_KIMLIGI) · altın saat göğüne karşı kontrast ≥ 4,5:1 (yetmezse
             bandın arkasına %35 opaklıkta düz koyu şerit — gradyan değil)
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ silüet (yeşil-altın vadide koyu yatay köprü çizgisi + ince
                 parlak su bandı + sağ ucunda kırmızı nokta) okunuyor mu · ⓑ (yedekte) bant ayırt ediliyor mu · ⓒ sağ alta
                 kara kutu (süre damgası) konunca kaybolan bir şey var mı: YOK olmalı
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez
                 ⭐ aynı test S0'ın 0. karesine de: solda havuzdaki kırmızı tekne (≈220 px → 120 px'te ≈14 px) ve askıdaki
                    parça okunuyor mu? (açılış nesnesi)
                 ⚠️ 120 px'te G20 teknesi ≈8 × 3 px — küçük resimde bir SICAK NOKTA olarak okunur; ayrıntı değil, renk farkı
                    taşır (kırmızı + krem, kömür grisi köprü üstünde)
② KAPAK KANITI  zincir_kontrol.sh g20_kaynak.jpg kapak.png → çıkış: ⬜ (üretimden sonra)   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → yabancı dönüm noktasını (kuru oluğa ilk suyun
                gelişi + seviye eşitlenince kapakların kalkması) söyleyebiliyor mu: kısmen — kapak dolu köprüyü ve karşıya
                varmış tekneyi gösterir (sahip kuralı: kapak = GN); dolum ve kapaklar saklı kalır [§3.3].
④ BAŞLIK = VAAT  kapak: "vadinin üstünde suyla dolu köprü ve ucunda tekne" · başlık: "tekneler için bir köprü" — vaat aynı ✓
```
