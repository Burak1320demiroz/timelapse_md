# ☀️ ZAMAN VE IŞIK KILAVUZU

> Timelapse'te ışık dekor değil, **saattir.** Bir izleyici gölgenin yanlış
> yönde gittiğini adlandıramaz ama görür ve videonun sahte olduğuna karar verir.
> Bu kılavuz iki saati ayırır ve ikisini de sayıya bağlar.

---

# 1. İKİ SAAT — karıştırma

```
SAHNE İÇİ SAAT      10 saniyenin İÇİNDE geçen zaman
                    varsayılan: 1 gün (şafak → alacakaranlık)
                    taşıyıcı: gölgenin kadrajı süpürmesi + bulut çizgileri

SAHNELER ARASI SAAT sahneler ARASINDA geçen zaman
                    varsayılan: haftalar–aylar (aşama merdiveninden gelir)
                    taşıyıcı: mevsim + güneşin yıl içindeki yüksekliği + yapı
```

⛔ **Bir sahnede iki saat birden çalıştırma.** Aynı klipte hem bir gün geçip
hem mevsim değişirse model geometriyi ve ışığı birlikte eritir. Bir klip =
bir gün + bir görünür iş adımı.

---

# 2. GÜNEŞ SATIRI — her promptta zorunlu

```
"sun azimuth 118°, elevation 34°, shadows falling to the west-north-west"
```

| Mevsim | Öğle yüksekliği | Gölge | Renk sıcaklığı | Gökyüzü |
|---|---|---|---|---|
| Yaz | 60-72° | kısa, sert, siyah | 5600 K nötr | derin mavi, yüksek bulut |
| Sonbahar | 35-48° | orta, uzayan | 5000 K sıcak | dağınık, alçak bulut |
| Kış | 14-22° | ⭐ çok uzun, mavi | 6500 K soğuk | düz beyaz-gri |
| İlkbahar | 40-55° | orta | 5400 K | değişken, hızlı bulut |

```
İKİ YÖN KURALI
  · Sahne İÇİNDE güneş TEK YÖNDE ilerler — geri dönmez, atlamaz, durmaz.
  · Sahneler ARASI mevsim TEK YÖNDE ilerler: yaz → sonbahar → kış → ilkbahar → yaz.
    Geri giden bir mevsim, izleyicinin sebebini bilmeden güvenini kaybettiği şeydir.
```

### ⚠️ GÖLGE DÖNGÜSÜNÜN PİK SAYISI = YIL SAYISI [A4-b]

```
Gölge boyu  L = h / tan(α)   → yaz gündönümünde en KISA, kış gündönümünde
                               en UZUN. Bir yıl = bir uzama-kısalma döngüsü.

⭐ 34 aylık bir film, gölge boyunun ÜÇ maksimum ve ÜÇ minimum pikine ulaşmak
   zorundadır. Bu, ③ merceğinin "34 ay yerine yaklaşık bir yıl" okumasının
   [DERS 14] mekanizmasıdır: izleyici bir tam güneş döngüsü görür ve bir yıl
   sayar. Zaman yayı kaç yılsa, gölge o kadar kez uzayıp kısalır.

⚠️ VARSAYIM — koşulmadı: güneş satırı bugün yalnız azimut ve yükseklik
   yazıyor. Zaman yayı ≥2 YIL olan filmlerde gölge BOYUNUN da sahne sahne
   yazılması gerekebilir ("the shadow of the brick block reaches [n] metres
   across the slab"). Yükseklik derecesi bunu ima eder, söylemez.
```

---

# 3. 6 SANİYEDE NE DEĞİŞİR — bütçe

Bir klipte aynı anda çalışabilecek zaman olayları. **En fazla İKİSİ seçilir**
(⭐ 10 sn ızgarasında üçtü — klip kısaldı, bütçe de kısaldı); üçüncüsü
kalabalıktır ve model geometriyi eritir.

```
⛔ v1 KANITI: tek klipte 13 kat çıkarıldı ve ② GEOMETRIC STABILITY 0/10 geldi
   ("slabs and columns visibly warp, ripple and breathe"). 10 aşamaya bölünmüş
   bir ızgarada her klip TEK ve KÜÇÜK bir iş adımı taşır; daha hızlı film,
   aynı zamanda daha az riskli filmdir.
```

```
① GÖLGE SÜPÜRMESİ   ⭐ her sahnede bulunur — saatin ana taşıyıcısı
                    "the shadow of the brick block sweeps across the slab
                     from left to right"
② BULUT ÇİZGİLERİ   yön SABİT, hız yüksek
                    "clouds streak across the sky in long smooth trails,
                     always from the north-west"
③ MAKİNE DÖNGÜSÜ    vinç yavaş döner, kanca iner-çıkar, ekskavatör kova döngüsü
④ ARAÇ İZLERİ       kamyonlar gelip gider — net araç değil, LEKE
⑤ İŞ ADIMI          bir kat belirir, bir panel dizisi takılır, bir döküm olur
                    ⚠️ bir klipte YALNIZ BİR iş adımı — ve 6 saniyede o adım
                       KÜÇÜKTÜR: 1-3 kat, bir cephe bandı, bir döküm
⑥ IŞIKLARIN YANMASI yalnız S5 · kat kat, aşağıdan yukarı
⑦ HAVA DÖNÜŞÜ       yağmur ıslatır, sonra kurur — direnci gösteren tek olay
```

### ⛔ MEVSİM ARA DURUMU BİR CÜMLE DEĞİL, BİR KAREDİR [DERS 26]

```
Ölçüldü (THE MOUNTAIN DOOR):
  PLAN   yaz → sonbahar → kış① → kış②(erime) → yaz     = 12 ay
  EKRAN  yaz → yaz      → kış  → yaz          → yaz
  ③ SEASON ORDER 0/10 · ⑥ C2 SEASON CHANGE 0/10

⛔ DERS 7 (kış İKİ sahne) uygulanmıştı — yetmedi.
⛔ DERS 21 (hazırlık giden klibin içinde) uygulanmıştı — cümleler beş I2V'de
   yazılıydı ve HİÇBİRİ üretilmedi.

⭐ SEBEP: "erime" bir ARA DURUMDUR ve tek bir kareden türetilemez. Kareler
   bağımsız üretilirse erime diye bir şey yoktur — ya kar vardır ya yoktur.
   Bina BİRİKİR, kar BİRİKMEZ: mevsim yapıdan daha kırılgandır.

KİLİT  Erime isteniyorsa erimenin KENDİ GÖRSELİ üretilir ve zincire girer.
       ⛔ Ve zincir (ters inşa) koşulmadan mevsim yayı hiç denenmez.
⚠️ BEDELİ: 5 sahnelik ızgarada kış birikme + erime + ara durum = üç sahne
   eder ve yer yoktur. Yani 5 sahnede mevsim yayı ya İKİ mevsimle
   sınırlanır, ya kırılır. Üçüncü seçenek ölçülmedi.
```

---

# 4. SAHNE İÇİ IŞIK YAYI — üç şablon

```
A) TAM GÜN        şafak → öğle → alacakaranlık. En güçlü zaman hissi.
                  gölge kadrajı baştan sona süpürür. Varsayılan.
B) YARIM GÜN      öğle → gün batımı. Gölge uzar ve renk ısınır. Kanca ve
                  final sahneleri için (S0, S5).
C) SABİT SAAT     gölge çok az hareket eder. Yalnız İŞ ADIMI'nın öne çıkması
                  gereken sahnede (S4 cephe gibi) kullanılır — bir filmde
                  en fazla bir kez.
```

---

# 5. GECE — bir kez, S5'te

```
Gece sahnesi filmin tek duygusal anıdır ve bir kez kullanılır.
  · ışıklar KAT KAT yanar, aşağıdan yukarı — hepsi birden değil
  · şantiye aydınlatması söner, bina aydınlatması yanar (devir teslim)
  · gökyüzü tam siyah değil, alacakaranlık mavisi (yapı silueti okunsun)
  · yıldız izi YAZILMAZ — şehirde yıldız görünmez ve model onu abartır
NEGATİF EK: "no light streaks in the sky, no star trails, no neon, no
             illuminated signage, no readable window content"
```

### ⭐ GECE FİZİĞİ SAYIYLA — şehir dışı sahalar için [A4-c · A4-d · A4-e]

⛔ Bu blok yalnız **negatif çekirdeğin `no star trails` maddesi saha kartıyla
çeliştiğinde** (dağ · çöl · kaya vadisi) kullanılır [DERS 16]. Şehir gecesinde
yukarıdaki negatif ek geçerlidir.

```
① YILDIZ İZİ — "short" bir sayı değildir
   Dünya saatte 15° döner. Pozlama süresi izin derecesini belirler:
      21 sn (24 mm tam kare · 500 kuralı)  → NOKTA · iz yok
      1 saat   → 15°        2 saat  → 30°
      3,5 saat → 52,5°      6 saat  → 90° (çeyrek daire)
   Kutba yakın izler iç içe daire, göksel ekvatorda düz çizgi.
   ⛔ Yay derecesi ile pozlama saati BİRLİKTE yazılır; biri diğerini ima
      eder ama söylemez [DERS 19'un gökyüzü hâli].
   KİLİT  "The stars render as concentric arcs about thirty degrees long,
           centred on the pole star, consistent with a two-hour exposure."

② VİNÇ TEPE LAMBASI DÜZENSİZ ÇAKAR
   ICAO/FAA gereği lamba dakikada 20-40 kez çakan bir flaşördür ve uzun
   dönem timelapse aralığı 10-15 dakikada bir karedir. Deklanşörün açık
   olduğu milisaniyede lambanın yanık olması RASTLANTISALDIR.
   ⛔ Sürekli yanan bir kırmızı tepe ışığı timelapse'i yalanlar.
   KİLİT  "The obstruction light at the crane mast head reads as a single
           bright red pixel in some frames and is completely dark in
           others, never a continuous glow."
   KALDIRDIĞI  Gece kadrajının kolay atmosfer kazancı olan sürekli kırmızı
               tepe ışığı. Karşılığı: gecenin fiziği doğru okunuyor.

③ ARAÇ FARI SÜREKLİ ŞERİT BIRAKIR
   10-20 sn pozlamada hareket eden araç farları kesintisiz beyaz (ön) ve
   kırmızı (arka) hatlar çizer. AI üretiminde bunlar donmuş kısa fırça
   darbelerine ya da iz bırakmayan parlak noktalara dönüşür.
   KİLİT  "Vehicles on the site road leave unbroken white and red light
           trails that run the full length of their path across the frame."
   ⭐ §9.4'ün "smeared light and colour trails" cümlesinin gece hâli ve
      renkli tarifi. Aynı kural, sayılı yüzey.
```

---

# 6. MEVSİMİ NEREDE OKUTURSUN — saha başına

| Saha | Mevsim taşıyıcısı |
|---|---|
| Şehir içi | ağaç yaprağı · komşu balkonlarda tente · kar · gölge boyu |
| Kırsal | ekin ve ot rengi ⭐ en güçlü · kar |
| Kıyı | deniz rengi · gökyüzü · kıyı bitkisi |
| Dağ | ⭐ kar çizgisinin yamaçta inip çıkması |
| Çöl | ⛔ mevsim görünmez — yalnız güneş yüksekliği ve yapı |
| **HEPSİ** | ⭐ **beton kürlenmesi** — mevsimden bağımsız, her sahada [A4-a] |

⛔ **Mevsim taşıyıcısı olmayan sahada** (çöl) zaman yükünün tamamı güneş
yüksekliğine ve yapının kendisine biner; güneş satırı orada daha da kritiktir.

### ⭐⭐ BETON KÜRLENMESİ — deponun hiç kullanmadığı taşıyıcı [A4-a]

```
FİZİK    Taze dökülen beton, hidrasyon ve nem kaybıyla GÜNLER boyunca koyu
         ıslak griden mat açık kemik rengine açılır (hiperspektral ölçüm:
         600-750 nm görünür bandında yansıma artışı · 1., 7. ve 28. gün).

⭐ NEDEN BU KADAR DEĞERLİ — iki şeyi birden çözer:

  ① ARDIŞIK DÖKÜMLER ARASINDAKİ KONTRAST BİR SAATTİR.
     Alt katlar açık ve kürlenmiş, en son dökülen döşeme taze ve koyu.
     Aradaki RENK SINIRI, o iki dökümün arasından kaç ay geçtiğini
     ekranda gösterir. Mevsim yayına hiç dokunmadan zaman okutur.

  ② MEVSİMİN GÖRÜNMEDİĞİ SAHADA ÇALIŞIR.
     Yukarıdaki tablo çölde "zaman yalnız gölge ve yapı ile anlatılır"
     diyor — beton kürlenmesi tam olarak "YAPI İLE ANLATMANIN" nesne
     düzeyindeki hâlidir. Çöl ve kaya vadisi artık taşıyıcısız değil.

⛔ VE DERS 14'ÜN ÖLÇÜLMÜŞ ARIZASINA DOĞRUDAN CEVAP:
   iki sahnede mevsim "Indeterminate — bare rock and concrete with no
   foliage, weather, or sun-height carriers" okundu. O karelerde BETON
   VARDI ve taşıyıcı sayılmıyordu. Sayılmıyordu çünkü hiçbir kılavuz onu
   taşıyıcı olarak yazmamıştı.

KİLİT (İngilizce · pozitif · ölçülebilir · aşama merdiveninin
       MEVSİM TAŞIYICISI sütununa da yazılır):
  "The lower floors are pale bone-grey fully cured concrete, while the slab
   poured most recently is still dark, wet and blotchy — the colour boundary
   between them sits exactly at the seventh floor slab edge."

KALDIRDIĞI  Hiçbir şey. Beton zaten kadrajdaydı; artık bir saat taşıyor. [D-f]
⚠️ KOŞULMADI: bu bir varsayımdır ve modelin renk sınırını tutup tutmadığı
   ölçülmedi. İlk üretimde ③ SEASON CARRIER satırından okunacak.
```

---

# 7. ZAMAN YAYININ HESABI

```
Toplam inşa süresi          → 60 saniyeye sığar
Sahne başına temsil süresi  → aşama merdiveninin TEMSİL SÜRE sütunu

⚠️ TEMSİL SÜRELERİ EŞİT OLMAK ZORUNDA DEĞİLDİR — ve olmamalıdır.
10 sahnelik ızgarada referans yay:

   S0  1 gün      (kanca · zamanı yavaşlatır, izleyici yerleşir)
   S1  3 hafta
   S2  5 hafta
   S3  2 ay
   S4  2 ay
   S5  6 hafta
   S6  2 ay       ⭐ kış ① · direnç · döngü yavaşlar
   S7  2 ay       ⭐ kış ② · erime · döngü hızlanır
   S8  3 ay
   S9  1 gün      (final · zamanı yeniden yavaşlatır, ödeme burada okunur)
   ────────────── toplam ≈ 15 ay

Bu yay — yavaş / hızlan / en yoğun / yavaşla — filmin nefesidir. On sahneyi
eşit bölmek videoyu bir tabloya çevirir.

⛔ İzleyicinin okuduğu süre, yazdığın süre değildir. v1'de plan 14 ay
   diyordu ve ③ merceği filmi "1,5-2 yıl" okudu — çünkü bir kış görüp
   sonra yaza dönmek "en az iki kış" demektir [DERS 7].
```
