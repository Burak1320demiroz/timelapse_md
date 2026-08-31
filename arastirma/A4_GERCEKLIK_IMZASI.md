# 🌦️ A4 — GERÇEKLİK İMZASI

```
AMAÇ      Bir timelapse'i GERÇEK gösteren fiziksel işaretleri ve AI olduğunu
          ele veren işaretleri ayrı ayrı, nesne düzeyinde çıkarmak.
KARŞILIĞI ③ ZAMAN merceği filmin 34 aylık süresini "yaklaşık bir yıl" okudu.
          İki sahnede mevsim OKUNAMADI: "Indeterminate — bare rock and concrete
          with no foliage, weather, or sun-height carriers."
          ① C4 GECE 0/10: "static, pinpoint stars with no trails, despite
          rapidly moving shadows confirming a long time-lapse span."
          Kar tek sahnede başlayıp bitti; izleyici İKİ kış saydı.
DÖNÜŞÜ    KILAVUZ_REHBERI §7 (negatif çekirdek) · SAHA_VE_IKLIM_KARTLARI ·
          ZAMAN_VE_ISIK_KILAVUZU · aşama merdiveni MEVSİM TAŞIYICISI sütunu ·
          DERS 7 · 14 · 16
```

⭐ Ölçülmüş bir kural: **"kış" bir taşıyıcı değildir; "yamaçtaki kar çizgisi",
"çıplak dallar", "sararmış ot", "su seviyesi" taşıyıcıdır.** Bu prompt o
taşıyıcı listesini saha saha doldurmak için var — ve negatif çekirdeğin hangi
maddesinin hangi sahada YANLIŞ olduğunu bulmak için.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden

Sen hem timelapse fotoğrafçılığı hem inşaat süreçleri üzerine çalışan bir
araştırmacısın. Görevin estetik tavsiye vermek değil, **gözle görülür,
adlandırılabilir NESNELER ve ölçülebilir SAYILAR** getirmek.

## BAĞLAM — araştırmayı bunun için yapıyorsun

```
ÜRÜN        9:16 dikey, konuşmasız, SABİT kameralı, AI ile üretilmiş inşaat
            timelapse filmi. 10 sahne × ~6 sn = 60 sn.
            Bir yapı (kule · konut · köprü · baraj · stadyum · yol/tünel ·
            liman · rüzgâr türbini) boş arsadan tamamlanmış hâline yükselir.
            Filmin kapsadığı gerçek zaman: 12 ile 36 ay arası.
SAHALAR     şehir içi · kırsal · kıyı · dağ/eğim · kar bölgesi · çöl · kaya vadisi
BEYAN       İçerik AI olarak beyan ediliyor. Amaç kimseyi kandırmak DEĞİL;
            amaç zamanın ekranda OKUNABİLİR olması. İzleyici filme bakıp
            "yaklaşık ne kadar zaman geçti" diyebilmeli.

ÖLÇÜLEN ARIZALAR — üçü de gerçek üretimde oldu:
  A. İki sahnede mevsim okunamadı: kaya vadisinde bitki yoktu, kar yoktu ve
     mevsimi taşıyan hiçbir nesne kadrajda değildi. Değerlendiren taraf filmin
     34 aylık süresini "yaklaşık bir yıl" okudu.
  B. Kar tek sahnede yağdı ve bir sonraki sahnede tamamen kayboldu; ayrıca
     aktif çalışma alanında kar LEKESİZ ve İZSİZ kaldı.
  C. Gece sahnesinde yıldızlar nokta hâlinde, izsiz çizildi — halbuki gölgeler
     hızla süpürüyordu. Bunun sebebi promptumuzdaki "no star trails" maddesiydi;
     o madde ŞEHİR sahası için doğruydu, DAĞ VADİSİ için yanlıştı.
     ⭐ Yani doğru bir kural yanlış sahaya taşınmıştı. Bu tür çelişkileri
        önceden bulmak istiyoruz.
```

## GÖREV — sekiz soru, sırayla

### 1. GERÇEK TIMELAPSE'İN FİZİĞİ — sayılarla
Uzun süreli inşaat timelapse'i profesyonelce nasıl çekiliyor?
- Aylar/yıllar süren bir inşaatta kare aralığı (interval) kaç saniye/dakika
  seçiliyor? 12 ay → 60 saniye çıktı için hangi hesap yapılıyor?
- "Holy grail" pozlama geçişi, deflicker (titreşim giderme), otomatik hizalama
  gibi işlemler ne yapar ve İŞLENMEMİŞ görüntüde hangi izleri bırakır?
- Sahada kamera nasıl konumlanır (sabit direk · komşu bina çatısı · vinç)?
  Kamera kaç ay dışarıda kalır ve görüntüde bunun izi nedir (lens üzerinde
  toz, yağmur damlası, örümcek ağı, camda çizik, güneş yansıması)?
- Bu alanda çalışan sistemleri ve tipik çıktılarını incele; ürettikleri
  görüntünün **ayırt edici imzası** ne?

⭐ Ayrıca: **hangi görsel imzalar YALNIZ uzun aralıklı çekimde ortaya çıkar?**
(bulut çizgileri, gölgenin süpürme hızı, kalabalığın erimesi, gece-gündüz
geçişinde pozlama kayması, hava değişimlerinin ani sıçraması, mevsim atlaması,
sahnede aniden beliren/kaybolan araçlar) — her birini ayrı tarif et.

### 2. ⭐⭐ MEVSİM TAŞIYICISI KARTLARI — saha saha
Aşağıdaki her saha için, **mevsimi ekranda taşıyan NESNELERİ** listele.
Her nesne için: hangi mevsimde ne hâlde olduğu, kaç haftada değiştiği ve
kadrajda nerede durabileceği.

```
SAHALAR:  şehir içi · kırsal/tarım · kıyı · dağ/eğim · kar bölgesi · çöl ·
          çıplak kaya vadisi (⛔ bu sonuncusu bizde ÇÖKTÜ — özel dikkat)
```

⛔ "Kış" ya da "yaz" yazma. NESNE yaz: yapraksız dal · sararmış ot · yamaçtaki
kar çizgisinin kotu · su seviyesi · gölgenin uzunluğu · tarlanın rengi ve
hasat izi · deniz rengi ve dalga · toz/kum birikintisi · yosun · kuş sürüsü...

⭐ **Çıplak kaya vadisinde bitki ve kar yoksa mevsimi ne taşır?** Bu soruyu
ayrıca ve uzun uzun cevapla — bizdeki ölçülmüş arıza tam olarak buydu.
En az 5 farklı taşıyıcı öner ve her birinin gerçek örneğini göster.

Çıktı biçimi — tablo:
```
SAHA | TAŞIYICI NESNE | İLKBAHAR | YAZ | SONBAHAR | KIŞ | DEĞİŞİM SÜRESİ | KAYNAK
```

### 3. KARIN ÖMRÜ — hafta hafta
Aktif bir şantiyede kar gerçekte nasıl davranır?
- İlk yağıştan tam erimeye kadar geçen tipik süre, iklime göre.
- ⛔ Karın aktif çalışma alanında NASIL göründüğü: tekerlek izleri, çamura
  inen oluklar, kenara kürelenmiş gri yığınlar, tuz/grit lekesi, buz,
  ısıtıcı/branda, dondan koruma örtüsü, beton dökümünün kışın durması.
- Şantiyede kışın hangi işler DURUR, hangileri devam eder? (beton dökümü,
  kazı, çelik montaj, cephe kaplaması) Bu, filmin "kış = direnç" sahnesinin
  gerçekliğini taşıyacak.
- Kar erirken sahanın hâli: çamur, göllenme, tekerlek izi, kirli su.
Her madde için fotoğraf/video referansı ver.

### 4. GECE VE YILDIZ İZİ — saha saha
- Uzun pozlamalı gece timelapse'inde yıldızlar ne zaman NOKTA, ne zaman İZ
  olarak görünür? Poz süresi ve kare aralığı ile iz uzunluğu arasındaki ilişki.
- Şehir ışığı altında gece gökyüzü nasıl görünür (ışık kirliliği · yıldız
  görünmemesi · turuncu gökyüzü)? Dağ vadisinde? Çölde? Kıyıda?
- Kutup yıldızı etrafında dairesel iz ne zaman oluşur, kadrajın yönüne göre
  iz nasıl değişir (doğuya bakan kamera vs kuzeye bakan kamera)?
- ⭐ Sonuç olarak: **"gece gökyüzü" tarifi hangi sahada nasıl yazılmalı?**
  Her saha için tek cümlelik İngilizce, POZİTİF tarif ver.

### 5. AI İŞARETLERİ — izleyicinin gördüğü şey
İzleyicilerin "bu yapay zekâ" dediği SOMUT görsel işaretleri topla; özellikle
mimari/inşaat/manzara içeriğinde. Kaynak: video yorum bölümleri, tartışma
forumları, AI video eleştiri toplulukları, teknik yazılar.
- En az 20 işaret çıkar, **kaç kez adlandırıldığına göre sırala.**
- Her işaret için: nasıl göründüğü, hangi sahnede ortaya çıktığı, önlenebilir
  mi ve nasıl.
- En az 15 gerçek yorum örneğini TAM METİNLE ver.
- ⛔ Ayrıca: hangi işaretler AI'ı ele verir ama izleyici RAHATSIZ OLMAZ,
  hangileri videoyu ÖLDÜRÜR? Bu ayrım bizim için karar verdirici.

### 6. ⭐ İNŞAAT MANTIĞI — profesyonelin gördüğü hata
İnşaat/mühendislik alanında çalışanların, sahte veya AI üretimi inşaat
görüntülerine yaptıkları TEKNİK itirazları topla. Aradığımız şey estetik değil,
**sıra ve mantık hatası:**
```
· yük yolu ve taşıyıcı sistem tutarsızlığı
· kalıp/donatı/döküm sırasının yanlış olması
· bir katın altındaki kat bitmeden yükselmesi
· vinç tipinin işe uymaması, vincin kendi kendini kurması, kanca-halat kopukluğu
· iskele ve tırmanan platform mantığı
· köprüde konsol/serbest uç, kablo/askı sırası, kapanış (closure) anı
· barajda gövde/dolusavak/derivasyon sırası
· kazı-iksa-radye sırası
· cephe kaplamasının hangi yönde ilerlediği (aşağıdan yukarı mı, kattan kata mı)
```
Her yapı tipi için, gerçek inşa sırasını **10 ADIMA bölünmüş hâlde** yaz.
Bu doğrudan bizim 10 sahnelik ızgaramıza oturacak.

### 7. PLATFORM GERÇEĞİ — beyan, para ve erişim
Bugün itibarıyla, kaynak ve tarih vererek:
- YouTube · TikTok · Instagram'ın AI içerik beyanı kuralları tam olarak ne?
  Hangi ekranda, hangi isimle, hangi durumda zorunlu?
- Beyanın erişime ya da para kazanmaya etkisi ÖLÇÜLMÜŞ mü? Platformlar ne
  diyor, yaratıcılar ne ölçüyor? İkisi çelişiyorsa ikisini de yaz.
- YouTube'un "özgün olmayan içerik" (inauthentic / mass-produced / repetitious)
  politikası ne diyor ve **AI üretimi bir kanalın bu politikadan etkilenmemek
  için ne yapması gerektiği** yazılı olarak nerede geçiyor?
- Belgelenmiş vaka: AI içerik ürettiği için para kazanması kesilen ya da
  kaldırılan kanallar. Gerekçeleri neydi?
- C2PA / içerik kimlik bilgisi üstverisi yüklemede korunuyor mu, platformlar
  okuyor mu? Otomatik AI etiketi tetikliyor mu?

### 8. İYİ KARŞILANAN AI İÇERİK
Aynı türde iyi karşılanan AI içerikleriyle "slop" denen içerikler arasındaki
farkı, YORUM VERİSİYLE ayır.
- Açık beyan koruyucu mu — beyan eden içerikler daha az düşmanlık alıyor mu?
- Başlıkta/açıklamada AI'ı nasıl anmak işe yarıyor?
- İzleyici hangi durumda AI'ı KABUL ediyor (imkânsız çekim · eğitici içerik ·
  açıkça kurgusal), hangi durumda reddediyor (belgesel taklidi · gerçek olay
  iddiası · gerçek firma/proje iddiası)?

---

## ⭐ ZORUNLU SON ÜÇ BÖLÜM

### MEVSİM TAŞIYICISI KARTLARI
Soru 2'nin tablosunun temiz hâli — yedi saha × dört mevsim, her hücrede
en az bir NESNE.

### NEGATİF ÇEKİRDEK ADAYLARI
Her aday **POZİTİF ve ÖLÇÜLEBİLİR bir İngilizce cümle** olarak yazılır —
yasak olarak değil. Bizde ölçüldü: yasak tutmuyor, ölçülebilir çapa tutuyor.
```
ADAY CÜMLE (İngilizce, pozitif) | HANGİ SAHADA GEÇERLİ | HANGİ SAHADA TERS
                                |                      | ÇEVRİLMELİ | KAYNAK
```
⛔ Her satırda "hangi sahada TERS çevrilmeli" sütunu doldurulmalı. Bizdeki
arıza tam olarak buydu: şehir için doğru olan madde dağda yanlıştı ve kimse
bunu önceden sormamıştı. Ters çevrilmesi gereken saha yoksa "yok" yaz —
ama boş bırakma.

### ON ADIMLIK İNŞA SIRALARI
Soru 6'daki her yapı tipi için 10 satırlık inşa sırası tablosu:
```
ADIM | EKRANDA GÖRÜNEN YENİ İŞ | GERÇEK SÜRE | KANIT NESNESİ (ilerlemeyi
     |                         |             | EKRANDA kanıtlayan tek nesne)
```
⭐ "Bina büyüdü" bir kanıt değildir. Kanıt nesnesi ölçülebilir olmalı:
"döşeme kenarı artık komşu binanın çatı mahyasıyla aynı hizada."

---

## 📏 KAYNAK VE YAZIM SÖZLEŞMESİ — beşi de zorunlu

```
① ETİKET     [ÖLÇÜLDÜ] · [İDDİA] · [VARSAYIM] — ⛔ etiketsiz cümle yazma.
② NESNE      Her tarif GÖRÜNÜR BİR NESNEYE bağlanır. "Kış hissi", "belgesel
             doku", "gerçekçi atmosfer" gibi cümleler yazma; onların yerine
             kadrajda duran şeyi adlandır.
③ SAYI       Süre, aralık, açı, yükseklik, hafta — sayı verebildiğin her yerde
             ver. Veremiyorsan "sayı bulunamadı" yaz.
④ ÇELİŞKİ    İki kaynak çelişiyorsa ikisini de yaz, ortalama ALMA.
⑤ KAYNAK     Bağlantı + tarih. Birincil kaynak tercih et: gerçek timelapse
             videosu, saha fotoğrafı, inşaat mühendisliği kaynağı, platformun
             kendi politika sayfası, gerçek yorum metni.
```

**Format:** Tablo ağırlıklı. Rapor Türkçe; prompt cümleleri, teknik terimler,
kaynak başlıkları ve yorum alıntıları ORİJİNAL DİLİNDE. Uzunluk sınırı yok.
