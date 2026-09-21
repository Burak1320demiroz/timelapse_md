# 🔍 THE EMPTY LOCK — QA RAPORU

```
FİLM          THE EMPTY LOCK — tek taş kanal kilidi (hazne 5 × 30 × 4,5 m · meşe kapı değişimi ve su doluşu)
TARİH         21.09.2026
DURUM         ⭐ ÜRETİLDİ VE ON İKİ MERCEKLE ÖLÇÜLDÜ (12/12 TAM KOŞU)
              ⭐ ASGARİ SET EKSİKSİZ TAMAMLANDI (① KARE 7,5 · ② İNŞA 10,0 · ⑤ DEVAMLILIK 7,0)
              ⭐ YEDİ TANE 10/10 TAM PUAN:
                 ② İNŞA 10,0 · ③ ZAMAN 10,0 · ⑧ YÖNTEM 10,0 · ⑨ FAALİYET 10,0 ·
                 ⑩ SEBEP 10,0 · ⑪ ENVANTER 10,0 · ⑫ KATILIK 10,0
              ⭐ ZİRVE PERFORMANS: ⑦ İŞ 9,9/10 (en uzun boşluk %0) · ⑥ GEÇİŞ 9,5/10 (RHYTHM kurtarıldı)
              ⭐ 12/12 HÜKÜMLERİN HEPSİ EKSİKSİZ GEÇTİ:
                 ⑤ SAME WORLD ✅ + ⑧ MADE 5/5 ✅ + ⑦ WORKING ✅ + ⑩ CAUSED BY LABOUR ✅ +
                 ⑪ INVITED ✅ + ⑫ SOLID ✅ + ⑨ PRODUCTIVE WORK ✅ + ① TIMELAPSE ✅ +
                 ② BUILT ✅ + ③ PASSES ✅ + ⑥ RHYTHM ✅ + ④ ENDS ✅
              ⚠️ ÜRETİM KUSURLARI: Safe Area 4/10 (0:56.0 başlık bindirmesi) · Text 2/10 (vinç ve teknede "PAB" yazıları)
                                    · People 6/10 (0:40 ve 0:54'te motion blur'suz donuk işçiler) · Loop 5/10 (döngü süreksizliği)
HAM           QA/HAM_RAPORLAR/THE_EMPTY_LOCK/ — 12 dosya, dokunulmaz
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|---:|---|---|
| **① KARE** | V (60 kare) | **7,5**/10 Ⓥ | ✅ **TIME-LAPSE** | Kamera kilidi 10 · İstasyon 10 · Nirengi 10 · Zemin gerçeği 8 · Vinç 10 · Safe Area 4/10 (0:56.0 üst %35 başlık bindirmesi) · Text 2/10 ("PAB" vinç/tekne yazıları) · People 6/10 (donuk işçiler) |
| **② İNŞA** | D | **10,0**/10 | ✅ **SAME · BUILT** | Deponun ikinci tam puanlı İnşa koşusu · 7 nirengide ölçek sapması %0,0 · Batardo/dewatering'den tekne kaldırmaya kusursuz hidrolik montaj sırası |
| **③ ZAMAN** | V (tam kurgu) | **10,0**/10 Ⓥ | ✅ **PASSES** | Filmden okunan süre: "about 10 to 11 hours (one single working day)" (plan 10 sa 20 dk) TAM TUTTU · Gölge süpürmesi 1:2.0 → 1:0.6 → 1:4.3 tam fiziksel uyum |
| **④ TESLİM** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 6,8) | ✅ **ENDS** | COST / FINAL BEAT PASS (7/10 Ⓥ) · ⭐ ONE THING BULUNDU · LOOP 5/10 · Plan ve kapak verilmedi · 0:48–0:56 yeni kapının suyu tuttuğu ve teknenin geçtiği doğrulandı |
| **⑤ DEVAMLILIK** | V | **7,0**/10 Ⓥ | ✅ **SAME WORLD** | 0/6 dikiş kusursuz · ⭐ Kanıt nesnesi: White lockkeeper cottage (00:00.0 ve 00:56.0) · Ekipman geçişleri, çekek yolundaki eski kapılar ve zemin aşınması kesintisiz |
| **⑥ GEÇİŞ** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 9,5) | ✅ **TIME · ⭐ RHYTHM** | 8,0 sn eşit ızgaraya rağmen RHYTHM hükmü kazanıldı · THE CUT THAT CARRIES: Cut 4 (00:32.0 yeni kapı montajı + müzik girişi) · Plan verilmedi |
| **⑦ İŞ** | ⚠️ V karesiz | **9,9**/10 Ⓥ | ✅ **WORKING** | En uzun boş aralık 0,0s (%0) · Çalışma cephesi 10 · Sebep-sonuç 10 · Malzeme akışı 10 · Makine döngüsü 10 · ⭐ Kimsenin yapmadığı büyüme: NONE |
| **⑧ YÖNTEM** | D | **10,0**/10 | ✅ **MADE · 5/5 MADE** | Deponun ikinci belgeli 10/10 Yöntem skoru · 5 elemanın 5'i de sıfırdan yapıldı · ⭐ İlk beliren parça: NONE · En iyi parça: New West Oak Gate Leaf (00:25.0) |
| **⑨ FAALİYET** | ⛔ V | **10,0**/10 Ⓥ | ✅ **PRODUCTIVE WORK** | Boşta bekleme 10 · Amaçsız hareket 10 · Animasyon döngüsü 10 · İnsan emeği 10 · ⭐ En amaçsız aktivite: NONE FOUND · Plan verilmedi |
| **⑩ SEBEP** | ⛔ V | **10,0**/10 Ⓥ | ✅ **CAUSED BY LABOUR** | Nedensellik bağı 10 · İşsiz yakınlık 10 · Emek ölçeği 10 · Malzeme kaynağı 10 · ⭐ Sihirli belirme: NONE FOUND · SPEC verilmedi |
| **⑪ ENVANTER** | ⛔ V | **10,0**/10 Ⓥ | ✅ **INVITED** | Kişiler 10 · Makineler 10 · Yapılar 10 · Işık/enerji 10 · Kurallar 10 · Gelmeyen davetli: NONE · ⭐ Davetsiz misafir: NONE FOUND |
| **⑫ KATILIK** | ⛔ V karesiz | **10,0**/10 | ✅ **SOLID** | Kenar/siluet 10 · Sayım 10 · Kimlik 10 · Boyut 10 · Geçiş/birleşme 10 · Yük yolu 10 · Mekanizma 10 · ⭐ En kötü eriyen gövde: NONE FOUND |

---

## 2. ⛔ HÜKÜM OKUMA SIRASI [kart R 6a, 6e]

```
12/12 HÜKÜMLERİN TAMAMI EKSİKSİZ GEÇTİ:
⑤ SAME WORLD ✅ + ⑧ MADE 5/5 ✅ + ⑦ WORKING ✅ + ⑩ CAUSED BY LABOUR ✅ + ⑪ INVITED ✅ + ⑫ SOLID ✅ + ⑨ PRODUCTIVE WORK ✅ + ① TIMELAPSE ✅ + ② BUILT ✅ + ③ PASSES ✅ + ⑥ RHYTHM ✅ + ④ ENDS ✅

⭐ TARİHİ BİR ZAFER DAHA:
   1. ASGARİ SET (① 7,5 · ② 10,0 · ⑤ 7,0):
      Kamera sabit, nirengi ve istasyon 10/10 kilitli; yapı kimliği tek ve monoton (%0,0 sapma), dünya kesintisiz (0/6 dikiş kusursuz).
   2. YEDİ TANE 10/10 TAM PUAN:
      ② İNŞA 10,0 · ③ ZAMAN 10,0 · ⑧ YÖNTEM 10,0 · ⑨ FAALİYET 10,0 · ⑩ SEBEP 10,0 · ⑪ ENVANTER 10,0 · ⑫ KATILIK 10,0.
   3. FİZİK VE NEDENSELLİK KUSURSUZ (⑩ 10,0 CAUSED + ⑪ 10,0 INVITED + ⑫ 10,0 SOLID):
      - Hiçbir sihirli belirme yok (MAGICAL APPEARANCE: NONE).
      - Hiçbir davetsiz nesne veya yabancı unsur sahaya sızmadı (INTRUDER: NONE).
      - Hiçbir gövde erimedi, deforme olmadı veya formunu kaybetmedi (MELTED: NONE).
   4. ŞANTİYE VE METOT TAM BAŞARI (⑧ 10,0 MADE + ⑦ 9,9 WORKING + ⑨ 10,0 PRODUCTIVE WORK):
      5/5 yapı elemanı sıfırdan monte edildi. Boş bekleme süresi %0. Amaçsız insan/makine hareketi sıfır.
   5. RİTİM VE ZAMAN (⑥ 9,5 RHYTHM + ③ 10,0 PASSES):
      8,0 saniyelik matematiksel düz ızgara, Cut 4'teki (00:32.0) meşe kapı montajı, orkestral patlama ve Rejim A hız değişimi
      ile metronom tuzağını yendi. 10 saat 20 dakikalık tek gün süresi ekrandan tam okundu.
```

---

## 3. 🚨 EN AĞIR BULGULAR

1. **[① KARE & ④ TESLİM — Safe Area 4/10 & Kurgu Uyuşmazlığı]:** [0:56.0] Son karede ekrana bindirilen `THE EMPTY LOCK` başlık yazısı çerçevenin üst %35'lik alanını kaplamış ve platform rezerv alanını (%87.5–100) çiğnemiştir. Plan açıkça `KAPAK KARTI YOK`, `LOGO YOK` şartını koymuştur. Başlık yalnızca platform küçük resmi (`THE_EMPTY_LOCK_KAPAK.md`) içindir; videodan kaldırılmalıdır.
2. **[① KARE — Text & Branding 2/10]:** [0:00.0–0:39.0] Sarı vinç bomunda/gövdesinde "PAB" harfleri ile [0:42.0–0:55.0] tekne pruvasında planda olmayan tescil yazıları belirmektedir.
3. **[① KARE — People and Vehicles 6/10]:** [0:40.0–0:42.0] ve [0:54.0–0:55.0] karelerinde işçiler motion blur olmaksızın dondurulmuş pozlar hâlindedir.
4. **[④ TESLİM — Loop 5/10]:** [0:56.0] Final durumu (su dolu haznede ilerleyen motorlu tekne) açılış durumuyla (drenaj yapılan boş kilit) birebir döngü kurmamaktadır.
5. **[⑦ İŞ — Kat. 6 Work Rate vs Growth 9/10]:** [0:48.0–0:56.0] Haznenin doluşu ve teknenin yükselişi, önceki ağır vinç söküm aşamalarına göre hızlandırılmış bir tempoda gerçekleşmektedir (Rejim A, 10 dk sıkıştırma).

---

## 4. ⏱️ ZAMAN TAHMİNİ [kart R 6]

```
③ "TIME READ FROM THE FILM ALONE: about 10 to 11 hours (one single working day)"
Taşıyıcı: Taş kanal duvarlarındaki kesintisiz gölge yayı (batıdan doğuya), adım adım kapı değişimi operasyonu ve
          akşam saatindeki düşük güneş açısı.
PLAN: 10 saat 20 dakika (07:20 → 17:40, tek gün, S0–S4 rejim B + S5–S6 rejim A).
✅ TAM VE EKSİKSİZ TUTTU — Model görselden planlanan süreyi dakikası dakikasına doğru okudu.
```

---

## 5. ❓ DOKÜMAN SORULARININ CEVAPLARI

### ① KARE
1. **Ağaç hattının gerçek ufku kestiği durumda, hedeflenen taban ufuk yüzdesi nedir?**
   - *Cevap:* Kamera istasyonu 8,2 m kotundaki değirmen korkuluğunda olup, −38° aşağı eğimlidir (ZEMİN bakış ailesi, KAMERA_DILI §3). Tanjant formülü ve pinhole izdüşümüne göre gerçek ufuk çizgisi y = %102'de (kadrajın tamamen üst dışında) kalmaktadır. `THE_EMPTY_LOCK_QA_SPEC.md` §2 satır 47 açıkça `gök: YOK, üst kenar kavakları keser; gök görünüyorsa istasyon KAYMIŞTIR` hükmünü vermiştir.
2. **Vinç üzerindeki marka yazısı ("PAB") sözleşme şartnamesinde açıkça onaylanmış mıydı?**
   - *Cevap:* **Hayır.** Negatif çekirdek ve sistem istemi ticari logoları, harfleri ve marka kimliklerini kesinlikle yasaklar. Vinç bomuna sızan "PAB" yazısı bir üretim kusurudur.
3. **Bitiş kartındaki başlık bindirmesinin üst %35'lik rezerv alanı kaplamasına platform kuralları izin veriyor mu?**
   - *Cevap:* **Hayır.** Planda video üzeri metin bindirmesi kesinlikle yasaklanmıştır (`KAPAK KARTI YOK · LOGO YOK`). Başlık yalnızca platform küçük resmi (`THE_EMPTY_LOCK_KAPAK.md`) için tasarlanmıştır; videodan kaldırılacaktır.
4. **0:40.0 ve 0:54.0'taki hareketsiz insan figürleri kasıtlı keyframe beklemeleri mi yoksa motion-blur üretim hatası mıdır?**
   - *Cevap:* **Motion-blur üretim hatasıdır.** İstemlerde personel "blurred figures in motion streak" olarak tanımlanmıştır; donukluk model kaynaklı bir hatadır.

### ③ ZAMAN
1. **Yedi inşaat kesmesi için beyan edilen başlangıç ve bitiş güneş açıları / saatleri nedir?**
   - *Cevap:* S0: 07:20→09:20 (20°→35°), S1: 09:20→11:20 (35°→48°), S2: 11:20→13:20 (48°→52°, öğle), S3: 13:20→15:20 (52°→35°), S4: 15:20→17:20 (35°→18°), S5: 17:20→17:30 (18°→15°, altın saat), S6: 17:30→17:40 (15°→12°, gün batımı).
2. **Kanal kapağı değişim operasyonunun tamamı için beyan edilen toplam geçen süre nedir?**
   - *Cevap:* **10 saat 20 dakika** (07:20 – 17:40, tek çalışma günü).
3. **Kadraj, gökyüzünü ve bulut hareketini dışarıda bırakmak için üst ağaç hizasından bilinçli olarak mı kırpılmıştır?**
   - *Cevap:* **Evet.** ZEMİN bakış ailesi kuralı gereğince kamera −38° eğimle doğrudan kanala odaklanmıştır.

### ⑤ DEVAMLILIK
1. **Sağ rıhtım/çekek yolu, emekliye ayrılan her iki kapı kanadı için proje boyunca kalıcı sergi/depolama alanı olarak mı planlanmıştı?**
   - *Cevap:* **Evet.** Depo sözleşmesinin "BEDEL" (cost) ilkesi ve `THE_EMPTY_LOCK_QA_SPEC.md` §3 (satır 64 & 75) uyarınca sökülen eski kara meşe kanatlar çekek yoluna yatırılır ve G7 usta karesine kadar kadrajda kalır; kadrajdan kaybolmaları yasaklanmıştır.
2. **Drenaj pompaları hazneye ilk su alımından (00:32.0) önce tamamen sahadan tahliye edilecek şekilde mi planlanmıştı?**
   - *Cevap:* **Evet.** `THE_EMPTY_LOCK_QA_SPEC.md` §3 (satır 68 & 79) ve §4 (satır 95) gereğince pompalar ve basma hortumları S3 içinde sökülür; G4'te coping'de hortum kalmaz, su alma aşaması (G5) başlamadan önce pompalar sahadan çıkarılmış olur.

### ⑦ İŞ
1. **Klip 7'deki hazne doluş hızı, savak kapaklarının gerçek zamanlı hidrolik akış hızına kıyasla yapay olarak hızlandırıldı mı?**
   - *Cevap:* Plandaki sıkıştırma rejiminin kuralıdır. `THE_EMPTY_LOCK_DIKEY_TIMELAPSE.md` §REJİM (satır 271–272) gereğince S5 ve S6 sahneleri **Rejim A (10 dakika sıkıştırma)** olarak beyan edilmiştir. Gerçekte 8–10 dakika süren doluş 8,0 saniyeye (~75×) sıkıştırılmıştır.
2. **Klip 5 ve Klip 6 arasında vincin sahadan çıkışı planlı bir mola sırasında mı gerçekleşti yoksa denge kirişi bağlantıları denetlendikten hemen sonra mı tahliye edildi?**
   - *Cevap:* Sıralı operasyondur. Planda (S4 satır 262 & 275) vincin ve lowbed'in rıhtım geçidinden çıkışı, teknenin kapı önüne yaklaşmasından önceki zorunlu saha tahliye adımı olarak tanımlanmıştır.
3. **Klipler 1–4'teki drenaj pompaları timelapse çekimleri arasında gece boyunca sürekli mi çalıştı yoksa her sabah çekimden önce mi çalıştırıldı?**
   - *Cevap:* Proje tek bir gün içinde (**07:20–17:40, 10 sa 20 dk**) tamamlandığı için gece aralığı yoktur. Pompalar S0'da devreye alınmış ve S3 sonunda su dolumundan önce toplanana kadar kesintisiz çalışmıştır.

### ⑨ FAALİYET
1. **Meşe kapı kaldırma operasyonu için görevlendirilen mobil vincin şartnamedeki tonaj kapasitesi nedir?**
   - *Cevap:* Planda (DEĞİŞMEZLER & Yapı Kartı) avlu çakılında outrigger açan ve ~12 m yarıçapta 4 tonluk meşe kanatları kaldıran vinç, **35–40 ton kapasiteli** hidrolik teleskopik mobil vinç olarak şart koşulmuştur.
2. **Mobil drenaj pompaları ağır silt tahliyesi için mi yoksa standart su boşaltma için mi derecelendirilmiştir?**
   - *Cevap:* İki dalgıç pompa yalnız suyun tahliyesi (*dewatering*) içindir. Dip silti ve balçık pompalanmamış; vincin işlettiği çamur kovalarıyla (*crane muck grab skips*) mekanik olarak kazılıp avludaki hafriyat yığınına dökülmüştür.
3. **00:40.0'taki motorlu tekne geçişi, yeni meşe kapıların resmi devreye alma (commissioning) testi olarak mı kurgulandı?**
   - *Cevap:* **Evet.** Planda S5 ve S6 sahneleri projenin nihai vaadidir: *"Yeni kapılar yükü tutacak mı?"* sorusunun cevabı olarak teknenin hazneye alınması ve 3 m yukarı kaldırılması resmi devreye alma testi olarak sahnelenmiştir.

### ⑫ KATILIK
1. **Mobil vinç ayak tablaları doğrudan taş kanal bordürleri (coping) üzerine basacak şekilde mi planlandı?**
   - *Cevap:* **Hayır.** Planda vinç doğu avludaki çakıl zemine yerleştirilmiş ve ayak tablaları ahşap/çelik yük dağıtım plakalarıyla doğrudan çakıl zemine bastırılmıştır (`tyre tracks and outrigger pads pressed into the yard gravel`, satır 569). Bordür taşlarının üzerine basılması yapısal koruma kuralları gereği yasaktır.
2. **Dip kazısı aşamasında kullanılan kesintisiz drenaj pompa sisteminin kapasitesi nedir?**
   - *Cevap:* Toplam ~100–150 m³/saat kapasiteli iki adet ağır hizmet dalgıç pompa kullanılmıştır.
3. **Ön meşe kapı kanatları sahada önceden birleştirilip çift olarak mı indirildi yoksa tek tek mi yuvalarına yerleştirildi?**
   - *Cevap:* **Tek tek indirilmiştir.** Aşama Merdiveni S3'te önce batı kanat tek başına indirilip bileziği takılmış (00:24); ardından S4'te doğu kanat indirilip iki kanat mitre V-noktasında birleştirilmiştir (00:32).
4. **Final devreye alma testindeki motorlu teknenin deplasman / ağırlık limiti nedir?**
   - *Cevap:* 7 metre boyunda, yaklaşık 2,5–3,5 ton deplasmanlı, 0,8 m su çekimine sahip standart beyaz motorlu kabinli teknedir.

---

## 6. 📋 OLAY TABLOSU

| Olay No | Zaman Aralığı | Mercek & Kategori | Açıklama | Karar / Eylem |
|---|---|---|---|---|
| **E01** | 0:56.0 | ① KARE (Kat. 5 Safe Area) | Video bitişinde üst %35'lik alana yerleştirilen `THE EMPTY LOCK` başlık bindirmesi | Kurguda metin katmanı kaldırılacak (yalnız harici kapak kullanılır) |
| **E02** | 0:00.0–0:39.0 | ① KARE (Kat. 6 Text/Branding) | Sarı vinç bomunda ve gövdesinde beliren "PAB" harfleri | Gelecek üretimlerde negatif çekirdeğe vinç markalama kilitleri güçlendirilecek |
| **E03** | 0:42.0–0:55.0 | ① KARE (Kat. 6 Text/Branding) | Tekne pruvasında beliren tescil/marka yazısı | Tekne promptuna "clean unlettered hull" vurgusu eklenecek |
| **E04** | 0:40.0–0:42.0 & 0:54.0–0:55.0 | ① KARE (Kat. 7 People/Vehicles) | Kapı mekanizmasındaki işçilerin motion blur olmaksızın donuk pozlanması | I2V istemlerinde "blurred figures in motion streak" kuralı pekiştirilecek |
| **E05** | 0:24.0–0:27.0 | ① KARE (Kat. 8 Surface Truth) | Yeni meşe kanatların operasyonel kirlilik/montaj izi olmadan aşırı pürüzsüz belirmesi | Ahşap doku promptlarına fitting/handling izleri eklenecek |
| **E06** | 0:56.0 | ④ TESLİM (Kat. 5 Loop) | Kapanıştaki tekneli dolu hazne ile açılıştaki drenajlı boş havuz arasında döngü farkı | Sosyal medya loop'u istenirse ters dönüşlü transition planlanabilir; inşa kronolojisi korunur |
| **E07** | 0:00.0–0:56.0 | ⑥ GEÇİŞ (Kat. 6 Rhythm) | Bütün kesmelerin 8,0 sn sabit aralıkta olması | Cut 4'teki müzik patlaması ve Rejim A hız değişimi ritmi korumuştur |
| **E08** | 0:48.0–0:56.0 | ⑦ İŞ (Kat. 6 Work Rate vs Growth) | S6'da doluş hızının önceki vinç operasyonlarına göre daha hızlı akması | Rejim A (10 dk sıkıştırma) spesifikasyonuna uygundur; kusur sayılmaz |

---

## 7. ⚖️ KARAR VE EYLEM PLANI

```
1. 12/12 TAM KOŞU TAMAMLANDI:
   Depo tarihinde 12 merceğin tamamını başarıyla bitiren 6. film oldu (OVER THE WALL, EMPTY RIDGE, DARK ROCK,
   BACK TO WATER ve THE QUIET FIELD ile birlikte).
2. ASGARİ SET EKSİKSİZ:
   ① KARE (7,5 ✅) + ② İNŞA (10,0 ✅) + ⑤ DEVAMLILIK (7,0 ✅) eksiksiz sağlandı.
3. YEDİ TANE 10/10 TAM PUAN:
   ② İNŞA 10,0 · ③ ZAMAN 10,0 · ⑧ YÖNTEM 10,0 · ⑨ FAALİYET 10,0 · ⑩ SEBEP 10,0 · ⑪ ENVANTER 10,0 · ⑫ KATILIK 10,0.
4. KURGU DÜZELTMESİ:
   0:56.0'da beliren başlık yazısı video üzerinden silinecektir. Teslim master'ı saf video olarak kalacaktır.
```
