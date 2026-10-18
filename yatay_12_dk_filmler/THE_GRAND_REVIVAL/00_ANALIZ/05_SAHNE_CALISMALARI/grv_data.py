# -*- coding: utf-8 -*-
"""THE GRAND REVIVAL — kare (F) ve klip (S) verisi.
F[n]   = G(n) karesi (S(n)'nin İLK karesi) · mom (THE TIME MOMENT gövdesi) · act (ACTIVITY gövdesi; insan kuralı üretici ekler)
F[n′]  = oda son karesi (segmentin son klibinin HEDEFİ; kapı saymaz) — anahtar "10'" biçiminde
S[s]   = G(s) → hedef klibi · title · ne (TR) · mf (MOTION FOCUS) · flow · son (TR, hedef kare) · ses · kilit · bes (①·②·③)
Plan: ../../THE_GRAND_REVIVAL_PLAN.md §SAHNE SAHNE PLAN · onay: ../00_HIKAYE_ONAYI.md (17.10.2026)."""

from grv_istasyon import KADRO, KADRO4

# segment: (oda kodu, istasyon, ilk sahne, son sahne) · dönüş segmentleri bitmiş odanın akşam hâlidir
SEGMENT = [
    ("A", "A", 0, 9), ("H", "H", 10, 16), ("L", "L", 17, 29), ("D", "D", 30, 41), ("K", "K", 42, 53),
    ("M", "M", 54, 65), ("W", "W", 66, 72), ("B", "B", 73, 79), ("T", "T", 80, 85),
    ("H2", "H", 86, 86), ("L2", "L", 87, 87), ("A2", "A", 88, 88), ("D2", "D", 89, 89),
]
ODALAR = [
    (1, "ODA_01_ON_CEPHE", "ÖN CEPHE — KANEPE ÇIKAR, SARMAŞIK GİDER, CEPHE YENİLENİR", 0, 9),
    (2, "ODA_02_GIRIS_HOLU", "GİRİŞ HOLÜ — TRAVERTEN, AVİZE, KONSOL", 10, 16),
    (3, "ODA_03_SALON", "SALON — PARKE, HALI, İKİ KANEPE, İKİ BERJER, TAŞ SEHPA", 17, 29),
    (4, "ODA_04_YEMEK_ODASI", "YEMEK ODASI — ON KİŞİLİK MASA, 2 → 6 → 10 SANDALYE", 30, 41),
    (5, "ODA_05_MUTFAK", "MUTFAK — DOLAPLAR, ADA, TAŞ TEZGÂH, DÖRT TABURE", 42, 53),
    (6, "ODA_06_YATAK_ODASI", "ANA YATAK ODASI — BAŞLIK, KING YATAK, KOMODİNLER", 54, 65),
    (7, "ODA_07_GIYINME_ODASI", "GİYİNME ODASI — İKİ GARDIROP DUVARI, ORTA ADA", 66, 72),
    (8, "ODA_08_BANYO", "BANYO — TAŞ DUVARLAR, ÇİFT LAVABO, BAĞIMSIZ KÜVET", 73, 79),
    (9, "ODA_09_VERANDA", "VERANDA — AHŞAP DÖŞEME, DIŞ MEKÂN OTURMA GRUBU, IŞIKLAR", 80, 85),
    (10, "ODA_10_AKSAM", "AKŞAM — IŞIKLAR YANAR, İLK AKŞAM YEMEĞİ", 86, 89),
]
G_SET = {26, 34, 48, 60, 77, 89}   # gerçek zaman: beş ağır yükün yerine konuşu + ilk akşam yemeği

F, S = {}, {}

# ═══ ODA 1 · ÖN CEPHE (A) · S0–S9 ═══════════════════════════════════════════
F[0] = dict(mom="the first morning of work; two workers are carrying the big old sofa out through the front door, and ivy still curtains the stone arch.",
            act=f"From the doorway {KADRO} lift the big old sofa through the open arch, already half out of the door, and back down the cracked path with it towards a low flat cart waiting at the left of the path.")
S[0] = dict(title="KANEPE ÇIKAR", ne="İki işçi büyük eski kanepeyi kapıdan çıkarıp yoldaki arabaya yükler; ardından kırık koltuk gelir.",
            mf="The two workers carry the big old sofa from the open arch down the path and lift it onto the low flat cart at the left of the path.",
            flow="From the first frame the sofa is already half out of the arch: the two workers back down the cracked path with it, set it down on the flat cart and lash it, then carry an old broken armchair out through the arch and lift it onto the cart beside the sofa. The ivy over the arch and the cracked panes stay exactly as they are.",
            son="Kanepe ve kırık koltuk arabada · sarmaşıklı kemer, kırık pencereler, hasarlı çatı görünür",
            ses="müziksiz pencere · kanepe ayaklarının taşa sürtmesi, kesik nefes, kuş, uzak köpek",
            kilit="AÇILIŞ NESNESİ · 'from the first frame' · kuşkulu yük yok", bes="eşikte, işçilerin elinde · iki işçi · yoldaki düz araba")

F[1] = dict(mom="the old sofa sits lashed on the flat cart, and the ivy still hangs over the arch and both windows.",
            act=f"From a stepladder and from the lawn {KADRO} pull the first long strands of ivy off the stone arch, while the low flat cart with the sofa stands at the left of the path and a pile of cut ivy grows on the lawn.")
S[1] = dict(title="SARMAŞIK GİDER", ne="Kemeri ve iki pencereyi örten sarmaşık şerit şerit çekilir, demetler arabaya yüklenir; kemer açığa çıkar.",
            mf="The two workers pull the ivy from the stone arch and the two window openings in long strands and stack the bundles from the lawn onto the low flat cart.",
            flow="Strand by strand, from the top of the arch down, the curtain of ivy comes away and grimy grey stone shows through behind it; the workers bundle the strands on the lawn and lift each bundle onto the cart until the arch and both window openings stand clear.",
            son="Kemer ve iki pencere açıklığı sarmaşıksız · taş hâlâ kirli gri · İLK BÜYÜK SONUÇ (0:16)",
            ses="yaprak hışırtısı, kopan dal çıtırtısı, araba tekerleği", kilit="İLK BÜYÜK SONUÇ · açıklık sayısı sabit",
            bes="kemer ve pencere üstünde · iki işçi, merdiven · demetler arabaya")

F[2] = dict(mom="the arch and both window openings stand clear of ivy, and the grimy grey stone of the whole front shows.",
            act=f"At the left end of the front face {KADRO} lift the first buckets of clean water off the low flat cart and scrub the grimy stone with long brushes, dark water running down to the wall foot.")
S[2] = dict(title="CEPHE YIKANIR", ne="Taş cephe fırça ve kovayla soldan sağa bölge bölge temizlenir; koyu kir aşağı akar.",
            mf="The two workers carry buckets of water from the low flat cart to the front face and scrub the grime from the limestone with long brushes, from the left end to the right end.",
            flow="Panel by panel the dark grime runs down the wall in streaks and the stone underneath turns a clean pale beige, the clean band moving from the left end of the house towards the right; the workers carry fresh buckets from the flat cart and set the empty ones back on it. Late in the shot the workers carry the parts of a scaffold tower from the cart and set it up against the wall at the right end.",
            son="Bütün cephe açık bej taş · geometri aynı", ses="fırça sürtmesi, kova şıngırtısı, su damlası",
            kilit="yalnız renk değişir", bes="arabadaki kovalar · iki işçi, fırça · cephe soldan sağa")

F[3] = dict(mom="the whole front face is clean pale beige stone, and the broken old roof sags above it.",
            act=f"From the scaffold tower at the right end {KADRO} lift the first broken tiles off the roof and lower full buckets of tiles from the eaves down to the low flat cart below.")
S[3] = dict(title="ÇATI SÖKÜLÜR", ne="Kırık kiremitler bölüm bölüm sökülür, kovalarla arabaya iner; çatı altlığı aynı eğimde görünür.",
            mf="The two workers strip the broken clay tiles from the roof section by section and lower them in buckets from the eaves onto the low flat cart.",
            flow="From the right end towards the left, row after row of old tiles comes off, and the grey underlay and timber battens show along the same low slope; the hole left of the ridge is opened out to its battens. The workers lower each full bucket onto the cart, wheel the full cart aside and bring it back empty.",
            son="Bütün çatı soyulmuş: gri altlık ve çıtalar aynı eğimde", ses="kiremit kırılması, kova sesi, iskele tıkırtısı",
            kilit="çatı eğimi ve yüksekliği sabit", bes="çatıda kiremit · kova, iskele kulesi · araba")

F[4] = dict(mom="the roof is stripped to its grey underlay along the same low slope.",
            act=f"From the scaffold tower {KADRO} lift the first dark anthracite roof panels off a stack on a pallet beside the low flat cart and set the first row along the eaves at the right end.")
S[4] = dict(title="ÇATI KAPANIR", ne="Koyu antrasit çatı panelleri sıra sıra döşenir; çatı aynı eğim ve yükseklikte yenilenir.",
            mf="The two workers carry the dark anthracite roof panels from the stack on the pallet up the scaffold tower and lay them onto the underlay in rows, from the eaves up to the ridge.",
            flow="Row by row from the right end to the left, the dark panels close over the grey underlay until the whole roof is one dark anthracite surface on the same low slope, and the stack on the pallet shrinks panel by panel.",
            son="Çatı yeni, koyu antrasit, aynı siluet çizgisi", ses="vida tabancası, panel tıkırtısı",
            kilit="çatı siluet çizgisi sabit", bes="paletteki istif · iki işçi, iskele kulesi · çatı altlığı")

F[5] = dict(mom="the new dark roof is complete, and the two big window openings still hold their rotten old frames.",
            act=f"At the left window {KADRO} lift the rotten old frame out of the opening and set it on the low flat cart, while a new glazed unit in a slim bronze frame waits on its lifting slings against the wall.")
S[5] = dict(title="SOL PENCERE", ne="Sol büyük pencerenin eski çerçevesi çıkar; yeni bronz çerçeveli cam ünite aynı açıklığa takılır.",
            mf="The two workers carry the new bronze-framed glazed unit from the low flat cart to the left window opening and set it into the opening on its slings.",
            flow="Early in the shot the workers carry the scaffold tower down in parts and stack them on the cart. The rotten frame goes onto the cart; the workers lift the new unit on its slings, angle it into the opening, seat it level and fix it, and the slings come loose. The right window opening still holds its old cracked frame.",
            son="Sol pencere yeni, sağ eski", ses="cam sesi, matkap", kilit="açıklık ölçüsü sabit",
            bes="araba üstünde cam ünite · iki işçi, sapan · sol açıklık")

F[6] = dict(mom="the left window is new, and the right window opening still holds its rotten frame.",
            act=f"At the right window {KADRO} lift the rotten old frame out of the opening onto the low flat cart, the second new glazed unit standing ready on its lifting slings.")
S[6] = dict(title="SAĞ PENCERE", ne="Sağ büyük pencere aynı ölçüyle yenilenir; iki pencere eşleşir.",
            mf="The two workers carry the second bronze-framed glazed unit from the low flat cart to the right window opening and set it into the opening on its slings.",
            flow="They seat the unit level, fix it and slip the slings off, and now both big windows are new and match each other exactly in size and frame; the old frame is carried to the cart and laid on it.",
            son="İki pencere yeni ve eş", ses="cam, vida", kilit="iki pencere aynı ölçü",
            bes="araba üstünde ikinci ünite · iki işçi, sapan · sağ açıklık")

F[7] = dict(mom="both windows are new, and the sagging old door still hangs in the arch.",
            act=f"At the arch {KADRO} lift the old door leaves off their hinges and lay them on the low flat cart, while the new walnut double door waits in two leaves on a padded stand beside the arch.")
S[7] = dict(title="CEVİZ KAPI", ne="Eski kapı sökülür; büyük çift kanatlı ceviz kapı aynı kemer açıklığına takılır.",
            mf="The two workers carry the two leaves of the new walnut double door from the padded stand to the stone arch and hang them on new hinges inside the arch.",
            flow="The old leaves are carried to the cart and laid on it; the new walnut leaves are lifted one at a time onto their hinges, swung once and closed, filling the arch exactly. The stone of the arch itself stays untouched. Late in the shot the workers bring a stack of large pale flagstones on a pallet and set it on the lawn.",
            son="Ceviz kapı yerinde, kanatlar kapalı · kemer korunur", ses="menteşe, ahşabın tok sesi",
            kilit="kemer korunur", bes="kemer yanındaki sehpa · iki işçi · kemer içi")

F[8] = dict(mom="the walnut door stands closed in the arch, and the front path is still cracked old concrete.",
            act=f"On the front path {KADRO} break up the cracked old concrete with a demolition drill and lift the broken pieces onto the low flat cart, a stack of large pale flagstones waiting on a pallet on the lawn.")
S[8] = dict(title="TAŞ YOL", ne="Eski beton yol kırılır; açık taş plakalar kapıdan dışa döşenir, kenarlara yol lambaları dikilir.",
            mf="The two workers lay the large pale flagstones from the stack on the pallet onto a bed of sand along the line of the old path, from the arch out towards the camera.",
            flow="The broken concrete goes onto the cart; flagstone after flagstone is carried from the stack, bedded and tapped level, and the new path grows from the door step down towards the bottom of the frame, the same width and line as the old one. Low bronze path lights are set at intervals along both edges, unlit.",
            son="Taş yol tamam, aynı genişlik ve çizgi · kenarlarda sönük yol lambaları", ses="taş üstüne taş, lastik tokmak",
            kilit="yol başı, sonu, genişliği sabit", bes="paletteki taş istifi · iki işçi · eski yolun çizgisi")

F[9] = dict(mom="the new stone path runs from the walnut door, and the two planting beds beside it are still overgrown.",
            act=f"In the left planting bed {KADRO} pull the weeds out by the armful and lift them onto the low flat cart, a heap of dark fresh soil and trays of young plants waiting on the lawn.")
S[9] = dict(title="BAHÇE · ARABA ÇIKAR", ne="İki bitki yatağı temizlenir, kazılır, lavanta ve şimşirle dikilir; sonda araba kadrajdan çekilir.",
            mf="The two workers carry young lavender and box plants from the trays on the lawn into the two dug planting beds, then lift the last empty trays onto the low flat cart.",
            flow="Bed by bed the weeds come out and dark soil is turned, and rows of small grey-green plants fill both beds; at the end the workers lift the empty trays onto the cart and wheel it out of the frame at the left.",
            son="Dış cephe ilk tamamlanmış hâlinde · içerisi henüz gösterilmedi", ses="kürek, toprak, kuş",
            kilit="ön cephe bölümünün sonu", bes="çimdeki fide kasaları · iki işçi · iki yatak")

F["10'"] = dict(mom="the front of the villa is restored: clean pale stone, a new dark roof, two new windows, the walnut door and the new path between planted beds.",
                act=f"At the left edge of the frame {KADRO} lift the last folded stepladder onto their shoulders and walk off along the lawn, leaving the garden quiet.")

# ═══ ODA 2 · GİRİŞ HOLÜ (H) · S10–S16 ═══════════════════════════════════════
F[10] = dict(mom="the first job inside: the entrance hall lies dim and ruined behind the new walnut door.",
             act=f"In the middle of the hall {KADRO} lift the broken old console table off the floor and carry it out through the open walnut door towards the low flat cart on the path, while heaps of plaster are shovelled into a barrow.")
S[10] = dict(title="HOL BOŞALIR", ne="Kırık eski konsol ve döküntü kapıdan dışarı taşınır; hol boşalır.",
             mf="The two workers carry the broken console and the heaps of fallen plaster from the hall floor out through the open walnut door onto the low flat cart on the path.",
             flow="Load by load the debris goes out, the console first and then barrow after barrow of plaster and dry leaves, until the floor lies bare and swept.",
             son="Hol boş · kemer, kapı, iki dar pencere sabit", ses="kürek sürtmesi, el arabası, kapıdan kuş sesi",
             kilit="kemer + ceviz kapı = A ile ortak çapa", bes="zemindeki enkaz · iki işçi, el arabası · dışarıdaki araba")

F[11] = dict(mom="the hall is empty and swept, its walls cracked and stained.",
             act=f"Along the right wall {KADRO} set a folded stepladder against the wall and spread fresh grey-white plaster over the cracks with wide trowels from a bucket on the low flat cart.")
S[11] = dict(title="DUVAR ONARILIR", ne="Bozuk duvar yüzeyleri sıvayla onarılır; duvarlar düz, henüz boyasız.",
             mf="The two workers carry buckets of fresh plaster from the low flat cart to the walls and spread it onto the cracked surfaces with wide trowels, from the left wall round to the right wall.",
             flow="Patch by patch the cracks and bare spots close under smooth grey-white plaster, the patched area spreading along the left wall, across the far wall around the door and along the right wall.",
             son="Duvarlar düz, gri-beyaz, boyasız", ses="mala sürtmesi, kova", kilit="—",
             bes="arabadaki sıva kovası · iki işçi, mala · çatlak yüzeyler")

F[12] = dict(mom="the walls are smooth fresh plaster, and the floor is still bare grey screed.",
             act=f"At the far end of the floor {KADRO} lift the first large travertine tiles off a stack on a pallet just inside the door and set them on a bed of mortar, a low flat cart bringing more.")
S[12] = dict(title="TRAVERTEN", ne="Büyük traverten zemin plakaları kapı eşiğinden kameraya doğru döşenir.",
             mf="The two workers lay the large pale travertine tiles from the stack on the pallet onto a mortar bed, row after row from the door towards the camera.",
             flow="The pale surface grows row by row from the threshold towards the camera, each tile set and tapped level, until the bare screed is covered edge to edge; the stack on the pallet shrinks to nothing and the empty pallet goes out on the cart.",
             son="Açık traverten zemin kesintisiz", ses="lastik tokmak, mala", kilit="—",
             bes="kapı içindeki palet · iki işçi · harç yatağı")

F[13] = dict(mom="the travertine floor is laid, and the patched walls are still unpainted grey-white.",
             act=f"Across the new travertine {KADRO} unroll a grey protective membrane and set the first rollers of warm off-white paint against the left wall, tins of paint on the low flat cart.")
S[13] = dict(title="BOYA", ne="Duvarlar sıcak kırık beyaza boyanır.",
             mf="The two workers roll warm off-white paint from the tins on the low flat cart onto the patched walls, the left wall first, then the far wall around the door, then the right wall.",
             flow="The grey-white patches go under an even warm off-white, the fresh colour spreading wall by wall and the hall turning brighter in the morning light; the empty tins are stacked back on the cart.",
             son="Duvarlar sıcak kırık beyaz · hol aydınlık", ses="rulo, merdiven tıkırtısı", kilit="—",
             bes="arabadaki boya · iki işçi, rulo · sıvalı duvarlar")

F[14] = dict(mom="the hall is painted warm off-white, and a short bare chain hangs from the ceiling.",
             act=f"Under the bare chain {KADRO} set a tall stepladder and lift the large bronze chandelier out of its padded crate on the low flat cart, carrying it between them towards the ladder.")
S[14] = dict(title="AVİZE", ne="Büyük bronz avize iki işçi ve sabit merdivenle mevcut bağlantıya takılır.",
             mf="The two workers carry the bronze chandelier from its crate on the low flat cart to the stepladder and hang it onto the short chain at the middle of the ceiling.",
             flow="One worker on the ladder takes the weight while the other lifts from below; the chandelier rises the last metre, is hooked onto the chain and hangs level, unlit, and the empty crate is carried out to the cart.",
             son="Avize asılı, sönük", ses="zincir şıkırtısı, merdiven", kilit="avize kendi zincirinde · ek kaldırma düzeni yok",
             bes="arabadaki sandık · iki işçi, merdiven · tavandaki zincir")

F[15] = dict(mom="the bronze chandelier hangs over the hall, and the left wall stands bare.",
             act=f"Just inside the walnut door {KADRO} lift the first stone leg of the long console off the low flat cart and set it against the far part of the left wall, the long travertine top waiting on the cart.")
S[15] = dict(title="KONSOL", ne="Üç metrelik traverten konsol parça parça taşınıp sol duvara kurulur; üstüne tek vazo konur.",
             mf="The two workers carry the long travertine console top from the low flat cart to the left wall and set it onto its two stone legs against the wall.",
             flow="The two legs go down first against the far part of the left wall; the workers slide the long top off the cart, carry it between them and lower it onto the legs. Late in the shot one tall ceramic vase is lifted from a crate on the cart and set on the console.",
             son="Tek konsol sol duvarda, üstünde tek vazo", ses="taşın taşa oturuşu", kilit="tek konsol",
             bes="arabadaki tabla ve ayaklar · iki işçi · sol duvar")

F[16] = dict(mom="the travertine console stands against the left wall, and the right wall stands bare.",
             act=f"Inside the walnut door {KADRO} lift a long upholstered cream bench off the low flat cart and carry it towards the right wall, a large framed painting in its wrapping leaning by the door.")
S[16] = dict(title="BANK VE TABLO", ne="Uzun döşemeli bank sağ duvara, konsolun üstüne büyük tablo; kapı kapanır. Hol tamam.",
             mf="The two workers carry the long cream bench from the low flat cart to the right wall, then lift the framed painting from beside the door onto the wall above the console.",
             flow="The bench is set down against the far part of the right wall, leaving the way to the door open; the wrapping comes off the painting and it goes up on two hooks above the console, hanging level. The workers roll up the grey membrane, wheel the empty cart out and close the walnut door.",
             son="Hol tamam: konsol, vazo, tablo, bank, avize", ses="kapı kapanışının tok sesi",
             kilit="ayna yok — tablo (sahip kararı)", bes="arabadaki bank, kapı yanındaki tablo · iki işçi · sağ duvar, konsol üstü")

F["17'"] = dict(mom="the entrance hall is finished: travertine floor, warm white walls, the bronze chandelier, the console with its vase and painting, and the long bench.",
                act=f"By the closed walnut door {KADRO} lift the rolled membrane onto the low flat cart and wheel it out of the frame at the right.")

# ═══ ODA 3 · SALON (L) · S17–S29 ═══════════════════════════════════════════
F[17] = dict(mom="the salon lies dim and ruined, and through the wide opening the finished entrance hall shows.",
             act=f"In the middle of the room {KADRO} lift the old torn sofa off the floor and carry it towards the wide opening, where a low flat cart waits, while a pile of debris is swept into a barrow.")
S[17] = dict(title="SALON BOŞALIR", ne="Kalan eski koltuk ve döküntü hol açıklığından çıkarılır; salon boşalır. Açılıştaki kanepe yeniden görünmez.",
             mf="The two workers carry the old sofa, the broken armchair and the debris from the salon floor out through the wide opening onto the low flat cart waiting in the hall.",
             flow="Load after load leaves through the opening, the torn sofa, the broken armchair, then barrows of debris, until the floor lies bare and swept.",
             son="Salon boş · açıklıktan bitmiş hol görünür", ses="sürtme, el arabası",
             kilit="açılış kanepesi geri dönmez · hol = ortak çapa", bes="zemindeki eski eşya · iki işçi, el arabası · holdeki araba")

F[18] = dict(mom="the salon is empty, its walls scuffed and stained.",
             act=f"By the left wall {KADRO} set a stepladder and roll warm ivory paint from tins on the low flat cart onto the scuffed walls, a grey protective membrane spread along the floor.")
S[18] = dict(title="FİLDİŞİ", ne="Duvarlar sıcak fildişine boyanır.",
             mf="The two workers roll warm ivory paint from the tins on the low flat cart onto the walls, from the left wall across the far wall round to the strips of wall between the glass doors.",
             flow="The stains go under an even warm ivory, wall by wall, and the room brightens; the empty tins are stacked back on the cart.",
             son="Duvarlar fildişi · pencere, tavan, duvar sınırları aynı", ses="rulo", kilit="—",
             bes="arabadaki boya · iki işçi, rulo · duvarlar")

F[19] = dict(mom="the walls are warm ivory, and the floor is still bare grey screed.",
             act=f"Along the far wall {KADRO} lift the first wide oak boards off a stack on the low flat cart and set the first row, a trestle workbench with a saw standing by the opening.")
S[19] = dict(title="MEŞE PARKE", ne="Geniş açık meşe parke uzak duvardan kameraya doğru, tek yönde döşenir.",
             mf="The two workers lay the wide pale oak boards from the stack on the low flat cart onto the screed, row after row from the far wall towards the camera.",
             flow="The pale boards advance across the screed in one direction, each cut to length at the workbench, until the whole room is oak; offcuts pile up beside the bench.",
             son="Meşe zemin tek yönde", ses="testere, tokmak", kilit="döşeme yönü sabit",
             bes="arabadaki tahta istifi · iki işçi, tezgâh · şap")

F[20] = dict(mom="the oak floor is down, and the far wall left of the opening is plain ivory plaster.",
             act=f"At the far wall {KADRO} lift the first tall walnut panel off a stack on the low flat cart and set it against the plaster left of the opening, fixing it with a drill.")
S[20] = dict(title="CEVİZ PANEL", ne="Hol açıklığının solundaki duvar bölümüne ceviz paneller takılır.",
             mf="The two workers carry the tall walnut panels from the stack on the low flat cart to the far wall and fix them onto the plaster left of the opening, one beside the next.",
             flow="Panel by panel the dark walnut spreads from the corner towards the opening until that part of the far wall is one warm dark surface; the right part of the wall and the opening stay unchanged.",
             son="Ceviz panel yalnız sol bölümde", ses="matkap", kilit="açıklık ve duvarın kalanı değişmez",
             bes="arabadaki panel istifi · iki işçi, matkap · uzak duvarın sol bölümü")

F[21] = dict(mom="the walnut panelling is up, and a bare ceiling rose marks the middle of the ceiling.",
             act=f"Under the ceiling rose {KADRO} set a tall stepladder and lift the ring-shaped bronze ceiling light out of its crate on the low flat cart.")
S[21] = dict(title="TAVAN IŞIĞI", ne="Bronz halka tavan aydınlatması belirlenen bağlantı noktasına kurulur.",
             mf="The two workers carry the bronze ring light from its crate on the low flat cart up the stepladder and hang it from the ceiling rose on three short chains.",
             flow="The ring rises the last metre, the three chains are hooked on, and it hangs level over the middle of the room, unlit; the empty crate is carried back to the cart.",
             son="Halka ışık asılı, sönük · yüksekliği sabit", ses="zincir", kilit="—",
             bes="arabadaki sandık · iki işçi, merdiven · tavan göbeği")

F[22] = dict(mom="the bronze ring light hangs over the empty oak floor.",
             act=f"At the far edge of the clear floor {KADRO} lift a big rolled cream rug off the low flat cart in the opening and set it down, ready to unroll.")
S[22] = dict(title="HALI", ne="Büyük krem halı boş zeminin ortasına serilir; köşeleri bundan sonra sabit.",
             mf="The two workers carry the rolled cream rug from the low flat cart to the middle of the room and unroll it from the far edge towards the camera.",
             flow="The roll travels across the oak and opens flat, the workers squaring its corners, until it lies centred under the ring light; the empty cart goes back out through the opening.",
             son="Halı ortada, köşeleri sabit", ses="halının yumuşak düşüşü", kilit="halı köşeleri kilit",
             bes="arabadaki rulo · iki işçi · zeminin ortası")

F[23] = dict(mom="the cream rug lies in the middle of the oak floor.",
             act=f"In the wide opening {KADRO} lift the long four-seat cream sofa off the low flat cart, one at each end, and carry it in.")
S[23] = dict(title="ANA KANEPE", ne="Dört kişilik ana kanepe hol açıklığından getirilip halının sol kenarına konur.",
             mf="The two workers carry the long cream sofa from the low flat cart in the opening to the left edge of the rug and set it down there.",
             flow="They walk the sofa in end-first, turn it square to the rug and lower it, then plump the cushions; the flat cart goes back out through the opening.",
             son="Tek ana kanepe", ses="ahşap ayakların meşeye konuşu", kilit="tek kanepe",
             bes="açıklıktaki araba · iki işçi · halının sol kenarı")

F[24] = dict(mom="the main sofa stands along the left edge of the rug.",
             act=f"In the wide opening {KADRO} lift the second big cream sofa off the low flat cart and carry it in, one at each end.")
S[24] = dict(title="İKİNCİ KANEPE", ne="İkinci büyük kanepe halının karşı kenarına konur.",
             mf="The two workers carry the second cream sofa from the low flat cart in the opening to the right edge of the rug and set it down facing the first.",
             flow="Set square to the rug, the two sofas face each other across a wide walkway, and the flat cart goes back out.",
             son="İki kanepe, aralarında geniş geçiş", ses="ayak sesi, kumaş", kilit="iki kanepe",
             bes="açıklıktaki araba · iki işçi · halının sağ kenarı")

F[25] = dict(mom="two cream sofas face each other across the rug.",
             act=f"In the wide opening {KADRO} lift the first cognac leather armchair off the low flat cart and carry it towards the far left corner of the rug.")
S[25] = dict(title="BERJERLER", ne="İki deri berjer uzak köşelere; sonda iki işçi daha katılır, taş sehpa açıklığa gelir.",
             mf="The two workers carry the two cognac leather armchairs one at a time from the low flat cart in the opening to the far corners of the rug and set each one down.",
             flow="The first armchair goes to the far left corner, the cart goes out and comes back, and the second goes to the far right corner, leaving the way to the opening clear. Late in the shot two more workers in the same clothes help wheel the big stone coffee table in on a low flat cart and stop just inside the opening.",
             son="İki berjer · taş sehpa arabada, açıklığın içinde", ses="deri gıcırtısı, tekerlek",
             kilit="her yük tek berjer · geç teslimat", bes="açıklıktaki araba · iki işçi · halının uzak köşeleri")

F[26] = dict(mom="the big stone coffee table waits on its low flat cart just inside the opening.",
             act=f"Just inside the opening {KADRO4} lift the big stone coffee table off the low flat cart, two at each side, and carry it slowly across the oak towards the rug.")
S[26] = dict(title="TAŞ SEHPA", ne="GERÇEK ZAMAN · dört işçi taş orta sehpayı arabadan alıp halının ortasına yavaşça indirir.",
             mf="Four workers lift the big stone coffee table from the low flat cart in the opening, carry it slowly to the middle of the rug and lower it onto its four short feet.",
             flow="From the first frame the table is already lifting off the cart; the four walk it in short careful steps, set it down square between the sofas so that its feet press into the rug and it touches neither sofa, and step back.",
             son="Sehpa halının ortasında, ayakları halıya basar, kanepelere değmez", ses="taşın yumuşak inişi, nefes",
             kilit="GERÇEK ZAMAN · ağırlık yavaş okunur", bes="açıklıktaki araba · dört işçi · halının ortası")

F[27] = dict(mom="the stone coffee table stands in the middle of the rug.",
             act=f"In the wide opening {KADRO} lift a long low walnut console off the low flat cart and carry it towards the walnut panelling.")
S[27] = dict(title="CEVİZ KONSOL", ne="Uzun alçak ceviz konsol ceviz panelin önüne konur.",
             mf="The two workers carry the long low walnut console from the low flat cart in the opening to the panelling and set it down against the panelling.",
             flow="They lower it gently, square it to the panelling and wipe its top, and the empty cart goes back out through the opening.",
             son="Konsolun ayak izi sabit", ses="ahşap", kilit="—", bes="açıklıktaki araba · iki işçi · panelin önü")

F[28] = dict(mom="the walnut console stands against the panelling.",
             act=f"In the wide opening {KADRO} lift the first small round side table off the low flat cart and carry it towards the near end of the left sofa.")
S[28] = dict(title="YAN SEHPALAR", ne="İki küçük yan sehpa sırayla, her seferinde tek yük, kanepelerin uçlarına konur.",
             mf="The two workers carry the two small round side tables one at a time from the low flat cart in the opening to the near ends of the two sofas.",
             flow="One table per trip: the first goes to the left sofa, the cart goes out and comes back, and the second goes to the right sofa, so that exactly two side tables stand in the room.",
             son="Tam iki yan sehpa", ses="ayak sesi", kilit="sayı 2", bes="açıklıktaki araba · iki işçi · kanepe uçları")

F[29] = dict(mom="two side tables stand at the near ends of the sofas.",
             act=f"In the wide opening {KADRO} lift a tall bronze floor lamp off the low flat cart, a young olive tree in a big stone pot waiting on a second cart behind it.")
S[29] = dict(title="LAMBADER VE ZEYTİN", ne="Lambader sağ kanepenin yanına; büyük taş saksıda genç zeytin cam kapıların yanına. Salon tamam.",
             mf="The two workers carry the tall floor lamp from the low flat cart to the right sofa, then wheel the potted olive tree on its cart to the glass doors and set it down.",
             flow="The lamp is stood beside the right sofa, unlit; the olive tree in its stone pot is set down by the glass doors. The workers roll up the membrane along the walking line and wheel both carts out through the opening.",
             son="Salon tamam — ilk iç mekân zirvesi · BÖLÜM 1 sonu", ses="saksının taşa oturuşu",
             kilit="BÖLÜM 1 sonu (240,0 sn)", bes="açıklıktaki iki araba · iki işçi · sağ kanepe yanı, cam kapılar")

F["30'"] = dict(mom="the salon is finished: two cream sofas and two cognac armchairs around the stone table on the cream rug, the walnut console, two side tables, the floor lamp and the olive tree.",
                act=f"In the wide opening {KADRO} lift the last rolled strip of membrane onto the low flat cart and wheel it away into the hall.")

# ═══ ODA 4 · YEMEK ODASI (D) · S30–S41 ═════════════════════════════════════
F[30] = dict(mom="the dining room lies dim and ruined, and beyond its glass doors the old veranda lies under weeds.",
             act=f"At the open glass doors {KADRO} lift the old dark table onto a low flat cart outside on the veranda and carry the broken chairs out after it.")
S[30] = dict(title="YEMEK ODASI BOŞALIR", ne="Eski masa ve sandalyeler cam kapılardan verandadaki arabaya taşınır; oda boşalır.",
             mf="The two workers carry the old table, the broken chairs and the debris from the floor out through the open glass doors onto the low flat cart on the veranda.",
             flow="Load after load leaves through the middle glass door, until the room lies bare and swept; the cart is wheeled away along the veranda and brought back empty.",
             son="Oda boş · mutfak kapısından harap mutfak, camlardan harap veranda", ses="sürtme, tekerlek",
             kilit="yük yolu = cam kapılar (veranda)", bes="zemindeki eski eşya · iki işçi · verandadaki araba")

F[31] = dict(mom="the room is empty, its walls stained grey-white.",
             act=f"By the left wall {KADRO} set a stepladder and roll warm greige paint from tins on the low flat cart onto the stained walls.")
S[31] = dict(title="GREJ", ne="Duvarlar sıcak greje boyanır; tavan ve pencere geometrisi korunur.",
             mf="The two workers roll warm greige paint from the tins on the low flat cart onto the walls, from the left wall around the windows to the right wall.",
             flow="The stains go under an even warm greige wall by wall, and the empty tins are stacked back on the cart.",
             son="Duvarlar grej", ses="rulo", kilit="—", bes="arabadaki boya · iki işçi · duvarlar")

F[32] = dict(mom="the walls are warm greige, and the floor is still bare grey screed.",
             act=f"At the far end by the glass doors {KADRO} lift the first large pale stone tiles off a stack on a pallet and set them on a mortar bed, a low flat cart bringing more.")
S[32] = dict(title="TAŞ ZEMİN", ne="Mat açık taş zemin plakaları cam kapılardan kameraya doğru döşenir.",
             mf="The two workers lay the large matt stone tiles from the stack on the pallet onto a mortar bed, row after row from the glass doors towards the camera.",
             flow="The pale surface grows towards the camera row by row, each tile set and tapped level, until the bare screed is covered; the empty pallet goes out on the cart.",
             son="Taş zemin · desen bundan sonra aynı", ses="lastik tokmak", kilit="zemin deseni kilit",
             bes="kapıdaki palet · iki işçi · harç yatağı")

F[33] = dict(mom="the stone floor is laid, and a bare hook marks the middle of the ceiling.",
             act=f"Under the bare hook {KADRO} set a tall stepladder and lift the long linear bronze chandelier out of its long crate on the low flat cart.")
S[33] = dict(title="AVİZE", ne="Bronz avize asılır; sonda iki işçi daha katılır, ceviz masa orta cam kapıdan gelir.",
             mf="The two workers carry the long bronze chandelier from its crate on the low flat cart up the stepladder and hang it from the ceiling hook on two chains along the length of the room.",
             flow="The chandelier rises the last metre and hangs level and low over the middle of the room, unlit. Late in the shot two more workers in the same clothes help bring the long walnut table in through the middle glass door on a low flat cart and stop just inside the door.",
             son="Avize merkez ekseninde · masa arabada, kapının içinde", ses="zincir, tekerlek",
             kilit="geç teslimat", bes="arabadaki sandık · iki işçi, merdiven · tavan kancası")

F[34] = dict(mom="the long walnut table waits on a low flat cart just inside the middle glass door.",
             act=f"Just inside the glass door {KADRO4} lift the long walnut table off the low flat cart, two at each end, and walk it slowly towards the chandelier.")
S[34] = dict(title="MASA", ne="GERÇEK ZAMAN · dört işçi on kişilik ceviz masayı avizenin altına koyar.",
             mf="Four workers lift the long walnut dining table from the low flat cart at the glass door, carry it to the middle of the room and set it down under the chandelier, its length pointing at the camera.",
             flow="From the first frame the table is already rising off the cart; the four carry it in short careful steps, line it up under the chandelier and lower it until all its legs stand on the stone, then step back to the sides.",
             son="Tek masa, tek sabit konum", ses="ahşabın taşa inişi, nefes", kilit="GERÇEK ZAMAN · ağırlık yavaş okunur",
             bes="kapıdaki araba · dört işçi · avizenin altı")

F[35] = dict(mom="the walnut table stands under the chandelier.",
             act=f"At the glass doors {KADRO} lift the first upholstered head chair off the low flat cart and carry it towards the far end of the table.")
S[35] = dict(title="BAŞ SANDALYELERİ", ne="İki baş sandalyesi sırayla masanın iki ucuna; toplam iki.",
             mf="The two workers carry the two head chairs one at a time from the low flat cart at the glass doors to the two ends of the table.",
             flow="One chair per trip: the first goes to the far end, the cart is wheeled back, and the second goes to the near end, so exactly two chairs stand at the table.",
             son="Toplam iki sandalye", ses="ayak sesi", kilit="sayı 2", bes="kapıdaki araba · iki işçi · masanın iki ucu")

F[36] = dict(mom="two chairs stand at the ends of the table.",
             act=f"At the glass doors {KADRO} lift a long low walnut sideboard off the low flat cart and carry it towards the right wall.")
S[36] = dict(title="BÜFE", ne="Uzun servis büfesi sağ duvara; iki sandalye yerinde, geçiş açık.",
             mf="The two workers carry the long walnut sideboard from the low flat cart at the glass doors to the right wall and set it down against the wall.",
             flow="They lower it and square it to the wall so the walkway beside the table stays open, and the two chairs stay where they are.",
             son="Büfe sağ duvarda · iki sandalye aynı yerde", ses="ahşap", kilit="büfe geçişi kapatmaz",
             bes="kapıdaki araba · iki işçi · sağ duvar")

F[37] = dict(mom="the sideboard stands against the right wall.",
             act=f"At the glass doors {KADRO} lift a tall walnut display cabinet with clear glass doors off the low flat cart and walk it upright towards the right wall.")
S[37] = dict(title="SERGİ DOLABI", ne="Ahşap çerçeveli yüksek sergileme dolabı büfenin ötesine; masa, büfe, iki sandalye korunur.",
             mf="The two workers carry the tall display cabinet from the low flat cart at the glass doors to the right wall and stand it beyond the sideboard.",
             flow="They walk it upright in small steps and set it plumb against the wall; the table, the sideboard and the two chairs stay unchanged.",
             son="Tek yeni dolap", ses="cam kapakların hafif tıkırtısı", kilit="tek dolap",
             bes="kapıdaki araba · iki işçi · büfenin ötesi")

F[38] = dict(mom="the display cabinet stands beyond the sideboard, and two chairs stand at the ends of the table.",
             act=f"At the glass doors {KADRO} lift the first of four side chairs off a stack of chairs on the low flat cart and carry it towards the left side of the table.")
S[38] = dict(title="DÖRT SANDALYE · SAYIM PİLOTU", ne="Dört yan sandalye tek tek sol yana; toplam altı. SAYIM PİLOTU.",
             mf="The two workers carry four side chairs one at a time from the stack on the low flat cart at the glass doors to the left side of the table and set them in a row.",
             flow="One chair per trip: the stack on the cart shrinks by one each time and the row along the left side grows to four, evenly spaced, while the head chairs at the two ends stay where they are, so six chairs stand at the table.",
             son="Toplam altı sandalye: iki baş + solda dört", ses="sandalye ayaklarının taşa konuşu ×4",
             kilit="SAYIM PİLOTU · her yük tek sandalye (DERS 89)", bes="arabadaki sandalye istifi · iki işçi · masanın sol yanı")

F[39] = dict(mom="six chairs stand at the table, four along its left side.",
             act=f"By the left wall {KADRO} set a stepladder under the first window and lift a bundle of folded linen curtains off the low flat cart.")
S[39] = dict(title="PERDELER", ne="Tavandan yere perdeler iki pencereye asılır; altı sandalye değişmez.",
             mf="The two workers carry the folded linen curtains from the low flat cart to the two tall windows in the left wall and hang them from the rods, ceiling to floor.",
             flow="Window by window the linen falls in soft folds to the floor; the six chairs and the window openings stay as they were.",
             son="Perdeler asılı · altı sandalye aynı", ses="halka şıkırtısı", kilit="pencere konumu sabit",
             bes="arabadaki perde demeti · iki işçi, merdiven · iki pencere")

F[40] = dict(mom="curtains hang at the two windows, and six chairs stand at the table.",
             act=f"At the glass doors {KADRO} lift the first of the last four chairs off the stack on the low flat cart and carry it towards the right side of the table.")
S[40] = dict(title="SON DÖRT SANDALYE", ne="Kalan dört sandalye tek tek sağ yana; toplam on.",
             mf="The two workers carry the last four side chairs one at a time from the stack on the low flat cart at the glass doors to the right side of the table and set them in a row.",
             flow="One chair per trip, the stack on the cart shrinks to nothing and the row along the right side grows to four, matching the left side, so ten chairs stand at the table.",
             son="Toplam on sandalye: iki baş + iki yanda dörder", ses="sandalye ayakları ×4", kilit="sayı 10 · her yük tek sandalye",
             bes="arabadaki istif · iki işçi · masanın sağ yanı")

F[41] = dict(mom="ten chairs stand at the table.",
             act=f"At the right wall {KADRO} lift a large framed painting off the low flat cart and carry it towards the sideboard, a low flower arrangement waiting in a box on the cart.")
S[41] = dict(title="TABLO VE ÇİÇEK", ne="Büfenin üstüne büyük tablo; sonda masaya tek çiçek aranjmanı. Oda tamam.",
             mf="The two workers carry the framed painting from the low flat cart to the right wall and hang it above the sideboard, then set the flower arrangement onto the middle of the table.",
             flow="The painting goes up level on two hooks; one low arrangement of white flowers is set in the middle of the table. The workers roll up the membrane and wheel the cart out through the glass doors.",
             son="Masa, on sandalye, büfe, dolap, perde, avize tamam", ses="kapının kapanışı", kilit="yemek odası sonu",
             bes="arabadaki tablo ve kutu · iki işçi · büfe üstü, masa ortası")

F["42'"] = dict(mom="the dining room is finished: the walnut table with ten chairs under the bronze chandelier, the sideboard with its painting, the display cabinet and the linen curtains.",
                act=f"Outside the glass doors {KADRO} lift the rolled membrane onto the low flat cart and wheel it away along the veranda.")

# ═══ ODA 5 · MUTFAK (K) · S42–S53 ══════════════════════════════════════════
F[42] = dict(mom="the kitchen lies dim and ruined, and through the doorway the finished dining room shows.",
             act=f"At the left wall {KADRO} pull the old broken base cabinets off the wall and lift them onto a low flat cart at the service door, a pry bar and a drill on the floor.")
S[42] = dict(title="SÖKÜM", ne="Eski alt dolaplar sökülüp servis kapısından çıkarılır; tesisat duvarı ve kapı açıklıkları değişmez.",
             mf="The two workers carry the broken cabinets and the cracked worktop from the left wall out through the service door onto the low flat cart.",
             flow="Piece by piece the old units come off the wall and go out, until the left wall stands stripped to its old pipe stubs and the floor is swept.",
             son="Sol duvar çıplak · kapılar aynı", ses="levye, kırılan sunta", kilit="tesisat duvarı sabit",
             bes="sol duvardaki eski dolaplar · iki işçi · servis kapısındaki araba")

F[43] = dict(mom="the left wall stands stripped, and the walls are stained and cracked.",
             act=f"By the right wall {KADRO} set a stepladder and spread plaster over the cracks from a bucket on the low flat cart, rolling soft cream paint behind it.")
S[43] = dict(title="DUVAR VE BOYA", ne="Duvar yüzeyleri onarılıp krem bitiş rengine getirilir.",
             mf="The two workers carry plaster and paint from the low flat cart to the walls and spread them onto the cracked surfaces, from the right wall round to the left wall.",
             flow="The cracks close and the walls turn an even soft cream wall by wall, and the empty buckets are stacked back on the cart.",
             son="Duvarlar krem · sınırlar aynı", ses="mala, rulo", kilit="—", bes="arabadaki kova · iki işçi · duvarlar")

F[44] = dict(mom="the walls are soft cream, and the floor is still bare grey screed.",
             act=f"At the far wall {KADRO} lift the first large grey-beige stone tiles off a stack on a pallet at the service door and set them on a mortar bed, a low flat cart bringing more.")
S[44] = dict(title="TAŞ ZEMİN", ne="Büyük mat taş zemin plakaları döşenir; tezgâh ve ada yerleri boş.",
             mf="The two workers lay the large matt stone tiles from the stack on the pallet onto a mortar bed, row after row from the far wall towards the camera.",
             flow="The surface grows towards the camera row by row until the bare screed is covered; the empty pallet goes out through the service door on the cart.",
             son="Taş zemin · ada yeri boş", ses="lastik tokmak", kilit="—", bes="kapıdaki palet · iki işçi · harç yatağı")

F[45] = dict(mom="the stone floor is laid, and the far wall between the service door and the doorway is bare.",
             act=f"At the service door {KADRO} lift the first tall walnut pantry module off the low flat cart and walk it upright to the far wall.")
S[45] = dict(title="KİLER DOLAPLARI", ne="Yüksek kiler dolabı bankası modül modül uzak duvara yerleştirilir.",
             mf="The two workers carry the tall walnut pantry modules one at a time from the low flat cart at the service door to the far wall and set them side by side.",
             flow="Module by module the tall walnut bank fills the far wall between the service door and the doorway, each one levelled and fixed to the next.",
             son="Yüksek dolaplar tek duvarda", ses="matkap, menteşe", kilit="tek duvar",
             bes="kapıdaki araba · iki işçi · uzak duvar")

F[46] = dict(mom="the walnut pantry bank fills the far wall.",
             act=f"At the left wall {KADRO} lift the first cream base cabinet off the low flat cart and set it under the window.")
S[46] = dict(title="ALT DOLAPLAR", ne="Taş tezgâhlı alt dolap modülleri sol duvar boyunca dizilir; dolap sayısı ve kapak bölümleri sabit kalır.",
             mf="The two workers carry the cream base cabinets from the low flat cart at the service door to the left wall, set them in a row under the window and lay the pale stone worktop onto them.",
             flow="Cabinet by cabinet the run grows along the left wall, and the long pale stone worktop is lowered onto it in two pieces and joined.",
             son="Alt dolaplar ve tezgâh sol duvarda", ses="tıkırtı, matkap", kilit="kapak bölümleri kilit",
             bes="kapıdaki araba · iki işçi · sol duvar")

F[47] = dict(mom="the base cabinets and worktop line the left wall, and the middle of the floor is bare.",
             act=f"At the service door {KADRO} lift the long walnut island body off a low flat cart and walk it towards the middle of the floor.")
S[47] = dict(title="ADA GÖVDESİ", ne="Büyük ada gövdesi ortaya getirilir; sonda iki işçi daha katılır, taş tezgâh arabada yanına gelir.",
             mf="The two workers carry the walnut island body from the low flat cart at the service door to the middle of the floor and set it down square to the far wall.",
             flow="They level it and fix it to the floor. Late in the shot two more workers in the same clothes help wheel the thick pale stone top in on a low flat cart, lying flat on a padded board with lifting slings under it, and stop beside the island.",
             son="Ada gövdesi ortada, üstü boş · taş tezgâh arabada yanında", ses="tekerlek, nefes",
             kilit="geç teslimat", bes="kapıdaki araba · iki işçi · zeminin ortası")

F[48] = dict(mom="the thick stone top lies on a low flat cart beside the bare walnut island.",
             act=f"Beside the island {KADRO4} lift the thick pale stone top off the low flat cart on four lifting slings, one at each corner, and raise it slowly above the island.")
S[48] = dict(title="TAŞ TEZGÂH · PİLOT", ne="GERÇEK ZAMAN · dört işçi kalın taş tezgâhı sapanlarla gövdeye indirir. PİLOT.",
             mf="Four workers lift the thick stone top from the low flat cart on four slings and lower it onto the walnut island body.",
             flow="From the first frame the stone is already rising off the cart; the four shuffle it over the island, line up its square edge with the body and lower it until it sits flat, then slip the slings out from under it and step back.",
             son="Ada tek parça; tezgâh kenarı, kalınlığı, boyu sabit", ses="taşın ahşaba oturuşu, nefes",
             kilit="GERÇEK ZAMAN · PİLOT", bes="arabadaki taş · dört işçi, sapan · ada gövdesi")

F[49] = dict(mom="the stone-topped island stands in the middle of the floor.",
             act=f"At the left wall {KADRO} lift the first pale stone panel off a stack on the low flat cart and set it on the wall between the worktop and the window.")
S[49] = dict(title="TAŞ PANELLER", ne="Tezgâh arası taş paneller sol duvara takılır.",
             mf="The two workers carry the pale stone panels from the stack on the low flat cart to the left wall and fix them onto the wall between the worktop and the window.",
             flow="Panel by panel the pale stone spreads along the wall above the worktop, its soft veins lining up.",
             son="Taş paneller yerinde", ses="taş, yapıştırıcı", kilit="taş deseni sabit",
             bes="arabadaki istif · iki işçi · tezgâh arası")

F[50] = dict(mom="pale stone panels line the wall above the worktop, and the niche in the right wall is empty.",
             act=f"At the service door {KADRO} lift the tall built-in refrigerator off the low flat cart and walk it upright towards the niche in the right wall.")
S[50] = dict(title="BUZDOLABI", ne="Büyük buzdolabı sağ duvardaki boşluğa yerleştirilir.",
             mf="The two workers carry the tall refrigerator from the low flat cart at the service door to the niche in the right wall and slide it into the niche.",
             flow="They ease it in, level it and fit its plain cream panel doors so they line up with the cabinets.",
             son="Buzdolabı yerinde · ön yüzü dolap çizgisinde", ses="tekerlek, tık", kilit="dolap çizgisi",
             bes="kapıdaki araba · iki işçi · sağ duvar nişi")

F[51] = dict(mom="the refrigerator stands in its niche.",
             act=f"At the service door {KADRO} lift the double wall oven off the low flat cart and carry it towards the tall cabinet beside the refrigerator.")
S[51] = dict(title="ÇİFT FIRIN", ne="Çift fırın ünitesi ayrılmış dolap yuvasına yerleştirilir; yeni dolap oluşmaz.",
             mf="The two workers carry the double oven from the low flat cart at the service door to the tall cabinet beside the refrigerator and slide it into its slot.",
             flow="It slides home and is fixed flush with the cabinet front, and the empty cart goes back out of the service door.",
             son="Tek fırın ünitesi", ses="metal kızak", kilit="yeni dolap yok",
             bes="kapıdaki araba · iki işçi · dolap yuvası")

F[52] = dict(mom="the double oven sits in its cabinet, and the near side of the island is empty.",
             act=f"At the service door {KADRO} lift the first walnut bar stool off the low flat cart and carry it to the near side of the island.")
S[52] = dict(title="İKİ TABURE", ne="İlk iki bar taburesi adanın oturma kenarına; tam iki.",
             mf="The two workers carry two walnut bar stools from the low flat cart at the service door to the near side of the island and set them down.",
             flow="One stool each, set down evenly spaced, so exactly two stools stand at the island.",
             son="Tam iki tabure", ses="ayak sesi", kilit="sayı 2", bes="kapıdaki araba · iki işçi · ada kenarı")

F[53] = dict(mom="two stools stand at the island.",
             act=f"At the service door {KADRO} lift two more walnut bar stools off the low flat cart, a boxed coffee machine waiting beside them.")
S[53] = dict(title="DÖRT TABURE · KAHVE", ne="İkinci tabure çifti gelir; sonda tek kahve makinesi tezgâha konur. Mutfak tamam.",
             mf="The two workers carry two more bar stools from the low flat cart to the island, then lift the coffee machine from its box onto the worktop.",
             flow="The four stools stand in an even row; the coffee machine is set on the worktop by the window. The workers roll up the membrane and wheel the cart out of the service door.",
             son="Dört tabure · ada, kiler, cihazlar, tezgâh tamam", ses="servis kapısının kapanışı",
             kilit="sayı 4 · mutfak sonu", bes="kapıdaki araba · iki işçi · ada kenarı, tezgâh")

F["54'"] = dict(mom="the kitchen is finished: the pantry bank, the base run and worktop with its stone panels, the refrigerator and oven, and the stone-topped island with four stools.",
                act=f"At the service door {KADRO} lift the rolled membrane onto the low flat cart and wheel it out into the side garden.")

# ═══ ODA 6 · ANA YATAK ODASI (M) · S54–S65 ═════════════════════════════════
F[54] = dict(mom="the main bedroom lies dim and ruined, an old iron bed against its far wall.",
             act=f"At the far wall {KADRO} lift the old iron bed frame and its sagging mattress off the floor and carry them towards a low flat cart inside the corridor door.")
S[54] = dict(title="ESKİ YATAK ÇIKAR", ne="Eski yatak çerçevesi koridor kapısından çıkarılır; yatak duvarı, pencere ve kapılar aynı.",
             mf="The two workers carry the old bed frame, the mattress and the debris from the floor out through the corridor door onto the low flat cart.",
             flow="Load by load the room empties, the mattress first, then the iron frame in two pieces, then barrows of debris, until the floor lies bare and swept.",
             son="Oda boş · kapı, pencere, giyinme kapısı aynı", ses="demir şangırtısı", kilit="—",
             bes="uzak duvardaki eski yatak · iki işçi · koridor kapısındaki araba")

F[55] = dict(mom="the bedroom is empty, its walls cracked and stained.",
             act=f"By the right wall {KADRO} set a stepladder and spread plaster over the cracks from a bucket on the low flat cart, rolling warm greige paint behind it.")
S[55] = dict(title="DUVAR VE GREJ", ne="Duvarlar onarılıp sakin sıcak greje getirilir.",
             mf="The two workers carry plaster and paint from the low flat cart to the walls and spread them onto the cracked surfaces, wall by wall.",
             flow="The cracks close and the walls turn an even calm greige, and the empty buckets are stacked back on the cart.",
             son="Duvar bitişi tamam", ses="mala, rulo", kilit="—", bes="arabadaki kova · iki işçi · duvarlar")

F[56] = dict(mom="the walls are calm greige, and the floor is still bare grey screed.",
             act=f"Along the far wall {KADRO} lift the first pale oak boards off a stack on the low flat cart and set the first row, a trestle workbench by the left wall.")
S[56] = dict(title="MEŞE PARKE", ne="Meşe parke uzak duvardan kameraya doğru döşenir.",
             mf="The two workers lay the pale oak boards from the stack on the low flat cart onto the screed, row after row from the far wall towards the camera.",
             flow="The boards advance in one direction, each cut to length at the workbench, until the whole room is oak.",
             son="Meşe zemin, bu kameraya göre sabit yön", ses="testere, tokmak", kilit="döşeme yönü",
             bes="arabadaki istif · iki işçi, tezgâh · şap")

F[57] = dict(mom="the oak floor is down, and the far wall is plain greige.",
             act=f"At the far wall {KADRO} lift the wide upholstered headboard panel off the low flat cart and walk it upright towards the middle of the wall.")
S[57] = dict(title="BAŞLIK", ne="Geniş döşemeli başlık paneli uzak duvarın ortasına monte edilir.",
             mf="The two workers carry the wide headboard panel from the low flat cart to the far wall and fix it onto the middle of the wall.",
             flow="They lift it onto its wall rail, centre it and fix it level; the corridor door at the left end stays clear.",
             son="Başlık duvarı ölçüsü değişmez", ses="matkap", kilit="başlık ortalı",
             bes="arabadaki panel · iki işçi · uzak duvar ortası")

F[58] = dict(mom="the greige headboard covers the middle of the far wall.",
             act=f"Under the tall window {KADRO} set a stepladder and lift a bundle of folded linen curtains off the low flat cart.")
S[58] = dict(title="PERDELER", ne="Tavandan yere perdeler sabit kornişe asılır; pencere ölçüsü ve konumu değişmez.",
             mf="The two workers carry the folded linen curtains from the low flat cart to the tall window in the right wall and hang them from the rod, ceiling to floor.",
             flow="The linen falls in soft folds at both sides of the window, which keeps its size and place.",
             son="Perdeler asılı", ses="halka şıkırtısı", kilit="pencere ölçüsü sabit",
             bes="arabadaki demet · iki işçi, merdiven · pencere")

F[59] = dict(mom="curtains hang at the tall window, and the floor in front of the headboard is bare oak.",
             act=f"Inside the corridor door {KADRO} lift a big rolled grey rug off the low flat cart and set it down in front of the headboard, ready to unroll.")
S[59] = dict(title="HALI", ne="Büyük halı serilir; sonda iki işçi daha katılır, yatak gövdesi kapıdan gelir. Bölüm 2 sonu.",
             mf="The two workers carry the rolled grey rug from the low flat cart to the space in front of the headboard and unroll it towards the camera.",
             flow="The rug opens flat and is squared to the headboard. Late in the shot two more workers in the same clothes help carry the king-size bed base in on its side through the corridor door and lay it flat on a low flat cart just inside the door.",
             son="Halı yerinde · yatak gövdesi arabada, kapının içinde · BÖLÜM 2 sonu (480,0 sn)", ses="halı, nefes",
             kilit="BÖLÜM SINIRI KARESİ G60 · geç teslimat", bes="arabadaki rulo · iki işçi · başlığın önü")

F[60] = dict(mom="the king-size bed base lies flat on a low flat cart just inside the corridor door.",
             act=f"Inside the corridor door {KADRO4} lift the king-size bed base off the low flat cart, two at each side, and carry it slowly towards the headboard.")
S[60] = dict(title="KING YATAK", ne="GERÇEK ZAMAN · dört işçi king yatak gövdesini başlığa ortalar.",
             mf="Four workers lift the king-size bed base from the low flat cart at the corridor door, carry it to the headboard and set it down centred on the rug.",
             flow="From the first frame the base is already lifting off the cart; the four carry it in short careful steps, turn it square to the headboard and lower it until its feet stand on the rug, then step back to the sides.",
             son="Yatak gövdesi başlığa ortalı", ses="ahşabın halıya inişi, nefes", kilit="GERÇEK ZAMAN · BÖLÜM 3 ilk sahnesi",
             bes="kapıdaki araba · dört işçi · başlığın önü")

F[61] = dict(mom="the bed base stands centred on the headboard.",
             act=f"At the corridor door {KADRO} lift the thick mattress off the low flat cart and carry it towards the bed base, white linen folded on the cart.")
S[61] = dict(title="ŞİLTE VE NEVRESİM", ne="Şilte gövdeye konur; sonda nevresim ve yastıklar düzenlenir.",
             mf="The two workers carry the thick mattress from the low flat cart at the corridor door to the bed and lower it onto the base, then lay the white linen and pillows onto it.",
             flow="The mattress settles on the base; the sheets are spread and tucked, the cover is laid smooth and the pillows are set against the headboard.",
             son="Tek yatak, sabit örtü düzeni", ses="kumaş", kilit="yatak ölçüsü sabit",
             bes="kapıdaki araba · iki işçi · yatak gövdesi")

F[62] = dict(mom="the bed is made up in white linen.",
             act=f"At the corridor door {KADRO} lift the first walnut bedside table off the low flat cart and carry it to the left side of the bed.")
S[62] = dict(title="KOMODİNLER", ne="İki komodin sırayla yatağın iki yanına; sonda iki abajur. Toplam iki + iki.",
             mf="The two workers carry the two walnut bedside tables one at a time from the low flat cart at the corridor door to the two sides of the bed, then set one small lamp onto each.",
             flow="The left table goes down first, then the right; one small lamp is set on each, unlit, so two tables and two lamps flank the bed.",
             son="İki komodin, iki abajur", ses="ayak sesi", kilit="sayı 2 + 2", bes="kapıdaki araba · iki işçi · yatak iki yanı")

F[63] = dict(mom="two bedside tables with lamps flank the bed.",
             act=f"At the corridor door {KADRO} lift a long upholstered bench off the low flat cart and carry it towards the foot of the bed.")
S[63] = dict(title="YATAK UCU BANKI", ne="Yatak ucuna uzun döşemeli bank; geçişler açık.",
             mf="The two workers carry the long bench from the low flat cart at the corridor door to the foot of the bed and set it down across it.",
             flow="They square it to the bed, leaving the walkways at both sides open.",
             son="Bank yatak ucunda, geçişler açık", ses="ahşap", kilit="—", bes="kapıdaki araba · iki işçi · yatak ucu")

F[64] = dict(mom="the bench stands across the foot of the bed.",
             act=f"At the corridor door {KADRO} lift a large cream chaise longue off the low flat cart and carry it towards the window.")
S[64] = dict(title="ŞEZLONG", ne="Pencere yanına büyük şezlong; dinlenme köşesi oluşur.",
             mf="The two workers carry the chaise longue from the low flat cart at the corridor door to the window in the right wall and set it down beside the curtains.",
             flow="They angle it towards the window and step back; a quiet reading corner forms by the light.",
             son="Dinlenme köşesi", ses="kumaş", kilit="—", bes="kapıdaki araba · iki işçi · pencere yanı")

F[65] = dict(mom="the chaise longue stands by the window.",
             act=f"At the corridor door {KADRO} lift a slim walnut dressing table off the low flat cart, its small upholstered stool waiting on the cart.")
S[65] = dict(title="MAKYAJ KONSOLU", ne="Makyaj konsolu ve tek pufu sırayla sol duvara; yatak odası tamam.",
             mf="The two workers carry the dressing table from the low flat cart at the corridor door to the left wall, then set its small stool in front of it.",
             flow="The table is set against the left wall beyond the doorway and the stool tucked under it. The workers roll up the membrane and wheel the cart out through the corridor door.",
             son="Yatak, komodinler, bank, şezlong, makyaj alanı tamam", ses="kapının kapanışı", kilit="ayna yok · oda sonu",
             bes="kapıdaki araba · iki işçi · sol duvar")

F["66'"] = dict(mom="the main bedroom is finished: the made bed on its rug, two bedside tables with lamps, the bench, the chaise longue and the dressing table.",
                act=f"At the corridor door {KADRO} lift the rolled membrane onto the low flat cart and wheel it out into the corridor.")

# ═══ ODA 7 · GİYİNME ODASI (W) · S66–S72 ═══════════════════════════════════
F[66] = dict(mom="the dressing room lies dim, sagging old shelves along both long walls.",
             act=f"Along the left wall {KADRO} pull the sagging old shelves off the wall and lift the boards onto a low flat cart in the bedroom doorway.")
S[66] = dict(title="RAFLAR SÖKÜLÜR", ne="Eski açık raflar sökülüp yatak odası kapısından çıkarılır; iki uzun duvar boşalır.",
             mf="The two workers carry the old shelf boards and brackets from both long walls out through the bedroom doorway onto the low flat cart.",
             flow="Shelf by shelf both long walls are stripped and the floor is swept, until both walls stand bare.",
             son="İki uzun duvar boş", ses="çivi gıcırtısı, tahta", kilit="—", bes="duvarlardaki raflar · iki işçi · kapıdaki araba")

F[67] = dict(mom="both long walls stand bare and stained.",
             act=f"By the right wall {KADRO} set a stepladder and roll pale warm white paint from tins on the low flat cart onto the walls.")
S[67] = dict(title="BOYA", ne="Duvarlar sıcak açık renge boyanır; iki uzun duvar aynı.",
             mf="The two workers roll pale warm white paint from the tins on the low flat cart onto the walls, the right wall first, then the left.",
             flow="The stains go under an even pale white, and the empty tins are stacked back on the cart.",
             son="Duvarlar açık renk", ses="rulo", kilit="—", bes="arabadaki boya · iki işçi · duvarlar")

F[68] = dict(mom="the walls are pale warm white, and the floor is still bare grey screed.",
             act=f"At the far end {KADRO} lift the first pale oak boards off a stack on the low flat cart and set the first row, a trestle workbench by the far wall.")
S[68] = dict(title="MEŞE ZEMİN", ne="Meşe zemin döşenir; orta ada yeri boş.",
             mf="The two workers lay the pale oak boards from the stack on the low flat cart onto the screed, row after row from the far wall towards the camera.",
             flow="The boards advance down the long room until the whole floor is oak.",
             son="Meşe zemin · ada yeri boş", ses="testere, tokmak", kilit="—", bes="arabadaki istif · iki işçi · şap")

F[69] = dict(mom="the oak floor is down, and both long walls stand bare.",
             act=f"In the bedroom doorway {KADRO} lift the first tall walnut wardrobe unit off the low flat cart and walk it upright towards the left wall.")
S[69] = dict(title="SOL GARDIROP", ne="Sol yüksek gardırop modülleri yerleştirilir; modül adedi ve raf düzeni sabit kalır.",
             mf="The two workers carry the tall walnut wardrobe units one at a time from the low flat cart in the doorway to the left wall and set them side by side.",
             flow="Unit by unit the walnut wall grows along the left side, each one levelled and fixed to the next.",
             son="Sol gardırop duvarı tam", ses="menteşe, matkap", kilit="modül sayısı kilit",
             bes="kapıdaki araba · iki işçi · sol duvar")

F[70] = dict(mom="a wall of walnut wardrobes lines the left side.",
             act=f"In the bedroom doorway {KADRO} lift the first matching walnut wardrobe unit off the low flat cart and walk it upright towards the right wall.")
S[70] = dict(title="SAĞ GARDIROP", ne="Sağ gardırop bankası düz ceviz kapaklarla yerleştirilir (aynasız).",
             mf="The two workers carry the matching walnut wardrobe units one at a time from the low flat cart in the doorway to the right wall and set them side by side.",
             flow="Unit by unit the right wall fills, its plain walnut doors matching the left side exactly.",
             son="İki gardırop duvarı eş · ayna yok", ses="menteşe", kilit="ayna yok (sahip kararı)",
             bes="kapıdaki araba · iki işçi · sağ duvar")

F[71] = dict(mom="walnut wardrobes line both long walls, and the middle of the floor is bare.",
             act=f"In the bedroom doorway {KADRO} lift the long low walnut island with drawers off the low flat cart and carry it towards the middle of the room.")
S[71] = dict(title="ORTA ADA", ne="Geniş çekmeceli orta ada getirilir; iki gardıroba eşit geçiş.",
             mf="The two workers carry the long walnut island from the low flat cart in the doorway to the middle of the floor and set it down with an equal walkway at each side.",
             flow="They square it down the length of the room so the two walkways match.",
             son="Ada ortada, eşit geçişler", ses="ahşap", kilit="eşit geçiş", bes="kapıdaki araba · iki işçi · zeminin ortası")

F[72] = dict(mom="the walnut island stands in the middle of the room.",
             act=f"In the bedroom doorway {KADRO} lift a long upholstered bench off the low flat cart, stacks of folded clothes and plain linen boxes waiting on a second cart.")
S[72] = dict(title="BANK VE KIYAFETLER", ne="Oturma bankı adanın önüne; sonda katlı kıyafetler ve kutular açık raflara. Giyinme odası tamam.",
             mf="The two workers carry the long bench from the low flat cart to the near end of the island, then lift the folded clothes and boxes from the second cart onto the open shelves.",
             flow="The bench is set down clear of the island; neat stacks of folded clothes and plain linen boxes go onto the open shelves at the ends of the wardrobes, the same few groups on each side. The workers roll up the membrane and wheel the carts out.",
             son="Bank ve ada ayrı · raflarda sabit sayıda grup", ses="kumaş", kilit="raflar çoğalmaz · oda sonu",
             bes="kapıdaki iki araba · iki işçi · ada ucu, açık raflar")

F["73'"] = dict(mom="the dressing room is finished: two walls of walnut wardrobes, the island with its bench, and folded clothes on the open shelves.",
                act=f"In the bedroom doorway {KADRO} lift the rolled membrane onto the low flat cart and wheel it out through the bedroom.")

# ═══ ODA 8 · BANYO (B) · S73–S79 ═══════════════════════════════════════════
F[73] = dict(mom="the main bathroom lies stripped, broken old tiles and rubble heaped on its floor.",
             act=f"In the middle of the floor {KADRO} shovel the rubble into buckets and lift the full buckets onto a low flat cart in the doorway.")
S[73] = dict(title="MOLOZ ÇIKAR", ne="Önceden boşaltılmış banyoda kalan moloz çıkarılır; küvet ve dolap yerleri boş, duş nişi yerinde.",
             mf="The two workers carry the rubble in buckets from the floor out through the doorway onto the low flat cart.",
             flow="Bucket after bucket the heaps go out until the floor lies bare and swept.",
             son="Zemin temiz · duş nişi yerinde", ses="kürek, kova", kilit="duş nişi sabit",
             bes="zemindeki moloz · iki işçi · kapıdaki araba")

F[74] = dict(mom="the bathroom is empty, its walls bare grey plaster.",
             act=f"At the far wall {KADRO} lift the first large pale stone slab off a stack on the low flat cart and set it against the wall beside the window, a trestle workbench by the left wall.")
S[74] = dict(title="TAŞ DUVARLAR", ne="Büyük taş duvar plakaları monte edilir; damarlar ve duş nişi sabitlenir.",
             mf="The two workers carry the large pale stone slabs from the stack on the low flat cart to the walls and fix them onto the plaster, from the far wall round to the side walls.",
             flow="Slab by slab the pale veined stone climbs the walls to the ceiling, around the window and into the shower niche, its soft grey veins lining up.",
             son="Duvarlar taş · damarlar sabit", ses="taş, yapıştırıcı", kilit="duvar damarları kilit",
             bes="arabadaki istif · iki işçi · duvarlar")

F[75] = dict(mom="pale stone clads the walls, and the floor is still bare grey screed.",
             act=f"At the far end {KADRO} lift the first matt stone tiles off a stack on the low flat cart and set them on a mortar bed.")
S[75] = dict(title="TAŞ ZEMİN", ne="Mat taş zemin döşenir; yön ve derz çizgileri sabit kalır.",
             mf="The two workers lay the matt stone tiles from the stack on the low flat cart onto a mortar bed, row after row from the window towards the camera.",
             flow="The surface grows towards the camera until the screed is covered, its joints running straight.",
             son="Zemin taş · derz yönü kilit", ses="lastik tokmak", kilit="derz çizgileri", bes="arabadaki istif · iki işçi · harç yatağı")

F[76] = dict(mom="the stone floor is laid, and the right wall is bare stone.",
             act=f"In the doorway {KADRO} lift the long walnut vanity off the low flat cart and carry it towards the right wall.")
S[76] = dict(title="ÇİFT LAVABO", ne="Çift lavabolu dolap, üstüne iki aplik (ayna yerine); sonda iki işçi daha katılır, küvet gelir.",
             mf="The two workers carry the long walnut vanity from the low flat cart in the doorway to the right wall and set it against the stone, then fix two bronze wall lights onto the wall above it.",
             flow="The vanity with its one stone top and two basins is levelled and fixed; two small bronze wall lights go up above it, unlit. Late in the shot two more workers in the same clothes help wheel the freestanding bathtub in through the doorway on a low flat cart and stop just inside.",
             son="Tek dolap bankası, iki lavabo, iki aplik · küvet arabada kapının içinde", ses="tekerlek, nefes",
             kilit="ayna yok — aplik (sahip kararı) · geç teslimat", bes="kapıdaki araba · iki işçi · sağ duvar")

F[77] = dict(mom="the white bathtub waits on a low flat cart just inside the doorway.",
             act=f"Just inside the doorway {KADRO4} lift the freestanding white bathtub off the low flat cart, two at each side, and carry it slowly towards the window.")
S[77] = dict(title="KÜVET", ne="GERÇEK ZAMAN · dört işçi bağımsız küveti pencerenin önüne koyar.",
             mf="Four workers lift the white bathtub from the low flat cart in the doorway, carry it to the window and set it down on the stone in front of the window.",
             flow="From the first frame the tub is already lifting off the cart; the four carry it in short careful steps, turn it parallel to the window and lower it onto its base, then step back.",
             son="Tek küvet, sabit yer", ses="seramiğin taşa inişi, nefes", kilit="GERÇEK ZAMAN",
             bes="kapıdaki araba · dört işçi · pencerenin önü")

F[78] = dict(mom="the bathtub stands in front of the window.",
             act=f"Beside the tub {KADRO} lift the slim bronze floor tap out of its box on the low flat cart and set it on the outlet in the floor, a drill and a spanner beside it.")
S[78] = dict(title="BATARYA", ne="Küvet yanındaki zemin bataryası mevcut çıkışa monte edilir; su gösteri değildir.",
             mf="The two workers carry the floor tap from its box on the low flat cart to the outlet beside the tub and fix it onto the outlet.",
             flow="They seat it plumb, tighten it and wipe it, and the empty box goes back onto the cart.",
             son="Batarya tek ve sabit", ses="anahtar tıkırtısı", kilit="su akışı yok", bes="arabadaki kutu · iki işçi · zemin çıkışı")

F[79] = dict(mom="the bronze tap stands beside the tub.",
             act=f"In the doorway {KADRO} lift an upholstered bench off the low flat cart, a stack of folded white towels waiting beside it.")
S[79] = dict(title="BANK VE HAVLULAR", ne="Döşemeli banyo bankı sol duvara; sonda katlı havlular. Banyo tamam.",
             mf="The two workers carry the bench from the low flat cart in the doorway to the left wall beside the shower niche, then lay the folded towels onto it.",
             flow="The bench is set down beside the niche and the white towels are stacked on it. The workers roll up the membrane and wheel the cart out.",
             son="Küvet, dolap, aplikler, bank, duş nişi tamam", ses="kumaş", kilit="banyo sonu",
             bes="kapıdaki araba · iki işçi · sol duvar")

F["80'"] = dict(mom="the main bathroom is finished: pale stone walls, the double vanity with its two wall lights, the white tub with its bronze tap, and the bench with towels.",
                act=f"In the doorway {KADRO} lift the rolled membrane onto the low flat cart and wheel it out through the dressing room.")

# ═══ ODA 9 · VERANDA (T) · S80–S85 ═════════════════════════════════════════
F[80] = dict(mom="the back of the villa in low evening sun: the covered veranda is cracked concrete under weeds, and through the glass doors the finished salon and dining room show.",
             act=f"On the veranda {KADRO} lift the first warm brown decking boards off a stack on the low flat cart at the left end and set the first row along the back wall, a trestle workbench beside the cart.")
S[80] = dict(title="AHŞAP DÖŞEME", ne="Mevcut üstü örtülü verandaya ahşap döşeme sıralar hâlinde serilir; kolonlar ve tavan değişmez.",
             mf="The two workers lay the decking boards from the stack on the low flat cart onto the veranda in rows, from the back wall out to the step.",
             flow="The weeds and leaves are swept off first; then row by row the warm boards cover the old concrete from left to right, each cut at the workbench, until the whole veranda is timber.",
             son="Ahşap veranda · kolonlar ve tavan aynı", ses="testere, tokmak, akşam kuşları",
             kilit="kolon ve tavan sabit", bes="arabadaki tahta istifi · iki işçi · eski beton")

F[81] = dict(mom="the veranda is new timber, and its floor stands empty.",
             act=f"From the lawn at the left {KADRO} lift the first grey cushioned sofa module off the low flat cart and carry it up the step onto the veranda.")
S[81] = dict(title="DIŞ KANEPE", ne="Büyük dış mekân kanepesi modülleri sırayla getirilir; tek oturma grubu oluşur.",
             mf="The two workers carry the grey sofa modules one at a time from the low flat cart on the lawn onto the veranda and set them side by side in the middle.",
             flow="Module by module the long sofa forms, facing the garden, its cushions plumped.",
             son="Tek oturma grubu", ses="kumaş, ayak sesi ahşapta", kilit="tek grup", bes="çimdeki araba · iki işçi · verandanın ortası")

F[82] = dict(mom="the outdoor sofa stands in the middle of the veranda.",
             act=f"From the lawn {KADRO} lift the first wide outdoor armchair off the low flat cart and carry it up the step.")
S[82] = dict(title="İKİ KOLTUK", ne="İki geniş dış mekân koltuğu sırayla; tam iki.",
             mf="The two workers carry the two wide armchairs one at a time from the low flat cart on the lawn onto the veranda and set them facing the sofa.",
             flow="One chair per trip, both set facing the sofa, so exactly two armchairs stand on the veranda.",
             son="Tam iki koltuk", ses="ayak sesi", kilit="sayı 2", bes="çimdeki araba · iki işçi · kanepenin karşısı")

F[83] = dict(mom="two armchairs face the sofa.",
             act=f"From the lawn {KADRO} lift a big low outdoor table off the low flat cart and carry it up the step.")
S[83] = dict(title="DIŞ SEHPA", ne="Büyük dış mekân orta sehpası oturma grubunun ortasına.",
             mf="The two workers carry the big low table from the low flat cart on the lawn onto the veranda and set it down between the sofa and the armchairs.",
             flow="They centre it in the group and step back.", son="Sehpa grubun merkezinde", ses="ahşap", kilit="—",
             bes="çimdeki araba · iki işçi · grubun ortası")

F[84] = dict(mom="the seating group is complete around its table.",
             act=f"From the lawn {KADRO} lift a long timber bench off the low flat cart and carry it up the step towards the back wall at the right.")
S[84] = dict(title="UZUN BANK", ne="Uzun ahşap bank arka duvarın önüne; açık geçiş korunur.",
             mf="The two workers carry the long bench from the low flat cart on the lawn onto the veranda and set it down against the back wall at the right.",
             flow="They set it between two glass doors so the doors and the walkway stay clear; the sun sinks low behind the camera.",
             son="Bank arka duvarda · geçiş açık", ses="ahşap", kilit="geçiş açık", bes="çimdeki araba · iki işçi · arka duvar")

F[85] = dict(mom="the sun is setting behind the camera, and the veranda furniture stands in the last warm light.",
             act=f"From the lawn {KADRO} lift the first big stone planter with an olive shrub off the low flat cart and set it at the outer edge of the veranda.")
S[85] = dict(title="SAKSILAR · IŞIKLAR", ne="İki büyük saksı sırayla; sonda güneş batarken mevcut veranda aydınlatması yanar.",
             mf="The two workers carry the two stone planters one at a time from the low flat cart on the lawn to the outer edge of the veranda, and late in the shot the wall lights come on.",
             flow="The planters are set at the two outer corners; the sun goes down behind the camera, and late in the shot the wall lights on the back wall come on all at once and stay on. The workers wheel the empty cart off across the lawn.",
             son="Tamamlanmış veranda, sıcak ışık, bütün mobilya aynı karede", ses="taş, akşam ağustosböcekleri",
             kilit="ışık tek karede yanar (ISIK_FINALI)", bes="çimdeki araba · iki işçi · veranda köşeleri")

F["86'"] = dict(mom="sunset has passed: the veranda is finished and its wall lights are lit, the furniture set out under the timber roof.",
                act=f"On the lawn at the left {KADRO} lift the folded stepladder onto the low flat cart and wheel it towards the house.")

# ═══ ODA 10 · AKŞAM · S86–S89 (dönüşler) ═══════════════════════════════════
F[86] = dict(mom="dusk after sunset; the finished entrance hall is dim, the chandelier unlit, both door leaves open to the darkening garden.",
             act=f"In the open doorway {KADRO} lift the last folded stepladder onto the low flat cart outside, while two people in simple evening clothes come in through the door carrying a crate of food and flowers.")
S[86] = dict(title="TESLİM · AVİZE YANAR", ne="Alacakaranlık: ekip son merdiveni çıkarır, ev sahipleri yemek sandığıyla girer; kapı kapanır, hol avizesi yanar.",
             mf="The two workers carry their last tools from the hall out through the walnut door onto the low flat cart, the two people carry a crate of food in from the door to the dining room, and the bronze chandelier comes on.",
             flow="The workers set the last stepladder on the cart outside and the two people cross the hall with their crate towards the dining room; the walnut door is pulled closed, and the chandelier comes on all at once and stays on, its warm light falling across the travertine.",
             son="Hol avizesi yanık · kapı kapalı", ses="kapının tok sesi, uzak ağustosböceği · müzik inceliyor",
             kilit="ışık tek karede yanar · sahip kararı: final ışıklar", bes="holdeki son aletler · iki işçi, iki kişi · dışarıdaki araba")

F["87'"] = dict(mom="the entrance hall at dusk, the bronze chandelier lit and the walnut door closed.",
                act="The hall stands quiet under the lit chandelier.")

F[87] = dict(mom="dusk; dust sheets cover the salon's sofas and armchairs, the lamps unlit, and through the glass doors the lit veranda shows.",
             act=f"Around the sofas {KADRO} pull the pale dust sheets off the furniture one by one and lift them onto a low flat cart in the opening.")
S[87] = dict(title="ÖRTÜLER KALKAR · LAMBALAR", ne="Son örtüler kanepelerden kalkar, araba dışarı; lambader ve halka ışık yanar.",
             mf="The two workers carry the dust sheets from the sofas and armchairs out through the wide opening onto the low flat cart, and the floor lamp and the ring light come on.",
             flow="Sheet by sheet the cream sofas and cognac armchairs show again; the workers lift the last folded sheet onto the cart and wheel it away through the opening, and the floor lamp and then the ring light come on, each all at once, and stay on.",
             son="Salon lambalı · örtü yok", ses="kumaş hışırtısı · müzik ince",
             kilit="ışık tek karede yanar", bes="mobilyadaki örtüler · iki işçi · açıklıktaki araba")

F["88'"] = dict(mom="the salon at the start of the blue hour, the floor lamp and ring light lit.",
                act="The salon stands quiet under its lamps.")

F[88] = dict(mom="the blue hour begins; the restored front of the villa stands under a deepening sky, the right window lit warm from the salon, the left window dark.",
             act=f"On the path {KADRO} lift the last stepladder onto the low flat cart and wheel it down the path and out of the frame at the left.")
S[88] = dict(title="DIŞ CEPHE · MAVİ SAAT", ne="Açılışla aynı açı: ekip arabayı yoldan çıkarır; yol lambaları ve yemek odası penceresi yanar.",
             mf="The two workers carry the last stepladder from the path onto the low flat cart and wheel it out of the frame, and the path lights and the left window come on.",
             flow="The cart rolls away down the path and out at the left; the low path lights come on all at once along both edges, and then the left window lights up warm from the dining room, so both front windows are lit and stay lit.",
             son="İki pencere yanık, yol ışıkları yanık · açılışla aynı kadraj, karşıt hâl", ses="ağustosböceği, uzak köpek",
             kilit="AÇILIŞ–FİNAL KAFİYESİ · ışık tek karede", bes="yoldaki merdiven · iki işçi · araba (kadraj dışı)")

F["89'"] = dict(mom="the blue hour: both front windows lit warm, the path lights on, the walnut door closed.",
                act="The garden stands still and empty.")

F[89] = dict(mom="the blue hour; the dining room is lit by its chandelier, the table laid for two at its far end, and two people stand beside their chairs; beyond the glass doors the lit veranda.",
             act="At the far end of the table the two people in simple evening clothes pull two chairs back from the table and lower themselves onto them.")
S[89] = dict(title="İLK AKŞAM YEMEĞİ", ne="İki kişi avizenin altında masaya oturur (gerçek hız, 0–4 sn), sonra tutuş. İlk akşam yemeği.",
             mf="The two people pull their chairs back from the far end of the table and sit down to the first dinner in the house.",
             flow="From the first frame to about four seconds the two people draw out the two side chairs nearest the far end of the table and sit, facing each other across the table. From about four to eight seconds the two people sit still at the table, the chandelier stays lit and nothing else changes.",
             son="USTA KARE G90 — iki kişi sofrada, avize yanık, on sandalye, camların ardında yanık veranda", ses="sandalyelerin taşta hafif sürtmesi, tabak tıkırtısı · müzik tutulan akorla biter",
             kilit="İŞLEV ANI · 4 + 4 · kapak kaynağı", bes="masa başında ayakta · iki kişi · sandalyeler")

# dönüş karelerinin defter değişiklikleri: (segment, 'bas' | 'son') → (degis, ek)
DONUS = {
    ("H2", "bas"): ({"kapi": "Both leaves of the walnut door stand open to the darkening garden.",
                     "isik": "The large bronze chandelier hangs from the ceiling over the middle of the hall on a short chain, unlit.",
                     "gecici": "A low flat cart stands just outside the open door, a folded stepladder on it."}, None),
    ("H2", "son"): ({"kapi": "Both leaves of the walnut door are closed.",
                     "isik": "The large bronze chandelier hangs from the ceiling over the middle of the hall on a short chain, lit warm.",
                     "gecici": ""}, None),
    ("L2", "bas"): ({"veranda": "Through the glass doors the finished veranda shows, its wall lights lit.",
                     "gecici": "A low flat cart stands in the opening, a folded stepladder on it."},
                    ["Pale dust sheets are draped over the two sofas and the two armchairs; the floor lamp and the ring light are unlit."]),
    ("L2", "son"): ({"veranda": "Through the glass doors the finished veranda shows, its wall lights lit.",
                     "lamba": "A tall bronze floor lamp, lit warm, stands beside the right sofa, and one young olive tree in a big stone pot stands by the glass doors.",
                     "isik": "A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, lit warm.",
                     "gecici": ""}, None),
    ("A2", "bas"): ({"sag": "The big window right of the arch is a new glazed unit in a slim bronze frame, lit warm from inside.",
                     "sol": "The big window left of the arch is a new glazed unit in a slim bronze frame, dark.",
                     "gecici": "A folded stepladder lies on a low flat cart on the path."}, None),
    ("A2", "son"): ({"sag": "The big window right of the arch is a new glazed unit in a slim bronze frame, lit warm from inside.",
                     "sol": "The big window left of the arch is a new glazed unit in a slim bronze frame, lit warm from inside.",
                     "yol": "The front path is laid with large pale flagstones, its low bronze path lights lit along both edges.",
                     "gecici": "A pair of spades leans on the wall beside the arch."}, None),
    ("D2", "bas"): ({"isik": "A long linear bronze chandelier hangs low over the middle of the room on two chains, lit warm.",
                     "mutfak": "Through the kitchen doorway the finished kitchen shows, softly lit.",
                     "veranda": "Through the glass doors the finished veranda shows, its wall lights lit.",
                     "gecici": ""},
                    ["The far end of the table is laid for two: two plates, two glasses, a jug of water and a basket of bread, set at the two side chairs nearest the far end, facing each other across the table."]),
    ("D2", "son"): ({"isik": "A long linear bronze chandelier hangs low over the middle of the room on two chains, lit warm.",
                     "mutfak": "Through the kitchen doorway the finished kitchen shows, softly lit.",
                     "veranda": "Through the glass doors the finished veranda shows, its wall lights lit.",
                     "gecici": ""},
                    ["The far end of the table is laid for two: two plates, two glasses, a jug of water and a basket of bread, set at the two side chairs nearest the far end, facing each other across the table."]),
}

USTA = ("> ⭐ **İŞLEV ANI ve KAPAK KAYNAĞI.** Mavi saat (20:00, güneş ≈ −7°): yemek odası bronz avizeyle yanık; on kişilik\n"
        "> ceviz masa, on sandalye (iki baş + iki yanda dörder), büfe + tablo, sergi dolabı, keten perdeler. Masanın uzak\n"
        "> ucunda iki kişi oturuyor (yan/arka, yüz okunmaz). Cam kapıların ardında yanık veranda, en altta ufukta son soluk\n"
        "> sıcak bant. Kapak bu karenin METİNSİZ hâlinden türer; başlık sol üst bölgeye (KAPAK §1). ⛔ Yok: işçi, araba,\n"
        "> membran, merdiven, ayna, mum, yazı.")
