# 🧪 A36 — SEMANTİK SIZMA VE SÖZLÜK KARANTİNASI

```
AMAÇ      Metin kodlayıcıların (CLIP / T5 / DiT cross-attention) mimari ve teknik terimleri
          yorumlamasındaki anlam kaymalarını, eşanlamlı kelime çatışmalarını ve kavramsal
          sızmaları (attribute binding / semantic leakage) engellemek; "tek eleman = tek sözlük"
          ve "kavramsal kalkan" kurallarını ölçülebilir kılmak.
KARŞILIĞI 15.10.2026 THE SKY STATION Bölüm 1 ölçümleri:
          · DERS 80: Çatı için "truss", "rafter", "timber framing" ve "standing seam" terimleri
            farklı sahnelerde karışık yazılınca, model çatıyı 3 kez mutasyona uğrattı: enine çelik
            makaslar → boyuna ahşap mertekler → 4 sivri piramit çatı → tek beşik çatı (3:38.0–3:51.0).
          · DERS 68: "Spoked bullwheel" terimi vinç kancasında taşınırken model çarkı kemerden
            geçirip yamulttu ve kanyona fırlattı (havada rotasyonel geometri kaybı · 2:24.0–3:03.0).
          · DERS 77: Sağ alt köşedeki doğal sivri kaya kütlesi (rock pinnacle) model tarafından "platform / kaide"
            olarak okunup üzerine devasa ölçek dışı tek bir insan figürü yerleştirildi (1:49.0).
          · DERS 83: Prompt içine yazılan müzik enstrümanları (guitar, orchestral) difüzyon modeli
            tarafından 8 saniyelik kopuk ham ses patlamalarına dönüştürüldü (0:16.0–4:08.0).
DÖNÜŞÜ    kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §3 ·
          INSAAT_YONTEMI_KILAVUZU §Sözlük · araclar/prompt_kontrol.py yasaklı eşanlamlılar
KOŞU      Henüz koşulmadı · derin araştırma botuna yapıştırılacak
```

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, tam metin

Sen üretken yapay zekâ metin-video modellerinde metin kodlayıcılar (Text Encoders: CLIP ViT-L/14, T5-XXL, Llama-3 tabanlı multimodal encoder'lar), çapraz dikkat bağlama mekanizmaları (cross-attention attribute binding / leakage) ve mimari görsel ontoloji üzerine uzmanlaşmış kıdemli bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — kamera tek ve sabit, her kesme zamanı atlar ve her sahne iki anahtar kare arasında üretilir (I2V keyframe zinciri).

Ölçülmüş arıza ve açık sorun şu: Yapay zekâ video modelleri mimari ve inşaat terimlerinde aşırı "anlamsal gevşeklik" ve "semantik kirlenme" göstermektedir:
1. Tekil bir çatı strüktürünü tarif ederken ardışık sahne promptlarında "truss", "rafter", "timber frame", "pitched roof", "decking" gibi birbirine yakın teknik terimler kullanıldığında, model her kesmede tamamen farklı bir strüktürel tipoloji üretmektedir. THE SKY STATION filminde çatı sadece 13 saniye içinde (3:38.0–3:51.0) iki enine çelik kafes makastan boyuna ahşap merteklere, ardından dört adet sivri piramidal köşke ve en sonunda düz beşik çatıya dönüşerek geometrik mutasyon geçirmiştir (DERS 80).
2. Açık seyir peronu için "cantilevered platform / deck" denilirken, çatı tahtaları için "roof decking" denmesi modelin bu iki terimi çapraz bağlamasına (cross-binding) ve peronun üstüne çatı örmesine yol açmaktadır.
3. Kadraj köşesindeki çıplak kaya sivrisi (rock pinnacle / cliff horn) modelce "heykel kaidesi / seyir kulesi" gibi yorumlanarak üzerine devasa tek bir insan figürü dikilmektedir (DERS 77).
4. Prompt metninde yer alan atmosferik/işitsel kelimeler ("acoustic guitar enters", "orchestral sound"), video modelinin işitsel latent uzayında kesintisiz fon müziği üretmek yerine sahnenin içine gömülen 8 saniyelik kopuk parazit seslere dönüşmektedir (DERS 83).

Birinci görevin: Büyük multimodal ve video difüzyon modellerinde (DiT, Stable Video Diffusion, Gen-3, Sora mimarisi, Wan2.1 vb.) metin kodlayıcıların (CLIP ve T5) mimari ve teknik terminolojiyi nasıl ayrıştırdığını açıkla — "Attribute Binding Failure" (özelliklerin yanlış nesneye bağlanması) ve "Semantic Bleed" (anlamsal sızma) olayının latent uzaydaki ve cross-attention katmanlarındaki matematiksel mekanizması nedir? Neden "truss" kelimesi piramit biçimlerini tetiklerken, "deck" kelimesi zemin ile çatı kaplamasını birbirine karıştırmaktadır?

İkinci görevin: Kontrollü Mimari Sözlük (Controlled Architectural Vocabulary) ve Kavramsal İzolasyon stratejilerini belgelenmiş araştırmalarla derle — inşaat ve timelapse süreçlerinde modelin mutasyona uğramasını engelleyen en katı, en hatasız İngilizce mimari terim eşleştirmeleri nelerdir? (Örnek: "Gable roof rafters" vs "Trusses" vs "Pergola"; "Cast concrete slab" vs "Timber deck"). Hangi kelimeler "yüksek sızma riskli (high-bleed tokens)" kabul edilmeli ve negatif prompt kalkanlarıyla bastırılmalıdır?

Üçüncü görevin: Görsel ve I2V promptları için "Semantik Bağlama ve Tipoloji Kilidi Sözdizimi" formüle et — modelin aynı elemanı farklı sahnelerde tek bir geometride dondurmasını garanti eden prompt kalıpları nelerdir? Metin dışı modalitelerin (örneğin müziğin veya atmosferik seslerin) video promptundan tamamen arındırılarak sadece diegetik çevresel seslere (ambient site sounds) sınırlandırılmasının video kalitesine ve görsel tutarlılığa ölçülmüş etkisi nedir?

Rapor Türkçe olsun, teknik terimler İngilizce kalsın; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] akademik makale veya benchmark · [İDDİA] doğrulanmamış literatür iddiası · [VARSAYIM] senin analizin), KAYNAK SINIFI (akademik · teknik doküman · benchmark) ve ÇÖZÜMLENEBİLİR KAYNAK (arXiv ID, DOI, teknik rapor başlığı) yaz. Raporun sonunda:
(a) YÜKSEK SIZMA RİSKLİ MİMARİ TERİMLER VE GÜVENLİ KARŞILIKLARI TABLOSU (Tehlikeli Terim · Neden Mutasyon Doğurur · Güvenli Kilit İfadesi),
(b) Çatı, döşeme, iskele ve mekanik parçalar için standart İNGİLİZCE TİPOLOJİ KİLİDİ ŞABLONU,
(c) En fazla 10 maddelik SEMANTİK SIZMA VE SÖZLÜK DENETİM LİSTESİ ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A36_<BOT>_HAM.md
2. DENETİM     SONUCLAR/A35-A38_DENETIM.md
3. KOD         VARSAYIMLAR.md A36 serisi
4. KILAVUZ     kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §3
5. KAPI        prompt_kontrol.py: yüksek sızma riskli mimari kelime taraması
```
