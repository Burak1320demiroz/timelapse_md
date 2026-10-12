# THE BURIED KHAN — bölüm dosyası üretici (ortak bloklar tek kaynaktan, DERS 20)
# KULLANIM (depo kökünden):
#   python3 yatay_2_dk_filmler/THE_BURIED_KHAN/00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py yatay_2_dk_filmler/THE_BURIED_KHAN
#   → THE_BURIED_KHAN_BOLUM_1.md + _BOLUM_2.md yeniden yazılır; ardından prompt_kontrol.py klasör modunda koşulur.
#   --tablo  → PLAN kare tablosu satırlarını basar (saat · azimut · yükseklik · kadrajda gölge yönü)
# ⛔ ÜRETİM BAŞLADIKTAN SONRA KOŞULMAZ: üretilmiş filmin promptu kanıttır (URETIM_GUNLUGU kuralı).
# ⛔ Bölüm dosyası elle düzeltilirse bu betik o düzeltmeyi EZER — düzeltme önce buraya yazılır.
# Kalıp: yatay_2_dk_filmler/THE_HIDDEN_FALLS/00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py (08.10.2026) —
#        tek istasyon (ikinci istasyon YOK), bölüm sınırı betiğin ceil(15/2) bölmesi: G8.
import math, os, sys

FILM = "THE_BURIED_KHAN"
OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
N_SAHNE = 15
B1_SON = 7          # BOLUM_1 = S0–S7 · BOLUM_2 = S8–S14 + USTA (sınır G8)
BEARING = 20        # kamera bakışı (derece, kuzeyden) — cephe 200°'ye bakar

# ── güneş (30° K · δ +20° · güneş saati) ───────────────────────────────────
phi, dec = math.radians(30.0), math.radians(20.0)
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
HEAD_MAIN = ("Photorealistic documentary site photograph — Scene {n} of 15. Horizontal 16:9 time-lapse of a long stone "
             "caravanserai being dug out of the desert sand and repaired; a progress photograph from a fixed 24 mm site "
             "camera.")
HEAD_USTA = ("Photorealistic documentary site photograph — master frame G15, the target frame of the last shot "
             "(Scene 14 of 15). Horizontal 16:9 time-lapse of a long stone caravanserai dug out of the desert sand and "
             "repaired; a progress photograph from a fixed 24 mm site camera.")
CAM_MAIN = ("Camera: MAIN STATION — fixed tripod bolted to the top of a low dark rock outcrop on the open desert floor, "
            "lens 6 metres above the desert floor, 67 metres from the face of the caravanserai along the lens axis, "
            "bearing 20 degrees, tilt 0 degrees, zero roll. The camera never moves.")
STRUCT = ("STRUCTURE: When finished this will be a long two-storey caravanserai of honey-coloured sandstone, 60 metres "
          "wide, behind a stone-paved forecourt: a blank lower storey, an open arcade of sixteen round arches above it, a "
          "tall gateway frame around a pointed arch at its centre with a pair of heavy timber doors, and a round corner "
          "tower with a domed cap at each end.")
SITE_MAIN = ("SITE / BACKGROUND: A wide flat desert of pale gold sand and grey gravel under a dead level horizon. Far "
             "away on the right a single flat-topped mesa of red-brown rock sits on the horizon. On the left a single "
             "dead acacia tree with a flat crown of bare grey branches stands on a low dark rock outcrop. Low sand "
             "ripples and scattered dark stones cover the foreground.")
NEG_MAIN = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The flat-topped mesa on the horizon "
            "keeps exactly the same silhouette in every frame; the dead acacia tree, its rock outcrop and the dead level "
            "horizon never change shape, position, size or spacing; heat shimmer only near the ground. The desert holds "
            "exactly one building site, this one. Nothing already built or uncovered is removed or resized; no opacity "
            "fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. "
            "Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. "
            "No architectural visualisation look, no CGI aesthetic.")
OUTPUT = "Output: 16:9, 4K, no text, no watermark."
CREW = "Crew register only as faint soft motion streaks beside their machines, never as sharp figures."
FILMSTOCK = "A documentary site photograph on colour negative film, true colour, fine grain."

COMP_HEAD = ("COMPOSITION: Horizontal 16:9. The camera is level: the horizon runs dead level at exactly half the frame "
             "height. The dead acacia tree spans about 105 pixels of frame width — about one eighteenth — from about 154 "
             "to 259 pixels from the left, its crown top at about fifty-four percent of frame height, and keeps that width "
             "and position in every frame; the mesa sits on the horizon from about 1660 to 1840 pixels. ")
C_DUNE = ("The long dune fills the middle of the frame from about 270 to 1650 pixels from the left, its crest at about "
          "sixty percent of frame height at the centre.")
C_FACADE = ("The caravanserai spans from about 330 to 1590 pixels from the left, from its foot at about thirty-nine "
            "percent of frame height to its wall top at about fifty-five percent; the gateway frame rises to about "
            "sixty-six percent.")
C_GATE = ("The pointed arch of the gateway stands at the centre, from about 912 to 1008 pixels from the left, its top at "
          "about fifty-three percent of frame height.")
C_BREACH = ("The breach right of the gateway runs from about 1190 to 1380 pixels from the left, down to about forty-six "
            "percent of frame height.")
C_BERM = "The low berm on the right runs from about 1530 pixels to the right edge, its top just below the horizon."
COMP_TAIL = ("The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth "
             "or the top-right corner of the frame.")

TR_A = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, drifting sand, machines, "
        "vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay "
        "almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay "
        "recognisable, trailing light motion blur. Nothing moves at normal speed.")
TR_B = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, drifting sand, machines, "
        "vehicles and crew all move at the same accelerated speed. Two hours pass across this shot: the shadows swing "
        "slowly round, the clouds streak across the sky, and machines smear into heavy motion blur. Nothing moves at "
        "normal speed.")
TR_G = ("TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the doors, "
        "the people and the lamplight move at their real pace; nothing is accelerated.")

I2V_HEAD = ("The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its "
            "last frame is that image, matched frame for frame — same framing, same light, same objects in the same "
            "places.")
LOCK_MAIN = ("The camera does not move at any point. The framing is identical in the first and last frame. The "
             "flat-topped mesa, the dead acacia tree, its rock outcrop and the dead level horizon stay exactly where they "
             "are, at exactly the same size and shape, for the whole shot; the acacia occupies exactly the same width of "
             "the frame in the first and last frame, and the horizon stays at exactly half the frame height. The desert "
             "holds exactly one building site. Nothing already built or uncovered is removed or resized.")
I2V_TAIL = ("Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
            "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
            "documentary time-lapse cinematography.")

# ── tekrarlanan durum cümleleri (aynı nesne her karede aynı kelimelerle) ─────
DUNE0 = ("a long smooth dune of pale gold sand, about twelve metres high, buries the whole caravanserai; only three "
         "weathered stone tips stand out of its crest — the flat top of a tall stone gateway frame at the centre and the "
         "domed caps of two round towers near its two ends")
STACK = "a stack of pale new cut stone blocks lies on timber bearers on the sand at the front left"
STACK_LOW = "the stack of new stone blocks at the front left is down to a few courses"
BERM_P = ("a long low windbreak berm of sand, about four metres high, runs along the right side behind the right tower, "
          "fed by a long conveyor belt from the right end of the site")
BERM = "a low windbreak berm of sand runs along the right side, with a line of palm-frond fences along its crest"
CONVEYOR_PARK = "the long conveyor belt stands folded and idle at the foot of the berm"
FACE_TOP = ("the honey-coloured stone of the upper storey stands out of the sand along the whole front — the open arcade "
            "of round arches from the left tower to the gateway and on to the right tower, broken right of the gateway by "
            "a wide gap where the arches have fallen")
FACE_DAMAGED = ("the honey-coloured stone face of the caravanserai stands free of sand over its full height — the blank "
                "lower storey, the arcade, the gateway frame round its pointed arch and the two domed towers; right of the "
                "gateway a breach about ten metres wide has torn four arches and the wall below them down to about four "
                "metres above the ground")
HEAP = "the fallen blocks of the breach lie in a rough heap at its foot"
SCAFF = "a steel scaffold stands against the wall at the breach"
REBUILT_WALL = ("the breach right of the gateway is rebuilt in paler new stone up to the springing of the arches, its "
                "piers standing up into the open gap of the arcade")
REBUILT = ("the breach right of the gateway is rebuilt in paler new stone, wall and arches, and the arcade runs unbroken "
           "from tower to tower")
DOORS = "a pair of heavy dark timber doors closes the pointed arch of the gateway"
BUILT = ("the restored caravanserai stands complete — its honey-coloured stone face, the unbroken arcade of sixteen "
         "round arches, the paler new stone of the rebuilt section right of the gateway, the band of carved geometric "
         "relief round the pointed arch, the pair of heavy dark timber doors and the two domed corner towers")
LANTERNS = "an iron lantern hangs unlit from an iron bracket in each of the sixteen arches"
LIT = ("all sixteen iron lanterns in the arcade are lit, every arch glowing warm, and a soft warm light falls from them "
       "onto the face of the stone")
OPEN = ("the two heavy timber doors stand open inward, and warm light from the courtyard inside pours out through the "
        "pointed arch in a long bright fan across the forecourt")
FORECOURT = "the stone-paved forecourt lies swept and clear in front of the caravanserai"
def U(x): return x[0].upper() + x[1:]

# ── doku ────────────────────────────────────────────────────────────────────
T_DUNE = ("Fine pale gold sand with crisp wind ripples across the dune, a thin plume of sand streaming off the crest, "
          "weathered honey-coloured stone tips pitted and rounded by the wind, dark gravel and scattered stones on the "
          "flat desert floor, fresh tyre tracks and footprints at the foot of the dune. " + FILMSTOCK)
T_DIG = ("Fresh-cut sand faces darker where the sand is opened, crisp wind ripples on the untouched slopes, weathered "
         "stone with sand packed in its joints and pale scars, deep tyre ruts and tracks, a film of dust over every "
         "machine, scattered gravel at the foot of the cut. " + FILMSTOCK)
T_RUBBLE = ("Honey-coloured stone with sand packed in its joints and pale scars where blocks broke away, a rough heap "
            "of fallen blocks half sunk in sand, trampled sand with tyre ruts and footprints, worn grey paving slabs "
            "showing through a film of sand, dry palm fronds in bundles. " + FILMSTOCK)
T_REPAIR = ("Old honey-coloured stone weathered and pitted beside crisp pale new blocks with sharp arrises, fresh "
            "lime mortar drying from grey to cream in the joints, stone dust on the scaffold boards, worn grey paving "
            "slabs with pale mortar stains, rows of salvaged blocks on the forecourt, footprints in a film of sand. " + FILMSTOCK)
T_FINISH = ("Honey-coloured stone brushed clean, the pale new blocks of the repair already dulled by a film of dust, "
            "cream lime mortar in the joints, worn grey paving slabs swept clean, a thin skin of fresh drift sand along "
            "the foot of the walls, pale broom streaks across the paving, wind ripples on the berm. " + FILMSTOCK)
T_BLUE = ("Honey-coloured stone gone cool and grey-blue in the dusk, the pale new blocks of the repair dulled by dust, "
          "worn grey paving swept clean with pale broom streaks, a thin skin of drift sand along the foot of the walls, "
          "wind ripples on the berm in cool blue light. " + FILMSTOCK)
T_DUSK = ("Honey-coloured stone gone soft amber in the lamplight, warm light pooling on the worn grey paving, the "
          "pale new blocks of the repair dulled by dust, a thin skin of drift sand along the foot of the walls, pale broom "
          "streaks across the paving, wind ripples on the berm in cool blue light. " + FILMSTOCK)

# ── ışık (bakış 20° — sabah güneşi önde sağda, akşam solda; hiçbir karede kadrajda değil) ──
LIGHT_DESC = {
 "dawn": ("low ahead on the right, beyond the right edge of the frame, so the face of the dune turned to the camera "
          "lies in cool blue shade while its crest and its right flank catch warm early light; long shadows fall towards "
          "the camera and to the left."),
 "am": ("ahead on the right, beyond the right edge of the frame, so the faces turned to the camera are still in soft "
        "shade under the bright sky while the tops catch hard light; shadows fall to the left and towards the camera."),
 "late_am": ("high on the right, so the light grazes the stone from the right and every joint and ripple casts a short "
             "hard shadow to the left."),
 "noon": ("almost overhead and a little behind the camera, so the light falls flat and hard on the stone and the "
          "shadows at the foot of every wall are short, black and fall away from the camera."),
 "pm": ("high on the left behind the camera, lighting the face of the stone from the left, with short hard shadows "
        "falling to the right and away from the camera."),
 "low": ("low on the left, raking the face of the stone from the left in warm gold light, with long shadows falling to "
         "the right across the sand."),
 "blue": ("below the horizon on the left, outside the frame, so there is no direct sun: deep blue hour, the sky deep "
          "clear blue with a last pale band low on the left, the sand and the stone cool blue-grey."),
}
SEASON = {
 "winter": "Winter: a crisp clear pale blue sky with a few thin high clouds, the air very clear and the mesa sharp on the horizon.",
 "spring": "Spring: a clear sky with a few small high clouds, a faint dust haze low over the horizon.",
 "summer": "Summer: a pale hazy sky bleached almost white near the horizon, a dust haze softening the mesa.",
 "autumn": "Autumn: a clear deep sky with a few thin high clouds, the air clear again and the mesa sharp on the horizon.",
}
def LIGHT(t, key, season):
    return f"LIGHTING: {sunline(t)}, {LIGHT_DESC[key]} {SEASON[season]} The sun stays outside the frame."

# ── sahne verisi ─────────────────────────────────────────────────────────────
S = []
def scene(**k): S.append(k)

# ---------- S0 ----------
scene(n=0, fiil="KAZAR", eleman="kumul sırtı +12 → kapı çerçevesinin çevresi açılır (%10) · taş istifi 0 → 1", rejim="A", t0="06:00", t1="06:10",
 g="G0",
 stage=("nothing has been uncovered yet. " + U(DUNE0) + ". A thin plume of sand streams off the crest of the dune. A "
        "yellow tracked excavator stands high on the left shoulder of the dune with its bucket already biting into the "
        "crest, a yellow dumper truck waits at the foot of the dune, and a small crew with shovels stands round the top of "
        "the gateway frame. A flatbed truck loaded with pale cut stone blocks has just stopped on the flat sand at the "
        "front left."),
 moment="Six in the morning on the first day of work: the excavator takes its first bite out of the dune.",
 comp=C_DUNE + " The top of the gateway frame stands out of the crest at the centre, from about 845 to 1075 pixels from the left.",
 light=LIGHT("06:00", "dawn", "winter"),
 tr=TR_A,
 act=("The excavator swings each bucket of sand off the crest of the dune and tips the load into the dumper truck, the "
      "crew shovels sand away from the top of the gateway frame, and a second crew unloads the stone blocks from the flatbed truck into a "
      "stack on timber bearers. " + CREW),
 tex=T_DUNE,
 phys=("The excavator stands on its tracks on the shoulder of the dune, its bucket resting in the sand of the crest. "
       "The dumper truck stands on its wheels on the flat sand. The stone blocks rest on the bed of the flatbed truck, "
       "and the acacia stands on its rock outcrop."),
 mf=("The excavator scoops sand from the crest of the dune into the dumper truck, and the crew carries the cut stone "
     "blocks from the flatbed truck onto a stack on timber bearers on the sand."),
 body=("Ten minutes pass in the early light. Everything in this shot is time-lapsed at the same rate. From the first "
       "frame the excavator bucket is already biting into the crest: it swings full loads of sand down into the dumper, "
       "and sand slides in small runs down the face of the dune. Round the top of the gateway frame the crew digs, and "
       "more of the weathered stone frame comes out of the sand. The crew unloads the flatbed truck block by block onto a "
       "stack on the sand. Halfway through, a second yellow excavator crawls in from the right to the right end of the "
       "dune, and the dumper drives off loaded to the right. The thin plume of sand keeps streaming off the crest. Long "
       "shadows lean towards the camera, and a few thin high clouds drift slowly from the right in one smooth flow."))

# ---------- S1 ----------
scene(n=1, fiil="SIYIRIR", eleman="kumul +12 → +9 (cephe önünde) · kapı çerçevesi %40 · kule kubbeleri açık · set %20", rejim="B", t0="06:10", t1="08:10",
 g="G1",
 stage=(U(DUNE0) + "; round the top of the gateway frame a shallow pit has been dug, its raw cut faces stepped in small "
        "benches. A thin plume of sand streams off the "
        "crest of the dune. Two yellow tracked excavators work on the crest, one at the left shoulder and one at the right "
        "end, and a yellow dumper truck waits at the foot. At the right end of the dune a long conveyor belt has just been "
        "set up, running from the foot of the dune out to the right. " + U(STACK) + "."),
 moment="Ten past six in the morning: the first pit is open round the gateway and the conveyor is ready.",
 comp=C_DUNE + " The top of the gateway frame stands out of the crest at the centre, from about 845 to 1075 pixels from the left.",
 light=LIGHT("06:10", "dawn", "winter"),
 tr=TR_B,
 act=("The two excavators cut the crest of the dune down and tip the sand into a line of dumper trucks and onto the "
      "conveyor belt, which drops the sand onto a growing long heap on the right. " + CREW),
 tex=T_DIG,
 phys=("The excavators stand on their tracks on the cut top of the dune. The conveyor belt stands on its wheeled legs on "
       "the flat sand, its far end resting over the new heap. The dumper truck stands on its wheels at the foot of the "
       "dune, and the stack of blocks rests on its timber bearers."),
 mf=("The two excavators cut the top of the dune down from the crest to the height of the walls, loading the sand into "
     "dumper trucks and onto the conveyor belt, which carries it out to a long low heap on the right."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The crest of the dune sinks steadily "
       "under the two excavators: the top of the gateway frame grows taller out of the sand, the domed caps of the two "
       "towers come clear, and a straight line of honey-coloured stone begins to show along the top of the buried wall. "
       "A line of dumper trucks streams away to the right, and the conveyor belt pours a steady stream of sand onto a long "
       "low heap on the right that grows into the start of a berm. The plume of sand off the crest thins. The shadows "
       "swing slowly from the left round towards the camera as the sun climbs on the right, and thin clouds streak "
       "across the sky."))

# ---------- S2 ----------
scene(n=2, fiil="AÇAR", eleman="kum +9 → +5 · üst kat kemer sırası soldan sağa %100 görünür · gedik belirir · set %50", rejim="B", t0="08:10", t1="10:10",
 g="G2",
 stage=("the top of the dune has been cut away down to the height of the walls: the flat top of the tall gateway frame "
        "and the domed caps of the two round towers stand clear, and the straight top of the long wall shows along the "
        "whole front, sand still packed against it up to the brim, its raw cut face stepped in benches by the buckets. Two yellow tracked excavators work on the cut sand, "
        "a dumper truck waits at the foot, and the long conveyor belt runs from the right end of the site to a long low "
        "heap of sand on the right. " + U(STACK) + "."),
 moment="Ten past eight in the morning: the top of the wall shows along the whole front.",
 comp=C_FACADE + " Sand still covers the face of the wall up to its top.",
 light=LIGHT("08:10", "am", "winter"),
 tr=TR_B,
 act=("The two excavators dig the sand away from the face of the upper storey from the left to the right and tip the "
      "sand into the dumper trucks and onto the conveyor belt, while a crew with shovels clears sand from inside each arch "
      "as it opens. " + CREW),
 tex=T_DIG,
 phys=("The excavators stand on their tracks on the packed sand in front of the wall. The conveyor belt stands on its "
       "wheeled legs, its far end resting over the heap. The domed caps rest on the round towers, and the stack of blocks "
       "rests on its timber bearers."),
 mf=("The two excavators dig the sand away from the front of the upper storey from the left end to the right end, "
     "loading it onto the conveyor belt and into the dumper trucks."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The sand falls away from the front of "
       "the upper storey, left end first: one round arch after another opens along the arcade, dark inside, from the left "
       "tower to the gateway, and on past it towards the right tower; right of the gateway the arcade breaks off into a "
       "wide ragged gap. The towers come out of the sand to half their height. The conveyor belt keeps pouring sand onto "
       "the heap on the right, which lengthens into a low berm, and the dumper trucks carry the rest of the sand away to the right. The shadows "
       "shorten as the sun climbs on the right, and thin clouds streak across the sky."))

# ---------- S3 ----------
scene(n=3, fiil="ORTAYA ÇIKARIR", eleman="kum +5 → zemin (cephe önü) · cephe tam boy %100 · gedik + yıkıntı yığını görünür · avlu hâlâ kumda", rejim="B", t0="10:10", t1="12:10",
 g="G3",
 stage=(U(FACE_TOP) + "; below it the lower storey is still buried, sand packed against it up to the foot of the arcade. "
        "Its raw cut face of sand is stepped in benches by the buckets. Two yellow tracked excavators work on the packed sand "
        "in front of the wall, a dumper truck waits at the foot, and "
        "the long conveyor belt runs from the right end of the site to a long low berm of sand on the right. " + U(STACK) + "."),
 moment="Ten past ten in the morning: the arcade is out of the sand, and the lower storey is still buried.",
 comp=C_FACADE + " Sand covers the lower storey up to about forty-eight percent of frame height.",
 light=LIGHT("10:10", "late_am", "spring"),
 tr=TR_B,
 act=("The two excavators dig the last of the sand away from the lower storey and tip the sand into the dumper trucks "
      "and onto the conveyor belt, while the crew digs round the fallen blocks at the foot of the breach. " + CREW),
 tex=T_RUBBLE,
 phys=("The excavators stand on their tracks on the sand in front of the wall. The conveyor belt stands on its wheeled "
       "legs on the flat sand. The fallen blocks lie half sunk in the sand at the foot of the breach, and the stack of new "
       "blocks rests on its timber bearers."),
 mf=("The two excavators dig the sand away from the lower storey down to the desert floor, from the left end to the "
     "right end, loading it onto the conveyor belt and into the dumper trucks."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The sand drops away from the face of "
       "the lower storey from the left: the blank wall with its narrow slit windows comes out of the sand, the towers "
       "stand clear down to their feet, and the pointed arch of the gateway opens, still filled with sand to two thirds "
       "of its height. Right of the gateway the breach shows its full size, torn down to about four metres above the "
       "ground, and a heap of fallen blocks rises out of the sand at its foot. A ramp of sand still slopes from the foot of "
       "the wall towards the camera, and each dumper truck carries its load away to the right. Twice a thin run of sand slides back off the cut face into the opened gateway. The "
       "shadows shorten and swing as the sun climbs high on the right, and thin clouds streak across the sky."))

# ---------- S4 ----------
scene(n=4, fiil="TEMİZLER", eleman="avlu döşemesi %0 → %100 · kapı ağzı kumdan boşalır · set %100 + hurma dalı çit · ekskavatörler gider", rejim="A", t0="12:10", t1="12:20",
 g="G4",
 stage=(U(FACE_DAMAGED) + "; the pointed arch of the gateway is still filled with sand to two thirds of its height. " + U(HEAP) +
        ". A ramp of sand still slopes from the foot of the wall towards the camera over the buried forecourt, its raw cut "
        "face stepped in benches. Two yellow "
        "tracked excavators and a dumper truck work on the ramp, the long conveyor belt runs from the right end of the "
        "site to a long low berm of sand on the right, and bundles of dry palm fronds lie at the foot of the berm. "
        + U(STACK) + "."),
 moment="Ten past twelve, midday: the whole face of the caravanserai stands out of the sand, and the breach is plain to see.",
 comp=C_FACADE + " " + C_BREACH,
 light=LIGHT("12:10", "noon", "spring"),
 tr=TR_A,
 act=("The two excavators dig the ramp of sand off the forecourt and tip the sand into the dumper trucks, and a crew on "
      "the berm lifts the palm fronds from the bundles and plants them in a line of fences along its crest. " + CREW),
 tex=T_RUBBLE,
 phys=("The excavators stand on their tracks on the ramp of sand. The conveyor belt stands on its wheeled legs at the "
       "foot of the berm. The fallen blocks lie in their heap on the sand, and the palm-frond bundles rest on the sand at "
       "the foot of the berm."),
 mf=("The two excavators dig the ramp of sand from the forecourt and the gateway into the dumper trucks, and the crew "
     "carries the palm fronds from the bundles onto the crest of the berm."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the excavator "
       "buckets are already scraping the ramp: the sand slope shrinks back towards the wall and worn grey paving slabs "
       "appear under it, row after row, until the whole forecourt lies open; the sand inside the pointed arch of the "
       "gateway is dug out down to its threshold. The crew carries the palm fronds from the bundles up the berm, and along its "
       "crest a line of palm-frond fences stands up, bundle by bundle. At the end the two excavators and the dumper truck drive off to the right and out of the frame; the "
       "conveyor belt is folded and stays at the foot of the berm. Short hard shadows stay at the foot of the wall, and a "
       "few small clouds drift slowly from the right."))

# ---------- S5 ----------
scene(n=5, fiil="KALDIRIR", eleman="mobil vinç girer · iskele 0 → %100 (gedikte) · yıkıntı yığını → avluda sıralar (%100)", rejim="A", t0="12:20", t1="12:30",
 g="G5",
 stage=(U(FACE_DAMAGED) + ". " + U(HEAP) + ". " + U(FORECOURT) + ", a thin skin of sand across it. " + U(BERM) + ", and "
        + CONVEYOR_PARK + ". " + U(STACK) + ". A flatbed truck loaded with steel scaffold tubes and boards stands on the "
        "forecourt left of the breach."),
 moment="Twenty past twelve: the forecourt is open, and the scaffold has arrived.",
 comp=C_FACADE + " " + C_BREACH + " " + C_BERM,
 light=LIGHT("12:20", "noon", "spring"),
 tr=TR_A,
 act=("The crew lifts the scaffold tubes from the flatbed truck and bolts a steel scaffold up against the wall at the "
      "breach, while a second crew levers the fallen blocks at the foot of the breach apart with steel bars. " + CREW),
 tex=T_RUBBLE,
 phys=("The fallen blocks lie in their heap on the paving at the foot of the breach. The flatbed truck stands on its "
       "wheels on the forecourt, the scaffold tubes resting on its bed. The stack of new blocks rests on its timber "
       "bearers, and the fences stand in the sand of the berm."),
 mf=("A small mobile crane drives in from the right onto the forecourt, the crew carries the scaffold tubes from the "
     "flatbed truck to the breach and bolts up the scaffold, and the crane lifts the fallen blocks from the heap and lays "
     "them in rows on the forecourt."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the crew is "
       "already carrying tubes: a steel scaffold climbs the wall at the breach lift by lift, and the flatbed truck drives "
       "off empty to the left. A small mobile crane drives in from the right, sets its outriggers on the paving right of "
       "the gateway and begins lifting the fallen blocks from the heap one by one; they come down on the forecourt in "
       "neat rows, and the heap at the foot of the breach shrinks. Short hard shadows stay at the foot of the wall, and a "
       "few small clouds drift slowly from the right."))

# ---------- S6 ----------
scene(n=6, fiil="ÖRER", eleman="gedik duvarı +4 → kemer üzengisi (%100) · ayaklar · eski taş + yeni açık taş · istif azalır", rejim="B", t0="12:30", t1="14:30",
 g="G6",
 stage=(U(FACE_DAMAGED) + ". " + U(SCAFF) + ". The salvaged blocks of the breach lie in neat rows on the forecourt. A small "
        "mobile crane stands on its outriggers on the paving right of the gateway, with a salvaged block slung on the hook. "
        + U(BERM) + ", and " + CONVEYOR_PARK + ". " + U(STACK) + "."),
 moment="Half past twelve: the scaffold stands at the breach, and the salvaged blocks lie in rows.",
 comp=C_FACADE + " " + C_BREACH + " " + C_BERM,
 light=LIGHT("12:30", "noon", "spring"),
 tr=TR_B,
 act=("The crane lifts the salvaged blocks from the rows and new blocks from the stack up to the scaffold, where masons "
      "bed them in lime mortar course by course across the breach; the crane carries a visible load, with a stone block "
      "slung on the hook. " + CREW),
 tex=T_REPAIR,
 phys=("The crane stands on its outriggers on the paving, the block hanging from its hook on two slings. The scaffold "
       "stands on base plates on the forecourt and is tied to the wall. The salvaged blocks rest in rows on the paving, "
       "and the new blocks rest on their timber bearers."),
 mf=("The crane lifts the salvaged blocks from the rows and the new blocks from the stack onto the scaffold, and the "
     "masons lay them course by course into the breach and up into its piers."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The crane swings block after block "
       "from the forecourt up to the scaffold; course by course the wall of the breach rises from about four metres to the "
       "foot of the arcade, old weathered blocks mixed with pale new ones, and the piers between the missing arches stand "
       "up into the gap. The rows of salvaged blocks on the forecourt empty, and the stack of new blocks at the front left "
       "shrinks to a few courses. The shadows swing from the left round to the right as the sun passes behind the camera, "
       "and white clouds streak across the sky."))

# ---------- S7 ----------
scene(n=7, fiil="KAPATIR", eleman="eksik kemer 0 → 4 (ahşap kalıp üstünde) · korkuluk duvarı +9 · kalıp sökülür", rejim="A", t0="14:30", t1="14:40",
 g="G7",
 stage=(U(REBUILT_WALL) + ". The rest of the honey-coloured stone face stands whole: the blank lower storey with narrow slit "
        "windows, the open arcade along the upper storey, the tall gateway frame round its pointed arch and the round "
        "corner towers with their domed caps. " + U(SCAFF) + ". Four curved timber arch frames stand ready on the scaffold "
        "boards, and the small mobile crane on the paving right of the gateway has a pallet of wedge-shaped arch stones on "
        "its hook. " + U(BERM) + ", and " + CONVEYOR_PARK + ". " + U(STACK_LOW) + "."),
 moment="Half past two in the afternoon: the wall of the breach is back up to the arcade.",
 comp=C_FACADE + " " + C_BREACH + " " + C_BERM,
 light=LIGHT("14:30", "pm", "spring"),
 tr=TR_A,
 act=("The masons set the curved timber frames between the piers, and the crane lifts the wedge-shaped arch stones from "
      "the pallet to them stone by stone; the crane carries a visible load, with a pallet of arch stones slung on the "
      "hook. " + CREW),
 tex=T_REPAIR,
 phys=("The crane stands on its outriggers on the paving, the pallet hanging from its hook on four slings. The timber "
       "frames stand on the piers of the breach. The scaffold stands on base plates on the forecourt and is tied to the "
       "wall."),
 mf=("The crane lifts the wedge-shaped arch stones from the pallet onto the timber frames between the piers, and the "
     "masons close the four missing arches one by one from the left, then take the timber frames down."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first timber "
       "frame is already standing between two piers: the arch stones climb it from both sides and meet at the top, and "
       "the frame is knocked out from under the finished arch; the next frame goes in, and four new round arches close "
       "the gap one by one from the left. The masons lay a last course of stone over them up to the top of the wall, and "
       "the arcade runs unbroken from tower to tower. The struck timber frames are lowered to the paving. Short shadows "
       "lean to the right, and a few small clouds drift slowly from the right."))

# ---------- S8 ----------
scene(n=8, fiil="ASAR", eleman="kapı kanadı 0 → 2 (vinçten) · kapı kapalı · vinç gider", rejim="A", t0="14:40", t1="14:50",
 g="G8",
 stage=(U(REBUILT) + ". The rest of the honey-coloured stone face stands whole: the blank lower storey with narrow slit "
        "windows, the tall gateway frame round its open pointed arch, empty down to its stone threshold, and the round "
        "corner towers with their domed caps. " + U(SCAFF) + ". The small mobile crane on the paving right of the gateway "
        "has a heavy dark timber door leaf slung upright on its hook, and the second leaf lies flat on timber bearers on the "
        "forecourt. " + U(BERM) + ", and " + CONVEYOR_PARK + ". " + U(STACK_LOW) + "."),
 moment="Twenty to three in the afternoon: the arcade is whole again, and the doors are on the forecourt.",
 comp=C_FACADE + " " + C_GATE + " " + C_BERM,
 light=LIGHT("14:40", "pm", "spring"),
 tr=TR_A,
 act=("The crane swings the first heavy timber door leaf to the gateway, where a crew guides it onto its iron pins with "
      "taglines; the crane carries a visible load, with a heavy door leaf slung on the hook. " + CREW),
 tex=T_REPAIR,
 phys=("The crane stands on its outriggers on the paving, the door leaf hanging from its hook on two slings. The second "
       "leaf rests flat on timber bearers on the forecourt. The scaffold stands on base plates on the forecourt and is "
       "tied to the wall."),
 mf=("The crane lifts the two heavy timber door leaves one after the other from the forecourt into the pointed arch of "
     "the gateway, and then the small mobile crane folds its boom and drives away to the right."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first door "
       "leaf is already swinging towards the gateway: it settles onto its pins on the left side of the arch, and the hook "
       "goes back for the second leaf, the crane lifts it from its stack of timber bearers and sets it on the right side; the two leaves close "
       "together and the pointed arch is shut. In the second half of the shot the crane lifts its outriggers, folds its "
       "boom and drives off to the right and out of the frame. Short shadows lean to the right, and a few small clouds "
       "drift slowly from the right."))

# ---------- S9 ----------
scene(n=9, fiil="DİRENİR", eleman="ikindi rüzgârı: kum setten savrulur → çitte birikir · avluya ince kum dili → süpürülür", rejim="B", t0="14:50", t1="16:50",
 g="G9",
 stage=(U(DOORS) + ". " + U(REBUILT) + ". The rest of the honey-coloured stone face stands whole, the round corner towers "
        "with their domed caps. " + U(SCAFF) + ". " + U(FORECOURT) + ". " + U(BERM) + ", and " + CONVEYOR_PARK + ". "
        + U(STACK_LOW) + ". The air is still."),
 moment="Ten to three in the afternoon: the doors are hung and the wind is about to rise.",
 comp=C_FACADE + " " + C_GATE + " " + C_BERM,
 light=LIGHT("14:50", "pm", "summer"),
 tr=TR_B,
 act=("A hot wind rises from the right and blows sand off the berm against the palm-frond fences, and a crew with wide "
      "brooms sweeps the thin tongues of drift sand into barrows and tips the barrows onto a heap at the foot of the "
      "berm. " + CREW),
 tex=T_FINISH,
 phys=("The palm-frond fences are planted in the sand of the berm, sand piled against their windward side. The "
       "scaffold stands on base plates on the forecourt and is tied to the wall. The closed doors are seated on iron pivots set "
       "in the threshold stone, and the conveyor belt rests folded at the foot of the berm."),
 mf=("The wind blows sand from the open desert on the right over the berm onto the palm-frond fences, and the crew "
     "sweeps the drift sand from the forecourt into barrows and wheels it back to the berm."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The wind rises from the right: sand "
       "smokes off the crest of the berm and streams along the ground in pale ribbons, and against the palm-frond fences "
       "it piles up in long smooth drifts, so that the fences catch most of it; a few thin tongues of sand still creep "
       "across the forecourt towards the wall. Again and again the crew sweeps them up and carries the sand in barrows to the "
       "heap at the foot of the berm, and the paving stays clear. A dust haze softens the mesa on the horizon and clears again as the wind drops near "
       "the end. The shadows lengthen to the right as the sun sinks on the left, and hazy clouds streak across the sky."))

# ---------- S10 ----------
scene(n=10, fiil="ASAR ②", eleman="fener 0 → 16 (her kemere bir, sönük) · oyma taş kuşak fırçalanır", rejim="A", t0="16:50", t1="17:00",
 g="G10",
 stage=(U(DOORS) + ". " + U(REBUILT) + ". The rest of the honey-coloured stone face stands whole, the band of carved "
        "geometric relief round the pointed arch still grey with packed dust, and the round corner towers with their "
        "domed caps. " + U(SCAFF) + ". " + U(FORECOURT) + ". " + U(BERM) + ", sand drifted against the fences, and "
        + CONVEYOR_PARK + ". " + U(STACK_LOW) + ". Two wooden crates of iron lanterns and two tall ladders stand on the "
        "forecourt in front of the left part of the arcade, the crates on a small cart; a third tall ladder leans on the "
        "gateway frame."),
 moment="Ten to five in the afternoon: the wind has dropped, and the lanterns have arrived.",
 comp=C_FACADE + " " + C_GATE + " " + C_BERM,
 light=LIGHT("16:50", "low", "summer"),
 tr=TR_A,
 act=("Two workers lift the iron lanterns from the crates on a small cart, wheel the cart along the front and hang "
      "one lantern in each arch of the arcade from the left, while a worker on a tall ladder against the gateway frame brushes the dust out of the carved band "
      "round the gateway arch. " + CREW),
 tex=T_FINISH,
 phys=("The ladders lean against the face of the lower storey, their feet resting on the paving. The crates rest on a "
       "small cart on the paving. The scaffold stands on base plates on the forecourt and is tied to the wall, and the "
       "closed doors are seated on iron pivots set in the threshold stone."),
 mf=("Two workers carry the iron lanterns from the crates on the forecourt up the ladders and hang one in each arch of "
     "the arcade, from the left tower to the right tower."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame a ladder is "
       "already leaning on the wall under the first arch: the two workers move it along the front arch by arch and "
       "hang a dark iron lantern in each arch as they pass, sixteen in all, unlit. Round the gateway the worker "
       "on the tall ladder brushes the grey dust out of the carved band, and its geometric pattern comes up crisp and "
       "honey-coloured. The crates are carried away empty. Long warm shadows lean to the right, and a few thin clouds "
       "drift slowly from the right."))

# ---------- S11 ----------
scene(n=11, fiil="SÖKER", eleman="iskele %100 → 0 · konveyör çekilir · son aletler gider · avlu boş", rejim="A", t0="17:00", t1="17:10",
 g="G11",
 stage=(U(BUILT) + ". " + U(LANTERNS) + ". " + U(SCAFF) + ". " + U(FORECOURT) + ". " + U(BERM) + ", sand drifted "
        "against the fences, and " + CONVEYOR_PARK + ". " + U(STACK_LOW) + ". A flatbed truck and a small tractor stand on "
        "the forecourt in front of the right part of the front."),
 moment="Five in the afternoon: the stone work is finished and the lanterns hang dark.",
 comp=C_FACADE + " " + C_GATE + " " + C_BERM,
 light=LIGHT("17:00", "low", "summer"),
 tr=TR_A,
 act=("The crew strips the scaffold from the top down and stacks the tubes and boards on the flatbed truck, and the small "
      "tractor tows the folded conveyor belt away to the right; the crew lifts the last few new blocks onto the truck. "
      + CREW),
 tex=T_FINISH,
 phys=("The scaffold stands on base plates on the forecourt and is tied to the wall. The flatbed truck stands on its "
       "wheels on the paving, the tubes resting on its bed. The conveyor belt rests folded on its wheels at the foot of "
       "the berm, and the lanterns hang from iron hook brackets in the arches."),
 mf=("The crew takes the scaffold down from the breach tube by tube onto the flatbed truck, the tractor tows the folded "
     "conveyor belt from the foot of the berm out to the right, and the truck drives the tubes and the last blocks away "
     "to the left."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the top lift of "
       "the scaffold is already coming down: lift by lift the scaffold shrinks against the rebuilt section, and the pale "
       "new stone of the repair stands open to view. The small tractor hitches the folded conveyor belt and tows it off to "
       "the right; the crew loads the last few new blocks and their timber bearers onto the flatbed truck, which drives "
       "off to the left and out of the frame. The forecourt is left empty and swept. Long warm shadows lean to the "
       "right, and a few thin clouds drift slowly from the right."))

# ---------- S12 ----------
scene(n=12, fiil="BATAR", eleman="altın ışık → gün batımı → mavi saat · eklenen yok · son süpürme", rejim="B", t0="17:10", t1="19:10",
 g="G12",
 stage=(U(BUILT) + ". " + U(LANTERNS) + ". " + U(FORECOURT) + ". " + U(BERM) + ", sand drifted against the fences. The site is "
        "clear; two workers with wide brooms and a hand cart stand at "
        "the right end of the forecourt."),
 moment="Ten past five in the afternoon: the site is clear, and the caravanserai stands restored in low gold light.",
 comp=C_FACADE + " " + C_GATE + " " + C_BERM,
 light=LIGHT("17:10", "low", "summer"),
 tr=TR_B,
 act=("A crew of two sweeps the last thin skin of drift sand into the hand cart and tips the cart onto the heap at the "
      "foot of the berm, and a light evening wind sends low ripples of sand along the crest of the berm. " + CREW),
 tex=T_FINISH,
 phys=("The closed doors are seated on iron pivots set in the threshold stone. The lanterns hang from an iron hook in each arch. The "
       "palm-frond fences are planted in the sand of the berm, and the hand cart rests on its wheels on the paving."),
 mf=("The sun sinks from the left towards the horizon, its warm light climbing from the foot of the stone to the tops "
     "of the towers and leaving them, until the caravanserai stands in the blue dusk; two workers wheel the swept sand "
     "from the forecourt to the berm."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Low gold light rakes the face of the "
       "caravanserai from the left: the long shadows of every pier and arch stretch out to the right across the stone, "
       "then the light climbs up the face, lingers on the gateway frame and the domed caps of the towers, and leaves "
       "them; the sky over the left burns orange and fades, and the stone and the sand turn cool blue-grey. Early in the "
       "shot two workers sweep the last drift sand off the paving and carry it in the hand cart to the heap at the "
       "foot of the berm. The restored "
       "caravanserai, the dark lanterns and the closed doors do not change. Clouds streak across the sky and thin out."))

# ---------- S13 ----------
scene(n=13, fiil="YAKAR", eleman="fener 0 → 16 yanık (soldan sağa, kemer kemer)", rejim="A", t0="19:10", t1="19:20",
 g="G13", iso=800,
 stage=(U(BUILT) + ". " + U(LANTERNS) + ". " + U(FORECOURT) + ". " + U(BERM) + ", sand drifted against the fences. A "
        "lamplighter with a long pole stands under the first arch at the left end of the arcade, and a last ladder leans on the "
        "wall beside the gateway."),
 moment="Ten past seven in the evening, blue hour: the lamplighter reaches the first lantern.",
 comp=C_FACADE + " " + C_GATE + " " + C_BERM,
 light=LIGHT("19:10", "blue", "autumn"),
 tr=TR_A,
 act=("The lamplighter walks along the front from the left with a long pole and lights the lanterns one after "
      "another, arch by arch, while two workers lift the last ladder onto a small cart and push the cart away to the "
      "left. " + CREW),
 tex=T_BLUE,
 phys=("The lanterns hang from an iron hook on a bracket in each arch. The closed doors are seated on iron pivots set in "
       "the threshold stone. The palm-frond fences are planted in the sand of the berm, and the cart rests on its wheels "
       "on the paving."),
 mf=("The lamplighter carries a flame along the front of the arcade from the left tower to the right tower, and the "
     "sixteen iron lanterns light one by one from the left to the right."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first "
       "lantern at the left end is already catching: then the next arch glows, and the next, a warm light running from "
       "the left along the arcade past the gateway to the right tower, until all sixteen arches glow and a soft warm light "
       "falls onto the face of the stone. The lamplighter stays a faint soft streak, and early in the shot two workers carry the last ladder to a small cart and push the cart away to the left. The closed doors and the stone do "
       "not change. The blue of the sky deepens, and a few thin high clouds drift slowly from the right."))

# ---------- S14 ----------
scene(n=14, fiil="AÇILIR", eleman="kapılar içe açılır · avlu ışığı dışarı taşar · üç kişi + el arabası eşiğe (gerçek zaman) · tutuş", rejim="G", t0="19:20", t1="19:20",
 g="G14", iso=800,
 stage=(LIT + ". " + U(BUILT) + ". " + U(FORECOURT) + ". " + U(BERM) + ", sand drifted against the fences. The doors are "
        "still closed. Three people pushing a loaded two-wheeled hand cart walk across the forecourt from the left towards "
        "the gateway, about five metres from it, small dark figures seen from afar, no readable faces."),
 moment="Twenty past seven in the evening, deep blue hour: the lanterns are lit and three travellers come to the closed gate.",
 comp=C_FACADE + " " + C_GATE + " The three people stand at about 830 pixels from the left, about thirty pixels tall.",
 light=LIGHT("19:20", "blue", "autumn"),
 tr=TR_G,
 act=("The three people pull the loaded hand cart the last five metres towards the closed doors, which are about to "
      "swing back, and stop at the threshold; they stay small dark figures, no readable faces."),
 tex=T_DUSK,
 phys=("The doors are seated on iron pivots set in the threshold stone. The hand cart rests on its two wheels on the paving, and the "
       "three people stand on the paving behind it. The lanterns hang from an iron hook in each arch."),
 mf=("The two heavy timber doors swing open inward from the pointed arch, and warm light from the courtyard pours out "
     "through the gateway onto the forecourt."),
 body=("Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame to about "
       "four seconds the two heavy doors swing slowly open inward, a widening blade of warm light falls out through the "
       "pointed arch and spreads in a long fan across the paving, and the three people push the loaded hand cart the last "
       "five metres to the threshold and stop in the light; from about four to eight seconds nothing else changes — the "
       "doors stand open, the three people stand still on the threshold, the lanterns burn steadily. The people stay "
       "small dark figures, no readable faces. The few thin high clouds stay still in the deep blue sky."))

USTA = dict(g="G15", t="19:20",
 stage=("everything is finished. " + LIT + ". " + U(OPEN) + ". " + U(BUILT) + ". " + U(BERM) + ", sand drifted against "
        "the fences. Three people stand still on the threshold of the open gateway beside a loaded two-wheeled hand cart, "
        "small dark figures against the warm light, no readable faces."),
 moment="Twenty past seven in the evening, deep blue hour, autumn: the caravanserai is open again.",
 comp=C_FACADE + " " + C_GATE + " The three people stand at about 910 pixels from the left, about thirty pixels tall.",
 light=LIGHT("19:20", "blue", "autumn"),
 tr=TR_G,
 act=("The three people stand still on the threshold beside the hand cart, small dark figures with no readable faces; "
      "the lanterns burn steadily and the warm light lies across the forecourt."),
 tex=T_DUSK,
 phys=("The open doors are seated on iron pivots set in the threshold stone. The hand cart rests on its two wheels on the paving, and the "
       "three people stand on the threshold. The lanterns hang from an iron hook in each arch."))

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

def i2v(d):
    return "\n\n".join([I2V_HEAD, "MOTION FOCUS: " + d["mf"], d["body"], LOCK_MAIN, I2V_TAIL])

RJ = {"A": "A (10 dk)", "B": "B (2 sa)", "G": "G (gerçek zaman · 8 sn)"}
def blok(d):
    n = d["n"]; bas, son = n * 8, (n + 1) * 8
    saat = f"{d['t0']}→{d['t1']}" if d["rejim"] != "G" else f"{d['t0']} (+8 sn)"
    out = [f"## 🎬 SAHNE {n} — {d['fiil']}", "",
           "```",
           f"SÜRE: 8,0 s ({bas},0–{son},0)  ·  ELEMAN + ARA HÂL: {d['eleman']}  ·  REJİM: {RJ[d['rejim']]}  ·  SAAT: {saat}  ·  İSTASYON: MAIN",
           "```", "",
           f"### 📸 GÖRSEL PROMPT ({d['g']})", "", "```", gorsel_main(d, HEAD_MAIN.format(n=n)), "```", "",
           f"### 🎥 I2V PROMPT ({d['g']} → G{n+1})", "", "```", i2v(d), "```", "", "---", ""]
    return "\n".join(out)

def usta_blok():
    d = USTA
    return "\n".join([
        "## 🌟 USTA KARE — G15 (SAHNE DEĞİLDİR · son klibin hedefi · kapak kaynağı)", "",
        "> Üretim sırasının İLK karesi [§8]: G15 önce üretilir ve ikna edici değilse DURULUR; sonra",
        "> image-to-image geriye G14 → G13 → … → G0. Kapı: final hiyerarşisi (PLAN) bu sırayla okunuyor mu ·",
        "> açık kapıdan taşan sıcak ışık · 16 yanık fener · kanıt nesnesi akasya x 154–259 / 105 px · vinç, iskele,",
        "> konveyör YOK (SÖKÜM satırı) · mavi saat, güneş −6° · eşikte üç küçük figür. Kapak",
        "> (`THE_BURIED_KHAN_KAPAK.md`) bu promptun kopyası + başlık bandı satırıdır [MUZIK_VE_KAPAK §2.2].", "",
        "### 📸 USTA KARE PROMPT (G15)", "", "```",
        gorsel_main(dict(d, iso=800), HEAD_USTA), "```", ""])

H1 = f"""# 🎬 {FILM} — BÖLÜM 1  (S0 – S7 · G0 … G7 + 8 I2V · 0,0–64,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `{FILM}_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır. STRUCTURE, SITE / BACKGROUND ve NEGATIVE blokları bütün karelerde BİREBİR aynı
> kelimelerle tekrarlanır; değişen AT THIS STAGE, THE TIME MOMENT, COMPOSITION'ın son cümleleri,
> LIGHTING, TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.
>
> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py`)
> ki ortak bloklar harfi harfine aynı kalsın [DERS 20].
>
> ⭐ Bu bölümün SON I2V'si (S7: G7 → G8) **G8 karesinde biter** ve G8 `BOLUM_2`'nin ilk görselidir:
> bölüm sınırı bir KAREDİR, kesme değil [DERS 52]. Kapı KLASÖR MODUNDA koşulur:
> `python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/{FILM}`.
>
> ⛔ Kelime kilitleri: "dune" yalnız G0–G2 ve S0–S2 I2V'lerinde (G3'ten sonra kum "sand" ve "berm"dir);
> "excavator" yalnız G0–G4 ve S0–S4 I2V'lerinde; "crane" yalnız G6–G8 ve S5–S8 I2V'lerinde; "lit" ve
> "glow" yalnız S13 I2V'sinden ve G14'ten sonra; "open inward" yalnız S14 I2V'sinde ve G15'te; YASAK
> KELİME (PLAN künyesi) hiçbir promptta yok — negatifte bile.

---
"""

H2 = f"""# 🎬 {FILM} — BÖLÜM 2  (S8 – S14 · G8 … G14 + 7 I2V · 64,0–120,0 sn) + ⭐ USTA KARE G15

> Bölüm 1 ile aynı kurallar: **yalnız sahne blokları**, her prompt self-contained, STRUCTURE ve
> SITE / BACKGROUND birebir, blok etiketleri birebir [DERS 20].
>
> ⛔ **Bölüm 2 "devamı" değildir, ikinci yarıdır.** "Bölüm 1'deki gibi" atfı yasak; model bu
> dosyayı tek başına okuyor. İLK görsel **G8** bölüm 1'in son I2V'sinin HEDEF karesidir — aynı
> kare, iki dosyada bir kez yazılır (burada); bölüm 1'in S7 I2V'si onu "second provided image" olarak alır.
>
> ⭐ **USTA KARE G15 bu dosyanın sonunda, kendi `## 🌟 USTA KARE` bölümündedir** — sahne
> değildir, son klibin (S14: G14 → G15) hedef karesidir ve kapak kaynağıdır.
>
> ⭐ S14 GERÇEK ZAMANDIR (rejim G · "eight seconds pass"). Son dört saniyesi TUTUŞTUR
> (final kanıtı 116,0–120,0); insan kuralı "no readable faces".

---
"""

if "--tablo" in sys.argv:
    def golge(t):
        az, e = sun(hm(t))
        if e < 0: return "— (güneş ufkun altında)"
        r = ((az + 180 - BEARING) + 180) % 360 - 180
        return f"{r:+d}°"
    for d in S + [USTA]:
        t = d["t"] if "t" in d else d["t0"]
        az, e = sun(hm(t))
        print(d["g"], t, f"{az}°", f"{e:.1f}°".replace(".", ","), golge(t))
    sys.exit(0)

b1 = H1 + "\n" + "\n".join(blok(d) for d in S if d["n"] <= B1_SON)
b2 = H2 + "\n" + "\n".join(blok(d) for d in S if d["n"] > B1_SON) + "\n" + usta_blok()
open(os.path.join(OUT, f"{FILM}_BOLUM_1.md"), "w").write(b1)
open(os.path.join(OUT, f"{FILM}_BOLUM_2.md"), "w").write(b2)
print("yazıldı", len(b1), len(b2))
