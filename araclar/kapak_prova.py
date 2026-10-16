#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
#  KAPAK PROVA — dikey kapağın kırpma ve küçük önizleme provaları
#  [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3 · §9 · §11]
#
#  KULLANIM
#     python3 araclar/kapak_prova.py <kapak.png|jpg> [cikis_klasoru]
#     varsayılan çıkış: <kapak klasörü>/KAPAK_PROVA/
#
#  ÜRETİR   tam 9:16 · merkezden 3:4 (y 240–1680) · 4:5 (y 285–1635) · 1:1 (y 420–1500) kırpmaları
#           · her birinin 140 px genişlikte küçüğü · güvenli alan şablonu bindirilmiş kopya
#           · hepsini yan yana koyan PROVA_PANOSU.png (gözle bakılacak tek dosya)
#  ÖLÇER    tuval 1080×1920 mi (değilse ⛔) · 9:16 mı
#  SORAR    (insan) film adı okunuyor mu · ana yapı tanınıyor mu · dönüşüm izi seçiliyor mu
#           · gerçek platform önizlemesi ayrıca kontrol edildi mi [§9 son karar]
#  ⚠️ Kırpmalar MERKEZDEN varsayımdır; platformun gerçek önizlemesi daha güçlü kanıttır [§1 · §12].
#  ÇIKIŞ    0 = tuval doğru, panolar üretildi · 2 = tuval 1080×1920 değil
# ═══════════════════════════════════════════════════════════════════
import os
import sys

from PIL import Image

if len(sys.argv) < 2:
    print(open(__file__, encoding="utf-8").read().split("KULLANIM")[1].split("ÜRETİR")[0])
    sys.exit(2)

kaynak = sys.argv[1]
cikis = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(kaynak)), "KAPAK_PROVA")
os.makedirs(cikis, exist_ok=True)
sablon_yol = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "kilavuzlar", "KAPAK_SAFE_AREA_1080x1920.png")

im = Image.open(kaynak).convert("RGB")
w, h = im.size
print("═" * 62)
print(f"  KAPAK PROVA · {os.path.basename(kaynak)} · {w}×{h}")
print("═" * 62)
dur = 0
if (w, h) != (1080, 1920):
    oran = h / w
    if abs(oran - 16 / 9) < 0.01:
        print(f"  ⚠️ tuval 9:16 ama {w}×{h} — 1080×1920'ye ölçeklenerek prova yapıldı; dışa aktarımı 1080×1920 yap [§9]")
    else:
        print(f"  ⛔ tuval 9:16 DEĞİL ({w}×{h}, oran {oran:.3f}) — yeni dikey tuval gerekir [§6]")
        dur = 2
    im = im.resize((1080, int(round(1080 * h / w))), Image.LANCZOS)
    if im.size[1] != 1920:
        im = im.crop((0, max(0, (im.size[1] - 1920) // 2), 1080, max(0, (im.size[1] - 1920) // 2) + 1920))
else:
    print("  ✅ tuval 1080×1920 · 9:16")

provalar = [("9x16", 0, 1920), ("3x4", 240, 1680), ("4x5", 285, 1635), ("1x1", 420, 1500)]
kucukler = []
for ad, y0, y1 in provalar:
    k = im.crop((0, y0, 1080, y1))
    k.save(os.path.join(cikis, f"kapak_{ad}.png"))
    t = k.resize((140, int(round(140 * k.size[1] / 1080))), Image.LANCZOS)
    t.save(os.path.join(cikis, f"kapak_{ad}_140px.png"))
    kucukler.append(t)

bindirme = im.convert("RGBA")
if os.path.exists(sablon_yol):
    bindirme = Image.alpha_composite(bindirme, Image.open(sablon_yol).convert("RGBA"))
    bindirme.convert("RGB").save(os.path.join(cikis, "kapak_SABLONLU.png"))
else:
    print(f"  ⚠️ şablon yok: {sablon_yol}")

# PANO: şablonlu tam kare (480 px boy) + dört kırpma (480 boy) + dört 140 px küçük
pano_h = 480
parcalar = [bindirme.convert("RGB").resize((270, 480))]
for ad, y0, y1 in provalar[1:]:
    k = im.crop((0, y0, 1080, y1))
    parcalar.append(k.resize((int(round(pano_h * 1080 / k.size[1])), pano_h)))
genislik = sum(p.size[0] for p in parcalar) + 10 * len(parcalar) + 10 + 4 * 150
pano = Image.new("RGB", (genislik, pano_h + 20), (24, 24, 24))
x = 10
for p in parcalar:
    pano.paste(p, (x, 10))
    x += p.size[0] + 10
for t in kucukler:
    pano.paste(t, (x, 10))
    x += 150
pano.save(os.path.join(cikis, "PROVA_PANOSU.png"))

print(f"\n  çıktı → {cikis}/  (PROVA_PANOSU.png · kapak_<oran>.png · _140px · kapak_SABLONLU.png)")
print("""
  ── ELLE · üç soru, her prova ve 140 px küçük için [§9] ──────────────
  ☐ film adını okuyabiliyor muyum?  (başlık kutusu x 180–900 · y 560–770 içinde mi)
  ☐ ana yapının ne olduğunu anlıyor muyum?  (ana yapı x 150–930 · y 800–1360)
  ☐ dönüşümün sıra dışı tarafını açıklamasız seçebiliyor muyum?
  ☐ kapaktaki sonuç filmde var mı · kaynak GN mi (zincir_kontrol GN ↔ kapak) [DERS 30 · 85]
  ☐ gerçek Instagram/TikTok/Shorts önizlemesi ayrıca görüldü mü [§8]
  Birine hayır → efekt ekleme; öğelerin yerini/büyüklüğünü değiştir.""")
sys.exit(dur)
