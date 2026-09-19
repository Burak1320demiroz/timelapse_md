#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  FİLM KLASÖRÜ AÇ — yatay timelapse iskeletini kur, sahne satırlarını
#  damgala, okuma çizelgesini üret   (14.09.2026 · film_md şablonundan)
#
#  NEDEN VAR:
#  İskelet TEK YERDE tanımlı (KILAVUZ_REHBERI §2.8 · kopyalanabilir hâli
#  kilavuzlar/FILM_KLASOR_SABLONU/). Elle kopyada yer tutucular, sahne
#  damgaları ve okuma çizelgesi kaçar; prompt kapısı ilk koşuda BLOCK
#  verir ve DERS 12 tekrar eder (yazılı kural kapı değildir).
#
#  KULLANIM
#      bash araclar/film_klasoru_ac.sh <FORMAT_KLASORU> <FILM_ADI> [SAHNE_SAYISI] [KLIP_SN]
#      bash araclar/film_klasoru_ac.sh <FORMAT_KLASORU> <FILM_ADI> --cizelge
#  ÖRNEK
#      bash araclar/film_klasoru_ac.sh yatay_4_dk_filmler THE_LONG_SHELF        # 24 sahne × 10,0
#      bash araclar/film_klasoru_ac.sh yatay_2_dk_filmler THE_LONG_SHELF 12
#      bash araclar/film_klasoru_ac.sh yatay_2_dk_filmler THE_OLD_ROAD 15 8     # 15 sahne × 8,0 (16.09.2026)
#
#  FORMAT   yatay_2_dk_filmler 12 · yatay_4_dk_filmler 24 · yatay_6_dk_filmler 36 ·
#           yatay_8_dk_filmler 48   (dikey_shorts bu betiği KULLANMAZ — dört dosyalı
#           kendi iskeleti: dikey_shorts/URETIM_GUNLUGU_SABLONU.md + kart A)
#  ⛔ Var olan film klasörünün üstüne YAZMAZ (--cizelge yalnız çizelgeyi yeniler).
#  ⛔ Sahne sayısı ve klip süresi formattan gelir; farklı verilirse bandın dışıdır —
#     betik uyarır, engellemez (sahip izni + PLAN'a gerekçe).
#  ⭐ 16.09.2026: sahne sayısı TEK olabilir (2 bölüm: B1 = ilk ceil(N/2), B2 = kalan) ve
#     klip süresi parametre oldu; toplam = N × KLIP + 5,0 sn kapak kartı.
# ═══════════════════════════════════════════════════════════════════
set -u
cd "$(dirname "$0")/.." || exit 1
command -v python3 >/dev/null || { echo "⛔ python3 yok"; exit 2; }

FMT="${1:-}"; FILM="${2:-}"; ARG3="${3:-}"; ARG4="${4:-}"
if [ -z "$FMT" ] || [ -z "$FILM" ]; then
  sed -n '/KULLANIM/,/engellemez/p' "$0" | sed 's/^#//'; exit 2
fi
case "$FMT" in
  yatay_2_dk_filmler) VARSAYILAN=12 ;;
  yatay_4_dk_filmler) VARSAYILAN=24 ;;
  yatay_6_dk_filmler) VARSAYILAN=36 ;;
  yatay_8_dk_filmler) VARSAYILAN=48 ;;
  dikey_shorts) echo "⛔ dikey_shorts bu betiği kullanmaz — kart A dört dosyalı iskelet"; exit 2 ;;
  *) echo "⛔ format klasörü tanınmadı: $FMT"; exit 2 ;;
esac
[ -d "$FMT" ] || { echo "⛔ format klasörü yok: $FMT"; exit 2; }
case "$FILM" in
  *[!A-Z0-9_]*|"") echo "⛔ film adı BUYUK_HARF_ALT_CIZGI olmalı (Türkçe karakter yok): $FILM"; exit 2 ;;
esac

CIZELGE=0; N="$VARSAYILAN"; KLIP=10
if [ "$ARG3" = "--cizelge" ]; then CIZELGE=1
elif [ -n "$ARG3" ]; then
  case "$ARG3" in ''|*[!0-9]*) echo "⛔ sahne sayısı sayı olmalı: $ARG3"; exit 2 ;; esac
  N="$ARG3"
fi
if [ -n "$ARG4" ]; then
  case "$ARG4" in ''|*[!0-9]*) echo "⛔ klip süresi tam saniye olmalı: $ARG4"; exit 2 ;; esac
  KLIP="$ARG4"
fi
HEDEF="$FMT/$FILM"; SAB="kilavuzlar/FILM_KLASOR_SABLONU"

if [ "$CIZELGE" -eq 1 ]; then
  [ -d "$HEDEF" ] || { echo "⛔ klasör yok: $HEDEF"; exit 2; }
else
  [ -e "$HEDEF" ] && { echo "⛔ ZATEN VAR: $HEDEF — üstüne yazılmaz"; exit 2; }
  if [ "$N" -ne "$VARSAYILAN" ]; then
    echo "⚠️  $FMT modülü $VARSAYILAN sahnedir; $N verildi — BANDIN DIŞI: sahip izni + PLAN'a gerekçe."
  fi
  if [ "$KLIP" -ne 10 ]; then
    echo "⚠️  yatay modülün klip süresi 10,0 sn'dir; $KLIP,0 verildi — BANDIN DIŞI: sahip izni + PLAN'a gerekçe."
  fi
  [ "$N" -ge 2 ] || { echo "⛔ sahne sayısı en az 2 olmalı: $N"; exit 2; }
  [ $((N % 2)) -eq 0 ] || echo "⚠️  sahne sayısı TEK ($N) — bölümler eşit değil: B1 $(( (N+1)/2 )) klip · B2 $(( N/2 )) klip."
fi

HEDEF="$HEDEF" SAB="$SAB" FMT="$FMT" FILM="$FILM" N="$N" KLIP="$KLIP" CIZELGE="$CIZELGE" python3 <<'PY'
import os, re, shutil, datetime, glob, sys
H=os.environ["HEDEF"]; S=os.environ["SAB"]; FMT=os.environ["FMT"]; FILM=os.environ["FILM"]
N=int(os.environ["N"]); KLIP=int(os.environ["KLIP"]); CIZ=os.environ["CIZELGE"]=="1"
K=(N+1)//2; SURE=N*KLIP; TOPLAM=SURE+5; B1=K*KLIP
DK=FMT.split("_")[1]
QA="BÖLÜM (iki yarım master × 12 mercek)" if DK in ("6","8") else "FİLM (tek master × 12 mercek)"
PART=(f"B1 = S0–S{K-1} · {K} klip · 0–{B1} s · kart YOK  ·  B2 = S{K}–S{N-1} + kart · {K} klip · {B1}–{TOPLAM} s — "
      f"QA her yarıya AYRI koşar; mod D merceklerine SPEC + \"THIS FILE IS PART n OF 2 — …\" beyanı; sınır G{K} elle kareyle (§7)"
      if DK in ("6","8") else "— (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)")
KES=" · ".join(f"{i*KLIP},0" for i in range(1,N)) if N<=12 else f"{KLIP},0 · {2*KLIP},0 · … · {(N-1)*KLIP},0  ({N-1} kesme, her {KLIP},0 sn)"
TARIH=datetime.date.today().strftime("%d.%m.%Y")
rep={"<FILM_ADI>":FILM,"<FILM>":FILM,"<FMT>":FMT,"<N1>":str(N+1),"<N_SON>":str(N-1),"<N>":str(N),
     "<K_SON>":str(K-1),"<K>":str(K),"<SURE>":str(SURE),"<TOPLAM>":str(TOPLAM),"<B1_SURE>":str(B1),
     "<QA_BIRIMI>":QA,"<KESMELER>":KES,"<TARIH>":TARIH,"<DK>":DK,"<PART_GRID>":PART,"<KLIP>":str(KLIP),"<KLIP1>":str(KLIP+1),"<OLCU>":str(KLIP//2)}
def fill(t):
    # uzun anahtarlar önce (<N1> ve <N_SON>, <N>'den önce)
    for k in sorted(rep,key=len,reverse=True): t=t.replace(k,rep[k])
    return t

def blok(n):
    t=open(os.path.join(S,"SAHNE_BLOGU.tpl.md"),encoding="utf-8").read()
    t=t.replace("<n1>",str(n+1)).replace("<n>",str(n)).replace("<BAS>",str(n*KLIP)).replace("<SON>",str((n+1)*KLIP))
    return fill(t)

damga={
 "<SAHNE_SATIRLARI>": "\n".join(f"S{n:02d} — ⬜" for n in range(N)),
 "<MERDIVEN_SATIRLARI>": "\n".join(f"| {n} | {KLIP},0 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ANA | ⬜ |" for n in range(N)),
 "<KARE_SATIRLARI>": "\n".join(f"| {g} | ⬜ | ⬜° | ⬜° | ⬜ | ⬜ | ⬜ | " + ("⭐ USTA KARE — tamam, söküm bitti" if g==N else ("⭐ bölüm sınırı — ⬜" if g==K else "⬜")) + " |" for g in range(N+1)),
 "<SIRALAMA_SATIRLARI>": "\n".join(f"| S{n:02d} | {KLIP},0 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ANA | ⬜ | ⬜ |" for n in range(N)),
 "<SPEC_SATIRLARI>": "\n".join(f"| S{n:02d} | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |" for n in range(N)),
 "<TABLO_SATIRLARI>": "\n".join(f"| S{n:02d} | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |" for n in range(N)) + f"\n| G{N} ⭐ | USTA KARE | ⬜ | söküm: hepsi gitti | ⬜ | ⬜ | ⬜ | — | ⬜ | — | ⬜ |",
 "<ZINCIR_SATIRLARI>": "\n".join(f"| {g} | | G{g+1} | | | geçti/düştü | ✓/✗ | ✓/✗ | " + ("⭐ bölüm sınırı karesi" if g==K else "") + " |" for g in range(N-1,-1,-1)),
 "<I2V_SATIRLARI>": "\n".join(f"| {n} | | | G{n} | G{n+1}{' (usta kare)' if n+1==N else ''} | geçti/düştü | | | 30/0 | {KLIP},0 | | ✓/✗ | ✓✗✗ | |" for n in range(N)),
}
def cizelge():
    rows=[]
    def add(bas, paths, not_=""):
        rows.append(f"\n### {bas}\n\n| okundu | dosya | satır | bu filme düşen kilit (yoksa —) |\n|:--:|---|--:|---|")
        for p in paths:
            try: n=sum(1 for _ in open(p,encoding="utf-8"))
            except Exception: n=0
            rows.append(f"| ⬜ | `{p}` | {n} | |")
    add("A · KILAVUZLAR — hepsi (KILAVUZ_REHBERI §1 sırasıyla)", sorted(glob.glob("kilavuzlar/*.md")))
    ders=0
    try: ders=sum(1 for l in open("kilavuzlar/DERSLER.md",encoding="utf-8") if re.match(r"^## DERS \d+",l))
    except Exception: pass
    rows.append(f"\n⭐ DERSLER.md: **{ders} ölçülmüş ders** — her biri 01_QA_DERS_HASADI §1'de ya kilit ya \"—\" alır.")
    add("B · FORMAT KARTI VE DEPO KONTRATI", ["AGENTS.md", f"{FMT}/README.md", "QA/00_README.md", "QA/00_INDEX.md"])
    add("C · QA RUBRİKLERİ — mercekler ne ölçer", sorted(glob.glob("QA/*_QA.md")))
    add("D · ÖLÇÜLMÜŞ FİLM KAYITLARI (aynı yapı/saha ÖNCE)", sorted(glob.glob("QA/RAPORLAR/*.md")))
    planlar=sorted(glob.glob("dikey_shorts/*/*_DIKEY_TIMELAPSE.md"))+[p for p in sorted(glob.glob("yatay_*_dk_filmler/*/*_PLAN.md")) if not p.startswith(H+"/")]
    add("E · ÖNCEKİ PLANLAR — DEĞİŞMEZLER ve AŞAMA MERDİVENİ nasıl yazılmış", planlar)
    add("F · KANAL — film bittikten sonrası (paketleme yazılırken)", [p for p in ["apexait/KANAL_KIMLIGI.md","apexait/YAYIN_PLANI.md","apexait/CAPRAZ_YAYIN.md","apexait/youtube/PAKETLEME_SABLONU.md","apexait/youtube/POLITIKA_VE_RISK.md"] if os.path.exists(p)])
    top=sum(1 for r in rows if r.startswith("| ⬜"))
    bas=(f"# 📚 {FILM} — OKUMA ÇİZELGESİ (betikten · {TARIH} · {top} dosya)\n\n"
         "> `araclar/film_klasoru_ac.sh` üretti; elle satır eklenmez, yeniden üretmek için `--cizelge`.\n"
         "> Her satır ⬜ → ✅; \"bu filme düşen kilit\" sütunu ya bir cümle ya \"—\" (etiket dışı — meşru).\n"
         "> ⛔ Hepsi \"—\" olan çizelge okunmamış çizelgedir; hepsi kilit olan çizelge sahtedir.\n"
         "> Çekirdek (atlanmaz): KILAVUZ_REHBERI · DERSLER · YAPI_TIPI · SAHA_VE_IKLIM · KAMERA_ISTASYONU ·\n"
         "> PROMPT_SABLONU · INSAAT_YONTEMI · SANTIYE_HAREKETI · ARAC_KARTLARI · KURGU_VE_TESLIM · format README.\n")
    open(os.path.join(H,"00_ANALIZ","00_OKUMA_CIZELGESI.md"),"w",encoding="utf-8").write(bas+"\n".join(rows)+"\n")
    return top

if CIZ:
    print(f"✅ çizelge yenilendi · {cizelge()} dosya → {H}/00_ANALIZ/00_OKUMA_CIZELGESI.md"); sys.exit(0)

os.makedirs(os.path.join(H,"00_ANALIZ","05_SAHNE_CALISMALARI"))
yazilan=[]
for kok,_,dosyalar in os.walk(S):
    for d in dosyalar:
        if d=="00_SABLON_README.md" or d.endswith(".tpl.md"): continue
        src=os.path.join(kok,d); rel=os.path.relpath(src,S)
        hedef_ad=re.sub(r"^FILM_",FILM+"_",os.path.basename(rel))
        dst=os.path.join(H,os.path.dirname(rel),hedef_ad)
        t=open(src,encoding="utf-8").read()
        if "<SAHNE_BLOKLARI>" in t:
            r=range(0,K) if "BOLUM_1" in d else range(K,N)
            t=t.replace("<SAHNE_BLOKLARI>","\n".join(blok(n) for n in r).rstrip("-\n")+"\n")
        for k,v in damga.items(): t=t.replace(k,v)
        t=fill(t)
        os.makedirs(os.path.dirname(dst),exist_ok=True)
        open(dst,"w",encoding="utf-8").write(t); yazilan.append(dst)
top=cizelge()
kalan=[p for p in yazilan if re.search(r"<[A-Z_0-9]+>",open(p,encoding="utf-8").read())]
print(f"✅ {FILM} açıldı → {H}   ({N} sahne × {KLIP},0 sn · {N+1} kare · B1 {K} + B2 {N-K} · {SURE},0 + 5,0 = {TOPLAM},0 sn · QA {QA})")
for p in sorted(yazilan): print("   ",p)
print(f"    {H}/00_ANALIZ/00_OKUMA_CIZELGESI.md  ({top} dosya)")
if kalan: print("⚠️  doldurulmamış yer tutucu kaldı:", ", ".join(os.path.basename(p) for p in kalan))
print("\nSIRA  00_ANALIZ/00_HIKAYE_ONAYI.md (sahip onayı) → 00_OKUMA_CIZELGESI → 01 → 02 → 03 → 04 → 05 → PLAN → BOLUM_2 usta kare → BOLUM_1/2 → KAPAK · MUZIK · YAYIN → QA_SPEC")
print(f"KAPI  python3 araclar/prompt_kontrol.py {H}    (klasör modu — PLAN + BOLUM_1 + BOLUM_2 birleşik)")
PY
