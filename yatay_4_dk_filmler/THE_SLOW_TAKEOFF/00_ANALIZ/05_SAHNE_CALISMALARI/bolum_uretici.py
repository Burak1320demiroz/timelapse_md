# THE SLOW TAKEOFF — bölüm dosyası üretici (ortak bloklar tek kaynaktan, DERS 20)
# KULLANIM (depo kökünden):
#   python3 yatay_4_dk_filmler/THE_SLOW_TAKEOFF/00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py yatay_4_dk_filmler/THE_SLOW_TAKEOFF
#   → THE_SLOW_TAKEOFF_BOLUM_1.md + _BOLUM_2.md yeniden yazılır; ardından prompt_kontrol.py klasör modunda koşulur.
# ⛔ ÜRETİM BAŞLADIKTAN SONRA KOŞULMAZ: üretilmiş filmin promptu kanıttır (URETIM_GUNLUGU kuralı).
# ⛔ Bölüm dosyası elle düzeltilirse bu betik o düzeltmeyi EZER — düzeltme önce buraya yazılır.
import math, os, sys

FILM = "THE_SLOW_TAKEOFF"
OUT = sys.argv[1] if len(sys.argv) > 1 else "."

# ── güneş (47° K · δ +12° · güneş saati) ─────────────────────────────────
phi, dec = math.radians(47.0), math.radians(12.0)
def sun(t):
    h = math.radians((t - 12) * 15)
    se = math.sin(phi) * math.sin(dec) + math.cos(phi) * math.cos(dec) * math.cos(h)
    e = math.degrees(math.asin(se))
    az = (math.degrees(math.atan2(math.sin(h), math.cos(h) * math.sin(phi) - math.tan(dec) * math.cos(phi))) + 180) % 360
    return round(az), e
def hm(s):
    a, b = s.split(":"); return int(a) + int(b) / 60

def sunline(t):
    az, e = sun(hm(t))
    if e >= 0.5:
        return f"Sun azimuth {az} degrees, elevation {round(e)} degrees"
    if e > -0.5:
        return f"Sun azimuth {az} degrees, elevation 0 degrees"
    return f"Sun azimuth {az} degrees, elevation {max(1, round(-e))} degree{'s' if round(-e) > 1 else ''} below the horizon"

# ── ortak bloklar ───────────────────────────────────────────────────────────
HEAD_MAIN = ("Photorealistic documentary site photograph — Scene {n} of 30. Horizontal 16:9 time-lapse of a retired "
             "jet airliner in a lakeside meadow being made into a lake house; a progress photograph from a fixed "
             "24 mm site camera.")
HEAD_USTA = ("Photorealistic documentary site photograph — master frame G30, the target frame of the last shot "
             "(Scene 29 of 30). Horizontal 16:9 time-lapse of a retired jet airliner in a lakeside meadow made into "
             "a lake house; a progress photograph from a fixed 24 mm site camera.")
HEAD_COCK = ("Photorealistic documentary interior photograph — Scene {n} of 30. Horizontal 16:9 time-lapse inside the "
             "cockpit of a retired jet airliner beside a lake being made into a lake house; a progress photograph from "
             "a fixed 24 mm camera inside the cockpit.")
HEAD_COCK_SON = ("Photorealistic documentary interior photograph — the last frame of Scene {n} of 30. Horizontal 16:9 "
                 "time-lapse inside the cockpit of a retired jet airliner beside a lake being made into a lake house; a "
                 "progress photograph from a fixed 24 mm camera inside the cockpit.")
CAM_MAIN = ("Camera: MAIN STATION — fixed tripod bolted to a concrete footing on the low grassy bank south of the "
            "meadow, lens 3.0 metres above the meadow, 50 metres from the centre of the fuselage along the lens axis, "
            "bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.")
CAM_COCK = ("Camera: COCKPIT STATION — fixed clamp mount bolted to the rear wall of the cockpit, lens 8.2 metres above "
            "the meadow, 2.4 metres from the windscreen, bearing 270 degrees, tilt 0 degrees, zero roll. The camera "
            "never moves.")
STRUCT = ("STRUCTURE: When finished this will be a lake house made from one retired twin-engine jet airliner, "
          "33 metres long, with a timber terrace round its near wing.")
SITE_MAIN = ("SITE / BACKGROUND: A low lakeside meadow seen from a grassy bank. One big old oak stands on a slight dry "
             "rise at the left edge of the frame, its trunk near the left edge and its crown reaching towards the "
             "top-left corner. Far back on the right, on the lake shore, stands one old timber boathouse with a dark "
             "shingle roof on short timber piles. At the lower right, at the foot of the grassy bank, sits one big grey "
             "lichen-spotted boulder. Behind the meadow the lake runs across the whole frame, and the far shore is a "
             "low line of dark wooded hills; the far shoreline runs dead level at exactly half the frame height. The "
             "meadow holds exactly one aircraft, this one; no other fuselage, wing or tail fin stands anywhere in "
             "view, and the shore and the hills carry only grass, reeds and trees.")
SITE_COCK = ("SITE / BACKGROUND: The cockpit of the raised airliner, seen from its rear wall looking forward over the "
             "nose through six windscreen panes in their curved frames, with a curved white ceiling and white side "
             "walls each holding one small side window. Through the left panes rises the crown of the one big old oak "
             "on its slight dry rise; ahead and to the right, beyond the meadow below, the lake runs out to the far "
             "shore, and the far shore is a low line of dark wooded hills; the far shoreline runs dead level at "
             "exactly half the frame height.")
NEG_MAIN = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The oak, the boathouse, the boulder, the "
            "lake shore, the far wooded hills and the far shoreline never change shape, position, size or spacing. The "
            "airliner is one rigid body that keeps its length, nose, wings, tail fin and window row in every frame; "
            "nothing already built is removed or resized; no opacity fades. No readable text, letters, digits, numbers "
            "or symbols anywhere in the frame, on any surface, the fuselage, the wings and the tail fin included. "
            "Nothing here has been branded, labelled, numbered or annotated by anyone: the fuselage, the wings and the "
            "tail fin carry one plain weathered off-white paint from nose to tail and nothing else. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI "
            "aesthetic.")
NEG_COCK = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The windscreen frames, the curved "
            "ceiling, the oak crown through the left panes, the far wooded hills and the far shoreline never change "
            "shape, position, size or spacing. The cockpit keeps the shape of its six windscreen panes and its curved "
            "white walls; nothing already built is removed or resized; no opacity fades. No readable text, letters, "
            "digits, numbers or symbols anywhere in the frame, on any surface, the walls and the furniture included. "
            "Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no "
            "fades. No architectural visualisation look, no CGI aesthetic.")
OUTPUT = "Output: 16:9, 4K, no text, no watermark."
CREW = "Crew register only as faint soft motion streaks beside their machines, never as sharp figures."
FILMSTOCK = "A documentary site photograph on colour negative film, true colour, fine grain."
FILMSTOCK_IN = "A documentary interior photograph on colour negative film, true colour, fine grain."

COMP_HEAD = ("COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The boathouse on "
             "the right spans about 150 pixels of frame width — about one thirteenth — from about 1550 to 1700 pixels "
             "from the left, and keeps that width and position in every frame. The airliner spans about 850 pixels of "
             "frame width, from a little over a quarter to a little under three quarters of the frame width, ")
COMP_PRE = ("its belly on the meadow at about forty-three percent of frame height, the top of its fuselage at about "
            "fifty-two percent, just above the far shoreline, and the top of its tail fin at about sixty-eight percent.")
COMP_MID = ("its belly level with the far shoreline at exactly half the frame height, the top of its fuselage at "
            "about fifty-nine percent and the top of its tail fin at about seventy-five percent.")
COMP_POST = ("its belly at about fifty-seven percent of frame height, above the far shoreline, the top of its "
             "fuselage at about sixty-six percent and the top of its tail fin at about eighty-two percent, below the "
             "top eighth of the frame.")
COMP_TAIL = ("The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth "
             "or the top-right corner of the frame.")
COMP_COCK = ("COMPOSITION: Horizontal 16:9. The far shoreline sits at exactly half the frame height. The six windscreen "
             "panes span about 1500 pixels of frame width — about four fifths — across the upper middle of the frame "
             "and keep that width and position in every frame; the floor and the furniture fill the lower third. "
             "Nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.")

TR_A = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, "
        "vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay "
        "almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay "
        "recognisable, trailing light motion blur. Nothing moves at normal speed.")
TR_B = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, "
        "vehicles and crew all move at the same accelerated speed. Two hours pass across this shot: the shadows swing "
        "slowly round, the clouds streak across the sky, and machines smear into heavy motion blur. Nothing moves at "
        "normal speed.")
TR_B_GREY = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, falling snow or rain, "
             "water, machines, vehicles and crew all move at the same accelerated speed. Two hours pass across this "
             "shot: the grey cloud deck rolls slowly over from the left, the ground changes colour under the weather, "
             "and vehicles smear into heavy motion blur. Nothing moves at normal speed.")
TR_A_IN = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds and the light outside, the "
           "rain and the water, and any crew inside all move at the same accelerated speed. Ten minutes pass across "
           "this shot: the light shifts only a little, the clouds drift in one smooth flow, and the crew trail light "
           "motion blur. Nothing moves at normal speed.")
TR_G = ("TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the water "
        "ripples, the reflections tremble and the canoe glides at its real pace; nothing is accelerated.")

I2V_HEAD = ("The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its "
            "last frame is that image, matched frame for frame — same framing, same light, same objects in the same "
            "places.")
LOCK_MAIN = ("The camera does not move at any point. The framing is identical in the first and last frame. The oak, the "
             "boathouse, the boulder, the lake shore, the far wooded hills and the far shoreline stay exactly where they are, at "
             "exactly the same size and shape, for the whole shot; the boathouse occupies exactly the same width of "
             "the frame in the first and last frame, and the far shoreline stays at exactly half the frame height. The "
             "meadow holds exactly one aircraft, and no other fuselage, wing or tail fin appears anywhere. Nothing "
             "already built is removed or resized.")
LOCK_COCK = ("The camera does not move at any point. The framing is identical in the first and last frame. The "
             "windscreen frames, the curved ceiling, the oak crown through the left panes, the far wooded hills and "
             "the far shoreline stay exactly where they are, at exactly the same size and shape, for the whole shot; "
             "the windscreen occupies exactly the same width of the frame in the first and last frame, and the far "
             "shoreline stays at exactly half the frame height. Nothing already built is removed or resized.")
I2V_TAIL = ("Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
            "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
            "documentary time-lapse cinematography.")
I2V_TAIL_COCK = ("Camera: fixed clamp mount, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
                 "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
                 "documentary time-lapse cinematography.")

# ── evin tamam hâli (S17 sonrası her karede birebir) ──────────────────────
HOUSE = ("The retired airliner stands fixed at its final height, its belly six metres above the ground, on two curved "
         "steel saddle beams pinned to two red steel frames; a pale timber terrace with slim steel railings, two "
         "benches and four planters surrounds the near wing root; a grey steel stair with timber steps runs from the "
         "dry rise under the oak to the forward cabin door; all its windows are clear dark glass.")
RAISED = ("The airliner sits fixed at its final height on its two curved steel saddle beams pinned to the red steel frames, its belly six metres above the meadow, the four lifting cables hanging slack from the jack units on "
          "the top beams.")

# ── sahne verisi ─────────────────────────────────────────────────────────────
# her kare: id, saat, istasyon (M/K), rejim (A/B/G), stage, moment, comp, light, activity, texture, physics
# her klip: mf, body
S = []
def scene(**k): S.append(k)

T_SUMMER = ("Green moss and black grime streaks along the fuselage, ivy over the nose, flaking grey paint on the "
            "wings, a ring of damp mud round the belly and old ruts in the grass, a gravel pad with fresh tyre "
            "tracks, dew on the long grass. " + FILMSTOCK)
T_WORK = ("Dry matte light-grey concrete with formwork edges and spatter on the grass, red primer on the steel with rust-brown streaks at the "
          "bolts, heaps of brown spoil, mud and tyre ruts round the footings, cut grass flattened into tracks, dried "
          "mud along the belly. " + FILMSTOCK)
T_LIFT = ("The empty trough below as a raw scar of damp mud printed with the shape of the belly, clods of mud fallen "
          "into it, red primer on the steel with rust-brown streaks at the bolts, spoil heaps by the footings, tyre "
          "ruts and tracks across the cut grass. " + FILMSTOCK)
T_FIT = ("Pale new timber with sawdust in the joints, grey steel and red primer, fallen oak leaves drifting on the "
         "grass, tyre ruts and a muddy gravel track, packing film and offcuts in a skip, the old trough below drying "
         "into cracked mud. " + FILMSTOCK)
T_WINTER = ("A thin even snow cover with soft blue-grey shadows, black wet bark on the bare oak, a line of frost on "
            "the railings, slush in the tyre ruts, a grey film of ice at the lake edge. " + FILMSTOCK)
T_FLOOD = ("Brown-grey floodwater with drifting twigs and foam lines, silt bands left on the grass, wet black bark, "
           "rain streaks down the fuselage, rain-darkened timber, mud along the foot of the dry rise. " + FILMSTOCK)
T_SPRING = ("Wet silt lines across the new grass, raw brown soil banks edged with packed grey stones, fresh spoil "
            "heaps by the channel, mud stains on the stepping stones, a gravel track with tyre ruts. " + FILMSTOCK)
T_DUSK = ("Calm dark water with trembling reflections, dew on the new grass, damp dark timber on the walkway, a thin haze and a film "
          "of mist low over the lake, faint tyre tracks on the gravel track, faint silt stains on the lower columns, a band of young reeds round the pond. "
          + FILMSTOCK)

LIGHT_DESC = {
 "am_low": ("low on the right and slightly behind the camera, so the near side of the fuselage is lit warm and long "
            "shadows fall to the left and away. Late summer: a clear pale morning sky with a few small high clouds, "
            "a thin mist lifting off the lake, the meadow deep green and the oak in full dark leaf."),
 "am_high": ("high on the right behind the camera, lighting the near side of the fuselage, with short shadows falling "
             "to the left and away. Early autumn: a clear blue sky with small white fair-weather clouds, the meadow "
             "turning yellow-green and the oak still green with the first yellow leaves."),
 "noon": ("high behind the camera, lighting the near side of the fuselage evenly, with short shadows falling away "
          "from the camera. Mid autumn: a soft blue sky with scattered white clouds, the oak gold."),
 "pm_high": ("high on the left behind the camera, lighting the near side of the fuselage, with short shadows falling "
             "to the right and away. Late autumn: a pale sky with high thin cloud, the oak bronze and thinning."),
 "pm_grey": ("hidden behind a thick, even grey cloud deck, so the light is flat and soft and shadows are faint and "
             "fall to the right. Late autumn turning to winter: a low grey sky, the oak brown and almost bare."),
 "snow": ("showing only as a pale glow through thinning grey cloud on the left, the light soft and cool, with faint "
          "shadows to the right. Winter: thin snow on the ground and the oak bare and black."),
 "flood": ("very low on the left under the lifting edge of the rain clouds, raking warm light along the water and the "
           "near side of the house, with long shadows reaching to the right and slightly towards the camera. Spring: "
           "a broken grey sky clearing from the left, the oak with a first green haze."),
 "spring": ("very low on the left, almost level, laying warm raking light along the near side of the house and long "
            "shadows to the right and slightly towards the camera. Late spring: a clear sky turning gold, the oak in "
            "fresh light green leaf and the meadow green."),
 "sunset": ("on the horizon on the left, outside the frame, its last level warm light touching only the top of the "
            "tail fin and the crown of the oak while the rest of the meadow lies in soft shade. Early summer: a clear "
            "sky turning gold low on the left and blue on the right."),
 "dusk": ("on the left outside the frame, so there is no direct sun: a soft afterglow low in the sky on the left and "
          "the cool blue of dusk spreading from the right. Early summer: a clear sky with a few high thin clouds."),
 "blue": ("on the left outside the frame, so there is no direct sun: deep blue hour, the sky deep clear blue with a "
          "last pale band low on the left and a few high thin clouds. Early summer."),
}
def LIGHT(t, key, extra=""):
    return f"LIGHTING: {sunline(t)}, {LIGHT_DESC[key]}{(' ' + extra) if extra else ''} The sun stays outside the frame."

# ---------- S0 ----------
scene(n=0, fiil="SÖKER", eleman="öndeki motor kanatta → vinçte, kamyonun üstünde (%100)", rejim="A", t0="07:40", t1="07:50",
 st="M", g="G0",
 stage=("nothing has been moved yet except the near engine. The airliner lies on its belly in the meadow, settled "
        "into a shallow muddy trough: a dull grey-white fuselage streaked with green moss "
        "and dark grime, thick ivy climbing over the nose and the cockpit windows, a long row of small cabin windows "
        "clouded and some broken, the tail fin standing tall at the right, the near wing reaching towards the camera "
        "with its tip propped on timber blocks in the grass. The near engine has just been lifted clear of its mounting "
        "under the near wing and hangs from the hook of a yellow mobile crane parked on a gravel pad in front of the "
        "tail; a flatbed truck waits beside the crane. Long grass, nettles and young birches crowd round the fuselage."),
 moment=("A quarter to eight in the morning on the first day of work: the near engine has just come off the wing and "
         "hangs a metre above the grass beside it, and the ivy still covers the nose."),
 comp=COMP_PRE + " The near engine hangs just above the grass at about the middle of the frame width.",
 light=LIGHT("07:40", "am_low"),
 tr=TR_A,
 act=("The mobile crane swings the near engine away from the wing towards the flatbed truck, two workers on the "
      "ground steady it with taglines, and a small excavator pulls the timber blocks out from under the near wingtip; "
      "the crane carries a visible load, with a heavy engine slung on the hook. Crushed grass and fresh tyre tracks "
      "mark the gravel pad. " + CREW),
 tex=T_SUMMER,
 phys=("The airliner rests on its belly in the soft ground of the meadow, pressed into a shallow trough. The near "
       "engine hangs from the crane hook on two taut slings, and the crane stands on its outriggers on the gravel pad. "
       "The near wingtip rests on two timber blocks."),
 mf=("The mobile crane swings the near engine from beneath the near wing across to the flatbed truck and holds it "
     "just above the truck bed."),
 body=("Ten minutes pass in the early light. Everything in this shot is time-lapsed at the same rate. From the first "
       "frame the engine is already moving: it swings slowly away from the wing on the crane hook, steadied by two "
       "taglines, and travels across to hang just above the bed of the flatbed truck. The excavator drags the timber "
       "blocks out from under the wingtip and stacks them on a pile beside the pad. The ivy over the nose, the clouded "
       "windows and the tail fin do not change. Thin morning mist lifts off the lake behind, and the small high clouds "
       "drift slowly from the left in one smooth flow. Long shadows lean to the left."))

# ---------- S1 ----------
scene(n=1, fiil="TEMİZLER", eleman="sarmaşık + kir %100 → %0 · motor kamyonda, vinç gider", rejim="A", t0="07:50", t1="08:00",
 st="M", g="G1",
 stage=("the near engine has been carried off the wing and hangs from the crane hook on its sling just above the bed "
        "of the flatbed truck parked in front of the tail, two taglines hanging slack from it; under the near wing its "
        "bare mounting shows as a short grey stub. The rest of the airliner is unchanged: it lies on its belly in the "
        "shallow muddy trough, a dull grey-white fuselage streaked with green moss and dark grime, thick ivy over the "
        "nose and the cockpit windows, clouded cabin windows, the tail fin tall at the right, the near wing reaching "
        "towards the camera. Two mobile work platforms and a pressure-washer cart wait by the nose; long grass, nettles "
        "and young birches crowd round the fuselage."),
 moment="Ten to eight in the morning: the engine hangs over the truck bed, and the clean-up of the fuselage is about to start.",
 comp=COMP_PRE + " The engine hangs over the truck at about two thirds of the frame width.",
 light=LIGHT("07:50", "am_low"),
 tr=TR_A,
 act=("The crane lowers the engine onto the flatbed truck, a team on two mobile work platforms pulls the ivy off the "
      "nose in long strips, and a pressure-washer cart sprays the first band of grime off the fuselage; the crane "
      "carries a visible load, with a heavy engine slung on the hook. Cut ivy piles up on a tarpaulin under the nose. "
      + CREW),
 tex=T_SUMMER,
 phys=("The engine hangs from the crane hook on two taut slings a metre above the truck bed. The crane stands on its "
       "outriggers on the gravel pad and the truck stands on its wheels beside it. The airliner rests on its belly in "
       "the trough."),
 mf=("A team on two mobile work platforms strips the ivy and the grime from the fuselage, from the nose back to the "
     "tail, and drops the cut ivy onto a tarpaulin pile under the nose."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Early in the shot the crane lowers "
       "the engine onto the truck bed; the truck drives off along the gravel track to the right, and the crane folds "
       "its boom and follows it out of the frame. Meanwhile the work platforms creep along the fuselage: the ivy comes "
       "away in long strips, and behind the pressure-washer the old white surface appears in clean bands — the nose "
       "first, then the cabin, then the tail. Cut ivy piles up on the tarpaulin, and the small excavator lifts the cut "
       "birches onto a trailer. The small high clouds drift slowly from the left in one smooth flow and the mist over "
       "the lake thins. Long shadows lean to the left."))

# ---------- S2 ----------
scene(n=2, fiil="DÖKER", eleman="temel 0 → 4 (%100) · gövde temiz", rejim="B", t0="08:00", t1="10:00",
 st="M", g="G2",
 stage=("the airliner has been cleaned: it lies on its belly in the shallow muddy trough, its long fuselage now clean "
        "old white with faded grey on the belly, the cockpit windows and the row of cabin windows uncovered but old "
        "and clouded, some broken, the tail fin tall at the right, the near wing reaching towards the camera, and under "
        "the near wing a short grey stub where the engine hung. The grass round it has been cut short and a tarpaulin "
        "heaped with cut ivy lies under the nose. A yellow excavator waits on the gravel pad, with a stack of rebar cages "
        "and a pile of timber boards beside it; stakes with orange tape mark two squares in the grass in front of the "
        "fuselage, one ahead of the wing and one behind it, and two matching squares lie behind the fuselage."),
 moment="Eight in the morning: the fuselage is clean white and the footing squares are staked out in the grass.",
 comp=COMP_PRE + " The two staked squares in front of the fuselage sit at about two fifths and three fifths of the frame width.",
 light=LIGHT("08:00", "am_low"),
 tr=TR_B,
 act=("The excavator digs the first footing pit beside the fuselage and swings the spoil onto a heap, a concrete mixer "
      "truck backs along the gravel track, and the crew lowers a rebar cage into the open pit; fresh tyre ruts cut "
      "across the short grass. " + CREW),
 tex=T_WORK,
 phys=("The airliner rests on its belly in the trough. The excavator stands on its tracks on the gravel pad, its "
       "bucket bearing on the ground at the pit edge. The rebar cages lie stacked on timber bearers that rest on the grass."),
 mf=("The excavator digs four square footing pits beside the fuselage, the crew lowers a rebar cage from the stack "
     "into each pit, and the mixer truck pours concrete from its chute into the pits, nose side first, then tail side."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The excavator works its way round the "
       "fuselage, digging and swinging spoil onto heaps; each pit gets its rebar cage and then its grey concrete, and "
       "four ringed groups of anchor bolts stand out of the fresh tops, two in front of the fuselage and two behind it. "
       "The mixer truck comes and goes along the gravel track. Late in the shot the yellow mobile crane drives back in "
       "and parks on the pad in front of the tail, and a long truck brings a load of red steel columns and beams and "
       "stops beside it; the crane lifts the first column from the truck. The shadows of the fuselage and the oak "
       "swing slowly from the left towards the back of the meadow as the sun climbs, and the clouds streak slowly across from the left."))

# ---------- S3 ----------
scene(n=3, fiil="DİKER", eleman="çerçeve 0 → 2 (kolon 4 · üst kiriş 2) %100", rejim="A", t0="10:00", t1="10:10",
 st="M", g="G3",
 stage=("four square concrete footings have been poured beside the fuselage, two in front of it and two behind it, "
        "each with a ring of anchor bolts standing out of its fresh grey top and a heap of brown spoil beside it. The "
        "airliner lies unchanged on its belly in the trough, clean old white, its cockpit and cabin windows clouded, "
        "the tail fin tall at the right, the near wing reaching towards the camera. The yellow mobile crane stands on "
        "its outriggers on the gravel pad in front of the tail and lifts the first red steel column on a short sling "
        "from a long truck loaded with columns and beams; the excavator and the mixer truck are parked at the right."),
 moment="Ten in the morning: the four footings are poured and the first steel column is in the air.",
 comp=COMP_PRE + " The two near footings sit at about two fifths and three fifths of the frame width.",
 light=LIGHT("10:00", "am_high"),
 tr=TR_A,
 act=("The crane lifts a red steel column from the truck and swings it onto the first footing, two riggers bolt its "
      "base plate down, and a telehandler carries a bundle of bracing from the truck; the crane carries a visible load, "
      "with a red steel column on the hook. Concrete spatter and spoil heaps lie round the footings. " + CREW),
 tex=T_WORK,
 phys=("The column hangs from the crane hook on a short sling, its base plate just above the anchor bolts of the "
       "footing. The crane stands on its outriggers on the gravel pad. The airliner rests on its belly in the trough, "
       "and the footings are planted in the ground beside it."),
 mf=("The crane lifts the red steel columns one by one from the long truck onto the anchor bolts beside the fuselage "
     "and then sets two red top beams across them, one ahead of the wing and one behind it, forming two steel frames "
     "that straddle the fuselage."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Each column swings over on the hook, "
       "is lowered onto its anchor bolts and bolted down while a rigger holds it plumb; then a top beam rises from the "
       "truck on the hook and is lowered across each pair of columns, high above the fuselage. The telehandler lifts "
       "four small grey jack units from the truck onto the beam tops, two on each beam, with their lifting cables "
       "coiled beside them. The airliner does not move. The small white clouds drift slowly from the left in one smooth "
       "flow, and the short shadows lean to the left and away."))

# ---------- S4 ----------
scene(n=4, fiil="BAĞLAR", eleman="beşik 0 → 2 · halat 0 → 4 gergin · uçak yerde", rejim="A", t0="10:10", t1="10:20",
 st="M", g="G4",
 stage=("two red steel steel frames now straddle the fuselage, one between the cockpit and the wing and one between "
        "the wing and the tail: each is two tall columns bolted on the concrete footings, one in front of the fuselage "
        "and one behind it, joined high above the fuselage by a red top beam carrying two small grey jack units with "
        "coiled lifting cables. The airliner lies unchanged on its belly in the trough between them, clean old white, "
        "its windows clouded. The yellow mobile crane stands on its outriggers on the gravel pad in front of the tail "
        "and holds the first curved steel saddle beam on a sling; the excavator digs a narrow trench under the belly "
        "beside the first steel frame."),
 moment="Ten past ten: both steel frames stand over the fuselage and the first saddle beam is on the hook.",
 comp=COMP_PRE + " The two steel frames rise at about two fifths and three fifths of the frame width, their top beams at about seventy percent of frame height.",
 light=LIGHT("10:10", "am_high"),
 tr=TR_A,
 act=("The excavator digs a narrow trench under the belly at each steel frame, the crane threads a curved steel saddle "
      "beam through each trench beneath the fuselage, and riggers on the beam tops pull the lifting cables down and "
      "shackle them to the saddle ends; the crane carries a visible load, with a curved saddle beam on the hook. Spoil "
      "from the trenches lies in two heaps. " + CREW),
 tex=T_WORK,
 phys=("The saddle beam hangs from the crane hook on a short sling. The frame columns stand bolted on their footings "
       "and the top beams are bolted across them, each carrying its jack units. The airliner rests on its belly in the "
       "trough."),
 mf=("The crane threads two curved steel saddle beams from the truck into trenches under the belly, and the riggers "
     "draw the lifting cables down from the jack units on the top beams onto the saddle ends and pull them taut."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The crane lifts the second saddle "
       "beam from the truck and threads it under the belly at the second steel frame. When both saddles are in place "
       "the four cables are drawn tight one after another and stand straight and taut from the beam tops down to the "
       "saddle ends; the airliner has not yet moved. The crane then folds its boom and drives off along the gravel "
       "track to the right and out of the frame, and the excavator backfills the trench edges. The small white clouds "
       "drift slowly from the left in one smooth flow, and the short shadows lean to the left and away."))

# ---------- S5 ----------
scene(n=5, fiil="KALKAR ①", eleman="uçak 0 → +3,0 m (%50) · halatlar çeker", rejim="A", t0="10:20", t1="10:30",
 st="M", g="G5",
 stage=("the airliner is ready to rise but has not moved: it lies on its belly in the trough between the two red "
        "steel frames, and under its belly at each frame a curved steel saddle beam runs across beneath the fuselage, "
        "its two ends shackled to two taut steel lifting cables and their slings, which run straight up to the jack "
        "units on the red top beam. The cables are drawn tight; the fuselage is still pressed into the mud. The clean "
        "old white fuselage, the clouded windows, the tall tail fin at the right and the near wing reaching towards the "
        "camera are unchanged. A telehandler and two work platforms stand at the right, and the excavator is parked by "
        "the nose; backfilled spoil lies round the saddle ends."),
 moment="Twenty past ten: all four lifting cables are taut and the airliner is still on the ground — the moment before it rises.",
 comp=COMP_PRE + " The four taut cables run straight up from the belly to the top beams at about seventy percent of frame height.",
 light=LIGHT("10:20", "am_high"),
 tr=TR_A,
 act=("The four jack units on the top beams pull the cables up in short even strokes and lift the saddle beams with "
      "the airliner on them, riggers on the beam tops watch the cables, and the telehandler moves a work platform clear "
      "of the near wing; mud drips from the belly as it leaves the trough. " + CREW),
 tex=T_WORK,
 phys=("The airliner still rests on its belly in the mud, with the two saddle beams lying under it; each saddle end "
       "is shackled to one taut lifting cable running up to a jack unit bolted on a red top beam, and the frame "
       "columns stand bolted on their footings."),
 mf=("The four jack units on the red top beams draw the cables upward and raise the airliner, resting on its two "
     "saddle beams, straight up from the muddy trough to half of its final height."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the cables are "
       "pulling: the fuselage breaks free of the mud with a shudder of falling clods, then rises slowly and evenly, "
       "level, nose and tail together, the wings and the tail fin moving with it as one rigid body. A dark gap opens "
       "and widens beneath the belly, and the shallow muddy trough appears below it, its shape the exact print of the "
       "belly. By the end of the shot the belly hangs about three metres above the meadow. The telehandler lifts a "
       "pallet of steel pins from the truck up to the riggers on the first beam top. The small white clouds drift "
       "slowly from the left in one smooth flow, and the shadow of the airliner begins to slide out from under it to "
       "the left."))

# ---------- S6 ----------
scene(n=6, fiil="KALKAR ②", eleman="uçak +3,0 → +6,0 m (%100)", rejim="A", t0="10:30", t1="10:40",
 st="M", g="G6",
 stage=("the airliner hangs halfway up: its belly about three metres above the meadow, level, resting on the two "
        "curved saddle beams, which hang on their slings from four taut steel cables running up to the jack units on "
        "the red top beams of the two steel frames. Beneath it the shallow muddy trough lies open in the grass, the "
        "exact print of the belly, with clods of mud fallen into it. The fuselage is clean old white with clouded "
        "windows, the tail fin tall at the right, the near wing reaching towards the camera above the grass; the "
        "telehandler stands by the near wingtip with a pallet on its forks."),
 moment="Half past ten: the airliner hangs halfway up, its belly three metres above its empty muddy bed.",
 comp=COMP_MID + " The empty trough lies beneath it at about forty-three percent of frame height.",
 light=LIGHT("10:30", "am_high"),
 tr=TR_A,
 act=("The jack units keep drawing the cables up and raise the airliner the rest of the way, riggers on both beam tops "
      "ride with the cables, and the telehandler lifts a pallet of steel pins up to the first beam top; damp clods "
      "drop into the empty trough below. " + CREW),
 tex=T_LIFT,
 phys=("The airliner rests on the two saddle beams, and each saddle end hangs on one taut lifting cable from a jack unit bolted on a top beam. The frame columns stand bolted on their footings. The telehandler stands on its "
       "wheels on the cut grass."),
 mf=("The jack units on the red top beams draw the cables on upward and raise the airliner on its saddle beams from "
     "half height to its final height, its belly level with the lower branches of the oak."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The rise continues exactly as "
       "before, at the same steady pace and in the same straight upward line, the airliner level and rigid; the gap "
       "beneath it grows until the far columns and the far footings show clearly under the belly, and the empty muddy "
       "trough lies in full view below. The telehandler lifts a pallet of steel pins from the truck up to the riggers on "
       "the first beam top. The small white clouds drift slowly from the left in one smooth flow, and the shadow of the "
       "airliner on the meadow slides out from under it to the left and away."))

# ---------- S7 ----------
scene(n=7, fiil="OTURTUR", eleman="yük halattan çerçeveye (%100) · halatlar gevşer", rejim="A", t0="10:40", t1="10:50",
 st="M", g="G7",
 stage=("the airliner has reached its final height: its belly about six metres above the meadow, level with the lower "
        "branches of the oak, resting on the two curved saddle beams, which still hang on their slings from four taut "
        "steel cables running up to the jack units on the red top beams. Under the raised fuselage the far columns and "
        "the far footings now show, and below it lies the empty muddy trough, the exact print of the belly, wet and "
        "pitted with fallen clods. The fuselage is clean old white with clouded windows, the tail fin tall at the right, "
        "the near wing reaching towards the camera high above the grass. Riggers stand on both beam tops beside a "
        "pallet of steel pins; the telehandler waits by the near wingtip."),
 moment="Twenty to eleven: the airliner hangs at its final height and its weight is about to pass to the frames.",
 comp=COMP_POST,
 light=LIGHT("10:40", "am_high"),
 tr=TR_A,
 act=("Riggers slide steel pins through the saddle beam ends into brackets on the frame columns, the jack units pay "
      "out the cables a little so the saddles settle onto the brackets, and the telehandler lifts a pallet of steel "
      "brackets up to the second steel frame; the cables go from taut to slack. Mud dries in the trough below. " + CREW),
 tex=T_LIFT,
 phys=("The saddle beams rest on steel brackets pinned to the frame columns, and the airliner rests on the saddle "
       "beams. The frame columns stand bolted on their footings. Each lifting cable hangs slack from its jack unit, which stays bolted on its top beam."),
 mf=("The riggers pin the saddle beam ends to steel brackets on the frame columns, and the jack units pay out the "
     "four cables until the weight of the airliner passes from the cables onto the steel frames."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. First the pins go in at the first "
       "steel frame and then at the second; then the saddles settle a hand's width onto the brackets, and the four "
       "cables slacken one after another and hang in loose curves. The airliner does not move at all. The telehandler "
       "lifts a pallet of steel brackets from the truck up to the second steel frame. The small white clouds drift "
       "slowly from the left in one smooth flow, and the shadow of the airliner lies on the meadow to the left and away."))

# ---------- S8 ----------
scene(n=8, fiil="ÇATAR", eleman="teras çerçevesi 0 → %100 (dört ayak · kiriş)", rejim="A", t0="10:50", t1="11:00",
 st="M", g="G8",
 stage=("the airliner now sits fixed at its final height, its belly six metres above the meadow, on two curved steel "
        "saddle beams pinned to steel brackets on the two red steel frames; the four lifting cables and their slings "
        "hang slack in loose curves from the jack units on the top beams. Below lies the empty muddy trough. The "
        "fuselage is clean old white with clouded windows, the tail fin tall at the right, the near wing reaching "
        "towards the camera high above the grass. A long truck stands at the right loaded with grey steel beams and "
        "slim steel posts, a small piling rig waits beside it, and two work platforms stand under the near wing; a "
        "heap of spoil lies by the far footings."),
 moment="Ten to eleven: the airliner is fixed on its frames and the first steel for the terrace has arrived.",
 comp=COMP_POST + " The near wing reaches out above the grass towards the lower middle of the frame.",
 light=LIGHT("10:50", "am_high"),
 tr=TR_A,
 act=("The telehandler lifts a grey steel beam from the truck and sets it on two slim posts beside the near wing, "
      "riggers bolt it to the posts, and the small piling rig drives post footings into the meadow; the steel on the "
      "truck dwindles. " + CREW),
 tex=T_LIFT,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the frame columns. The new terrace "
       "posts stand on driven footings in the meadow and carry the grey beams, bolted at their heads. The truck stands "
       "on its wheels on the gravel track."),
 mf=("The telehandler carries grey steel beams and slim posts from the truck to the near wing, and the crew bolts them "
     "into a separate terrace frame on its own posts round the wing root, clear of the wing itself."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The piling rig drives four post "
       "footings round the near wing root; the posts are stood on them, and the beams are lifted onto their heads and "
       "bolted, until a flat grey steel frame surrounds the wing root at the height of the top of the wing, with the "
       "wing passing through it unchanged. The airliner does not move. The small white clouds drift slowly from the "
       "left in one smooth flow, and the short shadows fall to the left and away."))

# ---------- S9 ----------
scene(n=9, fiil="DÖŞER", eleman="teras döşemesi %0 → %100 (burundan kuyruğa) · istif → 0", rejim="B", t0="11:00", t1="13:00",
 st="M", g="G9",
 stage=("a grey steel terrace frame now stands round the root of the near wing on four slim posts, its beams level "
        "with the top of the wing and the wing passing through it unchanged. " + RAISED + " The fuselage is clean old "
        "white with clouded windows. A flatbed truck stands at the right loaded with a high stack of pale timber "
        "decking boards; the telehandler waits beside it; two work platforms stand under the frame."),
 moment="Eleven in the morning: the terrace frame is up and the decking boards are stacked on the truck.",
 comp=COMP_POST + " The terrace frame sits at about sixty-three percent of frame height, between about two fifths and a little over half the frame width.",
 light=LIGHT("11:00", "am_high"),
 tr=TR_B,
 act=("The telehandler lifts a pack of decking boards from the truck onto the terrace frame, carpenters lay the boards "
      "across the beams from the cockpit side towards the tail, and a second team screws them down; offcuts drop into "
      "a skip below. " + CREW),
 tex=T_LIFT,
 phys=("The decking boards rest on the grey terrace beams, which bear on four slim posts standing on driven footings. "
       "The airliner rests on its saddle beams pinned to the frame columns. The truck stands on its wheels on the "
       "gravel track."),
 mf=("The telehandler lifts packs of decking boards from the truck onto the terrace frame, and the carpenters lay "
     "them across the beams in one direction, from the cockpit side towards the tail, until the whole terrace floor "
     "is covered."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Pack after pack rises from the truck "
       "on the telehandler forks, and the pale timber floor advances steadily along the frame in one direction, board "
       "by board, while the stack on the truck shrinks pack by pack until the truck bed is bare. The shadows swing "
       "slowly round under the airliner from the left to the right as the sun passes high behind the camera, and the clouds streak slowly across from the left. The oak turns from green to gold."))

# ---------- S10 ----------
scene(n=10, fiil="KURAR", eleman="merdiven 0 → 2 kol + sahanlık (%100)", rejim="A", t0="13:00", t1="13:10",
 st="M", g="G10",
 stage=("a pale timber terrace now surrounds the root of the near wing at the height of the wing top, its decking "
        "complete on the grey steel frame and four slim posts, the wing passing through it unchanged; the over-wing "
        "exit beside it is still shut. " + RAISED + " The cockpit windows and the row of cabin windows are still old "
        "and clouded, some broken. A truck stands on the dry rise under the oak, loaded with two sections of grey steel stair with timber steps and a small half-way platform; offcuts lie in a skip below the terrace."),
 moment="One in the afternoon: the terrace is floored and the stair has arrived under the oak.",
 comp=COMP_POST + " The truck with the stair stands under the oak at about a sixth of the frame width.",
 light=LIGHT("13:00", "noon"),
 tr=TR_A,
 act=("The telehandler lifts the lower stair section from the truck and sets it on a footing on the dry rise, riggers "
      "bolt a small half-way platform onto a slim post, and the telehandler then swings the upper section up to the forward cabin "
      "door; fallen leaves and tyre ruts mark the rise. " + CREW),
 tex=T_FIT,
 phys=("The lower stair section stands on a concrete footing on the dry rise and bears on the half-way platform, which stands on "
       "one slim post. The upper section hangs from the telehandler forks on a short sling until it is bolted at the "
       "door sill. The airliner rests on its saddle beams."),
 mf=("The telehandler lifts two steel stair sections and a half-way platform from the truck under the oak, and the riggers bolt "
     "them into one stair from the dry rise up to the forward cabin door."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The lower section is set on its "
       "footing, the half-way platform is bolted onto its post, and the upper section swings up on the forks and is bolted at the "
       "door sill; then the forward cabin door is swung open from inside. The truck drives off along the gravel track, and two workers roll two scaffold towers in under the cabin windows. The scattered white clouds drift slowly from the left in one smooth flow, and the short shadows fall away from "
       "the camera."))

# ---------- S11 ----------
scene(n=11, fiil="CAMLAR", eleman="cam: bulanık → yeni (%100, burundan kuyruğa) · kanat üstü kapı açılır", rejim="A", t0="13:10", t1="13:20",
 st="M", g="G11",
 stage=("a grey steel stair with timber steps now runs from the dry rise under the oak, by way of a small half-way platform on one slim post, up to the forward cabin door, which stands open. The pale timber terrace surrounds the root of "
        "the near wing. " + RAISED + " The cockpit windows and the row of cabin windows are still old and clouded, some "
        "broken. Two scaffold towers stand on the grass under the cabin windows, and a truck at the right carries "
        "crates of new window panes."),
 moment="Ten past one: the stair reaches the open door and the crates of new panes are waiting.",
 comp=COMP_POST + " The stair runs down from the door at about a third of the frame width to the foot of the oak.",
 light=LIGHT("13:10", "pm_high"),
 tr=TR_A,
 act=("Glaziers on the scaffold towers lift the old clouded panes out of the cabin windows and set new clear panes in, "
      "the telehandler lifts a crate of panes from the truck up to the cockpit, and a worker opens the over-wing exit "
      "onto the terrace; broken glass collects in a skip below. " + CREW),
 tex=T_FIT,
 phys=("The scaffold towers stand on their wheels on the grass beneath the windows. The crate of panes rests on the "
       "telehandler forks. The airliner rests on its saddle beams pinned to the frame columns."),
 mf=("The glaziers lift the old clouded panes out of the cockpit and the cabin windows and set clear new panes from "
     "the crates into the same openings, window by window from the nose towards the tail, and the over-wing exit "
     "opens onto the terrace."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The scaffold towers roll along "
       "under the windows, and the window row turns from milky white to clear dark glass, one window after another, "
       "the nose first; the telehandler lifts the crates from the truck up to the cockpit and lowers the empty ones "
       "back. The window openings keep their positions and their shapes. The high thin cloud drifts slowly from the "
       "left in one smooth flow, and the short shadows fall to the right and away."))

# ---------- S12 ----------
scene(n=12, fiil="YALITIR", eleman="kabin içi: yalıtım + zemin (palet 4 → 0 · vekil: eksilen yük)", rejim="A", t0="13:20", t1="13:30",
 st="M", g="G12", nxt="G14",
 stage=("every window of the airliner has been renewed: the six cockpit panes and the long row of small cabin windows "
        "are clear dark glass, and the over-wing exit stands open onto the pale timber terrace round the near wing "
        "root. The grey steel stair with timber steps runs from the dry rise under the oak to the open forward cabin "
        "door. " + RAISED + " Two scaffold towers stand under the cabin windows; a flatbed truck parked at the foot of "
        "the stair carries four tall pallets of insulation rolls and pale floor panels."),
 moment="Twenty past one: all the windows are new and four pallets for the cabin wait at the foot of the stair.",
 comp=COMP_POST + " The truck with the four pallets stands at the foot of the stair at about a sixth of the frame width.",
 light=LIGHT("13:20", "pm_high"),
 tr=TR_A,
 act=("Workers carry insulation rolls on their shoulders from the truck up the stair and in through the forward door, "
      "and the telehandler lifts a pallet of pale floor panels from the truck onto the terrace, where a second team "
      "carries the panels in through the over-wing exit; packing film and offcuts collect in a skip. " + CREW),
 tex=T_FIT,
 phys=("The truck stands on its wheels at the foot of the stair, and the pallet of floor panels rests on the "
       "telehandler forks. The stair stands on its footing on the dry rise. The airliner rests on its saddle beams "
       "pinned to the frame columns."),
 mf=("Workers carry insulation rolls and floor panels from the pallets on the truck at the foot of the stair up into "
     "the cabin through the forward door and the over-wing exit, until the truck bed is bare."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. A steady line of soft streaks flows "
       "up the stair with rolls on their shoulders and down again empty-handed, while the telehandler lifts pallet "
       "after pallet of panels from the truck onto the terrace; the four pallets on the truck shrink to bare boards and "
       "the empty truck drives off along the gravel track. The high thin cloud drifts slowly from the left in one "
       "smooth flow, and the short shadows fall to the right and away."))

# ---------- S13 (KOKPİT) ----------
scene(n=13, fiil="DONATIR", eleman="kokpit köşesi: boş → iki koltuk · masa · lamba · kilim (%100)", rejim="A", t0="13:20", t1="13:30",
 st="K", g="G13", nxt="G13′",
 stage=("the cockpit has been stripped and lined: the old instrument panel has been taken out and the front is lined "
        "flat with pale birch boards below the windscreen, the walls and the curved ceiling are lined with smooth white "
        "panels, a new floor of pale oak boards runs forward to the base of the windscreen, and the six windscreen panes "
        "are new and clear. The space is empty except for a rolled rug and a roll of insulation membrane left by the "
        "rear wall, and a low step down to the cabin door at the rear. Through the panes: the oak, bronze in late "
        "autumn, on the left; ahead and to the right the meadow below, the lake and the far wooded hills."),
 moment="Twenty past one in the afternoon: the cockpit is bare and lined, waiting for its furniture.",
 light=("LIGHTING: " + sunline("13:20") + ", high on the left, so a bright patch of sunlight falls through the left "
        "panes onto the new floor while the rest of the cockpit is in soft daylight. Late autumn outside: a pale sky "
        "with high thin cloud and the oak bronze. The sun stays outside the frame."),
 tr=TR_A_IN,
 act=("Two workers carry an armchair in from the cabin and set it by the left panes, a third carries a second "
      "armchair and a small round table, a hand cart brings a standing lamp, and a worker unrolls the rug across the "
      "floor; the patch of sunlight creeps across the boards. Crew register only as faint soft motion streaks, never "
      "as sharp figures."),
 tex=("Fresh pale oak floor boards with sawdust in the joints, smooth white wall panels with taped seams and a few "
      "glue stains, a faint film of dust on the new panes, packing film and offcuts by the rear wall, a band of "
      "sunlight on the floor. " + FILMSTOCK_IN),
 phys=("The rolled rug and the membrane roll rest on the new floor boards by the rear wall. The floor rests on the "
       "cockpit floor beams of the airliner. The wall panels are clamped to the curved frames of the fuselage, and the "
       "birch boards are bolted over the old panel frame."),
 mf=("Workers carry two armchairs, a small round table, a standing lamp and a rug from the cabin into the cockpit and "
     "set them in front of the windscreen, turning the bare cockpit into a reading corner that looks out over the lake."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. A hand cart brings the lamp and "
       "the rolled rug from the cabin; the rug is unrolled, the two chairs are set facing the windscreen with the table "
       "between them, and the lamp is stood beside the right chair. At the end the lamp is switched on and glows warm. "
       "Outside, the high thin cloud drifts slowly from the left over the lake and the far hills, and the patch of "
       "sunlight slides slowly across the floor."))

# ---------- S14 ----------
scene(n=14, fiil="YERLEŞTİRİR", eleman="mutfak: tezgâh + dolaplar (sandık 3 → 0 · kanat kapısından)", rejim="A", t0="13:30", t1="13:40",
 st="M", g="G14",
 stage=("the cabin has been lined inside, and the truck at the foot of the stair has gone. The grey steel stair with "
        "timber steps runs from the dry rise under the oak to the open forward cabin door; the pale timber terrace "
        "surrounds the near wing root, the over-wing exit open onto it. " + RAISED + " Two scaffold towers stand under "
        "the cabin windows. A second flatbed truck stands at the right beside the telehandler, loaded with a long wrapped "
        "kitchen counter and three wrapped crates of cabinets."),
 moment="Half past one: the cabin is lined, and the kitchen waits on the truck beside the telehandler.",
 comp=COMP_POST + " The truck with the three crates stands at the right at about four fifths of the frame width.",
 light=LIGHT("13:30", "pm_high"),
 tr=TR_A,
 act=("The telehandler lifts a crate of wrapped cabinets from the truck up onto the terrace, a team slides the cabinets "
      "off the crate and in through the over-wing exit on a low trolley, and the telehandler then lifts the long kitchen "
      "counter up to the terrace in the same way; packing film flaps in the skip. " + CREW),
 tex=T_FIT,
 phys=("The truck stands on its wheels at the right, and each crate rests on the telehandler forks as it rises. The "
       "terrace bears on its four slim posts. The airliner rests on its saddle beams pinned to the frame columns."),
 mf=("The telehandler lifts the three crates of cabinets and the long kitchen counter from the truck onto the terrace, "
     "and the team slides them on a low trolley from the terrace in through the over-wing exit into the middle of the "
     "cabin."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The forks rise from the truck to the "
       "terrace and come down empty again, crate by crate, and each time soft streaks of the team slide the load across "
       "the terrace and in through the over-wing exit; last of all the long counter goes up and in. The three crates on "
       "the truck go down to none. The high thin cloud drifts slowly from the left in one smooth flow, and the short "
       "shadows fall to the right and away."))

# ---------- S15 ----------
scene(n=15, fiil="TAŞIR", eleman="yatak: çerçeve + şilte (yük 2 → 0 · merdivenden) · iç donanım tamam", rejim="A", t0="13:40", t1="13:50",
 st="M", g="G15",
 stage=("the cabin is lined and the kitchen is in, and the truck beside the telehandler stands empty. The grey steel "
        "stair with timber steps runs from the dry rise under the oak to the open forward cabin door; the pale timber "
        "terrace surrounds the near wing root, the over-wing exit open onto it. " + RAISED + " Two scaffold towers stand "
        "under the rear cabin windows; a small truck at the foot of the stair carries a wrapped mattress and a pale "
        "timber bed frame."),
 moment="Twenty to two: the kitchen is in, and the bed waits at the foot of the stair.",
 comp=COMP_POST + " The small truck with the bed stands at the foot of the stair at about a sixth of the frame width.",
 light=LIGHT("13:40", "pm_high"),
 tr=TR_A,
 act=("Two workers carry the long bed frame from the truck up the stair, tilting it through the forward door, two more "
      "carry the wrapped mattress after it, and the telehandler lowers the empty kitchen crates from the terrace onto "
      "the truck at the right; offcuts and straps lie in the skip. " + CREW),
 tex=T_FIT,
 phys=("The small truck stands on its wheels at the foot of the stair. The stair stands on its footing on the dry rise "
       "and bears on its half-way platform. The airliner rests on its saddle beams pinned to the frame columns."),
 mf=("Workers carry a pale timber bed frame and a wrapped mattress from the small truck at the foot of the stair up "
     "the stair and in through the forward door, back along the cabin to the rear."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The bed frame climbs the stair as a "
       "long pale streak and tips in through the door, the mattress follows, and the small truck drives off empty; the "
       "telehandler stacks the empty crates on the truck at the right. The high thin cloud thickens slowly from the "
       "left in one smooth flow, and the short shadows fall to the right and away."))

# ---------- S16 ----------
scene(n=16, fiil="ÇEVİRİR", eleman="teras: korkuluk (+ sönük lamba dizisi) + 2 bank + 4 saksı (%100)", rejim="A", t0="13:50", t1="14:00",
 st="M", g="G16",
 stage=("the house is fitted inside. The grey steel stair with timber steps runs from the dry rise under the oak to "
        "the forward cabin door. " + RAISED + " The terrace round the near wing root is bare decking with open edges. "
        "A truck at the right carries bundles of slim steel railing panels with strings of small unlit lamps coiled on "
        "them, two timber benches and four large planters filled with soil; the telehandler stands beside it; two "
        "scaffold towers stand under the windows."),
 moment="Ten to two: the house is fitted inside, and the terrace edges are still open.",
 comp=COMP_POST + " The open terrace sits at about sixty-three percent of frame height round the wing root.",
 light=LIGHT("13:50", "pm_high"),
 tr=TR_A,
 act=("The telehandler lifts a bundle of railing panels from the truck onto the terrace, fitters bolt the panels along "
      "the open edges of the decking and clip the unlit lamp strings along the top rail and down the stair handrail, "
      "and the telehandler then sets the large planters and two timber benches on the terrace; packing straps and "
      "offcuts fall into the skip. " + CREW),
 tex=T_FIT,
 phys=("The railing panels are bolted to the edge beams of the terrace, and the benches and the planters stand on the "
       "decking. The terrace beams bear on their four slim posts. The airliner rests on its saddle beams pinned to the "
       "frame columns."),
 mf=("The telehandler lifts railing panels, two timber benches and four large planters from the truck onto the "
     "terrace, and the fitters bolt the railings along its edges and set the benches and the planters on the decking."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Slim steel railings run out along "
       "the open edges one panel after another, a thin line of unlit lamps follows along the top rail and down the stair, "
       "and then the benches and the planters are set down on the pale decking while the load on the truck shrinks "
       "bundle by bundle. The high grey cloud thickens slowly from the left in one smooth flow, and the short shadows "
       "soften and fall to the right."))

# ---------- S17 ----------
scene(n=17, fiil="SÖKER ②", eleman="kaldırma donanımı 4 → 0 · iskele 2 → 0 (söküm %100)", rejim="A", t0="14:00", t1="14:10",
 st="M", g="G17",
 stage=("the terrace round the near wing root is finished, with slim steel railings along its edges carrying a string "
        "of small unlit lamps, two timber benches and four large planters with young shrubs. " + RAISED + " The grey "
        "steel stair with timber steps runs from the dry rise under the oak to the forward cabin door, unlit lamps along "
        "its handrail. Two scaffold towers stand under the windows, and the telehandler and an empty flatbed truck wait "
        "at the right."),
 moment="Two in the afternoon: everything is built, and only the lifting gear and the scaffold are left.",
 comp=COMP_POST + " The slack cables hang from the top beams at about seventy percent of frame height.",
 light=LIGHT("14:00", "pm_grey"),
 tr=TR_A,
 act=("The telehandler lifts the jack units off the red top beams one by one and lowers them with their coiled cables "
      "onto the flatbed truck, two riggers on the beam tops unbolt them, and workers take the scaffold towers apart and "
      "carry the frames to the truck; tyre ruts and trampled grass mark the meadow. " + CREW),
 tex=T_FIT,
 phys=("The jack units sit bolted on the top beams until the riggers free them, and then rest on the telehandler "
       "forks. The scaffold towers stand on their wheels on the grass. The airliner rests on its saddle beams pinned "
       "to the frame columns."),
 mf=("The telehandler lifts the four jack units and their slack cables off the red top beams and lowers them onto the "
     "flatbed truck, and the workers carry the scaffold frames from under the windows to the truck, which then drives "
     "off along the gravel track."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. One by one the jack units leave the "
       "beam tops on the forks and are lowered onto the truck, and the slack cables are coiled down after them; the "
       "scaffold towers come apart into frames that are carried to the truck and stacked. The truck and the "
       "telehandler drive off along the gravel track to the right and out of the frame, and the finished lake house "
       "stands clear and empty for the first time. The grey cloud deck rolls slowly over from the left, and the faint "
       "shadows fall to the right."))

# ---------- S18 ----------
scene(n=18, fiil="KARLANIR", eleman="kış ①: yaprak → 0 · kar 0 → ince örtü", rejim="B", t0="14:10", t1="16:10",
 st="M", g="G18",
 stage=("the lake house stands complete and clear for the first time. " + HOUSE + " The windows are dark. Below the house the empty trough lies in the grass, drying pale, the "
        "raw scar of the old bed. The meadow is cut short, crossed by tyre ruts and the gravel track, and the oak is "
        "brown and almost bare."),
 moment="Ten past two on a grey late-autumn afternoon: the house is finished and the site is empty; winter is coming.",
 comp=COMP_POST + " The empty trough lies beneath the house at about forty-three percent of frame height.",
 light=LIGHT("14:10", "pm_grey"),
 tr=TR_B_GREY,
 act=("Snow begins to fall: a small delivery vehicle drives along the gravel track to the foot of the stair, two workers carry crates of supplies from it up the stair and stack the crates by the forward door, and a small loader pushes the first snow off the gravel track; fresh tyre tracks print the thin snow. " + CREW),
 tex=T_WINTER,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns. The stair stands "
       "on its footing on the dry rise, and the terrace bears on its four slim posts. The delivery vehicle stands on "
       "its wheels at the foot of the stair."),
 mf=("Winter arrives: the wind strips the last brown leaves from the oak onto the meadow, and then snow falls from the "
     "grey sky onto the meadow, the terrace, the wings and the top of the fuselage until a thin white cover lies over "
     "everything."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The last leaves whirl off the oak, "
       "the grey cloud deck rolls slowly over from the left, and the snow comes down in soft streaks; the meadow, the "
       "dry rise and the terrace decking turn white, the trough becomes a shallow white hollow, and the oak stands bare "
       "and black. The delivery vehicle brings crates of supplies along the gravel track to the foot of the stair, two "
       "workers carry them up, and the vehicle drives away. Behind the cockpit panes one warm light stays on; the rest "
       "of the windows stay dark. The lake beyond turns grey and still."))

# ---------- S19 ----------
scene(n=19, fiil="YÜKSELİR", eleman="kış ②: kar erir · göl çayıra girer (%0 → %40)", rejim="B", t0="16:10", t1="18:10",
 st="M", g="G19",
 stage=("a thin even cover of snow lies over the meadow, the dry rise, the terrace decking, the wings and the top of "
        "the fuselage, and the bare black oak stands leafless; the empty trough below the house is a shallow white "
        "hollow. " + HOUSE + " One warm light glows behind the cockpit panes; the other windows are dark. The lake "
        "beyond is grey and still."),
 moment="Ten past four on a winter afternoon: snow lies on everything and the lake beyond is grey and still.",
 comp=COMP_POST + " The white hollow of the trough lies beneath the house at about forty-three percent of frame height.",
 light=LIGHT("16:10", "snow"),
 tr=TR_B_GREY,
 act=("Rain sets in and the snow melts; a small loader brings a pallet of sandbags along the gravel track, two workers "
      "stack the sandbags in a short row round the stair footing, and a pump on the dry rise starts to draw water off "
      "the track; slush and mud spread in the tyre ruts. " + CREW),
 tex=T_WINTER,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns. The stair stands "
       "on its footing on the dry rise, and the terrace bears on its four slim posts. The loader stands on its wheels "
       "on the gravel track."),
 mf=("The thaw and the spring rain raise the lake: its water spreads from the lake shore at the right, round the "
     "boathouse piles, onto the low meadow and across it towards the house."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The rain clouds roll over from the left; the snow melts off the roof of the fuselage and the terrace and shrinks back across the meadow until wet "
       "grass shows everywhere. Then the edge of the lake creeps in from the right in a slow dark line across the low "
       "meadow, darkening the grass ahead of it, while the dry rise under the oak and the stair foot stay above it. The "
       "loader brings a pallet of sandbags from the gravel track, and the workers stack them round the stair footing. "
       "Rain streaks down the fuselage. A first green haze comes over the oak."))

# ---------- S20 ----------
scene(n=20, fiil="KAPLAR", eleman="su: eski yatak + ayaklar (%100) · ev kuru", rejim="A", t0="18:10", t1="18:20",
 st="M", g="G20", nxt="G22",
 stage=("the snow has gone and the meadow is flooding: a sheet of brown-grey lake water has spread in from the right "
        "across the low meadow and reaches the far edge of the empty trough beneath the house, while the near part of "
        "the meadow and the dry rise under the oak are still wet grass, and a short row of sandbags rings the stair "
        "footing. The bare oak shows a first green haze. " + HOUSE + " One warm light glows behind the cockpit panes."),
 moment="Ten past six on a wet spring evening: the water has crossed the meadow and is reaching the old bed of the airliner.",
 comp=COMP_POST + " The edge of the water runs across the meadow at about forty-three percent of frame height.",
 light=LIGHT("18:10", "flood"),
 tr=TR_A,
 act=("Two workers in waders check the sandbags at the stair foot, a small loader backs off the gravel track onto the "
      "dry rise, and the pump on the rise lifts the water off the track through a long hose; foam lines and drifting "
      "twigs mark the spreading water. " + CREW),
 tex=T_FLOOD,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns, standing in the "
       "water on their footings. The stair stands on its footing on the dry rise inside its ring of sandbags. The pump "
       "sits on the dry rise with its hose lying across the grass."),
 mf=("The lake water spreads from the far edge of the old bed into the empty trough beneath the house and on round "
     "the frame columns and the terrace posts, until it covers the whole low meadow under the house while the house "
     "stays dry above."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The water level rises evenly; the "
       "old muddy trough fills and its outline sinks under the surface, the water reaches round the near columns and "
       "the terrace posts and on to the foot of the camera bank, and then lies calm, mirroring the underside of the "
       "fuselage. The loader brings a pallet of sandbags along the dry rise to the stair foot. The rain thins to a "
       "drizzle; the clouds drift slowly from the left and a band of low warm light opens beneath them. The house above "
       "does not change."))

# ---------- S21 (KOKPİT) ----------
scene(n=21, fiil="SIĞINIR", eleman="kokpit: yağmur · su aşağıda (iç mekân değişmez)", rejim="A", t0="18:10", t1="18:20",
 st="K", g="G21", nxt="G21′",
 stage=("the cockpit reading corner is in use: the two soft grey armchairs face the windscreen with the small round "
        "oak table between them on the woven rug, and on the table stand a white cup and an open book; the standing lamp "
        "beside the right chair glows warm, and a low step leads down to the cabin door at the rear. Rain runs down the "
        "six windscreen panes. Through the panes, below the nose, brown-grey water lies across the meadow round the foot "
        "of the dry rise; beyond it the lake and the far wooded hills lie grey under low cloud, and the oak on the left "
        "shows a first green haze."),
 moment="Ten past six on a rainy spring evening: the meadow below is under water and the cockpit is dry and warm.",
 light=("LIGHTING: " + sunline("18:10") + ", low ahead and hidden behind the dark rain clouds, so only a thin brighter "
        "band glows low along the far hills; inside, the warm lamp lights the chairs, the table and the rug. Spring "
        "outside: a heavy grey sky, the oak with a first green haze. The sun stays hidden behind the clouds."),
 tr=TR_A_IN,
 act=("Rain streams down the windscreen panes in running trickles, wind ruffles the water below the nose, and a thin "
      "thread of steam rises from the cup on the table; out on the water a line of drifting twigs moves past the foot "
      "of the dry rise. No people are present."),
 tex=("Rain streaks and droplets on the panes, a film of condensation along their lower edges, the soft pile of the "
      "woven rug, a ring stain from the cup on the oak table, and below the nose brown-grey water with drifting debris "
      "and a band of silt along the dry rise. " + FILMSTOCK_IN),
 phys=("The cup and the open book rest on the oak table, which stands on the woven rug. The armchairs stand on the "
       "pale oak floor. The lamp stands on its heavy round foot beside the right chair."),
 mf=("Rain runs from the top of the windscreen panes down to their lower edges in trickles, and below the nose the "
     "water spreads on from the meadow to the foot of the dry rise."),
 body=("Ten minutes pass in the rainy dusk. Everything in this shot is time-lapsed at the same rate. Inside nothing "
       "moves except a thin thread of steam rising from the cup and the warm lamplight on the table; outside, the rain "
       "clouds drift slowly from the left over the far hills, the drizzle comes and goes in grey veils, and the water "
       "below ripples and creeps a little further up the dry rise. The water stays outside; the cockpit stays dry and "
       "still."))

# ---------- S22 ----------
scene(n=22, fiil="ÇEKİLİR", eleman="su %100 → çukurda kalan (gölet ön hâli)", rejim="A", t0="18:20", t1="18:30",
 st="M", g="G22",
 stage=("the flood is at its height: calm brown-grey lake water covers the whole low meadow from the lake shore at "
        "the right to the foot of the camera bank, lies round the frame columns and the terrace posts, and covers the "
        "old muddy trough beneath the house completely; the dry rise under the oak and the stair foot, ringed with "
        "sandbags, stand just above it. " + HOUSE + " One warm light glows behind the cockpit panes. The water mirrors "
        "the underside of the fuselage."),
 moment="Twenty past six on a spring evening: the flood is at its height and the house stands dry above it.",
 comp=COMP_POST + " The flood water fills the lower part of the frame below about forty-three percent of frame height.",
 light=LIGHT("18:20", "flood"),
 tr=TR_A,
 act=("The pump on the dry rise pulls water through a long hose back towards the lake shore, two workers in waders "
      "pull the sandbags off the stair foot and stack them on a pallet, and a small loader waits on the gravel track; "
      "lines of silt and debris appear on the grass as the water drops. " + CREW),
 tex=T_FLOOD,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns standing in the "
       "water on their footings. The stair stands on its footing on the dry rise. The pump sits on the dry rise with "
       "its hose lying across the grass."),
 mf=("The water drains from the low meadow back to the lake at the right, leaving a broad wet hollow beneath and in "
     "front of the house that stays partly filled with water."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The water line slides back towards "
       "the right, uncovering wet flattened grass marked with lines of silt and debris; beneath the house the old "
       "trough and the low ground in front of it stay filled with a broad shallow pool with ragged muddy edges. The "
       "workers carry the sandbags from the stair foot and stack them on a pallet, and the loader lifts the pallet onto "
       "its forks and drives it away. The clouds thin and drift slowly from the left, and the low warm light spreads "
       "across the wet meadow."))

# ---------- S23 ----------
scene(n=23, fiil="KAZAR", eleman="gölet kıyısı + su yolu 0 → %100 (göle bağlanır)", rejim="A", t0="18:30", t1="18:40",
 st="M", g="G23",
 stage=("the flood has gone back to the lake: the low meadow is wet, flattened grass streaked with silt and debris "
        "lines, and beneath and in front of the house a broad shallow pool fills the old trough and the low ground "
        "towards the camera bank, with ragged muddy edges. "
        + HOUSE + " A small excavator and a dump truck stand on the gravel track at the right, a pallet of grey stones "
        "beside them, and stakes with orange tape mark a curving line for a raw cut from the right end of the pool back "
        "to the lake shore beside the boathouse."),
 moment="Half past six on a late-spring evening: the water has gone back, the hollow under the house stays wet, and the line of a channel is staked out.",
 comp=COMP_POST + " The pool fills the lower part of the frame below about forty-three percent of frame height.",
 light=LIGHT("18:30", "spring"),
 tr=TR_A,
 act=("The excavator trims the ragged edges of the pool into a smooth curving shore and digs the narrow channel along "
      "the staked line, swinging the spoil into the dump truck, and the crew packs the new banks with stones from the "
      "pallet; fresh spoil heaps and bucket marks line the channel. " + CREW),
 tex=T_SPRING,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns standing in the "
       "pool on their footings. The excavator stands on its tracks on the bank, its bucket bearing on the wet ground. "
       "The dump truck stands on its wheels on the gravel track."),
 mf=("The excavator shapes the ragged pool into a smooth curving pond and digs a narrow channel from its right end "
     "back to the lake shore beside the boathouse, tipping the spoil into the dump truck."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Bucket by bucket the pool edge is "
       "cut into a smooth curve and the channel advances along the staked line; as the last bucket breaks through, "
       "lake water runs into the channel and joins it to the pond. The crew carries stones from the pallet and packs "
       "them along the new banks, and the dump truck leaves loaded. The clouds drift slowly from the left and turn "
       "gold, and the long shadows reach to the right."))

# ---------- S24 ----------
scene(n=24, fiil="YEŞERTİR", eleman="kıyı bitkileri %0 → %100 · basamak taşları", rejim="A", t0="18:40", t1="18:50",
 st="M", g="G24",
 stage=("a smooth curving pond now fills the low ground beneath and in front of the house, from the foot of the camera "
        "bank to beyond the far frame columns, its banks edged with packed stones, and a narrow channel runs from its "
        "right end back to the lake shore beside the boathouse, open water from end to end. The banks are raw brown "
        "soil, and spoil heaps lie by the channel. " + HOUSE + " A small loader and a trailer loaded with young reeds "
        "and shrubs in pots stand on the gravel track, with a pile of topsoil and a pallet of flat stepping stones "
        "beside them."),
 moment="Twenty to seven: the pond and its channel are dug and joined to the lake; the banks are still bare.",
 comp=COMP_POST + " The pond fills the lower part of the frame below about forty-three percent of frame height, and the channel leaves it at about two thirds of the frame width.",
 light=LIGHT("18:40", "spring"),
 tr=TR_A,
 act=("Gardeners set reeds and shrubs from the trailer along the bare banks, the loader spreads the topsoil from the "
      "pile, and the crew beds a line of flat stepping stones across the dry ground from the stair foot to the pond; "
      "soil and mud stain the stones. " + CREW),
 tex=T_SPRING,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns standing in the "
       "pond on their footings. The stepping stones are bedded into the soil of the dry ground. The loader stands on "
       "its wheels on the gravel track."),
 mf=("The gardeners carry reeds and shrubs from the trailer and plant them along the bare banks of the pond, and the "
     "crew beds flat stepping stones from the pallet across the dry ground from the stair foot to the water's edge."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The raw banks turn green, plant by "
       "plant, round the curve of the pond and along the channel, while the loader spreads dark topsoil between them "
       "and the trailer empties; the stepping stones are laid one after another from the stair foot to the water. The "
       "clouds drift slowly from the left and turn gold, the low light warms the side of the house, and the long "
       "shadows reach to the right."))

# ---------- S25 ----------
scene(n=25, fiil="İNDİRİR", eleman="iskele 0 → %100 · kano suya", rejim="A", t0="18:50", t1="19:00",
 st="M", g="G25",
 stage=("the pond banks are planted with young reeds and low shrubs, a line of flat stepping stones runs from the "
        "stair foot across the dry ground to the water's edge, and fresh topsoil lies dark between the plants. The "
        "smooth pond fills the low ground beneath and in front of the house and joins the lake by its narrow channel at "
        "the right. " + HOUSE + " A small truck at the foot of the stair carries timber posts, a stack of decking "
        "boards and a dark green wooden canoe; the telehandler stands beside it."),
 moment="Ten to seven, just before sunset: the banks are planted, and the walkway and the canoe wait at the foot of the stair.",
 comp=COMP_POST + " The truck with the canoe stands at the foot of the stair at about a sixth of the frame width.",
 light=LIGHT("18:50", "sunset"),
 tr=TR_A,
 act=("The crew drives timber posts into the pond edge below the stair and lays decking boards from the stack across "
      "them, the telehandler lifts the canoe from the truck and lowers it onto the water beside the new walkway, and a "
      "worker ties it to a post; wet mud and offcuts lie on the bank. " + CREW),
 tex=T_SPRING,
 phys=("The walkway posts stand driven into the pond bed, and the decking boards rest on their head beams. The canoe hangs on one sling under each end from the telehandler forks until it rests on the water. The truck stands on its wheels at "
       "the foot of the stair."),
 mf=("The crew builds a short timber walkway from the posts and the stack of decking boards on the truck out into the "
     "pond below the stair, and the telehandler lifts the canoe from the truck onto the water beside it."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The posts go in, the boards go "
       "across, and a short pale walkway reaches out over the water; the canoe swings down on its slings, settles on the "
       "pond and is tied to a post. Then the truck and the telehandler drive off along the gravel track to the right "
       "and out of the frame. The last warm light slides up the tail fin and the crown of the oak and leaves them, and "
       "the clear sky deepens towards blue while the few clouds drift slowly from the left."))

# ---------- S26 ----------
scene(n=26, fiil="YANAR", eleman="ışık: 0 → kabin + teras + merdiven (%100, gruplar)", rejim="A", t0="19:00", t1="19:10",
 st="M", g="G26", iso=400,
 stage=("the lake house is complete with its garden: a short timber walkway with pale decking runs out into the pond below "
        "the stair, a dark green canoe lies on the water tied to it, a line of flat stepping stones leads from the stair foot to the walkway, and reeds and low shrubs line the pond banks. The smooth pond fills the low ground beneath and in "
        "front of the house and joins the lake by its narrow channel at the right. " + HOUSE + " Only the cockpit "
        "glows softly; the cabin windows are dark and the site is empty and calm."),
 moment="Seven in the evening, just after sunset: the house and its garden are finished and the lights are still off.",
 comp=COMP_POST + " The canoe at the walkway sits at about a third of the frame width, and the pond mirrors the underside of the house.",
 light=LIGHT("19:00", "dusk"),
 tr=TR_A,
 act=("The lights of the house come on in groups — first the front of the cabin beside the softly lit cockpit, then "
      "the middle windows, then the rear windows, and last the string of small warm lamps along the terrace railings "
      "and down the stair — and the pond doubles them; the canoe rocks gently at the walkway. No people are present."),
 tex=T_DUSK,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns standing in the "
       "pond on their footings. The walkway decking rests on posts driven into the pond bed. The canoe lies on the water, tied to a walkway post by a short line."),
 mf=("The lights of the house come on in groups, from the front of the cabin at the left to the rear windows by "
     "the tail at the right, and then along the terrace railings and down the stair to the walkway."),
 body=("Ten minutes pass in the dusk. Everything in this shot is time-lapsed at the same rate. Beside the softly lit "
       "cockpit the front of the cabin glows warm first, then the middle windows and the rear windows one group after "
       "another, and last the small lamps light up along the terrace railings and down the stair; their reflections appear in the "
       "pond and tremble. The afterglow on the left fades and the sky deepens to blue, and the few high clouds drift "
       "slowly from the left."))

# ---------- S27 ----------
scene(n=27, fiil="İNER", eleman="bir kişi: kapı → merdiven → iskele → kano", rejim="A", t0="19:10", t1="19:20",
 st="M", g="G27", iso=400,
 stage=("the lake house is lit: warm light in the cockpit and along the whole row of cabin windows, and a string of "
        "small warm lamps along the terrace railings and down the stair to the walkway, all doubled in the calm pond "
        "beneath and in front of the house. The forward cabin door is shut. The dark green canoe lies tied at the "
        "short timber walkway with pale decking below the stair, a line of flat stepping stones leads from the stair foot "
        "to the walkway, and reeds and low shrubs line the pond banks. " + HOUSE),
 moment="Ten past seven, blue hour: every light of the house is on and the garden lies calm.",
 comp=COMP_POST + " The lit window row runs along the fuselage at about sixty-three percent of frame height, and its reflection lies in the pond in the lower quarter of the frame.",
 light=LIGHT("19:10", "blue"),
 tr=TR_A,
 act=("The forward cabin door opens and spills warm light onto the stair, one person comes out, walks down the stair "
      "and along the stepping stones to the walkway and sits in the canoe and lowers the paddle into the water, and the canoe line is untied; the "
      "canoe dips and ripples spread across the pond. The person registers only as faint soft motion streaks along the "
      "stair, never as a sharp figure."),
 tex=T_DUSK,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns standing in the "
       "pond on their footings. The stair stands on its footing on the dry rise. The canoe lies on the water, tied to a walkway post by a short line."),
 mf=("One person walks from the open forward cabin door down the stair and along the stepping stones onto the walkway "
     "and sits down in the canoe."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The forward door swings open and "
       "warm light spills onto the stair; a soft streak comes down the stair and along the stepping stones, the door "
       "swings shut behind it, the canoe dips as the person sits, and the line is untied and dropped on the walkway. The "
       "lights of the house stay on, and their reflections tremble in the ripples. The sky deepens to a darker blue and "
       "the few high clouds drift slowly from the left."))

# ---------- S28 ----------
LIT = ("the lake house is lit: warm light in the cockpit and along the whole row of cabin windows, and small warm "
       "lamps along the terrace railings and down the stair to the walkway, all doubled in the calm pond that fills "
       "the low ground beneath and in front of the house. ")
GARDEN = ("A line of flat stepping stones leads from the stair foot to the short timber walkway with pale decking, "
          "reeds and low shrubs line the pond banks, and a narrow channel leaves the right end of the pond and curves "
          "back to the lake shore beside the boathouse. ")
scene(n=28, fiil="SÜZÜLÜR", eleman="kano: iskele ucu → gövdenin altı, orta (gerçek hız · ~13 m)", rejim="G", t0="19:20", t1="19:20",
 st="M", g="G28", iso=400,
 stage=(LIT + "One person sits in the dark green canoe at the end of the walkway below the nose, a paddle in hand, the "
        "canoe just pushing off; the person is seen small and from the side, no readable face. " + GARDEN + HOUSE),
 moment="Twenty past seven, deep blue hour: the canoe is just leaving the walkway.",
 comp=COMP_POST + " The canoe at the end of the walkway spans about 160 pixels of frame width at about a third of the frame width.",
 light=LIGHT("19:20", "blue"),
 tr=TR_G,
 act=("The canoe glides from the walkway across the pond to the right and in beneath the belly of the raised airliner, "
      "between the two steel frames, the person pulls the paddle back on alternate sides in slow even strokes; its wake spreads in two "
      "thin lines through the reflected lights. The person in the canoe stays small, seen only as a dark silhouette from "
      "the side, no readable face."),
 tex=T_DUSK,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns standing in the "
       "pond on their footings. The canoe sits on the pond, pressed into the water by the weight of one person. The "
       "walkway decking rests on posts driven into the pond bed."),
 mf=("The canoe glides from the end of the walkway below the nose across the pond and in beneath the belly of the "
     "raised airliner, between the two steel frames, to the middle of the fuselage."),
 body=("Eight seconds pass in real time. Everything in this shot moves at natural speed: the paddle dips in slow even "
       "strokes, the canoe slides steadily to the right without turning and passes into the dark band of water beneath "
       "the belly, and its wake spreads in two thin lines that break the reflections of the lit windows into trembling "
       "gold. The person stays a small dark silhouette, no readable face. The house, its lights and the garden do not "
       "change. The few high thin clouds stay still in the deep blue sky."))

# ---------- S29 ----------
scene(n=29, fiil="DURULUR", eleman="kano: gövdenin altı → su yolu ağzı, durulur (final tutuş)", rejim="G", t0="19:20", t1="19:20",
 st="M", g="G29", iso=400,
 stage=(LIT + "The dark green canoe glides beneath the middle of the fuselage, between the two steel frames, with one "
        "person paddling, seen small from the side, no readable face; its wake trails back towards the empty walkway "
        "through the reflected lights. " + GARDEN + HOUSE),
 moment="Twenty past seven, deep blue hour: the canoe is passing beneath the house.",
 comp=COMP_POST + " The canoe beneath the middle of the fuselage spans about 130 pixels of frame width at about half the frame width.",
 light=LIGHT("19:20", "blue"),
 tr=TR_G,
 act=("The canoe glides on beneath the tail half of the house, out past the second steel frame to the mouth of the "
      "channel at the right as the person lifts the paddle out of the water, and slows; its ripples spread and fade, and the reflections of the lights settle. The person "
      "stays small, seen only as a dark silhouette from the side, no readable face."),
 tex=T_DUSK,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns standing in the "
       "pond on their footings. The canoe sits on the pond, pressed into the water by the weight of one person. The "
       "walkway decking rests on posts driven into the pond bed."),
 mf=("The canoe glides from beneath the middle of the fuselage out past the second steel frame to the mouth of the "
     "narrow channel at the right, and drifts slowly into it towards the open lake."),
 body=("Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame to about "
       "four seconds the canoe glides out from beneath the tail half of the house and past the second steel frame to "
       "the mouth of the channel, the paddle lifting out of the water; from about four to eight seconds it drifts slowly "
       "into the channel towards the open lake, its ripples spreading and fading, the lights of the house stay on and "
       "nothing else changes. The person stays a small dark silhouette, no readable face. The few high thin clouds stay "
       "still in the deep blue sky."))

USTA = dict(g="G30", t="19:20",
 stage=("everything is finished. " + HOUSE + " All its lights are on — warm light in "
        "the cockpit and along the whole row of cabin windows, small warm lamps along the terrace railings and down the "
        "stair — and they are doubled in the calm pond that fills the low ground beneath and in front of the house. "
        + GARDEN + "In the mouth of the channel, just past the tail, the dark green canoe rests on the calm water, its "
        "bow towards the open lake, with one person in it, seen small from the side, no readable face. Below the house, "
        "where the airliner once lay in its muddy bed, there is only water and reflected light."),
 moment="Twenty past seven, deep blue hour, early summer: the house is lived in.",
 comp=COMP_POST + " The canoe spans about 130 pixels of frame width at about two thirds of the frame width.",
 light=LIGHT("19:20", "blue"),
 tr=TR_G,
 act=("The canoe rests at the mouth of the channel, its last ripples spreading and fading; the reflections of the lit "
      "windows tremble in the pond and settle. The person in the canoe stays a small dark silhouette, no readable face."),
 tex=T_DUSK,
 phys=("The airliner rests on its saddle beams, which rest on the brackets of the red frame columns standing in the "
       "pond on their footings. The stair stands on its footing on the dry rise, and the terrace bears on its four slim "
       "posts. The canoe sits on the channel, pressed into the water by the weight of one person."))

COCK_SON = {
 13: dict(g="G13′", t="13:30",
   stage=("the cockpit is now a small reading corner: two soft grey armchairs face the windscreen with a small round "
          "oak table between them on a woven rug, and a standing lamp beside the right chair glows warm; the white "
          "lined walls, the curved ceiling, the pale oak floor, the pale birch boards below the windscreen, the low step "
          "down to the cabin door and the six clear windscreen panes are as before. Folded packing film lies by the rear "
          "wall. Through the panes: the bronze oak on the left; ahead and to the right the meadow below, the lake and "
          "the far wooded hills."),
   moment="Half past one in the afternoon: the reading corner is furnished and its lamp is on.",
   light=("LIGHTING: " + sunline("13:30") + ", high on the left, so a bright patch of sunlight lies across the rug "
          "from the left panes; the lamp adds a small warm glow by the right chair. Late autumn outside: a pale sky with "
          "high thin cloud and the oak bronze. The sun stays outside the frame."),
   act=("The work is finished: the last worker leaves down the low step towards the cabin as faint soft motion "
        "streaks, and the patch of sunlight lies still on the rug."),
   tex=("Fresh pale oak floor boards with sawdust in the joints, smooth white wall panels with taped seams and a few "
        "glue stains, a faint film of dust on the new panes, folded packing film by the rear wall, a band of sunlight "
        "across the rug. " + FILMSTOCK_IN),
   phys=("The two armchairs and the table stand on the rug, which lies on the new floor boards. The lamp stands on its "
         "heavy round foot beside the right chair. The wall panels are clamped to the curved frames of the fuselage.")),
 21: dict(g="G21′", t="18:20",
   stage=("the cockpit reading corner is unchanged and in use: the two soft grey armchairs face the windscreen with the "
          "small round oak table between them on the woven rug, a white cup and an open book on the table, the standing "
          "lamp glowing warm beside the right chair, and a low step down to the cabin door at the rear. Rain still runs "
          "down the six windscreen panes. Through the panes, below the nose, the brown-grey water has crept a little "
          "further up the dry rise; beyond it the lake and the far wooded hills lie grey under low cloud, darker now."),
   moment="Twenty past six on a rainy spring evening: the water below is at its height and the cockpit stays dry and warm.",
   light=("LIGHTING: " + sunline("18:20") + ", low ahead and hidden behind the dark rain clouds, so only a thin "
          "brighter band glows low along the far hills, a little dimmer than before; inside, the warm lamp lights the "
          "chairs, the table and the rug. Spring outside. The sun stays hidden behind the clouds."),
   act=("Rain streams down the panes in running trickles and a thin thread of steam rises from the cup. No people are "
        "present."),
   tex=("Rain streaks and droplets on the panes, a film of condensation along their lower edges, the soft pile of the "
        "woven rug, a ring stain from the cup on the oak table, and below the nose brown-grey water with drifting debris "
        "and a band of silt along the dry rise. " + FILMSTOCK_IN),
   phys=("The cup and the open book rest on the oak table, which stands on the woven rug. The armchairs stand on the "
         "pale oak floor. The lamp stands on its heavy round foot beside the right chair.")),
}

# ── yazıcılar ───────────────────────────────────────────────────────────────
def lens(iso):
    return f"Lens: 24 mm spherical, f/8, ISO {iso}."

def gorsel_main(d, head):
    comp = COMP_HEAD + d["comp"] + " " + COMP_TAIL
    return "\n".join([
        head, lens(d.get("iso", 100)), CAM_MAIN, "",
        STRUCT + " AT THIS STAGE: " + d["stage"], "",
        SITE_MAIN, "",
        "THE TIME MOMENT: " + d["moment"], "",
        comp, "",
        d["light"], "",
        d["tr"], "",
        "ACTIVITY: " + d["act"], "",
        "SITE TEXTURE: " + d["tex"], "",
        "PHYSICS: " + d["phys"], "",
        NEG_MAIN, OUTPUT])

def gorsel_cock(d, head, iso=100):
    return "\n".join([
        head, lens(iso), CAM_COCK, "",
        STRUCT + " AT THIS STAGE: " + d["stage"], "",
        SITE_COCK, "",
        "THE TIME MOMENT: " + d["moment"], "",
        COMP_COCK, "",
        d["light"], "",
        d.get("tr", TR_A_IN), "",
        "ACTIVITY: " + d["act"], "",
        "SITE TEXTURE: " + d["tex"], "",
        "PHYSICS: " + d["phys"], "",
        NEG_COCK, OUTPUT])

STAGE_COCK = ("This shot shows the same stage as the previous shot from the main station: the house stands at the "
              "same height, its belly about fifty-seven percent of frame height in that view, and nothing outside the "
              "cockpit is built during this shot.")
def i2v(d):
    lock = (STAGE_COCK + " " + LOCK_COCK) if d["st"] == "K" else LOCK_MAIN
    tail = I2V_TAIL_COCK if d["st"] == "K" else I2V_TAIL
    return "\n\n".join([I2V_HEAD, "MOTION FOCUS: " + d["mf"], d["body"], lock, tail])

RJ = {"A": "A (10 dk)", "B": "B (2 sa)", "G": "G (gerçek zaman · 8 sn)"}
def blok(d):
    n = d["n"]; bas, son = n * 8, (n + 1) * 8
    ist = "KOKPİT (detay · 2/2 kuralı)" if d["st"] == "K" else "MAIN"
    saat = f"{d['t0']}→{d['t1']}" if d["rejim"] != "G" else f"{d['t0']} (+8 sn)"
    hedef = d.get("nxt", f"G{n+1}")
    out = [f"## 🎬 SAHNE {n} — {d['fiil']}", "",
           "```",
           f"SÜRE: 8,0 s ({bas},0–{son},0)  ·  ELEMAN + ARA HÂL: {d['eleman']}  ·  REJİM: {RJ[d['rejim']]}  ·  SAAT: {saat}  ·  İSTASYON: {ist}",
           "```", ""]
    if d["st"] == "K":
        dis = "G14" if n == 13 else "G22"
        ek = "'ten" if n == 13 else "'den"
        out += [f"> 🪟 **KOKPİT EKİ** — ana zincirin DIŞINDA: S{n-1} ile AYNI on dakikanın içeriden görüntüsü. "
                f"S{n-1}'nin I2V'si ana kare {dis}'{'e' if n == 13 else 'ye'} biter · bu klip {d['g']} → {d['nxt']} (kokpit) · S{n+1} yine "
                f"{dis}{ek} başlar. Dış kare iki yakada AYNIDIR (detay klibi dış büyüme taşımaz — KAMERA_ISTASYONU §1 ④).", ""]
    if d["st"] == "K":
        out += [f"### 📸 GÖRSEL PROMPT ({d['g']} · KOKPİT İLK KARE)", "", "```",
                gorsel_cock(d, HEAD_COCK.format(n=n), 400 if n == 21 else 100), "```", ""]
    else:
        out += [f"### 📸 GÖRSEL PROMPT ({d['g']})", "", "```", gorsel_main(d, HEAD_MAIN.format(n=n)), "```", ""]
    out += [f"### 🎥 I2V PROMPT ({d['g']} → {hedef})", "", "```", i2v(d), "```", ""]
    if d["st"] == "K":
        c = COCK_SON[n]
        out += [f"### 🪟 KOKPİT SON KARESİ ({c['g']} · bu klibin hedefi — sahne görseli DEĞİL, kapı saymaz)", "",
                "> Kapı bu bloğu saymaz (başlıkta GÖRSEL PROMPT yok) — ama aynı disiplinle yazıldı: STRUCTURE,",
                "> SITE / BACKGROUND, NEGATIVE kokpit karelerinde birebir. Üretimde G13′ ÖNCE üretilir (ana",
                "> G14'ün mevsimi ve ışığıyla), G13 ondan geriye; G21 G13′'den türetilir, G21′ G21'den.", "",
                "```", gorsel_cock(dict(c, tr=TR_A_IN), HEAD_COCK_SON.format(n=n), 400 if n == 21 else 100), "```", ""]
    out += ["---", ""]
    return "\n".join(out)

def usta_blok():
    d = USTA
    return "\n".join([
        "## 🌟 USTA KARE — G30 (SAHNE DEĞİLDİR · son klibin hedefi · kapak kaynağı)", "",
        "> Üretim sırasının İLK karesi [§8]: G30 önce üretilir ve ikna edici değilse DURULUR; sonra",
        "> image-to-image geriye G29 → … → G0. Kapı: final hiyerarşisi (PLAN) bu sırayla okunuyor mu ·",
        "> kuyruk tepesi %82 · gövde altı %53 · kanıt nesnesi kayıkhane x 1560–1730 / 94 px · geçici ekipman YOK",
        "> (SÖKÜM satırı) · mavi saat, güneş −4° · üst sekiz boş. Kapak (`THE_SLOW_TAKEOFF_KAPAK.md`) bu promptun",
        "> kopyası + başlık bandı satırıdır [MUZIK_VE_KAPAK §2.2].", "",
        "### 📸 USTA KARE PROMPT (G30)", "", "```",
        gorsel_main(dict(d, iso=400), HEAD_USTA), "```", ""])

H1 = f"""# 🎬 {FILM} — BÖLÜM 1  (S0 – S14 · G0 … G14 + 15 I2V · 0,0–120,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `{FILM}_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır. STRUCTURE bloğu 33 promptta, SITE / BACKGROUND ve NEGATIVE blokları kendi
> istasyonlarının bütün karelerinde BİREBİR aynı kelimelerle tekrarlanır; değişen AT THIS STAGE,
> THE TIME MOMENT, COMPOSITION'ın son cümlesi, LIGHTING, TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.
>
> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py`)
> ki ortak bloklar harfi harfine aynı kalsın [DERS 20].
>
> ⭐ Bu bölümün SON I2V'si (S14: G14 → G15) **G15 karesinde biter** ve G15 `BOLUM_2`'nin ilk
> görselidir: bölüm sınırı bir KAREDİR, kesme değil [DERS 52]. Kapı KLASÖR MODUNDA koşulur:
> `python3 araclar/prompt_kontrol.py yatay_4_dk_filmler/{FILM}`.
>
> 🪟 **S13 KOKPİT EKİDİR** (sahip kararı 07.10.2026 — "tek kamera + 2 kokpit"): S12'nin I2V'si
> ana kare **G14**'e biter, S13 kokpitte G13 → G13′ koşar, S14 yine G14'ten başlar. Kokpit
> karelerinin SITE bloğu ana SITE ile iki cümleyi BİREBİR paylaşır (uzak kıyı + ufuk) [DERS 10].
>
> ⛔ Kelime kilitleri: "crane" yalnız G0 · G1 · G3 · G4 ve S0–S4 I2V'lerinde; "canoe" yalnız G25'ten
> sonra; YASAK KELİME (PLAN künyesi) hiçbir promptta yok — negatifte bile.

---
"""

H2 = f"""# 🎬 {FILM} — BÖLÜM 2  (S15 – S29 · G15 … G30 + 15 I2V · 120,0–240,0 sn) + ⭐ USTA KARE G30

> Bölüm 1 ile aynı kurallar: **yalnız sahne blokları**, her prompt self-contained, STRUCTURE ve
> SITE / BACKGROUND birebir, blok etiketleri birebir [DERS 20].
>
> ⛔ **Bölüm 2 "devamı" değildir, ikinci yarıdır.** "Bölüm 1'deki gibi" atfı yasak; model bu
> dosyayı tek başına okuyor. İLK görsel **G15** bölüm 1'in son I2V'sinin HEDEF karesidir — aynı
> kare, iki dosyada bir kez yazılır (burada); bölüm 1'in S14 I2V'si onu "second provided image"
> olarak alır.
>
> 🪟 **S21 KOKPİT EKİDİR**: S20'nin I2V'si ana kare **G22**'ye biter, S21 kokpitte G21 → G21′ koşar,
> S22 yine G22'den başlar.
>
> ⭐ **USTA KARE G30 bu dosyanın sonunda, kendi `## 🌟 USTA KARE` bölümündedir** — sahne
> değildir, son klibin (S29: G29 → G30) hedef karesidir ve kapak kaynağıdır.
>
> ⭐ S28 · S29 GERÇEK ZAMANDIR (rejim G · "eight seconds pass") — kano gerçek hızda; insan kuralı
> "no readable face". S29 son dört saniyesi TUTUŞTUR (final kanıtı 236,0–240,0).

---
"""

b1 = H1 + "\n" + "\n".join(blok(d) for d in S if d["n"] <= 14)
b2 = H2 + "\n" + "\n".join(blok(d) for d in S if d["n"] >= 15) + "\n" + usta_blok()
open(os.path.join(OUT, f"{FILM}_BOLUM_1.md"), "w").write(b1)
open(os.path.join(OUT, f"{FILM}_BOLUM_2.md"), "w").write(b2)
print("yazıldı", len(b1), len(b2))

import json
if "--json" in sys.argv: json.dump([{k: d[k] for k in ("n","fiil","eleman","rejim","t0","t1","st","g") } | {"nxt": d.get("nxt", f"G{d['n']+1}"), "mf": d["mf"]} for d in S],
          open(os.path.join(OUT, "sahne.json"), "w"), ensure_ascii=False, indent=1)
