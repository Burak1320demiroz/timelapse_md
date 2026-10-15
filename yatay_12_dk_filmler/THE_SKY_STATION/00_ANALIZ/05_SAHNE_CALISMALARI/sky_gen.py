#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""THE SKY STATION — perde dosyaları üreticisi (91 görsel + 90 I2V).
Ortak bloklar tek kaynaktan, harfi harfine aynı [DERS 20]."""
import math, os, re, sys

FILM = "THE_SKY_STATION"
KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # film klasörü
N = 90

# ── rejim ve saat ─────────────────────────────────────────────────────────
G_SET = {64, 65, 66, 84, 85, 86, 87, 88, 89}
def rejim(s): return "G" if s in G_SET else "A"
SAAT = []
_m = 6 * 60 + 10
for s in range(N):
    SAAT.append(_m)
    if rejim(s) == "A":
        _m += 10
SAAT.append(_m)  # G90
assert SAAT[90] == 19 * 60 + 40, SAAT[90]

def hhmm(m): return f"{m // 60:02d}:{m % 60:02d}"

def saat_en(m):
    h, mi = divmod(m, 60)
    def ad(x):
        x = x % 12 or 12
        return ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve"][x]
    if h < 12: gun = "in the morning"
    elif h < 17: gun = "in the afternoon"
    else: gun = "in the evening"
    if m == 12 * 60: return "Noon"
    if mi == 0: t = f"{ad(h)} o'clock"
    elif mi == 10: t = f"ten past {ad(h)}"
    elif mi == 20: t = f"twenty past {ad(h)}"
    elif mi == 30: t = f"half past {ad(h)}"
    elif mi == 40: t = f"twenty to {ad(h + 1)}"
    elif mi == 50: t = f"ten to {ad(h + 1)}"
    else: t = f"{ad(h)} {mi:02d}"
    return (t + " " + gun)[0].upper() + (t + " " + gun)[1:]

# ── güneş (45° K · δ 17,6° · güneş öğlesi 12:14) ──────────────────────────
LAT, DEC, NOON = math.radians(45.0), math.radians(17.6), 12 * 60 + 14
BAKIS = 10.0
def gunes(m):
    H = math.radians(15.0 * (m - NOON) / 60.0)
    se = math.sin(LAT) * math.sin(DEC) + math.cos(LAT) * math.cos(DEC) * math.cos(H)
    el = math.degrees(math.asin(se))
    az = math.degrees(math.atan2(math.sin(H), math.cos(H) * math.sin(LAT) - math.tan(DEC) * math.cos(LAT))) + 180.0
    return round(az) % 360, round(el)

def yon(rel):
    rel %= 360
    ana = [(0, "away from the camera"), (90, "to the right"), (180, "towards the camera"), (270, "to the left")]
    def fark(a, b): return min((a - b) % 360, (b - a) % 360)
    s = sorted(ana, key=lambda x: fark(rel, x[0]))
    if fark(rel, s[0][0]) <= 20: return s[0][1]
    return f"{s[0][1]} and slightly {s[1][1]}"

def golge(m):
    az, el = gunes(m)
    uzun = "long" if el < 15 else ("medium-length" if el < 35 else "short")
    return uzun, yon(az + 180 - BAKIS)

def gunes_yeri(m):
    az, el = gunes(m)
    rel = (az - BAKIS + 180) % 360 - 180
    yan = "on the right" if rel > 0 else "on the left"
    on = "ahead of the camera" if abs(rel) < 90 else "behind the camera"
    return f"{yan} and {on}"

# ── gök ───────────────────────────────────────────────────────────────────
def gok(n):
    if n <= 8:  return "a clear pale morning sky with a few small high clouds; the air is clear and the far ridge stands sharp"
    if n <= 26: return "a clear blue sky with a few small white fair-weather clouds; the air is clear"
    if n <= 44: return "a deep blue midday sky with scattered small white clouds; the air is clear"
    if n <= 46: return "a blue sky with white cumulus clouds building over the left part of the far ridge"
    if n == 47: return "a tall dark grey rain cloud rising over the far ridge at the left, the right half of the sky still blue"
    if n == 48: return "a dark grey rain cloud covering the left two thirds of the sky, the light dimmer and cooler, grey streaks of rain over the far slope at the left"
    if n == 49: return "the rain cloud drawing off to the right over the far ridge, blue sky returning from the left, sunlight back on the wet stations"
    if n == 50: return "broken white clouds after rain in a washed blue sky; the air is very clear"
    if n <= 62: return "a clear afternoon sky with a few white clouds; the air is clear"
    if n <= 72: return "a clear late-afternoon sky with a few white clouds, the light turning warmer"
    if n <= 78: return "golden late-afternoon light, a clear sky with a few thin high clouds turning gold"
    if n <= 80: return "low golden evening light, the crest of the far ridge lit warm, a few thin gold clouds"
    if n <= 83: return "soft warm afterlight just after sunset, the sky pale orange low at the left and clear blue above"
    return "deep clear blue hour, the sky deep blue with a last pale warm band low at the left edge and a few still thin clouds"

def gok_hareket(s):
    """I2V gök cümlesi — klibin başındaki saate göre."""
    if rejim(s) == "G":
        return "The few thin clouds stay still in the sky."
    m = SAAT[s]
    uzun, y = golge(m)
    if s == 48:
        return ""
    if s <= 44: bulut = "The small white clouds drift slowly from the left in one smooth flow"
    elif s <= 47: bulut = "The white cumulus clouds over the far ridge swell and drift from the left in one smooth flow"
    elif s <= 62: bulut = "The white clouds drift slowly from the left in one smooth flow"
    elif s <= 78: bulut = "The thin high clouds drift slowly from the left in one smooth flow and turn warmer"
    else: bulut = "The thin clouds drift slowly from the left and the sky deepens"
    if gunes(m)[1] <= 0 or s >= 81:
        return bulut + ", and the shadows soften as the light fades."
    return bulut + f", and the {uzun} shadows lean {y}, turning slowly with the sun."

# ── SABİT BLOKLAR ─────────────────────────────────────────────────────────
KAMERA = ("Camera: MAIN STATION — fixed tripod bolted to a concrete plinth on a rock shelf of the near slope, "
          "lens 6.0 metres above the near station floor, 40 metres from its long face, bearing 10 degrees, "
          "tilt 0 degrees, zero roll. The camera never moves.")
BIBLE = ("When finished this will be a small mountain cableway with two stone stations, one on each side of "
         "a deep valley, and one cabin.")
SITE = ("A deep, narrow mountain valley in grey limestone country. At the left edge of the frame a bare grey "
        "limestone shoulder rises from the bottom edge to above the near station. Across the valley a forested "
        "ridge runs the full width of the frame, its crest at about eighty-six percent of the frame height; the "
        "valley floor lies deep below in shadow, out of view. Near the lower right edge stands a lichen-covered "
        "rock spur, its top at about twenty-eight percent of the frame height. On the rock shelf right of the "
        "near boarding deck stands one small stone bell arch holding one dark cast-iron bell. The valley holds "
        "exactly one cableway and exactly one cabin, this one; no other cabin, tower, chair or line stands "
        "anywhere in view.")
KOMP_SABIT = ("Horizontal 16:9. Eye level sits at exactly half the frame height. The stone bell arch spans about "
              "64 pixels of frame width — one thirtieth — at about 1328 to 1392 pixels from the left, and keeps "
              "that width in every frame. The near station spans about 320 to 1088 pixels from the left, its floor "
              "at about thirty-two percent and its wall heads at about fifty-nine percent of the frame height.")
KOMP_SON = "Nothing that proves progress sits in the bottom tenth of the frame."
NEGATIVE = ("Locked-off camera — it never pans, tilts, zooms or drifts. The limestone shoulder, the far ridge, the "
            "rock spur and the bell arch never change shape, position, size or spacing. The near station keeps its "
            "five arched openings and its stone walls in every frame; there is only ever one cabin; no opacity "
            "fades. No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. "
            "Nothing here has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no "
            "fades. No architectural visualisation look, no CGI aesthetic.")
I2V_AC = ("The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its "
          "last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.")
I2V_SABIT = ("The camera does not move at any point. The framing is identical in the first and last frame. The "
             "limestone shoulder at the left, the forested far ridge, the rock spur at the lower right and the stone "
             "bell arch stay exactly where they are, at exactly the same size and shape, for the whole shot; the bell "
             "arch occupies exactly the same width of the frame in the first and last frame, and eye level stays at "
             "exactly half the frame height. The valley holds exactly one cabin, and no second cabin, tower or line "
             "appears anywhere. The stone walls of both stations are never removed, moved or resized.")
I2V_KAPA = ("Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
            "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
            "documentary time-lapse cinematography.")
FILM_DOKU = "A documentary site photograph on colour negative film, true colour, fine grain."

# ── DEFTERLER: her bileşen (EN cümle, TR not) ─────────────────────────────
def c_cati(n):
    if n == 0: return ("Its old roof of four rusted corrugated panels sags on old steel trusses; the third panel from the left, over the cabin bay, hangs on four slings from the crane hook one metre above the roof line.",
                       "yakın çatı: 4 eski paslı panel; kabin bölmesinin paneli kancada, 1 m havada")
    if n <= 2: return ("Three rusted panels of its old roof remain, with an open gap over the cabin bay.",
                       "yakın çatı: 3 panel kaldı, kabin bölmesinin üstü açık")
    if n == 3: return ("Three rusted roof panels remain; the right-end panel hangs on slings from the crane hook just above the roof line.",
                       "yakın çatı: sağ uç paneli kancada, çatının hemen üstünde")
    if n == 4: return ("Only the left-end rusted roof panel remains, hanging on slings from the crane hook just above the wall heads; the rest of the hall is open to the sky.",
                       "yakın çatı: yalnız sol uç paneli kaldı (kancada)")
    if n <= 27: return ("It stands roofless, its bare wall heads open to the sky.",
                        "yakın çatı: salon tamamen çatısız taş kabuk")
    if n == 28: return ("Two new galvanised steel roof trusses stand on the wall heads at its right end; the third hangs on slings from the crane hook above them.",
                        "yakın çatı: 2 yeni galvaniz makas (sağ uç), 3. makas kancada")
    if n == 29: return ("Five new galvanised steel roof trusses stand evenly on its wall heads, an open skeleton on the old ridge line.",
                        "yakın çatı: 5 makas tamam — iskelet göğe karşı")
    if n == 30: return ("Its five new trusses carry pale yellow timber boarding over the right half of the roof, the left half still open.",
                        "yakın çatı: sağ yarı açık sarı ahşap kaplama")
    if n == 31: return ("Its whole roof is boarded in pale yellow timber over five new trusses.",
                        "yakın çatı: tamamı ahşap")
    if n == 32: return ("Its timber roof is covered in dark grey membrane, the roll seams visible.",
                        "yakın çatı: koyu gri membran")
    if n == 33: return ("The right half of its roof is lead-grey standing-seam zinc, the left half dark grey membrane.",
                        "yakın çatı: sağ yarı dikişli çinko")
    return ("It has a new lead-grey standing-seam zinc roof with a ridge cap, on the old line.",
            "yakın çatı: çinko + mahya tamam")

def c_cephe(n):
    if n <= 2: return ("Thick green ivy covers its face; the arches hold broken glass in rotten frames.",
                       "cephe: tamamen sarmaşıklı, kemerlerde kırık cam")
    if n <= 6: return ("The left half of its face is stripped to stained cream limestone, the right half still thick ivy; the arches hold broken glass.",
                       "cephe: sol yarı sarmaşıksız (krem taş), sağ yarı hâlâ yeşil")
    if n <= 9: return ("Its face is bare grimy limestone, the five arches empty openings.",
                       "cephe: sarmaşık bitti, 5 kemer boş açıklık")
    if n == 10: return ("The left half of its face is washed pale cream, the right half still grey, a sharp boundary at the middle arch.",
                        "cephe: sol yarı yıkandı — ortada dikey sınır")
    if n == 11: return ("Its face is washed pale cream, a few broken blocks missing round the keystones.",
                        "cephe: tamamı temiz krem; kilit taşlarında kırık blok boşlukları")
    if n <= 36: return ("Its face is clean pale cream limestone, the arches repaired with a few paler new blocks and open to the hall inside.",
                        "cephe: 5 kemer onarıldı, yeni taşlar biraz açık")
    if n == 37: return ("Dark bronze window frames fill its five arches, still unglazed.",
                        "cephe: 5 kemerde bronz doğrama, cam yok")
    if n == 38: return ("Its left three arches are glazed in clear glass in bronze frames, the interior visible through it; the right two are open frames.",
                        "cephe: sol 3 kemer camlı (net, şeffaf)")
    return ("Its five arches are glazed in clear glass in bronze frames, the hall interior visible through it.",
            "cephe: 5 kemer camlı")

def c_ic(n):
    if n <= 5: return ("Rubble and rotten timber heap the hall floor.", None)
    if n <= 18: return ("The hall floor is swept bare.", "salon içi: moloz temizlendi" if n == 6 else None)
    if n == 19: return ("The new four-metre steel bullwheel hangs on slings from the crane hook above the open right end of the hall.", "makara tekerleği vinçte, açık çatının üstünde")
    if n >= 39: return ("Through the glass the graphite-grey bullwheel and the machine room show inside.", None)
    if n >= 26: return ("Inside lie the graphite-grey bullwheel, four metres across, its drive boxes and grey cabinets; a steel cage stands over the counterweight shaft at the left end.",
                        "makine dairesinde elektrik panoları" if n == 26 else None)
    s = "Inside at the right end lies the new graphite-grey bullwheel, four metres across, in its steel frame"
    t = "tekerlek yerine oturdu (salonun sağ ucu)" if n == 20 else None
    if n >= 21:
        s += ", the drive boxes beside it"
        if n == 21: t = "tahrik motoru + dişli kutusu yerinde"
    if n >= 25:
        s += "; a steel cage stands over the counterweight shaft at the left end"
        if n == 25: t = "gerdirme kuyusunun üstünde çelik kafes (sol uç)"
    return (s + ".", t)

def c_iskele(n):
    if 9 <= n <= 12: return ("Two scaffold towers stand against its face, one at each side of the middle arch.", "cephe önünde iki iskele kulesi kuruldu" if n == 9 else None)
    if n == 13: return ("", "iskele kuleleri söküldü")
    return ("", None)

def c_merdiven(n):
    if n <= 12: return ("A broken old stone stair climbs to the hall floor right of centre, its steps cracked and tilted.", "merdiven: eski, kırık")
    if n == 13: return ("A wet concrete stair base in timber formwork lies where the old steps stood.", "merdiven: eski basamaklar söküldü, ıslak beton taban")
    if n <= 44: return ("A new stair of pale limestone steps climbs from the yard to the hall floor right of centre.", "merdiven: yeni taş merdiven tamam")
    return ("A new stair of pale limestone steps with dark steel handrails climbs to a pair of tall timber doors.", "merdiven korkulukları + çift kanatlı ahşap kapı")

def c_peron(n):
    if n <= 14: s, t = ("At its right end an old boarding deck juts six metres over the valley on rusted girders, its planks broken.", "biniş tabanı: eski, çürük")
    elif n == 15: s, t = ("At its right end only bare grey cantilever girders jut six metres over the shadowed drop.", "biniş tabanı: çıplak konsol kirişler, döşemesiz — altında boşluk")
    elif n <= 17: s, t = ("At its right end a new wet dark grey concrete deck juts six metres over the valley, a yellow edge barrier along it.", "biniş tabanı: yeni beton döküldü (ıslak koyu gri)" if n == 16 else None)
    elif n == 18: s, t = ("At its right end the new concrete deck juts six metres over the valley under wet curing blankets, a yellow edge barrier along it.", "biniş tabanı: ıslak kür örtüleri altında")
    elif n <= 39: s, t = ("At its right end a pale concrete deck juts six metres over the valley, a yellow edge barrier along it.", "biniş tabanı: kürlendi, açık gri" if n == 19 else None)
    elif n == 40: s, t = ("At its right end the boarding deck is half laid with oiled timber, half pale concrete.", "peron: iç yarısı ahşap")
    else: s, t = ("At its right end a timber boarding deck with a slim steel wire railing juts six metres over the valley.", "peron: ahşap + çelik telli korkuluk" if n == 41 else None)
    if n >= 22:
        s += " A graphite-grey steel headframe, six metres tall on two legs, stands at its outer end."
    if n == 22: t = "biniş tabanı ucunda hat başlığı dikildi"
    return (s, t)

def c_karsi(n):
    b = "Across the valley, about 140 metres away and higher, stands the smaller far stone station with its boarding deck:"
    if n <= 4: s, t = " its old roof caved in, its face grimy.", "karşı istasyon: çökük çatı, kirli"
    elif n <= 7: s, t = " half its caved-in roof lifted away, its face grimy.", "karşı istasyon: çökük çatının yarısı indi"
    elif n <= 16: s, t = " a roofless grimy stone shell.", "karşı istasyon: çatısız taş kabuk"
    elif n == 17: s, t = " a roofless shell, its face washed cream, deck formwork set out.", "karşı cephe yıkandı + biniş tabanı kalıbı"
    elif n <= 22: s, t = " a roofless cream shell with a new concrete deck.", "karşı biniş tabanı döküldü" if n == 18 else None
    elif n == 23: s, t = " a roofless cream shell, its new bullwheel hanging from a small mobile crane just above its walls.", "karşı tekerlek mobil vinçte"
    elif n <= 34: s, t = " a roofless cream shell with its bullwheel inside and a dark steel headframe facing this side.", "karşı tekerlek yerinde + karşı hat başlığı" if n == 24 else None
    elif n == 35: s, t = " new trusses boarded in pale timber, a headframe facing this side.", "karşı çatı: makas + ahşap"
    elif n <= 41: s, t = " a new zinc roof, a headframe facing this side.", "karşı çatı çinko — iki istasyon da çatılı" if n == 36 else None
    else: s, t = " a zinc roof, clear glass, a timber deck and a headframe facing this side.", "karşı istasyon camlı + ahşap peron" if n == 42 else None
    if n == 43:
        s += " On the rock knoll right of it stands the bare steel frame of a viewing terrace."; t = "karşı kayalıkta seyir terası iskeleti"
    if n >= 44:
        s += " On the rock knoll right of it juts a timber viewing terrace with a railing and benches."
        if n == 44: t = "karşı seyir terası tamam"
    return (b + s, t)

def c_halat(n):
    if n < 24: return ("Between the two stations lies the open valley.", None)
    if n <= 45: return ("The two headframes face each other across the open valley with only air between them.", "iki hat başlığı karşı karşıya, arası boş" if n == 24 else None)
    if n == 46: return ("One thin pilot rope spans the valley between the headframes in a long slack curve.", "halat: ince pilot halat (gevşek yay)")
    if n == 47: return ("Two lines span the valley in slack curves: the thin pilot rope and a thicker steel haul rope.", "halat: + daha kalın çekme halatı")
    if n <= 49: return ("The pilot rope and the haul rope hang slack across the valley, and the end of a heavy dark carrying rope, drawn out along them, has passed the middle.",
                        "taşıyıcı halatın ucu vadinin ortasını geçti" if n == 48 else None)
    if n == 50: return ("The first heavy dark carrying rope spans the valley in a slack curve, anchored at both headframes, beside the haul rope.", "1. taşıyıcı halat iki istasyon arasında (gevşek)")
    if n == 51: return ("Two parallel heavy carrying ropes hang in slack curves between the headframes, beside the haul rope.", "2. taşıyıcı halat — iki paralel, gevşek")
    if n == 52: return ("Two heavy carrying ropes run taut and nearly straight from the near headframe up to the far one, the haul rope slack beside them.", "gerdirme: iki taşıyıcı halat gergin, düz")
    s = "Three lines run taut from the near headframe up to the far one: two heavy carrying ropes and a thinner haul rope in a closed loop"
    s += ", grey caps over the saddles." if n >= 54 else "."
    return (s, "çekme halatı tekerleğe sarıldı — 3 halat, hat tamam" if n == 53 else ("halat eyerleri kapatıldı" if n == 54 else None))

def c_kabin(n):
    if n <= 1: return ("Through the arch right of centre the one small cabin, a rusted faded-red box with three broken windows a side, hangs from an old hanger girder inside.",
                       "kabin: salonun içinde, eski askı kirişinde, paslı")
    y = "In the yard left of the stair the one small cabin, a four-metre box with three windows a side, a sliding door and a roof hanger arm, sits on a low steel cradle"
    if n == 2: return (y + ", rusted, its windows broken, four slack slings running up to the crane hook.", "kabin: salondan çıktı, bakım alanında beşikte (sapanlar bağlı)")
    if n <= 8: return (y + ", rusted, its windows broken.", "kabin sapanları çözüldü" if n == 3 else None)
    if n <= 53: return (y + ", rusted, its windows broken, a tarpaulin and a tool chest beside it.", "kabin yanına branda + alet sandığı" if n == 9 else None)
    if n == 54: return (y + ", rusted, inside a new scaffold.", "kabin iskele içinde — yenileme başlıyor")
    if n == 55: return (y + ", stripped inside its scaffold to a bare rusted shell, its glass, door and bench removed.", "kabin: cam, kapı, iç söküldü; her yer pas")
    if n == 56: return (y + ", blasted to bare matt grey steel inside its scaffold.", "kabin: kumlandı — çıplak mat gri çelik")
    if n == 57: return (y + ", in light grey primer over welded patches inside its scaffold.", "kabin: kaynak yamaları + açık gri astar")
    if n == 58: return (y + ", painted deep signal red with a thin cream band below the windows, inside its scaffold, the windows still open.", "kabin: derin kırmızı + ince krem şerit")
    if n == 59: return (y + ", red with a cream band, newly glazed, door closed, a timber bench inside, in its scaffold.", "kabin: yeni camlar, sürgülü kapı, bank")
    if n == 60: return ("In the yard the one small red cabin with its cream band stands on its cradle, a grey hanger arm and four-wheel carriage on its roof held by taut crane slings; the scaffold has gone.",
                        "kabin: askı kolu + makaralı taşıyıcı takıldı; kabin iskelesi söküldü")
    if n == 61: return ("The one small red cabin hangs from the crane hook by its carriage at the outer end of the near deck, one metre below the carrying ropes.", "kabin vinçte: peron ucunda, halatların ≈1 m altında")
    if n == 62: return ("The one small red cabin hangs by its four-wheel carriage from the carrying ropes at the edge of the near deck, the crane slings slack from its carriage.", "kabin halatta asılı; vinç sapanları gevşek")
    on = "The one small red cabin with its cream band hangs by its carriage on the carrying ropes"
    d = {63: (" at the near deck, its door open, two technicians inside.", "kabin peronda, kapı açık, içinde 2 teknisyen"),
         64: (" at the near deck, empty, its door closed, ready to leave.", "kabin boş, kapı kapalı — çıkışa hazır"),
         65: (", empty, about thirty-five metres out over the valley.", "kabin ≈35 m açıkta, boşluğun üstünde"),
         66: (", empty, about seventy metres out over the deepest part of the valley.", "kabin vadinin ortasında (≈70 m)"),
         67: (" at the far deck, a small red box in the distance.", "kabin karşı istasyonda"),
         68: (" back at the near deck, empty, its door closed.", "kabin geri döndü — yakın peronda"),
         69: (" at the near deck, its door closed, filled with blue water-filled test drums.", "kabin içi mavi su bidonlarıyla dolu"),
         70: (", loaded with blue drums and stopped over the middle of the valley, the ropes sagging visibly deeper.", "yüklü kabin vadinin ortasında durdu — halat sarkması derin"),
         71: (" back at the near deck, empty, its door open.", "kabin geri geldi, bidonlar boşaltıldı"),
         84: (" at the near deck, door closed, six small passenger silhouettes in its lit windows.", "6 yolcu kabinde, kapı kapalı"),
         85: (", lit, about fifteen metres out, six silhouettes inside.", "kabin ≈15 m açıkta"),
         86: (", lit, about fifty metres out over the valley, six silhouettes inside.", "kabin ≈50 m'de"),
         87: (", lit, about eighty-five metres out, past the middle, six silhouettes inside.", "kabin ≈85 m'de, vadinin ortasını geçti"),
         88: (" at the far deck, lit, six silhouettes inside, its door closed.", "kabin karşı istasyona vardı"),
         89: (" at the far deck, lit and empty, its door open.", "kabin kapısı açık, yolcular indi"),
         90: (", lit and empty, about ten metres out from the far deck, starting back across the valley.", "boş kabin dönüşe çıktı (≈10 m açıkta)")}
    if n in d: return (on + d[n][0], d[n][1])
    if n <= 79: return (on + " at the near deck, clean and gleaming, its door closed.", "kabin parlak, boş — deneme bitti" if n == 72 else None)
    return (on + " at the near deck, its interior lamp lit, its door closed.", "kabinin iç lambası yandı" if n == 80 else None)

def c_bahce(n):
    if n <= 5: return ("The front yard is overgrown with scrub and long grass.", "bahçe: çalı, uzun ot")
    if n <= 72: return ("The front yard is mown gravel and short grass.", "bahçe biçildi" if n == 6 else None)
    if n == 73: return ("The yard is bare gravel with tyre marks and pale imprints where the site equipment stood.", "bakım alanı boşaldı — araçlar, beşik, konteyner gitti")
    if n == 74: return ("The yard is graded, with raked gravel paths and dug beds of dark soil.", "bahçe tesviye edildi, yataklar kazıldı")
    s = "The yard is a garden of gravel paths, shrubs and two young trees"
    t = "bitkiler + iki genç ağaç" if n == 75 else None
    if n >= 76:
        s += ", a stone water channel running beside the stair into a small pool"
        if n == 76: t = "su kanalı akıyor, havuz dolu"
    if n >= 77:
        s += " and a stone terrace with benches and planters at the stair foot"
        if n == 77: t = "merdiven dibinde taş teras: bank + saksı"
    return (s + ".", t)

def c_isik(n):
    if n <= 77: return ("", None)
    if n <= 79: return ("Lamps on the hall walls, the stair and the deck railing are fitted, all unlit.", "armatürler takıldı — hepsi sönük" if n == 78 else None)
    if n == 80: return ("The near station is lit warm — the hall behind the glass, the deck, the stair and the garden lamps; the far station is unlit.", "yakın istasyon ışıkları yandı")
    return ("Both stations and the far viewing terrace are lit warm.", "karşı istasyon + seyir terası ışıkları yandı" if n == 81 else None)

def c_insan(n):
    if n == 82: return ("Six visitors stand at the foot of the stair, seen from the side and behind; an attendant stands at the open doors.", "6 ziyaretçi merdivenin dibinde, görevli kapıda")
    if n == 83: return ("Six visitors stand on the deck at the cabin door, seen from behind.", "6 ziyaretçi peronda, kabin kapısında")
    if 84 <= n <= 88: return ("Four more visitors sit on the stone terrace benches, seen from behind; the attendant stands on the deck.", "2. grup (4 kişi) taş terasta oturuyor" if n == 84 else None)
    if n == 89: return ("Across the valley six tiny figures walk from the far deck towards the viewing terrace; four visitors sit on the near terrace.", "yolcular karşı seyir terasına yürüyor")
    if n == 90: return ("Across the valley six tiny figures stand at the railing of the viewing terrace; four visitors sit on the near terrace, seen from behind.", "yolcular seyir terasının korkuluğunda")
    return ("", None)

def c_hava(n):
    if n == 49: return ("Every surface is dark and wet after a summer downpour.", "sağanak geçti — her yüzey ıslak")
    if n == 50: return ("", "yüzeyler kurudu")
    return ("", None)

BILESEN = [("yakın çatı", c_cati), ("cephe", c_cephe), ("iskele", c_iskele), ("iç", c_ic), ("merdiven", c_merdiven),
           ("peron", c_peron), ("kabin", c_kabin), ("bahçe", c_bahce), ("ışık", c_isik),
           ("karşı", c_karsi), ("halat", c_halat), ("insan", c_insan), ("hava", c_hava)]

def asama(n):
    gov = ["The near station is a long grey limestone hall with five tall round-arched openings in its long face."]
    for _, f in BILESEN:
        e, _ = f(n)
        if e: gov.append(e)
    return " ".join(gov)

EK_NOT = {47: "gök: batıda kümülüs yükselip kararıyor", 48: "gök: batıdan sağanak bulutu geliyor, ışık kısılıyor",
          73: "ışık: altın saate dönüyor", 79: "şantiye boş — kimse yok, güneş alçak (altın ışık)",
          83: "güneş sırtın ardına iniyor", 84: "güneş battı — art ışık, sonra mavi saat",
          90: "mavi saat; kabin dönüşte, yolcular korkulukta (film hareket hâlinde biter)"}

def degisen(n):
    if n == 0: return ["İlk kare — açılış. Önceki sahne yok."]
    out = []
    for ad, f in BILESEN:
        e0, _ = f(n - 1); e1, t1 = f(n)
        if (e0 != e1 or (e1 == "" and t1)) and t1:
            out.append(t1)
    if n in EK_NOT: out.append(EK_NOT[n])
    v0, v1 = vinc_yuk(n - 1), vinc_yuk(n)
    if v1 is None and v0 is not None: out.append("vinç yok — G63'ten sonra hiçbir karede vinç yok")
    elif v1 and v1[1] and v1 != v0: out.append(f"vinç kancası: {v1[1]}")
    k0, k1 = karsi_vinc(n - 1), karsi_vinc(n)
    if k1 and k1[1] and k1 != k0: out.append("karşı mobil vinç: " + k1[1])
    elif k0 and not k1: out.append("karşı mobil vinç gitti")
    out.append(f"ışık: {hhmm(SAAT[n - 1])} → {hhmm(SAAT[n])}" + (" (G — gerçek zaman, ışık sabit)" if SAAT[n] == SAAT[n - 1] else ""))
    return out

# ── vinç kancası (yakın paletli vinç) G0–G62 ───────────────────────────────
VINC = {
 0: ("a whole rusted roof panel", "panel 1 (kabin bölmesinin paneli)"),
 1: ("the rusted roof panel, now resting on the truck bed and still slung on the hook", "panel 1 kamyon kasasında, sapanlar bağlı"),
 2: ("the cabin's four slings, running slack down to its hanger arm", "kabinin sapanları (gevşek)"),
 3: ("the right-end rusted roof panel", "panel 2 (sağ uç)"),
 4: ("the left-end rusted roof panel", "panel 4 (sol uç)"),
 5: ("a full steel rubble bucket", "moloz kovası"), 6: ("a steel crate of broken glass", "cam kırığı kasası"),
 7: ("a bundle of scaffold tubes", "iskele borusu demeti"), 8: ("a bundle of scaffold tubes", None),
 9: ("a bundle of scaffold boards", "iskele tahtası demeti"), 10: ("a pallet of cut limestone blocks", "kesme taş paleti"),
 11: ("a pallet of cut limestone blocks", None), 12: ("a steel skip of broken stone", "kırık taş kovası (skip)"),
 13: ("a pallet of limestone steps", "taş basamak paleti"), 14: ("a steel skip of broken planks", "çürük tahta kovası"),
 15: ("a bundle of new steel girders", "yeni çelik kiriş demeti"), 16: ("a pallet of rolled curing blankets", "kür örtüsü paleti"),
 17: ("a pallet of rolled curing blankets", None), 18: ("the bullwheel, slung on four slings", "makara tekerleği"),
 19: ("the bullwheel, slung on four slings", None), 20: ("the drive motor, a big dark grey box", "tahrik motoru"),
 21: ("the steel headframe, slung upright", "hat başlığı çerçevesi"), 22: ("a concrete counterweight block", "gerdirme ağırlığı bloğu"),
 23: ("a concrete counterweight block", None), 24: ("a concrete counterweight block", None),
 25: ("a pallet of grey electrical cabinets", "elektrik panosu paleti"), 26: ("a second pallet of electrical cabinets", None),
 27: ("the first galvanised steel roof truss", "makas 1"), 28: ("the third galvanised steel roof truss", "makas 3"),
 29: ("a bundle of timber purlins and boards", "aşık + tahta paketi"), 30: ("a bundle of timber roof boards", "tahta paketi"),
 31: ("a pallet of membrane rolls", "membran rulosu paleti"), 32: ("a bundle of zinc sheet", "çinko paketi"),
 33: ("a bundle of zinc sheet and ridge caps", "çinko + mahya paketi"), 34: ("a crate of bronze window frames", "doğrama sandığı"),
 35: ("a crate of bronze window frames", None), 36: ("a crate of bronze window frames", None),
 37: ("a crate of glass panels", "cam paneli sandığı"), 38: ("a crate of glass panels", None),
 39: ("a pallet of oiled timber planks", "ahşap peron tahtası paleti"), 40: ("a bundle of steel railing posts", "korkuluk dikmesi demeti"),
 41: ("a pallet of steel handrail sections", "merdiven korkuluğu paleti"), 42: ("a pallet of steel handrail sections", None),
 43: ("a pallet of steel handrail sections", None), 44: ("a pallet of timber door leaves", "kapı kanadı paleti"),
 45: ("a big timber cable reel", "büyük ahşap makara"), 46: ("a big timber cable reel", None), 47: ("a big timber reel of carrying rope", "taşıyıcı halat makarası"),
 48: ("a big timber reel of carrying rope", None), 49: ("a big timber reel of carrying rope", None),
 50: ("a second big timber reel of carrying rope", "2. taşıyıcı halat makarası"), 51: ("a crate of grey rope saddle covers", "eyer kapağı sandığı"),
 52: ("a crate of grey rope saddle covers", None), 53: ("a bundle of scaffold tubes", "iskele borusu demeti"),
 54: ("a bundle of scaffold tubes", None), 55: ("a steel skip of old glass and rotten timber", "kabin söküntüsü kovası"),
 56: ("a steel skip of spent blast grit", "kumlama atığı kovası"), 57: ("a pallet of paint tins", "boya teneke paleti"),
 58: ("a crate of glass panes", "kabin camı sandığı"), 59: ("the dark grey hanger arm and its four-wheel carriage", "askı kolu + makaralı taşıyıcı"),
 60: ("the whole cabin, held by its carriage on taut slings", "kabin (gergin)"), 61: ("the whole cabin, held by its carriage on taut slings", "kabin peron ucunda"),
 62: ("the slack slings still shackled to the cabin's carriage", "kabine bağlı gevşek sapanlar"),
}
def vinc_yuk(n): return VINC.get(n)

KVINC = {4: ("a small mobile crane drives up the far service road", "servis yolundan geliyor"),
         5: ("a small mobile crane on the far service road carries a visible load, with a caved-in roof section on its hook", "çatı parçası kaldırıyor"),
         6: ("a small mobile crane on the far service road carries a visible load, with a caved-in roof section on its hook", None),
         7: ("a small mobile crane on the far service road carries a visible load, with a caved-in roof section on its hook", None),
         8: ("a small mobile crane on the far service road carries a visible load, with the last roof section on its hook, lowering it onto a trailer", "son çatı parçasını römorka indiriyor"),
         22: ("a small mobile crane on the far service road carries a visible load, with the far bullwheel on its hook", "karşı tekerleği kaldırıyor"),
         23: ("a small mobile crane on the far service road carries a visible load, with the far bullwheel on its hook", None),
         24: ("a small mobile crane on the far service road carries a visible load, with a bundle of steel on its hook, folding its boom", "işini bitirdi, bomunu topluyor"),
         34: ("a small mobile crane on the far service road carries a visible load, with a far roof truss on its hook", "karşı makasları taşıyor"),
         35: ("a small mobile crane on the far service road carries a visible load, with a bundle of zinc sheet on its hook", "karşı çinko paketi"),
         36: ("a small mobile crane on the far service road carries a visible load, with a bundle of offcuts on its hook, about to leave", "gidiyor"),
         42: ("a small mobile crane on the far service road carries a visible load, with a steel cantilever section on its hook", "seyir terası iskeleti"),
         43: ("a small mobile crane on the far service road carries a visible load, with a pallet of timber decking on its hook", "teras döşemesi"),
         44: ("a small mobile crane on the far service road carries a visible load, with a pallet of benches on its hook", "teras bankları — sonra gider")}
def karsi_vinc(n):
    v = KVINC.get(n)
    return v

# ── kabin px (COMPOSITION) ────────────────────────────────────────────────
def kabin_px(n):
    if n <= 1: return "The cabin shows through the arch at about 849 to 960 pixels from the left, forty to forty-seven percent of the frame height."
    if n <= 60: return "The cabin on its cradle spans about 160 pixels, from about 600 to 760 pixels from the left, twenty-three to thirty-three percent of the frame height."
    yer = {65: 1260, 66: 1375, 67: 1443, 70: 1375, 85: 1210, 86: 1310, 87: 1410, 88: 1443, 89: 1443, 90: 1425}
    if n in yer:
        x = yer[n]
        gen = 110 if x < 1250 else (80 if x < 1330 else (56 if x < 1420 else 37))
        return f"The cabin hangs below the rope line at about {x} pixels from the left, about {gen} pixels wide."
    return "The cabin hangs below the rope line at the end of the near deck, about 1110 to 1220 pixels from the left."

def komp(n):
    p = [KOMP_SABIT, kabin_px(n)]
    if n >= 46: p.append("The rope line runs from about 1164 pixels from the left at half the frame height up to about 1443 pixels at seventy-six percent.")
    elif n >= 22: p.append("The near headframe stands at about 1164 pixels from the left, its top at half the frame height.")
    p.append(KOMP_SON)
    return " ".join(p)

# ── doku ──────────────────────────────────────────────────────────────────
def doku(n):
    if n == 49: d = "Standing puddles on the gravel, dark wet stone, rain streaks drying on the zinc, wet tarpaulins over stacked material, tyre ruts full of water."
    elif n <= 8: d = "Rust streaks on the old panels, dark grime and ivy on the stone, broken glass and rotten timber debris, rubble heaps, fresh tyre marks and mud ruts on the gravel yard."
    elif n <= 17: d = "Grey slurry streaks down the washed stone, stone dust and chips, stacked pallets of cut stone, coiled hoses, concrete spatter, tyre ruts in the gravel, tarpaulins over material."
    elif n <= 26: d = "Deep tyre ruts and crawler prints in the gravel, stacked timber packing and steel offcuts, cable drums, grease stains on the deck, tarpaulins over pallets, stone dust on the wall heads."
    elif n <= 35: d = "Stacked bundles of timber and zinc on pallets, offcuts and sawdust on the wall heads, torn membrane wrappers, tyre ruts in the gravel, tarpaulins over material."
    elif n <= 44: d = "Crates and pallets of glass and timber, sawdust and offcuts on the decks, peeled protective film, tyre ruts in the gravel, tarpaulins over stacked material."
    elif n <= 53: d = "Big timber cable reels in the yard, coiled steel offcuts, grease streaks on the headframes, tyre ruts in the gravel, tarpaulins over stacked material."
    elif n <= 62: d = "Grey blast grit drifted in a band round the scaffold, paint overspray on the tarpaulins, stacked pallets of tins, tyre ruts and crawler prints in the gravel, cable offcuts."
    elif n <= 72: d = "Tyre ruts and crawler prints in the gravel, stacked test drums on pallets, water splashes darkening patches of the deck, grease streaks on the headframe, tarpaulins."
    elif n <= 78: d = "Raked gravel paths, dark damp soil in the new beds, faint tyre prints, stone dust in the stair joints, a sheen of water on the channel steps, patches of grass seed."
    else: d = "Raked gravel paths, dark damp soil in the beds, a sheen of water on the channel steps, faint tyre prints on the gravel, lichen stains on the old stone, a little stone dust in the stair joints."
    return d + " " + FILM_DOKU

# ── fizik ─────────────────────────────────────────────────────────────────
def fizik(n):
    p = []
    if n <= 62: p.append("The crawler crane stands on its crawlers on the gravel yard, its load hanging from the hook on one taut cable.")
    if n <= 1: p.append("The cabin hangs by its roof arm from the old girder, which bears on the hall walls.")
    elif n <= 59: p.append("The cabin sits on its cradle, which rests on timber packing on the gravel.")
    elif n == 60: p.append("The cabin sits on its cradle, the crane slings taut on its carriage.")
    elif n == 61: p.append("The cabin hangs from the crane hook on taut slings shackled to its carriage.")
    else: p.append("The cabin hangs by its carriage on the two carrying ropes, clamped to the haul rope.")
    if n >= 46: p.append("The ropes are anchored at both headframes, each headframe bolted to its deck.")
    p.append("Both stations stand on bedrock, and the near deck bears on steel girders anchored into the rock.")
    if karsi_vinc(n): p.append("The far crane stands on its outriggers on the service road.")
    return " ".join(p)

# ── zaman hızı ────────────────────────────────────────────────────────────
def zaman_hizi(n):
    if rejim(min(n, 89)) == "G" or n == 90:
        return ("Everything in this frame moves at natural speed. Eight seconds pass across this shot: the cabin glides at its real pace, "
                "the water runs and the clouds stay still; nothing is accelerated.")
    ozne = ["clouds", "shadows"]
    if n <= 72: ozne += ["machines", "vehicles"]
    if n >= 76: ozne.append("water")
    if n <= 78: ozne.append("crew")
    elif n >= 81: ozne.append("people")
    lst = ", ".join(ozne[:-1]) + " and " + ozne[-1]
    s = f"Everything in this frame is time-lapsed at the same rate: {lst} all move at the same accelerated speed. Ten minutes pass across this shot"
    return s + ". Nothing moves at normal speed."

def insan_kurali(n):
    if n in (79, 80): return "No people are present."
    if rejim(min(n, 89)) == "G" or n == 90:
        return "Every person is a small silhouette seen from the side or from behind, back to the camera, no readable face anywhere."
    if n >= 81: return "People appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere."
    return "Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, no readable face anywhere."

from sky_data import F, S, PERDELER, USTA

def gorsel(n):
    m = SAAT[n]
    az, el = gunes(m)
    uzun, y = golge(m)
    if el > 0:
        isik = (f"Sun azimuth {az} degrees, elevation {el} degrees, {gunes_yeri(m)}; {uzun} shadows lie {y}. "
                f"High summer in the mountains: {gok(n)}. The sun stays outside the frame.")
    else:
        isik = (f"Sun azimuth {az} degrees, elevation {abs(el)} degrees below the horizon, {gunes_yeri(m)}, so there is no direct sun: "
                f"{gok(n)}. High summer in the mountains. The sun stays outside the frame.")
    iso = "ISO 400" if n >= 79 else "ISO 100"
    act = F[n]["act"]
    v = vinc_yuk(n)
    if v: act += f" The crane carries a visible load, with {v[0]} on the hook."
    k = karsi_vinc(n)
    if k: act += f" Across the valley, small and distant, {k[0]}."
    act += " " + insan_kurali(n)
    bas = (f"Photorealistic documentary site photograph — Scene {n} of 90. " if n < 90 else
           "Photorealistic documentary site photograph — master frame G90, the target frame of the last shot (Scene 89 of 90). ")
    return "\n".join([
        bas + "Horizontal 16:9 time-lapse of a ruined mountain cableway being rebuilt across a deep valley, from a fixed 24 mm site camera.",
        f"Lens: 24 mm spherical, f/8, {iso}.",
        KAMERA, "",
        f"STRUCTURE: {BIBLE} AT THIS STAGE: {asama(n)}", "",
        f"SITE / BACKGROUND: {SITE}", "",
        f"THE TIME MOMENT: {saat_en(m)}: {F[n]['mom']}", "",
        f"COMPOSITION: {komp(n)}", "",
        f"LIGHTING: {isik}", "",
        f"TIME RATE: {zaman_hizi(n)}", "",
        f"ACTIVITY: {act}", "",
        f"SITE TEXTURE: {doku(n)}", "",
        f"PHYSICS: {fizik(n)}", "",
        f"NEGATIVE: {NEGATIVE}",
        "Output: 16:9, 4K, no text, no watermark.",
    ])

def i2v(s):
    d = S[s]
    if rejim(s) == "G":
        bas = "Eight seconds pass in real time. Everything in this shot moves at natural speed."
    else:
        bas = "Ten minutes pass. Everything in this shot is time-lapsed at the same rate."
    akis = " ".join(x for x in [bas, d["flow"], gok_hareket(s)] if x)
    return "\n".join([I2V_AC, "", f"MOTION FOCUS: {d['mf']}", "", akis, "", I2V_SABIT, "", I2V_KAPA])

# ── kelime kilitleri ve yasaklar ──────────────────────────────────────────
YASAK = ["train", "railway", "rail", "track", "tram", "funicular", "chairlift", "ski", "snow", "gondola",
         "station platform", "bridge", "helicopter", "drone", "zipline", "fall", "falling", "snap", "crash",
         "collapse", "fog", "mist", "haze", "smoke", "glow", "bloom", "rays", "beam", "flare", "fireworks",
         "neon", "mirror", "signboard"]
HATA = []
def denetle(etiket, metin, n_kare=None, s_klip=None):
    for w in YASAK:
        m = re.search(rf"\b{re.escape(w)}(s|es)?\b", metin, re.I)
        if m: HATA.append(f"{etiket}: yasak '{m.group(0)}'")
    idx = n_kare if n_kare is not None else s_klip
    kilit = [("crane", None, 62 if n_kare is not None else 62),
             ("rope", 46 if n_kare is not None else 45, None),
             ("rust", None, 55),
             ("red paint", 58 if n_kare is not None else 57, None),
             ("visitor", 82 if n_kare is not None else 81, None),
             ("lamps lit", 80 if n_kare is not None else 79, None)]
    for w, alt, ust in kilit:
        if re.search(rf"\b{w}", metin, re.I):
            if alt is not None and idx < alt: HATA.append(f"{etiket}: kilit '{w}' erken")
            if ust is not None and idx > ust: HATA.append(f"{etiket}: kilit '{w}' geç")

def main():
    assert len(F) == 91 and len(S) == 90
    os.makedirs(KOK, exist_ok=True)
    for (no, klasor, baslik, s0, s1) in PERDELER:
        yol = os.path.join(KOK, klasor)
        os.makedirs(yol, exist_ok=True)
        t0, t1 = s0 * 8.0, (s1 + 1) * 8.0
        sonG = s1 + 1
        out = [f"# 🎬 {FILM} — PERDE {no:02d} · {baslik}  (S{s0}–S{s1} · G{s0} … G{s1}{' + USTA KARE G90' if s1 == 89 else ''} + {s1 - s0 + 1} I2V · {t0:.1f}–{t1:.1f} sn)".replace(".", ","),
               "",
               f"> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler ve defterler `../{FILM}_PLAN.md`'de durur;",
               "> buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek başına çalışır. STRUCTURE (tam hâl), SITE / BACKGROUND,",
               "> NEGATIVE ve I2V'nin DEĞİŞMEYECEKLER paragrafı 181 promptta BİREBİR aynıdır; değişen AT THIS STAGE, THE TIME MOMENT,",
               "> COMPOSITION'ın kabin/halat cümleleri, LIGHTING, TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.",
               ">",
               "> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/sky_gen.py` + `sky_data.py`) [DERS 20].",
               ">",
               f"> ⭐ Zincir: bu perdenin ilk görseli **G{s0}**{' önceki perdenin son I2V’sinin HEDEF karesidir' if s0 else ' filmin açılış karesidir'}; son I2V (S{s1}: G{s1} → G{sonG}) "
               + (f"**G{sonG}**'de biter ve G{sonG} sonraki perdenin ilk görselidir — perde sınırı bir KAREDİR, kesme değil [DERS 52]." if s1 < 89 else "**USTA KARE G90**'da biter (bu dosyanın sonunda)."),
               "> 🇹🇷 Her sahnenin başında: **önceki sahneye göre değişenler** (G(n−1) → G(n), defterlerden otomatik) ve **bu sahnede** ne olduğu.",
               "", "---", ""]
        for s in range(s0, s1 + 1):
            d = S[s]; m0, m1 = SAAT[s], SAAT[s + 1]
            out += [f"## 🎬 SAHNE {s} — {d['title']}", "",
                    "```",
                    f"SÜRE: 8,0 s ({s * 8:.1f}–{(s + 1) * 8:.1f})  ·  #{s + 1:02d}  ·  REJİM: {rejim(s)} ({'gerçek zaman' if rejim(s) == 'G' else '10 dk'})  ·  SAAT: {hhmm(m0)}→{hhmm(m1)}  ·  İSTASYON: MAIN".replace(".", ","),
                    "```", "",
                    f"**🔄 Önceki sahneye göre değişen (G{s - 1} → G{s}):**" if s else "**🔄 Önceki sahneye göre değişen:**", ""]
            out += [f"- {x}" for x in degisen(s)]
            out += ["", f"**▶ Bu sahnede:** {d['ne']}", ""]
            g = gorsel(s); denetle(f"G{s}", g, n_kare=s)
            out += [f"### 📸 GÖRSEL PROMPT (G{s})", "", "```", g, "```", ""]
            v = i2v(s); denetle(f"S{s} I2V", v, s_klip=s)
            out += [f"### 🎥 I2V PROMPT (G{s} → G{s + 1})", "", "```", v, "```", "", "---", ""]
        if s1 == 89:
            g = gorsel(90); denetle("G90", g, n_kare=90)
            out += ["## 🌟 USTA KARE — G90 (SAHNE DEĞİLDİR · son klibin hedefi · kapak kaynağı)", "",
                    "**🔄 Önceki kareye göre değişen (G89 → G90):**", ""]
            out += [f"- {x}" for x in degisen(90)]
            out += ["", USTA, "", "### 📸 USTA KARE PROMPT (G90)", "", "```", g, "```", ""]
        dosya = os.path.join(yol, f"{FILM}_PERDE_{no:02d}.md")
        with open(dosya, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out).rstrip() + "\n")
        print("yazıldı", os.path.relpath(dosya, KOK))
    if HATA:
        print("\n".join(HATA)); sys.exit(1)
    uz = [len(gorsel(n)) for n in range(91)]
    print("görsel uzunluk min/max", min(uz), max(uz), "· I2V max", max(len(i2v(s)) for s in range(90)))

if __name__ == "__main__":
    main()
