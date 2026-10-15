# 🧪 A41 — SÖKÜM/MONTAJ KADEMELENDİRMESİ VE GÖZLE GÖRÜLÜR İŞ ARTIŞI (TANGIBLE WORK INTENSITY)

```
AMAÇ      Restorasyon ve dönüşüm projelerinde söküm/yıkım (demolition) fazı ile yeni montaj (assembly)
          fazının birbirine karışmasını, taze yapılan imalatın sökülüp tekrar yapılmasını engellemek;
          her 8 saniyelik sahnede izleyicinin gözüyle açıkça seçebileceği geri dönülmez, ölçülebilir
          bir iş artışı (tangible work volume) ve yüksek şantiye iş yoğunluğu (work intensity)
          üretme kurallarını belirlemek.
KARŞILIĞI THE SKY STATION ve dönüşüm filmlerinde yaşanan faz karmaşası:
          · DERS 78: Yıkım henüz bitmemişken çatının yarısının yeni sacla kaplanması, sonraki
            sahnede eski ahşapların sökülmesi emredildiğinde yeni sacların da sökülüp geri sarılması.
          · Bazı sahnelerde hiçbir yapısal ilerleme olmaması, işçilerin boş el arabalarıyla amaçsız
            yürümesi ("stagnant clip"), sonraki sahnede ise aniden devasa bir kütlenin belirmesi
            şeklindeki dengesiz iş dağılımı.
DÖNÜŞÜ    kilavuzlar/INSAAT_YONTEMI_KILAVUZU.md §Faz Ayrımı & §İş Yoğunluğu ·
          kilavuzlar/SANTIYE_HAREKETI_KILAVUZU.md §4.8 İş Yoğunluğu ·
          PROMPT_SABLONU §Tangible Work Progress
KOŞU      Henüz koşulmadı · derin araştırma botuna yapıştırılacak
```

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, tam metin

Sen inşaat mühendisliği süreç planlaması (construction phasing, work breakdown structure - WBS), üretken video difüzyon modelleri (video diffusion models, DiT) ve kurgusal zaman atlamalı görsel tempo yönetimi üzerine çalışan kıdemli bir araştırmacısın; benim ürünüm konuşmasız, iki anahtar kare arası (I2V) üretilen, kilitli sabit kamerada fotogerçekçi inşaat ve restorasyon timelapse filmleridir.

Açık sorun şudur:
Özellikle eski bir yapının restore edildiği veya dönüştürüldüğü filmlerde iki büyük yapısal arıza yaşanmaktadır:
1. **Faz Çakışması ve Geriye Yıkım:** Model, eski yapının sökümü (dismantling of rusted corrugated sheets and rotten rafters) ile yeni yapının inşasını (installing new steel purlins and standing-seam panels) aynı sahnede ya da ardışık kontrolsüz sahnelerde çakıştırmaktadır. Yıkım sahası henüz temizlenmeden yeni kaplama başlatılmakta; izleyen sahnede harabenin kalan kısımları sökülürken model zamanı tersine çevirerek yeni yaptığı kaplamaları da yıkmaktadır (DERS 78). Söküm fazı ile yapım fazı arasındaki termodinamik ve kronolojik duvar kurulamamaktadır.
2. **Gözle Görülür İş Artışı Eksikliği ve Dengesiz Tempo:** Bazı 8 saniyelik sahnelerde yapıda hiçbir kalıcı fiziksel ilerleme olmamakta; işçiler sadece moloz taşımakta veya araçlar rölantide dönmektedir (sıfır yapısal hacim artışı / stagnant clip). Hemen ardından gelen sahnede ise tek bir anda çatının %50'si aniden belirmekte (step-jump); izleyici inşaat emeğinin organik akışını görememektedir. Her sahnenin kendine ait net, ölçülebilir bir "iş hacmi artışı" (tangible structural delta) ve yüksek şantiye iş yoğunluğu (≥3 aktif el, görünür malzeme akışı, hazırlık adımları) taşıması zorunludur.

Birinci görevin: Üretken video difüzyon modellerinin restorasyon sahnelerinde yıkım ve yapım eylemlerini birbiriyle karıştırmasının matematiksel ve mimari nedenlerini açıkla.
- Difüzyon modellerinde "negatif eylem" (söküm, moloz kaldırma, eksilme) ile "pozitif eylem" (montaj, ekleme, hacim artışı) arasındaki dikkat ayrımı (attention separation) neden çöker?
- Söküm fazı (Demolition Phase) ile Yapım fazı (Construction Phase) arasına kesin bir kronolojik sınır kapısı (irreversible phase gate) nasıl yerleştirilir?

İkinci görevin: İnşaat timelapse projelerinde her sahnede gözle görülür, tatmin edici ve dengeli bir iş artışı (tangible work volume) sağlamak için literatürde ve endüstride uygulanan eylem dağılım mimarilerini karşılaştır.
- Kaba inşaattan ince işçiliğe kadar yapım adımları 8 saniyelik klip dilimlerine (work packages) nasıl homojen ve geri dönülmez olarak bölünür?
- Sahnede "boş rölanti" oluşmasını engelleyen ve izleyiciye sürekli bir inşaat devinimi hissettiren şantiye iş yoğunluğu bileşenleri (malzeme lojistiği $\to$ taşıyıcı hazırlığı $\to$ nihai montaj) nasıl kurgulanır?

Üçüncü görevin: Yalnızca metin istemi (positive prompt), negatif prompt ve iki anahtar kare zinciri kullanarak uygulanabilecek standart İngilizce **SÖKÜM-YAPIM FAZ KAPILAMASI VE GÖZLE GÖRÜLÜR İŞ ARTIŞI SÖZDİZİMİ (Demolition-to-Assembly Gating & Tangible Progress Syntax)** tasarla.
- Söküm devam ederken taze malzeme montajını %100 engelleyen (`STRICT DEMOLITION PHASE ONLY: ZERO NEW MATERIAL INSTALLATION`),
- Yapım fazına geçildiğinde ise yıkım fiillerini yasaklayıp her sahnede net bir yapısal eleman artışını garanti eden (`ADDITIVE ASSEMBLY PHASE ONLY: NET POSITIVE STRUCTURAL GAIN`) standart prompt ve negatif blokları nasıl yazılır?

Rapor Türkçe olsun, yapay zekâ, mühendislik ve difüzyon terimleri İngilizce kalsın; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] akademik deney, benchmark veya resmi doküman · [İDDİA] literatürde iddia edilmiş kanıtlanmamış · [VARSAYIM] çıkarım), KAYNAK SINIFI (akademik makale/arXiv · platform/araç teknik dokümanı · endüstriyel vaka analizi) ve ÇÖZÜMLENEBİLİR KAYNAK (DOI, arXiv ID, URL, tarihli sürüm notu) ekle. Raporun sonunda:
(a) Bir SÖKÜM VE MONTAJ FAZ MATRİSİ (Faz adı · İzin verilen eylem ve malzeme · Kesinlikle yasaklanan eylem · Klip başına gözle görülür iş kriteri),
(b) Standart İngilizce FAZ KAPISI VE İŞ ARTIŞI ŞABLONU (Phase Gating & Tangible Progress Block),
(c) En fazla 10 maddelik bir İŞ ARTIŞI VE FAZ DENETİM LİSTESİ (Checklist) ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A41_<BOT>_HAM.md
2. DENETİM     SONUCLAR/A39-A42_DENETIM.md
3. KOD         VARSAYIMLAR.md A41 serisi
4. KILAVUZ     kilavuzlar/INSAAT_YONTEMI_KILAVUZU.md §Faz Ayrımı &
               kilavuzlar/SANTIYE_HAREKETI_KILAVUZU.md §İş Yoğunluğu
5. KAPI        prompt_kontrol.py: faz çakışması ve görünür iş artışı denetimi
```
