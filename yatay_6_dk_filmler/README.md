# 🏗️ Yatay 6 Dakika Timelapse — 36 Sahne · 2 Bölüm · 37 Kare

> **Açılış:** 14.09.2026 · sahip kararı. Yatay (16:9) timelapse merdiveninin ÜÇÜNCÜ basamağı:
> yatay_4_dk_filmler/ 24 → **bu klasör 36 sahne · 6:00** → yatay_8_dk_filmler/ 48.
> Klasör iskeleti kardeş depo `film_md`'nin film klasörü şablonundan devralındı
> (PLAN · BOLUM_1 · BOLUM_2 · KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC · URETIM_GUNLUGU + `00_ANALIZ/`);
> **içerik bu deponun kılavuzları ve dersleridir** — `film_md`'nin D-numaralı dersleri, tema/novum/kurulum
> kapıları burada GEÇMEZ (`KILAVUZ_REHBERI` §1.2: kamera sabit, kesme = zaman, novum = zaman sıkışması).
>
> Geçerli kart: `kilavuzlar/KILAVUZ_REHBERI.md` **§2.8** · iskelet `kilavuzlar/FILM_KLASOR_SABLONU/` ·
> akış `AGENTS.md` kart A + kart Y (yatay ek) · zincir §2.7 (N sahne = N+1 kare · T2V yok).

---

## 📐 FORMAT KURALLARI

| Özellik | Değer |
|---|---|
| **Süre** | 6:00 sahne bloğu (36 × 10,0 s = 360,0 s) + kapak kartı 5,0 s = **365,0 s** — kart teslimin SON 5 saniyesi [DERS 4] |
| **Oryantasyon** | 16:9 yatay · 1920×1080 · 30 fps · tek master (dikey master AYRICA üretilmez — kadraj hesabı farklı) |
| **Toplam sahne** | 36 — kapak kartı SAHNE DEĞİL · S0 = kanca, İLERİ yönlü [DERS 3] · S35 = teslim, usta kare G36'ya biter |
| **Kare / prompt** | ⭐ **37 görsel** (G0…G36; G36 = USTA KARE, ayrı `## USTA KARE` bölümü) + **36 I2V** · ⛔ T2V YOK · toplam 73 prompt [§2.7] |
| **Yapı** | 2 bölüm × 18 sahne — `BOLUM_1` = S0–S17 (G0…G17 + 18 I2V) · `BOLUM_2` = S18–S35 + USTA KARE (G18…G36 + 18 I2V). ⭐ Bölüm sınırı bir **KAREDİR (G18)**, kesme değil: bölüm 1'in son I2V'si G18'e biter, G18 bölüm 2'nin ilk görselidir; ışık ve yapı orada atlamaz |
| **Klip süresi** | 10,0 s teslim → üretim 11,0 s, baştan kırp [A7-b] · ⛔ ARAÇ KUTU SETİ ölçülmeden ızgara kesinleşmez [DERS 23 · 31]: {5,10} kutusu gerekir; {4,6,8} çıkarsa her sahne iki zincirli klip (ara kare Gn′, 36 ara kare) — karar sahibe döner, plan tek kareli I2V'ye düşürülmez |
| **Izgara** | ⛔ DÜZ 36 × 10,0 (sahip beyanı 14.09.2026). Karşı kayıt yanında durur: düz ızgara üç filmde METRONOM, varyanslı kurgu üç filmde RHYTHM aldı [DERS 13 · 24 · 44]. Ritim isteniyorsa SÜRE sütunu değişir (120 BPM izinli: 4 · 6 · 8 · 10 · 12), prompt değil; toplam 360,0 sabit |
| **Kamera** | MAIN STATION — tek istasyon, tilt 0, 36 sahne + usta kare. Yatay formül: **yüzde(y) = 50 + 118,5·(y − h)/D** (alt kenardan) · taç %82 için **D = (H − h)/0,27** (dikeyde 0,48 — 1,8 kat uzak) · x(m) → **%50 + 66,7·x/D** (soldan). Detay istasyonu ≤ 2 klip, üç koşul [KAMERA_ISTASYONU §1] |
| **Işık günü** | ⛔ Kesmede ışık atlamaz [§2.7 ①] → Σ rejim penceresi (A 10 dk · B 2 h) ≤ **14 saat**, tek gün 06:00 → 20:00; gece yalnız sahibin kararıyla [ZAMAN_VE_ISIK §5]. 36 sahnede: rejim A: 36 × A = 6 h; en çok 3 × B (doruk · kış ① · kış ②) → 11,5 h. Takvim (haftalar/aylar) SAHADAN okunur, ışıktan değil [P1-c] |
| **Aşama merdiveni** | 36 satır — inşa sırası uydurulmaz (`YAPI_TIPI_KARTLARI`); sahne arttıkça aşama İNCELİR (ara hâl %25 / %50 / %75 satır olur — `INSAAT_YONTEMI` §2), yapı büyümez · kış İKİ sahne [DERS 7] · üç zorunlu satır KANIT · LOOP · SÖKÜM |
| **QA birimi** | ⭐ BÖLÜM — iki yarım master (B1 = S0–S17 · 0–180 s · B2 = S18–S35 + kart · 180–365 s), beş mercek (❶–❺) her yarıya AYRI → 24 rapor (aşağıda) |
| **Müzik** | 120 BPM · ölçü 2,0 s · 5 ölçü/sahne · kesmeler 10,0 · 20,0 · … · 350,0 · müziksiz pencere S0'da · süre 365,0 s [MUZIK_VE_KAPAK §1] |

```bash
bash araclar/film_klasoru_ac.sh yatay_6_dk_filmler <FILM_ADI>            # iskelet + damga (sahne sayısı 36 formattan gelir)
python3 araclar/prompt_kontrol.py yatay_6_dk_filmler/<FILM_ADI>          # ⭐ KLASÖR MODU — PLAN + BOLUM_1 + BOLUM_2 birleşik
bash araclar/kesme_kontrol.sh <teslim.mp4> yatay_6_dk_filmler/<FILM_ADI>/<FILM_ADI>_PLAN.md
bash araclar/qa_paket.sh yatay_6_dk_filmler/<FILM_ADI> <teslim.mp4> [kapak.png]
```

⛔ Bu klasörün köküne `.md` bırakma — yalnız bu README durur; `araclar/sayac.sh` kökteki
her klasörü BİR FİLM sayar. 36'nın dışı bandın dışıdır: sahip izni + plana gerekçe.

---

## 📁 KLASÖR — iskelet her basamakta aynı

Klasör ELLE açılmaz, betikle açılır (bölüm sayısı formattan gelir = 2):

```
yatay_6_dk_filmler/<FILM_ADI>/
├── 00_ANALIZ/                     yazımdan ÖNCEKİ iş — altı adım, bitmeden PLAN yazılmaz
│   ├── 00_HIKAYE_ONAYI.md         ⭐ sahip okur: VAAT · DİRENÇ · BEDEL · 36 sahne satırı · ONAY tarihli
│   ├── 00_OKUMA_CIZELGESI.md      betikten: kılavuzlar · DERSLER · QA/ARSIV_12_MERCEK/RAPORLAR · rubrikler
│   ├── 01_QA_DERS_HASADI.md       bu filme düşen DERS kilitleri + QA arızaları
│   ├── 02_KONSEPT_VE_RISK.md      konsept kapısı (VAAT/DİRENÇ/BEDEL) · yapı + saha kartı · kamera hesabı · vinç · ışık günü
│   ├── 03_SAHNE_SIRALAMASI.md     inşa sırası → 36 satır · monoton büyüme · rejim toplamı · bölüm sınırı
│   ├── 04_UYARI_NOTLARI.md        ölçülmüş arızaya bağlı uyarılar + bu deponun tekrar eden arıza tablosu
│   └── 05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md   sahne başına BİR satır (betik damgalar)
├── <FILM>_PLAN.md                 teslim yapısı · konsept · değişmezler (4 kutu) · aşama merdiveni (36 satır) ·
│                                  kare tablosu (G0…G36) · güneş saati · master lock — ⛔ PROMPT YOK
├── <FILM>_BOLUM_1.md              ## 🎬 SAHNE 0 … 17  — 📸 GÖRSEL (Gn) + 🎥 I2V (Gn → Gn+1)
├── <FILM>_BOLUM_2.md              ## 🎬 SAHNE 18 … 35 + ## 🌟 USTA KARE — G36
├── <FILM>_KAPAK.md                G36 + başlık bandı satırı · başlık dizgisi (px) · 120 px testi · KAPAK KANITI
├── <FILM>_MUZIK.md                BPM ızgarası · katman = aşama · müziksiz pencere · ses hedefi
├── <FILM>_YAYIN_PAKETI.md         ⭐ TAMAMEN İNGİLİZCE · 3 başlık · açıklama · hashtag · sabit yorum · AI beyanı
├── <FILM>_QA_SPEC.md              künye (sahne saatleri · PART GRID) · FİNAL KARE KANITI · kadraj kilitleri · yapı bible sayıları ·
│                                  aynı yer nesnesi · ⑧ defteri · kesme listesi · açık kapılar — ad DEĞİŞMEZ (betikler arar)
└── <FILM>_URETIM_GUNLUGU.md       ⛔ ÜRETİM doldurur: araç kapısı · usta kare · geriye zincir G35→G0 · I2V · yedi ölçüm
                                   günlüksüz filme qa_paket.sh açılmaz [DERS 28 — dört filmde dört kez ölçüldü]
```

⭐ Üretim sırası burada da TERSTİR ve zincirlidir [KILAVUZ_REHBERI §8]: G36 usta kare önce,
image-to-image geriye G35 → … → G0, her karede `araclar/zincir_kontrol.sh` + kanıt nesnesi ELLE
[DERS 25]; sonra 36 I2V, her biri iki onaylı kareye kilitli. Bölüm dosyası ÜRETİM SIRASI değildir,
YAZIM birimidir.

---

## ⛔ DİKEYDEN NE DEĞİŞTİ — dört fark, gerisi aynı

```
① KADRAJIN BOŞ YERİ YANLARDIR, üst değil. Dikeyde yapı kadrajın boş üstüne büyüyordu; yatayda
   taç %82 kuralı korunur ama kamera 1,8 kat uzağa gider (D = (H − h)/0,27) ve iki yan SAHAYA
   kalır: arka plan çapalarından en az biri yapının SOLUNDA, en az biri SAĞINDA durur ve her
   karede adıyla yazılır. Yapı gölgesi yana düşer — gölge süpürmesi yatayda daha uzun okunur.
② GÜVENLİ ALAN 16:9 (1920×1080): ⬜ ÖLÇÜLMEDİ — varsayılan: üst 60 px ve alt 100 px oynatıcı
   bantları (başlık · ilerleme çubuğu), sağ üst 300×100 px bilgi kartı; SON EKRAN öğeleri son
   5–20 s'de kadrajı kaplar → kapak kartı 5,0 s o bandın içindedir, kanıt nesnesi kartta değil
   S35'in tutuşundadır. Sayılar ilk yatay filmin ① koşusunda ölçülür ve §2.8'e yazılır.
③ BÖLÜM SINIRI BİR KAREDİR (G18). Dikeyde tek dosya vardı; burada iki bölüm dosyası var ve
   prompt kapısı KLASÖR MODUNDA koşulur (iki dosya birleşik) — tek bölüm dosyasına koşulan kapı
   "usta kare yok / Scene N of X tutmuyor" der ve bu bir arıza değil, eksik koşudur.
④ IŞIK GÜNÜ TOPLANIR. 36 klip × rejim B = 72 saat olurdu; kesmede ışık atlamadığı için Σ pencere
   ≤ 14 saat: rejim sütunu plana yazılır ve TOPLANIR (03_SAHNE_SIRALAMASI §4). Aşırı toplam BLOCK
   değil PLAN hatasıdır — ⑦ ve ③ mercekleri ölçer.
```

---

## ⭐ TEK FARK — QA BİRİMİ BÖLÜMDÜR (2 ve 4 dk'da FİLM)

> Film TEK master olarak kurgulanır ve yayınlanır; QA için **iki yarım master** ihraç edilir ve
> **beş mercek (❶–❺) her yarıya AYRI koşulur** → 10 ham rapor. Yarım master 4 dk hattının bir filmi
> ölçeğindedir (mercekler 60–240 s teslimde kalibre). Kurgu kapısı ve FİNAL KARE KANITI TAM
> master'a koşulur; yarım master QA aracıdır, teslim değil.

```
KOŞU
  B1 masterı  S0–S17  · 0–180 s · kart YOK       → ❶–❺ beş mercek, her biri ayrı geçici sohbette
  B2 masterı  S18–S35 · 180–365 s · kart VAR     → ❶–❺ beş mercek, her biri ayrı geçici sohbette
  Belgeli merceklere (❹ ❺) SPEC + TEK SATIR BEYAN verilir; kör mercekler (❶ ❷ ❸)
  yalnız yarım masterı ve kendi kare grablarını alır:
     "THIS FILE IS PART 1 OF 2 — scenes S0–S17 — the film's ending and the end card are NOT in this file."
     "THIS FILE IS PART 2 OF 2 — scenes S18–S35 + end card — the film's opening is NOT in this file."
  ⛔ Beyansız koşuda rubrik yarım makarayı EKSİK TESLİM sanır (④ FİNAL VURUŞ FAIL · ① kart sahne sayılır [DERS 4]).

SAYI TAŞIMAYAN KATEGORİLER — hücre "—" kalır, ortalamaya girmez
  ⚠️ 07.10.2026: aşağıdaki adlar 12 mercekli ARŞİV kategorileridir; ilk 6/8 dk filmde beş mercekli
     karşılıklarına (QA/Q1–Q5) çevrilir — mantık aynı: yarım dosyada olmayanı puanlama.
  B1'de (son dosyada yok):   ④ FİNAL VURUŞ · ④ BEDEL ÖDENDİ Mİ · ⑤ LOOP (G0↔G36) · ⑧ SÖKÜM
  B2'de (baş dosyada yok):   ④ KANCA · ③ AÇILIŞ SAATİ · ⑤ LOOP · ⑧ İLK ELEMAN KAYNAĞI
  Hiçbirinde (bütün filmi ister): ③ TOPLAM ZAMAN TAHMİNİ (iki yarının tahmini TOPLANIR, tek satır) ·
     ⑥ KURGU YAYI (doruk süresi en büyük mü — tam master'a elle) · ⑫ yapı boyu G0→G36
  ⬜ AÇIK (sahip kararı): bu dörtlü için (a) tam master'a yalnız ③ ④ ⑥ ÜÇÜNCÜ koşu · (b) elle kare
     denetimi · (c) hücre "—" kalır. Karar gelene kadar (c).

BÖLÜM SINIRI KÖR NOKTASI
  ⑤ DEVAMLILIK S17↔S18 dikişini hiçbir yarım masterda yan yana GÖREMEZ. Dikiş zincirli formatta
  bir KAREDİR (G18): B1'in son karesi ile B2'nin ilk karesi ELLE yan yana konur
  (ffmpeg -sseof -0.05 b1.mp4 · ffmpeg -ss 0.05 b2.mp4) → çapalar · yapı yüzdesi · gölge açısı · gök
  aynı mı; `araclar/zincir_kontrol.sh b1_son.jpg b2_ilk.jpg` çıkış 2 = dikiş kırık, kurgu teslim edilmez.
  SPEC §7'ye BÖLÜM SINIRI satırı yazılır.

KAYIT — üç yerde de bölüm etiketi taşınır
  ham:     QA/HAM/<FILM>/<FILM>_B1_Q<n>_<AD>_HAM.md  ·  <FILM>_B2_Q<n>_<AD>_HAM.md  (qa_paket.sh --bolum 1|2)
  kayıt:   QA/FILMLER/<FILM>.md — TEK dosya, "## BÖLÜM 1" / "## BÖLÜM 2" + "## BÜTÜN FİLM" başlıkları
  tablo:   QA/TABLO.md iki satır  **<FILM>** B1  ·  **<FILM>** B2  (TOPLAM FİLM'de BİR film)
  ⛔ Kesme listesi / REMOVE reçetesi bölüm raporundan UYGULANMAZ — kesme filmin kurgusudur.
  ⛔ Kurgu kapısı (KURGU_VE_TESLIM §6 yedi ölçüm) TAM master'a: klip 36 · süre 365,0 ±0,25 s ·
     kesme_kontrol.sh PLAN'ın SÜRE sütunuyla (35 kesme, top-N).
```

---

## 📏 MERDİVEN — komşu basamaklar

| Özellik | 12 · 2 dk | 24 · 4 dk | 36 · 6 dk | 48 · 8 dk |
|---|---|---|---|---|
| Klasör | `yatay_2_dk_filmler/` | `yatay_4_dk_filmler/` | `yatay_6_dk_filmler/` | `yatay_8_dk_filmler/` |
| Kare / I2V | 13 / 12 | 25 / 24 | 37 / 36 | 49 / 48 |
| Bölüm | 2 × 6 · sınır G6 | 2 × 12 · sınır G12 | 2 × 18 · sınır G18 | 2 × 24 · sınır G24 |
| Teslim | 125,0 s | 245,0 s | 365,0 s | 485,0 s |
| Işık günü | B ağırlıklı | A ağırlıklı | A + ≤3 B | A + ≤3 B |
| QA birimi | FİLM | FİLM | BÖLÜM (2 × 12) | BÖLÜM (2 × 12) |
| Yapı önerisi | türbin · villa · yol (6–12 ay) | kule · konut · stadyum | köprü · baraj · liman (≥ 2 yıl) | köprü · baraj · liman |

⚠️ Dikey hat (`dikey_shorts/`, 9:16 · 60 s bandı) ayrı kalır: oradaki film buraya taşınmaz, buradaki
film oraya kırpılmaz — kadraj hesabı, güvenli alan ve ızgara farklıdır (`CAPRAZ_YAYIN` tek master kuralı).

---

## 🎞️ FİLMLER

Film listesi burada tutulmaz — `QA/TABLO.md` tek sayaçtır (`bash araclar/sayac.sh`); 12 mercekli eski ölçümler `QA/ARSIV_12_MERCEK/00_ARSIV.md`.
Bu klasörde henüz film yok; ilk film kart A ile (`00_ANALIZ/00_HIKAYE_ONAYI.md` onaylanmadan
dosya yazılmaz) açılır.
