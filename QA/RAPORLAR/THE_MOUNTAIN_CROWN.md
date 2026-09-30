# 🔍 THE MOUNTAIN CROWN — QA RAPORU

```
FİLM          THE MOUNTAIN CROWN — boş bazalt duvardan kaya oyma su sarayı inşası (7 × 8,0 sn = 56,0 sn hedef, 2× hızlandırılmış 32,0 sn master)
TARİH         28.09.2026
DURUM         ⭐ ÜRETİLDİ VE TÜM ON İKİ MERCEK TAMAMLANDI (12/12)!
              ⚠️ DİFÜZYON MODELİNİN EKSİLTMELİ KAYA OYMADAKİ SINIRLARI BELGELENDİ:
                 - Depo ortalamasının altında genel kalite skoru: 6,15 / 10
                 - Asgari Set (① 8,1 · ② 7,3 · ⑤ 5,6) → DÜŞTÜ ❌ (② ve ⑤ baraj altı)
                 - En zayıf halkalar: ⑩ SEBEP 4,0 · ⑫ KATILIK 4,8 · ⑨ FAALİYET 5,5 · ⑤ DEVAMLILIK 5,6 · ③ ZAMAN 5,7
              ⭐ EN GÜÇLÜ KATEGORİLER:
                 ① KARE 8,1/10 Ⓥ (Kamera kilidi, istasyon ve nirengi 10/10; kanyon kenarları tek piksel oynamadı)
                 ② İNŞA 7,3/10 (6 nirengide ölçek kilidi 9/10; kütle eksiltme sırası korundu)
                 ⑦ İŞ 7,0/10 (7 eksiltme adımı moloz akışıyla tutarlı; teslimatta 4 sn duraksama)
                 ④ TESLİM 6,9/10 Ⓥ (FINAL BEAT PASS 8/10; ikiz şelaleler konsollardan döküldü)
              ⛔ KRİTİK MODEL ARIZALARI:
                 - ⑩ SEBEP (4,0): 60 m yukarıdaki kemer ve sütunlar, alet teması olmadan kendiliğinden oyuldu (MAGICAL APPEARANCE).
                 - ⑪ ENVANTER (6,5): 0:22'de A-frame çelik derrick vinç belirdi/kayboldu; uçurum çıkıntısında ekskavatör türedi; paletli taş bloklar sızdı.
                 - ⑫ KATILIK (4,8): 00:22.8'de tepe kafes portalı fade ile belirdi ve eridi (MELTING); kaba kaya apronu pürüzsüz kuma kaynadı.
                 - ⑤ DEVAMLILIK (5,6): 7 dikişin 7'sinde de geçici ekipman/iskele kusuru (A SET REBUILT EACH TIME).
                 - ③ ZAMAN (5,7): 00:24.3'te şelale açılışında ışık günbatımından öğle güneşine geri sıçradı (PASSES BUT NOT IN ONE DIRECTION).
                 - BİTİŞ KARTI (0:28.0): Tek tonozlu oyma cephe yerine çok katlı Petra tarzı tapınak görseli çıktı (DIFFERENT).
HAM           QA/HAM_RAPORLAR/THE_MOUNTAIN_CROWN/ — 12 dosya (1_KARE … 12_KATILIK)
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|---:|---|---|
| **① KARE** | V | **8,1**/10 Ⓥ | ✅ **TIME-LAPSE** | Kamera kilidi 10 · İstasyon 10 · Ankor 10 · Çerçeve 10 · Metin/Marka 10 · Safe Area 6 (apron araçları ve sprey) · İnsan/Araç 6 · Yüzey gerçeği 3 · ⛔ End Card: DIFFERENT |
| **② İNŞA** | D | **7,3**/10 | ✅ **SAME · BUILT** | 6 nirengide ölçek kilidi 9/10 · Kütle eksiltme adımları 8 · Yük yolu 6 · Monotonic growth 5 (apron dalgalanması) · ⛔ End Card: DIFFERENT (0:28 çok katlı tapınak) |
| **③ ZAMAN** | V | **5,7**/10 Ⓥ | ⛔ **NOT IN ONE DIRECTION** | Güneş yönü 7 · Gölge boyu 5 · Gökyüzü 5 · Mevsim 5 · Süreklilik 4 · 00:24.3 kesmesinde ışık gün batımından öğleye geri sıçradı · ⛔ End Card: DIFFERENT |
| **④ TESLİM** | D | **6,9**/10 Ⓥ | ✅ **SONA ERİYOR (ENDS)** | ⭐ **FINAL BEAT PROOF: BAŞARILI (PASS — 8/10)** · 0:24–0:28 ikiz şelaleler konsollardan dökülür · Vaat 8 · Direnç 7 · Sahne ayrışması 9 · ⛔ Kapak ve End Card 3/10 |
| **⑤ DEVAMLILIK** | V | **5,6**/10 Ⓥ | ⛔ **A SET REBUILT** | 7 dikişin 7'sinde de kusur (7 DEFECT, 0 INTENDED) · Sol ve sağ bazalt payandalar kilitli; ancak iskeleler, üst oluklar ve vinçler dikişlerde sıçrıyor · ⛔ End Card: DIFFERENT |
| **⑥ GEÇİŞ** | V | **6,4**/10 Ⓥ | ⚠️ **TIME · METRONOME** | 7 sert kesme · Nirengi kalıcılığı 9 · 00:24.3 kesmesinde zaman oku tersine döndü · 2,3–4,0 sn eşit pencereler metronom oluşturur · ⛔ End Card: DIFFERENT |
| **⑦ İŞ** | V | **7,0**/10 | ✅ **WORKING** | 7 eksiltme adımı moloz akışıyla tutarlı · 4,0 sn rölanti (teslimat şelalesinde) · 0:12–0:20 üst oymada alet teması yok · ⛔ End Card: DIFFERENT |
| **⑧ YÖNTEM** | D | **6,0**/10 Ⓥ | ⛔ **BELİRDİ (APPEARED)** | 5 eleman yapıldı, 2 eleman belirdi (5 MADE, 2 APPEARED) · Üst su tahliye kanalları 0:24.1'de kırımsız belirdi · En iyi yapılan: Moloz Apronu · ⛔ End Card: DIFFERENT |
| **⑨ FAALİYET** | V | **5,5**/10 Ⓥ | ⚠️ **PRODUCTIVE WORK** | Alt apronda dozer mekik döngüsü 4/10 · 00:24.3'te şelale altında donuk bekleyen personel 4/10 · İnsan emeği 6/10 · ⛔ End Card: DIFFERENT |
| **⑩ SEBEP** | D | **4,0**/10 | ⛔ **MAGICAL APPEARANCE** | 60 m yukarıdaki ana tonoz, sütunlar ve taç merlonları, makineler tabanda dururken alet teması olmadan kendiliğinden oyuldu · 0:28 bitiş kartı tamamen sihirli |
| **⑪ ENVANTER** | D | **6,5**/10 Ⓥ | ⛔ **INTRUDERS** | Davetsiz misafirler: 0:22 çelik A-frame derrick vinç (FORBIDDEN); 0:13 sarp kaya çıkıntısında ekskavatör (FORBIDDEN); 0:21 paletli taş bloklar (UNINVITED) |
| **⑫ KATILIK** | V | **4,8**/10 Ⓥ | ⛔ **MELTING** | En kötü eriyen gövde: 00:22.8 Tepe Çelik Kafes Kirişi (Overhead Steel Truss) fade ile belirdi ve kayboldu · Kaba kaya apronu 00:19.5'te pürüzsüz kuma kaynadı |

---

## 2. ⛔ HÜKÜM VE KALİTE ANALİZİ

```
DİFÜZYON MODELİNİN EKSİLTMELİ (SUBTRACTIVE) İNŞAAT SINIRLARI (ORTALAMA 6,15 / 10):
1. EKSİLTMELİ MANTIK VE NEDENSELLİK KIRILMASI (⑩ 4,0 · ⑧ 6,0 · ⑦ 7,0):
   - Model, eklemeli (additive) inşaatta vinç ve kalıpla parça koymaya alışkındır.
   - Kaya oymada ise 100 metrelik sarp duvardaki taç, kemer ve monolit sütunları üretirken fiziksel
     kesici/delici temasını kuramamıştır: ekskavatör ve dozerler 60 metre aşağıdaki taban apronunda
     dönüp dururken üst cephe "kendiliğinden" soyularak şekillenmiştir (Proximity without work).
2. İKİZ İNTİHAL VE HALÜSİNASYONLAR (⑪ 6,5 · ⑫ 4,8):
   - 0:22'de tepede aniden devasa bir çelik A-frame truss vinç ve portal belirip 0:24'te buharlaşmıştır.
   - Eksiltmeli bazalt oyması yapılan şantiyeye, eklemeli inşaat alışkanlığıyla paletli tuğla/taş bloklar girmiştir.
   - Apron molozları dozerle kademeli serilmek yerine bir karede kaynayarak pürüzsüz kum rampasına dönmüştür.
3. ZAMAN VE AKIŞKAN İHLALİ (③ 5,7 · ⑥ 6,4):
   - Güneş saati 18:00 günbatımına doğru düzenli ilerlerken, 00:24.3 kesmesinde şelalelerin devreye girmesiyle
     ışık birden öğle saatine ve yüksek azimuta sıçramıştır (Time reversal).
   - Su debisi devreye girdiğinde alt aprondaki makineler ve işçiler tahliye edilmemiş, tonlarca suyun
     altında donuk vaziyette kalmıştır.
4. BİTİŞ KARTI İHLALİ (TÜM MERCEKLERDE "DIFFERENT"):
   - Planda kapağın videosuz/yazısız olması şart koşulmuşken, model 0:28.0'da tek tonozlu 6 sütunlu cepheyi
     tamamen silip yerine çok katlı Petra tarzı klasik bir tapınak cephesi basmıştır.
```

---

## ⚡ 2.1. 2× HIZLANDIRILMIŞ KURGU (32.0 sn Master) VE QA ELEŞTİRİSİ

```
⚠️ DİKKAT: BU FİLM 2 KAT HIZLANDIRILMIŞ OLARAK ÜRETİLDİ VE ELEŞTİRİLDİ:
1. SÜRE VE KLİP FARKI:
   - Planda beyan edilen hedef: 7 sahne × 8,0 sn = 56,0 sn tek master kurgu.
   - Üretilen ve değerlendirilen video: 7 klip × ~4,0 sn = 28,0 sn sahne bloğu + 4,0 sn bitiş kartı = 32,0 sn.
   - THE LAST HARBOR'da olduğu gibi video dinamik bir 32 sn Shorts/Reels ritmiyle realize edilmiştir.
2. QA MERCEKLERİNE ETKİSİ:
   - ⑦ İŞ (7,0/10) & ⑨ FAALİYET (5,5/10): Klip süreleri kısaldığı için aprondaki dozerlerin mekik hareketleri
     hızlanmış, ancak üst oymaya doğrudan temas edemedikleri için "yakınlık alibisi" (proximity alibi) belirginleşmiştir.
   - ⑥ GEÇİŞ (6,4/10): Eşit ~4,0 saniyelik pencereler metronom oluşturmuş, Cut 6 @ 00:24.3'teki güneş sıçraması
     hızlı tempo içinde süreksizliği daha da keskinleştirmiştir.
   - ④ TESLİM (6,9/10): 56 sn yerine 32 sn teslim edilmesi teslimat vaadini yok etmemiş; ancak 0:28'deki
     bitiş kartı değişimi kurgunun final etkisini zedelemiştir.
```

---

## 3. ❓ DOKÜMAN SORULARININ YANITLARI

### ① KARE (LENS 1)
1. **Sözleşmede hedeflenen ufuk çizgisi yüzdesi ve A Görüş Grubu istasyon hizalaması nedir?**  
   * **Yanıt:** Planda (Değişmezler Tablosu Satır 189–200 ve 218) kamera vadinin güney kaya sekisinde (h = +52,00 m, d = 78,00 m, bearing 15°, TİLT 0°, 24 mm objektif) kilitlidir. Kadrajda **ufuk çizgisi yoktur**; bazalt kayalığı kadrajı kenardan kenara kaplar (%97,60 kaya tepesi, üstünde yalnızca 46 px gök kalır). Ufuksuz kompozisyon kasıtlı bir tasarım kararıdır (§Tasarım Kararları ⑧).
2. **0:02.0 ile 0:06.5 arasında sol şelalenin ani saptırılması planlanmış bir mühendislik sekansı mıydı?**  
   * **Yanıt:** **Evet, filmin temel direncidir.** Planda (§Aşama Merdiveni S0–S1 Satır 81–86, 327–328) suyun kendisi imalat direncidir. S0'da (0:00–0:04) iki doğal şelale eşikteki çelik oluğa alınır ve sağ kenara (%x 93,59) kahverengi tek jet olarak taşınır. Kaya yüzü ancak su saptırıldıktan sonra kurutulup oyulabilir.
3. **0:24.0'da üst uçurum duvarından fışkıran iki dikey su gayzeri nihai saha tasarımının hedeflenen özellikleri miydi?**  
   * **Yanıt:** Planda (§Aşama Merdiveni S6 Satır 9–10, 222, 333, 375–380) iki şelale +72,00 kotundaki **iki konsol oluk ağzından** kontrollü olarak dökülür; yukarı doğru gayzer şeklinde fışkırmaz, yerçekimiyle serbest düşüşe geçer (61,00 m, t = 3,53 sn). Modelin 0:24.0'da ürettiği dikey gayzer/fıskiye formu difüzyonun akışkan dinamiğindeki yapay yorumudur.
4. **0:28.0'daki bitiş kartı Klip 6'da oyulan yapıdan farklı bir mimari yapı sunmak üzere mi tasarlandı?**  
   * **Yanıt:** **Kesinlikle hayır!** Planda (§Teslim Yapısı Satır 45) `KAPAK KARTI: ⛔ YOK — logo yok, video üstünde yazı yok` kuralı konmuştur. Modelin 0:28.0'da tek tonozlu 6 sütunlu oyma saray yerine çok katlı Petra tarzı bir tapınak cephesi koyması difüzyonun jenerik kütüphanesinden kaynaklanan ağır bir halüsinasyondur.

### ⏱️ ZAMAN (LENS 3)
1. **Klipler için beyan edilen güneş azimutu ve yükseklik takvimi nedir?**  
   * **Yanıt:** Planda (§Güneş Saati Tablosu Satır 462–474) güneş takvimi 44° Kuzey enleminde 06:00'dan 18:00'e 12 saatlik kesintisiz ışık gününü kapsar:
     - 06:00 (az 84,23°, el 5,55°, soğuk mavi gölge)
     - 08:00 (az 105,87°, el 26,93°)
     - 10:00 (az 135,03°, el 45,53°, gölgeler sola)
     - 12:00 (az 180,00°, el 54,00°, en kısa gölge)
     - 14:00 (az 224,97°, el 45,53°, en parlak kare)
     - 16:00 (az 254,13°, el 26,93°, gölgeler sağa)
     - 18:00 (az 275,77°, el 5,55°, altın yalama ışık).  
     Klip 7'de (00:24.3) ışığın birden öğle saatine geri sıçraması zaman yönü ihlalidir (DÜŞTÜ).
2. **Tüm sekans boyunca ne kadar takvim süresinin geçmesi hedeflenmiştir?**  
   * **Yanıt:** Fiziksel imalat takviminde 10.228 m³ sert bazaltın oyulması 6–9 aylık bir mühendislik operasyonudur; ancak ekranda **12 saatlik tek bir güneş günü** (06:00 → 18:00) üzerinde hızlandırılmıştır.
3. **Ağır iş makinelerine karşı akışkan partikül dinamikleri için hedeflenen zaman sıkıştırma oranı nedir?**  
   * **Yanıt:** İlk 6 klip **Rejim B (1200×)** sıkıştırmadır. Klip 7 (S6) ise **Rejim G (1× / gerçek zamanlı)** olarak tasarlanmıştır (§Aşama Merdiveni Satır 371–385). 61 m serbest düşüş yerçekimi formülüyle t = 3,53 saniyedir; son 8 saniyenin yarısı suyun havada düşmesine, dozer ve işçiler ise donuk beklemeye ayrılmıştır.

### ⑤ DEVAMLILIK (LENS 5)
1. **Sağ uçurum duvarındaki iskele merdiveninin (0:02.0) aşamalar arasında sökülmesi planlanmış mıydı?**  
   * **Yanıt:** Planda (§Malzeme Kaynağı Satır 404) duvara dışarıdan getirilen tek geçici ekipman çelik saptırma oluğu, braketler ve asılı sahanlıklardır; S4'te (SÖKER) tamamı sökülür ve geride yalnızca boş cıvata yuvaları kalır. Merdivenin Klip 2'de aniden belirip sonra sanayi konveyörüne dönüşmesi tutarsızlıktır.
2. **0:22.0'daki sarı traktör/ekskavatör bir erişim yolu olmadan üst uçurum kenarına nasıl ulaştı?**  
   * **Yanıt:** **Ulaşamaz, model halüsinasyonudur.** Planda (§Konsept Kapısı Satır 83) `⛔ VİNÇ YOK — 118 m'lik bir duvara bom uzanamaz; bütün iş eşikten sarkan asılı sahanlıklardan yapılır` kuralı vardır. Ağır makineler yalnızca tabandaki moloz apronunda dozer olarak çalışabilir; uçurumun tepesine veya dar kaya çıkıntılarına ekskavatör yerleştirilmemiştir.
3. **0:14.0'daki üst uçurum oluk kazısı geçici bir mühendislik önlemi miydi yoksa istenmeyen bir üretim hatası mıydı?**  
   * **Yanıt:** **Planlıdır.** Eşikten (+112,00) inen iki kesme oluk yatağı ve konsol ağızları (+72,00) S3'te (TAÇLANIR) oyulur. Ancak sonraki sahnede bu olukların kaybolup pürüzsüz kayaya dönmesi modelin hafıza kaybıdır.

### ⑥ GEÇİŞ (LENS 6)
1. **Müzik parçası için beyan edilen BPM temposu ve ölçü hizalama takvimi nedir?**  
   * **Yanıt:** **Müzik kesinlikle yasaktır (MÜZİK YOK).** Plan Satır 5, 49 ve 519 gereğince filmde hiçbir sahnede müzik kullanılmaz; ses yatağı bütünüyle diegetik doğa ve şantiye sesidir (şelalenin gürlemesi, saptırma oluğu, taş kırılma sesleri ve finalde suyun geri dönüşü).
2. **Yapım planındaki aşamalar için hangi temsil süreleri atanmıştır?**  
   * **Yanıt:** Planda 7 sahne × 8,0 sn = 56,0 sn eşit bloklar beyan edilmiştir (§Teslim Yapısı Satır 57). Teslim edilen kurgu ise dinamik platform temposuyla **2× hızlandırılmış** (7 klip × ~4,0 sn = 28,0 sn + 4,0 sn bitiş kartı = 32,0 sn) olarak realize edilmiştir.
3. **00:27.8'deki statik bitiş kartı neden oyulan 6 sütunlu kemer yerine çok katlı Petra tarzı bir cephe sergilemektedir?**  
   * **Yanıt:** Modelin difüzyon eğitim setindeki "kaya oyma tapınak" önyargısı (Al-Khazneh / Petra) son karede baskın gelmiş ve şartnamedeki kilitli Usta Kareyi (GN) hiçe sayarak jenerik bir tapınak resmi basmıştır.

### ⑦ İŞ (LENS 7)
1. **Üretim planında 0:12.0–0:20.0 arasındaki devasa kütle eksiltme aşaması için ek ağır kesici ekipmanlar tanımlanmış mıdır, yoksa süreç yalnızca atık olukları üzerinden mi modellenmiştir?**  
   * **Yanıt:** Planda (§Konsept Kapısı Satır 83–86 ve S2 Satır 360–369) 118 metrelik sarp duvarda bomlu vinç veya devasa paletli makineler kullanılamayacağı için imalat, üst eşikten sarkan asılı sahanlıklardaki hidrolik el kesicileri ve patlatma/kesme ekipleriyle modellenmiş; kesilen taşların yerçekimiyle serbestçe tabana dökülerek apronu oluşturması öngörülmüştür.
2. **0:28.0'daki bitiş kartı görselinin tek tonozlu yapıdan farklı olması planlanmış mıdır?**  
   * **Yanıt:** **Hayır.** Bitiş kartı planda tamamen yasaklanmıştır; ortaya çıkan görsel modelin tamamen kontrol dışı bir fantezisidir.
3. **Klip 7'deki (0:24.0) şelale re-aktivasyon süresi boyunca makinelerin tamamen durdurulması teslimat protokolünün bir parçası mıdır?**  
   * **Yanıt:** **Evet, Rejim G protokolüdür.** Plan Satır 371–385 gereğince S6'da (Rejim G) makineler ve insan figürleri tamamen hareketsiz (donuk) kalmalıdır; sahnedeki tek dinamik unsur serbest düşen su jetleri ve havuza çarpan köpük bulutudur.

### ⑨ FAALİYET (LENS 9)
1. **Alt apron bölgesinde çalışan dozerlerin belirli bir hacimde moloz sermesi mi planlanmıştı, yoksa hareketler yalnızca görsel dolgu amacıyla mı kurgulandı?**  
   * **Yanıt:** Planda (§Defter Tablosu Satır 95–99 ve §Karar ⑥) çıkan 10.228 m³ katı bazalt kabarma ile 12.785 m³ gevşek aprona dönüşür. Dozerin görevi dökülen bu devasa molozu yaymak, 35° şevli apronu tesviye etmek ve tabanda iki havuz çanağını açmaktır. Hareketler bir dolgu değil, defteri kapatan mekanik hafriyattır.
2. **00:24.3 klibinde şelaleler tekrar açıldığında iş makinelerinin ve personelin bölgeden tahliye edilmemiş olması senaryo gereği bir kurgu tercihi midir?**  
   * **Yanıt:** **Kısmen kurgu kısıtıdır.** Planda suyun aprona değil, apronda açılan iki kesme havuzun içine düşmesi öngörülmüştür. Dozer ve tek figür apronun kuru güvenli kenarında (orta eksende) seyirci olarak durmalıdır. Model ise suyu makinelerin hemen üstüne kontrolsüzce boşaltmıştır.
3. **Sağ kayalıktaki oluktan dökülen malzemenin kaynağı ve üst kotta hangi kazı ekibi tarafından beslendiği planlanmış mıdır?**  
   * **Yanıt:** Planda eşikteki çelik saptırma oluğu yalnızca suyu tahliye eder. Taş molozları ise doğrudan cephenin kesilen noktalarından aşağı serbest düşer. Sağ oluktan toprak akması difüzyonun saptırma oluğunu bir moloz şutu ile karıştırmasından ibarettir.

### ⑫ KATILIK (LENS 12)
1. **00:22'de beliren çelik kafes kiriş portalı (Overhead Steel Truss) planlanmış bir gantry sistemi miydi yoksa yapay zeka halüsinasyonu muydu?**  
   * **Yanıt:** **Tamamen yapay zeka halüsinasyonudur.** Planda (§Konsept Kapısı Satır 83) `⛔ VİNÇ YOK, ⛔ GANTRY YOK` kuralı açıkça konmuştur. Çelik kafes portal difüzyonun inşaat kalıbı önyargısıyla uydurduğu sahte bir intruder'dır.
2. **Sağ uçurum yapısı ahşap bir personel merdiveni mi yoksa endüstriyel konveyör köprüsü mü olmalıydı?**  
   * **Yanıt:** İkisi de değildir. Planda sağda yalnızca su saptırma çelik borusu (%x 93,59) vardır; merdiven veya konveyör köprüsü şartnamede yer almaz.
3. **Alt moloz apronunun ekskavatörlerce temizlenmesi mi yoksa kalıcı bir dolgu seti olarak mühendislik tasarımıyla bırakılması mı hedeflenmiştir?**  
   * **Yanıt:** **Kalıcı dolgu seti (apron).** Planda (§Defter Satır 95–99) hiçbir kamyon moloz taşımaz; dağdan çıkan taş vadide kalıcı bir podyum ve havuz seti olarak kalır.
4. **00:25'te ikiz şelaleler açılmadan önce ekskavatörlerin ve yer ekibinin tahliye edilmesi amaçlanmış mıydı?**  
   * **Yanıt:** Planda S4'te (SÖKER) ağır iş makineleri ve ekipler sahadan çekilir; S6'da (DÖNER) apronda yalnızca tek bir park halinde dozer ve sırtı dönük tek bir figür kalır. Ekskavatörlerin suyun altında çalışmaya devam etmesi model hatasıdır.
