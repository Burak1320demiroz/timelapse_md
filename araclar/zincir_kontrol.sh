#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  ZİNCİR KONTROL — ÜRETİM ARASI KAPI  [DERS 12]
#
#  NEDEN VAR:
#  Ters inşa zinciri iki filmde de atlandı ve iki film de bu yüzden
#  düştü (THE LONG SHADOW: 3 farklı bina · THE CLOSING SPAN: 8 farklı
#  vantaj, 9/9 dikiş DEFECT). Kural her iki seferde de YAZILIYDI.
#
#  ⭐ Yazılı kural kapı değildir. Kapı KOŞULAN bir şeydir.
#  prompt_kontrol.py metni denetler; üretim SIRASINI denetleyemez.
#  Bu betik o boşluğu kapatır.
#
#  KULLANIM
#    ÜRETİM SIRASINDA (asıl kullanım — her yeni kareden sonra):
#       bash araclar/zincir_kontrol.sh <onceki_onayli.png> <yeni.png>
#
#    TESLİM SONRASI (bütün seriyi tara):
#       bash araclar/zincir_kontrol.sh <kareler_klasoru>
#
#  NE ÖLÇER:
#  Kamera istasyonu aynıysa kadrajın KENARLARI (çapaların yaşadığı yer)
#  sahneden sahneye neredeyse aynı kalır; değişen şey MERKEZDİR (yapı).
#  İstasyon değişmişse ya da dünya yeniden üretilmişse KENARLAR da bozulur.
#
#  ⚠️ EŞİKLER PROVİZYONDUR — bu depoda henüz kalibre edilmedi. Betiğin
#     asıl değeri MUTLAK sayıda değil, SERİ İÇİNDEKİ SAPMADA: bir çift
#     diğerlerinden belirgin biçimde düşükse istasyon orada kaymıştır.
# ═══════════════════════════════════════════════════════════════════
set -u
command -v ffmpeg >/dev/null || { echo "⛔ ffmpeg yok"; exit 2; }
[ $# -ge 1 ] || { sed -n '/KULLANIM/,/kareler_klasoru/p' "$0" | sed 's/^#//'; exit 2; }

# provizyon eşikler
ESIK_KENAR=0.80     # sol+sağ şerit ortalaması bunun altındaysa DUR
ESIK_ALT=0.70       # alt bant (ön plan zemin)
ESIK_GLOBAL=0.20    # bütün kare — bunun altı "başka bir yer" demektir

ssim() {  # <a> <b> <crop ifadesi veya BOS>
    local a="$1" b="$2" c="${3:-}"
    local fc
    if [ -z "$c" ]; then
        fc="[0:v][1:v]ssim=stats_file=-"
    else
        fc="[0:v]${c}[x0];[1:v]${c}[x1];[x0][x1]ssim=stats_file=-"
    fi
    ffmpeg -v error -i "$a" -i "$b" -filter_complex "$fc" -f null - 2>&1 \
      | grep -oE "All:[0-9.]+" | head -1 | cut -d: -f2
}

cift() {  # <a> <b> <etiket>
    local a="$1" b="$2" et="$3"
    local g l r alt kenar durum
    g=$(ssim "$a" "$b" "")
    l=$(ssim "$a" "$b" "crop=iw*0.12:ih:0:0")
    r=$(ssim "$a" "$b" "crop=iw*0.12:ih:iw*0.88:0")
    alt=$(ssim "$a" "$b" "crop=iw:ih*0.12:0:ih*0.88")
    kenar=$(awk -v l="$l" -v r="$r" 'BEGIN{printf "%.4f", (l+r)/2}')
    durum="✅"
    awk -v k="$kenar" -v e="$ESIK_KENAR" 'BEGIN{exit !(k<e)}' && durum="⛔ KENAR"
    awk -v k="$alt"   -v e="$ESIK_ALT"   'BEGIN{exit !(k<e)}' && durum="⛔ ALT"
    awk -v k="$g"     -v e="$ESIK_GLOBAL" 'BEGIN{exit !(k<e)}' && durum="⛔ BAŞKA YER"
    printf "  %-16s global %-8s sol %-8s sağ %-8s alt %-8s | kenar %-8s %s\n" \
           "$et" "$g" "$l" "$r" "$alt" "$kenar" "$durum"
    [ "${durum:0:1}" = "⛔" ] && return 1 || return 0
}

echo "═══════════════════════════════════════════════════════════════"
echo "  ZİNCİR KONTROL · $(date '+%d.%m.%Y %H:%M')"
echo "═══════════════════════════════════════════════════════════════"
echo "  ölçülen: kadraj KENARLARI (çapaların yaşadığı yer) sabit mi"
echo "  eşikler PROVİZYON — asıl sinyal seri içindeki SAPMADIR"
echo

HATA=0
if [ -d "$1" ]; then
    # ⚠️ macOS bash 3.2: mapfile YOK. Taşınabilir tutuluyor.
    LISTE=$(ls -1 "${1%/}"/*_ilk.* 2>/dev/null | sort -V)
    N=$(printf '%s\n' "$LISTE" | grep -c . )
    [ "$N" -ge 2 ] || { echo "⛔ en az iki '*_ilk' karesi gerek (bulunan: $N)"; exit 2; }
    echo "📁 seri modu · $N kare"
    ONCEKI=""
    while IFS= read -r KARE; do
        [ -n "$KARE" ] || continue
        if [ -n "$ONCEKI" ]; then
            et="$(basename "$ONCEKI" | sed 's/_ilk\..*//')→$(basename "$KARE" | sed 's/_ilk\..*//')"
            cift "$ONCEKI" "$KARE" "$et" || HATA=$((HATA+1))
        fi
        ONCEKI="$KARE"
    done <<EOF
$LISTE
EOF
else
    [ $# -ge 2 ] || { echo "⛔ iki dosya ver: <onceki> <yeni>"; exit 2; }
    echo "🔗 üretim modu"
    cift "$1" "$2" "önceki→yeni" || HATA=1
fi

echo
if [ "$HATA" -gt 0 ]; then
cat <<'NOT'
⛔ ZİNCİR KIRILDI — ÜRETİME DEVAM ETME.
   Yeni kare bir öncekinin KARESİNDEN türetilmemiş: kamera istasyonu
   kaymış ya da arka plan yeniden üretilmiş.
   YAPILACAK: bu kareyi at, önceki ONAYLI kareye dön ve image-to-image
   ile yeniden türet. Sonraki sahneleri ÜRETME — zincir kırıkken üretilen
   her kare kaybedilmiş bir karedir.
NOT
    exit 2
fi
echo "✅ ZİNCİR SAĞLAM — sonraki sahneye geçilebilir."
echo "═══════════════════════════════════════════════════════════════"
