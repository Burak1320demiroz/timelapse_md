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

---

# 6. MEVSİMİ NEREDE OKUTURSUN — saha başına

| Saha | Mevsim taşıyıcısı |
|---|---|
| Şehir içi | ağaç yaprağı · komşu balkonlarda tente · kar · gölge boyu |
| Kırsal | ekin ve ot rengi ⭐ en güçlü · kar |
| Kıyı | deniz rengi · gökyüzü · kıyı bitkisi |
| Dağ | ⭐ kar çizgisinin yamaçta inip çıkması |
| Çöl | ⛔ mevsim görünmez — yalnız güneş yüksekliği ve yapı |

⛔ **Mevsim taşıyıcısı olmayan sahada** (çöl) zaman yükünün tamamı güneş
yüksekliğine ve yapının kendisine biner; güneş satırı orada daha da kritiktir.

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
