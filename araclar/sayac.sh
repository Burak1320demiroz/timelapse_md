#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  SAYAÇ — belgelerdeki sayıları hesaplar, kimse elle yazmasın
#
#  KULLANIM:  bash araclar/sayac.sh
#  Belgeye sayı yazmadan önce bunu çalıştır.
# ═══════════════════════════════════════════════════════════════════
cd "$(dirname "$0")/.." || exit 1

echo "═══════════════════════════════════════════════════════"
echo "  SAYAÇ · $(date '+%d.%m.%Y %H:%M')"
echo "═══════════════════════════════════════════════════════"
echo

# ─── FİLMLER ───────────────────────────────────────────────────────
echo "🏗️  FİLMLER"
# ⭐ 14.09.2026: beş format klasörü — dikey_shorts (plan = _DIKEY_TIMELAPSE.md) +
#    yatay merdiven 2/4/6/8 dk (plan = _PLAN.md, KILAVUZ_REHBERI §2.8). Köke .md bırakılmaz.
FORMATLAR="dikey_shorts yatay_2_dk_filmler yatay_4_dk_filmler yatay_6_dk_filmler yatay_8_dk_filmler yatay_12_dk_filmler"
TOPLAM=0; PLANLI=0; SPECLI=0; GUNLUKLU=0; DIKEY=0; YATAY=0
for fmt in $FORMATLAR; do
  for d in "$fmt"/*/; do
    [ -d "$d" ] || continue
    TOPLAM=$((TOPLAM + 1))
    [ "$fmt" = "dikey_shorts" ] && DIKEY=$((DIKEY + 1)) || YATAY=$((YATAY + 1))
    ls "$d" 2>/dev/null | grep -qE "_(DIKEY_TIMELAPSE|PLAN)\.md$" && PLANLI=$((PLANLI + 1))
    ls "$d" 2>/dev/null | grep -q "_QA_SPEC\.md$"         && SPECLI=$((SPECLI + 1))
    ls "$d" 2>/dev/null | grep -q "_URETIM_GUNLUGU\.md$"  && GUNLUKLU=$((GUNLUKLU + 1))
  done
done
printf "   film klasörü          %s   (dikey %s · yatay %s)\n" "$TOPLAM" "$DIKEY" "$YATAY"
for fmt in $FORMATLAR; do
    [ -d "$fmt" ] || { printf "   ⛔ format klasörü yok: %s\n" "$fmt"; continue; }
    KOK_MD=$(ls -1 "$fmt"/*.md 2>/dev/null | grep -vE "README\.md$|URETIM_GUNLUGU_SABLONU\.md$" | wc -l | tr -d ' ')
    [ "$KOK_MD" -gt 0 ] && printf "   ⛔ %s kökünde %s başıboş .md — köke yalnız README durur\n" "$fmt" "$KOK_MD"
done
printf "   planı olan            %s / %s" "$PLANLI" "$TOPLAM"
[ "$PLANLI" -lt "$TOPLAM" ] && printf "   ⛔ %s klasör plansız" "$((TOPLAM - PLANLI))"; echo
printf "   SPEC'i olan           %s / %s" "$SPECLI" "$TOPLAM"
[ "$SPECLI" -lt "$TOPLAM" ] && printf "   ⛔ %s film SPEC'siz → final kare kanıtı koşulamaz" "$((TOPLAM - SPECLI))"; echo
printf "   üretim günlüğü olan  %s / %s" "$GUNLUKLU" "$TOPLAM"
[ "$GUNLUKLU" -lt "$TOPLAM" ] && printf "   ⚠️ günlüksüz filme QA paketi açılmaz [DERS 28]"; echo
echo

# ─── DERSLER ───────────────────────────────────────────────────────
echo "📚 DERSLER"
DERS=$(grep -cE "^## DERS [0-9]+" kilavuzlar/DERSLER.md 2>/dev/null | tr -d ' ')
# ⭐ 08.10.2026: varsayımlar DERSLER.md'den ayrıldı. Sayım DİZİN satırlarından: | KOD | başlık | kaynak | durum |
KOD_SATIRI='^\| (D|F1|A[0-9]+|C[0-9]|P[0-9]+)-[a-z] \|'
VARSAYIM=$(grep -cE "^\| D-[a-z] \|" kilavuzlar/VARSAYIMLAR.md 2>/dev/null | tr -d ' ')
ARASTIRMA=$(grep -cE "^\| (A[0-9]+|C[0-9]|F1)-[a-z] \|" kilavuzlar/VARSAYIMLAR.md 2>/dev/null | tr -d ' ')
PLANOKUMA=$(grep -cE "^\| P[0-9]+-[a-z] \|" kilavuzlar/PLAN_OKUMALARI.md 2>/dev/null | tr -d ' ')
D_ACIK=$(cat kilavuzlar/VARSAYIMLAR.md kilavuzlar/PLAN_OKUMALARI.md 2>/dev/null | grep -E "$KOD_SATIRI" | grep -c '| ⬜ açık')
D_OLC=$(cat kilavuzlar/VARSAYIMLAR.md kilavuzlar/PLAN_OKUMALARI.md 2>/dev/null | grep -E "$KOD_SATIRI" | grep -c '| ✅ ölçüldü')
D_DUS=$(cat kilavuzlar/VARSAYIMLAR.md kilavuzlar/PLAN_OKUMALARI.md 2>/dev/null | grep -E "$KOD_SATIRI" | grep -c '| ❌ düştü')
HAM_ARASTIRMA=$(ls -1 arastirma/SONUCLAR/[AP]*_HAM.md 2>/dev/null | wc -l | tr -d ' ')
printf "   ölçülmüş ders         %s   (DERSLER.md)\n" "${DERS:-0}"
printf "   devralınan varsayım   %s   ⚠️ film_md'den · VARSAYIMLAR.md D\n" "${VARSAYIM:-0}"
printf "   dış okuma varsayımı   %s   ⚠️ araştırma + sentez · VARSAYIMLAR.md A · C · F1\n" "${ARASTIRMA:-0}"
printf "   plan okuması kodu     %s   ⚠️ uzman okuması + plan kararı · PLAN_OKUMALARI.md P\n" "${PLANOKUMA:-0}"
printf "   kod durumu            ⬜ açık %s · ✅ ölçüldü %s · ❌ düştü %s   (DİZİN durum sütunu)\n" "${D_ACIK:-0}" "${D_OLC:-0}" "${D_DUS:-0}"
printf "   işlenmiş ham rapor    %s   (arastirma/SONUCLAR)\n" "${HAM_ARASTIRMA:-0}"
PROMPT_SAYI=$(ls -1 arastirma/A[0-9]*_*.md 2>/dev/null | wc -l | tr -d ' ')
# koşulan = promptu olan ve ham raporu gelen kod · promptsuz gelen (A13–A19) ayrı sayılır
KOSULAN=0; KOSULMAYAN=""
for pf in arastirma/A[0-9]*_*.md; do
    [ -f "$pf" ] || continue; k=$(basename "$pf" | sed 's/_.*//')
    if ls arastirma/SONUCLAR/${k}_*HAM.md >/dev/null 2>&1; then KOSULAN=$((KOSULAN + 1)); else KOSULMAYAN="$KOSULMAYAN $k"; fi
done
PROMPTSUZ=$(ls -1 arastirma/SONUCLAR/A[0-9]*_*_HAM.md 2>/dev/null | sed 's/.*\/\(A[0-9]*\)_.*/\1/' | sort -u \
            | while read -r k; do ls arastirma/${k}_*.md >/dev/null 2>&1 || echo "$k"; done | grep -c .)
printf "   araştırma promptu     %s   (koşulan %s · ⛔ koşulmayan %s%s · promptsuz gelen rapor %s)\n" \
       "${PROMPT_SAYI:-0}" "$KOSULAN" "$(( ${PROMPT_SAYI:-0} - KOSULAN ))" "${KOSULMAYAN:+ ·$KOSULMAYAN}" "$PROMPTSUZ"
[ "${ARASTIRMA:-0}" -gt 0 ] && [ "${HAM_ARASTIRMA:-0}" -eq 0 ] && \
  echo "   ⛔ kodlu varsayım var ama ham rapor YOK — kaynak kaybolmuş"
echo

# ─── KILAVUZ HACMİ ─────────────────────────────────────────────────
echo "📄 BELGE HACMİ"
printf "   kılavuz dosyası       %s\n" "$(ls -1 kilavuzlar/*.md 2>/dev/null | wc -l | tr -d ' ')"
printf "   toplam satır          %s\n" "$(cat kilavuzlar/*.md 2>/dev/null | wc -l | tr -d ' ')"
printf "   en büyük dosya        %s\n" "$(wc -l kilavuzlar/*.md 2>/dev/null | sort -rn | sed -n 2p | awk '{n=split($2,a,"/"); print a[n]" ("$1" satır)"}')"
echo
echo "   ⚠️ Dosya sayısı bir başarı ölçüsü DEĞİLDİR. film_md 40+ kılavuzla"
echo "      çekirdek arızasını engelleyemedi. Dosya ancak bir DERS taşıyorsa açılır."
echo

# ─── PROMPT KAPISI DURUMU ──────────────────────────────────────────
echo "🚪 PROMPT KAPISI"
if [ "$PLANLI" -eq 0 ]; then
    echo "   (henüz plan yok)"
else
    ZINCIRLI=0
    for f in dikey_shorts/*/*_DIKEY_TIMELAPSE.md yatay_*_dk_filmler/*/*_PLAN.md; do
        [ -f "$f" ] || continue
        # yatay iskelet: kapı KLASÖR MODUNDA koşar (PLAN + BOLUM_1 + BOLUM_2 birleşik)
        case "$f" in *_PLAN.md) hedef="$(dirname "$f")" ;; *) hedef="$f" ;; esac
        rapor=$(python3 araclar/prompt_kontrol.py "$hedef" 2>/dev/null)
        out=$(echo "$rapor" | tail -1)
        # ⭐ format [KILAVUZ_REHBERI §2.7]: usta karesi olan plan ZİNCİRLİDİR
        if echo "$rapor" | grep -q "ESKİ FORMAT"; then
            fmt="⛔ eski format"
        else
            fmt="⭐ zincirli"
            ZINCIRLI=$((ZINCIRLI + 1))
        fi
        printf "   %-45s %-16s %s\n" "$(basename "$f")" "$fmt" "$out"
    done
    printf "   ⭐ İKİ KEYFRAME ZİNCİRİ %s / %s plan   [KILAVUZ_REHBERI §2.7]\n" \
           "$ZINCIRLI" "$PLANLI"
fi
echo

# ─── QA DURUMU ─────────────────────────────────────────────────────
# tablo_satir: dosyadaki ilk markdown tablosunun VERİ satırlarını basar.
# Başlık + ayraç düşer. Tablo içindeki boş satır tabloyu BÖLMEZ — kardeş
# depoda tam bu yüzden altı tablonun altısı da "0 satır" sayılmıştı.
tablo_satir() {
    awk '/^\|/{n++; if(n>2)print; next}
         /^[[:space:]]*$/{next}
         n>0{exit}' "$1" 2>/dev/null
}
tablo_say() { tablo_satir "$1" | grep -c . ; }

# ⭐ 06.10.2026: beş mercek · QA/TABLO.md tek sayaç · eski 12 mercek ARSIV_12_MERCEK/ (dondurulmuş)
echo "🔍 QA — BEŞ MERCEK"
for q in Q1_GORUNTU Q2_ZAMAN_KESME Q3_SANTIYE Q4_INSA Q5_TESLIM; do
    [ -f "QA/$q.md" ] && printf "   ✅ %-16s rubrik\n" "$q" || printf "   ⛔ %-16s rubrik YOK\n" "$q"
done
TSATIR=$(awk '/^## FİLM × MERCEK/{p=1} p' QA/TABLO.md 2>/dev/null | tablo_satir /dev/stdin | grep -c .)
HAMYENI=$(find QA/HAM -name "*_HAM*.md" 2>/dev/null | wc -l | tr -d ' ')
HAMFILM=$(find QA/HAM -name "*_HAM*.md" 2>/dev/null | awk -F/ '{print $3}' | sort -u | grep -c .)
printf "   ham rapor (yeni)  %s · %s film · TABLO satırı %s\n" "$HAMYENI" "$HAMFILM" "$TSATIR"
# U1 kanıt var, kayıt yok · U2 kayıt var, kanıt yok [QA_KAYIT §5]
for d in QA/HAM/*/; do
    [ -d "$d" ] || continue; f=$(basename "$d")
    grep -qE "^\| $(echo "$f" | tr '_' ' ') \|" QA/TABLO.md 2>/dev/null || printf "   ❌ U1 %s — ham rapor var, TABLO'da satır yok\n" "$f"
done
awk '/^## FİLM × MERCEK/{p=1} p' QA/TABLO.md 2>/dev/null | tablo_satir /dev/stdin | awk -F'|' '{c=$2; gsub(/^[ \t]+|[ \t]+$/,"",c); gsub(/ /,"_",c); print c}' \
  | while read -r f; do [ -z "$f" ] || [ -d "QA/HAM/$f" ] || printf "   ❌ U2 %s — TABLO'da satır var, ham klasörü yok\n" "$f"; done
HAMARSIV=$(find QA/ARSIV_12_MERCEK/HAM_RAPORLAR -name "*_HAM.md" 2>/dev/null | wc -l | tr -d ' ')
ESLEME=$(($(wc -l < QA/ARSIV_12_MERCEK/00_ESLEME.tsv 2>/dev/null || echo 1) - 1))
printf "   arşiv (12 mercek) %s ham · eşleme %s satır" "$HAMARSIV" "$ESLEME"
[ "$HAMARSIV" = "$ESLEME" ] && printf " ✅\n" || printf " ❌ eşleme tablosu ham sayısını tutmuyor\n"

# TABLO karşılaştırması — sayı tek yerde durur, ama DOĞRULANIR
IDX=$(grep -oE "TOPLAM FİLM +[0-9]+" QA/TABLO.md 2>/dev/null | grep -oE "[0-9]+" | head -1)
if [ "${IDX:-x}" = "$TOPLAM" ]; then
    printf "   ✅ TABLO tutarlı (TABLO da %s diyor)\n" "$IDX"
else
    printf "   ❌ TABLO TUTMUYOR — TABLO %s diyor, dosya sistemi %s sayıyor\n" "${IDX:-?}" "$TOPLAM"
fi
echo

echo "═══════════════════════════════════════════════════════"
