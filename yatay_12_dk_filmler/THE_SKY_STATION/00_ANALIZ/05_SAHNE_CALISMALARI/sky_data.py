# -*- coding: utf-8 -*-
"""THE SKY STATION — kare (F) ve klip (S) verisi. F[n] = G(n) karesi (S(n)'nin başı);
S[s] = G(s) → G(s+1) klibi. Plan: THE_SKY_STATION_PLAN.md §SAHNE SAHNE PLAN."""

PERDELER = [
    (1, "PERDE_01_CATI_KALKAR", "ÇATI KALKAR, KABİN ÇIKAR, HARABE TEMİZLENİR", 0, 8),
    (2, "PERDE_02_TAS_CEPHE_MERDIVEN", "TAŞ CEPHELER, GİRİŞ MERDİVENİ, İKİ BİNİŞ TABANI", 9, 17),
    (3, "PERDE_03_MEKANIZMALAR", "ÇATILAR AÇIKKEN AĞIR MEKANİZMALAR VE HAT BAŞLIKLARI", 18, 26),
    (4, "PERDE_04_CATILAR", "İKİ İSTASYONUN ÇATILARI YENİDEN KURULUR", 27, 35),
    (5, "PERDE_05_CAM_VE_PERONLAR", "CAM CEPHELER, AHŞAP PERONLAR, KARŞI SEYİR ALANI", 36, 44),
    (6, "PERDE_06_HALATLAR", "HALATLAR VADİYİ GEÇER, İKİ İSTASYON BAĞLANIR", 45, 53),
    (7, "PERDE_07_KABIN", "AYNI PASLI KABİN YENİLENİR VE HATTA ASILIR", 54, 62),
    (8, "PERDE_08_ILK_GECIS", "BOŞ KABİNİN İLK GEÇİŞİ, ARDINDAN YÜKLE DENEME", 63, 71),
    (9, "PERDE_09_BAHCE_SU_ISIK", "ŞANTİYE TEMİZLENİR; BAHÇE, SU, TERAS, IŞIKLAR", 72, 80),
    (10, "PERDE_10_ILK_YOLCULAR", "İLK ZİYARETÇİLER, BİNİŞ, KARŞI YAMACA VARIŞ", 81, 89),
]

F = {}   # kare: act (ACTIVITY gövdesi — vinç yükü, karşı vinç ve insan kuralı üretici ekler) · mom
S = {}   # klip: title · is (TR) · mf · flow

# ═══ PERDE 1 ═══════════════════════════════════════════════════════════════
F[0] = dict(mom="the first day of work; the first old roof panel has just lifted clear of the near hall, and the rusted cabin still hangs inside.",
            act="The crawler crane in the gravel yard at the left lifts the third roof panel off the hall on four taut slings, the panel already about one metre above the roof line; a rigging crew on the old roof steadies it with taglines, and a flatbed truck backs in beside the crane.")
S[0] = dict(title="SÖKER", ne="Çatının 1. dev paneli (kabin bölmesinin üstü) vinçle kalkar, sola döner, kamyona iner; açılan boşluktan salona sabah ışığı düşer, kemerin ardında paslı kabin okunur.",
            mf="The crawler crane lifts the third roof panel from the roof of the hall, swings it to the left and lowers it onto the bed of the flatbed truck in the gravel yard.",
            flow="From the first frame the panel is already rising: it climbs clear of the roof on its four slings, swings slowly to the left above the yard and settles onto the truck bed, where the crew pull the taglines slack and the crane lowers the panel onto the truck. Morning light pours through the new gap in the roof into the hall, and through the broken glass of the arch the rusted cabin on its old hanger girder shows brighter inside.")

F[1] = dict(mom="the first roof panel lies on the truck bed, and a gap has opened in the roof right over the cabin bay.",
            act="A rigging crew on the truck bed unhooks the four slings from the roof panel, the crawler crane swings its hook back towards the gap in the roof, and the flatbed truck starts to pull away to the left.")
S[1] = dict(title="KABİNİ ÇIKARIR", ne="Kamyon paneli götürür; vinç kancayı açıklıktan içeri indirir, ekip sapanları kabine bağlar; kabin saçağın üstüne çıkar, sola döner, bakım alanındaki çelik beşiğe iner. İLK BÜYÜK SONUÇ.",
            mf="The crawler crane lifts the rusted cabin from its old hanger girder inside the hall, up through the gap in the roof, and lowers it onto the low steel cradle in the front yard left of the stair.",
            flow="The flatbed truck carries the panel away to the left out of the frame. The crane hook drops through the gap; inside, the crew clip four slings to the cabin's roof arm, and the cabin rises slowly up through the roof, clear of the wall heads, swings left over the yard and settles onto the cradle, the crane lowering it the last metre. The slings go slack, and inside the hall the old hanger girder is left bare.")

F[2] = dict(mom="the rusted cabin sits on its cradle in the front yard, and thick ivy still covers the whole face of the hall.",
            act="Two crews in harnesses on lines from the wall heads start to pull the ivy off the left half of the face in long strips, a team below wheels barrows of cut ivy to a skip at the left of the yard, and the crawler crane lifts its hook from the cabin.")
S[2] = dict(title="SARMAŞIĞI SÖKER", ne="İki ekip iple cephenin sol yarısındaki sarmaşığı şerit şerit söker, el arabalarıyla konteynere taşınır; vinç kabinin sapanlarını çözer, panel 2'yi kancaya alır.",
            mf="Two crews in harnesses pull the ivy from the left half of the hall's face in long strips and drop it onto a pile at the wall foot, from where a team carries it in barrows to the skip at the left.",
            flow="Strip by strip, from the wall heads down to the yard, pale limestone streaked with dark stains shows through behind the crews, until the left half of the face is bare stone and the right half is still thick green ivy. Meanwhile the crew unhook the slings from the cabin, and the crane lifts them clear, swings to the roof and hooks the right-end roof panel, raising it just above the roof line.")

F[3] = dict(mom="the left half of the face is bare stone, and the right-end roof panel is lifting off the hall.",
            act="The crawler crane lifts the right-end roof panel off the hall on taut slings, a rigging crew on the wall heads unbolts the next panel, and two flatbed trucks wait their turn in the yard, one reversing into place.")
S[3] = dict(title="PANELLERİ İNDİRİR", ne="Panel 2 ve 3 sırayla kalkar, iki kamyona iner; kamyonlar sırayla soldan çıkar. Salonda yalnız sol uç paneli kalır.",
            mf="The crawler crane lifts the right-end panel and then the second panel from the left off the hall roof and lowers each one onto a flatbed truck in the yard.",
            flow="The first truck carries its panel away to the left out of the frame, the second backs in, takes the next panel and follows it out. Each lift opens more of the hall to the sky, until only the left-end panel remains on its trusses; the crew fix the slings to it and the crane takes its weight.")

F[4] = dict(mom="one old roof panel is left on the near hall, and the far station still sags under its caved-in roof.",
            act="The crawler crane lifts the last, left-end roof panel off the wall heads, a rigging crew guides it with taglines, and a flatbed truck backs in below to take it.")
S[4] = dict(title="KARŞIYA GEÇER", ne="Son panel (4) kalkar, yakın salon çatısız taş kabuk olur. Karşı yamaçta servis yolundan gelen küçük mobil vinç karşı istasyonun çökük çatısını parça parça indirmeye başlar.",
            mf="The crawler crane lifts the last roof panel from the left end of the hall and lowers it onto the waiting flatbed truck, which carries it away to the left.",
            flow="The hall is left as an open stone shell, and the crane swings back and the crew hook a steel rubble bucket onto it. Across the valley, small and distant, the mobile crane drives up the service road beside the far station, plants its outriggers and lifts sections of the caved-in roof off the far station one by one, lowering them onto a trailer on the road, until half of the far roof has gone.")

F[5] = dict(mom="the near hall stands open as a roofless stone shell, still heaped with rubble inside, and half of the far roof has gone.",
            act="A mini excavator inside the roofless hall fills a steel rubble bucket with rubble, rotten timber and broken old machinery, the crawler crane lifts the full bucket over the wall heads towards a tipper truck in the yard, and a gang with brush cutters starts on the scrub in the front yard.")
S[5] = dict(title="MOLOZU BOŞALTIR", ne="Salonun içinde mini ekskavatör ve ekip: moloz, çürük ahşap, kırık eski makine parçaları kovayla vinçten kamyona. Ön bahçede çalılar biçilir.",
            mf="The mini excavator scoops the rubble from the hall floor into the steel bucket, and the crawler crane lifts each full bucket out over the wall heads and tips it into the tipper truck in the yard.",
            flow="The heaps inside the arches shrink load by load until the hall floor lies bare. In the front yard the gang cuts the scrub and long grass down to short stubble and stacks the cut branches by the skip. The full tipper truck drives off to the left and an empty one backs in. Across the valley the small mobile crane lifts the roof sections it has lowered onto the trailer and stacks them flat for the road.")

F[6] = dict(mom="the hall floor is clear and the front yard mown, but the right half of the face is still ivy and the arches still hold broken glass.",
            act="From a mobile work platform a glazing crew knocks the last broken glass and rotten frames out of the arches into a steel crate, two crews in harnesses start on the ivy of the right half of the face, and the crawler crane lifts a full glass crate down towards a truck in the yard.")
S[6] = dict(title="CAMLARI SÖKER", ne="Mobil platformdan kırık cam kemerin kalan camları ve çürük çerçeveler sökülür; cephenin sağ yarısından sarmaşık alınır. Beş kemer boş açıklık kalır (sayı ve yer sabit).",
            mf="From the mobile work platform the crew pull the broken glass and rotten frames out of the five arches into steel crates, and the crawler crane lifts each full crate down onto the truck in the yard.",
            flow="Arch by arch, from the left to the right, the openings come clear. At the same time the two harness crews strip the ivy from the right half of the face onto a pile at the wall foot, and a team carries it to the skip. By the end the whole face is bare stone blotched with grime and the five arches stand as empty openings, still exactly five, in exactly the same places.")

F[7] = dict(mom="the near face is bare and its five arches empty, and across the valley half of the far roof still sags on the walls.",
            act="Across the valley the small mobile crane lifts a section of the remaining far roof; at the near hall a tipper truck takes the last rubble from the skip, a crew sweeps the gravel, and the crawler crane lifts a bundle of scaffold tubes off a truck.")
S[7] = dict(title="İKİ KABUK", ne="Karşı istasyonda çatının kalan yarısı iner; yakında kamyonlar son molozu götürür. Film ilk kez iki boş taş kabuğu yan yana gösterir.",
            mf="Across the valley the small mobile crane lifts the last sections of the caved-in roof from the far station and lowers them onto the trailer on its service road.",
            flow="The far station turns into a roofless stone shell. At the near hall the tipper truck carries the last rubble away to the left, and the crawler crane swings the bundle of scaffold tubes from the truck down to the yard by the face. For the first time both stations stand as open stone shells facing each other across the empty valley.")

F[8] = dict(mom="both stations stand as open, roofless stone shells across the empty valley.",
            act="A scaffolding crew starts to bolt up two scaffold towers against the face of the hall from tube bundles on the gravel, the crawler crane lifts a bundle of scaffold tubes onto the first lift, and a team sweeps the hall floor.")
S[8] = dict(title="HARABE TEMİZ", ne="Cephe önüne iki iskele kulesi kurulur; salonun içi süpürülür; beşikteki kabinin yanına branda ve el aletleri sandığı bırakılır. Karşı mobil vinç ayrılır.",
            mf="The scaffolding crew lift tubes and boards from the bundle the crane has set in the yard and build two scaffold towers up against the face of the hall, one at each side of the middle arch.",
            flow="The towers rise lift by lift up to the wall heads. A team sweeps the hall floor clean, and two workers carry a folded tarpaulin and a tool chest from the truck to the cabin on its cradle and set them down beside it. Across the valley the small mobile crane folds its boom and drives away down the service road out of view.")

# ═══ PERDE 2 ═══════════════════════════════════════════════════════════════
F[9] = dict(mom="the two shells are cleared, and two scaffold towers stand ready against the near face.",
            act="From the two scaffold towers a crew with pressure-washer lances starts to blast the grime off the left half of the face, dirty water running down into the channel at the wall foot; a pump trailer runs in the yard, and the crawler crane lifts a bundle of scaffold boards onto the top of a tower.")
S[9] = dict(title="YIKAR ①", ne="İskeleden basınçlı suyla cephenin sol yarısı yıkanır; koyu kir aşağı akar, ön kanala süzülür. Sol yarı açık krem, sağ yarı gri.",
            mf="From the scaffold towers the crew drive the pressure-washer lances across the left half of the face, from the wall heads down to the yard, washing the dark grime off the stone into the channel at its foot.",
            flow="Band by band the stone of the left half turns from grey to pale cream, and muddy water runs along the channel at the wall foot. A truck delivers pallets of cut limestone blocks, and the crane lifts them from the truck onto a stack by the stair.")

F[10] = dict(mom="the left half of the face is washed pale cream, and the right half is still grey with grime.",
             act="The washing crew moves the lances onto the right half of the face from the towers, a mason marks broken blocks with chalk, and the crawler crane lowers a pallet of cut limestone blocks onto the stack by the stair.")
S[10] = dict(title="YIKAR ②", ne="Sağ yarı yıkanır; taş ustaları kırık blokları tebeşirle işaretler. Bütün cephe temiz krem; kilit taşlarında kırık blok boşlukları okunur.",
             mf="From the scaffold towers the crew drive the pressure-washer lances across the right half of the face, from the middle arch to the right corner and from the wall heads down to the yard.",
             flow="The grey boundary moves steadily to the right until the whole face is pale cream, and the masons chip out the broken blocks round the keystones of the arches and drop them into a skip. The crane lifts another pallet of cut stone from the truck onto the stack.")

F[11] = dict(mom="the whole face is washed pale cream, with a few broken blocks missing round the keystones.",
             act="A forklift carries a pallet of new cut limestone blocks from the stack to the foot of a scaffold tower, masons on the towers raise a block on a small chain hoist, and the crawler crane lifts a pallet up onto the top lift of a tower.")
S[11] = dict(title="TAŞI ONARIR", ne="Forklift paletlerle yeni kesme taş blokları getirir; ustalar iskeledeki makarayla kırık blokları değiştirir. Beş kemer bütün; yeni taşlar biraz açık.",
             mf="The masons lift each new limestone block from the pallet on the scaffold tower with the chain hoist and bed it into the broken gaps round the keystones of the five arches.",
             flow="Gap by gap the arches close again, from the left arch to the right, and the new blocks sit a shade paler than the old stone. The forklift carries more pallets from the stack to the towers, and the crane lifts them up.")

F[12] = dict(mom="the face is clean and whole and the five arches repaired; the old stair is still broken.",
             act="A breaker on a small excavator cracks out the broken old steps of the stair, the crawler crane lifts a steel skip of broken stone towards a tipper truck, a scaffolding crew starts to strip the two towers, and a concrete mixer truck backs up to the stair.")
S[12] = dict(title="MERDİVENİ SÖKER", ne="Giriş merdiveninin kırık eski basamakları kırıcıyla sökülür, ekskavatör yükler; beton taban dökülür. İki iskele kulesi sökülür.",
             mf="The breaker cracks the old steps out of the stair and the excavator loads the broken stone into the skip, and then the mixer truck pours a fresh concrete base from its chute into the timber formwork of the stair.",
             flow="The crane lifts the full skips from the stair onto the tipper truck, which carries them away to the left. Meanwhile the scaffolding crew strip the two towers down lift by lift and stack the tubes and boards on a truck, which drives out to the left with them.")

F[13] = dict(mom="the old stair has gone, and a fresh wet concrete stair base lies in its place.",
             act="A forklift carries a pallet of pale limestone steps from a truck to the stair, two masons set the first step on the concrete base, and the crawler crane lifts the next pallet of steps off the truck.")
S[13] = dict(title="MERDİVENİ KURAR", ne="Taş basamaklar aşağıdan yukarı tek tek yerleştirilir (forklift + iki usta); yanlarda korkuluk ankrajları. Geniş taş merdiven tamam.",
             mf="The two masons set the new limestone steps one by one from the pallet onto the concrete base, from the bottom step at the yard up to the top step at the hall floor.",
             flow="The stair climbs step by step, and the forklift carries the next pallets from the truck to the masons. At the sides the masons drill and set anchor sleeves for handrails to come, and the crew strip the timber formwork from the stair base and stack it on the truck.")

F[14] = dict(mom="the new stone stair is finished, and the old boarding deck still hangs rotten over the valley.",
             act="A crew in harnesses tears the rotten planks off the old boarding deck and drops them into a skip, the crawler crane lifts the skip of planks clear of the deck edge, and a grit-blasting crew sets up on the rusted cantilever girders.")
S[14] = dict(title="BOŞLUĞA AÇAR", ne="DİRENÇ: yakın biniş tabanının çürük döşemesi sökülür, paslı konsol kirişler kumlanır. Vadinin üstünde döşemesiz çıplak kirişler, altında gölgeli boşluk.",
             mf="The crew prise the rotten planks off the old boarding deck into the skip, and the crawler crane lifts the full skip from the deck onto the truck, until only the bare cantilever girders reach out over the drop; the blasting crew then blast the rust off the girders.",
             flow="Plank by plank the deck opens, and through the gaps the shadowed drop of the valley shows beneath the girders. The truck carries the full skips away to the left. Grey grit streams off the girders as the blasting crew works out along them in harnesses.")

F[15] = dict(mom="only bare steel girders reach out over the drop where the old deck was.",
             act="The crawler crane lowers a bundle of new steel girders onto the bare cantilever, a crew in harnesses bolts the first one in, and a concrete pump truck parks in the yard and unfolds its boom.")
S[15] = dict(title="TABANI DÖKER", ne="Vinç yeni çelik kirişleri ve trapez sac paketlerini konsola indirir; pompa kamyonu betonu döker, ekip mastarlar. Yakın biniş tabanı yeni, ıslak beton.",
             mf="The crawler crane lowers the new steel girders and bundles of steel deck sheet from the truck onto the bare cantilever, the crew bolt them down, and the pump truck pours concrete from its boom onto the sheet deck while the crew screed it level.",
             flow="The deck grows outward over the drop sheet by sheet, and the concrete spreads across it dark and wet. The crew bolt a temporary yellow edge barrier along its outer edge. The pump truck folds its boom and drives away to the left.")

F[16] = dict(mom="the near boarding deck is new, wet, dark grey concrete; across the valley the far station is still grey with grime.",
             act="Across the valley, small and distant, a crew on a mobile work platform starts to wash the face of the far station; at the near deck a worker hoses the fresh concrete, and the crawler crane lifts a pallet of rolled curing blankets off a truck.")
S[16] = dict(title="KARŞIYI YIKAR", ne="Karşı istasyonda cephe yıkanır, biniş tabanının kalıbı kurulur (uzak, küçük). Yakında taze beton ıslatılır.",
             mf="Across the valley the tiny crew wash the far station's face from the mobile work platform, and carpenters build timber formwork for its new boarding deck from stacked boards on the service road.",
             flow="The far face turns from grey to pale cream in the distance, and the formwork boards go up at its deck edge. At the near deck a worker keeps the fresh concrete wet with a hose, and the crane lifts the pallet of curing blankets from the truck and holds it over the yard.")

F[17] = dict(mom="the far face is pale cream and its deck formwork stands ready.",
             act="Across the valley a pump truck on the service road pours concrete into the far deck formwork, the tiny crew screeding it; at the near deck a crew starts to unroll wet curing blankets, and the crawler crane lowers a pallet of rolled blankets onto the deck.")
S[17] = dict(title="İKİ TABAN", ne="Karşı yamaçta pompa kamyonu karşı biniş tabanını döker; yakında beton kürü için ıslak örtüler serilir. İki istasyonun biniş tabanı yeni; arada hâlâ boşluk.",
             mf="Across the valley the pump truck pours concrete from its boom into the formwork of the far boarding deck, and at the near deck the crew unroll the wet curing blankets from the pallet across the fresh concrete.",
             flow="The far deck fills in the distance and its formwork stays round its edges. At the near deck the blankets cover the concrete strip by strip from the hall end out to the edge barrier, and a worker carries the empty pallet to the truck. Both stations now have new boarding decks, with the empty valley still between them.")

# ═══ PERDE 3 ═══════════════════════════════════════════════════════════════
F[18] = dict(mom="both boarding decks are new concrete, and a heavy truck has brought the big wheel.",
             act="A heavy low-loader truck stands in the gravel yard carrying a big horizontal steel bullwheel, four metres across; a rigging crew sets four slings on its spokes and the crawler crane starts to lift the wheel off the trailer, while a worker rolls up the curing blankets on the near deck.")
S[18] = dict(title="TEKERLEK GELİR", ne="Ağır yük kamyonu bakım alanına Ø 4 m çelik makara tekerleğini getirir; vinç onu kaldırır, açık çatının üstüne, salonun sağ ucuna hizalar.",
             mf="The crawler crane lifts the bullwheel from the low-loader in the yard up to hang above the open wall heads at the right end of the hall.",
             flow="The wheel rises flat and slow on its four slings, steadied by taglines, and turns gently as it climbs. On the near deck the worker rolls up the curing blankets and carries them to a pallet, leaving the concrete pale and dry. The empty low-loader drives out to the left.")

F[19] = dict(mom="the big wheel hangs above the open walls of the near hall.",
             act="The crawler crane lowers the bullwheel through the open top of the hall towards its steel frame at the right end, a rigging crew inside guides it with taglines, and a truck brings a crated drive motor into the yard.")
S[19] = dict(title="TEKERLEĞİ OTURTUR", ne="Tekerlek açık çatıdan salonun sağ ucundaki çelik çerçeveye iner; ekip cıvatalar. Koyu grafit gri tekerlek kemerden okunur.",
             mf="The crawler crane lowers the bullwheel from above the open wall heads into its steel frame at the right end of the hall, and the crew bolt it down.",
             flow="The wheel sinks below the wall heads and settles into its frame, visible through the right-hand arches. The crane lifts its slings clear and swings to the truck, where the crew sling the drive motor.")

F[20] = dict(mom="the bullwheel lies bolted in the hall, and the drive motor is on its way in.",
             act="The crawler crane lifts the drive motor, a big dark grey box, over the wall heads towards its bed beside the wheel, a fitting crew inside the hall waits at the bed, and the truck in the yard carries the gearbox, the next box.")
S[20] = dict(title="TAHRİKİ İNDİRİR", ne="Tahrik motoru ve dişli kutusu (iki büyük kutu yük) vinçle çatıdan indirilir. Makine dairesi dolu.",
             mf="The crawler crane lifts the drive motor and then the gearbox from the truck in the yard and lowers them through the open top of the hall onto their bed beside the bullwheel.",
             flow="Each box swings in over the wall heads and drops slowly out of sight into the hall, and the fitters bolt it down. The truck drives out to the left, and a second truck brings the steel headframe lying on its trailer.")

F[21] = dict(mom="the machine room is full, and the steel headframe has arrived on a truck.",
             act="The crawler crane lifts the dark graphite-grey steel headframe, about six metres tall, off a truck and swings it out towards the outer end of the boarding deck, while a rigging crew on the deck stands ready at the anchor bolts with taglines.")
S[21] = dict(title="HAT BAŞLIĞI", ne="Vinç koyu gri çelik hat başlığı çerçevesini biniş tabanının ucuna diker (≈6 m, iki ayaklı); ekip ankraj cıvatalarını sıkar. Vadiye bakan koyu bir kapı.",
             mf="The crawler crane swings the steel headframe from the truck in the yard out to the outer end of the near boarding deck and stands it on its anchor bolts, where the crew bolt its two legs down.",
             flow="The headframe swings out over the deck, turns upright and lowers onto the bolts, and the riggers pull it plumb with the taglines. The crane then lifts a concrete counterweight block off a second truck in the yard.")

F[22] = dict(mom="a dark steel headframe now stands at the end of the near deck, facing the empty valley.",
             act="At the near hall the crawler crane lifts a concrete counterweight block off a truck while electricians fit cable trays inside; across the valley a small mobile crane on the far service road lifts the far bullwheel off its trailer.")
S[22] = dict(title="KARŞI TEKERLEK", ne="Karşı yamaçta karşı vinç, karşı istasyonun tekerleğini açık çatıya taşır (uzak).",
             mf="Across the valley the small mobile crane lifts the far bullwheel from its trailer on the service road and raises it over the open walls of the far station.",
             flow="The tiny wheel climbs over the far walls, steadied by a tiny crew. At the near hall the electricians carry cable trays from a pallet into the machine room and bolt them along the walls, and the crawler crane sets the counterweight block down by the left end of the hall.")

F[23] = dict(mom="the far bullwheel hangs above the far station's open walls.",
             act="Across the valley the mobile crane lowers the far bullwheel into the far station; at the near hall the crawler crane lifts the counterweight block towards the shaft and a crew opens the shaft cover.")
S[23] = dict(title="İKİ BAŞLIK", ne="Karşı tekerlek yerinde; karşı hat başlığı dikilir. İki hat başlığı vadinin iki yakasında birbirine bakar — aralarında hiçbir çizgi yok.",
             mf="Across the valley the mobile crane lowers the far bullwheel into the far station and then swings the far headframe from the trailer onto the outer end of the far boarding deck.",
             flow="The far headframe stands up small and dark at the edge of the far deck, facing this side. At the near hall the crew lift the shaft cover off and stack it on a pallet. The two headframes now face each other across the valley, with only air between them.")

F[24] = dict(mom="the two headframes face each other across the valley with only air between them.",
             act="The crawler crane lowers a big concrete counterweight block into the shaft at the left end of the hall, a fitting crew inside guides it down, and a truck in the yard carries steel cage sections.")
S[24] = dict(title="AĞIRLIK İNER", ne="Yakın salonun sol ucundaki kuyuya beton gerdirme ağırlığı indirilir; üstüne çelik kafes kurulur.",
             mf="The crawler crane lowers the concrete counterweight block from the truck into the shaft at the left end of the hall, then lifts the steel cage sections from the truck onto the shaft, and the crew bolt them together over it.",
             flow="The block sinks into the shaft until only its top edge shows below the wall heads, and the cage rises over it section by section. The truck drives out to the left. Across the valley the mobile crane folds its boom and drives down the far service road out of view.")

F[25] = dict(mom="a steel cage stands over the counterweight shaft at the left end of the hall.",
             act="The crawler crane lowers a pallet of grey electrical cabinets through the open top of the hall into the machine room, electricians inside pull cable from drums along the new trays, and a forklift carries cable drums from a truck.")
S[25] = dict(title="ELEKTRİK", ne="Elektrik panoları ve kablo kanalları taşınır; ekip makine dairesinde çalışır.",
             mf="The crawler crane lowers the electrical cabinets from the truck into the machine room beside the drive, and the electricians pull cable from the drums along the trays to them.",
             flow="The cabinets go down one pallet at a time, and the forklift carries the cable drums from the truck to the hall. The empty pallets come back up on the hook and are stacked on the truck.")

F[26] = dict(mom="the machine room is finished inside the roofless hall, and a truck stacked with new roof trusses has arrived.",
             act="The crawler crane lowers a second pallet of electrical cabinets into the machine room, a truck stacked with five new galvanised steel roof trusses backs into the yard, and a rigging crew climbs onto its trailer with slings.")
S[26] = dict(title="İLK MAKAS", ne="Vinç ilk yeni çelik çatı makasını taşır; makas salonun sağ ucunun hemen üstünde kancada.",
             mf="The crawler crane lifts the first new galvanised steel roof truss from the stack on the truck in the yard and raises it above the right end of the hall.",
             flow="The electricians finish in the machine room and carry their tool cases out to a cart. The crew sling the top truss, and it rises slowly off the truck, turning flat in the air, and hangs above the wall heads at the right end.")

# ═══ PERDE 4 ═══════════════════════════════════════════════════════════════
F[27] = dict(mom="the first new roof truss hangs above the right end of the roofless hall.",
             act="The crawler crane lowers the first truss onto the wall heads at the right end of the hall, a crew on the wall heads guides its feet onto the bearings, and a truck in the yard carries the stack of remaining trusses.")
S[27] = dict(title="MAKASLAR ①", ne="Makas 1 duvar başlarına oturur, ekip cıvatalar; makas 2 de oturur, makas 3 kancaya alınır.",
             mf="The crawler crane lowers the first truss and then the second from the stack on the truck onto the wall heads at the right end of the hall, where the crew bolt their feet down.",
             flow="Each truss lands with its feet on the wall heads and stands upright against the sky, braced by the crew. The crane swings back to the truck and lifts the third truss.")

F[28] = dict(mom="two new trusses stand on the right end of the hall.",
             act="The crawler crane swings the third truss over the hall towards the wall heads, a crew on the wall heads waits at the bearings, and the truck in the yard carries the last two trusses.")
S[28] = dict(title="MAKASLAR ②", ne="Makas 3, 4, 5 sırayla oturur. Beş makas — çatı iskeleti tam, eski sırt ve saçak çizgisinde.",
             mf="The crawler crane lifts the third, fourth and fifth trusses one by one from the truck and seats each onto the wall heads, from the right towards the left end, until five trusses stand evenly spaced.",
             flow="The skeleton fills from right to left, each truss a beat after the last. The empty truck drives out to the left, and a second truck brings bundles of timber purlins and boards, which the crane lifts off.")

F[29] = dict(mom="five new steel trusses stand on the near hall, the old roof line drawn again against the sky.",
             act="The crawler crane lifts a bundle of timber purlins and boards onto the trusses, carpenters on the trusses fix the first purlins at the right end, and a truck in the yard carries more timber.")
S[29] = dict(title="AHŞAP ①", ne="Aşık ve ahşap kaplama paketleri vinçle çatıya; marangozlar sağdan sola döşer. Çatının sağ yarısı açık sarı ahşap. ⭐ G30 = BÖLÜM SINIRI KARESİ.",
             mf="The crawler crane lifts bundles of timber purlins and roof boards from the truck onto the trusses, and the carpenters fix them and lay the boards from the right end of the roof towards the middle.",
             flow="The pale yellow boarding spreads leftward across the trusses board by board until it reaches the middle of the roof. The crane lifts a new bundle of boards from the truck and lowers it onto the middle truss.")

F[30] = dict(mom="the right half of the near roof is boarded in pale timber.",
             act="The crawler crane swings a bundle of timber boards onto the middle truss, carpenters on the roof lay the boards across the left half, and the truck in the yard carries the last bundles.")
S[30] = dict(title="AHŞAP ②", ne="Sol yarı ahşapla kaplanır. Bütün çatı açık sarı ahşap.",
             mf="The carpenters lay the timber roof boards from the bundles the crane sets on the trusses across the left half of the roof, from the middle to the left end.",
             flow="Board by board the last open bays close. The crane lifts a pallet of membrane rolls from the truck and lowers it onto the ridge.")

F[31] = dict(mom="the whole near roof is boarded in pale timber.",
             act="Roofers unroll the first strip of dark grey membrane from a pallet of rolls the crawler crane has set on the ridge, and a truck in the yard carries more rolls.")
S[31] = dict(title="MEMBRAN", ne="Koyu gri su yalıtım membranı rulolar hâlinde açılır. Çatı koyu gri.",
             mf="The roofers unroll the dark grey membrane from the rolls on the pallet the crane has set on the ridge, from the eaves up to the ridge, strip by strip across the roof.",
             flow="The pale timber disappears under dark grey strips from right to left, the seams lapped and pressed down by the roofers. The crane lifts a bundle of zinc sheet from a truck in the yard.")

F[32] = dict(mom="the whole near roof is covered in dark grey membrane.",
             act="The crawler crane lifts a bundle of lead-grey zinc sheet onto the right end of the roof, roofers fold the first standing seams, and a truck in the yard carries more zinc bundles.")
S[32] = dict(title="ÇİNKO ①", ne="Kurşun grisi dikişli çinko levhalar sağdan döşenir; dikiş çizgileri ışığı yakalar.",
             mf="The crawler crane lifts bundles of lead-grey zinc sheet from the truck onto the roof, and the roofers fold and seat the long standing-seam sheets onto the right half, from the eaves to the ridge.",
             flow="Sheet by sheet the right half turns from dark membrane to lead-grey zinc, each seam catching the light. The crane brings the next bundle from the truck.")

F[33] = dict(mom="the right half of the near roof is clad in standing-seam zinc.",
             act="The crawler crane lowers a bundle of zinc sheet and ridge caps onto the left half of the roof, roofers seat the next sheets, and a truck in the yard carries the last bundles.")
S[33] = dict(title="ÇİNKO ②", ne="Sol yarı çinko + mahya. Yakın istasyonun çatısı tam — eski siluetle aynı çizgi.",
             mf="The roofers lay the zinc sheets from the bundles the crane sets on the roof across the left half, from the middle to the left end, and fix the zinc ridge cap along the ridge.",
             flow="The last membrane goes under zinc and the ridge cap runs along the top from end to end. The empty truck drives out to the left, and the crane lifts a crate of bronze window frames from another truck. Across the valley a small mobile crane drives up the far service road.")

F[34] = dict(mom="the near station has its new zinc roof on its old line; across the valley the far station is still an open shell.",
             act="Across the valley the small mobile crane lifts a far roof truss from its trailer onto the far walls; at the near hall the crawler crane lifts a crate of bronze window frames off a truck and a crew sweeps the deck.")
S[34] = dict(title="KARŞI MAKAS", ne="Karşı istasyonda makaslar ve ahşap kaplama (uzak).",
             mf="Across the valley the small mobile crane lifts new trusses and bundles of timber boards from its trailer onto the walls of the far station, and the tiny crew fix them.",
             flow="The far roof skeleton rises small and dark, then turns pale as the tiny crew lay the boards. At the near hall the crane lowers the crate of window frames onto the gravel by the face.")

F[35] = dict(mom="the far station has new trusses and timber boarding.",
             act="Across the valley the small mobile crane lifts a bundle of zinc sheet onto the far roof; at the near hall the crawler crane lifts a crate of bronze window frames and a glazing crew sets up a mobile work platform by the face.")
S[35] = dict(title="İKİ ÇATI", ne="Karşı çatı çinkoyla tamamlanır. İki istasyon da çatılı — merak ① kısmen cevaplandı.",
             mf="Across the valley the small mobile crane lifts bundles of zinc sheet onto the far roof, and the tiny crew seat them from the eaves to the ridge.",
             flow="The far roof turns lead-grey in the distance. Both stations stand roofed again on their old lines. At the near hall the glazing crew carry the first frames from the crate to the platform.")

# ═══ PERDE 5 ═══════════════════════════════════════════════════════════════
F[36] = dict(mom="both stations stand roofed again on their old lines.",
             act="A glazing crew on a mobile work platform bolts a dark bronze steel window frame into the left arch, the crawler crane lifts a crate of frames down to the platform, and across the valley the mobile crane drives away.")
S[36] = dict(title="DOĞRAMA", ne="Beş kemer açıklığına koyu bronz çelik doğrama ızgaraları takılır; cam yok.",
             mf="The crane lifts the bronze window frames from the crate on the truck to the work platform, and the glazing crew set each frame into its arch and bolt it, from the left arch to the right.",
             flow="Arch by arch the dark bronze frames fill the five openings, still unglazed. Across the valley the mobile crane drives down the far service road out of view. A truck brings crates of glass, and the crane lifts a crate from it.")

F[37] = dict(mom="the five arches carry new bronze frames, still without glass.",
             act="A small crawler glazing robot with vacuum cups lifts the first big glass panel from a crate in the yard, a glazing crew on the platform guides it into the left arch, and the crawler crane lifts the next crate of glass off a truck.")
S[37] = dict(title="CAM ①", ne="Paletli küçük cam robotu vantuzlarla büyük cam panelleri soldan takar. Sol üç kemer camlı — net şeffaf, içerisi okunur.",
             mf="The crawler glazing robot lifts each big glass panel from the crate in the yard on its vacuum cups and sets it into the bronze frames of the arches, from the left arch towards the middle.",
             flow="Panel by panel the left three arches fill with clear glass, and the bullwheel and machine room show sharp through it. The crane lowers a second crate of glass from the truck beside the robot.")

F[38] = dict(mom="the left three arches are glazed in clear glass.",
             act="The crawler glazing robot lifts a glass panel from a crate towards the fourth arch, the glazing crew on the platform seals the last panels in the middle arch, and the crawler crane lowers a crate of glass panels beside it.")
S[38] = dict(title="CAM ②", ne="Sağ iki kemer camlanır. Bütün cephe camlı; camın ardında tekerlek ve makine dairesi.",
             mf="The glazing robot lifts the last glass panels from the crate and sets them into the bronze frames of the right two arches, and the glazing crew seal them.",
             flow="The last two arches fill with clear glass, and the whole face now shows the hall through its glass. The crane lifts the empty crates onto the truck, and a second truck brings pallets of oiled timber planks.")

F[39] = dict(mom="all five arches are glazed in clear glass.",
             act="The crawler crane lowers a pallet of oiled timber planks onto the near boarding deck, carpenters lay the first planks from it at the hall end, and a truck in the yard carries more pallets of planks.")
S[39] = dict(title="PERON ①", ne="Yakın biniş tabanına sıcak yağlı ahşap peron döşemesi: paletler + marangozlar. Peronun yarısı ahşap.",
             mf="The carpenters carry oiled timber planks from the pallet the crane has set on the boarding deck and lay them across the deck, from the hall end out towards the headframe.",
             flow="Warm timber spreads over the pale concrete plank by plank to the middle of the deck. The crane lifts a bundle of steel railing posts from the truck.")

F[40] = dict(mom="the inner half of the near boarding deck is laid with warm timber.",
             act="Carpenters lay planks on the outer half of the deck from a pallet, fitters set out steel railing posts along the edge, and the crawler crane lowers a bundle of railing posts onto the deck.")
S[40] = dict(title="PERON ②", ne="Ahşap döşeme tamamlanır; ince koyu çelik korkuluk (gergin çelik tel dolgulu) takılır.",
             mf="The carpenters lay the last planks from the pallet out to the headframe, and the fitters bolt slim steel railing posts along the deck edge and thread taut steel wire through them.",
             flow="The timber reaches the headframe, the posts stand up along the edge and the wire tightens between them. The fitters unbolt the temporary yellow barrier and carry it to the truck, which drives out to the left.")

F[41] = dict(mom="the near boarding deck is timber, edged with a slim steel railing.",
             act="Across the valley, small and distant, a tiny glazing crew lifts glass panels from a crate into the windows of the far station; at the near hall the crawler crane lifts a pallet of steel handrail sections off a truck and a team sweeps the deck.")
S[41] = dict(title="KARŞI CAM", ne="Karşı istasyonun camları ve ahşap peronu (uzak).",
             mf="Across the valley the tiny crew lift glass panels from a crate on the service road into the far station's windows and lay timber planks from a pallet across its boarding deck.",
             flow="The far face catches the midday light in its new glass, and its deck turns warm brown. At the near hall the crane lowers the pallet of handrail sections onto the gravel by the stair.")

F[42] = dict(mom="the far station is glazed, with a warm timber boarding deck.",
             act="Across the valley the small mobile crane drives up the far service road and lifts a steel cantilever section towards the rock knoll right of the far station; at the near hall the crawler crane lifts a pallet of handrail sections and a crew sweeps the stair.")
S[42] = dict(title="SEYİR TERASI ①", ne="Karşı istasyonun sağındaki kayalığa karşı vinç seyir terasının çelik konsol iskeletini kurar.",
             mf="Across the valley the small mobile crane lifts steel cantilever sections from its trailer onto the rock knoll right of the far station, and the tiny crew bolt them into the frame of a viewing terrace.",
             flow="A thin dark frame juts out from the knoll over the drop. At the near hall the crew carry handrail sections from the pallet to the stair foot.")

F[43] = dict(mom="the steel frame of a viewing terrace juts from the rock knoll beside the far station.",
             act="Across the valley the small mobile crane lifts a pallet of timber decking onto the terrace frame; at the near hall the crawler crane holds a pallet of handrail sections over the stair and a crew sets out the first sections.")
S[43] = dict(title="SEYİR TERASI ②", ne="Seyir terası ahşap döşeme, korkuluk ve birkaç bank. Karşı seyir alanı tamam.",
             mf="Across the valley the small mobile crane lifts pallets of timber decking and benches from its trailer onto the terrace frame, and the tiny crew lay the decking, fix the railing and set the benches.",
             flow="The terrace turns into a pale timber strip with a fine railing at the edge of the drop. At the near hall the crane lowers the handrail sections onto the stair.")

F[44] = dict(mom="the far viewing terrace is finished, with its railing and benches.",
             act="Fitters bolt slim dark steel handrails up both sides of the stone stair, the crawler crane lowers a pallet of timber door leaves to the stair head, and carpenters lift the first door leaf towards the entrance; across the valley the mobile crane folds its boom.")
S[44] = dict(title="KAPI", ne="Yakında merdiven korkulukları (koyu çelik) ve çift kanatlı ahşap giriş kapısı takılır. İki istasyon dıştan bitmiş — ama aralarında hat yok.",
             mf="The crane lowers the handrail sections and the door leaves from the truck to the stair, the fitters bolt the handrails up both sides from the yard to the top step, and the carpenters hang the pair of timber doors in the entrance at its head.",
             flow="The stair gets its handrails and the doors close the entrance. Across the valley the mobile crane drives down the far service road out of view. A truck brings a big timber cable reel into the yard, and the crane lifts it off. Both stations stand finished outside, with only air between them.")

# ═══ PERDE 6 ═══════════════════════════════════════════════════════════════
F[45] = dict(mom="both stations stand finished outside, and only air fills the gap between them.",
             act="A winch drum on the near headframe starts to turn, a rigging crew on the boarding deck guides a thin line off it down into the valley, a matching tiny crew works at the far headframe, and the crawler crane lifts a big timber cable reel onto a truck in the yard.")
S[45] = dict(title="İLK BAĞ", ne="Hat başlığındaki tambur döner; ekip ince pilot halatı vadinin gölgeli dibinden yukarı çeker — halat iki yakada yükselir, boşluğun üstünde gevşek bir yay çizer.",
             mf="The winch drum on the near headframe hauls the thin pilot rope up from the shadowed floor of the valley, where the crews have laid it out, until it rises at both ends and spans from the near headframe to the far headframe in a slack curve.",
             flow="From the shadow below both decks a thin line lifts at the same time, climbs towards each headframe and comes clear of the valley as one long slack curve against the far slope. The crew on the deck guide it onto the drum as it winds. The crane lowers the cable reel onto the truck bed and holds it there.")

F[46] = dict(mom="one thin pilot rope now spans the valley — the first line between the two stations.",
             act="The big timber reel on the truck in the yard starts to turn, a rigging crew on the near deck clamps the end of a thicker haul rope to the pilot rope, and the crawler crane lifts the reel to feed the rope off it.")
S[46] = dict(title="ÇEKME HALATI", ne="Pilot halatla daha kalın çekme halatı geçirilir; yakında kamyon üstündeki büyük ahşap makara döner.",
             mf="The pilot rope draws the thicker steel haul rope off the big timber reel on the truck in the yard, across the valley from the near headframe to the far headframe.",
             flow="The reel turns on the truck, the haul rope pays out over the headframe and runs out along the pilot rope, sagging across the valley, until its end reaches the far headframe and the tiny far crew clamp it.")

F[47] = dict(mom="two lines span the valley: the pilot rope and the thicker haul rope.",
             act="A second big reel on the truck starts to turn, the rigging crew clamps the end of a heavy dark carrying rope to the haul rope at the headframe, and the crawler crane lifts the reel to feed it.")
S[47] = dict(title="TAŞIYICI ①", ne="Kalın koyu taşıyıcı halat çekilmeye başlar; makara döner, halat ucu çekme halatı boyunca karşıya ilerler.",
             mf="The haul rope draws the end of the first heavy carrying rope off the big reel on the truck, out from the near headframe along the haul rope to the middle of the valley.",
             flow="The heavy rope pays out slowly over the headframe saddle and creeps out along the haul rope until its end has passed the middle of the valley. Over the far ridge at the left the white clouds tower up and darken.")

F[48] = dict(mom="the end of the first carrying rope has passed the middle of the valley, and a summer storm is coming in from the left.",
             act="The rigging crew carries its tools from the headframe back into the hall as the wind rises, the crawler crane lowers the cable reel onto the truck bed, and a team pulls tarpaulins over the stacked material.")
S[48] = dict(title="SAĞANAK", ne="⚠️ DİRENÇ: batıdan kısa bir yaz sağanağı geçer — rüzgâr sertleşir, iş durur, ekip hat başlığından çekilir, yarı çekilmiş halat hafifçe salınır; yağmur taşı ve ahşabı koyulaştırır. Halat ucu AYNI yerde.",
             mf="A short summer downpour sweeps across the valley from the left; the rigging crew carry their tools from the headframe into the hall, and the half-drawn carrying rope sways on the haul rope and stays where it stopped.",
             flow="The dark rain cloud rolls in from the left over the far ridge, the light dims and cools, and grey streaks of rain sweep across the valley and darken the stone, the zinc and the timber decks. The crane lowers the reel onto the truck bed and the team stack the last loose material under tarpaulins. Then the cloud drifts off to the right over the far ridge, blue sky clears from the left and the sunlight comes back across the wet stations. The end of the carrying rope stays at exactly the same point past the middle of the valley.")

F[49] = dict(mom="the downpour has passed, every surface is wet, and the carrying rope hangs where the work stopped.",
             act="The rigging crew walks back out to the headframe, the reel on the truck starts to turn again, and the crawler crane lifts the reel of carrying rope to feed it.")
S[49] = dict(title="KARŞIYA ULAŞIR", ne="İş sürer; taşıyıcı halatın ucu karşı hat başlığına ulaşır, karşı ekip ankraja bağlar. Islak yüzeyler kurur.",
             mf="The haul rope draws the end of the first carrying rope from the middle of the valley on to the far headframe, where the tiny far crew anchor it.",
             flow="The heavy rope creeps the rest of the way across and climbs to the far headframe. The puddles in the yard shrink, and the stone, the zinc and the timber dry from dark to pale. The crane lowers the empty reel onto the truck and lifts the second full reel off a second truck.")

F[50] = dict(mom="the first heavy carrying rope spans the whole valley in a slack curve.",
             act="The rigging crew clamps the end of the second carrying rope to the haul rope at the headframe, the reel on the truck turns, and the crawler crane lifts the second reel to feed it.")
S[50] = dict(title="TAŞIYICI ②", ne="İkinci taşıyıcı halat aynı yoldan çekilir. İki paralel taşıyıcı halat.",
             mf="The haul rope draws the second heavy carrying rope off the reel on the truck from the near headframe across the valley to the far headframe, parallel to the first.",
             flow="The second rope pays out over the saddle and crosses beside the first in the same slack curve, and the tiny far crew anchor it. The crane lowers the empty reel onto the truck, which drives out to the left, and lifts a crate of saddle covers.")

F[51] = dict(mom="two parallel carrying ropes hang slack across the valley.",
             act="Riggers inside the hall release the counterweight, which starts down its shaft, the crawler crane lifts a crate of grey rope saddle covers onto the deck, and the crews at both headframes check the rope clamps.")
S[51] = dict(title="GERDİRME", ne="Gerdirme: yakın salondaki ağırlık kuyusunda iner; halatların sarkması azalır, çizgiler düzelir ve yükselir. İki istasyon görsel olarak bağlandı.",
             mf="The concrete counterweight sinks down its shaft at the left end of the hall and pulls the two carrying ropes from a slack curve into two taut, nearly straight lines running from the near headframe up to the far headframe.",
             flow="The sag in both ropes shrinks steadily and the lines lift and straighten across the valley, the haul rope still hanging slack beneath them. The crane lowers the crate of covers onto the deck beside the headframe.")

F[52] = dict(mom="two taut carrying ropes now run straight across the valley — the two stations are joined.",
             act="Riggers at the headframe pull the slack haul rope in towards the bullwheel, a crew inside the hall guides it round the wheel, and the crawler crane holds a crate of saddle covers over the deck.")
S[52] = dict(title="DÖNGÜ", ne="İnce çekme halatı tekerleğe sarılır ve kapalı döngü olur. Üç halat çizgisi — hat tamam.",
             mf="The riggers pull the haul rope from the headframe onto the bullwheel inside the hall and splice it into a closed loop, so it runs taut beside the two carrying ropes from the near headframe up to the far headframe.",
             flow="The haul rope lifts out of its slack curve and straightens beside the carrying ropes, and the bullwheel creeps round as the crew take up the loop. The crane lowers the crate of covers onto the deck.")

F[53] = dict(mom="three taut lines run across the valley, and the line is complete.",
             act="The crews at both headframes lift grey cover caps from a crate onto the rope saddles, a scaffolding crew carries tubes towards the rusted cabin on its cradle, and the crawler crane lifts a bundle of scaffold tubes off a truck.")
S[53] = dict(title="KABİNE DÖNER", ne="İki hat başlığında halat eyerleri kapatılır; bakım alanında paslı kabinin çevresine iskele kurulur — yenileme başlıyor. Merak ② geri döner.",
             mf="The crews at both headframes fit grey cover caps from the crate onto the rope saddles, and a scaffolding crew build a scaffold from the tube bundle round the rusted cabin on its cradle in the yard.",
             flow="The caps close over the saddles, and the scaffold rises round the cabin lift by lift, the cabin still clearly visible inside it. The crane lowers a second bundle of tubes from the truck to the scaffolders.")

# ═══ PERDE 7 ═══════════════════════════════════════════════════════════════
F[54] = dict(mom="the line is complete, and the rusted cabin stands inside a scaffold in the yard.",
             act="A crew inside the scaffold pulls the broken glass out of the cabin into a steel skip, two workers carry the old rotten bench towards the yard, and the crawler crane lifts a bundle of scaffold tubes clear of the cabin.")
S[54] = dict(title="KABİNİ SÖKER", ne="Kabinden kırık camlar sökülür, eski çürük ahşap bank ve iç kaplama dışarı taşınır, kapı çıkarılır. Kabin camsız, içi boş, her yer pas.",
             mf="The crew inside the scaffold pull the broken glass, the rotten timber bench and the old door from the cabin and carry them down to the skip in the yard.",
             flow="Piece by piece the cabin is emptied, until it stands as a bare rusted shell with open window holes. The crane lifts the full skip onto a truck, which carries it away to the left.")

F[55] = dict(mom="the cabin stands stripped to a bare rusted shell inside its scaffold.",
             act="A blasting crew inside the scaffold starts to grit-blast the cabin body from the roof down, grey dust drifting to the left, a compressor runs in the yard, and the crawler crane lifts a skip of old glass and rotten timber onto a truck.")
S[55] = dict(title="KUMLAR", ne="İskele çevresinde kumlama: gri toz sola savrulur. Kabin gövdesi çıplak mat gri çelik — pas yok. Oran ve boy AYNI.",
             mf="The blasting crew drive the grit blast across the cabin body from the roof down to the floor, stripping the rust off into a grey dust that drifts to the left.",
             flow="Band by band the faded red and the rust come away, and bare matt grey steel shows beneath, the box keeping exactly its size and shape. The crane lifts a skip of spent grit from the scaffold onto the truck.")

F[56] = dict(mom="the cabin body has been blasted back to bare grey steel.",
             act="A welder inside the scaffold welds a steel patch over a hole in the cabin body, a painter sets up a spray gun at the compressor, and the crawler crane lifts a skip of spent blast grit onto a truck.")
S[56] = dict(title="ASTAR", ne="Kaynakçı yamaları kapatır; açık gri astar püskürtülür.",
             mf="The welder closes the holes in the cabin's body with steel patches from the plate stack, and the painters spray light grey primer over it from the roof down to the floor.",
             flow="A few small bright sparks show at the patches, and then the grey steel turns pale and even under the primer. The crane lifts a pallet of paint tins from a truck onto the scaffold.")

F[57] = dict(mom="the cabin stands in pale grey primer.",
             act="Painters inside the scaffold start to spray the cabin body from the roof down, a compressor runs on the gravel, and the crawler crane lowers a pallet of paint tins onto the scaffold.")
S[57] = dict(title="KIRMIZI", ne="Kırmızı boya: derin sinyal kırmızısı gövde + pencerelerin altında ince krem şerit. Eski kabinle aynı model, aynı oran.",
             mf="The painters spray deep signal-red paint from the tins on the pallet over the cabin body from the roof down to the floor, then mask and spray a thin cream band below the windows.",
             flow="The pale primer turns deep red from the top down, and a thin cream band appears below the windows as the masking comes off. The crane lifts a crate of glass panes from a truck.")

F[58] = dict(mom="the same cabin is red again, with a thin cream band.",
             act="Glaziers inside the scaffold set the first clear pane into the cabin, a fitter offers up the new sliding door, and the crawler crane lowers a crate of glass panes onto the scaffold.")
S[58] = dict(title="CAMLAR", ne="Yeni net camlar ve sürgülü kapı takılır; içeri tek parça ahşap bank (büyük modül) taşınır.",
             mf="The glaziers set new clear glass panes from the crate into the cabin's windows, the fitters slide the new door onto its runner, and two workers carry a one-piece timber bench from the truck into the cabin.",
             flow="Window by window the cabin closes up with clear glass, the door slides shut, and the bench goes in through the doorway. The crane lifts the dark grey hanger arm and carriage off a truck.")

F[59] = dict(mom="the red cabin is glazed, with its door and a new bench.",
             act="The crawler crane lowers the repainted dark grey hanger arm with its four-wheel carriage from a truck towards the cabin roof, fitters on the scaffold guide it onto the roof plate, and a scaffolding crew starts to strip the scaffold.")
S[59] = dict(title="ASKI KOLU", ne="Vinç yeniden boyanmış koyu gri askı kolunu ve makaralı taşıyıcıyı kabinin üstüne indirir; ekip birleştirir. İskele sökülür. ⭐ G60 = BÖLÜM SINIRI KARESİ.",
             mf="The crawler crane lowers the hanger arm and carriage from the truck onto the roof of the cabin, the fitters bolt them on, and the scaffolding crew strip the scaffold from round the cabin and stack the tubes on the truck.",
             flow="The arm settles onto the roof and the carriage sits upright above it. The scaffold comes down lift by lift and the red cabin stands clear in the yard, its carriage held on taut slings from the crane hook.")

F[60] = dict(mom="the red cabin stands complete on its cradle, its carriage held on the crane hook.",
             act="The crawler crane lifts the red cabin by its carriage off the cradle on taut slings, a rigging crew steadies it with taglines, and a truck in the yard carries away the last scaffold tubes.")
S[60] = dict(title="TAŞIR", ne="Vinç kabini beşikten kaldırır, biniş tabanının ucuna, taşıyıcı halatların hemen altına getirir. ⚠️ DERS 57: uzun taşıma (≈25 m) — pilot önceliği.",
             mf="The crawler crane lifts the red cabin by its carriage from the cradle in the yard, swings it slowly to the right over the stair and the boarding deck, and holds it at the outer end of the deck, about one metre below the two carrying ropes.",
             flow="The cabin rises level and steady on its slings, the riggers walking with the taglines, and passes high over the stair and the deck railing as one rigid red box, never doubled, never stretched. The truck carries the scaffold tubes away to the left.")

F[61] = dict(mom="the red cabin hangs on the crane at the end of the near deck, just below the carrying ropes.",
             act="The crawler crane hoists the cabin up towards the carrying ropes, a rigging crew on the deck and on the headframe guides its carriage wheels onto the ropes, and a cart carries clamps from a pallet on the deck.")
S[61] = dict(title="HALATA ASAR", ne="Ekip makaralı taşıyıcıyı taşıyıcı halatlara oturtur, çekme halatına kenetler; sapanlar gevşer. Kabin halatta asılı — merak ② cevap.",
             mf="The crane eases the cabin up from the end of the deck until the crew seat its four-wheel carriage onto the two carrying ropes and clamp it to the haul rope, and the crane slings then go slack.",
             flow="The carriage wheels touch the ropes, the cabin settles onto them with a small sway, and the ropes take its weight. The riggers carry the clamps from the cart up to the carriage.")

F[62] = dict(mom="the red cabin hangs on the carrying ropes for the first time.",
             act="A rigging crew unhooks the slack slings from the cabin's carriage, the crawler crane lowers its boom, and two technicians carry a tool case along the deck into the cabin.")
S[62] = dict(title="VİNÇ GİDER", ne="Sapanlar çözülür; vinç bomunu yatırır ve paletleriyle kadrajın soluna çıkar. Kabin peronda, kapı açık, iki teknisyen içinde. Son vinç karesi.",
             mf="The crew unhook the slack slings from the cabin's carriage, and the crawler crane lowers its boom and drives out of the yard to the left on its crawlers.",
             flow="The boom comes down in a long slow arc, and the crane crawls away across the gravel and out of the frame, leaving deep crawler prints. Two technicians carry tool cases from a cart on the deck into the cabin.")

# ═══ PERDE 8 ═══════════════════════════════════════════════════════════════
F[63] = dict(mom="the yard is clear of the big machine, and the red cabin waits at the near deck with two technicians inside.",
             act="Two technicians of a small crew step out of the cabin onto the boarding deck and pull its door closed, a technician in the machine room behind the glass works at the drive, and a small cart carries a tool case away along the deck; the bullwheel inside begins to turn slowly.")
S[63] = dict(title="BEKLEYİŞ", ne="Teknisyenler makine dairesinde; peronda son kontrol; kapı kapanır. Tekerlek ilk kez döner.",
             mf="The technicians step from the cabin onto the deck and slide its door shut, and the drive in the machine room starts the bullwheel turning slowly for the first time, from rest to a steady crawl.",
             flow="The cart carries the tool case off the deck into the hall. Behind the arch glass the big wheel stirs, stops, then turns steadily, and the haul rope begins to creep over its saddle. The technicians stand back from the deck edge.")

F[64] = dict(mom="the empty red cabin is ready to leave the near deck for the first time.",
             act="The bullwheel hauls the empty cabin out from the boarding deck at natural speed, its hanger arm swinging slightly as the carriage wheels roll onto the open ropes under the headframe, while a crew of two technicians watches from the deck.")
S[64] = dict(title="İLK GEÇİŞ ①", ne="⭐ İLK GEÇİŞ — gerçek hız. Kabin peronu terk eder, hat başlığının altından geçip vadinin üstüne çıkar.",
             mf="The bullwheel hauls the empty cabin out from the near boarding deck, under the headframe and onto the open ropes over the valley, to about thirty-five metres out.",
             flow="The cabin moves off smoothly, rocks gently once as its carriage passes the headframe saddle, and glides out over the drop, the shadowed valley opening beneath it. The two technicians on the deck stay still, backs to the camera, no readable face.")

F[65] = dict(mom="the empty cabin is out over the valley for the first time.",
             act="The haul rope pulls the empty cabin on across the valley at natural speed, the bullwheel turning steadily behind the glass, its hanger arm steady, and a crew of two technicians watches from the deck.")
S[65] = dict(title="İLK GEÇİŞ ②", ne="Kabin vadinin ortasından geçer — altındaki boşluk en derin. En sessiz an.",
             mf="The haul rope draws the cabin from about thirty-five metres out to about seventy metres out, over the deepest part of the valley.",
             flow="The cabin glides steadily on, small against the far slope, the empty drop deepest beneath it. The ropes hum and hold their line. The technicians on the deck stay still, backs to the camera, no readable face.")

F[66] = dict(mom="the empty cabin crosses over the deepest part of the valley.",
             act="The haul rope pulls the cabin towards the far station at natural speed, its hanger arm steady, a tiny far crew waits at the far deck, and a crew of two technicians watches from the near deck.")
S[66] = dict(title="İLK GEÇİŞ ③", ne="Kabin yavaşlayarak karşı perona girer ve durur. Merak ⑤ açılır: yük taşır mı?",
             mf="The haul rope draws the cabin from the middle of the valley up into the far station, where it slows and stops at the far boarding deck.",
             flow="The red box climbs the last stretch, slows under the far headframe and stops at the far deck, small and bright in the distance. The tiny figures there stay still, no readable face.")

F[67] = dict(mom="the cabin has reached the far station for the first time.",
             act="The haul rope pulls the cabin back from the far station at slow inspection speed, a crew on the near deck wheels a cart of blue water-filled test drums out of the hall, and a truck in the yard carries more drums on pallets.")
S[67] = dict(title="DÖNÜŞ", ne="Kabin muayene hızında (10 dk'da ≈108 m) klip boyunca geri kayar. Yeniden A — dikiş beyanlı.",
             mf="The haul rope draws the empty cabin slowly back from the far boarding deck across the whole valley to the near boarding deck, gliding steadily through the shot.",
             flow="The cabin moves at slow inspection speed and stays visible all the way, gliding smoothly along the ropes rather than jumping. A truck delivers pallets of blue test drums, and the crew carry them from the truck to the deck.")

F[68] = dict(mom="the cabin is back at the near deck after its first crossing.",
             act="The crew wheels carts of blue water-filled test drums from the pallets on the deck into the cabin, stacks the first drums on its floor, and a truck in the yard carries more pallets.")
S[68] = dict(title="YÜK", ne="Ekip el arabalarıyla kabine mavi su dolu test bidonları taşır. Kabin içi dolu, kapı kapalı.",
             mf="The crew wheel the blue water-filled test drums from the pallets on the deck into the cabin on carts and stack them on its floor until it is full, then slide the door shut.",
             flow="Cart after cart rolls in through the door, and the windows fill with blue. The cabin sinks a little on its carriage as the load grows. The empty pallets are stacked on the truck.")

F[69] = dict(mom="the cabin is loaded with blue test drums.",
             act="The haul rope pulls the loaded cabin slowly out from the boarding deck, the crew watches from the deck, and a cart carries the empty pallets to the truck in the yard.")
S[69] = dict(title="FREN", ne="⚓ DİRENÇ: yüklü kısa deneme — kabin muayene hızında vadinin ortasına kayar, durur (fren testi), asılı bekler. Halat sarkması derin.",
             mf="The haul rope draws the loaded cabin slowly from the near boarding deck out over the valley to the middle of the span, where the brake stops it and it hangs still, the ropes sagging deeper under its weight.",
             flow="The loaded cabin glides out steadily, sways once as the brake holds, and hangs still over the deepest part of the valley. The crew on the deck stand watching, and a cart carries the empty pallets to the truck.")

F[70] = dict(mom="the loaded cabin hangs braked over the middle of the valley.",
             act="The haul rope pulls the loaded cabin back towards the near deck, a crew waits on the deck with empty carts, and a truck in the yard carries the drum pallets.")
S[70] = dict(title="BOŞALTIR", ne="Kabin geri gelir; bidonlar boşaltılır, el arabalarıyla peron dışına.",
             mf="The haul rope draws the loaded cabin slowly back from the middle of the valley to the near deck, and the crew carry the test drums out of it on carts to the pallets and empty them into the yard drain.",
             flow="The ropes rise back to their line as the cabin returns. Cart by cart the blue drums come out and the windows clear. The truck carries the empty drums away to the left.")

F[71] = dict(mom="the cabin is back at the near deck, empty, after the loaded test.",
             act="A crew on the deck wipes the cabin's windows, a technician pulls the door shut to test it, and a cart carries the last test drums to a truck in the yard.")
S[71] = dict(title="SON KONTROL", ne="Son kontrol: kapı, fren; camlar silinir. Kabin parlak, boş — deneme bitti. Merak ⑤ cevap.",
             mf="The crew wipe the cabin's windows clean from the deck, test the door and the brake, and carry the last test drums from the deck to the truck in the yard.",
             flow="The door slides open and shut twice, the cabin creeps a metre out and back as the brake is tested, and the glass comes up clear and bright. The truck drives out to the left.")

# ═══ PERDE 9 ═══════════════════════════════════════════════════════════════
F[72] = dict(mom="the tests are done, and the clean red cabin waits at the near deck.",
             act="A crew with a forklift lifts the steel cradle onto a truck, a second truck takes the site container, and the first truck starts to drive out of the yard to the left.")
S[72] = dict(title="BOŞALIR", ne="Son araçlar ayrılır: iskele kuleleri, beşik ve konteyner kamyonlara; kamyonlar sırayla soldan kadraj dışına çıkar. Bakım alanı boş.",
             mf="The forklift lifts the steel cradle, the last scaffold bundles and the site container from the yard onto the trucks, and the trucks drive out of the frame to the left one by one.",
             flow="The yard empties load by load, and each truck pulls away along the gravel and out of the frame. Pale imprints and tyre marks are left on the gravel where the cradle and the container stood.")

F[73] = dict(mom="the yard is empty for the first time, marked only by tyre marks.",
             act="A small roller levels the gravel of the yard, a gang with rakes spreads the gravel behind it, and two workers start to dig the first planting bed and pile the spoil on a tarpaulin.")
S[73] = dict(title="TESVİYE", ne="Ön bahçe tesviye edilir, çakıl tırmıklanır, beşik izleri silinir; bahçe yatakları kazılır.",
             mf="A small roller and a gang with rakes level the gravel of the yard from the hall wall to the yard edge, and the gang dig planting beds into the soil, piling the spoil on a tarpaulin.",
             flow="The tyre marks and imprints disappear under the rakes, and the yard turns flat and even. Dark beds open in the gravel one after another, and a cart carries the spoil from the tarpaulin to the yard edge.")

F[74] = dict(mom="the yard is graded flat, with dug beds of dark soil.",
             act="A truck at the yard edge carries pallets of shrubs, grasses and two young trees, a gang of gardeners lifts a young tree from a pallet into its bed, and a cart brings bags of compost.")
S[74] = dict(title="DİKER", ne="Paletlerle bitkiler gelir: çalılar, otlar, iki genç ağaç; ekip diker.",
             mf="The gardeners carry shrubs, grasses and two young trees from the pallets at the yard edge into the beds and plant them, filling the beds from the left to the right.",
             flow="Green spreads across the dark beds, and the two young trees are set upright and staked. The truck carries the empty pallets away to the left.")

F[75] = dict(mom="the yard is a young garden, with two new trees.",
             act="A gardener opens a valve at the head of the stone channel beside the stair, a gang sets the last flat stones round the pool edge, and a cart carries spare stones away along the path.")
S[75] = dict(title="SU", ne="Su: merdivenin yanındaki taş kanala eski kaynağın suyu yeniden verilir — su basamak basamak akmaya başlar, küçük havuzda toplanır.",
             mf="Water from the old spring runs from the valve at the head of the stone channel down its steps beside the stair into the small pool at its foot, filling it.",
             flow="The first water slips over the top step, runs down step by step and spreads into the pool, which fills and starts to spill quietly over its lip. The gang carry spare stones from the pool edge to the cart.")

F[76] = dict(mom="water runs again in the stone channel beside the stair.",
             act="Two workers lift a timber bench from a cart on the gravel path towards the stone terrace beside the stair foot, a gang sets stone planters in a row, and the cart rolls back for more.")
S[76] = dict(title="TERAS", ne="Merdiven başında taş teras: ahşap banklar ve saksılar yerleşir.",
             mf="Two workers carry timber benches and stone planters from a cart on the gravel path onto the stone terrace beside the stair foot and set them in a row.",
             flow="The terrace fills with benches and planters, and the cart brings the last bench from the path. The water runs on in the channel.")

F[77] = dict(mom="benches and planters stand on the stone terrace beside the stair.",
             act="Electricians on a mobile work platform fix wall lamps along the hall, a crew lifts a crate of lamps from a cart up the stair, and the cart rolls along the deck with more crates.")
S[77] = dict(title="ARMATÜR", ne="Armatürler takılır: duvar aplikleri, merdiven lambaları, peron lambaları (hepsi sönük).",
             mf="The electricians carry lamps from the crates on a cart and fix them along the hall walls, up the stair and along the deck railing, all left unlit.",
             flow="Small dark lamp fittings appear one after another as the electricians bolt them on. The cart carries the empty crates away along the path.")

F[78] = dict(mom="lamps are fitted all over the near station, all unlit.",
             act="A crew on a mobile work platform wipes the glass of the arches, two workers sweep the deck and stack the tool cases on a cart, and across the valley the last tiny crew walks out along the far service road.")
S[78] = dict(title="SON TEMİZLİK", ne="Son temizlik: cam silme, peron süpürme; karşı istasyonda son ekip ayrılır (uzak). Şantiye boş, kimse yok; güneş alçak, altın ışık.",
             mf="The crew wipe the arch glass from the platform, sweep the deck, and carry the last tool cases from the deck to a cart that rolls out of the yard to the left.",
             flow="The platform drives out after the cart, and the last figures walk off along the path at the left. Across the valley the last tiny crew leave along the far service road. The site stands empty in the low golden light, only the water moving.")

F[79] = dict(mom="the site is empty for the first time, in low golden light.",
             act="The water runs down the stone channel and fills the small pool, which spills over its lip, the young trees sway in the evening wind, and the haul rope lies still over the bullwheel.")
S[79] = dict(title="IŞIK ①", ne="⭐ IŞIK: yakın istasyonun lambaları gruplar hâlinde, her grup tek seferde yanar — önce salon içi, sonra peron, en son merdiven ve bahçe.",
             mf="The lamps of the near station come on in groups, each group at once, from the lamps inside the hall to the lamps along the deck and last to the lamps on the stair and in the garden.",
             flow="The lamps lit in the first group warm the hall behind the arch glass in one step; a beat later the deck lamps come on together, then the stair and garden lamps, and the cabin's own interior lamp. The water keeps running and the young trees sway.")

F[80] = dict(mom="the near station is lit, and the far station is still dark.",
             act="The water runs down the stone channel and fills the small pool, the young trees sway in the evening wind, and the lit hall stands still behind its glass.")
S[80] = dict(title="IŞIK ②", ne="Karşı istasyonun ve seyir alanının lambaları gruplar hâlinde yanar. İki istasyon da yanık; aralarında halatlar akşam göğüne karşı ince çizgi.",
             mf="The lamps of the far station and its viewing terrace come on in groups, each group at once, from the hall of the far station to its deck and last to the terrace railing.",
             flow="Across the valley the far hall lights up in one step, then its deck, then the small lamps along the terrace railing, and the ropes between the two lit stations show as fine dark lines against the evening sky. The water runs on beside the stair.")

# ═══ PERDE 10 ══════════════════════════════════════════════════════════════
F[81] = dict(mom="both stations are lit, and the cableway is ready.",
             act="An attendant walks out through the hall and opens the tall timber doors at the head of the stair, the water fills the pool and runs over its lip, and the young trees sway in the evening wind.")
S[81] = dict(title="İLK ZİYARETÇİLER", ne="Giriş kapısı açılır; görevli kapının yanında. İlk ziyaretçiler (6 yetişkin, uzaktan, yüz okunmaz) soldaki patikadan YÜRÜYEREK gelir.",
             mf="Six visitors walk in along the gravel path from the left edge of the frame to the foot of the stair, and the attendant opens the doors at its head.",
             flow="The visitors enter the frame at the left one after another, small figures seen from the side and from behind, and walk the path between the young trees to the stair foot, where they gather. The water runs on beside the stair.")

F[82] = dict(mom="the first six visitors stand at the foot of the stair.",
             act="The six visitors start to climb the stair, the attendant swings the doors wide at its head, and the water runs down the channel beside them.")
S[82] = dict(title="PERONA", ne="Ziyaretçiler merdiveni çıkar, salonun içinden (cam kemerlerin ardında silüetler) perona yürür.",
             mf="The six visitors climb the stair from the yard to the doors and walk through the lit hall, silhouettes behind the arch glass, out onto the boarding deck to the cabin door.",
             flow="The small figures go up the steps and through the doors, pass as dark silhouettes along the lit glass of the arches and come out onto the timber deck, where they stop by the cabin.")

F[83] = dict(mom="six visitors wait on the deck at the cabin door.",
             act="The attendant pulls the cabin door open, the first visitor steps in, and a second group of four visitors walks along the garden path from the left towards the stone terrace.")
S[83] = dict(title="BİNİŞ", ne="Kapı açılır, ziyaretçiler tek tek biner; kapı kapanır. İkinci grup (4 kişi) bahçe patikasından teras banklarına yürür. Güneş battı.",
             mf="The six visitors step one by one from the deck into the cabin, the attendant slides its door shut, and a second group of four walks along the garden path from the left to the terrace benches and sits down.",
             flow="The deck empties as the cabin fills, six silhouettes settling behind its lit windows. The four newcomers walk in from the left edge between the young trees and sit on the benches.")

F[84] = dict(mom="six passengers sit in the lit cabin, and four more visitors sit on the terrace.",
             act="The bullwheel hauls the lit cabin out from the boarding deck at natural speed, its hanger arm swinging slightly, the attendant on the deck watches it go, and a crew of four visitors on the terrace benches turns towards it.")
S[84] = dict(title="KALKIŞ", ne="Kabin kalkar, perondan ayrılır. Gerçek hız, mavi saat.",
             mf="The bullwheel hauls the lit cabin with its six passengers out from the near boarding deck, under the headframe and onto the open ropes, to about fifteen metres out.",
             flow="The cabin moves off smoothly, rocks once as its carriage passes the headframe saddle, and glides out over the dark drop, its windows warm. The attendant and the visitors on the terrace stay still, backs to the camera, no readable face. The water runs on beside the stair.")

F[85] = dict(mom="the first passengers are on their way across the valley.",
             act="The haul rope pulls the lit cabin on across the valley at natural speed, its hanger arm steady, the water runs down the channel, and a crew of four visitors on the terrace benches watches.")
S[85] = dict(title="BOŞLUĞUN ÜSTÜNDE", ne="Kabin boşluğun üstünde ilerler.",
             mf="The haul rope draws the lit cabin from about fifteen metres out to about fifty metres out over the valley.",
             flow="The cabin glides on steadily against the darkening far slope, the six silhouettes still in its windows. The visitors on the terrace stay still, backs to the camera, no readable face. The water runs on.")

F[86] = dict(mom="the lit cabin crosses the valley with its first passengers.",
             act="The haul rope pulls the lit cabin towards the middle of the valley at natural speed, its hanger arm steady, the water runs down the channel, and a crew of four visitors on the terrace benches watches.")
S[86] = dict(title="ORTA", ne="Kabin vadinin ortasını geçer; ışıklı pencerelerinde silüetler. En sessiz an — son büyük soru: varacak mı?",
             mf="The haul rope draws the lit cabin from about fifty metres out to about eighty-five metres out, past the middle of the valley.",
             flow="The small lit box passes over the deepest part of the drop, and the ropes hold their fine dark line across the blue. The visitors on the terrace stay still, backs to the camera, no readable face.")

F[87] = dict(mom="the lit cabin has passed the middle of the valley.",
             act="The haul rope pulls the lit cabin up towards the far station at natural speed, its hanger arm steady, the water runs down the channel, and a crew of four visitors on the terrace benches watches.")
S[87] = dict(title="VARIŞ", ne="Kabin yavaşlayarak karşı perona girer ve durur.",
             mf="The haul rope draws the lit cabin from about eighty-five metres out up into the far station, where it slows and stops at the far boarding deck.",
             flow="The cabin climbs the last stretch, slows under the far headframe and stops at the lit far deck. The visitors on the near terrace stay still, backs to the camera, no readable face.")

F[88] = dict(mom="the first passengers have arrived at the far station.",
             act="A tiny far attendant pulls the cabin door open, the six tiny passengers step out one by one onto the far deck, the cabin's hanger arm steady, the water runs down the channel on this side, and a crew of four visitors on the near terrace watches.")
S[88] = dict(title="İNERLER", ne="Kapı açılır; ziyaretçiler tek tek inip seyir alanına yürür.",
             mf="The cabin door slides open at the far boarding deck, and the six passengers step out one by one and walk from the deck towards the viewing terrace on the rock knoll.",
             flow="Six tiny figures leave the cabin and move in a short line along the lit far deck towards the terrace. On this side the water runs on and the visitors on the terrace stay still, backs to the camera, no readable face.")

F[89] = dict(mom="the passengers walk from the far deck to the viewing terrace, and the empty cabin waits with its door open.",
             act="Six tiny figures walk from the far deck onto the viewing terrace, a tiny far attendant pulls the cabin door shut, the water runs down the channel on this side, and a crew of four visitors on the near terrace benches shifts slightly.")
S[89] = dict(title="İŞLEV ANI", ne="⭐ İLK YOLCULAR seyir alanının korkuluğuna varır (0–4 sn); BOŞ KABİN DÖNÜŞE BAŞLAR (4 sn'de kımıldar, 8 sn'de ≈10 m açıkta). Su akar, ışıklar yanık. Film hareket hâlinde 12:00'da biter.",
             mf="The six passengers walk from the end of the far deck onto the viewing terrace and stop at its railing, and the empty lit cabin starts back from the far boarding deck onto the open ropes towards this side.",
             flow="From the first frame to about four seconds the six tiny figures walk out along the terrace and stop in a row at its railing above the valley. From about four to eight seconds the empty lit cabin starts back from the far deck and glides slowly about ten metres out onto the ropes; the water runs on beside the stair, the lamps of both stations stay on, the visitors on the near terrace stay seated, backs to the camera, no readable face, and nothing else changes.")

F[90] = dict(mom="deep blue hour on the first evening — the first passengers stand at the far terrace railing, and the empty cabin has started back.",
             act="The empty lit cabin glides slowly back onto the ropes from the far deck, the water runs down the channel into the pool, six tiny figures stand at the far terrace railing, and four visitors sit on the near terrace benches.")

USTA = """> Üretim sırasının İLK karesi: G90 önce üretilir ve ikna edici değilse DURULUR; sonra image-to-image geriye
> G89 → … → G0. Kapı: mavi saat (güneş ≈ −2°) · iki istasyon yanık · kırmızı kabin karşı perondan ≈10 m ayrılmış ·
> seyir terasında altı küçük silüet · yakın terasta dört kişi · su akıyor · çan kemeri x 1328–1392 · vinç, iskele,
> kamyon YOK (SÖKÜM). Kapak (onaydan sonra `THE_SKY_STATION_KAPAK.md`) bu promptun kopyası + başlık bandı satırıdır;
> öncesi/sonrası bölme YOK."""
