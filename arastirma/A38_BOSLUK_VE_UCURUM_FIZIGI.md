# 🧪 A38 — BOŞLUK, UÇURUM VE ZEMİN DESTEĞİ FİZİĞİ

```
AMAÇ      Uçurum kenarları, kanyonlar, su yüzeyleri ve gökyüzü gibi boşluklardan tekerleksiz
          hayalet iş makinelerinin türemesini (phantom machinery from voids), yerinde döküm
          ile prefabrikasyonun üst üste binerek gökyüzü kancasından hazır monolitik kütleler
          indirilmesini ve yıkım-montaj aşamalarının geriye doğru işlemesini engellemek;
          "boşluk dokunulmazlığı", "yerçekimi/zemin desteği" ve "yapım sırası grafı"
          kurallarını ölçülebilir kılmak.
KARŞILIĞI 15.10.2026 THE SKY STATION Bölüm 1 ölçümleri:
          · DERS 81: Uçurumun dibindeki dipsiz kanyon boşluğundan, tekerleği veya şasisi
            olmayan beyaz bir beton pompa bomu yukarı doğru yükselip perona uzandı (2:01.0 · Clip 16).
          · DERS 79: Yerinde dökülen beton tabliyenin üstüne, gökyüzünden sarkan kancasız
            bir kabloyla bitmiş sarı korkuluklu ve kuleli monolitik beton blok indi (2:49.0 · Clip 22).
          · DERS 78: Yıkım bitmeden çatının sağ yarısına yeni ahşap kaplama konuldu; 2 klip sonra
            vinç bu yeni kaplamayı söküp çatıyı çıplak duvarlara geri geriletti (0:23.0–0:34.0 · Clip 3–5).
          · DERS 84: İki yaka arasına taşıyıcı halatlar çekilmeden sol avludan vinçle uydurma
            bir teleferik kabini kaldırıldı ve havada eriyerek yok oldu (4:32.0–4:37.0 · Clip 35).
DÖNÜŞÜ    kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §6 ·
          FIZIK_VE_AGIRLIK_KILAVUZU §Yük Yolu · INSAAT_YONTEMI_KILAVUZU §Aşama Sırası
KOŞU      Henüz koşulmadı · derin araştırma botuna yapıştırılacak
```

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, tam metin

Sen yapay zekâ video üretiminde fizik temelli kısıtlamalar (physics-informed neural networks, physical plausibility in video diffusion), yerçekimi ve yapısal temas mekaniği (ground reaction forces, contact constraints) ve inşaat mühendisliğinde montaj öncelik grafikleri (construction sequence DAG / precedence constraints) üzerine çalışan kıdemli bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat ve dönüşüm timelapse filmleri — sabit kamera, zaman atlamalı kesmeler ve iki anahtar kare arası I2V video üretimi.

Ölçülmüş arıza ve açık sorun şu: Yapay zekâ video modelleri arazi boşluklarını (voids, chasms, drops) ve yerçekimi/zemin temas kurallarını ihlal etmekte, imkânsız hayalet makineler ve gökyüzü kancaları türetmektedir:
1. **Boşluktan Yükselen Hayalet Makineler (Phantom Machinery Rising from Voids):** Dar uçurum kenarlarında veya kanyonlarda model platforma beton dökmek istediğinde, ön plandaki araç yetersiz gelince sağdaki dipsiz kanyon uçurumunun boşluğundan (altında hiçbir yol veya tekerlek olmaksızın) havaya doğru ikinci bir beton pompa bomu filizlendirip uzatmaktadır (2:01.0 · Clip 16 · DERS 81).
2. **Gökten İnen Monolitik Hazır Yapı (Sky-Hook Modular Superposition):** Yerinde dökülen beton tabliye devam ederken, model montaj fiilini ayrıştıramadığı için gökyüzünden görünmeyen bir vinç kablosuyla sarı korkuluklu, siyah çelik kuleli bitmiş dev bir monolitik beton bloğu mevcut döşemenin üstüne tek parça halinde kondurmaktadır (2:49.0 · Clip 22 · DERS 79).
3. **Prematüre Montaj ve Yıkım Gerilemesi (Premature Assembly & Regression):** Aşama sırası sıkı kilitlenmediğinde model yıkım sürerken yeni çatı kaplamasını erkenden bitirmekte; bir sonraki sahnede eski yapının sökümü emredildiğinde yeni yaptığı taze malzemeyi vinçle yıkarak inşaatı geriye sarmaktadır (0:23.0–0:34.0 · DERS 78).
4. **Önkoşulsuz Eleman Türemesi (Unconditional Element Spawning):** Teleferik hattının taşıyıcı çelik halatları gerilmeden ve rayları kurulmadan, model avludan vinçle yolcu kabini kaldırmakta, nereye takacağını bilemeyince kabin havada eriyip yok olmaktadır (4:32.0 · DERS 84).

Birinci görevin: Video difüzyon modellerinin yerçekimi, zemin desteği ve fiziksel temas kurallarını (ground support, structural continuity, gravity plausibility) modellemedeki zaafını açıkla — model neden uçurum boşluklarını zeminle eşdeğer kabul edip havada asılı araç parçaları ve bomlar türetir? Fizik temelli video üretiminde (physics-grounded video generation / VideoPhy benchmarkları) zemin temasının ve serbest boşlukların (negative void spaces) modellenmesindeki son gelişmeler nelerdir?

İkinci görevin: İnşaat montaj öncelik ilişkilerini (Assembly Precedence Graph / Topological Sort) üretken video modellerine dayatmanın yöntemlerini araştır — bir parçanın ancak temeli, taşıyıcısı veya yıkımı bittikten sonra sahneye girebilmesini sağlayan mantıksal kısıtlama yöntemleri (hierarchical conditioning, state-machine prompting, stage gating) nelerdir? Erken montajı ve modelin geriye doğru yıkım yapmasını engelleyen prompt ve I2V kilitleri nasıl kurulur?

Üçüncü görevin: Prompt seviyesinde "Boşluk Dokunulmazlığı (Void Immunity) ve Zemin Teması Zorunluluğu Sözdizimi" tasarla — kanyonlar, su yüzeyleri, uçurum kenarları ve açık hava için modelin asla bom, iskele veya makine türetmemesini garanti eden, her bomun yerde sabit tekerleklere/şasiye dayandığını şart koşan standart İngilizce prompt kuralları ve negatif kalkanları nelerdir?

Rapor Türkçe olsun, fizik, inşaat ve yapay zekâ terimleri İngilizce kalsın; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] akademik araştırma, benchmark veya resmi doküman · [İDDİA] literatür iddiası · [VARSAYIM] senin analizin), KAYNAK SINIFI (akademik · teknik rapor · endüstriyel doküman) ve ÇÖZÜMLENEBİLİR KAYNAK (arXiv ID, DOI, teknik rapor başlığı) ekle. Raporun sonunda:
(a) BOŞLUK VE ZEMİN DESTEĞİ İHLAL VE ÇÖZÜM TABLOSU (İhlal Türü · Fiziksel Neden · Prompt Çözümü · Negatif Kalkan),
(b) Uçurum ve boşluklu sahalar için standart İNGİLİZCE BOŞLUK KORUMA ŞABLONU (Void Immunity & Grounded Chassis Block),
(c) En fazla 10 maddelik YERÇEKİMİ VE MONTAJ SIRASI DENETİM LİSTESİ ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A38_<BOT>_HAM.md
2. DENETİM     SONUCLAR/A35-A38_DENETIM.md
3. KOD         VARSAYIMLAR.md A38 serisi
4. KILAVUZ     kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §6
5. KAPI        prompt_kontrol.py: boşluk kalkanı ve zemin teması zorunluluğu
```
