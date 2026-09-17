# 🔍 THE NARROW GORGE — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM · ⑥ GEÇİŞ · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER).
> ⛔ ① KARE · ③ ZAMAN · ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET · ⑫ KATILIK merceklerine **VERİLMEZ** — o altısı
> dokümansız koşar [AGENTS değişmez ⑦]. Yorum yok, yalnız ölçülebilir kilitler.

---

## 0. KÜNYE

```
FİLM          THE NARROW GORGE — dar kireçtaşı boğazında beton kemer barajı, mansaptaki kaya sekisinden
FORMAT        9:16 dikey · 1080 × 1920 teslim · 30 fps
              ⛔ KAYNAK KLİPLER EN AZ 2160 × 3840 — kurgu yakınlaşması bunu ZORUNLU kılar (§8)

TESLİM YAPISI ⭐ SAHNE BLOĞU  7 sahne × 8,0 sn = 56,0 sn                  ← merceklerin konusu
              ⛔ KAPAK KARTI  YOK — proje sahibinin kararı (16.09.2026)
                 TOPLAM                           56,0 sn
              Son 2,0 sn = S6'nın tutuşu; sonuç ekranı bundan ibarettir (%3,6).

SAHNE SAATLERİ  S0 0,0–8,0 · S1 8,0–16,0 · S2 16,0–24,0 · S3 24,0–32,0
                S4 32,0–40,0 · S5 40,0–48,0 · S6 48,0–56,0
                (120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · her kesme ölçü başında)
⛔ DÜZ IZGARA   proje sahibinin kilidi. ⑥ METRONOM hükmü BEKLENEN ve KABUL EDİLMİŞ risktir; hüküm
                gelirse "beklenen" diye kaydedilir, yeniden üretim sebebi sayılmaz.
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]:
   ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — her sahne 8,0 sn teslim → en büyük kutu ≥ 9,0 gerekir.

YAPI          çift eğrilikli beton kemer barajı · kret +70,0 m · kapaklı dolusavak · dip savak · enerji kırıcı havuz
SAHA          dar kireçtaşı boğazı — iki duvar + açık kaya bandı + kaya burnu + tek gözlü taş köprü (yeni kart)
ZAMAN YAYI    birkaç yıl mertebesi · takvim KESMELERDE geçer · ışık kurgusu ÜSLUPTUR, süre iddiası değildir
IŞIK          TEK GÜN 05:30 → 19:30 (7 × rejim B = 14,0 saat) ⚠️ beyan edilen üst sınırın TAM üstünde
KAMERA        HOME — tek istasyon · h +25,0 m · D_eksen 94 m · D_köprü 60 m · D_portal 45 m · 0° · tilt 0°
⭐ KURGU       HOME + dört sahnede yakınlaşma (S0 1,55× · S1 2,0× · S3 1,7× · S6 2,0×) · S2 · S4 · S5 sabit
              ⛔ SAHİP KARARI: §1.2 ve P2-l ② geçersiz kılındı, ÖLÇÜLMEDİ (plan §KURGU)
VİNÇ          ⛔ YOK — beton bant konveyör + oluk ile gelir; havada asılı yük yok. Vinç görülürse DAVETSİZ
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G7 usta kare → G6 → … → G0 · her kare zincir_kontrol.sh
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S6
SANİYE      0:55,0   (S6'nın 7,0. saniyesi — son 2,0 sn'lik TUTUŞUN içi · kadraj TAM HOME)
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① İNEN BEYAZ TABAKA: savak dudağından (%80,1) enerji kırıcı havuza (%33) tek parlak düşey bant;
      serpinti ALÇAK kalır ve köprüyü ÖRTMEZ.
   ② TAM BETON GÖVDE: boğazı seyyar hiçbir şey olmadan kapatan kavisli kütle; yatay derz çizgileri ve
      kalıp panel izleri okunur; kalıp YOK, trestle YOK, makine YOK (duvarda ankraj izleri KALIR).
   ③ KÖPRÜ VE ÖLÇÜLÜ AKIŞ: köprünün kemerinin altından geçen ince kol; iki yanda KURU çakıl, söğüt
      kütükleri, KURU değirmen arkı.
   + KÖPRÜ aynı yerde aynı boyda (≈250 px) · kaya bandı ve kaya burnu yerinde ·
     güneş rimin arkasında (az 302°, ufkun 1° altında) — mavi gölge, kare AYDINLIK [DERS 45].

KOMUT       ffmpeg -ss 55.0 -i teslim.mp4 -frames:v 1 final_kanit.jpg
⛔ ÜÇÜ BİRDEN GÖRÜNMÜYORSA TESLİM YOKTUR.
⛔ KADRAJ KAPISI: 0:55,0 karesi TAM HOME olmalı. Yakınlaşma payı kalmışsa (çapalar HOME'daki
   piksellerinde değilse) kurgu düzeltilir — bu bir üretim hatası değil, KURGU hatasıdır.
⚠️ EN SIK BEKLENEN ARIZA: serpintinin kadrajın alt yarısını kaplaması. Serpinti havuz çevresinde kalır.
```

---

## 2. KADRAJ KİLİTLERİ — HOME (f=24 · h=+25,0 · tilt 0 · yüzde = 50 + 66,7·(y−25)/D, ALT kenardan)

```
⛔ Formül YALNIZ HOME için geçerlidir. Yakınlaşmış ara kadrajlara TAŞINMAZ.
⛔ Bu değerler TÜRETİLDİ, ÖLÇÜLMEDİ; usta kare onaylanınca ölçülür ve bu tablonun üstüne yazılır.

| ne | y (m) | D (m) | yüzde (alttan) | px (alttan) |
|---|---:|---:|---:|---:|
| portal ağzı (derivasyon ÇIKIŞI) | +3,0 | 45 | %17,4 | 334 |
| ⭐ köprü tabliyesi | +6,0 | 60 | %28,9 | 555 |
| yatak, baraj ekseninde | 0 | 94 | %32,3 | 620 |
| dip savak ağzı | +4,0 | 94 | %35,1 | 674 |
| gövdenin +6,0 m kotu (fiziksel karşılaştırma) | +6,0 | 94 | %36,5 | 701 |
| ⭐ GÖZ ÇİZGİSİ — S3'ün ilerleme eşiği | +25,0 | 94 | %50,0 | 960 |
| açık kaya bandı (baraj ekseninde) | +40,0 | 94 | %60,6 | 1164 |
| sağ duvar kaya burnu | +58,0 | 85 | %75,9 | 1457 |
| savak dudağı | +67,5 | 94 | %80,1 | 1538 |
| KRET | +70,0 | 94 | %81,9 | 1573 |
| boğaz kenarı / gök yarığı | +80,0 | 94 | %89,0 | 1709 |

⭐ ÖLÇEK ÇAPASI: TAŞ KÖPRÜ ≈250 px en (kadraj eninin yaklaşık dörtte biri) — SEKİZ karede aynı.
   Sapma > 4 px → kare ATILIR.
⛔ EKRAN KANITI UYARISI [eleştiri ④]: baraj tabanı (%32,3) kadrajda köprü tabliyesinden (%28,9) ZATEN
   yukarıdadır. Bu yüzden "beton köprü hizasını geçti" DENETİMİ YAPILMAZ. S3'ün kanıtı betonun
   GÖZ ÇİZGİSİNİ (%50,0) geçmesidir.
⛔ SHORTS UI: alt %0–13 ve sağ %87,5+ ilerleme kanıtı TAŞIMAZ.
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
kret            +70,0 m · kret uzunluğu 46 m · kret genişliği 4,0 m · taban kalınlığı 9,0 m
dolusavak       dudak +67,5 m · açıklık 14 m · iki beton ayak · TEK çelik radyal kapak
dip savak       +4,0 m · çelik gömlekli tek açıklık
enerji kırıcı   gövdenin altında betonarme havuz · son eşikli · S2'de kazılır, G3'ten beri KURU
mesnet          iki duvarda basamaklı kaya yuvası
boğaz           duvarlar +80 m · tabanda 18 m, kret kotunda 46 m · kaya bandı +40,0 m
köprü           tek gözlü taş kemer · tabliye +6,0 m · açıklık 12 m · KALIR
değirmen arkı   sağ kıyı · su alma kotu +4,0 m'nin ÜSTÜNDE → S1'den sonra KALICI KURU
derivasyon      çıkış portali sol duvarda, KÖPRÜNÜN AŞAĞISINDA · ağız +3,0 m · girişi kadraj DIŞINDA
kamera          +25,0 m · D_eksen 94 · D_köprü 60 · D_portal 45 · 24 mm · tilt 0° · bearing 0°
güneş           39°K · haziran sonu (δ +23,4°) — TÜRETİLMİŞ model, saat iddiası değil
```

### Saha durumu — kare kare (② İNŞA · ④ TESLİM · ⑩ SEBEP için)

| G | saat | gövde | su | geçici ekipman | kadraj |
|:-:|---|---|---|---|---|
| G0 | 05:30 | yok | doğal akış, berrak, değirmen arkı akıyor | kırıcı (tool kayada), kamyon, yarım yol | HOME |
| G1 | 07:30 | yok | bulanık doğal akış | kırıcı, ekskavatör, kamyon, portal çentiği | HOME |
| G2 | 09:30 | yok | ⭐ yatak KURU · portaldan plüm · köprünün aşağısı akar | pompalar, ekskavatör, kaya dolgu kapanışı | HOME |
| G3 | 11:30 | tesviye betonu | portal plümü | ekskavatör, kamyon, kuru havuz çukuru | HOME |
| G4 | 13:30 | %50,7 (göz çizgisi geçildi) | portal plümü | kalıp, trestle, konveyör, oluk, kür örtüsü | HOME |
| G5 | 15:30 | TAM · kret + dudak + KAPALI kuru kapak | portal plümü | kalıp (üst katlar), trestle, panel istifi | HOME |
| G6 | 17:30 | TAM, temiz | ⭐ portal KURU · dip savak jeti · köprü altında ölçülü kol | ⛔ yok (ankraj izleri kalır) | HOME |
| G7 | 19:30 | TAM · KAPAK AÇIK | ⭐ dudaktan TABAKA + dip savak + köprü altında akış | ⛔ yok | HOME |

```
⛔ KAPAK KİLİDİ [DERS 56]: radyal kapak G5 ve G6'da TAKILI, KAPALI ve KURU. G0–G4'te kapak YOKTUR
   (S4'te yerleşir). S6'dan önce herhangi bir karede savaktan su gelirse kare ATILIR.
⛔ HAVUZ KİLİDİ [DERS 48]: enerji kırıcı havuz G3'ten itibaren KURU olarak kadrajdadır — su ile
   birlikte belirmez.
⛔ PORTAL KİLİDİ: portal G1'de çentik, G2–G5'te AKAR, G6–G7'de KURU. Ters sırada görülürse ⑧ düşer.
⛔ SÖĞÜT KİLİDİ: G0 yapraklı sıra · G1 sol bariyer kütük · G2'den itibaren bu kesimde kütük ·
   G7'de hâlâ kütük. Söğüt GERİ GELMEZ — bedelin kanıtı budur.
```

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
⭐ AYNI YER NESNESİ   ① TAŞ KÖPRÜ (≈250 px en · tabliye %28,9)
                      ② AÇIK KAYA BANDI (iki duvarda, kadraj ortasına doğru %60,6'ya yakınsar)
                      ③ SAĞ DUVARDAKİ KAYA BURNU (%75,9)
KONTROL               her zincir_kontrol.sh koşusundan SONRA, İKİ karede de ELLE:
                      □ köprü aynı yerde mi (±4 px)  □ aynı boyda mı (±4 px)  □ TEK mi
                      □ kaya bandı aynı kotta ve aynı yakınsamada mı  □ kaya burnu yerinde mi
                      □ gök yarığı %89'da başlıyor mu
⛔ HERHANGİ BİRİ ✗ → KARE ATILIR.
⭐ YAKINLAŞMAYLA İLİŞKİSİ [eleştiri, kamera bölümü]: bu kontrol SEKİZ REFERANS KARESİNDE ve HER
   SAHNENİN İLK/SON KARESİNDE koşar. Yakınlaşmanın ortasındaki karelerde çapaların ekran konumu
   DEĞİŞİR; bu beklenen sonuçtur, ihlal DEĞİLDİR.
⛔ AMA: yakınlaşmış kadrajda da çapalardan EN AZ BİRİ görünür kalmalıdır. Hiçbir çapası olmayan
   yakın kadraj "ikinci istasyon" gibi okunur ve kurgudan çıkarılır.
```

---

## 5. ⑧ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ilk EKSİK görüldüğü kare [DERS 48]

| eleman | kaynağı (kadrajda nereden geldi) | geçici desteği | ilk EKSİK görüldüğü kare | tamamlandığı kare |
|---|---|---|---|---|
| hizmet yolu | sol duvara kesilir | — | G0 (yarım) | G1 |
| derivasyon portali | sol duvarda çentikten açılır | — | G1 (çentik) | G2 |
| kaya dolgu kapanışı | kamyonla, sol yoldan | — | G1 (yok) | G2 |
| temel + mesnetler | kuru yatakta kazılır | — | G2 | G3 |
| enerji kırıcı havuz | kuru yatakta kazılır | — | G2 (yok) | G5 (betonlanmış) |
| bant konveyör + trestle | sol yoldan, parça parça | duvar ankrajları | G3 (yok) | G4 |
| beton gövde | bantla gelir, OLUKTAN düşer | kalıp + braket + kür örtüsü | G3 (tesviye betonu) | G5 |
| savak dudağı + iki ayak | bantla gelen beton | kalıp | G4 (yok) | G5 |
| radyal kapak | sol yoldan, parça parça | mafsal ve ayaklar | G4 (yok) | G5 (kapalı, kuru) |
| dip savak | gövdeye gömülü çelik gömlek | — | G4 (yok) | G5 (kapalı) |

```
⛔ HİÇBİR ELEMAN KADRAJDA BELİRMEZ. Beton BANTLA gelir ve OLUKTAN düşer — kaynağı her karede görünür.
⛔ HİÇBİR ELEMAN KAYBOLMAZ. Giden her şey SOL DUVARDAKİ YOLDAN çıkar [P2-h].
⭐ SÖKÜM SIRASI (S5) SABİTTİR: kalıp → trestle/konveyör → kaya dolgu kapanışı → portal kesilir →
   dip savak açılır. Sıra bozulursa ⑧ düşer.
⭐ EKSİLEN İSTİF: kaya dolgu kapanışı (S5). BÜYÜYEN İSTİF: panel istifi (S5).
```

---

## 6. ⑥ GEÇİŞ — kesme listesi, kadraj ve ses

```
KESMELER    8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0   (hepsi ölçü başında · 120 BPM)
⛔ Her kesmenin İKİ YAKASI AYNI KAREDİR: S(n)'in son karesi = G(n+1) = S(n+1)'in ilk karesi.
⛔ HER KESME TAM HOME'DA OLUR. Yakınlaşmış hâlde kesmeye girilmez, yakınlaşmış hâlden çıkılmaz.
   kesme_kontrol.sh'e ek olarak ELLE: kesmenin iki yakasında da köprü ≈250 px mi.
IŞIK ATLAMAZ  kesmede saat 2 saat ilerler, ışık SÜREKLİDİR: 05:30 → 07:30 → … → 19:30.
              Gölge çizgisi tabloya uyar (sol duvardan iner → taban → sağ duvardan çıkar).
TAKVİM ATLAR  ⭐ S5 → S6 kesmesi haznenin dolduğu AYLARI taşır. Bu bilinçlidir ve plandadır;
              ③ merceği "kesme zaman atladı" derse BEKLENEN sayılır — ışık atlamadığı sürece.
SES         S0 kaya darbesi + ırmak · S1 suyun mikstan çekilmesi (duygusal dip) · S2 en kuru blok ·
            S3 bant + beton · S4 alçak sürdürülen nota · S5 seyrelme, sonra ince su hattı ·
            S6 suyun büyümesi, son 2,0 sn yalnız su
⛔ HER YAKINLAŞMAYA AYNI GEÇİŞ SESİ KONMAZ (whoosh/riser kalıbı yok).
```

---

## 7. ⭐ KURGU KAPISI — bu filme özel (sahip kararı, ÖLÇÜLMEDİ)

```
□ ÇÖZÜNÜRLÜK     kaynak klipler ≥ 2160 × 3840 mı: __  (2,0× için şart · 1,7× için ≥1836×3264 ·
                 1,55× için ≥1674×2976) · büyütme (upscale) sayılmaz
□ HOME DÖNÜŞÜ    S0 · S1 · S3 · S6'nın SON karesi HOME'la birebir mi (çapalar aynı pikselde): __
□ İLERİ DURUM    yakınlaşmadan dönerken inşaat GERİ ALINMIŞ mı: __  ⛔ alınmışsa klip ters
                 oynatılmıştır — TESLİM YOK
□ ÇAPA PAYI      yakın kadrajlarda en az bir çapa görünüyor mu: S1 köprü kemeri · S3 kaya bandı ·
                 S6 derz çizgileri + dudak: __
□ KIRPMA SINIRI  yakın kadraj kaynağın dışına taşıyor mu (boş kenar): __
□ RİTİM          dört yakınlaşmanın hız eğrileri BİRBİRİNİN AYNI mı olmuş: __ (aynıysa düzelt)
□ S6 İKİ AŞAMA   "su başladı" (2,4–3,8) ve "ne kadar büyükmüş" (3,8–6,0) ayrı ayrı okunuyor mu: __
```

---

## 8. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI          ARAC_KARTLARI §4 ölçümleri + ⑨ ÇÖZÜNÜRLÜK + ⑩ KAPAK + ⑪ TABAKA testleri
⛔ ÖN GÖRSELLEŞTİRME    plan + boy kesit (seki · köprü · portal · eksen · savak · havuz · iki duvar)
⛔ YÜZDE VE PİKSELLER   §2 tablosu TÜRETİLMİŞTİR; usta kare onaylanınca ÖLÇÜLÜR ve üstüne yazılır
⛔ YAKINLAŞMA HEDEFLERİ x/y koordinatları G kareleri üretilmeden verilmez
⛔ ÜRETİM GÜNLÜĞÜ       THE_NARROW_GORGE_URETIM_GUNLUGU.md §0 boşken tek kare üretilmez [DERS 28]
```
