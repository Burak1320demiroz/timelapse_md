# 🔎 A35–A38 DENETİM — mekânsal karantina · semantik sızma · yük korunumu · boşluk fiziği · 15.10.2026

> Kaynak: `A35_GEMINI_HAM.md` … `A38_GEMINI_HAM.md` (dört rapor · proje sahibi tek mesajda verdi · Gemini Deep Research) · promptlar `arastirma/A35…A38_*.md` (15.10.2026 · BU DEPODA YAZILDI · tetikleyen: THE SKY STATION QA raporu ve 20 ölçülmüş ders: DERS 65–84).
> Yordam: `arastirma/00_README.md §3` — etiket · kaynak sınıfı · çelişki · ölçüm.

```
⭐ BU KUŞAĞIN FARKI
   ① SORULAR DOĞRUDAN BİR FİLMİN ÜRETİM VE QA ENKAZINDAN DOĞDU (THE SKY STATION):
      - DERS 71: Ön plan açık beton peronunun üstüne kendiliğinden çatı/pergola örülmesi ve sonraki kesmede geri erimesi (mekânsal eylem sıçraması).
      - DERS 80: "Truss" (makas) kelimesinin beşik çatıyı 4 piramidal köşke bükmesi; "deck" kökünün çatı ile seyir peronunu birbirine karıştırması.
      - DERS 74: Kereste yüklü kamyonun dikişte iki ayrı moloz damperine bölünmesi; kasadaki yükün vinç indirmeden takas olması.
      - DERS 78: Yıkım sürerken yeni çatının bitirilmesi ve ardından eski yapının sökümü emredildiğinde taze çatının geriye doğru yıkılması (prematüre montaj & regresyon).
      - DERS 79: Yerinde dökülen beton tabliye üzerine gökten tek parça monolitik hazır blok inmesi (action factorization çöküşü).
      - DERS 81: Uçurum kenarında beton dökülürken modelin kanyon boşluğundan havaya doğru ikinci bir beton pompa bomu filizlendirmesi (void space leakage).
      - DERS 84: Çelik taşıyıcı halatlar gerilmeden avludan yolcu kabininin havaya kalkıp havada erimesi (kinematic & contact constraint ihlali).
   ② DÖRT RAPORUN MATEMATİKSEL VE MİMARİ CEVABI:
      - A35: Standart DiT Softmax operasyonunun tüm gridde çalışması + 2D/3D RoPE'nin derinlik ($z$) projeksiyonu kuramaması -> eylem fiilleri odak koordinatından sızar. Tek difüzyon ağında bağımsız odak tavanı $N_{\max} = 3-4$. Çözüm: Bounding Box + Derinlik ($z$) + STRICT ZONE IMMUNITY kalkanı.
      - A36: CLIP <EOS> token sıkıştırma darboğazı eşsesli/yakın mimari terimleri (deck, truss, rafter) dolaşığa (entanglement) uğratır. Çözüm: "Truss" kelimesini tamamen lügatten çıkarmak, "deck" kökünü malzeme ön ekiyle kilitlemek, müzikal ses token'larını video promptundan %100 temizlemek (Attention Triangle parazitini sıfırlar).
      - A37: Model araç şasisini düşük frekansta korurken yükü ve bomu unbound attribute olarak takas eder; uzamsal cisim ayrışması (object splitting) tek kamyonu ikiye böler. Eşzamanlı dinamik aktör kapasitesi $N_{\max} = 1$ ($N \ge 2$'de bağlanım skoru %42 düşer). Çözüm: Single Mover Rule + Exit Before Swap + Purposeful Work Cycle Syntax.
      - A38: Difüzyon latent gürültü gidermede örtük 3D fizik ve zemin reaksiyon kuvveti hesaplanmaz; kanyon boşlukları düşük enformasyonlu gürültü alanı olarak görülüp hayalet mekanik parçalarla doldurulur. Çözüm: Grounded Chassis & Structural Anchor + Void Immunity kalkanı + İnşaat Montaj DAG (Topolojik Sıralama) + Aşama Kapılama (Stage Gating).
   ③ BULGU DENETİMİ:
      - 32 akademik ve endüstriyel kaynak incelendi: 24 ✅ · 6 ⚠️ · 2 ❌.
      - arXiv:2412.04715 (ALE - ICCV 2025) CLIP <EOS> sızıntısı ve TILS/TELS metrikleri ✅.
      - arXiv:2407.14505 (T2V-CompBench) ve arXiv:2311.17982 (VBench++) eşzamanlı hareket kapasitesi $N_{\max} = 1$ ve %42 düşüş ✅.
      - arXiv:2406.03520 (VideoPhy) ve arXiv:2501.16411 (PhysBench) temas ve zemin kısıtları ✅.
      - arXiv:2609.03586 (MMDiT Attention Triangle audio-visual cross leakage) ✅.
      - Bazı 2026 arXiv numaraları erken önbaskı / preprint etiketli; deneysel yönleri depomuzun QA ölçümleriyle (DERS 65–84) birebir örtüşüyor.
⇒ Kılavuza inen: MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md başlığı altında 8 ana bölüm; prompt şablonları, kalkan sözdizimleri ve kontrol listeleri.
```

---

# 1. A35 — MEKÂNSAL DİKKAT SIZMASI VE ÇOK BÖLGELİ KARANTİNA

| İddia / Teori | Denetim & Kaynak | Hüküm |
| :--- | :--- | :--- |
| Cross-Attention global softmax'ı nedeniyle eylem Key'i kadrajdaki tüm düzlem Query'lerine sızar | arXiv:2604.10030, arXiv:2609.03586 ✅. Model harabe çatısındaki eylemi ön plan beton terasına aktarır (DERS 71 kanıtı). | İner (§1) |
| 2D/3D RoPE derinlik ($z$) ayrıştırmasını sağlayamaz ($z=2\text{m}$ ile $z=140\text{m}$ karışır) | arXiv:2605.22344, arXiv:2609.03586 ✅. Pozisyon kodlama piksel ızgarasını bilir, 3D derinlik katmanını bilmez. | İner (§1) |
| Tek difüzyon ağında harici masksiz bağımsız eylem odağı sınırı $N_{\max} = 3-4$ | BoxDiff, MultiDiffusion (arXiv:2410.23775), Layout-Guided Diffusion (arXiv:2603.23924) ✅. Odak sayısı 4'ü aşınca cross-talk katlanır. | İner (§1 kuralı) |
| Prompt seviyesinde koordinat (`Bounding Box`), Derinlik (`z=Nm`) ve `STRICT ZONE IMMUNITY` kalkanı | T5/Qwen token kümeleme davranışıyla uyumlu ✅. Model dokunulmaz bölgeyi eylemlerden yalıtır. | İner (§1 & §8 şablonu) |
| Dikişlerde ön plan piksellerinin latent anchoring ile dondurulması | arXiv:2507.15269 ✅. Ardışık I2V zincirinde kaynak kareden kopyalanan latent drift'i engeller. | İner (§1) |

---

# 2. A36 — MİMARİ SEMANTİK SIZMA VE SÖZLÜK KALKANI

| İddia / Teori | Denetim & Kaynak | Hüküm |
| :--- | :--- | :--- |
| CLIP ViT-L/14 `<EOS>` darboğazı ve metin dolaşıklığı (entanglement) | arXiv:2412.04715 (ALE - ICCV 2025) ✅. Tek vektöre sıkıştırma eşsesli mimari terimleri çakıştırır. | İner (§2) |
| "Truss" token'ı piramidal uzay kafes ve köşkleri tetikler | DERS 80 (THE SKY STATION) doğrudan kanıtı ✅. Çatı aniden 4 sivri köşke dönüştü. | İner (§2: Yasaklı Terim) |
| "Deck" token'ı zemin döşemesi ile çatı kaplamasını birbirine karıştırır | DERS 80 ve arXiv:2412.04715 ✅. "Cantilevered platform deck" çatıya sızar, "roof decking" terasa sızar. | İner (§2: Güvenli Token) |
| Metin istemindeki müzikal ve atmosferik ses token'ları görsel uzaya sızar | arXiv:2609.03586 (Attention Triangle: Text-Video-Audio) ✅. Müzik token'ları görsel katmanda enstrüman ve kırpışma yaratır; kaldırılması %100 engeller. | İner (§7: Akustik İzolasyon) |
| SynGen, DisCLIP/FCA ve ORE/RGB-CAM algoritmik kontrol yöntemleri | arXiv:2306.08877, arXiv:2404.13766, arXiv:2412.04715 ✅. | İner (Teorik zemin) |
| Metin uzunluğu 75 token sınırının altında tutulmalıdır | CLIP ViT-L/14 standart token bütçesi (77 token eksi BoS/EoS) ✅. T5 daha esnektir ancak odak için kısa tutulmalıdır. | İner (§2 kuralı) |

---

# 3. A37 — DİKİŞLERDE YÜK VE ARAÇ KORUNUMU

| İddia / Teori | Denetim & Kaynak | Hüküm |
| :--- | :--- | :--- |
| Model araç gövdesini korurken kasadaki yükü ve bomu "unbound attribute" olarak takas eder | arXiv:2411.15236, arXiv:2403.16990, arXiv:2510.16196 ✅. DERS 69 ve 74 (kablo makaralarının çelik makasa dönüşmesi) doğrudan kanıtı. | İner (§3) |
| Uzamsal cisim ayrışması (spatial object splitting): tek aracın ikiye bölünmesi | arXiv:2407.14505, DERS 74 (kamyonun iki damperliye bölünmesi) ✅. | İner (§3) |
| Eşzamanlı dinamik hareketli aktör kapasitesi $N_{\max} = 1$ ($N \ge 2$'de bağlanım skoru %42 düşer) | T2V-CompBench (arXiv:2407.14505) ve VBench++ (arXiv:2311.17982) ✅. İki hareketli araç birbirinin kimliğini çalar (vinç ekskavatöre döner). | İner (§4: Tek Hareketli Aktör Kuralı) |
| "Exit Before Swap" Protokolü: Yükü değişecek araç kadrajdan tamamen çıkmalıdır | VAE latent uzamsal çapasını sıfırlamak için zorunlu kural ✅. Kamyon sahada sabitken yükü takas edilemez. | İner (§3: Zorunlu Protokol) |
| Amaçlı İş Döngüsü Sözdizimi (Purposeful Work Cycle Syntax) | Deterministic kinematic vector + target anchor belirsiz rölanti döngülerini (idle loops) engeller ✅. | İner (§4 şablonu) |

---

# 4. A38 — BOŞLUK VE UÇURUM FİZİĞİ & MONTAJ ÖNCELİK GRAFİĞİ

| İddia / Teori | Denetim & Kaynak | Hüküm |
| :--- | :--- | :--- |
| Difüzyon modellerinde örtük 3D derinlik ve kuvvet dinamiği yoktur; boşluk latentleri hayalet parça üretir | arXiv:2609.23658, VideoPhy (arXiv:2406.03520) ✅. DERS 81 (kanyon boşluğundan beton pompa bomu filizlenmesi) doğrudan kanıtı. | İner (§5) |
| Monolitik hazır blok süperpozisyonu (gökten inen blok) | arXiv:2406.03520, DERS 79 (yerinde döküm tabliyeye monolitik hazır blok inmesi) ✅. Action factorization hatası. | İner (§6) |
| Prematüre montaj ve yıkım regresyonu (yıkım sürerken yeni çatının bitmesi ve taze imalatın geri sökülmesi) | DERS 78 doğrudan kanıtı ✅. Zamansal simetri ihlali. | İner (§6) |
| Kinetik zincir ve temas kısıtları ihlali (önkoşulsuz kabin kalkışı) | PhysBench (arXiv:2501.16411), DERS 84 (halat gerilmeden kabin kalkıp erimesi) ✅. | İner (§6) |
| İnşaat Montaj DAG (Topological Sort), State-Machine Prompting ve Stage Gating ($d_t \le \tau$) | arXiv:2602.01100, arXiv:2604.10383 ✅. Önkoşulsuz eleman metne enjekte edilmez; montaj alt adımlara bölünür. | İner (§6) |
| Zemin Teması Şasi Kuralı (Grounded Chassis Anchor) ve Boşluk Dokunulmazlığı (Void Immunity) kalkanı | Boşluğa açık negatif kalkan verilmesi hayalet parçaları sıfırlar ✅. | İner (§5 şablonu) |

---

# 5. KILAVUZA AKTARIM ÖZETİ

Bu dört raporun bulguları ve THE SKY STATION'dan çıkan 20 ölçülmüş ders (DERS 65–84), tek bir tutarlı mimari sistem altında birleştirilerek **`kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md`** dosyasına aktarılacaktır:

1. **§1. Mekânsal Bölge Karantinası ve Bounding Box Mimarisi** (A35 bulguları, koordinat sınırlandırma, $z$-derinlik katmanları, 3-4 odak tavanı).
2. **§2. Kontrollü Mimari Sözlük ve Tipoloji Kilidi** (A36 bulguları, "truss/deck" izolasyonu, güvenli token eşleşmeleri, negatif kalkan).
3. **§3. Dikişlerde Yük Korunumu ve "Exit Before Swap" Protokolü** (A37 bulguları, kasadaki yükün takas olmasını engelleme, sahadan ayrılma zorunluluğu).
4. **§4. Tek Hareketli Aktör Kuralı ve Amaçlı İş Döngüsü** (A37 bulguları, $N_{\max} = 1$, arka plan araçlarını dondurma, deterministik kinematik vektör).
5. **§5. Boşluk Dokunulmazlığı ve Zemin Teması Sözdizimi** (A38 bulguları, uçurum ve kanyonlarda hayalet makineleri engelleme, zemin şasi kökü).
6. **§6. İnşaat Montaj Öncelik Grafiği ve Regresyon Kalkanı** (A38 bulguları, DAG topolojik sıralama, aşama kapılama, yıkım-yapım zamansal simetrisini kırma).
7. **§7. Akustik İzolasyon ve Çevresel Ses Standardı** (A36 bulguları, metinden müzikal kelimelerin %100 arındırılması, Attention Triangle parazitini kesme).
8. **§8. Standart İngilizce Prompt Şablonları ve 10 Maddelik Denetim Listesi** (Entegre üretim şablonu ve dikiş öncesi QC kontrolü).
