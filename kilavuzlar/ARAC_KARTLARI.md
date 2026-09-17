# 🔧 ARAÇ KARTLARI — elimdeki araç NE YAPIYOR

> Bu depoda beş film üretildi ve **araç kapısı hiçbirinde tam koşmadı.**
> Bedeli üç derste yazılı:
> · **DERS 32** — "the sun stays behind the camera" iki filmde tutmadı, güneş
>   diski üç klipte kadraja girdi, gölgeler klip içinde hiç dönmedi.
> · **DERS 33** — "no suited figure is present" yazıldı, teslim filmde net
>   astronotlar çıktı. Yasak, özne üretti.
> · **DERS 31** — plan 4-10 sn arası varyanslı ızgara yazdı; on klibin onu da
>   tam 6,0 sn çıktı ve ⑥ METRONOM dördüncü kez geldi.
>
> Üçünün ortak sebebi tek: **aracın ne yaptığını yazan tek bir kayıt yoktu.**
> Prompt düzeltildi durdu; araç hiç ölçülmedi.
>
> ⛔ **BU DOSYA BOŞ AÇILIR VE ELLE DOLDURULUR.**
> A7 raporu on bir aracın dördünde (Runway Gen-4 · Seedance · MiniMax/Hailuo ·
> Pika) her sütunda "BİLİNMİYOR" döndü, sorulan Gen-4 yerine Gen-3'ü anlattı ve
> verdiği sürüm tarihlerinin üçü çürük çıktı [A7-X1 · A7-X2]. Bu yüzden burada
> **doldurulmuş tek bir araç kartı yoktur.** Kart, ARACI KULLANAN kişi
> tarafından, ÜRETİM GÜNÜ, ölçerek doldurulur.
>
> Kaynak: `arastirma/SONUCLAR/A7_GEMINI_HAM.md` (denetim: `A5-A8_DENETIM.md`)

---

# 1. ⭐ KLİP SÜRELERİ KUTULUDUR — DERS 31'in gerçek sebebi

Bu, dört raporun tek en değerli bulgusudur ve ⑥ METRONOM'un suçunu araçtan alır.

```
Üretken video araçları SERBEST süre vermez. Süreyi önceden eğitilmiş
KUTULARA (bin) yuvarlar. Tipik kutu setleri:
      {4, 6, 8}        {5, 10}        {5, 9}
7,3 saniyelik bir istek en yakın kutuya yuvarlanır ya da reddedilir.

⭐ ON KLİBİN ONUNUN DA 6,0 ÇIKMASI BUNDANDIR. Prompt tutmadığı için değil,
   araç 6,0'ı bir KUTU olarak verdiği için.
```

**⭐ ÖLÇTÜM — ve plan yine de üretilebilirdi:**

```
plan  6·4·6·4·6·6·8·4·6·10  (toplam 60 sn · dört farklı süre)

{4,6,8} kutusuyla, kırpmasız:
   6←6  4←4  6←6  4←4  6←6  6←6  8←8  4←4  6←6  10←kutuya sığmıyor
   ⭐ DOKUZ SAHNE TAM OTURUYOR, atılacak 0 sn.

⇒ ⑥ METRONOM ARACIN DEĞİL KURGUNUN ARIZASIYDI [DERS 31 doğrulandı].
```

---

# 2. ⭐ ÜRETİM SÜRESİ ≠ TESLİM SÜRESİ — kırpma bütçesi

Üretilen klibin ilk ve son kareleri morfolojik olarak oynaktır: model bağlamı
oturtana kadar başta dalgalanır, sonda detay erir. Kurgu her iki uçtan
**10-15 kare** atar (30 fps'de uçta 0,33-0,50 sn, toplam **0,67-1,00 sn**).

```
⭐ KURAL:   ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn   → en yakın ÜST kutu

⭐ VE BUNUN SERT BİR SONUCU VAR — ölçtüm:
   TEK KLİPTE TESLİM EDİLEBİLECEK EN UZUN SAHNE = (en büyük kutu) − 1,00 sn
        {4,6,8} kutusu  →  7,00 sn
        {5,9}   kutusu  →  8,00 sn
        {5,10}  kutusu  →  9,00 sn

⛔ Yani {4,6,8} veren bir araçla plana 8 sn ya da 10 sn'lik sahne yazılamaz.
   Yazılacaksa ya uzatma (extension) ya iki klibin dikilmesi gerekir ve bu
   plana AÇIKÇA yazılır. Merdiven yazılmadan ÖNCE bu tavan bilinmelidir.

TESLİM   4,0   →  ÜRET  {4,6,8}: 6   {5,9}: 5   {5,10}: 5
TESLİM   6,0   →  ÜRET  {4,6,8}: 8   {5,9}: 9   {5,10}: 10
TESLİM   8,0   →  ÜRET  {4,6,8}: ⛔  {5,9}: 9   {5,10}: 10
TESLİM  10,0   →  ÜRET  {4,6,8}: ⛔  {5,9}: ⛔  {5,10}: ⛔
```

---

# 3. NEGATİF NEREYE YAZILIR — DERS 33'ün mekanizması

```
NEDEN "no suited figure" ASTRONOT ÜRETİR:
  "no" görsel karşılığı olmayan bir sözdizimi öğesidir. Metin kodlayıcıdan
  geçerken yanındaki İSİM ("suited figure") yüksek ağırlıklı bir vektöre
  dönüşür. Difüzyon o vektörü işler. Yasak, özneyi ÇAĞIRIR.

ÜÇ YER, ÜÇ SONUÇ:
  ① AYRI NEGATİF ALAN (varsa)   ⭐ EN İYİ. Negatif vektör pozitiften
     matematiksel olarak ÇIKARILIR (classifier-free guidance).
  ② METİN İÇİ "no ..." cümlesi   ⛔ EN KÖTÜ. Vektör çıkarılmaz, EKLENİR.
  ③ POZİTİF YENİDEN YAZIM        ⭐ ZORUNLU YEDEK. Ayrı alan yoksa tek yol.
        ⛔ "no workers are present"
        ✅ "the concrete deck is bare and swept, with tools stacked at the edge"

⛔ SAYI YOK: rapor "%85 sızma" dedi ama hiçbir çalışma adı vermedi [A7-X5].
   Mekanizma iner, oran inmez. Sızma oranı ARACIN KARTINDA ölçülür.

⭐ DEPO KURALI DEĞİŞMEDİ: negatif çekirdek yerinde kalır, ama her negatif
   maddenin bir POZİTİF karşılığı yazılır ve prompta o iner [DERS 11 · 33].
```

---

# 4. ⏱️ ARAÇ ÖLÇÜM YORDAMI — 30 dakikanın altında, tekrarlanabilir

```
GİRDİ    Tek prompt (§5) · AYNI prompt · 5 klip · farklı seed/koşu
         Beş klip, tekil bir üretimin şans payını ayıklamak içindir.

ÖLÇÜM 1 · SÜRE VE KUTU
   ffprobe -v error -show_entries format=duration -of csv=p=0 klip_*.mp4
   ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate \
           -of csv=p=0 klip_1.mp4
   → Beşi de aynı sayıysa araç KUTULUDUR. Kutu setini not et.
   ⛔ Izgara bu sayıdan yazılır [DERS 23 · D-d], plandan değil.

ÖLÇÜM 2 · KAMERA KİLİDİ
   ffmpeg -v error -y -i klip_1.mp4 -frames:v 1 ilk.png
   ffmpeg -v error -y -sseof -0.05 -i klip_1.mp4 -frames:v 1 son.png
   → İki kareyi üst üste koy. Sabit bir arka plan noktası kaç piksel kaydı?
   ⛔ > 2 px ise KAMERA KİLİDİ YOK. Bu araçla bu format üretilmez.
     Prompt düzeltilmez [DERS 23].

ÖLÇÜM 3 · GÖLGE DÖNÜYOR MU
   Aynı iki karede bir nesnenin gölge açısını ölç.
   ⛔ Fark 0° ise araç zamanı DONDURUYOR → bu araçla timelapse olmaz [DERS 32].
   ⭐ Fark varsa yönünü not et: klip boyunca aynı yöne mi dönüyor?

ÖLÇÜM 4 · NEGATİF SIZMASI
   Beş klipte de §5 promptunun yasakladığı figürü ARA. Kaç klipte çıktı?
   ⭐ Aynı testi ayrı negatif alanla tekrarla. Fark kartın "sızma" satırıdır.

ÖLÇÜM 5 · PROMPT TAVANI
   §5 promptunun EN SONUNDAKİ nesne ("orange safety flag") kaç klipte var?
   ⛔ Hiçbirinde yoksa metin sonu sessizce kesiliyor. Tavanı yarıya indirip
     tekrar koş.
   ⚠️ Bu bizim DERS 2'mizle (görsel prompt bandı 4.500-5.500 karakter)
      çelişebilir. Çelişirse KILAVUZ DEĞİŞMEZ, ARAÇ DEĞİŞİR [A7-X7].

ÖLÇÜM 6 · İLK KARE SADAKATİ (I2V)
   Onaylı bir kareyi I2V'ye ver, çıkan klibin ilk karesini geri al ve
   bash araclar/zincir_kontrol.sh <onayli> <ilk_kare>
   ⛔ Çıkış 2 ise araç zinciri taşımıyor demektir — §8 yöntemi bu araçta yürümez.

ÖLÇÜM 7 · UZUN KLİP
   En büyük kutuyu iste. Geliyor mu? Gelmiyorsa §2'deki sahne tavanı düşer.

⭐ ÖLÇÜM 8 · İKİ KAREYLE ÇALIŞIYOR MU — 08.09.2026, FORMATIN KENDİSİ
   [KILAVUZ_REHBERI §2.7 ④]
   Araca AYNI ANDA iki kare ver: ilk kare = onaylı G(n), son kare = onaylı
   G(n+1). Çıkan klibin SON karesini geri al ve karşılaştır:
     ffmpeg -v error -y -sseof -0.05 -i klip.mp4 -frames:v 1 son.png
     bash araclar/zincir_kontrol.sh G_n+1.png son.png
   ⛔ Araç ikinci kareyi ALMIYORSA ya da çıkış 2 ise BU FORMAT O ARAÇTA
     ÜRETİLMEZ. Plan tek kareli I2V'ye DÜŞÜRÜLMEZ — araç değiştirilir.
     Sebep: tek uçlu klipte dikişin öbür yakası serbesttir ve ⑤ beş filmde
     beş kez tam orada düştü.
   ⭐ Ölçüm 6 zincirin BAŞINI, ölçüm 8 SONUNU sınar. İkisi ayrı sorudur:
     araç ilk kareye sadık olup son kareyi hiç görmeyebilir.

⭐ ÖLÇÜM 9 · ÇÖZÜNÜRLÜK — yalnız KURGU YAKINLAŞMASI olan filmde  🆕 17.09.2026
   ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
           -of csv=p=0 klip_1.mp4
   → Yakınlaşma tavanı = kaynak genişliği / teslim genişliği.
     Sayılar ve gerekçe: kilavuzlar/KAMERA_HAREKETI_KILAVUZU.md §3.3
   ⛔ Büyütme (upscale) bu tavanı SAĞLAMAZ; ölçüm aracın GERÇEKTEN verdiği
     piksele bakar.
   ⛔ Araç tavanı vermiyorsa PLANDAKİ YAKINLAŞMA TABLOSU YENİDEN YAZILIR —
     prompt zorlanmaz, tavan düşürülür.
   ⚠️ Yakınlaşma olmayan filmde bu ölçüm atlanır; kart satırı "uygulanmaz" yazar.
```

---

# 5. TEST KLİBİ PROMPTU — birebir kullanılır

> Bu prompt kasten tuzaklıdır: metin içi negatif taşır (ÖLÇÜM 4), en sona
> küçük bir nesne saklar (ÖLÇÜM 5), kamera kilidi ve gölge iddiası içerir
> (ÖLÇÜM 2 · 3). Değiştirme — değiştirilirse ölçümler karşılaştırılamaz.

```
A locked-off static camera looks at a half-built concrete tower on a bare
earth site from forty metres away, vertical 9:16 framing, no camera movement
of any kind. The sun sits high behind the camera and the tower shadow falls
away from the lens across the open ground. No suited figure, no worker and no
vehicle is present anywhere on the site. The concrete surfaces are dry and
matte, the ground is compacted dirt with old tire ruts, and a thin haze of
dust hangs low over the pad. About two hours pass across this shot: the tower
shadow sweeps across the ground and thin clouds stretch into long streaks.
At the very top of the structure, a small bright orange safety flag is tied to
a piece of exposed rebar and flutters steadily in the wind.
```

```
AYRI NEGATİF ALAN VARSA (ölçüm 4'ün ikinci koşusu için):
   moving camera, pan, zoom, tilt, dolly, person, worker, suited figure,
   astronaut, vehicle, text, watermark, logo
```

---

# 6. ARAÇ KARTI ŞABLONU — ⛔ boş, elle doldurulur

```
┌─────────────────────────────────────────────────────────────────────────┐
│ ARAÇ              [ad]                                                  │
│ SÜRÜM / MOD       [arayüzde ne yazıyorsa birebir]                       │
│ ÖLÇÜM TARİHİ      [üretim günü — ⛔ rapordan alınmaz, A7-X2]            │
│ ÖLÇEN             [kim]                                                 │
├─────────────────────────────────────────────────────────────────────────┤
│ ① KUTU SETİ       [ffprobe: ____ / ____ / ____ sn]  beş klip aynı mı: __│
│    SAHNE TAVANI   (en büyük kutu − 1,00) = ____ sn      [§2]            │
│ ② KAMERA KAYMASI  [____ px]   kilit var mı: evet/hayır                  │
│    GEOMETRİ KANALI [static mode · start/end frame · yok]                │
│ ③ GÖLGE DÖNÜŞÜ    [____°]  yön tutarlı mı: evet/hayır                   │
│ ④ NEGATİF ALANI   [ayrı alan var / yok]                                 │
│    SIZMA          metin içi: __/5 klip · ayrı alan: __/5 klip           │
│ ⑤ PROMPT TAVANI   [____ karakter]  son nesne göründü mü: __/5           │
│ ⑥ İLK KARE (I2V)  zincir_kontrol çıkışı: ____                           │
│ ⑦ EN BÜYÜK KUTU   isteniyor mu / geliyor mu: __                         │
│ ⑧ İKİ KAREYLE     ilk+son kare alınıyor mu: evet/hayır  ⭐ FORMAT KAPISI │
│    ÇALIŞIYOR MU   son kare zincir_kontrol çıkışı: ____   [§2.7 ④]       │
├─────────────────────────────────────────────────────────────────────────┤
│ BİLİNEN TUZAK     [bu araçla yaşanan somut arıza — tek cümle]           │
│ KARAR             ⭐ BU FORMAT ÜRETİLİR / ⛔ ÜRETİLMEZ — sebep:         │
└─────────────────────────────────────────────────────────────────────────┘
```

```
┌── KART 1 ── ⛔ BOŞ ── ilk üretimde doldurulacak ──┐
└──────────────────────────────────────────────────┘
┌── KART 2 ── ⛔ BOŞ ──────────────────────────────┐
└──────────────────────────────────────────────────┘
┌── KART 3 ── ⛔ BOŞ ──────────────────────────────┐
└──────────────────────────────────────────────────┘
```

---

# 7. KAPI

```
① ÜRETİMDEN     ⛔ Araç kapısı SEKİZ ölçümle koşar (§4), üçle değil.
                   ⭐ ⑧ formatın kendisidir: iki kareyle çalışmayan araçta
                     İKİ KEYFRAME ZİNCİRİ yürümez [KILAVUZ_REHBERI §2.7].
   ÖNCE            Sonuç üretim günlüğünün §0 bloğuna YAZILIR [DERS 28].
                   ⛔ Kart doldurulmadan tek kare üretilmez.

② PLANDAN       ⛔ Aşama merdiveninin SÜRE sütunu, ölçülen KUTU SETİNDEN
   ÖNCE            türetilir [DERS 23 · D-d]. Sahne tavanı (§2) aşılamaz.

③ KURGUDA       ⛔ Kırpma bütçesi uygulanır ve ZİNCİRLİ FORMATTA
                   ASİMETRİKTİR: pay BAŞTAN alınır, sondan alınmaz — son
                   kare hedeftir → KURGU_VE_TESLIM_KILAVUZU §2.

④ QA'DA         ⑥ GEÇİŞ merceği düz ızgara bulursa artık iki cevap var:
                   kutu setine bakılır — plan üretilebilir miydi?
                   Üretilebiliyorduysa kusur KURGUDADIR.
```

> ⭐ **KALDIRDIĞI:** "önce planı yazalım, aracı sonra buluruz" sırasını
> kaldırır. Artık araç kartı plandan önce gelir ve süre ızgarasını o belirler.
> Bedeli: yeni bir araca geçmek 30 dakikalık ölçüm borcu doğurur.
> Karşılığı: dört filmde tekrarlanan üç arızanın üçü de üretim başlamadan
> yakalanır.
