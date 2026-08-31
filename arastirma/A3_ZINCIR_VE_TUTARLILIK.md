# 🔗 A3 — ZİNCİR VE TUTARLILIK  ⭐ EN YÜKSEK KALDIRAÇ

```
AMAÇ      On sahnede AYNI binayı, AYNI kamera istasyonundan, AYNI hızda
          üretmenin ÇALIŞAN yöntemini bulmak.
KARŞILIĞI İki film de aynı sebepten düştü:
            ② İNŞA 0,0/10 · HÜKÜM FARKLI — "her kesmede taşıyıcı sistem,
              yük yolu ve ölçek değişiyor"
            ⑤ DEVAMLILIK 0,0/10 · 9 dikişin 9'u DEFECT ·
              "AYNI YER OLDUĞUNU KANITLAYAN NESNE: BULUNAMADI"
            ① VANTAGE GROUPS = 8 (plan 2 diyordu) — kamera her klibin İÇİNDE
              sabit (10/10) ama klipler ARASINDA istasyon yeniden doğuyor
            ③ TIME RATE 0/10 — "bulutlar timelapse hızında koşarken tabliyedeki
              işçiler ve kamyonlar gerçek zamanlı hızda hareket ediyor"
DÖNÜŞÜ    KILAVUZ_REHBERI §8 (ters inşa) · araclar/zincir_kontrol.sh ·
          PROMPT_SABLONU · DERS 5 · 12 · 15
```

⛔ **Bu bir prompt yazma sorunu değil, üretim hattı sorunudur.** Metin kapısı
iki kez de GO verdi ve film iki kez de düştü. Bu prompt "daha iyi prompt nasıl
yazılır" diye SORMUYOR; "hangi araç, hangi ayarla, kaç karede tutuyor" diye
soruyor.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden

Sen üretken görüntü/video modelleri üzerine çalışan, üretim hattı kuran bir
teknik araştırmacısın. Görevin en iyi modeli övmek değil, **hangi aracın neyi
tuttuğunu, hangi parametreyle ve hangi ölçülmüş zaafla** yazmak.

## BAĞLAM — çözmen gereken tam problem

```
ÜRETİLEN   9:16 dikey, konuşmasız, AI ile üretilmiş inşaat timelapse filmi.
           10 sahne × ~6 sn. Her sahne, aynı inşaatın farklı bir AYINI gösterir.

MUTLAK KISIT — üçü de aynı anda tutulmalı:
  ① AYNI BİNA      On sahnede tamamlanacak yapı AYNI yapıdır: aynı kat sayısı,
                   aynı oturum, aynı aks düzeni, aynı cephe, aynı çekirdek yeri.
                   Sahneden sahneye yalnız İNŞA AŞAMASI ilerler.
  ② AYNI KAMERA    On sahnede kamera istasyonu birebir aynıdır: aynı lens,
                   aynı yükseklik, aynı mesafe, aynı bakış açısı, tilt 0°.
                   Ufuk çizgisi her karede kare yüksekliğinin tam %50'sinde.
                   Arka plandaki üç çapa (komşu bina · tek ağaç · sırt hattı)
                   her karede aynı yerde, aynı genişlikte.
  ③ AYNI HIZ       Klibin İÇİNDE her şey aynı hızlandırılmış tempoda hareket
                   eder: bulut, gölge, makine, İNSAN ve ARAÇ. Hiçbir şey
                   gerçek zamanlı hareket etmez.

ÖLÇÜLEN ARIZALAR — üçü de gerçek üretimde oldu:
  A. Kareler bağımsız üretildiği için 10 klipte 8 farklı kamera istasyonu
     doğdu; arka plan dağ silueti, yol güzergâhı ve ağaçlar her kesmede değişti.
  B. Taşıyıcı sistem her kesmede değişti (gri panel cephe → tamamen cam giydirme
     → farklı oturumlu koyu kule).
  C. Model gökyüzünü hızlandırdı, YERİ hızlandırmadı: bulut çizgi olurken
     işçiler ve kamyonlar normal hızda hareket etti; bazı karelerde işçiler
     bütün klip boyunca donuk poz tuttu.
  D. Vinç kancası ve halatı troleyden koptu (fiziksel olarak bağlantısız
     çizildi) ve vinç TİPİ sahne arasında değişti.

DENENEN VE YETMEYEN ÇÖZÜM: Her promptta "YAPI BIBLE" bloğunu birebir tekrar
etmek. Metin denetimi geçti, üretim yine tutmadı. Yani sorun metinde DEĞİL.
```

## GÖREV — sekiz soru, sırayla

### 1. ⭐ ÖZNE TUTARLILIĞI — bir MİMARİ ÖZNEYİ 10 üretim boyunca tutmak
Bugün itibarıyla hangi görüntü modelleri/özellikleri **aynı binayı** ardışık
üretimlerde koruyabiliyor? En az şunları ayrı ayrı değerlendir ve bulduğun
başkalarını ekle:

```
· Google Gemini görüntü modelleri (Nano Banana / Nano Banana Pro dahil)
· Black Forest Labs FLUX.1 Kontext (dev · pro · max)
· Midjourney — omni-reference (--oref / --ow) ve style reference (--sref)
· ByteDance Seedream / SeedEdit
· Qwen-Image-Edit
· OpenAI görüntü üretimi/düzenleme
· Stable Diffusion + ControlNet (depth · canny · lineart · softedge)
· IP-Adapter / InstantID benzeri referans enjeksiyonu
· Tek özne üzerinde LoRA eğitimi (DreamBooth benzeri)
```

Her biri için tabloya:
```
· sürüm + tarih
· NEYİ tutuyor (geometri · malzeme · renk · oran · kadraj)
· NEDE kayıyor — kullanıcıların belgelediği ölçülmüş zaaflar
· TAM PARAMETRE ADLARI ve tipik değerleri
· kaç ardışık düzenlemeden sonra bozulma başlıyor (belgelenmişse)
· fiyat / erişim (API · abonelik · yerel çalıştırma)
· ⛔ MİMARİ özne için kanıt var mı? Karakter yüzü için çalışan bir yöntem
     binada da çalışmayabilir — bunu ayrıca sorgula.
```

### 2. ⭐⭐ KAMERA İSTASYONUNU KİLİTLEMEK — asıl soru
Aynı kamera açısını 10 üretim boyunca korumanın yolları neler? En az şu dört
yaklaşımı karşılaştır ve başka varsa ekle:

```
(a) ZİNCİRLİ img2img — her kare bir öncekinin karesinden türetilir
(b) SABİT PLAKA + INPAINT — tek bir "usta plaka" üretilir; her sahnede yalnız
    DEĞİŞEN BÖLGE (inşaat alanı) maskelenip yeniden üretilir, arka plan ve
    gökyüzü dokunulmadan kalır
(c) GEOMETRİ ÖNCÜLÜ — bir 3B proxy sahne (Blender / SketchUp) kurulur, kamera
    orada kilitlenir, her aşamanın derinlik/kenar haritası dışa aktarılır ve
    ControlNet ile giydirilir
(d) TEK KARE + VİDEO MODELİ — tek bir başlangıç karesinden uzun bir klip
    üretilip parçalara bölünür
```

Her yaklaşım için: **nerede tutar, nerede kopar, maliyeti ne, kaç adım sürer,
hangi araçla yapılır ve bunu GERÇEKTEN yapmış birinin yazısı/videosu var mı.**

⭐ Özellikle (b) üzerinde dur: inşaat timelapse'inde arka planın %70'i hiç
değişmiyor. Maskeli yeniden üretim bu türde uygulanmış mı? Hangi araç maskeli
düzenlemede arka planı BİREBİR koruyor (piksel düzeyinde), hangisi tüm kareyi
yeniden çiziyor? Bu ayrım kritik — belgeli cevap ver.

### 3. VİDEO MODELLERİ — sabit kamera ve kadraj sadakati
Görüntüden videoya (I2V) modellerini şu ölçütlerle karşılaştır:

```
· giriş karesinin KADRAJINI koruyor mu, yoksa kaydırıyor/yakınlaştırıyor mu
· "kamera hareketsiz" talimatına uyuyor mu — ölçülmüş kanıt
· İLK KARE + SON KARE (keyframe) girişi destekliyor mu   ⭐ bizim için kritik
· klip süresi seçenekleri · çözünürlük · 9:16 desteği
· fiyat (klip başına) · API erişimi
· timelapse/hızlandırılmış hareket talimatına tepkisi
```
En az şunları kapsa ve yenilerini ekle: Kling · Google Veo · Runway Gen-4 ·
MiniMax/Hailuo · ByteDance Seedance · Alibaba Wan · OpenAI Sora · Luma Ray ·
Pika. Her biri için sürüm ve tarih yaz.

⭐ "İlk kare + son kare" desteği bizde şu işe yarar: S3'ün onaylı karesi ile
S4'ün onaylı karesi arasında geçiş üretilebilir ve zincir kopamaz. Hangi model
bunu gerçekten yapıyor, kaç saniyeye kadar, ve iki kare arasındaki fark BÜYÜK
olduğunda (bir kat daha yükselmiş bina) ne oluyor?

### 4. ⭐ AYNI HIZ PROBLEMİ — bulut hızlı, insan gerçek zamanlı
Bu, belgelenmiş ve tekrar eden bir arıza. Araştır:
- Video modellerinde "her şey aynı hızlandırılmış tempoda" talimatının
  tutmadığına dair başka örnekler ve kullanıcı raporları var mı?
- Bunu ÇÖZEN prompt formülasyonları belgelenmiş mi? Varsa **TAM İNGİLİZCE
  METNİYLE** getir.
- ⭐ ALTERNATİF YOL: klibi NORMAL hızda üretip kurguda zaman haritalamasıyla
  (time-remap) hızlandırmak. Bu türde uygulanmış mı? 6 saniyelik bir çıktı için
  kaç saniyelik ham üretim gerekir? Kare enterpolasyonu (frame interpolation)
  ile birleştirilmiş örnekler var mı? Hangi araç?
- İnsan/araç sayısını azaltmanın bozulmayı azalttığına dair kanıt var mı?
- "Hareket bulanıklığı" (motion blur) ve "ışık izi" (light trail) talimatları
  modeli timelapse moduna sokuyor mu — ölçülmüş fark var mı?

### 5. KÜÇÜK VE İNCE NESNELER — vinç kancası, halat, iskele
Modellerin ince/uzun/hareketli nesnelerde (kablo, halat, kanca, korkuluk,
iskele borusu) bozulduğuna dair belgelenmiş bulgular ve **azaltma teknikleri**.
- Nesneyi kadraj dışında bırakmak dışında çalışan bir yöntem var mı?
- Negatif prompt bu tür arızada işe yarıyor mu — ölçüm var mı?
- Çözünürlüğü artırmak ince yapıyı düzeltiyor mu?

### 6. ⭐ KAYMAYI OTOMATİK ÖLÇMEK — kapı kurmak için
İki kare arasındaki kadraj/geometri kaymasını **komut satırından** ölçmenin
yolları. Bizde zaten bir kabuk betiği var; onu güçlendirmek istiyoruz.
Şunları somut tarif ve kod/komut düzeyinde getir:

```
· ufuk çizgisi yüzdesinin kareden ölçülmesi (kenar tespiti · Hough dönüşümü)
· arka plan çapasının genişlik/konum farkı (öznitelik eşleme: ORB/SIFT +
  homografi tahmini — OpenCV ile)
· maskeli SSIM / PSNR: yalnız DEĞİŞMEMESİ GEREKEN bölgeyi karşılaştırmak
· gömme temelli benzerlik (CLIP · DINOv2) — eşik değerleri ne olmalı
· hazır araçlar var mı (timelapse hizalama, deflicker, kamera sabitleme)
```
Her yöntem için: **hangi arızayı yakalar, hangi arızayı KAÇIRIR ve pratik
eşik değeri ne olmalı.** Eşik değeri bilinmiyorsa "eşik ölçülmemiş" yaz.

### 7. GERÇEKTEN YAPMIŞ OLANLAR — boru hattı çıkar
AI ile inşaat/büyüme/dönüşüm timelapse'i üretmiş kişilerin yazı, video veya
paylaşımlarını bul. Her biri için **adım adım boru hattını** çıkar:
hangi model → hangi parametre → hangi ara adım → hangi kurgu aracı.
Neyi çözememişler, neyi bırakmışlar? En az 5 gerçek örnek.

⭐ Bitişik alanlardan da bak: aynı sorunun çözüldüğü yerler — mimari
görselleştirme (aynı bina, farklı aşama), ürün fotoğrafı tutarlılığı,
sanal prodüksiyon plaka çalışmaları, çizgi film arka plan tutarlılığı.

### 8. MALİYET VE SÜRE TABLOSU
Bulduğun her boru hattı için 10 karelik zincirli bir sekans + 10 klip video
üretmenin tahmini maliyetini ve süresini yaz. Tahminse "tahmin" yaz ve neye
dayandığını söyle.

---

## ⭐ ZORUNLU SON ÜÇ BÖLÜM

### KARAR TABLOSU
```
AMAÇ                          | ARAÇ + SÜRÜM | TAM PARAMETRE | ÖLÇÜLEN ZAAF | KAYNAK
aynı bina 10 karede           |              |               |              |
aynı kamera istasyonu         |              |               |              |
arka planı birebir korumak    |              |               |              |
her şeyi aynı hızda oynatmak  |              |               |              |
ince nesneyi bozmadan çizmek  |              |               |              |
kaymayı otomatik ölçmek       |              |               |              |
```

### ÖNERİLEN BORU HATTI — tek tane, adım adım
Bütün bulgulara dayanarak **tek bir** boru hattı öner. "Duruma göre" deme;
bir tanesini seç ve neden onu seçtiğini yaz. Adımları numarala, her adımda
hangi araç ve hangi ayar olduğunu yaz, her adımın maliyetini yaz ve
**hangi adımın en kırılgan olduğunu** açıkça söyle.

### KOPYALANABİLİR PROMPT PARÇALARI
Bulgularından çıkan, İngilizce, kopyalanıp yapıştırılabilir prompt cümleleri.
En az şu dördü için:
```
· kamera istasyonu kilidi (POZİTİF ve ÖLÇÜLEBİLİR yazılmalı — "no zoom" gibi
  bir YASAK değil; bizde ölçüldü ki yasak tutmuyor, ölçülebilir çapa tutuyor:
  "the buttress occupies exactly the same width of the frame at both ends of
  the shot, and the horizon stays at exactly half the frame height throughout"
  — bu kalıp bir üretimde 10/10 tuttu, bu yüzden kalıp korunacak)
· tek hız cümlesi (bulut · gölge · makine · insan · araç aynı tempoda)
· arka plan çapası tarifi (aynı nesneyi HER promptta AYNI kelimelerle)
· vinç yük yolu (kanca yüklü ve düşey, ya da kadraj dışı)
```
Her parçanın yanına hangi modelde çalıştığı belgelenmişse yaz.

---

## 📏 KAYNAK VE YAZIM SÖZLEŞMESİ — beşi de zorunlu

```
① ETİKET     [ÖLÇÜLDÜ] rakam/ekran görüntüsü/karşılaştırma var · [İDDİA]
             satıcı ya da blog söylüyor, kanıt yok · [VARSAYIM] senin çıkarımın
             ⛔ Etiketsiz cümle yazma.
② SÜRÜM      Her araç adının yanına SÜRÜM ve TARİH. Bu alan aylık değişiyor;
             tarihsiz bir araç adı altı ay sonra yanlış bilgidir.
③ SATICI     Satıcının kendi tanıtım metnini ÖLÇÜM sayma. Bağımsız
             karşılaştırma, kullanıcı raporu veya kendi testin varsa öyle işaretle.
④ ÇELİŞKİ    İki kaynak çelişiyorsa ikisini de yaz, ortalama ALMA.
⑤ BOŞLUK     Bilmediğine "BİLİNMİYOR" yaz. ⛔ "En iyisi X" deme — neyi, hangi
             ölçütte, hangi ölçümle daha iyi yaptığını yaz.
```

**Format:** Tablo ağırlıklı. Rapor Türkçe; araç adları, parametre adları ve
prompt metinleri İngilizce/orijinal. Uzunluk sınırı yok.
