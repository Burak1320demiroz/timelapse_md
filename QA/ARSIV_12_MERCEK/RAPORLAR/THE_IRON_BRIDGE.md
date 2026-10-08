# 🔍 THE IRON BRIDGE — QA RAPORU

```
FİLM          THE IRON BRIDGE — Ilıman ormanlık dağ vadisinde nehir üstüne 40 m açıklıklı tek açıklıklı çelik kemer yaya köprüsü inşası (12 sahne × 10,0 sn = 120,0 sn + 5,0 sn kapak kartı = 125,0 sn plan; teslim: 12 sahne klipi + 1 kapak kartı · toplam süre: ~100 sn / video oynatma: 01:40.0)
TARİH         03.10.2026
DURUM         ⭐ ON İKİ MERCEK EKSİKSİZ TAMAMLANDI (12/12)!
              🏆 ON İKİ MERCEK GENEL ORTALAMASI: 7,65 / 10
              🏆 SEKİZ TEMEL MERCEK ORTALAMASI: 7,19 / 10
              ⭐ KUSURSUZ 10/10 TAM PUAN:
                 ⑪ ENVANTER 10,0/10 Ⓥ (Mod V) — INVITED (Her şey davetli, sivil/yabancı araç sızıntısı YOK / NONE FOUND)
              ⭐ ÖNE ÇIKAN YÖNTEM VE KATILIK BAŞARILARI:
                 ⑧ YÖNTEM 9,6/10 (Mod D) — MADE (9/9 yapı elemanı sıfırdan ekranda yapıldı, ilk beliren: YOK / NONE, en iyi: Sağ Beton Kenar Ayak)
                 ⑫ KATILIK 8,8/10 Ⓥ (Mod V) — SOLID (Ağır iş makineleri, vinçler ve çelik strüktür katı formunu korudu)
                 ⑨ FAALİYET 8,75/10 Ⓥ (Mod V) — PRODUCTIVE WORK (Yapay animasyon döngüsü ve ping-pong YOK)
              ⭐ BEYAN EDİLEN SÜRE VE MEVSİM TUTARLILIĞI:
                 Zaman tahmini "1,25–1,5 yıl (15–18 ay)" (plan: ~15 ay Nisan→Temmuz) TAM TUTTU!
                 Mevsim döngüsü ve taşıyıcıları 9/10 (ilkbahar → yaz → sonbahar → kış → ilkbahar → yaz → sonbahar)
              ⭐ ASGARİ SET (① + ② + ⑤):
                 ① 7,1 Ⓥ  ·  ② 6,0  ·  ⑤ 6,9 Ⓥ  →  GEÇTİ ANCAK 9,0 EŞİĞİNİN ALTINDA (Kritik arıza mevcut)
              ⭐ DÜNYA VE ÇAPA KANITI:
                 Sol kıyıdaki büyük meşe ağacı [00:02 ve 01:30] dünyayı ve mekanı kanıtlamıştır (SAME WORLD).
              ⛔ KRİTİK ZİNCİR HATASI (00:51.0):
                 Klip 7'de (S05) S03–S04 boyunca yükselmiş olan ana çelik kemer strüktürü aniden tamamen yok olmakta,
                 nehir yatağında sadece beton ayaklar kalmakta; 00:55.0'te (S06) kemer sıfırdan tekrar monte edilmektedir.
                 Bu arıza sebebiyle:
                   - ① KARE: "BU BİR TIME-LAPSE Mİ?: SIX SEPARATE SHOTS" (7,1/10 Ⓥ)
                   - ② İNŞA: Monotonik Büyüme 2/10, İnşa Sırası 5/10 (6,0/10)
                   - ④ TESLİM: Final Beat Fail (4/10), Bedel 4/10 (5,7/10)
                   - ⑤ DEVAMLILIK: Dikiş 6 Kusurlu (Kemer ve zemin sıfırlanması) (6,9/10 Ⓥ)
                   - ⑥ GEÇİŞ: Zaman yönü tersine döndü hissi (Direction 4/10), 8s aralıklar → METRONOME (7,3/10 Ⓥ)
                   - ⑦ İŞ: Sebep-Sonuç 3/10 (00:50.0 The Growth Nobody Made) (7,0/10 Ⓥ)
                   - ⑩ SEBEP: The Causal Link 4/10, Hüküm: MAGICAL APPEARANCE (6,8/10 Ⓥ)
              ⭐ BİTİŞ KARTI DENETİMİ:
                 Tüm 12 mercekte "AYNI" (SAME) onaylandı. Bitiş kartı S11 usta karesiyle birebir aynıdır.
HAM           QA/HAM_RAPORLAR/THE_IRON_BRIDGE/ (THE_IRON_BRIDGE_1_KARE_HAM.md … THE_IRON_BRIDGE_12_KATILIK_HAM.md)
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|---:|---|---|
| **① KARE** | V | **7,1**/10 Ⓥ | ⛔ **SIX SEPARATE SHOTS** | Kamera kilidi 8 · İstasyon kimliği 8 · Güvenli alan 9 · Metin 8 · Kadraj kimliği 7 · Çapa kimliği 6 · Yüzey gerçeği 6 · İnsan ve Araçlar 5 · C1 Vinç 7 · C2 Kar/Su 6 · C4 Gece/Alacakaranlık 8 · Ufuk %48,5 (%1,0 yayılım) · ⛔ 00:51 kemer yok olması · 00:41 meşe yaprak rüzgarında mikro titreme ve AI morphing · End Card: **SAME** |
| **② İNŞA** | D | **6,0**/10 | ✅ **SAME · BUILT** | **Hüküm: SAME · BUILT** · Yapı kimliği 8 · C2 Kazı 8 · Ölçek kilidi 7 · Makine ve yöntem 7 · Geometrik stabilite 7 · C3 Su varlığı 7 · Yük yolu ve destek 6 · İnşa sırası 5 · Geçici ekipman 5 · ⛔ **Monotonik Büyüme 2/10 (00:51.0'de kemerin aniden yok olup 00:55'te baştan kurulması)** · 00:20 ahşap servis köprüsünün sökümsüz kaybolması · End Card: **SAME** |
| **③ ZAMAN** | V | **7,9**/10 Ⓥ | ✅ **PASSES** | **Zaman tahmini "1,25–1,5 yıl (15–18 ay)" (plan ~15 ay) TAM TUTTU** · Mevsim sırası 9 · Mevsim taşıyıcısı 9 · Vejetasyon 9 · Gölge boyu/açı 8 · Bulut ve gökyüzü 8 · Pozlama kararlılığı 8 · Kar 8 · Güneş yönü 7 · Zaman hızı 7 · Zaman sıçraması kesmesi 6 · 00:40–00:55 kemer sıfırlanmasının zaman akışıyla yapısal çelişkisi · End Card: **SAME** |
| **④ TESLİM** | D | **5,7**/10 | ✅ **ENDS** | **Hüküm: ENDS** · ⭐ **ONE THING BULUNDU** ("Nehir üzerinde çelik kemerli bir köprünün doğa koşulları eşliğinde sıfırdan yapımını tek sabit açıdan sunması") · Vaat 7 · Kapak 7 · Direnç 6 · Çengel 6 · Sahne ayrışması 6 · Döngü 5 · Kurgu 5 · ⛔ **FINAL BEAT FAIL (4/10 — 00:51 yapı sıfırlanması kurgu bütünlüğünü bozdu)** · End Card: **SAME** |
| **⑤ DEVAMLILIK** | V | **6,9**/10 Ⓥ | ✅ **SAME WORLD** | **Hüküm: SAME WORLD** · ⭐ **Kanıt nesnesi: Sol kıyıdaki büyük meşe ağacı [00:02 ve 01:30]** · Bitki örtüsü ve su 9 · Aşınma ve birikim 8 · İnsan ve trafik 8 · Erişim ve güzergah 8 · Dikiş denetimi 7 (2/11 kusurlu) · İkincil nesne 6 · Makine kimliği 5 · Zemin durumu aktarımı 5 · C1 Kar/su 6 · End Card: **SAME** |
| **⑥ GEÇİŞ** | V | **7,3**/10 Ⓥ | ✅ **TIME · ⚠️ METRONOME** | **Hüküm: TIME · METRONOME** · ⭐ **THE CUT THAT CARRIES: Kesme 00:55.0 (İlkbahar gelişi ve kemer montajının yeniden ivmesi)** · Kesme mekaniği 10 · Nirengi hayatta kalma 9 · Bitiş kartı devri 9 · Sıçrama okunurluğu 8 · Mevsim değişimi 7 · Sıçrama boyu 6 · Ritim ve örüntü 5 (8s eşit aralıklar → metronom) · Zaman yönü 4 (00:40–00:48 geriye sıçrama) · Müzik: Not Triggered (doğal ses) |
| **⑦ İŞ** | V | **7,0**/10 Ⓥ | ✅ **WORKING** | **Hüküm: WORKING** · C2 Açılış/Teslim 9 · Makine döngüsü 8 · Malzeme akışı 8 · Çalışma cephesi 8 · Aynı bitki 8 · Yavaş klip 8 · Boşta bekleme 7 · İş/büyüme oranı 7 · Alma 4 · ⛔ **Sebep-sonuç 3 (00:50.0 The Growth Nobody Made)** · En uzun boş aralık: 16.0s (C2 teslim) |
| **⑧ YÖNTEM** | D | **9,6**/10 | ✅ **YAPILDI (MADE)** | **9/9 yapı elemanı sıfırdan ekranda yapıldı** · Envanter tamlık 10 · Bütün doğmama 10 · Yöntem ekranda 10 · Adım sırası 10 · C3 Vinç yerleştirme 10 · Tekrarlayan elemanlar 9 · Tek tek ilerleme 9 · Malzeme kaynağı 9 · Telefonda okunabilirlik 9 · ⭐ **İlk beliren parça: YOK (NONE)** · En iyi yapılan: Sağ Beton Kenar Ayak |
| **⑨ FAALİYET** | V | **8,75**/10 Ⓥ | ✅ **PRODUCTIVE WORK** | **Hüküm: PRODUCTIVE WORK** · Amaçsız hareket 9 · Animasyon döngüleri 9 · İnsan gücü/işçi faaliyeti 9 · Rölanti/park 8 · ⭐ **En amaçsız faaliyet: 00:41–00:45 rüzgarlı sahnede vincin boş halat salınımı** · Yapay ping-pong döngüsü YOK |
| **⑩ SEBEP** | V | **6,8**/10 Ⓥ | ⚠️ **MAGICAL APPEARANCE** | Emek ölçeği 8 · İşsiz yakınlık 8 · Malzeme kaynağı 7 · ⛔ **Nedensellik bağı 4 (00:50.0 kemer kaybı ve 00:55.0'de vinç kancasında aniden belirmesi)** · 10/11 eleman emekle açıklandı (CAUSED), 1 eleman MAGIC |
| **⑪ ENVANTER** | V | **10,0**/10 Ⓥ | ✅ **INVITED** | **6/6 kategori 10/10 kusursuz tam puan** · İnsanlar/canlılar 10 · Makine gövdeleri 10 · Yapılar/komşular 10 · Işık/enerji 10 · Dünyanın kuralları 10 · Davet edilenler 10 · ⭐ **Davetsiz misafir: YOK (NONE FOUND)** · Gelmeyen: YOK |
| **⑫ KATILIK** | V | **8,8**/10 Ⓥ | ✅ **SOLID** | **Hüküm: SOLID** · Kenarlar ve siluet 9 · Sayı 9 · Kimlik 9 · Boyut 9 · Geçişme 9 · Doğuş 9 · Mekanizma 9 · C1 Yük yolu 9 · C2 Toz/sprey 9 · Zemin/sıvı 8 · C3 Su/kar 8 · ⭐ **En çok eriyen gövde: 00:51 taşkın sahnesinde kule tabanı (edge crawl)** |

---

## 2. ⛔ HÜKÜM VE KALİTE ANALİZİ

```
1. 00:51.0 KEMER YOK OLUŞU VE YENİDEN MONTAJ (ÇEKİRDEK ARIZA):
   - S03 ve S04 (00:30–00:50) boyunca yükselen çelik kemer kavisinin, Klip 7 açılışında (00:51–00:54) aniden
     tamamen silinerek yalnızca temel ayaklarına dönmesi, ardından 00:55'te vinçlerle sıfırdan monte edilmesi
     bu filmin tüm merceklerini olumsuz etkileyen ana çekirdek arızadır.
   - Planda S4 (%40) → S5 (%65) → S6 (%80) kesintisiz lineer büyüme kilitlenmiştir; kemerin sökümü veya
     kaybolması hiçbir şekilde planlanmamıştır. Modelin referans kare tutarlılığını kaybettiği bariz bir I2V sıfırlanmasıdır.
   - Bu arıza:
       * ① KARE'de "SIX SEPARATE SHOTS" hükmü doğurmuş,
       * ② İNŞA'da Monotonik Büyüme'yi 2/10'a düşürmüş,
       * ④ TESLİM'de Bedel ve Final Beat'i FAIL (4/10) yapmış,
       * ⑤ DEVAMLILIK'ta Dikiş 6'yı kusurlu kılmış,
       * ⑥ GEÇİŞ'te zamanın geriye aktığı algısına (4/10) yol açmış,
       * ⑦ İŞ'te Sebep-Sonuç'u 3/10'a indirmiş ve "The Growth Nobody Made" satırına girmiş,
       * ⑩ SEBEP'te nedensellik bağını kırarak MAGICAL APPEARANCE hükmü vermiştir.

2. ENVANTER, YÖNTEM, KATILIK VE FAALİYET BAŞARISI (⑪ 10,0 · ⑧ 9,6 · ⑫ 8,8 · ⑨ 8,75):
   - ⑪ ENVANTER'de tüm kategorilerde 10/10 kusursuz puan alınmış; sahadaki tüm insanlar baretli/yelekli ekip,
     tüm makineler standart şantiye aracı olarak doğrulanmış, hiçbir yabancı sivil veya araç sızmamıştır (INVITED).
   - ⑧ YÖNTEM'de 9/9 elemanın tamamı (servis köprüsü, kenar ayaklar, kuleler, kemer, askı halatları, tabliye,
     ahşap kaplama/korkuluk, yaklaşım yolu) ekranda sıfırdan inşa edilmiştir (MADE).
     Kendiliğinden beliren parça YOKTUR (NONE). Deponun 12. belgeli yöntem başarısı tescil edilmiştir!
   - ⑫ KATILIK'ta görsel nesnelerin, ağır makinelerin ve çelik strüktürün katı form bütünlüğü başarıyla korunmuştur (SOLID).
   - ⑨ FAALİYET'te işçi ve makine hareketlerinin üretken olduğu (PRODUCTIVE WORK), yapay animasyon döngüsü
     veya sahte ping-pong bulunmadığı onaylanmıştır.

3. ZAMAN AKIŞI, DÜNYA VE ÇAPA SADAKATİ (③ 7,9 · ⑤ 6,9):
   - Zaman merceğinin bağımsız tahmini ("1,25–1,5 yıl / 15–18 ay"), projenin hedeflenen 15 aylık takvimiyle
     (Nisan ilkbaharından ertesi yılın Temmuz yazına) kusursuz örtüşmüştür.
   - Sol kıyıdaki anıt meşe ağacı [00:02 ve 01:30] ve sağ kayalık platform sahneler boyunca kilitli kalarak
     mekanın tek bir dünya olduğunu kanıtlamıştır (SAME WORLD).
   - Bitki örtüsü döngüsü (yeşerme → sararma → dökülme → kar örtüsü → yeniden filizlenme) ve nehir debisi
     mevsim taşıyıcısı olarak son derece başarılıdır (9/10).

4. RİTİM VE SÜRE DEĞERLENDİRMESİ (⑥ 7,3 METRONOME · ④ SÜRE SIKIŞMASI):
   - Filmde kesme aralıklarının neredeyse tamamı 8,0 saniyelik sabit adımlarla ilerlediği için kurgusal ritim
     yükseliş-düşüş yaşayamamış ve METRONOME hükmü almıştır. (Bu durum DÜZ IZGARA beyanında öngörülen riskle örtüşmektedir).
   - Toplam video süresi 01:40.0 (96 sn aktif sahne + 4 sn kapak), plandaki 120 sn + 5 sn hedefine kıyasla
     yaklaşık 24 saniye erken tamamlanmıştır.

5. BİTİŞ KARTI DENETİMİ:
   - Tüm 12 mercekte bitiş kapak kartı "AYNI (SAME)" olarak tescil edilmiştir; yabancı mimari öğe sızmamıştır.
```

---

## 3. ❓ DOKÜMAN SORULARININ YANITLARI

### ① KARE (LENS 1)

1. **Klip 7'de (00:48 – 00:55) yükselmiş olan kemerin aniden sahneden kaybolup nehir seviyesine dönmesi planlanmış bir revizyon/söküm adımı mıdır, yoksa zincir üretim hatası mıdır?**  
   * **Yanıt:** Kesinlikle bir **zincir ve üretim hatasıdır**. `THE_IRON_BRIDGE_PLAN.md` §AŞAMA MERDİVENİ ve `THE_IRON_BRIDGE_QA_SPEC.md` uyarınca kemer inşaatı S4 (%40 kemer) → S5 (%65 kemer) → S6 (%80 kemer, kış taşkını bekleme) → S7 (%95 kemer) şeklinde **monotonik olarak büyümek zorundadır**. Kemer hiçbir aşamada sökülmez veya sahneden silinmez. Klip 7 (S05) üretiminde I2V modelinin referans kare zincirini kopararak sahneyi ilk aşamalara sıfırladığı tespit edilmiştir.

2. **Kamera istasyonunun ufuk seviyesinin (%48.5) sahneler arasındaki %1.0'lik sapma toleransı kabul edilebilir sınırlar içinde midir?**  
   * **Yanıt:** Evet, kabul edilebilir tolerans dahilindedir. Plandaki nominal ufuk hattı (tilt 0° göz çizgisi) %50,0'dir. Ölçülen %48.5 değeri ve sahneler arası %1.0'lik maksimum yayılım, deponun ±%1.0 tolerans bandı içindedir.

3. **İnşaat araçları üzerindeki ticari markaların ve plakaların kasıtlı olarak jenerikleştirilmesi/bulanıklaştırılması istenen bir kural mıdır?**  
   * **Yanıt:** Evet, istenen ve zorunlu bir kuraldır. `KANAL_KIMLIGI` ve `PROMPT_SABLONU` gereğince şantiyedeki makinelerde gerçek marka logoları, ticari amblemler ve okunabilir plakalar yapaylık ve telif riski nedeniyle yasaktır; jenerik endüstriyel dokular hedeflenir.

---

### ③ ZAMAN (LENS 3)

1. **S03 sahnesinde birleştirilen ana çelik kemerin S04/S05 kış sahnelerinde kadrajda görünmeyip S06'da tekrar kaldırılması planlanmış geçici bir yapı aşaması mıdır, yoksa görsel bir hiyerarşi hatası mıdır?**  
   * **Yanıt:** Planlanmış bir aşama değildir; **görsel üretim arızasıdır**. Planda kış taşkını (S6) sırasında inşaat durur ("BEKLER · nehir TAŞKIN · iş durdu"), ancak o ana kadar monte edilmiş olan %80 oranındaki çelik kemer yerinde kalır. S05'te kemerin yok olması ve S06'da yeniden vinçlerle kaldırılması modelin zincir kopukluğudur.

2. **S08 sahnesindeki altın saat / gün batımı geçişi için beyan edilen hedef güneş açısı ve zaman katsayısı nedir?**  
   * **Yanıt:** Planda S8 sahnesi Nisan 11:00 (orta-yüksek güneş, azimut 185°, 65° yükseklik, Rejim B) olarak belirlenmiştir. Videoda S08'de güneşin hızla alçalıp gölgelerin uzaması, planda S10 (16:00, 45°) ve S11 (17:30, 18° altın saat) sahneleri için öngörülen Rejim A kapanış ışığının kurguda erken uygulanmasından veya kurgu zaman sıçramasından kaynaklanmaktadır.

3. **S04 ile S05 arasındaki sel ve kış geçişi için planlanan takvim aralığı kaç aydır?**  
   * **Yanıt:** S4 (Temmuz) ile S5 (Kasım) arası yaklaşık **4 aydır**; S5 (Kasım) ile S6 (Ocak) taşkını arası ise **2 aydır**. Dolayısıyla yaz sonundan tam kış koşullarına geçiş toplamda yaklaşık **6 aylık** bir takvimi kapsamaktadır.

---

### ⑤ DEVAMLILIK (LENS 5)

1. **S01 klibindeki geçici ahşap servis köprüsünün söküm süreci aşamalı olarak gösterilmeli miydi, yoksa planlı ani bir saha temizliği mi öngörüldü?**  
   * **Yanıt:** Planda ve `INSAAT_YONTEMI_KILAVUZU` kuralları uyarınca geçici servis köprüsünün söküm eylemi ya kadrajda gösterilmeli ya da kademeli olarak kaldırılmalıdır. S01'den S02'ye geçerken köprünün tek bir kesmede iz bırakmadan yok olması bir dikiş ve kurgu kusurudur (Dikiş 2 Kusurlu).

2. **S05 kış sahnesindeki sel/taşkın olayı, inşa edilen kemerin yıkılıp yeniden yapılmasına neden olan gerçek bir şantiye olayı mıdır, yoksa görsel jenerasyon tutarsızlığı mıdır?**  
   * **Yanıt:** Kesinlikle bir **görsel jenerasyon tutarsızlığıdır (model hallucination)**. Planda DİRENÇ ① (Nehir taşkını) inşaatın durmasını ve nehir suyunun yükselmesini simgeler; monte edilmiş çelik kemerin sel tarafından yıkılması veya sahneden silinmesi ASLA öngörülmemiştir.

3. **Sahneler arası değişen vinç ve ekskavatör tipleri/renkleri şantiyedeki alt yüklenici değişimini mi yansıtmaktadır?**  
   * **Yanıt:** Hayır, modelin makine kimliği devamlılığını koruyamamasından kaynaklanan bir AI morfi hatasıdır. Planda şantiye boyunca sabit bir 15 m mobil vinç ve standart ekskavatör tanımlanmıştır; araç renklerinin sarıdan beyaza, vincin turuncudan beyaza değişmesi üretim arızasıdır.

---

### ⑦ İŞ (LENS 7)

1. **Aşamalar merdiveninde (stage ladder) Klip 5 ile Klip 6 arasında kasıtlı bir revizyon veya söküm/yeniden montaj adımı tanımlanmış mıdır?**  
   * **Yanıt:** Hayır. Planda `THE_IRON_BRIDGE_PLAN.md` §AŞAMA MERDİVENİ S4 (KAYNAR · Kemer %40), S5 (DİRENİR · Kemer %65) ve S6 (BEKLER · Kemer %80 · nehir taşkını · iş durdu) adımları yer alır. Hiçbir revizyon veya söküm adımı tanımlanmamıştır; monotonik büyüme esastır.

2. **00:50.0'daki kemer kaybı kurgusal bir kare atlaması (missing render generation) mıdır, yoksa planlanmış bir mevsimsel ara mıdır?**  
   * **Yanıt:** Kurgusal/üretimsel bir model tutarsızlığı ve kare atlamasıdır (I2V sıfırlanması). Planda kış taşkınında işin durması öngörülmüş ("BEKLER · iş durdu"), fakat inşa edilen kemerin kadrajda kalması kilitlenmiştir.

3. **Ana kemerin montajı plan belgelerinde kaç aşamalı (tek seferlik mi yoksa çift döküm/montaj mı) olarak kodlanmıştır?**  
   * **Yanıt:** Tek seferlik kademeli montajdır: S4'te iki yakadan %40 yükselir, S5'te %65'e ulaşır, S7'de 2 m boşluk kalır ve S8'de taç birleşimiyle tek seferde kalıcı olarak kapanır. Çift montaj yoktur.

---

### ⑨ FAALİYET (LENS 9)

1. **00:48 - 00:54 arasındaki yüksek su seviyesi ve mevsim geçişi sahnesinde ekipmanların sahadan tahliyesi planlı bir duraklama mıdır?**  
   * **Yanıt:** Evet, tam olarak planlı bir duraklamadır. Planda DİRENÇ ① (Nehir taşkını) ve S6 (Ocak, BEKLER · nehir TAŞKIN · iş durdu) olarak kurgulanmıştır. Nehir taşkını sırasında çalışma cephelerinin durması ve araçların güvenli alana çekilmesi bilerek tasarlanmış şantiye direncidir.

2. **01:18 - 01:27 aralığındaki yürüyüş yolu taş döşeme çalışması ana köprü yüklenicisi kapsamına mı dahildir?**  
   * **Yanıt:** Evet, dahildir. Planda S10 (SÖKER) ve S11 (TESLİM) aşamalarında köprünün iki yakasındaki yaklaşım yollarının kilit taşı/blok taş ile kaplanması ve peyzaj düzenlemesi projenin ayrılmaz bir parçası olarak tanımlanmıştır.

---

### ⑫ KATILIK (LENS 12)

1. **00:48 - 00:55 arasındaki taşkın sahnesinde nehir ortasındaki geçici kafes kulenin suda kalan kısmındaki form değişimi fiziksel sökümden mi yoksa akıntı görselleştirmesinden mi kaynaklanmaktadır?**  
   * **Yanıt:** Akıntı ve su yükselmesi (taşkın) görselleştirmesinden kaynaklanmaktadır. Planda DİRENÇ ① (nehir taşkını) ve S6 (Ocak, BEKLER · nehir TAŞKIN · su seviyesi kule tabanını aşar) olarak kurgulanmıştır. Kulelerin fiziksel sökümü S10 aşamasındadır; sudaki hafif kenar dalgalanması yükselen suyun kafes metal gövdeyle yarattığı akış etkileşimidir.

2. **00:24 ve 00:32 sahnelerindeki destek kulelerinin montaj sıralamasında kullanılan vinç kapasiteleri şantiye planına uygun olarak mı kurgulanmıştır?**  
   * **Yanıt:** Evet, uygundur. Planda `THE_IRON_BRIDGE_PLAN.md` §DEĞİŞMEZLER ve §ÖNCELİK KATMANLARI P0.⑥ kapsamında: *"15 m mobil vinç · iki çelik destek kulesi H≈10 m dikimi"* ve S3/S4'te modül kaldırma operasyonları tanımlanmıştır. Kullanılan vinç boyut ve kapasite olarak şartnameye uygundur.

---

## 4. 📋 OLAY TABLOSU (EVENT LOG)

| Olay | Zaman Kodu | Ne Oldu (Görünen) | Mercekler | Kanıt / Durum | Karar |
|:---:|:---:|---|:---:|:---:|:---:|
| **E01** | 00:51.0 | S03–S04 boyunca yükselen çelik kemer Klip 7 açılışında tamamen yok olmuş, 00:55'te sıfırdan monte edilmeye başlanmıştır. | ① ② ③ ④ ⑤ ⑥ ⑦ ⑩ | Klip 7 (S05) | ⛔ **KRİTİK ZİNCİR HATASI (FAIL)** — Monotonik büyüme, dikiş ve nedensellik ihlali; I2V model sıfırlanması. Yeniden üretim gerektirir. |
| **E02** | 00:41.5 | Sol meşe ağacı dallarında sonbahar yaprak dökümü simülasyonu esnasında AI morphing ve biçimsel dal deformasyonu. | ① | Klip 6 (S04) | **KAYDEDİLDİ (RECORDED)** — Doğal hareket yerine üretken model distorsiyonu. |
| **E03** | 00:20.0 | S01'de nehri geçen geçici ahşap servis köprüsü, S02 başlangıcında söküm adımı gösterilmeksizin kaybolmuştur. | ② ⑤ | Klip 2 ↔ 3 (Dikiş 2) | **KAYDEDİLDİ (RECORDED)** — Geçici ekipman sökümünün gösterilmemesi. |
| **E04** | 00:25.5 | Mobil vincin çelik kemer segmentine bağlandığı kaldırma halatında kırılma ve tepe noktasında süreklilik kopukluğu. | ① | Klip 4 (S03) | **KAYDEDİLDİ (RECORDED)** — İnce kablo/halat AI çözünürlük kaybı. |
| **E05** | 01:17.5 | Kamyonet kasası ve plaka bölgesinde okunaksız metin benzeri leke desenleri. | ① | Klip 11 (S10) | **KABUL EDİLDİ (PASS)** — KANAL_KIMLIGI marka yasağına uygundur, okunabilir yabancı marka yoktur. |
| **E06** | 00:09.0 | Beton dökümü esnasında ön plandaki işçilerde time-lapse motion blur yerine donmuş poz deformasyonu. | ① | Klip 2 (S01) | **KAYDEDİLDİ (RECORDED)** — Düşük deklanşör hızı yerine statik AI poz üretimi. |
| **E07** | 01:19–01:25 | Köprü kaldırımı döşenirken güneşin hızla alçalması, gölgelerin aniden uzaması ve mercek parlaması. | ③ | Klip 10 (S08) | **KAYDEDİLDİ (RECORDED)** — Rejim A akşam ışığına erken geçiş. |
| **E08** | 00:05.0 ↔ 00:08.0 | Sarı paletli büyük ekskavatör dikiş sonrası beyaz renkli küçük paletli ekskavatöre dönüştü; 00:41 ↔ 00:55'te turuncu mobil vinç beyaz kamyon üstü vince dönüştü. | ⑤ | Klip 1 ↔ 2, Klip 5 ↔ 7 | **KAYDEDİLDİ (RECORDED)** — Makine kimliği devamlılık kusuru (AI model tutarsızlığı). |
| **E09** | 00:08 – 01:36 | 12 sahne kesmesinin neredeyse tamamı 8,0 saniyelik sabit düzende ilerleyerek metronomik kurgu oluşturmuştur. | ⑥ | Kurgu Zaman Çizelgesi | **KABUL EDİLDİ (PASS)** — Düz ızgara tercihiyle uyumlu, kabul edilen risk gerçekleşti. |
| **E10** | 01:40.0 | Kurgu toplam süresi 100 sn (96 sn aktif sahne + 4 sn kapak) sürmüştür (Planlanan: 120 sn + 5 sn kapak). | ④ ⑥ | Kurgu Zaman Çizelgesi | **KAYDEDİLDİ (RECORDED)** — Klip süreleri ortalama 8 sn olarak uygulanmış, süre 24 sn kısa kalmıştır. |
| **E11** | 00:55.0 | Kış taşkınının ardından ilkbaharın gelişi ve kemer montajının yeniden başladığı ana kırılma noktası (The Cut That Carries the Film). | ⑥ | Kesme 7 (00:55.0) | **ÖDÜLLENDİRİLDİ (CARRY)** — Filmin ana dramatik ve mevsimsel dönüşümünü taşıyan kesme. |
| **E12** | 00:41 – 00:45 | Rüzgarlı sonbahar sahnesinde mobil vincin kaldırma halatının yük olmaksızın boşta salınması. | ⑨ ⑫ | Klip 6 (S04) | **KABUL EDİLDİ (PASS)** — Doğal rüzgar etkisi altında hafif boşta salınım, yapay döngü içermez. |
| **E13** | 01:19 – 01:35 | Klip 11'de 16 saniye boyunca sahadan tüm iş makineleri çekilmiş halde gün batımında tamamlanmış köprünün sergilenmesi. | ⑦ | Klip 11 (S11) | **KABUL EDİLDİ (PASS)** — C2 Teslim tutuşu (Handover hold) kuralına uygundur. |
| **E14** | 00:48 – 00:54 | Taşkın ve eriyen kar suyunun yükseldiği sahnede nehir yatağındaki geçici çelik kulelerin zemin birleşim yüzeyinde hafif kenar dalgalanması (edge crawl). | ⑫ | Klip 7 (S05) | **KABUL EDİLDİ (PASS)** — Yüksek debili sıvı etkileşimi, metal gövde katı formunu korumuştur. |
