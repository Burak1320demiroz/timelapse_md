# 🧪 A40 — KÜMÜLATİF DEVAMLILIK VE DURUM KİLİTLEMESİ (COMMITTED STATE LOCKING)

```
AMAÇ      Ardışık I2V keyframe zincirinde üretilen zaman atlamalı filmlerde, önceki sahnelerde
          tamamlanan yapı elemanlarının (ör. bitirilen %25'lik çatı segmenti veya dökülen beton tabliye)
          sonraki sahnelerde doku değiştirmesini, titremesini, yeniden sıfırdan yapılmaya başlanmasını
          veya yer değiştirmesini engellemek; tamamlanan her aşamayı kalıcı/donmuş durum ("COMMITTED /
          FROZEN STATE") olarak sabitleyip yeni eylemi yalnızca ilave artışa (incremental delta ΔC)
          odaklayan durum yönetim mimarisini kurmak.
KARŞILIĞI Saha ölçümleri ve keyframe zinciri arızaları:
          · Klip 1'de tamamlanan çatı makasları ve aşıkları, Klip 2 başladığında model tarafından
            sabit bir zemin olarak algılanmayıp yeni bir renge bürünmekte, cıvata hatları kaymakta
            veya vinç daha önce bitmiş bölgeye tekrar müdahale etmektedir.
          · Tamamlanmış bölge ile yeni montaj bölgesi arasındaki sınır çizgisinde (assembly seam)
            sürekli dokusal kırpışma (texture flicker) ve geometrik uyumsuzluk yaşanmaktadır.
DÖNÜŞÜ    kilavuzlar/INSAAT_YONTEMI_KILAVUZU.md §Kümülatif Durum ·
          kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §Durum Kilidi ·
          PROMPT_SABLONU §Committed Geometry Block
KOŞU      Henüz koşulmadı · derin araştırma botuna yapıştırılacak
```

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, tam metin

Sen üretken yapay zekâ (video diffusion models, Image-to-Video - I2V), zamansal nesne sürekliliği (temporal object persistence, autoregressive video generation) ve mimari durum makineleri (architectural state machines, incremental scene graph) üzerine çalışan kıdemli bir araştırmacısın; benim ürünüm konuşmasız, sabit kilitli kamerada (tripod locked, zero pan/tilt) iki anahtar kare zinciriyle (two-keyframe I2V pipeline; Klip N'in son karesi Klip N+1'in ilk karesidir) üretilen profesyonel inşaat timelapse filmleridir.

Açık problem ve üretim arızası şudur:
Bir yapının inşası sahneler boyunca kümülatif olarak ilerlemek zorundadır. Örneğin Sahne 1'de çatının güney aksındaki ilk 4 çelik aşığı monte edilmiş ve sabitlenmiştir. Sahne 2'ye geçildiğinde hedef, bu bitmiş 4 aşığa dokunmadan sonraki 4 aşığı (5'ten 8'e kadar) monte etmektir. Ancak video difüzyon modelleri kümülatif bir "durum hafızasına" (stateful memory) sahip değildir. Sahne 2'nin I2V üretimi sırasında model:
1. Sahne 1'de bitirilmiş olan güney aksındaki çelik aşıkları donmuş/kalıcı bir yapı olarak koruyamamakta; aşıkların rengini, dokusunu, flanş kalınlıklarını ve aralıklarını değiştirmekte (structural drift / feature mutation),
2. Yeni sahnedeki montaj fiilini ("workers installing steel purlins") daha önce bitmiş olan ilk 4 aşığın üzerine de yayarak orayı tekrar sökmekte ya da sanki hiç yapılmamış gibi yeniden inşa etmeye çalışmakta (re-assembly conflict),
3. Tamamlanan imalat ile yeni başlayan imalatın kesişim arakesitinde (committed vs active boundary) yüksek frekanslı bir yırtılma ve geometri erimesi üretmektedir.

Birinci görevin: Video difüzyon transformatörlerinde (DiT mimarileri, MMDiT, Wan2.1, HunyuanVideo, CogVideoX, LTX-Video) kümülatif durum korunamamasının teorik ve matematiksel kök nedenini açıkla.
- Otoregresif olmayan veya ardışık pencereli I2V modelleri neden önceki klipten gelen pikselleri "kesin kilitli/değiştirilemez mimari gerçeklik" olarak algılayamaz?
- Denoising adımlarında metin kodlayıcının (T5/Qwen) genel eylem fiilleri, daha önce tamamlanmış görsel özellikleri (completed features) neden latent uzayda çözerek (unbinding) yeniden şekillendirmeye çalışır?

İkinci görevin: Çok sahneli ardışık video üretiminde tamamlanmış elemanları dondurup yalnızca yeni ilave artışı (incremental delta $\Delta C$) aktif tutan yöntemleri (Latent Freezing, KV-Cache Persistence, Segment-wise Latent Inpainting, Incremental ControlNet Depth Anchoring, State-Machine Prompting) 2024–2026 literatürü üzerinden karşılaştır.
- Önceki sahneden devralınan tamamlanmış piksellerin latent uzayda gradyan güncellemesinden muaf tutulması (zero-drift anchoring) nasıl sağlanır?
- Açık kaynak ve kurumsal modellerde "Committed / Frozen State" ile "Active Assembly Front" sınırını kusursuz korumanın pratik mühendislik çözümleri nelerdir?

Üçüncü görevin: Yalnızca metin yönlendirmesi (positive prompt), negatif prompt ve anahtar kareler kullanılarak uygulanabilecek bir **KÜMÜLATİF DURUM VE İLAVE ARTIŞ SÖZDİZİMİ (Cumulative State & Incremental Delta Syntax)** tasarla.
- Prompt metninde daha önce bitmiş elemanları "tamamen dondurulmuş, dokunulmaz, imalatı bitmiş referans yapı" (`COMMITTED BASELINE: STRICTLY UNTOUCHED`), yeni yapılacak elemanları ise "yegâne aktif montaj cephesi" (`ACTIVE INSTALLATION FRONT ONLY`) olarak ayıran standart İngilizce sözdizimi nasıl kurulur?
- Modelin daha önce yapılmış kısımlara el sürmesini, oradaki dokuları değiştirmesini ve yeniden montaj yapmasını %100 yasaklayan negatif kalkan ve pozitif kilit kalıpları nelerdir?

Rapor Türkçe olsun, yapay zekâ, bilgisayarlı görü ve inşaat terminolojisi İngilizce kalsın; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] akademik deney, benchmark veya resmi doküman · [İDDİA] literatürde iddia edilmiş kanıtlanmamış · [VARSAYIM] çıkarım), KAYNAK SINIFI (akademik makale/arXiv · platform/araç teknik dokümanı · endüstriyel vaka analizi) ve ÇÖZÜMLENEBİLİR KAYNAK (DOI, arXiv ID, URL, tarihli sürüm notu) ekle. Raporun sonunda:
(a) Bir KÜMÜLATİF DURUM VE MONTAJ CEPHESİ TABLOSU (İnşaat fazı · Donmuş baz elemanlar · Aktif imalat cephesi · Yasaklı yeniden montaj tipi),
(b) Standart İngilizce KÜMÜLATİF DURUM KİLİTLEME ŞABLONU (Committed State & Delta Lock Block),
(c) En fazla 10 maddelik bir SAHNELER ARASI DEVAMLILIK VE DURUM KONTROL LİSTESİ (Checklist) ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A40_<BOT>_HAM.md
2. DENETİM     SONUCLAR/A39-A42_DENETIM.md
3. KOD         VARSAYIMLAR.md A40 serisi
4. KILAVUZ     kilavuzlar/INSAAT_YONTEMI_KILAVUZU.md §Kümülatif Durum &
               kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §Durum Kilidi
5. KAPI        prompt_kontrol.py: kümülatif durum ve aktif cephe ayrımı denetimi
```
