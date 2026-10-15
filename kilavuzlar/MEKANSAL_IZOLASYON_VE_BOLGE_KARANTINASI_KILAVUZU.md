# 🛡️ MEKÂNSAL İZOLASYON VE BÖLGE KARANTİNASI KILAVUZU — kadrajda birden fazla dünya olduğunda

> Sabit kameralı, derinlemesine çoklu odak içeren inşaat ve dönüşüm timelapse filmlerinde (özellikle kanyon,
> uçurum, harabe ve geniş şantiye sahalarında) üretken video modelleri (DiT, MMDiT, I2V), mekânsal ve fiziksel
> sınırları ayırt edemez. Arka plandaki çatı sökümü ön plandaki açık terasa sıçrar; kanyon boşluğundan beton pompası
> filizlenir; kamyon kasasındaki yük vinç indirmeden takas olur ve aynı anda iki araç hareket ettiğinde vinç
> ekskavatöre dönüşür. Bu kılavuz, **mekânsal dikkat karantinasını, kontrollü mimari sözlüğü, araç ve yük
> tutarlılığını, zemin temas fiziğini ve montaj öncelik grafiğini** katı kurallara bağlar.
>
> Kaynak: A35–A38 · 15.10.2026 (`arastirma/SONUCLAR/A35…A38_GEMINI_HAM.md` · denetim `A35-A38_DENETIM.md`).
> Tetikleyen: THE SKY STATION (DERS 65–84) filminde yaşanan 20 ölçülmüş üretim ve QA arızası.
>
> ⭐ **Rapordan ve dersten inen kesin kurallar:**
>   - **Mekânsal Karantina:** Tek difüzyon ağında eşzamanlı bağımsız eylem odağı tavanı $N_{\max} = 3-4$ (§1).
>   - **Derinlik ve Bounding Box:** Her eylem normalize koordinat `[x1, y1, x2, y2]` ve metre cinsinden derinlik ($z$) ile cıvalanır (§1).
>   - **Bölge Dokunulmazlığı:** Değişmeyen açık alanlar pasif bırakılamaz; `STRICT ZONE IMMUNITY` kalkanıyla dondurulur (§1).
>   - **Yasaklı Terim:** "Truss" sözlükten tamamen çıkarılır (§2); piramidal uzay kafes ve köşk tetikler (DERS 80).
>   - **Eşsesli İzolasyonu:** Çatı kaplamasında asla "decking" geçmez (`corrugated steel roof sheathing`); zemin `concrete slab` (§2).
>   - **"Exit Before Swap":** Kasasındaki yük değişecek araç sahnede dururken takas yapılamaz; araç kadrajdan çıkmalıdır (§3).
>   - **Tek Hareketli Aktör ($N_{\max} = 1$):** Sahnede aynı anda yalnızca TEK araç dinamik hareket yapabilir; diğer tüm makineler motor kapalı park edilir (§4).
>   - **Amaçlı İş Döngüsü:** Rölanti döngülerini önlemek için `Active Subject + Initial Anchor + Deterministic Vector + Target + Stop` sözdizimi zorunludur (§4).
>   - **Boşluk Dokunulmazlığı:** Uçurum ve kanyon boşlukları `structurally immune void space` ilan edilir; hayalet bomlar negatif kalkanla engellenir (§5).
>   - **Zemin Şasi Kökü:** Havada asılı bağımsız uzuv yasaktır; her bom yerde duran tek bir şasiye bağlı olmak zorundadır (§5).
>   - **Montaj Önceliği (DAG):** Öncülü ($\text{Pre}(E_i)$) bitmemiş eleman metne giremez; gökten hazır blok inmesi ve temassız kabin yasaktır (§6).
>   - **Geriye Yıkım Kilidi:** Difüzyonun zamansal simetrisi aşama kapılama ile kırılır; taze imalat geri sarılarak sökülemez (§6).
>   - **Akustik İzolasyon:** Video promptundan müzikal kelimeler %100 temizlenir; Attention Triangle paraziti sıfırlanır (§7).

---

# 0. 🚪 KURAL — KADRAJDA ÇOKLU ODAK VE FİZİKSEL DOKUNULMAZLIK

```
Kadraj bir bütün değildir; bağımsız fiziksel katmanların ve temas yüzeylerinin toplamıdır:
  1. EYLEM YALNIZCA BAĞLANDIĞI BÖLGEDE YAŞAR: metindeki hiçbir fiil ("lifting", "repairing", "building")
     bölgesiz yazılamaz. Her fiil bir derinlik katmanına ve Bounding Box'a cıvatalanır [A35-a · DERS 71].
  2. DEĞİŞMEYEN BÖLGE AÇIKÇA DOKUNULMAZ İLAN EDİLİR: sessiz bırakılan her açık yüzey difüzyon için potansiyel
     bir montaj alanıdır. Değişmeyen terasa 'STRICT ZONE IMMUNITY' yazılır [A35-d].
  3. YASAK KELİME KULLANILMAZ: 'truss' çatıya köşk diker; 'deck' terası çatıya katar [A36-b · DERS 80].
  4. YÜK SAHADA SİHİRLE TAKAS OLMAZ: araç kasasındaki malzeme değişecekse araç kadrajdan çıkar [A37-c · DERS 74].
  5. İKİ ARAÇ AYNI ANDA HAREKET EDEMEZ: hareket kapasitesi N_max = 1'dir. İkinci araç morflar [A37-b].
  6. BOŞLUKTAN MAKİNE FİLİZLENEMEZ: kanyon ve gökyüzü negatif alan kalkanıyla korunur [A38-a · DERS 81].
  7. ÖNCÜLÜ OLMAYAN YAPI TÜREYEMEZ: temel olmadan kolon, halat gerilmeden kabin metne giremez [A38-c · DERS 84].
  8. MÜZİK KELİMESİ VİDEO PROMPTUNA GİRMEZ: 'guitar' ve 'soundtrack' görüntüde parazit yapar [A36-d].
```

Ölçülmüş bedeli (THE SKY STATION · 35 sahne · DERS 65–84):

| Sahne / Klip | Ekranda Ne Oldu | Hangi Fiziksel / Mimari Kural Yoktu | İhlal Kodu |
| :--- | :--- | :--- | :--- |
| Clip 9 (DERS 71 · 1:04.0) | Ön plandaki açık beton terasa kendiliğinden çatı ve ahşap pergola örüldü, sonraki kesmede geri eridi. | Arka plandaki çatı söküm fiili ön plana sızdı; terasa bölge bağışıklığı verilmedi. | `ERR_SPATIAL_BLEED` |
| Clip 18 (DERS 80 · 2:16.0) | İstemdeki "truss" ve "deck" kelimeleri çatıyı aniden 4 piramidal köşke büktü; seyir peronuna çatı ördü. | Sözlük kalkanı yoktu; eşsesli ve tehlikeli kök kelimeler kullanıldı. | `ERR_TYPOLOGY_MUTATION` |
| Clip 12 (DERS 74 · 1:28.0) | Kereste yüklü kamyon dikişte iki ayrı moloz damperine bölündü; kasadaki yük sihirle takas oldu. | "Exit Before Swap" uygulanmadı; yük araç şasisine kilitlenmedi. | `ERR_PAYLOAD_SWAP` |
| Clip 16 (DERS 81 · 2:01.0) | Sağdaki dipsiz kanyon boşluğundan havaya doğru ikinci bir beton pompa bomu filizlendi. | Boşluk dokunulmazlığı (Void Immunity) ve sert zemin şasi kökü tanımlanmadı. | `ERR_VOID_SPROUTING` |
| Clip 22 (DERS 79 · 2:49.0) | Yerinde dökülen beton tabliye imalatı sürerken gökten monolitik hazır bir beton blok konduruldu. | Montaj adımları alt parçalara ayrıştırılmadı (Action Factorization çöküşü). | `ERR_SKYHOOK_SPAWN` |
| Clip 4 (DERS 78 · 0:23.0) | Yıkım sürerken yeni çatı bitirildi; eski yapının sökümü emredildiğinde taze çatı geriye doğru yıkıldı. | İnşaat öncelik grafiği (DAG) ve aşama kapılama uygulanmadı; zamansal simetri ihlal edildi. | `ERR_DEMOLITION_REGRESSION` |
| Clip 34 (DERS 84 · 4:32.0) | Taşıyıcı çelik halatlar gerilmeden avludan yolcu kabini kaldırıldı ve havada eridi. | Kinetik zincir ve temas kısıtları (Contact Constraints) denetlenmedi. | `ERR_CONTACT_VIOLATION` |

---

# 1. 📐 MEKÂNSAL BÖLGE KARANTİNASI VE BOUNDING BOX MİMARİSİ

Sabit kameralı bir zaman atlamalı kadrajında birden fazla eylem alanı veya derinlik katmanı bulunduğunda, difüzyon transformatörlerinin (DiT) küresel çapraz dikkat (global Cross-Attention) mekanizması eylem fiillerini kadrajdaki tüm benzer yüzeylere yayar.

```
       ┌─────────────────────────────────────────────────────────────┐
       │ GÖKYÜZÜ / BOŞLUK (Void Immunity: Sıfır makine / Sıfır yapı) │
       │                                                             │
       │   ZONE A: DEEP BACKGROUND (z = 120-160m)                    │
       │   [x: 10-45%, y: 15-40%] → Mikro Ölçekli Çatı Sökümü        │
       │                                                             │
       │   ZONE B: MIDGROUND (z = 20-50m)                            │
       │   [x: 25-75%, y: 35-70%] → Taş Duvar / Kemer Temizliği      │
       │                                                             │
       │   ZONE C: FOREGROUND BOARDING DECK (z = 1-5m)               │
       │   [x: 60-100%, y: 55-100%] → STRICT ZONE IMMUNITY           │
       │   ⛔ ÇATI YOK · PERGOLA YOK · VİNÇ YOK · STATİK BETON       │
       └─────────────────────────────────────────────────────────────┘
```

### 1.1. Sızmanın Matematiksel Sebebi ve RoPE Körlüğü
1. **Global Softmax Dağılımı:** Standart DiT katmanlarında Softmax işlemi $H' \times W'$ görsel gridinin tamamında çalışır. Metindeki "dismantling roof" veya "erecting structure" ifadesine ait Anahtar ($K_{\text{action}}$) vektörü, kadrajdaki tüm düzlem Sorgu ($Q$) vektörleriyle yüksek nokta çarpım üretir [arXiv:2604.10030].
2. **RoPE Derinlik Projeksiyonu Eksikliği:** 2D ve 3D Döner Konumsal Gömmeler (RoPE), piksellerin ekrandaki 2D komşuluklarını korur ancak metin token'ları ile 3D derinlik ($z\text{-depth}$) arasında koordinat eşlemesi kuramaz. Bu nedenle model $z = 140\text{m}$'deki arka plan harabe çatısı ile $z = 2\text{m}$'deki ön plan açık beton platformunu aynı eylemin parçası sanır [arXiv:2605.22344].
3. **Self-Attention Bulaşması (Feature Contamination):** Erken gürültü giderme evresinde ($t$) sızan zayıf çatı gürültüsü, izleyen Self-Attention katmanlarında benzer dokuya sahip ön plan terasında pekişir ve açık platformun üzerine kendiliğinden ahşap pergola örülür (DERS 71).

### 1.2. Eşzamanlı Bağımsız Eylem Odağı Tavanı ($N_{\max} = 3-4$)
Harici bir maskeleme yazılımı veya piksel seviyesinde inpainting hattı kullanılmadığında, tek bir metin istemiyle kontrol edilebilecek bağımsız eylem odağı sayısı **en fazla 3 ila 4 bölgedir** [arXiv:2410.23775, arXiv:2603.23924].
- Odak sayısı $N \le 3$: Bölgeler arası izolasyon Bounding Box ve derinlik etiketleriyle tam sağlanır.
- Odak sayısı $N = 4$: Sınır bölgelerinde hafif doku bulaşması görülebilir; negatif kalkan ağırlığı artırılmalıdır.
- Odak sayısı $N > 4$: Çapraz girişim (cross-talk) kaçınılmazdır; model nitelikleri (attributes) birbirine karıştırır. Kadraj bölünmeli veya sahneler sıralı çekilmelidir.

### 1.3. Bölge Karantinası Sözdizimi
Her I2V isteminde kadraj üç derinlik katmanına ayrılmalı ve her bölgeye şu üçlü kilit uygulanmalıdır:
1. **Normalize Bounding Box Koordinatı:** `[x1, y1, x2, y2]` (ekranın sol üstü `[0, 0]`, sağ altı `[100, 100]`).
2. **Fiziksel Derinlik ($z$):** Metre cinsinden derinlik aralığı (`z=2m`, `z=35m`, `z=140m`).
3. **Tekil Eylem Tahsisi (Action Attribution):** Eylem fiili yalnızca ait olduğu bölgeye yazılır (`ISOLATED ACTION ONLY`).
4. **Dokunulmazlık Deklarasyonu (`STRICT ZONE IMMUNITY`):** Eylemden muaf olan bölge metinde asla boş bırakılmaz. "STRICT ZONE IMMUNITY / ABSOLUTE UNTOUCHED REGION" etiketiyle açıkça statik ve çatı/yapı eylemlerinden muaf ilan edilir.

---

# 2. 🏛️ KONTROLLÜ MİMARİ SÖZLÜK VE TİPOLOJİ KİLİDİ

CLIP ViT-L/14 metin kodlayıcısının nedensel maskelemesi ve `<EOS>` token sıkıştırma darboğazı, birbirine yakın veya çok anlamlı (polysemous) mimari terimleri tek bir latent noktada toplar [arXiv:2412.04715]. Model, terimin bağlamını ayırt edemeyerek geometriyi aniden mutasyona uğratır.

### 2.1. Tehlikeli Terimler ve Güvenli Karşılıkları Tablosu

| Tehlikeli / Yasaklı Terim | Neden Mutasyon Doğurur | Kontrollü Güvenli Karşılık (Strict Token) | Negatif Kalkan (Negative Prompt) |
| :--- | :--- | :--- | :--- |
| **truss** ⛔ | Eğitim verisindeki uzay kafes ve köşklerle eşleşir; beşik çatıyı 4 sivri piramidal pavilyona büker (DERS 80). | `parallel dual-chord steel I-beam rafters` veya `horizontal steel purlin system` | `pyramidal roof, space frame, pavilion, gazebo, wood truss, triangular tower` |
| **deck / decking** ⛔ | Zemin döşemesi ile çatı kaplamasını çakıştırır; açık seyir terasının üstüne çatı örer (DERS 71). | Çatı için: `corrugated steel roof sheathing` / `metal panels`<br>Zemin için: `reinforced concrete ground boarding slab` | `roof decking, floor decking, timber deck, wood terrace platform` |
| **rafter** ⚠️ | Rustik kulübe ve dik sivri ahşap dikmeler üretir; modern veya endüstriyel çizgiyi bozar. | `linear steel roof purlins along longitudinal slope` | `exposed rustic rafters, pointed timber spire, wooden chalet roof` |
| **platform** ⚠️ | Askıda konsol terası kütlesel çatı katına veya kapalı odaya dönüştürür. | `open-air cantilevered reinforced concrete slab terrace` | `enclosed platform, roofed deck, two-story structure, overhead pergola` |
| **scaffold / staging** ⚠️ | Cephedeki geçici iskeleyi kalıcı bir çelik kafes cepheye (cage facade) dönüştürür. | `temporary exterior modular tubular steel pipe scaffolding` | `permanent steel grid, cage facade, structural steel enclosure` |
| **rock pinnacle / horn** ⚠️ | Kadraj köşesindeki dikey doğal kayayı heykel kaidesi veya gözetleme kulesi sanıp üstüne insan diker. | `barren natural monolithic granite cliff face, sheer bedrock` | `statue, monument pedestal, watchtower, carved human figure, castle ruin` |
| **beam** ⚠️ | Duvar lentosu, taşıyıcı kolon ve çatı aşığını birbirine karıştırır. | Duvarda: `horizontal reinforced concrete lintel`<br>Çatıda: `longitudinal steel purlin` | `random wooden beams, crossing rafters, ceiling grid` |

### 2.2. Tipoloji Kilidi Sözdizim Kuralı
Bir yapının geometrisi inşaat süresince korunacaksa, istemde **Bileşen Düzeyinde Tipoloji Kilidi** (`PRIMARY_TYPOLOGY_LOCK`) açılır:
- Çatı formu: `Locked typology: Dual-sloped steel purlin gable roof. No pyramidal roofs, no trusses.`
- Döşeme formu: `Locked typology: Ground-level cast-in-place reinforced concrete slab. No timber decking.`
- İskele formu: `Locked typology: Temporary modular tubular steel pipe scaffolding, partially enclosing facade.`

---

# 3. 🚚 DİKİŞLERDE YÜK KORUNUMU VE "EXIT BEFORE SWAP" PROTOKOLÜ

Sabit kameralı inşaat sahnelerinde kamyon, treyler veya vagonların üzerindeki malzemeler ardışık kesmelerde (cuts) ağır tutarsızlıklar üretir.

### 3.1. Yük Takası ve Cisim Ayrışmasının Sebebi
- **Unbound Attribute (Bağlanmamış Nitelik):** Model ters difüzyon adımında ($z_t \to z_0$) kamyon şasisinin düşük frekanslı geometrik hatlarını (tekerlekler, kabin) yapısal çapa olarak korur. Ancak kasadaki yükü veya vincin bomunu serbest bir nitelik (unbound attribute) olarak işler; kesme dikişinde gürültüden rasgele yeni inşaat nesneleri (ahşap makara yerine çelik makas veya moloz) türetir [arXiv:2411.15236].
- **Uzamsal Cisim Ayrışması (Spatial Object Splitting):** Dikişteki yüksek frekanslı belirsizlik, modelin tek bir kamyonun kapladığı hacmi iki ayrı ağırlık merkezi olarak algılamasına ve tek kamyonun iki ayrı damperliye bölünmesine yol açar (DERS 74).

### 3.2. ⭐ "Exit Before Swap" Protokolü
Kamyon şantiyede sabit dururken kasasındaki malzeme vinç veya iş makinesi tarafından fiziksel olarak indirilmediyse, **aynı aracın kasasındaki yük sonraki klipte ASLA değiştirilemez.**

```
⛔ YASAK (Sihirli Takas):
  Klip N   : Sarı kamyon şantiyede duruyor · kasasında 2 adet ahşap kablo makarası var.
  Klip N+1 : Aynı sarı kamyon aynı yerde duruyor · kasasında çelik çatı makasları var.
  SONUÇ    : MODEL MUTASYONA UĞRAR (makaralar makasa erir veya kamyon ikiye bölünür).

✅ KURAL ("Exit Before Swap"):
  Adım 1 (Klip N)   : Sarı kamyon kasasındaki kablo makaralarıyla doğrusal hatta hareket eder
                      ve klip bitmeden KADRAJDAN TAMAMEN ÇIKAR ("exits the frame completely").
  Adım 2 (Dikiş)    : Kadrajda araç yoktur; zemin temizdir.
  Adım 3 (Klip N+1) : Yeni yükü (çelik makaslar) taşıyan yeni bir araç yoldan sahaya girer
                      veya saha boş olarak imalata devam eder.
```

Araç kadrajdan tamamen çıktığında VAE latent uzayındaki uzamsal çapa sıfırlanır; model semantik çelişki yaşamaz ve metamorfoz halüsinasyonları tamamen engellenir [arXiv:2407.14505].

---

# 4. 🚜 TEK HAREKETLİ AKTÖR KURALI VE AMAÇLI İŞ DÖNGÜSÜ

Video difüzyon modellerinin uzamsal-zamansal dikkat katmanlarının aynı kadraj içindeki karmaşık dinamik etkileşim kapasitesi sınırlıdır.

### 4.1. Eşzamanlı Dinamik Aktör Kapasitesi ($N_{\max} = 1$)
- **Kapasite Sınırı:** Bir video sahnesinde modelin kimlik değişimi, eylem karışması ve görsel metamorfoz yaşamadan takip edebileceği hatasız maksimum hareketli araç sayısı **$N_{\max} = 1$** olarak ölçülmüştür [T2V-CompBench / arXiv:2407.14505, VBench++ / arXiv:2311.17982].
- **Performans Düşüşü:** Kadrajda aynı anda iki bağımsız hareketli araç ($N \ge 2$) tanımlandığında (örneğin forklift hareket ederken kule vincin dönmesi), hareket bağlanım ve etkileşim skorları **%42 oranında çöker**. Model A aracının hareketini B aracına bağlar; paletli kafes bomlu vinç forkliftin yanındayken bomunu kaybedip ekskavatöre dönüşür (`ERR_MORPH_IDENTITY`).
- **Kural:** Her klipte sadece ve sadece **TEK BİR** araç dinamik hareket yapabilir (`Active Dynamic Agent`). Sahnede görünen diğer tüm iş makineleri, vinçler ve kamyonlar tam stop ve park durumunda dondurulur (`strictly stationary, engine off, parked, zero movement`).

### 4.2. Amaçlı İş Döngüsü Sözdizimi (Purposeful Work Cycle)
Genel ve ucu açık fiiller ("forklift works in yard", "crane operates") yönelim belirsizliği (directional entropy) yaratır; araçların daireler çizmesine veya vinçlerin yükü indirip geri kaldırmasına (idle loops) yol açar.

**Zorunlu 6 Bileşenli Sözdizimi İskeleti:**
```text
[Active Subject] + [Initial Spatial Anchor] + [Deterministic Action & Kinematic Vector] + [Target Destination Spatial Anchor] + [State Change Completion Trigger] + [Background Static Vehicles Constraint]
```

**Uygulama Örneği:**
> `[Active Subject]:` A single yellow hydraulic crawler excavator,
> `[Initial Spatial Anchor]:` starting at the southern soil trench,
> `[Deterministic Vector]:` moves its articulated arm linearly to scoop earth and rotates exactly 90 degrees right,
> `[Target Destination]:` discharging the soil directly into the open bed of the parked dump truck,
> `[State Change Trigger]:` rests its bucket inside the bed and comes to a complete halt.
> `[Background Static Constraint]:` All other cranes and vehicles in the yard remain strictly stationary with engines off.

---

# 5. 🕳️ BOŞLUK DOKUNULMAZLIĞI VE ZEMİN DESTEĞİ FİZİĞİ

Difüzyon modelleri piksel gürültüsü giderirken (denoising) örtük 3D derinlik, yerçekimi ve mesnet kuvveti (ground reaction forces) hesaplamaz. Boşluklar, kanyonlar ve uçurum kenarları model tarafından düşük enformasyonlu latent alanlar olarak algılanır [arXiv:2609.23658].

```
                     HAVADA ASILI BOM YOK ⛔
                     [Uçurum Boşluğu: VOID IMMUNITY]
                       │
       ┌───────────────┴───────────────┐
       │   DİPSİZ KANYON BOŞLUĞU       │
       │   Zero machinery              │
       │   Zero phantom booms          │
       │   Zero ungrounded steel       │
       └───────────────────────────────┘
                       ▲
                       │
      [SERT KAYA ZEMİNİ] ══════════════════════════════
      ┌─────────────────────────┐
      │ Beton Pompası Şasisi    │ ← Şasi ve hidrolik ayaklar
      │ ve Hidrolik Ayaklar     │   sert zemine basmak ZORUNDADIR
      └─────────────────────────┘   (Strict Anchor Rule)
```

### 5.1. Fiziksel İhlal Mekanizmaları
1. **Boşluktan Filizlenen Hayalet Bom (DERS 81):** Ön plandaki zemin alanı dolduğunda, model eylem fiilini tamamlamak için serbestlik derecesi en yüksek olan bitişikteki kanyon boşluğuna kayar ve boşluğun ortasından tekerleksiz bir beton pompası kolu filizlendirir (`ERR_VOID_SPROUTING`).
2. **Kinetik Kök Kopukluğu:** Havada serbest uzanan kollar veya bomlar yerde duran bir gövdeye bağlanmadığında model bu parçayı bağımsız bir uçan nesne sanır.

### 5.2. Boşluk Koruma ve Zemin Teması Kuralları
- **Strict Anchor Rule:** Sahnedeki her iş makinesi, iskele veya vinç; tekerlekleri, paletleri veya hidrolik denge ayakları (outriggers) ile görünür, tanımlanmış sert zemin (kaya, beton, sıkıştırılmış toprak) piksellerine basmak zorundadır (`deployed outriggers firmly pressed into solid bedrock`).
- **Void Immunity Rule:** Uçurum, kanyon, vadi tabanı veya açık gökyüzü "dokunulmaz negatif alan" (`structurally immune void space`) ilan edilir. Pozitif komutta açık hava tamamen boş tanımlanır; negatif prompta kanyon filizlenmesi açıkça yazılır.
- **Kinematic Connection Rule:** Uzatılmış her bom veya vinç kolu, fiziksel olarak yerde duran tek bir ana şasinin döner tablasına (turntable) bağlı olmak zorundadır (`boom originates solely from truck turntable`).

---

# 6. 🏗️ İNŞAAT MONTAJ ÖNCELİK GRAFİĞİ (DAG) VE REGRESYON KALKANI

İnşaat mühendisliğinde montaj sırası Yönlü Döngüsüz Grafikler (Directed Acyclic Graph - DAG) ve Topolojik Sıralama ile yönetilir:

$$\forall E_i \in \text{Nodes}, \quad \text{State}(E_i, t) = \text{Assembling} \implies \forall E_j \in \text{Pre}(E_i), \quad \text{State}(E_j, t) = \text{Completed}$$

Bir yapı elemanının ($E_i$) montajına başlanabilmesi için, ona mesnetlik eden tüm öncül elemanların ($\text{Pre}(E_i)$) fiziksel olarak tamamlanmış olması zorunludur.

### 6.1. Difüzyonun Zamansal Zaafı ve Geriye Yıkım (DERS 78)
Difüzyon modellerinin zaman adımı kodlamaları (temporal embeddings) termodinamik tersinmezlik kısıtına sahip değildir; zaman ekseninde simetriktir [Temporal Symmetry in Video Diffusion]. Yıkım devam ederken yeni çatı tamamlandığında ve sonraki adımda eski harabenin sökümü emredildiğinde, model taze yapılan çatıyı yıkarak inşaatı geriye sarar (`ERR_DEMOLITION_REGRESSION`).

### 6.2. Montaj Öncelik Kuralları
1. **Yıkım ve Yapım Asla Çakışmaz:** Bir yapının yıkım ve temizlik fazı tamamlanmadan, aynı aks üzerine yeni yapı elemanı montajı metne yazılamaz.
2. **Gökten Monolitik Blok İndirilemez (DERS 79):** Yerinde dökülen beton veya çelik yapılarda, tek anlık kesmede hazır monolitik bloklar gökten indirilemez (`ERR_SKYHOOK_SPAWN`). İmalat kademeli adımlarla ilerler: kalıp kurulumu $\to$ donatı montajı $\to$ beton dökümü $\to$ kalıp sökümü.
3. **Önkoşulsuz Eleman Sahneye Giremez (DERS 84):** Teleferik kabini, raylı araç veya asma köprü tabliyesi; taşıyıcı çelik halatlar, kuleler ve mesnetler tamamlanıp gerilmeden sahneye sokulamaz (`ERR_CONTACT_VIOLATION`). Önkoşulu sağlanmayan eleman prompta yazılamaz.
4. **Aşama Kapılama (Stage Gating):** İki anahtar kare arasındaki imalat adımı görsel ve fiziksel olarak kararlı duruma gelmeden ($d_t \le \tau$) bir sonraki montaj fazına geçilemez [arXiv:2602.01100].

---

# 7. 🔇 AKUSTİK İZOLASYON VE ÇEVRESEL SES STANDARDI

Modern çok modlu video difüzyon modellerinde (MMDiT, HunyuanVideo, Sora türevleri), metin koşullandırması hem görsel hem de işitsel latent uzayları eşzamanlı yönlendirir [Attention Triangle / arXiv:2609.03586].

### 7.1. İşitsel Token Sızmasının Görsel Yıkımı
Metin isteminde yer alan müzikal veya soyut işitsel kelimeler (`acoustic guitar`, `orchestral soundtrack`, `ambient music enters`), çapraz dikkat katmanlarında görsel Sorgu ($Q_{\text{video}}$) vektörlerinin metindeki müzik Anahtarlarına ($K_{\text{audio}}$) bağlanmasına sebep olur.
- **Sonuç:** Model, inşaat sahnesinin ortasında fiziksel müzik enstrümanı illüzyonları (ahşap gitar sapına benzeyen kirişler) üretir ve karesel tutarlılık (FVD) çöker; sahneler arası titreme ve parazit ses patlamaları yaşanır [arXiv:2609.03586].

### 7.2. Akustik İzolasyon Kuralı
- **⛔ Kesin Müzik Yasağı:** Video prompt metinlerinden tüm müzikal, enstrümantal ve soundtrack tanımları %100 çıkarılır.
- **Yalnız Diegetik Çevre Sesi:** Eğer model ses üretiyorsa, promptta yalnızca şantiye ortamına ait doğal fiziksel sesler tanımlanabilir: `"distant mechanical hum, subtle wind blowing across canyon, concrete pouring sound"`.
- Prompt metninden müzikal ifadelerin çıkarılması görsel çapraz dikkatteki parazit aktivasyonları **%100 oranında engellemektedir** [arXiv:2609.03586].

---

# 8. 📋 STANDART İNGİLİZCE PROMPT ŞABLONLARI VE 10 MADDELİK QC KONTROL LİSTESİ

### 8.1. Standart Bölge Karantinalı ve Fizik Kilitli I2V Prompt Şablonu

```text
[CAMERA & SCENE SETUP]:
Ultra-high-resolution architectural timelapse, fixed single locked-off tripod perspective, zero camera pan, zero camera tilt, zero camera zoom, absolute stationary frame.

[DEPTH LAYER 1 - ZONE A - DEEP BACKGROUND (z=140m, Bounding Box: [10, 15, 45, 40])]:
Distant ruined station structure on the opposite canyon ridge. ISOLATED ACTION ONLY: Workers in orange safety vests methodically dismantling damaged stone roof elements and installing linear steel purlins strictly within the perimeter of this background structure. Micro-scale construction activity confined exclusively to Zone A.

[DEPTH LAYER 2 - ZONE B - MIDGROUND (z=30m, Bounding Box: [25, 35, 75, 70])]:
Historical arched stone station building. STATIC MONITORED STRUCTURE: Solid ashlar limestone walls remain structurally stable; natural sunlight shadow sweeps smoothly across stone arches. Strictly no roof work, zero crane activity, zero structural modifications in this zone.

[DEPTH LAYER 3 - ZONE C - FOREGROUND (z=2m, Bounding Box: [60, 55, 100, 100])]:
STRICT ZONE IMMUNITY / ABSOLUTE UNTOUCHED REGION. Cantilevered open-air concrete boarding platform extending over the gorge. The platform is completely flat, roofless, and wide open to the sky with original steel perimeter railings. STRICTLY NO ROOF, NO PERGOLA, NO BEAMS, NO CRANES, NO SCAFFOLDING, NO MATERIAL STORAGE ON THIS DECK. The concrete deck remains 100% unchanged, static, and clear throughout the entire shot.

[ACTIVE DYNAMIC AGENT & KINEMATICS (N=1 ONLY)]:
A single heavy yellow dump truck carrying securely fastened stone rubble in its bed drives linearly forward along the designated access path and exits the frame completely to the left. All other vehicles in the yard remain 100% stationary, parked with engines off.

[GROUND ANCHOR & VOID IMMUNITY]:
All vehicle tires and outriggers are firmly pressed into visible solid bedrock. The deep canyon gorge and open airspace on the right are structurally immune empty void spaces; zero floating machinery, zero crane booms sprouting from the canyon air, zero detached limbs.

[PRIMARY TYPOLOGY LOCK]:
ROOF: Locked typology: Dual-sloped steel purlin gable roof. No pyramidal roofs, no trusses, no wooden rafters.
FLOOR: Locked typology: Ground-level cast-in-place reinforced concrete slab. No timber decking, no elevated wood platforms.

[CROSS-ATTENTION ISOLATION RULE]:
All construction verbs apply EXCLUSIVELY to ZONE A. Zero feature leakage to Zone C.

[NEGATIVE PROMPT SHIELD]:
(roof on foreground deck:1.5), (wooden pergola over platform:1.5), (crane boom sprouting from canyon void:1.5), (phantom machinery:1.5), (floating concrete pump boom:1.5), (sky hooks:1.4), (pyramid roof, gazebo, pavilion, space frame:1.4), (roof decking, timber rafters:1.4), (backward demolition, undoing construction:1.4), (payload morphing, truck splitting:1.4), (floating cable car without cables:1.5), (statue, pedestal, watchtower on cliff:1.4), acoustic guitar, orchestral music, soundtrack, dynamic camera, panning, tilting, visual bleed.
```

---

### 8.2. Dikiş ve Üretim Öncesi 10 Maddelik Denetim Listesi (Checklist)

Her I2V klip istemi modele gönderilmeden önce bu 10 madde denetlenir; tek bir ❌ varsa istem **ÜRETİLEMEZ (BLOCK)**:

1. **[ ] Bölge Koordinatı ve Derinlik:** Kadrajdaki tüm odakların normalize Bounding Box koordinatları `[x1, y1, x2, y2]` ve metre cinsinden derinliği ($z$) tanımlandı mı? [A35-a]
2. **[ ] Bölge Bağışıklığı (`STRICT ZONE IMMUNITY`):** Değişmemesi gereken açık alanlar (seyir terası, avlu) açıkça dokunulmaz ve çatı/yapı eylemlerinden muaf ilan edildi mi? [A35-d]
3. **[ ] "Truss" Sözlük Temizliği:** İstem metninden ve negatiften `truss` kelimesi tamamen çıkarıldı mı? Yerine `parallel dual-chord steel I-beam rafters` veya `steel purlins` yazıldı mı? [A36-b · DERS 80]
4. **[ ] "Deck" Hijyeni:** Çatı kaplaması için asla `decking` kullanılmadığı (`corrugated steel roof sheathing` yazıldığı), zemin için `concrete slab` yazıldığı doğrulandı mı? [A36-c]
5. **[ ] "Exit Before Swap" Doğrulaması:** Kasasındaki yük değişecek olan araç, mevcut klibin bitiminden önce kadrajdan tamamen çıktı mı? Sahada duran aracın yükü değiştirilmedi mi? [A37-c · DERS 74]
6. **[ ] Tek Hareketli Aktör ($N_{\max} = 1$):** Sahnede dinamik hareket eden araç sayısı bire indirildi mi? Diğer tüm iş makineleri `strictly stationary, engine off` ile donduruldu mu? [A37-b]
7. **[ ] Boşluk Dokunulmazlığı (Void Immunity):** Kanyon, uçurum ve açık hava boşlukları için `structurally immune void space` kalkanı yazıldı mı ve negatifte kanyon filizlenmesi yasaklandı mı? [A38-a · DERS 81]
8. **[ ] Sert Zemin Şasi Kökü:** Sahnedeki her aracın ve bomun tekerlek/ayaklarının sert zemine bastığı ve bomun tek bir şasiye bağlı olduğu teyit edildi mi? [A38-b]
9. **[ ] Montaj Öncelik Sırası (DAG):** Üretilen elemanın taşıyıcı öncülleri (temel, kolon, kablo) tamamlandı mı? Yıkım devam ederken yeni çatı bitirilmedi mi? [A38-c, A38-d · DERS 78, 84]
10. **[ ] Akustik Temizlik:** Video prompt metninden tüm müzik, enstrüman ve soundtrack kelimeleri tamamen çıkarıldı mı? [A36-d]
