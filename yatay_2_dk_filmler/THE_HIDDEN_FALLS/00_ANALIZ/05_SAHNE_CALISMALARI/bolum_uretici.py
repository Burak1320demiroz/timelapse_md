# THE HIDDEN FALLS — bölüm dosyası üretici (ortak bloklar tek kaynaktan, DERS 20)
# KULLANIM (depo kökünden):
#   python3 yatay_2_dk_filmler/THE_HIDDEN_FALLS/00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py yatay_2_dk_filmler/THE_HIDDEN_FALLS
#   → THE_HIDDEN_FALLS_BOLUM_1.md + _BOLUM_2.md yeniden yazılır; ardından prompt_kontrol.py klasör modunda koşulur.
#   --tablo  → PLAN kare tablosu satırlarını basar (saat · azimut · yükseklik · gölge yönü)
# ⛔ ÜRETİM BAŞLADIKTAN SONRA KOŞULMAZ: üretilmiş filmin promptu kanıttır (URETIM_GUNLUGU kuralı).
# ⛔ Bölüm dosyası elle düzeltilirse bu betik o düzeltmeyi EZER — düzeltme önce buraya yazılır.
# Kalıp: yatay_4_dk_filmler/THE_SLOW_TAKEOFF/00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py (07.10.2026)
import math, os, sys

FILM = "THE_HIDDEN_FALLS"
OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
N_SAHNE = 15
B1_SON = 8          # BOLUM_1 = S0–S8 · BOLUM_2 = S9–S14 + USTA (SAPMA ⑩ — sınır G9, ana kare)

# ── güneş (38° K · δ +15° · güneş saati) ───────────────────────────────────
phi, dec = math.radians(38.0), math.radians(15.0)
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
HEAD_MAIN = ("Photorealistic documentary site photograph — Scene {n} of 15. Horizontal 16:9 time-lapse of an abandoned "
             "limestone quarry being rebuilt around a new glass-fronted building; a progress photograph from a fixed "
             "24 mm site camera.")
HEAD_USTA = ("Photorealistic documentary site photograph — master frame G15, the target frame of the last shot "
             "(Scene 14 of 15). Horizontal 16:9 time-lapse of an abandoned limestone quarry rebuilt around a new "
             "glass-fronted building; a progress photograph from a fixed 24 mm site camera.")
HEAD_SALON = ("Photorealistic documentary interior photograph — Scene {n} of 15. Horizontal 16:9 time-lapse inside the "
              "double-height glass salon of a new building at the foot of a limestone quarry wall; a progress "
              "photograph from a fixed 24 mm camera inside the salon.")
HEAD_SALON_SON = ("Photorealistic documentary interior photograph — the last frame of Scene {n} of 15. Horizontal 16:9 "
                  "time-lapse inside the double-height glass salon of a new building at the foot of a limestone quarry "
                  "wall; a progress photograph from a fixed 24 mm camera inside the salon.")
CAM_MAIN = ("Camera: MAIN STATION — fixed tripod bolted to the rock of a narrow bench high on the south wall of the "
            "quarry, lens 16 metres above the basin floor, 110 metres from the foot of the far wall along the lens "
            "axis, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves.")
CAM_SALON = ("Camera: SALON STATION — fixed clamp mount bolted to the rock face at the back of the double-height glass "
             "salon, lens 12 metres above the basin floor, 10 metres from the glass front, bearing 180 degrees, tilt 0 "
             "degrees, zero roll. The camera never moves.")
STRUCT = ("STRUCTURE: When finished this will be a long two-storey building with a full-height glass front, 45 metres "
          "wide, standing on a raised concrete base against the foot of the far quarry wall, with a double-height glass "
          "salon at its right end, a timber terrace along its front and a steel footbridge to the entrance terrace.")
# ⭐ İki SITE bloğu iki cümleyi BİREBİR paylaşır (ortak çapa — ISTASYON_VE_IC_MEKAN §0 ② · DERS 10):
ORTAK_DUVAR = "The quarry walls are pale grey limestone cut in tall vertical faces and narrow horizontal benches."
ORTAK_SUTUN = ("A lone squat pillar of pale grey limestone stands in the middle of the quarry basin, its top about "
               "eleven metres above the basin floor.")
SITE_MAIN = ("SITE / BACKGROUND: A deep abandoned limestone quarry seen from a narrow bench high on its south wall, "
             "looking north across the basin. " + ORTAK_DUVAR + " The far wall rises sheer across the back of the frame "
             "to a dead level rim, with one narrow upper bench six metres below the rim and one dark rust-stained crack "
             "running diagonally down its face left of centre. The west wall closes the left side and the east wall the "
             "right side. An old haul road ramps down the west wall to a broad flat entrance terrace in the far left "
             "corner. One tall lone umbrella pine stands on the west rim at the top left; one small roofless ruined stone "
             "hut stands on the east rim at the top right. " + ORTAK_SUTUN)
SITE_SALON = ("SITE / BACKGROUND: The double-height glass salon at the right end of a new building at the foot of the "
              "far wall of a deep limestone quarry, seen from its back wall looking south through its tall glass front. "
              "The glass front is one wall of tall clear panes between slim dark steel mullions, from the floor to the "
              "ceiling, filling the whole width of the frame from about a third of its height up to the top edge. "
              "Through the glass the quarry basin opens out towards the south wall. " + ORTAK_DUVAR + " " + ORTAK_SUTUN)
NEG_MAIN = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The quarry walls, the far rim, the dark "
            "diagonal crack, the umbrella pine, the ruined stone hut, the haul road, the entrance terrace and the "
            "limestone pillar never change shape, position, size or spacing. The quarry holds exactly one building "
            "site, this one, at the foot of the far wall; nothing already built is removed or resized; no opacity "
            "fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. "
            "Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no "
            "fades. No architectural visualisation look, no CGI aesthetic.")
NEG_SALON = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The glass front, its slim steel "
             "mullions, the limestone pillar and the quarry walls seen through the glass never change shape, position, "
             "size or spacing. Nothing already built is removed or resized; no opacity fades. No readable text, "
             "letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been "
             "branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural "
             "visualisation look, no CGI aesthetic.")
OUTPUT = "Output: 16:9, 4K, no text, no watermark."
CREW = "Crew register only as faint soft motion streaks beside their machines, never as sharp figures."
FILMSTOCK = "A documentary site photograph on colour negative film, true colour, fine grain."
FILMSTOCK_IN = "A documentary interior photograph on colour negative film, true colour, fine grain."

COMP_HEAD = ("COMPOSITION: Horizontal 16:9. The camera is level; the far rim runs dead level at about seventy percent "
             "of frame height. The limestone pillar at the centre spans about 130 pixels of frame width — about one "
             "fifteenth — from about 920 to 1050 pixels from the left, its top at about thirty-eight percent of frame "
             "height, and keeps that width and position in every frame. ")
C_FOOT = ("The foot of the far wall, where the work happens, runs across the middle of the frame at about forty percent "
          "of frame height.")
C_BASE = ("The raised base runs along the foot of the far wall from about 750 to 1390 pixels from the left, its top at "
          "about forty-three percent of frame height.")
C_BLDG = ("The building spans from about 750 to 1340 pixels from the left, from its base at about forty-three percent "
          "of frame height to its roof at about fifty-three percent, far below the rim.")
C_BRIDGE = "The footbridge crosses from about 300 to 750 pixels from the left at about forty-three percent of frame height."
C_WATER = "The turquoise water reaches up to about thirty-nine percent of frame height at the foot of the far wall."
C_FALL = ("The waterfall falls from the roof edge at about fifty-three percent down to the water at about thirty-nine "
          "percent of frame height, from about 1210 to 1350 pixels from the left, in front of the right end of the "
          "building.")
COMP_TAIL = ("The working level sits above the bottom quarter; nothing that proves progress falls into the bottom tenth "
             "or the top-right corner of the frame.")
COMP_SALON = ("COMPOSITION: Horizontal 16:9. The camera is level: the horizon sits at exactly half the frame height. The "
              "tall glass front fills the whole width of the frame from about a third of its height up to the top edge, "
              "its slim dark mullions standing upright and evenly spaced, and keeps that position in every frame; the "
              "floor and the furniture fill the lower third. Through the glass the limestone pillar stands at about "
              "three quarters of the frame width, from about 1350 to 1460 pixels from the left, its top just below half "
              "the frame height; the pillar spans about 110 pixels of frame width — about one seventeenth — and keeps "
              "that width. Nothing that proves progress falls into the bottom tenth or the top-right corner of the frame.")

TR_A = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, "
        "vehicles and crew all move at the same accelerated speed. Ten minutes pass across this shot: the shadows stay "
        "almost where they are, the clouds drift in one smooth flow, and machines and vehicles move fast but stay "
        "recognisable, trailing light motion blur. Nothing moves at normal speed.")
TR_B = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines, "
        "vehicles and crew all move at the same accelerated speed. Two hours pass across this shot: the shadows swing "
        "slowly round, the clouds streak across the sky, and machines smear into heavy motion blur. Nothing moves at "
        "normal speed.")
TR_G = ("TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the water "
        "runs, falls and ripples at its real pace; nothing is accelerated.")
TR_A_IN = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: the light outside, the clouds, the "
           "band of sunlight on the floor and the crew inside all move at the same accelerated speed. Ten minutes pass "
           "across this shot: the light shifts only a little, the clouds drift in one smooth flow, and the crew trail "
           "light motion blur. Nothing moves at normal speed.")
TR_G_IN = ("TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the "
           "falling water outside the glass, the ripples on the water beyond and the lamplight inside move at their "
           "real pace; nothing is accelerated.")

I2V_HEAD = ("The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its "
            "last frame is that image, matched frame for frame — same framing, same light, same objects in the same "
            "places.")
LOCK_MAIN = ("The camera does not move at any point. The framing is identical in the first and last frame. The quarry "
             "walls, the far rim, the dark diagonal crack, the umbrella pine, the ruined stone hut, the haul road, the "
             "entrance terrace and the limestone pillar stay exactly where they are, at exactly the same size and "
             "shape, for the whole shot; the limestone pillar occupies exactly the same width of the frame in the first "
             "and last frame, and the far rim stays dead level at the same height. The quarry holds exactly one "
             "building site. Nothing already built is removed or resized.")
LOCK_SALON = ("The camera does not move at any point. The framing is identical in the first and last frame. The glass "
              "front, its slim steel mullions, the limestone pillar and the quarry walls seen through the glass stay "
              "exactly where they are, at exactly the same size and shape, for the whole shot; the mullions stand in "
              "exactly the same places in the first and last frame, and the horizon stays at exactly half the frame height. "
              "Nothing already built is removed or resized.")
I2V_TAIL = ("Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
            "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
            "documentary time-lapse cinematography.")
I2V_TAIL_SALON = ("Camera: fixed clamp mount, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
                  "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
                  "documentary time-lapse cinematography.")

# ── tekrarlanan durum cümleleri (aynı nesne her karede aynı kelimelerle) ─────
BASE = ("a long raised concrete base, about four metres high and fifty metres wide, along the foot of the far "
        "wall from just left of centre to well right of centre")
PIER = "one slim square concrete pier stands on the middle bench to the left of the base"
FRAME = ("the dark grey steel frame of the building stands on the raised base against the far wall: two storeys of "
         "slim steel, forty-five metres wide and about eight and a half metres high, its right end open to a double "
         "height for the salon")
BRIDGE = ("the steel footbridge — two dark grey spans with open railings, its deck about ten metres above the basin "
          "floor — runs from the entrance terrace over the slim pier to the left end of the raised base")
TERRACE = ("a pale timber terrace with a slim steel railing covers the base in front of the left part of the building; "
           "in front of the salon the base stops at the glass line")
ROOF = "the flat roof is closed, and over the salon it ends in a straight steel lip two metres out beyond the glass line"
GLASS = ("the whole front is glazed — tall clear panes between slim dark steel mullions on both storeys of the left "
         "part and over the full double height of the salon — reflecting the pale quarry walls and the sky")
BUILT = ("the finished building stands on its raised base against the far wall — its full-height glass front between "
         "slim dark steel mullions, the double-height salon at its right end under a straight steel roof lip, a pale "
         "timber terrace with a slim railing along the left part — and the steel footbridge on its slim pier links the "
         "terrace to the entrance terrace")
CHANNEL = ("a narrow concrete channel runs along the upper bench of the far wall to a short notch above the salon, and "
           "a dark steel pipe climbs the rock beside the building from a small pump house on the base to the channel")
GARDEN = ("young shrubs and trailing plants line the three narrow benches of the east wall, three young olive trees "
          "stand round the end of the footbridge on the entrance terrace, and ferns line the channel")
DRY = ("the basin below is dry — grey rock benches, silt and puddles, a pale scum line round the walls, the pillar "
       "on the dry basin floor")
FULL = ("the basin is full of calm clear water, pale turquoise over the drowned benches and blue-green over the deep "
        "floor, three metres below the raised base and the footbridge deck, lapping the pillar four metres below its top")
FALL = ("the waterfall runs: a bright sheet of water slides down the rock face from the notch onto the salon roof and "
        "falls from its steel lip as a wide thin curtain two metres in front of the right part of the salon glass into "
        "the turquoise water, white foam at its foot; the left part of the salon glass stays clear")
GARDEN_S = ("young planting greens the benches of the east wall and three olive trees stand round the end of the "
            "footbridge")
FALL_S = ("the waterfall runs from the notch down the rock face onto the salon roof and falls from its steel lip as a "
          "wide thin curtain two metres in front of the right part of the salon glass, white foam at its foot")
LIT = ("all the lights are on: the salon glows warm behind the falling water, both storeys of the glass front glow, and "
       "small lamps on the railings and among the plants throw long warm reflections across the water")
BUILT_S = ("the finished building stands on its raised base against the far wall — its full-height glass front, the "
           "double-height salon at its right end and the pale timber terrace — and the steel footbridge on its slim pier "
           "links it to the entrance terrace")
FULL_S = "the basin is full of calm turquoise water, three metres below the raised base and the footbridge deck"
def U(x): return x[0].upper() + x[1:]

# ── doku ────────────────────────────────────────────────────────────────────
T_OLD = ("Pale grey limestone with dark rain streaks and orange rust stains below old bolts, murky green-brown water "
         "with a pale scum line and floating debris, rubble heaps and weeds on the benches, rusty cable coils, fresh "
         "tyre tracks in the dust of the entrance terrace. " + FILMSTOCK)
T_DRY = ("Wet grey limestone and dark silt drying in pale patches, a pale scum line printed round the walls, puddles "
         "reflecting the sky, rubble heaps and tyre ruts on the benches, fresh grey concrete with timber formwork "
         "edges. " + FILMSTOCK)
T_BUILD = ("Dark grey steel with rust-brown streaks at the joints, fresh grey concrete with formwork edges, pale new "
           "timber with sawdust, dry grey silt and tyre ruts across the basin floor, a pale scum line round the walls, "
           "packing crates and offcuts in a skip on the entrance terrace. " + FILMSTOCK)
T_GARDEN = ("Freshly turned dark soil along the benches, young green shrubs and trailing plants, bark mulch, dry grey "
            "silt across the basin floor, pale timber with a few soil stains, tyre ruts on the entrance terrace. "
            + FILMSTOCK)
T_WATER = ("Calm clear turquoise water with a soft sheen over pale submerged rock, a thin pale band of wet rock just above "
           "the new waterline, drowned silt patches showing pale under the shallows, dark wet streaks where water runs down the "
           "rock, tyre tracks drying in the dust of the entrance terrace, young planting on the benches. " + FILMSTOCK)
T_DUSK = ("Deep teal water with a soft sheen, warm reflections breaking into streaks, a band of white foam and drifting "
          "spray at the foot of the fall, a wet dark stain down the rock below the notch, a thin pale band of wet rock above the "
          "waterline, damp patches on the terrace. " + FILMSTOCK)

# ── ışık ────────────────────────────────────────────────────────────────────
LIGHT_DESC = {
 "dawn": ("low on the right beyond the east rim, so the basin and the far wall lie in cool blue shade and only the "
          "upper west wall and the umbrella pine catch warm early light; long shadows fall to the left."),
 "am": ("on the right, a little behind the camera, raking the far wall from the right; the shadow of the east wall "
        "still lies across the right part of the basin, and shadows fall to the left."),
 "late_am": ("high on the right behind the camera, lighting the far wall from the right, with short shadows falling to "
             "the left and away from the camera."),
 "noon": ("high on the left behind the camera, lighting the far wall and everything at its foot evenly, with short "
          "shadows falling to the right and away from the camera."),
 "pm": ("on the left behind the camera, raking the far wall from the left and lighting the east wall warm; the shadow "
        "of the west wall lies across the left part of the basin, and shadows fall to the right."),
 "low": ("low on the left beyond the west rim, so the shadow of the west wall lies across most of the basin while "
         "its right part and the upper east wall glow warm gold; long shadows fall to the right."),
 "blue": ("below the horizon on the left, outside the frame, so there is no direct sun: deep blue hour, the sky deep "
          "clear blue with a last pale band low over the left rim, the rock walls cool blue-grey."),
 "in_noon": ("high ahead of the camera in the south, above the top of the frame, so a band of bright sunlight falls "
             "through the glass onto the floor just inside the front and the room is lit softly by the bright day "
             "outside; the view through the panes is bright and the room is in softer light."),
 "in_blue": ("below the horizon outside, so there is no direct sun: deep blue hour outside the glass, and the room is "
             "lit warm by its own lamps, the warm light catching the falling water just outside the panes."),
}
SEASON = {
 "spring0": "Early spring: a clear pale sky with a few small high clouds, the grass along the rims fresh green with a scatter of yellow flowers.",
 "summer0": "Early summer: a clear blue sky with small white fair-weather clouds, the grass along the rims turning green-gold.",
 "summer": "High summer: a hazy pale blue sky, the grass along the rims dry and straw-gold.",
 "late": "Late summer: a hazy sky with a few high clouds, the grass along the rims straw-gold.",
 "autumn": "Autumn after the first rains: a soft blue sky with scattered white clouds, dark wet streaks down the rock faces, the grass along the rims greening again at its roots.",
 "spring": "Spring: a clear sky with a few small clouds, the grass along the rims green, the new planting leafing out.",
 "summer1": "Early summer: a clear sky with a few high thin clouds, the grass along the rims green-gold, the new planting in full leaf.",
}
def LIGHT(t, key, season):
    return f"LIGHTING: {sunline(t)}, {LIGHT_DESC[key]} {SEASON[season]} The sun stays outside the frame."

# ── sahne verisi ─────────────────────────────────────────────────────────────
# kare alanları: g, t (kare saati), st (M/S), stage, moment, comp, light, tr (bu karenin başlattığı klibin hızı),
#                act, tex, phys · klip alanları: n, fiil, eleman, rejim, t0, t1, mf, body, nxt (hedef kare)
S = []
def scene(**k): S.append(k)

# ---------- S0 ----------
scene(n=0, fiil="KALDIRIR", eleman="paslı yükleme platformu dipte → vinçte → kamyonda (%100)", rejim="A", t0="06:30", t1="06:40",
 st="M", g="G0",
 stage=("nothing has been built yet. The basin holds a shallow sheet of murky green-brown water about three metres "
        "deep, with floating debris and a pale scum line round its edges; the broad bench at the foot of the far wall "
        "and the middle bench in front of it stand just above the water as bare grey rock with rubble and weeds. At the "
        "middle of the foot of the far wall a rusty steel loading hopper on four tall legs has just been lifted clear of "
        "its old concrete footings and hangs from the hook of a yellow crawler crane with a long lattice boom, which "
        "stands on the entrance terrace; a flatbed truck waits beside it. Rusty cable and broken conveyor rollers lie on "
        "the benches."),
 moment="Half past six in the morning on the first day of work: the old hopper has just come off its footings and hangs a metre above them.",
 comp=C_FOOT + " The rusty hopper hangs at the foot of the far wall at about the middle of the frame width.",
 light=LIGHT("06:30", "dawn", "spring0"),
 tr=TR_A,
 act=("The crawler crane swings the rusty hopper away from its footings towards the entrance terrace while two "
      "workers on the bench steady it with taglines, and a small excavator scrapes rubble along the foot bench; the "
      "crane carries a visible load, with a heavy rusty hopper slung on the hook. " + CREW),
 tex=T_OLD,
 phys=("The hopper hangs from the crane hook on four taut slings. The crawler crane stands on its tracks on the "
       "entrance terrace, its counterweight resting at the back. The limestone pillar stands on the basin floor, the "
       "murky water round its lower quarter, and the excavator sits on its tracks on the foot bench."),
 mf=("The crawler crane swings the rusty loading hopper from the foot of the far wall across the basin to the entrance "
     "terrace and lowers it onto the bed of the flatbed truck."),
 body=("Ten minutes pass in the early light. Everything in this shot is time-lapsed at the same rate. From the first "
       "frame the hopper is already moving: it swings slowly away from its four old footings on the crane hook, "
       "steadied by two taglines, travels across above the murky water and settles onto the bed of the flatbed truck, "
       "where the slings go slack. The excavator pushes a heap of rubble along the foot bench. The murky water, the "
       "pillar and the far wall do not change. The warm light on the upper west wall slides a little lower, long "
       "shadows lean to the left, and a few small high clouds drift slowly from the left in one smooth flow."))

# ---------- S1 ----------
scene(n=1, fiil="BOŞALTIR", eleman="kirli su +3 m → taban (su birikintisi) · basamaklı taban %0 → %100 görünür", rejim="B", t0="06:40", t1="08:40",
 st="M", g="G1",
 stage=("the old hopper has been carried off and sits on the bed of the flatbed truck beside the yellow crawler crane "
        "on the entrance terrace, with a heavy hopper on the hook resting on the truck bed on slack slings; at the foot of the far wall only its four "
        "broken concrete footings remain. The basin still holds the shallow sheet of murky green-brown water, about "
        "three metres deep, with floating debris and a pale scum line round its edges. Two diesel pumps stand on the "
        "middle bench at the water's edge with fat black hoses laid into the water, and a long discharge hose runs from "
        "them up the haul road."),
 moment="Twenty to seven in the morning: the hopper is on the truck and the pumps are about to start.",
 comp=C_FOOT + " The two pumps sit on the middle bench a little left of the pillar.",
 light=LIGHT("06:40", "dawn", "spring0"),
 tr=TR_B,
 act=("The two diesel pumps pull the murky water out through their hoses, the waterline drops and a widening band of "
      "wet grey rock and silt appears round the basin, and the flatbed truck carries the hopper up the haul road. " + CREW),
 tex=T_OLD,
 phys=("The pumps sit on their skids on the middle bench, their suction hoses resting in the water. The hopper stands on "
       "its four legs on the truck bed, the slack slings still on the crane hook. The limestone pillar stands on the "
       "basin floor with the murky water round its foot."),
 mf=("The two pumps drain the murky water from the basin through their hoses up the haul road to the rim, until only "
     "puddles remain and the stepped floor of the quarry appears."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The waterline sinks steadily: first "
       "the middle bench comes clear, then the slope below it, then the basin floor, until only scattered puddles and "
       "dark silt remain round the foot of the limestone pillar. A pale scum line stays printed on the rock where the "
       "water stood. Early in the shot the crane hook lifts free and the flatbed truck carries the hopper up the haul "
       "road and out of the frame on the left. The shadow of the east wall shrinks back across the basin to the right "
       "as the sun climbs, and small clouds streak across the strip of sky."))

# ---------- S2 ----------
scene(n=2, fiil="DÖKER", eleman="yükseltilmiş beton temel 0 → %100 · köprü ayağı 0 → 1", rejim="B", t0="08:40", t1="10:40",
 st="M", g="G2",
 stage=("the basin has been pumped dry: the stepped floor lies bare — the broad foot bench along the far wall, the "
        "middle bench below it and the lowest basin floor — wet grey rock and dark silt with scattered puddles, a pale "
        "scum line printed round the walls three metres above the floor. The limestone pillar stands on wet silt. The "
        "two pumps lie coiled on the middle bench. The yellow crawler crane stands on the entrance terrace, with a "
        "bundle of rebar cages on the hook; a yellow excavator and a small dumper work on the foot bench, where stakes with "
        "orange tape mark a long rectangle along the foot of the far wall and one small square on the middle bench to "
        "its left. A concrete pump truck waits on the entrance terrace."),
 moment="Twenty to nine in the morning: the quarry floor is bare for the first time and the base is staked out.",
 comp=C_FOOT + " The staked rectangle runs from about 750 to 1390 pixels from the left.",
 light=LIGHT("08:40", "am", "spring0"),
 tr=TR_B,
 act=("The excavator scrapes silt and rubble off the foot bench into the dumper, which shuttles it up the haul road; "
      "the crew raises timber formwork round the staked rectangle and the crane swings the rebar cages into it. " + CREW),
 tex=T_DRY,
 phys=("The rebar cages hang from the crane hook in a bundle on two slings. The excavator and the dumper stand on their "
       "tracks and wheels on the foot bench. The limestone pillar stands on the dry basin floor, and the formwork is "
       "braced against the rock."),
 mf=("The crew builds the raised concrete base in the staked rectangle along the foot of the far wall — formwork, rebar "
     "cages lowered from the crane hook into it, then grey concrete pumped from the long boom of the pump truck onto it, "
     "left end first — and casts one slim square pier on the middle bench to its left the same way."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The excavator and the dumper clear "
       "the foot bench; timber formwork rises round the rectangle, the crane lowers rebar cages from the bundle into "
       "it, and the pump boom swings over it and fills it with grey concrete from the left end to the right, until a "
       "long flat base about four metres high stands along the foot of the far wall with rows of anchor bolts on top. "
       "On the middle bench a slim square pier rises the same way. The puddles shrink and the silt dries in pale "
       "patches. The shadows shorten as the sun climbs on the right, and small clouds streak across the sky."))

# ---------- S3 ----------
scene(n=3, fiil="DİKER", eleman="çelik iskelet 0 → %100 (iki kat · sağ uç çift yükseklik)", rejim="A", t0="10:40", t1="10:50",
 st="M", g="G3",
 stage=(U(BASE) + " stands finished, its flat top level, rows of anchor bolts standing out of it; " + PIER + ". " + U(DRY) +
        ". The yellow crawler crane on the entrance terrace has a bundle of dark grey steel members on its hook, and "
        "two long trucks loaded with more steel wait beside it; the formwork timber lies stacked on the foot bench."),
 moment="Twenty to eleven in the morning: the base is finished and the first steel goes up.",
 comp=C_BASE,
 light=LIGHT("10:40", "late_am", "summer0"),
 tr=TR_A,
 act=("The crane lifts the dark grey steel members from the trucks and swings them across the basin onto the raised base, "
      "where the crew bolts them up from the left; the crane carries a visible load, with steel slung on the hook. " + CREW),
 tex=T_BUILD,
 phys=("The base sits on the foot bench against the rock. The crawler crane stands on its tracks on the entrance "
       "terrace, its long boom reaching out over the basin, the steel bundle hanging from its hook on two slings. The "
       "first steel members stand bolted to the anchor bolts of the base."),
 mf=("The crawler crane lifts dark grey steel members from the trucks onto the raised base, and the crew bolts them up "
     "into the two-storey steel frame of the building against the rock, from left to right, leaving the right end open "
     "to a double height."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first "
       "member is already swinging across on the crane hook. The crane lifts each piece from the truck beds; the frame "
       "stands up on the base piece by piece from the left and grows across to the right, where the last bay stays "
       "open to a double height. The crane lifts the stacked formwork timber onto an empty truck, and the trucks drive "
       "up the haul road. The pillar and the dry basin do not change. Short shadows lean to the left, and small white "
       "clouds drift slowly from the left."))

# ---------- S4 ----------
scene(n=4, fiil="YERLEŞTİRİR", eleman="köprü açıklığı 0 → 2 (terastan ayağa, ayaktan temele)", rejim="A", t0="10:50", t1="11:00",
 st="M", g="G4",
 stage=(U(FRAME) + "; its top beams bear against the rock. " + PIER + ". " + U(DRY) + ". The crane hook hangs over a "
        "stack of two finished steel footbridge spans, each about sixteen metres long, lying on timber bearers on the "
        "entrance terrace, a lifting beam already shackled to the top one."),
 moment="Ten to eleven in the morning: the steel frame stands complete and the two bridge spans wait on the terrace.",
 comp=C_BLDG,
 light=LIGHT("10:50", "late_am", "summer0"),
 tr=TR_A,
 act=("The crawler crane lifts the first footbridge span from the stack and swings it out over the basin while two "
      "workers on the pier and two on the terrace edge guide it with taglines; the crane carries a visible load, with a "
      "long steel span slung on the hook. " + CREW),
 tex=T_BUILD,
 phys=("The steel frame stands bolted to the base, its top beams bearing against the rock. The spans rest on timber "
       "bearers on the terrace, the lifting beam hanging from the crane hook on four slings. The slim pier stands on its "
       "footing on the middle bench."),
 mf=("The crawler crane lifts the first footbridge span from the stack on the entrance terrace and lowers it onto the "
     "terrace edge and the slim pier, then lifts the second span from the stack and lowers it onto the pier and the left "
     "end of the raised base."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first span "
       "is already rising from the stack. It swings out over the dry basin, level, and settles with one end on the "
       "terrace edge and the other on the pier; the hook goes back, lifts the second span from the stack and sets it "
       "between the pier and the left end of the base. The crew bolts the joints. Two spans, one bridge: no other span is "
       "lifted. The frame, the pillar and the far wall do not change. Short shadows lean to the left, and small white "
       "clouds drift slowly from the left."))

# ---------- S5 ----------
scene(n=5, fiil="KAPLAR", eleman="ahşap teras %0 → %100 (soldan sağa) · çatı kapanır · istif → 0", rejim="B", t0="11:00", t1="13:00",
 st="M", g="G5",
 stage=(U(BRIDGE) + ". " + U(FRAME) + ". " + U(DRY) + ". Stacks of pale timber decking boards and bundles of dark grey "
        "roof panels wait on the raised base in front of the frame, and the crawler crane has a pallet of boards on its hook."),
 moment="Eleven in the morning: the footbridge is in place and the boards are stacked on the base.",
 comp=C_BLDG + " " + C_BRIDGE,
 light=LIGHT("11:00", "late_am", "summer0"),
 tr=TR_B,
 act=("The crew lifts the pale boards from the stacks and lays them across the front of the base from left to right "
      "while a second crew on top of the frame lays dark roof panels; the crane carries a visible load, with a pallet of "
      "boards slung on the hook. " + CREW),
 tex=T_BUILD,
 phys=("The decking boards rest on timber joists bolted to the top of the base. The roof panels rest on the top beams of "
       "the frame. The footbridge spans rest on the terrace edge, the pier and the base, and the pallet hangs from the "
       "crane hook on four slings."),
 mf=("The crew carries pale timber boards from the stacks onto the front of the raised base and lays a terrace before "
     "the left part of the building, from left to right, with a slim steel railing along its edge, while a second crew "
     "lays dark grey panels from the bundles onto the top of the frame and closes the flat roof, ending over the salon in "
     "a straight steel lip; the stacks shrink to nothing."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Pale boards spread across the front "
       "of the base from the left, plank by plank, and a slim railing follows along the edge until a broad timber "
       "terrace lies before the left part of the building; before the salon the base stops at the frame. On top of the "
       "frame the dark panels close the roof from the left, and over the salon its edge ends in a straight steel lip. "
       "The crew carries the last boards from the stacks, which shrink and vanish onto the terrace and the roof. The "
       "shadows swing from the left round to the right as the sun passes behind the camera, and white clouds streak "
       "across the sky."))

# ---------- S6 ----------
scene(n=6, fiil="CAMLAR", eleman="cam cephe %0 → %100 (sağdan sola: önce salon) · yansıma belirir", rejim="A", t0="13:00", t1="13:10",
 st="M", g="G6", nxt="G8",
 stage=(U(TERRACE) + ". " + U(ROOF) + "; the steel frame below it stands open and unglazed. " + U(BRIDGE) + ". " + U(DRY) + ". On the "
        "entrance terrace two trucks loaded with tall crates of glass panes wait beside the crawler crane, which holds the "
        "first tall pane on a vacuum lifting frame on its hook."),
 moment="One in the afternoon: the terrace and the roof are finished, and the first glass pane is on the hook.",
 comp=C_BLDG + " " + C_BRIDGE,
 light=LIGHT("13:00", "noon", "summer"),
 tr=TR_A,
 act=("The crane lifts the tall glass panes one by one from the crates and swings them to the front of the building, where "
      "the crew sets them between the steel posts; the crane carries a visible load, with a tall pane on the hook. " + CREW),
 tex=T_BUILD,
 phys=("Each glass pane hangs flat from the vacuum frame on the crane hook. The terrace boards rest on joists bolted to "
       "the base. The roof and its steel lip rest on the frame, which stands bolted to the base."),
 mf=("The crawler crane lifts the tall glass panes one by one from the crates on the trucks and swings them to the front "
     "of the building, where the crew sets them between slim steel mullions — first the double-height salon at the right "
     "end, then both storeys of the left part, from right to left — until the whole front is glazed."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first pane "
       "is already swinging across on the hook. Pane after pane goes in, first over the full height of the salon, then "
       "along both storeys of the left part towards the footbridge, and each one catches the reflection of the pale "
       "walls and the sky as it goes in. The crane lifts the last panes from the crates, and the trucks drive away. The "
       "terrace, the roof, the footbridge and the dry basin do not change. Short shadows lean to the right, and a few "
       "hazy clouds drift slowly from the left."))

# ---------- S7 (SALON · ∥ S8 — SAPMA ④) ----------
scene(n=7, fiil="DÖŞER", eleman="salon: boş → uzun masa + 12 sandalye + oturma grubu (%100)", rejim="A", t0="13:10", t1="13:20",
 st="S", g="G7", nxt="G7′",
 stage=("the salon is glazed and floored but empty: pale oak floorboards and the tall glass front between slim dark "
        "steel mullions over the full double height. A pile of wrapped furniture and a long timber table top stand by the "
        "side door at the left edge of the frame, and nothing else stands in the room. Through the glass the basin below "
        "is dry: grey rock benches, silt and puddles, the limestone pillar standing on the dry floor, and beyond it the "
        "pale south wall of the quarry."),
 moment="Ten past one in the afternoon: the salon has its glass and its floor, and the furniture waits by the door.",
 light=("LIGHTING: " + sunline("13:10") + ", " + LIGHT_DESC["in_noon"] + " " + SEASON["summer"] + " The sun stays outside the frame."),
 tr=TR_A_IN,
 act=("Two workers carry the long table top from the pile to the middle of the floor and set the table top on its legs, then carry "
      "the chairs one by one to both sides of it and bring a low sofa and two armchairs to the glass at the right. The "
      "workers register only as faint soft motion streaks."),
 tex=("Fresh pale oak floorboards with sawdust in the joints, a faint dust film and a few smudges on the new panes, "
      "plastic wrapping and cardboard in a heap by the side door, a bright band of sunlight across the floor, a patch of "
      "glare on the glass, a few scuffed shoe prints on the floor. " + FILMSTOCK_IN),
 phys=("The wrapped furniture rests on the floorboards by the door. The glass panes stand clamped in their mullions on "
       "the floor edge. Outside, the limestone pillar stands on the dry basin floor."),
 mf=("Two workers carry the long timber table top and the chairs from the wrapped pile by the side door to the middle of "
     "the floor and set them out parallel to the glass, then bring a low sofa and two armchairs from the pile to the glass "
     "at the right."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The table top crosses the room and "
       "comes to rest on its legs in the middle of the floor; the workers carry chair after chair from the pile and set "
       "them along both sides, twelve in all; the sofa and the two armchairs are carried to the glass at the right and "
       "turned to face out over the quarry. The heap of wrapping grows by the door and the furniture pile is gone. The "
       "band of sunlight on the floor shifts slightly, and through the glass small clouds drift slowly across the sky "
       "over the south wall; the dry basin and the pillar do not change."))

# ---------- S8 ----------
scene(n=8, fiil="YOLLAR", eleman="üst basamak kanalı %0 → %100 · boru pompa evinden kanala · vinç gider", rejim="A", t0="13:10", t1="13:20",
 st="M", g="G8",
 stage=(U(BUILT) + ". " + U(DRY) + ". On the upper bench of the "
        "far wall a crew has begun a narrow concrete channel along the bench edge above the middle of the building, and a "
        "small concrete pump house stands on the base beside its right end with the first sections of a dark steel pipe "
        "fixed to the rock above it. The crawler crane has a bundle of pipe sections on its hook."),
 moment="Ten past one in the afternoon: the glass front is finished and the work moves up the far wall.",
 comp=C_BLDG + " " + C_BRIDGE + " The upper bench sits at about sixty-five percent of frame height.",
 light=LIGHT("13:10", "noon", "summer"),
 tr=TR_A,
 act=("A crew on the upper bench casts the channel along the bench edge, a second crew on ropes bolts pipe sections up "
      "the rock face, and the crane lifts the last sections to them; the crane carries a visible load, with a bundle of "
      "pipe slung on the hook. " + CREW),
 tex=T_BUILD,
 phys=("The channel sits on the rock of the upper bench. The pipe is clamped to the rock face with steel brackets, and "
       "the pipe bundle hangs from the crane hook on two slings. The pump house stands on the raised base."),
 mf=("A crew casts the narrow concrete channel along the edge of the upper bench from above the middle of the building "
     "to above its right end, a second crew bolts the dark steel pipe up the rock face from the pump house to the end of "
     "the channel, and then the crawler crane lowers its long boom and is driven away up the haul road."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The grey line of the channel grows "
       "to the right along the edge of the upper bench and ends at a short notch above the salon, over the bare rock "
       "face that drops to its roof; the crane lifts pipe sections from the bundle to the rope crew, and the dark pipe "
       "climbs the rock beside the building to the end of the channel. In the second half of the shot the crawler crane "
       "lowers and folds its boom and crawls up the haul road and out of the frame on the left. The glazed building, the "
       "footbridge and the dry basin do not change. Short shadows lean to the right, and a few hazy clouds drift slowly "
       "from the left."))

# ---------- S9 ----------
scene(n=9, fiil="DİKER ②", eleman="bahçe: doğu basamakları 0 → 3 sıra · zeytin 0 → 3 · eğreltiotu", rejim="B", t0="13:20", t1="15:20",
 st="M", g="G9",
 stage=(U(CHANNEL) + "; the channel is dry. " + U(BUILT) + ". " + U(DRY) + ". The entrance terrace is clear of machines; "
        "pallets of young shrubs, three small olive trees with wrapped root balls and bags of soil wait on it beside a "
        "small truck."),
 moment="Twenty past one in the afternoon: the building is finished and the plants have arrived.",
 comp=C_BLDG + " " + C_BRIDGE,
 light=LIGHT("13:20", "noon", "late"),
 tr=TR_B,
 act=("Crews carry young shrubs and trailing plants from the pallets along the narrow benches of the east wall and plant "
      "them in rows, and a small excavator digs three planting pits on the entrance terrace and lifts the first olive tree into one. " + CREW),
 tex=T_GARDEN,
 phys=("The plants stand in their pots on the pallets on the entrance terrace. The building stands bolted to its base "
       "against the rock, and the footbridge rests on its pier. The limestone pillar stands on the dry basin floor."),
 mf=("Crews carry young shrubs and trailing plants from the pallets on the entrance terrace onto the three narrow benches "
     "of the east wall and plant them in rows, bench by bench from the lowest up, then plant the three olive trees round "
     "the end of the footbridge and a line of ferns along the channel."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Green rows spread along the narrow "
       "benches of the east wall, one bench after another from the lowest up, until the grey wall is striped with young "
       "planting; three young olive trees stand up round the end of the footbridge; a thin green line of ferns runs "
       "along the channel on the upper bench. The crews carry the last plants from the pallets, and the small truck "
       "leaves up the haul road. The shadows swing slowly to the right as the sun moves round to the left, and white "
       "clouds streak across the sky."))

# ---------- S10 ----------
scene(n=10, fiil="DOLDURUR", eleman="su taban → +7 m (%100) · orta basamak + sütun dibi batar · platform kuru", rejim="B", t0="15:20", t1="17:20",
 st="M", g="G10",
 stage=(U(GARDEN) + ". " + U(CHANNEL) + "; the channel is dry. " + U(BUILT_S) +
        ". " + U(DRY) + ". Two large hoses come down the haul road from the rim and end at the edge of the entrance "
        "terrace above the dry basin."),
 moment="Twenty past three in the afternoon: the garden is planted and the hoses are ready to fill the basin.",
 comp=C_BLDG + " " + C_BRIDGE,
 light=LIGHT("15:20", "pm", "autumn"),
 tr=TR_B,
 act=("Clear water pours from the two large hoses fed by a pump truck on the rim, spreads across the basin floor and "
      "rises, while two workers on the entrance terrace pull the two hoses straight and a small truck waits. " + CREW),
 tex=T_GARDEN,
 phys=("The hoses lie along the haul road, their ends weighted down and resting on the edge of the entrance terrace. The "
       "building stands bolted to its base, and the footbridge rests on its pier. The limestone pillar stands on the dry "
       "basin floor."),
 mf=("Clear water pours from the two large hoses on the entrance terrace into the basin and rises steadily over the "
     "stepped quarry bed until it stands three metres below the raised base and turns clear turquoise; at the end the "
     "crew pulls the two hoses up the haul road onto a trailer."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The water spreads from the foot of the "
       "entrance terrace across the basin and climbs: the puddles join, the water closes over the basin floor, the "
       "middle bench goes under, the water creeps up the bridge pier and the limestone pillar, and finally covers the "
       "broad bench at the foot of the far wall by about a metre, three metres below the raised base and the footbridge "
       "deck, which stay dry. As it deepens the water clears from milky grey to calm turquoise, pale over the shallow "
       "benches and blue-green over the deep floor. At the end two workers pull the hoses up the haul road onto a "
       "trailer. The shadow of the west wall slides across the basin from the left as the sun sinks, and clouds streak "
       "across the sky."))

# ---------- S11 ----------
scene(n=11, fiil="AKAR", eleman="şelale: kuru → kanal → kaya → çatı → perde → göl (%100 · gerçek zaman)", rejim="G", t0="17:20", t1="17:20",
 st="M", g="G11",
 stage=(U(FULL) + ". " + U(GARDEN) + ". " + U(CHANNEL) + "; the channel is still dry and the rock face below the notch "
        "is bare and dry. " + U(BUILT) + ". The hoses are gone."),
 moment="Twenty past five in the afternoon: the quarry is a turquoise lake, and the channel is about to run.",
 comp=C_BLDG + " " + C_BRIDGE + " " + C_WATER,
 light=LIGHT("17:20", "low", "spring"),
 tr=TR_G,
 act=("A worker at the pump house pulls the valve lever, the pump starts, and two workers on the upper bench watch the "
      "channel fill, small and seen from afar, no readable faces; ripples run across the calm water."),
 tex=T_WATER,
 phys=("The building stands bolted to its base three metres above the water. The footbridge rests on its pier, whose "
       "foot stands in the water. The pump house sits on the base beside the pipe."),
 mf=("Water spills from the notch at the end of the channel on the upper bench, runs down the bare rock face onto the "
     "salon roof and pours over the straight steel lip at the roof's front edge, forming a wide thin curtain of water "
     "that falls two metres in front of the salon glass into the turquoise water."),
 body=("Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame water is "
       "already spilling from the notch: in the first two seconds it slides down the bare rock face in bright threads, "
       "by about four seconds it pours off the steel lip of the salon roof in a wide sheet, and by about six seconds the "
       "curtain reaches the water and white foam spreads at its foot; to the end of the shot the curtain falls steadily "
       "in front of the right part of the salon glass, and the left part of the glass stays clear. Ripples run out from "
       "the foot of the fall. Nothing else changes: the building, the footbridge, the garden and the pillar stand still, "
       "the two workers on the upper bench stay small with no readable faces, the long shadows stay where they are, and the few clouds hold still in the sky."))

# ---------- S12 ----------
scene(n=12, fiil="YANAR", eleman="gün batımı → mavi saat · ışıklar tek karede yanar · 3 kişi köprü ucuna", rejim="B", t0="17:20", t1="19:20",
 st="M", g="G12", nxt="G14",
 stage=(U(FALL_S) + "; the left part of the salon glass stays clear. " + U(FULL_S) + ". " + U(GARDEN_S) + ". " + U(BUILT_S) +
        ". The lights of the building are all still off."),
 moment="Twenty past five in the afternoon: the waterfall has just started to run.",
 comp=C_BLDG + " " + C_FALL,
 light=LIGHT("17:20", "low", "spring"),
 tr=TR_B,
 act=("A small crew lifts the last tools from the pump house onto a cart and a small truck drives them up the haul road, "
      "leaving fresh tyre tracks, while the waterfall falls steadily as a soft white veil and the low light fades from "
      "the walls. " + CREW),
 tex=T_WATER,
 phys=("The waterfall falls from the steel lip into the water two metres in front of the glass. The building stands "
       "bolted to its base three metres above the water, and the footbridge rests on its pier. The pump house sits on "
       "the base beside the pipe."),
 mf=("The sun sets beyond the left rim and the quarry fills with blue dusk; at one moment all the lights of the building "
     "come on at once, and their warm reflections stretch across the water; at the very end three people walk from the "
     "building onto the right end of the footbridge."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The last warm light climbs up the east "
       "wall and leaves it, the sky over the left rim glows and fades, and the rock walls turn cool blue-grey. The "
       "waterfall falls steadily all through the shot as a soft white veil. At one moment, about three quarters of the "
       "way through, all the lights come on together and stay on — the salon behind the falling water, both storeys of "
       "the glass front, the lamps on the terrace and footbridge railings, the low lights among the plants — and long "
       "warm reflections stretch across the darkening water. Early in the shot a small crew lifts the last tools from the "
       "pump house onto a cart and a small truck drives them up the haul road. In the last moments three people come out onto the "
       "terrace and step onto the end of the footbridge, small soft figures. Clouds streak across the sky and thin out."))

# ---------- S13 (SALON · ∥ S12'nin son 8 sn — SAPMA ⑤) ----------
scene(n=13, fiil="IŞIR", eleman="salon içi: perde akar · masa hazır · lambalar yanık (gerçek zaman)", rejim="G", t0="19:20", t1="19:20",
 st="S", g="G13", nxt="G13′", iso=800,
 stage=("the salon is finished and lived in: the long oiled timber table runs across the middle of the floor, parallel "
        "to the glass, laid with plates, glasses and linen napkins, twelve plain timber chairs along its sides; a low sofa "
        "and two armchairs stand by the glass at the right, and one person sits in the right armchair with a book, back to "
        "the camera, a dark silhouette against the water, no readable face; warm lamps glow over the table, and the tall panes stand between slim dark steel mullions. Just "
        "outside the glass, over the left two thirds of the front, a thin curtain of falling water pours down, blurring "
        "the view; through the clear glass at the right the turquoise water of the lake lies dark under the deep blue "
        "sky, the limestone pillar standing up out of it, warm reflections trembling on it, and beyond it the pale south "
        "wall of the quarry."),
 moment="Twenty past seven, deep blue hour: the table is laid and the water falls just outside the glass.",
 light=("LIGHTING: " + sunline("19:20") + ", " + LIGHT_DESC["in_blue"] + " " + SEASON["summer1"] + " The sun stays outside the frame."),
 tr=TR_G_IN,
 act=("The curtain of water falls steadily just outside the glass, its sheet rippling and catching the warm lamplight, "
      "the person in the armchair turns a page, back to the camera, no readable face, and the reflections tremble on "
      "the lake beyond the clear glass at the right."),
 tex=("Oiled oak table with a soft sheen, linen napkins, plates and glasses catching the lamplight, the pale oak floor "
      "with a warm patch of lamplight, fine droplets in a band on the outside of the panes where the spray drifts, the "
      "falling water streaking the view. " + FILMSTOCK_IN),
 phys=("The table stands on its legs on the oak floor, and the plates and glasses rest on it. Each lamp hangs from the "
       "ceiling on one long cable. The falling water pours down two metres outside the glass and never touches the "
       "panes, which stand clamped in their mullions."),
 mf=("Outside the glass the thin curtain of water keeps falling at its real speed from the roof lip into the lake over "
     "the left two thirds of the front, its sheet rippling and catching the warm light from the room, while beyond the "
     "clear glass at the right the warm reflections tremble on the dark water."),
 body=("Eight seconds pass in real time. Everything in this shot moves at natural speed. The curtain of water pours "
       "down just outside the glass without a pause, its folds sliding downward and its edges catching the warm "
       "lamplight; a fine mist of droplets beads on the outside of the panes. Through the clear glass at the right the "
       "reflections of the lights tremble on the dark water round the limestone pillar, and the deep blue sky holds "
       "still over the south wall. Inside, the person in the right armchair turns one page, back to the camera, a dark "
       "silhouette with no readable face; the laid table, the chairs and the lamps stay perfectly still."))

# ---------- S14 ----------
scene(n=14, fiil="DURULUR", eleman="üç kişi köprü ucundan → 5 m içeri, korkulukta durur (gerçek zaman) · tutuş", rejim="G", t0="19:20", t1="19:20",
 st="M", g="G14", iso=800,
 stage=(LIT + ". " + U(FALL_S) + ". " + U(FULL_S) + ". " + U(GARDEN_S) + ". " + U(BUILT_S) + ". Three people have just stepped "
        "onto the right end of the footbridge from the terrace, small dark figures seen from afar, no readable faces."),
 moment="Twenty past seven, deep blue hour: the building is lit and three people step out onto the footbridge.",
 comp=C_BLDG + " " + C_FALL + " The three people stand on the footbridge at about 690 pixels from the left, about twenty-five pixels tall.",
 light=LIGHT("19:20", "blue", "summer1"),
 tr=TR_G,
 act=("The three people walk slowly out along the footbridge and stop at the railing; the water falls steadily and "
      "the reflections tremble. The people stay small dark figures, no readable faces."),
 tex=T_DUSK,
 phys=("The footbridge spans rest on the terrace edge, the pier and the base. The building stands bolted to its "
       "base, and the people stand on the bridge deck."),
 mf=("The three people walk slowly from the right end of the footbridge to the railing about five metres out, and stop "
     "there facing the waterfall."),
 body=("Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame to about "
       "four seconds the three people walk slowly out along the footbridge, about five metres, and stop at the railing; "
       "from about four to eight seconds they stand still, looking towards the waterfall, the curtain of water falls "
       "steadily with white foam at its foot, the warm reflections tremble on the water, the lights stay on and nothing "
       "else changes. The people stay small dark figures, no readable faces. The few high thin clouds stay still in the "
       "deep blue sky."))

USTA = dict(g="G15", t="19:20",
 stage=("everything is finished. " + LIT + ". " + U(FALL_S) + ". " + U(FULL_S) + ". " + U(GARDEN_S) + ". " + U(BUILT_S) +
        ". Three people stand still at the footbridge railing, looking towards the waterfall, small dark figures, no "
        "readable faces."),
 moment="Twenty past seven, deep blue hour, early summer: the quarry is alive.",
 comp=C_BLDG + " " + C_FALL + " The three people stand at about 620 pixels from the left, about twenty-five pixels tall.",
 light=LIGHT("19:20", "blue", "summer1"),
 tr=TR_G,
 act=("The three people stand still at the railing, small dark figures with no readable faces; the water falls "
      "steadily and the reflections tremble."),
 tex=T_DUSK,
 phys=("The building stands bolted to its raised base against the rock, three metres above the water. The footbridge "
       "spans rest on the terrace edge, the pier and the base; the three people stand on the bridge deck."))

SALON_SON = {
 7: dict(g="G7′", t="13:20",
   stage=("the salon is furnished: one long solid timber table runs across the middle of the floor, parallel to the "
          "glass, with twelve plain timber chairs along both sides; a low sofa and two armchairs stand by the glass at the "
          "right round a low table, facing out over the quarry; a heap of plastic wrapping and flattened cardboard lies by "
          "the side door at the left edge of the frame. Through the glass the basin below is dry: grey rock benches, silt "
          "and puddles, the limestone pillar standing on the dry floor, and beyond it the pale south wall of the quarry."),
   moment="Twenty past one in the afternoon: the salon is furnished.",
   light=("LIGHTING: " + sunline("13:20") + ", " + LIGHT_DESC["in_noon"] + " " + SEASON["summer"] + " The sun stays outside the frame."),
   act=("The work is finished: the last worker leaves through the side door as a faint soft motion streak, and the band "
        "of sunlight lies still across the floor."),
   tex=("Fresh pale oak floorboards, the clean grain of the new table, a faint dust film on the new panes, plastic "
        "wrapping and cardboard in a heap by the side door, a bright band of sunlight across the floor, a patch of glare "
        "on the glass. " + FILMSTOCK_IN),
   phys=("The table stands on its legs on the floorboards, the chairs round it. The sofa and the armchairs rest on the "
         "floor by the glass. Outside, the limestone pillar stands on the dry basin floor.")),
 13: dict(g="G13′", t="19:20",
   stage=("the salon is unchanged: the long oiled timber table laid with plates, glasses and linen napkins, twelve chairs, "
          "the low sofa and two armchairs by the glass at the right, one person in the right armchair with a book, back "
          "to the camera, no readable face, warm lamps glowing over the table. Just outside the "
          "glass, over the left two thirds of the front, the thin curtain of falling water pours down, blurring the view; "
          "through the clear glass at the right the dark turquoise water of the lake, the limestone pillar standing up out "
          "of it, warm reflections trembling on it, and beyond it the pale south wall of the quarry."),
   moment="Twenty past seven, deep blue hour, eight seconds later: the water still falls just outside the glass.",
   light=("LIGHTING: " + sunline("19:20") + ", " + LIGHT_DESC["in_blue"] + " " + SEASON["summer1"] + " The sun stays outside the frame."),
   act=("The curtain of water falls steadily just outside the glass and the reflections tremble beyond it; the "
        "person in the armchair sits still, back to the camera, no readable face."),
   tex=("Oiled oak table with a soft sheen, linen napkins, plates and glasses catching the lamplight, the pale oak floor "
        "with a warm patch of lamplight, fine droplets in a band on the outside of the panes, the falling water streaking "
        "the view. " + FILMSTOCK_IN),
   phys=("The table stands on its legs on the oak floor, and the plates and glasses rest on it. Each lamp hangs from the "
         "ceiling on one long cable. The falling water pours down two metres outside the glass and never touches the "
         "panes, which stand clamped in their mullions.")),
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

def gorsel_salon(d, head, iso=100):
    return "\n".join([
        head, lens(iso), CAM_SALON, "",
        STRUCT + " AT THIS STAGE: " + d["stage"], "",
        SITE_SALON, "",
        "THE TIME MOMENT: " + d["moment"], "",
        COMP_SALON, "",
        d["light"], "",
        d.get("tr", TR_A_IN), "",
        "ACTIVITY: " + d["act"], "",
        "SITE TEXTURE: " + d["tex"], "",
        "PHYSICS: " + d["phys"], "",
        NEG_SALON, OUTPUT])

STAGE_SALON = ("This shot is the inside view of the same minutes as the neighbouring shot from the main station: "
               "nothing that can be seen through the glass is built or changed during this shot.")
def i2v(d):
    lock = (STAGE_SALON + " " + LOCK_SALON) if d["st"] == "S" else LOCK_MAIN
    tail = I2V_TAIL_SALON if d["st"] == "S" else I2V_TAIL
    return "\n\n".join([I2V_HEAD, "MOTION FOCUS: " + d["mf"], d["body"], lock, tail])

RJ = {"A": "A (10 dk)", "B": "B (2 sa)", "G": "G (gerçek zaman · 8 sn)"}
def blok(d):
    n = d["n"]; bas, son = n * 8, (n + 1) * 8
    ist = "SALON (ikinci istasyon · 2/2)" if d["st"] == "S" else "MAIN"
    saat = f"{d['t0']}→{d['t1']}" if d["rejim"] != "G" else f"{d['t0']} (+8 sn)"
    hedef = d.get("nxt", f"G{n+1}")
    out = [f"## 🎬 SAHNE {n} — {d['fiil']}", "",
           "```",
           f"SÜRE: 8,0 s ({bas},0–{son},0)  ·  ELEMAN + ARA HÂL: {d['eleman']}  ·  REJİM: {RJ[d['rejim']]}  ·  SAAT: {saat}  ·  İSTASYON: {ist}",
           "```", ""]
    if d["st"] == "S":
        if n == 7:
            out += ["> 🪟 **SALON KLİBİ** — ana zincirin DIŞINDA: S8 ile AYNI on dakikanın içeriden görüntüsü (SAPMA ④ — cam "
                    "cephe S6'nın SONUNDA biter, iç çekim camlı salonu ister). S6'nın I2V'si ana kare G8'e biter · bu klip "
                    "G7 → G7′ (salon) · S8 yine G8'den başlar. Dış kare iki yakada AYNIDIR; camdan görünen dünya bu on "
                    "dakikada değişmez (dış büyüme taşımaz — ISTASYON_VE_IC_MEKAN §0 ③).", ""]
        else:
            out += ["> 🪟 **SALON KLİBİ** — ana zincirin DIŞINDA: S12'nin SON sekiz saniyesi, içeriden, gerçek hızda "
                    "(SAPMA ⑤). S12'nin I2V'si ana kare G14'e biter · bu klip G13 → G13′ (salon) · S14 yine G14'ten "
                    "başlar. Dış kare iki yakada AYNIDIR.", ""]
        out += [f"### 📸 GÖRSEL PROMPT ({d['g']} · SALON İLK KARE)", "", "```",
                gorsel_salon(d, HEAD_SALON.format(n=n), d.get("iso", 100)), "```", ""]
    else:
        out += [f"### 📸 GÖRSEL PROMPT ({d['g']})", "", "```", gorsel_main(d, HEAD_MAIN.format(n=n)), "```", ""]
    out += [f"### 🎥 I2V PROMPT ({d['g']} → {hedef})", "", "```", i2v(d), "```", ""]
    if d["st"] == "S":
        c = SALON_SON[n]
        out += [f"### 🪟 SALON SON KARESİ ({c['g']} · bu klibin hedefi — sahne görseli DEĞİL, kapı saymaz)", "",
                "> Kapı bu bloğu saymaz (başlıkta GÖRSEL PROMPT yok) — ama aynı disiplinle yazıldı: STRUCTURE,",
                "> SITE / BACKGROUND, NEGATIVE salon karelerinde birebir. Üretimde G7′ ÖNCE üretilir (ana G9'un",
                "> mevsimi ve ışığıyla, kuru havza), G7 ondan geriye (mobilya çıkarılır); G13′ ana G14'ün ışığıyla,",
                "> G13 ondan (aynı an, perdenin kıvrımları farklı).", "",
                "```", gorsel_salon(dict(c, tr=(TR_G_IN if n == 13 else TR_A_IN)), HEAD_SALON_SON.format(n=n), 800 if n == 13 else 100), "```", ""]
    out += ["---", ""]
    return "\n".join(out)

def usta_blok():
    d = USTA
    return "\n".join([
        "## 🌟 USTA KARE — G15 (SAHNE DEĞİLDİR · son klibin hedefi · kapak kaynağı)", "",
        "> Üretim sırasının İLK karesi [§8]: G15 önce üretilir ve ikna edici değilse DURULUR; sonra",
        "> image-to-image geriye G14 → G12 → … → G0. Kapı: final hiyerarşisi (PLAN) bu sırayla okunuyor mu ·",
        "> perdenin arkasında ışıklı salon · çatı %53 · su %39 · kanıt nesnesi sütun x 922–1050 / 128 px · vinç ve",
        "> hortum YOK (SÖKÜM satırı) · mavi saat, güneş −6° · köprüde üç küçük figür. Kapak",
        "> (`THE_HIDDEN_FALLS_KAPAK.md`) bu promptun kopyası + başlık bandı satırıdır [MUZIK_VE_KAPAK §2.2].", "",
        "### 📸 USTA KARE PROMPT (G15)", "", "```",
        gorsel_main(dict(d, iso=800), HEAD_USTA), "```", ""])

H1 = f"""# 🎬 {FILM} — BÖLÜM 1  (S0 – S8 · G0 … G8 + G7/G7′ salon + 9 I2V · 0,0–72,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `{FILM}_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır. STRUCTURE bloğu bütün promptlarda, SITE / BACKGROUND ve NEGATIVE blokları kendi
> istasyonlarının bütün karelerinde BİREBİR aynı kelimelerle tekrarlanır; değişen AT THIS STAGE,
> THE TIME MOMENT, COMPOSITION'ın son cümleleri, LIGHTING, TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.
>
> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py`)
> ki ortak bloklar harfi harfine aynı kalsın [DERS 20].
>
> ⭐ Bu bölümün SON I2V'si (S8: G8 → G9) **G9 karesinde biter** ve G9 `BOLUM_2`'nin ilk görselidir:
> bölüm sınırı bir KAREDİR, kesme değil [DERS 52]. ⚠️ Sınır G9'dur (B1 9 · B2 6), betiğin ceil(15/2)
> = 8 bölmesi DEĞİL — salon klibi S7 iki dosyanın birleştiği kareye düşmesin diye (hikâye SAPMA ⑩).
> Kapı KLASÖR MODUNDA koşulur: `python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/{FILM}`.
>
> 🪟 **S7 SALON KLİBİDİR** (sahip senaryosu 08.10.2026 — "Cam salonun içindeyiz"): S6'nın I2V'si ana
> kare **G8**'e biter, S7 salonda G7 → G7′ koşar, S8 yine G8'den başlar. Salon karelerinin SITE
> bloğu ana SITE ile iki cümleyi BİREBİR paylaşır (kireçtaşı duvarlar + havzadaki sütun) [DERS 10].
>
> ⛔ Kelime kilitleri: "crane" yalnız G0–G8 ve S0–S8 I2V'lerinde; "turquoise" yalnız S10 I2V'sinden
> ve G11'den sonra; "waterfall" yalnız S11 I2V'sinden ve G12'den sonra; YASAK KELİME (PLAN künyesi)
> hiçbir promptta yok — negatifte bile.

---
"""

H2 = f"""# 🎬 {FILM} — BÖLÜM 2  (S9 – S14 · G9 … G14 + G13/G13′ salon + 6 I2V · 72,0–120,0 sn) + ⭐ USTA KARE G15

> Bölüm 1 ile aynı kurallar: **yalnız sahne blokları**, her prompt self-contained, STRUCTURE ve
> SITE / BACKGROUND birebir, blok etiketleri birebir [DERS 20].
>
> ⛔ **Bölüm 2 "devamı" değildir, ikinci yarıdır.** "Bölüm 1'deki gibi" atfı yasak; model bu
> dosyayı tek başına okuyor. İLK görsel **G9** bölüm 1'in son I2V'sinin HEDEF karesidir — aynı
> kare, iki dosyada bir kez yazılır (burada); bölüm 1'in S8 I2V'si onu "second provided image" olarak alır.
>
> 🪟 **S13 SALON KLİBİDİR**: S12'nin I2V'si ana kare **G14**'e biter, S13 salonda G13 → G13′ koşar
> (S12'nin son sekiz saniyesi, gerçek hız), S14 yine G14'ten başlar.
>
> ⭐ **USTA KARE G15 bu dosyanın sonunda, kendi `## 🌟 USTA KARE` bölümündedir** — sahne
> değildir, son klibin (S14: G14 → G15) hedef karesidir ve kapak kaynağıdır.
>
> ⭐ S11 · S13 · S14 GERÇEK ZAMANDIR (rejim G · "eight seconds pass"). S14'ün son dört saniyesi
> TUTUŞTUR (final kanıtı 116,0–120,0); insan kuralı "no readable faces".

---
"""

if "--tablo" in sys.argv:
    def golge(t):
        az, e = sun(hm(t))
        if e < 0: return "— (güneş ufkun altında)"
        r = ((az + 180) + 180) % 360 - 180
        return f"{r:+d}°"
    for d in S + [USTA]:
        t = d["t"] if "t" in d else d["t0"]
        az, e = sun(hm(t))
        print(d["g"], t, f"{az}°", f"{e:.1f}°".replace(".", ","), golge(t))
    for c in SALON_SON.values():
        az, e = sun(hm(c["t"])); print(c["g"], c["t"], f"{az}°", f"{e:.1f}°".replace(".", ","), "salon içi")
    sys.exit(0)

b1 = H1 + "\n" + "\n".join(blok(d) for d in S if d["n"] <= B1_SON)
b2 = H2 + "\n" + "\n".join(blok(d) for d in S if d["n"] > B1_SON) + "\n" + usta_blok()
open(os.path.join(OUT, f"{FILM}_BOLUM_1.md"), "w").write(b1)
open(os.path.join(OUT, f"{FILM}_BOLUM_2.md"), "w").write(b2)
print("yazıldı", len(b1), len(b2))
