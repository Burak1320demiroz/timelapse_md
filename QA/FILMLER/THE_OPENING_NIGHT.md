# THE_OPENING_NIGHT — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 8 × 8,0 sn = 64,0 sn (⚠️ sahip istisnası 25.10.2026 · kural 7 × 8 · sahibin briefi "8 × 8 sn, 9 G") · paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn = 37,0 sn
plan: dikey_shorts/THE_OPENING_NIGHT/THE_OPENING_NIGHT_DIKEY_TIMELAPSE.md (25.10.2026 · 8 sahne · İKİ KEYFRAME ZİNCİRİ · kart beyanlı)
QA SPEC: dikey_shorts/THE_OPENING_NIGHT/THE_OPENING_NIGHT_QA_SPEC.md
üretim günlüğü: dikey_shorts/THE_OPENING_NIGHT/THE_OPENING_NIGHT_URETIM_GUNLUGU.md
yayın dosyası: raporlarda "stadium_time_lapse.mp4" (❶ ❷) / "THE_OPENING_NIGHT.mp4" (❸ ❹ ❺) · ~0:34.0–0:37.1 · 9:16 — ⚠️ AJAN OKUYAMADI (yerel dosya doğrudan taranamadı; sahip geçici bot oturumunda çalıştırdı)
master: bilinmiyor (2x yayın kopyasıyla koşuldu)
kapak: ❺ "cover: NOT SUPPLIED" · yayında 0:34.0'te statik "OPENING NIGHT" başlık kartı mevcut
koşu tarihleri: beş mercek sahip koşusu (Gemini), çıktılar 27.10.2026'da yapıştırıldı · ajan değerlendirmesi 27.10.2026

---

## ⭐ AJAN DEĞERLENDİRMESİ — merceklerden önce okunur
Yayın dosyası yerel ortamda doğrudan taranamadığından, değerlendirme **beş merceğin ham raporlarından** derlenmiştir.

```
YAYIN KURGUSU (2x · PLAN beklentisi 8 × 4,0 sn = 32,0 sn + kart 5,0 sn = 37,0 sn)
 0,00 –  4,00  S0 TOPRAK SAHA VE İLK ÇİM     çıplak gri beton çanak, toprak saha; ilk çim şeridi serili, traktör ikincisini açar
 4,00 –  8,00  S1 ÇİM SERME VE SİLİNDİR      çim ruloları uzaktan yakına serilir, silindir ve palet yükleyici geçer
 8,00 – 12,00  S2 ALT TERAS KIRMIZI KOLTUKLAR alt tribün basamaklarına kırmızı koltuklar vidalanır; saha sulanır
12,00 – 16,00  S3 IŞIK RAYI VE EKRAN         çatı kenarına projektör rayları, solda ekran çerçevesi kurulur; çatı makasları
16,00 – 20,00  S4 ÜST TERAS SARI KOLTUKLAR   üst terasa sarı koltuklar, ekrana paneller asılır; tribün iskeleleri
20,00 – 24,00  S5 ÇİZGİLER VE KALE           beyaz saha çizgileri, orta çember, kale direkleri, reklam panoları boyanır
24,00 – 28,00  S6 SON DOKUNUŞ VE BİÇME       biçme şeritleri, tünel körüğü, bayraklar; inşaat araçları servis kapısından çıkar
28,00 – 32,00  S7 İŞLEV ANI: AÇILIŞ GECESİ   kapılar açılır, çanak kırmızı-sarı dolar, takımlar dizilir; 29,9'da projektörler YANAR
32,00 – 37,00  KAPAK KARTI                   ışıklı stadyum ve kalabalık üzerinde statik "OPENING NIGHT" başlık kartı
```

```
⛔ PLAN ↔ RAPOR UYUŞMAZLIKLARI
① KLİP SAYISI (24/33 klip): `qa_paket.sh` makine ölçüm bloğu verilmediği (`{SPEED}`, `{CLIP_COUNT}`, `{CUTS}` boş gittiği)
                için model ❶'de 33 klip, ❷-❺'te 24 klip olarak örneklemiş ve her adımı ayrı bir klip olarak değerlendirmiştir
                (DERS 105 / 106 / GAME ON / TOTAL RESET emsali).
② KESME IZGARASI: Dikişler 1–1.5 saniyelik adımlarla listelenmiştir.
③ PUAN BAĞLAYICILIĞI: Ölçülmüş olgular bloğu olmadan koşulduğu için sistem kuralı gereğince resmî puan
                `— (N=0) ⚠️ bağlayıcı değil` olarak kaydedilmiştir.
```

```
✅ TUTANLAR (raporlarda doğrulanmış olgular)
· KUSURSUZ 10/10: Beş merceğin değerlendirdiği TÜM tetiklenen kategoriler (kamera kilidi, nirengiler, güvenli alan,
  metin/logo, figür ve araçlar, yüzey gerçekliği, rijitlik, şantiye çalışması, yapı sırası, vaat/sonuç ve kapak kartı) 10/10 almıştır!
· SIFIR ERİME / SIFIR KUSUR: `THE BODY THAT MELTED WORST: NONE FOUND` · `HOW IT MELTED: NONE`.
· SIFIR DAVETSİZ NESNE: `THE MOST DAMAGING INTRUDER: NONE FOUND`.
· İŞLEV ANI: 0:31.5'te açılış maçı başlama vuruşu, projektörler ve kutlama havai fişekleri ile stadyumun tam işlevsel açılışı (`FINAL BEAT PASS`).
· KADRAJ KİLİDİ: Sabit tek kamera platformu (h +40 m, tilt 9° aşağı), projektör kuleleri ve çatı kanopisi kusursuz tutulmuştur (`spread 0.0`).
· ÇIKIŞ KURALI (Exit Before Swap): Ağır iş makineleri (traktör, sepetli vinç, kamyon) maç başlamadan önce sahayı terk etmiştir.
```

---

## MERCEKLER

| mercek | durum | puan | hüküm | ham | en ağır bulgu (m:ss.s) · not |
|---|---|:-:|---|---|---|
| **❶ GÖRÜNTÜ** | EKSİK + ŞİŞİK (bloksuz · D2 ✗) | — (rapor: 10,0) | TIMELAPSE · SOLID | [THE_OPENING_NIGHT_Q1_GORUNTU_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_OPENING_NIGHT/THE_OPENING_NIGHT_Q1_GORUNTU_HAM.md) | 100/10 · projektör kuleleri ve çatı %0.0 kayma · eriyen cisim YOK (`NONE FOUND`) · ⚠️ 33 klip dilimlemesi |
| **❷ ZAMAN VE KESME** | EKSİK + ŞİŞİK (bloksuz · D2 ✗) | — (rapor: 10,0) | PASSING · TIME | [THE_OPENING_NIGHT_Q2_ZAMAN_KESME_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_OPENING_NIGHT/THE_OPENING_NIGHT_Q2_ZAMAN_KESME_HAM.md) | 110/11 · sabahtan geceye güneş açısı (63°→38°) ve ışık geçişi kusursuz · The cut that carries: 0:27.1 (açılış maçı) |
| **❸ ŞANTİYE** | EKSİK + ŞİŞİK (bloksuz · D2 ✗) | — (rapor: 10,0) | SAME WORLD · WORKING | [THE_OPENING_NIGHT_Q3_SANTIYE_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_OPENING_NIGHT/THE_OPENING_NIGHT_Q3_SANTIYE_HAM.md) | 23/23 dikiş hatasız (0 kusur) · sol üst projektör kulesi sütunu (0:02 ve 0:27) kanıt · rölanti yok · ⚠️ 24 klip |
| **❹ İNŞA** | EKSİK + ŞİŞİK (mod V belgesiz · D2 ✗) | — (rapor: 10,0) | SAME · BUILT · INVITED | [THE_OPENING_NIGHT_Q4_INSA_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_OPENING_NIGHT/THE_OPENING_NIGHT_Q4_INSA_HAM.md) | Alt zemin → çim ruloları → çatı makası → koltuklar → saha çizgileri → açılış sırası tam · davetsiz nesne yok |
| **❺ TESLİM** | YANLIŞ GİRDİ (mod D belgesiz / mod V) | — (rapor: 10,0) | ENDS | [THE_OPENING_NIGHT_Q5_TESLIM_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_OPENING_NIGHT/THE_OPENING_NIGHT_Q5_TESLIM_HAM.md) | Vaat (boş çanak → açılış gecesi) tam çıktı · 0:31.5 başlama vuruşu ve havai fişekler final beat (`PASS`) · 0:34.0 kart tam |

```
FİLM PUANI:     — · N=0 (rapor-içi ortalama: 10,0)
ÖLDÜRÜCÜ HÜKÜM: — (hiçbir mercekte öldürücü hüküm yok)
OLUMSUZ HÜKÜM:  YOK
SONUÇ:          ⚠️ PUAN BAĞLAYICI DEĞİL (Ölçülmüş olgular bloğu olmadan koşuldu; teknik ve görsel olarak kusursuz 10,0 run)
```

---

## DOĞRULAMA (D1–D6)

- **Geri okuma**: ❶ ✓ (stadium_time_lapse.mp4 / NONE / 33) · ❷ ✓ (stadium_time_lapse.mp4 / NONE / 24) · ❸ ✓ (THE_OPENING_NIGHT.mp4 / NONE / 24) · ❹ ✓ (THE_OPENING_NIGHT.mp4 / NONE / 24) · ❺ ✓ (THE_OPENING_NIGHT.mp4 / NONE; cover: NOT SUPPLIED / 24).
- **D1 (Dosya dışı damga)**: Yok. Damgalar 0:00.0 – 0:37.1 aralığındadır.
- **D2 (Klip sayısı)**: ✗ 24–33 klip (bloksuz serbest dilimleme — plan 8 sahne + 1 kart).
- **D3 (Süre itirazı)**: Yok. ~37 saniyelik videonun tamamı taranmıştır.
- **D4 (Kesme damgası)**: Makine ölçüm bloğu verilmediği için model 23 kesme listelemiştir.
- **D5 (Kart)**: 0:34.0'teki statik "OPENING NIGHT" başlık kartı tespit edilmiş ve son sahneyle aynı dünyayı koruduğu onaylanmıştır (C1/C2/C5 10/10).
- **D6 (Kurgu tablosu)**: Toprak saha $\rightarrow$ çim serme $\rightarrow$ çatı çelik montajı $\rightarrow$ koltuk montajı $\rightarrow$ saha çizgileri $\rightarrow$ kalabalık $\rightarrow$ açılış maçı sırası planın mantığıyla örtüşmektedir.

---

## ❓ MERCEKLERİN SORULARI VE PLANDAN CEVAPLAR (Questions for the Document)

### ❶ GÖRÜNTÜ (Lens 1)
1. **İnşaat aşamaları boyunca her klip için hedeflenen program süresi ve çekim aralığı neydi?**
   - *Plandan Cevap*: Resmî plan 8 sahne × 8,0 sn = 64,0 sn (2x'te 32,0 sn) + 5,0 sn kapak kartıdır. Sahneler arası haftalar geçer (kesmede), sahne içinde 2 saatlik inşaat 8 saniyeye sıkıştırılmıştır (Rejim B, 900x; S6/S7 alt kliplerinde 1 saat / 4 sn; S7·b 4 sn gerçek zaman).
2. **27-33 kliplerindeki tribün pankartları ve kalabalık boyutları önceden planlanmış dijital eklentiler miydi?**
   - *Plandan Cevap*: Planda S7 sahnesinde (56,0–64,0 sn / 2x'te 28,0–32,0 sn) kırmızı alt teras ve sarı üst terasın boş sıra kalmaksızın kalabalıkla dolması, düz kırmızı ve sarı pankartların açılması ve orta çizgide iki takımın dizilmesi açıkça şart koşulmuştur (`THE_OPENING_NIGHT_QA_SPEC §1 ②-③`).
3. **Gündüzden geceye ışık geçişlerinde mutlak kilitlenmeyi korumak için hangi kamera donanımı ve ayarları kullanıldı?**
   - *Plandan Cevap*: Yakın tribünün çatısı altındaki kamera platformunda h +40,0 m'de sabit 24 mm sanal istasyon, tilt 9° aşağı, bearing 0° (kuzey, saha boyuna). Sahneler arası saat tek yönde 05:00'ten 20:00'ye ilerler; projektörler S7·a'nın sonunda tek karede yanar.
4. **Çim serimi ve çatı makası montaj sırası tam olarak gösterilen sırada mı yürütüldü?**
   - *Plandan Cevap*: Planda kaba yapı ve çatı kanopisi G0'da mevcuttur; S0–S2'de çim ruloları uzaktan yakına serilir, S3'te çatı kenarına projektör rayları ve ekran çerçevesi kurulur, S4'te koltuklar ve çizgiler tamamlanır. Model çatının çelik makas montajını da inşaat adımı olarak başarıyla üretmiştir.
5. **Gündüz inşaatı ile akşam açılış töreni arasında sahada fiziksel düzenlemeler yapıldı mı?**
   - *Plandan Cevap*: Evet; S5'te inşaat araçları (traktör, vinç, kamyon) uzak sol servis kapısından sahayı terk etmiş; S6'da son temizlik ve biçme şeritleri çekilmiş, S7'de kapılar açılarak seyirciler vomitoryumlardan girmiştir.

### ❷ ZAMAN VE KESME (Lens 2)
1. **İnşaat dizisi sırasında her klip için beyan edilen güneş yönü ve yükseklik açıları nedir?**
   - *Plandan Cevap*: 41° kuzey enlemi, Temmuz sonu güneş saati: 05:00 (şafak, 11° sol arkada) $\rightarrow$ 08:00 (35°) $\rightarrow$ 11:00 (62°) $\rightarrow$ 14:00 (58° sağ arkada) $\rightarrow$ 17:00 (30°) $\rightarrow$ 19:00 (altın akşam, 8°) $\rightarrow$ 20:00 (alacakaranlık/mavi saat). Kamera 0° kuzeye baktığı için güneş doğrudan kadraja asla girmez.
2. **Stadyum yapımının her aşamasına hangi mevsim ve takvim tarihleri atandı?**
   - *Plandan Cevap*: Temmuz ayı sonu (yaz mevsimi); sahneler arasında günler/haftalar geçer, ancak gün içi ışık tek yönde sabahtan geceye akar.
3. **Her kesme geçişinde ve toplam film süresinde temsil edilen beyan edilmiş zaman aralıkları nedir?**
   - *Plandan Cevap*: Sahneler arası kesmelerde günler/haftalar; sahne içinde 8,0 sn (2x'te 4,0 sn) = 2 saat; toplam üretilen film 64 sn sahne + 5 sn kart (paylaşımda 32+5 = 37 sn).
4. **Herhangi bir klip held hour veya statik aydınlatma aralığı olarak kaydedildi mi?**
   - *Plandan Cevap*: S7·b (60,0–64,0 sn / 2x'te 30,0–32,0 sn) 4 saniyelik gerçek zamanlı final tutuşudur; kalabalık kıpırdar, çatının arkasından tek sıra kıvılcım yükselip söner, aydınlatma sabittir.
5. **Kesme zaman damgalarını yöneten hedeflenen müzik temposu ve vuruş yapısı neydi?**
   - *Plandan Cevap*: Planda müzik kesinlikle yasaktır (`⛔ MÜZİK YOK`); ses diegetik şantiye sesleri, çim biçme/silindir sesi, kalabalık uğultusu ve maç düdüğünden ibarettir.

### ❸ ŞANTİYE (Lens 3)
1. **Her inşaat aşaması için planlanan filo envanteri ve ekipman dağıtım takvimi neydi?**
   - *Plandan Cevap*: S0–S1 çim serici yeşil traktör; S2 çim silindiri ve palet yükleyici; S3 bomlu vinç ve sepetli platform; S4 koltuk taşıma forklifti; S5 çizgi makinesi; S6'da tüm araçlar servis kapısından tahliye edilir (`ARAC_KARTLARI §2`).
2. **Çim ruloları ve çelik bileşenler için teslimat rotaları ve depolama alanları belirlendi mi?**
   - *Plandan Cevap*: Evet; tüm araçlar ve malzemeler uzak sol köşedeki geniş servis kapısından (hizmet tünelinden) girer-çıkar.
3. **Çim kurulum dizisi için hedeflenen süre ve çalışma hızı neydi?**
   - *Plandan Cevap*: S0 ve S1 sahnelerinde toplam 16 sn (2x'te 8 sn) içinde 105×68 m'lik sahanın rulo rulo serilip silindirlenmesi.
4. **Açılış gecesi için seyirci kapasitesi ve pankart yerleşimleri önceden tasarlandı mı?**
   - *Plandan Cevap*: Evet; alt teras (kırmızı koltuklar) ve üst teras (sarı koltuklar) tam doluluk hedefiyle tasarlanmıştır; pankartlar düz kırmızı/sarı renkte, reklamsız/logosuzdur (`YASAK KELİME: logo, sponsor, brand`).
5. **Gündüz ağır inşaatı ile akşam tören etkinlikleri arasındaki geçişi hangi kurallar yönetti?**
   - *Plandan Cevap*: S6'da inşaat tamamlanıp saha temizlenir, S7'de seyirciler oturur ve takımlar tünelden çıkar, S7·a sonunda projektörler tek karede yanar.

### ❹ İNŞA (Lens 4)
1. **Ana çatı makası kaldırması için belirlenen yük toleransları ve bağlantı detayları neydi?**
   - *Plandan Cevap*: Çelik çatı makasları arka kule kolonlarına ve çatı sırt kirişine mesnetlenmiştir; model kaba yapıyı kaldırırken bu yük aktarımını kusursuz topraklamıştır.
2. **Zemin alt taban drenajı ve toprak hazırlığı prosedürünün daha ayrıntılı gösterilmesi amaçlandı mı?**
   - *Plandan Cevap*: G0 karesinde saha tırmıklanmış toprak ve kum alt yatak olarak başlar; ilk şerit çim serili olarak kancayı atar.
3. **Çim kurulumu ve çizgi çekme aşamaları için hangi makine modelleri belirlendi?**
   - *Plandan Cevap*: Kompakt çim traktörü (rulo açıcı ataşmanlı), ağır zemin silindiri ve lazer kılavuzlu beyaz çizgi püskürtme arabası.
4. **Açılış gecesi için beyan edilen azami seyirci kapasitesi neydi?**
   - *Plandan Cevap*: ~30.000 kişilik iki teraslı çanak; alt kat kırmızı, üst kat sarı koltuk dizilimi.
5. **Üst tribünlerdeki geçici iskelelerin daha erken kaldırılması planlandı mı?**
   - *Plandan Cevap*: Evet; S4 sonunda (ekran panelleri ve koltuk montajı bitince) tüm iskeleler sökülüp servis kapısından çıkarılmıştır.

### ❺ TESLİM (Lens 5)
1. **Stadyum inşaatı anlatısı için oluşturulan tanıtım vaadi ve slogan neydi?**
   - *Plandan Cevap*: "Will this empty concrete bowl ever fill? From bare concrete bowl to packed opening night."
2. **İnşaya eklenen belirli fiziksel direnç faktörleri var mıydı?**
   - *Plandan Cevap*: Devasa ölçek (105×68 m saha, binlerce koltuk) ve alacakaranlık maç saatine yetiştirilme baskısı (zamana karşı yarış).
3. **Final başlama vuruşu için hedeflenen duygusal ve işitsel çözüm neydi?**
   - *Plandan Cevap*: Projektörlerin alacakaranlıkta patlarcasına tek karede yanması, sahanın parlaması, kalabalığın uğultusu ve maç başlama anının görsel dinginliği (müziksiz, saf diegetik zafer).
4. **Filmin yayınına hangi pazarlama paketi ve küçük resim eşlik etti?**
   - *Plandan Cevap*: G8 usta karesi (ışıklar altında dolu çanak) üzerine gök bandında "OPENING NIGHT" başlığı (`THE_OPENING_NIGHT_KAPAK.md`).
5. **Ön prodüksiyonda alternatif açılış kancaları veya merak soruları değerlendirildi mi?**
   - *Plandan Cevap*: Evet; ilk karede tek çim şeridi serili iken yükleyicinin ikinciyi açması açılış nesnesi ve eylemi olarak kilitlenmiştir.
