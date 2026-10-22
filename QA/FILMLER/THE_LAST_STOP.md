# THE_LAST_STOP — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 8 × 8,0 sn = 64,0 sn (⚠️ sahip istisnası 19.10.2026) · paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn = 37,0 sn
plan: dikey_shorts/THE_LAST_STOP/THE_LAST_STOP_DIKEY_TIMELAPSE.md (19.10.2026 · 8 sahne · kart beyanlı · kapı BLOCK 0 · FIX 1)
üretim günlüğü: dikey_shorts/THE_LAST_STOP/THE_LAST_STOP_URETIM_GUNLUGU.md
yayın dosyası: raporda `lens1_bus_renovation.mp4` (❶ ❷) / `the last stop (1).mp4` (❸ ❹ ❺) · 0:32.0 · 9:16 dikey · tek sürekli sekans (30 frame) · sesli
master: bilinmiyor (beş mercek de 2x yayın kopyasıyla koşuldu)
kapak: ❺ "cover: NOT SUPPLIED" (kart 0:32.0'de videodan görüldü)
koşu tarihleri: 22.10.2026 · sahip koşusu (Gemini) · ajan inceleme ve kaydı 22.10.2026

---

## ⭐ AJAN ÖLÇÜMÜ VE MERCEK DEĞERLENDİRMESİ

Video modele tek parça, sürekli bir sekans (0:00.0–0:32.0) olarak girmiştir. Beş merceğin beşi de kör/yarı-kör modda tam olarak koşulmuş ve tutarlı zaman damgalarıyla puanlanmıştır.

```
YAYIN KURGUSU (2x · 0:00.0 – 0:32.0)
 0:00.0 – 0:02.0  Açılış: Orman açıklığında yosunlu paslı otobüs ve sol alttaki kaya nirengisi
 0:02.0 – 0:05.0  Tavan kaldırma: Sol üstteki vinç paslı tavan panelini kaldırır
 0:05.0 – 0:10.0  Gövde değişimi: İşçiler çalışırken gövde paslı griden kırmızıya döner (0:10.0 MELTING)
 0:15.0 – 0:22.0  İç mekân döşeme: Mobilyalar ve zemin kaplaması yerleşir
 0:24.0 – 0:26.0  Ahşap teras: Kapı önüne dış ahşap platform kurulur
 0:26.0 – 0:28.0  Cam tavan montajı: Vinç büyük şeffaf cam tavan panelini indirip kilitler
 0:28.0 – 0:30.0  İşlev anı & Işık: Alacakaranlık çöker, iç ve dış lambalar yanar (FINAL BEAT PASS)
 0:30.0 – 0:32.0  Final tutuşu & Statik kart: "THE LAST STOP" başlık kartı
```

```
✅ TUTANLAR
· KAMERA KİLİDİ KUSURSUZ (❶ 10/10 · ❷ 10/10 · ❸ 10/10): Sol alttaki kaya nirengisi, kütük kümesi ve arka çam ağaçları 32 saniye boyunca sıfır piksel kaymayla sabit kalmıştır.
· ZAMAN VE IŞIK EĞRİSİ (❷ 10,0 · ❸ C4 10/10): Gün ışığından sıcak akşama ve mavi alacakaranlığa geçiş, gölge süpürmesi ve 0:28.0'daki ışık patlaması kusursuz okunmuştur.
· İNŞA SIRASI VE YÜK YOLU (❹ 9,4 · 10/10): İç mekân mobilyalarının cam tavan kapanmadan ÖNCE yerleştirilmesi (Order 10/10) ve cam tavanın vinç sapanlarıyla indirilmesi inşaat mantığına tam oturmuştur.
· FİNAL VURUŞU VE DÖNGÜ (❺ 9,3 · PASS): Hurda otobüsün parlayan cam tavanlı lüks bir inziva kabinine dönüşme vaadi ekrana eksiksiz çıkmıştır; son kare tutuşu ve kapanış kartı kusursuzdur.
```

```
⚠️ PLAN ↔ MODEL SAPMALARI (ÖĞRENİLEN DERSLER)
① VİNÇ SIZINTISI [DERS 59]: Planda `YASAK KELİME  crane · hoist` yazılmış ve tavanın küçük katlanır bomla
   veya vinçsiz kaldırılması hedeflenmişti. Ancak videoda sol üstte bariz bir mobil vinç (overhead crane truck)
   yer almıştır. Mercekler Mod V'de bunu mantıklı bir inşaat aracı sayıp tam puan vermiştir; fakat planın vinçsizlik kuralı çiğnenmiştir.
② GÖVDE BOYASINDA ERİME (MELTING @ 0:10.0) [DERS 61]: Otobüsün paslı gri dış yüzeyi 0:10.0'da fiziksel bir boyama/zımpara
   yolu gösterilmeden bir anda kırmızıya dönmüştür (identity swap). ❶ bunu haklı olarak "MELTING" olarak cezalandırmıştır (7/10).
③ METİN YASAĞI VE KAPAK KARTI KARIŞIKLIĞI: ❶ merceği 0:32.0'deki "THE LAST STOP" başlık kartını 4 TEXT AND BRANDING
   kategorisinde değerlendirip 5/10 kırmıştır. Kusur sahipliği kılavuzuna göre (RUBRIK_YAZIM §5) kapak kartı yazısı ❺'in konusudur;
   fakat kural gereği model çıktısına dokunulmamış, ham puan korunmuştur.
```

---

## MERCEKLER

| mercek | durum | puan | hüküm | ham | en ağır bulgu (m:ss.s) · not |
|---|---|:-:|---|---|---|
| ❶ GÖRÜNTÜ | TAM | 7,5 | TIMELAPSE · MELTING | [THE_LAST_STOP_Q1_GORUNTU_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_LAST_STOP/THE_LAST_STOP_Q1_GORUNTU_HAM.md) | 0:10.0 otobüs gövdesi kırmızıya eriyerek değişti (MELTING) · 0:32.0 kart metninden puan kırıldı |
| ❷ ZAMAN VE KESME | TAM | 10,0 | PASSING · TIME | [THE_LAST_STOP_Q2_ZAMAN_KESME_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_LAST_STOP/THE_LAST_STOP_Q2_ZAMAN_KESME_HAM.md) | Gün ışığından akşama kusursuz gölge süpürmesi · tek sekans nedeniyle kesme maddeleri NOT TRIGGERED |
| ❸ ŞANTİYE | TAM | 8,9 | SAME WORLD · WORKING | [THE_LAST_STOP_Q3_SANTIYE_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_LAST_STOP/THE_LAST_STOP_Q3_SANTIYE_HAM.md) | Kaya nirengisi 10/10 sabit · vinç döngüleri ve malzeme akışı 7–8/10 · duraksama yok |
| ❹ İNŞA | TAM (Mod V) | 9,4 | SAME · BUILT · INVITED | [THE_LAST_STOP_Q4_INSA_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_LAST_STOP/THE_LAST_STOP_Q4_INSA_HAM.md) | Gövde, deck, cam tavan ve mobilyaların hepsi görünür adımlarla yerleşti · sıra doğru |
| ❺ TESLİM | TAM (Mod V) | 9,3 | ENDS | [THE_LAST_STOP_Q5_TESLIM_HAM.md](file:///Users/dai/github/apex_md/timelapse_md/QA/HAM/THE_LAST_STOP/THE_LAST_STOP_Q5_TESLIM_HAM.md) | Final Beat PASS · 0:28.0 ışıklar yanar · vaat eksiksiz ekranda · kart tam |

```
FİLM PUANI:  9,0  (N=5)        [ (7,5 + 10,0 + 8,9 + 9,4 + 9,3) / 5 ]
ÖLDÜRÜCÜ:    YOK  (❶ TIMELAPSE · ❸ SAME WORLD · ❹ SAME · ❺ ENDS)
OLUMSUZ:     MELTING (❶ — 0:10.0 otobüs gövdesi renk sıçraması)
SONUÇ:       ✅ GEÇTİ (PASS)
```

---

## DOĞRULAMA (D1–D6)

- **Geri okuma**: ❶ ✓ (lens1_bus_renovation.mp4 / NONE / 1) · ❷ ✓ (lens1_bus_renovation.mp4 / NONE / 1) · ❸ ✓ (the last stop (1).mp4 / NONE / 1) · ❹ ✓ (the last stop (1).mp4 / NONE / 1) · ❺ ✓ (the last stop (1).mp4 / NONE; cover: NOT SUPPLIED / 1). Beş mercek de geri okumayı eksiksiz geçti.
- **D1 (Dosya dışı damga)**: Yok. Tüm zaman damgaları 0:00.0 – 0:32.0 aralığındadır.
- **D2 (Klip sayısı)**: 1 klip bildirilmiş (tek sürekli sekans); kurgu bölünmesi olmadığı için model uydurma yapmamıştır.
- **D3 (Süre itirazı)**: Yok. 32 saniyelik kurgunun tamamı değerlendirilmiştir.
- **D4 (Kesme damgası)**: Tek sekans olduğundan kesme uydurması yoktur.
- **D5 (Kart)**: 0:32.0'de kart görülmüş ve 10/10 ile puanlanmıştır.
- **D6 (Kurgu tablosu)**: Kareler ve olaylar kronolojik olarak örtüşmektedir.

---

## ❓ MERCEKLERİN SORULARI VE PLANDAN CEVAPLAR (Questions for the Document)

1. **Otobüsün paslı griden kırmızıya dönüşü fiziksel bir boyama mı, dijital geçiş mi?**
   - *Plandan Cevap*: Planda (S2) pasların tel fırça ve zımparayla temizlenmesi, ardından astar ve bordo boya rulosuyla boyanması hedeflenmişti. Ekranda ara aşamalar hızlı atlandığı için model bunu renk sıçraması (color swap) olarak yansıtmıştır; bu durum ❶ MELTING hükmünü doğurmuştur.
2. **İç mekân mobilyaları ve zemin elle mi yerleştirildi, dijital mi eklendi?**
   - *Plandan Cevap*: Planda (S3-S5) iki işçinin meşe zemin latalarını ve modüler minderleri kapıdan tek tek içeri taşıması şart koşulmuştur. Ekranda işçiler ve malzeme akışı görünür durumdadır (❹ 8/10), sıralama inşa mantığına uygundur.
3. **Gündüzden alacakaranlığa geçişin planlanan süresi nedir?**
   - *Plandan Cevap*: Plan tek bir günün (21 Haziran, yaz dönümü, 57°K) sabahından akşam 21:00 mavi saatine kadar olan 14 saatlik zaman dilimini Rejim B (hızlandırılmış gün) ile 32 saniyede temsil etmektedir.
4. **Cam tavan montajı sol üstteki vinçle mi yapıldı?**
   - *Plandan Cevap*: Planda vinç yasaklı kelimeydi (`YASAK KELİME crane`), ancak video üretim motoru çatı camını sol üstteki mobil vinç koluyla indirmiştir. Model bu mühendislik yöntemini mantıklı bularak ❹ C4'te 10/10 vermiştir.
5. **Akşam aydınlatması önceden mi kuruldu?**
   - *Plandan Cevap*: Evet; planda yatak kaidesi altındaki LED şeritler ve lambader tavan kapanmadan önce kablolanmış, finalde (0:28.0) anahtar çevrilerek tek karede devreye alınmıştır.
