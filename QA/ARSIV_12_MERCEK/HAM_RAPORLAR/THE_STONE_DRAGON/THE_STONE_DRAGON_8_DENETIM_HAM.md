## 📋 QA AUDIT RAPORU: THE STONE DRAGON

**Üretim Durumu:** 🔴 **RED / REJECTED (QA Şartnamesi Kalite Kapılarından Geçemedi)**

**Referans Doküman:** `THE STONE DRAGON — QA ŞARTNAMESİ`

**Ölçülen Video:** 13 Sahne Klibi + 1 Statik Son Kart (00:00.0 – 00:59.0)

---

### 1. ⭐ FİNAL KARE (54,0 sn) VE SON KART DENETİMİ

| Şartname Maddesi | Beklenen Durum | Ölçülen / Gözlemlenen Durum | Sonuç |
| --- | --- | --- | --- |
| **① Su Akışı** | Ağızdan hazneye inen 296 px kesintisiz berrak su ipi. | Su ağızdan düzgün akıyor; ancak zemin çanağından dışarı taşan çamurlu/köpüklü su dağılımı süreksiz. | ⚠️ KISMEN |
| **② İki Renkli Taş** | Ağzın üstü kuru/soluk; ağzın altı ıslak/iki ton koyu. | Heykelin yüzeyinde ıslaklık/kuru ayrımı tutarsız; üst gövdede de ton koyulaşması var. | ❌ BAŞARISIZ |
| **③ Ham Kesim Bandı** | %30,16–34,13 bandında KURU ve SOLUK tanık bandı. | Model taşı aşamalar boyunca tamamen yeniden ürettiği için orijinal blok dokusu ve kesim bandı kaybolmuş. | ❌ BAŞARISIZ |
| **④ Bedel & Tanıkları** | Solda moloz yığını, sağda karot silindiri. | Solda moloz var; ancak sağdaki karot silindiri G3-G7 arasında boyut ve konum değiştirmekte. | ❌ BAŞARISIZ |
| **⭐ Son Kart (End Card)** | Final karesindeki fiziksel heykel ile birebir aynı form. | **KRİTİK UYUŞMAZLIK:** 00:55.5'te giren Son Kart'taki ejderha; devasa açık kanatlara, farklı gövdeye ve tamamen farklı bir çanağa sahiptir. AI jeneratörü son kartta farklı bir konsept görseli çizmiştir. | ❌ BLOCK |

---

### 2. KADRAJ KİLİTLERİ VE YAPI SÜREKLİLİĞİ (§2 & §5)

* **Portal Vinç (Gantry Crane) Kaybolması [00:43.8 → 00:44.0]:**
Filmin ilk 43 saniyesi boyunca sahnenin ana taşıyıcı elemanı olan dev çelik portal vinç, hiçbir söküm veya taşıma aşaması gösterilmeden 00:44.0 karesinde **aniden yok olmuştur**.
* **Geçici Makine Eklemeleri [00:15.8 → 00:16.0 / 00:23.8 → 00:24.0]:**
00:16.0 karesinde vinç kirişine entegre otomatik raylı testere ünitesi belirmiş, 00:24.0 karesinde ise kurulum/söküm izi bırakmadan aniden ortadan kaybolmuştur.
* **Kompresör ve Pompa Sıçramaları [00:39.8 & 00:47.8]:**
Hava kompresörü ve su pompası üniteleri sahaya dışarıdan taşınarak getirilmek yerine dikiş noktalarında ışınlanarak peydah olmuştur.

---

### 3. KİMLİK KAPISI — EJDERHA GEOMETRİSİ (§3)

```
G2 (00:08) ──► G3 (00:16) ──► G4 (00:24) ──► G5 (00:32) ──► G6 (00:40) ──► G7 (00:48) ──► END CARD (00:56)
   [Form 1]        [Form 2]        [Form 3]        [Form 4]        [Form 5]        [Form 6]        [FARKLI HEYKEL]

```

* **Hacim ve Kontur İhlali:** Model, oyma işlemini mevcut blok hacminden eksilterek yapmak yerine her sahnede ejderhanın baş, boynuz ve kanat açılarını yeniden tanımlamıştır.
* **Kanat ve Boynuz Rutubeti:** G4 ve G5 kareleri arasında kanat düzlemleri gövdeden dışarı doğru açılmakta ve boynuz uzunlukları dikiş geçişlerinde değişmektedir (Şartname §3 ihlali).

---

### 4. EKSİLTME KAPISI VE MALZEME DEFTERİ (§4)

* **Moloz Yığını Sıfırlanması (Resetting Rubble):**
* **00:02.8 → 00:03.0:** Ön zeminde moloz yığını aniden peydah oluyor.
* **00:06.8 → 00:07.0:** Ustaların temizlediği moloz yığını bir sonraki karede aniden eski hacmine geri dönüyor/resetleniyor.
* **00:45.8 → 00:46.0:** Gece çekiminden gündüze geçişte temizlenmiş avlu zemininde sıfırdan taze moloz yığını oluşuyor.
* **Zemin Atık Su Süreksizliği [00:23.8 → 00:24.0]:**
Sulu kesim sırasında zemini kaplayan yoğun gri çamurlu su, tek bir kesme arasında tamamen kuruyarak yok olmaktadır.

---

### 5. IŞIK, GÖLGE VE REJİM G (§6 & §8)

* **Işığın Mantıksız Sıçraması [00:41.8 → 00:46.0]:**
00:42.0'da alacakaranlık / gün batımı atmosferine geçildikten sonra 00:46.0 karesinde aniden tekrar dik gündüz ışığına dönülmekte, ışık günü sürekliliği bozulmaktadır.
* **Gölge Yönü Tutarsızlığı:**
Işık açısındaki ani sıçramalar sebebiyle bloğun ve heykellerin avluya düşen gölge açıları gün içi kronolojik süpürme sırasını ihlal etmektedir.

---

### 🚨 ZAMAN KODLU KUSUR LOGU (DEFECT LOG)

| Dikiş / Zaman | Kusur Tipi | Açıklama |
| --- | --- | --- |
| **00:02.8 → 00:03.0** | `DEFECT Ⓥ` | Temiz zemin üzerinde aniden büyük moloz yığını ve el arabası beliriyor. |
| **00:06.8 → 00:07.0** | `DEFECT Ⓥ` | Temizlenmekte olan moloz yığını aniden eski hacmine sıfırlanıyor. |
| **00:15.8 → 00:16.0** | `DEFECT Ⓥ` | Vincin üst kirişinde dikey kesim testere makinesi aniden beliriyor. |
| **00:23.8 → 00:24.0** | `DEFECT Ⓥ` | Testere makinesi yok oluyor; zemindeki yoğun çamurlu su 1 saniyede kuruyor. |
| **00:39.8 → 00:40.0** | `DEFECT Ⓥ` | Sol ön zeminde gri tanklı hava kompresörü aniden beliriyor. |
| **00:43.8 → 00:44.0** | `DEFECT Ⓥ` | **[KRİTİK]** Dev çelik portal vinç konstrüksiyonu sahneden tamamen kayboluyor. |
| **00:45.8 → 00:46.0** | `DEFECT Ⓥ` | Gece görünümünden gündüze sıçranıyor; temizlenen zeminde yeni moloz beliriyor. |
| **00:55.5 → 00:59.0** | `DEFECT Ⓥ` | **[KRİTİK]** Son Kart'taki ejderha görseli, S6'daki heykelden tamamen farklı bir AI görseli ile yer değiştiriyor. |

---

### 💡 SONUÇ VE RE-RENDER AKSİYON PLANI

1. **Portal Vinç Sabitlemesi:** Prompt kilitlerinde `portal gantry crane` varlığı G0'dan G7'ye kadar sabitlenmeli; 00:44'teki kaybolma engellenmelidir.
2. **Son Kart (End Card) Üretimi:** 00:55.5 sonrasındaki jenerik görseli bağımsız bir AI görselinden değil, S6 / G7 karesinin (00:54.0) yüksek çözünürlüklü dondurulmuş karesinden (freeze frame) türetilmelidir.
3. **ControlNet / Depth Lock (Kimlik Sıkılaştırma):** Ejderha geometrisindeki kaymaları önlemek için S1'den itibaren üretilen heykel kütlesi Depth/3D mesh referansı olarak sonraki sahnelere beslenmelidir.
4. **Zemin Temizliği:** Moloz yığınının ve atık suların dikiş geçişlerinde sıfırlanıp tekrar belirme süreci kronolojik bir temizlik mantığına oturtulmalıdır.
