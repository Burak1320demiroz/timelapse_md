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
        if satir.startswith("## "):
            sahne = satir[3:].strip()
            tip = None
        elif satir.startswith("### "):
            tip = satir[4:].strip()
    return cikti


# ── yükleme ────────────────────────────────────────────────────────────────
if len(sys.argv) < 2:
    print("kullanım: prompt_kontrol.py <film.md>")
    sys.exit(2)

yol = sys.argv[1]
metin = open(yol, encoding="utf-8").read()
bloklar = blok_ayikla(metin)

gorsel = [(s, k) for s, t, k in bloklar
          if t and "GÖRSEL PROMPT" in t and "KAPAK" not in t and "KAPAK" not in (s or "")]
i2v = [(s, k) for s, t, k in bloklar if t and "I2V" in t]
t2v = [(s, k) for s, t, k in bloklar if t and "T2V" in t]

print("═" * 62)
print(f"  PROMPT KONTROL · {yol.split('/')[-1]}")
print("═" * 62)
print(f"  görsel prompt {len(gorsel)}  ·  I2V {len(i2v)}  ·  T2V {len(t2v)}")
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
    BLOCK.append(f"I2V sayısı görsel sayısına eşit değil ({len(i2v)} ≠ {len(gorsel)})")

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
for s, k in gorsel:
    m = re.search(r"STRUCTURE:(.*?)(AT THIS STAGE)", k, re.S)
    if not m:
        BLOCK.append(f"[{s}] STRUCTURE bloğu ya da 'AT THIS STAGE' ayracı yok")
        continue
    bibles.setdefault(normalize(m.group(1)), []).append(s)
if len(bibles) > 1:
    BLOCK.append(
        "YAPI BIBLE altı promptta BİREBİR aynı değil — "
        + str(len(bibles))
        + " farklı sürüm var: "
        + " | ".join(", ".join(v)[:60] for v in bibles.values())
    )

# ── 4. arka plan çapaları ──────────────────────────────────────────────────
ANA = "MAIN STATION"
siteler_ana, detay_site, capa_eksik = {}, [], []
for s, k in gorsel:
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
for s, k in gorsel:
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
for s, k in gorsel:
    if not re.search(r"azimuth\s+\d+", k) or not re.search(r"elevation\s+\d+", k):
        BLOCK.append(f"[{s}] güneş satırı eksik (azimuth + elevation dereceyle yazılmalı)")

# ── 7. köşeli parantez atfı ────────────────────────────────────────────────
for s, k in gorsel + i2v + t2v:
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
for s, k in gorsel:
    for ad, desen in IMZA:
        if not re.search(desen, k):
            BLOCK.append(f"[{s}] negatif çekirdek imzası eksik: {ad}")

# ── 9. metin yasağının KAPSAMI [D-b] ───────────────────────────────────────
YUZEY = ["hoarding", "signage", "machinery", "container", "vest", "helmet",
         "truck", "scaffolding", "facade", "billboard", "licence plate",
         "shop front", "street plate", "formwork", "crane"]
for s, k in gorsel:
    m = re.search(r"No readable text.*?annotated by anyone", k, re.S)
    if not m:
        continue
    sayi = sum(1 for y in YUZEY if y in m.group(0).lower())
    if sayi < 8:
        FIX.append(f"[{s}] metin yasağı KAPSAMSIZ — yalnız {sayi} yüzey sayılmış (en az 8) [D-b]")

# ── 10. render çukuru + insan kuralı + ZAMAN HIZI ──────────────────────────
for s, k in gorsel:
    if "SITE TEXTURE" not in k:
        FIX.append(f"[{s}] SITE TEXTURE bloğu yok — emlak render'ı riski [§9.1]")
    if "motion streaks" not in k:
        FIX.append(f"[{s}] insan kuralı yok ('soft motion streaks') [§9.4]")
    # [DERS 15] hız tek cümlede ve TÜM öznelere birden yazılır
    if not re.search(r"time-lapsed at the same rate", k):
        BLOCK.append(f"[{s}] TIME RATE bloğu yok [DERS 15] — model gökyüzünü "
                     f"hızlandırıp yeri gerçek zamanda bırakıyor. Tek cümle, "
                     f"tüm özneler: bulut · gölge · makine · insan · araç.")

# ── 10b. RİTİM ve MEVSİM TAŞIYICISI — plan seviyesi denetimleri ────────────
if "MEVSİM TAŞIYICISI" not in metin:
    BLOCK.append("AŞAMA MERDİVENİNDE 'MEVSİM TAŞIYICISI' sütunu yok [DERS 14] — "
                 "taşıyıcısı olmayan sahne zamanı durdurur ve film süresini "
                 "olduğundan kısa okutur.")

# Süre sütunu: on sahnenin süresi EŞİTSE ⑥ merceği METRONOM hükmü verir.
sureler = re.findall(r"^\|\s*\d\s*\|\s*([0-9]+(?:[.,][0-9]+)?)\s*\|", metin, re.M)
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
for s, k in gorsel:
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
for s, k in gorsel + i2v + t2v:
    for m in re.finditer(HAREKET, k, re.I):
        onceki = k[max(0, m.start() - 40):m.start()].lower()
        sonraki = k[m.end():m.end() + 24].lower()
        # "tilt 0 degrees" / "tilted 8 degrees down" bir SPESİFİKASYONDUR
        if re.match(r"\s*(-?\d+([.,]\d+)?)\s*(degrees|derece)", sonraki):
            continue
        if not re.search(r"\b(no|never|zero|without)\b[^.]*$", onceki):
            FIX.append(f"[{s}] olumlu kamera hareketi kelimesi: '{m.group(0)}' — bağlamı kontrol et")

# ── 13. uzunluk ────────────────────────────────────────────────────────────
for s, k in gorsel:
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
