# THE LAST CARRIAGE — bölüm dosyası üretici (ortak bloklar tek kaynaktan, DERS 20)
# KULLANIM (depo kökünden):
#   python3 yatay_2_dk_filmler/THE_LAST_CARRIAGE/00_ANALIZ/05_SAHNE_CALISMALARI/bolum_uretici.py yatay_2_dk_filmler/THE_LAST_CARRIAGE
#   → THE_LAST_CARRIAGE_BOLUM_1.md + _BOLUM_2.md yeniden yazılır; ardından prompt_kontrol.py klasör modunda koşulur.
#   --tablo  → PLAN kare tablosu satırlarını basar (saat · azimut · yükseklik · bağıl güneş)
#   --kadraj → PLAN DEĞİŞMEZLER px satırlarını basar (iğne deliği izdüşümü, 28 mm, tilt 14°, iki istasyon)
# ⛔ ÜRETİM BAŞLADIKTAN SONRA KOŞULMAZ: üretilmiş filmin promptu kanıttır (URETIM_GUNLUGU kuralı).
# ⛔ Bölüm dosyası elle düzeltilirse bu betik o düzeltmeyi EZER — düzeltme önce buraya yazılır.
# Kalıp: İKİ istasyon — MAIN (19 klip) + CARRIAGE (yalnız S14, iç mekân, S13 ile AYNI on dakika).
# Zincir: S13 I2V G13 → G15 (ana) · S14 G14 → G14′ (iç) · S15 G15'ten başlar [ISTASYON_VE_IC_MEKAN §2].
# Bölüm sınırı G10. Sahibin S01–S20'si = depo S0–S19 (sahibin S15'i = S14 iç klip).
# Rejim: A (10 dk) · B (2 sa: S3 pas · S4 boya · S10 ahşap döşeme) · G (8 sn gerçek zaman: S18 · S19 — final).
import math, os, sys

FILM = "THE_LAST_CARRIAGE"
OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
N_SAHNE = 20
B1_SON = 9          # BOLUM_1 = S0–S9 · BOLUM_2 = S10–S19 + USTA (sınır G10)
IC = 14             # iç istasyon sahnesi (paralel zaman)
BEARING = 337       # ana kamera bakışı (KKB) — kanyonun yukarısına, vagonun uzun yüzüne üç çeyrek

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

# ── kadraj (iğne deliği · 28 mm · 36 × 20,25 mm · 1920 × 1080 → f = 1493 px) ─
# Dünya: O = vagon tabanının merkezi, çelik tabliyenin üst yüzü (z 0). +x doğu (vagon ekseni), +y kuzey, z yukarı (m).
# Vagon x ±12,2 · y ±1,45 · tavan tepesi +4,2 (ortada +4,6) · iç döşeme +1,0. Boşluk (iki kaya rafı arası) x ±9, raflar −1,8.
# Tabliye: iki derin kiriş x ±16, yakın kiriş y −3; teras y −3 … −9, x ±7,5; cam orta bölüm x ±2,4, y −4 … −9.
# MAIN: (12, −30, +11), yaw −23° (bakış 337°), tilt 14° aşağı. CARRIAGE: (−10,6, 0,3, +3,1), bakış 90°, tilt 14° aşağı.
# ⚠️ İki kamerada tilt AYNI (14°) → uzak sırt çizgisi iki kamerada da üstten 168 px (%84) — İSTASYON §0 ①'in
#    "tilt 0 · ufuk %50" hükmünden SAPMA, gerekçe PLAN §İKİNCİ İSTASYON BEYANI (cam tabanı yukarıdan okumak).
F_PX = 28 / 36 * 1920
TILT = 14.0
def _mk(cx, cy, cz, yawd):
    yaw, t = math.radians(yawd), math.radians(TILT)
    def p(P):
        dx, dy, dz = P[0] - cx, P[1] - cy, P[2] - cz
        fwd = dx * math.sin(yaw) + dy * math.cos(yaw); right = dx * math.cos(yaw) - dy * math.sin(yaw)
        Zc = fwd * math.cos(t) - dz * math.sin(t); Yc = fwd * math.sin(t) + dz * math.cos(t)
        return round(960 + F_PX * right / Zc), round(540 - F_PX * Yc / Zc)
    return p
proj = _mk(12, -30, 11, -23)
proj_ic = _mk(-10.6, 0.3, 3.1, 90)
def pct(y): return round(100 * (1 - y / 1080))
UFUK = round(540 - F_PX * math.tan(math.radians(TILT)))

# ── ortak bloklar ───────────────────────────────────────────────────────────
HEAD_MAIN = ("Photorealistic documentary site photograph — Scene {n} of 20. Horizontal 16:9 time-lapse of an old railway "
             "passenger carriage over a narrow canyon made into a cliff-edge restaurant, from a fixed 28 mm site camera.")
HEAD_INT = ("Photorealistic documentary interior photograph — Scene 14 of 20. Horizontal 16:9 time-lapse inside an old "
            "railway passenger carriage over a narrow canyon being made into a restaurant; a photograph from a fixed 28 mm "
            "camera inside the carriage.")
HEAD_INT_SON = ("Photorealistic documentary interior photograph — the last frame of Scene 14 of 20. Horizontal 16:9 "
                "time-lapse inside an old railway passenger carriage over a narrow canyon being made into a restaurant; a "
                "photograph from a fixed 28 mm camera inside the carriage.")
HEAD_USTA = ("Photorealistic documentary site photograph — master frame G20, the target frame of the last shot "
             "(Scene 19 of 20). Horizontal 16:9 time-lapse of an old railway passenger carriage over a narrow canyon, "
             "now a cliff-edge restaurant on its opening evening, from a fixed 28 mm site camera.")
CAM_MAIN = ("Camera: MAIN STATION — fixed tripod bolted to a rock spur on the right rim of the canyon, downstream of the "
            "carriage, lens 11 metres above the steel support deck, 32 metres from the centre of the carriage, bearing 337 "
            "degrees, tilt 14 degrees down, zero roll. The camera never moves.")
CAM_INT = ("Camera: CARRIAGE STATION — fixed clamp mount bolted high on the left end wall inside the carriage, lens 3.1 "
           "metres above the steel support deck, 21 metres from the right end wall, bearing 90 degrees, tilt 14 degrees "
           "down, zero roll. The camera never moves.")
STRUCT = ("STRUCTURE: When finished this will be a cliff-edge restaurant made from one old railway passenger carriage, "
          "24 metres long, with a rounded roof, eight broad windows along each side and a vestibule at each end, on a "
          "dark steel deck over a narrow deep canyon, with a gangway at each end and a timber terrace with a "
          "glass-floored middle in front.")
ROCK = "one large pale rock split from top to bottom by a dark crack"
RIDGE = ("a long level line of distant blue ridges closes the view, at about sixteen percent of frame height from the "
         "top")
SITE_MAIN = ("SITE / BACKGROUND: A narrow, deep canyon of grey-brown rock. A dark steel support deck of two deep girders spans the gap between two broad rock ledges, "
             "bearing on steel pads on both, with a narrow walkway and low handrail along each side and a row of short "
             "bracket stubs along its near girder; below it the canyon walls drop away into deep shadow. On the left ledge a gravel service road comes in from the left edge to a level gravel yard, and "
             "near its rim stands one tall forked pine with two trunks. Behind the right end of the deck, on the right "
             "ledge, stands " + ROCK + ". Beyond, the canyon bends away to the left between forested slopes, and far "
             "beyond it, " + RIDGE + ".")
SITE_INT = ("SITE / BACKGROUND: The saloon of the carriage, seen from high on its left end wall looking down the centre "
            "aisle to the right end wall, which holds one glazed door in its middle; eight broad windows run down each "
            "side under a rounded ceiling. Through the right-hand windows lie the near walkway and the open air over the "
            "canyon; through the far left-hand windows, behind the right end of the deck, stands " + ROCK + ". Far "
            "away beyond the canyon, " + RIDGE + ".")
NEG_MAIN = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The canyon, the ledges, the steel "
            "deck, the forked pine, the split pale rock and the ridges never change shape, position, size or spacing. The canyon holds exactly one carriage, with exactly "
            "eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat "
            "on the steel deck. Nothing already built is removed or resized; no opacity fades. No readable text, "
            "letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, "
            "labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation "
            "look, no CGI aesthetic.")
NEG_INT = ("NEGATIVE: Locked-off camera — it never pans, tilts, zooms or drifts. The rounded ceiling, the end walls, the "
           "glazed door, the eight windows down each side, the split pale rock through the far left-hand windows and "
           "the distant ridges never change shape, position, size or spacing. The saloon keeps exactly eight windows "
           "down each side; nothing already built is removed or resized; no opacity fades. No readable text, letters, "
           "digits, numbers or symbols anywhere in the frame, on any surface. Nothing here has been branded, labelled, "
           "numbered or annotated by anyone. No cuts, no dissolves, no fades. No architectural visualisation look, no "
           "CGI aesthetic.")
OUTPUT = "Output: 16:9, 4K, no text, no watermark."
CREW = ("Dozens of workers in orange work clothes move fast in crews, small figures with soft motion streaks, never "
        "sharp, no readable faces.")
CREW_B = "Dozens of workers in orange work clothes show only as faint soft motion streaks, never as sharp figures."
CROWD_A = ("Guests show as faint soft motion streaks while they walk and as small still silhouettes once seated, no "
           "readable faces.")
CROWD_G = "Guests and staff are small distant figures, seen from the side or from behind, no readable faces."
FILMSTOCK = "A documentary site photograph on colour negative film, true colour, fine grain."

# kadraj sayıları (betik hesaplar; PLAN DEĞİŞMEZLER bu çıktıyı yazar)
_rkL, _rkR, _rkT = proj((14, 10, -1)), proj((17.5, 10, -1)), proj((15.75, 10, 5.5))
_cL, _cR = proj((-12.2, -1.45, 4.2)), proj((12.2, -1.45, 4.2))
_cLd, _cRd = proj((-12.2, -1.45, 0)), proj((12.2, -1.45, 0))
_pine = proj((-18, -4, 0)); _pineT = proj((-18, -4, 13))
COMP_HEAD = (f"COMPOSITION: Horizontal 16:9, looking down 14 degrees, the distant ridges at about {pct(UFUK)} percent of "
             f"frame height. The split pale rock spans about {_rkR[0] - _rkL[0]} pixels of frame width, from about "
             f"{_rkL[0]} to {_rkR[0]} pixels from the left, its top at about {pct(_rkT[1])} percent, and keeps that width "
             f"and position in every frame. The carriage spans from about {_cL[0]} to {_cR[0]} pixels from the left, "
             f"its roof line falling from about {pct(_cL[1])} to {pct(_cR[1])} percent of frame "
             f"height and its underframe from {pct(_cLd[1])} to {pct(_cRd[1])} percent. The forked pine stands at about "
             f"{_pine[0]} pixels from the left. ")
_crane = proj((-24, 6, 0)); _yard = proj((-20, 2, 0))
_tFL, _tFR = proj((-7.5, -9, 0)), proj((7.5, -9, 0))
_gFL, _gFR, _gBL = proj((-2.4, -9, 0)), proj((2.4, -9, 0)), proj((-2.4, -4, 0))
C_CRANE = (f"The mobile crane stands on the gravel yard of the left ledge at about {_crane[0]} pixels from the left, its "
           f"outriggers at about {pct(_crane[1])} percent of frame height.")
C_YARD = f"The gravel yard lies at the upper left, around {_yard[0]} pixels from the left."
C_TERR = (f"The near edge of the terrace runs from about {_tFL[0]} pixels at {pct(_tFL[1])} percent of frame height "
          f"to about {_tFR[0]} pixels at {pct(_tFR[1])} percent.")
C_GLASS = f"Its glass middle lies between about {_gFL[0]} and {_gFR[0]} pixels from the left."
COMP_TAIL = "Nothing that proves progress falls into the top-right corner of the frame."
_dL, _dR = proj_ic((11, 1.35, 3.9)), proj_ic((11, -1.35, 3.9))
_dB = proj_ic((11, 0, 1.0))
COMP_INT = (f"COMPOSITION: Horizontal 16:9, the camera looking down 14 degrees, the line of distant ridges through the "
            f"windows at about {pct(UFUK)} percent of frame height. The right end wall spans about {_dR[0] - _dL[0]} pixels "
            f"of frame width at the upper centre, from about {_dL[0]} to {_dR[0]} pixels from the left, its foot at about "
            f"{pct(_dB[1])} percent of frame height, and keeps that width and position in every frame; the two rows of "
            f"windows run in perspective from the frame edges towards it, and the floor and the furniture fill the lower "
            f"two thirds. Nothing that proves progress falls into the top-right corner of the frame.")

TR_A = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all "
        "move at the same accelerated speed. Ten minutes pass across this shot: shadows barely move, clouds drift "
        "smoothly, machines move fast with light motion blur.")
TR_B = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, shadows, machines and crews all "
        "move at the same accelerated speed. Two hours pass across this shot: shadows swing slowly round, clouds "
        "streak across the sky, machines smear into heavy motion blur.")
TR_A_DUSK = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: clouds, light, vehicles and people "
             "all move at the same accelerated speed. Ten minutes pass across this shot: the sky deepens slowly, "
             "clouds drift smoothly, people move fast as soft streaks.")
TR_G = ("TIME RATE: Everything in this frame moves at natural speed: the people, the trees and the sky. Eight seconds "
        "pass across this shot: the light holds, the clouds hold still, the pine branches sway slightly in a light "
        "breeze, and people move in small natural ways.")
TR_INT = ("TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds and the light outside and "
          "the crew inside all move at the same accelerated speed. Ten minutes pass across this shot: the bands of low "
          "sunlight slide slowly across the floor, the clouds outside drift smoothly, and the crew trail light motion "
          "blur.")

I2V_HEAD = ("The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its "
            "last frame is that image, matched frame for frame — same framing, same light, same objects in the same "
            "places.")
LOCK_MAIN = ("The camera does not move at any point. The framing is identical in the first and last frame. The canyon, "
             "the two rock ledges, the steel support deck, the forked pine, the split pale rock, the service road and "
             "the distant ridges stay exactly where they are, at exactly the same size and shape, for the whole shot; "
             "the split rock occupies exactly the same width of the frame in the first and last frame. The canyon "
             "holds exactly one carriage with exactly eight broad windows along its near side. Nothing already built "
             "is removed or resized.")
LOCK_SEATED = " Once seated on the deck, the carriage never lifts, swings or shifts again."
LOCK_INT = ("This shot shows the same stage as the previous shot from the main station: the carriage stands at the same "
            "place and size, a little over half the frame width in that view, and nothing outside the carriage is built "
            "during this shot. The camera does not move at any point. The framing is identical in the first and last "
            "frame. The rounded ceiling, the end walls, the glazed door, the eight windows down each side, the split "
            "pale rock through the far left-hand windows and the distant ridges stay exactly where they are, at exactly "
            "the same size and shape, for the whole shot; the right end wall occupies exactly the same width of the "
            "frame in the first and last frame. Nothing already built is removed or resized.")
I2V_TAIL = ("Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
            "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
            "documentary time-lapse cinematography.")
I2V_TAIL_INT = I2V_TAIL.replace("fixed tripod", "fixed clamp mount")

# ── tekrarlanan durum cümleleri (aynı nesne her karede aynı kelimelerle) ─────
CRANE = "a large yellow mobile crane stands on its outriggers on the gravel yard of the left ledge"
def HOOK(x): return CRANE + f", with {x} on the hook on taut slings"
def UP(): return CRANE + ", its boom raised steeply, its tip and line above the top edge of the frame"
SEATED = "the carriage sits on the steel support deck, its steel underframe bolted flat to the deck"
RUSTY = ("weathered rust-brown from end to end with patches of faded old paint, its rounded roof rust-brown and dented, "
         "one closed vestibule at each end")
PANES_OLD = "its eight broad window openings along the near side filled with broken and clouded old panes"
OPEN8 = "its eight broad window openings along the near side stand empty, the dim stripped saloon showing through them"
BARE = ("the carriage body is bare dull grey steel from end to end, scoured clean, its rounded roof bare grey steel, one "
        "vestibule at each end")
PAINT = ("the carriage body is painted a deep emerald green from end to end with a cream band along the tops of the "
         "windows, one vestibule at each end")
ROOF = "its rounded roof clad in warm copper-coloured sheets"
GLAZED = "eight broad clear windows along its near side"
GW_L = "a short dark steel gangway with handrails links the left vestibule to the gravel yard on the left ledge"
GW_R = ("a short dark steel gangway with handrails and a few steps links the right vestibule to a footpath on the right "
        "ledge")
GW_LAMPS = "small lamps on short posts stand at both ends of each gangway"
FRAME = ("a terrace frame of dark steel, three large modules bolted to the bracket stubs along the near girder, reaches "
         "towards the camera over the canyon, an open grid with the drop visible through it")
DECKED = ("warm timber decking covers the left and right sections of the terrace and a strip along the carriage, and "
          "the rectangular middle section is a steel-framed opening, open to the drop below")
GLASSF = ("three large clear glass floor panels fill the middle section of the terrace in slim steel frames, the canyon "
          "visible far below through them, their edges and soft reflections showing the glass")
RAILS = "slim dark posts with clear glass guardrail panels enclose the open edges of the terrace"
TABLES = "two timber dining tables with chairs on each timber section, the glass middle clear"
LAMPS_OFF = "the gangway lamps, the small lights at the foot of the guardrails and the lamps inside are unlit"
LAMPS_ON = ("warm light fills the eight windows, the gangway lamps are lit and small warm lights line the foot of "
            "the guardrails")
def U(x): return x[0].upper() + x[1:]
CARR_DONE = ("the carriage sits bolted on the steel support deck, deep emerald green with a cream band along the "
             "window tops, its rounded roof clad in warm copper-coloured sheets, eight broad clear windows along its near "
             "side")
GW_BOTH = ("short dark steel gangways with handrails link its left vestibule to the gravel yard and its right vestibule, "
           "by a few steps, to a footpath on the right ledge, small lamps on short posts at their ends")
FRAME_S = ("in front, a terrace frame of dark steel bolted to the bracket stubs on the near girder reaches towards the "
           "camera over the canyon")
DECK_S = "warm timber decking on its left and right sections and along the carriage"
GLASS_S = "three large clear glass floor panels in slim steel frames in its middle, the canyon visible far below"
RAIL_S = "slim dark posts with clear glass guardrail panels round its open edges"
FIN = ("the carriage sits bolted on the steel deck, deep emerald green with a cream band along the window tops, its "
       "rounded roof clad in copper-coloured sheets, eight broad clear windows along its near side; short dark steel "
       "gangways with handrails link its left vestibule to the gravel yard and its right vestibule, by a few steps, to "
       "a footpath on the right ledge, small lamps at their ends; in front, a terrace of dark steel frames bolted to the "
       "bracket stubs reaches towards the camera over the canyon, timber-decked on its left and right sections and "
       "along the carriage, three large clear glass floor panels in its middle with the canyon far below, and slim dark "
       "posts with clear glass guardrails round its open edges")

# ── doku ────────────────────────────────────────────────────────────────────
T_RUST = ("Flaking rust streaks and blistered old paint on the carriage, orange rust stains on the steel deck, tyre ruts "
          "and puddles in the gravel yard, stacks of empty crates, a film of dust on the old panes. " + FILMSTOCK)
T_BLAST = ("Bands of bare grey steel beside flaking rust-brown, drifts of spent grit and rust flakes on tarpaulins along "
           "the walkway, a film of dust on the deck, tyre ruts in the gravel yard, stacks of filled grit bags. " + FILMSTOCK)
T_PAINT = ("Fresh satin emerald paint with a soft sheen beside bands of grey primer, paint spatter on the tarpaulins, "
           "drums stacked on pallets, tyre ruts in the gravel yard, a film of dust on the deck. " + FILMSTOCK)
T_BARE = ("Bare dull grey steel with dark seams and a few pale primer patches, drifts of spent grit on the tarpaulins, "
          "filled grit bags stacked on a pallet, tyre ruts in the gravel yard, a film of dust on the deck. " + FILMSTOCK)
T_BUILD = ("Fresh satin emerald paint with a soft sheen, copper-coloured roof sheets with bright cut edges, pallets and "
           "offcuts stacked on the gravel yard, tyre ruts in the gravel, a film of dust on the steel deck. " + FILMSTOCK)
T_TIMBER = ("Fresh pale timber decking with sawdust in the joints, offcuts and pallets stacked on the gravel yard, tyre "
            "ruts in the gravel, a film of dust on the steel, a soft sheen on the new paint. " + FILMSTOCK)
T_DONE = ("Satin emerald paint with a soft sheen, clean timber decking, raked gravel on the yard with the faint "
          "print of tyre ruts, pale patches where the stacks stood, pine needles drifted in the terrace corners. " + FILMSTOCK)
T_EVE = ("Satin emerald paint with a soft sheen, raked gravel on the yard with the faint print of tyre ruts, pine "
         "needles drifted in the terrace corners, a soft sheen on the glass floor, a film of dust on the rock. " + FILMSTOCK)
T_INT = ("Fresh warm timber floor boards with sawdust in the joints, pale panelled walls with taped seams, packing film "
         "and offcuts stacked by the glazed door, a film of dust on the new panes, bands of low sunlight across the "
         "floor. A documentary interior photograph on colour negative film, true colour, fine grain.")

# ── ışık (bakış 337° — güneş hiçbir karede kadrajda değil: sabah arkada sağda, öğle arkada, akşam solda) ──
LIGHT_DESC = {
 "morning": ("behind the camera on the right: clear morning light on the near long side of the carriage, shadows "
             "falling forward to the left, the canyon below in shade."),
 "noon": ("high behind the camera: bright light on the near long side of the carriage, short shadows falling away from "
          "the camera, the upper canyon walls lit."),
 "pm": ("behind the camera on the left: warm afternoon light on the near long side, shadows falling forward to the "
        "right, the canyon below in soft shade."),
 "golden": ("low on the left: warm golden light rakes along the near long side of the carriage from "
            "the left, long shadows to the right, the canyon below in deep shade."),
 "dusk": ("on the left: the last warm light leaves the rims and the pine tops, the canyon lies in "
          "soft even shade without shadows, and the clear sky fades from pale gold to soft blue."),
 "blue": ("on the left: deep clear blue hour, the sky still readable, the emerald body, the copper "
          "roof and the rock clearly visible; the air is clear, and the lamps are small warm points with crisp edges."),
}
def LIGHT(t, key):
    tail = " The sun stays outside the frame." if sun(hm(t))[1] > -0.5 else " The sun is below the horizon, outside the frame."
    return f"LIGHTING: {sunline(t)}, {LIGHT_DESC[key]}{tail}"

# ── sahne verisi ─────────────────────────────────────────────────────────────
S = []
def scene(**k): S.append(k)

# ---------- S0 ----------
scene(n=0, fiil="İNDİRİR", eleman="⭐ vagon tabliyenin 1 m üstünden tabliyeye (DERS 57: kaldırma karede biter, klip yalnız son metreyi gösterir) · sapanlar bağlı kalır", rejim="A", t0="09:30", t1="09:40",
 g="G0",
 stage=("the old carriage already hangs over the canyon: one old railway passenger carriage, " + RUSTY + ", " + PANES_OLD +
        ", hangs level about one metre above the steel support deck on four short taut slings from a lifting spreader "
        "bar. " + U(HOOK("a lifting spreader bar")) + ", the boom head directly above the carriage. Crews stand on both "
        "ledges and on the deck walkways holding taglines tied to the two ends of the carriage, and a flatbed truck stands "
        "on the gravel yard."),
 moment="Half past nine on a clear autumn morning: the old carriage already hangs over the canyon, a metre above its steel deck.",
 comp=("In this frame the carriage still hangs one metre higher, its underframe about 40 pixels above that line, the gap "
       "between it and the steel deck clearly open. " + C_CRANE + " " + C_YARD),
 light=LIGHT("09:30", "morning"), tr=TR_A,
 act=("The mobile crane lowers the carriage the last metre onto the steel deck, the crews on both ledges steady its ends "
      "with taglines, a second crew bolts its underframe to the deck, and a flatbed truck brings crates of anchor bolts "
      "along the service road; the crane carries a visible load. " + CREW),
 tex=T_RUST,
 phys=("The carriage hangs from the spreader bar on four taut slings, and the spreader bar hangs from the crane hook. "
       "The crane stands on its outriggers on pads on the gravel, the steel deck bears on steel pads on both ledges, and "
       "the truck stands on its tyres on the gravel yard."),
 mf=("The mobile crane lowers the carriage from its hanging position one metre above the deck onto the steel support "
     "deck, and the crew bolts its underframe down."),
 body=("Ten minutes pass in the clear morning light. Everything in this shot is time-lapsed at the same rate. From the "
       "first frame the carriage is already sinking slowly and level, never swinging, as the crane pays out its line: the "
       "crews on both ledges hold it steady with taglines, its ends pass over the steel pads on the two ledges, and it "
       "settles flat onto the steel deck across the canyon. A crew moves along the walkways and bolts the underframe to "
       "the deck; the slings stay fastened and go slack only after the bolts are in. A flatbed truck brings crates of "
       "anchor bolts along the service road and the crew carries them to the deck. Thin high clouds drift slowly from "
       "the right, and long shadows fall forward to the left."),
 seated=False)

# ---------- S1 ----------
scene(n=1, fiil="ÇÖZER", eleman="sapanlar vagondan çözülür · çapraz kiriş vinçle sola, avluya iner · bom dik kalkar · avluya boş kasalar", rejim="A", t0="09:40", t1="09:50",
 g="G1",
 stage=(SEATED + ", " + RUSTY + ", " + PANES_OLD + ". " + U(HOOK("a lifting spreader bar")) + ", its four slings still "
        "fastened to the corners of the carriage roof. Riggers stand on the carriage roof at the sling shackles, and a "
        "flatbed truck stacked with empty timber crates stands on the gravel yard beside a small yellow telehandler."),
 moment="Twenty to ten in the morning: the carriage has landed on its deck, and the slings are about to come off.",
 comp=C_CRANE + " " + C_YARD,
 light=LIGHT("09:40", "morning"), tr=TR_A,
 act=("Riggers on the carriage roof unshackle the four slings, the mobile crane lifts the spreader bar off the roof and "
      "swings it to the gravel yard, the telehandler unloads the empty crates from the flatbed truck into a stack, and a "
      "crew lays timber walk boards along the deck walkways; the crane carries a visible load. " + CREW),
 tex=T_RUST,
 phys=("The spreader bar hangs from the crane hook on its taut slings. The carriage rests on the steel deck, its "
       "underframe bolted down; the crane stands on its outriggers on the gravel, and the telehandler stands on its "
       "tyres on the yard."),
 mf=("The riggers unshackle the four slings from the carriage roof, and the mobile crane lifts the spreader bar from "
     "above the carriage to the gravel yard on the left ledge."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the riggers are "
       "already at the shackles: the slings come free one corner after another, the crane lifts the spreader bar a few "
       "metres clear of the roof, swings it slowly to the left over the ledge and sets it down on the gravel yard, where "
       "the crew unhooks it; then the crane raises its boom steeply until its tip and line rise above the top edge of the "
       "frame. The carriage stays exactly where it landed. The telehandler unloads the empty crates from the flatbed "
       "truck into a stack on the yard and the truck drives off, and a crew carries timber walk boards along the deck "
       "walkways. Small clouds drift slowly from the right, and the shadows fall forward to the left."))

# ---------- S2 ----------
scene(n=2, fiil="SÖKER", eleman="sekiz kırık pencere paneli soldan sağa → avludaki kasalara (sayım 8 → 0) · eski koltuk iskeletleri sol vestibülden atık konteynerine", rejim="A", t0="09:50", t1="10:00",
 g="G2",
 stage=(SEATED + ", " + RUSTY + ", " + PANES_OLD + ". " + U(UP()) + "; the spreader bar lies on the gravel yard, its slings coiled beside it. A "
        "stack of empty timber crates and a steel skip stand on the yard beside the small yellow telehandler, and glaziers "
        "with suction lifters wait on the near walkway under the first window."),
 moment="Ten to ten in the morning: the carriage is down and free, and the old windows come out first.",
 comp=C_CRANE + " " + C_YARD,
 light=LIGHT("09:50", "morning"), tr=TR_A,
 act=("Glaziers lift the broken old panes out of the window openings with suction lifters and carry them along the "
      "walkway into the crates on the yard, a second crew carries old seat frames out through the left vestibule into "
      "the skip, and the telehandler lifts each filled crate onto a flatbed truck. " + CREW),
 tex=T_RUST,
 phys=("The crates stand on the gravel yard, the skip rests on its skids on the gravel, and the telehandler stands on its "
       "tyres. The carriage rests on the steel deck, its underframe bolted down."),
 mf=("The glaziers lift the eight broken old panes out of the window openings, from left to right, and carry them "
     "along the walkway into the crates on the gravel yard."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the glaziers are "
       "already at the first window: one opening after another along the near side, from left to right, the broken "
       "clouded panes come out and the dark empty openings remain, until all eight stand empty and the dim stripped "
       "saloon shows through them; the openings keep their size and spacing. A second crew carries old seat frames out "
       "through the left vestibule and tips them into the skip, and the telehandler lifts the filled crates onto a "
       "flatbed truck, which drives off up the service road. At the end a truck tows a compressor trailer and a grit "
       "hopper onto the yard. Small clouds drift slowly, and the shadows fall forward to the left."))

# ---------- S3 ----------
scene(n=3, fiil="SIYIRIR", eleman="pas → çıplak gri çelik, soldan sağa (%0 → %100) · tavan dâhil · kum ve pas pulu brandada", rejim="B", t0="10:00", t1="12:00",
 g="G3",
 stage=(SEATED + ", " + RUSTY + "; " + OPEN8 + ". " + U(UP()) + ". A compressor trailer and a grit hopper stand on the "
        "gravel yard with blast hoses running along the near walkway, tarpaulins are spread along both walkways, and "
        "blasting crews in hoods stand at the left end of the carriage, a step ladder at each vestibule, and on the roof on harness lines."),
 moment="Ten in the morning: the windows are out, and the blasting crews line up at the left end.",
 comp=C_CRANE + " " + C_YARD,
 light=LIGHT("10:00", "morning"), tr=TR_B,
 act=("Blasting crews spray the carriage body with grit from the walkways and from the roof, working from the left end to the "
      "right, a crew with grinders follows them over the seams, a second crew shovels the spent grit and rust flakes "
      "from the tarpaulins into bags, and the compressor and the hopper feed the hoses. " + CREW_B),
 tex=T_BLAST,
 phys=("The compressor trailer and the hopper stand on their tyres on the gravel yard, the hoses rest on the walkway, "
       "and the roof crews are clipped to harness lines anchored to the deck handrails. The carriage rests on the steel "
       "deck, bolted down."),
 mf=("The blasting crews strip the rust and old paint from the carriage body and roof, from the left end to the right, "
     "and shovel the spent grit from the tarpaulins into bags."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Band by band from the left end the "
       "rust-brown skin turns a clean dull grey, the bare steel spreading steadily along the body and over the rounded "
       "roof until the whole carriage is bare grey steel from end to end; its shape, its eight empty openings and its two "
       "vestibules stay exactly as they were. The spent grit gathers on the tarpaulins, and the crews shovel it into "
       "bags and stack them on a pallet on the yard. At the end the compressor trailer is towed off and a paint trailer with spray "
       "rigs and pallets of paint drums arrives. The shadows swing slowly round behind the camera as the sun climbs, "
       "and clouds streak across the sky."))

# ---------- S4 ----------
scene(n=4, fiil="BOYAR", eleman="astar griden koyu zümrüt gövdeye + krem şerit, soldan sağa (%0 → %100) · tavan çıplak kalır", rejim="B", t0="12:00", t1="14:00",
 g="G4",
 stage=(SEATED + "; " + BARE + "; " + OPEN8 + ". " + U(UP()) + ". A paint trailer with spray rigs stands on the gravel "
        "yard beside pallets of paint drums and a stack of filled grit bags, tarpaulins are spread along both walkways, "
        "and spray crews in white overalls wait at the left end of the carriage."),
 moment="Noon: the carriage is bare grey steel, and the painters are waiting at the left end.",
 comp=C_CRANE + " " + C_YARD,
 light=LIGHT("12:00", "noon"), tr=TR_B,
 act=("Spray crews on the walkways spray a pale primer coat along the bare carriage from the left end to the right and "
      "follow it with the body coat, a second crew masks the tops of the window openings for a band, and a crew carries "
      "paint drums from the pallets on the yard to the spray rigs. " + CREW_B),
 tex=T_BARE,
 phys=("The paint trailer stands on its tyres on the gravel yard, the drums rest on pallets, and the spray crews stand on "
       "the walkway beside the handrails. The carriage rests on the steel deck, bolted down."),
 mf=("The spray crews paint the carriage body deep emerald green with a cream band along the tops of the windows, from "
     "the left end to the right, from the drums carried from the pallets on the yard."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. A pale primer coat sweeps along the bare "
       "steel from the left, and close behind it the deep emerald green follows, band by band, until the whole body is "
       "emerald from end to end; then a crisp cream band runs along the tops of the eight empty openings. The rounded "
       "roof stays bare grey steel. The crews carry drum after drum from the pallets, and the stacks of drums shrink. At "
       "the end a flatbed truck loaded with pallets of curved copper-coloured roof sheets arrives on the yard, and the "
       "crane lowers its boom and lifts a pallet. The shadows swing slowly from behind the camera to the left side as "
       "the sun passes, and clouds streak across the sky."))

# ---------- S5 ----------
scene(n=5, fiil="KAPLAR", eleman="bakır renkli çatı levhaları kavisli tavana, soldan sağa (%0 → %100) · siluet aynı", rejim="A", t0="14:00", t1="14:10",
 g="G5",
 stage=(SEATED + "; " + PAINT + "; its rounded roof is still bare grey steel; " + OPEN8 + ". " +
        U(HOOK("a pallet of copper-coloured roof sheets")) + ", the pallet hanging just above the middle of the roof. A "
        "flatbed truck stands on the gravel yard, and roofers on harness lines wait on the roof."),
 moment="Two in the afternoon: the body is emerald green, and the copper for the roof is coming down onto it.",
 comp=C_CRANE + " " + C_YARD,
 light=LIGHT("14:00", "pm"), tr=TR_A,
 act=("The mobile crane lowers the pallet of copper-coloured roof sheets onto a timber cradle on the middle of the roof, "
      "roofers carry the curved sheets along the roof and fix them to the old roof from the left end to the right, and "
      "a crew carries offcuts down to the skip; the crane carries a visible load. " + CREW),
 tex=T_BUILD,
 phys=("The pallet hangs from the crane hook on four taut slings. The roofers are clipped to harness lines anchored to "
       "the deck handrails, the new sheets are screwed down onto the old rounded roof, the pallet will rest on a timber "
       "cradle bolted to the roof, and the carriage rests on the steel deck, bolted down."),
 mf=("The roofers carry the curved copper-coloured sheets from the pallet the crane sets on the roof and fix them onto "
     "the old rounded roof, from the left end to the right."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the pallet is "
       "already settling onto its cradle on the roof: sheet by sheet from the left a warm copper-coloured skin spreads "
       "over the bare grey curve, following its exact line, until the whole roof is copper from end to end; the carriage "
       "keeps its height, its length and its silhouette. The pallet on the roof shrinks to bare boards and the crew lowers "
       "it to the yard. At the end the crane lifts a steel stillage of large window panes from a flatbed truck. A few "
       "clouds drift slowly from the left, and the shadows fall forward to the right."))

# ---------- S6 ----------
scene(n=6, fiil="CAMLAR", eleman="sekiz geniş temiz cam mevcut açıklıklara, soldan sağa (sehpa 8 → 0) · direkler korunur", rejim="A", t0="14:10", t1="14:20",
 g="G6",
 stage=(SEATED + "; " + PAINT + ", " + ROOF + "; " + OPEN8 + ". " + U(HOOK("a stillage of window panes")) + ", the "
        "stillage hanging just above the near walkway at the left end of the carriage. Glaziers with suction lifters wait "
        "on the walkway."),
 moment="Ten past two in the afternoon: the roof is copper, and the new windows hang beside the empty openings.",
 comp=C_CRANE + " " + C_YARD,
 light=LIGHT("14:10", "pm"), tr=TR_A,
 act=("The mobile crane sets the stillage of window panes down on the near walkway, glaziers lift the large panes off it "
      "with suction lifters and set them into the empty openings from left to right, a second crew seals each pane in "
      "its frame from inside, and a crew carries the empty stillage frame to the yard; the crane carries a visible load. " +
      CREW),
 tex=T_BUILD,
 phys=("The stillage hangs from the crane hook on two taut slings. Each pane is clamped into its opening between the "
       "steel window posts, the glaziers stand on the walkway, and the carriage rests on the steel deck."),
 mf=("The glaziers carry the large panes from the stillage on the walkway with suction lifters and set them into the "
     "eight existing window openings, from left to right."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the stillage is "
       "already settling onto the walkway: one after another, from left to right, a large clear pane goes into each "
       "empty opening and catches the sky, until all eight broad windows are glazed; the window posts, the openings and "
       "the length of the carriage stay exactly the same. The panes on the stillage go down to none. At the end a flatbed "
       "truck brings a short steel gangway onto the yard and the crane lifts it. A few clouds drift slowly from the "
       "left, and the shadows fall forward to the right."))

# ---------- S7 ----------
scene(n=7, fiil="BAĞLAR", eleman="sol yaya bağlantısı: kısa çelik geçit avlu → sol vestibül (%100) · iki sönük lamba direği", rejim="A", t0="14:20", t1="14:30",
 g="G7",
 stage=(CARR_DONE + ". " + U(HOOK("a short steel gangway")) + ", the gangway hanging just above the gap between the rim "
        "of the gravel yard and the left vestibule. Fitters with taglines wait on the yard rim and in the open left "
        "vestibule door, and a flatbed truck with bags of gravel stands on the yard."),
 moment="Twenty past two in the afternoon: the carriage is finished outside, and its first way in is about to land.",
 comp=C_CRANE + " " + C_YARD,
 light=LIGHT("14:20", "pm"), tr=TR_A,
 act=("The mobile crane lowers the short steel gangway onto its bearings between the yard rim and the left vestibule, "
      "fitters guide it with taglines and bolt both ends, welders fix its handrails, a crew carries bags of gravel from "
      "the truck and spreads a path to it, and an electrician sets a small unlit lamp post at each end; the crane carries "
      "a visible load. " + CREW),
 tex=T_BUILD,
 phys=("The gangway hangs from the crane hook on four taut slings. Its far end bears on a steel bracket at the left "
       "vestibule, its near end on a concrete pad on the yard rim; the lamp posts are anchored in the pads, and "
       "the carriage rests on the steel deck, bolted down."),
 mf=("The mobile crane lowers the short steel gangway from just above the gap onto its bearings between the yard rim and "
     "the left vestibule, and the fitters bolt it down."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the gangway is "
       "already sinking the last metre: it lands level across the short gap, the fitters bolt both ends, and welders run "
       "its handrails, until a short dark gangway links the gravel yard to the open left vestibule door; the gap below it "
       "stays open to the canyon. A crew carries bags of gravel from the truck and rakes a path to the gangway, and an "
       "electrician sets a small unlit lamp post at each end. At the end the crane lifts a second short gangway from a "
       "truck. A few clouds drift slowly from the left, and the shadows fall forward to the right."))

# ---------- S8 ----------
scene(n=8, fiil="BAĞLAR", eleman="sağ servis bağlantısı: geçit + birkaç basamak sağ vestibül → sağ raf patikası (%100) · iki sönük lamba", rejim="A", t0="14:30", t1="14:40",
 g="G8",
 stage=(CARR_DONE + "; " + GW_L + ", a small unlit lamp post at each end. " + U(HOOK("a second short steel gangway")) +
        ", the gangway hanging just above the gap between the right vestibule and the right ledge. Fitters wait on the "
        "right ledge beside a stack of stone steps and bags of mortar."),
 moment="Half past two in the afternoon: the main way in is done, and the service way out is landing at the right.",
 comp=C_CRANE + " " + C_YARD,
 light=LIGHT("14:30", "pm"), tr=TR_A,
 act=("The mobile crane lowers the second short gangway onto its bearings between the right vestibule and the right "
      "ledge, fitters bolt it and fix its handrails, masons set a few stone steps from the stack down to a footpath on the "
      "right ledge, and an electrician sets a small unlit lamp post at each end; the crane carries a visible load. " + CREW),
 tex=T_BUILD,
 phys=("The gangway hangs from the crane hook on four taut slings. Its near end bears on a steel bracket at the right "
       "vestibule, its far end on a concrete pad on the right ledge, the stone steps are bedded in mortar and rest "
       "on the rock, and the crane stands on its outriggers on the gravel."),
 mf=("The mobile crane lowers the second short gangway from just above the gap onto its bearings between the right "
     "vestibule and the right ledge, and the masons set the steps from the stack down to the footpath."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the second "
       "gangway is already sinking the last metre: it lands across the gap at the right end, the fitters bolt it and run "
       "its handrails, and masons set a few stone steps from the stack down to a footpath that leaves the right edge of "
       "the frame, until both ends of the carriage are reachable; the left gangway stays exactly where it is. At the end "
       "a long flatbed truck brings three large steel terrace frames onto the yard and the crane lifts the first one. A "
       "few clouds drift slowly from the left, and the shadows fall forward to the right."))

# ---------- S9 ----------
scene(n=9, fiil="ÇATAR", eleman="üç büyük çelik teras modülü yakın kirişin dirsek uçlarına, soldan sağa (kamyon 3 → 0) · altından kanyon görünür", rejim="A", t0="14:40", t1="14:50",
 g="G9",
 stage=(CARR_DONE + "; " + GW_BOTH + ". " + U(HOOK("a large steel terrace frame")) + ", the "
        "frame hanging just above the left bracket stubs on the near girder. A long flatbed truck with two more large "
        "steel frames stands on the gravel yard, and fitters wait on the near walkway with taglines."),
 moment="Twenty to three in the afternoon: both ends are linked, and the frame of the terrace is coming in.",
 comp=C_CRANE + " " + C_YARD,
 light=LIGHT("14:40", "pm"), tr=TR_A,
 act=("The mobile crane lowers the first large steel terrace frame onto the left bracket stubs, then lifts the other two "
      "from the long flatbed truck and sets them beside it, fitters guide each with taglines and bolt it to the near "
      "girder, and welders join the three frames; the crane carries a visible load. " + CREW),
 tex=T_BUILD,
 phys=("The frame hangs from the crane hook on four taut slings. Each frame is bolted to the bracket stubs along the near "
       "girder of the steel deck, which bears on steel pads on both ledges, and the truck stands on its tyres on the yard."),
 mf=("The mobile crane sets the three large steel terrace frames from the long flatbed truck onto the bracket stubs "
     "along the near girder, from left to right, and the fitters bolt them on."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the first frame "
       "module is already sinking onto the left stubs: the crane sets one large open steel frame after another along the "
       "near side, from left to right, each bolted to the girder, until a terrace skeleton reaches towards the camera "
       "over the canyon, an open grid with the drop visible through it and a rectangular opening in its middle. The "
       "three frames on the truck go down to none and the empty truck drives off. At the end a truck brings pallets of "
       "timber deck boards and the crane lifts a pallet. A few clouds drift slowly from the left, and the shadows fall "
       "forward to the right."))

# ---------- S10 ----------
scene(n=10, fiil="DÖŞER", eleman="ahşap döşeme sol + sağ bölüme ve vagon boyunca şeride (%0 → %100) · orta dikdörtgen BİLEREK açık", rejim="B", t0="14:50", t1="16:50",
 g="G10",
 stage=(CARR_DONE + "; " + GW_BOTH + "; " + FRAME + ", with a rectangular opening in its middle. " + U(HOOK("a pallet of timber deck boards")) + ", the pallet hanging just above the left section of the "
        "frame. A flatbed truck with more pallets of deck boards stands on the gravel yard, and carpenters wait on the "
        "frame on harness lines."),
 moment="Ten to three in the afternoon: the terrace frame is open over the drop, and its timber floor comes next.",
 comp=C_TERR,
 light=LIGHT("14:50", "pm"), tr=TR_B,
 act=("The mobile crane lowers a pallet of timber deck boards onto the frame, carpenters screw the boards down across "
      "the left and right sections and along the carriage, leaving the middle opening clear, a second crew fits steel "
      "edge frames round the opening, and a crew carries offcuts to the skip; the crane carries a visible load. " + CREW_B),
 tex=T_TIMBER,
 phys=("The pallet hangs from the crane hook on four taut slings. The deck boards are screwed down onto the steel "
       "terrace frames, which are bolted to the near girder and rest on the bracket stubs, the carpenters are clipped to harness lines, "
       "and the crane stands on its outriggers on the gravel."),
 mf=("The carpenters lay the timber deck boards from the crane-set pallets onto the left and right sections of the "
     "terrace frame and along the carriage, leaving the middle opening open."),
 body=("Two hours pass. Everything in this shot is time-lapsed at the same rate. Board by board warm pale timber spreads "
       "over the left and right sections of the open frame and along the carriage, until both side sections and the "
       "strip are decked; the rectangular middle section stays an open steel-framed opening with the drop below it, never "
       "covered. The pallets on the truck go down to none and the trucks leave empty. As the sun sinks on the left the "
       "light turns golden along the emerald side. At the end the crane sets a padded steel A-frame stand holding two "
       "large glass floor panels on the left timber section and lifts a third panel in a suction frame. The shadows "
       "swing slowly to the right and lengthen, and clouds streak across the sky."))

# ---------- S11 ----------
scene(n=11, fiil="CAMLAR", eleman="⭐ üç büyük cam döşeme paneli orta açıklığa: 1. panel vinçten, 2–3 sehpadan el arabasıyla (sehpa 2 → 0)", rejim="A", t0="16:50", t1="17:00",
 g="G11",
 stage=(CARR_DONE + "; " + GW_BOTH + "; " + FRAME_S + ", " + DECK_S + ", its rectangular middle section an open "
        "steel-framed opening over the drop. " +
        U(HOOK("a glass floor panel in a suction frame")) + ", the panel hanging just above the right third of the "
        "middle opening. A padded steel A-frame stand holding two more large glass floor panels stands on the left timber "
        "section beside a glass trolley, and glaziers wait round the opening."),
 moment="Ten to five in the afternoon, golden hour: the middle of the terrace is still open over the drop, and the glass is here.",
 comp=C_TERR + " " + C_GLASS,
 light=LIGHT("16:50", "golden"), tr=TR_A,
 act=("The mobile crane lowers the first large glass floor panel into the middle opening, glaziers seat it on its rubber "
      "bearers, then roll the other two panels from the A-frame stand on a glass trolley with a suction lifter and lower "
      "them in beside it, and a crew seals the joints; the crane carries a visible load. " + CREW),
 tex=T_TIMBER,
 phys=("The panel hangs in its suction frame from the crane hook on two taut slings. Each glass panel bears on rubber "
       "bearers in the steel edge frames, the A-frame stand rests on the timber decking, and the crane "
       "stands on its outriggers on the gravel."),
 mf=("The glaziers set three large glass floor panels into the middle opening of the terrace, the first lowered by the "
     "crane, the other two rolled from the A-frame stand on the glass trolley."),
 body=("Ten minutes pass in the golden light. Everything in this shot is time-lapsed at the same rate. From the first "
       "frame the first panel is already sinking into the right third of the opening and settles on its bearers; then "
       "the glaziers roll a second panel from the stand on the glass trolley and lower it into the middle, and a third "
       "into the left third, until three large clear glass panels fill the opening. The canyon stays visible far below "
       "through them, and the panel edges and soft reflections of the sky show the glass. The stand on the timber goes "
       "empty and the crew carries it off. At the end the crane lifts a crate of glass guardrail panels. Long golden "
       "shadows fall to the right, and a few clouds drift slowly from the left."))

# ---------- S12 ----------
scene(n=12, fiil="ÇEVİRİR", eleman="ince koyu dikmeli şeffaf korkuluk terasın açık kenarlarına (%0 → %100) · dibinde sönük ışık şeridi", rejim="A", t0="17:00", t1="17:10",
 g="G12",
 stage=(CARR_DONE + "; " + GW_BOTH + "; " + FRAME_S + ", " + DECK_S + ", " + GLASS_S + ", its edges still open. " +
        U(HOOK("a crate of glass guardrail panels")) +
        ", the crate hanging just above the right timber section. Glaziers wait at the terrace edges beside bundles of "
        "slim dark posts."),
 moment="Five in the afternoon, golden hour: the glass floor is in, and its edges are still open to the drop.",
 comp=C_TERR + " " + C_GLASS,
 light=LIGHT("17:00", "golden"), tr=TR_A,
 act=("The mobile crane sets the crate of guardrail panels down on the right timber section, glaziers bolt slim dark "
      "posts along the open edges of the terrace and slide the clear glass panels in between them, an electrician fits "
      "a line of small unlit lights along their foot, and a crew carries the empty crate to the yard; then the crane "
      "raises its boom steeply. " + CREW),
 tex=T_TIMBER,
 phys=("The crate hangs from the crane hook on four taut slings. The posts are bolted to the steel edge of the terrace "
       "frames, the glass panels are clamped between them, and the deck boards rest on the frames."),
 mf=("The glaziers fit the slim dark posts and clear glass guardrail panels from the crate on the right timber section "
     "along the open edges of the terrace, from the right side round to the left."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the crate is "
       "already settling on the timber: post by post and pane by pane a clear guardrail grows along the open edges of "
       "the terrace, from the right side round the near edge to the left side, until every open edge is enclosed, a line "
       "of small unlit lights along its foot; the walkway strip and the glass floor stay clear. The crew carries the empty "
       "crate to the yard, the crane raises its boom steeply until its tip and line rise above the top edge of the frame, "
       "and a truck loaded with tables and chairs arrives on the yard. The sun sinks low on the left, long golden shadows "
       "fall to the right, and a few clouds drift slowly."))

# ---------- S13 ----------
scene(n=13, fiil="DÖŞER", eleman="dört dış masa + sandalyeler kamyondan sol geçitten terasın iki ahşap bölümüne (ikişer) · cam orta ve kapı önleri boş", rejim="A", t0="17:10", t1="17:20",
 g="G13", hedef="G15",
 stage=(FIN + ". " + U(UP()) + ". A flatbed truck "
        "loaded with timber dining tables and stacked chairs stands on the gravel yard, and a stack of empty crates stands "
        "beside the skip."),
 moment="Ten past five, sunset: the terrace is finished and empty, and the furniture has arrived.",
 comp=C_TERR + " " + C_GLASS,
 light=LIGHT("17:10", "golden"), tr=TR_A,
 act=("Crews carry four timber dining tables and stacks of chairs from the flatbed truck across the left gangway onto "
      "the terrace and set two tables on each timber section, a second crew wipes the glass floor and the guardrails "
      "clean, and the emptied truck drives off up the service road. " + CREW),
 tex=T_DONE,
 phys=("The truck stands on its tyres on the gravel yard, the tables and chairs stand on the timber decking, and the "
       "guardrail posts are bolted to the terrace frames. The crane stands on its outriggers on the gravel, its boom "
       "raised steeply."),
 mf=("The crews carry the four timber dining tables and their chairs from the flatbed truck on the yard across the left "
     "gangway onto the two timber sections of the terrace."),
 body=("Ten minutes pass as the sun sets. Everything in this shot is time-lapsed at the same rate. From the first frame "
       "the crews are already crossing the left gangway with the first table: two tables with their chairs appear on "
       "the left timber section and two on the right, set square to the rail, while the glass middle section and the "
       "space in front of both doors stay clear. The second crew wipes the glass floor and the rails. The truck goes "
       "empty and drives off up the service road, and at the end the crane lowers its boom, the crew hooks a bundle of "
       "empty crates to it on the yard, and the crane lifts it. The sun reaches the far ridges on the left, the last warm light slides "
       "up the copper roof, and a few clouds drift slowly."))

# ---------- S14 (İÇ İSTASYON · S13 ile aynı on dakika) ----------
INT_BASE = ("the saloon has been stripped and lined: a new floor of warm timber boards runs down the whole length, the "
            "walls below and between the eight broad clear windows on each side are lined with pale panels, the rounded "
            "ceiling under the copper roof is smooth cream, a step ladder stands against the left wall, and the glazed "
            "door stands in the middle of the right end wall")
scene(n=14, fiil="DONATIR", eleman="iç: ahşap masa modülleri + deri banklar pencerelerin önüne, sağ kapıdan (istif → %100) · sarkıt lambalar (sönük)", rejim="A", t0="17:10", t1="17:20",
 g="G14", hedef="G14′", ic=True,
 stage=(INT_BASE + ". The saloon is empty except for a stack of wrapped timber table tops and table frames and four "
        "wrapped leather bench seats standing just inside the glazed door at the far end, and a coil of lamp cable on "
        "the floor. Through the right-hand windows the near walkway and the guardrail of the terrace show against the "
        "open air."),
 moment="Ten past five, sunset, the same ten minutes as the furniture going out onto the terrace: the saloon is lined and empty.",
 comp="",
 light=("LIGHTING: " + sunline("17:10") + ", low behind the camera on the right, so long thin bands of warm low sunlight "
        "fall in through the right-hand windows across the floor and up the left wall, while the rest of the saloon is "
        "in soft daylight and the view through the panes is brighter than the room. The sun stays outside the frame."),
 tr=TR_INT,
 act=("Crews carry the timber table tops and frames from the stack at the glazed door down the aisle and set them "
      "against the windows on both sides, a second crew rolls the leather bench seats down the aisle on a hand cart and bolts one "
      "between each pair of tables, and an electrician hangs a row of unlit pendant lamps along the ceiling. " + CREW_B),
 tex=T_INT,
 phys=("The stack of wrapped table tops rests on the floor boards by the glazed door, and the step ladder stands on "
       "the floor. The floor boards rest on the steel underframe of the carriage, which is bolted to the girders of the "
       "deck, and the wall panels are clamped to the steel posts between the windows."),
 mf=("The crews carry the timber tables and the leather bench seats from the stack at the glazed door down the aisle "
     "and set them along the windows on both sides, turning the empty saloon into a dining room."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the crews are "
       "already lifting the first table from the stack: one after another the timber tables are set against the windows "
       "on both sides, each with a leather bench between them, from the far end towards the camera, until two rows of "
       "tables with benches line the whole saloon and the centre aisle stays clear; a row of unlit pendant lamps hangs "
       "along the ceiling. The stack at the door goes down to none. Outside the windows the clouds drift slowly, and the "
       "bands of low sunlight slide slowly up the left wall and fade as the sun reaches the ridges."))

INT_SON = dict(g="G14′", t="17:20",
 stage=(INT_BASE + ". The saloon is now a dining room: two rows of timber tables stand against the windows on both "
        "sides, a leather bench between each pair, the centre aisle clear, and a row of unlit pendant lamps hangs along "
        "the ceiling. Folded packing film lies by the glazed door. Through the right-hand windows the near walkway and "
        "the guardrail of the terrace show against the open air."),
 moment="Twenty past five, sunset: the saloon is furnished as a dining room, its lamps still unlit.",
 comp="",
 light=("LIGHTING: " + sunline("17:20") + ", behind the camera on the right: the last thin band of warm light fades from "
        "the top of the left wall, the saloon is in soft even daylight, and the view through the panes is brighter than "
        "the room. The sun stays outside the frame."),
 tr=TR_INT,
 act=("The work is finished: the last worker carries the folded packing film out through the glazed door as faint soft "
      "motion streaks, and the room stands still."),
 tex=T_INT.replace("packing film and offcuts stacked by the glazed door", "folded packing film by the glazed door")
         .replace("bands of low sunlight across the floor", "a last band of low sunlight high on the left wall"),
 phys=("The tables stand on their frames on the floor boards, and each bench seat is bolted to the floor between two "
       "tables. The pendant lamps hang from the ceiling on short cords, and the floor boards rest on the steel underframe."))

# ---------- S15 ----------
scene(n=15, fiil="BOŞALTIR", eleman="vinç + telehandler + kamyonlar + kasalar + atık konteyneri servis yolundan sırayla ÇIKAR · saha açılır", rejim="A", t0="17:20", t1="17:30",
 g="G15",
 stage=(FIN + "; " + TABLES + "; " + LAMPS_OFF + ". " + U(HOOK("a bundle of empty crates")) + ", hanging just above a "
        "flatbed truck on the yard, beside the telehandler, the skip and a stack of pallets."),
 moment="Twenty past five, the sun on the ridges: the restaurant is built, and the site is being cleared.",
 comp=C_TERR + " " + C_GLASS,
 light=LIGHT("17:20", "dusk"), tr=TR_A,
 act=("The mobile crane lowers the bundle of empty crates onto the flatbed truck, the telehandler lifts the pallets and "
      "the skip onto a second truck, a crew rakes the yard, and the crane stows its boom and drives off behind the "
      "trucks; the crane carries a visible load. " + CREW),
 tex=T_DONE,
 phys=("The bundle hangs from the crane hook on two taut slings. The crane stands on its outriggers on the gravel, "
       "the trucks stand on their tyres on the yard, and the carriage rests on the steel deck."),
 mf=("The mobile crane, the telehandler, the trucks, the empty crates, the pallets and the skip leave the site in turn, "
     "from the gravel yard up the service road to the left edge of the frame."),
 body=("Ten minutes pass. Everything in this shot is time-lapsed at the same rate. From the first frame the bundle is "
       "already settling onto the truck: the telehandler lifts the pallets and the skip onto a second truck, the trucks "
       "drive off up the service road one after another, the crane folds its boom down and drives slowly after them out "
       "of the left edge of the frame, the telehandler follows, and a crew rakes the yard smooth. For the first time the "
       "restaurant stands alone over the canyon, every part of it in view. A white van comes down the road at the end "
       "and stops on the yard. The last warm light leaves the rims, and a few clouds drift slowly from the left."))

# ---------- S16 ----------
scene(n=16, fiil="YAKAR", eleman="alacakaranlık: vagon içi ışıklar → geçit lambaları → korkuluk dibi ışık şeridi, gruplar hâlinde (her grup TEK karede)", rejim="A", t0="17:30", t1="17:40",
 g="G16", iso=800,
 stage=(FIN + "; " + TABLES + "; " + LAMPS_OFF + ". A white van stands on the raked gravel yard, its rear doors open, "
        "and restaurant staff in dark aprons stand at the left gangway beside an electrician at a small switch box on "
        "the yard rim."),
 moment="Half past five, dusk: the restaurant is ready, and its lights are still off.",
 comp=C_TERR + " " + C_GLASS,
 light=LIGHT("17:30", "dusk"), tr=TR_A_DUSK,
 act=("An electrical crew at the switch box switches the lights on group by group, a crew of waiters pushes a hand "
      "cart of folded white cloths from the van across the left gangway and spreads a cloth on each of the four terrace "
      "tables, and kitchen staff carry crates of supplies from the van into the carriage. Staff show as faint soft "
      "motion streaks, no readable faces."),
 tex=T_EVE,
 phys=("The van stands on its tyres on the gravel yard, the lamp posts are anchored at the gangway ends, and the small "
       "lights are fixed along the foot of the guardrails bolted to the terrace frames."),
 mf=("The electrician switches the lights on from the switch box on the yard rim, in three groups: first the lamps "
     "inside the carriage, then the lamps at the two gangways, last the small lights along the foot of the guardrails."),
 body=("Ten minutes pass as the day turns to dusk. Everything in this shot is time-lapsed at the same rate. The sky fades "
       "from pale gold to a soft clear blue and the canyon darkens slowly, never to black. The lights come on in groups, "
       "each group at once: first warm light fills all eight windows of the carriage, then the small lamps at both ends "
       "of the two gangways, last the line of small warm lights along the foot of the guardrails. Waiters carry cloths "
       "and cushions from the van over the left gangway to the four terrace tables, and kitchen staff carry crates of "
       "supplies from the van into the carriage. A few clouds drift slowly and fade to blue-grey."))

# ---------- S17 ----------
scene(n=17, fiil="GETİRİR", eleman="ilk konuk grupları servis yolundan → avlu → sol geçit → sol vestibül · pencerelerde silüetler (içerdeki masaların çoğu)", rejim="A", t0="17:40", t1="17:50",
 g="G17", iso=1600,
 stage=(FIN + "; " + TABLES + "; " + LAMPS_ON + ". The white van stands on the raked gravel yard, two waiters in dark "
        "aprons stand at the left gangway, and the four terrace tables are laid with white cloths, still empty."),
 moment="Twenty to six, blue hour: the lamps are lit, and the dining room is ready to open.",
 comp=C_TERR + " " + C_GLASS,
 light=LIGHT("17:40", "blue"), tr=TR_A_DUSK,
 act=("A crew of waiters at the left gangway waves the first small groups of guests in, the guests walk down the "
      "service road across the yard and over the left gangway into the left vestibule, silhouettes settle at the tables "
      "behind the lit windows, and a waiter pulls a hand cart of glasses from the van into the carriage. " + CROWD_A),
 tex=T_EVE,
 phys=("The van stands on its tyres on the gravel yard, the gangway bears on its pads, and the carriage rests on the "
       "steel deck, its underframe bolted down."),
 mf=("The first small groups of guests walk from the service road across the gravel yard and over the left gangway into "
     "the left vestibule, and sit down at the tables behind the lit windows."),
 body=("Ten minutes pass in the blue hour. Everything in this shot is time-lapsed at the same rate. From the first frame "
       "the first small groups are already coming down the road: they cross the yard and the left gangway and pass in "
       "through the left vestibule, each person walking in before sitting, and one after another small dark silhouettes "
       "settle behind the warm windows until most of the tables inside are taken; the terrace tables and the glass floor "
       "stay empty. A waiter carries a crate of glasses from the van into the carriage. The sky deepens slowly to a clear "
       "blue, the carriage windows the brightest things in the frame, and a few clouds drift slowly."))

# ---------- S18 ----------
scene(n=18, fiil="CANLANDIRIR", eleman="⭐ gerçek zaman: içerde masalar dolu · birkaç konuk sol geçitten terasa çıkar, iki-üç dış masaya oturur · cam boş", rejim="G", t0="17:50:00", t1="17:50:08",
 g="G18", iso=1600,
 stage=(FIN + "; " + TABLES + "; " + LAMPS_ON + ". Behind the lit windows most tables inside are taken, small dark "
        "silhouettes of seated guests; the four terrace tables are laid with white cloths and still empty, and a waiter "
        "stands at the left gangway."),
 moment="Ten to six, deep blue hour: the dining room is full, and the terrace is about to fill.",
 comp=C_TERR + " " + C_GLASS,
 light=LIGHT("17:50", "blue"), tr=TR_G,
 act=("A crew of waiters leads two small groups of guests from the left vestibule onto the terrace and pulls the "
      "chairs back at three of the timber tables, the guests sit down, a waiter rolls a small serving cart along the "
      "walkway, and the silhouettes inside move in small natural ways. " + CROWD_G),
 tex=T_EVE,
 phys=("The tables and chairs stand on the timber decking, the guardrail posts are bolted to the terrace frames, and the "
       "carriage rests on the steel deck, its underframe bolted down."),
 mf=("Two small groups of guests walk from the left vestibule onto the terrace and sit down at three of the timber "
     "tables, while the glass middle section stays clear."),
 body=("Eight seconds pass. Everything in this shot moves at natural speed. A waiter steps out of the left vestibule onto "
       "the terrace walkway and two small groups of guests follow, walking at an easy pace to the timber tables; chairs "
       "are drawn out and the guests sit down at three of the four tables, small distant figures without detailed hand "
       "movement. Behind the warm windows the seated silhouettes turn and lean in small natural ways. A waiter rolls "
       "a small serving cart along the walkway and sets a carafe on a table. The glass middle section stays empty. The pine branches sway slightly in a "
       "light breeze, and the clouds hold still in the deep blue sky."))

# ---------- S19 ----------
scene(n=19, fiil="TAMAMLAR", eleman="bir çift sol ahşap bölümden cam orta bölüme yürür, vadiye bakar (0–4 sn) · TUTUŞ (4–8 sn) · yeni yapı yok", rejim="G", t0="17:50:08", t1="17:50:16",
 g="G19", iso=1600,
 stage=(FIN + "; " + TABLES + "; " + LAMPS_ON + ". Behind the lit windows most tables inside are taken by seated "
        "silhouettes; guests sit at three of the four terrace tables, and an adult couple stands at the left timber "
        "section beside the glass middle section, which is clear."),
 moment="Ten to six, deep blue hour: the restaurant is full, and a couple is about to step out over the drop.",
 comp=C_TERR + " " + C_GLASS,
 light=LIGHT("17:50:08", "blue"), tr=TR_G,
 act=("An adult couple walks from the left timber section onto the glass middle section and stops to look out at the "
      "valley, a crew of waiters sets a carafe on a terrace table and rolls the serving cart back to the left gangway, "
      "and the diners inside move in small natural ways. " + CROWD_G),
 tex=T_EVE,
 phys=("The couple stands on the glass floor panels, which bear on rubber bearers in the steel edge frames; the tables "
       "stand on the timber decking, and the carriage rests on the steel deck."),
 mf=("The couple walks from the left timber section onto the glass middle section of the terrace and stands there "
     "above the canyon, looking out at the valley."),
 body=("Eight seconds pass. Everything in this shot moves at natural speed. In the first four seconds the couple walks "
       "calmly from the left timber section onto the glass floor and stops near its middle, turned towards the valley, "
       "seen from the side and from behind; the canyon stays visible far below the glass under their feet. A waiter "
       "sets a carafe on a terrace table and walks back to the left gangway; nothing is built and nothing in the "
       "restaurant moves. From about four to eight seconds the scene holds: the couple stands still on the glass, the "
       "diners inside and on the terrace move in small natural ways, the pine branches sway slightly in the light breeze "
       "and the clouds hold still in the deep blue sky; nothing else changes."))

USTA = dict(g="G20", t="17:50:16", iso=1600,
 stage=(FIN + "; " + TABLES + "; " + LAMPS_ON + ". Behind the lit windows most tables inside are taken by seated "
        "silhouettes; guests sit at three of the four terrace tables, and an adult couple stands near the middle of the "
        "glass floor, turned towards the valley. The gravel yard lies raked and "
        "empty except for one white van."),
 moment="Ten to six, deep blue hour: the old carriage is a lit restaurant over the canyon.",
 comp=C_TERR + " " + C_GLASS + " The lit windows are the brightest things in the frame.",
 light=LIGHT("17:50:16", "blue"), tr=TR_G,
 act=("Diners sit inside and on the terrace, a waiter walks along the walkway, and the couple stands on the glass. " +
      CROWD_G),
 tex=T_EVE,
 phys=("The couple stands on the glass floor panels, which bear on rubber bearers in the steel edge frames; the "
       "terrace frames are bolted to the near girder, and the carriage rests on the deck, bolted down."))

# ── yazıcılar ───────────────────────────────────────────────────────────────
def lens(iso): return f"Lens: 28 mm rectilinear, f/8, ISO {iso}."

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

def gorsel_ic(d, head):
    return "\n".join([
        head, lens(d.get("iso", 200)), CAM_INT, "",
        STRUCT + " AT THIS STAGE: " + d["stage"], "",
        SITE_INT, "",
        "THE TIME MOMENT: " + d["moment"], "",
        COMP_INT, "",
        d["light"], "",
        d["tr"], "",
        "ACTIVITY: " + d["act"], "",
        "SITE TEXTURE: " + d["tex"], "",
        "PHYSICS: " + d["phys"], "",
        NEG_INT, OUTPUT])

def i2v(d):
    if d.get("ic"):
        return "\n\n".join([I2V_HEAD, "MOTION FOCUS: " + d["mf"], d["body"], LOCK_INT, I2V_TAIL_INT])
    lock = LOCK_MAIN + ("" if d.get("seated") is False else LOCK_SEATED)
    return "\n\n".join([I2V_HEAD, "MOTION FOCUS: " + d["mf"], d["body"], lock, I2V_TAIL])

RJ = {"A": "A (10 dk)", "B": "B (2 sa)", "G": "G (8 sn · gerçek zaman · ölçülmedi)"}
def blok(d):
    n = d["n"]; bas, son = n * 8, (n + 1) * 8
    ist = "CARRIAGE (iç · paralel zaman · 1/1)" if d.get("ic") else "MAIN"
    hedef = d.get("hedef", f"G{n+1}")
    out = [f"## 🎬 SAHNE {n} — {d['fiil']}", "",
           "```",
           f"SÜRE: 8,0 s ({bas},0–{son},0)  ·  ELEMAN + ARA HÂL: {d['eleman']}  ·  REJİM: {RJ[d['rejim']]}  ·  SAAT: {d['t0']}→{d['t1']}  ·  İSTASYON: {ist}",
           "```", ""]
    if n in (0, 1):
        out += ["> 🏗️ **Kaldırma** [DERS 57 · DERS 8]: vagon G0'da tabliyenin 1 m üstünde, kısa ve gergin sapanlarda ASILI başlar;",
                "> klip yalnız son metreyi ve oturmayı gösterir. Yerden kalkış YOK. Oturduktan sonra vagon bir daha kalkmaz,",
                "> sallanmaz, kaymaz (LOCK cümlesi S1'den itibaren). Sapanlar S1'de çözülür.", ""]
    if n == 11:
        out += ["> 🔍 **Cam** [PLAN §CAM]: cam, kenar çerçevesi + gök yansımasıyla okunur; ayna gibi opak cam ya da yüzeysiz",
                "> açıklık YAZILMAZ. Üç panelin yalnız ilki vinçte; ikisi sehpadan el arabasıyla — üç ayrı havada taşıma yok.", ""]
    if n == 13:
        out += ["> 🪟 **İç istasyon dikişi** [ISTASYON_VE_IC_MEKAN §2]: bu klibin I2V'si ana kare **G15**'e biter; G14 iç",
                "> istasyonun karesidir (ana zincirde G14 numarası iç kameraya ayrıldı). S15 yine G15'ten başlar.", ""]
    if d.get("ic"):
        out += ["> 🪟 **İÇ İSTASYON (CARRIAGE)** — ana zincirin DIŞINDA: S13 ile AYNI on dakikanın (17:10→17:20) içeriden",
                "> görüntüsü. Bu klip G14 → G14′ (iç) · S13'ün I2V'si G15'e biter · S15 G15'ten başlar. Dış kare iki yakada",
                "> AYNIDIR; dış yapı bu klipte büyümez [KAMERA_ISTASYONU §1 ④ · DERS 52]. Tilt 14° iki kamerada aynı (PLAN beyanı).", ""]
    if n in (16, 17, 18, 19):
        out += ["> 🏮 **Işık defteri** [ISIK_FINALI §2 · §4]: S16'da üç grup sırayla ve her grup TEK KAREDE yanar (vagon içi →",
                "> geçit lambaları → korkuluk dibi); bir daha sönmez. Final güneş −4,9° (−4…−6 penceresi).", ""]
    if d["rejim"] == "G":
        out += ["> 🍽️ **Rejim G (8 sn · 1×)** [SANTIYE_HAREKETI §1]: iz YOK; konuklar yandan/arkadan, yüz okunmaz. Final ödülü",
                "> hareketin DOĞAL HIZDA olmasıdır (yürüyüş, oturma, rüzgâr). Üç rejim (A · B · G) — PLAN §REJİM SAYISI'nda beyanlı.", ""]
    if d.get("ic"):
        out += [f"### 📸 GÖRSEL PROMPT ({d['g']} · İÇ İLK KARE)", "", "```", gorsel_ic(d, HEAD_INT), "```", ""]
        out += [f"### 🎥 I2V PROMPT ({d['g']} → {hedef})", "", "```", i2v(d), "```", ""]
        out += ["### 🪟 İÇ SON KARESİ (G14′ · bu klibin hedefi — sahne görseli DEĞİL, kapı saymaz)", "",
                "> Kapı bu bloğu saymaz (başlıkta GÖRSEL PROMPT yok) — ama aynı disiplinle yazıldı: STRUCTURE,",
                "> SITE / BACKGROUND, NEGATIVE iç karelerde birebir. Üretimde G14′ ÖNCE üretilir (ana G15'in saati ve",
                "> ışığıyla), G14 ondan geriye (mobilya geri alınarak) [ISTASYON_VE_IC_MEKAN §2].", "",
                "```", gorsel_ic(INT_SON, HEAD_INT_SON), "```", "", "---", ""]
        return "\n".join(out)
    out += [f"### 📸 GÖRSEL PROMPT ({d['g']})", "", "```", gorsel_main(d, HEAD_MAIN.format(n=n)), "```", ""]
    out += [f"### 🎥 I2V PROMPT ({d['g']} → {hedef})", "", "```", i2v(d), "```", "", "---", ""]
    return "\n".join(out)

def usta_blok():
    return "\n".join([
        "## 🌟 USTA KARE — G20 (SAHNE DEĞİLDİR · son klibin hedefi · kapak kaynağı)", "",
        "> Üretim sırasının İLK karesi [§8]: G20 önce üretilir ve ikna edici değilse DURULUR; sonra",
        "> image-to-image geriye G19 → G18 → … → G0 (iç kareler kendi küçük zincirinde: G14′ → G14). Kapı: tek vagon,",
        "> sekiz pencere, iki vestibül, iki geçit, teras + üç cam panel + korkuluk · konuklar içerde ve üç dış masada ·",
        "> çift camın üstünde, yüzü okunmaz · gök MAVİ ve okunur (güneş −4,9°) · kanıt nesnesi yarık kaya ·",
        "> vinç, kamyon, kasa, palet YOK (SÖKÜM satırı). Kapak (`THE_LAST_CARRIAGE_KAPAK.md`) bu promptun kopyasıdır.", "",
        "### 📸 USTA KARE PROMPT (G20)", "", "```",
        gorsel_main(USTA, HEAD_USTA), "```", ""])

H1 = f"""# 🎬 {FILM} — BÖLÜM 1  (S0 – S9 · G0 … G9 + 10 I2V · 0,0–80,0 sn)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler, merdiven ve kare tablosu
> `{FILM}_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek
> başına çalışır. STRUCTURE, SITE / BACKGROUND ve NEGATIVE blokları bütün ana karelerde BİREBİR aynı
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
> ⛔ Vinç kancası [DERS 8 · 57]: vinç (G0–G15) her karede ya YÜKLÜ ("with a … on the hook on taut slings") ya da bom
> ucu KADRAJ DIŞINDA ("its tip and line above the top edge of the frame"); boş kanca hiçbir promptta yazılmaz.
> Her vinçli klipte yük ilk karede hedefin HEMEN ÜSTÜNDE asılı başlar.
>
> ⛔ Kelime kilitleri: "rust" yalnız G0–G3 ve S0–S3'te; "emerald" S4 I2V'sinden, "copper" S4 sonundan (palet) ve
> G5'ten; "gangway" G7'den; "terrace frame" G8 sonundan; "glass floor" S10 sonundan; ışıkların yanması yalnız S16
> I2V'sinden sonra; "guests" yalnız S17 I2V'sinden sonra. YASAK KELİME (PLAN künyesi) hiçbir promptta yok — negatifte bile.

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
> 🪟 **S14 İÇ İSTASYONDUR** (CARRIAGE · tek klip · %5): S13 ile aynı on dakika; S13'ün I2V'si G15'e biter.
> İç kamera bloğunun SITE'ı ana SITE ile iki cümleyi BİREBİR paylaşır (yarık kaya · uzak sırtlar) [DERS 10].
>
> 🏮 **S16 → S19 TEK AKŞAMDIR**: ışık grupları S16'da sırayla yanar ve bir daha sönmez; konuklar S17'de yalnız
> servis yolundan ve sol geçitten gelir, oturan kalkıp kaybolmaz; S18–S19 gerçek zamandadır (rejim G).
>
> ⭐ **USTA KARE G20 bu dosyanın sonunda, kendi `## 🌟 USTA KARE` bölümündedir** — sahne
> değildir, son klibin (S19: G19 → G20) hedef karesidir ve kapak kaynağıdır.
>
> ⭐ S19'un ikinci yarısı TUTUŞTUR (final kanıtı 156,0–160,0); insan kuralı "no readable faces".

---
"""

if "--tablo" in sys.argv:
    for d in S + [INT_SON, USTA]:
        t = d["t"] if "t" in d else d["t0"]
        az, e = sun(hm(t))
        print(d["g"], t, f"{az}°", f"{e:.1f}°".replace(".", ","), f"bağıl güneş {((az - BEARING + 180) % 360) - 180:+d}°")
    sys.exit(0)

if "--kadraj" in sys.argv:
    print("ufuk/sırt (üstten)", UFUK, "· %", pct(UFUK), "· f", round(F_PX), "px")
    rows = [("yarık kaya sol", (14, 10, -1)), ("yarık kaya sağ", (17.5, 10, -1)), ("yarık kaya tepe", (15.75, 10, 5.5)),
            ("çatal çam dip", (-18, -4, 0)), ("çatal çam tepe", (-18, -4, 13)),
            ("vagon sol çatı", (-12.2, -1.45, 4.2)), ("vagon sağ çatı", (12.2, -1.45, 4.2)),
            ("vagon sol alt", (-12.2, -1.45, 0)), ("vagon sağ alt", (12.2, -1.45, 0)), ("vagon orta çatı", (0, 0, 4.6)),
            ("pencere bandı sol", (-11, -1.45, 2.4)), ("pencere bandı sağ", (11, -1.45, 2.4)),
            ("G0 vagon altı (+1 m)", (0, -1.45, 1.0)),
            ("sol geçit avlu ucu", (-15.5, -2.5, 0)), ("sağ geçit raf ucu", (15.5, -2.5, 0)),
            ("kiriş sol mesnet", (-11, -3, -1.8)), ("kiriş sağ mesnet", (11, -3, -1.8)),
            ("teras ön sol", (-7.5, -9, 0)), ("teras ön sağ", (7.5, -9, 0)), ("teras arka sol", (-7.5, -3, 0)),
            ("cam ön sol", (-2.4, -9, 0)), ("cam ön sağ", (2.4, -9, 0)), ("cam arka sol", (-2.4, -4, 0)), ("cam arka sağ", (2.4, -4, 0)),
            ("vinç (avlu)", (-24, 6, 0)), ("avlu", (-20, 2, 0)), ("servis yolu (sol kenar)", (-34, -2, 1))]
    for ad, Q in rows:
        x, y = proj(Q); print(f"{ad:26s} x {x:5d} · üstten {y:4d} · %{pct(y)}")
    for ad, Q in [("cam orta", (0, -6.5, 0)), ("sol geçit", (-15, -2.5, 0)), ("teras sol masa", (-5, -6, 0))]:
        a, b = proj(Q), proj((Q[0], Q[1], Q[2] + 1.7)); print(f"insan (1,7 m) {ad}: {a[1] - b[1]} px")
    print("cama bakış", round(math.degrees(math.atan2(11, math.dist((12, -30), (0, -6.5)))), 1), "° · vagona uzaklık",
          round(math.dist((12, -30, 11), (0, 0, 2)), 1), "m · kayaya", round(math.dist((12, -30, 11), (15.75, 10, 2)), 1), "m")
    print("— iç istasyon —")
    for ad, Q in [("sağ uç duvar sol üst", (11, 1.35, 3.9)), ("sağ uç duvar sağ üst", (11, -1.35, 3.9)), ("uç duvar dibi", (11, 0, 1.0)),
                  ("cam kapı sol", (11, 0.45, 3.0)), ("cam kapı sağ", (11, -0.45, 3.0)), ("yakın taban", (-8, 0.3, 1.0)),
                  ("yarık kaya (pencereden)", (15.75, 10, 2))]:
        x, y = proj_ic(Q); print(f"{ad:26s} x {x:5d} · üstten {y:4d} · %{pct(y)}")
    sys.exit(0)

b1 = H1 + "\n" + "\n".join(blok(d) for d in S if d["n"] <= B1_SON)
b2 = H2 + "\n" + "\n".join(blok(d) for d in S if d["n"] > B1_SON) + "\n" + usta_blok()
open(os.path.join(OUT, f"{FILM}_BOLUM_1.md"), "w").write(b1)
open(os.path.join(OUT, f"{FILM}_BOLUM_2.md"), "w").write(b2)
print("yazıldı", len(b1), len(b2))
