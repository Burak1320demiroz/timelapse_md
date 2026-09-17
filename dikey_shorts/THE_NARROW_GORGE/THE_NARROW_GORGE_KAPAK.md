# 🖼️ THE NARROW GORGE — KAPAK

> ⛔ **KAPAK KARTI YOK.** Proje sahibinin kararı (16.09.2026): film 56,0 saniyede, akan suyla biter;
> bitmiş hikâyenin ardına hareketsiz afiş konmaz. Bu dosya yalnız **YÜKLENEN KÜÇÜK RESMİ** tarif eder.
> ⛔ **KAPAK İÇİN YENİ KARE ÜRETİLMEZ.** İki yarısı da filmin kendi karelerinden KIRPILIR [DERS 30].
> Yeni bir boğaz, daha büyük bir baraj, ekstra su ya da ekstra gök "afiş için" serbest değildir.

---

## 0. TEK İŞ, İKİ KARE

```
IZGARA KAPAĞI / SHORTS KÜÇÜK RESMİ   9:16 · 1080 × 1920 · siluet ailesi KÜTLE
KAYNAK KARELER   G0 (filmin ilk karesi) ve G7 (usta kare) — İKİSİ DE HOME kadrajında, aynı kamera
                 yedek: ffmpeg -ss 00.2 -i teslim.mp4 -frames:v 1 g0_kaynak.jpg
                        ffmpeg -ss 55.0 -i teslim.mp4 -frames:v 1 g7_kaynak.jpg
                 ⭐ kaynak kare TESLİM dosyasından alınırsa kırpma sonrası kare kullanılır [KURGU §7]
                 ⛔ S0, S1, S3 ve S6'nın YAKINLAŞMIŞ ara kadrajları kapağa girmez — yalnız HOME kareleri.
⛔ KAPAK KARTI   YOK (yukarı bakınız) · teslimin son 5 saniyesi diye bir bölüm bulunmaz
```

---

## 1. BÖLÜNMÜŞ KAPAK — kırpma geometrisi

> Eleştiri kuralı: **her iki yarı da hem KÖPRÜYÜ hem ANA AKIŞ DURUMUNU göstermeli.** Bir yarıya yalnız gök,
> diğerine yalnız su konursa önce–sonra karşılaştırması bozulur. Aşağıdaki kırpmalar bunu sağlar ve
> **ölçekleme yapmaz**: iki bant da kaynaktan 1:1 piksel alınır, bu yüzden hiçbir yerde esneme olmaz.

```
KAPAK          1080 × 1920
ÜST BANT       %45 · 864 px · KAYNAK G0 · kaynaktaki dikey aralık y 938 – 1802 (üstten), tam genişlik
               → içinde: dolaşan ırmak, söğütlü çakıl bariyerleri, TAŞ KÖPRÜ (kapakta y ≈ 427),
                 iki duvarın alt yarısı ve göz çizgisi
ALT BANT       %55 · 1056 px · KAYNAK G7 · kaynaktaki dikey aralık y 350 – 1406 (üstten), tam genişlik
               → içinde: SAVAK DUDAĞI ve inen beyaz TABAKA, enerji kırıcı havuz, TAŞ KÖPRÜ,
                 gövdenin derz çizgileri
DİKİŞ          y = 864 (üstten) · düz yatay çizgi · gradyan, gölge, çerçeve YOK
HİZA           ⭐ İki bant AYNI KAMERADAN geldiği için köprü, kaya bandı ve duvarlar iki yarıda da
               AYNI x'tedir. Kontrol: köprünün kemer ortası iki bantta da aynı piksel sütununda mı.
⛔ ÖLÇEKLEME    yok · döndürme yok · yatay kaydırma yok — yalnız dikey kırpma
⛔ Kırpma dikdörtgenleri usta kare ÜRETİLDİKTEN sonra doğrulanır; buradaki y değerleri plandaki
   TÜRETİLMİŞ yüzdelerden gelir (köprü %28,9 · dudak %80,1 · havuz %33), ölçülmemiştir.
```

---

## 2. BAŞLIK DİZGİSİ (post-prodüksiyon)

```
METİN         SAME RIVER?
DİL           İngilizce · 2 kelime   (TR alternatif: "AYNI IRMAK MI?" — üç satır olur)
SATIR         ⭐ İKİ SATIR: "SAME" / "RIVER?" — tek satırda 11 karakter kullanılabilir genişliğe
              (122 → 838 px = 716 px) sığmaz
YÜKSEKLİK     büyük harf yüksekliği ≥ kare yüksekliğinin %8'i (≥154 px) · toplam bant ≈ 348 px
KONUM         y = 60 – 408 (ÜSTTEN) — ÜST BANDIN üst bölümü: G0'ın duvarları ve göz çizgisi
              ⭐ NEDEN ORADA: üst bandın ALT yarısı "önce" ırmağını ve köprüyü taşıyor (y 368–864),
              alt bant ise ödülü taşıyor. Yazı ikisinden birinin üstüne düşerse karşılaştırma bozulur.
              Geriye yalnız üst bandın üst şeridi kalıyor: iki duvar ve aralarındaki boşluk.
              ⚠️ SAPMA BEYANI: MUZIK_VE_KAPAK §2.3 başlık bandını y 500–1400 arasında istiyor.
              Burada y 60–408 seçildi ve gerekçesi budur; §2.3'ten bilinçli sapmadır.
KONTRAST      ≥ 4,5:1 — METİN AÇIK (#E8E4DC, kanal paleti "ana işaret") · arkasında DÜZ koyu bant
              (#101315, opak ya da ≥ %80), gradyan yok
YAZI TİPİ     tek ağırlık, geniş harf aralığı, gölge/kontur/parlama YOK
⛔ Bu metin videonun İÇİNE girmez; promptlarda hiçbir yazı yoktur [D-b].
⛔ Açılış kancası kullanılacaksa (ör. 0,0–2,0 sn) AYRI bir kurgu katmanıdır, köprüyü ve ırmağı ÖRTMEZ.
```

---

## 3. KONTROL VE KANITLAR

- [ ] **HER İKİ YARIDA DA KÖPRÜ VAR MI** — yoksa kırpma yeniden; bu kapağın tek kuralı budur
- [ ] **HER İKİ YARIDA DA ANA AKIŞ DURUMU OKUNUYOR MU** — üstte dolaşan ırmak, altta inen tabaka
- [ ] **FİNAL HİYERARŞİ** alt bantta: ① inen beyaz tabaka → ② tam beton gövde → ③ köprü ve ölçülü akış
- [ ] **SERPİNTİ KÖPRÜYÜ ÖRTMÜYOR** — örtüyorsa G7 yeniden (plan §Final hiyerarşi)
- [ ] **120 PX TESTİ** — üç görüntüye: `sips -Z 120 kapak.png --out k_120.png` · aynısı g0 ve g7 için
      ⓐ silüet: boğazı kapatan tek kütle + ortada düşey beyaz bant seçiliyor mu? (KÜTLE ailesi)
      ⓑ ÜST bantta ırmak, ALT bantta tabaka 120 px'te de ayırt ediliyor mu? (bölünmüş kapağın riski)
      ⓒ başlık: "SAME / RIVER?" kelime şekilleri seçiliyor mu? Kaybolursa punto büyür — "olsun" denmez
- [ ] **KAPAK KANITI** [DERS 30] — İKİ koşu:
      `bash araclar/zincir_kontrol.sh g0_kaynak.jpg kapak_ust_bant.png` → __
      `bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak_alt_bant.png` → __  (çıkış 2 = TESLİM YOK)
- [ ] **GERÇEKLİK**: kapakta logo, firma, baraj adı, gerçek yer iddiası YOK
