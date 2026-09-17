# 🏗️ YAPI TİPİ KARTLARI

> Her kart bir yapının **gerçek inşa sırasını** verir. Aşama merdiveni
> (`KILAVUZ_REHBERI §4`) bu sıradan türer — uydurulmaz. Bir aşamayı yanlış
> sıraya koymak, izleyicinin adını koyamadığı ama hissettiği sahteliktir.
>
> Kart formatı sabittir: **İNŞA SIRASI · SÜRE · MAKİNE · DİKEY KADRAJ ·
> DİRENÇ ADAYLARI · RİSK**.

---

## 1. 🏢 ŞEHİR İÇİ KULE ⭐ REFERANS KART

```
İNŞA SIRASI (9 adım → 6 sahneye indirilir)
  ① yıkım / arsa temizliği          ② fore kazık + iksa perdesi
  ③ hafriyat (çukur derinleşir)     ④ radye temel dökümü
  ⑤ bodrum katlar + çekirdek başlar ⑥ kule vinci kurulur, karkas kat kat
  ⑦ çekirdek karkası geçer          ⑧ cephe aşağıdan yukarı sarılır
  ⑨ vinç sökülür, çevre düzenlenir

SÜRE          14-30 ay · tipik kat döngüsü 5-7 gün/kat
MAKİNE        fore kazık makinesi · ekskavatör · beton pompası · kule vinci
              (kendini yükselten) · mobil vinç (kurulum ve söküm için)
DİKEY KADRAJ  ⭐ EN İYİ EŞLEŞME. Yapı kadrajın boş üst kısmına doğru büyür.
              Kamera mesafesi = son yükseklik × 1,4 (§KAMERA_ISTASYONU §3)
DİRENÇ        dar parsel · komşu binaya sıfır · trafik · zemin suyu · yükseklik
RİSK          ⛔ kat yüksekliği kayıyor (kat sayısı artarken kat hizası
                 değişirse bina büyümüyor, ŞİŞİYOR gibi görünür)
              ⛔ vinç kadrajın üstünü keser — vinç boyu plana yazılır
              ⛔ cephe "aniden" bitiyor: cephe SARILIR, aşağıdan yukarı,
                 sınırı yatay bir hat olarak görünür

6 SAHNEYE İNDİRME (varsayılan)
  S0 ①      arsa (ters açılışta bina buradan sökülür)
  S1 ②③④   çukur + donatı + temel
  S2 ⑤⑥    çekirdek + ilk 4 kat + vinç
  S3 ⑥⑦    kat yığılması (kar altında)
  S4 ⑧      cephe sarılıyor, vinç sökülüyor
  S5 ⑨      teslim, akşam, ışıklar kat kat yanıyor
```

---

## 2. 🏘️ KONUT BLOĞU / SİTE

```
İNŞA SIRASI   arsa → temel (birden çok blok aynı anda) → karkas 5-8 kat →
              tuğla duvar → sıva/boya → çatı → peyzaj + havuz + yol
SÜRE          12-20 ay
MAKİNE        mobil vinç · beton pompası · küçük kule vinci · forklift
DİKEY KADRAJ  orta — yapı alçak, kadrajın üstü boş kalır. Çözüm: kamerayı
              alçalt (0,9 m) ve öne al; bloklar ÜST ÜSTE binerek derinlik verir
DİRENÇ        çok bloklu eşzamanlılık · çamur · mevsim
RİSK          ⛔ bloklar birbirinin kopyası olur ve model onları karıştırır —
                 her bloğa AYIRT EDİCİ bir işaret ver (farklı cephe rengi,
                 farklı çatı yönü) ve değişmezlere yaz
```

---

## 3. 🌉 KÖPRÜ (kablo askılı / kemer)

```
İNŞA SIRASI   ① kesonlar / kazıklar suya-zemine iner  ② ayaklar yükselir
              ③ pilonlar (kuleler) yükselir           ④ tabliye iki yakadan
              dengeli konsol olarak ilerler            ⑤ kablolar gerilir
              ⑥ ⭐ ORTA AÇIKLIK KAPANIR                ⑦ asfalt + korkuluk
SÜRE          3-5 yıl
MAKİNE        yüzer vinç · form traveller (konsol arabası) · kablo germe ekipmanı
DİKEY KADRAJ  ⚠️ ZORLU — köprü yatay bir yapıdır. İki çözüm:
              (a) kamerayı köprü EKSENİNE koy: tabliye izleyiciye doğru gelir,
                  dikey kadraj derinlik kazanır
              (b) tek pilonu özne yap: pilon dikeydir ve dikey kadrajı doldurur
DİRENÇ        ⭐ boşluk · rüzgâr · su · gelgit · iki yakanın buluşması
RİSK          ⛔ orta açıklık kapanışı filmin FİNAL VURUŞUDUR — S5'te ekranda
                 görülmüyorsa film teslim edilmemiştir (§8 adım 9)
              ⛔ model konsolu "havada yüzen tabliye" olarak çizer; her promptta
                 yük yolu yazılır: "supported continuously back to the pylon"
```

---

## 4. 🌊 BARAJ / HES

```
İNŞA SIRASI   ① derivasyon tüneli açılır  ② nehir saptırılır, yatak kurur
              ③ temel kayaya kadar kazılır ④ gövde blok blok yükselir
              ⑤ dolusavak + kapaklar       ⑥ ⭐ GÖLET DOLAR — vadi su altında
SÜRE          4-6 yıl
MAKİNE        kablolu vinç (cableway) · dev damper · beton santrali · delici
DİKEY KADRAJ  iyi — baraj gövdesi vadi içinde dikey bir duvardır
DİRENÇ        ⭐ nehrin kendisi · vadi eğimi · kış
BEDEL         ⭐ HAZIR: vadi, ağaçlar, eski yol su altında kalır. Bu türün
              içinde bedelin kendiliğinden var olduğu tek yapı budur
RİSK          ⛔ su seviyesi kademeli yükselir, bir sahnede DOLMAZ
              ⛔ kuru yatak ile dolu gölet arasında arka plan çapaları
                 kısmen su altında kalır — hangi çapanın kalacağı plana yazılır
              ⛔ İLK KALDIRMA HAVUZ OKUNUR [DERS 54]: nehir yatağındaki alçak
                 düz platform + ıslak parlak üst yüzey + kenarda su = "basin".
                 İlk kaldırma karesi KURU · MAT · KATLI (lift lines) yazılır;
                 su platformun yanından değil TÜNELDEN geçer.
              ⛔ KADRAJDA KÖPRÜ/YOL VARSA makine oraya kaçar [DERS 51]: iş
                 yüzeyi "the top of the dam lift at N percent" diye adlanır,
                 köprü "stays empty" diye pozitif boş yazılır.
```

---

## 5. 🏟️ STADYUM

```
İNŞA SIRASI   hafriyat çanak → temel → prekast tribün halkası → çelik çatı
              halkası yerde birleştirilip KALDIRILIR → membran → koltuklar → çim
SÜRE          2-3 yıl
MAKİNE        çok sayıda mobil vinç · strand jack (çatı kaldırma)
DİKEY KADRAJ  zayıf — stadyum geniş ve alçaktır. Kamerayı YÜKSELT (30-60 m,
              komşu bina çatısı) ve aşağı bak; çanak dikey kadrajda oval okunur
DİRENÇ        açıklık · çatının ağırlığı · takvim (turnuva tarihi)
RİSK          ⛔ çatı kaldırma anı tek seferliktir ve filmin doruğudur; ayrı
                 sahne olarak yazılır, başka aşamayla aynı klibe sıkıştırılmaz
```

---

## 6. 🛣️ YOL / TÜNEL

```
İNŞA SIRASI   güzergâh temizliği → yarma/dolgu → alt temel → sanat yapıları
              (menfez/viyadük) → bitümlü tabaka → çizgi ve bariyer
TÜNEL         portal → TBM veya patlatma → püskürtme beton → kaplama → aydınlatma
SÜRE          1-3 yıl · 4 SAHNELİK varyant için ideal
MAKİNE        greyder · silindir · finişer · TBM
DİKEY KADRAJ  ⚠️ zor — yol yataydır. Çözüm: yolu izleyiciye DOĞRU gelen bir
              çizgi olarak kadraja al (tek nokta perspektifi), dikey kadraj
              derinliği taşır
DİRENÇ        eğim · kaya · kar · heyelan
```

---

## 7. ⚓ LİMAN / DALGAKIRAN

```
İNŞA SIRASI   deniz dibi taraması → çekirdek taş dökümü → tetrapod/blok yerleşimi
              → rıhtım kesonları → üst yapı → vinç rayları
SÜRE          2-4 yıl
DİKEY KADRAJ  orta — dalgakıran ufka doğru uzayan bir çizgidir; kamerayı kıyıdan
              çizgiye bakacak şekilde kur
DİRENÇ        ⭐ deniz · fırtına · gelgit — direnç görsel olarak KENDİNİ gösterir
RİSK          ⛔ dalga hareketi 10 saniyelik timelapse'te sisli bir düzlüğe
                 dönüşür; bu doğrudur ve istenir — "silky smoothed sea" yazılır
```

---

## 8. 💨 RÜZGÂR TÜRBİNİ (4 sahnelik ideal aday)

```
İNŞA SIRASI   ① platform + temel dökümü  ② kule segmentleri üst üste
              ③ nasel kaldırılır         ④ kanatlar takılır, döner
SÜRE          6-10 hafta · ⭐ 4 × 10 = 40 sn varyantı için en temiz vaka
MAKİNE        800 tonluk paletli vinç (kendisi de bir olaydır)
DİKEY KADRAJ  ⭐ mükemmel — türbin saf dikeydir
DİRENÇ        rüzgâr (montaj rüzgârda durur) · uzaklık · yükseklik
FİNAL VURUŞ   ilk dönüş. S3'ün son iki saniyesinde kanat döner.
RİSK          ⛔ ÇOĞALIR [DERS 55]: "wind turbine" korpusu çiftliktir; tek yazılsa da yanına
                 türbin gelir (THE EMPTY RIDGE 0:39, dört mercek). Etraf pozitif boş yazılır:
                 "the only turbine on the ridge … every other crest bare"; günlükte kule sayımı.
              ⛔ ROTOR ERKEN DÖNER [DERS 56]: montajda "hub is turned" yazma — rotor işletme
                 hızında döner, kanatlar dönen göbeğe sıçrar. Göbek KİLİTLİ; dönüş yalnız finalde.
              ⛔ KALDIRMA POP EDER [DERS 57]: segment · nasel · kanat havada taşınmaz, hedefte
                 belirir, kanca boş kalır — dağ arka planı da kurtarmadı. Kaldırma karede biter:
                 G(n) yük hedefin üstünde asılı, klip yalnız oturur; her kaldırma bir ara kare.
              ⭐ 7 SAHNEYE AÇILMIŞ HÂLİ: dikey_shorts/THE_EMPTY_RIDGE/ (yol · temel · bom + seg 1 ·
                 seg 2–4 · nasel+göbek · 3 kanat · vinç çıkar + ilk dönüş).
```

---

## 9. 🏡 VİLLA / TEK EV (4 sahnelik)

```
İNŞA SIRASI   temel → karkas → çatı → duvar/pencere → sıva-boya → peyzaj
SÜRE          8-12 ay
DİKEY KADRAJ  zayıf tek başına — çözüm: kamerayı YAKIN kur (18-25 m) ve evi
              kadrajın alt yarısına otur, üst yarıyı gökyüzü ve ağaca bırak;
              mevsim değişimi ağaçta okunur
DİRENÇ        küçük ölçekte direnç zayıftır — SAHA'dan gelmelidir (eğim, kar, kıyı)
```

---

## 9b. 🌾 KAYAR KALIPLA SİLO / BACA / ŞAFT 🆕 17.09.2026

```
İNŞA SIRASI   ① dairesel kazı + radye dökümü (starter bar bırakılır)
              ② kayar kalıp halkası kurulur: şut panelleri + yoke + kriko +
                 tırmanma çubuğu + asılı iskele + üst çalışma platformu
              ③ ⭐ KESİNTİSİZ DÖKÜM — kalıp gece gündüz tırmanır (≈ 3-4 m/gün)
              ④ tepede kalıp sökülür, kriko ve çubuklar alınır
              ⑤ üst yapı (başlık / makine katı) vinçle oturur
              ⑥ yan ekipman (elevatör muhafazası, boru, merdiven) bağlanır
              ⑦ apron + çevre betonu, sonra ilk işletme
SÜRE          şaftın kendisi 8-12 gün · toplam 2-4 ay
MAKİNE        beton pompası · mikser · malzeme asansörü · mobil vinç (yalnız üst yapı)
DİKEY KADRAJ  ⭐ EN İYİ ADAYLARDAN BİRİ — yapı saf dikeydir VE kalıp kendisi
              9:16'nın eksenini yukarı süpürür (kadraj içi kinetik ② bedava gelir)
⭐ İKİ TERS SÜPÜRME  kalıp YUKARI çıkarken, altındaki taze/kürlenmiş beton sınırı
              gövdeye göre AŞAĞI iner. Aynı klipte zıt yönde iki hareket; A9-b'nin
              kürlenme takvimi bunun sözlüğüdür. ⇒ MALZEME_VE_DOKU §4
DİRENÇ        kürlenme hızı (kalıp betondan hızlı çıkarsa duvar yırtılır) ·
              kesintisiz döküm zorunluluğu · hasat/işletme penceresi · rüzgâr
FİNAL VURUŞ   ilk ürünün ALINMASI — ⛔ yapının DOLMASI değil [P3-d]
RİSK          ⛔ ÇOĞALIR [DERS 55]: "silo" korpusu DİZİDİR. Tek yazılsa da yanına
                 silo gelir. Üç katlı savunma: pozitif sayım cümlesi + "ufuk
                 gövdenin iki yanında da görünür" yerleşimi + araç kapısında SAYIM TESTİ.
              ⛔ KALIP İSKELE OKUNUR: "scaffold" demek kalıbı iskeleye çevirir.
                 Halka olarak yazılır: "a continuous ring of shutter panels clamped
                 round the wall on its yokes, with jacks on the climbing rods".
              ⛔ AKIŞ GÖRÜNMEZ [P3-d]: kapalı düzenekten tahıl/malzeme akışı
                 istenmez; kaynak ağzı ve düştüğü kap aynı kadrajda olmalı.
              ⛔ EŞİK ERKEN GEÇİLİR [P3-g]: "kule şu yapıyı geçer" olayı merdivene
                 yazılmadan önce KADRAJDAKİ hiza hesaplanır — alçak istasyonda
                 komşu yapılar ufkun altındadır ve eşik ilk üçte birde geçilir.
7 SAHNEYE EŞLEME  S0 zemin bozulur · S1 radye · S2 kalıp + ilk tırmanış ·
              S3 tırmanış · S4 gövde tamam + yan ekipman · S5 kalıp sökülür +
              üst yapı · S6 apron kapanır + ilk ürün
⭐ İLK UYGULAMA  dikey_shorts/THE_LAST_CIRCLE/ (17.09.2026 · tahıl silosu · ova)
```

---

## 10. 🆕 YENİ YAPI TİPİ ŞABLONU

```
İNŞA SIRASI   [gerçek sıra — uydurma. Kaynak: yapının kendi mühendislik sırası]
SÜRE          [ay/yıl + varsa döngü hızı]
MAKİNE        [ekranda görünecek olanlar]
DİKEY KADRAJ  [iyi/orta/zor + çözüm]
DİRENÇ        [en az üç aday]
RİSK          [modelin bu yapıda ne bozacağı]
6 SAHNEYE İNDİRME  [S0-S5 eşlemesi]
```
