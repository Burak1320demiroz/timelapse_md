# 📐 RUBRİK YAZIM KILAVUZU — rubrik bir ölçüm aracıdır

> `QA/00_README §5` rubriğin **dilini** söyler (salt İngilizce · tarihsiz · film adsız).
> Bu kılavuz rubriğin **ölçü mimarisini** söyler: format değişkenleri bloğu, çapalı
> ölçek ve 10'un kanıtı, koşullu kategori, puanın kodda hesaplanması, öldürücü hüküm
> ve aynı kusurun yalnız BİR mercekte puan kırması.
>
> Kaynak: A22 · 06.10.2026 (`arastirma/SONUCLAR/A22_GEMINI_HAM.md`) · denetim
> `A20-A24_DENETIM.md` · tetikleyen: 06.10.2026 QA denetimi.
> ⭐ Rapordan inen: format değişkenleri bloğu · "kanıt yoksa en fazla 7" · ortalamanın
> kodda hesaplanması · telafi etmeyen (öldürücü) kapı · kusur sahipliği (ayırt edici
> geçerlilik). ⭐ 06.10.2026: 12 mercek 5'e indi (QA/00_README) — çift sayım büyük ölçüde
> BİRLEŞTİRMEYLE çözüldü; §5 artık beş merceğin sınırıdır. ⛔ İnmeyen: "hüküm kategorilerden türetilir" (§4.3 — kısmen) · havuzlu
> mikro-ortalama (§4.2) · rapordaki iskelet (müzik kategorisini zorunlu alan yapıyor ·
> "Promise < 5 → FAIL" bizim mercek yapımızı bilmiyor). Rapordan SAYI inmedi.

---

# 0. 🚪 DÖRT KURAL

```
① FORMAT DEĞİŞKENLERİ RUBRİĞİN İÇİNDEDİR. Hız, klip sayısı, kart, müzik plandan ve
  ölçümden gelir; rubrik onları VARSAYMAZ. Değişkene bağlı kategori, değişken "yok"
  diyorsa NOT TRIGGERED'dır.                                                     §1
② 7'NİN ÜSTÜ KANITLA KAZANILIR. 8–10 için zaman damgası (m:ss.s) + görünen şey yazılır;
  yazılmadıysa kategori puanı en fazla 7'dir.                                    §2
③ ORTALAMAYI MODEL DEĞİL KOD HESAPLAR. Modelin AVERAGE satırı okunmaz; kategori
  puanlarından RUBRİK puanı, rubrik puanlarından FİLM puanı ajan tarafından çıkar. §4
④ HER KUSURUN TEK SAHİBİ VAR. Bir kusur yalnız sahibi olan mercekte puan kırar; öteki
  mercekler onu "SEE LENS n" diye ANAR, puan KIRMAZ.                             §5
```

Ölçülmüş bedeli (06.10.2026 denetimi):

| arıza | kural |
|---|---|
| rubrikler "dosya statik kartla biter", "six shots", BPM/ölçü uzunluğu varsayıyor; 2x'te 4 sn'lik 7. klip kart sanılabilir | ① |
| son 15 filmin 177 mercek raporunun 55'i (%31) tam 10,0 — çoğu "kusur tespit edilmedi" dışında kanıtsız | ② |
| 5 raporda yazılan ortalama hesapla tutmuyor; koşullu kategorinin ortalamaya girip girmediği 11 rubrikte yazılı değil | ③ |
| bir boşta ekskavatör ⑦ ⑧ ⑨ ⑩'da dört kez puan kırıyor | ④ |
| BROKEN CLIMB ④: hüküm "ENDS", aynı raporun final vuruşu 3/10 | §4.3 |

---

# 1. 🧾 FORMAT DEĞİŞKENLERİ BLOĞU

Rubriğin **en başında**, yapıştırma çizgisinin **altında** durur (README §5'e uyar: içine
film adı ve tarih girmez, yalnız değişkenler). Değerleri ajan doldurur — plan beyanından
ve `QA_OLCUM_ZEMINI §2` ölçümünden. İki blok tek bloktur:

```
FORMAT AND MEASURED FACTS — supplied by the operator. Do not re-estimate these.
PLAYBACK SPEED        {SPEED}x  (1 second on this file = {SPEED} seconds of the produced film)
CLIP COUNT            {CLIP_COUNT}
CLIP LENGTH ON FILE   {CLIP_SECONDS} s each
CUT TIMESTAMPS        {CUTS}
END CARD              {END_CARD}
MUSIC                 {MUSIC}
ASPECT                {ASPECT}
FILE DURATION         {DURATION}
FINAL HOLD            {FINAL_HOLD}
If what you see contradicts a line above, report the contradiction with a timestamp.
Do not change the line and do not score from your own estimate of it.
```

```
⛔ Değişkene bağlı kategoriler (beş mercek):
     ❷ MUSIC ALIGNMENT · ❺ müzik maddesi                    → MUSIC = NO ise NOT TRIGGERED
     ❷ RHYTHM                                               → klipler eşit uzunluktaysa NOT TRIGGERED
                                                              (dikey 7 × 8 sahip kuralı — kusur değil)
     ❷ son saniyeler · kart devri · ❶ kart bölümü           → END CARD = NO ise yalnız final tutuşu
     ❺ FINAL BEAT · HOOK · LOOP zaman damgaları              → plan saniyesi ÷ PLAYBACK SPEED
⭐ Kart ve müzik planda beyanlıdır (KAPAK KARTI · MÜZİK satırları — ihrac_kontrol.sh okur);
   bloğa ihrac_kontrol'ün ÖLÇTÜĞÜ değer yazılır, beyan ile ölçüm çelişirse DERS 63 işler.
```

---

# 2. 📏 ÇAPALI ÖLÇEK VE 10'UN KANITI

## 2.1 Çapalar

Her kategoride beş çapa yazılır; **çapa davranıştır, sıfat değildir** (BARS):

```
10  <the category's question> holds in every clip; named evidence at m:ss.s
 7  holds, with at most one minor exception, or holds but no timestamped evidence was given
 5  one clear failure a viewer would notice once
 3  repeated failures, or one failure that breaks the film's premise
 0  the category's question fails throughout
```

## 2.2 Kanıt kuralı — İngilizce cümle, her rubriğin puanlama bölümüne

```
EVIDENCE RULE. A category score above 7 requires at least one timestamp (m:ss.s)
and the visible thing at that timestamp that shows the category holding. "No defect
found" is not evidence. Without it, the highest score for that category is 7.
```

```
⭐ Neden 7: 7 "tutuyor ama kanıtlanmadı" demektir — film cezalandırılmaz, tavan kalkmaz.
   %31'lik 10,0 yığınının ne kadarı kanıtlı, ilk üç filmde ölçülür (QA_KALIBRASYON §1).
⚠️ VARSAYIM: raporun kendisi bu kuralı [VARSAYIM] etiketiyle verdi; ölçülmüş etkisi YOK.
   İlk üç filmden sonra 10,0 oranı ve kanıtlı 10 oranı yazılır; düşmezse kural düşer.
```

## 2.3 Evet/hayır kapıları

Bir kategorinin sorusu tek bir olgusa (kamera oynadı mı · yapı değişti mi · kart var mı)
0–10 yerine **YES / NO + zaman damgası** sorulur. Kontrol listesi biçimi modelin
"8 mi 9 mu" kararsızlığını kaldırır (A22-c · CheckEval) ve öldürücü kapı (§4.3) bu
satırlardan beslenir.

---

# 3. 🔀 KOŞULLU KATEGORİ

```
Koşul satırı her koşullu kategorinin İLK satırıdır ve değişken bloğuna bağlanır:
   "Open only if END CARD = YES." · "Open only if a crane is visible in any clip."
NOT TRIGGERED → puanı YOKTUR; rubrik puanının paydasına GİRMEZ (§4.1).
TRIGGERED     → puanlanır ve paydaya girer.
```

⛔ 12 mercekte yalnız `1_KARE_QA.md` "include it in the average" diyordu; on bir rubrik susuyordu.
Beş merceğin hepsi bu kuralı aynı cümleyle taşır. Yer tutucuları (`{SPEED}` …) `qa_paket.sh`
ölçüp doldurur [QA_OLCUM_ZEMINI §2].

---

# 4. ➗ BİRLEŞTİRME — kodda

## 4.1 Rubrik puanı

```
RUBRİK PUANI = tetiklenen kategorilerin aritmetik ortalaması (NOT TRIGGERED dışarıda)
               — ajan modelin kategori satırlarından hesaplar; modelin AVERAGE satırı
                 yalnız tutarlılık kontrolüdür (fark > 0,1 → raporda not)
```

## 4.2 Film puanı — mercek başına eşit ağırlık KALIR

```
FİLM PUANI = TAM durumlu merceklerin rubrik puanlarının ortalaması   [QA_KAYIT §1.2]
             + yanında N (kaç mercek TAM) — "8,4 (N=10)"
```

```
⚠️ ÇELİŞKİ — rapor havuzlu mikro-ortalama önerdi (bütün kategoriler tek havuza).
   İnmedi: her mercek TEK SORUDUR ve kategoriler o sorunun alt kanıtıdır. Raporun gördüğü
   asimetri (4 kategorili mercek 8 kategorilinin iki katı ağırlık) 12 mercekte gerçekti ve
   sebebi çakışmaydı; beş mercekte her mercek 8 kategori taşır ve çakışan sorular birleşti.
```

## 4.3 Öldürücü hüküm — telafi etmeyen kapı

```
FİLM HÜKMÜ:
  ❶ SEPARATE IMAGES · ❸ REBUILT EVERY SHOT · ❹ DIFFERENT
  bunlardan biri → FİLM DÜŞTÜ — ortalama ne olursa olsun    (eski asgari set ① ② ⑤'in karşılığı)
  ❺ STOPS · ❸ PARKED · ❹ APPEARING · ❹ INTRUDERS → yeniden üretim sebebi, film puanı yanında yazılır
  ⚠️ ❺'in öldürücü listeye girmesi sahip kararıdır (rapor "Promise < 5" önerdi).
```

```
⚠️ "HÜKÜM KATEGORİLERİ YENER" kuralı — rapor ters çevirmeyi önerdi; KISMEN indi:
   kural, ortalamanın yakalamadığı DÜZ ama kusursuz filmi yakalamak için var (⑥ METRONOM).
   O yön korunur. Ters yön korunmaz:

   KÖTÜ OLAN KAZANIR. Hüküm kötü, kategoriler iyiyse → hüküm (bugünkü kural).
                      Hüküm iyi, sahip kategori ≤ 3 ise → rapor TUTARSIZDIR:
                      puan bağlayıcı sayılmaz, mercek TEKRAR koşulur [QA_KOSU §4].
   Örnek (arşiv): BROKEN CLIMB ④ "ENDS" + FINAL BEAT 3/10 → tutarsız (ve 2x yanlış okuması).
```

---

# 5. 🏷️ KUSUR SAHİPLİĞİ — her kusur tek mercekte puan kırar

Beş merceğin sınırı. Rubrikler bu tabloyu İngilizce sınır cümlesiyle taşır
("<defect> belongs to Lens <n>. Write SEE LENS <n> with the timestamp and do not lower a score here").

| kusur | SAHİBİ | eski karşılığı |
|---|:-:|---|
| kamera oynadı · kadraj/çapa değişti · güvenli alan | ❶ | ① C1–C5 |
| kadrajda okunur yazı · logo · filigran | ❶ | ① C6 |
| insan ve araç çizimi · yüzeyde render görünümü | ❶ | ① C7 C8 · ⑫ C7 |
| katı nesne klip İÇİNDE erir · biçim/sayı/boy değiştirir · içinden geçer · silikleşerek belirir | ❶ | ⑫ C1–C6 C8 |
| güneş · gölge · mevsim · gök · tek saat · pozlama | ❷ | ③ C1–C6 C8 |
| kesme "zaman" mı "sıradaki" mi · sıçrama boyu · kesmeyi geçen çapa · son saniyeler | ❷ | ③ C7 · ⑥ C2–C5 C8 |
| yapı DIŞINDA bir şey kesmede taşınmıyor (makine · nesne · zemin · yol · bitki · su · aşınma · insan) | ❸ | ⑤ C1–C8 |
| şantiye duruyor · boşta makine · amaçsız ya da döngüsel hareket | ❸ | ⑦ C1 C2 C4 · ⑨ C1–C3 |
| büyümeyi yapan görünmüyor · iş gücü büyümeye yetmiyor · malzeme akmıyor | ❸ | ⑦ C3 C5–C7 · ⑩ C2 C3 |
| yapı başka yapı oldu · küçüldü · ölçek kaydı | ❹ | ② C1–C3 C8 |
| parça tamamlanmış belirdi · yöntem/eli görünmüyor · sıra yanlış | ❹ | ⑧ C2–C6 · ⑩ C1 · ② C4 |
| yük yolu · geçici işler · makine yöntemi · malzemenin kaynağı | ❹ | ② C5–C7 · ⑧ C7 · ⑩ C4 |
| planda olmayan (davetsiz) nesne · planda olup gelmeyen | ❹ | ⑪ C1–C6 |
| vaat · direnç · final vuruşu · kanca · döngü · kapak · ses yatağı | ❺ | ④ C1–C8 |

```
⭐ Klip İÇİ ↔ kesme ARASI ayrımı: bir makine klip içinde biçim değiştirirse ❶ (katılık);
   kesmede başka makine olursa ❸ (dünya). Yapının kendisi her iki durumda ❹.
⭐ Davetli mi (❹) ↔ katı mı (❶) aynı nesneye FARKLI soru — ikisi birden doğru olabilir
   (arşiv: DEEP STEP kamyonu ⑪ davetsiz · ⑫ HOLDS).
```

---

# 6. 🧹 ESKİ VARSAYIMLAR — beş mercekte temizlendi

12 mercekli rubriklerde bulunan ve yeni rubriklere TAŞINMAYAN varsayımlar (06.10.2026 denetimi ·
satırlar `QA/ARSIV_12_MERCEK/` dosyalarınındır):

| eski | varsayım | beş mercekte |
|---|---|---|
| 1_KARE 59 · 68 · on rubriğin girişi | "dosya statik kartla biter" · kart "öteki çekimlerden kısa" | END CARD değişkeni |
| 1_KARE 232 · 279 · 4_TESLIM 140 · 177 · 6_GECIS 147 · 174 | "six shots" · "sixty seconds" · "ten cuts" · "eleventh scene" | CLIP COUNT |
| 4_TESLIM 129 · 146 · 195 | plan saniyesi = dosya saniyesi · süre ±0,5 sn | ÷ PLAYBACK SPEED · süre ölçülmüş olgu |
| 4_TESLIM 198–200 · 6_GECIS 57–58 · 161–176 | iki müzik maddesi · TEMPO · BAR LENGTH · MUSIC ALIGNMENT koşulsuz | MUSIC = NO → NOT TRIGGERED |
| 6_GECIS C1 | kesme mekaniği (flaş kare · geçiş) | makine (kesme_kontrol) |
| 6_GECIS 243 | kart devri NOT TRIGGERED seçeneksiz | END CARD = NO → yalnız final tutuşu |
| 9_FAALIYET 26–27 · 3_ZAMAN | kör mercekte "belge yoksa…" · beyan yoksa RUN INCOMPLETE | kör mercek belge istemez; QUESTIONS FOR THE DOCUMENT |
| on bir rubrik | koşullu kategorinin ortalamaya girişi yazılı değil | §3 cümlesi her rubrikte |
| hepsi | kanıt kuralı yok · AVERAGE'ı model yazar | §2.2 cümlesi · AVERAGE yok, ajan hesaplar |

---

# 7. 🦴 İSKELET — yeni ya da yeniden yazılan rubrik

```
# <LENS NAME>
<one question, one paragraph: what this lens measures and what it does not>

FORMAT AND MEASURED FACTS — supplied by the operator. Do not re-estimate these.
<§1 block>

BEFORE YOU SCORE — first three lines of your report:
FILE NAME AS SHOWN · DOCUMENTS ATTACHED (first line of each, or NONE) · CLIPS YOU CAN SEE

RULES
- Timestamps are m:ss.s on this file.
- NOT VISIBLE / NOT VERIFIABLE is not a zero.
- <defect> belongs to Lens <n>. Write SEE LENS <n> with the timestamp; do not lower a score here.
- EVIDENCE RULE: <§2.2>

## CATEGORY 1 — <NAME>
<question> · anchors 10 / 7 / 5 / 3 / 0 <§2.1>
## CONDITIONAL — <NAME>
Open only if <variable or visible condition>. If not, write NOT TRIGGERED; it does not
enter the average.

FINDINGS        m:ss.s · what is visible · which category
SCORES          one line per category: n NAME  x/10 | NOT TRIGGERED · evidence m:ss.s
VERDICT         <A> / <B> — one line, independent of the scores
<lens-specific line>  (e.g. FIRST PIECE THAT APPEARED: name · m:ss.s / NONE)
QUESTIONS FOR THE DOCUMENT   (mode V lenses only)
```

```
⭐ Önce bulgular, sonra puan satırları: gerekçe puandan ÖNCE yazılır.
⚠️ Sohbet arayüzünde JSON şeması zorlanamaz; SCORES satırları sabit biçimdedir ve ajan
   onları okur. API'ye geçilirse (QA_KOSU §6) aynı alanlar yapılandırılmış çıktıya taşınır.
⛔ İskelet README §5'e uyar: içine Türkçe · tarih · film adı · ders numarası · yol girmez.
```
