# 🌤️ A12 — HAVA VE ATMOSFER

```
AMAÇ      Atmosferik gerçekçiliği kurmak: bulut, sis, toz, yağış, rüzgâr
          etkisinin klip İÇİ davranışı — nasıl hareket eder, ne hızda, hangi
          yöne — ve gök ile yerin AYNI saate bağlanması.
KARŞILIĞI ③ ZAMAN ⛔ CLOUD AND SKY düşüşleri · TIME RATE 0/10 (iki filmde)
          DERS 15 (gök hızlı, yer yavaş — iki ayrı saat)
          DERS 18 (I2V'de yazılmazsa gök donuyor)
          DERS 14 (mevsim taşıyıcısı olmayan sahne zamanı durduruyor)
          DERS 26 (mevsim üretilmedi — sonbahar hiç çıkmadı)
          DERS 40 (gölgesiz klip = zamanın tek taşıyıcısı yok)
          DERS 47 (motion blur var, gölge donuk — "frozen sun")
          DERS 50 (yıldızlar akıyor, araçlar cam gibi net — time rate disconnect)
          A4-c (yıldız izi derecesi) · A6-b ÖLÇTÜM (gölge dönüşü 116°–191°)
DÖNÜŞÜ    kilavuzlar/HAVA_VE_ATMOSFER_KILAVUZU.md (HENÜZ YOK — bu prompt onu
          yazdıracak) · PROMPT_SABLONU TIME RATE ve LIGHTING blokları ·
          prompt_kontrol.py
          ⚠️ Sınır: ZAMAN_VE_ISIK = güneş ve mevsim (SAAT) · SANTIYE_HAREKETI
             §1–2 = rejim (HIZ) · burası = göğün ve havanın o hızdaki GÖRÜNÜMÜ
KOŞU      ⛔ koşulmadı — v1 08.09.2026 · v2 11.09.2026
SÜRÜM v2  altı cümleye tamamlandı (A5 kalıbı) · gök–yer saat birliği tablosu
          eklendi (DERS 15·47·50 üç filmde) · havasız/ince atmosferli/buz gökü
          eklendi · anlamsal ayrışma sorusu eklendi · iki-keyframe kısıtı
          (ilk/son karede gök durumu) eklendi · ÇÖZÜMLENEBİLİR KAYNAK şartı eklendi
```

⛔ **ZAMAN_VE_ISIK güneşi tarif ediyor, gökyüzünü tarif etmiyor.** Model
gökyüzünü ayrı, yeri ayrı hızlandırıyor çünkü atmosfer fiziği prompt düzeyinde
hiç yazılmadı. Bulut tipi, hareket yönü, sıkıştırma oranına göre görünüm
hiçbir kılavuzda yok — ve aynı arıza üç filmde üç kez ölçüldü.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen atmosfer fiziği, bulut dinamiği ve gerçek (optik) timelapse sinematografisi üzerine çalışan bir araştırmacısın; benim ürünüm 9:16 dikey, konuşmasız, yapay zekâ ile üretilmiş bir inşaat timelapse filmi: 10 sahne, her sahne yaklaşık 6 saniye, kamera on sahnede aynı noktada sabit (24 mm eşdeğeri, yapıya ~40 m mesafe, tilt 0°, ufuk kare yüksekliğinin tam yarısında), her klip iki onaylı SABİT görsel arasında image-to-video ile üretiliyor (ilk kare ve son kare birer fotoğraf, video ikisini bağlıyor), her klip tek bir sıkıştırma rejimiyle beyan ediliyor (yaklaşık 100× = 10 dakika, 1200× = 2 saat, 5400× = 9 saatlik iş günü) ve her film bağımsız bir denetçi tarafından zaman damgalı rubriklerle puanlanıyor.

Ölçülmüş arıza şu: denetçi üç filmde gök ile yerin AYRI saatlerde aktığını ölçtü — "clouds race across the sky in heavy time-lapse, while the workers on the deck below move at near real-time speeds", "the trucks driving on the left-hand road move at normal, real-time video speed", "excavators move in near real-time within the pit while sky lighting and time-lapse progression occur at a hyper-accelerated rate" — bir filmde makineler motion blur ile akarken gölgeler klip boyunca hiç oynamadı, bir başkasında yıldızlar akarken araçlar ve kalkan toz cam gibi net kaldı, beş klipte bulut hiç hareket etmedi, iki sahnede mevsim "indeterminate — bare rock and concrete with no foliage, weather, or sun-height carriers" okundu ve bir filmde kar tek klipte yağıp aynı klipte eridi, o filmin ekrandan okunan süresi planın %30-70 üstüne çıktı; güneş açısı ve gölge yönü promptlarda dereceyle yazılıydı ama bulut tipi, hareket yönü, sıkıştırma oranındaki görünüm ve atmosferik derinlik hiç yazılmamıştı.

Birinci görevin: gerçek optik timelapse çekimlerinde sıkıştırma oranına göre — benim üç rejimim 100×, 1200× ve 5400× — gökyüzü ve atmosfer olaylarının GÖRSEL İMZASINI tablo hâlinde yaz: bulut tipi başına (cumulus, stratus, cirrus, cumulonimbus, altostratus, sis ve pus) hareket hızı (m/s ve kadraj geçiş süresi), şekil değişimi, yerdeki gölge etkisi, renk tonu; her oran × bulut tipi için 6 saniyelik bir klipte bulutun ekranda NE KADAR yol aldığını, kadrajın yüzde kaçını geçtiğini, nasıl uzadığını (şerit, akış, silinme, kaynama) belgelenmiş çekim verileriyle ver; sonra aynı tabloyu YER için de yaz — aynı rejimde bir nesnenin gölgesi kaç derece döner, bir kamyon kadrajı kaç karede geçer ve nasıl bulanır, yürüyen bir insan görünür mü — ki gök ile yerin AYNI saate bağlı olduğunu tek tabloda gösterebileyim.

İkinci görevin: atmosferik perspektif ve derinlik ipuçlarını — uzaktaki nesnenin renk kayması (Rayleigh saçılımı), pus yoğunluğu, kontrast düşüşü, detay kaybı — mesafe bandına göre (0-50 m, 50-200 m, 200-1000 m, ufuk) ve hava koşuluna göre (açık, bulutlu, sisli, tozlu, yağmurlu, karlı) tablo hâlinde yaz; havasız ve ince atmosferli dünyalar için karşılığını ayrıca yaz — Ay'da pus yok, siyah gök, gündüz yıldız görünürlüğü, gölge keskinliği ve ufkun yakınlığı; Mars'ta kızıl saçılım, mavi gün batımı ve toz fırtınası; buz gezegeninde kar sisi, beyaz gök ve gölgesiz düz ışık — ve her koşul için prompt düzeyinde İngilizce bir derinlik/gök cümlesi öner.

Üçüncü görevin: yağış ve rüzgârın klip İÇİ zaman damgasını — yağmur başlarken yüzeylerin ıslanma sırası ve süresi, kar birikme hızı (cm/saat ve kadrajda piksel/saniye), rüzgârın bayrak/tente/toz bulutuna etkisi, ıslak yüzeyin kuruma süresi — tablo hâlinde ve ölçülmüş verilerle yaz; "yağış bir klipte BAŞLARSA ne olur" ve "BİTERSE ne kalır" (birikinti, ıslak leke, erime çamuru, iz) sorularını yanıtla; gölgesi olmayan bir sahnede (kapalı gök, gece, kutup, fırtına) zamanın geçtiğini kanıtlayan ALTERNATİF taşıyıcıları (pus hareketi, toz duvarı, ıslak-kuru sınırının ilerlemesi, yapay ışık gölgesi, beton renk değişimi, yıldız izinin derece uzunluğu) sırala; AI video üretiminde "timelapse" komutunun gök ile yeri neden ayrı hızlandırdığı (anlamsal ayrışma) üzerine ne belgelenmiş, hangi prompt cümlesi ya da iş akışı (örneğin gerçek zamanlı üretip kurguda hızlandırma) ikisini yeniden aynı saate bağlıyor — ölçülmüş örneklerle yaz; ve benim formatımda her klibin ilk ve son karesi sabit iki görsel olduğundan, gök hareketinin bu iki kare arasında tutarlı olması için ilk ve son karedeki bulut, gölge ve ışık durumunun nasıl yazılması gerektiğini belirt.

Rapor Türkçe olsun, meteoroloji ve fizik terimleri İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, ölçüm ya da çekim kaydı var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · araç dokümanı · sinematografi kaynağı · uzay ajansı belgesi · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI ya da belge adı + bölüm; kaynağı gösterilemeyen sayı ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç ve yukarıda yanlış bulduğun her şeyi orada topla; en sonda her atmosfer durumu ve her rejim için üretim promptuna doğrudan yapıştırılacak, İngilizce ve POZİTİF (yasak cümlesi değil, ölçülebilir betimleme) birer TIME RATE + LIGHTING gök cümlesi ver, örneğin "clouds cross the full width of the frame from left to right in about four seconds, stretching into long horizontal streaks as they go; the shadow of the split-top boulder sweeps thirty degrees across the plain; the sky grades from deep blue at the zenith to pale white above the horizon".

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A12_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         VARSAYIMLAR.md · kuşak bölümüne (+ DİZİN satırı)  A12-a, A12-b…
3. KILAVUZ     kilavuzlar/HAVA_VE_ATMOSFER_KILAVUZU.md bu rapordan yazılır
4. KAPI        prompt_kontrol.py: I2V promptunda gök/atmosfer hareketi cümlesi zorunlu
```
