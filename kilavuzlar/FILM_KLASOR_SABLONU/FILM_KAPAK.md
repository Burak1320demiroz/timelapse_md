# 🖼️ <FILM_ADI> — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30]

## 0. İKİ İŞ, TEK GÖRÜNTÜ

```
KAYNAK KARE     G<N> usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Prompt aşağıda usta kare (G<N>) promptunun
                kopyası + tek ek satır (başlık bandı). Model başlığı YAZMAZ; tipografi post-prodüksiyon.
KAPAK KARTI     teslimin son 5,0 sn'si (<SURE>,0–<TOPLAM>,0) · hareketsiz · başlıklı · SAHNE DEĞİL [DERS 4]
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss ⬜ -i teslim.mp4 -frames:v 1 g<N>_kaynak.jpg
                bash araclar/zincir_kontrol.sh g<N>_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
BAŞLIK          "⬜" (İngilizce · ≤3 kelime) — YAYIN_PAKETI başlığıyla aynı vaadi söyler
ÖLÇÜ            16:9 · 1920×1080 (video içi kart) · küçük resim 1280×720 aynı kaynaktan
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G<N> + başlık bandı satırı)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.

```
[G<N> USTA KARE PROMPTU BİREBİR — BOLUM_2 son bölümü]
+ ek satır (COMPOSITION sonuna):
Leave a horizontal band between roughly ⬜ and ⬜ percent of frame height on the ⬜ [left / right] ⬜
of the picture visually simple and low-contrast so that a title can be set over it: no structural
detail, no strong edge and no bright object inside that band — open sky / plain ground only.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Yatayda bant YANDA durur (yapının boş tarafında), dikeydeki "üst orta üçte bir" kuralı değil:
yapı ve kanıt nesnesi kadrajın ⬜ [sol/sağ] yarısında, başlık öbür yarıda; bant güvenli alan
dışında (üst 60 px · alt 100 px · sağ üst 300×100 px — §2.8 varsayılanı, ⬜ ölçülmedi).

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        ⬜ (büyük harf · ≤3 kelime)
YÜKSEKLİK    büyük harf ≥ %8 kare boyu = ≥ 86 px @1080 (120 px'e küçülünce ≈ 10 px — okunma eşiği)
KONUM        x = ⬜–⬜ px (banda) · y = ⬜–⬜ px · sağ üst 300×100 px'e ve alt 100 px'e girmez
KONTRAST     ≥ 4,5:1 · gerekirse düz koyu bant (gradyan değil)
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK (5 sn hareketsiz)
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ silüet (yapı + ⬜) okunuyor mu · ⓑ KELİME şekli ayırt ediliyor mu
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez; ⓑ kayboluyorsa punto/kelime
② KAPAK KANITI  zincir_kontrol.sh g<N>_kaynak.jpg kapak.png → çıkış: ⬜   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → yabancı dönüm noktasını söyleyebiliyor mu: HAYIR olmalı [§3.3]
④ BAŞLIK = VAAT  kapak neyi vaat ediyor, YAYIN_PAKETI başlığı aynı şeyi mi söylüyor: ⬜
```
