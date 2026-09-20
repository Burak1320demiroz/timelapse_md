# 🔬 ARAŞTIRMA — on iki derin araştırma promptu

> Bu klasör **bilgi üretmez, bilgi İSTER.** İçindeki sekiz dosya, harici bir
> derin araştırma botuna (ChatGPT Deep Research · Gemini Deep Research ·
> Perplexity Deep Research · Claude Research) **kesilmeden yapıştırılacak**
> bloklardır.
>
> ⛔ Harici bot bu deponun hiçbir dosyasını okuyamaz. Atıf vermek hiçbir şey
> vermemektir [D-a]. **Her prompt kendi kendine yeter** — bağlamı, kısıtı ve
> ölçülmüş arızayı kendi içinde taşır. Bu yüzden dördü de birbirini tekrar eder;
> tekrar bir savurganlık değil, kendi kendine yetmenin maliyetidir.
>
> ⭐ **İKİ KUŞAK VAR.** A1–A4 (03.09.2026) ilk dört filmin arızalarından doğdu
> ve koşuldu. **A5–A8 (07.09.2026 yazıldı · 08.09.2026 KOŞULDU)** THE LONG DAY'in sekiz mercekli ölçümünden
> doğdu, HENÜZ KOŞULMADI, ve her biri **yazılmamış bir kılavuzu yazdırmak**
> için vardır — sonucu doğrudan `kilavuzlar/` altına yeni bir dosya olarak iner.

---

# 1. 🎯 PROMPTLAR NEDEN BUNLAR

Konular hevesten değil, **QA/RAPORLAR'daki ölçülmüş arızalardan** doğdu.
Her prompt bir hükmün karşısına konmuştur:

| # | Dosya | Karşıladığı ölçülmüş arıza | Kaynak |
|:-:|---|---|---|
| A1 | `A1_VIRAL_ANATOMI.md` | Film kimseye ulaşmıyor — paketleme ve tür seçimi ölçüsüz | Henüz yayınlanmadı; ölçüm YOK |
| A2 | `A2_RITIM_VE_TUTUNMA.md` | ⑥ **METRONOM** · RHYTHM 0/10 · "hâlâ yavaş" | DERS 13 · CLOSING SPAN |
| A3 | `A3_ZINCIR_VE_TUTARLILIK.md` | ② **FARKLI** · ⑤ **NONE FOUND** · ① VANTAGE GROUPS 8 | DERS 5 · 12 · 15 |
| A4 | `A4_GERCEKLIK_IMZASI.md` | ③ zaman okunmuyor · mevsim taşıyıcısı yok · yıldız izi | DERS 14 · 16 |
| A5 | `A5_INSA_YONTEMI.md` ⭐ | ⑧ **APPEARED · 1/9 MADE** · ② DIFFERENT beş filmin beşinde · ⑦ PARKED | LONG DAY · DERS 33 |
| A6 | `A6_SANTIYE_HAREKETI.md` | ⑦ **PARKED** · boş aralık %100 · ① PEOPLE 0 · SURFACE TRUTH 0 | LONG DAY |
| A7 | `A7_ARAC_PROFILI.md` | araç kapısı beş filmde koşulmadı · negatif sızdı · süre tutmadı | DERS 23 · 31 · 32 · 33 |
| A8 | `A8_KURGU_VE_TESLIM.md` | ⑥ **METRONOM** dördüncü kez · beş mercekte END CARD DIFFERENT | DERS 13 · 31 |

⭐ **A3 en yüksek kaldıraçlıdır.** İki film de aynı sebepten düştü ve sebep
bir üretim aracıdır, bir yazım kuralı değil. Tek prompt koşacaksan A3.

⭐ **Yeni dörtlüde A5 en yüksek kaldıraçlıdır.** ② · ⑦ · ⑧ aynı şeyi üç
açıdan söylüyor: hiçbir şey inşa edilmiyor, her şey kesmede beliriyor. A5 o üç
hükmün ortak kaynağını hedefler. Koşma sırası: **A5 → A8 → A7 → A6.**

```
✅ 08.09.2026: DÖRDÜ DE KOŞULDU, DENETLENDİ VE HEDEF KILAVUZLAR YAZILDI.
   INSAAT_YONTEMI_KILAVUZU · SANTIYE_HAREKETI_KILAVUZU · ARAC_KARTLARI ·
   KURGU_VE_TESLIM_KILAVUZU — dördü de kilavuzlar/ altında.
   ⛔ AMA: raporlardan tek bir SAYI doğrudan inmedi. Üç sayı bu depoda
      yeniden hesaplandı ve düştü, iki ffmpeg komutu koşmadı, bir eşik kör
      çıktı. Ayrıntı: SONUCLAR/A5-A8_DENETIM.md
```

## 1.1 📌 KOŞU DURUMU — 03.09.2026

| # | Ham dosya | Bot | Kaynak sınıfı | Kılavuza indi mi |
|:-:|---|---|---|---|
| A1 | `SONUCLAR/A1_GEMINI_HAM.md` | Gemini DR | ⚠️ ağırlıkla pazarlama blogu | kısmen (A1-b · A1-c · A1-d) |
| A2 | `SONUCLAR/A2_GEMINI_HAM.md` | Gemini DR | ⭐ akademik | evet (A2-a…e) |
| A3 | `SONUCLAR/A3_GEMINI_HAM.md` | Gemini DR | akademik + araç dokümanı | evet (A3-a…f) ⭐ en ağır |
| A4 | `SONUCLAR/A4_GEMINI_HAM.md` | Gemini DR | ⭐ akademik | evet (A4-a…f) |
| P1 | `SONUCLAR/P1_PLAN_OKUMA_HAM.md` | insan · profesyonel timelapse yapımcısı | uzman okuması · THE LONG DAY v0 PLANI | evet (P1-a…k) — ⛔ ölçüm değil, plan okuması |
| A5 | ✅ koşuldu | Gemini | 08.09.2026 | ✅ denetlendi → `A5-A8_DENETIM.md` |
| A6 | ✅ koşuldu | Gemini | 08.09.2026 | ✅ denetlendi → `A5-A8_DENETIM.md` |
| A7 | ✅ koşuldu | Gemini | 08.09.2026 | ✅ denetlendi → `A5-A8_DENETIM.md` |
| A8 | ✅ koşuldu | Gemini | 08.09.2026 | ✅ denetlendi → `A5-A8_DENETIM.md` |
| P2 | `SONUCLAR/P2_LONG_SHADOW_OKUMA_HAM.md` · `P3_MOUNTAIN_DOOR_…` · `P4_NARROW_LOT_…` · `P5_CLOSING_SPAN_…` | aynı yapımcı | uzman okuması · dört ÜRETİLMİŞ filmin planı + QA'sı | evet (P2-a…l · tek kod serisi) — ⛔ ölçüm değil, okuma |
| A9 | ✅ koşuldu · `SONUCLAR/A9_GEMINI_HAM.md` | Gemini (tahmin) | 11.09.2026 · standart adları doğru, sayılar çekilmedi | ✅ → MALZEME_VE_DOKU_KILAVUZU · denetim `A9-A12_DENETIM.md` |
| A10 | ✅ koşuldu · `SONUCLAR/A10_GEMINI_HAM.md` | Gemini (tahmin) | 11.09.2026 · standart adları doğru, benchmark DOI'siz | ✅ → FIZIK_VE_AGIRLIK_KILAVUZU |
| A11 | ✅ koşuldu · `SONUCLAR/A11_GEMINI_HAM.md` | Gemini (tahmin) | 11.09.2026 · 15 DOI: 7 ✅ · 4 ❌ yanlış atıf · 1 erişilemedi | ✅ → PERSPEKTIF_VE_OLCEK_KILAVUZU |
| A12 | ✅ koşuldu · `SONUCLAR/A12_GEMINI_HAM.md` | Gemini (tahmin) | 11.09.2026 · "Python Script Snippet" kaynak değil; gölge 15°/sa DÜŞTÜ | ✅ → HAVA_VE_ATMOSFER_KILAVUZU |
| A13 | ⚠️ İSTENMEDİ · `SONUCLAR/A13_BEYANSIZ_HAM.md` | ⛔ beyan edilmedi | 17.09.2026 · aritmetik temiz (20/20) ama fiziksel kamera anlatıyor | ✅ → KAMERA_HAREKETI_KILAVUZU |
| A14 | ⚠️ İSTENMEDİ · `SONUCLAR/A14_BEYANSIZ_HAM.md` | ⛔ beyan edilmedi | 17.09.2026 · güvenli alan rakamı kendi tablosuyla çelişti, DÜŞTÜ | ⚠️ kısmen (mekanizma) |
| A15 | ⚠️ İSTENMEDİ · `SONUCLAR/A15_BEYANSIZ_HAM.md` | ⛔ beyan edilmedi | 17.09.2026 · CTR bantları pazarlama sınıfı, inmedi | ⚠️ → MUZIK_VE_KAPAK §4 |
| A16 | ⚠️ İSTENMEDİ · `SONUCLAR/A16_BEYANSIZ_HAM.md` | ⛔ beyan edilmedi | 17.09.2026 · 11 satırın 10'u tuttu, 1'i bin kat şişik | ⚠️ yalnız yöntem (sapma çarpanı) |
| A17 | ⚠️ İSTENMEDİ · `SONUCLAR/A17_BEYANSIZ_HAM.md` | ⛔ beyan edilmedi | 17.09.2026 · platform zarfı (1280×720 · 2 MB · süre etiketi) | ⚠️ → MUZIK_VE_KAPAK §4 |
| A18 | ⚠️ İSTENMEDİ · `SONUCLAR/A18_BEYANSIZ_HAM.md` | ⛔ beyan edilmedi | 17.09.2026 · A14 ile TERS yönde konuşuyor (sabit kamera) | ⚠️ çelişki kaydı |
| P6 | `SONUCLAR/P6_THE_LAST_CIRCLE_OKUMA_HAM.md` | insan · uzman okuması | 17.09.2026 · YAZILMAMIŞ planı okudu | evet (P3-a…P3-i) — ⛔ bir kılavuz maddesini DÜZELTTİ |
| P7 | `SONUCLAR/P7_THE_BORROWED_HILL_OKUMA_HAM.md` | insan · uzman okuması | 17.09.2026 · YAZILMAMIŞ planı okudu | evet (P4-a…P4-i) — ⭐ bir HESAP HATASI yakaladı |
| A19 | ⚠️ İSTENMEDİ · `SONUCLAR/A19_KAMERA_DILI_HAM.md` (kökten taşındı) | ⛔ beyan edilmedi | 20.09.2026 · ⭐ kaynakça ÇEKİLDİ: 11'in 10'u iddiaya ait · 8 sayının 8'i tuttu · yarısı fiziksel kamera | ✅ → KAMERA_DILI_KILAVUZU · denetim `A19_DENETIM.md` (yeni sayı yok, iki formül) |

```
⭐ DÖRDÜNCÜ KUŞAK BAŞKA TÜRLÜ GELDİ — 17.09.2026
   Altı rapor, tek yapıştırmayla ve BU DEPODA YAZILMIŞ BİR PROMPT OLMADAN geldi.
   İlk üç kuşakta soruyu biz yazdık; burada yazmadık.
   ⛔ Yeni körlük: neyin SORULDUĞU bilinmiyorsa neyin DIŞARIDA BIRAKILDIĞI da
      bilinmiyor. Rapor "en sık kullanılan on hareket" diyor — hangi evrenden
      seçildiği, hangi filtreyle elendiği yazmıyor ve sorulamıyor.
   ⛔ İkinci körlük: [cite: n] işaretleri var, KAYNAKÇA YOK. A9–A12'de 12 kaynak
      çekilebilmişti (7 tuttu, 4 yanlış atıf); burada çekilecek bir şey yok.
   ⇒ Bu yüzden altı rapordan kılavuza TEK SAYI indi ve o da raporun değil,
     denetimde bu makinede hesaplanan sayıdır (A13-c · yakınlaşma tavanı).
   ⭐ Buna rağmen kuşağın değeri yüksek çıktı: bir ÇELİŞKİ görünür oldu
     (A18-a · sabit kamera) ve bu, kart S §4'ün "iki rapor aynı şeyi farklı
     söylüyorsa o şey ölçülmemiştir" kuralının ilk gerçek uygulamasıdır.
```

```
⛔ DÖRDÜ DE TEK BOTA KOŞULDU. §2'nin "aynı promptu iki bota koş" uyarısı
   işletilmedi; yani çelişki görünür değil ve bu, on altı maddenin
   ORTAK zayıflığıdır.
⛔ DÖRDÜ DE PROMPTUN KISA (6 cümlelik) SÜRÜMÜYLE koşuldu — bu klasördeki
   tam bloklar DEĞİL. Tam bloklar hâlâ koşulmamış durumda.
⭐ KÜNYE EKSİK: ham dosyaların SÜRE ve KESİLDİ Mİ satırları boş; proje
   sahibi doldurur.

⚠️ ETİKET GÜVENİ — bu koşunun en önemli bulgusu bir bulgu değil, bir uyarı:
   rapor her maddeye ÖLÇÜLDÜ / İDDİA / VARSAYIM yazdı ve A1'in ÖLÇÜLDÜ
   etiketlerinin çoğu SEO içerik çiftliğine dayanıyordu. Bir sayının
   yanında "ÖLÇÜLDÜ" yazması o sayıyı ölçmez — KAYNAĞINI ölçer.
   ⭐ Bu yüzden §3'ün 2. adımına bir alt adım eklendi: etiket okunduktan
      sonra KAYNAK SINIFI da yazılır (akademik · araç dokümanı ·
      pazarlama blogu) ve yalnız ilk ikisi kılavuza iner.
```

---

# 2. 🔁 AKIŞ

```
1. SEÇ        arastirma/A<n>_*.md dosyasını aç
2. YAPIŞTIR   "⛔ BURADAN AŞAĞISI YAPIŞTIRILIR" satırından dosya sonuna kadar
              olan bloğu, KESMEDEN, derin araştırma botuna ver
3. BEKLE      bot raporu üretsin (10-40 dk sürebilir)
4. KAYDET     gelen HAM çıktı → arastirma/SONUCLAR/A<n>_<BOT>_HAM.md
              ⛔ düzenleme · kısaltma · özetleme YOK — bu kanıttır
              (QA/HAM_RAPORLAR ile aynı disiplin)
5. AJANA VER  "arastirma/SONUCLAR/ okundu, kılavuzlara indir" de
```

⚠️ **Aynı promptu İKİ farklı bota koşmak ucuzdur ve çelişkiyi görünür yapar.**
İki rapor aynı sayıyı farklı veriyorsa o sayı ÖLÇÜLMEMİŞ demektir; ikisi de
`SONUCLAR/` altında ayrı dosya olarak durur, ortalaması ALINMAZ.

---

# 3. 📥 SONUÇ GELDİĞİNDE — ajanın işi

```
1. HAM KAYIT      SONUCLAR/ altına dokunulmadan yazılır
2. ETİKET AYIKLA  raporun her bulgusunda ÖLÇÜLDÜ / İDDİA / VARSAYIM etiketi
                  olmalı. Etiketsiz bulgu KURAL ÜRETMEZ — okuma sayılır.
2b. ⛔ KAYNAK SINIFI  etiketin YANINA kaynak sınıfı yazılır:
                  akademik · araç dokümanı · pazarlama blogu
                  ⛔ Yalnız ilk ikisi kılavuza iner. Ölçüldüğünü SÖYLEYEN
                     bir rapor, ölçülmüş bir rapor değildir [03.09.2026 koşusu].
3. ÇELİŞKİ TARA   "BİZİM FORMATIMIZLA ÇELİŞENLER" bölümü önce okunur.
                  Bir kılavuz maddesi ölçülmüş bir bulguyla çelişiyorsa
                  kılavuz DEĞİŞİR — bulgu değil.
4. DERSE ÇEVİR    yalnız ÖLÇÜLDÜ etiketli bulgular kilavuzlar/DERSLER.md
                  kalıbına girer. KALDIRDIĞI satırı zorunlu [D-f].
5. KİLİT YAZ      prompta inecek her cümle İNGİLİZCE ve POZİTİF hâlde
                  yazılır — yasak değil, ölçülebilir çapa [DERS 11].
```

⛔ **Araştırma bulgusu ders DEĞİLDİR.** Bu depoda ders, bu depoda ölçülmüş
bozulmadır. Araştırmadan çıkan her şey en fazla **gerekçeli varsayımdır** ve
`DERSLER.md`'nin "DEVRALINAN DERSLER" bölümüne, `A<n>-x` koduyla girer.
İlk üretimden sonra ya numaralı bir derse dönüşür ya düşer.

---

# 4. 📁 DOSYALAR

```
arastirma/
├── 00_README.md                  bu dosya
├── A1_VIRAL_ANATOMI.md           ne yayılıyor · paketleme · tür seçimi
├── A2_RITIM_VE_TUTUNMA.md        kanca · kesme varyansı · loop · ses
├── A3_ZINCIR_VE_TUTARLILIK.md    ⭐ aynı bina · aynı kamera · aynı hız
├── A4_GERCEKLIK_IMZASI.md        gerçek timelapse fiziği · AI işaretleri
│
│   ── ikinci kuşak · 07.09.2026 yazıldı · 08.09.2026 ✅ dördü de koşuldu ──
├── A5_INSA_YONTEMI.md         ⭐ eleman eleman yapım sırası · ara hâller
├── A6_SANTIYE_HAREKETI.md        ACTIVITY kaynağı · iz · yüzey kanıtı
├── A7_ARAC_PROFILI.md            aracın ölçülmüş davranışı · test protokolü
├── A8_KURGU_VE_TESLIM.md         kesme · dikiş · final · kapak · teslim QC
│
│   ── üçüncü kuşak · 08.09.2026 yazıldı · 11.09.2026 v2 (altı cümle + çözümlenebilir kaynak) · ✅ dördü de koşuldu ──
├── A9_MALZEME_VE_DOKU.md         yüzey gerçekliği · kirlilik katmanı · yaşlanma
├── A10_FIZIK_VE_AGIRLIK.md       yük yolu · söküm · robotik gövde · katılık ihlalleri
├── A11_PERSPEKTIF_VE_OLCEK.md    referans nesne · sayı sadakati · zincirde kayma
├── A12_HAVA_VE_ATMOSFER.md       bulut × rejim · atmosferik derinlik · iki kare arası gök
├── SONUCLAR/A9-A12_DENETIM.md    ⭐ kaynak doğrulama: 12 çekim, 7 tuttu, 4 yanlış atıf
│
│   ── dördüncü kuşak · 17.09.2026 · ⛔ PROMPT YOK, rapor sipariş edilmeden geldi ──
├── SONUCLAR/A13…A18_BEYANSIZ_HAM.md  kamera hareketi · tutunma · kapak (altı rapor)
├── SONUCLAR/A13-A18_DENETIM.md   ⭐ 20 formül yeniden hesaplandı · 1 çarpan bin kat
│                                   şişik · güvenli alan rakamı düştü · A14↔A18 çelişkisi
│
│   ── A19 · 20.09.2026 · ⛔ PROMPT YOK, sahip köke bıraktı · ⭐ kaynakça çekildi ──
├── SONUCLAR/A19_KAMERA_DILI_HAM.md  viral timelapse kamera/çekim rehberi (19 bölüm · 8 prompt)
├── SONUCLAR/A19_DENETIM.md       ⭐ 11 kaynağın 10'u açıldı · 8 sayı tuttu · katsayı formülü
│                                   rejim tablosunu bağımsız üretti · tiltli kadraj açığı
└── SONUCLAR/                     ham bot çıktıları ⛔ DOKUNULMAZ
```
