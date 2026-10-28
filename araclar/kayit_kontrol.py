#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
#  KAYIT KONTROL — QA kaydı kanıtına dayanıyor mu  [DENETİM 28.10.2026]
#
#  NEDEN VAR (28.10.2026):
#  Aynı arıza 12 günde on filmde tekrarlandı ve her seferinde bir ders yazıldı
#  (DERS 90 · 100 · 105 · 106): mercekler ölçülmüş olgular bloğu BOŞ koşuldu,
#  klip ızgarası uydurdu, rapor TAM ya da 10/10 kaydedildi. QA/KOSU/ hiç
#  oluşmadı — yani hiçbir koşu qa_paket.sh paketiyle yapılmadı. Kural yazılıydı;
#  kaydı kanıta karşı tutan bir adım yoktu [DERS 12: yazılı yordam koşmaz].
#  Ayrıca kayıtların "plandan cevap" bölümü planda olmayan sayılar yazdı
#  (SUNKEN GARDEN K2 havuz ölçüsü · DRIVE IN güneş açıları) ve üç kayıt yerel
#  dosya varken "AJAN OKUYAMADI" dedi.
#
#  KULLANIM
#     python3 araclar/kayit_kontrol.py                 bütün filmler — özet + kapı ihlalleri
#     python3 araclar/kayit_kontrol.py <FILM> [...]    o filmin ham raporları + kaydı, ayrıntılı
#     python3 araclar/kayit_kontrol.py --staged        commit kancası: yalnız sahnelenmiş dosyalar
#
#  ⛔ KAPI (çıkış 2) — 28.10.2026 ve sonrası tarihli ham raporda, durum TAM ise:
#     K1 künyede "paket:" satırı yok — qa_paket.sh paketiyle koşulmamış [DERS 90 · 105 · 106]
#     K2 paket dosyası diskte yok · ya da paketteki dosya sha256'sı künyedekiyle tutmuyor
#     K3 model çıktısında doldurulmamış yer tutucu ({SPEED} …) ya da RUN INVALID
#     K4 CLIPS YOU CAN SEE ölçülen klip sayısından farklı (kart +1 uyarıdır) [DERS 105 ② · 106 ②]
#     her tarihte: künyesiz yeni ham · QA/HAM ya da arşiv hamı DEĞİŞTİ/SİLİNDİ (--staged) ·
#     TABLO ↔ HAM klasörü (U1 · U2)
#  ⚠️ UYARI (çıkış 0) — kayıtta "plandan cevap" sayısı film klasöründe geçmiyor · "AJAN OKUYAMADI"
#     ama yayın dosyası yerelde · paket --ihracsiz · kart +1 · 28.10.2026 öncesi hamlarda K1–K4
#     (kapı öncesi — engellemez, sayılır)
# ═══════════════════════════════════════════════════════════════════
import datetime as dt
import glob
import os
import re
import subprocess
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(KOK, "araclar"))
from plan_oku import oku, PlanOkunamadi  # noqa: E402

KAPI_TARIHI = dt.date(2026, 10, 28)
YER_TUTUCU = re.compile(r"\{(SPEED|CLIP_COUNT|CLIP_SECONDS|CUTS|END_CARD|MUSIC|ASPECT|DURATION|FINAL_HOLD)\}")
KORUNAN = ("QA/HAM/", "QA/ARSIV_12_MERCEK/HAM_RAPORLAR/")

KAPI, UYARI, ONCESI = [], [], []          # ONCESI: (film, ad, kod, ileti)
TAM_SAYI = {}


def oku_metin(yol, staged=False):
    if staged:
        r = subprocess.run(["git", "show", f":{yol}"], cwd=KOK, capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout
    with open(os.path.join(KOK, yol), encoding="utf-8") as f:
        return f.read()


def plan_yolu(film):
    adaylar = [f"dikey_shorts/{film}/{film}_DIKEY_TIMELAPSE.md"] + \
        sorted(glob.glob(os.path.join(KOK, f"yatay_*_dk_filmler/{film}/{film}_PLAN.md")))
    for p in adaylar:
        p = os.path.relpath(os.path.join(KOK, p), KOK)
        if os.path.exists(os.path.join(KOK, p)):
            return p
    return None


def kunye(metin):
    """İlk '---' çiti arasındaki alanlar + çitin altı (model çıktısı)."""
    m = re.match(r"\s*---\n(.*?)\n---\n(.*)", metin, re.S)
    if not m:
        return None, metin
    alan = {}
    for l in m.group(1).splitlines():
        a = re.match(r"^([a-zçğıöşü_]+):\s*(.*)$", l)
        if a:
            alan[a.group(1)] = a.group(2).strip()
    return alan, m.group(2)


def tarih(s):
    m = re.search(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", s or "")
    return dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None


def ham_denetle(yol, staged=False):
    metin = oku_metin(yol, staged)
    film = yol.split("/")[2]
    ad = os.path.basename(yol)
    alan, cikti = kunye(metin)
    if alan is None:
        if staged:
            KAPI.append(f"{ad}: künye yok (QA_KAYIT §2.1)")
        else:
            ONCESI.append((film, ad, "künye", f"{ad}: künye yok (QA_KAYIT §2.1)"))
        return
    t = tarih(alan.get("tarih"))
    kapida = t is None or t >= KAPI_TARIHI
    durum = alan.get("durum", "")
    if not durum.startswith("TAM"):
        return
    TAM_SAYI[film] = TAM_SAYI.get(film, 0) + 1

    def hedef_ekle(kod, ileti):
        if kapida:
            KAPI.append(ileti)
        else:
            ONCESI.append((film, ad, kod, ileti))

    # K3 — model boş blok gördü
    if YER_TUTUCU.search(cikti) or "RUN INVALID" in cikti:
        hedef_ekle("K3", f"{ad}: TAM ama model çıktısı boş blok gösteriyor (yer tutucu yankısı / RUN INVALID) [K3]")

    # ölçülen klip sayısı: paket → plan
    paket = alan.get("paket", "")
    paket_yolu = paket.split(" · ")[0].strip() if paket else ""
    olculen = None
    if not paket:
        hedef_ekle("K1", f"{ad}: TAM ama künyede 'paket:' yok — qa_paket.sh paketiyle koşulmamış [K1 · DERS 90 · 105]")
    elif not os.path.exists(os.path.join(KOK, paket_yolu)):
        hedef_ekle("K2", f"{ad}: paket diskte yok: {paket_yolu} — aynı dosyayla qa_paket.sh yeniden koşulur [K2]")
    else:
        p = open(os.path.join(KOK, paket_yolu), encoding="utf-8").read()
        sha_p = re.search(r"^dosya:.*?sha256 ([0-9a-f]{12})", p, re.M)
        sha_h = re.search(r"sha256 ([0-9a-f]{12})", alan.get("dosya", ""))
        if not sha_p or not sha_h or sha_p.group(1) != sha_h.group(1):
            hedef_ekle("K2", f"{ad}: paketteki dosya sha256'sı künyedekiyle tutmuyor — mercek başka dosyayı gördü [K2]")
        m = re.search(r"^CLIP COUNT\s+(\d+)", p, re.M)
        olculen = int(m.group(1)) if m else None
        if "--ihracsiz" in paket or "--ihracsiz" in p:
            UYARI.append(f"{ad}: paket --ihracsiz ile açılmış — bu dosya şu hâliyle paylaşılmaz")
    if olculen is None:
        pl = plan_yolu(film)
        try:
            olculen = len(oku(os.path.join(KOK, pl))["sureler"]) if pl else None
        except PlanOkunamadi:
            olculen = None
        if olculen and re.search(r"_B[12]_", ad):
            olculen //= 2

    # K4 — D2
    m = re.search(r"CLIPS YOU CAN SEE:\s*\**\s*(\d+)", cikti)
    if m and olculen:
        g = int(m.group(1))
        if g == olculen + 1:
            UYARI.append(f"{ad}: CLIPS YOU CAN SEE {g} = ölçülen {olculen} + 1 — kartı klip saymış olabilir")
        elif g != olculen:
            hedef_ekle("K4", f"{ad}: TAM ama CLIPS YOU CAN SEE {g} ≠ ölçülen {olculen} — yeniden koşulur [K4 · D2 · DERS 105 ②]")


def u1_u2():
    tablo = open(os.path.join(KOK, "QA/TABLO.md"), encoding="utf-8").read()
    bolum = tablo.split("## FİLM × MERCEK", 1)[-1]
    satirlar = re.findall(r"^\| ([^|]+?) \|", bolum, re.M)
    filmler = {s.strip().replace(" ", "_") for s in satirlar
               if s.strip() not in ("film",) and not set(s.strip()) <= set(":-")}
    hamlar = {os.path.basename(d.rstrip("/")) for d in glob.glob(os.path.join(KOK, "QA/HAM/*/"))}
    for f in sorted(hamlar - filmler):
        KAPI.append(f"U1 {f}: ham rapor var, TABLO'da satır yok")
    for f in sorted(filmler - hamlar):
        KAPI.append(f"U2 {f}: TABLO'da satır var, ham klasörü yok")


SAYI = re.compile(r"\d+(?:[.,]\d+)?\s*[×x]\s*\d+(?:[.,]\d+)?(?:\s*m\b)?"     # ölçü: 10×4,5 m · 2×6
                  r"|\d+(?:[.,]\d+)?\s*°"                                       # açı: 63°
                  r"|\b\d{1,2}:\d{2}(?::\d{2})?\b"                              # saat: 12:45
                  r"|\b\d+(?:[.,]\d+)?\s*(?:m|cm|mm|km|kg|ton|m²)\b")           # birim: 20 m


def _desen(tok):
    tok = tok.strip()
    parcalar = re.split(r"(\d+(?:[.,]\d+)?)", tok)
    d = ""
    for p in parcalar:
        if re.fullmatch(r"\d+(?:[.,]\d+)?", p):
            d += r"(?<![\d.,])" + re.sub(r"[.,]", r"[.,]", p) + r"(?:[.,]0+)?(?![\d])" if "," not in p and "." not in p \
                else r"(?<![\d.,])" + re.sub(r"[.,]", r"[.,]", p)
        elif p.strip() in ("×", "x"):
            d += r"\s*[×x]\s*"
        elif p.strip():
            d += r"\s*" + re.escape(p.strip())
    return d


def kayit_denetle(film, staged=False):
    yol = f"QA/FILMLER/{film}.md"
    if not os.path.exists(os.path.join(KOK, yol)):
        return
    metin = oku_metin(yol, staged)
    klasor = os.path.dirname(plan_yolu(film) or "")
    belge = ""
    if klasor:
        for f in glob.glob(os.path.join(KOK, klasor, "*.md")):
            belge += open(f, encoding="utf-8").read() + "\n"
    if belge:
        for no, l in enumerate(metin.splitlines(), 1):
            if not re.search(r"plandan cevap", l, re.I):
                continue
            eksik = []
            govde = l.split(":", 1)[-1]
            for m in SAYI.finditer(govde):
                tok, sonra = m.group(0).strip(), govde[m.end():m.end() + 8]
                if re.fullmatch(r"\d:\d{2}", tok):                      # video damgası (m:ss), plan sayısı değil
                    continue
                if re.match(r"\d+x\s", tok) or re.match(r"\s*(sn|saniye)\b", sonra):   # hız (2x …) · süre (… sn)
                    continue
                if tok not in eksik and not re.search(_desen(tok), belge):
                    eksik.append(tok)
            if eksik:
                UYARI.append(f"{yol}:{no} plandan cevapta film klasöründe geçmeyen sayı: "
                             f"{' · '.join(sorted(eksik))} — planda yoksa 'planda yok' yazılır [K6]")
    if re.search(r"AJAN OKUYAMADI", metin):
        for aday in (os.path.join(KOK, "teslim", f"{film}.mp4"),
                     os.path.expanduser(f"~/Downloads/{film}.mp4")):
            if os.path.exists(aday):
                UYARI.append(f"{yol}: 'AJAN OKUYAMADI' yazıyor ama yayın dosyası yerelde: {aday} — "
                             f"kart R 2b ajan ölçümü yapılır")
                break


def staged_mod():
    r = subprocess.run(["git", "diff", "--cached", "--name-status", "-M"], cwd=KOK,
                       capture_output=True, text=True)
    qa_var = False
    for satir in r.stdout.splitlines():
        p = satir.split("\t")
        kod, yollar = p[0], p[1:]
        yol = yollar[-1]
        if any(y.startswith("QA/") for y in yollar):
            qa_var = True
        for y in yollar:
            if y.startswith(KORUNAN) and not y.endswith("00_README.md") and kod[0] in "MDR":
                KAPI.append(f"{y}: ham rapor {'silindi' if kod[0] == 'D' else 'değişti'} — HAM DOKUNULMAZ; "
                            f"yeniden koşu _K2 olarak yeni dosyaya yazılır [QA_KAYIT §3]")
        if kod[0] in "AC" and yol.startswith("QA/HAM/") and re.search(r"_HAM(_K\d+)?\.md$", yol):
            ham_denetle(yol, staged=True)
        if kod[0] in "AMR" and yol.startswith("QA/FILMLER/") and not yol.endswith("00_README.md"):
            kayit_denetle(os.path.basename(yol)[:-3], staged=True)
    if qa_var:
        u1_u2()
    return qa_var


def main(argv):
    staged = "--staged" in argv
    filmler = [a for a in argv[1:] if not a.startswith("--")]
    print("═══════════════════════════════════════════════════════")
    print(f"  KAYIT KONTROL · {'sahnelenmiş dosyalar' if staged else (' · '.join(filmler) or 'bütün filmler')}"
          f" · kapı tarihi {KAPI_TARIHI:%d.%m.%Y}")
    print("═══════════════════════════════════════════════════════")
    if staged:
        if not staged_mod():
            print("  QA dosyası sahnelenmemiş — denetlenecek kayıt yok.")
            return 0
    else:
        hepsi = sorted(os.path.basename(d.rstrip("/")) for d in glob.glob(os.path.join(KOK, "QA/HAM/*/")))
        for film in (filmler or hepsi):
            for h in sorted(glob.glob(os.path.join(KOK, f"QA/HAM/{film}/*_HAM*.md"))):
                ham_denetle(os.path.relpath(h, KOK))
            kayit_denetle(film)
        u1_u2()

    for baslik, liste, isaret in [("KAPI — bu kayıt böyle girmez", KAPI, "⛔"), ("UYARI", UYARI, "⚠️")]:
        if liste:
            print(f"\n{isaret} {baslik} · {len(liste)}")
            for x in liste:
                print(f"   {isaret} {x}")
    if ONCESI:
        print(f"\nℹ️ KAPI ÖNCESİ (< {KAPI_TARIHI:%d.%m.%Y}) — TAM sayılmış ama kanıta bağlanamayan koşular · engellemez")
        if filmler:
            for _, _, _, x in ONCESI:
                print(f"   ℹ️ {x}")
        else:
            print(f"   {'film':<22} {'TAM':>4} {'paketsiz':>9} {'boş blok':>9} {'klip≠ölçülen':>13}")
            for film in sorted({f for f, _, _, _ in ONCESI}):
                say = lambda k: len({a for f, a, kk, _ in ONCESI if f == film and kk == k})
                print(f"   {film:<22} {TAM_SAYI.get(film, 0):>4} {say('K1'):>9} {say('K3'):>9} {say('K4'):>13}")
            print("   (satır satır: python3 araclar/kayit_kontrol.py <FILM>)")
    print()
    if KAPI:
        print("SONUÇ: ⛔ KAYIT KANITA DAYANMIYOR — düzeltilmeden kayda/commit'e girmez")
        if staged:
            print("   Bile bile geçmek: git commit --no-verify  (yalnız sahip — kayda gerekçe yazılır)")
        return 2
    print("SONUÇ: ✅ kapı ihlali yok" + (f" · {len(UYARI)} uyarı" if UYARI else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
