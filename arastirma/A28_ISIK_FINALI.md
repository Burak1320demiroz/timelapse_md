# 🧪 A28 — IŞIK FİNALİ: MAVİ SAAT VE YAPAY IŞIK

```
AMAÇ      Filmlerin en çok kullandığı ödül anını — yapının ışıklarının yanması, mavi saat — bozulmayan
          bir dile bağlamak: mavi saatin zamanı ve süresi (enlem · mevsim), ışığın bir MALZEME olarak
          önceden takılması ve grup grup yanma sırası, gök ile yapay ışık arasındaki pozlama dengesi,
          sıkıştırma rejiminde ışığın "belirmesi", hale/bloom/flare halüsinasyonu ve küçük resim için
          en iyi ışıklı kare.
KARŞILIĞI arşiv ölçümleri (değerlendirici okuması, izleyici verisi DEĞİL):
          · en yüksek okunan finallerin çoğu ışıkla bitiyor: DEEP END (küçük ışıklar sıra sıra) · LAST HARBOR
            (fener yanar) · BLUE DOOR (lamba → fener → pencere) · FIRST GUEST (kapı ışığı kuma yayılır) ·
            EDEN ARK (kemer lambaları) · THE SLOW TAKEOFF (pencereler gruplar hâlinde, sonra kano)
          · POLAR HABITAT: promptta olmayan lazer, bloom, yıldırım arkı · FIRST GUEST: lamba halesi, asılı toz ·
            STAR DOCK: hacimsel huzme pozlamayı patlattı · THE LONG DAY: güneş diski kadraja girdi ·
            DERS 45: final zifiri karanlıkta biterse okunmaz
          · P12-d: 75× sıkıştırmada lamba "yanmaz, belirir" · P11-d: ışık önceden sönük takılmazsa yoktan doğar
          · mavi saat bugün YALNIZ DERSLER'de ve yayın planında geçiyor — kılavuzu yok
DÖNÜŞÜ    kilavuzlar/ISIK_FINALI_KILAVUZU.md (✅ 07.10.2026 yazıldı) · ZAMAN_VE_ISIK §5 (gece) ile sınır ·
          MUZIK_VE_KAPAK §2 (kapak = ışıklı usta kare)
          ⚠️ Sınır: A4/A12 güneş ve gök; burası YAPAY IŞIK + alacakaranlık + finalin kendisi
KOŞU      ✅ 07.10.2026 yazıldı ve koşuldu · SONUCLAR/A28_GEMINI_HAM.md · denetim A25-A29_DENETIM.md
```

⛔ **Bu depoda yasak kelime kuralı var: istenmeyen nesneyi adıyla anmak, negatifte bile, onu
çağırır** (DERS 33 · 35 · 59). Rapor "no lens flare, no bloom" önerirse bunun ölçülmüş etkisini
de sormuş olduk — kanıt yoksa [VARSAYIM].

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen mimari alacakaranlık fotoğrafçılığı, gündüzden geceye (day-to-night, "holy grail") timelapse tekniği ve yapay zekâ görüntü/video modellerinde ışık kaynaklarının üretimi üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — kamera tek, sabit ve tilt 0, her klip iki sabit görüntü arasında üretilir (bir klibin son karesi bir sonrakinin ilk karesidir), filmin ışığı tek bir günün sabahından akşamına kesintisiz akar (kesmede ışık atlamaz) ve klipler sıkıştırma rejimiyle yazılır: A = 8 saniyede 10 dakika (≈75 kat), B = 8 saniyede 2 saat (≈900 kat), G = gerçek zaman — ve en iyi okunan filmlerimin çoğu bir ışık anıyla bitiyor: tamamlanan yapının lambaları, fenerleri ya da pencereleri mavi saatte gruplar hâlinde yanar, ışıklar suya yansır, son birkaç saniye hiçbir şey değişmeden tutulur ve kanalın küçük resmi bu son karedir.

Ölçülmüş arızalar şu: bir filmde promptta hiç olmayan lazer ışınları, bloom ve yıldırım arkları belirdi, bir filmde lamba çevresinde hale ve havada asılı toz oluştu, bir filmde hacimsel bir ışık huzmesi pozlamayı patlattı, erken bir filmde güneş diski kadraja girdi, karanlıkta biten finaller okunmadı; 10 dakikanın 8 saniyeye sıkıştığı rejimde bir lamba "yanmıyor, bir anda beliriyor", ve önceden yerine takılmış gösterilmeyen ışık kaynağı yoktan doğuyor — bu yüzden lambaları birkaç klip önce SÖNÜK olarak taktırıyorum; ayrıca deneyimle şunu öğrendim ki istenmeyen bir nesneyi promptta adıyla anmak, "no …" diye bile olsa, o nesneyi çağırıyor — bu yüzden "no lens flare" yazmanın işe yarayıp yaramadığını bilmiyorum; ve mavi saatin kaç dakika sürdüğünü, filmin ışık bütçesine (sabah → akşam toplam en çok 14 saat) nasıl sığacağını, güneş ufkun kaç derece altındayken pencere ışığının gökle dengelendiğini sayıyla bilmiyorum.

Birinci görevin: fotoğraf ve astronomi gerçeklerini sayılarla yaz — mavi saat ve sivil alacakaranlığın tanımı (güneş ufkun 0°, −4°, −6° altı), 35°–60° enlemlerde gündönümü ve ekinoksta gün batımından sonra bu açılara kaç dakikada inildiği (tablo ya da formül), gökyüzü parlaklığının ve renk sıcaklığının bu aralıkta değişimi, mimari fotoğrafçıların iç/dış pozlama dengesini yakaladığı an ve kullandıkları kural, pencere ve lamba ışığının uzaktan görünür boyutu (kadrajda kaç piksel), sıcak (2700–3000K) ve soğuk ışık kaynaklarının gök mavisine karşı okunurluğu, ve yapay ışıkların sakin sudaki yansımasının görünüşü — her biri kaynağıyla.

İkinci görevin: gündüzden geceye timelapse pratiğini yaz — pozlama rampası (exposure ramping, bulb ramping, LRTimelapse gibi araçlar), aralık seçiminin ışıkların yanış anını ekranda nasıl gösterdiği (75 kat ve 900 kat sıkıştırmada bir lambanın açılması kaç kare sürer), titreşim (flicker) ve deflicker, mavi saatin ekranda kaç saniye kaldığı, profesyonel yapımlarda bir yapının ışıklarının "sırayla yanması" anının nasıl kurulduğu (gerçekte mi, kurguda mı) ve finalde hareketsiz tutuşun süresi — ve bunları İngilizce prompt cümlelerine çevirmek için rejim başına ifade önerileri.

Üçüncü görevin: yapay zekâ görüntü/video modellerinin ışıkla bilinen arızalarını tarihli ve ölçülmüş kaynaklarla yaz — bloom, hale, lens flare ve ışın halüsinasyonu, armatürü olmayan ışık kaynağı, gece sahnesinin ya çok karanlık ya "neon" olması, pozlama pompalanması, ışıkların yanlış sırada ya da birden yanması, ışığın sudaki yansımasının tutmaması — ve bunlara karşı yazım stratejilerini kanıt düzeyiyle karşılaştır: armatürü önceki karelerde sönük nesne olarak göstermek, yanma sırasını ve grupları saniyesiyle yazmak, negatif prompt'ta istenmeyen etkiyi ADIYLA anmanın ölçülmüş sonucu (işe yarıyor mu, tersine mi çalışıyor — negatif prompt ve "negation" üzerine yapılmış çalışmalar), önce ışıklı final karesini üretip ışıksız kareleri ondan düzenleyerek geriye türetmek; ayrıca ışıklı bir karenin küçük resim (thumbnail) olarak 120 piksele küçültüldüğünde okunurluğu için kontrast kuralları.

Rapor Türkçe olsun, fotoğraf, astronomi ve araç terimleri İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, ölçüm ya da resmi belge var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · araç/platform dokümanı · bağımsız karşılaştırma · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI ya da belge adı + bölüm + tarih; araç davranışı için tarihli sürüm notu — kaynağı gösterilemeyen iddia ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) 35° · 45° · 55° enlem ve 21 Mart · 21 Haziran · 21 Aralık için güneşin −2° · −4° · −6°'ye indiği, gün batımından sonraki dakika TABLOSU (ya da formülü ve bir örnek hesap), (b) yapının her ışık kaynağı için doldurulacak bir IŞIK DEFTERİ şablonu (armatür · takıldığı klip · sönük göründüğü kareler · grup · yanma sırası ve saniyesi · renk sıcaklığı · suda yansıması var mı), (c) rejim başına (≈75× · ≈900× · 1×) ışıkların yanışı, mavi saat göğü ve tutuş için İngilizce ifade tablosu ve (d) en fazla 12 maddelik bir kontrol listesi ver — her madde için ihlalde yapılacak tek eylem (KAREYİ YENİDEN ÜRET · SIRAYI YENİDEN YAZ · NEGATİFTEN ÇIKAR).

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A28_<BOT>_HAM.md — dokunulmadan [kart S]
2. DENETİM     SONUCLAR/A25-A29_DENETIM.md — alacakaranlık tablosu bu makinede güneş formülüyle
               yeniden hesaplanır (THE SLOW TAKEOFF 47° K · δ +12° · −4,4° = 19:20)
3. KOD         VARSAYIMLAR.md · kuşak bölümüne (+ DİZİN satırı)  A28-a, A28-b…
4. KILAVUZ     kilavuzlar/ISIK_FINALI_KILAVUZU.md bu rapordan yazılır
5. KAPI        PLAN'da IŞIK DEFTERİ (final ışıklıysa zorunlu) · lamba "sönük takılı" satırı yoksa FIX
```
