# THE SKY CANAL — bölüm dosyası üretici (ortak bloklar tek kaynaktan, DERS 20)
# KULLANIM (depo kökünden):
#   python3 yatay_2_dk_filmler/THE_SKY_CANAL/00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py yatay_2_dk_filmler/THE_SKY_CANAL
#   → THE_SKY_CANAL_BOLUM_1.md + _BOLUM_2.md yeniden yazılır; ardından prompt_kontrol.py klasör modunda koşulur.
#   --tablo  → PLAN kare tablosu satırlarını basar (saat · azimut · yükseklik · kadrajda gölge yönü)
#   --kadraj → PLAN DEĞİŞMEZLER px satırlarını basar (iğne deliği izdüşümü, tilt 17°)
# ⛔ ÜRETİM BAŞLADIKTAN SONRA KOŞULMAZ: üretilmiş filmin promptu kanıttır (URETIM_GUNLUGU kuralı).
# ⛔ Bölüm dosyası elle düzeltilirse bu betik o düzeltmeyi EZER — düzeltme önce buraya yazılır.
# Kalıp: TEK istasyon (20/20 klip ana kamera), bölüm sınırı G10. Sahibin S01–S20'si = depo S0–S19.
# Rejim: A (10 dk) · B (2 sa: S3 · S8 · S11) · Y (≈1 dk: S17–S19 tekne — YENİ, ölçülmedi · hikâye SAPMA ③).
import math, os, sys

FILM = "THE_SKY_CANAL"
OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
N_SAHNE = 20
B1_SON = 9          # BOLUM_1 = S0–S9 · BOLUM_2 = S10–S19 + USTA (sınır G10)
BEARING = 20        # kamera bakışı (KKD) — vadinin yukarısına bakar

# ── güneş (47° K · δ −9° · ekim ortası · güneş saati) ───────────────────────
phi, dec = math.radians(47.0), math.radians(-9.0)
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
    return f"Sun azimuth {az} degrees, elevation {max(1, round(e))} degrees"

# ── kadraj (iğne deliği · 24 mm · 36 × 20,25 mm · 1920 × 1080) ─────────────
# Dünya: x sağa, y kameradan ileri, z nehir suyundan yukarı (m). Kamera (0, 0, 85), tilt 17° aşağı.
# Köprü ekseni: merkez (5, 135), eksen x'ten 20° (sağ uç uzakta). s = eksen boyunca (merkezden, sağ +),
# off = enine (+ uzak taraf), z = kot. Oluk iç genişliği 8 m (off −4…+4), taban +35,0, duvar tepesi +37,0,
# dolu su +36,5 (duvarın dörtte üçü), kiriş altı +31,5. Ayaklar s ±20, kıyı mesnetleri s ±50.
CAM_H, TILT = 85.0, 17.0
XC, YC, AL = 5.0, 135.0, 20.0
_a = math.radians(AL); AX = (math.cos(_a), math.sin(_a)); NX = (-math.sin(_a), math.cos(_a))
def W(s, off, z): return (XC + AX[0] * s + NX[0] * off, YC + AX[1] * s + NX[1] * off, z)
def proj(P):
    x, y, z = P; vz = z - CAM_H; t = math.radians(TILT)
    Zc = y * math.cos(t) - vz * math.sin(t); Yc = y * math.sin(t) + vz * math.cos(t)
    return round(960 + 1280 * x / Zc), round(540 - 1280 * Yc / Zc)
def P(s, off, z): return proj(W(s, off, z))
def pct(y): return round(100 * (1 - y / 1080))
UFUK = round(540 - 1280 * math.tan(math.radians(TILT)))

# ── ortak bloklar ───────────────────────────────────────────────────────────
HEAD_MAIN = ("Photorealistic documentary site photograph — Scene {n} of 20. Horizontal 16:9 time-lapse of a steel "
             "canal bridge being built high across a green river valley, from a fixed 24 mm site camera.")
HEAD_USTA = ("Photorealistic documentary site photograph — master frame G20, the target frame of the last shot "
             "(Scene 19 of 20). Horizontal 16:9 time-lapse of a steel canal bridge built high across a green river "
             "valley; a progress photograph from a fixed 24 mm site camera.")
CAM_MAIN = ("Camera: MAIN STATION — fixed tripod bolted to a rock ledge high on the left valley slope, lens 85 "
            "metres above the river, 135 metres from the middle of the bridge along the lens axis, bearing 20 degrees, "
            "tilt 17 degrees down, zero roll. The camera never moves.")
STRUCT = ("STRUCTURE: When finished this will be a navigable steel canal bridge: an open-topped steel water trough "
          "100 metres long, 8 metres wide inside and 2 metres deep, carried high over the valley on three spans by two "
          "tall pale concrete piers and two bank abutments, with a walkway and railing along its near side and a "
          "vertical-lift steel gate at each end where it meets the canal on each bank.")
SITE_MAIN = ("SITE / BACKGROUND: A deep green river valley with steep wooded slopes, seen from high on its left "
             "side looking up the valley. A natural river about fifteen metres wide runs down the valley floor between "
             "pale gravel flats towards the camera, far below the line of the bridge, a rough track beside it. Upstream "
             "two long wooded ridges meet a level skyline. On the left bank a short water-filled canal arm along the "
             "hillside widens into a basin before the left gate frame, and a fixed steel filling pipe with a large "
             "valve wheel runs from the basin over that frame. On the right bank a short water-filled canal arm leads "
             "from the right gate frame into the trees. Gravel service roads come in from both side edges to a work "
             "pad on each bank. A single tall dark pine with a flat crown stands on a rock outcrop on the right slope "
             "below the right bank.")
NEG_MAIN = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The valley slopes, the river, the "
            "skyline ridges, the roads, the canal arms and the pine never change shape, position, size or spacing. The "
            "valley holds exactly one canal bridge, this one, on exactly two piers, and exactly one boat. Nothing "
            "already built is removed or resized; no opacity fades. Water stays inside the canal arms and the trough. "
            "No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here "
            "has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No "
            "architectural visualisation look, no CGI aesthetic.")
OUTPUT = "Output: 16:9, 4K, no text, no watermark."
CREW = "Crew show only as faint soft motion streaks, never as sharp figures."
CREW_Y = ("People are small figures with only faint soft motion streaks as they move, backs to the camera, no "
          "readable faces.")
FILMSTOCK = "A documentary site photograph on colour negative film, true colour, fine grain."

# kadraj sayıları (betik hesaplar; PLAN DEĞİŞMEZLER bu çıktıyı yazar)
_pL, _pR = P(-50, -4, 37.0), P(50, -4, 37.0)
_pineL, _pineR, _pineT = proj((43, 98, 40)), proj((49, 98, 40)), proj((46, 98, 48))
_lpier, _rpier = P(-20, -5, 31.5), P(20, -5, 31.5)
_bs, _bb = P(-82, -3, 36.5), P(-64, -3, 36.5)
_riv = proj((5, 135, 0))
COMP_HEAD = (f"COMPOSITION: Horizontal 16:9, the camera looking down 17 degrees, the level skyline at about "
             f"{pct(UFUK)} percent of frame height. The dark pine spans about {_pineR[0] - _pineL[0]} pixels of frame "
             f"width, from about {_pineL[0]} to {_pineR[0]} pixels from the left, its crown top at about "
             f"{pct(_pineT[1])} percent, and keeps that width and position in every frame. The abutments stand at about "
             f"{_pL[0]} and {_pR[0]} pixels, the piers at about {_lpier[0]} and {_rpier[0]} pixels from the left. ")
C_GAP = (f"The open gap between the two pier tops spans about {_rpier[0] - _lpier[0]} pixels of frame width, at about "
         f"{pct(_lpier[1])} to {pct(_rpier[1])} percent of frame height.")
C_LINE = (f"The bridge runs in one straight line from about {_pL[0]} to {_pR[0]} pixels from the left, its near "
          f"top edge falling gently from about {pct(_pL[1])} to {pct(_pR[1])} percent of frame height.")
C_BOAT = (f"The red boat lies in the left basin from about {_bs[0]} to {_bb[0]} pixels from the left, at about "
          f"{pct((_bs[1] + _bb[1]) // 2)} percent of frame height.")
C_RIVER = f"The river passes under the centre span at about {_riv[0]} pixels from the left."
COMP_TAIL = "Nothing that proves progress falls into the bottom tenth or the top-right corner of the frame."

TR_A = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and "
        "crew all move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, "
        "clouds drift smoothly, the river is smoothed to a soft sheen, machines move fast with light "
        "motion blur.")
TR_B = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, water, machines and "
        "crew all move at the same accelerated speed. Two hours pass across this shot: shadows swing slowly round, "
        "clouds streak across the sky, the river lies flat and glassy, machines smear into heavy motion blur.")
TR_Y = ("TIME RATE: Everything in this frame is time-lapsed at the same rate, gently: clouds, shadows, water, the "
        "boat and people all move about eight times faster than normal. About one minute passes across this shot: "
        "shadows stay put, clouds drift slowly, the water moves gently.")

I2V_HEAD = ("The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its "
            "last frame is that image, matched frame for frame — same framing, same light, same objects in the same "
            "places.")
LOCK_MAIN = ("The camera does not move at any point. The framing is identical in the first and last frame. The "
             "valley slopes, the river, the skyline ridges, the canal arms, the two piers and the dark pine on its "
             "rock outcrop stay exactly where they are, at exactly the same size and shape, for the whole shot; the "
             "pine occupies exactly the same width of the frame in the first and last frame. The valley holds "
             "exactly one canal bridge and exactly one boat. Nothing already built is removed or resized.")
I2V_TAIL = ("Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
            "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
            "documentary time-lapse cinematography.")

# ── tekrarlanan durum cümleleri (aynı nesne her karede aynı kelimelerle) ─────
PIERS = ("the two tall pale concrete piers stand on the lower slopes either side of the river, the two abutments at "
         "the bank edges")
GATES_SHUT = "both steel gates stand closed in their frames"
GATES_UP = "both steel gates are raised high in their frames, so the trough lies open to the canal arm on each bank"
BOAT_WAIT = ("one small red canal boat with a cream cabin lies moored along the near bank of the left basin, its "
             "hull low in the still water")
CRANE_L = "a large yellow crawler crane with a grey lattice boom stands on its tracks on the left work pad beyond the basin"
CRANE_R = "a second one stands on its tracks on the right work pad"
def UP(c): return c + ", its boom raised steeply, its tip and line above the top edge of the frame"
def HOOK(c, x): return c + f", with {x} on the hook on taut slings"
GIRD = "two deep steel girders in light grey primer"
CRIB = "the long centre span section lies on timber cribbing on the gravel flats far below, straddling the river"
TRUCKS = lambda x: f"A flatbed truck loaded with {x} stands on each work pad."
def U(x): return x[0].upper() + x[1:]

# oluk durum zinciri (her kare öncekine EKLER — monoton büyüme)
T_SPANS = ("the three span sections now reach from bank to bank in one straight line: " + GIRD + " run side by side "
           "over both piers")
T_GRID = T_SPANS + ", tied together by evenly spaced steel cross beams, the river still showing far below between them"
T_FLOOR = T_SPANS + ", carrying one continuous flat steel floor in light grey primer, open to the sky"
T_FAR = T_FLOOR + ", with a tall steel wall along its far edge"
T_U = ("the open-topped steel trough runs from bank to bank in one straight line over both piers: " + GIRD +
       " carry a flat steel floor between two tall steel walls, all in light grey primer")
T_JOIN = T_U + ", its ends joined to the gate frames on both abutments"
T_BLUE = ("the open-topped steel trough runs from bank to bank over both piers, grey outside, its ends joined to the "
          "gate frames, lined inside from end to end with a dry matte pale blue lining")
T_WALK = T_BLUE + "; a galvanised walkway on brackets runs along its near wall, with steel access steps at each end"
T_RAIL = T_WALK + " and a railing along its outer edge"
T_CHAR = T_RAIL.replace("grey outside", "deep charcoal grey outside")

# ── doku ────────────────────────────────────────────────────────────────────
T_EARLY = ("Tyre ruts and tracks in the gravel of the work pads, a film of dust on the crane tracks, streaks of light "
           "grey primer on the girders with rust stains at the bolt holes, stacks of timber blocking. " + FILMSTOCK)
T_BEAMS = ("Light grey primer on the girders and cross beams with scuffed patches and rust stains at the bolts, a "
           "film of dust along the top flanges, stacks of beams and pallets on the pads, tyre ruts and tracks in "
           "the gravel, dark water stains below the pier tops. " + FILMSTOCK)
T_DECK = ("Light grey primer on the floor and wall panels with scuff marks and boot prints in a film of dust, pallets "
          "and offcuts on the work pads, tyre ruts and tracks in the gravel, dark water stains below the pier "
          "tops. " + FILMSTOCK)
T_LINE = ("A crisp band where the dry matte lining meets the grey primer, faint overspray streaks on the wall tops, "
          "coating drums stacked on pallets, tyre ruts and tracks in the gravel, a film of dust on the crane "
          "tracks. " + FILMSTOCK)
T_GALV = ("Bright galvanised gratings and railings with a dull sheen, light grey primer on the outer faces with "
          "scuff patches, the dry matte lining under a thin film of dust, pallets and offcuts on the pads, tyre "
          "ruts in the gravel. " + FILMSTOCK)
T_PAINT = ("Fresh charcoal coating with a soft satin sheen beside bands of light grey primer, overspray streaks on "
           "the walkway edge, empty pallets stacked on the pads, tyre ruts and tracks in the gravel, a film of dust "
           "on the crane tracks. " + FILMSTOCK)
T_DONE = ("Even charcoal coating with a soft satin sheen, the dry matte lining under a thin film of dust, raked "
          "gravel on the empty work pads with the faint print of tyre tracks, pale patches where the stacks stood, "
          "dark water stains below the pier tops. " + FILMSTOCK)
T_SHEET = ("A thin sheet of clear water over the pale blue lining with a soft sheen of sky, the dry matte lining "
           "beyond its leading edge, raked gravel on the work pads with the faint print of tyre tracks, a film of "
           "dust on the walkway gratings, dark water stains below the pier tops. " + FILMSTOCK)
T_FULL = ("Calm clear water over the pale blue lining with a soft sheen of sky, a narrow dry band of lining above "
          "the water line, charcoal coating with a satin sheen, a film of dust on the walkway gratings, raked "
          "gravel with the faint print of tyre tracks, dark water stains below the pier tops. " + FILMSTOCK)

# ── ışık (bakış 20° — güneş hiçbir karede kadrajda değil: sabah sağda, öğle arkada, akşam arkada solda) ──
LIGHT_DESC = {
 "morning": ("low on the right of the camera, outside the frame: cool clear morning light from the right, long "
             "shadows falling to the left across the valley, the valley floor still in soft shade."),
 "am": ("on the right behind the camera: clear bright light from the right, the shadows falling to the left and "
        "away from the camera."),
 "noon": ("high behind the camera on the right: the light falls almost straight onto the faces turned to the "
          "camera, and short shadows fall to the left and away."),
 "pm": ("behind the camera on the left: warm afternoon light from the left, the shadows falling to the right and "
        "away from the camera."),
 "late": ("low behind the camera on the left: warm low afternoon light from the left, long shadows falling to the "
          "right across the valley."),
 "golden": ("low behind the camera on the left, outside the frame: warm golden late light on the bridge, the "
            "slopes and the water, the valley floor already in soft shade, long shadows to the right."),
}
SEASON = {
 "spring": "Late spring: the woods on the valley slopes are fresh light green.",
 "summer": "Summer: the woods on the valley slopes are deep full green.",
 "late": "Late summer: the woods on the slopes are deep green with the first dry yellow patches.",
 "autumn": "Autumn: the woods on the slopes are turning gold, orange and rust; the pine stays dark green.",
}
def LIGHT(t, key, season):
    return f"LIGHTING: {sunline(t)}, {LIGHT_DESC[key]} {SEASON[season]} The sun stays outside the frame."

# ── sahne verisi ─────────────────────────────────────────────────────────────
S = []
def scene(**k): S.append(k)

# ---------- S0 ----------
scene(n=0, fiil="OTURTUR", eleman="sol açıklık parçası ilk karede ASILI → sol mesnet + sol ayağa oturur (%100)", rejim="A", t0="08:20", t1="08:30",
 g="G0",
 stage=("the steel canal bridge is about to be built: " + PIERS + ", " + GATES_SHUT + ". The left span section — "
        + GIRD + ", braced together, thirty metres long — already hangs level on four taut slings from the left "
        "crane a metre above its bearings between the left abutment and the left pier. The right span section "
        "lies on timber blocking on the right work pad, four slings hooked to it from the second crane, and " + CRIB
        + " under the open gap. " + U(CRANE_L) + "; " + CRANE_R + ". " + U(BOAT_WAIT) + "."),
 moment="A cool morning in late spring, the first day of the lifts: the first span is already in the air over the gap.",
 comp=C_GAP + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("08:20", "morning", "spring"),
 tr=TR_A,
 act=("The left crawler crane lowers the left span section onto its bearings on the left abutment and the left "
      "pier, a crew on the pier top guides it in with taglines, and a second crew on the right work pad checks "
      "the slings on the right span section; the crane carries a visible load. " + CREW),
 tex=T_EARLY,
 phys=("The left span section hangs from the crane hook on four taut slings. The crawler cranes stand on their "
       "tracks on the gravel. The piers stand on their footings on the slopes, and the boat sits moored in the "
       "basin."),
 mf=("The left crawler crane lowers the left span section on its four slings from just above its bearings onto "
     "the left abutment and the left pier, and the slings fall slack."),
 body=("Ten minutes pass in the cool morning light. Everything in this shot is time-lapsed at the same rate. From "
       "the first frame the span section is already moving: it sinks slowly and level the last metre onto its "
       "bearings while the crew on the pier top steadies it with taglines; it does not bounce, and the slings fall "
       "slack once it rests. Beyond it the gap between the two piers stays open, and the centre span section waits "
       "on its cribbing far below over the river. The red boat lies still in the left basin. A flatbed truck brings "
       "a load of timber blocking along the left service road. At the end the left crane raises its boom steeply until "
       "its tip and line rise above the top edge of the frame. Thin high clouds drift slowly from the right in one "
       "smooth flow, and the river runs smooth far below."))

# ---------- S1 ----------
scene(n=1, fiil="YERLEŞTİRİR", eleman="sağ açıklık parçası sağ pedden → sağ ayak + sağ mesnede (%100) · kısa yol", rejim="A", t0="08:30", t1="08:40",
 g="G1",
 stage=("the first span is in place: " + PIERS + ", " + GATES_SHUT + ". The left span section of " + GIRD + " rests "
        "on its bearings on the left abutment and the left pier. The right span section lies on timber blocking on "
        "the right work pad, four slings rising taut from it to the hook of the second crane, and " + CRIB + " under "
        "the open gap. " + U(UP(CRANE_L)) + "; " + CRANE_R + ". " + U(BOAT_WAIT) + "."),
 moment="Half past eight in the morning: one span stands over the valley, and the second is slung for lifting.",
 comp=C_GAP + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("08:30", "morning", "spring"),
 tr=TR_A,
 act=("The right crawler crane lifts the right span section off its blocking, carries it slowly and level a short "
      "way out over the right slope and lowers it onto its bearings on the right pier and the right abutment, a "
      "crew on the pier top guides it with taglines, and a second crew stacks the freed blocking on the right "
      "work pad; the crane carries a visible load. " + CREW),
 tex=T_EARLY,
 phys=("The right span section hangs from the crane hook on four taut slings. The left span section rests on its "
       "bearings on the abutment and the pier. The crawler cranes stand on their tracks on the gravel, and the "
       "boat sits moored in the basin."),
 mf=("The right crawler crane lifts the right span section from its timber blocking on the right work pad and "
     "carries it level on four slings onto its bearings on the right pier and the right abutment."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the right "
       "span section is already rising off its blocking: it travels slowly and level, in one piece, a short way out "
       "over the right slope and sinks onto its bearings, where the crew steadies it; the slings fall slack. Now "
       "only the centre gap between the two piers stays open, with the centre span section waiting on its cribbing "
       "far below. The crew stacks the freed timber blocking in a pile on the right work pad, and the right crane "
       "raises its boom steeply until its tip and line rise above the top edge of the frame. At the end the left "
       "crane swings its boom out over the valley and the crew on the gravel flats hooks its four long slings to "
       "the centre span section. The red boat lies still in the basin. Long shadows fall to the left, and thin "
       "high clouds drift slowly from the right."))

# ---------- S2 ----------
scene(n=2, fiil="BİRLEŞTİRİR", eleman="merkez parça vadi dibindeki kalastan → DİMDİK yukarı → iki ayağın arasına (%100) · ⭐ kıyılar birleşir", rejim="A", t0="08:40", t1="08:50",
 g="G2",
 stage=("two spans are in place: " + PIERS + ", " + GATES_SHUT + ". The left and right span sections of " + GIRD +
        " rest on their bearings, reaching out from both banks to the two piers, and between the pier tops the "
        "centre gap is still open. " + U(CRIB) + ", four long slings rising taut from it to a steel spreader beam "
        "on the hook of the left crane. " + U(CRANE_L) + ", its boom swung out over the valley; " + UP(CRANE_R) + ". "
        + U(BOAT_WAIT) + ". A pile of freed timber blocking lies on the right work pad."),
 moment="Twenty to nine in the morning: two spans reach out from the banks, and the last piece waits far below.",
 comp=C_GAP + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("08:40", "morning", "spring"),
 tr=TR_A,
 act=("The left crawler crane lifts the centre span section straight up off its cribbing, a crew on the two "
      "pier tops guides it with taglines, and a second crew on the gravel flats pulls the freed timbers clear; the "
      "crane carries a visible load. " + CREW),
 tex=T_EARLY,
 phys=("The centre span section hangs from the crane hook on four long taut slings. The side span sections "
       "rest on their bearings on the piers and the abutments. The crawler cranes stand on their "
       "tracks on the gravel, and the boat sits moored in the basin."),
 mf=("The left crawler crane lifts the centre span section straight up from its timber cribbing on the gravel flats "
     "beside the river onto its bearings on the two piers, between the ends of the two side spans."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the centre "
       "span section is already lifting off its cribbing: it rises slowly, straight up and level, in one piece, "
       "past the faces of the two tall piers, high above the river, and comes to rest on its bearings between the "
       "ends of the two side spans; the slings fall slack. For the first time one continuous line of steel reaches "
       "from bank to bank across the valley. On the gravel flats far below the crew pulls the freed cribbing "
       "timbers into a pile beside the river. At the end a flatbed truck loaded with steel cross beams drives onto "
       "each work pad, and both cranes lift a bundle from it. The red boat lies still in the basin. The shadows "
       "shorten a little, and small high clouds drift slowly from the right."))

# ---------- S3 ----------
scene(n=3, fiil="BAĞLAR", eleman="enine kirişler iki uzun kirişin arasına (%0 → %100, iki uçtan ortaya) · ızgara", rejim="B", t0="08:50", t1="10:50",
 g="G3",
 stage=(T_SPANS + ", open between them, the river showing far below. " + U(PIERS) +
        ", " + GATES_SHUT + ". " + U(HOOK(CRANE_L, "a bundle of steel cross beams")) + "; " + HOOK(CRANE_R, "a bundle "
        "of steel cross beams") + ". " + TRUCKS("steel cross beams") + " A pile of cribbing timbers lies beside the "
        "river. " + U(BOAT_WAIT) + "."),
 moment="Ten to nine in the morning: the banks are joined by steel, and the cross beams have arrived.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("08:50", "morning", "spring"),
 tr=TR_B,
 act=("Both crawler cranes lift bundles of steel cross beams from the flatbed trucks onto the girders, a crew on "
      "the girders sets the beams one by one between the two girders and bolts them from both banks towards the "
      "middle, and a small truck on the gravel flats hauls the cribbing timbers away; the cranes carry a visible "
      "load. " + CREW),
 tex=T_BEAMS,
 phys=("The bundles hang from the crane hooks on two slings each. The span sections rest on their bearings on the "
       "piers and the abutments, and the beams already set are bolted between the girders. The crawler cranes "
       "stand on their tracks on the gravel."),
 mf=("The two crawler cranes lift the steel cross beams from the flatbed trucks on the work pads onto the girders, "
     "and the crew bolts them between the two girders one after another from both banks to the middle."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Beam by beam from both ends the "
       "open space between the two long girders fills with evenly spaced steel cross beams, until a regular ladder "
       "of beams runs the whole length of the bridge; through the gaps between them the river still shows far "
       "below. The emptied trucks drive off, a loaded truck brings more beams along each service road, and at the "
       "end a truck loaded with pallets of floor panels arrives on each pad and both cranes lift a pallet from it. A small "
       "truck on the gravel flats loads the cribbing timbers from the pile and drives off down the track. The "
       "shadows of the piers swing slowly across the slopes as the sun climbs on the right, and clouds streak "
       "across the sky."))

# ---------- S4 ----------
scene(n=4, fiil="KAPATIR", eleman="taban panelleri ızgaranın üstüne (%0 → %100, iki uçtan) · nehir aralıkları kapanır", rejim="A", t0="10:50", t1="11:00",
 g="G4",
 stage=(T_GRID + ". " + U(PIERS) + ", " + GATES_SHUT + ". " + U(HOOK(CRANE_L, "a pallet of wide steel floor "
        "panels")) + "; " + HOOK(CRANE_R, "a pallet of wide steel floor panels") + ". " + TRUCKS("pallets of wide "
        "steel floor panels") + " " + U(BOAT_WAIT) + "."),
 moment="Ten to eleven in the morning, early summer: the steel ladder is complete, and the floor panels are next.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("10:50", "am", "summer"),
 tr=TR_A,
 act=("Both crawler cranes lift the pallets of wide steel floor panels from the flatbed trucks onto the cross beams, "
      "and a crew lays the panels side by side and bolts them down from both banks towards the middle; the cranes "
      "carry a visible load. " + CREW),
 tex=T_BEAMS,
 phys=("The pallets hang from the crane hooks on four slings each. The cross beams are bolted between the girders, "
       "and the span sections rest on their bearings on the piers. The crawler cranes stand on their tracks on the "
       "gravel."),
 mf=("The two crawler cranes lift the pallets of wide steel floor panels from the flatbed trucks onto the cross "
     "beams, and the crew lays the panels from both banks towards the middle."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first "
       "pallets are already swinging in over the girders: panel by panel from both ends the gaps between the cross "
       "beams close, the river far below hidden strip by strip, until one continuous flat steel floor runs the "
       "whole length of the bridge, dry and open to the sky. The emptied trucks drive off along the service roads, "
       "and at the end a truck loaded with tall wall panels arrives on each pad and both cranes lift a panel from it. The red boat lies still in the basin. Short shadows fall to the left, "
       "and a few small clouds drift slowly from the right."))

# ---------- S5 ----------
scene(n=5, fiil="YÜKSELTİR", eleman="uzak kanal duvarı paneller (%0 → %100, iki uçtan ortaya)", rejim="A", t0="11:00", t1="11:10",
 g="G5",
 stage=(T_FLOOR + ". " + U(PIERS) + ", " + GATES_SHUT + ". " + U(HOOK(CRANE_L, "a tall steel wall panel")) + "; "
        + HOOK(CRANE_R, "a tall steel wall panel") + ". " + TRUCKS("tall steel wall panels") + " " + U(BOAT_WAIT)
        + "."),
 moment="Eleven in the morning: the floor is closed, and the first wall panels hang over the far edge.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("11:00", "am", "summer"),
 tr=TR_A,
 act=("Both crawler cranes lift the tall steel wall panels from the flatbed trucks onto the far edge of the bridge, and "
      "a crew sets each panel upright and bolts it along the far girder from both banks towards the middle; the "
      "cranes carry a visible load. " + CREW),
 tex=T_DECK,
 phys=("The wall panels hang from the crane hooks on two slings each. The panels already set are bolted upright to "
       "the far girder, and the span sections rest on their bearings on the piers. The crawler cranes stand on "
       "their tracks on the gravel."),
 mf=("The two crawler cranes lift the tall steel wall panels from the flatbed trucks onto the far edge of the "
     "bridge, and the crew bolts them upright along the far girder from both banks to the middle."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first "
       "panels are already swinging in: panel by panel from both ends a tall steel wall rises along the far edge of "
       "the floor, until it runs unbroken from bank to bank at one even height, and the bridge begins to read as a "
       "channel. The emptied trucks drive off, and a loaded truck brings more panels along each service road. The red "
       "boat lies still in the basin. Short shadows fall to the left, and a few small clouds drift slowly from the "
       "right."))

# ---------- S6 ----------
scene(n=6, fiil="TAMAMLAR", eleman="yakın kanal duvarı paneller (%0 → %100) · üstü açık U oluk", rejim="A", t0="11:10", t1="11:20",
 g="G6",
 stage=(T_FAR + ". " + U(PIERS) + ", " + GATES_SHUT + ". " + U(HOOK(CRANE_L, "a tall steel wall panel")) + "; "
        + HOOK(CRANE_R, "a tall steel wall panel") + ". " + TRUCKS("tall steel wall panels") + " " + U(BOAT_WAIT)
        + "."),
 moment="Ten past eleven in the morning: the far wall stands, and the near wall follows.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("11:10", "am", "summer"),
 tr=TR_A,
 act=("Both crawler cranes lift the tall steel wall panels from the flatbed trucks onto the near edge of the bridge, "
      "and a crew sets each panel upright and bolts it along the near girder from both banks towards the middle; "
      "the cranes carry a visible load. " + CREW),
 tex=T_DECK,
 phys=("The wall panels hang from the crane hooks on two slings each. The far wall is bolted upright to the far "
       "girder, and the span sections rest on their bearings on the piers. The crawler cranes stand on their "
       "tracks on the gravel."),
 mf=("The two crawler cranes lift the tall steel wall panels from the flatbed trucks onto the near edge of the "
     "bridge, and the crew bolts them upright along the near girder from both banks to the middle."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first "
       "near panels are already swinging in: panel by panel from both ends a matching wall rises along the near "
       "edge, until the bridge is one long open-topped steel trough, its inside still showing over the near wall "
       "top. The emptied trucks drive off, and a loaded truck brings short steel end sections along each service road. "
       "The red boat lies still in the basin. Short shadows fall to the left, and a few small clouds drift slowly "
       "from the right."))

# ---------- S7 ----------
scene(n=7, fiil="BAĞLAR", eleman="oluk uçları ↔ kıyıdaki kapak çerçeveleri (iki kısa uç parçası, %100) · kapaklar KAPALI", rejim="A", t0="11:20", t1="11:30",
 g="G7",
 stage=(T_U + "; at each end a short open joint still separates it from the gate frame on the abutment. "
        + U(PIERS) + ", " + GATES_SHUT + ". " + U(HOOK(CRANE_L, "a short steel end section")) + "; "
        + HOOK(CRANE_R, "a short steel end section") + ". " + TRUCKS("short steel end sections") + " "
        + U(BOAT_WAIT) + "."),
 moment="Twenty past eleven in the morning: the trough is whole, and only the joints to the banks are open.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("11:20", "noon", "summer"),
 tr=TR_A,
 act=("Both crawler cranes lower a short steel end section into the open joint at each end of the trough, and a "
      "crew bolts each one to the trough and to the gate frame on the abutment, while a second crew carries seal "
      "strips from a pallet to the joints; the cranes carry a visible load. " + CREW),
 tex=T_DECK,
 phys=("The end sections hang from the crane hooks on four slings each. The trough rests on its bearings on the "
       "piers and the abutments, and the gate frames are bolted to the abutments. The crawler cranes stand on "
       "their tracks on the gravel."),
 mf=("The two crawler cranes lower the short steel end sections from the flatbed trucks into the joints between the "
     "ends of the trough and the gate frames on both banks, where the crew bolts them closed; the steel gates "
     "stay shut."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the two end "
       "sections are already swinging in over the abutments: each one sinks into its joint and is bolted fast, "
       "until the trough runs unbroken from the left gate frame to the right gate frame. Both steel gates stay shut "
       "in their frames, the water of the canal arms held behind them. The emptied trucks drive off and a loaded "
       "one brings pallets of coating drums along the left service road; at the end the left crane lifts a pallet "
       "of drums from it, and the right crane raises its boom steeply until its tip and line rise above the top "
       "edge of the frame. The red boat lies still in the basin. Short shadows fall away from the camera, and a few small clouds drift slowly from the right."))

# ---------- S8 ----------
scene(n=8, fiil="KAPLAR", eleman="iç yüzey gri astar → açık mavi kaplama (%0 → %100, soldan sağa) · KURU", rejim="B", t0="11:30", t1="13:30",
 g="G8",
 stage=(T_JOIN + "; inside it the floor and walls are bare grey primer, dry. " + U(PIERS) + ", " + GATES_SHUT + ". "
        + U(HOOK(CRANE_L, "a pallet of coating drums")) + "; " + UP(CRANE_R) + ". A flatbed truck loaded with pallets "
        "of coating drums stands on the left work pad. " + U(BOAT_WAIT) + "."),
 moment="Half past eleven, high summer: the trough is joined to both banks, and the coating crew moves in.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("11:30", "noon", "summer"),
 tr=TR_B,
 act=("A crew inside the trough sprays the pale lining onto the dry floor and inner wall faces in bands from the "
      "left end towards the right end, the left crawler crane lowers pallets of coating drums from the flatbed "
      "truck into the trough, and a second crew moves the spray hoses along; the crane carries a visible load. "
      + CREW),
 tex=T_DECK,
 phys=("The pallet hangs from the crane hook on four slings. The trough rests on its bearings on the piers, and "
       "the wall panels are bolted to the girders. The crawler cranes stand on their tracks on the gravel."),
 mf=("A crew inside the trough sprays the pale blue lining from the coating drums onto the dry floor and inner wall "
     "faces from the left end to the right end, and the left crawler crane lowers more drums from the flatbed "
     "truck into the trough."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Band by band from the left the dull "
       "grey inside of the trough turns a clean pale blue, the floor and the inner faces of both walls, until a "
       "long pale blue band runs the whole length of the bridge between the grey walls; the lining stays dry and "
       "matte, without reflections. The emptied truck drives off; at the end a truck loaded with walkway "
       "sections arrives on each pad, and both cranes lift a section from it. The red boat lies still in the basin. The shadows of the piers "
       "swing slowly from the left to behind them as the sun passes behind the camera, and clouds streak across "
       "the sky."))

# ---------- S9 ----------
scene(n=9, fiil="KURAR", eleman="yakın taraf bakım yolu konsollar + ızgaralar (%0 → %100) · uçlarda erişim basamakları", rejim="A", t0="13:30", t1="13:40",
 g="G9",
 stage=(T_BLUE + ". " + U(PIERS) + ", " + GATES_SHUT + ". " + U(HOOK(CRANE_L, "a walkway section")) + "; "
        + HOOK(CRANE_R, "a walkway section") + ". " + TRUCKS("galvanised walkway sections") + " "
        + U(BOAT_WAIT) + "."),
 moment="Half past one in the afternoon: the trough is lined, and the walkway sections have arrived.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("13:30", "pm", "summer"),
 tr=TR_A,
 act=("Both crawler cranes lift the galvanised walkway sections from the flatbed trucks onto steel brackets along the "
      "outside of the near wall, and a crew bolts them down one after another from both banks towards the middle; "
      "the cranes carry a visible load. " + CREW),
 tex=T_LINE.replace("dry matte lining", "dry matte pale blue lining"),
 phys=("The walkway sections hang from the crane hooks on four slings each. The brackets are bolted to the near "
       "wall, and the sections already set rest on them. The crawler cranes stand on their tracks on the gravel."),
 mf=("The two crawler cranes lift the galvanised walkway sections from the flatbed trucks onto the steel brackets "
     "along the outside of the near wall, and the crew bolts them down from both banks to the middle, with steel "
     "access steps at each end."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first "
       "sections are already swinging in: section by section from both ends a narrow galvanised walkway grows along "
       "the outside of the near wall, outside the trough, until it runs the whole length of the bridge, with steel "
       "access steps at each end down to the banks. The emptied trucks drive off and loaded ones bring bundles of "
       "railing modules. The red boat lies still in the basin. Short shadows fall to the right, and a few small "
       "clouds drift slowly from the left."))

# ---------- S10 ----------
scene(n=10, fiil="ÇEVİRİR", eleman="bakım yolu dış kenarına korkuluk modülleri (%0 → %100)", rejim="A", t0="13:40", t1="13:50",
 g="G10",
 stage=(T_WALK + ". " + U(PIERS) + ", " + GATES_SHUT + ". " + U(HOOK(CRANE_L, "a bundle of railing modules"))
        + "; " + HOOK(CRANE_R, "a bundle of railing modules") + ". " + TRUCKS("bundles of railing modules") + " "
        + U(BOAT_WAIT) + "."),
 moment="Twenty to two in the afternoon: the walkway runs from bank to bank, and its railing is next.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("13:40", "pm", "summer"),
 tr=TR_A,
 act=("Both crawler cranes lift bundles of railing modules from the flatbed trucks onto the walkway, and a crew "
      "bolts the modules one after another along its outer edge from both banks towards the middle; the cranes "
      "carry a visible load. " + CREW),
 tex=T_GALV,
 phys=("The bundles hang from the crane hooks on two slings each. The walkway rests on its brackets on the near "
       "wall, and the railing posts are bolted to its edge. The crawler cranes stand on their tracks on the gravel."),
 mf=("The two crawler cranes lift the bundles of railing modules from the flatbed trucks onto the walkway, and the "
     "crew bolts the modules along its outer edge from both banks to the middle."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first "
       "bundles are already swinging in: module by module from both ends one clean, even railing line grows along "
       "the walkway's outer edge, until it runs the whole length of the bridge, the drop below it still open to the "
       "eye. The emptied trucks drive off and a loaded one brings pallets of coating drums along the left service "
       "road; at the end the left crane lifts a pallet of drums from it, and the right crane raises its boom steeply "
       "until its tip and line rise above the top edge of the frame. The red boat lies still in the basin. Short shadows fall to the right, and a few small clouds drift "
       "slowly from the left."))

# ---------- S11 ----------
scene(n=11, fiil="BOYAR", eleman="dış çelik açık gri astar → koyu kömür grisi (%0 → %100, soldan sağa)", rejim="B", t0="13:50", t1="15:50",
 g="G11",
 stage=(T_RAIL + ". " + U(PIERS) + ", " + GATES_SHUT + ". " + U(HOOK(CRANE_L, "a pallet of coating drums")) + "; "
        + UP(CRANE_R) + ". A flatbed truck loaded with pallets of coating drums stands on the left work pad. "
        + U(BOAT_WAIT) + "."),
 moment="Ten to two in the afternoon, late summer: the bridge is fitted out, and only its outer coat is missing.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("13:50", "pm", "late"),
 tr=TR_B,
 act=("A crew on the walkway and on rope lines sprays the dark top coat onto the outer faces of the walls and "
      "girders in bands from the left end towards the right end, the left crawler crane lowers pallets of coating "
      "drums from the flatbed truck onto the walkway; the crane carries a visible load. " + CREW),
 tex=T_GALV,
 phys=("The pallet hangs from the crane hook on four slings. The trough rests on its bearings on the piers, and the "
       "walkway rests on its brackets. The crawler cranes stand on their tracks on the gravel."),
 mf=("A crew on the walkway sprays the charcoal coating from the drums onto the outer faces of the walls and the "
     "girders from the left end to the right end, and the left crawler crane lowers more drums from the flatbed "
     "truck onto the walkway."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Band by band from the left the light "
       "grey primer on the outside of the bridge turns a deep charcoal grey, the walls and the girders below them, "
       "until the whole bridge stands dark against the green valley with its pale blue inside and its bright "
       "railing line. The emptied truck drives off, empty trucks arrive on both pads, and at the end both cranes lift "
       "a bundle of empty pallets from the stacks. The red boat lies still "
       "in the basin. The shadows of the piers swing slowly to the right and lengthen as the sun sinks behind the "
       "camera on the left, and clouds streak across the sky."))

# ---------- S12 ----------
scene(n=12, fiil="TOPLAR", eleman="paletler + kalaslar kamyonlara · iki vinç servis yollarından ÇIKAR · saha boşalır", rejim="A", t0="15:50", t1="16:00",
 g="G12",
 stage=(T_CHAR + ". " + U(PIERS) + ", " + GATES_SHUT + ". " + U(HOOK(CRANE_L, "a bundle of empty pallets")) + "; "
        + HOOK(CRANE_R, "a bundle of empty pallets") + ". An empty flatbed truck stands on each work pad beside "
        "stacks of empty pallets and spare slings. " + U(BOAT_WAIT) + "."),
 moment="Ten to four in the afternoon, early autumn: the bridge is finished and dry, and the site is being cleared.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("15:50", "late", "autumn"),
 tr=TR_A,
 act=("Both crawler cranes lift the last bundles of empty pallets from the work pads onto the flatbed trucks, a crew "
      "rakes the gravel of the pads, and then the cranes lower their booms and drive off along the service roads "
      "behind the trucks; the cranes carry a visible load. " + CREW),
 tex=T_PAINT,
 phys=("The bundles hang from the crane hooks on four slings each. The trough rests on its bearings on the piers "
       "and the abutments, and the railing posts are bolted to the walkway. The crawler cranes stand on their "
       "tracks on the gravel."),
 mf=("The two crawler cranes lift the last empty pallets from the work pads onto the flatbed trucks, lower their "
     "booms and drive from the pads along the service roads out of the frame, and the trucks follow."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the last "
       "bundles are already swinging onto the trucks: the trucks drive off along the service roads, the two cranes "
       "lower their booms and crawl away after them out of the frame, and the crew rakes the empty pads smooth. "
       "For the first time the finished dry bridge stands alone over the valley, charcoal outside and pale blue "
       "inside, without a machine beside it. The red boat lies still in the basin. Long shadows fall to the right, "
       "and a few clouds drift slowly from the left."))

# ---------- S13 ----------
scene(n=13, fiil="AKITIR", eleman="⭐ ilk su: dolum borusu açılır → sığ su soldan sol ayağa kadar (duvarın onda biri)", rejim="A", t0="16:00", t1="16:10",
 g="G13",
 stage=(T_CHAR + ", its inside dry from end to end. " + U(PIERS) + ", " + GATES_SHUT + ". The work pads lie "
        "raked and empty, and a small service vehicle stands on the left pad. Two people stand at the valve wheel "
        "of the filling pipe on the left gate frame, and two more wait on the walkway steps. " + U(BOAT_WAIT) + "."),
 moment="Four in the afternoon on filling day, autumn: the bridge is finished, dry and empty, and the valve is about to turn.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("16:00", "late", "autumn"),
 tr=TR_A,
 act=("A crew on the left gate frame turns the valve wheel of the filling pipe, a crew of two sets a crate of "
      "tools on the walkway steps, and the small service vehicle drives along the left service road. " + CREW),
 tex=T_DONE,
 phys=("The filling pipe is bolted to the left gate frame, and the gates sit closed in their frames. The trough "
       "rests on its bearings on the piers, and the walkway rests on its brackets. The boat sits moored in the "
       "basin."),
 mf=("Clear water runs from the filling pipe at the left gate onto the dry pale blue floor of the trough and spreads "
     "as one shallow sheet from the left end towards the left pier."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the valve "
       "wheel is turning: clear water runs from the mouth of the filling pipe onto the dry pale blue floor and "
       "spreads to the right as one shallow sheet, its leading edge moving steadily, the first soft sheen of sky "
       "sliding over it, until shallow water about a tenth of the wall height deep covers the floor from the left "
       "gate to about the left pier; beyond its edge the lining stays dry and matte. The crew carries crates of "
       "tools from the service vehicle to the walkway steps. The red boat lies still in the basin, the bank canals "
       "calm. Long shadows fall to the right, and a few clouds drift slowly from the left."))

# ---------- S14 ----------
scene(n=14, fiil="İLERLETİR", eleman="su cephesi sol ayaktan → sağ kapağa (sığ, duvarın onda biri) · bütün taban ıslak", rejim="A", t0="16:10", t1="16:20",
 g="G14",
 stage=(T_CHAR + "; shallow clear water about a tenth of the wall height deep covers its floor from the left gate to "
        "about the left pier, and beyond that the lining is still dry and matte. " + U(PIERS) + ", " + GATES_SHUT
        + ". Water runs from the filling pipe on the left gate frame into the trough. Two people stand on the "
        "walkway near the left pier, and the small service vehicle stands on the left pad. " + U(BOAT_WAIT) + "."),
 moment="Ten past four in the afternoon on filling day: the first water is in the trough, and its edge is moving right.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("16:10", "late", "autumn"),
 tr=TR_A,
 act=("The filling pipe fills the trough from its left end, the shallow sheet of water runs on to the right along "
      "the floor, a crew of two walks along the walkway beside its leading edge, and the small service vehicle "
      "drives along the right service road. " + CREW),
 tex=T_SHEET,
 phys=("The filling pipe is bolted to the left gate frame, and the gates sit closed in their frames. The trough "
       "rests on its bearings on the piers, and the shallow water lies on its floor between the walls. The boat "
       "sits moored in the basin."),
 mf=("The shallow sheet of water flows on from the left pier along the trough floor to the right gate, its leading "
     "edge moving steadily to the right."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The leading edge of the shallow "
       "water moves steadily to the right along the pale blue floor, past the left pier, across the whole centre "
       "span high above the river and over the right pier, until it reaches the closed right gate; the depth stays "
       "about a tenth of the wall height and nothing runs over the walls. The dry matte band ahead of it shrinks "
       "and is gone, and the soft sheen of sky now lies along the whole trough. The crew carries crates from the "
       "service vehicle to the right steps. The red boat lies still in the basin. Long shadows fall to the right, "
       "and a few clouds drift slowly from the left."))

# ---------- S15 ----------
scene(n=15, fiil="DOLDURUR", eleman="sığ su → duvarın dörtte üçü (kıyı kanallarıyla aynı seviye) · kapaklar KAPALI", rejim="A", t0="16:20", t1="16:30",
 g="G15",
 stage=(T_CHAR + "; shallow clear water about a tenth of the wall height deep covers its floor from the left gate to "
        "the right gate. " + U(PIERS) + ", " + GATES_SHUT + ". Water runs from the filling pipe on the left gate "
        "frame into the trough. Two people stand on the walkway near the right pier, and the small service vehicle "
        "stands on the right pad. " + U(BOAT_WAIT) + "."),
 moment="Twenty past four in the afternoon on filling day: the whole trough holds shallow water, and the level is rising.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("16:20", "late", "autumn"),
 tr=TR_A,
 act=("The filling pipe fills the trough from its left end, the water level rises evenly along the whole length "
      "between the walls, a crew of two on the walkway checks the water line against the gate frames, and the "
      "small service vehicle drives back along the right service road. " + CREW),
 tex=T_FULL,
 phys=("The filling pipe is bolted to the left gate frame, and the gates sit closed in their frames. The trough "
       "rests on its bearings on the piers and holds the water between its walls. The boat sits moored in the "
       "basin."),
 mf=("Water from the filling pipe at the left gate raises the level in the trough from a shallow sheet to three "
     "quarters of the wall height, level with the water in the canal arms beyond both gates."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. The water in the trough rises "
       "evenly and calmly along its whole length, never dropping, until it stands at three quarters of the wall "
       "height, level with the water of the canal arms behind both closed gates; a narrow dry band of pale blue "
       "lining stays above the water line, and nothing runs over the walls. Then the valve wheel turns shut and "
       "the pipe stops. The calm water takes the colour of the pale blue lining with a sheen of sky on top. The "
       "crew carries two crates from the service vehicle onto the walkway. The red boat lies still in the basin. "
       "Long shadows fall to the right, and a few clouds drift slowly from the left."))

# ---------- S16 ----------
scene(n=16, fiil="AÇAR", eleman="iki uç kapak kızaklarında YUKARI (%100) · seviyeler eşit · geçiş açık", rejim="A", t0="16:30", t1="16:40",
 g="G16",
 stage=(T_CHAR + "; calm clear water stands in it at three quarters of the wall height, level with the canal arms "
        "beyond both gates. " + U(PIERS) + ", " + GATES_SHUT + ". Two people stand on the walkway at each gate "
        "frame, and the small service vehicle stands on the right pad. " + U(BOAT_WAIT) + ", one person at its "
        "stern."),
 moment="Half past four in the afternoon on filling day: the trough is full and level, and both gates are still shut.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("16:30", "golden", "autumn"),
 tr=TR_A,
 act=("A crew at each gate frame lifts the steel gate slowly up its runners on its winch, the water stays calm and level, a "
      "crew of two carries crates from the service vehicle onto the walkway, and the small service vehicle drives "
      "off along the right service road. " + CREW),
 tex=T_FULL,
 phys=("The gates hang in their frames on steel winch cables as they rise, and the frames are bolted to the "
       "abutments. The trough rests on its bearings on the piers. The boat sits moored in the basin."),
 mf=("The two steel gates rise from their sills up into their frames at the left and right ends, opening the trough "
     "to the canal arms on both banks; the water stays calm and level."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. Both steel gates rise slowly and "
       "evenly in their frames, at the same pace, until they stand high above the water and the trough lies open "
       "to the canal arm on each bank; the water stays calm, flat and level, with no rush and no step at the open "
       "gates. The crew carries two crates from the service vehicle onto the walkway, and the vehicle drives off "
       "along the right service road. At the end the person on the red boat casts off the mooring line. Long "
       "shadows fall to the right, and a few clouds drift slowly from the left."))

# ---------- S17 ----------
scene(n=17, fiil="GİRER", eleman="⭐ aynı kırmızı tekne havuzdan → açık sol kapaktan → köprüye, burnu sol ayağa yakın", rejim="Y", t0="16:40", t1="16:41",
 g="G17",
 stage=(T_CHAR + "; calm clear water stands in it at three quarters of the wall height. " + U(PIERS) + ", "
        + GATES_UP + ". One small red canal boat with a cream cabin lies just off the near bank of the left basin, "
        "its mooring line cast off, its hull low in the still water, a helmsman at its stern. Two people stand on "
        "the walkway near the left gate, and the small service vehicle stands on the left pad."),
 moment="Twenty to five in the afternoon, golden hour: the way is open, and the boat is about to move.",
 comp=C_LINE + " " + C_BOAT + " " + C_RIVER,
 light=LIGHT("16:40", "golden", "autumn"),
 tr=TR_Y,
 act=("The helmsman steers the red boat out of the basin and through the open left gate onto the bridge, a crew of "
      "two pulls the mooring line aboard and walks along the walkway beside the boat, and the small service vehicle "
      "drives along the right service road. " + CREW_Y),
 tex=T_FULL,
 phys=("The boat sits on the water in the basin, its weight carried by the water. The trough rests on its bearings "
       "on the piers, and the walkway is bolted to its brackets. The gates are clamped high in their frames."),
 mf=("The red canal boat glides from its mooring in the left basin through the open left gate onto the bridge, "
     "along the middle of the trough, until its bow is near the left pier."),
 body=("About one minute passes. Everything in this shot is time-lapsed at the same rate, gently. The same red boat "
       "with the cream cabin moves out of the basin, straight along the middle of the canal, through the open left "
       "gate and onto the bridge, gliding at a slow even pace without turning; a small V-shaped wake spreads "
       "behind it in two thin lines and breaks the sheen of sky on the water. By the end its bow is near the left "
       "pier, the whole boat inside the trough and in view. The crew of two walks along the walkway beside it, and "
       "a crew lifts a crate from the service vehicle onto the left steps. The river runs far below. Long golden "
       "shadows fall to the right, and a few clouds drift slowly from the left."))

# ---------- S18 ----------
scene(n=18, fiil="GEÇER", eleman="⭐ DORUK: tekne birinci açıklıktan → merkez açıklığın ortasına · altta nehir", rejim="Y", t0="16:41", t1="16:42",
 g="G18",
 stage=(T_CHAR + "; calm clear water stands in it at three quarters of the wall height. " + U(PIERS) + ", "
        + GATES_UP + ". One small red canal boat with a cream cabin moves along the middle of the trough, its hull "
        "low in the water, its bow near the left pier, a helmsman at its stern and a thin wake behind it. Two people walk on the walkway beside "
        "it, and the small service vehicle stands on the left pad."),
 moment="Nineteen minutes to five in the afternoon, golden hour: the boat is on the bridge, high above the river.",
 comp=(C_LINE + " " + C_RIVER + f" The red boat lies in the trough from about {P(-42, -1, 36.5)[0]} to "
       f"{P(-24, -1, 36.5)[0]} pixels from the left, its bow near the left pier."),
 light=LIGHT("16:41", "golden", "autumn"),
 tr=TR_Y,
 act=("The helmsman swings the tiller gently and keeps the red boat in the middle of the trough over the centre span, a crew of two walks "
      "along the walkway beside it, and the small service vehicle drives along the left service road. " + CREW_Y),
 tex=T_FULL,
 phys=("The boat sits on the water in the trough, its weight carried by the water. The trough rests on its bearings "
       "on the piers, and the walkway rests on its brackets. The gates sit raised in their frames."),
 mf=("The red boat glides on from the first span over the left pier to the middle of the centre span, high above "
     "the river."),
 body=("About one minute passes. Everything in this shot is time-lapsed at the same rate, gently. The red boat "
       "glides on at the same slow even pace along the middle of the trough, straight, without turning, over the "
       "left pier and out onto the centre span, until it is in the middle of it, high above the river; far below "
       "it the river runs down the valley floor in the opposite direction, both waters in the same frame. Its thin "
       "wake spreads behind it and fades. The crew of two walks along the walkway beside it, and a crew carries a "
       "crate from the service vehicle to the left steps. Long golden shadows fall to the right, and a few clouds "
       "drift slowly from the left."))

# ---------- S19 ----------
scene(n=19, fiil="VARIR", eleman="tekne merkezden → sağ kapağa, yavaşlar, burnu kapak çerçevesinde durur (0–4 sn) · TUTUŞ (4–8 sn)", rejim="Y", t0="16:42", t1="16:43",
 g="G19",
 stage=(T_CHAR + "; calm clear water stands in it at three quarters of the wall height. " + U(PIERS) + ", "
        + GATES_UP + ". One small red canal boat with a cream cabin moves along the middle of the trough over the "
        "centre span, its hull low in the water, high above the river, a helmsman at its stern and a thin wake behind it. Two people walk on the "
        "walkway beside it, and the small service vehicle stands on the left pad."),
 moment="Eighteen minutes to five in the afternoon, golden hour: the boat is crossing the middle of the valley.",
 comp=(C_LINE + " " + C_RIVER + f" The red boat lies in the trough from about {P(-4, -1, 36.5)[0]} to "
       f"{P(14, -1, 36.5)[0]} pixels from the left, over the centre span."),
 light=LIGHT("16:42", "golden", "autumn"),
 tr=TR_Y,
 act=("The helmsman swings the tiller gently, brings the red boat along the trough to the open right gate and lets it come to rest, a crew of "
      "two walks along the walkway towards the right steps, and the small service vehicle drives off along the left "
      "service road. " + CREW_Y),
 tex=T_FULL,
 phys=("The boat sits on the water in the trough, its weight carried by the water. The trough rests on its bearings "
       "on the piers, and the walkway rests on its brackets. The gates sit raised in their frames."),
 mf=("The red boat glides on from the centre span over the right pier to the open right gate, slows and comes to "
     "rest with its bow at the gate frame."),
 body=("About one minute passes. Everything in this shot is time-lapsed at the same rate, gently. In the first four "
       "seconds the red boat glides on along the middle of the trough over the right pier, slows smoothly and comes "
       "to rest with its bow at the open right gate, the whole boat still on the bridge and in view; the two people "
       "on the walkway stop beside it. From about four to eight seconds nothing else changes: the boat lies still "
       "on the calm water, its last wake fading, the bridge, the open gates and the canal arms unchanged, the river "
       "running far below. Long golden shadows fall to the right, and a few clouds drift slowly from the left."))

USTA = dict(g="G20", t="16:43",
 stage=(T_CHAR + "; calm clear water stands in it at three quarters of the wall height, level with the canal arms. "
        + U(PIERS) + ", " + GATES_UP + ". The same small red canal boat with a cream cabin lies still on the water at "
        "the right end of the trough, its bow at the open right gate, its hull low in the water, a helmsman at its "
        "stern; two people stand on the walkway beside it, small figures, no readable faces. The work pads lie raked "
        "and empty."),
 moment="Seventeen minutes to five in the afternoon, golden hour, autumn: the boat has crossed the valley on the canal bridge.",
 comp=(C_LINE + " " + C_RIVER + f" The red boat lies at the right end of the trough from about {P(30, -1, 36.5)[0]} "
       f"to {P(48, -1, 36.5)[0]} pixels from the left, at about {pct(P(39, -1, 36.5)[1])} percent of frame height."),
 light=LIGHT("16:43", "golden", "autumn"),
 tr=TR_Y,
 act=("The red boat lies still at the open right gate; the two people stand still on the walkway, and the river "
      "runs far below. " + CREW_Y),
 tex=T_FULL,
 phys=("The boat sits on the water at the right end of the trough, its weight carried by the water. The trough rests "
       "on its bearings on the piers, and the railing posts are bolted to the walkway. The gates sit raised in "
       "their frames."))

# ── yazıcılar ───────────────────────────────────────────────────────────────
def lens(iso): return f"Lens: 24 mm spherical, f/8, ISO {iso}."

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

RJ = {"A": "A (10 dk)", "B": "B (2 sa)", "Y": "Y (≈1 dk · YENİ — ölçülmedi)"}
def blok(d):
    n = d["n"]; bas, son = n * 8, (n + 1) * 8
    out = [f"## 🎬 SAHNE {n} — {d['fiil']}", "",
           "```",
           f"SÜRE: 8,0 s ({bas},0–{son},0)  ·  ELEMAN + ARA HÂL: {d['eleman']}  ·  REJİM: {RJ[d['rejim']]}  ·  SAAT: {d['t0']}→{d['t1']}  ·  İSTASYON: MAIN",
           "```", ""]
    if n in (0, 1, 2):
        out += ["> ⚠️ **Uzun sert yük** [DERS 57 · hikâye SAPMA ①]: parça tek parça, dört sapanla, yavaş ve düz; S0'da ilk",
                "> karede zaten asılı · S1'de kısa yol · S2'de yalnız DİMDİK yukarı. Kopya yazılmaz (\"exactly two piers\").", ""]
    if n in (13, 14, 15):
        out += ["> 💧 **Su kotu** [SU_VE_YANSIMA §8]: kaynak dolum borusu (SITE, G0'dan beri) · yön soldan sağa · kot duvarın",
                "> kesriyle (onda bir → dörtte üç) · su gelmeden önce oluk KURU ve mat [DERS 54] · taşma yok.", ""]
    if d["rejim"] == "Y":
        out += ["> 🛶 **Rejim Y (≈1 dk · ≈8×)** — tekne klip başına ≈40 m ilerler (2,4 km/sa) [hikâye SAPMA ③ · SU_VE_YANSIMA §7].",
                "> Kapı bu rejimi tanımaz (\"one minute passes\" sözlükte yok) → beklenen FIX, PLAN'da beyanlı.", ""]
    out += [f"### 📸 GÖRSEL PROMPT ({d['g']})", "", "```", gorsel_main(d, HEAD_MAIN.format(n=n)), "```", ""]
    out += [f"### 🎥 I2V PROMPT ({d['g']} → G{n+1})", "", "```", i2v(d), "```", "", "---", ""]
    return "\n".join(out)

def usta_blok():
    return "\n".join([
        "## 🌟 USTA KARE — G20 (SAHNE DEĞİLDİR · son klibin hedefi · kapak kaynağı)", "",
        "> Üretim sırasının İLK karesi [§8]: G20 önce üretilir ve ikna edici değilse DURULUR; sonra",
        "> image-to-image geriye G19 → G18 → … → G0. Kapı: kırmızı tekne sağ uçta, burnu açık sağ kapakta, tamamı",
        "> kadrajda · iki kapak yukarıda · oluk duvarın dörtte üçüne dolu, kıyı kanallarıyla aynı seviye · nehir",
        "> çok aşağıda, ayrı · kanıt nesnesi çam · vinç, kamyon, palet YOK (SÖKÜM satırı) · altın saat, güneş ≈6°.",
        "> Kapak (`THE_SKY_CANAL_KAPAK.md`) bu promptun kopyası + gök bandı satırıdır [MUZIK_VE_KAPAK §2.2].", "",
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
> ⛔ Vinç kancası [DERS 8]: iki vincin kancası her karede ya YÜKLÜ ("with a … on the hook" / dört sapan bağlı)
> ya da bom ucu KADRAJ DIŞINDA ("its tip and line above the top edge of the frame"); boş kanca hiçbir promptta yazılmaz.
>
> ⛔ Kelime kilitleri: "crane" yalnız G0–G12 ve S0–S12 I2V'lerinde; oluğun içinde su yalnız S13 I2V'sinden ve
> G14'ten sonra (öncesi "dry"); "blue" (iç kaplama) yalnız S8 I2V'sinden ve G9'dan sonra; "charcoal" yalnız S11
> I2V'sinden ve G12'den sonra; kapaklar "raised" yalnız S16 I2V'sinden ve G17'den sonra; tekne yalnız S17'den
> sonra hareket eder; YASAK KELİME (PLAN künyesi) hiçbir promptta yok — negatifte bile.

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
> 💧 **S13 + S14 + S15 TEK DOLUMDUR**: kaynak aynı boru, yön soldan sağa, kot yalnız artar (onda bir → dörtte üç);
> her kesme öncekinin su cephesini ve seviyesini devralır, aynı bölüm iki kez ıslanmaz.
>
> 🛶 **S17 + S18 + S19 TEK GEÇİŞTİR** (rejim Y, ≈1 dk/klip): aynı tekne, aynı hız, aynı eksen; dönüş, ikinci
> tekne, yakın plan YOK. Tekne her kesmede bir öncekinin bıraktığı yerde.
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
        return f"{r:+d}°"
    for d in S + [USTA]:
        t = d["t"] if "t" in d else d["t0"]
        az, e = sun(hm(t))
        print(d["g"], t, f"{az}°", f"{e:.1f}°".replace(".", ","), golge(t), f"bağıl güneş {((az - BEARING + 180) % 360) - 180:+d}°")
    sys.exit(0)

if "--kadraj" in sys.argv:
    print("ufuk (üstten)", UFUK, "· %", pct(UFUK))
    rows = [("sol mesnet duvar tepesi (yakın)", -50, -4, 37), ("sol mesnet dibi", -50, -4, 30), ("sol kapak çerçevesi tepesi", -50, 0, 44),
            ("sol ayak tepesi", -20, -5, 31.5), ("sol ayak dibi", -20, -5, 8), ("sağ ayak tepesi", 20, -5, 31.5), ("sağ ayak dibi", 20, -5, 8),
            ("sağ mesnet duvar tepesi (yakın)", 50, -4, 37), ("sağ kapak çerçevesi tepesi", 50, 0, 44),
            ("oluk merkez: yakın duvar tepesi", 0, -4, 37), ("oluk merkez: uzak duvar tepesi", 0, 4, 37), ("oluk merkez: uzak taban", 0, 4, 35),
            ("oluk merkez: uzak su çizgisi +36,5", 0, 4, 36.5), ("oluk merkez: kiriş altı", 0, -4, 31.5), ("bakım yolu korkuluğu (merkez)", 0, -6, 37.9),
            ("tekne kıç (havuz)", -82, -3, 36.5), ("tekne burun (havuz)", -64, -3, 36.5), ("tekne kabin tepesi (havuz)", -73, -3, 38.8),
            ("havuz sonu", -90, 0, 36.5), ("sağ kanal s70", 70, 0, 36.5), ("sol vinç tabanı", -62, 18, 37.2), ("sağ vinç tabanı", 64, -22, 37.2),
            ("sağ parça istifi a", 55, -14, 38.5), ("sağ parça istifi b", 85, -14, 38.5),
            ("merkez parça kalasta a", -20, 0, 4), ("merkez parça kalasta b", 20, 0, 7.5),
            ("tekne G18 kıç", -42, -1, 36.5), ("tekne G18 burun", -24, -1, 36.5), ("tekne G19 kıç", -4, -1, 36.5), ("tekne G19 burun", 14, -1, 36.5),
            ("tekne G20 kıç", 30, -1, 36.5), ("tekne G20 burun", 48, -1, 36.5), ("tekne G20 kabin tepesi", 39, -1, 38.8)]
    for ad, s, off, z in rows:
        x, y = P(s, off, z); print(f"{ad:36s} x {x:5d} · üstten {y:4d} · %{pct(y)}")
    for ad, Q in [("nehir (köprü altı)", (5, 135, 0)), ("nehir (yukarı, 300 m)", (5, 300, 0)), ("çam sol", (43, 98, 40)), ("çam sağ", (49, 98, 40)),
                  ("çam dibi", (46, 98, 30)), ("çam tepesi", (46, 98, 48))]:
        x, y = proj(Q); print(f"{ad:36s} x {x:5d} · üstten {y:4d} · %{pct(y)}")
    d = math.hypot(XC, YC); dep = math.degrees(math.atan((CAM_H - 35) / d))
    cosn = abs((XC * NX[0] + YC * NX[1]) / d); gizli = 2.0 / math.tan(math.radians(dep)) * cosn
    print(f"oluk tabanına bakış {dep:.1f}° · yakın duvarın gizlediği taban {gizli:.1f} m / 8 → görünen {8 - gizli:.1f} m")
    sys.exit(0)

b1 = H1 + "\n" + "\n".join(blok(d) for d in S if d["n"] <= B1_SON)
b2 = H2 + "\n" + "\n".join(blok(d) for d in S if d["n"] > B1_SON) + "\n" + usta_blok()
open(os.path.join(OUT, f"{FILM}_BOLUM_1.md"), "w").write(b1)
open(os.path.join(OUT, f"{FILM}_BOLUM_2.md"), "w").write(b2)
print("yazıldı", len(b1), len(b2))
