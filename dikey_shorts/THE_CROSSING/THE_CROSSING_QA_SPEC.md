# 🔍 THE CROSSING — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM).
> ⛔ ① KARE ve ③ ZAMAN merceklerine **VERİLMEZ** — o ikisi dokümansız koşar.
> Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit değildir; tariftir.

---

## 0. KÜNYE

```
FİLM          THE CROSSING — Deniz Kıyı Köprüsü
FORMAT        9:16 dikey

TESLİM YAPISI ⭐ SAHNE BLOĞU  8 sahne (7.5s/10s/5s) = 60,0 sn   ← merceklerinin konusu
              ⭐ KAPAK KARTI  1 × 5,0 sn            =  5,0 sn   ← SAHNE DEĞİL
                 TOPLAM                                65,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR ve devamlılık
                 karşılaştırmalarına GİRMEZ. Ayrı denetlenir:
                 "kart, S7'deki köprünün AYNISINI mı gösteriyor?"

SAHNE SAATLERİ  S0 0,0-7,5 · S1 7,5-15,0 · S2 15,0-22,5 · S3 22,5-30,0
                S4 30,0-37,5 · S5 37,5-47,5 · S6 47,5-55,0 · S7 55,0-60,0
                KART 60,0-65,0
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez:
   ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
   Ölçülen değer: {4,6,8}

YAPI          kablo askılı köprü · 400 m ana açıklık · pilon 130 m · 32 kablo/pilon
SAHA          kıyı / deniz kabuğu
ZAMAN YAYI    36 ay (3 yıl)
KAMERA        MAIN STATION — sabit tripod (8 sahne)
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G8 usta kare → G7 → ... → G0
```

---

## 1. ⛔ FİNAL VURUŞ KANITI — teslimin tek kapısı

```
SAHNE       S7
SANİYE      0:58,0   (S7'nin 3,0. saniyesi)
GÖRÜLMESİ GEREKEN ŞEY:
   Alacakaranlıkta tamamlanmış 600 metrelik tabliye üzerinde kesintisiz araç far
   ve stop lambası çizgileri akıyor; 64 adet beyaz askı kablosu pilonlardan
   tabliyeye ışıldayarak iniyor, deniz seviyesinde hiçbir inşaat vinci veya
   barge kalmamış.

KOMUT
   ffmpeg -ss 58.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede akan araç ışıkları ve tamamlanmış köprü DEĞİLSE film TESLİM
   EDİLMEMİŞTİR.

⭐ İKİNCİ ZORUNLU KARE — KANIT ÇİFTİ
   ffmpeg -ss 3.5  -i teslim.mp4 -frames:v 1 kanit_s0.jpg
   ffmpeg -ss 58.0 -i teslim.mp4 -frames:v 1 kanit_s7.jpg
   İki karede Basalt Headland, Lighthouse Ridge ve Deniz Ufku tam aynı yerinde durmalı.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION

| Ne | Beklenen Frame Yüzdesi | Tol. | Hangi Sahnelerde |
|---|---|---|---|
| ufuk çizgisi | %48,0 | ±%1.0 | 8 sahnede de (S0-S7) |
| Pilon A tacı | %82,0 | ±%1.5 | S1-S7 |
| Pilon B tacı | %68,0 | ±%1.5 | S2-S7 |
| Tabliye kotu | %48,0 | ±%1.0 | S2-S7 |
| ⭐ KAPANMA NOKTASI | %48,0 | ±%1.0 | S6 · S7 |

```
⛔ ÜST SINIR   hiçbir yapı parçası %87,5'in üstünde olamaz
⛔ ALT SINIR   ilerlemeyi kanıtlayan hiçbir şey %25'in altında olamaz
⛔ SAĞ ŞERİT   kanıt nesnesi kare genişliğinin sağ %13'ünde duramaz
```

---

## 3. ⭐ BOŞLUK (GAP) VE KABLO SAYISI TAKİBİ

Ana açıklık 400 m.

| S | Pilon A Yükseklik | Pilon B Yükseklik | Kablo Sayısı / Pilon | GAP (Açıklık) | Ekranda Görünmesi Gereken İlerleme |
|:-:|---:|---:|---:|---:|---|
| S0 | 0 m | 0 m | 0 | 400 m | Deniz içi temeller (caissons) dökülüyor |
| S1 | 97 m (%75) | 0 m | 0 | 400 m | Pilon A tırmanır kalıpla yükseliyor |
| S2 | 130 m (%100) | 130 m (%100) | 4 çift | 360 m | İkiz pilonlar tamam, starter deck 20 m |
| S3 | 130 m | 130 m | 12 çift | 240 m | Cantilever tabliye ilerlemiş, derrick vinçler ucunda |
| S4 | 130 m | 130 m | 20 çift | 120 m | Gap daralmış, kablo ağı yoğunlaşmış |
| S5 | 130 m | 130 m | 26 çift | 50 m | Fırtına altında 50 m dar yarık kalmış |
| S6 | 130 m | 130 m | 32 çift | **0 m** | ⭐ Closure segment kaynaklandı, kesintisiz tabliye |
| S7 | 130 m | 130 m | 32 çift | **0 m** | Asfalt, aydınlatma, akan araç trafiği |
