# 📒 İZLEYİCİ DEFTERİ — QA puanı izleyiciyle tutuyor mu

> **Neden var (05.10.2026):** 31 film üretildi, 12 mercekle ölçüldü — ama depoda TEK BİR
> izleyici sayısı yok. Bütün içerik kuralları (C2 · KILAVUZ_REHBERI §6 İZLEYİCİ KAPISI)
> değerlendirici yargısından çıktı. Bu defter onları ya doğrular ya düşürür.
> Kural: `YAYIN_PLANI §6.2` — bir gözlem ÜÇ AYRI FİLMDE aynı yönde çıkmadan kural olmaz.
>
> **Kim doldurur:** sahip, paylaşımın **7. günü**, YouTube Studio → içerik → Analiz'den.
> Ajan yalnız QA sütunlarını doldurur ve analizi yapar; izleyici sütununa sayı UYDURMAZ.

---

## 1. Yedinci gün — dört sayı yeter

```
KAYDIRMADI %    Shorts "Viewed vs. swiped away" — izlemeyi seçenlerin oranı   → KANCA (AÇILIŞ NESNESİ)
ORT. İZLENME %  Average percentage viewed (2x kopya üzerinden; >%100 = tekrar izleme) → MERDİVEN + DÖNGÜ
ENGAGED VIEWS   görüntüleme sayısı DEĞİL — dağıtımı değil filmi ölçer
ABONE           videodan gelen abone                                           → KAPAK + İŞLEV ANI
(isteğe bağlı)  tutma eğrisinde en büyük düşüşün saniyesi (2x) · ⭐ sektörden düzeltme yorumu
```

⛔ Toplam görüntüleme tek başına karar verdirmez · evrensel "viral eşik" kullanılmaz ·
karşılaştırma yalnız bu kanalın kendi filmleri arasında [QA_CAPRAZ_ANALIZ/06 §2].

### 1b. Resmî adlar ve tanımlar — okundu 07.10.2026 [A31-a · A31-b · A31-e]

| sayı | platformdaki adı · yeri | resmî tanım | not |
|---|---|---|---|
| KAYDIRMADI % | **"How many chose to view"** · Studio → Analiz → İçerik → Shorts | "percentage of times that viewers viewed your Shorts versus swiped away" (12942217) | ⛔ "%40–50 kaydırırsa dağıtım durur" eşiği anonim forum yanıtı — kullanılmaz |
| ORT. İZLENME % | Average percentage viewed | engaged views ve izlenme süresinden; engaged views "not including any loops" | ⚠️ %100'ü aşan değerler yalnız kullanıcı raporu (129 · 150) — ">%100 = tekrar izleme" okuması VARSAYIM |
| ENGAGED VIEWS | Gelişmiş mod → Engaged views | eski görüntüleme ölçüsü; **views** 31.03.2025'ten (Shorts) ve 24.08.2026'dan (bütün formatlar) beri oynatma başlar başlamaz sayılır | kazanç engaged views'tan · YPP uygunluğu "qualified views" |
| TikTok | Average watch time · Watched full video · Traffic source (For You · Search · Profile) | resmî: "time spent watching a video … weighted more heavily" | "%70 tamamlama eşiği" blog — kullanılmaz |
| Instagram | Views · Watch time · **Sends** · Likes (erişim başına) | Mosseri 22.01.2025: ilk üç sinyal watch time · likes · sends; bağlantısız erişimde gönderme ağır | 0 takipçide neredeyse bütün erişim bağlantısızdır |

```
⭐ TikTok ve Instagram için ikinci defter YOK: o platformların paylaşım ve yorum sayıları §4'e
   platform satırıyla girer. YouTube dört sayısı ana defterdir — üç platform aynı filmi taşıdığı
   için kıyas film ARASINDA yapılır, platform arasında değil.
```

## 2. Defter

QA sütunları (ajan doldurdu · 12 mercekli arşiv `QA/ARSIV_12_MERCEK`): **④** teslim · **K** kanca ·
**D** döngü · **İŞLEV** final ödülü çalışıyor mu (✅ çalışır · ⏸ durağan) · **KONU** Sıf / Dön / Rest / Eks.
`*` = ④ belgesiz (mod V) koştu, yön gösterir.

> ⛔ **06.10.2026 [DERS 64]:** arşivdeki ④ koşularının 36'sından yalnız 9'u plan görerek koşuldu
> (`00_ESLEME.tsv`) — `*` işareti eksik konmuştu; bu sütunlar YÖN gösterir, karşılaştırma için zayıftır.
> Yeni sütun **❺** (beş mercekli TESLİM puanı) yeniden koşulan filmlerde dolar; S1–S6 önce ❺ ile okunur.

| film | yayın tarihi | KAYDIRMADI % | ORT. İZLENME % | ENGAGED | ABONE | ④ | K | D | İŞLEV | KONU | ❺ |
|---|---|---:|---:|---:|---:|---:|---:|---:|:-:|:-:|:-:|
| THE DEEP END | | | | | | 9,9 | 10 | 9 | ✅ | Dön | |
| THE LAST LIFT | | | | | | 9,6 | 10 | 10 | ✅ | Sıf | |
| THE FIRST GUEST | | | | | | 9,6 | 10 | 9 | ✅ | Sıf | |
| THE LAST HARBOR | | | | | | 9,5 | 10 | 9 | ✅ | Sıf | |
| THE VANISHING ROOM | | | | | | 9,5 | 9 | 9 | ✅ | Dön | |
| THE BLUE DOOR | | | | | | 9,2 | 10 | 8 | ✅ | Rest | |
| THE GLASS CROSSING | | | | | | 8,5 | 9 | 8 | ✅ | Dön | |
| THE QUIET FIELD | | | | | | 8,4* | 8 | 8 | ✅ | Sıf | |
| THE LAST FIRING | | | | | | 8,0 | 8 | 7 | ✅ | Sıf | |
| THE DEEP STEP | | | | | | 7,5* | 9 | 5 | ✅ | Eks | |
| THE STONE TOWER | | | | | | 7,5* | 8 | 7 | ⏸ | Sıf | |
| BACK TO WATER | | | | | | 7,1* | 9 | 3 | ✅ | Rest | |
| POLAR HABITAT | | | | | | 7,1* | 9 | 4 | ✅ | Sıf | |
| THE MOUNTAIN CROWN | | | | | | 6,9 | 8 | 6 | ✅ | Eks | |
| THE EMPTY LOCK | | | | | | 6,8* | 7 | 5 | ✅ | Rest | |
| BACK TO PLUMB | | | | | | 6,1 | 8 | 6 | ✅ | Rest | |
| THE DARK ROCK | | | | | | 6,1* | 9 | 3 | ✅ | Sıf | |
| THE STONE DRAGON | | | | | | 5,7 | 8 | 5 | ✅ | Eks | |
| THE STAR DOCK | | | | | | 5,5 ⚠️ | 9 | 6 | ✅ | Sıf | |
| THE BROKEN CLIMB | | | | | | 5,1* ⚠️ | 8 | 4 | ✅ | Rest | |
| THE EMPTY RIDGE | | | | | | 3,4* | 4 | 3 | ✅ | Sıf | |
| THE GLASS WALL (yatay) | | | | | | 7,4 | 9 | 7 | ⏸ | Sıf | |
| THE IRON BRIDGE (yatay) | | | | | | 5,7 | 6 | 5 | ⏸ | Sıf | |

> ⚠️ THE STAR DOCK · THE BROKEN CLIMB: ④ "final kesik" diye düştü; dosya 2x paylaşım kopyasıydı
> (DERS 58 · 63) — ④ yeniden koşulmadan bu iki satırın ④'ü karşılaştırmaya girmez.
> Erken dönem filmler (LONG DAY · MOUNTAIN DOOR · NARROW LOT · CLOSING SPAN · DUST YEAR ·
> BUILT FROM DUST · OVER THE WALL · LONG SHADOW v1) yayınlandıysa satır eklenir.

## 2b. Yatay defter — 1x · 7. ve 28. gün [UZUN_FORM_ANLATI §7 · 07.10.2026]

Yatay film shorts değildir: "kaydırmadı" yok, eğri saniyeyle okunur ve saniye SAHNEYE çevrilir —
S = ⌊t / klip süresi⌋ (eşit süre) · değişken sürede PLAN SÜRE sütununun kümülatifi. Sahip doldurur;
ajan yalnız saniye → S çevirisini ve QA sütunlarını yazar, izleyici sayısı UYDURMAZ.

```
INTRO %         Audience retention → 30. saniyede kalanların oranı ("Intro" ölçüsü ✅)
ORT. İZLENME %  Average percentage viewed (1x · 4:00'da %100 = sonuna kadar)
DÜŞÜŞ           eğrideki en büyük dip: saniye → S (ör. 132 sn · 8 sn klip → S16)
SIÇRAMA         en büyük spike (geri sarma / tekrar izleme): saniye → S
SON EKRAN       var / yok (son 5–20 sn)
A/B             Test & compare: Winner · Performed same · Inconclusive — izlenme süresi payını ölçer ✅
```

| film | yayın | gün | INTRO % | ORT. İZLENME % | DÜŞÜŞ sn → S | SIÇRAMA sn → S | SON EKRAN | A/B | ❺ |
|---|---|:-:|---:|---:|---|---|:-:|:-:|---:|
| THE GLASS WALL | | 7 | | | | | | | |
| THE IRON BRIDGE | | 7 | | | | | | | |
| THE SLOW TAKEOFF | ⬜ üretilmedi | 7 · 28 | | | | | | | |

> ⭐ THE SLOW TAKEOFF ölçüm sorusu [A25-e · Ç1]: kalkış 0:40'ta (S5–S6). Eğride 0:56'dan sonra (S7)
> dik bir düşüş varsa "erken doruk merakı bitirir" itirazı bir filmde doğrulanmış olur — kural için üç film.

## 3. Ne zaman bakılır — dokuz soru (S7–S8 yatay · S9 bedel), her biri üç filmde aynı yönde

```
S1  İŞLEV ✅ filmler ⏸ filmlerden daha mı çok ABONE getiriyor?          → C2-a kural olur / düşer
S2  K 9-10 filmler KAYDIRMADI %'de K ≤ 8 filmlerden yukarıda mı?        → C2-c
S3  D 9-10 filmlerde ORT. İZLENME %100'ü geçiyor mu (tekrar izleme)?      → C2-d
S4  AÇILIŞ DÜZENİ'nin dört vuruşunu taşıyan filmler KAYDIRMADI %'de önde mi? → C2-h
    (yeni filmlerde satıra 'AÇILIŞ: nesne · dokunuş · ipucu' notu düşülür)
S5  İŞ YOĞUNLUĞU kuralıyla yazılan ilk filmler ORT. İZLENME %'de öncekilerden yukarıda mı? → C2-g
S6  S0 GERİ ÇEKİLME (GÇ) açılışlı filmler sabit geniş (SG) açılışlılardan KAYDIRMADI %'de önde mi? → C2-i
    (yeni filmlerde AÇILIŞ notuna 'GÇ n,n×' ya da 'SG' eklenir)
S7  (yatay) İLK BÜYÜK SONUÇ ≤ 45 sn olan filmler INTRO %'de geç olanlardan önde mi?   → A25-a
S8  (yatay) en büyük DÜŞÜŞ, art arda dört "yeni şeysiz" klibin içine mi düşüyor?        → A25-a (kanca aralığı)
S9  (dikey) BEDEL ekranda güçlü filmler (direnç anı kadrajda: fırtına · sel · kış) ORT. İZLENME %'de
    zayıflardan aşağıda mı?  → A33'ün "dikeyde bedelden vazgeç" iddiası (kaynaksız) · KANAL_KIMLIGI §2
    (yeni filmlerde satıra 'BEDEL: ekranda ✅ / metinde ⏸' notu düşülür)
⭐  Ters çıkarsa: QA rubriği izleyiciyi temsil etmiyor demektir — o zaman RUBRİK değişir, film değil.
```

## 4. Paylaşım ve yorum — 7. gün, sahip sayar [A33-d · 07.10.2026]

> Neden: kanalın "en değerli çıktısı" sayılan sektör düzeltmesi (YAYIN_PLANI §6.1) için sayım yöntemi
> yoktu. Paylaşım sayısı platformun verdiği sayıdır; yorum türü EN ÜSTTEKİ 50 yorumdan (ya da hepsi,
> 50'den azsa) elle sayılır. Ajan sayı UYDURMAZ; sahip yapıştırırsa türü ajan kodlar.

| film | platform | paylaşım / gönderme | yorum toplam | övgü | şüphe ("gerçek mi" · "AI") | teknik düzeltme | mizah | soru | düzeltme → ders adayı |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| | | | | | | | | | |

```
TÜRLER    övgü · şüphe · teknik düzeltme (yapı, sıra, malzeme, fizik) · mizah · soru
          ⛔ bir yorum tek türe girer; iki türe uyuyorsa TEKNİK DÜZELTME önce gelir
NE YAPILIR
   şüphe            POLITIKA_VE_RISK §3 sabit cevabı · ⛔ tartışmayı büyütmek için cevapsız bırakılmaz
   teknik düzeltme  doğruysa kilavuzlar/DERSLER.md ders adayı · yanıtta TEŞEKKÜR, savunma değil
   soru             cevaplanır; aynı soru üç filmde geliyorsa sabit yoruma girer
⛔ Yorum DAVET EDİLMEZ: kasıtlı hata, "find the mistake", "send this to…", "tag a friend" yok
   [A33-b · Meta 2017 engagement bait · TikTok FYF]. Düzeltme yorumu, doğru yapılmış filmin
   kendiliğinden ürünüdür.
```
