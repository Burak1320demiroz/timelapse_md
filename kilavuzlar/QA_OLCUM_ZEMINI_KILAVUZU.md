# 📏 QA ÖLÇÜM ZEMİNİ KILAVUZU — sayıyı makine ölçer, model yargılar

> Video-dil modeli bir **hakemdir, kronometre değildir.** Süre, oynatma hızı, klip ve
> kesme sayısı, kesme zamanı, kart var mı, final kaç saniye tutuldu, ses akışı var mı —
> bunlar makinede ölçülür ve rubriğin içine **ÖLÇÜLMÜŞ OLGULAR** olarak verilir. Model
> yalnız bu olguların üstünde yargı kurar; onları yeniden tahmin etmez.
>
> Kaynak: A21 · 06.10.2026 (`arastirma/SONUCLAR/A21_GEMINI_HAM.md`) · denetim
> `A20-A24_DENETIM.md` · tetikleyen: 06.10.2026 QA denetimi.
> ⭐ Rapordan inen: hibrit düzen ("measured facts" bloğu) · 1 fps örnekleme sınırı
> (Gemini API dokümanı, çekildi ✅) · iki dosya seçeneği · zaman damgası doğrulama
> katmanı. ⛔ İnmeyen: PySceneDetect `-t 27` ile "%99 kesme" (kaynaksız; aracın kendi
> ölçümü %63–85; bizim sentetik sınamamızda düşük kontrastlı kesmenin 6'sından 3'ü) ·
> raporun benchmark tablosunun yarısı (yanlış makaleye atıf — denetim §2) · `tblend +
> blackframe` statik kart testi (yavaş timelapse'te her kareyi "statik" sayıyor).

---

# 0. 🚪 KURAL

```
Model SAYMAZ, SÜRE ÖLÇMEZ, HIZ TAHMİN ETMEZ.
Rubrikte sayı isteyen her soru ya ÖLÇÜLMÜŞ OLGULAR bloğundan cevaplanır ya da
"NOT VERIFIABLE" alır. Modelin raporundaki her zaman damgası makine ölçümüyle
karşılaştırılır (§5); dosya dışına düşen damga raporu bağlayıcılıktan düşürür.
```

Ölçülmüş bedeli (06.10.2026 denetimi):

| arıza | ne oldu |
|---|---|
| 2x kopya "kesik" okundu | en az 6 film — BROKEN CLIMB · STAR DOCK · STONE TOWER · DEEP STEP · BACK TO PLUMB · LAST LIFT (~1,5x); "56 sn yerine 32 sn'de bitiyor" → final vuruşu 0–3/10 |
| klip sayısı tahmin | aynı dosyada mercekler arası DEEP STEP 1·7·9·12·17·18 · STAR DOCK 2·8·23 · MOUNTAIN CROWN 7·8·12·16 |
| süre tahmin | aynı yatay dosya üç mercekte 109 · 125 · 148 sn (GLASS WALL) |
| beyan rubriğin dışında | 2x beyanı paket başlığında, "buradan aşağısı yapıştırılır" çizgisinin ÜSTÜNDE |
| kart varsayımı | on rubrik "dosya statik kartla biter" diyor; 2x'te 4 sn'lik 7. klip kart sanılabilir |

---

# 1. 🔬 NEDEN — model videoyu nasıl görüyor

```
Gemini API (dokümandan, 06.10.2026'da çekildi):
   · video varsayılan 1 kare/sn örneklenir; fps "processing" ayarıyla değiştirilebilir
   · kare başına ~70 token (düşük/orta çözünürlük) · 280 (yüksek)
   · zaman damgası MM:SS biçiminde anlaşılır
Gemini UYGULAMASI (sohbet): kaç kare örneklediği BELGELENMEMİŞ ❓
   (yardım sayfası yalnız boyut ve süre sınırı veriyor)
```

```
⇒ 2x dikey dosyada her klip 4 sn = 1 fps'te ~4 kare. Sabit kamerada kesme yalnız
  yapının bir aşama sıçramasıdır; 4 karelik klipte model bunu "hızlı timelapse"
  ile ayıramaz → klip sayar gibi yapar, sayamaz. Bizim ölçtüğümüz dağınıklık
  (1…23 klip) bununla tutarlıdır.
⭐ Bu bir rubrik sorunu değil, ÖLÇÜM ARACININ sınırıdır. Daha iyi cümle yazmak
  çözmez; sayıyı modelden ALMAK çözer.
```

---

# 2. 🧾 ÖLÇÜLMÜŞ OLGULAR BLOĞU

Rubriğin **içinde**, yapıştırma çizgisinin **altında**, ilk bölümdür — `RUBRIK_YAZIM §1`
format değişkenleriyle **tek blok**. Değerleri ajan aşağıdaki ölçümlerden doldurur:

```
FORMAT AND MEASURED FACTS — supplied by the operator. Do not re-estimate these.
PLAYBACK SPEED        2x  (1 second on this file = 2 seconds of the produced film)
CLIP COUNT            7
CLIP LENGTH ON FILE   4.0 s each
CUT TIMESTAMPS        0:04.0, 0:08.0, 0:12.0, 0:16.0, 0:20.0, 0:24.0
END CARD              NO — the last clip is a scene, score it
MUSIC                 NO — only site sound
ASPECT                9:16
FILE DURATION         0:28.0
FINAL HOLD            the last 1.0 s of the file is static (SSIM 0.97)
If what you see contradicts a line above, report the contradiction with a timestamp.
Do not change the line and do not score from your own estimate of it.
```

| satır | nereden | komut / araç |
|---|---|---|
| FILE DURATION · ASPECT | ffprobe | `ffprobe -v error -show_entries format=duration -of csv=p=0 f.mp4` · `ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x f.mp4` |
| PLAYBACK SPEED | plan (dikey = 2 · sahip kuralı) + süre/sahne bloğu oranı | `ihrac_kontrol.sh` ① (süre = blok/hız) |
| CLIP COUNT · CUT TIMESTAMPS | **`kesme_kontrol.sh --hiz`** (top-N: plan kaç kesme diyorsa en yüksek N skor) | `bash araclar/kesme_kontrol.sh f.mp4 <plan> --hiz 2` |
| END CARD | plan beyanı + `ihrac_kontrol.sh` ① (blok sonrası süre) | KAPAK KARTI satırı |
| MUSIC | plan + ses akışı | `ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 f.mp4` (boş = ses akışı yok) · müzik/saha sesi ayrımı KULAKLA (`ihrac_kontrol` ④) |
| FINAL HOLD | `ihrac_kontrol.sh` ③ SSIM | son 2,0/hız sn |

```
⛔ KESME TESPİTİNDE EŞİK KULLANILMAZ — top-N kullanılır.
   Sabit kamera + aynı yapı + yalnız aşama ilerleyen kesmede skor düşüktür:
   · gerçek teslimde ffmpeg scene skoru kesmelerde 0,016–0,022 [DERS 31 · A8-X2]
   · 06.10.2026 sentetik sınama (7 klip × 4 sn, yapı her kesmede 25 px sıçrıyor):
       PySceneDetect detect-content -t 27 (rapordaki komut)  → 6 kesmenin 3'ü
       PySceneDetect -t 10 → 5 · -t 5 → 6
       kesme_kontrol.sh --hiz 2 (top-N)                      → 6/6, marj 270 kat
   Eşik filme göre değişir; plandaki kesme SAYISI değişmez. Bu yüzden sayı plandan,
   YER ölçümden gelir; ikisi uyuşmazsa (marj dar) blok "CUT TIMESTAMPS NOT MEASURED"
   yazar ve ❷'nin kesme kategorileri NOT VERIFIABLE alır.
⛔ STATİK SON TESTİ tblend+blackframe ile YAPILMAZ: yavaş timelapse'te ardışık kareler
   zaten neredeyse aynı — sentetik sınamada 28 sn'lik dosyanın ~890 karesinin hepsini
   "siyah fark" saydı. ihrac_kontrol'ün SSIM'i kalır; o da yalnız "son N sn durağan mı"yı
   söyler, "kart mı yoksa yavaş final mi" ayrımını PLAN beyanı yapar.
```

---

# 3. 🎞️ HANGİ DOSYA — 2x yayın kopyası mı, 1x master mı

| dosya | artı | eksi |
|---|---|---|
| **2x yayın kopyası** | izleyicinin gördüğü şeyin aynısı (kanca, ritim, final süresi) | klip başına ~4 kare (1 fps) — kesme ve süreç ayrıntısı kaybolur |
| **1x master** | klip başına ~8 kare; parça parça yapım, kimlik, katılık daha okunur | ritim ve final süresi izleyicininki değil |

```
ÖNERİ (⚠️ sahip kararı — dosya seçimi QA'nın kapsamını değiştirir):
   1x MASTER   ❸ ŞANTİYE · ❹ İNŞA
               — soru "ne oldu, nasıl yapıldı"; kare yoğunluğu kazanır
   2x KOPYA    ❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❺ TESLİM   (kareler yine master'dan)
               — soru "izleyici ne gördü"; yayın dosyasının kendisi gerekir
   Her iki durumda ÖLÇÜLMÜŞ OLGULAR bloğu o dosyanın değerleriyle doldurulur
   (1x'te PLAYBACK SPEED 1x · CLIP LENGTH 8.0 s).
⭐ Master yoksa (yalnız 2x elde) hepsi 2x'le koşar; blok yine zorunludur.
⚠️ API'ye geçilirse (QA_KOSU §6) 2x kopyada fps 2'ye çıkarılarak klip başına 8 kare
   alınabilir — sohbet arayüzünde bu ayar yok.
```

---

# 4. 🖼️ KARE DESTEĞİ

```
BUGÜN   kare_al.sh klip başına üç kare → QA_KARELER/S<n>_{ilk,orta,son}.jpg
        (ad klip numarasını taşıyor, dosya saniyesini taşımıyor)
KURAL   · kare ADINA dosya saniyesi de eklenir (ör. S3_son_0m11.9.jpg) — model kareyi
          adıyla anar, saniyeyi tahmin etmez  ⚠️ kare_al.sh değişikliği · geçiş §6
        · dikiş çiftleri (S<n>_son · S<n+1>_ilk) ❸'ün çekirdeğidir, kesilmez
⚠️ KAREYE YAZI YAKMA (klip no + zaman damgası, rapor önerisi): bu makinedeki ffmpeg
   8.1 freetype'sız derlenmiş — `drawtext` filtresi YOK (sınandı). Yakma için
   freetype'lı ffmpeg ya da Python PIL gerekir; o güne kadar bilgi DOSYA ADINDADIR.
⚠️ İletişim tabakası (contact sheet) önerisinin kaynağı başka konuda bir makale çıktı
   (denetim §2) — ölçülmüş faydası YOK; denenirse tek değişkenli deney olarak.
```

---

# 5. ✅ DOĞRULAMA KATMANI — rapor geldikten sonra

Ajan her ham raporu kayda geçirmeden önce:

| # | kontrol | KALDI demek | eylem |
|:-:|---|---|---|
| D1 | dosya dışı damga | raporda FILE DURATION'dan büyük bir m:ss.s var | rapor BAĞLAYICI DEĞİL · `QA_KAYIT` durum YANLIŞ GİRDİ ya da EKSİK |
| D2 | klip sayısı | rapor CLIP COUNT'tan farklı sayı yazıyor (ör. "23 clips") | ilgili kategoriler NOT VERIFIABLE · ≥ %80'i ≤ 3 ise "ÇÖKÜK", ≥ %80'i ≥ 9 ise "ŞİŞİK" [DERS 105 · 106] · rapor notu |
| D3 | süre/hız itirazı | rapor "kesik · erken bitiyor · planlanan 56 sn" diyor | o bulgu ve ona bağlı puan DÜŞER (blok bunu baştan söylemişti) |
| D4 | kesme damgası | rapor bir kesmeyi CUT TIMESTAMPS'ten > 0,5 sn uzağa koyuyor | o bulgu doğrulanmadı (kareye bakılır) |
| D5 | kart | END CARD = NO iken rapor kartı puanlıyor | ⭐ ÖNCE DOSYA: klip_eslestir kuyruğu / kare panosu — kart dosyada YOKSA kategori NOT TRIGGERED; VARSA hata dosyanındır, rapor haklıdır [DERS 90 · POOL ROOM] |
| D6 | kurgu tablosu | raporun klip/kurgu tablosu ajanın 1 sn'lik kare panosuyla tutmuyor (kart görülmemiş, klip eksik) | o tabloya bağlı puanlar DÜŞER · kayıtta "ŞİŞİK" veya "ÇÖKÜK" etiketi [DERS 90 · 106] |

```
⭐ Tolerans ±0,5 sn (2x dosyada = 1 sn film zamanı) — VARSAYIM; ilk üç filmde
   ölçülür. kesme_kontrol'ün kendi toleransı 0,25 sn'dir (makine ↔ plan).
⛔ İki ya da daha çok D-kaldısı olan rapor TEKRAR koşulur [QA_KOSU §4].
```

---

# 6. 🔧 GEÇİŞ — bugünden yarına

```
1. qa_paket.sh   ÖLÇÜLMÜŞ OLGULAR bloğunu ölçüp doldurur ve rubriğin İÇİNE, yapıştırma
                 çizgisinin ALTINA basar (bugünkü 2x beyanı çizginin üstünde — DERS 63'ün
                 açığı). kesme_kontrol marjı darsa CUT TIMESTAMPS NOT MEASURED.
2. rubrikler     "ends with a static end card" vb. RUBRIK_YAZIM §6 listesiyle temizlenir.
2b. kare_al.sh   kare adına dosya saniyesi (§4).
3. ham rapor     D1–D6 elle; sayaç/betik U-kontrolleriyle birlikte otomatikleşir [QA_KAYIT §5].
4. yeniden koşu  seçilen filmler beş mercekle, blokla koşulur [ARSIV_12_MERCEK/00_ARSIV.md §6].
⭐ 06.10.2026: 1 ve 2 YAPILDI — qa_paket.sh bloğu ölçüp rubriğin içine basıyor (--master ile
   ❸ ❹ 1x'ten); beş rubrik temiz yazıldı. 2b ve 3 açık.
```
