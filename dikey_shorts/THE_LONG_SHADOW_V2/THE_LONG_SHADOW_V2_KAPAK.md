# 🖼️ THE LONG SHADOW v2 — KAPAK

```
⛔ FİLMDE KAPAK KARTI YOKTUR. Logo yok, kart yok, müzik yok. Bu dosya yalnız platforma YÜKLENEN
   küçük resmi tanımlar; teslim videosunun sonuna hiçbir şey eklenmez [TESLİM YAPISI].
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     ⭐ YALNIZ G7 — S6'nın hedef karesi, filmin SON karesi [DERS 30 · MUZIK_VE_KAPAK §2.2]
           ⛔ G0 kapağa GİRMEZ. Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026.
KANIT      bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
⭐ v1 NOTU  THE LONG SHADOW v1'in dört merceğinden üçü, teslim dosyasının sonundaki 5,4 saniyelik
           KAPAK KARTINI 7. sahne saydı ve ① ile ④ bu yüzden de düştü [QA/RAPORLAR/THE_LONG_SHADOW.md].
           Bu teslimde video içinde kart YOKTUR; kapak yalnız bu dosyadır ve yalnız G7'dir.
BAŞLIK     They Built a House and the Street Lost the Sun | AI Timelapse
           (⛔ İNGİLİZCE, PAKETLEME §10 · sahip onayı bekliyor)
```

---

## 1. ⭐ NEDEN SON KARE TEK BAŞINA ÇALIŞIYOR — çelişki kancası

```
KAPAKTA GÖRÜNEN   dar bir sokak, iki duvarı kaçış noktasına doğru daralıyor · SOLDA gölgede duran,
                  yeni, bitmiş, üç katlı bir ev — üst kenarı 1793 px'te, harpuştası taze ·
                  SAĞDA ikindi güneşiyle ılık, kireç badanalı kesintisiz bir sıra ev duvarı ·
                  o duvarın üstünde TABANDAN SAÇAĞA UZANAN, 163 px eninde KARA BİR BANT ·
                  yukarıda iki saçak arasında dar ve hâlâ açık bir gök yarığı ·
                  aşağıda tamamen gölgede kalmış, yeni dökülmüş sokak taşları

BAŞLIKTA YAZAN    THE LONG SHADOW

KANCA = ÇELİŞKİ   Kapakta üç şey aynı anda okunur ve birbirini yalanlar:
                  ① GÖK HÂLÂ AYDINLIK — akşam olmamış, saat üçe geliyor
                  ② DUVARIN YARISI GÜNEŞLİ — demek güneş hâlâ sokağı görüyor
                  ③ AMA ARADA TABANDAN TEPEYE KARA BİR BANT VAR
                  Soru kapakta doğar: "Gök aydınlıkken o duvarın o parçası neden kapkaranlık?"
                  Cevap da kapaktadır ve karşısında durur: solda yeni bir ev.

KANIT NESNESİ     ⭐ KARA BANT — 163 px eninde, 675 px boyunda, ılık taşın üstünde. 120 px'lik
                  küçük resimde 18 × 75 px kalır ve ışık/koyu kontrastını KORUR. Bant kapağın
                  ikinci cümlesidir: eve bakmadan "bir şey burayı kapattı" der [P3-b: piksel değil,
                  kontrast]. ⭐ Bandın iki dikey kenarı keskin, üst kenarı saçak hattının TAM ÜSTÜNDE.

İKİNCİ OKUMA      ⭐ İKİ TARAFLI DUVAR — aynı duvar, aynı taş, aynı badana: bir yanı ılık sarı,
                  öbür yanı soğuk mavi-gri. Küçük boyutta bile "burası kesildi" okunur. Filmin
                  bütün aritmetiği bu tek kenarın içindedir.
ÜÇÜNCÜ OKUMA      YENİ EV KENDİ GÖLGESİNDE. Güneşi alan şeyin kendisi de karanlıktadır; kapak
                  kimseyi suçlamaz, yalnız gösterir.
DÖRDÜNCÜ OKUMA    GÖK YARIĞI — dar, dikey, hâlâ parlak. Ölçek verir ve "akşam değil" der; bant
                  bir günün bitişi değil, bir düzenin başlangıcıdır.

⛔ Kapak G5 ya da G6 DEĞİLDİR: G5'te bant saçağın bir metre altındadır ve duvarın üstünde ince bir
   ışık şeridi kalır — "az kalsın" der, "oldu" demez; G6'da şerit bir karış kalır ve küçük boyutta
   bant tamamlanmış gibi görünür ama defter 0,955'tir, yani KAPAK YALAN SÖYLER [DERS 30].
⛔ Kırmızı ok / çember / "56 SECONDS" yazısı YOKTUR [MUZIK_VE_KAPAK §4.4 · KANAL_KIMLIGI palet].
⛔ SPOILER BÜTÇESİ: kapak sonucu verir, YOLU vermez. Kapakta görünmeyen ve filmin 56 saniyesini
   taşıyan iki şey var: ① çizginin nasıl basamak basamak çıktığı ② gölgeyi atan nesnenin film
   içinde üç kez DEĞİŞTİĞİ (duvar → çekirdek → çatı). Bakan kişi bandın nasıl büyüdüğünü bilemez.
⭐ DEFTERİN KENDİSİ KÜÇÜK BOYUTTA OKUNMAZ — ve bu bilerek böyledir. 1,000 sayısı 120 px'te 3 px'lik
   bir farktır. Kapak sayıyı değil, SONUCU gösterir; sayı QA_SPEC'in işidir.
```

---

## 2. BAŞLIK YERLEŞİMİ — ⭐ gökte değil, YERDE

```
METİN        THE LONG SHADOW       ⛔ iki satır (tek satır 15 harfte 96 px cap'e iner = okuma eşiği)
             satır 1  THE LONG     satır 2  SHADOW
CAP YÜKSEKLİĞİ  120 px · satır arası 30 px · blok yüksekliği 270 px
KONUM        ortalanmış · y = 1450 – 1720 px (ÜSTTEN)
             satır 1  y 1450 – 1570      satır 2  y 1600 – 1720
ZEMİN        ⭐ SOKAK TAŞLARI — 14:40'ta sokak tabanının TAMAMI gölgededir (güneş az 232°, yeni ev
             11,34 m; gölge sokağı boydan boya geçer). Alt 650 px düzgün koyu, dokusu ince.
             Kontrast 4,5:1 kendiliğinden sağlanır.
             ⛔ BANT KONMAZ — zemin zaten koyu ve düz [MUZIK_VE_KAPAK §2.5 KONTRAST].
             ⛔ GÖĞE KONMAZ: gök yarığı 14:40'ta hâlâ açıktır ve dardır; beyaz metin orada erir,
                ayrıca gök yarığı kapağın üçüncü okumasıdır, kapatılamaz.
PAYLAR       üstte 40 px (oluk şeridinin başladığı yere), altta 200 px (kadraj dibine)
             ⭐ Başlık, S0'da SÖKÜLÜP yeniden döşenen taşların üstünde durur — filmin ilk işi,
                filmin son gölgesinin altında.
YAZI TİPİ    tek ağırlık, geniş harf aralığı · gölge, kontur, parlama YOK
RENK         kırık beyaz · ⛔ saf beyaz değil (koyu taşta parlar)
```

### 120 px testi — üç soru [MUZIK_VE_KAPAK §2.5 · §4.2]

```
ⓐ 120 px'e indirildiğinde ne okunuyor?
  → sağda ılık duvar, üstünde kara dikdörtgen (18 × 75 px) · solda koyu dikey kütle · yukarıda
    ince parlak yarık · altta iki satır beyaz metin. Dört şey, dördü de ayrı. ✅
ⓑ Başlık ile kapak AYNI şeyi mi söylüyor?
  → HAYIR. Kapak "bir duvarın parçası karanlık" der; başlık yalnız adını koyar ve hangi gölge
    olduğunu söylemez. Asıl soru ("neden o parça?") ne kapakta ne başlıkta CEVAPLANIR. ✅ [§2.3 · §3.3]
ⓒ Sağ alt köşeye siyah bir kutu (≈120 × 35 px) konduğunda kaybolan bir şey var mı?
  → HAYIR. O bölge sokak tabanının sağ kenarıdır; bandın alt ucu y 1211 px'te (üstten) biter,
    zaman damgası bandının dışında. ✅
```

---

## 3. VARYANTLAR

```
ⓐ ⭐ ANA — yukarıdaki yerleşim. İki satır başlık, sokak taşlarının üstünde, kadrajın alt üçte birinde.

ⓑ BAŞLIKSIZ — hiç metin yok, yalnız kare. ⚠️ Bu filmde ZAYIFTIR: kare tek başına "dar bir sokakta
   akşam" diye de okunabilir ve kancayı kuran şey (bandın anormalliği) metinsiz kalınca kaybolur.
   LAST FIRING'de başlıksız varyant ciddi bir adaydı çünkü karede tek parlak nokta vardı; burada
   karede tek KOYU leke var ve koyu leke kendi başına soru sormuyor.

ⓒ ALT BAŞLIK — ⓐ'nın altına, y ≈ 1800 px'e, 45 px cap ile "ONE DAY" eklenir.
   ⚠️ Zamanı söyler ama kapağı iki cümleli yapar; küçük boyutta ikinci satır kaybolur.

⛔ KIRPMA VARYANTI YOK. Bu kare kırpılamaz: kanıt nesnesi SAĞDADIR (bant, x% 59,28 → 74,34) ve
   karşı ağırlık SOLDADIR (yeni ev, x% 35,00 → 42,50). Yatay kırpma ikisinden birini keser ve
   kapak çelişkisini yok eder. Dikey kırpma ya gök yarığını (üçüncü okuma) ya başlık zeminini alır.
```

---

## 4. ÜRETİM NOTU

```
Kapak G7'nin ÜRETİLMİŞ karesinden alınır, ayrıca üretilmez [DERS 30].
   bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png   → çıkış 0 olmalı
⛔ Kapakta renk düzeltmesi, kontrast itmesi, doygunluk artışı YAPILMAZ: kapak ile videonun son karesi
   aynı görüntüdür. Farklılarsa [DERS 30] kapak kanıtı düşer.
⭐ BU FİLMDE KONTRAST İTMESİ AYRICA YASAKTIR: bandın kenarı 6,2 px'lik bir yarıgölgedir ve
   kontrast itmesi onu sertleştirir. Sertleşen kenar QA_SPEC §2ⓐ'yı düşürür — yani kapak
   düzeltmesi filmin ölçümünü bozar. LUT kararı §2'den SONRA kilitlenir.
⛔ Metin yalnız kapağa basılır, MASTER'a değil [BROKEN CLIMB ④ 5,1].
```
