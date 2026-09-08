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
TOPLAM=0; PLANLI=0; SPECLI=0; GUNLUKLU=0
for d in dikey_shorts/*/; do
    [ -d "$d" ] || continue
    TOPLAM=$((TOPLAM + 1))
    ls "$d" 2>/dev/null | grep -q "_DIKEY_TIMELAPSE\.md$" && PLANLI=$((PLANLI + 1))
    ls "$d" 2>/dev/null | grep -q "_QA_SPEC\.md$"         && SPECLI=$((SPECLI + 1))
    ls "$d" 2>/dev/null | grep -q "_URETIM_GUNLUGU\.md$"  && GUNLUKLU=$((GUNLUKLU + 1))
done
printf "   film klasörü          %s\n" "$TOPLAM"
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
VARSAYIM=$(grep -cE "^D-[a-z]  " kilavuzlar/DERSLER.md 2>/dev/null | tr -d ' ')
ARASTIRMA=$(grep -cE "^[AP][0-9]-[a-z]  " kilavuzlar/DERSLER.md 2>/dev/null | tr -d ' ')
HAM_ARASTIRMA=$(ls -1 arastirma/SONUCLAR/[AP]*_HAM.md 2>/dev/null | wc -l | tr -d ' ')
printf "   ölçülmüş ders         %s\n" "${DERS:-0}"
printf "   devralınan varsayım   %s   ⚠️ film_md'den · bu depoda ÖLÇÜLMEDİ\n" "${VARSAYIM:-0}"
printf "   dış okuma varsayımı   %s   ⚠️ araştırma + uzman okuması · bu depoda ÖLÇÜLMEDİ\n" "${ARASTIRMA:-0}"
printf "   işlenmiş ham rapor    %s   (arastirma/SONUCLAR)\n" "${HAM_ARASTIRMA:-0}"
PROMPT_SAYI=$(ls -1 arastirma/A[0-9]_*.md 2>/dev/null | wc -l | tr -d ' ')
KOSULAN=$(ls -1 arastirma/SONUCLAR/A[0-9]_*_HAM.md 2>/dev/null | sed 's/.*\/\(A[0-9]\)_.*/\1/' | sort -u | wc -l | tr -d ' ')
printf "   araştırma promptu     %s   (koşulan %s · ⛔ koşulmayan %s)\n" \
       "${PROMPT_SAYI:-0}" "${KOSULAN:-0}" "$(( ${PROMPT_SAYI:-0} - ${KOSULAN:-0} ))"
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
    for f in dikey_shorts/*/*_DIKEY_TIMELAPSE.md; do
        [ -f "$f" ] || continue
        rapor=$(python3 araclar/prompt_kontrol.py "$f" 2>/dev/null)
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

T1=$(tablo_say QA/T1_KARE.md);  T2=$(tablo_say QA/T2_INSA.md)
T3=$(tablo_say QA/T3_ZAMAN.md); T4=$(tablo_say QA/T4_TESLIM.md)
T5=$(tablo_say QA/T5_DEVAMLILIK.md); T6=$(tablo_say QA/T6_GECIS.md)
T7=$(tablo_say QA/T7_IS.md); T8=$(tablo_say QA/T8_YONTEM.md)

echo "🔍 QA — SEKİZ MERCEK"
printf "   ① KARE        %s satır\n" "$T1"
printf "   ② İNŞA        %s satır\n" "$T2"
printf "   ③ ZAMAN       %s satır\n" "$T3"
printf "   ④ TESLİM      %s satır\n" "$T4"
printf "   ⑤ DEVAMLILIK  %s satır\n" "$T5"
printf "   ⑥ GEÇİŞ       %s satır\n" "$T6"
printf "   ⑦ İŞ          %s satır\n" "$T7"
printf "   ⑧ YÖNTEM      %s satır\n" "$T8"

# ölçülen film = dört tablonun herhangi birinde adı geçen benzersiz film
OLCULEN=$(for t in T1_KARE T2_INSA T3_ZAMAN T4_TESLIM T5_DEVAMLILIK T6_GECIS T7_IS T8_YONTEM; do
              tablo_satir "QA/$t.md"
          done | awk -F'|' '{c=$2; gsub(/\*\*|~~/,"",c); gsub(/^[ \t]+|[ \t]+$/,"",c); if(c!="")print c}' \
          | sort -u | grep -c .)
printf "   ⭐ ÖLÇÜLEN FİLM   %s / %s\n" "$OLCULEN" "$TOPLAM"
[ "$OLCULEN" -lt "$TOPLAM" ] && printf "   ⛔ ÖLÇÜLMEMİŞ      %s / %s\n" "$((TOPLAM - OLCULEN))" "$TOPLAM"

# ölçüldü ama tabloya işlenmedi: ham raporu var, T tablosunda satırı yok
HAM=$(ls -1 QA/HAM_RAPORLAR/*_HAM.md 2>/dev/null | wc -l | tr -d ' ')
printf "   ham rapor         %s\n" "$HAM"

# 00_INDEX karşılaştırması — kural ①: sayı tek yerde durur, ama DOĞRULANIR
IDX=$(grep -oE "TOPLAM FİLM +[0-9]+" QA/00_INDEX.md 2>/dev/null | grep -oE "[0-9]+" | head -1)
if [ "${IDX:-x}" = "$TOPLAM" ]; then
    printf "   ✅ 00_INDEX tutarlı (INDEX de %s diyor)\n" "$IDX"
else
    printf "   ❌ 00_INDEX TUTMUYOR — INDEX %s diyor, dosya sistemi %s sayıyor\n" "${IDX:-?}" "$TOPLAM"
fi
echo

echo "═══════════════════════════════════════════════════════"
