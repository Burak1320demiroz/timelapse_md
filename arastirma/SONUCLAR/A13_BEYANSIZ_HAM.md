# 🔬 A13 HAM — Sinematik Motion-Control Timelapse Raporu — teknik, estetik, üretim güvenliği

```
KÜNYE — kart S §1 · beş satır
BOT            ⛔ BEYAN EDİLMEDİ (proje sahibi yapıştırdı; hangi araç/model olduğu yazılmadı)
TARİH          17.09.2026 (deppoya giriş günü)
KESİLDİ Mİ     hayır — yapıştırılan metnin tamamı · 47538 karakter
PROMPT         ⛔ YOK. Bu kuşak İSTENMEDİ; rapor bu depoda yazılmış bir A13 promptuna
               cevap değildir. Neyin SORULDUĞU bilinmiyor ⇒ neyin DIŞARIDA BIRAKILDIĞI da bilinmiyor.
KAYNAK SINIFI  ⚠️ karışık · ağırlıkla pazarlama/SEO · atıf işaretleri ([cite: n]) çözümlenemiyor
               → arastirma/00_README §3 adım 2b gereği yalnız denetimden geçen madde kılavuza iner
DENETİM        arastirma/SONUCLAR/A13-A18_DENETIM.md
```

⛔ **BURADAN AŞAĞISI HAM ÇIKTIDIR — DOKUNULMAZ.** Düzenleme · kısaltma · özetleme YOK.

---

Sinematik Motion-Control Timelapse Raporu: Teknik, Estetik ve Üretim Güvenliği Standartları
Motion-control timelapse sinematografisi; optik, mekanik, matematiksel ve dijital süreçlerin hassas bir dengede yürütüldüğü ileri düzey bir görsel üretim disiplinidir. Gerçek zamanlı videodan farklı olarak timelapse, zamanın sıkıştırılması esnasında kamera konumu, bakış açısı ve ışık değerlerinin kare kare (frame-by-frame) manipüle edilmesi esasına dayanır. Kamera hareketinin akıcı, anlaşılır, sinematik ve izleyici zihnini yormayacak kadar kontrollü olması; fiziksel hareketin dinamikleri ile post-prodüksiyon yazılımlarının harmonik uyumunu gerektirir.

Temel Timelapse Hesaplamaları ve Matematiksel Modeller
Motion-control timelapse prodüksiyonlarında görsel akıcılık, hareketin ve zamanın doğru matematiksel denklemlerle kurgulanmasına bağlıdır. Yanlış hesaplanan bir interval veya adım miktarı, final videoda ya sarsıntılı ve kesikli bir akışa (jitter/stutter) ya da hareketin hiç hissedilmediği durağan bir görüntüye yol açar.   

Toplam Çekim Süresi (T 
c
¸
​
 ekim
​
 )
Toplam çekim süresi, sahadaki toplam fiziksel maruz kalma süresidir:
  

T 
c
¸
​
 ekim
​
 =N 
kare
​
 ×I
Örnek: 24 fps hızında 15 saniyelik bir klip için 360 kare (N 
kare
​
 ) çekilecekse ve interval (I) 5 saniye olarak belirlenmişse:
  

T 
c
¸
​
 ekim
​
 =360×5 saniye=1800 saniye=30 dakika
Çekilecek Toplam Kare Sayısı (N 
kare
​
 )
Final video süresi (T 
final
​
 ) ve hedeflenen oynatma kare hızına (FPS) göre required fotoğraf adedi:
  

N 
kare
​
 =T 
final
​
 ×FPS
Örnek: 25 fps oynatma hızında 12 saniyelik sinematik bir sekans için:
  

N 
kare
​
 =12 saniye×25 fps=300 kare
Final Timelapse Süresi (T 
final
​
 )
Çekilen toplam kare sayısının kurgu zaman çizgisindeki süresi:
  

T 
final
​
 = 
FPS
N 
kare
​
 
​
 
Örnek: 600 adet RAW fotoğraf çekilmişse ve proje 30 fps olarak ayarlanmışsa:
  

T 
final
​
 = 
30
600
​
 =20 saniye
Çekimler Arasındaki İnterval (I)
Sahada ayrılan toplam zaman bütçesi (T 
c
¸
​
 ekim
​
 ) ve gerekli kare sayısına göre iki deklanşör arasındaki bekleme süresi:
  

I= 
N 
kare
​
 
T 
c
¸
​
 ekim
​
 
​
 
Örnek: Gün batımı sürecinde sahada 45 dakika (2700 saniye) kalınabiliyorsa ve 25 fps hızında 12 saniyelik klip (300 kare) isteniyorsa:
  

I= 
300
2700
​
 =9 saniye
Kare Başına Kamera Hareketi (D 
kare
​
 )
Motion-control sisteminin her bir deklanşör tetiklemesi arasında mekanik eksende katedeceği mesafe:

D 
kare
​
 = 
N 
kare
​
 
D 
toplam
​
 
​
 
Örnek: 150 cm (1500 mm) uzunluğundaki bir slider rayında 500 kare çekilecekse:

D 
kare
​
 = 
500
1500 mm
​
 =3 mm/kare
Slider'ın Toplam Yol Mesafesi (D 
toplam
​
 )
Belirlenen step büyüklüğü ve kare sayısına göre mekanik eksen ihtiyacı:

D 
toplam
​
 =D 
kare
​
 ×N 
kare
​
 
Örnek: Kare başına 1.8 mm kaydırma yapılması planlanıyor ve 400 kare çekilecekse:

D 
toplam
​
 =1.8 mm×400=720 mm=72 cm
İleri Gidip Başlangıç Noktasına Dönün Simetrik Hareketin Zamanlaması (T 
simetrik
​
 )
Kameranın A noktasından B noktasına gidip tepe noktasında kısa bir süre durakladıktan sonra tam olarak A noktasına döndüğü simetrik döngülerde toplam zaman:

T 
simetrik
​
 =(2×N 
yarı
​
 +N 
bekleme
​
 )×I
Örnek: İleri yönlü hareket 200 kare (N 
yarı
​
 ), odak noktasındaki bekleme 40 kare (N 
bekleme
​
 ) ve geri dönüş 200 kare tutuyorsa; interval de 4 saniye ise:
  

T 
simetrik
​
 =(2×200+40)×4=440×4=1760 saniye≈29.3 dakika
Kamera Hareketlerinin Bireysel Teknik ve Estetik Analizi
1. Locked-off (Sabit Kamera)
Görsel ve Psikolojik Etkisi: Zamanın akışını nesnel, sarsılmaz ve belgesel nitelikte sunar. İnsan algısını kadraj içi değişime (bulutlar, ışık, insan akışı) yönlendirir.   

Etkili Olduğu Konular: Gökyüzü ve bulut hareketleri, şantiye süreçleri, trafiğin ışık izleri, mevsimsel değişimler.   

Dikkat Dağıttığı Durumlar: Kadraj içi hareketin son derece yavaş veya yetersiz olduğu durağan sahnelerde görsel durağanlık yaratır.

Kamera Başlangıç ve Bitiş Konumu: Konum sabittir; optik eksen değişmez.

Hareket Mesafesi ve Yönü: 0 mm, hareketsiz.

Paralaks Düzeni: Paralaks oluşmaz; derinlik hissi yalnızca ışık-gölge ve kadraj içi objelerin ölçek farkıyla sağlanır.

Ekipman İhtiyacı: Ağır ve sağlam tripod, kum torbaları, entegre veya harici intervalometre.   

Zamanlama Parametreleri: 10 saniyelik video (24 fps) için 240 kare; bulutlar için 3-5 sn interval ile 1200 sn (20 dk) çekim.   

Kare Başına Hareket: 0 mm/kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: 180 
∘
  enstantane kuralı uyarınca shutter hızı intervalin yarısı olmalıdır. Gündüz ND64-ND1000 filtre şarttır. Işık değişimlerinde diyalog atlaması (flicker) riski yüksektir.   

Post-Prodüksiyon İşlemleri: LRTimelapse ile de-flicker işlemi, mikroskobik titremeler için DaVinci Resolve Edit sayfasında "Perspective" stabilizasyonu.   

En Yaygın Hatalar ve Çözümleri: Otomatik odaklama (AF) yüzünden odak avlaması (focus hunting). Çözüm: Manuel odaklama (MF) yapmak ve netlik halkasını gaffer bant ile sabitlemek.   

2. Push-in (Yaklaşma)
Görsel ve Psikolojik Etkisi: İzleyicide merak uyandırır, ana konuya odaklanmayı zorunlu kılar ve sahnenin içine çekilme hissi yaratır.

Etkili Olduğu Konular: Mimari detaylar, tarihi anıtlar, stüdyo ürün çekimleri, orman patikaları.

Dikkat Dağıttığı Durumlar: Ön planda engellerin bulunduğu ve kadrajın aniden tıkandığı dar alanlar.

Kamera Başlangıç ve Bitiş Konumu: Başlangıç genel plan, bitiş yakın plan.

Hareket Mesafesi ve Yönü: Slider üzerinde ileri yönlü 80−150 cm.

Paralaks Düzeni: Ön plandaki nesnelerin (ağaç, sütun) kadraj kenarlarına doğru hızla genleşmesi, arka planın ise daha yavaş büyümesi gerekir.

Ekipman İhtiyacı: Motorlu slider veya lineal dolly.   

Zamanlama Parametreleri: 300 kare, 4 sn interval (1200 sn çekim) → 10 sn klip (30 fps).   

Kare Başına Hareket: 1000 mm/300 kare=3.33 mm/kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: İleri harekette ön plan nesnelerinde akıcı motion blur sağlamak için 1−2 sn shutter hızı tercih edilir.   

Post-Prodüksiyon İşlemleri: Hız eğrisini (ease-in/ease-out) yumuşatmak için kurguda dikey pozisyon eğrilerini düzenleme.

En Yaygın Hatalar ve Çözümleri: Sarsıntılı başlama. Çözüm: Moco motorunda S-curve ivmelenme (acceleration) tanımlamak.   

3. Pull-out (Uzaklaşma)
Görsel ve Psikolojik Etkisi: Yalnızlık, vedalaşma, ortamın genelini ortaya çıkarma (reveal) ve anlatıyı sonlandırma hissi verir.

Etkili Olduğu Konular: Manzara açılışları, kalabalık meydanlar, batan güneş eşliğinde şehir silüetleri.   

Dikkat Dağıttığı Durumlar: Arka planda görsel değeri olmayan boş veya estetik dışı alanların kadraja girmesi.

Kamera Başlangıç ve Bitiş Konumu: Başlangıç konuya yakın, bitiş çevreyi kapsayan genel plan.

Hareket Mesafesi ve Yönü: Gerilme ekseninde 100−200 cm geriye doğru.

Paralaks Düzeni: Yakındaki objeler kadrajın merkezine doğru küçülürken arka alan kadraja dahil olur.

Ekipman İhtiyacı: Uzun raylı slider veya otonom dolly.   

Zamanlama Parametreleri: 250 kare, 3 sn interval (750 sn çekim) → 10 sn klip (25 fps).   

Kare Başına Hareket: 1500 mm/250=6 mm/kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Geri geriye kayarken genişleyen kadrajda parlaklık değişimleri oluşabileceğinden ISO/Shutter ramping gerekebilir.   

Post-Prodüksiyon İşlemleri: Ters yönde oluşabilecek dijital moiré etkisini gidermek için hafif keskinlik düşürme.

En Yaygın Hatalar ve Çözümleri: Kamera gerilerken operatörün veya tripod gölgesinin kadraja girmesi. Çözüm: Güneş açısını ve hat izini önceden simüle etmek.

4. Push-in Sonrası Başlangıç Noktasına Geri Dönme (Symmetrical Push-Pull)
Görsel ve Psikolojik Etkisi: Tamamlanmışlık, hipnotik bir döngü ve süreç incelemesi hissi uyandırır. İzleyiciyi odak noktasına götürüp tekrar güvenli genel plana döndürür.

Etkili Olduğu Konular: Sanatsal enstalasyonlar, restorasyon projeleri, bitki büyümesi, bina inşaatı.   

Dikkat Dağıttığı Durumlar: Geri dönüş esnasında sahnenin ışığında aşırı tutarsızlık yaşanması.

Kamera Başlangıç ve Bitiş Konumu: A→B→A şeklinde aynı koordinat.

Hareket Mesafesi ve Yönü: Toplam 200 cm (100 cm ileri, 100 cm geri).

Paralaks Düzeni: İleri harekette genişleyen katmanlar, geri harekette aynı doğrultuda daralmalıdır.

Ekipman İhtiyacı: Hassas kodlayıcılı (encoder) motorlu moco slider.   

Zamanlama Parametreleri: İleri 200 kare, tepe noktasında 50 kare bekleme, geri 200 kare (Toplam 450 kare, 2 sn interval →900 sn çekim).

Kare Başına Hareket: 1000 mm/200=5 mm/kare (bekleme evresinde 0 mm).

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Yön değiştirme anında sıfır hız oluştuğundan durağan karelerde flicker fark edilebilir. Otomatik deflicker zorunludur.   

Post-Prodüksiyon İşlemleri: Tepe noktasındaki durağanlığı speed ramp ile akıcı hale getirmek.   

En Yaygın Hatalar ve Çözümleri: Başlangıç ve bitiş kadrajının kayması. Çözüm: Moco sisteminde "Keypose" kaydı yapmak.   

5. Sağdan Sola ve Soldan Sağa Slider (Tracking/Trucking)
Görsel ve Psikolojik Etkisi: Sinematik derinliği en yüksek harekettir. Sahnenin üç boyutlu olduğu algısını güçlendirir ve mekanı tanıtır.

Etkili Olduğu Konular: Şehir caddeleri, orman içi ağaç dizilimleri, mimari cepheler, müze sergileri.

Dikkat Dağıttığı Durumlar: Ön planda odak noktasını tamamen kapatan düzensiz nesnelerin varlığı.

Kamera Başlangıç ve Bitiş Konumu: X ekseninde paralelleştirilmiş sol ve sağ uç noktalar.

Hareket Mesafesi ve Yönü: 80−200 cm yanal hareket.

Paralaks Düzeni: Kamera sağa kayarken, yakın ön plan sola hızla kayar; orta plan yavaşça kayar; uzak arka plan neredeyse sabit kalır.

Ekipman İhtiyacı: Ağır hizmet tipi slider ve motor modülü.   

Zamanlama Parametreleri: 360 kare, 5 sn interval (1800 sn) → 12 sn klip (30 fps).   

Kare Başına Hareket: 1200 mm/360=3.33 mm/kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Ön plandaki dikey çizgilerin (direk, ağaç) takılmaması (stutter) için enstantane süresi uzatılmalıdır.   

Post-Prodüksiyon İşlemleri: Ön plan ve arka plan kayma oranlarını doğrulamak, gerekiyorsa hafif düzlem düzeltmesi yapmak.

En Yaygın Hatalar ve Çözümleri: Rayların esnemesi nedeniyle merkezde çökme. Çözüm: Slider'ı çift tripod ile desteklemek.   

6. Pan (Yatay Çevrinme)
Görsel ve Psikolojik Etkisi: Çevreyi tarama, geniş ufukları keşfetme ve iki farklı odak noktasını ilişkilendirme olanağı sağlar.

Etkili Olduğu Konular: Dağ manzaraları, panoramik şehir görünümleri, samanyolu pozlamaları.   

Dikkat Dağıttığı Durumlar: Yüksek hızlı pan hareketlerinde izleyicide oluşan mide bulantısı ve görsel kargaşa.

Kamera Başlangıç ve Bitiş Konumu: Pan kafasının A 
∘
  açısından B 
∘
  açısına rotasyonu.

Hareket Mesafesi ve Yönü: Yatay düzlemde 15 
∘
 −60 
∘
  arası dönme.

Paralaks Düzeni: Saf pan hareketinde paralaks oluşmaz; tüm katmanlar eşit derece hızında döner.

Ekipman İhtiyacı: Motorlu pan/tilt kafası.   

Zamanlama Parametreleri: 300 kare, 20 sn interval (gece sahası, 6000 sn) →10 sn klip (30 fps).   

Kare Başına Hareket: 30 
∘
 /300=0.1 
∘
  / kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Dar açılı lenslerde açısal adım yüksek tutulursa kesiklik hissi oluşur. Shutter açık kalma süresi yüksek tutulmalıdır.   

Post-Prodüksiyon İşlemleri: Motion blur eklemek için RSMB (ReVision Effects RealSmart Motion Blur) eklentisi entegrasyonu.   

En Yaygın Hatalar ve Çözümleri: Derece atlaması. Çözüm: Dişli motor kontrolcülerinin kayış gerginliğini denetlemek.

7. Tilt (Dikey Çevrinme)
Görsel ve Psikolojik Etkisi: Görkem, azamet, yükseklik veya derinlik hissi yaratır. Dikey yapıları açığa çıkarır.

Etkili Olduğu Konular: Gökdelenler, şelaleler, dev kanyonlar, roket fırlatmaları.

Dikkat Dağıttığı Durumlar: Alt veya üst sınırda görsel ilginin bulunmadığı boş alanlarda uzun süre kalmak.

Kamera Başlangıç ve Bitiş Konumu: Y ekseninde −30 
∘
  'den +45 
∘
 'ye açısal değişim.

Hareket Mesafesi ve Yönü: Dikey açılanmada 30 
∘
 −75 
∘
  arası.

Paralaks Düzeni: Saf tilt hareketinde katman derinliği oluşmaz, perspektif açısı dikey deformasyona uğrar.

Ekipman İhtiyacı: Motorlu Tilt Kafası.   

Zamanlama Parametreleri: 240 kare, 3 sn interval (720 sn) → 10 sn klip (24 fps).   

Kare Başına Hareket: 45 
∘
 /240=0.1875 
∘
  / kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Yüksek dikey yapılarda gökyüzü-zemin ışık farkı çok yüksek olduğundan kademeli ND kullanımı ve pozlama ramping zorunludur.   

Post-Prodüksiyon İşlemleri: Kurguda dikey perspektif bozulmalarını (keystone) lens düzeltme panelleriyle dengelemek.

En Yaygın Hatalar ve Çözümleri: Yerçekimi nedeniyle motorun aşağı inişte ivmelenmesi, yukarı çıkışta zorlanması. Çözüm: L-braket ile kamera ağırlık merkezini (CG) tork aksına tam hizalamak.   

8. Dikey Yükselme veya Alçalma (Pedestal/Crane/Jib)
Görsel ve Psikolojik Etkisi: Sahneye kuş bakışı üstünlük sağlama veya sahneye inerek dahil olma hissi sunar.

Etkili Olduğu Konular: Orman içi ağaç gövdeleri, tarihi alanlardaki sütunlar, kalabalık etkinlik alanları.

Dikkat Dağıttığı Durumlar: Hızlı yükselmelerde ön plandaki nesnelerin kadrajı aniden tıkaması.

Kamera Başlangıç ve Bitiş Konumu: Z ekseninde yerden 30 cm yükseklikten 200 cm yüksekliğe çıkış.

Hareket Mesafesi ve Yönü: Dik eksende 100−200 cm yukarısı veya aşağısı.

Paralaks Düzeni: Yakındaki yatay yüzeyler dikey olarak hızla yer değiştirirken ufuk çizgisi yavaşça çöker veya yükselir.

Ekipman İhtiyacı: Edelkrone Vertical Module veya motorlu perfore jib sistemleri.   

Zamanlama Parametreleri: 300 kare, 4 sn interval (1200 sn) →10 sn klip (30 fps).   

Kare Başına Hareket: 1500 mm/300=5 mm/kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Dikey harekette mekanik titreşim riski yüksektir. IBIS kapatılmalı ve post stabilizasyon adımı planlanmalıdır.   

Post-Prodüksiyon İşlemleri: Z ekseni sarsıntılarını düzeltmek için DaVinci Resolve Fusion sayfasında "Planar Tracker" düğümü uygulamak.   

En Yaygın Hatalar ve Çözümleri: Dikey dikey çekimlerde motor yükünün artarak pili erken bitirmesi. Çözüm: Harici V-Mount güç kaynakları ve yaylı dengeleme mekanizmaları kullanmak.   

9. Orbit / Arc (Yörünge Hareketi)
Görsel ve Psikolojik Etkisi: Konuyu merkeze alarak üç boyutlu bir heykel gibi sergiler. Odak noktasını kutsallaştırır.

Etkili Olduğu Konular: Tekil yapılar, heykeller, yalnız ağaçlar, otomobil tanıtımları.

Dikkat Dağıttığı Durumlar: Arka planda sürekli yön değiştiren karmaşık ışıkların izleyiciyi yorması.

Kamera Başlangıç ve Bitiş Konumu: Konu etrafında 180 
∘
  veya 360 
∘
  'lik dairesel yay.

Hareket Mesafesi ve Yönü: 1−3 metre yarıçaplı dairesel hat.

Paralaks Düzeni: Ana konu kadrajın tam merkezinde çakılı kalırken, arka plan ters yönde kesintisiz akar.

Ekipman İhtiyacı: 3 Eksenli moco (Slider + Pan + Target Tracking modülü).   

Zamanlama Parametreleri: 480 kare, 5 sn interval (2400 sn) →16 sn klip (30 fps).   

Kare Başına Hareket: 90 
∘
  arc/480=0.1875 
∘
  kayma ve pan e 
s
¸
​
 le 
s
¸
​
 mesi / kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Odak noktasındaki ana konunun keskin kalması için netleme hassasiyeti ve sarsıntısız adımlama elzemdir.

Post-Prodüksiyon İşlemleri: Odak noktasının merkeze sabit kalması için kurguda "Point Stabilization" çalıştırmak.   

En Yaygın Hatalar ve Çözümleri: Kameranın merkeze olan mesafesi değiştikçe odağın kayması. Çözüm: Edelkrone Point Tracking veya sistem içi hedef kilitleme kullanmak.   

10. Parallax Hareketi
Görsel ve Psikolojik Etkisi: İki boyutlu ekranda yüksek derinlik ve hacim hissi üreterek izleyiciye üst düzey sinematik deneyim yaşatır.

Etkili Olduğu Konular: Ön planında kayalıklar veya ağaçlar olan manzara sahneleri, şehir içindeki dar sokaklar.

Dikkat Dağıttığı Durumlar: Ön plan, orta plan ve arka plan mesafelerinin birbirine çok yakın olduğu düz sahneler.

Kamera Başlangıç ve Bitiş Konumu: Slider hattı boyunca yanal hareket yaparken pan kafasının ters yönde dönmesi.

Hareket Mesafesi ve Yönü: 150 cm slider hareketi esnasında −20 
∘
  'den +20 
∘
 'ye ters pan.

Paralaks Düzeni: Ön plan elemanı (1 m mesafede) sağa kayarken, orta plandaki konu (10 m) sabit kalır, arka plan (100 m) sola kayar.

Ekipman İhtiyacı: 2 Eksenli moco (Slider + Pan Head).   

Zamanlama Parametreleri: 300 kare, 3 sn interval (900 sn) →12 sn klip (25 fps).   

Kare Başına Hareket: 1 m slider kaymasına karşılık 0.133 
∘
  ters pan / kare.

Motion Blur, Shutter, ND Filtre, Flicker et Stabilizasyon: Ön plan çok hızlı akacağından akıcılık için ND filtre ile 1 sn seviyelerinde shutter hızı kullanılmalıdır.   

Post-Prodüksiyon İşlemleri: Hızlı kayan ön planda oluşan moiré yapılarını dijital filtrelerle temizlemek.

En Yaygın Hatalar ve Çözümleri: Ön plan nesnesinin kadrajdan tamamen çıkması veya pan hızının slider hızına uyumsuzluğu. Çözüm: Başlangıç ve bitiş kadraj sınırlarını çekim öncesi test etmek ve senkronize moco algoritmalarını tercih etmek.   

11. Top-down Kamera Hareketi (Overhead/Kuş Bakışı)
Görsel ve Psikolojik Etkisi: Grafiksel, mimari ve soyut bir bakış açısı sunar. Nesnelerin düzenini ve geometrik hareketini ön plana çıkarır.

Etkili Olduğu Konular: İnsan kalabalıklarının kavşaklardaki akışı, montaj hatları, çizim/sanat süreçleri, sofra hazırlıkları.

Dikkat Dağıttığı Durumlar: Dikey doğrultuda yeterli ışık bulunmayan gölgeli ortamlarda.

Kamera Başlangıç ve Bitiş Konumu: Yüzey düzlemine 90 
∘
  dik açı ile yerleştirilmiş tepe noktası.

Hareket Mesafesi ve Yönü: Yatay düzlemde 50−100 cm aks kaydırma veya Z ekseninde dikey alçalma.

Paralaks Düzeni: Düzlem tek bir katman gibi algılandığı için paralaks düşüktür; derinlik gölgeler aracılığıyla hissedilir.

Ekipman İhtiyacı: C-Stand, rig sistemleri veya rigid tavan slider'ları.

Zamanlama Parametreleri: 400 kare, 2 sn interval (800 sn) →16 sn klip (25 fps).   

Kare Başına Hareket: 800 mm/400=2 mm/kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Yapay aydınlatmalı iç mekanlarda 1/50 sn shutter seçilerek elektrik frekans flicker'ı engellenmelidir.

Post-Prodüksiyon İşlemleri: Kadrajı tam dikey eksene getirmek için kurguda 90-180 derece döndürme ve keystone düzeltmesi.

En Yaygın Hatalar ve Çözümleri: Ekipman bükülmesi ve kameranın aşağı düşme riski. Çözüm: Çift güvenlik halatı (safety bond) ve çelik bağlantı elemanları kullanmak.

12. Makrodan Geniş Plana Geçiş (Macro-to-Wide)
Görsel ve Psikolojik Etkisi: Sürpriz ve keşif duygusu oluşturur. Küçücük bir detaydan başlayarak devasa bir dünyayı açığa çıkarır.

Etkili Olduğu Konular: Çiçek açması, böcek dünyası, saat mekanizmaları, elektronik devre üretimi.

Dikkat Dağıttığı Durumlar: Odak geçişinin çok hızlı ve sarsıntılı yapılması durumunda görsel kopukluk.

Kamera Başlangıç ve Bitiş Konumu: Başlangıç 1:1 makro mesafesi (2 cm), bitiş sahanın genel planı (3 m).

Hareket Mesafesi ve Yönü: Z ekseni doğrultusunda 100−200 cm geriye doğru çekilme.

Paralaks Düzeni: İlk milimetrelerde makro nesne kadrajı kaplarken, geri çekildikçe çevre görünür hale gelir ve devasa bir paralaks sıçraması yaşanır.

Ekipman İhtiyacı: Probe Lens (ör. Laowa Probe Lens), uzun adımlı moco slider ve uzaktan odak motoru.   

Zamanlama Parametreleri: 600 kare, 10 sn interval (6000 sn) →20 sn klip (30 fps).   

Kare Başına Hareket: İlk 10 cm'de 0.1 mm/kare (üstel/exponential ivmelenme ile sonlarda 10 mm/kare).

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Makro lensteki f/14−f/40 diyafram değerleri yüksek ışık gerektirir; güçlü sürekli ışık kullanılmalıdır.

Post-Prodüksiyon İşlemleri: Makro lensteki kenar kararmalarını (vignette) yazılımsal olarak gidermek.

En Yaygın Hatalar ve Çözümleri: Makro alanda alan derinliğinin milimetrik olması sebebiyle odağın kayması. Çözüm: Moco sistemine odak motoru entegre edip kare kare "Focus Stacking" veya senkronize odak takibi uygulamak.

13. Hyperlapse
Görsel ve Psikolojik Etkisi: Büyük mekânları ve şehirleri dinamik, adeta uçarcasına katetme hissi sunar. Enerjik ve yüksek tempolu bir anlatı dili oluşturur.

Etkili Olduğu Konular: Şehir caddeleri, uzun köprüler, mimari komplekslerin çevresi, yürüyüş yolları.   

Dikkat Dağıttığı Durumlar: Yüzeyin çok engebeli olduğu durumlarda oluşan çözülemeyen aşırı sarsıntılar.

Kamera Başlangıç ve Bitiş Konumu: Fiziksel olarak 50 m'den 500 m'ye varan uzun hat üzerinde yürüyüş konumu.   

Hareket Mesafesi ve Yönü: Her karede 1 adım (50−70 cm) ileri veya yana doğru manüel hareket.   

Paralaks Düzeni: Sabit tutulan bir "Çapa Noktası" (Anchor Point) etrafında tüm çevre aksı yüksek hızla kayar.   

Ekipman İhtiyacı: Tripod veya Monopod, monoküler hedef ızgaralı vizör.   

Zamanlama Parametreleri: 200 kare, her fotoğraf arası fiziksel 1 adım atma süresi (≈10 sn interval) →8 sn klip (25 fps).   

Kare Başına Hareket: 50 cm / kare (fiziksel adım).   

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Elde veya monopod üzerinde 1/4−1/2 sn enstantane kullanılarak adımlama sarsıntıları yumuşatılır.

Post-Prodüksiyon İşlemleri: Zorunlu işlem! DaVinci Resolve Fusion sayfasında "Planar Tracker" veya Premiere Pro "Warp Stabilizer" kullanımı.   

En Yaygın Hatalar ve Çözümleri: Çapa noktasının vizörde kayması. Çözüm: Vizör ızgarasını (Grid View) açıp odak noktasını sabit bir bina köşesine kilitli tutmak.   

14. Motorlu Motion-Control
Görsel ve Psikolojik Etkisi: Kusursuz, matematiksel, insan eli değmemiş hissi veren milimetrik hareket stabilitesi sağlar.

Etkili Olduğu Konular: Ticari reklam filmleri, yüksek bütçeli belgeseller, karmaşık görsel efekt (VFX) birleştirmeleri.   

Kamera Başlangıç ve Bitiş Konumu: Yazılım üzerinden programlanmış 3-4 eksenli uzamsal koordinatlar.   

Hareket Mesafesi ve Yönü: X, Y, Z eksenlerinde ve Pan/Tilt/Roll açılarında senkronize hareket.   

Paralaks Düzeni: Tüm eksenlerin birleşimiyle çok katmanlı ve tamamen kontrollü paralaks eğrileri üretilir.

Ekipman İhtiyacı: Edelkrone, Kessler Crane veya Ditogear çok eksenli moco rigleri.   

Zamanlama Parametreleri: Programlanan süreye bağlı olarak 500 kare, 2.5 sn interval →20 sn klip (25 fps).   

Kare Başına Hareket: Moco işlemcisi tarafından mikro adım (micro-stepping) sürücüleriyle milimetrenin 1/100'ü oranında hesaplanır.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Motorların oluşturduğu mikro-titreşimlerin (micro-vibration) sensör tarafından algılanmaması için kameradaki tüm dahili stabilizasyonlar (IBIS/OIS) KAPATILMALIDIR.   

Post-Prodüksiyon İşlemleri: Post-prodüksiyon aşamasında DaVinci Resolve Edit sayfasında "Smoothness: 10-15%" değerinde stabilizasyon uygulamak.   

En Yaygın Hatalar ve Çözümleri: Pil bitmesiyle konum hafızasının silinmesi. Çözüm: Doğrudan AC adaptör veya yüksek kapasiteli Li-ion/V-Mount blokları kullanmak.   

15. Dijital Zoom ve Post-Prodüksiyon Keyframe Hareketi
Görsel ve Psikolojik Etkisi: Pratik ama fiziksel derinliği sınırlı bir yaklaşma hissi sunar.

Etkili Olduğu Konular: Fiziksel slider kurulumunun imkansız olduğu tehlikeli veya çok dar alanlar.

Dikkat Dağıttığı Durumlar: Aşırı ölçeklemede (>120%) görüntüde oluşan belirgin pikselleşme ve detay kaybı.

Kamera Başlangıç ve Bitiş Konumu: Kurgu yazılımında 100% Scale'den 130% Scale değerine keyframe dönüşümü.

Hareket Mesafesi ve Yönü: Dijital X/Y ekseni kaydırma ve dijital kırpma (crop).

Paralaks Düzeni: Sıfır Paralaks! İki boyutlu bir fotoğraf büyütüldüğü için ön plan ve arka plan aynı oranda büyür; üç boyutlu derinlik hissi oluşmaz.

Ekipman İhtiyacı: Yüksek çözünürlüklü gövde (ör. 8K RAW veya 61 MP tam kare sensör) ve sabit tripod.   

Zamanlama Parametreleri: Sabit çekilen 300 karelik dizilim.   

Kare Başına Hareket: Dijital olarak kare başına +0.1% Scale artışı.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Çekim anında fiziksel hareket olmadığı için mekanik stabilizasyon riski yoktur; ancak dijital zoom yapıldığında sensördeki gürültü (noise) büyür.

Post-Prodüksiyon İşlemleri: Premiere veya Resolve üzerinde "Bezier" yumuşatmalı keyframe eklentileri kullanmak.

En Yaygın Hatalar ve Çözümleri: Düz hatlı hareket nedeniyle yapaylık. Çözüm: X/Y eksenlerine hafif salınım eğrileri eklemek.

16. Speed Ramp ile Timelapse Birleştirme
Görsel ve Psikolojik Etkisi: Zaman algısını kırar; dramatik anları dondurur veya aksiyonu aniden hızlandırarak yüksek tempolu bir anlatı kurar.

Etkili Olduğu Konular: Spor belgeselleri, şehirde yürüyen bir insanın aniden durması ve etrafındaki hayatın timelapse akışına geçmesi, araç lansmanları.

Dikkat Dağıttığı Durumlar: Hız geçişlerinin yumuşatılmadığı sert ve kırılmalı kesmeler.

Kamera Başlangıç ve Bitiş Konumu: 50 fps normal video kaydından, kare kare çekilen timelapse moduna geçiş.

Hareket Mesafesi ve Yönü: Sürekli olan bir slider hareketi esnasında tempo değişimi.

Paralaks Düzeni: Hızlanma esnasında ön plan akışı çizgilere dönüşürken, duraksamada netleşir.

Ekipman İhtiyacı: Tam senkronize çalışabilen yüksek hızlı moco ve video modlu kamera.

Zamanlama Parametreleri: 5 sn gerçek zamanlı video (250 kare) + 200 kare timelapse dizilimi.   

Kare Başına Hareket: Hıza bağlı olarak değişen dinamik step motor hızı.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Normal video ile timelapse karesi arasındaki örtücü (shutter) açısı ve hareket bulanıklığı tutarsızlığı yaşanabilir. Video kısmında 180 
∘
  shutter rule uygulanırken, timelapse kısmında ND filtrelerle benzer hareket bulanıklığı sağlanmalıdır.   

Post-Prodüksiyon İşlemleri: Premiere Pro'da "Time Remapping" aracını açıp "Speed Ramp Bezier Handles" ile yumuşak eğri oluşturmak.   

En Yaygın Hatalar ve Çözümleri: Geçiş anında renk kayması. Çözüm: İki modda da sabit Kelvin ve LOG renk profili kullanmak.   

17. Match Cut veya Aynı Kadraja Dönüş
Görsel ve Psikolojik Etkisi: Zamanın dönüşümünü, mevsimlerin geçişini veya restorasyon süreçlerini kesintisiz biçimde birbirine bağlayarak büyüleyici bir metamorfoz hissi sağlar.

Etkili Olduğu Konular: Aynı mekanın Yaz/Kış geçişi, Gece/Gündüz dönüşümü, inşaat başlangıcı ve bitimi.   

Dikkat Dağıttığı Durumlar: İki çekim arasındaki milimetrik kadraj kaçıklıkları (alignment error).

Kamera Başlangıç ve Bitiş Konumu: A 
konumu
​
  (Örn: 1 Ocak saat 12:00) →A 
konumu
​
  (Örn: 1 Temmuz saat 12:00).

Hareket Mesafesi ve Yönü: Birebir aynı fiziksel koordinatlar ve moco rotası.

Paralaks Düzeni: Katman sınırları her iki çekimde de %100 örtüşmelidir.

Ekipman İhtiyacı: GPS koordinatı kaydetme yeteneği olan advanced moco veya hassas lazer işaretleyicili tripod durakları.   

Zamanlama Parametreleri: Her iki oturum için de eşit kare sayısı ve eşit interval kullanımı (örneğin 300'er kare).   

Kare Başına Hareket: İki çekimde de birebir aynı milimetrik adımlama.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: İki farklı tarihteki ışık seviyeleri farklı olacağından bağımsız pozlama ramping hesaplanmalıdır.   

Post-Prodüksiyon İşlemleri: Kurguda "Difference" karıştırma modunu (blend mode) açıp iki katmanı üst üste %100 çakıştırmak, ardından zaman geçişi için "Wipe" veya "Opacity Mask" kullanmak.

En Yaygın Hatalar ve Çözümleri: Odak uzaklığı (focal length) mikro değişimi. Çözüm: Manuel lenste odak halkasını gaffer bant ile sabitlemek.   

18. Kusursuz Loop Oluşturan Kamera Hareketleri
Görsel ve Psikolojik Etkisi: Sonsuzluk, hipnotik bir ritim ve kesintisiz akış hissi yaratır. Sosyal medya ve dijital sergileme alanlarında izlenme süresini artırır.

Etkili Olduğu Konular: 24 saatlik gece-gündüz şehir akışları, dönme dolaplar, dairesel fabrika bantları.   

Dikkat Dağıttığı Durumlar: Döngü birleşim noktasında (seam) oluşan belirgin ışık veya nesne atlamaları.

Kamera Başlangıç ve Bitiş Konumu: Kare 1 ile Kare N'in görsel içerik ve konum olarak birbirini tamamladığı noktalar.

Hareket Mesafesi ve Yönü: Tam 360 
∘
  döngüsel pan veya başa dönen doğrusal hareket.

Paralaks Düzeni: Sürekli ve simetrik bir paralaks kayması olmalıdır.

Ekipman İhtiyacı: Kesintisiz döngü moduna sahip 3 eksenli moco sistemleri (ör. Edelkrone Sequencer Loop modu).   

Zamanlama Parametreleri: 24 saatlik çekimde 1440 kare (1 dk interval) → tam 360 
∘
  döngü.   

Kare Başına Hareket: 360 
∘
 /1440=0.25 
∘
  / kare.

Motion Blur, Shutter, ND Filtre, Flicker ve Stabilizasyon: Gece ve gündüz ışık farkı 15−18 stop olacağından tam otomatik Holy Grail ramping şarttır.   

Post-Prodüksiyon İşlemleri: İlk ve son 1 saniyelik bölümleri cross-dissolve ile %50 opaklıkta harmanlamak (seamless crossfade loop).

En Yaygın Hatalar ve Çözümleri: Bulutların kesme noktasında aniden sıçraması. Çözüm: Bulutsuz ve kararlı gökyüzü koşullarını tercih etmek veya maskeleme yapmak.

Derinlemesine İnceleme: İleri-Geri Simetrik Hibrit Hareket Analizi
Bu senaryoda kamera başlangıçta sabit bir geniş plandadır. Yapım veya dönüşüm süreci hızlandıkça ana nesneye doğru güçlü fakat akıcı biçimde yaklaşır (Push-in). Kritik detay gösterildikten sonra aynı rota üzerinden geriye gider (Pull-out) ve tam olarak ilk geniş kadrajına döner.

İleri-geri simetrik hareketin zaman akışında, Kare 0'da başlayan geniş plan çekimi Kare 200'e kadar ivmelenerek detay noktasına yaklaşır. Kare 200 ile 250 arasında tepe noktasında durağan olarak detay sergilenir. Kare 250'den itibaren geriye doğru ivmelenen kamera, Kare 450'de tam olarak başlangıçtaki geniş kadrajına geri döner.

Yöntemlerin Karşılaştırması
Manuel / Fiziksel Slider
Teknik Uygulanabilirlik: Zordur ve riski yüksektir. İnsan elinin her karede milimetrik olarak tam eşit adım atması imkansızdır.

Estetik Kalite: Düzensiz adım aralıkları nedeniyle final videoda sarsıntı ve akış bozukluğu (jitter) kaçınılmazdır.

Üretim Güvenliği: Düşük. Uzun çekimlerde operatör yorgunluğu tork hatasına yol açar.

Maliyet: Düşük maliyetli donanım gereksinimi.

Saha Kurulum Süresi: 15 Dakika.

Motorlu Motion-Control
Teknik Uygulanabilirlik: Mükemmel. Sistem "Keypose" noktaları (A→B→A) arasında mikro-step hassasiyetle çalışır.   

Estetik Kalite: S-Curve yumuşatma sayesinde ivmelenme ve yavaşlama sinematik akıcılık sunar.   

Üretim Güvenliği: Yüksek. Sistem tamamen otomatiktir; hata payı düşüktür.

Maliyet: Yüksek ekipman yatırımı.   

Saha Kurulum Süresi: 45 - 60 Dakika.

Post-Prodüksiyon Dijital Zoom
Teknik Uygulanabilirlik: Kolay. Sabit çekilen yüksek çözünürlüklü görüntü kurgu yazılımında işlenir.

Estetik Kalite: Düşük/Orta. Fiziksel optik yaklaşma olmadığı için paralaks etkisi ve optik perspektif değişimi oluşmaz.

Üretim Güvenliği: En yüksek (Saha riskleri minimumdur).

Maliyet: Orta (Yüksek çözünürlüklü kamera gerektirir).

Saha Kurulum Süresi: 10 Dakika.

Yöntemlerin Teknik Karşılaştırma Tablosu
Parametre    Manuel Slider    Motorlu Motion-Control    Dijital Zoom (Post)
Paralaks Etkisi    Gerçek ve dinamik    Gerçek, hassas ve kusursuz    Yok (İki boyutlu büyütme)
Tekrarlanabilirlik    %10-20 (İmkansıza yakın)    
%100 (Kodlayıcı korumalı)

%100 (Yazılımsal)
Hareket Yumuşaklığı    Düşük (Sarsıntı yüksek)    Mükemmel (Mikro adımlama)    Mükemmel (Matematiksel)
Işık Ramping Desteği    Zor    
Moco-İntervalometre entegrasyonu

Kolay (Sabit kadraj)
Stabilizasyon İhtiyacı    Aşırı yüksek    
Çok düşük (Sadece micro-vibration)

Sıfır
  
Karar Matrisleri ve Karşılaştırma Tabloları
Kamera Açıları Karar Matrisi
Kamera Açısı    Görsel ve Psikolojik Etkisi    Uygulama Alanı    Teknik Zorluk    İdeal İnterval
Geniş Açı (12-24mm)    
Derinlik hissi, mekânsal görkem, çevresel bağlam

Doğa, şehir mimarisi, samanyolu, bulutlar

Düşük / Düzensizlikleri gizler    
3 - 30 Saniye

Orta Plan (35-50mm)    Doğal insan gözü perspektifi, tarafsız anlatı    
Şantiye dönüşümleri, insan kalabalığı, sokak

Orta / Denge gerektirir    
2 - 5 Saniye

Telefoto (85-200mm)    Düzleştirilmiş perspektif, katman sıkıştırması    Batan güneş/ay takibi, uzak dağlar, detaylar    Aşırı Yüksek / Rüzgâr ve titreme riski    
1 - 3 Saniye

Düşük Açı (Low Angle)    Anıtsal güç, egemenlik, dramatik yükseliş    Gökdelenler, tarihi kuleler, fırtına bulutları    Orta / Yansıma ve ışık patlaması    
2 - 5 Saniye

Yüksek Açı (High Angle)    Düzen, minyatür etkisi, kontrol hissi    Şehir kavşakları, etkinlik alanları, limanlar    Orta / Rig sabitleme riski    
1 - 3 Saniye

Kuş Bakışı (Overhead/90°)    Soyut grafik tasvir, geometrik akış    Çizim, montaj hattı, insan sirkülasyonu    Yüksek / Dikey sabitleme ve güvenlik    1 - 2 Saniye
  
Kamera Hareketleri Karşılaştırma Tablosu
Hareket Tipi    Ana Hareket Ekseni    Ekipman İhtiyacı    Paralaks Potansiyeli    Post Stabilizasyon Yükü
Locked-off    Yok (Sabit)    
Sabit Tripod

Yok    
Yok / Minimum

Push-in / Pull-out    Z Ekseni (İleri/Geri)    
Linear Slider / Rail

Yüksek (Kenar genleşmesi)    Düşük
Tracking (Yanal)    X Ekseni (Sol/Sağ)    
Motorlu Slider

Aşırı Yüksek    Düşük / Orta
Pan / Tilt    Açısal Rotasyon    
Motorlu Kafalar (Pan/Tilt)

Yok (Sadece açı değişimi)    Düşük
Orbit (Yörünge)    X Ekseni + Pan Rotasyonu    
2-3 Eksenli Moco

Mükemmel (Katman döngüsü)    
Orta

Dikey (Pedestal)    Y Ekseni (Yukarı/Aşağı)    
Dikey Modüllü Slider / Crane

Yüksek (Ufuk değişimi)    Orta
Hyperlapse    Fiziksel Yürüyüş Aksı    
Tripod / Monopod

Aşırı Yüksek    
Aşırı Yüksek (Zorunlu)

Macro-to-Wide    Z Ekseni + Odak Aksı    
Probe Lens + Moco Slider

Dinamik sıçrama    Yüksek
  
Ekipman Seviyelerine Göre Üretim Yöntemleri ve İş Akışları
Üretim iş akışları üç ana donanım seviyesinde şekillenir:

Mobil Seviye: Smartphone + Sabit Tripod + Dahili Timelapse Uygulaması.

Prosumer Seviye: DSLR/Mirrorless + Gimbal/Manuel Slider + ND Filtre.

Profesyonel MoCo Seviyesi: Sinema Kamerası + 3-Eksenli Moco + Post Deflicker/Stabilizasyon.

Akıllı Telefon ve Tripod (Mobil Seviye)
Kurulum ve Hazırlık: Telefonu bir akıllı telefon adaptörü ile ağır bir tripoda kilitleyin.

Kamera Ayarları: Uçak modunu açın. Dahili kamera uygulamasında "Timelapse" modunu seçin veya ProCam / Filmic Pro ile Manuel Moda geçin. Odak ve Pozlamayı kilitleyin (AE/AF Lock).

Saha Çekimi: Mobil sensörlerin küçük olması sebebiyle aşırı rüzgârlı ortamlarda tripod bacaklarına ek ağırlık bağlayın.

Yazılım İşleme: CapCut veya Lightroom Mobile ile renk düzenleme yapın. Dahili dijital stabilizasyonu aktif tutun.

Kamera, Gimbal veya Manuel Slider (Prosumer Seviye)
Kurulum ve Hazırlık: Kamerayı slider üzerine yerleştirip su terazisi ile dengeleyin. Gimbal kullanılacaksa "Timelapse / Motionlapse" modunu aktif edin.

Kamera Ayarları: Tam Manuel Mod (M). Enstantane süresini intervalin yarısına (180 
∘
  kuralı) ayarlamak için uygun ND filtre (ör. ND64 veya ND1000) takın. Beyaz Dengesi (WB) Kelvin değerinde kilitlenmelidir.   

Saha Çekimi: Manuel slider kullanılıyorsa, milimetrik kılavuz çizgilerini takip ederek her interval bip sesinde eşit mesafe kaydırın. IBIS ve OIS ayarlarını tamamen kapatın.   

Yazılım İşleme: RAW fotoğrafları Lightroom Classic'e aktarın. DaVinci Resolve Edit sayfasında "Similarity" veya "Perspective" stabilizasyonu uygulayın.   

Motorlu Motion-Control Sistemi (Profesyonel MoCo Seviye)
Kurulum ve Hazırlık: Moco raylarını kurun (ör. Edelkrone SliderPLUS + HeadPLUS veya Kessler Shuttle Dolly). Sistemi balanslayın.   

Kamera Ayarları: Kamera RAW formatında ayarlanır. İntervalometer moco ana kontrolcüsüne trigger kablosu ile bağlanır.   

Programlama: Mobil uygulama üzerinden A ve B Keypose noktaları belirlenir. Duraklama (pause), ivmelenme (ease-in/out) ve interval süreleri girilir.   

Saha Çekimi: Gece-Gündüz (Holy Grail) çekimlerinde, pozlama değişimlerini yönetmek için yazılımsal ramping veya uzaktan tetikleme uygulanır.   

Yazılım İşleme: RAW veriler LRTimelapse programına aktarılır; kilit keyframe'ler düzenlenir, de-flicker eğrisi hesaplanır. Render alınan ProRes 4444 XQ görüntü DaVinci Resolve Fusion sayfasında "Planar Tracker" yardımıyla mikro titreşimlerden arındırılır.   

En Az 12 Uygulanabilir Çekim Reçetesi
Reçete 1: Şehir Silüetinde Gece Trafiği ve Işık İzleri
Konu: Yoğun şehir içi kavşak ve köprü trafiği.   

Açı: Düşük Açı, Geniş Açı (20 mm).

Hareket: Yanal Slider Hareketi (Tracking, Soldan Sağa 120 cm).

Süre / İnterval: 300 Kare, 3 sn İnterval (Çekim: 15 dk, Final: 10 sn @ 30 fps).   

Ekipman: Tam Kare Kamera, ND8 Filtre, Motorlu Slider.   

Kurgu / Post: LRTimelapse De-flicker, DaVinci Resolve Color Grade.   

Riskler ve Çözümler: Farların aşırı pozlanması. Çözüm: Histogramı kontrol edip enstantaneyi 1.5 sn seviyesinde tutmak.   

Reçete 2: Tarihi Kule Üzerinde Bulut Akışı
Konu: Tarihi saat kulesi ve arkasındaki hızlı bulut geçişleri.   

Açı: Düşük Açı, Orta Plan (35 mm).

Hareket: Dikey Yükselme (Pedestal) ve Eşzamanlı Tilt Up.   

Süre / İnterval: 240 Kare, 2 sn İnterval (Çekim: 8 dk, Final: 10 sn @ 24 fps).   

Ekipman: Kamera, Dikey Modüllü Slider, ND64 Filtre.   

Kurgu / Post: Speed ramp ile bulut hareketini kurguda vurgulama.   

Riskler ve Çözümler: Dikey yük nedeniyle kayış kayması. Çözüm: Yaylı dengeleme modülü kullanmak.   

Reçete 3: Dağ Zirvesinde Samanyolu Doğuşu
Konu: Gece dağ zirvesi ve Samanyolu galaktik merkez hareketi.   

Açı: Yüksek Açı, Ultra Geniş Açı (14 mm f/1.8).

Hareket: Yörünge (Orbit / Arc) ile Ön Plan Kayasını Merkezde Tutma.   

Süre / İnterval: 300 Kare, 25 sn İnterval (Çekim: 125 dk, Final: 10 sn @ 30 fps).   

Ekipman: Yüksek ISO Yetenekli Kamera, 3 Eksenli Moco, Lens Isıtıcı (Buğu önleyici).   

Kurgu / Post: Astro-de-noise (Sequator/SiriL), DaVinci Resolve Fusion Yıldız Sabitleme.

Riskler ve Çözümler: Lensin çiğlenmesi. Çözüm: USB destekli lens ısıtıcı kuşak bağlamak.

Reçete 4: Şantiye / Bina İnşaatı Transformation
Konu: Çelik konstrüksiyon bina montajı.   

Açı: Genel Açı (24 mm).

Hareket: Symmetrical Push-Pull (Genişten Odak Noktasına Yaklaşma ve Dönüş).

Süre / İnterval: 600 Kare, 30 sn İnterval (Çekim: 5 Saat, Final: 20 sn @ 30 fps).   

Ekipman: Hava Koşullarına Dayanıklı Kamera, Şebeke Güç Adaptörü, Moco Slider.   

Kurgu / Post: Deflicker, Uzun süreli gün ışığı değişim kurgusu.   

Riskler ve Çözümler: Güneş açısının değişmesiyle oluşan sert gölgeler. Çözüm: Bulutlu günleri seçmek veya uzun interval ortalaması almak.

Reçete 5: Şehir Meydanında Gün Doğumu (Holy Grail)
Konu: Karanlık şehirden aydınlık gün ışığına geçiş.   

Açı: Yüksek Açı, Geniş Plan (24 mm).   

Hareket: Parallax Hareketi (Slider Sağa + Pan Sola).   

Süre / İnterval: 500 Kare, 4 sn İnterval (Çekim: 33 dk, Final: 20 sn @ 25 fps).   

Ekipman: Kamera, LRTimelapse PRO Timer, 2-Eksen Moco.   

Kurgu / Post: LRTimelapse Holy Grail Wizard ile Otomatik Pozlama Ramping Geçişi.   

Riskler ve Çözümler: Pozlama basamaklarında diyalog atlaması (flicker). Çözüm: LRTimelapse ile Holy Grail kilit karelerini düzeltmek.   

Reçete 6: Botanik Bahçesinde Çiçek Açma (Bloom)
Konu: Erotik bir çiçeğin katman katman açılması.   

Açı: Makro Açı (100 mm Makro).

Hareket: Makrodan Geniş Plana Yavaş Çekilme (Macro-to-Wide Pull-out).

Süre / İnterval: 720 Kare, 60 sn İnterval (Çekim: 12 Saat, Final: 24 sn @ 30 fps).   

Ekipman: Stüdyo Sürekli LED Aydınlatma, Makro Moco Slider.   

Kurgu / Post: Focus stacking entegrasyonu ve dijital keskinleştirme.

Riskler ve Çözümler: Çiçeğin ortam neminden dolayı titremesi. Çözüm: İklim kontrollü kapalı stüdyo ortamı oluşturmak.   

Reçete 7: Şehir Caddesinde Uzun Mesafe Hyperlapse
Konu: 300 metrelik alışveriş caddesinde insan ve mimari akışı.   

Açı: Göz Hizası, 24 mm Geniş Açı.   

Hareket: İleri Doğru Yürüyüşlü Hyperlapse.   

Süre / İnterval: 250 Kare, Her 1 adımda (60 cm) 1 kare.   

Ekipman: Kamera, Heavy-Duty Monopod, Lazer Mesafe Ölçer.   

Kurgu / Post: Premiere Pro Warp Stabilizer (%10 Smoothness) veya DaVinci Resolve Planar Tracker.   

Riskler ve Çözümler: Yaya trafiğinin kameranın önüne geçmesi. Çözüm: Sakin adımlarla ilerlemek veya yüksek monopod/tripod kullanmak.   

Reçete 8: Sahil Şeridinde Sis ve Deniz Dalgaları
Konu: Dalgakıran kayalıkları ve üzerini kaplayan sis tabakası.

Açı: Düşük Açı, 50 mm Orta Plan.

Hareket: Yanal Slider Hareketi (Soldan Sağa 100 cm).

Süre / İnterval: 300 Kare, 1 sn İnterval (Çekim: 5 dk, Final: 10 sn @ 30 fps).   

Ekipman: ND1000 Filtre (2 sn enstantane için), Motorlu Slider.   

Kurgu / Post: Düz deniz çizgisini korumak için Horizon Stabilize.

Riskler ve Çözümler: Dalga serpintisinin lense gelmesi. Çözüm: Lens siperliği ve koruyucu UV filtre kullanmak.

Reçete 9: Müze İçi Heykel Sergisi
Konu: Antik mermer heykel ve etrafından geçen ziyaretçiler.

Açı: Göz Hizası, 35 mm.

Hareket: 180 
∘
  Tam Dairesel Orbit.   

Süre / İnterval: 360 Kare, 3 sn İnterval (Çekim: 18 dk, Final: 12 sn @ 30 fps).   

Ekipman: 3 Eksenli Moco (Point Tracking modlu).   

Kurgu / Post: İnsan silüetlerini dinamik tutmak için motion blur optimizasyonu.

Riskler ve Çözümler: Müze ışıklarının frekans Flicker'ı. Çözüm: Enstantane süresini 1/50 sn PAL elektrik frekansına eşitlemek.

Reçete 10: Havalimanı Pistinde Uçak İniş-Kalkışları
Konu: Uçakların arka arkaya iniş yapması ve pist ışıkları.   

Açı: Telefoto Açı (135 mm).

Hareket: Sabit Kadraj (Locked-off) + Post-Prodüksiyon Keyframe Pan.   

Süre / İnterval: 400 Kare, 2 sn İnterval (Çekim: 13.3 dk, Final: 16 sn @ 25 fps).   

Ekipman: Ağır Tripod, Kum Torbaları, Uzaktan Kumanda.   

Kurgu / Post: Post kurguda dinamik dijital pan ve hızlandırma (speed ramp).   

Riskler ve Çözümler: Rüzgâr ve jet motoru titreşimi. Çözüm: Tripodu en alt seviyede tutmak.

Reçete 11: Endüstriyel Mutfak Şefi Hazırlık Süreci
Konu: Şefin karmaşık bir tabağı hazırlama aşamaları.

Açı: Tam Kuş Bakışı (90 
∘
  Overhead, 28 mm).

Hareket: Yukarıdan Dikey Alçalma (Pedestal Down).

Süre / İnterval: 300 Kare, 2 sn İnterval (Çekim: 10 dk, Final: 12 sn @ 25 fps).   

Ekipman: C-Stand Rig, Tavan Slider'ı, LED Panel.   

Kurgu / Post: Renk doygunluğunu gıda odaklı vurgulama.

Riskler ve Çözümler: Yemek buharının lense katman oluşturması. Çözüm: Yandan küçük bir fan ile buharı tahliye etmek.

Reçete 12: Stüdyo Araç Lansmanı Metamorfozu
Konu: Otomobil üzerindeki örtünün kalkması ve ışık şovları.

Açı: Düşük Açı Geniş Plan (18 mm).

Hareket: Push-in + Eşzamanlı Pan/Tilt Senkronize Moco.   

Süre / İnterval: 240 Kare, 1 sn İnterval (Çekim: 4 dk, Final: 8 sn @ 30 fps).   

Ekipman: Tam Senkron Yüksek Hızlı Moco Rig.   

Kurgu / Post: Match cut ile farklı renk seçeneklerini aynı hareket çizgisine kurgulamak.

Riskler ve Çözümler: Yansımalı araba yüzeyinde moco gölgesi. Çözüm: Dairesel Polarize (CPL) filtre kullanmak ve ışıkları yumuşatmak.   

Ne Zaman Kullanılmalı ve Ne Zaman Kullanılmamalı?
Locked-off
Kullanılmalı: Gökyüzünde radikal bulut değişimleri, Samanyolu çekimleri, aşırı rüzgârlı ve mekanik sistemlerin sallanacağı zirveler.   

Kullanılmamalı: Ön planın ve arka planın tamamen durağan olduğu, kadraj içi hiçbir hareketin bulunmadığı sahnelerde.

Push-in / Pull-out
Kullanılmalı: Odak noktasını izleyiciye hissettirmek, bir mekâna giriş yapmak veya mekândan vedalaşarak ayrılmak istendiğinde.

Kullanılmamalı: Ön planda görüntüyü dikey olarak tamamen bükebilecek ve kadrajı tıkayacak geniş engeller varsa.

Yanal Slider (Tracking)
Kullanılmalı: Ön plan, orta plan ve arka plan derinliğine sahip zengin mimari ve doğa sahnelerinde (Paralaks üretmek için).

Kullanılmamalı: Derinliği olmayan dümdüz duvar veya uzak deniz ufku çekimlerinde (Paralaks oluşmaz, vakit kaybıdır).

Hyperlapse
Kullanılmalı: Şehir içinde uzun mesafeler katetmek ve izleyiciye aksiyon dolu sinematik bir yürüyüş deneyimi sunmak için.   

Kullanılmamalı: Zemin yapısının çamur, kayalık veya aşırı engelli olduğu ve adım doğruluğunun sağlanamadığı alanlarda.   

Motorlu Motion-Control
Kullanılmalı: Yüksek bütçeli, milimetrik tekrarlanabilirlik gerektiren, VFX eşleşmesi yapılacak veya 3 eksenli hassas paralaks istenen sahnelerde.   

Kullanılmamalı: Lojistik olarak ulaşımın çok zor olduğu ekstradan ağırlık taşınamayacak dağ tırmanışlarında.

Kadrajlama ve Format Stratejileri: 16:9 Yatay ve 9:16 Dikey En-Boy Oranları
Günümüz dijital yayıncılık standartlarında aynı çekimin hem geleneksel sinematik (16:9) hem de dikey sosyal medya (9:16) platformlarında kullanılması gerekmektedir. 16:9 formatı geniş bir yatay görüş alanı sağlarken, 9:16 dikey format dar bir koridorda merkezi odaklanmayı zorunlu kılar.

16:9 Yatay Format Kadraj Önerileri
Yanal Alan Kullanımı: Altın oran (1/3 kuralı) doğrultusunda konuyu sağ veya sol dikey çizgiye yerleştirip hareket yönünde boşluk bırakın.

Paralaks Genişliği: Yatay eksende geniş slider hareketleri (120−200 cm) kullanarak sağ ve sol kenarlardan giren ön plan elemanlarını katmanlaştırın.   

Ufuk Çizgisi: Gökyüzü etkileyici ise ufuk çizgisini alt 1/3'e, zemin detaylı ise üst 1/3'e konumlandırın.

9:16 Dikey Format Kadraj Önerileri
Merkezi Odaklama (Center Framing): Dikey formatta kenarlar daraldığı için ana konuyu kadrajın tam orta dikey aksına sabitleyin.

Dikey Derinlik Kullanımı: Yatay slider hareketi yerine Tilt (Dikey Çevrinme) veya Pedestal (Dikey Yükselme) hareketlerini tercih edin. Bu sayede gökyüzünden zemine uzanan dikey paralaks hattı oluşturulur.   

Güvenli Alan (Safe Zone): Mobil arayüz butonlarının (beğeni, yorum, açıklama) görüntüyü kapatmaması için alt %20 ve üst %15'lik kısımlarda kritik detay bulundurmayın.

Ortak Çekim Metodu (Görsel İçerik Üretimi İçin)
Kamerayı 8K RAW (veya minimum 6K) çözünürlükte yatay olarak çekin. Moco sisteminde dikey pan hareketi tanımlamadan önce, kurgu yazılımında 1080×1920 dikey sekans açıp ana konuyu ortalayacak biçimde dijital pan/crop uygulayın. 8K çözünürlük, kalite kaybı olmadan dikey kesim yapılmasına olanak tanır.   

Anlatı Akışına Göre Hareket Seçenekleri
Başlangıç (Açılış / Estetik Bağlam)
Açılış sahnelerinin temel amacı izleyiciye mekanı tanıtmak ve atmosferi hissettirmektir.

İdeal Hareket 1: Geniş Plan Pull-out. Konuya yakın bir detaydan geriye doğru açılarak tüm coğrafyayı veya şehri ortaya çıkarmak.

İdeal Hareket 2: Yanal Parallax Hareketi (Slow Tracking). Ön plandaki nesnelerin arkasından kayarak sinematik bir giriş yapmak.   

Açı Tercihi: Göz Hizası veya Hafif Yüksek Açı.

Orta Süreç (Gelişme / Dönüşüm ve Eylem)
Zamanın akışının, değişimin, inşaatın veya iklim dönüşümünün gösterildiği ana gövde.

İdeal Hareket 1: Symmetrical Push-Pull. Dönüşümün en yoğun olduğu anlarda nesneye odaklanıp kritik aşama bitince tekrar açılmak.

İdeal Hareket 2: Speed Ramp Destekli Motorlu Pan/Tilt. Aksiyonun hızlandığı yerlerde ivmelenen moco hareketi.   

Açı Tercihi: Düşük Açı (Dramatik hissi artırmak için) veya Orta Plan.

Final Reveal (Sonuç / Kapanış ve Görkem)
Anlatının sonlandığı, üretilen eserin veya son durumun büyüleyici biçimde sergilendiği an.

İdeal Hareket 1: Orbit / Arc (360° Yörünge). Tamamlanan yapıyı veya konuyu merkezde tutup etrafında dönerek görkemli bir veda sunmak.   

İdeal Hareket 2: Pedestal Up + Tilt Down (Yükselerek Bakış). Kameranın dikey olarak gökyüzüne yükselirken aşağıya, ana konuya bakması.   

Açı Tercihi: Yüksek Açı veya Kuş Bakışı (Overhead).

Sonuç ve Sektörel Tavsiyeler
Motion-control timelapse çekimlerinde başarı, matematiksel planlama, doğru ekipman seçimi ve post-prodüksiyon disiplininin eksiksiz uygulanmasına bağlıdır.

Saha operasyonlarında görsel stabiliteyi korumak adına kamera sensör veya lens stabilizasyonlarının (IBIS/OIS) kesinlikle kapatılması gerekmektedir. Mikro titreşimler, fiziksel tork ayarları ve stabilizasyon gereksinimleri post-prodüksiyon aşamasında profesyonel yazılımlarla (DaVinci Resolve veya Adobe Suite) çözülmelidir.   

Çekimler esnasında 180 
∘
  shutter kuralına sadık kalınarak doğal hareket bulanıklığı (motion blur) elde edilmeli, gün geçişlerinde ise pozlama sapmalarını engellemek amacıyla LRTimelapse ve entegre intervalometre sistemleriyle çalışılmalıdır. Bu teknik gereksinimler doğru estetik açılarla birleştirildiğinde, izleyiciyi yormayan, son derece akıcı ve sinematik motion-control timelapse yapımları elde edilecektir.
