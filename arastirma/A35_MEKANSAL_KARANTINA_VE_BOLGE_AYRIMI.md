# 🧪 A35 — MEKÂNSAL KARANTİNA VE BÖLGE AYRIMI

```
AMAÇ      Aynı kadrajda birden fazla yapım odağı veya derinlik katmanı olduğunda
          (ör. ön konsol güverte, orta plan ana bina, derin arka plan harabesi),
          metindeki eylemlerin ve ekipmanların yanlış bölgelere sıçramasını (attention bleed)
          engellemek; kadrajı bağımsız karantina kutularına (zone quarantine) bölme
          kurallarını ve prompt sözdizimini ölçülebilir kılmak.
KARŞILIĞI 15.10.2026 THE SKY STATION Bölüm 1 (35 klip · 4:40.0) ölçümleri:
          · DERS 65: Karşı yamaçtaki istasyonun çatı restorasyonu metne girince, model
            ön plandaki tamamen açık seyir terasına (boarding deck) ahşap kırma çatı ve pergola ördü (4:34.0 · Clip 35).
          · DERS 66: Derin arka plandaki (140 m uzakta) mini harabe istasyona eylem yazılınca,
            model yapının kendi çatısından devasa bir vinç bomu fışkırttı (0:40.0 · Clip 6).
DÖNÜŞÜ    kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §1 & §2 ·
          PROMPT_SABLONU §Bölge Kalkanı · araclar/prompt_kontrol.py çoklu bölge denetimi
KOŞU      Henüz koşulmadı · derin araştırma botuna yapıştırılacak
```

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, tam metin

Sen üretken yapay zekâ (video diffusion models, text-to-video, image-to-video), uzamsal dikkat mekanizmaları (spatial attention, cross-attention control, regional prompting) ve bilgisayarlı görü (multi-region scene decomposition, layout-guided generation) üzerine çalışan kıdemli bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — kamera bütün film boyunca tek ve kilitli (tilt 0, hiç kıpırdamaz, tripod/ankraj sabit), her kesme yalnızca zamanı atlar ve her klip İKİ sabit görsel anahtar kare arasında üretilir (I2V / iki keyframe zinciri; bir klibin son karesi sonraki klibin ilk karesidir).

Ölçülmüş arıza ve açık sorun şu: Dağ kanyonunda restore edilen bir teleferik istasyonunu çektiğimiz 12 dakikalık (16:9, 90 sahne) filmimizin ilk 35 sahnesinde, kadrajda birden fazla fiziksel odak noktası bulunmaktadır: (1) Ön plan sağda vadiye uzanan konsol açık beton teras (boarding deck), (2) Orta planda 5 kemerli ana taş istasyon binası, (3) Derin arka planda (kanyonun karşı yamacında, 140 m uzakta) ikinci bir harabe istasyon. Model metindeki eylemleri bu bölgelere izole edememekte ve ağır "semantik sızma / eylem sıçraması (semantic bleed / attention leakage)" yaşamaktadır:
1. Karşı kıyıdaki harabenin çatısının sökümü ve onarımı prompta yazıldığında, model uzaktaki mini şantiyeyi ayrı çizemeyip harabenin taş çatısından imkânsız bir dev vinç bomu çıkartmış (0:40.0 · Clip 6) ve çapa yapısını bozmuştur.
2. Karşı istasyonun çatısı tamamlanırken, model bu "çatı yapımı" eylemini ön plandaki tamamen çatısız, açık korkuluklu seyir peronuna sıçratmış ve açık güverteye kendiliğinden ahşap kırma çatı ve pergola örüp sonra geri eritmiştir (4:34.0 · Clip 35).
3. Metindeki tek bir eylem fiili (ör. "crane lifts roof trusses"), kadrajdaki tüm açık yüzeyleri potansiyel montaj alanı olarak algılamaktadır.

Birinci görevin: Çok odaklı ve derinlikli sahnelerde üretken modellerin (T2V, I2V, Diffusion Transformers — DiT) uzamsal dikkat dağılımını (spatial cross-attention distribution) ve eylem sıçraması mekanizmasını açıkla — metindeki bir nesne/eylem token'ının ilgisiz mekânsal koordinatlara (image patches) sızmasının teorik ve mimari kök nedeni nedir? (Cross-attention map leakage, position embedding zayıflığı, self-attention'da nesne ayrıştırma kaybı). Modelin bir sahnede aynı anda başarıyla izole edebileceği maksimum bağımsız eylem odağı sayısı (focal regions / bounding zones) literatürde nedir?

İkinci görevin: Çok bölgeli difüzyon ve mekânsal karantina tekniklerini (Regional Prompting, MultiDiffusion, Mixture of Diffusers, Layout-to-Video, Bounding Box Attention Masking) 2024–2026 güncel literatürü ve ticari araç yetenekleri üzerinden karşılaştır — her bölgeye bağımsız prompt/negatif atama yöntemleri, dikkat pencerelerinin (attention masks) ayrıştırılması, katmanlı kompozitleme (layered foreground/midground/background generation) ve ardışık I2V zincirinde bu bölgelerin kilitli tutulması nasıl sağlanır? Ticari API'larda veya açık kaynak modellerde (Wan2.1, HunyuanVideo, CogVideoX, LTX-Video, Runway, Pika) mekânsal kısıtlama (spatial conditioning) için kanıtlanmış yöntemler nelerdir?

Üçüncü görevin: Prompt seviyesinde uygulanabilir bir "Bölge Karantinası (Zone Quarantine) Sözdizimi ve Kalkanı" tasarla — harici bir maske yazılımı olmadan, yalnızca text prompt, I2V son karesi ve negatif prompt kullanılarak kadrajın bölgelere ayrılması nasıl formüle edilir? (Örnek: COORDINATE BOUNDING [x1, y1, x2, y2], ZONE A / ZONE B açık etiketleme, RELATIVE DEPTH anchoring, "ZONE IMMUNITY / UNTOUCHED REGION" kuralı). Ön plandaki açık bir platformun metindeki diğer çatı eylemlerinden etkilenmesini %100 engelleyecek kesin prompt kalıpları nelerdir?

Rapor Türkçe olsun, yapay zekâ, bilgisayarlı görü ve difüzyon terimleri İngilizce kalsın; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] akademik deney, benchmark veya resmi doküman · [İDDİA] literatürde iddia edilmiş kanıtlanmamış · [VARSAYIM] çıkarım), KAYNAK SINIFI (akademik makale/arXiv · platform/araç teknik dokümanı · endüstriyel vaka analizi) ve ÇÖZÜMLENEBİLİR KAYNAK (DOI, arXiv ID, URL, tarihli sürüm notu) ekle. Raporun sonunda:
(a) Bir MEKÂNSAL BÖLGE KARANTİNA TABLOSU (Kadraj katmanları · İzin verilen maksimum eylem · Yasak eylemler · Sızma risk puanı),
(b) İki veya daha fazla odaklı sahneler için standart İngilizce PROMPT BÖLGE KALKANI ŞABLONU (Zone Isolation Block),
(c) En fazla 10 maddelik bir BÖLGE İZOLASYON KONTROL LİSTESİ (Checklist) ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A35_<BOT>_HAM.md
2. DENETİM     SONUCLAR/A35-A38_DENETIM.md
3. KOD         VARSAYIMLAR.md A35 serisi
4. KILAVUZ     kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §1 & §2
5. KAPI        prompt_kontrol.py: çoklu odak tespiti ve bölge kalkanı zorunluluğu
```
