KAYNAK        profesyonel timelapse yapımcısı (insan · dış okuma) — proje sahibi iletti
OKUNAN        THE MOUNTAIN DOOR v1 — planı + QA sonucu (üretilmiş film)
TARİH         07.09.2026
TÜR           FİLM/PLAN OKUMASI — mercek koşusu DEĞİL; yapımcının kendi şablon önerisini içerir
KESİLDİ Mİ    hayır — proje sahibinin ilettiği metin olduğu gibi (soru satırı dahil)

⛔ Aşağısı dokunulmamış ham metindir. Düzenleme · kısaltma · özetleme YOK.
   Ajanın ne anladığı kilavuzlar/DERSLER.md "DÖRT FİLM OKUMASI" bölümündedir (P2-a…l).

---

Yapıştırılan markdown.md
Dosya
bu video iicin sağlam bir eleştiri yaparmısın ve sen olsan nasıl yaparın nasıl bir şablon kullanırıdın iamge ve image to video promtları icin 

Evet. Bu sefer "The Mountain Door" özelinde bakınca bence temel fikir, önceki kule projesinden bile daha iyi; çünkü dönüşüm tek bakışta okunabiliyor: kapalı kaya yüzü → portal → beton yapı → yol → çalışan tünel. Ayrıca dosyanın kendi QA sonucu önemli bir şey söylüyor: prompt kapısından geçen film, üretimde beş mercekte düşmüş; özellikle kamera push-in'i, zincirin kopması ve kanıt nesnesinin kaybolması sorun olmuş.

Ben burada promptları "daha ayrıntılı" değil, daha hiyerarşik ve daha az çelişkili yapardım.

En büyük sorunlar

Birinci sorun prompt ile üretim kontrol sisteminin birbirine karışması. 620 m, 12.4 m, 62 lamba, 14 panel, 15 m aks, azimutlar, yüzde konumlar vb. production bible açısından değerli. Fakat görüntü modelinin hepsini aynı anda doğru çözmesini beklemek gereksiz risk yaratıyor.

İkinci sorun daha kritik: I2V'ye inşaat yaptırmaya çalışıyorsun. Örneğin "berm büyüsün, kar gelsin, güneş dönsün, kamyon çalışsın, beton dökülsün" aynı altı saniyede olduğunda modelin attention bütçesi parçalanıyor. Sonuçta esas istediğimiz portal yerine kaya şekli veya kamera değişebiliyor.

Üçüncü sorun, dosyada zaten ölçülmüş: "fixed tripod" yazmak kamerayı gerçekten kilitlememiş. Buradan benim çıkaracağım ders şu olurdu:

Kamera kilidi prompt problemi değil, üretim pipeline problemidir.

Yani 15 kere "zero movement" yazmak yerine aynı referans kare/seed/edit zinciri + varsa motion/camera controls üzerinden kilitlemek gerekir.

Dördüncü sorun: bu projede 620 metrelik tünelin ilerlemesini göstermeye çalışmak gereksiz. Kamera zaten tünelin içini görmüyor. Dosyanın en iyi fikirlerinden biri aslında bunu fark etmiş olması: ilerlemenin görsel göstergesi portal önü, pasa, headwall, canopy, retaining wall ve yol. Ben bunu daha da ileri götürür, "tünel 300 metre ilerledi" gibi görünmeyen bilgileri image promptundan tamamen çıkarırdım.

Benim versiyonum 4 keyframe + 4 I2V olurdu. Ve master kareyi önce üretirdim:

IMAGE 4 MASTER → IMAGE 3 → IMAGE 2 → IMAGE 1

Sonra videoyu ileri oynatırdım:

1→2 → 2→3 → 3→4 → final hero.

Aşağıdaki şablon tam olarak bunu hedefliyor.

⛰️ IMAGE 1 — Untouched Mountain / First Cut
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photograph. Static tripod permanently fixed to the opposite rocky slope, natural 24mm wide-angle lens feel, approximately 16 metres above the future road platform. Identical framing, perspective and horizon throughout the entire sequence. Preserve five permanent landmarks exactly: the grey rock buttress with two vertical clefts on frame right, the old mountain pass road with exactly two visible hairpin bends above the future portal, one large flat-topped granite boulder near the lower-left side of the future road, one small stone arch bridge over the stream below, and the distant ridge with one distinctive rock horn.

STAGE: Before major tunnel construction. A steep natural rock face blocks the future road alignment. Only the first shallow excavation scar has been cut into the base of the mountain directly below the lower cleft. One tracked excavator works against the rock and one dump truck waits nearby. No tunnel portal, concrete headwall, canopy, retaining wall or paved road exists.

DETAILS: Real mountain construction environment in summer. Excavator bucket physically breaks loose fractured rock, fresh pale spoil rests naturally below the cut, dry rock dust hangs near ground level, tyre tracks cross loose scree, alpine vegetation surrounds the disturbed area. The old pass road remains clearly visible above. Natural daylight, realistic shadows, documentary photography rather than architectural visualization.

NEGATIVE: No text, logos or watermarks. No camera movement or perspective change. Do not move, resize, reshape or replace the rock buttress, its two clefts, the two old-road hairpins, granite boulder, stone bridge, distant ridge or rock horn. No tunnel portal yet. No concrete structures. No floating machinery, impossible excavation, melting rock, warped mountain geometry, duplicated landmarks, artificial CGI appearance or sudden unexplained objects.

Generate in OpenArt

🚧 IMAGE 2 — Portal Excavation
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photograph. Exact same static tripod position, 24mm lens feel, camera height, framing, perspective and horizon as IMAGE 1. Preserve exactly the same grey rock buttress with two vertical clefts on frame right, two hairpin bends of the old pass road above, flat-topped granite boulder, stone arch bridge, stream and distant ridge with one rock horn. Every permanent landmark must remain identical in shape, scale and screen position.

STAGE: Active tunnel excavation in autumn. The same excavation scar has developed into one clearly defined tunnel mouth cut into the mountain. The portal opening is approximately 12 metres wide with a high arched excavation profile. Exposed rock around the opening is stabilized with sprayed concrete and visible rock-bolt plates. A rough graded approach platform now reaches the opening. A drilling jumbo works partly inside the tunnel and dump trucks remove broken rock. A pale spoil terrace has begun accumulating beside the approach. No finished architectural portal, canopy, retaining wall or asphalt exists yet.

DETAILS: Workers in PPE guide real equipment. Broken rock, wet mud, deep tyre ruts, puddles, ventilation duct, stacked steel support elements, cables and temporary construction materials. Rust-brown autumn vegetation and first traces of snow high on the distant ridge. Physically plausible excavation, load paths and material piles.

NEGATIVE: No text, logos or watermarks. No camera drift, zoom, push-in, pan or perspective change. Permanent landmarks remain untouched. Do not redesign the mountain. No completed tunnel portal, finished road or decorative architecture. No floating equipment, impossible rock overhangs, warped tunnel opening, duplicated machinery, instant construction, teleporting objects or CGI render appearance.

Generate in OpenArt

❄️ IMAGE 3 — Winter Structural Works
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photograph. Exact same locked tripod, framing, perspective, horizon and 24mm lens feel as IMAGE 1 and IMAGE 2. Preserve exactly the same rock buttress with two clefts, two old-road hairpins, flat-topped granite boulder, stone arch bridge, stream and distant ridge with one rock horn.

STAGE: Winter structural construction of the same tunnel portal. The excavated tunnel mouth remains in exactly the same location and proportions as IMAGE 2. A reinforced-concrete headwall now surrounds the opening and a concrete canopy projects outward above it. A retaining wall extends along the new approach embankment. The road platform remains unfinished. Workers are completing concrete and drainage works using realistic formwork, pump equipment and compact machinery. No finished asphalt, final safety barriers or completed landscaping yet.

DETAILS: Dirty tracked winter snow rather than pristine snow. Grey slush, black mud, frozen tyre ruts, meltwater, concrete stains, temporary formwork, cables and stacked materials. Workers in winter PPE physically operate equipment. Snow accumulates on stable surfaces while active vehicle paths remain muddy and disturbed. Realistic cold diffuse light and physically correct shadows.

NEGATIVE: No text, logos or watermarks. No camera movement, push-in, zoom or reframing. Do not change the tunnel opening or permanent mountain landmarks. No clean fantasy snow, floating concrete, unsupported canopy, warped retaining wall, instant material appearance, disappearing equipment without physical removal, duplicated structures, architectural visualization look or impossible geometry.

Generate in OpenArt

🚇 IMAGE 4 — Master Final / Mountain Door
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photograph. Master continuity frame. Same static tripod position, 24mm wide-angle lens feel, camera height, framing, perspective and horizon as every previous stage. Preserve exactly the grey rock buttress with two vertical clefts on frame right, the old pass road with exactly two hairpin bends above the portal, the flat-topped granite boulder, stone arch bridge and stream below, and the distant ridge with one rock horn.

STAGE: Final completed tunnel and road in summer one year later. The same portal is fully finished with its reinforced-concrete headwall and canopy. A dark asphalt road approaches from the valley and continues naturally into the tunnel. The retaining wall and roadside safety barrier are complete. A single orderly line of warm tunnel lights recedes deep into the dark opening. All temporary construction equipment, formwork, containers and fencing have been physically removed. The pale excavated rock terrace remains permanently visible as a scar on the mountain. The old pass road and its two hairpin bends remain physically unchanged above but are completely empty, with a simple pale gravel barrier closing its lower entrance.

DETAILS: Deep green summer vegetation has returned around disturbed areas while the permanent pale excavation scar remains visible. Realistic new asphalt, dusty shoulders, drainage, subtle tyre marks and restrained roadside finishing. A few vehicles physically travel through the new tunnel while the abandoned old road stays empty. Natural summer light, realistic concrete weathering and physically correct tunnel-light falloff.

NEGATIVE: No text, logos or watermarks. No camera movement or changed perspective. Do not beautify or redesign the mountain. Do not remove the permanent excavation scar or old pass road. No extra tunnel mouths, extra roads, extra hairpins, duplicated lamps, impossible lamp spacing, glowing portal, fantasy lighting, warped concrete, floating barriers, CGI appearance or sudden unexplained objects.

Generate in OpenArt

Video promptlarında ise özellikle image'i yeniden tarif etmiyorum. Image zaten geometry'nin kaynağı. Video promptunun görevi hareket.

⛏️ VIDEO 1 — First Cut → Tunnel Mouth
SCENE LOCK: Begin exactly from IMAGE 1. Preserve the source image composition and all permanent mountain landmarks pixel-stably throughout. Static tripod with absolutely no push-in, zoom, pan, tilt, orbit, shake, drift or reframing.

STAGE: Progress naturally from the first mountain cut toward the excavated portal condition represented by IMAGE 2.

DETAILS: Workers and machines physically perform every change. The excavator repeatedly breaks fractured rock from the face, rotates, loads dump trucks and returns for another cycle. Trucks physically drive away carrying spoil. The excavation gradually widens and deepens through repeated mechanical cycles rather than appearing instantly. Rock debris falls under gravity and the spoil terrace grows load by load. Workers install temporary stabilization around the emerging tunnel opening. Dust pulses after excavation and settles between cycles. Natural timelapse cloud and shadow motion continues while construction remains the dominant transformation.

NEGATIVE: No cuts, camera movement, push-in, zoom, morphing mountain, melting rock, instant tunnel opening, teleporting machinery, disappearing debris, floating equipment or changing landmarks. Nothing snaps into place. No text, logos or watermarks.

Animate in OpenArt

🚜 VIDEO 2 — Excavation → Winter Portal Structure
SCENE LOCK: Begin exactly from IMAGE 2. Preserve the tunnel opening, mountain geometry and every permanent landmark. Static tripod, identical framing throughout, absolutely no automatic cinematic push-in or camera motion.

STAGE: Construction progresses from the excavated tunnel mouth toward the winter structural condition represented by IMAGE 3.

DETAILS: Dump trucks repeatedly remove broken rock while workers stabilize the portal. Crews physically position reinforcement, assemble formwork and connect concrete equipment. Concrete is pumped into supported formwork in visible sequential operations. The headwall develops through believable construction phases and the canopy is formed only after its supporting structure exists. Earthmoving equipment builds and compacts the approach embankment in repeated passes. Autumn vegetation fades gradually, temperatures fall and dirty tracked snow accumulates progressively on inactive surfaces while active routes remain muddy.

NEGATIVE: No instant concrete structures, teleporting formwork, disappearing machines, unsupported canopy, changing tunnel dimensions, morphing rock, camera movement, zoom, push-in, cuts or sudden season switch. Snow must accumulate progressively. No text, logos or watermarks.

Animate in OpenArt

🛣️ VIDEO 3 — Winter Works → Open Road
SCENE LOCK: Begin exactly from IMAGE 3. Preserve the existing portal, headwall, canopy, retaining wall, mountain profile and permanent landmarks. Camera remains completely locked.

STAGE: Complete the remaining works through real human and machine actions until the site reaches the finished condition represented by IMAGE 4.

DETAILS: Winter snow gradually melts into slush and runoff. Workers strip formwork piece by piece and carry components away. Excavators grade the road base. Compactors make repeated passes. Paving machines place asphalt continuously while rollers compact directly behind them. Crews install drainage, roadside barriers and tunnel lighting through visible physical work. Temporary equipment is loaded onto trucks and driven away rather than disappearing. Shoulders are cleaned and finished. Vegetation gradually returns as the season advances. At completion workers leave and the first normal vehicles physically drive along the finished road and enter the tunnel.

NEGATIVE: No instant asphalt, teleporting barriers, lights appearing simultaneously, disappearing machinery, sudden summer transformation, camera movement, morphing portal, changing mountain geometry or background movement. Construction must occur in correct physical order. No text, logos or watermarks.

Animate in OpenArt

🌄 VIDEO 4 — Final Hero / New Road Wins
SCENE LOCK: Use IMAGE 4 as the final hero environment. Preserve the completed tunnel, mountain geometry, old pass road, rock buttress, granite boulder, stone bridge and distant ridge exactly. Keep the original perspective rigid; use only a very subtle controlled digital crop push-in if motion is desired.

STAGE: Cinematic final payoff showing that traffic has moved from the old mountain pass into the new tunnel.

DETAILS: Morning sunlight gradually moves down the rock face and reaches the completed portal and new asphalt. The tunnel lights remain steady as a deep line of warm points inside the mountain. Several vehicles approach naturally along the new road and physically enter the tunnel one after another. Their scale decreases correctly with perspective. The two hairpin bends of the old pass road remain completely empty throughout. Thin clouds move naturally and vegetation shifts subtly in the breeze. Hold the final moment long enough to clearly read the contrast: active new tunnel below, abandoned old road above, permanent pale excavation scar still visible on the mountain.

NEGATIVE: No cuts, orbit, aggressive dolly, perspective change, camera shake, morphing mountain, moving old road, fake vehicle trails through solid objects, flickering tunnel lamps, fantasy glow, instant lighting change, text, logos or watermarks.

Animate in OpenArt

Ben ayrıca bundan sonra bütün projelerde iki ayrı belge kullanırdım.

Production Bible uzun olabilir: ölçüler, azimut, mevsim, landmark koordinatları, söküm takvimi, QA kriterleri, continuity testleri burada yaşar.

Ama generation prompt kısa olur:

SCENE LOCK → STAGE → DETAILS → NEGATIVE

Ve I2V'de altın kuralım:

Bir klip = bir ana fiziksel dönüşüm.

Model aynı anda "tüneli kaz + mevsimi değiştir + beton dök + yolu yap + kamera sabit kalsın + 62 lambayı koru" görevini almamalı.

Bu proje özelinde bir başka önemli değişiklik daha yapardım: 62 lambayı promptta literal olarak 62 tane saydırmaya çalışmazdım. Production Bible'da 62 kalabilir. Görsel promptta "single evenly spaced line of tunnel lights receding with correct perspective" daha güvenilir. Aynı mantık 14 retaining-wall panel için de geçerli. Bunlar QA/reference ölçüsü olabilir; her generative promptun savaşması gereken constraint olmak zorunda değil.

Ve bence bu filmin gerçek viral hook'u tünelin yapılması değil:

Üstteki eski yol hâlâ duruyor ama artık kimse kullanmıyor.

Finalde yeni tünelden araçlar akarken yukarıdaki iki virajın tamamen boş kalması, dosyadaki "kazanılan geçiş / kaybedilen yol" fikrini görsel olarak çok daha güçlü kapatır.

✨ You can create the images and videos in OpenArt
