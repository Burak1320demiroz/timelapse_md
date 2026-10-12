# 🧪 A27 — SU VE YANSIMA

```
AMAÇ      Su filmin saati olduğunda (taşkın · dolum · boşalma · gölet · yağmur · su üstünde taşıt)
          bozulmayan bir dil kurmak: su kotunun kare kare kilidi ve tanık çizgisi, yükselme ve
          çekilmenin iki yönlü yazımı, sakin suda yansımanın GEOMETRİSİ (kamera yüksekliği → hangi
          su bandında görünür), sıkıştırma rejimine göre suyun görünüşü ve yapay zekânın suyla
          bilinen arızaları.
KARŞILIĞI arşiv ölçümleri + 07.10.2026 THE SLOW TAKEOFF:
          · OVER THE WALL: nehir tek karede kurudu; ıslak beton + nehir "havuz" okundu (DERS 54)
          · THE DEEP STEP: taban suyu fade/boil ile belirdi ("en kötü eriyen")
          · THE MOUNTAIN CROWN: su açılınca ışık günbatımından öğleye sıçradı; su makinelerin üstüne döküldü
          · THE IRON BRIDGE (yatay): taşkın klibinde yükselmiş kemer silindi, sonra sıfırdan kuruldu
          · BACK TO WATER: tekne finalde kadrajdan çıktı (döngü 3/10) · THE TIDE GATE: su kotu her karede
            yazılı, taşkın çizgisi tanık nesne — iyi okundu
          · THE SLOW TAKEOFF: 3 m'lik kameradan 50 m'deki evin yansıması yalnız kameraya 8–17 m'deki sudan
            görünür → gölet planı hesapla değişti; gerçek hızda kano 8 sn'de ≈10–13 m gider → final rotası
            değişti
DÖNÜŞÜ    kilavuzlar/SU_VE_YANSIMA_KILAVUZU.md (✅ 07.10.2026 yazıldı) · HAVA_VE_ATMOSFER (yağmur) ve
          SAHA_VE_IKLIM (kıyı kartı) ile sınır · PLAN'larda SU KOTU satırı
          ⚠️ Sınır: A12 bulut ve atmosferdi; A9 ıslak yüzeyleri malzeme olarak gördü — burası SUYUN
             KENDİSİ: kot, akış, yansıma, su üstündeki hareket
KOŞU      ✅ 07.10.2026 yazıldı ve koşuldu · SONUCLAR/A27_GEMINI_HAM.md · denetim A25-A29_DENETIM.md
```

⛔ **Yansıma hesabı bu depoda TÜRETİLDİ, ölçülmedi** (ayna noktası + ışının su düzlemini kestiği
yer). Rapor aynı hesabı bağımsız verirse doğrulama sayılır; vermezse formül sorulur.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen fiziksel optik (sakin su yüzeyinde yansıma), hidroloji (taşkın, kar erimesi, yüzey suyu davranışı), timelapse fotoğrafçılığı ve yapay zekâ video modellerinin akışkan fiziği üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — kamera tek, sabit ve tilt 0 (ufuk tam kadraj ortasında), dikey filmler 7 klip × 8 sn, yatay filmler 12–48 klip × 8–10 sn, her klip iki sabit görüntü arasında üretilir (bir klibin son karesi bir sonrakinin ilk karesidir) ve her klip bir sıkıştırma rejimiyle yazılır: A = 8 saniyede 10 dakika (≈75 kat), B = 8 saniyede 2 saat (≈900 kat), G = gerçek zaman — ve su filmlerimin çoğunda baş roldedir: fırtına kabarmasına karşı set, batırılan beton kutu, su alıp gemiyi yüzdüren kuru havuz, dolan kanal kilidi, ve son filmde bahar seli yerden 6 m kaldırılmış bir uçak evin altına kadar gelip çekiliyor, eskiden uçağın yattığı çukur gölete dönüşüyor ve finalde bir kano gerçek hızda gövdenin altından geçiyor.

Ölçülmüş arızalar şu: bir filmde nehir tek karede kurudu ve ıslak beton ile su birlikte "yüzme havuzu" diye okundu, bir filmde su saydamlıktan beliren bir kaynama gibi ortaya çıktı, bir filmde su açılınca ışık günbatımından öğleye sıçradı ve su makinelerin üstüne döküldü, bir taşkın klibinde daha önce yapılmış kemer silinip sonra sıfırdan kuruldu, bir filmde tekne finalde kadrajdan çıktı; iyi çalışan tek düzen su kotunun her karede sabit bir nesneye göre yazıldığı ve taşkının bıraktığı çizginin sonraki karelerde tanık olarak kaldığı filmdi; son filmde 3 m yükseklikteki kameradan 50 m ötedeki evin sudaki yansımasının ancak kameraya 8–17 m mesafedeki suda görüneceğini kendim hesapladım ve göleti buna göre büyüttüm, gerçek hızdaki bir kanonun 8 saniyede ancak 10–13 m gidebileceğini hesaplayıp final rotasını kısalttım — bu iki hesabın doğruluğunu ve suyu bu filmlerde nasıl yazmam gerektiğini bilmek istiyorum.

Birinci görevin: fizik ve optiği belgelenmiş kaynaklarla yaz — sakin suda yansıma geometrisi (kamera yüksekliği h, nesne yüksekliği y ve mesafesi D için ayna görüntüsünün kadrajda nereye düştüğü ve yansımanın suyun hangi mesafe bandında göründüğü, formülüyle), Fresnel yansıtırlığının bakış açısıyla değişimi (sıyırma açısında yansıma neden güçlenir), rüzgâr dalgacıklarının yansımayı kırma eşiği (rüzgâr hızı/Beaufort, kılcal dalgalar), bulanık taşkın suyunun rengi ve yansıtma farkı, ıslak/kuru sınırı ve yüksek su izi (silt çizgisi, kalıntı hattı), bir çayırda bahar taşkınının ve kar erimesi selinin tipik yükselme/çekilme hızları (cm/saat, gün) ve küçük bir teknenin/kanonun tipik hızları (m/s) — sayılarıyla ve kaynağıyla.

İkinci görevin: suyun timelapse'teki görünüşünü sıkıştırma oranına göre yaz — profesyonel timelapse fotoğrafçılarının su için aralık (interval) ve pozlama (ND filtre, 1–2 sn pozlama ile "ipek" su) seçimleri, 75 kat ve 900 kat sıkıştırmada yükselen suyun, yağmurun, akıntının ve dalgacığın ekranda nasıl göründüğü, gerçek zamanda (1 kat) su ve yansımanın titreşimi, gece/mavi saatte ışıkların suda yansıması — ve bu görünüşleri İngilizce prompt cümlelerine çevirmek için rejim başına kelime önerileri (her biri gerçek bir fotoğraf pratiğine dayanarak).

Üçüncü görevin: yapay zekâ video modellerinin suyla bilinen arızalarını ölçülmüş verilerle yaz — fizik akla yatkınlığı benchmark'larının (VideoPhy, PhyGenBench, Physics-IQ ve benzerleri) akışkan/sıvı kategorilerindeki tarihli sonuçları, suyun belirmesi/kaybolması, kotun karede zıplaması, yansımanın sahneyle tutmaması, su ile yapının birbirine karışması gibi arıza türleri, iki sabit kare arasında üretilen klipte (first/last frame) su kotunun nasıl kilitlenebileceği (kotu her karede sabit bir nesneye göre kesir olarak yazmak, tanık çizgiyi kalıcı nesne yapmak, yansımayı keyframe'de çizdirmek) ve su üstündeki bir taşıtın kadraja girip kadrajda KALMASI için yazım stratejileri — kanıtı olmayan öneriyi [VARSAYIM] diye işaretleyerek.

Rapor Türkçe olsun, fizik, fotoğraf ve araç terimleri İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, ölçüm ya da resmi belge var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · araç/platform dokümanı · bağımsız karşılaştırma · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI ya da belge adı + bölüm + tarih — kaynağı gösterilemeyen iddia ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç; en sonda (a) YANSIMA HESABI: formül + kamera yüksekliği 2 · 3 · 5 · 10 m ve nesne mesafesi 30 · 50 · 100 m için "yansıma hangi su mesafesinde ve kadrajın yüzde kaçında görünür" tablosu (24 mm tam kare, yatay 16:9, tilt 0), (b) kare başına doldurulacak bir SU KOTU DEFTERİ şablonu (sabit nesneye göre kot · kadraj yüzdesi · yükseliyor/çekiliyor · tanık çizgi), (c) rejim başına (≈75× · ≈900× · 1×) su, yağmur, taşkın, dalgacık ve yansıma için İngilizce ifade tablosu ve (d) en fazla 12 maddelik bir kontrol listesi ver — her madde için ihlalde yapılacak tek eylem (KAREYİ YENİDEN ÜRET · KOTU YENİDEN YAZ · ROTAYI KISALT).

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A27_<BOT>_HAM.md — dokunulmadan [kart S]
2. DENETİM     SONUCLAR/A25-A29_DENETIM.md — yansıma formülü bu makinede yeniden hesaplanır
               (THE SLOW TAKEOFF: h 3 · D 50 → 8–17 m bandı) · hız sayıları kaynağından çekilir
3. KOD         VARSAYIMLAR.md · kuşak bölümüne (+ DİZİN satırı)  A27-a, A27-b…
4. KILAVUZ     kilavuzlar/SU_VE_YANSIMA_KILAVUZU.md bu rapordan yazılır
5. KAPI        PLAN'da SU KOTU satırı (su varsa zorunlu) · prompt kapısında su kelimesi + kot cümlesi
```
