# 📋 THE LONG SHADOW — QA KAYDI

```
KÜNYE      v1 · 9:16 · 7 klip · 1:04,9 · dört mercek koşuldu (4/4)
           ⛔ dördü de MOD V — ② ve ④'e belge verilmedi, bu yüzden ön koşudur
TESLİM     6 sahne × ~10 sn + 5,4 sn kapak kartı
KARAR      ⛔ YAYINLANMAZ. Yeniden planlanır, yeniden üretilir.
```

---

## 1. DÖRT HÜKÜM — dördü de düştü

| Mercek | Skor | HÜKÜM |
|---|---:|---|
| ① KARE | 3,3/10 Ⓥ | ⛔ **ALTI AYRI GÖRÜNTÜ** |
| ② İNŞA | 0,4/10 Ⓥ | ⛔ **FARKLI** · ⛔ **APPEARING** |
| ③ ZAMAN | 4,3/10 Ⓥ | ⚠️ GEÇİYOR — ama yön kırık |
| ④ TESLİM | 2,7/10 Ⓥ | ⛔ **DURUYOR** · **NONE FOUND** |

```
⭐ ÖLÇÜMÜN ASIL DEĞERİ: dört mercek birbirinden habersiz koştu (ikisi
   tasarım gereği, ikisi belge verilmediği için) ve dördü de bağımsız
   olarak AYNI kök sebebe işaret etti.
```

---

## 2. KÖK SEBEP — tek cümle

**Ters inşa üretim sırası koşulmadı.** Altı kare bağımsız üretildi; bu yüzden
altı farklı bina çıktı ve geri kalan her şey onun sonucudur.

Kanıt zinciri:
```
② 0:49,5   panelli cephe → tamamen camlı cephe        STRUCTURE IDENTITY 0/10
② 0:59,5   camlı cephe → balkonlu koyu kule           (üçüncü bina)
① 1:00,0   tuğla blok 4 kattan 5 kata çıktı           ANCHOR IDENTITY 0/10
① 1:00,0   arkadaki tepeler tamamen değişti
④          "the structure being built is abandoned"    PROMISE 2/10
```

`KILAVUZ_REHBERI §8` adım 2-3 (usta kare + geriye image-to-image) atlanınca,
YAPI BIBLE'ın birebir tekrarı **tek başına yetmedi.** Bu artık varsayım değil,
ölçüm [DERS 5].

---

## 3. İKİNCİ KÖK SEBEP — kapak kartı beyan edilmemişti

Teslim dosyasının son 5,4 saniyesi **kapak kartıdır**, sahne değildir. Ama
hiçbir belgede beyan edilmediği için üç mercek onu 7. sahne saydı:

```
① ANCHOR IDENTITY 0/10   "at 1:00.0 ... completely change"  ← kapak kartı
② C1 0/10                "secondary vantage reveals a completely different structure"
④ FINAL BEAT FAIL        "acting as a disconnected glamor shot"
```

⛔ Yani ①'in **ALTI AYRI GÖRÜNTÜ** hükmünün ve ④'ün **FAIL**'inin bir kısmı
filmin değil, **beyan eksikliğinin** sonucudur. Rapor haklı; belge eksikti.
Düzeltme: `TESLİM YAPISI` satırı ve rubriklerin `END CARD` alanı [DERS 4].

---

## 4. EN AĞIR ÜÇ BULGU (kapak kartından bağımsız, filme ait)

```
① 0:00,0   S0 boyunca sürekli yavaş bir PUSH-IN var — kamera kilidi tutmadı.
           I2V'de "no zoom" yazılıydı ve yetmedi [DERS 6].

③ 0:09,5   "Cut 1 to Cut 2 reverses time entirely" — ters açılış, filmin
           kendi yönünü kırdı. ④: "sabotages its own promise" [DERS 3].

③ 0:30-0:40 Kar bir sahnede anlık belirdi, bir sonrakinde anlık kayboldu;
           üstelik tertemiz ve izsizdi. Mevsim yayı çöktü [DERS 7].
```

---

## 5. ①/③'ÜN "QUESTIONS FOR THE DOCUMENT" CEVAPLARI

```
①-1  Klip 1'e push-in KASITLI DEĞİLDİ. Plan tilt 0°, sıfır hareket diyor.
     → model I2V kilidini tutmadı [DERS 6].
①-2  Klip 2 (çukur) ve klip 7 planlıydı ama klip 7 SAHNE DEĞİL, KAPAK KARTI.
     Çukur istasyonu için çapa ① kadrajda olmalıydı; olmamış [DERS 4 + kart C3].
①-3  HAYIR. Farklı bir bina tasarımı planlanmadı. Klip 7'nin farklı bina
     göstermesi kapak kartının filmden ayrı üretilmiş olmasındandır.

③-1  Klip 1 ters timelapse KANCASI olarak planlandı ve plana risk notu
     yazılmıştı ("ÜRETİM RİSKİ VE GERİ ÇEKİLME PLANI"). Risk gerçekleşti.
③-2  EVET, kış çok yıllık yapının kış fazıydı. Geçiş/erime sahnesi
     PLANLANMAMIŞTI — 6 sahnelik ızgarada yer yoktu [DERS 7].
③-3  Klip başına temsil süresi planda vardı (1 gün / 3 ay / 2 ay / 4 ay /
     3 ay / 1 gün) ama PROMPTA SAYIYLA YAZILMADI, yalnız nesir olarak geçti.
```

---

## 6. ③'ÜN ZAMAN TAHMİNİ — planla karşılaştırma

```
PLAN               14 ay
RAPORUN OKUDUĞU    "about 1.5 to 2 years"
FARK               yaklaşık %30-70 fazla

⭐ Bu tek satır, hiçbir kategorinin yakalayamadığı bir şeyi söylüyor:
   film kendi süresini olduğundan UZUN anlatıyor. Sebep büyük ihtimalle
   mevsim sıçraması — bir kış görüp sonra yaza dönmek, izleyiciye
   "en az iki kış geçti" dedirtiyor.
   Yeni ızgarada (10 sahne) kış İKİ sahne alacak ve erime görünecek.
```

---

## 7. KARAR

```
⛔ v1 YAYINLANMAZ. Tekrar kurgu, tekrar renk, tekrar müzik ONU KURTARMAZ:
   düşen şey teslim değil, ÜRETİM SIRASI.

v2 İÇİN ZORUNLU DEĞİŞİKLİKLER
  ① TERS İNŞA KAPI OLUR — usta kare onaylanmadan hiçbir sahne üretilmez ve
     her sahne bir öncekinin KARESİNDEN türetilir [DERS 5]
  ② TERS AÇILIŞ KALDIRILIR — kanca ileri yönlüdür. Vaadi artık BAŞLIKLI
     KAPAK taşır [DERS 3]
  ③ TESLİM YAPISI BEYAN EDİLİR — sahne bloğu + kapak kartı ayrı [DERS 4]
  ④ IZGARA DEĞİŞİR — 10 sahne × 6 sn + 5 sn kapak = 65 sn
  ⑤ KIŞ İKİ SAHNEYE YAYILIR, erime görünür [DERS 7]
  ⑥ VİNÇ KANCASI ya yüklü ve düşey yazılır ya kadraj dışında kalır [DERS 8]
  ⑦ KAMERA KİLİDİ pozitif ve ÖLÇÜLEBİLİR yazılır [DERS 6]
```

## 8. BU FİLMDEN ÇIKAN DERSLER

`kilavuzlar/DERSLER.md` → **DERS 3 · 4 · 5 · 6 · 7 · 8 · 9**
(9 numaralı ders filmle değil, ③ RUBRİĞİNİN KENDİSİYLE ilgilidir.)
