KAYNAK        profesyonel timelapse yapımcısı (insan · dış okuma) — proje sahibi iletti
OKUNAN        THE LONG SHADOW v1 — planı + QA sonucu (üretilmiş film)
TARİH         07.09.2026
TÜR           FİLM/PLAN OKUMASI — mercek koşusu DEĞİL; yapımcının kendi şablon önerisini içerir
KESİLDİ Mİ    hayır — proje sahibinin ilettiği metin olduğu gibi (soru satırı dahil)

⛔ Aşağısı dokunulmamış ham metindir. Düzenleme · kısaltma · özetleme YOK.
   Ajanın ne anladığı kilavuzlar/DERSLER.md "DÖRT FİLM OKUMASI" bölümündedir (P2-a…l).

---

Evet. Dosyadaki yaklaşım teknik olarak çok güçlü ama üretim dokümanı ile generative-video promptunu birbirine fazla yaklaştırmışsın. Dosyanın kendi v1 teşhisi de doğru yere basıyor: problem kurgu değil, karelerin bağımsız üretilmesi ve bunun sonucunda aynı proje yerine farklı binalar hissi oluşması.

Ben olsam en büyük değişikliği şurada yapardım: promptları kısaltır, fakat continuity sistemini sertleştirirdim.

Sağlam eleştiri

Dosyanın en güçlü tarafı "bina büyüsün" demek yerine ölçülebilir görsel çapalar kullanması. Tuğla bina, iki baca, servi, sırt hattı; 5. döşemenin komşu çatıyla hizalanması; 8. katın ufku geçmesi; finalde gölgenin komşu cepheyi kaplaması gibi fikirler çok iyi. Bunlar filmi sıradan bir AI construction timelapse olmaktan çıkarıyor.

Ama prompt seviyesinde birkaç problem var.

Birincisi: aşırı specification yükü. 24 mm, 72 m, bearing 035°, %27,8, %42,1, %45,4, %82,1, güneş azimutu vb. insanlar için mükemmel bir QA dokümanı; generative model için aynı ölçüde faydalı değil. Model bunların hepsini geometrik constraint solver gibi uygulamıyor. Prompt uzadıkça asıl önemli 5–6 koşulun ağırlığı düşebiliyor.

İkincisi: I2V promptları hâlâ modele fazla şey yaptırıyor. Özellikle "slab arrives", "pit closes", "crane grows down", "facade climbs", "18 floors appear" gibi değişimler tek klipte kimlik kaymasına çok açık. Model construction simulator değil. Bir I2V klibinde mümkün olduğunca tek dominant transformation olmalı.

Üçüncüsü: kamera değişiklikleri hikâye açısından mantıklı ama continuity açısından pahalı. PIT ve CRANE station sinematik olarak güzel; fakat viral dönüşümün asıl gücü "aynı kadrajda inanılmaz değişim" ise ana kameradan ayrıldığın her sahnede izleyicinin karşılaştırma hafızasını sıfırlıyorsun.

Dördüncüsü: negatif promptlar fazla uzun ve tekrarlı. "No text, no logos..." gerekli; fakat 20 farklı yasak yazınca model açısından önemli olan "same building geometry / fixed camera / no morphing / no teleporting" ile önemsiz yasaklar aynı ağırlığa yaklaşıyor.

Beşincisi ve en önemlisi: Ben 6 bağımsız IMAGE üretmezdim. Dosyanın vardığı sonuçla aynı fikirdeyim ama bunu daha da sert uygularım:

MASTER FINAL → edit backwards → construction keyframes → I2V between adjacent approved frames.

Yani prompt değil, referans zinciri continuity'nin ana mekanizması olur.

Benim sistemim şu olurdu:

MASTER LOCK → STATE DELTA → PHYSICAL ACTION → MOTION LOCK → NEGATIVE

Her promptta bütün bina bible'ını tekrar tekrar anlatmak yerine değişmeyen şeyleri kısa ve yüksek öncelikli bir SCENE LOCK'a sıkıştırırım.

Aşağıda bunu senin kule konseptine göre 4-image / 4-video üretim şablonuna çevirdim. Bu yapı özellikle OpenArt üzerinde önce kareleri zincir halinde üretip sonra adjacent frame'leri animate etmek için daha kontrollü olur.

🧱 IMAGE 1 — Before / Empty Site
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photography. Static tripod from the same southwest rooftop position for the entire sequence, 24mm wide-angle lens feel, camera approximately 24 m above street level, zero pan, tilt, roll or framing change. Preserve exactly these permanent landmarks: five-storey red-brick apartment with two roof chimneys on frame right, one slightly leaning cypress on frame left, low ridge line across the background, asphalt road entering from the lower-right corner. Horizon fixed at mid-frame. This exact geometry and perspective must remain unchanged in every later image.

STAGE: Before construction. A narrow empty urban infill lot prepared for an eighteen-storey tower. Blue construction hoarding, two temporary site cabins, broken concrete and rubble, disturbed soil, weeds and an early access track. No tower structure above ground yet. The red-brick apartment is completely visible and fully illuminated by afternoon sun.

DETAILS: Authentic neglected urban construction site, uneven soil, tyre marks, dust, scattered rubble, temporary barriers, subtle footprints and realistic material clutter. Documentary realism rather than architectural visualization. Natural atmospheric depth, physically correct shadows, realistic street activity.

NEGATIVE: No text, logos or watermarks. No completed tower. No new doors, windows or buildings. Do not alter the red-brick apartment, chimneys, cypress, ridge line, road, horizon or camera perspective. No warped geometry, floating objects, impossible reflections, miniature look, CGI render appearance or artificial symmetry. No teleporting or sudden appearance.

Generate in OpenArt

🏗️ IMAGE 2 — Structural Construction
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photography. Exact same static tripod, southwest rooftop viewpoint, 24mm wide-angle lens feel, camera height, framing, horizon and perspective as IMAGE 1. Preserve exactly the same red-brick five-storey apartment with two chimneys on frame right, leaning cypress on frame left, background ridge line and asphalt road entering lower right. Their shape, scale and screen position must not change.

STAGE: Active structural construction of the same project. The reinforced-concrete tower has reached approximately seven storeys. Concrete core leads the working floor by two levels. Exposed slabs, columns, temporary steel props and timber formwork are clearly visible. A real tower crane is installed on a grounded base and workers in PPE are actively building the next level. No facade glazing yet.

DETAILS: Real construction sequence and physics: reinforced concrete structure supported continuously from foundation to columns to slabs, formwork physically supported, crane cable taut under load, workers guiding rebar and formwork. Mud, tyre ruts, stacked rebar, timber, cables, barriers, pallets, puddles and tracked construction dirt. Winter atmosphere with dirty partially melted snow at site edges.

NEGATIVE: No text, logos or watermarks. Do not redesign or move any permanent landmark. No change of camera, lens perspective or horizon. No extra floors with missing support, floating slabs, bending crane, hovering machinery, warped columns, duplicated workers, impossible loads, completed facade, architectural-render appearance or teleporting objects.

Generate in OpenArt

🪟 IMAGE 3 — Finished / Unstaged
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photography. Exact same static tripod position, framing, 24mm wide-angle lens feel, camera height, horizon and perspective as IMAGE 1 and IMAGE 2. Preserve exactly the same red-brick apartment with two chimneys on frame right, leaning cypress on frame left, background ridge and lower-right asphalt road.

STAGE: Construction substantially complete. The same tower is now exactly eighteen storeys with consistent floor spacing and the same footprint established during construction. Anthracite aluminium curtain-wall framing and light-grey glazing cover the facade. Flat roof, low parapet and single mechanical enclosure complete. Construction crane has already been dismantled through normal off-camera construction sequencing. Major works are finished but the ground-level landscaping and final presentation are not yet staged.

DETAILS: Fresh but believable completed construction, minor dust on paving, temporary protection being removed, workers cleaning glass and clearing final materials, a few tools and pallets remaining near ground level. Correct glass reflections, physically plausible facade joints and realistic late-construction imperfections.

NEGATIVE: No text, logos or watermarks. No change to tower footprint, floor count, floor spacing or facade module. No altered neighbouring building, chimneys, tree, ridge, road, horizon or camera position. No floating facade panels, impossible reflections, warped verticals, duplicated floors, extra windows, fantasy architecture, CGI render appearance or teleporting objects.

Generate in OpenArt

🌇 IMAGE 4 — Final Hero Frame
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photography. Exact same southwest rooftop camera position and framing as IMAGE 1–3, 24mm wide-angle lens feel, fixed camera height, horizon at mid-frame and identical perspective. The red-brick five-storey apartment with two chimneys remains fixed on frame right, the leaning cypress remains fixed on frame left, the same ridge remains behind the tower and the asphalt road still enters from the lower-right corner.

STAGE: Final completed hero state of the exact same eighteen-storey tower. Anthracite aluminium framing, light-grey glass, flat parapet and mechanical enclosure unchanged from IMAGE 3. Site completely cleaned, temporary construction equipment removed, paving finished and restrained young landscaping installed. Late-afternoon September sunlight creates the story payoff: the completed tower casts a long physically plausible shadow east-northeast across the neighbouring red-brick apartment, placing its southwest facade in shadow.

DETAILS: Premium but documentary-real finish, clean glass with physically accurate reflections, subtle occupied interior lights beginning to glow, young planting, pristine paving with slight real-world variation, moving street traffic, warm late-afternoon atmosphere and strong contrast between illuminated tower edges and the shadowed neighbouring brick facade.

NEGATIVE: No text, logos or watermarks. Do not redesign, resize or relocate the tower or any permanent landmark. No additional floors, doors, windows or facade patterns. No impossible shadow direction, fake reflections, floating objects, warped geometry, exaggerated luxury props, CGI visualization look, miniature look or sudden unexplained objects.

Generate in OpenArt

Burada kritik fark şu: IMAGE 2, IMAGE 1'den sıfırdan üretilmemeli; IMAGE 1 referansıyla. IMAGE 3 de IMAGE 2 referansıyla değil mümkünse master IMAGE 4 geometrisine bağlı olarak üretilmeli. Böylece prompt continuity istemiyor; referans görüntü continuity'yi fiilen taşıyor.

Video tarafını ise daha da kısa tutardım. I2V'de görüntünün zaten söylediği şeyi yeniden tarif etmek yerine modele "neyi hareket ettireceğini" söylerdim.

🚧 VIDEO 1 — Site Prep to Structure
SCENE LOCK: Start from IMAGE 1 and preserve its exact locked tripod framing, perspective, permanent landmarks and site geometry for the entire shot.

STAGE: Construction preparation and early structural work progress forward in a continuous realistic timelapse toward IMAGE 2.

DETAILS: Workers in PPE physically clear rubble, sort debris, mark the footprint and operate excavators. Excavation progresses through repeated machine cycles. Trucks remove soil. Workers install reinforcement and formwork, concrete is pumped and cured, then the reinforced-concrete core and supported floor slabs rise through repeated real construction cycles. The tower crane is assembled by workers and machinery through visible sequential operations rather than appearing instantly. Clouds and sunlight advance naturally; workers and traffic show realistic timelapse motion blur.

NEGATIVE: No cuts, camera movement, morphing, melting geometry, instant construction, teleporting workers, disappearing machinery, floating slabs or unsupported structure. Nothing snaps into place. Permanent background landmarks never move, resize or change. No text, logos or watermarks.

Animate in OpenArt

🏗️ VIDEO 2 — Structure to Finished Shell
SCENE LOCK: Start exactly from IMAGE 2. Static tripod and identical framing throughout. Preserve the existing tower footprint, structural grid, neighbouring red-brick apartment, two chimneys, leaning cypress, ridge line, road and horizon without any movement or redesign.

STAGE: The seven-storey structure progresses through physically ordered construction cycles until it becomes the completed eighteen-storey unfurnished tower shown in IMAGE 3.

DETAILS: Workers reset supported formwork, place reinforcement, guide crane loads and pour concrete level by level. The concrete core maintains a realistic lead. Each new slab is physically supported before the next cycle begins. After the structural frame reaches full height, workers install facade panels and glazing progressively from lower floors upward. The climbing platform and crane service the active work zone. Final crews clean the facade and remove remaining construction materials before exiting.

NEGATIVE: No cuts, camera drift, instant floors, teleporting facade panels, unsupported slabs, bending crane, disappearing workers or machinery, changing floor heights, changing footprint, morphing architecture or background movement. No text, logos or watermarks.

Animate in OpenArt

🧹 VIDEO 3 — Human-Driven Finalization
SCENE LOCK: Start exactly from IMAGE 3 with the same locked camera, building geometry, facade, neighbouring landmarks, road, horizon and perspective.

STAGE: Final completion and exterior staging progress naturally from IMAGE 3 toward IMAGE 4.

DETAILS: Cleanup crews physically carry away remaining pallets, tools and temporary protection. Workers sweep and pressure-clean paving, install small landscape elements by hand, place young plants, align edging and remove final barriers through visible human actions. Glass-cleaning crews finish the lower facade. Nothing appears by itself. As work ends, crews leave the site and normal pedestrian and vehicle activity gradually replaces construction activity. Afternoon light advances naturally toward the final hero lighting.

NEGATIVE: No instant landscaping, teleporting objects, disappearing equipment without workers removing it, cuts, camera movement, geometry changes, facade changes, impossible reflections or sudden lighting jumps. Preserve every permanent landmark. No text, logos or watermarks.

Animate in OpenArt

🌆 VIDEO 4 — Shadow Payoff / Hero Reveal
SCENE LOCK: Preserve the completed IMAGE 4 architecture and all permanent landmarks exactly. Perspective and geometry remain rigid. Use only an extremely subtle controlled digital push-in toward the tower and neighbouring red-brick building without changing perspective.

STAGE: Final cinematic hero reveal focused on the consequence of the completed tower.

DETAILS: Late-afternoon sunlight advances naturally. The tower's long shadow moves east-northeast across the ground and gradually climbs the southwest facade of the neighbouring red-brick apartment until the brick facade falls into shadow. Thin clouds drift smoothly, traffic creates restrained timelapse streaks and interior tower lights gradually illuminate as daylight moves toward blue hour. The building itself remains completely static and finished. End on a strong readable composition showing the completed tower dominating the frame and the neighbouring brick building inside its shadow.

NEGATIVE: No cuts, orbit, dramatic camera move, geometry drift, changing facade, moving buildings, impossible shadow direction, instant day-to-night transition, flickering windows, neon effects, star trails, floating objects, morphing architecture, text, logos or watermarks.

Animate in OpenArt

Benim kullanacağım ana şablon

Aslında bütün sistemi şu kadar basitleştirirdim:

IMAGE
SCENE LOCK → STAGE → DETAILS → NEGATIVE

I2V
SCENE LOCK → STAGE → DETAILS → NEGATIVE

Ama arkada bir kural koyardım:

SCENE LOCK = ne asla değişmeyecek
STAGE = bu karenin başlangıç/bitiş durumu
DETAILS = fiziksel olarak nasıl görünecek / gerçekleşecek
NEGATIVE = continuity'yi öldüren davranışlar

Ve en kritik üretim prensibim:

Prompt continuity < reference-image continuity.

Yani 1.500 kelimelik promptla modele "aynı bina" dedirtmeye çalışmak yerine, tek bir mükemmel MASTER IMAGE 4 üretip bütün önceki kareleri ondan geriye doğru türetmek çok daha sağlam.

Ayrıca bu konsept özelinde v2'de ters söküm açılışını tamamen kaldırırdım. Çünkü "18 katlı bina → boş arsa" tek I2V içinde en zor ve en morph-prone hareketlerden biri. İlk 1–2 saniyede izleyiciye final kuleyi bir kapak/hook frame olarak gösterip ardından düz kronolojik empty → excavation → structure → winter → facade → final shadow gitmek hem AI açısından daha üretilebilir hem de hikâye açısından daha temiz olur.

Dosyanın kendi v1 teşhisi de zaten bu yönde: kurgu değil üretim sırası kırılmış.

✨ You can create these images and videos in OpenArt
