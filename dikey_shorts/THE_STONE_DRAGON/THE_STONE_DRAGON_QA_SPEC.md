# 🔍 THE STONE DRAGON — QA ŞARTNAMESİ

> Bu dosya **teslimden önce ölçülecek olanı** tutar. Plan `THE_STONE_DRAGON_DIKEY_TIMELAPSE.md`,
> kapak `THE_STONE_DRAGON_KAPAK.md`. Buraya üretim bilgisi kopyalanmaz.
> Durum: ⛔ **ÜRETİLMEDİ** — hiçbir mercek koşulmadı, hiçbir sayı ölçülmedi.

---

## 1. ⭐ FİNAL KARE KANITI — 54,0 sn

Teslim videosundan 54,0 sn'deki kare alınır ve **dört şey sırayla** aranır:

```
① SU        ağızdan (%53,97) hazneye (%38,57) inen KESİNTİSİZ berrak su ipi — 296 px
            ⛔ Damlıyorsa, kopuk kopuksa ya da ağzın dışından/yanından sızıyorsa: G7 yeniden.
② İKİ RENKLİ TAŞ
            ağzın ÜSTÜ (baş · iki boynuz · kanat) KURU ve SOLUK
            ağzın ALTI (göğüs · hazne) ISLAK ve İKİ TON KOYU
            ⛔ Taşın tamamı ıslaksa su "yağmur" okunur, "çeşme" okunmaz: G7 yeniden.
③ HAM KESİM BANDI — TANIK ①
            %30,16 – %34,13 · 76 px · tam blok eni · KURU ve SOLUK · üstünde ocak testeresi yayları
            ⛔ Bant ıslaksa, oyulmuşsa, kapanmışsa ya da G0'dakinden farklı piksellerdeyse:
               filmin "bu aynı bloktu" ispatı yok demektir. G7 yeniden.
④ BEDEL ve TANIK ②
            solda MOLOZ YIĞINI (1,70 × 0,68 m · 367 × 174 px) · sağda KAROT (22 × 407 px · x %73,86)
            ⛔ Yığın yoksa film "taş nereye gitti" sorusunu cevapsız bırakır.

⛔ SERT KAPI — HEYKEL TAŞ KALDI MI:
   G7'de ve S6'nın sekiz saniyesinin hiçbir karesinde heykel göz kırpmaz, başını çevirmez, kıpırdamaz.
   Tek bir kare bile canlandıysa fiziksel yapım hikâyesi çöker [fikrin kendi maddesi]. S6 yeniden.
```

---

## 2. KADRAJ KİLİTLERİ — sekiz karede ölçülür

| ne | beklenen | tolerans | nerede |
|---|---|:-:|---|
| ufuk | %50,00 | ± 1 px | G0…G7 |
| blok tepesi | %67,46 | ± 2 px | G0…G7 |
| blok eni | 394 px | ± 2 px | G0…G7 |
| blok yüksekliği | 716 px | ± 2 px | G0…G7 |
| ⭐ ham kesim bandı | %30,16–34,13 · 76 px | ± 2 px | G0…G7 |
| banker eni | 489 px (%27,38–72,62) | ± 2 px | G0…G7 |
| moloz duvar üst hattı | %56,67 | ± 2 px | G0…G7 |
| servi tepeleri | %84,76 | ± 3 px | G0…G7 |
| ağız (su çıkışı) | %53,97 | ± 2 px | G4…G7 |
| hazne ön dudağı | %38,57 | ± 2 px | G4…G7 |
| karot | x %73,86 · 22 × 407 px | ± 3 px | G3…G7 |
| su düşüşü | 296 px | ± 4 px | G7 |

```
⛔ Kayma eşiği 2 px · MOTION FOCUS FIX — sahip kararı 19.09.2026, pilot ölçümüne kadar açılmaz.
⭐ ÖLÇÜM SIRASI: önce BANDA bak. Ham kesim bandı 2 px'den fazla kaydıysa diğer ölçümlere GEREK YOK —
   model bloğu yeniden çizmiş demektir, halka baştan üretilir.
```

---

## 3. ⭐ KİMLİK KAPISI — bu filmin özel merceği

Serbest biçimli geometri deponun ilk kez karşılaştığı sorundur. Sekiz kare yan yana konur ve **beş madde**
her karede ayrı ayrı doğrulanır (G2'den itibaren):

```
① baş AŞAĞI eğik ve biraz SOLA dönük            → G2 G3 G4 G5 G6 G7
② iki KISA GERİYE YATIK boynuz                   → G2 G3 G4 G5 G6 G7
③ boyun AŞAĞI ve SAĞA kıvrılıyor                 → G2 G3 G4 G5 G6 G7
④ BİR kanat, gövdeye yatık tek düz düzlem        → G4 G5 G6 G7
⑤ kuyruk haznenin kenarını sarıyor               → G4 G5 G6 G7

⛔ BLOCK sayılan sapmalar:
   · boynuz uzadı, çatallandı ya da öne döndü
   · ikinci kanat çıktı, kanat gövdeden AÇILDI
   · baş sağa döndü ya da yukarı kalktı
   · ⭐ herhangi bir parça BLOĞUN ORİJİNAL KONTURUNUN DIŞINA taştı (hacim kuralı)
   · ⭐ G3'te baş G2'den FARKLI (S2'de oyma yok, yalnız delik açılıyor)
⚠️ Kimlik kayması bu filmde ①ⓘKADRAJ hatasından daha tehlikelidir: kadraj kayması ölçülür, kimlik kayması
   yalnız göz ile yakalanır. Bu yüzden pilot S1'dir (plan §PİLOT ÜÇLÜ (b)).
```

---

## 4. ⭐ EKSİLTME KAPISI — malzeme defteri

```
Sekiz kare sırayla ve yalnız BİR YÖNE bakılarak okunur:

BLOK       her karede bir öncekinden EKSİK ya da AYNI olmalı. Hiçbir yerinde taş EKLENMEMELİ.
           ⛔ BLOCK: bir kare önce oyulmuş bir yer sonraki karede dolu görünüyorsa.
YIĞIN      G0 (yok) < G1 (194 px) < G2 (259) < G3 (292) < G4 (335) < G5 (367) = G6 = G7
           ⛔ BLOCK: yığın herhangi bir karede KÜÇÜLDÜYSE ya da YER DEĞİŞTİRDİYSE — bedel geri alınmış olur.
           ⛔ BLOCK: G5 → G6 → G7 arasında yığın değiştiyse — o iki sahnede hiç taş kesilmiyor.
KAROT      G0 G1 G2'de YOK · G3'te belirir · G3 G4 G5 G6 G7'de aynı yerde, aynı boyda.
           ⛔ BLOCK: karot G3'ten önce görünüyorsa (deliğin sebebi olmadan sonucu) ya da sonradan kayboluyorsa.
DELİK      G0 G1 G2'de YOK · G3'te bloğun TEPESİNDE · G4'ten itibaren AYRICA ağzın TABANINDA.
           ⛔ BLOCK: ağzın tabanındaki delik G4'ten önce varsa.
```

---

## 5. YÜK YOLU VE VİNÇ KAPISI

```
⛔ "crane" kelimesi hiçbir promptta YOK ve kadrajda hiçbir vinç YOK.
   Tek kaldırma aracı portal gantry'nin zincir palangasıdır ve yalnız G0'da yüklüdür (sapan başın üstünde).
   G1…G5'te palanga BOŞ ve sapanı kendi kirişine asılıdır. G6 ve G7'de gantry'nin kendisi YOK.
⛔ Havada asılı uzun rijit yük hiçbir karede YOK [DERS 57].
⭐ SU YOLU KAPALI DEVREDİR ve tamamı izleyiciye gösterilmiştir:
   çukur → pompa → boru (banker dibinde kelepçeli) → karot deliği → ağızdaki bronz boru → hazne →
   ön dudak → döşemedeki kanal → çukur.
   ⛔ Kadrajda kaynağı görünmeyen su YOK; hortum G5'ten sonra sahada değildir.
```

---

## 6. GÖLGE KAPISI [DERS 32 · 47]

```
Bloğun gölgesi filmin omurgasıdır ve YÖNÜ her karede ölçülür:
   G0 07:00  5,1 m SOLA ve kameraya doğru      G4 15:00  2,2 m SAĞA
   G1 09:00  2,2 m sola-arkaya                  G5 17:00  5,1 m SAĞA
   G2 11:00  1,0 m ARKADA (gizli)               G6 19:00  >50 m sağa, döşemeyi boydan boya geçer
   G3 13:00  1,0 m arkadan sağa                 G7 19:00+8sn  ⭐ G6 İLE BİREBİR AYNI (rejim G: gölge kıpırdamaz)
⛔ BLOCK: G6 ile G7 arasında gölge kıpırdadıysa rejim G ihlal edilmiştir.
⛔ BLOCK: gölge yönü sırayı bozduysa (örn. G4'te sola) ışık günü kırılmıştır.
⚠️ Klip İÇİ süpürme rejim B'nin kanıtıdır: 07→09 20,3° · 09→11 38,8° · 11→13 76,8° · 13→15 38,8° ·
   15→17 20,3° · 17→19 18,0°. Süpürme görünmeyen klip ⑦ merceğinde PARKED okunur.
```

---

## 7. SAYIM KAPISI — bir blok, bir banker, bir yığın [DERS 55]

```
Sekiz karenin her birinde sayılır:  blok 1 · banker 1 · yığın 1 · karot (G3'ten sonra) 1 · hazne 1 · pompa (G6'dan) 1
⛔ BLOCK: ikinci bir blok, ikinci bir yığın, ikinci bir heykel ya da avluda çalışılan başka bir taş.
⛔ BLOCK: kadrajda okunabilir metin, harf, rakam ya da sembol — taşta, banker'da, brandada, makinede.
   ⚠️ Bu filmde özel risk: ustaların gerçekte blok üstüne tebeşirle ölçü YAZAR. Tebeşir yalnız ÇİZGİ olabilir;
      rakam ya da harf içeren tek kare BLOCK'tur.
```

---

## 8. REJİM G KAPISI — S6

```
① S6'nın sekiz saniyesi boyunca gölge KIPIRDAMAZ
② tek figür, SIRTI KAMERAYA, yüz hiçbir karede okunmaz [DERS 15]
③ su gerçek hızda: akış 2,0–3,0 sn arasında kopar, hazne 3,0–4,5'te dolar, dudaktan 4,5–6,0'da taşar
   ⛔ Su ilk karede zaten akıyorsa S6 yeniden — "ödül" anı yok demektir.
   ⛔ Su 900× okunuyorsa (ipek/sis dokusu) rejim dikişi kırılmıştır.
④ G5 → G6 kesmesinde REJİM DİKİŞİ var ve BEYANLIDIR: B'den G'ye geçişte bulut dokusu şeritten durağana döner.
```

---

## 9. MÜZİKSİZ SES KAPISI

```
⛔ 0,0–56,0 boyunca müzik YOK — melodi, nabız, akor yastığı, yükselen ped hiçbir saniyede olmayacak.
⚠️ BLUE DOOR QA'sında 00:56–01:00 arasında arka plan müziği SIZDI. Teslim öncesi ses yatağı baştan sona
   dinlenir ve üretecin kendi müziği kapatılır.
⭐ Bu filmin ses kanıtı: taşın tınısı S0'dan S3'e İNCELİR (kalın kütle → ince duvar). Ölçüm: S0 ve S3'ün
   vuruş sesleri yan yana dinlenir; fark duyulmuyorsa ses yatağı yeniden kurulur.
S6'da 48,0–48,5 ve 49,0–49,8 aralıkları NEREDEYSE SESSİZDİR; bu sessizlik kurguda korunur.
```

---

## 10. ZAMAN VE IŞIK

```
IŞIK GÜNÜ  07:00 → 19:00 + 8 sn = 12 sa 0 dk 8 sn (6 × B + 1 × G) ≤ 14 sa ✅
GÜNEŞ      40°K · δ +21° (erken yaz) · 82°/24° → 295°/+2,6°
⛔ Güneş hiçbir karede kadrajda DEĞİL: kadraj yatayda 333,4°–26,6° görür [DERS 39].
⛔ Güneşe "disk" denmez, hiçbir promptta adı geçmez.
TAKVİM     ~5 hafta · ⛔ IŞIKTAN OKUNMAZ, SAHADAN okunur: yığın büyür, brandalı istif erir, döşemeye toz yayılır.
           ⛔ BLOCK: sekiz kare içinde mevsim değişirse (yaprak, kar, çiçek) — tek ışık günü kırılır.
```

---

## 11. BİLİNEN VE BEKLENEN RİSKLER

```
⚠️ BEYANLI FIX ×2 (prompt kapısı 23.09.2026 · BLOCK 0 · MOTION FOCUS FIX 0):
   ① ARAÇ KUTU SETİ ölçülmedi → ⛔ üretim açılamaz, plan yazılabilir
   ② yedi sahnenin süresi eşit (8,0) → ⑥ METRONOM, sahip kuralı, düzeltilmez

⚠️ EN BÜYÜK RİSK — KİMLİK: serbest biçimli ejderha sekiz bağımsız karede farklı çizilebilir (§3).
   Azaltma: blok zarfı px'le kilitli · ham kesim bandı çapa · beş maddelik ejderha cümlesi G2→G7'de birebir ·
   pilot S1.
⚠️ İKİNCİ RİSK — S2'nin "boş" görünmesi: bu sahnede oyma ilerlemez. Kanıt karot ve deliktir; ikisi de
   kadrajda ölçülebilir. Karot okunmuyorsa sahne ⑦ merceğinde PARKED okunur.
⚠️ ÜÇÜNCÜ RİSK — ıslanma sınırı: modelin bütün taşı ıslatma eğilimi yüksek. §1 ② bunun kapısıdır.
⚠️ DÖRDÜNCÜ RİSK — model eksiltmeyi anlamayıp taşı "büyütebilir" (§4). MOTION FOCUS'ların tamamı
   malzemeyi BLOKTAN yığına taşır ve sekiz karede "Stone is only ever taken away, never put back" durur.
ℹ️ §9'un metin yasağı 8 yüzey kontrolü bu depodaki NEGATIVE yazımında FİİLEN KOŞMUYOR (kontrol
   "…annotated by anyone" ifadesini arıyor, depodaki çekirdek "…included." ile bitiyor). Taş atölyesinde
   dürüstçe sayılabilecek yüzey 5–6 olduğu için liste UYDURULMADI; §7'nin sert kapısı bunun yerini tutar.
   Sahip kararına açık: ya kontrol gevşetilir ya çekirdek yeniden yazılır — 27 filmin hepsini ilgilendirir.
```
