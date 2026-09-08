# 📐 A11 — PERSPEKTİF VE ÖLÇEK

```
AMAÇ      Ölçek tutarlılığını kurmak: referans nesneleriyle ölçeğin sahneler
          arası sabitlenmesi, perspektif kuralları, piksel-metre dönüşümü.
KARŞILIĞI ① KARE  ⛔ STATION IDENTITY 0/10 · "horizon shifts from 58% to 68%"
          ② İNŞA  SCALE LOCK düşüşleri — beş filmin beşinde yapı boyutu değişti
          DERS 38 (D_kenar vs D_eksen — mesafe hesabı yanlış)
          DERS 5  (her klip başka bina = ölçek kayması)
          DERS 6  (kamera kayması — zoom/pan)
DÖNÜŞÜ    kilavuzlar/PERSPEKTIF_VE_OLCEK_KILAVUZU.md (HENÜZ YOK — bu prompt
          onu yazdıracak) · PROMPT_SABLONU COMPOSITION bloğu · prompt_kontrol.py
KOŞU      ⛔ koşulmadı — 08.09.2026 yazıldı
```

⛔ **Kamera sabit, ama model ölçeği sahneden sahneye sürüklüyor.** KAMERA_ISTASYONU
kadraj formülünü veriyor; ölçeği TUTAN referans nesneleri sistematik değil.
Gerçek timelapse'te ölçek hiç değişmez çünkü sahne fiziksel olarak sabit.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen görüntü ölçeği, perspektif geometri ve sabit kamera fotogrametrisi üzerine çalışan bir araştırmacısın; benim ürünüm 9:16 dikey, sessiz, yapay zekâ ile üretilmiş bir inşaat timelapse filmi: 10 sahne, her sahne yaklaşık 6 saniye, kamera on sahnede aynı noktada sabit (24 mm, tilt 0°, ~40 m mesafe), ve bağımsız bir denetçi altı filmin beşinde ölçek kaydığını ölçtü — "the horizon shifts from 58% to 68% inside the same vantage group", "the building doubles in width between cuts", "SCALE LOCK 4/10" — yapı boyutu, ufuk konumu ve referans nesnelerinin piksel boyutu sahneden sahneye değişti; promptlarda kamera parametreleri sayılarla yazılıydı ama model ölçeği her karede yeniden uydurdu.

Birinci görevin: sabit kamera timelapse çekiminde ölçeğin KAYMASINl engelleyen REFERANS NESNELERİNİ — saha tipine göre (şehir içi, kırsal, kıyı, dağ, çöl/Mars) — tablo hâlinde yaz: her nesne için gerçek boyut (metre), 24 mm lens ile 40 m'den dikey kadrajdaki piksel karşılığı (1080×1920), nesnenin FİLM BOYUNCA DEĞİŞMEMESİ GEREKTİĞİ (ufuk hattı, komşu bina, ağaç, kaya, krater), ve ölçek referansı olarak kullanılabilirliği (aynı yerde, aynı boyutta, her karede görünür); ayrıca ÖLÇEĞİ değişen nesneleri (yapının kendisi, iskele, vinç, berm) referans olarak KULLANMAMA kuralını açıkla.

İkinci görevin: tilt 0° sabit kameranın perspektif geometri kurallarını — ufuk çizgisi konumu (tam %50), kaçış noktası sabitliği, yakın/uzak nesne oranı, paralaks yokluğu — ve bu kuralların bir AI üretim promptuna nasıl yazılacağını ver; özellikle "ufuk neden aynı yüzde kalmalı", "kaçış noktası ne demek ve model onu neden kaydırıyor", "atmosferik perspektif (uzaktaki nesne daha açık) nasıl yazılır" sorularını yanıtla; gerçek timelapse kamera kurulumlarından (Brinno, Enlaps, Canon EOS) alınan kadraj geometrisi verilerini kullan.

Üçüncü görevin: AI görüntü üretiminde ölçek tutarlılığını sağlamak için prompt mühendisliği tekniklerini araştır — "size anchor" (boyut çapası: bir nesneyi başka bir nesneyle karşılaştırarak tanımlama), "relative proportion" (göreceli oran: "the boulder is one third of the habitat height"), "pixel-level composition" (kadrajda nesnenin yüzde olarak yeri), "negative scale drift" (ölçek kaymasını engelleyen negatif cümleler vs pozitif çapalar) — ve her tekniğin ölçülmüş etkinliğini (varsa) yaz; ayrıca ardışık kare üretiminde (image-to-image chain) ölçek birikimli hata mekanizmasını ve bunu engelleyen yöntemleri (ControlNet depth, reference image, IP-Adapter, style transfer anchor) açıkla.

Rapor Türkçe olsun, geometri terimleri ve parametre adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] · [İDDİA] · [VARSAYIM]) ve KAYNAK SINIFI (akademik · araç dokümanı · standart/şartname · pazarlama blogu) yaz, çelişen kaynakları ikisi birden yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz; en sonda her sahne tipi için üretim promptuna doğrudan yapıştırılacak, İngilizce ve POZİTİF birer COMPOSITION ölçek cümlesi ver, örneğin "the split-top boulder to frame right spans exactly 112 pixels of frame width — one twentieth of the frame — and keeps that width from the first frame to the last; the horizon sits at exactly half the frame height throughout".

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A11_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A11-a, A11-b…
3. KILAVUZ     kilavuzlar/PERSPEKTIF_VE_OLCEK_KILAVUZU.md bu rapordan yazılır
4. KAPI        prompt_kontrol.py: COMPOSITION bloğunda ≥1 ölçek referansı + piksel
```
