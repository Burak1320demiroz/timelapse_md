# 🧪 A34 — YENİ KANAL BÜYÜMESİ 2026: STOK, KADANS VE İLK 90 GÜN

```
AMAÇ      Sıfır aboneli yeni bir kanalın 2026'da bu nişte nasıl kırıldığını belgeye bağlamak: kadans ve
          tutarlılığın gerçek etkisi, soğuk başlangıç, Shorts → uzun form hunisi, 37 filmlik stokun sırası
          ve hızı, tek bir filmi ne zaman yargılayacağımız ve formatı ne zaman sorgulayacağımız —
          ve bunlardan bir 90 günlük açılış takvimi ile karar eşikleri.
KARŞILIĞI kanal belgeleri (07.10.2026):
          · YAYIN_PLANI §1 kadans 1 dikey/hafta + 1 uzun/ay (ağır hat) · §2 iki ayak · §4 açılış bloğu
            (3 dikey film aynı gün) · §6.2 üç film kuralı
          · POLITIKA_VE_RISK §5.1: Shorts YPP yolu (10 M / 90 gün) gerçekçi değil → abone Shorts'tan,
            izlenme saati uzun formdan — karar ölçülmedi
          · 37 film üretildi ve QA'landı (46 plan) · 0 yayın · IZLEYICI_DEFTERI boş
          · A23-d: QA ↔ izleyici ilişkisi için 29–30 film gerekir — stok bunu karşılar ama yayın hızı belirler
          · uzun form artık İKİ tür: yapım günlüğü (8–15 dk) + yatay filmler (2–8 dk) — YAYIN_PLANI §2
            yalnız ilkini tarif ediyor
          · ⚠️ YAYIN_PLANI §4 "müzik aracı lisans satırı" — dikeyde müzik yok kuralından (21.09.2026) önce yazıldı
DÖNÜŞÜ    apexait/YAYIN_PLANI.md §1 · §2 · §4 · §6 · §7 oynatma listeleri · CAPRAZ_YAYIN §4 ·
          IZLEYICI_DEFTERI (karar eşikleri)
          ⚠️ Sınır: A25 tek bir uzun filmin yapısı ve okunmasıydı; burası KANALIN büyümesi ve yayın sırası
KOŞU      ✅ 07.10.2026 yazıldı ve koşuldu · SONUCLAR/A34_GEMINI_HAM.md · denetim A30-A34_DENETIM.md
```

⛔ **Kadansı artırma kararı bir metrikten doğar, hevesten değil** [YAYIN_PLANI §1]. Rapor "günde bir
video" derse bu, prompt kapısını ve usta kare kapısını bozan bir öneridir — kanıtı ayrıca sorulur.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen yeni ve küçük video kanallarının büyümesi (soğuk başlangıç, yükleme sıklığı, seri formatlar, kısa formdan uzun forma geçiş, çok platformlu yayın) üzerine platform belgelerini ve bağımsız analizleri tarihleriyle takip eden bir araştırmacısın; benim ürünüm konuşmasız, anlatıcısız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — kamera bütün filmde tek ve sabit, her kesme yalnızca zamanı atlar; dikey (9:16) filmler 7 klip × 8 sn olarak üretilip 2 kat hızda (~28 sn) YouTube Shorts, TikTok ve Instagram Reels'e aynı gün ve aynı dosyayla yükleniyor, yatay (16:9) filmler 2–8 dakika olarak YouTube'a gidiyor, ayda bir de filmin nasıl kurulduğunu gösteren 8–15 dakikalık bir yapım günlüğü planlıyorum; paketleme İngilizce, her videoda yapay zekâ beyanı açık ve her filmin üretimi (plan, kareler, klipler, kurgu, kalite denetimi) yaklaşık bir hafta sürüyor.

Durumum şu: üretim hattım ağır olduğu için yayın planım haftada bir dikey film ve ayda bir uzun video; elimde üretilmiş ve bir yapay zekâ değerlendiricisiyle puanlanmış 37 film var ama hiçbiri yayımlanmadı ve kanalın sıfır abonesi var; YouTube Partner Programı'nın iki yolunu hesapladım (1.000 abone + 12 ayda 4.000 saat uzun form izlenmesi ya da 1.000 abone + 90 günde 10 milyon geçerli Shorts görüntülemesi) ve Shorts yolunu haftada bir filmle gerçekçi bulmadım, bu yüzden aboneyi Shorts'tan, izlenme saatini uzun formdan bekliyorum; bir gözlemi ancak üç ayrı filmde aynı yönde çıkarsa kural sayıyorum — ama yeni bir kanalın ilk 90 gününde ne beklemesi gerektiğini, eldeki 37 filmi hangi sırayla ve hangi hızla yayımlamam gerektiğini, tek bir filmi kaçıncı günde ve kaç görüntülemeyle değerlendirebileceğimi ve formatı ne zaman sorgulamam gerektiğini bilmiyorum.

Birinci görevin: KANITI topla — platformların 2024–2026 resmi açıklamaları (yükleme sıklığının ve tutarlılığın öneriye etkisi var mı, yeni kanalın soğuk başlangıcı nasıl işler, Shorts izleyicisinin uzun videoya geçişi ve Shorts'tan uzun videoya bağlantı özelliği, Shorts'tan gelen abonenin uzun formu izleyip izlemediği), büyük örneklemli bağımsız analizler (yükleme sıklığı ile büyüme, ilk kırılmaya kadar geçen süre ve video sayısı — örneklem büyüklüğü, dönem ve yöntemiyle) ve 2025–2026'da büyüyen yapay zekâ / timelapse / süreç kanallarının belgelenmiş zaman çizelgeleri (tarih, sayı, kaynak) — pazarlama iddialarını ve "algoritma sırrı" anlatılarını ayrı tutarak.

İkinci görevin: STOK VE SERİYİ yaz — 37 filmlik birikimin yayın sırası (en iyiler önce mi, karışık mı, konu dönüşümlü mü), hızı (toplu yükleme mi, haftalık mı) ve riskleri (kısa sürede çok yüklemenin spam ya da "şablon içerik" sinyali yaratıp yaratmadığı, düşük performanslı bir videoyu silip yeniden yüklemenin kurallara ve kanala etkisi), seri adlandırma ve oynatma listeleri, profil ızgarasının bütünlüğü (bütün kapaklar filmin son karesinden), sabitlenmiş yorum, uzun formun kısa videoları ve kısa videoların uzun formu beslemesi, ve üç platform arasında yayın aralığı — her öneride resmi kuralı, ölçülmüş veriyi ve iddiayı ayırarak.

Üçüncü görevin: bir KARAR PROTOKOLÜ yaz — küçük bir kanalda tek bir filmi yargılamadan önce gereken en az veri (gün sayısı ve görüntüleme), gürültüyü ayırma yolları (kanal içi kıyas, medyan, kayan pencere, aynı anda tek değişken), erken metriklerden hangilerinin sonraki büyümeyi öngördüğü (ölçülmüşse), aşama hedefleri (ilk 10 video · ilk 1.000 abone · Partner Programı) ve formatın bir değişkenini ne zaman değiştirmek, ne zaman durup yeniden düşünmek gerektiği — kanıt yoksa eşiği [VARSAYIM] diye işaretleyerek.

Rapor Türkçe olsun, platform özellik ve metrik adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, ölçüm ya da resmi belge var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (platform dokümanı · platform temsilcisinin kamuya açık açıklaması · bağımsız analiz · vaka · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL + belge adı + bölüm + tarih; vaka için kanalın kendi açıkladığı sayı ve tarihi — kaynağı gösterilemeyen iddia ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) bir 90 GÜNLÜK AÇILIŞ TAKVİMİ (hafta · platform · film türü · amaç metriği · karar noktası — 37 filmlik stok ve haftada bir yeni film varsayımıyla), (b) bir KARAR EŞİKLERİ tablosu (metrik · eşik · kaynak/etiket · eylem — kaynağı yoksa BİLİNMİYOR), (c) bir SERİ VE IZGARA KARTI (seri adı · oynatma listesi · kapak düzeni · sabitlenmiş yorum · uzun forma bağlantı) ve (d) en fazla 12 maddelik bir haftalık kontrol listesi ver — her madde için ihlalde yapılacak tek eylem (YÜKLE · ERTELE · FORMATI SORGULA).

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A34_<BOT>_HAM.md — dokunulmadan [kart S]
2. DENETİM     SONUCLAR/A30-A34_DENETIM.md — platform açıklamaları kaynağından çekilir · vaka sayıları
               kanalın kendi açıklamasıyla karşılaştırılır · takvim stok sayısıyla (37) aritmetik sınanır
3. KOD         DERSLER.md · DEVRALINAN bölümüne  A34-a, A34-b…
4. KILAVUZ     YAYIN_PLANI §1 (kadans) · §2 (iki tür uzun form) · §4 (açılış bloğu + 90 gün takvimi) ·
               §6 (karar eşikleri) · §7 (seri ve oynatma listeleri)
5. KAPI        kadans değişikliği ve stok sırası SAHİP KARARIDIR — ajan önerir, takvimi sahip onaylar
```
