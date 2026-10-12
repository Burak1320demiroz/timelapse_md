# 🧪 A29 — ONARIM VE YENİDEN ÜRETİM (QA bulgusundan klip onarımına)

```
AMAÇ      QA'nın verdiği her hükümden (mercek · kategori · saniye) DOĞRU onarım eylemine giden yazılı
          bir yol kurmak: aynı iki kareden yeniden koşmak mı, kareyi düzenlemek mi, klibi ara kareyle
          bölmek mi, promptu yeniden yazmak mı, bölgeyi düzeltmek mi, sahneyi değiştirmek mi — zinciri
          ve komşu klipleri bozmadan, yeniden çekim bütçesiyle, sürüm kaydıyla.
KARŞILIĞI arşiv (393 ham rapor · 37 film) + beş mercekli QA (06.10.2026):
          · öldürücü hükümler var (❶ SEPARATE IMAGES · ❸ REBUILT · ❹ DIFFERENT) ve ❹ "THE FIRST PIECE THAT
            APPEARED — o klip yeniden üretilir" diyor; ama NASIL yeniden üretileceği yazılı değil
          · yeniden koşu listesi hazır (00_ARSIV §6: pilot 3 film + 11 film) — onarım yordamı yok
          · ölçülmüş tekrar eden kusurlar: THE MOUNTAIN DOOR aracın ön ayarı push-in yaptı, zincir tutmadı
            (1,63) · THE IRON BRIDGE taşkın klibinde yapı sıfırlandı · THE STONE DRAGON moloz yığını üç dikişte
            sıfırlandı (REBUILT) · THE DEEP STEP kubbeler tek karede bitmiş belirdi (MOTION FOCUS başka işi
            anlatıyordu) · BACK TO WATER camlar montajsız belirdi · kart başka dünya (5 film)
          · zincirli formatta bir kareyi değiştirmek İKİ klibi birden etkiler (G(n) hem S(n−1)'in sonu hem
            S(n)'in başı) — komşu dikişin bozulma riski ölçülmedi
DÖNÜŞÜ    kilavuzlar/ONARIM_VE_YENIDEN_URETIM_KILAVUZU.md (✅ 07.10.2026 yazıldı) · URETIM_GUNLUGU §5 sapma
          şablonu · QA_KAYIT (_K2 sürüm adı) ile sınır · AGENTS kart R (rapor geldi) sonrasına "onarım" adımı
          ⚠️ Sınır: A7 araç profili, A8 kurgu ve teslim idi; burası QA'DAN SONRA düzeltme
KOŞU      ✅ 07.10.2026 yazıldı ve koşuldu · SONUCLAR/A29_GEMINI_HAM.md · denetim A25-A29_DENETIM.md
```

⛔ **Format çapraz geçişi (dissolve/fade) yasaklar** ve her kesme bir karedir. Rapor "kusuru bir
crossfade ile gizleyin" derse bu format için geçersizdir — rapor bunu kendisi söylemeli.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen film/VFX post-prodüksiyonu (shot triage, cleanup, pickup shot kararları, teslim QC), yayın kalite kontrolü ve yapay zekâ video üretiminde düzenleme/onarım iş akışları (yeniden üretim, video inpainting, keyframe düzenleme, kare enterpolasyonu) üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — kamera tek ve sabit, dikey filmler 7 klip × 8 sn, yatay filmler 12–48 klip × 8–10 sn, ve her klip İKİ sabit görüntü arasında üretilir: önce filmin son karesi üretilir, sonra bütün kareler ondan geriye doğru image-to-image türetilir, sonra her klip kendi iki karesine (ilk ve son kare) kilitli olarak bir image-to-video aracıyla üretilir, böylece bir klibin son karesi bir sonrakinin ilk karesidir ve kurgu bu karelerde kesilir; çapraz geçiş (dissolve/fade) yasaktır — ve bitmiş her film Gemini üzerinde beş ayrı İngilizce rubrikle (üçü planı görmeden kör, ikisi planla) puanlanır, rubrikler kusuru saniyesiyle ve bazen "öldürücü" bir hükümle verir: "ayrı görüntüler" (kamera ya da dünya değişti), "her çekimde yeniden kurulmuş" (sahadaki nesneler dikişte sıfırlanıyor), "farklı yapı" (yapının kimliği değişti), "eleman yöntemsiz belirdi", "final duruyor".

Ölçülmüş durum şu: 37 filmin 393 ham raporu var ve yeniden koşulacak filmlerin listesi hazır, ama bir rapor "0:17,5'te üç kubbe tek karede bitmiş belirdi" ya da "0:51'de taşkın klibinde kemer silindi ve 0:55'te sıfırdan kuruldu" dediğinde hangi eylemin doğru olduğunu söyleyen yazılı bir yolum yok; geçmiş arızalarda kök neden bazen aracın kendisiydi (ön ayar bir kamera yakınlaşması ekledi ve zincir tutmadı), bazen prompttu (klibin hareket paragrafı o klipte beliren en büyük elemanı değil başka bir işi anlatıyordu), bazen keyframe'di (sahadaki moloz yığını üç dikişte farklı çizilmişti), bazen kurguydu (teslim süresi plandan saptı, final yanlış saniyeye düştü); ve zincirli formatta bir kareyi düzeltmek İKİ klibi birden etkiler, çünkü o kare bir klibin sonu ve bir sonrakinin başıdır — onarımın komşu dikişleri bozup bozmadığını nasıl ölçeceğimi, kaç denemeden sonra sahneyi yeniden tasarlamam gerektiğini ve her sürümü git + markdown ile nasıl kaydedeceğimi bilmiyorum.

Birinci görevin: profesyonel post-prodüksiyon ve QC pratiğini belgelenmiş kaynaklarla yaz — shot triage (postta düzelt mi, yeniden çek mi; karar ölçütleri), cleanup/paint-out, stabilizasyon, retime, pickup shot kararı, kusurların ciddiyet sınıfları ve her sınıfın standart çaresi (yayın ve yayın platformu teslim QC şartnamelerinde — ör. akış platformlarının teslim/QC belgeleri, EBU/SMPTE QC önerileri — kusur sınıflandırması), bir düzeltmenin komşu çekimlerde gerileme (regression) yaratmadığını doğrulama pratikleri ve düzeltme sürümlerinin adlandırma/sürümleme alışkanlıkları — her iddianın etiketiyle.

İkinci görevin: yapay zekâ videosuna özgü onarım yöntemlerini 2025–2026 tarihli araç dokümanları ve ölçülmüş araştırmalarla karşılaştır — aynı iki kareden farklı tohumla yeniden koşmanın sonuç varyansı, bir keyframe'i düzenleyip ona bağlı iki klibi birlikte yeniden koşmak, bir klibi araya yeni bir keyframe koyarak iki zincirli klibe bölmek, video inpainting/bölge düzenleme ve video-to-video özelliklerinin (ticari araçların tarihli sürümleri) zincirli formatta riski, kare enterpolasyonu (RIFE/FILM benzeri) ile küçük boşluk köprüleme, ve onarımı doğrulamak için zamansal tutarlılık ölçüleri (dikişte SSIM/LPIPS, öznitelik eşleme, warping error, CLIP/DINO benzerliği) — hangi yöntem hangi kusur sınıfında ölçülmüş olarak işe yarıyor, hangisi yalnız iddia.

Üçüncü görevin: bir KARAR AĞACI kur — değerlendirici hükmünden (kusur sınıfı · saniye · klip) kök neden sınıfına (araç · prompt · keyframe · kurgu · plan) ve oradan tek bir onarım eylemine; gerilemeyi önleme protokolü (onarılan klibin iki komşu dikişinde otomatik ve elle karşılaştırma, yalnız etkilenen rubrikleri mi bütün QA'yı mı yeniden koşmak, hangi koşunun geçerli sayılacağı), yeniden çekim bütçesi ve durma kuralı (kaç başarısız denemeden sonra sahne yeniden tasarlanır ya da plan değişir), her eylemin tahmini maliyet ve süresi, ve veritabanı olmayan, git + markdown ile çalışan küçük bir ekip için en küçük sürüm kaydı düzeni (dosya adı şeması, dosya özeti, üretim günlüğüne satır).

Rapor Türkçe olsun, araç, yöntem ve metrik adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, ölçüm ya da resmi belge var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · araç/platform dokümanı · bağımsız karşılaştırma · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI ya da belge adı + bölüm + tarih; araç davranışı için tarihli sürüm notu — kaynağı gösterilemeyen iddia ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) bir ONARIM MATRİSİ (satırlar: kamera hareketi · yapının erimesi/şekil değiştirmesi · elemanın yöntemsiz belirmesi · yapının dikişte gerilemesi · sahadaki nesnelerin dikişte sıfırlanması · ışık/gölge sıçraması · okunur yazı/logo · net insan yüzü · boş/park hâlinde saha · finalin erken durması · su kotu sıçraması · ikinci kamerada başka dünya · teslim süresinin plandan sapması; sütunlar: aynı karelerden yeniden koş · keyframe düzenle · klibi böl · promptu yeniden yaz · bölge düzelt · sahneyi değiştir — her hücrede beklenen başarı, maliyet ve etiket), (b) onarılan her klip için bir DİKİŞ GÜVENLİĞİ protokolü, (c) bir SÜRÜM KAYDI şablonu ve (d) en fazla 12 maddelik bir kontrol listesi ver — her madde için ihlalde yapılacak tek eylem (YENİDEN KOŞ · KOMŞUYU DA YENİLE · SAHNEYİ YENİDEN TASARLA).

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A29_<BOT>_HAM.md — dokunulmadan [kart S]
2. DENETİM     SONUCLAR/A25-A29_DENETIM.md — araç sürümleri ve metrik atıfları çekilir
3. KOD         VARSAYIMLAR.md · kuşak bölümüne (+ DİZİN satırı)  A29-a, A29-b…
4. KILAVUZ     kilavuzlar/ONARIM_VE_YENIDEN_URETIM_KILAVUZU.md bu rapordan yazılır
5. KAPI        AGENTS kart R → "onarım" adımı · URETIM_GUNLUGU §5 sürüm satırı (_K2) ·
               onarılan klibin iki dikişinde zincir_kontrol zorunlu
```
