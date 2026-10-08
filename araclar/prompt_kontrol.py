#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROMPT KONTROL — üretimden ÖNCE koşar, maliyeti sıfır.

Kullanım:  python3 araclar/prompt_kontrol.py <film.md>
Çıkış kodu: 0 = GO · 1 = FIX (uyarı var) · 2 = BLOCK (üretme)

Bu betik METİN denetler, ANLAM denetlemez. Kapıdan geçen bir prompt iyi bir
prompt değildir — yalnız biçimsel olarak eksiksizdir. [AGENTS §6]
"""
import re
import sys
import unicodedata

BLOCK, FIX, INFO = [], [], []


def bul(baslik):
    return baslik


def normalize(t):
    t = unicodedata.normalize("NFKC", t)
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t


def blok_ayikla(metin):
    """(sahne_basligi, blok_tipi, kod) üçlüleri döndürür."""
    sahne, tip = None, None
    icinde, tampon = False, []
    cikti = []
    for satir in metin.splitlines():
        if satir.startswith("```"):
            if icinde:
                cikti.append((sahne, tip, "\n".join(tampon)))
                tampon, icinde = [], False
            else:
                icinde, tampon = True, []
            continue
        if icinde:
            tampon.append(satir)
            continue
        if satir.startswith("### "):
            tip = satir[4:].strip()
        elif satir.startswith("## "):
            sahne = satir[3:].strip()
            tip = None
        elif satir.startswith("# "):
            # üst başlık bölümü kapatır — sonraki kod blokları hiçbir sahneye
            # ait değildir (müzik promptu, paketleme, dosya listesi)
            sahne, tip = None, None
    return cikti


# ── yükleme ────────────────────────────────────────────────────────────────
if len(sys.argv) < 2:
    print("kullanım: prompt_kontrol.py <film.md>")
    sys.exit(2)

yol = sys.argv[1]

# ⭐ 14.09.2026 · YATAY İSKELET (KILAVUZ_REHBERI §2.8): film klasörü verilirse
# <FILM>_PLAN.md + <FILM>_BOLUM_1.md + <FILM>_BOLUM_2.md sahne sırasına göre
# BİRLEŞTİRİLİR ve kapı bir kez, bütün film boyunca koşar. Tek bölüm dosyasına
# koşulan kapı "usta kare yok / Scene N of X tutmuyor" der — bu arıza değil,
# eksik koşudur. Şablon klasörü (yolunda SABLON geçen) denetime girmez.
import os as _os
if "SABLON" in yol.upper():
    print(f"  şablon — atlandı: {yol}")
    sys.exit(0)
if _os.path.isdir(yol):
    _film = _os.path.basename(yol.rstrip("/"))
    _parcalar = [f"{_film}_PLAN.md", f"{_film}_BOLUM_1.md", f"{_film}_BOLUM_2.md"]
    _yollar = [_os.path.join(yol, d) for d in _parcalar]
    _eksik = [d for d, y in zip(_parcalar, _yollar) if not _os.path.exists(y)]
    if _eksik:
        _tek = _os.path.join(yol, f"{_film}_DIKEY_TIMELAPSE.md")
        if _os.path.exists(_tek):
            yol = _tek
            metin = open(yol, encoding="utf-8").read()
        else:
            print(f"⛔ klasör modu: eksik dosya {', '.join(_eksik)} (yatay iskelet PLAN + BOLUM_1 + BOLUM_2 ister)")
            sys.exit(2)
    else:
        metin = "\n\n".join(open(y, encoding="utf-8").read() for y in _yollar)
        print(f"  📁 FİLM KLASÖRÜ · {len(_yollar)} dosya birleşik (PLAN + BOLUM_1 + BOLUM_2) · {_film}")
else:
    metin = open(yol, encoding="utf-8").read()
bloklar = blok_ayikla(metin)

# ⭐ USTA KARE kendi BÖLÜMÜNDE durur (## başlığı) — sahne değildir [§2.7].
# Sahne içindeki "GÖRSEL PROMPT ⭐ USTA KARE" başlığı ESKİ formattır ve
# sahne görseli sayılır; ayıran şey blok başlığı değil BÖLÜMDÜR.
def _usta_bolum(baslik):
    """Bölüm başlığı 'USTA KARE' ile BAŞLIYOR mu (emoji sıyrılarak)."""
    if not baslik:
        return False
    return re.sub(r"^[^A-Za-zÇĞİÖŞÜ]+", "", baslik).startswith("USTA KARE")


usta = [(s, k) for s, t, k in bloklar
        if _usta_bolum(s) and t and "PROMPT" in t]
gorsel = [(s, k) for s, t, k in bloklar
          if t and "GÖRSEL PROMPT" in t and "KAPAK" not in t and "KAPAK" not in (s or "")
          and not _usta_bolum(s)]
i2v = [(s, k) for s, t, k in bloklar if t and "I2V" in t]
t2v = [(s, k) for s, t, k in bloklar if t and "T2V" in t]
# İçerik denetimleri usta kareyi de görür; sayım ve sıra denetimleri görmez.
kareler = gorsel + usta

print("═" * 62)
print(f"  PROMPT KONTROL · {yol.split('/')[-1]}")
print("═" * 62)
print(f"  sahne görseli {len(gorsel)}  ·  usta kare {len(usta)}  ·  "
      f"I2V {len(i2v)}  ·  T2V {len(t2v)}")
print()

# ── 1. sahne sayısı — promptun KENDİ beyanından türetilir ──────────────────
# Izgara sabit değildir (10×6 varsayılan, 4×10 gibi varyantlar meşru).
# Beklenen sayı dosyanın kendi "Scene N of X" satırından okunur.
beyanlar = [int(m.group(1)) for _, k in gorsel
            for m in [re.search(r"Scene\s+\d+\s+of\s+(\d+)", k)] if m]
if not beyanlar:
    BLOCK.append("hiçbir görsel promptta 'Scene N of X' satırı yok")
    BEKLENEN = len(gorsel)
elif len(set(beyanlar)) > 1:
    BLOCK.append(f"'Scene N of X' toplamı promptlar arasında tutarsız: {sorted(set(beyanlar))}")
    BEKLENEN = max(set(beyanlar), key=beyanlar.count)
else:
    BEKLENEN = beyanlar[0]

if len(gorsel) != BEKLENEN:
    BLOCK.append(f"görsel prompt sayısı {BEKLENEN} değil ({len(gorsel)})")
if len(i2v) != len(gorsel):
    BLOCK.append(f"I2V sayısı sahne görseli sayısına eşit değil ({len(i2v)} ≠ {len(gorsel)})")

# ── 1b. ⭐ İKİ KEYFRAME ZİNCİRİ — FORMATIN KENDİSİ [KILAVUZ_REHBERI §2.7] ───
# 08.09.2026, proje sahibinin kararı: foto1-video1-foto2-video2-…
# Her videonun solundaki foto ilk karesi, sağındaki foto son karesidir.
# N sahne = N+1 görsel + N I2V + 0 T2V. Yazılı kural kapı değildir [DERS 12];
# formatın kapısı burasıdır.
if not usta:
    BLOCK.append(
        f"⛔ ESKİ FORMAT — İKİ KEYFRAME ZİNCİRİ YOK [KILAVUZ_REHBERI §2.7]: "
        f"usta kare (G{BEKLENEN}) promptu yok. Format {BEKLENEN} sahne için "
        f"{BEKLENEN + 1} görsel + {BEKLENEN} I2V ister; son klibin HEDEF karesi "
        f"olmadan hiçbir klip iki uca kilitlenemez ve dikiş yine kırılır "
        f"(⑤ beş filmde beş kez düştü). Usta kare AYRI bir '## USTA KARE' "
        f"bölümünde durur — sahne bloğunun içinde değil ve başlığı 'USTA KARE' "
        f"ile BAŞLAR. Bu planın {len(i2v)} I2V'sinin hiçbiri son kareyi "
        f"kilitlemiyor; tek tek yazılmadı, sebep tek: format eski.")
elif len(usta) > 1:
    BLOCK.append(f"birden fazla usta kare promptu var ({len(usta)}) — "
                 f"zincirin son halkası TEKTİR [§2.7]")
if t2v:
    BLOCK.append(
        f"T2V bloğu var ({len(t2v)}) — zincirli formatta metinden üretilen klip "
        f"iki uca kilitlenemez, zinciri taşımaz ve dikişi kırar [§2.7 ②]. "
        f"Yedek, AYNI İKİ KAREDEN yeniden koşmaktır; T2V bloğu silinir.")

# ── 2. "Scene N of X" sıra tutarlılığı ─────────────────────────────────────
for i, (s, k) in enumerate(gorsel):
    m = re.search(r"Scene\s+(\d+)\s+of\s+(\d+)", k)
    if not m:
        BLOCK.append(f"[{s}] 'Scene N of X' satırı yok")
    elif int(m.group(1)) != i:
        BLOCK.append(f"[{s}] sahne numarası sırada değil: {m.group(1)}, beklenen {i}")

# ── 2b. TESLİM YAPISI beyanı [DERS 4] ──────────────────────────────────────
if not re.search(r"TESLİM YAPISI", metin):
    BLOCK.append("TESLİM YAPISI satırı yok — kapak kartı beyan edilmemiş [DERS 4]. "
                 "Beyansız kart, denetimde son SAHNE sayılır ve devamlılık ihlali üretir.")
elif not re.search(r"KAPAK KARTI", metin):
    BLOCK.append("TESLİM YAPISI var ama KAPAK KARTI satırı yok [DERS 4]")

# ── 3. YAPI BIBLE birebir tekrar ───────────────────────────────────────────
bibles = {}
for s, k in kareler:
    m = re.search(r"STRUCTURE:(.*?)(AT THIS STAGE)", k, re.S)
    if not m:
        BLOCK.append(f"[{s}] STRUCTURE bloğu ya da 'AT THIS STAGE' ayracı yok")
        continue
    bibles.setdefault(normalize(m.group(1)), []).append(s)
if len(bibles) > 1:
    BLOCK.append(
        f"YAPI BIBLE {len(kareler)} promptta BİREBİR aynı değil — "
        + str(len(bibles))
        + " farklı sürüm var: "
        + " | ".join(", ".join(v)[:60] for v in bibles.values())
    )

# ── 4. arka plan çapaları ──────────────────────────────────────────────────
ANA = "MAIN STATION"
siteler_ana, detay_site, capa_eksik = {}, [], []
for s, k in kareler:
    m = re.search(r"SITE / BACKGROUND:(.*?)\n\n", k + "\n\n", re.S)
    if not m:
        BLOCK.append(f"[{s}] 'SITE / BACKGROUND:' bloğu yok")
        continue
    govde = m.group(1)
    if ANA in k:
        siteler_ana.setdefault(normalize(govde), []).append(s)
    else:
        detay_site.append((s, govde))
if len(siteler_ana) > 1:
    BLOCK.append(
        "ANA istasyon sahnelerinde SITE/BACKGROUND birebir aynı değil — "
        + str(len(siteler_ana))
        + " farklı sürüm"
    )
# ⭐ Çapa denetimi FİLME ÖZEL KELİMEYE bağlanamaz [DERS 10]: ilk sürüm
# "brick / cypress / ridge" arıyordu ve ikinci filmde dört yanlış pozitif verdi.
# Genel ölçüt: detay istasyonunun SITE bloğu, ANA istasyonun SITE bloğuyla
# en az bir ALTI KELİMELİK ortak dizi paylaşmalı — yani aynı çapayı AYNI
# KELİMELERLE tarif etmeli.
def shingles(t, n=6):
    w = normalize(t).split()
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}

if siteler_ana:
    ana_govde = max(siteler_ana.items(), key=lambda kv: len(kv[1]))[0]
    ana_sh = shingles(ana_govde)
    for s, govde in detay_site:
        ortak = shingles(govde) & ana_sh
        if not ortak:
            BLOCK.append(f"[{s}] detay istasyonu ANA istasyonla ortak bir çapa cümlesi "
                         f"taşımıyor — aynı çapa AYNI KELİMELERLE yazılmalı [DERS 10]")
for s in capa_eksik:
    BLOCK.append(f"[{s}] detay istasyonu hiçbir arka plan çapası taşımıyor")

# ── 5. kamera satırı ───────────────────────────────────────────────────────
# GÖRSEL promptta altı alan zorunlu; I2V/T2V'de aranan şey SABİTLİK cümlesidir
# (I2V kamera satırı bilerek kısadır — istasyon görselde zaten tanımlı).
for s, k in kareler:
    m = re.search(r"^Camera:.*$", k, re.M)
    if not m:
        BLOCK.append(f"[{s}] görsel promptta 'Camera:' satırı yok")
        continue
    c = m.group(0).lower()
    for alan, desen in [
        ("yükseklik", r"metres (above|below)"),
        ("mesafe", r"metres from"),
        ("bakış açısı", r"bearing"),
        ("tilt", r"tilt"),
        ("roll", r"roll"),
    ]:
        if not re.search(desen, c):
            BLOCK.append(f"[{s}] kamera satırında '{alan}' yok — model onu her sahnede yeniden uydurur")
for s, k in i2v + t2v:
    if not re.search(r"(zero movement|never moves)", k, re.I):
        BLOCK.append(f"[{s}] video promptunda kamera sabitliği cümlesi yok")

# ── 6. güneş satırı ────────────────────────────────────────────────────────
for s, k in kareler:
    if not re.search(r"azimuth\s+\d+", k) or not re.search(r"elevation\s+\d+", k):
        BLOCK.append(f"[{s}] güneş satırı eksik (azimuth + elevation dereceyle yazılmalı)")

# ── 7. köşeli parantez atfı ────────────────────────────────────────────────
for s, k in kareler + i2v + t2v:
    for m in re.finditer(r"\[([A-ZÇĞİÖŞÜ_ ]{4,})\]", k):
        BLOCK.append(f"[{s}] köşeli parantez atfı: [{m.group(1)}] — prompt kendi başına çalışmalı [D-a]")

# ── 8. negatif çekirdek imzası ─────────────────────────────────────────────
IMZA = [
    ("kamera kilidi", r"never pans, tilts, zooms"),
    ("arka plan kilidi", r"never change shape, position, size"),
    ("metin yasağı", r"No readable text, letters, digits"),
    ("render yasağı", r"[Nn]o architectural visualisation look"),
    ("kesme yasağı", r"No cuts, no dissolves"),
]
for s, k in kareler:
    for ad, desen in IMZA:
        if not re.search(desen, k):
            BLOCK.append(f"[{s}] negatif çekirdek imzası eksik: {ad}")

# ── 9. metin yasağının KAPSAMI [D-b] ───────────────────────────────────────
# ⚠️ 08.09.2026: liste DÜNYA ŞANTİYESİNE göre yazılmıştı ve ilk Mars filminde
# sekiz yüzeyin yalnız beşi karşılık buldu — DERS 10'un aynısı, bu kez metin
# yasağında. Uzay/robotik saha yüzeyleri eklendi. Bir yüzeyi saymak onu
# ÇAĞIRMAK olmasın diye liste yalnız SAHADA GERÇEKTEN VAR OLANI ödüllendirir.
YUZEY = ["hoarding", "signage", "machinery", "container", "vest", "helmet",
         "truck", "scaffolding", "facade", "billboard", "licence plate",
         "shop front", "street plate", "formwork", "crane",
         # ── uzay · robotik saha ──
         "rover", "lander", "module", "habitat", "panel", "mast", "radiator",
         "antenna", "dish", "airlock", "spool", "cradle", "manipulator"]
# ⛔ 05.10.2026 [DERS 59]: "en az 8 yüzey say" kuralı SAHADA OLMAYAN nesneyi
# saymayı ödüllendirdi — DEEP STEP'in antik kuyusuna 'truck' buradan girdi.
# Artık kapsam iki yoldan biriyle sağlanır: genel 'on any surface' ifadesi ya da
# sahada GERÇEKTEN olan ≥8 yüzey. Olmayan nesnenin adı §10f'de BLOCK'tur.
YUZEY_METIN = YUZEY
for s, k in kareler:
    m = re.search(r"No readable text.*?(?:annotated by anyone|included\.)", k, re.S)
    if not m:
        continue
    if re.search(r"on any surface", m.group(0), re.I):
        continue
    govde = k.replace(m.group(0), " ")
    sayi = sum(1 for y in YUZEY if re.search(rf"\b{re.escape(y)}s?\b", govde, re.I)
               and y in m.group(0).lower())
    if sayi < 8:
        FIX.append(f"[{s}] metin yasağı KAPSAMSIZ — ne 'on any surface' ne de sahada olan ≥8 yüzey "
                   f"({sayi}) [D-b · DERS 59]")

# ── 10. render çukuru + insan kuralı + ZAMAN HIZI ──────────────────────────
for s, k in kareler:
    if "SITE TEXTURE" not in k:
        FIX.append(f"[{s}] SITE TEXTURE bloğu yok — emlak render'ı riski [§9.1]")
    # [DERS 33] insansız film "No people are present." der; o zaman insan kuralı
    # cümlesi ARANMAZ — koşullu cümle ("any suited figure…") astronot üretti.
    insansiz = re.search(r"\bno (people|humans?|workers|crew) (are|is) present\b", k, re.I)
    if insansiz and re.search(r"motion streaks|suited figure|workers appear", k, re.I):
        BLOCK.append(f"[{s}] insansız beyan VAR ama insan cümlesi de var [DERS 33] — "
                     f"olmayan özne prompta girmez, koşulla bile")
    # ⭐ 18.09.2026 REJİM G (gerçek zaman · 1×) [SANTIYE_HAREKETI §1 · ONE MORE TURN]:
    # klip sıkıştırılmıyorsa iz (streak) fiziksel olarak yoktur; insan kuralı
    # "sırtı kameraya, yüz okunmaz" hâline döner. ⚠️ Ölçülmedi — ilk koşu ONE MORE TURN.
    gercek = re.search(r"moves at natural speed", k)
    if gercek and not re.search(r"back to the camera|no readable face", k, re.I):
        FIX.append(f"[{s}] REJİM G (gerçek zaman) beyanı var ama insan kuralı yok — "
                   f"'back to the camera' / 'no readable face' [DERS 15 · SANTIYE_HAREKETI §1]")
    if "motion streaks" not in k and not insansiz and not gercek:
        FIX.append(f"[{s}] insan kuralı yok ('soft motion streaks') [§9.4]")
    # [DERS 15] hız tek cümlede ve TÜM öznelere birden yazılır
    if not re.search(r"time-lapsed at the same rate|moves at natural speed", k):
        BLOCK.append(f"[{s}] TIME RATE bloğu yok [DERS 15] — model gökyüzünü "
                     f"hızlandırıp yeri gerçek zamanda bırakıyor. Tek cümle, "
                     f"tüm özneler: bulut · gölge · makine · insan · araç.")

# ── 10a. ⭐ ARA HÂL · REJİM · ACTIVITY — A5-A8 kılavuzlarının kapısı ───────
# 08.09.2026: dört yeni kılavuz buraya bağlandı. Yazılı kural kapı değildir
# [DERS 12]; her kılavuz burada ya da kesme_kontrol.sh'de sonlanır.

# INSAAT_YONTEMI §2 — ara hâl GEÇİCİ EKİPMANLA tanımlanır
# ⚠️ Sözlük FİLME ÖZEL DEĞİLDİR [DERS 10]: hem geçici ekipmanı hem de
# toprak işlerinin ara hâl imzalarını kapsar. İlk sahne (henüz hiçbir şey
# yok) muaftır — merdivenin "önce" satırının ara hâli olmaz.
GECICI = (r"formwork|rebar|cage|scaffold|shoring|climbing|curing blanket|"
          r"sling|vacuum lifter|guy wire|falsework|prop|torch|paver|"
          r"piling rig|manlift|hoist|tagline|bracket|mullion|transom|"
          r"bucket teeth|teeth marks|step|bench|shotcrete|soil nail|auger|"
          r"grader|roller|screed|mesh|decking|membrane|welding|spark|"
          r"glowing|sinter|inflat|regolith bag|bags|spoil|raw cut|scar")
# INSAAT_YONTEMI §1 — 40 m'de 0,5 m altı nesne okunmaz (32 px/m)
KUCUK = r"torque mark|sealant bead|bolt head|test cylinder|weld bead|gasket|rivet"

for _i, (s, k) in enumerate(gorsel):
    m = re.search(r"AT THIS STAGE(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S)
    govde = m.group(1) if m else ""
    if _i > 0 and govde and not re.search(GECICI, govde, re.I):
        FIX.append(f"[{s}] AT THIS STAGE bloğunda GEÇİCİ EKİPMAN yok "
                   f"[INSAAT_YONTEMI §2] — kalıp · donatı kafesi · iskele · dikme · "
                   f"gergin sapan · kür örtüsü olmadan ara hâl yoktur, eleman BELİRİR "
                   f"(⑧ APPEARED · 1/9 MADE)")
    # ⭐ 08.09.2026: DERS 33'ün AT THIS STAGE hâli. "There is no mast and no
    # power unit" kadrajda OLMAYAN özneyi adlandırır ve model onu üretir.
    # Ölçüldü: aynı mekanizma astronot üretti. Boşluk POZİTİF tarif edilir:
    # "the mast footing is a bare sintered disc flush with the crust".
    if govde and re.search(r"\bthere (is|are) no\b|\bno \w+[, ]+(and )?no \w+", govde, re.I):
        FIX.append(f"[{s}] AT THIS STAGE'de OLMAYAN ÖZNE adlandırılmış [DERS 33] — "
                   f"'there is no X, no Y' modele istenmeyeni hatırlatır. Boşluğu "
                   f"POZİTİF yaz: orada ne VARSA onu tarif et (çıplak kabuk · boş "
                   f"sinter disk · izsiz ova).")
    m2 = re.search(KUCUK, k, re.I)
    if m2:
        FIX.append(f"[{s}] 0,5 m altı nesne yazılmış: '{m2.group(0)}' "
                   f"[INSAAT_YONTEMI §1] — 40 m'de 32 px/m; bu nesne 3 piksel, "
                   f"kadraja inmez, token harcar")

# SANTIYE_HAREKETI §1-2 — sıkıştırma rejimi beyan edilir ve tek olur
REJIM = r"ten minutes pass|two hours pass|a full working day passes|working day passes|eight seconds pass"  # ⭐ G: gerçek zaman (18.09.2026)
REJIM_C = r"(a full )?working day passes"
for s, k in kareler + i2v:
    if re.search(r"time-lapsed at the same rate|moves at natural speed", k) and not re.search(REJIM, k, re.I):
        FIX.append(f"[{s}] TIME RATE var ama SIKIŞTIRMA REJİMİ penceresi yok "
                   f"[SANTIYE_HAREKETI §2] — 'ten minutes pass' / 'two hours pass' / "
                   f"'a full working day passes' / 'eight seconds pass' (G) dördünden biri yazılır; yoksa model "
                   f"göğü sıkıştırıp yeri gerçek zamanda bırakır [DERS 15]")
    if re.search(REJIM_C, k, re.I) and re.search(
            r"\b(worker|workers|crew|people|operator)\b.{0,60}\b(walk|walks|carry|carries|"
            r"stand|stands|lay|lays|move|moves)\b", k, re.I):
        BLOCK.append(f"[{s}] REJİM C (iş günü · 5400x) beyan edilmiş ama görünür "
                     f"İNSAN cümlesi de var [SANTIYE_HAREKETI §1 · A6-X2] — 5400x'te "
                     f"insan kaybolur; iş YÜZEYLE kanıtlanır. Rejim A/B seç ya da "
                     f"insan cümlesini yüzey kanıtına çevir.")

# SANTIYE_HAREKETI §3-4 — ACTIVITY: iki hareket kaynağı + bir yüzey kanıtı
# Yüzey kanıtı ACTIVITY'de ya da SITE TEXTURE'da olabilir — ikisi birden okunur.
YUZEY = (r"\brut|\btrack|mud|dust|spoil|stockpile|pallet|\bpile|stack|cable|hose|"
         r"steam|puddle|crust|haze|clutter|offcut|tarpaulin|debris|scar")
# ⭐ HAREKET SAYIMI: kaç FARKLI HAREKET EDEN varsa o kadar kaynak.
# "stands · waits · queues" hareket DEĞİLDİR — ⑦ PARKED tam olarak odur.
EDEN = (r"excavator|loader|truck|crane|hoist|paver|roller|grader|pump|mixer|"
        r"telehandler|platform|climber|rover|drill|rig|dozer|worker|crew|"
        r"vehicle|jib|boom|cart|arm")
EYLEM = (r"work|lift|clear|pour|place|hoist|swing|crawl|travel|haul|tip|roll|"
         r"spray|unroll|weld|drill|bore|discharge|sweep|cross|rotate|glide|"
         r"dart|drive|climb|\brun|pulse|push|carry|move|dig|cut|spread|rise")
for _j, (s, k) in enumerate(gorsel):
    m = re.search(r"ACTIVITY:(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S)
    if not m:
        continue
    _son = (_j == len(gorsel) - 1)   # usta kare: saha bitmiştir, hareket borcu azdır
    g = m.group(1)
    mt = re.search(r"SITE TEXTURE:(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S)
    yuzey_govde = g + (mt.group(1) if mt else "")
    neden = len(set(x.lower() for x in re.findall(EDEN, g, re.I)))
    # ⭐ C2-g (05.10.2026): EKİP kelimesi iki el sayılır — adet yazılmaz, mertebe yazılır [§4]
    _ekip = 2 if re.search(r"\b(crew|team|gang|workers|labou?rers|masons|riggers|welders|carpenters|"
                           r"fitters|glaziers|divers)\b", g, re.I) else 0
    _el = len(set(x.lower() for x in re.findall(EDEN, g, re.I) if x.lower() not in ("worker", "crew"))) + _ekip
    if not _son and _el < 3:
        FIX.append(f"[{s}] ACTIVITY'de ana işe {_el} el (en az 3: taşıyıcı + ekip) [C2-g · SANTIYE_HAREKETI §4.8 ①] — "
                   f"iş SAYISI değil, tek işin etrafındaki EL artar")
    if neden > 6:   # ⭐ C1-d → C2-g: sınır 4'ten 6'ya (kalabalık notu ölçülmemiş varsayımdı)
        INFO.append(f"[{s}] ACTIVITY'de {neden} farklı hareket eden — hepsi ANA İŞE bağlı mı? "
                    f"[SANTIYE_HAREKETI §4.8 ⑤ · C2-g]")
    var_eylem = bool(re.search(EYLEM, g, re.I))
    yuzey_var = bool(re.search(YUZEY, yuzey_govde, re.I))
    if neden < 2 or not var_eylem or not yuzey_var:
        eksik = []
        if neden < 2:      eksik.append(f"hareket eden {neden} (en az 2)")
        if not var_eylem:  eksik.append("hiçbiri HAREKET ETMİYOR (stands/waits sayılmaz)")
        if not yuzey_var:  eksik.append("yüzey kanıtı yok (iz · çamur · toz · eksilen istif)")
        if _son:
            FIX.append(f"[{s}] ACTIVITY zayıf [SANTIYE_HAREKETI §4] — "
                       + " · ".join(eksik) + ". USTA KARE olduğu için kasıtlı "
                       f"olabilir; kasıtlıysa planda tek cümleyle gerekçelendir, "
                       f"değilse ⑦ merceği son klibi 'işsiz aralık' sayar.")
        else:
            FIX.append(f"[{s}] ACTIVITY eksik [SANTIYE_HAREKETI §4] — "
                       + " · ".join(eksik) + "; yoksa ⑦ İŞ merceği PARKED verir")

# ARAC_KARTLARI §1-2 — ızgara ölçülen kutu setinden yazılır
if not re.search(r"KUTU SET[İI]|kutu seti|bin set", metin, re.I):
    FIX.append("planda ARAÇ KUTU SETİ satırı yok [ARAC_KARTLARI §1] — klip süreleri "
               "kutuludur ({4,6,8} · {5,10} · {5,9}); ızgara ölçülen kutudan yazılır, "
               "plandan değil [DERS 23 · 31]")
elif re.search(r"KUTU SET[İI][^\n]*(ÖLÇÜLMEDİ|BİLİNMİYOR|⛔)", metin, re.I):
    FIX.append("ARAÇ KUTU SETİ satırı var ama ÖLÇÜLMEMİŞ [ARAC_KARTLARI §4] — "
               "plan yazılabilir, ÜRETİM AÇILAMAZ. Yedi ölçüm koşulup üretim "
               "günlüğü §0 doldurulmadan tek kare üretilmez [DERS 23].")
else:
    _kb = re.search(r"KUTU SET[İI][^\n]*?([0-9][0-9,\s·/]*)", metin, re.I)
    if _kb:
        _k = [float(x) for x in re.findall(r"[0-9]+(?:[.,][0-9]+)?", _kb.group(1).replace(",", "."))]
        if _k:
            _tavan = max(_k) - 1.00
            _uzun = [x.replace(",", ".") for x in
                     re.findall(r"^\|\s*\d\s*\|\s*([0-9]+[.,][0-9]+)\s*\|", metin, re.M)]
            _asan = [x for x in _uzun if float(x) > _tavan + 1e-9]
            if _asan:
                BLOCK.append(f"planda sahne tavanını aşan süre var: {' · '.join(sorted(set(_asan)))} sn "
                             f"[ARAC_KARTLARI §2] — kutu seti {_k}, kırpma bütçesi 1,00 sn, "
                             f"tek klipte teslim edilebilecek en uzun sahne {_tavan:.2f} sn. "
                             f"Uzatma ya da iki klip dikişi plana AÇIKÇA yazılmalı.")

# ── 10c. ⭐ THE DUST YEAR KAPILARI — DERS 35-43 · 08.09.2026 ───────────────
# Altıncı film (ilk uzay filmi) ölçüldü: ⑧ 0,0/10 · ⑦ PARKED · ② DIFFERENT.
# Aşağıdaki altı kapının her biri o teslimde ÖLÇÜLMÜŞ bir arızaya bağlıdır.

# sahne no → süre (aşama merdiveninin SÜRE sütunu)
_SURE = {int(a): float(b.replace(",", "."))
         for a, b in re.findall(r"^\|\s*(\d)\s*\|\s*([0-9]+[.,][0-9]+)\s*\|", metin, re.M)}
_ENUZUN = max(_SURE.values()) if _SURE else None

def _sahne_no(s):
    m = re.search(r"SAHNE\s+(\d+)", s or "")
    return int(m.group(1)) if m else None

# [DERS 35] metin yasağı HİÇBİR NESNE ADI ANMAZ.
# Ölçüldü: "module" on promptta yalnız NEGATIVE'in nesne listesinde geçti ve
# ekranda "utility modules" belirdi. Yasağın içindeki İSİM sahneyi doldurur.
for s, k in kareler + i2v:
    mneg = re.search(r"NEGATIVE:(.*?)(?:\nOutput:|\Z)", k, re.S)
    if not mneg:
        continue
    neg = mneg.group(1)
    govde = k.replace(neg, " ")
    mlist = re.search(r"\bnot on\b(.{0,400}?)(?:\.|\n)", neg, re.I | re.S)
    if mlist:
        adlar = [a.lower() for a in re.findall(r"\bthe ([a-z][a-z-]+)\b", mlist.group(1), re.I)]
        if len(adlar) >= 2:
            sizan = sorted({a for a in adlar if not re.search(rf"\b{re.escape(a)}s?\b", govde, re.I)})
            ek = (" · gövdede HİÇ geçmeyen: " + ", ".join(sizan)) if sizan else ""
            BLOCK.append(f"[{s}] metin yasağı {len(adlar)} NESNE ADI sayıyor [DERS 35] — "
                         f"yasağın içindeki isim ekrana gelir (ölçüldü: 'module'). "
                         f"Yasak YÜZEYE göre yazılır: 'anywhere in the frame, on any "
                         f"surface'{ek}")

# [DERS 36] STRUCTURE tam-hâl tarifi, AT THIS STAGE'den UZUN olamaz.
# Ölçüldü: 751 vs 403 karakter (1,86x) ve tam hâl ÖNDE → ⑧ 0,0/10,
# sekiz elemanın sekizi de "first seen INCOMPLETE at NEVER".
# İki prompt biçimi vardır: STRUCTURE/AT THIS STAGE ve SCENE LOCK/STAGE.
# ⚠️ [DERS 10] Kapı biçime körse SESSİZ GEÇER — üçüncü hâl FIX'tir.
for s, k in kareler:
    m = re.search(r"(?:^|\n)STRUCTURE:(.*?)(?:\nSITE / BACKGROUND:|\n[A-Z][A-Z /]+:)", k, re.S)
    if m and "AT THIS STAGE" in m.group(1):
        tam, asama = [x.strip() for x in m.group(1).split("AT THIS STAGE:", 1)]
    else:
        m1 = re.search(r"(?:^|\n)SCENE LOCK:(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S)
        m2 = re.search(r"(?:^|\n)STAGE:(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S)
        if not (m1 and m2):
            FIX.append(f"[{s}] ne STRUCTURE/AT THIS STAGE ne SCENE LOCK/STAGE bulunamadı "
                       f"[DERS 36] — ara hâl oranı ÖLÇÜLEMEDİ; kapı bu sahnede kördür")
            continue
        tam, asama = m1.group(1).strip(), m2.group(1).strip()
    if len(tam) > len(asama):
        BLOCK.append(f"[{s}] STRUCTURE tam-hâl tarifi ({len(tam)} krk) AT THIS STAGE'den "
                     f"({len(asama)} krk) UZUN [DERS 36] — model uzun, önde ve olumlu olanı "
                     f"beyan sayar; ara hâl niteleme olarak silinir. Tam hâl tek cümleye iner "
                     f"('When finished this will be a …'), sayılar QA_SPEC'te kalır.")

# [DERS 39] LIGHTING güneşi YALNIZ etkisiyle anar; disk anılırsa kadraja girer.
for s, k in kareler + i2v:
    m = re.search(r"LIGHTING:(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S)
    if m and re.search(r"\b(sun|solar)\b[^.]{0,40}\bdisc\b|\bdisc[^.]{0,20}\bsun\b|"
                       r"\bsun is visible\b|\bsun disc\b", m.group(1), re.I):
        BLOCK.append(f"[{s}] LIGHTING'de GÜNEŞ DİSKİ anılmış [DERS 39 · 32] — 'no edge' bir "
                     f"sıfattır, 'disc' bir nesnedir; nesne gelir. Güneş yalnız açı · gölge "
                     f"yönü · gölge oranı · gökyüzü rengiyle anılır.")

# [DERS 40] gölge taşıyıcısı olmayan sahne (rejim C) filmin EN UZUN sahnesi olamaz.
# ⚠️ [DERS 10] Ders "rejim C" hakkında DEĞİL, GÖLGESİZ sahne hakkındadır.
# Dünya'da "one accelerated working day" gölgeyi KALDIRMAZ, tersine en güçlü
# taşıyıcıdır. Kapı yalnız ışığın düz/gölgesiz beyan edildiği yerde açılır.
GOLGESIZ = (r"shadowless|no cast shadow|without shadows?|light stays flat|"
            r"flattened by|no shadow sweep|almost no shadow")
if _ENUZUN and len(set(_SURE.values())) > 1:
    _c_dusen = set()
    for s, k in kareler + i2v:
        n = _sahne_no(s)
        if n is None or n in _c_dusen or not re.search(REJIM_C, k, re.I):
            continue
        if not re.search(GOLGESIZ, k, re.I):
            continue
        if abs(_SURE.get(n, -1) - _ENUZUN) < 1e-9:
            _c_dusen.add(n)
            BLOCK.append(f"[{s}] REJİM C ({_SURE[n]:g} sn) filmin EN UZUN sahnesi [DERS 40] — "
                         f"rejim C gölgeyi kaldırır ve DERS 15 gereği geriye üretilmeyen bir "
                         f"taşıyıcı kalır. Ölçüldü: 10,0 sn'lik rejim C klibi ⑦'de %100 boş. "
                         f"Bu sahne en kısa banda iner, doruk fırtınanın BIRAKTIĞI sahneye geçer.")

# [DERS 41] insansız sahada makine, ELLE KULLANILAN makine adıyla anılmaz.
ELLI = r"\b(bulldozer|dozer|loader|grader|excavator|digger|backhoe|forklift|skid[- ]steer)\b"
for s, k in kareler + i2v:
    if not re.search(r"\bno (people|humans?|workers|crew) (are|is) present\b", k, re.I):
        continue
    mact = re.search(r"ACTIVITY:(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S)
    adlar = sorted({a.lower() for a in re.findall(ELLI, k, re.I)})
    if not adlar:
        continue
    hareketli = mact and re.search(ELLI, mact.group(1), re.I)
    mesaj = (f"[{s}] insansız beyan var ama ELLE KULLANILAN makine adı kullanılmış: "
             f"{', '.join(adlar)} [DERS 41] — bu adların korpusunda kabin, cam, basamak ve "
             f"OPERATÖR vardır ('rover' eki gövdeyi değiştirmiyor; ölçüldü: 'open-air cabins "
             f"and exposed operators'). Gövde pozitif kapatılır: 'Every machine is a sealed "
             f"robotic unit with no cab, no window, no seat and no handrail.'")
    (BLOCK if hareketli else FIX).append(mesaj)

# [DERS 43] ACTIVITY'de makine, büyüyen elemanı NESNE olarak alır; fiil GEÇİŞLİDİR.
GECISLI = (r"\b(lifts?|sets?|bolts?|places?|fills?|tips?|welds?|pulls?|unrolls?|lowers?|"
           r"hauls?|stacks?|pours?|spreads?|clamps?|threads?|drops?|slots?|seats?|"
           r"beds?|screeds?|sprays?|packs?|tamps?|hoists?|swings?)\s+"
           r"(a|an|the|one|its|another|two|three|four|five|six|filled|fresh)\b")
YORUNGE = r"\b(drives?|crosses?|moves?|orbits?|circles?|travels?|runs?|laps?)\b"
for _j, (s, k) in enumerate(gorsel):
    m = re.search(r"ACTIVITY:(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S)
    if not m:
        continue
    g = m.group(1)
    if re.search(GECISLI, g, re.I):
        continue
    ek = (" — cümledeki tek hareket YÖRÜNGE (drives/crosses/circles)" if re.search(YORUNGE, g, re.I) else "")
    FIX.append(f"[{s}] ACTIVITY'de GEÇİŞLİ FİİL + NESNE yok [DERS 43]{ek}. Ölçüldü: nesnesiz "
               f"ACTIVITY on klibin sekizinde ⑦ %100 boş verdi ve dört sahne 'a rover drives "
               f"in circles' diye okundu. En az bir makine, o sahnede BÜYÜYEN ELEMANI nesne "
               f"alır: 'lifts a filled tube out of the pit and sets it onto the fourth course'.")

# [DERS 38] geniş sahada İKİ mesafe beyan edilir (yakın kenar · yapı ekseni).
_capm = re.findall(r"Ø\s*([0-9]+(?:[.,][0-9]+)?)\s*m", metin)
_genis = any(float(x.replace(",", ".")) >= 20.0 for x in _capm)
if _genis and re.search(r"^\s*│?\s*mesafe", metin, re.M | re.I):
    if not re.search(r"D_eksen|yapı eksenine|eksen mesafesi", metin, re.I):
        FIX.append("geniş saha (Ø ≥ 20 m) ama Değişmezler tek MESAFE beyan ediyor [DERS 38] — "
                   "yükseklik yüzdeleri YAPI EKSENİNE olan mesafeden hesaplanır, sahanın yakın "
                   "kenarından değil. Ölçüldü: THE DUST YEAR'da direk tacı planda %82,0 yazıldı, "
                   "beyan edilen istasyon %70,7 üretir — 11,3 puan. İki satır yazılır: "
                   "D_kenar (güvenli alan) ve D_eksen (bütün yüzdeler).")

# ── 10b. RİTİM ve MEVSİM TAŞIYICISI — plan seviyesi denetimleri ────────────
if "MEVSİM TAŞIYICISI" not in metin:
    BLOCK.append("AŞAMA MERDİVENİNDE 'MEVSİM TAŞIYICISI' sütunu yok [DERS 14] — "
                 "taşıyıcısı olmayan sahne zamanı durdurur ve film süresini "
                 "olduğundan kısa okutur.")

_DIKEY_ON = ("dikey_shorts" in yol or yol.endswith("_DIKEY_TIMELAPSE.md"))
# Süre sütunu: on sahnenin süresi EŞİTSE ⑥ merceği METRONOM hükmü verir.
# ⚠️ 08.09.2026: desen ondalık İSTER. Eskisi "| 0 | 20 | ilkbahar |" gibi
# her tabloyu SÜRE sütunu sanıyordu ve Mars filminin güneş saati tablosunu
# ızgaraya karıştırdı. kesme_kontrol.sh zaten ondalık arıyordu — iki araç
# aynı deseni kullanır.
sureler = re.findall(r"^\|\s*\d\s*\|\s*([0-9]+[.,][0-9]+)\s*\|", metin, re.M)
if len(sureler) >= 6:
    benzersiz = {x.replace(",", ".") for x in sureler}
    if len(benzersiz) == 1 and _DIKEY_ON and benzersiz == {"8.0"}:
        # ⭐ 05.10.2026: dikey 7 × 8,0 sahip kuralıdır [DERS 58]. "Beklenen" FIX her planda
        # tekrarlandı ve gerçek uyarıları gürültüde boğdu — beyanlı ızgara bilgi satırıdır.
        INFO.append("süreler eşit (8,0) — sahip kuralı, beyanlı DÜZ IZGARA [DERS 58 · C1-e]; "
                    "ritim klip İÇİNDE taşınır (KURGU_VE_TESLIM §2.4)")
    elif len(benzersiz) == 1:
        FIX.append(f"AŞAMA MERDİVENİNDE bütün sahne süreleri aynı ({sureler[0]}) "
                     f"[DERS 13] — eşit aralıklı kesme dizisi tempo değil NABIZ "
                     f"üretir ve ⑥ merceği METRONOM hükmü verir. En az iki sahne "
                     f"KISA, en az bir sahne UZUN olmalı (ölçüye oturarak). "
                     f"⭐ Sahip beyanlı DÜZ IZGARADA (KILAVUZ_REHBERI §2.2 karşı kayıt · C1-e) "
                     f"bu uyarı BEKLENENDİR: düzeltilmez, plana kabul edilmiş risk yazılır.")
    else:
        INFO.append(f"süre dağılımı: {' · '.join(sureler)}")
elif "| SÜRE |" not in metin and "| S | SÜRE" not in metin:
    FIX.append("AŞAMA MERDİVENİNDE SÜRE sütunu okunamadı [DERS 13] — süreler "
               "eşitse ⑥ METRONOM verir; sütun tabloya eklenmeli")

# ── 11. I2V disiplini ──────────────────────────────────────────────────────
ACILIS = "The scene begins exactly as the provided image."
for s, k in i2v:
    if not k.strip().startswith(ACILIS):
        BLOCK.append(f"[{s}] I2V ilk cümlesi '{ACILIS}' değil")
    if usta and "ends exactly on the second provided image" not in k:
        BLOCK.append(f"[{s}] I2V SON kareyi KİLİTLEMİYOR [§2.7] — 'The shot ends "
                     f"exactly on the second provided image: its last frame is that "
                     f"image, matched frame for frame …' cümlesi yok. Tek uçlu I2V "
                     f"zincirin yarısıdır; dikiş yine serbest uçta kalır.")
    if "does not move at any point" not in k:
        BLOCK.append(f"[{s}] I2V'de 'kamera hareket etmez' paragrafı yok")
    if not re.search(r"identical in the first (and last frame|frame and in the last frame)", k):
        BLOCK.append(f"[{s}] I2V'de kadraj sabitliği cümlesi yok")
    if re.search(r"column grid|bay spacing|footprint", k):
        FIX.append(f"[{s}] I2V yapıyı YENİDEN TARİF ediyor — yalnız zaman geçişi yazılır")
    # [DERS 6] "no zoom" tek başına tutmadı; ölçülebilir çapa aranır
    if not re.search(r"same width of the frame|exactly the same width|half the frame height", k):
        FIX.append(f"[{s}] kamera kilidi ÖLÇÜLEBİLİR değil [DERS 6] — "
                   f"'the anchor occupies exactly the same width of the frame in the "
                   f"first and last frame' gibi bir çapa cümlesi ekle")

# ── 12b. vinç kancası: yüklü ve düşey mi, kadraj dışı mı [DERS 8] ──────────
for s, k in kareler:
    # "no crane", "There is no crane" gibi OLUMSUZ geçişler vinç varlığı sayılmaz
    olumlu = [m for m in re.finditer(r"\bcrane\b", k, re.I)
              if not re.search(r"\bno\s+$", k[max(0, m.start() - 4):m.start()], re.I)]
    if not olumlu:
        continue
    yuklu = re.search(r"carries a visible load|always carries a visible load|"
                      r"with a .{0,40} on the hook|hook block .{0,60}load", k, re.I)
    disari = re.search(r"above the top edge of the frame|out of the top of the frame|"
                       r"the jib is not visible|only the mast is visible", k, re.I)
    if not (yuklu or disari):
        FIX.append(f"[{s}] vinç var ama kanca kararı yok [DERS 8] — kanca ya YÜKLÜ ve "
                   f"düşey yazılır ya da bom KADRAJ DIŞINDA bırakılır. Boş kanca kopuyor.")
    if re.search(r"empty hook|hook hangs empty|unloaded hook", k, re.I):
        BLOCK.append(f"[{s}] BOŞ KANCA yazılmış [DERS 8] — v1'de kanca halattan koptu")

# ── 12. kamera hareketi kaçağı ─────────────────────────────────────────────
HAREKET = r"\b(pans?|tilts?|zooms?|dollys?|orbits?|tracking shot|handheld|gimbal|crane up|push in|pull back)\b"
for s, k in kareler + i2v + t2v:
    for m in re.finditer(HAREKET, k, re.I):
        onceki = k[max(0, m.start() - 40):m.start()].lower()
        sonraki = k[m.end():m.end() + 24].lower()
        # "tilt 0 degrees" / "tilted 8 degrees down" bir SPESİFİKASYONDUR
        if re.match(r"\s*(-?\d+([.,]\d+)?)\s*(degrees|derece)", sonraki):
            continue
        if not re.search(r"\b(no|never|zero|without)\b[^.]*$", onceki):
            FIX.append(f"[{s}] olumlu kamera hareketi kelimesi: '{m.group(0)}' — bağlamı kontrol et")

# ── 10d. ⭐ A9–A12 KILAVUZLARININ KAPISI — 11.09.2026 ─────────────────────
# Dört prompt bloğu (SITE TEXTURE · PHYSICS · COMPOSITION · TIME RATE gök)
# üçüncü kuşak araştırmadan birer kılavuz aldı. Yazılı kural kapı değildir
# [DERS 12]; dördü de burada sonlanır. Kaynak: arastirma/SONUCLAR/A9-A12_DENETIM.md

def _blok(k, ad):
    m = re.search(rf"(?:^|\n){ad}:(.*?)(?:\n[A-Z][A-Z /+]+:|\nOutput:|\Z)", k, re.S)
    return m.group(1) if m else None

# MALZEME_VE_DOKU §2 · §5 — SITE TEXTURE bant/alan sayar; havasız sahada su yazmaz
DOKU = (r"\bmud\b|\brut|\btrack|puddle|standing water|stack|pallet|offcut|tarpaulin|"
        r"clutter|slurry|spatter|streak|stain|rust|dust|grime|drift|regolith|ejecta|"
        r"tread|print|frost|ice|snow|sand|sheen|bleed|efflorescence|patch|crust|"
        r"debris|spoil|gravel|silt|oil|soot|film|band|apron|pond|scar|crack")
# ⚠️ "regolith" tek başına havasız demek DEĞİLDİR (buz gezegeninde de regolit var,
# POLAR HABITAT'ta kar yağıyor); yalnız AÇIK atmosfersizlik beyanı sayılır.
HAVASIZ = (r"\b(in (a |the )?(hard )?vacuum|vacuum of space|airless|no atmosphere|zero atmosphere|without (an )?atmosphere|"
           r"lunar surface|on the moon|the moon's|martian surface|on mars)\b")
# "frozen mud" sıvı su değildir; permafrost sahasında meşru.
SU = r"(?<!frozen )(?<!dried )\b(mud|muddy|puddles?|standing water|rain|rainwater|slush|wet mud)\b"
for s, k in kareler:
    dk = _blok(k, "SITE TEXTURE")
    if dk is None:
        continue   # blok yokluğu §10'da zaten FIX
    n = len(set(x.lower() for x in re.findall(DOKU, dk, re.I)))
    if n < 5:
        FIX.append(f"[{s}] SITE TEXTURE'da {n} somut yüzey nesnesi/bandı (en az 5) "
                   f"[MALZEME_VE_DOKU §2 · §5] — bant ve alan yazılır (çamur yolu · pas "
                   f"akıntısı · şerbet alanı · ejecta yelpazesi); nesne sayılmaz")
    if re.search(HAVASIZ, k, re.I) and re.search(SU, dk, re.I):
        BLOCK.append(f"[{s}] HAVASIZ saha beyan edilmiş ama SITE TEXTURE su/çamur yazıyor "
                     f"[MALZEME_VE_DOKU §5 · A9-g] — Ay/Mars'ta 'mud · puddles' fizik "
                     f"dışıdır; beş filmde aynı cümle Dünya'dan Ay'a taşındı ve model saçmaladı")

# FIZIK_VE_AGIRLIK §5 — PHYSICS üç satır: taşınan · asılı+taşıyıcı · mekanizma
TEMAS = (r"\b(rests?|resting|bears?|bearing|bolted|welded|clamped|pinned|anchored|"
         r"braced|planted|seated|sits|stands? on|pressed into|press into|locked into|"
         r"footed|founded|embedded|keyed|strapped)\b")
ASILI = r"\b(hangs?|hanging|suspended|floats?|floating|lifted|hoisted|slung|dangles?)\b"
TASIYICI = r"\b(cable|sling|hook|jib|boom|crane|tether|rope|wire|chain|trolley|gantry|winch|strap)\b"
for s, k in kareler:
    fz = _blok(k, "PHYSICS")
    if fz is None:
        FIX.append(f"[{s}] PHYSICS bloğu yok [FIZIK_VE_AGIRLIK §5] — altı filmde ⑧ APPEARED; "
                   f"her sahnede taşınan · asılı · hareket eden yazılır")
        continue
    if len(re.findall(TEMAS, fz, re.I)) < 3:
        FIX.append(f"[{s}] PHYSICS'te <3 TEMAS cümlesi [FIZIK_VE_AGIRLIK §5 · A10-i] — "
                   f"'rests on · bears on · bolted · planted · pressed into'; genel "
                   f"'everything rests on the ground' yük yolunu yazmaz")
    if re.search(ASILI, fz, re.I) and not re.search(TASIYICI, fz, re.I):
        FIX.append(f"[{s}] PHYSICS'te ASILI cisim var, TAŞIYICI yok [FIZIK_VE_AGIRLIK §4 · "
                   f"DERS 46] — gövdesiz kanca sarkar; 'hangs from the jib on one taut cable'")

# PERSPEKTIF_VE_OLCEK §4 — COMPOSITION'da ölçülen pikselden kesir-çapa cümlesi
KESIR = (r"\b(spans?|occupies|keeps|holds|covers)\b[^.]{0,80}\b(\d+\s*pixels?|one[- ]"
         r"(half|third|quarter|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|"
         r"fifteenth|sixteenth|twentieth|[a-z]+(?:-[a-z]+)?th)|percent of (the )?frame)")
for s, k in kareler:
    kp = _blok(k, "COMPOSITION")
    if kp is None:
        continue   # COMPOSITION yokluğu DERS 20 blok kapısında
    if not re.search(KESIR, kp, re.I):
        FIX.append(f"[{s}] COMPOSITION'da referans nesne KESİR/PİKSEL cümlesi yok "
                   f"[PERSPEKTIF_VE_OLCEK §4] — 'the boulder spans 96 pixels of frame "
                   f"width — one eleventh — and keeps that width'; yüzde tek başına "
                   f"ölçeği tutmaz (① STATION IDENTITY 0/10 · ② SCALE LOCK 4/10)")

# HAVA_VE_ATMOSFER §1 · §5 — I2V'de gök/atmosfer hareket cümlesi
GOK = r"\b(clouds?|sky|haze|fog|mist|stars?|overcast|dust wall|cirrus|cumulus|stratus)\b"
GOK_FIIL = (r"\b(drift|drifts|streak|streaks|sweep|sweeps|roll|rolls|cross|crosses|"
            r"stretch|stretches|flow|flows|race|races|boil|boils|thin|thins|hold|holds|"
            r"stay|stays|remain|remains|fade|fades|brighten|brightens|dim|dims|grade|"
            r"grades|move|moves|pass|passes|smooth|smooths|clear|clears)\b")
for s, k in i2v:
    if not re.search(GOK, k, re.I):
        FIX.append(f"[{s}] I2V'de GÖK cümlesi yok [HAVA_VE_ATMOSFER §1 · DERS 15 · 47] — "
                   f"gök yazılmazsa model onu ayrı saatte akıtır ya da dondurur; "
                   f"rejimin görünümü adıyla yazılır (drift · streak · flat haze) — "
                   f"havasız sahada 'the sky stays a hard black field'")
    elif not re.search(GOK + r"[^.]{0,60}" + GOK_FIIL + r"|" + GOK_FIIL + r"[^.]{0,60}" + GOK, k, re.I):
        FIX.append(f"[{s}] I2V'de gök var ama HAREKETİ yok [HAVA_VE_ATMOSFER §1] — "
                   f"bulut/gök bir fiil alır: drift · streak · sweep · roll · hold")

# ── 10e. ⭐ MOTION FOCUS — 18.09.2026 · SAHNE_PLAN_KARTI · C1-a/c ──────────
# Çapraz analiz (QA/ARSIV_12_MERCEK/QA_CAPRAZ_ANALIZ): ② İNŞA 9/15, ⑩ SEBEP 4/5 filmde 4,0 altı.
# F01 · F05 · F08 aynı şeyin üç yüzü — malzemenin NEREDEN gelip HANGİ taşıyıcıyla
# NEREYE oturduğu I2V'de yazılı değildi. I2V'ye kendi paragrafında MOTION FOCUS
# girer (PROMPT_SABLONU §2). ⚠️ ÖLÇÜLMEDİ — bu yüzden FIX, BLOCK değil.
# ⛔ _blok() BURADA KULLANILMAZ: I2V nesrinde büyük harfli sonlandırıcı yok,
#    _blok() metnin sonuna kadar yakalar ve "from the north-east to the north-west"
#    gibi gök cümleleri kalıbı yanlış geçirir (165 I2V'de 128 yanlış geçiş ölçüldü).
#    Paragraf BOŞ SATIRA kadar okunur.
MF_KAYNAK_HEDEF = r"\bfrom\b.{3,200}?\b(onto|into|to|against|on)\b"
MF_ELEMAN = (r"\b(foundation|footing|column|pier|wall|beam|girder|slab|deck|roof|"
             r"truss|segment|floor)s?\b")
for s, k in i2v:
    m = re.search(r"(?:^|\n)MOTION FOCUS:(.*?)(?:\n\s*\n|\Z)", k, re.S)
    if not m:
        FIX.append(f"[{s}] I2V'de MOTION FOCUS paragrafı yok [PROMPT_SABLONU §2 · SAHNE_PLAN_KARTI · C1-c] — "
                   f"tek ana iş: malzeme NEREDEN, HANGİ taşıyıcıyla, NEREYE; yoksa iş adımı "
                   f"sonuç cümlesine döner ve ⑩ SEBEP 'MAGIC' verir")
        continue
    mf = m.group(1)
    if not re.search(MF_KAYNAK_HEDEF, mf, re.I | re.S):
        FIX.append(f"[{s}] MOTION FOCUS'ta kaynak→hedef yok [C1-c] — 'lifts … from the pile … "
                   f"onto the flange' kalıbı; beş sorunun ① ve ③'ü bu paragrafta yazılır")
    eleman = set(x.lower() for x in re.findall(MF_ELEMAN, mf, re.I))
    if len(eleman) >= 3:
        FIX.append(f"[{s}] MOTION FOCUS'ta {len(eleman)} yapı elemanı ({' · '.join(sorted(eleman))}) — "
                   f"tek klipte TEK ana iş [C1-c]; ikincisi sıvı büyümeye döner (F05), sahne bölünür")

# ── 10f. ⭐ TEKRAR EDEN ARIZALARIN KAPISI — 05.10.2026 · DERS 58-63 ──────────
# Yedi üretilmiş filmin (STAR DOCK · DEEP STEP · STONE TOWER · IRON BRIDGE ·
# GLASS CROSSING · MOUNTAIN CROWN · BACK TO PLUMB) kök neden analizi: arıza
# modelin keyfi değil, PROMPTUN KENDİSİYDİ. Aşağıdaki her kapı ölçülmüş bir
# arızaya bağlıdır. ⛔ Hepsi BLOCK: FIX'ler her planda "beklenen" iki uyarının
# yanında gürültüye döndü ve okunmadı.
_DIKEY = ("dikey_shorts" in yol or yol.endswith("_DIKEY_TIMELAPSE.md"))

# [DERS 58] DİKEY = 7 SAHNE × 8,0 SN — sahip kuralı, kesin (05.10.2026).
# 56,0 sn üretilir, 2x hızda (~28 sn sahne bloğu) paylaşılır. 6 ya da 8 sahne
# önerilmez; brief başka sayı verirse plan yine 7 ile yazılır ve bu söylenir.
DIKEY_SAHNE, DIKEY_SURE = 7, 8.0
if _DIKEY:
    if BEKLENEN != DIKEY_SAHNE or len(gorsel) != DIKEY_SAHNE:
        BLOCK.append(f"DİKEY SAHNE SAYISI {len(gorsel)} (Scene N of {BEKLENEN}) — dikey shorts KESİN "
                     f"{DIKEY_SAHNE} sahnedir [DERS 58 · sahip kuralı 05.10.2026]: {DIKEY_SAHNE} sahne "
                     f"görseli + usta kare G{DIKEY_SAHNE} + {DIKEY_SAHNE} I2V")
    if len(i2v) != DIKEY_SAHNE:
        BLOCK.append(f"DİKEY I2V SAYISI {len(i2v)} — {DIKEY_SAHNE} olmalı [DERS 58]")
    _iz = re.search(r"^IZGARA\s+(.*)$", metin, re.M)
    if not _iz or not re.search(rf"\b{DIKEY_SAHNE} sahne × 8,0 sn = 56,0 sn", _iz.group(1)):
        BLOCK.append(f"DİKEY künyede 'IZGARA     {DIKEY_SAHNE} sahne × 8,0 sn = 56,0 sn' satırı yok "
                     f"[DERS 58] — ızgara künyenin ilk satırlarında, kelimesi kelimesine")
    _dur = {x.replace(",", ".") for x in sureler}
    if _dur and _dur != {"8.0"}:
        BLOCK.append(f"DİKEY merdivende 8,0 dışı sahne süresi: {' · '.join(sorted(_dur))} [DERS 58]")
    _kl = _os.path.dirname(_os.path.abspath(yol))
    _gl = _os.path.join(_kl, f"{_os.path.basename(_kl)}_URETIM_GUNLUGU.md")
    if not _os.path.exists(_gl):
        BLOCK.append(f"DİKEY film klasöründe üretim günlüğü yok: {_os.path.basename(_gl)} [DERS 62 · 28] — "
                     f"yedi üretilmiş filmin altısı günlüksüz üretildi; pilot, zincir_kontrol ve final "
                     f"kanıtı için tek kayıt yok. Plan yazılırken açılır: "
                     f"cp dikey_shorts/URETIM_GUNLUGU_SABLONU.md {_os.path.relpath(_gl)}")
    if not re.search(r"PİLOT ÜÇLÜ", metin):
        BLOCK.append("DİKEY planda '## 🧪 PİLOT ÜÇLÜ' bölümü yok [DERS 62 · KILAVUZ_REHBERI §8 adım 2b] — "
                     "DEEP STEP ve STONE TOWER pilotsuz üretildi, ikisinde de en büyük parça "
                     "yöntemsiz belirdi. Bölüm: (a) referans GN · (b) ilk halka · (c) FİNAL klip "
                     f"S{DIKEY_SAHNE - 1} · + en büyük değişikliğin klibi")
    elif not re.search(rf"PİLOT ÜÇLÜ[\s\S]{{0,1500}}\bS{DIKEY_SAHNE - 1}\b", metin):
        BLOCK.append(f"PİLOT ÜÇLÜ final klibini (S{DIKEY_SAHNE - 1}) adıyla anmıyor [DERS 62] — "
                     f"final klibi her filmde pilottur (BACK TO PLUMB finali 4/10)")

# [C2-a…d] İZLEYİCİ KAPISI — 31 filmin ④ TESLİM okuması (05.10.2026). Satırın VARLIĞI
# denetlenir, içeriği değil: içerik konsept kapısında sahiple konuşulur.
if _DIKEY:
    for _satir, _neden in [("İŞLEV ANI", "son klipte ne ÇALIŞIYOR (yanar · açılır · akar) — ④ 9+ altı filmin altısı"),
                           ("AÇILIŞ NESNESİ", "G0'da 1 sn'de tanınan nesne + ona ne oluyor — kanca 9-10 kalıbı"),
                           ("DÖNGÜ KAFİYESİ", "G7 ↔ G0 aynı yer aynı biçim · işlev anı kadrajda kalır")]:
        if not re.search(rf"^\s*│?\s*{_satir}\b", metin, re.M):
            BLOCK.append(f"künyede '{_satir}:' satırı yok [C2 · KILAVUZ_REHBERI §6 İZLEYİCİ KAPISI] — {_neden}")
    # [C2-h] AÇILIŞ DÜZENİ — merak sorusu · eylem ilk karede · S0 rejimi
    if not re.search(r"^\s*│?\s*MERAK SORUSU\b", metin, re.M):
        BLOCK.append("künyede 'MERAK SORUSU:' satırı yok [C2-h · KILAVUZ_REHBERI §6 AÇILIŞ DÜZENİ] — izleyicinin "
                     "1. saniyede sorduğu ≤6 kelimelik soru ('Çimin altında ne var?'); final onu cevaplar")
    if i2v and not re.search(r"from the (very )?first frame", i2v[0][1], re.I):
        BLOCK.append(f"[{i2v[0][0]}] S0 I2V'si eylemi İLK KAREDE başlatmıyor [C2-h] — 2x'te S0 ekranda 4 sn; "
                     f"'From the first frame to about one second the crew …' ile nesneye dokunan eylem "
                     f"0. saniyede başlar, ısınma yok")
    if i2v and re.search(r"rejim\s+[CG]\b", i2v[0][0] or ""):
        FIX.append(f"[{i2v[0][0]}] S0 rejim C/G [C2-h] — açılışta hareket ilk saniyede görünmeli: A ya da B")
    # [C2-i] S0 GERİ ÇEKİLME AÇILIŞI — yalnız plan ✅ VAR diyorsa [KAMERA_HAREKETI §4.2]
    if re.search(r"^\s*│?\s*AÇILIŞ GERİ ÇEKİLMESİ\s+✅", metin, re.M):
        for _et in ("KAYNAK ÇÖZÜNÜRLÜĞÜ", "BÜYÜTME", "HEDEF AYRINTI"):
            if not re.search(rf"^\s*│?\s*{_et}\b", metin, re.M):
                BLOCK.append(f"AÇILIŞ GERİ ÇEKİLMESİ ✅ ama '{_et}' satırı yok [C2-i · KAMERA_HAREKETI §4.2]")
        _kc = re.search(r"^\s*│?\s*KAYNAK ÇÖZÜNÜRLÜĞÜ\s+(.*)$", metin, re.M)
        _bu = re.search(r"^\s*│?\s*BÜYÜTME\s+([0-9]+[.,][0-9]+)\s*×", metin, re.M)
        _tavan = None
        if _kc:
            _wh = re.search(r"([0-9]{3,5})\s*[×x]\s*([0-9]{3,5})", _kc.group(1))
            if _wh:
                _tavan = int(_wh.group(1)) / 1080
            else:
                FIX.append("KAYNAK ÇÖZÜNÜRLÜĞÜ ÖLÇÜLMEDİ [C2-i · araç kapısı ⑨] — plan yazılabilir, ÜRETİM "
                           "AÇILAMAZ: geri çekilmenin tavanı aracın gerçek piksel sayısından okunur")
        if _bu:
            _n = float(_bu.group(1).replace(",", "."))
            if _tavan is not None and _n > _tavan + 1e-9:
                BLOCK.append(f"BÜYÜTME {_n:g}× > YAKINLAŞMA TAVANI {_tavan:.2f}× [C2-i · KAMERA_HAREKETI §3.3] — "
                             f"kırpılan kare bulanıklaşır; upscale tavanı sağlamaz")
            if _n > 2.0:
                FIX.append(f"BÜYÜTME {_n:g}× > 2,0× [C2-i] — ayrıntı bağlamından kopar; 1,5–1,8× önerilir")
        if i2v and re.search(r"rejim\s+C\b", i2v[0][0] or ""):
            BLOCK.append("S0 rejim C'de geri çekilme açılışı [C2-i] — iş günü 8 sn'ye sıkışır, ışık hareketin "
                         "içinde döner (§3.2 ⑤)")
    # [C2-b] final klibi 4 sn olay + 4 sn tutuş — 2x'te tutuş ekranda 2 sn
    if i2v and not re.search(r"from (about )?four (seconds )?to (the )?eight(h)? seconds?|last four seconds|"
                             r"final four seconds", i2v[-1][1], re.I):
        BLOCK.append(f"[{i2v[-1][0]}] final I2V'si son dört saniyeyi TUTUŞ olarak yazmıyor [C2-b · §8 adım 9] — "
                     f"2x paylaşımda 8 sn'lik final 4 sn kalır; işlev anı 0-4 sn'de biter, 'from about four "
                     f"to eight seconds the lights stay on and nothing else changes' gibi bir cümle 4-8'i tutar")

# [DERS 59] YASAK KELİME — filmin kendi yasak listesi, NEGATİFTE BİLE geçmez.
# Ölçüldü: DEEP STEP'te "truck" yalnız metin yasağında geçti → modern kamyon;
# STAR DOCK'ta "plumes are invisible in vacuum" → alev; STONE TOWER'da "hoist"
# → vinç kancası; BACK TO PLUMB'da "render" → çatlak sıvandı. Kelimeyi anmak,
# "no"/"never"/"invisible" ile bile, nesneyi ÇAĞIRIR [DERS 33 · 35'in genel hâli].
_yk = re.search(r"^\s*│?\s*YASAK KELİME[^\n]*?[\s:]{2,}(.+)$", metin, re.M)
YASAK_LISTE = []
if not _yk:
    BLOCK.append("künyede 'YASAK KELİME' satırı yok [DERS 59] — filmin istemediği her nesne "
                 "(vinçsiz: crane · hoist · jib · derrick · tarihi: truck · machinery · Ay: flame · "
                 "smoke · thrust · plume) burada sayılır ve HİÇBİR promptta, negatifte bile geçmez. "
                 "Yasak yoksa: 'YASAK KELİME  — (yok)'")
else:
    YASAK_LISTE = [w.strip().lower() for w in re.split(r"[·,;/]", _yk.group(1))
                   if w.strip() and not w.strip().startswith(("—", "(", "⛔", "yok"))]
    if re.search(r"⛔ VİNÇ YOK|VİNÇSİZ", metin) and not {"crane", "hoist"} <= set(YASAK_LISTE):
        BLOCK.append("plan VİNÇSİZ beyan ediyor ama YASAK KELİME'de crane + hoist yok [DERS 59] — "
                     "STONE TOWER 'hoist' kelimesinden vinç kancası üretti")
for s, k in kareler + i2v:
    for w in YASAK_LISTE:
        m = re.search(rf"\b{re.escape(w)}(s|es)?\b", k, re.I)
        if m:
            bag = k[max(0, m.start() - 50):m.end() + 30].replace("\n", " ")
            BLOCK.append(f"[{s}] YASAK KELİME geçiyor: '{m.group(0)}' [DERS 59] — …{bag}…")

# [DERS 60] HAVASIZ SAHADA YANMA KELİMESİ YOK — su kapısının (A9-g) eşi.
YANMA = r"\b(flames?|fire|fiery|smoke|smoking|exhaust|plumes?|thrust|jets?|burn(s|ing)?|afterglow)\b"
for s, k in kareler + i2v:
    if not re.search(HAVASIZ, k, re.I):
        continue
    m = re.search(YANMA, k, re.I)
    if m:
        BLOCK.append(f"[{s}] HAVASIZ saha ama YANMA/İTKİ kelimesi var: '{m.group(0)}' [DERS 60] — "
                     f"STAR DOCK 'plumes are invisible in vacuum' yazdı, ekranda turuncu alev ve asılı "
                     f"duman çıktı. İniş yalnız etkisiyle yazılır: 'dust sprays outward in straight "
                     f"ballistic lines and falls at once'")

# [DERS 59] metin yasağı SAHADA OLMAYAN nesneyi adlandıramaz (§9 D-b'nin düzeltmesi).
for s, k in kareler:
    m = re.search(r"No readable text.*?(?:annotated by anyone|included\.)", k, re.S)
    if not m:
        continue
    yasak_cumle = m.group(0)
    govde = k.replace(yasak_cumle, " ")
    yok = sorted({y for y in YUZEY_METIN if re.search(rf"\b{re.escape(y)}s?\b", yasak_cumle, re.I)
                  and not re.search(rf"\b{re.escape(y)}s?\b", govde, re.I)})
    if yok:
        BLOCK.append(f"[{s}] metin yasağı SAHADA OLMAYAN nesneyi adlandırıyor: {', '.join(yok)} "
                     f"[DERS 59 · 35] — DEEP STEP'in antik kuyusuna 'truck' buradan girdi. Yasak "
                     f"yalnız bu karede GERÇEKTEN olan yüzeyleri sayar ya da yalnız 'on any surface' der")

# [DERS 61] FARK = HAREKET — G(n) ile G(n+1) arasında eklenen yapı elemanı,
# o klibin MOTION FOCUS'unda ADIYLA geçer. Ölçüldü: DEEP STEP'te kubbeler yalnız
# G5'te vardı, MOTION FOCUS taban kayasını anlatıyordu → kubbe tek karede bitmiş
# belirdi. STAR DOCK · STONE TOWER · BACK TO PLUMB aynı kök. Eleman adı ARA HÂL
# bloğundan (AT THIS STAGE / STAGE) okunur; STRUCTURE tam hâli karşılaştırılmaz.
# ⚠️ Liste BÜYÜK ve AYRIK elemanlardır. "wall · ring · tier · course · panel · tree"
# ilk koşuda deponun en iyi filmlerinde (LAST HARBOR · DEEP END) tarif kelimesi
# olarak geçti ve yanlış alarm verdi [DERS 10]; arıza büyük parçanın belirmesiydi.
YAPI_ADI = (r"\b(domes?|cupolas?|chhatris?|arch(es)?|vaults?|storeys?|stor(y|ies)|towers?|spires?|"
            r"roofs?|girders?|piers?|slabs?|cladding|cylinders?|truss(es)?|canop(y|ies)|staircases?|"
            r"terraces?|parapets?|lintels?|gates?|tanks?|chimneys?|masts?|sails?|hulls?|funnels?|"
            r"pylons?|kiosks?|pavilions?|balcon(y|ies)|bridges?|columns?|gantr(y|ies)|turrets?)\b")
GECICI_ADI = r"\b(scaffold(ing)?|ramps?|formwork|props?|shoring|falsework|planks?|cradles?)\b"

TASIYAN_FIIL = (r"\b(sets?|carr(y|ies)|lifts?|lowers?|places?|delivers?|brings?|rolls?|raises?|hoists?|"
                r"swings?|seats?|stacks?|bolts?|fits?|assembles?|pulls?|tows?|draws?|unloads?|erects?|"
                r"builds?|lays?|mortars?|beds?|winch(es)?)\b")

def _asama(k):
    m = re.search(r"AT THIS STAGE:?(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S) or \
        re.search(r"(?:^|\n)STAGE:(.*?)(?:\n[A-Z][A-Z /]+:|\Z)", k, re.S)
    return m.group(1) if m else ""

def _kok(w):
    w = w.lower()
    if w.endswith("ss"):
        return w
    for a, b in (("ies", "y"), ("ches", "ch"), ("sses", "ss"), ("es", "e"), ("s", "")):
        if w.endswith(a) and len(w) > len(a) + 1:
            return w[: -len(a)] + b
    return w

def _adlar(t, desen=YAPI_ADI):
    return {_kok(m.group(0)) for m in re.finditer(desen, t, re.I)}

if usta and len(i2v) == len(gorsel):
    for n, (s, k) in enumerate(i2v):
        a, b = _asama(kareler[n][1]), _asama(kareler[n + 1][1])
        if not a or not b:
            continue
        # G(n)'de GÖRÜNEN her şey: STRUCTURE tam hâli ve NEGATIVE hariç bütün prompt
        # (funnel · bridge · hull ilk karede COMPOSITION/SITE'ta zaten duruyor — yeni değil).
        _gn = re.sub(r"STRUCTURE:.*?(?=AT THIS STAGE)", " ", kareler[n][1], flags=re.S)
        _gn = re.sub(r"NEGATIVE:.*", " ", _gn, flags=re.S)
        mmf = re.search(r"(?:^|\n)MOTION FOCUS:(.*?)(?:\n\s*\n|\Z)", k, re.S)
        if not mmf:
            continue   # paragraf yokluğu §10e'de
        # MF + I2V'de TAŞIYICI FİİLLİ cümle (son-kare kilidi cümlesi hariç): "Late in the shot a
        # truck sets stacked arch segments on the quay" bir yöntemdir; "by the last frame the
        # cupolas stand" değildir (DEEP STEP — kubbe yalnız LAST KEYFRAME satırındaydı).
        _tasi = " ".join(c for c in re.split(r"(?<=[.;])\s+", k)
                         if re.search(TASIYAN_FIIL, c, re.I)
                         and not re.search(r"ends exactly on|last frame|by the end|LAST KEYFRAME", c, re.I))
        mf = (_adlar(mmf.group(1)) | _adlar(mmf.group(1), GECICI_ADI) | _adlar(_tasi) | _adlar(_tasi, GECICI_ADI))
        yeni = _adlar(b) - _adlar(_gn) - mf
        giden = (_adlar(a, GECICI_ADI) - _adlar(b, GECICI_ADI)) - mf
        if yeni:   # ⚠️ FIX: sezgisel — deponun en iyi filmlerinde de kelime farkıyla tetiklendi
            FIX.append(f"[{s}] G{n + 1}'de YENİ eleman var, MOTION FOCUS'ta YOK: {', '.join(sorted(yeni))} "
                         f"[DERS 61] — yöntemi yazılmayan eleman tek karede bitmiş belirir (DEEP STEP "
                         f"kubbeleri). MOTION FOCUS onu kaynak → taşıyıcı → hedef diye anar; anamıyorsan "
                         f"eleman bu klibe ait değildir, merdiven bölünür")
        if giden:   # ⚠️ INFO: LAST HARBOR · DEEP END sökümü MF'siz yazdı ve tuttu — kapı silme FİİLİNDE
            INFO.append(f"[{s}] G{n}'deki geçici ekipman G{n + 1}'de yok, sökümü MOTION FOCUS'ta adsız: "
                        f"{', '.join(sorted(giden))} — taşıyan yazılı mı? [DERS 61]")

# [DERS 61] silme FİİLİ yazılmaz — model 'vanish'i solarak yok etme diye okur.
# Yalnız İNŞAAT NESNESİ öznesiyle ve örtme olmadan: "the grey disappearing behind
# them" (VANISHING ROOM) · "its shadow vanishing" · "the bicycle frame vanishing"
# (su altına) meşrudur ve geçer.
SILME = r"\b(vanish(es|ed|ing)?|disappear(s|ed|ing)?)\b"
SILME_OZNE = (YAPI_ADI[:-3] + r"|scaffold(ing)?|planks?|poles?|props?|ramps?|formwork|steel|tools?|"
              r"debris|rubble|blocks?|stones?|bricks?|panels?|walls?|bundles?|pallets?|wheelbarrows?)\b")
ORTME = r"^\W{0,3}\w*\W{0,3}(behind|under|beneath|below|into|inside)\b"
for s, k in kareler + i2v:
    for m in re.finditer(SILME, k, re.I):
        onceki = k[max(0, m.start() - 80):m.start()]
        if re.search(r"\b(no|never|nothing|without|not)\b[^.]*$", onceki, re.I):
            continue
        if re.search(ORTME, k[m.end():m.end() + 30], re.I):
            continue
        if not re.search(SILME_OZNE, onceki.split(".")[-1], re.I):
            continue
        BLOCK.append(f"[{s}] SİLME FİİLİ inşaat nesnesine: '{m.group(0)}' [DERS 61] — STONE TOWER 'poles, "
                     f"planks… vanish' yazdı, STAR DOCK 'the open steel disappears'; ikisinde de nesne solarak "
                     f"belirdi/kayboldu. Yerine taşıyan yazılır: 'workers carry the planks down the ramp and "
                     f"stack them on the cart'")

# [C2-g] MALZEME AKIŞI — I2V'de kaynak → taşıyan (usta kare klibi hariç: final ödülü işlevdir)
KAYNAK = r"\b(pile|stack|stockpile|heap|truck|lorry|crates?|pallets?|bundles?|barge|trailer|cart|skip|rolls?)\b"
for _j, (s, k) in enumerate(i2v):
    if _j == len(i2v) - 1:
        continue
    if not any(re.search(KAYNAK, c, re.I) and re.search(TASIYAN_FIIL, c, re.I)
               for c in re.split(r"(?<=[.;])\s+", k)):
        FIX.append(f"[{s}] I2V'de görünür MALZEME AKIŞI yok [C2-g · SANTIYE_HAREKETI §4.8 ②] — kaynak (istif · "
                   f"kamyon · sandık) → taşıyan → hedef; istif klipten klibe azalır")

# ── 13. uzunluk ────────────────────────────────────────────────────────────
for s, k in kareler:
    n = len(k)
    # Band ölçüme göre açıldı: negatif çekirdek tek başına ~1.500 karakter tutuyor
    # ve YAPI BIBLE + çapa bloğu birebir tekrarlandığı için taban zaten yüksek.
    if n < 2000:
        FIX.append(f"[{s}] görsel prompt kısa ({n} karakter · band 2000-6000)")
    elif n > 6000:
        FIX.append(f"[{s}] görsel prompt uzun ({n} karakter · band 2000-6000)")
    else:
        INFO.append(f"[{s}] {n} karakter")

# ── rapor ──────────────────────────────────────────────────────────────────
for baslik, liste, isaret in [("BLOCK", BLOCK, "⛔"), ("FIX", FIX, "⚠️")]:
    if liste:
        print(f"{isaret} {baslik} — {len(liste)}")
        for x in liste:
            print(f"   {isaret} {x}")
        print()

if INFO:
    print("ℹ️  bilgi (uzunluk · süre dağılımı · kalabalık)")
    for x in INFO:
        print(f"   {x}")
    print()

if BLOCK:
    print("SONUÇ: ⛔ BLOCK — ÜRETME")
    sys.exit(2)
if FIX:
    print("SONUÇ: ⚠️ FIX — düzelt, sonra üret")
    sys.exit(1)
print("SONUÇ: ✅ GO")
sys.exit(0)
