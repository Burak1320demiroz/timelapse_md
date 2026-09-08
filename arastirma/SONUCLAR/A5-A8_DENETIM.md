# 🔍 A5–A8 DENETİMİ — dört raporun doğruluk teyidi

> Kart S §2 (etiket) · §3 (çelişki) · §4 (iki rapor) uygulanmıştır.
> Ham dosyalar: `A5_GEMINI_HAM.md` · `A6_…` · `A7_…` · `A8_…` (08.09.2026)
>
> ⛔ Bu dosya raporları DEĞİŞTİRMEZ. Ham çıktı kanıttır ve dokunulmamıştır.
> ⭐ Bu dosyadaki "ÖLÇTÜM" satırları **bu depoda, bu makinede** hesaplanmış ya
>    da ffmpeg ile koşulmuştur. Rapordan gelen hiçbir sayı ölçülmüş sayılmaz.

---

## 0. DÖRDÜNÜN ORTAK KUSURU

```
O1  TEK BOT. Dördü de Gemini Deep Research'e koşuldu. Kart S §4'ün istediği
    çelişki görünürlüğü YOK. A1–A4'te de böyleydi; ikinci zayıflık üst üste
    biniyor.

O2  ⛔ ÇÖZÜMLENEBİLİR KAYNAK YOK. Dört raporun hiçbirinde tek bir URL, DOI,
    belge adı + bölüm numarası yok. A8 metin içinde [cite: 2, 3] gibi
    işaretler taşıyor ama kaynak listesi GELMEDİ — işaretler çözümlenemiyor.
    ⭐ Kart S §2'nin mantığı: etiket bulguyu değil KAYNAĞI ölçer. Kaynağı
       gösterilemeyen [ÖLÇÜLDÜ] etiketi en fazla [İDDİA] taşır.
    ⇒ Aşağıda ✅ verdiğim her madde ya bir MEKANİZMA (kaynak gerektirmez,
      mantığı kendi içinde denetlenebilir) ya da BEN ÖLÇTÜM.

O3  ETİKET-KAYNAK ÇİFTLERİ TUTMUYOR. "[VARSAYIM] (araç dokümanı)",
    "[VARSAYIM - akademik]" gibi kombinasyonlar var. VARSAYIM botun kendi
    çıkarımıdır; kaynak sınıfı taşıyamaz. A7'de 3, A8'de 5 yerde.
```

---

## 1. A5 — İNŞA YÖNTEMİ · **en güçlü rapor**

### ✅ Ayakta kalan
```
A5+1  ARA HÂL MERDİVENİ. On üç eleman × %25/%50/%75 × görünür fark.
      Dördünün en sağlam işi. Mekanizma denetlenebilir: her ara hâl bir
      GEÇİCİ EKİPMANLA tanımlanmış (kalıp · iskele · dikme · sapan · kür
      örtüsü), yani "beliren" değil "yapılan" hâl.
A5+2  EN KÜÇÜK İŞ KANITI ÜÇLÜSÜ: gergin vinç sapanı · toz bulutu · ıslak
      beton parlaklığı. Üçü de fiziksel, uzaktan okunur ve POZİTİF yazılabilir.
      ⭐ Bu üçlü doğrudan ⑧ APPEARED'in panzehiri.
A5+3  AY TARAFINDA TRL AYRIMI YAPILMIŞ. BEAM/TransHab (uçmuş donanım) ile
      biyomimetik robot sürüsü (laboratuvar) ayrı etiketlenmiş — istenen buydu.
A5+4  "Atmosfer olmadığı için toz parabol çizip hemen düşer" — fizik doğru.
```

### ⛔ Düşen / düzeltilen
```
A5-X1  ASTM A325 · ASTM A490 "yürürlükte" diye anılıyor.
       Bu iki standart 2015'te ASTM F3125 altında birleştirildi (F3125
       Grade A325 / Grade A490). Standart adı ESKİ.
       ⭐ EKRANA ETKİSİ YOK: görsel sonuç (gergin sapan + kaynak kıvılcımı)
          civata standardından bağımsız. Kılavuza standart adı yazılmaz.

A5-X2  "EN 13830 kurulum dizgisi sabittir" — YANLIŞ ATIF.
       EN 13830 bir ürün/performans standardıdır; montaj sırası şart koşmaz.
       Sıra (mullion → transom → yalıtım → cam) doğru bir SAHA PRATİĞİDİR.
       ⇒ Sıra alınır, standart atfı alınmaz.

A5-X3  "ASTM D698, 20 cm gevşek tabaka ve %95 sıkışmayı EMREDER" — YANLIŞ ATIF.
       D698 laboratuvar Proctor DENEYİDİR; saha tabaka kalınlığını ve %95
       hedefini şartnameler yazar, D698 yalnız yoğunluk referansını verir.
       ⇒ 20 cm tabaka + silindir izi görsel olarak alınır, atıf alınmaz.

A5-X4  ACI 318-19 "%70-85 dayanım" ve TBDY 2018 "αs ≥ 0,75" — DOĞRULANMADI.
       İkisi de tek kaynaksız sayı. Bizim için önemsiz: ekrana inen sonuç
       (başlık bölgesinde ışık geçirmeyen donatı yoğunluğu) sayıdan bağımsız.

A5-X5  ⭐ ÖLÇTÜM — KADRAJ HESABI DÜŞTÜ.
       Rapor: "9:16 dikey, 40 m, 24 mm eşdeğeri ≈ 10-15 katlı bina yüksekliği".
       Hesap (24 mm eşd. = 73,7° uzun kenar FOV, 40 m):
           kadraj = 33,7 m GENİŞ × 60,0 m YÜKSEK · 1920 px'te 32,0 px/m
       60 m = 3 m'lik katla YİRMİ kat. Rapor kadrajı %30-50 DAR sanıyor.
       ⇒ Yapı bible'ının kaç kat sığdığı bu sayıdan yazılır, rapordan değil.

A5-X6  ⭐ ÖLÇTÜM — "GÖRÜNMEZ" LİSTESİ SAYISIZ VE BİR YERİ YANLIŞ.
       Aynı hesapla 40 m'de piksel karşılıkları:
           insan 1,8 m           → 57,6 px    GÖRÜNÜR
           ekskavatör 6 m        → 192   px    tartışmasız
           kat yüksekliği 3 m    →  96   px    tartışmasız
           kalıp panosu 0,6 m    →  19   px    şekil olarak okunur
           donatı çapı 0,1 m     →   3   px    görünmez
       ⇒ OKUNABİLİRLİK EŞİĞİ ≈ 0,5 m. Bundan küçük nesne prompta YAZILMAZ.
       ⛔ Ve raporun ima ettiğinin aksine İNSAN 40 METREDE GÖRÜNÜR.
          İnsanı yok eden mesafe değil, ZAMAN SIKIŞTIRMASIDIR — bu A6'nın işi.

A5-X7  Ay tarafında "APEX tipi robotik matkap" geçiyor. Bu ad bizim depo
       adımızla çakışıyor ve doğrulanamadı — kılavuza alınmıyor.
```

---

## 2. A6 — ŞANTİYE HAREKETİ · **aritmetiği doğru, fiziği bir yerde yanlış, kendi içinde çelişkili**

### ✅ Ayakta kalan
```
A6+1  ⭐ ÖLÇTÜM — SIKIŞTIRMA ARİTMETİĞİ TUTUYOR. Dört satırın dördü:
          2 sn @30fps →   60x        (rapor 60)   ✅
         10 sn @30fps →  300x        (rapor 300)  ✅
         60 sn @24fps → 1440x        (rapor 1440) ✅
        180 sn @30fps → 5400x        (rapor 5400) ✅
      9 saatlik iş günü / 6 sn klip = 5400x · 30 fps'de kare başına 180 sn. ✅
A6+2  YÜZEY KANITI LİSTESİ. İz · çamurun kuruması · eksilen malzeme istifi ·
      hortum/kablo güzergâhı · gece kıvılcımı. Bu liste ① SURFACE TRUTH 0 ve
      ⑦ PARKED arızalarımızın doğrudan karşılığı.
A6+3  AY: regolit kohezyonu 0,1-1 kPa ve rüzgârsızlık nedeniyle izlerin
      günlerce kalması literatürle uyumlu; mertebe makul.
A6+4  ⭐ Raporun kendi teşhisi doğru: model gökyüzünü sıkıştırıp yeri
      sıkıştırmıyor. Bu bizim DERS 15'imizin birebir aynısı — dışarıdan doğrulama.
```

### ⛔ Düşen / düzeltilen
```
A6-X1  ⭐⭐ ÖLÇTÜM — GÖLGE DÖNÜŞ SAYISI YANLIŞ. En ağır hata.
       Rapor: "Güneş saatte 15° hareket eder → 9 saatte gölge 135° döner"
       ve bunu [ÖLÇÜLDÜ · Fizik] diye etiketliyor.
       15°/saat SAAT AÇISIDIR (hour angle), AZİMUT DEĞİL. Azimut hızı enleme
       ve mevsime göre değişir. 40°N için hesapladım (öğle ortalı 9 saat):
           ekinoks        gölge dönüşü 150,2°   öğle civarı en hızlı 23,1°/sa
           yaz gündönümü  gölge dönüşü 190,7°   öğle civarı en hızlı 46,3°/sa
           kış gündönümü  gölge dönüşü 115,9°   öğle civarı en hızlı 15,3°/sa
       ⇒ Rapor yazın %30 EKSİK, kışın %16 FAZLA söylüyor ve öğle civarındaki
         hızlanmayı (yazın 3 katı) hiç görmüyor.
       ⭐ Bu bizim için kritikti: DERS 32'nin (gölge süpürmesi üçüncü kez
         üretilmedi) sayısal karşılığı buradan gelecekti ve gelen sayı yanlıştı.

A6-X2  ⛔ İÇ ÇELİŞKİ — RAPOR KENDİ TABLOSUNU YALANLIYOR.
       Tablo 2, 5400x'te "insan ve araç TAMAMEN KAYBOLUR" diyor.
       §4'teki yedi ACTIVITY promptunun YEDİSİ de "motion streak" hâlinde
       ekskavatör, kamyon, işçi istiyor. İkisi aynı klipte olamaz.
       Dahası: 180 sn aralıkla çekilen bir karede "long exposure motion
       streak" fiziksel olarak imkânsızdır (gündüz 180 sn pozlama yok).
       ⇒ ÇÖZÜM BİZİM: sıkıştırma rejimi KLİP BAŞINA seçilir ve beyan edilir;
         hareket kanıtı ile yüzey kanıtı aynı rejimden türer.

A6-X3  ŞANTİYE ENVANTERİ SAYILARI KAYNAKSIZ. "2 × 20 t ekskavatör, 5 damper,
       17-22 kişi, 26,5 dk döngü" [ÖLÇÜLDÜ] etiketli ama tek bir belge adı yok.
       Mertebe makul, SAYI kullanılamaz. Kılavuza "aşama başına 2-3 hareket
       kaynağı" gibi mertebe iner, adet inmez.

A6-X4  "Marangoni etkisiyle malzemenin vakum altında yukarı tırmanması" —
       bağlam dışı ve doğrulanamadı. Alınmıyor.

A6-X5  Apollo DDE "100 µg/cm²/yıl" doğrulanmadı. Mertebe makul; ekrana inen
       sonuç (donanım üstünde koyulaşan ince toz) sayıdan bağımsız.
```

---

## 3. A7 — ARAÇ PROFİLİ · **tek en değerli bulgu burada, ama envanteri delik**

### ✅ Ayakta kalan
```
A7+1  ⭐⭐ EN DEĞERLİ BULGU: KLİP SÜRELERİ KUTULU (binned).
      Araçlar serbest süre vermiyor; 4/6/8 ya da 5/10 gibi kutulara yuvarlıyor.
      Bu, on klibin ONUNUN da 6,0 sn çıkmasını AÇIKLIYOR.
      ⭐ ÖLÇTÜM — ve suçu araçtan alıyor:
        plan 6·4·6·4·6·6·8·4·6·10 (toplam 60 sn), {4,6,8} kutusuyla:
            6←6  4←4  6←6  4←4  6←6  6←6  8←8  4←4  6←6  10←kutuya sığmıyor
            atılacak: 0 sn — DOKUZ SAHNE TAM OTURUYOR
        {5,10} kutusuyla: 25 sn atmak gerekir ama yine ÜRETİLEBİLİR.
      ⇒ Plan üretilebilirdi. ⑥ METRONOM ARACIN DEĞİL, KURGUNUN arızası.

A7+2  NEGATİF SIZMASININ MEKANİZMASI DOĞRU. "no" görsel karşılığı olmayan bir
      sözdizimi öğesidir; yanındaki isim tokeni yüksek ağırlıkla aktive olur.
      Ayrı negatif alan CFG'de vektör olarak ÇIKARILIR, metin içi negatif
      çıkarılmaz — eklenir. ⭐ Bu bizim DERS 33'ümüzü dışarıdan doğruluyor.

A7+3  YETERLİLİK PROTOKOLÜ UYGULANABİLİR: tek prompt · 5 klip · 5 ölçüm
      (süre · kamera kayması · gölge açısı farkı · sızma · prompt tavanı).
      Bizim araç kapımızın (⑴süre ⑵kamera ⑶gölge) eksik dördüncü ve beşinci
      sorusunu veriyor.

A7+4  "Her klip I2V uzatma ile beslenmelidir; T2V'de kamera kilidi imkânsıza
      yakındır." Bizim §8 zincir yöntemimizin dışarıdan doğrulanması.

A7+5  Test klibi promptu kullanılabilir hâlde ve kasten tuzaklı yazılmış
      (metin içi negatif + prompt sonuna gizlenmiş bayrak nesnesi). İyi iş.
```

### ⛔ Düşen / düzeltilen
```
A7-X1  ⛔ KAPSAM DELİĞİ. Sorulan 11 aracın DÖRDÜ her sütunda BİLİNMİYOR:
       Runway Gen-4 · ByteDance Seedance · MiniMax/Hailuo · Pika.
       Gen-4 adıyla soruldu, rapor Gen-3 Alpha'yı anlattı.
       ⇒ ARAÇ KARTLARI dosyası rapordan DOLDURULAMAZ; boş kart + ölçüm
         yordamı olarak açılır.

A7-X2  ⛔ TARİHLER GÜVENİLMEZ. "Kling 2.1 · Erken 2026", "Runway Gen-3 Alpha ·
       Nisan 2025", "Veo 3.1 · Aralık 2025" — üçü de bildiğimle çelişiyor
       (Kling 2.1 2025 ortası, Gen-3 Alpha 2024 ortası, Veo 3.1 2025 sonbaharı).
       Sürüm+tarih ISTENMIŞTI ve gelen alan çürük.
       ⇒ Araç kartındaki TARİH alanı rapordan doldurulmaz; ÜRETİM GÜNÜ elle yazılır.

A7-X3  ⚠️ "Runway Gen-3 Alpha ayrı negatif alan destekler" [ÖLÇÜLDÜ].
       Bildiğimle çelişiyor: Gen-3 için resmî yönlendirme negatiften kaçınıp
       pozitif betimlemektir; ayrı negatif alan Gen-2 dönemine ait.
       ⇒ Doğrulanmadan kullanılmaz. Araç kartında ÖLÇÜLEREK doldurulur.

A7-X4  ⚠️ "Veo negatif = metin içi" [VARSAYIM · araç dokümanı].
       Bildiğimle çelişiyor: Veo çağrısında `negativePrompt` AYRI bir
       parametredir. Rapor hem kaçırmış hem etiketi tutarsız vermiş.

A7-X5  ⛔ "%85 sızma" · "%80+ önlenir" — [ÖLÇÜLDÜ · akademik] etiketli,
       hiçbir çalışma adı yok. Uydurulmuş hassasiyet imzası.
       ⇒ MEKANİZMA iner, SAYI inmez.

A7-X6  ⚠️ "T5-XXL 512 token = 2.000-2.500 karakter" model bağımlıdır
       (kimi DiT 226, kimi 512). CLIP'in ünlü 77 token sınırı hiç anılmamış.
       ⇒ Sayı inmez; "prompt tavanı ARAÇ BAŞINA ÖLÇÜLÜR" kuralı iner.

A7-X7  ⛔ DEPOMUZLA ÇATIŞMA: rapor "2.000 karakterin altı daha iyi" diyor;
       DERS 2 bu depoda "bu türün görsel prompt bandı 4.500-5.500 karakter"
       diye ÖLÇÜLDÜ. Kart S §3 kılavuzun ölçülmüş bulguya yenilmesini ister —
       ama A7'nin bulgusu kaynaksız, DERS 2 bu depoda ölçüldü.
       ⇒ ⛔ KILAVUZ DEĞİŞMEZ. Araç kartına "prompt tavanı" satırı eklenir.
```

---

## 4. A8 — KURGU VE TESLİM · **komutları koşturdum: dördü çalıştı, ikisi kör**

### ✅ Ayakta kalan
```
A8+1  ⭐ ÖLÇTÜM — KOMUTLAR GERÇEKTEN KOŞTU (ffmpeg 8.1, sentetik 60 sn teslim):
        [2] ffprobe format=duration            → 60.000000     ✅
        [3] ffprobe stream=r_frame_rate        → 30/1          ✅
        [4] ffmpeg -af ebur128=peak=true       → I: -22.0 LUFS ✅
            ⚠️ "I:" satırı Summary BLOĞUNDADIR; `tail` ile kaçar,
               `grep -A8 Summary` ile okunur. Raporun okuma tarifi eksik.
        [6] ffmpeg -sseof -0.05 -frames:v 1    → son.jpg 8769 bayt ✅
A8+2  ⭐ ÇELİŞKİYİ ORTALAMAMASI. LUFS, gamma ve dosya boyutu satırlarında
      "ÇELİŞKİ / BİLİNMİYOR" yazmış, iki değeri yan yana bırakmış.
      Kart S §4'ün istediği tam olarak budur. Dört raporun en disiplinli yeri.
A8+3  BAŞ/SON KIRPMA MANTIĞI SAĞLAM: üretilen klibin ilk ve son kareleri
      morfolojik olarak oynak; 10-15 kare atılır.
A8+4  DİKİŞ EŞLEME YORDAMI (yalnız X/Y ötelemesi, rotasyon ve zoom KAPALI)
      bizim sabit istasyon değişmezimizle uyumlu.
```

### ⛔ Düşen / düzeltilen
```
A8-X1  ⭐⭐ ÖLÇTÜM — KOMUT 5 RAPORDAKİ HÂLİYLE HİÇBİR ŞEY BASMIYOR.
         ffmpeg -i in.mp4 -vf signalstats -f null - 2>&1 | grep "Parsed_signalstats"
       → eşleşen satır sayısı: 0.
       Doğrusu: -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF"
       ⇒ Rapordan komut kopyalayan biri "flicker yok" sanırdı.

A8-X2  ⭐⭐ ÖLÇTÜM — KOMUT 1'İN EŞİĞİ BİZİM FORMATTA KÖR.
       Sentetik teslim: 10 klip, sabit kadraj, aynı yapı, yalnız aşama
       ilerliyor; plan ızgarası 6·4·6·4·6·6·8·4·6·10; kesmeler 6/10/16/20/
       26/32/40/44/50 sn.
           eşik 0.40 (A8'in önerdiği) → 0 kesme buldu
           eşik 0.30 (bizim kesme_kontrol.sh) → 0 kesme buldu
           eşik 0.20 · 0.10 · 0.05    → 0 kesme buldu
       Kare kare ölçtüğümde gerçek dağılım:
           KESME karelerinde scene_score  0,01629 – 0,02217
           KLİP İÇİ en yüksek scene_score 0,00538   (ortanca 0,00006)
       ⇒ Ayrım VAR (3 kat marj) ama eşik 15-25 KAT fazla yazılmış.
       ⛔ Yani ⑥ METRONOM kapımız bugün AÇIK SANILIYORDU, KAPALIYDI.

A8-X3  ⭐ ÖLÇÜLMÜŞ ÇÖZÜM — EŞİK YERİNE TOP-N.
       Plandaki kesme sayısı kadar EN YÜKSEK skoru al, zaman damgalarını
       planla karşılaştır. Mutlak skor ölçeğinden bağımsızdır.
       Sentetikte 9 kesmenin 9'unu da ±0,05 sn içinde buldu. TAM İSABET.
       ⭐ İkinci bağımsız dedektör olarak YDIF de ayırıyor:
         kesmelerde 1,66-2,26 · klip içi en yüksek 0,54.

A8-X4  ⛔ "%18,7 tekrar izlenme artışı" — [ÖLÇÜLDÜ · bağımsız karşılaştırma]
       etiketli, çalışma adı yok. Uydurulmuş hassasiyet. Düşer.

A8-X5  ⛔ "Son kart 2-3 sn ideal · 5 sn Auto-Play Killer" — kaynaksız.
       Bizim kapak kartımız 5,0 sn, yani bu bulgu doğrudan formatımıza dokunuyor.
       ⇒ Kaynaksız olduğu için KILAVUZ DEĞİŞMEZ (A1-a ile aynı muamele).
         Yayından sonra kanalın kendi tutunma eğrisiyle ölçülür.

A8-X6  ⚠️ "Instagram profil ızgarası 1:1 kırpar" — bildiğimle çelişiyor;
       ızgara 4:5'e geçti. Kapak güvenli alanı 1:1'e göre kurulursa gereksiz
       daralır. Doğrulanmadan kılavuza inmez.

A8-X7  ⭐ ÖLÇTÜM — KIRPMA BÜTÇESİ SÜRE PLANINI VURUYOR (rapor bunu görmüyor).
       30 fps'de iki uçtan 10-15 kare = 0,67-1,00 sn.
           6 sn üretimden geriye 5,00-5,33 sn kalır.
       ⇒ 6,0 sn TESLİM etmek için 8 sn (Veo tipi) ya da 10 sn (Kling tipi)
         ÜRETMEK gerekir. Bunu ne A7 ne A8 söylüyor; İKİSİ BİRLEŞİNCE çıkıyor.
```

---

## 5. ÇELİŞKİLER — yan yana, ortalanmadan [kart S §4]

```
Ç1  A5 ↔ A6 · İNSAN
    A5'in döşeme promptu: "workers are actively laying down wire mesh".
    A6'nın tablosu: yüksek sıkıştırmada insan tamamen kaybolur.
    ⛔ ORTALAMA YOK. İkisi de doğru — FARKLI REJİMLERDE.
    ⇒ Rejim klip başına seçilir ve beyan edilir. İş kanıtı insan değil YÜZEY olur.

Ç2  A6 ↔ A6 · KENDİ İÇİNDE
    Tablo 2 "insan kaybolur" der, §4 promptları "motion streak insan" ister.
    ⇒ A6-X2'de çözüldü.

Ç3  A8 ↔ DEPO · BAŞTAN KIRPMA
    A8 her klibin başından 10-15 kare atılmasını ister.
    Bizim zincirde klibin İLK KARESİ zincirin çapasıdır [§8 · DERS 25].
    ⇒ ÇÖZÜM: kırpma bütçesi ÜRETİM süresine eklenir (A8-X7), kapak ve final
      kare kanıtı HER ZAMAN teslim dosyasından alınır — üretilen klipten değil.

Ç4  A7 ↔ DERS 2 · PROMPT UZUNLUĞU
    A7: "2.000 karakterin altı daha iyi" (kaynaksız).
    DERS 2: "bu türün bandı 4.500-5.500 karakter" (bu depoda ölçüldü).
    ⇒ ⛔ KILAVUZ DEĞİŞMEZ. Araç kartına "prompt tavanı" ölçüm satırı eklenir.
```

---

## 6. HÜKÜM — ne iniyor, ne inmiyor

| rapor | mesleki değer | kaynak disiplini | kılavuza iner mi |
|---|---|---|---|
| **A5 İNŞA YÖNTEMİ** | ⭐⭐ çok yüksek | zayıf (üç yanlış atıf) | ✅ **iner** — atıflar atılarak, kadraj sayısı bizimkiyle değiştirilerek |
| **A6 ŞANTİYE HAREKETİ** | ⭐ yüksek | orta (aritmetik ✅, fizik ⛔) | ✅ **iner** — gölge sayısı bizimkiyle değiştirilerek, iç çelişki çözülerek |
| **A7 ARAÇ PROFİLİ** | ⭐⭐ tek en değerli bulgu | ⛔ zayıf (envanter delik, tarihler çürük) | ⚠️ **kısmen** — mekanizma ve protokol iner, ENVANTER İNMEZ; kart boş açılır |
| **A8 KURGU VE TESLİM** | ⭐ yüksek | ⭐ en disiplinli (çelişkiyi ortalamadı) | ✅ **iner** — iki komut düzeltilerek, eşik bizim ölçümümüzle değiştirilerek |

```
⛔ RAPORDAN GELEN HİÇBİR SAYI KILAVUZA "ÖLÇÜLDÜ" DİYE YAZILMAZ.
   Kılavuzlara inen sayılar yalnız şunlardır ve hepsi bu dosyada hesaplandı:
     · kadraj 33,7 × 60,0 m · 32 px/m · okunabilirlik eşiği 0,5 m   [A5-X5/X6]
     · gölge dönüşü 116°/150°/191° · öğle hızı 15-46°/sa            [A6-X1]
     · sıkıştırma 60x/300x/1440x/5400x (rapor doğruydu, teyit ettim) [A6+1]
     · kesme skoru bandı 0,016-0,022 · klip içi tavan 0,005          [A8-X2]
     · kırpma bütçesi 0,67-1,00 sn → üretim süresi teslim + 2 sn     [A8-X7]
```
