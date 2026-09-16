# 🏗️ Yatay 4 Dakika Timelapse — 24 Sahne · 2 Bölüm · 25 Kare

> **Açılış:** 14.09.2026 · sahip kararı. Yatay (16:9) timelapse merdiveninin İKİNCİ basamağı:
> yatay_2_dk_filmler/ 12 → **bu klasör 24 sahne · 4:00** → yatay_6_dk_filmler/ 36.
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
| **Süre** | 4:00 sahne bloğu (24 × 10,0 s = 240,0 s) + kapak kartı 5,0 s = **245,0 s** — kart teslimin SON 5 saniyesi [DERS 4] |
| **Oryantasyon** | 16:9 yatay · 1920×1080 · 30 fps · tek master (dikey master AYRICA üretilmez — kadraj hesabı farklı) |
| **Toplam sahne** | 24 — kapak kartı SAHNE DEĞİL · S0 = kanca, İLERİ yönlü [DERS 3] · S23 = teslim, usta kare G24'e biter |
| **Kare / prompt** | ⭐ **25 görsel** (G0…G24; G24 = USTA KARE, ayrı `## USTA KARE` bölümü) + **24 I2V** · ⛔ T2V YOK · toplam 49 prompt [§2.7] |
| **Yapı** | 2 bölüm × 12 sahne — `BOLUM_1` = S0–S11 (G0…G11 + 12 I2V) · `BOLUM_2` = S12–S23 + USTA KARE (G12…G24 + 12 I2V). ⭐ Bölüm sınırı bir **KAREDİR (G12)**, kesme değil: bölüm 1'in son I2V'si G12'ye biter, G12 bölüm 2'nin ilk görselidir; ışık ve yapı orada atlamaz |
| **Klip süresi** | 10,0 s teslim → üretim 11,0 s, baştan kırp [A7-b] · ⛔ ARAÇ KUTU SETİ ölçülmeden ızgara kesinleşmez [DERS 23 · 31]: {5,10} kutusu gerekir; {4,6,8} çıkarsa her sahne iki zincirli klip (ara kare Gn′, 24 ara kare) — karar sahibe döner, plan tek kareli I2V'ye düşürülmez |
| **Izgara** | ⛔ DÜZ 24 × 10,0 (sahip beyanı 14.09.2026). Karşı kayıt yanında durur: düz ızgara üç filmde METRONOM, varyanslı kurgu üç filmde RHYTHM aldı [DERS 13 · 24 · 44]. Ritim isteniyorsa SÜRE sütunu değişir (120 BPM izinli: 4 · 6 · 8 · 10 · 12), prompt değil; toplam 240,0 sabit |
| **Kamera** | MAIN STATION — tek istasyon, tilt 0, 24 sahne + usta kare. Yatay formül: **yüzde(y) = 50 + 118,5·(y − h)/D** (alt kenardan) · taç %82 için **D = (H − h)/0,27** (dikeyde 0,48 — 1,8 kat uzak) · x(m) → **%50 + 66,7·x/D** (soldan). Detay istasyonu ≤ 2 klip, üç koşul [KAMERA_ISTASYONU §1] |
| **Işık günü** | ⛔ Kesmede ışık atlamaz [§2.7 ①] → Σ rejim penceresi (A 10 dk · B 2 h) ≤ **14 saat**, tek gün 06:00 → 20:00; gece yalnız sahibin kararıyla [ZAMAN_VE_ISIK §5]. 24 sahnede: rejim A ağırlıklı: ≤ 5 × B (10 h) + 19 × A (3,2 h) = 13,2 h — B klipleri doruk ve kış sahnelerine. Takvim (haftalar/aylar) SAHADAN okunur, ışıktan değil [P1-c] |
| **Aşama merdiveni** | 24 satır — inşa sırası uydurulmaz (`YAPI_TIPI_KARTLARI`); sahne arttıkça aşama İNCELİR (ara hâl %25 / %50 / %75 satır olur — `INSAAT_YONTEMI` §2), yapı büyümez · kış İKİ sahne [DERS 7] · üç zorunlu satır KANIT · LOOP · SÖKÜM |
| **QA birimi** | FİLM — on iki mercek TEK master'a bir kez · ham `QA/HAM_RAPORLAR/<FILM>/<FILM>_<n>_<MERCEK>_HAM.md` |
| **Müzik** | 120 BPM · ölçü 2,0 s · 5 ölçü/sahne · kesmeler 10,0 · 20,0 · … · 230,0 · müziksiz pencere S0'da · süre 245,0 s [MUZIK_VE_KAPAK §1] |

```bash
bash araclar/film_klasoru_ac.sh yatay_4_dk_filmler <FILM_ADI>            # iskelet + damga (sahne sayısı 24 formattan gelir)
python3 araclar/prompt_kontrol.py yatay_4_dk_filmler/<FILM_ADI>          # ⭐ KLASÖR MODU — PLAN + BOLUM_1 + BOLUM_2 birleşik
bash araclar/kesme_kontrol.sh <teslim.mp4> yatay_4_dk_filmler/<FILM_ADI>/<FILM_ADI>_PLAN.md
bash araclar/qa_paket.sh yatay_4_dk_filmler/<FILM_ADI> <teslim.mp4> [kapak.png]
```

⛔ Bu klasörün köküne `.md` bırakma — yalnız bu README durur; `araclar/sayac.sh` kökteki
her klasörü BİR FİLM sayar. 24'ün dışı bandın dışıdır: sahip izni + plana gerekçe.

---

## 📁 KLASÖR — iskelet her basamakta aynı

Klasör ELLE açılmaz, betikle açılır (bölüm sayısı formattan gelir = 2):

```
yatay_4_dk_filmler/<FILM_ADI>/
├── 00_ANALIZ/                     yazımdan ÖNCEKİ iş — altı adım, bitmeden PLAN yazılmaz
│   ├── 00_HIKAYE_ONAYI.md         ⭐ sahip okur: VAAT · DİRENÇ · BEDEL · 24 sahne satırı · ONAY tarihli
│   ├── 00_OKUMA_CIZELGESI.md      betikten: kılavuzlar · DERSLER · QA/RAPORLAR · rubrikler
│   ├── 01_QA_DERS_HASADI.md       bu filme düşen DERS kilitleri + QA arızaları
│   ├── 02_KONSEPT_VE_RISK.md      konsept kapısı (VAAT/DİRENÇ/BEDEL) · yapı + saha kartı · kamera hesabı · vinç · ışık günü
│   ├── 03_SAHNE_SIRALAMASI.md     inşa sırası → 24 satır · monoton büyüme · rejim toplamı · bölüm sınırı
│   ├── 04_UYARI_NOTLARI.md        ölçülmüş arızaya bağlı uyarılar + bu deponun tekrar eden arıza tablosu
│   └── 05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md   sahne başına BİR satır (betik damgalar)
├── <FILM>_PLAN.md                 teslim yapısı · konsept · değişmezler (4 kutu) · aşama merdiveni (24 satır) ·
│                                  kare tablosu (G0…G24) · güneş saati · master lock — ⛔ PROMPT YOK
├── <FILM>_BOLUM_1.md              ## 🎬 SAHNE 0 … 11  — 📸 GÖRSEL (Gn) + 🎥 I2V (Gn → Gn+1)
├── <FILM>_BOLUM_2.md              ## 🎬 SAHNE 12 … 23 + ## 🌟 USTA KARE — G24
├── <FILM>_KAPAK.md                G24 + başlık bandı satırı · başlık dizgisi (px) · 120 px testi · KAPAK KANITI
├── <FILM>_MUZIK.md                BPM ızgarası · katman = aşama · müziksiz pencere · ses hedefi
├── <FILM>_YAYIN_PAKETI.md         ⭐ TAMAMEN İNGİLİZCE · 3 başlık · açıklama · hashtag · sabit yorum · AI beyanı
├── <FILM>_QA_SPEC.md              künye (sahne saatleri) · FİNAL KARE KANITI · kadraj kilitleri · yapı bible sayıları ·
│                                  aynı yer nesnesi · ⑧ defteri · kesme listesi · açık kapılar — ad DEĞİŞMEZ (betikler arar)
└── <FILM>_URETIM_GUNLUGU.md       ⛔ ÜRETİM doldurur: araç kapısı · usta kare · geriye zincir G23→G0 · I2V · yedi ölçüm
                                   günlüksüz filme qa_paket.sh açılmaz [DERS 28 — dört filmde dört kez ölçüldü]
```

⭐ Üretim sırası burada da TERSTİR ve zincirlidir [KILAVUZ_REHBERI §8]: G24 usta kare önce,
image-to-image geriye G23 → … → G0, her karede `araclar/zincir_kontrol.sh` + kanıt nesnesi ELLE
[DERS 25]; sonra 24 I2V, her biri iki onaylı kareye kilitli. Bölüm dosyası ÜRETİM SIRASI değildir,
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
   S23'in tutuşundadır. Sayılar ilk yatay filmin ① koşusunda ölçülür ve §2.8'e yazılır.
③ BÖLÜM SINIRI BİR KAREDİR (G12). Dikeyde tek dosya vardı; burada iki bölüm dosyası var ve
   prompt kapısı KLASÖR MODUNDA koşulur (iki dosya birleşik) — tek bölüm dosyasına koşulan kapı
   "usta kare yok / Scene N of X tutmuyor" der ve bu bir arıza değil, eksik koşudur.
④ IŞIK GÜNÜ TOPLANIR. 24 klip × rejim B = 48 saat olurdu; kesmede ışık atlamadığı için Σ pencere
   ≤ 14 saat: rejim sütunu plana yazılır ve TOPLANIR (03_SAHNE_SIRALAMASI §4). Aşırı toplam BLOCK
   değil PLAN hatasıdır — ⑦ ve ③ mercekleri ölçer.
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

Film listesi burada tutulmaz — `QA/00_INDEX.md` tek sayaçtır (`bash araclar/sayac.sh`).
Bu klasörde henüz film yok; ilk film kart A ile (`00_ANALIZ/00_HIKAYE_ONAYI.md` onaylanmadan
dosya yazılmaz) açılır.
