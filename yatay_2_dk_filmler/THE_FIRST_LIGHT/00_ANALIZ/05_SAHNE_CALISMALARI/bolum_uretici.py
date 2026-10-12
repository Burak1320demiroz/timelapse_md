# THE FIRST LIGHT — bölüm dosyası üretici (ortak bloklar tek kaynaktan, DERS 20)
# KULLANIM (depo kökünden):
#   python3 yatay_2_dk_filmler/THE_FIRST_LIGHT/00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py yatay_2_dk_filmler/THE_FIRST_LIGHT
#   → THE_FIRST_LIGHT_BOLUM_1.md + _BOLUM_2.md yeniden yazılır; ardından prompt_kontrol.py klasör modunda koşulur.
#   --tablo  → PLAN kare tablosu satırlarını basar (saat · azimut · yükseklik · kadrajda gölge yönü)
#   --kadraj → PLAN DEĞİŞMEZLER px/yüzde satırlarını basar (KAMERA_DILI §3 tilt formülü)
# ⛔ ÜRETİM BAŞLADIKTAN SONRA KOŞULMAZ: üretilmiş filmin promptu kanıttır (URETIM_GUNLUGU kuralı).
# ⛔ Bölüm dosyası elle düzeltilirse bu betik o düzeltmeyi EZER — düzeltme önce buraya yazılır.
# TUR 3 (10.10.2026): sahip senaryosu 20 × 8,0 = 160,0 sn. 15 sahnelik sürüm (TUR 2) 05_SAHNE_CALISMALARI
#        dışında saklanmadı; farkları 00_HIKAYE_ONAYI.md TUR 3 tablosunda.
# Kalıp: ana istasyon + TEK iç klip (KUBBE İSTASYONU · S17, S16'nın son 8 sn'si ∥), bölüm sınırı G10.
import math, os, sys

FILM = "THE_FIRST_LIGHT"
OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
N_SAHNE = 20
B1_SON = 9          # BOLUM_1 = S0–S9 · BOLUM_2 = S10–S19 + USTA (sınır G10)
BEARING = 0         # ana kamera bakışı (kuzey) — kamera gözlemevinin güneyindeki tepecikte

# ── güneş (30° K · δ −15° · güneş saati) ───────────────────────────────────
phi, dec = math.radians(30.0), math.radians(-15.0)
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

# ── kadraj (KAMERA_DILI §3 · yatay 16:9 → kare yüksekliği 20,25 mm) ─────────
# TUR 3: h 24 → 28 · tilt 11 → 13 · davul 6 → 4 m — iç zemin ön duvarın üstünden okunsun (sahip şartı S06)
CAM_H, CAM_D, TILT = 28.0, 64.0, 13.0
def yv(y, d):
    return 50 + 24 * math.tan(math.radians(TILT) - math.atan((CAM_H - y) / d)) / 0.2025
def px(x, d):
    return round(960 + 1280.6 * x / d)

# ── ortak bloklar ───────────────────────────────────────────────────────────
HEAD_MAIN = ("Photorealistic documentary site photograph — Scene {n} of 20. Horizontal 16:9 time-lapse of an old "
             "mountain-top observatory being restored above a sea of cloud, from a fixed 24 mm site camera.")
HEAD_USTA = ("Photorealistic documentary site photograph — master frame G20, the target frame of the last shot "
             "(Scene 19 of 20). Horizontal 16:9 time-lapse of an old mountain-top observatory restored above a sea "
             "of cloud; a progress photograph from a fixed 24 mm site camera.")
HEAD_DOME = ("Photorealistic documentary interior photograph — Scene {n} of 20. Horizontal 16:9 time-lapse inside the "
             "copper dome of a restored mountain-top observatory; a progress photograph from a fixed 24 mm camera on "
             "the observing floor.")
HEAD_DOME_SON = ("Photorealistic documentary interior photograph — the last frame of Scene {n} of 20. Horizontal 16:9 "
                 "time-lapse inside the copper dome of a restored mountain-top observatory; a progress photograph from "
                 "a fixed 24 mm camera on the observing floor.")
CAM_MAIN = ("Camera: MAIN STATION — fixed tripod bolted to a high rock knoll to the south, lens 28 "
            "metres above the summit ground, 64 metres from the observatory's centre along the lens axis, "
            "bearing 0 degrees, tilt 13 degrees down, zero roll. The camera never moves.")
CAM_DOME = ("Camera: DOME STATION — fixed clamp mount bolted to the inside of the stone drum wall at the back of the "
            "observing floor, lens 2 metres above the floor, 10 metres from the telescope pier, bearing 160 degrees, "
            "tilt 0 degrees, zero roll. The camera never moves.")
STRUCT = ("STRUCTURE: When finished this will be a mountain-top observatory: a low round drum of pale grey granite, 24 "
          "metres across and 4 metres high, with an arched timber door and stone steps, under a copper dome of the "
          "same width that turns on a steel ring rail on the wall top and has one observing slit closed by a single "
          "copper shutter; inside, a large telescope with a dark grey fork mount and a long pale white tube; on the "
          "right a paved terrace with a steel railing at the cliff edge.")
# ⭐ İki SITE bloğu bir cümleyi BİREBİR paylaşır (ortak çapa — ISTASYON_VE_IC_MEKAN §0 ② · DERS 10).
#    TUR 3: çam yarıktan görünmez (yarık 159°, çam 125°) → ortak cümle TAŞ ÖRGÜSÜ (sahip: "aynı taş örgüsü").
ORTAK_TAS = ("The granite of the drum is laid in long low courses of squared blocks with thin dark joints.")
ORTAK_PINE = ("A single wind-bent mountain pine with a flat dark crown stands on a bare rock spur at the right end of "
              "the summit.")
CLOUD = "All round the summit a sea of white cloud fills the valleys far below, its surface flat and level."
SITE_MAIN = ("SITE / BACKGROUND: A bare summit ridge of grey rock and gravel. " + CLOUD +
             " Two far dark rock peaks rise out of it on the level horizon: a sharp twin-summit peak left of centre and "
             "a long flat-topped ridge right of centre. A gravel service road climbs from the left edge to a flat "
             "gravel work pad left of the drum. " + ORTAK_TAS + " " + ORTAK_PINE +
             " Behind the observatory the summit ends in a cliff edge.")
SITE_DOME = ("SITE / BACKGROUND: The observing floor inside the copper dome of a mountain-top observatory, seen from "
             "the back wall looking south-south-east towards the slit. " + ORTAK_TAS + " Above the curved wall the "
             "ribbed underside of the dome rises, dark steel arches between copper panels, and the slit shows the "
             "sky above the summit.")
NEG_MAIN = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The far peaks, the horizon, the "
            "cliff edge, the service road and the pine on its rock spur never change shape, position, size or "
            "spacing, and the sea of cloud stays at the same level. The summit holds exactly one "
            "building site, this one, and exactly one dome. Nothing already built or restored is removed or resized; "
            "no opacity fades. No beams of light into the sky. No readable text, letters, digits, numbers or symbols "
            "anywhere in the frame, on any surface. Nothing here has been branded, labelled, numbered or annotated by "
            "anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no CGI aesthetic.")
NEG_DOME = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The curved granite wall, the steel "
            "arches and the edges of the slit never change shape, position, size or spacing. The screen stays dark "
            "and blank all through the shot. Nothing already built is removed or resized; no opacity fades. No "
            "readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here "
            "has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No "
            "architectural visualisation look, no CGI aesthetic.")
OUTPUT = "Output: 16:9, 4K, no text, no watermark."
CREW = "Crew show only as faint soft motion streaks, never as sharp figures."
FILMSTOCK = "A documentary site photograph on colour negative film, true colour, fine grain."
FILMSTOCK_IN = "A documentary interior photograph on colour negative film, true colour, fine grain."

COMP_HEAD = ("COMPOSITION: Horizontal 16:9, the camera looking down 13 degrees, the level horizon at about "
             "seventy-seven percent of frame height. The mountain pine spans about 150 pixels of frame width — about "
             "one thirteenth — from about 1652 to 1805 pixels from the left, its crown top at about forty-nine "
             "percent, and keeps that width and position in every frame. ")
C_DRUM = ("The stone drum spans about 920 to 1400 pixels from the left, its front wall from about eighteen to "
          "twenty-five percent of frame height.")
C_FLOOR = "Over the front wall the round floor inside shows from about twenty-five to thirty-five percent."
C_DOME_ON = "The copper dome sits on the drum, its crown at about fifty-five percent of frame height."
C_STAND = "The maintenance stand spans about 382 to 877 pixels from the left."
C_TUBE_UP = "The upright telescope tube stands at about 1136 to 1184 pixels, its top at about forty-eight percent."
C_TUBE_LEVEL = "Inside the drum the level telescope tube lies from about 1070 to 1250 pixels from the left."
C_CRADLE = "The long cradle lies at the front left, from about 140 to 371 pixels from the left."
C_SLIT_STAND = "The slit runs up the front-right of the dome on the stand, from about 750 to 810 pixels at its base."
C_SLIT_R = "The slit runs up the front-right of the dome face, from about 1275 to 1340 pixels from the left at its base."
C_SLIT_C = "The slit runs up the middle of the dome face, from about 1125 to 1195 pixels from the left."
COMP_TAIL = "Nothing that proves progress falls into the bottom tenth or the top-right corner of the frame."
COMP_DOME = ("COMPOSITION: Horizontal 16:9. The camera is level. A large dark flat screen on a low desk fills the left "
             "foreground, from about 140 to 780 pixels from the left and from about twelve to fifty percent of frame "
             "height — about one third of the frame width — its blank face turned to the camera. The telescope stands "
             "right of centre on its pier, the fork from about 900 to 1260 pixels from the left, its long white tube "
             "rising to the right towards the slit; the slit is a tall straight band of sky from about 1300 to 1480 "
             "pixels from the left — it spans about 180 pixels of frame width, about one eleventh, and keeps that "
             "width — from about sixty-four percent of frame height to the top edge. " + COMP_TAIL)

TR_A = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and "
        "crew all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, "
        "clouds drift in one smooth flow, machines move fast with light motion blur. Nothing moves at "
        "normal speed.")
TR_B = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and "
        "crew all move at the same accelerated speed. Two hours pass across this shot: shadows swing slowly "
        "round, clouds streak across the sky, the sea of cloud rolls slowly, machines smear into heavy "
        "motion blur. Nothing moves at normal speed.")
TR_G_IN = ("TIME RATE: Everything in this frame moves at natural speed. Eight seconds pass across this shot: the "
           "telescope, the two people at the desk and the sky in the slit move at their real pace; nothing is "
           "accelerated.")

I2V_HEAD = ("The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its "
            "last frame is that image, matched frame for frame — same framing, same light, same objects in the same "
            "places.")
LOCK_MAIN = ("The camera does not move at any point. The framing is identical in the first and last frame. The two "
             "far peaks, the level horizon, the cliff edge, the service road and the mountain pine on its rock spur "
             "stay exactly where they are, at exactly the same size and shape, for the whole shot; the pine occupies "
             "exactly the same width of the frame in the first and last frame, and the sea of cloud stays at the "
             "same level. The summit holds exactly one building site and exactly one dome. Nothing already built or "
             "restored is removed or resized.")
LOCK_DOME = ("The camera does not move at any point. The framing is identical in the first and last frame. The "
             "curved granite wall, the steel arches and the edges of the slit stay exactly where they are, at exactly "
             "the same size and shape, for the whole shot; the slit occupies exactly the same width of the frame in "
             "the first and last frame. The screen stays dark and blank. Nothing already built is removed or resized.")
STAGE_DOME = ("This shot is the inside view of the same eight seconds as the end of the neighbouring shot from the "
              "main station: nothing outside the dome is built or changed during this shot.")
I2V_TAIL = ("Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
            "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
            "documentary time-lapse cinematography.")
I2V_TAIL_DOME = ("Camera: fixed clamp mount, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
                 "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
                 "documentary time-lapse cinematography.")

# ── tekrarlanan durum cümleleri (aynı nesne her karede aynı kelimelerle) ─────
DRUM_OLD = ("the granite drum stands on the summit, its stone darkened with grime and half covered in dark ivy, a "
            "rusty steel ring rail on its wall top and an old arched timber door in front")
DRUM_CLEAN_OLDRAIL = ("the granite drum stands washed clean, a rusty steel ring rail on its wall top and an old arched "
                      "timber door in front")
DRUM_NEW = "the granite drum stands washed clean, a bright new steel ring rail on its wall top and an arched timber door in front"
FLOOR_OLD = "the round floor inside dark and worn"
FLOOR_NEW = "the round floor inside laid in wide pale new panels"
DOME_OLD_AIR = ("the old copper dome, green with verdigris, hangs on four slings from the hook of a large yellow "
                "crawler crane a few metres above the drum, its slit on its front-right side closed by a single old "
                "green shutter")
DOME_OLD_STAND = ("the old green copper dome rests on a low round steel maintenance stand with a plank walkway on "
                  "the pad left of the drum, its slit on its front-right closed by a single old green shutter")
DOME_NEW_OLDSHUT = ("the dome, re-clad in bright new copper, rests on the maintenance stand left of the drum, its slit "
                    "on its front-right still closed by the old green shutter")
DOME_NEW_STAND = ("the dome, re-clad in bright new copper, rests on the maintenance stand left of the drum, its slit on "
                  "its front-right closed by a new copper shutter")
DOME_ON = ("the copper dome sits on the ring rail on top of the drum, its slit on its front-right side closed by a "
           "single copper shutter")
STAND_EMPTY = "the low round steel maintenance stand stands empty on the work pad left of the drum"
TEL_OLD = ("inside the roofless drum the old telescope stands on its round pier, a dark grey fork mount holding a long "
           "dull grey-white tube grimed with dust, pointing straight up above the wall top")
FORK_EMPTY = "inside the roofless drum the dark grey fork mount stands on its round pier, its two arms empty"
TEL_LEVEL = ("inside the roofless drum the telescope stands whole again on its round pier, the dark grey fork mount "
             "holding the long pale white tube level between its arms")
TEL_PARK = ("inside the roofless drum the whole telescope stands on its round pier, the fork mount holding the long "
            "pale white tube pointing straight up")
CRADLE_EMPTY = "a long low steel cradle stands empty at the front left of the work pad"
CRADLE_TUBE_OLD = ("the long dull grey-white telescope tube lies on a long low steel cradle at the front left of the "
                   "work pad, grimed with dust and scuffed")
CRADLE_TUBE_NEW = ("the long telescope tube lies on the long low steel cradle at the front left of the work pad in a "
                   "light steel lifting frame, its outer panels new and pale white")
CRANE = "a large yellow crawler crane with a long grey lattice boom stands on its tracks behind the drum"
CRANE_UP = CRANE + ", its boom raised steeply, its tip above the top edge of the frame"
TOWERS = "two steel scaffold towers with plank platforms stand against the flanks of the drum"
PATH_OLD = "a rutted gravel path and cracked old stone steps lead from the pad to the door"
PATH_NEW = ("a path of wide pale new stone slabs and new stone steps lead from the work pad to the door, a row of low "
            "dark path lamps beside them")
PATH_LIT = ("a path of wide pale new stone slabs and new stone steps lead from the work pad to the door, the low path "
            "lamps beside them lit low")
TERR_OLD = "on the right an old paved terrace runs to the cliff edge, its edge bare"
TERR_NEW = "on the right an old paved terrace runs to the cliff edge, a new steel railing along its whole edge"
def STACK(*x):
    base = "a roped-off stacking area at the front of the pad holds "
    if not x: return base + "a few empty steel crates"
    return base + (x[0] if len(x) == 1 else ", ".join(x[:-1]) + " and " + x[-1])
S_IVY = "crates of ivy"
S_COP = "green copper"
S_RAIL = "rusty rail"
S_FLOOR = "old boards"
S_PAN = "old tube panels"
S_SHUT = "the old green shutter"
S_PLANK = "walkway planks"
S_STEP = "old steps"
def U(x): return x[0].upper() + x[1:]

# ── doku ────────────────────────────────────────────────────────────────────
T_OLD = ("Dark grime and lichen streaks on the pale grey granite, dark ivy over half the drum, green verdigris on "
         "the old copper, rust stains below the rail, deep tyre tracks and ruts in the "
         "gravel, a film of dust on every machine. " + FILMSTOCK)
T_WASH = ("Pale grey granite washed clean in wide vertical bands beside darker strips still stained with grime, wet "
          "patches and dark runs of water below them, torn ivy on the gravel, tyre ruts and tracks, a film of dust on "
          "the machines. " + FILMSTOCK)
T_COPPER = ("Bright new salmon-pink copper sheets with crisp seams beside old green verdigris panels, a heap of "
            "stripped green copper on the gravel, pale scuff marks and boot prints in the dust on the walkway, tyre "
            "ruts and tracks. " + FILMSTOCK)
T_RAIL = ("Pale grey granite washed clean, a bright band of new steel rail on the wall top beside rust-stained old "
          "sections, rust offcuts and a stack of old rail on the gravel, tyre tracks and ruts across the work pad, a "
          "film of dust on the crane tracks. " + FILMSTOCK)
T_FLOOR = ("Wide pale new floor panels beside a band of dark worn boards, sawdust and offcuts on the floor, a bright "
           "band of new steel rail on the wall top, tyre ruts and tracks in the gravel, a film of dust on the crane "
           "tracks. " + FILMSTOCK)
T_TUBE = ("Clean pale white tube panels beside dull grimed ones, a stack of old panels with scuffed paint, pale scuff "
          "marks and boot prints in the dust round the cradle, tyre ruts and tracks in the gravel, bright new copper "
          "on the dome. " + FILMSTOCK)
T_FIT = ("Bright new copper on the dome, a clean pale white tube, crisp dark grey paint on the fork, a pale new "
         "floor, tyre ruts and tracks in the gravel, a film of dust on the crane tracks, scuffed planks on the "
         "scaffold. " + FILMSTOCK)
T_PATH = ("Copper already dulling from salmon-pink towards warm brown, pale new stone slabs with fresh mortar joints "
          "beside cracked old steps, raked gravel along the new path, tyre ruts and tracks on the work pad, a film of "
          "dust on the crane tracks. " + FILMSTOCK)
T_TERR = ("Copper dulled to warm brown, bright galvanised railing posts with a dull sheen, worn old paving with a "
          "band of fresh grout at the edge, raked gravel by the new path, tyre ruts and tracks on the work pad, a "
          "film of dust on the crane tracks. " + FILMSTOCK)
T_FINISH = ("Copper dulled to a warm even brown with a soft sheen, pale grey granite washed clean, pale new paving "
            "with a thin film of dust, raked gravel on the work pad with the faint print of old tyre tracks, a few "
            "pale scuff patches where the stands stood. " + FILMSTOCK)
T_DUSK = ("Copper gone deep warm brown in the dusk, pale grey granite cool and blue-grey, a faint red glow along the "
          "edges of the open slit, raked gravel with the faint print of old tyre tracks, a thin film of dust on the "
          "new paving, small warm pools of light from the low path lamps. " + FILMSTOCK)
T_EVE = ("Copper gone deep warm brown, pale grey granite cool and blue-grey, raked gravel with the faint print of "
         "old tyre tracks, a thin film of dust on the new paving, small warm pools of light from the low path lamps, "
         "a dull sheen on the railing. " + FILMSTOCK)
T_DOME = ("Pale grey granite of the inner wall with old grime streaks, ribbed copper panels, dark steel arches with "
          "a dull sheen, the pale white tube catching a dim red sheen, a thin film of dust on the pale new floor, "
          "scuff patches and boot prints round the pier, a dark band of cable along the wall. " + FILMSTOCK_IN)

# ── ışık (bakış 0° — güneş bütün gün kameranın ARKASINDA: sabah sağda, öğle tam arkada, akşam solda) ──
LIGHT_DESC = {
 "morning": ("low behind the camera on the right: cool soft morning light from the right, the sea of cloud "
             "below white and pale blue, long shadows to the left and away from the camera."),
 "am": ("behind the camera on the right, so the faces turned to the camera catch the light from the right and the "
        "shadows fall to the left and away from the camera."),
 "noon": ("high behind the camera, so the light falls almost straight onto the faces turned to the camera and short "
          "shadows fall away from the camera."),
 "pm": ("high behind the camera on the left, so the light falls almost straight onto the faces turned to the camera "
        "and short shadows fall to the right and away."),
 "warm": ("lower behind the camera on the left, so warm afternoon light catches the copper and the stone from the "
          "left and the shadows fall to the right and away."),
 "sunset": ("on the horizon behind the camera on the left, outside the frame: the last warm light has just left the "
            "summit, the sky pales to gold low in the west and blue overhead, and the sea of cloud below turns "
            "faintly pink."),
 "dusk": ("just below the horizon behind the camera on the left, outside the frame, so there is no direct sun: early "
          "blue hour, the sky clear and deepening blue, a last warm band low on the far horizon, the sea of cloud "
          "pale grey-blue."),
 "blue": ("below the horizon behind the camera on the left, outside the frame, so there is no direct sun: deep blue "
          "hour, the sky deep clear blue with the first bright stars, the sea of cloud below pale blue-grey, the "
          "stone and the copper cool and dim but clearly readable."),
 "in_dusk": ("below the horizon, so there is no direct sun: through the slit the sky is deepening blue; inside, the "
             "floor lies in dim cool light from the slit and the dim red light of a few low work lamps."),
}
SEASON = {
 "winter": "Winter: a crisp clear pale sky, the far peaks sharp.",
 "spring": "Spring: a few small high clouds over the far peaks.",
 "summer": "Summer: a soft hazy sky, tall white clouds building far off.",
 "autumn": "Autumn: a clear deep sky with a few thin high clouds.",
}
def LIGHT(t, key, season):
    return f"LIGHTING: {sunline(t)}, {LIGHT_DESC[key]} {SEASON[season]} The sun stays outside the frame."

# ── sahne verisi ─────────────────────────────────────────────────────────────
S = []
def scene(**k): S.append(k)

# ---------- S0 ----------
scene(n=0, st="M", fiil="KALDIRIR", eleman="eski kubbe havada → soldaki bakım sehpasına iner (%100) · teleskop açığa çıkar", rejim="A", t0="07:35", t1="07:45",
 g="G0",
 stage=("the restoration has just begun. " + U(DOME_OLD_AIR) + ", already moving to the left. " + U(DRUM_OLD) + "; "
        + TEL_OLD + ", " + FLOOR_OLD + ". Below it on the left a low round steel maintenance stand with a plank "
        "walkway waits empty on the work pad, and " + CRADLE_EMPTY + ". " + U(TOWERS) + ". "
        + U(PATH_OLD) + ". " + U(STACK()) + ". " + U(TERR_OLD) + "."),
 moment="Early morning on the first day of work: the old dome is already off its drum and swinging away.",
 comp=(C_DRUM + " The dome hangs above the left half of the drum, from about 716 to 1204 pixels from the left, its "
       "crown at about fifty-eight percent of frame height. " + C_TUBE_UP),
 light=LIGHT("07:35", "morning", "winter"),
 tr=TR_A,
 act=("The crawler crane swings the old dome on its four slings to the left and lowers it towards the maintenance "
      "stand, a crew on the walkway guides it with taglines, and a second crew carries empty crates from a flatbed "
      "truck to the stacking area; the crane carries a visible load. " + CREW),
 tex=T_OLD,
 phys=("The dome hangs from the crane hook on four taut slings. The crawler crane stands on its tracks on the "
       "gravel. The stand rests on the gravel, and the telescope rests on its pier."),
 mf=("The crawler crane carries the old copper dome on its four slings from above the drum to the work pad on the "
     "left and lowers it onto the low round maintenance stand."),
 body=("Ten minutes pass in the cool morning light. Everything in this shot is time-lapsed at the same rate. From the "
       "first frame the dome is already moving: it swings slowly to the left on its slings, clear of the drum, and "
       "comes down onto the maintenance stand, where the crew steadies it with taglines. Behind it the roofless drum "
       "stands open to the sky, the old telescope upright inside, grey with dust. The crew carries empty crates from "
       "the flatbed truck to the stacking area, and the truck drives off down the service road to the left. At the "
       "end the crew slings the telescope tube to the crane on four slings. The sea of cloud lies white below, and a "
       "few thin high clouds drift slowly from the right in one smooth flow."))

# ---------- S1 ----------
scene(n=1, st="M", fiil="SÖKER", eleman="teleskop ana gövdesi (tüp) çataldan → öndeki beşiğe (%100) · çatal + kaide kalır", rejim="A", t0="07:45", t1="07:55",
 g="G1",
 stage=(U(DOME_OLD_STAND) + ". " + U(DRUM_OLD) + "; " + TEL_OLD + ", four slings hooked to its tube from the crane, "
        + FLOOR_OLD + ". " + U(CRANE) + ". " + U(CRADLE_EMPTY) + ". " + U(TOWERS) + ". " + U(PATH_OLD) + ". "
        + U(STACK()) + ". " + U(TERR_OLD) + "."),
 moment="Quarter to eight in the morning: the dome is down, and the telescope tube is slung.",
 comp=C_DRUM + " " + C_STAND + " " + C_TUBE_UP + " " + C_CRADLE,
 light=LIGHT("07:45", "morning", "winter"),
 tr=TR_A,
 act=("The crawler crane lifts the long telescope tube straight up out of the fork mount on its slings, swings it to "
      "the left and lays it on the long cradle, while a crew on the scaffold tower unbolts it and a second crew "
      "lashes it down; the crane carries a visible load. " + CREW),
 tex=T_OLD,
 phys=("The tube hangs from the crane hook on four taut slings. The crawler crane stands on its tracks on the "
       "gravel. The dome rests on its maintenance stand, and the fork mount stays bolted on its pier."),
 mf=("The crawler crane lifts the long telescope tube from the fork mount inside the drum and carries it on its "
     "slings to the long cradle at the front left, where the crew lays it down; the fork mount stays on its pier."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the tube is "
       "already rising: it lifts slowly out of the fork on the crane hook, swings to the left over the work pad and "
       "comes down onto the cradle, where the crew lashes it. The dark fork mount stays standing on its pier, its two "
       "arms empty. A small truck brings a load of empty crates up the service road and the crew sets them in the "
       "stacking area. At the end the crane raises its boom steeply until its tip and its line rise above the top "
       "edge of the frame. Long shadows fall to the left, and thin high clouds drift slowly from the right."))

# ---------- S2 ----------
scene(n=2, st="M", fiil="TEMİZLER", eleman="sarmaşık + kir → temiz taş (%0 → %100, soldan sağa şerit şerit)", rejim="B", t0="07:55", t1="09:55",
 g="G2",
 stage=(U(FORK_EMPTY) + "; " + DRUM_OLD + ", " + FLOOR_OLD + ". " + U(DOME_OLD_STAND) + ". " + U(CRADLE_TUBE_OLD)
        + ". " + U(CRANE_UP) + ". " + U(TOWERS) + ", washing lances on their platforms. " + U(PATH_OLD)
        + ". " + U(STACK()) + ". " + U(TERR_OLD) + "."),
 moment="Five to eight in the morning: the drum stands open, and the cleaning begins.",
 comp=C_DRUM + " " + C_FLOOR + " " + C_STAND + " " + C_CRADLE,
 light=LIGHT("07:55", "morning", "winter"),
 tr=TR_B,
 act=("A crew on the two scaffold towers pulls the ivy off the drum and sprays the grime off its stone in wide "
      "bands from left to right, a second crew carries the stripped ivy in crates to the stacking "
      "area, and a small truck brings more empty crates up the service road. " + CREW),
 tex=T_WASH,
 phys=("The scaffold towers stand on timber pads on the gravel against the drum. The crates rest on the gravel in "
       "the stacking area, and the tube rests on the long cradle. The dome rests on its maintenance stand."),
 mf=("The crew on the scaffold towers strips the ivy and washes the drum from its left edge to its right edge in wide "
     "vertical bands, and carries the stripped ivy in crates from the foot of the drum to the stacking area."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Band by band from the left the dark "
       "ivy comes away and the grime runs off the drum, the pale grey granite coming up clean and drying lighter as "
       "the crew shifts the scaffold towers along to the right; at the end the whole drum is clean, the rusty rail "
       "still along its wall top. The crew carries the stripped ivy and grime in crates to the stacking area, where "
       "the full crates pile up, and a small truck brings more empty crates up the service road. The shadows shorten "
       "and swing as the sun climbs behind the camera on the right, and thin clouds streak across the sky."))

# ---------- S3 ----------
scene(n=3, st="M", fiil="KAPLAR", eleman="kubbe kaplaması yeşil → yeni bakır (%0 → %100, soldan) · eski kapak YERİNDE", rejim="B", t0="09:55", t1="11:55",
 g="G3",
 stage=(U(FORK_EMPTY) + "; " + DRUM_CLEAN_OLDRAIL + ", " + FLOOR_OLD + ". " + U(DOME_OLD_STAND) + ". "
        + U(CRADLE_TUBE_OLD) + ". " + U(CRANE) + ", with a pallet of new copper sheets on the hook. A flatbed truck "
        "loaded with pallets of bright copper sheets stands on the pad. " + U(TOWERS) + ". " + U(PATH_OLD) + ". "
        + U(STACK(S_IVY)) + ". " + U(TERR_OLD) + "."),
 moment="Five to ten in the morning: the stone is clean, and the new copper has arrived.",
 comp=C_DRUM + " " + C_STAND + " " + C_SLIT_STAND + " " + C_CRADLE,
 light=LIGHT("09:55", "am", "spring"),
 tr=TR_B,
 act=("A crew on the walkway of the stand strips the green copper panels off the dome and fixes bright new copper "
      "sheets in their place from the left, the crawler crane lifts the pallets of new sheets from the flatbed truck "
      "to the walkway, and a second crew stacks the stripped green panels in the stacking area; the crane carries a "
      "visible load. " + CREW),
 tex=T_COPPER,
 phys=("The pallet hangs from the crane hook on four slings. The dome rests on its maintenance stand and the crew "
       "stands on its plank walkway. The pallets rest on the bed of the flatbed truck."),
 mf=("The crawler crane lifts the pallets of new copper sheets from the flatbed truck to the walkway of the stand, "
     "and the crew fixes the sheets onto the dome from its left side to its right side."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Strip by strip from the left the old "
       "green panels come off the dome and bright salmon-pink copper takes their place, the seams running in crisp "
       "lines from the base to the crown, until the whole dome shines new; only the old green shutter stays in its "
       "slit on the front-right side. The crew stacks the stripped green panels in the stacking area, and the emptied "
       "truck drives off to the left. The shadows swing slowly round behind the camera as the sun climbs, and small "
       "white clouds drift across the sky."))

# ---------- S4 ----------
scene(n=4, st="M", fiil="YENİLER", eleman="paslı halka ray → yeni çelik ray (%0 → %100, duvar tepesinde parlak bant)", rejim="A", t0="11:55", t1="12:05",
 g="G4",
 stage=(U(FORK_EMPTY) + "; " + DRUM_CLEAN_OLDRAIL + ", " + FLOOR_OLD + ". " + U(DOME_NEW_OLDSHUT) + ". "
        + U(CRADLE_TUBE_OLD) + ". " + U(CRANE) + ", with a curved new rail section on the hook. A flatbed truck "
        "loaded with curved sections of bright new rail stands on the pad. " + U(TOWERS) + ". " + U(PATH_OLD) + ". "
        + U(STACK(S_IVY, S_COP)) + ". " + U(TERR_OLD) + "."),
 moment="Five to twelve: the dome is clad in new copper, and the new ring rail has arrived.",
 comp=C_DRUM + " " + C_STAND + " " + C_SLIT_STAND + " " + C_CRADLE,
 light=LIGHT("11:55", "noon", "spring"),
 tr=TR_A,
 act=("A crew on the scaffold towers unbolts the rusty old rail section by section and lowers the sections to the "
      "stacking area, and the crawler crane lifts the curved new sections from the flatbed truck and sets each one on "
      "the wall top, where the crew bolts it down; the crane carries a visible load. " + CREW),
 tex=T_RAIL,
 phys=("The rail section hangs from the crane hook on two slings. The new sections rest on timber bearers on the bed "
       "of the flatbed truck. The sections already set are bolted to the wall top, and the crawler crane stands on "
       "its tracks on the gravel."),
 mf=("The crawler crane lifts the curved new rail sections from the flatbed truck onto the wall top of the drum, and "
     "the crew bolts them down one after another round the ring from the left."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first new "
       "section is already swinging over the wall: the crew lifts the rusty old rail off the wall top piece by piece "
       "and carries it to the stack of old rail, and the crane sets the bright new sections down in its place one "
       "after another round the ring from the left, until a continuous bright band of new steel runs along the whole "
       "wall top. The emptied truck drives off to the left. Short shadows fall away from the camera, and a few small "
       "clouds drift slowly from the right."))

# ---------- S5 ----------
scene(n=5, st="M", fiil="DÖŞER", eleman="iç zemin koyu, aşınmış → açık renkli geniş paneller (%0 → %100, arkadan öne halka halka)", rejim="B", t0="12:05", t1="14:05",
 g="G5",
 stage=(U(FORK_EMPTY) + "; " + DRUM_NEW + ", " + FLOOR_OLD + ". " + U(DOME_NEW_OLDSHUT) + ". " + U(CRADLE_TUBE_OLD)
        + ". " + U(CRANE) + ", with a pallet of pale floor panels on the hook. A flatbed truck loaded with pallets of "
        "wide pale floor panels stands on the pad. " + U(TOWERS) + ". " + U(PATH_OLD) + ". "
        + U(STACK(S_IVY, S_COP, S_RAIL)) + ". " + U(TERR_OLD) + "."),
 moment="Five past twelve: the ring rail is new, and the floor inside is next.",
 comp=C_DRUM + " " + C_FLOOR + " " + C_STAND + " " + C_CRADLE,
 light=LIGHT("12:05", "noon", "spring"),
 tr=TR_B,
 act=("The crawler crane lowers the pallets of floor panels from the flatbed truck over the wall into the drum, a crew "
      "inside lifts the dark worn boards and lays wide pale new panels round the pier, ring by ring from the back "
      "wall, and a second crew carries the old boards in crates to the stacking area; the crane carries a visible "
      "load. " + CREW),
 tex=T_FLOOR,
 phys=("The pallet hangs from the crane hook on four slings. The fork mount stays bolted on its round pier. The new "
       "panels rest on the floor bed, and the pallets rest on the bed of the flatbed truck."),
 mf=("The crawler crane lowers the pallets of pale floor panels from the flatbed truck into the open drum, and the "
     "crew lays the panels on the round floor, ring after ring from the back towards the front."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Pallet after pallet swings over the "
       "wall into the open drum, and ring by ring from the back the dark worn floor gives way to wide pale new "
       "panels, until a clean pale round floor lies all round the dark fork mount on its pier. The crew carries the "
       "old boards in crates to the stacking area, and the emptied truck drives off to the left. The shadows swing "
       "slowly from the left to the right as the sun passes behind the camera, and small white clouds drift across "
       "the sky."))

# ---------- S6 ----------
scene(n=6, st="M", fiil="YENİLER", eleman="beşikteki tüpün dış panelleri kirli → yeni, açık renkli (%0 → %100, soldan) · aynı tüp", rejim="A", t0="14:05", t1="14:15",
 g="G6",
 stage=(U(FORK_EMPTY) + "; " + DRUM_NEW + ", " + FLOOR_NEW + ". " + U(DOME_NEW_OLDSHUT) + ". " + U(CRADLE_TUBE_OLD)
        + ". " + U(CRANE) + ", with a pallet of new tube panels on the hook. A flatbed truck loaded with pallets of "
        "pale white tube panels stands on the pad. " + U(TOWERS) + ". " + U(PATH_OLD) + ". "
        + U(STACK(S_IVY, S_COP, S_RAIL, S_FLOOR)) + ". " + U(TERR_OLD) + "."),
 moment="Five past two in the afternoon: the floor is new, and the tube's turn has come.",
 comp=C_DRUM + " " + C_FLOOR + " " + C_STAND + " " + C_CRADLE,
 light=LIGHT("14:05", "pm", "spring"),
 tr=TR_A,
 act=("A crew at the cradle unbolts the grimed outer panels of the tube and fits new pale white panels in their place "
      "from the left end, the crawler crane lifts the pallets of new panels from the flatbed truck to the cradle, and "
      "a second crew stacks the old panels in the stacking area; the crane carries a visible load. " + CREW),
 tex=T_TUBE,
 phys=("The pallet hangs from the crane hook on four slings. The tube rests on the long cradle, and the cradle stands "
       "on its feet on the gravel. The dome rests on its maintenance stand."),
 mf=("The crawler crane lifts the pallets of pale white tube panels from the flatbed truck to the cradle, and the crew "
     "fits the panels onto the tube from its left end to its right end."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first "
       "pallet is already swinging down to the cradle: panel by panel from the left end the dull grimed skin of the "
       "tube comes off and clean pale white panels take its place, until the whole tube lies new on the cradle, the "
       "same length and the same width; the crew bolts a light steel lifting frame round it. The crew stacks the old "
       "panels in the stacking area, and the emptied truck drives off to the left. Short shadows fall to the right, "
       "and a few small clouds drift slowly from the left."))

# ---------- S7 ----------
scene(n=7, st="M", fiil="GERİ GETİRİR", eleman="yenilenmiş tüp beşikten → çatala (%100, yatay) · beşik boşalır", rejim="A", t0="14:15", t1="14:25",
 g="G7",
 stage=(U(FORK_EMPTY) + "; " + DRUM_NEW + ", " + FLOOR_NEW + ". " + U(DOME_NEW_OLDSHUT) + ". " + U(CRADLE_TUBE_NEW)
        + ", four slings hooked to the frame from the crane. " + U(CRANE) + ". " + U(TOWERS) + ". " + U(PATH_OLD)
        + ". " + U(STACK(S_IVY, S_COP, S_RAIL, S_FLOOR, S_PAN)) + ". " + U(TERR_OLD) + "."),
 moment="Quarter past two in the afternoon: the tube is renewed and slung for lifting.",
 comp=C_DRUM + " " + C_FLOOR + " " + C_STAND + " " + C_CRADLE,
 light=LIGHT("14:15", "pm", "spring"),
 tr=TR_A,
 act=("The crawler crane lifts the renewed tube in its lifting frame off the cradle, swings it to the right over the "
      "drum wall and lowers it level between the arms of the fork mount, where a crew on the scaffold tower bolts it "
      "in, while a second crew carries the cradle lashings in a crate to the stacking area; the crane carries a "
      "visible load. " + CREW),
 tex=T_FIT,
 phys=("The tube in its frame hangs from the crane hook on four taut slings. The fork mount stays bolted on its round "
       "pier. The crawler crane stands on its tracks on the gravel, and the dome rests on its maintenance stand."),
 mf=("The crawler crane carries the renewed tube in its light steel lifting frame from the cradle on the left into "
     "the open drum and lowers it level into the fork mount on the pier."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the tube is "
       "already rising off the cradle in its frame: it swings slowly to the right over the dome and the drum wall and "
       "sinks level into the drum, until it rests between the dark arms of the fork — the same tube, the same length, "
       "now clean and pale. The cradle is left empty at the front left. The crew carries the cradle lashings in a "
       "crate to the stacking area, and at the end the crew unbolts the lifting frame and hooks it back to the crane. "
       "Short shadows fall to the right, and a few small clouds drift slowly from the left."))

# ---------- S8 ----------
scene(n=8, st="M", fiil="SINAR", eleman="ilk hareket testi: tüp yatay → dik park (tek eğim hareketi) · taşıma çerçevesi kamyonla gider", rejim="A", t0="14:25", t1="14:35",
 g="G8",
 stage=(U(TEL_LEVEL) + "; " + DRUM_NEW + ", " + FLOOR_NEW + ". " + U(DOME_NEW_OLDSHUT) + ". " + U(CRADLE_EMPTY) + ". "
        + U(CRANE) + ", with a light steel lifting frame on the hook. A flatbed truck stands empty on the pad. "
        + U(TOWERS) + ". " + U(PATH_OLD) + ". " + U(STACK(S_IVY, S_COP, S_RAIL, S_FLOOR, S_PAN)) + ". "
        + U(TERR_OLD) + "."),
 moment="Twenty-five past two in the afternoon: the telescope is whole again, and it is about to move.",
 comp=C_DRUM + " " + C_FLOOR + " " + C_STAND + " " + C_TUBE_LEVEL,
 light=LIGHT("14:25", "pm", "summer"),
 tr=TR_A,
 act=("The telescope swings its long tube up between the fork arms from level to straight up in one slow move while a "
      "crew on the scaffold tower watches it, and the crawler crane lowers the empty lifting frame onto the flatbed "
      "truck; the crane carries a visible load. " + CREW),
 tex=T_FIT,
 phys=("The fork mount stays bolted on its round pier, the tube held between its arms. The lifting frame hangs from "
       "the crane hook on two slings. The crawler crane stands on its tracks on the gravel, and the dome rests on its "
       "maintenance stand."),
 mf=("The telescope tips its long tube from level up to straight up between the fork arms and stops in its park "
     "position, and the crawler crane lowers the empty lifting frame from the hook onto the flatbed truck."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The long pale tube rises slowly and "
       "smoothly between the dark fork arms in one single move, from level to pointing straight up above the wall "
       "top, and then it stops and holds still, rigid, in its park position. The crane lowers the empty lifting frame "
       "onto the flatbed truck, which drives off to the left. At the end a second truck brings a curved new copper "
       "shutter up the service road and the crew slings it to the crane. Short shadows fall to the right, and tall "
       "white clouds build slowly far off."))

# ---------- S9 ----------
scene(n=9, st="M", fiil="DEĞİŞTİRİR", eleman="kubbenin eski yeşil kapağı → yeni bakır kapak, aynı kızaklarda (%100) · kapak kapalı", rejim="A", t0="14:35", t1="14:45",
 g="G9",
 stage=(U(TEL_PARK) + "; " + DRUM_NEW + ", " + FLOOR_NEW + ". " + U(DOME_NEW_OLDSHUT) + ", a crew on its walkway. "
        + U(CRANE) + ", with a curved new copper shutter on the hook. A flatbed truck stands on the pad. "
        + U(CRADLE_EMPTY) + ". " + U(TOWERS) + ". " + U(PATH_OLD) + ". "
        + U(STACK(S_IVY, S_COP, S_RAIL, S_FLOOR, S_PAN)) + ". " + U(TERR_OLD) + "."),
 moment="Twenty-five to three in the afternoon: the telescope stands parked, and the new shutter is in the air.",
 comp=C_DRUM + " " + C_STAND + " " + C_SLIT_STAND + " " + C_TUBE_UP,
 light=LIGHT("14:35", "pm", "summer"),
 tr=TR_A,
 act=("A crew on the walkway unbolts the old green shutter and slides it off its runners, the crawler crane lowers it "
      "to the stacking area and then sets the curved new copper shutter onto the same runners, where the crew bolts "
      "it closed; the crane carries a visible load. " + CREW),
 tex=T_FIT,
 phys=("The shutter hangs from the crane hook on two slings. The dome rests on its maintenance stand and the crew "
       "stands on its plank walkway. The telescope stands bolted on its pier inside the drum."),
 mf=("The crawler crane lifts the old green shutter from the slit of the dome to the stacking area and lowers the "
     "curved new copper shutter from the flatbed truck onto the same runners in the slit."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The old green shutter slides off its "
       "runners and swings away to the stacking area on the crane hook, leaving the slit as a dark empty band down "
       "the front-right of the dome; then the new copper shutter swings in from the truck, settles onto the same "
       "runners and slides down to close the slit. The dome is bright new copper from base to crown. The emptied "
       "truck drives off to the left. At the end the crew hooks four slings from the crane to the dome. Short shadows "
       "fall to the right, and tall white clouds drift slowly far off."))

# ---------- S10 ----------
scene(n=10, st="M", fiil="KALDIRIR", eleman="yeni bakır kubbe sehpadan → davulun üstünde, hizalı, ASILI (oturmaz)", rejim="A", t0="14:45", t1="14:55",
 g="G10",
 stage=(U(TEL_PARK) + "; " + DRUM_NEW + ", " + FLOOR_NEW + ". " + U(DOME_NEW_STAND) + ", four slings hooked to it "
        "from the crane. " + U(CRANE) + ". " + U(CRADLE_EMPTY) + ". " + U(TOWERS) + ". " + U(PATH_OLD) + ". "
        + U(STACK(S_IVY, S_COP, S_RAIL, S_FLOOR, S_PAN, S_SHUT)) + ". " + U(TERR_OLD) + "."),
 moment="Quarter to three in the afternoon: the dome is renewed and slung, and the telescope waits in the open drum.",
 comp=C_DRUM + " " + C_STAND + " " + C_SLIT_STAND + " " + C_TUBE_UP,
 light=LIGHT("14:45", "warm", "summer"),
 tr=TR_A,
 act=("The crawler crane lifts the copper dome off its maintenance stand, swings it to the right and holds it level "
      "above the drum, while a crew on the scaffold towers lines it up with taglines and a second crew carries the "
      "walkway planks in bundles to the stacking area; the crane carries a visible load. " + CREW),
 tex=T_FIT,
 phys=("The dome rests on its maintenance stand, four taut slings rising from it to the crane hook. The crawler crane "
       "stands on its tracks on the gravel. The telescope stands bolted on its pier inside the drum."),
 mf=("The crawler crane lifts the copper dome from its maintenance stand on the work pad and carries it on its four "
     "slings to a point a few metres above the drum, where it hangs level and is lined up, not yet set down."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the dome is "
       "already lifting off its stand: the bright copper dome rises slowly on its four slings, swings to the right "
       "over the scaffold towers and stops, hanging level a few metres above the drum, while the crew turns it with "
       "taglines until its slit faces the front-right. Inside the open drum the telescope stands upright beneath it. "
       "The afternoon light slides warm across the copper. The crew carries the walkway planks in bundles to the "
       "stacking area. Short shadows fall to the right, and tall white clouds drift slowly far off."))

# ---------- S11 ----------
scene(n=11, st="M", fiil="OTURTUR", eleman="asılı kubbe → halka raya iner, oturur (%100) · sapanlar boşalır · ⭐ DORUK", rejim="A", t0="14:55", t1="15:05",
 g="G11",
 stage=("the dome is coming home. The copper dome, clad in bright new copper, hangs level on four taut slings from the "
        "hook of the crane a few metres above the drum, lined up with its closed slit on its front-right side; "
        + DRUM_NEW + ". Inside the open drum the telescope stands upright beneath it. " + U(CRANE) + ". "
        + U(STAND_EMPTY) + ", and " + CRADLE_EMPTY + ". " + U(TOWERS) + ". " + U(PATH_OLD) + ". "
        + U(STACK(S_IVY, S_COP, S_RAIL, S_FLOOR, S_PAN, S_SHUT, S_PLANK)) + ". " + U(TERR_OLD) + "."),
 moment="Five to three in the afternoon: the dome hangs over the drum, lined up and ready to come down.",
 comp=(C_DRUM + " The dome hangs above the drum, from about 920 to 1400 pixels from the left, its crown at about "
       "sixty percent of frame height. " + C_SLIT_R),
 light=LIGHT("14:55", "warm", "summer"),
 tr=TR_A,
 act=("The crawler crane lowers the copper dome straight down onto the new ring rail, a crew on the scaffold towers "
      "guides it home with taglines, and a flatbed truck brings pallets of pale stone slabs up the service road; the "
      "crane carries a visible load. " + CREW),
 tex=T_FIT,
 phys=("The dome hangs from the crane hook on four taut slings. The crawler crane stands on its tracks on the gravel. "
       "The ring rail is bolted to the wall top, and the telescope stands bolted on its pier inside the drum."),
 mf=("The crawler crane lowers the copper dome on its four slings from above the drum onto the new steel ring rail on "
     "the wall top, and the slings fall slack."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the dome is "
       "already coming down: the bright copper dome sinks slowly and straight onto the drum in one controlled move, "
       "over the upright telescope, until it sits on the new ring rail — the same size, the same panels, its closed "
       "slit on the front-right side; it does not bounce. The four slings fall slack and the crew unhooks them. A "
       "flatbed truck brings pallets of pale stone slabs up the service road and stops on the pad, and the crew slings "
       "the first pallet to the crane. The warm light glints on the copper; short shadows fall to the right, and "
       "tall white clouds drift slowly far off."))

# ---------- S12 ----------
scene(n=12, st="M", fiil="DÖŞER", eleman="yol + giriş basamakları: çatlak, tekerlek izli → geniş açık taş plakalar (%0 → %100, pedden kapıya)", rejim="A", t0="15:05", t1="15:15",
 g="G12",
 stage=("the dome is back on its drum. " + U(DOME_ON) + "; " + DRUM_NEW + ". " + U(STAND_EMPTY) + ", and "
        + CRADLE_EMPTY + ". " + U(CRANE) + ", with a pallet of stone slabs on the hook. A flatbed truck loaded with "
        "pallets of wide pale stone slabs stands on the pad. " + U(TOWERS) + ". " + U(PATH_OLD) + ". "
        + U(STACK(S_IVY, S_COP, S_RAIL, S_FLOOR, S_PAN, S_SHUT, S_PLANK)) + ". " + U(TERR_OLD) + "."),
 moment="Five past three in the afternoon: the dome is home, and the path to the door is next.",
 comp=(C_DRUM + " " + C_DOME_ON + " " + C_SLIT_R + " The path runs along the front of the drum at about fourteen "
       "percent of frame height."),
 light=LIGHT("15:05", "warm", "summer"),
 tr=TR_A,
 act=("The crawler crane lifts the pallets of stone slabs from the flatbed truck to the path, a crew lifts the cracked "
      "old steps and lays wide pale new slabs and steps from the work pad to the door, and a second crew sets low "
      "dark path lamps beside them; the crane carries a visible load. " + CREW),
 tex=T_PATH,
 phys=("The pallet hangs from the crane hook on four slings. The new slabs rest on a bed of sand along the path. The "
       "crawler crane stands on its tracks on the gravel, and the dome sits on the ring rail on the drum."),
 mf=("The crawler crane carries the pallets of wide pale stone slabs from the flatbed truck to the path, and the crew "
     "lays the slabs and the new steps from the work pad to the door."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Slab by slab from the work pad the "
       "pale new path runs along the front of the drum towards the door, and a flight of new stone steps climbs to "
       "the arched door, a row of low dark path lamps set beside them; the route of the old path stays the same. The "
       "crew carries the cracked old steps in crates to the stacking area. The new copper of the dome dulls slowly "
       "from salmon-pink towards warm brown. The shadows lengthen to the right, and tall white clouds drift slowly "
       "far off."))

# ---------- S13 ----------
scene(n=13, st="M", fiil="ÇEVİRİR", eleman="uçurum terası: açık kenar → yeni çelik korkuluk, modül modül (%0 → %100, davuldan dışa)", rejim="A", t0="15:15", t1="15:25",
 g="G13",
 stage=("the observatory stands whole again. " + U(DOME_ON) + "; " + DRUM_NEW + ". " + U(PATH_NEW) + ". "
        + U(STAND_EMPTY) + ", and " + CRADLE_EMPTY + ". " + U(CRANE) + ", with a bundle of railing modules on the "
        "hook. A flatbed truck loaded with bundles of steel railing modules stands on the pad. " + U(TOWERS) + ". "
        + U(STACK(S_IVY, S_COP, S_RAIL, S_FLOOR, S_PAN, S_SHUT, S_PLANK, S_STEP)) + ". " + U(TERR_OLD) + "."),
 moment="Quarter past three in the afternoon: the path is laid, and the terrace edge is still bare.",
 comp=C_DRUM + " " + C_DOME_ON + " " + C_SLIT_R,
 light=LIGHT("15:15", "warm", "summer"),
 tr=TR_A,
 act=("The crawler crane lifts the bundles of railing modules from the flatbed truck over to the terrace, a crew sets "
      "the modules one after another along the cliff edge and bolts them down, and a second crew carries the empty "
      "bundle straps back to the truck; the crane carries a visible load. " + CREW),
 tex=T_TERR,
 phys=("The bundle hangs from the crane hook on two slings. The railing modules already set are bolted to the paving "
       "at the cliff edge. The crawler crane stands on its tracks on the gravel, and the dome sits on the ring rail."),
 mf=("The crawler crane carries the bundles of steel railing modules from the flatbed truck to the terrace, and the "
     "crew bolts the modules along the cliff edge one after another from the drum outwards."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Module by module a new steel railing "
       "rises along the cliff edge of the terrace, from the foot of the drum out to the far corner, until a "
       "continuous curve of railing frames the sea of cloud below; the outline of the terrace stays the same. The "
       "emptied truck drives off to the left. Warm light lies on the copper, the shadows lengthen to the right, and "
       "tall white clouds drift slowly far off."))

# ---------- S14 ----------
scene(n=14, st="M", fiil="TOPLAR", eleman="iskele kuleleri + sehpa + beşik + eski parça istifi → kamyonlara, gider · gün batımına", rejim="B", t0="15:25", t1="17:25",
 g="G14",
 stage=("the building work is done. " + U(DOME_ON) + "; " + DRUM_NEW + ". " + U(PATH_NEW) + ". " + U(TERR_NEW) + ". "
        + U(CRANE) + ", with a bundle of scaffold planks on the hook. " + U(TOWERS) + ". The empty maintenance stand "
        "and the empty cradle stand on the pad beside the full stacking area, and two flatbed trucks wait on the pad."),
 moment="Twenty-five past three in the afternoon: the building work is done, and the site is about to be cleared.",
 comp=C_DRUM + " " + C_DOME_ON + " " + C_SLIT_R,
 light=LIGHT("15:25", "warm", "autumn"),
 tr=TR_B,
 act=("A crew strips the two scaffold towers plank by plank, the crawler crane lifts the bundles of planks, the "
      "maintenance stand, the cradle and the crates of old parts onto the two flatbed trucks, and the trucks carry "
      "them away down the service road one after another; the crane carries a visible load. " + CREW),
 tex=T_TERR,
 phys=("The bundle hangs from the crane hook on two slings. The scaffold towers stand on timber pads against the drum. "
       "The crawler crane stands on its tracks on the gravel, and the dome sits on the ring rail on the drum."),
 mf=("The crew dismantles the two scaffold towers, and the crawler crane lifts the bundles of planks, the maintenance "
     "stand, the cradle and the crates of old parts from the work pad onto the flatbed trucks, which carry them away."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. The two scaffold towers come down "
       "level by level and their planks go onto the trucks in bundles; the crane lifts the empty maintenance stand, "
       "the empty cradle and the crates of old parts onto the trucks, which drive off to the left one after another "
       "and come back empty, until the work pad is bare. The front of the drum and the copper dome stand clear. The "
       "sun sinks behind the camera on the left: the warm light climbs up the dome, lingers on its crown and leaves "
       "it, and the sea of cloud turns pink. Clouds streak across the sky and thin out. At the end the crane raises "
       "its boom steeply until its tip and its line rise above the top edge of the frame."))

# ---------- S15 ----------
scene(n=15, st="M", fiil="AYRILIR", eleman="vinç bomunu servis yoluna yatırır, sola çıkar · saha iş makinesiz · yol lambaları belli belirsiz yanar", rejim="A", t0="17:25", t1="17:35",
 g="G15",
 stage=("the restoration is finished. " + U(DOME_ON) + "; " + DRUM_NEW + ". " + U(PATH_NEW) + ". " + U(TERR_NEW)
        + ". " + U(CRANE_UP) + ". The work pad is cleared to bare gravel, and a crew stands by the crane with rakes."),
 moment="Twenty-five past five in the evening, the sun on the horizon: only the crane is left.",
 comp=C_DRUM + " " + C_DOME_ON + " " + C_SLIT_R,
 light=LIGHT("17:25", "sunset", "autumn"),
 tr=TR_A,
 act=("The crawler crane lowers its long boom flat along the service road and crawls away to the left, a crew rakes "
      "the gravel of the work pad smooth and walks off behind it, and a small truck carries the last crates of tools "
      "away. " + CREW),
 tex=T_FINISH,
 phys=("The crawler crane stands on its tracks on the gravel. The dome sits on the ring rail on the drum, and the "
       "railing posts are bolted to the paving at the cliff edge. The path lamps stand on the path."),
 mf=("The crawler crane lowers its boom from the sky onto its rest along the service road and crawls away down the "
     "road out of the frame on the left; a small truck carries the last crates of tools from the work pad away."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The long boom of the crane comes "
       "slowly down out of the sky until it lies flat along the service road, and the crane crawls away to the left "
       "and out of the frame. A small truck carries the last crates of tools away behind it, and the crew rakes the "
       "gravel of the work pad smooth and walks off. For the first time the finished observatory stands without a "
       "machine beside it, and the low path lamps along the new steps begin to glow faintly. The sky fades from pale "
       "gold to early blue, the sea of cloud turns from pink to grey-blue, and a few thin high clouds drift slowly "
       "from the right."))

# ---------- S16 ----------
scene(n=16, st="M", fiil="AÇAR", eleman="tek gözlem kapağı kapalı → kızakta kubbenin tepesine kayar, yarık açık (%100) · kırmızı ışık · teleskop silueti", rejim="A", t0="17:35", t1="17:45",
 g="G16", nxt="G18", iso=800,
 stage=("the restoration is finished. " + U(DOME_ON) + "; " + DRUM_NEW + ". " + U(PATH_LIT) + ". " + U(TERR_NEW)
        + ". The work pad is raked clean and empty, and a small dark service vehicle with two people in it comes up "
        "the service road at the left edge."),
 moment="Twenty-five to six in the evening, early blue hour: the site is clear and the dome is still shut.",
 comp=C_DRUM + " " + C_DOME_ON + " " + C_SLIT_R,
 light=LIGHT("17:35", "dusk", "autumn"),
 tr=TR_A,
 act=("The small service vehicle drives up to the work pad, a crew of two lifts a small crate from it and carries it "
      "up the new steps in at the door, and the single copper shutter on the front-right of the dome begins to slide "
      "up its runners towards the crown. " + CREW),
 tex=T_EVE,
 phys=("The service vehicle stands on its wheels on the gravel. The dome sits on the ring rail on the drum, its "
       "shutter seated in its runners. The railing posts are bolted to the paving at the cliff edge."),
 mf=("The single copper shutter slides up from the base of the slit over the crown on its runners, a dim red light "
     "shows inside, and the telescope on its pier swings the end of its tube down into the open slit; two people carry "
     "a small crate from the service vehicle to the door."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The small service vehicle drives up "
       "the service road onto the pad, and two people carry a small crate from it up the new steps and in at the "
       "arched door. Then the single copper shutter on the front-right of the dome slides slowly up its runners and "
       "over the crown, and the slit opens from its base to the crown as a tall dark band with a dim red light "
       "inside; the dark outline of the telescope shows in it, and the end of the pale tube swings down into the slit "
       "and stops, pointing out to the south. The sky deepens to blue and the sea of cloud below turns pale "
       "grey-blue, and a few thin high clouds drift slowly from the right."))

# ---------- S17 (KUBBE İSTASYONU · ∥ S16'nın son 8 sn) ----------
scene(n=17, st="S", fiil="YÖNELİR", eleman="kubbe içi: teleskop son salınımı · yarığa hizalı durur · büyük ekran KARANLIK (görüntü sonradan bindirilir)", rejim="G", t0="17:45", t1="17:45",
 g="G17", nxt="G17′", iso=1600,
 stage=("the observatory is restored and working: the dark grey fork mount on its round concrete pier holds the long "
        "pale white tube, swinging slowly down towards the open slit; the single copper shutter is slid fully back "
        "over the crown, and the slit is a tall straight band of deep blue sky from the wall top to the crown. A large "
        "dark flat screen on a low desk fills the left foreground, its blank face turned towards the camera, and two "
        "people sit at the right end of the desk, backs to the camera, dark silhouettes, no readable faces. The pale "
        "new floor panels run round the pier, three low red work lamps stand along the inner wall, and a short step "
        "ladder leans on the pier."),
 moment="Quarter to six in the evening, blue hour: the shutter is open and the telescope turns to the sky.",
 light=("LIGHTING: " + sunline("17:45") + ", " + LIGHT_DESC["in_dusk"] + " " + SEASON["autumn"] + " The sun stays "
        "outside the frame."),
 act=("The telescope finishes its slow swing between the fork arms and stops, the crew of two at the desk sets a "
      "small notebook on the desk and leans towards the dark screen, backs to the camera, no readable faces, and the "
      "red work lamps burn steadily."),
 tex=T_DOME,
 phys=("The fork mount stands bolted on the round concrete pier, the tube held between its arms. The desk stands on "
       "its legs on the floor, and the screen sits on the desk. The red lamps rest on the floor along the wall."),
 mf=("The long pale white tube swings slowly down from high in the slit to its lower end and comes to rest pointing "
     "out through the open slit; one of the two people at the desk takes a small notebook from a stack on the shelf "
     "and sets it on the desk, and nothing on the terrace or the stone slabs outside changes."),
 body=("Eight seconds pass in real time. Everything in this shot moves at natural speed. From the first frame the "
       "telescope is already turning: in the first three seconds the long white tube swings smoothly down between "
       "the dark arms of the fork, a dim red sheen sliding along it, and comes to rest pointing out through the slit "
       "towards the deep blue sky; from three to eight seconds the telescope stands still. One of the two people at "
       "the desk takes a small notebook from a stack on the shelf, sets it on the desk and both lean towards the "
       "large dark blank screen, backs to the camera. The deep blue sky in the slit holds still."))

DOME_SON = {17: dict(g="G17′",
 stage=("the observatory is restored and working: the dark grey fork mount on its round concrete pier holds the long "
        "pale white tube at rest, pointing out through the lower part of the open slit towards the deep blue sky; "
        "the single copper shutter is slid fully back over the crown, and the slit is a tall straight band of deep "
        "blue sky from the wall top to the crown. A large dark flat screen on a low desk fills the left foreground, "
        "its blank face turned towards the camera, and two people sit at the right end of the desk, leaning towards "
        "the screen, backs to the camera, dark silhouettes, no readable faces. The pale new floor panels run round "
        "the pier, three low red work lamps stand along the inner wall, and a short step ladder leans on the pier."),
 moment="Quarter to six in the evening, blue hour: the telescope points out through the open slit.",
 light=("LIGHTING: " + sunline("17:45") + ", " + LIGHT_DESC["in_dusk"] + " " + SEASON["autumn"] + " The sun stays "
        "outside the frame."),
 act=("The telescope stands still, aligned with the slit; the two people at the desk lean towards the dark screen, "
      "backs to the camera, no readable faces; the red work lamps burn steadily."),
 tex=T_DOME,
 phys=("The fork mount stands bolted on the round concrete pier, the tube held between its arms. The desk stands on "
       "its legs on the floor, and the screen sits on the desk. The red lamps rest on the floor along the wall."))}

# ---------- S18 ----------
scene(n=18, st="M", fiil="DÖNER", eleman="kubbe halkada ≈30° döner: açık yarık sağ önden → kameraya bakan ön yüze · teleskop izler · ilk yıldızlar", rejim="A", t0="17:45", t1="17:55",
 g="G18", iso=800,
 stage=("the restoration is finished. The copper dome sits on the ring rail on top of the drum, its single shutter "
        "slid back over the crown, so the slit on its front-right side stands open from its base to the crown as a "
        "tall dark band with a dim red light inside, the end of the pale telescope tube pointing out of it; "
        + DRUM_NEW + ". " + U(PATH_LIT) + ". " + U(TERR_NEW) + ". The small dark service vehicle stands on the raked "
        "work pad, and two people stand at the foot of the steps."),
 moment="Quarter to six in the evening, blue hour: the slit is open and the telescope looks out to the south.",
 comp=C_DRUM + " " + C_DOME_ON + " " + C_SLIT_R,
 light=LIGHT("17:45", "dusk", "autumn"),
 tr=TR_A,
 act=("The dome turns slowly on its ring rail, carrying the open slit round from the front-right of the dome to its "
      "front, the telescope follows inside, and a crew of two lifts a second small crate from the service vehicle and "
      "carries it to the door. " + CREW),
 tex=T_DUSK,
 phys=("The dome sits on the ring rail on the drum, its shutter seated back in its runners. The service vehicle "
       "stands on its wheels on the gravel. The railing posts are bolted to the paving at the cliff edge."),
 mf=("The copper dome turns on its steel ring rail from the right towards the camera, about thirty degrees, and the "
     "open slit swings from the front-right of the dome to the middle of its face, with the telescope following "
     "inside; two people carry a small crate from the service vehicle to the door."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The whole copper dome turns slowly "
       "and smoothly on its ring rail, the drum below it standing still: the open slit glides round from the "
       "front-right of the dome to the middle of its face until it looks straight at the camera, a tall band of dim "
       "red light with the pale tube of the telescope inside it, tilted up to the sky. The panel seams of the dome "
       "slide past steadily as it turns, and then it stops. Two people carry a small crate from the vehicle up the "
       "steps to the door. The sky deepens to a dark clear blue and the first bright stars come out, and the sea of "
       "cloud below rolls slowly, pale blue-grey."))

# ---------- S19 ----------
scene(n=19, st="M", fiil="GÖZLER", eleman="eklenen yok · iki kişi terasa yürür, korkulukta durur · servis aracı gider · bulut denizi akar · TUTUŞ", rejim="A", t0="17:55", t1="18:05",
 g="G19", iso=800,
 stage=("the restoration is finished. The copper dome sits on the ring rail on top of the drum, its slit standing "
        "open in the middle of its face, turned towards the camera: a tall band of dim red light from the base to the "
        "crown, with the pale white tube of the telescope inside it, tilted up to the sky; " + DRUM_NEW + ". "
        + U(PATH_LIT) + ". " + U(TERR_NEW) + ". The small dark service vehicle stands on the raked work pad, and two "
        "people stand at the door, small dark figures seen from afar, no readable faces."),
 moment="Five to six in the evening, deep blue hour: the observatory looks at the sky again.",
 comp=(C_DRUM + " " + C_DOME_ON + " " + C_SLIT_C + " The two people stand at the door at about 1200 pixels from the "
       "left, about thirty-five pixels tall."),
 light=LIGHT("17:55", "blue", "autumn"),
 tr=TR_A,
 act=("A crew of two pulls the arched door shut behind them and walks across the terrace to the new railing at the "
      "cliff edge, the small service vehicle drives slowly down the service road and out of the frame on the left, "
      "and the dim red light in the slit holds steady. People register only as faint soft motion streaks while they "
      "walk; standing still they are small dark figures, no readable faces."),
 tex=T_DUSK,
 phys=("The dome sits on the ring rail on the drum. The railing posts are bolted to the paving at the cliff edge, "
       "and the two people stand on the paving. The service vehicle stands on its wheels on the gravel."),
 mf=("Two people walk from the arched door across the terrace to the railing at the cliff edge and stop there, the "
     "service vehicle drives from the work pad down the service road out of the frame, and the sea of cloud flows "
     "slowly from the right to the left below the summit."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. In the first half two people walk "
       "slowly from the door across the terrace to the new railing at the cliff edge, faint soft figures, and stop "
       "there, and the small service vehicle drives down the service road and out of the frame on the left; from the "
       "middle of the shot to the end nothing else changes — the dome stands still with its slit open towards the "
       "camera, the dim red light holds steady inside it, the two small figures stand still at the railing. Far "
       "below, the sea of cloud flows slowly from the right to the left, and the stars brighten in the deep blue "
       "sky."))

USTA = dict(g="G20", t="18:05",
 stage=("everything is finished. The copper dome sits on the ring rail on top of the drum, its slit standing open in "
        "the middle of its face, turned towards the camera: a tall band of dim red light from the base to the crown, "
        "with the pale white tube of the telescope inside it, tilted up to the sky; " + DRUM_NEW + ". " + U(PATH_LIT)
        + ". " + U(TERR_NEW) + ". Two people stand still at the railing at the cliff edge, small dark figures "
        "against the sea of cloud, no readable faces; the work pad lies raked clean and empty."),
 moment="Five past six in the evening, deep blue hour, autumn: the restored observatory looks at the sky.",
 comp=(C_DRUM + " " + C_DOME_ON + " " + C_SLIT_C + " The two people stand at the railing at about 1600 pixels from "
       "the left, about thirty pixels tall."),
 light=LIGHT("18:05", "blue", "autumn"),
 tr=TR_A,
 act=("The two people stand still at the railing; the dim red light holds steady in the open slit and the sea of "
      "cloud lies calm below. People register only as faint soft motion streaks while they walk; standing still they "
      "are small dark figures, no readable faces."),
 tex=T_DUSK,
 phys=("The dome sits on the ring rail on the drum, its shutter seated back in its runners. The railing posts are "
       "bolted to the paving at the cliff edge, and the two people stand on the paving."))

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

def gorsel_dome(d, head, iso):
    return "\n".join([
        head, lens(iso), CAM_DOME, "",
        STRUCT + " AT THIS STAGE: " + d["stage"], "",
        SITE_DOME, "",
        "THE TIME MOMENT: " + d["moment"], "",
        COMP_DOME, "",
        d["light"], "",
        TR_G_IN, "",
        "ACTIVITY: " + d["act"], "",
        "SITE TEXTURE: " + d["tex"], "",
        "PHYSICS: " + d["phys"], "",
        NEG_DOME, OUTPUT])

def i2v(d):
    lock = (STAGE_DOME + " " + LOCK_DOME) if d["st"] == "S" else LOCK_MAIN
    tail = I2V_TAIL_DOME if d["st"] == "S" else I2V_TAIL
    return "\n\n".join([I2V_HEAD, "MOTION FOCUS: " + d["mf"], d["body"], lock, tail])

RJ = {"A": "A (10 dk)", "B": "B (2 sa)", "G": "G (gerçek zaman · 8 sn)"}
def blok(d):
    n = d["n"]; bas, son = n * 8, (n + 1) * 8
    ist = "KUBBE (ikinci istasyon · 1/1)" if d["st"] == "S" else "MAIN"
    saat = f"{d['t0']}→{d['t1']}" if d["rejim"] != "G" else f"{d['t0']} (+8 sn)"
    hedef = d.get("nxt", f"G{n+1}")
    out = [f"## 🎬 SAHNE {n} — {d['fiil']}", "",
           "```",
           f"SÜRE: 8,0 s ({bas},0–{son},0)  ·  ELEMAN + ARA HÂL: {d['eleman']}  ·  REJİM: {RJ[d['rejim']]}  ·  SAAT: {saat}  ·  İSTASYON: {ist}",
           "```", ""]
    if n == 16:
        out += ["> ⭐ **Bu klibin hedefi ana kare G18'dir** (G17 iç kliptir): S16 G16 → G18 koşar, S17 kubbe içinde",
                "> G17 → G17′ koşar (S16'nın SON sekiz saniyesi, gerçek hız), S18 yine G18'den başlar. Dış kare iki",
                "> yakada AYNIDIR (ISTASYON_VE_IC_MEKAN §0 ③).", ""]
    if n in (10, 11):
        out += ["> ⭐ **S10 + S11 TEK OLAYDIR** (sahip: \"16 saniyelik tek olay iki klibe bölünür\"): G11'de kubbe davulun",
                "> üstünde, hizalı ve ASILI; yüksekliği, yönü, sapanları ve ışığı iki klipte aynı kare (DERS 52).", ""]
    if d["st"] == "S":
        out += ["> 🔭 **KUBBE KLİBİ** — ana zincirin DIŞINDA: S16'nın SON sekiz saniyesi, içeriden, gerçek hızda "
                "(hikâye SAPMA ⑤). S16'nın I2V'si ana kare G18'e biter · bu klip G17 → G17′ (kubbe) · S18 yine G18'den "
                "başlar. Dış kare iki yakada AYNIDIR; yarıktan görünen gök bu sekiz saniyede değişmez.", "",
                "> 🖥️ **EKRAN BİNDİRMESİ** — masadaki büyük ekran üretimde KARANLIK ve BOŞ kalır; gözlem görüntüsü "
                "kurguda ekrana yerleştirilir (sabit kamera · dört köşe takibi, 139,0 sn'den sonra). Promptta gözlem "
                "görüntüsünün adı GEÇMEZ (PLAN YASAK KELİME).", "",
                f"### 📸 GÖRSEL PROMPT ({d['g']} · KUBBE İLK KARE)", "", "```",
                gorsel_dome(d, HEAD_DOME.format(n=n), d.get("iso", 1600)), "```", ""]
    else:
        out += [f"### 📸 GÖRSEL PROMPT ({d['g']})", "", "```", gorsel_main(d, HEAD_MAIN.format(n=n)), "```", ""]
    out += [f"### 🎥 I2V PROMPT ({d['g']} → {hedef})", "", "```", i2v(d), "```", ""]
    if d["st"] == "S":
        c = DOME_SON[n]
        out += [f"### 🔭 KUBBE SON KARESİ ({c['g']} · bu klibin hedefi — sahne görseli DEĞİL, kapı saymaz)", "",
                "> Kapı bu bloğu saymaz (başlıkta GÖRSEL PROMPT yok) — ama aynı disiplinle yazıldı: STRUCTURE,",
                "> SITE / BACKGROUND, NEGATIVE kubbe karelerinde birebir. Üretimde G17′ ÖNCE üretilir (ana G18'in",
                "> ışığıyla), G17 ondan (tüp yarığın yukarısında, salınımın başında).", "",
                "```", gorsel_dome(c, HEAD_DOME_SON.format(n=n), 1600), "```", ""]
    out += ["---", ""]
    return "\n".join(out)

def usta_blok():
    d = USTA
    return "\n".join([
        "## 🌟 USTA KARE — G20 (SAHNE DEĞİLDİR · son klibin hedefi · kapak kaynağı)", "",
        "> Üretim sırasının İLK karesi [§8]: G20 önce üretilir ve ikna edici değilse DURULUR; sonra",
        "> image-to-image geriye G19 → G18 → G16 → … → G0 (G17/G17′ kubbe içi ayrıca, G18'in ışığıyla).",
        "> Kapı: final hiyerarşisi (PLAN) bu sırayla okunuyor mu · kameraya bakan açık yarık ve içindeki kırmızı",
        "> ışık · teleskop tüpü yarıkta · kanıt nesnesi çam x 1652–1805 / 150 px · vinç, iskele, sehpa, beşik YOK",
        "> (SÖKÜM satırı) · koyu mavi saat, güneş −9° · korkulukta iki küçük figür. Kapak",
        "> (`THE_FIRST_LIGHT_KAPAK.md`) bu promptun kopyası + başlık bandı satırıdır [MUZIK_VE_KAPAK §2.2].", "",
        "### 📸 USTA KARE PROMPT (G20)", "", "```",
        gorsel_main(dict(d, iso=800), HEAD_USTA), "```", ""])

H1 = f"""# 🎬 {FILM} — BÖLÜM 1  (S0 – S9 · G0 … G9 + 10 I2V · 0,0–80,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `{FILM}_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır. STRUCTURE bloğu bütün promptlarda, SITE / BACKGROUND ve NEGATIVE blokları kendi
> istasyonlarının bütün karelerinde BİREBİR aynı kelimelerle tekrarlanır; değişen AT THIS STAGE,
> THE TIME MOMENT, COMPOSITION'ın son cümleleri, LIGHTING, TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.
>
> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py`)
> ki ortak bloklar harfi harfine aynı kalsın [DERS 20].
>
> ⭐ Bu bölümün SON I2V'si (S9: G9 → G10) **G10 karesinde biter** ve G10 `BOLUM_2`'nin ilk görselidir:
> bölüm sınırı bir KAREDİR, kesme değil [DERS 52]. Kapı KLASÖR MODUNDA koşulur:
> `python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/{FILM}`.
>
> ⛔ Vinç kancası [DERS 8]: her karede ya YÜKLÜ ("carries a visible load" / "with a … on the hook") ya da bom
> ucu KADRAJ DIŞINDA (G2 · G15 — "its tip rises above the top edge of the frame"); boş kanca hiçbir promptta yazılmaz.
>
> ⛔ Kelime kilitleri: "crane" yalnız G0–G15 ve S0–S15 I2V'lerinde; "glow"/"lit" yalnız S15 I2V'sinden ve
> G16'dan sonra; "red light" yalnız S16 I2V'sinden, G17'den sonra; "stars" yalnız S18 I2V'sinden ve G19'dan
> sonra; yarık için "open" yalnız S16 I2V'sinden sonra; YASAK KELİME (PLAN künyesi) hiçbir promptta yok —
> negatifte bile.

---
"""

H2 = f"""# 🎬 {FILM} — BÖLÜM 2  (S10 – S19 · G10 … G19 + G17/G17′ kubbe + 10 I2V · 80,0–160,0 sn) + ⭐ USTA KARE G20

> Bölüm 1 ile aynı kurallar: **yalnız sahne blokları**, her prompt self-contained, STRUCTURE ve
> SITE / BACKGROUND birebir, blok etiketleri birebir [DERS 20].
>
> ⛔ **Bölüm 2 "devamı" değildir, ikinci yarıdır.** "Bölüm 1'deki gibi" atfı yasak; model bu
> dosyayı tek başına okuyor. İLK görsel **G10** bölüm 1'in son I2V'sinin HEDEF karesidir — aynı
> kare, iki dosyada bir kez yazılır (burada); bölüm 1'in S9 I2V'si onu "second provided image" olarak alır.
>
> ⭐ **S10 + S11 tek olaydır** (kubbe kalkar → hizalanır → oturur): G11 iki klibin ortak karesidir.
>
> 🔭 **S17 KUBBE KLİBİDİR** (tek ikinci istasyon): S16'nın I2V'si ana kare **G18**'e biter, S17 kubbe
> içinde G17 → G17′ koşar (S16'nın son sekiz saniyesi, gerçek hız), S18 yine G18'den başlar. Kubbe
> karelerinin SITE bloğu ana SITE ile TAŞ ÖRGÜSÜ cümlesini BİREBİR paylaşır [DERS 10]. Ekran KARANLIK
> üretilir; gözlem görüntüsü kurguda bindirilir.
>
> ⭐ **USTA KARE G20 bu dosyanın sonunda, kendi `## 🌟 USTA KARE` bölümündedir** — sahne
> değildir, son klibin (S19: G19 → G20) hedef karesidir ve kapak kaynağıdır.
>
> ⭐ S19'un ikinci yarısı TUTUŞTUR (final kanıtı 156,0–160,0); insan kuralı "no readable faces".

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

if "--kadraj" in sys.argv:
    for ad, y, d in [("davul dibi (ön)", 0, 52), ("davul duvar tepesi (ön) +4", 4, 52), ("davul duvar tepesi (arka)", 4, 76),
                     ("iç zemin (arka)", 0, 76), ("iç zemin (kaide)", 0, 64), ("kaide üstü +2", 2, 64),
                     ("çatal kolu tepesi +6,5", 6.5, 64), ("tüp yatay +5,5", 5.5, 64), ("tüp dik tepe +12", 12, 64),
                     ("kubbe tepesi +16 (davulda)", 16, 64), ("kubbe tabanı +7 (G11 asılı)", 7, 64),
                     ("kubbe tepesi +19 (G11 asılı)", 19, 64), ("kubbe tepesi +13,5 (sehpada)", 13.5, 62),
                     ("havadaki kubbe tepesi +18 (G0)", 18, 63), ("kapı tepesi +3", 3, 52), ("yol (d 49)", 0, 49),
                     ("çam tepesi +16", 16, 50), ("çam dibi +2", 2, 50), ("beşik üstü +2", 2, 50),
                     ("iskele kulesi tepesi +7", 7, 58), ("teras ön kenarı", 0, 56), ("korkuluk (arka) +1", 1, 72),
                     ("vinç tabanı", 0, 84), ("istif tepesi +2 (d 50)", 2, 50)]:
        p = yv(y, d)
        print(f"{ad:32s} %{p:5.1f}  (üstten {round(1080 * (1 - p / 100))})")
    print("ufuk", round(50 + 24 * math.tan(math.radians(TILT)) / 0.2025, 1))
    for ad, x, d in [("davul sol", -2, 64), ("davul sağ", 22, 64), ("sehpada kubbe sol", -28, 62), ("sehpada kubbe sağ", -4, 62),
                     ("G0 kubbe sol", -12, 63), ("G0 kubbe sağ", 12, 63), ("beşik sol", -32, 50), ("beşik sağ", -23, 50),
                     ("çam sol", 27, 50), ("çam sağ", 33, 50), ("kapı sol", 8.75, 52), ("kapı sağ", 11.25, 52),
                     ("tüp dik sol", 8.8, 64), ("tüp dik sağ", 11.2, 64), ("tüp yatay sol", 5.5, 64), ("tüp yatay sağ", 14.5, 64),
                     ("kule sol a", -4, 58), ("kule sol b", -1, 58), ("kule sağ a", 21, 58), ("kule sağ b", 24, 58),
                     ("teras sol", 23, 56), ("teras sağ", 38, 56), ("istif sol", -14, 50), ("istif sağ", -8, 50), ("vinç", -3, 84)]:
        print(f"{ad:20s} x {px(x, d)}")
    # yarık: kubbe ekseni (10, 64) · R 12 · kameraya bakan yön 189° · θ derece SAĞA (doğuya) döner
    for ad, cx, cd, y0, th in [("yarık davulda önde", 10, 64, 4, 0), ("yarık davulda sağ önde", 10, 64, 4, 30),
                               ("yarık sehpada sağ önde", -16, 62, 1.5, 30)]:
        b0 = math.atan2(-cx, -cd) - math.radians(th)
        for el in (0, 45):
            r = 12 * math.cos(math.radians(el)); X = cx + r * math.sin(b0); D = cd + r * math.cos(b0)
            print(f"{ad:24s} yükseklik {el:2d}° → x {px(X, D)} · %{yv(y0 + 12 * math.sin(math.radians(el)), D):.1f} · yön {math.degrees(b0) % 360:.0f}°")
    sys.exit(0)

b1 = H1 + "\n" + "\n".join(blok(d) for d in S if d["n"] <= B1_SON)
b2 = H2 + "\n" + "\n".join(blok(d) for d in S if d["n"] > B1_SON) + "\n" + usta_blok()
open(os.path.join(OUT, f"{FILM}_BOLUM_1.md"), "w").write(b1)
open(os.path.join(OUT, f"{FILM}_BOLUM_2.md"), "w").write(b2)
print("yazıldı", len(b1), len(b2))
