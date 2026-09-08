# 📋 THE LONG DAY — QA KAYDI

```
FİLM        THE LONG DAY — Uzun Gün
FORMAT      9:16 · teslim 11 klip: 10 × 6,0 sn + kapak 5,0 sn = 1:05,0
            ⛔ plan 6·4·6·4·6·6·8·4·6·10 yazmıştı; kurgu 10 × 6,0 DÜZ kesildi
PLAN        dikey_shorts/THE_LONG_DAY/THE_LONG_DAY_DIKEY_TIMELAPSE.md  (v0)
SPEC        THE_LONG_DAY_QA_SPEC.md — üretimden ÖNCE yazıldı
KAPAK       THE_LONG_DAY_KAPAK.md — üretimden ÖNCE yazıldı · ⛔ uygulanmadı
PROMPT KAPISI  ✅ GO — üretimden ÖNCE koşuldu (07.09.2026)
ÜRETİM      ⛔ ÜRETİM GÜNLÜĞÜ YOK: hangi araç, hangi promptlar, zincir koşuldu
            mu, araç kapısı koşuldu mu — hiçbiri kayıtlı değil.
ÖLÇÜM       8/8 mercek koşuldu (Gemini) · ham çıktı QA/HAM_RAPORLAR/THE_LONG_DAY_*
            ⛔ SEKİZİNİN SEKİZİ DE "RUN INCOMPLETE" İLE AÇILDI (§2)
```

⛔ **BU FİLM DEPONUN İLK UZAY SAHASI, İLK SEKİZ MERCEKLİ ÖLÇÜMÜ VE PLAN İLE
FİLMİN EN ÇOK AYRIŞTIĞI VAKASIDIR.** Ekranda planda olmayan şeyler var:
astronotlar (plan S0-S8 insansız), kadrajda güneş diski (plan güneşi kamera
arkasına koydu), dikey merkez habitat + ikiz kule + radar çanağı (plan iki
yatay gömülü modül + iki güç direği + kafes direk), tepesine kadar gündüz
biten gece (plan gece → S0 sabahı). Kapak dev Dünya'lı bilimkurgu afişi
(KAPAK.md tam tersini yazmıştı). **Prompt kapısından GO alan plan
üretilmedi; başka bir şey üretildi.** Sebep kayıtta yok — üretim günlüğü
tutulmadı [DERS 28].

---

## 1. SEKİZ HÜKÜM

| Mercek | Mod | Ham ort. | VERDICT |
|---|:---:|---:|---|
| ① KARE | V ⚠️ karesiz | 6,4 | ✅ **TIME-LAPSE** — CAMERA · FRAME · ANCHOR · STATION 10/10 |
| ② İNŞA | ⛔ V belgesiz | 6,2 | ⛔ **DIFFERENT · APPEARING** (5. kez) |
| ③ ZAMAN | ✅ **V tam** | **7,0** | ⛔ **PASSES BUT NOT IN ONE DIRECTION** · tahmin "several days or one lunar day" |
| ④ TESLİM | ⛔ V belgesiz | 4,8 | ⚠️ ENDS · ⭐ **ONE THING BULUNDU** (ilk kez): "habitat buried in regolith for shielding" |
| ⑤ DEVAMLILIK | V ⚠️ karesiz | 5,8 | ✅ **SAME WORLD** · ⭐ **kanıt BULUNDU**: kaya + taze krater (0:00,0 · 0:59,0) · 5/9 dikiş DEFECT |
| ⑥ GEÇİŞ | ⛔ V belgesiz · sessiz | 7,7 | ✅ TIME · ⛔ **METRONOME** (4. kez) |
| ⑦ İŞ | V ⚠️ karesiz | 4,4 | ⛔ **PARKED** · GROWTH NOBODY MADE: 0:30,0 ikiz kuleler + tümsek |
| ⑧ YÖNTEM | ⛔ V belgesiz | 3,0 | ⛔ **APPEARED** · ilk beliren: graded pad 0:06,0 · en iyi: berm · 1/9 MADE |

```
⭐ GEÇENLER — deponun ilk 10 sahnelik filminde ilk kez:
   ① TIMELAPSE hükmü + dört kilit kategori 10/10 (kamera · kadraj · çapa · istasyon)
   ⑤ SAME WORLD + "aynı yer" nesnesi ADIYLA bulundu — planın kaya + krater
     çifti. ⛔ VE ZİNCİR KOŞULMADAN tuttu: DERS 25 "zincirsiz çapa ölür"
     demişti; burada büyük, taşınamaz ve SAYILI çapa zincirsiz de yaşadı.
   ④ "THE ONE THING" satırı beş filmde ilk kez NONE FOUND değil: bedel
     tasarımı (gömme) mod V'de bile okundu [P1-b doğrulanıyor].
   ③ SEASON CARRIER 10/10 mevsimsiz sahada — DERS 14 seçenek (b) çalıştı.
   ⑥ DIRECTION 10 · ANCHOR SURVIVAL 10 · JUMP LEGIBILITY 8.
⛔ DÜŞENLER: ② ⑦ ⑧ aynı şeyi üç açıdan söylüyor — hiçbir şey İNŞA EDİLMEDİ,
   her şey kesmede BELİRDİ. ③ güneş kadrajda ve ileri-geri sıçrıyor, gölge
   klip içinde donuk. ① SURFACE TRUTH 0 (CGI), PEOPLE 0 (net astronot).
   ⑥ METRONOM. Beş mercek: END CARD DIFFERENT.
```

---

## 2. ⚠️ MOD DENETİMİ — SEKİZ MERCEĞİN SEKİZİ EKSİK GİRDİYLE KOŞTU

```
① KARE        ⛔ kare grabı verilmedi   (kare_al.sh 5. filmde de koşulmadı)
② İNŞA        ⛔ QA_SPEC verilmedi      ← SPEC üretimden ÖNCE hazırdı
③ ZAMAN       ✅ TAM — rubriği yalnız tam kurgu ister; modelin RUN INCOMPLETE
                 satırı yanlıştır, koşu geçerlidir
④ TESLİM      ⛔ plan ve kapak verilmedi
⑤ DEVAMLILIK  ⛔ kare grabı verilmedi
⑥ GEÇİŞ       ⛔ plan verilmedi · ⛔ ses NOT AUDIBLE
⑦ İŞ          ⛔ kare grabı verilmedi
⑧ YÖNTEM      ⛔ QA_SPEC verilmedi
```

⛔ **DERS 17 ÜÇÜNCÜ, DERS 27 İKİNCİ KEZ.** Belge erken yazıldı (17 çözmedi),
"girdi satırı" yordamı yazıldı (27 çözmedi), sekiz mercek yine belgesiz ve
karesiz koştu. Yordam artık ARACA bağlandı: `araclar/qa_paket.sh` [DERS 29].
② ④ ⑥ ⑧ skorları tabloya yazılmadı; ① ⑤ ⑦ "karesiz" olarak açıldı; bulgular
geçerlidir. ③ tam koştu ve tabloya yazıldı.

---

## 3. ⛔ EN AĞIR ÜÇ BULGU

### ⑧ 1/9 — dokuz elemanın sekizi tamam doğdu

```
graded pad NEVER 0:06.0 · central mast NEVER 0:12.0 · twin towers NEVER 0:30.0 ·
dish NEVER 0:42.0 · access road NEVER 0:48.0 · habitat "on a transporter, no
components seen" 0:24.0
⑦ GROWTH TABLE: beş büyüme olayının beşi "work visible at that spot: NO"
⑦ IDLE: klip 1 %100 · klip 4 %100 (astronotlar bakınıyor)
```
Plan on I2V'nin onuna TEK iş adımını ilk yarıya yazmıştı. Ekranda hiçbiri
yok. Bu, promptun düşmesi değil — **promptun kullanılmaması ya da aracın
I2V'yi görmezden gelmesi**; günlük olmadığı için ayrılamıyor [DERS 28].

### ③ güneş kadrajda, gölge donuk

```
C1 · C2 · C4  gölge klip boyunca 0° (üçüncü film: NARROW LOT 0°, LONG DAY 0°)
C6 · C7 · C9  güneş diski KADRAJDA, gölge yönü 120° zıplıyor; C8 geri dönüyor
C10           yıldızlar donuk (plan: gece bölümünde ~40° birlikte kayma)
```
On I2V'nin onunda başlangıç VE bitiş azimutu dereceyle yazılıydı [DERS 18].
Yine donuk. Prompt cümlesi üçüncü kez tutmadı → araç kapısının sorusu olur
[DERS 32].

### ① PEOPLE 0 · SURFACE TRUTH 0 — insan yazılmadı, insan çıktı; belgesel istendi, CGI çıktı

```
0:00 · 0:06 · 0:12 · 0:24  net odaklı rover/kamyon/ASTRONOT, motion blur yok
0:00  "entire site is a CGI rendering, miniature appearance, clean uniform textures"
0:00  iniş aracında siyah yıldız piktogramı + logo şeritleri (metin yasağı düştü)
```
Plan S0-S8'i insansız yazmış, promptlara "Any suited figure appears only as
soft motion streaks" koşullu cümlesini koymuştu (kapı 'motion streaks'
istiyordu). Model koşulu değil özneyi okudu: figür üretti [DERS 33 — P1-e
ölçüldü]. Ay için fotoğrafik korpus yok; "photorealistic documentary" tutmadı
[DERS 34].

---

## 4. DOKÜMAN SORULARI — ① ③ ⑤ ⑦'nin sorularına plandan cevap

```
① 3D render mi amaçlandı?           HAYIR — plan "photorealistic documentary", negatif "no CGI"
① iş alt %25'e mi düşecekti?        HAYIR — ova %45'te; kamera 3,0 m'ye bu yüzden kondu
① yıldız piktogramı?                HAYIR — "no agency logos, no flags, no mission patches"
① araç/astronot net mi?             HAYIR — S0-S8 insansız; araçlar "smeared trails"
③ süre?                             19 Ay günü; ③ "one lunar day" okudu → P1-c mertebe bile tutmadı
③ güneş sıçrayacak mıydı?           HAYIR — güneş HİÇBİR karede kadrajda değil (bearing 350°)
③ yıldız kayması?                   EVET, ~40° birlikte kayma (S9 I2V) — üretilmedi
⑤ merkez kule geçici miydi?         PLANDA MERKEZ KULE YOK — o eleman planın değil
⑤ araçlar taşınacak mıydı?          söküm satırı S9'dan önce; ama S9'dan önce değil, kesme İÇİNDE kayboldular
⑤ habitat–gömme arası eksik mi?     plan S4 → S5 → S6 üç adım; ekranda tek kesme
⑦ ikiz kule / çanak klibi?          PLANDA İKİZ KULE YOK; çanak S7'de kafes direkle teleskoplanır
⑦ klip 4 gözlem miydi?              HAYIR — S3 yığın sahnesi, iş adımı 1,5 sn'de
```

---

## 5. KARAR

```
YAYINLANMAZ. Yeniden ÜRETİLMEZ (depo felsefesi: eski film düzeltilmez).
Bu film beş ders taşıdı; hepsi YENİ film içindir:
   DERS 28  üretim günlüğü olmadan QA arızayı adlandıramaz → qa_paket kapısı
   DERS 29  koşu yordamı araca bağlandı (qa_paket.sh)
   DERS 30  kapak filmin dünyasından ayrı üretildi → kapak kanıtı (SSIM)
   DERS 31  varyanslı ızgara planda kaldı, kurgu düz kesti → kesme_kontrol.sh
   DERS 32  gölge süpürmesi üçüncü kez üretilmedi → araç kapısının 3. sorusu
   DERS 33  yok yazılan özne var oldu (koşullu cümle) → özne hiç anılmaz
   DERS 34  fotoğrafik korpusu olmayan saha CGI'ye düşer → korpus cümlesi
Kabul edilen kusur: yok — film teslim edilmemiştir (kapak kanıtı yok,
final kare kanıtı koşulmadı, loop üretilmedi).
```
