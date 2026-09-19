# 📈 İzleyici Verisi ve Deney Planı — ilk 6 film

> **Tarih:** 18.09.2026
> **Kapsam:** Çapraz analizde (01-05) eksik kalan üçüncü kalite aşaması: **gerçek izleyici
> davranışı.** Teknik puanı yükseltmek faydalıdır; hangi yaratıcı tercihin izlenmeyi
> artırdığı yalnız yayın verisiyle anlaşılır (`QA/00_README.md §7 ÜÇ AŞAMA`).
> **Bağ:** `apexait/YAYIN_PLANI.md §6` (her videodan sonra kaydedilecekler · üç filmde
> aynı yönde çıkmadan kural olmaz) burada TEKRAR EDİLMEZ; bu dosya o defterin
> **deney tasarımı** tarafıdır.
> ⚠️ Bu plan ÖLÇÜLMEDİ; sahip kararı bekleyen sorular §5'te.

---

## 1. Takip edilecek göstergeler

| gözlem | sorulacak soru | sonraki deneme |
|---|---|---|
| İzlemeyi seçme oranı düşük | İlk görüntü doğru izleyiciyi durduruyor mu? | Açılıştaki SORUN ve ana eylemin okunurluğunu değiştir (MUZIK_VE_KAPAK §5) |
| Başlangıç güçlü, ortada düşüş | Tekrarlanan iş · geciken ilerleme · görüntü karmaşası? | Orta bölümdeki TEKRAR miktarını azalt (KURGU_VE_TESLIM §2.4 klip içi ilerleme) |
| Montaj anında düşüş | Fizik hatası · anlaşılmayan hareket · tempo değişimi? | QA OLAY TABLOSU ile yan yana incele (aynı zaman kodunda E-kaydı var mı) |
| Finalden önce ayrılma | Sonuç gecikti mi, erken tahmin edildi mi? | Final gösterilişini değiştir (çalışan mekanizma süresi) |
| Bir bölüm tekrar izleniyor | Tatmin edici mi, anlaması zor mu? | Görüntü ve yorumları BİRLİKTE değerlendir — eğrideki yükseliş iki şeyi de gösterebilir |

---

## 2. YouTube ölçüm notları

```
· Shorts "görüntüleme" sayımı BAŞLATMALARI ve YENİDEN OYNATMALARI kapsar;
  izlenmeyi sürdürme karşılaştırmaları için ENGAGED VIEWS ayrıca kullanılır.
· Toplam görüntüleme tek başına karar verdirmez (dağıtımın sayısıdır, filmin değil —
  YAYIN_PLANI §6.2).
· Tutma verisi 1-2 gün gecikmeyle işlenir; 7. gün karşılaştırması bu yüzden.
· Tutma eğrisindeki YÜKSELİŞ hem yeniden izleme hem anlaşılmayan bölüme dönüş olabilir —
  yorumlarla birlikte okunur.
· ⛔ Evrensel "şu yüzdeyi geçince viral olur" eşiği KULLANILMAZ; karşılaştırma yalnız
  aynı kanalın kendi film çiftleri arasında yapılır.
```

---

## 3. İlk 6 film — tek değişkenli deney dizisi

> Aynı anda konu, süre, müzik ve kapak değiştirilirse hangi tercihin işe yaradığı
> ayrılamaz. Her adımda **tek değişken** oynar; geri kalanı sabit tutulur.
> ⛔ **Sahne süresi HER adımda sabittir** (sahip kuralı — KILAVUZ_REHBERI §2.2 karşı
> kayıt); süre hiçbir adımda değişken değildir.

| adım | film | SABİT tutulan | DEĞİŞTİRİLEN |
|---|---|---|---|
| 1-2 | ilk 2 film | teknik kalite koşulları (pilot üçlü onaylı · ①②⑤ mercekleri koşulmuş) · format · sahne süresi · müzik ızgarası | **Açılış yaklaşımı:** (A) eksik parça açıkça görünür vs (B) yerleşmek üzere olan parçayla yakın sonuç |
| 3-4 | sonraki 2 film | 1-2'nin kazanan açılışı · format · süre | **Orta bölüm tekrar miktarı:** (A) her klipte ayrı iş vs (B) aynı işin ilerleyişi |
| 5-6 | sonraki 2 film | açılış + orta bölüm kazananları | **Final gösterilişi:** (A) çalışan mekanizma uzun tutuş vs (B) hızlı final kesimi |

```
KAYIT   her film için 06 tablosuna bir satır: adım · değişken (A/B) · yayın tarihi ·
        7. gün engaged views · ilk 3 sn tutma · ortalama izlenme % · düşüş zaman kodları ·
        yeniden izlenen aralık · o aralıktaki QA olay kimliği (varsa)
KARAR   bir tercih "kazandı" demek için: aynı adımın iki filminde aynı yön VE
        YAYIN_PLANI §6.2'nin üç-film kuralı (üçüncü film sonraki adımın sabitidir).
```

| film | adım | değişken | yayın | 7. gün engaged | ilk 3 sn % | ort. izlenme % | düşüş (m:ss) | yeniden izlenen | QA olay |
|---|:-:|:-:|---|---:|---:|---:|---|---|---|
| | 1 | A | | | | | | | |
| | 2 | B | | | | | | | |
| | 3 | A | | | | | | | |
| | 4 | B | | | | | | | |
| | 5 | A | | | | | | | |
| | 6 | B | | | | | | | |

---

## 4. 7. gün karşılaştırma protokolü

```
1. Aynı adımın iki filmi yan yana: tutma eğrileri üst üste (aynı x ekseni, 0-100 %).
2. Düşüş noktaları zaman koduyla yazılır; her düşüş için filmin RAPORLAR/<FILM>.md
   OLAY TABLOSU'na bakılır — o saniyede bir E-kaydı var mı?
     · VAR  → düşüş teknik (aşama 2 sorunu); yaratıcı tercihe yazılmaz
     · YOK  → düşüş yaratıcı tercihe aday; ikinci filmde de aynı yerdeyse kayda geçer
3. Engaged views ve ilk 3 sn tutma karşılaştırılır (görüntüleme sayısı değil).
4. Sonuç 06 tablosuna; kazanan tercih bir sonraki adımın SABİT sütununa geçer.
5. Üç filmde aynı yönde çıkan gözlem → YAYIN_PLANI §6.2 yoluyla kural adayı →
   kilavuzlar/DERSLER.md (kart D). O zamana kadar VARSAYIM.
```

---

## 5. Sahip kararı bekleyen sorular

```
① Deney dizisinin başlangıç tarihi — ilk 2 filmin yayın planı ne zaman? (YAYIN_PLANI §4)
② YouTube Studio Analytics erişimi var mı; tutma eğrisi ve Engaged views çekilebiliyor mu?
③ OVER_THE_WALL yeniden üretimi bu diziye dâhil mi (05 §2.3 öncelik sırası), yoksa
   dizi yeni filmlerle mi başlar?
④ Beş soru kartı yeniden üretilecek eski filmlere de uygulanır (varsayım: EVET —
   yeniden üretim de yeni prompt yazar).
```
