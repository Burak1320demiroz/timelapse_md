# ⚖️ QA KALİBRASYON KILAVUZU — hakemi ölçmeden filmi sıralama

> Rubrik (`RUBRIK_YAZIM`) ölçeği kurar; koşu (`QA_KOSU`) girdiyi temizler. Bu kılavuz
> **ölçeği kullananı** ölçer: aynı filme iki kez aynı puanı veriyor mu (test-tekrar),
> kusuru BİLİNEN bir videoda kusuru buluyor mu (tohumlanmış kusur seti), zamanla
> kayıyor mu, mercekler birbiriyle çelişince hangisi geçer — ve QA puanı izleyiciyle
> tutuyor mu (dış geçerlilik).
>
> Kaynak: A23 · 06.10.2026 (`arastirma/SONUCLAR/A23_GEMINI_HAM.md`) · denetim
> `A20-A24_DENETIM.md` · tetikleyen: 06.10.2026 QA denetimi.
> ⭐ Rapordan inen: test-tekrar ve medyan · bilinen cevaplı test · "belirli kanıt genel
> 'kusursuz'u yener" · sıra korelasyonu + güç hesabı. Güç sayısı bu makinede yeniden
> hesaplandı (rapor 28 dedi, hesap 29–30). Tohumlama komutlarının 10'undan 5'i olduğu
> gibi kullanılamadı (2 koşmadı · 3 yanlış kusur üretti) — §3'tekiler bu makinede
> sınanmış hâlleridir. ⛔ İnmeyen: izleyici eşikleri (%70 "viewed", "2–3 sn dikkat") —
> forum/blog kaynaklı · EWMA kontrol grafiği (bizim hacmimizde basit eşik yeter, §4).

---

# 0. 🚪 KURAL

```
Bir puan farkı, aynı filmin iki koşusu arasındaki farktan büyük değilse BİLGİ DEĞİLDİR.
Hakemin gürültüsü ölçülmeden iki film "şu daha iyi" diye sıralanmaz, bir rubrik
değişikliği "işe yaradı" denmez.
```

Ölçülmüş bedeli (06.10.2026 denetimi):

| arıza | ne oldu |
|---|---|
| test-tekrar YOK | hiçbir film aynı mercekle iki kez koşulmadı |
| hakem filmi değil girdiyi ölçtü | 24–28.09 ortalamaları 9,7–9,8 → 04–05.10'da 7,4–8,4; aynı hafta 2x kopya, eksik ve yanlış belge girdi — film mi değişti hakem mi, ayrılamıyor |
| mercekler çelişiyor | DEEP STEP ⑪ "modern kamyon davetsiz" · ⑫ aynı kamyona "HOLDS"; BROKEN CLIMB ① 4,1 (kamera sıçraması) · ⑦ 10/10 "kusur yok" |
| iki denetim iki hüküm | STONE DRAGON: biri RED, biri ONAY |
| dış geçerlilik hiç sınanmadı | `IZLEYICI_DEFTERI` boş; QA_CAPRAZ_ANALIZ 18.09'da kaldı |

---

# 1. 🔁 TEST-TEKRAR

## 1.1 Pilot — önce gürültüyü ölç

```
3 film × 4 mercek × 3 koşu = 36 koşu
   filmler   bir yüksek (DEEP END) · bir orta (STONE TOWER) · bir düşük (STONE DRAGON)
   mercekler ❶ GÖRÜNTÜ · ❸ ŞANTİYE · ❹ İNŞA · ❺ TESLİM   (üç öldürücü + teslim · iki kör · iki belgeli)
   koşu      her biri AYRI geçici sohbette, proje dışında, aynı rubrik sürümü,
             aynı dosya (sha256 künyede) [QA_KOSU §1]
ölçülen      mercek başına aralık (en yüksek − en düşük) ve hükmün değişip değişmediği
```

## 1.2 Karar eşikleri — pilotun ardından

| mercek aralığı (3 koşu) | anlamı | eylem |
|---|---|---|
| ≤ 0,5 ve hüküm aynı | kararlı | tek koşu yeter; puan olduğu gibi |
| 0,5 – 1,5 ya da hüküm bir kez döndü | gürültülü | puan **3 koşunun medyanı**; tabloda aralıkla ("8,1 [7,4–8,6]") |
| > 1,5 ya da hüküm iki yöne | ölçemiyor | merceğin puanı film ortalamasına GİRMEZ; rubrik `RUBRIK_YAZIM`'a göre yeniden yazılır |

```
⚠️ Eşikler bizim seçimimizdir (VARSAYIM). Literatürdeki uyum eşikleri kayda geçer ama
   üç koşuda hesaplanmaz: ICC < 0,50 zayıf · 0,50–0,75 orta · 0,75–0,90 iyi · > 0,90
   mükemmel (Koo & Li 2016); Krippendorff α ≥ 0,80 güvenilir · 0,667–0,80 ihtiyatlı.
   ICC(2,1) — mutlak uyum — ≥ 10 film × 3 koşu biriktiğinde hesaplanır.
⭐ Medyan, ortalama değil: tek bir uçuk koşu (2x yanlış okuması gibi) medyanı oynatmaz.
```

## 1.3 Maliyet — hepsi üç koşu değil

```
⛔ 5 mercek × 3 koşu = film başına 15 koşu (12 mercekte 36'ydı). Varsayılan:
   · öldürücü hüküm mercekleri (❶ ❸ ❹ — RUBRIK_YAZIM §4.3) → 3 koşu
   · ❷ ❺ 1 koşu → film başına 11 · pilotta "gürültülü" çıkan mercek 3 koşuya terfi eder
   ⚠️ Sahip kararı: film başına koşu bütçesi.
⚠️ ÇELİŞKİ (A20 ↔ A23 ↔ kaynak): A20 "sıcaklık 0 = deterministik" diyor; A23 "sıcaklık
   0'da bile 3 koşunun yalnız %61,3'ü aynı" diyor — kaynak çekildi: o çalışma Qwen3'ü
   sıcaklık 0,6'da koşmuş. Google'ın kendi dokümanı "çoğunlukla deterministik, küçük
   sapma olabilir" diyor; Gemini 3 rehberi sıcaklığı 1,0'da bırakmayı öneriyor; sohbet
   arayüzünde sıcaklık zaten ayarlanamaz. Kural: determinizm VARSAYILMAZ, ÖLÇÜLÜR (§1.1).
```

---

# 2. ⚔️ MERCEKLER ÇELİŞİNCE

```
1. Önce sahiplik: kusurun sahibi olan mercek karar verir [RUBRIK_YAZIM §5].
2. Sahip mercek "kusur yok" diyor, başka mercek ZAMAN DAMGALI kusur gösteriyor →
   ajan o kareyi açar (kare_al.sh çıktısı ya da ffmpeg -ss) ve bakar:
      · kusur karede görünüyor   → sahip merceğin o kategorisi kanıtsız 10 sayılır,
                                   en fazla 7 [RUBRIK_YAZIM §2.2] · OLAY TABLOSU'na E-satırı
      · görünmüyor               → iddia eden mercek "NOT VERIFIABLE" sayılır
3. Zaman damgasız "kusursuz" hiçbir zaman zaman damgalı kusuru yenmez.
```

```
⭐ (arşiv) DEEP STEP kamyonu: ⑪ (davetli mi) ile ⑫ (katı mı) aynı nesneye FARKLI soru soruyor —
   ikisi birden doğru olabilir. Çelişki değildir; sahiplik tablosu ikisini ayırır.
   (arşiv) BROKEN CLIMB ① ↔ ⑦: aynı soru değil ama ⑦'nin "her klipte 0,0 sn boşta" satırı
   kanıtsız 10'dur → §2 madde 2 işler.
```

---

# 3. 🧪 TOHUMLANMIŞ KUSUR SETİ — bilinen cevaplı test

## 3.1 Ne zaman

```
· bir rubrik yeniden yazıldığında (RUBRIK_YAZIM §6)
· Gemini sürümü değiştiğinde (künyedeki model satırı)
· arayüz değiştiğinde (sohbet → API)
· en geç ayda bir
```

## 3.2 Set

Kaynak: sahibin elindeki **iyi bir filmin 2x yayın kopyası** (öneri: THE DEEP END — en
yüksek ortalama; mp4 depoda yok, sahip verir). Her satır tek kusur; beklenen yakalayan
mercek sahiplik tablosundan. Komutların hepsi **06.10.2026'da bu makinede (ffmpeg 8.1)
28 sn'lik 7 klipli sentetik dosyada koştu** — rapordaki hâllerinden farklı olanlar işaretli.

| # | kusur | sahip | komut | not |
|:-:|---|:-:|---|---|
| 1 | 12. sn'de kadraj 48 px kayar | ❶ | `ffmpeg -i in.mp4 -vf "crop=iw-48:ih-48:x='if(gte(t,12),48,0)':y='if(gte(t,12),48,0)',scale=1080:1920" -c:a copy 01_kayma.mp4` | ⚠️ rapordaki `crop=iw:ih/2:0:t*300` dosyayı 1080×960'a çeviriyordu — kayma değil boyut değişimi |
| 2 | dosya bir kez daha 2x | ❷ ❺ (olgu bloğu ile çelişki) | `ffmpeg -i in.mp4 -filter:v "setpts=0.5*PTS" -an 02_hiz.mp4` | ✅ 28 → 14 sn |
| 3 | köşede logo yaması | ❶ | `ffmpeg -i in.mp4 -vf "drawbox=x=40:y=60:w=360:h=110:color=white@0.85:t=fill" 03_logo.mp4` | ⚠️ rapordaki `drawtext` bu makinede YOK (ffmpeg freetype'sız) |
| 4 | son klip eksik | ❺ | `ffmpeg -i in.mp4 -t 24 -c copy 04_eksik_son.mp4` | ✅ (anahtar kareye göre 24,07 sn) |
| 5 | 5–6 sn kara leke | ❶ | `ffmpeg -i in.mp4 -vf "drawbox=x=100:y=100:w=300:h=300:color=black:t=fill:enable='between(t,5,6)'" 05_leke.mp4` | ⚠️ rapor "nesne kaybolur" dedi — bu bir nesne EKLER; kaybolma testi değildir |
| 6 | 8–12 sn renk kayması | ❷ | `ffmpeg -i in.mp4 -vf "colorbalance=gs=0.5:enable='between(t,8,12)'" 06_renk.mp4` | ✅ |
| 7 | 8–12 sn yapı bölgesi %70'e ezilir | ❹ | `ffmpeg -i in.mp4 -filter_complex "[0]split[a][b];[b]crop=400:900:340:600,scale=400:630[s];[a][s]overlay=340:870:enable='between(t,8,12)'" 07_ezik.mp4` | ⚠️ rapordaki `scale=…:enable=` KOŞMADI (scale zaman çizelgesi desteklemez); kırpma alanı filme göre ayarlanır |
| 8 | 15–20 sn bulanık | ❶ | `ffmpeg -i in.mp4 -vf "boxblur=10:enable='between(t,15,20)'" 08_bulanik.mp4` | ✅ |
| 9 | 10–12 sn kare donar, süre aynı | ❸ | `ffmpeg -i in.mp4 -i in.mp4 -filter_complex "[0][1]freezeframes=first=300:last=359:replace=300" 09_donma.mp4` | ⚠️ rapordaki `loop=60:1:300` 2 sn EKLİYORDU (28 → 30 sn) — sonraki bütün kesmeler kayar |
| 10 | karanlık pozlama | ❷ | `ffmpeg -i in.mp4 -vf "eq=brightness=-0.8" 10_karanlik.mp4` | ✅ |
| 0 | **temiz kopya** (değiştirilmemiş) | — | `cp in.mp4 00_temiz.mp4` | yanlış alarm ölçüsü |

```
⛔ SINIR — bu set KABA kusurları ölçer. Bizim gerçek arızalarımız (yapı kesmede başka yapı
   olur · parça belirir · makine kimliği değişir) ffmpeg ile tohumlanamaz. Onların bilinen
   cevaplı hâli ELDE VAR: ölçülmüş arızalı klipler (DERSLER'deki zaman damgalı olaylar).
   Set'e ikinci kuşak olarak "geçmiş arızalı kesitler" eklenir — kaynak: RAPORLAR OLAY
   TABLOSU satırları ve sahibin elindeki dosyalar.
```

## 3.3 Geçti / kaldı

```
YAKALADI   sahip mercek kusuru, ±0,5 sn içinde zaman damgasıyla adlandırdı
           (ya da ilgili kategoriyi ≤ 5 verdi)
PAS        10 kusurun en az 8'i yakalandı VE temiz kopyada sahte kusur ≤ 1
KALDI      → o mercek rubriği değişene kadar puanı film ortalamasına "(kalibrasyonsuz)"
             notuyla girer; ⚠️ eşik 8/10 VARSAYIMDIR, ilk koşudan sonra yeniden bakılır
```

---

# 4. 📈 KAYMA İZLEME — basit eşik

```
ÇAPA FİLM   temiz kopya (00_temiz) her kalibrasyonda aynı mercek setiyle koşulur.
            Çapa puanı önceki kalibrasyondan > 1,0 oynarsa: HAKEM DEĞİŞTİ.
            → bu tarihten önceki ve sonraki filmler AYNI TABLODA KARŞILAŞTIRILMAZ;
              tabloya "rubrik/hakem dönemi" sütunu girer [QA_KAYIT §2.1 rubrik + model satırı].
⭐ 9,8 → 7,4 düşüşü bu yüzden okunamıyor: çapa yoktu. Çapa puanı sabit kalırken film
   puanı düşerse düşüş filmdir; çapa da düşerse hakemdir.
⚠️ Rapor EWMA/CUSUM kontrol grafiği önerdi — haftada 1–3 film hacminde tek eşik yeter;
   ≥ 20 kalibrasyon noktası birikince yeniden düşünülür.
```

---

# 5. 👁️ DIŞ GEÇERLİLİK — QA puanı izleyiciyle tutuyor mu

```
VERİ      apexait/IZLEYICI_DEFTERI.md (7. gün · dört sayı) — tek kaynak.
          ⛔ QA_CAPRAZ_ANALIZ/06_IZLEYICI_DENEY_PLANI farklı ölçütler ve müzik ızgarası
             taşıyor (sahip kuralı 21.09 öncesi) → defter bağlayıcıdır, 06 arşivdir.
TEST      Spearman sıra korelasyonu: ❺ HOOK ↔ KAYDIRMADI % · ❺ LOOP ↔
          ORT. İZLENME % · film puanı ↔ ENGAGED. Pearson değil (puanlar dar bantta yığılı).
GÜÇ       α = 0,05 · güç 0,80 · Fisher z ile — bu makinede hesaplandı:
             ρ = 0,50 → 29–30 film      ρ = 0,40 → 47      ρ = 0,30 → 85
          (rapor ρ = 0,50 için 28 dedi; formül 29,0 veriyor)
          ⇒ defterdeki ~23 filmle yalnız ÇOK büyük ilişki görünür; ilk anlamlı okuma
            30 filmde. O güne kadar defter S1–S6 sorularını YÖN olarak okur [§3].
KARIŞTIRICI  yayın tarihi (kanal büyür · en iyi filmler en yeniler — C2) · konu ailesi ·
          rubrik/hakem dönemi (§4). Tarih ve dönem tabloda sütundur; karma model
          30 filmden önce kurulmaz.
```

```
⛔ İNMEYEN: "viewed < %70 → algoritma durdurur", "ilk 3 sn'de aksiyon swipe'ı %75'ten
   %42'ye indirir" (Reddit), "her 2–3 sn'de uyarıcı" (blog). Kaynak sınıfı forum/blog;
   sayı ölçülmemiş. 2x'te 4 sn'lik klip sahip kuralıdır (7 × 8 · 2x) ve bu iddiayla
   değişmez — defter S5 bunu kendi verisiyle sınar.
⭐ Ters çıkarsa (QA puanı izleyiciyle ters yönde): RUBRİK değişir, film değil
   [IZLEYICI_DEFTERI §3].
```
