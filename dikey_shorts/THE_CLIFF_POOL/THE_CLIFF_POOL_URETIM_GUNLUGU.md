# 🗒️ THE CLIFF POOL — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · bu günlüğe tek satır yazılmadı · (22.10.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
⭐ PİLOT SIRASI (plan §PİLOT ÜÇLÜ): (a) G8 METİNDEN + kapak_prova (G8 ONAYINDAN önce) → (b) G8 → G7 (su %75, ışık sönük, ateş çukuru boş) →
        (c) S7 final (su taşar, ateş çukuru alev alır, ışıklar yanar) + S3 kaplama (bazalt taş + tik güverte) + (c′) S0 açılış (vinçle ilk dev kiriş iner, taglinelar gergin) —
        dokuz görsel, üç klip (S0 · S3 · S7; S2 akrilik cam montajı isteğe bağlı dördüncü); hepsi 2x'te izlenir
⭐ İHRAÇ: ihrac_kontrol.sh (kart 5,0 sn) + klip_eslestir.py <yayin.mp4> <S0…S7.mp4> --hiz 2 --kart 5 [DERS 86]
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md`. Plan: `THE_CLIFF_POOL_DIKEY_TIMELAPSE.md` · SPEC: `THE_CLIFF_POOL_QA_SPEC.md`.
> Format: İKİ KEYFRAME ZİNCİRİ — 8 sahne = 9 kare (G0…G8) + 8 I2V [KILAVUZ_REHBERI §2.7]. Izgara 8 × 8,0 = 64,0 sn
> (⚠️ SAHİP İSTİSNASI 22.10.2026 · kural 7 × 8 · sahibin briefi 8), paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn.

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32 · A7-d]

> ⭐ 08.09.2026: üç soru SEKİZE çıktı. Yordam ve test promptu:
> `kilavuzlar/ARAC_KARTLARI.md` §4-§5. Kart doldurulmadan tek kare üretilmez.

```
ARAÇ            Nano Banana 2 (görsel) + Veo 3.1 Lite (I2V)
ÖLÇÜM TARİHİ    22.10.2026
① KUTU SETİ     ffprobe: 5,0 / 10,0 sn   beş klip aynı mı: evet
   SAHNE TAVANI (en büyük kutu − 1,00) = 9,00 sn  → plandaki en uzun sahne: 8,0 sn (UYGUN ✅)
② KAMERA        ilk/son kare kayması: 0 px (statik tripod kilitli)
   GEOMETRİ KANALI start/end frame (iki keyframe kilitli)
③ GÖLGE         ilk/son kare açı farkı: 8° (doğal dönüş)
④ NEGATİF       metin içi: 0/5 sızdı · ayrı alan: evet
⑤ PROMPT TAVANI 4511 karakter · promptun son nesnesi göründü mü: 5/5
⑥ İLK KARE      zincir_kontrol.sh çıkışı: 0
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: evet (10,0 sn)
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol çıkışı: 0
⑨ ÇÖZÜNÜRLÜK   ffprobe kaynak: 1080 × 1920 · YAKINLAŞMA TAVANI = 1,0× (tam dikey)
KARAR           bu araçla üretilir — kutu seti 10 sn tavan 9 sn, plan 8 sn, iki kare kilitli ✅
```

## 1. USTA KARE

```
KARE    ⭐ G8 İLK üretilen kare — METİNDEN (bitmiş teras, taşan sonsuzluk havuzu, yanan ateş çukuru, kehribar mimari ışıklar, alacakaranlık, işçisiz · tasarım referansı ve kapak
        kaynağı · son klibin HEDEF karesi) [§2.7 · DERS 91] — G7 bundan GERİYE (⏪), §2 tablosunun ilk satırı
ARAÇ    [görsel model + ayar]
TARIH   [gg.aa.yyyy]
DOSYA   ham: usta_ham.png · secilen: usta_secilen.png · teslim: G8.png
DENEME  __ / 4
ZAMAN   __ dk
NOT     [renk · ışık · boş çanak · çapa tuttu mu]
```

## 2. GÖRSEL ZİNCİRİ (⏪ G7…G0 GERİYE ÜRETİM)

```
G8 → G7  [değişim: su %75'e iner, ışıklar ve ateş çukuru söner, kuru taş dokusu]
G7 → G6  [değişim: su boşalır, havuz kuru, hortum ve vanalar çıkar]
G6 → G5  [değişim: mobilyalar ve biyo-etanol şömine çıkar, çıplak bazalt zemin]
G5 → G4  [değişim: pergola saçağı ve cam korkuluklar sökülür, boş güverte]
G4 → G3  [değişim: bazalt taş ve tik kaplamalar kalkar, çelik zemin plakaları açığa çıkar]
G3 → G2  [değişim: akrilik ön cam sökülür, açık konsol burun çeliği]
G2 → G1  [değişim: havuz haznesi ve oturma çukuru zemin plakaları kalkar, çıplak ana konsol kirişleri]
G1 → G0  [değişim: enine çelik çerçeve sökülür, vinçte askıda tek ilk I-kiriş, ham beton ankrajlar]
```
