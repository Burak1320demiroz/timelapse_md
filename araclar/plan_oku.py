#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
#  PLAN OKU — planın sahne sürelerini TEK yerden okur  [DENETİM 28.10.2026 · A1]
#
#  NEDEN VAR (28.10.2026):
#  kesme_kontrol.sh ile qa_paket.sh sahne satırını ayrı ayrı, aynı dar desenle
#  okuyordu ("| 2 | 8,0 |"). İki zincirli sahne "| 2 | 8,0 (4+4) |" yazılır ve
#  desene uymaz: LIT AGAIN 4 sahne, OPENING NIGHT 6 sahne okundu (ikisi de 8);
#  FIRST SLICE · MENDED SPAN · HIDDEN LAWN 6 okundu (hepsi 8). qa_paket koşulsaydı
#  merceğe YANLIŞ klip sayısı giderdi — boş bloktan daha tehlikeli, çünkü mercek
#  bloğa güvenir. Tablo ile beyanı karşılaştıran hiçbir adım yoktu.
#
#  KULLANIM
#     python3 araclar/plan_oku.py <plan.md> [--sureler | --sayi | --blok | --ozet]
#     --sureler  her sahnenin süresi (sn @1x), satır başına bir, nokta ondalık — varsayılan
#     --sayi     sahne sayısı
#     --blok     sahne bloğu (sn @1x)
#     --ozet     kaynak · sayı · blok · uyarılar (insan için)
#     Python'dan: sys.path'e araclar/ eklenir → from plan_oku import oku
#
#  OKUMA SIRASI
#     1. AŞAMA MERDİVENİ satırları "| S | SÜRE | …" — SÜRE "8,0" ya da "8,0 (4+4)".
#        Aynı sahne numarası ikinci kez gelirse ikinci tablo başlamıştır: okunmaz.
#     2. Tablo yoksa "SAHNE BLOĞU  N sahne × D sn = T sn" beyanı (düz ızgara).
#     ⛔ Beyan varsa tablo ona karşı DOĞRULANIR: sayı ya da toplam tutmuyorsa DURUR.
#
#  ÇIKIŞ: 0 = okundu · 2 = okunamadı ya da tablo ↔ beyan çelişkili (hata stderr'e)
# ═══════════════════════════════════════════════════════════════════
import re
import sys

SATIR = re.compile(r"^\|\s*(\d+)\s*\|\s*(\d+[.,]\d+)(?:\s*\([^)|]*\))?\s*\|")
BEYAN_SATIRI = re.compile(r"^SAHNE BLOĞU\b.*$", re.M)


class PlanOkunamadi(Exception):
    pass


def _sayi(s):
    return float(s.replace(",", "."))


def oku(yol):
    """{'sureler': [...], 'kaynak': 'tablo'|'beyan', 'beyan': satır|None, 'uyarilar': [...]}"""
    metin = open(yol, encoding="utf-8").read()
    satirlar, gorulen, uyarilar = [], set(), []
    for l in metin.splitlines():
        m = SATIR.match(l)
        if not m:
            continue
        no = int(m.group(1))
        if no in gorulen:          # ikinci tablo başladı
            break
        gorulen.add(no)
        satirlar.append((no, _sayi(m.group(2))))

    beyan = BEYAN_SATIRI.search(metin)
    b_sayi = b_sure = b_toplam = None
    if beyan:
        b = beyan.group(0)
        m = re.search(r"(\d+)\s*(?:sahne|klip)", b)
        b_sayi = int(m.group(1)) if m else None
        m = re.search(r"[×x]\s*(\d+[.,]\d+)\s*sn", b)
        b_sure = _sayi(m.group(1)) if m else None
        m = re.search(r"=\s*(\d+[.,]\d+)\s*sn", b)
        b_toplam = _sayi(m.group(1)) if m else None

    if satirlar:
        nolar = [n for n, _ in satirlar]
        if nolar != list(range(nolar[0], nolar[0] + len(nolar))):
            uyarilar.append(f"sahne numaraları ardışık değil: {nolar}")
        sureler = [s for _, s in satirlar]
        if b_sayi is not None and b_sayi != len(sureler):
            raise PlanOkunamadi(f"tablo {len(sureler)} sahne okudu, SAHNE BLOĞU {b_sayi} diyor — "
                                f"hangisi doğru, plan düzeltilmeden ölçülmez")
        if b_toplam is not None and abs(sum(sureler) - b_toplam) > 0.05:
            raise PlanOkunamadi(f"tablo toplamı {sum(sureler):g} sn, SAHNE BLOĞU {b_toplam:g} sn diyor")
        if beyan is None:
            uyarilar.append("SAHNE BLOĞU beyanı yok — tablo doğrulanamadı")
        kaynak = "tablo"
    elif b_sayi and (b_sure or b_toplam):
        d = b_sure if b_sure else b_toplam / b_sayi
        if b_sure and b_toplam and abs(b_sayi * b_sure - b_toplam) > 0.05:
            raise PlanOkunamadi(f"SAHNE BLOĞU kendi içinde tutmuyor: {b_sayi} × {b_sure:g} ≠ {b_toplam:g}")
        if not b_sure:
            uyarilar.append("SAHNE BLOĞU süre vermiyor — sahneler EŞİT varsayıldı")
        sureler = [d] * b_sayi
        kaynak = "beyan"
        uyarilar.append("planda '| S | SÜRE |' satırı yok — süreler SAHNE BLOĞU beyanından (düz ızgara)")
    else:
        raise PlanOkunamadi("ne '| S | SÜRE |' satırı ne 'SAHNE BLOĞU N sahne × D sn = T sn' beyanı okunabildi")

    return {"sureler": sureler, "kaynak": kaynak,
            "beyan": beyan.group(0).strip() if beyan else None, "uyarilar": uyarilar}


def main(argv):
    if len(argv) < 2:
        print(open(__file__, encoding="utf-8").read().split("KULLANIM")[1].split("OKUMA SIRASI")[0])
        return 2
    yol, kip = argv[1], (argv[2] if len(argv) > 2 else "--sureler")
    try:
        p = oku(yol)
    except (OSError, PlanOkunamadi) as h:
        print(f"⛔ plan okunamadı: {yol} — {h}", file=sys.stderr)
        return 2
    s = p["sureler"]
    if kip == "--sureler":
        print("\n".join(f"{x:g}" for x in s))
    elif kip == "--sayi":
        print(len(s))
    elif kip == "--blok":
        print(f"{sum(s):.2f}")
    elif kip == "--ozet":
        print(f"  plan    {yol}")
        print(f"  kaynak  {p['kaynak']} · {len(s)} sahne · blok {sum(s):g} sn · süreler {'·'.join(f'{x:g}' for x in s)}")
        if p["beyan"]:
            print(f"  beyan   {p['beyan']}")
        for u in p["uyarilar"]:
            print(f"  ⚠️ {u}")
    else:
        print(f"⛔ bilinmeyen kip: {kip}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
