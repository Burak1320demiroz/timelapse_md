# 🗄️ ARŞİV — 12 MERCEKLİ QA · 03.09–05.10.2026 · ⛔ DONDURULDU 06.10.2026

> Bu klasör eski QA sisteminin TAMAMIDIR: 12 rubrik · T1–T8 tabloları · 00_INDEX (sayaç + matris +
> film anlatıları) · RAPORLAR/ (31 film kaydı) · HAM_RAPORLAR/ (393 ham rapor · 37 film) ·
> QA_CAPRAZ_ANALIZ/ (18.09 çapraz analiz) · eski README (`00_README_12_MERCEK.md`).
> Yerine gelen: `QA/00_README.md` — **5 mercek** (❶ GÖRÜNTÜ · ❷ ZAMAN VE KESME · ❸ ŞANTİYE ·
> ❹ İNŞA · ❺ TESLİM).
>
> ⛔ Buradaki hiçbir dosya düzenlenmez. Ham raporlar zaten dokunulmazdı; artık RAPORLAR, INDEX ve
> tablolar da öyle. Eski belgelerdeki `QA/HAM_RAPORLAR/…`, `QA/RAPORLAR/…`, `QA/00_INDEX.md`,
> `QA/<n>_<MERCEK>_QA.md`, `QA/T<n>_….md` yolları artık `QA/ARSIV_12_MERCEK/…` altındadır.
> Canlı belgelerdeki yollar 06.10.2026'da güncellendi; arşivin İÇİNDEKİ yollar eski hâliyle kaldı.

---

## 1. Neden arşivlendi — 06.10.2026 denetimi

```
393 ham rapor tek tek sınıflandı (00_ESLEME.tsv):
   TAM 189 · BELGESİZ 98 · KARESİZ 71 · SIZINTI 18 · 2x OKUMA 7 · EKSİK 4 ·
   YANLIŞ BELGE 2 · BAĞLAYICI DEĞİL 2 · KAPAKSIZ 1 · YERİNE GEÇTİ 1
⇒ belge isteyen (mod D) koşuların YARISI belgesiz yapıldı (196'nın 98'i)
⇒ ④ TESLİM'in 36 koşusundan 9'u kullanılır · ⑥ 14/35 · ⑪ 10/26 · ⑧ 15/32 · ② 22/37 · ⑩ 16/28
⇒ ⑦ ⑧ ⑨ ⑩ aynı kusuru dört kez puanlıyordu; kategori sayısı 4–8 arası, ortalamaya eşit giriyordu
⇒ kullanılır koşuların %30'u (261'de 77) tam 10,0
⇒ INDEX elle tutuluyordu: 5 film "üretilmedi" ama 8–12 ham raporlu · STONE DRAGON "12 mercek" (9)
   · THE CROSSING'in 3 puanı hamsız
Ayrıntı: arastirma/SONUCLAR/A20-A24_DENETIM.md · kilavuzlar/QA_KAYIT · QA_KOSU · QA_OLCUM_ZEMINI
```

## 2. Eski → yeni mercek

| eski | yeni | not |
|---|---|---|
| ① KARE · ⑫ KATILIK | ❶ GÖRÜNTÜ | kamera · kare · yazı · insan/araç · yüzey · katılık |
| ③ ZAMAN · ⑥ GEÇİŞ | ❷ ZAMAN VE KESME | kesme mekaniği makineye geçti · müzik/ritim koşullu |
| ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET | ❸ ŞANTİYE | dikiş denetimi çekirdek · boşta/amaçsız/döngü tek yerde |
| ② İNŞA · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER | ❹ İNŞA | SPEC + plan · parça parça · davetli kadro |
| ④ TESLİM | ❺ TESLİM | plan saniyesi ÷ hız · süre ölçülmüş olgu · müzik koşullu |

⚠️ Eski puanlar yeni merceklerle KARŞILAŞTIRILMAZ (farklı ölçek, farklı kategori). Seçilen filmler
yeni merceklerle yeniden koşulur (sahip kararı 06.10.2026 — §6).

## 3. Durum tablosu — `00_ESLEME.tsv`

Her ham rapora bir satır: `dosya · film · mercek · durum · puan · olumsuz_hüküm · kaynak · not`.

| durum | anlamı | puan özetlere girer mi |
|---|---|:-:|
| TAM | doğru mod, doğru girdi, hüküm + kategoriler var | ✅ |
| KARESİZ | mod V · kare grabı verilmedi — puan var, kanıt zayıf | ✅ (zayıf) |
| KAPAKSIZ | mod D · yalnız kapak eksik | ✅ (zayıf) |
| BELGESİZ | mod D · plan/SPEC verilmedi | ❌ |
| SIZINTI | mod V · rapor plan/SPEC içeriği alıntılıyor | ❌ |
| 2x OKUMA | 2x yayın kopyası "kesik" okundu, puan buna dayanıyor | ❌ |
| YANLIŞ BELGE | başka filmin SPEC'i verildi | ❌ |
| EKSİK · BAĞLAYICI DEĞİL · YERİNE GEÇTİ | puan satırı yok · serbest denetim · ikinci koşu | ❌ |

```
kaynak = otomatik  → betikle sınıflandı (ilk satır · AVERAGE · "not supplied" · kare/belge eksikliği)
kaynak = elle      → SIZINTI · 2x OKUMA · YANLIŞ BELGE · YERİNE GEÇTİ satırları elle doğrulandı
⚠️ SIZINTI listesi ALT SINIRDIR: yalnız açık alıntılar (G7 · "şartname" · rejim · plan sayıları) sayıldı.
⚠️ olumsuz_hüküm betikle okundu (VERDICT bölümündeki cevap); kesin karar için ham dosya.
```

## 4. Temizlenmiş film tablosu

"kullanılır ort." = TAM + KARESİZ + KAPAKSIZ koşuların AVERAGE'ı; N = kaç mercek. Öldürücü
hüküm = kullanılır koşuda ① AYRI GÖRÜNTÜ · ② FARKLI YAPI · ⑤ YENİDEN KURULMUŞ (eski asgari set).
Sıra: ham raporların depoya giriş tarihi (koşu tarihi değil).

| film | biçim | kayıtlı ort. (N) | **kullanılır ort. (N)** | öldürücü hüküm | not |
|---|:-:|:-:|:-:|---|---|
| BEFORE NIGHTFALL | dikey | 3,69 (8) | **4,17** (4) | ① AYRI GÖRÜNTÜ · ⑤ YENİDEN KURULMUŞ | ⚠️ INDEX "üretilmedi" diyordu · kapsama 4/12 |
| BUILT FROM DUST | — | 2,34 (9) | **2,26** (5) | ① AYRI GÖRÜNTÜ · ⑤ YENİDEN KURULMUŞ | film klasörü depoda yok · kapsama 5/12 |
| OVER THE WALL | dikey | 4,97 (12) | **5,48** (6) | ① AYRI GÖRÜNTÜ · ⑤ YENİDEN KURULMUŞ | kapsama 6/12 |
| POLAR HABITAT | dikey | 8,76 (9) | **9,08** (5) | — | kapsama 5/12 |
| THE CLOSING SPAN | dikey | 1,55 (6) | **0,77** (3) | ① AYRI GÖRÜNTÜ · ⑤ YENİDEN KURULMUŞ | kapsama 3/12 · kart başka dünya (①③) |
| THE CROSSING | dikey | 7,73 (6) | **9,30** (4) | — | INDEX ④⑤⑥ puanlarının hamı yok · kapsama 4/12 |
| THE DARK ROCK | dikey | 4,27 (12) | **3,77** (6) | ① AYRI GÖRÜNTÜ · ⑤ YENİDEN KURULMUŞ | kapsama 6/12 |
| THE DUST YEAR | dikey | 2,52 (8) | **2,65** (4) | ① AYRI GÖRÜNTÜ · ⑤ YENİDEN KURULMUŞ | kapsama 4/12 · kart başka dünya (①) |
| THE EMPTY RIDGE | dikey | 6,52 (12) | **6,68** (6) | ① AYRI GÖRÜNTÜ | kapsama 6/12 |
| THE LONG DAY | dikey | 5,66 (8) | **5,90** (4) | — | kapsama 4/12 |
| THE LONG SHADOW | dikey | 2,67 (4) | **3,80** (2) | ① AYRI GÖRÜNTÜ | v1 · kapsama 2/12 |
| THE MOUNTAIN DOOR | dikey | 2,32 (6) | **1,63** (3) | ① AYRI GÖRÜNTÜ · ⑤ YENİDEN KURULMUŞ | kapsama 3/12 |
| THE NARROW LOT | dikey | 5,17 (6) | **5,27** (3) | — | kapsama 3/12 |
| THE OLD ROAD | yatay | 7,78 (12) | **7,12** (6) | — | ⚠️ INDEX "üretilmedi" diyordu · kapsama 6/12 |
| ONE MORE TURN | dikey | 5,90 (12) | **6,33** (6) | ① AYRI GÖRÜNTÜ · ⑤ YENİDEN KURULMUŞ | ⚠️ INDEX "üretilmedi" diyordu · kapsama 6/12 |
| THE SWALLOWED BUS | dikey | 9,12 (12) | **9,08** (11) | — | ⚠️ INDEX "üretilmedi" diyordu |
| BACK TO WATER | dikey | 8,75 (12) | **8,76** (9) | — | kart başka dünya (②) |
| THE EMPTY LOCK | dikey | 9,22 (12) | **9,30** (8) | — |  |
| THE QUIET FIELD | dikey | 9,72 (12) | **9,85** (8) | — |  |
| THE BLUE DOOR | dikey | 9,32 (12) | **9,31** (11) | — | kart başka dünya (①②③) |
| THE BROKEN CLIMB | dikey | 9,08 (12) | **9,39** (10) | — |  |
| THE DEEP END | dikey | 9,83 (12) | **9,81** (11) | — |  |
| THE STONE DRAGON | dikey | 7,51 (9) | **7,55** (5) | ⑤ YENİDEN KURULMUŞ | "12 mercek" değil, 9 · kapsama 5/12 |
| THE TIDE GATE | dikey | 8,52 (9) | **8,75** (8) | — | ⚠️ INDEX "üretilmedi" diyordu · kart başka dünya (②) |
| THE VANISHING ROOM | dikey | 9,62 (10) | **9,72** (8) | — |  |
| BACK TO PLUMB | dikey | 8,80 (12) | **8,77** (11) | — |  |
| THE FIRST GUEST | dikey | 9,66 (12) | **9,69** (11) | — |  |
| THE GLASS CROSSING | dikey | 9,04 (12) | **9,00** (10) | — |  |
| THE LAST FIRING | dikey | 9,57 (12) | **9,49** (9) | — |  |
| THE LAST HARBOR | dikey | 9,79 (12) | **9,81** (10) | — |  |
| THE LAST LIFT | dikey | 9,82 (12) | **9,85** (11) | — |  |
| THE MOUNTAIN CROWN | dikey | 6,15 (12) | **6,00** (9) | ⑤ YENİDEN KURULMUŞ | kart başka dünya (②③) |
| THE DEEP STEP | dikey | 7,72 (12) | **8,13** (6) | — | kapsama 6/12 |
| THE GLASS WALL | yatay | 8,94 (12) | **8,74** (10) | — |  |
| THE IRON BRIDGE | yatay | 7,65 (12) | **7,48** (8) | ① AYRI GÖRÜNTÜ |  |
| THE STAR DOCK | dikey | 7,42 (12) | **7,17** (4) | — | kapsama 4/12 |
| THE STONE TOWER | dikey | 8,38 (12) | **8,32** (6) | — | kapsama 6/12 |
```
OKUMA
· Eylül sonu yüksek filmleri temizlikten sonra da yerinde (DEEP END · LAST LIFT · FIRST GUEST ≈ 9,7–9,9 · N 11).
· Ekim düşüşü temizlikten sonra da görünüyor ama N 4–6 — film mi hakem mi AYRILAMAZ.
· SWALLOWED BUS (9,08 · N 11) ve TIDE GATE (8,75 · N 8) iyi ölçülmüş iki film; eski INDEX'te yoktu.
· "kart başka dünya" — kart filmdeki yapıyı göstermiyor (MOUNTAIN CROWN tipi) · DERS 63 kart kuralı.
```

## 5. Raporlar filmler hakkında ne söyledi — yeni dönem (19.09 sonrası · kullanılır koşular)

| kusur | eski mercek | ortalama | sıklık | yeni sahibi |
|---|---|:-:|---|:-:|
| insan ve araç çizimi | ① C7 | 6,2 | 17 koşunun 8'inde ≤ 5 | ❶ |
| kadrajda yazı/logo (kart dışı) | ① C6 | 7,0 | 17'nin 5'i | ❶ |
| yüzeyde render görünümü | ① C8 | 7,3 | 17'nin 6'sı | ❶ |
| davetsiz nesne (INTRUDERS) | ⑪ hüküm | — | 10 kullanılır koşunun 7'si (FIRST GUEST · LAST LIFT dâhil) | ❹ |
| katı nesne erimesi (MELTING) | ⑫ hüküm | — | 24'ün 6'sı | ❶ |
| büyümeyi yapan görünmüyor | ⑦ C5 | 7,7 | 19'un 5'i | ❸ |
| dikiş (kesmede dünya) | ⑤ C1 | 7,6 | 19'un 3'ü | ❸ |
| en güçlü: kesme mekaniği · yön · çapa | ⑥ C1 C2 C4 C5 | ≈ 10 | — | makine + ❷ |

```
⛔ ESKİ DÖNEMİN ÜÇLÜSÜ ÇÖZÜLDÜ: ① AYRI GÖRÜNTÜ · ⑤ YENİDEN KURULMUŞ · ⑦ PARKED 16.09 öncesi
   filmlerde birlikte çıkıyordu; 19.09 sonrası neredeyse yok (zincir yöntemi).
⚠️ C2 İÇERİK BULGULARI ZAYIF KANITTIR: "işlev anı en güçlü ayırıcı", "döngü en zayıf" gibi C2
   maddeleri ④ TESLİM'den çıktı; ④'ün 36 koşusundan yalnız 9'u plan görerek koşuldu.
   Yön gösterirler, kural değildirler — ilk sınavı yeni ❺ koşularıdır.
```

## 6. Yeniden koşu — seçilenler (sahip kararı 06.10.2026: "yalnız seçilenler")

Yeni 5 mercekle koşulacak ilk set — ölçülmüş olgular bloğu `qa_paket.sh`'den basıldıktan sonra:

```
KALİBRASYON PİLOTU (QA_KALIBRASYON §1 · 3 koşu)   THE DEEP END · THE STONE TOWER · THE STONE DRAGON
DEFTER FİLMLERİ (1 koşu, öldürücüler 3)            THE LAST LIFT · THE FIRST GUEST · THE LAST HARBOR ·
                                                   THE VANISHING ROOM · THE BLUE DOOR · BACK TO PLUMB ·
                                                   THE DEEP STEP · THE STAR DOCK · THE MOUNTAIN CROWN
KAYITSIZ İYİ FİLMLER                               THE SWALLOWED BUS · THE TIDE GATE
⚠️ Liste öneridir; hangi filmlerin mp4'ü elde olduğunu sahip bilir.
```
