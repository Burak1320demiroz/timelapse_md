# 📊 QA Çapraz Analiz Dizin Rehberi

> **Oluşturulma Tarihi:** 18.09.2026  
> **Kapsam:** `QA/HAM_RAPORLAR/` altında yer alan 15 dikey shorts filminin 132 adet ham QA raporunun (130 puanlı + 2 INC) çapraz analizi.  
> **Amaç:** Sistem genelinde en çok tekrarlanan hataları, en düşük alınan mercek puanlarını tespit etmek, kılavuzlardaki boşlukları haritalandırmak ve yapım/denetim kalitesini artıracak önlemleri ve aksiyon planını sunmak.

---

## 📂 Dizin İçeriği

| Dosya | Başlık | Açıklama |
|---|---|---|
| [`01_SKOR_MATRISI.md`](file:///Users/dai/github/apex_md/timelapse_md/QA/QA_CAPRAZ_ANALIZ/01_SKOR_MATRISI.md) | 15 Film × 12 Mercek Tam Skor Matrisi | Tüm filmlerin 12 mercekteki ortalama puanları, veri eksikliği durumları ve ham rapor sayıları. |
| [`02_EN_DUSUK_PUANLAR.md`](file:///Users/dai/github/apex_md/timelapse_md/QA/QA_CAPRAZ_ANALIZ/02_EN_DUSUK_PUANLAR.md) | Mercek Bazlı Başarısızlık ve Puan Sıralaması | Merceklerin ortalama puan sıralaması, 0-3 puan arası çöküş bölgeleri ve istatistiksel dağılım. |
| [`03_ARIZA_KALIPLARI.md`](file:///Users/dai/github/apex_md/timelapse_md/QA/QA_CAPRAZ_ANALIZ/03_ARIZA_KALIPLARI.md) | En Çok Tekrarlanan TOP 10 Hata Kalıbı | Filmler genelinde tespit edilen 10 kronik arıza kalıbı, etkilenen filmler ve ham rapordan kanıt alıntıları. |
| [`04_KILAVUZ_BOSLUK_HARITASI.md`](file:///Users/dai/github/apex_md/timelapse_md/QA/QA_CAPRAZ_ANALIZ/04_KILAVUZ_BOSLUK_HARITASI.md) | Kılavuz İhlalleri ve Kural Boşlukları | Mevcut `kilavuzlar/` dosyalarındaki hangi kuralların delindiği, hangi alanlarda hiç kural olmadığı ve zafiyet nedenleri. |
| [`05_NIHAI_RAPOR.md`](file:///Users/dai/github/apex_md/timelapse_md/QA/QA_CAPRAZ_ANALIZ/05_NIHAI_RAPOR.md) | Yönetici Özeti ve Önlem Tablosu | Çapraz analizin sentezi, on arıza için revize önlem tablosu, vazgeçilen öneriler, film bazlı müdahale sırası, ölçülecek pilot hedef. |
| [`06_IZLEYICI_DENEY_PLANI.md`](file:///Users/dai/github/apex_md/timelapse_md/QA/QA_CAPRAZ_ANALIZ/06_IZLEYICI_DENEY_PLANI.md) | İzleyici Verisi ve Deney Planı | Üçüncü kalite aşaması: takip göstergeleri, YouTube ölçüm notları, ilk 6 film için tek değişkenli deney dizisi, 7. gün protokolü. |

---

## 🔍 Temel Analiz Özet Verileri

- **Analiz Edilen Film Sayısı:** 15 Film
- **İncelenen Toplam Ham Rapor:** 132 Dosya (130 puanlı + 2 INC) — 15 filmin 12 mercekte tekrar okunmasıdır, 132 bağımsız deney değildir
- **Ortalama Puanı En Düşük Mercek:** **② İNŞA (3.83/10)** — Filmlerin %60,0'ı (9/15) 4.0 altı puan aldı.
- **En Kritik İkinci Mercek:** **⑧ YÖNTEM (4.25/10)** — 3 filmde tam sıfır (0.0/10) puan alındı.
- **En Kritik Üçüncü Mercek:** **⑩ SEBEP (4.24/10)** — Evaluated 5 filmin 4'ünde nedensellik "MAGIC" gerekçesiyle çöktü.
- **Puanı En Yüksek Mercekler:** **⑪ ENVANTER (8.42/10)** ve **⑨ FAALİYET (7.67/10)**

---

## ⚠️ Önemli Not
Bu dizindeki dokümanlar **analiz ve raporlama** amacı taşır. İlk sürüm (18.09.2026) kılavuz ve betiklere dokunmamıştı; aynı gün dış değerlendirmeyle düzeltilen sayılar ve `05_NIHAI_RAPOR.md` §2'deki revize önlem tablosu **uygulandı** — hangi kılavuz/betiğin değiştiği `kilavuzlar/DERSLER.md` ÇAPRAZ ANALİZ bölümünde (C1-a…h) kayıtlıdır. Buradaki her sayı `python3 araclar/capraz_sayim.py` çıktısıyla karşılaştırılır; elle yazılan sayı yanılır (ilk sürümde 138 yazıldı, matris 132 veriyordu).
