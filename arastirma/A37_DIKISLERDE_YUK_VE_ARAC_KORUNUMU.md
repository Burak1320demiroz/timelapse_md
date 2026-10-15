# 🧪 A37 — DİKİŞLERDE YÜK VE ARAÇ KORUNUMU

```
AMAÇ      Kesmeler (dikişler) arasında kamyon kasasındaki yüklerin sihirli şekilde başka malzemeye
          dönüşmesini (payload swap) ve sahada aynı anda hareket eden araçların birbirinin kimliğini
          çalmasını (vehicle morphing / identity theft) engellemek; "yük sürekliliği" ve "tek hareketli araç"
          kurallarını ölçülebilir kılmak.
KARŞILIĞI 15.10.2026 THE SKY STATION Bölüm 1 ölçümleri:
          · DERS 74: Kamyon kasasındaki iki dev kablo makarası indirilmediği halde dikişte
            aniden çelik çatı makaslarına dönüştü (3:28.0 · Clip 27); kereste kamyonu dikişte
            iki moloz kamyonuna ayrıştı (0:40.0 · Clip 5).
          · DERS 69: Sahada aynı anda vinç, forklift ve kamyon hareket ettirildiğinde araçlar
            birbirine eridi; paletli vinç ekskavatöre (2:16.0), beton pompası miksere (2:03.0) dönüştü.
          · DERS 75: Somut bir alma-bırakma hedefi verilmeyen iş makineleri sahte döngüler üretti:
            vinç yükü kaldırıp aynı römorka geri indirdi (2:24.0), forklift park halindeki tırın
            arkasında 1 dakikadan uzun süre yüksüz dairesel turlar attı (3:52.0–4:40.0).
DÖNÜŞÜ    kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §4 & §5 ·
          ARAC_KARTLARI §2 & §4 · SANTIYE_HAREKETI_KILAVUZU §3
KOŞU      Henüz koşulmadı · derin araştırma botuna yapıştırılacak
```

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, tam metin

Sen video difüzyon modellerinde zamansal nesne tutarlılığı (temporal object consistency, object permanence across cuts), araç kinematiği ve fiziksel yük taşınımı (payload mechanics) üzerine çalışan kıdemli bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — sabit kamera, zaman atlamalı kesmeler ve iki anahtar kare arası I2V video üretimi.

Ölçülmüş arıza ve açık sorun şu: Yapay zekâ video modelleri şantiye araçlarını ve üzerlerindeki yükleri kesmeler boyunca koruyamamaktadır:
1. **Dikişte Yük Takası (Payload Swap Across Cuts):** Kamyon sahada sabit dururken veya geri manevra yaparken, kasasındaki malzeme vinç tarafından indirilmediği halde kesme dikişinde aniden bambaşka bir inşaat malzemesine dönüşmektedir. THE SKY STATION filminde kasadaki iki dev ahşap kablo makarası indirilmeden dikişte aniden üçgen çelik çatı makaslarına dönüşmüş (3:28.0), kereste yüklü kamyon ise dikişte iki ayrı moloz damperli kamyona ayrışmıştır (DERS 74).
2. **Kimlik Hırsızlığı ve Araç Metamorfozu (Vehicle Identity Theft / Morphing):** Sahnede aynı anda birden fazla hareketli araç bulunduğunda (örneğin hareket halindeki bir forklift ve çalışan bir vinç), model araçların özelliklerini birbirine karıştırmakta; paletli kafes bomlu vinç dikişte bomunu kaybedip kazıcı ekskavatöre (2:16.0), beton pompası mikser kamyonuna (2:03.0) dönüşmekte veya araçlar birbirinin içinden geçmektedir (DERS 69).
3. **Amaçsız Gezinme ve Sahte Döngüler (Purposeless Wandering & Idle Loops):** I2V promptunda makineye somut bir "A noktasından alıp B noktasına koyma" hedefi verilmediğinde veya sadece genel bir eylem fiili ("forklift works in yard") yazıldığında, vinç yükü kaldırıp hiçbir montaj yapmadan aldığı yere geri indirmekte (2:24.0), forklift ise 50 saniye boyunca yüksüz olarak aynı kamyonun arkasında anlamsız küçük dairesel turlar atıp durmaktadır (DERS 75).

Birinci görevin: Video difüzyon modellerinde (I2V / DiT mimarileri) nesne sürekliliği ve parça-bütün ilişkisi (object permanence & part-whole binding) teorisini açıkla — ardışık video klipleri üretilirken model neden araç gövdesini (chassis) kısmen korusa bile kasadaki yükü veya makinenin bom tipini bağımsız bir token olarak yeniden hayal eder? Modelin bir video sahnesinde hatasız takip edebileceği maksimum bağımsız hareketli dinamik aktör sayısı (simultaneous moving agents capacity) nedir?

İkinci görevin: Dikişlerde Yük ve Ekipman Korunumu (Payload Persistence Across Seams) yöntemlerini belgelenmiş araştırmalarla incele — park etmiş veya seyir halindeki bir aracın kasasındaki yükün kesmeler arasında erimeden, takas olmadan kilitlenmesini sağlayan prompt, keyframe ve maskeleme stratejileri nelerdir? Kamyonun sahadan ayrılma protokolü ("exit before swap" kuralı) modelin halüsinasyonunu nasıl bastırır?

Üçüncü görevin: Şantiye iş makineleri için "Tek Hareketli Aktör Kuralı (Single Mover Rule)" ve "Amaçlı İş Döngüsü (Purposeful Work Cycle) Sözdizimi" tasarla — sahadaki araçların amaçsız gezinmesini engelleyip her hareketli makineyi somut bir yük-boşalt rotasına bağlayan, diğer tüm araçları ise tam stop ve park halinde tutan standart İngilizce prompt kural ve şablonları nelerdir?

Rapor Türkçe olsun, video, bilgisayarlı görü ve difüzyon terimleri İngilizce kalsın; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] akademik araştırma, benchmark veya resmi doküman · [İDDİA] literatür iddiası · [VARSAYIM] senin analizin), KAYNAK SINIFI (akademik · teknik rapor · endüstriyel doküman) ve ÇÖZÜMLENEBİLİR KAYNAK (arXiv ID, DOI, teknik rapor başlığı) ekle. Raporun sonunda:
(a) ŞANTİYE ARAÇ KORUNUMU VE HAREKET TABLOSU (Araç Türü · İzin Verilen Eylem · Kasadaki Yük Durumu · Yasak Davranış · Hata Kodu),
(b) Kamyon kasası ve iş makineleri için standart İNGİLİZCE YÜK KORUMA VE PARK ŞABLONU (Payload Persistence & Static Park Block),
(c) En fazla 10 maddelik DİKİŞTE ARAÇ VE YÜK DENETİM LİSTESİ ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A37_<BOT>_HAM.md
2. DENETİM     SONUCLAR/A35-A38_DENETIM.md
3. KOD         VARSAYIMLAR.md A37 serisi
4. KILAVUZ     kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §4 & §5
5. KAPI        prompt_kontrol.py: hareketli araç sayısı tavanı (≤1) ve dikişte yük koruma kuralı
```
