#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  QA PAKET — koşu YORDAMINI araca bağlar  [DERS 29]
#
#  NEDEN VAR:
#  Beş filmde beş kez aynı şey oldu: kare grabı alınmadı, mod D
#  merceklerine belge verilmedi. DERS 17 belgeyi erken yazdırdı, DERS 27
#  "girdi satırı" yordamını yazdırdı — ikisi de yazılı kaldı ve LONG DAY'de
#  sekiz merceğin sekizi de RUN INCOMPLETE ile açıldı.
#  ⭐ Yazılı yordam koşmaz [DERS 12]. Bu betik koşuyu PAKETLER: her mercek
#     için "verilen girdiler:" satırı + eklenecek dosyaların tam yolu +
#     rubriğin tam metni tek dosyada. Koşan kişi dosyayı açar, yapıştırır.
#
#  KULLANIM
#     bash araclar/qa_paket.sh <film_klasoru> <teslim.mp4> [kapak.png]
#     örn: bash araclar/qa_paket.sh dikey_shorts/THE_LONG_DAY teslim/long_day.mp4 teslim/kapak.png
#
#  ÇIKTI:  QA/KOSU/<FILM>/<n>_<MERCEK>_paket.md   (8 dosya)
#          + kare grabları: <teslim_dizini>/QA_KARELER/  (yoksa kare_al.sh koşulur)
#
#  ⛔ KAPI: film klasöründe <FILM>_URETIM_GUNLUGU.md yoksa DURUR [DERS 28].
#     Günlüksüz filmde QA, prompt arızasını üretim arızasından ayıramaz.
#     Bile bile geçmek için: --gunluksuz  (paketlerin başına uyarı yazılır)
# ═══════════════════════════════════════════════════════════════════
set -u
cd "$(dirname "$0")/.." || exit 2

GUNLUKSUZ=0
if [ "${1:-}" = "--gunluksuz" ]; then GUNLUKSUZ=1; shift; fi
[ $# -ge 2 ] || { sed -n '/KULLANIM/,/gunluksuz/p' "$0" | sed 's/^#//'; exit 2; }

DIR="${1%/}"; MP4="$2"; KAPAK="${3:-}"
FILM="$(basename "$DIR")"
PLAN="$DIR/${FILM}_DIKEY_TIMELAPSE.md"
SPEC="$DIR/${FILM}_QA_SPEC.md"
GUNLUK="$DIR/${FILM}_URETIM_GUNLUGU.md"

[ -f "$PLAN" ] || { echo "⛔ plan yok: $PLAN"; exit 2; }
[ -f "$SPEC" ] || { echo "⛔ SPEC yok: $SPEC"; exit 2; }
[ -f "$MP4"  ] || { echo "⛔ teslim yok: $MP4"; exit 2; }

if [ ! -f "$GUNLUK" ]; then
    if [ "$GUNLUKSUZ" -eq 1 ]; then
        echo "⚠️  ÜRETİM GÜNLÜĞÜ YOK ($GUNLUK) — --gunluksuz ile geçildi. Raporlar"
        echo "    prompt arızası ile üretim arızasını AYIRAMAZ; bu, kayda yazılır."
    else
        echo "⛔ ÜRETİM GÜNLÜĞÜ YOK: $GUNLUK  [DERS 28]"
        echo "   Klip başına: araç · ayar · kaynak kare · prompt birebir mi ·"
        echo "   zincir_kontrol sonucu · kanıt nesnesi elle ✓. Şablon: AGENTS kart B."
        echo "   Bile bile geçmek için: bash araclar/qa_paket.sh --gunluksuz ..."
        exit 2
    fi
fi

# ── kare grabları ─────────────────────────────────────────────────
MP4DIR="$(cd "$(dirname "$MP4")" && pwd)"
KARELER="$MP4DIR/QA_KARELER"
if [ ! -d "$KARELER" ] || [ -z "$(ls -A "$KARELER" 2>/dev/null)" ]; then
    echo "📸 kare grabı yok → kare_al.sh koşuluyor"
    SAHNE=$(grep -cE '^\| [0-9] \| [0-9]+[.,][0-9]+ \|' "$PLAN")
    [ "$SAHNE" -gt 0 ] || SAHNE=10
    bash araclar/kare_al.sh "$MP4" "$SAHNE" || { echo "⛔ kare_al.sh düştü"; exit 2; }
fi
KARE_SAYISI=$(ls -1 "$KARELER" 2>/dev/null | wc -l | tr -d ' ')

# ── paketler ──────────────────────────────────────────────────────
OUT="QA/KOSU/$FILM"; mkdir -p "$OUT"
MP4ABS="$MP4DIR/$(basename "$MP4")"
KAPAKABS=""; [ -n "$KAPAK" ] && [ -f "$KAPAK" ] && KAPAKABS="$(cd "$(dirname "$KAPAK")" && pwd)/$(basename "$KAPAK")"

paket() {  # <sira> <mercek_kodu> <rubrik> <mod> <girdi_listesi (satır satır)>
    local sira="$1" kod="$2" rubrik="$3" mod="$4" girdi="$5"
    local f="$OUT/${sira}_${kod}_paket.md"
    {
        echo "verilen girdiler: $(echo "$girdi" | sed 's|^.*/||' | paste -sd '·' - | sed 's/·/ · /g')"
        echo
        echo "⛔ YUKARIDAKİ SATIR RAPORUN İLK SATIRINA YAPIŞTIRILIR [DERS 27]."
        echo "⛔ MOD $mod — bu mercekte AŞAĞIDAKİLERDEN BAŞKA HİÇBİR ŞEY verilmez."
        [ "$GUNLUKSUZ" -eq 1 ] && echo "⚠️  ÜRETİM GÜNLÜĞÜ YOK — bu koşunun bulguları prompt/üretim ayrımı yapamaz."
        echo
        echo "EKLENECEK DOSYALAR (tam yol):"
        echo "$girdi" | sed 's/^/   /'
        echo
        echo "────────────────────────────── RUBRİK — buradan aşağısı yapıştırılır ──"
        echo
        cat "QA/$rubrik"
    } > "$f"
    printf "   %-14s %-3s → %s\n" "$kod" "$mod" "$f"
}

echo "📦 QA PAKET · $FILM"
echo "   teslim   $MP4ABS"
echo "   kareler  $KARELER ($KARE_SAYISI kare)"
[ -n "$KAPAKABS" ] && echo "   kapak    $KAPAKABS" || echo "   kapak    ⚠️ verilmedi — ④ eksik koşar"
echo "   ⭐ SIRA: mod V'ler ÖNCE (①③⑤⑦), sonra mod D (②④⑥⑧)."
echo
paket 1 KARE       1_KARE_QA.md       V "$MP4ABS
$KARELER/ (tüm kareler)"
paket 2 ZAMAN      3_ZAMAN_QA.md      V "$MP4ABS"
paket 3 DEVAMLILIK 5_DEVAMLILIK_QA.md V "$MP4ABS
$KARELER/ (tüm kareler)"
paket 4 IS         7_IS_QA.md         V "$MP4ABS
$KARELER/ (tüm kareler)"
paket 5 INSA       2_INSA_QA.md       D "$MP4ABS
$(pwd)/$SPEC"
paket 6 TESLIM     4_TESLIM_QA.md     D "$MP4ABS
$(pwd)/$PLAN
${KAPAKABS:-⚠️ KAPAK YOK}"
paket 7 GECIS      6_GECIS_QA.md      D "$MP4ABS (SESLİ)
$(pwd)/$PLAN"
paket 8 YONTEM     8_YONTEM_QA.md     D "$MP4ABS
$(pwd)/$SPEC"
echo
echo "⛔ Rapor geldiğinde: QA/HAM_RAPORLAR/${FILM}_<MERCEK>_HAM.md — dokunmadan."
echo "   İlk satırı RUN INCOMPLETE diyorsa skoru tabloya yazma, koşuyu TEKRARLA."
