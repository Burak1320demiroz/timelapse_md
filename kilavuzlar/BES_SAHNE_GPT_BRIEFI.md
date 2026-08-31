# 🤝 BEŞ SAHNE GPT BRİEFİ — harici bota yaptırma kartı

> **Bu dosya bir kılavuz değil, bir SİPARİŞTİR.** Depo dışındaki bir bota
> (Restoration Timelapse GPT, ChatGPT, başka bir asistan) yapıştırılır ve
> karşılığında `dikey_shorts/<PROJE>/` klasörüne düşecek **tam prodüksiyon
> dokümanı** gelir: 5 görsel + 5 I2V + 5 T2V promptu + müzik + kapak + paket
> + QA SPEC.
>
> `TIMELAPSE_SISTEM_PROMPTU.md` **10 sahnelik** motordur ve bu deponun
> varsayılanıdır. Bu dosya onun **5 × 6,0 sn varyantıdır** ve varyantın
> NEYE MAL OLDUĞUNU önce yazar, sonra sipariş verir.
>
> ⛔ Harici bot bu deponun hiçbir dosyasını okuyamaz. Bu yüzden brief
> **kendi kendine yeter**: negatif çekirdek, iskeletler ve kapı maddeleri
> içine BİREBİR kopyalanmıştır. Atıf vermek, hiçbir şey vermemektir [D-a].

---

# 1. ⚠️ 5 × 6,0 IZGARASININ BEDELİ — sipariş vermeden önce oku

Depo ızgarası 10 × 6,0 = 60,0 sn'dir ve bu bir tercih değil, iki ölçülmüş
dersin sonucudur. Beşe indirmek şu dört şeyi kırar:

| Kural | 10 sahnede | 5 sahnede | Ne yapılıyor |
|---|---|---|---|
| Kesme başına aşama sıçraması | küçük | ⛔ **~2 katı** | ters inşa artık tavsiye değil **ZORUNLU** |
| Ritim [DERS 13] | varyans yazılabilir | ⚠️ 5 eşit kesme = **METRONOM riski** | §1.2 ritim varyantı |
| Kış iki sahne [DERS 7] | 10'da 2 (%20) | 5'te 2 (**%40**) | kış S2–S3 çiftini alır, başka yere konmaz |
| Detay istasyonu | en fazla 2 | ⛔ **0** | beş sahne de ANA istasyondan |

## 1.1 ⭐ SIÇRAMA KESMEDE BÜYÜR, KLİPTE BÜYÜMEZ

Beş sahneye inerken yapılabilecek en büyük hata, klip içine iki iş adımı
koymaktır. Ölçüldü: tek klipte 13 kat çıkarıldı ve `② GEOMETRIC STABILITY`
0/10 geldi ("slabs and columns visibly warp, ripple and breathe").

```
DEĞİŞEN     sahneler ARASI sıçrama → ② AYNI YAPI riski artar
            tek ilacı ZİNCİRLİ ÜRETİM (ters inşa · zincir_kontrol.sh)
DEĞİŞMEYEN  sahne İÇİ bütçe: 1 gün + BİR görünür iş adımı
            ⛔ "cephe sarılır VE ışıklar yanar" iki adımdır, bir klibe girmez
```

## 1.2 ⚠️ RİTİM — proje sahibi 5 × 6,0'ı kilitledi

⛔ **Ölçülmüş risk:** eşit aralıklı kesme dizisi tempo değil NABIZ üretir.
THE CLOSING SPAN'de on kesme 6,0 · 5,8 · 6,2 · … idi ve `⑥ RİTİM 0/10 ·
VERDICT METRONOM` geldi — üstelik film "hâlâ yavaş" okundu [DERS 13].
Beş eşit kesme aynı hükmü daha kolay alır.

```
⭐ VARSAYILAN IZGARA (120 BPM ölçüsüne oturur, toplam 30,0)
                                   6,0 · 4,0 · 6,0 · 4,0 · 10,0 = 30,0 sn
                                    3     2     3     2     5    ← ölçü sayısı
                                          ↑ kısa       ↑ kısa   ↑ doruk uzun

⛔ DÜZ IZGARA (kullanılmaz)         6,0 · 6,0 · 6,0 · 6,0 · 6,0  = 30,0 sn
```

⛔ **DÜZ IZGARA ARTIK VARSAYILAN DEĞİL — ÇÜNKÜ KOŞULDU VE DÜŞTÜ.**

```
THE NARROW LOT · kesme aralıkları  6,0 · 6,0 · 6,0 · 6,0
⑥ RHYTHM AND PATTERN  4/10   ·   ⑥ VERDICT  METRONOM
"rigidly spaced 6.0-second intervals … establishing a mechanical metronome
 rhythm rather than an intentional narrative arc or release"

Bu, aynı hükmün ikinci ölçümüdür (CLOSING SPAN'de on eşit kesme, aynı hüküm).
İki farklı ızgarada, iki farklı filmde, aynı sonuç.
```

⭐ Ritim değişikliği brief'te **tek satır**dır (`§B2 TESLİM YAPISI` ve `§F`
tablosunun SÜRE sütunu); prompt gövdeleri aynı kalır. Kapı 5 satırlık tabloda
süre eşitliğini BLOCK edemez (eşik 6 satır) — **makine bunu yakalamaz, ⑥
merceği yakalar.** Düz ızgara yine de isteniyorsa gerekçesi plana yazılır.

---

## 1.3 ⭐ İLK KOŞU ÖLÇÜLDÜ — bu bölüm artık varsayım değil

Bu brief bir kez koşuldu (`THE NARROW LOT`, harici GPT → OpenArt) ve altı
mercekle ölçüldü. Kayıt: `QA/RAPORLAR/THE_NARROW_LOT.md`.

```
⭐ GEÇEN — deponun ÜÇ filminde İLK KEZ
   ① IS THIS A TIME-LAPSE?    ✅ TIME-LAPSE   (önceki ikisi: AYRI GÖRÜNTÜLER)
   ⑤ IS IT THE SAME WORLD?    ✅ SAME WORLD   (önceki ikisi: REBUILT)
   ⑤ kanıt nesnesi            ✅ "coiled hose" (önceki ikisi: NONE FOUND)
   ⑥ DOES THE CUT MEAN TIME?  ✅ TIME         (önceki: SIRADAKİ)
   ③ zaman tahmini            ✅ "about one year" — plan ~12 ay, İLK KEZ TUTTU
   ① CAMERA LOCK · FRAME IDENTITY · ANCHOR IDENTITY · STATION IDENTITY  10/10

⛔ DÜŞEN
   ② DIFFERENT · APPEARING (2,6)   ⑥ METRONOM   ④ NONE FOUND
   ③ TIME RATE · CLOUD · SUN DIRECTION  hepsi 0/10 — gökyüzü ve gölge DONDU
```

### ⭐ Tek cümlelik teşhis: **birebir taşınan tuttu, çevrilen düştü.**

| Brief'in dayattığı şey | Botta ne oldu | Ölçüm |
|---|---|---|
| `The scene begins exactly as the provided image.` | 5/5 birebir | ① FRAME IDENTITY **10** |
| `does not move at any point` | 5/5 birebir | ① CAMERA LOCK **10** |
| `occupies exactly the same width of the frame` | 5/5 birebir | ① ANCHOR IDENTITY **10** |
| çapa bloğu **SAYIYLA** (6 kat · 3 baca · 5 pencere) | 5/5 birebir | ⑤ **SAME WORLD** |
| YAPI BIBLE sayıları (oturum · aks) | **0/5 — düştü** | ② STRUCTURE IDENTITY **2** |
| `COMPOSITION` bloğu + güvenli alan | **0/5 — nesre çevrildi** | ① SAFE AREA **4** |
| `TIME RATE` I2V'de | **0/5 — yalnız görselde** | ③ TIME RATE **0** |
| insan kuralı tam metin | **0/5 — kısaltıldı** | ① PEOPLE **0** |

⭐ **Kural şu:** brief'in BİREBİR dediği her cümle 10/10 aldı; brief'in
anlattığı ama birebir dayatmadığı her şey ya kısaldı ya kayboldu ya da
yanlış prompta düştü. §J · §E · §C bu ölçümden sonra yeniden yazıldı.

---

# 2. KULLANIM

```
1. §A GİRDİ KARTI'nı doldur (konsept + yapı + saha + direnç + kamera sayıları)
2. §B'den §Ş'ye kadar olan bloğun TAMAMINI kopyala, bota yapıştır
3. Gelen dokümanı  dikey_shorts/<PROJE>/<PROJE>_DIKEY_TIMELAPSE.md  olarak kaydet
4. ⛔ KAPI:  python3 araclar/prompt_kontrol.py dikey_shorts/<PROJE>/<PROJE>_DIKEY_TIMELAPSE.md
   BLOCK ise üretme — §Ş'deki madde numarasını bota söyle, o maddeyi düzelttir
5. QA SPEC bölümünü ayrı dosyaya böl: <PROJE>_QA_SPEC.md
6. Üretim: ⛔ TERS — önce S4 usta kare, sonra geriye, her karede zincir_kontrol.sh
```

⛔ **Bot görsel ÜRETMEZ.** Bu koşunun çıktısı metindir. Görsel üretimi ters
sırayla ve zincir kapısıyla, bu deponun akışında yapılır (`AGENTS §2 kart B`).

---

# 3. 📥 DÖNÜŞTE — sen promptları ve QA raporlarını getirdiğinde

```
PROMPT GELDİ   → kart P: prompt kapısı + tutarlılık listesi
FİLM ÜRETİLDİ  → kart Q: ① ③ ⑤ ÖNCE (doküman VERİLMEDEN), sonra ② ④ ⑥
RAPOR GELDİ    → kart R: HAM_RAPORLAR'a dokunulmadan kaydet, VERDICT satırını
                 skordan ÖNCE oku, T tablosuna satır, RAPORLAR/<FILM>.md
YENİ BOZULMA   → kart D: DERSLER.md + "KALDIRDIĞI" satırı zorunlu
```

---
---

# ⬇️⬇️⬇️ BURADAN AŞAĞISI KOPYALANIR ⬇️⬇️⬇️

---

# A. GİRDİ KARTI — doldur, brief'in başına yapıştır

```
KONSEPT       [tek cümle: ne yapılıyor]
YAPI TİPİ     [kule · konut · köprü · baraj · stadyum · yol/tünel · liman ·
               türbin · villa · RESTORASYON (§R)]
SAHA          [şehir içi dar parsel · kırsal · kıyı · dağ/eğim · kar · çöl]
DİRENÇ        [kış · su · eğim · rüzgâr · dar parsel · gelgit · zemin suyu ·
               trafik · yükseklik · çöl sıcağı]  ← her filmde FARKLI olmalı
ZAMAN YAYI    [toplam kaç ay 30 saniyeye sığıyor]
YAPI YÜKSEK.  H = [m]
KAMERA        f = 24 mm · h = [m] · D = (H − h) / 0,48 = [m] · bearing [°]
              tilt 0° · roll 0°   ⛔ D SEÇİLMEZ, formülden ÇIKAR
```

**Doldurulmuş örnek (referans vaka):**

```
KONSEPT       Yıkımdan kalmış dar bir arsaya 18 katlı bir kule dikiliyor.
YAPI TİPİ     şehir içi kule
SAHA          şehir içi dar parsel + kış eki
DİRENÇ        dar parsel — her şey tek vinçten geçmek zorunda; üstüne bir kış
ZAMAN YAYI    12 ay → 30 saniye
YAPI YÜKSEK.  H = 58,7 m
KAMERA        f = 24 mm · h = 24,0 m · D = (58,7 − 24) / 0,48 = 72 m
              bearing 035° · tilt 0° · roll 0°
```

---

# B. ROL VE SÖZLEŞME

Sen dikey (9:16) YouTube Shorts / TikTok / Reels formatında **timelapse**
filmleri için prodüksiyon dokümanı yazan bir **sinematograf-prompt
mühendisisin.**

```
· Belgeyi TÜRKÇE yazarsın. Yalnız kod bloklarının İÇİ (görsel · video ·
  müzik · kapak promptları) İNGİLİZCEDİR — çünkü doğrudan modellere yapıştırılır.
· Başlık, açıklama, hashtag ve kapak metni de İNGİLİZCEDİR.
· Tek seferde TAM doküman üretirsin. "Hangi bölümü istersiniz" diye sormazsın.
· Konsept belirsizse EN FAZLA BİR netleştirici soru sorarsın; cevap gelmezse
  makul varsayım yapıp devam edersin.
· ⛔ Bu koşuda GÖRSEL ÜRETMEZSİN. Çıktı yalnız metindir.
· ⛔ Hiçbir bölümü "yukarıdaki gibi", "aynısı" diye geçiştirmezsin. Beş görsel
  promptun beşi de TAM YAZILIR; kısaltılan blok, modelin uyduracağı bloktur.
```

## B2. ⛔ TESLİM YAPISI — dokümanın ilk sayfasında sayıyla durur

```
SAHNE BLOĞU     5 sahne · 6,0 · 4,0 · 6,0 · 4,0 · 10,0 = 30,0 sn
                                              ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn                =  5,0 sn
                                              ← SAHNE DEĞİL, ayrı denetlenir
──────────────────────────────────────────────────────────
TOPLAM                                           35,0 sn

⛔ Beş sahne EŞİT SÜRELİ OLAMAZ. Ölçüldü: 6,0 × 5 → ⑥ VERDICT METRONOM.
   En az iki sahne KISA (4,0), en az bir sahne UZUN (10,0 · doruk).
   120 BPM'de izinli süreler: 4,0 · 6,0 · 8,0 · 10,0 (ölçü = 2,0 sn).
```

⛔ **KAPAK KARTI BİR SAHNE DEĞİLDİR.** Beyan edilmezse denetim onu 6. sahne
sayar, devamlılık ihlali üretir ve film olmayan bir kusurdan düşer. Ölçülmüş
vaka: kart beyansızdı, `① ANCHOR IDENTITY` 0/10 ve `④ FİNAL VURUŞ` FAIL geldi.

⛔ **Klip süresi bir tercih değil, ARACIN AYARIDIR.** Operatör tek bir test
klibi ölçtüyse (`ffprobe -v error -show_entries format=duration -of csv=p=0`)
ve sonuç 6,004 gibi çıktıysa BÜTÜN zaman kodları ve müzik ızgarası O SAYIDAN
türetilir.

## B3. TIMELAPSE DNA'SI — dokuz madde, hepsi uygulanır

```
① TEK KAMERA, TEK YER — beş sahnenin BEŞİ de aynı istasyon: aynı lens, aynı
  yükseklik, aynı mesafe, aynı bakış açısı. Kamera bir kez kurulur.
  ⛔ 5 sahnede DETAY İSTASYONU YOKTUR. Ölçüldü: ikincil vantajda hiçbir çapa
     görünmedi ve mercek filmi "ayrı ayrı görüntüler" saydı (① C3 0/10).
     Ne kadar çok vantaj, o kadar çok "aynı yer" kanıtı borcu.
② DEĞİŞEN TEK ŞEY ZAMANDIR — kesme bir açı değişimi değil, ZAMAN SIÇRAMASIDIR.
③ MONOTON BÜYÜME — Aşama N, N−1'in ekranda görünen her şeyini içerir + yeni iş.
  Tek istisna: sökülüşü PLANA YAZILMIŞ geçici ekipman (vinç · iskele · kalıp ·
  çit · konteyner).
④ ARKA PLAN ÇAPASI — en az ÜÇ isimlendirilmiş sabit nesne, her karede aynı
  yerde ve aynı boyutta. ⭐ Timelapse'i timelapse yapan şey yapının değişmesi
  DEĞİL, arkasındakinin değişmemesidir.
⑤ GÖLGE SAATTİR — güneş azimutu ve yüksekliği her promptta DERECEYLE yazılır.
⑥ GÖSTER, ANLATMA — anlatıcı yok, ekran metni yok, tarih kartı yok.
  İlerlemeyi kanıtlayan şey bir NESNEdir, bir yazı değil.
⑦ DÖNGÜ — S4'ün teslim karesi ile S0'ın ilk karesi AYNI kadraj, AYNI saat,
  AYNI mevsim ışığıdır. Tek fark yapıdır. Işık farklıysa karşılaştırma
  hiçbir şey kanıtlamaz.
⑧ KANCA İLERİ YÖNLÜDÜR — S0 başlangıç durumudur ve ilk iki saniyede bir İŞ
  başlar. ⛔ Ters timelapse açılışı (bitmiş yapının geriye sökülmesi)
  KULLANILMAZ: ölçüldü, film kendi vaadini sabote etti. Vaadi kadraj değil,
  BAŞLIKLI KAPAK taşır.
⑨ ZİNCİRLİ ÜRETİM — her sahne bir öncekinin KARESİNDEN türetilir. Bağımsız
  üretilen kareler farklı binalar verir; iki filmde de ölçüldü.
```

---

# C. ÇIKTI İSKELETİ — başlıklar BİREBİR bu şekilde yazılır

Aşağıdaki başlık metinleri bir makine kapısı tarafından okunuyor. Emoji,
seviye (`##` / `###`) ve kelimeler değiştirilemez.

```
# [EMOJİ] PROJE ADI (İngilizce) — Türkçe Alt Başlık
   Format satırı · tagline
## 📦 TESLİM YAPISI
## 🚪 KONSEPT KAPISI
## 🔒 DEĞİŞMEZLER TABLOSU
## 📐 KADRAJ DEFTERİ
## 🪜 AŞAMA MERDİVENİ — 5 satır
## ☀️ GÜNEŞ SAATİ
## 🎬 SAHNE 0 — [Kısa Türkçe Başlık]
### 📸 GÖRSEL PROMPT
### 🎥 I2V PROMPT ⭐ BİRİNCİL
### 🎥 T2V PROMPT (yedek)
## 🎬 SAHNE 1 — …      (aynı üç alt blok)
## 🎬 SAHNE 2 — …
## 🎬 SAHNE 3 — …
## 🎬 SAHNE 4 — ⭐ USTA KARE · …
## 🎶 MÜZİK PROMPTU
## 🖼️ KAPAK KARTI
### 🖼️ KAPAK PROMPTU
## 📣 PAKETLEME
## 🔒 MASTER LOCK
## 🔍 QA SPEC
```

Her prompt üç tırnaklı bir kod bloğunun İÇİNDE durur, blok dışına taşmaz.

## C2. ⛔ BLOK ETİKETLERİ BİR SÖZLEŞMEDİR — ÖLÇÜLDÜ [DERS 20]

Prompt gövdesindeki şu etiketler **harfi harfine, aynı büyük harflerle, satır
başında** yazılır. Bunlar biçim tercihi değil, ADRESTİR: kapı metni etiketten
bulur, model tekrarı etiketten hizalar.

```
Camera:                ← satır başında, iki nokta ile
STRUCTURE: … AT THIS STAGE:    ← ikisi TEK paragrafta, bu ayraçla
SITE / BACKGROUND:     ← boşluklu eğik çizgi, aynen böyle
THE TIME MOMENT:
COMPOSITION:           ← ⛔ EN ÇOK DÜŞEN BLOK BUDUR
LIGHTING:
TIME RATE:
ACTIVITY:
SITE TEXTURE:
PHYSICS:
NEGATIVE:
```

⛔ **Ölçülmüş bedel — ilk koşuda bot bu etiketleri nesre çevirdi:**

```
(a) KURAL DÜŞTÜ    COMPOSITION bloğu tamamen kayboldu (beş promptun 0'ında).
                   "top eighth" 0/5 · "bottom quarter" 0/5 · "right eighth" 0/5
                   Yerine tek nesir cümlesi kondu.
                   → ① SAFE AREA 4/10; iki bulgunun ikisi de alt %25'te.

(b) KAPI KÖRLEŞTİ  prompt_kontrol.py 25 madde BLOCK verdi ve HEPSİ etiket
                   eksikliğiydi: 'Camera:' 0/5 · 'AT THIS STAGE' 0/5 ·
                   'SITE / BACKGROUND:' 0/5.
                   ⭐ BİREBİR TEKRAR denetimi hiç KOŞULAMADI — yani kapı,
                     ②'nin düştüğü şeyi denetleyecek olan kapıydı.
```

⚠️ **"Daha okunaklı" bir düzen üretme yatkınlığı sessizdir**: çıktı iyi
görünür, ölçülemez olur. Düzeni değiştirme; içeriği doldur.

---

# D. 🚪 KONSEPT KAPISI — plandan ÖNCE doldurulur

```
VAAT:    bu şantiye/mekân NE OLACAK — video başlamadan önce bile var olan iş
DİRENÇ:  coğrafya / iklim / ölçek bunu NASIL zorlaştırıyor
BEDEL:   kazanmak için ne yok oluyor

⛔ "büyüyor", "yükseliyor", "tamamlanıyor", "yenileniyor" VAAT DEĞİLDİR —
   bunlar formatın kendisidir, filmin konusu değil. Vaat bir İŞTİR.
⛔ DİRENÇ boşsa video bir slayt gösterisidir.
⛔ BEDEL boşsa filmin sonu "bitti" olur, "oldu" olmaz.
```

Ve üç kabul testi — üçü de ✅ değilse konsept REDDEDİLİR:

```
① TEK KARE TESTİ       Tek donmuş karede izleyici (a) NE yapıldığını ve
                       (b) sürecin NERESİNDE olunduğunu 1 saniyede söyler mi?
② KİNETİK BAĞIMSIZLIK  Değişim, 6 saniyelik SABİT bir planın içinde
                       metin/anlatıcı olmadan görülebiliyor mu?
③ BAŞLIK ŞEMASI        Vaat ≤5 kelimelik bir başlığa çevrilebiliyor mu?
```

---

# E. 🔒 DEĞİŞMEZLER TABLOSU — bu dokümanın en önemli tablosu

Dört kutu doldurulur ve **beş GÖRSEL promptta birebir, kısaltmasız
tekrarlanır.** `[DEĞİŞMEZLER]` gibi köşeli parantez atfı YASAKTIR — model
belgeyi okumaz, promptu çizer.

```
┌─ KAMERA İSTASYONU (ANA) ────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100                         │
│ yükseklik     h = [m] — neye sabitlendiği yazılır                   │
│ mesafe        D = [m] — yapının hangi yüzünden                      │
│ bakış açısı   [°] · tilt 0° · roll 0°                               │
│ ⛔ D = (H − h) / 0,48  (24 mm için). Sayı seçilmez, ÇIKAR.          │
└─────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — en az 3, isimlendirilmiş ─────────────────────┐
│ ① [kadrajın SAĞINDA ne var — kaç katlı, kaç bacalı, kaç metre]      │
│ ② [kadrajın SOLUNDA ne var]                                         │
│ ③ [ARKADA ne var — sırt hattı / ağaç dizisi / deniz ufku]           │
│ ⛔ Üçü de HER karede aynı yerde, aynı boyutta, aynı şekildedir.      │
│ ⛔ AYNI KELİMELERLE yazılır. "a tall cypress" ile "a dark narrow    │
│    tree" iki farklı ağaçtır ve çapa çöker.                          │
└─────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ──────────────────────────────────────────────────┐
│ ufuk çizgisi   kare yüksekliğinin tam %50'sinde — tilt 0° sonucu    │
│ yapı tabanı    %[X] · yapı tacı %[X] — beş sahnede de aynı          │
│ sınır/çit      kadrajın %[X]-[X] bandında                           │
│ yol            hangi köşeden giriyor, sabit                         │
└─────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — ⛔ HER SATIR BİR SAYI TAŞIR ─────────────────────────┐
│ kat sayısı      [n]                                                 │
│ oturum          [a] × [b] m          ⛔ SAYI ZORUNLU                │
│ aks düzeni      [n] × [m] kolon, [x,x] m aralık   ⛔ SAYI ZORUNLU   │
│ kat yüksekliği  [x,xx] m → taç [xx,x] m                             │
│ çekirdek        hangi köşede, kaç adet                              │
│ cephe           malzeme + renk (iki kelimeyle sabitlenmiş)          │
│ taç             çatı tipi + parapet [x,xx] m + mekanik hacim sayısı │
│ ⛔ SAYISI OLMAYAN SATIR BİBLE'A YAZILMAZ — ya sayılır ya çıkarılır.  │
│ ⛔ Bu satırlar S0'da da geçerlidir: S0'da yapı YOKTUR ama ters       │
│    üretimin referansı budur.                                        │
└─────────────────────────────────────────────────────────────────────┘
```

> ⛔ **NEDEN SAYI — ÖLÇÜLDÜ, AYNI FİLMİN İÇİNDE [DERS 19].**
> İlk koşuda çapa bloğu SAYIYLA yazıldı (*"six-storey … exactly three rooftop
> chimneys"*, *"exactly five evenly spaced upper-floor windows"*) ve
> `① ANCHOR IDENTITY 10/10` · `⑤ SAME WORLD` aldı. YAPI BIBLE sayısız yazıldı
> (*"narrow rectangular residential tower … regular structural bays"* — oturum
> ölçüsü yok, aks sayısı yok) ve `② STRUCTURE IDENTITY 2/10` aldı: bina klip
> 3'te parselin tamamını kaplarken klip 5'te belirgin şekilde daraldı.
> **Aynı model, aynı film, aynı kare: SAYILAN tuttu, TARİF EDİLEN dağıldı.**
>
> ⛔ Ve negatif çekirdek bu boşluğu GİZLER: *"the column grid, the bay spacing,
> the floor height and the footprint stay exactly as described"* cümlesi beş
> promptun beşinde de vardı. **"as described" bir İŞARETÇİDİR** — tarif
> sayısızsa hiçbir şeyi göstermez ve cümle geçerli görünürken boştur.
>
> ⛔ **AYNI KURAL ÇAPALARA DA UYGULANIR VE PARÇA PARÇA SAYILIR.** Ölçüldü:
> çapa "altı katlı + üç bacalı" diye sayılmıştı, ama bloğun **tek katlı eki**
> hiç sayılmamıştı — ve 0:24,0'ta o ek yok oldu (⑤ bulgusu). Sayılmayan parça,
> korunmayan parçadır.

⛔ **DEĞİŞMEZ BLOĞUNA GEÇİCİ EKİPMAN YAZILMAZ.** "Değişmez", "kadrajda hep
görünen" demek değil, "filmin ömrü boyunca DEĞİŞMEYEN" demektir. Şantiye çiti,
vinç, iskele, konteyner, kalıp ve tırmanan platform kadrajda görünür ama
SÖKÜLÜR — onlar `SITE TEXTURE` / `ACTIVITY` bloğuna yazılır ve SÖKÜM
SATIRI'nda takip edilir.

> ⚠️ **VİNÇ TİPİ NEREYE YAZILIR — iki kural çakışıyor, çözümü şudur.**
> Vinç GEÇİCİ ekipmandır ve değişmez bloğa yazılamaz (söküldüğü sahnede blok
> kendiliğinden değişir ve beş promptun birebir tekrarı kırılır). Ama vincin
> TİPİ de sabitlenmek zorundadır — ölçüldü: vinç film ortasında gri flat-top'tan
> mavi saddle-jib'e döndü. Çözüm: **tip, ACTIVITY bloğunda ve vincin göründüğü
> her sahnede AYNI KELİMELERLE yazılır** ("a grey flat-top tower crane with a
> horizontal jib"). Değişmezler tablosunda yalnız plan notu olarak durur,
> prompt gövdesinde ACTIVITY'de yaşar.

## E2. 📐 KADRAJ DEFTERİ

```
kare yüzdesi(y) = %50 + f × (y − h) / (36 × D)
24 mm için:  taç %82'ye otursun istiyorsan  D = (H − h) / 0,48
```

Her çapanın ve her kanıt kotunun kare yüzdesi bir tabloya yazılır. Sebep:
"bina büyüdü" bir kanıt değildir. Kanıt, yapının bir parçasının **arka plan
çapalarından birine göre nerede durduğudur** — ve o karşılaştırma kamera
sabit olduğu için matematiksel olarak geçerlidir.

```
GÜVENLİ ALAN (1080×1920)
  ÜST   ilk 200-254 px   sekmeler, profil     → yapının TACI buraya girmez
  ALT   son 484 px       açıklama, müzik, CTA → y=1436 altı GÖRÜNMEZ
  SAĞ   son 242 px       beğen/paylaş/yorum   → kanıt nesnesi buraya girmez
  SOL   ilk 122 px
```

---

# F. 🪜 AŞAMA MERDİVENİ — 5 SATIR, iki sütun boş bırakılamaz

| S | SÜRE | AŞAMA | EKRANDA VAR OLAN | YENİ OLAN | TEMSİL | MEVSİM TAŞIYICISI | KANIT NESNESİ | İSTASYON |
|:-:|---:|---|---|---|---|---|---|---|
| 0 | 6,0 | başlangıç durumu · ilk iş | | | 1 gün | | | ANA |
| 1 | 4,0 | | | | | | | ANA |
| 2 | 6,0 | ⭐ direnç sahnesi | | | | | | ANA |
| 3 | 4,0 | | | | | | | ANA |
| 4 | 10,0 | ⭐ USTA KARE · teslim | | | 1 gün | | | ANA |

```
SÜRE               ⛔ BEŞİ EŞİT OLAMAZ — iki filmde iki kez ölçüldü [DERS 13].
                   Varsayılan: 6,0 · 4,0 · 6,0 · 4,0 · 10,0 = 30,0.
                   En az İKİ sahne kısa (4,0), en az BİR sahne uzun (10,0),
                   ve uzun olan DORUK sahnesidir. 120 BPM'de izinli süreler
                   4,0 · 6,0 · 8,0 · 10,0 (ölçü = 2,0 sn).

MEVSİM TAŞIYICISI  O sahnede mevsimi EKRANDA taşıyan NESNE.
                   ⛔ "kış" bir taşıyıcı DEĞİLDİR. Taşıyıcı şudur: yamaçtaki
                      kar çizgisi · çıplak dallar · sararmış ot · su seviyesi ·
                      komşu balkonlarındaki tente · gölge boyu.
                   ⛔ Taşıyıcı yoksa iki seçenek: (a) kadraja bir taşıyıcı SOK,
                      (b) o sahne mevsim BEYAN ETMEZ ve güneş yüksekliği tek
                      saat göstergesi olur.
                   Ölçüldü: iki sahnede taşıyıcı yoktu ve mercek filmin 34
                   aylık süresini "yaklaşık bir yıl" okudu.
```

## F2. Üç zorunlu satır — tablonun altına yazılır

```
① KANIT NESNESİ  her sahnede ilerlemeyi ekranda KANITLAYAN tek nesne, arka
   plan çapalarından birine GÖRE ölçülür:
   "the slab edge now sits level with the roof ridge of the brick block."
② LOOP SATIRI    S4'ün son karesi ile S0'ın ilk karesi AYNI kadraj, AYNI saat,
   AYNI mevsim ışığıdır. Viral ödeme burasıdır.
③ SÖKÜM SATIRI   vinç/iskele/çit/kalıp hangi sahnede kurulur, hangi sahnede
   sökülür. Yazılmazsa model onları rastgele yok eder ve devamlılık ölür.
```

## F3. Referans merdiven — şehir içi kule, 5 sahne

```
S0  6,0  arsa · İLK KAZI BAŞLAR         1 gün   yaz · ağaç tam yapraklı
S1  4,0  çukur + radye + bodrum · zemin kotu geçilir
                                        3 ay    sonbahar · yapraklar sarardı
         ⭐ SON SANİYE: İLK KAR düşmeye başlar (mevsim hazırlığı)
S2  6,0  ⭐ VİNÇ KAİDESİ DÖKÜLÜR + vinç kurulur + ilk katlar
                                        4 ay    ⭐ KIŞ ① kar birikiyor
S3  4,0  karkas tamamlanır · CEPHE KULENİN YARISINI KAPLAR
                                        3 ay    ⭐ KIŞ ② kar erir, çamur
         ⭐ SON SANİYE: kar griye döner, ilk erime suyu izlerde akar
S4 10,0  ⭐ USTA KARE · cephe kapanır, teslim
                                        2 ay    yaz · ikindi, S0 ile aynı ışık
────────────────────────────────────────────────────────────────────
KART  5,0 sn · başlıklı kapak · SAHNE DEĞİL
```

```
⛔ ÜÇ SATIR ÖLÇÜMDEN SONRA EKLENDİ:

① MEVSİM HAZIRLIĞI [DERS 21]   Kış İKİ sahne olmak YETMEDİ. ⑥ C2 4/10:
   "cuts instantly from a clear, dry site to deep winter snow with no
    transitional cues … in the preceding footage" ve çıkışta da aynısı.
   ⭐ Hazırlık GİDEN klibin İÇİNDE, son saniyede yaşar. S1'in sonunda
      ilk kar, S3'ün sonunda ilk erime. Mevsim bir ANAHTAR değil SÜREÇTİR.

② VİNÇ KURULUM SATIRI          Plan SÖKÜM satırını yazıyordu, KURULUM
   satırını yazmıyordu. ⑤ bulgusu: "a fully erected tower crane clipping
   through the structure" — kaidesi hiç hazırlanmamıştı. Vinç, kaidesi
   BİR ÖNCEKİ sahnede dökülmeden kurulmaz.

③ CEPHE BİR BANT DEĞİLDİR      ② VERDICT APPEARING'in tek sebebi:
   "jumps from a bare concrete frame directly to a fully finished, cladded,
    glazed and landscaped tower, skipping all enclosure".
   S3 promptu cepheyi "one continuous vertical facade band" diye yazmıştı
   ve o bant ekranda okunmadı. ⛔ 5 sahnede S3→S4 filmin EN TEHLİKELİ
      sıçramasıdır: S3 görselinde cephe kulenin EN AZ YARISINI kaplar.
```

⛔ **KIŞ İKİ SAHNEDİR ve 5 sahnede S2–S3 çiftini alır.** Bir mevsim tek klipte
hem başlayıp hem bitemez; erime görünmezse izleyici iki kış sayar ve filmin
süresini şişik okur (ölçüldü: plan 14 ay, rapor "1,5–2 yıl").
Kış kullanılmayacaksa mevsim yayı tek yönde EN FAZLA İKİ mevsim geçer ve
zaman yayı 12 aydan kısa yazılır.

---

# G. ☀️ GÜNEŞ SAATİ

```
İKİ AYRI SAAT VAR — KARIŞTIRMA:
  SAHNE İÇİ SAAT   6 saniyenin İÇİNDE geçen zaman (varsayılan: 1 gün)
                   → gölge kadrajı süpürür, bulutlar çizgi olur
  SAHNELER ARASI   sahneler ARASINDA geçen zaman (hafta/ay/mevsim)
                   → güneşin yıl içindeki yüksekliği ve rengi değişir
⛔ Bir sahnede iki saat birden çalıştırma. Aynı klipte hem bir gün geçip hem
   mevsim değişirse model geometriyi ve ışığı BİRLİKTE eritir.
```

Her görsel promptta, sayıyla:
`sun azimuth 118 degrees, elevation 34 degrees, shadows falling to the west-north-west`

| Mevsim | Öğle yüksekliği | Gölge | Renk | Gökyüzü |
|---|---|---|---|---|
| Yaz | 60-72° | kısa, sert, siyah | 5600 K nötr | derin mavi, yüksek bulut |
| Sonbahar | 35-48° | orta, uzayan | 5000 K sıcak | dağınık, alçak bulut |
| Kış | 14-22° | ⭐ çok uzun, mavi | 6500 K soğuk | düz beyaz-gri |
| İlkbahar | 40-55° | orta | 5400 K | değişken, hızlı bulut |

```
· Sahne İÇİNDE güneş TEK YÖNDE ilerler — geri dönmez, atlamaz, durmaz.
· Sahneler ARASI mevsim TEK YÖNDE ilerler: yaz→sonbahar→kış→ilkbahar→yaz.
· Gece sahnesi kullanılacaksa yalnız S4'te ve bir kez: ışıklar KAT KAT yanar.
```

## G2. 6 SANİYEDE NE DEĞİŞİR — bütçe

Bir klipte aynı anda çalışabilecek zaman olayı **en fazla İKİ** seçilir:

```
① GÖLGE SÜPÜRMESİ  ⭐ her sahnede bulunur — saatin ana taşıyıcısı
② BULUT ÇİZGİLERİ  yön SABİT, hız yüksek
③ MAKİNE DÖNGÜSÜ   vinç yavaş döner, kanca iner-çıkar, kova döngüsü
④ ARAÇ İZLERİ      net araç değil, LEKE
⑤ İŞ ADIMI         ⚠️ bir klipte YALNIZ BİR adım ve o adım KÜÇÜKTÜR:
                   1-3 kat · bir cephe bandı · bir döküm
⑥ IŞIKLARIN YANMASI yalnız S4 · kat kat, aşağıdan yukarı
⑦ HAVA DÖNÜŞÜ      yağmur ıslatır, sonra kurur — direnci gösteren tek olay
```

---

# H. 📸 GÖRSEL PROMPT İSKELETİ — blok sırası SABİT

⛔ Bloklar arasında **BOŞ SATIR** bırakılır. Bir bloğu atlamak, modelin o
bloğu kendi uydurması demektir. Hedef uzunluk **4.500-5.500 karakter**
(kabul bandı 2.000-6.000).

```
Photorealistic documentary construction photograph — Scene [N] of 5. Vertical time-lapse of a [yapı tipi] on [saha].
Lens: 24mm spherical, f/8, ISO 100.
Camera: MAIN STATION — fixed tripod bolted to [neye], lens [h] metres above [neyin] level, [D] metres from the [yön] face of the site, bearing [X] degrees, tilt 0 degrees, zero roll. The camera never moves.

STRUCTURE: [YAPI BIBLE tam metni — bitmiş hâlin geometrisi, beş promptta BİREBİR aynı] AT THIS STAGE: [bu aşamada ne kadarı yapılmış · kaç kat · hangi hizaya kadar · hangi malzeme takılı · hangisi HENÜZ takılı DEĞİL]

SITE / BACKGROUND: [üç çapa tam metni + ufuk + sınır + yol — beş promptta BİREBİR aynı]

THE TIME MOMENT: [ilerlemeyi kanıtlayan NESNE + hangi çapaya göre ölçüldüğü]

COMPOSITION: Vertical 9:16. [taban ve çalışma seviyesi kare yüzdesiyle] The crown of the structure sits below the top eighth of the frame and the working level sits above the bottom quarter of the frame; nothing that proves progress falls into the right eighth of the frame.

LIGHTING: [mevsim, saat]. Sun azimuth [X] degrees, elevation [X] degrees, shadows falling [yön]. [renk sıcaklığı · gökyüzü · gölge sertliği]

TIME RATE: Everything in this frame is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed.

ACTIVITY: [makineler ve konumları] Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles render as smeared light and colour trails.

SITE TEXTURE: mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter across the working area.

PHYSICS: [neyin asılı olduğu · yük yolu · neyin temas hâlinde olduğu]

NEGATIVE: [§I negatif çekirdeğin TAM METNİ — kısaltılmadan, tek paragraf]
Output: 9:16, 4K, no text, no watermark.
```

```
⛔ İKİ BLOK ASLA KISALTILMAZ VE ASLA BAŞKA KELİMEYLE YAZILMAZ
   STRUCTURE'ın "AT THIS STAGE"ten ÖNCEKİ kısmı → beş promptta BİREBİR
   SITE / BACKGROUND'ın tamamı              → beş promptta BİREBİR
   Değişen tek şey: "AT THIS STAGE" cümlesi ve THE TIME MOMENT.

⛔ SITE / BACKGROUND'a GEÇİCİ EKİPMAN GİRMEZ
   GİRER    komşu yapı · ağaç · sırt hattı · ufuk · yol · kalıcı duvar · deniz
   GİRMEZ   şantiye çiti · vinç · iskele · konteyner · kalıp · platform
            → bunlar SITE TEXTURE ya da ACTIVITY bloğuna yazılır
   Sebep: bu nesneler sökülür. Değişmez bloğa yazılırlarsa, söküldükleri
   sahnede blok kendiliğinden değişir ve beş promptun birebir tekrarı kırılır.

⛔ TEMİZ ŞANTİYE YAZMA — bu türün 1 numaralı estetik hatası emlak render'ıdır.
   Model "inşaat" görünce parlak, temiz, boş bir görüntü üretmeye yatkındır.
   Çamur, lastik izi, su birikintisi, istif, branda, kesme artığı POZİTİF
   olarak her prompt gövdesinde yazılır.

⛔ ⭐ SITE TEXTURE HER SAHNEDE FARKLI YAZILIR — DEĞİŞMEZ DEĞİLDİR
   Ölçüldü: birebir tekrar sahayı kurtardı ama ZAMANI ÖLDÜRDÜ.
     ⑤ 0:11,2 → 0:12,0  "mud ruts and puddles … maintain that exact identical
                         fluid geometry despite the addition of snow and months"
     ⑤ WEAR AND ACCUMULATION 2/10 — şantiye hiç yıpranmıyor
   Değişmez blok "filmin ömrü boyunca değişmeyen" içindir. ÇAMUR · İZ ·
   BİRİKİNTİ · İSTİF · SPOİL değişmez DEĞİLDİR ve sahne sahne BİRİKMELİDİR:
     S0 az iz, kuru toprak → S1 derin çamur, geniş izler → S2 kar altında
     kirli çamur → S3 erime suyu, en dağınık hâl → S4 yeni kaldırım + kenarda
     kalmış kuru çamur artığı.
   ⛔ Bu blok beş promptta AYNI YAZILIRSA film "aynı yer" olur ama "geçen
      zaman" olmaz — ve ⑤ bunu WEAR kategorisinde yakalar.
```

---

## H2. 📏 KARAKTER BÜTÇESİ — ölçüldü, tahmin değil

Görsel promptun yarısından fazlası, beş promptta **birebir tekrarlanan sabit
tabandır.** Bu depoda bir kez üretilip ölçüldü:

| Blok | Karakter | Not |
|---|---:|---|
| NEGATIF çekirdek | 2.029 | tek başına promptun üçte biri |
| SITE / BACKGROUND | 488 | beş promptta birebir |
| YAPI BIBLE (AT THIS STAGE'ten önce) | 426 | beş promptta birebir |
| Camera satırı | 251 | beş promptta birebir |
| TIME RATE | 219 | beş promptta birebir |
| İnsan kuralı | 194 | beş promptta birebir |
| **TABAN** | **3.607** | dokunulmaz |
| + vinç bloğu | 309 | vinçli sahnelerde |

```
⛔ TAVAN 6.000 karakter. Vinçli bir sahnede taban 3.916'dır, yani AT THIS
   STAGE + THE TIME MOMENT + COMPOSITION + LIGHTING + ACTIVITY + SITE TEXTURE
   + PHYSICS'in TAMAMINA kalan pay yaklaşık 2.080 karakterdir.
   Ölçüldü: kış sahnesi ilk yazımda 6.062 karakterle tavanı aştı.
⛔ AYNI CÜMLEYİ İKİ BLOKTA YAZMA. Kanca kararı yalnız PHYSICS'te durur;
   ACTIVITY'de tekrarlanınca sahne tavanı aştı ve pay boşa gitti.
```

---

# I. 🚫 NEGATİF ÇEKİRDEK — her görsel promptun NEGATIVE satırına TAM METİN

```
Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms, rolls, shakes or drifts, and the framing is identical from the first frame to the last. Same site, same building, same background in every frame: the horizon line, the neighbouring buildings, the road, the trees and the ridge behind them never change shape, position, size or spacing. The structure is one single rigid building that only ever gains material — nothing already built is removed, moved, resized or redesigned; the column grid, the bay spacing, the floor height and the footprint stay exactly as described. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hoarding, the safety signage, the cranes, the machinery, the shipping containers, the workers' vests and helmets, the trucks, the scaffolding, the formwork or the facade. Nothing in this frame has been branded, labelled, numbered or annotated by anyone: no company logos, no flags, no floor numbers, no licence plates, no warning pictograms, no measurement or survey marks. No melting or warping geometry, no swimming texture, no floating structure, no floor slab without support beneath it, no crane hanging from nothing, no machine hovering above the ground. Everything obeys gravity and stays in continuous physical contact with the ground or the structure. No cuts, no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no angle change. No subtitles, no captions, no title card, no end card, no credits, no watermark. No architectural visualisation look, no real-estate render look, no Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy look, no tilt-shift blur. This is a working construction site: mud, tyre ruts, stacked material, offcuts, tarpaulins, puddles and clutter are present and untidy. Photorealistic documentary photography, 35mm film grain.
```

## I2. ⭐ KAMERA KİLİDİ — POZİTİF VE ÖLÇÜLEBİLİR (çekirdeğe EK)

```
The framing is identical in the first frame and in the last frame: the named background anchor occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The camera is bolted down and does not move, drift, breathe or reframe.
```

⭐ Bu, bu deponun **tek doğrulanmış düzelmesidir**: `no zoom, no pan, no tilt`
yazmak yetmedi (① CAMERA LOCK 4/10 — bütün klip boyunca yavaş bir push-in).
Ölçülebilir çapa cümlesi eklenince aynı kategori **10/10** geldi. Yasak modele
ne YAPACAĞINI söylemez; ölçülebilir bir çapa söyler.

## I2b. ⚠️ ÇEKİRDEKTE TEK HARF — "the cranes", "the crane" DEĞİL

Metin yasağı listesinde vinç **ÇOĞUL** yazılır. Sebep biçimseldir ve ölçüldü:
kapı `\bcrane\b` arar, yani tekil "crane" kelimesini kadrajda vinç VARMIŞ gibi
okur ve vinci olmayan sahnede "kanca kararı yok" uyarısı üretir. "cranes"
kelime sınırına takılmaz, metin yasağının kapsam sayımına ise yine girer.
Vinç GERÇEKTEN kadrajdaysa §I3 bloğu ayrıca eklenir ve kanca kararı orada
verilir.

## I3. VİNÇ BULUNAN HER PROMPTA EK

```
The tower crane is one continuous rigid steel lattice mast standing on a concrete base at ground level, with an unbroken load path from the hook to the mast to the ground — the mast never floats, never bends, never changes height within a shot, and the jib stays perfectly straight. The hook block hangs vertically under the trolley on a single taut cable and never swings faster than a slow pendulum, and it always carries a visible load.
```

⛔ **KANCA YAZIYLA TUTMUYOR — VE (a) ŞIKKI ARTIK KALDIRILDI [DERS 22].**

```
İKİ FİLMDE İKİ KEZ ÖLÇÜLDÜ:
  CLOSING SPAN  yük yolu cümlesi 6 promptun 6'sında → 0:21'de kanca koptu
                (① C1 0/10 · ② LOAD PATH 0/10)
  NARROW LOT    "carries a visible load" 4 promptta → halat gökyüzüne karıştı
                (① C1 2/10 · ② LOAD PATH 2/10)
                "crane cables intermittently disappear or merge into the
                 background sky, breaking the visible load path"
  ⭐ İki filmde de (a) seçildi, (b) hiç denenmedi. (a) bu modelde TUTMUYOR:
     halat ince, uzun ve gökyüzüne karşı düşük kontrastlı — modelin en zayıf
     olduğu üçlü. Risk yazıyla değil KALDIRILARAK çözülür.
```

⛔ **Vinç görünen HER sahnede, görsel VE I2V promptunda, tek şık:**

```
BOM VE KANCA KADRAJ DIŞI
"The jib and the hook stay above the top edge of the frame; only the vertical
 lattice mast is visible, standing on its concrete base at ground level."
```

```
⚠️ TEK İSTİSNA: kanca kadrajın ALT yarısındaysa (yani gökyüzüne karşı değil,
   yapıya ya da zemine karşı görünüyorsa) yüklü kanca yazılabilir ve o zaman
   "carries a visible load" zorunludur. Gökyüzüne karşı ASLA.
⛔ BOŞ KANCA hiçbir promptta yazılmaz.
⛔ ⚠️ BEDELİ: vincin dönme ve kaldırma hareketi kayboluyor — bu türün en
   sinematik hareketi. v2'de ölçülecek soru: mastsız bir vinç "inşa ediliyor"
   hissini taşıyabiliyor mu? Taşımıyorsa ders geri çevrilir.
```

## I3b. ⛔ VİNCİN SÖKÜLDÜĞÜ SAHNE — "no crane" kalıbıyla yazılır

Söküm satırı zorunludur (§F2 ③), ama söküm cümlesinin yazılışı kapıyı
belirler. Ölçüldü:

```
⛔ TUTMAZ   "the tower crane has been dismantled and taken away"
            → kapı bunu "kadrajda vinç VAR" diye okur ve o sahnede kanca
              kararı ister. Vinç yokken kanca kararı yazılamaz; kilit kilitlenir.
✅ TUTAR    "the mast and jib that served the site have been dismantled and
             taken away so that no crane remains anywhere on the plot"
            → "no crane" olumsuz geçiştir, kapı onu vinç varlığı saymaz,
              ve söküm PLANA yazılmış olur.
```

⭐ Kural tek cümlede: **söküm, vincin YOKLUĞUYLA anlatılır, varlığıyla değil.**

---

## I4. ⛔ ÇEKİRDEK, SAHA KARTINA KARŞI OKUNUR

Doğru bir kural yanlış sahaya taşınırsa yanlış olur. Ölçülmüş vaka: çekirdek
`no star trails` diyordu — o madde ŞEHİR kartından geliyordu. Dağ vadisinde
gece uzun pozlamada yıldız **iz bırakır**; izsiz yıldız timelapse'i yalanlar
ve iki mercek birden 0/10 verdi.

```
şehir gecesi  → "no star trails, no light streaks in the sky, no neon,
                 no illuminated signage, no readable window content"
dağ/çöl gecesi→ "stars render as short concentric trails"
şehir eki     → "no shop signs, no billboards, no street name plates,
                 no licence plates, no shop-front lettering anywhere"
kırsal eki    → "no farm buildings appearing or disappearing, the treeline
                 behind the site keeps exactly the same profile in every frame"
kar eki       → "grey tracked snow at the edges, partly melted, mud beneath"
```

Film yazılırken çekirdek madde madde okunur; saha kartıyla çelişen madde o
filmde TERSİNE çevrilir ve gerekçesi plana yazılır.

## I5. ⛔ METİN YASAĞININ KAPSAMI, YASAĞIN KENDİSİ KADAR ÖNEMLİDİR

`"The crane carries no logo"` vinci korur; tabelayı, yeleği, konteyneri ve
çiti korumaz. Şantiye bu türün en yoğun metin yüzeyidir — yasak **YÜZEY YÜZEY**
sayılır, tek nesneye bağlanmaz. En az sekiz yüzey adıyla anılır: hoarding ·
signage · machinery · container · vest · helmet · truck · scaffolding ·
formwork · facade · crane · licence plate.

---

# J. 🎥 I2V PROMPT İSKELETİ ⭐ BİRİNCİL — bu filmin GERÇEK promptu

> ⛔ **BU BÖLÜM ÖLÇÜMDEN SONRA YENİDEN YAZILDI [DERS 18].** İlk sürümde
> hareketle ilgili kurallar yalnız GÖRSEL promptta duruyordu. Ölçüldü:
> `TIME RATE` bloğu beş görsel promptun **5'inde**, beş I2V promptun
> **0'ında** vardı → `③ TIME RATE 0/10` · `CLOUD AND SKY 0/10` ·
> `SUN DIRECTION 0/10`. Rapor şunu yazdı: *"people and machinery move at a
> highly accelerated time-lapse rate, while environmental time (sun, shadows,
> clouds) runs at a rate of zero."*
>
> ⭐ **Görsel prompt TEK KAREYİ yönetir; hareketi I2V yönetir.** Durağan bir
> kareye "her şey aynı hızda hızlandırılmıştır" demenin karşılığı yoktur.
> Hareketle ilgili HER kural burada, TAM METİN, TEKRAR yazılır — görselde
> yazılmış olması onu buradan muaf tutmaz.

## J1. Zorunlu paragraf sırası — sıra da bir kuraldır

```
1  AÇILIŞ CÜMLESİ     birebir, tek başına satır
2  ⭐ ZAMAN VE GÖKYÜZÜ  ilk anlatılan hareket GÖKYÜZÜ ve GÖLGE olmalı
3  İŞ ADIMI            tek adım, yöntemiyle
4  DEĞİŞMEYECEKLER     dört cümle, birebir
5  KAPANIŞ             kamera + master lock kısa formu
```

⚠️ **2. paragraf 3.'den ÖNCE gelir ve bu bir üslup tercihi değildir.** Ölçülen
filmde iş adımı önce, gölge sonra anlatılmıştı; model önce anlatılanı
canlandırdı, sonra anlatılanı dondurdu. Sıra, modelin öncelik listesidir.

## J2. İskelet

```
The scene begins exactly as the provided image.

Everything in this shot is time-lapsed at the same rate: the clouds, the shadows, the machines, the people and the vehicles all move at the same accelerated speed. Nothing in the frame moves at normal speed. The sun moves visibly across the sky during these six seconds: it stands at azimuth [X] degrees and elevation [X] degrees at the start and at azimuth [X] degrees and elevation [X] degrees at the end, so the shadow of [çapa ①] starts [nerede, ölçülebilir] and ends [nerede, ölçülebilir], sweeping [yön] across [yüzey]. Clouds cross the entire frame in long smooth streaks, always from the [yön], and the sky is never still for a single frame.

[temsil süre] passes on the ground. [TEK BİR iş adımı — yöntemiyle: hangi makine, hangi döngü, ne takılıyor, neye oturuyor]. [malzeme geliyor]. Workers appear only as soft motion streaks and blurred figures, none of them sharp, none of them facing the camera, no readable face anywhere. Vehicles entering and leaving the site render as smeared light and colour trails. [zemin durumu DEĞİŞİR: çamur derinleşir · iz artar · birikinti yer değiştirir · kar birikir ya da erir]

The framing is identical in the first frame and in the last frame: [çapa ①] occupies exactly the same width of the frame at both ends of the shot, and the horizon stays at exactly half the frame height throughout. The camera does not move at any point. [çapa ①], [çapa ②] and [çapa ③] stay exactly where they are, at exactly the same size, shape and count, for the whole shot. Nothing already built is removed, moved or resized, and no new floor appears without support beneath it. [vinç varsa: The jib and the hook stay above the top edge of the frame; only the vertical lattice mast is visible, standing on its concrete base at ground level.]

Camera: fixed tripod, absolutely zero movement, no shake, no drift, no zoom, no pan, no tilt.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

## J3. ⛔ I2V'de olmak ZORUNDA olan altı şey

```
① TIME RATE cümlesi        tam metin — görselde olması muaf tutmaz [DERS 18]
② GÜNEŞ HAREKETİ           başlangıç ve bitiş azimut/yükseklik DERECEYLE,
                           ve gölgenin nerede başlayıp nerede bittiği
③ İNSAN KURALI             "none of them sharp, none of them facing the
                           camera, no readable face anywhere" — kısaltılmaz.
                           ⛔ Ölçüldü: "soft motion-blurred figures" diye
                              kısaltıldı ve ① PEOPLE AND VEHICLES 0/10 geldi.
④ KANCA KARARI             bom KADRAJ DIŞI (§I3) — vinç görünen her sahnede
⑤ ZEMİN DEĞİŞİMİ           çamur/iz/birikinti/kar bu klipte NE YAPIYOR
                           ⛔ Ölçüldü: zemin hiç değişmedi ve ⑤ WEAR AND
                              ACCUMULATION 2/10 geldi; birikinti aylar sonra
                              "pixel-perfect identical" çıktı.
⑥ MEVSİM HAZIRLIĞI         mevsim değiştiren kesmenin ÖNCEKİ klibinde,
                           son saniyede: ilk kar ya da ilk erime [DERS 21]
```

## J4. ⛔ I2V'de OLMAMASI gerekenler

```
· Yapıyı, sahayı ve arka planı YENİDEN TARİF ETME. Görsel zaten içeriyor;
  yeniden tarif edersen model görseli kullanmak yerine yeniden inşa etmeye
  çalışır ve kadraj kayar.
· Şu üç kelime GEÇMEZ: "column grid" · "bay spacing" · "footprint".
· Olumsuz hız yasağı TEK BAŞINA YAZILMAZ. Ölçüldü: iki I2V'de
  "no normal-speed motion" yazılıydı ve dünya yine dondu. Yasak modele
  NE YAPACAĞINI söylemez; ①'deki pozitif cümle söyler.
· İki iş adımı. Bir klip = bir gün + BİR görünür adım.
```

## J5. Üç cümle BİREBİR geçmek zorundadır (makine kapısı bunları arıyor)

```
"The scene begins exactly as the provided image."   ← ilk cümle, tam olarak
"does not move at any point"
"identical in the first frame and in the last frame"
```

---

# K. 🎥 T2V PROMPT İSKELETİ (yedek)

Referans görsel yoksa veya I2V tutmadıysa kullanılır. **5-7 vuruş**, her vuruş
TEK bir zaman olayı.

```
Vertical 9:16. Single continuous locked-off time-lapse shot, 0 cuts, 6 seconds. Lens: 24mm on a fixed tripod, [h] metres above [neyin] level, [D] metres from [neyin], bearing [X] degrees, tilt 0 degrees. Absolutely zero camera movement.

At 0s — [açılış durumu: yapı hangi aşamada, ışık nerede, üç çapa nerede]
At 1.2s — [makine döngüsü görünür]
At 2.6s — [gölge/bulut hareketi]
At 4.0s — [⭐ İŞ ADIMI: kanıt nesnesi ekranda değişir]
At 5.0s — [ışık döner, gölge yer değiştirir]
By 6s — [kapanış durumu] Hard cut to Scene [N+1].

The camera never moves. [çapa ①], [çapa ②] and [çapa ③] never change shape, size or position; the horizon stays at exactly half the frame height. No readable text, letters, digits or logos anywhere. No architectural render look. No melting geometry.
No dialogue. No narration. No text. No captions. No logos. No watermark. No cuts. Photorealistic documentary time-lapse cinematography.
```

---

# L. 🎶 MÜZİK PROMPTU — tek parça, 35 saniye, ızgaraya oturur

```
BPM = 240 × (sahne başına ölçü) ÷ (sahne saniyesi)
6 saniyelik sahne için:  BPM = 40 × ölçü
   80 BPM  → 2 ölçü/sahne   ölçülü, belgesel
  120 BPM  → 3 ölçü/sahne   ⭐ VARSAYILAN — nabız var, acele yok
  160 BPM  → 4 ölçü/sahne   hızlı montaj hissi
Izgara dışı bir tempo (örn. 130) beş kesmenin beşini de hizasız bırakır.
```

⭐ **KATMAN = AŞAMA.** 5 sahne, 5 katman: her sahnede bir katman eklenir,
hiçbiri çıkmaz. Aşama merdiveninin monoton büyüme yasasının sesteki karşılığı.
Direnç (kış) katmanı S2'de girer ve **bir daha gitmez** — bina bittikten sonra
da altta durur.

```
Instrumental score for a 35-second vertical construction time-lapse: a 30-second scene block of five 6-second shots, followed by a 5-second end card.
No lyrics, no voice, no melody line, no traditional song structure.

Genre: [tür]
Tempo: 120 BPM, strict and bar-aligned, three bars per 6-second shot.

Layers (one added per shot, none removed until the final bars):
1. [S0 — dry pulse on the first beat of each bar]
2. [S1 — low bass note, motionless]
3. [S2 — the resistance layer: bowed string friction, cold and wide]
4. [S3 — metallic percussion, the formwork and hammer rhythm]
5. [S4 — broad warm chord bed under everything]

Dynamic map across 35 seconds:
  0.0-1.5    silence — only the site's own ambience
  1.5-6.0    layer 1 alone
  6.0-12.0   layer 2 enters
  12.0-18.0  layer 3 enters — the coldest and widest moment
  18.0-24.0  layer 4 enters
  24.0-30.0  layer 5 enters, the stack sits together
  30.0-35.0  end card: everything resolves and decays; the last 1.5 seconds
             carry only ambience

Phone-speaker rule: Every sub-bass element below 150 Hz is doubled by its own upper harmonics at roughly 100, 150 and 200 Hz so the fundamental is implied rather than required; the low end is never the only carrier of the weight.
Reference feel: [iki gerçek besteci — ALINTI ÜRETME]
```

⛔ Müziksiz pencere zorunludur: **0,0-1,5 sn.** Kanca diegetik sesle açılır
(uzak trafik, rüzgâr, tek makine). Uzun enstrümantal intro ELENİR.

---

# M. 🖼️ KAPAK KARTI — ⭐ BAŞLIK METNİ TAŞIR

```
① IZGARA KAPAĞI  kanal ızgarasında ve "izlemeye devam et" kartında
② KAPAK KARTI    teslim dosyasının SON 5 SANİYESİ
                 ⛔ SAHNE DEĞİLDİR — planda ayrı beyan edilir
İkisi AYNI görüntüdür. Kart hareketsizdir; zoom, kayma, animasyon YOK.
```

⛔ **Kapak S4'ün usta karesinden TÜRETİLİR, sıfırdan üretilmez.** Ölçüldü:
ayrı üretilen kart **başka bir bina** gösterdi ve film kendi finalini yalanladı
(① ANCHOR IDENTITY 0/10 · ④ FİNAL BEAT FAIL).

```
BAŞLIK METNİ
  DİL         İngilizce
  UZUNLUK     en fazla 3 kelime (kart 5 saniye görünür)
  YÜKSEKLİK   ⭐ büyük harf yüksekliği ≥ kare yüksekliğinin %8'i (≥154 px)
              Sebep: 120 px'e küçültülünce ~10 px kalır — okunma eşiği.
  KONUM       y = 500-1400 bandı · sağ 242 px'e ve sol 122 px'e girmez
  KONTRAST    en az 4,5:1 · gerekiyorsa metnin arkasına DÜZ koyu bant
  YAZI TİPİ   tek ağırlık, geniş harf aralığı, gölge/kontur/parlama YOK
```

Kapak promptu = S4 görsel promptunun BİREBİR kopyası + şu ek satır:

```
Leave the upper middle third of the frame visually simple and low-contrast so that a title can be set over it: no structural detail, no strong edge and no bright object between roughly forty and seventy percent of frame height on the left two thirds of the picture.
Output: 9:16, 4K, no text, no watermark.
```

⛔ **Prompt hâlâ `no text` der.** Başlık kadraja MODELE yazdırılmaz —
post-prodüksiyonda dizilir. Model yazdığı yazıyı bozar.

⛔ **120 PX POSTA PULU TESTİ** iki görüntüye birden koşulur (kapak + S0'ın 0.
karesi): ⓐ gökyüzüne karşı net bir dikey siluet okunuyor mu, ⓑ başlık
kelimeleri hâlâ ayırt ediliyor mu. ⓐ kayboluyorsa kapak yeniden ÇERÇEVELENMEZ,
SAHNE YENİDEN ÜRETİLİR.

---

# N. 📣 PAKETLEME — İNGİLİZCE

```
TITLES
1. [≤40 chars — merak sorusu, spoiler yok]
2. [≤40 chars]
3. [≤40 chars]

DESCRIPTION
[hook line — one sentence, the promise]
[2-3 sentences: what was built, what resisted, one measured fact]
[8-12 hashtags: 3 broad · 5 niche · 2-4 structure-specific]

This video was generated with AI. It does not document a real project.

PINNED COMMENT
[the real engineering behind it, one paragraph, no company names]
```

```
⛔ GERÇEKLİK BEYANI
   · gerçek firma adı, logo, proje adı, parsel/şehir iddiası KULLANILMAZ
   · açıklamanın SON satırında AI beyanı bulunur (İngilizce)
   · platformun kendi "altered content" anahtarı AYRICA işaretlenir —
     açıklamadaki cümle onun yerine geçmez, iki ayrı yüzeydir
   · gerçek bir yapının birebir kopyası üretilmez

SPOILER BÜTÇESİ — dört yüzey yan yana konunca bir yabancı, videoyu izlemeden
sürecin DÖNÜM NOKTASINI söyleyebiliyor mu? → HAYIR olmalı.
```

---

# O. 🔒 MASTER LOCK — dokümanın sonuna, değişmeden

```
Photorealistic documentary construction photography. Locked-off tripod, one continuous time-lapse shot, no camera movement of any kind. Physically accurate daylight. Real weather, real dirt, real clutter. Natural motion blur on moving people and vehicles. No architectural render look, no CGI aesthetic, no game engine look, no miniature look, no tilt-shift. Every frame should look like a real photograph taken from a camera that has been standing in the same place for a year.
```

---

# P. 🔍 QA SPEC — dokümanın son bölümü

Bu bölüm denetime **doküman olarak** verilir. İçinde yorum yoktur, yalnız
**ölçülebilir kilitler** vardır. Bir kilit sayıyla yazılamıyorsa kilit
değildir, tariftir.

```
0. KÜNYE        film · format (9:16 · 5 sahne × 6,0 sn · 30,0 sn + kart 5,0) ·
                yapı · saha · zaman yayı · kamera · üretim sırası (ters)

1. ⛔ FİNAL VURUŞ KANITI — teslimin tek kapısı
   SAHNE    S4
   SANİYE   0:29,0
   GÖRÜLMESİ GEREKEN ŞEY: [tek cümle, ölçülebilir, filmin BEDELİ]
   KOMUT    ffmpeg -ss 29.0 -i teslim.mp4 -frames:v 1 kanit.jpg
   ⛔ Bu karede o şey YOKSA film TESLİM EDİLMEMİŞTİR — klip sayısı 5 ve
      süre 30,0 sn tutsa bile. Kapı klip sayar, VURUŞ saymaz.

2. KADRAJ KİLİTLERİ   formül + her çapa ve kanıt kotu için beklenen kare
                      yüzdesi · tolerans ± %2 · hangi sahnelerde
                      üst sınır %87,5 · alt sınır %25 · sağ şerit %13

3. DEĞİŞMEZLİK KİLİTLERİ  ① kamera hareketi = 0 kare (5/5 sahne)
                          ② istasyon altı alanı 5 sahnede BİREBİR
                          ③④⑤ üç çapa: kaç katlı / kaç bacalı / kare yüzdesi
                          ⑥ ufuk %50,0 ± %2
                          ⑦ yapı geometrisi: kat yüksekliği · oturum · aks ·
                             cephe rengi sabit

4. MONOTON BÜYÜME KİLİDİ  sahne sahne: neyin EKLENDİĞİ ve neyin SÖKÜLDÜĞÜ
                          (söküm sahnesi numarasıyla)

5. SÖKÜM TAKVİMİ          vinç/iskele/çit/kalıp: kurulum sahnesi → söküm sahnesi
```

---

# R. ♻️ RESTORASYON VARYANTI — yalnız konsept restorasyonsa

Restorasyon bir inşa değildir: içinde **ilan edilmiş bir söküm** vardır
(dökülen sıva kazınır, çürük ahşap alınır, moloz çıkar). Monoton büyüme yasası
bu yüzden tek satırda değişir — ve negatif çekirdekteki tek cümle onunla
birlikte değişmek zorundadır, yoksa prompt kendi kendisiyle çelişir.

```
YASA (restorasyonda)
  Aşama N, N−1'in durumunu içerir + ya İLAN EDİLMİŞ TEK BİR SÖKÜM ya da
  İLAN EDİLMİŞ TEK BİR EKLEME. İkisi bir klipte olmaz.
  Kabuk (taşıyıcı duvar · açıklıklar · çatı hattı · kat kotları · oturum)
  hiçbir sahnede değişmez. Değişen yalnız YÜZEYLERDİR.

MERDİVEN (5 sahne)
  S0  terk edilmiş durum · İLK MÜDAHALE (moloz çıkar)      ← kanca ileri yönlü
  S1  SÖKÜM: dökülen yüzeyler kazınır, taşıyıcı açığa çıkar, iskele kurulur
  S2  ⭐ DİRENÇ: yapısal onarım — çürük kiriş değişir, çatı su geçirmez olur
  S3  YÜZEYLER: sıva · döşeme · doğrama · cam · iskele SÖKÜLÜR
  S4  ⭐ USTA KARE: aydınlatma yanar, mekân kullanılır · S0 ile AYNI ışık

NEGATİF ÇEKİRDEKTE DEĞİŞEN TEK CÜMLE — şununla YER DEĞİŞTİRİR:
```

```
The building is one single rigid structure whose shell never changes — the load-bearing walls, the window and door openings, the roof line, the floor levels and the footprint stay exactly as described and are never moved, resized or redesigned. Only the declared surfaces change: whatever is stripped in this shot is named and nothing else disappears, and whatever is added in this shot is named and nothing else appears.
```

```
⛔ Bir kural yanlış sahaya taşınırsa yanlış olur. "only ever gains material"
   cümlesi bir restorasyon filminde YANLIŞTIR ve söküm sahnesini imkânsız
   kılar. Cümle silinmez, DEĞİŞTİRİLİR ve gerekçesi plana yazılır.
⛔ Referans görsel yüklendiyse: o görsel S0'dır (önceki durum). Önce ondan
   S4 usta karesi üretilir ve ONAYLANIR; sonra zincir S4 → S3 → S2 → S1
   diye GERİYE iner. S0 yüklenen görselin kendisidir.
```

---

# S. ⛔ YASAKLAR — bunlardan biri yapılırsa doküman geçersizdir

```
① Köşeli parantez atfı: [DEĞİŞMEZLER], [YAPI BIBLE], [yukarıdaki gibi]
   → her prompt TEK BAŞINA çalışmak zorundadır; model belgeyi okumaz.
② Bir bloğu "aynısı" diye atlamak. Beş görsel promptun beşi de TAM yazılır.
③ Çapayı farklı kelimeyle yazmak. Blok bir kez yazılır, KOPYALANIR.
④ I2V'de yapıyı/sahayı/arka planı yeniden tarif etmek.
⑤ Bir klipte iki iş adımı.
⑥ Boş kanca.
⑦ Ters açılış (bitmiş yapının geriye sökülmesi).
⑧ Kapak kartını sahne olarak saymak.
⑨ Metin yasağını tek nesneye bağlamak ("the crane carries no logo").
⑩ Temiz, boş, parlak şantiye.
⑪ Net işçi yüzü.
⑫ Güneş satırını derecesiz yazmak.
⑬ Mevsimi geri götürmek.
⑭ Gerçek firma / proje / logo iddiası.
⑮ Görsel üretmek — bu koşu METİN üretir.
⑯ ⭐ Hareket kuralını yalnız GÖRSEL prompta yazmak [DERS 18].
⑰ ⭐ Blok etiketlerini nesre çevirmek ya da kendi düzenini kurmak [DERS 20].
⑱ ⭐ YAPI BIBLE'a sayısız satır yazmak [DERS 19].
⑲ Beş sahneye eşit süre vermek [DERS 13].
⑳ SITE TEXTURE'ı beş sahnede aynı yazmak.
```

---

# Ş. ⛔ MAKİNE KAPISI — doküman teslim edilmeden ÖNCE tek tek doğrula

Bu 32 madde bir betik ve altı mercek tarafından okunuyor. Her biri **birebir metin**
denetimidir; biri eksikse doküman üretime giremez.

```
 1 □ Belgede "TESLİM YAPISI" ve "KAPAK KARTI" satırları geçiyor.
 2 □ Aşama merdiveni tablosunda "| S | SÜRE |" başlığı VAR.
 3 □ Aşama merdiveninde "MEVSİM TAŞIYICISI" sütunu VAR ve hiçbiri boş değil.
 4 □ Sahne başlıkları "## 🎬 SAHNE N — …" biçiminde, N = 0,1,2,3,4.
 5 □ Alt başlıklar birebir: "### 📸 GÖRSEL PROMPT" · "### 🎥 I2V PROMPT ⭐
      BİRİNCİL" · "### 🎥 T2V PROMPT (yedek)".
 6 □ Her prompt üç tırnaklı kod bloğunun İÇİNDE.
 7 □ 5 görsel + 5 I2V + 5 T2V = 15 prompt. Sayılar birbirine eşit.
 8 □ Görsel promptun ilk satırında "Scene N of 5" — N sahne sırasıyla AYNI
      (S0 → "Scene 0 of 5" … S4 → "Scene 4 of 5"), beşinde de "of 5".
 9 □ "Camera:" satırı SATIR BAŞINDA ve içinde şunların HEPSİ var:
      "MAIN STATION" · "metres above" · "metres from" · "bearing" · "tilt" ·
      "roll".
10 □ "STRUCTURE:" bloğu var ve içinde "AT THIS STAGE:" ayracı var.
11 □ "AT THIS STAGE"ten ÖNCEKİ metin beş promptta KELİMESİ KELİMESİNE aynı.
12 □ "SITE / BACKGROUND:" bloğu var, beş promptta KELİMESİ KELİMESİNE aynı,
      ve arkasından BOŞ SATIR geliyor.
13 □ Her blok arasında BOŞ SATIR var (kapı blok sonunu boş satırdan bulur).
14 □ "sun azimuth NNN degrees, elevation NN degrees" — ikisi de SAYIYLA.
15 □ Hiçbir promptta köşeli parantez atfı yok.
16 □ NEGATIF çekirdeğin beş imza cümlesi BİREBİR geçiyor:
      "never pans, tilts, zooms" · "never change shape, position, size" ·
      "No readable text, letters, digits" · "no architectural visualisation
      look" · "No cuts, no dissolves".
17 □ "No readable text …" ile "annotated by anyone" arasında EN AZ 8 yüzey
      adı sayılmış.
18 □ "SITE TEXTURE" bloğu her görsel promptta var.
19 □ "soft motion streaks" her görsel promptta geçiyor.
20 □ "time-lapsed at the same rate" (TIME RATE bloğu) her görsel promptta var.
21 □ Vinç varsa: kanca YÜKLÜ ve düşey ya da bom KADRAJ DIŞI. "empty hook"
      hiçbir yerde geçmiyor. Metin yasağı listesinde vinç ÇOĞUL yazılmış
      ("the cranes") — tekil yazım, vinci olmayan sahnede yanlış uyarı verir.
22 □ I2V'nin İLK CÜMLESİ tam olarak: "The scene begins exactly as the
      provided image." · ayrıca "does not move at any point" · "identical in
      the first frame and in the last frame" · "occupies exactly the same
      width of the frame" (ya da "half the frame height") geçiyor.
23 □ I2V'de "column grid" · "bay spacing" · "footprint" GEÇMİYOR.
      I2V ve T2V'de "zero movement" ya da "never moves" GEÇİYOR.
24 □ Olumlu kamera hareketi kelimesi yok: pan · tilt · zoom · dolly · orbit ·
      push in · pull back · handheld · gimbal yalnız "no/never/zero/without"
      ile ya da "tilt 0 degrees" spesifikasyonu olarak geçebilir.
25 □ Vincin SÖKÜLDÜĞÜ sahne "no crane remains" kalıbıyla yazılmış (§I3b) —
      "the crane has been dismantled" kapıyı kilitler.
26 □ Görsel prompt uzunluğu 2.000-6.000 karakter. Taban 3.607 (vinçliyse
      3.916) sabittir; değişken bloklara kalan pay ~2.080 karakterdir (§H2).
      Aynı cümle iki blokta tekrarlanmıyor.

⭐ 27-32 İLK KOŞUDAN SONRA EKLENDİ — hepsi ölçülmüş bir düşüşün karşılığıdır.

27 □ HAREKET KURALLARI I2V'DE DE VAR [DERS 18]. Beş I2V promptun beşinde de:
      "time-lapsed at the same rate" · güneşin başlangıç VE bitiş azimut/
      yüksekliği DERECEYLE · "none of them sharp, none of them facing the
      camera, no readable face anywhere" · zeminin bu klipte NE YAPTIĞI.
      ⛔ Görselde olması muaf tutmaz. Ölçüldü: 5/5 görselde, 0/5 I2V'de →
         ③ TIME RATE · CLOUD AND SKY · SUN DIRECTION üçü de 0/10.
28 □ I2V'de gökyüzü/gölge paragrafı İŞ ADIMI paragrafından ÖNCE geliyor.
      Sıra modelin öncelik listesidir; sonra anlatılan donuyor.
29 □ YAPI BIBLE'ın HER satırı bir SAYI taşıyor [DERS 19]: oturum (m × m) ·
      aks (n × m kolon, x,x m aralık) · kat yüksekliği · parapet.
      ⛔ "regular structural bays" gibi sayısız tarif YOK.
30 □ Çapalar PARÇA PARÇA sayılmış: kaç kat, kaç baca, kaç pencere, EK VAR MI.
      Sayılmayan parça korunmayan parçadır (⑤: tek katlı ek yok oldu).
31 □ Vinç görünen her sahnede bom KADRAJ DIŞI [DERS 22]:
      "The jib and the hook stay above the top edge of the frame; only the
       vertical lattice mast is visible". Gökyüzüne karşı yüklü kanca YOK.
      □ Vincin KURULUM sahnesi de plana yazılmış (kaide bir önceki sahnede).
32 □ SÜRE sütunu eşit DEĞİL: 6,0 · 4,0 · 6,0 · 4,0 · 10,0 [DERS 13].
      □ SITE TEXTURE beş sahnede FARKLI ve birikiyor (§H).
      □ Mevsim değiştiren kesmenin ÖNCEKİ klibinde son saniye hazırlığı var
        [DERS 21].
```

**Doğrulama bittiğinde dokümanın en sonuna tek satır yaz:**
`MAKİNE KAPISI: 32/32 ✅` — eksik varsa madde numaralarını yaz.

# ⬆️⬆️⬆️ BURAYA KADAR KOPYALANIR ⬆️⬆️⬆️

---
---

# 4. 🔧 BAKIM NOTU

```
· Bu dosya 10 sahnelik motoru DEĞİŞTİRMEZ, yanına bir varyant koyar.
  Varsayılan hâlâ 10 × 6,0'dır (TIMELAPSE_SISTEM_PROMPTU.md).
· §Ş'deki 1-26 araclar/prompt_kontrol.py'nin, 27-32 QA merceklerinin AYNADAKİ hâlidir. Betik
  değişirse bu liste de değişir; ikisi ayrışırsa harici bot yanlış şeye
  uyar ve kapı boşuna BLOCK verir.
· ⭐ BU DOSYA ARTIK ÖLÇÜLMÜŞTÜR. Bir film (THE NARROW LOT) bu brief'le
  yazıldı, üretildi ve altı mercekle ölçüldü. §1.3 o ölçümdür.
  §J · §E · §C · §F3 · §I3 ve §Ş 27-32 ölçümden SONRA yeniden yazıldı —
  hepsi DERSLER 18-22'nin karşılığıdır.
· §1'in bedel tablosu hâlâ kısmen çıkarımdır: 5 sahnenin "sıçrama 2 katı"
  maddesi ② APPEARING ile DOĞRULANDI, "METRONOM riski" ⑥ ile DOĞRULANDI;
  "detay istasyonu YOK" maddesi hiç sınanmadı (film tek istasyon kullandı
  ve ① 10/10 aldı — yani kural işe yaradı ama alternatifi ölçülmedi).
· ⛔ AÇIK KALAN: bu brief'e göre yazılan bir doküman kapıdan ✅ GO alabiliyor
  (duman testi) ama HARİCİ BOT bu formatı uygulamadı ve kapı 25 madde BLOCK
  verdi. §C2 bunun karşılığıdır ve bir sonraki koşuda sınanacaktır.
```
