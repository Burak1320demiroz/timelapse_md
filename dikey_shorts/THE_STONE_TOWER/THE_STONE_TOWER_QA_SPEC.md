# 🔍 THE STONE TOWER — QA ŞARTNAMESİ

> Bu dosya **teslimden önce ölçülecek olanı** tutar. Plan `THE_STONE_TOWER_DIKEY_TIMELAPSE.md`,
> kapak `THE_STONE_TOWER_KAPAK.md`. Buraya üretim bilgisi kopyalanmaz.
> Durum: ⛔ **ÜRETİLMEDİ** — hiçbir mercek koşulmadı, hiçbir sayı ölçülmedi.

---

## 1. ⭐ FİNAL KARE KANITI — 54,0 sn (G7 Usta Kare)

Teslim videosundan 54,0 sn'deki kare alınır ve **dört şey sırayla** aranır:

```
① KULE TAM VE YALNIZ — 8,0 m
            Taç taşı halkası (%81) gökyüzüne karşı kesintisiz durur — 12 yassı capstone.
            Güneye bakan kapı boşluğu ve üzerindeki 1,2 tonluk yekpare lentol taşı net.
            5,0 m seviyesindeki iki dar mazgal pencere açık ve içinden ışık süzülüyor.
            ⛔ Kule eğriyse, taş sıraları erimiş/kaymışsa ya da harçlı derz çizgisi varsa: G7 yeniden.

② SAHA TEMİZ VE İSKELE SÖKÜLMÜŞ — SÖKÜM KANITI
            Hiçbir ahşap iskele dikmesi, kalas, halat, rampa ya da el arabası KADRAJDA KALMAMIŞTIR.
            Taş ocağı çukuru gevşek taş ve toprakla doldurulmuş, yeni otlar yarayı kapatmıştır.
            İskele söküm delikleri taş kırıntısıyla kapatılmıştır.
            ⛔ Kadrajda unutulmuş kalas, merdiven veya alet varsa: G7 yeniden.

③ ÜÇ ARKA PLAN ÇAPASI — TANIKLAR
            · Asırlık zeytin ağacı (sol, %15–25, ~450 px yükseklik, 65 px gövde eni)
            · Ege Denizi ufku (%50 yükseklik, kenardan kenara, iki ada silueti %55 ve %70)
            · Beyaz kireçtaşı çıkıntısı (sağ, %75–85, ~120 px yükseklik)
            ⛔ Çapalardan biri bile 2 px'den fazla kaydıysa kamera sabitliği ihlal edilmiştir: G7 yeniden.

④ MEVSİM DÖNGÜSÜ — LOOP KANITI
            Tepe yüzeyindeki kırmızı-kahve toprak ceplerinde vahşi mor kekik çiçekleri tam çiçek açmıştır
            (S0'ın ilk karesi G0 ile aynı mevsimsel doku — 12 aylık döngünün tamamlandığının kanıtı).
            Akşam altın saati ışığı kulenin batı ve güney yüzünü sıcak kehribar-turuncuya boyar.
```

---

## 2. KADRAJ KİLİTLERİ — sekiz karede ölçülür

| ne | beklenen | tolerans | nerede |
|---|---|:-:|---|
| ufuk çizgisi | %50,00 | ± 1 px | G0…G7 |
| zeytin ağacı gövde eni | 65 px (%6,02) | ± 2 px | G0…G7 |
| zeytin ağacı taç tepesi | %67,00 | ± 3 px | G0…G7 |
| sağ kireçtaşı çıkıntı | %75–85 arası · 120 px | ± 2 px | G0…G7 |
| sol ada silueti | x %55,00 · 40 px | ± 2 px | G0…G7 |
| sağ ada silueti | x %70,00 · 40 px | ± 2 px | G0…G7 |
| kule tabanı (zemin oturumu) | %43,00 | ± 1 px | G0…G7 |
| kule tacı (tamamlanmış taç) | %81,00 | ± 2 px | G5…G7 |
| kapı lentosu üst kotu | %53,00 | ± 2 px | G2…G7 |
| mazgal pencere kotu | %60,00 | ± 2 px | G3…G7 |

```
⛔ Kayma eşiği 2 px · zincir_kontrol.sh ile her halkada denetlenir.
⭐ ÖLÇÜM SIRASI: önce ZEYTİN GÖVDESİNE bak. Zeytin gövdesi 2 px'den fazla kaydıysa kamera oynamış demektir.
```

---

## 3. YAPI VE GEOMETRİ KAPISI — kuru taş fiziği

```
① HARÇSIZ VE ÇELİKSİZ: Hiçbir karede çimento harcı, derz dolgusu, demir donatı, çelik profil görünmez.
   Taşlar yalnızca yerçekimi ve yüzey sürtünmesiyle taş üstüne oturur.
② DARALMA (BATTER): Kule tabanda 3,0 m dış çaptan tepede 2,2 m dış çapa doğru düzenli ~3° daralır.
③ SIRA DÜZENİ: Yatay sıralar düzgün, dikey derzler şaşırtmalı (çapraz kilitli).
④ AĞIR LENTOL: Kapı lentosu tek parça 1,2 tonluk dikdörtgen bloktur; iki uçta en az 15 cm duvara oturur.
⑤ TAÇ HALKASI: 12 yassı taç taşı kulenin üst çemberini kapatır ve kilitler.
```

---

## 4. GEÇİCİ EKİPMAN VE SÖKÜM KAPISI

```
GEÇİCİ EKİPMANLARIN ÖMRÜ:
· Taş ocağı yığını: G0'da büyük yığın → G1 (%66) → G2 (%40) → G3 (%20) → G4 (az) → G5 (bitti) → G6/G7 (düzeltildi)
· Ahşap rampa: Yalnızca S2'de (lentol kaldırma anı) kurulur; S3'te tamamen sökülmüştür.
· Pencere ahşap kalıbı: Yalnızca S3'te (mazgal oluşumu) takılıdır; S4'te sökülmüştür.
· Dış ahşap iskele: S4'te kurulur, S5'te taç için yükselir, S6'da sökülür, G7'de tamamen yok.
· El arabası: S0–S5 arasında görünür, S6'da kaldırılır, G7'de yok.

⛔ BLOCK: Sökülmesi gereken ekipman sonraki sahnede ekranda kalırsa devamlılık kırılır.
```

---

## 5. MEVSİM VE IŞIK DÖNGÜSÜ — 12 Aylık Takvim

```
G0 (Nisan Yıl 1)  : İlkbahar başlangıcı · mor kekik çiçekleri canlı · sabah güneşi 095°
G1 (Mayıs)         : Geç ilkbahar · kekik solar, taze yeşil ot · sabah 118°
G2 (Haziran)       : Erken yaz · otlar sarıya döner · yüksek öğle güneşi 155°
G3 (Ağustos)       : Tam yaz · kavrulmuş altın saman sarısı ot · sıcak öğleden sonra 245°
G4 (Ekim)          : Sonbahar · ilk yağmurlar, nemli koyu toprak, koyu yapraklar · ikindi 135°
G5 (Ocak)          : Kış · ıslak parıldayan taşlar, kış yeşili ot hollowlarda · alçak kış güneşi 195°
G6 (Nisan Yıl 2)  : İkinci ilkbahar · iskele sökümü, sabah güneşi 095°
G7 (Nisan Yıl 2)  : Altın saat teslim · mor kekik tam çiçek açmış · gün batımı 285° (kehribar ışık)

⛔ BLOCK: Mevsim sırası bozulursa (örn. kıştan sonra yaz gelirse) zaman akışı çöker.
```

---

## 6. SAYIM KAPISI [DERS 55]

```
Sekiz karenin her birinde sayılır:
· Kule: 1 adet (ikinci bir kule, baca ya da pilon YOK)
· Zeytin ağacı: 1 adet (ikinci bir büyük ağaç kadrajda YOK)
· Sağ kireçtaşı çıkıntı: 1 adet
· Ada silueti: 2 adet (ufukta sabit siluetler)

⛔ BLOCK: Çevrede beliren modern direk, kablo, yol, araç ya da fazladan yapı.
⛔ BLOCK: Taş, tahta veya aletler üzerinde okunabilir yazı, logo veya marka.
```

---

## 7. MÜZİK VE SES SENKRONU

```
Izgara: 7 sahne × 8,0 sn = 56,0 sn + 5,0 sn kapak = 61,0 sn · 120 BPM (4 ölçü/sahne)
· 0,0 sn  : Taş çekiç vuruşu + rüzgâr uğultusu girişi
· 16,0 sn : Lentol rampada — bas drone derinleşmesi
· 24,0 sn : Lentolün yerine oturuşu — rezonanslı taş-taşa çarpma vuruşu
· 40,0 sn : Kış rüzgârı fırtınası + hızlı taş tıkırtısı
· 48,0 sn : İskele sökümü ve sakinleşme — akustik gitar solo
· 56,0 sn : Kapanış akoru ve deniz dalgası sesi
```

---

## 8. BİLİNEN VE BEKLENEN RİSKLER

```
⚠️ BEYANLI UYARI ×2:
   ① ARAÇ KUTU SETİ henüz ölçülmedi (üretim öncesi zorunlu adım).
   ② Düz ızgara (7 × 8,0 sn) — sahip kararı, metronom riski klip içi dinamizm ile dengelenir.

⚠️ TAŞ DOKUSU VE TUTARLILIK RİSKİ:
   Modelin harç ekleme veya taşları beton blok gibi pürüzsüzleştirme riski vardır.
   Bunu önlemek için YAPI BIBLE ve AT THIS STAGE bloklarında "hand-dressed grey limestone blocks
   laid without mortar" ifadesi her promptta birebir korunmuştur.
```
