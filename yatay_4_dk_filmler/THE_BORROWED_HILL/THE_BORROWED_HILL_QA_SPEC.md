# 🔍 THE BORROWED HILL — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦).
> Plan: `THE_BORROWED_HILL_PLAN.md` · Günlük: `..._URETIM_GUNLUGU.md`

```
FİLM      THE BORROWED HILL · 24 × 10,0 = 240,0 sn · ⛔ KAPAK KARTI YOK
SCENE BLOCK / END CARD    240,0 sn / yok
FORMAT    16:9 · 1920 × 1080 · 30 fps · 25 görsel (G0…G24) + 24 I2V · T2V yok
KADRO     ⛔ İNSAN YOK — "No people are present." 25 promptta da yazılı [DERS 33]
QA BİRİMİ FİLM — on iki mercek TEK master'a bir kez
SAHNE SAATLERİ  06:20 → 19:30 · 5 × B + 19 × A = 13 sa 10 dk
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 238.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① kapalı tümsek — sığınak tamamen gömülü, kron %51,9'da
  ② yanık pencere — hava kilidi portalında tek sıcak leke (≈19 px)
  ③ ⭐ eksilmiş tepe — tacı %44,9'da, uzak krater sırtının (%51,6) ALTINDA

⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 238,0'da kadraj TAM MAIN STATION olmalı: yakınlaşma 238,5'te (klip içi 8,5) bitmiştir.
```

## 2. ⭐ İKİ SİLUET, TEK ÇİZGİ — bu filmin ana ölçümü

| kare | tepe tacı | uzak krater sırtı | hüküm |
|:-:|---|---|---|
| G0 | **%66,9** | %51,6 | tepe çizginin 15,3 puan (165 px) ÜSTÜNDE |
| G21 | %57,3 | %51,6 | hâlâ 5,7 puan (62 px) üstünde |
| G22 | **%44,9** | %51,6 | ⭐ 6,7 puan (72 px) ALTINDA — S21'de geçti |
| G24 | %44,9 | %51,6 | altında · tümsek kronu %51,9'a çıkmış |

```
⛔ UZAK KRATER SIRTI 25 KAREDE DE %51,6'DADIR (±0,5 puan). Bu filmin bütün bedeli
   o çizgiye göre ölçülür; sırt kayarsa ölçüm geçersizdir ve kare ATILIR.
⛔ TEPE ÇAPA DEĞİLDİR: bilerek değişir. ⑤ merceği onu "morphing" sayarsa hüküm
   BEKLENEN kabul edilir — beklenen yükseklikler §3'te sahne sahne yazılıdır.
```

## 3. Kadraj kilitleri

| ne | beklenen | tolerans |
|---|---|---|
| ufuk | %50,0 | ±0,5 puan |
| uzak krater sırtı | %51,6 | ±0,5 puan · 25 karede |
| bazalt kümesi (sağ ön plan) | 120 px geniş | ±15 px · 25 karede |
| anten direği tacı (G7+) | %62,9 | ±1,5 puan |
| tümsek kronu (G22+) | %51,9 | ±1 puan |
| üs zemini | %42,5 | ±1 puan |
| sığınak boyu (G12+) | 539 px | ±30 px |
| hava kilidi portalı (G14+) | 47 px | ±8 px |
| ⭐ pencere (G24) | 19 px | ±5 px · SICAK leke |

### Tepe yüksekliği — sahne sahne (kare · metre · kadraj)

```
G0 16,0 %66,9 · G1 15,7 %66,4 · G2 15,3 %65,8 · G3 14,8 %64,9 · G4 14,5 %64,3
G5 14,1 %63,6 · G6 13,7 %63,1 · G7 13,4 %62,6 · G8 13,2 %62,3 · G9 13,0 %61,9
G10 12,9 %61,7 · G11 12,7 %61,4 · G12 12,6 %61,2 · G13 12,5 %61,0 · G14 12,4 %60,9
G15 10,9 %58,3 · G16 10,8 %58,1 · G17 10,7 %57,9 · G18 10,5 %57,6
⛔ G19 10,5 %57,6 — G18 İLE BİREBİR AYNI (fırtına · iş durdu)
G20 10,4 %57,4 · G21 10,3 %57,3 · G22 3,0 %44,9 · G23 3,0 · G24 3,0
⛔ GERİ GİDİŞ YOK: bir karede alınan malzeme sonraki karede geri gelemez.
```

## 4. ⭐ MALZEME DENGESİ KAPISI [P4-c]

```
KURAL   Tepeden eksilen malzemenin AYNI ya da SONRAKİ sahnede GÖRÜNÜR bir varış
        yeri vardır: stok yığını · yol · pad dolgusu · örtü · berm · red yığını.
        Varış yeri plandaki merdivenin "ALINAN → VARIŞ YERİ" sütununda yazılıdır.
⛔ S18 (fırtına): ocak DURUR. G18 → G19 arasında tepe DEĞİŞMEZ ve fırtınadan sonra
   (G20) tamamlanmış YENİ İŞ görünmez.
⛔ G22'de ocak tabanı DÜZ olmalı ve tepe 3,0 m'lik tek bir kütük bırakmalıdır —
   "kendiliğinden eriyen tepe" arızası budur ve ② merceği bunu yakalar.
HACİM   4.896 − 4.724 = 172 m³ kalır. Defter plandadır.
```

## 5. ⭐ DÜNYA MALZEMESİ ALANI — ters sayaç

```
G0 %100 dolu (kaburga demetleri · panel sandıkları · iki tank · kablo tamburları ·
direk bölümleri) → G12 %30 → G22 %0 boş.
⛔ Yığın ASLA BÜYÜMEZ. Bir sahnede eksilen sandık sonraki sahnede geri gelemez.
⛔ Çelik, panel, kablo ve tank Dünya'dan gelir; ÖRTÜ VE DOLGU tepeden gelir. İkisi
   karışmaz: yığından örtü çıkmaz, tepeden kaburga çıkmaz [P4-d].
```

## 6. ⭐ TEK ÜS KAPISI [DERS 55]

```
SAYIM   sığınak 1 · hava kilidi 1 · anten direği 1 · tank 2 · tepecik 1 — 25 KAREDE
⛔ İkinci bir kubbe, modül kümesi, tank tarlası, silindir dizisi ya da ikinci bir
   tepe = KARE ATILIR.
⛔ Araç kapısının ⑨ SAYIM TESTİ bunu ÜRETİMDEN ÖNCE ölçer; çıkarsa araç değişir.
```

## 7. ⭐ BİLİMKURGU SIZINTISI KAPISI [POLAR HABITAT ölçümü]

```
POLAR HABITAT'ta model, plan dışı mavi lazer ışını, bloom parıltısı ve yıldırım arkı
üretti — tetikleyici "geothermal tower" idi.
⛔ ARANAN: ışık huzmesi · hale · lens parlaması · parlayan panel · enerji arkı ·
   neon kenar · holografik yüzey · plazma. Bunlardan HERHANGİ BİRİ = KARE ATILIR.
✅ TEK MEŞRU IŞIK: G24'te hava kilidi penceresindeki sabit sıcak leke. Huzme YOK,
   hale YOK, yere düşen ışık havuzu YOK — yalnız yanan bir pencere.
⛔ Ve o ışık S23'ten ÖNCEKİ hiçbir promptta anılmaz [DERS 56].
```

## 8. ⭐ KURGU KAPISI — üç an [KAMERA_HAREKETI §3]

```
① ÇÖZÜNÜRLÜK    kaynak ≥ 3840 × 2160 (2,0× için). Upscale sayılmaz.
② ÜÇ AN         S0 (2,0×) · S14 (1,8×) · S23 (2,0×) — BAŞKA HİÇBİR SAHNEDE hareket yok
③ ⛔ S21 SABİT   doruk bir KARŞILAŞTIRMA anıdır; yakınlaşma yükseklik okumasını bozar
④ HOME DÖNÜŞÜ   her üçünde de dönüşte uzak krater sırtı ≤ 4 px kayma
⑤ İLERİ DURUM   dönüşte iş geri alınmaz: kesik kapanmaz, dökülen toprak kalkmaz,
                ışık sönmez. KAPI: klibin son karesi ↔ G(n+1) · zincir_kontrol.sh
⑥ HEDEF         S0 kesit · S14 ilk temas · S23 portal — ⛔ hiçbirinde tepeye ya da
                direğe savrulma yok; her klipte TEK hareket
⑦ S23 ZAMANLAMA ışık 5,0 sn'de yanar; 6,5–8,5 geri çekilme; 8,5–10,0 tam MAIN STATION
```

## 9. Zaman, ışık ve mevsim

```
GÜNEŞ      kadrajda HİÇ görünmez (bakış kuzey, azimut 72°→270°) · disk anılmaz [DERS 39]
GÖLGE      Mars gölgesi ZAYIF ve YUMUŞAK KENARLIDIR — meşrudur, render hatası değil [F1-d]
⛔ AY DİLİ  "no atmospheric haze" ve "shadows absolutely black" Mars'ta FİZİK HATASIDIR
KIŞ        S15 · S16 — iki sahne [DERS 7] · kırağı, SU BİRİKİNTİSİ DEĞİL
FIRTINA    S18 · neden–sonuç: görüş düşer → makineler durur → paneller kirlenir → S19 silinir
TAKVİM     sahadan okunur [P1-c]: iz dolması [F1-a] · panel tozu · kırağı · fırtına
FİNAL      G24 aydınlıktır [DERS 45]; tümsek ve direk son ışıkta, ova gölgede
```

## 10. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM        süreler eşit (24 × 10,0) — formatın bandı ve sahip beyanı
① / ⑤ "istasyon"  S0 · S14 · S23'teki kurgu yakınlaşması istasyon değişimi sayılırsa
                  hüküm BEKLENEN kabul edilir [KAMERA_HAREKETI §9]
⚠️ ÇOĞUL ÜS       beklenen DEĞİL — çıkarsa §6 gereği araç değişir
⚠️ BİLİMKURGU     beklenen DEĞİL — çıkarsa §7 gereği kare atılır
⬜ GÜVENLİ ALAN   16:9 için ÖLÇÜLMEDİ. ⭐ Bu film deponun İLK 16:9 ölçümüdür:
                  ① koşusu üst/alt/sağ üst bantları ölçer ve §2.8'e yazar.
```
