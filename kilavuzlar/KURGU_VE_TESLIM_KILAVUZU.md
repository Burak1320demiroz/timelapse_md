# 🎬 KURGU VE TESLİM KILAVUZU — planı dosyaya kesmek ve kanıtlamak

> THE LONG DAY planı klip sürelerini **6-4-6-4-6-6-8-4-6-10** yazdı; kurgu on
> klibi de **6,0 saniyede düz kesti** ve ⑥ **METRONOM dördüncü kez** geldi
> [DERS 31]. Beş ayrı mercek son karttaki görüntünün filmden farklı olduğunu
> yazdı. Kapak, S9'un karesinden türemedi [DERS 30]. Açılıştaki müziksiz
> pencere ve ses yüksekliği hiç ölçülmedi.
>
> Hepsi tek bir boşluktan geçti: **teslim dosyasını planla karşılaştıran bir
> adım yoktu.** Süre sütunu yalnız planda yaşıyordu.
>
> ⭐ Bu kılavuz o adımı kurar ve **kanıtın kendisini ölçer.**
> Aşağıdaki her komut bu makinede (ffmpeg 8.1) koşturuldu; koşmayan iki
> komut düzeltildi, kalibre edilmemiş eşik ölçülerek değiştirildi.
>
> Kaynak: `arastirma/SONUCLAR/A8_GEMINI_HAM.md` (denetim: `A5-A8_DENETIM.md`)

---

# 1. SIRA — kurgu üç adımdır, biri atlanırsa teslim yok

```
1. KIRPMA      her klibin baş ve sonundan kare atılır          §2
2. KESME       kırpılmış klipler planın SÜRE sütununa göre dizilir  §3
3. KANIT       teslim dosyası ÖLÇÜLÜR, plana karşı okunur      §5 · §6
⛔ 3 koşmadan yayın yok. Dört filmde de 3 hiç koşmadı.
```

---

# 2. KIRPMA — üretim süresi teslim süresi değildir

Üretilen klibin uçları oynaktır: başta model bağlamı oturtana kadar dalgalanır,
sonda detay erir ve halüsinasyon artar.

```
⛔ 08.09.2026 — ZİNCİRLİ FORMATTA KIRPMA ASİMETRİKTİR [KILAVUZ_REHBERI §2.7 ③]
   Klibin SON karesi artık bir HEDEFTİR: G(n+1), hem bu klibin sonu hem
   sonraki klibin başıdır. Sondan kare atmak DİKİŞİ ATMAKTIR ve formatın
   bütün kazancını götürür.
   ⭐ HER KLİPTEN: baştan 25-30 kare · sondan 0-5 kare
      30 fps'de toplam yine ~1,00 sn ⇒ ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn
   ⚠️ A7-b'nin "sonda detay erir" bulgusu SERBEST UÇLU klip içindir; son karesi
      kilitli bir klipte o uç zaten hedefe bağlıdır. Bu bir VARSAYIMDIR ve
      ölçülür: her klibin son 5 karesi ile hedef görsel arasındaki
      zincir_kontrol çıktısı üretim günlüğüne yazılır.

⛔ BU YÜZDEN 6,0 SN TESLİM İÇİN 6,0 SN ÜRETİLMEZ.
   {4,6,8} kutulu araçta 8 sn üretilir, 6,0'a kırpılır.

kırpma komutu (kare hassasiyetinde, yeniden kodlayarak):
   ffmpeg -y -i uretim_S3.mp4 -vf "trim=start_frame=30:end_frame=210,setpts=PTS-STARTPTS" \
          -an -c:v libx264 -crf 16 -pix_fmt yuv420p kirpik_S3.mp4
   (30 = baştan atılan kare · 210 = 30 + 180 → 6,0 sn @30fps · sondan 0 kare)
```

```
⛔ ZİNCİRLE ÇATIŞMA VE ÇÖZÜMÜ [A8 ↔ depo · Ç3]
   Klibin İLK KARESİ zincirin çapasıdır [§8 · DERS 25]. Baştan kare atmak
   teslim dosyasındaki dikişi çapadan uzaklaştırır.
   ⚠️ ZİNCİRLİ FORMATTA BU ÇATIŞMA BÜYÜR: baştan 30 kare atılınca dikişin
      İLK yakası 1,00 sn ilerideki bir kareye kayar, SON yakası ise hedefte
      durur. Kesme yine sıçramasızdır (aynı klibin içi), ama G(n) karesi
      teslimde tam olarak görünmez — kanıtı ÜRETİLEN klipten alınır.
   ⭐ ÇÖZÜM: zincir kanıtı ÜRETİLEN klibin ilk karesinden alınır (üretim anında,
     zincir_kontrol.sh ile). Kapak ve final kare kanıtı ise HER ZAMAN TESLİM
     dosyasından alınır. İki kanıt iki ayrı dosyadan okunur ve bu bilinçlidir.
```

---

## ⭐ 2.4 VARYANS ⑥'YI KURTARMAZ — ÖNCE ⑤ OKUNUR  [DERS 44]

```
DERS 13 ve 31: hız kesme SIKLIĞI değil kesme VARYANSIDIR. THE DUST YEAR'ın
ızgarası düz DEĞİLDİ — teslimde bile 6·8·4·4·6·4·10·4·6·10, dört farklı süre,
2,5 kat aralık. Hüküm yine METRONOM — BEŞİNCİ KEZ.
⑥'nın gerekçesi süreleri HİÇ ANMIYOR:
   "largely due to the failure of anchor survival across the seams … the
    edits read as a slideshow"

KURAL  Süre varyansı ⑥'nın GEREK şartıdır, YETER şartı değil. Kesmenin
       "sonraki" değil "sonra" demesi için dikişin İKİ YAKASINDA aynı
       dünyanın durması gerekir.
⭐ OKUMA SIRASI ÖLÇÜLDÜ — ⑥ ⑤'İN ALTINDADIR:
   ⑤ hükmü "A SET REBUILT EACH TIME" ise ⑥ METRONOM hükmü IZGARAYA YAZILMAZ.
   Sebep ⑤'tir. kesme_kontrol.sh ızgarayı doğrulasa bile bu böyledir.
⛔ Düz ızgara yasağı KALKMAZ; varyans hâlâ gereklidir — tek başına yetmiyor.
```

# 3. KESME YERİ — nereye düşer

Bizim formatta her kesme bir AY atlar; iki klip aynı anın devamı değildir.
Bu yüzden "harekete kesme" (cutting on action) burada işe yaramaz — kesilen
hareket öbür tarafta yoktur.

```
⭐ BİZİM KURALIMIZ: DURUŞA KES (resting cut).
   Kesme, giden klipte mikro hareketin (vinç bomu, araç, platform) en sakin
   olduğu ana düşer. Gelen klip de sakin bir andan açılır.
   Sebep: aynı sabit kadrajda iki farklı ayı yan yana koyuyoruz. Kesme
   noktasında hareket ne kadar sakinse, izleyicinin gözü YAPI'daki farka
   o kadar kolay gider — arıza sanmaz, zaman sanar.

⚠️ ⑥ METRONOM ile karıştırma [DERS 13 · 24]: hız kesme SIKLIĞI değil kesme
   VARYANSIDIR. Duruşa kesmek varyansı azaltmaz — kesme YERİNİ seçer,
   kesme SÜRESİNİ değil. Süre planın SÜRE sütunundan gelir ve değişmez.
```

**DİKİŞ EŞLEME** — aynı istasyondan gelen iki klip arasında:

```
① GEOMETRİ   yalnız X/Y ötelemesi. ⛔ Rotasyon ve zoom KAPALI —
             açılırsa kamera istasyonu değişmez'i düşer.
② FOTOMETRİ  iki klibin temas karelerinde siyah seviyesi · orta ton · beyaz
             seviyesi eşlenir. Gökyüzü rengi kesmede sıçramamalıdır.
③ ÖLÇÜM      ffmpeg -v error -i teslim.mp4 \
               -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF:file=ydif.txt" -f null -
             ⛔ Raporun verdiği hâli (yalnız -vf signalstats) HİÇBİR ŞEY
                BASMIYOR — ölçtüm, eşleşen satır sayısı 0 [A8-X1].
```

---

# 4. TESLİM ŞARTNAMESİ — çelişkiler ortalanmadan

```
KESİN (üç platformda da aynı)
   çözünürlük     1080 × 1920 · 9:16       ⛔ tek piksel sapma letterbox üretir
   kodek          H.264 · MP4
   renk           Rec.709
   gerçek tepe    −1,0 dBTP

⚠️ ÇELİŞKİLİ — ORTALAMA ALINMADI [kart S §4]
   SES LUFS       kaynak A: −14 LUFS        kaynak B: −12 … −10 LUFS
                  ⭐ DEPO KARARI: −14 LUFS yerinde kalır (kart Y §4'te yazılı,
                     dört filmde kullanıldı). Çelişki BİLİNİYOR ve kayıtlı.
   GAMMA          2,2 mi 2,4 mü — BİLİNMİYOR. Rec.709 yazılır, gamma zorlanmaz.
   DOSYA BOYUTU   kaynaklar 72 MB ile 15 GB arasında çelişiyor — BİLİNMİYOR.
                  Pratikte anlamsız: 60 sn 1080p ~10-15 Mbps = 75-110 MB.

⛔ KILAVUZA İNMEYENLER — kaynaksız sayılar [A8-X4 · A8-X5]
   "%18,7 tekrar izlenme artışı"        → çalışma adı yok, düştü
   "son kart 2-3 sn ideal, 5 sn öldürür" → kaynak yok; bizim kart 5,0 sn ve
     DEĞİŞMEDİ. Yayından sonra kanalın kendi tutunma eğrisiyle ölçülür [A1-a].
   "Instagram ızgarası 1:1 kırpar"       → doğrulanmadı, güvenli alan buna
     göre daraltılmaz [A8-X6].
```

---

# 5. ⭐⭐ KESME KANITI — eşik değil, TOP-N

Bu bölüm bu deponun en somut düzeltmesidir.

```
⛔ ESKİ HÂL KÖRDÜ. Ölçtüm:
   Sabit kadraj + aynı yapı + yalnız aşama ilerleyen 10 klipli sentetik
   teslimde (plan ızgarası 6·4·6·4·6·6·8·4·6·10, kesmeler 6/10/16/20/26/32/
   40/44/50 sn):
        eşik 0,40 (A8'in önerdiği)          →  0 kesme buldu
        eşik 0,30 (kesme_kontrol.sh'nin)    →  0 kesme buldu
        eşik 0,20 · 0,10 · 0,05             →  0 kesme buldu
   Kare kare gerçek dağılım:
        KESME karelerinde scene_score   0,01629 – 0,02217
        KLİP İÇİ en yüksek scene_score  0,00538   (ortanca 0,00006)
   ⇒ Ayrım VAR (3 kat marj) ama eşik 15-25 KAT fazla yazılmıştı.
   ⛔ Yani ⑥ METRONOM kapısı açık sanılıyordu; KAPALIYDI.

⭐ YENİ HÂL: EŞİK YOK. Plandaki kesme sayısı kadar EN YÜKSEK skoru al ve
   zaman damgalarını planla karşılaştır. Mutlak skor ölçeğinden bağımsızdır.
   Sentetikte 9 kesmenin 9'unu da ±0,05 sn içinde buldu — TAM İSABET.

⭐ İKİNCİ BAĞIMSIZ DEDEKTÖR: YDIF.
   kesmelerde 1,66 – 2,26 · klip içi en yüksek 0,54. O da temiz ayırıyor.
   İki dedektör aynı kesmeleri bulmuyorsa kurgu incelenir.
```

```
KOŞ:  bash araclar/kesme_kontrol.sh teslim.mp4 <plan.md>
      (betik artık top-N ile çalışır; eşik parametresi yalnız
       "hepsini göster" kipi içindir)
```

---

# 6. YAYIN ÖNCESİ QC — sırayla, hepsi koşturuldu

> ⛔ Yedisi de koşmadan yayın yok. Sonuçlar üretim günlüğü §4'e yazılır.

```
① BİÇİM
   ffprobe -v error -select_streams v:0 \
     -show_entries stream=width,height,r_frame_rate,codec_name -of csv=p=0 teslim.mp4
   BEKLENEN: 1080,1920,30/1,h264          TOLERANS: sıfır
   ✅ koşturuldu

② SÜRE
   ffprobe -v error -show_entries format=duration \
     -of default=noprint_wrappers=1:nokey=1 teslim.mp4
   BEKLENEN: sahne bloğu + kapak kartı 5,0 sn      TOLERANS: ±1 kare
   ✅ koşturuldu → 60.000000

③ KESME KANITI  ⭐ [DERS 31]
   bash araclar/kesme_kontrol.sh teslim.mp4 <plan.md>
   BEKLENEN: çıkış 0                      TOLERANS: kesme başına ±0,25 sn
   ⛔ Çıkış 1 ise kurgu SÜRE sütunundan YENİDEN KESİLİR.

④ SES YÜKSEKLİĞİ
   ffmpeg -i teslim.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -A8 "Summary"
   BEKLENEN: I ≈ −14 LUFS · Peak ≤ −1,0 dBFS      TOLERANS: ±0,5 LUFS
   ⚠️ "I:" satırı Summary BLOĞUNDADIR; `tail` ile kaçar. `grep -A8 Summary` kullan.
   ✅ koşturuldu → I: −22.0 LUFS (test dosyası)

⑤ AÇILIŞ PENCERESİ
   ffmpeg -v error -i teslim.mp4 -t 2 -af ebur128 -f null - 2>&1 | tail -3
   BEKLENEN: müziksiz pencere plana uygun (bizde 0,0-1,5 sn)
   ⛔ Plan sessizlik yazmışsa ve ses varsa, ya da tersi → düzelt.

⑥ TİTREME (FLICKER)
   ffmpeg -v error -i teslim.mp4 \
     -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF:file=ydif.txt" -f null -
   BEKLENEN: kesme dışındaki karelerde YDIF sıçraması yok
   ⛔ Raporun komutu (yalnız -vf signalstats) çalışmıyor — ölçtüm [A8-X1].
   ✅ düzeltilmiş hâli koşturuldu

⑦ FİNAL KARE + KAPAK KANITI  ⭐ [DERS 30]
   ffmpeg -y -sseof -0.05 -i teslim.mp4 -frames:v 1 -q:v 2 son_kare.jpg
   bash araclar/zincir_kontrol.sh son_kare.jpg kapak.png
   BEKLENEN: SPEC §1'de yazan şey son karede GÖRÜNÜYOR · zincir çıkışı ≠ 2
   ✅ koşturuldu (kare dışa aktarımı çalışıyor)
```

---

# 7. KAPAK VE SON KART

```
⭐ DEĞİŞMEYEN: kapak S9'un usta karesinden türer ve İngilizce başlık taşır
   [MUZIK_VE_KAPAK · DERS 30]. Kapak kartı SAHNE DEĞİLDİR, ayrı beyan edilir
   [DERS 4] ve teslim yapısı satırı KONUMUNU da yazar: SON 5,0 saniye [A1-b].

⭐ KAPAK KAYNAĞI ARTIK TESLİM DOSYASINDANDIR (kırpma yüzünden):
   ffmpeg -y -ss <s9_saniyesi> -i teslim.mp4 -frames:v 1 -q:v 2 s9_kaynak.jpg
   Üretilen klipten alınan kare, kırpma sonrası teslimdeki kareyle aynı değildir.

⚠️ SON KART SÜRESİ TARTIŞMAYA AÇILDI AMA DEĞİŞMEDİ:
   Rapor 2-3 sn önerdi ve 5 sn'yi "otomatik oynatma katili" saydı; ama kaynak
   göstermedi [A8-X5]. Bizim kart 5,0 sn ve YERİNDE KALIYOR.
   ⭐ Yayından sonra ilk ölçülecek şey budur: kanalın kendi tutunma eğrisi
     kartın süresini ya doğrular ya düşürür.

⭐ DÖNGÜ: S9'un son karesi S0'ın ilk karesine bağlanır [merdiven LOOP satırı].
   Kırpmadan SONRA kontrol edilir — kırpma döngü noktasını kaydırır.
```

---

# 8. KAPI

```
① KURGUDAN     ⛔ Kırpma bütçesi uygulanmadan kesilmez (§2).
   ÖNCE           Üretim süresi kutu setinden gelir [ARAC_KARTLARI §2].

② YAYINDAN     ⛔ §6'daki YEDİ ölçüm koşar. Yedisinin çıktısı üretim
   ÖNCE           günlüğü §4'e YAZILIR. Yazılmamışsa kart Y açılmaz.

③ QA'DA        ⑥ GEÇİŞ merceği artık iki kaynaktan okunabilir:
                  plan SÜRE sütunu + kesme_kontrol çıktısı. İkisi
                  ayrışıyorsa arıza KURGUDADIR, planda değil.
```

> ⭐ **KALDIRDIĞI:** "kurguyu göz kararı kes, nasılsa plan yazıyor"
> serbestliğini kaldırır ve kurgudan sonra yedi ölçüm borcu doğurur.
> Bedeli: yayın on beş dakika gecikir.
> Karşılığı: dört kez tekrarlanan ⑥ METRONOM ve iki kez tekrarlanan kapak
> arızası yayına çıkmadan yakalanır.
