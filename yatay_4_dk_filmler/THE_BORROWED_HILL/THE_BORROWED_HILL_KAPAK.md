# 🖼️ THE BORROWED HILL — KAPAK

```
⛔ FİLMDE KAPAK KARTI YOKTUR (sahip kararı 17.09.2026). Film S23'ün son geniş
   kadrajında biter. Bu dosya yalnız platforma YÜKLENEN küçük resmi tanımlar.
BOYUT   1280 × 720 · JPG · ≤ 2 MB  [A17-b · araç dokümanı sınıfı]
KAYNAK  G0 ve G24 — ikisi de filmin kendi kareleri [DERS 30]
KANIT   bash araclar/zincir_kontrol.sh g24_kaynak.jpg kapak.png → çıkış 2 = TESLİM YOK
```

## 1. Fikir — aynı açıdan iki durum

```
Proje sahibinin şartı (17.09.2026): "Kapakta, aynı açıdan başlangıçtaki tepe ile son
durum arasındaki fark okunmalı; küçük yazı ve çok sayıda makine bu fikri gölgelemesin."

⭐ İki yarı DEĞİL, İKİ DURUM: kapak dikey olarak ortadan bölünür.
   SOL %50   G0 kırpması — tepe 16,0 m, kadrajın %66,9'unda, uzak krater sırtının ÜSTÜNDE
   SAĞ %50   G24 kırpması — tepe 3,0 m, %44,9, o çizginin ALTINDA; tümsek ve yanık pencere
⛔ İKİ YARIDA DA UZAK KRATER SIRTI GÖRÜNÜR ve AYNI YÜKSEKLİKTEDİR (%51,6).
   Kapağın çalışması buna bağlıdır: izleyici farkı ancak ortak çizgiden okur.
⛔ İki yarı da 1:1 piksel kırpmadır; ölçeklenmez. Aralarına çizgi, çerçeve ya da
   gradyan konmaz — sert kesme.
⛔ MAKİNE YOK: iki yarıda da çalışan makine görünmez. Fikri gölgeler.
   G0 kırpmasında kesim rigi kadraj dışında bırakılır; G24 zaten boştur.
```

## 2. Metin

```
METİN   SAME HILL        (2 kelime · 0–3 kelime kuralı [MUZIK_VE_KAPAK §2.3])
YER     üst orta bant · y 40–140 · iki yarının ortasına oturur, ikisini de kesmez
PUNTO   kalın sans-serif · büyük harf · siyah dış hat + düşme gölgesi
⛔ "Mars" · "üs" · "sığınak" kelimeleri KULLANILMAZ — başlık zaten söylüyor,
   kapak SORUYU sorar [MUZIK_VE_KAPAK §3.3 spoiler bütçesi].
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketi bandı (≈120 × 35 px) [MUZIK_VE_KAPAK §4.2].
   Yanık pencere oraya DÜŞMEZ — sağ yarının orta bandında durur.
```

## 3. Testler

```
① 120 PX       sips -Z 120 kapak.png → ⓐ iki yarının farkı ⓑ metin okunuyor mu
② SAĞ ALT      köşeye siyah kutu koy: kaybolan bir şey var mı
③ ⭐ ÇAPA      uzak krater sırtı iki yarıda da aynı yükseklikte mi
④ ⭐ PENCERE   sağ yarıda yanık pencere seçiliyor mu (1,2 m → 19 px; kapak kırpmasında
               1280 geniş kaynaktan ~2,0× → ≈ 25 px · sıcak leke olarak okunmalı)
⑤ KAPAK KANITI zincir_kontrol.sh g24_kaynak.jpg kapak.png [DERS 30]
⑥ KARANLIK MOD sağ yarı akşam ışığındadır; koyu temada tümsek ile gök ayrışıyor mu
```

## 4. Üç varyant [MUZIK_VE_KAPAK §4.3]

```
ⓐ İKİ DURUM + METİN   yukarıdaki yerleşim · ana varyant
ⓑ YALNIZ G24          tek kare: tümsek, düz ocak tabanı, yanık pencere · metin yok
ⓒ YALNIZ G0           tek kare: el değmemiş sırt tarlası ve tepe · metin "SAME HILL"
⚠️ Kısa dikey formatta platform A/B aracı çalışmaz; bu film 16:9 UZUN formattır,
   yani "Test & Compare" BU FİLMDE KULLANILABİLİR [A15-b · A17-c]. ⭐ Deponun ilk
   A/B denemesi burada yapılabilir — kazanan İZLEME SÜRESİ PAYINA göre seçilir.
```
