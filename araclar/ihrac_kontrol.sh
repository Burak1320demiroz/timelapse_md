#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  İHRAÇ KONTROL — paylaşılacak dosya PLANIN TESLİM YAPISINA uyuyor mu  [DERS 63]
#
#  NEDEN VAR (05.10.2026):
#  Planlar "⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK" diyordu; paylaşılan dosyalarda
#  4 sn'lik kart (GLASS CROSSING · SWALLOWED BUS · TIDE GATE), promo yazısı ve
#  "AI TIMELAPSE" metni (BACK TO PLUMB kartı) ve müzik (BACK TO PLUMB, dikey)
#  vardı. Plan beyanı ile dışa aktarma arasında HİÇBİR adım yoktu.
#  Ayrıca dikey shorts 7 × 8,0 = 56 sn üretilir ve 2x hızda paylaşılır
#  (sahip kuralı 05.10.2026): 28 sn'lik sahne bloğu KESİK DEĞİLDİR. Sahip istisnası
#  (THE POOL ROOM 8 × 8 = 64 sn) planın SAHNE BLOĞU satırından okunur. Bu betik
#  hızı beyan eder; QA paketi aynı beyanı merceklere taşır (qa_paket --hiz).
#
#  KULLANIM
#     bash araclar/ihrac_kontrol.sh <film_klasoru> <paylasim.mp4> [--hiz 2]
#     örn: bash araclar/ihrac_kontrol.sh dikey_shorts/THE_BLUE_SILO paylas/blue_silo_2x.mp4 --hiz 2
#     --hiz varsayılan: dikey 2 · yatay 1
#
#  ÖLÇER (makine):  süre = sahne bloğu/hız (+ kart, PLAN izin veriyorsa) · çözünürlük ·
#                   final tutuşu (≥2,0 sn @1x → ≥2,0/hız sn @paylaşım, SSIM) ·
#                   kartın gerçek başı ve süresi (freezedetect — dosyanın sonundaki donuk kuyruk) ·
#                   kart/final kareleri <mp4_dizini>/IHRAC_KARELER/<FILM>/ altına
#  ⭐ 28.10.2026 [DENETİM 28.10.2026 · A3 · A4]: kareler film başına ayrı klasörde (beş koşu aynı
#     klasöre üst üste yazıyordu) · süre tutmazsa ③ final penceresi plan bloğuna değil ÖLÇÜLEN
#     kart başına konur (blok kaymış dosyada yanlış saniye ölçülüyordu) · sahne bloğu plan_oku.py'den.
#  SORAR (insan):   müzik · logo/promo/"AI TIMELAPSE" yazısı · kart ↔ GN aynı dünya
#  ÇIKIŞ: 0 = makine ölçümleri tuttu (elle maddeler yine işaretlenir) · 2 = TESLİM EDİLMEZ
# ═══════════════════════════════════════════════════════════════════
set -u
command -v ffmpeg  >/dev/null || { echo "⛔ ffmpeg yok"; exit 2; }
command -v ffprobe >/dev/null || { echo "⛔ ffprobe yok"; exit 2; }
[ $# -ge 2 ] || { sed -n '/KULLANIM/,/varsayılan/p' "$0" | sed 's/^#//'; exit 2; }

DIR="${1%/}"; MP4="$2"; shift 2
HIZ=""
while [ $# -gt 0 ]; do
    case "$1" in --hiz) HIZ="${2:-}"; shift 2 ;; *) echo "⛔ bilinmeyen argüman: $1"; exit 2 ;; esac
done
FILM="$(basename "$DIR")"
PLAN="$DIR/${FILM}_DIKEY_TIMELAPSE.md"; DIKEY=1
[ -f "$PLAN" ] || { PLAN="$DIR/${FILM}_PLAN.md"; DIKEY=0; }
[ -f "$PLAN" ] || { echo "⛔ plan yok: $DIR"; exit 2; }
[ -f "$MP4" ]  || { echo "⛔ dosya yok: $MP4"; exit 2; }
[ -n "$HIZ" ] || { [ "$DIKEY" -eq 1 ] && HIZ=2 || HIZ=1; }

# ── plan beyanları (TESLİM YAPISI) ─────────────────────────────────
SAHNE_BLOK=$(python3 "$(dirname "$0")/plan_oku.py" "$PLAN" --blok) || exit 2
KART_SATIR=$(grep -m1 -E '^KAPAK KARTI' "$PLAN")
MUZIK_SATIR=$(grep -m1 -E '^MÜZİK' "$PLAN")
KART_YOK=0; echo "$KART_SATIR" | grep -q '⛔ YOK' && KART_YOK=1
KART_SN=$(echo "$KART_SATIR" | grep -oE '[0-9]+[.,][0-9]+ *sn' | head -1 | grep -oE '[0-9]+[.,][0-9]+' | tr ',' '.')
ERIME=$(echo "$KART_SATIR" | grep -oE 'erime *≤ *[0-9]+([.,][0-9]+)?' | head -1 | grep -oE '[0-9]+([.,][0-9]+)?$' | tr ',' '.')
MUZIK_YOK=0; echo "$MUZIK_SATIR" | grep -q '⛔ YOK' && MUZIK_YOK=1
[ "$DIKEY" -eq 1 ] && MUZIK_YOK=1     # sahip kuralı 21.09.2026 — dikeyde müzik yok, beyan ne derse desin
GERI=0; grep -qE '^ *AÇILIŞ GERİ ÇEKİLMESİ +✅' "$PLAN" && GERI=1
[ -n "$SAHNE_BLOK" ] || { echo "⛔ planda sahne bloğu okunamadı"; exit 2; }

# ── dosya ölçümleri ────────────────────────────────────────────────
SURE=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$MP4")
WH=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$MP4")
SES=$(ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$MP4" | head -1)
OUT="$(cd "$(dirname "$MP4")" && pwd)/IHRAC_KARELER/$FILM"; mkdir -p "$OUT"

DIKEY="$DIKEY" HIZ="$HIZ" SAHNE_BLOK="$SAHNE_BLOK" KART_YOK="$KART_YOK" KART_SN="${KART_SN:-0}" ERIME="${ERIME:-1}" \
MUZIK_YOK="$MUZIK_YOK" GERI="$GERI" SURE="$SURE" WH="$WH" SES="$SES" MP4="$MP4" OUT="$OUT" FILM="$FILM" python3 <<'PY'
import os, re, subprocess, sys
e = os.environ
hiz, blok, sure = float(e["HIZ"]), float(e["SAHNE_BLOK"]), float(e["SURE"])
kart_yok, kart_sn = e["KART_YOK"] == "1", float(e["KART_SN"] or 0)
dikey, muzik_yok = e["DIKEY"] == "1", e["MUZIK_YOK"] == "1"
mp4, out = e["MP4"], e["OUT"]
dur = 0

def kare(t, ad):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(t,0):.3f}", "-i", mp4,
                    "-frames:v", "1", f"{out}/{ad}.png"], check=False)
    return f"{out}/{ad}.png"

def ssim(a, b):
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", a, "-i", b, "-lavfi", "ssim", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = re.search(r"All:([0-9.]+)", r.stderr)
    return float(m.group(1)) if m else None

def donuk_kuyruk():
    """Dosyanın sonuna kadar süren son donukluğun başı (kart başı) — yoksa None.
    Ölçüldü 28.10.2026: beş yayın dosyasında kart başını 0,1 sn içinde verdi."""
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", mp4, "-vf", "scale=270:-2,freezedetect=n=-50dB:d=0.4",
                        "-an", "-f", "null", "-"], capture_output=True, text=True)
    olay = re.findall(r"freeze_(start|end): ([0-9.]+)", r.stderr)
    if not olay or olay[-1][0] != "start":
        return None
    return float(olay[-1][1])

print("═══════════════════════════════════════════════════════")
print(f"  İHRAÇ KONTROL · {e['FILM']} · {os.path.basename(mp4)}")
print("═══════════════════════════════════════════════════════")
pblok = blok / hiz
beklenen = pblok + (0 if kart_yok else kart_sn)
print(f"  plan    sahne bloğu {blok:g} sn @1x · hız {hiz:g}x → {pblok:.2f} sn · kart "
      f"{'⛔ YOK' if kart_yok else f'{kart_sn:g} sn'} · müzik {'⛔ YOK' if muzik_yok else 'var'}")
print(f"  dosya   {sure:.2f} sn · {e['WH']} · ses akışı {'var' if e['SES'] else 'YOK'}\n")

# ① süre ve kart
fark = sure - pblok
if fark < -0.30:
    print(f"  ⛔ ① dosya sahne bloğundan KISA ({sure:.2f} < {pblok:.2f}) — klip eksik ya da hız yanlış beyan")
    dur = 1
elif kart_yok and fark > 0.50:
    print(f"  ⛔ ① plan KART YOK diyor ama dosyada sahne bloğundan sonra {fark:.2f} sn var — kart kesilir "
          f"[DERS 63 · GLASS CROSSING · SWALLOWED BUS · TIDE GATE]")
    dur = 1
elif not kart_yok and abs(sure - beklenen) > 0.50:
    print(f"  ⛔ ① süre {sure:.2f} ≠ beklenen {beklenen:.2f} (blok {pblok:.2f} + kart {kart_sn:g})")
    dur = 1
else:
    print(f"  ✅ ① süre planla tutuyor ({sure:.2f} sn)")

# ①b kartın gerçek başı — dosyanın sonundaki donuk kuyruk [DENETİM 28.10.2026 · A3]
kart_bas = None if kart_yok else donuk_kuyruk()
blok_kaydi = False   # ölçülen blok sonu plandan erime payından fazla mı sapıyor
if not kart_yok:
    if kart_bas is None:
        print("  ⚠️ ①b kart ölçülemedi (dosya sonunda donuk kuyruk yok) — kart hareketli mi, yok mu? gözle bak")
    else:
        # erime kartın içindedir: donukluk erime bitince başlar → kart en çok erime kadar kısa,
        # blok en çok erime kadar uzun ölçülür
        erime = float(e.get("ERIME") or 1)
        k_olc, b_olc = sure - kart_bas, kart_bas
        notlar = []
        if not (kart_sn - erime - 0.50 <= k_olc <= kart_sn + 0.50):
            notlar.append(f"kart {k_olc:.2f} sn (plan {kart_sn:g})")
        if not (pblok - 0.50 <= b_olc <= pblok + erime + 0.50):
            blok_kaydi = True
            notlar.append(f"sahne bloğu {b_olc:.2f} sn (plan {pblok:g}) — "
                          + ("fazladan " if b_olc > pblok else "eksik ") + f"{abs(b_olc - pblok):.2f} sn")
        if notlar:
            print(f"  ⛔ ①b ölçülen: kart {kart_bas:.2f} sn'de başlıyor · " + " · ".join(notlar)); dur = 1
        else:
            print(f"  ✅ ①b ölçülen: kart {kart_bas:.2f} sn'de başlıyor · {k_olc:.2f} sn")

# ② çözünürlük
w, h = (int(x) for x in e["WH"].split("x"))
if dikey and (w, h) != (1080, 1920):
    print(f"  ⛔ ② dikey teslim 1080×1920 olmalı — dosya {w}×{h}"); dur = 1
elif not dikey and (w, h) != (1920, 1080):
    print(f"  ⛔ ② yatay teslim 1920×1080 olmalı — dosya {w}×{h}"); dur = 1
else:
    print(f"  ✅ ② çözünürlük {w}×{h}")

# ③ final tutuşu — usta kare klibinin son ≥2,0 sn'si (@1x) sabit [KILAVUZ_REHBERI §8 adım 9]
tut = 2.0 / hiz
# blok plandan kaymışsa final penceresi ÖLÇÜLEN kart başına konur — plan saniyesi başka bir anı ölçer
blok_son = kart_bas if blok_kaydi else min(pblok, sure)
sonz = blok_son - 0.15   # dosya bloktan birkaç ms kısa olabilir — son kare yine alınır
son = kare(sonz, "final_son")
once = kare(sonz - tut, "final_tutus_basi")
s = ssim(son, once)
if blok_son != min(pblok, sure):
    print(f"  ℹ️ ③ final penceresi ölçülen kart başına göre: {sonz - tut:.2f}–{sonz:.2f} sn (plan {pblok:g} değil)")
if s is None:
    print("  ⚠️ ③ final tutuşu ölçülemedi (ssim okunamadı) — gözle bak")
elif s < 0.90:
    print(f"  ⛔ ③ final TUTULMUYOR: son {tut:.2f} sn'de SSIM {s:.3f} (< 0,90) — vaat edilen son kare "
          f"ekranda durmuyor [P2-i · BACK TO PLUMB finali 2x'te 1,25 sn]"); dur = 1
else:
    print(f"  ✅ ③ final {tut:.2f} sn tutuluyor (SSIM {s:.3f})")

if not kart_yok:
    kare((kart_bas if kart_bas is not None else pblok) + min(1.0, kart_sn / 2), "kart")
print(f"\n  kareler → {out}/  (final_son.png{'' if kart_yok else ' · kart.png'})")

print("""
  ── ELLE · her biri ✓ yazılmadan PAYLAŞILMAZ (üretim günlüğü §4'e) ──────────""")
if muzik_yok:
    print("  ☐ ④ MÜZİK YOK — baştan sona dinle: yalnız saha sesi (diegetik). Müzik varsa ses yatağı yeniden"
          + (" [sahip kuralı 21.09.2026 · BACK TO PLUMB]" if dikey else ""))
else:
    print("  ☐ ④ müzik planın MUZIK dosyasındaki giriş noktalarına oturuyor")
print("  ☐ ⑤ kadrajda ve kartta OKUNUR YAZI YOK: logo · promo · kanal adı · 'AI TIMELAPSE' · filigran")
print("       (gerçeklik beyanı açıklamada ve platform bayrağındadır, görüntüde değil)")
if not kart_yok:
    print("  ☐ ⑥ kart.png ile final_son.png AYNI DÜNYA — kart başka yapı göstermiyor [MOUNTAIN CROWN]")
if e.get("GERI") == "1":
    print("  ☐ ⑧ S0 GERİ ÇEKİLME: yakın kadrajda başlıyor, ilk ≤ 3,0 sn (1x) içinde HOME'a oturuyor ve S1'e"
          " GENİŞ planda giriliyor; ayrıntı bulanık değil [KAMERA_HAREKETI §4.2]")
print("  ☐ ⑦ kurgu planın klip ızgarasında: "
      + (f"{round(blok / 8)} klip × {8/hiz:g} sn (dikey)" if dikey else "SÜRE sütunu")
      + f" → bash araclar/kesme_kontrol.sh {os.path.basename(mp4)} <plan> --hiz {hiz:g}")
print(f"\n  ⭐ QA'YA: bu dosya {hiz:g}x paylaşım kopyasıdır — zaman damgası × {hiz:g} = plan saniyesi;"
      f" {pblok:g} sn'lik sahne bloğu KESİK DEĞİLDİR → bash araclar/qa_paket.sh --hiz {hiz:g} …")
print()
print("  SONUÇ: ⛔ TESLİM EDİLMEZ — yukarıdaki ⛔ satırları" if dur else
      "  SONUÇ: ✅ makine ölçümleri tuttu — elle maddeler işaretlenince paylaşılır")
sys.exit(2 if dur else 0)
PY
