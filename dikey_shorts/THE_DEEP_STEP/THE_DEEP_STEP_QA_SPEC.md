# 🔬 THE DEEP STEP — QA ŞARTNAMESİ

```
KAPSAM     7 sahne × 8,0 sn = 56,0 sn · 8 görsel (G0..G7) + 7 I2V · tek istasyon (HOME)
AMAÇ       Bu dosya "güzel mi" diye sormaz. Tek soru: ⭐ YERALTI BASAMAKLI KUYUSU, 28 KADEMEYİ
           TEK TEK İNEREK −21,60 METRE DERİNLİKTEKİ AKİFER SUYUNA DİKİŞSİZ ULAŞTI MI?
DURUM      ⛔ ÜRETİLMEDİ — bu şartname ÖLÇÜM BEKLİYOR. Aşağıdaki tüm değerler plandan türetilmiş HEDEFTİR.
TARİH      30.09.2026
```

---

## 1. ⛔ FİNAL KARE KANITI — 56,0 sn (G7 Usta Kare) [AGENTS.md]

Teslim videosunun son karesi (56,0 sn) dondurulur ve **dört kanıt sırayla** aranır:

```
① 28 BASAMAK KATMANI VE 1.400 KUMTAŞI BASAMAK TAM VE KESKİN
   · 36,00 × 24,00 m kuyu ağzından başlayarak içe doğru daralan V-şekilli basamak labirenti.
   · Her basamak keskin 90° açılı sarı kumtaşı kenarı taşır; erimiş, akmış veya yamulmuş basamak YOKTUR.
   · Doğu, batı ve güney duvarlarındaki basamak dizilimi kusursuz simetrik geometridir.
   ⛔ Herhangi bir basamakta "erime / morfing / merdiven basamağının rampaya dönüşmesi" varsa: G7 RED.

② KUZEY DUVARI ÜÇ KATLI OYMA PAVYONLARI EKSİKSİZ
   · Üç katlı sütunlu taş galeri ayakta ve sağlamdır.
   · En üst katta flütlü taş kubbeli chhatri pavyonları, orta katta oyma jali kafes panelleri.
   · Kolonlar, başlıklar ve konsol kornişler net taş oyma detaylarıyla seçilir.
   ⛔ Sütunların kayması, kemerlerin erimesi veya pavyonun deforme olması: G7 RED.

③ AKİFER SU AYNASI VE 8 YANAN TAŞ KANDİL
   · Kuyu tabanında −19,80 m kotunda (1,80 m su derinliği) 342 × 186 piksellik dingin zümrüt yeşili su aynası.
   · Su yüzeyinde kuzey pavyonunun kusursuz ters yansıması görünür.
   · Pavyon nişlerinde ve havuz köşelerinde 8 adet yontma taş kandil (diya) altın sarısı alevle yanar.
   · Alevlerin yansıması su aynasında 8 parlak sarı nokta olarak parıldar.
   ⛔ Su tabanı kuruysa veya yeşil plastik render rengindeyse: G7 RED.

④ SAHA TAMAMEN TEMİZLENMİŞ VE SÖKÜM KANITLANMIŞ
   · S1–S5 boyunca kullanılan tüm ahşap iksa dikmeleri, iskele kalasları, halatlar ve el arabaları
     KADRAJIDAN TAMAMEN ÇIKARILMIŞTIR.
   · Üst parapet ve kuyu çevresindeki çöl toprağı temizce süpürülmüş; hafriyat yığını kalmamıştır.
   · S0'daki cılız akasya ağacı tamamen yok olmuştur (Bedel ödenmiştir).
   ⛔ Kadrajda unutulmuş kalas, iskele dikmesi veya modern alet varsa: G7 RED.
```

---

## 2. 📏 KADRAJ KİLİTLERİ (Piksel Defteri — G0..G7)

Kamera sabit sehpadadır (`h = +1,60 m`, tilt −42,0° aşağı, 24 mm f/8).
Aşağıdaki nirengi noktaları **8 görselin tamamında** ölçülür:

| Referans Çapası | Konum / Koordinat | Beklenen Boyut | Tolerans | Denetlenen Kareler |
|---|---|---|:---:|:---:|
| Kuzey Sınır Parapeti (Üst Hat) | `y% 94,0 – 98,0` | En 1080 px (tam en) | ± 1 px | G0 … G7 |
| Kuzeybatı Taş Sınır Taşı | `x% 8,0 – 14,0` · `y% 92,0 – 98,0` | 64 × 48 px | ± 1 px | G0 … G7 |
| Kuzeydoğu Taş Sınır Taşı | `x% 86,0 – 92,0` · `y% 92,0 – 98,0` | 64 × 48 px | ± 1 px | G0 … G7 |
| Kuyu Ağzı Dış Çerçevesi (36×24 m) | `x% 12,0 – 88,0` · `y% 8,0 – 94,0` | 820 × 1650 px | ± 2 px | G0 … G7 |
| Optik Eksen Zemin İzdüşümü | Tam Merkez (`x% 50,0` · `y% 50,0`) | Orta Teras Kotu | ± 1 px | G0 … G7 |
| Taban Havuzu Aynası | `x% 34,2 – 65,8` · `y% 18,5 – 36,5` | 342 × 186 px | ± 2 px | G5 … G7 |

---

## 3. 🔍 SEKİZ MERCEK DEĞERLENDİRME KRİTERLERİ

```
① KARE MERCEĞİ (Sabitlik & Kadraj)
   · Kamera sabit sehpadadır; sıfır pan, sıfır tilt, sıfır roll, sıfır zoom.
   · Kuzey sınır parapeti sekiz karede de aynı piksel satırında durur (tolerans ±1 px).
   · Kadrajda ufuk ve gökyüzü görünmez (ZEMİN ailesi tam kilit).

② İNŞA MERCEĞİ (Geometri & Yapım Sırası)
   · Basamaklar havadan belirmez (APPEARED yasaktır); her basamak altındaki kazılmış şeve ve
     harç yatağına oturarak aşağı doğru iner.
   · 0 → 4 → 8 → 14 → 20 → 26 → 28 basamak katmanı sırası hiçbir karede atlamaz.
   · Kuzey pavyonu kolonları zemin temeline basar; konsollar kademe kademe taşınır.

③ ZAMAN MERCEĞİ (Güneş Saati & Gölge İbresi)
   · Azimut 105°'den (sabah) 285°'ye (akşam) döner.
   · Kuyu içine vuran üçgen gölge bıçakları günün saatine tam uyar.
   · Öğlen (S2-S3) gölge tabana iner; akşamüstü (S5-S6) kuyu tabanı loşlaşır, üst galeriler parlar.

④ TESLİM MERCEĞİ (Vaat / Direnç / Bedel)
   · S0'daki cılız akasya ve kuru toprak yok olmuş; yerini 21,6 m derindeki akifer suyu almıştır.
   · Su aynasında gökyüzü ve pavyon yansıması kusursuzdur.
   · Video içi başlık kartı yoktur; teslim saf mimariyle kapanır.

⑤ DEVAMLILIK MERCEĞİ (İki Keyframe Dikişi)
   · Her I2V klibinin ilk karesi G(n), son karesi G(n+1) ile piksel piksel aynıdır.
   · Sahneler arasında taş dokuları, renk tonu veya kuyu geometrisi sıçramaz.

⑥ GEÇİŞ MERCEĞİ (Ritim & Kesme)
   · 7 × 8,0 sn düz ızgara beyanlıdır; ritmi klibin içindeki derinleşme ve iş hacmi taşır.
   · Kesmelerde optik eksen oynamaz; zaman ileriye doğru kesintisiz akar.

⑦ İŞ MERCEĞİ (Şantiye Hareketi)
   · Kuyu içinde en az iki hareket eden unsur (işçi, sepet, vinç caraskalı) her klipte işe bağlıdır.
   · S6'da tüm iskelelerin sökülmesi ve sahadan çıkarılması kanıtlanır.

⑧ YÖNTEM MERCEĞİ (Fizik & Ağırlık)
   · Taş bloklar taşınır, yontulur, yerine konur ve tokmaklanır.
   · Ağır parçalar halat ve makaralarla indirilir; yerçekimi yük yolu pavyon sütunlarına basar.
```

---

## 4. ⚠️ RİSK ANALİZİ VE ÖNLEM TABLOSU (10 RİSK)

| # | Risk Tanımı | Kritiklik | Olası Arıza / Mercek | Alınan Önlem & Prompt Kilidi |
|---|---|:---:|---|---|
| 1 | Tekrarlayan basamaklarda AI erimesi | YÜKSEK | ② İNŞA (morphing) | Her basamak "hand-dressed yellow sandstone with crisp 90-degree beveled edges" olarak kilitlendi. |
| 2 | Ufuksuz kadrajda kamera kaçıklığı | YÜKSEK | ① KARE (drift) | Kuzey taş parapeti 1080 px genişliğinde yatay cetvel olarak sabitlendi (±1 px tolerans). |
| 3 | Ahşap iksaların aniden yok olması | ORTA | ⑧ YÖNTEM (appeared/disappeared) | S5'te iksalar gevşetilir; S6'da halatlarla yukarı çekilerek söküldüğü sahnede açıkça gösterilir. |
| 4 | Su aynasının yapay görünmesi | YÜKSEK | ④ TESLİM (render look) | "Still emerald-green water mirror, 1.80m depth, reflecting carved pavilion facade and lamp flames" ile fiziksel su tanımlandı. |
| 5 | Düz ızgarada metronom etkisi | ORTA | ⑥ GEÇİŞ (metronome) | Sahip kararı beyan edildi; her sahnenin derinleşme kotu ve eylemi farklılaştırılarak ritim içe aktarıldı. |
| 6 | İnsan figürlerinin donuk/bulanık çıkması | ORTA | ① KARE / ⑦ İŞ (people) | "Crew appear only as soft motion streaks, none facing camera, no readable face" kuralı konuldu. |
| 7 | Akasya ağacının geri belirmesi | ORTA | ⑤ DEVAMLILIK | S1'de kökünden söküldüğü ve yerinde yalnız çukur kaldığı açıkça belirtildi. |
| 8 | Taş pavyon sütunlarının yamulması | YÜKSEK | ② İNŞA (geometric stability) | Kuzey sütunları "monolithic sandstone shafts with lead-filled mortise joints" olarak yapı biblesine işlendi. |
| 9 | Güneş yönünün kuyu içinde karışması | ORTA | ③ ZAMAN (shadow direction) | Azimut 105° → 285° derece derece tablolaştırıldı; her I2V'ye gölge süpürme cümlesi yazıldı. |
| 10 | Kandil alevlerinin gündüz yanması | DÜŞÜK | ③ ZAMAN | 8 taş diya yalnız S6 (mavi saat) ve G7 usta karesinde yakıldı; gündüz sahnelerinde boş niş bırakıldı. |
