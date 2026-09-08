KAYNAK        profesyonel timelapse yapımcısı (insan · dış okuma) — proje sahibi iletti
OKUNAN        THE CLOSING SPAN — planı + QA sonucu (üretilmiş film)
TARİH         07.09.2026
TÜR           FİLM/PLAN OKUMASI — mercek koşusu DEĞİL; yapımcının kendi şablon önerisini içerir
KESİLDİ Mİ    hayır — proje sahibinin ilettiği metin olduğu gibi (soru satırı dahil)

⛔ Aşağısı dokunulmamış ham metindir. Düzenleme · kısaltma · özetleme YOK.
   Ajanın ne anladığı kilavuzlar/DERSLER.md "DÖRT FİLM OKUMASI" bölümündedir (P2-a…l).

---

Yapıştırılan markdown.md
Dosya
bu video iicin sağlam bir eleştiri yaparmısın ve sen olsan nasıl yaparın nasıl bir şablon kullanırıdın iamge ve image to video promtları icin 

Evet. Bu kez dosyanın tamamındaki mantığı ve QA sonucunu dikkate alarak söyleyeyim: THE CLOSING SPAN'ın fikri çok güçlü, ama v1 üretim sistemi fikrin gücünü görüntüye taşıyamamış. Dosyanın kendi ölçümünde camera lock 10/10'a çıkmış; buna rağmen ayrı görüntüler, farklı appearing, yanlış yönde geçiş, her çekimde yeniden kurulmuş dünya ve metronom problemi yüzünden beş hüküm düşmüş. En kritik veri de 9/9 dikişin defect olması.

Bence burada sorun "promptlar yeterince detaylı değil" değil. Tam tersi: promptlar fazla detaylı, fakat üretim zinciri yeterince sert değil.

En büyük problem: prompt mimariyi tarif ediyor, ama referans görüntü mimariyi yönetmiyor

Her IMAGE promptunda 640 m, 400 m açıklık, 22 m tabliye, 22 kablo, 12 m aralık, pylon yüksekliği, kamera koordinatları vs. tekrar ediliyor. Bunlar mükemmel bir production bible, fakat image model için her sahnede yeniden yorumlanabilecek talimatlar.

Sonuçta model şunu yapıyor:

"Tamam, yine cable-stayed bridge üreteyim."

Bizim istediğimiz ise:

"Hayır. Bir önceki görüntüdeki aynı köprüye yalnızca şu parçayı ekle."

Bu ikisi çok farklı.

Dosyanın kendisinin belirlediği ters zincir — S9 → S8 → S7 → ... → S0 — aslında doğru çözüm. Problem bunun v1'de uygulanmamış olması.

İkinci problem: 10 × 6 saniye matematiksel olarak temiz, izleyici açısından fazla temiz

Dosya bunu çok doğru teşhis etmiş:

"Hız kesme sıklığı değil, kesme varyansıdır."

10 sahnenin hepsi yaklaşık altı saniye olunca izleyici birkaç sahneden sonra videonun ritmini çözüyor:

değişim → cut → değişim → cut → değişim → cut

Köprünün ortada birleşmesi filmin doruk noktası olması gerekirken yalnızca "sıradaki altı saniyelik blok" haline geliyor.

Ben örneğin ritmi:

4s → 3s → 5s → 4s → 7s → 5s → 4s → 8s → 10s → 7s

gibi kurardım.

Özellikle son 20 metre açıklığın kapanmasını diğer aşamalardan daha uzun izletirdim.

Üçüncü problem: iki kamera mantıklı ama viral transformation açısından pahalı

MAIN → PYLON → MAIN → MAIN → PYLON → MAIN...

Mühendislik belgeseli açısından güzel. Fakat transformation videosunda izleyicinin beyninde çalışan şey:

"Az önce burada ne vardı?"

Kamera değiştiğinde o karşılaştırma belleğini sıfırlıyoruz.

Ben ana transformation'ın %85–90'ını tek MAIN STATION üzerinden yapardım. Pylon station görüntülerini ana timeline'ın aşaması değil, 1–2 saniyelik detail insert olarak kullanırdım.

Ve köprü birleşirken kesinlikle kamera değiştirmezdim.

Çünkü filmin kahramanı aslında köprü değil:

BOŞLUK.

400 m → 260 m → 150 m → 20 m → 0 m

Dosyanın en güçlü yaratıcı fikri bu.

Dördüncü problem: I2V'ye fazla uzun zaman yükleniyor

"Four months pass" veya "five months pass" güzel bir anlatı cümlesi ama model açısından fazla soyut.

I2V'nin görevi:

34 aylık projeyi anlamak değil.

Görevi:

A görüntüsünden B görüntüsüne fiziksel olarak ikna edici hareket üretmek.

Bu yüzden I2V promptlarında takvimden çok şu mantığı kullanırım:

SOURCE STATE → ONE DOMINANT OPERATION → PHYSICAL MOTION → TARGET STATE

Örneğin:

"4 ay geçiyor, köprü ilerliyor"

yerine:

"form traveller moves onto the last completed segment → workers secure it → next deck segment is assembled → next stay cable is tensioned → repeat."

Çok daha kontrol edilebilir.

🧠 Benim kullanacağım sistem

Production Bible ayrı tutulur:

WORLD LOCK

kamera
arazi
4 anchor
bridge identity
pylon identity
deck cross-section
cable pattern

Prompt içine ise yalnız gereken bölüm girer.

Ve dört MASTER CHECKPOINT üretirim:

IMAGE 4 — FINAL MASTER
↓ bridge'i fiziksel olarak geriye edit et
IMAGE 3 — 20 m GAP
↓ cantilever'ları kısalt
IMAGE 2 — EARLY CANTILEVER
↓ deck'i kaldır, pylonları indir
IMAGE 1 — EMPTY GORGE

Yani dört ayrı generation değil.

Bir görüntünün dört tarihsel versiyonu.

Bu ayrım çok önemli.

🖼️ IMAGE PROMPT ŞABLONUM

IMAGE promptunun görevi hareket anlatmak değil; tek bir kusursuz checkpoint oluşturmak.

🌄 IMAGE 1 — Empty Gorge
SCENE LOCK: Vertical 9:16 photorealistic documentary construction photograph. Static tripod permanently fixed on the bridge centreline from the same near-rim rock outcrop, natural 24mm wide-angle lens feel. Identical framing, perspective, horizon and lens distortion throughout the entire project. Preserve four permanent landmarks exactly: the deeply notched rock buttress on frame right, the cluster of three dark pine trees on the far rim, the twin-summit ridge with the left summit higher, and the old switchback road descending to the small stone bridge on the gorge floor.

STAGE: Initial construction state. The mountain gorge is completely open with no bridge spanning it. Only the first foundation excavation activity has begun on the near rim. One excavator works in a fresh rock cut while the opposite rim remains untouched. The full four-hundred-metre central void is visually dominant.

DETAILS: Real mountain construction environment, exposed fractured rock, excavator tracks, spoil piles at natural angles, dust, temporary barriers, hoses, stacked pipe and workers in realistic PPE. Machines remain grounded. Summer daylight and physically consistent shadows. The old road at the bottom of the gorge remains active and visible.

NEGATIVE: No text, logos or watermarks. No bridge deck, pylons or stay cables yet. No camera movement or changed perspective. Do not alter the notched rock buttress, three pine trees, twin-summit ridge or old road. No floating machinery, warped terrain, duplicated mountains, impossible shadows, architectural render appearance or teleporting construction.

Generate in OpenArt

🏗️ IMAGE 2 — Pylons + Early Cantilever
SCENE LOCK: Use IMAGE 1 as the same physical world and exact camera reference. Preserve the identical static tripod position, 24mm lens feel, framing, horizon, terrain geometry and four permanent landmarks. Preserve the exact gorge width and bridge centreline established by IMAGE 1.

STAGE: Structural construction is underway. Two matching pale-grey concrete pylons now rise from physically grounded foundation benches on opposite rims. Short balanced cantilever deck arms extend from each pylon toward the centre of the gorge. The two sides remain separated by a very large open-air gap. Steel form travellers stand only on the outer ends of completed deck segments. Several white stay cables connect each completed cantilever section back to its own pylon.

DETAILS: Workers in PPE physically operate on supported working platforms. Deck segments connect continuously back to their pylons. Stay cables are taut and mechanically connected at both ends. Construction equipment, stacked materials, muddy access routes and temporary works remain visible. Early winter conditions begin with dirty tracked snow only on inactive surfaces.

NEGATIVE: No text, logos or watermarks. Do not redesign the pylons, gorge, bridge axis or background. No complete bridge, no centre closure segment, no unsupported deck, floating form traveller, disconnected stay cable, symmetrical fantasy architecture, duplicated cables, warped mountains, camera movement or instant construction.

Generate in OpenArt

🌉 IMAGE 3 — The Final 20-Metre Gap
SCENE LOCK: Use IMAGE 2 as the direct structural and camera reference. Preserve exactly the same static tripod, 24mm lens feel, gorge, pylons, deck width, cable system, terrain and four permanent landmarks. Existing bridge components must retain their exact geometry and position.

STAGE: Near-complete balanced-cantilever construction. Both deck arms have advanced far into the gorge through repeated supported construction cycles. Only a narrow approximately twenty-metre opening remains at mid-span. The two deck tips face each other at the same elevation and alignment but remain visibly separated by open air. The closure segment has not yet been installed.

DETAILS: The narrow central gap is the hero evidence. Stay cables form consistent fan patterns from both pylons to their respective deck arms. Form travellers remain positioned at the two outer deck tips. Workers and equipment are small but physically grounded. Late-spring conditions, melting residual snow at high shaded areas, wet rock, realistic atmospheric depth and construction clutter.

NEGATIVE: No text, logos or watermarks. Do not close the centre gap. No bridge redesign, changed pylons, changed deck thickness, random cable pattern, floating segment, unsupported deck, mismatched deck elevations, warped terrain, camera drift, zoom, altered background or architectural render appearance.

Generate in OpenArt

✨ IMAGE 4 — Final Master / Closed Span
SCENE LOCK: Final master continuity frame. Preserve exactly the same static tripod, 24mm lens feel, framing, horizon, gorge geometry, pylons, deck width and four permanent landmarks established by all previous images. This image defines the canonical final bridge identity for every other stage.

STAGE: The same cable-stayed bridge is fully completed. The two balanced cantilever arms meet precisely at mid-span through one structurally continuous closure zone. The roadway surface, barriers and restrained lighting infrastructure are complete. Temporary form travellers, construction cranes, work platforms, containers and major construction equipment have already been physically removed between stages.

DETAILS: Late-summer afternoon progressing toward evening. Realistic finished asphalt and barriers, subtle construction residue rather than sterile perfection, physically consistent white stay cables and natural concrete texture. Traffic now crosses high above the gorge. The old switchback road remains physically unchanged below but carries very little traffic. The bridge carries the dominant stream of vehicle lights as dusk approaches.

NEGATIVE: No text, logos or watermarks. No changed bridge geometry, additional pylons, extra cables, altered gorge, altered mountains or changed camera perspective. No construction equipment remaining. No impossible reflections, floating vehicles, fantasy illumination, excessive architectural visualization polish, geometry warping or duplicated structures.

Generate in OpenArt

🎥 I2V ŞABLONUM

Burada kritik fark şu:

IMAGE prompt = noun-heavy.
Ne var?

I2V prompt = verb-heavy.
Ne yapılıyor?

Ve her klibe mümkünse tek dominant construction operation veriyorum.

⛏️ VIDEO 1 — Gorge → Foundations + Pylons
SCENE LOCK: Begin exactly from IMAGE 1. Preserve the source-image camera, terrain, gorge width, old road and permanent landmarks pixel-stably. Static tripod throughout with no pan, tilt, zoom, push-in, orbit, shake or perspective drift.

STAGE: Construction progresses through physically sequential foundation and early pylon operations. Excavators cut foundation benches into both rims, workers install reinforcement and formwork, concrete is placed into supported forms, and the two pylon bases progressively rise from their grounded foundations.

DETAILS: Excavators perform repeated digging and loading cycles. Trucks physically arrive and leave. Reinforcement is carried, positioned and tied by workers before concrete placement. Formwork is assembled around supported reinforcement. Concrete enters through real equipment and fills prepared forms under gravity. Clouds streak continuously, shadows sweep across the gorge and workers and vehicles move at the same accelerated timelapse rate.

NEGATIVE: No text, logos or watermarks. No instant pylons, teleporting concrete, floating reinforcement, unsupported structure, changing terrain, morphing landmarks, camera movement, frozen sky, frozen shadows, normal-speed workers or objects snapping into place.

Animate in OpenArt

🏗️ VIDEO 2 — Balanced Cantilever Growth
SCENE LOCK: Begin exactly from IMAGE 2. Preserve both pylons, their foundations, deck cross-section, bridge centreline, terrain and permanent landmarks. Camera remains completely locked and all existing structural geometry remains rigid.

STAGE: Balanced cantilever construction advances from both pylons toward mid-span through repeated physically plausible segment cycles. The central gap progressively becomes smaller but does not close.

DETAILS: A form traveller advances only after resting on the last completed deck segment. Workers prepare the next supported segment, reinforcement and structural connections are installed, concrete or prefabricated structural components are placed, and the new segment becomes continuous with the existing deck. New stay cables are installed only after corresponding deck progress and become visibly taut between the pylon and supported deck. The operation alternates in balanced progression on both sides. Winter weather slows activity, with longer inactive intervals between visible construction cycles. Clouds and long shadows continue moving even while construction pauses.

NEGATIVE: No text, logos or watermarks. No deck extrusion, instant bridge growth, teleporting segments, unsupported cantilever, floating form traveller, disconnected cables, random new cable pattern, changing pylons, camera drift, frozen clouds, frozen shadows or simultaneous appearance of multiple completed segments.

Animate in OpenArt

🔗 VIDEO 3 — The Closure

Bu benim bütün videonun en pahalı promptu olurdu. Çünkü viral an burada.

SCENE LOCK: Begin exactly from IMAGE 3. Preserve the two completed cantilever arms, both pylons, all stay cables, deck alignment, gorge, terrain and permanent landmarks exactly. Absolute static camera. The narrow central opening is the only major geometry allowed to change.

STAGE: Perform the final mid-span closure as one deliberate human-driven construction operation. The two existing deck tips remain rigid and aligned while crews physically prepare the final closure zone. The last structural segment is brought into the remaining opening, carefully aligned between the two existing deck ends and permanently connected. The moment the continuous deck line is completed is the visual climax.

DETAILS: Workers inspect and prepare both deck ends. Lifting equipment carries the closure component along a mechanically plausible controlled path. Guide lines and workers stabilize it while it approaches the gap. The component lowers gradually into alignment rather than appearing instantly. Workers secure the connection before lifting tension is released. The two original cantilever arms never move toward each other or morph; only the missing centre section is physically completed. Clouds and shadows continue sweeping naturally during the operation.

NEGATIVE: No text, logos or watermarks. No snapping bridge halves together, no deck stretching, no morphing gap, no instant closure, no floating closure segment, no bending pylons, no changing cable layout, no camera movement, no cut, no transition and no teleporting workers or machinery.

Animate in OpenArt

🌆 VIDEO 4 — Final Payoff / Traffic Moves Up

Dosyadaki en sevdiğim fikirlerden biri bu: finalde sadece "köprü bitti" demiyorsun. Trafik aşağıdaki eski yoldan yukarıdaki köprüye taşınıyor. Bu gerçek bir before/after kanıtı. Dosya da bunu filmin "bedeli" olarak tanımlıyor.

SCENE LOCK: Begin from IMAGE 4. The completed bridge, pylons, stay cables, roadway, gorge, old switchback road and all permanent landmarks remain structurally unchanged. Preserve the original locked perspective. Only a very subtle controlled digital crop push-in may occur near the end while maintaining stable geometry.

STAGE: One late-summer afternoon progresses into dusk, revealing the final consequence of the completed bridge. The architecture itself does not change. Traffic gradually transfers visually from the old road on the gorge floor to the completed bridge high above.

DETAILS: Afternoon shadows visibly lengthen and sweep across the gorge while high clouds move continuously. At first occasional vehicles remain visible on the old switchback road below. Traffic progressively increases across the completed bridge and becomes accelerated opposing streams. As dusk deepens, the gorge floor becomes dark and the old road carries only isolated vehicle lights while the bridge carries the dominant continuous flow high above. Existing bridge lighting activates progressively along the already completed roadway. Finish with a short hero hold on the illuminated bridge spanning the dark gorge.

NEGATIVE: No text, logos or watermarks. No bridge geometry changes, new cables, new structures, disappearing old road, teleporting vehicles, instant night transition, frozen sky, frozen shadows, fantasy lighting, excessive light trails in the sky, aggressive zoom, orbit, parallax shift or architectural morphing.

Animate in OpenArt

🎯 Özetle benim şablonum

Bu projede sayısal mühendislik bible'ını çöpe atmazdım. Tam tersine QA için saklardım. Ama onu generation promptuyla aynı şey olarak görmezdim.

Production katmanı:

WORLD BIBLE → MASTER FINAL → REVERSE IMAGE CHAIN → CHECKPOINT QA

Generation katmanı:

SCENE LOCK → STAGE DELTA → PHYSICAL EVIDENCE → NEGATIVE

Animation katmanı:

SOURCE FRAME → ONE OPERATION → HUMAN/MACHINE ACTION → ENVIRONMENTAL TIME → TARGET STATE → NEGATIVE

Ve en önemlisi:

Continuity'yi kelimelerle değil, görüntü mirasıyla taşırdım.

S9'u sıfırdan, S8'i sıfırdan, S7'yi sıfırdan üretmek yerine S9 master → S8 edit → S7 edit → ... → S0 edit. Dosyanın kendi QA'sında camera lock 10/10 olduğu halde 9/9 dikişin bozulması bana göre bunun en net kanıtı: kamera artık çözülmüş; sıradaki büyük problem world/structure inheritance.

✨ You can create these images and videos in OpenArt
