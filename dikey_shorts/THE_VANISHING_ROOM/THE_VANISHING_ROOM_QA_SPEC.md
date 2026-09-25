# 🔍 THE VANISHING ROOM — QA ŞARTNAMESİ

> Bu dosya **teslimden önce ölçülecek olanı** tutar. Plan `THE_VANISHING_ROOM_DIKEY_TIMELAPSE.md`,
> kapak `THE_VANISHING_ROOM_KAPAK.md`. Buraya üretim bilgisi kopyalanmaz.
> Durum: ⛔ **ÜRETİLMEDİ** — hiçbir mercek koşulmadı, hiçbir sayı ölçülmedi.

---

## 1. ⭐ İKİ FİNAL KARE KANITI — 47,5 sn VE 54,0 sn

⭐ Bu filmin **iki** final karesi vardır ve ikisi de kanıt taşır. Depodaki hiçbir filmde böyle bir çift yoktu:
birincisi bir şeyin **olmadığını**, ikincisi **olduğunu** ispatlar. Biri geçip öteki düşerse film düşer.

### ① 47,5 sn — KAYBOLMA KARESİ (G6'ya karşılık gelir) · ⭐ önce bu ölçülür

```
① TEK DÜZLEM  Çakıl yolun uzak kenarından (%18,30) bahçe duvarının tabanına (%67,84) kadar kesintisiz,
              tek bir çim düzlemi. Kadrajda ağız, çukur, tepsi, ray, kalıp, alet, araç YOKTUR.
              ⛔ Bunlardan biri kalmışsa "kayboldu" iddiası düşer: S5 yeniden.
② DİKİŞ       Kapağın çevresinde 2,4 px'lik (± 1,5 px) dikdörtgen çizgi, kilitli piksellerde:
              yakın kenar %35,40 · uzak kenar %48,62 · en 440 px (yakın) → 297 px (uzak).
              ⛔ Dikiş 6 px'ten KALINSA gizlenme başarısızdır. ⛔ Dikiş HİÇ YOKSA oda hiç olmamış gibidir
                 ve ⑤ DEVAMLILIK G5 → G6 arasındaki bağı ölçemez. İkisi de G6 yeniden.
③ BİÇİLMİŞ ŞERİTLER  Çimin biçilme şeritleri dikişin ÜSTÜNDEN kesintisiz geçer, yönü G0 ile aynıdır.
              ⛔ Şeritler dikişte kırılıyorsa ya da yön değiştiyse model çimi yeniden çizmiştir: G6 yeniden.
④ BEDEL       Solda dikilmiş toprak seti: x %14,2 – %26,6 · 88–103 px kalın · üstünde alçak çalılar.
              ⛔ Set yoksa film "toprak nereye gitti" sorusunu cevapsız bırakır ve gizlenme bir hile olur.
⑤ TEK FİGÜR   Bir kişi, sırtı kameraya, dikişin solunda. Yüz okunmaz, ikinci figür yok.
```

### ② 54,0 sn — AÇILMA KARESİ (G7 · usta kare · kapak kaynağı)

```
① YARIK       %35,40 → %45,11 · 186 px (± 10 px) · içinden SICAK ışık çıkıyor.
              ⛔ Yarık karanlıksa ödül yok: G7 yeniden.
② IŞIĞIN YÖNÜ Işık AŞAĞIDAN YUKARI çıkar ve yarığın YAKIN dudağındaki çime düşer.
              ⛔ Işık yukarıdan yarığın içine düşüyorsa (yani kadraj dışı bir kaynak varsa): G7 yeniden.
                 Filmin tek yukarı doğru hareketi budur ve tersine çevrilirse anlamı da tersine döner.
③ ODANIN İÇİ  Yarıktan ahşap zemin, halı ve merdivenin ayağı görünür (d 7,64 → 9,60 arası taban bandı).
              ⛔ Yarığın içi boş bir çukursa S3'ün bütün döşeme işi boşa gitmiştir: G7 yeniden.
④ KAPAĞIN ÇİMİ Yarığın ARKASINDA, 194 px'lik (± 10 px) çim kaplı panel — kenarında ince alüminyum çizgi.
              ⛔ Panel yoksa ya da tamamen kadraj dışındaysa "gizlenmişti" bilgisi son kareden silinir
                 ve kapak karesi çelişki kancasını kaybeder: G7 yeniden [KAPAK §1].
⑤ FİGÜR       Üç basamak inmiş, sırtı kameraya, başı ve omuzları çimin üstünde, bir eli korkulukta.
⑥ SET ve RULOLAR  Solda set G6 ile AYNI · ön solda 2 rulo çim.

⛔ SERT KAPI — İKİ KARE BİR ARADA:
   G6 ve G7 yan yana konduğunda ÇAKIL YOL (%18,30), DUVAR KRETESİ (%77,28), AĞACIN GÖVDESİ (x %87,5) ve
   ÜST KOYU BANT (%86,48) 2 px içinde AYNI olmalı; DEĞİŞEN TEK ŞEY kapaktır. Işık, gölge, çim dokusu,
   biçilmiş şerit yönü ve set birebir aynıdır (arada 8 gerçek saniye vardır). Başka bir şey değiştiyse
   model iki kareyi bağımsız üretmiştir: S6 yeniden.
```

---

## 2. KADRAJ KİLİTLERİ — sekiz karede ölçülür

| ne | beklenen | tolerans | nerede |
|---|---|:-:|---|
| ufuk | ⭐ kadrajın DIŞINDA (%105,94) | — | G0…G7 · gök görünürse BLOCK |
| çakıl yolun uzak kenarı | %18,30 | ± 2 px | G0…G7 |
| çukurun yakın dudağı | %32,81 | ± 2 px | G1…G4 |
| ağzın yakın dudağı | %35,40 | ± 2 px | G5 · G7 |
| ağzın uzak dudağı | %48,62 | ± 2 px | G5 |
| çukurun uzak dudağı | %55,84 | ± 2 px | G1…G4 |
| çukur derinliği (kadrajda) | 442 px | ± 6 px | G2 · G3 · G4 |
| çukur eni (yakın kenar) | 821 px | ± 8 px | G1…G4 |
| çukur eni (uzak kenar) | 410 px | ± 6 px | G1…G4 |
| ağız (tam açık) | 254 px yüksek | ± 8 px | G5 |
| ⭐ G7 yarığı | 186 px yüksek | ± 10 px | G7 |
| ⭐ kapağın çim paneli (G7) | 194 px | ± 10 px | G7 |
| ⭐ dikiş | 2,4 px | ± 1,5 px · üst sınır 6 px | G5 · G6 · G7 |
| bahçe duvarı tabanı | %67,84 | ± 2 px | G0…G7 |
| bahçe duvarı kretesi | %77,28 | ± 2 px | G0…G7 |
| ağacın gövdesi | x %87,5 | ± 3 px | G0…G7 |
| üst koyu ağaç bandı | %86,48 | ± 3 px | G0…G7 |
| toprak seti (x aralığı) | %14,2 – %26,6 | ± 6 px | G4…G7 |

```
⭐ ÖLÇÜM SIRASI — ÖNCE ÜÇ NİRENGİYE BAK. Bu filmde G6'da ölçülecek YAPI YOKTUR; kadrajda yalnız çim vardır.
   Nirengiler kaydıysa kalan bütün ölçümler anlamsızdır. Sıra: ① çakıl yol ② duvar kretesi ③ ağaç gövdesi
   → sonra dikiş → sonra set → sonra ağız/yarık.
⛔ UFUK KAPISI: hiçbir karede gökyüzü, bulut yüzeyi ya da ufuk çizgisi görünmez. Görünürse istasyon kaymıştır
   (tilt 40° → ufuk %105,94) ve film ZEMİN ailesinden çıkar: o kare yeniden.
```

---

## 3. ⭐ GÖRÜNÜRLÜK KAPISI — bu filmin özel merceği

Depodaki yirmi sekiz filmde ölçülen şey hep **büyüme**ydi. Burada ölçülen şey **görünürlüğün eğrisi**dir ve
tek yönlü değildir. Her karede odanın kadrajda kapladığı alan ölçülür:

```
G0   0 px²                      çim bozulmamış
G1   ~0                         yalnız çıplak toprak (oda henüz yok)
G2   ⭐ ~272 000 px²             çukur tam açık (442 × ~615 px)
G3   ~272 000 px²               dört duvar, hâlâ üstü açık
G4   ⭐ ~272 000 px²             ODA BİTTİ, hâlâ üstü açık — görünürlük ZİRVEDE
G5   ~94 000 px²                yalnız ağız (254 × ~368 px)  ⭐ %65 düşüş
G6   ⭐⭐ 0 px²                   ODA GÖRÜNMÜYOR — filmin doruğu
G7   ~72 000 px²                yarık (186 × ~385 px)

⛔ BU EĞRİ TERSİNE ÇEVRİLEMEZ: G4 > G5 > G6 ve G6 < G7 olmak ZORUNDA.
   G5'te oda ağızdan BÜYÜK görünüyorsa tavan tam oturmamıştır.
   G6'da odadan HERHANGİ bir piksel görünüyorsa gizlenme başarısızdır → S5 yeniden.
   G7'de yarık G5'in ağzından BÜYÜKSE kapak tam açılmış demektir ve kapak karesi bozulur (§1 ② ④).
⚠️ Bu kapı modelin en güçlü eğilimine terstir: model her klipte kadraja nesne EKLEMEK ister.
   S5 (40,0–48,0) sekiz saniyede sekiz şeyi ÇIKARIR. Pilot bu yüzden S5'tir.
```

---

## 4. ⭐ İKİ DEFTER KAPISI — toprak ve çim

```
DEFTER ① TOPRAK (tek yönlü · geri alınamaz)
   set uzunluğu   G0 yok · G1 2,00 m · G2 3,00 m · G3 4,20 m · G4 5,00 m · G5–G7 5,00 m
   ⛔ SET HİÇBİR KAREDE KÜÇÜLMEZ ve YER DEĞİŞTİRMEZ (Δx −3,40 · d 9,50–14,50).
      Küçüldüğü kare BLOCK'tur: bedel geri alınmıştır.
   ⭐ G6'da set DİKİLİR ama HACMİ DEĞİŞMEZ — yüzeyi değişir, sırtı aynı kalır.
   HACİM: çukur 55,1 m³ = oda 40,7 + geri dolgu 14,4 · net dışarı 36,0 = set 8,8 + damper 27,2

DEFTER ② ÇİM (kapanan defter)
   yığın   G0 4 rulo · G1 18 · G2 18 · G3 18 · G4 11 · G5 11 · G6 2 · G7 2
   ⛔ Yığın G1'den sonra BÜYÜMEZ. Büyüdüğü kare BLOCK'tur: çim dışarıdan gelmiş olur ve filmin
      "bahçeye hiçbir şey eklenmedi" iddiası çöker.
   ⭐ G4 → G5'te eksilen 7 rulo tavanın üstünde GÖRÜNÜR olmalı; G5 → G6'da eksilen 9 rulo kapağın
      üstünde ve dikişin çevresinde OLMALI. Kaybolan rulo = açıklanmamış malzeme [DERS 48].
```

---

## 5. YÜK YOLU KAPISI — ⭐ 550 kg ve vinçsiz saha

```
⛔ FİLMDE VİNÇ YOKTUR. Hiçbir karede havada asılı rijit yük bulunmaz [DERS 57 · DERS 8].
   Tavan yerinde dökülür (kalıp + iki ayarlı dikme), kapak tepsisi rayların ÜSTÜNDE kaynaklanır.
   ⛔ Herhangi bir karede vinç, bom ya da havada asılı panel görünürse: o kare yeniden.

KAPAĞIN YÜK YOLU — G5'ten G7'ye her karede aynı ve GÖRÜNÜR:
   çim + toprak → alüminyum tepsi → dört makara → iki çelik ray → tavan plağı → dört duvar → taban plağı
   ⛔ Tepsi raysız duruyorsa, makaralar görünmüyorsa ya da tepsi ağzın üstünde YÜZÜYORSA: o kare yeniden.
   ⭐ ZİNCİR ve DİŞLİ TAHRİK gömülüdür (ray döşemesinin altında) ve yalnız S6'da SESLE ve YAVAŞLIKLA
      kanıtlanır. Görünür bir motor kutusu kadraja GİRMEZ.

HAREKET KAPISI — kapak:
   ⛔ Kapak KALKMAZ, MENTEŞELENMEZ, DEVRİLMEZ, DÖNMEZ. Yalnız kendi düzleminde ve yalnız kameradan
      uzağa/kameraya doğru kayar. Tek bir karede bile kalkarsa ya da menteşelenirse S5/S6 yeniden.
   ⛔ Kapak açılırken odayı kameradan GİZLEMEZ: kameradan uzağa gider, öne doğru gelmez.
```

---

## 6. GÖLGE KAPISI [DERS 32 · 47]

```
Düz bir çim bu deponun EN İYİ gölge yüzeyidir; bu filmde gölge tek zaman taşıyıcısıdır (gök yok).
   G0 06:00  gölge yönü 263,9° · boy 11,1 katı · SOLA ve kameraya doğru
   G1 08:00  283,9° · 1,9 katı
   G2 10:00  311,9° · 0,9 katı
   G3 12:00  ⭐ 0,0° · 0,6 katı · KAMERADAN UZAĞA (en kısa)
   G4 14:00  48,1° · 0,9 katı
   G5 16:00  76,1° · 1,9 katı
   G6 18:00  96,1° · 11,1 katı · SAĞA
   G7 18:00 + 8 sn  ⭐ G6 İLE BİREBİR AYNI — rejim G'de gölge kıpırdamaz
⛔ G6 = G7 gölge kimliği bu filmin en sert kapısıdır: 8 gerçek saniyede gölge 0,03° döner, yani ölçülemez.
   Gölge kaymışsa model iki kareyi bağımsız üretmiştir.
⛔ Sağdaki ağacın gölgesi her karede kadrajda olmalı ve yönü yukarıdaki tabloyu tutmalı — bu filmin
   "zaman geçti" kanıtı özellikle S1'de (sorusuz klip) ve S5'te (boşalan klip) yalnız buna yaslanır.
```

---

## 7. SAYIM KAPISI — bir bahçe, bir çalışma, bir set, bir yığın [DERS 55]

```
Her karede sayılır:  1 çalışma dikdörtgeni · 1 toprak seti · 1 çim rulo yığını · 1 ağaç · 1 duvar · 1 çakıl yol
⛔ İkinci bir çukur, ikinci bir set, ikinci bir ağaç, bahçe mobilyası, sera, havuz ya da ikinci bir figür:
   o kare yeniden.
⚠️ RİSK — G6'nın "boş" karesi: model boşluğu doldurmak için bahçeye nesne EKLEMEYE eğilimlidir
   (masa, sandalye, saksı, ikinci ağaç). §1 ① ve bu kapı aynı arızayı iki yerden yakalar.
⚠️ RİSK — çalı sayısı: G6 ve G7'de setin üstündeki alçak çalılar AYNI SAYIDA ve AYNI YERDE olmalı.
```

---

## 8. REJİM G KAPISI — S6 (48,0 – 56,0)

```
① "moves at natural speed" + "eight seconds pass" beyanı G6 ve G7 promptlarında ✅ (kapı doğruladı)
② TEK FİGÜR · SIRTI KAMERAYA · YÜZ OKUNMAZ — sekiz saniyenin HER karesinde
   ⛔ Figür dönerse, yüzü okunursa ya da ikinci bir kişi girerse: S6 yeniden
③ İZ (streak) YOKTUR — 1×'te fiziksel olarak olamaz. İz görünürse rejim dikişi kırılmıştır
④ GÖLGE KIPIRDAMAZ (§6)
⑤ ⭐ KAPAK SABİT HIZDA GİDER: 8,0 saniyede 1,80 m (0,225 m/sn). Hızlanma/yavaşlama yalnız ilk ve son
   0,3 saniyede. ⛔ Kapak "atlarsa" (bir karede kapalı, sonrakinde açık) 550 kg iddiası çöker
⑥ IŞIK KAPAĞIN AÇILMASIYLA ORANTILI GENİŞLER — önce kıl payı çizgi (1,0–2,0), sonra bant (2,0–4,0)
⛔ REJİM DİKİŞİ 48,0'de BEYANLIDIR [P5-c]: 1200× → 1×. Çim dokusu ve gölge iki yakada aynı kalır;
   değişen tek şey hareketin hızıdır.
```

---

## 9. MÜZİKSİZ SES KAPISI

```
⛔ 0,0–56,0 boyunca MÜZİK YOK — melodi, nabız, akor yastığı, yükselen ped: hiçbiri.
⭐ SESSİZLİK KAPISI (bu filme özel): 46,0–48,4 arası (2,4 sn) yalnız akşam kuşu ve cırcır böceği duyulur.
   ⛔ Bu aralığa ses KONULMAZ. Konursa fikrin "kapak kapanınca kısa bir sakinlik" maddesi düşer ve
      S6'nın şalter sesi vurgusunu kaybeder.
⚠️ BLUE DOOR SIZINTISI: son 5 saniyeye hiçbir "kapanış akoru" konmaz. Film dişli sesi SÜRERKEN kesilir.
SENKRON  48,4 şalter "tık" · 48,8 dişli notası · 49,6 makara tıkırtısı · 54,2 ilk basamak (ahşap üstünde tok)
⭐ KANIT: 42,0–43,0'te (rejim B, 1200×) kapağın kapanma sesi SIKIŞTIRILMAZ — ses 1× kalır ve görüntüyle
   senkron değildir. Bu beyanlı bir dikiştir, hata değil: ses yatağı hiçbir sahnede hızlandırılmaz.
```

---

## 10. ZAMAN VE IŞIK

```
IŞIK GÜNÜ  06:00 → 18:00 + 8 sn = 12 sa 0 dk 8 sn ≤ 14 sa ✅
           40°K · δ +8° · doğuş 05:33 · batış 18:27 → pencere iki ucunda 27'şer dakika payla gündüzün içinde
⛔ IŞIK KESMEDE ATLAMAZ: G(n) hem S(n−1)'in son karesi hem S(n)'in ilk karesidir. Kesmelerde renk
   sıcaklığı, gölge yönü ve gölge boyu birebir aynıdır.
⭐ TAKVİM (~5 hafta) SAHADAN okunur, ışıktan değil: set büyür · çim yığını erir · yeni çim derzleri kapanır ·
   çalılar dikilir. Işıkta mevsim değişmez.
⛔ GÖK KAPISI: kadrajda gök yok. Yedi I2V'nin gök borcu BULUT GÖLGESİYLE ödenir; G6→G7'de komşu çayırın
   üstündeki pus "holds still". Gökyüzü kadraja girerse §2'nin ufuk kapısı zaten düşer.
```

---

## 11. BİLİNEN VE BEKLENEN RİSKLER

```
⚠️ 1. G6'DA ÖLÇÜLECEK YAPI YOK. Depodaki en zor süreklilik karesi: kadrajda yalnız çim var ve 2 px eşiği
      tamamen üç nirengiye yaslanıyor. Bu, filmin kabul edilmiş ana riskidir. Pilot sırası bu yüzden
      G6 → G7 → S5'tir (plan §PİLOT ÜÇLÜ).
⚠️ 2. MODEL EKLEME EĞİLİMLİ. S5 sekiz saniyede sekiz şeyi çıkarır; model bunun tersini yapmaya eğilimlidir.
      §3 ve §7 aynı arızayı iki yerden yakalar.
⚠️ 3. DİKİŞ DENGESİ. 2,4 px hedeftir ve okunurluk eşiğinin ALTINDADIR (bilerek). Model dikişi ya hiç
      çizmeyecek ya da bir beton derzi kalınlığında çizecektir. Üst sınır 6 px, alt sınır "var olmalı".
⚠️ 4. KAPAK MENTEŞELENEBİLİR. "Hatch" kelimesinin korpusunda menteşeli kapaklar baskındır; beş maddelik
      kapak kilidi (plan §KAPAK KİLİDİ) G5→G7'de birebir tekrarlanıyor ama ölçülmedi.
⚠️ 5. IŞIK TERSİNE DÖNEBİLİR. G7'de ışığın YUKARI çıkması gerekiyor; model çukura yukarıdan ışık düşürmeye
      eğilimlidir. §1 ② bunun kapısıdır ve filmin anlamı buna bağlıdır.
⚠️ 6. ÇİM DOKUSU DEĞİŞEBİLİR. Sekiz bağımsız karede aynı çim: biçilme şeritlerinin yönü ve genişliği
      G0 ile G7 arasında aynı kalmalı (plan §KARE TABLOSU · DÖRT KARE TESTİ).
⚠️ 7. P13-h DEVAM EDİYOR: kapının §9 metin yasağı kapsam kontrolü ("…annotated by anyone" aralığı) bu
      depodaki hiçbir filmde koşmuyor; bu film de ev standardı sözcüklerle yazıldı. Sahip kararı bekliyor
      [kilavuzlar/DERSLER.md P13-h · QA/00_INDEX].
⚠️ 8. ARAÇ KUTU SETİ ÖLÇÜLMEDİ — üretim açılamaz [ARAC_KARTLARI §4].
```
