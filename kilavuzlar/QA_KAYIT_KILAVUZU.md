# 🗂️ QA KAYIT KILAVUZU — ham kanıt tek kaynak, özet ondan türetilir

> `QA/00_README` merceklerin **ne** ölçtüğünü söyler. Bu kılavuz ölçümün **nasıl
> kaydedildiğini** söyler: film ve koşu için durum modeli, koşu künyesi, tek adlandırma
> şeması, ham dosyaya dokunmadan eşleme tablosu ve iki yönlü uzlaştırma kontrolleri.
>
> Kaynak: A24 · 06.10.2026 (`arastirma/SONUCLAR/A24_GEMINI_HAM.md`) · denetim
> `A20-A24_DENETIM.md` · tetikleyen: 06.10.2026 QA denetimi.
> ⭐ Rapordan inen: MEKANİZMA (tek kaynak · durum makinesi · iki yönlü yetim · "yerine
> geçti" işareti). ⛔ İnmeyen: ham dosyaya YAML enjekte etmek (kart S "dokunulmaz"
> kuralına aykırı) · küçük harfe göç · pandas/yaml'lı betik (bu makinede ikisi de yok,
> ve iskelet `---` ayıracıyla bölüyor — ham raporlarda yatay çizgi var).
> ⭐ 06.10.2026: 12 mercekli sistem `QA/ARSIV_12_MERCEK/` altına DONDURULDU; eşleme tablosu
> (393 satır) ve temizlenmiş özet orada. Bu kılavuzun yolları yeni beş mercekli düzenindir.

---

# 0. 🚪 KURAL — tek cümle

```
Bir puan, arkasında TAM durumlu bir ham dosya yoksa KAYIT DEĞİLDİR.
Bir ham dosya, eşleme tablosunda satırı yoksa ÖLÇÜM DEĞİLDİR.
Özet (00_INDEX matrisi · T tabloları · RAPORLAR künyesi) bu ikisinden TÜRETİLİR;
elle yazılan sayı yalnız uzlaştırmadan geçtiyse durur.
```

Ölçülmüş bedeli (06.10.2026 denetimi):

| arıza | ne oldu | bu kılavuzda |
|---|---|---|
| kanıt var, kayıt yok | 5 film INDEX'te "ÜRETİLMEDİ" — her birinin 8–12 ham raporu 16–25.09'dan beri depoda | §1 durum · §5 U1 |
| kayıt var, kanıt yok | THE CROSSING ④ 7,9 · ⑤ 5,8 · ⑥ 10,0 — ham dosya yok | §5 U2 |
| yanlış sayılan koşu | STONE DRAGON "12 mercek" — `_7_HAM` ikinci bir ④, `_8_DENETIM`/`_9_KONTROL` puansız | §1.2 · §5 U4 |
| eksik koşu puanlandı | RUN INCOMPLETE ile başlayan raporlar tabloya puanla girdi | §1.2 · §5 U5 |
| dört ad şeması | README · qa_paket.sh · dosyalar üç ayrı şey söylüyor | §3 |
| üç yerde üç durum | "belgesiz — TEKRARLANACAK" T'de var, matriste yok | §4 |
| sayaç kör | `sayac.sh` yalnız TOPLAM FİLM'i karşılaştırıyor | §5 |

---

# 1. 🔁 DURUM MODELİ

## 1.1 Film

```
PLANLANDI ──► ÜRETİLDİ ──► ÖLÇÜLDÜ (k/5) ──► YAYINLANDI ──► İZLEYİCİ (7. gün)
   plan +        üretim günlüğü ya da     TAM durumlu ham     yayın tarihi     IZLEYICI_DEFTERI
   SPEC          teslim dosyası beyanı    rapor sayısı k      (sahip)          satırı dolu
                 ⚠️ VEYA ham rapor var    (yalnız TAM sayılır)
```

```
⛔ Geçiş ELLE İLAN EDİLMEZ, KANITTAN OKUNUR:
   · bir filmin ham raporu varsa film en az ÜRETİLDİ'dir — günlük boş olsa bile.
     Günlük boşsa durum "ÜRETİLDİ · GÜNLÜKSÜZ" yazılır [DERS 28], "ÜRETİLMEDİ" yazılmaz.
   · "k/5" sayısı yalnız §1.2'de TAM olan koşulardan sayılır.
   · plan v2 yazıldıysa (LONG SHADOW v2) v1'in hamları v1'e aittir; v2 PLANLANDI'dır.
```

## 1.2 Koşu

| durum | ne demek | ortalamaya girer mi | örnek (denetim) |
|---|---|:-:|---|
| **TAM** | doğru video + doğru belgeler + doğru rubrik · VERDICT ve kategori puanları var | ✅ | — |
| **EKSİK** | rapor RUN INCOMPLETE diyor ya da kategori/hüküm eksik | ❌ | LAST LIFT ④ (plan + kapak yok) |
| **YANLIŞ GİRDİ** | başka filmin belgesi/videosu · mod D belgesiz · film adı tutmuyor | ❌ | DEEP STEP ⑧ ← STONE TOWER SPEC |
| **SIZINTI** | mod V raporu plan içeriği alıntılıyor [QA_KOSU §3] | ❌ (bulguları okunur) | STONE TOWER ① "G7" |
| **YERİNE GEÇTİ** | aynı film + mercek için daha yeni bir TAM koşu var | ❌ (tarihçe) | — |
| **BAĞLAYICI DEĞİL** | serbest denetim · deneme · stres testi | ❌ | STONE DRAGON `_8_DENETIM` |

```
⭐ Bulgu ile puan ayrıdır: EKSİK / SIZINTI / YANLIŞ GİRDİ koşunun BULGULARI rapora
   işlenebilir (README §3 "bulguları geçerlidir"), PUANI hiçbir özete girmez.
⛔ Bir koşunun durumu ham dosyaya YAZILMAZ — ham dosya dokunulmazdır. Durum §2.2
   eşleme tablosunda tutulur; değişince (ör. YERİNE GEÇTİ) yalnız o satır değişir
   ve git geçmişi kimin ne zaman değiştirdiğini saklar.
```

---

# 2. 🏷️ KÜNYE VE EŞLEME

## 2.1 Yeni ham rapor — künye kaydederken yazılır

Model çıktısı **altına** olduğu gibi yapıştırılır; künye **üstüne**, kaydeden kişi ya da
ajan tarafından yazılır (araştırma hamlarındaki künyeyle aynı disiplin). Alanların içeriği
`QA_KOSU_KILAVUZU §2` manifestosudur; burada yalnız biçim:

```
---
film:        THE_BLUE_SILO
mercek:      Q4_INSA
dosya:       blue_silo_2x.mp4 · sha256 3f9a1c… (ilk 12) · 28,00 sn · 1080×1920 · 2x
belgeler:    THE_BLUE_SILO_QA_SPEC.md ("# 🔒 THE BLUE SILO — QA SPEC")   | YOK (mod V)
rubrik:      QA/Q4_INSA.md @ <git kısa hash>
paket:       QA/KOSU/THE_BLUE_SILO/Q4_INSA_paket.md · blok dolu · klip 7 · ihraç ✅   ← qa_paket.sh yazar
model:       Gemini <sürüm> · sohbet | API · proje DIŞI · geçici sohbet ✓
tarih:       gg.aa.yyyy
geri_okuma:  dosya adı ✓ · belge başlığı ✓          ← modelin ilk satırı [QA_KOSU §2.2]
durum:       TAM
---
<model çıktısı — dokunulmaz>
```

```
⭐ Neden YAML çitleri: makine okur (§5), insan da okur. Çitin İÇİ künyedir; ALTI kanıttır.
⛔ Künye 06.10.2026'dan SONRAKİ ham raporlarda zorunludur. Öncekilere EKLENMEZ — §2.2.
⛔ 28.10.2026'dan sonraki koşuda "paket:" satırı olmayan ham TAM yazılmaz (kayit_kontrol K1).
```

## 2.2 Eski arşiv — eşleme tablosu, ham dosyaya dokunmadan

`QA/ARSIV_12_MERCEK/00_ESLEME.tsv` — ✅ 06.10.2026 yazıldı · 393 satır · her ham dosyaya bir satır:

```
dosya	film	mercek	durum	puan	olumsuz_hüküm	kaynak	not
THE_DEEP_STEP/THE_DEEP_STEP_8_YONTEM_HAM.md	THE_DEEP_STEP	8_YONTEM	YANLIŞ GİRDİ	5,1	STONE TOWER SPEC'i verildi
THE_STONE_DRAGON/THE_STONE_DRAGON_7_HAM.md	THE_STONE_DRAGON	4_TESLIM	YERİNE GEÇTİ	6,5	ikinci ④ koşusu · ⑦ DEĞİL
THE_STONE_DRAGON/THE_STONE_DRAGON_8_DENETIM_HAM.md	THE_STONE_DRAGON	—	BAĞLAYICI DEĞİL	—	serbest denetim · RED
```

```
⭐ Dosya yeniden ADLANDIRILMAZ. Şema dışı ad (§3) tabloda doğru film + mercekle
   eşlenir; ad hatası tarihin parçası olarak kalır.
⭐ "puan" sütunu ham dosyanın KENDİ AVERAGE satırıdır (model ne dediyse); yeniden
   hesaplanan puan RUBRIK_YAZIM §4'e göre ayrı sütuna (ileride) yazılır.
⛔ Tablo doldurulmadan INDEX matrisindeki eski puanlara "doğrulandı" denmez.
```

---

# 3. 📛 TEK ADLANDIRMA ŞEMASI

```
QA/HAM/<FILM>/<FILM>_Q<n>_<AD>_HAM.md          ilk koşu
QA/HAM/<FILM>/<FILM>_Q<n>_<AD>_HAM_K2.md       ikinci koşu (test-tekrar · yeniden koşu)
QA/HAM/<FILM>/<FILM>_B<b>_Q<n>_<AD>_HAM.md     yarım master bölümü (yatay)

<n>   1–5 · <AD>  GORUNTU · ZAMAN_KESME · SANTIYE · INSA · TESLIM  (rubrik dosyasının adı)
```

| karar | neden |
|---|---|
| `Q<n>_<AD>` = rubrik dosya adı | paket, rubrik ve ham aynı adı taşır; 12 mercekte paket sırası ile mercek numarası ayrıydı (paket 2 = ③) |
| büyük harf kalır | depo geleneği; tek şema varken büyük/küçük çakışması doğmaz (rapor küçük harf önerdi — inmedi) |
| `_K2` eki | yeni koşu eskisini silmez; eskisi YERİNE GEÇTİ olur (FILMLER mercek tablosunda) |
| eski 393 ham yeniden adlandırılmaz | arşivdedir; dört eski şema `00_ESLEME.tsv`'de film + mercekle eşlendi |

---

# 4. 📊 ÜÇ YER, TEK DURUM

Aynı puan üç yerde görünür. **Kaynak sırası** budur ve aşağıdaki yukarıdakini ezemez:

```
1. ham dosya (+ künye)                       kanıt          QA/HAM/<FILM>/
2. FILMLER/<FILM>.md mercek tablosu          durum + puan   (künyeden; sonradan değişen durum burada)
3. QA/TABLO.md                               GÖRÜNÜM        (FILMLER'den)
```

```
⭐ Görünümde durum etiketi TEKTİR ve eşleme tablosundan gelir:
     TAM → puan · EKSİK → "EKS" · YANLIŞ GİRDİ → "YG" · SIZINTI → "SZ" ·
     YERİNE GEÇTİ → görünmez · BAĞLAYICI DEĞİL → görünmez
   Ⓥ ("mod V ön koşu") ayrı bir eksen değildir: mod D merceği belgesiz koştuysa
   durumu YANLIŞ GİRDİ'dir.
⛔ Bir hücrede "Ⓥ 9,6" ile T tablosunda "belgesiz — TEKRARLANACAK" yan yana duramaz.
```

## 4.1 FILMLER/<FILM>.md — zorunlu bölümler (şablon: QA/FILMLER/00_README.md)

```
KÜNYE · MERCEKLER (her biri: durum · puan · VERDICT · en ağır üç bulgu) ·
DOKÜMAN (mod V soruları ve cevapları) · OLAY TABLOSU (E01… · QA/FILMLER/00_README) ·
KARAR (yeniden üretilecek · kabul edilen · sebep) · DERS (numara ya da "yeni ders yok")
```

```
⛔ 20.09'dan sonra yazılan ~16 raporda KARAR ve DERS yok; OLAY TABLOSU yalnız 8'inde.
   Eksik bölüm "—" ile AÇILIR, atlanmaz: "DERS — yeni ders yok" bir bilgidir,
   bölümün hiç olmaması bilgi değildir.
```

---

# 5. 🔍 UZLAŞTIRMA KONTROLLERİ — `sayac.sh` genişler

Her biri tek cümlelik geçti/kaldı tanımıdır. **U1–U5 ilk aşamadır** (bugünkü arızaları
yakalar); U6–U10 künyeli dosyalar biriktikçe açılır.

| # | kontrol | KALDI demek | yakaladığı (06.10) |
|:-:|---|---|---|
| U1 | kanıt var, kayıt yok | ham klasörü olan film INDEX'te ÜRETİLMEDİ ya da matriste satırsız | 5 film |
| U2 | kayıt var, kanıt yok | matriste puanlı hücrenin ham dosyası (eşleme satırı) yok | CROSSING ④⑤⑥ |
| U3 | şema dışı ad | §3 deseni tutmayan ve eşleme tablosunda satırı olmayan ham dosya | STONE DRAGON `_7/_8/_9` · POLAR `_9_AKTIVITE` |
| U4 | çift aktif koşu | aynı film + mercek için iki TAM satır | — |
| U5 | eksik koşu puanlı | ilk satırı RUN INCOMPLETE olan dosyanın puanı görünümde | LAST LIFT ④ · IRON BRIDGE ④ … |
| U6 | künyesiz yeni ham | 06.10.2026 sonrası eklenmiş, `---` künyesi olmayan ham | — |
| U7 | sızıntı | mod V hamında QA_KOSU §3 sızıntı listesinden kelime | 6 film |
| U8 | belge başka filmin | künyedeki belge adı/başlığı film adını taşımıyor | DEEP STEP ⑧ · STAR DOCK ⑧ |
| U9 | k/12 iddiası | INDEX'teki "k mercek" sayısı TAM satır sayısına eşit değil | STONE DRAGON 12 ≠ 9 |
| U10 | rapor bölümleri | RAPORLAR dosyasında §4.1 bölümlerinden biri yok | ~16 dosya |

```
⭐ Betik standart kütüphaneyle yazılır (bu makinede pyyaml ve pandas YOK):
   künye = ilk satır "---" ile ikinci "---" arası, "anahtar: değer" satırları.
   Ham dosyanın gövdesinde "---" geçebilir — yalnız İLK çit okunur.
⛔ Aynı film + mercekte iki TAM puan bulunursa betik ORTALAMA ALMAZ, KALDI verir (U4).
   (Rapordaki iskelet çakışmada ortalama alıyordu — inmedi.)
```

## 5.1 Türetme — hedef

```
00_ESLEME.tsv + künyeler ──► araclar/qa_tablo.py ──► 00_INDEX matrisi · T1–T12
                                                     (betiğin yazdığı bloklar
                                                      "⛔ ELLE DÜZENLENMEZ" başlığı taşır)
```

Betik yazılana kadar INDEX elle tutulur, ama **U1–U5 geçmeden INDEX'e sayı yazılmaz.**

---

# 6. 🚚 GÖÇ — 06.10.2026 durumu

```
✅ 1. 00_ESLEME.tsv          393 ham → durum (ARSIV_12_MERCEK/) · ham dosyaya dokunulmadı
✅ 2. arşiv                   12 mercek · INDEX · T1–T8 · RAPORLAR · HAM_RAPORLAR · çapraz analiz →
                              QA/ARSIV_12_MERCEK/ (git mv) · temizlenmiş özet 00_ARSIV.md
                              (5 film "ÜRETİLDİ" · STONE DRAGON 9 mercek · CROSSING hamsız puanlar orada)
✅ 3. yeni düzen              QA/00_README · Q1–Q5 · TABLO.md · HAM/ · FILMLER/
✅ 4. sayac.sh                TABLO karşılaştırması · U1 · U2 · arşiv ↔ eşleme sayımı
✅ 5. qa_paket.sh             künye taslağı + ölçülmüş olgular bloğu rubriğin içinde · 5 paket
⬜ 6. qa_tablo.py             TABLO.md'yi FILMLER'den türetir — ilk beş mercekli koşular gelince
⬜ 7. U3–U10                  künyeli dosyalar biriktikçe sayaca eklenir
```
