# 🌤️ A12 — HAVA VE ATMOSFER

```
AMAÇ      Atmosferik gerçekçiliği kurmak: bulut, sis, toz, yağış, rüzgar
          etkisinin klip İÇİ davranışı — nasıl hareket eder, ne hızda, hangi yöne.
KARŞILIĞI ③ ZAMAN ⛔ CLOUD AND SKY düşüşleri · TIME RATE 0/10 (iki filmde)
          DERS 15 (gök hızlı, yer yavaş — iki ayrı saat)
          DERS 18 (I2V'de yazılmazsa gök donuyor)
          DERS 14 (mevsim taşıyıcısı olmayan sahne zamanı durduruyor)
          DERS 26 (mevsim üretilmedi — sonbahar hiç çıkmadı)
          DERS 40 (gölgesiz klip = zamanın tek taşıyıcısı yok)
DÖNÜŞÜ    kilavuzlar/HAVA_VE_ATMOSFER_KILAVUZU.md (HENÜZ YOK — bu prompt onu
          yazdıracak) · PROMPT_SABLONU TIME RATE ve LIGHTING blokları ·
          prompt_kontrol.py
KOŞU      ⛔ koşulmadı — 08.09.2026 yazıldı
```

⛔ **ZAMAN_VE_ISIK güneşi tarif ediyor, gökyüzünü tarif etmiyor.** Model
gökyüzünü ayrı, yeri ayrı hızlandırıyor [DERS 15] çünkü atmosfer fiziği
prompt düzeyinde hiç yazılmadı. Bulut tipi, hareket yönü, sıkıştırma oranına
göre görünüm hiçbir kılavuzda yok.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen atmosfer fiziği, bulut dinamiği ve gerçek (optik) timelapse sinematografisi üzerine çalışan bir araştırmacısın; benim ürünüm 9:16 dikey, sessiz, yapay zekâ ile üretilmiş bir inşaat timelapse filmi: 10 sahne, her sahne yaklaşık 6 saniye, kamera on sahnede aynı noktada sabit (24 mm, tilt 0°, ~40 m mesafe), ve bağımsız bir denetçi altı filmin altısında atmosfer gerçekliğini düşük ölçtü — "clouds race across the sky while workers move at real-time speed" (③ TIME RATE 0/10), "the sky is frozen while machines crawl" (③ SUN DIRECTION 0/10), "no cloud movement at all in five clips" — model gökyüzünü ayrı, yeri ayrı hızlandırdı veya gökyüzünü tamamen dondurdu; promptlarımda güneş açısı ve gölge yönü sayılarla yazılıydı ama bulut tipi, hareket yönü, sıkıştırma oranına göre görünüm ve atmosferik derinlik hiç tarif edilmemişti.

Birinci görevin: gerçek timelapse çekimlerinde sıkıştırma oranına göre (100× = ~10 dk, 1200× = ~2 saat, 5400× = ~9 saat) gökyüzü ve atmosfer olaylarının GÖRSEL İMZASINI tablo hâlinde yaz — bulut tipi başına (cumulus, stratus, cirrus, cumulonimbus, altostratus) hareket hızı (m/s ve kadraj geçiş süresi), şekil değişimi, gölge etkisi, renk tonu; ve her oran × bulut tipi kombinasyonu için 6 saniyelik bir klipte bulutun ekranda NE KADAR yol aldığını, kadrajın yüzde kaçını kapladığını, ne şekilde uzadığını (şerit, akış, silinme) belgelenmiş çekim verileriyle ver; Mars/Ay atmosfersiz veya ince atmosferli sahalarda bunun karşılığını (toz duvarı, regolith plume, yıldız izi yokluğu) ayrıca yaz.

İkinci görevin: atmosferik perspektif (aerial perspective) ve derinlik ipuçlarını — uzaktaki nesnenin renk kayması (mavi kayma / Rayleigh saçılımı), pus yoğunluğu, kontrast düşüşü, detay kaybı — mesafe bandına göre (0-50 m, 50-200 m, 200-1000 m, ufuk) tablo hâlinde yaz; farklı hava koşullarında (açık, bulutlu, sisli, tozlu, yağmurlu, karlı) bu değerlerin nasıl değiştiğini ver; Mars'ta ters durumu açıkla (CO₂ atmosferi, Rayleigh saçılımının kızıl uçta yoğunlaşması, mavi gün batımı); ve her koşul için prompt düzeyinde yazılacak İngilizce bir atmosferik derinlik cümlesi öner.

Üçüncü görevin: yağış ve rüzgar etkisinin klip içi zaman damgasını — yağmur başlarken yüzeylerin ıslanma sırası ve süresi (saniye), kar birikiminin hızı (cm/saat ve kadrajda piksel/saniye), rüzgarın zemin nesnelerine etkisi (bayrak, tente, toz bulutu, yaprak), ıslak yüzeyin kuruma süresi — tablo hâlinde ve ölçülmüş verilerle yaz; özellikle "yağış bir sahnede BAŞLARSA ne olur" ve "yağış bir sahnede BİTERSE ne kalır" (birikinti, ıslak leke, erime çamuru) sorularını yanıtla; bunların mevsim taşıyıcısı olarak kullanılabilirliğini ve gölge olmadan zamanın geçtiğini kanıtlayan alternatif taşıyıcıları (pus hareketi, toz duvarı, ıslak-kuru sınır, yapay ışık gölgesi, beton kürlenme tonu) sırala.

Rapor Türkçe olsun, meteoroloji ve fizik terimleri İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] · [İDDİA] · [VARSAYIM]) ve KAYNAK SINIFI (akademik · araç dokümanı · sinematografi kaynağı · pazarlama blogu) yaz, çelişen kaynakları ikisi birden yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz; en sonda her atmosfer durumu için üretim promptuna doğrudan yapıştırılacak, İngilizce ve POZİTİF birer TIME RATE + LIGHTING atmosfer cümlesi ver, örneğin "clouds cross the full width of the frame from left to right in about four seconds, stretching into long horizontal streaks as they go; the shadow of the split-top boulder sweeps thirty degrees across the plain; the sky grades from deep blue at the zenith to pale white above the horizon".

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A12_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A12-a, A12-b…
3. KILAVUZ     kilavuzlar/HAVA_VE_ATMOSFER_KILAVUZU.md bu rapordan yazılır
4. KAPI        prompt_kontrol.py: I2V promptunda atmosfer/gök hareketi cümlesi zorunlu
```
