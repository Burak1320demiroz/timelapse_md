# 🔎 A20–A24 DENETİM — QA onarımı · 06.10.2026

> Kaynak: `A20_GEMINI_HAM.md` … `A24_GEMINI_HAM.md` (beş rapor · proje sahibi tek mesajda
> verdi · bot beyan edilmedi, "[cite: n]" izi Gemini Deep Research) · promptlar
> `arastirma/A20…A24_*.md` (06.10.2026 · altı cümle · BU DEPODA YAZILDI).
> Yordam: `arastirma/00_README.md §3` — etiket · kaynak sınıfı · çelişki · ölçüm.

```
⭐ BU KUŞAĞIN FARKI
   ① SORUYU BİZ YAZDIK, arızaları sayıyla verdik (06.10 QA denetimi). Raporlar bizim
      sayılarımızı tekrar ediyor — onlar KANIT değil, bizim ölçümümüzdür.
   ② KAYNAKÇA ÇEKİLDİ (§2): 61 atıf · 32 ✅ · 24 ⚠️ · 2 ❌ · 3 ❓. ⚠️'lerin çoğu GERÇEK bir
      makale ama BAŞKA konuda — atıf uydurma değil, yanlış iliştirme. A24 en zayıf.
   ③ KOMUTLAR KOŞTURULDU (§1): A21'in 4 komutu · A23'ün 10 tohumlama komutu. A23'te
      10'un 5'i olduğu gibi kullanılamadı; A21'in kesme komutu düşük kontrastta yarı kör.
   ④ İKİ RAPOR BİRBİRİYLE ÇELİŞİYOR (§3) — kart S §4: çelişen sayı ölçülmemiştir.
⇒ Kılavuza inen: MEKANİZMA + bu makinede sınanmış KOMUT + yeniden hesaplanmış ARİTMETİK.
  Rapordan doğrudan inen yeni sayı: Gemini API dokümanının üç değeri (1 fps · ~70 token/kare ·
  fps ayarı) — kaynak çekildi.
```

---

# 1. ÖLÇTÜM — bu makinede (ffmpeg 8.1 · PySceneDetect 0.6.7.1 · Python 3)

## 1.1 Sentetik sınama dosyaları

```
base.mp4  7 klip × 4,0 sn = 28,0 sn · 1080×1920 · 30 fps · sabit "kamera" · yapı her
          kesmede 150 px sıçrar (belirgin kesme) · ses yok
soft.mp4  aynı · yapı her kesmede 25 px sıçrar (düşük kontrast — gerçek kesmeye yakın)
          ffmpeg scene skoru kesmelerde 0,055–0,278 · klip içi tavan 0,00007
          (gerçek teslimde 0,016–0,022 ölçülmüştü [DERS 31] — sentetik HÂLÂ kolay)
```

## 1.2 A21 komutları

| # | komut | sonuç |
|:-:|---|---|
| 1 | `ffprobe … stream=width,height,r_frame_rate,duration` | ✅ 1080 · 1920 · 30/1 · 28,0 |
| 2 | `ffprobe -select_streams a … codec_type` | ✅ boş çıktı = ses akışı yok |
| 3 | `scenedetect -i f.mp4 detect-content -t 27.0 list-scenes` | ✅ base: 7/7 · ⛔ **soft: 6 kesmenin 3'ü** · `-t 10` → 5 · `-t 5` → 6 |
| 3' | `bash araclar/kesme_kontrol.sh soft.mp4 <7×8 plan> --hiz 2` (bizim top-N) | ✅ **6/6 · marj 270 kat** |
| 4 | `ffmpeg -i f -filter_complex "tblend=all_mode=difference,blackframe=99:32" -f null -` | ⚠️ koştu ama AYIRT ETMİYOR: 28 sn + 2 sn donmuş sonlu dosyada ~890 karenin hepsini "siyah fark" saydı (yavaş değişen kare = durağan sanılıyor) |

⇒ "eşik 27–30 ile sert kesmelerin %99'u yakalanır" — kaynaksız (PySceneDetect'in kendi
ölçümü %63–85) ve bizim ölçümümüzde YANLIŞ. Kesme yeri top-N ile kalır.

## 1.3 A23 tohumlama komutları — 10'un 5'i olduğu gibi kullanılamadı

| # | rapordaki | sonuç | yerine (sınandı ✅) |
|:-:|---|---|---|
| 1 | `crop=iw:ih/2:0:t*300` | ⚠️ koştu · çıktı 1080×**960** — kayma değil boyut | `crop=iw-48:ih-48:x='if(gte(t,12),48,0)':y='…',scale=1080:1920` |
| 2 | `setpts=0.5*PTS` | ✅ 28 → 14 sn | — |
| 3 | `drawtext=…` | ⛔ **koşmadı** — bu ffmpeg freetype'sız | `drawbox` logo yaması |
| 4 | `-t 24 -c copy` | ✅ 24,07 sn | — |
| 5 | `drawbox … enable=between(t,5,6)` | ⚠️ koştu · nesne KAYBETTİRMİYOR, kara leke EKLİYOR | aynı komut, adı "leke" |
| 6 | `colorbalance … enable` | ✅ | — |
| 7 | `scale=iw:ih*0.7:enable=…` | ⛔ **koşmadı** — scale zaman çizelgesi desteklemez | `split + crop + scale + overlay:enable` |
| 8 | `boxblur … enable` | ✅ | — |
| 9 | `loop=60:1:300` | ⚠️ koştu · süre 28 → **30 sn** (kare ekliyor, bütün kesmeler kayar) | `[0][1]freezeframes=first=300:last=359:replace=300` (iki girdi) |
| 10 | `eq=brightness=-0.8` | ✅ | — |

## 1.4 Aritmetik

```
Güç (Fisher z · α 0,05 iki yönlü · güç 0,80):  n = ((1,960 + 0,842) / atanh ρ)² + 3
   ρ 0,50 → 29,0 (rapor: 28) · ρ 0,40 → 46,7 · ρ 0,30 → 84,9 (rapor: 85 ✅)
Model kare bütçesi: 2x dikey 28 sn · 1 fps → 28 kare · klip başına 4 (doküman 1 fps ✅)
```

---

# 2. KAYNAK ÇEKİMİ — 06.10.2026 (WebFetch/WebSearch · ajan)

| rapor | ✅ | ⚠️ | ❌ | ❓ | not |
|---|:-:|:-:|:-:|:-:|---|
| A20 körlük | 8 | 5 | 0 | 0 | ⭐ Gem bilgi dosyaları her sohbete girer ✅ · geçici sohbet kişiselleştirmeyi kapatır ✅ · proje dosyaları paylaşılır ✅ · "temperature 0 deterministik" ⚠️ (Google: "çoğunlukla") · "aynı tarayıcıda oturum belleği" · "Drive önbellek çakışması" belgesiz |
| A21 ölçüm | 8 | 6 | 2 | 1 | Gemini token/fps dokümanı ✅ · Video-MME ✅ · "MVBench sayma" aslında VideoReasonBench genel skoru ⚠️ · TempCompass 63,9 başka makalenin ortalaması ⚠️ · "2502.1315" ❌ · "%99" ❌ · sohbet arayüzünün kare örneklemesi belgesiz ❓ |
| A22 rubrik | 6 | 1 | 0 | 1 | CheckEval ✅ (IEA α 0,67 vs G-Eval 0,05) · G-Eval 0,514 ✅ · ⭐ JSON "biçim vergisi" 2606.09410 ✅ (−28/−36 puan · gecikmeli yapı kurtarıyor) · TICK ID'si başka makale ⚠️ · BARS 2,30/4,34 bulunamadı ❓ |
| A23 güvenilirlik | 8 | 6 | 0 | 1 | Koo & Li ICC ✅ · Krippendorff eşik ✅ · kappa deflasyonu ✅ · ⚠️ Qwen3 %61,3 sıcaklık **0,6**'da (rapor "0" dedi) · CUSUM/EWMA atfı yüz mimiği makalesi ⚠️ · Reddit erişilemedi ❓ |
| A24 kayıt | 2 | 6 | 0 | 0 | ⚠️ FDA "Q15" → doğrusu Q12 (transkripsiyon) · ALCOA+ FDA'da değil, ALCOA Q1a'da · ⚠️ check-jsonschema Markdown ön bilgisini OKUMAZ · üç arXiv atfı başka konu · BIDS ✅ · Smithsonian ✅ ("Stanford" denmiş) |

```
⭐ En sonuçlu üç yanlış atıf:
   1. DETERMİNİZM — iki rapor sıcaklık 0'ı iki zıt yönde kullanıyor; ikisi de kaynağa uymuyor.
   2. check-jsonschema — A24'ün pre-commit planı bu araçla kurulamaz (ön bilgiyi önce
      ayıklayan adım gerekir) → QA_KAYIT §5 standart kütüphaneyle.
   3. A21 benchmark tablosu — "sayma %6,9–27,4" sayıları başka bir benchmark'ın genel
      skorları; "model sayamaz" sonucu yine de BİZİM ölçümümüzle (1…23 klip) ayakta.
```

---

# 3. ÇELİŞKİLER — kart S §4

| # | çelişki | karar |
|:-:|---|---|
| Ç1 | A20 "sıcaklık 0 = deterministik" ↔ A23 "sıcaklık 0'da bile %61 tutarlılık" | ikisi de kaynağa uymuyor (§2) → determinizm VARSAYILMAZ, ÖLÇÜLÜR [QA_KALIBRASYON §1] |
| Ç2 | A20 "süre geri okuması ±%10 tolerans kapısı" ↔ A21 "model süre ölçemez" | A21 + bizim ölçüm (2x'e "32 sn") → süre geri okuması KAPI DEĞİL [QA_KOSU §2.2] |
| Ç3 | A22 "hüküm kategorilerden türetilmeli" ↔ README §4 "hüküm kazanır" | KISMEN: "KÖTÜ OLAN KAZANIR" — kötü hüküm iyi kategoriyi ezer; iyi hüküm sahip kategori ≤ 3'ü ezemez, rapor tutarsız [RUBRIK_YAZIM §4.3] |
| Ç4 | A22 havuzlu mikro-ortalama ↔ "her mercek tek soru" | İNMEDİ: asimetrinin sebebi ortalama türü değil ⑨ ⑩ çakışması → sahiplik tablosu [RUBRIK_YAZIM §4.2 · §5] |
| Ç5 | A24 "ham dosyaya YAML enjekte et, durum değişince güncelle" ↔ kart S "ham dokunulmaz" | İNMEDİ: yeni hamlarda künye kaydederken; eski arşiv için eşleme tablosu; durum tabloda [QA_KAYIT §2] |
| Ç6 | A24 "dosya adları küçük harf, sıfır dolgulu" ↔ 25 filmin büyük harfli şeması | İNMEDİ: tek şema seçildi (çoğunluğunki) [QA_KAYIT §3] |
| Ç7 | A23 "2x'te 4 sn'lik klip 2–3 sn dikkat sınırını aşıyor" ↔ sahip kuralı 7 × 8 · 2x | İNMEDİ: kaynak blog sınıfı; defter S5 kendi verisiyle sınar |
| Ç8 | A20 "kör merceğin 'belge yok' demesi James endeksine göre başarı" ↔ kendi tespiti "RUN INCOMPLETE listesine alındı" | KISMEN: kör merceğin "belge yok" demesi sızıntı DEĞİLDİR (doğru) — ama rubrik 9'un "belge yoksa mod V'ye geç" satırı kopyalama hatasıdır [RUBRIK_YAZIM §6] |

---

# 4. KILAVUZA İNEN — ve inmeyen

| kod | kılavuz | inen | inmeyen |
|---|---|---|---|
| A20 | `QA_KOSU_KILAVUZU` | Gem/proje/kişisel bağlam yalıtım tablosu · geçici sohbet kuralı · geri okuma (ad + belge başlığı) · sızıntı listesi · kanarya · fail-closed tablosu · sohbet↔API karşılaştırması | süre kapısı · körlük endeksleri · "tensör kalıntısı" teşhisi · JSON "400 garantisi" |
| A21 | `QA_OLCUM_ZEMINI_KILAVUZU` | ÖLÇÜLMÜŞ OLGULAR bloğu · 1 fps sınırı · iki dosya önerisi · D1–D5 doğrulama | `-t 27` eşiği · tblend statik testi · benchmark tablosu · contact sheet faydası |
| A22 | `RUBRIK_YAZIM_KILAVUZU` | format değişkenleri · "kanıtsız en fazla 7" (VARSAYIM) · ortalama kodda · öldürücü hüküm · kusur sahipliği · önce gerekçe sonra puan | mikro-ortalama · rapordaki iskelet · "Promise < 5 → FAIL" |
| A23 | `QA_KALIBRASYON_KILAVUZU` | 3 × 4 × 3 pilot · medyan · çelişki kuralı · sınanmış tohumlama seti · çapa film · Spearman + güç (yeniden hesaplandı) | EWMA/CUSUM · izleyici eşikleri · "sıcaklık 0'da %61" |
| A24 | `QA_KAYIT_KILAVUZU` | durum modeli · künye · eşleme tablosu · tek şema · U1–U10 · türetme hedefi | YAML enjeksiyonu · küçük harf · pandas/pyyaml iskeleti · content_hash (git geçmişi yeter) |

⛔ **Araştırma bulgusu ders DEĞİLDİR** (`arastirma/00_README §3`). Hepsi `DERSLER.md`
A20–A24 bölümünde VARSAYIM olarak durur; ilk sınavı kalibrasyon pilotu (QA_KALIBRASYON §1)
ve kör merceklerin geçici sohbette yeniden koşusudur.
