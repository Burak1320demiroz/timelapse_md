# 🏜️ THE_BURIED_KHAN — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **15 × 8,0 sn = 120,0 sn** | Kapak kartı: **⛔ YOK** | Toplam: **120,0 sn**
Prompt yapısı: ⭐ **15 sahne → 16 görsel (G0…G15) + 15 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G8** · tek istasyon
Yapı: **kumun altından çıkarılıp onarılan iki katlı taş kervansaray (60 m cephe) — 16 kemerli galeri, 15 m kapı çerçevesi, iki kubbe başlıklı köşe kulesi** (kart yok: `YAPI_TIPI_KARTLARI` §10 şablonuyla 00_ANALIZ/02 §2'de yazıldı; en yakın emsal THE BLUE DOOR taş cephe onarımı · THE STONE DRAGON eksiltme) · Saha: **sıcak çöl, 30° K, düz kum ve çakıl** (`SAHA_VE_IKLIM_KARTLARI` §3.6 ÇÖL / KURAK)
Zaman yayı: **gerçekte ≈11 ay (kış → ertesi sonbahar) → 120 saniye** · film mertebe anlatır: *"bir kış kum, bir bahar taş, bir yaz rüzgâr, bir sonbahar ışık"* [P1-c] · ÜSLUP BEYANI: takvim tek bir günün ışığına sıkıştırıldı (THE OLD ROAD · THE HIDDEN FALLS emsali)
Işık günü: **06:00 → 19:20 (mavi saat) · Σ rejim penceresi 13 sa 20 dk ≤ 14** — kesmede ışık atlamaz [§2.7 ①]
Kamera mimarisi: **MAIN STATION** — tek istasyon, 15 sahne + usta kare · detay istasyonu YOK
Izgara: ⛔ **DÜZ — 15 × 8,0** · ⚠️ BANDIN DIŞI (format 12 × 10,0) — sahip izinli varyant (yatay_2 README, 16.09.2026) · format sorusu cevapsız → varsayım (hikâye SAPMA ⑬) · §DÜZ IZGARA BEYANI
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 09.10.2026 (TUR 1 · SAPMA ①–⑭)
Havuz kaydı: `apexait/YAYIN_PLANI.md` — ⬜ satır açılmadı (16:9 hattı dikey ızgaraya sayılmaz; sahip kararı bekliyor) · siluet ailesi: **uzun alçak taş cephe / kumdan çıkan yapı** (THE BLUE DOOR · THE STONE DRAGON ile akraba; THE HIDDEN FALLS'tan farklı — su ve cam YOK)

_"İlk karede çölde dev bir kum tepesi ve sırtından çıkan üç taş uç; son karede aynı yerde onarılmış uzun bir taş kervansaray, kemerlerinde yanan fenerler ve açık kapısından taşan sıcak ışık."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     15 sahne × 8,0 sn                       = 120,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     ⛔ YOK — format sorusu cevapsız, varsayım: tam 120,0 sn (THE HIDDEN FALLS emsali); film adı yalnız
               küçük resme eklenir · teslim son ana görüntüyle biter; ihrac_kontrol.sh --kart YOK
──────────────────────────────────────────────────────────────
TOPLAM                                                     120,0 sn
HIZ             1x (yatay hat 2x'e çevrilmez — 2x yalnız dikey paylaşım kuralıdır [DERS 58])
MÜZİK           ⛔ YOK (varsayım — sahip sorusu cevapsız; hikâye SAPMA ⑫) · SES TABLOSU THE_BURIED_KHAN_MUZIK.md (kum →
               taş → rüzgâr → ışık) · ⬜ sahip müzik isterse eklenir (yatay hatta müzik serbest, sahip 05.10.2026)
YASAK KELİME    ruins · ruin · ruined · temple · pyramid · mosque · minaret · palace · tomb · castle · fortress · fort · oasis · camel · camels · sahara · petra · egypt · hotel · archaeological · archaeologist · excavation · khan
               ⭐ [DERS 59 · 55 · 42] hiçbir promptta, negatifte bile — "ruins" harabe ALANI (çoğul yıkıntı, sütun
                  ormanı) çağırır; "temple · pyramid · mosque · minaret · palace · tomb · castle · fortress · fort"
                  yanlış yapı tipi (kule başlıkları minare/burç olur); "oasis" palmiye + havuz; "camel" hayvan
                  anatomisi (kervan YOK); "sahara · petra · egypt" GERÇEK YER; "archaeological · excavation" kazı
                  ızgarası ve ip ağı (bu iş arkeoloji değil, toprak işi + onarım); "khan" kişi adı → yapı yalnız
                  "caravanserai" yazılır. Kazı fiili "dig" ve "cut down" yazılır.
KELİME KİLİDİ   "dune" yalnız G0–G2 + S0–S2 I2V (G3'ten sonra kum "sand", "ramp of sand", "berm") · "excavator" yalnız
               G0–G4 + S0–S4 I2V · "crane" yalnız G6–G8 + S5–S8 I2V [P7-e] · "lit"/"glow" yalnız S13 I2V ve G14'ten
               sonra · "open inward" yalnız S14 I2V ve G15 · STRUCTURE'da kum, kumul, fener ve ışık YOK (yalnız yapı) [DERS 36]
BÖLÜM DOSYASI   BOLUM_1 = S0–S7 (0–64,0)  ·  BOLUM_2 = S8–S14 + USTA KARE (64,0–120,0) · betiğin ceil(15/2)=8 bölmesi
QA BİRİMİ       FİLM (tek master × 5 mercek · ❶ ❷ ❸ kör · ❹ ❺ belgeli) — QA/HAM/THE_BURIED_KHAN/
```

⛔ Kart olmadığı için platform son ekranı **son 5 saniyeye konmaz** ya da yalnız gök bandına (üstten 0–300 px) konur — kapı, fenerler ve eşikteki üç kişinin üstüne yerleştirilmez.
⚠️ Son sahnenin (S14) son 4,0 sn'lik TUTUŞU final kanıtıdır (`QA_SPEC` §1): kapılar açık, üç kişi eşikte durur, fenerler yanık, başka hiçbir şey değişmez.
⭐ Platform küçük resmi (kapak) G15'ten gelir (sahip kararı 19.09.2026 — öncesi/sonrası bölme yok).

### ⭐ İZLEYİCİ KAPISI [C2-a…d · KILAVUZ_REHBERI §6]

```
İŞLEV ANI         S13 fenerler kemer kemer YANAR → S14 kapılar gerçek hızda içe AÇILIR, avlunun ışığı ön avluya taşar,
                  yük arabalı üç kişi eşiğe gelir. Olay S14'ün ilk yarısında (0–4 sn), ikinci yarı TUTUŞ (4–8 sn).
AÇILIŞ NESNESİ    G0: dev kum tepesi (kadrajın x 270–1650'si, %60'a kadar) ve sırtından çıkan ÜÇ TAŞ UÇ — ortada kapı
                  çerçevesinin düz tepesi, iki yanda kule kubbeleri · ona ne oluyor: gömülü (tuhaflık) ve ilk kova
                  kumu ilk karede kalkıyor. 120 px'te okunan: altın kum tepesi + üç koyu taş ucu.
DİRENÇ EKRANDA    ① kum — S0–S4 ekskavatör, sağa akan kamyon sırası, sete kum döken konveyör · ② rüzgâr — S0–S2 sırttan
                  tüten kum, S3 açılan kapıya geri kayan kum, S9 setin üstünden savrulan ve çitlerde biriken kum ·
                  ③ yıkık bölüm — S3 gedik ve yığın, S5–S7 iskele, yeni taş, ahşap kalıp
DÖNGÜ KAFİYESİ    G15 ↔ G0 aynı kadraj, aynı akasya (x 154–259), aynı masa dağı: G0'da kapı çerçevesinin düz tepesi kum
                  sırtından 57 px çıkar (368–425), G15'te AYNI çerçeve tam boy (368 → 655) ve açık kapısından ışık
                  taşar; G0'da kule kubbeleri kumdan çıkan iki uç, G15'te iki kulenin tepesi. Işık FARKLI, bilinçli:
                  sabah 06:00 ↔ mavi saat. İşlev anı (kapı) kadrajın ORTASINDA kalır [BACK TO WATER döngü 3 dersi].
MERAK SORUSU      Kumun altında ne var?
AÇILIŞ DÜZENİ     ① NESNE kum tepesi + üç taş uç · ② DOKUNUŞ "From the first frame the excavator bucket is already
                  biting into the crest" · ③ İPUCU sol önde açık renkli yeni taş yüklü kamyon — amacı okunmaz ·
                  ④ ÖLÇEK ikinci ekskavatör sağdan girer, damperli yüklü gider · AÇILIŞ GERİ ÇEKİLMESİ ⛔ YOK (sabit geniş)
```

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Çölün yuttuğu bir kervansarayı kumdan çıkarıp onarmak ve kapılarını yeniden açmak.
DİRENÇ   ① kum (12 m'lik tepe; her kova bir yere gider — kamyon ya da konveyör)  ② rüzgâr (kum geri gelir; set ve
         hurma dalı çit)  ③ yıkık bölüm (10 m gedik, dört kemer; düşen taşlar kumun içinde)
         EKRANDA NASIL [P1-b]:  S0–S2 · sırttan tüten kum  ·  S1–S4 · sağa akan kamyonlar + sete kum döken konveyör  ·
                                S3 · kapıya geri kayan kum  ·  S5–S7 · iskele, yeni taş, ahşap kalıp  ·  S9 · çitlerde
                                biriken kum, süpürülen ön avlu
BEDEL    ⭐ Kum tepesinin kendisi — G0'da x 270–1650 · sırt %60,6 (üstten 425); S0–S4'te kova kova gider; G15'te aynı yerde
         açık kapılı, ışıklı kervansaray. Kum yok olmaz: sağda alçak sete (x 1530 → sağ kenar, tepe 570) dönüşür.
         Okuma bilinçli: "kum temizlendi" değil, "çölün yuttuğu yer geri açıldı".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            kum tepesi                                                         ✅
  □ kadrajda görünüyor mu?    x 270–1650 · sırt 425 → yok; yerine cephe 387–1533 · 483–655           ✅
  □ cevap "zaman geçiyor" mu? hayır — "gömülü yapı açıldı, kapısı çalışıyor"                       ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: kum nerede (sırt · duvar hizası · kat hizası · avlu) · gedik açık mı, iskelede
                           mi, örülü mü · kapı kanatları var mı · fenerler asılı mı, yanık mı
② KİNETİK BAĞIMSIZLIK   ✅ her klipte makine, ekip, kum ya da ışık hareket eder (ekskavatör · konveyör · kamyon · ekip ·
                           vinç · mason · rüzgârla kum · süpürge · fener yakıcı · kapı · üç kişi)
③ BAŞLIK ŞEMASI         ✅ kapak "THE BURIED KHAN" (3 kelime) · yayın başlığı YAYIN_PAKETI (≤40 karakter adayları)
④ OMURGA CÜMLESİ [P1-k] ✅ üç uç kazılır → tepe sıyrılır → galeri açılır → cephe çıkar → avlu temizlenir → iskele kurulur
                           → gedik örülür → kemerler kapanır → kapı asılır → rüzgâr direnir → fenerler asılır → iskele
                           sökülür → güneş batar → fenerler yanar → kapılar açılır
```

⚠️ **THE BLUE DOOR ile aile benzerliği [P16-a]:** ikisinde de taş bir cephe onarılır ve final bir kapıdır. AYIRICI FARK:
BLUE DOOR'da sarmaşık sökülür, dar sokakta tek dükkân; burada 12 m kum KAZILIR, 60 m'lik cephe çölün içinden çıkar ve
kapı İÇERİDEN açılır. THE STONE DRAGON ile eksiltme akrabalığı: orada taş oyulur, burada yapı kumdan çıkarılır.
THE HIDDEN FALLS ile ardışık yayınlanabilir (su ve cam yok, renk ailesi farklı).

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera (tek istasyon)
                          ② kanıt nesnesi: kuru AKASYA (x 154–259 · üstten 495–585 · 105 px · 16 karede birebir)
                          ③ çapa: MASA DAĞI (sağ ufuk x 1660–1840 · 518–540 · siluet hiç değişmez)
                          ④ çapa: ufuk düz %50 (540) · ⑤ çapa: akasyanın kaya yükseltisi
                          ⑥ cephe tek parça: x 387–1533 (kuleler 329–1591) · duvar tepesi 483 · kapı çerçevesi 368 · zemin
                             655 — G3 → G15 ±2 px; yalnız KAZANIR (gedik örülür, kanat, fener)
                          ⑦ kum defteri: sırt 425 (G0–G1) · duvar tepesi 483 (G2) · kemer tabanı 559 (G3) · zemin + rampa
                             (G4) · avlu açık (G5+) — kum ASLA geri tepe olmaz (S9 yalnız ince dil, süpürülür)
                          ⑧ insan: A/B'de iz ("soft motion streaks") · G'de küçük figür, yüz okunmaz
P1.5 · fırsat buldukça   gökyüzü pusu (kış berrak → yaz beyaz → sonbahar berrak) · gölge süpürmesi (B: S1 · S2 · S3 · S6 ·
                          S9 · S12) · yeni taşın matlaşması (G7 parlak → G11+ tozlu) · harç rengi (gri → krem)
SPEC · yalnız belge      azimut/yükseklik dereceleri (kapı şartı) · px tabloları
```

**Malzeme kimliği (her promptta):** *bal rengi kumtaşı · altın kum ve gri çakıl · açık renkli yeni taş · koyu ahşap kapı · demir fener* — korpus: "documentary site photograph on colour negative film" [DERS 34 · 42].
**İnsan kararı:** ekip var — A/B'de iz; S13 fener yakıcı (A, iz) + iki işçi; S14–G15 üç kişi yük arabasıyla (G, ≈30 px, yüz okunmaz). Deve YOK (hayvan anatomisi riski; kelime hiç yazılmaz).
**Vinç kararı [DERS 8 · 22 · 46 · 57]:** küçük mobil vinç yalnız G6–G8 (S5'te sağdan girer, S8'de bomunu katlayıp sağdan çıkar); kanca her karede YÜKLÜ ("with a … on the hook"): G6 kurtarılmış blok · G7 kemer taşı paleti · G8 kapı kanadı. Uzun rijit yük YOK — en uzun parça kapı kanadı (2,5 × 8 m), dik asılı, tek tek.
**Korpus kararı [DERS 55]:** çöl + taş yapı korpusu çoğuldur (harabe alanı, köy, ikinci kervansaray) → NEGATIVE'de her karede: "The desert holds exactly one building site, this one."
**Yapı adı kararı [DERS 42 · P23-b]:** "khan" (kişi adı) → "caravanserai" · "ruins" (harabe alanı) → "the breach", "the fallen blocks" · "minaret/fort" (köşe kulesi) → "a round corner tower with a domed cap" · "excavation/archaeological" (kazı ızgarası) → "dig", "cut down".

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0,
                 yani en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp [A7-b]; kutu tam 8,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 15 sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.

┌─ KAMERA İSTASYONU (ANA · tek) ───────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 (G13–G15 ISO 800) · tam kare YATAY │
│ yükseklik     h = +6,0 m (çöl zemininden) — alçak koyu kaya yükseltisinin tepesi│
│ mesafe        D_cephe = 67,0 m · D_avlu önü = 47,0 m · D_kumul topuğu = 40,0 m · │
│               D_akasya = 85,0 m · D_set = 85,0 m · kadraj altı: zemin 14,2 m'de  │
│               [DERS 38]                                                       │
│ bakış açısı   bearing 20° (KKD) · tilt 0° · roll 0° · cephe 200°'ye bakar      │
│ sabitleme     "fixed tripod bolted to the top of a low dark rock outcrop"     │
│ ⛔ HESAP (KILAVUZ_REHBERI §2.8 · f=24 · yatay · yüzde ALT kenardan):            │
│    yüzde(y) = 50 + 118,5·(y − h)/D       px(x) = 960 + 1280,6·x/D (soldan)     │
│    ⚠️ "taç %82 → D = (H − h)/0,27" UYGULANMAZ: yapı alçak ve uzun (60 × 9 m) — │
│       konu cephenin ENİDİR: 60 m → 1146 px (kadrajın %60'ı) → D 67            │
│    kapı çerçevesi tepesi  y=+15 · D 67 → %65,9 (üstten 368)                    │
│    kumul sırtı (orta)     y=+12 · D 67 → %60,6 (425) · uçlarda +10 → %57,1 (464)│
│    kule kubbesi           y=+13 · D 67 → %62,4 (406)                           │
│    duvar tepesi           y=+9  · D 67 → %55,3 (483)                           │
│    kapı kemeri tepesi     y=+8  · D 67 → %53,5 (502)                           │
│    kemer tabanı (galeri)  y=+5  · D 67 → %48,2 (559)                           │
│    gedik dibi             y=+4  · D 67 → %46,5 (578)                           │
│    cephe dibi (zemin)     y=0   · D 67 → %39,4 (655) ✓ çalışma seviyesi ≥ %25   │
│    avlu ön kenarı         y=0   · D 47 → %34,9 (703)                           │
│    kumul topuğu (G0)      y=0   · D 40 → %32,2 (732)                           │
│    cephe x −30…+30 → 387–1533 · kuleler −33…−27 / +27…+33 → 329–444 / 1476–1591 │
│    kapı çerçevesi x −6…+6 → 845–1075 · kapı açıklığı x −2,5…+2,5 → 912–1008     │
│    gedik x +12…+22 → 1189–1380 · kumul x −36…+36 → 272–1648                     │
│    ⭐ kanıt nesnesi AKASYA x −53,5…−46,5 · D 85 → 154–259 (105 px) · kaya üstü   │
│       +3 → 585 · taç tepesi +9 → 495                                           │
│    çapa MASA DAĞI ≈8 km · ≈150 m → ufkun %2 üstü (518–540) · x 1660–1840        │
│    set x +38…+62 · D 85 → 1533 → sağ kenar · tepe +4 → %47,2 (570) < ufuk ✓    │
│    taş istifi x −20 · D 38 → x ≈286 · 692–742 (akasyanın ALTINDA, çakışmaz) ✓    │
│    mobil vinç x +8 · D 52 → x ≈1157 · bom ucu +14 → 343                        │
│    üç kişi 1,7 m · D 66 → ≈30 px boy · G14 x ≈830 · G15 eşikte x ≈910           │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① ⭐ KURU AKASYA (SOL · x 154–259 · 495–585) — KANIT NESNESİ, kaya yükseltisi  │
│    üstünde, çıplak gri dallar; hiç yaprak açmaz (mevsimle değişmez)            │
│ ② MASA DAĞI (SAĞ UFUK · x 1660–1840 · 518–540) — siluet her karede aynı        │
│    [SAHA §3.6 negatif eki]; yaz pusunda soluklaşır, biçimi değişmez            │
│ ③ UFUK düz %50 (540)                                                          │
│ ④ ön plan kum dalgaları + dağınık koyu taşlar (alt %30) — iz değişebilir,      │
│    zemin değişmez                                                             │
│ ⚠️ KUMUL ÇAPA DEĞİLDİR (SAHA §3.0 · §3.6) — kaybolan şeyin kendisi, BEDEL       │
│ + "The desert holds exactly one building site, this one" korpus kilidi — her NEGATIVE'de │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ tilt 0 → ufuk %50 · kapı çerçevesi %65,9 · cephe dibi %39,4 ≥ %25             │
│ yanlar: solda akasya + kaya yükseltisi + taş istifi · sağda set + çitler +     │
│ konveyör + masa dağı                                                          │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ (§2.8 varsayılanı) — kanıt nesnesi alt 100 px'e  │
│ (üstten > 980) ve sağ üst 300×100 px'e (x > 1620 · üstten < 100) girmez ✓       │
│ ⚠️ masa dağı sağda ama üstten 518–540 → bilgi kartı bandının (<100) ÇOK ALTINDA ✓│
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ kervansaray: 60 m cephe (x −30…+30) · iki kat · alt kat 0 → +5 (penceresiz,     │
│   dar mazgal pencereler) · üst kat galeri +5 → +9 · 16 yuvarlak kemer (kapının   │
│   iki yanında 8'er, her biri ≈2,6 m) · duvar tepesi +9                         │
│ kapı çerçevesi: 12 m en (x −6…+6) · +15 · sivri kemer 5 × 8 m · oyma geometrik  │
│   kuşak kemerin çevresinde · iki kanatlı koyu ahşap kapı (her kanat 2,5 × 8 m)  │
│ köşe kuleleri: Ø 6 m · x ±27…±33 · kubbe başlık +13                            │
│ gedik: x +12…+22 (10 m) · +4'e kadar yıkık · 4 kemer eksik · yıkıntı yığını     │
│   dibinde                                                                     │
│ ön avlu: 60 × 20 m taş döşeme (D 47–67)                                       │
│ kumul: x −36…+36 · sırt +12 (orta) · +10 (uçlar) · cepheyi tümüyle örter ·      │
│   topuk D 40 · G0'da yalnız kapı çerçevesi (+12…+15) ve kule kubbeleri (+10…+13) │
│   dışarıda                                                                    │
│ set: x +38…+62 · D 75–95 · +4 · sırtında hurma dalı çitler (S4)                 │
│ fener: 16 demir fener, her kemerde bir (S10 asılır · S13 yanar)                │
│ STRUCTURE'ın İngilizce tam hâli tek cümle (DERS 36): "When finished this will be│
│   a long two-storey caravanserai of honey-coloured sandstone, 60 metres wide,  │
│   behind a stone-paved forecourt: a blank lower storey, an open arcade of      │
│   sixteen round arches above it, a tall gateway frame around a pointed arch at │
│   its centre with a pair of heavy timber doors, and a round corner tower with a │
│   domed cap at each end." — 16 görselde BİREBİR                                │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 15 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az YAPI göstermez. Bu filmde "büyüme" iki yönlüdür: kum
> AZALIR (S0–S4, bedel), görünen yapı ARTAR (cephe kumdan çıkar, gedik örülür) — kumun azalması yapının kaybı değildir.
> Kış görüntüsü YOK (sıcak çöl, karsız — "kış İKİ sahne" kuralı tetiklenmez).

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | İSTASYON | KANIT NESNESİ (px) |
|:-:|:-:|---|---|:-:|:-:|:-:|:-:|---|
| 0 | 8,0 | KAZAR | kumul sırtı +12 → kapı çerçevesinin çevresi açılır (%10) · taş istifi 0 → 1 | 1 gün | A | 06:00→06:10 | ANA | çerçeve tepesi 368–425 · istif x ≈286 |
| 1 | 8,0 | SIYIRIR | kumul +12 → +9 (cephe önünde) · kapı çerçevesi %40 · kule kubbeleri açık · set %20 | 3 hafta | B | 06:10→08:10 | ANA | kum sırtı 425 → 483 |
| 2 | 8,0 | AÇAR | kum +9 → +5 · üst kat kemer sırası soldan sağa %100 · gedik belirir · set %50 | 3 hafta | B | 08:10→10:10 | ANA | kum 483 → 559 · kemerler 16 − 4 |
| 3 | 8,0 | ORTAYA ÇIKARIR | kum +5 → zemin (cephe önü) · cephe tam boy %100 · gedik + yığın · avlu hâlâ kumda | 4 hafta | B | 10:10→12:10 | ANA | ⭐ cephe 483–655 tam · gedik 1189–1380 |
| 4 | 8,0 | TEMİZLER | avlu döşemesi %0 → %100 · kapı ağzı boşalır · set %100 + çit · ekskavatörler gider | 3 hafta | A | 12:10→12:20 | ANA | avlu 655–703 açık |
| 5 | 8,0 | KALDIRIR | mobil vinç girer · iskele 0 → %100 · yığın → avluda sıralar (%100) | 2 hafta | A | 12:20→12:30 | ANA | yığın → 0 · iskele 1189–1380 |
| 6 | 8,0 | ÖRER | gedik duvarı +4 → kemer üzengisi (%100) · ayaklar · istif azalır | 2 ay | B | 12:30→14:30 | ANA | gedik dibi 578 → 559 |
| 7 | 8,0 | KAPATIR | eksik kemer 0 → 4 (ahşap kalıp) · duvar +9 · kalıp sökülür | 6 hafta | A | 14:30→14:40 | ANA | galeri 16/16 · tepe 483 |
| 8 | 8,0 | ASAR | kapı kanadı 0 → 2 (vinçten) · kapı kapalı · vinç gider | 2 hafta | A | 14:40→14:50 | ANA | kapı 912–1008 kapalı · vinç → 0 |
| 9 | 8,0 | DİRENİR | ikindi rüzgârı: kum setten savrulur → çitte birikir · avlu süpürülür | 1 gün | B | 14:50→16:50 | ANA | çit önünde kum dili · avlu açık |
| 10 | 8,0 | ASAR ② | fener 0 → 16 (sönük) · oyma kuşak fırçalanır | 3 hafta | A | 16:50→17:00 | ANA | 16 kemerde fener |
| 11 | 8,0 | SÖKER | iskele %100 → 0 · konveyör çekilir · son taşlar gider | 1 hafta | A | 17:00→17:10 | ANA | iskele → 0 · istif → 0 |
| 12 | 8,0 | BATAR | altın ışık → gün batımı → mavi saat · eklenen yok · son süpürme | 1 akşam | B | 17:10→19:10 | ANA | gölge +82° → güneş batar |
| 13 | 8,0 | YAKAR | fener 0 → 16 yanık (soldan sağa) | 10 dk | A | 19:10→19:20 | ANA | 16 kemer sönük → yanık |
| 14 | 8,0 | AÇILIR | kapılar içe açılır · ışık taşar · üç kişi eşiğe · TUTUŞ | 8 sn | G | 19:20 (+8 sn) | ANA | ⭐ kapı 912–1008 açık · kişiler x 830 → 910 |

```
IZGARA          8,0 sn × 15 · kesmeler 8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn) · müzik YOK (BPM ızgarası yok)
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: format sorusu cevapsız → THE HIDDEN FALLS'un sahip senaryosundaki 15 × 8,0 (08.10.2026) ve
                       yatay_2 README'deki sahip izinli 15 × 8,0 varyantı (16.09.2026); emsal THE OLD ROAD · THE HIDDEN
                       FALLS. ⚠️ BANDIN DIŞI: format 12 × 10,0.
                   (b) ritim klip İÇİNE: ① rejim nabzı — B'ler S1 · S2 · S3 · S6 · S9 · S12 (kum iner, taş örülür, rüzgâr,
                       gün batımı), G S14 (gerçek hız — kapı ve insan); ② iş yönü değişir: aşağı (S1–S3 kum) · öne (S4
                       avlu) · yukarı (S5 iskele · S6 duvar) · soldan sağa (S2 kemerler · S7 kemerler · S10 fener · S13
                       ışık) · içe (S14 kapı); ③ ses katmanı = aşama (MUZIK.md SES TABLOSU).
                   (c) kabul edilen risk: eşit klipte ❷ RHYTHM kategorisi NOT TRIGGERED (beş mercekli rubrik) — sapma
                       kurgudan gelirse (klip ≠ 8,0) ❷ açılır ve ❺ final saniyesi kayar [IRON BRIDGE · GLASS WALL].
                       Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
REJİM SAYISI    ⚠️ ÜÇ rejim (A · B · G) — SANTIYE_HAREKETI §2 sınırı iki. Gerekçe: B kumun inişini ve gölge süpürmesini
                taşır [A12-j]; G yalnız finaldir (kapının açılışı ve üç kişinin adımı gerçek hızda okunur); geçiş
                KESMEDE (S13 → S14) [P5-c]. Emsal: THE SLOW TAKEOFF · THE HIDDEN FALLS (A+B+G, beyanlı).
IŞIK GÜNÜ       Σ pencere = 8 A × 10 dk + 6 B × 2 sa + 1 G × 8 sn = 80 dk + 12 sa ≈ 13 sa 20 dk ≤ 14 ✓
                06:00 → 19:20 (mavi saat, güneş −6,2°)
BÖLÜM SINIRI    G8 — sahne S7 son karesi = sahne S8 ilk karesi; galeri 16/16 bütün, kapı ağzı boş (eşiğe kadar), kanat
                vinçte + biri avluda, iskele gedikte, gölge +64°, bahar — ikisinde de aynı [DERS 52]
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: kuru AKASYA — G0'da ve usta karede (G15) aynı konum (x 154–259) ve aynı boy (105 px en ·
        taç 495 · kaya üstü 585) [DERS 25]; kaya yükseltisinin üstünde, hiç yaprak açmaz. Yedek: MASA DAĞI x 1660–1840
        (siluet). Kum tepesi kanıt OLAMAZ (değişen şeyin kendisi).
LOOP    G15 ↔ G0: aynı kadraj · aynı akasya · aynı masa dağı · ışık FARKLI (bilinçli — G0 06:00 sabah, G15 mavi saat;
        tek gün): kum sırtından çıkan üç uç / aynı yerde kapı çerçevesi ve iki kule tepesi. Biçim kafiyesi: G0'da kapı
        çerçevesinin düz tepesi (845–1075 · 368–425) → G15'te aynı çerçeve, altında açık kapıdan ışık (912–1008).
SÖKÜM   S0 düz kasalı kamyon (boşaltır, S1'de gider) · S4 iki ekskavatör + damperli kamyonlar (sağdan çıkar) · S5 iskele
        kamyonu (solda gider) · S6–S7 kurtarılmış blok sıraları (biter) · S7 ahşap kalıplar (sökülür) · S8 MOBİL VİNÇ
        (bomunu katlar, sağdan çıkar) · S10 fener sandıkları · S11 iskele + konveyör (traktörle) + son istif · S12 son
        süpürme · S13 son merdiven — ekranda gider; set + çitler KALIR (kalıcı) [DERS 48 · P2-h]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
kum (GİDEN)              → ekskavatör kovası → damperli kamyonlar (sağdan çıkar) · konveyör → sağdaki set     → G0 · G1
yeni taş blok            → düz kasalı kamyon → sol önde ahşap takozlu istif (x ≈286)                        → G0
hurma dalı çit           → setin dibinde demetler                                                       → G4
iskele                   → avlunun solunda iskele borusu yüklü kamyon                                     → G5
kurtarılmış blok         → gediğin dibindeki yığın → vinç → avluda sıralar                                → G3 · G5
kemer taşı               → vinçte kama biçimli taş paleti · ahşap kalıplar iskelede                        → G7
kapı kanatları           → vinçte bir kanat · avluda ahşap takozlar üstünde ikinci kanat                    → G8
fener                    → avluda iki ahşap sandık, küçük el arabasında                                    → G10
GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL (prompta yalnız vekil girer):
   avlunun ve odaların onarımı → S14'te açık kapıdan taşan sıcak ışık · kapı menteşesi → "iron pivots set in the
   threshold stone" · ışık → S13 fener yakıcı
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① açık kapıdan taşan sıcak ışık (912–1008 · 502–655 → avluda yelpaze, ilk okunan, en sıcak) → ② yanık 16 fener (galeri
   x 444–1476 · 483–559) → ③ eşikte üç kişi + yük arabası (x ≈910 · ≈30 px) → ④ bütün cephe ve yeni taşlı onarım
   (1189–1380) → ⑤ akasya + masa dağı (kanıt)
FİNAL KARE KANITI  ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 kanit.jpg   (S14 tutuşu 116,0–120,0 içinde · mavi saat,
                   okunur [DERS 45]) · kart YOK → son kare = G15
```

---

## 🖼️ KARE TABLOSU — 16 görsel [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Gölge yönü kadrajda: 0 = kameradan uzağa · − sola · + sağa (|x| > 90 = kameraya doğru). Güneş DİSKİ anılmaz.
> Sayılar `bolum_uretici.py --tablo` çıktısıdır (30° K · δ +20° · güneş saati · kamera bakışı 20°).

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| G0 | 06:00 | 73° | 9,8° | -127° | berrak soluk mavi, ince yüksek bulut | kış · hava çok berrak, masa dağı keskin | ⭐ AÇILIŞ — kumul + üç taş uç · ekskavatör sırtta |
| G1 | 06:10 | 74° | 11,9° | -126° | aynı | aynı | çerçeve çevresinde çukur · konveyör kuruldu |
| G2 | 08:10 | 87° | 37,5° | -113° | berrak, ince bulut | aynı | kum duvar hizasında (483) |
| G3 | 10:10 | 106° | 63,2° | -94° | açık, küçük yüksek bulut | bahar · ufukta hafif toz pusu | galeri açık · alt kat kumda · gedik görünür |
| G4 | 12:10 | 193° | 79,7° | -7° | aynı | aynı | ⭐ cephe tam boy · rampa · yığın |
| G5 | 12:20 | 205° | 79,0° | +5° | aynı | aynı | avlu açık · set + çit · iskele kamyonu |
| G6 | 12:30 | 216° | 77,9° | +16° | aynı | aynı | iskele · bloklar sırada · vinç (blok yükte) |
| G7 | 14:30 | 262° | 54,7° | +62° | aynı | bahar · yeni taş parlak açık | duvar üzengide · kalıplar · vinç (palet) |
| G8 | 14:40 | 264° | 52,6° | +64° | aynı | aynı | ⭐ BÖLÜM SINIRI — galeri bütün · kapı ağzı boş · vinç (kanat) |
| G9 | 14:50 | 265° | 50,4° | +65° | soluk puslu, beyaza yakın | yaz · masa dağı pusta solgun | kapı asılı · durgun hava |
| G10 | 16:50 | 280° | 24,6° | +80° | aynı | yaz · çitlerde biriken kum | fener sandıkları · merdivenler |
| G11 | 17:00 | 281° | 22,4° | +81° | aynı | yaz · yeni taş tozla matlaşmış | 16 fener sönük · iskele duruyor |
| G12 | 17:10 | 282° | 20,3° | +82° | aynı | aynı | saha temiz · iki işçi süpürür |
| G13 | 19:10 | 296° | −4,2° | — (güneş ufkun altında) | mavi saat, ince yüksek bulut | sonbahar · hava yine berrak | fener yakıcı ilk kemerde |
| G14 | 19:20 | 297° | −6,2° | — (güneş ufkun altında) | derin mavi saat | aynı | 16 fener yanık · kapı kapalı · üç kişi geliyor |
| G15 | 19:20 +8 sn | 297° | −6,2° | — (güneş ufkun altında) | ⭐ derin mavi saat | aynı | ⭐ USTA KARE — kapı açık · ışık taşar · üç kişi eşikte |

```
KUM DEFTERİ (kare kilidi [P10-e])   G0 sırt 425 (yalnız üç uç dışarıda) · G1 aynı + çerçeve çevresinde çukur · G2 kum
   duvar hizasında 483 · G3 kemer tabanında 559 (alt kat kumda) · G4 zemine indi, rampa avluyu örter, kapı ağzı 2/3
   kumlu · G5+ avlu açık, kapı ağzı boş · G9–G15 yalnız duvar diplerinde ince kum dili · set G1 %20 → G2 %50 → G4 %100
   ⛔ kum GERİ TEPE OLMAZ — S9 rüzgârı yalnız çitlerde birikir ve ince dil olarak avluya sızar (süpürülür)
   TANIK İZ [P10-g]: G3–G4 açılan cephede kum çizgisi (taşın üstünde soluk bant) yazılmaz — taş derzlerinde kum yazılır
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G15 usta kare → G14 (kapı kapalı, kişiler 5 m geride) → G13 (fenerler sönük, fener yakıcı) → G12 (iki işçi, altın
   ışık) → G11 (iskele geri, konveyör) → G10 (fener yok, sandıklar) → G9 (çit önünde kum yok) → G8 (kapı kanadı vinçte)
   → G7 (kemerler yok, kalıplar) → G6 (gedik +4) → G5 (vinç yok, bloklar yığında) → G4 (rampa, avlu kumda) → G3 (alt
   kat kumda) → G2 (galeri kumda) → G1 (kum sırtı) → G0 (çukur yok)
   ⚠️ ters inşada kum EKLENİR: G4 → G0 adımlarında model kumu "yapının üstüne örtü" diye değil KUM TEPESİ diye çizmeli —
      her adımda kum sırtının px'i (425 · 483 · 559) elle ölçülür
   sonra I2V S0 (G0→G1) … S14 (G14→G15) — her klip iki uca kilitli, üretim 9,0 sn, baştan 1,0 kırp
```

## 🧪 PİLOT ÜÇLÜ [DERS 62 · KILAVUZ_REHBERI §8 adım 2b]

```
⛔ Üretim başlamadan, aşağıdaki üçü geçmeden kalan klipler üretilmez:
① FİNAL      G15 + G14 + S14 — mavi saat, kapılar gerçek hızda içe açılır, ışık yelpazesi avluya düşer, üç kişi eşikte ve
             4 sn tutuş [C1-b] · kapı kanatları kopyalanmaz, kemer biçimi değişmez
② EN BÜYÜK   G1 + G2 + S1 — kumun inişi: sırt 425 → 483 iki saatte, kum kamyonlarla ve konveyörle GİDER (bir karede
   DEĞİŞİKLİK  silinmez) · çerçeve ve kuleler kumdan "büyümez", kum onlardan çekilir · S1 = 00:08
③ DİRENEN    G9 + G10 + S9 — rüzgâr: kum çitlerde birikir, avluya ince dil sızar ve süpürülür; yapı GERİ GÖMÜLMEZ,
              masa dağı pusta solar ama biçimi değişmez [IRON BRIDGE 00:51 dersi: direnç yapıyı geriletmez]
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     30,0° K · ışık günü tarihi: δ +20° (ışık tek gün; takvim sahadan) · doğuş 05:11 · batış 18:49 (güneş
                saati) · kamera bakışı 20° (KKD) → kadraj −17° … +57° · güneş 73° → 297°: sabah önde sağda (kadrajın sağ
                kenarının 16° dışında — kumulun kameraya bakan yüzü gölgede, sırtı ışıkta), öğle tepede ve arkada, akşam
                solda (cepheyi soldan sıyırır) — HİÇBİR karede kadrajda değil [P8-h] · ⚠️ G0–G1'de güneş kadraj
                kenarına 16° — mercek parlaması riski, "The sun stays outside the frame" her promptta
CEPHE IŞIĞI     cephe 200°'ye bakar → doğrudan güneş azimut 110°–290° arasında: G0–G2 gölgede (kumul), G3 sıyırma (sağdan),
                G4–G6 tepeden, G7–G12 soldan (G10–G12 altın sıyırma), G13+ güneş yok
GÖLGE SÜPÜRMESİ rejim B klipte: S1 (−126° → −113°: 13°) · S2 (−113° → −94°: 19°) · S3 (−94° → −7°: 87°) · S6 (+16° → +62°:
                46°) · S9 (+65° → +80°: 15°) · S12 (+82° → güneş batar) · rejim A klipte fark edilmez → yüzeyle kanıtlanır
MEVSİM YAYI     kış (G0–G2: çok berrak hava, masa dağı keskin) → bahar (G3–G8: ufukta hafif toz pusu, yeni taş parlak) →
                yaz (G9–G12: beyaza yakın puslu gök, masa dağı solgun, yeni taş tozla matlaşır) → sonbahar (G13–G15: hava
                yine berrak) · taşıyıcı: GÖK PUSU + YENİ TAŞIN RENGİ (SAHA §3.0: çölde mevsim neredeyse görünmez;
                yeni taşın matlaşması betonun kürlenmesinin karşılığı) · akasya kuru ve hiç değişmez (çapa)
KIŞ             görüntü YOK (sıcak çöl, karsız) · DERS 7 tetiklenmez
GECE            yok · final MAVİ SAAT, güneş −6,2° (G14–G15) · zifiri değil: cephe, fenerler, kapıdan taşan ışık ve üç kişi
                okunur, ışık kadrajın en parlak kaynağı [DERS 45]
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   h +6,0 · D_cephe 67,0 · bakış 20° · tilt 0 · roll 0 · tek istasyon
YAPI     cephe 387–1533 · kuleler 329–444 / 1476–1591 · duvar tepesi 483 · zemin 655 · çerçeve 845–1075 · 368 ·
         kapı 912–1008 · 502–655 · gedik 1189–1380 · 578
ÇAPALAR  ① AKASYA x 154–259 · 495–585 (kanıt nesnesi 105 px) · ② masa dağı x 1660–1840 · 518–540 · ③ ufuk 540
KUM      sırt 425 (G0–G1) · 483 (G2) · 559 (G3) · zemin + rampa (G4) · avlu açık (G5+) · set 1533 → sağ kenar · 570
IZGARA   15 × 8,0 · kesmeler 8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn) · kart YOK · 120,0 sn
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_BURIED_KHAN   → sonuç QA_SPEC §8'de (09.10.2026)
✅ FIX'ler ve beyanları (hepsi elle okundu):
   · ARAÇ KUTU SETİ ölçülmedi — beyanlı; üretim araç kapısıyla açılır
   · süreler eşit (8,0) — düz ızgara (varsayım, SAPMA ⑬); beş mercekte ❷ RHYTHM eşit klipte tetiklenmez
   · S14 (final): ACTIVITY'de hareket eden tek özne (üç kişi + kapı) — KASITLI: final ödül ve sakin andır, şantiye bitti
     [P4-f · C1-d]; ❸'e PARKED gerekçesi SPEC §5 DECLARED WORLD'de
✅ YASAK KELİME taraması 0 · kelime kilitleri (dune G0–G2 · excavator G0–G4 · crane G6–G8 · lit/glow S13+ · open inward
   S14+) betikle doğrulandı (09.10.2026)
✅ 00_ANALIZ altı dosya · hikâye onayı 09.10.2026 (TUR 1 · SAPMA ①–⑭ sahip okur)
⛔ ARAÇ KAPISI koşulmadı → THE_BURIED_KHAN_URETIM_GUNLUGU.md §0
⛔ PİLOT ÜÇLÜ koşulmadı → S14 · S1 · S9
```
