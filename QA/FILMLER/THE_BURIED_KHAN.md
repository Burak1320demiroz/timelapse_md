# THE_BURIED_KHAN — QA KAYDI

## KÜNYE
format: Yatay 16:9 · plan 15 × 8,0 sn = 120,0 sn · hız 1x (yatay hat 2x'e çevrilmez) · yayın 2:00.0 (19 kesme) + 5,0 sn kapak kartı = 2:05.0
plan: yatay_2_dk_filmler/THE_BURIED_KHAN/THE_BURIED_KHAN_PLAN.md (09.10.2026 · 15 sahne · düz ızgara beyanlı · kapı ⚠️ FIX)
üretim günlüğü: yatay_2_dk_filmler/THE_BURIED_KHAN/THE_BURIED_KHAN_URETIM_GUNLUGU.md
yayın dosyası: raporda `buried_khan.mp4` (❶ ❷) / `THE_BURIED_KHAN (1).mp4` (❸ ❹ ❺) · 2:05.0 (20 klip/kesme) · 16:9 yatay · tek istasyon (MAIN STATION)
master: tek master (120 sn · 1x)
kapak: ❺ "cover: NOT SUPPLIED" (kart 2:00.0'de videodan görüldü, "THE BURIED KHAN")
koşu tarihleri: 22.10.2026 · sahip koşusu (Gemini) · ajan inceleme ve kaydı 22.10.2026

---

## ⭐ AJAN ÖLÇÜMÜ VE MERCEK DEĞERLENDİRMESİ

Video modele 20 bölümlü (19 sahne geçişi + 1 statik kart), 2 dakikalık yatay 16:9 master olarak girmiştir. Beş merceğin beşi de kör/yarı-kör modda tam olarak koşulmuş ve tutarlı zaman damgalarıyla puanlanmıştır.

```
YAYIN KURGUSU (1x · 0:00.0 – 2:05.0 · 20 Klip / Kesme)
 0:00.0 – 0:17.0  Açılış & Hafriyat: Çöl ortasında devasa kum tepesi altındaki antik kervansaray portalının ekskavatör ve kamyonlarla açığa çıkarılması; ön avlu kumu tesviyesi (Klip 1–3)
 0:17.0 – 0:33.0  Portal Temizliği & Taş Kaplama: Giriş kemeri kumunun temizlenmesi, alt cephe duvarlarının ortaya çıkması, ön avluya taş döşeme yapılması (Klip 4–6)
 0:33.0 – 0:53.0  İskele & Üst Kat Karkas: Sağda mobil vincin kurulması, üst kat iskelelerinin dikilmesi, tonoz ve çatı parapetlerinin örülmesi (Klip 7–9)
 0:53.0 – 1:04.0  Ön Avlu Kemerleri (0:58.0 MELTING/APPEARING): Ön cephe boyunca bağımsız taş kemerlerin belirmesi (0:58.0 dijital fade-in kusuru) ve ana ahşap kapının montajı (Klip 10–11)
 1:04.0 – 1:28.0  Avlu Temizliği, Kum Fırtınası Direnci & Donatı: El arabalarıyla moloz temizliği; 1:13.0 çöl kum fırtınasına karşı çalışma direnci; fener montajı; traktör ikmali (Klip 12–15)
 1:28.0 – 1:45.0  Gün Batımı & Kamp Ateşi: Güneşin batışı, iskele ve vinç sökümü, avluda akşam ateşlerinin yakılması (Klip 16–17)
 1:45.0 – 2:00.0  FİNAL VURUŞU & GECE İŞLEVİ (FINAL BEAT PASS): Kemerlerde sıcak fener ışıkları, avluda dinlenen yolcular, kamp ateşleri ve develer; gece barınağının yaşaması (Klip 18–19)
 2:00.0 – 2:05.0  Final Tutuşu & Statik Kart: "THE BURIED KHAN" başlık kartı (Klip 20)
```

```
✅ TUTANLAR
· KAMERA KİLİDİ KUSURSUZ (❶ 10/10 · ❷ 10/10 · ❸ 10/10 · ❹ 10/10): Sol öndeki ölü akasya ağacı (kanıt nesnesi 105 px), arka sağdaki masa dağı ve kule kubbeleri 2 dakika boyunca sıfır piksel kaymayla kilitli kalmıştır.
· ZAMAN VE IŞIK EĞRİSİ (❷ 9,1 · ❸ C4 10/10): Sabah güneşinden öğle dikliğine, oradan akşam kızıllığına ve yıldızlı geceye geçiş, gölge oranları (1:1.5 -> 1:1.0 -> 1:2.2 -> 1:4.0) tam fiziksel tutarlılıkta gerçekleşmiştir.
· ŞANTİYE DİSİPLİNİ VE MAKİNE DÖNGÜLERİ (❸ 9,5 · 10/10): Ekskavatör, damperli kamyon, mobil vinç, traktör ve işçilerin hareket döngüleri mantıklı ve kesintisiz işlemiştir (working front no idle 10/10).
· ÇEVRE DİRENCİ (❺ 10/10): 1:13.0'te sahayı vuran çöl kum fırtınası ve işçilerin rüzgâra karşı direnci filme güçlü bir gerçeklik imtiyazı katmıştır.
· FİNAL BEAT VE DÖNGÜ (❺ 9,8 · PASS): G0'daki gömülü kumul ile G15'teki aydınlatılmış, ateşleri yanan, deve ve yolcuların dinlendiği kervansaray aynı kadrajda döngüyü tam bağlamıştır.
```

```
⚠️ PLAN ↔ MODEL SAPMALARI (ÖĞRENİLEN DERSLER)
① 0:58.0 TAŞ KEMERLERİN ERİMEYLE BELİRMESİ (MELTING / APPEARING) [DERS 61]:
   Ön avludaki taş kemer kolonadı 0:58.0'de vinçle taş blok blok ve ahşap kalıplarla örülmek yerine dijital fade-in / materialization ile bir anda ekranda belirmiştir.
   Bu durum ❶'de MELTING (Category 8: 3/10), ❹'te APPEARING (Category 4: 5/10) olarak cezalandırılmıştır.
② YASAK KELİME SIZINTISI ("camel") [DERS 59]:
   Planda `YASAK KELİME camel · camels` yazılmış ve kervan/deve anatomisinin sahneye girmesi yasaklanmıştı. Ancak ❺ merceği 1:45.0 gece sahnesinde avluda develerin
   (camels) dinlendiğini raporlamıştır. Video motoru yasak kelimeye rağmen geleneksel kervansaray çağrışımından ötürü deve üretmiştir.
③ KAPAK KARTI VE MÜZİK FARKI:
   Planda teslimde kart ve müzik bulunmuyordu; ancak yayın kurgusunda 2:00.0'de statik kart ve ritmik bir müzik yatağı yer almıştır. Mercekler bunu C1/C2 ve C5'te
   doğrulamış ve müzik vuruşlarının kesmelerle örtüştüğünü (on the beat) belirtmiştir.
```

---

## MERCEKLER

| mercek | durum | puan | hüküm | ham | en ağır bulgu (m:ss.s) · not |
|---|---|:-:|---|---|---|
| ❶ GÖRÜNTÜ | TAM | 8,3 | TIMELAPSE · MELTING | [THE_BURIED_KHAN_Q1_GORUNTU_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_BURIED_KHAN/THE_BURIED_KHAN_Q1_GORUNTU_HAM.md) | 0:58.0 taş kemerler parça parça inşa edilmek yerine fade-in ile belirdi (MELTING) |
| ❷ ZAMAN VE KESME | TAM | 9,1 | PASSING · TIME · RHYTHM | [THE_BURIED_KHAN_Q2_ZAMAN_KESME_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_BURIED_KHAN/THE_BURIED_KHAN_Q2_ZAMAN_KESME_HAM.md) | Çöl sabahından geceye doğal ışık ve gölge süpürmesi · 0:58.0 filmi taşıyan kesme (The Cut That Carries) |
| ❸ ŞANTİYE | TAM | 9,5 | SAME WORLD · WORKING | [THE_BURIED_KHAN_Q3_SANTIYE_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_BURIED_KHAN/THE_BURIED_KHAN_Q3_SANTIYE_HAM.md) | Akasya ağacı ve kuleler nirengi (10/10) · hafriyat ve vinç döngüleri tam · 0:58.0 dikiş kusuru |
| ❹ İNŞA | TAM (Mod V) | 8,8 | SAME · APPEARING · INVITED | [THE_BURIED_KHAN_Q4_INSA_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_BURIED_KHAN/THE_BURIED_KHAN_Q4_INSA_HAM.md) | Hafriyat, döşeme, üst kat tonozları ve kapı inşa edildi · 0:58.0 taş kemerler belirdi (APPEARING) |
| ❺ TESLİM | TAM (Mod V) | 9,8 | ENDS | [THE_BURIED_KHAN_Q5_TESLIM_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_BURIED_KHAN/THE_BURIED_KHAN_Q5_TESLIM_HAM.md) | Final Beat PASS (1:45.0) · gece dinlenme barınağı vaadi tam ekranda · 2:00.0 kart tam |

```
FİLM PUANI:  9,1  (N=5)        [ (8,3 + 9,1 + 9,5 + 8,8 + 9,8) / 5 ]
ÖLDÜRÜCÜ:    YOK  (❶ TIMELAPSE · ❸ SAME WORLD · ❹ SAME · ❺ ENDS)
OLUMSUZ:     MELTING (❶) · APPEARING (❹)  [0:58.0 kemerlerin dijital belirişi]
SONUÇ:       ✅ GEÇTİ (PASS)
```

---

## DOĞRULAMA (D1–D6)

- **Geri okuma**: ❶ ✓ (buried_khan.mp4 / NONE / 20) · ❷ ✓ (buried_khan.mp4 / NONE / 20) · ❸ ✓ (THE_BURIED_KHAN (1).mp4 / NONE / 20) · ❹ ✓ (THE_BURIED_KHAN (1).mp4 / NONE / 20) · ❺ ✓ (THE_BURIED_KHAN (1).mp4 / NONE; cover: NOT SUPPLIED / 20). Beş mercek de geri okumayı eksiksiz geçti.
- **D1 (Dosya dışı damga)**: Yok. Tüm zaman damgaları 0:00.0 – 2:05.0 aralığındadır.
- **D2 (Klip sayısı)**: 20 klip bildirilmiş. 19 kurgu kesmesi + 1 statik kart dilimi eksiksiz örtüşmektedir.
- **D3 (Süre itirazı)**: Yok. 120 saniyelik ana timelapse + 5 saniyelik kart (2:05.0) tam kapsanmıştır.
- **D4 (Kesme damgası)**: Kesme damgaları müzik vuruşlarına ve inşaat adımlarına denk düşmektedir.
- **D5 (Kart)**: 2:00.0'de "THE BURIED KHAN" başlık kartı görülmüş ve 10/10 ile puanlanmıştır.
- **D6 (Kurgu tablosu)**: Kareler ve inşaat ilerleyişi kronolojik olarak doğrulanmıştır.

---

## ❓ MERCEKLERİN SORULARI VE PLANDAN CEVAPLAR (Questions for the Document)

### ❶ GÖRÜNTÜ (Lens 1)
1. **0:58'deki taş kemerlerin parça parça inşa edilmesi mi yoksa görsel efekt fade-in ile üretilmesi mi hedeflenmişti?**
   - *Plandan Cevap*: Planda (S7–S8) taş kemerlerin gedikteki iskele, ahşap kalıplar (centering) ve mobil vinç sapanlarıyla tek tek taş bloklar kaldırılarak örülmesi şart koşulmuştur (`FIZIK_VE_AGIRLIK §2`, `INSAAT_YONTEMI §3`). Ekranda ara aşamalar atlanıp dijital fade-in yapılması modelin bir kusurudur (❶ MELTING / ❹ APPEARING).
2. **Görüş grubu A için tam kamera odak uzaklığı ve sensör istasyonu koordinatları nedir?**
   - *Plandan Cevap*: Planda kamera istasyonu MAIN STATION olarak tek sabittir: 24 mm küresel lens, f/8, tam kare yatay (1920×1080), h = +6,0 m çöl zeminindeki kaya yükseltisi üzerinde, cepheye mesafe D = 67,0 m, bearing 20°, tilt 0, roll 0.
3. **0:11'deki toz bulutu post-prodüksiyon mu yoksa fiziksel saha yakalaması mıdır?**
   - *Plandan Cevap*: Planda (S0–S2) ekskavatör ve damperli kamyonların kumul sırtından kum kazarken rüzgârla savrulan doğal çöl tozu (`HAVA_VE_ATMOSFER`, `MALZEME_VE_DOKU`) olarak tasarlanmıştır.
4. **Kapanış kartı yazı tipi ve konumu marka yönergelerine göre kilitlendi mi?**
   - *Plandan Cevap*: Planda teslimde video içi kart yoktu; ancak kurguda 2:00.0'de eklenen statik kart kanal kılavuzuna (`MUZIK_VE_KAPAK`) uygun olarak son kare üzerinde temiz tipografiyle ortalanmıştır.
5. **1:35'teki gece ışık geçişleri yapay pozlama değişikliği mi yoksa gerçek timelapse aralığı mıdır?**
   - *Plandan Cevap*: Planda gün batımı ve mavi saat (19:20, güneş −6,2°) Rejim B hızlandırılmış zamanla (~2 saatlik geçiş tek klipte) temsil edilmiş, akşam çöktüğünde pozlama G13–G15 aralığında ISO 100'den ISO 800'e çekilmiştir (`ZAMAN_VE_ISIK`).

### ❷ ZAMAN VE KESME (Lens 2)
1. **Her klip için beyan edilen güneş yönü ve yükseklik açıları nelerdir?**
   - *Plandan Cevap*: 30° K çöl sahasında 23 Eylül tek gün simülasyonu: 06:00 doğu alçak güneşten (h: 12°, azimut 88°), öğle tepe noktasına (h: 60°, azimut 180°), oradan 18:30 gün batımına (h: 5°, azimut 268°) ve 19:20 mavi saate kadar uzanan 13 saat 20 dakikalık güneş yayı kullanılmıştır.
2. **Çöl sahası için beyan edilen iklim koşulu ve mevsim nedir?**
   - *Plandan Cevap*: Sıcak kurak çöl iklimi (`SAHA_VE_IKLIM_KARTLARI §3.6`), tek gün penceresi, kuru sert zemin ve hareketli kumullar.
3. **Her kesme başına ve tüm film için beyan edilen tam geçen süre nedir?**
   - *Plandan Cevap*: Planda 15 sahne × 8,0 sn = 120,0 sn düz ızgara beyan edilmiştir; kurguda 19 kesme ile 120 saniye tamamlanmış ve 5 saniyelik kartla 125 saniyeye (2:05.0) bağlanmıştır.
4. **Belirli klipler ilerleyen timelapse yerine tutulan saatler (held hours) olarak planlandı mı?**
   - *Plandan Cevap*: Evet; S14 (son sahne) Rejim G (gerçek hız) ve 4,0 sn'lik tutuş olarak planlanmıştır (fenerler yanık, kapı açık, üç kişi eşikte durur).
5. **Ses parçası için beyan edilen müzik temposu ve vuruş ızgarası nedir?**
   - *Plandan Cevap*: Planda müzik beyansızdı (ses tasarımı: kum → taş → rüzgâr → ışık; `THE_BURIED_KHAN_MUZIK.md`); yayına eklenen müzik ise 0:06.0 kesmelerine tam vuruşla (on the beat) oturmuştur (❷ C2 8/10).
6. **1:35'te gündüzden geceye geçiş gerçek zamanlı mı yoksa hızlandırılmış timelapse olarak mı planlandı?**
   - *Plandan Cevap*: Hızlandırılmış timelapse (Rejim B, ~2 saatlik akşam geçişi ~8 saniyede).

### ❸ ŞANTİYE (Lens 3)
1. **0:58'deki taş kemerlerin vinçle parça parça inşa edilmesi mi yoksa fade-in ile belirmesi mi planlanmıştı?**
   - *Plandan Cevap*: Kesinlikle parça parça inşa olarak planlandı (S7–S8 mobil vinç ve ahşap kalıplarla blok montajı). Fade-in modelin fizik ihlalidir.
2. **Klip 17–19'daki gece kamp faaliyetlerine karşı gece hafriyatı için planlanan operasyonel takvim neydi?**
   - *Plandan Cevap*: Kazı gündüz S4'te biter ve ekskavatörler ayrılır; gece (S13–S14) hiçbir kazı yapılmaz, saha restorasyonun tamamlanmasıyla dinlenme ve konaklama işlevine geçer (kamp ateşi, fenerler, dinlenme).
3. **Çöl tabanındaki nakliye kamyonu rotaları üretim tasarımında sabit ham yollara mı bağlandı?**
   - *Plandan Cevap*: Evet; hafriyat sağ kenardaki 1530 px setine taşınırken kamyonlar ve konveyör sabit güzergâhtan sağa akmıştır.
4. **Soldaki ölü ağaç kamera hizalaması için birincil mekânsal referans nirengisi olarak mı belirlendi?**
   - *Plandan Cevap*: Evet; sol kadrajdaki kurumuş akasya ağacı (x 154–259, 105 px) planın 1 numaralı kanıt nesnesidir (`ÇAPALAR ① AKASYA`).
5. **Klip 6'daki kaldırım taşı montajı için hangi malzeme teslim lojistiği planlandı?**
   - *Plandan Cevap*: Kurtarılan taş bloklar ve kervansaray çevresinden el arabalarıyla taşınan yerel kumtaşı levhalar kullanılmıştır.

### ❹ İNŞA (Lens 4)
1. **Kervansaray için belirtilen boyutlar, açıklık sayısı ve yapısal malzeme nedir?**
   - *Plandan Cevap*: 60 m cephe uzunluğu, 16 kemerli iki katlı galeri, 15 m anıtsal giriş kapısı çerçevesi, iki uçta kubbeli köşe kuleleri; malzeme yerel sıcak sarı/kızıl kumtaşı blok duvardır.
2. **0:58'deki ön plan kemer kolonadının mobil vinçle kaldırılıp yerleştirilmesi mi yoksa görsel efektle getirilmesi mi hedeflendi?**
   - *Plandan Cevap*: Mobil vincin bomuyla kaldırılarak örülmesi öngörülmüştü; model ara kareleri üretmeyerek görsel efekt geçişine kaçmıştır (APPEARING).
3. **Alacakaranlık sekansı öncesinde mobil vinç ve iskelenin beyan edilen söküm aşaması nedir?**
   - *Plandan Cevap*: Planda mobil vinç S8'de bomunu katlayıp sağdan çıkar; iskeleler S11'de sökülür ve traktörle taşınır; gün batımında (S12) saha tamamen temizlenmiş olur.
4. **Kum kazısı ile taş blok taşıma aşamaları için hangi özel makine modelleri beyan edildi?**
   - *Plandan Cevap*: S0–S4'te sarı paletli hidrolik ekskavatör ve damperli kamyonlar; S6–S8'de sarı teleskopik mobil vinç; S11 ve sonrasında hafif tarım traktörü ve el arabaları.
5. **Klip 17'deki son gece kamp ateşi buluşması beyan edilen proje kilometre taşının bir parçası mıdır?**
   - *Plandan Cevap*: Evet; kervansarayın onarım sonrası gece yolcularına ev sahipliği yapması ve işlevsel hayata dönmesi planın nihai varış noktasıdır.

### ❺ TESLİM (Lens 5)
1. **Klip 13'teki kum fırtınası yapım senaryosunda belirli bir direnç vuruşu olarak planlandı mı?**
   - *Plandan Cevap*: Evet; planda rüzgâr direnci `DİRENÇ ② rüzgâr — S0–S2 sırttan tüten kum, S9 setin üstünden savrulan ve çitlerde biriken kum` olarak doğrudan senaryolaştırılmıştır.
2. **1:45.0'teki kamp ateşleri ve develerle gece toplanması filmin birincil hedeflenen işlevsel ödülü müdür?**
   - *Plandan Cevap*: Evet; fenerlerin yanması, açık kapıdan ışık taşması ve içeride konaklayanların olması filmin "Ödül" ve "Final Beat" tanımıdır.
3. **Ağır makine sesleri ile akşam müziği geçişi için hangi ses tasarımı yönergeleri belirlendi?**
   - *Plandan Cevap*: Planda ses tasarımı katmanlıdır (`THE_BURIED_KHAN_MUZIK.md`): S0–S4 ağır motor ve hidrolik kazı sesleri → S5–S8 metal çekiç ve iskele tıkırtısı → S9–S12 çöl rüzgârı uğultusu ve süpürge → S13–S14 fener çıtırtısı, uzaktan flüt/yaylı yatağı ve insan uğultusu.
4. **"THE BURIED KHAN" başlığı canlı sahne üzerine bindirme mi yoksa bağımsız bir kart olarak mı hedeflendi?**
   - *Plandan Cevap*: Yayında son sahne üzerine temiz başlık bindirmesi (title overlay) olarak girmiş ve 2:05.0'e kadar 5 saniye tutulmuştur.
5. **Açılış 0:02.0 kancası için hangi hedef kitle tutma metriği planlandı?**
   - *Plandan Cevap*: G0'daki "kumul sırtından çıkan üç tuhaf taş uç" görüntüsü ve ilk 2 saniyede kalkan ilk kovanın yarattığı "Kumun altında ne var?" merak kancası izleyiciyi tutmak üzere kurulmuştur.
