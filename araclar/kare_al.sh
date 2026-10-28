#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  KARE AL — ① KARE QA'nın makine ön koşusu
#
#  İKİ MERCEĞE BİRDEN HİZMET EDER:
#    ① KARE       "kadraj kaydı mı" sorusu bir MODELE değil bir SAYIYA sorulur
#    ⑤ DEVAMLILIK ⭐ DİKİŞ DENETİMİ — sahne N'in SON karesi ile N+1'in İLK
#                 karesi yan yana konur; ⑤'in çekirdek kategorisi budur.
#  Her klibin İLK · ORTA · SON karesi çıkarılır.
#
#  KULLANIM
#     bash araclar/kare_al.sh <teslim.mp4> [klip_sayisi] [sahne_blogu_sn]   tek dosya (varsayılan 10)
#        ⭐ 05.10.2026: sahne_blogu_sn verilirse klipler YALNIZ o süreye bölünür — kart
#           klip sayılmaz (dikey 2x paylaşım: 7 klip · 28 sn) [DERS 63]
#     bash araclar/kare_al.sh <klipler_klasoru/>             klip klasörü
#
#  ÇIKTI:  tek dosya   <dosya_dizini>/QA_KARELER/<dosya_adı>/ · S<n>_{ilk,orta,son}.jpg · KAYNAK.txt
#          klasör      <klipler_klasoru>/QA_KARELER/
#  ⭐ 28.10.2026: tek dosya modu dosya başına ALT KLASÖRE yazar ve KAYNAK.txt'ye dosyanın sha256'sını
#     koyar. Eskiden ~/Downloads'taki her yayın dosyası aynı QA_KARELER/'e düşüyordu ve qa_paket.sh
#     dolu klasörü yeniden kullanıyordu: ikinci filmin paketi BİRİNCİ filmin karelerini gösterirdi
#     (aynı çakışma ihrac_kontrol'de ölçüldü — DENETİM 28.10.2026 · A4).
# ═══════════════════════════════════════════════════════════════════
set -u

command -v ffmpeg  >/dev/null || { echo "⛔ ffmpeg yok"; exit 2; }
command -v ffprobe >/dev/null || { echo "⛔ ffprobe yok"; exit 2; }

[ $# -ge 1 ] || { sed -n '4,16p' "$0" | sed 's/^#//'; exit 2; }
GIRDI="$1"
KLIP_SAYISI="${2:-10}"
BLOK_SN="${3:-}"

sure() { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"; }

cikar() {  # <dosya> <baslangic_sn> <bitis_sn> <etiket> <hedef_dizin>
    local f="$1" b="$2" s="$3" et="$4" d="$5"
    local orta; orta=$(awk -v b="$b" -v s="$s" 'BEGIN{printf "%.3f", b+(s-b)/2}')
    local son;  son=$(awk  -v s="$s" 'BEGIN{printf "%.3f", s-0.05}')
    ffmpeg -v error -y -ss "$b"    -i "$f" -frames:v 1 "$d/${et}_ilk.jpg"
    ffmpeg -v error -y -ss "$orta" -i "$f" -frames:v 1 "$d/${et}_orta.jpg"
    ffmpeg -v error -y -ss "$son"  -i "$f" -frames:v 1 "$d/${et}_son.jpg"
    printf "   %-6s ilk %-8s orta %-8s son %-8s\n" "$et" "$b" "$orta" "$son"
}

if [ -d "$GIRDI" ]; then
    HEDEF="${GIRDI%/}/QA_KARELER"; mkdir -p "$HEDEF"
    echo "📁 klip klasörü modu"
    n=0
    for f in "${GIRDI%/}"/*.mp4 "${GIRDI%/}"/*.mov; do
        [ -f "$f" ] || continue
        s=$(sure "$f"); cikar "$f" 0 "$s" "S$n" "$HEDEF"; n=$((n+1))
    done
    echo "   $n klip · $((n*3)) kare"
else
    [ -f "$GIRDI" ] || { echo "⛔ dosya yok: $GIRDI"; exit 2; }
    AD="$(basename "$GIRDI")"; HEDEF="$(dirname "$GIRDI")/QA_KARELER/${AD%.*}"; mkdir -p "$HEDEF"
    rm -f "$HEDEF"/S*_ilk.jpg "$HEDEF"/S*_orta.jpg "$HEDEF"/S*_son.jpg   # eski kesimden kare kalmasın
    echo "sha256 $(shasum -a 256 "$GIRDI" | cut -c1-12) · $AD · $(date '+%d.%m.%Y %H:%M')" > "$HEDEF/KAYNAK.txt"
    TOPLAM=$(sure "$GIRDI")
    [ -n "$BLOK_SN" ] && TOPLAM="$BLOK_SN"
    KLIP=$(awk -v t="$TOPLAM" -v n="$KLIP_SAYISI" 'BEGIN{printf "%.4f", t/n}')
    echo "🎬 tek dosya modu · toplam ${TOPLAM}s · $KLIP_SAYISI klip · klip ${KLIP}s"
    echo "   ⚠️ klipler EŞİT varsayıldı. Değillerse klip klasörü moduyla koş."
    for i in $(seq 0 $((KLIP_SAYISI-1))); do
        b=$(awk -v k="$KLIP" -v i="$i" 'BEGIN{printf "%.3f", k*i}')
        s=$(awk -v k="$KLIP" -v i="$i" 'BEGIN{printf "%.3f", k*(i+1)}')
        cikar "$GIRDI" "$b" "$s" "S$i" "$HEDEF"
    done
fi

cat <<'NOT'

═══════════════════════════════════════════════════════
  ŞİMDİ NE YAPILIR — ①'in sayıya çevrilen kısmı
═══════════════════════════════════════════════════════
  ① KARE için
     1. Aynı istasyondan çekilmiş sahneleri grupla.
     2. Grubun her klibinin İLK karesinde ölç: ufuk yüzdesi ve en yüksek
        arka plan nesnesinin tepesi.
     3. Grup içindeki YAYILIM 2 puandan büyükse → ① KATEGORİ 2 DÜŞER.

  ⑤ DEVAMLILIK için  ⭐ DİKİŞ ÇİFTLERİ
     S<n>_son.jpg  ile  S<n+1>_ilk.jpg  yan yana konur — her dikiş için bir çift.
     Her çiftte DEĞİŞEN her şey listelenir ve ikiye ayrılır:
        INTENDED  zamanın üreteceği değişim (yapı ilerledi, mevsim döndü)
        DEFECT    zamanın üretmeyeceği değişim (makine tip değiştirdi,
                  konteyner yer değiştirdi, çamur sıfırlandı)

  Kareleri rubriklerle birlikte ver: QA/Q1_GORUNTU.md · QA/Q3_SANTIYE.md
  ⛔ İkisine de PLAN VERİLMEZ — mod V.
NOT
