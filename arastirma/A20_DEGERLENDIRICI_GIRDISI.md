# 🧪 A20 — DEĞERLENDİRİCİ GİRDİSİ VE KÖRLÜK

```
AMAÇ      QA koşusuna NE girdiğini kanıtlı hâle getirmek: kör merceğe belge
          sızmasın, belge isteyen mercek belgesiz koşmasın, yanlış filmin
          belgesi ya da yanlış video yüklenmesin, tamamlanmayan koşu puan
          olarak tabloya girmesin — ve her ham rapor hangi girdilerle
          koşulduğunu ilk satırlarında taşısın.
KARŞILIĞI 06.10.2026 QA denetimi (393 ham rapor · 37 film):
          · kör mercek (① ③ ⑤ ⑦) plandan alıntı yapıyor — 6 filmde
            ("şartnamedeki akifer su aynası" · "G7" · "56,0 sn hedefi")
          · belge isteyen mercek belgesiz — en az 11 koşu; LAST LIFT ④
            plansız + kapaksız koşup final vuruşuna 10/10 verdi
          · yanlış film belgesi: STAR DOCK ⑧ ← DEEP STEP SPEC ·
            DEEP STEP ⑧ ← STONE TOWER SPEC (iki puan ortalamada)
          · POLAR HABITAT: sekiz mercek 1…21 klip saydı, ikisi "kule" anlattı
          · "RUN INCOMPLETE" raporlar puanıyla tabloya girdi
          · QA/KOSU/ hiç oluşmadı — hangi koşuya ne verildiği kayıtsız
DÖNÜŞÜ    kilavuzlar/QA_KOSU_KILAVUZU.md (✅ 06.10.2026 yazıldı) ·
          araclar/qa_paket.sh (koşu manifestosu) · QA/00_README §2-§3
          ⚠️ Sınır: A21 = değerlendiricinin ÖLÇEMEDİĞİ şey (süre, hız, kesme) ·
             burası = değerlendiriciye GİDEN şey (dosya, belge, oturum)
KOŞU      ✅ 06.10.2026 yazıldı ve koşuldu · SONUCLAR/A20_GEMINI_HAM.md · denetim A20-A24_DENETIM.md
```

⛔ **Değerlendirici Gemini sohbet arayüzünde, proje içinde koşuyor.** Proje
dosyaları ve önceki sohbetler yeni sohbete taşınıyorsa körlük arayüz düzeyinde
bozuluyor demektir; hiçbir rubrik cümlesi bunu düzeltemez.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen kör değerlendirme (blinded assessment) protokolleri, yapay zekâ değerlendirme altyapıları (LLM-as-a-judge, eval harness) ve kalite kontrol süreçlerinin girdi denetimi üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat timelapse filmleri — dikey (9:16) filmler her zaman 7 klip × 8,0 sn = 56 sn olarak üretilip 2 kat hızda (~28 sn) yayımlanıyor, yatay (16:9) filmler 12–18 klip × 8–10 sn olarak normal hızda yayımlanıyor, kamera bütün kliplerde sabit — ve her film, Gemini'nin sohbet arayüzünde bir "proje" içinde yeni sohbet açılarak, video dosyası + kare görüntüleri + (bazı rubriklerde) plan ya da şartname belgesi yüklenerek 12 ayrı İngilizce rubrikle puanlanıyor: dört rubrik bilerek BELGESİZ (kör) koşuyor ki filmi planı hiç görmemiş bir izleyici gibi okusun, diğerleri planla sözleşme denetimi yapıyor, ve koşuyu bir betik hazırlıyor (paket dosyası: girdi listesi + rubrik metni) ama yapıştırma ve yükleme elle yapılıyor.

Ölçülmüş arıza şu: 37 filmin 393 ham raporunu denetledim — kör koşması gereken rubriklerin raporları altı filmde plan belgesinin içinden alıntı yapıyor ("şartnamedeki akifer su aynası", "G7", "56,0 sn hedefi") ve bazıları "specification not supplied" diye başlayıp belge bekliyor, belge isteyen rubriklerden en az 11 koşu plan ya da şartname verilmeden yapıldı ve biri buna rağmen "final vuruşu"na 10/10 verdi, iki filmde başka bir filmin şartnamesi yüklendi ve iki puan da ortalamaya girdi, bir filmde sekiz rubriğin saydığı klip sayısı 1 ile 21 arasında değişti ve ikisi filmde olmayan bir yapıyı ("kule") anlattı — yani yanlış video yüklenmiş olabilir — "RUN INCOMPLETE" diye başlayan raporlar puanlarıyla özet tabloya girdi, ve raporların çoğunda hangi video sürümüyle, hangi belgelerle, hangi rubrik sürümüyle koşulduğu yazmıyor.

Birinci görevin: kör değerlendirmenin başka alanlarda nasıl KORUNDUĞUNU ve ihlalinin nasıl tespit edilip ele alındığını yaz — klinik araştırmalarda körlük değerlendirmesi (blinding index, unblinding kaydı, duyarlılık analizi), çift kör hakem süreci, film test gösterimleri ve kullanılabilirlik testleri — ve bunu sohbet tabanlı büyük dil modellerine uygula: Gemini sohbet arayüzünde "proje"/Gem dosyalarının, "saved info"/kişisel bağlam ve hafıza özelliklerinin ve aynı projedeki önceki sohbetlerin yeni bir sohbete taşınıp taşınmadığını, hangi ayarla ya da hangi kullanım biçimiyle (geçici sohbet, proje dışı sohbet, API ile durumsuz çağrı) tam yalıtım sağlandığını belgelenmiş kaynaklarla ve tarihli sürüm bilgisiyle yaz; kör bir değerlendiricinin belge görüp görmediğini raporun METNİNDEN tespit etmenin yollarını (sızıntı kelime listesi, kanarya terimleri — yalnız belgede geçen uydurma bir ad — ve benzeri) ölçülmüş örneklerle sırala.

İkinci görevin: olgun değerlendirme altyapılarının (OpenAI Evals, EleutherAI lm-evaluation-harness, Stanford HELM, UK AISI Inspect, MLflow/W&B değerlendirme kayıtları) ve yayın/film teslim QC süreçlerinin her koşu için hangi girdileri KAYDETTİĞİNİ yaz — dosya özeti (SHA-256), model adı ve sürümü, arayüz mü API mi, örnekleme parametreleri, prompt/rubrik sürümü, yüklenen belgelerin adı ve başlığı, tarih — ve koşudan ÖNCE değerlendiricinin doğru dosyayı gördüğünü doğrulatmanın yollarını (modelden dosya adını, süreyi, ilk ve son karenin kısa betimini, belge başlığını ilk satırda geri okumasını istemek ve bunu makine ölçümüyle karşılaştırmak) ve bu doğrulamanın ne kadar güvenilir olduğunu belgelenmiş verilerle anlat; yanlış girdi tespit edilince uygulanan "fail closed" kurallarını (koşma · koşuyu iptal et · puanı bağlayıcı sayma) karşılaştır.

Üçüncü görevin: eksik ya da bozuk koşunun ele alınışını yaz — ölçüm biliminde ve klinik veri yönetiminde eksik veri politikası (0 ya da tavan puanla doldurmamak, "incomplete" durumunun ortalamadan çıkarılması, yeniden koşu sayısı ve hangi koşunun geçerli sayılacağı), ve sohbet arayüzü yerine API ile durumsuz, betikle tekrarlanabilir koşunun (Gemini API: Files API ile video yükleme, sistem talimatı, sıcaklık, yapılandırılmış çıktı) körlük, girdi kaydı ve maliyet açısından artısını ve eksisini ölçülmüş örneklerle tablo hâlinde ver; az kişili, veritabanı olmayan, git + markdown ile çalışan bir ekip için en küçük uygulanabilir düzeni öner.

Rapor Türkçe olsun, araç, parametre ve ölçüt adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, ölçüm ya da resmi belge var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · araç/platform dokümanı · bağımsız karşılaştırma · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI ya da belge adı + bölüm + tarih; arayüz davranışı için tarihli sürüm notu — kaynağı gösterilemeyen iddia ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) her ham raporun ilk satırlarına yapıştırılacak İngilizce bir KOŞU MANİFESTOSU şablonu (film, video dosya adı + SHA-256 + süre + çözünürlük + oynatma hızı, yüklenen belgeler ve ilk satır başlıkları, rubrik adı ve sürümü, model ve arayüz, yeni/geçici sohbet mi, tarih, modelin geri okuduğu dosya adı ve süre) ve (b) koşudan önce ve sonra işaretlenecek en fazla 12 maddelik bir ÖN UÇUŞ / SON UÇUŞ kontrol listesi ver — her madde için ihlalde yapılacak tek eylemi (KOŞMA · TEKRAR KOŞ · PUANI BAĞLAYICI SAYMA) yaz.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A20_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A20-a, A20-b…
3. KILAVUZ     kilavuzlar/QA_KOSU_KILAVUZU.md bu rapordan yazılır
4. KAPI        qa_paket.sh: paket başına KOŞU MANİFESTOSU · ham rapor manifestosuz
               ya da sızıntı kelimesi taşıyorsa puan tabloya GİRMEZ
```
