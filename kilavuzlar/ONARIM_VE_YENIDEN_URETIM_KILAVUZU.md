# 🔧 ONARIM VE YENİDEN ÜRETİM KILAVUZU — QA hükmünden klip onarımına

> `AGENTS` kart R raporu **kaydeder**; bu kılavuz kayıttan sonra **ne yapılacağını** söyler:
> hangi hüküm hangi kök nedene, hangi kök neden hangi TEK eyleme gider; zincirli formatta
> bir kareyi değiştirmenin iki klibi birden nasıl etkilediği; onarımdan sonra dikişin nasıl
> sınandığı; kaç denemede durulacağı; her denemenin nereye yazılacağı.
>
> Kaynak: A29 · 07.10.2026 (`arastirma/SONUCLAR/A29_GEMINI_HAM.md`) · denetim `A25-A29_DENETIM.md` §5 ·
> tetikleyen: arşivde 393 ham rapor ve yeniden koşu listesi var (`QA/ARSIV_12_MERCEK/00_ARSIV.md` §6),
> onarım yordamı yok.
> ⭐ Rapordan inen: **video inpainting zincirde kullanılmaz — kare düzenlenir, klip yeniden koşulur** ·
> **klibi ara kareyle bölmek** yöntemsiz belirmenin ve erimenin birinci çaresidir · **kare değişirse
> komşu da yenilenir** · **durma kuralı** · onarımdan sonra iki dikişin sınanması.
> ⛔ İnmeyen: onarım matrisinin başarı yüzdeleri (%80 · %95 …) — kaynak yok, hepsi uydurma "ÖLÇÜLDÜ";
> LPIPS < 0,02 / 0,05 eşikleri (sınanmadı); yeniden koşu maliyeti "$0,20 · 2 dk" (kaynak yok);
> "Bursa'daki ekibiniz" (rapor uydurdu). Araç sürümleri (Luma Ray 3.2 · Kling 4.0) denetimde ⇒ §8.

---

# 0. 🚪 KURAL

```
Onarım bir KÖK NEDENE yapılır, bir belirtiye değil.
  · önce sınıfla: ARAÇ · PROMPT · KARE · KURGU · PLAN — eylem sınıftan seçilir
  · ⛔ zincirde bölge düzeltme (video inpainting / video-to-video) YOK: dikiş karesini bozar
  · bir kare (Gn) değişirse İKİ klip yeniden üretilir: S(n−1) ve S(n) — Gn ikisinin ortak ucudur
  · her onarımdan sonra İKİ DİKİŞ sınanır (zincir_kontrol + kanıt nesnesi elle)
  · aynı klipte aynı eylem en çok 3 kez; toplam 6 deneme → SAHNEYİ YENİDEN TASARLA
  · her deneme günlüğe bir satır: klip · deneme no · eylem · sebep · sonuç
```

⛔ **Çapraz geçiş YOK.** Kusuru dissolve/fade ile örtmek bu formatta onarım değildir: her kesme bir
KAREDİR [KILAVUZ_REHBERI §2.7] ve kart A negatif çekirdeği "No cuts, no dissolves, no fades" der.

---

# 1. 🗂️ TRİYAJ — hüküm → kök neden → eylem

## 1.1 Beş kök neden

| kök neden | nasıl anlaşılır | örnek (ölçülmüş) |
|---|---|---|
| **ARAÇ** | aynı iki kare + aynı promptla yeniden koşunca kusur başka yerde/başka biçimde çıkıyor; kamera hareketi, kadraj kayması, aracın ön ayarı | THE MOUNTAIN DOOR — ön ayar push-in ekledi, zincir tutmadı (1,63) |
| **PROMPT** | kusur her koşuda AYNI; MOTION FOCUS başka bir işi anlatıyor, taşıyan yok, yasak kelime var | THE DEEP STEP — kubbeler tek karede bitmiş belirdi; MOTION FOCUS taban kayasını anlatıyordu [DERS 61] |
| **KARE** | klip iki ucuna sadık ama UÇLARDAN biri yanlış: nesne iki karede farklı çizilmiş, yapı yüzdesi geride | THE STONE DRAGON — moloz yığını üç dikişte farklı (REBUILT) |
| **KURGU** | klipler doğru, teslim yanlış: süre plandan sapmış, kesme yanlış saniyede, kart başka dünya | THE IRON BRIDGE · THE GLASS WALL — 100/109 sn ↔ 125 sn, final yanlış saniyede |
| **PLAN** | iki uç arasındaki iş tek klibe sığmıyor ya da fizik olarak imkânsız (8 sn'de 40 m kano, 10 dk'da bir kat) | THE EMPTY RIDGE — uzun rijit yük havada taşındı, kopyalandı [DERS 57] |

## 1.2 Altı eylem — hangisi ne zaman

| eylem | ne yapılır | kareler değişir mi | komşu etkilenir mi |
|---|---|:-:|:-:|
| **YENİDEN KOŞ** | aynı iki kare, aynı prompt, yeni tohum | hayır | hayır |
| **PROMPTU YENİDEN YAZ** | MOTION FOCUS / taşıyan / hız cümlesi düzeltilir, aynı iki kareden koşulur | hayır | hayır |
| **KAREYİ DÜZENLE** | Gn image-to-image düzeltilir (nesne yeri, yapı yüzdesi, yazı silme) — onaylı komşu kareye karşı | **evet** | **evet: S(n−1) + S(n) yeniden** |
| **KLİBİ BÖL** | araya ara kare Gn′ (iş %50) üretilir; S(n) iki zincirli klip olur (G(n) → Gn′ → G(n+1)) | yeni kare eklenir | hayır (uçlar aynı) |
| **KURGUYU DÜZELT** | kesme_kontrol ile SÜRE sütunundan yeniden kes; ihrac_kontrol; kart = GN | hayır | hayır |
| **SAHNEYİ YENİDEN TASARLA** | merdiven satırı / iki uç / rota yeniden yazılır (PLAN + 00_ANALIZ/05 satırı + sahip SAPMA) | evet | evet |

⭐ **KLİBİ BÖL bu depoda zaten tanımlı:** araç kutusu {4,6,8} çıkarsa her sahne iki zincirli klip
olur, ara kare Gn′ [PLAN §DEĞİŞMEZLER]. Onarımda aynı yol tek sahneye uygulanır: bölünen sahnenin
süresi DEĞİŞMEZ (8,0 = 4,0 + 4,0 ya da kutuya göre), kurgu tek sahne gibi keser.

---

# 2. 🧭 ONARIM MATRİSİ — beş merceğin hükmünden ilk ve ikinci eyleme

> Başarı yüzdesi YOKTUR — ölçülmedi. Sıra: kök nedenin en olası sınıfı önce. ⛔ = bu kusurda asla.

| mercek · hüküm / satır | kusur | en olası kök neden | 1. eylem | 2. eylem | ⛔ asla |
|---|---|---|---|---|---|
| ❶ SEPARATE IMAGES | kamera/kadraj kaydı, istasyon karıştı | ARAÇ · KARE | YENİDEN KOŞ (kamera cümlesi birebir) | KAREYİ DÜZENLE (kadraj çapalara göre) | yakınlaştırıp kırpmak |
| ❶ MELTING · THE BODY THAT MELTED WORST | gövde eriyor, sayı değişiyor, kimlik takası | PROMPT · PLAN | KLİBİ BÖL (eriyen anın ara karesi) | PROMPTU YENİDEN YAZ (gövde "one rigid body", sayı) | bölge düzeltme |
| ❶ Cat 4 yazı/logo | okunur yazı | KARE · PROMPT | KAREYİ DÜZENLE (yazı silinir, komşu yenilenir) | PROMPTU YENİDEN YAZ ("on any surface" + pozitif boya) | negatife nesne adı yazmak [DERS 35 · 59] |
| ❶ Cat 5 insan | net yüz, donuk işçi | PROMPT · ARAÇ | YENİDEN KOŞ | PROMPTU YENİDEN YAZ (streak / "no readable face") | — |
| ❷ WRONG DIRECTION · ONLY LIGHT | gün/mevsim geri, ışık sıçradı | KARE | KAREYİ DÜZENLE (ışık KARE TABLOSU'na) | SAHNEYİ YENİDEN TASARLA (SAAT sütunu) | renk düzeltmesiyle kurguda örtmek |
| ❷ NEXT | kesme zaman değil "sonraki" okunuyor | PLAN | PROMPTU YENİDEN YAZ (zaman taşıyıcısı klip içinde) | SAHNEYİ YENİDEN TASARLA | — |
| ❸ REBUILT · THE OBJECT … NONE | sahadaki nesneler dikişte sıfırlanıyor | KARE | KAREYİ DÜZENLE (nesne önceki karedeki yerine) + komşu | — | bölge düzeltme (dikişi kırar) |
| ❸ PARKED · THE LONGEST IDLE STRETCH | saha boş, makine park | PROMPT | PROMPTU YENİDEN YAZ (≥3 el + geçişli fiil + malzeme akışı) | YENİDEN KOŞ | — |
| ❸ THE GROWTH NOBODY MADE | ajansız büyüme | PROMPT | PROMPTU YENİDEN YAZ (MOTION FOCUS taşıyanı adıyla) | KLİBİ BÖL | — |
| ❹ DIFFERENT | yapının kimliği değişti | KARE · PLAN | KAREYİ DÜZENLE (usta kareye karşı) + komşular | SAHNEYİ YENİDEN TASARLA | — |
| ❹ APPEARING · THE FIRST PIECE THAT APPEARED | eleman yöntemsiz belirdi | PROMPT · PLAN | KLİBİ BÖL (eleman %50 ara karesi) | PROMPTU YENİDEN YAZ (kaynak → taşıyan → hedef) [DERS 61] | — |
| ❹ INTRUDERS · THE MOST DAMAGING INTRUDER | davetsiz nesne | PROMPT · KARE | KAREYİ DÜZENLE (nesne çıkar) + komşu | PROMPTU YENİDEN YAZ (korpus kilidi, yasak kelime) | negatifte adını anmak |
| ❹ yapı dikişte geriledi | monoton büyüme bozuldu | KARE | KAREYİ DÜZENLE (yüzde PLAN'dan) + komşu | — | — |
| ❺ STOPS | final erken duruyor / olay yok | PROMPT · KURGU | PROMPTU YENİDEN YAZ ("from about four to eight seconds …") | KURGUYU DÜZELT (süre, kesme) | finali kurguda uzatmak (donmuş kare) |
| ❺ NEVER REACHED THE SCREEN | plan vaadi ekranda yok | PLAN · KURGU | KURGUYU DÜZELT (süre, saniye) | SAHNEYİ YENİDEN TASARLA | — |
| teslim süresi plandan saptı | kart/kesme/süre | KURGU | KURGUYU DÜZELT (kesme_kontrol · ihrac_kontrol) | — | — |
| su kotu sıçradı | kot karede zıpladı | KARE | KAREYİ DÜZENLE (kot SU KOTU DEFTERİ'nden) + komşu | PROMPTU YENİDEN YAZ (kesir + tanık çizgi) | — |
| ikinci istasyonda başka dünya | iç kamerada çapa tutmadı | KARE | KAREYİ DÜZENLE (ortak çapa cümlesi, ana kareye bak) | KAMERAYI KALDIR (sahne ana istasyona) | — |

Mercek → kategori ayrıntısı: `QA/Q1…Q5`. Kusur sahipliği (bir kusur tek mercekte): `RUBRIK_YAZIM_KILAVUZU` §5.

---

# 3. 🔗 ZİNCİR ETKİSİ — bir kare iki klibin ucudur

```
   G(n−1) ──S(n−1)──▶ G(n) ──S(n)──▶ G(n+1)
                        ▲
            Gn DÜZENLENİRSE:  S(n−1) (son karesi değişti) + S(n) (ilk karesi değişti) YENİDEN ÜRETİLİR
            S(n) YENİDEN KOŞULURSA (kareler aynı): yalnız S(n) — komşular değişmez
            S(n) BÖLÜNÜRSE:   G(n) ──▶ Gn′ ──▶ G(n+1)   uçlar aynı, komşular değişmez
```

```
KARE DÜZENLEME SIRASI (ters zincirle uyumlu [DERS 5 · P2-a])
  1. düzeltilecek kare Gn, onaylı KOMŞU karelerden (G(n+1) ve usta kare GN) image-to-image düzenlenir —
     sıfırdan üretilmez
  2. zincir_kontrol.sh G(n+1) Gn' GN   ve   zincir_kontrol.sh Gn' G(n−1) GN   → iki yönde de çıkış ≠ 2
  3. kanıt nesnesi iki karede aynı pikselde (elle ✓/✗) [DERS 25]
  4. S(n−1) ve S(n) aynı promptla yeniden koşulur — iki klip de yeni karelere kilitli
  5. düzeltme bir sonraki kareyi de bozuyorsa (zincir_kontrol düştü) zincir bir halka daha yürür; en çok
     İKİ halka — üçüncüde SAHNEYİ YENİDEN TASARLA
```

⭐ **İkinci istasyon:** kokpit/detay kareleri ana zincire bağlı DEĞİLDİR. Kokpit karesini düzeltmek ana
klipleri etkilemez; ana dış kareyi (ör. G14 · G22) düzeltmek kokpit klibini etkilemez ama o dış karenin
İKİ ana komşusunu etkiler [ISTASYON_VE_IC_MEKAN_KILAVUZU §2].

---

# 4. 🧪 DİKİŞ GÜVENLİĞİ — onarımdan sonra iki dikiş

```
① KAREDEN    yeni klibin ilk ve son karesi çıkarılır:
               ffmpeg -ss 0.05 -i S<n>_K<k>.mp4 -frames:v 1 ilk.png
               ffmpeg -sseof -0.05 -i S<n>_K<k>.mp4 -frames:v 1 son.png
② ZİNCİR     bash araclar/zincir_kontrol.sh G<n>.png ilk.png G<N>.png     (giriş dikişi)
             bash araclar/zincir_kontrol.sh son.png G<n+1>.png G<N>.png    (çıkış dikişi)
             çıkış 2 = dikiş kırık → klip reddedilir (yeniden koşu, eylem değişmez)
③ ELLE       kanıt nesnesi iki dikişte aynı piksel · ışık/gölge yönü KARE TABLOSU ile aynı · ±1 sn
             çevresinde %400 büyütmede titreme (flicker) ya da "nefes alma" yok
④ KURGU      klip yerine konunca bash araclar/kesme_kontrol.sh teslim.mp4 <PLAN>  (± 0,25 sn)
             ve bash araclar/ihrac_kontrol.sh — süre, kart, final tutuşu
⑤ QA         yeni master = yeni sürüm. Yeniden koşulan mercekler:
               · onarılan kusurun SAHİBİ mercek (§2 tablosundaki)
               · ❶ GÖRÜNTÜ her zaman (öldürücü; dikiş ve erime onu en çok etkiler)
               · 3 ya da daha çok klip değiştiyse BEŞ mercek
             ham ad _K2 (QA_KAYIT §3) · eski koşu SİLİNMEZ, durumu YERİNE GEÇTİ
```

⚠️ Rapor dikiş için LPIPS ve optik akışa dayalı warping error önerdi (RAFT). Bu depoda kurulu değil ve
eşikleri sınanmadı; `zincir_kontrol.sh` kenar ve nirengi ölçer, kalibre değildir [araç başlığı].
LPIPS/RAFT bir gün eklenirse önce arşiv kesitlerinde (bilinen kırık dikişler) eşik ölçülür [A29-d].

---

# 5. ⏱️ BÜTÇE VE DURMA KURALI

```
AYNI KLİP · AYNI EYLEM    en çok 3 deneme → sonra matristeki 2. eyleme geçilir
AYNI KLİP · TOPLAM        en çok 6 deneme → SAHNEYİ YENİDEN TASARLA (PLAN + sahip SAPMA)
KARE DÜZENLEME ZİNCİRİ    en çok 2 halka (§3)
FİLM                      onarım 5 klibi geçerse ya da bir öldürücü hüküm (❶ SEPARATE · ❸ REBUILT ·
                          ❹ DIFFERENT) onarımdan sonra SÜRERSE → film yeniden üretim kararı sahibe
MALİYET / SÜRE            ÖLÇÜLMEDİ — günlüğe her deneme için araç kredisi ve dakika yazılır;
                          üç filmden sonra bu satır gerçek sayıyla dolar
```

⚠️ 3 / 6 sayıları VARSAYIMDIR (rapor 3 dedi, kaynak yok); ilk üç onarılan filmde ölçülür [A29-c].

---

# 6. 🗃️ SÜRÜM KAYDI — veritabanı yok, git + markdown

```
DOSYA ADI    kare   G<n>.png → düzenlenince G<n>_K<k>.png         (k = 2, 3 …; onaylı olan günlükte)
             klip   S<n>.mp4 → yeniden üretilince S<n>_K<k>.mp4
             bölünmüş klip  S<n>a_K<k>.mp4 · S<n>b_K<k>.mp4  (ara kare G<n>′_K<k>.png)
             master teslim_K<k>.mp4 · QA ham <FILM>_Q<n>_<AD>_K<k>_HAM.md [QA_KAYIT §3]
ÖZET         dosyanın sha256 ilk 12 hanesi günlük satırına (shasum -a 256 dosya | cut -c1-12)
VİDEO DOSYASI depoya girmez (bugünkü düzen); Git LFS sahip kararıdır ⬜
```

Üretim günlüğü §5 (PLANDAN SAPMALAR) her onarım için bir satır alır:

```
| tarih | S | deneme | hüküm (mercek · satır · m:ss.s) | kök neden | eylem | değişen dosya (sha) | dikiş ①② | sonuç |
| 07.10.2026 | S5 | K2 | ❹ APPEARING · gövde 0:41,0 | PROMPT | KLİBİ BÖL (G5′ +1,5 m) | S5a_K2 · S5b_K2 · G5′_K2 (a1b2c3d4e5f6) | ✓ ✓ | ✅ |
```

---

# 7. ✅ KONTROL LİSTESİ — her onarımda (ihlalde TEK eylem)

| # | madde | ihlal → eylem |
|:-:|---|---|
| 1 | hüküm bir mercek satırına ve saniyeye bağlandı mı (genel "kötü" değil) | → raporu yeniden oku (QA'yı değil) |
| 2 | kök neden beş sınıftan biri olarak yazıldı mı | → sınıflamadan eylem seçme |
| 3 | seçilen eylem matristeki ⛔ sütununda mı | → matristeki 1. eylem |
| 4 | bir kare değiştiyse iki komşu klip de yeniden üretildi mi | → KOMŞUYU DA YENİLE |
| 5 | düzenlenen kare onaylı komşudan ve usta kareden türetildi mi (sıfırdan değil) | → KAREYİ YENİDEN DÜZENLE |
| 6 | iki dikişte zincir_kontrol çıkışı 2 değil mi | → YENİDEN KOŞ |
| 7 | kanıt nesnesi iki dikişte aynı piksel mi | → KAREYİ DÜZENLE |
| 8 | bölünmüş sahnenin toplam süresi plandaki SÜRE ile aynı mı | → KURGUYU DÜZELT |
| 9 | aynı eylem 3 kez denendi mi | → 2. eyleme geç |
| 10 | toplam 6 deneme aşıldı mı | → SAHNEYİ YENİDEN TASARLA |
| 11 | sahibi mercek + ❶ yeniden koşuldu mu (_K2) | → QA'yı koş |
| 12 | günlük §5'e satır yazıldı mı (sha dâhil) | → yaz, sonra devam |

---

# 8. 📎 İNMEYENLER VE AÇIK OLANLAR

```
⛔ başarı yüzdeleri matrisi            kaynaksız — her hücre "ÖLÇÜLDÜ" etiketliydi, hiçbirinde kaynak yok
⛔ LPIPS < 0,02 / > 0,05 eşikleri      sınanmadı; araç kurulu değil
⛔ "$0,20 · 2 dk / yeniden koşu"        kaynak yok
⛔ "Bursa'daki küçük ekibiniz"          rapor uydurdu (promptta yer yok)
⚠️ çoklu keyframe                     Luma Ray 3.2 (9 Haz 2026 — rapor "Eylül" dedi) 16 keyframe · 1080p'de 20 sn ·
                                        16-bit EXR ✅ · Kling 4.0 (duyuru 30 Eyl 2026; tam sürüm Ekim) 10 keyframe · 3–30 sn ✅.
                                        Ara kareler "kilit" değil yönlendirme olabilir [İDDİA] — ARAÇ KAPISINDA ölçülene kadar
                                        bölmek (iki zincirli klip) kalır; çok kareli tek klip yolu açılmaz
⚠️ yayın QC sınıfları (Blocker/Issue/FYI) — arka plan bilgisi · VFX sürüm adı: Netflix örneği
                                        AGM_104_065_010_comp_NFX_v005 ✅ (rapor fazladan "TCC" alanı uydurdu) — §6 şeması
                                        aynı mantıkla (sahne_görev_sürüm) · warping error'ın zamansal bozulmaya duyarlılığı
                                        TRAJAN makalesinde (arXiv:2505.00209 — rapor başlığı uydurdu) ✅
⬜ Git LFS — sahip kararı
⬜ LPIPS / RAFT ölçümü araclar/'a — sahip kararı; önce arşivde kalibrasyon
```
