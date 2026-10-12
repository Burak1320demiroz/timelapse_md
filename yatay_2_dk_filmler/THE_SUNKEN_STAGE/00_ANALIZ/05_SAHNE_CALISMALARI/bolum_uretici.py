# THE SUNKEN STAGE — bölüm dosyası üretici (ortak bloklar tek kaynaktan, DERS 20)
# KULLANIM (depo kökünden):
#   python3 yatay_2_dk_filmler/THE_SUNKEN_STAGE/00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py yatay_2_dk_filmler/THE_SUNKEN_STAGE
#   → THE_SUNKEN_STAGE_BOLUM_1.md + _BOLUM_2.md yeniden yazılır; ardından prompt_kontrol.py klasör modunda koşulur.
#   --tablo  → PLAN kare tablosu satırlarını basar (saat · azimut · yükseklik · kadrajda gölge yönü)
#   --kadraj → PLAN DEĞİŞMEZLER px satırlarını basar (iğne deliği izdüşümü, 16 mm, tilt 27°)
# ⛔ ÜRETİM BAŞLADIKTAN SONRA KOŞULMAZ: üretilmiş filmin promptu kanıttır (URETIM_GUNLUGU kuralı).
# ⛔ Bölüm dosyası elle düzeltilirse bu betik o düzeltmeyi EZER — düzeltme önce buraya yazılır.
# Kalıp: TEK istasyon (20/20 klip ana kamera), bölüm sınırı G10. Sahibin S01–S20'si = depo S0–S19.
# Rejim: A (10 dk) · B (2 sa: S4 yıkama · S6 ahşap oturma · S10 bakır kabuk) · G (8 sn gerçek zaman: S18 · S19 — final).
import math, os, sys

FILM = "THE_SUNKEN_STAGE"
OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
N_SAHNE = 20
B1_SON = 9          # BOLUM_1 = S0–S9 · BOLUM_2 = S10–S19 + USTA (sınır G10)
BEARING = 15        # kamera bakışı (KKD) — tiyatronun ekseni boyunca sahneye

# ── güneş (47° K · δ −9° · ekim ortası · güneş saati) ───────────────────────
phi, dec = math.radians(47.0), math.radians(-9.0)
def sun(t):
    h = math.radians((t - 12) * 15)
    se = math.sin(phi) * math.sin(dec) + math.cos(phi) * math.cos(dec) * math.cos(h)
    e = math.degrees(math.asin(se))
    az = (math.degrees(math.atan2(math.sin(h), math.cos(h) * math.sin(phi) - math.tan(dec) * math.cos(phi))) + 180) % 360
    return round(az), e
def hm(s):
    p = s.split(":"); return int(p[0]) + int(p[1]) / 60 + (int(p[2]) / 3600 if len(p) > 2 else 0)
def sunline(t):
    az, e = sun(hm(t))
    if e >= 0.5:
        return f"Sun azimuth {az} degrees, elevation {round(e)} degrees"
    if e > -0.5:
        return f"Sun azimuth {az} degrees, elevation 0 degrees, on the horizon"
    return f"Sun azimuth {az} degrees, elevation {round(-e)} degrees below the horizon"

# ── kadraj (iğne deliği · 16 mm · 36 × 20,25 mm · 1920 × 1080 → f = 853 px) ─
# Dünya: O = orkestra zemininin merkezi (z 0). +y sahneye doğru (kameradan ileri), x sağa, z yukarı (m).
# Teraslar: k = 1…12, ön kenar yarıçapı 16 + 1,2·(k−1), basamak yüksekliği 0,6 → 12. teras üstü +7,2, dış kenar 30,4.
# Yarım daire φ −90…+90 (φ 0 = kameraya doğru). Üç merdiven φ −30 · 0 · +30. Sahne platformu x ±13, y −3…+10, üstü +1,2.
# Kamera (0, −44, +22), tilt 27° aşağı, eksen üstünde (simetrik).
F_PX = 16 / 36 * 1920
CAM_H, CAM_D, TILT = 22.0, 44.0, 27.0
def proj(P):
    x, y, z = P[0], P[1] + CAM_D, P[2] - CAM_H; t = math.radians(TILT)
    Zc = y * math.cos(t) - z * math.sin(t); Yc = y * math.sin(t) + z * math.cos(t)
    return round(960 + F_PX * x / Zc), round(540 - F_PX * Yc / Zc)
def pol(r, ph, z):
    a = math.radians(ph); return (r * math.sin(a), -r * math.cos(a), z)
def pct(y): return round(100 * (1 - y / 1080))
UFUK = round(540 - F_PX * math.tan(math.radians(TILT)))
def RIMR(k): return 16 + 1.2 * (k - 1)            # k. terasın ön kenarı
def WL(L):                                        # su çizgisinin dokunduğu terasın ön kenarı (kot L)
    k = int(L // 0.6) + 1; return k, RIMR(k)

# ── ortak bloklar ───────────────────────────────────────────────────────────
HEAD_MAIN = ("Photorealistic documentary site photograph — Scene {n} of 20. Horizontal 16:9 time-lapse of a flooded "
             "open-air theatre in a forest hollow being drained, restored and opened, from a fixed 16 mm site camera.")
HEAD_USTA = ("Photorealistic documentary site photograph — master frame G20, the target frame of the last shot "
             "(Scene 19 of 20). Horizontal 16:9 time-lapse of a restored open-air theatre in a forest hollow on its "
             "opening evening; a photograph from a fixed 16 mm site camera.")
CAM_MAIN = ("Camera: MAIN STATION — fixed tripod bolted to a rock outcrop on the ridge above the near rim of the "
            "theatre, lens 22 metres above the orchestra floor, 44 metres from the centre of the orchestra, bearing 15 "
            "degrees, tilt 27 degrees down, zero roll, on the axis of the theatre. The camera never moves.")
STRUCT = ("STRUCTURE: When finished this will be a restored open-air theatre in a forest hollow: twelve broad concentric "
          "semicircular stone seating terraces with timber seat boards and three radial stone stair aisles around a "
          "level orchestra floor, a timber stage on the original rectangular stone stage platform, a fan-shaped "
          "acoustic shell over the rear third of the stage, two compact technical towers flanking the stage, and two "
          "paved audience paths.")
SITE_MAIN = ("SITE / BACKGROUND: A deep hollow in a mixed autumn forest of gold, orange and rust-coloured trees, seen "
             "from a rocky ridge above the near rim of the theatre. The theatre fills the floor of the hollow; behind "
             "the stage platform a steep grassy bank rises to a low dry-stone wall, and beyond it the forested slope "
             "climbs to a level treeline against the sky. Upper left, on the slope, stands one large pale rock split "
             "from top to bottom by a dark crack. Upper right, two tall dark green pines rise above the treeline. A "
             "gravel service road enters from the left edge and runs down across the left slope to a gravel hardstand "
             "beside the left end of the stage platform.")
NEG_MAIN = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The hollow, the forest, the split "
            "rock, the two pines, the back wall and the service road never change shape, position, size or spacing. "
            "The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair "
            "aisles. Nothing already built is removed or resized; no opacity fades. No readable text, letters, "
            "digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, "
            "labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural "
            "visualisation look, no CGI aesthetic.")
OUTPUT = "Output: 16:9, 4K, no text, no watermark."
CREW = ("Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never "
        "sharp, no readable faces.")
CREW_B = "Dozens of workers in orange work clothes show only as faint soft motion streaks, never as sharp figures."
CROWD_A = ("People show as faint soft motion streaks while they walk and as small still seated figures once seated, "
           "backs to the camera, no readable faces.")
CROWD_G = ("People are small distant figures, the audience seated with their backs to the camera, the musicians far "
           "away on the stage, no readable faces.")
FILMSTOCK = "A documentary site photograph on colour negative film, true colour, fine grain."

# kadraj sayıları (betik hesaplar; PLAN DEĞİŞMEZLER bu çıktıyı yazar)
_rkL, _rkR, _rkT = proj((-69, 52, 18)), proj((-59, 52, 18)), proj((-64, 52, 23))
_rimL, _rimR, _rimC = proj(pol(30.4, -60, 7.2)), proj(pol(30.4, 60, 7.2)), proj(pol(30.4, 0, 7.2))
_sFL, _sFR = proj((-13, -3, 1.2)), proj((13, -3, 1.2))
_tree = proj((0, 200, 22))
COMP_HEAD = (f"COMPOSITION: Horizontal 16:9, the camera looking down 27 degrees, the level treeline at about "
             f"{pct(_tree[1])} percent of frame height. The split pale rock spans about {_rkR[0] - _rkL[0]} pixels of "
             f"frame width, from about {_rkL[0]} to {_rkR[0]} pixels from the left, its top at about {pct(_rkT[1])} "
             f"percent, and keeps that width and position in every frame. The seating bowl spans from about "
             f"{_rimL[0]} to {_rimR[0]} pixels from the left at its widest, its near rim lowest at about {pct(_rimC[1])} percent of "
             f"frame height in the middle; the stage platform lies at the upper centre, its front edge from about "
             f"{_sFL[0]} to {_sFR[0]} pixels at about {pct(_sFL[1])} percent. ")
def C_WATER(L):
    k, r = WL(L); m, s = proj(pol(r, 0, L)), proj(pol(r, -90, L))
    return (f"The water line runs along the foot of the {ORD[k]} terrace, at about {pct(m[1])} percent of frame height "
            f"in the middle, curving up to about {pct(s[1])} percent at both sides.")
ORD = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth",
       9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth"}
_crane = proj((-26, 10, 0.2)); _towL, _towR, _towT = proj((-16, 2, 1.2)), proj((16, 2, 1.2)), proj((16, 2, 10.2))
_shT = proj((0, 10, 13.2)); _pump = proj((-48, 12, 8))
C_CRANE = f"The mobile crane stands at about {_crane[0]} pixels from the left, its outriggers at about {pct(_crane[1])} percent of frame height."
C_PUMP = f"The pumps and settling tanks stand at the upper left, around {_pump[0]} pixels from the left."
C_SHELL = f"The shell rises to about {pct(_shT[1])} percent of frame height above the middle of the stage."
C_TOW = (f"The two towers stand at about {_towL[0]} and {_towR[0]} pixels from the left, their tops at about "
         f"{pct(_towT[1])} percent of frame height.")
COMP_TAIL = "Nothing that proves progress falls into the top-right corner of the frame."

TR_A = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and "
        "crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, "
        "clouds drift smoothly, machines move fast with light motion blur.")
TR_A_W = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and "
          "crews all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, "
          "clouds drift smoothly, the brown water is smoothed to a soft sheen, machines move fast with light motion blur.")
TR_B = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all "
        "move at the same accelerated speed. Two hours pass across this shot: shadows swing slowly round, clouds "
        "streak across the sky, machines smear into heavy motion blur.")
TR_A_DUSK = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, light, vehicles and people "
             "all move at the same accelerated speed. Ten minutes pass across this shot: the sky deepens slowly, "
             "clouds drift smoothly, people move fast as soft streaks.")
TR_G = ("TIME RATE: Everything in this frame moves at natural speed: the people, the trees and the sky. Eight seconds "
        "pass across this shot: the light holds, the clouds hold still, the treetops sway slightly in a light "
        "breeze, and people move in small natural ways.")

I2V_HEAD = ("The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its "
            "last frame is that image, matched frame for frame — same framing, same light, same objects in the same "
            "places.")
LOCK_MAIN = ("The camera does not move at any point. The framing is identical in the first and last frame. The "
             "hollow, the forest, the split pale rock, the two pines, the back wall and the service road stay exactly "
             "where they are, at exactly the same size and shape, for the whole shot; the split rock occupies exactly "
             "the same width of the frame in the first and last frame. The hollow holds exactly one theatre with "
             "exactly twelve terraces and three stair aisles. Nothing already built is removed or resized.")
I2V_TAIL = ("Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
            "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
            "documentary time-lapse cinematography.")

# ── tekrarlanan durum cümleleri (aynı nesne her karede aynı kelimelerle) ─────
TERR = "the twelve stepped stone terraces and the three radial stair aisles of steps"
PUMPS = ("two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road at "
         "the upper left, thick black hoses running from the pumps")
PUMPS_IDLE = ("two yellow trailer pumps and a row of three grey settling tanks stand on a lay-by of the service road "
              "at the upper left, their thick black hoses coiled beside them")
CRANE = "a large yellow mobile crane stands on its outriggers on the hardstand at the left end of the stage"
def HOOK(x): return CRANE + f", with {x} on the hook on taut slings"
def UP(): return CRANE + ", its boom raised steeply, its tip and line above the top edge of the frame"
DRY = "clean, pale and dry"
SEATS = "all twelve stone terraces carry continuous warm brown timber seat boards between the three stair aisles of steps"
STAGE_T = "a broad warm timber stage floor covers the whole stone stage platform"
SHELL = ("the fan-shaped acoustic shell stands complete over the rear third of the stage, warm copper-coloured on its "
         "upper outer face and pale timber on its curved inner face")
TOWERS = ("two compact dark steel towers stand at the left and right sides of the stage, hung with black loudspeaker "
          "and lighting units")
PATHS = ("two broad pale paved paths lined with low lamps lead from the lower left and lower right edges of the frame "
         "to the entrances at the top of the left and right aisles")
LAMPS_OFF = "the small step lamps along the three aisles, the light fittings inside the shell and the path lamps are unlit"
LAMPS_ON = ("the small warm step lamps along the three aisles, the warm light inside the timber face of the shell and the "
            "low lamps along the two paths are lit, while the main stage lights on the towers stay dark")
ENS = "a small ensemble of musicians sits on chairs among music stands across the front of the stage"
def U(x): return x[0].upper() + x[1:]
FIN = SEATS + "; " + STAGE_T + "; " + SHELL + "; " + TOWERS + "; " + PATHS   # bitmiş yapı (G14+)

# ── doku ────────────────────────────────────────────────────────────────────
T_FLOOD = ("Wet dark silt coating the stone of the top terraces, drifts of wet autumn leaves along the water line, thin "
           "foam lines and floating twigs on the brown water, tyre ruts and puddles in the gravel of the service road, "
           "coils of hose stacked beside the pumps. " + FILMSTOCK)
T_MUD = ("Thick dark mud with tyre ruts and track marks on the orchestra floor, a film of brown silt and drifts of "
         "leaves on every terrace, mud spatter on the machines, puddles in the gravel of the hardstand, stacks of "
         "timber planks. " + FILMSTOCK)
T_WASH = ("Bands of clean pale stone beside dull silt-brown stone, grey wash water running in streaks down the steps, "
          "puddles on the orchestra floor, wet sheen on the freshly washed stone, dirt-stained hoses and tyre ruts on "
          "the hardstand. " + FILMSTOCK)
T_DRYING = ("Clean pale stone drying from the top down, darker damp patches on the lower terraces, fresh mortar joints "
            "on the new blocks, stacks of pallets and offcuts on the hardstand, a film of dust and tyre ruts in the "
            "gravel. " + FILMSTOCK)
T_BUILD = ("Clean pale dry stone with faint old stains, fresh sawn timber with pale cut ends, pallets and offcuts "
           "stacked on the hardstand, coils of cable, tyre ruts and a film of dust in the gravel. " + FILMSTOCK)
T_DONE = ("Clean pale dry stone with faint old stains, warm timber with a soft satin sheen, raked gravel on the empty "
          "hardstand with the faint print of tyre tracks, pale patches where the stacks stood, fallen leaves in the "
          "corners of the steps. " + FILMSTOCK)
T_EVE = ("Clean pale stone, warm timber seat boards with a soft sheen, cables taped along the edge of the stage, "
         "fallen leaves in the corners of the steps, raked gravel with the faint print of tyre tracks. " + FILMSTOCK)

# ── ışık (bakış 15° — güneş hiçbir karede kadrajda değil: sabah arkada sağda, öğle arkada, akşam arkada solda) ──
LIGHT_DESC = {
 "morning": ("on the right behind the camera: clear morning light from the right, long shadows falling forward to the "
             "left across the bowl."),
 "noon": ("high behind the camera: bright light falls straight into the bowl and onto the stage, short shadows fall "
          "away from the camera."),
 "pm": ("behind the camera on the left: warm afternoon light from the left, shadows falling forward to the right."),
 "golden": ("low behind the camera on the left: warm golden light across the stage, the shell and the treetops, long "
            "shadows to the right, the bowl floor in soft shade."),
 "dusk": ("behind the camera on the left: the last warm light leaves the treetops, the hollow lies in soft even shade "
          "without shadows, and the clear sky fades from pale gold to soft blue."),
 "blue": ("behind the camera on the left: deep clear blue hour, the sky still readable, the stone, the timber seats, "
          "the shell and the trees clearly visible; the air is clear and dry, and the lit lamps are small warm points "
          "with crisp edges."),
}
def LIGHT(t, key):
    tail = " The sun stays outside the frame." if sun(hm(t))[1] > -0.5 else " The sun is below the horizon, outside the frame."
    return f"LIGHTING: {sunline(t)}, {LIGHT_DESC[key]}{tail}"

# ── sahne verisi ─────────────────────────────────────────────────────────────
S = []
def scene(**k): S.append(k)

# ---------- S0 ----------
scene(n=0, fiil="BOŞALTIR", eleman="su çizgisi 11. terasın dibinden → 7. terasın dibine (kot +6,1 → +4,1) · üstten dört yeni yay", rejim="A", t0="09:20", t1="09:30",
 g="G0",
 stage=("the theatre is still flooded: opaque brown floodwater fills the bowl up to the foot of the eleventh terrace, "
        "drifting autumn leaves and thin foam lines on its surface. Only the two top terraces of stepped stone seating "
        "stand clear, dark with silt, curving round the near rim, with the steps of the three stair aisles running down "
        "into the water; the edge of the next terrace shows just under the surface, and the lower terraces and the stage "
        "platform lie under the water. The lower part of the service road runs down into the water. " + U(PUMPS) +
        " down the slope into the water. A crew on the top terrace holds the hose ends."),
 moment="Twenty past nine on a clear autumn morning: the pumps are already running, and the first stone curves are rising out of the floodwater.",
 comp=C_WATER(6.1) + " " + C_PUMP,
 light=LIGHT("09:20", "morning"), tr=TR_A_W,
 act=("The two trailer pumps draw the brown water up the hoses into the settling tanks, a crew pulls the hose ends "
      "down the steps after the falling water line, a second crew rakes wet leaves and silt off the emerging stone "
      "into piles, and a small truck brings coils of spare hose along the service road. " + CREW),
 tex=T_FLOOD,
 phys=("The trailer pumps stand on their wheels on the gravel lay-by, the hoses rest on the stone steps and run down "
       "into the water, and the settling tanks sit on steel skids on the road. The stone terraces are founded on the "
       "floor of the hollow and stay unchanged under the water."),
 mf=("The water level in the bowl falls from the foot of the eleventh terrace to the foot of the seventh terrace as "
     "the pumps draw it up the hoses into the tanks, uncovering four more stone terraces from the top down."),
 body=("Ten minutes pass in the clear morning light. Everything in this shot is time-lapsed at the same rate. From the "
       "first frame the water line is already sliding down: it drops evenly all round the bowl, never rising, and one "
       "wet, silt-dark stone curve after another comes up out of the brown water around the same centre, each a little "
       "smaller, until six terraces stand clear; the lower terraces and the stage platform stay under the water. Slow "
       "current lines drift across the surface towards the hose ends at the left. The crew pulls the hoses down the "
       "steps after the water, a second crew rakes leaves and silt into piles, and a small truck brings coils of spare "
       "hose along the service road and the crew carries them to the pumps. Thin high clouds drift slowly from the "
       "right, and long shadows fall forward to the left."))

# ---------- S1 ----------
scene(n=1, fiil="AÇIĞA ÇIKARIR", eleman="su 7. terasın dibinden → sahne platformunun hemen üstüne (+4,1 → +1,5) · üç merdiven bağlanır · sol merdivende hasar görünür", rejim="A", t0="09:30", t1="09:40",
 g="G1",
 stage=("the water is going down: opaque brown floodwater still fills the lower bowl up to the foot of the seventh "
        "terrace, leaves and foam lines on its surface. The six top terraces of stepped stone seating stand clear, dark "
        "and wet with silt, the steps of the three radial stair aisles running down into the water; the lower terraces "
        "and the stage platform lie under it. " + U(PUMPS) + " down the centre aisle into the water. Crews stand on "
        "the wet terraces beside piles of raked leaves and silt."),
 moment="Half past nine in the morning: half the seating is out of the water, and the curves already read as a theatre.",
 comp=C_WATER(4.1) + " " + C_PUMP,
 light=LIGHT("09:30", "morning"), tr=TR_A_W,
 act=("The two trailer pumps keep drawing the water up the hoses, a crew pulls the hose ends down the three stair "
      "aisles after the falling water line, a second crew shovels silt from the wet terraces into hand carts, and a "
      "truck brings more hose along the service road. " + CREW),
 tex=T_FLOOD,
 phys=("The trailer pumps stand on their wheels on the gravel lay-by, the hoses rest on the steps of the aisles, and "
       "the hand carts stand on the terraces. The stone terraces are founded on the floor of the hollow and stay "
       "unchanged under the water."),
 mf=("The water level falls from the foot of the seventh terrace to just above the stage platform, uncovering the lower "
     "terraces, the bottoms of the three stair aisles and a broken stretch of the left aisle."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the water line "
       "keeps sliding down evenly, never rising: the lower terraces come out of the brown water one after another and "
       "the three stair aisles join the curves into one complete stepped bowl round the hidden stage. On the left aisle "
       "a broken stretch shows: several steps and the ends of the terraces beside them are cracked and missing. By the "
       "end only a thin sheet of brown water lies over the stage platform and the orchestra floor. The crew pulls the "
       "hoses down the aisles after the water, a second crew shovels silt into hand carts and pushes them up the centre "
       "aisle to the rim, and a truck brings more hose along the service road. Small clouds drift slowly from the "
       "right, and the shadows fall forward to the left."))

# ---------- S2 ----------
scene(n=2, fiil="KURUTUR", eleman="son sığ su sahne + orkestradan hortuma (+1,5 → 0) · ⭐ dikdörtgen sahne çamurdan çıkar · bütün geometri görünür", rejim="A", t0="09:40", t1="09:50",
 g="G2",
 stage=("the bowl is almost drained: " + TERR + " stand clear all round, dark and wet with silt, the left aisle broken "
        "where several steps and terrace ends are cracked and missing. A thin sheet of brown floodwater still covers "
        "the orchestra floor and the stage platform, the platform's straight outline faint under it. " + U(PUMPS) +
        " down the centre aisle into the shallow water. A small truck loaded with timber planks stands on the "
        "hardstand at the edge of the water."),
 moment="Twenty to ten in the morning: the whole bowl stands clear, and only a sheet of water still hides the stage.",
 comp=C_WATER(1.5) + " " + C_PUMP,
 light=LIGHT("09:40", "morning"), tr=TR_A_W,
 act=("The two trailer pumps draw the last shallow water up the hoses, a crew drags the hose ends across the orchestra "
      "after the shrinking water, a second crew pulls the floating leaves and branches into piles on the lower "
      "terraces, and a crew lays timber planks from the truck as walkways at the edge of the water. " + CREW),
 tex=T_FLOOD,
 phys=("The trailer pumps stand on their wheels on the gravel lay-by, the hoses rest on the steps and the floor of the "
       "orchestra, and the truck sits on the gravel of the hardstand. The stone stage platform is founded on the floor "
       "of the hollow."),
 mf=("The last shallow water drains from the stage platform and the orchestra floor up the hoses into the tanks, and "
     "the straight stone edge of the rectangular stage platform comes up out of thick dark mud."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the sheet of "
       "brown water is already shrinking towards the hose ends at the left, never rising again, and the straight edges "
       "of the rectangular stage platform come up through it, coated in thick dark mud, until the water is gone and "
       "the whole theatre lies open: twelve curves, three aisles and the stage. The crew drags the hoses after the last "
       "water, a second crew pulls leaves and branches into piles, and a crew carries timber planks from the truck and "
       "lays them as walkways across the mud. At the end a small tracked loader, a wheel loader and two orange dump "
       "trucks drive down the service road onto the hardstand. Small clouds drift slowly, and the shadows fall forward "
       "to the left."))

# ---------- S3 ----------
scene(n=3, fiil="TEMİZLER", eleman="kalın çamur sahne + orkestradan → yükleyici → damperli kamyonlar (%0 → %100) · ekipler teraslardaki birikintiyi toplar", rejim="A", t0="09:50", t1="10:00",
 g="G3",
 stage=("the bowl is drained: the orchestra floor and the stage platform lie under a thick layer of dark wet mud "
        "with heaps of mud, leaves and branches on the platform, and " + TERR + " are coated in dark silt, the left "
        "aisle broken. Timber plank walkways cross the mud. A small yellow tracked loader stands on the stage "
        "platform, and a yellow wheel loader and two orange dump trucks stand on the hardstand. " + U(PUMPS) +
        " down to the orchestra floor."),
 moment="Ten to ten in the morning: the water has left a bowl of mud, and the machines have come down.",
 comp=C_PUMP + " The stage platform reads as one dark rectangle of mud at the upper centre.",
 light=LIGHT("09:50", "morning"), tr=TR_A,
 act=("The small tracked loader scrapes the thick mud off the stage platform and pushes it along the planks to the "
      "hardstand, the wheel loader lifts the heaps into a dump truck, which drives up the service road and back "
      "empty, and crews with shovels and hand carts clear the silt from the terraces into piles at the foot of the "
      "aisles. " + CREW),
 tex=T_MUD,
 phys=("The tracked loader sits on its tracks on the stone platform, the wheel loader and the dump trucks stand on the "
       "gravel of the hardstand, and the planks rest on the mud. The stone terraces are founded on the floor of the "
       "hollow."),
 mf=("The tracked loader pushes the thick mud from the stage platform and the orchestra floor to the hardstand, and "
     "the wheel loader lifts it from the heaps into the dump trucks, which carry it away up the service road."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the machines are "
       "already working: the dark heaps on the stage shrink load by load, the straight stone edge of the stage "
       "platform and the curved front of the first terrace come clear, and the crews scrape the terraces from the top "
       "down and wheel the silt in carts to the loader; at the end every surface lies bare but still dull brown under a "
       "film of silt. The wheel loader lifts each heap into a dump truck, and the trucks drive up the service road "
       "loaded and come back empty, and a crew carries the planks up to the hardstand and stacks them. At the end a white water tanker truck arrives on the hardstand and the crews carry "
       "coiled washer hoses to the top terrace. Small clouds drift slowly, and the shadows fall forward to the left."))

# ---------- S4 ----------
scene(n=4, fiil="YIKAR", eleman="basınçlı yıkama koyu silt → açık taş (%0 → %100, en üst terastan orkestraya) · ıslak", rejim="B", t0="10:00", t1="12:00",
 g="G4",
 stage=("the heavy clean-up is done: the stage platform and the orchestra floor are bare stone, and " + TERR + " are "
        "scraped bare but still dull brown-grey under a film of dried silt, the left aisle broken. " + U(PUMPS) + " down to the "
        "orchestra floor. A white water tanker truck stands on the hardstand with coiled pressure-washer hoses, and "
        "washing crews with long lances stand along the top terrace."),
 moment="Ten in the morning: the bowl is bare but dirty, and the washing crews are lined up along the top.",
 comp=C_PUMP + " The whole bowl reads one dull brown-grey from the near rim to the stage.",
 light=LIGHT("10:00", "morning"), tr=TR_B,
 act=("Crews with pressure-washer lances spray the silt off the stone terrace by terrace from the near rim down towards "
      "the orchestra, a crew moves the long washer hoses from the tanker truck down the aisles behind them, and the "
      "pumps draw the grey wash water from the orchestra floor back up the hoses into the tanks. " + CREW_B),
 tex=T_WASH,
 phys=("The tanker truck stands on its wheels on the gravel hardstand, the washer hoses rest on the steps, and the "
       "pumps sit on the lay-by. The stone terraces are founded on the floor of the hollow."),
 mf=("The washing crews spray the dark silt from the stone terraces and stair aisles, from the near rim down to the "
     "orchestra, and the grey wash water runs down the steps to the pump hoses."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Band by band from the top the dull "
       "brown stone turns a clean pale grey-white, wet and darker at first, the clean area growing steadily down the "
       "bowl terrace after terrace and along the three aisles, until the whole bowl and the stage platform are clean "
       "pale stone, still wet; the broken left aisle stays broken. The grey wash water runs down the steps to the "
       "orchestra and the pumps draw it up the hoses, and the emptied tanker truck drives off up the service road. At the end a large yellow mobile crane drives down the service "
       "road onto the hardstand, sets its outriggers, and lifts a pallet of cut stone blocks from a flatbed truck. The "
       "shadows swing slowly round behind the camera as the sun climbs, and clouds streak across the sky."))

# ---------- S5 ----------
scene(n=5, fiil="ONARIR", eleman="sol merdivenin kırık basamakları + yandaki teras uçları taş bloklarla (%0 → %100) · teras sayısı aynı", rejim="A", t0="12:00", t1="12:10",
 g="G5",
 stage=("the stone is washed: " + TERR + ", the orchestra floor and the stage platform are clean pale stone, still wet "
        "and dark in patches; on the left aisle several steps and the terrace ends beside them are still broken and "
        "missing. " + U(HOOK("a pallet of cut stone blocks")) + ". A flatbed truck loaded with pallets of cut pale "
        "stone blocks stands on the hardstand. " + U(PUMPS) + " to the orchestra floor. A masonry crew waits at the "
        "broken steps beside a small mortar mixer."),
 moment="Noon: the whole bowl is clean, and the stonemasons start on the broken aisle.",
 comp=C_CRANE + " " + C_PUMP,
 light=LIGHT("12:00", "noon"), tr=TR_A,
 act=("The mobile crane lifts the pallets of cut stone blocks from the flatbed truck and lowers them beside the broken "
      "left aisle, a masonry crew sets the blocks one by one into the missing steps and terrace ends and beds them in "
      "mortar, and a second crew mixes mortar at the small mixer; the crane carries a visible load. " + CREW),
 tex=T_DRYING,
 phys=("The pallet hangs from the crane hook on four taut slings. The crane stands on its outriggers on pads on the "
       "gravel, the new blocks are seated in mortar on the old stone, and the mixer sits on a terrace."),
 mf=("The mobile crane lifts the pallets of cut stone blocks from the flatbed truck on the hardstand to the broken left "
     "aisle, and the masonry crew sets the blocks into the missing steps and terrace ends."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first pallet "
       "is already swinging in over the terraces: block by block the gap in the left aisle closes, step after step and "
       "the broken terrace ends beside it, until all three stair aisles run unbroken from the orchestra to the near "
       "rim, the new pale blocks matching the old stone; the number and shape of the terraces stay the same. The stone "
       "keeps drying in patches from the top down. The emptied truck drives off up the service road, and a truck loaded "
       "with bundles of timber seat boards arrives; at the end the crane lifts a bundle from it. Small clouds drift "
       "slowly, and short shadows fall away from the camera."))

# ---------- S6 ----------
scene(n=6, fiil="OTURTUR", eleman="ahşap oturma tahtaları 12 terasa, alttan yukarı sıra sıra (%0 → %100) · yeni tribün katı YOK", rejim="B", t0="12:10", t1="14:10",
 g="G6",
 stage=("the stone is repaired: " + TERR + " run unbroken round the bowl in clean pale stone, drying from the top down, "
        "a few damp patches on the lower terraces. " + U(HOOK("a bundle of timber seat boards")) + ". A flatbed truck "
        "loaded with bundles of warm brown timber seat boards stands on the hardstand, and more bundles lie stacked on "
        "the orchestra floor. " + U(PUMPS) + " to the orchestra floor."),
 moment="Ten past twelve: the bowl is whole again, and the timber for the seats has arrived.",
 comp=C_CRANE + " " + C_PUMP,
 light=LIGHT("12:10", "noon"), tr=TR_B,
 act=("The mobile crane lifts the bundles of seat boards from the flatbed truck onto the orchestra floor, carpentry "
      "crews carry the boards up the three aisles and screw them onto steel brackets along the front of each terrace, "
      "row after row from the lowest terrace upwards; the crane carries a visible load. " + CREW_B),
 tex=T_BUILD,
 phys=("The bundle hangs from the crane hook on two taut slings. The crane stands on its outriggers on the gravel, and "
       "the seat boards are bolted to steel brackets anchored in the stone terraces."),
 mf=("Carpentry crews carry the warm brown timber seat boards from the stacked bundles on the orchestra floor up the "
     "aisles and fix them along the front of each stone terrace, row after row from the lowest terrace to the near rim."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Row by row from the bottom a warm brown "
       "band of timber runs along each pale stone curve, terrace after terrace up the bowl, until all twelve terraces "
       "carry continuous seat boards between the three aisles and the bowl reads as warm brown curves on pale stone; "
       "the number of terraces stays twelve and no new tier is added. The crane lifts bundle after bundle from the "
       "trucks onto the orchestra floor, and the stacks there shrink as the crews carry them up. The last damp patches "
       "dry out. At the end a flatbed truck loaded with low steel deck-frame modules arrives on the hardstand and the "
       "crane lifts a module from it. The shadows swing slowly from behind the camera to the left side as the sun "
       "passes, and clouds streak across the sky."))

# ---------- S7 ----------
scene(n=7, fiil="ÇATAR", eleman="alçak çelik döşeme iskeleti modülleri sahne platformuna (%0 → %100, soldan sağa) · platform sınırı aşılmaz", rejim="A", t0="14:10", t1="14:20",
 g="G7",
 stage=("the seating is fitted: " + SEATS + ", the stone " + DRY + ". The stage platform is bare pale stone. " +
        U(HOOK("a steel deck-frame module")) + ". A flatbed truck loaded with low steel deck-frame modules stands on "
        "the hardstand. " + U(PUMPS_IDLE) + ". A crew waits on the stage platform with bolt boxes."),
 moment="Ten past two in the afternoon: the seats are in, and the stage itself comes next.",
 comp=C_CRANE + " " + C_PUMP,
 light=LIGHT("14:10", "pm"), tr=TR_A,
 act=("The mobile crane lifts the low steel deck-frame modules from the flatbed truck onto the stage platform, a crew "
      "bolts them together into one level grid from the left end to the right end, and a second crew sets steel "
      "levelling feet under them; the crane carries a visible load. " + CREW),
 tex=T_BUILD,
 phys=("The module hangs from the crane hook on four taut slings. The crane stands on its outriggers on the gravel, and "
       "the modules already set rest on levelling feet on the stone platform, bolted together."),
 mf=("The mobile crane lifts the low steel deck-frame modules from the flatbed truck on the hardstand onto the stone "
     "stage platform, and the crew bolts them into one level grid from the left end to the right."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first module "
       "is already swinging in over the platform: module by module from the left a low, regular grid of dark steel "
       "spreads across the stone, staying inside its edges, until it covers the whole platform; the seating stays as it "
       "was. The emptied truck drives off and a truck loaded with pallets of wide timber deck panels arrives; at the end "
       "the crane lifts a pallet from it. A few clouds drift slowly from the left, and the shadows fall forward to the "
       "right."))

# ---------- S8 ----------
scene(n=8, fiil="KAPLAR", eleman="geniş ahşap döşeme panelleri ızgaranın üstüne (%0 → %100, önden arkaya) · sıcak renkli sahne", rejim="A", t0="14:20", t1="14:30",
 g="G8",
 stage=(SEATS + ", the stone " + DRY + ". The stage platform is covered from edge to edge by a low, level grid of dark "
        "steel deck frame, bolted together, its open squares showing the stone below. " +
        U(HOOK("a pallet of timber deck panels")) + ". A flatbed truck loaded with pallets of wide timber deck panels "
        "stands on the hardstand beside a skip. " + U(PUMPS_IDLE) + "."),
 moment="Twenty past two in the afternoon: the stage frame is set, and its timber floor is next.",
 comp=C_CRANE + " " + C_PUMP,
 light=LIGHT("14:20", "pm"), tr=TR_A,
 act=("The mobile crane lifts the pallets of wide timber deck panels from the flatbed truck onto the stage, a carpentry "
      "crew lays the panels across the steel grid from the front edge to the back and screws them down, and a second "
      "crew carries offcuts to the skip on the hardstand; the crane carries a visible load. " + CREW),
 tex=T_BUILD,
 phys=("The pallet hangs from the crane hook on four taut slings. The crane stands on its outriggers on the gravel, and "
       "the panels already laid are screwed down onto the steel grid, bolted together and resting on the stone platform."),
 mf=("The carpentry crew lays the wide timber deck panels from the crane-lifted pallets onto the steel deck frame, from "
     "the front edge of the stage to the back."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first "
       "pallet is already swinging in: panel by panel from the front the dark grid closes under warm timber, until one "
       "broad, warm-coloured timber stage covers the whole stone platform and stays inside its old edges. The second "
       "crew carries the offcuts to the skip. The emptied truck drives off and a long flatbed truck loaded with curved "
       "steel ribs arrives; at the end the crane lifts the first rib from it. A few clouds drift slowly from the left, "
       "and the shadows fall forward to the right."))

# ---------- S9 ----------
scene(n=9, fiil="DİKER", eleman="yedi kavisli çelik kaburga sahnenin arkasına, yelpaze gibi (%0 → %100, soldan sağa) · ön üçte iki açık", rejim="A", t0="14:30", t1="14:40",
 g="G9",
 stage=(SEATS + ", the stone " + DRY + "; " + STAGE_T + ". " + U(HOOK("a long curved steel rib")) + ". A long flatbed "
        "truck loaded with curved steel ribs stands on the hardstand. Steel base plates are bolted along the back edge "
        "of the stage, and a rigging crew with taglines waits beside a scissor-lift platform. " + U(PUMPS_IDLE) + "."),
 moment="Half past two in the afternoon: the stage is built, and the frame of its shell is going up.",
 comp=C_CRANE + " " + C_PUMP,
 light=LIGHT("14:30", "pm"), tr=TR_A,
 act=("The mobile crane lifts the long curved steel ribs one by one from the flatbed truck to the back of the stage, a "
      "rigging crew guides each rib with taglines and bolts its foot to a base plate, and a second crew on the "
      "scissor-lift platform bolts the rib tops together; the crane carries a visible load. " + CREW),
 tex=T_BUILD,
 phys=("The rib hangs from the crane hook on two taut slings. The crane stands on its outriggers on the gravel, and the "
       "ribs already set are bolted to base plates anchored in the stone platform, braced to each other at the top."),
 mf=("The mobile crane lifts the seven long curved steel ribs from the flatbed truck onto the base plates along the "
     "back of the stage, where they fan out and curve forward over the rear third of the stage."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first rib is "
       "already rising on the hook: rib by rib from the left, each one swings in, stands on its base plate and is bolted "
       "fast, until seven tall curved steel ribs fan out from the back of the stage and curve forward over its rear "
       "third, open to the sky like the frame of a great shell; the front two thirds of the stage stay clear. The "
       "emptied truck drives off, and a truck loaded with crates of outer shell panels and timber modules arrives; at "
       "the end the crane lifts a crate from it. A few clouds drift slowly from the left, and the shadows fall forward "
       "to the right."))

# ---------- S10 ----------
scene(n=10, fiil="KAPLAR", eleman="bakır renkli dış paneller + ahşap iç modüller kaburgalara (%0 → %100, aşağıdan yukarı) · ⭐ kabuk tamam", rejim="B", t0="14:40", t1="16:40",
 g="G10",
 stage=(SEATS + ", the stone " + DRY + "; " + STAGE_T + ". Seven tall curved steel ribs fan out from base plates at the "
        "back of the stage and curve forward over its rear third, bare and open to the sky, the front two thirds of the "
        "stage clear. " + U(HOOK("a crate of outer shell panels")) + ". A flatbed truck loaded with crates of outer "
        "shell panels and timber modules stands on the hardstand. Two scissor-lift platforms stand at the back of the "
        "stage. " + U(PUMPS_IDLE) + "."),
 moment="Twenty to three in the afternoon: the bones of the shell stand, and its skin goes on next.",
 comp=C_CRANE + " " + C_SHELL,
 light=LIGHT("14:40", "pm"), tr=TR_B,
 act=("The mobile crane lifts crates of outer shell panels and timber modules from the flatbed truck to the back of the "
      "stage, a crew on the two scissor-lift platforms bolts the panels onto the ribs from the bottom up, and a second "
      "crew fixes the timber modules under them; the crane carries a visible load. " + CREW_B),
 tex=T_BUILD,
 phys=("The crate hangs from the crane hook on four taut slings. The ribs are bolted to base plates on the stone "
       "platform, the panels are bolted to the ribs, and the scissor lifts stand on the timber stage."),
 mf=("The crew bolts the warm copper-coloured outer panels and the timber inner modules from the crane-lifted crates "
     "onto the seven steel ribs, from the bottom up, closing the shell."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Panel by panel from the bottom the open "
       "ribs close into one smooth fan-shaped shell, warm copper-coloured on its upper outer face and pale timber on its "
       "curved inner face turned towards the seats, with a row of small unlit light fittings along its inner edge; it "
       "covers only the rear third of the stage, the front two thirds open to the camera. The trucks bring crate after "
       "crate and leave empty. As the sun sinks behind the camera on the left the copper takes on the low warm light. "
       "At the end a truck brings two dark lattice tower frames and crates of loudspeakers, and the crane lifts the "
       "first frame. The shadows swing slowly to the right and lengthen, and clouds streak across the sky."))

# ---------- S11 ----------
scene(n=11, fiil="KURAR", eleman="iki koyu teknik kule (ışık + hoparlör) sahnenin iki yanına (%100) · merdiven kenarı basamak lambaları (sönük)", rejim="A", t0="16:40", t1="16:50",
 g="G11",
 stage=(SEATS + ", the stone " + DRY + "; " + STAGE_T + "; " + SHELL + ", a row of small unlit light fittings along "
        "its inner edge. " + U(HOOK("a dark steel tower frame")) + ". A flatbed truck loaded with a second dark steel "
        "tower frame and crates of loudspeaker and lighting units stands on the hardstand. " + U(PUMPS_IDLE) + "."),
 moment="Twenty to five in the afternoon, golden hour: the shell is finished, and the tower frames go up.",
 comp=C_CRANE + " " + C_SHELL,
 light=LIGHT("16:40", "golden"), tr=TR_A,
 act=("The mobile crane lifts the two dark steel tower frames from the flatbed truck and sets one at each side of the "
      "stage, a rigging crew bolts them down and hangs black loudspeaker and lighting units on them from a scissor-lift "
      "platform, and an electrical crew fits small unlit step lamps along the edges of the three stair aisles; the "
      "crane carries a visible load. " + CREW),
 tex=T_BUILD,
 phys=("The tower frame hangs from the crane hook on four taut slings. The crane stands on its outriggers on the "
       "gravel, the shell is bolted to its ribs, and the seat boards are bolted to brackets on the terraces."),
 mf=("The mobile crane lifts the two dark steel towers from the flatbed truck onto their footings at the left and "
     "right sides of the stage, and the crew hangs the loudspeaker and lighting units on them."),
 body=("Ten minutes pass in the golden light. Everything in this shot is time-lapsed at the same rate. From the first "
       "frame the first tower frame is already swinging in: the left tower stands at the left side of the stage, then "
       "the right one, two compact dark towers standing symmetrically, and the crew hangs the black loudspeakers and "
       "the unlit lighting units on them. Along the three aisles the electrical crew fits a line of small unlit step "
       "lamps. The emptied truck drives off, and the scissor-lift platforms roll down the ramp and away up the service road; at the end small dumpers bring pallets of pale paving stones down to the "
       "two entrances, and the crane raises its boom steeply until its tip and line rise above the top edge of the "
       "frame. Long golden shadows fall to the right, and a few clouds drift slowly from the left."))

# ---------- S12 ----------
scene(n=12, fiil="DÖŞER", eleman="iki giriş yolu geniş taşlarla, kadraj kenarından girişe (%0 → %100) + alçak yol lambaları (sönük)", rejim="A", t0="16:50", t1="17:00",
 g="G12",
 stage=(SEATS + "; " + STAGE_T + "; " + SHELL + "; " + TOWERS + "; small unlit step lamps line the three aisles. " +
        U(UP()) + ". Two rough earth tracks lead from the lower left and lower right edges of the frame to the entrances "
        "at the top of the left and right aisles, pallets of broad pale paving stones stacked beside them. " +
        U(PUMPS_IDLE) + "."),
 moment="Ten to five in the afternoon, golden hour: the stage is ready, and the ways in are being paved.",
 comp=C_CRANE + " " + C_TOW,
 light=LIGHT("16:50", "golden"), tr=TR_A,
 act=("Two paving crews set the broad pale paving stones from the pallets along the two entrance tracks, a small "
      "roller packs the gravel bed ahead of them, a small dumper brings more pallets along each track, and an "
      "electrical crew sets a row of low unlit lamps along the path edges. " + CREW),
 tex=T_BUILD,
 phys=("The paving stones are bedded on packed gravel, the lamps are anchored in the path edges, and the dumpers stand "
       "on the tracks. The crane stands on its outriggers on the gravel, its boom raised steeply."),
 mf=("The paving crews lay the broad pale paving stones from the pallets along the two entrance tracks, from the lower "
     "left and lower right edges of the frame up to the entrances on the near rim."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the crews are "
       "already setting stones: stone by stone two broad pale paths grow from the frame edges up to the two entrances, "
       "edged and level, until both run paved to the top of the left and right aisles, a row of low unlit lamps along "
       "each; the forest edge and the outer line of the theatre stay as they were. The dumpers bring pallet after "
       "pallet and the stacks beside the tracks shrink, and the emptied dumpers and the roller drive off along the tracks. At the end the crane lowers its boom, the crew hooks a bundle of "
       "empty pallets to it on the hardstand, and the crane lifts it. Long golden shadows fall to the right, and a few clouds drift slowly from "
       "the left."))

# ---------- S13 ----------
scene(n=13, fiil="BOŞALTIR", eleman="vinç + pompalar + çökeltme tankları + paletler servis yolundan sırayla ÇIKAR · saha açılır", rejim="A", t0="17:00", t1="17:10",
 g="G13",
 stage=(SEATS + "; " + STAGE_T + "; " + SHELL + "; " + TOWERS + "; " + PATHS + "; small unlit step lamps line the "
        "three aisles. " + U(HOOK("a bundle of empty pallets")) + ". Two empty flatbed trucks stand on the hardstand "
        "beside stacks of empty pallets and timber planks. " + U(PUMPS_IDLE) + "."),
 moment="Five in the afternoon, golden hour: the theatre is restored, and the site is being cleared.",
 comp=C_CRANE + " " + C_PUMP,
 light=LIGHT("17:00", "golden"), tr=TR_A,
 act=("The mobile crane lifts the last bundles of empty pallets and planks onto the flatbed trucks, a crew coils the hoses and "
      "hitches the trailer pumps and the settling tanks to trucks, a crew rakes the hardstand, and then the crane "
      "stows its boom and drives up the service road behind the trucks; the crane carries a visible load. " + CREW),
 tex=T_BUILD,
 phys=("The bundle hangs from the crane hook on two taut slings. The crane stands on its outriggers on the gravel, the "
       "trailer pumps stand on their wheels, and each settling tank sits on steel skids on the lay-by."),
 mf=("The mobile crane, the trailer pumps, the settling tanks, the planks and the empty pallets leave the site in turn, from the "
     "hardstand and the lay-by up the service road to the left edge of the frame."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the last bundle "
       "is already swinging onto a truck: the crews coil the hoses and load them, a truck tows the two trailer pumps "
       "away up the service road, a flatbed carries the settling tanks off one by one, the crane folds its boom down "
       "and drives slowly up the road after them and out of the left edge of the frame, and a crew rakes the hardstand "
       "smooth. For the first time the restored theatre stands alone in the hollow, every part of it in view. A white "
       "van comes down the road at the end and stops on the hardstand. Long golden shadows fall to the right, and a few "
       "clouds drift slowly from the left."))

# ---------- S14 ----------
scene(n=14, fiil="YERLEŞTİRİR", eleman="sandalye + nota sehpası + ekipman kutuları vanadan sahneye · küçük topluluk oturur · sıralar boş", rejim="A", t0="17:10", t1="17:20",
 g="G14",
 stage=(FIN + "; " + LAMPS_OFF + ". The hardstand lies raked and empty except for a white van parked beside the ramp "
        "at the left end of the stage, its rear doors open, stacks of folded chairs and cases inside. A stage crew "
        "waits at the ramp, and the terraces stand empty."),
 moment="Ten past five, the last of the sun: the theatre is finished and empty, and the musicians are arriving.",
 comp=C_SHELL + " " + C_TOW,
 light=LIGHT("17:10", "golden"), tr=TR_A,
 act=("A stage crew carries chairs, music stands and black equipment cases from the white van up the side ramp, sets "
      "them out in a wide curve on the front two thirds of the stage, lifts the heavy cases onto a hand cart, a second "
      "crew lays cables to the two towers, and a small group of musicians walks up the ramp with instrument cases. " +
      CREW),
 tex=T_DONE,
 phys=("The van sits on its wheels on the gravel hardstand, the chairs and stands stand on the timber stage, and the "
       "shell is bolted to its ribs on base plates anchored in the stone platform."),
 mf=("The stage crew carries the chairs, music stands and equipment cases from the white van on the hardstand up the "
     "side ramp onto the front of the stage, and the musicians take their places."),
 body=("Ten minutes pass in the last low sunlight. Everything in this shot is time-lapsed at the same rate. From the "
       "first frame the crew is already carrying chairs up the ramp: chairs and stands fill a wide curve on the front "
       "of the stage under the open front of the shell, a crew rolls the heavy cases on a hand cart, cables run to the "
       "towers, and a small ensemble of distant musicians settles on the chairs, still small figures without detail; "
       "the seats in the bowl stay empty. The sun sinks low behind the camera on the left and the last warm light "
       "slides up the shell and the treetops. A few clouds drift slowly from the left."))

# ---------- S15 ----------
scene(n=15, fiil="YAKAR", eleman="alacakaranlık: basamak lambaları → kabuk içi sıcak ışık → yol lambaları gruplar hâlinde · ana sahne ışıkları sönük", rejim="A", t0="17:20", t1="17:30",
 g="G15", iso=400,
 stage=(FIN + "; " + ENS + "; " + LAMPS_OFF + ". The white van stands on the hardstand beside the ramp, and an electrical crew "
        "stands at a switch panel at the left side of the stage. The terraces stand empty."),
 moment="Twenty past five, sunset: the theatre is ready, and its lights are still off.",
 comp=C_SHELL + " " + C_TOW,
 light=LIGHT("17:20", "dusk"), tr=TR_A_DUSK,
 act=("An electrical crew at the switch panel beside the stage switches the lights on group by group, a stage crew sets the last music "
      "stands and lays a cable along the stage edge, and the white service vehicle drives off up the service road. " +
      CREW),
 tex=T_EVE,
 phys=("The van stands on its wheels on the gravel hardstand, the lamps are anchored in the aisle edges and the path edges, "
       "and the light fittings are bolted inside the shell."),
 mf=("The electrical crew switches the lights on from the switch panel at the left side of the stage to the lamps, in "
     "three groups: first the step lamps along the three stair "
     "aisles, then the warm lights inside the shell, last the low lamps along the two entrance paths."),
 body=("Ten minutes pass as the day turns to dusk. Everything in this shot is time-lapsed at the same rate. The sky fades "
       "from pale gold to a soft clear blue and the hollow darkens slowly, never to black. The lights come on in groups, "
       "each group at once: first the small warm step lamps along the three stair aisles, then the warm light on the "
       "timber inside of the shell, last the low lamps along the two paths; the main stage lights on the towers stay "
       "dark. The stage crew carries the last music stand from the stack of cases at the ramp and sets it on the "
       "stage, and the van drives off up the service road. A few clouds drift slowly and fade to blue-grey."))

# ---------- S16 ----------
scene(n=16, fiil="GETİRİR", eleman="ilk seyirci grupları iki yoldan → girişler → üç merdiven → alt + orta sıralar (≈üçte bir)", rejim="A", t0="17:30", t1="17:40",
 g="G16", iso=800,
 stage=(FIN + "; " + ENS + "; " + LAMPS_ON + ". The twelve timber-seated terraces stand empty and ready, and two "
        "ushers stand at each entrance."),
 moment="Half past five, blue hour: the lamps are lit, and the first audience is coming up the paths.",
 comp=C_SHELL + " " + C_TOW,
 light=LIGHT("17:30", "blue"), tr=TR_A_DUSK,
 act=("Ushers at the two entrances wave the first groups in, the audience walks along the two paved paths and down the "
      "three lit aisles to the lower and middle rows, and a stage crew lifts a last case from a hand cart at the ramp "
      "and carries the cart off. " + CROWD_A),
 tex=T_EVE,
 phys=("The seat boards are bolted to steel brackets on the stone terraces, the towers stand bolted on their footings, "
       "and the lamps are anchored in the aisle edges."),
 mf=("The first audience groups walk from the two paved paths through the entrances on the near rim and down the three "
     "stair aisles into the lower and middle rows, where they sit down."),
 body=("Ten minutes pass in the blue hour. Everything in this shot is time-lapsed at the same rate. From the first "
       "frame the first small groups are already coming up the two paths: they stream through the two entrances and "
       "down the three lit aisles, and every person walks to a seat before sitting, row by row into the lower and middle "
       "terraces, until about a third of the seats are taken and the upper rows stay empty. The people show as soft "
       "streaks while they walk and as small still figures once seated, backs to the camera. A stage crew lifts a last "
       "case from a hand cart at the ramp and carries the cart away. The sky deepens slowly to a clear blue, the shell "
       "and the step lamps the brightest things in the frame, and a few clouds drift slowly."))

# ---------- S17 ----------
scene(n=17, fiil="DOLDURUR", eleman="seyirci akışı sürer · üst sıralar dolar (sıraların çoğu) · koridorlar açık · alttakiler yerinde", rejim="A", t0="17:40", t1="17:50",
 g="G17", iso=800,
 stage=(FIN + "; " + ENS + "; " + LAMPS_ON + ". About a third of the seats in the lower and middle rows are taken by a "
        "seated audience, small figures with their backs to the camera, the upper rows still empty; more people walk "
        "along the two paths, and ushers stand at the entrances."),
 moment="Twenty to six, blue hour: the lower rows are full, and the audience keeps coming in.",
 comp=C_SHELL + " " + C_TOW,
 light=LIGHT("17:40", "blue"), tr=TR_A_DUSK,
 act=("The audience keeps streaming in along the two paths and down the three aisles into the upper rows, ushers guide "
      "latecomers to the last free places, and a stage crew lifts a stack of spare chairs onto a hand cart and moves it "
      "down the ramp. " + CROWD_A),
 tex=T_EVE,
 phys=("The seat boards are bolted to steel brackets on the stone terraces, the towers stand bolted on their footings, "
       "and the people are seated on the timber seat boards."),
 mf=("More audience walks from the two paved paths down the three stair aisles into the upper rows, until most seats "
     "are taken and the aisles stay clear."),
 body=("Ten minutes pass in the blue hour. Everything in this shot is time-lapsed at the same rate. The audience keeps "
       "streaming in along the two paths and down the three aisles, each person walking to a seat; the people already "
       "seated in the lower rows stay in their places, and the upper rows fill row by row until most of the twelve "
       "terraces are full and the three aisles stay open. A stage crew rolls a hand cart of spare chairs down the ramp "
       "and carries a stack of cases off to the side. The main stage lights on the towers are still dark. The sky "
       "deepens to a clear deep blue, the treeline and the pines still readable against it, and a few clouds drift "
       "slowly."))

# ---------- S18 ----------
scene(n=18, fiil="AÇAR", eleman="⭐ ana sahne ışıkları kulelerden karanlıktan tama (≈3 sn) · topluluk çalmaya başlar · gerçek zaman", rejim="G", t0="17:50:00", t1="17:50:08",
 g="G18", iso=1600,
 stage=(FIN + "; " + ENS + ", ready to play; " + LAMPS_ON + ". Most seats on the twelve terraces are taken by a seated "
        "audience, small distant figures with their backs to the camera, the three aisles clear; ushers stand at the "
        "two entrances."),
 moment="Ten to six, deep blue hour: the theatre is full, and the stage is about to light up.",
 comp=C_SHELL + " " + C_TOW,
 light=LIGHT("17:50", "blue"), tr=TR_G,
 act=("The lighting crew on the left tower platform brings up the main stage lights, a stagehand sets the last music "
      "stand straight, the musicians lift their instruments, and the audience settles. " + CROWD_G),
 tex=T_EVE,
 phys=("The towers stand bolted on their footings beside the stage, the musicians sit on chairs on the timber stage, "
       "and the audience sits on the timber seat boards bolted to the stone terraces."),
 mf=("The main stage lights on the two towers rise smoothly from dark to full over about three seconds onto the front "
     "of the stage, and the musicians begin to play."),
 body=("Eight seconds pass. Everything in this shot moves at natural speed. In the first three seconds the main stage "
       "lights on both towers rise smoothly from dark to full, washing the front of the stage and the ensemble in warm "
       "light; the musicians raise their instruments and begin to play, small distant figures without detailed hand "
       "movement. The audience sits still, a few heads turning, small natural movements. At the side of the stage a "
       "stagehand carries an empty case from the stack of crates to the ramp. The trees at the edge of the hollow sway "
       "slightly in a light breeze, and the clouds hold still in the deep blue sky."))

# ---------- S19 ----------
scene(n=19, fiil="ALKIŞLATIR", eleman="müzik yükselir · seyirci alkışlar (0–4 sn) · TUTUŞ (4–8 sn) · yeni yapı yok", rejim="G", t0="17:50:08", t1="17:50:16",
 g="G19", iso=1600,
 stage=(FIN + "; " + ENS + ", playing under the full warm light of the main stage lights on both towers; the step "
        "lamps, the shell and the path lamps are lit. Most seats on the twelve terraces are taken by a seated audience, "
        "small distant figures with their backs to the camera, the three aisles clear."),
 moment="Ten to six, deep blue hour: the music has begun in the bowl that was drained this morning.",
 comp=C_SHELL + " " + C_TOW,
 light=LIGHT("17:50:08", "blue"), tr=TR_G,
 act=("The ensemble plays on as the music swells, the audience claps, a stagehand sets a coil of cable beside the "
      "left tower and moves on along the stage edge, and the lighting crew moves along the right tower platform. " + CROWD_G),
 tex=T_EVE,
 phys=("The towers stand bolted on their footings beside the stage, the musicians sit on chairs on the timber stage, "
       "and the audience sits on the timber seat boards bolted to the stone terraces."),
 mf=("The music swells and the audience answers with applause, small natural movements running across the seated "
     "figures from the front rows to the upper rows."),
 body=("Eight seconds pass. Everything in this shot moves at natural speed. In the first four seconds the ensemble plays "
       "on under the warm stage light and the audience breaks into applause, hands moving in small quick movements "
       "across the rows, a few people in the front rows rising to their feet; nothing is built and nothing in the "
       "theatre moves. From about four to eight seconds the scene holds: the stage stays lit, the audience keeps "
       "clapping softly, the treetops sway slightly in the light breeze and the clouds hold still in the deep blue sky; "
       "nothing else changes."))

USTA = dict(g="G20", t="17:50:16", iso=1600,
 stage=(FIN + "; " + ENS + ", playing under the full warm light of the main stage lights on both towers; the step "
        "lamps along the three aisles, the warm light inside the shell and the low path lamps are lit. Most seats on "
        "the twelve terraces are taken by a seated audience, small distant figures with their backs to the camera, the "
        "three aisles clear, a few people in the front rows standing and clapping. The hardstand lies raked and empty."),
 moment="Ten to six on an autumn evening, deep blue hour: the restored theatre is full, and the music has begun.",
 comp=C_SHELL + " " + C_TOW + " The lit stage and shell are the brightest things in the frame.",
 light=LIGHT("17:50:16", "blue"), tr=TR_G,
 act=("The ensemble plays and the audience applauds; a stage crew moves along the right tower platform, and the "
      "treetops sway slightly. " + CROWD_G),
 tex=T_EVE,
 phys=("The towers stand bolted on their footings beside the stage, the shell is bolted to its ribs on base plates "
       "anchored in the stone platform, and the audience sits on the timber seat boards bolted to the stone terraces."))

# ── yazıcılar ───────────────────────────────────────────────────────────────
def lens(iso): return f"Lens: 16 mm rectilinear, f/8, ISO {iso}."

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

RJ = {"A": "A (10 dk)", "B": "B (2 sa)", "G": "G (8 sn · gerçek zaman · ölçülmedi)"}
def blok(d):
    n = d["n"]; bas, son = n * 8, (n + 1) * 8
    out = [f"## 🎬 SAHNE {n} — {d['fiil']}", "",
           "```",
           f"SÜRE: 8,0 s ({bas},0–{son},0)  ·  ELEMAN + ARA HÂL: {d['eleman']}  ·  REJİM: {RJ[d['rejim']]}  ·  SAAT: {d['t0']}→{d['t1']}  ·  İSTASYON: MAIN",
           "```", ""]
    if n in (0, 1, 2):
        out += ["> 💧 **Su kotu** [SU_VE_YANSIMA §8]: tek yön — yalnız ALÇALIR (11. teras → 7. teras → sahnenin üstü → 0);",
                "> çıkış tek (pompalar, G0'dan kadrajda) · yapı su altında da VAR, \"belirmez\" · su gelmez, geri dönmez.", ""]
    if n in (4, 5, 6):
        out += ["> 🧽 **Islaklık defteri**: G5 ıslak (yıkandı) → G6 lekeli kuruyor → G7+ kuru, açık taş. Temizlenen yer bir daha",
                "> kirlenmez; kırık sol merdiven yalnız S5'te onarılır.", ""]
    if n in (15, 16, 17, 18, 19):
        out += ["> 🏮 **Işık defteri** [ISIK_FINALI §2 · §4]: A'da her grup TEK KAREDE yanar (basamak → kabuk → yol); ana sahne",
                "> ışıkları yalnız S18'de, gerçek zamanda (G) karanlıktan tama yükselir. Final güneş −4,9° (−4…−6 penceresi).", ""]
    if d["rejim"] == "G":
        out += ["> 🎻 **Rejim G (8 sn · 1×)** [SANTIYE_HAREKETI §1]: iz YOK; seyirci sırtı kameraya, yüz okunmaz. Final ödülü",
                "> hareketin DOĞAL HIZDA olmasıdır (alkış, rüzgâr). Üç rejim (A · B · G) — PLAN §REJİM SAYISI'nda beyanlı.", ""]
    out += [f"### 📸 GÖRSEL PROMPT ({d['g']})", "", "```", gorsel_main(d, HEAD_MAIN.format(n=n)), "```", ""]
    out += [f"### 🎥 I2V PROMPT ({d['g']} → G{n+1})", "", "```", i2v(d), "```", "", "---", ""]
    return "\n".join(out)

def usta_blok():
    return "\n".join([
        "## 🌟 USTA KARE — G20 (SAHNE DEĞİLDİR · son klibin hedefi · kapak kaynağı)", "",
        "> Üretim sırasının İLK karesi [§8]: G20 önce üretilir ve ikna edici değilse DURULUR; sonra",
        "> image-to-image geriye G19 → G18 → … → G0. Kapı: on iki teras + üç merdiven + sahne + kabuk + iki kule +",
        "> iki yol · sıraların çoğu dolu, koridorlar açık · sahne ışıkları tam, kabuk ve lambalar yanık · gök MAVİ ve",
        "> okunur (güneş −4,9°) · kanıt nesnesi yarık kaya · vinç, pompa, kamyon, palet YOK (SÖKÜM satırı).",
        "> Kapak (`THE_SUNKEN_STAGE_KAPAK.md`) bu promptun kopyası + gök bandı satırıdır [MUZIK_VE_KAPAK §2.2].", "",
        "### 📸 USTA KARE PROMPT (G20)", "", "```",
        gorsel_main(USTA, HEAD_USTA), "```", ""])

H1 = f"""# 🎬 {FILM} — BÖLÜM 1  (S0 – S9 · G0 … G9 + 10 I2V · 0,0–80,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `{FILM}_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır. STRUCTURE, SITE / BACKGROUND ve NEGATIVE blokları bütün karelerde BİREBİR aynı
> kelimelerle tekrarlanır; değişen AT THIS STAGE, THE TIME MOMENT, COMPOSITION'ın son cümleleri, LIGHTING,
> TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.
>
> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py`)
> ki ortak bloklar harfi harfine aynı kalsın [DERS 20].
>
> ⭐ Bu bölümün SON I2V'si (S9: G9 → G10) **G10 karesinde biter** ve G10 `BOLUM_2`'nin ilk görselidir:
> bölüm sınırı bir KAREDİR, kesme değil [DERS 52]. Kapı KLASÖR MODUNDA koşulur:
> `python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/{FILM}`.
>
> ⛔ Vinç kancası [DERS 8]: vinç (G5–G13) her karede ya YÜKLÜ ("with … on the hook on taut slings") ya da bom ucu
> KADRAJ DIŞINDA ("its tip and line above the top edge of the frame"); boş kanca hiçbir promptta yazılmaz.
>
> ⛔ Kelime kilitleri: kahverengi taşkın suyu ("floodwater") yalnız G0–G2 ve S0–S2 I2V'lerinde; "crane" yalnız S4
> I2V'sinden G13'e (S13 I2V dâhil); "seat boards" S6 I2V'sinden, "copper" S10 I2V'sinden ve G11'den, "towers" S11
> I2V'sinden ve G12'den sonra; ışıkların yanması yalnız S15 I2V'sinden sonra; seyirci yalnız S16 I2V'sinden sonra;
> YASAK KELİME (PLAN künyesi) hiçbir promptta yok — negatifte bile.

---
"""

H2 = f"""# 🎬 {FILM} — BÖLÜM 2  (S10 – S19 · G10 … G19 + 10 I2V · 80,0–160,0 sn) + ⭐ USTA KARE G20

> Bölüm 1 ile aynı kurallar: **yalnız sahne blokları**, her prompt self-contained, STRUCTURE ve
> SITE / BACKGROUND birebir, blok etiketleri birebir [DERS 20].
>
> ⛔ **Bölüm 2 "devamı" değildir, ikinci yarıdır.** "Bölüm 1'deki gibi" atfı yasak; model bu
> dosyayı tek başına okuyor. İLK görsel **G10** bölüm 1'in son I2V'sinin HEDEF karesidir — aynı
> kare, iki dosyada bir kez yazılır (burada); bölüm 1'in S9 I2V'si onu "second provided image" olarak alır.
>
> 🏮 **S15 → S19 TEK AKŞAMDIR**: ışık grupları S15'te sırayla yanar ve bir daha sönmez; seyirci S16–S17'de yalnız
> iki yoldan ve üç merdivenden gelir, oturan kalkıp kaybolmaz; S18–S19 gerçek zamandadır (rejim G).
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
        r = ((az + 180 - BEARING) + 180) % 360 - 180
        return f"{r:+d}°" if e > 0 else "—"
    for d in S + [USTA]:
        t = d["t"] if "t" in d else d["t0"]
        az, e = sun(hm(t))
        print(d["g"], t, f"{az}°", f"{e:.1f}°".replace(".", ","), golge(t), f"bağıl güneş {((az - BEARING + 180) % 360) - 180:+d}°")
    sys.exit(0)

if "--kadraj" in sys.argv:
    print("ufuk (üstten)", UFUK, "· %", pct(UFUK), "· f", round(F_PX), "px")
    rows = [("ağaç çizgisi 200 m", (0, 200, 22)), ("yarık kaya sol", (-69, 52, 18)), ("yarık kaya sağ", (-59, 52, 18)),
            ("yarık kaya tepe", (-64, 52, 23)), ("yarık kaya dip", (-64, 52, 13)),
            ("çam 1 dip", (88, 110, 12)), ("çam 1 tepe", (88, 110, 32)), ("çam 2 dip", (96, 118, 13)), ("çam 2 tepe", (96, 118, 34)),
            ("arka duvar sol", (-34, 16, 7)), ("arka duvar orta", (0, 16, 7)), ("arka duvar sağ", (34, 16, 7)),
            ("sahne ön sol", (-13, -3, 1.2)), ("sahne ön sağ", (13, -3, 1.2)), ("sahne arka sol", (-13, 10, 1.2)),
            ("sahne arka sağ", (13, 10, 1.2)), ("sahne merkez", (0, 3.5, 1.2)),
            ("kabuk taban sol", (-11, 5.7, 1.6)), ("kabuk taban sağ", (11, 5.7, 1.6)), ("kabuk tepe (arka)", (0, 10, 13.2)),
            ("kabuk ön dudak", (0, 5.7, 11)), ("kule sol dip", (-16, 2, 1.2)), ("kule sol tepe", (-16, 2, 10.2)),
            ("kule sağ dip", (16, 2, 1.2)), ("kule sağ tepe", (16, 2, 10.2)),
            ("vinç (hardstand)", (-26, 10, 0.2)), ("pompalar", (-48, 12, 8)), ("tank sırası a", (-56, 18, 9)), ("tank sırası b", (-44, 20, 7)),
            ("servis yolu (sol kenar)", (-62, 4, 11)), ("servis yolu orta", (-36, 8, 4)), ("hardstand", (-25, 9, 0.2)),
            ("sol merdiven dip", pol(16, -30, 0)), ("sol merdiven tepe = sol giriş", pol(30.4, -30, 7.2)),
            ("orta merdiven dip", pol(16, 0, 0)), ("orta merdiven tepe", pol(30.4, 0, 7.2)),
            ("sağ merdiven tepe = sağ giriş", pol(30.4, 30, 7.2)), ("hasar 4. teras", pol(19.6, -30, 1.8)), ("hasar 6. teras", pol(22, -30, 3.0)),
            ("yol sol (kenara)", (-17, -32, 8)), ("yol sağ (kenara)", (17, -32, 8)),
            ("dış kenar φ −90", pol(30.4, -90, 7.2)), ("dış kenar φ −60", pol(30.4, -60, 7.2)), ("dış kenar φ 0", pol(30.4, 0, 7.2)),
            ("dış kenar φ +60", pol(30.4, 60, 7.2)), ("dış kenar φ +90", pol(30.4, 90, 7.2)),
            ("orkestra kenarı φ 0", pol(16, 0, 0))]
    for ad, Q in rows:
        x, y = proj(Q); print(f"{ad:32s} x {x:5d} · üstten {y:4d} · %{pct(y)}")
    for L in (6.1, 4.1, 1.5):
        k, r = WL(L); m, s = proj(pol(r, 0, L)), proj(pol(r, -90, L))
        print(f"su +{L} → {k}. terasın dibi · orta üstten {m[1]} (%{pct(m[1])}) · yanlar {s[1]} (%{pct(s[1])}) · x {s[0]}–{1920 - s[0]}")
    for ad, Q in [("sahne", (0, 3.5, 1.2)), ("6. teras", (0, -22, 3.0)), ("dış kenar", (0, -30.4, 7.2))]:
        a, b = proj(Q), proj((Q[0], Q[1], Q[2] + 1.7)); print(f"insan (1,7 m) {ad}: {a[1] - b[1]} px")
    print("sahneye bakış", round(math.degrees(math.atan((CAM_H - 1.2) / (CAM_D + 3.5))), 1), "° · sahneye uzaklık",
          round(math.dist((0, -CAM_D, CAM_H), (0, 3.5, 1.2)), 1), "m · kayaya", round(math.dist((0, -CAM_D, CAM_H), (-64, 52, 18)), 1), "m")
    sys.exit(0)

b1 = H1 + "\n" + "\n".join(blok(d) for d in S if d["n"] <= B1_SON)
b2 = H2 + "\n" + "\n".join(blok(d) for d in S if d["n"] > B1_SON) + "\n" + usta_blok()
open(os.path.join(OUT, f"{FILM}_BOLUM_1.md"), "w").write(b1)
open(os.path.join(OUT, f"{FILM}_BOLUM_2.md"), "w").write(b2)
print("yazıldı", len(b1), len(b2))
