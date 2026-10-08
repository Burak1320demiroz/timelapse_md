# 📺 apexait — üç hesap, tek kanal

`kilavuzlar/` **filmi nasıl yapacağını**, `dikey_shorts/` **hangi filmi**
yaptığını, `QA/` **filmin geçip geçmediğini** tutar. Burası dördüncü soruyu
tutar: **film QA'dan geçtikten sonra ne oluyor.**

```
Kanal:  Apex AI Timelapse
Handle: @apexait          ← üçünde de aynı
Ürün:   9:16 · sessiz · sabit kamera · inşaat timelapse
        teslim yapısı: KILAVUZ_REHBERI §2.1 (sahne bloğu + başlıklı kapak kartı)
Tez:    ⭐ HER FİLM BİR BEDEL GÖSTERİR
```

---

## 🗂️ YAPI — ortak kökte, platforma özel klasörde

```
apexait/
├── KANAL_KIMLIGI.md      ⭐ ÜÇÜNDE DE AYNI — tez · negatif çekirdek ·
│                            palet · logo şartnamesi · dil · kanal metinleri
├── YAYIN_PLANI.md        ⭐ ÜÇÜNDE DE AYNI — kadans · iki ayak ·
│                            siluet sırası · açılış · film havuzu · ölçüm
├── CAPRAZ_YAYIN.md       ⭐ ÜÇÜNDE DE AYNI — tek master · filigran yasağı ·
│                            metadata · güvenli alan zarfı · yükleme sırası
├── IZLEYICI_DEFTERI.md   7. gün sayıları · QA ↔ izleyici · paylaşım ve yorum türü
├── TUR_HARITASI.md       dış vaka havuzu 2025–2026 · vaka defteri [A30 · 07.10.2026]
│
├── youtube/              POLITIKA_VE_RISK.md · PAKETLEME_SABLONU.md
├── instagram/            HESAP_KIMLIGI.md   · PAKETLEME_SABLONU.md
└── tiktok/               HESAP_KIMLIGI.md   · PAKETLEME_SABLONU.md
```

```
⛔ KÖKTEKİ HİÇBİR ŞEY PLATFORM KLASÖRÜNE KOPYALANMAZ.
   Kopyalandığı gün üç kimlik ayrışır ve hangisinin doğru olduğu kaybolur
   (AGENTS.md §3 ①). Ne ortak ne özel → CAPRAZ_YAYIN §5 tablosu.
```

---

## 📖 OKUMA SIRASI

```
İLK KEZ OKUYORSAN
  1. KANAL_KIMLIGI.md              kanal ne · neyi reddediyor
  2. youtube/POLITIKA_VE_RISK.md   ⭐ kanalı ne öldürür (üçünü de ilgilendirir)
  3. YAYIN_PLANI.md                ne zaman ne yayınlanıyor
  4. CAPRAZ_YAYIN.md               bir film üç hesaba nasıl gidiyor

YÜKLEME YAPACAKSAN — elinde tutacağın iki dosya
  · CAPRAZ_YAYIN.md §6            (çapraz kontrol listesi)
  · <platform>/PAKETLEME_SABLONU  (o platformun listesi ve metinleri)
```

## 🧭 ÜÇ HESAP, ÜÇ AYRI İŞ

```
YouTube    arşiv ve arama · para ayağı        → youtube/
TikTok     erişim ve yeniden izlenme          → tiktok/
Instagram  otorite ve düzeltme yorumları      → instagram/

⛔ Üçünde aynı metni paylaşmak "çapraz yayın" değildir. Film aynı,
   paketleme farklıdır — sebepleri her klasörün §1'inde yazılı.
```

---

## ⛔ BU KLASÖR NE DEĞİL

```
· Üretim kılavuzu DEĞİL. Prompt, kadraj, güneş açısı, negatif çekirdek,
  klip süresi, kapak metni kuralları → kilavuzlar/. Buraya kopyalanmaz.
· Film klasörü DEĞİL. Filmler dikey_shorts/ altında yaşar.
· QA DEĞİL. Yayın kapısı QA/00_README'dedir ve paketlemeden ÖNCE koşar.
· Sayı kaynağı DEĞİL — üç istisna, üçü de burada DOĞAR:
    youtube/POLITIKA_VE_RISK §5   YouTube'un dış sayıları
    instagram/HESAP_KIMLIGI §6    Instagram'ın dış sayıları
    tiktok/HESAP_KIMLIGI §6       TikTok'un dış sayıları
    KANAL_KIMLIGI §5.1            kanal paleti
    CAPRAZ_YAYIN §3.2             4:5 ızgara kırpması (türetilmiş)
```

---

## 🔲 AÇIK İŞLER — üç hesap da yayına girmeden önce

```
□ LOGO           sende. Şartname + 32 px testi: KANAL_KIMLIGI §5.2
                 ⭐ üç platformda da AYNI logo kullanılır
□ BANNER         yalnız YouTube: KANAL_KIMLIGI §5.3
□ HANDLE         @apexait üç platformda da alındı mı
□ KADANS         YAYIN_PLANI §1'de öneri var; kararı yaz ve üç biyografideki
                 <kadans> alanını doldur
□ MÜZİK LİSANSI  youtube/POLITIKA_VE_RISK §4'teki üç boşluk BOŞ.
                 ⛔ Dolmadan müzikli video yayınlanmaz.
□ AÇILIŞ BLOĞU   3 film gerekiyor, 1'inin planı var (THE_LONG_SHADOW).
                 YAYIN_PLANI §5 havuzundan, farklı siluet ailelerinden.
□ ÖLÇÜM          güvenli alan kaplama testi (CAPRAZ_YAYIN §3.3) ilk filmden
                 sonra koşulur — tablodaki ⚠️'ler ancak öyle kalkar
□ DOĞRULAMA      üç ⚠️ tablosu (YouTube · Instagram · TikTok dış sayıları)
                 uygulamadan doğrulanmadı
```
