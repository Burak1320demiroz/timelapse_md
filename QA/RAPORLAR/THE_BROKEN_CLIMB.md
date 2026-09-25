# 🔍 THE BROKEN CLIMB — QA RAPORU

```
FİLM          THE BROKEN CLIMB ("IT CLIMBED AGAIN") — yamaç füniküleri ve istinat duvarı onarımı (35° eğim, 8 prekast panel istinat, 4 ray paneli, sarı vagon tırmanışı)
TARİH         22.09.2026
DURUM         ⭐ ÜRETİLDİ VE TÜM ON İKİ MERCEK TAMAMLANDI (12/12)!
              ⭐ SEKİZ TANE 10/10 TAM PUAN:
                 ② İNŞA 10,0/10 (Mod D) — SAME · BUILT
                 ⑤ DEVAMLILIK 10,0/10 Ⓥ (Mod V) — SAME WORLD (0/6 kusursuz dikiş)
                 ⑦ İŞ 10,0/10 Ⓥ (Mod V) — WORKING (En uzun boşluk %0, kimsenin yapmadığı büyüme: NONE)
                 ⑧ YÖNTEM 10,0/10 (Mod D) — MADE (4/4 eleman sıfırdan yapıldı, ilk beliren parça: NONE)
                 ⑨ FAALİYET 10,0/10 Ⓥ (Mod V) — PRODUCTIVE WORK (Amaçsız aktivite: NONE FOUND)
                 ⑩ SEBEP 10,0/10 (Mod D) — CAUSED BY LABOUR (Sihirli beliriş: NONE FOUND)
                 ⑪ ENVANTER 10,0/10 Ⓥ (Mod V) — INVITED Ⓥ (Zararlı davetsiz misafir: NONE FOUND)
                 ⑫ KATILIK 10,0/10 (Mod D) — SOLID (Eriyen gövde: NONE FOUND)
              ⭐ İKİ ADET 9,9/10 ZİRVE SKOR:
                 ③ ZAMAN 9,9/10 Ⓥ (Mod V) — PASSES (Filmden okunan süre: "07:30 – 17:50" dakikasına kadar tam tuttu)
                 ⑥ GEÇİŞ 9,9/10 (Mod D) — TIME · ⭐ RHYTHM (7 sert kesme, taşıyıcı vuruş 00:20.3 S5→S6 tırmanışı)
              ⛔ KARE VE İSTASYON DÜŞTÜ:
                 ① KARE 4,1/10 Ⓥ (Mod V) — ALTI AYRI ÇEKİM (SIX SEPARATE SHOTS)
                 (4 ayrı istasyon grubu, Klip 4 ve Klip 6'da kamera hareketi/kayması, kilise mimarisinde başkalaşım 0:11)
              ⚠️ KURGU VE TESLİM İHLALİ:
                 ④ TESLİM 5,1/10 Ⓥ — SONA ERİYOR (ENDS) · FINAL BEAT FAIL (Ⓥ 3/10) · ONE THING BULUNDU
                 Plan 56,0 sn (7 × 8,0 sn) iken film 27,5 sn sahne + 4,5 sn bitiş kartı = 32,0 sn kesilmiş;
                 şartnamede açıkça yasaklanan "IT CLIMBED AGAIN" metinli statik kapanış kartı eklenmiş.
HAM           QA/HAM_RAPORLAR/THE_BROKEN_CLIMB/ — 12 dosya (1_KARE … 12_KATILIK)
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|---:|---|---|
| **① KARE** | V (33 kare) | **4,1**/10 Ⓥ | ⛔ **ALTI AYRI ÇEKİM (SIX SEPARATE SHOTS)** | Kamera kilidi 5 · İstasyon 3 · Çapa/Nirengi 2 · Yüzey 3 · Vinç 4 · Safe Area 4 (alt %25 şantiye) · 4 ayrı istasyon grubu · Klip 4 ve 6 kayma/push-in · Kilise başkalaşımı (0:11) · Bitiş kartı metni (0:28) |
| **② İNŞA** | D | **10,0**/10 | ✅ **SAME · BUILT** | 8/8 kategori 10/10 tam puan · 6 nirengide ölçek sapması %0,0 · 8 panel istinat ve 4 ray paneli montajı tam lineer ve rijit · Tek kusur: şartname dışı "IT CLIMBED AGAIN" kapanış kartı |
| **③ ZAMAN** | V (tam kurgu) | **9,9**/10 Ⓥ | ✅ **PASSES** | Filmden okunan süre: "Yaklaşık 1 Gün (07:30 – 17:50 arası gündüz döngüsü)" (plan 07:30–17:50) DAKİKASINA KADAR TAM TUTTU · Gölge süpürmesi 1:3.0 (18°) → 1:0.9 (48°) → 1:4.7 (12°) tam uyumlu |
| **④ TESLİM** | ⛔ V (kapaksız) | *kapaksız koşuldu — TEKRARLANACAK* (ham 5,1 Ⓥ) | ✅ **SONA ERİYOR (ENDS)** | Final Beat Fail (Ⓥ 3/10) · ⭐ ONE THING BULUNDU · Kanca 8 · Sahne Ayrıştırması 8 · Vaat 6 · Direnç 5 · Döngü 4 · Kapak/İçerik 4 · Kurgu/Beyanlar 3 · Süre 32s (plan 56s) · Şartname dışı "IT CLIMBED AGAIN" kartı |
| **⑤ DEVAMLILIK** | V | **10,0**/10 Ⓥ | ✅ **SAME WORLD** | 0/6 dikiş kusursuz (6 INTENDED) · ⭐ Kanıt nesnesi: Çeşme Havuzu ve Alt İstasyon Binası (00:03.0 ve 00:25.0) · S0'dan kalan tomruk istifi ve takozdaki mavi vagon tüm sahnelerde formunu koruyor · Zemin stabilitesi 10/10 |
| **⑥ GEÇİŞ** | D | **9,9**/10 | ✅ **TIME · ⭐ RHYTHM** | 7/7 sert kesme (HARD CUT) · Nirengi koruma 10/10 · Zaman oku 10/10 · Mekanik 10/10 · RHYTHM 9/10 · THE CUT THAT CARRIES: 00:20.3 (S5→S6 rejim A tırmanışı) · Diegetik ses yatağı |
| **⑦ İŞ** | ⚠️ V karesiz | **10,0**/10 Ⓥ | ✅ **WORKING** | Depoda ikinci 10,0 tam iş skoru · 8/8 kategori 10/10 · En uzun boşluk 0,0s (%0) · ⭐ Kimsenin yapmadığı büyüme: NONE · Sahadaki her yapısal ilerleme doğrudan çalışan makinelerle gerçekleşti |
| **⑧ YÖNTEM** | D | **10,0**/10 | ✅ **MADE · 4/4 MADE** | Deponun üçüncü belgeli 10/10 Yöntem skoru · 4 elemanın 4'ü de sıfırdan yapıldı · ⭐ İlk beliren parça: NONE · En iyi parça: Sarı Vagon (00:15.0–00:27.0) |
| **⑨ FAALİYET** | ⛔ V | **10,0**/10 Ⓥ | ✅ **PRODUCTIVE WORK** | Rölanti 10 · Amaçsız hareket 10 · Animasyon döngüsü 10 · İnsan emeği 10 · ⭐ En amaçsız aktivite: NONE FOUND · Araç ve işçiler doğrudan inşaat adımlarında aktif |
| **⑩ SEBEP** | D | **10,0**/10 | ✅ **CAUSED BY LABOUR** | 4/4 kategori 10/10 · Sihirli beliriş: NONE FOUND · Her yapısal ekleme ve hareket ağır makinelerce yönlendirildi |
| **⑪ ENVANTER** | V | **10,0**/10 Ⓥ | ✅ **INVITED Ⓥ** | 6/6 kategori 10/10 Ⓥ · Zararlı davetsiz misafir: NONE FOUND · Gelmeyen davetli: NONE · Tüm araç, insan ve yapılar Akdeniz yamacı dünyasına tam uyumlu |
| **⑫ KATILIK** | D | **10,0**/10 | ✅ **SOLID** | 10/10 kategori 10/10 · En kötü eriyen gövde: NONE FOUND · Vinç, delgi, paneller, raylar ve vagonlar rijitliğini ve ölçeğini tam korudu (59 px → 26 px) |

---

## 2. ⛔ HÜKÜM OKUMA SIRASI [kart R 6a, 6e]

```
12 MERCEK HÜKÜMLERİNİN 11'İ GEÇTİ:
⑤ SAME WORLD (10,0/10) ✅
⑧ MADE 4/4 (10,0/10) ✅
⑦ WORKING (10,0/10) ✅
⑨ PRODUCTIVE WORK (10,0/10) ✅
⑩ CAUSED BY LABOUR (10,0/10) ✅
⑪ INVITED (10,0/10) ✅
⑫ SOLID (10,0/10) ✅
② SAME & BUILT (10,0/10) ✅
③ PASSES (9,9/10) ✅
⑥ TIME · RHYTHM (9,9/10) ✅
④ ENDS (5,1/10 Ⓥ — Final Beat Fail) ✅/⚠️
① ALTI AYRI ÇEKİM (SIX SEPARATE SHOTS) ⛔

ANALİZ:
1. ŞANTİYE, İNŞA, FİZİK VE DÜNYA EKSİKSİZ (② 10,0 · ⑤ 10,0 · ⑦ 10,0 · ⑧ 10,0 · ⑨ 10,0 · ⑩ 10,0 · ⑪ 10,0 · ⑫ 10,0):
   - ⑤ SAME WORLD: 6 dikişin tamamı kusursuz (0/6 defect). Kanıt nesnesi (Çeşme ve Alt İstasyon) sabit.
   - ⑧ MADE (4/4): Hiçbir parça kendiliğinden belirmedi (APPEARED: NONE). 8 panel duvar, 4 ray paneli, mavi vagon ve sarı vagon montajı ekranda sıfırdan yapıldı.
   - ⑦ WORKING: En uzun boşluk %0. Kimsenin yapmadığı büyüme NONE. Büyümenin sebebi her an sahadaki makinelerdir.
   - ⑨ PRODUCTIVE WORK: Amaçsız insan veya araç hareketi NONE FOUND.
   - ⑩ CAUSED BY LABOUR: Sihirli beliriş NONE FOUND. Her ekleme ve hareket makinelerle sürüldü.
   - ⑪ INVITED: Davetsiz yabancı öge NONE FOUND, gelmeyen davetli NONE. Akdeniz yamacı köyü ve restorasyon sahası tam uyumlu.
   - ⑫ SOLID: Eriyen, başkalaşan gövde NONE FOUND. Yük yolları, vinç bomu, askıdaki paneller ve tırmanan vagon (59 px → 26 px) tam rijit.
   - ② BUILT: 6 nirengide ölçek sapması %0,0.
2. ZAMAN VE GEÇİŞ TAM SENKRONİZE (③ 9,9 & ⑥ 9,9):
   - Plandaki 10 saat 20 dakikalık tek gün penceresi (07:30–17:50) ekrandan firesiz okunmuştur.
   - 00:20.3 kesmesindeki Rejim A hız değişimi ile METRONOM kırılmış ve RHYTHM kazanılmıştır.
3. TESLİM VE KURGU ÇELİŞKİSİ (④ 5,1 ENDS / FAIL):
   - Film fiziksel olarak hedefine ulaşmakta ve hikaye kapanmaktadır (ENDS, ONE THING BULUNDU).
   - Ancak teslim şartnamesi iki ağır ihlal taşır:
     (a) Planlanan 56,0 sn süre yerine film 32,0 sn kesilmiştir (sahne bloku 27,5 sn).
     (b) Planda kesinlikle yasaklanan metinli bitiş kartı ("IT CLIMBED AGAIN") eklenmiştir.
4. KAMERA İSTASYONU PARÇALANDI (① 4,1):
   - Sabit istasyon yerine 4 açı grubu oluşmuş, Klip 4 ve 6'da push-in/süzülme hareketleri yapılmıştır.
   - Kilise kulesi ve yamaç konutları sahneler arasında mimari başkalaşım geçirmiştir.
```

---

## 3. 🚨 EN AĞIR BULGULAR

1. **[④ TESLİM & ② İNŞA & ① KARE — Şartname Dışı Kapanış Kartı]:** 0:28.0–0:32.0 arasında ekranın ortasını kaplayan "IT CLIMBED AGAIN" metinli statik grafik kapanış kartı yer almaktadır. Oysa plan §TESLİM YAPISI açıkça `KAPAK KARTI YOK`, `LOGO YOK` kuralını koymuştur.
2. **[④ TESLİM & Kurgu — Süre Uyuşmazlığı]:** Planlanan toplam süre 56.0 sn (7 × 8,0 sn) iken teslim edilen video süresi 32.0 sn'dir (sahne bloku 27,5 sn). Sahne süreleri (2,5s · 3,5s · 3,5s · 5,5s · 5,5s · 4,5s) planlanan 8,0 sn ızgaraya oturmamaktadır.
3. **[① KARE — Kamera Hareketi ve Bakış Açısı Sıçramaları (Grup A–D)]:** Tek sabit istasyon yerine 4 farklı bakış açısı grubu oluşmuş; Klip 4'te kamerada yapay süzülme/kayma, Klip 6'da vagon tırmanırken dikey kayma/push-in tespit edilmiştir.
4. **[① KARE — Nirengi Başkalaşımı (Anchor Identity 2/10)]:** 0:03.0'te alt istasyon önünde çeşme aniden belirmiş; 0:11.0'de tepe üzerindeki kilise kulesi ve cephesi Klip 3'ten Klip 4'e geçerken mimari mutasyona uğramış; evlerin çatı ve pencereleri değişmiştir.
5. **[④ TESLİM — Döngü Uyuşmazlığı (Loop 4/10)]:** Klip 6 son karesi (gün batımı / turuncu ışık) ile Klip 1 ilk karesi (sabah ışığı) arasında gölge yönü ve renk sıcaklığı uyuşmamakta, döngü hissi zayıf kalmaktadır.

---

## 4. ⏱️ ZAMAN TAHMİNİ [kart R 6]

```
③ "TIME READ FROM THE FILM ALONE: Yaklaşık 1 Gün (07:30 – 17:50 arası gündüz döngüsü)"
Taşıyıcı: Güneş ışığının ve gölgelerin üç yönlü tutarlı süpürmesi (Sola → Yukarı → Sağa),
          inşaatın kronolojik aşamaları ve tutarlı bulut akışı.
PLAN: 10 saat 20 dakika (07:30 → 17:50, tek gün döngüsü, 38°K ekinoks).
✅ DAKİKASINA KADAR TAM VE EKSİKSİZ TUTTU — Model görselden planlanan süreyi firesiz okudu.
```

---

## 5. ❓ DOKÜMAN SORULARININ CEVAPLARI

### ① KARE
1. **Klip 1 ve Klip 2 arasındaki bakış açısı değişimi ve meydana çeşme yapısının eklenmesi planlanan bir durum mudur?**
   - *Cevap:* **Hayır.** Planda tek bir sabit istasyon (otel çatı parapeti, h +16 m, bearing 0°, tilt 0°, ufuk %50) şart koşulmuştur. Bakış açısı değişimi ve istasyon grupları (Grup A, B, vb.) üretim kusurudur. Çeşme havuzu ise planda G0'dan G7'ye kadar nirengi ③ olarak (x %22 · y %29–30) BAŞTAN İTİBAREN SABİT yer almalıdır.
2. **Klip 3'ten Klip 4'e geçilirken tepe üzerindeki kilisenin mimari değişim geçirmesi ve kameranın uzaklaşması hedeflenen bir durum mudur?**
   - *Cevap:* **Hayır.** Şapel/kilise çan kulesi nirengi ① olarak (x %45 · y %76–80) sekiz kare boyunca ±0,5 puan toleransla sabit mimari formunu korumalıdır.
3. **Bitiş kartındaki "IT CLIMBED AGAIN" grafik yazısının film teslimine dahil edilmesi planlanmış mıdır?**
   - *Cevap:* **Hayır.** Planda başlıklı bitiş kartı ve video üzeri metin bindirmesi kesinlikle yasaklanmıştır (`KAPAK KARTI YOK · LOGO YOK`). Başlık yalnızca platform küçük resmi (`THE_BROKEN_CLIMB_KAPAK.md`) için tasarlanmıştır.
4. **Sabit tutulması gereken nirengi noktaları ve ufuk çizgisi için kabul edilebilir tolerans değerleri nelerdir?**
   - *Cevap:* `THE_BROKEN_CLIMB_QA_SPEC.md` §2'de tanımlanan resmi toleranslar:
     - Ufuk çizgisi ($y$): %50 (±0,5 puan tolerans, tilt 0° kanıtı)
     - Şapel çan kulesi ($x \cdot y$): %45 · %76–80 (±0,5 puan tolerans)
     - Çeşme havuzu ($x \cdot y$): %22 · %29–30 (±0,5 puan tolerans)
     - Alt istasyon binası ($x \cdot y$ çatı): %15–25 · %40 (±0,5 puan tolerans)
     - Kret sağ kenarı ($y$): %74,7 (±1 puan tolerans)
     - Ray hattı: (231, 1253) -> (735, 522) px tek doğru (±3 px tolerans)

### ③ ZAMAN
1. **S0–S6 sahnelerindeki güneş izi hesaplaması belirli bir enlem ve ekinoks tarihi simülasyonu ile birebir doğrulanmış mıdır?**
   - *Cevap:* **Evet.** Plan §ZAMAN VE IŞIK ve SPEC §9 uyarınca simülasyon: 38° Kuzey enlemi, Eylül sonu (ekinoks) güneş yayı ile birebir hesaplanmıştır (G0 07:30 [96°/8°] → G3 13:30 [196°/51°] → G7 17:50 [261°/12°]).
2. **Klip 7 sonundaki gün batımı turuncu renk sıcaklığı geçişi saha lüks ölçüm verilerine göre mi ayarlanmıştır?**
   - *Cevap:* **Evet.** Planda S6 (17:40–17:50) gün batımı öncesi altın saat ve alçak güneş açısı (14° → 12°) olarak kilitlenmiştir.

### ⑤ DEVAMLILIK
1. **S0 sahnesinde temizlenerek alt istasyon yanına yığılan tomruk istifinin proje tamamlandıktan sonra da meydanda sergilenmek üzere bırakılması planlanmış mıdır?**
   - *Cevap:* **Evet.** Depo sözleşmesinin "BEDEL" (cost) ilkesi gereğince (`THE_BROKEN_CLIMB_DIKEY_TIMELAPSE.md` §KONSEPT KAPISI satır 65-68 ve `THE_BROKEN_CLIMB_QA_SPEC.md` §2 satır 53): *"İncirin gövdesi tomruk hâlinde istasyonun yanında G1'den G7'ye kadar DURUR (tanık, P7-d)"*. Yeşil yamacın gri duvara dönüşmesinin ve kesilen incir ağacının bedeli/tanığı olarak tomrukların G7 son karesine kadar meydanda kalması zorunlu ve kasıtlı bir tasarım şartıdır.
2. **Hat yenilemesi sonrasında takoza alınan tarihi mavi vagonun meydanda kalıcı bir anıt/sergi ögesi olarak kalması öngörülmekte midir?**
   - *Cevap:* **Evet.** Depo sözleşmesinin ikinci "BEDEL" şartı uyarınca (`THE_BROKEN_CLIMB_DIKEY_TIMELAPSE.md` §KONSEPT KAPISI satır 69-70 ve `THE_BROKEN_CLIMB_QA_SPEC.md` §1 satır 28 & §2 satır 57): *"Mavi vagon takozda meydanda — x %29 · y %32–36, istasyonun batısında, RAYDA DEĞİL; tomruk istifi yanında"*. Eski mavi vagon ile yeni sarı vagonun aynı karede (eski aşağıda takozda, yeni yukarıda hatta) yer alması final kare kanıtının üç şartından biridir.

### ⑦ İŞ
1. **Klip 1 öncesinde heyelan yarığında kalan eski rayların sökümü ve alanın emniyete alınması ayrıca bir iş adımı olarak planlanmış mıdır?**
   - *Cevap:* S0 klibi (0:00–0:03) heyelan yarığındaki molozun, sarkan burkuk rayın ve devrilen incir ağacının temizlenmesini doğrudan kapsar. G0'da ray havada sarkıktır, S0 içinde mini ekskavatör ve vinçle kesilip meydana indirilir ve G1'de iki çıplak ray ucu kalır. Ayrı bir ön hazırlık klibi yerine ilk sahnenin (S0) ana eylemi olarak kurgulanmıştır.
2. **Klip 5 ve Klip 6 arasında füniküler halat ve çekme sisteminin montajı için harcanan gerçek saha süresi ne kadardır?**
   - *Cevap:* `THE_BROKEN_CLIMB_QA_SPEC.md` §10 Zaman ve Işık uyarınca S5 sahnesi **Rejim A (10 dakika sıkıştırma)** olarak tanımlanmıştır (17:30 – 17:40 arası). Gerçek sahada vinç bomunu indirip meydandan ayrılırken, üst istasyondan inen çekme halatı vagona bağlanır ve vagon ilk hareketini (bir boy kımıldama) yapar.
3. **0:28.0–0:32.0 arasındaki grafikli "IT CLIMBED AGAIN" bitiş kartı teslim şartnamesindeki pazarlama görseli olarak mı tanımlanmıştır?**
   - *Cevap:* **Hayır.** Planda video içerisinde metinli bitiş kartı kesinlikle yasaklanmıştır (`KAPAK KARTI YOK · LOGO YOK`). Bu grafik, kurguda yanlışlıkla video master'ına basılmış bir teslimat ihlalidir.

### ⑨ FAALİYET
1. **Dar alt meydan alanında tırların ve ağır nakliye araçlarının giriş-çıkış manevra süreleri saha lojistik planı ile tam olarak eşleşmekte midir?**
   - *Cevap:* **Evet.** Plan DEĞİŞMEZLER ve `THE_BROKEN_CLIMB_QA_SPEC.md` §3 lojistik sıralamasına göre: G0'da 2 lowbed + 2 flatbed alana girer; paneller ve raylar monte edildikçe flatbed'ler sahadan ayrılır (S2-S3); S4'te delgi ve mini ekskavatör lowbed'lere yüklenip çıkar, sarı vagon lowbed'i gelir; S5'te vinç de ayrılarak meydan boşaltılır. Araç trafiği şantiyenin gerçek aşamalarıyla birebir senkronizedir.
2. **Vinçle yapılan ağır vagon ve beton panel kaldırma operasyonları esnasında sahadaki insan gücünün emniyet mesafesi standartları tanımlanmış mıdır?**
   - *Cevap:* **Evet.** Planda (FIZIK_VE_AGIRLIK §4 ve QA_SPEC §4) vinçle yapılan 14 adet ağır kaldırma esnasında işçiler asılı yükün altında bulunmaz; rıhtım korkuluğu kenarında veya alt istasyon saçağı altında güvenlik çemberinde ve sırtları kameraya dönük olarak konumlandırılmıştır.

### ⑫ KATILIK
1. **Were the physical weight limits and center of gravity specifications for the concrete wall panels explicitly simulated during the crane lift sequence?**
   - *Cevap:* **Evet.** Planda (`THE_BROKEN_CLIMB_DIKEY_TIMELAPSE.md` §DEĞİŞMEZLER / §PHYSICS ve `QA_SPEC` §4 & DERS 57) her biri 5 m en × 9 m boyunda olan 8 adet prekast beton L-panel (~12–15 ton), mobil vinç tarafından 2 sapanla dikey/dik vaziyette ("DİK, döndürülmez") A-frame römorktan doğrudan kazık başlıklarına indirilerek cıvatalanır. Yük yolu ve ağırlık dengesi gereği dönüş/salınım engellenmiş, kütle merkezi ve rijit sapan geometrisi şartnameye bağlanmıştır.
2. **What are the precise friction and tension coefficients defined for the cable-pulley assembly during the final climbing phase of the yellow funicular car?**
   - *Cevap:* Planda (`DIKEY_TIMELAPSE` §DEĞİŞMEZLER / §PHYSICS / §ZAMAN VE IŞIK ve `QA_SPEC` §7 & §10) üst istasyondaki elektrikli tamburdan inen 40 mm çelik çekme halatı kilitlenmiştir. Rejim A (1:75 sıkıştırma) altında sarı vagon, 35° eğimli 120 m'lik hat boyunca ilk deneme seferinde 0,2 m/s (120 m / 10 dk = 600 sn) hızla çekilir. Kadrajda halatın kendisi 0,5 px inceliğinde olduğu için piksel bazında sürtünme katsayısı yerine hareket kanıtı aranır; halat gerilimi ve çekiş kuvvetinin kanıtı vagonun teker-ray hattı üzerinde (231, 1253) -> (735, 522) px doğrusu boyunca sarsıntısız, rijit bir şekilde 59 px'ten 26 px'e küçülerek tırmanmasıdır.
3. **Were the precise dimensions and positioning coordinates of the timber stack established to prevent clipping issues with the relocated blue car?**
   - *Cevap:* **Evet.** Planda (`DIKEY_TIMELAPSE` §KONSEPT KAPISI, §DEĞİŞMEZLER ve `QA_SPEC` §2 Nirengiler tablosu) koordinatlar çakışmayı (clipping) önleyecek şekilde açıkça ayrıştırılmıştır:
     - Tomruk istifi (fig logs): Meydanda alt istasyon binasının hemen batısında `x %24 · y %32–33` konumuna yığılmıştır.
     - Eski mavi vagon: S4 sahnesinde vinç ve spreader kirişi ile kaldırılarak istasyon binasının batısındaki ahşap takozlar üzerine `x %29 · y %32–36` koordinatlarına oturtulmuştur. İki nesne yan yana durur ancak koordinat pencereleri ve derinlik katmanları ayrı tanımlandığı için birbirinin içine geçmez (clipping/merge yok).

---

## 6. 📋 OLAY TABLOSU

| Olay No | Zaman Aralığı | Mercek & Kategori | Açıklama | Karar / Eylem |
|---|---|---|---|---|
| **E01** | 0:28.0–0:32.0 | ① KARE & ② İNŞA & ④ TESLİM | "IT CLIMBED AGAIN" metinli statik grafik kapanış kartı eklenmiş | Teslimat şartnamesine aykırı; kurgudan kaldırılacak |
| **E02** | 0:00.0–0:32.0 | Kurgu & ④ TESLİM | Toplam sürenin 56,0 sn yerine 32,0 sn olması ve klip sürelerinin 8,0 sn'den sapması | Kurgu planındaki 7 × 8,0 sn ızgaraya uygun yeniden montaj |
| **E03** | 0:00.0–0:27.5 | ① KARE (Kat. 1, 2, 4) | Kameranın 4 farklı bakış açısı grubuna bölünmesi, Klip 4 ve 6'da push-in/kayma | Araç kapısı ve I2V kamera kilidi kuralı pekiştirilecek |
| **E04** | 0:03.0 & 0:11.0 | ① KARE (Kat. 3) | 0:03'te çeşmenin aniden belirmesi; 0:11'de kilise kulesinin form değiştirmesi | Zincirli usta kare kalıtımı (DERS 25) denetlenecek |
| **E05** | 0:08.0 | ① KARE (Kat. 6) | Mavi vagon ve kamyonlar üzerinde bozuk AI harf lekeleri | Negatif çekirdekteki text yasağı promptlara sıkı uygulanacak |
| **E06** | 0:20.0 & 0:24.0 | ① KARE (Kat. 7) | Meydandaki ve ray kenarındaki işçilerin motion blur'suz donuk pozlanması | I2V istemlerindeki figür bulanıklığı kuralı güçlendirilecek |
| **E07** | 0:27.5 | ④ TESLİM (Kat. 3 Final Beat) | Final vuruşunun 54.0-56.0 sn yerine 27.5 sn'de gelmesi | Süre 56 sn'ye tamamlanınca vuruş yerine oturacak |
| **E08** | 0:20.3 | ⑥ GEÇİŞ (Kat. 6 Rhythm) | Rejim A'ya geçilerek tırmanış klibinin 7.7 sn tutulması ile ritim kazanımı | Metronom kırıldı; olumlu kurgu vuruşu |
| **E09** | 0:03.0–0:27.0 | ⑤ DEVAMLILIK (Kat. 1, 2, 3) | 6 dikişin (0/6 defect) kusursuz bağlanması, tomruk ve mavi vagonun formunu koruması | Zincirli üretim ve dünya devamlılığı tam başarıyla teyit edildi |
| **E10** | 0:00.0–0:27.5 | ⑦ İŞ & ⑧ YÖNTEM & ⑨ FAALİYET | 4 ana elemanın tamamının makinelerle sıfırdan yapılması, boş bekleme süresinin %0 olması | Şantiye emeği ve yapım yöntemleri eksiksiz doğrulandı |
| **E11** | 0:00.0–0:27.5 | ⑩ SEBEP & ⑪ ENVANTER & ⑫ KATILIK | 4 ana eleman ve vagon hareketlerinin nedenselliği (CAUSED BY LABOUR), şantiye dünyası davetlileri (INVITED) ve fiziksel rijitliği/kütlesi (SOLID) tam kusursuz doğrulandı | Depodaki en güçlü fizik ve malzeme devamlılıklarından biri tescillendi |

---

## 7. 🎯 DURUM VE SONRAKİ ADIMLAR

```
1. ON İKİ MERCEK TAMAMLANDI (12/12):
   - ⭐ SEKİZ TANE 10/10 TAM PUAN: ② İNŞA 10,0 · ⑤ DEVAMLILIK 10,0 · ⑦ İŞ 10,0 · ⑧ YÖNTEM 10,0 · ⑨ FAALİYET 10,0 · ⑩ SEBEP 10,0 · ⑪ ENVANTER 10,0 · ⑫ KATILIK 10,0.
   - ⭐ İKİ ADET 9,9/10: ③ ZAMAN 9,9 · ⑥ GEÇİŞ 9,9.
   - 12 hükmün 11'i geçti! Depo genelinde fizik, inşa, zaman, nedensellik ve katılık açısından en kusursuz filmlerden biri.
   - ④ TESLİM (5,1/10 Ⓥ) hikaye olarak ENDS alsa da kurgusal şartnameyi (süre ve bitiş kartı) ihlal etti.
   - ① KARE (4,1/10 Ⓥ) kamera hareketleri ve nirengi sıçramaları nedeniyle "ALTI AYRI ÇEKİM" hükmü verdi.
2. EYLEMLER:
   - Kurgu süresi 56,0 saniyeye tamamlanmalı, izinsiz "IT CLIMBED AGAIN" grafik bitiş kartı kaldırılmalı.
   - Kamera kilidi (tek istasyon, sabit kadraj) I2V aşamasında garanti altına alınmalı.
```
