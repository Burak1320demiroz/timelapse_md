#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
#  KLİP EŞLEŞTİR — üretilen her klip yayın dosyasında VAR MI, NEREDE  [DERS 86]
#
#  NEDEN VAR (16.10.2026 · THE POOL ROOM):
#  Sekiz klip üretildi; yayın kurgusunda S4 (CAMLAR — filmin özgün anı) YOKTU.
#  Zincir kareleri birebir tuttuğu için kesme görünmedi: 14,87'de açık kanal,
#  15,00'te cam yerinde. Kör mercekler bunu "cam belirdi" diye üretim arızası
#  saydı. Plan ↔ dosya arasında klip sayımı yapan adım yoktu; kesme_kontrol
#  zincirli filmde kesmeyi göremez (dikiş kareleri aynıdır).
#
#  KULLANIM
#     python3 araclar/klip_eslestir.py <yayin.mp4> <S0.mp4> <S1.mp4> … [--hiz 2] [--kart 5.5]
#     --kart: plandaki kapak kartı + erime süresi (sn, yayın dosyasında) — sahip kuralı 16.10.2026:
#             her filmin sonunda kapak; kuyruk bu süreyle ±1,0 sn tutarsa geçer
#     klipler SAHNE SIRASIYLA verilir.
#
#  ÖLÇER   her klibin %10 · %30 · %50 · %70 · %90 karesini yayında arar (54×96 gri, ortalama
#          mutlak fark) · klibin yayındaki başı/sonu · süresi (beklenen klip_süresi/hız)
#          · son klipten sonra kalan süre (kart / erime) · klip sırası
#  ⚠️ EŞİK  fark ≤ 6,0 = bulundu — VARSAYIM: POOL ROOM'da bulunan klipler 1,5–3,5,
#          kurgudan düşen klip 9,8–13,3 verdi. Tek filmde ölçüldü.
#  ÇIKIŞ   0 = her klip tam bulundu, sıra doğru · 2 = eksik/kırpılmış/ters klip ya da kuyruk
# ═══════════════════════════════════════════════════════════════════
import subprocess
import sys

import numpy as np

W, H, ESIK = 54, 96, 6.0


def kareler(yol):
    ham = subprocess.run(["ffmpeg", "-v", "error", "-i", yol, "-vf", f"scale={W}:{H},format=gray",
                          "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(ham, np.uint8).reshape(-1, H * W).astype(np.int16)


def fps(yol):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=r_frame_rate", "-of", "csv=p=0", yol], capture_output=True, text=True).stdout
    a, b = r.strip().split("/")
    return float(a) / float(b)


arg = sys.argv[1:]
hiz, kart = 1.0, 0.0
if "--kart" in arg:
    i = arg.index("--kart")
    kart = float(arg[i + 1])
    del arg[i:i + 2]
if "--hiz" in arg:
    i = arg.index("--hiz")
    hiz = float(arg[i + 1])
    del arg[i:i + 2]
if len(arg) < 2:
    print(__doc__ or "", open(__file__, encoding="utf-8").read().split("KULLANIM")[1].split("ÖLÇER")[0])
    sys.exit(2)

yayin, klipler = arg[0], arg[1:]
P, pf = kareler(yayin), fps(yayin)
sure = len(P) / pf
print("═" * 62)
print(f"  KLİP EŞLEŞTİR · {yayin.split('/')[-1]} · {sure:.2f} sn · {len(klipler)} klip · hız {hiz:g}x")
print("═" * 62)

dur, bulunan, son_bitis = 0, [], 0.0
for k, yol in enumerate(klipler):
    C, cf = kareler(yol), fps(yol)
    ks = len(C) / cf
    sonuc = []
    for q in (0.10, 0.30, 0.50, 0.70, 0.90):
        f = C[int(q * (len(C) - 1))]
        d = np.abs(P - f).mean(axis=1)
        j = int(d.argmin())
        sonuc.append((q, j / pf, float(d[j])))
    tut = [x for x in sonuc if x[2] <= ESIK]
    ad = yol.split('/')[-1][:44]
    if len(tut) <= 1:   # tek tutan nokta uç karedir = komşu klibin zincir karesi (G(n) ortak)
        dur = 2
        print(f"  ⛔ S{k}  {ad:44s} YAYINDA YOK (beş noktadan {len(tut)} tuttu — yalnız ortak zincir karesi) — "
              f"kurgudan düşmüş; bitişik kesmede iş 'belirir'")
        continue
    bas = tut[0][1] - tut[0][0] * ks / hiz
    bit = tut[-1][1] + (1 - tut[-1][0]) * ks / hiz
    bulunan.append((k, tut[len(tut) // 2][1]))
    son_bitis = max(son_bitis, bit if len(tut) == len(sonuc) else tut[-1][1])
    eksik = [f"%{int(x[0] * 100)}" for x in sonuc if x[2] > ESIK]
    if eksik:
        dur = 2
        print(f"  ⚠️ S{k}  {ad:44s} KIRPILMIŞ — yayında yok: {' · '.join(eksik)} noktaları "
              f"(bulunan kısım ≈ {max(bas, 0):5.2f}–{tut[-1][1]:5.2f} sn)")
    else:
        print(f"  ✅ S{k}  {ad:44s} yayında ≈ {max(bas, 0):5.2f}–{bit:5.2f} sn "
              f"(beklenen {ks / hiz:.2f} sn · en büyük fark {max(x[2] for x in sonuc):.1f})")

sira = [k for k, _ in sorted(bulunan, key=lambda x: x[1])]
if sira != sorted(sira):
    dur = 2
    print(f"  ⛔ SIRA bozuk: yayındaki sıra {['S%d' % k for k in sira]}")
kuyruk = sure - son_bitis
if kart and abs(kuyruk - kart) <= 1.0:
    print(f"  ✅ son klipten sonra {kuyruk:.2f} sn — beyan edilen kapak kartı {kart:g} sn ile tutuyor")
elif kart or kuyruk > 0.5:
    dur = 2
    print(f"  ⛔ son klipten sonra {kuyruk:.2f} sn (beyan: {kart:g} sn) — kart planla tutmuyor; kart tutuştan "
          f"SONRA mı, GN'den mi: ihrac_kontrol.sh [DERS 63 · 85]")
print("\n  SONUÇ:", "✅ her klip yayında, sıra doğru" if dur == 0 else "⛔ KURGU PLANLA TUTMUYOR")
sys.exit(dur)
