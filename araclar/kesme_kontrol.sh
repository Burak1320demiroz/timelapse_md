#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  KESME KONTROL — kurgu, planın SÜRE sütununa uydu mu  [DERS 31]
#
#  NEDEN VAR:
#  THE LONG DAY planı varyanslı ızgara yazdı (6·4·6·4·6·6·8·4·6·10) ve
#  kurgu 10 × 6,0 kesildi → ⑥ METRONOM, dördüncü kez. Süre sütunu yalnız
#  planda yaşıyordu; teslim dosyasını onunla karşılaştıran hiçbir şey yoktu.
#
#  ⭐ 08.09.2026 · EŞİK KALDIRILDI, TOP-N GELDİ  [A8-X2 · A8-X3]
#  Ölçüldü: sabit kadraj + aynı yapı + yalnız aşama ilerleyen 10 klipli bir
#  teslimde kesme skorları 0,016-0,022; klip içi tavan 0,005. Eski varsayılan
#  eşik 0,30 ve A8 raporunun önerdiği 0,40 SIFIR kesme buluyordu — yani bu
#  kapı açık sanılıyordu, KAPALIYDI.
#  Yeni yordam: bütün karelerin scene skoru okunur, planda kaç kesme varsa
#  o kadar EN YÜKSEK skor seçilir (birbirine 0,40 sn'den yakın olanlar
#  bastırılır) ve zaman damgaları planla karşılaştırılır. Mutlak skor
#  ölçeğinden BAĞIMSIZDIR.
#
#  KULLANIM
#     bash araclar/kesme_kontrol.sh <teslim.mp4> <plan.md> [tolerans_sn] [--hiz N]
#     tolerans varsayılan 0.25 sn
#     ⭐ 05.10.2026 --hiz N: dosya N kat hızlı PAYLAŞIM kopyası (dikey: 2x — sahip kuralı).
#        Plan süreleri N'e bölünür; 7 × 8,0 dikey 2x'te 7 × 4,0 aranır [DERS 63].
#
#  ÇIKIŞ: 0 = ızgara tutuyor · 1 = sapma var · 2 = ölçülemedi
#  ⭐ 14.09.2026: sahne no iki basamaklı olabilir (yatay 12-48 sahne) — <FILM>_PLAN.md'nin
#     AŞAMA MERDİVENİ tablosu aynı "| S | SÜRE |" desenini taşır.
#  ⭐ 28.10.2026: süreler araclar/plan_oku.py'den — "8,0 (4+4)" satırı okunmuyordu
#     (LIT AGAIN 4, OPENING NIGHT 6 sahne sanıldı; ikisi de 8) [DENETİM 28.10.2026 · A1].
# ═══════════════════════════════════════════════════════════════════
set -u
command -v ffmpeg  >/dev/null || { echo "⛔ ffmpeg yok"; exit 2; }
command -v ffprobe >/dev/null || { echo "⛔ ffprobe yok"; exit 2; }
command -v python3 >/dev/null || { echo "⛔ python3 yok"; exit 2; }
[ $# -ge 2 ] || { sed -n '/KULLANIM/,/tolerans varsayılan/p' "$0" | sed 's/^#//'; exit 2; }
HIZ=1; ARGS=()
while [ $# -gt 0 ]; do
    case "$1" in --hiz) HIZ="${2:-1}"; shift 2 ;; *) ARGS+=("$1"); shift ;; esac
done
MP4="${ARGS[0]}"; PLAN="${ARGS[1]}"; TOL="${ARGS[2]:-0.25}"
[ -f "$MP4" ]  || { echo "⛔ teslim yok: $MP4"; exit 2; }
[ -f "$PLAN" ] || { echo "⛔ plan yok: $PLAN"; exit 2; }

# ── plandan süreler — ortak okuyucu (tablo ↔ SAHNE BLOĞU beyanı doğrulanır) ──
SURELER=$(python3 "$(dirname "$0")/plan_oku.py" "$PLAN" --sureler) || exit 2
N=$(echo "$SURELER" | grep -c .)
[ "$N" -ge 2 ] || { echo "⛔ planda iki sahneden az süre okundu"; exit 2; }

SURE=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$MP4")
TMP=$(mktemp -t kesme).txt
ffmpeg -v error -i "$MP4" -vf "select='gte(scene,0)',metadata=print:file=$TMP" -f null - 2>/dev/null

SURELER="$SURELER" N="$N" SURE="$SURE" HIZ="$HIZ" TOL="$TOL" MP4="$MP4" TMP="$TMP" python3 <<'PY'
import os, re, sys

hiz     = float(os.environ.get("HIZ", "1"))
sureler = [float(x) / hiz for x in os.environ["SURELER"].split()]
N       = int(os.environ["N"])
sure    = float(os.environ["SURE"])
tol     = float(os.environ["TOL"])
mp4     = os.path.basename(os.environ["MP4"])

kum, t = [], 0.0
for s in sureler:
    t += s; kum.append(round(t, 2))
toplam = kum[-1]

metin = open(os.environ["TMP"]).read()
kareler = [(float(a), float(b)) for a, b in
           re.findall(r'pts_time:([0-9.]+)\s*\n\s*lavfi\.scene_score=([0-9.eE+-]+)', metin)]

print("═══════════════════════════════════════════════════════")
print(f"  KESME KONTROL · {mp4} · top-N yordamı")
print("═══════════════════════════════════════════════════════")
if hiz != 1:
    print(f"  ⭐ hız  : {hiz:g}x paylaşım kopyası — plan süreleri ÷ {hiz:g}")
print(f"  plan   : {N} sahne · süreler {'·'.join(f'{s:g}' for s in sureler)} · sahne bloğu {toplam:.2f} sn")
print(f"  teslim : {sure:.2f} sn · okunan kare {len(kareler)}\n")

if len(kareler) < 10:
    print("  ⛔ kare skoru okunamadı — ffmpeg sürümü metadata=print desteklemiyor olabilir")
    sys.exit(2)

# son beklenen kesme dosya sonuna denk geliyorsa (kart yok) aranmaz
arananlar = kum[:]
kart_yok = abs(sure - toplam) < 0.25
if kart_yok:
    arananlar = kum[:-1]
K = len(arananlar)

# top-K, birbirine 0,40 sn'den yakın adaylar bastırılarak
sirali = sorted(kareler, key=lambda x: -x[1])
secili = []
for zaman, skor in sirali:
    if all(abs(zaman - z) >= 0.40 for z, _ in secili):
        secili.append((zaman, skor))
    if len(secili) == K:
        break
secili.sort()
secili_zamanlar = {z for z, _ in secili}
disarida = [s for z, s in kareler if z not in secili_zamanlar]
marj_alt  = min(s for _, s in secili) if secili else 0.0
marj_ust  = max(disarida) if disarida else 0.0

sapma = 0
print(f"  {'kesme':<6} {'beklenen':<10} {'bulunan':<10} {'fark':<8} {'skor':<9}")
for i, e in enumerate(arananlar, 1):
    if i <= len(secili):
        b, sk = secili[i-1]
        d = abs(b - e)
        im = "✅" if d <= tol else "⛔"
        if d > tol: sapma += 1
        print(f"  {i:<6} {e:<10.2f} {b:<10.2f} {d:<8.2f} {sk:<9.5f} {im}")
    else:
        sapma += 1
        print(f"  {i:<6} {e:<10.2f} {'—':<10} {'—':<8} {'—':<9} ⛔")
if kart_yok:
    print(f"  {'kart':<6} {kum[-1]:<10.2f} {'—':<10} {'—':<8} {'—':<9} ✅ (dosya sonu — kart yok)")

print()
print(f"  AYIRIM  seçilen en düşük skor {marj_alt:.5f} · seçilmeyen en yüksek {marj_ust:.5f}")
if marj_ust > 0 and marj_alt / marj_ust < 2.0:
    print("  ⚠️  MARJ DAR (<2 kat) — kesme tespiti belirsiz. Kurguyu gözle doğrula.")
else:
    print("  ✅ marj yeterli (≥2 kat) — seçilen kesmeler klip içi gürültüden ayrışıyor")

if len(set(sureler)) == 1:
    if N in (7, 8) and abs(sureler[0] * hiz - 8.0) < 1e-6:
        print(f"\n  ℹ️  düz ızgara {N} × 8,0 — sahip kuralı (8 sahne: sahip istisnası), beyanlı [DERS 58]")
    else:
        print(f"\n  ⛔ PLANIN KENDİSİ DÜZ: bütün süreler {sureler[0]:g} — ⑥ METRONOM [DERS 13]")

print()
if sapma == 0:
    print("  SONUÇ: ✅ kurgu planın SÜRE sütununa oturuyor")
    sys.exit(0)
print(f"  SONUÇ: ⛔ {sapma} kesme planla uyuşmuyor — kurgu SÜRE sütunundan yeniden kesilir")
sys.exit(1)
PY
KOD=$?
rm -f "$TMP"
exit $KOD
