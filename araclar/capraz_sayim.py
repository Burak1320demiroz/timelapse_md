#!/usr/bin/env python3
"""
capraz_sayim.py — QA/ARSIV_12_MERCEK/QA_CAPRAZ_ANALIZ/01_SKOR_MATRISI.md tablosunu okur ve
raporlarda anılan sayıları YENİDEN HESAPLAR. Raporlara sayı elle yazılmaz;
yazılan her sayı bu çıktıyla karşılaştırılır (AGENTS §3 ①: sayı tek yerde durur).

  python3 araclar/capraz_sayim.py            → özet
  python3 araclar/capraz_sayim.py --film     → film ortalamaları da

Neden var: 18.09.2026 çapraz analizinde toplam 138 yazıldı, matris 132 veriyordu;
İnşa %73,3 (11/15) yazıldı, matris 9/15 veriyordu. Elle sayılan sayı yanılır.
"""
import re, sys, os

YOL = "QA/ARSIV_12_MERCEK/QA_CAPRAZ_ANALIZ/01_SKOR_MATRISI.md"
ESIK = 4.0

def main():
    if not os.path.exists(YOL):
        print(f"⛔ {YOL} yok"); sys.exit(2)
    satirlar = [l for l in open(YOL, encoding="utf-8") if l.startswith("|")]
    baslik = None; filmler = []
    for l in satirlar:
        h = [c.strip().strip("*") for c in l.strip().strip("|").split("|")]
        if h and h[0] == "Film Başlığı":
            baslik = h; continue
        if baslik is None or set(h[0]) <= set("-: "):
            continue
        if h[0] == "GENEL ORTALAMA":
            break                                 # §2'nin tabloları matris değildir
        filmler.append(h)
    if baslik is None:
        print("⛔ matris başlığı bulunamadı"); sys.exit(2)
    mercekler = baslik[2:-1]                      # ① KARE … ⑫ KATILIK
    puanli = inc = 0; kolon = {m: [] for m in mercekler}; film_ort = {}
    for h in filmler:
        ad, rapor, hucreler = h[0], int(h[1]), h[2:-1]
        skorlar = []
        for m, c in zip(mercekler, hucreler):
            if c == "INC": inc += 1
            elif re.fullmatch(r"\d+(\.\d+)?", c):
                v = float(c); puanli += 1; kolon[m].append((ad, v)); skorlar.append(v)
        film_ort[ad] = (sum(skorlar) / len(skorlar) if skorlar else None, rapor, len(skorlar) + sum(1 for c in hucreler if c == "INC"))
    print(f"toplam kayıt      : {puanli + inc}  (puanlı {puanli} + INC {inc})")
    print(f"Rapor sütunu topl.: {sum(r for _, r, _ in film_ort.values())}")
    print(f"film sayısı       : {len(filmler)}")
    print(f"\n{'mercek':<14}{'film':>5}{'<'+str(ESIK):>6}{'oran':>8}  ort   <{ESIK} olanlar")
    for m in mercekler:
        v = kolon[m]
        if not v: continue
        dus = [(a, s) for a, s in v if s < ESIK]
        ort = sum(s for _, s in v) / len(v)
        print(f"{m:<14}{len(v):>5}{len(dus):>6}{100*len(dus)/len(v):>7.1f}%  {ort:4.2f}  " + ", ".join(f"{a} {s}" for a, s in dus))
    if "--film" in sys.argv:
        print("\nfilm ortalamaları (INC ve - hariç):")
        for ad, (o, r, n) in film_ort.items():
            uyari = " ⚠️ eksik mercek" if n < len(mercekler) else ""
            print(f"  {ad:<20} {o:5.2f}  rapor {r:>2}{uyari}" if o is not None else f"  {ad:<20}   —")
    for ad, (o, r, n) in film_ort.items():
        if n != r:
            print(f"⚠️ {ad}: Rapor sütunu {r}, hücre sayısı {n} — uyuşmuyor")

if __name__ == "__main__":
    main()
