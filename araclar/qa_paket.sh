#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  QA PAKET — beş merceğin koşusunu araca bağlar  [DERS 29 · 06.10.2026 beş mercek]
#
#  NEDEN VAR:
#  Yazılı yordam koşmaz [DERS 12]. 12 mercekli dönemde belge isteyen koşuların
#  YARISI belgesiz yapıldı, 2x kopya "kesik" okundu, hız beyanı yapıştırılan
#  rubriğin DIŞINDA kaldı (ARSIV_12_MERCEK/00_ARSIV.md). Bu betik her mercek için
#  tek dosya üretir: künye taslağı + eklenecek dosyalar + ÖLÇÜLMÜŞ OLGULARLA
#  DOLDURULMUŞ rubrik. Model sayı tahmin etmez; sayıyı makine ölçer
#  [QA_OLCUM_ZEMINI_KILAVUZU].
#
#  KULLANIM
#     bash araclar/qa_paket.sh [--gunluksuz] [--hiz N] [--master 1x.mp4] [--bolum 1|2] \
#          <film_klasoru> <yayin.mp4> [kapak.png]
#     örn: bash araclar/qa_paket.sh --master teslim/blue_silo_1x.mp4 \
#          dikey_shorts/THE_BLUE_SILO teslim/blue_silo_2x.mp4 teslim/kapak.png
#     --hiz      yayın dosyasının hızı (dikey varsayılan 2 · yatay 1)
#     --master   1x ana dosya (varsa) — ❸ ŞANTİYE ve ❹ İNŞA onunla koşar
#                (klip başına iki kat kare) [QA_OLCUM_ZEMINI §3]
#     --bolum    yatay 6/8 dk yarım master (paketler QA/KOSU/<FILM>/B<n>/)
#
#  ÇIKTI:  QA/KOSU/<FILM>/Q<n>_<AD>_paket.md   (5 dosya)
#          kareler: <dosya_dizini>/QA_KARELER/ (yoksa kare_al.sh koşulur)
#  HAM:    QA/HAM/<FILM>/<FILM>_Q<n>_<AD>_HAM.md — künye üstte, model çıktısı altta
#
#  ⛔ KAPI: film klasöründe <FILM>_URETIM_GUNLUGU.md yoksa DURUR [DERS 28].
#     Bile bile geçmek için: --gunluksuz  (paketlerin başına uyarı yazılır)
# ═══════════════════════════════════════════════════════════════════
set -u
cd "$(dirname "$0")/.." || exit 2
command -v ffprobe >/dev/null || { echo "⛔ ffprobe yok"; exit 2; }

GUNLUKSUZ=0; BOLUM=""; HIZ=""; MASTER=""
while [ $# -gt 0 ]; do
    case "$1" in
        --gunluksuz) GUNLUKSUZ=1; shift ;;
        --hiz)       HIZ="${2:-}"; shift 2 ;;
        --master)    MASTER="${2:-}"; shift 2 ;;
        --bolum)     BOLUM="${2:-}"; shift 2
                     case "$BOLUM" in 1|2) ;; *) echo "⛔ --bolum 1 ya da 2"; exit 2 ;; esac ;;
        *) break ;;
    esac
done
[ $# -ge 2 ] || { sed -n '/KULLANIM/,/--bolum    yatay/p' "$0" | sed 's/^#//'; exit 2; }

DIR="${1%/}"; MP4="$2"; KAPAK="${3:-}"
FILM="$(basename "$DIR")"
PLAN="$DIR/${FILM}_DIKEY_TIMELAPSE.md"; DIKEY=1
[ -f "$PLAN" ] || { PLAN="$DIR/${FILM}_PLAN.md"; DIKEY=0; }
[ -n "$HIZ" ] || { [ "$DIKEY" -eq 1 ] && HIZ=2 || HIZ=1; }
SPEC="$DIR/${FILM}_QA_SPEC.md"
GUNLUK="$DIR/${FILM}_URETIM_GUNLUGU.md"

[ -f "$PLAN" ] || { echo "⛔ plan yok: $PLAN"; exit 2; }
[ -f "$SPEC" ] || { echo "⛔ SPEC yok: $SPEC"; exit 2; }
[ -f "$MP4"  ] || { echo "⛔ yayın dosyası yok: $MP4"; exit 2; }
[ -z "$MASTER" ] || [ -f "$MASTER" ] || { echo "⛔ master yok: $MASTER"; exit 2; }
for q in Q1_GORUNTU Q2_ZAMAN_KESME Q3_SANTIYE Q4_INSA Q5_TESLIM; do
    [ -f "QA/$q.md" ] || { echo "⛔ rubrik yok: QA/$q.md"; exit 2; }
done

if [ ! -f "$GUNLUK" ]; then
    if [ "$GUNLUKSUZ" -eq 1 ]; then
        echo "⚠️  ÜRETİM GÜNLÜĞÜ YOK ($GUNLUK) — --gunluksuz ile geçildi; kayda yazılır."
    else
        echo "⛔ ÜRETİM GÜNLÜĞÜ YOK: $GUNLUK  [DERS 28]"
        echo "   Bile bile geçmek için: bash araclar/qa_paket.sh --gunluksuz ..."
        exit 2
    fi
fi

abs() { echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"; }
MP4ABS="$(abs "$MP4")"; MASTERABS=""; [ -n "$MASTER" ] && MASTERABS="$(abs "$MASTER")"
KAPAKABS=""; [ -n "$KAPAK" ] && [ -f "$KAPAK" ] && KAPAKABS="$(abs "$KAPAK")"
SPECABS="$(abs "$SPEC")"; PLANABS="$(abs "$PLAN")"

# ── plan beyanları ────────────────────────────────────────────────
SAHNE=$(grep -cE '^\| [0-9]+ \| [0-9]+[.,][0-9]+ \|' "$PLAN")
[ -n "$BOLUM" ] && SAHNE=$((SAHNE / 2))
[ "$SAHNE" -gt 0 ] || { echo "⛔ planda SÜRE sütunu okunamadı (| S | SÜRE | satırları)"; exit 2; }
BLOK=$(grep -m1 -E '^SAHNE BLOĞU' "$PLAN" | grep -oE '= *[0-9]+[.,][0-9]+' | tr -d '= ' | tr ',' '.')
[ -n "$BLOK" ] || BLOK=$(grep -E '^\| [0-9]+ \| [0-9]+[.,][0-9]+ \|' "$PLAN" | awk -F'|' '{gsub(/ /,"",$3); gsub(",",".",$3); s+=$3} END{printf "%.1f", s}')
[ -n "$BOLUM" ] && BLOK=$(awk -v b="$BLOK" 'BEGIN{printf "%.1f", b/2}')
KART_SATIR=$(grep -m1 -E '^KAPAK KARTI' "$PLAN"); MUZIK_SATIR=$(grep -m1 -E '^MÜZİK' "$PLAN")

# ── kareler: master varsa ondan (❶ ❸ aynı kareyi görür; kare hızdan bağımsızdır) ──
KAYNAK_KARE="$MP4"; KARE_HIZ="$HIZ"; [ -n "$MASTER" ] && { KAYNAK_KARE="$MASTER"; KARE_HIZ=1; }
KARELER="$(cd "$(dirname "$KAYNAK_KARE")" && pwd)/QA_KARELER"
if [ ! -d "$KARELER" ] || [ -z "$(ls -A "$KARELER" 2>/dev/null)" ]; then
    echo "📸 kare grabı yok → kare_al.sh koşuluyor"
    BLOK_HIZ=$(awk -v b="$BLOK" -v h="$KARE_HIZ" 'BEGIN{printf "%.3f", b/h}')
    bash araclar/kare_al.sh "$KAYNAK_KARE" "$SAHNE" "$BLOK_HIZ" || { echo "⛔ kare_al.sh düştü"; exit 2; }
fi
KARE_SAYISI=$(ls -1 "$KARELER" 2>/dev/null | wc -l | tr -d ' ')

# ── ölçülmüş olgular: dosya başına bir kez ─────────────────────────
olgular() {  # <dosya> <hız> → OLGU_<anahtar>=… satırları
    local f="$1" h="$2" ko
    ko=$(bash araclar/kesme_kontrol.sh "$f" "$PLAN" 0.25 --hiz "$h" 2>/dev/null)
    F="$f" H="$h" BLOK="$BLOK" SAHNE="$SAHNE" DIKEY="$DIKEY" KO="$ko" \
    KART="$KART_SATIR" MUZIK="$MUZIK_SATIR" python3 <<'PY'
import os, re, subprocess
e=os.environ; f=e["F"]; h=float(e["H"]); blok=float(e["BLOK"]); n=int(e["SAHNE"])
def probe(*a):
    return subprocess.run(["ffprobe","-v","error",*a,f],capture_output=True,text=True).stdout.strip()
dur=float(probe("-show_entries","format=duration","-of","csv=p=0") or 0)
wh=probe("-select_streams","v:0","-show_entries","stream=width,height","-of","csv=p=0:s=x")
w,hh=(int(x) for x in wh.split("x"))
pblok=blok/h
def mmss(t): return f"{int(t//60)}:{t%60:04.1f}"
# kesmeler: kesme_kontrol tablosu (beklenen · bulunan · fark · skor · ✅/⛔)
rows=re.findall(r"^\s*\d+\s+([0-9.]+)\s+([0-9.]+|—)\s+([0-9.]+|—)\s+([0-9.]+|—)\s+(✅|⛔)",e["KO"],re.M)
cuts=[(float(a),b,m) for a,b,_,_,m in rows if float(a) < pblok-0.01]
dar="MARJ DAR" in e["KO"]
if not rows:
    cutline="NOT MEASURED — cut detection failed; do not count cuts yourself"
elif dar or any(m=="⛔" or b=="—" for _,b,m in cuts):
    cutline="NOT MEASURED — weak cut signal; plan grid on this file: " + ", ".join(mmss(a) for a,_,_ in cuts)
else:
    cutline=", ".join(mmss(float(b)) for _,b,_ in cuts)
# kart
kalan=dur-pblok
kart_yok="⛔ YOK" in e["KART"]
if kalan>0.5:
    card=f"YES from {mmss(pblok)} to {mmss(dur)}" + ("  (the plan declares NO card — report it)" if kart_yok else "")
else:
    card="NO — the last clip is a scene, score it"
# müzik
music="NO — only site sound" if (e["DIKEY"]=="1" or "⛔ YOK" in e["MUZIK"]) else "YES"
# final tutuşu: blok sonu − 0,05 ile (2,0/h) öncesi arasında SSIM
def kare(t,p):
    subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{max(t,0):.3f}","-i",f,"-frames:v","1",p],check=False)
import tempfile
d=tempfile.mkdtemp(); a=f"{d}/a.png"; b=f"{d}/b.png"
tut=2.0/h; son=min(pblok,dur)-0.15   # son kare: dosya bloktan kısa olabilir (kare zaman damgası)
kare(son,a); kare(son-tut,b)
r=subprocess.run(["ffmpeg","-v","info","-i",a,"-i",b,"-lavfi","ssim","-f","null","-"],capture_output=True,text=True)
m=re.search(r"All:([0-9.]+)",r.stderr)
if m:
    s=float(m.group(1))
    hold=f"the last {tut:.1f} s of the scene block are {'static' if s>=0.90 else 'still changing'} (SSIM {s:.2f})"
else:
    hold="NOT MEASURED"
clipsec=f"{8.0/h:.1f}" if abs(pblok/n-8.0/h)<0.05 else f"{pblok/n:.1f} on average (plan lengths vary)"
asp="9:16" if hh>w else "16:9"
out={"SPEED":f"{h:g}","CLIP_COUNT":str(n),"CLIP_SECONDS":clipsec,"CUTS":cutline,"END_CARD":card,
     "MUSIC":music,"ASPECT":f"{asp} ({w}x{hh})","DURATION":mmss(dur),"FINAL_HOLD":hold}
for k,v in out.items(): print(f"OLGU_{k}={v}")
PY
}

echo "📏 ölçülmüş olgular · yayın dosyası (${HIZ}x) → ❶ ❷ ❺"
OLGU_YAYIN="$(olgular "$MP4" "$HIZ")" || { echo "⛔ ölçüm düştü"; exit 2; }
echo "$OLGU_YAYIN" | sed 's/^OLGU_/   /'
OLGU_MASTER="$OLGU_YAYIN"
if [ -n "$MASTER" ]; then
    echo "📏 ölçülmüş olgular · master (1x) → ❸ ❹"
    OLGU_MASTER="$(olgular "$MASTER" 1)" || { echo "⛔ master ölçümü düştü"; exit 2; }
    echo "$OLGU_MASTER" | sed 's/^OLGU_/   /'
fi

# ── paketler ──────────────────────────────────────────────────────
OUT="QA/KOSU/$FILM"; [ -n "$BOLUM" ] && OUT="$OUT/B$BOLUM"; mkdir -p "$OUT"
HAMDIR="QA/HAM/$FILM"; ONEK="${FILM}_${BOLUM:+B${BOLUM}_}"

paket() {  # <Qn_AD> <mod V|D> <dosya: yayin|master> <girdi satırları>
    local q="$1" mod="$2" hangi="$3" girdi="$4" f olgu video
    f="$OUT/${q}_paket.md"
    if [ "$hangi" = "master" ] && [ -n "$MASTER" ]; then olgu="$OLGU_MASTER"; video="$MASTERABS"
    else olgu="$OLGU_YAYIN"; video="$MP4ABS"; fi
    girdi="$(echo "$girdi" | sed "s|@VIDEO@|$video|")"
    {
        echo "# PAKET · $FILM · $q · mod $mod"
        echo
        echo "⛔ YALITIM: AYRI ve GEÇİCİ sohbet · Gemini projesi/Gem DIŞINDA [QA_KOSU §1]."
        [ "$mod" = "V" ] && echo "⛔ KÖR MERCEK — aşağıdaki dosyalardan BAŞKA hiçbir şey verilmez (plan · SPEC · kapak YOK)."
        [ "$mod" = "D" ] && echo "⭐ BELGELİ MERCEK — belgeler bu sohbete ELLE eklenir; ilk satırları film adını taşımalı."
        [ "$GUNLUKSUZ" -eq 1 ] && echo "⚠️  ÜRETİM GÜNLÜĞÜ YOK — bulgular prompt/üretim ayrımı yapamaz."
        echo
        echo "EKLENECEK DOSYALAR (tam yol):"
        echo "$girdi" | sed 's/^/   /'
        echo
        echo "HAM RAPOR → $HAMDIR/${ONEK}${q}_HAM.md — künye (aşağıda) üstte, model çıktısı altta, dokunmadan."
        echo
        echo '```'
        echo "---"
        echo "film:        $FILM"
        echo "mercek:      $q"
        echo "dosya:       $(basename "$video") · sha256 $(shasum -a 256 "$video" | cut -c1-12) · $(echo "$olgu" | sed -n 's/^OLGU_DURATION=//p') · $(echo "$olgu" | sed -n 's/^OLGU_ASPECT=//p') · $(echo "$olgu" | sed -n 's/^OLGU_SPEED=//p')x"
        if [ "$mod" = "V" ]; then echo "belgeler:    YOK (kör mercek)"
        else echo "$girdi" | grep -E '\.md$' | while read -r b; do echo "belgeler:    $(basename "$b") (\"$(head -1 "$b" | cut -c1-70)\")"; done; fi
        local rh; rh=$(git log -1 --format=%h -- "QA/$q.md" 2>/dev/null)
        git diff --quiet HEAD -- "QA/$q.md" 2>/dev/null || rh="${rh:+$rh+}commit edilmemiş değişiklik"
        echo "rubrik:      QA/$q.md @ ${rh:-commit edilmemiş}"
        echo "model:       Gemini <sürüm> · sohbet | API · proje DIŞI · geçici sohbet ✓   ← koşan doldurur"
        echo "tarih:       $(date '+%d.%m.%Y')"
        echo "geri_okuma:  dosya adı ✓/✗ · belge başlığı ✓/✗ · görülen klip <n>         ← ajan doldurur"
        echo "durum:       TAM | EKSİK | YANLIŞ GİRDİ | SIZINTI | TUTARSIZ                 ← ajan doldurur"
        echo "---"
        echo '```'
        echo
        echo "────────────────────────────── RUBRİK — buradan aşağısı yapıştırılır ──"
        echo
        OLGU="$olgu" python3 -c '
import os,sys
t=open(sys.argv[1],encoding="utf-8").read()
for l in os.environ["OLGU"].splitlines():
    k,v=l[5:].split("=",1); t=t.replace("{"+k+"}",v)
sys.stdout.write(t)' "QA/$q.md"
    } > "$f"
    local kalan; kalan=$(grep -oE '\{(SPEED|CLIP_COUNT|CLIP_SECONDS|CUTS|END_CARD|MUSIC|ASPECT|DURATION|FINAL_HOLD)\}' "$f" | sort -u | tr '\n' ' ')
    [ -z "$kalan" ] || echo "   ⛔ $q: doldurulmamış yer tutucu: $kalan"
    printf "   %-16s %s → %s\n" "$q" "$mod" "$f"
}

echo
echo "📦 QA PAKET · $FILM · yayın ${HIZ}x$( [ -n "$MASTER" ] && echo ' · master 1x') · $KARE_SAYISI kare"
[ -n "$KAPAKABS" ] || echo "   ⚠️ kapak verilmedi — ❺ TESLİM'in kapak kategorisi NOT VERIFIABLE kalır"
echo "   ⭐ SIRA: kör mercekler ÖNCE (Q1 Q2 Q3), sonra belgeliler (Q4 Q5)."
paket Q1_GORUNTU     V yayin  "@VIDEO@
$KARELER/ (tüm kareler)"
paket Q2_ZAMAN_KESME V yayin  "@VIDEO@"
paket Q3_SANTIYE     V master "@VIDEO@
$KARELER/ (tüm kareler · dikiş çiftleri S<n>_son + S<n+1>_ilk)"
paket Q4_INSA        D master "@VIDEO@
$SPECABS
$PLANABS"
paket Q5_TESLIM      D yayin  "@VIDEO@
$PLANABS
${KAPAKABS:-⚠️ KAPAK YOK}"
echo
echo "⛔ Rapor geldiğinde: $HAMDIR/${ONEK}Q<n>_<AD>_HAM.md — künye + model çıktısı, dokunmadan."
echo "   Sonra: geri okuma · D1–D5 · durum · QA/FILMLER/$FILM.md · QA/TABLO.md [QA/00_README §3]."
