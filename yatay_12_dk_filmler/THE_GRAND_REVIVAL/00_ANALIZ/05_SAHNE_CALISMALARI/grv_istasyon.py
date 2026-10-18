# -*- coding: utf-8 -*-
"""THE GRAND REVIVAL — dokuz istasyonun sabit blokları ve oda defterleri.
Plan: ../../THE_GRAND_REVIVAL_PLAN.md §DEĞİŞMEZLER · §DEFTERLER. Ortak bloklar harfi harfine aynı [DERS 20].

px hesabı (yatay 16:9 · 24 mm · tilt 0): x_px = 960 + 1280·x/D (soldan) · y_px = 540 − 1280·(y − h)/D (üstten).
Yüzdeler ALT kenardan: (1080 − y_px) / 1080."""

# ── ortak ──────────────────────────────────────────────────────────────────
BIBLE = ("When finished this will be a single-storey limestone villa of about five hundred square metres, "
         "its high rooms finished in oak, walnut, travertine and bronze.")
# ⭐ ortak çapa cümlesi — A ile yedi iç istasyonun SITE bloğunda BİREBİR (kapı ≥6 kelimelik ortak dizi arar [DERS 10])
TEPELER = ("Far away a line of low dry hills, pale gold and dotted with dark cypress trees, runs level along the "
           "horizon at exactly half the frame height.")
# T istasyonu tepeleri göremez (ev ufku kapatır); A ile ortak dizisi zeytin cümlesidir
ZEYTIN = "Two old olive trees with silver-grey leaves stand"
NEG_BAS = "Locked-off camera — it never pans, tilts, zooms or drifts."
NEG_SON = ("No readable text, letters, digits, numbers or symbols anywhere in the frame, on any surface. Nothing here "
           "has been branded, labelled, numbered or annotated by anyone. No cuts, no dissolves, no fades. No "
           "architectural visualisation look, no CGI aesthetic.")
I2V_AC = ("The scene begins exactly as the provided image. The shot ends exactly on the second provided image: its "
          "last frame is that image, matched frame for frame — same framing, same light, same objects in the same places.")
I2V_KAPA = ("Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.\n"
            "No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic "
            "documentary time-lapse cinematography.")
KADRO = "the two workers in dark blue shirts and grey trousers"
KADRO4 = "four workers in the same dark blue shirts and grey trousers"


def i2v_sabit(capalar, olcu, kabuk):
    return ("The camera does not move at any point. The framing is identical in the first and last frame. "
            f"{capalar} stay exactly where they are, at exactly the same size and shape, for the whole shot; "
            f"{olcu} occupies exactly the same width of the frame in the first and last frame, and eye level stays "
            f"at exactly half the frame height. {kabuk} are never removed, moved or resized.")


# ── dokuz istasyon ─────────────────────────────────────────────────────────
# bakis: kamera yönü (derece) · ic: iç mekân mı · oda: İngilizce ad
IST = {}

IST["A"] = dict(
    ad="ÖN CEPHE", oda="front garden", ic=False, bakis=270,
    kamera=("Camera: MAIN STATION — fixed tripod on the front lawn, lens 1.6 metres above the ground, 26 metres "
            "from the front face of the villa, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves."),
    site=("A wide private garden in dry, warm hill country. The long, low front face of the villa stands across the "
          "middle of the frame, with its round stone entrance arch at the centre and one big window opening at each "
          "side of the arch. A straight path runs from the bottom centre of the frame up to the arch. Right of the "
          "path, on the lawn, stands one round stone birdbath on a short pedestal. " + ZEYTIN + " beyond the left and "
          "right ends of the house. " + TEPELER + " There is exactly one house here, this villa, and no other building "
          "stands anywhere in view."),
    komp=("Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone birdbath spans about 86 "
          "pixels of frame width at about 1397 to 1483 pixels from the left, and keeps that width in every frame. The "
          "front face of the villa spans about 222 to 1698 pixels from the left, its base at about forty-three percent "
          "and its eaves at about sixty-three percent of the frame height; the stone arch spans about 881 to 1039 pixels."),
    neg=(NEG_BAS + " The front face of the villa, its stone arch and two window openings, the two olive trees, the "
         "birdbath and the far hills never change shape, position, size or spacing. There is only ever one house; "
         "no opacity fades. " + NEG_SON),
    sabit=i2v_sabit("The front face of the villa, its stone arch, the two olive trees and the round stone birdbath",
                    "the birdbath", "The stone walls and openings of the villa"),
)

IST["H"] = dict(
    ad="GİRİŞ HOLÜ", oda="entrance hall", ic=True, bakis=90,
    kamera=("Camera: HALL STATION — fixed tripod at the inner end of the entrance hall, lens 1.5 metres above the "
            "floor, 7.0 metres from the front wall, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves."),
    site=("The entrance hall of the villa, six metres wide, with a high flat ceiling. In the middle of the far wall "
          "the front entrance opens in a round stone arch fitted with a walnut double door, and one tall narrow window "
          "stands at each side of the arch; through those windows the front garden shows, the lawn and an olive "
          "tree. The two side walls run plain to the far corners. " + TEPELER + " The hall keeps exactly these "
          "openings: one arch with its door and two narrow windows."),
    komp=("Horizontal 16:9. Eye level sits at exactly half the frame height. The round stone arch of the front "
          "entrance spans about 584 pixels of frame width at about 668 to 1252 pixels from the left, and keeps that "
          "width in every frame. The far wall spans about 411 to 1509 pixels from the left, its floor line at about "
          "twenty-five percent and its ceiling line at about ninety-six percent of the frame height."),
    neg=(NEG_BAS + " The stone arch, the two narrow windows, the corners of the hall and the far hills never change "
         "shape, position, size or spacing. The hall keeps its one arch and two narrow windows; no opacity fades. " + NEG_SON),
    sabit=i2v_sabit("The stone arch, the two narrow windows and the far corners of the hall",
                    "the stone arch", "The walls, the arch and the windows of the hall"),
)

IST["L"] = dict(
    ad="SALON", oda="salon", ic=True, bakis=180,
    kamera=("Camera: SALON STATION — fixed tripod against the north wall of the salon, lens 1.5 metres above the "
            "floor, 8.5 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves."),
    site=("The salon of the villa, ten metres wide and nine deep, with a high flat ceiling. In the middle of the far "
          "wall a wide square opening leads through to the entrance hall; through it the finished hall shows, its pale "
          "travertine floor, its bronze chandelier and its long cream bench. The right wall is a row of three tall "
          "glass doors onto the covered veranda at the back of the house, the garden beyond it; the left wall holds "
          "one big window onto the front garden. " + TEPELER + " The salon keeps exactly these openings: one wide "
          "opening to the hall, three glass doors and one big window."),
    komp=("Horizontal 16:9. Eye level sits at exactly half the frame height. The wide opening to the hall spans "
          "about 542 pixels of frame width at about 689 to 1231 pixels from the left, and keeps that width in every "
          "frame. The far wall spans about 207 to 1713 pixels from the left, its floor line at about twenty-nine "
          "percent and its ceiling line at about ninety-two percent of the frame height."),
    neg=(NEG_BAS + " The wide opening, the three glass doors, the big window, the corners of the room and the far "
         "hills never change shape, position, size or spacing. The salon keeps its one opening, three glass doors "
         "and one window; no opacity fades. " + NEG_SON),
    sabit=i2v_sabit("The wide opening to the hall, the three glass doors, the big window and the far corners of the room",
                    "the wide opening", "The walls, the opening, the glass doors and the window of the salon"),
)

IST["D"] = dict(
    ad="YEMEK ODASI", oda="dining room", ic=True, bakis=270,
    kamera=("Camera: DINING STATION — fixed tripod against the east wall of the dining room, lens 1.5 metres above "
            "the floor, 8.5 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves."),
    site=("The dining room of the villa, nine metres long and six wide, with a high flat ceiling. The far wall is "
          "three tall glass doors side by side onto the covered veranda at the back of the house, the garden beyond "
          "it. The left wall holds two tall windows onto the side garden, and near its far end a wide doorway leads "
          "through to the kitchen. The right wall runs plain from end to end. " + TEPELER + " The dining room keeps "
          "exactly these openings: three glass doors, two tall windows and one kitchen doorway."),
    komp=("Horizontal 16:9. Eye level sits at exactly half the frame height. The three glass doors in the far wall "
          "span about 918 pixels of frame width at about 501 to 1419 pixels from the left, and keep that width in "
          "every frame. Their floor line sits at about twenty-nine percent and their tops at about seventy-one "
          "percent of the frame height."),
    neg=(NEG_BAS + " The three glass doors, the two tall windows, the kitchen doorway, the corners of the room and "
         "the far hills never change shape, position, size or spacing. The dining room keeps its three glass doors, "
         "two windows and one doorway; no opacity fades. " + NEG_SON),
    sabit=i2v_sabit("The three glass doors, the two tall windows, the kitchen doorway and the far corners of the room",
                    "the row of three glass doors", "The walls, the glass doors, the windows and the doorway of the dining room"),
)

IST["K"] = dict(
    ad="MUTFAK", oda="kitchen", ic=True, bakis=0,
    kamera=("Camera: KITCHEN STATION — fixed tripod against the south wall of the kitchen, lens 1.5 metres above "
            "the floor, 7.3 metres from the north wall, bearing 0 degrees, tilt 0 degrees, zero roll. The camera never moves."),
    site=("The kitchen of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of the "
          "far wall a glazed service door opens to the side garden; in the right part of the far wall a wide doorway "
          "leads through to the dining room, and through it the finished dining room shows, the walnut table and its "
          "chairs under the bronze chandelier. The left wall holds one wide window above the line of the worktop, onto "
          "the side garden; the right wall runs plain, with one tall niche for a refrigerator. " + TEPELER + " The "
          "kitchen keeps exactly these openings: one service door, one dining-room doorway and one wide window."),
    komp=("Horizontal 16:9. Eye level sits at exactly half the frame height. The wide doorway to the dining room "
          "spans about 420 pixels of frame width at about 1031 to 1451 pixels from the left, and keeps that width in "
          "every frame. The far wall spans about 302 to 1618 pixels from the left, its floor line at about twenty-six "
          "percent and its ceiling line at about eighty-seven percent of the frame height; the service door spans "
          "about 329 to 504 pixels."),
    neg=(NEG_BAS + " The service door, the dining-room doorway, the wide window, the refrigerator niche, the corners "
         "of the room and the far hills never change shape, position, size or spacing. The kitchen keeps its one "
         "service door, one doorway and one window; no opacity fades. " + NEG_SON),
    sabit=i2v_sabit("The service door, the dining-room doorway, the wide window and the far corners of the kitchen",
                    "the dining-room doorway", "The walls, the doors and the window of the kitchen"),
)

IST["M"] = dict(
    ad="YATAK ODASI", oda="main bedroom", ic=True, bakis=180,
    kamera=("Camera: BEDROOM STATION — fixed tripod against the north wall of the main bedroom, lens 1.5 metres "
            "above the floor, 8.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves."),
    site=("The main bedroom of the villa, seven and a half metres wide, with a high flat ceiling. At the left end of "
          "the far wall a single walnut door opens from the private corridor; the rest of the far wall is plain. The "
          "right wall holds one tall window onto the back garden. The left wall holds a wide doorway through to the "
          "dressing room. " + TEPELER + " The bedroom keeps exactly these openings: one corridor door, one tall window "
          "and one dressing-room doorway."),
    komp=("Horizontal 16:9. Eye level sits at exactly half the frame height. The corridor door at the left end of "
          "the far wall spans about 192 pixels of frame width at about 400 to 592 pixels from the left, and keeps that "
          "width in every frame. The far wall spans about 352 to 1568 pixels from the left, its floor line at about "
          "twenty-eight percent and its ceiling line at about eighty-seven percent of the frame height."),
    neg=(NEG_BAS + " The corridor door, the tall window, the dressing-room doorway, the corners of the room and the "
         "far hills never change shape, position, size or spacing. The bedroom keeps its one door, one window and "
         "one doorway; no opacity fades. " + NEG_SON),
    sabit=i2v_sabit("The corridor door, the tall window, the dressing-room doorway and the far corners of the room",
                    "the corridor door", "The walls, the door, the window and the doorway of the bedroom"),
)

IST["W"] = dict(
    ad="GİYİNME ODASI", oda="dressing room", ic=True, bakis=270,
    kamera=("Camera: DRESSING STATION — fixed tripod against the east wall of the dressing room, lens 1.5 metres "
            "above the floor, 8.2 metres from the west wall, bearing 270 degrees, tilt 0 degrees, zero roll. The camera never moves."),
    site=("The dressing room of the villa, a long room four and a half metres wide with a flat ceiling. In the middle "
          "of the far wall a doorway leads through to the main bedroom; through it the finished bedroom shows, and "
          "straight ahead its tall window onto the back garden. High in the left wall runs one long strip window "
          "onto the sky. The two long side walls are where the wardrobes stand. " + TEPELER + " The dressing room "
          "keeps exactly these openings: one bedroom doorway and one high strip window."),
    komp=("Horizontal 16:9. Eye level sits at exactly half the frame height. The bedroom doorway spans about 250 "
          "pixels of frame width at about 835 to 1085 pixels from the left, and keeps that width in every frame. The "
          "far wall spans about 601 to 1319 pixels from the left, its floor line at about twenty-eight percent and "
          "its ceiling line at about seventy-seven percent of the frame height."),
    neg=(NEG_BAS + " The bedroom doorway, the high strip window, the corners of the room and the far hills never "
         "change shape, position, size or spacing. The dressing room keeps its one doorway and one strip window; "
         "no opacity fades. " + NEG_SON),
    sabit=i2v_sabit("The bedroom doorway, the high strip window and the far corners of the room",
                    "the bedroom doorway", "The walls, the doorway and the window of the dressing room"),
)

IST["B"] = dict(
    ad="BANYO", oda="main bathroom", ic=True, bakis=180,
    kamera=("Camera: BATH STATION — fixed tripod against the north wall of the main bathroom, lens 1.5 metres above "
            "the floor, 6.0 metres from the south wall, bearing 180 degrees, tilt 0 degrees, zero roll. The camera never moves."),
    site=("The main bathroom of the villa, six metres square, with a flat ceiling. In the middle of the far wall one "
          "wide window looks onto the garden. In the left wall a tall open shower niche is set into the wall. Near the "
          "far end of the right wall a doorway leads through to the dressing room, and through it the finished "
          "dressing room shows. " + TEPELER + " The bathroom keeps exactly these openings: one wide window, one "
          "shower niche and one doorway."),
    komp=("Horizontal 16:9. Eye level sits at exactly half the frame height. The window in the far wall spans about "
          "512 pixels of frame width at about 704 to 1216 pixels from the left, and keeps that width in every frame. "
          "Its sill sits at about thirty-eight percent and its head at about eighty-two percent of the frame height."),
    neg=(NEG_BAS + " The wide window, the shower niche, the doorway, the corners of the room and the far hills never "
         "change shape, position, size or spacing. The bathroom keeps its one window, one niche and one doorway; "
         "no opacity fades. " + NEG_SON),
    sabit=i2v_sabit("The wide window, the shower niche, the doorway and the far corners of the bathroom",
                    "the window", "The walls, the window, the niche and the doorway of the bathroom"),
)

IST["T"] = dict(
    ad="VERANDA", oda="back garden", ic=False, bakis=90,
    kamera=("Camera: VERANDA STATION — fixed tripod on the back lawn, lens 1.6 metres above the ground, 12 metres "
            "from the back wall of the villa, bearing 90 degrees, tilt 0 degrees, zero roll. The camera never moves."),
    site=("The back of the villa seen from its garden. A covered veranda, twelve metres wide and five deep, runs along "
          "the back wall under a flat timber roof carried on four square stone columns at its outer edge, with one "
          "low stone step along the outer edge of its floor. In the back wall, left of centre, three tall glass doors "
          "open into the salon; right of centre, three tall glass doors open into the dining room; through them the "
          "finished salon and dining room show. " + ZEYTIN + " at the left and right edges of the frame, and the back "
          "lawn runs from the bottom of the frame to the step. There is exactly one house here, this villa."),
    komp=("Horizontal 16:9. Eye level sits at exactly half the frame height. The second stone column from the left "
          "spans about 64 pixels of frame width at about 654 to 718 pixels from the left, and keeps that width in "
          "every frame. The back wall of the villa spans the full frame width; the outer edge of the veranda floor "
          "sits at about thirty-one percent and the edge of the veranda roof at about eighty percent of the frame height."),
    neg=(NEG_BAS + " The back wall, the six glass doors, the four stone columns, the veranda roof and the two olive "
         "trees never change shape, position, size or spacing. There is only ever one house; no opacity fades. " + NEG_SON),
    sabit=i2v_sabit("The back wall, the six glass doors, the four stone columns and the two olive trees",
                    "the second stone column", "The walls, the columns and the veranda roof"),
)

# ── oda defterleri: anahtar → [(k_from, cümle)] · k = segmentin yerel kare no ──
DEFTER = {}

DEFTER["A"] = [
    ("yuk", [(0, "The big old sofa is half out of the open door, held between the two workers.", "="),
             (1, "The big old sofa sits lashed on the low flat cart at the left of the path.", "=")]),
    ("cati", [(0, "The villa's low hipped roof of old clay tiles is broken in patches, a dark hole gaping left of the ridge."),
              (4, "The villa's old tiles are stripped from the whole roof: grey underlay and timber battens lie bare along the same low slope."),
              (5, "New dark anthracite roof panels cover the whole roof along the same low slope.")]),
    ("tas", [(0, "The villa's limestone walls are dark grey with old grime."),
             (3, "The villa's limestone walls are washed back to a clean pale beige.")]),
    ("sarmasik", [(0, "Thick old ivy hangs in a curtain over the stone arch and across both window openings."),
                  (2, "The stone arch and both window openings stand clear of ivy.")]),
    ("sol", [(0, "The big window opening left of the arch holds a rotten old frame with cracked panes."),
             (6, "The big window left of the arch is a new glazed unit in a slim bronze frame.")]),
    ("sag", [(0, "The big window opening right of the arch holds a rotten old frame with cracked panes."),
             (7, "The big window right of the arch is a new glazed unit in a slim bronze frame, matching the left one.")]),
    ("kapi", [(0, "The arch holds a sagging old door, both leaves open."),
              (8, "A tall new walnut double door fills the stone arch, both leaves closed.")]),
    ("yol", [(0, "The front path is cracked old concrete with weeds in the joints."),
             (9, "The front path is laid with large pale flagstones, low bronze path lights along both edges.")]),
    ("yatak", [(0, "Two overgrown planting beds flank the path."),
               (10, "The two planting beds beside the path are dug, edged and planted with low lavender and young box.")]),
    ("gecici", [(0, "A low flat cart stands at the left of the path."),
                (1, "A folded aluminium stepladder leans on the wall right of the arch, and a low flat cart stands at the left of the path."),
                (3, "A scaffold tower stands against the wall at the right end, and a low flat cart stands on the path."),
                (6, "Lifting slings hang loose from the new window frame, and a low flat cart stands on the path."),
                (8, "A stepladder leans on the wall and a low flat cart stands on the lawn beside a stack of pale flagstones on a pallet."),
                (9, "A stepladder leans on the wall and a low flat cart stands beside a heap of dark soil and trays of young plants."),
                (10, "A folded stepladder leans on the wall beside the arch.")]),
]

DEFTER["H"] = [
    ("enkaz", [(0, "A broken old console table, heaps of fallen plaster and dry leaves lie across the floor."),
               (1, "The floor is swept clear."), (3, "")]),
    ("duvar", [(0, "The walls are cracked and stained, the plaster fallen away in patches."),
               (2, "The walls are freshly patched with grey-white plaster, still unpainted."),
               (4, "The walls are painted a warm off-white.")]),
    ("zemin", [(0, "The floor is bare grey screed with old stains."),
               (3, "The floor is laid with large pale travertine tiles.")]),
    ("isik", [(0, "A short bare chain hangs from the ceiling over the middle of the hall."),
              (5, "A large bronze chandelier hangs from the ceiling over the middle of the hall on a short chain, unlit.")]),
    ("konsol", [(0, "The left wall stands bare."),
                (6, "A three-metre travertine console stands against the far part of the left wall, one tall ceramic vase on it.")]),
    ("bank", [(0, "The right wall stands bare."),
              (7, "A long upholstered cream bench stands against the far part of the right wall, and a large framed painting hangs above the console.")]),
    ("kapi", [(0, "Both leaves of the walnut door stand open to the bright garden."),
              (7, "Both leaves of the walnut door are closed.")]),
    ("gecici", [(0, "A low flat cart waits just inside the door."),
                (1, "A folded aluminium stepladder stands by the right wall, a low flat cart inside the door."),
                (3, "A roll of grey protective membrane lies along the wall, a stepladder beside it."),
                (4, "Grey protective membrane covers the travertine, a stepladder stands under the bare chain."),
                (5, "Grey protective membrane runs along the walking line on the travertine, a low flat cart inside the door."),
                (7, "A strip of grey protective membrane lies rolled up by the door, a folded stepladder against it.")]),
]

DEFTER["L"] = [
    ("enkaz", [(0, "An old torn sofa, a broken armchair and heaps of debris stand on the floor."),
               (1, "The room is empty and swept."), (6, "")]),
    ("duvar", [(0, "The walls are scuffed grey-white and stained."),
               (2, "The walls are painted a warm ivory.")]),
    ("zemin", [(0, "The floor is bare grey screed."),
               (3, "The floor is laid with wide pale oak boards running away from the camera.")]),
    ("panel", [(0, "The far wall left of the opening is plain plaster."),
               (4, "Dark walnut panelling covers the far wall left of the opening.")]),
    ("isik", [(0, "A bare round ceiling rose marks the middle of the ceiling."),
              (5, "A ring-shaped bronze ceiling light hangs over the middle of the room on three short chains, unlit.")]),
    ("hali", [(6, "A large cream rug lies in the middle of the floor.")]),
    ("kanepe", [(7, "A long four-seat cream sofa stands along the left edge of the rug."),
                (8, "Two big cream sofas face each other along the left and right edges of the rug, a wide walkway between them.")]),
    ("berjer", [(9, "Two cognac leather armchairs stand at the far corners of the rug, one at each side, leaving the way to the opening clear.")]),
    ("sehpa", [(10, "A big low stone coffee table stands in the middle of the rug on four short square feet, touching neither sofa.")]),
    ("konsol", [(11, "A long low walnut console stands against the walnut panelling.")]),
    ("yan", [(12, "Two small round walnut side tables stand at the near ends of the two sofas.")]),
    ("lamba", [(13, "A tall bronze floor lamp stands beside the right sofa, and one young olive tree in a big stone pot stands by the glass doors.")]),
    ("veranda", [(0, "Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves.")]),
    ("bekleyen", [(9, "The big stone coffee table waits on a low flat cart just inside the opening.", "=")]),
    ("gecici", [(0, "A low flat cart stands in the opening."),
                (1, "A stepladder stands in the middle of the room, a low flat cart in the opening."),
                (3, "A trestle workbench with offcuts stands by the far wall, a low flat cart in the opening."),
                (5, "A stepladder stands under the ceiling light, grey protective membrane along the walking line."),
                (6, "Grey protective membrane runs from the opening along the walking line, a low flat cart in the opening."),
                (13, "A strip of grey protective membrane lies rolled up in the opening, a folded stepladder beside it.")]),
]

DEFTER["D"] = [
    ("enkaz", [(0, "An old dark dining table, three broken chairs and heaps of debris stand on the floor."),
               (1, "The room is empty and swept."), (4, "")]),
    ("duvar", [(0, "The walls are stained grey-white."),
               (2, "The walls are painted a warm greige.")]),
    ("zemin", [(0, "The floor is bare grey screed."),
               (3, "The floor is laid with large matt pale stone tiles.")]),
    ("isik", [(0, "A bare ceiling hook marks the middle of the ceiling."),
              (4, "A long linear bronze chandelier hangs low over the middle of the room on two chains, its length along the room, unlit.")]),
    ("masa", [(5, "A long walnut dining table for ten stands under the chandelier, its length pointing at the camera.")]),
    ("sandalye", [(6, "Two upholstered dining chairs stand at the table, one at each end."),
                  (9, "Six upholstered dining chairs stand at the table: one at each end and four along the left side."),
                  (11, "Ten upholstered dining chairs stand at the table: one at each end and four along each side.")]),
    ("bufe", [(7, "A long low walnut sideboard stands against the right wall.")]),
    ("dolap", [(8, "A tall walnut display cabinet with clear glass doors stands against the right wall beyond the sideboard.")]),
    ("perde", [(10, "Floor-length linen curtains hang at the two tall windows in the left wall.")]),
    ("tablo", [(12, "A large framed painting hangs above the sideboard, and one low flower arrangement stands in the middle of the table.")]),
    ("mutfak", [(0, "Through the kitchen doorway the old kitchen shows, stripped and dim.")]),
    ("veranda", [(0, "Through the glass doors the old veranda shows: cracked concrete, weeds and heaped dry leaves.")]),
    ("bekleyen", [(4, "The long walnut table waits on a low flat cart just inside the middle glass door.", "=")]),
    ("gecici", [(0, "A low flat cart stands outside the open middle glass door."),
                (1, "A folded stepladder stands by the left wall, a low flat cart at the glass doors."),
                (3, "Grey protective membrane covers the new stone floor, a stepladder under the bare hook."),
                (5, "Grey protective membrane runs from the glass doors along the walking line, lifting slings coiled on it."),
                (6, "Grey protective membrane runs from the glass doors along the walking line, a low flat cart at the doors."),
                (12, "A strip of grey protective membrane lies rolled up by the glass doors, a folded stepladder beside it.")]),
]

DEFTER["K"] = [
    ("eski", [(0, "Old broken base cabinets and a cracked worktop line the left wall under the window."),
              (1, "The left wall stands stripped bare to its old pipe stubs."), (5, "")]),
    ("duvar", [(0, "The walls are stained and cracked."),
               (2, "The walls are patched and painted a soft cream.")]),
    ("zemin", [(0, "The floor is bare grey screed."),
               (3, "The floor is laid with large matt grey-beige stone tiles.")]),
    ("kiler", [(4, "A bank of tall walnut pantry cabinets fills the far wall between the service door and the doorway.")]),
    ("alt", [(5, "A run of cream base cabinets with a pale stone worktop lines the left wall under the window.")]),
    ("ada", [(6, "A long walnut island body stands in the middle of the floor, its top bare."),
             (7, "A long walnut island stands in the middle of the floor under a thick pale stone top with a square edge.")]),
    ("panel", [(8, "Pale stone panels cover the wall between the worktop and the window.")]),
    ("buzdolabi", [(9, "A tall built-in refrigerator with plain cream panel doors stands in the niche in the right wall.")]),
    ("firin", [(10, "A double wall oven with a plain dark front sits in a tall cabinet beside the refrigerator.")]),
    ("tabure", [(11, "Two walnut bar stools stand at the near side of the island."),
                (12, "Four walnut bar stools stand in a row at the near side of the island, and one coffee machine stands on the worktop.")]),
    ("bekleyen", [(6, "The thick pale stone top lies flat on a padded board on a low flat cart beside the island, lifting slings under it.", "=")]),
    ("gecici", [(0, "A low flat cart stands at the service door."),
                (1, "A trestle workbench and a stepladder stand by the right wall, a low flat cart at the service door."),
                (3, "Grey protective membrane covers the new stone floor, a stepladder by the right wall."),
                (6, "Grey protective membrane runs from the service door along the walking line, lifting slings coiled on it."),
                (8, "Grey protective membrane runs from the service door along the walking line, a low flat cart at the door."),
                (12, "A strip of grey protective membrane lies rolled up by the service door, a folded stepladder beside it.")]),
]

DEFTER["M"] = [
    ("enkaz", [(0, "An old iron bed frame with a sagging mattress stands against the far wall, debris around it."),
               (1, "The room is empty and swept."), (4, "")]),
    ("duvar", [(0, "The walls are cracked and stained."),
               (2, "The walls are smoothed and painted a calm warm greige.")]),
    ("zemin", [(0, "The floor is bare grey screed."),
               (3, "The floor is laid with pale oak boards running away from the camera.")]),
    ("baslik", [(4, "A wide upholstered greige headboard panel covers the middle of the far wall.")]),
    ("perde", [(5, "Floor-length linen curtains hang at the tall window in the right wall.")]),
    ("hali", [(6, "A large soft grey rug lies in front of the headboard.")]),
    ("yatak", [(7, "A king-size bed base stands centred on the headboard."),
               (8, "A king-size bed stands centred on the headboard, made up with a thick mattress, white linen and pillows.")]),
    ("komodin", [(9, "A walnut bedside table with one small lamp stands at each side of the bed — two tables and two lamps.")]),
    ("bank", [(10, "A long upholstered bench stands across the foot of the bed.")]),
    ("sezlong", [(11, "A large cream chaise longue stands by the window in the right wall.")]),
    ("makyaj", [(12, "A slim walnut dressing table with one small upholstered stool stands against the left wall beyond the doorway.")]),
    ("giyinme", [(0, "Through the doorway in the left wall the old dressing room shows, its sagging shelves dim.")]),
    ("bekleyen", [(6, "The king-size bed base lies flat on a low flat cart just inside the corridor door.", "=")]),
    ("gecici", [(0, "A low flat cart stands just inside the corridor door."),
                (1, "A folded stepladder stands by the right wall, a low flat cart inside the corridor door."),
                (3, "A trestle workbench with offcuts stands by the left wall, grey protective membrane rolled beside it."),
                (4, "Grey protective membrane runs from the corridor door along the walking line, a stepladder by the far wall."),
                (6, "Grey protective membrane runs from the corridor door along the walking line, lifting slings coiled on it."),
                (8, "Grey protective membrane runs from the corridor door along the walking line, a low flat cart at the door."),
                (12, "A strip of grey protective membrane lies rolled up by the corridor door, a folded stepladder beside it.")]),
]

DEFTER["W"] = [
    ("raf", [(0, "Sagging old open shelves and loose boards line both long walls."),
             (1, "Both long walls stand bare."), (4, "The right long wall stands bare."), (5, "")]),
    ("duvar", [(0, "The walls are stained grey-white."),
               (2, "The walls are painted a pale warm white.")]),
    ("zemin", [(0, "The floor is bare grey screed."),
               (3, "The floor is laid with pale oak boards.")]),
    ("sol", [(4, "A full wall of tall walnut wardrobe units lines the left wall, its doors closed.")]),
    ("sag", [(5, "A matching wall of tall walnut wardrobe units with plain walnut doors lines the right wall.")]),
    ("ada", [(6, "A long low walnut island with drawers stands in the middle of the floor, an equal walkway at each side.")]),
    ("bank", [(7, "A long upholstered bench stands at the near end of the island, and folded clothes and plain linen boxes sit on the open shelves at the ends of the wardrobes.")]),
    ("gecici", [(0, "A low flat cart stands in the bedroom doorway."),
                (1, "A folded stepladder stands by the right wall, a low flat cart in the doorway."),
                (3, "A trestle workbench with offcuts stands by the far wall, grey protective membrane rolled beside it."),
                (4, "Grey protective membrane runs from the doorway along the middle, a stepladder by the far wall."),
                (7, "A strip of grey protective membrane lies rolled up in the doorway, a folded stepladder beside it.")]),
]

DEFTER["B"] = [
    ("moloz", [(0, "Broken old tiles and rubble lie heaped on the floor."),
               (1, "The floor is cleared and swept."), (3, "")]),
    ("duvar", [(0, "The walls are bare grey plaster with old stains."),
               (2, "Large pale stone slabs with soft grey veins clad the walls up to the ceiling.")]),
    ("zemin", [(0, "The floor is bare grey screed."),
               (3, "The floor is laid with matt pale stone tiles.")]),
    ("lavabo", [(4, "A long walnut vanity with two basins in one stone top stands against the right wall, two bronze wall lights above it.")]),
    ("kuvet", [(5, "A freestanding white oval bathtub stands in front of the window.")]),
    ("batarya", [(6, "A slim floor-standing bronze tap stands beside the bathtub.")]),
    ("bank", [(7, "An upholstered bench stands against the left wall beside the shower niche, folded white towels on it.")]),
    ("bekleyen", [(4, "The freestanding white bathtub waits on a low flat cart just inside the doorway.", "=")]),
    ("gecici", [(0, "A low flat cart stands in the doorway."),
                (1, "A folded stepladder stands by the left wall, a low flat cart in the doorway."),
                (2, "A trestle workbench with stone offcuts stands by the left wall, a stepladder beside it."),
                (3, "Grey protective membrane covers the new floor, a stepladder by the left wall."),
                (4, "Grey protective membrane runs from the doorway to the window, lifting slings coiled on it."),
                (6, "Grey protective membrane runs from the doorway to the window, a low flat cart in the doorway."),
                (7, "A strip of grey protective membrane lies rolled up in the doorway, a folded stepladder beside it.")]),
]

DEFTER["T"] = [
    ("zemin", [(0, "The veranda floor is cracked old concrete with weeds in the joints and dry leaves heaped against the back wall."),
               (1, "The veranda floor is laid with warm brown timber decking boards.")]),
    ("cim", [(0, "The back lawn is long dry grass, and the low stone step along the veranda edge is chipped and stained."),
             (1, "The back lawn is cut short, and the low stone step along the veranda edge is scrubbed clean.")]),
    ("kanepe", [(2, "A big outdoor sofa of grey cushioned modules stands in the middle of the veranda, facing the garden.")]),
    ("koltuk", [(3, "Two wide outdoor armchairs face the sofa.")]),
    ("sehpa", [(4, "A big low outdoor table stands between the sofa and the armchairs.")]),
    ("bank", [(5, "A long timber bench stands against the back wall at the right.")]),
    ("saksi", [(6, "Two big stone planters with olive shrubs stand at the outer edge, and the wall lights on the back wall are lit.")]),
    ("gecici", [(0, "A low flat cart stands on the lawn at the left."),
                (1, "A trestle workbench with offcuts stands at the left end, a low flat cart on the lawn."),
                (2, "A strip of grey protective membrane lies along the new boards, a low flat cart on the lawn."),
                (6, "A folded stepladder leans on the back wall at the left end.")]),
]

# Segment uzunlukları (klip sayısı) — kontrol için
SEG_UZ = {"A": 10, "H": 7, "L": 13, "D": 12, "K": 12, "M": 12, "W": 7, "B": 7, "T": 6}


def durum(oda, k, degis=None, ek=None):
    """Oda defterinden yerel kare k'nin AT THIS STAGE gövdesi. degis: anahtar → cümle (ya da None = çıkar)."""
    parcalar = []
    for anahtar, satirlar in DEFTER[oda]:
        if degis and anahtar in degis:
            if degis[anahtar]:
                parcalar.append(degis[anahtar])
            continue
        # (k, cümle) k'dan itibaren geçerli · (k, cümle, "=") YALNIZ o karede (geç teslimat, eldeki yük)
        gecerli = [x[1] for x in satirlar if (x[0] == k if len(x) > 2 else x[0] <= k)]
        if gecerli and gecerli[-1]:          # "" = bu kareden sonra cümle düşer
            parcalar.append(gecerli[-1])
    if ek:
        parcalar += ek
    return " ".join(parcalar)


# ── doku ───────────────────────────────────────────────────────────────────
DOKU = {
    "ic_harabe": ("Dust lying grey over everything, damp stains and grime streaks on the walls, cracked plaster, dead "
                  "leaves in drifts in the corners, debris heaped along the skirting."),
    "ic_is": ("Plaster dust in a pale band along the skirting, paint spatter on the protective membrane, offcuts and a "
              "stack of empty tins, faint shoe prints in the dust, a tarpaulin over the stored material."),
    "ic_doseme": ("A thin film of dust along the skirting, faint shoe prints on the grey protective membrane, flattened "
                  "cardboard offcuts in a stack by the door, strips of packing tape, a patch of light on the floor."),
    "ic_bitti": ("A soft sheen on the new floor, a last faint band of dust along one skirting, faint shoe prints near the "
                 "door, a folded stack of dust sheets, one small offcut forgotten by the wall."),
    "ic_yasam": ("A soft sheen on the new floor, a faint gloss on the polished walnut, the fresh creases of new "
                 "upholstery, faint fingerprints on the bronze door handles, a patch of warm lamplight on the floor, "
                 "every surface free of dust."),
    "dis_harabe": ("Moss and grime streaks on the stone, rust stains under the old window frames, cracked concrete with "
                   "weeds, dead leaves in drifts against the wall, broken tile debris on the lawn."),
    "dis_is": ("Grey slurry streaks drying down the washed stone, broken tile debris in a band along the wall foot, a "
               "stack of material on a pallet, wheel tracks and shoe prints in the damp grass, a tarpaulin over a heap of soil."),
    "dis_bitti": ("Fresh dark soil in the beds, a faint sheen of water on the new stone, light wheel tracks in the grass, a "
                  "little stone dust in the path joints, lichen stains on the old garden stones, a patch of worn grass."),
    "ver_harabe": ("Cracked concrete, weeds and dead leaves in drifts against the wall, grime streaks and old rust stains "
                   "on the stone, debris along the step, a patch of bare dry earth."),
    "ver_is": ("Sawdust and timber offcuts in a band along the edge, a stack of boards on a pallet, shoe prints in the "
               "dust, wheel tracks across the grass, a tarpaulin over the stored cushions."),
    "ver_bitti": ("A soft sheen on the new decking, faint wheel tracks across the grass, a few offcuts in a stack by the "
                  "step, a little sawdust in the board joints, a patch of trampled grass."),
}
FILM_IC = "A documentary interior photograph on colour negative film, true colour, fine grain."
FILM_DIS = "A documentary site photograph on colour negative film, true colour, fine grain."
