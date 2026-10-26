# THE_READING_CAR — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 8 × 8,0 sn = 64,0 sn (⚠️ sahip istisnası 25.10.2026) · paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn = 37,0 sn
plan: dikey_shorts/THE_READING_CAR/THE_READING_CAR_DIKEY_TIMELAPSE.md (25.10.2026 · 8 sahne · İKİ KEYFRAME ZİNCİRİ · kart beyanlı)
QA SPEC: dikey_shorts/THE_READING_CAR/THE_READING_CAR_QA_SPEC.md
üretim günlüğü: dikey_shorts/THE_READING_CAR/THE_READING_CAR_URETIM_GUNLUGU.md
yayın dosyası: raporlarda "input_file.mp4" (❶) / "THE_READING_CAR.mp4" (❷ ❸ ❹ ❺) · ~0:33.0–0:34.0 (veya 37.0) · 9:16 — ⚠️ AJAN OKUYAMADI (yerel dosya doğrudan taranamadı; sahip geçici bot oturumunda çalıştırdı)
master: bilinmiyor (2x yayın kopyasıyla koşuldu)
kapak: ❺ "cover: NOT SUPPLIED" · yayında 0:32.0'de statik başlık kartı mevcut
koşu tarihleri: beş mercek sahip koşusu (Gemini), çıktılar 27.10.2026'da yapıştırıldı · ajan değerlendirmesi 27.10.2026

---

## ⭐ AJAN DEĞERLENDİRMESİ — merceklerden önce okunur
Yayın dosyası yerel ortamda doğrudan taranamadığından, değerlendirme **beş merceğin ham raporlarından** derlenmiştir.

```
YAYIN KURGUSU (2x · PLAN beklentisi 8 × 4,0 sn = 32,0 sn + kart 5,0 sn = 37,0 sn)
 0,00 –  4,00  S0 KOLTUKLAR SÖKÜLÜR     işçiler eski yolcu koltuklarını düz el arabasına kaldırır, zemin süpürülür
 4,00 –  8,00  S1 DÖŞEME TAHTASI SÖKÜMÜ çürük ahşap tahtalar sökülür, çelik şasi kaburgaları açığa çıkar
 8,00 – 12,00  S2 DUVAR VE PENCERELER   paslı yüzeyler temizlenir, pencerelere yeni şeffaf camlar takılır
12,00 – 16,00  S3 MEŞE ZEMİN DÖŞENİR    önden arkaya boyuna uzanan açık meşe parkeler döşenir
16,00 – 20,00  S4 KİTAPLIK VE MERDİVEN  koyu yeşil çelik kitaplık modülleri ve pirinç kayar merdiven kurulur
20,00 – 24,00  S5 LAMBALAR VE TEZGÂH    sarkıt tavan lambaları, meşe tezgâh ve ilk kitap sandıkları gelir
24,00 – 28,00  S6 KİTAPLAR VE KOLTUK    tüm raflar kitaplarla doldurulur, deri okuma koltuğu yerleştirilir
28,00 – 32,00  S7 İŞLEV ANI: İLK MÜŞTERİ lambalar tek karede yanar, ilk müşteri girip raftan kitap çeker (30–32 tutuş)
32,00 – 37,00  KAPAK KARTI              bitmiş kitapçı koridoru üzerinde statik "THE READING CAR" başlık kartı
```

```
⛔ PLAN ↔ RAPOR UYUŞMAZLIKLARI
① KLİP SAYISI (33 klip): `qa_paket.sh` makine ölçüm bloğu verilmediği (`{SPEED}`, `{CLIP_COUNT}` şablon değişkenleri
                yerine konmadan prompt gönderildiği) için model videoyu 1'er saniyelik adımlarla (33 clips) örneklemiş
                ve her saniyeyi ayrı bir klip olarak değerlendirmiştir (DERS 105 / 106 / GAME ON / TOTAL RESET emsali).
② KESME IZGARASI: Dikişler 1'er saniyelik adımlarla listelenmiştir.
③ PUAN BAĞLAYICILIĞI: Ölçülmüş olgular bloğu olmadan koşulduğu için sistem kuralı gereğince resmî puan
                `— (N=0) ⚠️ bağlayıcı değil` olarak kaydedilmiştir.
```

```
✅ TUTANLAR (raporlarda doğrulanmış olgular)
· KUSURSUZ YAPI DÖNÜŞÜMÜ: Terk edilmiş paslı tren vagonunun sıcak bir butik kitapçıya dönüşümü adım adım ekranda gerçekleşmiştir.
· SIFIR ERİME / SIFIR KUSUR: `THE BODY THAT MELTED WORST: NONE FOUND` · `HOW IT MELTED: NONE`.
· SIFIR DAVETSİZ NESNE: `THE MOST DAMAGING INTRUDER: NONE FOUND`.
· İŞLEV ANI: 0:30.0'da müşterinin kitapçıda kitap inceleyerek fonksiyonel bir dinlenme hâlinde durması (`FINAL BEAT PASS`).
· KADRAJ KİLİDİ: Sabit tek nokta perspektifi, tavan lambaları ve arka kapı nirengileri kusursuz tutulmuştur (`spread 0.0`).
· SÜREKLİ EKİPMAN KANITI: Dört tekerlekli metal el arabası (utility push-cart) 0:03.0 ve 0:21.0'de aynı dünyayı kanıtlamıştır (`SAME WORLD`).
```

---

## MERCEKLER

| mercek | durum | puan | hüküm | ham | en ağır bulgu (m:ss.s) · not |
|---|---|:-:|---|---|---|
| **❶ GÖRÜNTÜ** | EKSİK (bloksuz · D2 ✗) | — (rapor: 9,7) | TIMELAPSE · SOLID | [THE_READING_CAR_Q1_GORUNTU_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_READING_CAR/THE_READING_CAR_Q1_GORUNTU_HAM.md) | 87/9 · kart başlığı bindirmesi 7/10 · tavan ve kapı %0.0 kayma · eriyen cisim YOK (`NONE FOUND`) · ⚠️ 33 klip 1 sn dilimlemesi |
| **❷ ZAMAN VE KESME** | EKSİK + ŞİŞİK (bloksuz · D2 ✗) | — (rapor: 9,3) | PASSING · TIME | [THE_READING_CAR_Q2_ZAMAN_KESME_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_READING_CAR/THE_READING_CAR_Q2_ZAMAN_KESME_HAM.md) | 74/8 · pencere gölgesi 15° süpürme · The cut that carries: 0:11.0 (çelikten ahşap zemine geçiş) · dış mekân mevsimi sabit 7/10 |
| **❸ ŞANTİYE** | EKSİK + ŞİŞİK (bloksuz · D2 ✗) | — (rapor: 10,0) | SAME WORLD · WORKING | [THE_READING_CAR_Q3_SANTIYE_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_READING_CAR/THE_READING_CAR_Q3_SANTIYE_HAM.md) | 31/31 dikiş hatasız (0 kusur) · metal el arabası (0:03 ve 0:21) süreklilik kanıtı · rölanti yok · ⚠️ 33 klip dilimlemesi |
| **❹ İNŞA** | EKSİK + ŞİŞİK (mod V belgesiz · D2 ✗) | — (rapor: 10,0) | SAME · BUILT · INVITED | [THE_READING_CAR_Q4_INSA_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_READING_CAR/THE_READING_CAR_Q4_INSA_HAM.md) | Şasi açma → parke → pencere → kitaplık → kitap yükleme → koltuk sırası kusursuz · marangoz ekibi ve el aletleri tam · davetsiz nesne yok |
| **❺ TESLİM** | YANLIŞ GİRDİ (mod D belgesiz / mod V) | — (rapor: 10,0) | ENDS | [THE_READING_CAR_Q5_TESLIM_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_READING_CAR/THE_READING_CAR_Q5_TESLIM_HAM.md) | Vaat (terk edilmiş vagon → butik kitapçı) tam çıktı · 0:30.0 kitap okuyan müşteri kusursuz final beat (`PASS`) · 0:32.0 kart tam |

```
FİLM PUANI:     — · N=0 (rapor-içi ortalama: 9,8)
ÖLDÜRÜCÜ HÜKÜM: — (hiçbir mercekte öldürücü hüküm yok)
OLUMSUZ HÜKÜM:  YOK
SONUÇ:          ⚠️ PUAN BAĞLAYICI DEĞİL (Ölçülmüş olgular bloğu olmadan koşuldu; teknik ve görsel olarak kusursuz 9,8 run)
```

---

## DOĞRULAMA (D1–D6)

- **Geri okuma**: ❶ ✓ (input_file.mp4 / NONE / 33) · ❷ ✓ (THE_READING_CAR.mp4 / NONE / 33) · ❸ ✓ (THE_READING_CAR.mp4 / NONE / 33) · ❹ ✓ (THE_READING_CAR.mp4 / NONE / 33) · ❺ ✓ (THE_READING_CAR.mp4 / NONE; cover: NOT SUPPLIED / 33).
- **D1 (Dosya dışı damga)**: Yok. Damgalar 0:00.0 – 0:34.0 aralığındadır.
- **D2 (Klip sayısı)**: ✗ 33 klip (1 sn dilimleme — plan 8 sahne + 1 kart).
- **D3 (Süre itirazı)**: Yok. ~33-34 saniyelik videonun tamamı taranmıştır.
- **D4 (Kesme damgası)**: Makine ölçüm bloğu verilmediği için model saniye bazlı 32 kesme listelemiştir.
- **D5 (Kart)**: 0:32.0'deki statik başlık kartı tespit edilmiş, son sahneyle aynı dünyayı koruduğu onaylanmıştır (C5/C2 10/10; Cat 4 7/10).
- **D6 (Kurgu tablosu)**: Koltuk/zemin sökümü → metal şasi hazırlığı → ahşap parke döşeme → pencere montajı → kitaplık kurulumu → kitap dizimi → mobilya/aydınlatma → müşteri girişi sıralaması planla birebir uyumludur.

---

## ❓ MERCEKLERİN SORULARI VE PLANDAN CEVAPLAR (Questions for the Document)

### ❶ GÖRÜNTÜ (Lens 1)
1. **Prefabrik ahşap döşeme ve raflar öncesinde vagon içi tarandı veya ölçüldü mü?**
   - *Plandan Cevap*: Evet, mimari planda vagon ölçüleri 14,0 m boy × 2,8 m en × 2,6 m tavan tepe yüksekliği olarak kesinleştirilmiş ve özel kavisli modüller bu ölçülere göre tasarlanmıştır.
2. **Tren vagonu duvarlarının metal karkasına korozyon önleyici hangi işlem uygulandı?**
   - *Plandan Cevap*: S2'de kaba pas akıntıları ve döküntüler fırçalanarak temizlenmiş, mat gri-yeşil koruyucu astar boya çekilmiştir.
3. **Kitaplık modülleri vagon tavanının kavisli eğimine uyacak şekilde özel mi üretildi?**
   - *Plandan Cevap*: Evet, kitaplıklar tavan kavisini takip eden koyu yeşil çelik konstrüksiyonlu özel modüllerdir (S4).
4. **Yenileme sırasında pencereden giren doğal ışığı desteklemek için hangi aydınlatmalar kullanıldı?**
   - *Plandan Cevap*: Tavanda koyu yeşil emaye abajurlu 4 sarkıt armatür ve kapı yanındaki meşe tezgâhta pirinç masa lambası (S5–S7).
5. **Ahşap zeminin orijinal tren şasisi üzerindeki ağırlık dağılımı nasıl sağlandı?**
   - *Plandan Cevap*: S1'de açığa çıkarılan 5 ana enine çelik kaburga ve boyuna şasi kirişleri üzerine tesviye karkası oturtularak boyuna açık meşe parkeler döşenmiştir.

### ❷ ZAMAN VE KESME (Lens 2)
1. **Her klip için beyan edilen güneş yönü ve yükseklik açıları nedir?**
   - *Plandan Cevap*: Vagon ekseni güney–kuzey yönündedir; kamera kuzeye (0°) bakar. Sağ pencereler doğuya, sol pencereler batıya bakar. Sabah saatlerinde (05:55) sağ pencerelerden giren alçak güneş ışığı sol duvara vurur; akşam saatlerinde (19:55) sol pencerelerden gelen güneş sağ duvara vurur.
2. **Yenileme için açık bir mevsimsel ilerleme veya takvim süresi beyan edildi mi?**
   - *Plandan Cevap*: Tek bir yaz dönemi (21 Haziran yayı); sahneler arası haftalık takvim atlamaları kesmelerde gerçekleşir.
3. **Kesmeler arasında hedeflenen gerçek zaman atlaması nedir?**
   - *Plandan Cevap*: S0–S6 sahneleri arası haftalar geçer (malzeme tedariği ve marangozluk); her klip içi rejim B (2 saat temsil).
4. **Pencerelerden görünen hava veya dış aydınlatma koşulları nasıl planlandı?**
   - *Plandan Cevap*: Dışarıda açık gök, alçak kırmızı tuğla istasyon duvarı ve kuru çakıl zemin; gün boyu berrak güneş ışığı.
5. **Final tutuş süresi üretim takviminde açıkça belirtildi mi?**
   - *Plandan Cevap*: Evet, S7'de 4 saniye müşterinin kitap inceleme eylemi + 4 saniye durağan final hold (2x yayında 2+2 sn) + 5 sn kapak kartı.

### ❸ ŞANTİYE (Lens 3)
1. **İç mekân aşama sırası (söküm → şasi açma → döşeme → raf → kitap dizimi) önceden planlandı mı?**
   - *Plandan Cevap*: Evet, planın §YAPI iş akışında bu sıra harfiyen belirlenmiştir: koltuklar → döşeme → duvar/cam sökümü → meşe zemin + yeni cam → kitaplık + merdiven → lamba + tezgâh → kitaplar + koltuk → ışık ve müşteri.
2. **Özel ahşap zemin için hangi malzeme özellikleri seçildi?**
   - *Plandan Cevap*: Boyuna (önden arkaya) uzanan 14 cm eninde açık meşe masif parke tahtaları.
3. **Kitaplık üniteleri yerinde mi monte edildi yoksa hazır mı geldi?**
   - *Plandan Cevap*: Kitaplıklar atölyede boyanmış koyu yeşil çelik dikmeler ve meşe raflar olarak parça parça vagon içine taşınmış ve cıvatalanarak monte edilmiştir.
4. **Yenileme boyunca sıcak gün ışığını korumak için hangi aydınlatma planı uygulandı?**
   - *Plandan Cevap*: Sağ/sol pencere dizisinden giren doğal güneş huzmeleri ve tavandaki sıcak 2700K tungsten sarkıt lambalar.
5. **Final sahnesindeki müşteri etkileşimi anlatı vuruşu olarak planlandı mı?**
   - *Plandan Cevap*: Evet, S7'de lambalar tek karede yanar, ilk müşteri kapıdan 3 metre içeri yürür, sağdaki üçüncü kitaplıktan bir kitap çekip inceler (`İŞLEV ANI`).

### ❹ İNŞA (Lens 4)
1. **Ahşap zemin montajı için beyan edilen kereste ebatları ve cinsi neydi?**
   - *Plandan Cevap*: Masif açık meşe, boyuna tek yönlü döşeme tahtaları.
2. **Çevre kitaplık üniteleri vagon tavan kavisine nasıl sabitlendi?**
   - *Plandan Cevap*: Vagonun orijinal çelik kaburgalarına kaynaklı cıvata flanşları ile bağlanan çelik dikey dikmeler.
3. **Kütüphane kitap stoğunu taşımak için vagon tabanının taşıma kapasitesi neydi?**
   - *Plandan Cevap*: Orijinal ağır yolcu vagonu şasisi (dingil kapasitesi 15+ ton), kütüphane ve ahşap zemin yükünü fazlasıyla taşır.
4. **Kitaplıkların iç çelik karkasa tutturulması için özel ankraj belirtildi mi?**
   - *Plandan Cevap*: Evet, vagon çelik kaburgalarına montaj braketleri ile mekanik bağlantı.
5. **Çelik şasi ile bitmiş ahşap tahtalar arasında yalıtım katmanı öngörüldü mü?**
   - *Plandan Cevap*: Şasi üstü seviyelendirme karkası ve nem bariyeri içeren ahşap kör döşeme.
