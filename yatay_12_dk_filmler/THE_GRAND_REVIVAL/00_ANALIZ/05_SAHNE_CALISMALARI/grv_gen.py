#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""THE GRAND REVIVAL — oda dosyaları üreticisi (90 sahne görseli + 12 oda son karesi + usta kare + 90 I2V).
Ortak bloklar tek kaynaktan, harfi harfine aynı [DERS 20]. Ayrıca PLAN · ÜRETİM GÜNLÜĞÜ · QA_SPEC içindeki
'ÜRETİCİ' işaretli tabloları ve 00_SAHNE_TABLOSU.md'yi yeniden yazar.

Koşu:  python3 yatay_12_dk_filmler/THE_GRAND_REVIVAL/00_ANALIZ/05_SAHNE_CALISMALARI/grv_gen.py"""
import math, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grv_istasyon import (IST, BIBLE, I2V_AC, I2V_KAPA, DOKU, FILM_IC, FILM_DIS, SEG_UZ, durum, DEFTER)
from grv_data import F, S, SEGMENT, ODALAR, G_SET, DONUS, USTA

FILM = "THE_GRAND_REVIVAL"
KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
N = 90
YASAK = ["crane", "hoist", "mirror", "television", "screen", "pool", "swimming", "fireplace", "candle", "flame",
         "smoke", "fog", "mist", "haze", "glow", "bloom", "rays", "beam", "flare", "neon", "signboard"]

# ── rejim ve saat (güneş saati) ───────────────────────────────────────────
def rejim(s): return "G" if s in G_SET else "A"
SAAT = []
_m = 6 * 60
for s in range(N):
    SAAT.append(_m)
    if rejim(s) == "A":
        _m += 10
SAAT.append(_m)
assert SAAT[89] == 20 * 60 and SAAT[90] == 20 * 60, (SAAT[89], SAAT[90])

def hhmm(m): return f"{m // 60:02d}:{m % 60:02d}"

def saat_en(m):
    h, mi = divmod(m, 60)
    ad = lambda x: ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "eleven", "twelve"][x % 12]
    gun = "in the morning" if h < 12 else ("in the afternoon" if h < 17 else "in the evening")
    if m == 12 * 60: return "Noon"
    t = {0: f"{ad(h)} o'clock", 10: f"ten past {ad(h)}", 20: f"twenty past {ad(h)}", 30: f"half past {ad(h)}",
         40: f"twenty to {ad(h + 1)}", 50: f"ten to {ad(h + 1)}"}[mi]
    if mi >= 40 and h + 1 == 12: gun = "in the morning"
    s = f"{t} {gun}"
    return s[0].upper() + s[1:]

# ── güneş (38° K · 21 Haziran · δ 23,44° · güneş öğlesi 12:00) ─────────────
LAT, DEC = math.radians(38.0), math.radians(23.44)
def gunes(m):
    H = math.radians(15.0 * (m - 720) / 60.0)
    se = math.sin(LAT) * math.sin(DEC) + math.cos(LAT) * math.cos(DEC) * math.cos(H)
    el = math.degrees(math.asin(se))
    az = math.degrees(math.atan2(math.sin(H), math.cos(H) * math.sin(LAT) - math.tan(DEC) * math.cos(LAT))) + 180.0
    return round(az) % 360, round(el)

def yon(rel):
    rel %= 360
    ana = [(0, "away from the camera"), (90, "to the right"), (180, "towards the camera"), (270, "to the left")]
    fark = lambda a, b: min((a - b) % 360, (b - a) % 360)
    s = sorted(ana, key=lambda x: fark(rel, x[0]))
    return s[0][1] if fark(rel, s[0][0]) <= 20 else f"{s[0][1]} and slightly {s[1][1]}"

def gunes_yeri(m, bakis):
    az, _ = gunes(m)
    rel = (az - bakis + 180) % 360 - 180
    return ("on the right" if rel > 0 else "on the left") + (" and ahead of the camera" if abs(rel) < 90 else " and behind the camera")

def gok(m):
    if m < 8 * 60: return "a clear pale early-summer morning sky with a few small high clouds; the air is clear"
    if m < 11 * 60: return "a clear blue sky with a few small white clouds; the air is clear"
    if m < 15 * 60: return "a deep blue midday sky with a few small white clouds; the air is clear"
    if m < 17 * 60 + 30: return "a clear afternoon sky with a few white clouds, the light turning warmer"
    if m < 19 * 60 + 20: return "golden late light, a clear sky with a few thin high clouds turning gold"
    if m < 19 * 60 + 40: return "soft afterlight just after sunset, the sky pale orange low and clear blue above"
    return "deep clear blue hour, the sky deep blue with a last pale warm band low on the horizon"

# ── kare kimliği ───────────────────────────────────────────────────────────
def seg_of(s):
    for kod, ist, a, b in SEGMENT:
        if a <= s <= b: return kod, ist, a, b
    raise KeyError(s)

def kare_bilgi(key):
    """key: int n (0..90) ya da "n'" → (seg kodu, istasyon, oda defteri, yerel k, saat, uç 'bas'/'son', önceki klip)"""
    if key == 90:
        return "D2", "D", "D", SEG_UZ["D"], SAAT[90], "son", 89
    if isinstance(key, str):
        n = int(key[:-1]); s = n - 1
        kod, ist, a, b = seg_of(s)
        assert s == b, key
        if kod in ("H2", "L2", "A2", "D2"):
            return kod, ist, kod[0], SEG_UZ[kod[0]], SAAT[n], "son", s
        return kod, ist, kod, b - a + 1, SAAT[n], "son", s
    kod, ist, a, b = seg_of(key)
    if kod in ("H2", "L2", "A2", "D2"):
        return kod, ist, kod[0], SEG_UZ[kod[0]], SAAT[key], "bas", key
    return kod, ist, kod, key - a, SAAT[key], "bas", key

def asama(key):
    kod, ist, oda, k, m, uc, s = kare_bilgi(key)
    if kod in ("H2", "L2", "A2", "D2"):
        degis, ek = DONUS[(kod, uc)]
        return durum(oda, k, degis, ek)
    return durum(oda, k)

# kapak kartı başlığı sol üstte (KAPAK §2) — yalnız son klibin iki karesi
BASLIK = (" Keep the upper left of the frame, above the tops of the left windows, plain ceiling and plain wall, "
          "low in contrast, with no light fitting or bright object in it.")

def faz(key):
    kod, ist, oda, k, m, uc, s = kare_bilgi(key)
    tam = SEG_UZ.get(oda, 0)
    if kod in ("H2", "L2", "A2", "D2"):
        if oda == "A": return "dis_bitti"
        return "ic_yasam" if (kod == "D2" or uc == "son") else "ic_bitti"
    if oda == "A": return "dis_harabe" if k == 0 else ("dis_bitti" if k >= tam else "dis_is")
    if oda == "T": return "ver_harabe" if k == 0 else ("ver_bitti" if k >= tam else "ver_is")
    doseme = {"H": 5, "L": 6, "D": 5, "K": 4, "M": 4, "W": 4, "B": 4}[oda]
    if k == 0: return "ic_harabe"
    if k >= tam: return "ic_bitti"
    return "ic_doseme" if k >= doseme else "ic_is"

def insanli(key):
    """kare kimin olduğunu söyler: 'yok' · 'isci' · 'isci+kisi' · 'kisi'"""
    act = F[key]["act"]
    if re.search(r"workers", act): return "isci+kisi" if "two people" in act else "isci"
    if "two people" in act: return "kisi"
    return "yok"

def klip_rejimi(key):
    """karenin TIME RATE'i: başladığı klibin rejimi (son kareler biten klibin)."""
    kod, ist, oda, k, m, uc, s = kare_bilgi(key)
    return rejim(s)

# ── blok üreticileri ───────────────────────────────────────────────────────
def isik(key):
    kod, ist, oda, k, m, uc, s = kare_bilgi(key)
    st = IST[ist]
    az, el = gunes(m)
    yer = gunes_yeri(m, st["bakis"])
    if el <= 0:
        bas = f"Sun azimuth {az} degrees, elevation {abs(el)} degrees below the horizon, {yer}, so there is no direct sun: "
        if ist == "A":
            govde = ("deep blue hour, the sky deep blue overhead with a last pale warm band low along the horizon behind "
                     "the roof; the lit windows and path lights give the only warm light")
        elif ist == "T":
            govde = ("soft afterlight just after sunset, the sky pale orange low behind the camera and clear blue above; "
                     "the lit wall lights give a small warm light under the veranda roof")
        elif ist == "H":
            govde = ("soft dusk light comes through the door and the two narrow windows, the garden outside deep blue"
                     + (", and the bronze chandelier is lit warm over the hall" if uc == "son" else ", the hall dim"))
        elif ist == "L":
            govde = ("the glass doors show the deep blue garden and the lit veranda"
                     + ("; the floor lamp and the ring light are lit warm over the room" if uc == "son" else "; the room lies in soft dusk light"))
        else:  # D
            govde = ("the bronze chandelier is lit warm over the table, and the glass doors show the deep blue garden with "
                     "the lit veranda beyond and a last pale warm band low on the horizon")
        return bas + govde + ". Early summer. The sun stays outside the frame."
    if ist == "A":
        _, y = golge_yonu(m, st["bakis"])
        return (f"Sun azimuth {az} degrees, elevation {el} degrees, {yer}; the front face of the villa stands in full warm "
                f"morning sun, the shadows lying {y}. Early summer in dry hill country: {gok(m)}. The sun stays outside the frame.")
    if ist == "T":
        _, y = golge_yonu(m, st["bakis"])
        return (f"Sun azimuth {az} degrees, elevation {el} degrees, {yer}; low golden sun lies full on the back of the villa "
                f"and under the veranda roof, long shadows stretching {y}. Early summer: {gok(m)}. The sun stays outside the frame.")
    leke = {
        "H": "sunlight falls in through the two narrow windows beside the arch in two long bright patches across the floor towards the camera, the rest of the hall in soft reflected light, and the view through the windows is bright daylight",
        "L": "sunlight falls in through the big window in the left wall in one bright slanting patch on the floor, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight",
        "D": "high sunlight falls in through the two tall windows in the left wall in short bright patches near the wall, the rest of the room in soft daylight from the glass doors, and the view through the glass is bright daylight",
        "K": "sunlight falls in through the wide window in the left wall in a bright slanting patch across the worktop line and the floor, the rest of the kitchen in soft daylight, and the view through the window is bright daylight",
        "M": "sunlight falls in through the tall window in the right wall in one long slanting patch across the floor, the rest of the room in soft daylight, and the view through the window is bright daylight",
        "W": "soft daylight falls from the long high strip window, and warm low sunlight from the bedroom window beyond the doorway spills across the floor, the sky in the strip window bright",
        "B": "soft warm evening daylight fills the room from the wide window, and the view through it is bright and golden",
    }[ist]
    return (f"Sun azimuth {az} degrees, elevation {el} degrees, outside {yer}; {leke}. Through the glass: {gok(m)}. "
            f"The sun stays outside the frame.")

def golge_yonu(m, bakis):
    az, el = gunes(m)
    uzun = "long" if el < 15 else ("medium-length" if el < 35 else "short")
    return uzun, yon(az + 180 - bakis)

def zaman_hizi(key):
    kod, ist, oda, k, m, uc, s = kare_bilgi(key)
    kim = insanli(key)
    if klip_rejimi(key) == "G":
        ozne = "the two people move" if kim == "kisi" else "the workers carry"
        return (f"Everything in this frame moves at natural speed. Eight seconds pass across this shot: {ozne} at their "
                "real pace and the light holds still; nothing is accelerated.")
    if IST[ist]["ic"]:
        ozne = ["the light", "the patches of sun", "the clouds outside the windows"]
    else:
        ozne = ["the clouds", "the shadows"]
    if kim == "isci": ozne.append("the workers")
    elif kim == "isci+kisi": ozne.append("the workers and the people")
    if ist == "A" or ist == "T": ozne.append("the carts")
    lst = ", ".join(ozne[:-1]) + " and " + ozne[-1]
    return (f"Everything in this frame is time-lapsed at the same rate: {lst} all move at the same accelerated speed. "
            "Ten minutes pass across this shot. Nothing moves at normal speed.")

def insan_kurali(key):
    kim = insanli(key)
    if kim == "yok": return "No people are present."
    if klip_rejimi(key) == "G":
        return "Every person is seen from the side or from behind, back to the camera, no readable face anywhere."
    if kim == "isci+kisi":
        return ("Workers and people appear only as soft motion streaks and blurred figures, none of them sharp, none "
                "facing the camera, no readable face anywhere.")
    return ("Workers appear only as soft motion streaks and blurred figures, none of them sharp, none facing the camera, "
            "no readable face anywhere.")

def fizik(key):
    kod, ist, oda, k, m, uc, s = kare_bilgi(key)
    a = asama(key)
    p = []
    if ist == "A":
        p.append("The villa stands on its stone base on level ground.")
        if "cart" in F[key]["act"] or "cart" in a: p.append("The low flat cart rests on its four wheels on the path.")
        if "scaffold" in a: p.append("The scaffold tower stands on its four feet on the lawn, braced against the wall.")
        if oda == "A" and k in (5, 6) and kod == "A":
            p.append("The new window unit hangs from one lifting sling held at each end by the workers until it is seated in the opening.")
        p.append("The birdbath sits on its pedestal" + (", and the stepladder stands on the lawn leaning on the wall." if "stepladder" in a else "."))
    elif ist == "T":
        p.append("The veranda roof bears on the four stone columns, and each column stands on the edge of the veranda floor.")
        if "cart" in a or "cart" in F[key]["act"]:
            p.append("The low flat cart rests on its four wheels on the lawn.")
        p.append("Every piece of furniture stands on the floor on its own feet." if k >= 2 or kod != "T" else
                 "The stacked boards rest on a pallet beside the cart.")
    else:
        p.append("The walls and the high ceiling bear on the stone shell of the villa.")
        if "cart" in a or "cart" in F[key]["act"]:
            p.append("The low flat cart rests on its four wheels on the floor.")
        if re.search(r"chandelier|ring-shaped|ceiling light", a) and re.search(r"hangs", a):
            p.append("The light fitting hangs from its ceiling hook, each chain taut under its weight.")
        if klip_rejimi(key) == "G" and kod != "D2" and uc == "bas":
            if oda == "K":
                p.append("The stone top hangs from a lifting sling at each corner, each sling held by a worker, its weight on their arms and backs.")
            else:
                p.append("The load is gripped in the workers' hands, its weight on their arms and backs, its underside clear of the floor.")
        if "two people" in F[key]["act"] and re.search(r"\bsit\b", F[key]["act"]):
            p.append("The two people are seated on their chairs, their weight on the seats.")
        if re.search(r"sofa|table|chair|bed|wardrobe|cabinet|console|bench|vanity|tub|island|stool", a):
            p.append("Every piece of furniture stands on the floor on its own feet and rests its full weight there.")
        else:
            p.append("The stepladder stands on its four feet on the floor, and the stored material rests on the membrane.")
    return " ".join(p)

def gorsel(key):
    kod, ist, oda, k, m, uc, s = kare_bilgi(key)
    st = IST[ist]
    if key == 90:
        bas = "Photorealistic documentary photograph — master frame G90, the target frame of the last shot (Scene 89 of 90). "
    elif isinstance(key, str):
        bas = f"Photorealistic documentary photograph — end frame of Scene {s} of 90, the target frame of that shot. "
    else:
        bas = f"Photorealistic documentary photograph — Scene {key} of 90. "
    gece = gunes(m)[1] <= 0
    if st["ic"]:
        lens = f"Lens: 24 mm spherical, f/5.6, ISO {800 if gece else 400}."
    else:
        lens = f"Lens: 24 mm spherical, f/8, ISO {800 if gece else (400 if m >= 18 * 60 else 100)}."
    act = F[key]["act"] + " " + insan_kurali(key)
    doku = DOKU[faz(key)] + " " + (FILM_IC if st["ic"] else FILM_DIS)
    return "\n".join([
        bas + "Horizontal 16:9 time-lapse of an abandoned stone villa being restored room by room, from a fixed 24 mm "
        f"camera in the {st['oda']}.",
        lens, st["kamera"], "",
        f"STRUCTURE: {BIBLE} AT THIS STAGE: {asama(key)}", "",
        f"SITE / BACKGROUND: {st['site']}", "",
        f"THE TIME MOMENT: {saat_en(m)}: {F[key]['mom']}", "",
        f"COMPOSITION: {st['komp']} Nothing that proves progress sits in the bottom tenth of the frame.{BASLIK if key in (89, 90) else ''}", "",
        f"LIGHTING: {isik(key)}", "",
        f"TIME RATE: {zaman_hizi(key)}", "",
        f"ACTIVITY: {act}", "",
        f"SITE TEXTURE: {doku}", "",
        f"PHYSICS: {fizik(key)}", "",
        f"NEGATIVE: {st['neg']}",
        "Output: 16:9, 4K, no text, no watermark.",
    ])

def gok_hareket(s):
    kod, ist, a, b = seg_of(s)
    m = SAAT[s]
    if rejim(s) == "G":
        return "Through the glass the few small clouds hold still."
    if ist == "A":
        if m >= 19 * 60 + 40:
            return "The sky dims from blue to deep blue in one smooth grade, and the last warm band low behind the roof fades."
        return "The small white clouds drift slowly from the right in one smooth flow, and the shadows shorten and turn slowly with the sun."
    if ist == "T":
        if s == 85:
            return "The thin high clouds drift slowly and the sky fades from gold to pale orange as the sun goes down behind the camera."
        return "The thin high clouds drift slowly and turn gold, and the long shadows stretch further towards the house as the sun sinks."
    if m >= 19 * 60 + 20:
        return "Through the windows the sky dims from pale orange to deep blue in one smooth grade."
    if ist == "W":
        return "Through the strip window the thin clouds drift slowly and turn warmer, and the warm patch from the doorway creeps slowly across the floor."
    if ist == "B":
        return "Through the window the thin clouds drift slowly and turn warmer, and the light in the room deepens towards gold."
    return "Through the windows the small white clouds drift slowly in one smooth flow, and the bright patch of sunlight creeps slowly across the floor."

def i2v(s):
    d = S[s]
    kod, ist, a, b = seg_of(s)
    if rejim(s) == "G":
        bas = "Eight seconds pass in real time. Everything in this shot moves at natural speed."
    else:
        bas = "Ten minutes pass. Everything in this shot is time-lapsed at the same rate."
    akis = " ".join(x for x in [bas, d["flow"], gok_hareket(s)] if x)
    return "\n".join([I2V_AC, "", f"MOTION FOCUS: {d['mf']}", "", akis, "", IST[ist]["sabit"], "", I2V_KAPA])

def hedef(s):
    kod, ist, a, b = seg_of(s)
    if s == 89: return 90
    return f"{s + 1}'" if s == b else s + 1

def etiket(key):
    return "G90" if key == 90 else (f"G{key[:-1]}′" if isinstance(key, str) else f"G{key}")

F[90] = dict(mom="the blue hour; the dining room is lit by its chandelier, and the two people sit at the far end of the table laid for two; beyond the glass doors the lit veranda.",
             act="At the far end of the table the two people in simple evening clothes sit at their places, in the two side chairs nearest the far end, facing each other across the table, the meal laid between them.")

# ── denetim ────────────────────────────────────────────────────────────────
HATA = []
def denetle(etk, metin):
    for w in YASAK:
        mm = re.search(rf"\b{re.escape(w)}(s|es)?\b", metin, re.I)
        if mm: HATA.append(f"{etk}: yasak '{mm.group(0)}'")
    for w in [r"\bdolly\b", r"\bvanish", r"\bdisappear"]:   # kamera kelimeleri kapıda bağlamıyla denetlenir
        mm = re.search(w, metin, re.I)
        if mm: HATA.append(f"{etk}: riskli kelime '{mm.group(0)}'")

# ── dosya yazımı ───────────────────────────────────────────────────────────
def degisen(s):
    kod, ist, a, b = seg_of(s)
    m0 = SAAT[s]
    if s == 0:
        return ["İlk kare — açılış. Önceki sahne yok."]
    if s == a:
        pk, pist, pa, pb = seg_of(s - 1)
        return [f"⛔ İSTASYON KESMESİ — {IST[pist]['ad']} → **{IST[ist]['ad']}** (sahip istisnası: oda başına sabit kamera)",
                f"önceki oda sonu ({etiket(hedef(s - 1))}): {S[s - 1]['son']}",
                f"bu odanın ilk karesi: {S[s]['ne'].split(';')[0]}",
                f"ışık: {hhmm(SAAT[s - 1])}→{hhmm(m0)} (kesmede saat sürer, atlamaz)"]
    return [f"önceki klibin hedefi = bu klibin ilk karesi: {S[s - 1]['son']}", f"ışık: {hhmm(SAAT[s - 1])} → {hhmm(m0)}"]

def oda_dosyasi(no, klasor, baslik, s0, s1):
    t0, t1 = s0 * 8.0, (s1 + 1) * 8.0
    kareler = s1 - s0 + 1
    out = [f"# 🎬 {FILM} — ODA {no:02d} · {baslik}  (S{s0}–S{s1} · {kareler} sahne görseli + oda son kareleri"
           f"{' + USTA KARE G90' if s1 == 89 else ''} + {kareler} I2V · {t0:.1f}–{t1:.1f} sn)".replace(".", ","),
           "",
           f"> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, değişmezler ve defterler `../{FILM}_PLAN.md`'de durur;",
           "> buradaki hiçbir prompt oraya ATIF YAPMAZ — her prompt tek başına çalışır. STRUCTURE (tam hâl) bütün promptlarda,",
           "> SITE / BACKGROUND · COMPOSITION · NEGATIVE ve I2V'nin DEĞİŞMEYECEKLER paragrafı aynı istasyonun bütün promptlarında",
           "> BİREBİR aynıdır; değişen AT THIS STAGE, THE TIME MOMENT, LIGHTING, TIME RATE, ACTIVITY, SITE TEXTURE ve PHYSICS.",
           ">",
           "> ⛔ Bloklar elle değil tek kaynaktan türetildi (`00_ANALIZ/05_SAHNE_CALISMALARI/grv_gen.py` + `grv_data.py` +",
           "> `grv_istasyon.py`) [DERS 20].",
           ">",
           "> ⭐ ÇOK İSTASYON (sahip istisnası 17.10.2026): her odanın kendi sabit kamerası ve kendi kare zinciri var. Bir odanın",
           "> son klibi o odanın **ODA SON KARESİ**'nde (G<n>′) biter; sonraki odanın ilk görseli başka kameradır — oda sınırı",
           "> bir KESMEDİR, ışık ve saat kesmede sürer. `🚪 ODA SON KARESİ` blokları prompt kapısının sayımına GİRMEZ (kapı",
           "> zinciri tek istasyon sayar); onlar da üretilir ve zincir_kontrol'e girer.",
           "> 🇹🇷 Her sahnenin başında: **önceki sahneye göre değişenler** ve **bu sahnede** ne olduğu.",
           "", "---", ""]
    for s in range(s0, s1 + 1):
        d = S[s]
        kod, ist, a, b = seg_of(s)
        out += [f"## 🎬 SAHNE {s} — {d['title']}", "", "```",
                (f"SÜRE: 8,0 s ({s * 8:.1f}–{(s + 1) * 8:.1f})  ·  #{s + 1:02d}  ·  REJİM: {rejim(s)} "
                 f"({'gerçek zaman' if rejim(s) == 'G' else '10 dk'})  ·  SAAT: {hhmm(SAAT[s])}→{hhmm(SAAT[s + 1])}  ·  "
                 f"İSTASYON: {ist} · {IST[ist]['ad']}").replace(".", ","),
                "```", "", f"**🔄 Önceki sahneye göre değişen (→ G{s}):**", ""]
        out += [f"- {x}" for x in degisen(s)]
        out += ["", f"**▶ Bu sahnede:** {d['ne']}", ""]
        g = gorsel(s); denetle(f"G{s}", g)
        out += [f"### 📸 GÖRSEL PROMPT (G{s})", "", "```", g, "```", ""]
        v = i2v(s); denetle(f"S{s} I2V", v)
        hd = hedef(s)
        out += [f"### 🎥 I2V PROMPT (G{s} → {etiket(hd)})", "", "```", v, "```", ""]
        if isinstance(hd, str):
            gp = gorsel(hd); denetle(etiket(hd), gp)
            out += [f"### 🚪 ODA SON KARESİ ({etiket(hd)} · {IST[ist]['ad']}) — S{s}'in hedefi · kapı saymaz", "",
                    f"> {IST[ist]['ad']} kamerasının son karesi; sonraki sahne başka istasyondan açılır. Önce bu kare üretilir (odanın",
                    "> usta karesi), oda zinciri ondan GERİYE türetilir.", "",
                    "```", gp, "```", ""]
        out += ["---", ""]
    if s1 == 89:
        g = gorsel(90); denetle("G90", g)
        out += ["## 🌟 USTA KARE — G90 (SAHNE DEĞİLDİR · son klibin hedefi · kapak kaynağı)", "",
                USTA, "", "### 📸 USTA KARE PROMPT (G90)", "", "```", g, "```", ""]
    yol = os.path.join(KOK, klasor)
    os.makedirs(yol, exist_ok=True)
    dosya = os.path.join(yol, f"{FILM}_ODA_{no:02d}.md")
    with open(dosya, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out).rstrip() + "\n")
    print("yazıldı", os.path.relpath(dosya, KOK))

# ── PLAN · GÜNLÜK · SPEC tabloları ─────────────────────────────────────────
def plan_tablolari():
    out = []
    for no, klasor, baslik, s0, s1 in ODALAR:
        out += [f"### 🎬 ODA {no} · {baslik}", "",
                f"`S{s0}–S{s1}` · #{s0 + 1:02d}–{s1 + 1:02d} · **{s0 * 8 // 60:02d}:{s0 * 8 % 60:02d}–{(s1 + 1) * 8 // 60:02d}:{(s1 + 1) * 8 % 60:02d}**"
                f" · ışık {hhmm(SAAT[s0])} → {hhmm(SAAT[s1 + 1])} · prompt dosyası `{klasor}/{FILM}_ODA_{no:02d}.md`", "",
                "| S · # | zaman · saat · rejim · istasyon | İŞ — ne hareket eder | SAHNE SONU — hedef kare | SES | ⚓ · kilit |",
                "|---|---|---|---|---|---|"]
        for s in range(s0, s1 + 1):
            d = S[s]; kod, ist, a, b = seg_of(s)
            z0, z1 = s * 8, (s + 1) * 8
            out.append(f"| **S{s}** · #{s + 1:02d} | {z0 // 60:02d}:{z0 % 60:02d}–{z1 // 60:02d}:{z1 % 60:02d} · {hhmm(SAAT[s])} · "
                       f"{rejim(s)} · {ist} | {d['ne']} | {etiket(hedef(s))}: {d['son']} | {d['ses']} | {d['kilit']} |")
        out.append("")
    return "\n".join(out)

def sahne_tablosu():
    out = ["| S | İST | REJİM · SAAT · AZ/EL | AŞAMA FİİLİ | ① kaynak · ② taşıyıcı · ③ hedef | ④ ne değişti (hedef kare) | ⑤ ne sabit (ölçü çapası) | KİLİT | KAPI |",
           "|:--:|:--:|---|---|---|---|---|---|:--:|"]
    capa = {"A": "kuş banyosu 86 px", "H": "taş kemer 584 px", "L": "hol açıklığı 542 px", "D": "üç cam kapı 918 px",
            "K": "yemek odası kapısı 420 px", "M": "koridor kapısı 192 px", "W": "yatak odası kapısı 250 px",
            "B": "pencere 512 px", "T": "2. kolon 64 px"}
    for s in range(N):
        d = S[s]; kod, ist, a, b = seg_of(s)
        az, el = gunes(SAAT[s])
        out.append(f"| S{s:02d} | {ist} | {rejim(s)} · {hhmm(SAAT[s])} · {az}°/{el}° | {d['title']} | {d['bes']} | {d['son']} | "
                   f"{capa[ist]} · ufuk %50 | {d['kilit']} | ✅ |")
    out.append(f"| G90 | D | G · 20:00 · {gunes(1200)[0]}°/{gunes(1200)[1]}° | USTA KARE | — | {S[89]['son']} | üç cam kapı 918 px · ufuk %50 | kapak kaynağı | ✅ |")
    return "\n".join(out)

def gunluk_kareler():
    out = ["| G | istasyon | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ | prompt birebir mi | zincir_kontrol | ölçü çapası elle | dosya |",
           "|:-:|:-:|---|---|---|---|:---:|:---:|---|"]
    # ters sıra: G90 → … · her segment kendi zinciri (son kare önce)
    for kod, ist, a, b in reversed(SEGMENT):
        son = hedef(b)
        out.append(f"| **{etiket(son)}** | {ist} | | {'— (metinden · KAPAK KAYNAĞI)' if son == 90 else '— (metinden · ODA USTA KARESİ) / ' + ist + ' akşam karesinden'} | | | | | |")
        for n in range(b, a - 1, -1):
            out.append(f"| {etiket(n)} | {ist} | | | | | | | |")
    return "\n".join(out)

def gunluk_klipler():
    out = ["| S | istasyon | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef zincir_kontrol | prompt birebir mi | ffprobe süre | kırpma | teslim süre | baş/orta/son | dosya |",
           "|:-:|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|---|"]
    for s in range(N):
        kod, ist, a, b = seg_of(s)
        out.append(f"| S{s} | {ist} | | {rejim(s)} | G{s} | {etiket(hedef(s))} | | | | | | | |")
    return "\n".join(out)

def spec_tablosu():
    out = ["| S | saniye | saat · rejim | istasyon | hedef karede görülmesi gereken | kanıt / sayı |",
           "|:-:|---|---|:-:|---|---|"]
    for s in range(N):
        d = S[s]; kod, ist, a, b = seg_of(s)
        out.append(f"| S{s} | {s * 8:.1f}–{(s + 1) * 8:.1f} | {hhmm(SAAT[s])} · {rejim(s)} | {ist} | {d['son']} | {d['kilit']} |".replace(".", ","))
    return "\n".join(out)

def isaretle(dosya, ad, govde):
    yol = os.path.join(KOK, dosya)
    if not os.path.exists(yol):
        print("  (atlandı, yok)", dosya); return
    metin = open(yol, encoding="utf-8").read()
    bas, son = f"<!-- ÜRETİCİ: {ad} BAŞI -->", f"<!-- ÜRETİCİ: {ad} SONU -->"
    if bas not in metin:
        print("  (işaret yok)", dosya, ad); return
    yeni = re.sub(re.escape(bas) + r".*?" + re.escape(son), lambda _: bas + "\n" + govde + "\n" + son, metin, flags=re.S)
    with open(yol, "w", encoding="utf-8") as fh:
        fh.write(yeni)
    print("tablo", ad, "→", dosya)

def main():
    assert len(S) == N and all(n in F for n in range(N))
    for kod, ist, a, b in SEGMENT:
        if b != 89: assert f"{b + 1}'" in F, (kod, b)
    for no, klasor, baslik, s0, s1 in ODALAR:
        oda_dosyasi(no, klasor, baslik, s0, s1)
    isaretle(f"{FILM}_PLAN.md", "SAHNE PLANI", plan_tablolari())
    isaretle(f"{FILM}_URETIM_GUNLUGU.md", "KARE ZİNCİRİ", gunluk_kareler())
    isaretle(f"{FILM}_URETIM_GUNLUGU.md", "KLİPLER", gunluk_klipler())
    isaretle(f"{FILM}_QA_SPEC.md", "SAHNE SAHNE", spec_tablosu())
    tab = os.path.join(KOK, "00_ANALIZ", "05_SAHNE_CALISMALARI", "00_SAHNE_TABLOSU.md")
    with open(tab, "w", encoding="utf-8") as fh:
        fh.write(f"# 🧮 {FILM} — SAHNE TABLOSU (sahne başına BİR satır · 90 satır + usta kare)\n\n"
                 "> Betikten üretilir (`grv_gen.py`); elle satır eklenmez. BEŞ SORU [SAHNE_PLAN_KARTI]: ① malzeme başlangıçta nerede ·\n"
                 "> ② taşıyıcı · ③ nereye oturur · ④ klip sonunda ne değişti · ⑤ ne sabit. KAPI ✅ = beşi cevaplı, prompt yazıldı.\n"
                 "> ⭐ Çok istasyon: ⑤ her istasyonun kendi ölçü çapasıdır (COMPOSITION'daki px cümlesi + I2V 'same width').\n\n"
                 + sahne_tablosu() + "\n")
    print("yazıldı", os.path.relpath(tab, KOK))
    if HATA:
        print("\n".join(HATA)); sys.exit(1)
    uz = [len(gorsel(n)) for n in range(N)] + [len(gorsel(90))]
    print("görsel uzunluk min/max", min(uz), max(uz), "· I2V max", max(len(i2v(s)) for s in range(N)))


if __name__ == "__main__":
    main()
