# 🧪 A39 — MONOTONİK İLERLEME VE ARA HÂL AŞIMI (OVERSHOOT & YO-YO ASSEMBLY)

```
AMAÇ      İki anahtar kare (Frame A ve Frame B) arasında belirli bir ara hâl (%25, %50 vb.)
          hedeflendiğinde, video difüzyon modelinin klip ortasında tüm yapıyı (%100) erkenden bitirip
          ardından Frame B'ye oturmak için yapılan kısımları geri sökmesi / eritmesi ("yo-yo construction",
          "elastic rebound", "premature overshoot") arızasını engellemek; inşaat ilerleme hızını
          zamana göre kesin monotonik (dC/dt >= 0) ve tavan kısıtlı (progress bounded) kılacak
          matematiksel/prompt mimarisini belirlemek.
KARŞILIĞI 15.10.2026 THE SKY STATION ve timelapse üretimleri saha gerçeği:
          · Sahnede çatının çeyreği (%25) hedeflenirken modelin klibin 4. saniyesinde çatının
            tamamını kaplaması, 4–8 saniye arasında ise Frame B'deki %25'lik hedef sınıra
            dönebilmek için yeni yapılan kiremit ve kaplamaları havada eriterek geriye sökmesi.
          · İzleyen sahnede (%25 → %50) modelin aynı prematüre aşımı tekrarlayıp yapıyı tekrar
            yo-yo gibi bozup yapması; sahneler arası fiziksel güvenilirliğin çökmesi.
DÖNÜŞÜ    kilavuzlar/INSAAT_YONTEMI_KILAVUZU.md §Ara Hâl Tavanı ·
          PROMPT_SABLONU §Monotonic Progress Lock · prompt_kontrol.py §Monotonic Assembly Check
KOŞU      Henüz koşulmadı · derin araştırma botuna yapıştırılacak
```

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, tam metin

Sen üretken yapay zekâ (video diffusion models, Image-to-Video - I2V, Diffusion Transformers - DiT), zamansal gürültü giderme dinamikleri (temporal latent interpolation, trajectory optimization) ve inşaat simülasyonu üzerine çalışan kıdemli bir yapay zekâ araştırmacısısın; benim ürünüm konuşmasız, iki anahtar kare (Keyframe A ve Keyframe B) arasında üretilen, kameranın sabit tripodda kilitli kaldığı fotogerçekçi inşaat ve dönüşüm timelapse filmleridir (her klip 8,0 saniye sürmekte ve kesintisiz iki kare zinciriyle ilerlemektedir).

Yaşanan ağır üretim ve fizik arızası şudur:
Bir sahnede (örneğin 8 saniyelik bir I2V klibinde), başlangıç karesi (Frame A) çatının %0 yapılmış halini, bitiş karesi (Frame B) ise çatının tam %25'inin tamamlandığı ara hâli (partial state) göstermektedir. Ancak difüzyon modeli zamansal interpolasyon yaparken inşaat sürecini doğrusal veya kademeli işletememektedir. Klip başladığında (0–4. saniyeler arasında) model kontrolsüz bir tamamlama dürtüsüyle çatının neredeyse %100'ünü inşa etmekte; fakat 8. saniyedeki Frame B koşuluna (conditioning) yetişmek zorunda olduğu için klibin ikinci yarısında (4–8. saniyeler arasında) yeni yaptığı çatı kaplamasını, aşıklarını ve kiremitlerini geriye doğru sökerek/eriterek %25 seviyesine geri çekmektedir ("yo-yo assembly / elastic rebound / premature overshoot"). Bir sonraki klipte (%25'ten %50'ye geçişte) model aynı hatayı tekrarlamakta; klibin ortasında çatıyı yine %100 bitirip klibin sonunda %50'ye geri yıkmaktadır. Bu durum izleyicide yapay zekâ illüzyonunu açığa çıkarmakta ve fiziksel montaj inandırıcılığını tamamen yok etmektedir.

Birinci görevin: Video difüzyon modellerinin (DiT, Wan2.1, HunyuanVideo, CogVideoX, LTX-Video, Sora/Gen-3 mimarileri) iki anahtar kare arası latent gürültü giderme (denoising trajectory) sürecinde neden böyle bir "erken tamamlama ve ardından geri sökülme / elastik geri tepme" (premature overshoot & elastic rebound) ürettiğini matematiksel ve mimari olarak açıkla.
- Difüzyon zaman adımlarındaki ($t$) uzamsal-zamansal dikkat (spatiotemporal attention) ve gürültü tahmin kaybı neden monotonik artışı ($\frac{dC}{dt} \ge 0$) koruyamaz?
- Hedef anahtar kare koşullandırması (end-frame guidance / trajectory anchoring) neden klibin orta noktalarında gevşeyerek aşırı üretime (overshoot) izin verir?

İkinci görevin: Literatürde ve endüstriyel video üretim hatlarında (2024–2026) bu ara hâl aşımını ve yo-yo montajını engelleyen teknikleri (Monotonic Progress Constraints, Trajectory Boundary Enforcement, Velocity Bounding, Monotonic Attention Guidance, Paced Denoising) karşılaştır.
- Modelin orta karelerde bitiş karesindeki yapısal hacmi ($V_{\text{target}}$) aşmasını fiziksel veya latent seviyede engelleyen yöntemler nelerdir?
- Diferansiyellenebilir monotonluk cezaları (monotonicity loss penalties) veya hız kısıtlamaları (assembly velocity clamps) video transformatörlerine nasıl uygulanır?

Üçüncü görevin: Yalnızca metin istemi (positive prompt), negatif prompt ve iki anahtar kare girdisi kullanılarak modelin "asla hedef kareden fazlasını inşa etmemesini" ve "yapılan işin asla geriye sökülmemesini" sağlayan standart İngilizce **MONOTONİK İLERLEME VE TAVAN SÖZDİZİMİ (Monotonic Progress & Upper-Bound Constraint Syntax)** tasarla.
- Prompt seviyesinde "%25 tamamlanma tavanı" (strict 25% upper bound ceiling), "geri dönüşsüz doğrusal montaj" (irreversible monotonic progression) ve "aşırı inşa yasağı" (zero premature completion) nasıl formüle edilir?
- Modelin klibin 4. saniyesinde %100'e fırlamasını durduran mikro-eylem ve malzeme sınırlama kalıpları nelerdir?

Rapor Türkçe olsun, yapay zekâ, difüzyon ve bilgisayarlı görü terimleri İngilizce kalsın; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] akademik deney, benchmark veya resmi doküman · [İDDİA] literatürde iddia edilmiş kanıtlanmamış · [VARSAYIM] çıkarım), KAYNAK SINIFI (akademik makale/arXiv · platform/araç teknik dokümanı · endüstriyel vaka analizi) ve ÇÖZÜMLENEBİLİR KAYNAK (DOI, arXiv ID, URL, tarihli sürüm notu) ekle. Raporun sonunda:
(a) Bir ARA HÂL VE MONOTONİK İLERLEME TABLOSU (Aşama hedefi · Tipik model arızası / Yo-Yo mekanizması · Çözüm kısıtı · İlerleme hız formülü),
(b) Standart İngilizce MONOTONİK İLERLEME VE TAVAN KİLİDİ ŞABLONU (Monotonic Assembly Lock Block),
(c) En fazla 10 maddelik bir ARA HÂL AŞIMI ÖNLEME KONTROL LİSTESİ (Checklist) ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A39_<BOT>_HAM.md
2. DENETİM     SONUCLAR/A39-A42_DENETIM.md
3. KOD         VARSAYIMLAR.md A39 serisi
4. KILAVUZ     kilavuzlar/INSAAT_YONTEMI_KILAVUZU.md §Monotonik İlerleme &
               kilavuzlar/MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md §Ara Hâl
5. KAPI        prompt_kontrol.py: ara hâl tavanı ve monotonluk sözdizimi denetimi
```
