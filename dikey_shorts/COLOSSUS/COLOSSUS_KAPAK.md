# 🖼️ COLOSSUS — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7'nin 4–8 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⭐ Paketin kapak promptu ("Create ONE vertical 9:16 cover … Reserve a clean central area for the title") YENİDEN
              KOMPOZİSYONDUR — KAPAK_KILAVUZU §0 ①'e göre yalnız G8 çekirdek testinden geçmezse kullanılır; o zaman da
              zincir_kontrol G8 ↔ kapak koşulur. Varsayılan: G8'in kendisi + başlık katmanı.
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 62.0 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99: RAIN TOWER'da usta kare plandan büyük çıktı, başlık kaydı;
           HIDDEN LOFT'ta prova koşulmadı]
METİN      COLOSSUS  (1 kelime · tek satır · İngilizce · film adı · paketin önerisi)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi saatte, yukarıdan, kale arkasından bakılan dev bir açık hava stadyumu: ortada projektörlerle aydınlanmış çizgili
                  yeşil saha, iki beyaz kale, dört sarı bayrak · iki yanda uzak yarıya doğru yükselen iki katlı mavi tribünler · altta
                  yakın alçak mavi tribün · uzak köşelerde iki direğin parlayan lamba başları · uzak tribünün ardında koyu park ve ağaç
                  kuşağı (başlık) · koyu mavi gök
BAŞLIKTA YAZAN    COLOSSUS

KANCA             "bu nasıl yapıldı?" — kapak bitmiş, ışıklı arenayı gösterir; görünmeyen şey başlangıçtır (çamurlu dikdörtgen, çıplak gri
                  çanak, küçücük buldozer). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ IŞIKLI YEŞİL SAHA — kadrajın en parlak şekli, koyu çanağın ortasında beyaz çizgili dikdörtgen. 140 px'te bile "futbol
                  sahası" okunur [P3-b: kontrast].
İKİNCİ OKUMA      mavi tribünler: "binlerce boş koltuk — dev bir yer"
ÜÇÜNCÜ OKUMA      iki direğin lamba başları: "maç gecesi"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① çamur ve küçücük makineler ② gri çanağın maviye, sahanın yeşile dönüşü ③ ışıkların yandığı an.
⛔ Kapak G7 DEĞİLDİR: G7'de ışıklar sönük, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" / "BEFORE-AFTER" / "BUILDWAKE" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   koyu mavi gök                     0–417      kanıt yok
   uzak kent silueti                 437–459
   ⭐ lamba başları (iki direk)       517–556    x 161–196 · 884–919 — kutunun HEMEN ÜSTÜNDE, x sınırında
   ⭐ BAŞLIK KUTUSU                   560–770    x 180–900 (kılavuz §3 "film adı kutusu") — uzak kent bandının altı + ağaç kuşağı
                                                (611–679) + park (679–740) + uzak alçak tribünün üst kenarı (740–770)
   uzak alçak tribün                 740–835    x 265–815 → 343–737
   ⭐ uzak kale çizgisi + kale         843–857    x 367–713 · kale 521–559
   ⭐ saha (uzak → yakın)              857–1354   x 367–713 → 171–909
   ⭐ merkez dairesi                   981–1056   x 477–603
   yan tribünlerin uzak kamaları     674–1345   iki kenarda
   tünel ağzı (karanlık)             1348–1408  x 104–184
   yakın alçak tribün                1457–1666  kadraj boyu
   alt UI bandı                      1440–1920  (yakın tribün, dış yol — yardımcı doku)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · saha ✅ · iki kale ✅ · uzak tribün ✅ · lamba başları (517–556, çekirdeğin 23 px üstü —
   beyanlı) · yakın tribün çekirdeğin altında — yardımcı doku, beyanlı
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, lamba başlarını, sahanın tamamını ve yakın tribünün önünü taşır · 4:5 (285–1635) ve 3:4
   (240–1680) yakın tribünün tamamını da taşır.
⚠️ Projektör ışığı park + ağaç kuşağına taşmamalı (başlık zemini) — G8 elle kontrol, plan RİSK ve PİLOT (a).
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      COLOSSUS — TEK SATIR, ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — uzak alçak tribünün ardındaki koyu park + ağaç kuşağı (sahip seçimi "Uzak uç alçak, tek
           katlı" 22.10.2026) · yazı sahayı, kaleleri ve çizgileri örtmez (paketin "saha çizgilerinin kritik kısmını boğmayacak" isteği)
           satır y ≈ 600–730 (dikey ortası ≈ 665)
PUNTO      "COLOSSUS" 8 harf: 720 px'lik kutuya ≈ 110–125 px yazı boyu sığar (kalın, dar olmayan sans-serif); gerçek yazı sınırları
           720 × 210'u AŞMAZ, aşarsa punto küçülür, harf aralığı daraltılmaz · tek ağırlık · parlama YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan mavi saatte koyu park + ağaç → kontrast iyi beklenir; ölçülür, 4,5:1'i
           geçmezse başlığın arkasına ölçülü koyu geçiş [kılavuz §5] (paketin "dar, hafif koyu arka gölge" önerisiyle aynı)
           ⚠️ lamba başlarının halesi kutunun üst kenarına (py 560) yaklaşır — prova metinsiz G8 ile ÖNCE yapılır; hale kutuya taşarsa
           satır aşağı alınır (en çok y 770'e kadar — uzak tribünün üstüne binmeden)
⛔ Başka kelime yok: "AI" · "timelapse" · "stadium" · "MUD TO MATCHDAY" · "before/after" · "BUILDWAKE" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada yakın tribün ve dış yol var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "ışıklı yeşil saha" ayrışıyor mu ⓑ COLOSSUS okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "çamurlu dev çanak, küçük buldozer" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, saha ve iki kale TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "maç gecesi, dev bir stadyum" diyor mu — "render", "oyun ekranı" ya da "çatılı arena" diyorsa G8
               yeniden; kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki saha = finaldeki saha [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + COLOSSUS   yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ       G8 tam kare — sahip kararı
ⓒ METİNSİZ        ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (paketin "merkez kare ve daha kısa dikey kırpmaları ayrıca dene"
   isteği PROVA'dır — kapak_prova.py — ayrı varyant değildir).
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse. (Paketteki "BUILDWAKE" kanal adı DEĞİLDİR — "by BUILDWAKE" ve BUILDWAKE etiketi çıkarıldı.)
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/kulüp adı yok · ≤ 40 karakter.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     From Mud to a Mega Stadium               (26)   ⭐ paketin başlığı, "| AI Timelapse" eki olmadan
② SORU   What Will Fill This Giant Bowl?          (31)   ⭐ planın MERAK SORUSU
③ KISA   Mud to Matchday                          (15)   ⭐ paketin açılış yazısı — burada başlık olarak
```

> ⚠️ Paketteki tam hâl "From Mud to a Mega Stadium | AI Timelapse" 41 karakter — kanal tavanı 40 (MUZIK_VE_KAPAK §3); "| AI Timelapse"
> eki ancak sahibin açık onayıyla kalır (THE SLOW TAKEOFF emsali). ① sonucu söyler; ② merak sorusunu söyler (KILAVUZ_REHBERI §6: "BAŞLIK
> soruyu söyler"); ③ kısa ve ritimli — karar sahibin. Üçü de 40 karakterin altında.

**Açıklama:**

```
A muddy construction site inside a giant bare concrete bowl. One bulldozer, two cranes and a crew of four turn it,
stage by stage, into a football stadium: the upper stands go on, the seats turn blue, the pitch is laid and marked.
Then the evening comes.

Weeks of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real stadium, no real club, no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #stadium #football #soccer #stadiumconstruction
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). Paketin etiketlerinden "football stadium construction" · "soccer stadium"
> yapı-özel dörtlüye girdi; BUILDWAKE çıkarıldı. Altbilginin iki dilli beyanı SİLİNMEZ, KISALTILMAZ.
> ⚠️ Paketin açıklaması ("… one stage at a time. Watch the concrete stands rise, the blue seats spread and the pitch turn green.
> COLOSSUS — an AI-generated construction timelapse concept by BUILDWAKE.") kanal adı yüzünden yeniden yazıldı; açıklama ışığı ANMAZ
> ("Then the evening comes.") — spoiler bütçesi. "Weeks of work" sahneler arası takvim atlamasının beyanıdır (plan TASARIM ⑪).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
football stadium construction, stadium timelapse, football pitch, soccer stadium, construction timelapse, stadium build, pitch installation, turf laying, ai timelapse, ai video, timelapse, colossus, stadum timelapse, footbal stadium
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("stadum timelapse" · "footbal stadium" bu yüzden bilerek var). Paketin "satisfying transformation" etiketi kanal kuralı
> ("SATISFYING" yok) yüzünden çıkarıldı. Gerçek yer/firma/kulüp adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Big stadium pitches are often not grown in the stadium at all. The grass is usually grown on a turf farm and brought in as
large rolls, laid over a carefully levelled sand-based layer that drains quickly, then rolled and watered for some time before
the first match. The white lines are normally painted by small machines that follow measured string lines, and they are
repainted before every game.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("often · usually · normally · some time"); belirli
> stadyum, ürün, ölçü ya da süre iddia edilmez (ÇIKARIM, genel bilgi). Paketin sabit yorumu ("Which transformation was your favorite:
> the stands, the turf, or the lights?") yorum tuzağı sorusudur → KULLANILMADI [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | çamurdan stadyuma (① ③), ya da bir gizem (②) | nasıl, hangi sırayla, ışık anı |
| kapak | bitmiş, ışıklı arena + başlık | çamur, çıplak çanak, küçücük makineler, maviye ve yeşile dönüş |
| ilk 2 sn | çamura girmiş bıçak, dev gri çanak, iki vinç | çanağın neye dönüşeceği |
| açıklama | buldozer, iki vinç, dört kişilik ekip, üst tribün, mavi koltuk, saha, çizgi, "akşam gelir" | ışıkların yanışı |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (mavi saatte iki direk yanar) kapak dışında söyleyemez → ✅ (taslak; kurgudan
sonra tekrar). ⚠️ Başlık ① ve ③ "stadium / matchday" sonucunu verir; ışık anı yine saklıdır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: ⭐ZEMİN ailesi — GAME ON (spor sahası, çizgi, ışıklı final) ve THE LAST LIFT (stadyum) ile ARDIŞIK YAYINLANAMAZ
   [YAYIN_PLANI §3].
