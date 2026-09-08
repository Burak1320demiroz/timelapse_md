KAYNAK        profesyonel timelapse yapımcısı (insan · dış okuma) — proje sahibi iletti
OKUNAN        THE NARROW LOT — planı + QA sonucu (üretilmiş film)
TARİH         07.09.2026
TÜR           FİLM/PLAN OKUMASI — mercek koşusu DEĞİL; yapımcının kendi şablon önerisini içerir
KESİLDİ Mİ    hayır — proje sahibinin ilettiği metin olduğu gibi (soru satırı dahil)

⛔ Aşağısı dokunulmamış ham metindir. Düzenleme · kısaltma · özetleme YOK.
   Ajanın ne anladığı kilavuzlar/DERSLER.md "DÖRT FİLM OKUMASI" bölümündedir (P2-a…l).

---

Yapıştırılan markdown.md
Dosya
bu video iicin sağlam bir eleştiri yaparmısın ve sen olsan nasıl yaparın nasıl bir şablon kullanırıdın iamge ve image to video promtları icin 

Evet. Bu dosyada The Narrow Lot için temel yaklaşım doğru ama prompt sistemi fazla "spesifikasyon belgesi", yeterince "generative control prompt" değil. QA sonuçları da bunu doğruluyor: timelapse, same-world, zaman yayı ve mevsim taşıyıcısı çalışmış; buna karşılık yapı kimliği, time-rate/gökyüzü-gölge hareketi, cover ve ritim tarafında sorunlar kalmış.

Ben en büyük değişikliği şurada yapardım: 5 bağımsız sahne üretmek yerine 4 güçlü checkpoint üretip her yeni image'i bir önceki onaylı kareden edit/reference zinciriyle türetirdim. Böylece "aynı bina mı?" problemi promptla çözülmeye çalışılmaz; görüntünün kendisi continuity taşıyıcısı olur.

Ayrıca 58.7 metre, 3.15 metre, 18 kat, exactly three chimneys, exactly five windows gibi bilgiler production bible'da kalabilir; fakat modelin görüntüyü üretmesi için sadece görsel olarak ayırt edici olanları prompta taşırdım.

Benim şablonum şu:

IMAGE: SCENE LOCK → STAGE → DETAILS → NEGATIVE

I2V: SCENE LOCK → STAGE → DETAILS → NEGATIVE

Ama işlevleri farklı: IMAGE "bu anda dünya nasıl görünüyor?", VIDEO ise "bu dünyada hangi fiziksel işlemler gerçekleşiyor?" sorusunu cevaplar.

🏚️ IMAGE 1 — Demolition Lot / Before
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photograph. Static tripod permanently fixed on the same neighbouring rooftop, natural 24mm wide-angle lens feel, approximately 24 metres above street level. Identical framing, perspective, horizon and lens distortion for every stage. Preserve four permanent visual anchors exactly: the dark-red six-storey brick apartment building with three rooftop chimneys on frame right, the pale four-storey stone building on frame left, the narrow street frontage below, and the distinctive tree-covered ridge silhouette behind the site. The future tower footprint remains fixed in the exact centre of the narrow lot.

STAGE: Before major construction. A narrow urban demolition lot between the same neighbouring buildings. Broken concrete slabs, exposed soil, old foundation fragments and rubble cover the site. One tracked excavator has started the first excavation cut at the centre of the future tower footprint. No foundation slab, concrete core, structural floors, tower crane or new building exists yet.

DETAILS: Workers in realistic PPE physically guide excavation and truck movement. Excavator tracks press into compacted soil, its bucket is physically connected to the hydraulic arm and carries real excavated material. One dump truck waits in the narrow access lane. Broken concrete, dust, muddy tyre marks, footprints, puddles, cables, hoses, timber scraps and temporary barriers create an untidy working site. Summer daylight, natural shadows, realistic urban atmosphere, documentary photography rather than architectural visualization.

NEGATIVE: No text, logos or watermarks. No camera movement, push-in, zoom, pan, tilt, orbit or changed perspective. Do not move, resize, redesign or replace either neighbouring building, the three chimneys, street frontage or ridge silhouette. No tower yet, no foundation yet, no crane yet. No floating equipment, warped architecture, melting geometry, duplicated buildings, impossible shadows, teleporting objects, sterile CGI render or miniature appearance.

Generate in OpenArt

🏗️ IMAGE 2 — Foundation + Early Structure
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photograph. Exact same static rooftop tripod position, 24mm lens feel, framing, perspective, horizon and lens distortion as IMAGE 1. Preserve exactly the same dark-red six-storey brick apartment with three rooftop chimneys on frame right, pale four-storey stone building on frame left, narrow street frontage and distant tree-covered ridge. The new building footprint must occupy exactly the same position established by IMAGE 1.

STAGE: Active structural construction in autumn. The excavation has become a completed reinforced-concrete foundation and ground-level podium. A narrow central reinforced-concrete core now rises from the same footprint and the first three structural floor slabs are complete around it. One grey flat-top tower crane stands on a physically grounded base within the site. Workers are preparing formwork and reinforcement for the next structural level. The final facade does not exist yet.

DETAILS: Real reinforcement cages, slab-edge formwork, temporary guardrails, concrete pump hoses, material pallets, cables and wet construction surfaces. Workers in PPE physically align reinforcement and formwork. Crane hook carries one visible material load on a taut vertical cable. Autumn leaves, damp pavement, puddles, muddy vehicle tracks and realistic concrete staining. Every structural slab has visible support beneath it.

NEGATIVE: No text, logos or watermarks. No camera drift, push-in, zoom or perspective change. Permanent background anchors remain identical to IMAGE 1. Do not change the building footprint, core position or structural bay rhythm. No completed tower, no finished facade, no floating slabs, disconnected crane cable, impossible crane geometry, unsupported concrete, instant construction, duplicated floors, warped neighbouring buildings or CGI appearance.

Generate in OpenArt

❄️ IMAGE 3 — Full Structural Frame
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photograph. Exact same locked rooftop tripod, 24mm lens feel, framing, perspective and horizon as IMAGE 1 and IMAGE 2. Preserve exactly the same neighbouring brick building with three chimneys, pale stone building, street frontage and distant ridge. Preserve the exact footprint, width, core position and vertical proportions established by IMAGE 2.

STAGE: Late-winter construction. The same reinforced-concrete tower has now reached its full eighteen-storey structural height. The narrow rectangular frame and central core are complete. The same grey flat-top tower crane remains grounded in the same site position. Only part of the facade is installed: one coherent vertical section has charcoal-grey horizontal bands, warm pale-stone vertical panels and floor-to-ceiling glazing while large areas of the concrete frame remain exposed. Workers actively install facade components.

DETAILS: Dirty melting snow and grey slush remain around site edges, with wet black mud and puddles along active routes. Facade panel crates, temporary access equipment, sealant tools, cables and construction waste remain visible. Workers physically receive suspended facade panels, align them against existing supports and mechanically fasten them. Crane cable remains taut and the suspended load follows a plausible lifting path. Real winter daylight and wet concrete reflections.

NEGATIVE: No text, logos or watermarks. No camera movement, push-in, zoom, reframing or perspective change. Do not alter the established tower width, floor rhythm, core or neighbouring buildings. No instant complete facade, no disappearing crane, floating panels, empty disconnected hook, unsupported floors, changing floor count, duplicated windows, melting architecture, sudden summer vegetation, teleporting workers or polished architectural-render appearance.

Generate in OpenArt

🌆 IMAGE 4 — Final Master Tower
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photograph. Final master continuity frame from the exact same static rooftop tripod, same 24mm lens feel, framing, perspective, horizon and lens distortion as every previous stage. Preserve exactly the dark-red six-storey brick apartment with three rooftop chimneys on frame right, pale four-storey stone building on frame left, narrow street frontage and distant tree-covered ridge. Preserve exactly the tower footprint, width, height, core position and floor rhythm established during construction.

STAGE: Final completed eighteen-storey narrow residential tower in summer. The same structural frame is now fully enclosed. Restrained contemporary facade with charcoal-grey horizontal metal bands, warm pale-stone vertical elements and consistent floor-to-ceiling glazing follows the exact existing structural grid. The flat crown is complete. Tower crane, formwork, temporary access systems and major material stacks have been physically removed. The ground-level entrance and forecourt are complete but restrained and realistic.

DETAILS: Natural inhabited urban environment rather than a sterile luxury render. Realistic glass reflections, slight pavement dirt, drainage details, subtle tyre marks, a few pedestrians and restrained landscaping. Summer foliage has returned to the distant ridge. Natural afternoon daylight creates physically consistent shadows across the completed facade. The neighbouring buildings remain visually unchanged, emphasizing how the new narrow tower has grown between them.

NEGATIVE: No text, logos or watermarks. No changed camera position or perspective. No additional floors, balconies, doors or windows beyond the established architecture. Do not redesign neighbouring buildings or ridge. No crane, scaffolding or construction equipment remaining. No impossible glass reflections, warped facade grid, duplicated windows, floating landscaping, excessive luxury decoration, fantasy lighting, CGI render appearance or architectural geometry changes.

Generate in OpenArt

Şimdi asıl önemli kısım: I2V promptlarında modeli mimar olmaktan çıkarıp şantiye işçisi yapıyorum. Kaynak image geometrinin ne olduğunu zaten söylüyor. Video promptu tekrar "18 floors, 58.7m..." anlatmamalı; hangi hareketin nasıl gerçekleşeceğini anlatmalı.

⛏️ VIDEO 1 — Excavation → Foundation
SCENE LOCK: Begin exactly from IMAGE 1. Preserve the source-image composition, neighbouring buildings, street frontage and ridge pixel-stably throughout. Static tripod with absolutely no push-in, zoom, pan, tilt, orbit, shake, drift or automatic cinematic camera motion.

STAGE: Progress naturally from demolition-site excavation toward the foundation condition required for IMAGE 2. Construction happens through repeated physical operations rather than instant transformation.

DETAILS: The excavator performs repeated mechanically correct digging cycles: boom lowers, bucket enters soil, bucket curls, lifts excavated material, rotates and empties into waiting dump trucks. Trucks physically enter, receive material and leave. Workers clear debris and prepare the excavation. After excavation progresses, crews physically place reinforcement and assemble formwork in visible sequential operations. Concrete arrives through real equipment and gradually fills prepared areas under gravity. Dust rises and settles, workers move as accelerated human motion and clouds and shadows move continuously through the timelapse.

NEGATIVE: No cuts, camera movement, push-in, zoom, instant foundation, teleporting concrete, disappearing rubble, floating equipment, morphing neighbouring buildings, changing street geometry, unsupported structures or objects snapping into place. No text, logos or watermarks.

Animate in OpenArt

🏗️ VIDEO 2 — Foundation → Tower Frame
SCENE LOCK: Begin exactly from IMAGE 2. Preserve the existing foundation, tower footprint, central core, neighbouring buildings and background geometry. Camera remains completely locked with identical perspective throughout.

STAGE: The reinforced-concrete tower grows upward through believable repetitive construction cycles toward the full structural-frame condition of IMAGE 3.

DETAILS: Workers assemble reinforcement, position supported formwork and prepare one floor zone at a time. The tower crane physically lifts formwork and reinforcement bundles on a taut cable. Workers receive each load before it is released. Concrete is pumped into prepared supported forms. After curing is implied, formwork is stripped and moved upward for the next cycle. The central core and structural slabs rise progressively through repeated cycles; upper floors never appear before supporting structure exists beneath them. Winter weather gradually develops during the passage of construction time, with dirty snow accumulating on inactive surfaces while active working areas remain disturbed and muddy.

NEGATIVE: No instant stack of floors, no tower stretching upward like an extrusion, no teleporting slabs, no unsupported floors, no floating crane, disconnected cable, changing crane type, morphing footprint, camera movement, sudden snow switch, duplicated structural bays or geometry breathing. No text, logos or watermarks.

Animate in OpenArt

🪟 VIDEO 3 — Structure → Finished Facade
SCENE LOCK: Begin exactly from IMAGE 3. Preserve the completed structural frame, floor rhythm, central core, neighbouring buildings and skyline. Static tripod remains absolutely locked.

STAGE: Complete the existing tower through real facade installation, temporary-equipment removal and ground-level finishing until it reaches IMAGE 4.

DETAILS: Crane-supported facade panels arrive one load at a time. Workers physically receive each panel, rotate it into alignment, position it against existing structural supports and mechanically fasten it before the crane releases tension. Glazing and facade sections advance progressively across the existing frame rather than appearing simultaneously. Temporary access equipment is dismantled section by section. The tower crane is dismantled through visible sequential removal of components and equipment is transported away. Workers clean the forecourt, finish paving and remove remaining materials. Dirty late-winter snow gradually melts into runoff, vegetation returns gradually and summer conditions emerge only after construction progresses.

NEGATIVE: No instant full facade, no windows appearing simultaneously, no teleporting panels, no disappearing crane, no instant cleanup, no sudden landscaping, no instant season change, no floating workers, no facade changing the structural grid, no camera movement, push-in, zoom or geometry warping. No text, logos or watermarks.

Animate in OpenArt

✨ VIDEO 4 — Final Hero Reveal
SCENE LOCK: Use IMAGE 4 as the completed hero environment. Preserve the finished tower, neighbouring buildings, street and ridge exactly. Maintain the original perspective and geometry. For the hero reveal only, use a very subtle controlled digital crop push-in toward the tower while keeping all architectural lines stable.

STAGE: Cinematic final payoff of the completed narrow tower occupying the same constrained lot seen at the beginning.

DETAILS: Afternoon sunlight moves gradually across the finished facade, creating changing highlights on the glazing while reflections remain physically consistent. Thin clouds move smoothly across the sky. A few pedestrians naturally cross the completed forecourt and occasional street vehicles pass through the existing road without dominating the frame. Interior lights activate gradually in a small number of already existing windows toward the end. The tower itself remains completely static and architecturally unchanged. Finish with a clean hero hold emphasizing the dramatic vertical transformation between the two unchanged neighbouring buildings.

NEGATIVE: No aggressive dolly, orbit, parallax shift, camera shake, architectural morphing, new windows, changing floor count, bending facade lines, impossible reflections, flickering entire building, teleporting pedestrians, suddenly appearing furniture, fantasy lighting, text, logos or watermarks.

Animate in OpenArt

Ben olsam üretim sistemini de değiştirirdim

Dosyanın en önemli bulgularından biri SAME WORLD testinin geçmiş olması; yani mevcut yaklaşım tamamen çöpe atılacak durumda değil. Buna karşılık yapı kimliği hâlâ yalnız 2.6/10, time-rate problemi var ve eşit 6 saniyelik yapı METRONOM hissi üretmiş.

Bu yüzden yeni sistemimde prompt değil, keyframe zinciri ana omurga olurdu:

IMAGE 4 MASTER
↓ remove facade / restore construction equipment
IMAGE 3
↓ remove upper floors
IMAGE 2
↓ remove structure / restore demolition site
IMAGE 1

Sonra ters yönde animate:

IMAGE 1 → VIDEO 1 → IMAGE 2 → VIDEO 2 → IMAGE 3 → VIDEO 3 → IMAGE 4 → VIDEO 4 HERO

Böylece her I2V klibinin ulaşacağı somut bir sonraki kare var.

Ve en önemli değişiklik: 6 + 6 + 6 + 6 gibi metronom kurgu yapmazdım. Örneğin final editte yaklaşık 4.5s excavation → 7s structure rise → 5.5s facade → 7s final transformation/cleanup → hero hold gibi görsel değişimin büyüklüğüne göre süre dağıtırdım.

Bence burada asıl sıçrama promptu 3 kat uzatmak değil; promptun sorumluluğunu azaltıp reference-image zincirinin sorumluluğunu artırmak. Bu yaklaşım özellikle bina timelapse'larında "başka bina çıktı / pencere sayısı değişti / kamera yaklaştı / vinç mutasyona uğradı" problemlerini ciddi biçimde azaltır.

✨ You can create the images and videos in OpenArt
