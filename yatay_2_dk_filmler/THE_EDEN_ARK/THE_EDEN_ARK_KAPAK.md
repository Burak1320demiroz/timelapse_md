# 🖼️ THE_EDEN_ARK — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30]

## 0. İKİ İŞ, TEK GÖRÜNTÜ

```
KAYNAK KARE     G18 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Model başlığı YAZMAZ; tipografi post-prodüksiyon.
                ⛔ Öncesi/sonrası bölme YOK — sahip kararı 19.09.2026 (kapak yalnız GN).
KAPAK KARTI     teslimin son 5,0 sn'si (144,0–149,0) · hareketsiz · başlıklı · SAHNE DEĞİL [DERS 4]
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 143.9 -i teslim.mp4 -frames:v 1 g18_kaynak.jpg
                bash araclar/zincir_kontrol.sh g18_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
BAŞLIK          "THE EDEN ARK" (İngilizce · 3 kelime · sahibin film adı) — YAYIN_PAKETI başlığıyla aynı vaadi söyler
ÖLÇÜ            16:9 · 1920×1080 (video içi kart) · küçük resim 1280×720 aynı kaynaktan
```

### Kapakta ne var — G18'in ölçüsüyle

```
GÖRÜNEN       mavi saat · üst yarı koyu mavi gök (üstten 0 → 540), solda soluk turuncu pay · solda tuğla baca (x 100,
              üstten 418 → 671) · ortada su dolu BOŞ kuru havuz ve açık kapılar · sağda kapıyı yeni geçmiş gemi (x 1328 →
              1657, üstten 552 → 675): lacivert gövde, ışıyan cam kubbe, içinde yeşil taçlar ve sıcak lamba dizileri ·
              kıçın sağında küçük kırmızı römorkör (x 1685 → 1728) · uzakta mendirek feneri (x 1850)
⭐ KANCA        IŞIK — lacivert bir karede tek sıcak, uzun, parlak cisim: camın altında yeşil. "Gemide ORMAN mı var?"
⭐ İKİNCİ OKUMA BOŞ HAVUZ — gemi az önce oradan çıktı; havuz, geminin nereden geldiğini söyler (öncesi bölmesiz).
⚠️ ZAYIFLIK — ÖLÇÜLDÜ: gemi kadraj eninin yalnız %17'si (329 px). 1280'lik küçük resimde 219 px, 120 px testinde
              ≈ 21 px. Kapağın sağ yarısını gemi değil IŞIK taşır. Bu, "gemi kapıyı geçmiş olsun" kararının bedelidir
              (02 §1 tablosu). ⛔ Kırpma, yakınlaştırma ve ikinci açı ile kurtarılmaz [P21-f].
⚠️ SPOİLER BÜTÇESİ — BEYANLI: kapak sonucu verir (gemi yüzüyor, içi yeşil). Yolu vermez: paslı açılış, tek ağacın
              indirilişi, camın yürüyüşü, havuzun doluşu.
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G18 + başlık bandı satırı)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.

```
[G18 USTA KARE PROMPTU BİREBİR — BOLUM_2 son bölümü]
+ ek satır (COMPOSITION sonuna):
Leave a horizontal band between roughly sixty-two and eighty-five percent of frame height on the left two
thirds of the picture visually simple and low-contrast so that a title can be set over it: no structural
detail, no strong edge and no bright object inside that band — open deep blue sky only.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Yatayda bant YANDA ve ÜSTTE durur: gemi sağ alt çeyrekte, başlık sol üstte gökte. Bant güvenli alan dışında
(üst 60 px · alt 100 px · sağ üst 300×100 px — §2.8 varsayılanı, ⛔ ölçülmedi). ⭐ Ek satır G18'in KENDİSİNİ değiştirmez:
o bölge G18'de zaten boş gök — satır yalnız modelin oraya bulut kümesi koymasını önler.

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        THE EDEN ARK (büyük harf · tek satır)
YÜKSEKLİK    büyük harf 100 px (%9,3 kare boyu ≥ %8 ✓) — 120 px'e küçülünce ≈ 11 px
KONUM        x = 180 – 1080 px (≈ 900 px en) · y = 200 – 300 px (üstten) · bacanın tepesinden (418) 118 px yukarıda,
             gemiden (x 1328) 248 px solda · sağ üst 300×100 px'e ve alt 100 px'e girmez ✓
KONTRAST     kırık beyaz metin, koyu mavi gök üstünde ≈ 10:1 · ⛔ bant konmaz
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK (5 sn hareketsiz)
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png
                 ⓐ silüet: sağda sıcak, yatay bir ışık çizgisi (gemi ≈ 21 px) + solda ince koyu dik çizgi (baca) — ⚠️ KISMEN
                 ⓑ kelime şekli: "THE EDEN ARK" 11 px cap — ✅ eşiğin üstünde
                 ⓐ zayıfsa SAHNE yeniden üretilmez (karar 02 §1); kayıt QA'ya geçer
② KAPAK KANITI  zincir_kontrol.sh g18_kaynak.jpg kapak.png → çıkış 0 olmalı   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) → yabancı dönüm noktasını (tek kaldırma · yüzme anı)
                söyleyebiliyor mu: HAYIR — kapak sonu gösterir, başlık dönüşümü adlandırır, ilk 2 sn paslı ölü gemi
④ BAŞLIK = VAAT  kapak "ışıyan yeşil bir gemi" der; platform başlığı "terk edilmiş yük gemisi yüzen yağmur ormanı
                olur" der — ✅ aynı vaat, kapak sonucu, başlık yolu söyler
```
