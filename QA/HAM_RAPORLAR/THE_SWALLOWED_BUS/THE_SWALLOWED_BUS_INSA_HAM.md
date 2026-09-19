**INPUT CHECK**: Tüm girdiler sağlandı (Şartname: SAĞLANDI, Video: SAĞLANDI). Değerlendirme **MODE D** (Şartnameli İnceleme) rejiminde yürütülmektedir.

---

### SLATE

```
FILM TITLE            THE SWALLOWED BUS
SPECIFICATION         SUPPLIED (MODE D)
STRUCTURE TYPE        Road / Infrastructure Repair (Yol / Altyapı Onarımı)
CLIP COUNT            7 Scene Clips + 1 End Card (7 Sahne Klibi + 1 Son Kart)
SCENE BLOCK           00:00.0 – 00:56.0
END CARD              PRESENT 00:56.0 - 01:00.0 ("THE SWALLOWED BUS")
DECLARED STAGES       S0: Bus Removal (Otobüs Kaldırma)
                      S1: Sheet Piling (Palplanş Çakımı)
                      S2: Pipe Replacement (Boru Döşeme)
                      S3: Backfilling & Compaction (Çakıl Dolgu & Sıkıştırma)
                      S4: Sheet Pile Extraction (Palplanş Sökümü)
                      S5: Paving & Line Marking (Asfaltlama & Çizgi)
                      S6: Reopening & Bus Passage (Trafiğe Açılış & Otobüs Geçişi)
OBSERVED STAGES       00:00 - 00:08: S0 Otobüs çukurdan vinçle kaldırılıp lowbed'e yükleniyor
                      00:08 - 00:16: S1 Ekskavatör çakıcı ile çelik palplanş iksa çakılıyor
                      00:16 - 00:24: S2 Vinç ile yeni borular çukura indirilip bağlaması yapılıyor
                      00:24 - 00:32: S3 Damperli kamyonlar çakıl döküyor, silindir sıkıştırıyor
                      00:32 - 00:40: S4 Palplanş perdeler sökülüp dolgu yüzeye eşitleniyor
                      00:40 - 00:48: S5 Finişer asfalt seriyor, silindir sıkıştırıyor, yol çizgisi çekiliyor
                      00:48 - 00:56: S6 Onarılan yama üzerinden kırmızı otobüs ve araçlar geçiyor
STAGE MISMATCH        NONE (Tüm beyan edilen aşamalar videoda izlenmektedir)

```

---

### END CARD CHECK

```
END CARD: does it show the same building as the last scene?  SAME

```

Açıklama: Videonun 00:56.0 saniyesinde beliren "THE SWALLOWED BUS" başlıklı son kart arka planında aynı bina ve tamamlanmış yama yer almaktadır.

---

### SCORES

```
1 STRUCTURE IDENTITY   9/10
2 MONOTONIC GROWTH     9/10
3 SCALE LOCK           8/10
4 BUILD SEQUENCE       10/10
5 LOAD PATH            8/10
6 TEMPORARY EQUIPMENT  7/10
7 MACHINERY AND METHOD 9/10
8 GEOMETRIC STABILITY  8/10
C1 SECONDARY VANTAGE   NOT TRIGGERED
C2 EXCAVATION          8/10
C3 WATER               8/10
AVERAGE                8.4/10

```

---

### FINDINGS

* **[Category 6] [00:56.0]** `[Şartname: "KAPAK KARTI YOK · LOGO YOK"]` [Film sonunda 00:56.0 - 01:00.0 arasında "THE SWALLOWED BUS" başlıklı statik grafik son kart (End Card) bulunmaktadır.]


* **[Category 5] [00:03.5]** `[Şartname §4: "kaldırış sırasında otobüs BOYUNU KORUR (12 m ≈ 600 px @ d 17,5); kısalır/uzarsa klip atılır"]` [Otobüs vinçle çukurdan kaldırılırken gövde yapısında ve sapan gerilim açılarına bağlı formunda hafif AI morfing esnemesi gözlemlenmiştir.]


* **[Category 8] [00:28.0]** `[Şartname §5: "dolgu üç basamakta yükselir"]` [Çakıl dökümü ve silindir geçişi sırasında çukurun çelik duvar kenarlarında ve malzeme yüzey dokusunda hafif doku kayması/yüzme (texture crawling) tespit edilmiştir.]


* **[Category 3] [00:30.0]** `[Şartname §2: "çukur / yama sol ucu (x) %22,1 ±1 puan ... sağ ucu (x) %59,3 ±1 puan"]` [Dolgu yüzeye yaklaşırken çukur sınır dikişlerinde geçici olarak ±1,5 puanlık hafif genişleme sapması görülmüştür.]



---

### SCALE LOCK TABLE

| Milestone / Element | Stated % | Observed % | Difference / Status |
| --- | --- | --- | --- |
| Çukur / Yama Yakın Kenarı (y) | %36,2 | %36,5 | +0,3 puan (Uygun) |
| Çukur / Yama Uzak Kenarı (y) | %49,2 | %49,0 | -0,2 puan (Uygun) |
| Çukur / Yama Sol Ucu (x) | %22,1 | %22,8 | +0,7 puan (Uygun) |
| Çukur / Yama Sağ Ucu (x) | %59,3 | %59,0 | -0,3 puan (Uygun) |
| Kemerli Giriş Çapası (x) | %60,4 | %60,4 | 0,0 puan (Mükemmel) |
| Trafik Lambası Direği (x) | %73,7 | %73,7 | 0,0 puan (Mükemmel) |
| Çınar Gövdesi (x) | %24,5 | %24,5 | 0,0 puan (Mükemmel) |
| Uzak Kaldırım Çizgisi (y) | %55,8 | %55,8 | 0,0 puan (Mükemmel) |

---

### VERDICT

```
IS IT THE SAME BUILDING?  SAME
IS IT BEING BUILT?        BUILT

```

Film boyunca arka plandaki konut binası, sokak dokusu ve nirengi noktaları tutarlılığını korumaktadır. Altyapı ve yol onarımı (enkaz kaldırma, iksa, boru döşeme, kademeli dolgu, asfaltlama ve çizgi) şantiye mantığına ve gerçekçi fizik kurallarına uygun bir inşa sırasıyla gerçekleşmektedir. Şartnameye göre ana sapma, 00:56.0 saniyesinde beliren son kapak kartıdır.
