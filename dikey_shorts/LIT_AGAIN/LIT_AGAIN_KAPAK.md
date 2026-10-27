# 🖼️ LIT AGAIN — KAPAK + YAYIN PAKETİ

```
⭐ KAPAK FİLMİN SONUNDA KART OLARAK DA VAR (sahip kuralı 16.10.2026 — her film): 64,0–69,0 (yayında 32,0–37,0),
   erime ≤ 1 sn, S7·b'nin 60,0–64,0 tutuşundan SONRA. Kart 5,0 sn — sahip seçimi (16.10.2026). Logo yok, müzik yok. YouTube
   Shorts'ta kapak "videodan kare seç" ile bu karttan seçilir [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §8 · K3]; ayrı açılış afişi YOK.
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB  ⭐ HIDDEN LOFT kapağı 941 × 1672 çıktı [DERS 99 2. ölçüm] — ölçü dışa aktarımda kontrol
KAYNAK     ⭐ YALNIZ G8 — S7'nin hedef karesi, filmin SON karesi (zincirin İLK üretilen karesi, metinden; G7a ile aynı dosya)
           [DERS 30 · 91 · DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 ①]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
           ⛔ Ayrı üretilmiş kapak görseli KULLANILMAZ: POOL ROOM'da başka kamera, gündüz, fazladan nesne oldu [DERS 85].
           ⛔ Paketin "dönen huzme kadrajın üst üçte birinde" kapak fikri UYGULANMAZ: huzme hiçbir promptta yok [ISIK_FINALI · STAR DOCK];
              kapak sabit ışıltılı G8'dir.
KANIT      bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png  → çıkış 2 = TESLİM YOK
           ⭐ kaynak TESLİM dosyasından alınır: ffmpeg -ss 63.5 -i teslim_1x.mp4 -frames:v 1 g8_kaynak.jpg
PROVA      python3 araclar/kapak_prova.py kapak.png → 9:16 · 3:4 · 4:5 · 1:1 + 140 px küçükler + PROVA_PANOSU.png [DERS 94]
           ⭐ İLK PROVA METİNSİZ G8 İLE, G8 ONAYINDAN ÖNCE [DERS 99]
METİN      LIT AGAIN  (2 kelime · tek satır · İngilizce · film adı)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR

```
KAPAKTA GÖRÜNEN   mavi saatte, kayalık bir burnun ucunda tek bir fener kulesi: beyaz gövde, iki koyu kırmızı bant, koyu kırmızı kapı, siyah
                  korkuluk; tepede sıcak beyaz ışıldayan fener odası ve yeşil bakır kubbe · arkada düz deniz ufku, sağ uzakta dalgakıran ·
                  önde boş kaya, patika, yosunlu kaya ve şamandıra kaidesi · üstte düz derin mavi gök (başlık)
BAŞLIKTA YAZAN    LIT AGAIN

KANCA             "bu fener sönmüş müydü?" — başlık "AGAIN" der; kapak yanan feneri gösterir, görünmeyen şey harabedir (çalı, dökük boya,
                  kırık cam). Merak "ne olacak?"tan "neydi?"ye kayar [P21-f]; cevabı 64 saniyenin yolu verir.
KANIT NESNESİ     ⭐ YANAN FENER ODASI — mavi gökte, kadrajın en parlak noktası; 140 px'te bile "ışık yanıyor" okunur [P3-b: kontrast].
İKİNCİ OKUMA      kırmızı-beyaz bantlı kule: "bu bir deniz feneri"
ÜÇÜNCÜ OKUMA      boş kaya ve ufuk: "ıssız bir burun"

⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmi taşıyan üç şey:
   ① çalılara gömülü, boyası dökülen, camları kırık kule ② iskelenin kat kat yükselişi ve kulenin yüzünün değişimi ③ lambanın yandığı an
   ve lensin dönüşü.
⛔ Kapak G7 DEĞİLDİR: G7'de fener sönük, kamyonet ve işçiler sahada, ödül yok. Kırmızı ok / çember / emoji / "AI TIMELAPSE" /
   "BEFORE-AFTER" YOKTUR.
```

## 2. Yerleşim — G8 tam kare, kırpma yok [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §3]

```
KAYNAK DOSYA   G8 (3840 px boy) → 1080 × 1920'ye ÖLÇEKLENİR, kırpılmaz · kapak için ayrı görsel ÜRETİLMEZ [DERS 30]

KARE İÇİNDE NE NEREDE (üstten px · G8 kilitleri · TÜRETİLMİŞ, ön görselleştirmede ölçülür):
   açık gök (derin mavi)              0–560      kadraj boyu
   ⭐ BAŞLIK KUTUSU                   560–770    x 180–900 (kılavuz §3 "film adı kutusu") — fener odasının üstündeki DÜZ derin mavi gök
   açık gök                           770–813    — kutuyla top arasında 43 px
   ⭐ havalandırma topu + kubbe        813–867    x 467–613 (yeşil bakır)
   ⭐ fener odası (YANIK)              867–922    x 506–574 — kadrajın EN PARLAK şeyi
   galeri + siyah korkuluk            919–949    x 473–607
   deniz ufku                         960        kadraj boyu
   dalgakıran                         ≈ 1000–1030 x ≈ 760–1080
   ⭐ üst kırmızı bant                 1044–1113
   ⭐ alt kırmızı bant                 1208–1276
   ⭐ koyu kırmızı kapı                1298–1358  x 529–551
   kule tabanı                        1358
   yosunlu kaya · şamandıra kaidesi   1455–1583 · 1496–1544
   alt UI bandı                       1440–1920  (kaya, patika — yardımcı doku)

⭐ KAPAK ÇEKİRDEĞİ (x 150–930 · y 540–1380): başlık ✅ · fener odası ✅ · bantlar ✅ · kapı ✅ · ufuk ✅ — kule kutunun tam ortasında
⭐ KIRPMA HESABI: 1:1 (y 420–1500) başlığı, kulenin tamamını, kapıyı ve kayanın üstünü taşır · 4:5 (285–1635) ve 3:4 (240–1680) daha çok gök
   ve ön plan taşır.
⚠️ Fener ışıltısı başlık kutusuna taşmamalı (aradaki boşluk yalnız 43 px üstte, top ile kutu arası) — G8 elle kontrol, plan RİSK ④ ve PİLOT (a).
⚠️ Kule DAR (138 px) — başlık kuleden geniş olur; bu kılavuzun kutusudur, beyanlı (sahip seçimi "kapak çekirdeği").
```

## 3. Metin — DIKEY_TIMELAPSE_KAPAK_KILAVUZU §5 ölçüleriyle

```
METİN      LIT AGAIN — TEK SATIR, ORTALI
YER        ⭐ başlık kutusu x 180–900 · y 560–770 — fener odasının üstündeki düz derin mavi gök · yazı kuleyi ve fener odasını örtmez · satır
           y ≈ 600–720 (dikey ortası ≈ 660)
PUNTO      "LIT AGAIN" 9 karakter: 720 px'lik kutuya ≈ 110–130 px yazı boyu sığar (kalın, dar olmayan sans-serif); gerçek yazı sınırları
           720 × 210'u AŞMAZ, aşarsa punto küçülür, harf aralığı daraltılmaz · tek ağırlık · parlama YOK
RENK       kırık beyaz #E8E4DC [KANAL_KIMLIGI palet] · arka plan derin mavi gök → kontrast iyi beklenir; ölçülür, 4,5:1'i geçmezse başlığın
           arkasına ölçülü koyu geçiş [kılavuz §5]
⛔ Başka kelime yok: "AI" · "timelapse" · "lighthouse" · "before/after" kapağa girmez.
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı [MUZIK_VE_KAPAK §4.2] — orada şamandıra kaidesi ve kaya var.
⛔ Metin MODELE yazdırılmaz — post-prodüksiyonda dizilir; G8 promptu "no text" der.
```

## 4. Testler — geçmeden yüklenmez

```
① 140 PX       kapak_prova.py küçükleri → ⓐ "yanan fener" ayrışıyor mu ⓑ LIT AGAIN okunuyor mu ⓒ sağ alt köşe boş mu ·
               ⭐ aynı test G0'a: "çalılara gömülü harabe fener" 140 px'te okunuyor mu
② KIRPMA       PROVA_PANOSU.png: 3:4 · 4:5 · 1:1'de başlık TAM, kule ve fener odası TAM mı [DERS 94 · 99]
③ SONUÇ OKUMASI kapağa 3 sn bakan biri "yeniden yanan eski bir fener" diyor mu — "kart-postal", "render", "oyun ekranı" diyorsa G8 yeniden;
               kapak yeniden ÇERÇEVELENMEZ
④ KAPAK KANITI zincir_kontrol.sh g8_kaynak.jpg kapak_metinsiz.png [DERS 30 · 85]
⑤ GERÇEK ÖNİZLEME Instagram profil ızgarası · TikTok kapak seçici · Shorts "videodan kare" — üçü ayrı bakılır [kılavuz §8]
⑥ ÜÇ NOKTA     açılış (G0) · final (G8) · kart (G8 + metin) yan yana: karttaki kule = finaldeki kule [MUZIK_VE_KAPAK §5]
```

## 5. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ G8 + LIT AGAIN       yukarıdaki yerleşim · ANA VARYANT · filmin sonundaki kart budur
ⓑ BAŞLIKSIZ            G8 tam kare — sahip kararı
ⓒ METİNSİZ             ⓑ ile aynı görsel, ayrı dosya adı — zincir_kontrol'ün koşulduğu varyant
⛔ ÜÇÜ DE YALNIZ G8'DEN TÜRER. Öncesi/sonrası yok, kırpma varyantı yok (kırpmalar PROVA'dır — kapak_prova.py).
```

---

# 📣 YAYIN PAKETİ — İNGİLİZCE [MUZIK_VE_KAPAK §3 · apexait/youtube/PAKETLEME_SABLONU]

```
⛔ Kanal: Apex AI Timelapse.
⛔ Başlık: büyük harf bağırma yok · "SATISFYING" yok · sayı yemi yok · gerçek yer/firma/marka adı yok · ≤ 40 karakter.
```

**Başlık — üç kalıp (biri seçilir · sahip kararı):**

```
① İŞ     Abandoned Lighthouse Lit Again           (30)   ⭐ sahibin paketinin başlığı
② SORU   Will This Lighthouse Shine Again?        (33)   ⭐ planın MERAK SORUSU
③ KISA   From Ruin to Beacon                      (19)   ⭐ paketin alternatifi
```

> ① sonucu söyler; ② merak sorusunu söyler (KILAVUZ_REHBERI §6: "BAŞLIK soruyu söyler"); ③ kısa ve yaylı — karar sahibin. Üçü de
> 40 karakterin altında. Kapak kartının metni her durumda film adı "LIT AGAIN" kalır.

**Açıklama:**

```
An abandoned lighthouse on a rocky point, buried in brambles, its paint peeling and its lantern glass broken.
A crew of three clears it, wraps it in scaffold and strips it back, then paints it white with two red bands
and fits a new door and new glass. Then the scaffold comes down and the evening comes.

Weeks of work in 32 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration; the only text is the closing title card.
Every frame is generated with AI. This is not a record of a real project:
no real lighthouse, no real place, no real company is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #lighthouse #restoration #coastal #seaside
```

> Hashtag: 3 geniş + 5 niş (sabit) + 4 yapı-özel = 12 ✅ (8–12). "before/after" etiketi bilerek YOK (sahip kuralı 19.09.2026). Altbilginin iki dilli beyanı
> SİLİNMEZ, KISALTILMAZ. Açıklama ışığın yanışını ANMAZ ("Then … the evening comes.") — spoiler bütçesi. "Weeks of work" sahneler arası
> takvim atlamasının beyanıdır (plan TASARIM ⑬).

**Etiketler (YouTube Studio "Etiketler" alanı · virgülle):**

```
lighthouse restoration, abandoned lighthouse, lighthouse timelapse, scaffold timelapse, restoration timelapse, construction timelapse, ai timelapse, ai video, timelapse, lit again, lighthose restoration, lighthouse restoraton
```

> ⚠️ Depoda Studio etiketi kuralı YOK — YouTube'un kendi notu: etiketin keşfe katkısı azdır, en çok yanlış yazılan aramalarda
> işe yarar ("lighthose restoration" · "lighthouse restoraton" bu yüzden bilerek var). Gerçek yer/firma/marka adı yok.

**Sabit yorum (işin arkasındaki gerçek yöntem · tek paragraf):**

```
Old lighthouse lenses are often kept and cleaned rather than replaced: the big glass prisms bend the light of a fairly small lamp into a
narrow, bright pencil, and as the lens turns, that pencil sweeps past a ship as a flash. The red and white bands are a daymark — each
lighthouse along a coast tends to carry its own pattern, so sailors can tell one tower from another in daylight.
```

> ⚠️ Sabit yorum ŞABLONLAŞTIRILMAZ (PAKETLEME §4). İddialar genel ve ihtiyatlı ("often · tends to"); belirli ürün, ölçü, süre ya da
> fener iddia edilmez (ÇIKARIM, genel bilgi). Yorum tuzağı sorusu YOK [A33-b].

**🧾 SPOİLER BÜTÇESİ — dört yüzey [MUZIK_VE_KAPAK §3.3]:**

| yüzey | verir | saklar |
|---|---|---|
| başlık | fener yeniden yanar (①), bir soru (②), bir yay (③) | nasıl, hangi sırayla, ışığın anı |
| kapak | bitmiş, yanan fener + başlık | harabe, iskele, yüzeyin değişimi, lambanın yanışı |
| ilk 2 sn | çalılara gömülü harabe kule, kesilen çalı, konteynere yürüyen işçi | kulenin neye dönüşeceği |
| açıklama | üç kişilik ekip, iskele, raspa, beyaz + iki kırmızı bant, yeni kapı ve cam, "akşam gelir" | ışığın yanışı, lensin dönüşü |

TEK CÜMLE TESTİ: dört yüzeyi okuyan biri dönüm noktasını (mavi saatte lamba tek karede yanar, lens döner) kapak dışında söyleyemez → ✅
(taslak; kurgudan sonra tekrar). ⚠️ Kapak yanan feneri gösterir; YANIŞ ANI ve dönüş yine saklıdır.

**Yükleme:** ⛔ YouTube "Altered content" · TikTok AIGC · Instagram AI etiketi — üçü de elle [AGENTS kart Y adım 6].
⛔ Yayın sırası: KULE ailesi — THE DARK ROCK (fener inşası), THE BLUE DOOR (restorasyon, ışıklı final), THE LAST HARBOR (fener yanar) ve
   THE RAIN TOWER (aynı KULE siluet) ile ARDIŞIK YAYINLANAMAZ [YAYIN_PLANI §3].
