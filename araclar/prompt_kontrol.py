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
for s, k in kareler:
    m = re.search(r"No readable text.*?annotated by anyone", k, re.S)
    if not m:
        continue
    sayi = sum(1 for y in YUZEY if y in m.group(0).lower())
    if sayi < 8:
        FIX.append(f"[{s}] metin yasağı KAPSAMSIZ — yalnız {sayi} yüzey sayılmış (en az 8) [D-b]")

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
    if "motion streaks" not in k and not insansiz:
        FIX.append(f"[{s}] insan kuralı yok ('soft motion streaks') [§9.4]")
    # [DERS 15] hız tek cümlede ve TÜM öznelere birden yazılır
    if not re.search(r"time-lapsed at the same rate", k):
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
REJIM = r"ten minutes pass|two hours pass|a full working day passes|working day passes"
REJIM_C = r"(a full )?working day passes"
for s, k in kareler + i2v:
    if re.search(r"time-lapsed at the same rate", k) and not re.search(REJIM, k, re.I):
        FIX.append(f"[{s}] TIME RATE var ama SIKIŞTIRMA REJİMİ penceresi yok "
                   f"[SANTIYE_HAREKETI §2] — 'ten minutes pass' / 'two hours pass' / "
                   f"'a full working day passes' üçünden biri yazılır; yoksa model "
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

# Süre sütunu: on sahnenin süresi EŞİTSE ⑥ merceği METRONOM hükmü verir.
# ⚠️ 08.09.2026: desen ondalık İSTER. Eskisi "| 0 | 20 | ilkbahar |" gibi
# her tabloyu SÜRE sütunu sanıyordu ve Mars filminin güneş saati tablosunu
# ızgaraya karıştırdı. kesme_kontrol.sh zaten ondalık arıyordu — iki araç
# aynı deseni kullanır.
sureler = re.findall(r"^\|\s*\d\s*\|\s*([0-9]+[.,][0-9]+)\s*\|", metin, re.M)
if len(sureler) >= 6:
    benzersiz = {x.replace(",", ".") for x in sureler}
    if len(benzersiz) == 1:
        BLOCK.append(f"AŞAMA MERDİVENİNDE bütün sahne süreleri aynı ({sureler[0]}) "
                     f"[DERS 13] — eşit aralıklı kesme dizisi tempo değil NABIZ "
                     f"üretir ve ⑥ merceği METRONOM hükmü verir. En az iki sahne "
                     f"KISA, en az bir sahne UZUN olmalı (ölçüye oturarak).")
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
    print("ℹ️  prompt uzunlukları")
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
