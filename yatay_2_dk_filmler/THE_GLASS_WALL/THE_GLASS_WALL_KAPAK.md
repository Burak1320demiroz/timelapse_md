# 🖼️ THE_GLASS_WALL — KAPAK

**Kaynak:** `MUZIK_VE_KAPAK.md` §2 · kart A adım 9 · KAPAK KANITI [DERS 30]

## 0. İKİ İŞ, TEK GÖRÜNTÜ

```
KAYNAK KARE     G12 usta kare — kapak AYRI ÜRETİLMEZ, ondan türer [§2.2]. Prompt aşağıda usta kare (G12) promptunun
                kopyası + tek ek satır (başlık bandı). Model başlığı YAZMAZ; tipografi post-prodüksiyon.
KAPAK KARTI     teslimin son 5,0 sn'si (120,0–125,0) · hareketsiz · başlıklı · SAHNE DEĞİL [DERS 4]
KAPAK KANITI    kaynak TESLİM dosyasından alınır (kırpma kareleri kaydırır — KURGU_VE_TESLIM §2):
                ffmpeg -ss 118.0 -i teslim.mp4 -frames:v 1 g12_kaynak.jpg
                bash araclar/zincir_kontrol.sh g12_kaynak.jpg kapak.png   → çıkış 2 = kapak filmin dünyasından değil, TESLİM YOK
BAŞLIK          "THE GLASS WALL" (İngilizce · 3 kelime) — YAYIN_PAKETI başlığıyla aynı vaadi söyler
ÖLÇÜ            16:9 · 1920×1080 (video içi kart) · küçük resim 1280×720 aynı kaynaktan
```

---

## 📸 KAPAK GÖRSEL PROMPTU (G12 + başlık bandı satırı)

> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve kapı sayımına girmez.
> ⛔ **Metinsiz üret.** Prompt hâlâ `no text` der. Model yazdığı yazıyı bozar.

```
[G12 USTA KARE PROMPTU BİREBİR — BOLUM_2 son bölümü]
+ ek satır (COMPOSITION sonuna):
Leave a horizontal band between roughly 48 and 60 percent of frame height on the LEFT side
of the picture visually simple and low-contrast so that a title can be set over it: the olive tree
top sits at approximately 56 percent — keep the area left of the olive trunk, between 48 and 62
percent frame height, free of structural detail, strong edges and bright objects. Open sky or
low-contrast hillside haze only inside that band.
Output: 16:9, 4K, no text, no watermark.
```

⚠️ Yatayda bant SOL YAN — zeytin ağacı sol %8–15, sera ve ev sağ yarıda; bant zeytin ağacının
solunda, ufuk hizasında, güvenli alan dışında (üst 60 px · alt 100 px · sağ üst 300×100 px —
§2.8 varsayılanı, ölçülmedi). Bant: %x 0–15 arası, %y 48–62 arasında.

---

## 🔤 BAŞLIK DİZGİSİ (post-prodüksiyon) [MUZIK_VE_KAPAK §2.3]

```
METİN        THE GLASS WALL (büyük harf · 3 kelime)
YÜKSEKLİK    büyük harf ≥ %8 kare boyu = ≥ 86 px @1080 (120 px'e küçülünce ≈ 10 px — okunma eşiği)
KONUM        x = 30–280 px (sol bant · %x 1,6–14,6) · y = 480–560 px (%y 44–52 · ufuk hizası) · sağ üst 300×100 px'e ve alt 100 px'e girmez
KONTRAST     ≥ 4,5:1 · gerekirse düz koyu bant (gradyan değil) — gün batımı sarısı zemin için koyu
YAZI TİPİ    tek ağırlık · geniş harf aralığı · gölge/kontur/parlama YOK · animasyon YOK (5 sn hareketsiz)
```

---

## 🔍 KONTROL VE KANITLAR

```
① 120 PX TESTİ  sips -Z 120 kapak.png --out kapak_120.png   → ⓐ silüet (sera + ev + zeytin + deniz) okunuyor mu · ⓑ "THE GLASS WALL" şekli ayırt ediliyor mu
                 ⓐ kayboluyorsa SAHNE yeniden üretilir, kapak yeniden çerçevelenmez; ⓑ kayboluyorsa punto/kelime
② KAPAK KANITI  zincir_kontrol.sh g12_kaynak.jpg kapak.png → çıkış: ⬜   [DERS 30]
③ SPOILER       dört yüzey (başlık · kapak · ilk 2 sn · açıklama) yan yana → biten sera ve hasat kasasını söyleyebiliyor mu: HAYIR olmalı [§3.3]
④ BAŞLIK = VAAT  kapak "THE GLASS WALL" (yapı adı) · YAYIN_PAKETI başlığı aynı yapıyı söylüyor: ✓
```
