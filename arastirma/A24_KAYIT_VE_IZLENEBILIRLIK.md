# 🗂️ A24 — KAYIT VE İZLENEBİLİRLİK

```
AMAÇ      QA kaydını tek kaynaktan türetmek: ham rapor kanıttır, özet
          tablolar ondan ÜRETİLİR, elle tutulmaz; film ve koşu için durum
          modeli; adlandırma şeması; iki yönlü yetim kontrolü.
KARŞILIĞI 06.10.2026 QA denetimi:
          · INDEX 5 filme "ÜRETİLMEDİ" diyor — her birinin 8-12 ham raporu
            haftalardır depoda (BEFORE NIGHTFALL · OLD ROAD · ONE MORE TURN ·
            SWALLOWED BUS · TIDE GATE)
          · STONE DRAGON "12 mercek" — 3 dosya başka şey (ikinci ④ · iki puansız denetim)
          · THE CROSSING ④ ⑤ ⑥ puanlı, ham dosyası yok
          · 4 adlandırma şeması · README ile qa_paket.sh farklı şema söylüyor
          · aynı puan 3 yerde (T tablosu · matris · film raporu), durum etiketleri tutmuyor
          · sayac.sh "tutarlı" diyor — yalnız toplam film sayısını karşılaştırıyor
          · 20.09 sonrası ~16 film raporunda KARAR ve DERS bölümü yok
DÖNÜŞÜ    kilavuzlar/QA_KAYIT_KILAVUZU.md (✅ 06.10.2026 yazıldı) · araclar/sayac.sh ·
          QA/ARSIV_12_MERCEK/00_INDEX.md · QA/ARSIV_12_MERCEK/HAM_RAPORLAR/00_README.md · QA/ARSIV_12_MERCEK/RAPORLAR/00_README.md
          ⚠️ Sınır: A20 = koşu ANINDA neyin kaydedileceği (manifesto) ·
             burası = kayıtların birbirine nasıl BAĞLANDIĞI ve özetin nasıl türetildiği
KOŞU      ✅ 06.10.2026 yazıldı ve koşuldu · SONUCLAR/A24_GEMINI_HAM.md · denetim A20-A24_DENETIM.md
```

⛔ **00_INDEX "projedeki tek sayaç" diyor ama elle yazılıyor.** Elle tutulan
bir özet ile ham kanıt arasındaki her fark bir gün yanlış karar demektir; bu
denetimde beş film, üç puan ve bir "12 mercek" iddiası öyle çıktı.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen araştırma verisi yönetimi, deney/değerlendirme kaydı (experiment tracking, data lineage) ve prodüksiyon takip sistemleri üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat timelapse filmleri ve küçük bir ekip olarak her şeyi bir git deposunda markdown dosyalarıyla, veritabanı olmadan tutuyoruz: her film için bir plan klasörü, her filmin her değerlendirme koşusu için bir "ham rapor" dosyası (12 rubrik × yaklaşık 45 film; şimdiye kadar 393 dosya, model çıktısı olduğu gibi, dokunulmaz), her film için ajanın işlediği bir özet rapor, rubrik başına bir puan tablosu, ve bütün filmlerin durumunu ve puanlarını gösteren, ELLE güncellenen 1000 satırlık bir ana dizin; bir sayaç betiği ana dizini dosya sistemiyle karşılaştırıyor.

Ölçülmüş arıza şu: ana dizin beş filme "üretilmedi" diyor ama her birinin 8–12 ham değerlendirme raporu haftalardır depoda duruyor ve bunların puanları hiçbir özete girmemiş, bir film "12 rubrikle tam ölçüldü" diye kayıtlı ama 12 dosyasından üçü başka şey (biri başka bir rubriğin ikinci koşusu, ikisi puansız serbest denetim ve birbiriyle çelişiyor), başka bir filmin üç puanının arkasında ham dosya yok, ham dosyalar dört ayrı adlandırma şemasıyla duruyor ve klasör açıklaması ile koşu betiği iki farklı şema söylüyor, aynı puan üç ayrı yerde (rubrik tablosu, ana dizin matrisi, film raporu) tutuluyor ve "tekrarlanacak / bağlayıcı değil" gibi durum etiketleri bu üç yerde birbirini tutmuyor, sayaç betiği "dizin tutarlı" diyor ama yalnız toplam film sayısını karşılaştırıyor, ve yeni film raporlarının yarısında karar ve ders bölümleri eksik — yani özet kayıt kanıttan koptu ve kimse fark etmedi.

Birinci görevin: "tek doğruluk kaynağı" ve veri soy ağacı (data lineage) uygulamalarını yaz — deney takip araçlarının (MLflow, Weights & Biases, DVC), değerlendirme kayıtlarının ve klinik araştırma veri yönetiminin (ALCOA+ ilkeleri, denetim izi / audit trail) ham kanıtı nasıl değiştirilemez tuttuğunu, özet tabloları ham kayıttan nasıl OTOMATİK türettiğini ve elle düzenlenen özetin neden ve nasıl yasaklandığını anlat; sonra bunu veritabanı olmadan git + markdown ile çalışan küçük bir ekibe indir: her ham dosyanın başına konacak yapılandırılmış üst bilgi (YAML front matter), içerik özeti (hash) ile dosya kimliği, özetin bir betikle yeniden üretilmesi ve git ön-commit kancasıyla (pre-commit hook) denetlenmesi — belgelenmiş küçük ölçekli örneklerle ve artı/eksi tablosuyla.

İkinci görevin: DURUM MODELİNİ yaz — bir film (planlandı → üretildi → ölçüldü → yayımlandı → izleyici verisi geldi) ve bir değerlendirme koşusu (tam · tamamlanmadı · yanlış girdi · yerine yenisi geçti · bağlayıcı değil) için hangi durumların tanımlandığını, geçişlerin neyle tetiklendiğini ve bayat durumun (stale state) nasıl önlendiğini görsel efekt/animasyon prodüksiyon takip sistemleri (ShotGrid, ftrack), yayın teslim QC iş akışları ve klinik veri yönetimi örnekleriyle karşılaştır; "kanıt var, kayıt yok" ve "kayıt var, kanıt yok" yetimlerini iki yönde yakalayan uzlaştırma (reconciliation) kontrollerinin nasıl tasarlandığını belgelenmiş örneklerle anlat.

Üçüncü görevin: adlandırma ve sürümleme kurallarını yaz — dosya adı şeması tasarımı (sabit alan sırası, sıfır dolgulu numara, ayırıcı, büyük/küçük harf), değerlendirme rubriğinin sürümlenmesi ve her koşunun hangi rubrik sürümüyle yapıldığının bağlanması, bir koşunun yerine yenisi geçtiğinde eskisinin silinmeden "superseded" işaretlenmesi, ve bunların bir lint betiğiyle otomatik denetlenmesi — ve bu kuralları mevcut karışık bir arşive GERİYE DÖNÜK uygularken ham dosyaya dokunmadan (yeniden adlandırma mı, eşleme tablosu mu) nasıl göç edileceğini belgelenmiş göç örnekleriyle öner.

Rapor Türkçe olsun, araç ve kavram adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] belge, standart ya da ölçülmüş vaka var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · standart/düzenleyici belge · araç dokümanı · bağımsız vaka · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI ya da belge adı + bölüm; kaynağı gösterilemeyen iddia ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) bir ham rapor için ve bir film durum dosyası için YAML üst bilgi şeması (alan adı · tür · zorunlu mu · örnek değer), (b) her biri tek cümlelik geçti/kaldı tanımıyla en fazla 12 maddelik bir UZLAŞTIRMA KONTROLLERİ listesi (yetim ham rapor, kanıtsız puan, durum çelişkisi, şema dışı ad, eski rubrik sürümü vb.) ve (c) ana dizinin puan matrisini ham dosyaların üst bilgisinden yeniden üreten kısa bir Python iskeleti ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A24_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A24-a, A24-b…
3. KILAVUZ     kilavuzlar/QA_KAYIT_KILAVUZU.md bu rapordan yazılır
4. KAPI        sayac.sh uzlaştırma kontrolleriyle genişler · 00_INDEX matrisi
               betikten üretilir · ham dosyalara DOKUNULMAZ (eşleme tablosu)
```
