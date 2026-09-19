# 🖼️ ONE MORE TURN — KAPAK

```
⛔ FİLMDE KAPAK KARTI YOKTUR. Logo yok, kart yok. Bu dosya yalnız platforma YÜKLENEN
   küçük resmi tanımlar; teslim videosunun sonuna hiçbir şey eklenmez [TESLİM YAPISI].
BOYUT      1080 × 1920 (dikey) · JPG · ≤ 2 MB
KAYNAK     G0 ve G6 — ikisi de filmin kendi kareleri [DERS 30]
KANIT      bash araclar/zincir_kontrol.sh g6_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
BAŞLIK     Will This Abandoned Watermill Turn Again? | AI Timelapse   (proje sahibinin metni)
```

---

## 1. ⭐ NEDEN BÖLÜNMÜŞ KAPAK — mil dikeyinde

```
Proje sahibinin şartı: kapak MİL MERKEZİNDEN bölünür (18.09.2026). Bu filmde bölme
YATAY değil DİKEYDİR: sol yarı eski çark, sağ yarı yeni çark, ikisi AYNI MİLİN üstünde.
İzleyici aynı göbeği iki yarıda da görür — "aynı çark mı?" sorusu kapağın kendisidir.
⚠️ Bölünmüş kapak bu depoda ÖLÇÜLMEMİŞTİR [MUZIK_VE_KAPAK §4.4]; THE LAST CIRCLE ve
   THE NARROW GORGE'la birlikte tutunma verisiyle okunacak.
```

## 2. Yerleşim — 1:1 piksel, ölçek değişmeden

```
BÖLME ÇİZGİSİ  dikey · x = mil merkezi = %46,1 → x ≈ 498 px
SOL  x 0–498     G0 kırpması · aynı x aralığı, aynı y (kırpma yok, yalnız maske)
                 ⭐ içinde: kırık gri çarkın SOL yarısı (sarmaşıklı alt-sol, açık üst-sol
                    çeyrek), kuru oluk, kapalı kapak, boş römork, iki dikme
SAĞ  x 498–1080  G6 kırpması · aynı aralık
                 ⭐ içinde: yeni çarkın SAĞ yarısı (kuru pale meşe; sağ alt kovalar boşalıyor),
                    duvar köşesi %82,4, beyaz çıkış oluğu, dere

⛔ DEMİR GÖBEK İKİ YARIDA DA GÖRÜNÜR — bölme çizgisi göbeğin tam ortasından geçer ve
   göbek iki yarıda aynı pikseldedir. Kapağın çalışması buna bağlıdır: izleyici aynı
   çarkı ancak ortak göbekten tanır. Göbek bir yarıda kayarsa iki ayrı değirmen okunur.
⛔ İki yarı da 1:1 PİKSEL kırpmadır — ölçeklenmez, sıkıştırılmaz.
⛔ Yarılar arasına çizgi, çerçeve, gradyan ya da gölge konmaz; sınır sert kesmedir.
⚠️ Işık farkı (sol 10:10 sağdan sıyırıcı · sağ 18:10 turuncu) yarıların sınırını zaten
   çizer; ayrıca vurgu istemez.
⚠️ SAĞ YARIDA ISLAK SOL YARI GÖRÜNMEZ (o, mil sol tarafındadır). Kapağın "döndü" kanıtı
   ıslaklık değil, beyaz çıkış oluğu + boşalan sağ alt kovalardır. Bu bilinerek seçildi:
   dikey bölmede kuru/ıslak karşıtlığı feda edilir, eski/yeni karşıtlığı alınır.
```

## 3. Metin

```
METİN      ONE MORE / TURN     (3 kelime · iki satır · 0–3 kelime kuralı [MUZIK_VE_KAPAK §2.3])
YER        üst gökyüzü bandı · y 60–300 (üstten) · mahya %80,2'nin (y ≈ 380) ÜSTÜNDE ·
           sol hizalı, sol kenardan 90 px içeride; her iki yarının üstüne yayılır
PUNTO      kalın sans-serif · büyük harf · beyaz · siyah dış hat + düşme gölgesi
⛔ "overshot" · "flume" · "sluice" gibi bilgi isteyen kelime KULLANILMAZ [P6].
⛔ SAĞ ALT KÖŞE BOŞ: süre etiketinin bandı (≈120 × 35 px) [MUZIK_VE_KAPAK §4.2].
   Dere ve çıkış oluğunun köpüğü %28–36 bandındadır; köşe (alt %5) zaten boştur.
```

## 4. Testler — geçmeden yüklenmez

```
① 120 PX       sips -Z 120 kapak.png → ⓐ iki yarının FARKI (gri/pale) ⓑ metin okunuyor mu
② SAĞ ALT      köşeye siyah kutu koy: kaybolan bir şey var mı [MUZIK_VE_KAPAK §4.2]
③ ⭐ GÖBEK      demir göbek iki yarıda da görünüyor mu · aynı pikselde mi (≤ 4 px)
④ KAPAK KANITI zincir_kontrol.sh g6_kaynak.jpg kapak.png [DERS 30]
⑤ KARANLIK MOD sağ yarı akşam ışığındadır; koyu temada duvar ile gök ayrışıyor mu
⑥ YÖN          sağ yarıda çıkış oluğu BEYAZ mı — "dönüyor" tek kanıt budur
```

## 5. Üç varyant — A/B için hazır [MUZIK_VE_KAPAK §4.3]

```
ⓐ BÖLÜNMÜŞ + METİN   yukarıdaki yerleşim · ana varyant
ⓑ BEDELİN NESNESİ    yalnız G0'dan yakın kırpma: sarmaşıklı kırık çark, gergin halat · metin yok
ⓒ METİNSİZ SİLUET    yalnız G6 · turuncu ışıkta dönen çark, ıslak sol yarı, beyaz çıkış
⚠️ Kısa dikey formatta platform A/B aracı ÇALIŞMAZ [A17-c]; üçü hazır durur.
   ⓐ ve ⓒ USTA KAREDEN, ⓑ G0'dan türer.
```
