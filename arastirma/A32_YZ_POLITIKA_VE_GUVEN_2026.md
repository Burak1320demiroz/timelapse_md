# 🧪 A32 — YAPAY ZEKÂ İÇERİĞİ 2026: POLİTİKA, ETİKET VE İZLEYİCİ GÜVENİ

```
AMAÇ      Yapay zekâ ile üretilmiş bir timelapse kanalının 2026'da var olma koşullarını tarihli belgeye
          bağlamak: para kazanma ve özgünlük politikaları nasıl UYGULANIYOR, beyan ve etiket kuralları
          neler, etiket ve "AI slop" tepkisi izleyici güvenini ve paylaşımı nasıl etkiliyor, ve bizim
          şablonlu üretim hattımız "özgün değer" kanıtını nasıl gösterir.
KARŞILIĞI kanal belgeleri (07.10.2026):
          · POLITIKA_VE_RISK §1.2: format kartı, YouTube "inauthentic content" (07/2025) politikasının
            "şablon" tanımının birebir karşılığı · §1.3 ilaç üç katman — ölçülmedi, hiç yayın yok
          · §5: yapay zekâ beyanı para kazanmayı etkilemez (30.08.2026 doğrulandı) · A1-d: risk beyansızlıkta
          · CAPRAZ_YAYIN §2: C2PA verisi silinmez → TikTok bu veriyle otomatik etiketler (bildirilen)
          · 11/2025 TikTok izleyiciye yapay zekâ içeriğini azaltma kaydırıcısı verdi — dağıtım artık
            izleyicinin tercihine de bağlı [doğrulandı 07.10.2026 · TechCrunch 18.11.2025]
          · kanal adında "AI" (KANAL_KIMLIGI §1) — yapısal beyan; etkisi ölçülmedi
          · hiç uyarı, para kazanma reddi ya da itiraz deneyimi yok — kriz kartları (§6) sınanmadı
DÖNÜŞÜ    apexait/youtube/POLITIKA_VE_RISK.md §1 · §2 · §5 · §6 · CAPRAZ_YAYIN §2 ·
          tiktok/instagram HESAP_KIMLIGI · KANAL_KIMLIGI §2–§4 (tez · izleyici)
          ⚠️ Sınır: A1-d beyanın erişim cezası olup olmadığını sordu (2025); burası 2026 UYGULAMASI,
             izleyici güveni ve itiraz kanıtı
KOŞU      ✅ 07.10.2026 yazıldı ve koşuldu · SONUCLAR/A32_GEMINI_HAM.md · denetim A30-A34_DENETIM.md
```

⛔ **Politika ÖZETİ politika değildir.** Rapor her kural için birebir alıntı + URL + tarih vermeli;
"YouTube AI içeriği cezalandırıyor" türü cümle kaynak göstermiyorsa [İDDİA]'dır. Rapor hukuki tavsiye değildir.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen platform içerik politikaları (para kazanma, özgünlük, sentetik medya beyanı), içerik kaynağı standartları (C2PA, görünmez filigran) ve yapay zekâ ile üretilmiş içeriğe izleyici tepkisi üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, anlatıcısız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — kamera bütün filmde tek ve sabit, her kesme yalnızca zamanı atlar; dikey (9:16) filmler 7 klip × 8 sn olarak üretilip 2 kat hızda (~28 sn) YouTube Shorts, TikTok ve Instagram Reels'e aynı gün ve aynı dosyayla yükleniyor, yatay (16:9) filmler 2–8 dakika olarak YouTube'a gidiyor, ayda bir de filmin nasıl kurulduğunu (plan, reddedilen kareler, modelin bozduğu yapılar) gösteren uzun bir yapım günlüğü planlıyorum; paketleme İngilizce, her videoda yapay zekâ beyanı açık, dosyadaki içerik kimliği (C2PA) verisi silinmiyor ve kanal adında "AI" geçiyor.

Bildiğim şu: YouTube Temmuz 2025'te "repetitious content" politikasını "inauthentic content" olarak yeniden adlandırdı ve seri hâlinde, şablonla, videodan videoya çok az değişen, ölçekte çoğaltılabilir içeriği para kazanmanın dışında tuttu; benim üretim sistemim tanım gereği bir şablon (her filmde aynı klip sayısı ve süresi, aynı sabit kamera, aynı açılış düzeni, aynı negatif prompt çekirdeği, haftada bir film) ama her filmin konusu, yapısı ve "bedeli" (yapının neye karşılık yükseldiği: bir kış, bir sel, sökülen eski bir yapı) farklı; Ağustos 2026'da kontrol ettiğimde YouTube'un yapay zekâ beyanı ("altered or synthetic content") para kazanmayı etkilemiyordu, TikTok Kasım 2025'te izleyiciye yapay zekâ içeriğini azaltma kaydırıcısı verdi — ama bu politikaların 2026'da nasıl UYGULANDIĞINI, hangi kanalların neden para kazanmadan çıkarıldığını, etiketin izleyici güvenini ve paylaşımı nasıl etkilediğini ve "AI slop" tepkisinin hangi içeriği vurup hangisini vurmadığını bilmiyorum.

Birinci görevin: POLİTİKA METİNLERİNİ tarihleriyle topla — YouTube Partner Programı'nın "inauthentic content" ve "reused content" kuralları ile 2025–2026 güncellemeleri, "altered or synthetic content" beyanının ne zaman zorunlu olduğu, etiketin oynatıcıda mı açıklamada mı göründüğü ve beyan edilmemesinin sonucu; TikTok'un yapay zekâ içeriği (AIGC) kuralları, C2PA ve görünmez filigranla otomatik etiketleme, Creator Rewards Program'ın yapay zekâ içeriğine yaklaşımı ve Kasım 2025 kaydırıcısının nasıl çalıştığı; Meta/Instagram'ın yapay zekâ bilgi etiketi ve 2025–2026 özgünlük/yeniden yükleme kuralları ile para kazanma etkisi — her biri birebir alıntı, URL ve tarihle; ayrıca güvenilir basında belgelenmiş uygulama vakalarını (hangi kanal türü, ne zaman, gerekçe, itiraz sonucu) söylentiden ayırarak yaz.

İkinci görevin: İZLEYİCİ TEPKİSİNİ ölçülmüş kanıtla yaz — 2024–2026 akademik çalışmalar ve bağımsız anketlerde yapay zekâ etiketinin ve beyanın algılanan güvenilirlik, beğeni, paylaşma niyeti ve izleme davranışı üzerindeki etkisi (örneklem, ülke, içerik türü, etki büyüklüğü), izleyicinin bir içeriği "AI slop" diye reddetmesini tetikleyen özellikler (aldatma, fizik dışı hareket, seri üretim izi, insan emeği görünmemesi) ile kabul görmesini sağlayanlar (açıklık, görünür zanaat ve süreç, tutarlılık, merak/fayda), "bu gerçek mi" yorumlarının yayılmaya ve kanal itibarına etkisi ve 2025'ten 2026'ya tutumun yönü — ölçülmüş olanı yorumdan ayır.

Üçüncü görevin: SAVUNMAYI yaz — politika metinlerinin ve itiraz rehberlerinin "özgün değer" ya da "anlamlı insan katkısı" olarak neyi saydığı, filmin nasıl kurulduğunu gösteren aylık bir yapım günlüğünün bir kanal incelemesinde işe yarayıp yaramadığı (belge ya da belgelenmiş vaka var mı), itiraz için hangi kanıtların saklanması gerektiği (plan, promptlar, reddedilen kareler, kurgu projesi, sürüm kaydı) ve bir seriyi format kimliğini kaybetmeden "şablon" hükmünden uzak tutmanın yolları — her öneriyi kanıt düzeyiyle ve kanıt yoksa [VARSAYIM] diye işaretleyerek.

Rapor Türkçe olsun, politika, özellik ve standart adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, ölçüm ya da resmi belge var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · platform politika belgesi · güvenilir basın · bağımsız anket · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL + belge adı + bölüm + tarih; politika için yürürlük ya da güncelleme tarihi — kaynağı gösterilemeyen iddia ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) POLİTİKA TABLOSU (platform · kural · birebir alıntı · URL · tarih · neyin tetiklediği · sonucu), (b) bir RİSK MATRİSİ (satırlar: sabit kamera · her filmde eşit klip sayısı ve süresi · aynı açılış düzeni · aynı negatif çekirdek · haftalık kadans · kanal adında "AI" · müziksiz ortam sesi · açık yapay zekâ beyanı · aynı dosyanın üç platforma yüklenmesi; sütunlar: para kazanmadan çıkarılma · dağıtımın kısılması · zorunlu etiket · izleyici tepkisi — her hücrede olasılık, kanıt ve etiket), (c) platform başına bir BEYAN KARTI (beyan nerede açılır · etiket nasıl görünür · yanıltıcı olmayan İngilizce açıklama cümlesi önerisi) ve (d) en fazla 12 maddelik bir kontrol listesi ver — her madde için ihlalde yapılacak tek eylem (YÜKLE · BEYANI DÜZELT · SERİYİ FARKLILAŞTIR).

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A32_<BOT>_HAM.md — dokunulmadan [kart S]
2. DENETİM     SONUCLAR/A30-A34_DENETIM.md — her politika alıntısı resmi sayfadan birebir çekilir;
               vaka haberleri en az iki bağımsız kaynakla · akademik etki büyüklükleri makaleden
3. KOD         VARSAYIMLAR.md · kuşak bölümüne (+ DİZİN satırı)  A32-a, A32-b…
4. KILAVUZ     POLITIKA_VE_RISK §1 (uygulama) · §2 (beyan kartları) · §5 DIŞ SAYILAR (tarihli) · §6 kriz
               kartları (itiraz kanıt listesi) · CAPRAZ_YAYIN §2
5. KAPI        risk matrisinde "yüksek" çıkan satır sahibe karar olarak sunulur — ajan format değiştirmez
```
