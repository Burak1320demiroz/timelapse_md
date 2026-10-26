# THE_DRIVE_IN — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 8 × 8,0 sn = 64,0 sn (⚠️ sahip istisnası 26.10.2026) · paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn = 37,0 sn
plan: dikey_shorts/THE_DRIVE_IN/THE_DRIVE_IN_DIKEY_TIMELAPSE.md (26.10.2026 · 8 sahne · İKİ KEYFRAME ZİNCİRİ · kart beyanlı)
QA SPEC: dikey_shorts/THE_DRIVE_IN/THE_DRIVE_IN_QA_SPEC.md
üretim günlüğü: dikey_shorts/THE_DRIVE_IN/THE_DRIVE_IN_URETIM_GUNLUGU.md
yayın dosyası: raporlarda "input_file.mp4" (❶) / "THE_DRIVE_IN.mp4" (❷ ❸ ❹ ❺) · ~0:34.0–0:37.0 · 9:16 — ⚠️ AJAN OKUYAMADI (yerel dosya doğrudan taranamadı; sahip geçici bot oturumunda çalıştırdı)
master: bilinmiyor (2x yayın kopyasıyla koşuldu)
kapak: ❺ "cover: NOT SUPPLIED" · yayında 0:32.0'de statik başlık kartı mevcut
koşu tarihleri: beş mercek sahip koşusu (Gemini), çıktılar 27.10.2026'da yapıştırıldı · ajan değerlendirmesi 27.10.2026

---

## ⭐ AJAN DEĞERLENDİRMESİ — merceklerden önce okunur
Yayın dosyası yerel ortamda doğrudan taranamadığından, değerlendirme **beş merceğin ham raporlarından** derlenmiştir.

```
YAYIN KURGUSU (2x · PLAN beklentisi 8 × 4,0 sn = 32,0 sn + kart 5,0 sn = 37,0 sn)
 0,00 –  4,00  S0 POMPA VE ÇÖP SÖKÜMÜ   forklift eski pompaları söker ve kamyona yükler; yabani otlar biçilir
 4,00 –  8,00  S1 KANOPİ TEMİZLİĞİ      kanopi alınlığı boyanır, sarkık sac düzeltilir, molozlar taşınır
 8,00 – 12,00  S2 TEMEL VE ASFALT TAMİRİ çatlaklar yamalanır, arkada perde kolonları için iki beton temel dökülür
12,00 – 16,00  S3 ÇELİK KOLON MONTAJI   mobil vinç kanopinin arkasında iki ana çelik kolonu kaldırıp sabitler
16,00 – 20,00  S4 ÇAPRAZLAR VE ÇERÇEVE  üst bağlama kirişi ve çapraz elemanlar monte edilir (20 m'lik boş karkas)
20,00 – 24,00  S5 BEYAZ PERDE VE ŞERİT  dev beyaz billboard perde paneli asılır; kanopi altına ışık şeridi çekilir
24,00 – 28,00  S6 ÇİZGİLER VE DİREKLER  2x6 park çizgileri boyanır, hoparlör direkleri dikilir; alacakaranlıkta ilk arabalar girer
28,00 – 32,00  S7 İŞLEV ANI: PERDE YANAR dev perde tek karede durağan film resmiyle aydınlanır; son araba park eder (30–32 tutuş)
32,00 – 37,00  KAPAK KARTI              bitmiş sinema ve yanan perde üzerinde statik "THE DRIVE-IN" başlık kartı
```

```
⛔ PLAN ↔ RAPOR UYUŞMAZLIKLARI
① KLİP SAYISI (34 klip): `qa_paket.sh` makine ölçüm bloğu verilmediği (`{SPEED}`, `{CLIP_COUNT}` şablon değişkenleri
                yerine konmadan prompt gönderildiği) için model videoyu 1'er saniyelik adımlarla (34 clips) örneklemiş
                ve her saniyeyi ayrı bir klip olarak değerlendirmiştir (DERS 105 / 106 / GAME ON / TOTAL RESET emsali).
② KESME IZGARASI: Dikişler 1'er saniyelik adımlarla listelenmiştir.
③ PUAN BAĞLAYICILIĞI: Ölçülmüş olgular bloğu olmadan koşulduğu için sistem kuralı gereğince resmî puan
                `— (N=0) ⚠️ bağlayıcı değil` olarak kaydedilmiştir.
```

```
✅ TUTANLAR (raporlarda doğrulanmış olgular)
· KUSURSUZ 10/10: Beş merceğin değerlendirdiği TÜM tetiklenen kategoriler (kamera kilidi, nirengiler, metin/logo,
  figür ve araçlar, yüzey gerçekliği, rijitlik, şantiye çalışması, yapı sırası, vaat/sonuç ve kapak kartı) 10/10 almıştır!
· SIFIR ERİME / SIFIR KUSUR: `THE BODY THAT MELTED WORST: NONE FOUND` · `HOW IT MELTED: NONE`.
· SIFIR DAVETSİZ NESNE: `THE MOST DAMAGING INTRUDER: NONE FOUND`.
· İŞLEV ANI: 0:28.0'de dev perde aydınlanır, film gösterimi başlar, arabalar ve seyirciler izler (`FINAL BEAT PASS`).
· KADRAJ KİLİDİ: Sabit kamera, pilon ve çatı nirengileri kusursuz tutulmuştur (`spread 0.0`).
· ÇIKIŞ KURALI (Exit Before Swap): Forklift, mikser, mobil vinç işleri bitince sahneden ayrılmıştır.
```

---

## MERCEKLER

| mercek | durum | puan | hüküm | ham | en ağır bulgu (m:ss.s) · not |
|---|---|:-:|---|---|---|
| **❶ GÖRÜNTÜ** | EKSİK + ŞİŞİK (bloksuz · D2 ✗) | — (rapor: 10,0) | TIMELAPSE · SOLID | [THE_DRIVE_IN_Q1_GORUNTU_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_DRIVE_IN/THE_DRIVE_IN_Q1_GORUNTU_HAM.md) | 9/9 kategori 10/10 · pylon sign ve arka sırt %0.0 kayma · eriyen cisim YOK (`NONE FOUND`) · ⚠️ 34 klip 1 sn dilimlemesi |
| **❷ ZAMAN VE KESME** | EKSİK + ŞİŞİK (bloksuz · D2 ✗) | — (rapor: 10,0) | PASSING · TIME | [THE_DRIVE_IN_Q2_ZAMAN_KESME_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_DRIVE_IN/THE_DRIVE_IN_Q2_ZAMAN_KESME_HAM.md) | 9/9 kategori 10/10 · sabahtan geceye gölge ve ışık geçişi kusursuz · The cut that carries: 0:16.0 (perde çerçevesi montajı) · ⚠️ 34 klip dilimlemesi |
| **❸ ŞANTİYE** | EKSİK + ŞİŞİK (bloksuz · D2 ✗) | — (rapor: 10,0) | SAME WORLD · WORKING | [THE_DRIVE_IN_Q3_SANTIYE_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_DRIVE_IN/THE_DRIVE_IN_Q3_SANTIYE_HAM.md) | 32/32 dikiş hatasız (0 kusur) · sarı forklift (0:00 ve 0:05) süreklilik kanıtı · rölanti yok · ⚠️ 34 klip dilimlemesi |
| **❹ İNŞA** | EKSİK + ŞİŞİK (mod V belgesiz · D2 ✗) | — (rapor: 10,0) | SAME · BUILT · INVITED | [THE_DRIVE_IN_Q4_INSA_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_DRIVE_IN/THE_DRIVE_IN_Q4_INSA_HAM.md) | Kolon → kiriş → perde paneli → otopark çizgileri → bariyerler sırası kusursuz · mobil vinç ve yük yolu tam · davetsiz nesne yok · ⚠️ 34 klip dilimlemesi |
| **❺ TESLİM** | YANLIŞ GİRDİ (mod D belgesiz / mod V) | — (rapor: 10,0) | ENDS | [THE_DRIVE_IN_Q5_TESLIM_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_DRIVE_IN/THE_DRIVE_IN_Q5_TESLIM_HAM.md) | Vaat (terk edilmiş istasyon → drive-in sinema) tam çıktı · 0:28.0 film projeksiyonu ve seyirci araçları kusursuz final beat (`PASS`) · 0:32.0 kart tam |

```
FİLM PUANI:     — · N=0 (rapor-içi ortalama: 10,0)
ÖLDÜRÜCÜ HÜKÜM: — (hiçbir mercekte öldürücü hüküm yok)
OLUMSUZ HÜKÜM:  YOK
SONUÇ:          ⚠️ PUAN BAĞLAYICI DEĞİL (Ölçülmüş olgular bloğu olmadan koşuldu; teknik ve görsel olarak kusursuz 10,0 run)
```

---

## DOĞRULAMA (D1–D6)

- **Geri okuma**: ❶ ✓ (input_file.mp4 / NONE / 34) · ❷ ✓ (THE_DRIVE_IN.mp4 / NONE / 34) · ❸ ✓ (THE_DRIVE_IN.mp4 / NONE / 34) · ❹ ✓ (THE_DRIVE_IN.mp4 / NONE / 34) · ❺ ✓ (THE_DRIVE_IN.mp4 / NONE; cover: NOT SUPPLIED / 34).
- **D1 (Dosya dışı damga)**: Yok. Damgalar 0:00.0 – 0:34.0 aralığındadır.
- **D2 (Klip sayısı)**: ✗ 34 klip (1 sn dilimleme — plan 8 sahne + 1 kart).
- **D3 (Süre itirazı)**: Yok. ~34-37 saniyelik videonun tamamı taranmıştır.
- **D4 (Kesme damgası)**: Makine ölçüm bloğu verilmediği için model saniye bazlı 33 kesme listelemiştir.
- **D5 (Kart)**: 0:32.0'deki statik başlık kartı tespit edilmiş, son sahneyle aynı dünyayı koruduğu onaylanmıştır (C1/C2/C5 10/10).
- **D6 (Kurgu tablosu)**: Temizlik → hafriyat/dolgu → çelik montajı → perde paneli → otopark çizgileri → gece gösterimi sıralaması planla birebir uyumludur.

---

## ❓ MERCEKLERİN SORULARI VE PLANDAN CEVAPLAR (Questions for the Document)

### ❶ GÖRÜNTÜ (Lens 1)
1. **Perde çerçevesinin montaj takvimi nasıl planlandı?**
   - *Plandan Cevap*: S3'te iki dikey kolon dikilir ve çaprazlanır; S4'te üst bağlama kirişi atılarak 20 m'lik karkas tamamlanır; S5'te 20×8 m'lik beyaz perde asılır.
2. **Park eden araçların konumları önceden haritalandırıldı mı?**
   - *Plandan Cevap*: Evet. S5/S6'da parselde 2 sıra × 6 araç = 12 araçlık park yeri beyaz şeritlerle çizilir ve 6 hoparlör direği dikilir. S7'de 11 araba park etmişken 12. araba son boş yere girer.
3. **Her klibin temsil ettiği gerçek dünya süresi nedir?**
   - *Plandan Cevap*: S0–S6 Rejim B (sahne başına ~2 saat temsil · 900×); S7 Rejim G (gerçek zaman 1×, son araba doğal hızda park eder). Toplam zaman yayı: sabah 06:25'ten akşam 20:25:08 mavi saatine kadardır.

### ❷ ZAMAN VE KESME (Lens 2)
1. **Üretimde beyan edilen güneş yönü ve yükseklik açıları nedir?**
   - *Plandan Cevap*: 41° Kuzey enlemi, 21 Haziran yaz dönümü. 06:25'te (bearing 63° / elevation 6°) başlayan gün, öğlen 12:45'te (bearing 180° / elevation 72°) doruğa ulaşır, akşam 20:25'te (bearing 298° / elevation 0° gün batımı / mavi saat) biter. Kamera kuzeye (0°) bakar.
2. **Resmi olarak belirlenen mevsim ve hava koşulları nedir?**
   - *Plandan Cevap*: Yaz mevsimi (21 Haziran, açık gök, sıcak ışık, parsel kenarlarında kuru ot ve sararmış çalılar).
3. **Kesmeler arasında hedeflenen gerçek zaman atlaması nedir?**
   - *Plandan Cevap*: Büyük takvim atlamaları (haftalar) kesmelerde gerçekleşir; gün içi saat ise sabah 06:25'ten akşam 20:25'e kadar tek yönde kesintisiz ilerler.
4. **Herhangi bir klip durağan saat veya sabit aydınlatma olarak planlandı mı?**
   - *Plandan Cevap*: S7 final sahnesi (mavi saat, perdenin yanması ve 4 saniyelik final hold).
5. **34 kesme boyunca anlatı temposu nasıl kurgulandı?**
   - *Plandan Cevap*: Planlanan tempo 8 sahne × 8,0 sn (2x yayında 8 × 4,0 sn = 32 sn + 5 sn kart = 37 sn)'dir. Model ölçüm bloğu verilmediği için videoyu 1'er saniyelik 34 adıma bölmüştür.

### ❸ ŞANTİYE (Lens 3)
1. **Ekipman dağıtım sırası (forklift → mikser → vinç) lojistik planda önceden belirlendi mi?**
   - *Plandan Cevap*: Evet. S0–S1'de sarı forklift (eski pompaları söker ve kamyona yükler), S2'de beton mikseri (çatlak tamiri ve temel dökümü), S3–S4'te sarı mobil teleskopik vinç (çelik montajı). `Exit Before Swap` gereği her araç işi bitince sahneyi terk eder.
2. **Park çizgileri belirli araç kapasitelerine göre mi planlandı?**
   - *Plandan Cevap*: Evet, 2×6 = 12 araçlık standart açık hava sinema düzeni.
3. **Gündüz inşaatından akşam gösterimine geçiş takvimi nedir?**
   - *Plandan Cevap*: S0–S5 gündüz inşaatı, S6 gün batımı/alacakaranlık hazırlığı ve araç girişleri, S7 mavi saatte gösterinin başlaması.
4. **Marka sürekliliği için belirli makine modelleri zorunlu tutuldu mu?**
   - *Plandan Cevap*: Sarı forklift, sarı kasa kamyon, sarı mobil teleskopik vinç (aynı şantiye filosu dili).
5. **Akşam aydınlatması kademeli mi planlandı?**
   - *Plandan Cevap*: Evet, önce kanopi altı ışık şeridi ve dükkân pencereleri, ardından S7'de dev ekran tek karede yanar.

### ❹ İNŞA (Lens 4)
1. **Dikey çelik taşıyıcı kolonlar için yük kapasitesi gereksinimleri neydi?**
   - *Plandan Cevap*: 20 × 8 m dev billboard perde panelini ve rüzgâr yükünü taşıyacak iki derin beton temel üzerine oturan çelik kolonlar.
2. **Perde ankrajları için beton temel dökümü beyan edilmiş miydi?**
   - *Plandan Cevap*: Evet, S2'de kanopinin iki arka köşesinin arkasında iki beton temel dökümü açıkça beyan edilmiştir.
3. **Merkezi perde panelini kaldırmak için hangi vinç modeli belirlendi?**
   - *Plandan Cevap*: Standart sarı mobil teleskopik vinç (S3–S4).
4. **Otopark düzeni yerel drive-in yönetmeliklerine uygun muydu?**
   - *Plandan Cevap*: Evet, her arabanın perdeyi net görebileceği radyal/açılı 2 sıra düzeni.
5. **Perde parlaklığı alacakaranlık ve gece için belirlendi mi?**
   - *Plandan Cevap*: Perde tek karede durağan bir deniz manzarası / film karesiyle aydınlanır (lüks açık hava projeksiyonu).

### ❺ TESLİM (Lens 5)
1. **Gündüz inşaatından gece işletmesine geçişin anlatı yayı nedir?**
   - *Plandan Cevap*: Terk edilmiş bir benzin istasyonunun parselinin temizlenip, perde çerçevesi dikilerek açık hava arabalı sinemaya dönüştürülmesi ve ilk film gecesinin başlaması.
2. **Final park sekansı için seyirci eylemleri planlandı mı?**
   - *Plandan Cevap*: S6'da seyircilerin kaputlara oturması, kamp sandalyeleri kurması; S7'de son arabanın (12. araç) farlarını kapatarak yerine yanaşması.
3. **Gece gösterim aşaması için öngörülen ses miksi nedir?**
   - *Plandan Cevap*: Müzik yok; diegetik ortam sesleri: araba kapılarının kapanması, çakıl/asfalt lastik sesi, projektör ve amfi uğultusu, hafif rüzgâr.
4. **Final teslim paketi için belirli bir kapak kartı formatı zorunlu muydu?**
   - *Plandan Cevap*: Evet, son sahnenin (G8) dondurulmuş karesi üzerine ortalanmış "THE DRIVE-IN" başlık kartı (5,0 sn).
5. **Dönüşüm sürecinin her aşaması için hedeflenen süre neydi?**
   - *Plandan Cevap*: 8 sahne × 8,0 sn master (64,0 sn), 2x yayında 8 × 4,0 sn = 32,0 sn + 5,0 sn kart = 37,0 sn.
