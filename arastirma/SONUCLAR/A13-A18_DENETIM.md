# 🔎 A13–A18 DENETİM — dördüncü kuşak · 17.09.2026

> Kaynak: `A13_BEYANSIZ_HAM.md` … `A18_BEYANSIZ_HAM.md` (altı rapor, tek yapıştırma)
> Yordam: `arastirma/00_README.md §3` — etiket · kaynak sınıfı · çelişki · ölçüm

```
⛔ BU KUŞAĞIN İKİ YAPISAL ZAYIFLIĞI — her maddeden önce okunur
   ① PROMPT YOK. Altı rapor da bu depoda yazılmış bir A<n> promptuna cevap
      değil; sipariş metni bilinmiyor. Neyin SORULDUĞU bilinmiyorsa neyin
      DIŞARIDA BIRAKILDIĞI da bilinmiyor — bu, önceki üç kuşakta olmayan
      yeni bir körlüktür.
   ② KAYNAK ÇÖZÜMLENEMİYOR. Raporlar [cite: n] işaretleri taşıyor ama
      kaynakça YOK. A9–A12'de 12 kaynak çekilebilmişti (7 tuttu, 4 yanlış
      atıf çıktı); burada ÇEKİLECEK BİR ŞEY YOK.
      ⇒ 00_README §3 adım 2b gereği bu kuşaktan kılavuza SAYI İNMEZ.
        İnen şey MEKANİZMA ve KARAR ÇERÇEVESİDİR, rakam değil.
```

---

# 1. ÖLÇTÜM — bu makinede yeniden hesaplanan her şey

## 1.1 A13 · motion-control formülleri — ⭐ YİRMİSİ DE TUTTU

Rapordaki her çalışılmış örnek yeniden hesaplandı (python3, 17.09.2026):

```
T_çekim = N×I · N = T×fps · I = T_çekim/N · D_kare = D_toplam/N
T_simetrik = (2×N_yarı + N_bekleme) × I
→ 20 örneğin 20'si tuttu. İç tutarsızlık YOK.
```

⭐ **Bu, dört kuşakta ilk kez oluyor.** A5–A8'de üç sayı düştü, A9–A12'de gölge
satırı düştü. A13'ün aritmetiği temiz.
⚠️ **Ama bu, iddiaları doğrulamaz.** Formüller tanım gereği tutar (N×I zaten
N×I'dır); tuttuğu şey aritmetik, ölçüm değil. Ve A13'ün tamamı **fiziksel
kamerayı** anlatır — bu depoda fiziksel kamera YOKTUR. Yirmi doğru sayının
yirmisi de burada uygulanamaz. ⇒ `KAMERA_HAREKETI_KILAVUZU §2`

## 1.2 A16 · sapma çarpanı tablosu — 11 satırın 10'u tuttu, 1'i bin kat şişik

```
✅ 10 satır: M = izlenme / kanal ortalaması yeniden hesaplandı, tuttu
❌ DarkLoom "The House on Route 9": 1.200.000 / 25.000 = 48,00x
   RAPOR YAZIYOR: 48.000x   → bin kat hata, üstelik "Mega Outlier" sınıfında
   ve metinde bu satır bir örüntü kanıtı olarak kullanılıyor.
```

⛔ Bir tablonun 10/11'inin tutması, 11.'sini kurtarmaz — çünkü rapor o satırı
**kendisi denetlemedi.** Aynı gözden kaçış, çekilemeyen atıfların hepsinde
olabilir; tek fark, bu satırın çarpması.

## 1.3 A14 · dikey güvenli alan — rakam kendi tablosuyla çelişiyor

```
RAPOR    "1080×1920 tuvalde evrensel güvenli alan ≈ 900×1400 px"
RAPOR    üst marj 150–269 · alt marj 320–672 · sağ marj 84–140

ÖLÇTÜM   en dar marjlarla:   1080−140 = 940  ×  1920−269−672 =  979 px
         en geniş marjlarla: 1080− 84 = 996  ×  1920−150−320 = 1450 px
```

⛔ "900×1400" genişliği EN DAR marjdan, yüksekliği EN GENİŞ marjdan almış —
tek bir cihazda birlikte var olmayan iki değer. Gerçek en kötü hâl **940×979**.
⭐ Bizim zarfımız (`KAMERA_ISTASYONU §6`) zaten daha dar ve DEĞİŞMEZ.

## 1.4 A18 · yüzde tabloları

```
ÖLÇTÜM   kamera AÇISI tablosu toplamı = %102,5  (40 videoda 1 video = %2,5)
         kamera HAREKETİ tablosu toplamı = %97,5
```

İkisi de 100 değil. 40'lık tabana oturuyorlar (her satır %2,5'in katı ✅), yani
tablo uydurma değil — ama bir video iki açıda birden sayılmış ve bir video hiç
sayılmamış. ⇒ yüzdeler **sıralama** olarak okunur, **oran** olarak değil.

## 1.5 A13 §15 · dijital zoom eşiği — ⭐ BİZİM SAYIMIZI DOĞRULADI

```
RAPOR    ">%120 ölçekleme → belirgin pikselleşme"
ÖLÇTÜM   bu eşik 1080×1920 KAYNAK varsayar. 1080×1920 TESLİMDE bozulmasız tavan
         = kaynak_genişliği / 1080:
            1080×1920 → 1,00×      1674×2976 → 1,55×
            1836×3264 → 1,70×      2160×3840 → 2,00×
```

⭐ THE NARROW GORGE'un çözünürlük kapısı (⑨) bu üç sayıyı **bağımsız olarak**
aynı veriyor. Rapor eşiği yanlış değil, **eksik koşullu**: kaynak = teslim
olduğunda doğru. ⇒ `KAMERA_HAREKETI_KILAVUZU §3`

---

# 2. ÇELİŞKİLER — önce okunur [kart S §3]

## 2.1 ⛔ RAPORLAR BİRBİRİYLE ÇELİŞİYOR: sabit kamera kusur mu, imza mı

```
A14  "Tamamen Sabit Kamera: 10. saniyeden sonra izleyici kaybı %40'a ulaşır"
     → sabit kamera bir zayıflık olarak sunuluyor

A18  Aynı yapıdaki veri setinde EN SIK KULLANILAN HAREKET = "Sabit Kamera %27,5"
     ve "Kesin Bulgular" başlığı altında merkez-kilitli SABİT kadraj
     tamamlanma oranının kanıtlanmış mekanizması sayılıyor
```

⛔ Aynı yapıştırmada gelen iki rapor, aynı değişken hakkında ters yönde
konuşuyor. Kart S §4: **iki rapor aynı şeyi farklı söylüyorsa o şey
ÖLÇÜLMEMİŞTİR** — ve bu bilgi, sayının kendisinden değerlidir.
⇒ Format kimliği (`KILAVUZ_REHBERI §1.2`) bu kuşak yüzünden DEĞİŞMEZ.

## 2.2 ⚠️ TERS AÇILIŞ ÜÇÜNCÜ KEZ ÖNERİLDİ

```
A14 · A15  "finali ilk 0,5–1 sn'de flaş kare olarak göster"
BİZDE      DERS 3 ölçtü (ters açılış), P2-l ① bekletti, kart SONDA kaldı [A1-b]
```
⇒ Karar değişmedi. Ama artık **üç ayrı dış kaynak** aynı şeyi söylüyor ve
bizim karşı kaydımız tek bir filmden geliyor. Bu, ölçülmeyi hak eden bir
ayrılıktır — nasıl ölçüleceği `KAMERA_HAREKETI_KILAVUZU §4`'te yazılı.

## 2.3 ⚠️ KESME SIKLIĞI — bizim ızgaramız raporların bandının DIŞINDA

```
A14   Shorts için ideal açı değişimi: 2,5–3,5 sn
A18   Shorts ortalama plan süresi: 1,5–3,5 sn
BİZDE dikey ızgara 6,0 sn · son iki film 8,0 sn
```
⛔ Bandı takip etmek, ızgarayı ikiye katlamak demektir: her kesme yeni bir
anahtar kare + yeni bir klip ister (§2.7). Bedel, film başına iki katı üretim.
⇒ Çözüm kesmeyi sıklaştırmak değil, **kesme olmadan olay üretmektir**
(kurgu yakınlaşması + kadraj içi kinetik). ⇒ `KAMERA_HAREKETI_KILAVUZU §6`

## 2.4 ✅ ÇELİŞMEYEN — ve bizi doğrulayan üç madde

```
A13 §15  dijital zoom PARALAKS ÜRETMEZ; iki boyutlu büyütmedir
         ⇒ bizim kurgu yakınlaşmamız DERİNLİK vaat edemez, yalnız DİKKAT yönetir
A14      kesintisiz kamera hareketi + timelapse hızı = "motion drift" ve doku bozulması
         ⇒ DERS 56 ile aynı yönde (hareket fiili korpus hareketini çağırır)
A18      "Çevre Elemanlarını Sabitleme": nesne değişirken arka plan/ışık sabit
         ⇒ negatif çekirdeğin arka plan cümlesiyle aynı [§7]
```

---

# 3. ETİKET VE KAYNAK SINIFI — madde madde

| Rapor | Konu | Etiket | Kaynak sınıfı | Kılavuza iner mi |
|:-:|---|---|---|---|
| A13 | moco aritmetiği | ÖLÇTÜM (bu makinede) | tanım/aritmetik | ⚠️ yalnız §15 zoom eşiği |
| A13 | ekipman · ND · shutter · reçeteler | İDDİA | ekipman pazarlaması | ⛔ hayır — fiziksel kamera yok |
| A14 | %72–84 bakış oranı · %40 drop-off · %20 retention | İDDİA | çözümlenemiyor | ⛔ hayır |
| A14 | kanca · loop · çıpa-keşif dengesi | VARSAYIM | mekanizma anlatısı | ✅ mekanizma olarak |
| A15 | CTR bantları · %25–30 yüz · "60.000 kat" | İDDİA | pazarlama blogu | ⛔ hayır |
| A15 | MrBeast kapalı ağız A/B testi (Eylül 2023) | İDDİA · adı anılabilir kaynak | ikincil aktarım | ⚠️ yalnız "denenmiş" olarak |
| A15/A17 | Test & Compare mekaniği (3 varyant · izleme süresi payı) | İDDİA · araç dokümanı sınıfı | platform özelliği | ✅ tarif olarak |
| A16 | 108 video · sapma çarpanı | İDDİA (10/11 aritmetik ✅) | çözümlenemiyor | ⚠️ yalnız yöntem |
| A17 | 1280×720 · 2 MB · zaman damgası köşesi | İDDİA · araç dokümanı sınıfı | platform özelliği | ✅ |
| A17 | YZ kapak kusurları (plastik cilt · anatomi · ışık tutarsızlığı) | VARSAYIM | üretim deneyimi | ✅ mekanizma olarak |
| A18 | açı/hareket sıralaması | İDDİA (tablo %102,5) | çözümlenemiyor | ⚠️ sıralama olarak |
| A18 | merkez kilitleme · çevre sabitleme | VARSAYIM | bizim ölçümümüzle aynı yönde | ✅ |

```
⛔ BU KUŞAKTAN İNEN SAYI: BİR TANE.
   Dijital yakınlaşma tavanı = kaynak_genişliği / teslim_genişliği — ve o da
   rapordan değil, bu makinedeki hesaptan indi. Rapor yalnız eşiğin VAR
   olduğunu söyledi; DEĞERİ burada hesaplandı.
```

---

# 4. HEDEF DOSYALAR

```
✅ kilavuzlar/KAMERA_HAREKETI_KILAVUZU.md   ⭐ YENİ — bu kuşağın tek çıktısı
✅ kilavuzlar/MUZIK_VE_KAPAK.md §4          kapak maddeleri (A15 · A16 · A17)
✅ kilavuzlar/DERSLER.md                    DÖRDÜNCÜ KUŞAK · A13-x … A18-x
✅ kilavuzlar/KILAVUZ_REHBERI.md §1         okuma listesine satır
✅ arastirma/00_README.md                   koşu durumu tablosuna altı satır
```
