# 🔍 QA — BEŞ MERCEK

> Bu klasör **rubrikleri** (girdi), **ham raporları** (kanıt) ve **film kayıtlarını**
> (çıktı) tutar. 06.10.2026'da 12 mercekli sistem arşivlendi (`ARSIV_12_MERCEK/00_ARSIV.md`):
> belge isteyen koşuların yarısı belgesizdi, dört mercek aynı kusuru dört kez sayıyordu,
> 2x kopya "kesik" okunuyordu. Yeni sistem beş mercek, tek kayıt düzeni ve makinede
> ölçülmüş olgularla çalışır.
>
> Kılavuzlar: `kilavuzlar/QA_KOSU` (nerede, nasıl koşulur) · `QA_OLCUM_ZEMINI` (model
> saymaz, makine ölçer) · `RUBRIK_YAZIM` (rubrik nasıl yazılır, puan nasıl birleşir) ·
> `QA_KALIBRASYON` (hakem tutarlı mı) · `QA_KAYIT` (nasıl kaydedilir).

---

## 1. BEŞ MERCEK

| | dosya | tek soru | mod | girdi | hüküm |
|:-:|---|---|:-:|---|---|
| ❶ | `Q1_GORUNTU.md` | Tek kameradan tek bir timelapse mi, görüntü katı mı? | **V** | video + kareler | TIMELAPSE / SEPARATE IMAGES ⛔ · SOLID / MELTING |
| ❷ | `Q2_ZAMAN_KESME.md` | Zaman tek yönde, tek hızda geçiyor mu; kesme "zaman" mı demek? | **V** | video + ölçülmüş olgular | PASSING / WRONG DIRECTION / ONLY LIGHT · TIME / NEXT |
| ❸ | `Q3_SANTIYE.md` | Her kesmede aynı dünya mı; şantiye hep çalışıyor, her değişimin sebebi görünüyor mu? | **V** | video + kareler (dikiş çiftleri) | SAME WORLD / REBUILT ⛔ · WORKING / PARKED |
| ❹ | `Q4_INSA.md` | Tek ve tutarlı yapı mı; parça parça, görünen bir eliyle, davetli kadroyla mı yapıldı? | **D/V** | video (+ isteğe bağlı QA_SPEC + plan) | SAME / DIFFERENT ⛔ · BUILT / APPEARING · INVITED / INTRUDERS |
| ❺ | `Q5_TESLIM.md` | Vaat ekrana çıktı mı; film BİTİYOR mu (oturuyor mu), DURUYOR mu? | **D/V** | yayın dosyası (+ isteğe bağlı plan + kapak) | ENDS / STOPS |

```
⛔ ÖLDÜRÜCÜ HÜKÜM — ❶ SEPARATE IMAGES · ❸ REBUILT · ❹ DIFFERENT
   üçünden biri → FİLM DÜŞTÜ, ortalama ne olursa olsun (eski asgari set ① ② ⑤'in karşılığı).
   ❺ STOPS → yeniden üretim sebebi (öldürücü listeye girmesi sahip kararıdır).
⭐ KÖR (V) modda mercekler filmi planı hiç görmemiş izleyici gözüyle okur; sonunda QUESTIONS FOR THE
   DOCUMENT listesi çıkarır, ajan plandan cevaplar. BELGELİ (D) modda sözleşme denetimidir.
   Belge yoksa ❹ ve ❺ de mod V'de (iç tutarlılık, inşa mantığı ve ekrandaki vaat/sonuçla) tam koşar;
   ASLA durmaz, RUN INCOMPLETE vermez.
⭐ Her kusurun TEK sahibi var; rubrikler sınır cümlesi taşır ("SEE LENS n") [RUBRIK_YAZIM §5].
```

| eski | yeni |
|---|---|
| ① KARE · ⑫ KATILIK | ❶ |
| ③ ZAMAN · ⑥ GEÇİŞ | ❷ |
| ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET | ❸ |
| ② İNŞA · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER | ❹ |
| ④ TESLİM | ❺ |

---

## 2. ÇALIŞTIRMA

```
0. MAKİNE   bash araclar/qa_paket.sh <film_klasoru> <dosya.mp4> [kapak] [--hiz 2] [--master <1x.mp4>]
            → kare_al.sh (klip başına ilk/orta/son + dikiş çiftleri)
            → kesme_kontrol.sh (top-N) · ffprobe · SSIM → ÖLÇÜLMÜŞ OLGULAR bloğu
            → QA/KOSU/<FILM>/Q<n>_<AD>_paket.md × 5 — blok rubriğin İÇİNDE, künye taslağı üstte
            ⛔ üretim günlüğü yoksa durur [DERS 28]

1. ❶ GÖRÜNTÜ        ⛔ BELGE YOK   video + kareler
2. ❷ ZAMAN VE KESME ⛔ BELGE YOK   video (+ blok)
3. ❸ ŞANTİYE        ⛔ BELGE YOK   video + kareler
4. ❹ İNŞA           video + <FILM>_QA_SPEC.md + plan
5. ❺ TESLİM         yayın dosyası + plan + kapak
   ⭐ Kör mercekler ÖNCE koşulur: önce belge görüp sonra "kör koşuyorum" demek körlüğü
      zaten kaybetmektir.
```

```
⛔ YALITIM [QA_KOSU §1] — her mercek AYRI, GEÇİCİ sohbette, Gemini projesi/Gem DIŞINDA.
   Gem ve proje dosyaları o Gem'in/projenin BÜTÜN sohbetlerine girer; plan oradaysa kör
   mercek planı görür. Belgeli mercekte belge o sohbete ELLE eklenir.
⭐ HANGİ DOSYA [QA_OLCUM_ZEMINI §3]: ❸ ❹ 1x master (varsa — klip başına iki kat kare) ·
   ❶ ❷ ❺ yayın dosyası (dikey: 2x). Blok her paketi kendi dosyasının değerleriyle doldurur.
```

---

## 3. RAPOR GELDİĞİNDE

```
1. HAM      QA/HAM/<FILM>/<FILM>_Q<n>_<AD>_HAM.md — künye üstte, model çıktısı altta, DOKUNULMAZ
            [QA_KAYIT §2.1] · ikinci koşu _K2 · yarım master bölümü <FILM>_B<b>_Q<n>_…
2. GERİ OKUMA  ilk üç satır: dosya adı · belgeler · görülen klip sayısı [QA_KOSU §2.2]
            dosya adı ya da belge tutmuyorsa → koşu YOK, yeniden koş
3. DOĞRULAMA   D1–D5 [QA_OLCUM_ZEMINI §5] — dosya dışı damga · klip sayısı · süre itirazı ·
            kesme damgası · kart · kör raporda sızıntı [QA_KOSU §3]
4. DURUM    TAM · EKSİK · YANLIŞ GİRDİ · SIZINTI · TUTARSIZ · YERİNE GEÇTİ · BAĞLAYICI DEĞİL
            [QA_KAYIT §1.2] — yalnız TAM puan taşır
5. PUAN     mercek puanı = tetiklenen kategorilerin ortalaması — AJAN hesaplar (rubrik AVERAGE
            yazdırmaz) · film puanı = TAM merceklerin ortalaması + N ("9,1 · N=5")
            hüküm ↔ kategori: KÖTÜ OLAN KAZANIR [RUBRIK_YAZIM §4.3]
6. KAYIT    QA/FILMLER/<FILM>.md (tek şablon) + QA/TABLO.md satırı
```

---

## 4. KLASÖR

```
QA/
├── 00_README.md          bu dosya
├── Q1_GORUNTU.md         ❶ rubrik — salt İngilizce prompt
├── Q2_ZAMAN_KESME.md     ❷
├── Q3_SANTIYE.md         ❸
├── Q4_INSA.md            ❹
├── Q5_TESLIM.md          ❺
├── TABLO.md              ⭐ TEK SAYAÇ + film × mercek tablosu (her hücre bir ham dosyaya bağlı)
├── HAM/<FILM>/           ham raporlar — dokunulmaz
├── FILMLER/<FILM>.md     film başına kayıt — künye · mercekler · olay tablosu · karar · ders
├── KOSU/<FILM>/          qa_paket.sh paketleri (yeniden üretilebilir)
└── ARSIV_12_MERCEK/      ⛔ 03.09–05.10.2026 · 12 mercek · 393 ham · DONDURULDU
                            00_ARSIV.md (özet · temizlenmiş puanlar) · 00_ESLEME.tsv (her ham → durum)
```

---

## 5. RUBRİK YAZIM KURALI

```
Rubrik dosyalarının İÇİ SALT İNGİLİZCE PROMPTTUR.
İçine YAZILMAZ: Türkçe not · tarih · film adı · ders numarası · depo yolu.
Ders GÖVDEYE KURAL olarak girer; numarası DERSLER.md'de durur.
Mimari (format değişkenleri · çapalar · kanıt kuralı · koşullu kategori · sınır cümlesi ·
çıktı biçimi): kilavuzlar/RUBRIK_YAZIM_KILAVUZU.md
```

## 6. ÜÇ AŞAMA — biri geçmek ötekini geçmiş saymaz  [C1 · 18.09.2026]

| aşama | ne denetlenir | araç | çıktı |
|---|---|---|---|
| **1 · PLAN** | prompt metni | `prompt_kontrol.py` | GO / FIX / BLOCK · üretim günlüğü §0 |
| **2 · VİDEO** | planlanan iş oluştu mu | `zincir_kontrol.sh` + beş mercek | `FILMLER/<FILM>.md` |
| **3 · YAYIN** | izleyici devam etti mi | YouTube Analytics (7. gün) | `apexait/IZLEYICI_DEFTERI.md` |

⛔ Aşama 2'nin puanı, hakemin gürültüsü ölçülmeden (kalibrasyon) filmleri SIRALAMAZ
[QA_KALIBRASYON §0].
