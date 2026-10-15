# 🏗️ Yatay 12 Dakika Timelapse — 90 Sahne · 3 Bölüm · 91 Kare

> **Açılış:** 13.10.2026 · sahip kararı (THE SKY STATION senaryosu: "yatay 12 dk'lık filmler klasörü açalım").
> Yatay (16:9) merdivenin BEŞİNCİ basamağı: yatay_8_dk_filmler/ 48 → **bu klasör 90 sahne · 12:00**.
> Iskelet öbür basamaklarla aynı (PLAN · BOLUM_n · KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC · URETIM_GUNLUGU + `00_ANALIZ/`).
> **Fark: iki değil ÜÇ bölüm** — ışık günü ve QA birimi bunu zorunlu kılar (aşağıda).
>
> Geçerli kart: `kilavuzlar/KILAVUZ_REHBERI.md` §2.8 · iskelet `kilavuzlar/FILM_KLASOR_SABLONU/` ·
> akış `AGENTS.md` kart A + kart Y2 · zincir §2.7 (N sahne = N+1 kare · T2V yok) · anlatı `UZUN_FORM_ANLATI_KILAVUZU`.

---

## 📐 FORMAT KURALLARI

| Özellik | Değer |
|---|---|
| **Süre** | 12:00 sahne bloğu (**90 × 8,0 s = 720,0 s**) · kapak kartı filmin kararıdır (THE SKY STATION: ⛔ YOK → 720,0 s) |
| **Oryantasyon** | 16:9 yatay · 1920×1080 · 30 fps · tek master (dikey master AYRICA üretilmez) |
| **Toplam sahne** | 90 — S0 = kanca, İLERİ yönlü [DERS 3] · S89 = teslim, usta kare G90'a biter |
| **Kare / prompt** | ⭐ **91 görsel** (G0…G90; G90 = USTA KARE) + **90 I2V** · ⛔ T2V YOK · toplam **181 prompt** [§2.7] |
| **Yapı** | ⭐ **3 bölüm × 30 sahne** — `BOLUM_1` = S0–S29 (G0…G29) · `BOLUM_2` = S30–S59 (G30…G59) · `BOLUM_3` = S60–S89 + USTA KARE (G60…G90). Bölüm sınırları **KAREDİR (G30 · G60)**, kesme değil; ışık ve yapı orada atlamaz [DERS 52] |
| **Klip süresi** | 8,0 s teslim (sahip ızgarası — THE LAST CARRIAGE · THE SLOW TAKEOFF emsali) → üretim ≥ 9,0 s, baştan 1,0 kırp [A7-b] · ⛔ ARAÇ KUTU SETİ ölçülmeden ızgara kesinleşmez [DERS 23 · 31] |
| **Izgara** | ⛔ DÜZ 90 × 8,0 (sahip beyanı). Karşı kayıt: düz ızgara üç filmde METRONOM [DERS 13 · 24 · 44] — ritim klip İÇİNE taşınır (iş yönü · rejim nabzı A/G · müzik katmanı · perde başı kanca) |
| **Kamera** | MAIN STATION — tek istasyon, tilt 0. Yatay formül: **yüzde(y) = 50 + 118,5·(y − h)/D** (alt kenardan) · x(m) → **%50 + 66,7·x/D** (soldan) · ikinci istasyon yalnız sahip kararıyla [ISTASYON_VE_IC_MEKAN §1] |
| **Işık günü** | ⛔ Kesmede ışık atlamaz → Σ rejim penceresi ≤ **14 saat**. ⚠️ **90 × A (10 dk) = 15 sa — sınırı AŞAR.** Bu basamakta en az **6 klip rejim G** (gerçek zaman, 0 dk) zorunludur; B (2 sa) neredeyse hiç kullanılamaz (1 × B = 12 G gerektirir). G yalnız ödül hareketinde (ilk geçiş, final) [SANTIYE_HAREKETI §1] |
| **Aşama merdiveni** | 90 satır — sahne arttıkça aşama İNCELİR (%25/%50/%75 ara hâller ayrı satır), yapı büyümez · üç zorunlu satır KANIT · LOOP · SÖKÜM |
| **QA birimi** | ⭐ **BÖLÜM — üç masterın her biri 240 s** (= 4 dk filmin ölçeği; mercekler 60–240 s'de kalibre). Beş mercek (❶–❺) her bölüme AYRI → **15 ham rapor**. Kör merceklere tek satır beyan: `"THIS FILE IS PART n OF 3 — scenes S… — …"` |
| **Müzik** | yatay hat ✅ VAR (sahip 05.10.2026) · 120 BPM · 8,0 s = 4 ölçü · müziksiz pencere S0 · 720,0 s [MUZIK_VE_KAPAK §1] |

---

## ⛔ ARAÇLAR BU BASAMAĞI HENÜZ TANIMIYOR (13.10.2026)

| araç | durum | ne gerekir |
|---|---|---|
| `film_klasoru_ac.sh` | `yatay_12_dk_filmler` → "format klasörü tanınmadı"; 2 bölüm sabit | `case` satırı (90 · 8) + 3 bölüm iskeleti |
| `sayac.sh` | `FORMATLAR` listesinde yok → bu klasördeki filmler SAYILMAZ | listeye ekleme |
| `prompt_kontrol.py` | klasör modu BOLUM_1 + BOLUM_2 birleştirir; BOLUM_3'ü görmez | üç bölüm birleştirme |
| `qa_paket.sh` | `--bolum 1\|2` | `--bolum 3` |

⛔ Araçlar güncellenmeden bu basamakta prompt kapısı ve QA paketi KOŞMAZ. Sahip onayıyla ayrı iş olarak yapılır.
Bu klasörün ilk filmi (THE SKY STATION) bu yüzden şimdilik yalnız **PLAN** dosyasıyla açıldı.

---

## 📏 MERDİVEN — komşu basamaklar

| Özellik | 48 · 8 dk | **90 · 12 dk** |
|---|---|---|
| Klasör | `yatay_8_dk_filmler/` | `yatay_12_dk_filmler/` |
| Kare / I2V | 49 / 48 | **91 / 90** |
| Bölüm | 2 × 24 · sınır G24 | **3 × 30 · sınır G30 · G60** |
| Teslim | 485,0 s | **720,0 s** (kartsız) |
| Işık günü | A + ≤3 B | **A + ≥6 G** (B yok) |
| QA birimi | BÖLÜM (2 × 5) | **BÖLÜM (3 × 5)** |
| Merak zinciri | 5 soru | **6–7 soru** · yeniden kanca ≈ her perde (9 klip ≈ 72 s) |

⛔ Bu klasörün köküne `.md` bırakma — yalnız bu README durur (sayaç kökteki her klasörü BİR FİLM sayar).

---

## 🎞️ FİLMLER

Film listesi burada tutulmaz — `QA/TABLO.md` tek sayaçtır (`bash araclar/sayac.sh`).
İlk film: `THE_SKY_STATION/` — plan + **181 prompt perde perde klasörlerde** (`PERDE_01_…` … `PERDE_10_…`, sahip kararı
13.10.2026: 10 perde × 9 sahne; her sahnenin başında Türkçe "önceki sahneye göre değişen" notu). Prompt dosyası PERDE'dir;
QA ve montaj birimi yine 3 BÖLÜM'dür (G30 · G60). Kapı birleşik dosyayla koşar (PLAN'daki ÜRETİM ÖNCESİ DURUM).
