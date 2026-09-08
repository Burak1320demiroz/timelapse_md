# 🧰 A7 — ARAÇ PROFİLİ

```
AMAÇ      Üretim aracının ÖLÇÜLMÜŞ davranışını karta bağlamak: klip süresi,
          negatif alanı, koşullu özne sızması, kamera kilidi, gölge davranışı,
          prompt uzunluğu tavanı — ve bunu 30 dakikada ölçen test protokolü.
KARŞILIĞI Araç kapısı BEŞ FİLMDE DE koşulmadı [DERS 23]:
          DERS 32  "güneş kamera arkasında" cümlesi iki kez tutmadı; son
                   filmde güneş diski üç klipte kadraja girdi, gölge donuk
          DERS 33  "any suited figure" negatifi ASTRONOT üretti
          DERS 31  plan 4–10 sn varyans yazdı; on klip de 6,0 sn çıktı
DÖNÜŞÜ    kilavuzlar/ARAC_KARTLARI.md (HENÜZ YOK) · üretim günlüğü §0 araç
          kapısı · PROMPT_SABLONU band hedefi · KILAVUZ_REHBERI §8
KOŞU      ⛔ koşulmadı — 07.09.2026 yazıldı
```

⚠️ **A3'ten farkı:** A3 "hangi boru hattı aynı binayı tutar" diye sordu.
A7 "elimdeki araç NE YAPIYOR ve bunu nasıl ölçerim" diye soruyor. A3 seçim,
A7 profil. İkisi aynı rapora sığmaz; A3'ün karar tablosu araç seçer, A7'nin
kartı seçilen aracın sınırlarını yazar.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen üretken video ve görüntü modelleri üzerine üretim hattı kuran bir teknik araştırmacısın; benim ürünüm 9:16 dikey, sessiz, on klipten oluşan bir yapay zekâ inşaat timelapse filmi ve her klip aynı sabit kameradan, aynı yapının daha ileri bir aşamasını göstermek zorunda.

Ölçülmüş arıza şu: promptta "no suited figure is present" yazdığım hâlde teslim filmde net astronotlar çıktı, "the sun stays behind the camera" cümlesine rağmen güneş diski üç klipte kadraja girdi ve gölgeler klip içinde hiç dönmedi, plan 4 ile 10 saniye arasında değişen klip süreleri istediği hâlde on klibin onu da tam 6,0 saniye çıktı — ve bunların hiçbiri üretimden önce ölçülmemişti, çünkü aracın ne yaptığını yazan tek bir kayıt yoktu.

Birinci görevin: bugün itibarıyla şu video modellerinin her biri için sürüm ve tarih vererek şunları belgele — Google Veo 3 serisi, Kling 2 serisi, Runway Gen-4, Luma Ray, Pika, MiniMax/Hailuo, OpenAI Sora, ByteDance Seedance, Alibaba Wan, Lightricks LTX ve bulduğun diğerleri: seçilebilen tam klip süreleri, negatif promptun ayrı bir alan mı yoksa metin içi mi olduğu, metin içi negatif cümlelerin yasakladığı şeyi ÜRETME (sızma) davranışı üzerine ölçüm var mı, kamerayı sabitleyen bir ayar/mod var mı, görüntüden videoda ilk kare birebir korunuyor mu, ve gölge/ışık yönünün klip boyunca tutarlılığı üzerine belgelenmiş ne var.

İkinci görevin: bilinmeyen bir aracı 30 dakikanın altında profilleyen, TEKRARLANABİLİR bir test protokolü tasarla — kaç test klibi, hangi tek prompt, hangi ölçümler (ffprobe ile gerçek süre ve fps, ilk/son karede kamera kayması, bir nesnenin gölge açısı farkı, negatif sızması var mı, prompt uzunluğu tavanı) — ve profesyonel stüdyoların yeni bir aracı devreye alırken yaptığı yeterlilik testlerinden (VFX/previz vendor qualification) örnek ver.

Üçüncü görevin: prompt uzunluğu ve yapısı üzerine ölçülmüş ne var — iki bin karakterlik bir prompt ile altı bin karakterlik bir prompt arasında talimata uyum farkı ölçülmüş mü, "CAMERA:", "LIGHTING:" gibi etiketli bloklar modelde gerçekten ayrı okunuyor mu, promptun sonuna doğru dikkat düşüyor mu, araç başına token/karakter sınırı nedir, ve negatif cümlelerin promptun neresine konması ölçülmüş olarak daha iyi çalışıyor.

Rapor Türkçe olsun, araç ve parametre adları İngilizce ve SÜRÜM+TARİH ile yazılsın, tablo ağırlıklı olsun; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] bağımsız karşılaştırma, ekran görüntüsü ya da kendi testin · [İDDİA] satıcı ya da blog söylüyor · [VARSAYIM] senin çıkarımın) ve KAYNAK SINIFI (akademik · araç dokümanı · bağımsız karşılaştırma · pazarlama blogu) yaz, satıcının kendi tanıtımını ÖLÇÜM sayma, çelişkiyi ortalama ALMA, bilmediğine "BİLİNMİYOR" yaz; en sonda doldurulmuş tek bir örnek ARAÇ KARTI ver (araç, sürüm, tarih, klip süreleri, negatif alanı, sızma, kamera kilidi, gölge davranışı, ilk kare sadakati, prompt tavanı, bilinen tuzak) ve o kartı doldurmak için kullanılacak İngilizce test klibi promptunu birebir yaz.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A7_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A7-a, A7-b…
3. KILAVUZ     kilavuzlar/ARAC_KARTLARI.md bu rapordan yazılır; her yeni film
               kartı GÜNCELLER (tarihli satır ekler), kart silinmez
4. KAPI        üretim günlüğü §0 bu karttan doldurulur; kart yoksa qa_paket.sh
               zaten durur [DERS 28]
```
